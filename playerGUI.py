#Written by Abdulaziz Albastaki in January 2021
from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectFrame import DirectFrame

class GUI():
    def __init__(self):
        # self.topLeftHUD = OnscreenImage(image='assets/base/GUI/HUD2.png', pos=(-1.5, 0, 0.7),scale=0.2)
        self.npfont = loader.loadFont("assets/base/fonts/OPTINewportLand.ttf")
        self.npfont.setPixelsPerUnit(120)
        #self.frame = DirectFrame(parent=render2d, frameColor=(0, 0, 0.4, 1),
        #                        frameSize=(-0.25, 0.25, -0.15, 0.15),
        #                        pos=(-0.7, 0, 0.8))
        self.jetpackStatus = OnscreenText(text='JETPACK FUEL: 100%', pos=(-0.7, 0.85),font=self.npfont,
                                          fg=(212/255,175/255,55/255,1),
                                          scale=0.06,parent=render2d)


