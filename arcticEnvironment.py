#Written by Abdulaziz Albastaki in January 2021
from panda3d.core import BitMask32, AmbientLight, PointLight, DirectionalLight
from objectLib import dock
from water import water
class environment():
    def __init__(self,render,loader):
        self.loader = loader
        def make(x):
            self.fakeWorld = loader.loadModel('assets/environment/arctic/nature/world.bam')
            self.fakeWorld.reparentTo(render)
            self.fakeWorld.setScale(100)
            self.fakeWorld.setSz(10000)
            self.fakeWorld.setZ(-1010)
            self.fakeWorld.setY(x)
            self.fakeWorld.flattenStrong()
        make(0)
        make(90000)
        make(-100000)
        self.river = water(render, loader, (36728.9, 31409.8, -150), 34000, 300000)  # 200,200
        self.world = loader.loadModel('assets/environment/arctic/nature/world.bam')
        self.maximumHeight = 1350  #  4000
        self.world.reparentTo(render)
        self.world.setScale(100)
        self.world.setSz(10000)
        self.world.setZ(-1010)
        self.world.setY(0)
        self.world.setCollideMask(BitMask32.bit(1))
        self.world.hide()
        self.town()
        self.setupLights()

        def generatedMap():
            self.building16909 = self.loader.loadModel('assets/environment/arctic/buildings/building1.bam')
            self.building16909.setScale(3)
            self.building16909.setPos(45938.30078125, 43149.30078125, -9.174566268920898)
            self.building16909.setH(-89.99999237060547)
            self.building16909.reparentTo(render)

            self.building11699 = self.loader.loadModel('assets/environment/arctic/buildings/building1.bam')
            self.building11699.setScale(3)
            self.building11699.setPos(45938.30078125, 42579.30078125, -9.174566268920898)
            self.building11699.setH(-89.99999237060547)
            self.building11699.reparentTo(render)

            self.tree17425 = self.loader.loadModel('assets/environment/arctic/nature/tree.bam')
            self.tree17425.setScale(12)
            self.tree17425.setPos(45818.30078125, 42774.30078125, -9.174566268920898)
            self.tree17425.setH(-89.99999237060547)
            self.tree17425.reparentTo(render)

            self.tree18761 = self.loader.loadModel('assets/environment/arctic/nature/tree.bam')
            self.tree18761.setScale(12)
            self.tree18761.setPos(45818.30078125, 42894.30078125, -9.174566268920898)
            self.tree18761.setH(-89.99999237060547)
            self.tree18761.reparentTo(render)

            self.tree19412 = self.loader.loadModel('assets/environment/arctic/nature/tree.bam')
            self.tree19412.setScale(12)
            self.tree19412.setPos(45938.30078125, 42834.30078125, -9.174566268920898)
            self.tree19412.setH(-89.99999237060547)
            self.tree19412.reparentTo(render)
        generatedMap()

    def setupLights(self):
        ambiet = AmbientLight('ambient')
        ambiet.setColor((0.2,0.2,0.2,1))
        alight = render.attachNewNode(ambiet)
        render.setLight(alight)
        dlight = DirectionalLight('dlight')
        dlight.setColor((0.8, 0.8, 0.8, 1))
        dlnp = render.attachNewNode(dlight)
        dlnp.setHpr(0, -45, 0)
        render.setLight(dlnp)
    def town(self):
        port = dock(self.loader,(45150, 42978.6, 30))
