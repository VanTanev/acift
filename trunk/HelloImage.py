#!/usr/bin/python
# -*- coding: utf-8 -*-
#HelloImage - display an image file
# Simon Peverett - October 2003
# uses the PIL module: http://www.pythonware.com/products/pil/
# developed using ActivePython 2.2: http://www.activestate.com

from Tkinter import *
from tkFileDialog import askopenfilename
import Image            #PIL
import ImageTk          #PIL
import sys
import getopt
import os

""" Filenames е или един или няколко файла, или папка
    Във всеки от случаите програмата отваря съответните файлове
    Това е клас в нов стил, наследяващ списък - има доста готови методи :)
"""
class Pages:        
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

class MainFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self,master)
        self.grid(sticky=N+S+E+W)
        self.files = Pages()
        self.createMenuBar()        
        #FIXME: Hardcoded!
        self.loadImages()
        
        self.loadAndShowImage()

    def selecFile():
        self.filename = askopenfilename(filetypes=[("Jpeg Files","*.jpg"),("All Files","*")])
        return self.filename
        
    def createMenuBar(self):
        menubar = Frame(self, relief=RAISED,borderwidth=1)
        menubar.grid(column=0, sticky=NW)

        fileButton = Menubutton(menubar, text="File")
        fileButton.grid(column=0, sticky=NW)
        fileButton.menu = Menu(fileButton)

        fileButton.menu.add_command(label="Open")#, command=selectFile())
        fileButton['menu'] = fileButton.menu
        

        
        #self.quitButton = Button(self, text="Quit!", command=quit)
        #self.quitButton.grid()
        return

    def loadAndShowImage(self):
        try:
            self.im = Image.open(self.files.pages[0])
        except Exception, e:
            print >>sys.stderr, e
            sys.exit(1)
            
        self.canvas = Canvas(self, height=self.im.size[1]+15, width=self.im.size[0]+25)
        self.canvas.grid()
        self.photo = ImageTk.PhotoImage(self.im)
        self.item = self.canvas.create_image(10,10,anchor=NW, image=self.photo)
    
    """ Този метод трябва да вика File Chooser-ът и да му праща списък от
    имена на файлове/директории.
    """
    def loadImages(self):
        #FIXME: Hardcoded
        self.files.setFiles(["1.jpg"])


ACIFT = MainFrame()
ACIFT.master.title("ACiF7 - A Comic is Fine, too")
ACIFT.mainloop()   
