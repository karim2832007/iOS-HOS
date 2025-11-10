



init:
    transform customzoom: #to resize imagebuttons with at customzoom
        zoom 0.7
    transform halfzoom: #to resize imagebuttons with at customzoom
        zoom 0.5

    transform mobile_scale: #used in some screens for mobile
        zoom 0.8


    #transitions
    transform fast_move_from_side(start_x, end_x, duration):
        xalign start_x yalign 0.5
        linear duration xalign end_x

    transform increasing_shake:
        function renpy.curry(gradualshake)(t=0, duration=60.0, max_intensity=50)
        repeat


    transform endcreen_text:
        blur 50
        alpha 0.0
        linear 1 blur 0 alpha 1.0
    transform endcreen_text2:
        blur 50
        alpha 0.0
        zoom 2.0
        linear 2 blur 25 alpha 0.75 zoom 1.2
        linear 0.5 blur 0 alpha 1.0 zoom 1.0
    
    transform atblur:
        blur 80
        xalign 1.0
        linear 4 blur 0

    transform brightreveal:
        blur 80
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(1.1)*HueMatrix(0.0) 
        linear 4 blur 0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)

    transform brightrevealzoom:
        blur 80 zoom 1.3
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(1.1)*HueMatrix(0.0) 
        easein 3.5 blur 0 zoom 1.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    
    transform dizzy:
        linear 1 blur 30 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.3)*HueMatrix(0.0)
        linear 3 blur 3 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
        linear 2 blur 60 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.3)*HueMatrix(0.0)
        linear 1 blur 10 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
        repeat

    transform dizzy2:
        
        linear 0.3 blur 50 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.2)*HueMatrix(0.0)
        linear 0.5 blur 20 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
        linear 0.5 blur 30 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.2)*HueMatrix(0.0)
        linear 0.3 blur 10 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
        repeat

    transform dizzyflash:
        linear 0.7 blur 30 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.3)*HueMatrix(0.0)
        linear 0.5 blur 3 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
        linear 1 blur 60 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.3)*HueMatrix(0.0)
        linear 1 blur 0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)

    transform dizzyflashshort:
        linear 0.6 blur 30 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.4)*HueMatrix(0.0)
        linear 0.3 blur 5 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
        linear 0.3 blur 20 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.2)*HueMatrix(0.0)
        linear 0.3 blur 0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)


        
    transform shake(rate=0.090):
        linear rate xoffset 2 yoffset -6
        linear rate xoffset -2.8 yoffset -2
        linear rate xoffset 2.8 yoffset -2
        linear rate xoffset -2 yoffset -6
        linear rate xoffset +0 yoffset +0
        repeat 4

    transform shakeforever(rate=0.090):
        linear rate xoffset 4 yoffset -6
        linear rate xoffset -5.8 yoffset -2
        linear rate xoffset 5.8 yoffset -2
        linear rate xoffset -5 yoffset -6
        linear rate xoffset +0 yoffset +0
        repeat
    
    transform smallshake(rate=0.090):
        linear rate xoffset 2 yoffset -2
        linear rate xoffset -2.8 yoffset -2
        linear rate xoffset 2.8 yoffset -2
        linear rate xoffset -2 yoffset -2
        linear rate xoffset +0 yoffset +0
        repeat 1

    transform pov_jerkoff(rate=0.15, repetitions=2):
        linear rate yoffset 5
        # linear rate yoffset 0
        linear rate yoffset 10
        linear rate yoffset 0
        repeat repetitions
    transform pov_jerkoffpullback(rate=0.1):
        linear rate yoffset 5
        # linear rate yoffset 0
        linear rate yoffset 10
        linear rate yoffset 0
        linear 0.5 yoffset 50
    transform pov_jerkoffthrust:
        linear 0.2 yoffset 0
        linear 0.1 yoffset 3
        linear 0.1 yoffset 0
        linear 0.1 yoffset 2
        linear 0.1 yoffset 0
        linear 0.1 yoffset 1
        linear 0.1 yoffset 0
        linear 0.1 yoffset 2
        linear 0.1 yoffset 0



    transform customzoom2: #to resize imagebuttons with at customzoom
        zoom 0.75

    transform customzoom3: #to resize imagebuttons with at customzoom
        zoom 0.6

    transform customzoomtopleftbuttons: #to resize imagebuttons with at customzoom
        zoom 0.80

    transform alpha0: #to resize imagebuttons with at customzoom
        alpha 0.0
    
    transform alpha1: #to resize imagebuttons with at customzoom
        alpha 1.0

    transform dissolvehack:
        alpha 0.0
        linear 0.5 alpha 1.0
    transform wakeup:
        "/transitions/eyeclosed.png"
        .3
        "/transitions/eyefullopen.png" 
        .3
        "/transitions/eyehalfopen.png"
        alpha 1
    
    screen displayTextScreen_advancetime():
        zorder 1000
        default displayText_stats_advancetime = _("Advance time")
        frame:
            background "#0008"  # Semi-transparent background
            padding (10, 10)
            align (0.5, 0.75)  # Adjust the alignment as needed
            if day_part == 4:
                text "During midnight, sleep to advance time":
                    size 20
                    color "#fff"
            else:
                text _(displayText_stats_advancetime):
                    size 20
                    color "#fff"


image ctc_arrowblink:
    xoffset 9
    yoffset 4
    "gui/ctc_arrow.png"
    linear 0.65 alpha 0.8
    linear 0.6 alpha 0.1
    pause .05
    repeat

label splashscreen:
    $ check_language_installation_status()
    scene black
    play sound "soun_fx/ominous_sound.opus" volume 0.5
    show disclameimerintro with Fade(0.3,0,2):
        zoom 2.0 xalign 0.6 yalign 0.3
    show disclameimerintro:
        easeout 15 subpixel True zoom 1.5 xalign 0.492 yalign 0.3
    show screen splash with Dissolve(1)
    pause 4

    hide screen splash with dissolve
    pause 1
    scene black with dissolve

    pause 0.5

    return

screen splash():
    # First line: title + version number
    # Second line: "Modded by Gaming Mods" in gold, bold, italic
    text ("House of Shinobi " 
          + config.version.split("Modded by Gaming Mods")[0].strip()
          + "\n{color=#FFD700}{b}{i}Modded by Gaming Mods{/i}{/b}{/color}"):
        xalign 0.5
        yalign 0.0
        yoffset 150
        size 60
        text_align 0.5  # centers both lines

    text _("By Cutepercentage"):
        xalign .5
        yalign 0.0
        yoffset 300
        size 40
        xmaximum 600
        text_align 0.5
        color "#fff"

    add "gui/splashdisclaimer.webp" xalign .5 yalign 0.95 zoom 1.0

#-------------------------------------------------------------------------------------
default percentage = 0
label blink(t1,t2,t3):
    show fullblack
    show eyehalfopen
    hide fullblack with dissolve
    hide eyeclosed with dissolve
    bot"[t1]"
    pause 0.2
    show eyeclosed with dissolve
    bot"[t2]"
    show eyefullopen
    hide eyeclosed with dissolve
    pause .2
    
    hide eyehalfopen with dissolve
    bot"[t3]"
    hide eyefullopen with dissolve
    return

screen lustbar():
    vbar:
        value AnimatedValue(percentage, range=100, delay= 1)
        left_bar "gui/bar/top.png"
        right_bar "gui/bar/bottom.png"
        xysize (445,350)
        yalign 0.52 xalign 0.04 xfill True
    if percentage > 100:
        text "max" xalign 0.02 yalign 0.2
    elif percentage < 0:
        text "empty" xalign 0.02 yalign 0.2
    else:
        text "[percentage]%" xalign 0.02 yalign 0.2





#lust bar----------------------------------------------------------------------------


#Top left buttons
screen topleftbuttons(): #bottom left transparent background
    zorder 2
    # Info Button
    if showrelationships == True:
        imagebutton:
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            xpos 0
            ypos 0.02
            auto "ui/info_%s.png"
            hovered Show("displayTextScreen", displayText = "Show Relationships")
            unhovered Hide("displayTextScreen")
            action [Show("relationships")]

    #Map UI
    if completed_intro > 4 and showmapaftertutorial == True:
        imagebutton:
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            xpos 0.07
            ypos 0.034
            auto "/ui/map_button_%s.png"
            hovered Show("displayTextScreen", displayText = "Open Map")
            #hovered Show("displayTextScreen_map")
            unhovered Hide("displayTextScreen")
            action [Show("mapui")]
            at customzoomtopleftbuttons

    #Time UI
    if completed_intro > 4 and day_part != 4:
        imagebutton:
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            xpos 0.13
            ypos 0.034
            auto "/ui/wait_button_%s.png"
            hovered Show("displayTextScreen_advancetime")
            unhovered Hide("displayTextScreen_advancetime")
            action [SetVariable("boruto_clothes", "Casual"), Jump("action_taken")]
            at customzoomtopleftbuttons
    elif completed_intro > 4:
        imagebutton:
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            xpos 0.13
            ypos 0.034
            auto "ui/wait_button_%s.png"
            hovered Show("displayTextScreen_advancetime")
            unhovered Hide("displayTextScreen_advancetime")
            action If(boruto_location == "borutobedroom",
                    true=[SetVariable("boruto_clothes", "Casual"), Jump("borutobedroomactionmenu")],
                    false=[SetVariable("boruto_clothes", "Casual"), Jump("borutobedroom")])
            at customzoomtopleftbuttons
    
    #Journal
    if completed_intro > 5: 
        
        imagebutton:
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            xpos 0.19
            ypos 0.034
            auto "/ui/journal_button_%s.png"
            hovered Show("displayTextScreen", displayText = "Open Journal")
            unhovered Hide("displayTextScreen")
            action [Function(disable_rollback), Show("diary")]
            at customzoomtopleftbuttons

    #Inventory
    if completed_intro > 5:  
        frame:
            xpos 0.24 ypos 0
            xminimum 100
            yminimum 7
            background None
            text "$[money]" xalign 0.5 size 19
        imagebutton:
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            xpos 0.25
            ypos 0.034
            auto "/ui/inventory_button_%s.png"
            hovered Show("displayTextScreen", displayText = "Open Inventory")
            unhovered Hide("displayTextScreen")
            action [Function(disable_rollback), Show("inventoryScreen")] 
            at customzoomtopleftbuttons


#House map----------------------------------------------------------------------------
screen housemap(): #bottom left transparent background
    frame:
        background "#0008"
        padding (10, 10)
        align (1, 1.0)  # Adjust the alignment as needed
        xmaximum 385
        ymaximum 130

   
    #DAY INFORMATION
    frame:
        background "#0008"  # Semi-transparent background
        padding (10, 10)
        align (0.5, 0.0)  # Adjust the alignment as needed
        xmaximum 200
        ymaximum 60

        text "[day_name] [day_part_name]":
            align (0.5, 0.0)
            size 15
            color "#fff"
        text "Day [day_number]":
            align (0.5, 1.0)
            size 13

    #bedroom circle buttons
    if boruto_location == "hallway":
        imagebutton:
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            idle Transform("ui/icons/hallway_boruto.webp", alpha=0.8)
            hover "ui/icons/hallway_boruto.webp"
            focus_mask True
            hovered Show("displayTextScreen", displayText = "[bo_name]'s Bedroom")
            unhovered Hide("displayTextScreen")
            action [SetVariable("show_buttons", False), Function(move_to_room, "borutobedroom")]

        imagebutton:
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            if hin_location == "hinatabedroom":
                idle Transform("ui/icons/hallway_hinata.webp", alpha=0.8)
            else:
                idle Transform("ui/icons/hallway_hinata.webp", alpha=0.8,matrixcolor=SaturationMatrix(0))
            hover "ui/icons/hallway_hinata.webp"
            focus_mask True
            hovered Show("displayTextScreen", displayText = "[hin_name]'s Bedroom")
            unhovered Hide("displayTextScreen")
            action [SetVariable("show_buttons", False), Function(move_to_room, "hinatabedroom")]

        imagebutton:
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            if him_location == "himawaribedroom":
                idle Transform("ui/icons/hallway_himawari.webp", alpha=0.8)
            else:
                idle Transform("ui/icons/hallway_himawari.webp", alpha=0.8,matrixcolor=SaturationMatrix(0))
            hover "ui/icons/hallway_himawari.webp"
            focus_mask True
            hovered Show("displayTextScreen", displayText = "[him_name]'s Bedroom")
            unhovered Hide("displayTextScreen")
            action [SetVariable("show_buttons", False), Function(move_to_room, "himawaribedroom")]

    #event icons
    if hin_location == "himawaribedroom" or hin_location == "hinatabedroom" or hin_location == "borutobedroom" or him_location == "himawaribedroom" or him_location == "hinatabedroom" or him_location == "borutobedroom":
        add "ui/icons/green_dot.png" xpos 0.027 ypos 0.82 zoom 0.9

    if hin_location == "laundryroom" or him_location == "laundryroom":
        add "ui/icons/green_dot.png" xpos 0.083 ypos 0.82 zoom 0.9

    if hin_location == "livingroom" or him_location == "livingroom":
        add "ui/icons/green_dot.png" xpos 0.136 ypos 0.82 zoom 0.9

    if hin_location == "kitchen" or him_location == "kitchen":
        add "ui/icons/green_dot.png" xpos 0.193 ypos 0.82 zoom 0.9

    if hin_location == "bathroom" or him_location == "bathroom":
        add "ui/icons/green_dot.png" xpos 0.251 ypos 0.82 zoom 0.9


    #laundryroom
    imagebutton:
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus" 
        xpos 0.065
        ypos 0.85
        at customzoom
        auto "ui/icons/laundry_%s.png"
        action [Hide("displayTextScreen"), SetVariable("show_buttons", False), Function(move_to_room, "laundryroom")]
        hovered Show("displayTextScreen", displayText = "Laundry room")
        unhovered Hide("displayTextScreen")

    #livingroom
    imagebutton:
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"
        xpos 0.120
        ypos 0.85
        at customzoom
        auto "ui/icons/livingroom_%s.png"
        action [Hide("displayTextScreen"), SetVariable("show_buttons", False), Function(move_to_room, "livingroom")]
        hovered Show("displayTextScreen", displayText = "Living Room")
        unhovered Hide("displayTextScreen")

    #kitchen
    imagebutton:
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"
        xpos 0.176
        ypos 0.85
        at customzoom
        auto "ui/icons/kitchen_%s.png"
        action [Hide("displayTextScreen"), SetVariable("show_buttons", False), Function(move_to_room, "kitchen")]
        hovered Show("displayTextScreen", displayText = "Kitchen")
        unhovered Hide("displayTextScreen")

    #bathroom
    imagebutton:
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"
        xpos 0.232
        ypos 0.85
        at customzoom2
        auto "ui/icons/bathroom_%s.png"
        action [Hide("displayTextScreen"), SetVariable("show_buttons", False), Function(move_to_room, "bathroom")]
        hovered Show("displayTextScreen", displayText = "Bathroom")
        unhovered Hide("displayTextScreen")


    #bedrooms
    imagebutton:
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"
        xpos 0.01
        ypos 0.85
        at customzoom
        auto "ui/icons/bedroom_%s.png"
        action [Hide("displayTextScreen"), ToggleVariable("show_buttons",True), Function(move_to_room, "bedroom_hallway")]
        hovered Show("displayTextScreen", displayText = "Bedrooms")
        unhovered Hide("displayTextScreen")

    if show_buttons:
        if him_location == "himawaribedroom":
            add "ui/icons/green_dot.png" xpos 0.06 ypos 0.69 zoom 0.7
        if him_location == "hinatabedroom":
            add "ui/icons/green_dot.png" xpos 0.06 ypos 0.59 zoom 0.7
        if him_location == "borutobedroom":
            add "ui/icons/green_dot.png" xpos 0.06 ypos 0.785 zoom 0.7


        if hin_location == "hinatabedroom":
            add "ui/icons/green_dot.png" xpos 0.06 ypos 0.59 zoom 0.7
        if hin_location == "himawaribedroom":
            add "ui/icons/green_dot.png" xpos 0.06 ypos 0.69 zoom 0.7
        if hin_location == "borutobedroom":
            add "ui/icons/green_dot.png" xpos 0.06 ypos 0.785 zoom 0.7

        imagebutton:
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            auto "ui/icons/boru_%s.png"
            action [SetVariable("show_buttons", False), Jump("borutobedroom")] xpos 0.011 ypos 0.75

        imagebutton:
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            auto "ui/icons/hima_%s.webp"
            action [SetVariable("show_buttons", False), Function(move_to_room, "himawaribedroom")] xpos 0.011 ypos 0.66
        

        imagebutton:
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            auto "ui/icons/hina_%s.webp"
            action [SetVariable("show_buttons", False), Function(move_to_room, "hinatabedroom")] xpos 0.011 ypos 0.57
        



# text when hovering any button / tooltip
screen displayTextScreen:
    zorder 1100
    default displayText = "bedrooms"
    frame:
        background "#000000CC"  # Semi-transparent background
        padding (10, 10)
        align (0.5, 0.72)  # Adjust the alignment as needed

        text displayText:
            size 20
            color "#fff"

screen tooltip:
    zorder 1100
    default tooltipText = None
    frame:
        background "#0008"  # Semi-transparent background
        padding (10, 10)
        align (0.07, 0.3)  # Adjust the alignment as needed

        text tooltipText:
            size 20
            color "#fff"

#-------------------------------------------------------------------------------------

default bgicon ="wait"





style talkbutton is default:
    hover_sound "audio/soun_fx/select1.opus"
    activate_sound "audio/soun_fx/select4.opus"
    size 50
    background Frame("ui/talk.png", 0, 0)
    xminimum 50
    yminimum 50
    xmaximum 50
    ymaximum 50
    xpadding 0
    ypadding 0


style gymbutton is default:
    hover_sound "audio/soun_fx/select1.opus"
    activate_sound "audio/soun_fx/select4.opus"
    size 50
    background Frame("ui/strength_button.png", 0, 0)
    xminimum 50
    yminimum 50
    xmaximum 50
    ymaximum 50
    xpadding 0
    ypadding 0



style actionbutton is default:
    hover_sound "audio/soun_fx/select1.opus"
    activate_sound "audio/soun_fx/select4.opus"
    size 50
    background Frame("ui/action.png", 0, 0)
    xminimum 50
    yminimum 50
    xmaximum 50
    ymaximum 50
    xpadding 0
    ypadding 0

style infobutton_shown is default:
    hover_sound "audio/soun_fx/select1.opus"
    activate_sound "audio/soun_fx/select4.opus"
    size 50
    background Frame("ui/questionmark_shown.png", 0, 0)
    xminimum 50
    yminimum 50
    xmaximum 50
    ymaximum 50
    xpadding 0
    ypadding 0

style infobutton_inactive is default:
    hover_sound "audio/soun_fx/select1.opus"
    activate_sound "audio/soun_fx/select4.opus"
    size 50
    background Frame("ui/questionmark_inactive.png", 0, 0)
    xminimum 50
    yminimum 50
    xmaximum 50
    ymaximum 50
    xpadding 0
    ypadding 0

style infobutton is default:
    hover_sound "audio/soun_fx/select1.opus"
    activate_sound "audio/soun_fx/select4.opus"
    size 50
    background Frame("ui/questionmark.png", 0, 0)
    xminimum 50
    yminimum 50
    xmaximum 50
    ymaximum 50
    xpadding 0
    ypadding 0


style hoveredbutton:
    # background Solid("#666")
    #foreground "#ffff00"
    background Frame("ui/[bgicon].png", 0, 0)
    xminimum 53
    yminimum 53
    xmaximum 53
    ymaximum 53
    # xpadding 10
    # ypadding 10

style button_clicked:
    size 50
    # background Frame("ui/talk.webp", 0, 0)
    # foreground "#ffff00"
    xminimum 50
    yminimum 50
    xmaximum 50
    ymaximum 50
    xpadding 10
    ypadding 10



#tutorial boruto bedroom
screen borutobedroombuttonstutorial():
    default tooltip_text = None
    default button_style1 = "sleepbutton"
    default button_style2 = "gymbutton"
    default button_style3 = "talkbutton"
    frame:
        xalign 0.9
        yalign 0.93        
        button:
            style button_style1
            hovered [Show("tooltip", tooltipText = "Sleep"),SetScreenVariable("button_style1", "hoveredbutton"), SetVariable("bgicon", "sleep")]
            unhovered [Hide("tooltip"), SetScreenVariable("button_style1", "sleepbutton")]
            action [Jump("borutobedroommenu"), SetScreenVariable("button_style1", "button_clicked")]




    
###### action/talk buttons #######
screen actionbuttonshouse():
    zorder 1000
    default button_style_sleep = "sleepbutton"
    default button_style_gym = "gymbutton"
    default button_style_talk = "talkbutton"
    default button_style_infoinactive = "infobutton_inactive"
    default button_style_info = "infobutton"
    default button_style_infoshown = "infobutton_shown"
    default button_style_action = "actionbutton"
    default infotext = "There is nothing to do here..."
    frame:
        ypos 200
        background "#0009"
        vbox:
            xalign 0.5 yalign 0.5
            spacing 20
    #Laundry room ----------------------------------------------
            if boruto_location == "laundryroom":
                #actionbutton
                if actionbutton == True:
                          
                        button:
                            style button_style_action
                            hovered [Show("tooltip", tooltipText = "Action"),SetScreenVariable("button_style_action", "hoveredbutton"), SetVariable("bgicon", "action")]
                            unhovered [Hide("tooltip"), SetScreenVariable("button_style_action", "actionbutton")]
                            action [Jump("laundryroomactionmenu")]

                #talkbutton
                if talkbutton == True:
                   
                        button:
                            style button_style_talk
                            hovered [Show("tooltip", tooltipText = "Talk"),SetScreenVariable("button_style_talk", "hoveredbutton"), SetVariable("bgicon", "talk")]
                            unhovered [Hide("tooltip"), SetScreenVariable("button_style_talk", "talkbutton")]
                            action [Jump("laundryroomntalkmenu"), SetScreenVariable("button_style2", "button_clicked")]


                if infobutton == "active":

                    button:
                        style button_style_info
                        hovered [Show("tooltip", tooltipText = "There is something of importance here!"), SetScreenVariable("button_style_info", "hoveredbutton"), SetVariable("bgicon", "questionmark")]
                        unhovered [Hide("tooltip"), SetScreenVariable("button_style_info", "infobutton")]
                        action [Show("scrollingtext"), SetScreenVariable("texttosend", "infotext")]
                elif infobutton == "inactive":
                
                    button:
                        style button_style_infoinactive
                        hovered [Show("tooltip", tooltipText = "There is nothing to do here right now"), SetScreenVariable("button_style_infoinactive", "hoveredbutton"), SetVariable("bgicon", "questionmark_inactive")]
                        unhovered [Hide("tooltip"), SetScreenVariable("button_style_infoinactive", "infobutton_inactive")]
                        action NullAction()
                else:

                    button:
                        style button_style_infoshown
                        hovered [Show("tooltip", tooltipText = "There are available actions"), SetScreenVariable("button_style_infoshown", "hoveredbutton"), SetVariable("bgicon", "questionmark_shown")]
                        unhovered [Hide("tooltip"), SetScreenVariable("button_style_infoshown", "infobutton_shown")]
                        action NullAction()
    #Boruto bedroom--------------------------------------------------------------------------            
            elif boruto_location == "borutobedroom":


                #strengthbutton
                if strengthbutton == True:
                    button:
                        
                        style button_style_gym
                        hovered [Show("tooltip", tooltipText = "Strength Training"),SetScreenVariable("button_style_gym", "hoveredbutton"), SetVariable("bgicon", "gym")]
                        unhovered [Hide("tooltip"), SetScreenVariable("button_style_gym", "gymbutton")]
                        action [Jump("strengthmenu"), SetScreenVariable("button_style_gym", "button_clicked")]

                #actionbutton
                if actionbutton == True:
                     
                    button:
                        style button_style_action
                        hovered [Show("tooltip", tooltipText = "Action"),SetScreenVariable("button_style_action", "hoveredbutton"), SetVariable("bgicon", "action")]
                        unhovered [Hide("tooltip"), SetScreenVariable("button_style_action", "actionbutton")]
                        action [Jump("borutobedroomactionmenu")]

                #talkbutton
                if talkbutton == True:
                    
                    button:
                        style button_style_talk
                        hovered [Show("tooltip", tooltipText = "Talk"),SetScreenVariable("button_style_talk", "hoveredbutton"), SetVariable("bgicon", "talk")]
                        unhovered [Hide("tooltip"), SetScreenVariable("button_style_talk", "talkbutton")]
                        action [Jump("borutobedroomntalkmenu")]

                if infobutton == "active":
                
                    button:
                        style button_style_info
                        hovered [Show("tooltip", tooltipText = "There is something of importance here!")]
                        unhovered [Hide("tooltip")]
                        action [Hide("scrollingtext"), Show("scrollingtext", text=clickinfobutton)]
                elif infobutton =="inaxctive":
                    button:
                        style button_style_infoinactive
                        hovered Show("tooltip", tooltipText = "There is nothing to do here right now")
                        unhovered [Hide("tooltip")]
                        action NullAction()
                
                else:

                    button:
                        style button_style_infoshown
                        hovered [Show("tooltip", tooltipText = "There are available actions"), SetScreenVariable("button_style_infoshown", "hoveredbutton"), SetVariable("bgicon", "questionmark_shown")]
                        unhovered [Hide("tooltip"), SetScreenVariable("button_style_infoshown", "infobutton_shown")]
                        action NullAction()

        #Hinata bedroom ----------------------------------------------
            elif boruto_location == "hinatabedroom":
                #actionbutton
                if actionbutton == True:
                          
                        button:
                            style button_style_action
                            hovered [Show("tooltip", tooltipText = "Action"),SetScreenVariable("button_style_action", "hoveredbutton"), SetVariable("bgicon", "action")]
                            unhovered [Hide("tooltip"), SetScreenVariable("button_style_action", "actionbutton")]
                            action [Jump("hinatabedroomactionmenu")]

                #talkbutton
                if talkbutton == True:
                   
                        button:
                            style button_style_talk
                            hovered [Show("tooltip", tooltipText = "Talk"),SetScreenVariable("button_style_talk", "hoveredbutton"), SetVariable("bgicon", "talk")]
                            unhovered [Hide("tooltip"), SetScreenVariable("button_style_talk", "talkbutton")]
                            action [Jump("hinatabedroomntalkmenu"), SetScreenVariable("button_style_talk", "button_clicked")]


                if infobutton == "active":
    
                        button:
                            style button_style_info
                            hovered [Show("tooltip", tooltipText = "There is something of importance here!"), SetScreenVariable("button_style_info", "hoveredbutton"), SetVariable("bgicon", "questionmark")]
                            unhovered [Hide("tooltip"), SetScreenVariable("button_style_info", "infobutton")]
                            action [Show("scrollingtext"), SetScreenVariable("texttosend", "infotext")]
                elif infobutton == "inactive":
                
                        button:
                            style button_style_infoinactive
                            sensitive True
                            hovered [Show("tooltip", tooltipText = "There is nothing to do here right now"), SetScreenVariable("button_style_infoinactive", "hoveredbutton"), SetVariable("bgicon", "questionmark_inactive")]
                            unhovered [Hide("tooltip"), SetScreenVariable("button_style_infoinactive", "infobutton_inactive")]
                            action NullAction() 
                
                else:

                    button:
                        style button_style_infoshown
                        hovered [Show("tooltip", tooltipText = "There are available actions"), SetScreenVariable("button_style_infoshown", "hoveredbutton"), SetVariable("bgicon", "questionmark_shown")]
                        unhovered [Hide("tooltip"), SetScreenVariable("button_style_infoshown", "infobutton_shown")]
                        action NullAction()

        #himawari bedroom--------------------------------------------------------------------------            
            elif boruto_location == "himawaribedroom":

                #actionbutton
                if actionbutton == True:
                
                    button:
                        style button_style_action
                        hovered [Show("tooltip", tooltipText = "Action"),SetScreenVariable("button_style_action", "hoveredbutton"), SetVariable("bgicon", "action")]
                        unhovered [Hide("tooltip"), SetScreenVariable("button_style_action", "actionbutton")]
                        action [SetScreenVariable("button_style1", "button_clicked"), Jump("himawaribedroomactionmenu")]

                #talkbutton
                if talkbutton == True:
               
                        button:
                            style button_style_talk
                            hovered [Show("tooltip", tooltipText = "Talk"),SetScreenVariable("button_style_talk", "hoveredbutton"), SetVariable("bgicon", "talk")]
                            unhovered [Hide("tooltip"), SetScreenVariable("button_style_talk", "talkbutton")]
                            action [Jump("himawaribedroomntalkmenu"), SetScreenVariable("button_style_talk", "button_clicked")]


                if infobutton == "active":
                    button:
                        style button_style_info
                        hovered [Show("tooltip", tooltipText = "There is something of importance here!"), SetScreenVariable("button_style_info", "hoveredbutton"), SetVariable("bgicon", "questionmark")]
                        unhovered [Hide("tooltip"), SetScreenVariable("button_style_info", "infobutton")]
                        action [Hide("scrollingtext"), Show("scrollingtext", text=clickinfobutton)]
                elif infobutton == "inactive":
                    button:
                        style button_style_infoinactive
                        hovered Show("tooltip", tooltipText = "There is nothing to do here right now")
                        unhovered [Hide("tooltip")]
                        action NullAction()
                else:
                    button:
                        style button_style_infoshown
                        hovered [Show("tooltip", tooltipText = "There are available actions"), SetScreenVariable("button_style_infoshown", "hoveredbutton"), SetVariable("bgicon", "questionmark_shown")]
                        unhovered [Hide("tooltip"), SetScreenVariable("button_style_infoshown", "infobutton_shown")]
                        action NullAction()    

        #Living room ----------------------------------------------
            elif boruto_location == "livingroom":
                #actionbutton
                if actionbutton == True:
                          
                        button:
                            style button_style_action
                            hovered [Show("tooltip", tooltipText = "Action"),SetScreenVariable("button_style_action", "hoveredbutton"), SetVariable("bgicon", "action")]
                            unhovered [Hide("tooltip"), SetScreenVariable("button_style_action", "actionbutton")]
                            action [Jump("livingroomactionmenu")]

                #talkbutton
                if talkbutton == True:
                   
                        button:
                            style button_style_talk
                            hovered [Show("tooltip", tooltipText = "Talk"),SetScreenVariable("button_style_talk", "hoveredbutton"), SetVariable("bgicon", "talk")]
                            unhovered [Hide("tooltip"), SetScreenVariable("button_style_talk", "talkbutton")]
                            action [Jump("livingroomtalkmenu"), SetScreenVariable("button_style2", "button_clicked")]


                if infobutton == "active":
                    button:
                        style button_style_info
                        hovered [Show("tooltip", tooltipText = "There is something of importance here!"), SetScreenVariable("button_style_info", "hoveredbutton"), SetVariable("bgicon", "questionmark")]
                        unhovered [Hide("tooltip"), SetScreenVariable("button_style_info", "infobutton")]
                        action [Show("scrollingtext"), SetScreenVariable("texttosend", "infotext")]
                elif infobutton == "inactive":
                    button:
                        style button_style_infoinactive
                        hovered [Show("tooltip", tooltipText = "There is nothing to do here right now"), SetScreenVariable("button_style_infoinactive", "hoveredbutton"), SetVariable("bgicon", "questionmark_inactive")]
                        unhovered [Hide("tooltip"), SetScreenVariable("button_style_infoinactive", "infobutton_inactive")]
                        action NullAction()
                else:
                    button:
                        style button_style_infoshown
                        hovered [Show("tooltip", tooltipText = "There are available actions"), SetScreenVariable("button_style_infoshown", "hoveredbutton"), SetVariable("bgicon", "questionmark_shown")]
                        unhovered [Hide("tooltip"), SetScreenVariable("button_style_infoshown", "infobutton_shown")]
                        action NullAction()        
        #Kitchen room ----------------------------------------------
            elif boruto_location == "kitchen":
                #actionbutton
                if actionbutton == True:
                          
                    button:
                        style button_style_action
                        hovered [Show("tooltip", tooltipText = "Action"),SetScreenVariable("button_style_action", "hoveredbutton"), SetVariable("bgicon", "action")]
                        unhovered [Hide("tooltip"), SetScreenVariable("button_style_action", "actionbutton")]
                        action [Jump("kitchenactionmenu")]

                #talkbutton
                if talkbutton == True:

                    button:
                        style button_style_talk
                        hovered [Show("tooltip", tooltipText = "Talk"),SetScreenVariable("button_style_talk", "hoveredbutton"), SetVariable("bgicon", "talk")]
                        unhovered [Hide("tooltip"), SetScreenVariable("button_style_talk", "talkbutton")]
                        action [Jump("kitchentalkmenu")]


                if infobutton == "active":
                    button:
                        style button_style_info
                        hovered [Show("tooltip", tooltipText = "There is something of importance here!"), SetScreenVariable("button_style_info", "hoveredbutton"), SetVariable("bgicon", "questionmark")]
                        unhovered [Hide("tooltip"), SetScreenVariable("button_style_info", "infobutton")]
                        action [Show("scrollingtext")]
                elif infobutton == "inactive": 
                    button:
                        style button_style_infoinactive
                        sensitive True
                        hovered [Show("tooltip", tooltipText = "There is nothing to do here right now"), SetScreenVariable("button_style_infoinactive", "hoveredbutton"), SetVariable("bgicon", "questionmark_inactive")]
                        unhovered [Hide("tooltip"), SetScreenVariable("button_style_infoinactive", "infobutton_inactive")]
                        action NullAction()
                else:

                    button:
                        style button_style_infoshown
                        hovered [Show("tooltip", tooltipText = "There are available actions"), SetScreenVariable("button_style_infoshown", "hoveredbutton"), SetVariable("bgicon", "questionmark_shown")]
                        unhovered [Hide("tooltip"), SetScreenVariable("button_style_infoshown", "infobutton_shown")]
                        action NullAction()

        #bathroom ----------------------------------------------
            elif boruto_location == "bathroom":
                #actionbutton
                if actionbutton == True:
                          
                    button:
                        style button_style_action
                        hovered [Show("tooltip", tooltipText = "Action"),SetScreenVariable("button_style_action", "hoveredbutton"), SetVariable("bgicon", "action")]
                        unhovered [Hide("tooltip"), SetScreenVariable("button_style_action", "actionbutton")]
                        action [Jump("bathroomactionmenu")]

                #talkbutton
                if talkbutton == True:
                
                    button:
                        style button_style_talk
                        hovered [Show("tooltip", tooltipText = "Talk"),SetScreenVariable("button_style_talk", "hoveredbutton"), SetVariable("bgicon", "talk")]
                        unhovered [Hide("tooltip"), SetScreenVariable("button_style_talk", "talkbutton")]
                        action [Jump("bathroomntalkmenu"), SetScreenVariable("button_style2", "button_clicked")]


                if infobutton == "active":    
                    button:
                        style button_style_info
                        hovered [Show("tooltip", tooltipText = "There is something of importance here!"), SetScreenVariable("button_style_info", "hoveredbutton"), SetVariable("bgicon", "questionmark")]
                        unhovered [Hide("tooltip"), SetScreenVariable("button_style_info", "infobutton")]
                        action [Show("scrollingtext"), SetScreenVariable("texttosend", "infotext")]
                elif infobutton == "inactive":
                    button:
                        style button_style_infoinactive
                        sensitive True
                        hovered [Show("tooltip", tooltipText = "There is nothing to do here right now"), SetScreenVariable("button_style_infoinactive", "hoveredbutton"), SetVariable("bgicon", "questionmark_inactive")]
                        unhovered [Hide("tooltip"), SetScreenVariable("button_style_infoinactive", "infobutton_inactive")]
                        action NullAction()
                else:

                    button:
                        style button_style_infoshown
                        hovered [Show("tooltip", tooltipText = "There are available actions"), SetScreenVariable("button_style_infoshown", "hoveredbutton"), SetVariable("bgicon", "questionmark_shown")]
                        unhovered [Hide("tooltip"), SetScreenVariable("button_style_infoshown", "infobutton_shown")]
                        action NullAction()
                
            elif boruto_location == "nightspy":
                if infobutton == "active":    
                    button:
                        style button_style_info
                        hovered [Show("tooltip", tooltipText = "Find hotspots around the room"), SetScreenVariable("button_style_info", "hoveredbutton"), SetVariable("bgicon", "questionmark")]
                        unhovered [Hide("tooltip"), SetScreenVariable("button_style_info", "infobutton")]
                        action [Hide("scrollingtext"), Show("scrollingtext", text=clickinfobutton)]
            elif boruto_location == "wrestlehimawari":
                if infobutton == "active":    
                    button:
                        style button_style_info
                        hovered [Show("tooltip", tooltipText = "Find hotspots on her body"), SetScreenVariable("button_style_info", "hoveredbutton"), SetVariable("bgicon", "questionmark")]
                        unhovered [Hide("tooltip"), SetScreenVariable("button_style_info", "infobutton")]
                        action [Hide("scrollingtext"), Show("scrollingtext", text=clickinfobutton)]


#No location ----------------------------------------------
            else: # no location
                button:
                    style button_style_infoinactive
                    # sensitive False
                    hovered Show("tooltip", tooltipText = "There is nothing to do here right now")
                    unhovered [Hide("tooltip")]
                    action NullAction()
                




#boruto bedroom
screen borutobedroombuttons():
    default tooltip_text = None
    default button_style1 = "sleepbutton"
    default button_style2 = "gymbutton"
    default button_style3 = "talkbutton"

    #sleep button night
    frame:
        xalign 0.90
        yalign 0.93        
        button:
            style button_style1
            hovered [Show("tooltip", tooltipText = "Sleep"),SetScreenVariable("button_style1", "hoveredbutton"), SetVariable("bgicon", "sleep")]
            unhovered [Hide("tooltip"), SetScreenVariable("button_style1", "sleepbutton")]
            action [Jump("sleepmenu"), SetScreenVariable("button_style1", "button_clicked")]



    #talkbutton
    if talkbutton == True:
        frame:
            xalign 0.80
            yalign 0.93

            button:
                style button_style3
                hovered [Show("tooltip", tooltipText = "Talk"),SetScreenVariable("button_style3", "hoveredbutton"), SetVariable("bgicon", "talk")]
                unhovered [Hide("tooltip", None), SetScreenVariable("button_style3", "talkbutton")]
                action [Jump("borutobedroomntalkmenu"), SetScreenVariable("button_style3", "button_clicked")]

  


#himawari bedroom
screen himawaribedroombuttons():
    default tooltip_text = None
    default button_style1 = "actionbutton"
    default button_style2 = "talkbutton"


    if actionbutton == True:
        frame:
            xalign 0.9
            yalign 0.93        
            button:
                style button_style1
                hovered [Show("tooltip", tooltipText = "Action"),SetScreenVariable("button_style1", "hoveredbutton"), SetVariable("bgicon", "action")]
                unhovered [Hide("tooltip"), SetScreenVariable("button_style1", "actionbutton")]
                action [Jump("himawaribedroomnactionmenu"), SetScreenVariable("button_style1", "button_clicked")]


    #talkbutton
    if talkbutton == True:
        frame:
            xalign 0.85
            yalign 0.93

            button:
                style button_style2
                hovered [Show("tooltip", tooltipText = "Talk"),SetScreenVariable("button_style2", "hoveredbutton"), SetVariable("bgicon", "talk")]
                unhovered [Hide("tooltip"), SetScreenVariable("button_style2", "talkbutton")]
                action [Jump("himawaribedroomntalkmenu"), SetScreenVariable("button_style2", "button_clicked")]



#hinata bedroom
screen hinatabedroombuttons():
    default tooltip_text = None
    default button_style1 = "actionbutton"
    default button_style2 = "talkbutton"

    if actionbutton == True:
        frame:
            xalign 0.9
            yalign 0.93        
            button:
                style button_style1
                hovered [Show("tooltip", tooltipText = "Action"),SetScreenVariable("button_style1", "hoveredbutton"), SetVariable("bgicon", "action")]
                unhovered [Hide("tooltip"), SetScreenVariable("button_style1", "actionbutton")]
                action [Jump("hinataroomactionmenu"), SetScreenVariable("button_style1", "button_clicked")]


    #talkbutton
    if talkbutton == True:
        frame:
            xalign 0.85
            yalign 0.93

            button:
                style button_style2
                hovered [Show("tooltip", tooltipText = "Talk"),SetScreenVariable("button_style2", "hoveredbutton"), SetVariable("bgicon", "talk")]
                unhovered [Hide("tooltip"), SetScreenVariable("button_style2", "talkbutton")]
                action [Jump("hinatabedroomntalkmenu"), SetScreenVariable("button_style2", "button_clicked")]



#living room
screen livingroombuttons():
    default tooltip_text = None
    default button_style1 = "actionbutton"
    default button_style2 = "talkbutton"

    #actionbutton
    if actionbutton == True:
        frame:
            xalign 0.9
            yalign 0.93        
            button:
                style button_style1
                hovered [Show("tooltip", tooltipText = "Action"),SetScreenVariable("button_style1", "hoveredbutton"), SetVariable("bgicon", "action")]
                unhovered [Hide("tooltip"), SetScreenVariable("button_style1", "actionbutton")]
                action [Jump("sleepmenu"), SetScreenVariable("button_style1", "button_clicked")]

    #talkbutton
    if talkbutton == True:
        frame:
            xalign 0.85
            yalign 0.93

            button:
                style button_style2
                hovered [Show("tooltip", tooltipText = "Talk"),SetScreenVariable("button_style2", "hoveredbutton"), SetVariable("bgicon", "talk")]
                unhovered [Hide("tooltip"), SetScreenVariable("button_style2", "talkbutton")]
                action [Jump("livingroomtalkmenu"), SetScreenVariable("button_style2", "button_clicked")]



#laundry room
screen laundryroombuttons():
    default tooltip_text = None
    default button_style1 = "actionbutton"
    default button_style2 = "talkbutton"

    #actionbutton
    if actionbutton == True:
        frame:
            xalign 0.9
            yalign 0.93        
            button:
                style button_style1
                hovered [Show("tooltip", tooltipText = "Action"),SetScreenVariable("button_style1", "hoveredbutton"), SetVariable("bgicon", "action")]
                unhovered [Hide("tooltip"), SetScreenVariable("button_style1", "actionbutton")]
                action [SetScreenVariable("button_style1", "button_clicked"), Jump("laundryroomactionmenu")]

    #talkbutton
    if talkbutton == True:
        frame:
            xalign 0.85
            yalign 0.93

            button:
                style button_style2
                hovered [Show("tooltip", tooltipText = "Talk"),SetScreenVariable("button_style2", "hoveredbutton"), SetVariable("bgicon", "talk")]
                unhovered [Hide("tooltip"), SetScreenVariable("button_style2", "talkbutton")]
                action [Jump("laundryroomntalkmenu"), SetScreenVariable("button_style2", "button_clicked")]


#kitchen room
screen kitchenbuttons():
    default tooltip_text = None
    default button_style1 = "actionbutton"
    default button_style2 = "talkbutton"

    #actionbutton
    if actionbutton == True:
        frame:
            xalign 0.9
            yalign 0.93        
            button:
                style button_style1
                hovered [Show("tooltip", tooltipText = "Action"),SetScreenVariable("button_style1", "hoveredbutton"), SetVariable("bgicon", "action")]
                unhovered [Hide("tooltip"), SetScreenVariable("button_style1", "actionbutton")]
                action [Jump("sleepmenu"), SetScreenVariable("button_style1", "button_clicked")]

    #talkbutton
    if talkbutton == True:
        frame:
            xalign 0.85
            yalign 0.93

            button:
                style button_style2
                hovered [Show("tooltip", tooltipText = "Talk"),SetScreenVariable("button_style2", "hoveredbutton"), SetVariable("bgicon", "talk")]
                unhovered [Hide("tooltip"), SetScreenVariable("button_style2", "talkbutton")]
                action [Jump("kitchentalkmenu"), SetScreenVariable("button_style2", "button_clicked")]




#bathroom
screen bathroombuttons():
    default tooltip_text = None
    default button_style1 = "actionbutton"
    default button_style2 = "talkbutton"

    #actionbutton
    if actionbutton == True:
        frame:
            xalign 0.9
            yalign 0.93        
            button:
                style button_style1
                hovered [Show("tooltip", tooltipText = "Action"),SetScreenVariable("button_style1", "hoveredbutton"), SetVariable("bgicon", "action")]
                unhovered [Hide("tooltip"), SetScreenVariable("button_style1", "actionbutton")]
                action [Jump("bathroomactionmenu"), SetScreenVariable("button_style1", "button_clicked")]

    #talkbutton
    if talkbutton == True:
        frame:
            xalign 0.85
            yalign 0.93

            button:
                style button_style2
                hovered [Show("tooltip", tooltipText = "Talk"),SetScreenVariable("button_style2", "hoveredbutton"), SetVariable("bgicon", "talk")]
                unhovered [Hide("tooltip"), SetScreenVariable("button_style2", "talkbutton")]
                action [Jump("bathroomntalkmenu"), SetScreenVariable("button_style2", "button_clicked")]

