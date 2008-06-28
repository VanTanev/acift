#!/usr/bin/python
from utils import *
#from menu import MenuBar

class ACIFT(wx.PySimpleApp):
    def __init__(self, *args, **kwargs):
        wx.PySimpleApp.__init__(self, *args, **kwargs)


if __name__ == "__main__":
    ACIFT = ACIFT()

    wx.InitAllImageHandlers()

    Main = ImageFrame(None, -1, "")
    Menu = MenuBar(Main)
    
    ACIFT.SetTopWindow(Main)
    
    Main.Show()
    ACIFT.MainLoop()
