from manim import *

Text.set_default(font="Songti SC",font_size=50,fill_color=BLACK)

class THE_HISTORY_OF_COLONIAL_DEVELOPMENT(MovingCameraScene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        text = Text("后殖民主义现象",font='Osaka')
        self.play(Write(text,run_time=2))
        self.play(FadeOut(text))
        text = Text("崇洋媚外",font="Songti SC")
        self.play(Write(text,run_time=2))
        self.play(FadeOut(text))
