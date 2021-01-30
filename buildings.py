#Written by Abdulaziz Albastaki in January 2021
from panda3d.core import CollideMask,BitMask32
class dock():
    def __init__(self,loader,location):
        self.loader = loader
        self.port = self.loader.loadModel("assets/environment/buildings/port.bam")
        self.port.setPos(location)
        self.port.setH(90)
        #self.port.setScale(4)
        self.port.setCollideMask(BitMask32.bit(0))
        self.port.reparentTo(render)