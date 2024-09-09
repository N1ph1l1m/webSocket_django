from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def test(request):
    return HttpResponse ('Channels')


def index(request):
    return render(request, 'chat/channelindex.html')


def room(request, room_name):
    return render(request, 'chat/channelroom.html', {'room_name':room_name})
