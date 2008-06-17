#!/usr/bin/python
# -*- coding: utf-8 -*-
#HelloImage - display an image file

#from Tkinter import *
import tkMessageBox
import Image
import ImageTk

from utils import *


"""
TODO:
Next/Previous Buttons
Debugging information would be good. Very good. Implement logger?
An event manager should be implemented for every key that is pressed.
OS INTEGRATION!!! This is very important! Either find a way to make
    Tkinter integrate seamlessly with both Windows and Unix, or we
    should scrap the whole TkIdea and switch to wxWidgets while there is
    still not much code written. Noone will ever use an ugly-looking
    program if there is a pretty, almost perfect analogy.

DONE:
Class separation in files
"""

class MainFrame(Tk.Frame):
    def __init__(self, master = None):
        Tk.Frame.__init__(self, master)
        self.controlFrames = ControlFrames()
        self.menu = MenuBar(self)
        self.grid(row = 0, sticky = Tk.N + Tk.S + Tk.E + Tk.W)
        self.canvas = Tk.Canvas(self)
        self.canvas.grid(row=1)
        self.setBindings()
        #self.showImage()
        
    def loadImages(self, data = (".","",0) ):
        self.dirName, self.filenames, self.currentFile = data
        self.numberOfImages = len(self.filenames)
        print self.filenames, self.currentFile
        self.showImage()

    def setBindings(self):
        self.bind_all("<Next>", self.nextPage)
        self.bind_all("<Prior>", self.prevPage)
        self.bind_all("Space", self.nextPage)

    def showImage(self):
        print "     Files:", self.filenames
        print "     Starting with:", self.currentFile
        #print "     Trying to open item", currentFile, "Out of", filenames
        try:
            self.im = Image.open(self.filenames[self.currentFile])
            self.canvas.config(height=self.im.size[1]+15, width=self.im.size[0]+25)
            self.photo = ImageTk.PhotoImage(self.im)
            self.item = self.canvas.create_image(10,10,anchor=Tk.NW, image=self.photo)
        #TODO: Check which type of exception should be caught here
        #It shouldn't be just 'Exception', because that will catch
        #*all* exceptions, not just the ones about the file opening.
        except Exception, e:
            print Exception, e
            tkMessageBox.showwarning(
                "File open error",
                "Cannot open this file\n(%s)" % self.filenames[self.currentFile]
            )

    def nextPage(self, event):
        self.currentFile += 1
        if self.currentFile >= self.numberOfImages:
            self.currentFile = 0
        self.showImage()

    def prevPage(self, event):
        self.currentFile -= 1
        if self.currentFile < 0:
            self.currentFile = self.numberOfImages -1            
        self.showImage()

ACIFT = MainFrame()
ACIFT.master.title("ACiF7 - A Comic is Fine, too")
ACIFT.mainloop()
