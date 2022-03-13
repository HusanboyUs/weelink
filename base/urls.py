from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('', views.homeView, name='homeView'),
    #for loggin and register links
    path('register/', views.registerView, name='registerView'),
    path('login/', views.loginView, name='loginView'),
    #profile
    path('profile/', views.profileView, name='profileView'),
    path('updateProfile/', views.updateProfileView, name='updateProfileView'),
    path('addLink/', views.addProfileLink, name='addProfileLink')
]
