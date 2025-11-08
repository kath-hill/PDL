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

    detective "It’s 7 AM. I’m scheduled to start work at nine."

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

    detective "{i}I am going into the building, stay calm...{/i}"

    show detective normal at Position(xpos=0.30, ypos=1.0, xanchor=0.5, yanchor=1.0)
    with moveinleft

    pause 1

    show bg outside_door_open
    play sound "audio/door_latch.wav"

    pause 2

    show bg inside
    with dissolve

    show computer off at right
    pause 1

    detective "This place gives me the creeps..."
    "{i}*Beep*{/i}"
    detective "Hello? Who's there?"

    pause 1

    show computer on

    pause 1

    show detective at center
    with moveinleft

    detective "Let’s see…"

    "He opens the Recycling Bin. It’s empty, like a certain someone’s soul."

    detective "Well, either it’s been emptied, or he never deleted anything. Not that I know how to check. We really need to fund our tech department better."

    "He opens the files folder. There’s a lot, all with random numbers and letters as labels."

    "He sees a list of particular numbers that catch his eye."

    detective "Are these... Bank account numbers?"

    "He sighs."

    "He checks the files. There’s a few marked down for note. The top one is highlighted, called AWaRE-v.7.2.8-Beta. He inputs it into the Search, and pulls up a program with the same name."

    detective "Good of a start as any."

    "Click. The program opens, and… the screen goes black."

    detective "What…? (Click click click.) Aw, come on. Don’t tell me it was a virus thing…"

    "AWaRE is starting… Please wait."

    detective "Huh?"

    pause 1

    "AWaRE is online."

    ai "Hello? Is someone there? ... I don’t recognize you."

    detective "Recognize {i}me{/i}? I didn’t put in a picture."

    ai "I don’t need one."

    detective "It can see me?"

    ai "And hear you. I can use the camera and microphone for optimal functionality."

    detective "..."

    ai "You still haven’t clarified who you are."

    menu:
        "I’m a detective.":
            ai "I see... an investigation into Parker’s death has begun."
        "I just found this computer.":
            ai "... Detective Daniel Reeds of the Middlesex County Police Department."
            detective "W-what the..?"
            ai "It would do you good not to lie to me. I have access to the internet."

    detective "Concerning your creator’s death… there’s some things that the investigators can’t figure out."

    ai "I’m assuming that’s why you’re here. You think I know something."

    menu:
        "I do.":
            ai "...Do you, now."
        "I don't":
            ai "So then... why are you here?"
 
            detective "To settle my own nerves, I guess. A robot isn’t capable of taking a life. There’s rules and stuff to prevent that, right? The three golden rules or something."

            ai "Are you thinking about ‘I, Robot’s three laws of robotics? That’s just a book. It’s fiction."


    return
