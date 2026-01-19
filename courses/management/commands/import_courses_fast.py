#
# This is the full, corrected code for:
# review/courses/management/commands/import_courses_fast.py
#

import csv
from django.core.management.base import BaseCommand
from courses.models import Course
from django.conf import settings
import os
from django.db import transaction

class Command(BaseCommand):
    help = "Imports courses from CSV *very fast*. DELETES ALL EXISTING COURSES FIRST!"

    def handle(self, *args, **kwargs):
        # Make sure this points to your NEW v3 file
        file_path = os.path.join(settings.BASE_DIR, "data", "kenya_courses_CLEANED_v5.csv")

        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"File not found at {file_path}"))
            self.stdout.write(self.style.ERROR("Did you run 'python enhance_data_v3.py' yet?"))
            return

        self.stdout.write(self.style.WARNING(
            "WARNING: This will DELETE all existing courses from your database before importing."
        ))
        
        # Python 3 input function
        confirm = input("Are you sure you want to continue? (yes/no): ")

        if confirm.lower() != 'yes':
            self.stdout.write(self.style.ERROR("Import cancelled."))
            return

        try:
            self.stdout.write("Deleting old courses...")
            with transaction.atomic():
                Course.objects.all().delete()
            self.stdout.write(self.style.SUCCESS("Old courses deleted."))

            self.stdout.write(f"Reading courses from {file_path}...")
            courses_to_create = []
            
            with open(file_path, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        cluster_points = float(row.get('min_cluster_points') or 0.0)
                    except (ValueError, TypeError):
                        cluster_points = 0.0

                    # We strip() all text fields to remove hidden whitespace
                    name = row.get('name', '').strip()
                    level = row.get('level', '').strip()
                    path = row.get('path', '').strip()
                    min_grade = row.get('min_mean_grade', 'Any').strip() or 'Any'
                    
                    if not name or not level or not path:
                        continue
                        
                    course = Course(
                        name=name,
                        level=level,
                        path=path,
                        min_mean_grade=min_grade,
                        min_cluster_points=cluster_points,
                        subject_requirements=row.get('subject_requirements', '').strip(),
                        description=row.get('description', '').strip(),
                        career_path_info=row.get('career_path_info', '').strip(),
                    )
                    courses_to_create.append(course)

            self.stdout.write(f"Importing {len(courses_to_create)} courses in a single batch...")
            with transaction.atomic():
                Course.objects.bulk_create(courses_to_create, batch_size=1000)

            self.stdout.write(self.style.SUCCESS(
                f"Successfully imported {len(courses_to_create)} courses!"
            ))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))
            self.stdout.write(self.style.ERROR("Import failed."))