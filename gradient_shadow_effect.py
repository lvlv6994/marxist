from manim import *

class GradientShadowEffect(Scene):
    def construct(self):
        # 创建一个圆形
        circle = Circle(radius=1, color=BLUE)
        
        # 创建一个带有渐变颜色的阴影效果
        shadow = Circle(radius=1.1)
        shadow.set_fill(color=[GREY, GREY_A, GREY_C, GREY_E], opacity=0.8)
        shadow.set_stroke(width=0)  # 移除阴影的边框
        
        # 调整阴影的位置
        shadow.shift(DOWN * 0.1 + LEFT * 0.1)
        
        # 添加阴影和实际图形
        self.add(shadow, circle)

# 运行这个 Scene 的命令是
# manim -pql script.py GradientShadowEffect
