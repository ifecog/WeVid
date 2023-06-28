from django.shortcuts import render

# Create your views here.
def lobby(request):
    return render(request, 'screens/lobby.html')

def room(request):
    return render(request, 'screens/room.html')

