import requests
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from blog.models import Post
import time
import urllib.parse

class Command(BaseCommand):
    help = "Automatically generates and saves AI images for blog posts (with Retry & Fallback)"

    def handle(self, *args, **kwargs):
        posts = Post.objects.all()
        
        if not posts.exists():
            self.stdout.write(self.style.WARNING("No posts found. Run 'python manage.py populate_blog' first."))
            return

        self.stdout.write("Starting AI Image Generation...")

        # Dictionary to map categories/keywords to image prompts
        prompts = {
            'Career Advice': 'professional career counseling session office business high quality',
            'University News': 'modern university campus building kenya students sunny photorealistic',
            'KUCCPS Updates': 'students looking at computer screen happy applying college africa',
            'Success Stories': 'successful african graduate student holding diploma smiling graduation',
            'Medicine': 'doctor in hospital laboratory medical equipment professional lighting',
            'Engineering': 'civil engineer construction site helmet blueprints skyscrapers',
            'ICT': 'software developer coding computer screen matrix futuristic technology',
            'Law': 'gavel wooden hammer law justice court books library',
            'Money': 'kenyan shillings money finance graph business growth success',
        }

        for post in posts:
            # Skip if it already has an image
            if post.image:
                self.stdout.write(f"Skipping '{post.title}' (Image exists)")
                continue

            self.stdout.write(f"Generating image for: {post.title}...")
            
            # 1. Determine the prompt
            search_term = prompts.get(post.category, 'education students learning')
            
            if 'Medicine' in post.title or 'Doctor' in post.title: search_term = prompts['Medicine']
            elif 'Engineer' in post.title: search_term = prompts['Engineering']
            elif 'ICT' in post.title or 'Tech' in post.title: search_term = prompts['ICT']
            elif 'Law' in post.title: search_term = prompts['Law']
            elif 'Pay' in post.title or 'Job' in post.title: search_term = prompts['Money']

            # Encode the prompt for the URL
            encoded_prompt = urllib.parse.quote(search_term)
            
            # URL for AI Generator
            ai_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=800&height=500&nologo=true&seed={post.id}"
            
            # URL for Fallback (Reliable Placeholder)
            fallback_url = f"https://placehold.co/800x500/2c3e50/ffffff.png?text={urllib.parse.quote(post.category)}"

            # 2. Try to download (with retries)
            success = False
            for attempt in range(1, 4): # Try 3 times
                try:
                    # Increased timeout to 60 seconds
                    response = requests.get(ai_url, timeout=60)
                    
                    if response.status_code == 200:
                        filename = f"blog_{post.id}.jpg"
                        post.image.save(filename, ContentFile(response.content), save=True)
                        self.stdout.write(self.style.SUCCESS(f"✓ Saved AI image for {post.title}"))
                        success = True
                        break
                    else:
                        self.stdout.write(self.style.WARNING(f"  Attempt {attempt}: AI Server returned {response.status_code}"))
                
                except Exception as e:
                    self.stdout.write(self.style.WARNING(f"  Attempt {attempt}: Timeout or Error ({str(e)})"))
                    time.sleep(2) # Wait 2 seconds before retry

            # 3. Use Fallback if AI fails
            if not success:
                self.stdout.write(self.style.ERROR(f"x Failed to get AI image. Using fallback."))
                try:
                    response = requests.get(fallback_url, timeout=10)
                    if response.status_code == 200:
                        filename = f"blog_{post.id}_placeholder.jpg"
                        post.image.save(filename, ContentFile(response.content), save=True)
                        self.stdout.write(self.style.SUCCESS(f"✓ Saved fallback image for {post.title}"))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Critical: Could not save any image for {post.title}"))

        self.stdout.write(self.style.SUCCESS("\nProcess Complete!"))