# -*- coding: utf-8 -*-

import wx
from MyGlobal import *



class StationManagement():
    def __init__(self):

        self.stationList = []

        return


    def addCanStation(self, canStation):
        self.stationList.append(canStation)

    def setCanStationList(self, canStationList):
        self.stationList = canStationList

    def getCanStationList(self):
        return self.stationList


class DeviceCanStation():
    def __init__(self, name=LABEL_STATION_NAME, info=LABEL_STATION_INFO):
        self.name = name
        self.info = info
        self.id = 0
        self.InputBoardList = []
        self.OutputBoardList = []


    def addNewIoBoard(self, board):

        if board.boardType == DeviceIoBoard.BOARD_TYPE_INPUT:
            self.InputBoardList.append(board)
        elif board.boardType == DeviceIoBoard.BOARD_TYPE_OUTPUT:
            self.OutputBoardList.append(board)
        else:
            print "addNewIoBoard error"



class DeviceIoBoard():

    BOARD_TYPE_INPUT, BOARD_TYPE_OUTPUT = range(2)
    board_type_choices = [LABEL_IO_BOARD_INPUT, LABEL_IO_BOARD_OUTPUT]

    def __init__(self):
        self.boardType = 0
        self.boardId = 0

        return

    def getBoardIdStr(self):

        return str(self.boardId)

    def getBoardTypeStr(self):
        return DeviceIoBoard.board_type_choices[self.boardType]