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
            self.building18297 = self.loader.loadModel('assets/environment/arctic/buildings/building1.bam')
            self.building18297.setScale(4)
            self.building18297.setPos(45398.30078125, 43389.30078125, -9.174566268920898)
            self.building18297.setCollideMask(BitMask32.bit(4))
            self.building18297.setH(0.0)
            self.building18297.reparentTo(render)

            self.building1_collision8664 = self.loader.loadModel(
                'assets/environment/arctic/buildings/building1collision.bam')
            self.building1_collision8664.setScale(4)
            self.building1_collision8664.setPos(45398.30078125, 43389.30078125, -9.174566268920898)
            self.building1_collision8664.setCollideMask(BitMask32.bit(0))
            self.building1_collision8664.setH(0.0)
            self.building1_collision8664.hide()
            self.building1_collision8664.reparentTo(render)

            self.tree12698 = self.loader.loadModel('assets/environment/arctic/nature/tree.bam')
            self.tree12698.setScale(22)
            self.tree12698.setPos(45884.0, 43433.58203125, -9.174566268920898)
            self.tree12698.setH(0.0)
            self.tree12698.reparentTo(render)
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
