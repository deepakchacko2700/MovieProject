from django.urls import path
from . import views
app_name='movieapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<int:movie_id>/', views.details, name='details'),
    path('add/', views.add_movie, name='add'),
    path('update/<int:movie_id>/', views.update, name= 'update'),
    path('delete/<int:movie_id>/', views.delete, name='delete'),
]