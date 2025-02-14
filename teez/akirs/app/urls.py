from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),  
    path('signin/', views.signin, name='signin'), 
    path('profile/<int:facility_id>/', views.profile_view, name='facility_profile'),
    path("edit-profile/<int:facility_id?/", views.edit_profile, name="edit_profile"),


]