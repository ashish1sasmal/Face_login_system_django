from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

	path('',views.home,name='home'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('register/',views.register,name='register'),
]
