import time
import random
from util.Util import timeStempForShow
class ModbusFactory():
    def getConn(self,p,PORT):
        al=''
        if p == 'N':
            master='Thermal'
        else:
            master='CDU'
        return master

    #将一次数据处理成合适的格式
    def formatData(self,data):
        dataDic = {'data':data,'time':time.time()}
        return dataDic
    #获取一次数据读取
    def readData(self,master,startNum,length):

        if master == 'Thermal':
            read = [random.randint(450,500), random.randint(500,530), random.randint(400,500), random.randint(450,480), 64536, 64536, 64536, 64536, 64536, 64536, 64536, 64536, 64536, 64536, 64536, 64536, 64536, 64536, 64536, 64536, 64536, 64536, 64536, 64536]
            data = self.formatData(read)
        else:
            read = [44, 39, 156, 161, 176, 45, 81, 199, 87, 2300, 2293, 2305, 310, 100, 80, 33, 0, 0, 0]
            data = self.formatData(read)

        return data


#
# from dao.mongodbConn import MongoDao
# mdb = MongoDao()
#
# mod = ModbusFactory()
# ma = mod.getConn(p='N',PORT="/dev/ttyUSB0")
#
# for i in range(1,100):
#     read = mod.readData(master=ma,startNum=32,length=24)
# #
# #     dataDic = {'data':read,'time':time.time()}
#     print(read)
# #     mdb.iniertOneData('test',dataDic)
#
# #
# # dic = mdb.selectMany('test',{'time':1584004627.4233627})
# #
# #
# #
# # timeString = dic[0]['time']
# # timeArray = timeStempForShow(timeString)
# # print(timeArray)
