# little hack i did to make it work: give this screen an argument
screen the_big_question(v = [0]):
    style_prefix "choice"

    python:
        BouncingBubble.update_bubble_radius(600 / 2)
    
    for val in v:
        textbutton 'Can I take you on a date?' at bounce_update(val), pop_in(val), fade_in(val) action Return():
            xysize (600, 600) 
    
    timer 0.016 repeat True action Function(update_bouncing_bubbles)