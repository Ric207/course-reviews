from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import Post

class StaticViewSitemap(Sitemap):
    """
    Maps the main static pages of the website.
    """
    priority = 0.6
    changefreq = 'weekly'

    def items(self):
        # The URL names as defined in your urls.py files
        return ['home', 'about', 'contact_us', 'blog_list']

    def location(self, item):
        return reverse(item)

class BlogSitemap(Sitemap):
    """
    Maps every individual blog post automatically.
    This helps Google index your specific articles.
    """
    changefreq = 'monthly'
    priority = 0.8

    def items(self):
        return Post.objects.all().order_by('-created_at')

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        # Points to the blog detail view: /blog/<id>/
        return reverse('blog_detail', args=[obj.id])