play sound "audio/splash_tone.wav" fadein 1.0

define detective = Character("Detective")

image detective normal = "detective_normal.png"

label start:
    scene bg room
    show detective normal

    detective "I am making a Ren'Py Game!"

    return
