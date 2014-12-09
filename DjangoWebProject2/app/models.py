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
    title = models.CharField(max_length = 150)
    about = models.TextField()
    timestamp = models.DateField()