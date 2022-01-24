from django.urls import path
from . import views

app_name= 'algorithm'
urlpatterns = [
    path('', views.home, name='homepage'),
    path('processing/', views.processing, name='processing'),
  
]
