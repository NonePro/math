from manimlib import *


class MoveTo(Scene):
    def construct(self) -> None:
        c = Circle()
        self.play(c.animate.shift(RIGHT + DOWN))
        self.wait()
        self.play(c.animate.to_edge(LEFT))


class MoveToAnotherObject(Scene):
    def construct(self) -> None:
        h = Text("Hello")
        h.to_edge(UP)

        s = Square()
        s.next_to(h, DOWN)

        self.add(h, s.rotate(-PI / 4))
        self.wait()
        self.play(s.animate.rotate(PI / 4))  # 注意如果是播放动画需要使用animate
        self.wait()

        tran1 = Triangle()
        tran2 = Triangle()
        tran2.rotate(PI).shift(0.5 * DOWN)
        vg = VGroup(tran1, tran2)
        vg.shift(DOWN)
        self.add(vg)
        self.play(vg.animate.rotate(PI / 2))


class ColorChange(Scene):
    def construct(self) -> None:
        t = Text("Some text")
        t.set_color(BLUE_E)
        self.play(t.animate.scale(3))
        self.play(t.animate.set_color_by_gradient(RED_D, YELLOW_E))
        self.add(t)
        self.wait()


class Rainbow(Scene):
    def construct(self) -> None:
        r = Text("RAINBOW")
        r[0].set_color(RED)
        r[1].set_color(ORANGE)
        r[2].set_color(YELLOW)
        r[3].set_color(GREEN)
        r[4].set_color(TEAL)
        r[5].set_color(BLUE)
        r[6].set_color(PURPLE)

        self.play(Write(r), run_time=5)


class Work(Scene):
    def construct(self) -> None:
        w = Tex(R"W(s) = \int \vec{F}(s)\cdot d\vec{s}", t2c={"s": YELLOW})
        self.play(Write(w), run_time=4)
