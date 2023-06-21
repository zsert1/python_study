from django.http import HttpResponse,Http404
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView
post_list = ListView.as_view(model=Post)

# def post_list(request):
#     qs = Post.objects.all()
#     q = request.GET.get('q', '')
#     if q:
#         qs = qs.filter(message__icontains=q)
#     # instagram/templates/instagram/post_list.html
#     return render(request, 'instagram/post_list.html', {
#         "post_list": qs,
#         'q': q, })
# request.POST
# request.FILES
# Create your views here.


# def post_detail(request, pk):
#     reponse = HttpResponse()
#     reponse.write('helloWord')
#     return reponse

    # reponse = HttpResponse()
    # reponse.write('helloWord')
    # return reponse
# def post_detail(request:HttpResponse, pk:int)->HttpResponse:
#     try:
#       post=Post.objects.get(pk=pk)
#     except Post.DoesNotExist:
#       raise Http404
#     return render(request,'instagram/post_detail.html',{'post':post})
post_detail=DetailView.as_view(model=Post)
def archives_years(request,year):
    return HttpResponse(f"{year}년 archive")


