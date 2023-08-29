from django.urls import path
from . import views

app_name = 'cliente'

# /home
urlpatterns = [
    path('', views.index, name='index'),
    # path('login/', views.index, name='login'),
]