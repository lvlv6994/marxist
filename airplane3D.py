from manim import *
# watchman
class Airplane3D(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # 创建飞机的主体
        body = Cylinder(radius=1, height=10, direction=RIGHT).set_color(BLUE)
        body.shift(UP * 0.2)

        # 创建飞机的机翼
        wing1 = Prism(dimensions=[0.05, 1.5, 0.6]).set_color(RED)
        wing2 = wing1.copy()
        wing1.shift(UP * 0.2 + LEFT * 0.6)
        wing2.shift(UP * 0.2 + RIGHT * 0.6)

        # 创建飞机的尾翼
        tail = Prism(dimensions=[0.05, 0.8, 0.2]).set_color(GREEN)
        tail.shift(UP * 0.9 + LEFT * 1.9)

        # 创建飞机的水平尾翼
        horizontal_tail = Prism(dimensions=[0.05, 0.5, 0.2]).set_color(GREEN)
        horizontal_tail.shift(UP * 0.2 + LEFT * 1.9)

        # 创建飞机的机头
        nose = Cone(base_radius=0.2, height=0.4, direction=RIGHT).set_color(YELLOW)
        nose.shift(UP * 0.2 + RIGHT * 1.2)

        # 将所有部件添加到场景中
        # self.add(body, wing1, wing2, tail, horizontal_tail, nose)
        self.add(body)

        # 方式1: 使用 move_camera
        self.move_camera(phi=60 * DEGREES, theta=45 * DEGREES, run_time=5)
        self.wait(5)

        # 方式2: 使用 rotate 旋转对象
        self.play(Rotate(body, angle=PI / 2, axis=UP, run_time=5))
        self.wait(5)

        # 方式3: 使用 set_camera_orientation 设置相机角度
        self.set_camera_orientation(phi=45 * DEGREES, theta=60 * DEGREES)
        self.wait(5)
        # 绕Y轴旋转飞机
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(10)

if __name__ == "__main__":
    from manim import config
    config.media_width = "50%"
    config.verbosity = "WARNING"
    scene = Airplane3D()
    scene.render()
