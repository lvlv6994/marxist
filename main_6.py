from manim import *

class ChineseChessBoard(Scene):
    def construct(self):
        # 棋盘的尺寸
        rows = 10
        cols = 9
        square_size = 1  # 每个格子的大小

        # 创建棋盘边框
        border = Rectangle(width=cols * square_size, height=rows * square_size)
        
        # 创建纵向的线
        vertical_lines = VGroup()
        for col in range(cols):
            x = col * square_size - (cols - 1) / 2 * square_size
            line = Line(
                start=[x, (rows - 1) / 2 * square_size, 0],
                end=[x, -(rows - 1) / 2 * square_size, 0]
            )
            vertical_lines.add(line)
        
        # 创建横向的线
        horizontal_lines = VGroup()
        for row in range(rows):
            y = row * square_size - (rows - 1) / 2 * square_size
            line = Line(
                start=[-(cols - 1) / 2 * square_size, y, 0],
                end=[(cols - 1) / 2 * square_size, y, 0]
            )
            horizontal_lines.add(line)

        # 添加楚河汉界的标记
        chu_he_han_jie = Text("楚河              汉界", font_size=24, color=RED)
        chu_he_han_jie.move_to([0, 0, 0])

        # 将所有元素添加到场景
        self.add(border, vertical_lines, horizontal_lines, chu_he_han_jie)

        # 动画展示棋盘
        self.play(Create(border))
        self.play(Create(vertical_lines), Create(horizontal_lines))
        self.play(Write(chu_he_han_jie))
        self.wait(2)

if __name__ == "__main__":
    from manim import config
    config.media_width = "50%"
    config.verbosity = "WARNING"
    scene = ChineseChessBoard()
    scene.render()
