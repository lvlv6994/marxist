from manim import *

class WavyArrowExample(Scene):
    def construct(self):
        # 定义波浪线路径
        wave_path = VMobject()
        wave_path.set_points_smoothly([
            [-3, 0, 0], [-2, 1, 0], [-1, -1, 0], [0, 1, 0], [1, -1, 0], [2, 1, 0], [3, 0, 0]
        ])
        wave_path.set_stroke(width=6)

        # 创建箭头头部
        arrow_tip = ArrowTip(tip_length=0.3).move_to(wave_path.get_end())

        # 将波浪线和箭头头部组合成一个整体
        wavy_arrow = VGroup(wave_path, arrow_tip)

        # 显示波浪线箭头
        self.play(Create(wavy_arrow))
        self.wait(2)
