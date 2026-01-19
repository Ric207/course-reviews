import csv
import os
from django.core.management.base import BaseCommand
from courses.models import Course
from django.conf import settings
from django.db import transaction

class Command(BaseCommand):
    help = "Cleans duplicates and enforces strict Kenyan grading rules"

    def handle(self, *args, **kwargs):
        # 1. Setup File Path
        file_path = os.path.join(settings.BASE_DIR, "data", "kenya_courses_20000 (1).csv")

        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"File not found: {file_path}"))
            return

        self.stdout.write(self.style.WARNING("WARNING: This will DELETE existing courses and import CLEANED data."))
        confirm = input("Type 'yes' to continue: ")
        if confirm.lower() != 'yes':
            return

        # 2. Define Logic Helpers
        def determine_level(name, raw_level):
            name_lower = name.lower()
            if 'bachelor' in name_lower or 'b.sc' in name_lower or 'b.ed' in name_lower or 'degree' in name_lower:
                return 'Degree'
            if 'diploma' in name_lower:
                return 'Diploma'
            if 'certificate' in name_lower:
                return 'Certificate'
            if 'artisan' in name_lower:
                return 'Artisan'
            # Fallback
            if 'degree' in str(raw_level).lower(): return 'Degree'
            return 'Certificate' 

        def determine_path(name, raw_field):
            name = name.lower()
            raw = str(raw_field).lower()
            if 'med' in name or 'nurs' in name or 'health' in name or 'pharm' in name: return 'Medicine'
            if 'engin' in name: return 'Engineering'
            if 'comp' in name or 'it' in name or 'software' in name: return 'ICT'
            if 'educ' in name or 'teach' in name: return 'Education'
            if 'law' in name: return 'Law'
            if 'bus' in name or 'comm' in name or 'econ' in name: return 'Business'
            if 'agri' in name: return 'Agriculture'
            return 'Others'

        # STRICT KENYAN GRADING RULES
        def get_strict_grade(level):
            if level == 'Degree': return 'C+' # Minimum for Degree
            if level == 'Diploma': return 'C-' # Minimum for Diploma
            if level == 'Certificate': return 'D' # Minimum for Certificate
            return 'D-' # Artisan

        # 3. Process Data
        try:
            # Use a dictionary to track unique course names so we don't add duplicates
            unique_courses = {}
            
            self.stdout.write(f"Reading {file_path}...")
            
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                
                for row in reader:
                    # Extract raw data
                    raw_name = row.get('program_name', '').strip()
                    if not raw_name: continue

                    # Clean Name (remove extra spaces)
                    clean_name = " ".join(raw_name.split())

                    # Skip if we already processed this course name
                    if clean_name in unique_courses:
                        continue

                    # Logic
                    raw_level_col = row.get('level', '')
                    raw_field = row.get('field', '')
                    
                    final_level = determine_level(clean_name, raw_level_col)
                    final_path = determine_path(clean_name, raw_field)
                    final_grade = get_strict_grade(final_level) # FORCE CORRECT GRADE
                    
                    # Fix Points (Estimate based on level if missing)
                    try:
                        final_points = float(row.get('min_cluster_points', 0))
                    except:
                        if final_level == 'Degree': final_points = 30.0
                        elif final_level == 'Diploma': final_points = 20.0
                        else: final_points = 0.0

                    # Enrich Description if generic
                    raw_desc = row.get('description', '')
                    if len(raw_desc) < 20 or "focused on" in raw_desc:
                        final_desc = f"{clean_name} is a {final_level} program in {final_path}. It prepares students for professional roles."
                    else:
                        final_desc = raw_desc

                    # Create Object (in memory)
                    course = Course(
                        name=clean_name,
                        level=final_level,
                        path=final_path,
                        min_mean_grade=final_grade,
                        min_cluster_points=final_points,
                        subject_requirements=row.get('subject_requirements', 'KCSE Certificate'),
                        description=final_desc,
                        career_path_info=row.get('career_info', '')
                    )
                    
                    # Add to dictionary (key = name) to ensure uniqueness
                    unique_courses[clean_name] = course

            # 4. Bulk Insert
            self.stdout.write("Deleting old courses...")
            Course.objects.all().delete()

            self.stdout.write(f"Importing {len(unique_courses)} unique courses...")
            with transaction.atomic():
                Course.objects.bulk_create(unique_courses.values(), batch_size=1000)

            self.stdout.write(self.style.SUCCESS(f"Successfully imported {len(unique_courses)} UNIQUE courses!"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {e}"))