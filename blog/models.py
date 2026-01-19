from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    CATEGORY_CHOICES = [
        ('Career Advice', 'Career Advice'),
        ('University News', 'University News'),
        ('KUCCPS Updates', 'KUCCPS Updates'),
        ('Success Stories', 'Success Stories'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, help_text="Unique URL identifier (e.g. how-to-choose-course)")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Career Advice')
    
    # Requires Pillow (pip install Pillow)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
        
    def get_read_time(self):
        # Simple read time calculator (150 words per minute)
        words = len(self.content.split())
        minutes =  words // 150
        return max(1, minutes)
