label sneak_in_dungeon:
    $ renpy.sound.play("/audio/soun_fx/dungeon_ambient.opus", channel="ambience", loop=True, relative_volume = 1.0)
    $ renpy.sound.play("/audio/soun_fx/dungeon_ambient2.opus", channel="ambience2", loop=True, relative_volume = 1.0)
    $ renpy.sound.play("/audio/soun_fx/intro/bodythud.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    bot"I am going in!" with vpunch
    scene v20_bo_dropin1_1 with dissolve:
        yalign 1.0
    show v20_bo_dropin1_1 with dissolve:
        easein 44 yalign 0.2
    bot"W-what the hell is this place..."
    bot"It reeks of... death and piss!"
    show captives 0 with dissolve:
        yalign 1.0
    show captives 0:
        easein 3 yalign 0.2
    bot"Is that guy d-dead? No wonder it smells like death..."
    hide captives with dissolve
    bot"Is this the kind of place [hin_rel] is held captive in for the measly crime of not paying debts?"
    bot"What bollocks! This place is hell. No proper ruler would ever do something like this..."
    scene black with dissolve
    bot"I'll have the Daimyo pay after I free [hin_rel]!"
    if hinata_captured_eventcounter == 1:
        pass
    elif hinata_captured_eventcounter == 2:
        pass
    else:
        "Meanwhile..."
        jump jumphere_capture_counter_3
    


    show v20_bo_dropin1 with dissolve:
        yalign 0.0
    show v20_bo_dropin1:
        easein 4 yalign 0.7
    bot"H-how much deeper does this place go..."
    bot"And what the hell is up with..."
    show captives 1_2 with dissolve:
        yalign 0.0
    show captives 1_2:
        easein 3 yalign 1.0
    $ renpy.sound.play("/audio/soun_fx/horror.opus", channel="sfx2", loop=False, relative_volume = 0.6)
    bot"...her!" with vpunch
    bot"She looks... d-defiled! M-maybe dead too..."
    hide captives with dissolve
    bot"F-fuck! I better find [hin_rel] fast..."
    scene black with dissolve
    "You head deeper into the dungeons..."
    $ renpy.sound.play("/audio/soun_fx/dream_ambient.opus", channel="sfxstat", loop=True, relative_volume = 0.5)
    "..."
    show bg cell:
        alpha 0.0 yalign 1.0
    show bg cell:
        easein 8 alpha 1.0 yalign 0.5
    bot"Someone's there! I can hear them..."
    bot"..."
    $ renpy.sound.play("/audio/soun_fx/heartbeatlongfast.opus", channel="sfx2", loop=False, relative_volume = 1.2)
    bot"Whatever it is, it's behind this cell, I am sure of it!"
    menu:
        bot"Whatever it is, it's behind this cell, I am sure of it!"
        "...":
            pass
        "...":
            pass
        "...":
            pass
    scene black with dissolve
    play sound"/audio/soun_fx/heartbeat.opus" volume 2.5
    show emptycell_boruto_ntr1:
        alpha 0.0
    show emptycell_boruto_ntr1:
        easein 5 alpha 1.0
    bo"Is someone... th-there?"
    if hinata_captured_eventcounter == 1:
        show v20_hin_captured 1_4 with dissolve:
            yalign 1.0
        show v20_hin_captured 1_4:
            easein 5 yalign 0.3
    else:
        show v20_hin_captured 1_5 with dissolve:
            yalign 1.0
        show v20_hin_captured 1_5:
            easein 5 yalign 0.4
    bo"[hin_rel]...?"
    hin"[bo_name_stutter]...?"
    scene black
    $ renpy.sound.play("/audio/soun_fx/eye4s.opus", channel="sfx1", loop=False, relative_volume = 0.3)
    show emptycell_boruto_ntr1_3 with flash:
        alpha 1.0 yalign 0.3
    show emptycell_boruto_ntr1_3:
        easein 1 alpha 0.0
    $ renpy.sound.play("/audio/soun_fx/crate_break2.opus", channel="sfx3", loop=False, relative_volume = 1.5)
    bo"[hin_rel_stutter.upper()]!"
    scene black with dissolve
    "A sudden power erupted from within you, tearing down the iron bars of [hin_name]'s cell."
    "In almost primal like-movements, you pick her up and make your escape before the guards could respond to the commotion..."
    stop ambience fadeout 1
    stop ambience2 fadeout 1
    scene v20_hinescaped1 with dissolve:
        yalign 0.0
    show v20_hinescaped1:
        easein 4 yalign 1.0
    bo"..."
    "A surge of inexplicable power engulfed your entire being."
    scene black with dissolve
    "With its help, you managed to free [hin_name], and flee the Daimyo's estate in mere moments."
    scene v20_hinescaped1_1 with dissolve:
            yalign 1.0
    show v20_hinescaped1_1:
        easein 5 yalign 0.0
    "You dropped [hin_name] safely to her bedroom, before collapsing in the hallway moments after..."
    scene black
    $ renpy.sound.play("/audio/soun_fx/bodythud.opus", channel="sfx1", loop=False, relative_volume = 1.0)
    "*Body Thuds*" with vpunch
    "Hours pass before you recover your senses. With no recollection of what happened, all you know is that your [hin_rel_mother] is safe and sound."
    
    default hinata_rescued_once = False
    $ hinata_rescued_once = True
    $ hinata_captured = False
    jump action_taken