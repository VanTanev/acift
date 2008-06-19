import wx


class KeyEvent(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)

        panel = wx.Panel(self, -1)
        panel.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        panel.SetFocus()

        self.Centre()
        self.Show(True)


def OnKeyDown(self, event):
    keycode = event.GetKeyCode()
    print keycode
    event.Skip()
