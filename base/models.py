from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver


class Song(models.Model):
    song_file = models.FileField(upload_to='user-playlist')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(default=datetime.now)

    def __str__(self):
        return str(self.song_file)


class Book(models.Model):
    cover = models.ImageField(upload_to='books/coverpages')
    book_file = models.FileField(upload_to='books/pdfs')
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(default=datetime.now)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ("-created_at",)
