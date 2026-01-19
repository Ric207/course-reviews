from django import forms
from .models import StudentGrades
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# --- FIX: Import CourseReview from 'courses.models', NOT '.models' ---
from courses.models import CourseReview 

# --- SIGN-UP FORM ---
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Required. We will never share your email.')

    class Meta:
        model = User
        fields = ('username', 'email')

# --- GRADE ENTRY FORM ---
class GradeEntryForm(forms.ModelForm):
    
    class Meta:
        model = StudentGrades
        
        # We add 'mean_grade' to the top of the list
        fields = [
            'mean_grade', 
            
            # Group 1
            'mathematics', 'english', 'kiswahili',
            # Group 2
            'biology', 'physics', 'chemistry',
            # Group 3
            'history', 'geography', 'cre', 'ire', 'hre',
            # Group 4
            'home_science', 'art_and_design', 'agriculture', 'woodwork',
            'metalwork', 'building_construction', 'power_mechanics',
            'electricity', 'drawing_and_design', 'computer_studies',
            'aviation_technology',
            # Group 5
            'french', 'german', 'arabic', 'kenyan_sign_language',
            'music', 'business_studies',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # This makes the new 'mean_grade' field look good
        self.fields['mean_grade'].empty_label = "--- Select Your Mean Grade ---"
        self.fields['mean_grade'].widget.attrs.update({'class': 'form-control mb-3', 'style': 'font-weight: bold; font-size: 1.1rem;'})
        
        for field_name in self.fields:
            if field_name != 'mean_grade':
                field = self.fields[field_name]
                field.empty_label = "--- Select Grade ---"
                field.widget.attrs.update({'class': 'form-control form-control-sm mb-2'})

# --- CAREER QUIZ FORM ---
class CareerQuizForm(forms.Form):
    INTEREST_CHOICES = [
        ('tech', 'Working with computers, code, and technology'),
        ('health', 'Helping sick people and understanding the human body'),
        ('build', 'Designing structures, machines, and fixing things'),
        ('biz', 'Managing money, leading teams, and starting businesses'),
        ('law', 'Debating, fighting for justice, and reading history'),
        ('art', 'Creative design, music, fashion, or writing'),
    ]
    
    STRENGTH_CHOICES = [
        ('math', 'Mathematics & Physics'),
        ('bio', 'Biology & Chemistry'),
        ('lang', 'English, History & Languages'),
        ('biz', 'Business Studies & Economics'),
        ('tech', 'Computer Studies & Technical Subjects'),
        ('art', 'Art & Design or Music'),
    ]

    WORK_ENV_CHOICES = [
        ('office', 'In a modern office or corporate setting'),
        ('field', 'Outdoors, construction sites, or farms'),
        ('lab', 'In a laboratory or hospital'),
        ('studio', 'In a creative studio or media house'),
        ('remote', 'Working from home / Remote'),
    ]

    interest = forms.ChoiceField(
        choices=INTEREST_CHOICES, 
        widget=forms.RadioSelect, 
        label="1. What interests you the most?"
    )
    strength = forms.ChoiceField(
        choices=STRENGTH_CHOICES, 
        widget=forms.RadioSelect, 
        label="2. Which subjects are your strongest?"
    )
    environment = forms.ChoiceField(
        choices=WORK_ENV_CHOICES, 
        widget=forms.RadioSelect, 
        label="3. Where would you prefer to work?"
    )