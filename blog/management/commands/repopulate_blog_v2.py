from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Post
from django.utils.text import slugify
from django.utils import timezone
import requests
from django.core.files.base import ContentFile

class Command(BaseCommand):
    help = "Wipes and repopulates blog with PREMIUM content and images"

    def handle(self, *args, **kwargs):
        # 1. Get Author (Admin)
        try:
            author = User.objects.filter(is_superuser=True).first()
            if not author:
                self.stdout.write(self.style.ERROR("No Admin user found. Please create a superuser first."))
                return
        except:
            return

        # 2. Clear Old Data to ensure no "boring" posts remain
        self.stdout.write("Deleting old posts...")
        Post.objects.all().delete()

        # 3. Define Premium Content Data
        # Note: The text includes the [LOCKED CONTENT STARTS HERE] marker for your paywall logic.
        
        data = [
            {
                "title": "Understanding the New Higher Education Funding Model",
                "category": "University News",
                "image": "https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=800&q=80", 
                "content": """The new Higher Education Funding (HEF) model has completely changed how university fees are paid in Kenya. Unlike the old HELB system where everyone got a standard loan, this new system classifies families into four specific 'Bands' based on monthly household income. If you get classified wrongly, you could end up paying Ksh 200,000+ per year instead of Ksh 10,000.

[LOCKED CONTENT STARTS HERE]

**The Classification Bands (The Secret Criteria):**
* **Band 1 (Vulnerable):** Families earning less than **Ksh 5,995**.
    * *Benefit:* 100% Government Scholarship + Upkeep Loan of Ksh 60,000. You pay **Zero Fees**.
* **Band 2 (Extremely Needy):** Income between **Ksh 5,995 and Ksh 23,670**.
    * *Benefit:* 70% Scholarship, 30% Loan. You pay approx **7% of fees**.
* **Band 3 (Needy):** Income between **Ksh 23,671 and Ksh 70,000**.
    * *Benefit:* 50% Scholarship, 30% Loan. You pay **20% of fees**.
* **Band 4 & 5 (Less Needy):** Income **above Ksh 70,000**.
    * *Risk:* You pay **40% to 60% of fees**.

**How to Win an Appeal:**
If you are placed in Band 4 or 5 but cannot afford it, you must appeal. The system checks for 'markers of poverty'.
* **Tip 1:** Upload a death certificate if a parent is deceased.
* **Tip 2:** Upload siblings' birth certificates to prove high dependency ratio.
* **Tip 3:** Do NOT use a photo of a permanent stone house during application; this triggers the 'Less Needy' flag automatically."""
            },
            {
                "title": "Top 5 Highest Paying Jobs in Kenya (2025)",
                "category": "Career Advice",
                "image": "https://images.unsplash.com/photo-1579621970563-ebec7560ff3e?w=800&q=80", 
                "content": """The job market has shifted drastically. The traditional 'lucrative' careers of Law and Pilot are becoming saturated, while new digital frontiers are minting young millionaires. If you are choosing a course based on money, you need to look at the 2025 salary data, not what your parents told you 10 years ago.

[LOCKED CONTENT STARTS HERE]

**The New Top 5 (Monthly Net Salaries):**

1.  **Remote Software Engineer (Global):**
    * *Salary:* **Ksh 250,000 - Ksh 800,000+**
    * *The Secret:* Don't work for Kenyan firms. Learn Python/React and work remotely for US/European startups (Andela, Microsoft ADC).
2.  **Specialized Medicine (Surgeon/Anesthesiologist):**
    * *Salary:* **Ksh 300,000 - Ksh 1M+**
    * *The Catch:* It takes 12+ years of study to reach this level. Interns only earn ~Ksh 150k.
3.  **Data Science & AI Specialist:**
    * *Salary:* **Ksh 180,000 - Ksh 350,000**
    * *Why:* Banks (Equity, KCB) and Telcos (Safaricom) are desperate for people who can analyze big data.
4.  **Actuarial Science (Fully Qualified):**
    * *Salary:* **Ksh 200,000+**
    * *Requirement:* You MUST pass the professional papers (SOA/IFoA). A degree alone pays peanuts (Ksh 40k).
5.  **NGO Project Management (UN/World Bank):**
    * *Salary:* **Ksh 200,000 - Ksh 500,000 (Tax-Free)**
    * *Path:* Study International Relations or Development Studies, but pair it with French/Spanish."""
            },
            {
                "title": "KUCCPS Application Hacks: Secure Your Dream Course",
                "category": "KUCCPS Updates",
                "image": "https://images.unsplash.com/photo-1523240795612-9a054b0db644?w=800&q=80", 
                "content": """Making a mistake on the KUCCPS portal is irreversible. Every year, thousands of students with A and A- grades miss out on their dream courses because they listed highly competitive courses (like Medicine) as 1a, 1b, and 1c. If you miss the cutoff for one, you likely miss them all.

[LOCKED CONTENT STARTS HERE]

**The 'Safe Bet' Algorithm:**
To guarantee placement, structure your 4 choices like this:

* **Choice 1a (The Dream):** The course you really want (e.g., Medicine at UoN).
* **Choice 1b (The Smart Swap):** Same course, different uni (e.g., Medicine at Maseno). The cutoff is usually 1-2 points lower.
* **Choice 2 (The Pivot):** A related professional course (e.g., Pharmacy or Dental Surgery).
* **Choice 3 (The Safety Net):** A course where your Cluster Points are **5+ points higher** than the cutoff (e.g., Nursing).
* **Choice 4 (The Guarantee):** A course you are overqualified for, just to ensure you get a government capitation slot.

**Insider Hack:** Submit your application between **2 AM and 5 AM**. The portal crashes during the day due to traffic."""
            },
            {
                "title": "Diploma to Degree: The Hidden Shortcut",
                "category": "Success Stories",
                "image": "https://images.unsplash.com/photo-1627556592933-ffe99c1cd9eb?w=800&q=80", 
                "content": """Missing the C+ cutoff in KCSE often feels like the end of the road, but for many successful Kenyans, it was just a detour. The 'TVET Pathway' is actually a hidden gem. Employers in 2025 often prefer Diploma graduates because they have 3 years of practical, hands-on experience compared to Degree students who focus on theory.

[LOCKED CONTENT STARTS HERE]

**The 'Credit Transfer' Hack:**
You do not have to start from Year 1.
* **Step 1:** Enroll in a KNEC Diploma course (2-3 years) at a Technical Training Institute (TTI) or Polytechnic. Cost is low (approx Ksh 30k/year with capitation).
* **Step 2:** Score a **Credit** or **Distinction**.
* **Step 3:** Apply for a 'Credit Transfer' at a university like TUK, MKU, or Strathmore. They can exempt you from up to **40% of the degree units**, allowing you to join in **Year 2 or Year 3**.

**Best Courses for this Path:**
* **Pharmaceutical Technology:** High demand, easy transition to B.Pharm.
* **Quantity Surveying:** Diploma holders often start their own construction firms immediately.
* **Software Engineering:** Skills matter more than papers. A portfolio built during your diploma is worth more than a degree."""
            },
            {
                "title": "UoN vs JKUAT: The Ultimate Comparison",
                "category": "University News",
                "image": "https://images.unsplash.com/photo-1562774053-701939374585?w=800&q=80", 
                "content": """This is the ultimate rivalry in Kenyan higher education: The prestigious City Campus (UoN) vs. The Tech Farm in Juja (JKUAT). Your choice shouldn't just be about the name, but about the *culture* and *resources* specific to your field. Choosing the wrong one can mean 4 years of frustration.

[LOCKED CONTENT STARTS HERE]

**1. Engineering & Technology:**
* **Winner: JKUAT.**
* *Why:* JKUAT was built for tech. Their labs in Juja are better equipped for practicals (Mechatronics, Civil, Agricultural Engineering). UoN is theory-heavy.

**2. Medicine & Health:**
* **Winner: UoN.**
* *Why:* UoN medical school is physically attached to Kenyatta National Hospital (KNH). You get exposure to complex referral cases that JKUAT students in smaller hospitals don't see.

**3. The 'Strike' Factor:**
* **Winner: JKUAT.** Historically, JKUAT has a more stable academic calendar. UoN politics can lead to strikes that delay graduation by up to a year.

**4. Campus Life:**
* **UoN:** Fast-paced, hustler mentality, expensive city living.
* **JKUAT:** Community vibe, cheaper rent in Juja, focused environment."""
            }
        ]

        # 4. Create Posts & Download Images
        self.stdout.write(f"Creating {len(data)} Premium Posts...")
        
        for item in data:
            self.stdout.write(f"Processing: {item['title']}...")
            post = Post.objects.create(
                title=item['title'],
                slug=slugify(item['title']),
                category=item['category'],
                content=item['content'],
                author=author,
                created_at=timezone.now()
            )
            
            # Download Image
            try:
                response = requests.get(item['image'], timeout=10)
                if response.status_code == 200:
                    file_name = f"blog_{post.id}.jpg"
                    post.image.save(file_name, ContentFile(response.content), save=True)
                    self.stdout.write(self.style.SUCCESS(f"✓ Created & Image Saved"))
            except Exception as e:
                self.stdout.write(self.style.WARNING(f"Image failed for {item['title']}: {e}"))

        self.stdout.write(self.style.SUCCESS("BLOG REPOPULATION COMPLETE!"))