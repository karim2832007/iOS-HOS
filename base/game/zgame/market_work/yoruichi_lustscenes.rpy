init python:
    from renpy.display.render import Render
    import pygame

    class FocusEffect(renpy.Displayable):
        def __init__(self, child, focus_x, focus_y, focus_radius, darkness=0.5):
            super(FocusEffect, self).__init__()
            self.child = renpy.displayable(child)
            self.focus_x = focus_x
            self.focus_y = focus_y
            self.focus_radius = focus_radius
            self.darkness = darkness

        def render(self, width, height, st, at):
            render = renpy.Render(width, height)
            
            # Render the child
            cr = renpy.render(self.child, width, height, st, at)
            render.blit(cr, (0, 0))

            # Create the darkening surface
            dark = pygame.Surface((width, height), pygame.SRCALPHA)
            dark.fill((0, 0, 0, int(255 * self.darkness)))

            # Create the circular focus area
            pygame.draw.circle(dark, (0, 0, 0, 0), (self.focus_x, self.focus_y), self.focus_radius)

            # Blit the darkening surface onto the render
            render.blit(renpy.Render(width, height), (0, 0))
            render.blit(dark, (0, 0))

            return render

screen focused_screen(background, focus_x, focus_y):
    add background
    add "darkening_overlay"
    add "focus_area" at focus_position(focus_x, focus_y)

screen yoruichi_lustscene1_screen(baseImage):
    on "show" action Function(mark_screen_image_gallery, baseImage)
    imagebutton:
        xalign 0.5 yalign 0.01
        auto "images/ui/pov_change_%s.png"
        hovered Show("displayTextScreen", displayText = "Change PoV")
        unhovered [Hide("displayTextScreen")]
        action [Show("yoruichi_lustscene1_povs", baseImage = baseImage), Hide("displayTextScreen")]
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"

screen yoruichi_lustscene1_povs(baseImage):
    on "show" action Function(mark_screen_image_gallery, baseImage)    
    modal True
    add baseImage zoom 1.0 xalign 0.5 yalign 0.5
    for k in ['K_RETURN', 'K_SPACE', 'K_KP_ENTER', 'K_SELECT', 'mouseup_1']:
        key k action NullAction()
    
    #full screen button
    button:
        action NullAction()

    #return
    imagebutton:
        xalign 0.95 yalign 0.05
        auto "images/ui/return_button_%s.png"
        hovered Show("displayTextScreen", displayText = "Return to Event")
        unhovered [Hide("displayTextScreen")]
        action [Hide("yoruichi_lustscene1_povs"), Hide("displayTextScreen")]
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"


label yoruichi_lustscene1:
    default yoruichi_lustscene1_firsttime = True
    scene black with dissolve
    if yoruichi_lustscene1_firsttime == False:
        jump yoruichi_lustscene1_repeat
    bo"F-fuck!" with vpunch
    bot"I've let my condition fester for too long!"
    show ramenkitchen
    show boruto surprised3 at left
    show yoru shy at right
    with dissolve
    call borutoevil2 from _call_borutoevil2_13
    show boruto bonersurprised2 with dissolve
    bo"I've forgotten... about my... arrh!"
    show yoru scared2 with dissolve
    yo"W-what the hell... is that!?" with vpunch
    bo"I... told you about my condition, remember?"
    show boruto bonersurprisedred
    show yoru shy2 with dissolve
    bo"F-fuck!" with vpunch
    bo"L-listen to me and listen carefully before I turn into a goddamn animal!"
    bo"I need you to... take off your s-shirt."
    show yoru surprised with dissolve
    yo"W-what!?" with vpunch
    bo"Do it... p-please!"
    show yoru shy with dissolve
    yo"Y-you are scaring me..."
    call borutoevil3 from _call_borutoevil3
    show boruto bonerevil3
    bo"Now, bitch!" with vpunch
    bo"I'll do more than scare you if you don't do as I say!" with vpunch
    show yoru obedient with dissolve
    yo"Okay, okay! I will do it, but p-please... don't do anything stupid!"
    hide yoru
    show tits3t at right:
        zoom 0.6
    with Dissolve(1)
    yo"Is this... w-what you wanted?"
    show boruto bonerevil4:
        easein 1.5 xalign 0.5
    bo"Now kneel!"
    hide tits3t
    show tits misc5t at right with dissolve:
        zoom 0.6
    yo"K-kneel...?"
    show boruto:
        linear 0.3 xalign 0.8
    pause 0.3
    scene black with vpunch
    bo"KNEEL! And look sraight into my eyes..."
    show yorusecretabove0 with dissolve
    bo"Good girl..."
    yo"W-why are you doing this...?"
    bo"Now I need you to sit there while I am handling my condition!"
    yo"W-what are you talking about!"
    bo"What else..."
    $ renpy.sound.play("/audio/soun_fx/clothes_undress.opus", channel="sfx3", loop=False, relative_volume = 0.7)
    show yorusecretintro1 with fade
    bo"But this!"
    yo"Y-you cannot be serious..."
    show screen yoruichi_lustscene1_screen("yorusecretabove2")
    show expression FocusEffect("idle1", 640, 50, 75, 0.7) with dissolve
    "You can change PoVs using the camera button"
    hide expression FocusEffect with dissolve
    show yorusecretintro0 with dissolve
    yo"What's wrong with your thing!?" with vpunch
    show yoruichi_lustscene1_anim with dissolve
    $ renpy.sound.play("/audio/soun_fx/handjob1.opus", channel="sfx3", loop=False, relative_volume = 0.7)
    bo"Nothing's wrong with it... In fact, it seems to have taken a liking to you!"
    yo"*Gasps*"
    bo"Don't worry, this won't take long..."
    bo"Not with how pretty your face looks while you are kneeling right under my cock!"
    hide screen yoruichi_lustscene1_screen
    bo"Allow me to change that!" with flash
    menu:
        bo"Allow me to change that!"
        "Cum from PoV":
            $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx3", loop=False, relative_volume = 0.4)
            show yorusecretabove3 with flash
            bo"Arrrgh!"
            $ renpy.sound.play("/audio/soun_fx/cum5.opus", channel="sfx3", loop=False, relative_volume = 0.4)
            show yorusecretabove4 with flash
            call decreaselust(50) from _call_decreaselust_38
            bo"Yesss!" with flash
            bo"T-that's it Y-yoru!..."
            $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx3", loop=False, relative_volume = 0.4)
            show yorusecretabove5 with longerflash
            call decreaselust(50) from _call_decreaselust_39
            show screen yoruichi_lustscene1_screen("yorusecretintro3")
            bo"Take it all on your pretty face!" with flash
            $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            bo"*Panting*"
            yo"Y-you..."
            bo"Wait... W-what have I done?"
            hide screen yoruichi_lustscene1_screen
            jump yoruichi_lustscene1_ending

        "Cum from side":
            $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx3", loop=False, relative_volume = 0.4)
            show yorusecretintro2 with flash
            call decreaselust(50) from _call_decreaselust_40
            bo"Arrrgh!"
            $ renpy.sound.play("/audio/soun_fx/cum5.opus", channel="sfx3", loop=False, relative_volume = 0.4)
            show yorusecretintro2 with flash
            bo"Yesss!" with flash
            bo"T-that's it Y-yoru!..."
            $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx3", loop=False, relative_volume = 0.4)
            show yorusecretintro3 with longerflash
            call decreaselust(50) from _call_decreaselust_41
            show screen yoruichi_lustscene1_screen("yorusecretabove5")
            bo"Take it all on your pretty face!" with flash
            $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            bo"*Panting*"
            yo"Y-you..."
            bo"Wait... W-what have I done?"
            hide screen yoruichi_lustscene1_screen
            jump yoruichi_lustscene1_ending
        



    label yoruichi_lustscene1_ending:
        scene black with vpunch
        yo"Y-you piece of shit!"
        $ notification ("Yoruichi's relationship changed")
        "Yoruichi's status is now 'Apprehensive'"
        $ yoruichi_relationship = "Apprehensive"
        "You've lost Yoruichi's trust. You can try earning it back by bribing her..."
        yo"...I thought I could trust you!"
        yo"And this is the kind of shit you pull off?"
        bo"Yoru I... I lost control, I didn't mean to!"
        yo"A convenient excuse, you fucking asshole!"
        "You both take some time to gather yourselves..."
        show ramenkitchen
        show boruto suspicious at left with dissolve
        bot"Welp. I don't think there's any chance I can make her trust me after that..."
        show boruto sceeming with dissolve
        bot"In which case..."
        show boruto sceeming3 with dissolve
        call borutoevil2 from _call_borutoevil2_14
        call changeHatred(1,"none") from _call_changeHatred_65
        bot"Might as well show her who I really am..."
        hide boruto with dissolve
        $ yoruichiinteractiontaken = True
        $ yoruichi_lustscene1_firsttime = False
        jump ramenkitchenmenu


label yoruichi_lustscene1_repeat:
    bo"F-fuck!" with vpunch
    bot"I've let my condition fester again!"
    show ramenkitchen
    show boruto surprised3 at left
    show yoru shy at right
    with dissolve
    call borutoevil2 from _call_borutoevil2_15
    show boruto bonersurprised2 with dissolve
    bo"F-fuck it! It's not like I haven't been here before"
    show yoru scared2 with dissolve
    yo"N-not this a-again..." with vpunch
    bo"I... told you about my condition, remember?"
    show boruto bonersurprisedred
    show yoru shy2 with dissolve
    bo"F-fuck!" with vpunch
    bo"Do it... take off your s-shirt!"
    show yoru surprised with dissolve
    yo"W-what!?" with vpunch
    bo"Do it... now!"
    show yoru shy with dissolve
    yo"A-are you seriously-"
    call borutoevil3 from _call_borutoevil3_1
    show boruto bonerevil3
    bo"Now, bitch!" with vpunch
    bo"I'll do worse than last time if you don't do as I say!" with vpunch
    show yoru obedient with dissolve
    yo"O-okay but p-please! Don't do anything stupid!"
    hide yoru
    show tits3t at right:
        zoom 0.6
    with Dissolve(1)
    yo"Is this... enough?"
    show boruto bonerevil4:
        easein 1.5 xalign 0.5
    bo"Now kneel!"
    hide tits3t
    show tits misc5t at right with dissolve:
        zoom 0.6
    yo"..."
    show boruto:
        linear 0.3 xalign 0.8
    pause 0.3
    scene black with vpunch
    bo"KNEEL! And look sraight into my eyes!"
    show yorusecretabove0 with dissolve
    bo"That's my bitch..."
    yo"W-why are you doing this again!?"
    bo"Shut the fuck up and sit there while I paint your face white!"
    yo"P-please..."
    $ renpy.sound.play("/audio/soun_fx/clothes_undress.opus", channel="sfx3", loop=False, relative_volume = 0.7)
    show yorusecretintro1 with fade
    yo"Y-you are an animal!"
    show screen yoruichi_lustscene1_screen("yorusecretabove2")
    show expression FocusEffect("idle1", 640, 50, 75, 0.7) with dissolve
    "You can change PoVs using the camera button"
    hide expression FocusEffect with dissolve
    show yorusecretintro0 with dissolve
    yo"It's... monstrous" with vpunch
    show yoruichi_lustscene1_anim with dissolve
    $ renpy.sound.play("/audio/soun_fx/handjob1.opus", channel="sfx3", loop=False, relative_volume = 0.7)
    bo"..."
    yo"*Gasps*"
    bo"Don't worry, this shouldn't take long..."
    bo"You kneeling right there like an obedient little bitch has me excited!"
    hide screen yoruichi_lustscene1_screen
    bo"Take this!" with flash
    menu:
        bo"Take this!"
        "Cum from PoV":
            $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx3", loop=False, relative_volume = 0.4)
            show yorusecretabove3 with flash
            bo"Arrrgh!"
            $ renpy.sound.play("/audio/soun_fx/cum5.opus", channel="sfx3", loop=False, relative_volume = 0.4)
            show yorusecretabove4 with flash
            call decreaselust(50) from _call_decreaselust_42
            bo"Yesss!" with flash
            bo"T-that's it Y-yoru!..."
            $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx3", loop=False, relative_volume = 0.4)
            show yorusecretabove5 with longerflash
            call decreaselust(50) from _call_decreaselust_43
            show screen yoruichi_lustscene1_screen("yorusecretintro3")
            bo"Take it all you whore!" with flash
            $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            bo"*Panting*"
            yo"Y-you..."
            bo"Heh... that was fun!"
            hide screen yoruichi_lustscene1_screen
            jump yoruichi_lustscene1_ending_repeat

        "Cum from side":
            $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx3", loop=False, relative_volume = 0.4)
            show yorusecretintro2 with flash
            call decreaselust(50) from _call_decreaselust_44
            bo"Arrrgh!"
            $ renpy.sound.play("/audio/soun_fx/cum5.opus", channel="sfx3", loop=False, relative_volume = 0.4)
            show yorusecretintro2 with flash
            bo"Yesss!" with flash
            bo"T-that's it Y-yoru!..."
            $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx3", loop=False, relative_volume = 0.4)
            show yorusecretintro3 with longerflash
            call decreaselust(50) from _call_decreaselust_45
            show screen yoruichi_lustscene1_screen("yorusecretabove5")
            bo"Take it all on your pretty face!" with flash
            $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            bo"*Panting*"
            yo"Y-you..."
            bo"Heh... that was fun!"
            hide screen yoruichi_lustscene1_screen
            jump yoruichi_lustscene1_ending_repeat
        



    label yoruichi_lustscene1_ending_repeat:
        scene black with vpunch
        yo"Y-you piece of shit!"
        $ notification ("Yoruichi's relationship changed")
        "Yoruichi's status is now 'Apprehensive'"
        $ yoruichi_relationship = "Apprehensive"
        "You've lost Yoruichi's trust. You can try earning it back by bribing her..."
        yo"You are no better than Obo!"
        yo"Fuck you!" with vpunch
        bo"Yeah yeah, go clean yourself up!"
        "You both take some time to gather yourselves..."
        show ramenkitchen
        show boruto suspicious at left with dissolve
        bot"Should be fine as long as I keep bribing her..."
        show boruto sceeming with dissolve
        bot"Stupid whore..."
        show boruto sceeming3 with dissolve
        call borutoevil2 from _call_borutoevil2_16
        call changeHatred(1,"none") from _call_changeHatred_66
        bot"Desperate for my money... Soon to be desperate for my cum too!"
        hide boruto with dissolve
        $ yoruichiinteractiontaken = True
        $ yoruichi_lustscene1_firsttime = False
        jump ramenkitchenmenu
























label yoruintro_kneel:
$ initialize_replay_defaults()
show yorusecretintro1 with fade
yo"Y-you are an animal!" with vpunch
show screen yoruichi_lustscene1_screen("yorusecretabove2")
show expression FocusEffect("idle1", 640, 50, 75, 0.7) with dissolve
"You can change PoVs using the camera button"
hide expression FocusEffect with dissolve
show yorusecretintro0 with dissolve
show yoruichi_lustscene1_anim with dissolve
$ renpy.sound.play("/audio/soun_fx/handjob1.opus", channel="sfx3", loop=False, relative_volume = 0.7)
bo"..."
yo"*Gasps*" with vpunch
bo"Don't worry, this shouldn't take long..."
bo"You kneeling right there like an obedient little bitch has me excited!"
hide screen yoruichi_lustscene1_screen
bo"Now sit there looking pretty and..." with flash
menu:
    bo"Now sit there looking pretty and..."
    "Cum from PoV":
        $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx3", loop=False, relative_volume = 0.4)
        show yorusecretabove3 with flash
        bo"Arrrgh!"
        $ renpy.sound.play("/audio/soun_fx/cum5.opus", channel="sfx3", loop=False, relative_volume = 0.4)
        show yorusecretabove4 with flash
        call decreaselust(50) from _call_decreaselust_46
        bo"Yesss!" with flash
        bo"T-that's it Y-yoru!..."
        $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx3", loop=False, relative_volume = 0.4)
        show yorusecretabove5 with longerflash
        call decreaselust(50) from _call_decreaselust_47
        show screen yoruichi_lustscene1_screen("yorusecretintro3")
        bo"Take it all you whore!" with flash
        $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
        bo"*Panting*"
        yo"Y-you..."
        bo"Heh... that was fun!"
        hide screen yoruichi_lustscene1_screen
        jump yoruichi_lustscene1_ending_intro

    "Cum from side":
        $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx3", loop=False, relative_volume = 0.4)
        show yorusecretintro2 with flash
        call decreaselust(50) from _call_decreaselust_48
        bo"Arrrgh!"
        $ renpy.sound.play("/audio/soun_fx/cum5.opus", channel="sfx3", loop=False, relative_volume = 0.4)
        show yorusecretintro2 with flash
        bo"Yesss!" with flash
        bo"T-that's it Y-yoru!..."
        $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx3", loop=False, relative_volume = 0.4)
        show yorusecretintro3 with longerflash
        call decreaselust(50) from _call_decreaselust_49
        show screen yoruichi_lustscene1_screen("yorusecretabove5")
        bo"Take it all you whore!" with flash
        $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
        bo"*Panting*"
        yo"Y-you..."
        bo"Heh... that was fun!"
        hide screen yoruichi_lustscene1_screen
        jump yoruichi_lustscene1_ending_intro
    



label yoruichi_lustscene1_ending_intro:
    scene black with vpunch
    yo"Y-you piece of shit!"
    yo"You are no better than Obo!"
    yo"Fuck you!" with vpunch
    "Yoruichi has lost any respect she had for you. She won't talk to you until you find a way to coerce her."
    bo"Yeah yeah, go clean yourself up!"
    bot"Stupid whore..."
    "You both take some time to gather yourselves..."
    jump threecommandsending