
## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

init python:
    import math
    import random

    class BouncingBubble:
        bubble_radius = 200 / 2

        wind_angle = 0
        wind_angle_speed = 0
        
        wind_strength = 200

        def __init__(self, x, y):
            self.x = x
            self.y = y
            initial_angle = random.uniform(0, 2 * math.pi)
            initial_speed = random.uniform(70, 100)
            self.dx = math.cos(initial_angle) * initial_speed
            self.dy = math.sin(initial_angle) * initial_speed

        def update(self, dt):
            min_x = BouncingBubble.bubble_radius
            max_x = 1920 - BouncingBubble.bubble_radius
            min_y = BouncingBubble.bubble_radius
            max_y = 1080 - BouncingBubble.bubble_radius

            self.dx += math.cos(BouncingBubble.wind_angle) * BouncingBubble.wind_strength * dt
            self.dy += math.sin(BouncingBubble.wind_angle) * BouncingBubble.wind_strength * dt

            self.x += self.dx * dt
            self.y += self.dy * dt

            if self.x < min_x or self.x > max_x:
                self.dx *= -0.9

            if self.y < min_y or self.y > max_y:
                self.dy *= -0.9
                
            # Clamp
            self.x = max(min_x, min(max_x, self.x))  
            self.y = max(min_y, min(max_y, self.y)) 

        @classmethod
        def update_wind(cls):
            cls.wind_angle_speed += random.uniform(-0.01, 0.01)
            cls.wind_angle += cls.wind_angle_speed

            # Clamp
            cls.wind_angle = cls.wind_angle % (2 * math.pi)

        @classmethod
        def update_bubble_radius(cls, radius):
            cls.bubble_radius = radius

    def create_bouncing_bubbles(count):
        objects = []
        for _ in range(count):
            x = random.uniform(0, 1920)
            y = random.uniform(0, 1080)
            objects.append(BouncingBubble(x, y))
        return objects

    def update_bouncing_bubbles():
        dt = 0.016 # 1 / 60.0

        BouncingBubble.update_wind()

        for obj in bouncing_objects:
            obj.update(dt)
        renpy.restart_interaction()

    bouncing_objects = create_bouncing_bubbles(25)

transform bounce_update(index):
    xpos 0
    ypos 0
    xoffset bouncing_objects[index].x
    yoffset bouncing_objects[index].y
    xanchor 0.5
    yanchor 0.5

transform pop_in(index):
    xzoom 0 yzoom 0
    pause index * 0.15
    easein_back 0.25 xzoom 1.0 yzoom 1.0

screen choice(items):
    style_prefix "choice"

    python:
        BouncingBubble.update_bubble_radius(200 / 2)

    for idx, val in enumerate(items):
        textbutton val.caption xysize (200, 200) action val.action at bounce_update(idx), pop_in(idx)

    timer 0.016 repeat True action Function(update_bouncing_bubbles)


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")
