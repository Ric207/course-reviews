import math
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# --- IMPORT COURSE MODEL (Needed for Favorites) ---
from courses.models import Course

# Grade choices for grade dropdowns (Points)
GRADE_CHOICES_POINTS = [
    (12, 'A'), (11, 'A-'), (10, 'B+'), (9, 'B'), (8, 'B-'),
    (7, 'C+'), (6, 'C'), (5, 'C-'), (4, 'D+'), (3, 'D'), (2, 'D-'), (1, 'E'),
]

# Grade choices for the mean_grade field (Letters)
GRADE_CHOICES_MEAN = [
    ('A', 'A'), ('A-', 'A-'), ('B+', 'B+'), ('B', 'B'), ('B-', 'B-'),
    ('C+', 'C+'), ('C', 'C'), ('C-', 'C-'), ('D+', 'D+'), ('D', 'D'), ('D-', 'D-'), ('E', 'E'),
]

class StudentGrades(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    validator_list = [MinValueValidator(1), MaxValueValidator(12)]

    # --- MEAN GRADE ---
    mean_grade = models.CharField(
        max_length=2, 
        choices=GRADE_CHOICES_MEAN, 
        null=True, 
        blank=False,
        help_text="Your official KCSE Mean Grade"
    )

    # --- Group 1: Compulsory ---
    mathematics = models.IntegerField(choices=GRADE_CHOICES_POINTS, null=True, blank=True, validators=validator_list)
    english = models.IntegerField(choices=GRADE_CHOICES_POINTS, null=True, blank=True, validators=validator_list)
    kiswahili = models.IntegerField(choices=GRADE_CHOICES_POINTS, null=True, blank=True, validators=validator_list)

    # --- Group 2: Sciences ---
    biology = models.IntegerField(choices=GRADE_CHOICES_POINTS, null=True, blank=True, validators=validator_list)
    physics = models.IntegerField(choices=GRADE_CHOICES_POINTS, null=True, blank=True, validators=validator_list)
    chemistry = models.IntegerField(choices=GRADE_CHOICES_POINTS, null=True, blank=True, validators=validator_list)

    # --- Group 3: Humanities ---
    history = models.IntegerField(choices=GRADE_CHOICES_POINTS, null=True, blank=True, validators=validator_list)
    geography = models.IntegerField(choices=GRADE_CHOICES_POINTS, null=True, blank=True, validators=validator_list)
    cre = models.IntegerField(choices=GRADE_CHOICES_POINTS, null=True, blank=True, validators=validator_list)
    ire = models.IntegerField(choices=GRADE_CHOICES_POINTS, null=True, blank=True, validators=validator_list)
    hre = models.IntegerField(choices=GRADE_CHOICES_POINTS, null=True, blank=True, validators=validator_list)

    # --- Group 4: Technicals ---
    home_science = models.IntegerField(choices=GRADE_CHOICES_POINTS, null=True, blank=True, validators=validator_list)
    art_and_design = models.IntegerField(choices=GRADE_CHOICES_POINTS, null=True, blank=True, validators=validator_list)
    agriculture = models.IntegerField(choices=GRADE_CHOICES_POINTS, null=True, blank=True, validators=validator_list)
    woodwork = models.IntegerField(choices=GRADE_CHOICES_POINTS, null=True, blank=True, validators=validator_list)
    metalwork = models.IntegerField(choices=GRADE_CHOICES_POINTS, null=True, blank=True, validators=validator_list)
    building_construction = models.IntegerField(choices=GRADE_CHOICES_POINTS, null=True, blank=True, validators=validator_list)
    power_mechanics = models.IntegerField(choices=GRADE_CHOICES_POINTS, null=True, blank=True, validators=validator_list)
    electricity = models.IntegerField(choices=GRADE_CHOICES_POINTS, null=True, blank=True, validators=validator_list)
    drawing_and_design = models.IntegerField(choices=GRADE_CHOICES_POINTS, null=True, blank=True, validators=validator_list)
    computer_studies = models.IntegerField(choices=GRADE_CHOICES_POINTS, null=True, blank=True, validators=validator_list)
    aviation_technology = models.IntegerField(choices=GRADE_CHOICES_POINTS, null=True, blank=True, validators=validator_list)

    # --- Group 5: Languages & Business ---
    french = models.IntegerField(choices=GRADE_CHOICES_POINTS, null=True, blank=True, validators=validator_list)
    german = models.IntegerField(choices=GRADE_CHOICES_POINTS, null=True, blank=True, validators=validator_list)
    arabic = models.IntegerField(choices=GRADE_CHOICES_POINTS, null=True, blank=True, validators=validator_list)
    kenyan_sign_language = models.IntegerField(choices=GRADE_CHOICES_POINTS, null=True, blank=True, validators=validator_list)
    music = models.IntegerField(choices=GRADE_CHOICES_POINTS, null=True, blank=True, validators=validator_list)
    business_studies = models.IntegerField(choices=GRADE_CHOICES_POINTS, null=True, blank=True, validators=validator_list)

    # --- CALCULATED RESULTS ---
    cluster_points_medicine = models.FloatField(default=0.0)
    cluster_points_engineering = models.FloatField(default=0.0)
    cluster_points_law = models.FloatField(default=0.0)
    cluster_points_arts = models.FloatField(default=0.0)

    def __str__(self):
        return f"Grades for {self.student.username}"

    def _get_all_grades_as_dict(self):
        return {
            'mathematics': self.mathematics or 0,
            'english': self.english or 0,
            'kiswahili': self.kiswahili or 0,
            'biology': self.biology or 0,
            'physics': self.physics or 0,
            'chemistry': self.chemistry or 0,
            'history': self.history or 0,
            'geography': self.geography or 0,
            'cre': self.cre or 0,
            'ire': self.ire or 0,
            'hre': self.hre or 0,
            'home_science': self.home_science or 0,
            'art_and_design': self.art_and_design or 0,
            'agriculture': self.agriculture or 0,
            'woodwork': self.woodwork or 0,
            'metalwork': self.metalwork or 0,
            'building_construction': self.building_construction or 0,
            'power_mechanics': self.power_mechanics or 0,
            'electricity': self.electricity or 0,
            'drawing_and_design': self.drawing_and_design or 0,
            'computer_studies': self.computer_studies or 0,
            'aviation_technology': self.aviation_technology or 0,
            'french': self.french or 0,
            'german': self.german or 0,
            'arabic': self.arabic or 0,
            'kenyan_sign_language': self.kenyan_sign_language or 0,
            'music': self.music or 0,
            'business_studies': self.business_studies or 0,
        }

    def calculate_all_clusters(self):
        grades = self._get_all_grades_as_dict()

        # --- Cluster: MEDICINE ---
        med_g1 = grades['biology']
        med_g2 = grades['chemistry']
        med_g3 = max(grades['mathematics'], grades['physics'])
        med_g4 = max(grades['english'], grades['kiswahili'])
        self.cluster_points_medicine = med_g1 + med_g2 + med_g3 + med_g4

        # --- Cluster: ENGINEERING (Civil/Mech/Elec) ---
        eng_g1 = grades['mathematics']
        eng_g2 = grades['physics']
        eng_g3 = grades['chemistry']
        eng_g4 = max(
            grades['english'], grades['kiswahili'], grades['biology'],
            grades['geography'], grades['history'], grades['cre'],
            grades['business_studies'], grades['agriculture']
        )
        self.cluster_points_engineering = eng_g1 + eng_g2 + eng_g3 + eng_g4

        # --- Cluster: LAW ---
        law_g1 = grades['english']
        law_g2 = max(grades['kiswahili'], grades['french'], grades['german'])
        law_g3 = max(grades['mathematics'], grades['biology'], grades['physics'], grades['chemistry'])
        law_g4 = max(grades['history'], grades['geography'], grades['cre'], grades['business_studies'])
        self.cluster_points_law = law_g1 + law_g2 + law_g3 + law_g4

        # --- Cluster: ARTS / SOCIAL SCIENCES ---
        arts_g1 = grades['english']
        arts_g2 = max(grades['mathematics'], grades['biology'], grades['physics'], grades['chemistry'])
        arts_g3 = max(grades['history'], grades['geography'], grades['cre'])
        arts_g4 = max(grades['kiswahili'], grades['french'], grades['german'], grades['business_studies'], grades['music'])
        self.cluster_points_arts = arts_g1 + arts_g2 + arts_g3 + arts_g4
        
        self.save()


# --- PAYMENT MODEL (Updated for Manual Pay) ---
class Payment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    has_paid = models.BooleanField(default=False)
    
    # NEW FIELDS: To store manual payment details
    transaction_code = models.CharField(max_length=20, blank=True, null=True, help_text="M-Pesa Transaction Code")
    date_paid = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} - Paid: {self.has_paid} ({self.transaction_code})"

# --- FAVORITE MODEL ---
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')

    def __str__(self):
        return f"{self.user.username} -> {self.course.name}"