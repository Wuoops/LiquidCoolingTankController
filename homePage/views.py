from django.shortcuts import render
from server.serverClass import ServerClass
#主页访问
def homepage(request):
    sc = ServerClass()
    confList = sc.readConf()
    return render(request,'homePageV4.html',{'confList':confList})

def homePage(request):
    sc = ServerClass()
    confList = sc.readConf()
    return render(request,'homePageV4.html',{'confList':confList})


sc = ServerClass()
confList = sc.readConf()
print(confList)
