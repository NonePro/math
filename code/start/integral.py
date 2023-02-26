from manimlib import *


class Integral(Scene):
    def construct(self) -> None:
        axes = Axes((-3, 20), (-3, 15))
        axes.add_coordinate_labels()
        self.play(Write(axes))

        graph = axes.get_graph(lambda x: 0.1 * (x + 3 - 5) * (x - 3 - 5) * (x - 5) + 5, x_range=[-2, 15])
        self.play(Write(graph))
        self.embed()
