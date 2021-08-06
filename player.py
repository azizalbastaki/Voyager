#Written by Abdulaziz Albastaki in January 2021
import sys
from panda3d.core import Vec3,Quat,PointLight,CollisionHandlerQueue,CollisionRay, WindowProperties, CollisionTraverser, CollisionHandlerPusher, CollisionSphere, CollisionNode, CollideMask, BitMask32, CollisionSegment
from playerModes import playerModes
from playerGUI import GUI
from tools import buildingTool
class Player():
    def __init__(self,camera,accept,render,loader,maxJPHeight):
        #initial variables and sounds

        self.developer = True # Developer tools (building tools) will be accessible if this is turned on.
        self.gameMode = self.mode0 # the current playerUpdate function that is in use
        # self.playerModeParameters = () # the parameters being fed into the function above.
        self.groundContact = False # if the player is on the ground or a surface, gravity will not pull the player below the surface
        self.jetPack_energy = 100
        self.maximumHeight = maxJPHeight # maximum height in which the jetpack can fly to, this is dependent on the map loaded.
        self.jetPack_AUDIO = loader.loadSfx("assets/base/sounds/jetpack2.wav")
        self.jetPack_AUDIO.setLoop(True)
        self.vertical_velocity = 0 # Current Z velocity, positive = Upwards.
        self.z_velocity = 0 # Current Y velocity
        self.x_velocity = 0
        self.movingZ = False
        self.movingX = False


        #initiate GUI
        self.HUD = GUI()
        self.playerHolder = render.attachNewNode('player')

        # camera control - Hiding mouse and using it to rotate the camera
        props = WindowProperties()
        props.setCursorHidden(True)
        props.setMouseMode(WindowProperties.M_relative)
        base.win.requestProperties(props)

        # PLAYER MODEL SCENE GRAPH
        self.thirdPersonCamera_ZOOM = -50 # initial distance of third person camera.
        self.character = loader.loadModel('assets/base/models/playerModel/player.bam')
        self.toggleFPCam = False # Whether first person camera is on, this is initially off.
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

        # Horizontal collisions
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

        # Vertical collisions - Downwards
        self.groundRay = CollisionRay()
        self.groundRay.setDirection(0, 0, -1)
        self.groundRayCol = CollisionNode('playerRay')
        self.groundRayCol.addSolid(self.groundRay)
        self.groundRayCol.setFromCollideMask(CollideMask.bit(1))
        self.groundRayCol.setIntoCollideMask(CollideMask.allOff())
        self.groundColNp = self.playerHolder.attachNewNode(self.groundRayCol)
        self.groundHandler = CollisionHandlerQueue()
        self.cTrav.addCollider(self.groundColNp, self.groundHandler)

        # Third Person Camera Collision
        self.cameraRay = CollisionSegment()
        self.cameraRayNode = CollisionNode('camerRay')
        self.cameraRayNode.addSolid(self.cameraRay)
        self.cameraRayNodePath = render.attachNewNode(self.cameraRayNode)
        self.cameraCollisionHandler = CollisionHandlerQueue()
        self.cTrav.addCollider(self.cameraRayNodePath, self.cameraCollisionHandler)

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
            self.tool = buildingTool("newbuildings",self.playerHolder,loader,accept) # Load up building tool if developer modee is on.

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

        self.playerMode = playerModes(self.playerBase,self.playerHolder,self.character,self.vertical_velocity,self.z_velocity,self.x_velocity,self.keyMap,self.monitor,self.thirdPersonNode,self.jetPack_energy,self.jetPack_AUDIO,self.thirdPersonCamera_ZOOM, self.toggleFPCam,self.HUD, self.cTrav,self.groundHandler,self.upwardsHandler, self.maximumHeight)


    def playerUpdate(self,task): # our UPDATE TASK
        self.gameMode()
        return task.cont


    def updateKey(self,key,value):
        self.keyMap[key] = value
        if key == "change_camera":
            self.changeCamera()
        self.scrollFactor = 10
        if key == "scrollup": # third person zoom in/out
            self.thirdPersonCamera_ZOOM += self.scrollFactor
        if key == "scrolldown":
            self.thirdPersonCamera_ZOOM -= self.scrollFactor

    def changeCamera(self): # Toggle first person camera.
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
        plnp.setPos(0,1,7)
        render.setLight(plnp)

# PLAYER MODES, HOW THE USER INTERACTS AND CONTROLS WITH THE USER

    #   MODE 0
    # Mode 0 is the default update mode, it allows WASD movement,
    # mouse controlled camera rotations, first person and third
    # person switching, it also has GUI display and player physics.

    def mode0(self):

        #THIRD PERSON CAMERA COLLISION

        # print("thirdpersonnode")
        # print(self.playerBase.getHpr())
        # print("pb")
        # print(self.character.getHpr())

        deltaTime = globalClock.getDt()
        self.movingZ = False
        self.movingX = False
        self.walkConstant = 25
        self.rotateConstant = 750

        # Keyboard controls
        # LEVITATION STUFF (FORMERLY CALLED JETPACK)

        if self.keyMap["space"] and self.jetPack_energy > 0:
            jetpack = 0.00001 * (((self.playerHolder.getZ()) - self.maximumHeight) ** 2) + 9.81
            self.playerHolder.setZ(self.playerBase, jetpack)
            self.jetPack_energy -= 15 * deltaTime
            self.walkConstant = 70
            self.jetPack_AUDIO.play()
        else:
            self.jetPack_AUDIO.stop()
        if self.jetPack_energy < 100:
            self.jetPack_energy += 10 * deltaTime
        if self.jetPack_energy > 100:
            self.jetPack_energy = 100

        self.HUD.jetpackStatus.text = "Levitation Battery: "+ str(int(self.jetPack_energy)) + "%"

        if (self.keyMap["forward"] or self.keyMap["backwards"]) and (self.keyMap["right"] or self.keyMap["left"]):
            self.walkConstant = int(((self.walkConstant ** 2)/2) ** 0.5)

        # WASD MOVEMENT
        if self.keyMap["forward"]:
            self.monitor.setH(self.playerBase.getH() - 90)
            self.movingZ = True
            self.z_velocity += 5
            if self.z_velocity > self.walkConstant:
                self.z_velocity = self.walkConstant

        if self.keyMap["right"]:
            self.monitor.setH(self.playerBase.getH() - 180)
            self.movingX = True
            self.x_velocity += 5
            if self.x_velocity > self.walkConstant:
                self.x_velocity = self.walkConstant
        if self.keyMap["p"]:
            print(self.playerHolder.getPos())
            print(self.thirdPersonCamera_ZOOM)
            self.gameMode = self.mode1
        if self.keyMap["left"]:
            self.monitor.setH(self.playerBase.getH())
            self.movingX = True
            self.x_velocity -= 5
            if self.x_velocity < -self.walkConstant:
                self.x_velocity = -self.walkConstant
        if self.keyMap["backwards"]:
            self.monitor.setH(self.playerBase.getH() + 90)
            self.movingZ = True
            self.z_velocity -= 20
            if self.z_velocity < -self.walkConstant:
                self.z_velocity = -self.walkConstant

        if self.movingZ == False:
            if self.z_velocity <= 7 or (self.z_velocity >= -5 and self.z_velocity < 0): # Shaking bug fix
                self.z_velocity = 0
            if self.z_velocity > 0:
                self.z_velocity -= 10
            elif self.z_velocity < 0:
                self.z_velocity += 10
        if self.movingX == False:
            if self.x_velocity <= 5 or (self.x_velocity >= -5 and self.x_velocity < 0): # Shaking bug fix
                self.x_velocity = 0
            if self.x_velocity > 0:
                self.x_velocity -= 10
            elif self.x_velocity < 0:
                self.x_velocity += 10
        # MONITOR HEADINGS FOR DOUBLE INPUT
        if self.keyMap["forward"] and self.keyMap["right"]:
            self.monitor.setH(self.playerBase.getH() - 135)
        elif self.keyMap["forward"] and self.keyMap["left"]:
            self.monitor.setH(self.playerBase.getH() - 45)
        elif self.keyMap["backwards"] and self.keyMap["left"]:
            self.monitor.setH(self.playerBase.getH() + 45)
        elif self.keyMap["backwards"] and self.keyMap["right"]:
            self.monitor.setH(self.playerBase.getH() + 135)



        # third person camera control
        if (self.toggleFPCam == False):  # third person camera controls
            if (base.mouseWatcherNode.hasMouse() == True):
                mouseposition = base.mouseWatcherNode.getMouse()
                self.thirdPersonNode.setP(mouseposition.getY() * 30)
                self.playerBase.setH(mouseposition.getX() * -50)
                if (mouseposition.getX() < 0.1 and mouseposition.getX() > -0.1):
                    self.playerBase.setH(self.playerBase.getH())

            if self.thirdPersonNode.getP() > 90:
                self.recenterMouse()
                self.thirdPersonNode.setP(90)  # TRACK MOUSE
            elif self.thirdPersonNode.getP() < -90:
                self.recenterMouse()
                self.thirdPersonNode.setP(-90)
            if self.thirdPersonCamera_ZOOM > -20:  # validate zoom
                self.thirdPersonCamera_ZOOM = -20
            elif self.thirdPersonCamera_ZOOM < -390:
                self.thirdPersonCamera_ZOOM = -390
        # CAMERA STUFF
        # FIRST PERSON CAMERA
        if self.toggleFPCam:  # first person camera controls
            camera.setPos(self.character.getPos())  # 0,-50,-10
            camera.setZ(camera.getZ() + 6)
            self.playerHolder.hide()
            if (base.mouseWatcherNode.hasMouse() == True):
                mouseposition = base.mouseWatcherNode.getMouse()
                camera.setP(mouseposition.getY() * 20)
                self.playerBase.setH(mouseposition.getX() * -50)
                if (mouseposition.getX() < 0.1 and mouseposition.getX() > -0.1):
                    self.playerBase.setH(self.playerBase.getH())
            if camera.getP() > 90:
                self.recenterMouse()
                camera.setP(90)  # TRACK MOUSE
            elif camera.getP() < -90:
                self.recenterMouse()
                camera.setP(-90)
        else:  # takes out of first person perspective if toggleFPS is turned off.
            self.playerHolder.show()
            camera.setPos(0, self.thirdPersonCamera_ZOOM, 0)  # 0,-50,-4
            camera.lookAt(self.character)
        # movement updates
        self.playerHolder.setY(self.playerBase, (self.z_velocity * deltaTime))
        self.playerHolder.setX(self.playerBase, (self.x_velocity * deltaTime))

        # forward/backward rolling
        axis = self.playerBase.getQuat().getRight()
        angle = (self.z_velocity * deltaTime * -8)
        quat = Quat()
        quat.setFromAxisAngle(angle, axis)
        newVec = self.character.getQuat() * quat
        # print(newVec.getHpr())
        self.character.setQuat(newVec)

        # sideways rolling
        axis = self.playerBase.getQuat().getForward()
        angle = (self.x_velocity * deltaTime * 8)
        quat = Quat()
        quat.setFromAxisAngle(angle, axis)
        newVec = self.character.getQuat() * quat
        # print(self.playerBase.getPos())
        self.character.setQuat(newVec)
        self.cameraRay.setPointA(self.playerBase.getPos())
        if camera.getPos() != (0,0,0):
            self.cameraRay.setPointB(camera.getPos(base.render))
            
        self.cTrav.traverse(render)

        # checking for camera collisions
        entries = list(self.cameraCollisionHandler.entries)
        for entry in entries:
            if str(entry.getIntoNodePath())[:19] != "render/worldTerrain":
                #camera.setPos(entry.getSurfacePoint(self.thirdPersonNode))
                self.thirdPersonCamera_ZOOM += 1
        

        # if len(entries) > 0:
        #     if (self.playerHolder.getZ() < entries[-1].getSurfacePoint(render).getZ() + 8):
        #         self.playerHolder.setZ(entries[-1].getSurfacePoint(render).getZ() + 8)
        #         self.vertical_velocity = 0

        # checking for collisions - downwards
        entries = list(self.groundHandler.entries)
        entries.sort(key=lambda x: x.getSurfacePoint(render).getZ())
        self.performGravity = True
        if self.performGravity == True:
            self.vertical_velocity -= (deltaTime * 9.81)
            if self.vertical_velocity <= -15:
                self.vertical_velocity = -15
            self.playerHolder.setPos(self.playerHolder, Vec3(0, 0, self.vertical_velocity))  # Gravity
        if len(entries) > 0:
            if (self.playerHolder.getZ() < entries[-1].getSurfacePoint(render).getZ() + 8):
                self.playerHolder.setZ(entries[-1].getSurfacePoint(render).getZ() + 8)
                self.vertical_velocity = 0

        # checking for collisions - upwards
        entries = list(self.upwardsHandler.entries)
        entries.sort(key=lambda x: x.getSurfacePoint(render).getZ())
        if len(entries) > 0:
            for entry in entries:
                if (self.playerHolder.getZ() > entry.getSurfacePoint(render).getZ() - 70):
                    self.playerHolder.setZ(entry.getSurfacePoint(render).getZ() - 130)

    # PLAYER MODES, HOW THE USER INTERACTS AND CONTROLS WITH THE USER
    #   MODE 1
    # Mode 1 is a test update loop used to test player loop switching.
    # it simply freezes the controls.

    def mode1(self):
        self.playerHolder.hide()
        self.playerHolder.setHpr(0,0,0)
        if self.keyMap["backwards"]:
            self.playerHolder.show()
            self.gameMode = self.mode0