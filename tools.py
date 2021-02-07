#Written by Abdulaziz Albastaki in February 2021

class buildingTool():
    def __init__(self,location,models,player):
        self.player = player
        self.models = open(models,"r") #Open file with all the gameobjects
        self.gameObjects = []
        for i in self.models:
            self.gameObjects.append(i)
        self.models.close()
        self.index = 0
        self.currentGameObject = self.gameObjects[0].loader.loadModel()
        self.currentGameObject.setPos(location)
        self.currentSizeFactor = 1
        self.toggle = False
        self.keymap = {
            "b": False,
            "up": False,
            "down": False,
            "right": False,
            "left": False
        }
        self.updateTask = taskMgr.add(self.update, "update")
    def update(self):
        pass
    def setupGUI(self):
        pass
    def placeObject(self):
        pass
    def toggleOn(self):
        self.currentGameObject.reparentTo(render)
        self.currentGameObject.setX(self.player,10)
        self.toggle = True
