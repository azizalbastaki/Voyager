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
            self.walkway18112 = self.loader.loadModel('assets/environment/arctic/buildings/walkway.bam')
            self.walkway18112.setScale(12)
            self.walkway18112.setPos(45183.828125, 43877.11328125, -9.174566268920898)
            self.walkway18112.setCollideMask(BitMask32.bit(7))
            self.walkway18112.setH(90.00000762939453)
            self.walkway18112.flattenStrong()
            self.walkway18112.reparentTo(render)

            self.walkway17662 = self.loader.loadModel('assets/environment/arctic/buildings/walkway.bam')
            self.walkway17662.setScale(12)
            self.walkway17662.setPos(45183.828125, 43517.11328125, -9.174566268920898)
            self.walkway17662.setCollideMask(BitMask32.bit(7))
            self.walkway17662.setH(90.00000762939453)
            self.walkway17662.flattenStrong()
            self.walkway17662.reparentTo(render)

            self.walkway1156 = self.loader.loadModel('assets/environment/arctic/buildings/walkway.bam')
            self.walkway1156.setScale(12)
            self.walkway1156.setPos(45183.828125, 43157.11328125, -9.174566268920898)
            self.walkway1156.setCollideMask(BitMask32.bit(7))
            self.walkway1156.setH(90.00000762939453)
            self.walkway1156.flattenStrong()
            self.walkway1156.reparentTo(render)

            self.walkway18646 = self.loader.loadModel('assets/environment/arctic/buildings/walkway.bam')
            self.walkway18646.setScale(12)
            self.walkway18646.setPos(45183.828125, 42797.11328125, -9.174566268920898)
            self.walkway18646.setCollideMask(BitMask32.bit(7))
            self.walkway18646.setH(90.00000762939453)
            self.walkway18646.flattenStrong()
            self.walkway18646.reparentTo(render)

            self.walkway12383 = self.loader.loadModel('assets/environment/arctic/buildings/walkway.bam')
            self.walkway12383.setScale(12)
            self.walkway12383.setPos(45183.828125, 44237.11328125, -9.174566268920898)
            self.walkway12383.setCollideMask(BitMask32.bit(7))
            self.walkway12383.setH(90.00000762939453)
            self.walkway12383.flattenStrong()
            self.walkway12383.reparentTo(render)

            self.walkway12223 = self.loader.loadModel('assets/environment/arctic/buildings/walkway.bam')
            self.walkway12223.setScale(12)
            self.walkway12223.setPos(45183.828125, 44537.11328125, -9.174566268920898)
            self.walkway12223.setCollideMask(BitMask32.bit(7))
            self.walkway12223.setH(90.00000762939453)
            self.walkway12223.flattenStrong()
            self.walkway12223.reparentTo(render)

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

            self.light7208 = self.loader.loadModel('assets/base/models/light.bam')
            self.light7208.setScale(14)
            self.light7208.setPos(45193.30078125, 43214.30078125, -9.174566268920898)
            self.light7208.setH(0.0)
            # self.light7208.reparentTo(render)
            # render.setLight(self.light7208.getChild(1).getChild(0))

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
