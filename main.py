#Written by Abdulaziz Albastaki in January 2021
from direct.showbase.ShowBase import ShowBase
from arcticEnvironment import environment
from player import Player
from panda3d.core import loadPrcFile
loadPrcFile("configuration.prc")
import simplepbr

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)   # initialise
        base.set_background_color(0.53,0.81,0.92)
        world = environment(self.render,self.loader)
        # simplepbr.init(use_normal_maps=True) -- UNCOMMENT THIS OUT
        base.setFrameRateMeter(True)
        self.disableMouse()
        self.player = Player(self.camera,self.accept,self.render,self.loader,world.maximumHeight)
        self.render.setShaderAuto() # -- COMMENT THIS OUT
        self.updateTask = taskMgr.add(self.player.playerUpdate, "update")
app = MyApp()
app.run()