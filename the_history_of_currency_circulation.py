#!./bin/python3
from manim import *

Text.set_default(font="Songti SC",font_size=100)

class THE_HISTORY_OF_CURRENCY_CIRCULATION(Scene):
    def construct(self):
        """
        中国货币史
        """
        
        text = Text("中国货币史",font_size=150)
        self.play(Write(text,run_time = 1))
        self.play(FadeOut(text,run_time = 1))
        
        text = Text("先秦时期")
        self.play(Write(text,run_time = 1))
        self.play(FadeOut(text,run_time = 1))

        image1 = ImageMobject("640px-Cypraea_Moneta_Unearthed_in_Shaoxing_2012-07.jpeg").shift(LEFT * 3)
        image2 = ImageMobject("640px-Monetaria_moneta_01.jpeg").shift(RIGHT * 3)

        self.play(FadeIn(image1),run_time = 1)
        self.play(FadeIn(image2),run_time = 1)

        self.play(FadeOut(image1,run_time = 1))
        self.play(FadeOut(image2,run_time = 1))
        
        text = Text("商代")
        self.play(Write(text,run_time = 1))
        self.play(FadeOut(text,run_time = 1))
        
        text = Text("周代")
        self.play(Write(text,run_time = 1))
        self.play(FadeOut(text,run_time = 1))
        
        text = Text("秦至两汉")
        self.play(Write(text,run_time = 1))
        self.play(FadeOut(text,run_time = 1))




        pass
