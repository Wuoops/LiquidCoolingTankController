from django.shortcuts import render
from server.serverClass import *
from django.http import JsonResponse
from dao.serverDao import getNodeUUId
def server(request):
    sc = ServerClass()
    confList = sc.readConf()
    # print(confList)
    return render(request,'server.html',{'confList':confList})


def getBmcData(request):
        line = request.POST.get('line')
        sc = ServerClass()
        node = str(request.POST.get('node'))
        nodeUuid = getNodeUUId(node)
        data = sc.readOneBmcDate(str(nodeUuid),int(line))
        jsonData = {'data':data}
        return JsonResponse(jsonData)

##########
######CPU表数据更新(注意在BMC配置表CPU的关键字描述，为cpu0temp和cpu1temp的关键字用于图表数据提取)

def getcpuData(request):
    sc = ServerClass()
    #CPU关键字获取
    cpu0,cpu1=sc.cpuKeyWord()
    #获取CPU最大值
    sc = ServerClass()
    data = sc.getCpuData(cpu0,cpu1)

    jsonData={'data':data}
    return JsonResponse(jsonData)


#节点详情页
def serverNode(request):
    node = request.GET.get('node')
    #根据节点uuid查询节点详情
    sc = ServerClass()
    nodeInfo = list(sc.getNodeInfo(node))
    print(nodeInfo)

    return render(request,'serverNode.html',{'nodeInfo':nodeInfo})
