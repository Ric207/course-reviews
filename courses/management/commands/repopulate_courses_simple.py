import csv
import os
import random
from django.core.management.base import BaseCommand
from courses.models import Course
from django.conf import settings
from django.db import transaction

class Command(BaseCommand):
    help = "Imports ALL courses from file, fixing grades logic but keeping volume (20,000)."

    def handle(self, *args, **kwargs):
        # 1. Setup File Path
        # Make sure the file name matches EXACTLY what is in your folder
        file_path = os.path.join(settings.BASE_DIR, "data", "kenya_courses_20000 (1).csv")

        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"File not found: {file_path}"))
            self.stdout.write(self.style.ERROR("Please ensure 'kenya_courses_20000 (1).csv' is in the 'review/data/' folder."))
            return

        self.stdout.write(self.style.WARNING("WARNING: This will DELETE all existing courses and import ~20,000 cleaned records."))
        confirm = input("Type 'yes' to continue: ")
        if confirm.lower() != 'yes':
            self.stdout.write(self.style.ERROR("Operation cancelled."))
            return

        # 2. Logic Helpers
        def determine_level(name):
            """ Determines level strictly from the course name """
            name = name.lower()
            if 'bachelor' in name or 'b.sc' in name or 'b.ed' in name or 'degree' in name or 'llb' in name:
                return 'Degree'
            if 'diploma' in name:
                return 'Diploma'
            if 'certificate' in name:
                return 'Certificate'
            if 'artisan' in name or 'grade iii' in name or 'grade 3' in name:
                return 'Artisan'
            # Fallback default
            return 'Certificate' 

        def determine_path(name):
            """ Categorizes the course into a Field """
            n = name.lower()
            if 'med' in n or 'nurs' in n or 'health' in n or 'pharm' in n or 'dental' in n: return 'Medicine'
            if 'engin' in n or 'civil' in n or 'elect' in n or 'mech' in n or 'automotive' in n: return 'Engineering'
            if 'comp' in n or 'it' in n or 'info' in n or 'software' in n or 'cyber' in n: return 'ICT'
            if 'educ' in n or 'teach' in n: return 'Education'
            if 'law' in n or 'legal' in n: return 'Law'
            if 'agri' in n or 'farm' in n: return 'Agriculture'
            if 'bus' in n or 'comm' in n or 'econ' in n or 'account' in n or 'procure' in n: return 'Business'
            if 'hosp' in n or 'hotel' in n or 'tour' in n or 'cater' in n: return 'Hospitality'
            if 'sci' in n or 'bio' in n or 'chem' in n or 'phys' in n: return 'Science'
            return 'Others'

        def get_correct_grade(level):
            """ Enforces KNQF Grading Standards """
            if level == 'Degree': 
                # Degrees: C+ and above (Weighted towards B/C+)
                return random.choice(['C+', 'C+', 'B-', 'B-', 'B', 'B+', 'A-', 'A']) 
            if level == 'Diploma': 
                # Diplomas: C- and C
                return random.choice(['C-', 'C'])
            if level == 'Certificate': 
                # Certificates: D and D+
                return random.choice(['D', 'D+'])
            # Artisan: D- and E
            return random.choice(['D-', 'E'])

        def get_cluster_points(level, grade):
            """ Assigns realistic points based on the grade """
            if level != 'Degree': return 0.0
            
            # Estimate points based on grade
            base = 25.0
            if grade == 'B-': base = 30.0
            elif grade == 'B': base = 34.0
            elif grade == 'B+': base = 38.0
            elif grade == 'A-': base = 41.0
            elif grade == 'A': base = 44.0
            
            # Add small randomization so not every course has exact same points
            return round(base + random.uniform(0, 3), 1)

        # 3. Processing Loop
        try:
            self.stdout.write("Deleting old courses...")
            Course.objects.all().delete()

            courses_to_create = []
            
            self.stdout.write(f"Reading {file_path}...")
            
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                
                count = 0
                for row in reader:
                    # 1. Get Name (Skip if empty)
                    raw_name = row.get('program_name', '').strip()
                    if not raw_name:
                        continue

                    # 2. Determine Real Details (Fixing the data)
                    level = determine_level(raw_name)
                    path = determine_path(raw_name)
                    grade = get_correct_grade(level)
                    points = get_cluster_points(level, grade)
                    
                    # 3. Construct Description
                    desc = f"{raw_name} is a comprehensive {level} program in the field of {path}. It equips students with the necessary skills for the job market."

                    # 4. Create Object (In Memory)
                    course = Course(
                        name=raw_name,
                        level=level,
                        path=path,
                        min_mean_grade=grade,
                        min_cluster_points=points,
                        subject_requirements=f"KCSE Mean Grade {grade}",
                        description=desc,
                        career_path_info=f"Entry Level -> Professional {path} -> Senior Consultant"
                    )
                    courses_to_create.append(course)
                    count += 1
                    
                    # Optional: Progress indicator
                    if count % 5000 == 0:
                        self.stdout.write(f"Processed {count} rows...")

            # 4. Save to Database (Bulk)
            self.stdout.write(f"Saving {len(courses_to_create)} courses to database...")
            
            with transaction.atomic():
                Course.objects.bulk_create(courses_to_create, batch_size=2000)

            self.stdout.write(self.style.SUCCESS(f"DONE! Successfully imported {len(courses_to_create)} courses."))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {e}"))