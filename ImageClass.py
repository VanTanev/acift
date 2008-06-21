#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import Image
import os
import menu
import zipfile
import cStringIO

class ImageFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        #self.events = events()
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)

        #Default data - this needs to be changed at some point
        self.dir = "./"
        self.files = [u"1.jpg"]
        self.current = 0
        self.size = 1
        self.isZip = False
        
        self.sizer = wx.BoxSizer(wx.VERTICAL | wx.EXPAND)
        self.background_panel = wx.Panel(self, -1)
        try:
            self.image = Image.open(self.dir + self.files[self.current])
            self.bmp = pilToBitmap(self.image)
            self.picture = wx.StaticBitmap(self, -1, self.bmp)

            self.SetSizer(self.sizer)
            self.sizer.Add(self.picture, 0, wx.EXPAND, 0)
            self.sizer.Fit(self)
        except Exception, e:
            print Exception, e


        self.SetTitle("ACIFT")
        self._doLayout()
        self._setBindings()

     
    def _doLayout(self):
        self.Layout()
        self.Centre()
        self.MainFrame_menubar = wx.MenuBar()
        self.ID_OPEN=111
        self.ID_ABOUT=101
        self.ID_EXIT=110
        menu_file = wx.Menu()
        menu_file.Append(self.ID_OPEN, "Open", "")
        menu_file.AppendSeparator()
        menu_file.Append(self.ID_EXIT, "Exit", "Exit the program")
        self.MainFrame_menubar.Append(menu_file, "File")
        menu_about = wx.Menu()
        self.MainFrame_menubar.Append(menu_about, "About")
        self.SetMenuBar(self.MainFrame_menubar)
    
    def _setBindings(self):
        self.background = wx.Panel(self, -1)
        self.background.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.background.SetFocus()
        wx.EVT_MENU(self, self.ID_OPEN, self.openFile)
        #wx.EVT_MENU(self, ID_EXIT, self.terminateProgram)
        self.bindings = {
                        wx.WXK_PAGEDOWN: self.Next,
                        wx.WXK_PAGEUP: self.Prev,
                        wx.WXK_SPACE: self.openFile
                        }


    def openFile(self, event = None):
        openFileDialog = wx.FileDialog(self, "Open a file", self.dir, "",
        "All files (*.*)|*.*|BMP files (*.bmp)|*.bmp|JPEG files (*.jpg)|*.jpg|Zip files (*.zip)|*.zip"
        , wx.OPEN | wx.FD_MULTIPLE | wx.FD_PREVIEW)
        if openFileDialog.ShowModal() == wx.ID_OK:
            #Default case - working with several files
            self.files=openFileDialog.GetFilenames()
            self.dir=openFileDialog.GetDirectory() + "/"
            self.current = 0
            self.isZip = False

            #We are working with a zip file
            if len(self.files) == 1 and self.files[0].endswith(".zip"):
                self.zip = zipfile.ZipFile(self.files[0], "r")
                self.files = self.zip.namelist()
                print self.files
                self.dir = ""
                self.isZip = True

            #Working with a directory (not used at the moment)
            elif len(self.files) == 1 and os.path.isdir(self.files[0]):
                self.dir = self.files[0] + "/"
                self.files = [file for file in os.listdir(self.dir) if file.endswith(".jpg")]

            #Working with only one file - open all files in the folder
            elif len(self.files) == 1:
                self.current = self.files[0]
                self.files = [file for file in os.listdir(self.dir) if file.endswith(".jpg")]
                self.current = self.files.index(self.current)

            self.size = len(self.files)
            openFileDialog.Destroy()
            #TODO: Make this work with """ and %s
            print "*"*20
            print "Loading filenames"
            print "Current Dir:", self.dir
            print "Files", self.files
            print "Starting with", self.current
            print "*"*20
            self.openImage()
        
    def openImage(self):
        #Is this needed?
        self.bmp.Destroy()
        del self.image
        self.image = self.getImage()
        self.bmp = pilToBitmap(self.image)
        self.picture.SetBitmap(self.bmp)
        self.sizer.Fit(self)
        
    def getImage(self):
        if self.isZip == True:
            self.stream = cStringIO.StringIO(self.zip.read(self.files[self.current]))
            #bmp = wx.BitmapFromImage( wx.ImageFromStream( stream ))
            return Image.open(self.stream)
        return Image.open(self.dir + self.files[self.current])
    
    def OnKeyDown(self, event):
        #TODO: Write events for special buttons
        keycode = event.GetKeyCode()
        print keycode
        try:
            self.bindings[keycode]()
        except Exception,e:
            print Exception, e



#-----------------------------------#
#                                   #
#           Events                  #
#                                   #
#-----------------------------------#

    def Next(self):
        print "Next!"
        self.current += 1
        if self.current >= self.size:
            self.current = 0
        print "Going to image %d out of %d." %(self.current + 1, self.size)
        self.openImage()
    
    def Prev(self):
        print "Prev!"
        self.current -= 1
        if self.current < 0:
            self.current = self.size - 1
        print "Going to image %d out of %d." %(self.current + 1, self.size)
        self.openImage()


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
