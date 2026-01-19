import requests
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from blog.models import Post
import time

class Command(BaseCommand):
    help = "Force updates blog images using reliable stock photos with backups"

    def handle(self, *args, **kwargs):
        posts = Post.objects.all()
        self.stdout.write("Starting Image Update...")

        # PRIMARY LINKS (High Quality)
        IMAGE_MAP = {
            'Medicine': 'https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=800&q=80',
            'Engineering': 'https://images.unsplash.com/photo-1503387762-592deb58ef4e?w=800&q=80',
            'ICT': 'https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800&q=80',
            'Business': 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=800&q=80',
            'Money': 'https://images.unsplash.com/photo-1579621970563-ebec7560ff3e?w=800&q=80',
            'Law': 'https://images.unsplash.com/photo-1589829085413-56de8ae18c73?w=800&q=80',
            'University': 'https://images.unsplash.com/photo-1541339907198-e08756dedf3f?w=800&q=80',
            'Graduation': 'https://images.unsplash.com/photo-1627556592933-ffe99c1cd9eb?w=800&q=80',
            'General': 'https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=800&q=80'
        }

        # BACKUP LINKS (If primary fails)
        BACKUP_MAP = {
            'Medicine': 'https://images.unsplash.com/photo-1505751172876-fa1923c5c528?w=800&q=80',
            'Engineering': 'https://images.unsplash.com/photo-1581094794329-cd136df4bf75?w=800&q=80',
            'ICT': 'https://images.unsplash.com/photo-1587620962725-abab7fe55159?w=800&q=80',
            'University': 'https://images.unsplash.com/photo-1562774053-701939374585?w=800&q=80',
            'General': 'https://images.unsplash.com/photo-1497633762265-9d179a990aa6?w=800&q=80'
        }

        for post in posts:
            # Check if image works (size > 0)
            if post.image:
                try:
                    if post.image.size > 0:
                        self.stdout.write(f"Skipping: {post.title} (Image OK)")
                        continue
                except:
                    pass # Image file missing, so re-download

            self.stdout.write(f"Updating: {post.title}...")
            
            # 1. Determine the category
            key = 'General'
            title_lower = post.title.lower()
            
            if 'med' in title_lower or 'doctor' in title_lower: key = 'Medicine'
            elif 'engin' in title_lower: key = 'Engineering'
            elif 'tech' in title_lower or 'ict' in title_lower: key = 'ICT'
            elif 'pay' in title_lower or 'money' in title_lower: key = 'Money'
            elif 'law' in title_lower: key = 'Law'
            elif 'univ' in title_lower or 'kuccps' in title_lower: key = 'University'
            elif 'degree' in title_lower or 'diploma' in title_lower: key = 'Graduation'
            
            urls_to_try = [IMAGE_MAP.get(key), BACKUP_MAP.get(key, BACKUP_MAP['General'])]

            # 2. Attempt Download
            success = False
            for url in urls_to_try:
                if not url: continue
                try:
                    response = requests.get(url, timeout=15)
                    if response.status_code == 200:
                        filename = f"blog_{post.id}.jpg"
                        post.image.save(filename, ContentFile(response.content), save=True)
                        self.stdout.write(self.style.SUCCESS(f"✓ DONE ({key})"))
                        success = True
                        break
                except Exception:
                    continue
            
            if not success:
                self.stdout.write(self.style.ERROR(f"x Failed all attempts for {post.title}"))

        self.stdout.write(self.style.SUCCESS("\nAll images updated successfully!"))