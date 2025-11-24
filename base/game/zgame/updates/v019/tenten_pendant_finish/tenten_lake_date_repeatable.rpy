label tenten_lake_date_start_repeatable:
    default tenten_date_shop_dialogueflavor_mentioned = False
    default tenten_lake_date_bj = False
    default tenten_date_success_repeatable = 0 # Flag for counting successful repeated dates
    default tenten_brain_damage = False
    $ initialize_replay_defaults()
    $ playmusic("audio/ost/lakedate.opus",0.3)
    show boruto:
        easein 2 xalign -3
    show ten:
        easein 2 xalign -3
    with moveoutleft
    hide ten
    hide boruto
    scene black
    with dissolve
    pause(1)
    scene bg_night_forest1 with Dissolve(0.5):
        xalign 0.5 yalign 1.0 subpixel True
    show bg_night_forest1:
        easein 10 zoom 1.15 yalign 0.0 xalign 1.0 subpixel True
    pause(2)
    $ renpy.sound.play("/audio/soun_fx/crickets.opus",channel="sfx1",loop=True,relative_volume=0.05)
    "The path winds through the darkening woods, while crickets chirp the silence of the night away."
    show tenten_walk1 with dissolve
    "Once again, Tenten guides you through the forest, towards her favorite place..."
    bot "It feels nice, spending time with her..."
    scene replace_handhold_overlay
    with Dissolve(1)
    scene replace_handhold_overlay:
        subpixel True
        align (0.5, 0.5)
        easein 10 zoom 1.15
    bot"With all our troubles, it feels like I can relate to her, and she to me..."
    if tenten_lake_date_fail_retry>0: # Repeatable from a fail retry attempt
        "Despite your previous date's awkwardness, she lets you."
        bot "I still have a chance... I'm not gonna screw up this time."
        bo "Tenten, about last time-"
        ten "It's okay, we already talked about it, I trust this time will be different"
        bo "R-right!"
        "You continue walking hand in hand, determined to put the awkwardness behind you."
    elif tenten_date_success_repeatable == 0 and tenten_helped_release: # First repeatable after a successful date
        "The atmosphere feels charged, but in a good way."
        bot "The fact that she still feels comfortable after all that happened last time..."
        bo "Hey, Tenten, about last time-"
        ten "Didn't I make you promise you're never gonna mention what happened last time?"
        bo "Yes but, my condition... I wanted to say sorry for putting you on the spot like that."
        ten "Like I said, I wanted to help. You didn't force me. And you can't help it, right?"
        bo "R-right..."
        bot "It almost feels like she needs it as well, and helping with my curse is just a convenient excuse for her to hide that desire."
        "You continue walking hand in hand, the sexual tension between you rising by the minute."
    elif not tenten_helped_release: # If nothing ever happened yet
        "The atmosphere feels charged, but in a good way."
        bot "The fact that she still feels comfortable after what almost happened last time..."
        bo "Hey, Tenten, about last time-"
        ten "Relax, you kept it under control. It's okay!"
        bo "Yes but, my condition... I wanted to say sorry for putting you on the spot like that."
        bo "And there's no guarantee that I'll always be able to control it."
        ten "I know you can't help it, and regardless of what happens, I'm here for you."
        bo "T-thank you Tenten, that means a lot."
        bot "It almost feels like she {b}wants{/b} me to lose control so she can get a chance to 'help' me with it..."
        "You continue walking hand in hand, the sexual tension between you rising by the minute."
    else: # Subsequent repeatables
        bo "Do you always walk this slow? If I didn't know any better I'd think you're not looking forward to this!"
        ten "Hey, watch your tone mister."
        ten "Just cause we hooked up a couple of times doesn't mean you're the boss."
        bo "Did you just say 'hooked up' or maybe I misheard? I thought you were helping me with the c-"
        ten "T-that's what I meant, idiot. Helping you with the condition..."
        bo "S-sure..."
        "You share a laugh as you hurriedly make your way forward."

    scene black with dissolve
    pause (1)
    show bg_lake_1 with dissolve:
        zoom 1.3 xalign 0.5 yalign 1.0 subpixel True
    show bg_lake_1:
        easein 10 zoom 1.0 yalign 0.0 subpixel True
    $ renpy.sound.play("/audio/soun_fx/lake_owl_ambience.opus",channel="sfx2",loop=True,relative_volume=0.4)
    "Soon you arrive at the lake."
    "Tenten lets go of your hand as she walks towards the water's edge..."
    jump tenten_lake_date_undress_repeatable

label tenten_lake_date_fail_permanent_label_repeatable:
    hide screen image_with_border
    $ tenten_lake_date_fail_permanent = True
    $ tenten_date_agreed = False
    $ tenten_date_success = False
    stop sound channel "sfx1"
    stop sound channel "sfx2"
    stop sound channel "sfx3"
    $ playmusic("audio/ost/lakedate_fail.opus",0.5)
    $ renpy.sound.play("/audio/soun_fx/crickets.opus",channel="sfx1",loop=True,relative_volume=0.05)
    $ renpy.sound.play("/audio/soun_fx/lake_owl_ambience.opus",channel="sfx2",loop=True,relative_volume=0.4)
    scene black with vpunch
    scene bg_lake_1
    show ten angry at right
    show boruto surprised at left
    with dissolve
    ten "You're despicable."
    ten "After all those words, all this, everything, was just to... take advantage of me?"
    ten "I was stupid to think you were ever really listening to me."
    ten "You can find your own way back to the village."
    ten "I'm leaving."
    show ten angry with dissolve:
        easein 1 xpos 2500
    bot "W-whatever! She's way too sensitive, sheesh!"
    show boruto angry with dissolve
    bot "Her loss!" with vpunch
    jump action_taken

label tenten_lake_date_fail_retry_repeatable:
    $ tenten_lake_date_fail_retry += 1
    $ tenten_date_agreed = False
    $ tenten_date_success = False
    $ tenten_date_counter += 1
    $ tenten_date_shop_dialogueflavor_mentioned = False
    stop sound channel "sfx1"
    stop sound channel "sfx2"
    stop sound channel "sfx3"
    $ playmusic("audio/ost/lakedate_fail.opus",0.5)
    $ renpy.sound.play("/audio/soun_fx/crickets.opus",channel="sfx1",loop=True,relative_volume=0.05)
    $ renpy.sound.play("/audio/soun_fx/lake_owl_ambience.opus",channel="sfx2",loop=True,relative_volume=0.4)
    scene black with dissolve
    pause(1.0)
    scene bg_lake_1
    show ten angry at right
    with dissolve
    if tenten_lake_date_fail_retry > 0:
        ten "Come on, [bo_name]! It's not the first time you're trying to pull this off!"
        show boruto surprised at left with dissolve
        ten "Last time you promised you'd do better!"
    else:
        ten "I think we got off on the wrong foot here."
        show boruto surprised at left with dissolve
        ten "You should take some time alone to figure out what you want."
    bo "B-but... Tenten I-"
    ten "You can find your own way back home!" with vpunch
    show ten angry with dissolve:
        easein 1 xpos 2500
    bo "Here we go again..."
    show boruto sad with dissolve
    bot "...fuck."
    bot "Maybe I should change my approach slightly next time..."
    bot "...if there is a next time."
    jump action_taken

label tenten_lake_date_undress_repeatable:
    show screen parallax1280("tenten_lookaway_2") with flash
    call showscrollingimage from _call_showscrollingimage_123
    ten "You know, I was thinking..."
    ten "I don't r-really mind if... you w-watch this time!"
    if tenten_lake_date_fail_retry>0:
        ten "As long as you promise not to act like an idiot as you did last time!"
    bo "O-okay..."
    if tenten_date_peeked == True:
        bot "Whew... So she doesn't know I peeked last time too!"
        bot "At least now I can do it with her permission, that's kinda hot."
    scene black
    call hidescrollingimage2 from _call_hidescrollingimage2_52
    "You stare intensely as she begins to undress."
    show tenten_lake_back_undress with flash:
        zoom 1.25 xalign 0.5 yalign 1.0
        ease 2 yalign 0.5
    pause (1.5)
    show tenten_lake_back_undress_full with dissolve:
        zoom 1.25 xalign 0.5 yalign 0.0
        ease 2 yalign 0.5
    pause (1.5)
    scene black
    with dissolve
    bot "I guess behaving well pays off!"
    call increaselust(10) from _call_increaselust_230

    $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus",channel="sfx1",loop=False,relative_volume=0.5)
    "You hear the rustle of clothing and before you know it,"
    $ renpy.sound.play("/audio/soun_fx/waterjump.opus",channel="sfx1",loop=False,relative_volume=0.5)
    "-she's already in the water."
    bo "H-hey w-wait for me!"
    jump tenten_lake_date_swimming_repeatable

label tenten_lake_date_swimming_repeatable:
    scene black with vpunch
    $ renpy.sound.play("/audio/soun_fx/waterjump2.opus",channel="sfx1",loop=False,relative_volume=0.5)
    pause(0.5)
    show screen parallax1280("both_in_lake_submerged", 1.25) with flash
    call showscrollingimage from _call_showscrollingimage_124
    bot "For some reason, I'm even more nervous than I was the first time..."
    if tenten_lake_date_fail_retry == 0:
        show screen parallax1280("both_in_lake_submerged2", 1.25) with dissolve
        bot "And it doesn't seem she minds about where I'm staring..."
    else:
        show screen parallax1280("both_in_lake_submerged2", 1.25) with dissolve
        bot "Probably because I promised I'd do better this time, and I still have no idea what I'm doing!"
    ten "What's the matter, [bo_name]?"
    "She teases you."
    jump tenten_lake_date_release_check_repeatable


label tenten_lake_date_release_check_repeatable:
    bo "A-are you not w-worried about my... Condition?"
    ten "[bo_name], I know that you are... troubled, as am I. But It's okay, because we both have a brighter side to us, don't we? *Giggles*"
    if tenten_lake_date_fail_retry > 0:
        # Dialogue for retry after fail
        ten "And I mean these words. But... after last time..."
        show screen parallax1280("blackscreen", 1.25, 0.5, False) with dissolve
        $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
        show screen parallax1280("pov2_1talk", 1.25) with dissolve
        ten "I just hope you can control it better now. I don't want things to get... awkward again."
        bo "I know, Tenten. I messed up badly. I won't let that happen again. I promise."
        bo "It's just... hard sometimes. But having you here... knowing you're giving me another chance... it helps."
        ten "Okay. I believe you want to do better. Just... be careful, alright?"
        bo "I will be."
    else:
        # Dialogue for first repeat after success
        ten "And your condition doesn't scare me anymore. Seeing you struggle with it... I just want to help, to understand..."
        show screen parallax1280("blackscreen", 1.25, 0.5, False) with dissolve
        $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
        show screen parallax1280("pov2_1talk", 1.25) with dissolve
        ten "You don't have to hide it from me, [bo_name]. You can trust me."
        bo "Just knowing you aren't scared of me, that you want to be here with me... That means a lot, more than you know."
        ten "What would I be scared of? We're friends... right?"
        "She looks at you intently, a hint of something more in her eyes."
        bo "R-right... friends."

    "Just as the emotional connection deepens, you feel a familiar twinge..."
    show screen parallax1280("blackscreen", 1.25, 0.5, False) with vpunch
    $ renpy.sound.play("/audio/soun_fx/bassstart.opus",channel="sfx3",loop=False,relative_volume=0.5)
    bo "*Groans*! Ar-ah..." with vpunch
    show screen parallax1280("both_in_lake_slightly_submerged", 1.25, 0.5, menuenabled=True) with dissolve
    $ renpy.sound.play("/audio/soun_fx/heartbeatlong.opus",channel="sfx4",loop=True,relative_volume=0.5)
    ten "[bo_name]!? It's the curse again, isn't it?"

    menu ask_sex_scene_repeatable:
        bo "It's getting really bad again. I... I need..."

        "{color=[obediencecolor]}Ask for a blowjob{/color}" if tenten_lake_date_fail_retry==0:
            jump tenten_lake_date_blowjob_scene_repeatable           

        "Ask for a handjob":
            if tenten_date_handjob == True:
                bo "Yeah... Could you... help me? Just... with your hand again?"
            else:
                bo "Yeah... Could you... help me? Just... with your hand?"
            ten "[bo_name], as long as you behave, I'll help in every w-way I can!"
            jump tenten_lake_date_handjob_scene_repeatable

        "Grab her ass":
            call hidescrollingimage2 from _call_hidescrollingimage2_53
            jump tenten_lake_date_assgrab_fail_repeatable

        "Ask if you can grab her ass":
            jump tenten_lake_date_assgrab_repeatable

        "Ask if you can suck on her breasts":
            jump tenten_lake_date_titsuck_repeatable
        
        "{color=[obediencecolor]}???{/color}" if tenten_date_success == False:
            "Complete a date with Tenten successfully to unlock!"
            jump ask_sex_scene_repeatable

label tenten_lake_date_handjob_scene_repeatable:
    $ tenten_helped_release = True
    ten "O-okay... um... where...?"
    show screen parallax1280("blackscreen", 1.25, 0.5, False) with dissolve
    $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
    "She gestures vaguely for you to follow her."
    bot"She's less hesitant than last time."
    bot"Maybe she really is into m-me after all?"
    scene black
    call hidescrollingimage2 from _call_hidescrollingimage2_54
    $ renpy.sound.play("/audio/soun_fx/water_move_4.opus", channel="sfx1", loop=False, relative_volume = 0.5)
    "You walk to a slightly more shallow part of the lake."
    $ renpy.sound.play("/audio/soun_fx/water_move_3.opus", channel="sfx1", loop=False, relative_volume = 0.5)
    $ playmusic("audio/ost/lakedate.opus",0.3)
    $ renpy.sound.play("/audio/soun_fx/crickets.opus",channel="sfx2",loop=True,relative_volume=0.05)
    $ renpy.sound.play("/audio/soun_fx/lake_owl_ambience.opus",channel="sfx3",loop=True,relative_volume=0.4)
    stop sfx4 fadeout 1
    show hj2 with dissolve:
        zoom 1.25 xalign 0.5 yalign 1.0
    show hj2:
        easein 3 yalign 0.0
    ten"It's growing so f-fast... Is it painful?"
    bo "Y-yeah..."
    show screen parallax1280("hj2", 1.25, 1.0) with dissolve
    call showscrollingimage from _call_showscrollingimage_125
    ten "*Gasps softly* D-don't let it just poke me..." with vpunch
    bo"I can't quite c-control it you know..."
    ten"The heat it emanates, I can feel it..."
    ten"I can almost sense your p-pain through it. It's so ...hardened too."
    bo "Part of the curse, I t-think..."
    "She takes a deep breath."
    ten "Then..."
    scene black with dissolve
    call hidescrollingimage2 from _call_hidescrollingimage2_55
    "Hesitantly, she reaches out. Her touch is surprisingly gentle."
    ten"Leave it to my capable hands..."
    $ renpy.sound.play("/audio/soun_fx/water_move_2.opus", channel="sfx1", loop=False, relative_volume = 0.5)
    scene hj4 with dissolve
    "Her hand closes around you, still slightly trembling..."
    show screen parallax1280("tenten_handjob_1", 1.25, 0.8, menuenabled=True) with dissolve
    $ renpy.sound.play("/audio/soun_fx/handjob1.opus", channel="sfx1", loop=True, relative_volume = 1.0)
    "She starts a slow, uncertain rhythm..."
    bo "Tenten..."
    "She starts a slow, uncertain rhythm..."
    ten "Is this... h-helping?"
    menu hj_option_1_repeatable:
        ten "Is this... h-helping?"
        "Enjoy the process...":
            bo "Just like that..."
            pass
        "Come on, f-faster!":
            bo "Y-yeah... faster... maybe?"
            label date0gofaster_repeatable:
            $ renpy.sound.play("/audio/soun_fx/water_move_2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            $ renpy.sound.play("/audio/soun_fx/handjob2.opus", channel="sfx1", loop=True, relative_volume = 1.0)
            show screen parallax1280("tenten_handjob_1_fast", 1.25, 0.8) with dissolve
            "She nods, blushing furiously but increasing the pace. Her movements become more erratic."
            ten "I... I can't believe I'm doing this..."
            bo "Ah... y-yes! Faster, Tenten! Please!"
            ten "You are getting really a-anxious, are you not?"
            bo "Ngh... Don't stop..."
            ten "Just... tell me when..."
            bo "A-almost... there!"
            ten"It's best if I end this quickly then..."
            call hidescrollingimage2 from _call_hidescrollingimage2_56
            $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            label date0gofaster_2_repeatable:
            scene hj3 with dissolve:
                xzoom -1
            "She brings herself closer to you, her stomach brushing against the tip of your manhood while she keeps delicately working the shaft..."
            show tenten_handjob_2 with dissolve
            bo"T-tenten..."
            ten"Don't worry. I'll take care of it for you..."
            show tenten_handjob_2_fast with dissolve
            ten"This ought to get the job done!"
            bot"F-fuck! She is kinda good at t-this..."
            bot"I can't hold on any longer!" with flash
            ten"It's pulsating... t-throbbing!"
            scene hj3 with dissolve:
                xzoom -1
            ten"You are about to... aren't you?"
            $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            show hj3_cum1 with flash:
                xzoom -1
            bo"S-sorry... I am c-cumming!" with flash
            ten"It's okay... Let it all out..."
            bo"Aaahh! *Moans*" with vpunch
            $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            show hj3_cum1_1 with longerflash:
                xzoom -1
            $ renpy.sound.stop(channel="sfx1")
            $ renpy.sound.stop(channel="sfx2")
            $ renpy.sound.stop(channel="sfx3")
            call decreaselust(100) from _call_decreaselust_106
            ten"..."
            bo"*Heavy breathing*..."
            ten"...F-feeling better?"
            bo"M-much better. Thank you, Tenten..."
            if tsunade_discovery_seen == True:
                $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx4", loop=False, relative_volume = 1.2)
                bot "W-wait! Tsunade's discovery... My cum just t-touched her, w-will she..." with vpunch
                bot "Tenten... For your own sake I really hope the water around us is enough to dilute it before it had time to act on you!"
            ten"*Sigh*"
            ten"Look at this mess you made..."
            scene black with dissolve
            bo"My a-apologies..."
            ten"Come on, let's wash ourselves..."
            if tsunade_discovery_seen == True:
                bo "T-tenten, you might wanna wash yourself extra carefully..."
                ten "Huh? Stop being weird and move!"
            $ renpy.sound.play("/audio/soun_fx/water_move_2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            show screen parallax1280("both_in_lake_submerged2",1.25) with dissolve
            call showscrollingimage from _call_showscrollingimage_126
            jump date0endingjump_repeatable
    ten"Just... r-relax, okay?"
    bot "She's... actually good at this. And she's doing it... for me."
    menu dialogue_option_hj_repeatable:
        "I'm glad you got your pendant back":
            bo "The pendant..."
            bo "I'm glad-"
            scene black with dissolve
            hide hj3
            "You didn't even manage to finish your sentence when..."
            $ renpy.sound.play("/audio/soun_fx/water_move_3.opus", channel="sfx1", loop=False, relative_volume = 0.5)
            show screen parallax1280("hj", 1.25, menuenabled=True) with dissolve
            call showscrollingimage from _call_showscrollingimage_127
            $ renpy.sound.play("/audio/soun_fx/kiss1.opus", channel="sfx3", loop=False, relative_volume = 1.0)
            "...She leans in and unexpectedly interrupts you with a kiss."
            bot "!" with vpunch
            bot"M-my first real kiss..."
            
        "{color=[dominancecolor]}You're an expert at this!{/color}":
            call changeDominance(1) from _call_changeDominance_104
            bo "You're an expert at this!"
            ten "Sh-shut up idiot..."
            ten "I don't do stuff like this often..."
            ten "I'm just trying to help with your.. p-problem, just like you helped with mine..."
            $ expert_option = True
                
    menu hj_option_2_repeatable:
        bo "..."
        "{color=[dominancecolor]}Reach for a kiss{/color}" if expert_option == True:
            if dominance >= 15:
                
                bo"Tenten, I am sorry but..."
                call checkDominance(15,"none") from _call_checkDominance_35
                show screen parallax1280("hj7_grabtit", 1.25) with dissolve
                bo"You are too pretty for me not to make a move..."
                "You reach in for a kiss, and a little something more..."
                show screen parallax1280("blackscreen", 1.25) with vpunch
                "Tenten pushes you slightly back by gently pressing her palm against your chest..."
                ten"That was... a bit s-sudden!"
                ten"A heads up would be nice! Like..."
                $ renpy.sound.play("/audio/soun_fx/kiss1.opus", channel="sfx3", loop=False, relative_volume = 1.0)
                show screen parallax1280("hj", 1.25) with dissolve
                ten"...This!"
                bot"O-oh...? She went in for it herself!" with vpunch
                bot"And she keeps s-stroking my cock! I think I am about to..." with flash
                show screen parallax1280("hj2", 1.25) with dissolve
                "She pulled back momentarily..."
                ten"Bet you enjoyed that one..."
                call changeDominance(1) from _call_changeDominance_105
                bo"Almost as much as you did!"
                ten"Oh you..."
                show screen parallax1280("blackscreen", 1.25) with vpunch
                ten"Job's not finished, is it...? *Giggles*"
                call hidescrollingimage2 from _call_hidescrollingimage2_57
                jump date0gofaster_2_repeatable
            else:
                show screen parallax1280("hj7_grabtit", 1.25) with dissolve
                ten"*Gasps*" with vpunch
                call checkDominance(15,"none") from _call_checkDominance_36
                "You reach in for a kiss, but you reached for more than what Tenten was comfortable with..."
                show screen parallax1280("hj2", 1.25) with dissolve
                ten"H-hey, careful!"
                bo"S-sorry..."
                ten"Just, follow my lead, okay...?"
                call hidescrollingimage2 from _call_hidescrollingimage2_58
                jump date0gofaster_repeatable


            "You instinctively reached for her breasts!"
            $ renpy.sound.play("/audio/soun_fx/water_move_5.opus", channel="sfx1", loop=False, relative_volume = 0.5)
            show screen parallax1280("hj7_grabtit", 1.25) with flash
            call showscrollingimage from _call_showscrollingimage_128
            ten "[bo_name_stutter]!"
            bo "Just... keep going..."
        

        "Enjoy the kiss..." if expert_option == False:
            $ renpy.sound.play("/audio/soun_fx/kiss1.opus", channel="sfx3", loop=False, relative_volume = 1.0)
            "You kept exploring each other's lips, while Tenten kept gently stroking your manhood..."
            bot"She..."
            bot"She has a nice t-taste to her. I think I am about to..." with flash
            show screen parallax1280("hj2", 1.25) with dissolve
            "She pulled back momentarily..."
            ten"Bet you enjoyed that one..."
            bo"Tenten, I-"
            show screen parallax1280("blackscreen", 1.25) with vpunch
            ten"Job's not finished, is it...? *Giggles*"
            call hidescrollingimage2 from _call_hidescrollingimage2_59
            jump date0gofaster_2_repeatable

    label date0endingjump_repeatable:
    ten "Oh dear..."
    bo "T-thank you, Tenten. I... I feel much better. The pain's gone."
    "You both avoid each other's gaze, feeling somewhat flustered by what transpired..."
    ten "G-good... Just don't mention this. To anyone. Ever."
    bo "R-right. This will be our secret..."
    call hidescrollingimage2 from _call_hidescrollingimage2_60
    scene black with dissolve

    jump tenten_lake_date_ending_kind_repeatable

label tenten_lake_date_assgrab_fail_repeatable:
    call changeDominance(1) from _call_changeDominance_106
    $ renpy.sound.play("/audio/soun_fx/spank7.opus", channel="sfx3", loop=False)
    show screen parallax1280("2h_assgrab",1.25,1.0)
    call showscrollingimage from _call_showscrollingimage_129
    with vpunch
    stop sfx4
    ten "Hey! [bo_name], what do you think you're doing?!"
    if tenten_assgrab_fail == True:
        ten "You try to pull this off on me again? You have no respect for boundaries!"
    call hidescrollingimage2 from _call_hidescrollingimage2_61
    $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
    scene black with dissolve
    show screen parallax1280("pov2_angry",1.25,0.3) with dissolve
    ten "I offered to help you because you said you were in pain, not so you could just... grope me!"
    ten "I thought maybe you were different, but you're just like everyone else!"
    call hidescrollingimage2 from _call_hidescrollingimage2_62
    "Tenten stepped out of the water to dry herself..."
    show tenten_lake_back_undress with dissolve:
        zoom 1.25 xalign 0.5 yalign 0.0
    show tenten_lake_back_undress:
        easein 6 yalign 1.0
    if tenten_assgrab_fail == True:
        bot"Fuck! Can't believe I blew my chances with her... AGAIN!"
        bot"Stupid [bo_name]..."
    else:
        bot"Fuck! Can't believe I blew my chances with her..."
    scene black with dissolve
    jump tenten_lake_date_fail_retry_repeatable

label tenten_lake_date_assgrab_repeatable:
    if tenten_assgrab_normal == True:
        bo "Can I just... feel your ass for a few seconds again?"
        bo "You know how big of a difference it can make..."
        ten "S-sure, but be gentle!"
    else:
        bo "Can I just... feel your ass for a few seconds?"
        bo "It... it helps ground me sometimes. When the curse flares up... Physical contact..."
        ten "Grab... my ass? Seriously? Is that... part of the 'treatment' Tsunade mentioned?"
        ten "I... I don't know, [bo_name]... This feels..."
        bo "Please, Tenten? Just for a moment? If it doesn't help, I'll stop."
        ten "...Okay. Fine. Just... be quick about it."
    call hidescrollingimage2 from _call_hidescrollingimage2_63
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
    $ playmusic("audio/ost/lakedate.opus",0.3)
    $ renpy.sound.play("/audio/soun_fx/lake_owl_ambience.opus",channel="sfx2",loop=True,relative_volume=0.4)
    stop sfx4 fadeout 1
    show screen parallax1280("1h_assgrab",1.25, menuenabled=True) with dissolve
    call showscrollingimage from _call_showscrollingimage_130
    call increaselust(10) from _call_increaselust_231
    ten "*Gasps softly* O-okay...?"

    menu lakedate_assgrab_choice1_repeatable:

        "Pull her close and wholly grab her ass":
            call hidescrollingimage2 from _call_hidescrollingimage2_64
            scene black with dissolve
            pause(0.5)
            $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
            show screen parallax1280("2h_assgrab_v2",1.25, menuenabled=True) with dissolve
            ten "[bo_name_stutter]!"
            menu lakedate_assgrab_choice2_repeatable:
                "{color=[hatredcolor]}Finger her ass{/color}":
                    call changeHatred(1) from _call_changeHatred_156
                    bo "Tenten... Bent over a bit more... just for a second."
                    ten "Wh-what? Why?"
                    call hidescrollingimage2 from _call_hidescrollingimage2_65
                    scene black with dissolve
                    "Before she can fully react, you move your hand right between her asscheeks, your fingers probing gently at first."
                    show screen parallax1280("finger",1.25,1.0) with flash
                    $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                    call showscrollingimage from _call_showscrollingimage_131
                    ten "Eek! [bo_name]! Stop it! What are you doing?!" with vpunch
                    call hidescrollingimage2 from _call_hidescrollingimage2_66
                    scene black with dissolve
                    $ renpy.sound.play("/audio/soun_fx/water_move_2.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                    "She pushes you away forcefully, eyes wide with betrayal and disgust."
                    show screen parallax1280("pov2_angry",1.25,0.3) with dissolve
                    ten "I offered to help you because you said you were in pain, not so you could just... do that to me!"
                    ten "I thought maybe you were different, but you're just like everyone else!"
                    call hidescrollingimage2 from _call_hidescrollingimage2_67
                    "Tenten stepped out of the water to dry herself..."
                    show tenten_lake_back_undress with dissolve:
                        zoom 1.25 xalign 0.5 yalign 0.0
                    show tenten_lake_back_undress:
                        easein 6 yalign 1.0
                    bot"Fuck! Can't believe I blew my chances with her..."
                    scene black with dissolve                    
                    call hidescrollingimage2 from _call_hidescrollingimage2_68
                    jump tenten_lake_date_fail_permanent_label_repeatable

                "{color=[dominancecolor]}Touch her pussy{/color}":
                    bo "Just... let me..."
                    call hidescrollingimage2 from _call_hidescrollingimage2_69
                    scene black with dissolve
                    "You shift your grip slightly, letting your fingers slip inside her pussy."
                    $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                    call changeDominance(1) from _call_changeDominance_107
                    show screen parallax1280("finger_front",1.25) with flash
                    call showscrollingimage from _call_showscrollingimage_132
                    ten "N-no! [bo_name], don't!" with vpunch
                    call hidescrollingimage2 from _call_hidescrollingimage2_70
                    scene black with dissolve
                    $ renpy.sound.play("/audio/soun_fx/water_move_2.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                    "She shoves your hand away, looking horrified."
                    show screen parallax1280("pov2_angry",1.25,0.3) with dissolve
                    if tenten_pussy_fail == True:
                        ten "Again? You clearly have no respect for boundaries!"
                    ten "I said I'd help, but... not like that! What's wrong with you?!"
                    bo"S-sorry! I thought we had something going here..."
                    ten"Ugh! Men..."
                    scene black
                    call hidescrollingimage2 from _call_hidescrollingimage2_71
                    ten"Boys, rather!" with vpunch
                    ten"Immature little boys..."
                    "Tenten stepped out of the water to dry herself..."
                    show tenten_lake_back_undress with dissolve:
                        zoom 1.25 xalign 0.5 yalign 0.0
                    show tenten_lake_back_undress:
                        easein 6 yalign 1.0
                    if tenten_pussy_fail == True:
                        bot"Fuck! Can't believe I blew my chances with her... AGAIN!"
                    else:
                        bot"Fuck! Can't believe I blew my chances with her..."
                    scene black with dissolve                    
                    call hidescrollingimage2 from _call_hidescrollingimage2_72
                    jump tenten_lake_date_fail_retry_repeatable

                "{color=[dominancecolor]}Fuck her thighs{/color}":
                    call checkDominance(20,"lakedate_assgrab_choice2_repeatable") from _call_checkDominance_37
                    bo "Just like this... hold still..."
                    call hidescrollingimage2 from _call_hidescrollingimage2_73
                    scene black with dissolve
                    "You reposition yourself slightly, pressing your hardening erection against the inside of her upper thighs, trapping it between them."
                    $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                    show screen parallax1280("tenten_ts_anim1",1.25, 0.8) with flash
                    call showscrollingimage from _call_showscrollingimage_133
                    if tenten_date_thighfuck == True:
                        ten "Y-you really enjoy my thighs don't you?"
                        bo "In fact I c-can't get enough of them..."
                    else:
                        ten "Wh-what are you...? [bo_name]! This is...!"
                        "She tenses up, her breathing becoming shallow..."
                        bo"Is it o-okay if I..."
                    call hidescrollingimage2("Click twice to thrust deeper!") from _call_hidescrollingimage2_74
                    call changeDominance(1) from _call_changeDominance_108
                    hide screen parallax1280
                    show screen parallax1280("tenten_ts_anim1_1",1.25, 0.8) with vpunch
                    ten"It doesn't seem that b-bad to m-me..."
                    ten"Is this what you need to f-feel better?"
                    call hidescrollingimage2("Click twice to use her thighs!") from _call_hidescrollingimage2_75
                    $ renpy.sound.play("/audio/soun_fx/handjob3.opus", channel="sfx1", loop=True, relative_volume = 0.8)
                    hide screen parallax1280
                    show screen parallax1280("tenten_thighsex_1",1.25, 0.8)
                    with dissolve
                    bo"I feel like it really helps, Tenten!"
                    ten"Good l-lord, [bo_name_stutter]!?"
                    bo "Ngh... Tenten... your thighs... so soft... so warm..."
                    ten "[bo_name]! Wh-what are you doing?! That's not...!"
                    bo "Can't... help it... Feels too good... Need this... The curse..."
                    ten "Is.. is it really helping?"
                    bo "Just... hold still... please..."
                    "She bites her lip, looking torn between pulling away and letting you continue, her hands gripping your shoulders tightly."
                    call hidescrollingimage2("Click twice to thrust harder!") from _call_hidescrollingimage2_76
                    hide screen parallax1280
                    show screen parallax1280("tenten_thighsex_1_fast",1.25, 0.8)
                    with dissolve
                    bo "Ngh... Almost... Tenten, just a bit more..."
                    ten "You're... you're going so fast...!"
                    bo "It feels... so good... Hnngh!"
                    ten "*Small gasp* Be careful...!"
                    scene black with dissolve
                    $ renpy.sound.play("/audio/soun_fx/water_move_3.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                    show screen parallax1280("tenten_ts_anim2",1.25, menuenabled=True) with flash
                    bo "*Hhh... Ngh...*"
                    ten "..."
                    jump lakedate_thighjob_choice_repeatable

                    menu lakedate_thighjob_choice_repeatable:
                        ten "..."
                        "Keep going...":
                            bo "Almost there, Tenten... just... hold on..."
                            show screen parallax1280("tenten_thighsex_2",1.25, 0.8) with dissolve
                            ten"H-hold on a moment! W-where do you plan to..."
                            show screen parallax1280("tenten_thighsex_2_fast",1.25, 0.8) with dissolve
                            "You increase the pace, rubbing yourself raw against her soft inner thighs."
                            bo"W-where else, Tenten..."
                            ten"You are c-close to somewhere you shouldn't be. C-careful!" with vpunch
                            bo"I... I a-am!" with flash
                            $ renpy.sound.play("/audio/soun_fx/cum5.opus", channel="sfx3", loop=False, relative_volume = 0.3)
                            show screen parallax1280("tenten_ts_cum1",1.25, 0.8) with flash
                            $ renpy.sound.stop(channel="sfx1") # Stop thighjob loop
                            bo"I am c-cumming!"
                            ten"!" with vpunch
                            if tsunade_discovery_seen == True:
                                $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx4", loop=False, relative_volume = 1.2)
                                bot "W-wait! Tsunade's discovery... If it touches her, w-will she..." with vpunch
                                bot "Tenten... For your own sake I really hope the water around us is enough to dilute it."
                                bo "I can't hold back anymore!"
                            $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx3", loop=False, relative_volume = 0.3) 
                            show screen parallax1280("tenten_ts_cum2",1.25, 0.8) with longerflash
                            call decreaselust(100) from _call_decreaselust_107
                            "You shudder, releasing onto her legs and into the water."
                            call hidescrollingimage2 from _call_hidescrollingimage2_77
                            scene black with dissolve
                            $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                            show screen parallax1280("both_in_lake_submerged2",1.25) with dissolve
                            call showscrollingimage from _call_showscrollingimage_134
                            "Tenten stares down at the mess with wide, unblinking eyes, trembling slightly."
                            ten "You... you finished..."
                            bo "I... yeah. Thank you, Tenten. The... the pain is easing now."
                            ten "..." 
                            $ tenten_helped_release = True
                            call hidescrollingimage2 from _call_hidescrollingimage2_78
                            scene black with dissolve
                            jump tenten_lake_date_ending_kind_repeatable

                        "Pull back and ask for a handjob":
                            $ renpy.sound.stop(channel="sfx1") 
                            call hidescrollingimage2 from _call_hidescrollingimage2_79
                            scene black with dissolve
                            $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                            "You stop moving, pulling back slightly and hiding back into the water out of embarrassment, still not quite believing what's happening."
                            $ renpy.sound.play("/audio/soun_fx/water_move_2.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                            show screen parallax1280("both_in_lake_slightly_submerged",1.25) with dissolve
                            call showscrollingimage from _call_showscrollingimage_135
                            bo "Tenten... This is... maybe making it worse... The friction..."
                            bo "I think... what Tsunade said... about direct... 'manual stimulation'..."
                            ten "You mean...?"
                            "She looks hesitant but relieved it's not some of the worse ideas she had in mind."
                            bo "Could you... just... use your hand? Like we talked about?"
                            jump tenten_lake_date_handjob_scene_repeatable

                        "Stop and apologize":
                            call hidescrollingimage2 from _call_hidescrollingimage2_80
                            $ renpy.sound.stop(channel="sfx1") 
                            scene black with dissolve
                            "You suddenly stop, pulling away."
                            $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                            show screen parallax1280("both_in_lake_slightly_submerged",1.25) with dissolve
                            call showscrollingimage from _call_showscrollingimage_136
                            bo "I... I'm sorry, Tenten. This isn't right. I shouldn't have..."
                            "She looks surprised by your apology, her tension easing slightly."
                            ten "[bo_name]... It's okay. You said it was the curse..."
                            bo "Still... I took advantage. Let's just... forget it."
                            bot "Managed to pull back before things got worse. Good."
                            call hidescrollingimage2 from _call_hidescrollingimage2_81
                            scene black with dissolve
                            jump tenten_lake_date_ending_kind_repeatable

                "Ask for more":
                    "You hold her close for another moment, then release your grip."
                    $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                    show screen parallax1280("both_in_lake_slightly_submerged",1.25) with dissolve
                    call showscrollingimage from _call_showscrollingimage_137
                    bo "Tenten.. I think... just holding you isn't quite enough... The pain..."
                    bo "It feels like... I need that 'release' Tsunade mentioned."
                    ten "Release...? You mean..."
                    "She looks nervous, understanding dawning."
                    bo "Yeah... If you could... just... with your hand? Please?"
                    ten "...Okay, [bo_name]. If it's really for the pain... I'll help."
                    jump tenten_lake_date_handjob_scene_repeatable

        "{color=[hatredcolor]}Finger her ass{/color}":
            call changeHatred(1) from _call_changeHatred_157
            bo "Tenten... Bent over a bit more... just for a second."
            ten "Wh-what? Why?"
            call hidescrollingimage2 from _call_hidescrollingimage2_82
            scene black with dissolve
            "Before she can fully react, you move your hand right between her asscheeks, your fingers probing gently at first."
            show screen parallax1280("finger",1.25,1.0) with flash
            $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
            call showscrollingimage from _call_showscrollingimage_138
            ten "Eek! [bo_name]! Stop it! What are you doing?!" with vpunch
            call hidescrollingimage2 from _call_hidescrollingimage2_83
            scene black with dissolve
            $ renpy.sound.play("/audio/soun_fx/water_move_2.opus", channel="sfx1", loop=False, relative_volume = 0.5)
            "She pushes you away forcefully, eyes wide with betrayal and disgust."
            ten "That's NOT okay! Get away from me!"
            show screen parallax1280("pov2_angry",1.25,0.3) with dissolve
            ten "I offered to help you because you said you were in pain, not so you could just... do that to me!"
            ten "I thought maybe you were different, but you're just like everyone else!"
            call hidescrollingimage2 from _call_hidescrollingimage2_84
            "Tenten stepped out of the water to dry herself..."
            show tenten_lake_back_undress with dissolve:
                zoom 1.25 xalign 0.5 yalign 0.0
            show tenten_lake_back_undress:
                easein 6 yalign 1.0
            bot"Fuck! Can't believe I blew my chances with her..."
            scene black with dissolve                    
            call hidescrollingimage2 from _call_hidescrollingimage2_85
            jump tenten_lake_date_fail_permanent_label_repeatable

        "{color=[dominancecolor]}Touch her pussy{/color}":
            bo "Just... let me..."
            call hidescrollingimage2 from _call_hidescrollingimage2_86
            scene black with dissolve
            "You shift your grip slightly, letting your fingers slip inside her pussy."
            $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
            show screen parallax1280("finger_front",1.25) with flash
            call showscrollingimage from _call_showscrollingimage_139
            call changeDominance(1) from _call_changeDominance_109
            ten "N-no! [bo_name], don't!" with vpunch
            call hidescrollingimage2 from _call_hidescrollingimage2_87
            scene black with dissolve
            $ renpy.sound.play("/audio/soun_fx/water_move_2.opus", channel="sfx1", loop=False, relative_volume = 0.5)
            "She shoves your hand away, looking horrified."
            show screen parallax1280("pov2_angry",1.25,0.3) with dissolve
            if tenten_pussy_fail == True:
                ten "Again? You clearly have no respect for boundaries!"
            ten "I said I'd help, but... not like that! What's wrong with you?!"
            bo"S-sorry! I thought we had something going here..."
            ten"Ugh! Men..."
            scene black
            call hidescrollingimage2 from _call_hidescrollingimage2_88
            ten"Boys, rather!" with vpunch
            ten"Immature little boys..."
            "Tenten stepped out of the water to dry herself..."
            show tenten_lake_back_undress with dissolve:
                zoom 1.25 xalign 0.5 yalign 0.0
            show tenten_lake_back_undress:
                easein 6 yalign 1.0
            if tenten_pussy_fail == True:
                bot"Fuck! Can't believe I blew my chances with her... AGAIN!"
            else:
                bot"Fuck! Can't believe I blew my chances with her..."
            scene black with dissolve                    
            call hidescrollingimage2 from _call_hidescrollingimage2_89
            jump tenten_lake_date_fail_retry_repeatable

        "Ask for more":
            "You hesitantly release your grip."
            $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
            show screen parallax1280("both_in_lake_slightly_submerged",1.25) with dissolve
            call showscrollingimage from _call_showscrollingimage_140
            bo "Tenten.. I think... just that isn't quite enough... The pain..."
            bo "It feels like... I need that 'release' Tsunade mentioned."
            ten "Release...? You mean..."
            bo "Yeah... If you could... just... with your hand? Please?"
            jump tenten_lake_date_handjob_scene_repeatable

label tenten_lake_date_titsuck_repeatable:
    if tenten_date_titsuck == True:
        bo "Maybe... Could I... suck on your... Like last time?"
        ten "You know, it's still kinda weird but... If it helps with your c-condition, maybe."
    else:
        bo "Maybe... Could I... suck on your... ?"
        ten "Suck... suck my *what*?! [bo_name], are you serious? How is *that* supposed to help with your... 'condition'?"
        bo "I... I don't know! It's... maybe the closeness? The... comfort? Tsunade said... unconventional things might help manage the... urges... the pain..."
        ten "Unconventional is one thing, [bo_name], but this is..." 

    menu tenten_lake_date_titsuck_choice_repeatable:
        bot "Okay, maybe that was a weird ask still. How do I play this?"

        "{color=[hatredcolor]}Don't question it, just let me.{/color}":
            call hidescrollingimage2 from _call_hidescrollingimage2_90
            bo "Less talking, more helping."
            scene black with dissolve
            "Ignoring her hesitation, you reach out quickly, cupping her breast through her wet top."
            $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
            stop sfx4 fadeout 1
            show screen parallax1280("titgrab",1.25, 1.0) with flash
            call showscrollingimage from _call_showscrollingimage_141
            call changeHatred(1) from _call_changeHatred_158
            bo"That's a nice pair you have on you, Tenten!"
            ten "H-hey! W-what are you doing all of a sudden!" with vpunch
            call hidescrollingimage2 from _call_hidescrollingimage2_91
            scene black with dissolve
            $ renpy.sound.play("/audio/soun_fx/water_move_2.opus", channel="sfx1", loop=False, relative_volume = 0.5)
            "She slaps your hand away hard and scrambles back, looking furious and betrayed."
            $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
            scene black with dissolve
            show screen parallax1280("pov2_angry",1.25,0.3) with dissolve
            ten "I offered to help you because you said you were in pain, not so you could just... grope me!"
            ten "I thought maybe you were different, but you're just like everyone else!"
            call hidescrollingimage2 from _call_hidescrollingimage2_92

            "Tenten stepped out of the water to dry herself..."
            show tenten_lake_back_undress with dissolve:
                zoom 1.25 xalign 0.5 yalign 0.0
            show tenten_lake_back_undress:
                easein 6 yalign 1.0
            ten "I try to be understanding because you're supposedly in pain, and you pull this?! You're disgusting!"
            bot"Fuck! Can't believe I blew my chances with her..."
            scene black with dissolve
            jump tenten_lake_date_fail_permanent_label_repeatable

        "Please, Tenten? Just for a little bit?":
            if tenten_date_titsuck == True:
                bo "Please? I'm sure it won't be as awkward as last time..."
                bo "And it really really helped!"
                ten "F-fine, I guess I'm getting used to it now..."
            else:
                bo "Please? I know it sounds crazy... but the pain is really bad right now. Maybe... maybe the warmth... or... something... might just... calm it down? If it doesn't work, I'll stop immediately. Promise."
                ten "..."
                ten "This is... really weird, [bo_name]. Are you *sure* this isn't just... you being...?" 
                bo "No! It's the curse, I swear! Please?"
                ten "*Sighs deeply*... Fine. Fine! But just for a *minute*. And if this is some kind of trick..."

            menu tenten_lake_date_titsuck_agreed_repeatable:
                "Suck on her breasts.":
                    call hidescrollingimage2 from _call_hidescrollingimage2_93
                    scene black with dissolve
                    "She looks away, face burning red, standing rigidly..."
                    stop sfx4 fadeout 1
                    show screen parallax1280("titgrab",1.25,1.0) with dissolve        
                    "You lean in, your heart pounding..."
                    $ renpy.sound.play("/audio/soun_fx/water_move_2.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                    ten"Gently... O-okay?"
                    bo"Y-yeah..."
                    show screen parallax1280("use1",1.25) with dissolve
                    call showscrollingimage from _call_showscrollingimage_142
                    $ renpy.sound.play("/audio/soun_fx/sucking.mp3", channel="sfx3", loop=True, relative_volume = 0.9)
                    ten "*Gasp!* Ah..." 
                    "She trembles slightly..."
                    show screen parallax1280("tenten_breastsuck_anim1",1.25, menuenabled=True) with dissolve
                    "You continue to suckle gently, the warmth and softness surprisingly calming for both of you..."
                    bot "She... she's letting me suck on her tiddies!"
                    bot"It's somewhat... comforting..."

                    menu tenten_lake_date_titsuck_ongoing_repeatable:
                        "Keep going gently":
                            "You continue your ministrations, occasionally swirling your tongue."
                            ten "*Ngh...*"
                            jump tenten_lake_date_titsuck_relief_check_repeatable

                        "Suck harder":
                            show screen parallax1280("tenten_breastsuck_anim1_1",1.25) with dissolve
                            $ renpy.sound.play("/audio/soun_fx/sucking.mp3", channel="sfx1", loop=True, relative_volume = 1.0)
                            ten "Ngh! [bo_name]... We s-said gently! R-remember?" with vpunch
                            scene black with dissolve
                            $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                            ten "Ngh! [bo_name]... We s-said gently! R-remember?" with vpunch
                            "Her breath hitches as she instinctively grabs your shoulder."
                            jump tenten_lake_date_titsuck_relief_check_repeatable

                        "Stop now":
                            $ renpy.sound.stop(channel="sfx3")
                            call hidescrollingimage2 from _call_hidescrollingimage2_94
                            scene black with dissolve
                            $ renpy.sound.play("/audio/soun_fx/water_move_2.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                            "You pull back gently."
                            bo "Okay... Okay, that's... thank you, Tenten."
                            $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                            show screen parallax1280("both_in_lake_slightly_submerged",1.25) with dissolve
                            call showscrollingimage from _call_showscrollingimage_143
                            "She avoids your gaze, still breathing a little heavily, looking incredibly flustered."
                            ten "Did... did it help? At all?"
                            bo "Yeah... a little. Thanks."
                            bot "Better stop before I push it too far."
                            call hidescrollingimage2 from _call_hidescrollingimage2_95
                            scene black with dissolve
                            jump tenten_lake_date_ending_kind_repeatable

        "Back down and apologize.":
            stop sfx4 fadeout 1
            bo "You know what? You're right. That was... a really weird and stupid thing to ask. I'm sorry, Tenten. Pain's making me say dumb things."
            "Tenten seems relieved, though still a bit wary."
            ten "B-but.. The pain, are you just gonna suffer through it?"
            bo "It's still.. hurting really bad but, it's not the f-first time I've had to endure it."
            bo "I can't be using it as an excuse to use you."
            ten "It... It's okay. Just... maybe stick to more normal requests if you need help?"
            bo "I w-will. Thank you for being so understanding, Tenten"
            bot "Managed to salvage that. Asking to suck her tits... what was I thinking?"
            call hidescrollingimage2 from _call_hidescrollingimage2_96
            scene black with dissolve
            "You do your best to cope with the pain without making things more awkward."
            "Time passes, the layer of awkwardness slowly going away."
            ten "Shall we get going?"
            $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
            bo "Last one out is cleaning shuriken for another week!"
            ten "H-hey you started moving before you said that!"
            $ renpy.sound.play("/audio/soun_fx/water_move_2.opus", channel="sfx1", loop=False, relative_volume = 0.5)
            jump tenten_lake_date_ending_kind_repeatable


label tenten_lake_date_titsuck_relief_check_repeatable:
    bo "Ngh... Tenten... I think... it's actually helping..." 
    call hidescrollingimage2 from _call_hidescrollingimage2_97
    scene black with dissolve
    $ renpy.sound.stop(channel="sfx1") 
    $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx3", loop=False, relative_volume = 0.8)
    call decreaselust(100) from _call_decreaselust_108 
    $ tenten_helped_release = True 

    "You pull away, breathing heavily but looking more relaxed."
    $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
    show screen parallax1280("both_in_lake_slightly_submerged",1.25) with dissolve
    call showscrollingimage from _call_showscrollingimage_144
    bo "Wow... I... I think the pain's gone. Thank you, Tenten. Really."
    if tsunade_discovery_seen == True:
        $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx4", loop=False, relative_volume = 1.2)
        bot "W-wait! Tsunade's discovery... My cum just t-touched her, w-will she..." with vpunch
        bot "Tenten... For your own sake I really hope the water around us is enough to dilute it."
    "Tenten stares at you, her expression a mixture of shock, embarrassment, and confusion."
    ten "It... it actually worked?"
    bo "Yeah... Yeah, it did."
    ten "That's... good. I guess."
    ten "Something like breastfeeding an infant... Eh-eh! *Nervous chuckle*"
    "She's still processing the strangeness of it all."
    ten "Just... let's not... talk about this method. Ever."
    bo "Agreed. Sealed lips..."
    call hidescrollingimage2 from _call_hidescrollingimage2_98
    scene black with dissolve

    jump tenten_lake_date_ending_kind_repeatable

label tenten_lake_date_blowjob_scene_repeatable:
    $ initialize_replay_defaults()
    $ tenten_helped_release = True
    if tenten_lake_date_bj == True:
        bo "Tenten, that time when you let me, w-with your... m-mouth."
        bo "Could we please, try it one m-more time?"
        ten "You don't need to be so awkward about it silly!"
        ten "I'm always happy to help you with your condition."
        stop sfx4 fadeout 1
        bo "T-thank you!"
    else:
        bo "Tenten... I... Th-this is really embarrassing to ask, but do you think this time... m-maybe-"
        ten "Spit it out, [bo_name]. Are you asking or just gonna stare at my lips all night?"
        show screen parallax1280("both_in_lake_slightly_submerged3_1",1.25) with dissolve
        "She notices you staring intensely at her mouth, a small, knowing smirk playing on hers."
        ten "You mean... You want something a little more... {i}direct{/i} for your... condition?"
        $ renpy.sound.play("/audio/soun_fx/water_move_2.opus", channel="sfx1", loop=False, relative_volume = 0.5)
        "She 'accidentally' brushes her hand against your hardening erection through the water as she speaks." with vpunch
        bo "*Gulp*... Y-yeah. If you could maybe use y-your m-mouth this time?"
        ten "My mouth, huh? Getting bold, aren't we, [bo_name]?"
        ten "Well... if you {i}promise{/i} you'll behave, and you genuinely think it will help... then maybe!"
        bo "R-really? You'd do that for me?"
        ten "I'm not hearing that promise, [bo_name]. And I mean it. No funny business."
        stop sfx4 fadeout 1
        bo "I promise! Cross my heart! I'll be... a distinguished gentleman."
        ten "Oh? We'll see about that! Come on then."
    scene black
    call hidescrollingimage2 from _call_hidescrollingimage2_99
    $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
    "You move to a slightly more shallow part of the lake."
    ten"Hmm..."
    ten"This will do!" with vpunch
    "Tenten grabs your hand and stops you. Before you realize it, she's on her knees..."
    $ renpy.sound.play("/audio/soun_fx/water_move_2.opus", channel="sfx1", loop=False, relative_volume = 0.5)
    $ renpy.sound.play("/audio/soun_fx/suck2.opus", channel="sfx3", loop=False, relative_volume = 1.0)
    show screen parallax1280("tenten_lake_bj_1_1") with dissolve
    call showscrollingimage from _call_showscrollingimage_145
    bo "T-t-tenten!?" with vpunch
    show screen parallax1280("tsunade_lake_bj_anim1") with dissolve
    with vpunch 
    $ renpy.sound.play("/audio/soun_fx/suck1.opus", channel="sfx1", loop=False, relative_volume = 1.0)
    $ renpy.sound.play("/audio/soun_fx/sucking.mp3", channel="sfx3", loop=False, relative_volume = 1.0)
    "There's a surprising eagerness in her touch, as if she's been waiting for this moment..."
    bot "H-holy crap, she's actually doing it! But it's almost as if she's teasing me, sucking only on the h-head..."
    bot "Still, the fact that she still trusts me despite all she knows about the curse... Out here, in the open..."
    bot "It makes me even harder!"
    bo "*Moans*... T-Tenten... D-don't stop!" with vpunch

    call hidescrollingimage2 from _call_hidescrollingimage2_100
    $ renpy.sound.play("/audio/soun_fx/water_move_3.opus", channel="sfx1", loop=False, relative_volume = 0.5)
    show screen parallax1280("tenten_lake_bj_2") with dissolve
    call showscrollingimage from _call_showscrollingimage_146
    "Her initial hesitation vanishes, as she braces your hand on your thigh, preparing to  take you deeper!"
    show screen parallax1280("tenten_lake_bj_3",1.25) with dissolve
    $ renpy.sound.play("/audio/soun_fx/bj3.opus", channel="sfx3", loop=False, relative_volume = 1.0)
    ten "*Gluck!* ngh... mmm..." with vpunch
    show screen parallax1280("tsunade_lake_bj_anim2",1.25) with dissolve
    bo "Oh, f-fuck... y-yes... j-just like that Tenten! th-that feels... ngh... s-so good..."
    bot "Damn... she's got s-skills. So much better than what I imagined!"
    bo "Don't stop! I am c-close!" with vpunch
    call hidescrollingimage2 from _call_hidescrollingimage2_101
    $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
    $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    show screen parallax1280("tenten_lake_bj_4", 1.25, menuenabled=True) with flash
    call showscrollingimage from _call_showscrollingimage_147
    $ renpy.sound.play("/audio/soun_fx/sucking.mp3", channel="sfx3", loop=False, relative_volume = 1.0)
    bot"Oh f-fuck, she is almost taking it all in!"
    ten "Mmmphh...*Gluck*... ngh!" with vpunch
    bot "I'm gonna lose control if she keeps this up... Th-this is... f-fucking intense. My whole body is on fire."
    "Control is slipping away fast, pleasure coiling tight in your gut, almost too much to handle."
    $ tenten_takecontrol = False
    menu tenten_lake_bj_options_repeatable:
        bot "Her trust is admirable. But I feel an urge that's hard to control! My c-condition is flaring up!"

        "{color=[dominancecolor]}Take control and grab her head{/color}":
            default tenten_takecontrol = False
            $ tenten_takecontrol = True
            call checkDominance(20, "tenten_lake_bj_options_repeatable") from _call_checkDominance_38
            bot "Th-this is incredible... b-but I need more. I need to guide her. Show her how I want it."
            bo "S-sorry, Tenten... You are doing great but..."
            call hidescrollingimage2 from _call_hidescrollingimage2_102
            scene black with dissolve
            "Reaching down, your hands find the back of her head, fingers gently tangling in her hair."
            bo "L-let me... help you!"
            $ renpy.sound.play("/audio/soun_fx/water_move_2.opus", channel="sfx1", loop=False, relative_volume = 0.5)
            show screen parallax1280("tenten_lake_bj_dom5", 1.25) with dissolve
            call showscrollingimage from _call_showscrollingimage_148
            $ renpy.sound.play("/audio/soun_fx/hima_gag.opus", channel="sfx3", loop=False, relative_volume = 1.0)
            ten "*Gluck*!" with vpunch
            call changeDominance(2) from _call_changeDominance_110
            "She looks up, eyes wide with surprise. A muffled gasp for air escaping her, before you gently but firmly push her head back down."
            bo "Y-yeah... th-that's it... all the way!"
            bo "You are f-fucking amazing Tenten..."
            bo "But I think you c-can do even b-better..."
            call hidescrollingimage2 from _call_hidescrollingimage2_103
            $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
            $ renpy.sound.play("/audio/soun_fx/hima_gag.opus", channel="sfx3", loop=False, relative_volume = 1.0)
            show screen parallax1280("tenten_lake_bj_dom6", 1.25) with dissolve
            call showscrollingimage from _call_showscrollingimage_149
            "You pushed Tenten all the way to the base..."
            $ renpy.sound.play("/audio/soun_fx/gluck1.opus", channel="sfx3", loop=False, relative_volume = 1.6)
            show screen parallax1280("tsunade_lake_bj_anim2_2", 1.25) with dissolve
            "Setting a harder pace, your hips started to move. Tenten whimpers, but doesn't give up and instead, tries to keep up."
            bo "S-so good... You t-take it so well, Tenten... *Moans*..."
            
            show screen parallax1280("tsunade_lake_bj_anim2_3", 1.25) with dissolve
            $ renpy.sound.play("/audio/soun_fx/bjair2.opus", channel="sfx3", loop=False, relative_volume = 0.8)
            $ renpy.sound.play("/audio/soun_fx/gluck2.opus", channel="sfx1", loop=False, relative_volume = 1.5)
            ten "*Gluck!* glph... ngh..."
            bot "She's... she's actually taking it. Fuck, this is driving me crazy!" with flash
            call hidescrollingimage2("Click twice to cum!") from _call_hidescrollingimage2_104
            $ renpy.sound.play("/audio/soun_fx/water_move_3.opus", channel="sfx1", loop=False, relative_volume = 0.5)
            show screen parallax1280("tenten_lake_bj_dom6_2", 1.25) with flash
            $ renpy.sound.play("/audio/soun_fx/cum9.opus", channel="sfx3", loop=False, relative_volume = 0.6)
            $ renpy.sound.play("/audio/soun_fx/hima_gag.opus", channel="sfx2", loop=False, relative_volume = 1.2)
            call showscrollingimage from _call_showscrollingimage_150
            bot"*Moans* Aaagh! F-fuck! The back of your t-throat feels so nice!" with flash
            show screen parallax1280("tenten_lake_bj_dom6_3", 1.25) with dissolve
            $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx3", loop=False, relative_volume = 0.6)
            "You explode, shooting your load deep down her throat, your hands still gripping her head. Her eyes widened in shock..." with flash
            show screen parallax1280("tenten_lake_bj_end1", 1.25) with flash
            $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx3", loop=False, relative_volume = 0.6)
            $ renpy.sound.play("/audio/soun_fx/hima_gag.opus", channel="sfx2", loop=False, relative_volume = 1.2)
            call decreaselust(100) from _call_decreaselust_109
            ten "*Gagging softly* Mmph-Gwak!" with vpunch
            "Tenten trembles, fingers digging into your thighs, as she feels your final pump flooding her throat. Your grip loosens..."
            bo "*Panting* H-holy shit..."
            scene black
            call hidescrollingimage2 from _call_hidescrollingimage2_105
            jump tenten_lake_date_blowjob_climax

        "{color=[hatredcolor]}*The beast growls...*{/color}":# (supporter_scene = True)
            call checkHatred(30, "tenten_lake_bj_options_repeatable") from _call_checkHatred_22
            label thebeastgrowls:
            $ initialize_replay_defaults()
            jump tenten_beast_growls
            # $ call_label_action("tenten_beast_growls")
            call supp_rew from _call_supp_rew_5
            jump tenten_lake_bj_options_repeatable
            

        "Let her take control.":
            call hidescrollingimage2 from _call_hidescrollingimage2_106
            scene black with dissolve
            "She looks up at you with a determined glint in her eyes."
            ten "I... I want to do this right for you, [bo_name]."
            ten "You can... guide me. Tell me what you like. I want to make you feel good."
            bo "Tenten... are you s-sure? You don't have to prove anything."
            bot "Her willingness, her desire to please... it's stirring something deep within me. A different kind of heat."
            ten "I'm sure. I want this. Let me."
            $ renpy.sound.play("/audio/soun_fx/bj3.opus", channel="sfx3", loop=False, relative_volume = 0.9)
            $ renpy.sound.play("/audio/soun_fx/water_move_2.opus", channel="sfx1", loop=False, relative_volume = 0.5)
            show screen parallax1280("tenten_lake_bj_4", 1.25) with dissolve
            call showscrollingimage from _call_showscrollingimage_151
            bo "W-woah, Tenten... *Moans* Th-that's..."
            ten "Shhh... Just... r-relax."
            bot "She's incredible... Taking charge like this... It's... I'm losing it." with flash
            show screen parallax1280("blackscreen", 1.25) with dissolve
            ten"You can... touch me if you'd like, show me where it feels good for you..."
            $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
            bo"A-are you sure...?"
            "Tenten grabs one of your hands, and places it on her head..."
            show screen parallax1280("tsunade_lake_bj_anim2_2", 1.25) with dissolve
            $ renpy.sound.play("/audio/soun_fx/gluck1.opus", channel="sfx3", loop=False, relative_volume = 1.0)
            bot "Fuck, she's good. Her tongue, her lips... she knows exactly what she's doing!"
            bo "Tenten... you're... you're so... d-damn... good! I c-can't..." with flash
            $ renpy.sound.play("/audio/soun_fx/gluck2.opus", channel="sfx3", loop=False, relative_volume = 1.0)
            ten "Mmmph... *Gluck*... mmm..." with vpunch
            bo "You're driving me wild... I am a-about to..." with flash
            call hidescrollingimage2("Click twice to cum!") from _call_hidescrollingimage2_107
            $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
            $ renpy.sound.play("/audio/soun_fx/cum4.opus", channel="sfx3", loop=False, relative_volume = 0.6)
            show screen parallax1280("tenten_lake_bj_dom6_2", 1.25) with flash
            call showscrollingimage from _call_showscrollingimage_152
            "Overwhelmed by your desires, you carelessly let your release flood her throat, considering her earlier initiative as consent."
            bo "T-there's more c-coming! *Moans*" with vpunch
            $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx3", loop=False, relative_volume = 0.6)
            show screen parallax1280("tenten_lake_bj_dom6_3", 1.25) with longerflash
            $ renpy.sound.play("/audio/soun_fx/gags/SDTGag13.opus", channel="sfx3", loop=False, relative_volume = 1.0)
            bo "Aaarhh! I am c-cumming!" with flash
            $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx3", loop=False, relative_volume = 1.0)
            "Her whole body trembles, eyes widen, as you release another load, catching her by surprised and flooding her throat with your semen."with flash
            "She moans around your cock, taking all of your cum, swallowing hard as you shoot your load."
            call decreaselust(100) from _call_decreaselust_110
            jump tenten_lake_date_blowjob_climax

label tenten_lake_date_blowjob_climax:
    $ renpy.sound.stop(channel="sfx2")
    scene black with dissolve
    call hidescrollingimage2 from _call_hidescrollingimage2_108
    "You black out for a second, as Tenten slowly retreats, semen gushing out of her mouth..."
    $ renpy.sound.play("/audio/soun_fx/gaspforair3.opus", channel="sfx2", loop=False, relative_volume = 0.7)
    $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
    $ renpy.sound.play("/audio/soun_fx/panting.opus", channel="sfx3", loop=False, relative_volume = 1.0)
    show screen parallax1280("tenten_lake_bj_end2", 1.25) with flash
    call showscrollingimage from _call_showscrollingimage_153
    bo"T-tenten... Are you okay? *Panting* I can't believe you..."
    "She looks at you, eyes kinda dazed. She opens her mouth a little, showing your thick cum all over her tongue."
    bo"...Y-you took that so well!" with vpunch
    if tsunade_discovery_seen == True:
        $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx4", loop=False, relative_volume = 1.2)
        bot "W-wait! Tsunade's discovery... I really fucked up this time, w-will she..." with vpunch
        bot "Tenten... For your own sake I really hope that..."
    $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx4", loop=False, relative_volume = 1.2)
    show screen parallax1280("tenten_lake_bj_end3", 1.25) with flash
    ten "Mmph... *cough softly*... Hahhh..."
    "Her mouth is full of your cum. Some of it dribbles down her chin."
    if tenten_takecontrol == True:
        ten"That... *Heavy breathing* was not very nice of you now... was it?"
    $ renpy.sound.play("/audio/soun_fx/swallow.opus", channel="sfx3", loop=False, relative_volume = 1.0)
    show screen parallax1280("tenten_lake_bj_end3_1", 1.25) with dissolve
    call showscrollingimage from _call_showscrollingimage_154
    "She swallows it all down. A drop runs down her chin but she wipes it off, almost unfazed."
    bo "You... you s-swallowed? Tenten, you... you didn't have to..."
    ten "*Clears throat, voice still husky*... W-well... seemed like a waste t-to spit it in the lake, r-right? Bad for the... f-fish, or something."
    ten "Besides... a promise is a promise. I said I'd help you... with your... {i}condition{/i}." 
    "She gives you a shaky, tired smile. It looks genuine. Her eyes are still a bit wild, almost mischievous."
    if tenten_takecontrol == True:
        bo"Was that... too m-much for you? S-sorry, I got a bit lost in my-"
        ten"That? That was nothing [bo_name]. I've been beaten down and roughed up by life for more years than you were alive." with vpunch
        ten"I am more resilient than what you think! In fact... "
        ten"I quite enjoy the...*Giggles*, handsy side of sex, if you know what I mean!"
        ten"Although I would appreciate a more cooperative approach next time!"
        bo"Tenten..."

    else:
        bot "She... she actually smiled. After all that. Maybe... maybe she l-likes me!?"
    ten"Come on, let's gather ourselves!"
    call hidescrollingimage2 from _call_hidescrollingimage2_109
    $ tenten_lake_date_bj = True
    scene black with dissolve
    $ renpy.sound.stop(channel="sfx1")
    call showscrollingimage from _call_showscrollingimage_155
    show screen parallax1280("pov2_1talk", 1.25) with dissolve
    $ renpy.sound.play("/audio/soun_fx/water_move_2.opus", channel="sfx1", loop=False, relative_volume = 0.5)
    ten "Feeling better, [bo_name]?"
    bo "Y-yeah... much better. Th-that was... incredible."
    ten "I enjoyed your company too, [bo_name]. Just doing my part to help with your 'condition'!"
    bo "R-right... the condition... Still... thank you. You're... really something."
    ten "Heh. Don't get too flustered on me now."
    ten "Shall we get going? It's getting late, your parents will start wondering where you are! If they figure you were out with a woman twice your age..."
    bo "Don't w-worry, not a word of this to anyone else!" with vpunch
    bo "It will be our s-secret!"
    ten "Good boy! *Giggles*"
    scene black
    call hidescrollingimage2 from _call_hidescrollingimage2_110
    $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
    "She keeps teasing you playfully, as you both start drying yourselves..."

    jump tenten_lake_date_ending_kind_repeatable


label tenten_lake_date_ending_kind_repeatable:
    $ tenten_date_success = True
    $ tenten_date_counter += 1
    $ tenten_last_date_day = day_number
    $ tenten_date_decline_counter = 0
    $ tenten_days_since_agreed = 0 # Reset waiting counter
    $ tenten_date_agreed = False # Date is done, agreement fulfilled
    $ tenten_lake_date_fail_retry = 0 # Reset fail retry to 0 in case there were previous failed tries that now led to success
    $ tenten_date_success_repeatable += 1
    $ tenten_date_shop_dialogueflavor_mentioned = False

    scene black with dissolve
    pause(1)
    $ playmusic("audio/ost/lakedate.opus",0.3)

    if tenten_helped_release:
        "You both take some time to dress back up. The initial awkwardness dissipates, as you both get comfortable in each other's presence. "
        scene bg_night_forest3 with dissolve
        "The walk back continues with the usual back and forth teasing between you."
        show ten sad2 at right with dissolve
        ten "That was-"
        show boruto embarassed at left with dissolve
        bo "Amazing! I m-mean..." with vpunch
        show boruto normal with dissolve
        bo "No, I said what I said. It was great. You're great, Tenten..."
        bo "Thank you. For... everything. You really helped."
        ten "Don't get too used to it, kid!"
        show boruto snob with dissolve
        bo "Ok... mom!" with vpunch
        ten "D-don't say that, you idiot! That's actually kinda weird!"
        bo "You started it, don't call me a kid!"
        scene black with dissolve
        "You share a laugh together."
        ten "We should probably get going by now, It's getting late."
        bo "Right."
    else:
        scene bg_night_forest3 with dissolve
        "You start making your way back."
        show boruto laughing at left:
            xalign 0.3
        show ten sad2 at right:
            xalign 0.7
        with dissolve
        ten "I actually had a really nice time, [bo_name]. Despite the... awkward bits."
        bo "Me too. you are fun to be around, Tenten."
        bo "Should we... do this again sometime?"
        ten "I'd like that..."
        bo "Great! Then it's settled."
        ten "It is getting a bit chilly out here though, maybe we should head back?"
        bo "Yeah, probably for the best. Don't want my favorite shopkeeper to catch a cold!"
        ten "*Giggles softly* Right."
        "You both retrieve your clothes from the shore."
        show boruto:
            easein 2 xalign -3
        show ten:
            easein 2 xalign -3
        with moveoutleft
        hide ten
        hide boruto
        scene black
        with dissolve
        bot "That went... surprisingly well. Maybe there's something here after all."

    "You walk back towards the village together, a comfortable silence settling between you."
    scene bg ramenshop night with dissolve
    show ten sad2 at center with dissolve
    ten"Thank you for accompanying me, [bo_name]..."
    ten"I'll see you again sometime soon, right?"
    hide ten with dissolve
    bo"I'll see you around."
    scene black with dissolve
    bot "That was... even better than last time. I think this is starting to become something more!"
    jump tenten_date_end_cleanup_repeatable

label tenten_date_end_cleanup_repeatable:
    $ tenten_date_agreed = False

    $ renpy.sound.stop(channel="music") 
    $ renpy.end_replay() 
    stop sound channel "sfx1"
    jump action_taken