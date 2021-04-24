import uuid

from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Isbn(models.Model):

    isbn_number = models.CharField(max_length=100, default=uuid.uuid4,editable=False)
    book_title = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.isbn_number)


class Store(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=2048, null=True, blank=True)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="store")
    categories = models.ManyToManyField(Category)
    tag = models.ForeignKey(Tag, null=True, blank=True, on_delete=models.CASCADE)
    isbn = models.OneToOneField(Isbn, on_delete=models.CASCADE, null=True, blank=True)
    #thumb = models.ImageField(upload_to='books',null=True,blank=True)

    def __str__(self):
        return self.title



