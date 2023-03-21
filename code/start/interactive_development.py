from manimlib import *


class InteractiveDevelopment(Scene):
    def construct(self) -> None:
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)
        square = Square()

        self.play(ShowCreation(square))
        self.wait()

        # 打开python终端
        self.embed()

        # 尝试拷贝粘贴下面这些行到交互终端中
        self.play(ReplacementTransform(square, circle))
        self.wait()
        self.play(circle.animate.stretch(4, 0))
        self.play(Rotate(circle, 90 * DEGREES))
        self.play(circle.animate.shift(2 * RIGHT).scale(0.25))

        text = Text("""
            In general, using the interactive shell is very helpful when developing new scenes
        """)
        self.play(Write(text))

        # 在交互终端中，你可以使用play,add,remove,clear,wait,save_state和restore来代替self.play,self.add ...

        # 这时如果要使用鼠标键盘来与窗口互动，需要输入执行touch()
        # 然后你就可以滚动窗口，或者在按住z时滚动来缩放
        # 按住d时移动鼠标来更改相机视角，按r重置相机位置。
