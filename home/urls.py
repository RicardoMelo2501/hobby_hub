from django.urls import path
from .views import home_view, user_view
from hobby import views 

app_name = 'home'

# /home
urlpatterns = [
    path('', views.index, name='index'),

    ####### USUÁRIO #######
    path('login/', user_view.login, name='login'),
    path('logout/', user_view.logout, name='logout'),

    # MODIFICAR O PERFIL
    path('edit/<int:pk>/', user_view.update, name='edit'),
    
    # VER PERFIL
    path('profile/<int:pk>/', user_view.profile, name='profile'),

    # CADASTRAR
    path('register/', user_view.register, name='register'),

    # MODIFICAR A SENHA
    path('change_password/<int:pk>/', user_view.change_password, name='change_password'),

    # Hobby
    path('hobby/add/', views.add, name='add_hobby'),
    # path('hobby/add/<int:pk>/', views.add, name='add_hobby'),

    # USAR PARA TESTES
    # path('default/', home_view.default_page, name='defalt_page'),
    
]