from manim import *



class DotTest(Scene):
    def construct(self):
        dot = Dot(radius=1,color=RED)
        self.add(dot)
        pass
class AMSLaTeX(Scene):
    def construct(self):
        tex = Tex(r'$\mathtt{H} \looparrowright$ \LaTeX', font_size=144)
        self.add(tex)


class AMSLaTeX2(Scene):
    def construct(self):
        tex = Tex(r'$\mathtt{H} \looparrowright$ \LaTeX', font_size=144)
        self.add(tex)


class LaTeXTemplateLibrary(Scene):
    def construct(self):
        tex = Tex('你好 \\LaTeX', tex_template=TexTemplateLibrary.ctex, font_size=144)
        self.add(tex)        
