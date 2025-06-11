from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Flower(models.Model):
    name = models.CharField(max_length=100)
    meaning = models.TextField()
    icon = models.ImageField(upload_to='flower_icons/', blank=True, null=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

class SavedBouquet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    flowers = models.ManyToManyField(Flower)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.user.username})"
