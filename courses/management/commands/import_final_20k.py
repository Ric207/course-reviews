import csv
import os
import random
from django.core.management.base import BaseCommand
from courses.models import Course
from django.conf import settings
from django.db import transaction

class Command(BaseCommand):
    help = "Imports ALL 20,000 courses but fixes Grades and Levels to match Kenyan Standards"

    def handle(self, *args, **kwargs):
        # 1. Setup File Path
        file_path = os.path.join(settings.BASE_DIR, "data", "kenya_courses_20000 (1).csv")

        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"File not found: {file_path}"))
            return

        self.stdout.write(self.style.WARNING("WARNING: This will DELETE existing courses and import 20,000 FIXED records."))
        confirm = input("Type 'yes' to continue: ")
        if confirm.lower() != 'yes':
            return

        # --- LOGIC HELPERS ---

        def get_correct_level(name_raw, level_raw):
            """
            Forces the correct Level based on the Course Name.
            Priority: Name > CSV Level column.
            """
            name = name_raw.lower()
            # Strict keyword matching
            if 'bachelor' in name or 'b.sc' in name or 'b.ed' in name or 'degree' in name or 'llb' in name:
                return 'Degree'
            if 'diploma' in name:
                return 'Diploma'
            if 'certificate' in name:
                return 'Certificate'
            if 'artisan' in name or 'grade iii' in name or 'grade 3' in name:
                return 'Artisan'
            if 'masters' in name or 'phd' in name:
                return 'Degree' # Simplify Post-Grad to Degree for sorting
            
            # Fallback to CSV column if name is ambiguous
            if 'degree' in str(level_raw).lower(): return 'Degree'
            if 'diploma' in str(level_raw).lower(): return 'Diploma'
            
            return 'Certificate' # Default safe option

        def get_correct_grade(level):
            """
            Enforces strict Kenyan Qualification Framework (KNQF) grades.
            """
            if level == 'Degree':
                # Degrees MUST be C+ or higher. 
                # We use a weighted choice so C+ and B- are more common than A.
                return random.choice(['C+', 'C+', 'B-', 'B-', 'B', 'B+', 'A-', 'A'])
            
            if level == 'Diploma':
                # Diplomas MUST be C- or C.
                return random.choice(['C-', 'C-', 'C'])
            
            if level == 'Certificate':
                # Certificates are usually D or D+
                return random.choice(['D', 'D+'])
            
            # Artisan is D- or E
            return random.choice(['D-', 'E'])

        def get_realistic_points(level, grade):
            """Assigns cluster points that make sense for the grade."""
            if level == 'Degree':
                # Logic: Higher grade = Higher points
                base = 24.0 # Base points for C+
                if grade == 'B-': base = 30.0
                if grade == 'B': base = 34.0
                if grade == 'B+': base = 38.0
                if grade == 'A-': base = 41.0
                if grade == 'A': base = 44.0
                # Add small random variation
                return round(base + random.uniform(0, 3), 1)
            
            if level == 'Diploma':
                return round(random.uniform(18.0, 26.0), 1)
            
            return 0.0 # Cert/Artisan usually strictly grade-based

        def determine_path(name):
            """Categorizes the course into a Field."""
            n = name.lower()
            if 'med' in n or 'nurs' in n or 'health' in n or 'pharm' in n or 'clinic' in n: return 'Medicine'
            if 'engin' in n or 'civil' in n or 'elect' in n or 'mech' in n or 'automotive' in n: return 'Engineering'
            if 'comp' in n or 'it' in n or 'info' in n or 'software' in n or 'cyber' in n: return 'ICT'
            if 'educ' in n or 'teach' in n: return 'Education'
            if 'law' in n or 'legal' in n: return 'Law'
            if 'agri' in n or 'farm' in n: return 'Agriculture'
            if 'bus' in n or 'comm' in n or 'econ' in n or 'account' in n or 'procure' in n: return 'Business'
            if 'hosp' in n or 'hotel' in n or 'tour' in n or 'cater' in n: return 'Hospitality'
            if 'sci' in n or 'bio' in n or 'chem' in n or 'phys' in n: return 'Science'
            return 'Arts' # Default

        # 4. PROCESS DATA
        try:
            self.stdout.write("Deleting old courses...")
            Course.objects.all().delete()

            courses_to_create = []
            processed_count = 0

            self.stdout.write(f"Reading {file_path}...")
            
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                
                for row in reader:
                    # 1. Get Raw Data
                    raw_name = row.get('program_name', '').strip()
                    if not raw_name: continue # Skip empty rows

                    raw_level_col = row.get('level', '')
                    raw_desc = row.get('description', '')
                    raw_career = row.get('career_info', '')

                    # 2. APPLY FIXES
                    final_level = get_correct_level(raw_name, raw_level_col)
                    final_path = determine_path(raw_name)
                    final_grade = get_correct_grade(final_level)
                    final_points = get_realistic_points(final_level, final_grade)

                    # 3. FIX DESCRIPTION
                    # If description is too short or generic, enhance it
                    if len(raw_desc) < 20 or "focused on" in raw_desc:
                        final_desc = f"{raw_name} is a comprehensive {final_level} program in the field of {final_path}. It equips students with both theoretical knowledge and practical skills required for the job market."
                    else:
                        final_desc = raw_desc

                    # 4. FIX CAREER PATH
                    if len(raw_career) < 5:
                        final_career = f"Entry Level {final_path} Role -> Mid-Level Professional -> Senior Consultant / Manager."
                    else:
                        final_career = raw_career

                    # 5. Create Object
                    course = Course(
                        name=raw_name,
                        level=final_level,
                        path=final_path,
                        min_mean_grade=final_grade,
                        min_cluster_points=final_points,
                        subject_requirements=f"KCSE Mean Grade {final_grade} or equivalent.",
                        description=final_desc,
                        career_path_info=final_career
                    )
                    courses_to_create.append(course)
                    processed_count += 1

                    # Batch insert every 2000 records to manage memory
                    if len(courses_to_create) >= 2000:
                        Course.objects.bulk_create(courses_to_create)
                        self.stdout.write(f"Imported batch... ({processed_count} so far)")
                        courses_to_create = [] # Reset list

            # Insert remaining courses
            if courses_to_create:
                Course.objects.bulk_create(courses_to_create)
            
            self.stdout.write(self.style.SUCCESS(f"DONE! Successfully imported {processed_count} courses."))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {e}"))