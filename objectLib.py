#Written by Abdulaziz Albastaki in January 2021
from panda3d.core import TextureStage,BitMask32, AmbientLight
class dock():
    def __init__(self,loader,location):
        self.loader = loader
        self.port = self.loader.loadModel("assets/environment/arctic/buildings/port.bam")
        self.port.setPos(location)
        self.port.setH(90)
        self.port.setCollideMask(BitMask32.bit(1))
        #ambiet = AmbientLight('ambient')
        #ambiet.setColor((0.2, 0.2, 0.2, 1))
        #alight = self.port.attachNewNode(ambiet)
        #self.port.setLight(alight)
        self.port.setShaderAuto()
        self.port.reparentTo(render)
class collisions():
    def __init__(self,loader):
        self.name = "building1_collision"
        self.file = "assets/environment/arctic/buildings/building1collision.bam"
        self.loader = loader
        self.bitmask = 0
        self.otherCommands = ["hide"]
        self.gameObject = self.loader.loadModel(self.file)
class building1():
    def __init__(self,loader):
        self.name = "building1"
        self.file = "assets/environment/arctic/buildings/building1.bam"
        self.loader = loader
        self.bitmask = 4
        self.otherCommands = ["flattenStrong"]
        self.gameObject = self.loader.loadModel(self.file)
class tree1():
    def __init__(self,loader):
        self.name = "tree1"
        self.file = "assets/environment/arctic/nature/tree.bam"
        self.loader = loader
        self.otherCommands = ["flattenStrong"]
        self.gameObject = self.loader.loadModel(self.file)
class walkway1():
    def __init__(self,loader):
        self.name = "walkway1"
        self.file = "assets/environment/arctic/buildings/walkway.bam"
        self.loader = loader
        self.bitmask = 4
        self.otherCommands = ["flattenStrong"]
        self.gameObject = self.loader.loadModel(self.file)
class water():
    def __init__(self,render,loader,location,sizeX,sizeY):
        self.water = loader.loadModel('assets/environment/arctic/nature/water.bam')
        self.water.setPos(location)
        self.water.setSx(sizeX)
        self.water.setSy(sizeY)
        self.newTS = TextureStage('ts')
        self.normal_TS = TextureStage('normal')
        self.normal_TS.setMode(TextureStage.MNormal)
        self.water.setTexture(self.newTS, loader.loadTexture('assets/environment/arctic/nature/textures/water_colormap.jpg'))
        self.water.setTexScale(self.newTS, 80)
        self.water.setTexture(self.normal_TS, loader.loadTexture('assets/environment/arctic/nature/textures/water_normalmap.jpg'))
        self.water.setTexScale(self.normal_TS, 80)
        self.water.setShaderAuto()
        ambiet = AmbientLight('ambient')
        ambiet.setColor((0.2, 0.2, 0.2, 1))
        alight = self.water.attachNewNode(ambiet)
        #self.water.setLight(alight)
        self.water.reparentTo(render)
        self.skybox = loader.loadModel("assets/environment/arctic/nature/skybox.bam")
        self.skybox.setPos(location)
        self.skybox.setScale(2000)
        #self.skybox.reparentTo(render)
class cafe1():
    def __init__(self,loader):
        self.name = "cafe1"
        self.file = "assets/environment/arctic/buildings/cafe.bam"
        self.loader = loader
        self.bitmask = 4
        self.otherCommands = ["flattenStrong"]
        self.gameObject = self.loader.loadModel(self.file)
class light():
    def __init__(self,loader):
        self.name = "light"
        self.file = "assets/base/models/light.bam"
        self.loader = loader
        self.otherCommands = []
        self.gameObject = self.loader.loadModel(self.file)