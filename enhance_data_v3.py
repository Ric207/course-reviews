import csv
import random
import os

# --- 1. MARKET DEMAND RANKING (Most demanding first) ---
# Courses with these words in their 'path' will be ranked higher.
FIELD_PRIORITY = {
    'Medicine': 1,
    'Engineering': 2,
    'ICT': 3,
    'Computer': 3,
    'Law': 4,
    'Business': 5,
    'Economics': 5,
    'Education': 6,
    'Agriculture': 7,
    'Science': 8,
    'Hospitality': 9,
    'Arts': 10
}

# --- 2. DETAILED GRADE DISTRIBUTION ---
# We ensure every grade is represented within its logical level.
DEGREE_GRADES = ['A', 'A-', 'B+', 'B', 'B-', 'C+']
DIPLOMA_GRADES = ['C', 'C-', 'D+']
CERT_GRADES = ['D', 'D-']
ARTISAN_GRADES = ['D-', 'E']

# --- 3. DESCRIPTION COMPONENTS ---
INTROS = {
    'Medicine': [
        "A premier program designed for future healthcare leaders.",
        "Step into the world of advanced medical science and patient care.",
    ],
    'Engineering': [
        "Master the principles of design, innovation, and structural analysis.",
        "This course bridges the gap between theoretical physics and real-world application.",
    ],
    'ICT': [
        "Learn the cutting-edge technologies driving the global digital economy.",
        "Become an expert in software, networks, and modern computing systems.",
    ],
    'Business': [
        "Develop the strategic vision required to lead in the corporate world.",
        "A comprehensive course covering finance, management, and global strategy.",
    ],
    'Default': [
        "A specialized program equipping students with essential industry skills.",
        "This course offers a blend of theoretical knowledge and practical workshops.",
    ]
}

BODIES = [
    "The curriculum focuses on critical thinking, problem-solving, and technical proficiency. Students will engage in hands-on projects that simulate real-world challenges.",
    "You will explore advanced topics and emerging trends in the field. The program emphasizes professional ethics and leadership development.",
    "Through a mix of classroom lectures and field attachment, learners gain the confidence to innovate and excel in competitive environments."
]

CONCLUSIONS = [
    "Graduates are highly sought after by top employers in Kenya and abroad.",
    "This qualification paves the way for a successful career or further academic pursuits.",
    "Prepare yourself for a dynamic career with limitless growth potential."
]

def get_market_rank(path):
    """Returns a rank number (1 is best) based on the field."""
    for key, rank in FIELD_PRIORITY.items():
        if key.lower() in str(path).lower():
            return rank
    return 99 # Low priority for others

def get_random_grade(level):
    """Assigns a specific grade based on level."""
    level = str(level).strip().title()
    if 'Degree' in level:
        return random.choice(DEGREE_GRADES)
    elif 'Diploma' in level:
        return random.choice(DIPLOMA_GRADES)
    elif 'Certificate' in level:
        return random.choice(CERT_GRADES)
    elif 'Artisan' in level:
        return random.choice(ARTISAN_GRADES)
    return 'C'

def generate_description(path):
    """Generates a vivid 3-part description."""
    # Find category
    category = 'Default'
    for key in INTROS.keys():
        if key.lower() in str(path).lower():
            category = key
            break
    
    intro = random.choice(INTROS[category])
    body = random.choice(BODIES)
    conclusion = random.choice(CONCLUSIONS)
    
    return f"OVERVIEW:\n{intro}\n\nDETAILS:\n{body}\n\nCAREER:\n{conclusion}"

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(base_dir, 'data', 'kenya_courses_20000.csv')
    output_file = os.path.join(base_dir, 'data', 'kenya_courses_v3_sorted.csv')

    if not os.path.exists(input_file):
        print("Error: Input file not found.")
        return

    print("Processing, Grading, and Sorting 20,000 courses...")
    
    all_courses = []

    with open(input_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # 1. Clean Data
            row['name'] = row['name'].strip().title()
            row['level'] = row['level'].strip().title()
            row['path'] = row['path'].strip().title()
            
            # 2. Assign Grade
            row['min_mean_grade'] = get_random_grade(row['level'])
            
            # 3. Generate Description
            row['description'] = generate_description(row['path'])
            
            # 4. Calculate Rank (for sorting)
            # We add a temporary 'rank' key to the dictionary
            row['_sort_rank'] = get_market_rank(row['path'])
            
            all_courses.append(row)

    # --- SORTING MAGIC ---
    # Sort by Rank (ascending: 1, 2, 3...) then by Grade (ascending text: A, B...)
    all_courses.sort(key=lambda x: (x['_sort_rank'], x['min_mean_grade']))

    # Write to new file
    with open(output_file, 'w', encoding='utf-8', newline='') as f:
        # Get headers from first row, excluding our temporary sort key
        fieldnames = [k for k in all_courses[0].keys() if k != '_sort_rank']
        
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for row in all_courses:
            del row['_sort_rank'] # Remove the temp key before writing
            writer.writerow(row)

    print(f"Success! Processed {len(all_courses)} courses.")
    print(f"Sorted by Demand (Medicine -> Arts) and saved to: {output_file}")

if __name__ == "__main__":
    main()