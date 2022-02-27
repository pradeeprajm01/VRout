from django.shortcuts import render

def index(request):
    return render(request, 'kumar/index.html')

def room(request, room_name):
    return render(request, 'kumar/room.html', {
        'room_name': room_name
    })