from manim import *

config.background_color = '#151515'

class OppenheimerSnyder(Scene):
    def construct(self):
        buff = 0.15
        headheight = 1
        rect1 = RoundedRectangle(
            corner_radius=0.1,
            width=self.camera.frame_width/2 - buff*3/2, height=self.camera.frame_height - buff - headheight,
            fill_color=BLACK, fill_opacity=1, stroke_color='#2A2A2A', stroke_width=2
        )
        rect2 = rect1.copy()
        Group(rect1, rect2).arrange(buff=buff).to_edge(DOWN, buff=buff)
        self.add(rect1, rect2)

        header = Tex("Observer on surface", "Distant observer")
        header.set_y(mid(rect1.get_top()[1], self.camera.frame_height/2) - 0.05)
        header[0].set_x(rect1.get_x())
        header[1].set_x(rect2.get_x())
        self.add(header)

        R_0 = 12
        M = 2
        Delta_tau = PI * R_0 / 2

        star_scale = 1.8 / R_0

        star1 = Dot(radius=star_scale*R_0, color=YELLOW).move_to(rect1)
        star2 = star1.copy().move_to(rect2)
        self.add(star1, star2)

        schwartzschild = DashedVMobject(
            Circle(radius=star_scale*2*M, stroke_width=2, color='#2A2A2A'),
            num_dashes=35, dashed_ratio=1/3
        ).move_to(star2)
        self.add(schwartzschild)

        tau = ValueTracker(0)
        star1.add_updater(lambda mob: mob.scale_to_fit_height(
            star_scale * R_0 * (1 + np.cos(2 * tau.get_value() / R_0))
        ))

        a = 1/3
        f = lambda t: 1 - 2/PI * np.arctan(a*(t - Delta_tau))
        g = lambda t: f(t) * (R_0 - 2*M) / f(0) + 2*M

        star2.add_updater(lambda mob: mob.scale_to_fit_height(
            star_scale * 2 *  g(tau.get_value())
        ))

        self.play(
            tau.animate.set_value(Delta_tau),
            run_time=Delta_tau, rate_func=rate_functions.linear
        )

        star1.clear_updaters()
        tau.add_updater(lambda tracker, dt: tracker.increment_value(dt))

        self.wait(20)


class OppenheimerSnyderSurface(Scene):
    def construct(self):
        buff = 0.15
        headheight = 1
        rect1 = RoundedRectangle(
            corner_radius=0.1,
            width=self.camera.frame_width/2 - buff*3/2, height=self.camera.frame_height - buff - headheight,
            fill_color=BLACK, fill_opacity=1, stroke_color='#2A2A2A', stroke_width=2
        )
        rect2 = rect1.copy()
        Group(rect1, rect2).arrange(buff=buff).to_edge(DOWN, buff=buff)
        self.add(rect1, rect2)

        header = Tex("Observer on surface", "Distant observer")
        header.set_y(mid(rect1.get_top()[1], self.camera.frame_height/2) - 0.05)
        header[0].set_x(rect1.get_x())
        header[1].set_x(rect2.get_x())
        self.add(header)

        header[1].set(color='#2A2A2A')

        R_0 = 12
        M = 2
        Delta_tau = PI * R_0 / 2

        star_scale = 1.8 / R_0

        star1 = Dot(radius=star_scale*R_0, color=YELLOW).move_to(rect1)
        star2 = star1.copy().move_to(rect2)
        self.add(star1, star2)

        schwartzschild1 = DashedVMobject(
            Circle(radius=star_scale*2*M, stroke_width=2, color='#2A2A2A'),
            num_dashes=35, dashed_ratio=1/3
        ).move_to(star1)
        schwartzschild2 = schwartzschild1.copy().move_to(star2)
        self.add(schwartzschild1, schwartzschild2)

        tau = ValueTracker(0)
        star1.add_updater(lambda mob: mob.scale_to_fit_height(
            star_scale * R_0 * (1 + np.cos(2 * tau.get_value() / R_0))
        ))

        self.play(
            tau.animate.set_value(Delta_tau),
            run_time=Delta_tau, rate_func=rate_functions.linear
        )

        star1.clear_updaters()
        
        self.wait(0.5)


class OppenheimerSnyderDistant(Scene):
    def construct(self):
        buff = 0.15
        headheight = 1
        rect1 = RoundedRectangle(
            corner_radius=0.1,
            width=self.camera.frame_width/2 - buff*3/2, height=self.camera.frame_height - buff - headheight,
            fill_color=BLACK, fill_opacity=1, stroke_color='#2A2A2A', stroke_width=2
        )
        rect2 = rect1.copy()
        Group(rect1, rect2).arrange(buff=buff).to_edge(DOWN, buff=buff)
        self.add(rect1, rect2)

        header = Tex("Observer on surface", "Distant observer")
        header.set_y(mid(rect1.get_top()[1], self.camera.frame_height/2) - 0.05)
        header[0].set_x(rect1.get_x())
        header[1].set_x(rect2.get_x())
        self.add(header)

        header[0].set(color='#2A2A2A')

        R_0 = 12
        M = 2
        Delta_tau = PI * R_0 / 2

        star_scale = 1.8 / R_0

        star2 = Dot(radius=star_scale*R_0, color=YELLOW).move_to(rect2)
        self.add(star2)

        schwartzschild1 = DashedVMobject(
            Circle(radius=star_scale*2*M, stroke_width=2, color='#2A2A2A'),
            num_dashes=35, dashed_ratio=1/3
        ).move_to(rect1)
        schwartzschild2 = schwartzschild1.copy().move_to(star2)
        self.add(schwartzschild1, schwartzschild2)

        tau = ValueTracker(0)

        a = 1/3
        f = lambda t: 1 - 2/PI * np.arctan(a*(t - Delta_tau))
        g = lambda t: f(t) * (R_0 - 2*M) / f(0) + 2*M

        star2.add_updater(lambda mob: mob.scale_to_fit_height(
            star_scale * 2 *  g(tau.get_value())
        ))

        self.play(
            tau.animate.set_value(60),
            run_time=60, rate_func=rate_functions.linear
        )

        self.wait(0.5)
