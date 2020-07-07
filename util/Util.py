import time
import re

#用于合并两个list
def listToDict(list1=list,list2=list):
    len = list1.__len__()
    dict={}
    for i in range(len):
        dict[list1[i]]=list2[i]
    return dict
#用于去掉字符串中的特殊符号
def clearStr(s=str):
    return s.replace('\'','')

#用于将时间戳改为用于展示的时间格式
def timeStempForShow(timeStemp):
    timeString = timeStemp
    timeArray = time.localtime(timeString)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)

    return otherStyleTime
#用于将时间戳改为用于展示的时间格式(只包含时间)
def timeStempForShowTime(timeStemp):
    timeString = timeStemp
    timeArray = time.localtime(timeString)
    otherStyleTime = time.strftime("%H:%M:%S", timeArray)

    return otherStyleTime

#将配置和数据转换为dataset可用的数据格式(用于sensor)
def datasetSourceList(confList,dataList):

    datasetLine = []
    for i in confList:
        dataLine = []
        dataLine.append(i[1])
        for j in dataList:
            if j['data'][i[0]-1] == 64536 :
                dataLine.append(-1)

            else:
                # print(format((j['data'][i[0]-1])*0.1,'.1f'))
                dataLine.append(format((j['data'][i[0]-1])*0.1,'.1f'))
        datasetLine.append(dataLine)
    return datasetLine


#将BMC配置改为grep开头的数组
def formatBmcConf(bmclist):
    flist = []
    flist.append('grep')
    for i  in bmclist:
        flist.append('-e')
        flist.append(str(i[1]))

    return flist
    # print(flist)

#将BMCres处理成配置列表

def formatBmcresTolist(bmclist):
    resList = []
    for i in bmclist:
        resList.append(str(i[1]))

    return resList

#匹配BMC文件,得到匹配后的数据列表
def findUsefull(bmcresList,bmcFile):
    resList = []
    for kw in bmcresList:
        # print(bmcresList.index(i))
        for file in bmcFile:
            pattern = re.compile(kw)
            result = pattern.findall(file)
            if result != []:

                resList.append(re.sub('\D','',file.strip().split("|")[1].split()[0]))
    return resList
#将数据调整为dataset可用的数据格式（用于server)
def datasetForServer(req):
    timeLine = []
    timeLine.append('Time')
    dataLine = []
    for i in req:
        keyLine = []
        dataTemp = []
        for key in i:
            if key == 'time':
                #处理成时间轴数组数据
                ti =timeStempForShowTime(i['time'])
                timeLine.append(ti)
            else:
                if i[key] != 'no':
                    keyLine.append(key)
                    dataTemp.append(i[key])
        dataLine.append(dataTemp)

    # print(timeLine)
    # print(keyLine)
    # print(dataLine)
    data = []
    data.append(timeLine)
    for i in range(len(keyLine)):
        dataA=[]
        dataA.append(keyLine[i])
        for j in range(len(dataLine)):
            dataA.append(dataLine[j][i])
        data.append(dataA)
    return data

#将数据调整为dataset可用的数据格式（用于CPU）
def datasetForCpu(reqList,rList,cpu0,cpu1):
    resList=[]
    resList.append(rList)
    cpu0List = ['CPU0']
    cpu1List = ['CPU1']
    for req in reqList:
        cpu0List.append(req[0][cpu0])
        cpu1List.append(req[0][cpu1])

    resList.append(cpu0List)
    resList.append(cpu1List)
    return resList
