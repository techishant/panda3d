from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        properties = WindowProperties()
        properties.setSize(1000,756)
        self.win.requestProperties(properties)

app = App()
app.run()