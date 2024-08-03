from manim import *

Text.set_default(font="Songti SC",font_size=100)

class THE_LEFT(Scene):
    def construct(self):
        self.add_sound('the_left.mp3')
        text = Text("什么是左？")
        self.play(Write(text,run_time = 1))
        text1 = Text("姓资姓社？")
        self.play(ReplacementTransform(text,text1,run_time = 1))
        self.wait(2)
        self.play(FadeOut(text1,run_time = 1))
        

        
        
        pass
