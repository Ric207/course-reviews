from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Shows these columns in the list view
    list_display = ('title', 'category', 'author', 'created_at')
    
    # Adds sidebar filters
    list_filter = ('category', 'created_at')
    
    # Adds a search bar at the top
    search_fields = ('title', 'content')
    
    # Automatically fills the 'slug' field when you type the title
    prepopulated_fields = {'slug': ('title',)}
