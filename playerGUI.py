#Written by Abdulaziz Albastaki in January 2021
from direct.gui.OnscreenText import OnscreenText
from panda3d.core import TextNode
class GUI():
    def __init__(self):
        # self.topLeftHUD = OnscreenImage(image='assets/base/GUI/HUD2.png', pos=(-1.5, 0, 0.7),scale=0.2)
        self.npfont = loader.loadFont("assets/base/fonts/OPTINewportLand.ttf")
        self.npfont.setPixelsPerUnit(120)

        #   - PARENT BOX INCASE WANTED IN THE FUTURE -
        #self.frame = DirectFrame(parent=render2d, frameColor=(0, 0, 0.4, 1),
        #                        frameSize=(-0.25, 0.25, -0.15, 0.15),
        #                        pos=(-0.7, 0, 0.8))


        self.jetpackStatus = OnscreenText(text='JETPACK FUEL: 100%', pos=(-0.95, 0.9),font=self.npfont,
                                          fg=(212/255,175/255,55/255,1),
                                          scale=0.06,parent=render2d, shadow=(0.05,0.05,0.05,1)
                                          ,shadowOffset=(0.05,0.05), align = TextNode.ALeft)

        # self.jetpackStatus.setShadow(0.05)
        # self.jetpackStatus.setShadowColor(0,0,0,1)



