from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

#from webSocket.chat.models import Room


# Create your views here.
def test(request):
    return HttpResponse ('Chat')


# def index(request):
#     if request.method == "POST":
#         name = request.POST.get("name", None)
#         if name:
#             room = Room.objects.create(name=name, host= request.user)
#             print(room.pk)
#             return HttpResponseRedirect(reverse("room",kwargs={"pk":room.pk}))
#     return render(request, 'chat/channelindex.html')
#
#
# def room(request,pk):
#     room: Room = get_object_or_404(Room,pk=pk)
#     return  render(request,'chat/channelroom.html', {
#         'room':room,
#     })


