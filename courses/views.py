from django.shortcuts import render
from django.http import HttpResponse
from courses.models import Course, CourseReview
from blog.models import Post
from django.db.models import Avg

def home(request):
    """
    Renders the public homepage with dynamic data.
    """
    # 1. Get Stats (Total number of courses in DB)
    total_courses = Course.objects.count()
    
    # 2. Get Latest 3 Blog Posts
    latest_posts = Post.objects.all().order_by('-created_at')[:3]
    
    # 3. Get Top Rated Courses (Courses with 4+ stars, ordered by rating)
    # We use 'reviews__rating' because of related_name='reviews' in models.py
    top_courses = Course.objects.annotate(
        avg_rating=Avg('reviews__rating')
    ).filter(avg_rating__gte=4).order_by('-avg_rating')[:3]

    context = {
        'total_courses': total_courses,
        'latest_posts': latest_posts,
        'top_courses': top_courses,
    }
    return render(request, "courses/home.html", context)


def about(request):
    """
    Renders the public 'About Us' page.
    """
    return render(request, "courses/about.html")


def contact_us(request):
    """
    Renders the public 'Contact Us' page.
    """
    if request.method == "POST":
        # Get the name to show a personalized success message
        name = request.POST.get('name', 'Student')
        
        # (Optional) Here you would add logic to send an email
        
        return render(request, "courses/contact_us.html", {
            'success': True, 
            'user_name': name
        })

    return render(request, "courses/contact_us.html")


def robots_txt(request):
    """
    Generates the robots.txt file for SEO.
    Tells search engines where to find the sitemap.
    """
    # We explicitly point to the /sitemap.xml URL
    sitemap_url = request.build_absolute_uri('/sitemap.xml')
    
    lines = [
        "User-Agent: *",
        "Disallow: /admin/",
        "Disallow: /students/",  # Keep student data private
        "Allow: /",
        f"Sitemap: {sitemap_url}",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
