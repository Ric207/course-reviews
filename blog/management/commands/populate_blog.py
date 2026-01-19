from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Post
from django.utils.text import slugify # <-- IMPORT THIS
from django.utils import timezone

class Command(BaseCommand):
    help = "Populate the blog with sample data"

    def handle(self, *args, **kwargs):
        # Get the admin user (ID 1) to be the author
        try:
            author = User.objects.get(pk=1)
        except User.DoesNotExist:
            # Fallback: Get the first superuser if ID 1 doesn't exist
            author = User.objects.filter(is_superuser=True).first()
            if not author:
                self.stdout.write(self.style.ERROR("Error: No Admin user found. Please create a superuser first using 'python manage.py createsuperuser'"))
                return

        # Clear old posts to avoid duplicates and slug conflicts
        Post.objects.all().delete()
        self.stdout.write("Old blog posts deleted.")

        # Sample Data
        samples = [
            {
                "title": "How to Choose the Right Degree for You",
                "category": "Career Advice",
                "content": """Choosing a degree is one of the biggest decisions you will make. Start by assessing your strengths and interests. Do you prefer solving mathematical problems, or are you more interested in social sciences? 
                
                Don't just look at the 'prestige' of a course; look at the job market demand. Courses in ICT, Engineering, and Medicine are competitive but rewarding. However, emerging fields in Data Science and Renewable Energy are also gaining traction.
                
                Take your time, research university requirements, and use our Cluster Points Calculator to see where you fit best."""
            },
            {
                "title": "KUCCPS Application Guide 2025",
                "category": "KUCCPS Updates",
                "content": """The Kenya Universities and Colleges Central Placement Service (KUCCPS) has opened its portal for the 2025 intake. 
                
                Key things to remember:
                1. Ensure you have your KCSE index number and KCPE index number ready.
                2. Pay the application fee via M-Pesa (usually Ksh 1,500).
                3. You have 4 choices for degree programs. 1a, 1b, and 1c must be the same course at different universities.
                
                Don't wait until the last minute! The portal often experiences traffic jams on the final day."""
            },
            {
                "title": "Top 5 Highest Paying Jobs in Kenya",
                "category": "Career Advice",
                "content": """Everyone wants a career that pays well. According to recent market data, here are the top 5 highest paying sectors in Kenya:
                
                1. **Medicine & Surgery:** Specialized consultants earn top shilling.
                2. **Software Engineering:** With remote work options, devs are earning in USD.
                3. **Actuarial Science:** High demand in insurance and banking.
                4. **Law:** Corporate lawyers and advocates in top firms command high fees.
                5. **Pilot / Aviation:** A high-risk, high-reward profession.
                
                Remember, passion drives success. Don't pick a job solely for money if you hate the work!"""
            },
            {
                "title": "University of Nairobi vs JKUAT Which is Better",
                "category": "University News",
                "content": """This is the classic debate. UoN is known as the center of academic excellence with a strong focus on Medicine, Law, and Humanities. It is located in the CBD, offering a fast-paced city life.
                
                JKUAT, on the other hand, is the 'Tech' giant. It is the premier destination for Agriculture, Engineering, and Technology courses. The Juja campus offers a quieter, more focused environment.
                
                Verdict: Go to JKUAT for Tech/Agri, and UoN for Arts/Medicine."""
            },
            {
                "title": "From Diploma to Degree It Is Possible",
                "category": "Success Stories",
                "content": """Did you miss the C+ cutoff? Don't worry. Thousands of successful professionals started with a Diploma. 
                
                John M., a Senior Network Engineer at Safaricom, started with a Diploma in IT at a TVET institution. After working for 2 years, he used his credit transfers to join a Degree program in year 2.
                
                The path might be longer, but the destination is the same. Never give up on your dream."""
            },
            {
                "title": "Understanding the New Higher Education Funding Model",
                "category": "University News",
                "content": """The government has introduced a new funding model (HEF) that categorizes students based on need: Vulnerable, Extremely Needy, Needy, and Less Needy.
                
                Scholarships and Loans are awarded based on this classification. Ensure you fill out your details truthfully on the HEF portal to get the support you deserve."""
            }
        ]

        # Create Posts
        for sample in samples:
            # THIS IS THE FIX: Generate a slug from the title
            slug = slugify(sample['title'])
            
            Post.objects.create(
                title=sample['title'],
                slug=slug,  # <--- We now provide the slug explicitly
                category=sample['category'],
                content=sample['content'],
                author=author,
                created_at=timezone.now()
            )

        self.stdout.write(self.style.SUCCESS(f"Successfully added {len(samples)} sample blog posts!"))