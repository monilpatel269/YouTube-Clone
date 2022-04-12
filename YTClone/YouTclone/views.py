from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request,'YouTclone/index.html')

def video(request):
    return render (request,'YouTclone/video.html')

def explore(request):
    return render (request,'YouTclone/explore.html')

def subscription(request):
    return render (request,'YouTclone/subscription.html')

def originals(request):
    return render (request,'YouTclone/originals.html')

def music(request):
    return render (request,'YouTclone/music.html')

def library(request):
    return render (request,'YouTclone/library.html')

def search(request):
    return render (request,'YouTclone/search.html')

def create(request):
    return render (request,'YouTclone/create.html')

def menu(request):
    return render (request,'YouTclone/menu.html')

def notifications(request):
    return render (request,'YouTclone/notifications.html')

def userprofile(request):
    return render (request,'YouTclone/userprofile.html')