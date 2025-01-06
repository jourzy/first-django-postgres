from django.urls import path
from . import views_old
from . import views

# Create a list of all the urls we will have in our project
urlpatterns = [
    path('', views_old.index, name='index'),
    path('counter', views.counter, name='counter'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('post/<str:pk>', views.post, name='post')
]