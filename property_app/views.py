from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'public/index.html')

def about(request):
    return render(request, 'public/about.html')

def agents(request):
    return render(request, 'public/agent.html')

def agent_dashboard(request):
    return render(request, 'public/dashboard.html')