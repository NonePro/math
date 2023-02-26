from manimlib import *

from custom.drawings import *
from custom.characters.pi_creature import *
from sympy import symbols, diff

DISTANCE_COLOR = BLUE
TIME_COLOR = YELLOW
VELOCITY_COLOR = GREEN


class VelocityAtIndividualPointsVsPairs(Scene):
    CONFIG = {
        "start_time" : 6.5,
        "end_time" : 3,
        "dt" : 1.0,
    }
    def construct(self):
        axes = Axes()
        distance_graph = axes.get_graph(lambda t : 100*smooth(t/10.))
        distance_label = axes.get_graph_label( distance_graph, label = "s(t)")
        x = symbols('x')
        f = x**2 + 2*x - 3
        df = diff(f,x)
        velocity_graph = distance_graph.get_derivative_graph()
        self.play(ShowCreation(velocity_graph))
        velocity_label = self.label_graph(
            velocity_graph, 
            label = "v(t)",
            proportion = self.start_time/10.0, 
            direction = UP,
            buff = MED_SMALL_BUFF
        )
        velocity_graph.add(velocity_label)

        self.show_individual_times_to_velocity(velocity_graph)
        self.play(velocity_graph.fade, 0.4)
        self.show_two_times_on_distance()
        self.show_confused_pi_creature()

    def show_individual_times_to_velocity(self, velocity_graph):
        start_time = self.start_time
        end_time = self.end_time
        line = self.get_vertical_line_to_graph(start_time, velocity_graph)
        def line_update(line, alpha):
            time = interpolate(start_time, end_time, alpha)
            line.put_start_and_end_on(
                self.coords_to_point(time, 0),
                self.input_to_graph_point(time, graph = velocity_graph)
            )

        self.play(ShowCreation(line))
        self.wait()
        self.play(UpdateFromAlphaFunc(
            line, line_update,
            run_time = 4,
            rate_func = there_and_back
        ))
        self.wait()
        velocity_graph.add(line)

    def show_two_times_on_distance(self):
        line1 = self.get_vertical_line_to_graph(self.start_time-self.dt/2.0)
        line2 = self.get_vertical_line_to_graph(self.start_time+self.dt/2.0)
        p1 = line1.get_end()
        p2 = line2.get_end()
        interim_point = p2[0]*RIGHT+p1[1]*UP
        dt_line = Line(p1, interim_point, color = TIME_COLOR)
        ds_line = Line(interim_point, p2, color = DISTANCE_COLOR)
        dt_brace = Brace(dt_line, DOWN, buff = SMALL_BUFF)
        ds_brace = Brace(ds_line, RIGHT, buff = SMALL_BUFF)
        dt_text = dt_brace.get_text("Change in time", buff = SMALL_BUFF)
        ds_text = ds_brace.get_text("Change in distance", buff = SMALL_BUFF)

        self.play(ShowCreation(VGroup(line1, line2)))
        for line, brace, text in (dt_line, dt_brace, dt_text), (ds_line, ds_brace, ds_text):
            brace.set_color(line.get_color())
            text.set_color(line.get_color())
            text.add_background_rectangle()
            self.play(
                ShowCreation(line),
                GrowFromCenter(brace),
                Write(text)
            )
            self.wait()

    def show_confused_pi_creature(self):
        randy = Randolph()
        randy.to_corner(DOWN+LEFT)
        randy.shift(2*RIGHT)

        self.play(randy.change_mode, "confused")
        self.play(Blink(randy))
        self.wait(2)
        self.play(Blink(randy))
        self.play(randy.change_mode, "erm")
        self.wait()
        self.play(Blink(randy))
        self.wait(2)