from django.urls import path
from . import views



urlpatterns = [
	path('', views.index, name='index'),
	path('profile/<str:username>/', views.profile, name='profile'),
	path('profile_edit/<str:username>/',views.edit_profile, name='edit_profile'),
	path('register/', views.register, name='register'),
	path('login/', views.login_view, name='login'),
	path('logout/', views.logout_view, name='logout'),
]

