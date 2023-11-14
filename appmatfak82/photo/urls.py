import about as about
from django.urls import path, re_path
from appmatfak82 import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('category/', show_category, name='category'),
    path('category/<int:cat_id>/', show_category_all, name='category'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]

# Добавление  [***] от appmatfak82.setttins
if settings.DEBUG:  # from appmatfak82 import settings
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#  для static from django.conf.urls.static import settings
