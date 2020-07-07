from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
def cdu(request):
    return render(request,'tank.html')

def getLevel(request):

    return HttpResponse(89)
