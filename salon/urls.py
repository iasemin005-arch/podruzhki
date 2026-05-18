from django.urls import path

from .views import home

app_name = 'salon'

urlpatterns = [
    path('', home, name='home'),
]
