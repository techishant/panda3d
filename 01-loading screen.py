"""
https://arsthaumaturgis.github.io/Panda3DTutorial.io/tutorial/tut_lesson01.html
"""

from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties

class App(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # changing screen size 
        properties = WindowProperties()
        properties.setSize(900,656)
        self.win.requestProperties(properties)

        # disable mouses
        self.disableMouse()

App = App()
App.run()