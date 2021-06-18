from django.db import models
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator,MaxValueValidator,MinLengthValidator
from django.db.models.base import Model
from django.db.models.fields import CharField
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=30)

    def __str__(self):
        return f"{ self.caption }"
 

class Author(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(max_length=80)

    def fullName(self):
        return f"{self.firstName} {self.lastName}"

    def __str__(self):
        return self.fullName()

class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to='posts' , null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(db_index=True, unique=True)
    content = models.TextField(validators = [MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tag = models.ManyToManyField(Tag)

    def __str__(self): 
        return f"{self.title}"



    # def __str__(self):
    #     return self.title



class Comment(models.Model):
    user_name = models.CharField(max_length=20)
    user_email = models.EmailField()
    text = models.TextField(max_length=400)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")



