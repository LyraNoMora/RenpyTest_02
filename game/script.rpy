# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define p = Character("Persona", color="#32a852")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg day

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show player panick

    # These display lines of dialogue.

    p "You've created a new Ren'Py game."

    show bg night
    ## dissolve goes from scene 1 to scene 2, fade goes from scene 1 to black screen to scene 2
    with dissolve

    show player default

    p "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.
    menu:

        "Yes":
            return
        "No":
            return
        "I'm nervous":
            return
        "Bye":
            return
        "Yes":
            return
        "No":
            return
        "I'm nervous":
            return
        "Bye":
            return
        "Yes":
            return
        "No":
            return
        "I'm nervous":
            return
        "Bye":
            return
        "Yes":
            return
        "No":
            return
        "I'm nervous":
            return
        "Bye":
            return
        "Yes":
            return
        "No":
            return
        "I'm nervous":
            return
        "Bye":
            return
        "Yes":
            return
        "No":
            return
        "I'm nervous":
            return
        "Bye":
            return

    return
