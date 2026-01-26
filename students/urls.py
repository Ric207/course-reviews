from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    # Auth
    path('signup/', views.signup_view, name='signup'),
    path('profile/', views.profile_view, name='profile'),
    
    # Core
    path('enter-grades/', views.enter_grades, name='enter_grades'),
    path('results/', views.results, name='results'),
    
    # Payment (Cleaned up - Only one page needed)
    path('payment/', views.payment_page, name='payment'),
    
    # Features
    path('career-quiz/', views.career_quiz, name='career_quiz'),
    path('toggle-favorite/<int:course_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('my-favorites/', views.favorite_list, name='favorite_list'),
    path('course/<int:course_id>/reviews/', views.course_reviews, name='course_reviews'),
]