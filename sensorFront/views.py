from django.shortcuts import render
from django.http import JsonResponse
from sensorFront.sensorClass import SensorModel
#sensor页面
def sensor(request):
    #直接从sensorclass中获取传感器模块信息列表

    sm = SensorModel()
    modelList = sm.getConf()

    return render(request,'sensorV4.html',{'modelList':modelList})


def getSensorData(request):

    line = request.POST.get('line')
    sm = SensorModel()
    data = sm.sonsor(int(line))

    jsonData = {'data':data}
    return JsonResponse(jsonData)
