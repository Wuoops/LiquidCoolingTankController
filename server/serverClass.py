from dao.sqliteDb import sqlDao
from dao.mongodbConn import MongoDao
from util.Util import datasetForServer,datasetForCpu
#服务器类用于对接服务器节点
class ServerClass():
    #读取某一个节点的N条数据
    def readOneBmcDate(self,nodeId,num):
        sd = sqlDao()
        nodeUUID = (str(nodeId),)
        sql = 'select * from server_NodeInfo where uuid = ?'
        res = sd.getAllP(sql,nodeUUID)
        # print(res)
        nodeName = res[0][1]
        # print(nodeName)
        mdb = MongoDao()
        req = mdb.selectLast(nodeName,num)
        # print(req)
        #将数据调整为dataset可用的数据格式
        data = datasetForServer(req)
        return data
    #根据配置从数据库读取n条数据
    def readBmcData(self,num):
        resList = []
        sd = sqlDao()
        #循环获取bmc选中配置
        sql = 'select * from server_BmcCheckoutConf'
        checked = sd.getAll(sql)
        for i in checked:
            nodeUUID = (str(i[2]),)
            sql = 'select * from server_NodeInfo where uuid = ?'
            res = sd.getOneP(sql,nodeUUID)
            # print(res)
            nodeName = res[1]
            # print(nodeName)
            mdb = MongoDao()
            req = mdb.selectLast(nodeName,num)
            # print(req)
            #将数据调整为dataset可用的数据格式
            data = datasetForServer(req)

            resList.append(data)

        return resList

    #读取配置信息返回配置列表
    def readConf(self):
        resList = []
        sd = sqlDao()
        #循环获取bmc选中配置
        sql = 'select * from server_BmcCheckoutConf'
        checked = sd.getAll(sql)
        confList = []
        for i in checked:
            nodeUUID = (str(i[2]),)
            sql = 'select * from server_NodeInfo where uuid = ?'
            res = sd.getOneP(sql,nodeUUID)
            # print(list(res))

            confList.append(list(res))
        return confList

    #获取一次CPU数据
    def getCpuData(self,cpu0,cpu1):
        resList = []
        sd = sqlDao()
        #循环获取bmc选中配置
        sql = 'select * from server_BmcCheckoutConf'
        checked = sd.getAll(sql)
        reqList = []
        nodeList = ['node']
        for i in checked:
            nodeUUID = (str(i[2]),)
            sql = 'select * from server_NodeInfo where uuid = ?'
            res = sd.getOneP(sql,nodeUUID)
            # print(res)
            nodeName = res[1]
            nodeList.append(nodeName)
            mdb = MongoDao()
            req = mdb.selectLast(nodeName,1)
            reqList.append(req)
        #将数据调整为dataset可用的数据格式（用于CPU）
        return  datasetForCpu(reqList,nodeList,cpu0,cpu1)

    #CPU关键字获取
    def cpuKeyWord(self):
        resList = []
        sd = sqlDao()
        #循环获取bmc选中配置
        sql = 'select * from server_BmcCheckoutConf'
        checked = sd.getAll(sql)
        confUUId = (str(checked[0][1]),)
        sql = 'select * from server_bmcconfig where confid_id = ?'
        res = sd.getAllP(sql,confUUId)


        for conf in res:
            if (conf[2]) == 'cpu0temp':
                cpu0 = conf[1]
            elif (conf[2]) == 'cpu1temp':
                cpu1 = conf[1]

        return cpu0,cpu1
    #根据节点uuid查询节点详情
    def getNodeInfo(self,nodeUuid):
        sql = 'select * from server_nodeinfo where uuid = ?'
        uuid = [str(nodeUuid),]
        sd = sqlDao()
        nodeinfo = sd.getOneP(sql,uuid)

        return (nodeinfo)
#
# sc = ServerClass()
# sc.getNodeInfo('2')
