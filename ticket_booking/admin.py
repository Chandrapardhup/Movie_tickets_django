from django.contrib import admin
from .models import User, Movie, Theatre, Show, Booking

admin.site.register(User)
admin.site.register(Movie)
admin.site.register(Theatre)
admin.site.register(Show)
admin.site.register(Booking)
