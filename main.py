
#from pydub import AudioSegment

from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService




class MarxistAnimation(Scene):
    def construct(self):
        
        self.camera.background_color = "#ece6e2"
        self.add_sound("audio.wav")
        
        group = Group()
        msf = Text("马上风", font="Xingkai SC",font_size=30,color=BLACK).scale(1.5)
        self.play(Write(msf),run_time=1)
        group.add(msf)
        self.play(group.animate.shift(UP*4))
        self.add_sound("demo.mp3")
        self.wait()
        
        gongchanzhuyi = Text("共产主义",font="Xingkai SC",color=BLACK).scale(1.5)
        self.play(Write(gongchanzhuyi),run_time=2)
        group.add(gongchanzhuyi)
        self.play(group.animate.shift(UP*4))
        
        a_question_mark = ImageMobject('./public/images/a_question_mark.png')
        self.play(FadeIn(a_question_mark))
        group.add(a_question_mark)
        self.play(group.animate.shift(UP*10))

        makesi = ImageMobject('./public/images/karl_marx.png').shift(LEFT * 3).scale(0.8)
        diyiguoji = Text("第一国际",font="Xingkai SC",color=BLACK).shift(RIGHT * 1)
        baligongshe = Text("巴黎公社",font="Xingkai SC",color=BLACK).shift(RIGHT * 4)
                
        self.play(FadeIn(makesi))
        self.play(Write(diyiguoji))
        self.play(Write(baligongshe))
        
        group.add(baligongshe)
        group.add(makesi)
        group.add(diyiguoji)
        
        self.play(group.animate.shift(UP*4))

        liening = ImageMobject("./public/images/liening.png").shift(LEFT * 3).scale(0.9)
        dierguoji = Text("第二国际",font="Xingkai SC",color=BLACK).shift(RIGHT * 1)
        shiyuegeming = Text("十月革命",font="Xingkai SC",color=BLACK).shift(RIGHT * 4)
        
        group.add(liening)
        group.add(dierguoji)
        group.add(shiyuegeming)
        
        self.play(group.animate.shift(UP*4))

        maozedong = ImageMobject('./public/images/maozedong.png').shift(LEFT * 3).scale(0.5)
        zhonggong = Text("毛泽东思想",font="Xingkai SC",color=BLACK).shift(RIGHT)

        self.play(FadeIn(maozedong))
        self.play(Write(zhonggong))
        
        group.add(maozedong)
        group.add(zhonggong)
        self.play(group.animate.shift(UP*5))

        tietuo = ImageMobject('./public/images/tietuo.jpg').shift(LEFT * 3).scale(2)
        tietuozhuyi = Text("铁托主义",font="Xingkai SC",color=BLACK).shift(RIGHT)

        self.play(FadeIn(tietuo))
        self.play(Write(tietuozhuyi))
        
        group.add(tietuo)
        group.add(tietuozhuyi)
        self.play(group.animate.shift(UP * 4))
        
