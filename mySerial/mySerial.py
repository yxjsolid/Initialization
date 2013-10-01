import sys,threading,time
import serial
import binascii,encodings
import re
import socket
from canData import *

class SerialHandler:
    def __init__(self, Port=0, DataProxy=None):
        self.l_serial = None
        self.alive = False
        self.waitEnd = None
        self.port = Port
        self.dataProxy = DataProxy

        self.serialLock = threading.Lock()

    def waiting(self):
        if not self.waitEnd is None:
            self.waitEnd.wait()

    def SetStopEvent(self):
        if not self.waitEnd is None:
            self.waitEnd.set()
        self.alive = False
        self.stop()

    def start(self):
        print "start111,", self.l_serial

        self.l_serial = serial.Serial()
        self.l_serial.port = self.port
        self.l_serial.baudrate = 9600
        self.l_serial.timeout = 2
        #self.l_serial.setStopbits()

        print "start222,", self.l_serial

        try:
            self.l_serial.open()
        except Exception, ex:
            if self.l_serial.isOpen():
                self.l_serial.close()

            print "start", ex
            self.l_serial = None

            return False

        if self.l_serial.isOpen():
            #create recieve task
            self.waitEnd = threading.Event()
            self.alive = True
            self.thread_read = None
            self.thread_read = threading.Thread(target=self.FirstReader)
            self.thread_read.setDaemon(1)
            self.thread_read.start()
            return True
        else:
            #serial not open
            return False

    def InitHead(self):
        print "InitHead"

        try:
            #time.sleep(0.1)
            print "InitHead"
            #start to read
            self.l_serial.flushInput()
            #self.l_serial.write('\x11')
        except ValueError,ex:
            #error
            self.SetStopEvent()
            print "stop event"
            return

    def doSerialLock(self):
        return self.serialLock.acquire()

    def doSerialRelease(self):
        self.serialLock.release()

    def SendData(self, i_msg):
        if self.doSerialLock():
            self.l_serial.write(i_msg)
            self.doSerialRelease()

        print "serial send done"
        return
    def FirstReader(self):

        #print "FirstReader"

        self.InitHead()

        while self.alive:
            #try:
            data = ''
            n = self.l_serial.inWaiting()
            if n:

                if self.doSerialLock():
                    dataNew = self.l_serial.read(n)
                    self.doSerialRelease()

                data += dataNew

                print "FirstReader 111 ", data

                #print "\n\n######################\n"
                #print n,"data", "new",dataNew
                #print binascii.b2a_hex(dataNew)
                #print binascii.b2a_hex(data)

                if self.dataHandler is not None:
                    self.dataHandler.receiveSerialRawData(data)

            #except Exception, ex:
                #print "FirstReader:",ex

        self.waitEnd.set()
        self.alive = False

    def stop(self):
        self.alive = False
        self.thread_read.join()
        if self.l_serial.isOpen():
            self.l_serial.close()


    def sendSomeTestData(self):
        self.dataHandler.serialSendCanDataTest()
        return


    def printHex(self, s):
        s1 = binascii.b2a_hex(s)
        print s1

if __name__ == '__main__':

    rt = SerialHandler(Port=3)
    dataHandler = CanProxy(SerialHandler=rt)
    rt.dataHandler = dataHandler




    #try:
    if rt.start():
        #help( rt.l_serial)

        # print rt.l_serial.getCD()
        # print rt.l_serial.getCTS()
        # print rt.l_serial.getDSR()
        # print rt.l_serial.getRI()
        # print rt.l_serial.rtscts
        #
        # print rt.l_serial.getByteSize()
        # print rt.l_serial.getDsrDtr()
        # print rt.l_serial.getRtsCts()
        # print rt.l_serial.getStopbits()
        # print rt.l_serial.getXonXoff()
        # print rt.l_serial.dsrdtr
        # print rt.l_serial.rtscts
        # print rt.l_serial.stopbits

        #rt.l_serial.setXonXoff(1)
        #print "xonxoff", rt.l_serial.getXonXoff()


        #help(rt.l_serial.write)
        rt.sendSomeTestData()

        rt.waiting()


        rt.stop()
    #     else:
    #         pass
    # except Exception,se:
    #     print str(se)
    #
    # if rt.alive:
    #     rt.stop()

    print 'End OK .'
    del rt
