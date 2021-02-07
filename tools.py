#Written by Abdulaziz Albastaki in February 2021
class buildingTool():
    def __init__(self,models,player,loader):
        self.player = player
        self.loader = loader
        self.models = open(models,"r") #Open file with all the gameobjects
        self.gameObjects = []
        for i in self.models:
            self.gameObjects.append(i)
        self.models.close()
        self.index = 0
        self.currentGameObject = self.loader.loadModel(self.gameObjects[0])
        self.currentGameObject.reparentTo(render)
        self.currentSizeFactor = 1
        self.toggle = False

        self.keymap = {
            "b": False,
            "up": False,
            "down": False,
            "right": False,
            "left": False,
            "R": False,
            "sizeup": False,
            "sizedown": False,
            "p": False
        }

        self.updateTask = taskMgr.add(self.update, "update")
    def update(self):
        deltatime = globalClock.getDt()
        if self.keymap["b"] and self.toggle == False:
            self.toggleOn()
        elif self.keymap["b"] and self.toggle == True:
            self.toggleOff()

        if self.toggle == True:
            def setHeight():
                pass
            self.moveFactor = 50
            if self.keymap["up"]:
                self.currentGameObject.setX(self.currentGameObject,self.moveFactor*deltatime)
            if self.keymap["down"]:
                self.currentGameObject.setX(self.currentGameObject,-self.moveFactor*deltatime)
            if self.keymap["left"]:
                self.currentGameObject.setY(self.currentGameObject,-self.moveFactor*deltatime)
            if self.keymap["right"]:
                self.currentGameObject.setY(self.currentGameObject,self.moveFactor*deltatime)
            if self.keymap["sizeup"]:
                self.currentSizeFactor+=1
                self.currentGameObject.setScale(self.currentSizeFactor)
            if self.keymap["sizedown"]:
                self.currentSizeFactor-=1
                self.currentGameObject.setScale(self.currentSizeFactor)
            if self.keymap["R"]:
                self.currentGameObject.setH(self.currentGameObject, 45)
            if self.keymap["p"]:
                self.placeObject()

    def setupGUI(self):
        pass
    def placeObject(self):
        self.model = self.loader.loadModel(self.gameObjects[self.index])
        self.model.setPos(self.currentGameObject.getPos())
        self.model.setScale(self.currentSizeFactor)
        self.model.setH(self.currentGameObject.setH())
        self.model.reparentTo(render)
    def toggleOn(self):
        self.currentGameObject.setPos(self.player.getPos())
        self.currentGameObject.setX(self.player,10)
        self.currentGameObject.show()
        self.toggle = True
    def toggleOff(self):
        self.currentGameObject.hide()
        self.toggle = False
