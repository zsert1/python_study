from django.contrib import admin
from .models import Post

# admin.site.register(Post)
# # Register your models here.

# class PostAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Post,PostAdmin)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['id','message','message_lenght','create_at','update_at']
    list_display_links=['message']
    
    # def message_lenght(self,post):
    #     return len(post.message)
    
    def message_lenght(self,post):
        return f"{len(post.message)} 글자"
    
