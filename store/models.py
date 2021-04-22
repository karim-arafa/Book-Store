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


class Store(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=2048, null=True, blank=True)
    author = models.ForeignKey(User, null=True,blank=True, on_delete=models.CASCADE, related_name="store")
    categories = models.ManyToManyField(Category)
    tag = models.ForeignKey(Tag, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

class Isbn(models.Model):
    isbn_number = models.AutoField(primary_key=True)
    author_title = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    book_name= models.OneToOneField(Store, on_delete=models.CASCADE, null=True, blank=True)
    

    def __str__(self):
        return f"Isbn {self.isbn_number}  | Author {self.author_title}  | Book {self.book_name}"

