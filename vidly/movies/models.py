# this package encapsulates all the functionality around working
# with databases.  We have a module named models and in this module we have a class called model.
# this class encaps a lot of functionality for storing a model object in a database, retrieving model objects, filtering and so on.
from django.db import models

# Create your models here.

"""
    models are python classes we use to represent our application data.

    we will have models like genre and movie
"""

# derive this class from models.Model

"""
    By inheriting our Genre class from the base model class in Django, our genre class will also inherit all that functionality.  So we don't have to write any code to store genre objects in a database.  Django will automatically take care of that.
"""


class Genre(models.Model):
    # no genre can have a name longer than 255 chars.  One way to prevent security attacks by enforcing this limit
    name = models.CharField(max_length=255)


class Movie(models.Model):
    # what attributes of a movie do we need?
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    number_in_stock = models.IntegerField()
    daily_rate = models.FloatField()

    # with this we can create a relationship between movies and genres

    # on_delete tells Django what should happen when a genre is deleted
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
