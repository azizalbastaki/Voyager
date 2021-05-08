#Written by Abdulaziz Albastaki in January 2021
from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectFrame import DirectFrame

class GUI():
    def __init__(self):
        #self.topLeftHUD = OnscreenImage(image='assets/base/GUI/HUD2.png', pos=(-0.7, 0, 0.7))
        self.frame = DirectFrame(parent=render2d, frameColor=(0.1, 0.1, 0.1, 0.7),
                                 frameSize=(-0.25, 0.25, -0.15, 0.15),
                                 pos=(-0.7, 0, 0.8))
        #self.topLeftHUD.setTransparency(True)
        self.jetpackStatus = OnscreenText(text='JETPACK FUEL: 100%', pos=(-0.75, 0.85), scale=0.04,parent=render2d,fg=(1,1,1,1))


