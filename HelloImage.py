#!/usr/bin/python
# -*- coding: utf-8 -*-
#HelloImage - display an image file

import Tkinter as Tk
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
        self.showImage()

    def selectFile(self):
        self.filename = askopenfilename(filetypes=[("Jpeg Files","*.jpg"),("All Files","*")])
        return self.filename
        
    def showImage(self, fileName = "1.jpg"):
        try:
            self.im = Image.open(fileName)
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
                "Cannot open this file\n(%s)" % fileName
            )


ACIFT = MainFrame()
ACIFT.master.title("ACiF7 - A Comic is Fine, too")
ACIFT.mainloop()
