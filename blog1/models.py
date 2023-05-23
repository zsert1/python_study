from django.db import models

class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    create_at=models.DateField(auto_now_add=True)
    update_at=models.DateField(auto_now=True)

# Create your models here.
