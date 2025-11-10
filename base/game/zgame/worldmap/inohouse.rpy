label inohouse:
    $ playmusic("/audio/ost/market.opus", volume=0.7)
    call hidemarketUI from _call_hidemarketUI_11
    if day_part == 0 or day_part == 1 or day_part == 2:
        scene black
        scene inohouse day with dissolve
    else:
        scene black
        scene inohouse night with dissolve
    hide screen housemap
    call hideUI from _call_hideUI_60
    bot"Considering what happened, I should probably stay away from here for a while..."
    show screen topleftbuttons
    $ ui.interact()
 