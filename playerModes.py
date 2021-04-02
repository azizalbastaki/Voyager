# Written by Abdulaziz Albastaki in March 2021
from panda3d.core import Quat, Vec3
class playerModes():
    def __init__(self, playerBase, playerHolder, character, verticalv,zvelocity,xvelocity,keymap, monitor, thirdpersonnode, jetpackE, jetpackA,thirdpersonzoom, toggleFpCam,HUD, cTrav, groundHandler, upwardsHandler, maximumheight):
        self.gameMode = 0
        self.playerBase = playerBase
        self.playerHolder = playerHolder
        self.character = character
        self.vertical_velocity = verticalv
        self.toggleFPCam = toggleFpCam
        self.z_velocity = zvelocity
        self.x_velocity = xvelocity
        self.keyMap = keymap
        self.monitor = monitor
        self.thirdPersonNode = thirdpersonnode
        self.jetPack_energy = jetpackE
        self.jetPack_AUDIO = jetpackA
        self.thirdPersonCamera_ZOOM = thirdpersonzoom
        self.HUD = HUD
        self.cTrav = cTrav
        self.groundHandler = groundHandler
        self.upwardsHandler = upwardsHandler
        self.maximumHeight = maximumheight
    def fixedScene(self, playerPosition, playerPose,cameraPosition, cameraAngle):
        self.playerBase.setPos(playerPosition)
        self.playerBase.setHpr(playerPose)
        camera.setPos(cameraPosition)
        camera.setHpr(cameraAngle)

    def freeze(self):
        pass

#deltaTime = globalClock.getDt()
        self.movingZ = False
        self.movingX = False
        # mouse controls
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

        self.walkConstant = 40
        self.rotateConstant = 500

        def rotateMonitor():
            self.monitor.setH(self.playerBase.getH() - 90)

        # Keyboard controls
        if self.keyMap["forward"]:
            self.monitor.setH(self.playerBase.getH() - 90)
            self.movingZ = True
            self.z_velocity += 20
            if self.z_velocity > self.walkConstant:
                self.z_velocity = self.walkConstant

        if self.keyMap["right"]:
            self.monitor.setH(self.playerBase.getH() - 180)
            self.movingX = True
            self.x_velocity += 20
            if self.x_velocity > self.walkConstant:
                self.x_velocity = self.walkConstant
        if self.keyMap["p"]:
            print(self.playerHolder.getPos())
            print(self.thirdPersonCamera_ZOOM)
        if self.keyMap["left"]:
            self.monitor.setH(self.playerBase.getH())
            self.movingX = True
            self.x_velocity -= 20
            if self.x_velocity < -self.walkConstant:
                self.x_velocity = -self.walkConstant
        if self.keyMap["backwards"]:
            self.monitor.setH(self.playerBase.getH() + 90)
            self.movingZ = True
            self.z_velocity -= 20
            if self.z_velocity < -self.walkConstant:
                self.z_velocity = -self.walkConstant

        if self.movingZ == False:
            if self.z_velocity > 0:
                self.z_velocity -= 10
            elif self.z_velocity < 0:
                self.z_velocity += 10
        if self.movingX == False:
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

        if self.keyMap["space"] and self.jetPack_energy > 0:
            jetpack = 0.00001 * (((self.playerHolder.getZ()) - self.maximumHeight) ** 2) + 9.81
            self.playerHolder.setZ(self.playerBase, jetpack)
            self.jetPack_energy -= 8 * deltaTime
            if self.jetPack_AUDIO.status() != self.jetPack_AUDIO.PLAYING:
                self.jetPack_AUDIO.play()
        else:
            if self.jetPack_energy < 100:
                self.jetPack_energy += 10 * deltaTime
            if self.jetPack_energy > 100:
                self.jetPack_energy = 100
            self.jetPack_AUDIO.stop()
        self.HUD.jetpackStatus.text = str(int(self.jetPack_energy)) + "%"
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
        # print(newVec.getHpr())
        self.character.setQuat(newVec)

        # checking for collisions - downwards
        self.cTrav.traverse(render)
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
