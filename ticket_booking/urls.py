from django.urls import path
from .views import create_movie, list_movies, create_theatre, list_theatres, create_show, list_shows, create_user, list_users, create_booking, list_bookings

urlpatterns = [
    path('users/', list_users),
    path('users/create/', create_user),

    path('movies/', list_movies),
    path('movies/create/', create_movie),

    path('theatres/', list_theatres),
    path('theatres/create/', create_theatre),

    path('shows/', list_shows),
    path('shows/create/', create_show),

    path('bookings/', list_bookings),
    path('bookings/create/', create_booking),
]

