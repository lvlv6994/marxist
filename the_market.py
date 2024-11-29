from manim import *

Text.set_default(font_size=100,font="Songti SC",fill_color=BLACK)

class THE_MARKET(MovingCameraScene):
    def construct(self):
        """
        如何理解中国的民用市场，毛时代有没有民用市场? 从什么角度去看待市场呢？
        从改革开放的历史看市场的逻辑。为什么当年有口号是反官倒呢？毛时代的中
        国人，80，90年代中国人是不是同样的呢？新闻自由，言论自由，很时髦嘛。
        出现89学运的历史背景是什么呢？主要矛盾是什么呢？资产阶级自由化的问题。
        后毛时代的左派去哪里了？是不存在了还是发不出声音了。
        市场的意义，货币的意义，代码的意义。
        """
        # if the code is like this , and coding is not art .
        # if only for the work ,and not be useful
        self.camera.background_color = "#ece6e2"
        self.camera.background_color = "#ece6e2"
        self.add_sound("the_market.mp3")
        
        text = Text("什么是市场？")
        self.play(Write(text,run_time = 1))
        #  工业化
        #  制造 
        #  商品
        #  市场
        
        # the important of China is the market of people
        text1 = Text("存在主义",font_size = 50).next_to(text,DOWN)
        text2 = Text("现实主义",font_size = 50).next_to(text,DOWN)
        self.play(Create(text1,run_time = 1))
        self.wait(2)
        self.play(ReplacementTransform(text1,text2))
        self.wait(2)
        self.play(FadeOut(text2,run_time = 1))
        
        VGroup(text,text1,text2).move_to(UP * 2)
        VGroup(text,text1,text2).move_to(UP * 2)

        text3 = Text("马克思")

        self.play(Write(text3,run_time = 2))        

        text4 = Text("凯恩斯").next_to(text3,RIGHT * 4)
        self.play(Write(text4,run_time = 1))
        self.play(self.camera.frame.animate.move_to(text4))

        text5 = Text("哈耶克").next_to(text3,RIGHT * 4)
        self.play(Write(text5,run_time = 1))
        self.play(self.camera.frame.animate.move_to(text5))
#        self.play(self.camera.frame.animate.move_to(text5))

        text6 = Text("弗里德曼").next_to(text5,RIGHT * 4)
        self.play(Write(text6,run_time = 1))
        self.play(self.camera.frame.animate.move_to(text6))

        self.play(self.camera.frame.animate.scale(2),run_time = 2)

        

        
