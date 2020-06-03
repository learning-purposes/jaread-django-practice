from django.contrib import admin
from .models import Article, Journalist, Book, Review
# Register your models here.

admin.site.register(Article)
admin.site.register(Journalist)
admin.site.register(Book)
admin.site.register(Review)