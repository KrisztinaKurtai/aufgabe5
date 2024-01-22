from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='user_home'),
    path('', views.index, name='user_about'),
    path('', views.index, name='user_contact'),
]
