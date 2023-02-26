from manimlib import *


class Eoc1Thumbnail(Scene):

    def construct(self):
        title = Text(
            "The Essence of Calculus",
            t2c={
                "\\emph{you}": YELLOW,
            },
        )
        subtitle = Text("Chapter 1")
        subtitle.match_width(title)
        subtitle.scale(0.75)
        subtitle.next_to(title, DOWN)
        # title.add(subtitle)
        title.set_width(FRAME_WIDTH - 2)
        title.to_edge(UP)
        title.set_stroke(BLACK, 8, background=True)
        # answer = OldTexText("...yes")
        # answer.to_edge(DOWN)

        axes = Axes(
            x_range=(-1, 5, 1),
            y_range=(-1, 5, 1),
            y_axis_config={
                "include_tip": False,
            },
            x_axis_config={
                "unit_size": 2,
            },
        )
        axes.set_width(FRAME_WIDTH - 1)
        axes.center().to_edge(DOWN)
        axes.shift(DOWN)

        graph = axes.get_graph(self.func)
        rect_list = axes.get_riemann_rectangles(graph, x_range=[0, 4, 0.001], dx=0.1)
        rect_list.set_submobject_colors_by_gradient(PURPLE, ORANGE)
        rect_list.set_opacity(1)
        rect_list.set_stroke(BLACK, 1)

        self.add(axes)
        self.add(graph)
        self.add(rect_list)
        self.add(title)
        # self.add(answer)

    def func(self, x):
        return 0.35 * ((x - 2)**3 - 2 * (x - 2) + 6)