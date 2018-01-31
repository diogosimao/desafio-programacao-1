from django.conf.urls import url
from .views import upload_file_view, income_view


urlpatterns = [
    url('^upload/', upload_file_view, name='upload'),
    url('^income/(?P<text_file_slug>[^\.]+)/$', income_view, name='income')
]

