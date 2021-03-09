#Written by Abdulaziz Albastaki in January 2021
import sys
from panda3d.core import Vec3,DirectionalLight,PointLight,CollisionHandlerQueue,CollisionRay, WindowProperties, CollisionTraverser, CollisionHandlerPusher, CollisionSphere, CollisionNode, CollideMask, BitMask32
import math
from playerGUI import GUI
from tools import buildingTool
class Player():
    def __init__(self,camera,accept,render,loader,maxJPHeight):
        #initial variables and sounds
        self.developer = True
        self.groundContact = False
        self.jetPack_energy = 100
        self.maximumHeight = maxJPHeight
        self.jetPack_AUDIO = loader.loadSfx("assets/base/sounds/jetpack2.wav")
        self.jetPack_AUDIO.setLoop(True)
        self.velocity = 0
        #initiate GUI
        self.HUD = GUI()
        self.playerHolder = render.attachNewNode('player')
        #camera control
        props = WindowProperties()
        props.setCursorHidden(True)
        props.setMouseMode(WindowProperties.M_relative)
        base.win.requestProperties(props)
        self.thirdPersonCamera_ZOOM = -50
        self.character = loader.loadModel('assets/base/models/playerModel/player.bam')
        self.toggleFPCam = False
        self.character.setPos(0,0,0)
        self.character.reparentTo(self.playerHolder)
        self.playerBase = self.playerHolder.attachNewNode('camParent')
        self.thirdPersonNode = self.playerBase.attachNewNode('thirdPersonCam')
        camera.reparentTo(self.thirdPersonNode)
        self.mouseSeconds = []
        self.playerHolder.setScale(4)
        self.monitor = loader.loadModel('assets/base/models/faces/playerMonitor.bam')
        self.monitor.reparentTo(self.playerHolder)
        self.cTrav = CollisionTraverser()
        #Horizontal collisions
        self.pusher = CollisionHandlerPusher()
        self.pusher.horizontal = True
        self.colliderNode = CollisionNode("player")
        self.colliderNode.addSolid(CollisionSphere(0, 0, 0, 2))
        self.colliderNode.setFromCollideMask(CollideMask.bit(1))
        self.colliderNode.setFromCollideMask(CollideMask.bit(0))
        self.colliderNode.setIntoCollideMask(BitMask32.allOff())
        collider = self.playerHolder.attachNewNode(self.colliderNode)
        collider.show()
        self.pusher.addCollider(collider, self.playerHolder)
        self.cTrav.addCollider(collider,self.pusher)

        #Vertical collisions - Downwards
        self.groundRay = CollisionRay()
        self.groundRay.setDirection(0, 0, -1)
        self.groundRayCol = CollisionNode('playerRay')
        self.groundRayCol.addSolid(self.groundRay)
        self.groundRayCol.setFromCollideMask(CollideMask.bit(1))
        self.groundRayCol.setIntoCollideMask(CollideMask.allOff())
        self.groundColNp = self.playerHolder.attachNewNode(self.groundRayCol)
        self.groundHandler = CollisionHandlerQueue()
        self.cTrav.addCollider(self.groundColNp, self.groundHandler)

        # Vertical collisions - Upwards
        self.upwardsRay = CollisionRay()
        self.upwardsRay.setDirection(0, 0, 1)
        self.upwardsRayCol = CollisionNode('playerupRay')
        self.upwardsRayCol.addSolid(self.upwardsRay)
        self.upwardsRayCol.setFromCollideMask(CollideMask.bit(1))
        self.upwardsRayCol.setIntoCollideMask(CollideMask.allOff())
        self.upwardsColNp = self.playerHolder.attachNewNode(self.upwardsRayCol)
        self.upwardsHandler = CollisionHandlerQueue()
        self.cTrav.addCollider(self.upwardsColNp, self.upwardsHandler)
        #self.cTrav.showCollisions(render)


        if self.developer == True:
            self.tool = buildingTool("newbuildings",self.playerHolder,loader,accept)

        #self.setupLighting() # light
        #initial position
        self.playerHolder.setPos(45178.3, 43109.3, 0)
        self.keyMap = {
            "left": False,
            "right": False,
            "forward": False,
            "backwards": False,
            "change_camera": False,
            "leftClick": False,
            "space": False,
            "p":False,
            "scrollup": False,
            "scrolldown": False
        }

        accept("escape", sys.exit)
        accept("w", self.updateKey, ["forward", True])  #
        accept("w-up", self.updateKey, ["forward", False])

        accept("a", self.updateKey, ["left", True])
        accept("a-up", self.updateKey, ["left", False])

        accept("s", self.updateKey, ["backwards", True])
        accept("s-up", self.updateKey, ["backwards", False])

        accept("d", self.updateKey, ["right", True])
        accept("d-up", self.updateKey, ["right", False])

        accept("c",self.updateKey,["change_camera", True])

        accept("wheel_up",self.updateKey,["scrollup",True])

        accept("wheel_down",self.updateKey,["scrolldown",True])

        accept("p", self.updateKey, ["p", True])
        accept("p-up", self.updateKey, ["p", False])

        accept("space",self.updateKey,["space",True])
        accept("space-up",self.updateKey,["space",False])

    def updateKey(self,key,value):
        self.keyMap[key] = value
        if key == "change_camera":
            self.changeCamera()
        self.scrollFactor = 10
        if key == "scrollup": # third person zoom in/out
            self.thirdPersonCamera_ZOOM += self.scrollFactor
        if key == "scrolldown":
            self.thirdPersonCamera_ZOOM -= self.scrollFactor

    def changeCamera(self):
        if self.toggleFPCam == False:
            self.toggleFPCam = True
        else:
            self.toggleFPCam = False

    def recenterMouse(self):
        base.win.movePointer(0, int(base.win.getProperties().getXSize() / 2), int(base.win.getProperties().getYSize() / 2))
    def setupLighting(self):
        plight = PointLight('plight')
        plight.setColor((1, 1, 1, 1))
        plnp = self.playerHolder.attachNewNode(plight)
        render.setLight(plnp)
    def playerUpdate(self,task): #our UPDATE TASK
        deltaTime = globalClock.getDt()
        #mouse controls
        if self.toggleFPCam: #first person camera controls
            camera.setPos(self.character.getPos())  # 0,-50,-10
            camera.setZ(camera.getZ()+6)
            self.playerHolder.hide()

            if (base.mouseWatcherNode.hasMouse() == True):
                mouseposition = base.mouseWatcherNode.getMouse()
                camera.setP(mouseposition.getY()*20)
                self.playerBase.setH(mouseposition.getX() * -50)
                if (mouseposition.getX() < 0.1 and mouseposition.getX() > -0.1):
                    self.playerBase.setH(self.playerBase.getH())
            if camera.getP() > 90:
                self.recenterMouse()
                camera.setP(90) #TRACK MOUSE
            elif camera.getP() < -90:
                self.recenterMouse()
                camera.setP(-90)
        else: # takes out of first person perspective if toggleFPS is turned off.
            self.playerHolder.show()
            camera.setPos(0, self.thirdPersonCamera_ZOOM, 0)  # 0,-50,-4
            camera.lookAt(self.character)

        self.walkConstant = 40
        self.rotateConstant = 500
        def rotateMonitor():
            self.monitor.setH(self.playerBase.getH()-90)
        # Keyboard controls
        if self.keyMap["forward"]:
            self.monitor.setH(self.playerBase.getH()-90)
            self.playerHolder.setY(self.playerBase, (self.walkConstant*deltaTime))
            self.character.setP(self.character.getP() + (-self.rotateConstant*deltaTime*(math.cos(math.radians(self.playerBase.getH())))))
            self.character.setR(self.character.getR() - (self.rotateConstant*deltaTime*(-math.sin(math.radians(self.playerBase.getH())))))
        if self.keyMap["right"]:
            self.monitor.setH(self.playerBase.getH()-180)
            self.playerHolder.setX(self.playerBase, (self.walkConstant*deltaTime))
        if self.keyMap["p"]:
            print(self.playerHolder.getPos())
            print(self.thirdPersonCamera_ZOOM)
        if self.keyMap["left"]:
            self.monitor.setH(self.playerBase.getH())
            self.playerHolder.setX(self.playerBase, (-self.walkConstant*deltaTime))
        if self.keyMap["backwards"]:
            self.monitor.setH(self.playerBase.getH()+90)
            self.playerHolder.setY(self.playerBase, (-self.walkConstant * deltaTime))
            self.character.setP(self.character,(self.rotateConstant*deltaTime))
        # MONITOR HEADINGS FOR DOUBLE INPUT
        if self.keyMap["forward"] and self.keyMap["right"]:
            self.monitor.setH(self.playerBase.getH()-135)
        elif self.keyMap["forward"] and self.keyMap["left"]:
            self.monitor.setH(self.playerBase.getH()-45)
        elif self.keyMap["backwards"] and self.keyMap["left"]:
            self.monitor.setH(self.playerBase.getH()+45)
        elif self.keyMap["backwards"] and self.keyMap["right"]:
            self.monitor.setH(self.playerBase.getH()+135)

        if self.keyMap["space"] and self.jetPack_energy>0:
            jetpack = 0.00001*(((self.playerHolder.getZ())-self.maximumHeight)**2)+9.81
            self.playerHolder.setZ(self.playerBase, jetpack)
            self.jetPack_energy -= 8*deltaTime
            if self.jetPack_AUDIO.status() != self.jetPack_AUDIO.PLAYING:
                self.jetPack_AUDIO.play()
        else:
            if self.jetPack_energy < 100:
                self.jetPack_energy += 10*deltaTime
            if self.jetPack_energy > 100:
                self.jetPack_energy = 100
            self.jetPack_AUDIO.stop()
        self.HUD.jetpackStatus.text = str(int(self.jetPack_energy))+"%"
        # third person camera control
        if (self.toggleFPCam == False): # third person camera controls
            if (base.mouseWatcherNode.hasMouse() == True):
                mouseposition = base.mouseWatcherNode.getMouse()
                self.thirdPersonNode.setP(mouseposition.getY() * 30)
                self.playerBase.setH(mouseposition.getX() * -50)
                if (mouseposition.getX() < 0.1 and mouseposition.getX() > -0.1):
                    self.playerBase.setH(self.playerBase.getH())
            if self.thirdPersonNode.getP() > 90:
                self.recenterMouse()
                self.thirdPersonNode.setP(90) # TRACK MOUSE
            elif self.thirdPersonNode.getP() < -90:
                self.recenterMouse()
                self.thirdPersonNode.setP(-90)
            if self.thirdPersonCamera_ZOOM > -20: # validate zoom
                self.thirdPersonCamera_ZOOM = -20
            elif self.thirdPersonCamera_ZOOM < -390:
                self.thirdPersonCamera_ZOOM = -390

        self.cTrav.traverse(render)

        # checking for collisions - downwards
        entries = list(self.groundHandler.entries)
        entries.sort(key=lambda x: x.getSurfacePoint(render).getZ())
        self.performGravity = True
        if self.performGravity == True:
            self.velocity -= (deltaTime*9.81)
            if self.velocity <= -15:
                self.velocity = -15
            self.playerHolder.setPos(self.playerHolder, Vec3(0, 0, self.velocity))  # Gravity
        if len(entries) > 0:
            if (self.playerHolder.getZ()<entries[-1].getSurfacePoint(render).getZ()+8):
                self.playerHolder.setZ(entries[-1].getSurfacePoint(render).getZ()+8)
                self.velocity = 0
        # checking for collisions - upwards
        entries = list(self.upwardsHandler.entries)
        entries.sort(key=lambda x: x.getSurfacePoint(render).getZ())
        if len(entries) > 0:
            for entry in entries:
                if (self.playerHolder.getZ() > entry.getSurfacePoint(render).getZ() - 70):
                    self.playerHolder.setZ(entry.getSurfacePoint(render).getZ() - 130)

        return task.cont