from manim import *


MarkupText.set_default(font="Songti SC",font_size=50,fill_color = BLACK)

class AnimatedTextColoring(MovingCameraScene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        text1 = MarkupText("马克思")
        self.play(Indicate(text1, color=YELLOW,run_time = 1))
        text2 = MarkupText("恩格斯")
        self.play(ReplacementTransform(text1,text2))
        self.wait(2)

        text3 = MarkupText("私有制").next_to(text2,RIGHT * 4)
        self.play(Write(text3,run_time = 1))
        self.play(self.camera.frame.animate.move_to(text3))
        self.wait(2)

        text4 = MarkupText("圈地运动").next_to(text3,RIGHT * 4 + UP * 4)
        self.play(Write(text4,run_time = 1))
        self.play(self.camera.frame.animate.move_to(text4))
        self.wait(2)
        text5 = MarkupText("货币").next_to(text3,RIGHT * 4)
        self.play(Write(text5,run_time = 1))
        self.play(self.camera.frame.animate.move_to(text5))
        self.wait(2)
        
        text6 = MarkupText("资本").next_to(text3,RIGHT * 4 + DOWN  * 4)
        self.play(Write(text6,run_time = 1))
        self.play(self.camera.frame.animate.move_to(text6))
        self.wait(2)


        text7 = MarkupText("股市").next_to(text6,RIGHT * 4 + DOWN  * 4)
        self.play(Write(text7,run_time = 1))
        self.play(self.camera.frame.animate.move_to(text7))
        self.wait(2)

        text8 = MarkupText("金融").next_to(text7,RIGHT * 4 + DOWN  * 4)
        self.play(Write(text8,run_time = 1))
        self.play(self.camera.frame.animate.move_to(text8))
        self.wait(2)
        
        self.play(self.camera.frame.animate.scale(2),run_time = 1)
        


        

# 运行这个 Scene 的命令是
# manim -pql script.py AnimatedTextColoring
