#HelloImage - display an image file
# -*- coding: utf-8 -*-
# Simon Peverett - October 2003
# uses the PIL module: http://www.pythonware.com/products/pil/
# developed using ActivePython 2.2: http://www.activestate.com

from Tkinter import *
import Image            #PIL
import ImageTk          #PIL
import sys
import getopt



class ACIF(Frame):
    def __init__(self, master=None):
    	Frame.__init__(self,master)
    	#self = TK()
        self.pack(fill=BOTH, expand=1)
        im = Image.open("1.jpg")
        self.canvas = Canvas(self, height=1000, width=500)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.canvas.grid(row=0, column=0, sticky='nesw')
        photo = ImageTk.PhotoImage(im)
        item = self.canvas.create_image(10,10,anchor=NW, image=photo)

execute = ACIF()
execute.master.title("ACIF - A Comic is Fine too")
try:
    execute.mainloop()

except Exception, e:
    print >>sys.stderr, e
    print "USAGE: HelloImage <image filename>"
    sys.exit(1)

