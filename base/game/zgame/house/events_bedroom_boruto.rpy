
label bedroom_boruto_morning:
    call resetbuttons from _call_resetbuttons_3
    call hideUI from _call_hideUI_7
    if hin_location == "borutobedroom" and him_location == "borutobedroom":
        scene bg bb day with dissolve
        call enabletalk from _call_enabletalk_1
        call enableaction from _call_enableaction_9
    elif hin_location == "borutobedroom":
        scene bg bb day with dissolve
        call enabletalk from _call_enabletalk_2
        call enableaction from _call_enableaction_10
    elif him_location == "borutobedroom":
        scene bg bb day with dissolve
        call enabletalk from _call_enabletalk_3
        call enableaction from _call_enableaction_11
        
    else:
        scene bg bb day with dissolve
        call enableaction from _call_enableaction_12
        call enablestrength from _call_enablestrength

    call showUIhouse from _call_showUIhouse_10
    $ ui.interact()

label bedroom_boruto_evening:
    call hideUI from _call_hideUI_8
    call resetbuttons from _call_resetbuttons_4
    if hin_location == "borutobedroom" and him_location == "borutobedroom":
        scene bg bb day with dissolve
        call enabletalk from _call_enabletalk_4
        call enableaction from _call_enableaction_13
    elif hin_location == "borutobedroom":
        scene bg bb day with dissolve
        call enabletalk from _call_enabletalk_5
        call enableaction from _call_enableaction_14
    elif him_location == "borutobedroom":
        scene bg bb day with dissolve
        call enabletalk from _call_enabletalk_6
        call enableaction from _call_enableaction_15
        
    else:
        scene bg bb day with dissolve
        call enableaction from _call_enableaction_16
        call enablestrength from _call_enablestrength_1

    call showUIhouse from _call_showUIhouse_11
    $ ui.interact()

label bedroom_boruto_night:
    call hideUI from _call_hideUI_9
    call resetbuttons from _call_resetbuttons_5
    if hin_location == "borutobedroom" and him_location == "borutobedroom":
        scene bg bb night with dissolve
        call enabletalk from _call_enabletalk_7
        call enableaction from _call_enableaction_17
    elif hin_location == "borutobedroom":
        scene bg bb night with dissolve
        call enabletalk from _call_enabletalk_8
        call enableaction from _call_enableaction_18
    elif him_location == "borutobedroom":
        scene bg bb night with dissolve
        call enabletalk from _call_enabletalk_9
        call enableaction from _call_enableaction_19
        
    else:
        scene bg bb night with dissolve
        call enableaction from _call_enableaction_20
        # if day_part == 1 or day_part == 2 or day_part == 3:
            # call enablestrength from _call_enablestrength_2

    call showUIhouse from _call_showUIhouse_12
    $ ui.interact()


label borutobedroomntalkmenu:
    call hideUI from _call_hideUI_10
    menu:
        "..."
        "Talk to [hin_name]" if hin_location == "borutobedroom":
            bo"a"
            call showUIhouse from _call_showUIhouse_13
            $ ui.interact()
        "Talk to [him_name]" if him_location == "borutobedroom":
            bo"a"
            call showUIhouse from _call_showUIhouse_14
            $ ui.interact()
        "Return":
            call showUIhouse from _call_showUIhouse_15
            $ ui.interact()


label borutobedroomactionmenu:
    call hideUI from _call_hideUI_11
    if day_part == 4:
        menu borutonormalsleepmenu:
            "..."
            "Sleep until tomorrow":
                bot"At last, my favorite past-time activity..."
                scene black with dissolve
                jump action_taken

            "Visit Kushina" if day_part == 4 and kushina_plan_unlocked == True and day_number > 13:
                if nochoice_made_yet == True:
                    jump kuramachoice_dream_repeat
                elif chosen_hate_path:
                    jump kushinavisit_hate_repeat
                elif chosen_love_path:
                    jump kushinavisit_love_repeat
                else:
                    jump kuramachoice_dream
            "Visit Kushina" if day_part == 4 and kushina_plan_unlocked == False and day_number > 13:
                jump kuramachoice_dream
            "Fantasize/Dream" if day_part == 4:
                
                bot"I need a release..."
                if fantasizetutorial == False:
                    default fantasizetutorial = False
                    $ fantasizetutorial = True
                    dev"You can use the 'Fantasize' mechanic to decrease your Lust whenever you need to."
                    dev"This section of the game will feature some CG that are either unfinished or suffer from irregularities!"
                    dev"You can attribute any abnormalities to the MC's lackluster imagination (Hehe)"
                menu fantasizemenu:
                    dev"Reminder that there might be unfinished CG in here!"
                    "[hin_name]":
                        bot"I can't stop thinking about [hin_rel]..."
                        jump hinata_fantasize

                    "[him_name]":
                        bot"To think that even [him_name] occupies my thoughts... How far have I fallen?"
                        $ himpantiesinv = inventory.find_item_by_name(f"Panties")
                        $ himpantiscumininv = inventory.find_item_by_name(f"Soiled Panties")
                        jump himawari_fantasize

                    "Dream" if day_number < 7:
                        "Available after Day 7"
                        jump fantasizemenu

                    "Dream" if day_number >= 7:
                        bot"I've been told that If you think about something before you sleep, you'll dream about it..."
                        stop music fadeout 1
                        bot"Might as well think of big booty Kunoichi bitches! Hehe..."
                        $ renpy.sound.play("/audio/ost/sleep.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                        scene black with fade
                        "You fall into a deep slumber..."
                        show dreamvignette zorder 100 with dissolve
                        "A lucid dream slowly takes shape..."
                        play music"/audio/ost/dreaming.opus" volume 0.5
                        default disablentrwarning = False
                        if disablentrwarning == False:
                            "Would you like to disable optional NTR content?"
                            $ disablentrwarning = True
                            menu:
                                "Would you like to disable optional NTR content?"
                                "Disable optional NTR":
                                    $ persistent.netorareoptional = True
                                    "Optional NTR content is now disabled."
                                    "Keep in mind that given the circumstances of the Shinobi world, your actions may still lead to avoidable NTR!"
                                    "Act wisely..."
                                    pass
                                "Enable optional NTR":
                                    $ persistent.netorareoptional = False
                                    pass
                                
                        menu dreammenu:
                            "A lucid dream slowly takes shape..."

                            "Succubus of the Lake" if tenten_pendant_found == True:
                                jump lake_succubus

                            "[na_name] is... back?" if persistent.netorareoptional == False:
                                label replay_narutoisback:
                                $ initialize_replay_defaults()
                                $ renpy.sound.play("/audio/soun_fx/wind3.opus", channel="sfx3", loop=False, relative_volume = 0.8)
                                show bg day at brightreveal:
                                    zoom 0.70 
                                show boruto normal at center,brightreveal
                                with flash
                                bot"..."
                                bot"Uh, what was I doing here again? My mind is... hazy..."
                                $ renpy.sound.play("/audio/soun_fx/sexslaps2.opus", channel="sfxstat", loop=False, relative_volume = 0.5,fadein=4)
                                $ renpy.sound.play("/audio/soun_fx/femalemoan1.opus", channel="sfx1", loop=False, relative_volume = 0.9,fadein=4)
                                show boruto embarassed with dissolve
                                bot"Oh r-right! I was about to take another nap, hehe!"
                                hide boruto with dissolve
                                bot"Here I come, my beloved bed!"
                                "Muffled sounds echo through the walls... Soft moans mixed with rhythmic movements..." with vpunch
                                "... Ahh... *Plap, Plap*...Y-yes..." with vpunch
                                $ renpy.sound.play("/audio/soun_fx/sexslaps1.opus", channel="sfx2", loop=False, relative_volume = 0.6,fadein=4)
                                $ renpy.sound.play("/audio/soun_fx/femalemoan2.opus", channel="sfx1", loop=False, relative_volume = 1.0,fadein=4)
                                show boruto surprised3 at center with dissolve
                                $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx3", loop=False, relative_volume = 1.2)
                                bot"Those sounds... A-are they're coming from [hin_rel]'s bedroom!?"
                                show boruto surprised2 with dissolve
                                bot"Does that mean... [na_rel] is back!?" with vpunch
                                bot"And w-why are they... so loud!? S-shameless..." with vpunch
                                show boruto worried with dissolve
                                bot"But how comes I haven't seen [na_rel]..."
                                show boruto:
                                    easein 2 xpos 1700 alpha 0.0
                                $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx3", loop=False, relative_volume = 1.4)
                                bot"A little peek wouldn't hurt... just to make sure everything's alright..."
                                scene black with dissolve
                                show hima_end1:
                                    alpha 0.0
                                show hima_end1:
                                    linear 10 zoom 1.3 xalign 0.5 yalign 0.5 alpha 1.0
                                $ renpy.sound.play("/audio/soun_fx/sexslaps2.opus", channel="sfxstat", loop=False, relative_volume = 0.5,fadein=4)
                                $ renpy.sound.play("/audio/soun_fx/femalemoan1.opus", channel="sfx1", loop=False, relative_volume = 0.9,fadein=4)
                                bot"Though I suppose if I had someone like [hin_rel] waiting for me after being away for so long, I might have... other priorities too!"
                                hin"S-sun... Sun!" with vpunch
                                $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx3", loop=False, relative_volume = 1.6)
                                bot"Sun? What the hell does the sun have to do with a-anything..."
                                $ renpy.sound.play("/audio/soun_fx/sexslaps3.opus", channel="sfxstat", loop=False, relative_volume = 0.5,fadein=4)
                                $ renpy.sound.play("/audio/soun_fx/femalemoan2.opus", channel="sfx1", loop=False, relative_volume = 0.9,fadein=4)
                                na"I always knew this is what you w-were, [hin_name]!" with vpunch
                                hin"J-just like that... More, M-MORE! S-sun..." with vpunch
                                $ renpy.sound.play("/audio/soun_fx/heartbeatlong.opus", channel="sfx2", loop=False, relative_volume = 0.9,fadein=2)
                                
                                bot"*Gulp* They sure enjoy the sun... for s-some reason..."
                                show hima_end1 with dissolve:
                                    zoom 1.4 xalign 0.5 yalign 0.5 alpha 1.0
                                bot"W-what the hell is going on in there anyway..." with vpunch
                                menu:
                                    bot"W-what the hell is going on in there anyway..."
                                    "Take a peek...":
                                        pass
                                show hima_end1 with dissolve:
                                    zoom 1.6 xalign 0.5 yalign 0.5 alpha 1.0
                                $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx3", loop=False, relative_volume = 1.6)
                                bot"My curiosity is killing me..."
                                show hima_end1 with dissolve:
                                    zoom 1.65 xalign 0.5 yalign 0.5 alpha 1.0
                                $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx3", loop=False, relative_volume = 2.0)
                                bot"Just to see w-what's going on..."
                                show hima_end1 with dissolve:
                                    zoom 1.7 xalign 0.5 yalign 0.5 alpha 1.0
                                $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx3", loop=False, relative_volume = 2.2)
                                bot"Just one peek... Just to be certain everything's alright..."
                                bot"."
                                show hima_end1 with dissolve:
                                    zoom 1.75 xalign 0.5 yalign 0.5 alpha 1.0
                                $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx3", loop=False, relative_volume = 2.6)
                                bot".."
                                show hima_end1 with dissolve:
                                    zoom 1.8 xalign 0.5 yalign 0.5 alpha 1.0
                                $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx3", loop=False, relative_volume = 2.8)
                                bot"..."
                                scene black with dissolve
                                $ renpy.sound.play("/audio/soun_fx/horror.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                                show screen peeking1024("hinata_ndream_start1")
                                show screen peaking_overlay("bgp peak_updown")
                                show layer screens at dizzyflash
                                with longerflash
                                call showscrollingimage from _call_showscrollingimage_80
                                bot"M...[hin_rel]!? Who the..." with vpunch
                                bot"W-who the fuck is that!" with vpunch
                                bot"Is she... c-cheating on [na_rel]!?" with vpunch
                                hin"*Panting* W-why did you s-stop... S-sun?"
                                "Sun" "I want you to beg for it, [hin_name]..."
                                hin"W-what!?" with vpunch
                                "Sun" "Do it, [hin_name]... Beg for my cock to keep drilling your desperate pussy!" with vpunch
                                bot"[hin_rel_stutter] would never do such a thing..."
                                hin"D-don't say such vulgar things... P-please!"
                                "Sun" "Shall we stop here then?"
                                hin"{size=*0.7}*Heavy breathing* N-no... P-please... D-dont stop!{/size}"
                                $ renpy.sound.play("/audio/soun_fx/pushitin2.opus", channel="sfx2", loop=False, relative_volume = 1.2)
                                $ renpy.sound.play("/audio/soun_fx/femalegrunt1.opus", channel="sfx3", loop=False, relative_volume = 0.8)
                                show screen peeking1024("hinata_ndream_start1_1") with flash
                                "Sun" "Don't you worry, [hin_name]..." with vpunch
                                $ renpy.sound.play("/audio/soun_fx/sexslaps1.opus", channel="sfxstat", loop=False, relative_volume = 0.5,fadein=1)
                                $ renpy.sound.play("/audio/soun_fx/femalemoan1.opus", channel="sfx1", loop=False, relative_volume = 0.9,fadein=1)
                                show screen peeking1024("hinata_ndreamnoturn_anim1") with dissolve
                                "Sun" "You'll be getting it for the rest of the day!"
                                bot"This can't be real... [hin_rel]..."
                                "Sun" "I've forgotten how amazing you Konoha women are at working our cocks! You put our Kumo girls to shame with your passion..."
                                "Sun" "The way you work a man... Your fair skin, your beauty, your cravings even! You are beyond comparisson!"
                                $ renpy.sound.play("/audio/soun_fx/sexslaps2.opus", channel="sfxstat", loop=False, relative_volume = 0.5,fadein=1)
                                $ renpy.sound.play("/audio/soun_fx/femalemoan2.opus", channel="sfx1", loop=False, relative_volume = 0.9,fadein=1)
                                $ renpy.sound.play("/audio/soun_fx/bedcreak.opus", channel="sfx2", loop=False, relative_volume = 0.6,fadein=1)
                                show screen peeking1024("hinata_ndreamnoturn_anim2") with dissolve
                                hin"Be quiet, Sun! Just... don't stop! Please, h-harder!"
                                "The bed creaks rhythmically every time Sun thrusts faster, harder and deeper into [hin_name]..."
                                bot"It must b-be a... n-nightmare..."
                                "Sun" "You really are the best [hin_name]..."
                                "Sun" "Mind as sharp as a kunai, beautiful as a flower, and a body as curvy as a whore's! But more importantly..."
                                "Sun" "So lusting... So desperate for Kumo cock that you'd betray even your husband's trust!" with vpunch
                                "Sun" "While [na_name] is out negotiating with my father, his precious wife is getting railed by his son..."
                                "Sun" "How perverse is that, 'Lady' [hin_name]. How scandalous..."
                                "Sun" "To be riding my cock behind your husband's back! What would he think of your depravity?"
                                $ renpy.sound.play("/audio/soun_fx/sexslaps3.opus", channel="sfxstat", loop=False, relative_volume = 0.5,fadein=1)
                                $ renpy.sound.play("/audio/soun_fx/femalemoan2.opus", channel="sfx1", loop=False, relative_volume = 0.9,fadein=1)
                                $ renpy.sound.play("/audio/soun_fx/bedcreak.opus", channel="sfx2", loop=False, relative_volume = 0.6,fadein=1)
                                hin"S-shut up, Shut up! *Loud moans*"
                                bot"This can't be r-real..."
                                bot"It f-feels like I am f-floating, like I am not really here..."
                                call hidescrollingimage from _call_hidescrollingimage_79
                                hide screen peeking1024
                                hide screen peaking_overlay
                                scene black
                                with dissolve
                                scene borutontr0 with dissolve:
                                        zoom 1.6 xalign 0.5 yalign 0.0
                                $ renpy.sound.play("/audio/soun_fx/sexslaps3.opus", channel="sfxstat", loop=False, relative_volume = 0.25,fadein=2)
                                $ renpy.sound.play("/audio/soun_fx/femalemoan2.opus", channel="sfx1", loop=False, relative_volume = 0.4,fadein=2)
                                $ renpy.sound.play("/audio/soun_fx/bedcreak.opus", channel="sfx2", loop=False, relative_volume = 0.3,fadein=2)
                                bot"If t-this isn't real, then..."
                                menu:
                                    bot"If t-this isn't real, then..."
                                    "Open the door and confront them!":
                                        show borutontr0 with dissolve:
                                            zoom 1.65 xalign 0.5 yalign 0.0
                                        bot"I... I have to confirm my s-suspicions!" with vpunch
                                        show borutontr1_1 with dissolve:
                                            zoom 1.7 xalign 0.5 yalign 0.0
                                        bot"[hin_rel]..."
                                        show borutontr1_1 with dissolve:
                                            zoom 1.75 xalign 0.5 yalign 0.0
                                        bot"T-this isn't y-you, right? This isn't real..."
                                        show borutontr1_1 with dissolve:
                                            zoom 1.8 xalign 0.5 yalign 0.0
                                        $ renpy.sound.play("/audio/soun_fx/wind3.opus", channel="sfxstat", loop=False, relative_volume = 0.6)
                                        $ renpy.sound.play("/audio/soun_fx/dooropen.opus", channel="sfx1", loop=False, relative_volume = 0.6)
                                        $ renpy.sound.play("/audio/soun_fx/wakeup.opus", channel="sfx3", loop=False, relative_volume = 1.2)
                                        with Shake((0, 0, 0, 0), 2, dist=10, peak_time=1.4, smoothness=50)
                                        show hinata_ndreamnoturn_anim2 at brightreveal:
                                            yalign 0.9 zoom 1.25 xalign 0.5
                                        $ renpy.sound.play("/audio/soun_fx/sexslaps3.opus", channel="sfxstat", loop=False, relative_volume = 0.5,fadein=1)
                                        $ renpy.sound.play("/audio/soun_fx/femalemoan2.opus", channel="sfx1", loop=False, relative_volume = 0.9,fadein=1)
                                        $ renpy.sound.play("/audio/soun_fx/bedcreak.opus", channel="sfx2", loop=False, relative_volume = 0.6,fadein=1)
                                        bot"I am s-sure... of it!"
                                        show screen parallax1280("hinata_ndreamnoturn_anim2",1.27,0.6,False) with dissolve
                                        call showscrollingimage from _call_showscrollingimage_81
                                        bot"[hin_rel]! W-what are you..." with vpunch
                                        bot"No r-reaction... She just keeps... going..."
                                        bot"What if I t-try to... t-touch her?"
                                        "Your immaterial presence flows through the atmosphere, passing through their bodies..."
                                        bot"It really is j-just a nightmare!"
                                        bot"And yet it feels so vivid, so real..."
                                        bot"W-why would I dream of s-something like this..."
                                        bot"How could [hin_rel] ever act like this..."
                                        $ secretlymasturbate = False
                                        menu:
                                            bot"How could [hin_rel] ever act like this..."
                                            "Wake up... Wake up!":
                                                bot"If it's a n-nightmare, then..."
                                                hide screen peeking1024
                                                hide screen peaking_overlay
                                                hide scrollingimage onlayer screens
                                                $ renpy.sound.play("/audio/soun_fx/wakeup.opus", channel="sfx3", loop=False, relative_volume = 1.2)
                                                with Shake((0, 0, 0, 0), 2, dist=10, peak_time=1.4, smoothness=50)
                                                $ playmusic("/audio/ost/house2.opus", 0.5)
                                                hide screen parallax1280
                                                scene bg bb intro at brightreveal:
                                                    matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 
                                                with longerflash
                                                with Shake((0, 0, 0, 0), 1, dist=20, peak_time=0.8, smoothness=50)
                                                show boruto box2surprised with Dissolve(1):
                                                    blur 30
                                                show boruto box2surprised with Dissolve(2):
                                                    easein 2 blur 0
                                                $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                                                bot"*Rapid breathing* W-what just... happened?" with vpunch
                                                bot"I... I feel like I've had the worst dream ever, but I can't recall anything..."
                                                bot"Am I... Am I losing my mind?"
                                                hide boruto with dissolve
                                                bot"Better put on some clothes and get on with my day..."
                                                scene black with dissolve
                                                bot"Can't even enjoy some sleep with this damned condition *Sigh...*"
                                                jump action_taken
                                            "Keep watching...":
                                                pass
                                            


                                    "{color=[hatredcolor]}Resentfully masturbate at her infidelity!{/color}":
                                        bot"I... W-why would [hin_rel] do something like this..." with vpunch
                                        show borutontr1_1 with dissolve:
                                            zoom 1.7 xalign 0.5 yalign 0.0
                                        bot"And w-why do I..."
                                        $ renpy.sound.play("/audio/soun_fx/sexslaps3.opus", channel="sfxstat", loop=False, relative_volume = 0.25,fadein=2)
                                        $ renpy.sound.play("/audio/soun_fx/femalemoan2.opus", channel="sfx1", loop=False, relative_volume = 0.4,fadein=2)
                                        $ renpy.sound.play("/audio/soun_fx/bedcreak.opus", channel="sfx2", loop=False, relative_volume = 0.3,fadein=2)
                                        call increaselust(50) from _call_increaselust_150
                                        $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx3", loop=False, relative_volume = 0.8)
                                        with fade
                                        show borutontr1_1 with dissolve:
                                            easein 1 zoom 1.2 xalign 0.5 yalign 1.0
                                        bot"Why do I f-feel like this!" with vpunch
                                        $ renpy.sound.play("/audio/soun_fx/jerkoff2.opus", channel="sfx3", loop=False, relative_volume = 0.2)
                                        show borutontr1 with fade:
                                            zoom 1.2 xalign 0.5 yalign 1.0
                                        show borutontr1 with dissolve:
                                            easein 1 zoom 1.2 xalign 0.5 yalign 0.0
                                        bot"Why would you do this, [hin_rel]..."
                                        $ renpy.sound.play("/audio/soun_fx/jerkoff2.opus", channel="sfx3", loop=False, relative_volume = 0.2)
                                        scene borutontr1_1 with dissolve:
                                            zoom 1.3 xalign 0.5 yalign 0.0
                                        show borutontr1_1:
                                            easein 5 zoom 1.4
                                        bot"I thought that..."
                                        bot"I thought that you loved [na_rel], that you..."
                                        $ renpy.sound.play("/audio/soun_fx/jerkoff1.opus", channel="sfx3", loop=False, relative_volume = 0.2)
                                        bot"T-that you loved m-me!" with vpunch 
                                        show borutontr1_2 with dissolve:
                                            zoom 1.5 xalign 0.5 yalign 0.0
                                        bot"Y-you..."
                                        $ renpy.sound.play("/audio/soun_fx/jerkoff2.opus", channel="sfx3", loop=False, relative_volume = 0.2)
                                        show borutontr1_2 at dizzyflashshort
                                        call changeHatred(1,"ntrdream1") from _call_changeHatred_131
                                        bot"Y-you infidel w-whore!" with vpunch
                                        $ renpy.sound.play("/audio/soun_fx/sexslaps3.opus", channel="sfxstat", loop=False, relative_volume = 0.5,fadein=1)
                                        $ renpy.sound.play("/audio/soun_fx/femalemoan2.opus", channel="sfx1", loop=False, relative_volume = 0.9,fadein=1)
                                        $ renpy.sound.play("/audio/soun_fx/bedcreak.opus", channel="sfx2", loop=False, relative_volume = 0.6,fadein=1)
                                        scene black
                                        hide screen peeking1024
                                        hide screen peaking_overlay
                                        show screen peeking1024("hinata_ndreamnoturn_anim2")
                                        show screen peaking_overlay("bgp peak_updown")
                                        with dissolve
                                        call showscrollingimage from _call_showscrollingimage_82
                                        
                                        bot"You will p-pay for this, [hin_rel_stutter]!"
                                        default secretlymasturbate = False
                                        $ secretlymasturbate = True

                                    

                                "Sun" "What would the village think of their beloved Hokage's wife now?"
                                hin"S-stop it! Don't say such t-things to a lady!"
                                $ renpy.sound.play("/audio/soun_fx/sexslaps2.opus", channel="sfxstat", loop=False, relative_volume = 0.5,fadein=1)
                                $ renpy.sound.play("/audio/soun_fx/femalemoan1.opus", channel="sfx1", loop=False, relative_volume = 0.9,fadein=1)
                                $ renpy.sound.play("/audio/soun_fx/bedcreak.opus", channel="sfx2", loop=False, relative_volume = 0.6,fadein=1)
                                "Sun" "A Lady? No... you're something else entirely..."
                                "Sun" "You are just a desperate, cock-craving slut!" with flash
                                hin"N-no, no... I am only doing this b-because-"
                                "Sun" "Turn around, face me! Look into my eyes while you try to justify your infidelity..." with vpunch
                                $ renpy.sound.play("/audio/soun_fx/sexslaps1.opus", channel="sfxstat", loop=False, relative_volume = 0.5,fadein=1)
                                $ renpy.sound.play("/audio/soun_fx/femalemoan2.opus", channel="sfx1", loop=False, relative_volume = 0.9,fadein=1)
                                $ renpy.sound.play("/audio/soun_fx/bedcreak.opus", channel="sfx2", loop=False, relative_volume = 0.6,fadein=1)
                                if secretlymasturbate == True:
                                    show screen peeking1024("hinata_ndream_turnanim1") with dissolve
                                else:
                                    show screen parallax1280("hinata_ndream_turnanim1",1.27,0.6,False) with dissolve
                                "Sun" "Tell me then, [hin_name]... Why are you letting me stretch your pussy like a common whore would!"
                                hin"It's been... it's been so long since [na_name]..."
                                hin"He's been gone for m-months and I... I..."
                                hin"I've never felt such intense-" with vpunch
                                "Sun" "Ahhh... There it is, the truth emerges!"
                                "Sun" "The 'great' Hokage's prick was never enough to satisfy someone as needy as you... Was it?"
                                hin "N-no...! That's not true...!"
                                "Sun" "So you had to jump on the first cock that came knocking... Now you are addicted to what a real man feels like!"
                                hin"*Desperate Moans* Y-you are wrong!" with vpunch
                                if secretlymasturbate == True:
                                    show screen peeking1024("hinata_ndream_letgo") with fade
                                else:
                                    show screen parallax1280("hinata_ndream_letgo",1.27,0.6,False) with dissolve
                                "Sun" "I am wrong, you say?"
                                "Sun" "Here I'll prove it to you..."
                                "The man stopped his visicous thrusting and instead, raised [hin_name]'s hips an inch away from losing grip of his cock..."
                                hin"W-why did... *Heavy breathing* W-why did you... s-stop!"
                                "Sun" "You said I am wrong didn't you?"
                                hin"...Y-you are!" with vpunch
                                "Sun" "Then you wouldn't mind raising your hips an inch further and losing grip of my cock, right?"
                                hin"..."
                                "Sun" "Heh... Your silence is betrayed by how tight your pussy is gripping me, even if it's just the tip of my cock!"
                                "Sun" "Here's the deal, [hin_name]... I'll be counting to three..."
                                "Sun" "On the count of three, I'll let go of your legs..."
                                "Sun" "You can either get off me, in which case I'll dress up, be on my way and promise that you'll never see me again..."
                                "Sun" "Or..."
                                "Sun" "You'll start bouncing on my cock like the depraved whore that you really are!" with vpunch
                                hin"I a-am not a w-whore! Y-you..." with vpunch
                                "Sun" "One..." with vpunch
                                hin"P-please..."
                                "Sun" "Two!" with vpunch
                                hin"..."
                                if secretlymasturbate == True:
                                    show screen peeking1024("hinata_ndream_turnanim2") with dissolve
                                else:
                                    show screen parallax1280("hinata_ndream_turnanim2",1.27,0.6,False) with dissolve
                                $ renpy.sound.play("/audio/soun_fx/sexslaps2.opus", channel="sfxstat", loop=False, relative_volume = 0.5,fadein=1)
                                $ renpy.sound.play("/audio/soun_fx/femalemoan2.opus", channel="sfx1", loop=False, relative_volume = 0.9,fadein=1)
                                $ renpy.sound.play("/audio/soun_fx/bedcreak.opus", channel="sfx2", loop=False, relative_volume = 0.6,fadein=1)
                                "Sun" "That's it, you bitch! Give in to your true desires..." with vpunch
                                "Sun" "Look at how you willingly raise and drop your hips! Just like a cock-hungry whore would..."
                                hin"S-shut up... *Moans*... shut up!" with vpunch
                                if secretlymasturbate == True:
                                    bot"[hin_rel] really is a fucking whore!"
                                    bot"I won't stand for this any m-more!"
                                    bot"Tonight I'll make her..."
                                    bot"No, I'll f-force her to service my cock!"
                                    bot"How dare she cheat on my f-feelings for her..."
                                "Sun" "Don't you worry, [hin_name]..."
                                "Sun" "Soon enough, your pussy will crave only for what I can give you..."
                                "Sun" "From now on..."
                                if secretlymasturbate == True:
                                    show screen peeking1024("hinata_ndream_anim2_cum1")
                                else:
                                    show screen parallax1280("hinata_ndream_anim2_cum1",1.27,0.6,False) with dissolve
                                $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                                "Sun" "I'll be emptying my balls in you whenever your husband is away..." with flash
                                if secretlymasturbate == True:
                                    show screen peeking1024("hinata_ndream_anim2_cum2")
                                else:
                                    show screen parallax1280("hinata_ndream_anim2_cum2",1.27,0.6,False) with dissolve
                                $ renpy.sound.play("/audio/soun_fx/cum11.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                                "Sun" "I'll tend to your needs, and you'll service mine... Do we have an arrangement?" with flash
                                hin"N-no... *Between heavy breaths* We..."
                                if secretlymasturbate == True:
                                    show screen peeking1024("hinata_ndream_turnanim3") with dissolve
                                else:
                                    show screen parallax1280("hinata_ndream_turnanim3",1.27,0.6,False) with dissolve
                                $ renpy.sound.play("/audio/soun_fx/sexslaps3.opus", channel="sfxstat", loop=False, relative_volume = 0.5,fadein=1)
                                $ renpy.sound.play("/audio/soun_fx/femalemoan2.opus", channel="sfx1", loop=False, relative_volume = 0.9,fadein=1)
                                $ renpy.sound.play("/audio/soun_fx/bedcreak.opus", channel="sfx2", loop=False, relative_volume = 0.6,fadein=1)
                                hin"We do n-not! Aaah...Ahh-ah! *Moans*"
                                "Sun" "Bwahaha! Even when your pussy is brimming with my semen, you try and deny me..."
                                "Sun" "And yet, you keep on bouncing like a bitch in heat!" with vpunch
                                "Sun" "You Konoha women are something else..."
                                "Sun" "Let alone the Hokage's wife! You are truly one of a kind, [hin_name]!"
                                $ renpy.sound.play("/audio/soun_fx/sexslaps1.opus", channel="sfxstat", loop=False, relative_volume = 0.5,fadein=1)
                                $ renpy.sound.play("/audio/soun_fx/bedcreak.opus", channel="sfx2", loop=False, relative_volume = 0.6,fadein=1)
                                hin"S-shut up, SHUT UP!! Aaah...Ahh-ah! *Moans*" with flash
                                $ renpy.sound.play("/audio/soun_fx/femaleorgasm.opus", channel="sfx1", loop=False, relative_volume = 0.7,fadein=1)
                                hin"*Orgasmic Moans* Aaah!? ♡ Mmhmhm!!♡" with flash
                                $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                                $ renpy.sound.stop(channel="sfxstat", fadeout=1.0)
                                if secretlymasturbate == True:
                                    show screen peeking1024("hinata_ndream_anim2_cum2") with dissolve
                                else:
                                    show screen parallax1280("hinata_ndream_anim2_cum2",1.27,0.6,False) with dissolve
                                hin"♡ ♡ ♡ Aaaaaaaaaaaaraah!??♡ ♡ ♡ " with longerflash
                                if secretlymasturbate == True:
                                    bot"What a slut..."
                                    bot"She might even jump on my cock the second I ask her too. And even if she doesn't..."
                                    bot"I'll simply have to blackmail her! Cheating cunt..."
                                "Sun" "You can pretend as much as you want, but I can see the truth in your wanting eyes..."
                                "Sun" "Look at you trembling with my cock still inside of you..."
                                "Sun" "You've just had the greatest orgasm of your life, didn't you?"
                                hin"*Heavy breathing* N-no... I...-"
                                "Sun" "Get off my cock, woman... I have business to attend to!" with vpunch
                                if secretlymasturbate == True:
                                    show screen peeking1024("hinata_ndream_end1") with dissolve
                                else:
                                    show screen parallax1280("hinata_ndream_end1",1.27,0.6,False) with dissolve
                                hin"...T-this was *Panting*..."
                                hin"This was the last t-time... I'll ever see you, Sun..."
                                "Sun" "The last time, you say?"
                                hin"I can't be doing this with y-you..."
                                hin"W-what would everyone think of-"
                                "Sun" "This is only the beginning, [hin_name]..." with vpunch
                                $ renpy.sound.play("/audio/soun_fx/jutsu.opus", channel="sfx2", loop=False, relative_volume = 0.9)
                                $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx3", loop=False, relative_volume = 0.1)
                                if secretlymasturbate == True:
                                    show screen peeking1024("hinata_ndream_end1_1") with flash
                                else:
                                    show screen parallax1280("hinata_ndream_end1_1",1.27,0.6,False) with dissolve
                                "Sun" "This will all but guarantee it!" with flash
                                hin"What did you... do to m-me!" with vpunch
                                if secretlymasturbate == True:
                                    show screen peeking1024("hinata_ndream_end1_2") with flash
                                else:
                                    show screen parallax1280("hinata_ndream_end1_2",1.27,0.6,False) with dissolve
                                hin"My w-womb... It's t-tingling! It feels... strange..."
                                "Sun" "Don't worry about that, [hin_name]..."
                                $ renpy.sound.play("/audio/soun_fx/intro/evilmenlaugh.opus", channel="sfx2", loop=False, relative_volume = 0.1)
                                "Sun" "You now bear the mark of Kumo..."
                                "Sun" "Your womb shall reject your brethren's seed... But it will gladly embrace mine!"

                                hide screen peeking1024
                                hide screen peaking_overlay
                                hide scrollingimage onlayer screens
                                if secretlymasturbate == False:
                                    $ renpy.sound.play("/audio/soun_fx/wakeup.opus", channel="sfx3", loop=False, relative_volume = 1.2)
                                    with Shake((0, 0, 0, 0), 2, dist=10, peak_time=1.4, smoothness=50)
                                    $ playmusic("/audio/ost/house2.opus", 0.5)
                                    hide screen parallax1280
                                    scene bg bb intro at brightreveal:
                                        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 
                                    with longerflash
                                    with Shake((0, 0, 0, 0), 1, dist=20, peak_time=0.8, smoothness=50)
                                    show boruto box2surprised with Dissolve(1):
                                        blur 30
                                    show boruto box2surprised with Dissolve(2):
                                        easein 2 blur 0
                                    $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                                    bot"*Rapid breathing* W-what just... happened?" with vpunch
                                    bot"I... I feel like I've had the worst dream ever, but I can't recall anything..."
                                    bot"Am I... Am I losing my mind?"
                                    hide boruto with dissolve
                                    bot"Better put on some clothes and get on with my day..."
                                    scene black with dissolve
                                    bot"Can't even enjoy some sleep with this damned condition *Sigh...*"
                                    $ renpy.end_replay()
                                    jump action_taken

                                $ renpy.sound.play("/audio/soun_fx/jerkoff1.opus", channel="sfx3", loop=False, relative_volume = 0.2)
                                show borutontr1_2:
                                    zoom 1.5 xalign 0.5 yalign 1.0
                                with dissolve
                                bot"[hin_rel]... Y-you..."
                                $ renpy.sound.play("/audio/soun_fx/jerkoff2.opus", channel="sfx3", loop=False, relative_volume = 0.2)
                                show borutontr1_2:
                                    easein 0.5 xalign 0.5 yalign 0.0
                                bot"You b-betrayed [na_rel]... You betrayed ME! Y-you stupid fucking bitch!" with vpunch
                                show borutontr1_2 at dizzyflashshort
                                $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                                bot"How could you..." with flash
                                $ renpy.sound.play("/audio/soun_fx/wakeup.opus", channel="sfx3", loop=False, relative_volume = 1.2)
                                with Shake((0, 0, 0, 0), 2, dist=10, peak_time=1.4, smoothness=50)
                                $ playmusic("/audio/ost/house2.opus", 0.5)
                                scene bg bb intro at brightreveal:
                                    matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 
                                with longerflash
                                with Shake((0, 0, 0, 0), 1, dist=20, peak_time=0.8, smoothness=50)
                                show boruto box2surprised with Dissolve(1):
                                    blur 30
                                show boruto box2surprised with Dissolve(2):
                                    easein 2 blur 0
                                $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                                bot"*Rapid breathing* W-what just... happened?" with vpunch
                                bot"I... I feel like I've had the worst dream ever, but I can't recall anything..."
                                bot"Am I... Am I losing my mind?"
                                call decreaselust(50) from _call_decreaselust_91
                                bot"Fuck! I even soiled my boxers in my sleep..."
                                hide boruto with dissolve
                                bot"Better put on some clothes and get on with my day..."
                                scene black with dissolve
                                bot"Can't even enjoy some sleep with this damned condition *Sigh...*"
                                $ renpy.end_replay()
                                jump action_taken
                            "[na_name] is... back?" if persistent.netorareoptional == True:
                                label narutoisback_nonntr:
                                $ initialize_replay_defaults()
                                $ renpy.sound.play("/audio/soun_fx/wind3.opus", channel="sfx3", loop=False, relative_volume = 0.8)
                                show bg day at brightreveal:
                                    zoom 0.70 
                                show boruto normal at center,brightreveal
                                with flash
                                bot"..."
                                bot"Uh, what was I doing here again? My mind is... hazy..."
                                $ renpy.sound.play("/audio/soun_fx/sexslaps2.opus", channel="sfxstat", loop=False, relative_volume = 0.5,fadein=4)
                                $ renpy.sound.play("/audio/soun_fx/femalemoan1.opus", channel="sfx1", loop=False, relative_volume = 0.9,fadein=4)
                                show boruto embarassed with dissolve
                                bot"Oh r-right! I was about to take another nap, hehe!"
                                hide boruto with dissolve
                                bot"Here I come, my beloved bed!"
                                "Muffled sounds echo through the walls... Soft moans mixed with rhythmic movements..." with vpunch
                                "... Ahh... *Plap, Plap*...Y-yes..." with vpunch
                                $ renpy.sound.play("/audio/soun_fx/sexslaps1.opus", channel="sfx2", loop=False, relative_volume = 0.6,fadein=4)
                                $ renpy.sound.play("/audio/soun_fx/femalemoan2.opus", channel="sfx1", loop=False, relative_volume = 1.0,fadein=4)
                                show boruto surprised3 at center with dissolve
                                $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx3", loop=False, relative_volume = 1.2)
                                bot"Those sounds... A-are they're coming from [hin_rel]'s bedroom!?"
                                show boruto surprised2 with dissolve
                                bot"Does that mean... [na_rel] is back!?" with vpunch
                                bot"And w-why are they... so loud!? S-shameless..." with vpunch
                                show boruto worried with dissolve
                                bot"That stupid [na_rel] of mine. Didn't even bother to say hello..."
                                show boruto:
                                    easein 2 xpos 1700 alpha 0.0
                                $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx3", loop=False, relative_volume = 1.4)
                                bot"..."
                                scene black with dissolve
                                show hima_end1:
                                    alpha 0.0
                                show hima_end1:
                                    linear 10 zoom 1.3 xalign 0.5 yalign 0.5 alpha 1.0
                                $ renpy.sound.play("/audio/soun_fx/sexslaps2.opus", channel="sfxstat", loop=False, relative_volume = 0.5,fadein=4)
                                $ renpy.sound.play("/audio/soun_fx/femalemoan1.opus", channel="sfx1", loop=False, relative_volume = 0.9,fadein=4)
                                bot"Though I suppose if I had someone like [hin_rel] waiting for me after being away for so long, I might have... other priorities too!"
                                # scene bedroomdoor
                                hin"[na_name]... I m-missed you so much!" with vpunch
                                $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx3", loop=False, relative_volume = 1.6)
                                menu:
                                    hin"[na_name]... I m-missed you so much!"
                                    "{color=[hatredcolor]}Lucky bastard...{/color}" if hatred >=20:
                                        call checkHatred(20,"none") from _call_checkHatred_17
                                        $ renpy.sound.play("/audio/soun_fx/sexslaps3.opus", channel="sfxstat", loop=False, relative_volume = 0.5,fadein=4)
                                        $ renpy.sound.play("/audio/soun_fx/femalemoan2.opus", channel="sfx1", loop=False, relative_volume = 0.9,fadein=4)
                                        bot"[hin_rel] is such a freaking hottie after all..."
                                        na"[hin_name]... It's been so long since..." with vpunch
                                        hin"J-just like that... More, M-MORE!" with vpunch
                                        $ renpy.sound.play("/audio/soun_fx/heartbeatlong.opus", channel="sfx2", loop=False, relative_volume = 0.9,fadein=2)
                                        call increaselust(10) from _call_increaselust_151
                                        bot"Even her moans are enough to arouse me..."
                                        show hima_end1 with dissolve:
                                            zoom 1.4 xalign 0.5 yalign 0.5 alpha 1.0
                                        bot"[na_rel] is such a lucky bastard..." with vpunch
                                        show hima_end1 with dissolve:
                                            zoom 1.6 xalign 0.5 yalign 0.5 alpha 1.0
                                        $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx3", loop=False, relative_volume = 1.6)
                                        hin"Y-yes... *Moans* Y-yes!"
                                        show hima_end1 with dissolve:
                                            zoom 1.65 xalign 0.5 yalign 0.5 alpha 1.0
                                        $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx3", loop=False, relative_volume = 2.0)
                                        call increaselust(10) from _call_increaselust_152
                                        bot"Does he even deserve someone like [hin_rel]...?"
                                        show hima_end1 with dissolve:
                                            zoom 1.7 xalign 0.5 yalign 0.5 alpha 1.0
                                        $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx3", loop=False, relative_volume = 2.2)
                                        na"[hin_name]... I am c-close!"
                                        show hima_end1 with dissolve:
                                            zoom 1.75 xalign 0.5 yalign 0.5 alpha 1.0
                                        hin"Y-you can... You can d-do it i-inside of m-me, [na_name]!"
                                        $ renpy.sound.play("/audio/soun_fx/sexslaps1.opus", channel="sfxstat", loop=False, relative_volume = 0.5,fadein=2)
                                        $ renpy.sound.play("/audio/soun_fx/bedcreak.opus", channel="sfx2", loop=False, relative_volume = 0.6,fadein=2)
                                        hin"Aarh, ♡ AAH!! H-harder! F-faster! Aaah...Ahh-ah! *Moans*" with flash
                                        $ renpy.sound.play("/audio/soun_fx/femaleorgasm.opus", channel="sfx1", loop=False, relative_volume = 0.7,fadein=1)
                                        hin"*Orgasmic Moans* Aaah!? ♡ Mmhmhm!!♡" with flash
                                        $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                                        $ renpy.sound.stop(channel="sfxstat", fadeout=1.0)
                                        na" Aaah! *Loud moans* M-my love! Aaaaaah!!" with flash
                                        na"How I've missed you..."
                                        show hima_end1 with dissolve:
                                            zoom 1.8 xalign 0.5 yalign 0.5 alpha 1.0
                                        bot"To think that all he does is fuck around for months and then..."
                                        scene black with dissolve
                                        show screen peeking1024("hinata_ndream_end1_1_unmarked")
                                        show screen peaking_overlay("bgp peak_updown")
                                        show layer screens at dizzyflashshort
                                        with longerflash
                                        call showscrollingimage from _call_showscrollingimage_83
                                        hin"[na_name]... *Heavy breathing*" with vpunch
                                        call increaselust(10) from _call_increaselust_153
                                        bot"He gets home only to be greeted by a literal goddess..." with vpunch
                                        call changeHatred(1,"ntrdream2") from _call_changeHatred_132
                                        bot"He is unworthy... Undeserving!"
                                        na"I am sorry [hin_name], but I'll have to go away for some time again..."
                                        bot"[hin_rel] is simply too good for someone like him..."
                                        bot"E-even like this, covered in sweat and sex juices... She is just so..."
                                        bot"S-she's so fucking sexy!"

                                        menu:
                                            bot"S-she's so fucking sexy!"
                                            "Open the door!":
                                                bot"[hin_rel] needs someone to satisfy her desires..."
                                                call increaselust(10) from _call_increaselust_154
                                                hide screen peeking1024
                                                hide screen peaking_overlay
                                                scene borutontr1:
                                                    zoom 1.6 xalign 0.5 yalign 0.0
                                                with dissolve
                                                bot"If [na_rel] won't do that, then..."
                                                $ renpy.sound.play("/audio/soun_fx/jerkoff2.opus", channel="sfx3", loop=False, relative_volume = 0.2)
                                                show borutontr1:
                                                    easein 0.6 yalign 1.0
                                                bot"Then I will!"          
                                                scene borutontr1 with dissolve:
                                                    zoom 1.8 xalign 0.5 yalign 0.0
                                                bot"I need y-you, [hin_rel]!"
                                                show hima_end1_1 with dissolve
                                                $ renpy.sound.play("/audio/soun_fx/dooropen.opus", channel="sfx1", loop=False, relative_volume = 0.6)
                                                pause 0.2
                                                show hima_end1_1 with dissolve:
                                                    zoom 1.5 xalign 0.5 yalign 0.5
                                                show screen parallax1280("hinata_ndream_end1",1.27,0.0,False) with longerflash
                                                call showscrollingimage from _call_showscrollingimage_84
                                                $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                                                show screen parallax1280("hinata_ndream_end1_surprised",1.27,0.0,False) with dissolve
                                                hin"[bo_name_stutter]!?" with vpunch
                                                show hinata_ndream_end1_surprised:
                                                    zoom 1.27 xalign 0.5 yalign 0.3
                                                call hidescrollingimage("Click twice to cum!") from _call_hidescrollingimage_80
                                                $ renpy.sound.play("/audio/soun_fx/jerkoff1.opus", channel="sfx3", loop=False, relative_volume = 0.2)
                                                hide screen parallax1280
                                                show hinata_ndream_end1_surprised with flash:
                                                    zoom 1.27 xalign 0.5 yalign 0.3
                                                bo"[hin_rel]... [hin_rel_stutter]!" with vpunch
                                                $ renpy.sound.play("/audio/soun_fx/wakeup.opus", channel="sfx3", loop=False, relative_volume = 1.2)
                                                $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                                                $ playmusic("/audio/ost/house2.opus", 0.5)
                                                scene bg bb intro at brightreveal:
                                                    matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 
                                                with longerflash
                                                with Shake((0, 0, 0, 0), 1, dist=20, peak_time=0.8, smoothness=50)
                                                show boruto box2surprised with Dissolve(1):
                                                    blur 30
                                                show boruto box2surprised with Dissolve(2):
                                                    easein 2 blur 0
                                                $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                                                bot"*Rapid breathing* W-what just... happened?" with vpunch
                                                bot"I... I feel like I've dreamt about something, but I don't remember a thing..."
                                                bot"Am I... Am I losing my mind?"
                                                call decreaselust(50) from _call_decreaselust_92
                                                bot"S-shit! How the h-hell did I soil my boxers in my sleep..."
                                                hide boruto with dissolve

                                                bot"Better put on some clean clothes and get on with my day..."
                                                scene black with dissolve
                                                bot"Can't even enjoy some sleep with this damned condition *Sigh...*"
                                                $ renpy.end_replay()
                                                jump action_taken

                                    "Leave them be...":
                                        bot"W-what am I even doing here..."
                                        scene black with dissolve
                                        bot"I should take a nap..."
                                        bot"I'll say hello to [na_rel] later..."
                                        $ playmusic("/audio/ost/house2.opus", 0.5)
                                        $ renpy.sound.play("/audio/soun_fx/wakeup.opus", channel="sfx3", loop=False, relative_volume = 1.2)
                                        scene bg bb intro at brightreveal:
                                            matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 
                                        with longerflash
                                        with Shake((0, 0, 0, 0), 1, dist=20, peak_time=0.8, smoothness=50)
                                        show boruto box2surprised with Dissolve(1):
                                            blur 30
                                        show boruto box2surprised with Dissolve(2):
                                            easein 2 blur 0
                                        $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                                        bot"*Rapid breathing* W-what just... happened?" with vpunch
                                        bot"I... I feel like I've dreamt about something, but I don't remember a thing..."
                                        bot"Am I... Am I losing my mind?"
                                        hide boruto with dissolve
                                        bot"Better put on some clothes and get on with my day..."
                                        scene black with dissolve
                                        bot"Can't even enjoy some sleep with this damned condition *Sigh...*"
                                        $ renpy.end_replay()
                                        jump action_taken
                                    "Take a peek!":
                                        
                                        $ renpy.sound.play("/audio/soun_fx/sexslaps3.opus", channel="sfxstat", loop=False, relative_volume = 0.5,fadein=4)
                                        $ renpy.sound.play("/audio/soun_fx/femalemoan2.opus", channel="sfx1", loop=False, relative_volume = 0.9,fadein=4)
                                        na"[hin_name]... It's been so long since..." with vpunch
                                        hin"J-just like that... More, M-MORE!" with vpunch
                                        $ renpy.sound.play("/audio/soun_fx/heartbeatlong.opus", channel="sfx2", loop=False, relative_volume = 0.9,fadein=2)   
                                        bot"*Gulp* They sure enjoy each other..."
                                        show hima_end1 with dissolve:
                                            zoom 1.4 xalign 0.5 yalign 0.5 alpha 1.0
                                        bot"W-what the hell is going on in there anyway..." with vpunch
                                        show hima_end1 with dissolve:
                                            zoom 1.6 xalign 0.5 yalign 0.5 alpha 1.0
                                        $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx3", loop=False, relative_volume = 1.6)
                                        hin"Y-yes... *Moans* Y-yes!"
                                        show hima_end1 with dissolve:
                                            zoom 1.65 xalign 0.5 yalign 0.5 alpha 1.0
                                        $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx3", loop=False, relative_volume = 2.0)
                                        call increaselust(10) from _call_increaselust_155
                                        bot"[hin_rel]'s moans are so..."
                                        show hima_end1 with dissolve:
                                            zoom 1.7 xalign 0.5 yalign 0.5 alpha 1.0
                                        $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx3", loop=False, relative_volume = 2.2)
                                        na"[hin_name]... I am c-close!"
                                        show hima_end1 with dissolve:
                                            zoom 1.75 xalign 0.5 yalign 0.5 alpha 1.0
                                        hin"Y-you can... You can let it inside of m-me, [na_name]!"
                                        $ renpy.sound.play("/audio/soun_fx/sexslaps1.opus", channel="sfxstat", loop=False, relative_volume = 0.5,fadein=2)
                                        $ renpy.sound.play("/audio/soun_fx/bedcreak.opus", channel="sfx2", loop=False, relative_volume = 0.6,fadein=2)
                                        hin"Aarh, ♡ AAH!! H-harder! F-faster! Aaah...Ahh-ah! *Moans*" with flash
                                        $ renpy.sound.play("/audio/soun_fx/femaleorgasm.opus", channel="sfx1", loop=False, relative_volume = 0.7,fadein=1)
                                        hin"*Orgasmic Moans* Aaah!? ♡ Mmhmhm!!♡" with flash
                                        $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                                        $ renpy.sound.stop(channel="sfxstat", fadeout=1.0)
                                        na" Aaah! *Loud moans* M-my love... Aaaaaah!!" with flash
                                        show hima_end1 with dissolve:
                                            zoom 1.8 xalign 0.5 yalign 0.5 alpha 1.0
                                        bot"*Gulp*..."
                                        scene black with dissolve
                                        show screen peeking1024("hinata_ndream_end1_1_unmarked")
                                        show screen peaking_overlay("bgp peak_updown")
                                        show layer screens at dizzyflashshort
                                        with longerflash
                                        call showscrollingimage from _call_showscrollingimage_85
                                        hin"[na_name]... *Heavy breathing*" with vpunch
                                        call increaselust(10) from _call_increaselust_156
                                        bot"[hin_rel]... She is..." with vpunch
                                        bot"Covered in sweat and sex jjuices..."
                                        bot"They must have been at it for a while..."
                                        bot"E-even like this, she is just so... b-beautiful..."
                                        bot"[na_rel] is so lucky to have someone like her..."
                                        bot"I wonder if..."
                                        menu:
                                            bot"I wonder if..."
                                            "M-maybe we could share [hin_rel]...":
                                                bot"M-maybe [na_rel] wouldn't mind if we..."
                                                call increaselust(10) from _call_increaselust_157
                                                hide screen peeking1024
                                                hide screen peaking_overlay
                                                scene borutontr00:
                                                    zoom 1.6 xalign 0.5 yalign 0.0
                                                with dissolve
                                                bot"C-can't we both enjoy [hin_rel]!?"
                                                $ renpy.sound.play("/audio/soun_fx/jerkoff2.opus", channel="sfx3", loop=False, relative_volume = 0.2)
                                                show borutontr00:
                                                    easein 0.6 yalign 1.0
                                                bot"S-she is just... too p-pretty not to share!"
                                                $ renpy.sound.play("/audio/soun_fx/jerkoff1.opus", channel="sfx3", loop=False, relative_volume = 0.2)
                                                show borutontr00 at dizzyflashshort
                                                bot"Such a beautiful woman, so kind, so pure... so l-loving!"
                                                show borutontr00:
                                                    easein 0.6 yalign 0.0
                                                $ renpy.sound.play("/audio/soun_fx/jerkoff2.opus", channel="sfx3", loop=False, relative_volume = 0.2)
                                                bot"S-surely [na_rel] and [hin_rel] would be o-okay with it..."
                                                bot"Just o-one time..."
                                                bot"Just to feel her t-touch..."
                                                $ renpy.sound.play("/audio/soun_fx/jerkoff1.opus", channel="sfx3", loop=False, relative_volume = 0.2)
                                                menu:
                                                    bot"Just to feel her t-touch..."
                                                    "Open the door!":
                                                        bot"[hin_rel]..."
                                                        scene borutontr00 with dissolve:
                                                            zoom 1.8 xalign 0.5 yalign 0.0
                                                        bot"I need y-you, [hin_rel_mother]!"
                                                        show hima_end1_1 with dissolve
                                                        $ renpy.sound.play("/audio/soun_fx/dooropen.opus", channel="sfx1", loop=False, relative_volume = 0.6)
                                                        pause 0.2
                                                        show hima_end1_1 with dissolve:
                                                            zoom 1.5 xalign 0.5 yalign 0.5
                                                        show screen parallax1280("hinata_ndream_end1",1.27,0.0,False) with longerflash
                                                        call showscrollingimage from _call_showscrollingimage_86
                                                        $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                                                        show screen parallax1280("hinata_ndream_end1_surprised",1.27,0.0,False) with dissolve
                                                        hin"[bo_name_stutter]!?" with vpunch
                                                        show hinata_ndream_end1_surprised:
                                                            zoom 1.27 xalign 0.5 yalign 0.3
                                                        call hidescrollingimage("Click twice to cum!") from _call_hidescrollingimage_81
                                                        $ renpy.sound.play("/audio/soun_fx/jerkoff1.opus", channel="sfx3", loop=False, relative_volume = 0.2)
                                                        hide screen parallax1280
                                                        show hinata_ndream_end1_surprised with flash:
                                                            zoom 1.27 xalign 0.5 yalign 0.3
                                                        bo"I am s-sorry [hin_rel]! I am c-cumming!" with vpunch
                                                        $ renpy.sound.play("/audio/soun_fx/wakeup.opus", channel="sfx3", loop=False, relative_volume = 1.2)
                                                        $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                                                        $ playmusic("/audio/ost/house2.opus", 0.5)
                                                        scene bg bb intro at brightreveal:
                                                            matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 
                                                        with longerflash
                                                        with Shake((0, 0, 0, 0), 1, dist=20, peak_time=0.8, smoothness=50)
                                                        show boruto box2surprised with Dissolve(1):
                                                            blur 30
                                                        show boruto box2surprised with Dissolve(2):
                                                            easein 2 blur 0
                                                        $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                                                        bot"*Rapid breathing* W-what just... happened?" with vpunch
                                                        bot"I... I feel like I've dreamt about something, but I don't remember a thing..."
                                                        bot"Am I... Am I losing my mind?"
                                                        call decreaselust(50) from _call_decreaselust_93
                                                        bot"S-shit! How the h-hell did I soil my boxers in my sleep..."
                                                        hide boruto with dissolve

                                                        bot"Better put on some clean clothes and get on with my day..."
                                                        scene black with dissolve
                                                        bot"Can't even enjoy some sleep with this damned condition *Sigh...*"
                                                        $ renpy.end_replay()
                                                        jump action_taken
                                                
                                                    
                                            "W-what am I thinking!":
                                                bot"W-what am I even thinking..."
                                                hide screen peeking1024
                                                hide screen peaking_overlay
                                                scene hima_end1:
                                                    zoom 1.6 xalign 0.5 yalign 0.5
                                                with dissolve
                                                bot"Damn it..."
                                                $ playmusic("/audio/ost/house2.opus", 0.5)
                                                $ renpy.sound.play("/audio/soun_fx/wakeup.opus", channel="sfx3", loop=False, relative_volume = 1.2)
                                                scene bg bb intro at brightreveal:
                                                    matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 
                                                with longerflash
                                                with Shake((0, 0, 0, 0), 1, dist=20, peak_time=0.8, smoothness=50)
                                                show boruto box2surprised with Dissolve(1):
                                                    blur 30
                                                show boruto box2surprised with Dissolve(2):
                                                    easein 2 blur 0
                                                $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                                                bot"*Rapid breathing* W-what just... happened?" with vpunch
                                                bot"I... I feel like I've dreamt about something, but I don't remember a thing..."
                                                bot"Am I... Am I losing my mind?"
                                                hide boruto with dissolve
                                                bot"Better put on some clothes and get on with my day..."
                                                scene black with dissolve
                                                bot"Can't even enjoy some sleep with this damned condition *Sigh...*"
                                                $ renpy.end_replay()
                                                jump action_taken
                                            
                                        
                            
                            
                        
                    "Return":
                        jump borutonormalsleepmenu
                        
                  
            "Return":
                call showUIhouse from _call_showUIhouse_16
                
                $ ui.interact()

    elif day_part == 1 or day_part == 2 or day_part == 3:
        $ massagebooklvl1inv = inventory.find_item_by_name("Massage Tips Volume 1")
        menu:
            "..."
            "Sleep":
                menu borutosleepmenu:
                    "..."
                    "Sleep until the Evening" if day_part == 1:
                        hide screen borutobedroombuttons
                        hide screen housemap
                        bot"At last, my favourite past-time activity..."
                        scene black with dissolve
                        jump action_taken
                    "Sleep until the Night" if day_part == 1 or day_part == 2:
                        hide screen borutobedroombuttons
                        hide screen housemap
                        bot"At last, my favourite past-time activity..."
                        scene black with dissolve
                        jump action_taken_night
                    
                    "Sleep until the Midnight" if day_part == 3:
                        hide screen borutobedroombuttons
                        hide screen housemap
                        bot"At last, my favourite past-time activity..."
                        scene black with dissolve
                        jump action_taken
                    # "Sleep until the Midnight" if day_part == 1 or day_part == 2 or day_part == 3:
                    #     hide screen borutobedroombuttons
                    #     hide screen housemap
                    #     bot"At last, my favourite past-time activity..."
                    #     scene black with dissolve
                    #     jump action_taken_midnight
                    "Return":
                        call showUIhouse from _call_showUIhouse_17
                        $ ui.interact()
            "Change Clothes":
                menu borutoclothesmenu:
                    "..."
                    "Casual":
                        $ boruto_clothes = "Casual"
                        show screen relationships
                        call showUIhouse from _call_showUIhouse_18
                        $ ui.interact()
                    "Underwear":
                        $ boruto_clothes = "Underwear"
                        show screen relationships
                        call showUIhouse from _call_showUIhouse_19
                        $ ui.interact()
                    "Naked":
                        $ boruto_clothes = "Naked"
                        show screen relationships
                        call showUIhouse from _call_showUIhouse_20
                        $ ui.interact()
                    "Return":
                        call showUIhouse from _call_showUIhouse_21
                        $ ui.interact()
            "Read Massage Guide" if massagebooklvl1inv != None:
                show boruto sceeming with dissolve
                bot"Let's see if there's anything useful in this book..."
                bot"Hopefully I haven't wasted my money on this crap!"
                show blackscreen with dissolve
                show boruto surprised2
                "You spent some time disecting the book..."
                hide blackscreen with dissolve
                call useItem(massagebooklvl1,1) from _call_useItem_4
                bot"Aha! Effleurage techniques to first relax the muscles, followed by Petrissage techniques to pierce through the tension of the muscle."
                show boruto sceeming with dissolve
                $ notification ("Event option unlocked")
                default massageknowledge = 0
                $ massageknowledge = 1
                bot"This should come in useful next time [hin_rel] let's me help her relax!"
                jump action_taken



  
            "Return":
                call showUIhouse from _call_showUIhouse_22
                $ ui.interact()

        
