from django.db import models
from django.db.models.fields import TextField
from django.contrib.auth.models import User 
from datetime import date
from django.utils import timezone

# 1-2
# class Author(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)

#     class Meta:
#         ordering = ['last_name', 'first_name']

#     def __str__(self):
#         return self.first_name

# class Book(models.Model):
#     title = models.CharField(max_length=150)
#     author = models.ManyToManyField(Author, related_name="title")

#     def __str__(self):
#         return self.title

# class Visitors(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.first_name    

# class Library(models.Model):
#     book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
#     borrower = models.ForeignKey(Visitors, on_delete=models.CASCADE, related_name='Visitors', null=True, blank=True)

#     def __str__(self):
#         return f'The book "{self.book}" was borrowed by {self.borrower}'


#3
class Publisher(models.Model):
    user = models.CharField(max_length=120, blank=True, null=True)
    information = models.CharField(max_length=255, help_text="Enter some information about yourself.")

    def __str__(self):
        return str(self.user)

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Publisher, on_delete= models.CASCADE)
    body = TextField(help_text="Enter you post here.")
    publish_date = models.DateField(auto_now=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.TextField(help_text="Enter you cooment here here.")
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    blog= models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    blog = models.ForeignKey(Post, on_delete=models.DO_NOTHING)

    def __str__(self):
        return "By user {} to article {}".format(self.user.username, self.blog.id)
    
# Create your models here.
