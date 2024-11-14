from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('settings/', views.settings_view, name='settings'),

]
