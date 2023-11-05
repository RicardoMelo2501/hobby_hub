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
    path('user/delete/<int:pk>/', user_view.delete, name='user_delete'),

    # MODIFICAR O PERFIL
    path('edit/<int:pk>/', user_view.update, name='edit'),
    
    # VER PERFIL
    path('profile/<int:pk>/', user_view.profile, name='profile'),

    # CADASTRAR
    path('register/', user_view.register, name='register'),

    # MODIFICAR A SENHA
    path('change_password/<int:pk>/', user_view.change_password, name='change_password'),
    path('forgot_password/', user_view.forgot_password, name='forgot_password'),

    # Hobby
    path('hobby/add/', views.add, name='add_hobby'),
    path('hobby/delete/<int:pk>/', views.delete, name='delete_hobby'),
    path('hobby/participar/<int:pk>/', views.add_participacao, name='participar_hobby'),
    path('hobby/list/', views.list_hobby, name='list_hobby'),

    # USAR PARA TESTES
    # path('default/', home_view.default_page, name='defalt_page'),
    
]