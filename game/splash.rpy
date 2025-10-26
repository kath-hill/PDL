image logo = "images/logo.png"


label splashscreen:
    scene black with fade

    # Show logo and give it a displayable name
    show logo at truecenter
    with dissolve
    play sound "audio/splash_tone.wav"

    pause 4.0

    # Hide the logo properly
    hide logo
    with fade

    pause 1.0

    return
