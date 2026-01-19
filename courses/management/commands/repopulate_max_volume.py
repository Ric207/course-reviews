from django.core.management.base import BaseCommand
from courses.models import Course
import random
from django.db import transaction

class Command(BaseCommand):
    help = "Generates comprehensive unique courses - NO DUPLICATES"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("Clearing existing courses..."))
        Course.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("✓ Database cleared"))

        # Track all unique course names
        all_courses = {}  # Use dict to prevent any duplicates
        
        # Core Majors by Field
        MAJORS = {
            'Medicine': ['Nursing', 'Pharmacy', 'Clinical Medicine', 'Dental Surgery', 'Public Health', 
                        'Nutrition', 'Radiography', 'Medical Laboratory', 'Physiotherapy', 'Occupational Therapy', 
                        'Community Health', 'Health Records', 'Medical Engineering', 'Optometry', 'Epidemiology', 
                        'Health Systems Management', 'Mortuary Science', 'Medical Psychology'],
            'Engineering': ['Civil Engineering', 'Electrical Engineering', 'Mechanical Engineering', 'Automotive Engineering', 
                           'Mechatronic Engineering', 'Geospatial Engineering', 'Petroleum Engineering', 'Aerospace Engineering', 
                           'Agricultural Engineering', 'Water Engineering', 'Structural Engineering', 'Telecommunications Engineering', 
                           'Biomedical Engineering', 'Marine Engineering', 'Mining Engineering', 'Instrumentation Engineering', 
                           'Chemical Engineering', 'Industrial Engineering', 'Software Engineering', 'Environmental Engineering', 
                           'Textile Engineering'],
            'ICT': ['Computer Science', 'Information Technology', 'Cyber Security', 'Data Science', 
                   'Business Information Technology', 'Web Development', 'Network Administration', 
                   'Computer Technology', 'Applied Computer Science', 'Informatics', 'Library and Information Science'],
            'Business': ['Commerce', 'Economics', 'Accounting', 'Finance', 'Marketing', 'Human Resource Management', 
                        'Supply Chain Management', 'Procurement', 'Entrepreneurship', 'Project Management', 
                        'Business Administration', 'Office Management', 'International Business', 'Real Estate Management', 
                        'Insurance', 'Banking and Finance', 'Cooperative Management', 'Strategic Management'],
            'Education': ['Education Science', 'Education Arts', 'Early Childhood Development', 'Special Needs Education', 
                         'Primary Education', 'Guidance and Counseling', 'Agricultural Education', 'Physical Education'],
            'Agriculture': ['Agriculture', 'Agribusiness', 'Horticulture', 'Animal Health', 'Food Science and Technology', 
                           'Dairy Technology', 'Soil Science', 'Forestry', 'Fisheries', 'Range Management', 
                           'Wildlife Management', 'Dryland Agriculture'],
            'Hospitality': ['Hospitality Management', 'Tourism Management', 'Catering and Accommodation', 'Food and Beverage Management', 
                           'Tour Guiding', 'Travel and Tour Operations', 'Event Management', 'Hotel Management', 'Ecotourism'],
            'Arts': ['International Relations', 'Journalism', 'Mass Communication', 'Public Relations', 
                    'Social Work', 'Psychology', 'Community Development', 'Fashion Design', 'Interior Design', 
                    'Music', 'Fine Arts', 'Criminology', 'Security Studies', 'Political Science', 'Sociology', 
                    'Gender Studies', 'History', 'Anthropology', 'Philosophy', 'Literature'],
            'Science': ['Biochemistry', 'Microbiology', 'Biotechnology', 'Actuarial Science', 'Statistics', 
                       'Mathematics', 'Physics', 'Chemistry', 'Biology', 'Geology', 'Meteorology', 
                       'Environmental Science', 'Industrial Chemistry', 'Analytical Chemistry', 'Botany', 'Zoology']
        }

        # Complete Program Descriptions
        DESCRIPTIONS = {
            'Nursing': "Comprehensive healthcare program covering patient care, clinical procedures, pharmacology, and community health. Combines theoretical knowledge with extensive clinical practice in hospitals and healthcare facilities preparing graduates for diverse nursing roles.",
            'Pharmacy': "Rigorous pharmaceutical sciences program focusing on drug formulation, dispensing, pharmacology, medicinal chemistry, and patient counseling. Graduates work in retail, hospital, industrial, and regulatory pharmacy settings ensuring safe medication management.",
            'Clinical Medicine': "Intensive medical program training clinical officers to diagnose, treat, and manage common diseases. Emphasizes primary healthcare, emergency medicine, surgery assistance, and community health serving as frontline healthcare providers.",
            'Dental Surgery': "Specialized dental program covering oral health, dental procedures, oral surgery, orthodontics, and preventive dentistry. Combines classroom learning with extensive clinical practice preparing graduates for dental practice.",
            'Public Health': "Population-focused program addressing disease prevention, health promotion, epidemiology, environmental health, and health systems management. Graduates work with government agencies, NGOs tackling public health challenges.",
            'Nutrition': "Science-based program exploring human nutrition, dietetics, food safety, clinical nutrition, and community nutrition interventions. Graduates advise on dietary management promoting healthy eating practices across communities.",
            'Radiography': "Medical imaging program training professionals in X-ray, CT, MRI, ultrasound, and radiation therapy techniques. Combines physics principles with clinical application for diagnostic and therapeutic radiography roles.",
            'Medical Laboratory': "Laboratory sciences program covering clinical chemistry, microbiology, hematology, immunology, and molecular diagnostics. Graduates analyze patient samples, detect diseases supporting clinical decision-making.",
            'Physiotherapy': "Rehabilitation-focused program teaching movement assessment, therapeutic exercise, manual therapy, and electrotherapy for injury recovery and disability management helping patients restore optimal physical function.",
            'Occupational Therapy': "Holistic program enabling individuals with physical, mental, or developmental conditions to participate in daily activities through therapeutic techniques and adaptive equipment.",
            'Community Health': "Grassroots-focused program preparing community health workers to deliver primary healthcare, health education, disease surveillance, and health promotion at village levels.",
            'Health Records': "Health informatics program covering medical records management, health information systems, coding, data privacy, and healthcare statistics supporting healthcare administration.",
            'Medical Engineering': "Interdisciplinary program combining medicine and engineering to design, maintain, and manage medical equipment and healthcare technology ensuring safe effective use.",
            'Optometry': "Eye care program focusing on vision examination, prescription of corrective lenses, detection of eye diseases, and vision therapy improving visual health and quality of life.",
            'Epidemiology': "Disease investigation program studying patterns, causes, and effects of health conditions in populations conducting outbreak investigations and informing public health policies.",
            'Health Systems Management': "Healthcare administration program covering health policy, hospital management, healthcare financing, quality assurance, and leadership preparing graduates for managerial roles.",
            'Mortuary Science': "Specialized program in embalming, body preservation, funeral management, grief counseling, and mortuary operations providing dignified end-of-life services.",
            'Medical Psychology': "Clinical psychology program focusing on mental health assessment, psychotherapy, counseling, and behavioral interventions supporting patients coping with illness and psychological disorders.",
            
            'Civil Engineering': "Comprehensive engineering program covering structural design, construction management, hydraulics, transportation systems, and geotechnical engineering. Graduates design infrastructure projects including roads, bridges, buildings shaping national growth.",
            'Electrical Engineering': "Power and electronics-focused program teaching electrical systems design, power generation and distribution, electronics, control systems, and instrumentation driving technological advancement.",
            'Mechanical Engineering': "Versatile engineering program covering thermodynamics, mechanics, manufacturing processes, machine design, and automotive systems. Graduates design analyze and maintain mechanical systems.",
            'Automotive Engineering': "Specialized program in vehicle design, engines, transmission systems, vehicle electronics, and automotive diagnostics serving Kenya's growing transport sector.",
            'Mechatronic Engineering': "Integrated program combining mechanical, electrical, and computer engineering to design intelligent systems and robotics for Industry 4.0.",
            'Geospatial Engineering': "Geomatics program covering surveying, GIS, remote sensing, cartography, and spatial data analysis supporting urban planning and infrastructure development.",
            'Petroleum Engineering': "Oil and gas engineering program focusing on exploration, drilling, production, and reservoir management ensuring efficient petroleum resource extraction.",
            'Aerospace Engineering': "Aviation-focused program covering aircraft design, propulsion systems, aerodynamics, and avionics supporting Kenya's aviation industry.",
            'Agricultural Engineering': "Engineering program applying technology to farming systems, irrigation, mechanization, processing, and post-harvest management modernizing agriculture.",
            'Water Engineering': "Hydraulic engineering program specializing in water supply systems, wastewater treatment, irrigation, drainage, and water resources management.",
            'Structural Engineering': "Specialized program in structural analysis, design of buildings and bridges, earthquake engineering, and construction materials ensuring structural safety.",
            'Telecommunications Engineering': "ICT infrastructure program covering wireless networks, fiber optics, satellite communication, signal processing, and network design enabling digital connectivity.",
            'Biomedical Engineering': "Healthcare technology program combining engineering with medicine to design medical devices, diagnostic equipment, and prosthetics improving patient care.",
            'Marine Engineering': "Maritime engineering program covering ship design, marine propulsion, offshore structures, and naval architecture supporting maritime operations.",
            'Mining Engineering': "Mineral extraction program teaching mining methods, mineral processing, mine safety, and environmental management ensuring sustainable mineral exploitation.",
            'Instrumentation Engineering': "Control systems program focusing on sensors, measurement systems, process control, and automation ensuring precision and efficiency.",
            'Chemical Engineering': "Process engineering program covering chemical reactions, plant design, process safety, and industrial chemistry developing products and optimizing processes.",
            'Industrial Engineering': "Manufacturing-focused program teaching production systems, quality management, supply chain optimization, and operations research improving organizational efficiency.",
            'Software Engineering': "Software development program covering programming, software architecture, databases, and systems analysis driving digital transformation.",
            'Environmental Engineering': "Sustainability-focused program addressing pollution control, waste management, environmental impact assessment, and sustainable development promoting environmental conservation.",
            'Textile Engineering': "Fabric technology program covering textile manufacturing, garment production, fabric design, and quality control ensuring competitive textile products.",
            
            'Computer Science': "Foundational computing program covering algorithms, programming languages, software development, artificial intelligence, and computer systems solving complex computational problems.",
            'Information Technology': "IT systems program focusing on network administration, database management, cybersecurity, cloud computing, and IT service management supporting business operations.",
            'Cyber Security': "Information security program covering ethical hacking, network security, cryptography, incident response, and security auditing protecting organizations from cyber threats.",
            'Data Science': "Analytics-focused program teaching statistical analysis, machine learning, data visualization, big data technologies, and predictive modeling extracting insights from data.",
            'Business Information Technology': "Business-aligned IT program bridging technology and management covering business analysis, ERP systems, and e-commerce aligning technology with business objectives.",
            'Web Development': "Internet technologies program covering front-end and back-end development, responsive design, content management systems, and web security creating dynamic web applications.",
            'Network Administration': "IT infrastructure program focusing on network design, server management, network security, troubleshooting, and system administration maintaining reliable network operations.",
            'Computer Technology': "Hardware-focused program covering computer repair, hardware troubleshooting, system assembly, and technical support providing hands-on technical services.",
            'Applied Computer Science': "Practical computing program applying technology to solve real-world problems across healthcare, finance, education, and governance domains.",
            'Informatics': "Information systems program studying how people interact with technology, information management, and digital systems designing user-centered information systems.",
            'Library and Information Science': "Information management program covering library systems, digital archives, information retrieval, and knowledge management supporting education and research.",
            
            'Commerce': "Comprehensive business program covering trade, finance, marketing, business law, and entrepreneurship preparing graduates for diverse business careers.",
            'Economics': "Economic theory and policy program analyzing resource allocation, market systems, development economics, and econometrics. Graduates work in policy analysis and financial organizations.",
            'Accounting': "Financial reporting program teaching bookkeeping, auditing, taxation, financial management, and accounting standards ensuring accurate financial records and compliance.",
            'Finance': "Investment and corporate finance program covering financial markets, portfolio management, risk management, and financial planning managing money and investments.",
            'Marketing': "Customer-focused program teaching market research, brand management, digital marketing, consumer behavior, and sales strategy creating value and driving growth.",
            'Human Resource Management': "People management program covering recruitment, talent development, employee relations, compensation, and organizational behavior managing workforce planning.",
            'Supply Chain Management': "Logistics program focusing on procurement, inventory management, distribution, supply chain analytics, and operations optimizing flow of goods.",
            'Procurement': "Strategic sourcing program teaching supplier management, contract negotiation, procurement law, ethics, and spend analysis ensuring quality acquisition.",
            'Entrepreneurship': "Business creation program fostering innovation, opportunity identification, business planning, startup financing, and venture management driving economic growth.",
            'Project Management': "Project delivery program covering planning, scheduling, budgeting, risk management, and stakeholder engagement ensuring timely project delivery.",
            'Business Administration': "General management program teaching leadership, strategic planning, organizational management, and business decision-making driving organizational success.",
            'Office Management': "Administrative program covering office procedures, records management, business communication, and secretarial skills supporting smooth office operations.",
            'International Business': "Global trade program covering export-import procedures, international marketing, cross-cultural management, and global supply chains facilitating international trade.",
            'Real Estate Management': "Property management program teaching real estate law, property valuation, investment analysis, and facility management. Graduates work in property development.",
            'Insurance': "Risk management program covering underwriting, claims management, actuarial principles, and insurance regulations assessing risks and managing claims.",
            'Banking and Finance': "Financial services program teaching banking operations, credit analysis, retail banking, investment banking, and financial regulations.",
            'Cooperative Management': "Cooperative societies program covering cooperative principles, member services, governance, and cooperative finance promoting financial inclusion.",
            'Strategic Management': "Leadership program focusing on corporate strategy, competitive analysis, change management, and performance management positioning organizations for success.",
            
            'Education Science': "Teacher training program preparing educators to teach science subjects including Biology, Chemistry, Physics, and Mathematics combining subject mastery with pedagogy.",
            'Education Arts': "Teacher training program for humanities and languages including English, Kiswahili, History, CRE, Geography, and Business Studies inspiring critical thinking.",
            'Early Childhood Development': "Child development program focusing on early learning pedagogy, child psychology, play-based learning, and holistic development laying educational foundations.",
            'Special Needs Education': "Inclusive education program teaching special education pedagogy, disability assessment, individualized education plans, and adaptive technologies.",
            'Primary Education': "Elementary teaching program preparing teachers for primary school instruction across curriculum areas for Grades 1-6.",
            'Guidance and Counseling': "Student support program teaching counseling theories, career guidance, psychological assessment, and crisis intervention supporting student development.",
            'Agricultural Education': "Vocational teaching program combining agriculture and education to train agricultural instructors in technical institutions promoting agricultural knowledge.",
            'Physical Education': "Sports and health program teaching physical activity pedagogy, sports coaching, sports psychology, and health education promoting physical fitness.",
            
            'Agriculture': "Comprehensive farming program covering crop production, animal husbandry, soil management, agricultural economics, and farm management improving food production.",
            'Agribusiness': "Agricultural entrepreneurship program linking farming with business covering value addition, agricultural marketing, and supply chains commercializing agriculture.",
            'Horticulture': "Crop sciences program specializing in fruits, vegetables, flowers production with greenhouse management and irrigation boosting horticultural exports.",
            'Animal Health': "Veterinary program training animal health technicians in disease diagnosis, treatment, vaccination, and livestock management supporting livestock productivity.",
            'Food Science and Technology': "Food technology program covering food processing, preservation, quality control, nutrition, and food safety ensuring safe nutritious food supply.",
            'Dairy Technology': "Specialized program in dairy farming, milk processing, dairy products manufacturing, and dairy business management supporting Kenya's dairy industry.",
            'Soil Science': "Land resources program studying soil fertility, soil conservation, land use planning, and sustainable agriculture promoting sustainable land use.",
            'Forestry': "Natural resources program covering forest management, tree nurseries, agroforestry, forest conservation, and wood technology ensuring sustainable forestry.",
            'Fisheries': "Aquatic resources program teaching fish farming, fisheries management, aquaculture systems, and fish processing boosting fish production.",
            'Range Management': "Rangeland program focusing on pasture management, livestock grazing systems, wildlife conservation, and arid lands development.",
            'Wildlife Management': "Conservation program covering wildlife ecology, protected area management, human-wildlife conflict, and eco-tourism protecting biodiversity.",
            'Dryland Agriculture': "Arid lands program teaching drought-resistant crops, water harvesting, soil conservation, and climate-smart agriculture addressing food security.",
            
            'Hospitality Management': "Hotel operations program covering front office, housekeeping, food and beverage services, hospitality marketing, and quality service delivering exceptional guest experiences.",
            'Tourism Management': "Tourism industry program teaching tour operations, destination marketing, tourism planning, and customer service promoting tourism attractions.",
            'Catering and Accommodation': "Food service program covering culinary arts, menu planning, kitchen management, food safety, and event catering.",
            'Food and Beverage Management': "Restaurant service program teaching table service, bar operations, beverage management, and customer relations providing professional service.",
            'Tour Guiding': "Tourism interpretation program covering tour guiding techniques, destination knowledge, cultural heritage, and customer engagement creating memorable experiences.",
            'Travel and Tour Operations': "Travel industry program teaching ticketing, travel documentation, tour packaging, and travel agency operations facilitating travel arrangements.",
            'Event Management': "Event planning program covering conference organization, wedding planning, exhibitions, logistics, and event marketing planning successful events.",
            'Hotel Management': "Accommodation management program focusing on hotel operations, guest services, revenue management, and hospitality leadership ensuring quality operations.",
            'Ecotourism': "Sustainable tourism program combining conservation and tourism teaching responsible travel and community tourism supporting conservation.",
            
            'International Relations': "Global affairs program studying diplomacy, international organizations, foreign policy, conflict resolution, and global governance navigating global dynamics.",
            'Journalism': "News reporting program teaching news writing, investigative journalism, media law, ethics, and digital journalism informing and engaging audiences.",
            'Mass Communication': "Media studies program covering broadcasting, public communication, media production, and communication theory shaping public discourse.",
            'Public Relations': "Strategic communication program teaching corporate communication, crisis management, media relations, and reputation management building positive relationships.",
            'Social Work': "Community welfare program teaching social work practice, counseling, community development, and vulnerable populations support promoting social justice.",
            'Psychology': "Behavioral sciences program studying human behavior, mental processes, psychological assessment, and counseling supporting psychological wellbeing.",
            'Community Development': "Grassroots program teaching participatory development, project management, social mobilization, and community empowerment driving inclusive development.",
            'Fashion Design': "Creative program covering garment design, pattern making, textile selection, fashion illustration, and fashion marketing in Kenya's fashion industry.",
            'Interior Design': "Spatial design program teaching interior decoration, space planning, color theory, furniture design, and sustainable interiors designing beautiful spaces.",
            'Music': "Performing arts program covering music theory, composition, performance, music production, and music education contributing to Kenya's music scene.",
            'Fine Arts': "Visual arts program teaching painting, sculpture, printmaking, art history, and visual communication contributing to cultural expression.",
            'Criminology': "Criminal justice program studying crime causation, criminal law, corrections, policing, and crime prevention promoting safety and justice.",
            'Security Studies': "Security management program covering risk assessment, security operations, intelligence, emergency management, and corporate security ensuring safety.",
            'Political Science': "Governance program analyzing political systems, public policy, political theory, and electoral systems shaping political discourse and governance.",
            'Sociology': "Social structures program studying society, social change, inequality, family, and institutions conducting social research.",
            'Gender Studies': "Social equity program focusing on gender relations, women's empowerment, gender policy, and social justice advocating for gender equality.",
            'History': "Historical analysis program studying past events, historiography, heritage conservation, and historical research methods preserving cultural heritage.",
            'Anthropology': "Human cultures program studying cultural diversity, ethnography, human evolution, and social organization promoting cultural understanding.",
            'Philosophy': "Critical thinking program exploring ethics, logic, metaphysics, and philosophical traditions developing analytical skills.",
            'Literature': "Literary studies program analyzing poetry, prose, drama, literary theory, and creative writing promoting literacy and cultural appreciation.",
            
            'Biochemistry': "Molecular sciences program studying chemical processes in living organisms, enzyme kinetics, metabolism, and molecular biology conducting biochemical analysis.",
            'Microbiology': "Microorganisms program covering bacteriology, virology, mycology, immunology, and medical microbiology detecting pathogens.",
            'Biotechnology': "Applied biology program using living organisms for technological applications including genetic engineering and bioprocessing innovating in agriculture and medicine.",
            'Actuarial Science': "Risk quantification program combining mathematics, statistics, finance, and economics to assess financial risks designing financial products.",
            'Statistics': "Data analysis program teaching statistical theory, survey design, probability, computational statistics, and data visualization supporting evidence-based decisions.",
            'Mathematics': "Pure and applied mathematics program covering calculus, algebra, analysis, numerical methods, and mathematical modeling solving quantitative problems.",
            'Physics': "Physical sciences program studying mechanics, electromagnetism, thermodynamics, quantum physics, and astrophysics applying physics principles.",
            'Chemistry': "Chemical sciences program covering organic, inorganic, physical, and analytical chemistry conducting chemical analysis and synthesis.",
            'Biology': "Life sciences program studying organisms, ecology, genetics, evolution, and physiology understanding and protecting living systems.",
            'Geology': "Earth sciences program studying rocks, minerals, earth processes, natural resources, and geological mapping managing earth resources.",
            'Meteorology': "Atmospheric sciences program covering weather forecasting, climate science, atmospheric physics, and climatology providing weather information.",
            'Environmental Science': "Ecosystem management program studying environmental chemistry, ecology, pollution control, and environmental policy promoting environmental stewardship.",
            'Industrial Chemistry': "Applied chemistry program focusing on chemical manufacturing, process chemistry, industrial catalysis, and chemical plant operations.",
            'Analytical Chemistry': "Laboratory analysis program teaching instrumental methods, quality assurance, chemical analysis techniques, and validation ensuring product quality.",
            'Botany': "Plant sciences program studying plant physiology, taxonomy, ecology, plant pathology, and ethnobotany advancing plant knowledge.",
            'Zoology': "Animal sciences program covering animal physiology, taxonomy, ecology, animal behavior, and wildlife biology advancing animal science.",
        }

        # Subject Requirements Templates
        REQUIREMENTS = {
            'Medicine': {
                'Degree': "KCSE mean grade {grade} with minimum B+ in Biology, Chemistry, and either Physics or Mathematics. English/Kiswahili C+.",
                'Diploma': "KCSE mean grade {grade} with minimum C in Biology and Chemistry, C- in English/Kiswahili.",
                'Certificate': "KCSE mean grade {grade} with minimum D+ in Biology, Chemistry, and English/Kiswahili.",
                'Artisan': "KCSE mean grade {grade} with basic literacy and healthcare interest."
            },
            'Engineering': {
                'Degree': "KCSE mean grade {grade} with minimum B in Mathematics and Physics, C+ in English/Kiswahili.",
                'Diploma': "KCSE mean grade {grade} with minimum C- in Mathematics, Physics, and English/Kiswahili.",
                'Certificate': "KCSE mean grade {grade} with minimum D in Mathematics, Physics, and English/Kiswahili.",
                'Artisan': "KCSE mean grade {grade} with minimum D- in Mathematics and English."
            },
            'ICT': {
                'Degree': "KCSE mean grade {grade} with minimum B in Mathematics, C+ in English/Kiswahili.",
                'Diploma': "KCSE mean grade {grade} with minimum C- in Mathematics and English/Kiswahili.",
                'Certificate': "KCSE mean grade {grade} with minimum D in Mathematics and English/Kiswahili.",
                'Artisan': "KCSE mean grade {grade} with basic computer literacy."
            },
            'Business': {
                'Degree': "KCSE mean grade {grade} with minimum C+ in Mathematics and English/Kiswahili.",
                'Diploma': "KCSE mean grade {grade} with minimum C- in Mathematics and English/Kiswahili.",
                'Certificate': "KCSE mean grade {grade} with minimum D in Mathematics and English/Kiswahili.",
                'Artisan': "KCSE mean grade {grade} with functional literacy and numeracy."
            },
            'Education': {
                'Degree': "KCSE mean grade {grade} with minimum C+ in two teaching subjects and English/Kiswahili.",
                'Diploma': "KCSE mean grade {grade} with minimum C- in teaching subjects and English/Kiswahili.",
                'Certificate': "KCSE mean grade {grade} with minimum D+ in relevant subjects.",
                'Artisan': "Not applicable."
            },
            'Agriculture': {
                'Degree': "KCSE mean grade {grade} with minimum C+ in Agriculture/Biology, C in Mathematics, C+ in English/Kiswahili.",
                'Diploma': "KCSE mean grade {grade} with minimum C- in Agriculture/Biology and English/Kiswahili.",
                'Certificate': "KCSE mean grade {grade} with minimum D in Agriculture/Biology and English/Kiswahili.",
                'Artisan': "KCSE mean grade {grade} with practical agricultural skills."
            },
            'Hospitality': {
                'Degree': "KCSE mean grade {grade} with minimum C+ in English/Kiswahili, C in Mathematics.",
                'Diploma': "KCSE mean grade {grade} with minimum C- in English/Kiswahili and Mathematics.",
                'Certificate': "KCSE mean grade {grade} with minimum D in English/Kiswahili and Mathematics.",
                'Artisan': "KCSE mean grade {grade} with functional English and hospitality interest."
            },
            'Arts': {
                'Degree': "KCSE mean grade {grade} with minimum C+ in English/Kiswahili and relevant humanities subjects.",
                'Diploma': "KCSE mean grade {grade} with minimum C- in English/Kiswahili and one humanities subject.",
                'Certificate': "KCSE mean grade {grade} with minimum D+ in English/Kiswahili.",
                'Artisan': "KCSE mean grade {grade} with creative or technical skills."
            },
            'Science': {
                'Degree': "KCSE mean grade {grade} with minimum B in two science subjects, B- in Mathematics, C+ in English/Kiswahili.",
                'Diploma': "KCSE mean grade {grade} with minimum C in two science subjects, C- in Mathematics and English/Kiswahili.",
                'Certificate': "KCSE mean grade {grade} with minimum D+ in science subjects and Mathematics.",
                'Artisan': "Not applicable."
            }
        }

        # Career paths
        CAREERS = {
            'Nursing': "Entry: Staff Nurse → Mid: Senior Nurse/Ward In-charge → Senior: Nursing Officer/Matron → Advanced: Chief Nursing Officer/Director of Nursing. NCK registration required.",
            'Civil Engineering': "Entry: Graduate Engineer → Mid: Project Engineer → Senior: Project Manager/Chief Engineer → Advanced: Principal Engineer/Director. EBK registration required.",
            'Computer Science': "Entry: Junior Developer → Mid: Software Engineer → Senior: Senior Developer/Team Lead → Advanced: CTO/IT Director/Consultant.",
            'Accounting': "Entry: Junior Accountant → Mid: Accountant → Senior: Finance Manager → Advanced: CFO/Finance Director. CPA-K enhances career progression.",
        }

        def create_course(name, level, field, major):
            """Create a single unique course"""
            # Check if already exists
            if name in all_courses:
                return
            
            # Grade assignments
            if level == 'Degree':
                grade = random.choice(['A', 'A-', 'B+', 'B', 'B-', 'C+'])
                points = {'A': 44, 'A-': 42, 'B+': 38, 'B': 34, 'B-': 30, 'C+': 26}[grade]
            elif level == 'Diploma':
                grade = random.choice(['C', 'C-', 'D+'])
                points = {'C': 20, 'C-': 18, 'D+': 16}[grade]
            elif level == 'Certificate':
                grade = random.choice(['D', 'D-'])
                points = {'D': 14, 'D-': 12}[grade]
            else:  # Artisan
                grade = random.choice(['D-', 'E'])
                points = {'D-': 12, 'E': 0}[grade]
            
            # Get requirements template
            req_template = REQUIREMENTS.get(field, {}).get(level, "KCSE mean grade {grade} with relevant subjects.")
            requirements = req_template.format(grade=grade)
            
            # Get description - use major without "Engineering" suffix for lookup
            desc_key = major.replace(' Engineering', '').replace(' Management', '').replace(' and ', ' ')
            description = DESCRIPTIONS.get(major, DESCRIPTIONS.get(desc_key, 
                f"Comprehensive {level} program in {major} providing theoretical knowledge and practical skills for professional competence in the field."))
            
            # Get career path
            career_key = major.replace(' Engineering', '').replace(' Management', '')
            career = CAREERS.get(major, CAREERS.get(career_key,
                f"Entry: {major} Assistant → Mid: {major} Officer → Senior: Senior {major} Officer/Manager → Advanced: Director/Chief {major} Officer/Consultant."))
            
            # Store in dictionary (prevents duplicates automatically)
            all_courses[name] = {
                'name': name,
                'level': level,
                'path': field,
                'min_mean_grade': grade,
                'min_cluster_points': points,
                'subject_requirements': requirements,
                'description': description,
                'career_path_info': career
            }

        # Generate courses - each major gets ONE of each level
        self.stdout.write("Generating unique courses...")
        
        for field, majors in MAJORS.items():
            for major in majors:
                # ONE Degree per major
                create_course(f"Bachelor of Science in {major}", 'Degree', field, major)
                
                # ONE Diploma per major
                create_course(f"Diploma in {major}", 'Diploma', field, major)
                
                # ONE Certificate per major
                create_course(f"Certificate in {major}", 'Certificate', field, major)
                
                # ONE Artisan (only for applicable fields)
                if field in ['Engineering', 'Hospitality', 'Agriculture', 'ICT']:
                    create_course(f"Artisan Certificate in {major}", 'Artisan', field, major)

        # Convert dictionary to Course objects
        courses_to_create = []
        for course_data in all_courses.values():
            courses_to_create.append(Course(**course_data))

        # Save to database
        total = len(courses_to_create)
        self.stdout.write(f"\nSaving {total} unique courses...")
        
        with transaction.atomic():
            Course.objects.bulk_create(courses_to_create, batch_size=500)
        
        # Show statistics
        level_counts = {}
        for course in courses_to_create:
            level_counts[course.level] = level_counts.get(course.level, 0) + 1
        
        self.stdout.write(self.style.SUCCESS(f"\n{'='*60}"))
        self.stdout.write(self.style.SUCCESS(f"✓ SUCCESS! Created {total} UNIQUE courses"))
        self.stdout.write(self.style.SUCCESS(f"{'='*60}"))
        self.stdout.write("\nBreakdown by Level:")
        for level in ['Degree', 'Diploma', 'Certificate', 'Artisan']:
            if level in level_counts:
                self.stdout.write(f"  • {level}: {level_counts[level]} courses")
        self.stdout.write(self.style.SUCCESS(f"\n✓ Zero duplicates guaranteed!"))
        self.stdout.write(self.style.SUCCESS(f"✓ All programs have complete descriptions"))
        self.stdout.write(self.style.SUCCESS(f"✓ Career paths included\n"))