from cStringIO import StringIO

class Zip():
    def __init__(self, dir = "./", files = ""):
        self.dir = dir
        self.files = files

    def getImage(self):
        return StringIO(self.zip.read(self.files[self.current]))

class Files():
    def __init__(self, dir = "./", files = ""):
        self.dir = dir
        self.files = files

    def getImage(self):
        return self.dir + self.files[self.current]

