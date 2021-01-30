#Written by Abdulaziz Albastaki in January 2021
from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.OnscreenText import OnscreenText

class GUI():
    def __init__(self):
        self.topLeftHUD = OnscreenImage(image='assets/base/GUI/HUD1.png', pos=(-0.7, 0, 0.7),parent=render2d)
        self.topLeftHUD.setTransparency(True)
        self.topLeftHUD.setScale(0.30)
        self.jetpackStatus = OnscreenText(text='100%', pos=(-0.62, 0.93), scale=0.05,parent=render2d,fg=(1,1,1,1))


