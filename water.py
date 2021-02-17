#Written by Abdulaziz Albastaki in January 2021
from direct.showbase.ShowBase import ShowBase   # import the bits of panda
from panda3d.core import TextureStage, AmbientLight

class water():
    def __init__(self,render,loader,location,sizeX,sizeY):
        self.water = loader.loadModel('assets/environment/arctic/nature/newwater.egg')
        self.water.setPos(location)
        self.water.setSx(sizeX)
        self.water.setSy(sizeY)
        self.newTS = TextureStage('ts')
        self.normal_TS = TextureStage('ts')
        self.normal_TS.setMode(TextureStage.MNormal)
        self.water.setTexture(self.newTS,loader.loadTexture('assets/environment/arctic/nature/textures/water_colormap.jpg'))
        self.water.setTexScale(self.newTS, 40)
        self.water.setTexture(self.normal_TS, loader.loadTexture('assets/environment/arctic/nature/textures/water_normalmap.jpg'))
        self.water.setTexScale(self.normal_TS, 40)
        ambiet = AmbientLight('ambient')
        ambiet.setColor((0.2, 0.2, 0.2, 1))
        alight = self.water.attachNewNode(ambiet)
        self.water.setLight(alight)
        self.water.reparentTo(render)