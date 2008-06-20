import wx
ID_OPEN=111
ID_ABOUT=101
ID_EXIT=110

class MenuBar():
    def __init__(self, master):
        Main_MenuBar = wx.MenuBar()
        menu_file = wx.Menu()
        menu_file.Append(ID_OPEN, "Open", "")
        menu_file.AppendSeparator()
        menu_file.Append(ID_EXIT, "Exit", "Exit the program")
        Main_MenuBar.Append(menu_file, "File")
        menu_about = wx.Menu()
        Main_MenuBar.Append(menu_about, "About")
        master.SetMenuBar(Main_MenuBar)
        
        master.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        wx.EVT_MENU(master, ID_OPEN, master.openFile)
        wx.EVT_MENU(master, ID_EXIT, self.terminateProgram)

    def terminateProgram(self, event):
        master.Close(True)

    def OnKeyDown(self, event):
        keycode = event.GetKeyCode()
        print chr(keycode)
        event.Skip()
