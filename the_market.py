from manim import *


Text.set_default(font_size=100,font="Songti SC")


class THE_MARKET(Scene):
    def construct(self):
        self.add_sound("the_market.mp3")
        text = Text("什么是市场？")
        self.play(Write(text,run_time = 1))
        self.play(FadeOut(text,run_time = 1))

        text1 = Text("存在主义")
        text2 = Text("现实主义")
        self.play(Create(text1,run_time = 1))
        self.wait(2)
        self.play(ReplacementTransform(text1,text2))
        self.wait(2)
        self.play(FadeOut(text2,run_time = 1))
        
        


        pass
