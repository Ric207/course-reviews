import csv
import os
import random

# --- CONFIGURATION ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(BASE_DIR, 'data', 'kenya_courses_20000 (1).csv') # Use your new uploaded file name
OUTPUT_FILE = os.path.join(BASE_DIR, 'data', 'kenya_courses_final_cleaned.csv')

# --- DATA DICTIONARIES ---

# 1. FIELD DESCRIPTIONS (To replace generic text)
FIELD_DESCS = {
    'Civil': "Focuses on the design, construction, and maintenance of the physical and naturally built environment, including roads, bridges, canals, dams, and buildings.",
    'Electrical': "Covers the physics and mathematics of electricity, electronics, and electromagnetism. Students learn to design complex power systems and electronic circuits.",
    'Computer': "A deep dive into the world of software, algorithms, and data structures. Prepares students for the rapidly evolving tech industry.",
    'Education': "Prepares future educators with pedagogical skills, curriculum development knowledge, and subject mastery to shape the next generation.",
    'Medicine': "A rigorous program covering anatomy, physiology, and clinical practice. Essential for those aspiring to become licensed medical practitioners.",
    'Nursing': "Focuses on patient care, health promotion, and disease prevention. Combines theoretical knowledge with intense practical clinical placements.",
    'Business': "Explores the fundamentals of commerce, finance, marketing, and strategy. Develops the leadership skills needed for the corporate world.",
    'Agriculture': "Combines biology and technology to improve farming practices, food security, and agribusiness management.",
    'Hospitality': "Training in hotel management, culinary arts, and customer service. Ideal for the booming tourism and service industry.",
}

# 2. CAREER PATHS BY LEVEL (To fix generic careers)
CAREERS_BY_LEVEL = {
    'Degree': "Senior Officer -> Manager -> Consultant -> Director. Opportunities in Government, Multi-nationals, and Private Practice.",
    'Diploma': "Technical Assistant -> Technician -> Supervisor -> Senior Officer. High demand in operational and mid-management roles.",
    'Certificate': "Assistant -> Operator -> Skilled Technician. Good entry-level opportunities with room for further studies.",
    'Artisan': "Apprentice -> Skilled Worker -> Foreman -> Self-Employed Contractor. Focus on hands-on, practical trade skills."
}

def clean_row(row):
    """
    Takes a raw row from the CSV and fixes the Level, Grade, and Description logic.
    """
    name = row.get('program_name', '').strip()
    
    # --- 1. FIX LEVEL BASED ON NAME ---
    # The CSV has mismatches (e.g. "B.Sc" labeled as "Artisan"). We trust the NAME.
    new_level = "Certificate" # Default
    if "Bachelor" in name or "B.Sc" in name or "B.Ed" in name or "Degree" in name:
        new_level = "Degree"
    elif "Diploma" in name:
        new_level = "Diploma"
    elif "Artisan" in name:
        new_level = "Artisan"
    elif "Certificate" in name:
        new_level = "Certificate"
    
    # --- 2. FIX GRADE BASED ON NEW LEVEL ---
    # Assign realistic grades
    if new_level == "Degree":
        new_grade = random.choice(['B-', 'B', 'B+', 'A-', 'C+'])
        new_cluster = round(random.uniform(32.0, 43.0), 1)
    elif new_level == "Diploma":
        new_grade = random.choice(['C-', 'C'])
        new_cluster = round(random.uniform(20.0, 28.0), 1)
    elif new_level == "Certificate":
        new_grade = "D+"
        new_cluster = round(random.uniform(15.0, 19.0), 1)
    else: # Artisan
        new_grade = random.choice(['D-', 'E'])
        new_cluster = 0.0

    # --- 3. GENERATE VIVID DESCRIPTION ---
    # Find the best keyword in the name to pick a description
    desc_base = "A comprehensive course designed to provide students with the essential skills and theoretical knowledge required for this profession."
    for key, text in FIELD_DESCS.items():
        if key in name:
            desc_base = text
            break
            
    # Combine with level for context
    final_desc = f"{name} is a {new_level} program. {desc_base} It includes practical workshops and industry exposure."

    # --- 4. FIX CAREER INFO ---
    final_career = CAREERS_BY_LEVEL.get(new_level, "Professional -> Senior -> Expert")

    # --- 5. STANDARDIZE PATH ---
    # Map complex paths to simple ones for the dropdown filter
    raw_field = row.get('field', 'Other')
    if 'Eng' in name: final_path = "Engineering"
    elif 'Med' in name or 'Nurs' in name or 'Health' in name: final_path = "Medicine"
    elif 'Comp' in name or 'IT' in name: final_path = "ICT"
    elif 'Educ' in name: final_path = "Education"
    elif 'Bus' in name or 'Comm' in name: final_path = "Business"
    elif 'Agri' in name: final_path = "Agriculture"
    else: final_path = "General"

    # Return the cleaned data mapped to YOUR model fields
    return {
        'name': name,
        'level': new_level,
        'path': final_path,
        'min_mean_grade': new_grade,
        'min_cluster_points': new_cluster,
        'subject_requirements': row.get('subject_requirements', 'KCSE Certificate'),
        'description': final_desc,
        'career_path_info': final_career
    }

def main():
    if not os.path.exists(INPUT_FILE):
        print(f"Error: File not found at {INPUT_FILE}")
        return

    print("Cleaning and Enriching Data...")
    
    with open(INPUT_FILE, 'r', encoding='utf-8') as f_in, \
         open(OUTPUT_FILE, 'w', encoding='utf-8', newline='') as f_out:
        
        # Read the messy CSV
        reader = csv.DictReader(f_in)
        
        # Write the clean CSV (headers matching your Django Import Script)
        fieldnames = ['name', 'level', 'path', 'min_mean_grade', 'min_cluster_points', 'subject_requirements', 'description', 'career_path_info']
        writer = csv.DictWriter(f_out, fieldnames=fieldnames)
        writer.writeheader()
        
        count = 0
        for row in reader:
            cleaned_row = clean_row(row)
            writer.writerow(cleaned_row)
            count += 1
            
    print(f"✅ Success! Processed {count} courses.")
    print(f"📁 Clean file saved to: {OUTPUT_FILE}")
    print("Next: Update your import script to point to this new file!")

if __name__ == "__main__":
    main()