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
    #timestamp = models.DateField()
    #class Meta:
    #    ordering = ('-timestamp',)