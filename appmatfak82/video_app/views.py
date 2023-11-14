from django.http import StreamingHttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Video
from .services import open_file

def videoapp(request):
    return HttpResponse('<h1>Страница не найдена</h1>')  # должны импортировать эту функцию


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')  # должны импортировать эту функцию

def get_list_video(request):
    return render(request, 'videoapp/video_hosting/home.html', {'video_list': Video.objects.all()})

def get_video(request, pk: int):
    _video = get_object_or_404(Video, id=pk)
    return render(request, "videoapp/video_hosting/video.html", {"video": _video})

def get_streaming_video(request, pk: int):
    file, status_code, content_length, content_range = open_file(request, pk)
    response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')

    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response



