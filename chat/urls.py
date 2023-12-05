from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.splash_view, name='splash'),
    path('home/', views.homepage, name='home'),
    path('friends/<int:pk>/', views.details, name='detail'),
    path('friends_list/', views.friends_list, name='friends_list'),
    path('profile/', views.profile, name='profile'),
    path('send_message/<int:pk>/', views.send_message, name='send_message'),
]