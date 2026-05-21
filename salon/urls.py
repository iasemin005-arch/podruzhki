from django.urls import path
from . import views

app_name = 'salon'

urlpatterns = [
    path('', views.home, name='home'),
]
