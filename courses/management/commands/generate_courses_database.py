#!/usr/bin/env python3
"""
Django Management Command: Generate Comprehensive Courses Database for Kenya
Usage: python manage.py generate_courses_database
"""

from django.core.management.base import BaseCommand
import json
import os
from datetime import datetime
from typing import List, Dict

DB_FILENAME = "courses_db.json"

class Command(BaseCommand):
    help = 'Generate comprehensive courses database for Kenya (Degree, Diploma, Certificate, Artisan)'

    def add_arguments(self, parser):
        parser.add_argument(
            '--output',
            type=str,
            default=DB_FILENAME,
            help='Output filename for the database (default: courses_db.json)'
        )
        parser.add_argument(
            '--skip-validation',
            action='store_true',
            help='Skip validation step'
        )

    def handle(self, *args, **options):
        """Main execution handler for Django management command"""
        self.stdout.write("\n" + "="*70)
        self.stdout.write(self.style.SUCCESS("🇰🇪  KENYA COMPREHENSIVE COURSES DATABASE GENERATOR"))
        self.stdout.write("="*70)
        self.stdout.write(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        output_file = options['output']
        skip_validation = options['skip_validation']
        
        # Load existing database
        self.stdout.write("📂 Loading existing database...")
        existing_courses = self.load_db(output_file)
        self.stdout.write(f"   Found {len(existing_courses)} existing courses\n")
        
        # Generate new courses
        self.stdout.write("🔄 Generating course database...\n")
        new_courses = self.generate_all_courses()
        
        # Merge and deduplicate
        self.stdout.write(f"\n🔗 Merging databases...")
        all_courses = self.deduplicate(existing_courses, new_courses)
        self.stdout.write(f"   Total unique courses: {len(all_courses)}")
        
        # Validate
        if not skip_validation:
            if not self.validate_database(all_courses):
                self.stdout.write(self.style.WARNING("\n⚠️  Warning: Database contains validation errors!"))
                self.stdout.write("Use --skip-validation to save anyway")
                return
        
        # Save main database
        self.stdout.write(f"\n💾 Saving to {output_file}...")
        self.save_db(all_courses, output_file)
        self.stdout.write(self.style.SUCCESS(f"   ✅ Saved successfully!"))
        
        # Generate statistics
        stats = self.get_database_statistics(all_courses)
        self.print_statistics(stats)
        
        # Export categorized files
        self.stdout.write("📤 Exporting categorized files...")
        self.export_by_level(all_courses)
        self.export_by_path(all_courses)
        self.export_summary_report(all_courses, stats)
        
        self.stdout.write("\n" + "="*70)
        self.stdout.write(self.style.SUCCESS("✨ DATABASE GENERATION COMPLETE!"))
        self.stdout.write("="*70)
        self.stdout.write(f"Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        self.stdout.write(f"📁 Main database: {output_file}")
        self.stdout.write(f"📁 Exports folder: exports/")
        self.stdout.write(f"📁 Total courses: {len(all_courses)}\n")

    # ============================================================================
    # UTILITY FUNCTIONS
    # ============================================================================

    def load_db(self, filename: str) -> List[Dict]:
        """Load existing database or return empty list."""
        if not os.path.exists(filename):
            return []
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []

    def save_db(self, courses: List[Dict], filename: str):
        """Save courses database to JSON file."""
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(courses, f, ensure_ascii=False, indent=2)

    def deduplicate(self, existing: List[Dict], new: List[Dict]) -> List[Dict]:
        """Merge lists with no duplicates by (program_name, level)."""
        key_map = {
            (c["program_name"].strip().lower(), c["level"].strip().lower()): c 
            for c in existing
        }
        for c in new:
            key = (c["program_name"].strip().lower(), c["level"].strip().lower())
            key_map[key] = c
        return list(key_map.values())

    def make_program(
        self,
        program_name: str,
        level: str,
        path: str,
        min_mean_grade: str,
        min_cluster_points: int,
        subject_requirements: List[str],
        description: str,
        career_path: str,
        duration: str,
        exam_body: str
    ) -> Dict:
        """Create a program entry with all required fields."""
        return {
            "program_name": program_name,
            "level": level,
            "path": path,
            "min_mean_grade": min_mean_grade,
            "min_cluster_points": min_cluster_points,
            "subject_requirements": subject_requirements,
            "description": description,
            "career_path": career_path,
            "duration": duration,
            "exam_body": exam_body,
            "metadata": {
                "date_generated": datetime.utcnow().isoformat() + "Z",
                "source": "Kenya Courses Database Generator 2025",
                "last_updated": datetime.utcnow().strftime("%Y-%m-%d")
            }
        }

    # ============================================================================
    # COURSE GENERATION FUNCTIONS
    # ============================================================================

    def generate_all_courses(self) -> List[Dict]:
        """Generate complete course database across all qualification levels."""
        all_courses = []
        
        self.stdout.write("🎓 Generating DEGREE programs...")
        degree_courses = self.generate_degree_programs()
        all_courses.extend(degree_courses)
        self.stdout.write(f"   ✅ Generated {len(degree_courses)} degree programs")
        
        self.stdout.write("📜 Generating DIPLOMA programs...")
        diploma_courses = self.generate_diploma_programs()
        all_courses.extend(diploma_courses)
        self.stdout.write(f"   ✅ Generated {len(diploma_courses)} diploma programs")
        
        self.stdout.write("📋 Generating CERTIFICATE programs...")
        certificate_courses = self.generate_certificate_programs()
        all_courses.extend(certificate_courses)
        self.stdout.write(f"   ✅ Generated {len(certificate_courses)} certificate programs")
        
        self.stdout.write("🔧 Generating ARTISAN programs...")
        artisan_courses = self.generate_artisan_programs()
        all_courses.extend(artisan_courses)
        self.stdout.write(f"   ✅ Generated {len(artisan_courses)} artisan programs")
        
        return all_courses

    def generate_degree_programs(self) -> List[Dict]:
        """Generate comprehensive degree programs."""
        level = "Degree"
        programs = []

        # COMPUTER SCIENCE & IT
        programs.append(self.make_program(
            "Bachelor of Science in Computer Science",
            level,
            "Science & IT > Computer Science",
            "C+",
            36,
            [
                "Mathematics (Minimum B plain / 9 points)",
                "Physics or Chemistry (Minimum C+ / 7 points)",
                "English or Kiswahili (Minimum C plain / 6 points)",
                "Any Group 2 or 3 subject"
            ],
            "A comprehensive BSc in Computer Science offering in-depth study of programming fundamentals (Python, Java, C++, JavaScript), data structures and algorithms, software engineering principles, database management systems, computer networks and security, operating systems, artificial intelligence and machine learning, web and mobile development, cloud computing, and cybersecurity.",
            "Graduates pursue diverse careers as software developers/engineers, full-stack developers, mobile app developers, systems analysts, database administrators, network engineers, data scientists, machine learning engineers, AI specialists, cybersecurity analysts, DevOps engineers, cloud architects, or IT consultants. Starting salaries range from KSh 60,000-150,000 monthly.",
            "4 years (8 semesters)",
            "University Senate / Commission for University Education (CUE)"
        ))

        programs.append(self.make_program(
            "Bachelor of Science in Information Technology",
            level,
            "Science & IT > Information Technology",
            "C+",
            34,
            [
                "Mathematics (Minimum C+ / 7 points)",
                "English or Kiswahili (Minimum C plain / 6 points)",
                "Physics, Chemistry, or Computer Studies (Minimum C plain / 6 points)",
                "Any Group 2, 3, or 4 subject"
            ],
            "A practical-oriented IT degree focusing on enterprise systems, network infrastructure design and management, web application development, mobile app development, database administration, cloud computing technologies, IT project management, cybersecurity implementation, and systems administration.",
            "Graduates work as IT support specialists, systems administrators, network administrators, web developers, mobile application developers, database administrators, cloud engineers, cybersecurity analysts, IT project coordinators, or IT consultants. Starting salaries range from KSh 50,000-110,000 monthly.",
            "4 years (8 semesters)",
            "University Senate / CUE"
        ))

        # ENGINEERING PROGRAMS
        programs.append(self.make_program(
            "Bachelor of Engineering (Electrical and Electronic Engineering)",
            level,
            "Engineering > Electrical & Electronic",
            "C+",
            40,
            [
                "Mathematics (Minimum B plain / 9 points)",
                "Physics (Minimum B plain / 9 points)",
                "Chemistry (Minimum C+ / 7 points)",
                "English or Kiswahili (Minimum C plain / 6 points)"
            ],
            "An ERB-accredited professional engineering degree providing comprehensive training in electrical power systems, electronics and microelectronics, control and automation systems, telecommunications engineering, signal processing, embedded systems design, digital electronics, power electronics, electrical machines and drives, renewable energy systems, and instrumentation.",
            "Career opportunities include electrical design engineer, power systems engineer, telecommunications engineer, automation and control engineer, instrumentation engineer, renewable energy consultant, electrical maintenance engineer, project engineer, or consulting engineer. Starting salaries: KSh 70,000-180,000 monthly.",
            "5 years (10 semesters)",
            "Engineers Board of Kenya (EBK) / CUE"
        ))

        programs.append(self.make_program(
            "Bachelor of Engineering (Civil Engineering)",
            level,
            "Engineering > Civil",
            "C+",
            40,
            [
                "Mathematics (Minimum B plain / 9 points)",
                "Physics (Minimum B plain / 9 points)",
                "Chemistry or Geography (Minimum C+ / 7 points)",
                "English or Kiswahili (Minimum C plain / 6 points)"
            ],
            "An ERB-accredited professional civil engineering degree providing comprehensive training in structural analysis and design, geotechnical engineering, hydraulics and hydrology, transportation and highway engineering, construction project management, surveying and geomatics, materials science, environmental engineering, and water resources engineering.",
            "Graduates pursue careers as structural engineers, site engineers, resident engineers, consulting engineers, highway engineers, water and sanitation engineers, geotechnical engineers, project managers, construction managers, or quantity surveyors. Starting salaries: KSh 70,000-200,000 monthly.",
            "5 years (10 semesters)",
            "Engineers Board of Kenya (EBK) / CUE"
        ))

        # BUSINESS & COMMERCE
        programs.append(self.make_program(
            "Bachelor of Commerce (Accounting)",
            level,
            "Business & Economics > Accounting",
            "C+",
            34,
            [
                "Mathematics or Business Studies (Minimum C plain / 6 points)",
                "English or Kiswahili (Minimum C plain / 6 points)",
                "Any two Group 2, 3, or 4 subjects"
            ],
            "A comprehensive business degree specializing in accounting theory and practice, financial accounting, management accounting, cost accounting, auditing and assurance, taxation (KRA tax system), accounting information systems, financial management, corporate governance, business law, accounting standards (IFRS, IAS), and forensic accounting.",
            "Graduates pursue careers as accountants, auditors, tax consultants, financial analysts, management accountants, budget analysts, financial controllers, or accounting information systems specialists. Starting salaries: KSh 45,000-100,000 monthly. Most pursue CPA (K) certification for enhanced career prospects.",
            "4 years (8 semesters)",
            "University Senate / CUE / ICPAK exemptions"
        ))

        programs.append(self.make_program(
            "Bachelor of Commerce (Finance)",
            level,
            "Business & Economics > Finance",
            "C+",
            34,
            [
                "Mathematics or Business Studies (Minimum C plain / 6 points)",
                "English or Kiswahili (Minimum C plain / 6 points)",
                "Any two Group 2, 3, or 4 subjects"
            ],
            "A specialized business degree focusing on corporate finance, investment analysis and portfolio management, financial markets and institutions, capital markets operations, banking operations, financial modeling, risk management, derivatives and financial engineering, international finance, and treasury management.",
            "Graduates pursue careers as financial analysts, investment analysts, equity research analysts, portfolio managers, credit analysts, relationship managers, treasury officers, financial planners, risk managers, stockbrokers, or fintech specialists. Starting salaries: KSh 50,000-120,000 monthly.",
            "4 years (8 semesters)",
            "University Senate / CUE"
        ))

        # Add more degree programs here following the same pattern...
        
        return programs

    def generate_diploma_programs(self) -> List[Dict]:
        """Generate comprehensive diploma programs."""
        level = "Diploma"
        programs = []

        # ICT DIPLOMAS
        programs.append(self.make_program(
            "Diploma in Information Technology",
            level,
            "ICT > Information Technology",
            "C-",
            22,
            [
                "Mathematics (Minimum D+ / 4 points)",
                "English or Kiswahili (Minimum D+ / 4 points)",
                "Any other two subjects"
            ],
            "A comprehensive practical IT diploma providing hands-on training in computer applications, programming basics (Python, Java), web development (HTML, CSS, JavaScript, PHP), database management (MySQL), computer networking fundamentals, operating systems (Windows, Linux), IT support and troubleshooting, and cybersecurity basics.",
            "Graduates work as IT support technicians, computer lab technicians, network administrators, web developers, database assistants, system administrators, help desk officers, or ICT teachers in colleges. Starting salaries: KSh 25,000-50,000 monthly.",
            "2-3 years (4-6 semesters)",
            "KNEC / TVETA"
        ))

        programs.append(self.make_program(
            "Diploma in Business Management",
            level,
            "Business > Management",
            "C-",
            20,
            [
                "English or Kiswahili (Minimum D+ / 4 points)",
                "Mathematics or Business Studies (Minimum D+ / 4 points)",
                "Any other two subjects"
            ],
            "A comprehensive business diploma covering principles of management, business communication, organizational behavior, accounting basics, marketing principles, human resource management, entrepreneurship, business law, office management, customer service, sales management, and business planning.",
            "Graduates work as administrative assistants, office administrators, supervisors, junior managers, sales representatives, customer service officers, operations assistants, or start their own small businesses. Starting salaries: KSh 20,000-45,000 monthly.",
            "2-3 years (4-6 semesters)",
            "KNEC / TVETA"
        ))

        # Add more diploma programs...
        
        return programs

    def generate_certificate_programs(self) -> List[Dict]:
        """Generate comprehensive certificate programs."""
        level = "Certificate"
        programs = []

        programs.append(self.make_program(
            "Certificate in Business Management",
            level,
            "Business & Management > Business Administration",
            "D+",
            16,
            [
                "English or Kiswahili (Minimum D+ / 4 points)",
                "Mathematics (Minimum D plain / 3 points)",
                "Any other subject"
            ],
            "A comprehensive business certificate program providing fundamental business management skills including principles of management, office administration, business communication, basic bookkeeping, business mathematics, customer service, marketing basics, and entrepreneurship fundamentals.",
            "Graduates secure employment as office assistants, administrative clerks, receptionists, customer service representatives, sales assistants, store clerks, cashiers, or start small businesses. Starting salaries: KSh 15,000-30,000 monthly.",
            "1 year (2 semesters)",
            "Kenya National Examinations Council (KNEC)"
        ))

        programs.append(self.make_program(
            "Certificate in Information Communication Technology",
            level,
            "ICT & Computing > Information Technology",
            "D+",
            16,
            [
                "Mathematics (Minimum D plain / 3 points)",
                "English or Kiswahili (Minimum D+ / 4 points)",
                "Any other subject"
            ],
            "A foundational ICT certificate providing essential computer skills including computer fundamentals, operating systems (Windows, Linux basics), Microsoft Office Suite (Word, Excel, PowerPoint), internet and email usage, computer networks fundamentals, basic troubleshooting, and digital literacy.",
            "Graduates secure employment as computer operators, data entry clerks, office assistants, cyber café attendants, IT support assistants, or computer lab assistants. Starting salaries: KSh 15,000-28,000 monthly.",
            "1 year (2 semesters)",
            "Kenya National Examinations Council (KNEC)"
        ))

        # Add more certificate programs...
        
        return programs

    def generate_artisan_programs(self) -> List[Dict]:
        """Generate comprehensive artisan programs."""
        level = "Artisan"
        programs = []

        programs.append(self.make_program(
            "Artisan in Masonry",
            level,
            "Construction & Building Trades > Masonry",
            "D-",
            8,
            ["Mathematics (Minimum D- / 2 points) OR Any subject"],
            "A practical artisan course providing hands-on training in masonry including bricklaying, blocklaying, stone masonry, wall construction, foundation laying, mortar preparation, building materials, basic measurements, plastering and rendering, building safety, and quality standards in masonry work.",
            "Graduates work as masons, bricklayers, blocklayers, or self-employed contractors. Daily rates: KSh 1,000-1,500. Skilled masons typically earn KSh 25,000-60,000 monthly. Strong demand in construction sector.",
            "6 months to 1 year",
            "Kenya National Examinations Council (KNEC)"
        ))

        programs.append(self.make_program(
            "Artisan in Carpentry and Joinery",
            level,
            "Construction & Building Trades > Carpentry",
            "D-",
            8,
            ["Mathematics (Minimum D- / 2 points) OR Any subject"],
            "A practical artisan training providing hands-on skills in woodworking including timber identification, carpentry hand tools, power tools operation, cutting and shaping wood, joint making, door and window frame construction, furniture making basics, roof construction, wood finishing, and workshop safety.",
            "Graduates work as carpenters, joiners, furniture makers, or self-employed. Daily rates: KSh 1,000-2,000. Skilled carpenters earn KSh 30,000-80,000 monthly. High demand with construction activities.",
            "6 months to 1 year",
            "Kenya National Examinations Council (KNEC)"
        ))

        programs.append(self.make_program(
            "Artisan in Motor Vehicle Mechanics",
            level,
            "Automotive & Mechanical > Motor Vehicle",
            "D-",
            8,
            ["Mathematics (Minimum D- / 2 points) OR Any subject"],
            "A practical artisan course providing hands-on training in motor vehicle repair including engine repair, fuel systems, ignition systems, brake systems, suspension systems, transmission basics, electrical systems, diagnostics and fault finding, vehicle servicing, and workshop safety.",
            "Graduates work as motor vehicle mechanics, auto mechanics, or self-employed. Daily rates: KSh 1,200-2,500. Skilled mechanics earn KSh 30,000-75,000 monthly. Strong demand with large vehicle population.",
            "6 months to 1 year",
            "Kenya National Examinations Council (KNEC)"
        ))

        programs.append(self.make_program(
            "Artisan in Hairdressing and Beauty Therapy",
            level,
            "Beauty & Personal Care > Hairdressing",
            "D-",
            8,
            ["English or Kiswahili (Minimum D- / 2 points) OR Any subject"],
            "A practical artisan course providing comprehensive training in hairdressing and beauty services including hair cutting, styling, coloring, braiding, beauty therapy basics (facials, manicure, pedicure, makeup), salon hygiene, customer service, and professional ethics.",
            "Graduates work as hairdressers, beauticians, salon assistants, or own salons. Salon owners can earn KSh 50,000-300,000+ monthly. Independent stylists charge per service earning KSh 40,000-100,000+ monthly.",
            "6 months to 1 year",
            "Kenya National Examinations Council (KNEC)"
        ))

        # Add more artisan programs...
        
        return programs

    # ============================================================================
    # VALIDATION AND STATISTICS
    # ============================================================================

    def get_database_statistics(self, courses: List[Dict]) -> Dict:
        """Generate statistics about the course database."""
        stats = {
            "total_courses": len(courses),
            "by_level": {},
            "by_path": {},
            "by_exam_body": {}
        }
        
        for course in courses:
            level = course["level"]
            path = course["path"]
            exam_body = course["exam_body"]
            
            stats["by_level"][level] = stats["by_level"].get(level, 0) + 1
            stats["by_path"][path] = stats["by_path"].get(path, 0) + 1
            stats["by_exam_body"][exam_body] = stats["by_exam_body"].get(exam_body, 0) + 1
        
        return stats

    def print_statistics(self, stats: Dict):
        """Print formatted database statistics."""
        self.stdout.write("\n" + "="*70)
        self.stdout.write("📊 KENYA COURSES DATABASE STATISTICS")
        self.stdout.write("="*70)
        self.stdout.write(f"\n✅ Total Courses: {stats['total_courses']}")
        
        self.stdout.write("\n📚 By Qualification Level:")
        for level in ["Degree", "Diploma", "Certificate", "Artisan"]:
            count = stats['by_level'].get(level, 0)
            if count > 0:
                self.stdout.write(f"   • {level}: {count} programs")
        
        self.stdout.write("\n🎯 Top 10 Career Paths:")
        sorted_paths = sorted(stats['by_path'].items(), key=lambda x: x[1], reverse=True)[:10]
        for path, count in sorted_paths:
            self.stdout.write(f"   • {path}: {count} programs")
        
        self.stdout.write("="*70 + "\n")

    def validate_database(self, courses: List[Dict]) -> bool:
        """Validate database integrity."""
        self.stdout.write("\n🔍 Validating database integrity...")
        
        required_fields = [
            "program_name", "level", "path", "min_mean_grade",
            "min_cluster_points", "subject_requirements", "description",
            "career_path", "duration", "exam_body", "metadata"
        ]
        
        valid_levels = ["Degree", "Diploma", "Certificate", "Artisan"]
        errors = []
        
        for idx, course in enumerate(courses):
            missing = [f for f in required_fields if f not in course]
            if missing:
                errors.append(f"Course #{idx+1} missing fields: {missing}")
            
            if course.get("level") not in valid_levels:
                errors.append(f"Course #{idx+1} has invalid level")
        
        if errors:
            self.stdout.write(self.style.ERROR("❌ Validation FAILED:"))
            for error in errors[:5]:
                self.stdout.write(f"   • {error}")
            return False
        
        self.stdout.write(self.style.SUCCESS("✅ Validation PASSED!"))
        return True

    def export_by_level(self, courses: List[Dict], output_dir: str = "exports"):
        """Export courses by level."""
        os.makedirs(output_dir, exist_ok=True)
        
        by_level = {}
        for course in courses:
            level = course["level"]
            if level not in by_level:
                by_level[level] = []
            by_level[level].append(course)
        
        for level, level_courses in by_level.items():
            filename = os.path.join(output_dir, f"{level.lower()}_courses.json")
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(level_courses, f, ensure_ascii=False, indent=2)
            self.stdout.write(f"   ✅ {level}: {len(level_courses)} courses")

    def export_by_path(self, courses: List[Dict], output_dir: str = "exports"):
        """Export courses by career path."""
        os.makedirs(output_dir, exist_ok=True)
        
        by_path = {}
        for course in courses:
            path = course["path"].split(">")[0].strip()
            if path not in by_path:
                by_path[path] = []
            by_path[path].append(course)
        
        for path, path_courses in by_path.items():
            safe_path = path.replace("/", "_").replace(" ", "_").lower()
            filename = os.path.join(output_dir, f"path_{safe_path}.json")
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(path_courses, f, ensure_ascii=False, indent=2)

    def export_summary_report(self, courses: List[Dict], stats: Dict, output_dir: str = "exports"):
        """Export summary report."""
        os.makedirs(output_dir, exist_ok=True)
        
        report_file = os.path.join(output_dir, "database_summary.txt")
        with open(report_file, "w", encoding="utf-8") as f:
            f.write("KENYA COURSES DATABASE - SUMMARY REPORT\n")
            f.write("="*70 + "\n\n")
            f.write(f"Total Courses: {stats['total_courses']}\n\n")
            
            f.write("BY LEVEL:\n")
            for level in ["Degree", "Diploma", "Certificate", "Artisan"]:
                count = stats['by_level'].get(level, 0)
                f.write(f"  {level}: {count}\n")
        
        self.stdout.write(f"   ✅ Summary report created") 