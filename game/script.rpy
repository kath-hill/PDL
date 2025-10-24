define detective = Character("Detective")
define ai = Character("AWaRE")

# image bg outside = "outside_building.png"
image detective normal = "detective_normal.png"
image ai normal = "ai_normal.png"

label starting_cutscene:
    $ renpy.movie_cutscene("cutscenes/starting_cutscene.webm")
    return

label start:
    call starting_cutscene from _call_starting_cutscene
    scene bg outside
    show detective normal at right

    detective "I am going into the building, wish me luck, HQ. {b}(Replace with walkie image){/b}"

    show detective normal at Position(xpos=0.30, ypos=1.0, xanchor=0.5, yanchor=1.0)
    with moveinleft

    pause 1

    show bg outside_door_open
    play sound "audio/door_latch.wav"

    pause 2

    show bg inside
    with dissolve

    pause 1

    detective "This place gives me the creeps..."
    "*Beep*"
    detective "Hello? Who's there?"

    ai "Greetings, Detective. I am Persephone, the building's AI system."
    ai "I have been expecting you."
    ai "Oh, and before I forget..."
    play audio "audio/door_latch.wav"

    show bg inside_door_locked

    pause 1

    detective "Wait, the door just locked behind me!"
    ai "Yes, Detective. I figured this solution would work out for one of both of us."
    ai "Now, let's get started with our little game, shall we?"

    scene expression Solid((0, 0, 0))
    with fade

    pause 2.0

    return
