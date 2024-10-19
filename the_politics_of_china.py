from manim import *

Text.set_default(font_size=100,font="Songti SC",fill_color=BLACK)


class THE_POLITICS_OF_CHINA(MovingCameraScene):
    def construct(self):
        self.camera.background_color = "#ece6e2"

        text = Text("中国政治的逻辑是什么？",font_size = 50)
        self.play(Write(text,run_time = 1))
        pass
