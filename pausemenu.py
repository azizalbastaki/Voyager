# Written by Abdulaziz Albastaki in June 2022
from direct.gui.OnscreenText import OnscreenText
from direct.gui.OnscreenImage import OnscreenImage
from direct.gui.DirectButton import DirectButton
from panda3d.core import TextNode, CardMaker


class pauseMenu():
    def __init__(self,ourRender):
        # self.topLeftHUD = OnscreenImage(image='assets/base/GUI/HUD2.png', pos=(-1.5, 0, 0.7),scale=0.2)

        self.cardMaker = CardMaker('pausemenu')
        self.cardMaker.setColor(1,1,1,0.3)
        self.cardMaker.setFrameFullscreenQuad()
        self.card = render2d.attachNewNode(self.cardMaker.generate())
        self.cardTexture = loader.loadTexture('assets/base/GUI/pausemenubackground.jpeg')
        self.card.setTexture(self.cardTexture)
        #self.resumeGameMode = ourResume

        self.npfont = loader.loadFont("assets/base/fonts/OPTINewportLand.ttf")

        self.menuText = OnscreenText(text='Pause Menu', pos=(0, 0.7),font=self.npfont,
                                          fg=(212/255,175/255,55/255,1),
                                          scale=0.06,parent=self.card, shadow=(0.05,0.05,0.05,1)
                                          ,shadowOffset=(0.05,0.05), align = TextNode.ACenter)

        self.resumeButton = DirectButton(text=("Resume"),

                 scale=0.1, command=self.hide)

    # def resumeFunc(self):
    #     print("Clicked!")
    #     self.card.hide()
    #     self.menuText.hide()
    #     self.resumeButton.hide()
    #     #self.resumeGameMode()

    def show(self):
        print("HELLO")
        self.card.show()
        self.menuText.show()
        self.resumeButton.show()

    def hide(self):
        print("HIDE!")
        self.card.hide()
        self.menuText.hide()
        self.resumeButton.hide()





