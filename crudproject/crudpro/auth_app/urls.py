from django.urls import path
from . import views

urlpatterns = [
    path('suv/', views.sign_up_view, name='signup_url'),
    path('siv/', views.signin_view, name='signin_url'),
    path('so/', views.logout_view, name='logout_url')
]