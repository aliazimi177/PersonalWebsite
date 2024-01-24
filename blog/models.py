from django.db import models

# Create your models here
class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories"
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")
    image = models.ImageField(upload_to='blog/%Y/%m/%d',null=True)
 
    def __str__(self) -> str:
        return self.title
    
class Comment(models.Model):
    author = models.CharField(max_length=50)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} on '{self.post}'"


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} from {self.email}"
