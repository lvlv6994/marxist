from manim import *

"""
中国改革开放的历史

"""

Text.set_default(font="Songti SC",font_size=100)

class THE_CHANGED_AND_OPENED(Scene):
    def construct(self):
        """
        中国是如何实现私有化的？
        """

        self.add_sound("the_changed_and_opened.mp3")
        self.play(Write(Text("改革开放"),run_time = 1))


        
        pass
