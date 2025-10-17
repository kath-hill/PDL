define detective = Character("Detective")
define ai = Character("AI")

image detective normal = "detective_normal.png"
image ai normal = "ai_normal.png"

label setup_scene:
    scene bg outside
    show detective normal at right
    show ai normal at left

    return

label starting_cutscene:
    $ renpy.movie_cutscene("cutscenes/starting_cutscene.webm . , ,m m  ,m")


label start:
    call setup_scene

    "You see a mysterious stranger in the cafe."

    menu:
        "Greet them":
            "You wave and say hi."
            "They smile back at you. Nice start!"

        "Ignore them":
            "You look away and sip your coffee."
            "They look a little sad you ignored them."
    return
