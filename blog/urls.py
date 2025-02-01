from django.urls import path
from . import views
from .views import register, login_view, logout_view


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('post/<str:post_id>/', views.post_detail, name='post-detail'),
    path('create/', views.create_post, name='create-post'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('accounts/login/', login_view, name='login'),  # Alias for login

]