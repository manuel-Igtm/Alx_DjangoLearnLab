from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Author Model:
# name: CharField.
class Author(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
# Book Model:
# title: CharField.
# author: ForeignKey to Author.
class Book(models.Model):
    title = models.CharField(max_length = 100)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    def __str__(self):
        return self.title
    


# Library Model:
# name: CharField.
# books: ManyToManyField to Book.
class Library(models.Model):
    name = models.CharField(max_length = 100)
    book = models.ManyToManyField(Book)

    def __str__(self):
        return self.name
# Librarian Model:
# name: CharField.
# library: OneToOneField to Library
class Librarian(models.Model):
    name = models.CharField(max_length = 100)
    library = models.OneToOneField(Library, on_delete = models.CASCADE)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]
    role = models.CharField(
        max_length=100, choices=ROLE_CHOICES, default='Member')
    user = models.OneToOneField(
        User, related_name='user_profile', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
    
