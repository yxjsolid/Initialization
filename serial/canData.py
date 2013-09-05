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


class RSDataFormater():
    DATA_STARTER = "$KA"
    DATA_SPLITER = ","
    DATA_ENDER = "*"

    def __init__(self):
        self.rawDataList = []
        return

    def doPaser(self, dataIn):
        dataLeft = dataIn

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


    def doConstruct(self, dataIn):
        dataOut = self.__class__.DATA_STARTER + self.__class__.DATA_SPLITER

        for index,ch in enumerate(dataIn):
            dataOut += chr(ch)
            if index%2 > 0:
                dataOut += self.__class__.DATA_SPLITER

        print dataOut
        print len(dataIn)

        if len(dataIn)%2 != 0:
            dataOut += self.__class__.DATA_SPLITER

        dataOut += self.__class__.DATA_ENDER
        return dataOut

class CAN_DATA(Structure):
    _fields_ = [("info", c_ubyte),
                ("sig", c_ubyte*4),
                ("canData", c_ubyte*8)]


    def sturctureToByteArray(self):
        byteArray = bytearray(sizeof(CAN_DATA))
        canBuff = (c_ubyte*sizeof(CAN_DATA))()
        memmove(byref(canBuff), byref(self), sizeof(CAN_DATA))

        for index, elem in enumerate(canBuff):
            byteArray[index] = elem

        print "can data raw:[%r]" % byteArray
        return byteArray

    def buildTestData(self):
        self.info = ord('a')
        self.sig[0] = ord('b')
        self.sig[1] = ord('c')
        self.sig[2] = ord('d')
        self.sig[3] = ord('e')

        val = ord('f')
        for i in range(8):
            self.canData[i] = val + i


class CanProxy():
    def __init__(self, CanData=None, SerialHandler=None):

        self.serialHandler = SerialHandler
        self.canData = CanData
        self.receivedData = ""
        self.receivedRawDataList = []
        return

    def serialSendCanData(self, canData):

        #serialData = canData.

        dataArray = canData.sturctureToByteArray()


        dataArray = RSDataFormater().doConstruct(dataArray)


        if self.serialHandler:
            self.serialHandler.SendData(dataArray)

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

        formater = RSDataFormater()
        self.receivedData, returenRawDataList = formater.doPaser(self.receivedData)

        for index, elem in enumerate(returenRawDataList):
            print
            print "##################"
            print "received:",index, elem
            self.receivedRawDataList.append(elem)
        #print "receiveSerialRawData"
        #print self.printHex(data)

            self.dumpAllRawData()

    def serialSendCanDataTest(self):

        #data = getSomeCanTestData()

        canDataTest = CAN_DATA()
        canDataTest.buildTestData()

        self.serialSendCanData(canDataTest)
        return


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



def getSomeCanTestData():
    canTest = CAN_DATA()
    canTest.buildTestData()
    buf = canTest.sturctureToByteArray()
    print "getSomeCanTestData 1 ", buf

    formater = RSDataFormater()
    data1 = formater.doConstruct(buf)

    print "getSomeCanTestData 2 ", data1

if __name__ == '__main__':

    canTest = CAN_DATA()
    canTest.buildTestData()

    buf = canTest.sturctureToByteArray()
    print buf



    formater = RSDataFormater()
    data1 = formater.doConstruct(buf)

    print data1