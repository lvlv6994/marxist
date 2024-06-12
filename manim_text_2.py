from manim import *

Text.set_default(font="Xingkai SC",color=BLACK,font_size=180,weight=BOLD)
class ManimText1(Scene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        Kongzi = Text("""丘也闻有国有家者，
        \n不患寡而患不均，不患贫而患不安。
        \n盖均无贫，和无寡，安无倾。
        \n夫如是，故远人不服，则修文德以来之。
        \n既来之，则安之。
        \n                        ---- 孔子""",font_size = 50)
        self.play(Write(Kongzi),run_time =2)
        self.play(FadeOut(Kongzi),run_time = 1)
        Yinyang = ImageMobject("./yin-yang.png").scale(0.5)
        
        # self.play(Transform(Kongzi,Yinyang),run_time = 2)
        self.play(FadeIn(Yinyang),run_time = 2)
        self.play(Yinyang.animate.rotate(5*TAU/4),run_time = 4)
        pass

class ManimText2(Scene):
    def construct(self):
        text = Text("你好",font="Xingkai SC",font_size=180,weight=BOLD)
        image = ImageMobject("image_marx.jpeg")
        group = Group(text,image).arrange(RIGHT)
        
        self.add(group)

        #self.play(Write(text,run_time = 2))

class ManimText3(Scene):
    def construct(self):
        text = Text("共产主义",font="Xingkai SC",font_size=180,weight=BOLD)
        self.add(text)
        #self.play(Write(text,run_time = 2))

class ManimText4(Scene):
    def construct(self):
        text = Text("共产主义",font="Baoli SC",font_size=180,weight=BOLD)
        self.add(text)
        #self.play(Write(text,run_time = 2))

class ManimText5(Scene):
    def construct(self):
        text = Text("共产主义",font="Kaiti SC",font_size=180,weight=BOLD)
        self.add(text)
        #self.play(Write(text,run_time = 2))

        
