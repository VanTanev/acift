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
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.dirname = "."
        self.openFile(None)

        self.SetTitle("ACIFT")
        self.__do_layout()

        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        wx.EVT_MENU(self, ID_OPEN, self.openFile)
        wx.EVT_MENU(self, ID_EXIT, self.terminateProgram)

    def terminateProgram(self, event):
        self.Close(True)

    def OnKeyDown(self, event):
        keycode = event.GetKeyCode()
        print chr(keycode)
        event.Skip()

        
    def __do_layout(self):


        self.Layout()
        # Menu Bar
        self.MainFrame_menubar = wx.MenuBar()
        menu_file = wx.Menu()
        menu_file.Append(ID_OPEN, "Open", "")
        menu_file.AppendSeparator()
        menu_file.Append(ID_EXIT, "Exit", "Exit the program")
        self.MainFrame_menubar.Append(menu_file, "File")
        menu_about = wx.Menu()
        self.MainFrame_menubar.Append(menu_about, "About")
        self.SetMenuBar(self.MainFrame_menubar)
        # Menu Bar end

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
        try:
            self.current_image
        except AttributeError:
            pass
        else:
            self.current_image.Destroy()
        self.bitmap = wx.StaticBitmap(self, -1, self.bmp)
        self.current_image = self.sizer.Add(self.bitmap, 0, wx.EXPAND|wx.SHAPED, 0)
        self.SetSizer(self.sizer)
        self.sizer.Fit(self)        
