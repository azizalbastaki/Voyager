#Written by Abdulaziz Albastaki in January 2021
import sys
from panda3d.core import WindowProperties

class Player():                          # our 'class'
    def __init__(self,camera,accept,base):
        camera.setPos(22824.9, 15280.5, 20)
        props = WindowProperties()
        props.setCursorHidden(True)
        props.setMouseMode(WindowProperties.M_relative)
        base.win.requestProperties(props)
        self.keyMap = {
            "left": False,
            "right": False,
            "forward": False,
            "backwards": False
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

    def updateKey(self,key,value):
        self.keyMap[key] = value

    def playermove(self,task):
        deltaTime = globalClock.getDt()



        if (base.mouseWatcherNode.hasMouse() == True):
            mouseposition = base.mouseWatcherNode.getMouse()
            camera.setP(mouseposition.getY() * 30)
            camera.setH(mouseposition.getX() * -50)
            if (mouseposition.getX() < 0.1 and mouseposition.getX() > -0.1):
                camera.setH(camera.getH())
            else:
                camera.setH(camera.getH() + mouseposition.getX() * -1)

        self.walkConstant = 4000
        if self.keyMap["forward"]:
            camera.setY(camera, (self.walkConstant*deltaTime))

        if self.keyMap["right"]:
            camera.setX(camera, (self.walkConstant*deltaTime))
        if self.keyMap["left"]:
            camera.setX(camera, (-self.walkConstant*deltaTime))
        if self.keyMap["backwards"]:
            camera.setY(camera, (-self.walkConstant * deltaTime))
        return task.cont