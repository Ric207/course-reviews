import csv
import os

# Define file paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INPUT_FILE = os.path.join(BASE_DIR, 'data', 'kenya_courses_20000.csv')
OUTPUT_FILE = os.path.join(BASE_DIR, 'all_courses_cleaned.txt')

def clean_text(text):
    """Removes hidden spaces and fixes formatting."""
    if not text:
        return "N/A"
    # Remove surrounding whitespace
    text = str(text).strip()
    # Replace multiple internal spaces with a single space
    text = " ".join(text.split())
    return text

def format_course(row):
    """Formats a single course entry vividly."""
    # 1. Clean and standardize data
    name = clean_text(row.get('name'))
    
    # Fix Level: Ensure "Degree", "Diploma" (Title Case)
    level_raw = clean_text(row.get('level'))
    level = level_raw.title() 
    
    # Fix Path: Title Case
    path = clean_text(row.get('path')).title()
    
    # Fix Grade: Uppercase (e.g., 'c+' -> 'C+')
    grade = clean_text(row.get('min_mean_grade')).upper()
    
    # Fix Cluster Points
    try:
        cp_val = float(row.get('min_cluster_points', 0))
        cluster = f"{cp_val:.1f}"
    except:
        cluster = "0.0"

    subjects = clean_text(row.get('subject_requirements'))
    desc = clean_text(row.get('description'))
    career = clean_text(row.get('career_path_info'))

    # 2. Create the formatted string
    entry = (
        f"====================================================================\n"
        f"COURSE TITLE: {name}\n"
        f"====================================================================\n"
        f"• Level:           {level}\n"
        f"• Field of Study:  {path}\n"
        f"• Minimum Grade:   {grade}\n"
        f"• Cluster Points:  {cluster}\n"
        f"--------------------------------------------------------------------\n"
        f"SUBJECT REQUIREMENTS:\n"
        f"{subjects}\n"
        f"--------------------------------------------------------------------\n"
        f"COURSE DESCRIPTION:\n"
        f"{desc}\n"
        f"--------------------------------------------------------------------\n"
        f"CAREER PATH & OPPORTUNITIES:\n"
        f"{career}\n"
        f"====================================================================\n\n"
    )
    return entry

def main():
    print(f"Reading from: {INPUT_FILE}")
    
    if not os.path.exists(INPUT_FILE):
        print("Error: Input CSV file not found. Make sure it is in the 'data' folder.")
        return

    try:
        with open(INPUT_FILE, 'r', encoding='utf-8') as f_in:
            reader = csv.DictReader(f_in)
            
            print("Processing courses... (This handles all 20,000 entries)")
            
            with open(OUTPUT_FILE, 'w', encoding='utf-8') as f_out:
                # Write a header
                f_out.write("FULL LIST OF REGISTERED COURSES (CLEANED & VERIFIED)\n")
                f_out.write("Generated from database. Errors fixed: Whitespace, Capitalization, Formatting.\n\n")
                
                count = 0
                for row in reader:
                    formatted_entry = format_course(row)
                    f_out.write(formatted_entry)
                    count += 1
                    
                    if count % 1000 == 0:
                        print(f"Processed {count} courses...")

        print(f"\nSuccess! All {count} courses have been written to:")
        print(f"-> {OUTPUT_FILE}")
        print("You can now open this file to see the full list.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()