from django.shortcuts import render, redirect
from django.http import HttpResponse
from courses.models import Course, CourseReview
from blog.models import Post
from django.db.models import Avg, Count
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from students.models import Payment, Favorite
import datetime

# ==========================================
# PUBLIC PAGES
# ==========================================

def home(request):
    """
    Renders the public homepage with dynamic data.
    """
    # 1. Get Stats (Total number of courses in DB)
    total_courses = Course.objects.count()
    
    # 2. Get Latest 3 Blog Posts
    latest_posts = Post.objects.all().order_by('-created_at')[:3]
    
    # 3. Get Top Rated Courses
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
        name = request.POST.get('name', 'Student')
        return render(request, "courses/contact_us.html", {
            'success': True, 
            'user_name': name
        })

    return render(request, "courses/contact_us.html")


def robots_txt(request):
    """
    Generates the robots.txt file for SEO.
    """
    sitemap_url = request.build_absolute_uri('/sitemap.xml')
    
    lines = [
        "User-Agent: *",
        "Disallow: /admin/",
        "Disallow: /students/",
        "Allow: /",
        f"Sitemap: {sitemap_url}",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")

# ==========================================
# OWNER ANALYTICS DASHBOARD
# ==========================================

@staff_member_required
def owner_dashboard(request):
    """
    A custom dashboard for the site owner to see business stats.
    Only accessible by Admins/Staff.
    """
    # 1. User Stats
    total_users = User.objects.count()
    new_users_today = User.objects.filter(date_joined__date=datetime.date.today()).count()
    
    # 2. Financials
    paid_users = Payment.objects.filter(has_paid=True).count()
    total_revenue = paid_users * 100 # Assuming Ksh 100 per user
    
    # 3. Engagement
    total_reviews = CourseReview.objects.count()
    total_favorites = Favorite.objects.count()
    
    # 4. Most Popular Courses (Top 5 favorited)
    popular_courses = Course.objects.annotate(
        num_likes=Count('favorite')
    ).order_by('-num_likes')[:5]

    context = {
        'total_users': total_users,
        'new_users_today': new_users_today,
        'paid_users': paid_users,
        'total_revenue': total_revenue,
        'total_reviews': total_reviews,
        'popular_courses': popular_courses,
        'total_favorites': total_favorites,
    }
    return render(request, 'courses/owner_dashboard.html', context)
