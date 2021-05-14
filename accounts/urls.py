from django.urls import path
from . import views
app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registration/', views.registration, name='registration'),
]