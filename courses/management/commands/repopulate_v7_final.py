from django.core.management.base import BaseCommand
from courses.models import Course
import random
from django.db import transaction

class Command(BaseCommand):
    help = "Generates 20,000+ UNIQUE courses using Advanced Specialization Logic"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("Deleting all existing courses..."))
        Course.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("Database Cleared."))

        courses_to_create = []
        seen_names = set()

        # --- 1. CORE DISCIPLINES & MAJORS ---
        # The base subjects
        MAJORS = {
            'Medicine': ['Nursing', 'Pharmacy', 'Clinical Medicine', 'Dental Surgery', 'Public Health', 'Nutrition & Dietetics', 'Radiography', 'Medical Laboratory Science', 'Physiotherapy', 'Occupational Therapy', 'Community Health', 'Health Records & IT', 'Medical Engineering', 'Optometry', 'Epidemiology', 'Health Systems Management', 'Mortuary Science', 'Medical Psychology', 'Forensic Medicine', 'Biomedical Science'],
            'Engineering': ['Civil Engineering', 'Electrical & Electronics Engineering', 'Mechanical Engineering', 'Automotive Engineering', 'Mechatronic Engineering', 'Geospatial Engineering', 'Petroleum Engineering', 'Aerospace Engineering', 'Agricultural Engineering', 'Water Engineering', 'Structural Engineering', 'Telecommunications Engineering', 'Biomedical Engineering', 'Marine Engineering', 'Mining Engineering', 'Instrumentation & Control', 'Chemical Engineering', 'Industrial Engineering', 'Software Engineering', 'Environmental Engineering', 'Textile Engineering', 'Production Engineering', 'Renewable Energy Engineering'],
            'ICT': ['Computer Science', 'Information Technology', 'Software Engineering', 'Cyber Security', 'Data Science', 'Business Information Technology', 'Web Design & Development', 'Network Administration', 'Computer Technology', 'Applied Computer Science', 'Informatics', 'Library & Information Science', 'Cloud Computing', 'Artificial Intelligence', 'Computer Forensics', 'Mobile App Development', 'Systems Administration', 'Digital Media', 'Animation & Graphics'],
            'Business': ['Commerce', 'Economics', 'Accounting', 'Finance', 'Marketing', 'Human Resource Management', 'Supply Chain Management', 'Procurement & Logistics', 'Entrepreneurship', 'Project Management', 'Business Administration', 'Office Management', 'International Business', 'Real Estate', 'Insurance & Risk Mgt', 'Cooperative Management', 'Strategic Management', 'Operations Management', 'Sales Management'],
            'Education': ['Education (Science)', 'Education (Arts)', 'Early Childhood (ECDE)', 'Special Needs Education', 'Primary Education', 'Guidance & Counseling', 'Agricultural Education', 'Physical Education', 'French Education', 'Music Education', 'Religious Studies Education', 'Home Science Education'],
            'Agriculture': ['General Agriculture', 'Agribusiness Management', 'Horticulture', 'Animal Health & Production', 'Food Science & Technology', 'Dairy Technology', 'Soil Science', 'Forestry', 'Fisheries & Aquatic Sciences', 'Range Management', 'Wildlife Management', 'Dryland Agriculture', 'Crop Protection', 'Tea Technology', 'Sugar Technology', 'Agricultural Economics', 'Veterinary Medicine'],
            'Hospitality': ['Hospitality Management', 'Tourism Management', 'Catering & Accommodation', 'Food & Beverage Production', 'Housekeeping & Laundry', 'Tour Guiding & Administration', 'Travel Operations', 'Event Management', 'Hotel Management', 'Ecotourism', 'Air Travel Operations', 'Cabin Crew', 'Pastry & Baking'],
            'Arts': ['International Relations', 'Journalism', 'Mass Communication', 'Public Relations', 'Social Work', 'Psychology', 'Community Development', 'Fashion Design', 'Interior Design', 'Music', 'Fine Arts', 'Criminology', 'Security Studies', 'Political Science', 'Sociology', 'Gender Studies', 'History', 'Anthropology', 'Philosophy', 'Literature', 'Film Production', 'Performing Arts', 'Sound Engineering', 'Photography'],
            'Science': ['Biochemistry', 'Microbiology', 'Biotechnology', 'Actuarial Science', 'Statistics', 'Mathematics', 'Physics', 'Chemistry', 'Biology', 'Geology', 'Meteorology', 'Environmental Science', 'Industrial Chemistry', 'Analytical Chemistry', 'Botany', 'Zoology', 'Forensic Science', 'Laboratory Technology']
        }

        # --- 2. SPECIALIZATION GENERATOR ---
        # These are added in brackets to create unique variations: "Diploma in ICT (Networking)"
        OPTIONS = {
            'General': ['General', 'Advanced', 'Applied', 'Industrial'],
            'ICT': ['Networking Option', 'Software Dev Option', 'Cyber Security Option', 'Database Mgt Option', 'System Admin Option', 'Cloud Option', 'AI Option'],
            'Business': ['Finance Option', 'Accounting Option', 'Marketing Option', 'HRM Option', 'Insurance Option', 'Banking Option', 'Procurement Option', 'Entrepreneurship Option', 'Operations Option'],
            'Engineering': ['Power Option', 'Telecomm Option', 'Instrumentation Option', 'Structural Option', 'Highway Option', 'Water Option', 'Production Option', 'Plant Option'],
            'Education': ['Math/Physics', 'Bio/Chem', 'Hist/CRE', 'Eng/Lit', 'Kisw/Hist', 'Math/Bus', 'Comp/Math', 'Geog/Bus', 'Bio/Agri'],
            'Agriculture': ['Crop Science Option', 'Animal Science Option', 'Soil Science Option', 'Ag. Econ Option', 'Extension Option'],
            'Media': ['Print Media', 'Broadcast Media', 'Public Relations', 'Advertising', 'Digital Media', 'Film Production'],
            'Hospitality': ['Front Office Option', 'Housekeeping Option', 'F&B Service Option', 'Food Production Option'],
            'Science': ['Pure Option', 'Industrial Option', 'Analytical Option', 'Forensic Option']
        }

        # --- 3. LEVEL PREFIXES ---
        PREFIXES = {
            'Degree': ["Bachelor of Science in", "Bachelor of Arts in", "Bachelor of Technology in", "Bachelor of Education in", "Bachelor of"],
            'Diploma': ["Diploma in", "Higher Diploma in", "Advanced Diploma in", "Ordinary Diploma in", "Professional Diploma in"],
            'Certificate': ["Certificate in", "Advanced Certificate in", "Craft Certificate in", "Proficiency Certificate in"],
            'Artisan': ["Artisan in", "Trade Test Grade I in", "Trade Test Grade II in", "Trade Test Grade III in", "National Vocational Cert in"]
        }

        self.stdout.write("Generating Massive Course Database...")

        # --- GENERATOR FUNCTION ---
        def add_course(name_base, level, path, specialization=None):
            # Construct Name
            name = name_base
            if specialization:
                name = f"{name_base} ({specialization})"
            
            # Clean up
            name = name.replace("Bachelor of Bachelor of", "Bachelor of").strip()
            
            # STRICT UNIQUENESS
            if name in seen_names: 
                return
            seen_names.add(name)

            # Grade & Points Logic (Strict KNQF)
            if level == 'Degree':
                grade = random.choice(['A', 'A-', 'B+', 'B', 'B-', 'C+'])
                if grade == 'A':
                    points = 44.0
                elif grade == 'B+':
                    points = 38.0
                else:
                    points = 26.0
                reqs = f"KCSE Mean Grade {grade} with C+ in relevant subjects."
                duration = "4 Years"
            elif level == 'Diploma':
                grade = random.choice(['C', 'C-'])
                points = 20.0
                reqs = f"KCSE Mean Grade {grade}."
                duration = "2-3 Years"
            elif level == 'Certificate':
                grade = random.choice(['D+', 'D'])
                points = 14.0
                reqs = f"KCSE Mean Grade {grade}."
                duration = "1-2 Years"
            else: # Artisan
                grade = random.choice(['D-', 'E'])
                points = 0.0
                reqs = "KCSE Mean Grade D- or E."
                duration = "6 Months - 1 Year"

            # Construct Description
            desc = f"A comprehensive {level} program in {name}. Designed to provide students with practical skills and theoretical knowledge in {path}. Duration: {duration}."

            courses_to_create.append(Course(
                name=name, 
                level=level, 
                path=path, 
                min_mean_grade=grade, 
                min_cluster_points=points,
                subject_requirements=reqs,
                description=desc,
                career_path_info=f"Entry Level -> Professional -> Expert in {path}."
            ))

        # --- MASTER LOOP ---
        for field, majors in MAJORS.items():
            for major in majors:
                
                # Determine relevant specializations for this major
                specs = OPTIONS['General'].copy() # Default - use copy to avoid mutation
                if field == 'ICT' or 'Computer' in major: 
                    specs += OPTIONS['ICT']
                if field == 'Business' or 'Commerce' in major: 
                    specs += OPTIONS['Business']
                if field == 'Engineering': 
                    specs += OPTIONS['Engineering']
                if field == 'Education': 
                    specs += OPTIONS['Education']
                if field == 'Agriculture': 
                    specs += OPTIONS['Agriculture']
                if field == 'Arts' and ('Media' in major or 'Journalism' in major): 
                    specs += OPTIONS['Media']

                # 1. DEGREES (High Volume)
                for pre in PREFIXES['Degree']:
                    # Logic check to avoid "Bachelor of Arts in Engineering"
                    if field in ['Engineering', 'Medicine', 'Science', 'Agriculture'] and "Arts" in pre: 
                        continue
                    if field in ['Arts', 'Law', 'Education', 'Business', 'Hospitality'] and "Science" in pre: 
                        continue
                    
                    # Add base course
                    add_course(f"{pre} {major}", 'Degree', field)
                    
                    # Add specialized versions (This creates volume!)
                    for spec in specs:
                        add_course(f"{pre} {major}", 'Degree', field, spec)

                # 2. DIPLOMAS
                for pre in PREFIXES['Diploma']:
                    add_course(f"{pre} {major}", 'Diploma', field)
                    for spec in specs:
                        add_course(f"{pre} {major}", 'Diploma', field, spec)

                # 3. CERTIFICATES
                for pre in PREFIXES['Certificate']:
                    add_course(f"{pre} {major}", 'Certificate', field)
                    # Fewer specializations for certs to keep it realistic
                    if random.random() > 0.5: # 50% chance
                        for spec in specs[:3]:
                            add_course(f"{pre} {major}", 'Certificate', field, spec)

                # 4. ARTISAN (Selective)
                if field in ['Engineering', 'Hospitality', 'Agriculture', 'Arts', 'ICT']:
                    for pre in PREFIXES['Artisan']:
                        add_course(f"{pre} {major}", 'Artisan', field)


        # --- SAVE ---
        total = len(courses_to_create)
        self.stdout.write(f"Generated {total} UNIQUE courses.")
        
        # Batch save to handle memory
        batch_size = 2000
        with transaction.atomic():
            for i in range(0, total, batch_size):
                Course.objects.bulk_create(courses_to_create[i:i+batch_size])
                self.stdout.write(f"Saved batch {i} to {i+batch_size}...")

        self.stdout.write(self.style.SUCCESS(f"DONE! Database populated with {total} unique courses."))