
default sakura_relationship = 0
default sarada_relationship = 0

label uchihahousehold:
    $ playmusic("/audio/ost/market.opus", volume=0.7)
    call hidemarketUI from _call_hidemarketUI_12
    if day_part == 0 or day_part == 1 or day_part == 2:
        scene black
        scene inohouse day with dissolve

    elif day_part == 4:
        scene black
        scene inohouse night with dissolve
        if sakura_asked_for_wine == True:
            $ wine_in_inventory = inventory.find_item_by_name("Wine")
            if wine_in_inventory!= None:
                bot"I got the wine Auntie Sakura asked for. Shall I try knocking on the door at this time?"
                menu:
                    bot"I got the wine Auntie Sakura asked for. Shall I try knocking on the door at this time?"
                    "Knock on the door":
                        jump sakura_wine_date
                    "M-maybe later...":
                        show screen topleftbuttons
                        $ ui.interact()
        else:
            bot"There's nothing to do here at this time... I think?"
            "Perhaps Sakura would allow you to visit during midnight if you improved your relationship with her!"
            show screen topleftbuttons
            $ ui.interact()
    else:
        scene black
        scene inohouse night with dissolve
    hide screen housemap
    call hideUI from _call_hideUI_62
    if uchihas_visited == True:
        bot"I've already visited today. Would be weird to show up again so soon..."
        if sakura_asked_for_wine == True:
            bot"Although Auntie Sakura did ask me to bring some wine and visit her during midnight!"
        show screen topleftbuttons
        $ ui.interact()
    else:
        pass
    bot"Shall I pay them a visit?"
    menu:
        bot"Shall I pay them a visit?"
        "Knock on the door":        
            jump visituchihas_label
        "Leave":
            pass
        
    show screen topleftbuttons
    $ ui.interact()