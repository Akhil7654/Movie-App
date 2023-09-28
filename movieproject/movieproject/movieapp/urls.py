
from django.urls import path
from movieapp import views
from movieapp.views import update_movie

app_name="movieapp"


urlpatterns = [
    path('',views.index,name="index"),
    path('movie/<int:movie_id>/',views.detail,name="detail"),
    path('add/',views.add_movie,name="add_movie"),
    path('update/<int:id>/',views.update_movie,name="update_movie"),
    path('delete/<int:id>/',views.delete_movie,name="delete_movie")
]
