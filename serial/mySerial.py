import sys,threading,time
import serial
import binascii,encodings
import re
import socket
from canData import *

class SerialHandler:
    def __init__(self, Port=0, DataHandler=None):
        self.l_serial = None
        self.alive = False
        self.waitEnd = None
        self.port = Port
        self.dataHandler = DataHandler

    def waiting(self):
        if not self.waitEnd is None:
            self.waitEnd.wait()

    def SetStopEvent(self):
        if not self.waitEnd is None:
            self.waitEnd.set()
        self.alive = False
        self.stop()

    def start(self):
        self.l_serial = serial.Serial()
        self.l_serial.port = self.port
        self.l_serial.baudrate = 9600
        self.l_serial.timeout = 2

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
        try:
            time.sleep(1)
            #start to read
            self.l_serial.flushInput()
            self.l_serial.write('\x11')
        except ValueError,ex:
            #error
            self.SetStopEvent()
            print "stop event"
            return



    def SendData(self, i_msg):
        lmsg = ''
        isOK = False
        if isinstance(i_msg, unicode):
            lmsg = i_msg.encode('gb18030')
        else:
            lmsg = i_msg
        try:
            pass
        except Exception, ex:
            pass
        return isOK

    def FirstReader(self):
        self.InitHead()

        while self.alive:
            try:
                data = ''
                n = self.l_serial.inWaiting()
                if n:
                    dataNew = self.l_serial.read(n)
                    data += dataNew

                    print "\n\n######################\n"
                    print binascii.b2a_hex(dataNew)
                    print binascii.b2a_hex(data)

                    if self.dataHandler is not None:
                        self.dataHandler.receiveSerialRawData(data)


                    self.printHex(data)
            except Exception, ex:
                print "FirstReader:",ex

        self.waitEnd.set()
        self.alive = False

    def stop(self):
        self.alive = False
        self.thread_read.join()
        if self.l_serial.isOpen():
            self.l_serial.close()

    def printHex(self, s):
        s1 = binascii.b2a_hex(s)
        print s1

if __name__ == '__main__':

    rt = SerialHandler(Port=2)
    dataHandler = CanProxy()

    rt.dataHandler = dataHandler

    try:
        if rt.start():
            rt.waiting()
            rt.stop()
        else:
            pass
    except Exception,se:
        print str(se)

    if rt.alive:
        rt.stop()

    print 'End OK .'
    del rt
