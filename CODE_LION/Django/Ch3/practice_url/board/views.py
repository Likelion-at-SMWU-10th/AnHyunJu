from django.shortcuts import render

# Create your views here.
def boardlist(request):
    return render(request, 'boardlist.html')

def boardfirst(request):
    return render(request, 'boardfirst.html')
