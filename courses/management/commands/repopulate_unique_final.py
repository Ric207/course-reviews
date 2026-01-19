from django.core.management.base import BaseCommand
from courses.models import Course
import random
from django.db import transaction

class Command(BaseCommand):
    help = "Wipes DB and generates UNIQUE courses with correct grades."

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("Deleting all existing courses..."))
        Course.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Database Cleared."))

        # --- DATA GENERATOR ---
        
        # 1. Define Fields
        FIELDS = {
            'Medicine': ['Medicine & Surgery', 'Dental Surgery', 'Pharmacy', 'Nursing', 'Clinical Medicine', 'Medical Laboratory', 'Radiography', 'Physiotherapy', 'Occupational Therapy', 'Optometry', 'Nutrition & Dietetics', 'Community Health', 'Health Records', 'Medical Engineering', 'Orthopedic Tech'],
            'Engineering': ['Civil', 'Electrical', 'Mechanical', 'Automotive', 'Mechatronic', 'Geospatial', 'Petroleum', 'Aerospace', 'Agricultural', 'Water', 'Structural', 'Telecommunications', 'Biomedical', 'Marine', 'Mining'],
            'ICT': ['Computer Science', 'Information Technology', 'Software Engineering', 'Cyber Security', 'Data Science', 'Business Info Tech', 'Web Development', 'Network Administration', 'Computer Technology', 'Applied Computer Science'],
            'Business': ['Commerce', 'Economics', 'Accounting', 'Finance', 'Marketing', 'Human Resources', 'Supply Chain Mgt', 'Procurement', 'Entrepreneurship', 'Project Management', 'Business Admin', 'Office Mgt', 'International Business'],
            'Law': ['Laws (LLB)', 'Legal Studies', 'Criminology', 'Forensic Science', 'Criminal Justice', 'Security Management'],
            'Education': ['Education (Science)', 'Education (Arts)', 'Early Childhood (ECDE)', 'Special Needs Education', 'Primary Education', 'Guidance & Counseling'],
            'Agriculture': ['Agriculture', 'Agribusiness', 'Horticulture', 'Animal Health', 'Food Science', 'Dairy Tech', 'Soil Science', 'Forestry', 'Fisheries', 'Range Management'],
            'Hospitality': ['Hospitality Management', 'Tourism Management', 'Catering', 'Food & Beverage', 'Tour Guiding', 'Travel Operations', 'Event Management'],
            'Arts': ['International Relations', 'Journalism', 'Mass Communication', 'Public Relations', 'Social Work', 'Psychology', 'Community Development', 'Fashion Design', 'Interior Design', 'Music', 'Fine Arts'],
            'Science': ['Biochemistry', 'Microbiology', 'Biotechnology', 'Actuarial Science', 'Statistics', 'Mathematics', 'Physics', 'Chemistry', 'Biology', 'Geology', 'Meteorology']
        }

        courses_to_create = []
        seen_names = set() # To ensure uniqueness

        self.stdout.write("Generating Unique Courses...")

        # --- DEGREE GENERATION (C+ to A) ---
        # Prefixes make them unique
        degree_prefixes = ["Bachelor of Science in", "Bachelor of", "Bachelor of Technology in", "Bachelor of Arts in"]
        
        for field, specs in FIELDS.items():
            for spec in specs:
                for prefix in degree_prefixes:
                    # Clean up naming logic
                    if "Bachelor" in spec: name = spec # If spec already has Bachelor
                    elif field == "Arts": name = f"Bachelor of Arts in {spec}"
                    elif field == "Science" or field == "Medicine": name = f"Bachelor of Science in {spec}"
                    else: name = f"{prefix} {spec}"

                    if name in seen_names: continue
                    seen_names.add(name)

                    grade = random.choice(['A', 'A-', 'B+', 'B', 'B-', 'C+'])
                    points = 44.0 if grade == 'A' else 38.0 if grade == 'B+' else 26.0

                    courses_to_create.append(Course(
                        name=name, level='Degree', path=field, min_mean_grade=grade, min_cluster_points=points,
                        subject_requirements=f"KCSE {grade} with C+ in relevant subjects.",
                        description=f"A comprehensive Degree program in {spec}. Prepares students for leadership roles.",
                        career_path_info=f"Internship -> Professional {spec} -> Consultant."
                    ))

        # --- DIPLOMA GENERATION (C- to C) ---
        diploma_prefixes = ["Diploma in", "Higher Diploma in", "Advanced Diploma in", "Ordinary Diploma in"]
        
        for field, specs in FIELDS.items():
            for spec in specs:
                for prefix in diploma_prefixes:
                    name = f"{prefix} {spec}"
                    if "Bachelor" in name: name = name.replace("Bachelor of ", "") # Clean up
                    
                    if name in seen_names: continue
                    seen_names.add(name)

                    grade = random.choice(['C', 'C-'])
                    
                    courses_to_create.append(Course(
                        name=name, level='Diploma', path=field, min_mean_grade=grade, min_cluster_points=22.0,
                        subject_requirements=f"KCSE {grade} or Certificate in related field.",
                        description=f"Practical Diploma training in {spec}. Focuses on technical skills.",
                        career_path_info=f"Technician -> Technologist -> Senior Officer."
                    ))

        # --- CERTIFICATE GENERATION (D to D+) ---
        cert_prefixes = ["Certificate in", "Advanced Certificate in", "Craft Certificate in"]
        
        for field, specs in FIELDS.items():
            for spec in specs:
                for prefix in cert_prefixes:
                    name = f"{prefix} {spec}"
                    if "Bachelor" in name: name = name.replace("Bachelor of ", "")

                    if name in seen_names: continue
                    seen_names.add(name)

                    grade = random.choice(['D', 'D+'])
                    
                    courses_to_create.append(Course(
                        name=name, level='Certificate', path=field, min_mean_grade=grade, min_cluster_points=14.0,
                        subject_requirements=f"KCSE {grade}.",
                        description=f"Foundational course in {spec}.",
                        career_path_info=f"Assistant -> Operator -> Further Studies."
                    ))

        # --- ARTISAN GENERATION (E to D-) ---
        # Only specific trade fields usually have Artisan
        artisan_specs = ['Plumbing', 'Masonry', 'Welding', 'Electrical Installation', 'Carpentry', 'Hairdressing', 'Beauty Therapy', 'Sales', 'Storekeeping', 'Agribusiness', 'Motor Vehicle Mechanics']
        artisan_prefixes = ["Artisan in", "Trade Test in", "NITA Grade in"]

        for spec in artisan_specs:
            # Map spec to field
            field = 'Engineering'
            if spec in ['Hairdressing', 'Beauty Therapy']: field = 'Arts'
            if spec in ['Sales', 'Storekeeping']: field = 'Business'
            if spec == 'Agribusiness': field = 'Agriculture'

            for prefix in artisan_prefixes:
                name = f"{prefix} {spec}"
                if name in seen_names: continue
                seen_names.add(name)

                grade = random.choice(['D-', 'E'])
                
                courses_to_create.append(Course(
                    name=name, level='Artisan', path=field, min_mean_grade=grade, min_cluster_points=0.0,
                    subject_requirements="KCSE Certificate or KCPE.",
                    description=f"Skill-based training in {spec}.",
                    career_path_info=f"Apprentice -> Skilled Worker."
                ))

        # --- SAVE ---
        self.stdout.write(f"Saving {len(courses_to_create)} UNIQUE courses to database...")
        with transaction.atomic():
            Course.objects.bulk_create(courses_to_create, batch_size=1000)

        self.stdout.write(self.style.SUCCESS(f"DONE! Database populated with {len(courses_to_create)} unique courses."))
