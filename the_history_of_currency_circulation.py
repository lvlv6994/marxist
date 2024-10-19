#!./bin/python3
from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService

"""
还是需要将文字转语音的功能写入代码中，而不是说明网站。当然这个问题是需要使用程序解决的。
使用tts或者是chattts。目前chattts似乎有点问题。

"""


Text.set_default(font="Songti SC",font_size=100)

class THE_HISTORY_OF_CURRENCY_CIRCULATION(Scene):
    def construct(self):
        """
        中国货币史
        """
        text = Text("中国货币史",font_size=150)
        self.play(Write(text,run_time = 1))
        self.add_sound("the_history_of_currency_circulation_1.wav")
        self.wait(12)
        self.play(FadeOut(text,run_time = 1))

        """
        重点是不同的货币对应的不同的社会形态。不应该是罗列哪个朝代使用了什么样的钱币。分析共产主义
        的那个题目也是这个样子的，要有问题意识，共产主义当年为什么火热现在为什么有销声匿迹了。哪个
        共产主义的理想到底能不能实现了，现实中共产主义的问题是什么呢？人民 领袖 党 的关系是什么？
        现在的社会能不能从技术的角度实现共产主义。

        贝壳作为货币对社会发展的影响，
        金属铸币作为货币对社会发展的影响，
        纸币作为货币对社会发展的影响，
        数字货币对社会发展的影响。

        钱作为货币的历史
        钱作为资本的历史
        钱作为生产资料的历史
        
        """
        
        text = Text("先秦时期")
        self.play(Write(text,run_time = 1))
        self.play(FadeOut(text,run_time = 1))

        # 货币到底和什么有关系呢？单纯的交换经济，货币是金融的特征吧。有货币的话，说明是有银行。
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

        image1 = ImageMobject("22-23mm.jpg")
        self.play(FadeIn(image1),run_time = 1)
        self.play(FadeOut(image1),run_time = 1)
        
        image1 = ImageMobject("174001.jpg").shift(LEFT * 3)
        image2 = ImageMobject("174000.jpg").shift(RIGHT * 3)
        
        self.play(FadeIn(image1),run_time = 1)
        self.play(FadeIn(image2),run_time = 1)
        
        self.play(FadeOut(image1,run_time = 1))
        self.play(FadeOut(image2,run_time = 1))

        text = Text("谢谢收看",font_size=150)
        self.add_sound("the_history_of_currency_circulation_2.wav")
        self.play(Create(text),run_time = 1)
        self.play(FadeOut(text),run_time = 1)


        pass
 
