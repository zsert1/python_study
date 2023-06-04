from django.db import models
from django.conf import settings
# Create your models here.
class Post(models.Model):
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    message=models.TextField()
    tAG_set=models.ManyToManyField('Tag',blank=True)
    photo=models.ImageField(blank=True,upload_to='instagram/post/%Y/%m/%d')
    is_public=models.BooleanField(default=False,verbose_name='공개여부')
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def message_lenght(self):
        return len(self.message)
    class Meta:
        ordering=['-id']
    message_lenght.short_description="메세지 글자수"


class Comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    message=models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name=models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name
   