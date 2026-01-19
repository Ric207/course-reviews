from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    # Authentication & Profile
    path('signup/', views.signup_view, name='signup'),
    path('profile/', views.profile_view, name='profile'),
    
    # Core Student Flow
    path('enter-grades/', views.enter_grades, name='enter_grades'),
    path('results/', views.results, name='results'),
    
    # Payment Flow (New Polling System)
    path('payment/', views.payment_page, name='payment'),
    path('payment/processing/', views.payment_processing, name='payment_processing'),
    path('payment/check-status/', views.check_payment_status, name='check_payment_status'),
    path('payment/confirm-manual/', views.confirm_payment_manual, name='confirm_payment_manual'),
    
    # Features (Quiz, Favorites, Reviews)
    path('career-quiz/', views.career_quiz, name='career_quiz'),
    path('toggle-favorite/<int:course_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('my-favorites/', views.favorite_list, name='favorite_list'),
    path('course/<int:course_id>/reviews/', views.course_reviews, name='course_reviews'),
]