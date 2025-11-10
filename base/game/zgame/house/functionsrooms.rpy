# way to hide bottom right buttons
label hideButtons:
    hide screen borutobedroombuttonstutorial
    hide screen borutobedroombuttons
    hide screen himawaribedroombuttons
    hide screen hinatabedroombuttons
    hide screen livingroombuttons
    hide screen laundryroombuttons
    hide screen kitchenbuttons
    hide screen bathroombuttons
    hide screen bohim_1_screen
    hide screen actionbuttonshouse
    hide screen tooltip
    return

label hideUI:
    call hideButtons from _call_hideButtons_1
    hide screen marketnightmap
    hide screen marketmap
    hide screen workmenutopright
    hide screen infirmarymenutopright
    hide screen gymmenutopright

    hide text
    hide screen housemap
    hide screen topleftbuttons
    hide screen displayTextScreen_advancetime
    hide screen bohim_1_screen
    hide screen scrollingtext
    hide screen tooltip

    # Some additions
    hide screen marketreturn
    hide screen returnbutton
    return



label hideEventScreens:
    #room/event screens (ADD EVERY EVENT SCREEN HERE)
    hide screen hinata_bedroom_day1
    hide screen v1_night_massage_screen
    hide screen himawari_stretching_talk
    hide screen kitchen_hinata_day
    hide screen v1_laundry_hinata
    return

label showUIhouse:
    show screen housemap
    show screen topleftbuttons
    show screen actionbuttonshouse
    return

label resetbuttons:
    $ talkbutton = False
    $ actionbutton = False
    $ strengthbutton = False
    $ infobutton = "inactive"
    hide screen tooltip
    return
label enabletalk:
    $ talkbutton = True
    $ infobutton = "shown"
    return
label enableaction:
    $ actionbutton = True
    $ infobutton = "shown"
    return

label enablestrength:
    $ strengthbutton = True
    $ infobutton = "shown"
    return

label enableinfo:
    $ infobutton = "active"
    return




#room actions
label borutobedroomActions():
    call hideUI from _call_hideUI_40
    if day_part == 1:
        jump bedroom_boruto_morning
    elif day_part == 2:
        jump bedroom_boruto_evening
    elif day_part == 3 or day_part ==4:
        jump bedroom_boruto_night


label hinatabedroomActions():
    call hideUI from _call_hideUI_41
    if day_part == 1:
        jump bedroom_hinata_morning
    elif day_part == 2:
        jump bedroom_hinata_evening
    elif day_part == 3 or day_part ==4:
        jump bedroom_hinata_night

label himawaribedroomActions():
    call hideUI from _call_hideUI_42
    if day_part == 1:
        jump bedroom_himawari_morning
    elif day_part == 2:
        jump bedroom_himawari_evening
    elif day_part == 3 or day_part ==4:
        jump bedroom_himawari_night


label bathroomActions():
    call hideUI from _call_hideUI_43
    if day_part == 1:
        jump bathroom_morning
    elif day_part == 2:
        jump bathroom_evening
    elif day_part == 3 or day_part ==4:
        jump bathroom_night


label livingroomActions():
    call hideUI from _call_hideUI_44
    if day_part == 1:
        jump livingroom_morning
    elif day_part == 2:
        jump livingroom_evening
    elif day_part == 3 or day_part ==4:
        jump livingroom_night



label laundryroomActions():
    call hideUI from _call_hideUI_45
    if day_part == 1:
        jump laundryroom_morning
    elif day_part == 2:
        jump laundryroom_evening
    elif day_part == 3 or day_part ==4:
        jump laundryroom_night


label kitchenActions():
    call hideUI from _call_hideUI_46
    if day_part == 1:
        jump kitchen_morning
    elif day_part == 2:
        jump kitchen_evening
    elif day_part == 3 or day_part ==4:
        jump kitchen_night