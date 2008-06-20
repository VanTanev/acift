#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wx
import Image

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
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)

        background = wx.Panel(self, -1)
        background.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.dirname = "."
        self.SetTitle("ACIFT")
        self.__do_layout()


    def OnKeyDown(self, event):
        keycode = event.GetKeyCode()
        print chr(keycode)
        event.Skip()        
     
    def __do_layout(self):
        self.Layout()


    def openFile(self, event):
        openFileDialog = wx.FileDialog(self, "Open a file", self.dirname, "", "*.jpg", wx.OPEN|wx.FD_MULTIPLE)
        if openFileDialog.ShowModal() == wx.ID_OK:
            self.files=openFileDialog.GetFilenames()
            self.dir=openFileDialog.GetDirectory()
            print "*"*20
            print "Loading filenames"
            print "Current Dir:", self.dir
            print "Files",self.files
            print "*"*20
            self.openImage()
        openFileDialog.Destroy()
        
    def openImage(self):
        self.image = Image.open(self.dir + "/" + self.files[0])
        self.bmp = pilToBitmap(self.image)
        self.bitmap = wx.StaticBitmap(self, -1, self.bmp)
        self.current_image = self.sizer.Add(self.bitmap, 0, wx.EXPAND|wx.SHAPED, 0)
        self.SetSizer(self.sizer)
        self.sizer.Fit(self)        
