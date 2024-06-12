from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService
        
class TriangleExample(Scene):
    def construct(self):
        vertices = [
            [-1, -1, 0],
            [1, -1, 0],
            [0, 1, 0]
        ]
        triangle = Polygon(*vertices, color=BLUE)
        self.add(triangle)
        
        vertices1 = [
            [0, 1, 0],
            [1, -1, 0],
            [-1, -1, 0],
        ]
        triangle1 = Polygon(*vertices, color=BLUE)
        self.add(triangle1)

# Simply inherit from VoiceoverScene instead of Scene to get all the
# voiceover functionality.
class RecorderExample(VoiceoverScene):
    def construct(self):
        # You can choose from a multitude of TTS services,
        # or in this example, record your own voice:
        self.set_speech_service(RecorderService())

        circle = Circle()

        # Surround animation sections with with-statements:
        with self.voiceover(text="This circle is drawn as I speak.") as tracker:
            self.play(Create(circle), run_time=tracker.duration)
            # The duration of the animation is received from the audio file
            # and passed to the tracker automatically.

        # This part will not start playing until the previous voiceover is finished.
        with self.voiceover(text="Let's shift it to the left 2 units.") as tracker:
            self.play(circle.animate.shift(2 * LEFT), run_time=tracker.duration)



class LineChart(Scene):
    def construct(self):
        # 创建坐标系
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 5, 1],
            axis_config={"color": BLUE},
            x_axis_config={"numbers_to_include": range(1, 11)},
            y_axis_config={"numbers_to_include": range(1, 6)}
        )
        # 添加坐标系到画布
        self.play(Create(axes),run_time = 3)
        self.wait()

        # 定义数据点
        data = [(1, 1), (2, 2), (3, 3), (4, 2), (5, 4), (6, 3), (7, 2), (8, 1)]

        # 创建折线
        line = VGroup()
        for i in range(len(data) - 1):
            start_point = axes.c2p(*data[i])
            end_point = axes.c2p(*data[i+1])
            line.add(Line(start_point, end_point, color=RED))

        # 添加折线到画布
        self.play(Create(line),run_time = 3)
            

class TableExamples(Scene):
    def construct(self):
        t0 = Table(
            [["First", "Second"],
             ["Third","Fourth"]],
            row_labels=[Text("R1"), Text("R2")],
            col_labels=[Text("C1"), Text("C2")],
            top_left_entry=Text("TOP"))
        t0.add_highlighted_cell((2,2), color=GREEN)
        x_vals = np.linspace(-2,2,5)
        y_vals = np.exp(x_vals)
        t1 = DecimalTable(
            [x_vals, y_vals],
            row_labels=[MathTex("x"), MathTex("f(x)")],
            include_outer_lines=True)
        t1.add(t1.get_cell((2,2), color=RED))
        t2 = MathTable(
            [["+", 0, 5, 10],
             [0, 0, 5, 10],
             [2, 2, 7, 12],
             [4, 4, 9, 14]],
            include_outer_lines=True)
        t2.get_horizontal_lines()[:3].set_color(BLUE)
        t2.get_vertical_lines()[:3].set_color(BLUE)
        t2.get_horizontal_lines()[:3].set_z_index(1)
        cross = VGroup(
            Line(UP + LEFT, DOWN + RIGHT),
            Line(UP + RIGHT, DOWN + LEFT))
        a = Circle().set_color(RED).scale(0.5)
        b = cross.set_color(BLUE).scale(0.5)
        t3 = MobjectTable(
            [[a.copy(),b.copy(),a.copy()],
             [b.copy(),a.copy(),a.copy()],
             [a.copy(),b.copy(),b.copy()]])
        t3.add(Line(
            t3.get_corner(DL), t3.get_corner(UR)
        ).set_color(RED))
        vals = np.arange(1,21).reshape(5,4)
        t4 = IntegerTable(
            vals,
            include_outer_lines=True
        )
        g1 = Group(t0, t1).scale(0.5).arrange(buff=1).to_edge(UP, buff=1)
        g2 = Group(t2, t3, t4).scale(0.5).arrange(buff=1).to_edge(DOWN, buff=1)
        self.add(g1, g2)
        


class SurfaceExample(Scene):
    CONFIG = {
        "camera_class": ThreeDCamera,
    }

    def construct(self):
        surface_text = Text("For 3d scenes, try using surfaces")
        surface_text.fix_in_frame()
        surface_text.to_edge(UP)
        self.add(surface_text)
        self.wait(0.1)

        torus1 = Torus(r1=1, r2=1)
        torus2 = Torus(r1=3, r2=1)
        sphere = Sphere(radius=3, resolution=torus1.resolution)

        # 你可以使用最多两个图像对曲面进行纹理处理，
        # 这两个图像将被解释为朝向灯光的一侧和远离灯光的一侧。
        # 这些可以是URL，也可以是指向本地文件的路径
        # day_texture = "EarthTextureMap"
        # night_texture = "NightEarthTextureMap"
        day_texture = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4d/Whole_world_-_land_and_oceans.jpg/1280px-Whole_world_-_land_and_oceans.jpg" 
        night_texture = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/The_earth_at_night.jpg/1280px-The_earth_at_night.jpg"

        surfaces = [
            TexturedSurface(surface, day_texture, night_texture)
            for surface in [sphere, torus1, torus2]
        ]

        for mob in surfaces:
            mob.shift(IN)
            mob.mesh = SurfaceMesh(mob)
            mob.mesh.set_stroke(BLUE, 1, opacity=0.5)

        # 设置视角
        frame = self.camera.frame
        frame.set_euler_angles(
            theta=-30 * DEGREES,
            phi=70 * DEGREES,
        )

        surface = surfaces[0]

        self.play(
            FadeIn(surface),
            ShowCreation(surface.mesh, lag_ratio=0.01, run_time=3),
        )
        for mob in surfaces:
            mob.add(mob.mesh)
        surface.save_state()
        self.play(Rotate(surface, PI / 2), run_time=2)
        for mob in surfaces[1:]:
            mob.rotate(PI / 2)

        self.play(
            Transform(surface, surfaces[1]),
            run_time=3
        )

        self.play(
            Transform(surface, surfaces[2]),
            # 在过渡期间移动相机帧
            frame.increment_phi, -10 * DEGREES,
            frame.increment_theta, -20 * DEGREES,
            run_time=3
        )
        # 添加自动旋转相机帧
        frame.add_updater(lambda m, dt: m.increment_theta(-0.1 * dt))

        # 移动光源
        light_text = Text("You can move around the light source")
        light_text.move_to(surface_text)
        light_text.fix_in_frame()

        self.play(FadeTransform(surface_text, light_text))
        light = self.camera.light_source
        self.add(light)
        light.save_state()
        self.play(light.move_to, 3 * IN, run_time=5)
        self.play(light.shift, 10 * OUT, run_time=5)

        drag_text = Text("Try moving the mouse while pressing d or s")
        drag_text.move_to(light_text)
        drag_text.fix_in_frame()

        self.play(FadeTransform(light_text, drag_text))
        self.wait()
        
class CameraExample(Scene):
    def construct(self):
        # 创建一个圆形对象
        circle = Circle()
        # 显示圆形对象
        self.add(circle)

class AnimateChainExample(Scene):
    def construct(self):
        s = Square()
        self.play(Create(s))
        self.play(s.animate.shift(RIGHT).scale(2).rotate(PI / 2))
        self.play(Uncreate(s))
 
class ConnectObjects(Scene):
    def construct(self):
        # 创建两个圆形对象
        circle1 = Circle(radius=1, color=BLUE).shift(LEFT * 3)
        circle2 = Circle(radius=1, color=RED).shift(RIGHT * 3)

        # 创建带有箭头的连接线
        arrow = Arrow(circle1.get_right(), circle2.get_left(), color=GREEN, buff=0.1)

        # 显示对象和连接线
        self.play(Create(circle1), Create(circle2), Create(arrow))

        self.wait(2)  # 等待一段时间
        

class MapAnimation2(Scene):
    def construct(self):
        # 地图坐标数据（经度和纬度）
        map_coordinates = [(0, 0), (1, 0), (1, 1), (0, 1)]
        # 将地图坐标转换为屏幕坐标
        screen_coordinates = [self.coords_to_point(x, y) for x, y in map_coordinates]
        # 创建地图对象
        map_region = Polygon(*screen_coordinates, color=BLUE)
        # 显示地图
        self.play(Create(map_region))
        # 等待一段时间
        self.wait(2)

    def coords_to_point(self, x, y):
        # 实现地图坐标到屏幕坐标的转换
        # 在这里编写你的坐标转换代码
        return np.array([x, y, 0])

class UsefulAnnotations(Scene):
    def construct(self):
        m0 = Dot()
        m1 = AnnotationDot()
        m2 = LabeledDot("ii")
        m3 = LabeledDot(MathTex(r"\alpha").set_color(ORANGE))
        m4 = CurvedArrow(2*LEFT, 2*RIGHT, radius= -5)
        m5 = CurvedArrow(2*LEFT, 2*RIGHT, radius= 8)
        m6 = CurvedDoubleArrow(ORIGIN, 2*RIGHT)

        self.add(m0, m1, m2, m3, m4, m5, m6)
        for i, mobj in enumerate(self.mobjects):
            mobj.shift(DOWN * (i-3))



class MapAnimation(Scene):
    def construct(self):
        # 创建一个简单的地图，由两个区域组成
        region1 = Polygon([-2, -2, 0], [2, -2, 0], [0, 2, 0], color=BLUE)
        region2 = Circle(radius=1, color=RED).shift(3 * RIGHT)

        # 显示地图
        self.play(Create(region1), Create(region2))
        # 等待一段时间
        self.wait(2)


        
class MarkupTest(Scene):
    def construct(self):
        tex = Tex(r"\LaTeX", font_size=144).shift(2*UP)
        self.add(tex)
        text = MarkupText(
            f'<span underline="double" underline_color="green">double green underline</span> in red text<span fgcolor="{YELLOW}"> except this</span>',
            color=RED,
            font_size=34
        )
        self.add(text)




        

class MathTeXDemo(Scene):
    def construct(self):
        rtarrow0 = MathTex(r"\xrightarrow{x^6y^8}", font_size=96)
        rtarrow1 = Tex(r"$\xrightarrow{x^6y^8}$", font_size=96)
        self.add(VGroup(rtarrow0, rtarrow1).arrange(DOWN))


        
class MindMap(Scene):
    def construct(self):
        # 创建主节点
        main_node = Circle(radius=0.5, color=BLUE, fill_opacity=1).shift(UP*2)
        main_text = Text("Main Node", color=WHITE).scale(0.5).next_to(main_node, DOWN)

        # 创建子节点
        child_node1 = Circle(radius=0.3, color=GREEN, fill_opacity=1).shift(LEFT*2)
        child_text1 = Text("Child Node 1", color=WHITE).scale(0.4).next_to(child_node1, DOWN)

        child_node2 = Circle(radius=0.3, color=GREEN, fill_opacity=1).shift(RIGHT*2)
        child_text2 = Text("Child Node 2", color=WHITE).scale(0.4).next_to(child_node2, DOWN)

        # 连接节点
        connection1 = Line(main_node.get_bottom(), child_node1.get_top(), color=WHITE)
        connection2 = Line(main_node.get_bottom(), child_node2.get_top(), color=WHITE)

        # 显示节点和连接线
        self.play(Create(main_node), Create(child_node1), Create(child_node2))
        self.play(Write(main_text), Write(child_text1), Write(child_text2))
        self.play(Create(connection1), Create(connection2))

        self.wait(2)  # 等待一段时间





class ImageExample(Scene):
    def construct(self):
        # 导入图像文件
        image_path = "./public/images/karl_marx.jpg"  # 替换为你的图像文件路径
        image = ImageMobject(image_path).scale(0.25)  # 缩放图像大小
        # 显示图像
        self.play(FadeIn(image),run_time = 2)
        self.wait(2)  # 等待一段时间
        
class ThreeDExample(ThreeDScene):
    def construct(self):
        # 创建立方体
        cube = Cube()
        # 将立方体添加到 3D 场景中
        self.add(cube)
        # 设置摄像头位置和视角
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        self.play(Rotate(cube,axis=OUT,radians=PI/2))

        self.wait(2)  # 等待一段时间        
        
class ManimCELogo(Scene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#343434"
        ds_m = MathTex(r"\mathbb{MSF}", fill_color=logo_black).scale(7)
        ds_m.shift(2.25 * LEFT + 1.5 * UP)
        #circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT)
        #square = Square(color=logo_blue, fill_opacity=1).shift(UP)
        #triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)
        logo = VGroup(ds_m)  # order matters
        logo.move_to(ORIGIN)
        self.play(Create(logo),run_time=3)



            
class GradientExample(Scene):
    def construct(self):
        t = Text("Hello", gradient=(RED, BLUE, GREEN), font_size=96)
        self.add(t)


class Textt2cExample(Scene):
    def construct(self):
        t2cindices = Text('Hello', t2c={'[1:-1]': BLUE}).move_to(LEFT)
        t2cwords = Text('World',t2c={'rl':RED}).next_to(t2cindices, RIGHT)
        self.add(t2cindices, t2cwords)

class DifferentWeight(Scene):
    def construct(self):
        import manimpango

        g = VGroup()
        weight_list = dict(
            sorted(
                {
                    weight: manimpango.Weight(weight).value
                    for weight in manimpango.Weight
                }.items(),
                key=lambda x: x[1],
            )
        )
        for weight in weight_list:
            g += Text(weight.name, weight=weight.name, font="Open Sans")
        self.add(g.arrange(DOWN).scale(0.5))

        
class SlantsExample(Scene):
    def construct(self):
        a = Text("Italic", slant=ITALIC)
        self.add(a)

class FontsExample(Scene):
    def construct(self):
        ft = Text("马上风",font="Songti SC",slant=ITALIC)
        self.play(Create(ft))



class VGroupExample(Scene):
    def construct(self):
        # 创建两个圆形对象
        circle1 = Circle(color=BLUE)
        circle2 = Circle(color=RED).shift(RIGHT * 2)

        # 创建一个VGroup对象
        v_group = VGroup(circle1, circle2)

        # 将另一个圆形对象添加到VGroup中
        circle3 = Circle(color=GREEN).shift(UP * 2)
        v_group.add(circle3)

        # 将VGroup对象显示在场景中
        self.play(Create(v_group))


        self.wait(2)  # 等待一段时间
        


# what is war?

class ArrowExample2(Scene):
    def construct(self):
        circle1 = Circle(color=BLUE).shift(LEFT * 6)
        circle2 = Circle(color=RED).shift(RIGHT * 6)
        self.play(Transform(circle1,circle2),run_time=2)
        pass



class ArrowExample(Scene):
    def construct(self):
        marx_image = ImageMobject("./public/images/karl_marx.jpg").scale(0.25).move_to(LEFT)
        liening_image = ImageMobject("./public/images/LieNing.png").scale(0.15).next_to(marx_image,RIGHT)
        sidalin_image = ImageMobject("./public/images/SiDaLin.jpg").scale(0.5).next_to(liening_image,RIGHT)

        group = Group(marx_image,liening_image,sidalin_image).shift(4*LEFT + 1.5*UP)
        
        self.play(FadeIn(group))

        
        self.wait(2)

        

class IncorrectLaTeXSubstringColoring(Scene):
    def construct(self):
        equation = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots"
        )
        equation.set_color_by_tex("x", YELLOW)
        self.add(equation)
        
class LaTeXSubstrings(Scene):
    def construct(self):
        tex = Tex('Hello', r'$\bigstar$', r'\LaTeX', font_size=144)
        tex.set_color_by_tex('igsta', RED)
        self.add(tex)

class AddPackageLatex(Scene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        tex = Tex(
            r"$\mathscr{H} \rightarrow \mathbb{H}$",
            tex_template=myTemplate,
            font_size=144,
        )
        self.add(tex)

class LaTeXAttributes(Scene):
    def construct(self):
        tex = Tex(r'Hello \LaTeX', color=BLUE, font_size=144)
        self.add(tex)

class AMSLaTeX(Scene):
    def construct(self):
        tex = Tex(r'$\mathtt{H} \looparrowright$ \LaTeX', font_size=144)
        self.add(tex)


