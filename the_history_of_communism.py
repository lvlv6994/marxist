from manim import *

MarkupText.set_default(font="Xingkai SC", font_size=180, color=WHITE, weight=BOLD, line_spacing = 2)
Text.set_default(font="Xingkai SC", font_size=180, color=WHITE, weight=BOLD, line_spacing = 2)
Circle.set_default(color=WHITE,fill_color=WHITE,fill_opacity=1)

class ManimText(Scene):
    def communismus(self):
        text = Text("共产主义",color="#FF1F38",font="Xingkai SC",font_size=180,weight=BOLD)
        image = ImageMobject("question-mark.png")
        image.scale(0.2)
        group = Group(text,image).arrange(RIGHT,buff = 1);
        self.play(Write(text,run_time = 2),FadeIn(image,run_time = 2))
        self.play(*[FadeOut(Group(text,image),run_time = 1)])

        image = ImageMobject("kongzi.png").scale(0.5).shift(LEFT * 5)
        self.play(FadeIn(image))
        text = Text("大道之行也，天下为公").scale(0.4).shift(RIGHT * 2)
        self.play(Write(text))
        self.play(FadeOut(text),FadeOut(image))
        
        text = Text("马克思主义:").scale(0.5).shift(UP * 3 + LEFT * 3)
        self.play(Write(text))
        text1 = Text("社会产品极大丰富").scale(0.5)
        text2 = Text("人们具有高度的思想觉悟").scale(0.5)
        text3 = Text("人间天堂")
        self.play(Write(text1))
        self.wait(2)
        self.play(ReplacementTransform(text1,text2))
        self.wait(2)
        self.play(ReplacementTransform(text2,text3),FadeOut(text))
        self.wait(2)
        self.play(FadeOut(text3))
        image = ImageMobject("public/images/a_question_mark.png")
        self.play(FadeIn(image),run_time = 2)
        self.play(FadeOut(image))
        
        pass

    def hammer_and_sickle(self):
        image = ImageMobject("Hammer_and_sickle_red_on_transparent.svg.png")
        image.scale( 2)
        self.play(FadeIn(image))
        self.play(FadeOut(image))
        pass

    def a_question_mark_image(self):
        image = ImageMobject("./public/images/a_question_mark.png")
        self.add(image)
        pass
    
    def question_mark_image(self):
        image = ImageMobject("./question-mark.svg")
        self.add(image)
        pass

    def images(self):
        image1 = ImageMobject("capitalism-and-labor.jpg").shift(LEFT * 3)
        image2 = ImageMobject("victorian_satire.jpg").shift(RIGHT * 3)
        self.play(
            FadeIn(image1,run_time = 1),
            FadeIn(image2,run_time = 1),
            )
        self.wait(2)
        self.play(
            FadeOut(image1,run_time = 1),
            FadeOut(image2,run_time = 1),
        )
        
        text = Text("无产阶级的出路在哪里？").scale(0.5)
        text1 = Text("内卷、躺平？").scale(0.5)
        self.play(Write(text),run_time = 1)
        self.play(ReplacementTransform(text,text1),run_time = 1)
        self.play(FadeOut(text1))
        
        image1 = ImageMobject("mr-capitalism-game-over.jpg").shift(LEFT * 3)
        image2 = ImageMobject("istockphoto.jpg").shift(RIGHT * 3)
        self.play(
            FadeIn(image1,run_time = 1),
            FadeIn(image2,run_time = 1),            
        )
        self.wait(2)
        self.play(
            FadeOut(image1,run_time = 1),
            FadeOut(image2,run_time = 1),            
        )

        text  = Text("""
        现在的问题是：
        物质极大丰富的时候，
        人类是和谐还是灭亡呢？
        """).scale(0.4)
        self.play(Create(text),run_time = 1)
        self.play(FadeOut(text),run_time = 1)
        
        pass
    
    def construct(self):
        # self.question_mark_image()
        self.communismus()
        self.what_is_the_history()
        self.karl_marx()

        pass
    
    def what_is_the_history(self):
        text_history = Text("What is History?",font= "Hack Nerd Font",font_size = 100)
        text_history_old1 = Text("分久必合，合久必分").scale(0.5)
        text_history_old2 = Text("你方唱罢我登场").scale(0.5)
        text_history_old3 = Text("周而复始，循环往复").scale(0.5)
        
        self.play(Write(text_history));
        self.wait(2)
        self.play(ReplacementTransform(text_history,text_history_old1))
        self.wait(2)
        self.play(ReplacementTransform(text_history_old1,text_history_old2))
        self.wait(2)
        self.play(ReplacementTransform(text_history_old2,text_history_old3))
        self.wait(2)
        self.play(FadeOut(text_history_old3))
        
        # text_history_old_yin_yang = ImageMobject("./yin-yang.png") # this image is svg and blackground
        
        # self.play(FadeIn(text_history_old_yin_yang),run_time=2)
        # self.play(FadeOut(text_history_old_yin_yang),run_time=2)


        engels_image = ImageMobject("public/images/engels_1856.jpg").scale(1).shift(RIGHT * 5 + UP * 2)
        self.play(FadeIn(engels_image),run_time = 2)
        text_history_new = Text("一切成文史都是阶级斗争的历史").scale(0.4)
        self.play(Write(text_history_new))
        self.wait(2)
        self.play(FadeOut(text_history_new),FadeOut(engels_image))
        pass

    
    def karl_marx(self):

        Kongzi = MarkupText("""
        丘也闻有国有家者，
        <span fgcolor="red">不患寡而患不均，不患贫而患不安。</span>
        盖均无贫，和无寡，安无倾。
        夫如是，故远人不服，则修文德以来之。
        既来之，则安之。
        """,font_size = 50,line_spacing = 1)
        self.play(Write(Kongzi,run_time = 2));
        self.play(FadeOut(Kongzi,run_time = 2));

        self.images()           # 资本主义本身存在的矛盾

        # 巴黎公社
        # 十月革命

        text_marx = Text("马克思")
        image_marx = ImageMobject("image_marx.jpeg")
        self.play(*[Write(text_marx,run_time = 1)])
        self.play(Group(text_marx,image_marx).arrange(DOWN).animate.shift(LEFT * 3).scale(0.5),run_time = 1)
        
        text_marx_theories = Text("1.无产阶级专政\n2.生产资料公有制",).shift(RIGHT * 3).scale(0.25);
        
        self.play(Write(text_marx_theories),run_time = 2)
        self.play(FadeOut(text_marx,run_time = 2),FadeOut(image_marx,run_time=2))
        self.play(text_marx_theories.animate.scale(2))
        text_marx_theories_change = Text("1.独裁\n2.官僚资本主义").scale(0.5)
        self.play(ReplacementTransform(text_marx_theories,text_marx_theories_change),run_time = 1)
        self.play(FadeOut(text_marx_theories_change,run_time = 2))

        
        text_liening = Text("列宁")
        image_liening = ImageMobject("image_liening.jpg").scale(1.5)
        self.play(Create(text_liening,run_time = 2))

        self.play(Group(text_liening,image_liening).arrange(DOWN).animate.shift(LEFT * 3).scale(0.5),run_time = 1)
        text_liening_theories = Text("1.社会主义建设\n2.党的领导\n3.国际主义\n4.实践重于理论").shift(RIGHT * 3).scale(0.25);
        self.play(Write(text_liening_theories),run_time = 2)
        self.play(FadeOut(text_liening,run_time = 2),FadeOut(image_liening,run_time = 2))
        self.play(FadeOut(text_liening_theories,run_time = 2))
        
        text_mao = Text("毛泽东")
        image_mao = ImageMobject("image_maozedong.png").scale(0.5)
        self.play(Create(text_mao,run_time = 2))
        self.play(Group(text_mao,image_mao).arrange(DOWN).animate.shift(LEFT * 3).scale(0.5),run_time = 1)        
        text_mao_theories = Text("1.人民公社\n2.文化大革命\n").shift(RIGHT * 3).scale(0.25);
        self.play(Write(text_mao_theories),run_time = 2)
        self.play(FadeOut(text_mao,run_time = 2),FadeOut(image_mao,run_time = 2))
        self.play(FadeOut(text_mao_theories,run_time = 2))
