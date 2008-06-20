#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
import Image
import os
import menu


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

ID_OPEN=111
ID_ABOUT=101
ID_EXIT=110

class ImageFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        #self.events = events()
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)

        #Default data - this needs to be changed at some point
        self.dir = "."
        self.files = [u"1.jpg"]
        self.current = 0
        self.size = 1
        
        self.sizer = wx.BoxSizer(wx.VERTICAL | wx.EXPAND)
        self.background_panel = wx.Panel(self, -1)
#        self.openFile(None)
        try:
            self.image = Image.open(self.dir + "/" + self.files[self.current])
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
        menu_file = wx.Menu()
        menu_file.Append(ID_OPEN, "Open", "")
        menu_file.AppendSeparator()
        menu_file.Append(ID_EXIT, "Exit", "Exit the program")
        self.MainFrame_menubar.Append(menu_file, "File")
        menu_about = wx.Menu()
        self.MainFrame_menubar.Append(menu_about, "About")
        self.SetMenuBar(self.MainFrame_menubar)
    
    def _setBindings(self):
        self.background = wx.Panel(self, -1)
        self.background.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.background.SetFocus()
        wx.EVT_MENU(self, ID_OPEN, self.openFile)
        #wx.EVT_MENU(self, ID_EXIT, self.terminateProgram)
        self.bindings = {
                        wx.WXK_PAGEDOWN: self.Next,
                        wx.WXK_PAGEUP: self.Prev
                        }


    def openFile(self, event):
        openFileDialog = wx.FileDialog(self, "Open a file", self.dir, "", "*.jpg", wx.OPEN | wx.FD_MULTIPLE | wx.FD_PREVIEW)
        if openFileDialog.ShowModal() == wx.ID_OK:
            self.files=openFileDialog.GetFilenames()
            self.dir=openFileDialog.GetDirectory()
            self.current = 0

            if len(self.files) == 1 and os.path.isdir(self.files[0]):
                self.dir = self.files[0]
                self.files = [file for file in os.listdir(self.dir) if file.endswith(".jpg")]
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
        #self.image.Destroy()
        self.image = Image.open(self.dir + "/" + self.files[self.current])
        self.bmp = pilToBitmap(self.image)
        self.picture.SetBitmap(self.bmp)
        self.sizer.Fit(self)
        
    def OnKeyDown(self, event):
        #TODO: Write events for special buttons
        keycode = event.GetKeyCode()
        try:
            self.bindings[keycode]()
        except Exception,e:
            print Exception, e

    def Next(self):
        print "Next!"
        self.current += 1
        print "Going to image %d out of %d." %(self.current,self.size)
        if self.current >= self.size:
            self.current = 0
        self.openImage()
    
    def Prev(self):
        print "Prev!"
        self.current -= 1
        print "Going to image %d out of %d." %(self.current,self.size)
        if self.current < 0:
            self.current = self.size
        self.openImage()
