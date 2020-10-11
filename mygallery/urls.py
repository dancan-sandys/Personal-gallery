from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.gallery, name='gallery'),
    url(r'^categories/$', views.categories, name='categories'),
    url(r'^image/(\d+)', views.image, name='image'),
    url(r'^category/(\d+)', views.category, name='category'),
    url(r'^search/$', views.search_results, name='search_results')

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)