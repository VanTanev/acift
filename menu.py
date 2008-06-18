# -*- coding: utf-8 -*-
import Tkinter as Tk
from controlFrames import ControlFrames
from tkFileDialog import askopenfilenames as getFilenames #Лигавя се :)
import os

"""
This class contains the menu bar and its event handlers
"""
class MenuBar():
    def __init__(self, master):

        '''
        ACIFT_main_menu = Tk.Menu(master)
        master.config(menu=ACIFT_main_menu)
        filemenu = Tk.Menu(ACIFT_main_menu)
        ACIFT_main_menu.add_cascade(label="File",menu=filemenu)
        filemenu.add_command(label="Open",command = self.openButton)
        '''
        master_menu = Tk.Menu(master)
        master.config(menu=master_menu)
        self.FileMenu = Tk.Menu(master_menu)
        master_menu.add_cascade(label="File", menu=self.FileMenu)
        master_menu.add_command(label="About")
        self.FileMenu.add_command(label="Open", command=self.openButton)
        self.FileMenu.add_separator()
        self.FileMenu.add_command(label="Exit", command=quit)

        


#        self.fileButton = Tk.Menubutton(self.menubar, text = "File")
#        self.fileButton.grid(column = 0, sticky = Tk.NW)
#        self.fileButton.menu = Tk.Menu(self.fileButton)
#        self.fileButton.menu.add_command(label = "Open", command = self.openButton)
#        self.fileButton['menu'] = self.fileButton.menu
        return
    def showAbout(self):
        about = Toplevel()

    def openButton(self):
        self.data = self.openFiles()
        
        if self.data:
            parent.loadImages(self.data) # <- change I tried to make :)
        else:
            print "No image selected"
            
    def openFiles(self):
        #filenames = [file for file in getFilenames(filetypes=[("Jpeg Files","*.jpg"),("All Files","*")])]
        filesToOpen = getFilenames(filetypes = [("Jpeg Files","*.jpg"),("All Files","*")], multiple = True)
        if len(filesToOpen) == 1 and os.path.isdir(filesToOpen[0]):
            self.dir = filesToOpen
            #TODO: Optimize next line and make it work for all types
            filesToOpen = [file for file in os.listdir(self.dir) if file.endswith(".jpg")]
            firstFile = 0
        else:
            self.dir = os.path.split(filesToOpen[0])[0]
            if len(filesToOpen) == 1:
                firstFile = filesToOpen[0]
                #filesToOpen = [ os.path.join(self.dir,file) for file in os.listdir(self.dir) if file.endswith(".jpg")]
                filesToOpen = [ self.dir + '/' + file for file in os.listdir(self.dir) if file.endswith(".jpg")]
                print firstFile
                print "lol"
                print filesToOpen
                print "lol"
                firstFile = filesToOpen.index(firstFile)
            else:
                firstFile = 0
        print "     Opening files:", filesToOpen, "Starting with:", firstFile
        return self.dir, filesToOpen, firstFile
