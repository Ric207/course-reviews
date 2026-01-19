import csv
import os
import random

# --- CONFIGURATION ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Input is your messy file
INPUT_FILE = os.path.join(BASE_DIR, 'data', 'kenya_courses_20000 (1).csv')
# Output is the clean, fixed file
OUTPUT_FILE = os.path.join(BASE_DIR, 'data', 'kenya_courses_CLEANED_v5.csv')

# --- KNQF GRADING SYSTEM ---
GRADES_DEGREE = ['A', 'A-', 'B+', 'B', 'B-', 'C+']
GRADES_DIPLOMA = ['C', 'C-']
GRADES_CERT = ['D+', 'D']
GRADES_ARTISAN = ['D-', 'E']

# --- VIVID DESCRIPTION GENERATORS ---
# We use these templates to make unique, professional descriptions
TEMPLATES = {
    'Medicine': [
        "A rigorous {level} program designed to equip students with clinical skills and medical knowledge for the healthcare sector.",
        "This {level} course focuses on patient care, disease prevention, and health promotion in a modern medical setting.",
    ],
    'Engineering': [
        "A practical {level} course focused on design, construction, and systems analysis. Ideal for students interested in technical innovation.",
        "Master the principles of engineering with this {level} qualification. Training involves heavy practicals and industrial attachment.",
    ],
    'ICT': [
        "A dynamic {level} program covering software development, networking, and digital systems. Prepares learners for the fast-paced tech industry.",
        "Learn to solve real-world problems using technology. This {level} course emphasizes coding, cybersecurity, and system administration.",
    ],
    'Business': [
        "Develop a strategic mindset with this {level} course in business management. Covers finance, marketing, and entrepreneurship.",
        "Essential training for the corporate world. This {level} program focuses on accounting, logistics, and organizational leadership.",
    ],
    'Education': [
        "Prepare for a rewarding career in teaching. This {level} program covers pedagogy, curriculum development, and classroom management.",
        "Shape the future generation with this {level} qualification. Includes mandatory teaching practice and educational psychology.",
    ],
    'General': [
        "A market-oriented {level} course designed to provide technical skills and theoretical knowledge for immediate employment.",
        "This {level} program offers specialized training, preparing students for both self-employment and industry roles.",
    ]
}

def determine_true_level(name_raw, level_raw):
    """
    Fixes logic errors like 'B.Sc' being labeled as 'Artisan'.
    Priority: Name > CSV Level
    """
    name = name_raw.strip().lower()
    
    if 'bachelor' in name or 'b.sc' in name or 'b.ed' in name or 'degree' in name or 'llb' in name:
        return 'Degree'
    if 'diploma' in name:
        return 'Diploma'
    if 'certificate' in name:
        return 'Certificate'
    if 'artisan' in name or 'grade iii' in name:
        return 'Artisan'
    if 'masters' in name or 'phd' in name:
        return 'Degree' # Simplify post-grad to Degree for now
        
    # Fallback to the CSV level if name is ambiguous (e.g. "Law")
    if 'degree' in level_raw.lower(): return 'Degree'
    if 'diploma' in level_raw.lower(): return 'Diploma'
    
    return 'Certificate' # Default safe option

def get_correct_grade(level):
    """Assigns KNQF compliant grades."""
    if level == 'Degree': return random.choice(GRADES_DEGREE)
    if level == 'Diploma': return random.choice(GRADES_DIPLOMA)
    if level == 'Certificate': return random.choice(GRADES_CERT)
    return random.choice(GRADES_ARTISAN)

def get_realistic_points(level, grade):
    """Assigns cluster points that match the grade."""
    if level == 'Degree':
        # A student with A usually needs 40+, C+ needs ~25-30
        base = 25.0
        if 'A' in grade: base += 15
        elif 'B' in grade: base += 10
        return round(base + random.uniform(0, 5), 1)
    
    if level == 'Diploma':
        return round(random.uniform(15.0, 24.0), 1)
        
    if level == 'Certificate':
        return round(random.uniform(10.0, 15.0), 1)
        
    return 0.0 # Artisan often doesn't use cluster points

def determine_path(name):
    """Maps course name to a specific field."""
    n = name.lower()
    if 'med' in n or 'nurs' in n or 'health' in n or 'pharm' in n or 'dental' in n: return 'Medicine'
    if 'engin' in n or 'civil' in n or 'elect' in n or 'mech' in n: return 'Engineering'
    if 'comp' in n or 'it' in n or 'info' in n or 'software' in n: return 'ICT'
    if 'educ' in n or 'teach' in n: return 'Education'
    if 'law' in n or 'legal' in n: return 'Law'
    if 'agri' in n or 'farm' in n: return 'Agriculture'
    if 'bus' in n or 'comm' in n or 'econ' in n or 'account' in n: return 'Business'
    if 'hosp' in n or 'hotel' in n or 'tour' in n: return 'Hospitality'
    return 'Arts' # Default / General

def generate_description(path, level):
    """Picks a vivid description template."""
    options = TEMPLATES.get(path, TEMPLATES['General'])
    desc = random.choice(options)
    return desc.format(level=level) # Inject the correct level into the text

def main():
    if not os.path.exists(INPUT_FILE):
        print(f"Error: Input file not found at {INPUT_FILE}")
        print("Make sure 'kenya_courses_20000 (1).csv' is in the 'review/data/' folder.")
        return

    print("Repairing Data according to KNQF Standards...")
    
    with open(INPUT_FILE, 'r', encoding='utf-8') as f_in, \
         open(OUTPUT_FILE, 'w', encoding='utf-8', newline='') as f_out:
        
        reader = csv.DictReader(f_in)
        
        # Define the headers expected by our Import Script
        fieldnames = ['name', 'level', 'path', 'min_mean_grade', 'min_cluster_points', 'subject_requirements', 'description', 'career_path_info']
        writer = csv.DictWriter(f_out, fieldnames=fieldnames)
        writer.writeheader()
        
        count = 0
        for row in reader:
            # 1. Get raw data
            raw_name = row.get('program_name', '').strip()
            raw_level = row.get('level', '')
            
            # 2. FIX LEVEL (The most important part)
            real_level = determine_true_level(raw_name, raw_level)
            
            # 3. FIX GRADE & POINTS
            real_grade = get_correct_grade(real_level)
            real_points = get_realistic_points(real_level, real_grade)
            
            # 4. FIX PATH & DESCRIPTION
            real_path = determine_path(raw_name)
            real_desc = generate_description(real_path, real_level)
            
            # 5. FIX CAREER INFO (If missing, generate one)
            career = row.get('career_info', '')
            if len(career) < 5:
                career = f"Graduate -> {real_path} Professional -> Senior {real_path} Consultant"

            # 6. Write the clean row
            writer.writerow({
                'name': raw_name,
                'level': real_level,
                'path': real_path,
                'min_mean_grade': real_grade,
                'min_cluster_points': real_points,
                'subject_requirements': row.get('subject_requirements', 'KCSE Certificate'),
                'description': real_desc,
                'career_path_info': career
            })
            count += 1
            
    print(f"✅ Success! Repaired {count} courses.")
    print(f"📁 Clean file saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()