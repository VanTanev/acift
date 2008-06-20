from utils import *
#from menu import MenuBar

class ACIFT(wx.PySimpleApp):
    def __init__(self, *args, **kwargs):
        wx.PySimpleApp.__init__(self, *args, **kwargs)
        

if __name__ == "__main__":
    ACIFT = ACIFT()

    wx.InitAllImageHandlers()
   
    MainFrame = ImageFrame(None, -1, "")
    teh_menu = MenuBar(MainFrame)
    

    ACIFT.SetTopWindow(MainFrame)
    MainFrame.Show()
    ACIFT.MainLoop()

