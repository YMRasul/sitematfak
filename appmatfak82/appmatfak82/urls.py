from django.contrib import admin
from django.urls import path, include
from photo.views import pageNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('photo.urls')),  # Создать файл urls.py в папке photo
    path('', include('video_app.urls')),  # Создать файл urls.py в папке video_app
]


handler404 = pageNotFound # обработчик для страницы 404
                          # функцию pageNotFound добавим в photo.views.py
