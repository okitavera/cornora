#!/usr/bin/python3
import argparse
from os import kill
from time import sleep
from Xlib import display
from getopt import getopt
from signal import SIGKILL
from sys import argv, exit
from subprocess import PIPE, Popen
from multiprocessing import Process

screen = display.Display().screen()
maxW = screen.width_in_pixels-1
maxH = screen.height_in_pixels-1

parser = argparse.ArgumentParser()
parser.add_argument("-tl", metavar='"cmd"', help="top-left command")
parser.add_argument("-tr", metavar='"cmd"', help="top-right command")
parser.add_argument("-bl", metavar='"cmd"', help="bottom-left command")
parser.add_argument("-br", metavar='"cmd"', help="bottom-right command")
when = parser.parse_args()

class Service:
    def __init__(self):
        self.process = Process(target=self.mouseListener)
        self.process.daemon = True
    def isTopLeft(self, data):
        return when.tl is not None and data["root_x"] <= 1 and data["root_y"] <= 1
    def isTopRight(self, data):
        return when.tr is not None and data["root_x"] == maxW and data["root_y"] <= 1
    def isBottomLeft(self, data):
        return when.bl is not None and data["root_x"] <= 1 and data["root_y"] == maxH
    def isBottomRight(self, data):
        return when.br is not None and data["root_x"] == maxW and data["root_y"] == maxH
    def executor(self,process):
        if self.subpid == 0:
            out = Popen(process.split(), stdout=PIPE, stderr=PIPE)
            self.subpid = out.pid
        else:
            kill(self.subpid, SIGKILL)
            self.subpid = 0
    def mouseListener(self):
        self.subpid = 0
        self.listening = True
        print("daemon started")
        try:
            while self.listening == True:
                mouse = display.Display().screen().root.query_pointer()._data
                if self.isTopLeft(mouse):
                    self.executor(when.tl)
                elif self.isTopRight(mouse):
                    self.executor(when.tr)
                elif self.isBottomLeft(mouse):
                    self.executor(when.bl)
                elif self.isBottomRight(mouse):
                    self.executor(when.br)
                sleep(0.3)
        except (KeyboardInterrupt, SystemExit):
            self.stopService()
    def stopService(self):
        self.listening = False
        print("\rdaemon stopped")

def main():
    Service().process.run()
