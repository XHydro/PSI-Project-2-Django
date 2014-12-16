"""
Definition of models.
"""

from django.db import models
from django.contrib import admin
# Create your models here.

class app(models.Model):
    title = models.CharField(max_length = 150)
    body = models.TextField()
    timestamp = models.DateTimeField()

class appAdmin(admin.ModelAdmin):
    list_display = ('title','timestamp')

#admin.site.register(app)
admin.site.register(app, appAdmin)

class Book(models.Model):
    title = models.CharField(max_length = 30)
    about = models.CharField(max_length = 150)
    #author = models.CharField(max_length = 50)
    timestamp = models.CharField(max_length = 4)
    
class Author(models.Model):
    name = models.CharField(max_length = 50)

class BookComment(models.Model):
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Book, related_name='comments')
    class Meta:
        ordering = ('-timestamp',)