import csv
import random
import os

# Define grades suitable for each level
DEGREE_GRADES = ['A', 'A-', 'B+', 'B', 'B-', 'C+']
DIPLOMA_GRADES = ['C', 'C-', 'D+']
CERT_GRADES = ['D', 'D-', 'E']
ARTISAN_GRADES = ['E', 'D-']

def get_random_grade(level):
    level = str(level).lower()
    if 'degree' in level:
        return random.choice(DEGREE_GRADES)
    elif 'diploma' in level:
        return random.choice(DIPLOMA_GRADES)
    elif 'certificate' in level:
        return random.choice(CERT_GRADES)
    elif 'artisan' in level:
        return random.choice(ARTISAN_GRADES)
    return 'Any'

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(base_dir, 'data', 'kenya_courses_20000.csv')
    output_file = os.path.join(base_dir, 'data', 'kenya_courses_fixed.csv')

    if not os.path.exists(input_file):
        print(f"Error: Could not find {input_file}")
        return

    print("Fixing grades in your CSV file...")
    
    with open(input_file, 'r', encoding='utf-8') as f_in, \
         open(output_file, 'w', encoding='utf-8', newline='') as f_out:
        
        reader = csv.DictReader(f_in)
        fieldnames = reader.fieldnames
        writer = csv.DictWriter(f_out, fieldnames=fieldnames)
        writer.writeheader()
        
        count = 0
        for row in reader:
            # Randomize the grade based on the level
            row['min_mean_grade'] = get_random_grade(row['level'])
            
            # Clean up whitespace while we are at it
            row['name'] = row['name'].strip()
            row['level'] = row['level'].strip()
            
            writer.writerow(row)
            count += 1
            
    print(f"Success! Created 'kenya_courses_fixed.csv' with {count} courses.")
    print("Now import this new file using your import script.")

if __name__ == "__main__":
    main()