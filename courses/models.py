from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Grade choices for the minimum grade field
GRADE_CHOICES = [
    ('A', 'A'), ('A-', 'A-'),
    ('B+', 'B+'), ('B', 'B'), ('B-', 'B-'),
    ('C+', 'C+'), ('C', 'C'), ('C-', 'C-'),
    ('D+', 'D+'), ('D', 'D'), ('D-', 'D-'),
    ('E', 'E'), ('Any', 'Any'),
]

class Course(models.Model):
    # Your original choices
    LEVEL_CHOICES = [
        ('Degree', 'Degree'),
        ('Diploma', 'Diploma'),
        ('Certificate', 'Certificate'),
        ('Artisan', 'Artisan'),
    ]

    PATH_CHOICES = [
        ('Medicine', 'Medicine & Health Sciences'),
        ('Engineering', 'Engineering & Technology'),
        ('Business', 'Business & Economics'),
        ('ICT', 'Information Technology'),
        ('Education', 'Education'),
        ('Agriculture', 'Agriculture & Environment'),
        ('Arts', 'Arts, Media & Humanities'),
        ('Law', 'Law & Criminology'),
        ('Hospitality', 'Hospitality & Tourism'),
        ('Science', 'Pure & Applied Sciences'),
        ('Others', 'General & Social Studies'),
    ]

    # Your original fields
    name = models.CharField(max_length=255)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    path = models.CharField(max_length=50, choices=PATH_CHOICES)
    
    # --- THIS FIELD IS NOW FIXED ---
    # We added 'default', 'blank', and 'null'
    min_mean_grade = models.CharField(
        max_length=5, 
        choices=GRADE_CHOICES, 
        help_text="Minimum KCSE Mean Grade required.",
        default='Any',  # Sets a default for new entries
        blank=True,     # Allows the field to be blank in forms
        null=True       # Allows the database to store a null value
    )
    
    # --- NEW FIELDS TO STORE DETAILED GUIDANCE ---
    
    min_cluster_points = models.FloatField(
        default=0.0, 
        blank=True, 
        null=True,
        help_text="Minimum cluster points (if applicable, e.g., for degrees)"
    )
    
    subject_requirements = models.TextField(
        blank=True, 
        null=True,
        help_text="Specific subject requirements, e.g., 'C+ in Maths'"
    )

    description = models.TextField(blank=True)
    
    career_path_info = models.TextField(
        blank=True, 
        null=True,
        help_text="Example career path after this course"
    )

    def __str__(self):
        return f"{self.name} ({self.level})"

# --- NEW COURSE REVIEW MODEL ---
class CourseReview(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rate from 1 (Poor) to 5 (Excellent)"
    )
    comment = models.TextField(help_text="Share your experience about this course.")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at'] # Newest reviews first

    def __str__(self):
        return f"{self.user.username} - {self.course.name} ({self.rating}/5)"
