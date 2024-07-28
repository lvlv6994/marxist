from manim import *


Text.set_default(font_size=100,font="Songti SC",fill_color=BLACK)


class THE_MARKET(MovingCameraScene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        self.add_sound("the_market.mp3")
        text = Text("什么是市场？")
        self.play(Write(text,run_time = 1))
        
        text1 = Text("存在主义").next_to(text,DOWN)
        text2 = Text("现实主义").next_to(text,DOWN)
        self.play(Create(text1,run_time = 1))
        self.wait(2)
        self.play(ReplacementTransform(text1,text2))
        self.wait(2)
        self.play(FadeOut(text2,run_time = 1))
        VGroup(text,text1,text2).move_to(UP * 2)

        text3 = Text("马克思")
        arrow = Arrow(text.get_center(),text3.get_center(),color=GREEN,stroke_width=8,tip_length=0.5,tip_shape=ArrowTriangleTip)
        self.play(Create(arrow,run_time=1))
        self.play(Write(text3,run_time = 2))        

        text4 = Text("凯恩斯").next_to(text3,RIGHT * 4)
        self.play(Write(text4,run_time = 1))
        self.play(self.camera.frame.animate.move_to(text4))

        text5 = Text("哈耶克").next_to(text3,RIGHT * 4)
        self.play(Write(text5,run_time = 1))
        self.play(self.camera.frame.animate.move_to(text5))

        text6 = Text("弗里德曼").next_to(text5,RIGHT * 4)
        self.play(Write(text6,run_time = 1))
        self.play(self.camera.frame.animate.move_to(text6))


        self.play(self.camera.frame.animate.scale(2),run_time = 2)

        
        

        pass
    
