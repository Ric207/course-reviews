from django import forms
# We import the new CourseReview model
from .models import CourseReview

# =================================================
# SECTION 1: YOUR INITIAL GRADES FORM (PRESERVED)
# =================================================

GRADES = [
    ('', '---'),
    ('A', 'A'), ('A-', 'A-'),
    ('B+', 'B+'), ('B', 'B'), ('B-', 'B-'),
    ('C+', 'C+'), ('C', 'C'), ('C-', 'C-'),
    ('D+', 'D+'), ('D', 'D'), ('D-', 'D-'),
    ('E', 'E'),
]

SUBJECTS_LIST = [
    {'display': 'Mathematics', 'name': 'mathematics'},
    {'display': 'English', 'name': 'english'},
    {'display': 'Kiswahili', 'name': 'kiswahili'},
    {'display': 'Biology', 'name': 'biology'},
    {'display': 'Physics', 'name': 'physics'},
    {'display': 'Chemistry', 'name': 'chemistry'},
    {'display': 'History', 'name': 'history'},
    {'display': 'Geography', 'name': 'geography'},
    {'display': 'CRE', 'name': 'cre'},
    {'display': 'IRE', 'name': 'ire'},
    {'display': 'Business Studies', 'name': 'business_studies'},
    {'display': 'Home Science', 'name': 'home_science'},
    {'display': 'Computer Studies', 'name': 'computer_studies'},
    {'display': 'German', 'name': 'german'},
    {'display': 'French', 'name': 'french'},
    {'display': 'Art and Design', 'name': 'art_and_design'},
    {'display': 'Agriculture', 'name': 'agriculture'},
]

MIN_SUBJECTS = 7

class GradesForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for subj in SUBJECTS_LIST:
            self.fields[subj['name']] = forms.ChoiceField(
                choices=GRADES,
                required=False,
                label=subj['display'],
                widget=forms.Select(attrs={'class': 'form-select'})
            )

    def clean(self):
        cleaned = super().clean()
        filled = [v for v in cleaned.values() if v and v != '']
        if len(filled) < MIN_SUBJECTS:
            raise forms.ValidationError(f"Please fill at least {MIN_SUBJECTS} subjects (you filled {len(filled)}).")
        return cleaned


# =================================================
# SECTION 2: NEW REVIEW FORM (ADDED)
# =================================================

class ReviewForm(forms.ModelForm):
    """
    Form for students to add reviews and ratings to a course.
    """
    class Meta:
        model = CourseReview
        fields = ['rating', 'comment']
        
        widgets = {
            'rating': forms.NumberInput(attrs={
                'class': 'form-control', 
                'min': 1, 
                'max': 5,
                'placeholder': '1-5'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 3, 
                'placeholder': 'Share your experience: Is the course hard? How are the job prospects?'
            }),
        }