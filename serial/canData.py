from ctypes import *


'''
typedef struct canFrameStruct
{
	uint8 info;
	uint8 sig[4];
	uint8 canData[8];
}canFrameStruct;
'''

class CAN_DATA(Structure):
    _fields_ = [("info", c_ubyte),
                ("sig", c_ubyte*4),
                ("canData", c_ubyte*8)]


can = CAN_DATA()
print sizeof(can)


can.info = 0x62
can.sig[0] = 0x63







buffer=(c_ubyte*sizeof(CAN_DATA))()


buffer[0] = 9

myaa = range(9)

for index,num in enumerate(myaa):
    buffer[index] = num

print buffer[0]
print buffer[1]
print buffer[2]
memmove(byref(can), byref(buffer), sizeof(can))
print "can.info", can.info



class CanProxy():
    def __init__(self, CanData=None, Sender=None):

        self.canData = CanData
        self.dataSender = Sender
        return

    def sendCanData(self):
        if self.dataSender:
            self.dataSender(self.canData)

    def receiveCanData(self, bufIn, bufSize):
        if bufSize > sizeof(CAN_DATA):
            print "CanProxy-> bufIn size too large"
            return 0

        canBuff = (c_ubyte*sizeof(CAN_DATA))()
        for index,num in enumerate(bufIn):
            canBuff[index] = num
        memmove(byref(self.canData), byref(canBuff), sizeof(CAN_DATA))

        self.dumpCanData()
        return 1

    def receiveSerialRawData(self, data):
        print "receiveSerialRawData"
        print self.printHex(data)

    def dumpCanData(self):
        if self.canData is None:
            print "CanProxy->dumpCanData error canData is Null"
            return

        print "info = ", self.canData.info
        for index,num in enumerate(canData.sig):
            print "sig[%d] = %x" % (index, num)

        for index,num in enumerate(canData.canData):
            print "canData[%d] = %x" % (index, num)


    def printHex(self, s):
        s1 = binascii.b2a_hex(s)
        print s1