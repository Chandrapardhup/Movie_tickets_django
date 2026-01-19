from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    duration = models.IntegerField()   # minutes
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Theatre(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    total_screens = models.IntegerField()

    def __str__(self):
        return self.name


class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    show_time = models.DateTimeField()
    screen_number = models.IntegerField()
    available_seats = models.IntegerField()

    def __str__(self):
        return f"{self.movie} - {self.theatre}"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    seats = models.IntegerField()
    booked_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=20)

    def __str__(self):
        return f"Booking {self.id}"
