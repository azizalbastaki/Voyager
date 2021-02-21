#Written by Abdulaziz Albastaki in February 2021
from panda3d.core import CollisionRay,CollisionTraverser,CollisionNode,CollideMask,CollisionHandlerQueue
from direct.gui.DirectGui import DirectFrame
from direct.gui.DirectGui import OnscreenText
class buildingTool():
    def __init__(self,models,player,loader,accept):
        self.player = player
        self.loader = loader
        self.models = open(models,"r") #Open file with all the gameobjects
        self.gameObjects = []
        self.setupGUI()
        self.frame.hide()
        for i in self.models:
            self.gameObjects.append(i)
        self.models.close()
        self.index = 0
        self.currentGameObject = self.loader.loadModel(self.gameObjects[0])
        self.currentGameObject.reparentTo(render)
        self.currentSizeFactor = 1
        self.toggle = False
        self.placedObjects = []
        self.pressedKey = False

        #Collisions
        self.cTrav = CollisionTraverser()
        self.groundRay = CollisionRay()
        self.groundRay.setDirection(0, 0, -1)
        self.groundRayCol = CollisionNode('playerRay')
        self.groundRayCol.addSolid(self.groundRay)
        self.groundRayCol.setFromCollideMask(CollideMask.bit(1))
        self.groundRayCol.setIntoCollideMask(CollideMask.allOff())
        self.groundColNp = self.currentGameObject.attachNewNode(self.groundRayCol)
        self.groundHandler = CollisionHandlerQueue()
        self.cTrav.addCollider(self.groundColNp, self.groundHandler)

        self.keymap = {
            "b": False,
            "up": False,
            "down": False,
            "right": False,
            "left": False,
            "R": False,
            "sizeup": False,
            "sizedown": False,
            "P": False
        }
        accept("b", self.updateKey, ["b", True])  #
        accept("b-up", self.updateKey, ["b", False])

        accept("arrow_left", self.updateKey, ["left", True])
        accept("arrow_left-up", self.updateKey, ["left", False])

        accept("arrow_right", self.updateKey, ["right", True])
        accept("arrow_right-up", self.updateKey, ["right", False])

        accept("arrow_up", self.updateKey, ["up", True])
        accept("arrow_up-up", self.updateKey, ["up", False])

        accept("arrow_down", self.updateKey, ["down", True])
        accept("arrow_down-up", self.updateKey, ["down", False])

        accept("r", self.updateKey, ["R", True])
        accept("r-up", self.updateKey, ["R", False])

        accept("]", self.updateKey, ["sizeup", True])
        accept("]-up", self.updateKey, ["sizeup", False])

        accept("[", self.updateKey, ["sizedown", True])
        accept("[-up", self.updateKey, ["sizedown", False])

        accept("enter", self.updateKey, ["P", True])
        accept("enter-up", self.updateKey, ["P", False])

        self.updateTask = taskMgr.add(self.update, "update")

    def updateKey(self, key, value):
        self.keymap[key] = value

        if (value==False)and(key=="P" or "b" or "R" or "sizeup" or "sizedown"):
            self.pressedKey = False

    def update(self,task):
        deltatime = globalClock.getDt()
        if (self.keymap["b"] and self.toggle == False) and self.pressedKey == False:
            self.toggleOn()
        elif (self.keymap["b"] and self.toggle == True) and self.pressedKey == False:
            self.toggleOff()
        if self.toggle == True:
            def updatePosition():
                self.positionText.text = "Position: " + str(self.currentGameObject.getPos())
            def updateSize():
                self.scaleText.text = "Scale: " + str(self.currentSizeFactor)
            self.moveFactor = 5
            if self.keymap["up"]:
                self.setHeight()
                self.currentGameObject.setX(self.currentGameObject,self.moveFactor)
                updatePosition()
            if self.keymap["down"]:
                self.setHeight()
                self.currentGameObject.setX(self.currentGameObject,-self.moveFactor)
                updatePosition()
            if self.keymap["left"]:
                self.setHeight()
                self.currentGameObject.setY(self.currentGameObject,-self.moveFactor)
                updatePosition()
            if self.keymap["right"]:
                self.setHeight()
                self.currentGameObject.setY(self.currentGameObject,self.moveFactor)
                updatePosition()
            if self.keymap["sizeup"] and self.pressedKey == False:
                self.currentSizeFactor+=1
                updateSize()
                self.currentGameObject.setScale(self.currentSizeFactor)
            if self.keymap["sizedown"] and self.pressedKey == False:
                self.currentSizeFactor-=1
                updateSize()
                self.currentGameObject.setScale(self.currentSizeFactor)
            if self.keymap["R"] and self.pressedKey==False:
                self.currentGameObject.setH(self.currentGameObject, 90)
                self.pressedKey = True
                self.setHeight()
            if self.keymap["P"] and self.pressedKey == False:
                self.placeObject(self.loader,self.gameObjects,self.index,self.currentGameObject,self.currentSizeFactor)
                self.pressedKey = True
        return task.cont

    def setupGUI(self):
        self.frame = DirectFrame(parent=render2d ,frameColor=(0, 0,0, 1),
                              frameSize=(-0.2, 0.4, -0.4, 0.2),
                              pos=(-1, -1, 0))
        self.devMode = OnscreenText(parent= self.frame, text='DEVELOPER MODE', pos=(0.2, 0.1), scale=0.04, fg=(1,1,1,1))
        self.scaleText = OnscreenText(parent= self.frame, text='Scale: 1', pos=(0.2, 0), scale=0.04, fg=(1,1,1,1))
        self.positionText = OnscreenText(parent= self.frame, text='Position: 0,0,0', pos=(0.2, -0.1), scale=0.04, fg=(1,1,1,1))
        self.loadedtext = OnscreenText(parent= self.frame, text='Loaded Model:', pos=(0.2, -0.2), scale=0.04, fg=(1,1,1,1))
        self.loadedModel =  OnscreenText(parent= self.frame, text='assets/environment/arctic/buildings/Townhouse1/Townhouse1.egg', pos=(0.5, -0.3), scale=0.03, fg=(1,1,1,1))

    class placeObject():
        def __init__(self,loader,gameObjects,index,currentGameObject,currentSizeFactor):
            model = loader.loadModel(gameObjects[index])
            model.setPos(currentGameObject.getPos())
            model.setScale(currentSizeFactor)
            model.setH(currentGameObject.getH())
            model.reparentTo(render)
    def toggleOn(self):
        self.currentGameObject.setPos(self.player.getPos())
        self.currentGameObject.setX(self.player,10)
        self.currentGameObject.show()
        self.frame.show()
        self.toggle = True
    def toggleOff(self):
        self.currentGameObject.hide()
        self.frame.hide()
        self.toggle = False

    def setHeight(self):
        self.cTrav.traverse(render)
        entries = list(self.groundHandler.entries)
        entries.sort(key=lambda x: x.getSurfacePoint(render).getZ())
        for entry in entries:
            self.currentGameObject.setZ(entry.getSurfacePoint(render).getZ() + 1)