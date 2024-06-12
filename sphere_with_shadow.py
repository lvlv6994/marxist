from manim import *

class SphereWithShadow(ThreeDScene):
    def construct(self):
        # 设置摄像机位置
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # 创建一个球体
        sphere = Sphere(radius=1, color=BLUE)
        sphere.shift(UP)  # 将球体移动到上方，便于看到阴影

        # 创建一个平面来投射阴影
        plane = NumberPlane()
        plane.shift(DOWN)

        # 创建一个稍大的圆形来模拟阴影
        shadow = Circle(radius=1.2, color=GREY, fill_opacity=0.5)
        shadow.rotate(PI / 2, axis=RIGHT)  # 将圆形旋转到平面上
        shadow.shift(DOWN * 1.02)  # 将阴影移动到球体正下方

        # 添加球体、平面和阴影
        self.add(plane)
        self.add(shadow)
        self.add(sphere)

        # 如果需要更逼真的效果，可以考虑调整透明度和阴影的位置
        self.wait()

# 运行这个 Scene 的命令是
# manim -pql script.py SphereWithShadow
