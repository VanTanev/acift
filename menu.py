import wx

class MenuBar():
    def __init__(self, master):
        ID_OPEN=111
        ID_ABOUT=101
        ID_EXIT=110
        self.master = master #needed for internal functions
        Main_MenuBar = wx.MenuBar()
        menu_file = wx.Menu()
        menu_file.Append(ID_OPEN, "Open", "")
        menu_file.AppendSeparator()
        menu_file.Append(ID_EXIT, "Exit", "Exit the program")
        Main_MenuBar.Append(menu_file, "File")
        menu_about = wx.Menu()
        Main_MenuBar.Append(menu_about, "About")
        master.SetMenuBar(Main_MenuBar)
        
        wx.EVT_MENU(master, ID_OPEN, master.openFile)
        wx.EVT_MENU(master, ID_EXIT, self.terminateProgram)

    def terminateProgram(self, event):
        self.master.Close(True)

