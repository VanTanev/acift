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
		#Frame.__init__(self,master)
		self.im = Image.open("1.jpg")
		self.canvas = Canvas(master, height=self.im.size[1]+20, width=self.im.size[0]+20)
		self.canvas.pack(side=LEFT,fill=BOTH,expand=1)
		self.photo = ImageTk.PhotoImage(self.im)
		self.item = self.canvas.create_image(10,10,anchor=NW, image=self.photo)
		print "ASD"


tk = Tk()
tk.title("ACIF - A Comic is Fine too")

#execute.master.title("ACIF - A Comic is Fine too")
try:
	print "ASDD"
	execute = ACIF(tk)
	tk.mainloop()	
    
except Exception, e:
    print >>sys.stderr, e
    print "USAGE: HelloImage <image filename>"
    sys.exit(1)


