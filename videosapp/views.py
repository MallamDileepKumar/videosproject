from django.shortcuts import render,redirect
from .models import Video

# Create your views here.
def display(request):
    videos = Video.objects.all()
    print(videos)

    return render(request,'videos.html',context={'videos':videos})
def upload(request):
    if request.method == 'POST':
        title = request.POST["title"]
        video = request.POST["video"]
        videos = Video(Title = title,video = video)

        videos.save()
        return redirect('videos')
    return render(request,template_name='upload.html')

