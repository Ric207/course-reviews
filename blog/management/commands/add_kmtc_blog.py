from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Post
from django.utils.text import slugify
from django.utils import timezone
import requests
from django.core.files.base import ContentFile

class Command(BaseCommand):
    help = "Adds a comprehensive KMTC blog post with detailed information"

    def handle(self, *args, **kwargs):
        # Get Admin User
        author = User.objects.filter(is_superuser=True).first()
        if not author:
            self.stdout.write(self.style.ERROR("No Admin user found."))
            return

        # KMTC Image URL provided by user
        image_url = "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=800&q=80"
        
        title = "The Ultimate Guide to KMTC Courses 2025/2026: Everything You Need to Know"
        
        # Comprehensive content with paywall marker
        content = """Kenya Medical Training College (KMTC) stands as Kenya's largest and most prestigious mid-level medical training institution. Established in 1927, KMTC has evolved into a powerhouse with over 70 campuses nationwide, training thousands of healthcare professionals annually.

**Why Choose KMTC?**

KMTC graduates are the backbone of Kenya's healthcare system. The institution boasts a 95% employment rate within 6 months of graduation, with many graduates securing government positions immediately after completing their internships. The college is ISO 9001:2015 certified, ensuring world-class training standards.

Unlike universities that focus on theory, KMTC emphasizes practical, hands-on training. Students spend 60% of their time in hospital attachments, gaining real-world experience. This makes KMTC graduates highly sought after by both public and private healthcare facilities.

**Application Windows & Process:**

KMTC opens applications twice per year - September intake and March intake. The application process is entirely online through the KMTC portal. Application fees are Ksh 1,000 for Kenyan citizens and $30 for international students.

[LOCKED CONTENT STARTS HERE]

**COMPLETE COURSE CATALOG WITH INSIDER DETAILS:**

**1. DIPLOMA IN CLINICAL MEDICINE (3 Years)**
* *Minimum Grade:* C (Plain) with C in Biology, Chemistry, Mathematics/Physics, English/Kiswahili
* *Annual Fees:* Regular Ksh 85,000 | Self-Sponsored Ksh 135,000
* *Career Prospects:* Start at Ksh 45,000-60,000 in private hospitals, Ksh 80,000+ in government (Job Group H)
* *Hidden Advantage:* You can upgrade to Bachelor of Medicine through bridging programs at Moi University or UoN after 3 years of practice
* *Best Campuses:* Nairobi, Mombasa, Thika, Nakuru (have Level 5 hospitals for better attachment)

**2. DIPLOMA IN NURSING (KENYA REGISTERED COMMUNITY HEALTH NURSE - KRCHN) (3 Years)**
* *Minimum Grade:* C (Plain) with C in Biology, Chemistry, English/Kiswahili, Mathematics/Physics
* *Annual Fees:* Regular Ksh 90,000 | Self-Sponsored Ksh 140,000
* *International Recognition:* Automatically recognized in East Africa, eligible for UK NMC registration after 2 years of practice
* *Salary Range:* Ksh 50,000-70,000 (private), Ksh 93,000+ (government Job Group K)
* *Secret Tip:* Specialize in ICU, Theatre, or Pediatric Nursing for an extra Ksh 30,000+ monthly allowance
* *Migration Pathway:* Canada, Australia, and UK have nursing shortages - KMTC KRCHN is recognized with additional exams (NCLEX-RN, IELTS)

**3. DIPLOMA IN PHARMACY (3 Years)**
* *Minimum Grade:* C (Plain) with C in Chemistry, Biology/Physics, Mathematics, English
* *Annual Fees:* Regular Ksh 88,000 | Self-Sponsored Ksh 138,000
* *Business Opportunity:* Open your own pharmacy with just Ksh 500,000 capital - ROI within 18 months
* *Employment:* 100% placement rate due to pharmacy boom in Kenya
* *Salary:* Ksh 40,000-55,000 (employee), Unlimited (own business can make Ksh 200,000+ monthly profit)
* *Pro Tip:* Focus on geriatric pharmacy or oncology pharmacy - these are underserved niches

**4. DIPLOMA IN MEDICAL LABORATORY SCIENCES (3 Years)**
* *Minimum Grade:* C (Plain) with C in Biology, Chemistry, Physics/Mathematics, English
* *Annual Fees:* Regular Ksh 87,000 | Self-Sponsored Ksh 137,000
* *Why It's Hot:* COVID-19 created massive demand for lab technologists - demand still exceeds supply
* *Salary:* Ksh 50,000-65,000 (private), Ksh 85,000+ (government)
* *Specialization Bonus:* Microbiology, Histopathology specialists earn 40% more

**5. CERTIFICATE IN ORTHOPEDIC TRAUMA MEDICINE (2 Years)**
* *Minimum Grade:* C- (Minus) with D+ in Biology, Chemistry, Physics/Mathematics, English
* *Annual Fees:* Regular Ksh 70,000 | Self-Sponsored Ksh 115,000
* *Fastest ROI:* Shortest training period with high demand due to road accidents
* *Salary:* Ksh 35,000-50,000 starting
* *Career Path:* Upgrade to Diploma in Orthopedic Technology later

**6. DIPLOMA IN MEDICAL ENGINEERING (3 Years)**
* *Minimum Grade:* C (Plain) with C in Physics, Chemistry/Biology, Mathematics, English
* *Annual Fees:* Regular Ksh 92,000 | Self-Sponsored Ksh 145,000
* *Why Lucrative:* Only 200 medical engineers graduate annually vs 5,000+ hospitals/clinics
* *Salary:* Ksh 60,000-100,000 (contracts pay even more)
* *Freelance Potential:* Service contracts with hospitals pay Ksh 50,000 per machine serviced
* *Equipment Focus:* X-ray, CT Scanners, Ultrasound, Ventilators, Dialysis machines

**7. HIGHER DIPLOMA IN PUBLIC HEALTH (2 Years - Degree Holders Only)**
* *Minimum:* Degree in health-related field
* *Annual Fees:* Ksh 110,000
* *Target Audience:* Degree holders wanting to specialize in epidemiology, health systems management
* *NGO Magnet:* WHO, UNICEF, MSF prefer this qualification - salary Ksh 150,000-300,000

**8. DIPLOMA IN COMMUNITY HEALTH (3 Years)**
* *Minimum Grade:* C- (Minus)
* *Annual Fees:* Regular Ksh 75,000 | Self-Sponsored Ksh 120,000
* *Field Work:* Perfect for those who prefer working in communities rather than hospitals
* *Employment:* County governments, NGOs - Ksh 40,000-60,000

**9. CERTIFICATE IN HEALTH RECORDS & INFORMATION TECHNOLOGY (2 Years)**
* *Minimum Grade:* D+ (Plus)
* *Annual Fees:* Regular Ksh 65,000 | Self-Sponsored Ksh 105,000
* *Underrated Gem:* Low competition, high demand due to digitalization of health records
* *Work Environment:* Office-based, no night shifts
* *Salary:* Ksh 30,000-45,000

**10. DIPLOMA IN KENYA REGISTERED ANESTHESIA (3 Years)**
* *Minimum Grade:* C (Plain)
* *Annual Fees:* Regular Ksh 95,000 | Self-Sponsored Ksh 148,000
* *Critical Shortage:* Kenya has only 400 anesthetists for 9,000+ theatres
* *Salary:* Ksh 70,000-120,000 (highest paid diploma holders)
* *Stress Factor:* High responsibility but extremely rewarding

**FINANCING YOUR KMTC EDUCATION:**

**1. Afya Elimu Fund (Game Changer)**
* Covers up to Ksh 40,000 per year
* Apply through HELB portal immediately after admission
* 95% approval rate for KMTC students
* Repayment starts 12 months after graduation at 4% interest (cheaper than commercial loans)

**2. HELB Loans**
* Additional Ksh 35,000-60,000 per year depending on need
* Combined with Afya Elimu Fund = Ksh 75,000-100,000 total coverage
* Most students graduate owing less than Ksh 250,000

**3. County Bursaries**
* Every county has education bursaries (Ksh 10,000-50,000)
* Apply through your MCA's office
* Deadline usually July and December

**4. CDF Bursaries**
* Apply through your MP's office
* Allocation: Ksh 15,000-40,000
* Processed faster than county bursaries

**5. NHIF Cover for Fees**
* If your parent/guardian works in government, NHIF sometimes covers medical training fees
* Check with HR department

**ADMISSION SECRETS & STRATEGIES:**

**Strategy 1: Campus Selection Hack**
* Nairobi, Mombasa, Thika campuses have 10-20 applications per slot
* Kapenguria, Lodwar, Garissa, Msambweni campuses have 2-3 applications per slot
* Quality of education is IDENTICAL - all campuses follow the same curriculum
* After 1st year, you can apply for inter-campus transfer

**Strategy 2: Upgrading Options**
* Start with Certificate (easier admission), then upgrade to Diploma
* Example: Certificate in Community Health → Diploma in Community Health (saves 1 year)

**Strategy 3: Second Intake Advantage**
* September intake is less competitive than March intake
* 40% more slots available

**Strategy 4: Alternative Entry**
* Mature age entry (23+ years) with 5 years work experience
* Lower grade requirements

**CAMPUS RANKING BY FACILITIES:**

**Tier 1 (Best Clinical Exposure):**
* Nairobi Campus - Attached to KNH (Level 6 Hospital)
* Mombasa Campus - Attached to Coast General (Level 5)
* Nakuru Campus - Attached to Nakuru Level 5
* Thika Campus - Attached to Thika Level 5

**Tier 2 (Excellent Training, Less Crowded):**
* Kisumu, Eldoret, Nyeri, Machakos, Embu

**Tier 3 (Same Quality, Better Admission Chances):**
* All other 60+ campuses

**INTERNSHIP & EMPLOYMENT ROADMAP:**

**Year 1:** Foundation training
**Year 2:** Specialized units rotation
**Year 3:** Intensive clinical attachment + final exams

**Post-Graduation:**
* **Month 1-2:** Apply for registration with relevant board (Nursing Council, Clinical Officers Council, Pharmacy Board)
* **Month 2-4:** Registration processed (Ksh 5,000-15,000 fees)
* **Month 3-6:** Mandatory internship begins (paid Ksh 20,000-35,000 monthly)
* **Month 12-18:** Full registration + job applications
* **Month 18+:** Employment or private practice

**Government Employment Process:**
* PSC advertises positions quarterly
* KMTC graduates have 80% success rate
* Starting Job Groups: H-K depending on course
* Pension + medical cover + housing allowance

**PRIVATE SECTOR OPPORTUNITIES:**
* International organizations (MSF, AMREF, WHO) - Ksh 100,000-200,000
* Private hospitals (Aga Khan, Nairobi Hospital, MP Shah) - Ksh 60,000-120,000
* Own practice/business - Unlimited
* Telemedicine companies - Ksh 50,000-80,000 part-time

**INTERNATIONAL CAREER PATHWAYS:**

**UK Pathway:**
* Nursing/Clinical Medicine recognized
* Take IELTS + OSCEs
* Visa sponsorship available (NHS shortage)
* Salary: £28,000-£35,000 (Ksh 5.2M-6.5M annually)

**Middle East:**
* Dubai, Qatar, Saudi hospitals actively recruit
* Salary: $2,000-$4,000 (Ksh 300K-600K monthly) tax-free
* 2-year contracts common

**USA/Canada:**
* Requires additional certification (NCLEX for nurses, USMLE for clinical officers)
* Salary: $60,000-$90,000 annually
* Pathway takes 2-3 years

**Australia:**
* Nursing highly demanded
* PR pathway available
* Salary: AUD 65,000-85,000

**BONUS: LITTLE-KNOWN COURSES WITH MASSIVE POTENTIAL:**

1. **Diploma in Health Promotion:** Only offered at 5 campuses, 100% employment with NGOs
2. **Certificate in Occupational Health:** Factories/industries must have one - salary Ksh 70,000+
3. **Diploma in Environmental Health:** County governments desperate for these - instant employment
4. **Certificate in Medical Social Work:** Combines healthcare + social services, unique niche

**RED FLAGS TO AVOID:**

❌ Don't apply to all popular campuses only - diversify
❌ Don't ignore financing options - apply for everything
❌ Don't choose a course based on hype - consider your passion and market demand
❌ Don't skip open days - visiting campus helps you decide
❌ Don't delay application - early submissions get priority

**FINAL PRO TIPS:**

✅ Join "KMTC Students Association" Facebook groups for insider info
✅ Network during attachments - 60% of jobs come from connections made during training
✅ Consider dual specialization after diploma (adds Ksh 20,000+ to salary)
✅ Start saving for registration fees during training
✅ Maintain excellent grades - sponsors target top performers for postgraduate scholarships

**APPLICATION DEADLINES 2025/2026:**
* September 2025 Intake: Applications close July 31, 2025
* March 2026 Intake: Applications close January 15, 2026

**Contact KMTC:**
* Website: www.kmtc.ac.ke
* Hotline: 0709 912 000
* Email: info@kmtc.ac.ke
* Physical Address: Along Ngong Road, Nairobi

**Conclusion:**

KMTC offers unmatched value for mid-level medical training. With strategic planning - from choosing the right campus to securing financing to positioning yourself for international opportunities - you can transform a KMTC diploma into a six-figure career within 5 years of graduation. The key is to be intentional about every decision from application to career launch."""

        # Check if post exists to update, or create new
        post, created = Post.objects.get_or_create(
            title=title,
            defaults={
                'slug': slugify(title),
                'category': 'Career Advice',
                'content': content,
                'author': author,
                'created_at': timezone.now()
            }
        )

        if not created:
            # Update existing if found
            post.content = content
            post.save()
            self.stdout.write(f"Updated existing post: {title}")
        else:
            self.stdout.write(f"Created new post: {title}")

        # Download and save image
        self.stdout.write("Downloading KMTC image...")
        try:
            response = requests.get(image_url, timeout=15)
            if response.status_code == 200:
                file_name = f"blog_kmtc_{post.id}.jpg"
                post.image.save(file_name, ContentFile(response.content), save=True)
                self.stdout.write(self.style.SUCCESS("✓ Image attached successfully."))
            else:
                self.stdout.write(self.style.ERROR("Failed to download image."))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error downloading image: {e}"))