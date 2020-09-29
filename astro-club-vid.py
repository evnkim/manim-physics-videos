from manimlib.imports import *

class twod_orbit(Scene):
    def construct(self):
        orbitEllipse = Ellipse(width = 10,height =6,color=DARK_GRAY,sheen_factor = 0.7,fill_color = DARK_GRAY,fill_opacity = 0,sheen_direction = RIGHT)
        sun = Circle(color = YELLOW,fill_color = YELLOW,fill_opacity=1,radius=0.5,sheen_factor = 0.9,sheen_direction = UR)
        sun.move_to(2.5*RIGHT)

        sattelite = Circle(color = DARK_GRAY,fill_opacity = 1,fill_color = DARK_GRAY,sheen_factor = 0.9,sheen_direction = UR,radius=0.2)
        sattelite.move_to(5*LEFT)
        sattelite.velVec = UP
        sattelite.count_time = 0
        sattelite.adjustable_constant = 50

        orbitEllipse.count_time = 0

        gravitation_force_vector = Vector(direction = sun.get_center() - sattelite.get_center())
        gravitation_force_vector.put_start_and_end_on(sattelite.get_center(), sattelite.get_center() + (sun.get_center() - sattelite.get_center())*0.5)

        # def ellipse_updater(mob,dt):
        #     time = orbitEllipse.count_time/60
        #     mob.set_sheen_direction =(3*np.sin(time)*UP+5*np.cos(time)*RIGHT)
        
        def force_updater(mob,dt):
            diff_vec  = sun.get_center() - sattelite.get_center()
            diff_vec_mag = np.sqrt(diff_vec[0]*diff_vec[0] + diff_vec[1]*diff_vec[1] + diff_vec[2]*diff_vec[2])
            gravitation_force_vector.put_start_and_end_on(sattelite.get_center(), sattelite.get_center() + 10*(diff_vec)/(diff_vec_mag**3))

        def sattelite_updater(mob,dt):
            diff_vec  = sun.get_center() - sattelite.get_center()
            diff_vec_mag = np.sqrt(diff_vec[0]*diff_vec[0] + diff_vec[1]*diff_vec[1] + diff_vec[2]*diff_vec[2])



            mob.move_to(sattelite.get_center() + sattelite.velVec * dt)
            sattelite.velVec += sattelite.adjustable_constant*(diff_vec)/(diff_vec_mag**3)*dt
        
        gravitation_force_vector.add_updater(force_updater)
        # orbitEllipse.add_updater(ellipse_updater)
        sattelite.add_updater(sattelite_updater)


        for i in range(-6,7):
            for j in range(-4,5):
                locDot = Dot()
                locDot.move_to(RIGHT*i + UP*j)
                self.add(locDot)

        self.add(orbitEllipse,locDot,sun,sattelite,gravitation_force_vector)
        self.wait(10)