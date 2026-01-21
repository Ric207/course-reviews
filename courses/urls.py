
from django.urls import path
from . import views

urlpatterns = [
    # Homepage
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact_us, name="contact_us"), 
    path("owner/dashboard/", views.owner_dashboard, name="owner_dashboard"),
]




