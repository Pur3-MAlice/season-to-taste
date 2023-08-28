from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    ingredients = models.TextField()
    calories = models.IntegerField(default=0)
    fat = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)
    carbs = models.IntegerField(default=0)
    servs = models.IntegerField(default=0)
    featured_image = CloudinaryField('image', default='placeholder')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe"
        )
    categories = models.ForeignKey(
        Categories, on_delete=models.CASCADE, related_name="categories"
        )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    rate = models.ManyToManyField(User, related_name='rate')
    saved = models.ForeignKey(
        Saved, on_delete=models.CASCADE, related_name="saved"
        )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    Recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="comments"
        )
    name = models.CharField(max_length=80)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class Categories():
    id = models.AutoField(primary_key=True)
    Recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="recipe"
        )
    season = models.CharField(max_length=80)
    diet = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.diet}, {self.season}"


class Saved():
    id = models.AutoField(primary_key=True)
    Recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="recipe"
        )

    def __str__(self):
        return "Saved"
