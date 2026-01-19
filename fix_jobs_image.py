import requests
import os
import sys
import django
from django.core.files.base import ContentFile

# 1. Add the current directory to the Python path so it finds 'coursereviews'
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 2. Setup Django Environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coursereviews.settings')
django.setup()

# 3. Import Models (Must be done AFTER django.setup())
from blog.models import Post

def fix_image():
    # Find the specific post
    try:
        post = Post.objects.get(title__icontains="Top 5 Highest Paying Jobs")
        print(f"Found post: {post.title}")
    except Post.DoesNotExist:
        print("Error: Could not find the blog post. Check the title.")
        return

    # Use a reliable Stock Image URL (Money/Finance theme)
    image_url = "https://images.unsplash.com/photo-1579621970563-ebec7560ff3e?auto=format&fit=crop&w=800&q=80"
    
    print("Downloading replacement image...")

    try:
        response = requests.get(image_url, timeout=30)
        if response.status_code == 200:
            # Save it to the model
            filename = f"blog_{post.id}_money.jpg"
            post.image.save(filename, ContentFile(response.content), save=True)
            print(f"✅ Success! Image updated for: {post.title}")
        else:
            print(f"Failed to download image. Status code: {response.status_code}")
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fix_image()