from django.shortcuts import render

# Create your views here.
<<<<<<< HEAD
def index(request):
    return render(request, 'vjapp/index.html')


def room(request, room_name):
    return render(request, 'vjapp/room.html', {
        'room_name': room_name
    })
=======
>>>>>>> parent of 9b1d3db (Merge pull request #15 from Vijay-0404/main)
