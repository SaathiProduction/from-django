from django.shortcuts import render, redirect , HttpResponse

def home(request):
    return render(request, 'home.html')
    
def aboutus(request):
    return render(request, 'aboutus.html')

def team(request):
    return render(request, 'team.html')

def contactus(request):
    return render(request, 'contactus.html')