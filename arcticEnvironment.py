#Written by Abdulaziz Albastaki in January 2021
from panda3d.core import BitMask32, AmbientLight, PointLight, DirectionalLight
from objectLib import dock, water
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
            self.fakeWorld.setShaderAuto()
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

            self.tree14160 = self.loader.loadModel('assets/environment/arctic/nature/tree.bam')
            self.tree14160.setScale(9)
            self.tree14160.setPos(45723.828125, 43787.11328125, -9.174566268920898)
            self.tree14160.setH(90.00000762939453)
            self.tree14160.flattenStrong()
            self.tree14160.reparentTo(render)

            self.tree14165 = self.loader.loadModel('assets/environment/arctic/nature/tree.bam')
            self.tree14165.setScale(9)
            self.tree14165.setPos(45723.828125, 43697.11328125, -9.174566268920898)
            self.tree14165.setH(90.00000762939453)
            self.tree14165.flattenStrong()
            self.tree14165.reparentTo(render)

            self.tree15679 = self.loader.loadModel('assets/environment/arctic/nature/tree.bam')
            self.tree15679.setScale(9)
            self.tree15679.setPos(45633.828125, 43742.11328125, -9.174566268920898)
            self.tree15679.setH(90.00000762939453)
            self.tree15679.flattenStrong()
            self.tree15679.reparentTo(render)

            # self.light7208.reparentTo(render)
            # render.setLight(self.light7208.getChild(1).getChild(0))
            self.cafe16403 = self.loader.loadModel('assets/environment/arctic/buildings/cafe.bam')
            self.cafe16403.setScale(3)
            self.cafe16403.setPos(45472.99609375, 43970.4140625, -9.174566268920898)
            self.cafe16403.setCollideMask(BitMask32.bit(4))
            self.cafe16403.setH(-90.00000762939453)
            self.cafe16403.flattenStrong()
            self.cafe16403.reparentTo(render)


        generatedMap()

    def setupLights(self):
        ambiet = AmbientLight('ambient')
        ambiet.setColor((0.1,0.1,0.1,1))
        alight = render.attachNewNode(ambiet)
        render.setLight(alight)
        dlight = DirectionalLight('dlight')
        dlight.setColor((0.8, 0.8, 0.8, 1))
        dlnp = render.attachNewNode(dlight)
        dlnp.setHpr(0, -45, 0)
        render.setLight(dlnp)
    def town(self):
        port = dock(self.loader,(45150, 42978.6, 30))
