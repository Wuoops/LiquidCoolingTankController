import serial
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
import time

class ModbusFactory():
    def getConn(self,p,PORT):
        read = []
        alarm = ""
        try:
            # 设定串口为从站
            master = modbus_rtu.RtuMaster(serial.Serial(port=PORT,baudrate=9600, bytesize=8, parity=p, stopbits=1))
            master.set_timeout(5.0)
            master.set_verbose(True)

        except Exception as exc:
            print(str(exc))
            alarm = (str(exc))
        return master  ##如果异常就返回[],故障信息

    #将一次数据处理成合适的格式
    def formatData(self,data):
        dataDic = {'data':data,'time':time.time()}
        return dataDic

    def readData(self,master,startNum,length):
        read = master.execute(1, cst.READ_HOLDING_REGISTERS, startNum, length)
        data = self.formatData(read)
        return list(data)




#mod = ModbusFactory()
#ma,al = mod.getConn(p='N',PORT="/dev/ttyUSB0")
#for i in range(1,100):
#    read = mod.readData(master=ma,startNum=32,length=24)
#    print(read)

