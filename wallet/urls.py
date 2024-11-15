from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('transactions/', views.transactions_view, name='transactions'),
    path('settings/', views.settings, name='settings'),
    path('support/', views.support, name='support'),
    path('send-money/', views.send_money, name='send_money'),
    path('receive-money/', views.receive_money, name='receive_money'),
]
