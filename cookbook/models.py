from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))

RATE = (
    (0, "N/A"),
    (1, "Bad"),
    (2, "Okay"),
    (3, "Good"),
    (4, "Great"),
    (5, "Excellent")
)


class Diet(models.Model):
    name = models.TextField(max_length=70, default="Uncategorised")

    def __str__(self):
        return self.name


class Season(models.Model):
    name = models.TextField(max_length=70, default="Uncategorised")

    def __str__(self):
        return self.name


class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    ingredients = models.TextField()
    content = models.TextField()
    calories = models.IntegerField(default=0)
    fat = models.IntegerField(default=0)
    protein = models.IntegerField(default=0)
    carbs = models.IntegerField(default=0)
    servs = models.IntegerField(default=0)
    featured_image = CloudinaryField('image', default='placeholder')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipes"
        )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    diet = models.ForeignKey(
        Diet, on_delete=models.CASCADE,
        related_name="recipes")
    season = models.ForeignKey(
        Season, on_delete=models.CASCADE,
        related_name="recipes")
    # rate = models.ManyToManyField(
    #     Categories, related_name="recipes"
    #     )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title + " | " + str(self.author)


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    recipe = models.ForeignKey(
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


class Saved(models.Model):
    id = models.AutoField(primary_key=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


# class Rating(models.Model):
#     id = models.AutoField(primary_key=True)
#     recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     rating = models.IntegerField(choices=RATE, default=0)
