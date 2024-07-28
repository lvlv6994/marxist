from manim import *
import numpy as np

class MovingCube3D(ThreeDScene):
    def construct(self):
        # 创建 3D 立方体

        self.camera.background_color = "#ece6e2"
        cube = Cube()

        # 设置立方体的颜色
        cube.set_fill(RED, opacity=0.8)
        cube.set_stroke(RED, width=2)

        # 显示立方体
        self.play(Create(cube))

        # 立方体移动到右边
        self.play(cube.animate.shift(RIGHT * 2))

        # 立方体旋转
        self.play(cube.animate.rotate(PI / 4, axis=UP))

        # 立方体在三维空间中旋转
        self.play(cube.animate.rotate(PI / 4, axis=RIGHT))


        def path_func(t):
            x = np.sin(t)
            y = np.cos(t)
            z = t
            return np.array([x,y,z])

        # 创建路径对象
        path = ParametricFunction(path_func, t_range=[0, 2*PI], color=WHITE)

        # 绘制路径
        self.play(Create(path))
        path_animation = MoveAlongPath(cube,path,run_time =10, rate_func = linear)

        self.play(path_animation)

        # 结束
        self.wait(2)
