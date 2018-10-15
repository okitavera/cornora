#!/usr/bin/python3
"""
Cornora
Simple Hotcorner Launcher for X

usage:

   arguments          run a command when mouse touching :
   ------------------------------------------------------
   --tl "command"     top-left corner of the screen
   --tr "command"     top-right
   --bl "command"     bottom-left
   --br "command"     bottom-right

   -h  --help         show help docs
"""
from os import kill
from time import sleep
from Xlib import display
from getopt import getopt
from signal import SIGKILL
from sys import argv, exit
from subprocess import PIPE, Popen

screen = display.Display().screen()
maxW = screen.width_in_pixels-1
maxH = screen.height_in_pixels-1

Pass = True
try:
    opts, args = getopt(argv[1:], 'h', ['tl=', 'tr=', 'bl=', 'br=', 'help='])
    for opt, arg in opts:
        Pass = True
        if opt == '--tl':
            when_tl = arg
        elif opt == '--tr':
            when_tr = arg
        elif opt == '--bl':
            when_bl = arg
        elif opt == '--br':
            when_br = arg
        else:
            Pass = False
except:
    Pass = False

class Service:
    def isTopLeft(self, data):
        return data["root_x"] == 0 and data["root_y"] == 0
    def isTopRight(self, data):
        return data["root_x"] == maxW and data["root_y"] == 0
    def isBottomLeft(self, data):
        return data["root_x"] == 0 and data["root_y"] == maxH
    def isBottomRight(self, data):
        return data["root_x"] == maxW and data["root_y"] == maxH
    def executor(self,process):
        if self.subpid == 0:
            out = Popen(process.split(), stdout=PIPE, stderr=PIPE)
            self.subpid = out.pid
        else:
            kill(self.subpid, SIGKILL)
            self.subpid = 0
        sleep(.5)
    def run(self):
        self.subpid = 0
        try:
            print("daemon started")
            while 1:
                mouse = display.Display().screen().root.query_pointer()._data
                try:
                    if self.isTopLeft(mouse):
                        self.executor(when_tl)
                    elif self.isTopRight(mouse):
                        self.executor(when_tr)
                    elif self.isBottomLeft(mouse):
                        self.executor(when_bl)
                    elif self.isBottomRight(mouse):
                        self.executor(when_br)
                except:
                    sleep(.25)
        except (KeyboardInterrupt, SystemExit):
            print("daemon stopped")
            exit()

def main():
    if Pass:
        Service().run()
    else:
        print(__doc__)

if __name__ == "__main__":
    main()