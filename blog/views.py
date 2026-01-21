from django.shortcuts import render, get_object_or_404
from .models import Post
# Import the Payment model to check status from the students app
from students.models import Payment

def blog_list(request):
    """
    Displays the list of blog posts.
    Checks payment status to determine if 'Premium' badges should be shown.
    """
    # 1. Get all posts (ordered by newest first via Meta in models.py)
    posts = Post.objects.all().order_by('-created_at')
    
    # 2. Filter by category if selected (e.g., ?category=University News)
    category = request.GET.get('category')
    if category:
        posts = posts.filter(category=category)
        
    # 3. CHECK PAYMENT STATUS
    # We need to know if the user has paid to show the "Unlock" buttons vs "Read More"
    has_full_access = False
    if request.user.is_authenticated:
        # Check if they have a payment record and it is True
        payment = Payment.objects.filter(user=request.user).first()
        if payment and payment.has_paid:
            has_full_access = True
            
    context = {
        'posts': posts,
        'category': category,
        'has_full_access': has_full_access, # Pass this to the template
    }
    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, post_id):
    """
    Displays a single article.
    Checks payment status to either show full content or the 'Paywall'.
    """
    post = get_object_or_404(Post, pk=post_id)
    
    # Find related posts (same category, exclude current one)
    related_posts = Post.objects.filter(category=post.category).exclude(id=post.id)[:3]
    
    # --- CHECK PAYMENT STATUS ---
    has_full_access = False
    
    if request.user.is_authenticated:
        payment = Payment.objects.filter(user=request.user).first()
        if payment and payment.has_paid:
            has_full_access = True
            
    # ----------------------------
    
    context = {
        'post': post,
        'related_posts': related_posts,
        'has_full_access': has_full_access, # Pass this to the template
    }
    return render(request, 'blog/blog_detail.html', context)