from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User


class Journalist(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    biography = models.TextField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Article(models.Model):
    author = models.ForeignKey(Journalist,
                               on_delete=models.CASCADE,
                               related_name='articles')
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=200)
    body = models.TextField()
    location = models.CharField(max_length=120)
    publication_date = models.DateField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author} wrote {self.title}"


class Book(models.Model):
    author = models.CharField(max_length=140)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=200)
    publication_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"


class Review(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    review_author = models.ForeignKey(User,
                                      on_delete=models.CASCADE)
    review = models.TextField(blank=True,
                              null=True)

    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),
                                                     MaxValueValidator(5)])

    book = models.ForeignKey(Book,
                             related_name='reviews',
                             on_delete=models.CASCADE)

    def __str__(self):
        return str(self.rating)
