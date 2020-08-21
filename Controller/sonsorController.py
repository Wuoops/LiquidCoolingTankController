from dao.sqliteDb import sqlDao
from concurrent.futures import ThreadPoolExecutor
import time
from dao.mongodbConn import MongoDao
from dao.sensorDaoTest import  ModbusFactory
#用于写入数据到数据库
#间隔时间设置
sleepTime= 1
##传感器类处理模块类
def writeToDB(arg):
    devName = arg[0]
    RuntimeLong = arg[1]
    # print(devName)
    #获取到设备名称
    mdb = MongoDao()
    # mdb.selectMany(devName)

    #获取一次数据
    mf = ModbusFactory()
    ma = mf.getConn(p='N',PORT="/dev/ttyUSB0")
    # print(dataDic)
    #以设备名称作为表名称持续插入
    for i in range(RuntimeLong):
        dataDic = mf.readData(master=ma,startNum=32,length=24)
        # print(devName)
        mdb.iniertOneData(str(devName),dataDic)
        time.sleep(sleepTime)
        # print(devName)

        # print(mdb.selectAll(str(devName)))

class CensorController():

    def startSensorLog(self,RuntimeLong):
        #获取处理器核心数量
        #线程池线程数量配置
        pool = ThreadPoolExecutor(30)
        sd = sqlDao()
        #获取选中的传感器配置和数量
        choicedConf = sd.getChoicedConf()
        choiceNum = (choicedConf.__len__())
        for i in choicedConf:
            arg = []
            #1-根据设备uuid得到设备名称和设备路径
            dev = sd.getDevPath(str(i[0]),)
            devId = dev[0]
            devPath = dev[1]
            devName = dev[2]
            #2-根据配置uuid获取配置关系列表
            conf = sd.getSensorConf(str(i[1]))
            # print(conf)
            # print(i)
            #3-开始根据获取到的数据实例化sensorClass
                #开启线程记录数据
            # while True:

            arg.append(devName)
            arg.append(RuntimeLong)
            pool.submit(writeToDB,arg)

        return pool




c = CensorController()
#启动数据采集脚本参数为采集数量
po = c.startSensorLog(600)
