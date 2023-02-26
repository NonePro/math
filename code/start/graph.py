from manimlib import *


class GraphExample(Scene):
    def construct(self) -> None:
        axes = Axes((-3, 10), (-1, 8))
        axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        # 默认平滑插值
        sin_graph = axes.get_graph(lambda x: 2 * math.sin(x), color=BLUE)

        # 平滑性设置 -> 设置插值方式为非平滑
        relu_graph = axes.get_graph(lambda x: max(x, 0), use_smoothing=False, color=YELLOW)

        # 连续点设置
        step_graph = axes.get_graph(lambda x: 2.0 if x > 3 else 1.0, discontinuities=[3], color=GREEN)

        sin_label = axes.get_graph_label(sin_graph, R"sin(x)")
        relu_label = axes.get_graph_label(relu_graph, Text("Relu"))
        step_label = axes.get_graph_label(step_graph, Text("Step"), x=4)

        self.play(ShowCreation(sin_graph), FadeIn(sin_label, RIGHT))
        self.wait(2)
        self.play(ReplacementTransform(sin_graph, relu_graph), FadeTransform(sin_label, relu_label))
        self.wait(2)
        self.play(ReplacementTransform(relu_graph, step_graph), FadeTransform(relu_label, step_label))
        self.wait()

        parabola = axes.get_graph(lambda x: 0.25 * x**2)
        parabola.set_stroke(BLUE)
        self.play(FadeOut(step_graph), FadeOut(step_label), ShowCreation(parabola))
        self.wait()

        # 获取图像上的点
        dot = Dot(color=RED)
        dot.move_to(axes.i2gp(2, parabola))
        self.play(FadeIn(dot, scale=0.5))

        # 制作可变参数动画 ValueTracker Updater f_always
        x_tracker = ValueTracker(2)
        f_always(dot.move_to, lambda: axes.i2gp(x_tracker.get_value(), parabola))
        self.play(x_tracker.animate.set_value(4), run_time=3)
        self.play(x_tracker.animate.set_value(-2), run_time=3)
        self.wait()
        self.play(FadeOut(parabola), FadeOut(dot))
