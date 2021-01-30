#Written by Abdulaziz Albastaki in January 2021
from direct.showbase.ShowBase import ShowBase   # import the bits of panda
from panda3d.core import TextureStage, CollideMask

class water(ShowBase):
    def __init__(self,render,loader,location,sizeX,sizeY):
        self.water = loader.loadModel('assets/environment/nature/water.bam')
        self.water.setPos(location)
        self.water.setSx(sizeX)
        self.water.setSy(sizeY)
        self.newTS = TextureStage('ts')
        self.normal_TS = TextureStage('normal')
        self.normal_TS.setMode(TextureStage.MNormal)
        self.water.setTexture(self.newTS,loader.loadTexture('assets/environment/nature/textures/water_colormap.jpg'))
        self.water.setTexScale(self.newTS, 40)
        self.water.setTexture(self.normal_TS, loader.loadTexture('assets/environment/nature/textures/water_normalmap.jpg'))
        self.water.setTexScale(self.normal_TS, 20)
        self.water.setCollideMask(CollideMask.bit(0))

        self.water.reparentTo(render)


