from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    # For the login page, we use Django’s built-in LoginView and specify our own template.
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'
    ), name='login'),
    # For logout, we use Django’s built-in LogoutView, and the post-logout redirect
    # is controlled by LOGOUT_REDIRECT_URL in settings.py.
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]