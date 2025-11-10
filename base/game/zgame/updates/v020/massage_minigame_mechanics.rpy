# DEFAULTS

default satisfactionpercentage = 0
# These are not strictly needed as label arguments but are kept to maintain your structure
default addsatisfaction = 0
default subtractsatisfaction = 0

# SCREENS

image animated_heart_icon:
    # The base image file
    "v20/madame/massage_gui/heart_icon.webp"
    # The static size you want
    xysize (50, 50)
    # The ATL block for the animation
    block:
        # Over 0.7 seconds, SMOOTHLY do ALL of these at once:
        # - Zoom in to 120%
        # - Fade out to 70% opacity
        linear 0.7 zoom 1.2 alpha 0.7 subpixel True

        # Over the next 0.7 seconds, SMOOTHLY do ALL of these at once:
        # - Zoom back to normal size
        # - Fade back in to full opacity
        linear 0.7 zoom 1.0 alpha 1.0 subpixel True

        repeat

screen massage_stage_display():
    zorder 1
    # A simple frame to give the text a background and make it readable
    frame:
        # Position it at the top right corner with a small margin
        xalign 1.0
        yalign 0.0
        xmargin 20
        ymargin 20
        
        # Add some padding inside the frame
        padding (10, 5)

        # The text itself, which will automatically update when massage_stage changes
        text "Stage [massage_stage] of 5"

screen massagebar():
    # This is the container for the BAR AND THE ICON.
    # It has the exact position and size of your bar ELEMENT.
    zorder 1
    fixed:
        xysize (445, 350)
        yalign 0.52
        xalign 0.04

        # 1. The VBAR, filling the container.
        vbar:
            top_bar "v20/madame/massage_gui/bar_empty.webp"
            bottom_bar "v20/madame/massage_gui/bar_full.webp"
            value AnimatedValue(satisfactionpercentage, range=100, delay=1)
            xfill True
            yfill True

        # 2. The ICON, positioned with precise pixels.
        add "animated_heart_icon":
            ypos -5
            xpos 13
            anchor (0.5, 0.5)

    # 3. The TEXT, independent and correctly positioned relative to the screen.
    if satisfactionpercentage >= 100:
        text "Success!" xalign 0.02 yalign 0.2
    elif satisfactionpercentage <= 0:
        text "Failure!" xalign 0.02 yalign 0.2
    else:
        text "[satisfactionpercentage]%" xalign 0.02 yalign 0.2

# screen dimming overlay
image halfblackmassagebar = "#00000088"

# FUNCTIONS

label increasesatisfaction(addsatisfaction):
    show halfblackmassagebar zorder 100000 with dissolve
    show screen massagebar zorder 100001 with dissolve
    $ satisfactionpercentage = satisfactionpercentage + addsatisfaction
    if satisfactionpercentage > 100:
        $ satisfactionpercentage = 100
    pause 1
    hide halfblackmassagebar with dissolve
    hide screen massagebar with dissolve
    $ addsatisfaction = 0
    return

label decreasesatisfaction(subtractsatisfaction):
    show halfblackmassagebar zorder 100000 with dissolve
    show screen massagebar zorder 100001 with dissolve
    $ satisfactionpercentage = satisfactionpercentage - subtractsatisfaction
    if satisfactionpercentage < 0:
        $ satisfactionpercentage = 0
    pause 1
    hide halfblackmassagebar with dissolve
    hide screen massagebar with dissolve
    $ subtractsatisfaction = 0
    return