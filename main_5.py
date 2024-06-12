from manim import *

class Main_5(Scene):
    def construct(self):
        self.camera.background_color ="#ece6e2"
        self.add(Circle(radius=2, color=BLACK, fill_color=RED, fill_opacity=0.5).shift(LEFT * 3))
        self.add(Circle(radius=2, color=BLACK, fill_color=RED, fill_opacity=0.5).shift(RIGHT * 3))
        self.add(Text("将",font="Xingkai SC",color=BLACK,font_size = 180,weight=BOLD).shift(LEFT * 3))
        self.add(Text("军",font="Xingkai SC",color=BLACK,font_size = 180,weight=BOLD).shift(RIGHT * 3))
        pass




