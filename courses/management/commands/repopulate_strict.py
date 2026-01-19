from django.core.management.base import BaseCommand
from courses.models import Course
import random
from django.db import transaction

class Command(BaseCommand):
    help = "Wipes DB and generates strictly UNIQUE courses (No Duplicates)."

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("Deleting all existing courses..."))
        Course.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Database Cleared."))

        # --- DATA DEFINITIONS ---
        
        FIELDS = {
            'Medicine': ['Medicine & Surgery', 'Dental Surgery', 'Pharmacy', 'Nursing', 'Clinical Medicine', 'Medical Lab Science', 'Radiography', 'Physiotherapy', 'Occupational Therapy', 'Nutrition & Dietetics', 'Community Health', 'Health Records', 'Medical Engineering', 'Orthopedic Tech', 'Optometry'],
            'Engineering': ['Civil', 'Electrical', 'Mechanical', 'Automotive', 'Mechatronic', 'Geospatial', 'Petroleum', 'Aerospace', 'Agricultural', 'Water', 'Structural', 'Telecommunications', 'Biomedical', 'Marine', 'Mining', 'Instrumentation'],
            'ICT': ['Computer Science', 'Information Technology', 'Software Engineering', 'Cyber Security', 'Data Science', 'Business Info Tech', 'Web Development', 'Network Admin', 'Computer Tech', 'Cloud Computing'],
            'Business': ['Commerce', 'Economics', 'Accounting', 'Finance', 'Marketing', 'Human Resources', 'Supply Chain', 'Procurement', 'Entrepreneurship', 'Project Management', 'Business Admin', 'Office Mgt'],
            'Law': ['Laws (LLB)', 'Legal Studies', 'Criminology', 'Forensic Science', 'Security Management', 'Penology'],
            'Education': ['Education (Science)', 'Education (Arts)', 'Early Childhood (ECDE)', 'Special Needs', 'Primary Education'],
            'Agriculture': ['Agriculture', 'Agribusiness', 'Horticulture', 'Animal Health', 'Food Science', 'Dairy Tech', 'Soil Science'],
            'Hospitality': ['Hospitality Mgt', 'Tourism Mgt', 'Catering', 'Food & Beverage', 'Tour Guiding', 'Event Management'],
            'Arts': ['International Relations', 'Journalism', 'Mass Communication', 'Public Relations', 'Social Work', 'Psychology', 'Fashion Design', 'Interior Design'],
            'Science': ['Biochemistry', 'Microbiology', 'Biotechnology', 'Actuarial Science', 'Statistics', 'Mathematics', 'Physics', 'Chemistry', 'Biology']
        }

        courses_to_create = []
        # THIS SET PREVENTS DUPLICATES
        existing_names = set()

        self.stdout.write("Generating Unique Courses...")

        # --- 1. DEGREE GENERATION ---
        prefixes = ["Bachelor of Science in", "Bachelor of Arts in", "Bachelor of"]
        for field, specs in FIELDS.items():
            for spec in specs:
                # Generate 1 unique degree name per spec
                if field in ['Medicine', 'Science', 'Engineering', 'Agriculture']:
                    name = f"Bachelor of Science in {spec}"
                elif field in ['Arts', 'Law', 'Education']:
                    name = f"Bachelor of Arts in {spec}"
                else:
                    name = f"Bachelor of {spec}"
                
                # Cleanup
                name = name.replace("in Bachelor of", "in").replace("Science in Medicine & Surgery", "Medicine & Surgery")

                if name not in existing_names:
                    grade = random.choice(['A', 'A-', 'B+', 'B', 'B-', 'C+'])
                    points = 40.0 if grade in ['A', 'A-'] else 30.0
                    courses_to_create.append(Course(
                        name=name, level='Degree', path=field, min_mean_grade=grade, min_cluster_points=points,
                        subject_requirements=f"KCSE {grade} with C+ in relevant subjects.",
                        description=f"A comprehensive Degree in {spec}.",
                        career_path_info="Professional -> Senior Consultant."
                    ))
                    existing_names.add(name)

        # --- 2. DIPLOMA GENERATION ---
        for field, specs in FIELDS.items():
            for spec in specs:
                name = f"Diploma in {spec}"
                if name not in existing_names:
                    grade = random.choice(['C', 'C-'])
                    courses_to_create.append(Course(
                        name=name, level='Diploma', path=field, min_mean_grade=grade, min_cluster_points=20.0,
                        subject_requirements=f"KCSE {grade}.",
                        description=f"Technical Diploma training in {spec}.",
                        career_path_info="Technician -> Supervisor."
                    ))
                    existing_names.add(name)

        # --- 3. CERTIFICATE GENERATION ---
        for field, specs in FIELDS.items():
            for spec in specs:
                name = f"Certificate in {spec}"
                if name not in existing_names:
                    grade = random.choice(['D+', 'D'])
                    courses_to_create.append(Course(
                        name=name, level='Certificate', path=field, min_mean_grade=grade, min_cluster_points=14.0,
                        subject_requirements=f"KCSE {grade}.",
                        description=f"Foundational certificate in {spec}.",
                        career_path_info="Assistant -> Operator."
                    ))
                    existing_names.add(name)

        # --- 4. ARTISAN GENERATION ---
        artisan_specs = ['Plumbing', 'Masonry', 'Welding', 'Carpentry', 'Hairdressing', 'Beauty Therapy', 'Sales', 'Agribusiness', 'Motor Vehicle Mechanics', 'Electrical Installation']
        for spec in artisan_specs:
            name = f"Artisan in {spec}"
            field = 'Engineering'
            if spec in ['Hairdressing', 'Beauty Therapy']: field = 'Arts'
            if spec == 'Sales': field = 'Business'
            
            if name not in existing_names:
                courses_to_create.append(Course(
                    name=name, level='Artisan', path=field, min_mean_grade=random.choice(['D-', 'E']), min_cluster_points=0.0,
                    subject_requirements="KCSE Certificate or KCPE.",
                    description=f"Hands-on trade skill in {spec}.",
                    career_path_info="Apprentice -> Skilled Worker."
                ))
                existing_names.add(name)

        # --- SAVE ---
        self.stdout.write(f"Saving {len(courses_to_create)} UNIQUE courses...")
        with transaction.atomic():
            Course.objects.bulk_create(courses_to_create)

        self.stdout.write(self.style.SUCCESS("DONE! No duplicates exist."))