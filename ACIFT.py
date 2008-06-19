from utils import *

def setBindings(object):
    object.Bind(wx.EVT_KEY_DOWN, OnKeyDown)
    print "Binded!"

class ACIFT(wx.PySimpleApp):
    def __init__(self, *args, **kwargs):
        wx.PySimpleApp.__init__(self, *args, **kwargs)
        

if __name__ == "__main__":
    ACIFT = ACIFT()
    #ACIFT.setBindings = setBindings(ACIFT)
    wx.InitAllImageHandlers()
    
    print menu
    
    Main = ImageFrame(None, -1, "")
    
    #Main.setBindings = setBindings(Main)
    ACIFT.SetTopWindow(Main)
    Main.Show()
    ACIFT.MainLoop()

