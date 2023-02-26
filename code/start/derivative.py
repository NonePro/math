import sympy as sp
from manimlib import *


class Diff(Scene):
    def construct(self) -> None:
        axes = Axes()
        self.add(axes)

        x = sp.symbols('x')
        f = sp.sin(x)
        f_graph = axes.get_graph(sp.lambdify(x, f))
        self.add(f_graph)

        df = sp.diff(f, x)
        print(df)
        df_graph = axes.get_graph(sp.lambdify(x, df))
        self.add(df_graph)