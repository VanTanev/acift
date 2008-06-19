#!/usr/bin/python
# -*- coding: utf-8 -*-
#HelloImage - display an image file

#import Tkinter as Tkinter
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

class MainFrame():
    def __init__(self, master = None):

        main_frame = Tk.Frame(master)
        main_frame.pack()
        #self.controlFrames = ControlFrames()
        ACIFT_top_menu = MenuBar(ACIFT)     #the menus    

        ###  Should be removed later on
        self.filenames = ["1.jpg", "2.jpg"]
        self.currentFile = 0
        self.numberOfImages = 2
        self.sizeChanged = True #<- DO NOT touch this, or program goes BooM!
        ###

        self.canvas = Tk.Canvas(main_frame)
        self.canvas.grid(row=1)

        
        self.showImage()

        self.setBindings()
        
    def loadImages(self, data = (".","",0) ):
        self.dirName, self.filenames, self.currentFile = data
        self.numberOfImages = len(self.filenames)
        print self.filenames, self.currentFile
        self.showImage()

    def setBindings(self):
        ACIFT.bind_all("<Next>", self.nextPage)
        ACIFT.bind_all("<Prior>", self.prevPage)
        ACIFT.bind_all("<space>", self.nextPage)
        #ACIFT.bind_all("<ButtonPress>", self.mouseButtonPressed)
        ACIFT.bind(("a"), self.changeImageSize)

    def changeImageSize(self,event):
        if self.sizeChanged:
            self.sizeChanged = False
            return False
        try:
            print "Width: ", event.width, "Height: ", event.height
            self.im = self.im.resize(
                (self.im.size[0]+5,self.im.size[1]+5))
            self.sizeChanged = True
            self.showImage_updateCanvas()        
        except Exception, e:
            print Exception, e
        return True

    def showImage(self):
        self.showImage_openFile()
        self.showImage_updateCanvas()
        return
    
    def showImage_openFile(self):
        print "     Files:", self.filenames
        print "     Starting with:", self.currentFile
        #print "     Trying to open item", currentFile, "Out of", filenames
        try:
            self.im = Image.open(self.filenames[self.currentFile])
        #TODO: Check which type of exception should be caught here
        #It shouldn't be just 'Exception', because that will catch
        #*all* exceptions, not just the ones about the file opening.
        except Exception, e:
            print Exception, e
            tkMessageBox.showwarning(
                "File open error",
                "Cannot open this file\n(%s)" % self.filenames[self.currentFile]
            )
        self.showImage_updateCanvas()
        return
    
    def showImage_updateCanvas(self):
        self.canvas.config(height=self.im.size[1], width=self.im.size[0])
        self.photo = ImageTk.PhotoImage(self.im)
        self.item = self.canvas.create_image(0,0,anchor=Tk.NW, image=self.photo)

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



ACIFT = Tk.Tk()
####  Acift components:
ACIFT_mainframe = MainFrame(ACIFT)   #the actual frame for images
#ACIFT_top_menu = MenuBar(ACIFT)     #the menus    

####
ACIFT.title("ACiF7 - A Comic is Fine, too")
ACIFT.mainloop()
