from manimlib import *


class HelloWorld(Scene):
    def construct(self) -> None:
        t = Text("Hello world!")
        self.play(Write(t))
        self.wait()

        circle = Circle()
        self.play(ShowCreation(circle))
        self.wait()

        dashed_square = DashedVMobject(Square())
        self.play(ShowCreation(dashed_square))
        self.play()

        line = Line(np.array([4, 0, 0]), np.array([6, 0, 0]))
        self.play(ShowCreation(line))
