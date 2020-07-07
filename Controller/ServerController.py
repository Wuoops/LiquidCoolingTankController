import  subprocess
from util.Util import *
from dao.sqliteDb import sqlDao
import os
from dao.mongodbConn import MongoDao
from concurrent.futures import ThreadPoolExecutor
#用于获取bmc信息，写入数据库，该Controller可用于控制采集数据的间隔时间，数量等

class BmcController():
    threadNum = 10
    #根据节点连接信息生成用来获取sdr数据的shell并获取一条sdr
    def runShellToGetBmc(self,arg):
        nodeName = arg['nodeName']
        bmcresList = arg['bmcresList']
        print('run Shell to get BMC Success')
        ######################################################开启
        # p1 = subprocess.Popen(['ipmitool','-H',arg['bmcIpaddr'],'-U',arg['userName'],'-P',arg['pwd'],'sdr','>',nodeName])
        #########################################################
        #判断各个节点保存的临时BMC数据文件是否存在
        A= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        b = os.path.exists(str(A)+'/dao/bmcFile/'+nodeName)

        path = (str(A)+'/dao/bmcFile/'+nodeName)
        with  open(path) as f:
            bmcFile = f.readlines()
            f.close()
        # print(bmcFile)
        #匹配BMC文件,得到匹配后的数据列表
        resList = findUsefull(bmcresList,bmcFile)
        #将两个list合并为字典
        resDic = listToDict(bmcresList,resList)
        resDic['time'] = time.time()
        #将数据写入到数据库
        mdb = MongoDao()
        mdb.iniertOneData(colName=nodeName,data=resDic)



    #读取并写入MongoDB各个节点配置信息
    def getBmcInfo(self):
        pool = ThreadPoolExecutor(self.threadNum)
        sd = sqlDao()
        #循环获取bmc选中配置
        sql = 'select * from server_BmcCheckoutConf'
        checked = sd.getAll(sql)
        for i in checked:
            nodeUUID = (str(i[2]),)
            bmcConfId = (str(i[1]),)
            #根据选中配置ID查询BMC配置信息
            bmcInfosql = 'select * from server_BmcConfig where confId_id = ?'
            #BMC配置信息
            bmcres = sd.getAllP(bmcInfosql,bmcConfId)
            #将BMC配置改为grep开头的数组
            flist = formatBmcConf(bmcres)
            bmcresList = formatBmcresTolist(bmcres)
            # print(bmcresList)
            #根据nodeId查找节点的连接信息
            sql = 'select * from server_NodeInfo where uuid = ?'
            res = sd.getAllP(sql,nodeUUID)
            # print(res)
            nodeName = res[0][1]
            ipAddr = res[0][2]
            userName = res[0][4]
            pwd = res[0][5]
            status = res[0][6]
            remark = res[0][7]
            bmcIpaddr = res[0][8]
            # print(nodeName)
            #根据节点连接信息生成用来获取sdr数据的shell并获取一条sdr
            #开启多线程执行采集语句
            # self.runShellToGetBmc(ipAddr,userName,pwd,nodeName)
            arg ={'nodeName':nodeName,'ipAddr':ipAddr,'userName':userName,'pwd':pwd,'status':status,'remark':remark,'bmcresList':bmcresList,'bmcIpaddr':bmcIpaddr}
            #开启多线程执行采集语句并写入数据库
            pool.submit(self.runShellToGetBmc,arg)



        # return resList



bc = BmcController()
for  i in range(1000):
    time.sleep(1)
    resL = bc.getBmcInfo()
