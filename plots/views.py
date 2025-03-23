from django.shortcuts import render

def home(request):
    return render(request, 'plots/plots.html')