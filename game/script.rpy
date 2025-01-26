# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Protagonist", color="#32a852")
define Poppie = Character("Poppie", color="#f0b5d2")
define g = Character("Girl", color="#f0b5d2")

# Define images

layeredimage Poppie:

    always:
        "poppie_body"

    group face auto:
        attribute neutral default:
            "poppie_neutral"
        attribute sad:
            "poppie_sad"
        attribute smile:
            "poppie_smile"
        attribute surprised:
            "poppie_surprised"
        attribute cheery:
            "poppie_cheery"
        attribute gum:
            "poppie_gum"

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

    $ relationship = 0

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

    show Poppie looking away neutral

    g "..."

    "It seems she’s playing with a small bubble wand on her own."

    "She seems lost in her thoughts."

    p "Hey you!"

    "Why did I say that?!"

    g "Hm?"

    "She looks up, directly at my eye."

    "Crap, I gotta say something before this situation turns awkward."

    p "Sorry to interrupt, but I was drawn here by the bubbles floating down the road. Why are you doing that?"

    show Poppie neutral

    g "Doing what?"

    p "Blowing bubbles by yourself?"

    g "Why wouldn’t I?"

    show Poppie smile

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

    show Poppie neutral

    Poppie "So my bubbles brought you here to me, hm?"

    p "...Sort of? I guess, yeah they did."

    Poppie "Do you like them?"

    p "I was actually pretty distracted by them. It sort of interrupted my walk home."

    show Poppie sad

    Poppie "So you don’t like them..."

    p "No-! I mean yes-! I mean-!"

    p "I do like them, of course."

    p "It’s just that I wasn’t expecting to see them today."

    "What am I saying? I like bubbles now?"

    "Well, I guess they do make me feel a little nostalgic."

    show Poppie smile

    Poppie "I love bubbles!"

    p "I guessed as much."

    show Poppie neutral

    Poppie "Here, take this."

    "She handed me her bubble bottles."

    show Poppie serious

    p "Why are you giving me this?"

    Poppie "I’m getting tired of blowing bubbles, it's your turn!"

    p "..."

    "Against my better judgement, I began blowing bubbles."

    show Poppie smile

    Poppie "Yay!"

    "She begins dancing around, trying to pop every bubble that floats by her."

    "The evening sun reflects off the soapy bubbles, illuminating them like a sea of glass."

    "I’ll be honest, it does make me feel a bit happier."

    "Watching her jumping around reminds me of myself when I was a kid and still playing with bubbles."

    "Things feel easier when your only care in the world is popping as many bubbles as you can."

    scene beach sunset
    with dissolve

    show Poppie neutral

    Poppie "Hey, may I ask you something?"

    p "What’s up?"

    Poppie "What do you think about bubbles?"

    p "Didn’t you ask me earlier?"

    show Poppie serious

    Poppie "Well, answer it again!"

    p "Enough of you asking me that, why don’t you answer?"

    show Poppie surprised

    Poppie "...!"

    show Poppie neutral

    Poppie "..."

    Poppie "You know what I think?"

    Poppie "I think..."

    show Poppie smile

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

    show Poppie neutral

    Poppie "So, are you doing anything tomorrow?"

    p "Huh?!"

    Poppie "What? It’s a simple question."

    p "That's quite the topic change."

    Poppie "Just answer."

    p "Well, I’m not, but-"

    show Poppie cheery

    Poppie "Great! Meet me back here, 11am sharp!"

    show Poppie cheery
    with moveoutright

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

    show Poppie serious

    Poppie "Finally, you’re here! I’ve been waiting here for like, forever!"

    p "Forever? I’m 5 minutes early!"

    show Poppie surprised

    Poppie "Wait, really?"

    "Poppie checks her watch."

    show Poppie serious

    Poppie "You’re five minutes late!"

    p "Alright, you caught me, but I’m here now aren’t I?"

    show Poppie smile

    Poppie "Well whatever, let’s get going!"

    scene downtown day
    with fade

    "We walk for a few minutes, and eventually we arrive downtown."

    show Poppie neutral

    Poppie "Geez, it’s pretty crowded here today, isn’t it?"

    p "Actually this seems pretty normal. There’s always a lot of people. Is this your first time coming downtown?"

    Poppie "No! It’s… it’s my second time!"

    scene downtown day
    with dissolve

    "The sun is beating down today."

    show Poppie neutral

    Poppie "Hey, are you thirsty?"

    p "A little."

    Poppie "I know of a nearby shop we can grab something to drink at."

    p "If this is your second time downtown, how do you know what’s around here?"

    show Poppie smile

    Poppie "Well I found it my first time here! I didn’t order anything, though it looked good."

    p "Alright, let’s go check it out! And actually order something this time, yeah?"

    #script says boba shop, asset is a restaurant
    scene restaurant day
    with dissolve

    show Poppie neutral

    Poppie "Here we are!"

    "She seems a little nervous, but tries to hide it with her bubbly persona."

    Poppie "Look at all these options, it’s going to be a tough choice!"

    p "Well you better hurry up, because the line’s gonna pile on."

    "There wasn’t actually a line behind us, but I’d rather not spend the whole day waiting for her to choose."

    show Poppie serious

    Poppie "Aaaah! I can’t decide!"

    p "So you wanna just not drink anything and dehydrate?"

    show Poppie smile

    Poppie "I know! I’ll go with whatever you get!"

    p "Are you serious?"

    Poppie "Yeah, I trust you!"

    Poppie "So, what are you getting?"
menu:
    "Bubble Tea":
        jump choices2_a
    "Sparkling Water":
        jump choices2_b
    "Soda":
        jump choices2_c

label choices2_a:
    show Poppie cheery
    Poppie "Good choice! We’ll get 2 of that!"
    $ relationship += 1
    jump choices2_common

label choices2_b:
    Poppie "Alright, we’ll get 2 of that!"
    jump choices2_common

label choices2_c:
    Poppie "Right then, we’ll get 2 of that!"
    jump choices2_common

label choices2_common:
    show Poppie
    with dissolve

    "Clerk" "Hello, what may I get you?"

    #show restaurant red tint
menu:
    "What if I order wrong?":
        jump choices5_common
    "What’s my order again?":
        jump choices5_common
    "I can’t disappoint Poppie!":
        $ relationship += 1
        jump choices5_common

label choices5_common:
    p "...!"

    scene restaurant day
    with fade

    show Poppie sad

    Poppie "Hey, is something the matter?"

    p "No, nothing. Nothings wrong."

    Poppie "...Why don’t I order for us?"

    scene restaurant day
    with dissolve

    p "How’s your drink?"

    Poppie "Very bubbly."

    p "Heh, I get it."

    scene beach sunset
    with dissolve

    show Poppie

    Poppie "Well, today was a lot of fun!"

    Poppie "Here, this is for you."

    "Poppie hands me a piece of paper with a phone number on it."

    show Poppie cheery

    Poppie "Call me if you’d like to do this again sometime, yeah?"

    p "Oh, I…um, thank you."

    Poppie "Well, I'll see you around!"

    show Poppie cheery
    with moveoutright

    "Poppie skipped away, bouncing further and further down the street."

    "As I get up to go, I shove my hands in my pocket."

    "I feel a little bottle at the bottom."

    p "Wait, Poppie!"

    "It seems like she didn’t hear me."

    "Dang, I forgot to give her back her bubbles."

    "Wait, I have her number now!"

    "As fast I could, I pulled out my phone and dialed her number."

    "*BEEP*"

    if relationship < 2:
        p "C’mon…"

    "*BEEP*"

    if relationship < 2:
        p "Pick up!"

    p "..."

    "*CLICK*"

    "It’s her!"

    Poppie "Hello!"

    p "Poppie, I-"

    Poppie "Unfortunately, I’m not available at this moment to pick-up my phone, please leave a message after the beep!"

    "*BEEP*"

    p "..."

    "She didn’t pick up my call."

    "That’s fine, maybe she was running so fast that she didn’t hear her phone going off."

    "I put the bubble bottle back into my pocket."

    "Next time I’ll remember."

    #show apartment night
    #with fade

    "What a weird day. Definitely not something I would have planned myself."

    "My routine was thrown off, that’s for sure."

    "..."

    "It was so much more fun."

    "Maybe I should try and call Poppie again to see if she’d like to hang out tomorrow?"

    #show apartment red tint
    #with fade
menu:
    "Maybe I shouldn’t call her...":
        jump choices4_b
    "Is tomorrow too soon to hang out again?":
        jump choices4_b
    "What if she says no?":
        jump choices4_b
    "She didn’t pick up earlier...":
        jump choices4_b
    "Sure, I’ll call her.":
        jump choices4_a

label choices4_a:
    $ relationship += 1

    p "..."
    
    Poppie "Heyyo!"
    
    "She picked up!"
    
    p "Yo, how’s it hanging?"
    
    Poppie "Pretty good!"
    
    Poppie "Oh, I saw your call earlier. Sorry I couldn’t pick up. I was in such a rush that I accidentally left my phone at home today."
    
    p "No worries."

    Poppie "So, what did you call me earlier for?"

    p "I was gonna ask if you’re available to hang out again tomorrow."
    jump choices4_common

label choices4_b:
    p "..."

    "Yeah, maybe it’s best if I don’t."

    "*RIIING RIIING*"

    "...?"

    "My phone’s ringing."

    "*CLICK*"

    p "Hello?"

    Poppie "Thank goodness it’s you!"

    p "Huh?"

    Poppie "Well, I gave you my number, but I never got yours!"

    p "O-oh, right."

    Poppie "I saw I had a missed call from earlier, so I decided to call it and see if it was you!"

    Poppie "And it is! Heyyo!"

    Poppie "By the way, I couldn’t pick up the phone earlier because I was in such a rush that I accidentally left my phone at home!"

    p "No worries."

    "Well since she’s here, I might as well ask what I was going to initially."

    p "Are you, by any chance, busy on the next day? If not, if you would like to wanna meet up somewhere out?"

label choices4_common:
    Poppie "Sure, I’d love to! Maybe we could go to the ice rink together!"

    "The ice rink? But..."

    p "Well, I’m not much of an ice skater myself."

    Poppie "It’s okay! I could teach you! Trust me, I’m a pro!"

    "Even through the phone, I could tell she’s making a smug look."

    p "Heh, very well then. We’ll meet at 11am by the beach, just like today?"

    Poppie "Heehee, you bet!"

    Poppie "See you tomorrow then."

    show beach day
    with fade

    "Morning came pretty fast, and next thing I know, I’m waiting for Poppie at the same spot."

    p "Hm..."

    "I check the clock, it’s 11:10."

    p "She’s certainly taking her time today."

    Poppie "Gooooood morning!"

    "From the distance, I hear Poppie’s faint voice."

    show Poppie

    Poppie "Sorry, were you waiting for a while?"
menu:
    "Nope, I just got here.":
        jump choices6_common
    "What took you so long?":
        jump choices6_a

label choices6_a:
    show Poppie sad

    Poppie "Sorry, I had a bit of trouble sleeping last night."

    p "I see."

    jump choices6_common

label choices6_common:
    show Poppie smile

    Poppie "Well anyways, let’s get going! I’ll lead the way!"

    #scene ice_rink interior
    #with fade

    Poppie "How are those shoes?"

    p "A little tight? Don’t they have a bigger size here?"

    Poppie "Perfect, you’re ready to go, c’mon!"

    #scene ice_rink interior
    #with fade

    "As I step out onto the rink, the ice is slippier than I remember."

    p "So… How does one skate again?"

    Poppie "Just lean your body forward, push your legs forward and out, and glide!"

    p "Like this? WOAAAH!"

    show Poppie moveoutleft

    #shake screen

    "*CRASH*"

    "Apparently, not like that."

    "I fell over."

    p "Ouch..."

    show Poppie smile

    Poppie "Looks like someone forgot to lean forward, silly!"

    p "Well, it’s a lot harder to balance than it looks."

    Poppie "Heehee, here, let me help you up!"

    "Poppie reached out her hand for me."

    show Poppie surprised

    "WA-WAAAH!"

    show Poppie moveoutdown

    "*CRASH*"

    show Poppie sad

    Poppie "WA-WAAAH!"

    "Who’s the silly one now?"

    Poppie "..."

    show Poppie surprised

    Poppie "Huh?"

    "In an instant, Poppie’s smile dissipates, replaced with a curious, childlike expression."

    show Poppie smile

    Poppie "Wow! Look at that!"

    "I look around and notice that there’s bits of snow slowly falling from the ceiling."

    p "Wait, is this real snow?"

    show Poppie

    Poppie "Heehee, take a closer look, why don’t you?"

    "As she requested, I took a closer look at the “snow”."

    p "Wait, these are-!"

    Poppie "That’s right, they’re bubbles!"

    p "I see. Quite a creative way to make fake snow."

    show Poppie cheery

    Poppie "Hahaha!"

    "Poppie seemed to have been enjoying this quite a lot."

    "I couldn’t help but laugh with her."

    #scene ice-rink interior
    #with fade

    "The two of us get up and continue skating together."

    "After a bit of guidance from Poppie, I’m able to keep my balance."

    show Poppie

    Poppie "See, look at you! You’re a natural!"

    p "Heh, yeah I guess."

    #add music here

    Poppie "Woah- HEY! WATCH OUT-"

    show Poppie moveoutleft

    "*CRASH*"

    "It seems like another skater wasn’t paying attention and ran into me."

    "Skater" "Ugh, that was careless of me."

    "Skater" "Hey, sorry about that! Are you okay?"

    #add music - clouded

    #scene ice-rink red tint
menu:
    "Watch where you are going!":
        jump choices7_b
    "Learn how to skate!":
        jump choices7_b
    "Do I look okay to you?":
        jump choices7_b
    "What the heck!":
        jump choices7_b
    "Get outta’ my way!":
        jump choices7_b
    "You skate like an amateur!":
        jump choices7_b
    "All good, no worries!":
        jump choices7_a

label choices7_a:
    $ relationship += 1
    "...!"

    "The right words can’t seem to get out of my mouth."

    #scene ice-rink interior

    #music - ice skating

    show Poppie cheery

    Poppie "Don’t worry about it sir. Just be careful next time!"

    "Skater" "Of course, ma’am."

    "The skater skated away."

    #scene ice-rink interior
    #with fade

label choices7_b:

label choices7_common:





    show beach sunset
    
    call screen the_big_question()

    return
