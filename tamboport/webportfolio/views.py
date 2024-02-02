from django.shortcuts import render

def Home(request): return render(request, 'pages/Home.html')

def About(request): return render(request, 'pages/About.html')

def Info(request): return render(request, 'pages/projek.html')


