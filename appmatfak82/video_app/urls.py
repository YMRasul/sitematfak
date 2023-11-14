from django.urls import path
#from .import views
from django.conf.urls.static import static
from appmatfak82 import settings
from .views import *

urlpatterns = [
    path('videos/', get_list_video, name='videoapp'),
#    path('videos/', get_list_video, name='videoapp'),
    path('stream/<int:pk>/', get_streaming_video, name='stream'),
    path('videos/<int:pk>/', get_video, name='video'),
]

# Добавление  [n3] от mywork.setttins
if settings.DEBUG:  # from mywork import settings
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #  для static from django.conf.urls.static import settings

handler404 = pageNotFound
