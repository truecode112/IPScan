from django.urls import path, include
from . import views

app_name = 'signup'

urlpatterns = [
    path('signupWithEmail/', views.signup_with_email, name='signupWithEmail'),
    path('register', views.signup_with_token, name='signupWithToken'),
    path('loginWithEmail/', views.login_with_email, name='loginWithEmail'),
]
