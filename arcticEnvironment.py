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
            self.walkway19550 = self.loader.loadModel('assets/environment/arctic/buildings/walkway.bam')
            self.walkway19550.setScale(12)
            self.walkway19550.setPos(45208.30078125, 43239.30078125, -9.174566268920898)
            self.walkway19550.setCollideMask(BitMask32.bit(4))
            self.walkway19550.setH(90.0)
            self.walkway19550.reparentTo(render)

            self.walkway1122 = self.loader.loadModel('assets/environment/arctic/buildings/walkway.bam')
            self.walkway1122.setScale(12)
            self.walkway1122.setPos(45208.30078125, 43599.30078125, -9.174566268920898)
            self.walkway1122.setCollideMask(BitMask32.bit(4))
            self.walkway1122.setH(90.0)
            self.walkway1122.reparentTo(render)

            self.walkway12859 = self.loader.loadModel('assets/environment/arctic/buildings/walkway.bam')
            self.walkway12859.setScale(12)
            self.walkway12859.setPos(45208.30078125, 43959.30078125, -9.174566268920898)
            self.walkway12859.setCollideMask(BitMask32.bit(4))
            self.walkway12859.setH(90.0)
            self.walkway12859.reparentTo(render)

            self.walkway11356 = self.loader.loadModel('assets/environment/arctic/buildings/walkway.bam')
            self.walkway11356.setScale(12)
            self.walkway11356.setPos(45208.30078125, 44259.30078125, -9.174566268920898)
            self.walkway11356.setCollideMask(BitMask32.bit(4))
            self.walkway11356.setH(90.0)
            self.walkway11356.reparentTo(render)

            self.walkway12535 = self.loader.loadModel('assets/environment/arctic/buildings/walkway.bam')
            self.walkway12535.setScale(12)
            self.walkway12535.setPos(45208.30078125, 44619.30078125, -9.174566268920898)
            self.walkway12535.setCollideMask(BitMask32.bit(4))
            self.walkway12535.setH(90.0)
            self.walkway12535.reparentTo(render)

            self.walkway14996 = self.loader.loadModel('assets/environment/arctic/buildings/walkway.bam')
            self.walkway14996.setScale(12)
            self.walkway14996.setPos(45208.30078125, 44979.30078125, -9.174566268920898)
            self.walkway14996.setCollideMask(BitMask32.bit(4))
            self.walkway14996.setH(90.0)
            self.walkway14996.reparentTo(render)

            self.walkway13196 = self.loader.loadModel('assets/environment/arctic/buildings/walkway.bam')
            self.walkway13196.setScale(12)
            self.walkway13196.setPos(45208.30078125, 45159.30078125, -9.174566268920898)
            self.walkway13196.setCollideMask(BitMask32.bit(4))
            self.walkway13196.setH(90.0)
            self.walkway13196.reparentTo(render)

            self.walkway16789 = self.loader.loadModel('assets/environment/arctic/buildings/walkway.bam')
            self.walkway16789.setScale(12)
            self.walkway16789.setPos(45208.30078125, 45399.30078125, -9.174566268920898)
            self.walkway16789.setCollideMask(BitMask32.bit(4))
            self.walkway16789.setH(90.0)
            self.walkway16789.reparentTo(render)

            self.walkway16750 = self.loader.loadModel('assets/environment/arctic/buildings/walkway.bam')
            self.walkway16750.setScale(5)
            self.walkway16750.setPos(45408.30078125, 44139.30078125, -9.174566268920898)
            self.walkway16750.setCollideMask(BitMask32.bit(4))
            self.walkway16750.setH(180.0)
            self.walkway16750.reparentTo(render)

            self.walkway1311 = self.loader.loadModel('assets/environment/arctic/buildings/walkway.bam')
            self.walkway1311.setScale(5)
            self.walkway1311.setPos(45408.30078125, 43489.30078125, -9.174566268920898)
            self.walkway1311.setCollideMask(BitMask32.bit(4))
            self.walkway1311.setH(180.0)
            self.walkway1311.reparentTo(render)

            self.building1539 = self.loader.loadModel('assets/environment/arctic/buildings/building1.bam')
            self.building1539.setScale(3)
            self.building1539.setPos(45588.30078125, 43504.30078125, -9.174566268920898)
            self.building1539.setCollideMask(BitMask32.bit(4))
            self.building1539.setH(-89.99999237060547)
            self.building1539.reparentTo(render)

            self.building1_collision5640 = self.loader.loadModel(
                'assets/environment/arctic/buildings/building1collision.bam')
            self.building1_collision5640.setScale(3)
            self.building1_collision5640.setPos(45588.30078125, 43504.30078125, -9.174566268920898)
            self.building1_collision5640.setCollideMask(BitMask32.bit(0))
            self.building1_collision5640.setH(-89.99999237060547)
            self.building1_collision5640.hide()
            self.building1_collision5640.reparentTo(render)

            self.building1_collision7003 = self.loader.loadModel(
                'assets/environment/arctic/buildings/building1collision.bam')
            self.building1_collision7003.setScale(3)
            self.building1_collision7003.setPos(45588.30078125, 44164.30078125, -9.174566268920898)
            self.building1_collision7003.setCollideMask(BitMask32.bit(0))
            self.building1_collision7003.setH(-89.99999237060547)
            self.building1_collision7003.hide()
            self.building1_collision7003.reparentTo(render)

            self.building19085 = self.loader.loadModel('assets/environment/arctic/buildings/building1.bam')
            self.building19085.setScale(3)
            self.building19085.setPos(45588.30078125, 44164.30078125, -9.174566268920898)
            self.building19085.setCollideMask(BitMask32.bit(4))
            self.building19085.setH(-89.99999237060547)
            self.building19085.reparentTo(render)

            self.tree11919 = self.loader.loadModel('assets/environment/arctic/nature/tree.bam')
            self.tree11919.setScale(12)
            self.tree11919.setPos(45588.30078125, 43899.30078125, -9.174566268920898)
            self.tree11919.setH(-89.99999237060547)
            self.tree11919.reparentTo(render)

            self.tree13882 = self.loader.loadModel('assets/environment/arctic/nature/tree.bam')
            self.tree13882.setScale(12)
            self.tree13882.setPos(45588.30078125, 43779.30078125, -9.174566268920898)
            self.tree13882.setH(-89.99999237060547)
            self.tree13882.reparentTo(render)

            self.tree15447 = self.loader.loadModel('assets/environment/arctic/nature/tree.bam')
            self.tree15447.setScale(12)
            self.tree15447.setPos(45828.30078125, 43839.30078125, -9.174566268920898)
            self.tree15447.setH(-89.99999237060547)
            self.tree15447.reparentTo(render)

            self.tree15349 = self.loader.loadModel('assets/environment/arctic/nature/tree.bam')
            self.tree15349.setScale(12)
            self.tree15349.setPos(45828.30078125, 43959.30078125, -9.174566268920898)
            self.tree15349.setH(-89.99999237060547)
            self.tree15349.reparentTo(render)

            self.tree14798 = self.loader.loadModel('assets/environment/arctic/nature/tree.bam')
            self.tree14798.setScale(12)
            self.tree14798.setPos(45828.30078125, 43719.30078125, -9.174566268920898)
            self.tree14798.setH(-89.99999237060547)
            self.tree14798.reparentTo(render)

            self.tree11773 = self.loader.loadModel('assets/environment/arctic/nature/tree.bam')
            self.tree11773.setScale(12)
            self.tree11773.setPos(45768.30078125, 43539.30078125, -9.174566268920898)
            self.tree11773.setH(-89.99999237060547)
            self.tree11773.reparentTo(render)

            self.tree13219 = self.loader.loadModel('assets/environment/arctic/nature/tree.bam')
            self.tree13219.setScale(12)
            self.tree13219.setPos(45768.30078125, 43299.30078125, -9.174566268920898)
            self.tree13219.setH(-89.99999237060547)
            self.tree13219.reparentTo(render)

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
