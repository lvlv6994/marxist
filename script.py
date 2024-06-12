from manim import *

class AnimatedTextColoring(Scene):
    def construct(self):
        # 创建一个带有部分文本着色的 MarkupText 对象
        text = MarkupText(
            'This is an <span fgcolor="red">animated</span> word.',
            font_size=48
        )

        # 将文本对象添加到场景中
        self.add(text)


        # 对文本对象应用动画
        self.play(Indicate(text, color=YELLOW))
        self.wait(2)

# 运行这个 Scene 的命令是
# manim -pql script.py AnimatedTextColoring
