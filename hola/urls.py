from django.conf.urls import url
from . import views

app_name = 'hola'

urlpatterns = [
    url(r'^$', views.indexView, name='index'),
]