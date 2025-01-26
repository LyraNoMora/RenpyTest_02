﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("Protagonist", color="#C47A2A", window_background=Image("gui/textbox_player.png", xalign=0.5, yalign=1.0))
define Poppie = Character("Poppie", color="#E550BF", window_background=Image("gui/textbox_poppie.png", xalign=0.5, yalign=1.0))
define g = Character("Girl", color="#E550BF", window_background=Image("gui/textbox_poppie.png", xalign=0.5, yalign=1.0))
define a = Character("Poppie", color="#E550BF", window_background=Image("gui/textbox_poppie.png", xalign=0.5, yalign=1.0))
define s = Character("Poppie", color="#E550BF", window_background=Image("gui/textbox_poppie.png", xalign=0.5, yalign=1.0))

# Define images

layeredimage Poppie:

    always:
        "poppi_base"

    group face auto:
        attribute neutral default:
            "poppi_neutral"
        attribute sad:
            "poppi_sad"
        attribute smile:
            "poppi_smile"
        attribute surprised:
            "poppi_surprised"
        attribute cheery:
            "poppi_cheery"
        attribute calm:
            "poppi_calm"
        attribute cry:
            "poppi_cry"
        attribute serious:
            "poppi_serious"


layeredimage a:

    always:
        "poppi_mature_base"

    group face auto:
        attribute neutral default:
            "poppi_mature_neutral"
        attribute sad:
            "poppi_mature_sad"

layeredimage s:

    always:
        "poppi_side_base"

    group face auto:
        attribute neutral default:
            "poppi_side_neutral"
        attribute sad:
            "poppi_side_sad"

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

    show s neutral

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
    Poppie "Good choice! We’ll get two of that!"
    $ relationship += 1
    jump choices2_common

label choices2_b:
    Poppie "Alright, we’ll get two of that!"
    jump choices2_common

label choices2_c:
    Poppie "Right then, we’ll get two of that!"
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

    "*CRASH*" with vpunch

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
    "Get outta’ my way!":
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

    #music - Poppie's Theme

    Poppie "Sorry that you got hurt. This never would have happened if I hadn’t asked you to come here."

    p "Don’t worry, I’m not all that hurt. It’s not your fault, anyways, it was an accident."

    Poppie "..."

    show Poppie

    Poppie "..."

    Poppie "Way to keep your cool back there."

    p "What do you mean?"

    Poppie "You could’ve yelled at that skater, or made a scene. It was a tense situation, afterall."

    p "Like I said, it was an accident, and mistakes happen."

    Poppie "I know. I just think you handled it well. I wasn’t sure how you would react after you tensed up."

    p "Hah, am I that much of an open book?"

    show Poppie smile

    Poppie "A little."

    p "...Heh."

    "I couldn’t help but make a faint smile at the revelation."

    jump choices7_common

label choices7_b:
    "...!"

    "The right words can’t seem to get out of my mouth."

    #scene ice-rink interior

    #music - ice skating

    show Poppie cheery

    Poppie "Don’t worry about it sir. Just be careful next time!"

    "Skater" "Of course, ma’am."

    "The skater skated away."

    show Poppie sad

    Poppie "..."

    #scene ice-rink interior
    #with fade

    #music - Poppie's Theme

    Poppie "Sorry that you fell over, it’s my fault that all this happened."

    p "Don’t worry about it, it’s not your fault at all."

    Poppie "..."

    show Poppie sad

    Poppie "You wanted to yell at them, didn't you?"

    p "You could tell?"

    Poppie "It was written all over your face."

    "I let out a quiet sigh."

    p "Am I that much of an open book?"

    show Poppie smile

    Poppie "A little."

    p "..."

    Poppie "I would probably wanna give that guy a piece of my mind too if I was you!"

    "I couldn’t help but make a faint smile at her response."

    jump choices7_common

label choices7_common:
    #music - afternoon

    scene beach sunset
    with fade

    "The two of us walk back to the beach together."

    show Poppie

    Poppie "Well, that was a wild experience today!"

    p "I’ll say."

    show Poppie smile

    Poppie "I’m glad you gave learning how to ice skate a shot."

    show Poppie serious

    Poppie "I expect you to be able skate like a pro the next time I see you, okay?"

    p "Aye aye, captain."

    #music - none

    show Poppie

    Poppie "..."

    show Poppie surprised

    "*Stomach grumble*"

    Poppie "..."

    p "..."

    Poppie "Um..."

    p "Are you hungry?"

    Poppie "Maybe just a little bit."

    p "You can come over to my place for dinner if you want."

    show Poppie sad

    Poppie "Is that okay with you?"

    p "Yeah, my place is pretty close by."

    show Poppie

    Poppie "Alright, lead the way!"

    #music - Poppie's Theme

    #scene apartment night
    #with fade

    "The two of us arrived back at my apartment."

    "As soon as I flicked the lights on, Poppie started wandering around, observing everything I owned."

    show Poppie

    Poppie "Wow, you said your house was nearby, but I wasn’t expecting it to be this close!"

    Poppie "Guess you have no excuse for being late on the first day, huh?"

    p "Hey!"

    #scene apartment night
    #with fade

    "I bring out a pot to boil water."

    show Poppie

    Poppie "What are you making?"

    p "Instant noodles."

    show Poppie sad

    Poppie "Really?"

    p "What's wrong?"

    Poppie "Just feels rather bland."

    p "I will not let you sit there and insult instant noodles like that! They are God’s gift to humanity!"

    Poppie "...Right."

    Poppie "..."

    show Poppie

    Poppie "..."

    Poppie "Sit down, let me handle the cooking!"

    p "Are you sure? You are the guest after all."

    Poppie "Well, you’re hosting me, so it’s only fair that I cook."

    p "I fail to see how that evens out."

    show Poppie moveoutright

    "Ignoring my response, she begins cracking open my cabinets to see what I have."

    show Poppie serious

    Poppie "What is this?"

    p "Uncooked noodles."

    Poppie "Why didn't you want to eat this instead?"

    p "Because it’s uncooked."

    Poppie "..."

    p "...And there’s no flavor packet."

    show Poppie sad

    Poppie "You don’t know how to cook, do you?"

    p "..."

    show Poppie

    Poppie "That’s fine, I’ll teach you."

    p "..."

    #scene apartment night
    #with fade

    show Poppie

    Poppie "Well, first you grab a pot and pour some water in."

    Poppie "Next, you set the stove to high and let the water boil."

    p "..."

    Poppie "..."

    p "So, what do we do next?"

    Poppie "We just wait for it to boil."

    p "How do you know if it’s finished boiling?"

    show Poppie smile

    Poppie "Take a look for yourself!"

    "Poppie points to the water inside."

    "After seeing it, I faintly smile."

    show Poppie

    Poppie "That’s right, it’s our old friend: bubbles!"

    #scene apartment night
    #with fade

    show Poppie

    Poppie "And with that, you’re ready to serve!"

    p "That easy?"

    show Poppie smile

    Poppie "Yup!"

    p "Wow, if I had known it was that easy, I would have been making this everyday."

    Poppie "Just remember what I taught you, and you’ll be golden!"

    #scene apartment night
    #with fade

    show Poppie

    Poppie "Sooo full. That was a good meal, if I do say so myself."

    Poppie "Still think instant noodles are God's gift?"

    p "You’re gonna have to try harder if you want to change my mind on that."

    show Poppie smile

    Poppie "Heehee!"

    "I couldn’t help but laugh with her as well."

    show Poppie

    Poppie "Well, I should get going now."

    p "Now? But the night is still young, don’t you want to stay here a bit and hang out?"

    Poppie "I’ve had a lot of fun, and I want to stay, but..."

    Poppie "It will be harder to go if I stay, and I know I’ll have to leave eventually."

    show Poppie calm

    Poppie "After all, every bubble has to pop."

    #music - Poppie's Clouded
menu:
    "Wait, please stay!":
        jump choices8_common
    "Why are you leaving?":
        jump choices8_common
    "Did I do something wrong?":
        jump choices8_common
    "All good, no worries!":
        $ relationship += 1
        jump choices8_common

label choices8_common:
    p "..."

    #music - Poppie's Theme

    show Poppie smile

    Poppie "Well, I’ll see you around!"

    "With that, she headed out."

    "I watched her leave out the front door."

    "As it closed behind her, I saw her bubble bottle sitting on a shelf nearby."

    p "...Maybe next time."

    #fade to black

    #music - none

    "It’s 2AM, and I’m trying my hardest to sleep but I can’t."

    "I just can’t get Poppie out of my mind."

    "Maybe I should try calling her."

    "But would she even pick up?"

    "She might be asleep during this hour."

    "Whatever, I might as well give it a shot."

    "*CLICK*"

    "*BEEP*"

    "*BEEP*"

    "*BEEP*"

    p "..."

    "*CLICK*"

    p "Poppie? Hey, I-"

    "Automated Voice" "The prepaid phone customer you’re trying to reach is unavailable."

    "Prepaid phone?"

    #music - sorry

    "Wait, why would Poppie be using a prepaid phone?"

    p "Maybe I should visit her, and-"

    p "...!"

    "That’s when I realized."

    "I don’t know this person."

    "How’s that possible?"

    "It’s strange, we’ve hung out for two days straight,"

    "And despite only knowing each other for a short period of time, we’ve grown quite close."

    "Yet, it still feels distant."

    "I know nothing about Poppie. Not her residence, her family and friends, or any method of contact other than a prepaid phone number."

    "Is her name even Poppie?"

    p "..."

    "In the end, I was left with only one option."

    p "Poppie..."

    #fade to black

    scene beach day
    with fade

    "I woke up the next day, and immediately went to the beach."

    "I’m not sure why. It’s not like she invited me again."

    "I guess this felt like the only way to see her again."

    p "..."

    "And so I waited."

    scene beach day
    with fade

    "I hear a neighborhood dog barking from afar."

    "I wonder what it’s barking at."

    scene beach day
    with fade

    "An ambulance drives by."

    "They seem to be in a hurry, there must be an emergency somewhere."

    scene beach day
    with fade

    "Two kids run around on the beach together. One of them trips and falls into the sand."

    "Usually I’d laugh at that, but I don’t seem to have the willpower to do so."

    scene beach day
    with fade

    "When was the last time I ate?"

    "I feel like I should be hungry for standing here for so long."

    "Yet I can’t get myself to budge from this spot."

    scene beach day
    with fade

    "Some seagulls fly by."

    "They’re all flying in parallel to each other."

    "They certainly do look pretty together."

    scene beach sunset
    with fade

    #music - none

    "I keep waiting, and waiting, but there’s no sign of Poppie anywhere."

    #music - Poppie's Theme

    Poppie "..."

    Poppie "Hey, whatcha doin? You’ve been standing there for quite a while."

    p "Poppie!"

    show Poppie surprised

    Poppie "Y-yes?!"

    p "Oh thank god, I’m so happy to see you!"

    Poppie "Oh?! Why, what’s up?"

    p "Forget about it, I’m just overjoyed that you’re here!"

    Poppie "O-okay?"

    "Poppie looks rather flustered to see me right now."

    "Who would blame her? I look like an insane person right now."

    "During my excitement, I noticed something in her hand."

    p "Oh, what’s that you got there?"

    show Poppie

    Poppie "This is a bubble gun!"

    p "A bubble... gun?"

    show Poppie cheery

    Poppie "Yup, it automatically blows bubbles with a push of a button!"

    Poppie "Certainly more convenient than blowing it yourself, that’s for sure!"

    show Poppie smile

    Poppie "Wanna test it out?"

    p "You bet!"

    #fade to black

    scene beach sunset

    "The two of us mess around with the bubble gun for a while."

    "Minutes passed, possibly even hours, but I didn’t care, I was having the time of my life."

    show Poppie sad

    Poppie "Aw..."

    p "What’s wrong? Why’d you stop the bubbles?"

    Poppie "The bubble gun’s out of soap."

    p "You know, there are other ways to make bubbles."

    show Poppie surprised

    Poppie "What? How?"

    p "Give me a second."

    "I immediately dash to a nearby corner store to pick something up."

    scene beach sunset
    with fade

    show Poppie sad

    p "We'll use this."

    "I hand Poppie a packet."

    Poppie "What is this?"

    p "Bubble gum."

    Poppie "It says \“Hubba Bubba\” on it."

    p "Just take one and pop it in your mouth."

    Poppie "Alright."

    show Poppie serious

    "Poppie took one and observed it for a bit."

    p "What’re you waiting for? It’s not gonna poison you or anything."

    "After hearing me, Poppie immediately shoved it in her mouth."

    show Poppie

    Poppie "So how are we going to make bubbles with Hubba Bubba?"

    p "Like this."

    show Poppie surprised

    "*POP*"

    Poppie "Woah! How did you do that?"
menu:
    "You can just flatten it on your tongue, and blow.":
        jump choices3_common
    "Latch it to the tip of your tongue, then blow on it.":
        jump choices3_common
    "Just YOLO it.":
        jump choices3_common

label choices3_common:
    show Poppie smile
    
    Poppie "Okay, I’ll try!"

    show Poppie serious

    "Poppie tries to blow as hard as possible."

    "Suddenly the gum shoots out of her mouth."

    show Poppie surprised

    Poppie "...!"

    "And her gum landed on my face."

    p "..."

    Poppie "..."

    p "Maybe that’s enough bubble blowing for today."

    show Poppie cheery

    "We both fall into a fit of laughter."

    scene beach sunset
    with fade

    #music afternoon

    show Poppie

    Poppie "Can I ask you a question?"

    p "I assume you’re not gonna take “no” for an answer?"

    show Poppie cheery

    Poppie "Heehee!"

    show Poppie

    Poppie "..."

    Poppie "Why are you so afraid to talk to people?"

    p "..."

    Poppie "I noticed this when you talked to the boba shop clerk, and when that guy at the ice skating rink ran into you."

    p "..."

    p "I guess I’m just worried about how people will judge me."

    Poppie "..."

    show s

    s "Hmph."

    p "...?"

    s "I’m not a confident person myself too, you know?"

    p "You? But you’re so-"

    s "\“Outgoing\”? Please, if only."

    s "I’m afraid of what people think of me too."

    s "Do you know how much courage it took for me to ask you if you wanted to hang out again when we first met?"

    p "..."

    show Poppie calm

    Poppie "I was so afraid at the time that you’d say \“No.\”"

    p "..."

    Poppie "Even now, I’m worried about what you think of me."

    p "That’s not-! You shouldn’t, I-!"

    show s sad

    Poppie "Are you disappointed that I’m not the person you thought I was?"

    p "..."

    Poppie "..."

    p "Can I say something?"

    show Poppie calm
    
    call screen the_big_question()

    Poppie "..."

    #music - sorry

    show Poppie sad

    Poppie "I'm sorry."

    Poppie "Forgive me, but there’s something else I didn’t reveal about myself."

    Poppie "I don’t live here."

    p "...!"

    show s

    Poppie "My family lives far away. I only moved here to take care of my aunt."

    show Poppie sad

    Poppie "..."

    Poppie "She died three days ago."

    p "Poppie… I’m so sorry."

    show s sad

    Poppie "That’s when I decided that I need to get my mind off it by going outside. I found that bubble bottle in her house."

    Poppie "When I was young, we used to play with bubbles when I would visit her. I thought if I tried it then, it might help me."

    Poppie "It didn’t help."

    show Poppie calm

    Poppie "..."

    Poppie "Just when I was about to give up hope."

    Poppie "I met you."

    Poppie "You gave me the break I needed."

    Poppie "Someone you listened to my weird ramblings."

    Poppie "Someone who took a chance on me."

    Poppie "You..."

    Poppie "You saved me."

    show s neutral

    Poppie "..."

    Poppie "I wish I could stay here with you."

    Poppie "We could’ve had fun skating together."

    Poppie "Learned how to cook new meals."

    Poppie "And play with bubbles till the sun sets."

    Poppie "But I knew from the beginning that my time here wouldn’t last forever."

    Poppie "This happiness..."

    Poppie "Someday, it would pop."

    Poppie "..."

    p "..."

    p "Is there anything I could do to make you stay?"

    show Poppie calm

    Poppie "I’m so sorry, but my flight leaves tonight."

    p "..."

    show Poppie sad

    Poppie "..."

    show Poppie looking away sad

    Poppie "Please, don’t show up at the airport tonight."

    Poppie "I can’t stand the thought of having to say goodbye to another person I care about."

    p "..."

    #fade to black

    if relationship = 0 or relationship = 1:
        jump Bad_End
    if relationship = 2 or relationship = 3:
        jump Neutral_End
    else:
        jump Good_End

label Bad_End:
    #music - never again
    "And that’s the last I heard from her."

    "I still have that bottle of bubbles she gave me all those years ago."

    "When I’m sad, I take it out and blow a few bubbles just to watch them pop and vanish."

    "Just like her."

    "I’m not sure where she is or how she’s doing."

    "But wherever she is..."

    "I hope she’s happy."
    return

label Neutral_End:
    jump Bad_End

label Good_End:
    #music - never again
    "Against her wishes, I went to the airport that night."

    "I can’t let it end like this."

    "What was all this for?"

    "What about those sleepless nights where she consumed my thoughts?"

    "I saw her bubbles for a reason, I met her for a reason!"

    "I had to see her one last time."

    scene Airport
    "Please be here, please be here."

    "I have to find her."

    scene Airport
    with fade

    "I began running around all over the place, trying to find Poppie."

    scene Airport
    with fade

    "Each and every nook and cranny, I had searched."

    scene Airport
    with fade

    "Nothing, there’s no sign of her."

    "Then, an idea pops into my mind."

    #music - joy

    "I shove my hand in my pocket and pull out the bubble bottle she gave me on the first day."

    "I pull the wand out and blow into it, creating a flurry of bubbles."

    "The people around me give me strange looks."

    "I know they think I’m weird, or child-like, but I don’t care."

    "I need her to see."

    scene Airport
    with fade

    show Poppie sad
    Poppie "..."

    Poppie "Huh? Bubbles?"

    Poppie "What... Where are you coming from?"

    scene Airport
    with fade

    "A short while later, I hear a trail of footsteps approaching."

    p "...!"

    show Poppie calm

    Poppie "You showed up, even after I told you not to."

    p "I know, I’m sorry Poppie, I just couldn’t-"

    show Poppie cry

    Poppie "I’m so overjoyed right now."

    Poppie "..."

    Poppie "I’m just so happy to see you, even if it’s just one last time."

    p "..."

    p "Please, stay."

    Poppie "..."

    Poppie "I can't."

    p "My every day was the same."

    p "I thought I liked my routine, I felt safe in the mundane."

    p "I never wanted anything to change."

    p "Until I met you."

    show Poppie smile

    p "I didn’t save you, Poppie."

    Poppie "..."

    p "You saved me."

    Poppie "..."

    p "..."

    Poppie "I promise I won’t ever forget you, or all of those fond memories we made together."

    Poppie "..."

    Poppie "I hope you’ll remember me."

    #fade to black

    "And that was it."

    "Poppie got on her plane, and flew away."

    "..."

    #music - leaving
    #show apartment
    "With Poppie gone, life returned to normal."

    scene downtown day
    "Sure, my life went on, but there was barely anything exciting happening."

    #fade to black

    "And over the years, my memories of Poppie started to slowly dissipate."

    "..."

    scene restaurant day
    p "Two Bubble Teas, please."

    "Clerk" "Right away!"

    #fade to black

    "Clerk" "Here you go!"

    p "Thank you."

    scene downtown day
    with dissolve

    "I bought two bubble teas."

    "I’m not sure why. It’s not like it was ever my favorite drink."

    "And why two? I can barely finish one."

    "Whatever, maybe I’ll just store it in my fridge and save it for the next day."

    scene beach sunset
    with dissolve

    "Left at the intersection, three blocks down, right at the corner store, and then I’m home."

    "I like it when things stay the same. Routines are predictable, dependable."

    "As I continue down the road, something catches my eye."

    #music - none 

    #a bubble flies by the screen

    p "...!"

    p "A bubble?"

    "That’s new. Where are those bubbles coming from?"

    "I follow the trail and see the source of the floating chaos:"

    #music - reunion

    show s

    g "..."

    #shake screen

    p "Are- Are you-?"

    "I can’t believe what I’m looking at."

    scene beach sunset
    with fade

    "I rub my eyes, in disbelief at what I’m seeing."

    Poppie "Hm?"

    show a sad

    a "..."

    "There she is, staring right back at me."

    p "..."

    p "Poppie..."

    Poppie "..."

    show a calm

    "Upon hearing my voice, her frown turns to a warm, cheerful smile."

    Poppie "I missed you."

    p "Welcome back."

    #fade to black

    #music - ice skating

    $ persistent.got_best_ending = True

    return


