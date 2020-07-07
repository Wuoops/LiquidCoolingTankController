from django.shortcuts import render


def setup(request):
    return render(request,'setup.html')
