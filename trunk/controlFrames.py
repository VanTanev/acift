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
        filenames = [file for file in getFilenames(filetypes=[("Jpeg Files","*.jpg"),("All Files","*")])]
        print filenames
        if len(filenames) == 1 and os.path.isdir(filenames[0]):
            """
            os.path.walk връща 3 неща - предполагам е очевидно кои са :)
            """
            self.dirPath, self.dirList, self.files = os.walk(filenames[0])        
        return filenames
