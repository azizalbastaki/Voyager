#Written by Abdulaziz Albastaki in January 2021
from direct.showbase.ShowBase import ShowBase
from arcticEnvironment import environment
from player import Player
import simplepbr

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)   # initialise
        simplepbr.init()
        world = environment(self.render,self.loader)
        self.set_background_color(0.53,0.81,0.92)
        base.setFrameRateMeter(True)
        self.disableMouse()
        self.player = Player(self.camera,self.accept,self.render,self.loader,world.maximumHeight)
        self.render.setShaderAuto()
        self.updateTask = taskMgr.add(self.player.playerUpdate, "update")
app = MyApp()
app.run()
