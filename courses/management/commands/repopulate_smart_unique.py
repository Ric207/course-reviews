from django.core.management.base import BaseCommand
from courses.models import Course
import random
from django.db import transaction

class Command(BaseCommand):
    help = "Generates thousands of UNIQUE courses using Specializations (No Universities)"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("Deleting all existing courses..."))
        Course.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Database Cleared."))

        # --- DATA GENERATOR ENGINE ---

        # 1. Define Core Disciplines
        DISCIPLINES = {
            'Medicine': ['Nursing', 'Pharmacy', 'Clinical Medicine', 'Dental Surgery', 'Public Health', 'Nutrition', 'Radiography', 'Medical Laboratory', 'Physiotherapy', 'Occupational Therapy', 'Community Health', 'Health Records', 'Optometry', 'Orthopedic Technology', 'Medical Engineering', 'Health Systems Mgt', 'Epidemiology', 'Mortuary Science'],
            'Engineering': ['Civil', 'Electrical', 'Mechanical', 'Automotive', 'Mechatronic', 'Geospatial', 'Petroleum', 'Aerospace', 'Chemical', 'Marine', 'Mining', 'Agricultural', 'Water', 'Structural', 'Telecommunications', 'Instrumentation', 'Biomedical', 'Textile', 'Manufacturing', 'Energy'],
            'ICT': ['Computer Science', 'Information Technology', 'Software Engineering', 'Cyber Security', 'Data Science', 'Business Info Tech', 'Network Admin', 'Web Development', 'Mobile App Dev', 'Cloud Computing', 'Artificial Intelligence', 'Computer Forensics', 'Database Mgt', 'System Admin', 'Digital Media'],
            'Business': ['Commerce', 'Economics', 'Accounting', 'Finance', 'Marketing', 'Human Resources', 'Supply Chain', 'Procurement', 'Entrepreneurship', 'Project Management', 'Business Admin', 'Office Management', 'Secretarial Studies', 'International Business', 'Real Estate', 'Insurance', 'Banking', 'Cooperative Mgt'],
            'Education': ['Early Childhood (ECDE)', 'Primary Education', 'Secondary (Arts)', 'Secondary (Science)', 'Special Needs', 'Guidance & Counseling', 'Educational Mgt', 'Physical Education', 'ICT Education', 'Agricultural Education', 'French Education', 'Music Education', 'Religious Studies'],
            'Agriculture': ['General Agriculture', 'Horticulture', 'Agribusiness', 'Animal Health', 'Dairy Tech', 'Food Science', 'Soil Science', 'Forestry', 'Fisheries', 'Wildlife Mgt', 'Range Mgt', 'Agricultural Extension', 'Crop Protection', 'Tea Tech', 'Sugar Tech'],
            'Hospitality': ['Hospitality Mgt', 'Tourism Mgt', 'Catering', 'Food & Beverage', 'Housekeeping', 'Tour Guiding', 'Travel Operations', 'Event Management', 'Cabin Crew', 'Air Travel', 'Hotel Management', 'Culinary Arts', 'Pastry & Baking'],
            'Arts': ['International Relations', 'Journalism', 'Mass Communication', 'Public Relations', 'Criminology', 'Social Work', 'Psychology', 'Community Development', 'Fashion Design', 'Interior Design', 'Music', 'Theatre Arts', 'Film Production', 'Animation', 'Graphic Design', 'Fine Arts', 'Hairdressing', 'Beauty Therapy'],
            'Science': ['Biochemistry', 'Microbiology', 'Biotechnology', 'Actuarial Science', 'Statistics', 'Mathematics', 'Physics', 'Chemistry', 'Biology', 'Environmental Science', 'Geology', 'Meteorology', 'Industrial Chemistry', 'Analytical Chemistry']
        }

        # 2. Define Grade Logic (Strict Kenyan Standards)
        def get_grade_and_points(level):
            if level == 'Degree':
                g = random.choice(['A', 'A-', 'B+', 'B', 'B-', 'C+'])
                p = 44.0 if g == 'A' else 41.0 if g == 'A-' else 38.0 if g == 'B+' else 34.0 if g == 'B' else 30.0 if g == 'B-' else 26.0
                return g, p
            elif level == 'Diploma':
                g = random.choice(['C', 'C-'])
                p = 24.0 if g == 'C' else 20.0
                return g, p
            elif level == 'Certificate':
                g = random.choice(['D+', 'D'])
                p = 16.0 if g == 'D+' else 14.0
                return g, p
            else: # Artisan
                g = random.choice(['D-', 'E'])
                return g, 0.0

        courses_to_create = []
        
        # --- GENERATION LOOPS ---
        
        self.stdout.write("Generating Unique Courses...")

        # LOOP 1: Generate for all Levels and Disciplines
        for field, specs in DISCIPLINES.items():
            for spec in specs:
                
                # 1. DEGREE VARIATIONS
                # e.g. Bachelor of Science in Civil Engineering, Bachelor of Technology in Civil Engineering
                prefixes = ["Bachelor of Science in", "Bachelor of Technology in", "Bachelor of Arts in", "Bachelor of"]
                if field == 'Medicine' or field == 'Science': prefixes = ["Bachelor of Science in"]
                if field == 'Arts': prefixes = ["Bachelor of Arts in"]
                
                for prefix in prefixes:
                    name = f"{prefix} {spec}"
                    # Ensure unique name check in list
                    if not any(c.name == name for c in courses_to_create):
                        g, p = get_grade_and_points('Degree')
                        courses_to_create.append(Course(
                            name=name, level='Degree', path=field, min_mean_grade=g, min_cluster_points=p,
                            subject_requirements=f"KCSE {g} with C+ in relevant subjects.",
                            description=f"A comprehensive Degree program in {spec}. Prepares students for leadership roles.",
                            career_path_info=f"Internship -> Professional {spec} -> Consultant."
                        ))

                # 2. DIPLOMA VARIATIONS
                # e.g. Diploma in Civil Engineering, Higher Diploma in Civil Engineering
                dip_prefixes = ["Diploma in", "Higher Diploma in", "Advanced Diploma in"]
                for prefix in dip_prefixes:
                    name = f"{prefix} {spec}"
                    g, p = get_grade_and_points('Diploma')
                    courses_to_create.append(Course(
                        name=name, level='Diploma', path=field, min_mean_grade=g, min_cluster_points=p,
                        subject_requirements=f"KCSE {g} or Certificate in related field.",
                        description=f"Practical Diploma training in {spec}. Focuses on technical skills.",
                        career_path_info=f"Technician -> Technologist -> Senior Officer."
                    ))

                # 3. CERTIFICATE VARIATIONS
                cert_name = f"Certificate in {spec}"
                g, p = get_grade_and_points('Certificate')
                courses_to_create.append(Course(
                    name=cert_name, level='Certificate', path=field, min_mean_grade=g, min_cluster_points=p,
                    subject_requirements=f"KCSE {g}.",
                    description=f"Foundation course in {spec}.",
                    career_path_info=f"Assistant -> Operator -> Further Studies."
                ))
                
                # 4. ARTISAN VARIATIONS (Only for relevant fields)
                if field in ['Engineering', 'Hospitality', 'Arts', 'Agriculture', 'ICT']:
                    art_name = f"Artisan in {spec}"
                    g, p = get_grade_and_points('Artisan')
                    courses_to_create.append(Course(
                        name=art_name, level='Artisan', path=field, min_mean_grade=g, min_cluster_points=p,
                        subject_requirements="KCSE Certificate or KCPE.",
                        description=f"Skill-based training in {spec}.",
                        career_path_info=f"Apprentice -> Skilled Worker."
                    ))

        # --- SAVING ---
        self.stdout.write(f"Generated {len(courses_to_create)} Unique Courses.")
        
        with transaction.atomic():
            Course.objects.bulk_create(courses_to_create, batch_size=1000)

        self.stdout.write(self.style.SUCCESS("DONE! Database populated with unique, clean data."))