from manimlib import *


# 理解屏幕坐标和坐标轴坐标两套坐标之间的关系
class CoordinateSystem(Scene):
    def construct(self) -> None:
        axes = Axes(x_range=(-1, 10),
                    y_range=(-2, 2, 0.5),
                    height=6,
                    width=10,
                    axis_config={
                        "stroke_color": GREY_A,
                        "stroke_width": 2,
                    },
                    y_axis_config={
                        "include_tip": False,
                    })
        axes.add_coordinate_labels(font_size=20, num_decimal_places=1)
        self.add(axes)

        dot = Dot(fill_color=RED)
        dot.move_to(axes.c2p(0, 0))
        self.play(FadeIn(dot))
        self.play(dot.animate.move_to(axes.c2p(3, 2)))
        self.wait()
        self.play(dot.animate.move_to(axes.c2p(5, 0.5)))
        self.play()

        print(axes.p2c(dot.get_center()))

        # 每一帧都会重新复制，保证直线会跟随着点来移动
        h_line = always_redraw(lambda: axes.get_h_line(dot.get_left()))
        v_line = always_redraw(lambda: axes.get_v_line(dot.get_bottom()))
        self.play(ShowCreation(h_line), ShowCreation(v_line))
        self.play(dot.animate.move_to(axes.c2p(3, -2)))
        self.wait()
        self.play(dot.animate.move_to(axes.c2p(1, 1)))
        self.wait()

        # 将点始终固定到坐标轴的1,1位置上。从这里看到点是相对于屏幕来说的，坐标是相对于坐标轴来说的
        f_always(dot.move_to, lambda: axes.c2p(1, 1))
        self.play(axes.animate.scale(0.75).to_corner(UL), run_time=2)
        self.wait()
        self.play(FadeOut(VGroup(axes, dot, h_line, v_line)))
