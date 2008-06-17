# -*- coding: utf-8 -*-
from tkFileDialog import askopenfilenames as getFilenames #Лигавя се :)

import os

class ControlFrames:
    """
    Filenames е или един или няколко файла, или папка
    Във всеки от случаите програмата отваря съответните файлове
    Това е клас в нов стил, наследяващ списък - има доста готови методи :)
    """
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
                filesToOpen = [ os.path.join(self.dir,file) for file in os.listdir(self.dir) if file.endswith(".jpg")]
                print firstFile
                print filesToOpen
                firstFile = filesToOpen.index(firstFile)
            else:
                firstFile = 0
        print "     Opening files:", filesToOpen, "Starting with:", firstFile
        return self.dir, filesToOpen, firstFile

