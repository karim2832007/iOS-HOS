transform fadeinandout:
    linear 2 alpha 0.1
    linear 2 alpha 0.9
    repeat

label ch1_d14_moneyproblems:
    default ch1_d14_moneyproblems_completion = False
    $ ch1_d14_moneyproblems_completion = True
    show eyeclosed
    show hinaq1bg 2 behind eyeclosed:
        blur 6

    call blink("...", "What's up with the commotion downstairs...","O-oh shit!") from _call_blink_5
    scene black with dissolve
    bot"Must be those debt-collecting assholes again..."
    $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    show bg bb day with dissolve
    show boruto surprised2 with dissolve
    bot"I should hurry downstairs and take care of this..."
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/footsteps.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    bot"One way or another!"
    #todo jumps for repetitons
    if ch1_d14_moneyproblems_completion == True and toji_defeated == True:
        jump daimyo_debt_collect_repeat
    elif ch1_d14_moneyproblems_completion == True and toji_pay300 == True:
        jump daimyo_debt_collect_repeat

    else:
        pass
    $ ch1_d14_moneyproblems_completion = True
    scene debtcollector_repeat with dissolve:
        yalign 1.0
    show debtcollector_repeat:
        easein 4 yalign 0.0
    to"You know why we are here, don't you... pretty little lady!"
    hin"Y-yes, but I..."
    "An all too familiar figure menacingly stood by the doorway, almost inviting himself inside your house..."
    "[hin_name] heard you coming. With an uncertain look she turned towards you as if she was asking for help..."
    menu:
        "[hin_name] heard you coming. With an uncertain look she turned towards you as if she was asking for help..."
        "Don't worry [hin_rel]. I'll take care of this!":
            bo"Are the debt collectors causing trouble again?"
            hin"[bo_name]..."
            call changeRespect("Hinata",1) from _call_changeRespect_239
            bo"Don't worry [hin_rel], I'll handle th-"
        "Stare at her ass...":
            show debtcollector_repeat:
                easein 2 yalign 1.0
            "You paid no attention at the severity of the situation. Instead..."
            bot"You went and got yourself in trouble again, didn't you [hin_rel]..."
            call changeRespect("Hinata",-2) from _call_changeRespect_240
            "[hin_name] noticed you standing idly."
            bot"I bet that ass of yours is going to keep causing trouble to plenty of men..."
            call increaselust(10) from _call_increaselust_283
            bot"...Including me!"
    scene black with vpunch
    to"Pay attention when I am talking to you!" with vpunch
    scene debtcollector_repeat1 with dissolve:
        yalign 1.0
    show debtcollector_repeat1:
        easein 2 yalign 0.0
    "The menacing man grabbed [hin_name]'s chin and turned her gaze away from you, and onto him..."
    to"You don't want to provoke my temper any more, little lady..."
    show love_choice with dissolve
    $ renpy.sound.play("/audio/soun_fx/heartbeatlong.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    stop music fadeout 2
    menu randomjumpmenu_d14:
        to"You don't want to provoke my temper any more, little lady..."
        "{color=[lovecolor]}That's enough, shithead!{/color}":
            hide love_choice
            scene black
            with dissolve
            bo"You fucking asshole..."
            $ renpy.music.play("audio/ost/borutotheme.opus", channel="music", loop=True, relative_volume = 0.6)
            $ renpy.sound.play("/audio/soun_fx/slapecho.opus", channel="sfx2", loop=False, relative_volume = 1.5)
            show dm_fight_intervene with flash
            bo"That's enough, shithead!" with vpunch
            to"Oi, oi..."
            show hin_in_fight with easeinright
            hin"[bo_name_stutter]!"
            "You swoop in, slamming Toji's hand away, and placing yourself between him and [hin_name]!"
            bo"To think he'd put his hands on you..."
            bo"Stay back [hin_rel]! I'll deal with this asshole!"
            show hin_in_fight at smallshake
            hin"Be c-careful!"
            hide hin_in_fight with dissolve
            scene bg porch with dissolve
            show shina surprised3 at left
            show demandingmen badguys1:
                xpos 570 yalign 1.0 xzoom -1.0 yzoom 1.12 zoom 1.21 
            with dissolve
            if lost_toji_fight == True:
                to"Bwaaaa-haaa-ha! Came back for another ass-beating you little shit?"
            else:

                to "Trust me on this one, my lady, you don't want to intervene..."
                to "Adding an injunction of violence on top of failing to pay your debts wouldn't be well received by the Daimyo."
                to "Besides, my partner here may be a bit less... intellectually inclined, but even he knows that he can't just kill dumb kids."
                to "He'll probably just teach the blonde twerp a lesson, I think..."
            scene dm_fight_intervene2 with dissolve
            to"I knew you were an idiot, but it seems like you've exceeded all expectations!"
            to"You are a full-blown moron! Bwa-hah-hah!"
            to"You sure you want to have your face beaten in!?" with vpunch
           

            hin"P-please! There's no need for violence!"
            menu:
                hin"P-please! There's no need for violence!"
                "{color=[dominancecolor]}Fight him!{/color}":
                    label fight_toji_c:
                    bo"I'll beat the shit out of you!"
                    show dm_fight_intervene2 with dissolve:
                        zoom 1.4 xalign 0.4 yalign 0.0
                    to"You must be confused..."
                    scene black with vpunch
                    # show screen qte_background(bg_image="dm_fight1 afraidt")
                    show screen qte_background_boruto(dodge_image="boruto_dodge_fight")
                    show screen qte_vfx_controller
                    with dissolve
                    to"IT'LL BE ME WHO'S GOING TO BEAT THE SHIT OUT OF YOU!" with vpunch
                    "You've initiated a fight!"
                    default combat_tutorial_completed = False
                    if combat_tutorial_completed == False:
                        "Pay attention to the enemy's movement and input the displayed commands to attack or defend!"
                        "Sometimes you'll have to dodge by entering the correct sequence of inputs!\nJust like the following tutorial:"
                        call screen qte_combat(mode="defend", damage_taken=0,input_duration=10.0, input_sequence="RRRR")
                        if qte_success:
                            "You successfully evaded!"
                        else:
                            "Careful! Failing to dodge in time, or inserting the wrong inputs will result in taking damage!" with vpunch
                        "When an opportunity presents itself, be prepared to unleash your own barrage of attacks by rapidly tapping/clicking!\nJust like the following tutorial:"
                        call screen qte_combat(mode="attack", damage_taken=0,input_duration=3.0, input_sequence="spamclick")
                        $ enemy_hp = 100
                    else:
                        pass

                    "Deplete the enemy's HP bar before the enemy depletes yours!"
                    $ combat_tutorial_completed = True
                    show dm_fight1 attack with dissolve
                    to"You've dug your own grave!"
                    "Toji launches a barrage of attacks against you!"
                    show boruto_defend_fight:
                        yalign 1.0
                    with dissolve
                    $ renpy.sound.play("/audio/soun_fx/punchbarrage.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    show boruto_defend_fight at shakeforever:
                        easein 8 yalign 0.1
                    show speedlines with dissolve
                    
                    to"ORA ORA ORA ORA ORA ORA!"
                    $ renpy.sound.stop(channel="sfx2", fadeout=1)
                    scene black with flash
                    bo"..." with vpunch
                    if is_opportunity_unlocked("l2_opportunity1", strength):
                        show dm_fight1 attack with dissolve
                        to"How's that for a beating!"
                        show boruto_defend_fight2 with dissolve:
                            yalign 1.0
                        bo"Is that... all you got?"
                        show boruto_defend_fight2:
                            easein 0.4 yalign 0.4
                        bo"My turn now, asshole!" with vpunch
                        pass
                    else:
                        "Toji's barrage of attacks overwhelmed you..."
                        jump lost_toji_fight
                    # call vfx_tests
                    scene bg porchfight
                    $ qte_current_bg = "dm_fight1 afraidt"
                    show screen qte_background
                    with dissolve
                    to"W-what the... H-how the hell are you still standing!"
                    "Prepare to fight!"
                    call screen qte_combat(mode="attack", damage_taken=1,input_duration=2.0, input_sequence="spamclick")
                    if qte_success:
                        "Your attack connects!"
                    else:
                        "Your attempt to attack failed!"
                    to"S-so what if you can put up a little fight..."
                    to"No one can match my raw strength, let alone a fucking twerp like you!" with vpunch
                    call screen qte_combat("defend", 15, 3.0, "LLLL")
                    if qte_success:
                        $ qte_current_bg = "dm_fight1 afraidt"
                        "You successfully evaded the attack!"
                        $ enemy_sprite_state = "afraid"
                    else:
                        $ qte_current_bg = "dm_fight1 smugt"
                        "The enemy's strike connects!"
                    call screen qte_combat("defend", 15, 3.0, "RRRR")
                    if qte_success:
                        $ qte_current_bg = "dm_fight1 afraidt"
                        "You successfully evaded the attack!"
                        $ enemy_sprite_state = "afraid"
                    else:
                        $ qte_current_bg = "dm_fight1 smugt"
                        "The enemy's strike connects!"
                    bot"An opening! It's time to utilize my Ninjutsu!"
                    call screen qte_combat("attack", 15, 4.0, "RLRLR")
                    if qte_success:
                        to"Lightning jutsu!? T-that hurt you asshole!"
                    else:
                        to"Bwa-ha-ha! Is that some sort of joke?"
                    
                    to"I'LL KILL YOU!" with vpunch
                    "Toji's enraged! His movements become erratic!"
                    call qte_combat_controller(win_label="toji_defeated", lose_label="lost_toji_fight") from _call_qte_combat_controller
                    if _return == "victory":
                        jump toji_defeated
                    elif _return == "defeat":
                        jump lost_toji_fight
                    label toji_defeated:
                    scene black with vpunch
                    to"Uh-arrh!" with vpunch
                    show dm_fight1 defeat0 with dissolve
                    to"Y-you... you BASTARD! H-how are you so s-strong!?" with vpunch
                    to"Fuck you and your w-whore [hin_rel_mother]!"
                    show dm_fight1 defeat0 at shakeforever
                    show powerup2 with dissolve
                    "Toji prepares a last-ditch effort!"
                    show boruto_defend_fight:
                        yalign 1.0
                    with dissolve
                    $ renpy.sound.play("/audio/soun_fx/punchbarrage.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    show boruto_defend_fight at shakeforever:
                        easein 8 yalign 0.1
                    show speedlines with dissolve
                    call screen qte_combat("defend", 150, 8.0, "spamclick")
                    if qte_success:
                        jump won_toji_fight
                    else:
                        jump lost_toji_fight
                    label won_toji_fight:
                    default toji_defeated = False
                    $ toji_defeated = True
                    show bg porchfight
                    show boruto_parry
                    with flash
                    "You successfully parried Toji's last ditch effort!"
                    scene dm_fight1 defeat0 with fade
                    to"W-what the!"
                    menu:
                        to"W-what the!"
                        "Finish him!":
                            default toji_killed_try = False
                            $ toji_killed_try = True
                            bo"You are wide open!"
                            $ renpy.sound.play("/audio/soun_fx/rasengan.opus", channel="sfx2", loop=False, relative_volume = 4.0)
                            with Shake((0, 0, 0, 0), 2, dist=15, peak_time=1.5, smoothness=50)
                            show boruto_rasengan 0 with flash:
                                ypos 120 xpos 100
                            
                            with Shake((0, 0, 0, 0), 2, dist=30, peak_time=1.5, smoothness=50)
                            $ renpy.sound.play("/audio/soun_fx/crate_break2.opus", channel="sfx3", loop=False, relative_volume = 1.5)
                            scene black with flash
                            $ renpy.sound.play("/audio/soun_fx/crate_break.opus", channel="sfx2", loop=False, relative_volume = 2.5)
                            with Shake((0, 0, 0, 0), 1, dist=20, peak_time=0.8, smoothness=50)
                            show dm_fight1 defeat1 with dissolve
                            "Your attack propelled Toji backwards, scarring his chest with a deep wound!"
                            to"*Wheezing*"
                            show dm_fight1 defeat1_1 with dissolve:
                                zoom 1.1
                            show dm_fight1:
                                easein 5 yalign 0.0
                            to"You b-bastard... *Wheezing*... you almost k-killed me!"
                            scene bg porch with dissolve
                            show shina surprised5 at left
                            show demandingmen badguys1:
                                xpos 570 yalign 1.0 xzoom -1.0 yzoom 1.12 zoom 1.21
                            show demandingmen:
                                easein 0.5 xpos 850
                            with dissolve
                            to "T-toji!" with vpunch
                            show demandingmen:
                                easeout 0.5 xpos 1300
                            "Koji rushed to his companion's care, leaving [hin_name] unattended..."
                            show blackscreen with dissolve
                            ko"You a-alright?"
                            show dm_fight1 defeat1_1 with dissolve:
                                zoom 1.1
                            hide blackscreen with dissolve
                            show dm_fight1:
                                easein 5 yalign 0.0
                            to"Just... *Wheezing*... H-help me make it back to the Daimyo's plot alive..."
                            show blackscreen with dissolve
                            "The two men limp their way back to where they came from after your superior display of strength."
                            hide blackscreen
                            hide dm_fight1
                            with dissolve
                            show shina concerned with dissolve:
                                easein 0.5 xalign 0.5
                            hin"[bo_name]! Are you hurt!?" with vpunch
                            bo"..."
                            show shina surprised5 with dissolve:
                                easein 0.5 xpos 1200
                            hin"[bo_name] answer me, please!" with vpunch
                            stop music fadeout 2
                            $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx3", loop=False, relative_volume = 1.6)

                            jump after_fightjump_kill
                        "Spare him...":
                            bo"Get the hell out of here before I get serious..."
                            to"*Tsk!* The Daimyo will have your head for t-this transgression!" with vpunch
                            bo"You let the Daimyo know this..."
                            bo"If he has a problem with us, he'll have to deal with me directly instead of sending his weak ass goons to threaten us!"
                            scene bg porch with dissolve
                            show shina surprised5 at left
                            show demandingmen badguys1:
                                xpos 570 yalign 1.0 xzoom -1.0 yzoom 1.12 zoom 1.21
                            show demandingmen:
                                easein 0.5 xpos 850
                            with dissolve
                            to "U-uuh... M-my lady, It's best I get going now!"
                            show demandingmen:
                                easeout 0.5 xpos 1300
                            to"Get a grip Toji! We have- *Ahem!* o-other matters to attend to!"
                            show blackscreen with dissolve
                            ko"..."
                            "The two men hesitantly take their leave after you put a stop to their aggression..."
                            hide blackscreen with dissolve
                            show shina concerned with dissolve:
                                easein 0.5 xalign 0.5
                            hin"[bo_name]! Are you hurt!?" with vpunch
                            bo"..."
                            show shina surprised5 with dissolve:
                                easein 0.5 xpos 1200
                            hin"[bo_name] answer me, please!" with vpunch
                            stop music fadeout 2
                            $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx3", loop=False, relative_volume = 1.6)
                            label after_fightjump_kill:
                            scene black with dissolve
                            show boruto_afterfight at dizzy with dissolve
                            $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx3", loop=False, relative_volume = 1.6)
                            $ renpy.sound.play("/audio/soun_fx/earringing.opus", channel="sfx2", loop=False, relative_volume = 0.05)
                            bo"F-fuck... That did a number on me..."
                            $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx3", loop=False, relative_volume = 1.6)
                            bo"M-my head, it h-hurts!" with flashred
                            $ renpy.sound.play("/audio/soun_fx/growl1.opus", channel="sfx3", loop=False, relative_volume = 0.9)   
                            $ renpy.sound.play("/audio/soun_fx/eye4s.opus", channel="sfx1", loop=False, relative_volume = 0.3)
                            $ renpy.sound.play("/audio/soun_fx/heartbeatlong.opus", channel="sfx2", loop=False, relative_volume = 1.2)
                            show kurama1 onlayer screens with flashred
                            show kurama1 onlayer screens:
                                easein 2 alpha 0.2
                            show kurama1 at fadeinandout
                            beast"*Growls...*"
                            "With adrenaline slowly wearing off, you felt the accumulated pain from Toji's barrage of attacks hitting you all at once, leaving you dazed."
                            beast"My power is not to be borrowed without a price!"
                            scene black with dissolve
                            beast"I shall keep you alive, for now..."
                            hin "{size=*0.5}[bo_name]...{/size}"
                            $ renpy.sound.play("/audio/soun_fx/growl2.opus", channel="sfx3", loop=False, relative_volume = 0.9)
                            show kurama1 onlayer screens:
                                easein 2 alpha 0.0
                            beast"In due time, you'll serve your purpose...*Low growl*"
                            scene black with flash
                            hin"[bo_name_stutter]!" with vpunch
                            show bg porchfight
                            show boruto_afterfight_t
                            with dissolve
                            show shina concerned:
                                xpos 1500
                            show shina:
                                easein 1 xpos 800
                            bo"[hin_rel_stutter]...?"
                            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                            show shina surprised with dissolve
                            hin"*Gasps*!" with vpunch
                            hin"That look in your eyes..."
                            hint"...It's just like the other time with Ino!"
                            bo"I don't... feel like... m-myself!"
                            show shina surprised5 with dissolve
                            hint"No... It can't be!"
                            "[hin_name] recounted the time she found you in a similar state with Ino. She knew there was not much time to act..."
                            show shina concerned with dissolve
                            hin"[bo_name]... My [hin_rel_to_bo]..."
                            show shina:
                                easein 1 xpos 300
                            pause 0.5
                            label replay_hinhj_afterfight:
                            $ initialize_replay_defaults()
                            scene black with dissolve
                            $ renpy.sound.play("/audio/soun_fx/intro/bodythud.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                            "*Body thud*!" with vpunch
                            
                            "Your legs gave out from beneath you. You blacked out momentarily from severe exhaustion."
                            show hin_afterfight with dissolve
                            hin"I got you!"
                            hin"You shouldn't have done that..."
                            hin"Putting yourself at risk for me... what were you thinking!"
                            call changeLove("Hinata",2) from _call_changeLove_51
                            hin"You i-idiot! *Sniffles* I should be the one protecting you..."
                            jump inside_hj_afterfight

                        
                "{color=[lovecolor]}Pay the money he is asking for{/color}":
                    label paymoney_r:
                    default toji_pay300 = False
                    $ playmusic("/audio/ost/house2.opus", 0.6)
                    scene black with dissolve
                    bo"I am not here to fight you, asshole..."
                    scene bg porch with dissolve
                    show demandingmen badguys1:
                        xpos 600
                    show shina surprised3 at left
                    show boruto angry at left behind shina:
                        xalign 0.3
                    with dissolve
                    bo"It's money you are after, isn't it?"
                    call checkMoney(300, "failtopaymoney") from _call_checkMoney_3
                    bo"Here it is. Now piss of and stop bothering us!"
                    if ch1_dy_200paid == False:
                        show demandingmen at smallshake
                        to"Oi... are you trying to be funny? Where's the rest of it!"
                        show boruto at smallshake
                        bo"What the hell are you talking about."
                        to"Last week's sum, you think we'd forget? Now pay up!"
                        call checkMoney(200, "failtopaymoney") from _call_checkMoney_4
                        to"That's more like it!"
                    $ toji_pay300 = True
                    to"Bit of a shame, really..."
                    show demandingmen:
                        easein 5 xpos 500
                    to"I was looking forward to some alone time with your-"
                    $ renpy.sound.play("/audio/soun_fx/slapecho.opus", channel="sfx2", loop=False, relative_volume = 1.5)
                    show dm_fight_intervene with flash
                    bo"Piss off, asshole! You already have what you asked for..." with vpunch
                    show dm_fight_intervene2 with dissolve
                    to"Oi, oi! You trying to act tough or something?"
                    show boruto_defend_fight with dissolve:
                        yalign 0.0
                    bo"You have a stick up your ass or something?"
                    $ renpy.sound.play("/audio/soun_fx/eye1.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                    show boruto_defend_fight_red with flashred:
                        yalign 0.0
                    bo"Get the hell out of here!" with vpunch
                    scene bg porchfight
                    show demandingmen badguys1
                    with dissolve
                    show demandingmen at smallshake
                    ko"T-toji! That's enough. The lady and the gentleman have adequately satisfied his highness' demands..."
                    to"*Tsk*" with vpunch               
                    "The more perceptive of the two men noticed that something was different. A sense of danger breezed through the air..."
                    ko"We thank you for your compliance!"
                    ko"We will of course be back next week to collect further payments. Fare well, my lady..."
                    hide demandingmen with dissolve
                    to"No fun..."
                    scene black with dissolve
                    show boruto_afterfight_red at dizzy with dissolve
                    $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx3", loop=False, relative_volume = 1.6)
                    $ renpy.sound.play("/audio/soun_fx/earringing.opus", channel="sfx2", loop=False, relative_volume = 0.05)
                    hin"...[bo_name_stutter]?"
                    bo"[hin_rel_stutter]? Ar-ah!" with vpunch
                    $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx3", loop=False, relative_volume = 1.6)
                    bo"All of a sudden... M-my head, it h-hurts!" with flashred
                    $ renpy.sound.play("/audio/soun_fx/growl1.opus", channel="sfx3", loop=False, relative_volume = 0.9)   
                    $ renpy.sound.play("/audio/soun_fx/eye4s.opus", channel="sfx1", loop=False, relative_volume = 0.3)
                    $ renpy.sound.play("/audio/soun_fx/heartbeatlong.opus", channel="sfx2", loop=False, relative_volume = 1.2)
                    show kurama1 onlayer screens with flashred
                    show kurama1 onlayer screens:
                        easein 2 alpha 0.2
                    show kurama1 at fadeinandout
                    beast"*Growls...*"
                    beast"My power is not to be borrowed without a price!"
                    scene black with dissolve
                    beast"I shall keep you alive, for now..."
                    hin "{size=*0.5}[bo_name]...{/size}"
                    $ renpy.sound.play("/audio/soun_fx/growl2.opus", channel="sfx3", loop=False, relative_volume = 0.9)
                    show kurama1 onlayer screens:
                        easein 2 alpha 0.0
                    beast"In due time, you'll serve your purpose...*Low growl*"
                    scene black with flash
                    hin"[bo_name_stutter]!" with vpunch
                    show bg porchfight
                    show boruto_afterfight_redt
                    with dissolve
                    show shina concerned:
                        xpos 1500
                    show shina:
                        easein 1 xpos 800
                    bo"I..."
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                    show shina surprised with dissolve
                    hin"*Gasps*!" with vpunch
                    hin"That look in your eyes..."
                    hint"...It's just like the other time with Ino!"
                    bo"I don't... feel like... m-myself!"
                    show shina surprised5 with dissolve
                    hint"No... It can't be!"
                    "[hin_name] recounted the time she found you in a similar state with Ino. She knew there was not much time to act..."
                    show shina concerned with dissolve
                    hin"[bo_name]... My [hin_rel_to_bo]..."
                    show shina:
                        easein 1 xpos 300
                    pause 0.5
                    scene black with dissolve
                    $ renpy.sound.play("/audio/soun_fx/intro/bodythud.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                    "*Body thud*!" with vpunch
                    
                    "Your legs gave out from beneath you. You blacked out momentarily..."
                    show hin_afterfight with dissolve
                    hin"I got you!"
                    hin"You shouldn't have done that..."
                    hin"Putting yourself at risk for me... what were you thinking!"
                    call changeLove("Hinata",2) from _call_changeLove_52
                    hin"You i-idiot! *Sniffles* I should be the one protecting you..." with vpunch
                    jump inside_hj_afterfight



        "(I am sure [hin_name] can take care of herself)":
            $ playmusic("/audio/ost/house2.opus", 0.6)
            hide love_choice with dissolve
            hin"What gives you the right..."
            show debtcollector_repeat1_1 with dissolve
            show debtcollector_repeat1_1:
                easein 4 yalign 0.0
            hin"...to put your hands on me!" with vpunch
            $ renpy.sound.play("/audio/soun_fx/slapecho.opus", channel="sfx2", loop=False, relative_volume = 1.5)
            scene bg porch
            show demandingmen badguys1:
                xpos 600
            show demandingmen at smallshake
            show shina angry at left
            "[hin_name] stands up for herself, sternly slamming the man's hand away!" with flash
            hin"The Hokage will hear of your misconduct." with vpunch
            to"Hah! Don't make me laugh woman..." with vpunch
            to"The Hokage won't be of much help if your financial obligations to the Daimyo are not met..."
            show shina shy with dissolve
            hin "Surely the Daimyo would understand. It'll be taken care off as soon as [na_name] is back!"
            to"In that case..."
            show demandingmen:
                easein 0.5 xpos 440
            to"The Daimyo would like to hear your plead personally!"
            menu:
                to"The Daimyo would like to hear your plead personally!"
                "...":
                    bot"It's not like I can do much..."
                    if borutoknockedoutlove == True or borutoknockedouthatred == True:
                        bot"Last time I got the shit beat out of me."
                        show shina surprised2 with dissolve
                        hin"The D-daimyo...?"
                        show demandingmen:
                            easein 0.5 xpos 100
                        pause 0.1
                        scene bg porchfight
                        show mp_v1_2
                        with dissolve
                        show mp_v1_3 with dissolve
                        ko"You are under arrest for insubordination!"
                        jump hinata_captured_repeat
                    jump hinata_captured_repeat
                
                "{color=[dominancecolor]}That's enough, shithead!{/color}":
                    bot"This fucking asshole is getting on my nerves..."
                    show boruto angry:
                        xpos -1000
                    show boruto angry:
                        easein 0.8 xpos 500
                    pause 0.4
                    $ renpy.music.play("audio/ost/borutotheme.opus", channel="music", loop=True, relative_volume = 0.6)
                    $ renpy.sound.play("/audio/soun_fx/slapecho.opus", channel="sfx2", loop=False, relative_volume = 1.5)
                    show dm_fight_intervene with flash
                    bo"That's enough, shithead!" with vpunch
                    to"Oi, oi..."
                    show hin_in_fight with easeinright
                    hin"[bo_name_stutter]!"
                    "You swoop in, slamming Toji's hand away, and placing yourself between him and [hin_name]!"
                    bo"To think he'd put his hands on you..."
                    bo"Stay back [hin_rel]! I'll deal with this asshole!"
                    show hin_in_fight at smallshake
                    hin"Be c-careful!"
                    hide hin_in_fight with dissolve
                    scene bg porch with dissolve
                    show shina surprised3 at left
                    show demandingmen badguys1:
                        xpos 570 yalign 1.0 xzoom -1.0 yzoom 1.12 zoom 1.21 
                    with dissolve
                    to "Trust me on this one, my lady, you don't want to intervene..."
                    to "Adding an injunction of violence on top of failing to pay your debts wouldn't be well received by the Daimyo."
                    to "Besides, my partner here may be a bit less... intellectually inclined, but even he knows that he can't just kill dumb kids."
                    to "He'll probably just teach the blonde twerp a lesson, I think..."
                    scene dm_fight_intervene2 with dissolve
                    to"I knew you were an idiot, but it seems like you've exceeded all expectations!"
                    to"You are a full-blown moron! Bwa-hah-hah!"
                    to"You sure you want to have your face beaten in!?" with vpunch
                    jump fight_toji_c

                "{color=[lovecolor]}Pay the money he is asking for{/color}":
                    show boruto angry:
                        xpos -1000
                    show boruto:
                        easein 0.4 xpos 250
                    show demandingmen:
                        easein 0.5 xpos 650
                    show shina surprised with dissolve
                    bo"That's enough!" with vpunch
                    to"Stay out of this kid, unless you'd like to have your ass beat!" with vpunch
                    jump paymoney_r
                
            

            

        


label failtopaymoney:
    default failtopaymoney = False
    $ failtopaymoney = True
    show boruto surprised2 with dissolve
    bot"S-shit! I don't have enough money to pay off our debts..."
    show boruto angry with dissolve
    bo"Well, we don't have your m-money, assholes!"
    ko"Ha! Tough luck, kid..."
    ko"But do not fret, for there are other ways the Daimyo will have you pay your debts..."
    bo"..."
    show demandingmen:
        linear 0.4 xalign 0.3
    show boruto:
        linear 0.3 xalign -2.0
    with vpunch
    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp4.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    show shina surprised4 at smallshake
    dm"The lady here, will have to pay in other ways!"
    scene black with vpunch
    bo"U-ugh!"
    "The men pushed you away and restrained [hin_name]!"
    scene bg porch
    show mp_v1_0introt
    with dissolve
    bo"What do you think you are doing you assholes!"
    dm"Under the Daimyo's command, failure to comply will result in imprisonment!"
    dm"You try anything stupid, and the Daimyo will have your heads on a spike for it..."
    show mp_v1_0introt 1 with dissolve
    hin"I'll be okay, [bo_name]..."
    hin"I am the Hokage's wife, am I not?"
    hin"They can't hurt me even if they tried!"
    hin"Please let [him_name] know that I'll be handling some chores outside the house if she returns before me..."
    show mp_v1_0introt with dissolve
    hin"Okay?"
    bo"..."
    show mp_v1_0introt:
        easeout 2 xpos 1500 alpha 0.0
    bo"Wait! You bastards!" with vpunch
    dm"Trust me when I say, kid..."
    $ renpy.sound.play("/audio/soun_fx/intro/evilmenlaugh.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    dm"You don't want to try following us, or else..."
    scene bg porch with dissolve
    show boruto angry with dissolve
    bot"Fuck!"
    jump hinata_captured_repeat



label lost_toji_fight:
    default lost_toji_fight = False
    $ lost_toji_fight = True
    $ toji_defeated = False
    scene black with vpunch
    stop sfx2 fadeout 1
    to"BWA-HAHAHA!"
    scene dm_fight1 defeat0 with flash
    to"That actually hurt, you bastard!"
    show dm_fight defeat with dissolve
    hin"[bo_name]!!" with vpunch
    "Toji's barrage left you unconscious. [hin_name] worried about your well-being, started running towards you, but..."
    scene black with vpunch
    ko"Not so fast, my lady..."
    show bg porchfight
    show mp_v1_2
    with dissolve
    show mp_v1_3 with dissolve
    hin"B-bastards! You won't get away with this!" with vpunch
    hide mp_v1_2
    hide mp_v1_3
    show mp_v1_spank 0
    with Dissolve(0.3)
    # show mp_v1_spank 2 with Dissolve(0.3)
    show mp_v1_spank 3 with Dissolve(0.3)
    $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
    show mp_v1_spank 4 with Dissolve(0.3)
    to"Shut up, bitch!" with vpunch
    jump hinata_captured_repeat

label hinata_captured_repeat:
    default hinata_captured = False
    $ hinata_captured = True
    "[hin_name] was detained for failing to meet her obligations to the Daimyo."
    $ playmusic("audio/ost/Senya.opus",0.5)
    scene black with dissolve
    if toji_defeated == True or toji_pay300:
        jump jumphere_if_toji_defeated
    scene bg konoha1
    show demandingmen normal badguys2
    show shina restrained:
        zoom 1.01 
    with fade
    to"Keep walking, woman!"
    ko"Take it easy, Toji. A modicum of respect is the least you can offer for the lady..."
    to"HAH!" with vpunch
    to"What respect is she showing to his highness, huh!?" with vpunch
    scene bg konoha1
    show mp_v1_3:
        xpos 0.30
    with dissolve
    hide mp_v1_3
    show mp_v1_grab:
        xpos 0.30
    with dissolve
    $ renpy.sound.play("/audio/soun_fx/grope2.opus", channel="sfx3", loop=False, relative_volume = 1.0)
    to"Ignoring the Daimyo's stature, not paying what is due..."
    hin"D-don't touch me!" with vpunch
    show mp_v1_grab 2 with dissolve
    $ renpy.sound.play("/audio/soun_fx/spank6.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp2.opus", channel="sfx3", loop=False, relative_volume = 1.0)
    to"That's not very respectful now, is it!?" with vpunch
    hin"I promise... you'll pay for this!"
    scene black with dissolve
    to"BWA-HAHAHA!" with vpunch
    scene palace
    show demandingmen normal badguys2:
        xpos 600
    show shina restrained:
        xpos 10 zoom 1.01
    with fade
    ko"Enough games! Toji..." with vpunch
    to"We'll see how much respect you'll have left after spending a few nights in his highness' dungeons!"
    hin"..."
    hide demandingmen
    hide shina
    with dissolve
    label jumphere_if_toji_defeated:
    show palace with dissolve:
        zoom 1.2 xalign 0.5 yalign 0.5
    if toji_defeated == True:
        ko"OPEN THE GATES!" with vpunch
    else:
        to"OPEN THE GATES!" with vpunch
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/gateopening.opus", channel="sfx3", loop=False, relative_volume = 0.5)
    "..."
    $ playmusic("audio/ost/Senya.opus",0.5)
    "Meanwhile..."
    scene bg porch with dissolve
    show boruto worried at center with dissolve
    $ playmusic("audio/ost/house2.opus",0.6)
    if failtopaymoney == True:
        bot"Fuck! Those bastards took [hin_rel] away..."

    elif lost_toji_fight == True:
        show boruto angry with dissolve
        bot"I can't believe I got my ass beat by that bastard!"
        show boruto worried with dissolve
        bot"And it seems they took [hin_rel] away too..."

    else:
        pass

    show boruto angry with dissolve
    bot"This Daimyo and his goons are way out of line!"
    bot"I'll look into getting in the Daimyo's place. There must be something I can do!"
    scene black with dissolve
    default daimyo_unlocked = False
    if daimyo_unlocked == False:
        $ daimyo_unlocked = True
        if quest.exists("job2_2"):
            if failtopaymoney == True or lost_toji_fight == True:
                $ quest.check("job2_2", "done")
            else:
                $ quest.check("job2_2", "completed")
            $ quest.check("job2_3", "in progress")
            $ notification("Quest updated")
        "You can now visit the Daimyo's plot."


    jump action_taken

















label inside_hj_afterfight:
    scene black with dissolve
    if daimyo_unlocked == False:
        $ daimyo_unlocked = True
        if quest.exists("job2_2"):
            $ quest.check("job2_2", "completed")
            $ quest.check("job2_3", "in progress")
            $ notification("Quest updated")
        "You can now visit the Daimyo's plot."
    
    "..."
    scene hin_afterfight1 with dissolve:
        yalign 1.0
    show hin_afterfight1:
        easein 4 yalign 0.0
    "[hin_name] picked you up, and carried your unconscious body inside.\nHer fingertips were warm with a lingering burning sensation, emanating from your body."
    hin "This... thing inside you. Its tearing you apart, eating you alive..."
    hin"And yet all I've done is stand by, watching you suffer. What kind of [hin_rel_mother] would do that..."
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 0.7)
    hin"My sweet, brave boy..."
    scene v20hin_handy 0 with dissolve:
        yalign 1.0
    show v20hin_handy 0:
        easein 3 yalign 0.1
    hin"You've fought so fiercely for me..."
    hin "Pushed through that cursed pain until it shattered you."
    hin"I should have never let it come to this. S-stupid me! Argh!" with vpunch
    
    hin "Now it's my turn to take care of you..."
    show v20hin_handy with dissolve:
        zoom 1.1 yalign 1.0 xalign 0.0
    show v20hin_handy 0_1 with dissolve
    $ renpy.sound.play("/audio/soun_fx/clothes_undress.opus", channel="sfx3", loop=False, relative_volume = 1)
    hin"Let's take these shoes off first..."
    scene v20hin_handy 0_1 with dissolve:
        yalign 1.0
    show v20hin_handy 0_1:
        easein 3 yalign 0.2
    hin"..."
    hint"His... his p-penis..."
    hin "That desperate look in your eyes before you collapsed... I've seen it before."
    hin "I know what this curse does to you. How it twists you into something... feral."
    show v20hin_handy 0_2 with dissolve
    bo"Hnn... Aaarh! *Groans of 'pain)'..." with vpunch
    hin"[bo_name]!" with vpunch
    hint "It's come to this... hasn't it?"
    hin "I can't let you become that monster again. Not if I can stop it."
    scene black with dissolve
    stop music fadeout 1
    hin"So if this is what it takes..."
    $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 0.7)
    "She tugs your pants down, her hands shaking..."
    show dreamvignette zorder 100 with dissolve
    play music"/audio/ost/dreaming.opus" volume 0.5
    $ renpy.sound.play("/audio/soun_fx/wind4.opus", channel="sfx3", loop=False, relative_volume = 1.2)
    show v20hin_hanaba 1 at brightreveal, custom_vpunch_repeat with flash:
        yalign 1.0
    $ renpy.sound.play("/audio/soun_fx/various_sex/bedsex_young.opus",loop=False, channel="sfx2", relative_volume = 0.5, fadein=2)
    hint"This is the least I can do for you. At least while you are still unconscious..."
    bot"Hehe..."
    bot"Hehehh...eheh!"
    "Unknown girl" "  Aaah-ahrrh!♡ Y-yes-yes-yes, [bo_name_stutter]! F-faster!  Aah-ah-arrh!♡!"
    bot"Wet dreams are the best!"
    call showscrollingimage from _call_showscrollingimage_247
    show screen parallax1280("v20hin_handy 1_1",1,1.0) with dissolve
    bot"And this one almost feels... r-real!"
    hint"*Gulp*..."
    hint"I expected as much of course. But seeing my own [hin_rel_to_bo]'s p-penis like this, pulsing in my palm..."
    hint"It feels wrong in so many ways! Yet I know for a fact..."
    hint"This is how his curse affects him, and this is how I can s-stop it!"
    hide screen parallax1280
    show screen parallax1280("v20hin_handy 1_1",1,0.0)
    with dissolve
    hint"Even while unconscious it seems like he is in a world of hurt."
    hint"[bo_name_stutter]... I won't let this pain last long, I promise!"
    scene black
    call hidescrollingimage from _call_hidescrollingimage_214
    $ renpy.sound.play("/audio/soun_fx/various_sex/bedsex_young.opus",loop=True, channel="sfx2", relative_volume = 0.7)
    # show screen parallax1280("v20_daimyoend_0test2_1",1,0.6,transformeffect=custom_vpunch_repeat(timer=1.8)) with dissolve
    $ renpy.sound.play("/audio/soun_fx/wind3.opus", channel="sfx3", loop=False, relative_volume = 0.8)
    show v20hin_hanaba 1 with longerflash:
        yalign 1.0 subpixel True
    show v20hin_hanaba 1 at custom_vpunch_repeat:
        easein 6 yalign 0.0
    
    bot"Ehehe-ehheh!"
    bot"A wet dream with Auntie Hanabi is s-something else. I am beyond perverted!" with vpunch
    "Hanabi" "Aaah-ahrrh!♡ Y-you can go... d-deeper than that! Aaah-ahrrh!♡"
    call showscrollingimage from _call_showscrollingimage_248
    show screen parallax1280("v20hin_hanaba 1",1,1.0,transformeffect=custom_vpunch_repeat) with dissolve
    bot"But who can blame me! Auntie Hanabi is the best!"
    bot"We used to spend so much time together... So much so that her perfect body is now forever carved into my mind..."
    bot"Fuck, she is hot! M-maybe as hot as [hin_rel] even..."
    stop sfx2 fadeout 2
    $ renpy.sound.play("/audio/soun_fx/wind3.opus", channel="sfx3", loop=False, relative_volume = 0.8)
    show screen parallax1280("v20hin_handy 2_1",1,1.0) with flash
    bot"Guess it runs in my [hin_rel_mother]'s bloodline..."
    hint"Come on, [hin_name] get through this first few strokes..."
    hint"It's just a medical procedure, nothing more..."
    hide screen parallax1280
    show screen parallax1280("v20hin_handy 2",1,1.0)
    with dissolve
    hint"I am just... h-helping my [hin_rel_to_bo], easing his pain..."
    hide screen parallax1280
    show screen parallax1280("v20hin_handy 2_1",1,1.0)
    with dissolve
    hint"A little relief is all he needs..." with vpunch
    hide screen parallax1280
    show screen parallax1280("v20hin_handy 2",1,1.0)
    with dissolve
    hint"And this much I cannot deny him. Not after everything he's been going through..." with vpunch
    $ renpy.sound.play("/audio/soun_fx/handjob4.opus", channel="sfx3", loop=True, relative_volume = 0.5)
    show screen parallax1280("v020_hina_handjob1",1,1.0,transformeffect=custom_vpunch_repeat(timer=1.3)) with dissolve
    hint"Besides..."
    hint"If I move faster, I should be able to get this done before he wakes up..."
    hint"There's no harm in h-helping, if no one knows I provide relief to my own [hin_rel_to_bo]."
    hint"Let alone you, [bo_name]..."
    scene black
    call hidescrollingimage from _call_hidescrollingimage_215
    $ renpy.sound.play("/audio/soun_fx/wind4.opus", channel="sfx3", loop=False, relative_volume = 1.2)
    show v20hin_hanaba 1_1 at brightreveal, custom_vpunch_repeat with flash:
        yalign 1.0
    $ renpy.sound.play("/audio/soun_fx/various_sex/bedsex_young.opus",loop=False, channel="sfx2", relative_volume = 0.5, fadein=2)
    show v20hin_hanaba:
        easein 5 yalign 0.0
    "Hanabi" "M-my nephew... Aaah-ahrrh!♡ My nephew is stretching my p-pussy! *moans* Aaah-ahrrh!♡" with flash
    "Hanabi" "F-fuck me [bo_name] Aaah-ahrarh!♡!"
    call showscrollingimage from _call_showscrollingimage_249
    show screen parallax1280("v20hin_hanaba 1_1",1,1.0,transformeffect=custom_vpunch_repeat) with dissolve
    "Hanabi" "G-grab m-me... Aaah-ahrarh!♡! F-fuck me harder!" with vpunch
    hide screen parallax1280
    show screen parallax1280("v20hin_hanaba 1_1a",1,0.4,transformeffect=custom_vpunch_repeat)
    with dissolve
    bot"F-fuck yeah I will!" with vpunch
    show screen parallax1280("v20hin_handy 2",1,1.0) with flash
    $ renpy.sound.play("/audio/soun_fx/wind2.opus", channel="sfx3", loop=False, relative_volume = 1.2)
    "Hanabi" "S-squeeze them harder-Aaaaaaaarhaaah!♡!♡!"
    stop sfx3 fadeout 1
    show screen parallax1280("v20hin_handy 2",1,1.0) with dissolve
    $ renpy.sound.play("/audio/soun_fx/handjob4.opus", channel="sfx3", loop=True, relative_volume = 0.5)
    show screen parallax1280("v20hin_handy 2",1,1.0) with dissolve
    hint"This isn't going a-anywhere, not to mention my back aches from being hunched for so long..."
    hin"Let's... let's get us comfortable, shall we?"
    show screen parallax1280("v20hin_handy 3_1",1,1.0) with dissolve
    hint"R-right... This ought to be easier on both of us."
    hide screen parallax1280
    show screen parallax1280("v020_hina_handjob2",1,1.0)
    with dissolve
    bo"Ah-ah! *Groans*..." with vpunch
    hint"He is in a world of hurt! Because of me..."
    hide screen parallax1280
    show screen parallax1280("v20hin_hanaba 1_1a",1,1.0)
    with dissolve
    bot"Don't mind if I s-squeeze them tiddies harder, Auntie!"
    show screen parallax1280("v020_hina_handjob2",1,1.0) with dissolve
    hint"His h-hands... are they twitching? Is the p-pain that unbearable?"
    hint"I'll take care of it, [bo_name]! Hang in there, please..."
    bot"Tiddies are the best!"
    bot"This dream is unreal! It feels like I am about to cum in two parallel universes!"
    bo"Heavy breathing*... A-ah.... Eh!" with flash
    hin"My sweet boy... We a-are almost there, I can tell..."
    bot"I wonder if Auntie Hanabi could be as much of a nympho as she appears to be in my fantasies..."
    bot"Eheh-he-heh!" with vpunch
    stop sfx3 fadeout 1
    hide screen parallax1280
    show screen parallax1280("v20hin_handy 3_2",1,1.0)
    with dissolve
    hint"I should be extra careful during these final s-strokes..."
    hint"Wouldn't want to make a mess, or leave any evidence for him to find out..."
    $ renpy.sound.play("/audio/soun_fx/various_sex/bedsex_young.opus",loop=True, channel="sfx2", relative_volume = 0.7)
    # show screen parallax1280("v20_daimyoend_0test2_1",1,0.6,transformeffect=custom_vpunch_repeat(timer=1.8)) with dissolve
    $ renpy.sound.play("/audio/soun_fx/wind3.opus", channel="sfx3", loop=False, relative_volume = 0.8)
    show screen parallax1280("blackscreen",1,1.0) with flash
    bot"Can I cum inside... A-auntie?"
    $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.4)
    show screen parallax1280("v20hin_hanaba 1_2",1,0.5) with longerflash
    "Hanabi" "F-fill me up... Aaah-ahrarh!♡! Fill me uuup-Aaaraaaah!♡!!♡!!♡! *orgasmic moans*"
    show screen parallax1280("blackscreen",1,1.0) with dissolve
    hin"There, there..."
    hide screen parallax1280
    show screen parallax1280("v20hin_handy nurse0",1,1.0)
    with dissolve
    hint"Like an infant baby, being nursed by his [hin_rel_mother]..."
    hint"I could m-maybe get used to this..."
    hide screen parallax1280
    show screen parallax1280("v20hin_handy nurse1_0",1,1.0)
    with dissolve
    hint"...If it weren't for t-this, of course. Nothing 'baby' about that!"
    hint"It's been almost half an hour now..."
    hint"His breathing has stabilized. It seems whatever was agitating him is slowly being neutralized..."
    hint"But his p-penis..."
    show screen parallax1280("v20hin_handy nurse1",1,1.0) with dissolve
    hint"It shows no signs of retreating yet..."
    show screen parallax1280("v020_hina_handjob3",1,1.0) with dissolve
    $ renpy.sound.play("/audio/soun_fx/handjob4.opus", channel="sfx3", loop=True, relative_volume = 0.5)
    hint"I can't give up now!"
    scene black
    call hidescrollingimage from _call_hidescrollingimage_216
    hint"If what Lady Tsunade said is right..."
    call showscrollingimage from _call_showscrollingimage_250
    show screen parallax1280("v020_hina_handjob4",1,1.0,transformeffect=custom_vpunch_repeat(timer=2)) with dissolve
    hint"Him waking up in this state could be d-dangerous..."
    hint"There's no more time to waste!" with dissolve
    hint"I have to get serious!"
    show screen parallax1280("v020_hina_handjob4fast",1,1.0,transformeffect=custom_vpunch_repeat(timer=1)) with dissolve
    $ renpy.sound.play("/audio/soun_fx/handjob5.opus", channel="sfx3", loop=True, relative_volume = 0.5)
    hin"Come on... come on!" with vpunch
    hint"His t-thing is so rigidly pointing upwards, I am a-afraid of hurting him further!"
    hint"All that blood circulating t-there for so long cannot be healthy..."
    hint"Though it feels like with every s-stroke it gets warmer and warmer, he m-must be close!"
    stop sfx3 fadeout 2
    show screen parallax1280("v20hin_handy 4_2",1,1.0) with dissolve
    bo"Mhmm.. Ar-ah! *groans*"
    hin"O-oh!" with vpunch
    hint"W-wrapping his legs around mine... t-this must be a signal!"
    show screen parallax1280("v20hin_handy end",1,1.0) with dissolve
    bo"Ah-h... *moans*" with flash
    hint"I am s-sorry [bo_name]! It'll be easier to clean up if you don't s-stain your bed... or me..."
    $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.4)
    show screen parallax1280("v20hin_handy end1",1,0.5) with longerflash
    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx2", loop=False, relative_volume = 0.7)
    hin"*Gasp*!"
    scene black 
    call hidescrollingimage from _call_hidescrollingimage_217
    show v20hin_handy end1_1 with dissolve:
        yalign 1.0
    show v20hin_handy end1_1:
        easein 5 yalign 0.1
    hin"G-good heavens!" with vpunch
    show v20hin_handy end1_2 with dissolve
    hin"W-what the heck was that!"
    call changeObedience("Hinata",1) from _call_changeObedience_142
    scene black with dissolve
    hin"Not even [na_name]'s t-thing ever got anywhere n-near my face!"
    "[hin_name] quickly wipes her face clean of your juices..."
    show v20hin_handy 0 with dissolve:
        yalign 0.0
    "She then meticulously wipes you clean to avoid raising any suspicion."
    show v20hin_handy 0 with dissolve:
        zoom 1.2 yalign 0.0 xalign 0.8
    bo"*snorts*" with vpunch
    scene black with dissolve
    bo"Mi-mi-mi-mi-mi...."
    $ daimyo_unlocked = True
    jump action_taken


label daimyo_debt_collect_repeat:
    scene bg porch with dissolve
    show shina concerned at left
    if toji_pay300 == True:
        show demandingmen badguys1:
            xpos 570 yalign 1.0 yzoom 1.12 zoom 0.93
        with dissolve
        show demandingmen at smallshake
        to "You know why we are here, don't you!" with vpunch
        show shina shy2 with dissolve
        hin"..."
    else: 
        show demandingmen badguys1:
            xpos 570 yalign 1.0 xzoom -1.0 yzoom 1.12 zoom 1.21
        with dissolve
        ko "You know why we are here, don't you my Lady..."
        show shina shy2 with dissolve
        hin"Debt collecting, again..."
    default daimyo_collect_firsttimedebt = False
    if daimyo_collect_firsttimedebt == False:
        "???" "Allow me to have a word with the Lady..."
        $ daimyo_collect_firsttimedebt = True
        show demandingmen:
            easein 1 xpos 1300
        ko"H-hai!" with vpunch
        show daimyo normal at right
        show shina surprised3
        with dissolve
        da"Greetings, my Lady..." with dissolve
        hin"Y-you... W-what do you need from us?"
        da"Only that which I am owed."
        show boruto angry:
            xpos -1000
        show boruto:
            easein 0.5 xpos 200
        show shina concerned:
            easein 0.6 xpos -50
        bo"You aren't owed shit! Stay back [hin_rel]..."
        show daimyo pervert with dissolve
        da"There's the man of the hour! Bwaa-ha-haaa!" with vpunch
        show daimyo normal with dissolve
        if toji_pay300 == True:
            da"So you are the one who sent my men back to me with their tails wagged between their legs."
            da"Koji mentioned that something felt off..."
            show daimyo pervert with dissolve
            da"But all I see here is a pretty lady and a snot-faced boy!"
            show daimyo normal with dissolve
            da"Still, commendable of you to take up responsibility in absence of the Hokage."
            bo"What do you want from us!"
            da"What I want from you is simple..."
            da"Compliance!" with vpunch
            da"Heed my one last and final warning, lest you find yourselves rotting in my dungeons, or better yet dead!"
            da"Hurling insults or threatening my men with violence for simply doing their job is grounds for punishment!" with vpunch
            da"You shall not disobey my rule, or my men again."
            da"Failure to comply with my policy, or violence against my men will befall catastrophic consequences upon you."
        else:
            da"So you are the one who sent Toji back to me with his tail wagged between his legs."
            da"The man has suffered serious injuries because of your mindless aggression..."
            bo"M-mindless? He put his hands on my [hin_rel] first!"
            if toji_killed_try == True:
                da"You almost damn near killed him, kid..."
            else:
                da"Can you blame him? Hee-hee!"
            show daimyo pervert with dissolve
            da"In any case, stupid... but impressive nonetheless, what you did!" with vpunch
            show daimyo normal with dissolve
            da"Yet equally disrespectful to your ruler!" with vpunch
            da"Heed my one last and final warning, lest you find yourselves rotting in my dungeons, or better yet dead!"
            da"You shall not disobey my rule again."
            da"Failure to comply with my policy, or further violence against my men will befall catastrophic consequences upon you."
        show daimyo at smallshake
        da"Have I made myself clear?" with vpunch
        bo"Tsk!" with vpunch
        show shina shy2 with dissolve
        hin"Y-yes, your highness. Please accept both of our apologies!"
        da"And you, boy?"
        bot"This is not the time to act out... yet!"
        bo"Uuh, sure. My apologies..."
        show daimyo pervert with dissolve
        da"Splendid!" with vpunch
        da"Given your prominence in our Nation's affairs, and considering the lengthy absence of this household's main breadwinner..."
        da"I as your benevolent ruler, have ordered a significant reduction in your owed amount."
        da"I hope you'll show at least half as much compassion as I have shown here today to you!"
        hide daimyo with dissolve
        if toji_pay300 == True:
            da"That'll be all! Toji, proceed..."
        else:
            da"That'll be all! Koji, proceed..."
        default reduced_debts = False
        $ reduced_debts = True
        if toji_pay300 == True:
            show demandingmen badguys1:
                xpos 570 yalign 1.0 yzoom 1.12 zoom 0.93
            with dissolve
            to"H-hai!" with vpunch
            to"Hehe! Now pay up!" with vpunch
        else: 
            show demandingmen badguys1:
                xpos 570 yalign 1.0 xzoom -1.0 yzoom 1.12 zoom 1.21
            with dissolve
            ko"H-hai!" with vpunch
            ko"Don't try anything s-stupid kid. You've heard what the Daimyo had to say..."
        menu paydebt1_repeatmenu2:
            ko"Don't try anything s-stupid kid. You've heard what the Daimyo had to say..."
            "{color=[lovecolor]}Pay your household's debts({color=#85bb65}-$20{/color})": #todo change to 100 in the future
                call checkMoney(20, "paydebt1_repeatmenu2") from _call_checkMoney_5
                bo"Here, now piss off!" with vpunch
                ko"Right. We appreciate your cooperation!"
                hide demandingmen with dissolve
                show boruto normal at right with dissolve
                bo"There, all taken care off!"
                scene black with dissolve
                call changeLove("Hinata",1) from _call_changeLove_53
                hin"Thank you, [bo_name]!"
                call changeObedience("Hinata",1) from _call_changeObedience_143
                hin"What would I ever do without you..."
                $ daimyo_unlocked = True

                #v21 ramen obedience entry
                if (chosen_hate_path or chosen_love_path) and high_score>4200 and v21ramenintro_progression == 0:
                    $ v21ramenintro_progression = 1
                    jump v21_ramenintro_talk
                jump action_taken

            "{color=[hatredcolor]}Pay your household's debts({color=#85bb65}-$20{/color})" if chosen_hate_path: #todo change to 100 in the future
                call checkMoney(20, "paydebt1_repeatmenu2") from _call_checkMoney_9 
                bot"Fuck! Guess I have to take care of this if I want to convince [hin_rel] to do lewd stuff for me... Hehe!"
                bo"Here, now piss off!" with vpunch
                ko"R-right. We appreciate your cooperation!"
                hide demandingmen with dissolve
                show boruto snob at right with dissolve
                bo"Pieces of shit..."
                scene black with dissolve
                call changeLove("Hinata",1) from _call_changeLove_78 
                hin"H-hey!{p}N-nevermind... Thank you, [bo_name]!"
                bo"Yeah well, I can't keep doing this forever, you know...{p}I'm going to need you to start helping soon..."
                call changeObedience("Hinata",1) from _call_changeObedience_181
                hin"R-right... I'll think of something, I promise!"
                
                $ daimyo_unlocked = True
                #v21 ramen obedience entry
                if (chosen_hate_path or chosen_love_path) and high_score>4200 and v21ramenintro_progression == 0:
                    $ v21ramenintro_progression = 1
                    bot"In fact, I might just have a plan in mind for you [hin_rel]!"
                    bot"I wonder if this will work..."
                    jump v21_ramenintro_talk
                jump action_taken
                
            "I can't pay right now":
                show boruto worried with dissolve
                show shina concerned with dissolve
                bo"I can't pay you right now. Can't we push back the date or something?"
                scene black with dissolve
                ko"I am afraid that's not how it works..."
                hin"N-no! Not again!" with vpunch
                jump hinata_captured_repeat

    else:
        show boruto angry:
            xpos -1000
        show boruto:
            easein 0.5 xpos 200
        show shina concerned:
            easein 0.6 xpos -50
        bo"I'll handle this."
        ko"Don't try anything s-stupid kid. You've heard what the Daimyo had to say..."
        menu paydebt1_repeatmenu:
            ko"Don't try anything s-stupid kid. You've heard what the Daimyo had to say..."
            "{color=[lovecolor]}Pay your household's debts({color=#85bb65}-$200{/color})" if reduced_debts == False:
                call checkMoney(200, "paydebt1_repeatmenu") from _call_checkMoney_6
                bo"Here, now piss off!" with vpunch
                ko"R-right. We appreciate your cooperation!"
                hide demandingmen with dissolve
                show boruto normal at right with dissolve
                bo"There, all taken care off!"
                scene black with dissolve
                call changeLove("Hinata",1) from _call_changeLove_54
                hin"Thank you, [bo_name]!"
                call changeObedience("Hinata",1) from _call_changeObedience_144
                hin"What would I ever do without you..."
                $ daimyo_unlocked = True

                #v21 ramen obedience entry
                if (chosen_hate_path or chosen_love_path) and high_score>4200 and v21ramenintro_progression == 0:
                    $ v21ramenintro_progression = 1
                    jump v21_ramenintro_talk
                jump action_taken

            "{color=[lovecolor]}Pay your household's debts({color=#85bb65}-$20{/color})" if reduced_debts == True: #todo change to 100 in the future
                call checkMoney(20, "paydebt1_repeatmenu") from _call_checkMoney_7
                bo"Here, now piss off!" with vpunch
                ko"R-right. We appreciate your cooperation!"
                hide demandingmen with dissolve
                show boruto normal at right with dissolve
                bo"There, all taken care off!"
                scene black with dissolve
                call changeLove("Hinata",1) from _call_changeLove_55
                hin"Thank you, [bo_name]!"
                call changeObedience("Hinata",1) from _call_changeObedience_145
                hin"What would I ever do without you..."
                $ daimyo_unlocked = True

                #v21 ramen obedience entry
                if (chosen_hate_path or chosen_love_path) and high_score>4200 and v21ramenintro_progression == 0:
                    $ v21ramenintro_progression = 1
                    jump v21_ramenintro_talk
                jump action_taken

            "{color=[hatredcolor]}Pay your household's debts({color=#85bb65}-$20{/color})" if reduced_debts and chosen_hate_path: #todo change to 100 in the future
                call checkMoney(20, "paydebt1_repeatmenu") from _call_checkMoney_8
                bot"Fuck! Guess I have to take care of this if I want to convince [hin_rel] to do lewd stuff for me... Hehe!"
                bo"Here, now piss off!" with vpunch
                ko"R-right. We appreciate your cooperation!"
                hide demandingmen with dissolve
                show boruto snob at right with dissolve
                bo"Pieces of shit..."
                scene black with dissolve
                call changeLove("Hinata",1) from _call_changeLove_56
                hin"H-hey!{p}N-nevermind... Thank you, [bo_name]!"
                bo"Yeah well, I can't keep doing this forever, you know...{p}I'm going to need you to start helping soon..."
                call changeObedience("Hinata",1) from _call_changeObedience_146
                hin"R-right... I'll think of something, I promise!"
                
                $ daimyo_unlocked = True
                #v21 ramen obedience entry
                if (chosen_hate_path or chosen_love_path) and high_score>4200 and v21ramenintro_progression == 0:
                    $ v21ramenintro_progression = 1
                    bot"In fact, I might just have a plan in mind for you [hin_rel]!"
                    bot"I wonder if this will work..."
                    jump v21_ramenintro_talk
                jump action_taken

            "I can't pay right now":
                show boruto worried with dissolve
                bo"I can't pay you right now. Can't we push back the date or something?"
                scene black with dissolve
                ko"I am afraid that's not how it works..."
                hin"N-no! Not again!" with vpunch
                jump hinata_captured_repeat
    
    

