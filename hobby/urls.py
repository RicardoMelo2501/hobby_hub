from django.urls import path
from . import views

app_name = 'hobby'

# /hobby
urlpatterns = [
    path('', views.index, name='index')
]