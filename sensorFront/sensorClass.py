import datetime
from dao.sqliteDb import *
from dao.mongodbConn import *
from util.Util import *

class SensorModel():


    #获取传感器配置信息
    def getConf(self):
        #获取传感器模块数量
        #获取选中的传感器配置和数量
        sd = sqlDao()
        choicedConf = sd.getChoicedConf()
        #配置字典
        confDic={}
        #配置列表
        confList=[]

        for i in choicedConf:
            arg = []
            #1-根据设备uuid得到设备名称和设备路径
            dev = sd.getDevPath(str(i[0]),)
            devId = dev[0]
            devPath = dev[1]
            devName = dev[2]
            confName = sd.getConfName(str(i[1]))[1]
            # print(devPath)
            # print(devName)
            # print(confName)
            conf = sd.getSensorConf(str(i[1]))
            sensorNum = conf.__len__()
            #2-将这下打包放到字典当中
            confDic = {'devName':devName,'devPath':devPath,'confName':confName,'sensorNum':sensorNum}
            confList.append(confDic)
        # print(confList)

        return confList
    #获取传感器最后n条数据
    def sonsor(self,num):
        #获取传感器模块数量
        #获取选中的传感器配置和数量
        sd = sqlDao()
        choicedConf = sd.getChoicedConf()
        choiceNum = (choicedConf.__len__())
        datasetList = []
        dataset = []
        for i in choicedConf:
            arg = []
            #1-根据设备uuid得到设备名称和设备路径
            dev = sd.getDevPath(str(i[0]),)
            devId = dev[0]
            devPath = dev[1]
            devName = dev[2]
            # print(devName)
            #2-根据配置uuid获取配置关系列表
            conf = sd.getSensorConf(str(i[1]))
            # print(dev)
            # print(conf)
            #3-根据设备名称查询num条数据并整理
            mdb = MongoDao()
            list = mdb.selectLast(dev[2],num)
        # 4-处理成规范的格式
            dataset.append(datasetSourceList(conf,list))

        timeLine = []
        timeLine.append('Time')
        for k in list:
            ti = k['time']
            timeLine.append(timeStempForShowTime(ti))
        datasetList.append(timeLine)
        for i in dataset:
            for j in i:
                datasetList.append(j)
        return datasetList
#
#
# sm = SensorModel()
# datasetList = sm.sonsor(10)
# for i in datasetList:
#     print(i)
