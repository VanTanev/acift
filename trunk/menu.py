import Tkinter as Tk

"""
This class contains the menu bar and its event handlers
"""
class MenuBar(Tk.Frame):
    def __init__(self, master = None):
        Tk.Frame.__init__(self, master)
        self.menubar = Tk.Frame(master, relief = Tk.RAISED, borderwidth = 1)
        self.menubar.grid(column = 0, sticky = Tk.NW)

        self.fileButton = Tk.Menubutton(self.menubar, text = "File")
        self.fileButton.grid(column = 0, sticky = Tk.NW)
        self.fileButton.menu = Tk.Menu(self.fileButton)
        self.fileButton.menu.add_command(label = "Open", command = self.openButton)
        self.fileButton['menu'] = self.fileButton.menu
        return

    def openButton(self):
        self.pages = self.master.controlFrames.openFiles()
        
        if self.pages:
            print self.pages
            self.master.showImage(self.pages[0])
        else:
            print "No image selected"

