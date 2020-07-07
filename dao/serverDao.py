from dao.sqliteDb import sqlDao
#跟节点名称获取节点编号
def getNodeUUId(nodeName):
    nName = [nodeName,]
    sql = 'select UUID from server_NodeInfo where nodename = ?'
    db = sqlDao()
    uuid = db.getOneP(sql,nName)
    return uuid[0]

