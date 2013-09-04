from ctypes import *
import binascii

'''
typedef struct canFrameStruct
{
	uint8 info;
	uint8 sig[4];
	uint8 canData[8];
}canFrameStruct;
'''


class RSDataPaser():
    DATA_STARTER = "$KA"
    DATA_SPLITER = ","
    DATA_ENDER = "*"

    def __init__(self):
        self.rawDataList = []
        return

    def doPaser(self, data):
        dataLeft = data

        while self.__class__.DATA_STARTER in dataLeft and self.__class__.DATA_ENDER in dataLeft:
            startIndex = dataLeft.index(self.__class__.DATA_STARTER)
            endIndex = dataLeft.index(self.__class__.DATA_ENDER)

            starterSize = len(self.__class__.DATA_STARTER)
            enderSize = len(self.__class__.DATA_ENDER)

            #print
            #print "startIndex", startIndex

            if startIndex < endIndex:
                rawData = dataLeft[startIndex + starterSize:endIndex].replace(self.__class__.DATA_SPLITER, "")
                dataLeft = dataLeft[endIndex + enderSize:]
                self.rawDataList.append(rawData)

                #print "doPaser, raw: ", rawData
                #print "left:[%s]" % dataLeft


        #print "before return"
        return dataLeft, self.rawDataList




class CAN_DATA(Structure):
    _fields_ = [("info", c_ubyte),
                ("sig", c_ubyte*4),
                ("canData", c_ubyte*8)]


class CanProxy():
    def __init__(self, CanData=None, Sender=None):

        self.canData = CanData
        self.dataSender = Sender
        self.receivedData = ""
        self.receivedRawDataList = []
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
        self.receivedData += data
        #print "[%s]" % self.receivedData

        paser = RSDataPaser()
        self.receivedData, returenRawDataList = paser.doPaser(self.receivedData)

        for index, elem in enumerate(returenRawDataList):
            print
            print "##################"
            print "received:",index, elem
            self.receivedRawDataList.append(elem)
        #print "receiveSerialRawData"
        #print self.printHex(data)

            self.dumpAllRawData()

    def dumpAllRawData(self):
        print
        print "dump all raw data:"
        for index, elem in enumerate(self.receivedRawDataList):
            print index, elem

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