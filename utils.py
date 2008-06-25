"""
This file serves as a hub for all imports, so that the Main
can look pretty.
"""

from menu import *
from ImageClass import *

"""
Nice trick - keep this in mind :)
source = self.source
            source.one = "ASDASDASDASDASDASD"
            print self.source.one
"""

"""
From ImageClass
Old code:
    def getImage(self):
        if self.isZip == True:
            self.stream = StringIO(self.zip.read(self.files[self.current]))
            return self.stream
            return Image.open(self.stream)
        return self.dir + self.files[self.current]
        return Image.open(self.dir + self.files[self.current])
"""

def get_events():
    return [_ for _ in dir(wx) if _.startswith("EVT") ]
            
def get_FD_commands():
    return [_ for _ in dir(wx) if _.startswith("FD") ]

def get_StaticBitmap_Set():
    return [_ for _ in dir(wx.StaticBitmap) if _.startswith("Set") ]


if __name__ == '__main__':
    print get_events()
    #get_FD_commands()
    #get_StaticBitmap_Set()
