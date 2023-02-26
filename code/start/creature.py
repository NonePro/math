from manimlib import *
from manimlib.mobject.svg.old_tex_mobject import *

from custom.backdrops import *
from custom.banner import *
from custom.characters.pi_creature import *
from custom.characters.pi_creature_animations import *
from custom.characters.pi_creature_scene import *
from custom.deprecated import *
from custom.drawings import *
from custom.end_screen import *
from custom.filler import *
from custom.logo import *
from custom.opening_quote import *


class NowWeHaveEmotions(TeacherStudentsScene):
    def construct(self):
        # mob = SVGMobject("E:\\study\\math\\assets\\images\\pi_creature\\plain.svg")
        # self.add(mob)
        # randy = Randolph()
        # self.add(randy)
        # self.play(randy.change("pondering"))
        # self.wait()
        # self.play(Blink(randy))
        # self.wait()

        self.play(self.change_students('happy', 'hooray', 'well'))
        self.play_change_teacher('happy')
        self.teacher_says('Now we have emotions!')
        self.wait()
        self.student_says('Hooray!', index=1, target_mode='hooray')
        self.play_change_teacher('hooray')
        self.wait(2)
        self.play(RemovePiCreatureBubble(self.students[1], 'hooray'))
        self.wait(3)