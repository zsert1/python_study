from django.db import models

# Create your models here.
class Post(models.Model):
    message=models.TextField()
    photo=models.ImageField(blank=True,upload_to='instagram/post/%Y/%m/%d')
    is_public=models.BooleanField(default=False,verbose_name='공개여부')
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def message_lenght(self):
        return len(self.message)
    message_lenght.short_description="메세지 글자수"