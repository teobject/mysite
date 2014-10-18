from django.db import models

# Create your models here.

from django.contrib import admin

class BB(models.Model):
    title  = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    post_date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

    def __unicode__(self):
        return self.title + '(' + self.name + ')'
        
admin.site.register(BB)
