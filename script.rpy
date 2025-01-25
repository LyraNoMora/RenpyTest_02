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
    #scene beach sunset

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "The same walk home is always accompanied by the cool ocean breeze."

    scene beach sunset
    with dissolve

    "Left at the intersection, three blocks down, right at the corner store, and then I’m home."

    "I like it when things stay the same. Routines are predictable, dependable."

    "As I continue down the road, something catches my eye."

    p "...!"

    p "A bubble?"

    "That’s new. Where are those bubbles coming from?"

    "I follow the trail and see the source of the floating chaos:"

    #show Poppie looking away neutral

    g "..."

    "It seems she’s playing with a small bubble wand on her own."

    "She seems lost in her thoughts."

    p "Hey you!"

    "Why did I say that?!"

    g "Hm?"

    "She looks up, directly at my eye."

    "Crap, I gotta say something before this situation turns awkward."

    p "Sorry to interrupt, but I was drawn here by the bubbles floating down the road. Why are you doing that?"

    #show Poppie neutral

    g "Doing what?"

    p "Blowing bubbles by yourself?"

    g "Why wouldn’t I?"

    #show Poppie smile

    g "..."

    g "My name is Poppie, nice to meet you bubble police!"
menu:
    "Nice to meet you too!":
        jump choices1_common
    "Hey, I’m no bubble police!":
        jump choices1_common
    "Be careful, I might have to give you a ticket.":
        jump choices1_common

label choices1_common:

    #show Poppie neutral

    Poppie "So my bubbles brought you here to me, hm?"

    p "...Sort of? I guess, yeah they did."

    Poppie "Do you like them?"

    p "I was actually pretty distracted by them. It sort of interrupted my walk home."

    #show Poppie sad

    Poppie "So you don’t like them..."

    p "No-! I mean yes-! I mean-!"

    p "I do like them, of course."

    p "It’s just that I wasn’t expecting to see them today."

    "What am I saying? I like bubbles now?"

    "Well, I guess they do make me feel a little nostalgic."

    #show Poppie smile

    Poppie "I love bubbles!"

    p "I guessed as much."

    #show Poppie neutral

    Poppie "Here, take this."

    "She handed me her bubble bottles."

    #show Poppie serious

    p "Why are you giving me this?"

    Poppie "I’m getting tired of blowing bubbles, it's your turn!"

    p "..."

    "Against my better judgement, I began blowing bubbles."

    #show Poppie smile

    Poppie "Yay!"

    "She begins dancing around, trying to pop every bubble that floats by her."

    "The evening sun reflects off the soapy bubbles, illuminating them like a sea of glass."

    "I’ll be honest, it does make me feel a bit happier."

    "Watching her jumping around reminds me of myself when I was a kid and still playing with bubbles."

    "Things feel easier when your only care in the world is popping as many bubbles as you can."

    scene beach sunset
    with dissolve

    #show Poppie neutral

    Poppie "Hey, may I ask you something?"

    p "What’s up?"

    Poppie "What do you think about bubbles?"

    p "Didn’t you ask me earlier?"

    #show Poppie serious

    Poppie "Well, answer it again!"

    p "Enough of you asking me that, why don’t you answer?"

    #show Poppie surprised

    Poppie "...!"

    #show Poppie neutral

    Poppie "..."

    Poppie "You know what I think?"

    Poppie "I think..."

    #show Poppie smile

    Poppie "...Bubbles are a lot like people."

    Poppie "Some are small, some are big and round, others wobbly, or sturdy."

    Poppie "All these bubbles float up, dance around in the air, trying not to bump into each other."

    Poppie "Sometimes they do bump into one another, and stick together."

    Poppie "...And like a bubble, it’ll continue to fly high, ever drifting, oblivious to what comes next."

    Poppie "Then, one day, it pops."

    Poppie "With no rhyme or reason. It just pops, and it’s gone in an instant."

    p "..."

    "What a strange answer."

    "She seems so light and happy, but that response was so bleak."

    "There’s definitely more to this girl than spontaneous bubble blowing."

    #show Poppie neutral

    Poppie "So, are you doing anything tomorrow?"

    p "Huh?!"

    Poppie "What? It’s a simple question."

    p "That's quite the topic change."

    Poppie "Just answer."

    p "Well, I’m not, but-"

    #show Poppie cheery

    Poppie "Great! Meet me back here, 11am sharp!"

    #fade Poppie
    "Poppie immediately begins skipping away."

    "I glance down at my hands and realize I’m still holding her bubble bottle."



    p "Wait! You forgot your bottle!"

    "In the distance, I hear a faint voice yell back at me."

    Poppie "Keep it! You can give it back to me tomorrow!"

    "I look down at the bubble bottle then back at her and crack a faint smile."

    p "What an odd girl."

    scene beach day
    with fade

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
