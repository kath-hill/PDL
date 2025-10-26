define detective = Character("Detective")
define ai = Character("AWaRE")

# TODO: Make game assets
#
# image bg outside = "outside_building.png"
# image bg outside_door_open = "outside_building_door_open.png"
# image bg inside = "inside_building.png"
# image bg inside_door_locked = "inside_building_door_locked.png"

# image detective scared = "detective_scared.png"
image detective normal = "detective_normal.png"
image ai normal = "ai_normal.png"

label starting_cutscene:
    scene black
    detective "{i}I’ll be honest; I don’t like this new age of technology. Algorithms, chatbots, metaverses, whatever that Blockchain thing is…{/i}"
    detective "{i}I don’t understand a single thing about it. There’s just nothing real in an artificial ‘intelligence.’ No soul. No passion. No humanity.{/i}"
    detective "{i}And I especially don’t understand the people who slave themselves away to making that stuff.{/i}"

    return

label start:
    call starting_cutscene
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
    # show detective scared # TODO: Make detective scared
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

    scene black
    with fade

    pause 2.0

    return
