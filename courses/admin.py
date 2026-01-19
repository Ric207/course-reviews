from django.contrib import admin
from .models import Course, CourseReview # Removed University

# --- COURSE MANAGEMENT ---
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    # Shows these columns in the admin list
    list_display = ('name', 'level', 'path', 'min_mean_grade', 'min_cluster_points')
    
    # Adds filter options on the side
    list_filter = ('level', 'path', 'min_mean_grade')
    
    # Adds a search bar
    search_fields = ('name', 'description')
    
    # Organizes the edit form layout
    fieldsets = (
        (None, {
            # Removed 'universities' from fields since the model relation is gone
            'fields': ('name', 'level', 'path', 'description') 
        }),
        ('Requirements', {
            'fields': ('min_mean_grade', 'min_cluster_points', 'subject_requirements')
        }),
        ('Career Path', {
            'fields': ('career_path_info',)
        }),
    )

# --- REVIEW MANAGEMENT (View Feedback) ---
@admin.register(CourseReview)
class CourseReviewAdmin(admin.ModelAdmin):
    # Shows the course, the student, the rating, and the date
    list_display = ('course', 'user', 'rating', 'created_at', 'short_comment')
    
    # Filters to find "5 Star" or "Recent" reviews
    list_filter = ('rating', 'created_at')
    
    # Search for reviews by course name or student username
    search_fields = ('course__name', 'user__username', 'comment')
    
    # Helper to preview long comments in the list view
    def short_comment(self, obj):
        return obj.comment[:50] + "..." if len(obj.comment) > 50 else obj.comment
    short_comment.short_description = 'Comment Preview'