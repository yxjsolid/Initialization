from ctypes import *
import binascii

# '''
# typedef struct canFrameStruct
# {
# 	uint8 info;
# 	uint8 sig[4];
# 	uint8 canData[8];
# }canFrameStruct;
# '''
#
# """
# typedef struct  {
# BYTE  id[4];
# BYTE  data[8];            //channel
# BYTE  len;                //
# BYTE  ch;                 // 0xff:config
# BYTE  format;             // 00:sff  01:eff
# BYTE  type;               // 00:data 01:far
# BYTE  checkSum
# }  CAN_msg;
# """


class USB2CAN_DATA(Structure):
    _fields_ = [("id",       c_ubyte * 4),
                ("data",     c_ubyte * 8),
                ("len",      c_ubyte),
                ("ch",       c_ubyte),
                ("format",   c_ubyte),
                ("type",     c_ubyte),
                ("checkSum", c_ubyte)]

    def __init__(self):
        Structure.__init__(self)
        self.dataParser = USB2CANParser()
        return

    def getByteArray(self):
        checkSum = c_ubyte(0)

        byteArray = bytearray(sizeof(USB2CAN_DATA))
        dataBuffer = (c_ubyte * sizeof(USB2CAN_DATA))()
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

    def convertFromUsbRawData(self, rawData):
        if len(rawData) != sizeof(USB2CAN_DATA):
            print "receiveFrame -> error data len not match"
            return 0

        canBuff = (c_ubyte * sizeof(USB2CAN_DATA))()
        for index, num in enumerate(rawData):
            canBuff[index] = ord(num)

        memmove(byref(self), byref(canBuff), sizeof(USB2CAN_DATA))

        return

    def convertCanIdToUsb(self, canFrame):
        idTmp = canFrame.sig[0] << 24
        idTmp |= canFrame.sig[1] << 16
        idTmp |= canFrame.sig[2] << 8
        idTmp |= canFrame.sig[3]
        idTmp >>= 3

        memmove(byref(self.id), byref(c_uint32(idTmp)), 4)

        return

    def convertUsbIdToCan(self, canFrame):
        idTmp = self.id[3] << 24
        idTmp |= self.id[2] << 16
        idTmp |= self.id[1] << 8
        idTmp |= self.id[0]
        idTmp <<= 3

        sigTmp = (c_ubyte * 4)()
        memmove(byref(sigTmp), byref(c_uint32(idTmp)), 4)

        canFrame.sig[0] = sigTmp[3]
        canFrame.sig[1] = sigTmp[2]
        canFrame.sig[2] = sigTmp[1]
        canFrame.sig[3] = sigTmp[0]

        return

    def convertFromCanFrame(self, canFrame):
        self.convertCanIdToUsb(canFrame)

        self.data[0] = canFrame.canData[0]
        self.data[1] = canFrame.canData[1]
        self.data[2] = canFrame.canData[2]
        self.data[3] = canFrame.canData[3]
        self.data[4] = canFrame.canData[4]
        self.data[5] = canFrame.canData[5]
        self.data[6] = canFrame.canData[6]
        self.data[7] = canFrame.canData[7]

        self.len = canFrame.info
        self.ch = 0x66
        self.format = 1
        self.type = 0

    def convertToCanFrame(self):
        canFrame = CAN_FRAME()

        self.convertUsbIdToCan(canFrame)

        canFrame.info = self.len
        canFrame.canData[0] = self.data[0]
        canFrame.canData[1] = self.data[1]
        canFrame.canData[2] = self.data[2]
        canFrame.canData[3] = self.data[3]
        canFrame.canData[4] = self.data[4]
        canFrame.canData[5] = self.data[5]
        canFrame.canData[6] = self.data[6]
        canFrame.canData[7] = self.data[7]

        return canFrame





    def buildTestData(self):
        self.convertCanIdToUsb()

        print "sizeof(c_uint)", sizeof(c_uint)

        print "sizeof(USB2CAN_DATA)", sizeof(USB2CAN_DATA)

#        self.id = 0xff

        #dd = c_uint





        #byteArray = bytearray(sizeof(USB2CAN_DATA))
        # dataBuffer = (c_ubyte * 4)()
        #
        # memmove(byref(dataBuffer),      byref(self.id) + 3, 1)
        # memmove(byref(dataBuffer) + 1,  byref(self.id) + 2, 1)
        # memmove(byref(dataBuffer) + 2,  byref(self.id) + 1, 1)
        # memmove(byref(dataBuffer) + 3,  byref(self.id), 1)




        self.len = 8
        self.ch = 0x66
        self.format = 1
        self.type = 0

        val = 5
        for i in range(8):
            self.data[i] = val

    def dumpDataToSend(self):
        return self.dataParser.genDataToSend(self.getByteArray())


class USB2CANParser():
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

        sep = chr(self.m_FrameCtrl)
        rawList = sep.join(rawList)

        #print "rawList:"
        #print "%r " % rawList

        return rawList

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

        #print
        #print
        #print "self.receivedData %r" % dataIn

        startStr = chr(self.m_FrameHead) + chr(self.m_FrameHead)

        frameList = dataIn.split(startStr)
        #print frameList

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
                validFrameList.append(self.getFrameFromRawData(validFrame))



        #print "dataLeft: %r" % dataLeft
        #print "validFrameList : "
        #print validFrameList

        #for rawFrame in validFrameList:
            #self.getFrameFromRawData(rawFrame)


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


class CAN_FRAME(Structure):
    _fields_ = [("info",    c_ubyte),
                ("sig",     c_ubyte * 4),
                ("canData", c_ubyte * 8)]

    CAN_FRAME_STATUS_CHECK = 1
    CAN_FRAME_SET_ACTION = 2

    def structureToByteArray(self):
        byteArray = bytearray(sizeof(CAN_FRAME))
        canBuff = (c_ubyte * sizeof(CAN_FRAME))()
        memmove(byref(canBuff), byref(self), sizeof(CAN_FRAME))

        print "sizeof(CAN_FRAME) = ", sizeof(CAN_FRAME)


        outstr = ""
        for index, elem in enumerate(canBuff):
            byteArray[index] = elem

            outstr += "0x%02x, " % elem



        print "can data raw:[%r]" % byteArray
        print "outstr = ", outstr
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

    def setCanFrameLen(self, length):
        self.info = length

    def setCanStationId(self, stationId):
        self.sig[2] = stationId >> 5
        self.sig[3] = (stationId & 0x1f) << 3

    def setCMDType(self, cmdType):
        self.canData[0] = cmdType

    def getCMDType(self):
        return self.canData[0]

    def setCMDBoardType(self, boardType):
        self.canData[1] = boardType

    def getCMDBoardType(self):
        return self.canData[1]

    def setCMDBoardID(self, boardID):
        self.canData[2] = boardID

    def getCMDBoardID(self):
        return self.canData[2]

    def setCMDBoardStatus(self, boardStatus):
        self.canData[3] = boardStatus

    def getCMDBoardStatus(self):
        return self.canData[3]

    def setCmdData(self, cmdData):
        self.canData[4] = cmdData

    def getCmdData(self):
        return self.canData[4]

    def setInputBoardCnt(self, cnt):
        self.sig[1] &= 0x0f
        self.sig[1] |= cnt << 4

    def setOutputBoardCnt(self, cnt):
        self.sig[1] &= 0xf0
        self.sig[1] |= cnt

    # def setCanFrameType(self, frameType):
    #     self.sig[0] = frameType

    def setCanFrameData(self, index, data):
        self.canData[index] = data

    def getCanFrameLen(self):
        return self.info

    def getCanStationId(self):
        stationId = (self.sig[3] >> 3) & 0x1f
        stationId |= (self.sig[2] & 0x7) << 5
        print "getCanStationid = ", stationId

        return stationId

    def getCanFrameType(self):
        return self.sig[0] & 0x7f
        #return self.sig[0]

    def getInputBoardCnt(self):
        return (self.sig[1] & 0xf0) >> 4

    def getOutputBoardCnt(self):
        return self.sig[1] & 0x0f

    def getCanFrameData(self, index):
        return self.canData[index]

    def dumpCanData(self):
        return
        print "info = ", self.info
        for index,num in enumerate(self.sig):
            print "sig[%d] = %x" % (index, num)

        for index,num in enumerate(self.canData):
            print "canData[%d] = %x" % (index, num)


class CanProxy():
    def __init__(self, SerialHandler=None, stationDaemonMgmt=None):

        self.serialHandler = SerialHandler
        self.stationDaemonMgmt = stationDaemonMgmt
        self.receivedData = ""
        #self.receivedRawDataList = []
        if self.serialHandler:
            self.serialHandler.dataProxy = self

        if self.stationDaemonMgmt:
            self.stationDaemonMgmt.dataProxy = self

        return

    def proxyHandleCanFrameReceived(self, canFrame):
        print "handleCanFrameReceived"
        stationId = canFrame.getCanStationId()
        self.stationDaemonMgmt.getStationDaemon(stationId).daemonHandleCanFrameReceived(canFrame)
        
        return

    def sendCanFrame(self, frame):
        dataToSend = USB2CAN_DATA()
        dataToSend.convertFromCanFrame(frame)

        if self.serialHandler:
            self.serialHandler.SendData(dataToSend.dumpDataToSend())

    def proxyReceiveCanFrame(self, rawData):
        print "proxyReceiveCanFrame"

        if len(rawData) != sizeof(USB2CAN_DATA):
            print "receiveFrame -> error data len not match"
            return 0

        usb2canData = USB2CAN_DATA()
        usb2canData.convertFromUsbRawData(rawData)

        canFrame = usb2canData.convertToCanFrame()
        canFrame.dumpCanData()

        self.proxyHandleCanFrameReceived(canFrame)
        return 1

    def receiveSerialRawData(self, data):
        self.receivedData += data
        #print "[%r]" % self.receivedData

        # formater = RSDataFormater()
        # self.receivedData, returenRawDataList = formater.doPaser(self.receivedData)

        parser = USB2CANParser()
        self.receivedData, returnRawDataList = parser.analyzeRawDataReceived(self.receivedData)
        #self.receivedData, returenRawDataList = formater.analyzeDataReceived(self.receivedData)

        for index, elem in enumerate(returnRawDataList):
            #print
            #print "##################"
            #print "received:",index, elem
            #self.receivedRawDataList.append(elem)
            self.proxyReceiveCanFrame(elem)
            #print "receiveSerialRawData"
            #print self.printHex(data)

            #self.dumpAllRawData()

    def serialSendCanDataTest(self):

        #canDataTest = CAN_DATA()
        #canDataTest.buildTestData()
        usb2can = USB2CAN_DATA()
        usb2can.buildTestData()
        #usb2can.dumpDataToSend()
        dataToSend = usb2can.dumpDataToSend()
        if self.serialHandler:
            self.serialHandler.SendData(dataToSend)

        return


    def dumpAllRawData(self):
        print
        print "dump all raw data:"
        for index, elem in enumerate(self.receivedRawDataList):
            print index, elem




    def printHex(self, s):
        s1 = binascii.b2a_hex(s)
        print s1



def getSomeCanTestData():
    canTest = CAN_FRAME()
    canTest.buildTestData()
    buf = canTest.structureToByteArray()
    print "getSomeCanTestData 1 ", buf

    formater = RSDataFormater()
    data1 = formater.doConstruct(buf)

    print "getSomeCanTestData 2 ", data1

if __name__ == '__main__':




    canFrame = CAN_FRAME()
    canFrame.sig[0] = 1
    canFrame.sig[1] = 2
    canFrame.sig[2] = 3
    canFrame.sig[3] = 4

    canFrame.structureToByteArray()


"""
    canTest = CAN_DATA()
    canTest.buildTestData()
    buf = canTest.sturctureToByteArray()
    print buf
    formater = RSDataFormater()
    data1 = formater.doConstruct(buf)

    print data1
"""