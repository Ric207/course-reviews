import csv
import os
from django.core.management.base import BaseCommand
from courses.models import Course
from django.conf import settings
from django.db import transaction

class Command(BaseCommand):
    help = "Imports and cleans 'kenya_courses_20000 (1).csv'"

    def handle(self, *args, **kwargs):
        # 1. Setup File Path
        file_path = os.path.join(settings.BASE_DIR, "data", "kenya_courses_20000 (1).csv")

        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"File not found: {file_path}"))
            return

        self.stdout.write(self.style.WARNING("WARNING: This will DELETE existing courses and import new data."))
        
        # 2. Define Helper Functions
        def determine_level(name, raw_level):
            """Fixes the mismatch (e.g. 'B.Sc' labeled as 'Artisan')"""
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
            """Maps CSV fields to your website categories"""
            name = name.lower()
            raw = str(raw_field).lower()
            
            if 'med' in name or 'nurs' in name or 'health' in name or 'pharm' in name: return 'Medicine'
            if 'engin' in name: return 'Engineering'
            if 'comp' in name or 'it' in name or 'software' in name: return 'ICT'
            if 'educ' in name or 'teach' in name: return 'Education'
            if 'law' in name: return 'Law'
            if 'bus' in name or 'comm' in name or 'econ' in name: return 'Business'
            if 'agri' in name: return 'Agriculture'
            
            # Map CSV field names
            if 'engineering' in raw: return 'Engineering'
            if 'it' in raw: return 'ICT'
            if 'education' in raw: return 'Education'
            
            return 'Others'

        def clean_grade(grade, level):
            """Ensures grades match the level"""
            grade = str(grade).strip().upper()
            valid_grades = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'E']
            
            if grade in valid_grades:
                return grade
            
            # If grade is missing or invalid, assign default based on level
            if level == 'Degree': return 'C+'
            if level == 'Diploma': return 'C-'
            if level == 'Certificate': return 'D'
            return 'D-'

        # 3. Process Data
        try:
            courses_to_create = []
            
            self.stdout.write("Deleting old courses...")
            Course.objects.all().delete()

            self.stdout.write(f"Reading {file_path}...")
            
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                
                for row in reader:
                    # Extract raw data using NEW file headers
                    raw_name = row.get('program_name', '').strip()
                    raw_level_col = row.get('level', '')
                    raw_field = row.get('field', '')
                    raw_grade = row.get('min_grade', '')
                    raw_points = row.get('min_cluster_points', '')
                    raw_desc = row.get('description', '')
                    raw_career = row.get('career_info', '')

                    # APPLY FIXING LOGIC
                    final_level = determine_level(raw_name, raw_level_col)
                    final_path = determine_path(raw_name, raw_field)
                    final_grade = clean_grade(raw_grade, final_level)
                    
                    # Fix Points
                    try:
                        final_points = float(raw_points)
                    except:
                        if final_level == 'Degree': final_points = 35.0
                        elif final_level == 'Diploma': final_points = 25.0
                        else: final_points = 0.0

                    # Enrich Description
                    if len(raw_desc) < 20 or "focused on" in raw_desc:
                        final_desc = f"{raw_name} is a comprehensive {final_level} program in the field of {final_path}. It is designed to equip students with market-ready skills."
                    else:
                        final_desc = raw_desc

                    course = Course(
                        name=raw_name,
                        level=final_level,
                        path=final_path,
                        min_mean_grade=final_grade,
                        min_cluster_points=final_points,
                        subject_requirements=row.get('subject_requirements', 'KCSE Certificate'),
                        description=final_desc,
                        career_path_info=raw_career
                    )
                    courses_to_create.append(course)

            # 4. Bulk Insert
            self.stdout.write(f"Importing {len(courses_to_create)} courses...")
            with transaction.atomic():
                Course.objects.bulk_create(courses_to_create, batch_size=1000)

            self.stdout.write(self.style.SUCCESS(f"Successfully imported {len(courses_to_create)} courses!"))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {e}"))
