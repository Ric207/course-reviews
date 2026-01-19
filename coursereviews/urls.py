from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# --- SEO IMPORTS ---
# These are needed for the sitemap and robots.txt features
from django.contrib.sitemaps.views import sitemap
from courses.sitemaps import StaticViewSitemap, BlogSitemap
from courses.views import robots_txt

# Define which sitemaps to include
sitemaps = {
    'static': StaticViewSitemap,
    'blog': BlogSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # User Authentication (Login/Logout/Password Reset)
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Your Apps
    path('students/', include('students.urls')),
    path('blog/', include('blog.urls')),
    
    # --- SEO URLS ---
    # 1. Sitemap Index (XML file for Google)
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    
    # 2. Robots.txt (Text file for crawlers)
    path('robots.txt', robots_txt, name='robots_txt'),
    
    # Homepage & Static Pages (Must be LAST so it doesn't block specific URLs)
    path('', include('courses.urls')),
]

# --- Serve Media Files (Images) During Development ---
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)