import datetime
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"

class Posts(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateField(auto_now_add=True)
    last_update = models.DateField(auto_now=True)
    category = models.ManyToManyField('Category', related_name='posts')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "posts"

class Comments(models.Model):
    author = models.CharField(max_length=60)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    # many to one relationship
    post = models.ForeignKey('Posts', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "comments"

