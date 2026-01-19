#!/usr/bin/env python3
"""
Complete Comprehensive Courses Database Generator for Kenya
Generates ALL qualification levels with detailed information:
- DEGREE: C+ minimum (7 points)
- DIPLOMA: C- minimum (5 points)  
- CERTIFICATE: D+ minimum (4 points)
- ARTISAN: D- minimum (2 points)

Version: 2.0 - Complete Edition 2025
"""

import json
import os
from datetime import datetime
from typing import List, Dict

DB_FILENAME = "courses_db.json"

def load_db(filename: str = DB_FILENAME) -> List[Dict]:
    """Load existing database or return empty list."""
    if not os.path.exists(filename):
        return []
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def save_db(courses: List[Dict], filename: str = DB_FILENAME):
    """Save courses database to JSON file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(courses, f, ensure_ascii=False, indent=2)

def deduplicate(existing: List[Dict], new: List[Dict]) -> List[Dict]:
    """
    Merge lists with no duplicates by (program_name, level).
    Updates existing entries with new data.
    """
    key_map = {
        (c["program_name"].strip().lower(), c["level"].strip().lower()): c 
        for c in existing
    }
    for c in new:
        key = (c["program_name"].strip().lower(), c["level"].strip().lower())
        key_map[key] = c
    return list(key_map.values())

def make_program(
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

# ============================================================
# DEGREE PROGRAMS (Minimum: C+ / 7 points)
# ============================================================

def generate_degree_programs(self) -> List[Dict]:
    """Generate degree programs"""
    level = "Degree"
    programs = []

    # COMPUTER SCIENCE & IT
    programs.append(make_program(
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
        (
            "A comprehensive BSc in Computer Science offering in-depth study of programming fundamentals (Python, Java, C++, JavaScript), "
            "data structures and algorithms, software engineering principles, database management systems, computer networks and security, "
            "operating systems, artificial intelligence and machine learning, web and mobile development, cloud computing, and cybersecurity. "
            "The program combines theoretical foundations with extensive hands-on experience through laboratory sessions, individual and team "
            "projects, hackathons, and industrial attachments in technology companies. Students master software development methodologies "
            "(Agile, Scrum, DevOps), version control systems (Git), and modern frameworks (React, Angular, Django, Spring). Advanced courses "
            "cover big data analytics, Internet of Things (IoT), blockchain technology, and computer graphics. The curriculum emphasizes "
            "problem-solving, computational thinking, innovation, and entrepreneurship. Final year capstone project involves developing "
            "complete software systems addressing real-world problems, often in collaboration with industry partners."
        ),
        (
            "Graduates pursue diverse careers as software developers/engineers, full-stack developers, mobile app developers, systems analysts, "
            "database administrators, network engineers, data scientists, machine learning engineers, AI specialists, cybersecurity analysts, "
            "DevOps engineers, cloud architects (AWS, Azure, Google Cloud), quality assurance engineers, IT consultants, technical project managers, "
            "or solutions architects. Employment opportunities in leading technology companies (Safaricom, Equity Bank Technology, KCB Innovation Labs), "
            "fintech startups (M-KOPA, Twiga Foods, Apollo Agriculture), multinational corporations (Google, Microsoft, IBM, Andela), software houses "
            "(Craft Silicon, Ajira Digital), government ICT departments (ICTA, Konza Technopolis), telecommunications firms, banks, insurance companies, "
            "educational institutions, and research centers. Starting salaries range from KSh 60,000-150,000 monthly. Many graduates become successful "
            "entrepreneurs, founding tech startups or offering freelance services internationally. Career advancement leads to senior developer, tech lead, "
            "CTO, or engineering manager positions. Further education: Master's in Computer Science, Data Science, AI, Software Engineering, Cybersecurity, "
            "or specialized certifications (AWS, Google Cloud, Microsoft Azure, CISSP). PhD opportunities for research and academic careers."
        ),
        "4 years (8 semesters)",
        "University Senate / Commission for University Education (CUE)"
    ))

    programs.append(make_program(
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
        (
            "A practical-oriented IT degree focusing on enterprise systems, network infrastructure design and management, web application development, "
            "mobile app development, database administration and design, cloud computing technologies, IT project management, cybersecurity implementation, "
            "systems administration (Linux, Windows Server), and IT service management (ITIL framework). Students gain hands-on experience with "
            "industry-standard technologies: programming languages (Python, PHP, Java, C#, JavaScript), web frameworks (Laravel, Django, React, Angular), "
            "mobile development (Android, iOS, Flutter), database systems (MySQL, PostgreSQL, MongoDB, Oracle), networking equipment and protocols "
            "(Cisco CCNA concepts, TCP/IP), server administration, virtualization (VMware, VirtualBox), containerization (Docker, Kubernetes), and cloud "
            "platforms (AWS, Microsoft Azure, Google Cloud). The curriculum emphasizes practical skills through extensive laboratory work, real-world "
            "projects, system implementations, and mandatory 3-month industrial attachment. Students build complete information systems, deploy web "
            "applications, configure network infrastructures, and implement security solutions. Final year project involves developing and deploying a "
            "comprehensive IT solution for a real client or organization."
        ),
        (
            "Graduates work as IT support specialists, systems administrators, network administrators, web developers, mobile application developers, "
            "database administrators, cloud engineers, cybersecurity analysts, IT project coordinators, business analysts, IT consultants, technical "
            "support engineers, DevOps specialists, or ERP system administrators. Strong employment demand in commercial banks (Equity, KCB, Co-operative), "
            "telecommunications companies (Safaricom, Airtel, Telkom), government ministries, county governments, educational institutions, hospitals, "
            "insurance companies, manufacturing firms, retail chains, BPO centers (Konza Technopolis), NGOs, software companies, and consultancy firms. "
            "Starting salaries range from KSh 50,000-110,000 monthly. Many graduates work as freelance developers or start IT services businesses. Career "
            "progression leads to IT manager, systems architect, CTO, or IT director positions. Professional certifications enhance prospects: CompTIA "
            "(A+, Network+, Security+), Cisco (CCNA, CCNP), Microsoft (MCSA, Azure), AWS Certified Solutions Architect, CEH, CISSP, ITIL, PMP. Further "
            "education: Master's in IT, Information Systems, Cybersecurity, Data Science, Project Management, or MBA Technology Management."
        ),
        "4 years (8 semesters)",
        "University Senate / CUE"
    ))

    # ENGINEERING PROGRAMS
    programs.append(make_program(
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
        (
            "An ERB-accredited professional engineering degree providing comprehensive training in electrical power systems, electronics and microelectronics, "
            "control and automation systems, telecommunications engineering, signal processing, embedded systems design, digital electronics, power electronics, "
            "electrical machines and drives, renewable energy systems, and instrumentation. The curriculum integrates theoretical foundations with extensive "
            "hands-on laboratory work, design projects, and practical applications. Students gain proficiency in circuit analysis and design, PCB design and "
            "fabrication, PLC programming (Siemens, Allen Bradley), SCADA systems, microcontroller programming (Arduino, ARM, PIC), FPGA design, power system "
            "analysis and protection, electrical installation design, motor control systems, and industrial automation. Computer-aided engineering tools include "
            "MATLAB/Simulink, AutoCAD Electrical, ETAP, Proteus, and LabVIEW. Mandatory 3-month industrial attachment provides exposure to real engineering "
            "environments. Final year capstone project addresses practical challenges such as designing solar power systems, developing IoT monitoring systems, "
            "creating automation solutions, or optimizing power distribution networks. Graduates eligible for ERB registration as Graduate Engineers, progressing "
            "to Professional Engineer (PEng) status after supervised work experience."
        ),
        (
            "Career opportunities include electrical design engineer, power systems engineer, protection and control engineer, telecommunications engineer, "
            "automation and control engineer, instrumentation engineer, renewable energy consultant, electrical maintenance engineer, project engineer, "
            "electrical contractor, consulting engineer, R&D engineer, and technical sales engineer. Major employers: Kenya Power (KPLC), KETRACO, KenGen, "
            "Geothermal Development Company (GDC), telecommunications companies (Safaricom, Airtel, Telkom), manufacturing industries (EABL, Bamburi Cement, "
            "BAT, Coca-Cola), construction firms, engineering consultancies, county governments, NCA, EPRA, KEBS, and international organizations. Starting "
            "salaries: KSh 70,000-180,000 monthly. Engineers can establish electrical contracting businesses or consultancy firms after gaining experience. "
            "Excellent growth potential with infrastructure development, renewable energy expansion, smart grid implementation, and industrial automation. "
            "Career advancement leads to senior engineer, principal engineer, chief engineer, engineering manager, or technical director positions. Emerging "
            "opportunities in solar energy, electric vehicle charging, smart building automation, IoT, and sustainable energy. Further education: Master's in "
            "Electrical Engineering (Power Systems, Control, Telecommunications, Power Electronics, Renewable Energy), MBA, or PhD for research and academic careers."
        ),
        "5 years (10 semesters)",
        "Engineers Board of Kenya (EBK) / CUE"
    ))

    programs.append(make_program(
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
        (
            "An ERB-accredited professional civil engineering degree providing comprehensive training in structural analysis and design, geotechnical engineering, "
            "hydraulics and hydrology, transportation and highway engineering, construction project management, surveying and geomatics, materials science and "
            "testing, environmental engineering, water resources engineering, and municipal engineering. Students learn to design, analyze, and supervise "
            "construction of buildings, bridges, roads, dams, water supply and sewerage systems, drainage systems, and other infrastructure. The curriculum "
            "combines classroom instruction with extensive laboratory work (materials testing, soil mechanics, hydraulics), field surveys (leveling, traversing, "
            "GPS), computer-aided design using industry-standard software (AutoCAD Civil 3D, STAAD Pro, SAP2000, ETABS, Bentley software), Building Information "
            "Modeling (BIM with Revit), and mandatory industrial attachment. Students undertake realistic design projects including multi-storey buildings, "
            "bridges, highways, water distribution networks, and wastewater treatment plants. Covers reinforced concrete design, steel structures, foundation "
            "engineering, pavement design, traffic engineering, construction methods, quantity surveying, contract administration, and construction law. Final "
            "year involves comprehensive research project. Program emphasizes international codes (Eurocodes, British Standards, American codes), sustainability, "
            "value engineering, health and safety, quality assurance, and professional ethics. Graduates prepared for ERB registration."
        ),
        (
            "Graduates pursue careers as structural engineers, site engineers/supervisors, resident engineers, consulting engineers, highway/road engineers, "
            "water and sanitation engineers, geotechnical engineers, project managers, construction managers, quantity surveyors, facilities managers, municipal "
            "engineers, or infrastructure planners. Employment in major construction companies (China Road and Bridge, China Wu Yi, Civicon, H. Young, Erdemann), "
            "government road agencies (KeNHA, KURA, KeRRA), NCA, State Department of Public Works, county governments, consulting engineering firms (Mauzo, "
            "Associated Consulting Engineers, Vibanzi Designs), real estate developers, water utilities (Nairobi City Water, Athi Water Services), international "
            "organizations (World Bank, African Development Bank, UN-Habitat), and NGOs. Starting salaries: KSh 70,000-200,000 monthly. Many engineers establish "
            "construction companies, consultancy firms, or real estate development businesses. Excellent growth prospects driven by Kenya's infrastructure "
            "development agenda. Career progression leads to senior engineer, principal engineer, project director, chief engineer, or managing director positions. "
            "Specialization opportunities in structural design, road engineering, water resources, construction management, or project management. Further "
            "education: Master's in Civil Engineering specializations (Structural, Geotechnical, Transportation, Water Resources, Construction Management), "
            "Master's in Project Management, MBA, or PhD for research and university teaching."
        ),
        "5 years (10 semesters)",
        "Engineers Board of Kenya (EBK) / CUE"
    ))

    programs.append(make_program(
        "Bachelor of Engineering (Mechanical Engineering)",
        level,
        "Engineering > Mechanical",
        "C+",
        40,
        [
            "Mathematics (Minimum B plain / 9 points)",
            "Physics (Minimum B plain / 9 points)",
            "Chemistry (Minimum C+ / 7 points)",
            "English or Kiswahili (Minimum C plain / 6 points)"
        ],
        (
            "An ERB-accredited professional mechanical engineering program covering mechanics of materials (stress analysis, failure theories), engineering "
            "thermodynamics, fluid mechanics and hydraulics, heat transfer, machine design and analysis, manufacturing processes and technology, engineering "
            "dynamics, control systems, CAD/CAM/CAE, robotics and automation, automotive engineering, HVAC systems, and maintenance engineering. Students develop "
            "strong practical skills through comprehensive workshop training including welding (arc, gas, MIG, TIG), machining operations (lathe, milling, "
            "drilling, grinding), fitting and assembly, sheet metal work, and foundry practice. Extensive use of computer-aided tools: SolidWorks, CATIA, AutoCAD "
            "Mechanical, Inventor for 3D modeling; ANSYS for FEA; MATLAB/Simulink for simulation; CNC programming. Laboratory work covers materials testing "
            "(tensile, hardness, impact), engine performance testing, fluid mechanics experiments, heat transfer experiments, and metrology. Industrial attachment "
            "provides real-world exposure. Final year project typically involves design and fabrication of mechanical systems such as solar dryers, biogas "
            "digesters, hydraulic systems, conveyor systems, or research in renewable energy, automotive technology, or manufacturing optimization. Curriculum "
            "includes production planning, quality control, industrial safety, engineering economics, project management, and professional practice. Graduates "
            "prepared for ERB registration as Graduate Engineers and eventual Professional Engineer (PEng) status."
        ),
        (
            "Career opportunities include mechanical design engineer, maintenance engineer, production/manufacturing engineer, quality assurance engineer, plant "
            "engineer, automotive engineer, HVAC design engineer, project engineer, process engineer, technical sales engineer, facilities engineer, energy auditor, "
            "and consulting engineer. Employers include manufacturing companies (EABL, Bamburi Cement, Coca-Cola, BAT, Bidco Africa, KWAL), automotive sector "
            "(Toyota Kenya, General Motors East Africa, Isuzu, CMC Motors, Simba Corporation), construction and infrastructure firms, energy companies (KenGen, "
            "GDC, Kenya Pipeline Company), aviation (Kenya Airways, Moi International Airport), maritime and port operations, sugar industries, tea and coffee "
            "factories, county governments, consulting engineering firms, equipment suppliers, and international organizations. Starting salaries: KSh 70,000-170,000 "
            "monthly. Strong demand in manufacturing, energy, construction, and maintenance sectors. Many engineers establish mechanical workshops, equipment "
            "supply businesses, fabrication shops, or consultancy practices. Emerging opportunities in renewable energy (solar thermal, biogas), electric vehicles, "
            "3D printing/additive manufacturing, robotics, and mechatronics. Career advancement leads to senior engineer, engineering manager, plant manager, "
            "operations director, or technical director positions. Specialization in automotive engineering, energy systems, manufacturing systems, or maintenance "
            "management. Further education: Master's in Mechanical Engineering specializations (Thermofluids, Design and Manufacturing, Energy Systems, Automotive), "
            "Master's in Energy Studies, Project Management, MBA, or PhD for research and academic careers."
        ),
        "5 years (10 semesters)",
        "Engineers Board of Kenya (EBK) / CUE"
    ))

    # BUSINESS & COMMERCE
    programs.append(make_program(
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
        (
            "A comprehensive business degree specializing in accounting theory and practice, financial accounting, management accounting and control, cost and "
            "management accounting, auditing and assurance, taxation (KRA tax system including income tax, VAT, excise duty), accounting information systems, "
            "financial management and analysis, corporate governance, business law and commercial law, accounting standards (IFRS, IAS), forensic accounting "
            "and fraud examination, and public sector accounting. Students develop strong analytical, numerical, computational, and critical thinking skills "
            "through extensive case studies, practical assignments, group projects, and accounting software training. Hands-on experience with accounting "
            "software packages including Sage, QuickBooks, Pastel, SAP ERP Financials, Oracle Financials, and Microsoft Dynamics. The curriculum covers "
            "preparation, presentation and analysis of financial statements, budgeting and budget control, variance analysis, standard costing, activity-based "
            "costing, financial reporting for different entity types, internal control systems, risk management, and ethical considerations. Includes foundational "
            "business courses: economics, business mathematics, business statistics, quantitative methods, entrepreneurship, organizational behavior, marketing, "
            "and strategic management. Industrial attachment (8-12 weeks) provides exposure to accounting departments, audit firms, or financial institutions. "
            "Final year project involves comprehensive financial analysis, audit case study, tax planning exercise, or accounting system implementation. Program "
            "aligned with ICPAK CPA syllabus, providing exemptions in several CPA examination papers."
        ),
        (
            "Graduates pursue careers as accountants (financial, management, cost), auditors (internal, external, forensic), tax consultants and advisors, "
            "financial analysts and planners, management accountants, cost accountants, budget analysts and officers, financial controllers, accounts payable/"
            "receivable managers, payroll managers, treasury officers, credit controllers, financial reporting specialists, or accounting information systems "
            "specialists. Employment in Big Four accounting firms (PwC, KPMG, Deloitte, EY) and other audit firms (BDO, Grant Thornton, PKF, Crowe), commercial "
            "banks (KCB, Equity, Co-operative, Standard Chartered, Barclays), insurance companies (Britam, CIC, Jubilee, UAP), microfinance institutions, SACCOs, "
            "investment firms, manufacturing companies, retail businesses, hospitality industry, real estate firms, government ministries (National Treasury), "
            "regulatory bodies (KRA, Central Bank, Public Procurement Regulatory Authority), state corporations, county governments, NGOs, international "
            "development organizations, educational institutions, and private consultancy. Starting salaries: KSh 45,000-100,000 monthly. Most graduates pursue "
            "CPA (K) certification through ICPAK to become fully qualified CPAs, significantly enhancing career prospects (qualified CPAs earn KSh 80,000-300,000+ "
            "monthly). Career progression leads to senior accountant, finance manager, financial controller, chief accountant, finance director, or CFO positions. "
            "Many experienced accountants establish their own accounting firms, tax consultancy practices, or financial advisory services. The accounting "
            "profession offers excellent job security and consistent demand. Further education: Master's in Accounting, Master's in Finance, MBA (Finance/"
            "Accounting), professional qualifications (ACCA, CIMA, CFA), or PhD in Accounting for research and academic careers."
        ),
        "4 years (8 semesters)",
        "University Senate / CUE / ICPAK exemptions"
    ))

    programs.append(make_program(
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
        (
            "A specialized business degree focusing on corporate finance and financial management, investment analysis and portfolio management, financial markets "
            "and institutions, capital markets operations, banking operations and management, financial modeling and forecasting, risk management and insurance, "
            "derivatives and financial engineering, international finance and foreign exchange, treasury management, financial econometrics, behavioral finance, "
            "and financial technology (fintech). Students develop advanced analytical, quantitative, and decision-making skills through rigorous coursework, case "
            "analyses, investment simulations, and practical projects. The curriculum covers comprehensive financial statement analysis, capital budgeting and "
            "investment appraisal techniques (NPV, IRR, payback), working capital management, dividend policy, capital structure decisions, mergers and acquisitions, "
            "corporate valuation techniques, and financial planning and strategy. Extensive study of financial markets including money markets, capital markets "
            "(Nairobi Securities Exchange NSE), foreign exchange markets, and derivative markets. Students learn equity analysis, bond valuation, portfolio theory "
            "and management, asset pricing models (CAPM, APT), risk assessment and management, and investment strategies. Hands-on experience with financial "
            "software and tools including Microsoft Excel for financial modeling, Bloomberg Terminal (where available), financial calculators, statistical packages "
            "(STATA, EViews), and investment simulation platforms. Covers banking products and services, credit analysis and lending, Islamic banking, microfinance, "
            "mobile money systems (M-Pesa), and emerging fintech innovations. Includes foundational business courses: accounting principles, business statistics, "
            "economics, business law, entrepreneurship, and strategic management. Industrial attachment in banks, investment firms, insurance companies, or "
            "corporate finance departments provides practical exposure. Final year project typically involves financial analysis of companies, investment strategy "
            "development, portfolio optimization, business valuation, or research on financial markets."
        ),
        (
            "Graduates pursue careers as financial analysts, investment analysts, equity research analysts, portfolio managers, fund managers, credit analysts and "
            "officers, relationship managers (corporate, retail), treasury officers, financial planners and advisors, risk managers and analysts, insurance "
            "underwriters, stockbrokers and investment advisors, forex traders, financial controllers, corporate finance officers, or fintech specialists. Employment "
            "in commercial banks (KCB, Equity, Co-operative, Standard Chartered, NCBA, Barclays/Absa), investment banks, stockbrokerage firms (Dyer & Blair, "
            "Genghis Capital, Sterling Capital, AIB Capital), asset management companies (CIC Asset Management, Cytonn Investments, ICEA Lion, Britam Asset "
            "Managers), insurance companies (Britam, CIC, Jubilee, APA, UAP Old Mutual), microfinance institutions (Faulu, Kenya Women Finance Trust), SACCOs, "
            "pension fund administrators, investment funds, private equity firms, regulatory bodies (Capital Markets Authority CMA, Central Bank of Kenya, Insurance "
            "Regulatory Authority IRA, Retirement Benefits Authority RBA), corporate finance departments, financial advisory and consulting firms, and fintech "
            "companies (M-Pesa, mobile banking platforms). Starting salaries: KSh 50,000-120,000 monthly. The finance sector offers strong career growth and "
            "lucrative compensation. Many graduates pursue prestigious professional certifications: CFA (Chartered Financial Analyst) - globally recognized, FRM "
            "(Financial Risk Manager), ACCA, or CFP (Certified Financial Planner). Career progression leads to senior analyst, finance manager, head of treasury, "
            "CIO, CRO, or CFO positions. Emerging opportunities in fintech, mobile financial services, cryptocurrency/blockchain, algorithmic trading, and "
            "sustainable finance. Some graduates establish financial advisory firms, investment clubs, or fintech startups. Further education: Master's in Finance, "
            "MBA Finance, Master's in Financial Engineering, Master's in Risk Management, or PhD in Finance for research and academic positions."
        ),
        "4 years (8 semesters)",
        "University Senate / CUE"
    ))

    programs.append(make_program(
        "Bachelor of Business Administration",
        level,
        "Business & Economics > Management",
        "C+",
        32,
        [
            "English or Kiswahili (Minimum C plain / 6 points)",
            "Mathematics or Business Studies (Minimum C plain / 6 points)",
            "Any two Group 2, 3, or 4 subjects"
        ],
        (
            "A versatile and comprehensive business degree providing broad management education covering organizational management and administration, strategic "
            "management and planning, human resource management, marketing management and strategy, operations and supply chain management, financial management "
            "basics, entrepreneurship and innovation, business communication and correspondence, organizational behavior and psychology, leadership and team "
            "management, project management, quality management (TQM, Six Sigma concepts), business ethics and corporate social responsibility, international "
            "business, and business policy. Students develop essential management competencies including strategic thinking, decision-making, leadership, "
            "communication, teamwork, problem-solving, and analytical skills through case studies, business simulations, group projects, presentations, and "
            "research projects. The curriculum integrates theory with practical applications, preparing students for management roles across various business "
            "sectors and organizational types. Covers business planning and development, change management, business analytics and data-driven decision making, "
            "digital business transformation, business law and regulations, business research methods, and contemporary management issues. Students learn to use "
            "business software tools including Microsoft Office Suite (Excel, PowerPoint, Word), project management software (MS Project, Trello), business "
            "intelligence tools, and basic ERP systems. Mandatory industrial attachment (8-12 weeks) in companies, government organizations, or NGOs provides "
            "real-world exposure to business operations and management practices. Final year research project or business plan addresses practical management "
            "challenges or business opportunities. The program prepares graduates for entry-level management trainee positions and provides foundation for career "
            "advancement to senior management roles. Emphasizes adaptability, continuous learning, ethical leadership, and global business perspectives essential "
            "in today's dynamic business environment."
        ),
        (
            "Graduates pursue diverse careers as management trainees, administrative officers, operations managers, business development officers, sales and "
            "marketing managers, human resource officers, project coordinators, supply chain officers, customer service managers, business analysts, office "
            "managers, branch managers, retail managers, operations supervisors, procurement officers, or entrepreneurs establishing their own businesses. "
            "Employment opportunities across all economic sectors including banks and financial institutions, manufacturing companies, retail and wholesale "
            "businesses, hospitality industry (hotels, restaurants, travel agencies), telecommunications companies, insurance firms, real estate companies, "
            "logistics and transportation firms, consulting companies, government ministries and departments, state corporations, county governments, NGOs "
            "and international organizations, educational institutions, healthcare facilities, media and entertainment companies, and fast-moving consumer goods "
            "(FMCG) companies. Starting salaries: KSh 40,000-90,000 monthly depending on organization, role, and location. The broad nature of BBA training "
            "provides flexibility to work in various industries and functions. Career progression typically leads to middle management (assistant manager, "
            "manager), senior management (senior manager, general manager), and eventually executive positions (director, CEO). Many BBA graduates successfully "
            "start their own businesses in retail, services, consultancy, or other sectors, leveraging entrepreneurship skills gained during study. The degree "
            "provides strong foundation for further professional development. Further education options include specialized Master's degrees (MBA, Master's in "
            "HRM, Master's in Marketing, Master's in Project Management, Master's in Supply Chain Management), professional certifications (PMP - Project "
            "Management Professional, CHRP - Certified Human Resource Professional, CIM - Chartered Institute of Marketing, CIPS - Chartered Institute of "
            "Procurement and Supply), or PhD in Business Administration for research and academic careers in universities."
        ),
        "4 years (8 semesters)",
        "University Senate / CUE"
    ))

    # HEALTH SCIENCES
    programs.append(make_program(
        "Bachelor of Medicine and Bachelor of Surgery (MBChB)",
        level,
        "Health Sciences > Medicine",
        "B+",
        48,
        [
            "Biology (Minimum B+ / 11 points)",
            "Chemistry (Minimum B+ / 11 points)",
            "Physics or Mathematics (Minimum B plain / 9 points)",
            "English or Kiswahili (Minimum C+ / 7 points)"
        ],
        (
            "A rigorous professional medical degree program approved by the Medical Practitioners and Dentists Council (MPDC) providing comprehensive training "
            "to become a medical doctor. The 6-year curriculum integrates basic medical sciences (anatomy, physiology, biochemistry, pharmacology, pathology, "
            "microbiology, immunology), clinical sciences (internal medicine, surgery, pediatrics, obstetrics and gynecology, psychiatry, community health), "
            "and clinical rotations in hospitals and healthcare facilities. First two years focus on pre-clinical studies covering human anatomy (dissection), "
            "physiology, biochemistry, and introduction to clinical medicine. Years 3-5 involve clinical rotations in major medical specialties with hands-on "
            "patient care under supervision, developing clinical examination skills, diagnostic reasoning, treatment planning, and patient management. Students "
            "rotate through medical wards, surgical theaters, pediatric departments, maternity units, psychiatric wards, and community health settings. "
            "Final year (internship year) involves supervised clinical practice in various hospital departments. Program emphasizes evidence-based medicine, "
            "clinical decision-making, medical ethics, patient communication, professionalism, and continuous learning. Graduates must complete one-year "
            "internship and register with MPDC to practice medicine in Kenya."
        ),
        (
            "Upon completion and MPDC registration, graduates work as medical officers in government hospitals (Kenyatta National Hospital, Moi Teaching and "
            "Referral Hospital, county referral hospitals), private hospitals (Aga Khan Hospital, Nairobi Hospital, MP Shah Hospital, Avenue Healthcare), "
            "mission hospitals, health centers, or establish private clinics. Starting salary for government medical officers: KSh 150,000-250,000 monthly. "
            "After gaining experience, doctors can specialize through postgraduate training (Master of Medicine MMed) in fields such as surgery, internal "
            "medicine, pediatrics, obstetrics and gynecology, anesthesiology, radiology, pathology, ophthalmology, ENT, orthopedics, or psychiatry. Specialists "
            "earn significantly higher (KSh 300,000-1,000,000+ monthly). Career opportunities in public health, medical research, medical education (university "
            "lecturers), medical administration, international health organizations (WHO, MSF, Red Cross), pharmaceutical industry (medical affairs), medical "
            "insurance, or telemedicine. Many doctors establish successful private practices or specialty clinics. The medical profession offers high job "
            "security, respect, and rewarding career helping save lives and improve health outcomes. Further education: MMed specialization (4-5 years), "
            "Master's in Public Health (MPH), PhD in Medical Sciences, or international medical qualifications (MRCP, MRCS, USMLE)."
        ),
        "6 years (12 semesters including internship)",
        "Medical Practitioners and Dentists Council (MPDC) / CUE"
    ))

    programs.append(make_program(
        "Bachelor of Pharmacy",
        level,
        "Health Sciences > Pharmacy",
        "B plain",
        42,
        [
            "Chemistry (Minimum B plain / 9 points)",
            "Biology (Minimum B plain / 9 points)",
            "Mathematics or Physics (Minimum C+ / 7 points)",
            "English or Kiswahili (Minimum C plain / 6 points)"
        ],
        (
            "A professional pharmacy degree approved by the Pharmacy and Poisons Board (PPB) providing comprehensive training in pharmaceutical sciences, "
            "medicinal chemistry, pharmacology and therapeutics, pharmaceutics and drug formulation, pharmacognosy (natural products), pharmaceutical analysis, "
            "clinical pharmacy practice, hospital and community pharmacy management, pharmacokinetics and pharmacodynamics, pharmaceutical microbiology, "
            "biopharmaceutics, pharmacy law and ethics, and pharmaceutical care. Students gain in-depth understanding of drug discovery, development, "
            "formulation, dispensing, and patient counseling. Laboratory-intensive program with extensive practical work in pharmaceutical chemistry, drug "
            "formulation, quality control testing, compounding, and dispensing. Clinical rotations in hospitals and community pharmacies provide hands-on "
            "experience in medication therapy management, patient counseling, drug information services, and pharmaceutical care. Students learn to use "
            "pharmacy management systems, understand drug interactions, dosage calculations, prescription interpretation, and medication safety protocols. "
            "The curriculum covers antimicrobial stewardship, pharmacovigilance, pharmacoeconomics, pharmaceutical marketing, and regulatory affairs. "
            "Industrial attachment in pharmaceutical manufacturing companies, hospital pharmacies, retail pharmacies, or regulatory bodies. Final year project "
            "involves pharmaceutical research, drug formulation development, or clinical pharmacy studies. Graduates must complete one-year internship and "
            "register with PPB to practice as pharmacists in Kenya."
        ),
        (
            "Graduates work as community pharmacists (retail pharmacy), hospital pharmacists, clinical pharmacists, pharmaceutical industry professionals "
            "(quality assurance, quality control, production, regulatory affairs, medical information, clinical research), pharmaceutical sales and marketing, "
            "drug information specialists, pharmacovigilance officers, or pharmaceutical regulatory officers. Employment in retail pharmacy chains (Goodlife "
            "Pharmacy, Carepoint Pharmacy, Medilife), hospitals (public and private), pharmaceutical manufacturing companies (GlaxoSmithKline, Regal "
            "Pharmaceuticals, Dawa Ltd, Beta Healthcare, Cosmos Pharmaceuticals), pharmaceutical wholesalers and distributors, Pharmacy and Poisons Board, "
            "Kenya Medical Supplies Authority (KEMSA), Mission for Essential Drugs and Supplies (MEDS), National Quality Control Laboratory, research "
            "institutions, NGOs (CHAI, MSH), or international organizations. Starting salaries: KSh 70,000-130,000 monthly. Many pharmacists establish their "
            "own retail pharmacies or consulting practices. Career advancement leads to senior pharmacist, chief pharmacist, pharmacy manager, pharmaceutical "
            "affairs manager, or director of pharmacy positions. Specialization opportunities in clinical pharmacy, industrial pharmacy, pharmaceutical "
            "analysis, or pharmacology. The pharmacy profession offers excellent career prospects with increasing healthcare needs and pharmaceutical industry "
            "growth. Further education: Master's in Clinical Pharmacy, Pharmaceutical Sciences, Pharmacology, Industrial Pharmacy, Public Health, or PhD for "
            "research and academic careers."
        ),
        "5 years (10 semesters including internship)",
        "Pharmacy and Poisons Board (PPB) / CUE"
    ))

    programs.append(make_program(
        "Bachelor of Science in Nursing",
        level,
        "Health Sciences > Nursing",
        "C+",
        36,
        [
            "Biology or Biological Sciences (Minimum C+ / 7 points)",
            "Chemistry or Physical Sciences (Minimum C plain / 6 points)",
            "English or Kiswahili (Minimum C plain / 6 points)",
            "Mathematics or any Group 2, 3, or 4 subject (Minimum C plain / 6 points)"
        ],
        (
            "A professional nursing degree approved by the Nursing Council of Kenya (NCK) providing comprehensive training in nursing theory, anatomy and "
            "physiology, medical-surgical nursing, community health nursing, maternal and child health nursing, psychiatric and mental health nursing, critical "
            "care nursing, nursing research, nursing management and leadership, pharmacology for nurses, pathophysiology, nutrition and dietetics, health "
            "assessment, and professional nursing practice. The program integrates theoretical classroom instruction with extensive clinical practice in "
            "hospitals and community health settings. Students develop essential nursing competencies including patient assessment, care planning, medication "
            "administration, wound care, IV therapy, catheterization, vital signs monitoring, patient education, infection control, emergency care, and "
            "documentation. Clinical rotations in medical wards, surgical wards, pediatric wards, maternity units, outpatient departments, intensive care units, "
            "operating theaters, psychiatric units, and community health centers provide hands-on patient care experience under supervision. Students learn "
            "nursing procedures, patient safety protocols, healthcare technology use, interprofessional collaboration, ethical decision-making, and cultural "
            "competence. The curriculum emphasizes evidence-based nursing practice, critical thinking, patient-centered care, health promotion, disease "
            "prevention, and holistic nursing care. Final year involves nursing research project and comprehensive clinical practice. Graduates must register "
            "with NCK to practice as professional nurses in Kenya."
        ),
        (
            "Graduates work as registered nurses in government hospitals (national, county, sub-county hospitals), private hospitals, mission hospitals, "
            "health centers, dispensaries, occupational health settings (industries, schools, companies), nursing homes, home-based care, military and police "
            "medical services, or international health organizations. Starting salary for government nurses: KSh 35,000-80,000 monthly depending on job group. "
            "Private sector often offers higher compensation. Career specialization opportunities through postgraduate training in critical care nursing, "
            "perioperative nursing, oncology nursing, nephrology nursing, emergency nursing, public health nursing, midwifery, neonatal nursing, or nurse "
            "anesthetist. Career progression leads to senior nurse, nurse in-charge, nursing officer, senior nursing officer, principal nursing officer, chief "
            "nursing officer, or matron/patron positions. Many nurses pursue master's degrees and transition to nursing education (college/university lecturers), "
            "nursing research, or healthcare administration. Opportunities in nursing consultancy, medical equipment companies, pharmaceutical companies, health "
            "insurance, or establishing private nursing services. International employment opportunities in countries with nursing shortages (UK, USA, Canada, "
            "Middle East, Australia). The nursing profession offers job security, personal fulfillment, and diverse career pathways. Further education: Master's "
            "in Nursing (various specializations), Master's in Public Health, Master's in Health Systems Management, PhD in Nursing for research and academic "
            "careers."
        ),
        "4 years (8 semesters)",
        "Nursing Council of Kenya (NCK) / CUE"
    ))

    # EDUCATION
    programs.append(make_program(
        "Bachelor of Education (Science)",
        level,
        "Education > Science Education",
        "C+",
        36,
        [
            "Two teaching subjects from: Mathematics, Physics, Chemistry, Biology (Minimum C+ / 7 points each)",
            "English or Kiswahili (Minimum C plain / 6 points)",
            "Any other subject"
        ],
        (
            "A professional teacher education degree focusing on science education, approved by the Teachers Service Commission (TSC). The program prepares "
            "graduate teachers for secondary schools, combining deep content knowledge in two science teaching subjects (commonly Mathematics with Physics, "
            "Chemistry, or Biology) with pedagogical training. Students study subject content at advanced level, science education methods, curriculum studies, "
            "educational psychology, educational assessment and evaluation, educational technology, educational philosophy, educational administration, classroom "
            "management, and teaching practice. The curriculum emphasizes science pedagogy including inquiry-based learning, hands-on experiments, science "
            "process skills, laboratory safety and management, use of teaching aids and demonstrations, integrating ICT in science teaching, and developing "
            "critical thinking and problem-solving skills in students. Students learn the Competency-Based Curriculum (CBC) framework, lesson planning, scheme "
            "of work preparation, examination setting and marking, continuous assessment, learner-centered approaches, differentiated instruction, and inclusive "
            "education. Teaching practice placements (typically two sessions) in secondary schools provide supervised classroom teaching experience with mentor "
            "teachers and university supervisors. Students teach actual classes, manage classrooms, assess students, and reflect on teaching practice. The "
            "program includes educational research methods with final year research project on science education topics. Graduates registered with TSC for "
            "employment as teachers in Kenyan secondary schools."
        ),
        (
            "Graduates work as secondary school teachers in government schools (national, county, sub-county secondary schools), private schools, international "
            "schools, or mission schools teaching their specialized science subjects. TSC employs most graduates with starting salary typically KSh 27,000-45,000 "
            "monthly (Job Group L-M) depending on qualifications and posting. Private schools may offer competitive salaries. Career progression through TSC job "
            "groups: Senior Teacher, Senior Master/Mistress, Deputy Principal, and Principal with corresponding salary increases. Opportunities beyond classroom "
            "teaching include educational administration (headship, TSC county/national offices), curriculum development at Kenya Institute of Curriculum "
            "Development (KICD), educational assessment at Kenya National Examinations Council (KNEC), quality assurance as TSC Quality Assurance and Standards "
            "Officers, educational consultancy, textbook writing and publishing, educational technology companies, or NGOs focused on education. Some teachers "
            "establish private tutorial centers, online teaching businesses, or educational content creation. The teaching profession offers job security, "
            "pension benefits, career progression opportunities, and personal fulfillment. Further education: Master of Education (MEd) in science education "
            "specializations, curriculum studies, educational administration, or educational technology leading to university lecturer positions or higher "
            "administrative roles; PhD in Education for research and academic leadership careers."
        ),
        "4 years (8 semesters)",
        "Teachers Service Commission (TSC) / CUE"
    ))

    programs.append(make_program(
        "Bachelor of Education (Arts)",
        level,
        "Education > Arts Education",
        "C+",
        36,
        [
            "Two teaching subjects from: English, Kiswahili, History, Geography, CRE/IRE, Business Studies (Minimum C+ / 7 points each)",
            "English or Kiswahili (Minimum C plain / 6 points)",
            "Any other subject"
        ],
        (
            "A professional teacher education degree for arts/humanities education, approved by TSC. The program prepares graduate teachers for secondary "
            "schools, combining deep content knowledge in two arts teaching subjects (commonly English with Kiswahili, History, Geography, Religious Education, "
            "or Business Studies) with pedagogical training. Students study subject content at advanced level, arts education methods, curriculum studies, "
            "educational psychology, educational assessment and evaluation, educational technology, educational philosophy, educational administration, classroom "
            "management, and teaching practice. The curriculum emphasizes arts pedagogy including language teaching methodologies, literature appreciation, "
            "historical analysis, geographical skills, critical thinking, discussion facilitation, debate and drama, creative writing, oral skills development, "
            "cultural appreciation, and values education. Students learn the Competency-Based Curriculum (CBC) framework, lesson planning, scheme of work "
            "preparation, examination setting and marking, continuous assessment, learner-centered approaches, differentiated instruction, inclusive education, "
            "and integrating ICT in arts teaching. Teaching practice placements (typically two sessions) in secondary schools provide supervised classroom "
            "teaching experience. Students teach actual classes, manage diverse learners, assess student work, use various teaching methods (group work, "
            "presentations, projects), and develop reflective practice. The program includes educational research methods with final year research project "
            "on arts education topics. Graduates registered with TSC for employment as teachers in Kenyan secondary schools."
        ),
        (
            "Graduates work as secondary school teachers in government schools (national, county, sub-county secondary schools), private schools, international "
            "schools, or mission schools teaching their specialized arts subjects. TSC employs most graduates with starting salary typically KSh 27,000-45,000 "
            "monthly (Job Group L-M). Career progression through TSC job groups: Senior Teacher, Senior Master/Mistress, Deputy Principal, and Principal. "
            "Opportunities beyond classroom teaching include educational administration (headship, TSC offices), curriculum development at KICD, educational "
            "assessment at KNEC, quality assurance as TSC Quality Assurance Officers, educational consultancy, textbook writing and publishing, journalism and "
            "media (especially for language teachers), public relations, corporate training, content development, translation services, or NGOs in education "
            "sector. History/Geography teachers may work in museums, cultural heritage sites, tourism sector, or research institutions. Language teachers may "
            "pursue opportunities in publishing, editing, translation, or language training institutes. Some establish private tutorial centers, online teaching "
            "platforms, or educational content creation businesses. The teaching profession offers job security, pension benefits, and career growth. Further "
            "education: Master of Education (MEd) in arts education specializations, curriculum studies, educational administration, language education, or "
            "educational technology leading to university lecturer positions; PhD in Education for research and academic leadership careers."
        ),
        "4 years (8 semesters)",
        "Teachers Service Commission (TSC) / CUE"
    ))

    return programs


# ============================================================
# DIPLOMA PROGRAMS (Minimum: C- / 5 points)
# ============================================================

def generate_diploma_programs() -> List[Dict]:
    """Generate comprehensive diploma programs."""
    level = "Diploma"
    programs = []

    # ICT DIPLOMAS
    programs.append(make_program(
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
        (
            "A comprehensive practical IT diploma providing hands-on training in computer applications (Microsoft Office Suite, Google Workspace), basic "
            "programming (Python, Java basics), web development (HTML, CSS, JavaScript, PHP), database management (MySQL, MS Access), computer networking "
            "fundamentals (TCP/IP, LAN setup, troubleshooting), operating systems (Windows, Linux basics), IT support and troubleshooting, cybersecurity "
            "basics, system administration basics, and hardware maintenance. Students gain practical skills through extensive lab sessions building websites, "
            "creating databases, configuring networks, troubleshooting systems, and developing simple applications. The curriculum covers office automation, "
            "digital literacy, computer graphics basics (Photoshop, CorelDraw), introduction to cloud computing, mobile apps overview, and IT project "
            "management basics. Industrial attachment (8-12 weeks) in IT departments, cyber cafes, computer shops, or tech companies provides real-world "
            "experience. Final project involves developing a complete IT solution such as a website, database system, or network setup. Program prepares "
            "graduates for entry to mid-level IT positions in various organizations. Duration typically 2-3 years depending on institution."
        ),
        (
            "Graduates work as IT support technicians, computer lab technicians, network administrators (small networks), web developers, database assistants, "
            "system administrators, help desk officers, IT officers in SMEs, cyber cafe managers, computer trainers, or ICT teachers in colleges. Employment "
            "opportunities in government offices, county governments, schools and colleges, hospitals, banks, microfinance institutions, SACCOs, retail "
            "businesses, hotels, NGOs, computer shops, ISPs, and SMEs needing IT support. Starting salaries: KSh 25,000-50,000 monthly. Many establish "
            "computer businesses (sales, repairs, cyber cafes), provide freelance web development, offer IT consultancy to small businesses, or provide "
            "computer training services. Career growth through gaining experience, professional certifications (CompTIA A+, Network+, CCNA, Microsoft "
            "certifications), and specialization in networking, web development, or systems administration. Further education: Upgrade to Bachelor's degree "
            "in IT/Computer Science for enhanced career prospects, specialized certifications, or professional courses in specific technologies."
        ),
        "2-3 years (4-6 semesters)",
        "KNEC / Technical and Vocational Education and Training Authority (TVETA)"
    ))

    programs.append(make_program(
        "Diploma in Software Engineering",
        level,
        "ICT > Software Engineering",
        "C-",
        24,
        [
            "Mathematics (Minimum C- / 5 points)",
            "English or Kiswahili (Minimum D+ / 4 points)",
            "Physics, Computer Studies, or any science subject (Minimum D+ / 4 points)",
            "Any other subject"
        ],
        (
            "A specialized diploma focusing on software development and programming, covering programming fundamentals (Python, Java, C++), object-oriented "
            "programming, data structures and algorithms, software engineering principles, web application development (HTML, CSS, JavaScript, React, PHP, "
            "Laravel), mobile app development (Android, Flutter basics), database design and management (MySQL, PostgreSQL), software testing and quality "
            "assurance, version control (Git, GitHub), API development, software project management basics, and system analysis and design. Students develop "
            "practical programming skills through extensive coding assignments, individual projects, group projects, and hackathons. The curriculum emphasizes "
            "problem-solving, algorithm design, clean code practices, debugging techniques, software documentation, and Agile development methodologies. "
            "Students build complete software applications including web applications, mobile apps, desktop applications, and database-driven systems. "
            "Covers user interface design basics, user experience considerations, software security fundamentals, and deployment processes. Industrial "
            "attachment in software companies, IT departments, or tech startups provides exposure to professional software development environments. Final "
            "year project involves developing a comprehensive software system with proper documentation, testing, and presentation."
        ),
        (
            "Graduates work as junior software developers, web developers, mobile app developers (junior), front-end developers, back-end developers, full-stack "
            "developers (junior), software testers, quality assurance testers, junior programmers, IT support (development team), technical support engineers, "
            "or freelance developers. Employment in software development companies, fintech companies, digital agencies, telecommunications companies, banks' "
            "IT departments, e-commerce companies, startups, government ICT departments, or tech consulting firms. Starting salaries: KSh 30,000-65,000 monthly "
            "depending on skills and portfolio. Many graduates work as freelance developers on platforms like Upwork, Fiverr, or Freelancer, earning "
            "international rates. Some establish software development startups creating mobile apps, web applications, or software solutions for local "
            "businesses. Career advancement through building strong portfolio, mastering frameworks and technologies, contributing to open-source projects, "
            "and continuous learning. Professional certifications enhance prospects: AWS Certified Developer, Google Associate Android Developer, Microsoft "
            "Certified developer certifications, or specific technology certifications. Further education: Upgrade to Bachelor's in Software Engineering, "
            "Computer Science, or IT for senior developer roles and better career progression."
        ),
        "2-3 years (4-6 semesters)",
        "KNEC / TVETA"
    ))

    programs.append(make_program(
        "Diploma in Computer Networking",
        level,
        "ICT > Computer Networking",
        "C-",
        22,
        [
            "Mathematics (Minimum D+ / 4 points)",
            "English or Kiswahili (Minimum D+ / 4 points)",
            "Physics or Computer Studies (Minimum D / 3 points)",
            "Any other subject"
        ],
        (
            "A specialized networking diploma providing comprehensive training in computer networks, network design and implementation, network protocols "
            "(TCP/IP, DNS, DHCP, HTTP, FTP), network hardware (routers, switches, hubs, cables), LAN/WAN technologies, wireless networking (Wi-Fi standards, "
            "configuration), network security fundamentals, firewall configuration, VPN setup, network troubleshooting and diagnostics, network monitoring "
            "and management, Windows Server and Linux server administration, Active Directory basics, cloud networking basics, and network documentation. "
            "The program is often aligned with Cisco CCNA curriculum, providing strong foundation for industry certifications. Students gain hands-on "
            "experience through extensive laboratory work: setting up networks, configuring routers and switches, implementing security measures, "
            "troubleshooting network problems, installing cabling systems, configuring wireless access points, and managing network services. Covers "
            "network planning, IP addressing and subnetting, routing protocols, switching technologies, network performance optimization, disaster recovery "
            "planning, and network policy development. Industrial attachment in ISPs, telecommunications companies, IT departments, or networking firms "
            "provides practical experience with enterprise networks. Final project involves designing and implementing a complete network solution with "
            "proper documentation, security implementation, and performance testing."
        ),
        (
            "Graduates work as network administrators, network technicians, network support engineers, system administrators, IT support engineers, network "
            "security technicians, wireless network specialists, ISP technicians, telecommunications technicians, or network operations center (NOC) engineers. "
            "Employment in ISPs (Safaricom, Airtel, Telkom, Zuku, Liquid Telecom, Jamii Telecommunications), telecommunications companies, IT companies, "
            "banks and financial institutions, corporate organizations with large networks, government ministries, educational institutions, hospitals, hotels, "
            "manufacturing companies, BPO centers, or networking solution providers. Starting salaries: KSh 30,000-60,000 monthly. Many establish network "
            "installation and maintenance businesses, ISP services for specific areas, network consultancy for SMEs, or CCTV and security systems installation "
            "(often combined with networking). Career advancement through experience and professional certifications significantly improves prospects and "
            "earning potential: Cisco CCNA (essential), CCNP, CompTIA Network+, CompTIA Security+, Microsoft network certifications, or specialized vendor "
            "certifications. Senior positions include senior network administrator, network engineer, network architect, or IT manager. Further education: "
            "Upgrade to Bachelor's in IT, Computer Networks, or telecommunications for career advancement to network engineering and architecture roles."
        ),
        "2-3 years (4-6 semesters)",
        "KNEC / TVETA / Cisco Academy alignment"
    ))

    
    programs.append(make_program(
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
        (
            "A comprehensive business diploma covering principles of management, business communication, organizational behavior, business mathematics and "
            "statistics, accounting basics, marketing principles, human resource management basics, entrepreneurship and small business management, business "
            "law, office management and administration, customer service and public relations, sales management, operations management basics, and business "
            "planning. Students develop practical business skills through case studies, group projects, business simulations, presentations, business plan "
            "development, and research assignments. The curriculum emphasizes practical application of management concepts, decision-making skills, leadership "
            "basics, teamwork, communication skills, problem-solving, and professional conduct. Covers business correspondence, report writing, meeting "
            "management, record keeping, business ethics, computer applications for business (MS Excel, Word, PowerPoint), and introduction to digital business. "
            "Industrial attachment (8-12 weeks) in companies, SACCOs, government offices, or NGOs provides exposure to real business operations and "
            "management practices. Final project involves developing a comprehensive business plan or conducting business research on contemporary management "
            "issues. Program prepares graduates for supervisory and middle management positions in various organizations or for entrepreneurship."
        ),
        (
            "Graduates work as administrative assistants, office administrators, supervisors, junior managers, sales representatives, customer service officers, "
            "operations assistants, procurement assistants, business development assistants, branch coordinators, retail store supervisors, or start their own "
            "small businesses. Employment opportunities in banks, microfinance institutions, SACCOs, insurance companies, retail businesses, wholesale companies, "
            "manufacturing firms, service companies, hotels, transport companies, government offices, county governments, NGOs, or educational institutions. "
            "Starting salaries: KSh 20,000-45,000 monthly depending on organization and role. The diploma provides strong foundation for entrepreneurship - "
            "many graduates successfully establish retail shops, service businesses, trading businesses, consultancy practices, or become suppliers to "
            "organizations. Career progression through experience leads to management positions: office manager, operations manager, branch manager, or "
            "business owner/entrepreneur. Professional development through short courses (customer service, sales, leadership) and professional certifications "
            "(CIM - Chartered Institute of Marketing, CIPS - Chartered Institute of Procurement and Supply, CHRP) enhances career prospects. Further education: "
            "Upgrade to Bachelor of Commerce, BBA, or specialized Bachelor's degrees for career advancement to senior management positions; professional "
            "accounting qualifications (CPA) for accounting careers; or MBA for executive roles."
        ),
        "2-3 years (4-6 semesters)",
        "KNEC / TVETA"
    ))

    programs.append(make_program(
        "Diploma in Accounting",
        level,
        "Business > Accounting",
        "C-",
        22,
        [
            "Mathematics or Business Studies (Minimum D+ / 4 points)",
            "English or Kiswahili (Minimum D+ / 4 points)",
            "Any other two subjects"
        ],
        (
            "A specialized accounting diploma providing comprehensive training in financial accounting, cost accounting, management accounting, auditing basics, "
            "taxation (KRA tax system - income tax, VAT, PAYE), bookkeeping, computerized accounting (Sage, QuickBooks, Pastel), business mathematics, business "
            "statistics, commercial law and business law, principles of management, financial management basics, and accounting ethics. Students develop strong "
            "numerical, analytical, and record-keeping skills through extensive practical exercises, case studies, financial statement preparation, and "
            "accounting software training. The curriculum covers the full accounting cycle, preparation of financial statements, bank reconciliations, payroll "
            "processing, budgeting basics, cash management, credit control, inventory accounting, and financial analysis basics. Emphasizes accuracy, attention "
            "to detail, ethical conduct, confidentiality, and professional standards in accounting practice. Students learn to use accounting software packages, "
            "Excel for accounting purposes, and understand accounting standards. Industrial attachment (8-12 weeks) in accounting departments, audit firms, "
            "banks, or SACCOs provides practical exposure to accounting operations, bookkeeping systems, financial reporting, and professional accounting "
            "environments. Final project typically involves comprehensive accounting case study, financial analysis, or accounting system documentation. The "
            "diploma provides foundation for professional accounting qualifications and prepares graduates for entry-level accounting positions."
        ),
        (
            "Graduates work as accounts clerks, bookkeepers, accounts assistants, junior accountants, cashiers, accounts payable/receivable clerks, payroll "
            "clerks, audit assistants, tax assistants, finance assistants, accounts officers, or credit control officers. Employment in commercial banks, "
            "microfinance institutions, SACCOs, audit firms, accounting firms, insurance companies, manufacturing companies, retail businesses, hospitals, "
            "hotels, schools and colleges, government offices, county governments, NGOs, or any organization requiring accounting services. Starting salaries: "
            "KSh 18,000-40,000 monthly depending on organization and location. Many graduates pursue professional accounting qualifications: CPA (K) through "
            "ICPAK - the diploma provides exemptions in some CPA papers; ACCA (Association of Chartered Certified Accountants); or CIMA (Chartered Institute "
            "of Management Accountants). Qualified professional accountants earn significantly higher (KSh 60,000-200,000+ monthly). Career progression leads "
            "to accounts officer, accountant, senior accountant, accounts supervisor, or finance officer positions. Some experienced accountants establish "
            "bookkeeping services, tax consultancy practices, or accounting firms serving SMEs. Further education: Upgrade to Bachelor of Commerce (Accounting), "
            "continue with CPA (K) professional qualification, pursue ACCA or CIMA, or take specialized courses in taxation, auditing, or financial management "
            "for career advancement to senior accounting and finance positions."
        ),
        "2-3 years (4-6 semesters)",
        "KNEC / TVETA / ICPAK (some exemptions)"
    ))

    programs.append(make_program(
        "Diploma in Sales and Marketing",
        level,
        "Business > Marketing",
        "C-",
        20,
        [
            "English or Kiswahili (Minimum D+ / 4 points)",
            "Mathematics or Business Studies (Minimum D+ / 4 points)",
            "Any other two subjects"
        ],
        (
            "A practical marketing diploma covering principles of marketing, consumer behavior, marketing research basics, sales management, advertising and "
            "promotion, public relations, brand management basics, digital marketing fundamentals (social media marketing, email marketing, online advertising), "
            "customer relationship management, retail management, distribution and logistics basics, marketing communications, business communication, "
            "entrepreneurship, and marketing strategy basics. Students develop sales and marketing skills through practical assignments, marketing plans, "
            "promotional campaigns, field assignments, market surveys, presentations, and sales simulations. The curriculum emphasizes understanding customer "
            "needs, market segmentation, targeting and positioning, marketing mix (4Ps), competitive analysis, sales techniques, negotiation skills, customer "
            "service excellence, and professional selling. Covers marketing metrics, sales forecasting basics, territory management, merchandising, product "
            "knowledge development, and use of CRM systems. Students learn digital marketing tools including social media platforms (Facebook, Instagram, "
            "Twitter, LinkedIn), content creation, basic graphic design (Canva), and online marketing strategies. Industrial attachment (8-12 weeks) in "
            "marketing departments, sales companies, advertising agencies, retail companies, or FMCG companies provides hands-on experience in real marketing "
            "and sales environments. Final project involves developing a comprehensive marketing plan, conducting market research, or analyzing marketing "
            "campaigns. Program prepares graduates for sales and marketing positions in various industries."
        ),
        (
            "Graduates work as sales representatives, sales executives, marketing assistants, marketing officers, brand ambassadors, customer relationship "
            "officers, retail sales supervisors, merchandisers, marketing coordinators, sales coordinators, digital marketing assistants, social media managers "
            "(entry-level), business development officers, account managers (junior), or sales consultants. Employment opportunities in FMCG companies (Unilever, "
            "Procter & Gamble, Coca-Cola, Bidco, Unga Group), pharmaceutical companies, telecommunications companies (Safaricom, Airtel), banks and financial "
            "institutions, insurance companies, media houses, advertising agencies, real estate firms, hotels and hospitality, retail chains, manufacturing "
            "companies, distributors and wholesalers, or startups. Starting salaries: KSh 20,000-50,000 monthly plus commissions (sales roles often include "
            "significant commission components). Sales careers offer high earning potential based on performance. Many graduates establish their own businesses "
            "(distributorships, retail shops, marketing consultancy, event management, digital marketing agencies) or work as independent sales agents. Career "
            "progression leads to senior sales executive, marketing manager, sales manager, regional sales manager, brand manager, or marketing director "
            "positions. Professional certification enhances prospects: CIM (Chartered Institute of Marketing) - highly valued, digital marketing certifications "
            "(Google Digital Marketing, Facebook Blueprint, HubSpot), or sales training programs. Further education: Upgrade to Bachelor's in Marketing, Business "
            "Administration, or Commerce for senior marketing and sales management positions; MBA Marketing for executive roles."
        ),
        "2-3 years (4-6 semesters)",
        "KNEC / TVETA / CIM Kenya"
    ))

    programs.append(make_program(
        "Diploma in Supply Chain Management",
        level,
        "Business > Supply Chain",
        "C-",
        22,
        [
            "Mathematics or Business Studies (Minimum D+ / 4 points)",
            "English or Kiswahili (Minimum D+ / 4 points)",
            "Any other two subjects"
        ],
        (
            "A specialized diploma covering procurement and purchasing, inventory management, warehousing and storage, logistics and distribution, supply chain "
            "planning, vendor management, contract management basics, stores management, materials handling, transport and fleet management basics, supply chain "
            "information systems, procurement law and regulations (Public Procurement and Asset Disposal Act), business ethics and integrity in procurement, "
            "and supply chain performance metrics. Students develop practical skills in supplier selection, purchase requisition processing, quotation analysis, "
            "tender evaluation, order processing, inventory control techniques (EOQ, ABC analysis, JIT), stock valuation, warehouse layout and operations, and "
            "supply chain software basics. The curriculum covers the full procurement cycle, sourcing strategies, supplier relationship management, quality "
            "assurance in supply chain, cost management, supply chain risk management, and sustainable supply chain practices. Emphasizes compliance with "
            "procurement regulations, ethical conduct, transparency, value for money, and professional standards. Students learn to use procurement management "
            "systems, inventory management software, and Microsoft Excel for supply chain analysis. Industrial attachment (8-12 weeks) in procurement departments, "
            "warehouses, logistics companies, or supply chain operations provides hands-on experience. Final project involves supply chain case analysis, "
            "procurement process improvement, or inventory optimization study. Program prepares graduates for supply chain and procurement careers."
        ),
        (
            "Graduates work as procurement officers, purchasing officers, stores officers, inventory controllers, warehouse assistants, logistics coordinators, "
            "supply chain assistants, procurement assistants, materials controllers, buyer assistants, or fleet assistants. Employment in manufacturing companies, "
            "retail chains, wholesale distributors, logistics companies (DHL, G4S, Wells Fargo), transport companies, hospitals, hotels, educational institutions, "
            "government ministries, county governments, state corporations, NGOs, international organizations, banks, or any organization with procurement "
            "departments. Starting salaries: KSh 25,000-50,000 monthly. Career progression leads to senior procurement officer, procurement manager, supply chain "
            "manager, logistics manager, warehouse manager, or procurement director positions. Professional certification highly valued and often required: CIPS "
            "(Chartered Institute of Procurement and Supply) UK qualification - globally recognized, KISM (Kenya Institute of Supplies Management) certification. "
            "These certifications significantly enhance career prospects and earning potential (certified procurement professionals earn KSh 60,000-200,000+ "
            "monthly). Some graduates establish procurement consultancy services, logistics businesses, or become procurement specialists for SMEs. Further "
            "education: Upgrade to Bachelor's in Procurement and Supply Chain Management, Business Administration, or Commerce; pursue CIPS professional "
            "qualification; take specialized courses in logistics, transport management, or warehousing for senior supply chain management positions."
        ),
        "2-3 years (4-6 semesters)",
        "KNEC / TVETA / KISM affiliation"
    ))

    # ENGINEERING DIPLOMAS
    programs.append(make_program(
        "Diploma in Electrical and Electronic Engineering",
        level,
        "Engineering > Electrical & Electronic",
        "C-",
        26,
        [
            "Mathematics (Minimum C- / 5 points)",
            "Physics or Physical Sciences (Minimum C- / 5 points)",
            "English or Kiswahili (Minimum D+ / 4 points)",
            "Chemistry or any other science subject"
        ],
        (
            "A comprehensive engineering diploma covering electrical circuit theory, electronics and microelectronics, electrical power systems, electrical "
            "machines and drives, control systems basics, digital electronics, electrical installation and wiring, PLC programming basics, instrumentation, "
            "power electronics, renewable energy systems basics, electrical workshop practice, electrical engineering drawing (AutoCAD Electrical basics), and "
            "electrical safety standards. Students develop practical skills through extensive laboratory work and workshop sessions including circuit assembly "
            "and testing, electrical wiring (domestic and industrial), motor installation and maintenance, PLC programming, electronic circuit construction, "
            "PCB design basics, transformer testing, power measurement, and troubleshooting electrical systems. The curriculum covers electrical installation "
            "standards and codes, electrical safety regulations, use of electrical testing equipment (multimeters, oscilloscopes, function generators, power "
            "meters), electrical maintenance procedures, and technical documentation. Students learn electrical estimation and costing, project planning basics, "
            "and work supervision. Industrial attachment (8-12 weeks) in electrical contracting firms, manufacturing industries, KPLC, or maintenance departments "
            "provides real-world exposure. Final project involves designing and implementing an electrical system or solving practical electrical engineering "
            "problems. Program prepares graduates for technician roles and provides pathway to engineering registration with EBK as Engineering Technicians."
        ),
        (
            "Graduates work as electrical technicians, electrical installation supervisors, maintenance technicians, electrical estimators, electrical inspectors, "
            "PLC technicians, instrumentation technicians, electrical drafters, power systems technicians, renewable energy technicians, or electrical supervisors. "
            "Employment in Kenya Power (KPLC), KETRACO, KenGen, GDC, electrical contracting companies, manufacturing industries (EABL, Bamburi, BAT), construction "
            "companies, telecommunications companies, county governments, real estate developers, hospitals, hotels, educational institutions, or maintenance "
            "service providers. Starting salaries: KSh 25,000-55,000 monthly. Many establish electrical contracting businesses, solar installation companies, "
            "or electrical maintenance services after gaining experience. The diploma provides foundation for professional engineering progression: graduates can "
            "register with EBK as Engineering Technicians, gain work experience, and potentially upgrade qualifications. Career advancement leads to senior "
            "technician, electrical supervisor, electrical foreman, electrical engineer (with further education), or electrical contractor positions. Further "
            "education: Upgrade to Bachelor of Engineering (Electrical) through bridging programs for full engineering qualifications and professional engineer "
            "registration; specialized courses in PLC programming, SCADA systems, solar energy systems, or electrical maintenance management enhance skills and "
            "career prospects."
        ),
        "3 years (6 semesters)",
        "KNEC / TVETA / Engineers Board of Kenya (Technician level)"
    ))

    programs.append(make_program(
        "Diploma in Civil Engineering",
        level,
        "Engineering > Civil",
        "C-",
        26,
        [
            "Mathematics (Minimum C- / 5 points)",
            "Physics or Physical Sciences (Minimum C- / 5 points)",
            "English or Kiswahili (Minimum D+ / 4 points)",
            "Chemistry, Geography, or any science subject"
        ],
        (
            "A comprehensive civil engineering diploma covering engineering mathematics, engineering mechanics, strength of materials, structural analysis basics, "
            "building construction technology, surveying and leveling, engineering drawing and AutoCAD basics, concrete technology and testing, soil mechanics "
            "and foundation engineering basics, highway engineering, hydraulics and water supply, drainage and sanitation, construction materials and testing, "
            "quantity surveying basics, construction project management basics, and civil engineering workshop practice. Students develop practical skills through "
            "extensive fieldwork and laboratory sessions including land surveying (leveling, traversing, contouring), materials testing (concrete, aggregates, "
            "soil), setting out building works, structural drawing, construction methods, and site supervision basics. The curriculum covers construction codes "
            "and standards, building regulations, construction safety, construction estimation and costing, interpretation of construction drawings, construction "
            "equipment, and construction documentation. Students learn computer-aided design using AutoCAD for civil engineering drawings and basic structural "
            "design software. Industrial attachment (8-12 weeks) on construction sites, consulting firms, road agencies, or county governments provides hands-on "
            "experience in construction supervision, surveying, materials testing, or site engineering. Final project involves practical civil engineering problem "
            "such as building design, survey project, road design, water supply design, or construction case study. Program prepares graduates for technician "
            "roles and pathway to EBK registration as Engineering Technicians."
        ),
        (
            "Graduates work as civil engineering technicians, site supervisors, survey technicians, materials testing technicians, quantity surveying assistants, "
            "construction supervisors, draughtspersons (civil), clerk of works, site engineers (technician level), roads technicians, water supply technicians, "
            "or building inspectors. Employment in construction companies (China Road and Bridge, China Wu Yi, Civicon), consulting engineering firms, government "
            "road agencies (KeNHA, KURA, KeRRA), county governments (roads and public works departments), NCA, real estate developers, building contractors, "
            "water companies, materials testing laboratories, or survey firms. Starting salaries: KSh 25,000-60,000 monthly depending on employer and location. "
            "Many establish construction businesses (building contractors, survey services, materials supply), consultancy practices, or become independent "
            "construction supervisors after gaining experience. Career progression leads to senior technician, site supervisor, resident technician, assistant "
            "engineer, or project supervisor positions. The diploma provides foundation for engineering progression: graduates can register with EBK as "
            "Engineering Technicians. Further education: Upgrade to Bachelor of Engineering (Civil) through bridging programs for full engineering qualifications "
            "and professional engineer registration; specialized training in AutoCAD Civil 3D, STAAD Pro, quantity surveying, project management, or construction "
            "management enhances career prospects and earning potential."
        ),
        "3 years (6 semesters)",
        "KNEC / TVETA / Engineers Board of Kenya (Technician level)"
    ))

    programs.append(make_program(
        "Diploma in Mechanical Engineering",
        level,
        "Engineering > Mechanical",
        "C-",
        26,
        [
            "Mathematics (Minimum C- / 5 points)",
            "Physics or Physical Sciences (Minimum C- / 5 points)",
            "English or Kiswahili (Minimum D+ / 4 points)",
            "Chemistry or any science subject"
        ],
        (
            "A comprehensive mechanical engineering diploma covering engineering mathematics, engineering mechanics (statics and dynamics), strength of materials, "
            "thermodynamics, fluid mechanics basics, machine design basics, manufacturing processes (machining, welding, fitting), workshop technology and "
            "practice, engineering drawing and AutoCAD basics, materials science, maintenance engineering, power engineering (engines, boilers), refrigeration "
            "and air conditioning basics, hydraulics and pneumatics, and industrial safety. Students develop strong practical skills through extensive workshop "
            "training including lathe operations, milling, drilling, grinding, welding (arc, gas, MIG), sheet metal work, fitting and assembly, and basic CNC "
            "operations. The curriculum covers machine maintenance procedures, troubleshooting techniques, preventive maintenance planning, spare parts management, "
            "technical documentation, and workshop safety standards. Students learn to read engineering drawings, use measuring instruments (micrometers, vernier "
            "calipers), understand engineering specifications, and apply quality control procedures. Industrial attachment (8-12 weeks) in manufacturing companies, "
            "maintenance departments, automotive workshops, or engineering firms provides real-world experience. Final project involves practical mechanical "
            "engineering problem such as machine design, fabrication project, maintenance optimization study, or mechanical system analysis. Program prepares "
            "graduates for technician roles and pathway to EBK registration as Engineering Technicians."
        ),
        (
            "Graduates work as mechanical technicians, maintenance technicians, production technicians, workshop supervisors, machine operators (CNC, conventional), "
            "maintenance supervisors, plant technicians, automotive technicians, HVAC technicians, quality control technicians, or fabrication supervisors. "
            "Employment in manufacturing companies (EABL, Bamburi Cement, Coca-Cola, BAT, Bidco), automotive companies (Toyota, Isuzu, CMC Motors), energy "
            "companies (KenGen, GDC, Kenya Pipeline), construction equipment companies, hotels and hospitality (maintenance), hospitals (biomedical equipment), "
            "sugar factories, tea factories, engineering workshops, county governments, or maintenance service providers. Starting salaries: KSh 25,000-60,000 "
            "monthly. Many establish mechanical workshops, welding and fabrication businesses, machinery maintenance services, or automotive repair shops after "
            "gaining experience and capital. The mechanical engineering field offers diverse opportunities across many industries. Career progression leads to "
            "senior technician, maintenance supervisor, workshop foreman, plant supervisor, or maintenance engineer (with further education) positions. The "
            "diploma provides foundation for engineering progression: graduates can register with EBK as Engineering Technicians. Further education: Upgrade to "
            "Bachelor of Engineering (Mechanical) through bridging programs for full engineering qualifications and professional engineer registration; specialized "
            "training in CNC programming, welding certifications, HVAC systems, automotive technology, or maintenance management enhances career prospects."
        ),
        "3 years (6 semesters)",
        "KNEC / TVETA / Engineers Board of Kenya (Technician level)"
    ))

    # HEALTH SCIENCES DIPLOMAS
    programs.append(make_program(
        "Diploma in Clinical Medicine and Surgery",
        level,
        "Health Sciences > Clinical Medicine",
        "C-",
        30,
        [
            "Biology or Biological Sciences (Minimum C- / 5 points)",
            "Chemistry or Physical Sciences (Minimum C- / 5 points)",
            "English or Kiswahili (Minimum D+ / 4 points)",
            "Mathematics or Physics (Minimum D+ / 4 points)"
        ],
        (
            "A comprehensive medical diploma approved by the Clinical Officers Council training clinical officers to provide medical services. The program covers "
            "anatomy and physiology, pathology, pharmacology, microbiology, medical-surgical nursing, medicine (internal medicine, pediatrics), surgery (general "
            "surgery, orthopedics), obstetrics and gynecology, psychiatry, community health, emergency medicine, clinical examination and diagnosis, minor "
            "surgical procedures, wound management, and clinical therapeutics. Students develop practical clinical skills through extensive hospital rotations "
            "in medical wards, surgical wards, pediatric departments, maternity units, outpatient clinics, casualty/emergency departments, and community health "
            "settings. Learn patient history taking, physical examination, vital signs monitoring, diagnosis formulation, treatment planning, prescription "
            "writing, minor surgery (suturing, incision and drainage, circumcision), wound dressing, plaster of Paris application, normal delivery assistance, "
            "family planning services, immunization, health education, and medical documentation. The curriculum emphasizes clinical decision-making, emergency "
            "management (resuscitation, trauma care), infection prevention, patient safety, medical ethics, and referral protocols. Students gain experience in "
            "laboratory specimen collection, interpretation of basic lab results and x-rays, and use of medical equipment. Final year involves comprehensive "
            "clinical practice and research project. Graduates must register with Clinical Officers Council to practice in Kenya."
        ),
        (
            "Graduates work as clinical officers in government health facilities (county hospitals, sub-county hospitals, health centers, dispensaries), private "
            "hospitals and clinics, mission hospitals, nursing homes, occupational health settings (industries, schools, companies), military and police medical "
            "services, prison health services, or establish private clinics. Starting salary for government clinical officers: KSh 30,000-65,000 monthly depending "
            "on job group and location (hardship allowances for remote areas). Private sector may offer competitive packages. Clinical officers are essential "
            "healthcare providers in Kenya, especially in rural and underserved areas where they often work independently. They perform diverse duties: diagnosing "
            "and treating diseases, performing minor surgeries, conducting deliveries, managing emergencies, health education, disease surveillance, and supervising "
            "lower cadre health workers. Career progression through government job groups leads to senior clinical officer, clinical officer in-charge of health "
            "facilities, or administrative positions in health departments. Further education highly encouraged: upgrade to Bachelor of Medicine and Surgery (MBChB) "
            "through special bridging programs offered by some universities, pursue Bachelor's in Clinical Medicine and Community Health, specialize through "
            "higher diplomas in Emergency Medicine, Anesthesia, Ophthalmology, Orthopedics, or pursue Master's in Public Health. The clinical officer profession "
            "offers job security, opportunity to serve communities, and pathways for career advancement through further education and specialization."
        ),
        "3 years (6 semesters)",
        "Clinical Officers Council / KNEC / TVETA"
    ))

    programs.append(make_program(
        "Diploma in Kenya Registered Community Health Nursing",
        level,
        "Health Sciences > Community Health Nursing",
        "C-",
        28,
        [
            "Biology or Biological Sciences (Minimum C- / 5 points)",
            "Chemistry or Physical Sciences (Minimum D+ / 4 points)",
            "English or Kiswahili (Minimum D+ / 4 points)",
            "Mathematics or any other subject"
        ],
        (
            "A professional nursing diploma approved by the Nursing Council of Kenya focusing on community health nursing and primary healthcare delivery. The "
            "program covers anatomy and physiology, nutrition and dietetics, microbiology, pharmacology, nursing fundamentals, medical-surgical nursing, maternal "
            "and child health (MCH), family planning, communicable disease nursing, non-communicable disease management, community health nursing, health education "
            "and promotion, epidemiology basics, environmental health, mental health nursing, nursing management and administration, and nursing ethics. Students "
            "develop essential nursing skills through practical training in hospitals and community settings: patient assessment, vital signs monitoring, medication "
            "administration (oral, IM, IV), wound dressing, catheterization, IV therapy, immunization, antenatal and postnatal care, normal delivery, newborn care, "
            "growth monitoring, health education, home visits, disease surveillance, and outreach activities. Clinical practice in hospitals (medical, surgical, "
            "pediatric, maternity wards) and community placements (health centers, dispensaries, community health programs) provide hands-on experience. The "
            "curriculum emphasizes primary healthcare approach, disease prevention, health promotion, community participation, cultural sensitivity, and public "
            "health interventions. Students learn to manage common health conditions, identify health needs, plan health interventions, work with community health "
            "volunteers, and maintain health records. Final year involves comprehensive clinical practice and nursing research project. Graduates must register "
            "with Nursing Council of Kenya as Kenya Registered Community Health Nurses (KRCHN)."
        ),
        (
            "Graduates work as registered community health nurses in government health facilities (health centers, dispensaries, sub-county hospitals), county "
            "health departments (community health units, disease surveillance), private clinics, mission health facilities, NGO health programs (community health "
            "projects, maternal health, HIV/AIDS programs), occupational health (industries, schools), home-based care programs, or establish private nursing "
            "services. Starting salary for government nurses: KSh 25,000-50,000 monthly depending on job group. Community health nurses play vital role in Kenya's "
            "healthcare system, especially in rural areas and underserved communities, providing primary healthcare services, health education, disease prevention, "
            "and connecting communities with health services. Career progression leads to senior enrolled nurse, nurse in-charge of health facilities (dispensaries, "
            "health centers), public health officer, or community health coordinator positions. Further education highly recommended: upgrade to Bachelor of Science "
            "in Nursing through bridging programs (1-2 years) for better career prospects and higher positions; specialize through post-basic diplomas in midwifery, "
            "critical care, theater nursing, public health nursing; pursue Master's in Nursing or Public Health for leadership, education, or management roles. "
            "Opportunities exist in international health organizations, health research, community health training, or nursing education in colleges. The profession "
            "offers job security, opportunity to serve communities, and personal fulfillment through improving health outcomes."
        ),
        "2.5-3 years (5-6 semesters)",
        "Nursing Council of Kenya / KNEC / TVETA"
    ))

    programs.append(make_program(
        "Diploma in Pharmaceutical Technology",
        level,
        "Health Sciences > Pharmacy",
        "C-",
        28,
        [
            "Chemistry or Physical Sciences (Minimum C- / 5 points)",
            "Biology or Biological Sciences (Minimum C- / 5 points)",
            "Mathematics (Minimum D+ / 4 points)",
            "English or Kiswahili (Minimum D+ / 4 points)"
        ],
        (
            "A pharmaceutical diploma approved by the Pharmacy and Poisons Board training pharmaceutical technologists for pharmacy practice. The program covers "
            "pharmaceutical chemistry, pharmaceutics (drug formulation), pharmacology, pharmacognosy (medicinal plants), pharmaceutical microbiology, pharmaceutical "
            "analysis and quality control, dispensing practice, pharmacy law and ethics, hospital and community pharmacy practice, pharmaceutical calculations, "
            "pharmaceutical management, and patient counseling basics. Students develop practical pharmacy skills through extensive laboratory work and pharmacy "
            "practice: drug compounding and formulation, tablet preparation, ointment preparation, liquid preparations, drug identification, drug storage and "
            "handling, prescription interpretation and dispensing, pharmaceutical calculations, drug interactions checking, patient counseling, inventory management, "
            "and pharmacy records. Clinical attachments in hospital pharmacies and community pharmacies provide hands-on experience in real pharmacy environments. "
            "The curriculum covers drug classifications, dosage forms, routes of administration, common diseases and their treatments, rational drug use, medication "
            "safety, adverse drug reactions, pharmaceutical care basics, and pharmacy management. Students learn to use pharmacy management systems, understand "
            "Standard Operating Procedures (SOPs), maintain pharmacy hygiene and safety standards, and provide pharmaceutical services. Final year involves "
            "pharmaceutical research project and comprehensive pharmacy practice. Graduates must register with Pharmacy and Poisons Board as Pharmaceutical "
            "Technologists to practice in Kenya."
        ),
        (
            "Graduates work as pharmaceutical technologists in community pharmacies (retail pharmacies), hospital pharmacies, pharmaceutical manufacturing companies, "
            "pharmaceutical wholesale and distribution companies, drug regulatory authorities (Pharmacy and Poisons Board, National Quality Control Laboratory), "
            "health facilities (government and private), KEMSA, MEDS, NGOs health programs, or establish their own community pharmacies (with proper licensing). "
            "Starting salaries: KSh 25,000-50,000 monthly depending on employer. Pharmaceutical technologists work under supervision of registered pharmacists "
            "performing dispensing duties, drug compounding, inventory management, drug information provision, patient counseling, pharmaceutical care activities, "
            "and pharmacy operations. In many community pharmacies, especially in rural areas, pharmaceutical technologists manage pharmacy operations. Career "
            "progression leads to senior pharmaceutical technologist, pharmacy supervisor (in manufacturing), or pharmacy manager positions. Many establish their "
            "own community pharmacies after gaining experience and meeting licensing requirements, offering good entrepreneurship opportunities. Further education "
            "highly valuable: upgrade to Bachelor of Pharmacy through bridging programs (typically 2-3 years) to become registered pharmacist with expanded scope "
            "of practice and significantly better career prospects; specialized training in pharmaceutical quality assurance, pharmaceutical manufacturing, clinical "
            "pharmacy, or pharmacy management enhances career opportunities. The profession offers stable employment, opportunity to serve communities, and potential "
            "for business ownership."
        ),
        "3 years (6 semesters)",
        "Pharmacy and Poisons Board / KNEC / TVETA"
    ))

    return programs


# ============================================================
# CERTIFICATE PROGRAMS (Minimum: D+ / 4 points)
# ============================================================

def generate_certificate_programs() -> List[Dict]:
    """
    Generate comprehensive Certificate (Craft) programs.
    Minimum requirement: D+ (4 points) in KCSE.
    """
    level = "Certificate"
    programs = []

    # BUSINESS & MANAGEMENT CERTIFICATES
    programs.append(make_program(
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
        (
            "A comprehensive business certificate program designed to equip students with fundamental business management skills including "
            "principles of management, office administration, business communication, basic bookkeeping and accounting, business mathematics, "
            "customer service, marketing basics, entrepreneurship fundamentals, and business ethics. Students learn essential office skills such "
            "as filing systems, record keeping, business correspondence, telephone etiquette, reception management, and office technology including "
            "Microsoft Office Suite (Word, Excel, PowerPoint). The curriculum covers small business management, cash handling, inventory management "
            "basics, sales techniques, and business planning fundamentals. Practical training includes attachments in business offices, retail shops, "
            "or small enterprises where students apply classroom knowledge in real business environments. Students develop professional skills in "
            "communication, teamwork, time management, problem-solving, and customer relations. The program prepares graduates for entry-level "
            "positions in various business sectors or to start and manage their own small businesses. Final assessment includes written examinations "
            "and practical evaluations conducted by Kenya National Examinations Council (KNEC). Upon successful completion, graduates receive a "
            "nationally recognized KNEC Certificate in Business Management, which qualifies them for employment or progression to diploma programs."
        ),
        (
            "Graduates secure employment as office assistants, administrative clerks, receptionists, customer service representatives, sales assistants, "
            "store clerks, cashiers, data entry clerks, records management clerks, front office attendants, business assistants, or small business "
            "operators. Employment opportunities exist in retail shops, supermarkets (Naivas, QuickMart, Carrefour), banks (as service assistants), "
            "hospitals and clinics (administrative support), hotels and restaurants, government offices (clerical positions), schools (administrative "
            "assistants), SACCOs, microfinance institutions, petrol stations, telecommunication shops, courier services, insurance agencies, real estate "
            "offices, and small to medium enterprises across all sectors. Starting salaries range from KSh 15,000-30,000 monthly depending on employer "
            "and location, with urban areas typically offering higher compensation. Many graduates successfully establish their own small businesses such "
            "as retail shops, stationery stores, cybercafés, M-Pesa agencies, mobile money businesses, or general merchandise stores. The certificate "
            "provides foundational business knowledge essential for entrepreneurship. Career progression opportunities include advancing to supervisory "
            "roles (supervisor, team leader) with experience, or pursuing further education through diploma programs in business management, human resource "
            "management, or related fields to enhance career prospects. The broad business foundation allows flexibility to work across various industries "
            "and sectors. Skills acquired are highly transferable and valued in the job market, providing good employment prospects even in challenging "
            "economic conditions. Continuous professional development through short courses and workshops enhances competitiveness and career growth potential."
        ),
        "1 year (2 semesters)",
        "Kenya National Examinations Council (KNEC)"
    ))

    programs.append(make_program(
        "Certificate in Human Resource Management",
        level,
        "Business & Management > Human Resource",
        "D+",
        16,
        [
            "English or Kiswahili (Minimum D+ / 4 points)",
            "Mathematics (Minimum D plain / 3 points)",
            "Any other subject"
        ],
        (
            "A specialized certificate program providing foundational knowledge and practical skills in human resource management including recruitment "
            "and selection processes, employee induction and orientation, training and development basics, personnel record management, payroll "
            "administration fundamentals, employment law and labor relations in Kenya (Employment Act, Labour Relations Act), employee welfare and "
            "benefits administration, performance management basics, workplace safety and health, office administration, business communication, and "
            "professional ethics. Students learn HR documentation procedures including preparing employment contracts, maintaining personnel files, "
            "processing leave applications, handling grievances, and preparing HR reports. The curriculum covers organizational behavior basics, "
            "interpersonal relations, conflict resolution, time and attendance management, and introduction to computerized HR systems. Practical "
            "components include role-plays, case studies, group discussions, and industrial attachment in HR departments or administrative offices. "
            "Students develop essential soft skills including communication, interpersonal relations, confidentiality, attention to detail, and customer "
            "service orientation. Computer applications relevant to HR including Microsoft Excel for payroll calculations, Word for correspondence, and "
            "basic database management are covered. The program prepares graduates for entry-level HR support roles in organizations across sectors. "
            "Assessment through KNEC examinations (theory and practical) ensures competency in HR fundamentals. Graduates receive nationally recognized "
            "KNEC Certificate enabling employment or further studies in human resource management."
        ),
        (
            "Graduates work as HR assistants, recruitment assistants, personnel clerks, payroll clerks, training assistants, administrative officers, "
            "records officers, office administrators, or support staff in HR departments. Employment opportunities in private companies (manufacturing, "
            "retail, hospitality, security firms), government ministries and departments (as administrative staff), parastatals, county governments, "
            "NGOs and international organizations, educational institutions (schools, colleges), hospitals and healthcare facilities, banks and financial "
            "institutions, telecommunications companies, security companies (G4S, KK Security), cleaning companies, recruitment agencies, hotels and "
            "restaurants, transport companies, and SMEs. Starting salaries range from KSh 18,000-35,000 monthly depending on organization size, sector, "
            "and location. Urban areas and larger organizations typically offer better compensation. The HR field provides stable employment as every "
            "organization requires HR support functions. With experience (2-3 years), graduates can progress to senior HR assistant or HR officer roles. "
            "Many pursue further education through Diploma in HRM or degree programs to advance to HR manager positions. Some specialize in specific HR "
            "areas such as recruitment, training, or payroll administration. Professional certification through Institute of Human Resource Management "
            "(IHRM) enhances career prospects significantly. The certificate provides good foundation for entrepreneurship in HR consultancy, recruitment "
            "services, or training services after gaining sufficient experience. Continuous skill development in labor laws, HR software, and best practices "
            "improves competitiveness and career growth. The profession offers respect, job security, and opportunities to impact organizational culture "
            "and employee welfare positively."
        ),
        "1 year (2 semesters)",
        "Kenya National Examinations Council (KNEC)"
    ))

    programs.append(make_program(
        "Certificate in Sales and Marketing",
        level,
        "Business & Management > Sales & Marketing",
        "D+",
        16,
        [
            "English or Kiswahili (Minimum D+ / 4 points)",
            "Mathematics (Minimum D plain / 3 points)",
            "Any other subject"
        ],
        (
            "A practical certificate program designed to develop competent sales and marketing professionals with skills in principles of marketing, "
            "sales techniques and strategies, customer relationship management, marketing communications, advertising basics, digital marketing "
            "fundamentals, market research basics, consumer behavior, product knowledge and presentation, retail management, merchandising and display, "
            "business communication, and professional selling ethics. Students learn the complete sales process including prospecting for customers, "
            "approaching potential clients, making effective presentations, handling objections, closing sales, and after-sales service. The curriculum "
            "covers essential marketing concepts including market segmentation, targeting and positioning, marketing mix (4Ps), branding basics, pricing "
            "strategies, distribution channels, and promotional strategies. Practical training includes sales demonstrations, customer service simulations, "
            "merchandising exercises, and field attachments in retail stores, supermarkets, banks, insurance companies, or sales departments where students "
            "gain hands-on experience. Students develop crucial soft skills including communication, persuasion, negotiation, interpersonal relations, "
            "confidence, resilience, and customer service orientation. Introduction to digital marketing covers social media marketing basics, online "
            "advertising, email marketing, and e-commerce fundamentals. Computer applications for marketing including Microsoft Office, basic graphic "
            "design tools, and point-of-sale systems are covered. The program emphasizes professional ethics, honesty in sales, customer satisfaction, "
            "and building long-term customer relationships. Assessment through KNEC examinations ensures competency in sales and marketing fundamentals. "
            "Graduates receive nationally recognized KNEC Certificate qualifying them for employment in sales and marketing roles across industries."
        ),
        (
            "Graduates secure positions as sales representatives, marketing assistants, sales agents, retail sales assistants, customer service "
            "representatives, merchandisers, sales promoters, brand ambassadors, telesales agents, field sales agents, insurance agents, direct sales "
            "agents, or business development assistants. Employment opportunities exist in retail chains (Naivas, Carrefour, QuickMart, Tuskys), "
            "supermarkets, pharmaceutical companies (as medical representatives), FMCG companies (Unilever, Procter & Gamble), telecommunications "
            "companies (Safaricom, Airtel - retail shops), banks and financial institutions, insurance companies (Britam, CIC, Jubilee as sales agents), "
            "real estate agencies, hotels and hospitality industry, travel agencies, motor vehicle dealerships, electronics and appliance stores, "
            "bookshops and stationery suppliers, agricultural input companies, and virtually every business that requires sales personnel. Starting "
            "salaries range from KSh 20,000-45,000 monthly, often with attractive commission structures that can significantly increase earnings based "
            "on performance. Top sales performers can earn KSh 60,000-100,000+ monthly through commissions. Sales and marketing offers excellent income "
            "potential for motivated individuals. Many graduates become successful entrepreneurs, starting businesses in retail, distribution, agency "
            "services, or independent sales representation. Some specialize in specific industries becoming experts in insurance sales, pharmaceutical "
            "sales, real estate sales, or B2B sales. Career progression leads to senior sales representative, sales supervisor, area sales manager, or "
            "marketing manager positions with experience and proven results. Professional certifications from Chartered Institute of Marketing (CIM) or "
            "Kenya Institute of Management (KIM) enhance career prospects. Further education through diploma or degree in marketing significantly improves "
            "advancement opportunities. The field offers job flexibility, income growth potential, and diverse industry options, making it attractive for "
            "ambitious and people-oriented individuals."
        ),
        "1 year (2 semesters)",
        "Kenya National Examinations Council (KNEC)"
    ))

    programs.append(make_program(
        "Certificate in Supply Chain Management",
        level,
        "Business & Management > Supply Chain & Logistics",
        "D+",
        16,
        [
            "English or Kiswahili (Minimum D+ / 4 points)",
            "Mathematics (Minimum D plain / 3 points)",
            "Any other subject"
        ],
        (
            "A comprehensive certificate program providing essential knowledge and skills in supply chain management including procurement fundamentals, "
            "stores management and warehousing, inventory control and management, logistics and transportation, supplier relationship management, purchase "
            "requisitioning and ordering, goods receiving and inspection, stock recording and documentation, distribution management, basics of the Public "
            "Procurement and Asset Disposal Act (PPADA) in Kenya, business communication, computer applications for supply chain, and professional ethics "
            "in procurement. Students learn the complete procurement cycle from identifying needs, requisitioning, supplier selection, ordering, receiving, "
            "inspection, storage, issuing, to disposal of obsolete stock. The curriculum covers practical warehouse operations including stock arrangement, "
            "FIFO/LIFO methods, bin cards, stock cards, goods received notes (GRN), goods issued notes (GIN), and conducting physical stock takes. "
            "Introduction to procurement laws and regulations governing public procurement in Kenya ensures compliance understanding. Students develop skills "
            "in vendor evaluation, negotiation basics, contract management fundamentals, and purchase documentation. Practical training includes store "
            "operations, use of store management software, handling of inventory management systems, and industrial attachment in procurement departments, "
            "warehouses, or stores where students apply theoretical knowledge. Computer skills relevant to supply chain including Microsoft Excel for "
            "inventory tracking, Word for correspondence, and introduction to ERP systems are covered. The program emphasizes accuracy, attention to detail, "
            "organization, record keeping, security of stock, and ethical conduct in procurement. Assessment through KNEC examinations (theory and practical) "
            "ensures competency. Graduates receive nationally recognized KNEC Certificate enabling employment in procurement and supply chain roles or "
            "progression to diploma level studies."
        ),
        (
            "Graduates work as procurement assistants, store clerks, warehouse assistants, inventory clerks, supply chain assistants, logistics assistants, "
            "purchasing clerks, stock controllers, goods receiving clerks, dispatch clerks, or supply officers. Employment opportunities exist in "
            "manufacturing companies, hospitals and healthcare facilities (medical stores), hotels and restaurants (stores departments), schools and "
            "educational institutions, government ministries and departments, county governments (procurement offices), parastatals, NGOs and international "
            "organizations, retail chains, supermarkets, wholesale distributors, logistics and courier companies (DHL, G4S Courier), transport companies, "
            "construction firms, telecommunications companies, banks, and virtually all organizations that maintain inventory and conduct procurement "
            "activities. Starting salaries range from KSh 18,000-35,000 monthly depending on organization type, size, and location. Government and parastatal "
            "positions often offer better job security and benefits. With experience (2-3 years), graduates advance to senior store keeper, procurement "
            "officer, or warehouse supervisor positions. Many pursue further education through Diploma in Procurement and Supply Chain Management or degree "
            "programs to qualify for higher positions like procurement manager or supply chain manager. Professional certification from Chartered Institute "
            "of Purchasing and Supply (CIPS) or Kenya Institute of Supplies Management (KISM) significantly enhances career advancement and earning potential. "
            "Some graduates establish businesses in logistics, warehousing services, distribution, or become procurement consultants after gaining sufficient "
            "experience. The field offers stable employment as every organization requires supply chain management. Growing e-commerce sector creates new "
            "opportunities in logistics and distribution. Continuous skill development in inventory management software, procurement laws, and supply chain "
            "best practices ensures career growth and competitiveness in the evolving job market."
        ),
        "1 year (2 semesters)",
        "Kenya National Examinations Council (KNEC)"
    ))

    # ICT & COMPUTING CERTIFICATES
    programs.append(make_program(
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
        (
            "A foundational ICT certificate program providing essential computer skills and knowledge including computer fundamentals and hardware basics, "
            "operating systems (Windows, Linux basics), word processing (Microsoft Word), spreadsheets (Microsoft Excel), presentations (PowerPoint), "
            "database basics (Access), internet and email usage, web browsing and online safety, computer networks fundamentals, basic computer maintenance "
            "and troubleshooting, introduction to programming concepts, website design basics (HTML, CSS), graphic design fundamentals, digital literacy, "
            "cyber security awareness, and ICT professional ethics. Students gain hands-on practical experience through extensive computer lab sessions "
            "covering typing skills, document formatting, data entry, spreadsheet formulas and functions, creating presentations, internet research, email "
            "communication, and basic troubleshooting procedures. The curriculum includes PC assembly and disassembly basics, peripheral devices installation, "
            "software installation, virus protection, data backup procedures, and basic networking setup. Introduction to emerging technologies such as cloud "
            "computing, mobile applications, social media for business, and e-commerce basics prepares students for the digital economy. Students develop "
            "problem-solving skills, logical thinking, attention to detail, and adaptability to new technologies. Practical industrial attachment in offices, "
            "cyber cafés, computer shops, or IT departments provides real-world exposure. The program prepares graduates for various ICT support roles or "
            "progression to advanced ICT studies. Assessment through KNEC examinations includes both theory and extensive practical tests to ensure competency. "
            "Graduates receive nationally recognized KNEC Certificate in ICT, which is widely accepted by employers and qualifies holders for entry-level IT "
            "positions or further studies in diploma programs."
        ),
        (
            "Graduates secure employment as computer operators, data entry clerks, office assistants (with ICT skills), cyber café attendants, IT support "
            "assistants, help desk support staff, computer lab assistants, records management clerks, administrative assistants (ICT), receptionist-typists, "
            "ICT trainers (basic level), or computer technicians (basic repairs). Employment opportunities exist in government offices (data entry, records "
            "management), county governments, schools and colleges (computer lab assistants), hospitals and health facilities (records departments), banks "
            "and SACCOs (data entry, customer service), insurance companies, NGOs, private companies across all sectors, cyber cafés and computer bureaus, "
            "computer hardware and software shops, printing and photocopying shops, bookshops with computer sections, telecommunication shops, and business "
            "process outsourcing (BPO) centers. Starting salaries range from KSh 15,000-28,000 monthly depending on employer, location, and specific role. "
            "Many graduates establish their own businesses such as cyber cafés, typing and printing bureaus, computer repair shops, or offer freelance typing "
            "and data entry services. The certificate provides essential digital skills increasingly required in all professions and industries. With "
            "experience, graduates advance to senior data entry positions, office administrators, or IT coordinators. Further education through Diploma in "
            "ICT, Information Technology, or Computer Science opens opportunities for better-paying technical roles like systems administrators, web developers, "
            "or network administrators. Additional certifications like CompTIA A+, Microsoft Office Specialist (MOS), or ICDL (International Computer Driving "
            "License) enhance employability and earning potential. The growing digitalization of businesses and government services creates continuous demand "
            "for ICT-skilled personnel. Online freelancing opportunities through platforms like Upwork, Fiverr, or local platforms allow graduates to earn "
            "additional income through data entry, transcription, virtual assistance, or basic web design services. Continuous learning and staying updated "
            "with new technologies and software ensures career relevance and growth in the rapidly evolving ICT field."
        ),
        "1 year (2 semesters)",
        "Kenya National Examinations Council (KNEC)"
    ))

    programs.append(make_program(
        "Certificate in Computer Hardware and Networking",
        level,
        "ICT & Computing > Computer Hardware & Networks",
        "D+",
        16,
        [
            "Mathematics (Minimum D plain / 3 points)",
            "English or Kiswahili (Minimum D+ / 4 points)",
            "Physics (helpful but not mandatory)"
        ],
        (
            "A technical certificate program providing hands-on training in computer hardware maintenance, repair, and networking fundamentals including "
            "computer architecture and organization, identification and functions of computer components (motherboard, CPU, RAM, hard drives, power supply), "
            "PC assembly and disassembly, BIOS configuration, hardware troubleshooting and diagnostics, peripheral devices installation and configuration "
            "(printers, scanners, monitors), operating system installation and configuration (Windows, Linux), device driver installation, software "
            "installation and troubleshooting, basic networking concepts (LAN, WAN, network topologies), network cable preparation and crimping (UTP, fiber "
            "optics), network hardware (routers, switches, hubs), IP addressing and subnetting basics, network setup and configuration, internet connectivity "
            "setup, wireless networks basics (Wi-Fi), network troubleshooting, computer security basics (antivirus, firewalls), data recovery basics, and "
            "customer service in IT support. Students gain extensive practical experience through hands-on workshops involving actual PC assembly, component "
            "replacement, fault diagnosis using testing tools, operating system installations, network cable making and testing, setting up small networks, "
            "and troubleshooting common hardware and network problems. The curriculum covers proper handling of sensitive electronic components, ESD (electrostatic "
            "discharge) precautions, use of computer maintenance tools (multimeters, cable testers, POST cards), and professional service delivery. Introduction "
            "to emerging technologies like cloud computing basics, virtualization concepts, and mobile device basics provides broader perspective. Students "
            "develop problem-solving skills, analytical thinking, attention to detail, patience, and customer service orientation essential for technical "
            "support roles. Industrial attachment in computer repair shops, IT support departments, or networking companies provides real-world troubleshooting "
            "experience. Assessment through KNEC examinations includes comprehensive practical tests demonstrating competency in hardware repair and network "
            "setup. Graduates receive nationally recognized KNEC Certificate enabling employment as computer technicians or progression to advanced networking "
            "studies."
        ),
        (
            "Graduates work as computer technicians, IT support technicians, hardware maintenance technicians, network support assistants, help desk support "
            "staff, field service technicians, computer repair technicians, cyber café technicians, or IT assistants. Employment opportunities exist in "
            "computer hardware and software shops, computer repair centers, IT support companies, telecommunications companies (field support), internet "
            "service providers (ISPs), schools and colleges (ICT departments), hospitals and clinics (technical support), banks and financial institutions "
            "(branch support), government offices (ICT support), private companies (IT departments), hotels and hospitality industry (technical support), "
            "and security companies (installing surveillance systems). Starting salaries range from KSh 18,000-35,000 monthly depending on employer and "
            "location. Many graduates successfully establish their own businesses including computer repair shops, computer sales and service centers, network "
            "installation services, or become freelance IT technicians serving homes, offices, and cyber cafés. The entrepreneurial path offers unlimited "
            "income potential based on customer base and service quality. With experience (1-2 years) and additional certifications, technicians advance to "
            "senior technician, IT supervisor, or network administrator positions. Professional certifications significantly enhance career prospects and "
            "earning potential: CompTIA A+ (industry-standard hardware certification), CompTIA Network+, Cisco CCNA (networking), Microsoft certifications, "
            "or Linux+ certification. Further education through Diploma in ICT or IT enables transition to higher technical roles like systems administrators, "
            "network engineers, or IT managers with better compensation (KSh 60,000-120,000+). The growing computerization of businesses, institutions, and "
            "homes creates continuous demand for hardware and networking technicians. Additional skills in CCTV installation, biometric systems, access control "
            "systems, or phone repairs increase marketability and income opportunities. Building strong customer relationships and reputation for quality "
            "service leads to repeat business and referrals, essential for entrepreneurial success. Continuous learning through online resources, YouTube "
            "tutorials, and staying updated with new hardware technologies and networking trends ensures career relevance in the evolving technology landscape."
        ),
        "1 year (2 semesters)",
        "Kenya National Examinations Council (KNEC)"
    ))

    # ENGINEERING & TECHNICAL CERTIFICATES
    programs.append(make_program(
        "Certificate in Electrical and Electronic Engineering",
        level,
        "Engineering & Technology > Electrical & Electronics",
        "D+",
        16,
        [
            "Mathematics (Minimum D plain / 3 points)",
            "Physics or Physical Sciences (Minimum D plain / 3 points)",
            "English or Kiswahili (Minimum D+ / 4 points)"
        ],
        (
            "A technical certificate program providing foundational knowledge and practical skills in electrical and electronic systems including basic "
            "electricity principles (voltage, current, resistance, power), electrical circuits and circuit laws (Ohm's Law, Kirchhoff's Laws), electrical "
            "wiring and installation (domestic, commercial), electrical safety and protection devices, electrical measuring instruments and their use, "
            "basic electronics components (resistors, capacitors, diodes, transistors), electronic circuits basics, power systems fundamentals, electrical "
            "machines basics (motors, transformers), electrical drawings and symbols interpretation, hand tools and power tools usage, soldering and PCB "
            "basics, troubleshooting and fault finding, electrical maintenance basics, and workshop safety practices. Students gain extensive hands-on "
            "experience through practical workshops involving house wiring practice on wiring boards, installation of electrical fittings (sockets, switches, "
            "lights), testing and fault finding in electrical installations, motor connection and testing, transformer testing, circuit board soldering "
            "practice, use of measuring instruments (multimeters, clamp meters, meggers), and electrical drawing practice. The curriculum covers Kenya Power "
            "regulations for domestic electrical installations, electrical safety standards, use of proper wiring materials (cables, conduits, circuit "
            "breakers), earthing and grounding systems, and professional electrical installation practices. Introduction to renewable energy systems (solar "
            "panel basics), energy-saving technologies, and modern electrical appliances prepares students for emerging opportunities. Students develop "
            "practical problem-solving skills, safety consciousness, attention to detail, and professional work ethics essential for electrical technicians. "
            "Industrial attachment in electrical contracting firms, maintenance departments, or electrical workshops provides real-world experience and "
            "exposure to industry practices. Assessment through KNEC examinations includes both theoretical tests and comprehensive practical evaluations "
            "demonstrating competency in electrical work. Graduates receive nationally recognized KNEC Certificate enabling them to work as electrical "
            "technicians under supervision or progress to diploma level for higher qualifications and independent practice."
        ),
        (
            "Graduates secure employment as electrical technicians (under supervision), electrical installation assistants, maintenance technicians (electrical), "
            "electrical wiremen, panel wiring assistants, electrical fault finders, electrical helpers in construction sites, or electrical workshop assistants. "
            "Employment opportunities exist in electrical contracting companies, construction firms (electrical department), manufacturing industries (maintenance "
            "departments), hotels and hospitality industry (maintenance), hospitals and healthcare facilities (technical services), schools and colleges "
            "(maintenance staff), county governments (electrical departments), Kenya Power & Lighting Company (as casuals or contract staff), water and sewerage "
            "companies, shopping malls and commercial buildings (maintenance), security companies (electrical installations), solar panel installation companies, "
            "and electrical equipment suppliers. Starting salaries range from KSh 20,000-35,000 monthly for employed positions. Many graduates work as freelance "
            "electricians or artisans earning daily wages of KSh 1,000-2,500 depending on job type and location, potentially earning KSh 30,000-50,000 monthly "
            "with consistent work. Some establish small electrical contracting businesses offering house wiring, electrical repairs, appliance repairs, or solar "
            "panel installations, with income depending on customer base and business management. The demand for electricians remains strong due to construction "
            "activities, building maintenance needs, and electrical repairs. With experience (2-3 years) and additional training, technicians can specialize in "
            "industrial electrical work, motor rewinding, transformer maintenance, or solar energy systems, commanding higher rates (KSh 40,000-70,000 monthly). "
            "Further education through Diploma in Electrical and Electronic Engineering opens opportunities for better positions as electrical supervisors, "
            "electrical engineers (under ERB supervision), or maintenance managers with significantly better compensation (KSh 50,000-100,000+). Professional "
            "certification as an Electrical Wireman through ERB (after 3 years experience and passing exams) allows independent practice and contracting work. "
            "Growing solar energy sector creates opportunities for technicians skilled in solar panel installation, battery systems, and solar water heaters. "
            "Developing expertise in emerging areas like electric vehicle charging stations, home automation, or energy-efficient systems enhances marketability. "
            "Building a good reputation for quality work, reliability, and fair pricing leads to repeat customers and referrals, essential for successful "
            "independent electrical practice. Safety consciousness and adherence to electrical codes ensures both personal safety and client satisfaction, "
            "critical for long-term career success in the electrical field."
        ),
        "1 year (2 semesters)",
        "Kenya National Examinations Council (KNEC)"
    ))

  # CONTINUING ENGINEERING & TECHNICAL CERTIFICATES
    programs.append(make_program(
        "Certificate in Mechanical Engineering",
        level,
        "Engineering & Technology > Mechanical Engineering",
        "D+",
        16,
        [
            "Mathematics (Minimum D plain / 3 points)",
            "Physics or Physical Sciences (Minimum D plain / 3 points)",
            "English or Kiswahili (Minimum D+ / 4 points)"
        ],
        (
            "A comprehensive technical certificate providing foundational knowledge in mechanical engineering principles including engineering "
            "drawing and technical sketching, workshop technology and practices, basic engineering mathematics, mechanics and strength of materials, "
            "machine tools and machining operations, welding and fabrication basics, fitting and assembly work, measurement and metrology, metal "
            "cutting and joining processes, hand tools and power tools operation, engineering materials and their properties, basic thermodynamics, "
            "hydraulics and pneumatics fundamentals, machine maintenance basics, and workshop safety. Students gain extensive hands-on experience "
            "through practical workshops involving lathe machine operations (turning, facing, drilling), milling operations, welding practice (arc "
            "welding, gas welding basics), sheet metal work, fitting exercises, use of measuring instruments (vernier calipers, micrometers), "
            "engineering drawing practice, and machine assembly and disassembly. The curriculum emphasizes proper tool handling, safety procedures, "
            "accurate measurements, quality workmanship, and professional work ethics. Students learn to read and interpret engineering drawings, "
            "prepare working drawings, understand tolerances and fits, and follow standard workshop practices. Introduction to CNC basics, modern "
            "manufacturing processes, and quality control prepares students for contemporary industrial environments. Practical training includes "
            "project work where students design and fabricate simple mechanical components or assemblies. Industrial attachment in manufacturing "
            "companies, engineering workshops, or maintenance departments provides exposure to real industrial operations and professional standards. "
            "Assessment through KNEC examinations includes theoretical tests and extensive practical evaluations demonstrating competency in mechanical "
            "workshop operations and engineering fundamentals. Graduates receive nationally recognized KNEC Certificate qualifying them for entry-level "
            "mechanical technician positions or progression to diploma programs for advanced training."
        ),
        (
            "Graduates work as mechanical technicians, workshop assistants, machine operators, fitters and turners, welders and fabricators, maintenance "
            "assistants, production technicians, quality control assistants, or artisan helpers in engineering workshops. Employment opportunities exist "
            "in manufacturing industries (food processing, textile, plastics, metal fabrication), motor vehicle garages and service centers, construction "
            "companies (plant maintenance), agricultural machinery dealers, hotels and hospitality (maintenance departments), hospitals (engineering services), "
            "water companies (pump maintenance), sugar factories, cement factories, tea and coffee factories, breweries, bottling plants, steel fabrication "
            "workshops, welding and fabrication shops, machinery suppliers, and government technical departments. Starting salaries range from KSh 18,000-35,000 "
            "monthly for formal employment. Many work as artisans earning daily wages of KSh 1,000-3,000 depending on skill level and job complexity, with "
            "skilled welders and fabricators potentially earning KSh 40,000-60,000 monthly. Some establish small businesses in welding and fabrication, metal "
            "works, machinery repair, or general mechanical services with income depending on customer base and specialization. The mechanical engineering field "
            "offers diverse opportunities across multiple industries. With experience (2-3 years) and specialization, technicians can focus on welding (coded "
            "welders earn premium rates), CNC machining, hydraulics, or plant maintenance, commanding higher wages. Further education through Diploma in "
            "Mechanical Engineering opens opportunities for supervisory roles, mechanical engineers (under ERB), maintenance engineers, or production managers "
            "earning KSh 50,000-120,000+. Professional certification through welding certifications (coded welder certificates), ERB registration, or specialized "
            "training enhances employability and earning potential. Skills in specialized areas like industrial refrigeration, HVAC systems, heavy machinery "
            "maintenance, or automotive technology increase marketability. Building expertise in emerging technologies like robotics, automation, or 3D printing "
            "provides competitive advantages. Establishing reputation for quality work, precision, and reliability leads to steady employment or successful "
            "self-employment in the mechanical engineering field."
        ),
        "1 year (2 semesters)",
        "Kenya National Examinations Council (KNEC)"
    ))

    programs.append(make_program(
        "Certificate in Building and Civil Engineering",
        level,
        "Engineering & Technology > Civil & Construction",
        "D+",
        16,
        [
            "Mathematics (Minimum D plain / 3 points)",
            "Physics or Physical Sciences (Minimum D plain / 3 points)",
            "English or Kiswahili (Minimum D+ / 4 points)"
        ],
        (
            "A practical certificate program providing essential knowledge and skills in building construction and civil engineering including building "
            "construction technology, construction materials and their properties, building drawing and plan reading, site preparation and setting out, "
            "foundation construction, masonry and brickwork, carpentry and joinery basics, concrete technology and practice, reinforcement work basics, "
            "plastering and rendering, roofing systems, plumbing basics, building measurements and quantities, construction site management basics, building "
            "safety and health, quality control in construction, and construction tools and equipment. Students gain hands-on experience through practical "
            "workshops involving mixing concrete and mortars, laying bricks and blocks, setting out buildings using surveying instruments, reading and "
            "interpreting building plans, reinforcement bar cutting and bending, formwork construction, plastering practice, and basic carpentry work. The "
            "curriculum covers Kenya building codes and standards, construction permits and approvals, sustainable building practices, and professional "
            "construction ethics. Students learn to use construction tools (spirit levels, plumb bobs, tape measures, mason tools), basic surveying equipment "
            "(theodolite, leveling instruments), and understand construction drawings including architectural, structural, and services drawings. Introduction "
            "to modern construction methods, building information modeling (BIM) basics, and green building concepts prepares students for contemporary "
            "construction industry. Practical training includes site visits to active construction projects, observing various construction activities, and "
            "industrial attachment in construction companies or consultancy firms where students participate in actual construction work. Students develop "
            "problem-solving skills, teamwork, attention to detail, safety consciousness, and understanding of construction quality standards. Assessment "
            "through KNEC examinations includes theory tests and practical evaluations demonstrating competency in construction skills and knowledge. Graduates "
            "receive nationally recognized KNEC Certificate enabling employment in construction sector or progression to diploma level for advanced training "
            "and professional registration."
        ),
        (
            "Graduates secure employment as construction technicians, site supervisors (junior), building inspectors (assistant), quantity surveying assistants, "
            "clerk of works assistants, masonry foremen, site clerks, construction material testers, draughtsmen assistants, or construction site assistants. "
            "Employment opportunities exist in construction companies (building contractors), civil engineering firms, real estate development companies, county "
            "governments (building inspection, public works departments), National Construction Authority (NCA), Kenya Urban Roads Authority (KURA), Kenya "
            "National Highways Authority (KeNHA), Kenya Rural Roads Authority (KeRRA), architectural firms, quantity surveying firms, project management "
            "companies, building material suppliers, and property development firms. Starting salaries range from KSh 20,000-40,000 monthly depending on "
            "employer and location. Many work as independent contractors or artisans (fundis) in masonry, concrete work, or general construction earning "
            "daily wages of KSh 800-2,000 or project-based payments potentially totaling KSh 35,000-70,000 monthly with consistent work. Some establish "
            "small construction businesses offering building services, renovation work, or specialize in masonry, concrete works, or building repairs with "
            "income depending on contracts secured. Kenya's growing construction industry driven by infrastructure development, real estate expansion, and "
            "urbanization creates strong demand for construction workers. With experience (3-5 years) and additional training, technicians advance to site "
            "supervisors, foremen, or site managers earning KSh 50,000-90,000 monthly. Further education through Diploma in Building and Civil Engineering "
            "enables registration with Engineers Board of Kenya (EBK) and progression to positions like construction manager, civil engineer, or building "
            "surveyor earning KSh 70,000-150,000+. Professional registration with NCA as a contractor opens opportunities for tendering government and private "
            "construction projects. Specializing in areas like structural works, road construction, water and sewerage, or building finishing trades enhances "
            "marketability and income potential. Developing expertise in modern construction technologies, project management software, or green building "
            "practices provides competitive advantages. Building strong reputation for quality work, meeting deadlines, and maintaining safety standards leads "
            "to repeat contracts and business growth in the construction industry."
        ),
        "1 year (2 semesters)",
        "Kenya National Examinations Council (KNEC)"
    ))

    programs.append(make_program(
        "Certificate in Plumbing",
        level,
        "Engineering & Technology > Plumbing",
        "D+",
        16,
        [
            "Mathematics (Minimum D plain / 3 points)",
            "Physics or Physical Sciences (Minimum D plain / 3 points)",
            "English or Kiswahili (Minimum D+ / 4 points)"
        ],
        (
            "A specialized technical certificate providing comprehensive training in plumbing systems and practices including plumbing principles and theory, "
            "water supply systems design and installation, drainage systems and sanitary plumbing, pipe materials and their applications (GI pipes, PVC, PPR, "
            "copper), pipe joining techniques (threading, welding, solvent cementing), plumbing tools and equipment usage, sanitary fixtures installation "
            "(sinks, toilets, showers, bathtubs), water storage systems (tanks, cisterns), hot water systems (geysers, solar water heaters), sewerage systems, "
            "rainwater harvesting systems, plumbing drawings reading and interpretation, plumbing measurements and estimation, leak detection and repair, "
            "preventive maintenance, and plumbing safety practices. Students gain extensive hands-on experience through practical workshops involving pipe "
            "cutting and joining, thread cutting practice, pipe bending, installation of water supply systems, drainage system installation, sanitary fixtures "
            "mounting, water pump installation and testing, solar water heater installation basics, and fault finding in plumbing systems. The curriculum "
            "covers Kenya plumbing codes and standards, water conservation practices, proper sanitation standards, and professional plumbing ethics. Students "
            "learn to use plumbing tools (pipe wrenches, cutters, threading machines, bending springs, plungers), testing equipment (pressure gauges), and "
            "understand hydraulic principles affecting plumbing systems. Introduction to modern plumbing technologies including sensor taps, water treatment "
            "systems, greywater recycling, and smart plumbing systems prepares students for contemporary plumbing requirements. Practical training includes "
            "project work designing and installing complete bathroom or kitchen plumbing systems. Industrial attachment in plumbing companies, construction "
            "sites, or maintenance departments provides real-world experience in residential, commercial, and industrial plumbing installations. Students "
            "develop problem-solving skills, customer service orientation, attention to detail, cleanliness, and professional work habits essential for "
            "successful plumbers. Assessment through KNEC examinations includes theory tests and comprehensive practical evaluations demonstrating competency "
            "in plumbing installations, repairs, and maintenance. Graduates receive nationally recognized KNEC Certificate enabling them to work as plumbers "
            "or progress to diploma level for advanced specialization."
        ),
        (
            "Graduates work as plumbers, plumbing technicians, maintenance plumbers, drainage specialists, water supply technicians, sanitary installation "
            "technicians, or plumbing assistants in various settings. Employment opportunities exist in plumbing companies and contractors, construction "
            "firms (plumbing department), building maintenance companies, hotels and hospitality industry (maintenance), hospitals and healthcare facilities "
            "(technical services), schools and educational institutions, shopping malls and commercial buildings, manufacturing industries, county governments "
            "(water and sanitation departments), water and sewerage companies, real estate management companies, and property maintenance firms. Starting "
            "salaries range from KSh 18,000-35,000 monthly for employed positions. Many plumbers work independently as artisans earning daily rates of "
            "KSh 1,500-3,500 depending on job type and location, potentially earning KSh 40,000-80,000 monthly with steady clientele. Plumbing offers excellent "
            "opportunities for self-employment with many establishing plumbing services businesses offering installation, repair, and maintenance services with "
            "income depending on customer base and service quality. Plumbing is an essential trade with consistent demand due to ongoing construction, building "
            "maintenance needs, and regular repairs required in homes and commercial properties. Emergency plumbing services (burst pipes, blockages) command "
            "premium rates especially during nights and weekends. With experience (2-3 years) and building clientele, skilled plumbers can earn KSh 60,000-120,000+ "
            "monthly through combination of contracts and call-out services. Specializing in areas like industrial plumbing, solar water heater installation, "
            "water treatment systems, or luxury bathroom installations increases earning potential. Further education through Diploma in Plumbing or related "
            "certifications enhances professional credentials and opens opportunities for larger contracts. Professional registration and obtaining business "
            "licenses enables tendering for institutional and government plumbing contracts. Developing expertise in modern plumbing technologies including "
            "water-saving fixtures, smart plumbing systems, or rainwater harvesting provides competitive advantages. Building strong reputation for quality "
            "work, reliability, fair pricing, and cleanliness leads to referrals and repeat customers essential for successful plumbing business. Offering "
            "comprehensive services including design, installation, maintenance, and emergency services creates multiple revenue streams. Continuous learning "
            "about new plumbing materials, techniques, and technologies ensures career relevance and competitiveness in the evolving plumbing industry."
        ),
        "1 year (2 semesters)",
        "Kenya National Examinations Council (KNEC)"
    ))

    # HOSPITALITY & TOURISM CERTIFICATES
    programs.append(make_program(
        "Certificate in Food and Beverage Sales and Service",
        level,
        "Hospitality & Tourism > Food & Beverage",
        "D+",
        16,
        [
            "English or Kiswahili (Minimum D+ / 4 points)",
            "Mathematics (Minimum D plain / 3 points)",
            "Any other subject"
        ],
        (
            "A practical certificate program designed to produce competent food and beverage service professionals with skills in restaurant service operations, "
            "table setting and laying, food and beverage service methods (silver service, family service, buffet service), menu knowledge and merchandising, "
            "beverage service including alcoholic and non-alcoholic beverages, cocktail preparation basics, customer service excellence, point of sale systems, "
            "cash handling and billing, food safety and hygiene (HACCP basics), restaurant equipment and tools, dining room management, banqueting and catering "
            "basics, room service operations, professional grooming and etiquette, and hospitality communication. Students gain hands-on experience through "
            "practical training in simulated restaurant environments and real hospitality establishments learning proper table service techniques, carrying "
            "trays and plates, napkin folding, cutlery arrangement, taking orders, serving food and beverages, clearing tables, handling customer complaints, "
            "and maintaining dining areas. The curriculum covers various types of food service establishments (hotels, restaurants, cafes, fast food), different "
            "service styles, table etiquette, wine service basics, and bar operations fundamentals. Students learn to operate point-of-sale systems, prepare "
            "simple beverages (coffee, tea, juices), understand menu planning basics, and maintain hygiene standards in food service. Introduction to different "
            "cuisines, food presentation basics, and modern hospitality trends prepares students for diverse work environments. Practical industrial attachment "
            "in hotels, restaurants, clubs, or catering companies provides real-world experience in busy food service operations, customer interaction, teamwork, "
            "and professional service delivery. Students develop essential soft skills including communication, interpersonal relations, patience, attention to "
            "detail, multitasking ability, stress management, and maintaining professional demeanor under pressure. Assessment through KNEC examinations includes "
            "both theory and extensive practical tests demonstrating competency in food and beverage service operations. Graduates receive nationally recognized "
            "KNEC Certificate qualifying them for employment in the vibrant hospitality industry or progression to diploma programs for career advancement."
        ),
        (
            "Graduates secure employment as waiters/waitresses, food and beverage servers, restaurant attendants, room service attendants, banqueting servers, "
            "bar attendants, coffee shop attendants, buffet attendants, fast food service crew, or catering assistants. Employment opportunities exist in hotels "
            "(Sarova, Hilton, Radisson, Intercontinental, local hotels), restaurants and fine dining establishments, resorts and lodges, coffee shops and cafes "
            "(Java House, Artcaffe, Dormans), fast food chains (KFC, Subway, Pizza Inn), clubs and entertainment venues, cruise ships and airlines (with further "
            "training), conference centers, corporate cafeterias, hospitals and healthcare institutions (dietary departments), schools and universities (catering "
            "departments), and catering companies serving events and functions. Starting salaries range from KSh 15,000-30,000 monthly depending on establishment "
            "type and location, with tips significantly supplementing income in busy restaurants and high-end establishments - experienced servers in upscale "
            "venues can earn KSh 40,000-60,000+ monthly including tips. Tourism and hospitality industry in Kenya provides numerous opportunities especially in "
            "Nairobi, Mombasa, and tourist destinations. Many graduates work in international hotel chains gaining valuable experience and exposure to global "
            "hospitality standards. With experience (2-3 years), servers advance to senior waiter/waitress, head waiter, restaurant supervisor, or shift leader "
            "positions earning KSh 35,000-55,000 monthly. Further education through Diploma in Food and Beverage Management or Hotel Management opens pathways "
            "to restaurant manager, food and beverage manager, or banqueting manager positions earning KSh 60,000-150,000+ depending on establishment. Some "
            "graduates establish their own food service businesses including restaurants, cafes, catering services, or mobile food services with income depending "
            "on business success and management skills. International opportunities exist in hospitality industries across Middle East, cruise lines, and other "
            "countries seeking trained hospitality professionals. Professional certifications like HABC (Highfield Awarding Body for Compliance) in Food Safety "
            "or customer service certifications enhance employability. Specializing in fine dining service, sommelier training (wine service), barista skills, "
            "or event catering increases marketability and earning potential. Multilingual skills (especially French, German, Chinese) significantly enhance "
            "career prospects in international hotels and tourist establishments. Building excellent customer service reputation, maintaining professional "
            "appearance, and developing strong interpersonal skills leads to career advancement and better opportunities in the competitive but rewarding "
            "hospitality industry."
        ),
        "1 year (2 semesters)",
        "Kenya National Examinations Council (KNEC)"
    ))

    programs.append(make_program(
        "Certificate in Food and Beverage Production",
        level,
        "Hospitality & Tourism > Culinary Arts",
        "D+",
        16,
        [
            "English or Kiswahili (Minimum D+ / 4 points)",
            "Mathematics (Minimum D plain / 3 points)",
            "Any other subject"
        ],
        (
            "A hands-on certificate program training competent cooks and food production staff with skills in food preparation techniques, basic cooking methods "
            "(boiling, frying, baking, roasting, grilling, steaming), knife skills and cutting techniques, kitchen equipment operation and maintenance, recipe "
            "following and adaptation, food costing and portion control, menu planning basics, food safety and hygiene standards, HACCP principles, kitchen "
            "organization and workflow, stock management, vegetable and fruit preparation, meat, poultry and fish preparation, soup and sauce preparation, "
            "breakfast cookery, lunch and dinner preparation, pastry and baking basics, food presentation and garnishing, and kitchen safety practices. Students "
            "gain extensive practical experience through hands-on training in well-equipped kitchens preparing various dishes including Kenyan cuisine, "
            "continental dishes, Asian basics, and international recipes. The curriculum covers proper use of kitchen tools and equipment (knives, ovens, "
            "fryers, grills, food processors), understanding cooking times and temperatures, flavor combinations, seasoning, and quality control in food "
            "production. Students learn to prepare different categories of foods: appetizers, soups, main courses (meat, chicken, fish dishes), vegetables, "
            "starches, desserts, and baked goods. Training includes quantity cooking for institutions, special dietary requirements (vegetarian, diabetic), "
            "food allergies awareness, and waste reduction in kitchens. Introduction to modern culinary trends, fusion cuisine basics, and plating techniques "
            "prepares students for contemporary kitchens. Practical industrial attachment in hotel kitchens, restaurant kitchens, institutional catering, or "
            "bakeries provides real-world experience in busy kitchen environments, teamwork, time management under pressure, and professional kitchen operations. "
            "Students develop creativity in food preparation, attention to detail, cleanliness habits, ability to work under pressure, and physical stamina "
            "required in kitchen work. Assessment through KNEC examinations includes theory tests and extensive practical cooking tests demonstrating competency "
            "in food preparation and cooking techniques. Graduates receive nationally recognized KNEC Certificate qualifying them for employment as cooks in "
            "various food service establishments or progression to diploma level for advanced culinary training."
        ),
        (
            "Graduates secure employment as cooks, commis chefs, kitchen assistants, prep cooks, institutional cooks, bakery assistants, pastry assistants, "
            "kitchen stewards, or food production assistants. Employment opportunities exist in hotels and resorts (kitchen departments), restaurants, fast "
            "food outlets, bakeries and pastry shops, catering companies, schools and universities (catering departments), hospitals and healthcare institutions "
            "(dietary kitchens), corporate cafeterias, airline catering companies, cruise ships (with additional training), private clubs, coffee shops, "
            "military and police catering, prisons catering departments, and private households (personal chefs for wealthy families). Starting salaries range "
            "from KSh 18,000-35,000 monthly depending on establishment type, location, and specific role. Hotel and upscale restaurant kitchens typically offer "
            "better compensation. With experience and skill development, cooks can earn KSh 40,000-70,000 monthly in mid-level positions. The food service "
            "industry provides stable employment as eating establishments operate daily requiring kitchen staff. Many graduates start their own food businesses "
            "including small restaurants, food kiosks, catering services, bakeries, food delivery services, or specialize in particular cuisines (nyama choma, "
            "traditional Kenyan foods, fast food) with income depending on location, menu, and business management skills. Street food vending and food stall "
            "operations in markets provide entrepreneurial opportunities requiring lower capital investment. With experience (2-3 years) and proven skills, "
            "cooks advance to chef de partie (station chef), pastry chef, or kitchen supervisor positions. Further education through Diploma in Food and "
            "Beverage Production or Culinary Arts opens pathways to head chef, executive chef, or food production manager positions in hotels and large "
            "establishments earning KSh 60,000-200,000+ depending on establishment size and prestige. Professional chef certifications, specialization in "
            "particular cuisines (French, Italian, Asian), or advanced baking and pastry training significantly enhance career prospects and earning potential. "
            "International opportunities exist for skilled chefs in Middle East hotels, cruise ships, international chains, and other countries. Some graduates "
            "become celebrity chefs, food bloggers, culinary instructors, or food consultants. Developing signature dishes, building culinary reputation, and "
            "continuously learning new techniques and cuisines ensures career growth. Creativity, passion for cooking, maintaining hygiene standards, and "
            "ability to work efficiently under pressure are keys to success in the culinary profession."
        ),
        "1 year (2 semesters)",
        "Kenya National Examinations Council (KNEC)"
    ))

    programs.append(make_program(
        "Certificate in Front Office Operations",
        level,
        "Hospitality & Tourism > Hotel Management",
        "D+",
        16,
        [
            "English (Minimum D+ / 4 points)",
            "Mathematics (Minimum D plain / 3 points)",
            "Any other subject"
        ],
        (
            "A specialized certificate program preparing competent front office staff for hotels and hospitality establishments covering front office operations "
            "and procedures, guest reception and check-in/check-out procedures, reservation systems and booking management, telephone etiquette and handling, "
            "guest services and concierge duties, room assignment and inventory management, cashiering and billing procedures, night audit basics, complaint "
            "handling and problem-solving, property management systems (PMS), communication systems in hotels, guest relations and customer service excellence, "
            "knowledge of hotel departments and their functions, tourism products and local attractions, business communication, professional appearance and "
            "grooming, and hospitality ethics. Students gain practical experience through training in simulated front desk environments and actual hotel "
            "operations learning to use hotel management software, handle reservations, process check-ins and check-outs, manage room keys, prepare bills, "
            "handle cash and card payments, coordinate with housekeeping and other departments, and provide excellent customer service. The curriculum covers "
            "various types of accommodation establishments (hotels, lodges, motels, serviced apartments), room categories, rate structures, occupancy management, "
            "and revenue basics. Students learn proper telephone techniques, email etiquette, handling inquiries, processing special requests, managing "
            "complaints professionally, and maintaining guest history records. Training includes security procedures, emergency protocols, lost and found "
            "procedures, mail and message handling, and coordination of guest services (transport, tours, dining reservations). Introduction to online travel "
            "agencies (OTAs), distribution channels, and digital marketing basics prepares students for modern hospitality operations. Practical industrial "
            "attachment in hotel front offices provides hands-on experience in busy reception environments, handling diverse guests, multitasking, working "
            "shifts (including nights and weekends), and professional guest interaction. Students develop essential skills including excellent communication, "
            "interpersonal relations, patience, problem-solving, attention to detail, multitasking ability, cultural sensitivity, professional demeanor, and "
            "maintaining composure under pressure. Assessment through KNEC examinations includes theory and practical tests demonstrating competency in front "
            "office operations. Graduates receive nationally recognized KNEC Certificate qualifying them for employment in hotel front offices or progression "
            "to diploma programs for career advancement in hotel management."
        ),
        (
            "Graduates secure employment as receptionists, front desk agents, guest service agents, reservation agents, front office assistants, night auditors, "
            "concierge assistants, bell attendants, or guest relations officers. Employment opportunities exist in hotels of all categories (luxury, mid-range, "
            "budget hotels), resorts and lodges, serviced apartments, hostels, guest houses, conference centers, hospitals (reception), corporate offices "
            "(reception), educational institutions (reception), banks (customer service), government offices (front desk), rental car companies, travel agencies, "
            "tour operators, and any organization requiring professional reception services. Starting salaries in hospitality range from KSh 20,000-35,000 monthly "
            "for entry-level positions, with upscale hotels offering better compensation. Urban hotels and international chains typically pay higher salaries and "
            "provide better benefits. The front office is often considered the heart of the hotel, providing stable employment opportunities. With experience "
            "(2-3 years) and demonstrated competency, receptionists advance to senior receptionist, front office supervisor, or shift leader positions earning "
            "KSh 35,000-60,000 monthly. Further education through Diploma in Front Office Management or Hotel Management opens pathways to front office manager, "
            "rooms division manager, or guest services manager positions earning KSh 70,000-150,000+ in hotels. International hotel chains offer opportunities "
            "for career progression within their global networks. Professional certifications in hospitality customer service or specialized training in hotel "
            "management systems enhance career prospects. Skills gained in front office operations are transferable to various customer-facing roles across "
            "industries. Some graduates transition to sales and marketing roles in hotels, event management, or establish their own accommodation businesses "
            "(guest houses, Airbnb management, serviced apartments). Multilingual abilities significantly enhance employability especially in tourist hotels "
            "where international guests are common. Working in front office provides excellent exposure to all hotel operations and networking opportunities "
            "within the hospitality industry. Building reputation for excellent customer service, professionalism, and problem-solving leads to recommendations "
            "and career advancement. The skills in guest relations, conflict resolution, and professional communication are valuable across many industries. "
            "Continuous learning about hospitality trends, technology systems, and customer service innovations ensures career relevance and growth in the "
            "evolving hospitality sector."
        ),
        "1 year (2 semesters)",
        "Kenya National Examinations Council (KNEC)"
    ))

    # AGRICULTURE CERTIFICATES
    programs.append(make_program(
        "Certificate in Agriculture",
        level,
        "Agriculture & Veterinary > Agriculture",
        "D+",
        16,
        [
            "Agriculture, Biology or Biological Sciences (Minimum D plain / 3 points)",
            "English or Kiswahili (Minimum D+ / 4 points)",
            "Mathematics (Minimum D- / 2 points)"
        ],
        (
            "A comprehensive agricultural certificate providing practical knowledge and skills in modern farming practices including crop production (cereals, "
            "legumes, vegetables, fruits), soil science and management, crop protection and pest management, farm machinery and equipment operation, livestock "
            "production (cattle, poultry, goats, sheep), animal husbandry and health basics, farm management and record keeping, agricultural economics basics, "
            "agribusiness fundamentals, irrigation and water management, organic farming practices, post-harvest handling and storage, agricultural extension "
            "principles, and sustainable agriculture. Students gain hands-on experience through practical training in demonstration farms learning land "
            "preparation, planting techniques, crop management practices, harvesting, animal feeding and care, basic veterinary procedures (deworming, "
            "vaccination), milking, egg collection, and general farm operations. The curriculum covers modern farming techniques including greenhouse farming, "
            "drip irrigation, zero-grazing, improved breeds and varieties, fertilizer application, pesticide use and safety, and good agricultural practices "
            "(GAP). Students learn to operate farm equipment (tractors, ploughs, planters, harvesters), maintain tools and machinery, and understand mechanization "
            "benefits. Training includes soil testing basics, composting, farm planning and layout, crop rotation, and integrated pest management. Introduction "
            "to value addition, agricultural marketing, cooperatives, and accessing agricultural credit prepares students for agribusiness. Practical field "
            "attachments in commercial farms, agricultural research stations, or agricultural companies provide exposure to large-scale farming operations, "
            "modern technologies, and professional farm management. Students develop skills in observation, problem-solving, physical work, entrepreneurial "
            "thinking, and understanding agricultural value chains. The program emphasizes climate-smart agriculture, environmental conservation, and sustainable "
            "farming practices relevant to Kenyan agricultural context. Assessment through KNEC examinations includes theory tests and practical evaluations "
            "demonstrating competency in agricultural practices. Graduates receive nationally recognized KNEC Certificate enabling employment in agricultural "
            "sector or establishing own farming enterprises."
        ),
        (
            "Graduates secure employment as agricultural extension officers (assistant level), farm supervisors, farm managers (small to medium farms), crop "
            "production assistants, livestock production assistants, agricultural demonstrators, research assistants in agricultural institutes, quality control "
            "assistants in agricultural companies, agricultural input sales representatives, farm training assistants, or agricultural project assistants. "
            "Employment opportunities exist in county governments (agricultural departments), Ministry of Agriculture, agricultural research institutions (KALRO), "
            "large commercial farms (Kakuzi, Sasini, Del Monte, flower farms), tea and coffee estates, sugar plantations, horticultural export companies, "
            "agricultural input companies (fertilizers, seeds, pesticides), agricultural cooperatives, NGOs implementing agricultural projects, agricultural "
            "training institutions, seed companies, animal feed manufacturers, and agro-processing companies. Starting salaries range from KSh 18,000-35,000 "
            "monthly depending on employer and role. Many graduates successfully establish their own farming enterprises specializing in high-value crops "
            "(vegetables, fruits, herbs), poultry farming (layers for eggs, broilers for meat), dairy farming, goat farming, fish farming, beekeeping, or mixed "
            "farming with income depending on scale, market access, and management. Agriculture offers significant entrepreneurial opportunities "
            "especially for those with access to land or willing to lease land. Urban and peri-urban farming (vegetables, poultry) provides good income with "
            "limited space. Export horticulture (French beans, snow peas, flowers) offers premium prices but requires meeting strict quality standards. Dairy "
            "farming provides regular income through milk sales to cooperatives or processors. Poultry farming (layers producing 280-320 eggs annually) offers "
            "quick returns with proper management. With experience and capital, successful farmers can earn KSh 50,000-200,000+ monthly from well-managed "
            "agricultural enterprises. Further education through Diploma in Agriculture or specialized diplomas (horticulture, animal production) enhances "
            "technical knowledge and qualifies for higher positions like senior agricultural officer, farm manager (large farms), or agribusiness manager earning "
            "KSh 50,000-100,000+. Specializing in high-demand areas like greenhouse farming, organic agriculture, aquaculture, or precision agriculture increases "
            "income potential. Professional certifications in organic farming, good agricultural practices (GlobalGAP), or agricultural extension strengthen "
            "credentials. Kenya's agricultural sector remains critical to the economy, employing majority of rural population and offering diverse opportunities. "
            "Government initiatives supporting agriculture (subsidized inputs, extension services, credit access) create enabling environment. Access to "
            "agricultural loans through banks, SACCOs, or government programs facilitates business establishment. Contract farming with established companies "
            "provides guaranteed markets and technical support. Joining agricultural cooperatives improves market access, input costs, and negotiating power. "
            "Value addition through processing (drying, packaging) increases profits from farm produce. Continuous learning about new varieties, technologies, "
            "and market trends ensures competitiveness and farm profitability."
        ),
        "1 year (2 semesters)",
        "Kenya National Examinations Council (KNEC)"
    ))

    programs.append(make_program(
        "Certificate in Veterinary Laboratory Technology",
        level,
        "Agriculture & Veterinary > Veterinary Science",
        "D+",
        16,
        [
            "Biology or Biological Sciences (Minimum D plain / 3 points)",
            "English or Kiswahili (Minimum D+ / 4 points)",
            "Chemistry or Physical Sciences (Minimum D- / 2 points)"
        ],
        (
            "A specialized certificate providing practical training in veterinary laboratory procedures and animal health diagnostics including veterinary "
            "anatomy and physiology basics, animal diseases and parasitology, veterinary microbiology, clinical pathology, laboratory safety and biosecurity, "
            "specimen collection and handling (blood, urine, feces, tissue samples), microscopy techniques, hematology basics (blood cell counting, smears), "
            "parasitology diagnostics (fecal examination, blood parasites), bacteriology basics (culture, staining), laboratory equipment operation and "
            "maintenance, quality control in veterinary laboratories, laboratory records and documentation, veterinary pharmacology basics, animal nutrition "
            "basics, and professional ethics. Students gain hands-on experience through extensive practical training in veterinary laboratories performing "
            "fecal examinations for parasites (worms, coccidia, protozoa), blood smear preparation and examination, urine analysis, bacterial culture basics, "
            "disease diagnosis support, and proper specimen handling. The curriculum covers common animal diseases in Kenya affecting livestock (cattle, goats, "
            "sheep, poultry, pigs) and companion animals (dogs, cats), their diagnosis, and control. Students learn to use laboratory equipment (microscopes, "
            "centrifuges, autoclaves, incubators), prepare reagents and media, maintain laboratory inventory, and follow standard operating procedures. Training "
            "includes biosafety practices, proper disposal of biological waste, personal protective equipment use, and maintaining sterile conditions. Introduction "
            "to modern diagnostic techniques (ELISA, PCR basics) and laboratory information systems prepares students for contemporary veterinary laboratories. "
            "Practical industrial attachment in veterinary diagnostic laboratories, veterinary clinics, research institutions, or animal health companies provides "
            "real-world laboratory experience and professional exposure. Students develop accuracy, attention to detail, cleanliness, organizational skills, "
            "scientific approach to problem-solving, and understanding of laboratory quality assurance. Assessment through KNEC examinations includes theory and "
            "practical tests demonstrating competency in veterinary laboratory procedures. Graduates receive nationally recognized KNEC Certificate enabling "
            "employment in veterinary diagnostics or progression to diploma programs for advanced training."
        ),
        (
            "Graduates secure employment as veterinary laboratory technicians, animal health assistants, veterinary clinic assistants, laboratory assistants in "
            "veterinary diagnostics, research assistants in animal health institutions, quality control assistants in animal health product companies, or field "
            "veterinary assistants. Employment opportunities exist in government veterinary diagnostic laboratories, county veterinary departments, private "
            "veterinary clinics and hospitals, veterinary diagnostic centers, Kenya Agricultural and Livestock Research Organization (KALRO), International "
            "Livestock Research Institute (ILRI), veterinary pharmaceutical companies, animal feed manufacturers (quality control), large commercial farms "
            "(veterinary departments), dairy farms, poultry farms, pig farms, zoos and wildlife facilities, veterinary product distributors, and NGOs working "
            "in animal health. Starting salaries range from KSh 20,000-35,000 monthly depending on employer type and location. The growing importance of animal "
            "health and food safety creates steady demand for veterinary laboratory technicians. With experience (2-3 years), technicians can advance to senior "
            "laboratory technician or laboratory supervisor positions earning KSh 35,000-60,000 monthly. Further education through Diploma in Veterinary Laboratory "
            "Technology or related programs enhances technical expertise and qualifies for higher positions like laboratory manager or veterinary diagnostician "
            "earning KSh 50,000-90,000+. Some graduates establish mobile veterinary diagnostic services partnering with veterinarians to serve farmers in rural "
            "areas. Specializing in specific areas like poultry diseases, dairy cattle health, or parasitology enhances expertise and marketability. Professional "
            "certifications or additional training in specific diagnostic techniques improves career prospects. The certificate provides foundation for those "
            "interested in animal health but unable to pursue full veterinary medicine degree. Skills in laboratory procedures are transferable to human health "
            "laboratories with additional training. Growing livestock sector in Kenya and emphasis on disease control, food safety, and animal welfare create "
            "opportunities for qualified veterinary laboratory personnel. Supporting farmers through accurate diagnosis helps improve animal productivity and "
            "incomes. Continuous learning about new diseases, diagnostic techniques, and laboratory technologies ensures career relevance in the evolving field "
            "of veterinary diagnostics."
        ),
        "1 year (2 semesters)",
        "Kenya National Examinations Council (KNEC)"
    ))

    # EDUCATION & SOCIAL SERVICES CERTIFICATES
    programs.append(make_program(
        "Certificate in Early Childhood Development and Education (ECDE)",
        level,
        "Education & Social Services > Early Childhood Education",
        "D+",
        16,
        [
            "English or Kiswahili (Minimum D+ / 4 points)",
            "Mathematics (Minimum D- / 2 points)",
            "Any other subject"
        ],
        (
            "A specialized certificate preparing competent early childhood educators to work with children aged 0-6 years covering child growth and development, "
            "early childhood education principles and practices, curriculum development for early learners, teaching methods and strategies for young children, "
            "play-based learning, learning materials development and use, classroom management for young children, assessment and evaluation in ECDE, child health, "
            "nutrition and safety, first aid for children, special needs education basics, parent and community engagement, children's rights and protection, "
            "creative activities (art, music, movement), storytelling and language development, numeracy basics for young children, professional ethics in ECDE, "
            "and child psychology basics. Students gain practical experience through teaching practice in ECDE centers, nursery schools, and daycare facilities "
            "learning to plan and implement age-appropriate activities, manage classroom behavior, create safe and stimulating learning environments, prepare "
            "teaching and learning materials from locally available resources, conduct songs and games, tell stories, facilitate play activities, and interact "
            "positively with young children. The curriculum covers the Competency Based Curriculum (CBC) for ECDE, understanding developmental milestones, "
            "creating inclusive learning environments, and identifying children with special needs for early intervention. Students learn to prepare nutritious "
            "meals and snacks for children, maintain hygiene standards, handle emergencies, administer basic first aid, and ensure child safety in ECDE settings. "
            "Training includes observation and assessment of children's development, record keeping, reporting to parents, organizing parent meetings, and working "
            "with parents as partners in child development. Introduction to modern ECDE approaches (Montessori basics, Reggio Emilia), use of technology in early "
            "learning, and innovative teaching materials prepares graduates for diverse ECDE settings. Students develop patience, creativity, love for children, "
            "communication skills, empathy, cultural sensitivity, and professional responsibility essential for early childhood educators. Assessment through KNEC "
            "examinations includes theory tests and practical teaching demonstrations. Graduates receive nationally recognized KNEC Certificate enabling employment "
            "in ECDE centers or establishing own ECDE facilities."
        ),
        (
            "Graduates secure employment as ECDE teachers in public and private nursery schools, preschool teachers, daycare caregivers, nursery school assistants, "
            "ECDE center managers (small centers), children's home caregivers, or early learning facilitators. Employment opportunities exist in public primary "
            "schools (ECDE classes), private nursery schools and kindergartens, international schools (ECDE sections), children's homes and orphanages, daycare "
            "centers, community ECDE centers, churches and religious organizations (children's programs), NGOs running ECDE programs, county governments (ECDE "
            "officers), private homes (nannies with ECDE training), and corporate daycare facilities. Starting salaries range from KSh 12,000-25,000 monthly in "
            "public ECDE centers and community schools, while private nursery schools offer KSh 18,000-35,000 depending on school category and location. Urban "
            "areas and upscale nursery schools typically offer better compensation. Many graduates successfully establish their own ECDE centers or nursery schools "
            "with proper registration from county governments, with income depending on enrollment numbers, fees charged, and location - successful ECDE centers can "
            "generate KSh 40,000-150,000+ monthly profit depending on scale. The growing recognition of importance of early childhood education creates increasing "
            "demand for qualified ECDE teachers. Government support for ECDE through county governments ensures opportunities in public sector. With experience "
            "(3-5 years), teachers can advance to head teacher positions in ECDE centers or coordinators of ECDE programs earning KSh 30,000-50,000 monthly. Further "
            "education through Diploma in ECDE significantly improves career prospects, qualifications for better positions, and earning potential (KSh 35,000-65,000+). "
            "TSC registration after obtaining diploma enables employment in public primary schools teaching ECDE classes with government benefits and job security. "
            "Some graduates work as private tutors for young children, run home-based daycare, or offer parenting workshops and training. Specialized training in "
            "special needs education, Montessori method, or child counseling enhances marketability. Working as nanny with ECDE qualifications commands premium rates "
            "(KSh 25,000-50,000 monthly) especially with wealthy families or expatriates. International opportunities exist for trained ECDE teachers in other countries. "
            "The profession offers fulfillment from shaping young minds and contributing to child development. Continuous professional development through workshops, "
            "new teaching methods, and CBC implementation ensures effectiveness and career growth. Building reputation for quality ECDE provision, caring for children, "
            "and professional conduct leads to parental trust and successful ECDE career or business."
        ),
        "1 year (2 semesters)",
        "Kenya National Examinations Council (KNEC)"
    ))

    programs.append(make_program(
        "Certificate in Social Work and Community Development",
        level,
        "Education & Social Services > Social Work",
        "D+",
        16,
        [
            "English or Kiswahili (Minimum D+ / 4 points)",
            "Any other two subjects (Minimum D- / 2 points each)"
        ],
        (
            "A comprehensive certificate program preparing community development workers and social service providers with knowledge in community development "
            "principles and practices, social work basics, community needs assessment, participatory development approaches, project planning and management basics, "
            "community mobilization and organization, adult education and training methods, communication for development, behavior change communication, monitoring "
            "and evaluation basics, report writing and documentation, group dynamics and facilitation, conflict resolution, human rights and social justice, gender "
            "and development, children and youth development, vulnerable groups support (elderly, persons with disabilities, orphans), HIV/AIDS awareness and support, "
            "substance abuse awareness, and professional ethics in social work. Students gain practical experience through fieldwork and attachments in communities, "
            "NGOs, or government social programs learning to conduct community meetings, facilitate focus group discussions, organize community activities, implement "
            "development projects, work with diverse community groups, support vulnerable populations, and mobilize communities for self-help initiatives. The "
            "curriculum covers community entry approaches, building trust with communities, understanding community dynamics, working with local leadership structures, "
            "and promoting sustainable community development. Students learn to conduct simple surveys, prepare project proposals, write activity reports, maintain "
            "program records, and use participatory rural appraisal (PRA) tools. Training includes basics of community health promotion, nutrition education, "
            "livelihood support programs, microfinance group formation, and linking communities to resources and services. Introduction to government social protection "
            "programs (cash transfers, feeding programs), children's protection systems, and community-based organizations prepares students for practical community "
            "work. Students develop interpersonal skills, cultural sensitivity, empathy, listening skills, patience, problem-solving abilities, and genuine commitment "
            "to serving communities and vulnerable groups. Assessment through KNEC examinations includes theory tests and practical fieldwork evaluations. Graduates "
            "receive nationally recognized KNEC Certificate enabling employment in community development and social service roles."
        ),
        (
            "Graduates secure employment as community development assistants, social work assistants, project assistants in NGOs, field officers, community "
            "mobilizers, youth workers, children's officers (assistant level), community health volunteers coordinators, program assistants, or outreach workers. "
            "Employment opportunities exist in NGOs and international organizations (Plan International, World Vision, Save the Children, CARE), county governments "
            "(social services departments), government ministries (Labor and Social Protection, Health), community-based organizations (CBOs), faith-based "
            "organizations (churches, mosques), children's homes and rescue centers, rehabilitation centers, community development projects, HIV/AIDS support "
            "organizations, women and youth empowerment programs, microfinance institutions (community mobilization), and rural development programs. Starting "
            "salaries range from KSh 18,000-35,000 monthly depending on organization type and funding. NGOs and international organizations typically offer better "
            "compensation and benefits. The social development sector provides meaningful employment helping communities and vulnerable groups. With experience "
            "(3-5 years) and proven impact, development workers advance to program officers, project coordinators, or field supervisors earning KSh 40,000-70,000 "
            "monthly. Further education through Diploma or Degree in Social Work and Community Development significantly enhances career prospects, enabling senior "
            "positions like project managers, program managers, or social work officers earning KSh 60,000-120,000+ in established organizations. Professional "
            "registration with National Council for Social Workers after completing degree requirements enables independent practice. Some graduates establish "
            "their own community-based organizations or consultancies offering community development services, training, or project management. The field attracts "
            "passionate individuals committed to social change and helping vulnerable populations. Skills in community mobilization, project management, and working "
            "with diverse groups are valuable across many sectors. International organizations offer opportunities for working in different regions or countries. "
            "Specializing in specific areas like child protection, gender advocacy, livelihood programs, or disaster response enhances expertise and career "
            "advancement. Additional certifications in project management, monitoring and evaluation, or proposal writing improve employability. The work provides "
            "fulfillment from making tangible difference in people's lives and community transformation. Building strong community relationships, demonstrating "
            "commitment to service, and achieving measurable development outcomes leads to career growth and reputation in the community development sector. "
            "Continuous learning about development approaches, donor requirements, and community needs ensures effectiveness and relevance in serving communities."
        ),
        "1 year (2 semesters)",
        "Kenya National Examinations Council (KNEC)"
    ))

    return programs


# ============================================================
# ARTISAN PROGRAMS (Minimum: D- / 2 points)
# ============================================================

def generate_artisan_programs() -> List[Dict]:
    """
    Generate comprehensive Artisan (Craft) programs.
    Minimum requirement: D- (2 points) in KCSE.
    """
    level = "Artisan"
    programs = []

    # CONSTRUCTION & BUILDING ARTISAN
    programs.append(make_program(
        "Artisan in Masonry",
        level,
        "Construction & Building Trades > Masonry",
        "D-",
        8,
        [
            "Mathematics (Minimum D- / 2 points) OR",
            "English or Kiswahili (Minimum D- / 2 points) OR",
            "Any other subject (Minimum D- / 2 points)"
        ],
        (
            "A practical artisan course providing hands-on training in masonry and building construction including bricklaying and blocklaying techniques, "
            "stone masonry, wall construction, foundation laying, mortar preparation and mixing, building materials identification and use, basic building "
            "measurements and setting out, use of masonry tools (trowels, levels, plumb bobs), plastering and rendering, building safety, and quality standards "
            "in masonry work. Students gain extensive practical experience through workshop training involving actual wall construction practice, laying bricks "
            "and blocks in different bonds (stretcher bond, English bond, Flemish bond), corner work, openings construction (doors and windows), plastering "
            "practice, and working with different wall materials (bricks, concrete blocks, stones). The curriculum covers proper mortar mixing ratios, cement, "
            "sand and water proportions, curing of walls, maintaining vertical and horizontal alignment using spirit levels and plumb lines, and achieving quality "
            "finishes. Students learn to interpret simple building plans, measure and mark out walls, calculate material quantities, and follow instructions from "
            "supervisors or building plans. Training emphasizes safety on construction sites including use of personal protective equipment, scaffolding safety, "
            "safe handling of materials, and awareness of site hazards. Introduction to modern walling materials (interlocking blocks, pre-fabricated panels) and "
            "sustainable building practices provides broader perspective. Practical industrial attachment on actual construction sites provides real-world experience "
            "in residential, commercial, or institutional building projects working alongside experienced masons. Students develop physical stamina, hand-eye "
            "coordination, attention to detail, pride in quality work, and professional work ethics essential for skilled masons. Assessment through KNEC examinations "
            "includes practical masonry tests demonstrating competency in wall construction and related skills. Graduates receive nationally recognized KNEC Artisan "
            "Certificate in Masonry enabling employment as skilled masons or self-employment in construction industry."
        ),
        (
            "Graduates work as masons (fundis), bricklayers, blocklayers, stone masons, building artisans, construction workers, or masonry foremen. Employment "
            "opportunities exist in construction companies and building contractors of all sizes, real estate development companies, county and national government "
            "infrastructure projects (roads, bridges, buildings), building maintenance companies, self-employment as independent artisan masons serving individual "
            "home builders, renovation contractors, and general construction work. Kenya's growing construction sector driven by urbanization, infrastructure "
            "development (affordable housing, roads, schools, hospitals), and private building creates strong continuous demand for skilled masons. Earnings vary "
            "significantly based on skill level, location, and type of work: entry-level masons earn KSh 500-800 daily wage, experienced masons command KSh 1,000-1,500 "
            "daily, while highly skilled specialist masons (stone work, decorative work) can charge KSh 1,800-3,000 daily. With consistent work 20-25 days monthly, "
            "skilled masons typically earn KSh 25,000-60,000 monthly, with top artisans in urban areas earning even more. Many masons work independently as small-scale "
            "contractors taking on complete house construction projects or specific masonry jobs, pricing projects based on scope and earning KSh 50,000-200,000+ per "
            "project depending on size. Self-employment offers flexibility and unlimited income potential for ambitious and reliable masons. Building strong reputation "
            "for quality work, reliability, fair pricing, and honest dealings leads to steady flow of work through customer referrals. Urban and peri-urban areas offer "
            "more work opportunities but also more competition. With experience (5+ years), exceptional masons become masonry foremen or site supervisors for construction "
            "companies earning KSh 35,000-70,000 monthly salaries plus benefits. Some masons specialize in particular areas: stone masonry (retaining walls, decorative "
            "features), tiling, or heritage building restoration, commanding premium rates. Further training through Certificate or Diploma in Building and Construction "
            "enhances technical knowledge and opens opportunities in construction management. The trade provides sustainable livelihood and employment security as "
            "construction activities continue regardless of economic conditions. Masonry skills are highly transferable internationally - skilled masons find opportunities "
            "in Middle East, other African countries, and globally wherever construction occurs. Starting with small residential projects and gradually building capacity "
            "to handle larger commercial projects enables business growth. Forming construction groups or cooperatives improves access to larger contracts and equipment. "
            "Continuous improvement in skills, learning new techniques, and maintaining quality standards ensures competitiveness and career longevity in construction "
            "industry."
        ),
        "6 months to 1 year",
        "Kenya National Examinations Council (KNEC)"
    ))

    programs.append(make_program(
        "Artisan in Carpentry and Joinery",
        level,
        "Construction & Building Trades > Carpentry",
        "D-",
        8,
        [
            "Mathematics (Minimum D- / 2 points) OR",
            "English or Kiswahili (Minimum D- / 2 points) OR",
            "Any other subject (Minimum D- / 2 points)"
        ],
        (
            "A practical artisan training in carpentry and joinery providing hands-on skills in woodworking including timber identification and selection, "
            "carpentry hand tools and their uses (saws, planes, chisels, hammers), power tools operation (circular saws, drills, routers), timber measurement "
            "and marking, cutting and shaping wood, joint making (mortise and tenon, dovetail, lap joints), door and window frame construction, door hanging, "
            "furniture making basics, roof construction and carpentry, formwork for concrete, wood finishing (sanding, staining, varnishing), timber preservation, "
            "workshop safety, and quality craftsmanship. Students gain extensive practical experience through workshop training making various carpentry items "
            "including wooden doors, window frames, furniture pieces (tables, chairs, cabinets), roof trusses, shelving, and practicing different joinery "
            "techniques. The curriculum covers reading simple carpentry drawings, calculating timber quantities, understanding wood properties and grain direction, "
            "proper tool maintenance and sharpening, and achieving precise measurements and cuts essential for quality carpentry. Students learn both traditional "
            "hand tool techniques and modern power tool operations, safety procedures when using machinery, and proper handling and storage of timber materials. "
            "Training includes practical projects where students design and build complete items from timber, applying learned skills in measuring, cutting, "
            "joining, assembling, and finishing. Introduction to modern materials (plywood, MDF, laminates, engineered wood) and contemporary furniture designs "
            "prepares students for current market demands. Practical industrial attachment in carpentry workshops, furniture manufacturers, or construction sites "
            "provides real-world experience in production environments and customer interaction. Students develop accuracy, attention to detail, creativity, "
            "problem-solving skills, patience, and pride in craftsmanship essential for skilled carpenters. Assessment through KNEC examinations includes extensive "
            "practical tests demonstrating competency in carpentry and joinery work. Graduates receive nationally recognized KNEC Artisan Certificate in Carpentry "
            "and Joinery enabling employment or self-employment in the woodworking industry."
        ),
        (
            "Graduates work as carpenters, joiners, furniture makers, construction carpenters, formwork carpenters, roof carpenters, workshop assistants, or "
            "wood crafters. Employment opportunities exist in construction companies (carpentry work on building sites), furniture manufacturing companies, "
            "carpentry and joinery workshops, building contractors, property maintenance companies, interior design firms (custom furniture), door and window "
            "manufacturers, real estate development projects, self-employment as independent carpenter artisans serving homeowners, offices, and institutions. "
            "The carpentry trade remains in high demand due to ongoing construction activities and need for wooden fixtures, furniture, and repairs. Earnings "
            "vary by skill level and specialization: entry-level carpenters earn KSh 500-800 daily, experienced carpenters command KSh 1,000-2,000 daily, while "
            "highly skilled furniture makers and specialized joiners charge KSh 2,000-4,000 daily. With steady work, skilled carpenters typically earn KSh "
            "30,000-80,000 monthly, with master craftsmen earning even more. Many carpenters work independently, taking custom orders for furniture, doors, "
            "windows, or complete carpentry packages for houses under construction. Project-based work (making full bedroom set, kitchen cabinets, complete house "
            "doors and windows) can earn KSh 50,000-300,000+ depending on scope and materials. Self-employment offers flexibility and unlimited income potential "
            "for skilled and entrepreneurial carpenters. Starting small carpentry workshop requires relatively modest investment in basic tools and workspace. "
            "Building portfolio of quality work and satisfied customers leads to referrals and repeat business essential for success. Urban and peri-urban areas "
            "provide more diverse opportunities including residential, commercial, and institutional projects. With experience (5+ years), exceptional carpenters "
            "become workshop supervisors, carpentry foremen on large construction sites, or establish thriving furniture businesses earning significantly more. "
            "Specializing in specific areas enhances earning potential: custom furniture making, kitchen cabinetry, built-in wardrobes, wooden staircases, "
            "decorative woodwork, antique furniture restoration, or boat building. Further training through Certificate or Diploma in Furniture Technology or "
            "Building and Construction improves technical knowledge and business opportunities. Skills in modern techniques like CNC woodworking, laminate work, "
            "or 3D furniture design software increase competitiveness. The carpentry trade provides sustainable livelihood with skills that remain relevant across "
            "economic conditions. International opportunities exist for skilled carpenters in construction projects globally, particularly Middle East. Combining "
            "carpentry with related skills like upholstery, wood finishing, or interior decoration creates additional income streams. Quality craftsmanship, "
            "reliability, fair pricing, and professional conduct build strong reputation leading to business growth. Continuous learning about new materials, "
            "techniques, and design trends ensures competitiveness in the evolving woodworking industry."
        ),
        "6 months to 1 year",
        "Kenya National Examinations Council (KNEC)"
    ))

    programs.append(make_program(
        "Artisan in Plumbing",
        level,
        "Construction & Building Trades > Plumbing",
        "D-",
        8,
        [
            "Mathematics (Minimum D- / 2 points) OR",
            "English or Kiswahili (Minimum D- / 2 points) OR",
            "Any other subject (Minimum D- / 2 points)"
        ],
        (
            "A hands-on artisan course providing practical plumbing skills including basic plumbing principles, pipe types and uses (GI, PVC, PPR, copper pipes), "
            "pipe cutting and joining techniques, water supply installation, drainage systems installation, sanitary fixtures installation (toilets, sinks, "
            "showers, taps), plumbing tools and equipment operation, pipe threading and fitting, leak detection and repair, blockage clearing, water tank "
            "installation, basic water pump installation, sewerage connections, plumbing measurements, and workplace safety. Students gain extensive hands-on "
            "experience through practical workshops involving pipe cutting, threading, bending, joining different pipe materials, installing complete water supply "
            "systems, drainage system installation, sanitary fixtures mounting, connecting water tanks, testing installations for leaks, and troubleshooting common "
            "plumbing problems. The curriculum covers proper plumbing practices, understanding water flow and pressure, drainage gradients, proper venting, "
            "compliance with basic plumbing standards, and quality workmanship. Students learn to use plumbing tools (pipe wrenches, cutters, threading machines, "
            "plungers, drain snakes) safely and effectively, read simple plumbing drawings, estimate materials required for jobs, and follow instructions for "
            "installations. Training includes practical problem-solving such as fixing leaking taps, unblocking drains and toilets, repairing burst pipes, and "
            "replacing faulty fixtures. Introduction to modern plumbing materials and technologies (PPR pipes, water-saving fixtures, sensor taps) prepares "
            "students for current market needs. Practical industrial attachment with plumbing companies, construction sites, or building maintenance departments "
            "provides real-world experience in diverse plumbing situations from residential to commercial installations. Students develop practical problem-solving "
            "skills, physical capability for plumbing work, customer service orientation, cleanliness habits, and professional work ethics. Assessment through KNEC "
            "examinations includes practical plumbing tests demonstrating competency in installations and repairs. Graduates receive nationally recognized KNEC "
            "Artisan Certificate in Plumbing enabling employment or self-employment in the plumbing trade."
        ),
        (
            "Graduates work as plumbers, plumbing artisans, drainage specialists, maintenance plumbers, plumbing assistants, or water system installers. Employment "
            "opportunities exist in plumbing companies and contractors, construction firms (plumbing departments), building maintenance companies, hotels and "
            "hospitality establishments (maintenance), hospitals and healthcare facilities (plumbing maintenance), schools and institutions, manufacturing industries, "
            "county water and sewerage departments, property management companies, and self-employment as independent plumber artisans. Plumbing is an essential trade "
            "with consistent demand for new installations, repairs, and maintenance across residential, commercial, and industrial sectors. Earnings vary by skill "
            "and experience: entry-level plumbers earn KSh 600-1,000 daily, experienced plumbers command KSh 1,500-2,500 daily, while highly skilled plumbers handling "
            "complex installations charge KSh 2,500-4,000+ daily. With steady work, skilled plumbers typically earn KSh 35,000-70,000 monthly, with top plumbers in "
            "urban areas earning KSh 80,000-120,000+. Many plumbers work independently offering installation and repair services, with emergency call-outs (burst "
            "pipes, major blockages) commanding premium rates especially nights and weekends. Project-based work (complete house plumbing installation) can earn KSh "
            "40,000-150,000+ depending on house size and complexity. Self-employment in plumbing offers excellent income potential for reliable and skilled artisans. "
            "Starting plumbing business requires basic tool kit and transport (motorcycle or vehicle for carrying materials and tools), with relatively low initial "
            "investment. Building reputation for quality work, reliability, and fair pricing leads to steady customer base and referrals. Urban and peri-urban areas "
            "provide abundant opportunities due to construction activities and maintenance needs. With experience (5+ years), exceptional plumbers become plumbing "
            "supervisors, foremen on large projects, or establish successful plumbing businesses employing other plumbers and handling multiple projects simultaneously. "
            "Specializing in particular areas increases earning potential: solar water heater installation, water treatment systems, industrial plumbing, drainage "
            "specialists, or luxury bathroom installations. Further training through Certificate or Diploma in Plumbing enhances technical knowledge and access to "
            "larger commercial contracts. Skills in modern plumbing technologies (water-saving systems, smart fixtures, rainwater harvesting) provide competitive "
            "advantages. The plumbing trade provides stable livelihood as water and sanitation services are essential regardless of economic conditions. International "
            "opportunities exist for skilled plumbers in construction projects globally, particularly Middle East and other developing countries. Obtaining necessary "
            "business licenses and insurance enables tendering for institutional and government contracts. Diversifying services (plumbing, drainage, water tanks, "
            "pumps, solar water heaters) creates multiple revenue streams. Building network with builders, contractors, and property developers ensures steady project "
            "flow. Quality workmanship, professional conduct, cleanliness on job sites, and excellent customer service build strong reputation essential for thriving "
            "plumbing business. Continuous learning about new materials, regulations, and technologies ensures competitiveness and relevance in the plumbing industry."
        ),
        "6 months to 1 year",
        "Kenya National Examinations Council (KNEC)"
    ))

    programs.append(make_program(
        "Artisan in Electrical Installation",
        level,
        "Construction & Building Trades > Electrical",
        "D-",
        8,
        [
            "Mathematics (Minimum D- / 2 points) OR",
            "Physics or Physical Sciences (Minimum D- / 2 points) OR",
            "Any other subject (Minimum D- / 2 points)"
        ],
        (
            "A practical artisan training providing hands-on electrical installation skills including basic electrical principles, electrical wiring for domestic "
            "and commercial buildings, electrical cables and wiring materials, electrical fittings and fixtures (sockets, switches, lights), electrical tools and "
            "equipment, conduit wiring, surface wiring, concealed wiring, earthing and grounding systems, electrical safety devices (MCBs, ELCBs, fuses), basic "
            "electrical testing and fault finding, electrical measuring instruments, reading simple electrical drawings, and electrical safety practices. Students "
            "gain extensive hands-on experience through practical workshops involving house wiring practice on wiring boards and actual installations, connecting "
            "electrical fittings (switches, sockets, light points), installing distribution boards, running cables through conduits, making proper connections, "
            "testing installations, and fault finding exercises. The curriculum covers practical electrical installation following Kenya Power regulations for "
            "domestic installations, proper cable sizing, circuit protection, safe wiring practices, and quality workmanship standards. Students learn to use "
            "electrical tools (wire strippers, crimping tools, testers, screwdrivers, pliers) safely, work with live electricity following safety procedures, "
            "use multimeters for testing, and understand electrical hazards and safety measures. Training includes practical problem-solving such as identifying "
            "and fixing electrical faults, replacing faulty switches and sockets, connecting electrical appliances, and ensuring proper earthing. Introduction to "
            "solar panel installation basics, energy-saving lighting, and modern electrical systems prepares students for evolving market demands. Practical "
            "industrial attachment in electrical contracting companies, construction sites, or maintenance departments provides real-world experience in electrical "
            "installations and repairs under supervision. Students develop safety consciousness, attention to detail, logical troubleshooting approach, customer "
            "service skills, and professional work ethics essential for electrical work. Assessment through KNEC examinations includes practical electrical "
            "installation tests demonstrating competency in wiring and basic electrical work. Graduates receive nationally recognized KNEC Artisan Certificate in "
            "Electrical Installation enabling employment or self-employment in electrical work under appropriate supervision initially."
        ),
        (
            "Graduates work as electrical wiremen, electrical assistants, maintenance electricians (basic level), electrical installers, electrical helpers in "
            "construction, or electrical artisans. Employment opportunities exist in electrical contracting companies, construction firms (electrical departments), "
            "building maintenance companies, manufacturing industries (maintenance), hotels and hospitality (electrical maintenance), institutions (schools, hospitals), "
            "county electrical departments, and self-employment offering electrical installation and repair services. The electrical trade provides steady employment "
            "due to continuous construction activities and electrical maintenance needs. Entry-level electrical wiremen earn KSh 700-1,200 daily, experienced "
            "electricians command KSh 1,500-2,500 daily, while skilled electrical artisans handling complex installations charge KSh 2,500-4,000 daily. With "
            "consistent work, skilled electricians typically earn KSh 35,000-75,000 monthly, with top electricians in urban areas earning KSh 80,000-120,000+. "
            "Many electricians work independently offering house wiring, electrical repairs, appliance installations, and general electrical services. Complete "
            "house wiring projects earn KSh 30,000-120,000+ depending on house size and electrical load. Self-employment offers good income potential for reliable "
            "and skilled electrical artisans. Starting electrical services business requires basic tool kit and test equipment with modest initial investment. "
            "Building reputation for safe quality work, reliability, and reasonable pricing leads to steady customer base through referrals. Urban construction "
            "boom and electrical maintenance needs provide abundant opportunities. With experience (3-5 years) and additional training, electricians can obtain "
            "Electrical Wireman license from Engineers Registration Board (ERB) enabling independent contracting and better-paying opportunities. Certified wiremen "
            "can tender for institutional contracts and commercial projects with significantly higher earning potential. Specializing increases income: solar panel "
            "installation, electrical appliance repairs, industrial electrical work, or CCTV and security system installation. Further training through Certificate "
            "or Diploma in Electrical Engineering enhances technical knowledge and career opportunities. The electrical trade provides sustainable livelihood with "
            "skills that remain relevant across economic cycles. International opportunities exist for skilled electricians in construction and industrial projects "
            "globally. Growing solar energy market creates opportunities for electricians trained in solar installations. Combining electrical skills with related "
            "areas (electronics repairs, appliance servicing, generator maintenance) creates additional income streams. Safety must always be priority - proper "
            "training, following safety procedures, and using correct tools and equipment prevents accidents. Building professional network with builders, contractors, "
            "and property owners ensures steady project flow. Quality workmanship, adherence to electrical codes, reliability, and fair pricing build strong "
            "reputation essential for successful electrical business. Continuous learning about new technologies, safety standards, and electrical systems ensures "
            "competitiveness in the electrical field."
        ),
        "6 months to 1 year",
        "Kenya National Examinations Council (KNEC)"
    ))

    # MECHANICAL & AUTOMOTIVE ARTISAN
    programs.append(make_program(
        "Artisan in Motor Vehicle Mechanics",
        level,
        "Automotive & Mechanical > Motor Vehicle",
        "D-",
        8,
        [
            "Mathematics (Minimum D- / 2 points) OR",
            "Physics or Physical Sciences (Minimum D- / 2 points) OR",
            "Any other subject (Minimum D- / 2 points)"
        ],
        (
            "A practical artisan course providing hands-on training in motor vehicle repair and maintenance including engine basics and operation, engine "
            "dismantling and assembly, engine repair fundamentals, fuel systems (carburetor and fuel injection basics), ignition systems, cooling systems, "
            "lubrication systems, electrical systems basics (battery, alternator, starter motor), brake systems, suspension systems, transmission basics, "
            "clutch operation and repair, basic diagnostics and fault finding, vehicle servicing procedures, use of garage tools and equipment, vehicle safety "
            "checks, and workshop safety. Students gain extensive hands-on experience through practical workshops involving actual vehicle repairs: engine "
            "overhaul practice, replacing worn parts (piston rings, bearings, valves), brake system repairs and servicing, suspension repairs, electrical fault "
            "finding and repairs, oil and filter changes, tire repairs and replacement, and general vehicle maintenance tasks. The curriculum covers both petrol "
            "and diesel engines, understanding different vehicle systems, identifying faulty components, using diagnostic tools (multimeters, compression testers), "
            "proper use of garage equipment (jacks, hoists, wheel alignment machines), and following service schedules. Students learn to diagnose common vehicle "
            "problems through symptoms (noises, performance issues, warning lights), perform systematic troubleshooting, repair or replace faulty parts, and test "
            "repairs properly. Training includes reading basic wiring diagrams, understanding vehicle manuals, proper handling of automotive fluids, waste disposal, "
            "and maintaining clean organized workshop. Introduction to modern vehicle technologies (fuel injection, electronic systems, diagnostics) prepares "
            "students for working on contemporary vehicles. Practical industrial attachment in garages, motor vehicle service centers, or fleet maintenance "
            "workshops provides real-world experience in busy automotive repair environments and customer interaction. Students develop mechanical aptitude, "
            "problem-solving skills, patience and attention to detail, physical capability for mechanical work, and customer service orientation essential for "
            "automotive technicians. Assessment through KNEC examinations includes practical vehicle repair tests demonstrating competency in mechanical work. "
            "Graduates receive nationally recognized KNEC Artisan Certificate in Motor Vehicle Mechanics enabling employment or self-employment in automotive "
            "repair industry."
        ),
        (
            "Graduates work as motor vehicle mechanics, auto mechanics, garage technicians, vehicle service technicians, fleet maintenance mechanics, or automotive "
            "artisans. Employment opportunities exist in motor vehicle garages and service centers, vehicle dealerships (service departments), motor vehicle assembly "
            "plants, fleet management companies, transport companies (maintenance departments), county and government motor vehicle pools, matatu and bus companies, "
            "construction companies (equipment maintenance), and self-employment operating own garage or mobile mechanics services. Kenya's large vehicle population "
            "and imported used vehicles requiring frequent repairs create strong continuous demand for mechanics. Earnings vary by skill and specialization: entry-level "
            "mechanics earn KSh 600-1,000 daily, experienced mechanics command KSh 1,200-2,500 daily, while highly skilled diagnostic technicians and specialist "
            "mechanics charge KSh 2,500-5,000 daily. With steady work, skilled mechanics typically earn KSh 30,000-75,000 monthly as employees or more through self-employment. "
            "Many mechanics work independently from home workshops, roadside garages, or as mobile mechanics (coming to customer locations), charging per job rather "
            "than daily rates - major repairs (engine overhaul, transmission repairs) can earn KSh 20,000-80,000+ per job depending on vehicle and complexity. "
            "Self-employment offers unlimited income potential for skilled and entrepreneurial mechanics. Starting small garage requires basic tools, workspace, and "
            "some working capital for spare parts, with possibility of gradual expansion. Building reputation for quality repairs, honest dealings, and fair pricing "
            "leads to loyal customer base and referrals essential for success. Urban and peri-urban areas along busy roads provide good locations for garages. With "
            "experience (5+ years), exceptional mechanics become garage foremen, workshop supervisors, or establish thriving automotive repair businesses employing "
            "other mechanics and handling multiple vehicles. Specializing significantly increases earning potential: diesel engine specialists, automatic transmission "
            "experts, electrical diagnostics specialists, brake specialists, air conditioning experts, or modern vehicle electronics and computer diagnostics. Further "
            "training through Certificate or Diploma in Automotive Engineering enhances technical knowledge and opens opportunities in dealerships and corporate fleets. "
            "Additional certifications (manufacturer training from Toyota, Nissan, Isuzu, etc.) improve credentials and access to better opportunities. The automotive "
            "trade provides sustainable livelihood as vehicles require regular maintenance and repairs regardless of economic conditions. Diversifying services "
            "(mechanical repairs, electrical, body work, spray painting) in one location creates full-service garage attracting more customers. Combining mechanical "
            "skills with business acumen leads to successful garage business. Investing in diagnostic equipment, quality tools, and continuous learning about new "
            "vehicle technologies ensures competitiveness. Specializing in particular vehicle makes/models or vehicle types (commercial vehicles, matatus, heavy trucks) "
            "can create niche markets. Building relationships with spare parts suppliers ensures competitive pricing and parts availability. Honest assessments, quality "
            "repairs, warranty on work done, clean workspace, and professional customer service build strong reputation leading to business growth. International "
            "opportunities exist for skilled automotive technicians particularly in Middle East and other developing countries. The field rewards continuous learning as "
            "vehicle technologies evolve - mechanics who stay updated with training remain competitive and valuable."
        ),
        "6 months to 1 year",
        "Kenya National Examinations Council (KNEC)"
    ))

    programs.append(make_program(
        "Artisan in Welding and Fabrication",
        level,
        "Automotive & Mechanical > Welding",
        "D-",
        8,
        [
            "Mathematics (Minimum D- / 2 points) OR",
            "Physics or Physical Sciences (Minimum D- / 2 points) OR",
            "Any other subject (Minimum D- / 2 points)"
        ],
        (
            "A hands-on artisan training providing practical welding and metal fabrication skills including welding principles and safety, arc welding (SMAW), "
            "gas welding and cutting, basic MIG/MAG welding, welding positions and techniques, metal identification and selection, metal cutting and shaping, "
            "sheet metal work, metal bending and forming, fabrication basics, welding symbols reading, measuring and marking metals, grinding and finishing, "
            "welding defects and remedies, and workshop safety practices. Students gain extensive practical experience through workshops involving actual welding "
            "practice in different positions (flat, horizontal, vertical, overhead), making various weld joints (butt joints, lap joints, T-joints, corner joints), "
            "gas cutting practice, sheet metal fabrication projects, making metal structures (gates, grills, frames, stands), and quality weld inspection. The "
            "curriculum covers proper electrode selection, welding current settings, joint preparation, tack welding, welding sequence, distortion control, and "
            "achieving quality welds. Students learn to use welding equipment (arc welding machines, gas welding sets, cutting torches) safely including proper "
            "PPE use (welding helmets, gloves, aprons, safety boots), workshop tools (grinders, drills, measuring tools), and understanding welding hazards and "
            "safety procedures. Training includes reading simple fabrication drawings, calculating material requirements, planning fabrication sequences, and "
            "quality control basics. Introduction to advanced welding processes (MIG, TIG basics) and modern fabrication techniques prepares students for diverse "
            "welding applications. Practical industrial attachment in welding workshops, fabrication shops, or construction sites provides real-world experience "
            "in production welding environments and commercial fabrication work. Students develop hand-eye coordination, steady hands, attention to detail, safety "
            "consciousness, problem-solving skills, and pride in quality workmanship essential for skilled welders. Assessment through KNEC examinations includes "
            "extensive practical welding tests demonstrating competency in various welding techniques and fabrication work. Graduates receive nationally recognized "
            "KNEC Artisan Certificate in Welding and Fabrication enabling employment or self-employment in metal fabrication industry."
        ),
        (
            "Graduates work as welders, fabricators, metal workers, arc welders, gas welders, welder-fitters, structural welders, or fabrication artisans. "
            "Employment opportunities exist in welding and fabrication workshops, construction companies (structural welding), manufacturing industries, metal "
            "fabrication companies, motor vehicle repair garages (body repairs), engineering workshops, shipyards, pipeline construction, oil and gas industry, "
            "steel fabrication firms, agricultural machinery manufacturers, and self-employment offering welding and fabrication services. Welding is highly sought-after "
            "trade with strong demand across construction, manufacturing, and maintenance sectors. Earnings vary significantly by skill level and welding type: "
            "entry-level welders earn KSh 600-1,000 daily, experienced welders command KSh 1,500-3,000 daily, while highly skilled certified welders (coded welders) "
            "charge KSh 3,000-6,000+ daily especially for specialized work (pipeline, structural, underwater). With steady work, skilled welders typically earn KSh "
            "40,000-90,000 monthly, with top welders and fabricators earning KSh 100,000-200,000+ monthly. Many welders work independently operating small fabrication "
            "workshops making gates, grills, window frames, metal furniture, structures, and offering repair welding services - projects range from KSh 5,000 for "
            "simple gates to KSh 200,000+ for complex fabrication projects. Self-employment offers excellent income potential for skilled and entrepreneurial welders. "
            "Starting welding business requires welding machine, basic tools, workspace, and some operating capital, with gradual expansion as business grows. Building "
            "reputation for quality welds, reliable service, and fair pricing leads to steady customers and referrals. Urban areas provide diverse opportunities from "
            "small repair welding to large fabrication contracts. With experience (5+ years) and additional certifications, welders become welding supervisors, welding "
            "inspectors, or establish successful fabrication businesses employing other welders and handling multiple projects. Obtaining coded welder certification "
            "through testing significantly increases earning potential and opens opportunities in oil and gas, pipeline construction, structural welding for buildings "
            "and bridges, and industrial projects - coded welders earn premium rates (KSh 4,000-8,000 daily or more). Specializing in particular welding processes "
            "(TIG welding for aluminum and stainless steel, MIG welding, underwater welding) or applications (pipeline welding, boiler making, pressure vessel welding) "
            "creates high-value niche expertise. Further training through Certificate or Diploma in Welding and Fabrication or Mechanical Engineering enhances technical "
            "knowledge and career opportunities. International opportunities abound for skilled welders particularly in Middle East, Europe, and globally wherever "
            "construction and industrial projects occur - international welders can earn USD 2,000-5,000+ monthly. The welding trade provides sustainable livelihood "
            "with skills applicable across numerous industries. Combining welding with fabrication design skills, artistic metal work, or metal finishing creates "
            "additional opportunities. Investing in quality welding equipment, learning advanced processes, and obtaining certifications ensures competitiveness. "
            "Diversifying services (welding, fabrication, machining, metal repairs) attracts broader customer base. Building network with construction companies, "
            "property developers, and institutions ensures steady project flow. Quality workmanship, meeting deadlines, safety compliance, and professional conduct "
            "build strong reputation essential for thriving welding business. Continuous learning about new welding technologies, materials, and techniques ensures "
            "career longevity and relevance in the evolving metal fabrication industry."
        ),
        "6 months to 1 year",
        "Kenya National Examinations Council (KNEC)"
    ))

    # BEAUTY & PERSONAL CARE ARTISAN
    programs.append(make_program(
        "Artisan in Hairdressing and Beauty Therapy",
        level,
        "Beauty & Personal Care > Hairdressing",
        "D-",
        8,
        [
            "English or Kiswahili (Minimum D- / 2 points) OR",
            "Any other subject (Minimum D- / 2 points)"
        ],
        (
            "A practical artisan course providing comprehensive training in hairdressing and beauty services including hair structure and types, shampooing and "
            "conditioning, hair cutting techniques (men's cuts, women's cuts, children's cuts), hair styling and blow-drying, hair coloring and bleaching, hair "
            "treatments (perming, relaxing, keratin treatment), hair braiding and extensions, natural hair care, wig making and fixing, basic beauty therapy "
            "(facials, manicure, pedicure, makeup), salon hygiene and sanitation, customer service, salon management basics, and professional ethics. Students "
            "gain extensive hands-on practice through training on live models and mannequins learning various cutting techniques (blunt cuts, layering, graduation, "
            "texturizing), styling techniques (curling, straightening, updos, braiding styles), coloring application, chemical treatments, and beauty procedures. "
            "The curriculum covers proper use of salon tools and equipment (scissors, clippers, dryers, flat irons, curling irons, steamers), product knowledge "
            "(shampoos, conditioners, colors, relaxers, styling products), understanding hair problems and solutions, and creating styles suitable for different "
            "occasions and face shapes. Students learn consultation skills to understand client needs, recommend appropriate services and products, perform skin "
            "and hair analysis, and deliver satisfactory results. Training includes salon hygiene practices, tool sterilization, proper draping, safety precautions "
            "when handling chemicals, and maintaining clean organized workspace. Introduction to current hair trends, modern techniques (balayage, ombre, Brazilian "
            "blowout), natural hair movement, and social media marketing for salons prepares students for contemporary beauty industry. Practical industrial attachment "
            "in salons, beauty parlors, or barbershops provides real-world experience in busy salon environments, diverse clientele, time management, and professional "
            "service delivery. Students develop creativity, attention to detail, manual dexterity, interpersonal skills, patience, stamina to stand long hours, and "
            "customer service orientation essential for beauty professionals. Assessment through KNEC examinations includes practical tests demonstrating competency "
            "in hairdressing and beauty services. Graduates receive nationally recognized KNEC Artisan Certificate in Hairdressing and Beauty Therapy enabling "
            "employment in salons or establishing own beauty businesses."
        ),
        (
            "Graduates work as hairdressers, hair stylists, beauticians, beauty therapists, salon assistants, barbers, braiders, makeup artists, or salon attendants. "
            "Employment opportunities exist in hair salons and beauty parlors, barbershops, beauty spas, hotels and resorts (salon services), high-end salons in "
            "shopping malls, unisex salons, bridal shops (makeup and hair styling), fashion industry (runway shows, photoshoots), media and entertainment (film, TV "
            "makeup), funeral homes (mortuary beauticians), and self-employment operating own salon or providing mobile beauty services. The beauty industry thrives "
            "in Kenya with growing middle class willing to spend on personal grooming and appearance. Earnings vary widely: salon employees earn KSh 12,000-30,000 "
            "monthly basic salary plus commission on services and products, experienced stylists in upscale salons earn KSh 30,000-60,000 monthly, while successful "
            "salon owners can earn KSh 50,000-300,000+ monthly depending on salon size, location, and clientele. Many hairdressers work independently from home-based "
            "salons, kiosks, or provide mobile services visiting clients at homes or offices - independent stylists charge per service (KSh 500-5,000+ per client "
            "depending on service complexity) potentially earning KSh 40,000-100,000+ monthly with loyal customer base. Self-employment offers flexibility and unlimited "
            "income potential for talented and entrepreneurial beauty professionals. Starting small salon requires modest investment in basic equipment, products, "
            "workspace, with gradual expansion as clientele grows. Location is critical - busy areas, near residential estates, shopping centers, or along main roads "
            "attract walk-in customers. Building loyal clientele through quality service, friendly personality, reliability, and fair pricing ensures steady income. "
            "Social media marketing (Instagram, Facebook, TikTok) showcasing work attracts new clients significantly. Urban areas especially Nairobi and major towns "
            "provide more diverse opportunities and higher earning potential. Specializing increases marketability and income: bridal hair and makeup (earning KSh "
            "10,000-50,000 per wedding), natural hair specialist, color specialist, barbing expert, braiding specialist, or celebrity stylist. Further training through "
            "Certificate or Diploma in Beauty Therapy or specialized courses (makeup artistry, nail technology, spa therapy) enhances skills and service offerings. "
            "International beauty certifications (City & Guilds, CIDESCO) improve credentials and opportunities in upscale establishments or international markets. "
            "With experience (3-5 years) and business acumen, successful stylists open multiple salon branches, train other stylists, or establish beauty training "
            "academies. The beauty industry provides sustainable livelihood with repeat customers providing consistent income. Retailing hair care products, beauty "
            "supplies, or wigs creates additional revenue streams. Offering comprehensive services (hair, nails, makeup, spa treatments) in one location attracts more "
            "clients and increases earning per customer. Keeping updated with trends, new techniques, and products through workshops and online resources ensures "
            "competitiveness. Building professional image through personal grooming, maintaining clean attractive salon, providing excellent customer experience, and "
            "ethical business practices creates strong reputation essential for success. Joining professional associations, participating in beauty competitions, and "
            "networking with other beauty professionals opens opportunities for growth. The beauty industry offers creative fulfilling career helping clients look "
            "and feel their best, with potential for significant income and business ownership for dedicated professionals."
        ),
        "6 months to 1 year",
        "Kenya National Examinations Council (KNEC)"
    ))

    # TAILORING & FASHION ARTISAN
    programs.append(make_program(
        "Artisan in Dress Making and Tailoring",
        level,
        "Fashion & Design > Tailoring",
        "D-",
        8,
        [
            "English or Kiswahili (Minimum D- / 2 points) OR",
            "Any other subject (Minimum D- / 2 points)"
        ],
        (
            "A practical artisan training in garment construction and tailoring providing hands-on skills in dress making and clothing production including fabric "
            "types and characteristics, taking body measurements accurately, pattern drafting basics, pattern adaptation, fabric cutting and layout, hand sewing "
            "techniques, machine sewing operations (straight stitch, zigzag, overlocking), seam types and finishes, construction techniques for different garments "
            "(shirts, trousers, dresses, skirts, suits), fitting and alterations, finishing techniques (hems, buttonholes, zippers, linings), pressing and ironing, "
            "garment repairs and adjustments, customer service, and costing garments. Students gain extensive hands-on experience through practical workshops making "
            "complete garments from taking measurements through cutting, sewing, fitting, and finishing - students produce various items including men's shirts and "
            "trousers, women's dresses and skirts, children's clothes, school uniforms, and other garments. The curriculum covers proper use of sewing equipment "
            "(sewing machines, overlockers, irons, cutting tools), understanding different fabric behaviors, selecting appropriate fabrics for designs, quality "
            "control in garment construction, and achieving professional finishes. Students learn to interpret fashion designs, draft simple patterns from measurements, "
            "adapt patterns for different body types and sizes, calculate fabric requirements, and price garments considering materials and labor. Training includes "
            "common alterations (taking in/letting out, shortening/lengthening, repairs), understanding garment quality standards, and maintaining sewing equipment. "
            "Introduction to fashion trends, modern designs, computerized sewing machines, and small business management basics prepares students for entrepreneurship. "
            "Practical industrial attachment in tailoring shops, garment factories, fashion houses, or boutiques provides real-world experience in production "
            "environments, dealing with diverse customer preferences, and professional garment construction. Students develop creativity, attention to detail, hand-eye "
            "coordination, patience, problem-solving skills, and customer relations essential for successful tailors. Assessment through KNEC examinations includes "
            "practical tests requiring students to construct complete garments demonstrating competency in tailoring skills. Graduates receive nationally recognized "
            "KNEC Artisan Certificate in Dress Making and Tailoring enabling employment or establishing own tailoring businesses."
        ),
        (
            "Graduates work as tailors, dress makers, seamstresses/seamsters, garment makers, alteration specialists, costume makers, or tailoring assistants. "
            "Employment opportunities exist in tailoring shops and boutiques, garment manufacturing factories, fashion houses and designers, costume departments "
            "(theater, film, TV productions), uniform manufacturers, schools and institutions (tailoring departments), textile companies, export garment factories, "
            "and self-employment operating own tailoring business. The tailoring industry remains vibrant in Kenya with strong demand for custom-made clothing, "
            "school uniforms, alterations, and affordable fashion. Many Kenyans prefer tailored clothes over ready-made for better fit and customization. Earnings "
            "vary by skill level and business model: employed tailors earn KSh 10,000-25,000 monthly, experienced tailors in good locations earn KSh 25,000-50,000 "
            "monthly, while successful tailoring business owners can earn KSh 50,000-200,000+ monthly depending on volume, clientele, and specialization. Independent "
            "tailors charge per garment: simple items (KSh 500-1,500), formal wear (KSh 2,000-5,000), suits (KSh 5,000-15,000), wedding dresses (KSh 10,000-50,000+) "
            "- skilled tailors with steady customer flow easily earn KSh 40,000-100,000+ monthly. Self-employment offers excellent income potential for talented and "
            "business-minded tailors. Starting tailoring business requires sewing machine(s), overlocker, workspace, basic materials and notions, with relatively low "
            "initial investment - many start from home reducing overhead costs. Location near residential areas, markets, or along busy streets provides good customer "
            "traffic. Building loyal clientele through quality workmanship, good fitting, timely delivery, fair pricing, and excellent customer service ensures steady "
            "income and referrals. School uniforms provide consistent bulk business especially January and May when schools open. Corporate uniforms for companies, "
            "organizations, and institutions offer lucrative contracts. Specializing increases earning potential and reputation: men's suits specialist, wedding gowns "
            "and formal wear, African fashion (kitenge, ankara designs), children's wear, or alterations specialist. Further training through Certificate or Diploma "
            "in Fashion and Design enhances technical skills, pattern making, and fashion business knowledge. With experience (5-7 years) and capital, successful "
            "tailors expand businesses opening multiple outlets, hiring other tailors, adding retail clothing sections, or moving into fashion design and production. "
            "Some establish clothing labels producing ready-to-wear lines sold in boutiques and online. Combining tailoring with fabric retail creates additional revenue "
            "and convenience for customers. Online presence through social media (Instagram, Facebook showcasing work) and e-commerce platforms significantly expands "
            "customer reach beyond physical location. Participating in fashion shows, exhibitions, and community events increases visibility and attracts customers. "
            "The tailoring trade provides sustainable livelihood with skills always in demand regardless of economic conditions. Offering quick alterations and repairs "
            "service attracts walk-in customers and generates additional income. Building reputation for excellent fitting, quality construction, creative designs, "
            "timely delivery, and professional service leads to word-of-mouth referrals essential for business growth. Keeping updated with fashion trends through "
            "magazines, online resources, and training workshops ensures competitive and relevant services. Investing in quality equipment, improving skills continuously, "
            "and maintaining high standards ensures success and longevity in the competitive but rewarding tailoring business."
        ),
        "6 months to 1 year",
        "Kenya National Examinations Council (KNEC)"
    ))

    # FOOD PRODUCTION ARTISAN
    programs.append(make_program(
        "Artisan in Food and Beverage Production",
        level,
        "Hospitality & Food Service > Food Production",
        "D-",
        8,
        [
            "English or Kiswahili (Minimum D- / 2 points) OR",
            "Any other subject (Minimum D- / 2 points)"
        ],
        (
            "A practical artisan course providing hands-on training in food preparation and cooking including basic cooking methods, food preparation techniques, "
            "knife skills, kitchen equipment operation, recipe following, portion control, food hygiene and safety, food storage, common dishes preparation (local "
            "and international), breakfast cookery, soup making, vegetable preparation, meat and chicken preparation, pastry basics, baking basics, food presentation, "
            "kitchen organization, and safety practices. Students gain extensive practical experience through training kitchens preparing various dishes including "
            "Kenyan foods (ugali, githeri, mukimo, nyama choma, chapati, mandazi), common international dishes, breakfast items, main courses, snacks, and basic "
            "pastries. The curriculum covers proper food handling, preventing contamination, understanding cooking temperatures and times, seasoning, and achieving "
            "taste quality. Students learn to use kitchen tools and equipment safely (knives, ovens, stoves, fryers, mixers), maintain cleanliness, organize "
            "ingredients and workspace, and work efficiently in kitchen environments. Training includes understanding different foods, basic nutrition, cooking for "
            "numbers, minimizing waste, and quality control in food production. Introduction to food presentation, garnishing basics, and customer service in food "
            "service prepares students for diverse work settings. Practical industrial attachment in hotel kitchens, restaurants, institutional catering, or food "
            "production businesses provides real-world experience in busy kitchen operations and food service. Students develop speed and efficiency, ability to work "
            "under pressure, teamwork, cleanliness habits, attention to taste and presentation, and professional kitchen conduct. Assessment through KNEC examinations "
            "includes practical cooking tests demonstrating competency in food preparation. Graduates receive nationally recognized KNEC Artisan Certificate in Food "
            "and Beverage Production enabling employment in food service or starting food businesses."
        ),
        (
            "Graduates work as cooks, kitchen assistants, food preparation workers, catering assistants, institutional cooks, or food production assistants. "
            "Employment opportunities exist in hotels and restaurants, fast food outlets, cafes and coffee shops, institutional catering (schools, hospitals, "
            "companies), catering companies, private households (personal cooks), food kiosks and eateries, bakeries, food processing companies, and self-employment "
            "running food businesses. The food service industry provides abundant opportunities as eating establishments operate daily requiring kitchen staff. "
            "Employed cooks earn KSh 12,000-30,000 monthly depending on establishment type and experience. Hotels and upscale restaurants offer better compensation. "
            "Many graduates successfully establish their own food businesses with relatively low startup capital: food kiosks, small restaurants, catering services, "
            "home-based food businesses, food delivery services, or specialize in particular foods (nyama choma, traditional foods, fast food, baked goods). Small "
            "food kiosk or restaurant can generate KSh 30,000-100,000+ monthly profit depending on location, menu, pricing, and customer traffic. Catering for events "
            "(weddings, meetings, parties) offers good income - events catering charges range from KSh 300-1,500 per person depending on menu, potentially earning "
            "KSh 50,000-200,000+ per large event. Self-employment offers unlimited income potential for entrepreneurial and skilled cooks. Location is critical for "
            "food businesses - near offices (lunch business), residential areas, bus stages, markets, or high-traffic areas ensure customers. Starting small with "
            "affordable menu, quality food, good hygiene, and excellent customer service builds customer base. Many successful food entrepreneurs started with small "
            "kiosks or home cooking growing into established restaurants. Specializing creates unique market position: specific cuisine (Somali food, coastal food, "
            "Ethiopian, Chinese), specific items (grilled chicken, fish, samosas, mandazi), healthy foods, or catering particular markets (office workers, students, "
            "travelers). Further training through Certificate in Food Production or related courses enhances culinary skills and food business knowledge. With "
            "experience and capital, successful food entrepreneurs open multiple outlets, franchise their concepts, or establish food brands. The food industry provides "
            "stable livelihood as people must eat daily regardless of economic conditions. Online food delivery platforms (Uber Eats, Glovo, Jumia Food) create "
            "additional sales channels for food businesses. Social media marketing showcasing delicious food attracts customers significantly. Maintaining consistent "
            "quality, cleanliness, reasonable pricing, friendly service, and food safety standards builds loyal customer base essential for food business success. "
            "Obtaining necessary licenses (business permit, health certificate, food handler certificate) ensures legal operation. Understanding food costs, portion "
            "control, minimizing waste, and efficient operations ensures profitability. Building supplier relationships for quality ingredients at good prices improves "
            "margins. The food business rewards passion for cooking, creativity in menu development, cleanliness, reliability, and commitment to customer satisfaction. "
            "Many food entrepreneurs achieve financial success and independence through hard work and quality food provision."
        ),
        "6 months to 1 year",
        "Kenya National Examinations Council (KNEC)"
    ))

    # ICT ARTISAN
    programs.append(make_program(
        "Artisan in Information Communication Technology",
        level,
        "ICT & Computing > Basic ICT",
        "D-",
        8,
        [
            "Mathematics (Minimum D- / 2 points) OR",
            "English or Kiswahili (Minimum D- / 2 points) OR",
            "Any other subject (Minimum D- / 2 points)"
        ],
        (
            "Practical training in computer basics, MS Office (Word, Excel, PowerPoint), internet usage, email, typing skills, file management, "
            "basic troubleshooting, cyber cafe operations, and digital literacy. Hands-on lab work covers document creation, data entry, printing, "
            "scanning, and common computer tasks essential for office work and cyber cafe services."
        ),
        (
            "Work as cyber cafe attendants, data entry clerks, computer operators, typists, office assistants, or start cyber cafes. Salaries: KSh "
            "10,000-20,000 monthly. Self-employment: cyber cafes earn KSh 20,000-60,000+ monthly. Opportunities in offices, schools, hospitals, and "
            "government for basic ICT support roles."
        ),
        "6 months to 1 year",
        "Kenya National Examinations Council (KNEC)"
    ))

    # ADDITIONAL CONSTRUCTION ARTISAN
    programs.append(make_program(
        "Artisan in Painting and Decoration",
        level,
        "Construction & Building Trades > Painting",
        "D-",
        8,
        [
            "Any subject (Minimum D- / 2 points)"
        ],
        (
            "Hands-on training in surface preparation, painting techniques, spray painting, decorative finishes, color mixing, wall papering, "
            "staining and varnishing, texture finishes, paint types and uses, brush and roller techniques, ladder safety, and customer service. "
            "Practical work on walls, ceilings, woodwork, and metal surfaces."
        ),
        (
            "Work as painters, decorators, or self-employed painting contractors. Daily rates: KSh 600-2,000. Skilled painters earn KSh "
            "30,000-80,000 monthly. House painting projects: KSh 20,000-150,000+. High demand in construction, renovations, and property maintenance."
        ),
        "6 months",
        "Kenya National Examinations Council (KNEC)"
    ))

    programs.append(make_program(
        "Artisan in Tiling and Floor Laying",
        level,
        "Construction & Building Trades > Tiling",
        "D-",
        8,
        [
            "Any subject (Minimum D- / 2 points)"
        ],
        (
            "Practical skills in floor and wall tiling, ceramic tiles, porcelain tiles, marble laying, tile cutting and fixing, grouting, "
            "surface preparation, waterproofing, tile patterns and designs, measuring and setting out, and quality finishing. Hands-on practice "
            "on floors, walls, bathrooms, and kitchens."
        ),
        (
            "Work as tilers, floor layers, or independent tiling contractors. Daily rates: KSh 800-2,500. Experienced tilers earn KSh 35,000-90,000 "
            "monthly. Projects earn KSh 30,000-200,000+ depending on area and tile type. Strong demand in construction and renovations."
        ),
        "6 months",
        "Kenya National Examinations Council (KNEC)"
    ))

    programs.append(make_program(
        "Artisan in Aluminium and Glass Work",
        level,
        "Construction & Building Trades > Aluminium & Glass",
        "D-",
        8,
        [
            "Mathematics (Minimum D- / 2 points) OR",
            "Any subject (Minimum D- / 2 points)"
        ],
        (
            "Training in aluminium window and door fabrication, glass cutting and installation, shower cubicles, partitions, shop fronts, measuring "
            "and cutting aluminium, glass handling safety, sealants application, hardware fitting, and customer consultation. Practical work on "
            "various aluminium and glass installations."
        ),
        (
            "Work as aluminium fabricators, glass installers, or run fabrication workshops. Daily rates: KSh 1,000-3,000. Skilled artisans earn "
            "KSh 40,000-100,000+ monthly. Projects: windows KSh 15,000-80,000, shower cubicles KSh 25,000-60,000. High demand in construction."
        ),
        "6 months to 1 year",
        "Kenya National Examinations Council (KNEC)"
    ))

    programs.append(make_program(
        "Artisan in Steelwork and Metal Roofing",
        level,
        "Construction & Building Trades > Roofing",
        "D-",
        8,
        [
            "Any subject (Minimum D- / 2 points)"
        ],
        (
            "Practical training in steel roof truss fabrication, iron sheet roofing installation, gutter fixing, roof measurements, cutting and "
            "bending iron sheets, ridge capping, box profile roofing, mabati fixing, roof maintenance, safety on roofs, and waterproofing basics."
        ),
        (
            "Work as roofers, steel fixers, or roofing contractors. Daily rates: KSh 800-2,000. Skilled roofers earn KSh 30,000-70,000 monthly. "
            "Roofing projects earn KSh 40,000-300,000+ depending on house size. Steady demand in construction sector."
        ),
        "6 months",
        "Kenya National Examinations Council (KNEC)"
    ))

    # ADDITIONAL AUTOMOTIVE ARTISAN
    programs.append(make_program(
        "Artisan in Auto Electrical Work",
        level,
        "Automotive & Mechanical > Auto Electrical",
        "D-",
        8,
        [
            "Mathematics (Minimum D- / 2 points) OR",
            "Physics (Minimum D- / 2 points) OR",
            "Any subject"
        ],
        (
            "Hands-on training in vehicle electrical systems, wiring, battery testing and charging, alternator and starter motor repairs, lighting "
            "systems, car audio installation, alarm systems, diagnostics, fault finding, and using electrical testing equipment."
        ),
        (
            "Work as auto electricians or self-employed. Daily rates: KSh 1,000-3,000. Skilled auto electricians earn KSh 35,000-80,000 monthly. "
            "Major repairs earn KSh 15,000-50,000 per job. Growing demand with modern vehicle electronics."
        ),
        "6 months to 1 year",
        "Kenya National Examinations Council (KNEC)"
    ))

    programs.append(make_program(
        "Artisan in Panel Beating and Spray Painting",
        level,
        "Automotive & Mechanical > Body Work",
        "D-",
        8,
        [
            "Any subject (Minimum D- / 2 points)"
        ],
        (
            "Practical training in car body repair, dent removal, panel beating, welding body parts, spray painting techniques, color matching, "
            "surface preparation, putty application, sanding, priming, painting, and polishing for professional vehicle finishes."
        ),
        (
            "Work as panel beaters, spray painters, or own body shops. Daily rates: KSh 1,000-3,000. Skilled artisans earn KSh 40,000-100,000+ "
            "monthly. Body repair jobs: KSh 20,000-150,000+ depending on damage. High demand with accident repairs."
        ),
        "6 months to 1 year",
        "Kenya National Examinations Council (KNEC)"
    ))

    programs.append(make_program(
        "Artisan in Motorcycle Mechanics",
        level,
        "Automotive & Mechanical > Motorcycle",
        "D-",
        8,
        [
            "Any subject (Minimum D- / 2 points)"
        ],
        (
            "Training in motorcycle engine repair, two-stroke and four-stroke engines, electrical systems, brake systems, clutch, transmission, "
            "suspension, tire repairs, motorcycle servicing, diagnostics, and common bodaboda motorcycle maintenance and repairs."
        ),
        (
            "Work as motorcycle mechanics or open bodaboda repair shops. Daily rates: KSh 600-2,000. Skilled mechanics earn KSh 25,000-60,000 "
            "monthly. Engine overhauls earn KSh 8,000-25,000. Huge demand with bodaboda industry growth."
        ),
        "6 months",
        "Kenya National Examinations Council (KNEC)"
    ))

    # TEXTILE & LEATHER ARTISAN
    programs.append(make_program(
        "Artisan in Shoe Making and Repair",
        level,
        "Fashion & Design > Footwear",
        "D-",
        8,
        [
            "Any subject (Minimum D- / 2 points)"
        ],
        (
            "Practical training in shoe construction, leather working, shoe repair, stitching, sole replacement, shoe design basics, leather "
            "cutting and shaping, pattern making, shoe finishing, and operating shoe-making equipment."
        ),
        (
            "Work as cobblers, shoe makers, or own shoe repair shops. Shoe repairs: KSh 200-1,500 per pair. Making shoes: KSh 2,000-8,000 per pair. "
            "Skilled artisans earn KSh 25,000-70,000 monthly. Steady demand for repairs and custom shoes."
        ),
        "6 months",
        "Kenya National Examinations Council (KNEC)"
    ))

    programs.append(make_program(
        "Artisan in Upholstery",
        level,
        "Fashion & Design > Upholstery",
        "D-",
        8,
        [
            "Any subject (Minimum D- / 2 points)"
        ],
        (
            "Hands-on training in furniture upholstery, foam cutting, fabric selection, frame repair, spring work, cushion making, car seat "
            "upholstery, pattern drafting, stitching, and finishing for sofas, chairs, mattresses, and vehicle seats."
        ),
        (
            "Work as upholsterers or own workshops. Sofa sets: KSh 15,000-60,000. Car seats: KSh 8,000-25,000. Mattresses: KSh 5,000-20,000. "
            "Skilled artisans earn KSh 30,000-80,000 monthly. Good demand in homes and auto industry."
        ),
        "6 months",
        "Kenya National Examinations Council (KNEC)"
    ))

    programs.append(make_program(
        "Artisan in Leather Work and Bag Making",
        level,
        "Fashion & Design > Leather Craft",
        "D-",
        8,
        [
            "Any subject (Minimum D- / 2 points)"
        ],
        (
            "Training in leather bag making, wallets, belts, leather cutting and stitching, pattern design, hardware attachment, leather finishing, "
            "dyeing, and creating various leather products for sale."
        ),
        (
            "Make and sell leather bags, belts, wallets, and accessories. Bags sell KSh 1,500-15,000+. Belts: KSh 500-3,000. Skilled artisans "
            "earn KSh 25,000-80,000 monthly. Growing market for quality leather products locally and exports."
        ),
        "6 months",
        "Kenya National Examinations Council (KNEC)"
    ))

    # AGRICULTURAL ARTISAN
    programs.append(make_program(
        "Artisan in Greenhouse Construction and Management",
        level,
        "Agriculture & Horticulture > Greenhouse",
        "D-",
        8,
        [
            "Agriculture or any subject (Minimum D- / 2 points)"
        ],
        (
            "Practical training in greenhouse construction, site selection, frame assembly, plastic covering, drip irrigation installation, "
            "greenhouse crop production (tomatoes, capsicum, cucumbers), pest management, and greenhouse maintenance."
        ),
        (
            "Build greenhouses or work in horticultural farms. Greenhouse construction: KSh 50,000-500,000+ per project. Greenhouse management "
            "jobs: KSh 20,000-45,000 monthly. Own greenhouse farming earns KSh 50,000-300,000+ monthly with good crops."
        ),
        "6 months",
        "Kenya National Examinations Council (KNEC)"
    ))

    programs.append(make_program(
        "Artisan in Poultry Production",
        level,
        "Agriculture & Veterinary > Poultry",
        "D-",
        8,
        [
            "Agriculture or any subject (Minimum D- / 2 points)"
        ],
        (
            "Hands-on training in poultry house construction, broiler production, layer management, feeding, disease control, vaccination, "
            "record keeping, egg handling, and poultry business basics for commercial chicken farming."
        ),
        (
            "Work in poultry farms or start own farms. Farm workers earn KSh 15,000-30,000 monthly. Own poultry farm (500 layers) earns "
            "KSh 30,000-100,000+ monthly. Broilers offer quick returns. Growing demand for chicken and eggs."
        ),
        "6 months",
        "Kenya National Examinations Council (KNEC)"
    ))

    programs.append(make_program(
        "Artisan in Dairy Production and Management",
        level,
        "Agriculture & Veterinary > Dairy",
        "D-",
        8,
        [
            "Agriculture or any subject (Minimum D- / 2 points)"
        ],
        (
            "Practical training in dairy cattle management, milking techniques, feeding, breeding basics, calf rearing, milk handling, hygiene, "
            "disease prevention, zero-grazing systems, and dairy farming business management."
        ),
        (
            "Work as dairy farm workers or own dairy farms. Farm workers earn KSh 15,000-35,000 monthly. Own dairy farm (5-10 cows) earns "
            "KSh 40,000-150,000+ monthly from milk sales. Reliable income with good farm management."
        ),
        "6 months",
        "Kenya National Examinations Council (KNEC)"
    ))

    programs.append(make_program(
        "Artisan in Beekeeping",
        level,
        "Agriculture & Horticulture > Beekeeping",
        "D-",
        8,
        [
            "Any subject (Minimum D- / 2 points)"
        ],
        (
            "Training in modern beekeeping, hive construction, bee colony management, honey harvesting, bee products processing (honey, wax, "
            "propolis), queen rearing basics, disease control, and honey marketing."
        ),
        (
            "Start beekeeping projects or work in apiaries. 10 hives produce 200-400 kg honey annually worth KSh 100,000-250,000+. Low capital "
            "investment. Can combine with farming. Growing demand for natural honey."
        ),
        "6 months",
        "Kenya National Examinations Council (KNEC)"
    ))

    # BEAUTY & PERSONAL CARE ARTISAN
    programs.append(make_program(
        "Artisan in Barbering",
        level,
        "Beauty & Personal Care > Barbering",
        "D-",
        8,
        [
            "Any subject (Minimum D- / 2 points)"
        ],
        (
            "Hands-on training in men's haircuts, shaving, beard trimming and styling, hair clipper techniques, straight razor use, customer "
            "service, salon hygiene, and barbershop management basics."
        ),
        (
            "Work in barbershops or own barbershop. Employed barbers earn KSh 15,000-35,000 monthly plus tips. Own barbershop earns "
            "KSh 30,000-100,000+ monthly. Haircuts: KSh 100-500. Low startup capital. Consistent daily demand."
        ),
        "3-6 months",
        "Kenya National Examinations Council (KNEC)"
    ))

    programs.append(make_program(
        "Artisan in Nail Technology",
        level,
        "Beauty & Personal Care > Nail Care",
        "D-",
        8,
        [
            "Any subject (Minimum D- / 2 points)"
        ],
        (
            "Training in manicure, pedicure, nail art and design, gel nails, acrylic nails, nail extensions, nail health, hygiene and "
            "sanitation, and client consultation for professional nail services."
        ),
        (
            "Work in salons or start nail services. Manicure/pedicure: KSh 500-2,000. Nail extensions: KSh 2,000-6,000. Skilled technicians "
            "earn KSh 25,000-70,000 monthly. Growing market in urban areas. Mobile services possible."
        ),
        "3-6 months",
        "Kenya National Examinations Council (KNEC)"
    ))

    programs.append(make_program(
        "Artisan in Makeup Artistry",
        level,
        "Beauty & Personal Care > Makeup",
        "D-",
        8,
        [
            "Any subject (Minimum D- / 2 points)"
        ],
        (
            "Practical training in makeup application, bridal makeup, special effects basics, color theory, contouring, eye makeup, product "
            "knowledge, hygiene, and building makeup artistry portfolio."
        ),
        (
            "Work as makeup artists or freelance. Bridal makeup: KSh 5,000-25,000+ per wedding. Regular makeup: KSh 1,500-5,000. Events and "
            "photoshoots offer good income. Successful artists earn KSh 40,000-150,000+ monthly."
        ),
        "3-6 months",
        "Kenya National Examinations Council (KNEC)"
    ))

    # HOSPITALITY & FOOD ARTISAN
    programs.append(make_program(
        "Artisan in Pastry and Baking",
        level,
        "Hospitality & Food Service > Baking",
        "D-",
        8,
        [
            "Any subject (Minimum D- / 2 points)"
        ],
        (
            "Hands-on training in bread baking, cakes, pastries, cookies, mandazi, scones, doughnuts, icing and decoration, dough preparation, "
            "oven operation, food hygiene, and bakery business basics."
        ),
        (
            "Work in bakeries or start own bakery. Bakers earn KSh 15,000-30,000 monthly. Own bakery earns KSh 30,000-150,000+ monthly. "
            "Wedding cakes: KSh 5,000-50,000+. Bread and pastries have daily demand. Good business potential."
        ),
        "6 months",
        "Kenya National Examinations Council (KNEC)"
    ))

    programs.append(make_program(
        "Artisan in Butchery",
        level,
        "Hospitality & Food Service > Butchery",
        "D-",
        8,
        [
            "Any subject (Minimum D- / 2 points)"
        ],
        (
            "Practical training in meat cutting and portioning, bone removal, sausage making, meat grading, hygiene and safety, cold storage, "
            "customer service, and butchery business management."
        ),
        (
            "Work in butcheries, supermarkets, or own butchery. Butchers earn KSh 18,000-35,000 monthly. Own butchery earns KSh 40,000-200,000+ "
            "monthly depending on location. Steady demand for meat products."
        ),
        "6 months",
        "Kenya National Examinations Council (KNEC)"
    ))

    # ELECTRONICS ARTISAN
    programs.append(make_program(
        "Artisan in Mobile Phone Repair",
        level,
        "ICT & Electronics > Phone Repair",
        "D-",
        8,
        [
            "Any subject (Minimum D- / 2 points)"
        ],
        (
            "Training in smartphone hardware repair, screen replacement, battery replacement, software flashing, unlocking, water damage repair, "
            "charging port repair, diagnostics, and phone accessories sales."
        ),
        (
            "Own phone repair shops or work in shops. Repairs: KSh 300-5,000 per phone. Skilled technicians earn KSh 25,000-70,000 monthly. "
            "High demand with smartphone usage. Low capital to start."
        ),
        "3-6 months",
        "Kenya National Examinations Council (KNEC)"
    ))

    programs.append(make_program(
        "Artisan in TV and Electronics Repair",
        level,
        "ICT & Electronics > Electronics Repair",
        "D-",
        8,
        [
            "Mathematics (Minimum D- / 2 points) OR",
            "Physics (Minimum D- / 2 points) OR",
            "Any subject"
        ],
        (
            "Hands-on training in TV repair (LED, LCD, plasma), home theater systems, amplifiers, radio repair, basic electronics, fault "
            "diagnosis, component replacement, soldering, and using testing equipment."
        ),
        (
            "Work as electronics technicians or own repair shops. TV repairs: KSh 1,000-8,000. Skilled technicians earn KSh 20,000-60,000 "
            "monthly. Steady demand for home electronics repairs and maintenance."
        ),
        "6 months",
        "Kenya National Examinations Council (KNEC)"
    ))

    # SECURITY & SAFETY ARTISAN
    programs.append(make_program(
        "Artisan in CCTV Installation and Maintenance",
        level,
        "Security & Technology > CCTV",
        "D-",
        8,
        [
            "Mathematics (Minimum D- / 2 points) OR",
            "Any subject (Minimum D- / 2 points)"
        ],
        (
            "Practical training in CCTV camera installation, DVR/NVR setup, cable running, power supply, network configuration, remote viewing "
            "setup, system maintenance, troubleshooting, and customer service."
        ),
        (
            "Work with security companies or self-employed. Installation jobs: KSh 15,000-80,000 per site. Technicians earn KSh 25,000-70,000 "
            "monthly. Growing security market with increasing CCTV demand for homes and businesses."
        ),
        "3-6 months",
        "Kenya National Examinations Council (KNEC)"
    ))
   
   # ============================================================================
# MAIN EXECUTION AND COORDINATION FUNCTIONS
# ============================================================================

def generate_all_courses() -> List[Dict]:
    """
    Generate complete course database across all qualification levels.
    Returns list of all courses combined.
    """
    all_courses = []
    
    print("🎓 Generating DEGREE programs...")
    all_courses.extend(generate_degree_programs())
    print(f"   ✅ Generated {len([c for c in all_courses if c['level'] == 'Degree'])} degree programs")
    
    print("📜 Generating DIPLOMA programs...")
    all_courses.extend(generate_diploma_programs())
    print(f"   ✅ Generated {len([c for c in all_courses if c['level'] == 'Diploma'])} diploma programs")
    
    print("📋 Generating CERTIFICATE programs...")
    all_courses.extend(generate_certificate_programs())
    print(f"   ✅ Generated {len([c for c in all_courses if c['level'] == 'Certificate'])} certificate programs")
    
    print("🔧 Generating ARTISAN programs...")
    all_courses.extend(generate_artisan_programs())
    print(f"   ✅ Generated {len([c for c in all_courses if c['level'] == 'Artisan'])} artisan programs")
    
    return all_courses


def get_database_statistics(courses: List[Dict]) -> Dict:
    """Generate statistics about the course database."""
    stats = {
        "total_courses": len(courses),
        "by_level": {},
        "by_path": {},
        "by_exam_body": {},
        "by_duration": {}
    }
    
    # Count by level
    for course in courses:
        level = course["level"]
        path = course["path"]
        exam_body = course["exam_body"]
        duration = course["duration"]
        
        stats["by_level"][level] = stats["by_level"].get(level, 0) + 1
        stats["by_path"][path] = stats["by_path"].get(path, 0) + 1
        stats["by_exam_body"][exam_body] = stats["by_exam_body"].get(exam_body, 0) + 1
        stats["by_duration"][duration] = stats["by_duration"].get(duration, 0) + 1
    
    return stats


def print_statistics(stats: Dict):
    """Print formatted database statistics."""
    print("\n" + "="*70)
    print("📊 KENYA COURSES DATABASE STATISTICS")
    print("="*70)
    print(f"\n✅ Total Courses: {stats['total_courses']}")
    
    print("\n📚 By Qualification Level:")
    level_order = ["Degree", "Diploma", "Certificate", "Artisan"]
    for level in level_order:
        count = stats['by_level'].get(level, 0)
        if count > 0:
            print(f"   • {level}: {count} programs")
    
    print("\n🎯 Top 10 Career Paths:")
    sorted_paths = sorted(stats['by_path'].items(), key=lambda x: x[1], reverse=True)[:10]
    for path, count in sorted_paths:
        print(f"   • {path}: {count} programs")
    
    print("\n🏛️  By Examination Body:")
    for body, count in sorted(stats['by_exam_body'].items()):
        print(f"   • {body}: {count} programs")
    
    print("="*70 + "\n")


def validate_database(courses: List[Dict]) -> bool:
    """
    Validate database integrity.
    Returns True if all validations pass, False otherwise.
    """
    print("\n🔍 Validating database integrity...")
    
    required_fields = [
        "program_name", "level", "path", "min_mean_grade",
        "min_cluster_points", "subject_requirements", "description",
        "career_path", "duration", "exam_body", "metadata"
    ]
    
    valid_levels = ["Degree", "Diploma", "Certificate", "Artisan"]
    errors = []
    warnings = []
    
    for idx, course in enumerate(courses):
        # Check required fields
        missing = [f for f in required_fields if f not in course]
        if missing:
            errors.append(f"Course #{idx+1} ({course.get('program_name', 'Unknown')}) missing fields: {missing}")
        
        # Validate level
        if course.get("level") not in valid_levels:
            errors.append(f"Course #{idx+1} has invalid level: {course.get('level')}")
        
        # Validate cluster points against level minimums
        level_min_points = {
            "Degree": 7, "Diploma": 5, "Certificate": 4, "Artisan": 2
        }
        level = course.get("level")
        points = course.get("min_cluster_points", 0)
        expected_min = level_min_points.get(level, 0)
        
        if points < expected_min:
            errors.append(
                f"Course #{idx+1} ({course.get('program_name')}) has insufficient "
                f"cluster points ({points}) for {level} (minimum: {expected_min})"
            )
        
        # Check for empty descriptions or career paths
        if len(course.get("description", "").strip()) < 100:
            warnings.append(f"Course #{idx+1} ({course.get('program_name')}) has short description")
        
        if len(course.get("career_path", "").strip()) < 100:
            warnings.append(f"Course #{idx+1} ({course.get('program_name')}) has short career path")
    
    if errors:
        print("❌ Validation FAILED:")
        for error in errors[:10]:  # Show first 10 errors
            print(f"   • {error}")
        if len(errors) > 10:
            print(f"   ... and {len(errors)-10} more errors")
        return False
    
    if warnings:
        print("⚠️  Warnings found:")
        for warning in warnings[:5]:  # Show first 5 warnings
            print(f"   • {warning}")
        if len(warnings) > 5:
            print(f"   ... and {len(warnings)-5} more warnings")
    
    print("✅ Validation PASSED - Database is valid!")
    return True


def export_by_level(courses: List[Dict], output_dir: str = "exports"):
    """Export courses to separate files by qualification level."""
    os.makedirs(output_dir, exist_ok=True)
    
    by_level = {}
    for course in courses:
        level = course["level"]
        if level not in by_level:
            by_level[level] = []
        by_level[level].append(course)
    
    print("\n📤 Exporting by level:")
    for level, level_courses in sorted(by_level.items()):
        filename = os.path.join(output_dir, f"{level.lower()}_courses.json")
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(level_courses, f, ensure_ascii=False, indent=2)
        print(f"   ✅ {level}: {len(level_courses)} courses → {filename}")


def export_by_path(courses: List[Dict], output_dir: str = "exports"):
    """Export courses to separate files by career path."""
    os.makedirs(output_dir, exist_ok=True)
    
    by_path = {}
    for course in courses:
        # Get the main path (first part before >)
        path = course["path"].split(">")[0].strip()
        if path not in by_path:
            by_path[path] = []
        by_path[path].append(course)
    
    print("\n📤 Exporting by career path:")
    exported_count = 0
    for path, path_courses in sorted(by_path.items()):
        safe_path = path.replace("/", "_").replace(" ", "_").lower()
        safe_path = "".join(c for c in safe_path if c.isalnum() or c == "_")
        filename = os.path.join(output_dir, f"path_{safe_path}.json")
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(path_courses, f, ensure_ascii=False, indent=2)
        if exported_count < 10:  # Show first 10
            print(f"   ✅ {path}: {len(path_courses)} courses → {filename}")
        exported_count += 1
    
    if exported_count > 10:
        print(f"   ... and {exported_count - 10} more path files")


def export_summary_report(courses: List[Dict], stats: Dict, output_dir: str = "exports"):
    """Export a summary report in text format."""
    os.makedirs(output_dir, exist_ok=True)
    
    report_file = os.path.join(output_dir, "database_summary.txt")
    
    with open(report_file, "w", encoding="utf-8") as f:
        f.write("="*70 + "\n")
        f.write("KENYA COMPREHENSIVE COURSES DATABASE - SUMMARY REPORT\n")
        f.write("="*70 + "\n\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        f.write(f"Total Courses: {stats['total_courses']}\n\n")
        
        f.write("BY QUALIFICATION LEVEL:\n")
        f.write("-" * 40 + "\n")
        for level in ["Degree", "Diploma", "Certificate", "Artisan"]:
            count = stats['by_level'].get(level, 0)
            percentage = (count / stats['total_courses'] * 100) if stats['total_courses'] > 0 else 0
            f.write(f"  {level:12s}: {count:4d} ({percentage:5.1f}%)\n")
        
        f.write("\n\nTOP CAREER PATHS:\n")
        f.write("-" * 40 + "\n")
        sorted_paths = sorted(stats['by_path'].items(), key=lambda x: x[1], reverse=True)[:15]
        for idx, (path, count) in enumerate(sorted_paths, 1):
            f.write(f"  {idx:2d}. {path:30s}: {count:3d} programs\n")
        
        f.write("\n\nEXAMINATION BODIES:\n")
        f.write("-" * 40 + "\n")
        for body, count in sorted(stats['by_exam_body'].items(), key=lambda x: x[1], reverse=True):
            f.write(f"  • {body}: {count} programs\n")
        
        f.write("\n" + "="*70 + "\n")
    
    print(f"   ✅ Summary report → {report_file}")


def main():
    """Main execution function."""
    print("\n" + "="*70)
    print("🇰🇪  KENYA COMPREHENSIVE COURSES DATABASE GENERATOR")
    print("="*70)
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Load existing database
    print("📂 Loading existing database...")
    existing_courses = load_db(DB_FILENAME)
    print(f"   Found {len(existing_courses)} existing courses\n")
    
    # Generate new courses
    print("🔄 Generating course database...\n")
    new_courses = generate_all_courses()
    
    # Merge and deduplicate
    print(f"\n🔗 Merging databases...")
    all_courses = deduplicate(existing_courses, new_courses)
    print(f"   Total unique courses: {len(all_courses)}")
    
    # Validate
    if not validate_database(all_courses):
        print("\n⚠️  Warning: Database contains validation errors!")
        response = input("Continue saving? (y/n): ")
        if response.lower() != 'y':
            print("❌ Aborted. Database not saved.")
            return
    
    # Save main database
    print(f"\n💾 Saving to {DB_FILENAME}...")
    save_db(all_courses, DB_FILENAME)
    print(f"   ✅ Saved successfully!")
    
    # Generate statistics
    stats = get_database_statistics(all_courses)
    print_statistics(stats)
    
    # Export categorized files
    print("📤 Exporting categorized files...")
    export_by_level(all_courses)
    export_by_path(all_courses)
    export_summary_report(all_courses, stats)
    
    print("\n" + "="*70)
    print("✨ DATABASE GENERATION COMPLETE!")
    print("="*70)
    print(f"Completed: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    print(f"📁 Main database: {DB_FILENAME}")
    print(f"📁 Exports folder: exports/")
    print(f"📁 Total courses: {len(all_courses)}")
    print("\n💡 Use this database for:")
    print("   • Course recommendation systems")
    print("   • Student guidance platforms")
    print("   • Educational institution APIs")
    print("   • Career planning applications")
    print("   • KCSE results analysis tools\n")


# ============================================================================
# SCRIPT ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Process interrupted by user")
        print("❌ Database generation cancelled\n")
    except Exception as e:
        print(f"\n\n❌ ERROR: {str(e)}")
        print("Database generation failed\n")
        import traceback
        traceback.print_exc()
        raise
 
   