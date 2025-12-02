image logo = "images/logo.png" # TODO: Replace with actual logo image

label splashscreen:
    scene black
    with fade

    # Show logo and give it a displayable name
    show logo at truecenter
    with dissolve
    play sound "audio/splash_tone.wav"

    # Unskippable pause
    $ renpy.pause(4.0, hard=True)

    # Hide the logo
    hide logo
    with fade

    # Short unskippable delay before continuing
    $ renpy.pause(1.0, hard=True)

    return
