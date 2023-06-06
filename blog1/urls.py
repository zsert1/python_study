
from django.urls import path, include
from . import views

app_name='blog1' # URL Reverse에서 namespace역할을 하게된다
urlpatterns=[ 
    path('',views.post_list,name='post_list'), 
    
]