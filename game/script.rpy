# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Protagonist", color="#32a852")
define Poppie = Character("Poppie", color="#f0b5d2")
define g = Character("Girl", color="#f0b5d2")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # change to black screen
    scene bg day

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "I’m walking home, just taking the cool breeze in."

    #scene bg beach
    #with dissolve

    "As I continue down the road, something catches my eye."

    p "...!"

    p "A bubble?"

    p "Heh, that’s quite nostalgic. I remember playing with bubbles when I was younger."

    "I look around and see the source of the bubble."

    #show Poppie default

    g "..."

    "It seems she’s playing with bubble bottles on her own."

    "She seems lost in her thoughts."

    g "Hm?"

    "She looks up, directly at my eye."

    "Crap, I gotta say something before this situation turns awkward."

    p "Sorry to intrude, I saw you playing here by yourself."

    #show Poppie smile

    g "Greetings! My name is Poppie."
menu:
    "Nice to meet you too!":
        jump choices1_common
    "Good day!":
        jump choices1_common
    "Pleased to meet you!":
        jump choices1_common
    "Did you know that climate change is going to be the end of the planet as we know it?":
        jump choices1_common

label choices1_common:

    Poppie "So, what do you think about bubbles?"

    p "...?"

    "Her sudden question caught me off guard."

    p "Yeah. Bubbles are... quite something."

    Poppie "I love bubbles!"

    p "I see."

    Poppie "Here, take this."

    "She handed me her bubble bottles."

    p "Why are you giving me this?"

    Poppie "I’m getting tired of blowing bubbles, your turn!"

    p "..."

    "Against my better judgement, I began blowing bubbles."

    Poppie "Yay!"

    "She begins dancing around, trying to pop every bubble blown."

    "I’ll be honest, it does feel kinda heart warming."

    "Almost resembling when I was a kid and I was still playing with bubbles."

    #fade to black

    #fade to beach

    Poppie "May I ask you something?"

    p "What’s up?"

    Poppie "What do you think about bubbles?"

    p "Didn’t you ask me earlier?"

    Poppie "Well, answer it again!"

    p "Enough of you asking me that, why don’t you answer?"

    #show Poppie surprised

    Poppie "..."

    Poppie "You know what I think?"

    Poppie "I think..."

    Poppie "...Bubbles are like life."

    Poppie "One day, a life is created one day, any time your life can just pop."

    p "..."

    "What a strange answer she gave."

    Poppie "So, are you doing anything tomorrow?"

    p "No, why?"

    Poppie "Great! Meet me back here, 11am!"

    "Poppie immediately begins skipping away."

    p "Wait! You forgot your bubble bottle!"

    "In the distance, I hear a faint voice yell back at me:"

    Poppie "Keep it!"

    "I look down at the bubble bottle then back at her and crack a faint smile."

    p "What an odd girl."

    #fade to black

    "I show up back at the beach at 11am."

    Poppie "Finally, you’re here! I’ve been waiting here for like forever!"

    p "Forever? I’m actually 5 minutes early!"

    Poppie "Wait, really?"

    "It’s not, I’m actually 5 minutes late."

    Poppie "Well whatever, let’s get going!"

    #fade to black 

    #scene downtown

    "We walk for a few minutes, and eventually we arrive at downtown."

    Poppie "Geez, there's a lot of people today, isn’t there?"

    p "There’s always a lot of people here. Is this your first time coming downtown?"

    Poppie "No! It’s my second time!"

    #fade to black

    #back to downtown

    "The sun is beating down today."

    Poppie "Hey, are you feeling thirsty?"

    p "Yeah, a little."

    p "I know of a nearby restaurant we could grab something to drink at."

    Poppie "Awesome, let’s check it out!"

    #scene to restaurant

    p "Here we are."

    Poppie "Woah, look at all these choices!"

    p "Well you better hurry up, because the line’s gonna pile on."

    "There wasn’t actually a line behind us, but I’d rather not spend the whole day waiting for her to choose."

    #show Poppie sad

    Poppie "Aaaah! I can’t decide!"

    p "So you wanna just not drink anything and dehydrate?"

    #show Poppie smile

    Poppie "I know! I’ll go with whatever you get!"

    p "Are you serious?"

    Poppie "Yeah, I trust you!"

    Poppie "So, what are you getting?"
menu:
    "Bubble Tea":
        jump choices2_a
    "Milk Tea":
        jump choices2_b
    "Soda":
        jump choices2_c

label choices2_a:
    #show Poppie cheery
    Poppie "Good choice! We’ll get 2 of that!"
    jump choices2_common

label choices2_b:
    Poppie "Alright, we’ll get 2 of that!"
    jump choices2_common

label choices2_c:
    Poppie "Right then, we’ll get 2 of that!"
    jump choices2_common

label choices2_common:
    #fade to black
    #fade to restaurant
    #show Poppie default

    p "How’s your drink?"

    Poppie "Very bubbly."

    p "Heh, I see."

    " "

    Poppie "Aw..."

    p "What’s wrong?"

    Poppie "My bubble bottle’s out of water."

    p "You know there’s other ways to make bubbles."

    Poppie "How?"

    p "With this."

    "I pull out a packet of-"

    Poppie "What is this?"

    p "Bubble gum."

    Poppie "But it says \“Hubba Bubba\” on it."

    p "Just take one and pop it in your mouth."

    Poppie "Alright."

    "Poppie took one and observed it for a bit."

    p "What’re you waiting for? It’s not gonna poison you or anything."

    "After hearing me, Poppie immediately ate it."

    Poppie "So how are we going to make bubbles with Hubba Bubba?"

    p "Like this."

    "*POP*"

    #show Poppie surprised

    Poppie "Woah! How did you do that?"
menu:
    "You can just flatten it on your tongue, and blow.":
        jump choices3_common
    "Latch it to the tip of your tongue, then blow on it.":
        jump choices3_common
    "Just YOLO it.":
        jump choices3_common

label choices3_common:
    #show Poppie smile
    Poppie "Okay, I’ll try!"

    #show Poppie Trying as hard as possible to blow a bubble
    "Poppie tries to blow as hard as possible."

    "Eventually something came out of her mouth."

    "..."

    #show Poppie surprised

    Poppie "...!"

    "And her gum landed on my face."

    p "..."

    Poppie "..."

    p "Maybe that’s enough bubble blowing for today."

    #show beach at sunset
    
    call screen the_big_question()

    return
