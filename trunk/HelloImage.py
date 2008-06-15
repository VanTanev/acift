#!/usr/bin/python
# -*- coding: utf-8 -*-
#HelloImage - display an image file
# Simon Peverett - October 2003
# uses the PIL module: http://www.pythonware.com/products/pil/
# developed using ActivePython 2.2: http://www.activestate.com

from Tkinter import *
from tkFileDialog import *
import Image            #PIL
import ImageTk          #PIL
import sys
import getopt
import os

""" Filenames е или един или няколко файла, или папка
    Във всеки от случаите програмата отваря съответните файлове
    Това е клас в нов стил, наследяващ списък - има доста готови методи :)
"""
class FileOperations:        
    def setFiles(self, filenames = []):
        print "ASD"
        if len(filenames) == 1 and os.path.isdir(filenames[0]):
            """ os.walk връща 3 неща:
                път към директорията,
                списък от директории в нея,
                списък от файлове в нея.
            """
            self.dirPath, self.dirList, self.files = os.walk(filenames[0])
            self.pages = [ os.join(self.dirPath,filename) for filename in self.files]
        else:
          self.pages = filenames


          
class ControlFrames:
    def openFiles(self):
        filename = askopenfilenames(filetypes=[("Jpeg Files","*.jpg"),("All Files","*")])
        for n in filename: print n
        return filename



class MainFrame(Frame):
    def __init__(self, master=None):
        self.fileOps = FileOperations()
        self.controlFrames = ControlFrames()

        Frame.__init__(self,master)
        self.createMenuBar()  
        self.grid(row=0, sticky=N+S+E+W)
      
        #FIXME: Hardcoded!
        self.loadImages()
        
        self.loadAndShowImage()

    def selectFile(self):
        self.filename = askopenfilename(filetypes=[("Jpeg Files","*.jpg"),("All Files","*")])
        return self.filename
        
    def createMenuBar(self):
        menubar = Frame(self, relief=RAISED,borderwidth=1)
        menubar.grid(column=0, sticky=NW)

        fileButton = Menubutton(menubar, text="File")
        fileButton.grid(column=0, sticky=NW)
        fileButton.menu = Menu(fileButton)

        fileButton.menu.add_command(label="Open", command=self.fileOps.setFiles(self.controlFrames.openFiles))
        fileButton['menu'] = fileButton.menu
        
        return

    def loadAndShowImage(self, fileName = "1.jpg"):
        try:
            self.im = Image.open(fileName)
        except Exception, e:
            print >>sys.stderr, e
            sys.exit(1)
            
        self.canvas = Canvas(self, height=self.im.size[1]+15, width=self.im.size[0]+25)
        self.canvas.grid(row=1)
        self.photo = ImageTk.PhotoImage(self.im)
        self.item = self.canvas.create_image(10,10,anchor=NW, image=self.photo)
    
    """ Този метод трябва да вика File Chooser-ът и да му праща списък от
    имена на файлове/директории.
    """
    def loadImages(self):
        #FIXME: Hardcoded
        self.fileOps.setFiles(["1.jpg"])


ACIFT = MainFrame()
ACIFT.master.title("ACiF7 - A Comic is Fine, too")
ACIFT.mainloop()   
