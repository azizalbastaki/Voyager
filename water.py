#Written by Abdulaziz Albastaki in January 2021
from direct.showbase.ShowBase import ShowBase   # import the bits of panda
from panda3d.core import TextureStage, AmbientLight, CompassEffect

class water():
    def __init__(self,render,loader,location,sizeX,sizeY):
        self.water = loader.loadModel('assets/environment/arctic/nature/newwater.egg')
        self.normalmaptexture = loader.loadTexture("assets/environment/arctic/nature/textures/water_normalmap.jpg", "assets/environment/arctic/nature/textures/water_heightmap.png")
        self.water.setPos(location)
        self.water.setSx(sizeX)
        self.water.setSy(sizeY)
        self.newTS = TextureStage('ts')
        self.normal_TS = TextureStage('tsnormal')
        #self.normal_TS.setMode(TextureStage.MNormal)
        self.water.setTexture(self.newTS,loader.loadTexture('assets/environment/arctic/nature/textures/water_colormap.jpg'))
        self.water.setTexScale(self.newTS, 60)
        self.water.setTexture(self.normal_TS, self.normalmaptexture)
        self.water.setTexScale(self.normal_TS, 60)
        ambiet = AmbientLight('ambient')
        ambiet.setColor((1, 1, 1, 1))
        alight = self.water.attachNewNode(ambiet)
        self.water.setLight(alight)
        self.water.reparentTo(render)
        self.skybox = loader.loadModel("assets/environment/arctic/nature/skybox.bam")
        self.skybox.setPos(location)
        self.skybox.setScale(2000)
        self.skybox.setEffect(CompassEffect.make(render))
        self.skybox.reparentTo(render)