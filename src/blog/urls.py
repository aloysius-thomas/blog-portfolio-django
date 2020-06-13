from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('details', views.blog_details, name='blog-details'),

]
