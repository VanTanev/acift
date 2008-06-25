#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Image
import os
import menu
import zipfile
#These are the UI commands - next, previous...
from events import *
#These are the types of input we work with - archives, lists of files...
from ImageLoaders import *
#These are the UI options - Fullscreen, Fit-to-screen...
from options import Options

class ImageFrame(wx.Frame, Events):
    def __init__(self, *args, **kwds):
        #self.events = events()
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.options = Options()
        #Default data - this needs to be changed at some point
        self.source = Files()
        source = self.source
        source.dir = "./"
        source.files = [u"1.jpg"]
        source.current = 0
        source.size = 1
        self.allowedTypes = ("png","jpg","jpeg","gif")
        
        
        self.background_panel = wx.Panel(self, -1)
        try:
            self.picture = wx.StaticBitmap(self, -1)
            self.sizer = wx.BoxSizer(wx.VERTICAL | wx.EXPAND)
            self.SetSizer(self.sizer)
            self.sizer.Add(self.picture, 0, wx.EXPAND, 0)
            self.openImage()
        except Exception, e:
            print Exception, e

        self._doLayout()
        self._setBindings()

     
    def _doLayout(self):
        self.Layout()
        self.Centre()
    

#-----------------------------------#
#                                   #
#            Fucntions              #
#                                   #
#-----------------------------------#

    def openFile(self, event = None):
        openFileDialog = wx.FileDialog(self, "Open a file", self.source.dir, "",
        "All files (*.*)|*.*|BMP files (*.bmp)|*.bmp|JPEG files (*.jpg)|*.jpg|Zip files (*.zip)|*.zip"
        , wx.OPEN | wx.FD_MULTIPLE | wx.FD_PREVIEW)
        if openFileDialog.ShowModal() == wx.ID_OK:
            #Default case - working with several files
            self.source = Files( dir = openFileDialog.GetDirectory() + "/", files = openFileDialog.GetFilenames())
            source = self.source
            self.isZip = False
            
            #We are working with a zip file
            if len(source.files) == 1 and source.files[0].endswith(".zip"):
                self.source = Zip( dir = source.dir, files = source.files )
                source = self.source
                source.zip = zipfile.ZipFile(source.dir + source.files[0], "r")
                source.files = [file for file in source.zip.namelist() if file.endswith(self.allowedTypes)]
                source.current = 0
                source.dir = ""
                self.isZip = True

            #Working with a directory (not used at the moment)
            elif len(source.files) == 1 and os.path.isdir(source.files[0]):
                source.dir = source.files[0] + "/"
                source.files = [file for file in os.listdir(source.dir) if file.endswith(self.allowedTypes)]

            #Working with only one file - open all files in the folder
            elif len(source.files) == 1:
                source.current = source.files[0]
                source.files = [file for file in os.listdir(source.dir) if file.endswith(self.allowedTypes)]
                source.current = source.files.index(source.current)

            source.size = len(source.files)
            openFileDialog.Destroy()
            #TODO: Make this work with """ and %s
            print "*"*20
            print "Loading filenames"
            print "Current Dir:", source.dir
            print "Files", source.files
            print "Starting with", source.current
            print "*"*20
            self.openImage()
        
    def openImage(self):
        self.rawImage = Image.open( self.source.getImage() )
        self.processedImage = self.resize(self.rawImage, self.rawImage.size)
        self.showImage()
        self.SetTitle("ACIFT - " + self.source.files[self.source.current])

    def showImage(self):
        self.bmp = pilToBitmap( self.processedImage )
        self.picture.SetBitmap( self.bmp )
        self.sizer.Fit(self)

    def resize(self, image, (x, y)):
        x,y = int(x), int(y)
        print x,y
        #This fits a big image to the screen. It should be in a
        #separate function (this for later)
        
        #if the options are set to fit image to screen
        #need to make them dynamic - work for any resolution?
        if self.options.fit:
            if x > 1280:
                (x,y) = (1280, int(y*1280/x))
            if y > 700:
                (x,y) = (int(x*700/y), 700)
#        print x,y
        return image.resize((x,y), Image.ANTIALIAS)

#-----------------------------------#
#                                   #
#          Helper Methods           #
#                                   #
#-----------------------------------#


def bitmapToPil(bitmap):
    return imageToPil(bitmapToImage(bitmap))

def bitmapToImage(bitmap):
    return wx.ImageFromBitmap(bitmap)

def imageToBitmap(image):
    return image.ConvertToBitmap()

def pilToBitmap(pil):
    return imageToBitmap(pilToImage(pil))

def pilToImage(pil):
    image = wx.EmptyImage(pil.size[0], pil.size[1])
    image.SetData(pil.convert('RGB').tostring())
    return image
