#HelloImage - display an image file
# -*- coding: utf-8 -*-
# Simon Peverett - October 2003
# uses the PIL module: http://www.pythonware.com/products/pil/
# developed using ActivePython 2.2: http://www.activestate.com

from Tkinter import *
import Image            #PIL
import ImageTk          #PIL
import sys
import getopt

class MainFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.grid(sticky=N+S+E+W)
        self.createMainMenu()
        self.loadAndShowImage()
        
    def createMainMenu(self):
        self.quitButton = Button(self, text="Quit!", command=self.quit)
        self.quitButton.grid()

    def loadAndShowImage(self):
        try:
            self.im = Image.open("1.jpg")
        except Exception, e:
            print >>sys.stderr, e
            sys.exit(1)
            
        self.canvas = Canvas(self, height=self.im.size[1]+15, width=self.im.size[0]+25)
        self.canvas.grid()
        self.photo = ImageTk.PhotoImage(self.im)
        self.item = self.canvas.create_image(10,10,anchor=NW, image=self.photo)



ACIFT = MainFrame()
ACIFT.master.title("ACiF7 - A Comic is Fine too")
ACIFT.mainloop()   
