
import csv
from django.core.management.base import BaseCommand
from courses.models import Course
from django.conf import settings
import os

class Command(BaseCommand):
    help = "Import 20,000+ Kenya courses from CSV"

    def handle(self, *args, **kwargs):
        # This script expects your CSV file to be in:
        # review/data/kenya_courses_20000.csv
        file_path = os.path.join(settings.BASE_DIR, "data", "kenya_courses_20000.csv")

        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"File not found at {file_path}"))
            self.stdout.write(self.style.ERROR("Please create a 'data' folder in your 'review' directory and place 'kenya_courses_20000.csv' inside it."))
            return

        self.stdout.write(self.style.NOTICE(f"Importing courses from {file_path}... (This may take a minute or two)"))

        created_count = 0
        updated_count = 0

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                
                for row in reader:
                    # --- This code safely handles missing or bad data ---
                    
                    # 1. Handle cluster points (converts to float, defaults to 0.0)
                    try:
                        cluster_points = float(row.get('min_cluster_points') or 0.0)
                    except (ValueError, TypeError):
                        cluster_points = 0.0 

                    # 2. Get essential data and provide defaults
                    name = row.get('name')
                    level = row.get('level')
                    path = row.get('path')
                    min_grade = row.get('min_mean_grade') or 'Any' # 'Any' is our model default

                    # 3. Skip row if essential data is missing
                    if not name or not level or not path:
                        self.stdout.write(self.style.WARNING(f"Skipping row with missing name/level/path: {name}"))
                        continue

                    # 4. Use get_or_create to prevent duplicates
                    course, created = Course.objects.get_or_create(
                        name=name,
                        defaults={
                            'level': level,
                            'path': path,
                            'min_mean_grade': min_grade,
                            'min_cluster_points': cluster_points,
                            'subject_requirements': row.get('subject_requirements'),
                            'description': row.get('description'),
                            'career_path_info': row.get('career_path_info'),
                        }
                    )
                    
                    if created:
                        created_count += 1
                    else:
                        updated_count += 1

            self.stdout.write(self.style.SUCCESS(f"Successfully finished import."))
            self.stdout.write(self.style.SUCCESS(f"Created: {created_count} new courses."))
            self.stdout.write(self.style.SUCCESS(f"Updated: {updated_count} existing courses."))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"Error: File not found at {file_path}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))
            self.stdout.write(self.style.ERROR("Check if your CSV column headers (name, level, path, etc.) are 100% correct."))