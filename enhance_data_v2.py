import csv
import random
import os

# --- CONFIGURATION ---
# 1. Realistic Grade Logic
DEGREE_GRADES = ['A', 'A-', 'B+', 'B', 'B-', 'C+']
DIPLOMA_GRADES = ['C', 'C-', 'D+']
CERT_GRADES = ['D', 'D-', 'E']
ARTISAN_GRADES = ['E', 'D-']

# 2. Description Components (To create non-repetitive text)
# We mix and match these to create unique descriptions.

INTROS = {
    'Medicine': [
        "This comprehensive program is designed for students passionate about saving lives and improving community health.",
        "Step into the challenging and rewarding world of healthcare with this rigorous course.",
        "A premier program that combines advanced medical theory with hands-on clinical practice.",
    ],
    'Engineering': [
        "Immerse yourself in the world of innovation, design, and structural analysis.",
        "This course focuses on the practical application of scientific principles to build complex systems.",
        "Designed for future innovators, this program covers the essential foundations of modern engineering.",
    ],
    'ICT': [
        "Master the digital technologies that are shaping the future of the global economy.",
        "This dynamic course offers deep insights into software, networks, and modern computing architecture.",
        "Stay ahead of the curve with a curriculum focused on cutting-edge technology and problem-solving.",
    ],
    'Business': [
        "Develop the strategic mindset and leadership skills required to thrive in the corporate world.",
        "This program offers a blend of economic theory, financial management, and business strategy.",
        "Perfect for aspiring entrepreneurs, this course covers the pillars of modern business management.",
    ],
    'Default': [
        "This specialized course provides students with the essential skills and theoretical knowledge for this profession.",
        "A practical program designed to equip learners with industry-relevant competencies.",
        "Focusing on skill acquisition and career readiness, this course prepares you for the job market.",
    ]
}

BODIES = {
    'Medicine': [
        "You will engage in intensive training covering anatomy, physiology, and patient care ethics. The curriculum is designed to build critical thinking skills required for diagnosis and treatment.",
        "Students will participate in clinical rotations and laboratory work, gaining real-world experience under the guidance of seasoned professionals.",
    ],
    'Engineering': [
        "The curriculum covers project management, technical drawing, and material science. You will learn to design, test, and maintain systems that solve real-world problems.",
        "Through workshops and practical projects, you will develop the technical proficiency needed to oversee large-scale industrial operations.",
    ],
    'ICT': [
        "Key topics include coding, database management, and cybersecurity. You will work on capstone projects that simulate real industry challenges.",
        "The program emphasizes logic, algorithms, and system design, ensuring you are ready to develop scalable software solutions.",
    ],
    'Business': [
        "You will explore modules on marketing, accounting, and human resources. The course encourages analytical thinking and effective decision-making.",
        "Emphasis is placed on real-world case studies, giving you insights into how successful organizations navigate complex markets.",
    ],
    'Default': [
        "The curriculum balances classroom learning with practical workshops, ensuring a holistic educational experience.",
        "Students will cover core concepts and advanced techniques, preparing them for further specialization or immediate employment.",
    ]
}

CONCLUSIONS = [
    "Graduates are highly sought after in both the public and private sectors, with opportunities for rapid career advancement.",
    "Upon completion, you will be fully prepared to enter the workforce or pursue further studies in this field.",
    "This qualification opens doors to a variety of career paths, from consultancy to direct employment in top firms.",
    "Equip yourself with the credentials needed to succeed in a competitive global marketplace.",
    "Join a network of professionals making a tangible difference in this industry."
]

def get_random_grade(level):
    """Returns a realistic grade based on the course level."""
    level = str(level).strip().lower()
    if 'degree' in level:
        return random.choice(DEGREE_GRADES)
    elif 'diploma' in level:
        return random.choice(DIPLOMA_GRADES)
    elif 'certificate' in level:
        return random.choice(CERT_GRADES)
    elif 'artisan' in level:
        return random.choice(ARTISAN_GRADES)
    return 'C'

def generate_vivid_description(name, level, path):
    """Generates a unique, multi-paragraph description."""
    
    # 1. Determine Category
    category = 'Default'
    for key in INTROS.keys():
        if key.lower() in str(path).lower():
            category = key
            break
    
    # 2. Select Random Components
    intro = random.choice(INTROS[category])
    body = random.choice(BODIES[category])
    conclusion = random.choice(CONCLUSIONS)
    
    # 3. Construct the Text with Paragraphs
    # We use specific formatting that looks good in text files
    description = (
        f"COURSE OVERVIEW:\n{intro}\n\n"
        f"WHAT YOU WILL LEARN:\n{body}\n\n"
        f"FUTURE OUTLOOK:\n{conclusion}"
    )
    return description

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(base_dir, 'data', 'kenya_courses_20000.csv')
    output_file = os.path.join(base_dir, 'data', 'kenya_courses_enhanced_v2.csv')

    if not os.path.exists(input_file):
        print(f"Error: Could not find {input_file}")
        return

    print(f"Enhancing data with vivid descriptions...")
    
    with open(input_file, 'r', encoding='utf-8') as f_in, \
         open(output_file, 'w', encoding='utf-8', newline='') as f_out:
        
        reader = csv.DictReader(f_in)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(f_out, fieldnames=fieldnames)
        writer.writeheader()
        
        count = 0
        for row in reader:
            # 1. Clean basic data
            row['name'] = row['name'].strip().title()
            row['level'] = row['level'].strip().title()
            row['path'] = row['path'].strip().title()
            
            # 2. Fix Grade
            row['min_mean_grade'] = get_random_grade(row['level'])
            
            # 3. Generate Vivid, Multi-Paragraph Description
            row['description'] = generate_vivid_description(row['name'], row['level'], row['path'])
            
            writer.writerow(row)
            count += 1
            
    print(f"Success! Enhanced {count} courses.")
    print(f"New file created: {output_file}")

if __name__ == "__main__":
    main()