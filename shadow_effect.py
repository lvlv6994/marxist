from manim import *

class ShadowEffect(Scene):
    def construct(self):
        # 创建一个圆形
        circle = Circle(radius=1, color=BLUE)
        
        # 创建一个阴影，稍微大一些并且有透明度
        shadow = Circle(radius=1.1, color=GREY, fill_opacity=0.5)
        
        # 调整阴影的位置，使其看起来像是从光源方向投射出来的
        shadow.shift(DOWN * 0.1 + LEFT * 0.1)
        
        # 先添加阴影，再添加实际图形，这样阴影会在图形下面
        self.add(shadow, circle)

# 运行这个 Scene 的命令是
# manim -pql script.py ShadowEffect
