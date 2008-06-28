import wx


class Events():
    def _setBindings(self):
        self.background = wx.Panel(self, -1)
        self.background.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.background.SetFocus()
        self.bindings = {
                        wx.WXK_PAGEDOWN: self.Next,
                        wx.WXK_PAGEUP: self.Prev,
                        wx.WXK_HOME: self.First,
                        wx.WXK_END: self.Last,
                        wx.WXK_SPACE: self.Next,
                        ord('D'): self.fitScreen,
                        wx.WXK_UP: self.scrollUp,
                        wx.WXK_DOWN: self.scrollDown,
                        ord('='): self.makeBigger,
                        ord('O'): self.openFile,
                        #FIXME: This seems to be needed by Windows
                        43: self.makeBigger,
                        ord('-'): self.makeSmaller,
                        ord('F'): self.fullScreen,
                        }

    def OnKeyDown(self, event):
        #TODO: Write events for special buttons - Done?
        keycode = event.GetKeyCode()
        try:
            self.bindings[keycode]()
        except Exception,e:
            print Exception, e			

#-----------------------------------#
#                                   #
#           Events                  #
#                                   #
#-----------------------------------#
    def fullScreen(self, value = -1):
        #ACIFT.ShowFullScreen(self.fit)
        if value != -1:
            self.options.fullScreen = value
        else:
            self.options.fullScreen = True - self.options.fullScreen
        print "Fullscreen is now set to: %s"% self.options.fullScreen
        self.ShowFullScreen(self.options.fullScreen)
        #self.ShowFullScreen(self.options.fullScreen, style = 0)
        #Style = 0, lol :)

    def fitScreen(self):
    	#TODO: Make this be fullscreen
        self.options.fit = True - self.options.fit
        print "Fit-to-screen is now set to: %s"% self.options.fit
        self.openImage()
    
    #TODO: make this work
    def scrollDown(self):
        print "Scroll Down!"
    
    #TODO: make this work
    def scrollUp(self):
        print "Scroll Up!"
        
    #TODO: make these two work dynamically
    def makeBigger(self):
        #will not work if the image is set to a specific size
        if not self.options.fit:
            self.processedImage = self.resize(
                self.rawImage,
                (self.processedImage.size[0]*1.2, self.processedImage.size[1]*1.2))
            self.showImage()
        
    def makeSmaller(self):
        #will not work if the image is set to a specific size
        if not self.options.fit:
            if self.processedImage.size[0] >= 100 and self.processedImage.size[1] >= 100:
                self.processedImage = self.resize(
                    self.rawImage,
                    (self.processedImage.size[0]/1.2, self.processedImage.size[1]/1.2))
            self.showImage()
        
    def Next(self):
        self.source.current += 1
        if self.source.current >= self.source.size:
            self.source.current = 0
        print "Going to image %d out of %d." %(self.source.current + 1, self.source.size)
        self.openImage()
    
    def Prev(self):
        self.source.current -= 1
        if self.source.current < 0:
            self.source.current = self.source.size - 1
        print "Going to image %d out of %d." %(self.source.current + 1, self.source.size)
        self.openImage()

    def First(self):
        self.source.current = 0
        print "Going to image %d out of %d." %(self.source.current + 1, self.source.size)
        self.openImage()
    
    def Last(self):
        self.source.current = self.source.size - 1
        print "Going to image %d out of %d." %(self.source.current + 1, self.source.size)
        self.openImage()
