import pymongo

MongoAddr = "mongodb://localhost:27017/"
Dbname = "LcpDataBase"

#MongoDB操作dao层
class  MongoDao():
    #获取连接
    def __init__(self):
        self.conn = pymongo.MongoClient(MongoAddr)
        self.db = self.conn[Dbname]

    #插入一条数据到数据库
    #提供需要插入的表，一条数据返回是否成功
    def iniertOneData(self,colName,data):
        self.col = self.db[colName]
        self.col.insert_one(data)
    #根据条件查询数据(colName为查询的表，arg为字典数据类型的查询条件
    def selectMany(self,colName,arg):
        list = []
        self.col = self.db[colName]
        x = self.col.find(arg,{'_id':0})
        for i in x:
            print(i)
            list.append(i)
        return list
    #查询一个表的全部数据
    def selectAll(self,colName):
        list = []
        self.col = self.db[colName]
        x = self.col.find({},{'_id':0})
        for i in x:
            # print(i)
            list.append(i)
        return list

    #查询最后n条数据
    def selectLast(self,colName,num):
        list = []
        self.col = self.db[colName]
        x = self.col.find({},{'_id':0}).skip(self.col.count() - num )
        for i in x:
            # print(i)
            list.append(i)
        return list

    #断开连接
    def closeMongoConn(self):
        pass
#
#
# nodeName = 'Node1'
# # resDic = {'Inlet_Temp': 'no', 'CPU0_Temp': '14', 'CPU1_Temp': '15', 'CPU0_Margin_Temp': '77', 'CPU1_Margin_Temp': '76', 'PS1_Power': '40', 'PS2_Power': '40', 'PCH_Temp': '18', 'DIMMG0_Temp': '16'}
# #
# mdb = MongoDao()
# mdb.iniertOneData(nodeName,{'s':'a'})
# a = mdb.selectAll(nodeName)
# # a = mdb.iniertOneData(nodeName,resDic)
# print(a)
