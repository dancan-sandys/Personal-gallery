from . import views
from django.conf.urls import url
from django.conf import settings


urlpatterns = [
    url(r'^$', views.gallery, name='gallery'),
    url(r'^categories/$', views.categories, name='categories'),
    url(r'^image/(\d+)', views.image, name='image')
    url(r'^category/(\d+)', views.category, name='category')

]
