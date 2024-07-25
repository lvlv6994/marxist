from manim import *

Text.set_default(font="Songti SC",font_size=100)

class THE_LEFT(Scene):
    def construct(self):
        self.add_sound('the_left.mp3')
        self.play(Write(Text("什么是左？"),run_time = 1))
        pass
