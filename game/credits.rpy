transform scroll_up:
    yanchor 0.0 ypos 1.0
    linear 30 yanchor 1.0 ypos 0.0

screen credits:

    modal True
    
    frame:
        xsize 1280
        ysize 720
        
        background "#000000"

        vbox at scroll_up:
        
            xalign 0.5

            style_prefix "credits"

            label "Programmer"
            text "Leeann G (Moonlit_heart)"
            text "Jalen (Jaygantic)"

            label "Writer"
            text "Ronnie (CLTurtle)"
            text "Allie L (InkAtlas)"
            text "Jalen (Jaygantic)"
            
            label "Artist"
            text "Shakoba"
            text "Ronnie (CLTurtle)"

            label "Title Art"
            text "Ronnie (CLTurtle)"
            text "Allie L (InkAtlas)"

            label "UI Art and Design"
            text "Jalen (Jaygantic)"

            label "Sound Designer"
            text "Ronnie (CLTurtle)"

            label "Music"
            text "Autumn Scene by Keys of Moon"
            text "Winter Joy by Keys Of Moon"
            text "Lights by Roa"
            text "Jul by Scott Buckley"
            text "Flowing Into The Darkness by Nyoko"
            text "Miss You by Sarah Jansen"
            text "Only Memories Remain by Hayden Folker"
            text "Blooming Melody by Keys Of Moon"
            text "Enchanted by Keys Of Moon"
            text "Icicles by The Piano Says"
            text "Until We Meet Again by Arthur Vyncke"
            
            label "Image Assets"
            text "Title Art Lens Flare - notjungcg (vecteezy.com)"
            text "Beach - Mariakray (Adobe Stock)"
            text "Downtown - Unknown (explorelouisiana.com)?"
            text "Boba Store - Suzi Pratt (seattle.eater.com)"
            text "Apartment - kurtgoltz (flickr.com)"
            text "Ice Rink - suloev.d (wallpapers.com)"
            text "Airport - cindhyade (vecteezy.com)"

            label "Special Thanks"
            text "Heimer Dongger"
            text "Everyone in SJSU’s Game Dev Club!"

            label ""
            text "This game was made in 24 hours for Global Game Jam 2025."

    timer 30 action Hide("credits", transition=dissolve)

style credits_text:
    xalign 0.5

style credits_label:
    xalign 0.5
    top_padding 64