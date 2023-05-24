from django.db import models

# Create your models here.
class Post(models.Model):
    message=models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def message_lenght(self):
        return len(self.message)
    message_lenght.short_description="메세지 글자수"