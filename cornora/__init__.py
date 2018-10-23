#!/usr/bin/python3
import argparse
from os import kill, nice
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
    def executor(self,process):
        if self.subpid == 0:
            out = Popen(process.split(), stdout=PIPE, stderr=PIPE)
            self.subpid = out.pid
        else:
            kill(self.subpid, SIGKILL)
            self.subpid = 0
    def checkMouse(self):
        data = display.Display().screen().root.query_pointer()._data
        if when.tl is not None and data["root_x"] <= 1 and data["root_y"] <= 1:
            self.executor(when.tl)
        elif when.tr is not None and data["root_x"] == maxW and data["root_y"] <= 1:
            self.executor(when.tr)
        elif when.bl is not None and data["root_x"] <= 1 and data["root_y"] == maxH:
            self.executor(when.bl)
        elif when.br is not None and data["root_x"] == maxW and data["root_y"] == maxH:
            self.executor(when.br)
    def mouseListener(self):
        self.subpid = 0
        self.listening = True
        print("daemon started")
        try:
            while self.listening == True:
                self.checkMouse()
                sleep(0.3)
        except (KeyboardInterrupt, SystemExit):
            self.stopService()
    def stopService(self):
        self.listening = False
        print("\rdaemon stopped")

def main():
    nice(19)
    Service().process.run()
