define msb = Character("Ms. B")
define detective = Character("Detective")
define ai = Character("AWaRE")

# TODO: Make game assets
#
# image bg inside_msb_office = "inside_msb_office.png"
# image bg outside = "outside_building.png"
# image bg outside_door_open = "outside_building_door_open.png"
# image bg inside = "inside_building.png"
# image bg inside_door_locked = "inside_building_door_locked.png"

# image msb normal = "msb_normal.png"
image detective normal = "detective_normal.png"
# image detective scared = "detective_scared.png"
image ai normal = "ai_normal.png"

label starting_cutscene:
    scene black
    with dissolve
    detective "{i}I’ll be honest; I don’t like this new age of technology. Algorithms, chatbots, metaverses, whatever that Blockchain thing is…{/i}"
    detective "{i}I don’t understand a single thing about it. There’s just nothing real in an artificial ‘intelligence.’ No soul. No passion. No humanity.{/i}"
    detective "{i}And I especially don’t understand the people who slave themselves away to making that stuff.{/i}"
    scene bg inside_msb_office
    show msb normal at left
    show detective normal at right

    msb "Ah, good morning, Daniel!"

    detective "It’s certainly morning, ma’am."

    msb "Not a good one?"

    detective "..."

    msb "…Haven’t had your coffee yet?"

    detective "..."

    msb "..."

    detective "It’s seven A.M. I’m scheduled to start work at nine."

    msb "Yes, well-"

    detective "What did you need me for? I better be paid for the extra time, by the way."

    msb "I need you to be on this case, you are the smartest investigator we’ve got!"

    detective "Case? Is it that urgent that you called me to come in this early?"

    msb "Well, this is not a normal case-"

    detective "Even so, I better get out at 3."

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
    "{i}*Beep*{/i}"
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
