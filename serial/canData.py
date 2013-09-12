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


"""
typedef struct  {
BYTE  id[4];
BYTE  data[8];            //channel
BYTE  len;                //
BYTE  ch;                 // 0xff:config
BYTE  format;             // 00:sff  01:eff
BYTE  type;               // 00:data 01:far
BYTE  checkSum
}  CAN_msg;
"""
class USB2CAN_DATA(Structure):
    _fields_ = [("id",      c_ubyte*4),
                ("data",    c_ubyte*8),
                ("len",     c_ubyte),
                ("ch",      c_ubyte),
                ("format",  c_ubyte),
                ("type",    c_ubyte),
                ("checkSum",c_ubyte)]

    def __init__(self):

        Structure.__init__(self)
        self.formater = USB2CANFormater()
        return

    def getByteArray(self):
        checkSum = c_ubyte(0)

        byteArray = bytearray(sizeof(USB2CAN_DATA))
        dataBuffer = (c_ubyte*sizeof(USB2CAN_DATA))()
        memmove(byref(dataBuffer), byref(self), sizeof(USB2CAN_DATA))

        for index, elem in enumerate(dataBuffer):
            byteArray[index] = elem
            if index != sizeof(USB2CAN_DATA)-1:
                checkSum.value += elem
            else:
                byteArray[index] = checkSum.value
                self.checkSum = checkSum.value

        print "can data raw:[%r]" % byteArray
        return byteArray

    def buildTestData(self):
        self.id[0] = 0
        self.id[1] = 0
        self.id[2] = 0
        self.id[3] = 0
        self.len = 8
        self.ch = 0x66
        self.format = 1
        self.type = 0

        val = 0xaa
        for i in range(8):
            self.data[i] = val

    def dumpDataToSend(self):
        return self.formater.genDataToSend(self.getByteArray())


class USB2CANFormater():
    def __init__(self):
        self.m_FrameHead = 0xAA
        self.m_FrameTail = 0x55
        self.m_FrameCtrl = 0xA5
        self.m_FrameSpecial = [self.m_FrameHead, self.m_FrameTail, self.m_FrameCtrl]
        self.receivedByteArray = None

        return

    def genDataToSend(self, dataIn):
        arrayToSend = bytearray()
        arrayToSend.append(self.m_FrameHead)
        arrayToSend.append(self.m_FrameHead)

        for index,dataByte in enumerate(dataIn):
            if dataByte in self.m_FrameSpecial:
                arrayToSend.append(self.m_FrameCtrl)
            arrayToSend.append(dataByte)

        arrayToSend.append(self.m_FrameTail)
        arrayToSend.append(self.m_FrameTail)

        print "byteArray %r" % arrayToSend
        return arrayToSend


    def getFrameFromRawData(self, rawFrame):
        specialStr = chr(self.m_FrameCtrl) + chr(self.m_FrameCtrl)
        startStr = chr(self.m_FrameHead) + chr(self.m_FrameHead)
        endStr = chr(self.m_FrameTail) + chr(self.m_FrameTail)

        rawFrame = rawFrame.replace(startStr, "")
        rawFrame = rawFrame.replace(endStr, "")
        rawList = []
        for elem in rawFrame.split(specialStr):
            newelem = elem.replace(chr(self.m_FrameCtrl), "")
            rawList.append(newelem)

        sep= chr(self.m_FrameCtrl)
        rawList = sep.join(rawList)


        print "rawList:"
        print "%r " % rawList





    def checkRawFrameData(self, frame):
        dataLeft = ""
        validFrame = None

        startStr = chr(self.m_FrameHead)+chr(self.m_FrameHead)
        endStr = chr(self.m_FrameTail)+chr(self.m_FrameTail)

        frameMaxDataSize = 17*2
        frameLen = len(frame)

        if startStr in frame and endStr in frame:
            endIndex = frame.index(endStr)

            if endIndex <= (frameMaxDataSize + 2):
                validFrame = frame[0:endIndex+2]
            dataLeft = frame[endIndex+2:]


        #print "frame %r " % frame

        if startStr not in frame:
            dataLeft = frame[-1:] #in case the last char is 0xaa
        elif endStr not in frame:
            if frameLen >= (frameMaxDataSize + 4):
                dataLeft = frame[-1:] #in case the last char is 0xaa
            else:
                dataLeft = frame

        return validFrame, dataLeft





    def analyzeRawDataReceived(self, dataIn):
        validFrameList = []

        print
        print
        print "self.receivedData %r" % dataIn


        startStr = chr(self.m_FrameHead)+chr(self.m_FrameHead)

        frameList = dataIn.split(startStr)
        print frameList


        for index, frame in enumerate(frameList):

            if index == 0: #ugly hack, split() remove the header
                if dataIn[0:2] is startStr:
                    frameTmp = startStr + frame
                else:
                    frameTmp = frame
            else:
                frameTmp = startStr + frame

            validFrame, dataLeft = self.checkRawFrameData(frameTmp)

            if validFrame is not None:
                validFrameList.append(validFrame)



        print "dataLeft: %r" % dataLeft
        print "validFrameList : "
        print validFrameList

        for rawFrame in validFrameList:
            self.getFrameFromRawData(rawFrame)


        return dataLeft, validFrameList



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
        datatoSend = canData.dumpDataToSend()
        if self.serialHandler:
            self.serialHandler.SendData(datatoSend)

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
       # print "[%r]" % self.receivedData

        # formater = RSDataFormater()
        # self.receivedData, returenRawDataList = formater.doPaser(self.receivedData)



        formater = USB2CANFormater()

        self.receivedData, returenRawDataList = formater.analyzeRawDataReceived(self.receivedData)
        #self.receivedData, returenRawDataList = formater.analyzeDataReceived(self.receivedData)



        for index, elem in enumerate(returenRawDataList):
            print
            print "##################"
            print "received:",index, elem
            self.receivedRawDataList.append(elem)
        #print "receiveSerialRawData"
        #print self.printHex(data)

            self.dumpAllRawData()

    def serialSendCanDataTest(self):



        #canDataTest = CAN_DATA()
        #canDataTest.buildTestData()

        usb2can = USB2CAN_DATA()
        usb2can.buildTestData()
        #usb2can.dumpDataToSend()

        self.serialSendCanData(usb2can)
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


    usb2can = USB2CAN_DATA()

    usb2can.buildTestData()
    #bytearray = usb2can.getByteArray()

    usb2can.dumpDataToSend()



"""
    canTest = CAN_DATA()
    canTest.buildTestData()
    buf = canTest.sturctureToByteArray()
    print buf
    formater = RSDataFormater()
    data1 = formater.doConstruct(buf)

    print data1
"""