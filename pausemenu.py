# Written by Abdulaziz Albastaki in June 2022
from direct.gui.OnscreenText import OnscreenText
from panda3d.core import TextNode


class pauseMenu():
    def __init__(self):
        # self.topLeftHUD = OnscreenImage(image='assets/base/GUI/HUD2.png', pos=(-1.5, 0, 0.7),scale=0.2)
        self.npfont = loader.loadFont("assets/base/fonts/OPTINewportLand.ttf")
        self.npfont.setPixelsPerUnit(120)
        self.jetpackStatus = OnscreenText(text='Pause Menu', pos=(-0, 0.7),font=self.npfont,
                                          fg=(212/255,175/255,55/255,1),
                                          scale=0.06,parent=render2d, shadow=(0.05,0.05,0.05,1)
                                          ,shadowOffset=(0.05,0.05), align = TextNode.ALeft)

        # self.jetpackStatus.setShadow(0.05)
        # self.jetpackStatus.setShadowColor(0,0,0,1)



