from django.urls import path, re_path, register_converter
from . import views


class YearConverter:
    regex = r"20\d{2}"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return "%04d" % value


register_converter(YearConverter, 'year')

app_name='instagram' # URL Reverse에서 namespace역할을 하게된다
urlpatterns = [
    path('', views.post_list),
    path('<int:pk>/', views.post_detail),
    path('archives/<year:year>/', views.archives_years)
    # re_path(r'archives/(?P<year>\d{4})/', views.archives_years)

]
