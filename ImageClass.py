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

class ImageFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.dirname = "."
        self.openFile(None)
        self.image = Image.open(self.dir + "/" + self.files[0])
        self.bmp = pilToBitmap(self.image)
        self.bitmap = wx.StaticBitmap(self, -1, self.bmp)
        self.SetTitle("ACIFT")
        self.__do_layout()
        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)

    def OnKeyDown(self, event):
        keycode = event.GetKeyCode()
        print keycode
        event.Skip()

        
    def __do_layout(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.bitmap, 0, wx.EXPAND|wx.SHAPED, 0)
        self.SetSizer(sizer)
        sizer.Fit(self)
        self.Layout()
                # Menu Bar
        self.MainFrame_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.NewId(), "Open", "", wx.ITEM_NORMAL)
        wxglade_tmp_menu.AppendSeparator()
        wxglade_tmp_menu.Append(wx.NewId(), "Exit", "", wx.ITEM_NORMAL)
        self.MainFrame_menubar.Append(wxglade_tmp_menu, "File")
        wxglade_tmp_menu = wx.Menu()
        self.MainFrame_menubar.Append(wxglade_tmp_menu, "About")
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
            openFileDialog.Destroy()
