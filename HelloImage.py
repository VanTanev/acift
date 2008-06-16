#!/usr/bin/python
# -*- coding: utf-8 -*-
#HelloImage - display an image file
# Simon Peverett - October 2003
# uses the PIL module: http://www.pythonware.com/products/pil/
# developed using ActivePython 2.2: http://www.activestate.com

from Tkinter import *
from tkFileDialog import *
import tkMessageBox

import Image            #PIL
import ImageTk          #PIL
import sys
import getopt
import os

          
class ControlFrames:
    """
    Filenames е или един или няколко файла, или папка
    Във всеки от случаите програмата отваря съответните файлове
    Това е клас в нов стил, наследяващ списък - има доста готови методи :)
    """
    def openFiles(self):
        filenames = [file for file in askopenfilenames(filetypes=[("Jpeg Files","*.jpg"),("All Files","*")])]
        print filenames
        if len(filenames) == 1 and os.path.isdir(filenames[0]):
            """
            os.path.walk връща 3 неща - предполагам е очевидно кои са :)
            """
            self.dirPath, self.dirList, self.files = os.walk(filenames[0])        
        return filenames

"""
This class contains the menu bar and its event handlers
"""
class MenuBar(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.menubar = Frame(master, relief = RAISED, borderwidth = 1)
        self.menubar.grid(column = 0, sticky = NW)

        self.fileButton = Menubutton(self.menubar, text = "File")
        self.fileButton.grid(column = 0, sticky = NW)
        self.fileButton.menu = Menu(self.fileButton)
        self.fileButton.menu.add_command(label = "Open", command = self.openButton)
        self.fileButton['menu'] = self.fileButton.menu
        return

    def openButton(self):
        self.pages = ACIFT.controlFrames.openFiles()
        
        if self.pages:
            print self.pages
            ACIFT.showImage(self.pages[0])
        else:
            print "No image selected"

class MainFrame(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.controlFrames = ControlFrames()
        self.menu = MenuBar(self)
        self.grid(row = 0, sticky = N + S + E + W)
        self.canvas = Canvas(self)
        self.canvas.grid(row=1)
        self.showImage()

    def selectFile(self):
        self.filename = askopenfilename(filetypes=[("Jpeg Files","*.jpg"),("All Files","*")])
        return self.filename
        
    def showImage(self, fileName = "1.jpg"):
        try:
            print fileName
            self.im = Image.open(fileName)
            self.canvas.config(height=self.im.size[1]+15, width=self.im.size[0]+25)

            self.photo = ImageTk.PhotoImage(self.im)
            self.item = self.canvas.create_image(10,10,anchor=NW, image=self.photo)
        except Exception, e:
            print >>sys.stderr, e
            tkMessageBox.showwarning(
                "File open error",
                "Cannot open this file\n(%s)" % fileName
            )

            


    
    """ Този метод трябва да вика File Chooser-ът и да му праща списък от
    имена на файлове/директории.
    """

print "LOL"
ACIFT = MainFrame()
print "LOL"
ACIFT.master.title("ACiF7 - A Comic is Fine, too")
ACIFT.mainloop()
print "LOL"
