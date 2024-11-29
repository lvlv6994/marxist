from manim import *

Text.set_default(font_size=100,font="Songti SC",fill_color=BLACK)


class THE_POLITICS_OF_CHINA(MovingCameraScene):
    def construct(self):
        self.camera.background_color = "#ece6e2"

        text = Text("中国政治的逻辑是什么？",font_size = 50)
        
        self.play(Write(text,run_time = 1))


        self.play(FadeOut(text,run_time = 1))

        # 中国革命的逻辑是什么呢？
        """
        农民革命的成果是否被偷窃了？中国的农民革命的历史经验。
        """
        text = Text("农民革命",font_size = 50)
        self.play(Write(text,run_time = 1))
        
        
        pass
