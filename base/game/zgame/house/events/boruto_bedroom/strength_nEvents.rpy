default hima_wrestling_won = False

label start_strength_minigame:
    $ renpy.sound.play("/audio/soun_fx/countdown.opus", channel="sfx2", loop=False, relative_volume = 0.9)
    show pushup_down
    show halfblack
    with dissolve
    show screen scrollingtext("Get ready to tap as fast as you can!")
    hide halfblack with Dissolve(3)
    $ result = renpy.call_screen("strength_minigame")
    $ pushups = result[0]
    $ ended_by_stamina = result[1]
    
    if ended_by_stamina:
        "You got exhausted after completing [pushups] pushups!"
    else:
        "You completed [pushups] pushups!"
    show bedroom_gymend with dissolve
    call changeStrength(pushups) from _call_changeStrength
    bo"I somehow already feel a little bit stronger...!"
    default opportunity_tofail = "" #unused (prolly)
    default opportunity_sakurasarada_introduction = False


    if opportunity_sakurasarada_introduction == False and strength >= 1 and hin_location != "captured":
        if is_opportunity_unlocked("l1_opportunity1", strength):
            jump saradasakuraintroduction
        else:
            pass

    if ((day_name == "Saturday" or day_name == "Sunday") or (day_part == 2)):
        if is_opportunity_unlocked("l0_opportunity1", strength):
            pass
            if l0_opportunity1_win_defeated == True:
                scene black with dissolve
                "Meanwhile..."
                $ change_music_volume(0.3, 1.0)
                scene bg day with dissolve:
                    zoom 0.70
                show hima mad with dissolve:
                    zoom 0.4 xalign 0.5
                him"This freaking idiot! How many times do I have to tell him..."
                show hima:
                    easein 1 xpos -500
                pause 0.5
                scene black with dissolve
                $ change_music_volume(0.7, 1.0)
                show bg bb day with dissolve:
                    blur 10
                show hima mad3:
                    zoom 0.4 xalign 2.0
                show hima:
                    easein 0.5 xalign 0.5
                him"Hey asshole!" with vpunch
                show hima at smallshake
                himt"He can't even hear me through his stupid music! Argh!" with vpunch
                show pushup_anim with dissolve
                himt"Since when is this stupid idiot taking training seriously anyway..."
                himt"I can't believe he brushed me off as easily as he did last time..."
                himt"Am I really this weak? Or was he always stronger than me..."
                scene black with dissolve
                scene bedroom_gymend with dissolve:
                    zoom 1.05
                "You finish your set and notice [him_name] standing behind you looking frustrated..."
                
                scene bg bb day:
                    blur 10
                show hima mad3 with dissolve:
                    zoom 0.4 xalign 0.5
                him"H-hey assho- "
                show hima worried2 with dissolve
                him"I m-mean, [bo_name]..."
                him"Can you p-please turn your music down?"
                scene bedroom_gymend with dissolve:
                    zoom 1.05
                bo"Found your manners after getting your ass beat last time, did you? Heh!"
                him"Grr! *Annoyed groans*"


                menu l0_opportunity2_repeatable:
                    bo"Found your manners after getting your ass beat last time, did you? Heh!"
                    "{color=[hatredcolor]}Piss her off! (Turn it up){/color}":
                        bo"Let me think about that for a second..."
                        $ change_music_volume(2.0, 1.0)
                        call changeHatred(1) from _call_changeHatred_100
                        bo"Yep. That sounds better to me, now piss off! Bitch..."
                        
                        
                    "{color=[dominancecolor]}Taunt her!{/color}":
                        scene bedroom_gymend with dissolve:
                            zoom 1.05 yalign 1.0
                        bo"Why don't you try doing that yourself!"
                        show hima worried2:
                            xpos 1200 zoom 0.34
                        show hima:
                            easein 0.5 xpos 700
                        him"Mmmmmhh! Can we n-not do this again!?"
                        bo"This is my domain [him_name]! If you want me to meet your demands, you are gonna have to convince me first!"
                        show hima mad with dissolve
                        him"You are a real a-asshole! You know that?"
                        show hima:
                            easein 0.5 xpos 70
                        pause 0.4
                        scene black
                        him"I'll beat you to a pulp this time!" with vpunch
                        show bg bb day:
                            blur 10
                        show int1_tr at smallshake
                        bo"Quick to take the bait, aren't you? You little brat!" with vpunch
                        show int1_tr at smallshake
                        him"You... *Grrr*!"
                        bo"You never learn, do you!?"
                        bo"Let's find out who beats who once again!"
                        $ renpy.sound.play("/audio/soun_fx/countdown.opus", channel="sfx2", loop=False, relative_volume = 0.9)
                        hide screen scrollingtext
                        show screen scrollingtext (f"Push {him_name} off you by rapidly tapping!")
                        show halfblack with dissolve
                        pause 1
                        hide halfblack with dissolve
                        hide int1_tr with Dissolve(0.2)
                        call screen strength_minigame2("l0_opportunity2_win", "l0_opportunity2_lose", "int1_tr", 0.5,False,strengthlevel)

                    "Only because you asked nicely...":
                        $ change_music_volume(0.4, 1.0)
                        bo"Alright, alright..."
                        bo"I can respect the fact that you at least asked nicely this time..."
                        call changeRespect("Himawari", 2) from _call_changeRespect_115
                        scene bg bb day:
                            blur 10
                        show hima worried2:
                            zoom 0.4 xalign 0.5
                        with dissolve
                        him"T-thanks... I'll leave you to it."
                        hide hima with dissolve
                        himt"...Asshole!"
                        scene bedroom_gymend with dissolve:
                            zoom 1.05
                        himt"I've never really paid much attention to his physique, but it looks like he's been putting on some extra muscle lately..."
                        scene black with dissolve
                        call changeStrength(2) from _call_changeStrength_1
                        "You spent some extra time training..."
                        jump action_taken
                    


                show hima mad:
                    xpos 1200 zoom 0.34
                show hima:
                    easein 0.5 xpos 70
                pause 0.4
                scene black
                him"W-why did you turn it louder, you stupid bozo!" with vpunch
                show bg bb day:
                    blur 10
                show int1_tr at smallshake
                bo"Oh! There she goes again... Hehe!" with vpunch
                show int1_tr at smallshake
                him"You... *Grrr*!"
                bo"You never learn, do you!?"
                $ renpy.sound.play("/audio/soun_fx/countdown.opus", channel="sfx2", loop=False, relative_volume = 0.9)
                hide screen scrollingtext
                show screen scrollingtext (f"Push {him_name} off you by rapidlly tapping!")
                show halfblack with dissolve
                pause 1
                hide halfblack with dissolve
                hide int1_tr with Dissolve(0.2)
                call screen strength_minigame2("l0_opportunity2_win", "l0_opportunity2_lose", "int1_tr", 0.5,False,strengthlevel)

            else:
                "You were just about to wrap up when..."
                show bedroom_gymend with dissolve:
                    zoom 1.05
                him"Hey asshole!" with Shake((0, 0, 0, 0), 0.7, dist=20, peak_time=0.7, smoothness=50)
                show hima mad:
                    xpos 2000 zoom 0.34
                show hima:
                    easein 0.7 xpos 700
                bo"Huh? What do you-"
                show hima:
                    easein 0.3 xpos 300
                pause 0.2
                scene black
                him"Turn down your shitty music you stupid bozo!" with vpunch
                show bg bb day:
                    blur 10
                show int1_tr
                with dissolve
                "[him_name] angrily charges on to you and tries to push you out of her way..."
                bo"W-what the hell has gotten into you?"
                show int1_tr at smallshake
                him"M-move out of the way, asshole!"
                menu:
                    him"M-move out of the way, asshole!"
                    "Wrestle her off!":
                        bo"You really think I'll let you walk in here and make demands?"
                        bo"You'll have to get past me first! Hehe!" with vpunch
                        show int1_tr at smallshake
                        him"You... *Grrr*!"
                        $ renpy.sound.play("/audio/soun_fx/countdown.opus", channel="sfx2", loop=False, relative_volume = 0.9)
                        hide screen scrollingtext
                        show screen scrollingtext (f"Push {him_name} off you by rapidlly tapping!")
                        show halfblack with dissolve
                        pause 1
                        hide halfblack with dissolve
                        hide int1_tr with Dissolve(0.2)
                        if is_opportunity_unlocked("l0_opportunity2", strength):
                            call screen strength_minigame2("l0_opportunity2_win", "l0_opportunity2_lose", "int1_tr", 0.5,False,strengthlevel)
                        else:
                            call screen strength_minigame2("l0_opportunity1_win", "l0_opportunity1_lose", "int1_tr", 0.5,True,strengthlevel)

                        

                        label l0_opportunity2_lose:
                            $ renpy.sound.play("audio/soun_fx/attributeslost.opus", channel="sfxstat", loop=False, relative_volume=1)
                            hide screen scrollingtext
                            show screen scrollingtext(f"Strength check{{color=#FF0000}} failed{{/color}}")
                            show int2_tr at smallshake
                            $ renpy.pause(0.6, hard=True)
                            "You tried to push [him_name] away, but you slipped up and..."
                            label l0_opportunity2_lose_jumpbed:
                            hide screen scrollable_scene
                            scene black
                            bo"Aw-Ouch!" with vpunch
                            show int3 with dissolve
                            $ l0_opportunity1_lose_1sttime = True
                            "...She kicked you in the balls!"
                            bo"N-not... fair...! *Wheezing*"
                            show int3_1 with dissolve
                            him"Hands off of me, loser!" with vpunch
                            if pullpants_d_wrestle3_pants == True:
                                him"I am also telling [hin_rel] you tried to pull my shorts down!"
                            $ change_music_volume(0.5, 2.0)
                            "[him_name] walked all over you and turned down your music..."
                            him"And stay down!"
                            bo"Y-you... B-bitch! *Painful groans* Aw-w..."
                            $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.8)
                            him"Hmph!"
                            scene black
                            $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                            call changeRespect("Himawari", -1) from _call_changeRespect_116
                            him"...Better luck next time, weakling! Teehee!" with vpunch
                            bo"*Groans* Next time... I'll g-get you for sure..."
                            $ renpy.end_replay()
                            jump action_taken


                        label l0_opportunity1_win:
                            $ renpy.sound.play("audio/soun_fx/attributes.opus", channel="sfxstat", loop=False, relative_volume=1)
                            hide screen scrollingtext
                            show screen scrollingtext(f"Strength check{{color=#00ff00}} passed{{/color}}")
                            show int1_tr at smallshake
                            default l0_opportunity1_lose_1sttime = False
                            if l0_opportunity1_lose_1sttime == False:
                                $ l0_opportunity1_lose_1sttime = True
                                hide int1_tr
                                show int2_tr
                                with dissolve
                                bo"I got you now!"
                                him"In your dreams!"
                                jump l0_opportunity1_lose_1sttime

                            default l0_opportunity1_win_defeated = False
                            $ l0_opportunity1_win_defeated = True
                            $ renpy.pause(0.6, hard=True)
                            hide int1_tr
                            show int2_tr
                            with dissolve
                            bo"You are done for..."
                            scene black with vpunch
                            bo"Hehe! You thought I wouldn't be ready for your dirty tricks?"
                            show int4_1 with dissolve
                            bo"Weak!"
                            him"L-let me go, you s-shithead!"
                            bo"I am not falling for your shady tactics again!"
                            bo"This time..."
                            menu:
                                bo"This time..."
                                "You'll face the consequences!":
                                    pass
                                "{color=[hatredcolor]}I should punish you...{/color}":
                                    pass
                                "Forgive her...":
                                    pass
                                
                            jump action_taken
                        label l0_opportunity1_lose:
                            $ renpy.sound.play("audio/soun_fx/attributeslost.opus", channel="sfxstat", loop=False, relative_volume=1)
                            hide screen scrollingtext
                            show screen scrollingtext(f"Strength check{{color=#FF0000}} failed{{/color}}")
                            label l0_opportunity1_lose_1sttime:
                            show int2_tr at smallshake
                            $ renpy.pause(0.6, hard=True)
                            "You tried to push [him_name] away, but she read your move, grabbed your hand and..."
                            scene black
                            bo"Aw-Ouch!" with vpunch
                            show int3 with dissolve
                            $ l0_opportunity1_lose_1sttime = True
                            "...Kicked you in the balls!"
                            bo"N-not... fair...! *Wheezing*"
                            show int3_1 with dissolve
                            him"Hands off of me, loser!" with vpunch
                            $ change_music_volume(0.5, 2.0)
                            "[him_name] walked all over you and turned down your music..."
                            him"And stay down!"
                            bo"Y-you... B-bitch! *Painful groans* Aw-w..."
                            $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.8)
                            him"Hmph!"
                            scene black
                            $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                            call changeRespect("Himawari", -1) from _call_changeRespect_117
                            him"...Better luck next time, weakling! Teehee!" with vpunch
                            jump action_taken





                    "Okay, okay! I am sorry...":
                        bo"Okay, okay! You don't have to be so pushy..."
                        show int1_tr at smallshake
                        him"Then get out of the way, you stinky sweaty stickman!"
                        scene black
                        bo"H-hey!" with vpunch
                        "You held back and didn't put up much of a fight..."
                        show int3_1 with dissolve
                        $ change_music_volume(0.5, 2.0)
                        "[him_name] took advantage of that..."
                        "She pushes you away and turns down your music."
                        him"Use your peanut sized brain to consider that there's others besides you in the house..."
                        him"What if [hin_rel] was sleeping, what if I was studying?"
                        bo"I know, I know... I am sorry!"
                        $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.8)
                        call changeRespect("Himawari",1) from _call_changeRespect_118
                        him"Hmph!"
                        scene black
                        $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                        him"...Asshole!" with vpunch
                        "[him_name] left, slamming your bedroom door behind her..."
                        show bedroom_gymstart with dissolve
                        bot"It wasn't even that loud to begin with..."
                        bo"*Sigh*"
                        bot"I was about to wrap up anyway..."
                        jump action_taken

        else:
            label opportunity1failed:
            "You are satisfied with your progress, but... nothing eventful happened."
            scene black with dissolve
        
    "Nothing eventful happened..."
    jump action_taken

label l0_opportunity2_win:
    $ renpy.sound.play("audio/soun_fx/attributes.opus", channel="sfxstat", loop=False, relative_volume=1)
    hide screen scrollingtext
    show screen scrollingtext(f"Strength check{{color=#00ff00}} passed{{/color}}")
    show int1_tr at smallshake
    if l0_opportunity1_lose_1sttime == False:
        $ l0_opportunity1_lose_1sttime = True
        hide int1_tr
        show int2_tr
        with dissolve
        bo"I got you now!"
        him"In your dreams!"
        jump l0_opportunity1_lose_1sttime
    $ l0_opportunity1_lose_1sttime = True
    $ renpy.pause(0.6, hard=True)
    hide int1_tr
    show int2_tr
    with dissolve
    bo"You are done for..."
    scene black with vpunch
    him"N-not yet!"
    show int4_1 with dissolve
    bo"Hehe! You thought I wouldn't be ready for your dirty tricks?"
    bo"Weak!" with vpunch
    him"L-let me go, you s-shithead!"
    $ l0_opportunity1_win_defeated = True
    bo"I am not falling for your shady tactics again!"
    bo"This time..."
    menu l0_opportunity2_win_menu:
        bo"This time..."
        "{color=[dominancecolor]}You'll face the consequences!{/color}":
            default facetheconsequences = False
            $ facetheconsequences = True
            label replay_wrestlingdom:
            $ initialize_replay_defaults()
            bo"This time, you'll have to face the consequences of your actions..."
            show int4 with dissolve:
                zoom 1.2 xalign 1.0
            him"C-consequences? What are you talking about you dork!"
            bo"I have a few ideas in mind!"
            menu:
                bo"I have a few ideas in mind!"
                "Pin her against the wall":
                    pass
            scene black with dissolve
            bo"For starters..."
            show bg bb day:
                blur 10
            show wall_pinned:
                zoom 0.7 xalign 0.5
            call changeDominance(1) from _call_changeDominance_63
            him"H-hey! What are you doing!?"with vpunch
            bo"You are the one who tried to wrestle with me in the first place..."
            him"Y-yeah, because you are annoying!"
            bo"Heh! Remember when we used to wrestle all the time when we were younger?"
            him"Because you WERE annoying back then too!"
            bo"Annoying as I am... I always had the upper hand! Is that why you started taking your own training so seriously...?"
            bo"Dreaming that one day you could beat me? Hehehe!"
            "You kept playfully teasing [him_name]..."
            him"I could beat you anytime I wanted, loser! You are just not worth taking seriously is all..." with vpunch
            scene black
            bo"Oh yeah? Show me then!" with vpunch
            $ boruto_location = "wrestlehimawari"
            $ infobutton ="active"
            $ clickinfobutton = f"Find hotzones and 'wrestle' with {him_name}!" # text displayed when clicking info button
            show screen actionbuttonshouse with dissolve
            him"H-hey! What do you think you are doing?"
            show wrestle1:
                yalign 1.0
            show wrestle1:
                easein 2 yalign 0.0
            with dissolve
            "You threw [him_name] on to your bed and climbed on top of her!"
            "Find hotzones on her body and 'wrestle' with her!"
            show screen scrollable_scene(bgtoadd="bg wrestle", imagetoadd="wrestle1", facetoadd=None,mask1="wrestle1_arms", hovertext1="Pin her arms", jump1="d_pinarms1", mask2="wrestle1_stomach", hovertext2="Press on her stomach", jump2="d_stomach1", mask3=None, hovertext3=None, jump3=None) with dissolve
            him"H-hey! What do you think you are doing?" with vpunch
            $ ui.interact()




                

        "{color=[hatredcolor]}I should punish you...{/color}" (secrethatred = True) if facetheconsequences == True:
            call checkHatred(20, "l0_opportunity2_win_menu") from _call_checkHatred_12
            bo"This time, I am thinking I should punish you!"
            bo"Frankly, I've had enough of your shit..."
            label replay_wrestlinghate:
            $ initialize_replay_defaults()
            if _in_replay:
                $ percentage = 0
            show int4 with dissolve:
                zoom 1.2 xalign 1.0
            bo"Brats should be taught a lesson after all, should they not!?" with vpunch
            him"W-what are you talking about you dork! L-let me go..."
            bo"I don't think so!"
            menu:
                bo"I don't think so!"
                "Pin her against the wall":
                    pass
            scene black with dissolve
            bo"I am only getting started after all!"
            show bg bb day:
                blur 10
            show wall_pinned:
                zoom 0.7 xalign 0.5
            call changeDominance(1) from _call_changeDominance_64
            him"H-hey! What are you doing!?"with vpunch
            bo"You are the one who tried to wrestle with me in the first place, scared to do it now?"
            him"S-scared... of you? HA! Don't make me laugh..."
            bo"Heh! Remember when we used to wrestle all the time when we were younger?"
            him"S-so what..."
            bo"I always gave you a fighting chance because I felt sorry for you..."
            bo"Not this time! No more favors, no more Mr. Nice guy for you!"
            him"I can b-beat you anytime I want you bum!"
            bo"Oh yeah? Is that why you started taking your own training so seriously...?"
            bo"Dreaming that one day you could beat me? Hehehe!"
            "You kept teasing [him_name]..."
            him"You are just not worth taking seriously is all..." with vpunch
            scene black
            bo"That's it! I've had it with you!" with vpunch
            bo"It's time for you to learn your place..."
            $ boruto_location = "wrestlehimawari"
            $ infobutton ="active"
            $ clickinfobutton = f"Find hotzones and 'wrestle' with {him_name}!" # text displayed when clicking info button
            show screen actionbuttonshouse with dissolve
            show h_wrestle1:
                yalign 1.0
            show h_wrestle1:
                easein 2 yalign 0.0
            with dissolve
            call changeHatred(1) from _call_changeHatred_101
            bo"And your place is beneath me, you little bitch!"
            him"H-hey! What do you think you are doing?"
            "You threw [him_name] on to your bed and climbed on top of her!"
            show h_wrestle1:
                easein 2 yalign 1.0
            "You held her in place by sitting on top of her and restricting her legs in between your crotch, your arms ready to stop any of her movements..."
            "Find hotzones on her body and 'wrestle' with her!"
            show screen scrollable_scene(imagetoadd="h_wrestle1", facetoadd=None,mask1="h_wrestle1_asshover", hovertext1="Grab her ass!", jump1="h_wrestle1_asslabel", mask2="h_wrestle1_torso", hovertext2="Pin her down!", jump2="h_wrestle1_torsolabel") with dissolve    
            $ ui.interact()
        "Forgive her...":
            bo"This time I'll let you go, if you promise to stop making a fuss. More importantly, you'll stop making demands of me..."
            bo"You could just nicely ask you know... 'Hey [bo_name], my lovely [him_rel_to_bo]... Could you please turn down the volume a little bit?' Hehe!"
            him"Hmph! As if..." with vpunch
            bo"Say the words, [him_name]..."
            him"F-fine... I promise. Happy now?"
            bo"That's my good little [him_rel]!"
            him"Now let me go!" with vpunch
            scene black with dissolve
            bo"Careful though, next time I may not be so lenient!"
            show bedroom_gymend with dissolve
            show hima mad at right with dissolve:
                zoom 0.31
            him"You are lucky you were born a boy, and I was born a girl..."
            him"Otherwise I'd beat your ass!"
            bo"In the coping phase I see..."
            bo"Maybe I'll let you win next time, don't want you to be depressed after all! Hehe!"
            hide hima with dissolve
            call changeRespect("Himawari",1) from _call_changeRespect_119
            him"...Y-you dummy!"
            jump action_taken


label h_wrestle1_asslabel:
    hide screen scrollable_scene
    hide screen scrollingtext
    show screen scrollable_scene(initial_ypos=1.0,imagetoadd="h_wrestle1_ass")
    with dissolve
    call increaselust(5) from _call_increaselust_90
    bot"So s-soft... and squishy! Maybe I'll give it a little spank as her punishment!"
    hide screen scrollable_scene
    hide screen scrollingtext
    show screen scrollable_scene(initial_ypos=0.0,imagetoadd="h_wrestle1_ass")
    with dissolve
    him"W-where do you think you are putting your hands on!"
    bo"I am just h-holding you down! Too weak to do anything about it!? Heheheh!"
    hide screen scrollable_scene
    scene black
    call changeRespect("Himawari", -1) from _call_changeRespect_120
    bo"Aww-ouch!" with vpunch
    him"W-what's with the creepy grin on your face, you weirdo!" with vpunch
    "She raised her heel and..."
    jump l0_opportunity2_lose_jumpbed

label h_wrestle1_torsolabel:
    hide screen scrollable_scene
    hide screen scrollingtext
    show screen scrollable_scene(initial_ypos=0.5,imagetoadd="h_wrestle1_1")
    with dissolve
    "You pressed against her back pinning her down against the mattress. Your other hand opportunistically pushed against her buttocks for support!"
    him"H-hey! W-where are you touching me!" with vpunch
    bo"We are just wrestling..."
    bo"You said you could beat me, did you not!?"
    him"Hnng! L-let... me... GO! Grrr!" with vpunch
    him"I said..."
    $ renpy.sound.play("/audio/soun_fx/countdown.opus", channel="sfx2", loop=False, relative_volume = 0.9)
    hide screen scrollable_scene
    show screen scrollingtext("Let... me... go!")
    show h_wrestle1_1:
        yalign 0.4
    show halfblack
    with dissolve
    pause 1
    hide halfblack with Dissolve(3)
    show screen scrollable_scene(initial_ypos=0.4,imagetoadd="h_wrestle1_1")

    if is_opportunity_unlocked("l0_opportunity3", strength):
        call screen strength_minigame2("hate_wrestlewin", "l0_opportunity2_lose", "h_wrestle1_1", 0.4,False,strengthlevel)
    else:
        call screen strength_minigame2("l0_opportunity3_win", "l0_opportunity2_lose", "h_wrestle1_1", 0.4,True,strengthlevel)
    $ ui.interact()

label hate_wrestlewin:
    hide screen scrollable_scene
    hide screen scrollingtext
    show screen scrollable_scene(initial_ypos=0.0,imagetoadd="h_wrestle1_2")
    with dissolve
    bo"Can't even make me budge... You are so weak!"
    "[him_name] kept struggling to escape your clutches, but you easily held her down in place..."
    him"Hnnng...! Mhmmm...!" with vpunch
    bo"Surrender, admit defeat, and maybe I'll consider letting you go!"
    bo"But first, you gotta beg for forgiveness and say that I am superior to you! Hehehe!"
    "Exhausted and weakened, [him_name] laid almost powerless under you, only managing a few feeble attempts to push you off whenever she would gasp for enough air and strength to muster another effort..."
    him"Gnnnnhg... N-never! Grrr-!" with vpunch
    bo"Then you'll have to learn the hard way!"
    bot"She doesn't even have the presence of mind to realize that I am coping a feel of her ass!"
    bot"Considering this is supposed to be a punishment, maybe I can go even further!"
    bot"Hehehe..."
    show screen scrollable_scene(initial_ypos=0.0,bgtoadd=None, imagetoadd="h_wrestle1_2",mask1="h_wrestle1_asshover2", hovertext1="Lower her pants!", jump1="hate_wrestle_lowerpants", mask2="h_wrestle1_choke", hovertext2="Put her in a chokehold!", jump2="hate_wrestle_chokehold") with dissolve
    show screen scrollingtext("Teach her a lesson!")
    $ ui.interact()

label hate_wrestle_chokehold:
    hide screen scrollable_scene
    hide screen scrollingtext
    show screen scrollable_scene(initial_ypos=1.0,imagetoadd="h_wrestle2")
    with dissolve
    "You slid upwards until your torso was brushing against her buttocks..."
    hide screen scrollable_scene
    show screen scrollable_scene(initial_ypos=0.0,imagetoadd="h_wrestle2")
    with dissolve
    him"D-don't touch me t-there! You perv-"
    hide screen scrollable_scene
    scene black
    "Before she could mutter her protests, you lunged forward..." with vpunch
    show h_wrestle3 with dissolve
    show h_wrestle3:
        easein 2 yalign 0.5
    bo"...You were saying!?" with vpunch
    bo"If you aren't comfortable getting up close and personal, perhaps you aren't cut out for being a Kunoichi, [him_name]!" with vpunch
    him"Hnnng... L-let... go of me! Hnngn-"
    bo"Maybe you should give up on you training and look into a different profession..."
    him"Hnnhn... S-shut up! I am n-not..." with vpunch
    call increaselust(10) from _call_increaselust_91
    $ renpy.sound.play("/audio/soun_fx/eye1s.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    show h_wrestle3_1 with flash:
        zoom 1.1 xalign 1.0 yalign 0.4
    call changeHatred(2) from _call_changeHatred_102
    "Wrestling and dominating [him_name] awakened something in you. The feeling of control over her seemed to only embolden you..."
    bot"I am getting a massive erection right now, it's rubbing against her ass! She must be surely feeling my cock, but she is too dumb to even realize..."
    him"Hnnhn... I am n-not... Hnngn... giving up... yet!" with vpunch
    bo"Then I'll have to show you why I was renowned for my Taijutsu!"
    hide screen scrollable_scene
    show bg wrestle:
        blur 10
    show h_wrestle4:
        zoom 0.65 xalign 0.5 yalign 0.9
    with dissolve
    bo"How's this, you bitch! Give up already..."
    him"Hnnng... N-no!"
    "By now, [him_name] was struggling to breathe... It was clear she stood no chance. Her stubbornness was the only thing keeping her from surrendering..."
    bo"Come on... I wouldn't want you to faint on me! Or would I..." with vpunch
    him"Hnngn... S-shut... Hnnghgnn.... Up!" with vpunch
    bo"Just tap on my leg and admit defeat!"
    him"Hnng... N-no!"
    bo"Remember, you brought this upon yourself by being a bitch...  Surrender already!"
    show h_wrestle4_1 with dissolve:
        zoom 1.5 xalign 0.5 yalign 1.0
    show h_wrestle4_1:
        easein 2 yalign 0.4
    pause 1.5
    show h_wrestle4_1 with dissolve:
        zoom 0.65 xalign 0.5 yalign 0.9
    him"N-no... Hhnng... I won't... Hnghn!!"
    "Her words were steadfast, but her body was caving in, evident by her eyes rolling up and her hand reaching back towards your leg. A few seconds longer and she would surely lose her senses..."
    him"Hnng... I can s-still... win!"
    "Her will was betrayed by her own body. She reflexively started tapping on your leg, but her fighting words never ceased..."
    menu:
        "Her will was betrayed by her own body. She reflexively started tapping on your leg, but her fighting words never ceased..."
        "{color=[hatredcolor]}Maintain the chokehold...{/color}":
            bo"Which one is it [him_name]! You say you want to fight, your body says otherwise..."
            him"Hnng... I... Hngn..."
            call changeHatred(1) from _call_changeHatred_103
            bo"Hahaha! So weak, you can't even speak! Remember this fight next time you parade around the house, you bitch!" with vpunch
            him"..."
            "By now, [him_name] was almost completely silent, barring the occasional gag..."
            "You knew she had no fight left in her besides her delusional words..."
            scene black with vpunch
            bo"There, there..."
            hide screen scrollable_scene
            show screen scrollable_scene(initial_ypos=0.0,imagetoadd="h_wrestle2_1")
            with dissolve
            him"*Exhausted gasping*"
            hide screen scrollable_scene
            show screen scrollable_scene(initial_ypos=1.0,imagetoadd="h_wrestle2_1")
            with dissolve
            "You let her go before she lost her senses and fell back on her buttocks once again..."
            "[him_name] only had enough strength to gasp for air until she would regain her awareness..."
            bo"I kinda feel sorry for you, but I do like you better when you are not constantly nagging and insulting me!"
            him"*Gasping*"
            bo"Let this be a lesson to you! Swallow your pride and surrender when given the chance to do so you bitch!"
        "Let her go":
            scene black
            bo"I kinda feel sorry for you..." with vpunch
            hide screen scrollable_scene
            show screen scrollable_scene(initial_ypos=0.0,imagetoadd="h_wrestle2_1")
            with dissolve
            him"*Gasping for air*"
            bo"You should learn when to give up, little [him_rel]..."
            him"*Gasp* That hurt, you... *Gasp* asshole!"
            bo"You could give up at any time... You brought this upon yourself!"
            him"*Exhausted gasping*"
    bot"Now would be the time to try something! Heheh..."
    hide screen scrollingtext
    hide screen scrollable_scene
    show screen scrollable_scene(initial_ypos=0.0,bgtoadd=None, imagetoadd="h_wrestle2_1",mask1="h_wrestle2_asshover", hovertext1="Lower her pants!", jump1="hate_wrestle_pantsfinal", mask2="h_wrestle2_fishhook", hovertext2="Fishhook her!", jump2="hate_wrestle_fishhook")
    show screen scrollingtext("Serve the final punishment!")
    with dissolve
    
    $ ui.interact()


        
label hate_wrestle_pantsfinal:
    hide screen scrollable_scene
    hide screen scrollingtext
    show h_wrestle1_ass2:
        yalign 1.0
    with dissolve
    bo"But we aren't done just yet..."
    hide screen scrollable_scene
    hide screen scrollingtext
    show screen scrollable_scene(initial_ypos=1.0,imagetoadd="h_wrestle1_ass3", facetoadd="h_wrestle1_assface1")
    with dissolve
    bo"I have one more punishment to dish out..." with vpunch
    bo"N-nice matching panties, you bitch!"
    hide screen scrollable_scene
    hide screen scrollingtext
    show screen scrollable_scene(initial_ypos=0.0,imagetoadd="h_wrestle1_ass3", facetoadd="h_wrestle1_assface1")
    with dissolve
    him"*Gasping for air* W-what a-are you..."
    call increaselust(5) from _call_increaselust_92
    hide screen scrollable_scene
    hide screen scrollingtext
    show screen scrollable_scene(initial_ypos=1.0,imagetoadd="h_wrestle1_ass3", facetoadd="h_wrestle1_assface1")
    with dissolve
    bot"*Gulp* What an ass!"
    menu:
        bot"*Gulp* What an ass!"
        "Spank her!":
            bo"A little disciplinary spanking never hurt anyone, [hin_rel] would concur!"
            hide screen scrollable_scene
            show h_wrestle1_ass3_grope3:
                yalign 1.0
            with dissolve
            bo"Remember, this is your punishment!"
            show h_wrestle_spank with moveinleft
            $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.7)
            with vpunch
            hide h_wrestle_spank
            show h_wrestle1_ass3_grope4 
            with dissolve
            bo"...Bitch!"
            hide screen scrollable_scene
            show screen scrollable_scene(initial_ypos=0.0,imagetoadd="h_wrestle1_ass3_grope4", facetoadd="h_wrestle1_assface1")
            with dissolve
            bo"I gotta give it to you, all that exercising surely helped develop this area down here..."
            hide screen scrollable_scene
            show screen scrollable_scene(initial_ypos=1.0,imagetoadd="h_wrestle1_ass3_grope4", facetoadd="h_wrestle1_assface1")
            with dissolve
            bot"My god! To think my [him_rel] had an ass like that on her... I had no idea!"
            call increaselust(10) from _call_increaselust_93
            bot"F-fuck! I am getting the urge to shove something else in there..."
            show hatred_choice onlayer screens with dissolve 
            $ config.menu_include_disabled = False
            $ config.menu_include_disabled = True
            $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx2", loop=False, relative_volume = 1.2)
            menu h_wrestlefinalmenu:
                bot"F-fuck! I am getting the urge to shove something else in there..."
                "Spank her again!" if percentage <80:
                    hide screen scrollable_scene
                    $ config.menu_include_disabled = False
                    show h_wrestle1_ass3_spank1:
                        yalign 1.0
                    with dissolve
                    bo"Just one spanking isn't enough for you..."
                    show h_wrestle_spankright with moveinright
                    $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                    with vpunch
                    hide h_wrestle_spank
                    show h_wrestle1_ass3_spank3 
                    with dissolve
                    bo"...Is it?!"
                    hide screen scrollable_scene
                    show screen scrollable_scene(initial_ypos=0.0,imagetoadd="h_wrestle1_ass3_spank3")
                    with dissolve
                    $ renpy.sound.play("/audio/soun_fx/himawari/kyaa.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                    him"*Gasp*!" with vpunch
                    hide screen scrollable_scene
                    show screen scrollable_scene(initial_ypos=1.0,imagetoadd="h_wrestle1_ass3_spank3")
                    with dissolve
                    bot"O-oh shit!" with vpunch
                    hide screen scrollable_scene
                    scene black with vpunch
                    bo"Ow-ouch!" with vpunch
                    "[him_name] regained her awareness... In an instant, she raised her heel and kicked you in the balls..."
                    him"MOOOOOOM!!!" with vpunch
                "{color=[hatredcolor]}!?! *The beast rumbles...*{/color}" (secrethatred = True) if percentage >=80:
                    if v17_update == True:
                        pass
                    else:
                        $ notification("Exclusive supporters scene")

                    
                    label hima_gameover_wrestling:
                    $ initialize_replay_defaults()
                    hide screen actionbuttonshouse with dissolve
                    stop music fadeout 3
                    $ config.menu_include_disabled = False
                    $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx2", loop=False, relative_volume = 1.2)
                    bot"What is this... f-feeling inside of me!"  with flashred
                    $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx2", loop=False, relative_volume = 1.2)
                    bot"I..." with flashred
                    $ playmusic("audio/ost/kumogakure.opus",0.6)
                    $ renpy.sound.play("/audio/soun_fx/growl1.opus", channel="sfx3", loop=False, relative_volume = 0.9)   
                    $ renpy.sound.play("/audio/soun_fx/eye4s.opus", channel="sfx1", loop=False, relative_volume = 0.3) 
                    show kurama1 onlayer screens with flashred
                    show kurama1 onlayer screens:
                        easein 2 alpha 0.0
                    $ renpy.sound.play("/audio/soun_fx/heartbeatlong.opus", channel="sfx2", loop=False, relative_volume = 1.2)
                    beast"*Growls...*"
                    bo"[him_name]..." with flashred
                    bo"I... Y-you..."
                    bo"You..."
                    hide screen scrollable_scene
                    show hatred_choice zorder 100000 onlayer screens with dissolve
                    $ renpy.sound.play("/audio/soun_fx/heartbeatlongfast.opus", channel="sfx2", loop=False, relative_volume = 1.2)
                    $ renpy.sound.play("/audio/soun_fx/claw2.opus", channel="sfx1", loop=False, relative_volume = 0.6)
                    $ renpy.sound.play("/audio/soun_fx/ripclothes1.opus", channel="sfx3", loop=False, relative_volume = 0.8)
                    show blackscreen onlayer screens with flashred
                    $ renpy.sound.play("/audio/soun_fx/growl2.opus", channel="sfx1", loop=False, relative_volume = 0.6)
                    beast"Yes... YES! *Primal Growl*!" with vpunch
                    "A deep resonant rumble reverberated through your entire being..."
                    "Something ancient awakened within, seizing control of both body and mind."
                    $ renpy.sound.play("/audio/soun_fx/ripclothes2.opus", channel="sfx3", loop=False, relative_volume = 0.8)
                    show screen scrollable_scene(initial_ypos=1.0,imagetoadd="rip1", facetoadd="h_wrestle1_assface1") with flashred
                    bo"You f-fucking bitch!" with vpunch
                    him"*Gasping for air* ...[bo_name_stutter]?"
                    "[him_name] still on the brink of unconsciousness, felt that something was wrong but had yet to fully regain her awareness..."
                    bo"W-what's... h-happening to me..." with flashred
                    "In a state of trance, and in constant excruciating pain, you helplessly observed yourself physically responding to whatever was burrowed inside you..."
                    "Your fingernails grew into sharp, fox-like claws, your facial features contorted and reshaped with audible cracks..."
                    bo"T-this pain... T-this reaction..." with vpunch
                    bo"It's the s-same as w-with Ino..."
                    $ renpy.sound.play("/audio/soun_fx/claw3.opus", channel="sfx1", loop=False, relative_volume = 0.6)
                    $ renpy.sound.play("/audio/soun_fx/ripclothes1.opus", channel="sfx3", loop=False, relative_volume = 0.8)
                    show screen scrollable_scene(initial_ypos=1.0,imagetoadd="rip2", facetoadd="h_wrestle1_assface1") with flashred
                    "Another tear of your claws, and what little was left of her clothing was now ripped to shreds..."
                    "Your claws swept and burrowed her skin, living crimson trails of blood across her vulnerable flesh..."
                    bo"It.. It m-must be your fault! Y-you bitch..."
                    bo"You will pay for t-this..." with vpunch
                    $ renpy.sound.play("/audio/soun_fx/growl3.opus", channel="sfx3", loop=False, relative_volume = 0.9)   
                    $ renpy.sound.play("/audio/soun_fx/eye4s.opus", channel="sfx1", loop=False, relative_volume = 0.3) 
                    show kurama1 onlayer screens with flashred
                    show kurama1 onlayer screens:
                        easein 2 alpha 0.0
                    beast"Take her... Breed her! *Growls*"
                    him"*Heavy breathing* M-my... clothes? It h-hurts...? W-why..."
                    "[him_name] was on the cusp of understanding the nightmare she was being subjected to..."
                    bo"It's... your fault! This pain I am feeling... This desire... I must... share it with you!" with vpunch
                    hide hatred_choice onlayer screens with dissolve 
                    "The pain started to subside, or rather..."
                    hide screen scrollable_scene
                    show screen scrollable_scene(initial_ypos=1.0,imagetoadd="rip2", facetoadd="h_wrestle1_assface1")
                    with dissolve
                    "It morphed into a twisted, all-consuming lust..."
                    hide screen scrollable_scene
                    show screen scrollable_scene(initial_ypos=0.0,imagetoadd="rip2", facetoadd="h_wrestle1_assface1")
                    with dissolve
                    bo"[him_name]... My beautiful little [him_rel], I see now..."
                    scene blackscreen
                    hide screen scrollable_scene with dissolve
                    $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                    "You took a step back and teared away your own clothes..."
                    hide blackscreen onlayer screens
                    show rip2:
                        yalign 0.0
                    show h_wrestle1_assface1:
                        yalign 0.0
                    with dissolve
                    him"..."
                    scene rip2:
                        yalign 0.0 zoom 1.2 xalign 0.5
                    show h_wrestle1_assface2:
                        yalign 0.0 zoom 1.2 xalign 0.5
                    with dissolve
                    him"[bo_name_stutter]... W-what are you-"
                    scene rip2:
                        yalign 0.0 zoom 1.4 xalign 0.5
                    show h_wrestle1_assface2:
                        yalign 0.0 zoom 1.4 xalign 0.5
                    with dissolve
                    scene black with vpunch
                    $ renpy.sound.play("/audio/soun_fx/himawari/himascared2.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                    him"!! *Whimpering*" with vpunch
                    show boru1 at dizzyflash:
                        yalign 1.0 blur 20
                    with dissolve
                    $ renpy.sound.play("/audio/soun_fx/earringing.opus", channel="sfx3", loop=False, relative_volume = 0.05)
                    show boru1 at dizzyflash:
                        easein 5 yalign 0.0 blur 0
                    bo"Your virgin holes... they are calling for me..." with vpunch
                    himt"*Regaining consciousness* V-virgin...? Is that...?"
                    bo"It is what I lusted for all along..."
                    bo"I was only held back by shitty ideals, but with this power surging in me..."
                    bo"I know what I need..."
                    $ renpy.sound.play("/audio/soun_fx/himawari/himascared1.opus", channel="sfx3", loop=False, relative_volume = 0.4)
                    him"[bo_name_stutter]!? W-w-w-why are you n-" with vpunch
                    scene boru1 with dissolve:
                        zoom 1.2 xalign 0.5 yalign 0.0
                    bo"I will breed you myself, you FUCKING WHORE!" with vpunch
                    scene boru1 with dissolve:
                        zoom 1.4 xalign 0.5 yalign 0.0
                    "One look into your eyes and [him_name] knew..."
                    scene black with vpunch
                    $ renpy.sound.play("/audio/soun_fx/himawari/himascream.opus", channel="sfx3", loop=False, relative_volume = 0.3)
                    him"*Screams!*"
                    show kurama1 at dizzy with dissolve:
                        alpha 0.8
                    menu:
                        beast"..."
                        "{color=[hatredcolor]}I've laid dormant long enough...{/color}":
                            beast"I've laid dormant long enough..."
                            beast"It's time for me to be reborn..."
                            beast"Silence her..."
                            $ renpy.sound.play("/audio/soun_fx/growl1.opus", channel="sfx3", loop=False, relative_volume = 0.9)   
                            $ renpy.sound.play("/audio/soun_fx/eye4s.opus", channel="sfx1", loop=False, relative_volume = 0.3) 
                            show kurama1 at dizzy2 with flashred:
                                linear 1 alpha 0.0
                            beast"Breed her!"
                    him"N-No, NO! W-WHAT ARE Y-YOU- MOOOOOOOOOOOOOM!!!!" with vpunch
                    show choke1:
                        yalign 0.0
                    $ renpy.sound.play("/audio/soun_fx/himawari/himagrunt.opus", channel="sfx3", loop=False, relative_volume = 0.3)
                    bo"Shut the fuck up already..." with flashred
                    scene black with dissolve
                    "Meanwhile..."
                    scene kitchen day hinata with dissolve
                    $ renpy.sound.play("/audio/soun_fx/himawari/himascream.opus", channel="sfx3", loop=False, relative_volume = 0.03)
                    "*Faint yells from upstairs*..." with vpunch
                    scene kitchen day
                    show shina surprised at center with dissolve
                    hin"Was that... [him_name]?"
                    show shina serious with dissolve
                    hin"These two must be fighting over something trivial again..."
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatasigh3.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                    show shina shy2 with dissolve
                    hin"*Sigh* Yare yare..."
                    show shina shy with dissolve
                    hin"I should probably check in on them, but first..."
                    show shina smiling with dissolve
                    hin"Gotta make sure lunch is ready! Preferably not burned to a crisp too!"
                    scene kitchen day hinata with dissolve
                    hin"Today's specialty is [him_name]'s favorite red bean soup!"
                    hin"Maybe I can convince her to stop antagonizing [bo_name] so much by preparing it more often! *Giggles*!"
                    scene black with dissolve
                    $ renpy.sound.play("/audio/soun_fx/inogag3.opus", channel="sfx3", loop=False, relative_volume = 0.9)
                    show choke1 with dissolve:
                        yalign 0.1
                    him"*Struggling to breathe* Ahh...Gah...gh!" with vpunch
                    bo"This is for all the times you looked down on me!" with vpunch
                    show choke1 with dissolve:
                        yalign 0.2
                    bo"And this..."
                    $ renpy.sound.play("/audio/soun_fx/pushitin2.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                    show choke1 with flash:
                        yalign 0.4
                    bo"This is for every smirk, every disdainful glance, every time you teased me with those whoreish looks of yours!"
                    $ renpy.sound.play("/audio/soun_fx/inogag2.opus", channel="sfx3", loop=False, relative_volume = 0.9)
                    $ renpy.sound.play("/audio/soun_fx/pushitin1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                    show internal_vag 1 with dissolve:
                        zoom 0.5 xalign 1.0 yalign 0.0
                    show choke1 with flash:
                        yalign 0.6
                    bo"How's this for revenge, you bitch!"
                    $ renpy.sound.play("/audio/soun_fx/pushitin2.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                    show internal_vag 2 with dissolve:
                        zoom 0.5 xalign 1.0 yalign 0.0
                    show choke1 with flash:
                        yalign 1.0
                    him"!! *Asphyxiating* Gah... nnh..ah!" with vpunch
                    bo"Acting so superior, so untouchable..."
                    $ renpy.sound.play("/audio/soun_fx/pushitin1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                    show internalvag_anim1 with dissolve:
                        zoom 0.5 xalign 1.0 yalign 0.0
                    $ renpy.sound.play("/audio/soun_fx/pushitin2.opus", channel="sfx1", loop=False, relative_volume = 1.0)
                    show choke1:
                        easein 10 yalign 0.1
                    bo"Feeling your pride crumbling yet!?" with vpunch
                    hide internalvag_anim1
                    hide internal_vag
                    with dissolve
                    bo"All this time, I've been tolerating your shitty behavior, thinking you'd eventually come around..."
                    bo"But it seems to me, your abusive bratty demeanor is just who you are..."
                    bo"Perhaps what you really need..."
                    $ renpy.sound.play("/audio/soun_fx/pushitin1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                    $ renpy.sound.play("/audio/soun_fx/inogag1.opus", channel="sfx3", loop=False, relative_volume = 0.9)
                    hide internalvag_anim1
                    show choke2 with flash:
                        yalign 0.0
                    bo"Is some disciplinary measures!" with vpunch
                    "You tightened your grip around her neck..."
                    show internal_vag 2 with dissolve:
                        zoom 0.5 xalign 1.0 yalign 0.0
                    bo"Tell me, [him_name]..."
                    show choke2 with flash:
                        easein 10 yalign 1.0
                    $ renpy.sound.play("/audio/soun_fx/pushitin2.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                    show internalvag_anim1 with dissolve:
                        zoom 0.5 xalign 1.0 yalign 0.0
                    bo"How does your [him_rel_to_bo]'s cock buried deep inside your virgin pussy feel like..." with vpunch
                    $ renpy.sound.play("/audio/soun_fx/pushitin1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                    bo"You are a virgin, aren't you [him_name]?"
                    $ renpy.sound.play("/audio/soun_fx/pushitin2.opus", channel="sfx1", loop=False, relative_volume = 1.0)
                    bo"I can tell just by how hard your pussy is squeezing me..."
                    $ renpy.sound.play("/audio/soun_fx/pushitin1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                    bo"You are absolutely a virgin! Your walls are gripping my cock with such force..."
                    $ renpy.sound.play("/audio/soun_fx/pushitin2.opus", channel="sfx1", loop=False, relative_volume = 1.0)
                    bo"I am worried I may fill you up in just a few thrusts!"
                    hide internalvag_anim1
                    hide internal_vag
                    with dissolve
                    $ renpy.sound.play("/audio/soun_fx/inogag1.opus", channel="sfx3", loop=False, relative_volume = 0.9)
                    show choke2 with dissolve:
                        yalign 0.0
                    him"*Gasping for air* Gh... Aaah..."
                    bo"But don't worry, my plans for you go much further than simply filling your cunt up once... or twice!"
                    bo"For all these times you've disrespected me..."
                    bo"You'll pass out with my cock buried deep inside of you. And after you do..."
                    $ renpy.sound.play("/audio/soun_fx/pushitin2.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                    show internal_vag 2 with dissolve:
                        zoom 0.5 xalign 1.0 yalign 0.0
                    show choke2 with dissolve:
                        yalign 1.0
                    $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                    $ renpy.sound.play("/audio/soun_fx/pushitin1.opus", channel="sfx3", loop=False, relative_volume = 1.0)
                    show internal_vagcum 1 with flash:
                        zoom 0.5 xalign 1.0 yalign 0.0
                    bo"I'll fill your dumb cunt with my cum! Again... *Moans*"
                    $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                    $ renpy.sound.play("/audio/soun_fx/pushitin2.opus", channel="sfx3", loop=False, relative_volume = 1.0)
                    show internal_vagcum 2 with flash:
                        zoom 0.5 xalign 1.0 yalign 0.0
                    bo"And again... Aaarh! *Loud Moans*"
                    $ renpy.sound.play("/audio/soun_fx/cum11.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                    $ renpy.sound.play("/audio/soun_fx/pushitin2.opus", channel="sfx3", loop=False, relative_volume = 1.0)
                    show internal_vagcum 3 with flash:
                        zoom 0.5 xalign 1.0 yalign 0.0
                    bo"*Moans* And a-again! Till your cunt drains every last drop of my semen..."
                    call decreaselust(10) from _call_decreaselust_78
                    bo"I'll breed your fertile womb like the bitch in heat that you are!" with vpunch
                    $ renpy.sound.play("/audio/soun_fx/pushitin2.opus", channel="sfx3", loop=False, relative_volume = 1.0)
                    hide internalvag_anim1
                    hide internal_vag
                    hide internal_vagcum 
                    with dissolve
                    scene choke3 with dissolve:
                        yalign 1.0
                    show choke3:
                        easein 5 yalign 0.0
                    bo"...You hear me?" with vpunch
                    him"..."
                    bo"Aww, poor little [him_rel]... Just when things were about to get fun..."
                    bo"You went and lost your senses again. You are gonna miss out on what comes next!" with vpunch
                    show choke2 with dissolve:
                        zoom 1.2 yalign 1.0 xalign 0.5
                    pause 0.3
                    bo"Your tight, virgin pussy sure seemed to enjoy my cock seeing how wet you got down there..."
                    scene choke3 with dissolve:
                        yalign 0.0
                    bo"But... I can't help but wonder how the rest of your holes would feel!"
                    bo"I'd prefer if you were awake so we could both enjoy ourselves, but given your attitude... *Sigh*..."
                    bo"Something had to be done!" with vpunch
                    bo"But don't you worry, we are still going to have some fun together..."
                    call increaselust(10) from _call_increaselust_100
                    bo"Seeing your passed out, stupid slutty face like this is enough to keep me going for the rest of the day!"
                    default hima_bad_end_tongueout = False
                    menu hima_badend_finalmenu:
                        bo"Seeing your passed out, stupid slutty face like this is enough to keep me going for the rest of the day!"
                        "{color=[hatredcolor]}Pull her tongue out!{/color}" if hima_bad_end_tongueout == False:
                            $ hima_bad_end_tongueout = True
                            bo"Are you in there, little [him_rel]?"
                            him"..."
                            show choke3_tongue3_1 with dissolve:
                                yalign 0.0
                            bo"Come on, say something..."
                            him"..."
                            bo"Just kidding..."
                            scene choke3_tongue with dissolve:
                                yalign 0.0
                            call changeHatred(100) from _call_changeHatred_111
                            bo"You dumb bitch! You better stay silent..." with vpunch
                            if hima_bad_end_tongueout == True:
                                scene choke3_tongue with dissolve:
                                    yalign 0.0
                            else:
                                scene choke3 with dissolve:
                                    yalign 0.0
                            jump hima_badend_finalmenu
                        "{color=[hatredcolor]}Spit on her!{/color}" if hima_bad_end_tongueout == False:
                            bo"Even passed out, it's like your face calls for me to defile it..."
                            bo"You are such a despicable brat..."
                            $ renpy.sound.play("/audio/soun_fx/spit2.opus", channel="sfx2", loop=False, relative_volume = 0.9)
                            pause 0.4
                            show spitfx1:
                                zoom 1.1 xalign 0.5 yalign 0.05
                            show spitmark1:
                                xalign 0.55 yalign 0.15 zoom 0.15
                            with dissolve and flash
                            call changeHatred(100) from _call_changeHatred_112
                            hide spitfx1
                            show spitmark1 zorder 1:
                                xalign 0.55 yalign 0.15 zoom 0.15 alpha 0.7
                            with dissolve
                            bo"That'll teach you, Bitch!" with vpunch
                            if hima_bad_end_tongueout == True:
                                scene choke3_tongue with dissolve:
                                    yalign 0.0
                            else:
                                scene choke3 with dissolve:
                                    yalign 0.0
                            jump hima_badend_finalmenu

                        "{color=[hatredcolor]}Spit in her mouth!{/color}" if hima_bad_end_tongueout == True:
                            bo"Ah, [him_name]..."
                            show choke3_tongue3_1 with dissolve:
                                yalign 0.0
                            bo"How I wish I could defile you while you were awake..."
                            bo"But we both know [hin_rel] would have something to say about that..."
                            show choke3_tongue3_1 with dissolve:
                                yalign 0.0 zoom 1.2 xalign 0.5
                            bo"I mean, look at the way you look... Just like a bitch in heat!"
                            bo"It's like you are asking to be degraded..."
                            bo"*Sigh* This will have to do..."
                            $ renpy.sound.play("/audio/soun_fx/spit2.opus", channel="sfx2", loop=False, relative_volume = 0.9)
                            pause 0.4
                            show spitfx1:
                                zoom 1.1 xalign 0.48 yalign 0.17
                            show spitmark1:
                                xalign 0.46 yalign 0.76 zoom 0.15
                            with dissolve and flash
                            call changeHatred(100) from _call_changeHatred_113
                            hide spitfx1
                            show spitmark1 zorder 1:
                                xalign 0.46 yalign 0.76 zoom 0.15 alpha 0.6
                            with dissolve
                            bo"You dirty slut!" with vpunch
                            if hima_bad_end_tongueout == True:
                                scene choke3_tongue with dissolve:
                                    yalign 0.0
                            else:
                                scene choke3 with dissolve:
                                    yalign 0.0
                            jump hima_badend_finalmenu

                        "{color=[hatredcolor]}Stretch her mouth open!{/color}" if hima_bad_end_tongueout == True:
                            bo"Ah, [him_name]..."
                            show choke3_tongue3 with dissolve:
                                yalign 0.0
                            bo"If only you used this hole of yours for something else besides barking at me..."
                            show choke3_tongue3_1 with dissolve:
                                yalign 0.0
                            bo"Maybe me and you would be closer then..."
                            show hima_badend_mouthanim with dissolve:
                                yalign 0.1 zoom 1.1 xalign 0.5
                            call changeHatred(100) from _call_changeHatred_114
                            bo"But don't you worry..."
                            bo"I can think of a few other uses for your mouth besides your useless barking!" with vpunch
                            bo"There's still a long day ahead of us..."
                            if hima_bad_end_tongueout == True:
                                scene choke3_tongue with dissolve:
                                    yalign 0.0
                            else:
                                scene choke3 with dissolve:
                                    yalign 0.0
                            jump hima_badend_finalmenu
                        "Let her body drop down..." if hima_bad_end_tongueout == True:
                            pass
                        
                    bo"My dear [him_rel]..."
                    $ renpy.sound.play("/audio/soun_fx/intro/bodythud.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                    scene black with vpunch
                    "You broke the chokehold, leaving [him_name]'s body to drop on the bed..."
                    show boru1 with dissolve:
                        yalign 1.0
                    show boru1:
                        easein 2 yalign 0.0
                    bo"I told you, haven't I?"
                    show choke4 with dissolve:
                        yalign 1.0
                    show choke4:
                        easein 2 yalign 0.0
                    bo"I'll sow my seed in every hole of yours for the rest of the day, you pretentious bitch!" with vpunch
                    show choke4 with dissolve:
                        yalign 1.0
                    bo"I'll fuck you senseless, over and over and over again!"
                    scene black with dissolve
                    $ renpy.sound.play("/audio/soun_fx/clothes_undress.opus", channel="sfx3", loop=False, relative_volume = 1)
                    bo"But before I get started..."
                    show hima_badend0 with dissolve:
                        yalign 1.0
                    show hima_badend0:
                        easein 4 yalign 0.1
                    "You shifted [him_name]'s body around, preparing to mount her as if she were a mare..."
                    "Your cock kept brushing against her vulva as you adjusted her posture to allow for deeper penetration..."
                    show hima_badend0 with dissolve:
                        yalign 0.4
                    bo"I'll make sure I have easy access to all three of your holes..."
                    show hima_badend0 with dissolve:
                        zoom 1.3 xalign 0.0 yalign 0.4
                    bo"Besides, I'd prefer to take a good look at your helpless face whenever I unload my seed in you!"
                    scene black with dissolve
                    "..."
                    scene kitchen day hinata with dissolve
                    "*Silence*..."
                    scene kitchen day
                    show shina shy at center
                    with dissolve
                    hin"Right! Food's ready..."
                    show shina shy2 with dissolve
                    hin"These two have been quiet since then..."
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatasigh2.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                    show shina normal with dissolve
                    hin"*Sigh*... Another one of their short, futile altercations then!"
                    hin"Shall I check up on them anyway?"
                    show shina shy at center with dissolve
                    hin"They'll probably be downstairs soon anyway..."
                    show shina smiling with dissolve
                    hin"They know it's lunch time, and they both eat like there's no tomorrow! *Giggles*"
                    scene black with dissolve
                    "..."

                    scene hima_badend0 with dissolve:
                        yalign 0.6
                    bo"By the end of this day, your womb will be overflowing with my cum..."
                    show screen parallax1280("hima_badend0",1,0.5,False) with dissolve
                    call showscrollingimage from _call_showscrollingimage_53
                    bo"I'll make sure I'll impregnate your ovulating cunt!" with vpunch
                    call hidescrollingimage("Click twice to breed with her...") from _call_hidescrollingimage_54
                    menu:
                        beast"Sow my seed..."
                        "{color=[hatredcolor]}Fuck her pussy!{/color}":
                            pass
                        "{color=[hatredcolor]}Fuck her asshole!{/color}":
                            pass
                        "{color=[hatredcolor]}Fuck her mouth!{/color}":
                            pass
                    $ renpy.sound.play("/audio/soun_fx/growl2.opus", channel="sfx3", loop=False, relative_volume = 0.9)
                    $ renpy.sound.play("/audio/soun_fx/pushitin2.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                    $ renpy.sound.play("/audio/soun_fx/sexslaps1.opus", channel="sfx1", loop=False, relative_volume = 0.4)
                    scene black with flashred
                    beast"..."
                    $ renpy.sound.play("/audio/soun_fx/eye4s.opus", channel="sfx2", loop=False, relative_volume = 0.3) 
                    show kurama1 with flashred
                    show kurama1:
                        easein 2 alpha 0.0
                    beast"Yes... Yes! My time is coming..."
                    scene bg day with dissolve:
                        zoom 0.70 
                    show shina shy2 at center with dissolve
                    hin"Maybe I should check up on them after all..."
                    show shina:
                        easeout 1 xpos 1500 alpha 0.0
                    hin"I'll check in with [him_name] first..."
                    $ renpy.sound.play("/audio/soun_fx/doorknock.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                    hin"[him_name]? Can I come in...?"
                    hin"."
                    hin".."
                    hin"..."
                    hide shina
                    show shina shy2 at center with dissolve
                    hin"Hmmm... Rare for [him_name] to not be in her bedroom at this hour..."
                    show shina shy with dissolve
                    hin"I shouldn't barge in though... Maybe I'll check up on [bo_name] instead?"
                    hide shina with dissolve
                    hin"I'll ask him what happened between the two of them..."
                    $ renpy.sound.play("/audio/soun_fx/doorknock.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                    hin"[bo_name]? ...Are you inside?"
                    hin"."
                    hin".."
                    show shina concerned at center with dissolve
                    hin"...No reply from [bo_name] either?"
                    hide shina with dissolve
                    scene black with dissolve
                    hin"*Sigh*... I am not one to invade their privacy..."
                    "[hin_name]'s hand trembled as her fingers closed around the wooden knob - A strange scent wafted from beneath the door..."
                    $ renpy.sound.play("/audio/soun_fx/dooropen.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                    stop music fadeout 4
                    "She could sense something was off..."
                    hin"...But, I..." with vpunch
                    $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx2", loop=False, relative_volume = 1.2)
                    show hima_badend_hinata1 with dissolve:
                        yalign 1.0 xalign 0.5 zoom 1.05
                    $ playmusic("/audio/ost/ramennight.opus",1.1)
                    hin"I have to-"
                    $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx2", loop=False, relative_volume = 1.4)
                    hin"..."
                    $ renpy.sound.play("/audio/soun_fx/sexslaps2.opus", channel="sfx1", loop=False, relative_volume = 0.7,fadein=2)
                    $ renpy.sound.play("/audio/soun_fx/handjob4.opus", channel="sfx3", loop=False, relative_volume = 0.7,fadein=2)
                    show hima_badend_hinata1:
                        easein 0.6 yalign 0.9
                    "Wet, rhythmic sounds were the last thing [hin_name] heard before her mind shut down, unable to comprehend..."
                    hin"...B-" with vpunch
                    $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx2", loop=False, relative_volume = 1.6)
                    $ renpy.sound.play("/audio/soun_fx/spank5.opus", channel="sfxstat", loop=False, relative_volume = 1.2)
                    bo"*Groans* T-take that you bitch!" with flash
                    show hima_badend_hinata1:
                        easein 0.6 yalign 0.8
                    hin"...[bo_name_stutter]?"
                    $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx2", loop=False, relative_volume = 1.8)
                    $ renpy.sound.play("/audio/soun_fx/spank6.opus", channel="sfxstat", loop=False, relative_volume = 1.2)
                    bo"*Moans* A-and that! Yes, Y-YES! I am c-cumming again, [him_name]!" with flash
                    $ partial_name = him_name[:4] + "..." + him_name[-4:]
                    show hima_badend_hinata1:
                        easein 0.5 yalign 0.8
                    hin"[partial_name]?"
                    show hima_badend_hinata1:
                        easein 0.5 yalign 0.7
                    $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                    $ renpy.sound.play("/audio/soun_fx/spank7.opus", channel="sfxstat", loop=False, relative_volume = 1.2)
                    bo"Aaargh! *Moans* A-another load for your asshole! [him_name]..." with flash
                    show hima_badend_hinata1:
                        easein 0.5 yalign 0.2
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                    hin"*Gasps!*" with vpunch
                    $ renpy.sound.play("/audio/soun_fx/pushitin2.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                    $ renpy.sound.play("/audio/soun_fx/spank5.opus", channel="sfxstat", loop=False, relative_volume = 1.2)
                    scene black with vpunch
                    bo"*Panting* But we aren't done yet... Your cunt is up next!" with flash
                    $ renpy.sound.play("/audio/soun_fx/sexslaps3.opus", channel="sfx1", loop=False, relative_volume = 0.7,fadein=2)
                    $ renpy.sound.play("/audio/soun_fx/handjob1.opus", channel="sfx3", loop=False, relative_volume = 0.7,fadein=2)
                    "[hin_name] gasped in sheer terror, as she quickly realized, that her reality was being twisted into a horrifying nightmare..."
                    "She wanted to run, to scream, to shield her eyes, to erase the moment..."
                    show hima_badend1:
                        yalign 0.6 alpha 0.0 blur 20 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.7)*HueMatrix(0.0)
                    show hima_badend1 at vertical_pan(height=300,speed=0.5):
                        easein 10 alpha 1.0 blur 0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
                    "But she could only stand there, as the most inexplicably grotesque scene a mother could ever lay her eyes on, was being unraveled right in front of her eyes..."
                    $ renpy.sound.play("/audio/soun_fx/spank5.opus", channel="sfxstat", loop=False, relative_volume = 1.2)
                    $ renpy.sound.play("/audio/soun_fx/sexslaps3.opus", channel="sfx1", loop=False, relative_volume = 0.7,fadein=2)
                    $ renpy.sound.play("/audio/soun_fx/handjob1.opus", channel="sfx3", loop=False, relative_volume = 0.7,fadein=2)
                    scene hima_badend1 with flash:
                        yalign 0.0
                    show hima_badend1:
                        easein 5 yalign 0.6
                    "The sight of her beloved daughter, being violated by her own [him_rel_to_bo]..."
                    "[him_name]'s once vibrant face, was now a canvas of creeping terror; Her eyes hollow, rolled up and reddened from the tears shed in futile struggle..."
                    "The same struggles [hin_name] heard a little while ago, and chose to put aside, only for a moment..."
                    $ renpy.sound.play("/audio/soun_fx/spank5.opus", channel="sfxstat", loop=False, relative_volume = 1.2)
                    show hima_badend1 with flash:
                        yalign 0.6
                    bo"*Groans!* Aargh! [him_name]... There's nothing like your cunt after all!" with vpunch
                    "That moment, those few minutes were all it took for [bo_name] to reduce [him_name]'s body to what seemed like the carcass of an animal..."
                    "Bruises across her skin, from her delicate face down to her trembling toes. Scratches across her legs, arms and chest..."
                    "Her orifices filled and dripping with what was undisputedly, [bo_name]'s semen..."
                    "All signs of relentless abuse, at the hands of her [him_rel_to_bo]..."
                    show hima_badend1 with flash:
                        yalign 0.6
                    $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                    bo"E-every time I fill your cunt up, it grips me even tighter than before!" with flash
                    bo"But we aren't done just yet, you fucking whore!" with vpunch
                    $ renpy.sound.play("/audio/soun_fx/spank5.opus", channel="sfxstat", loop=False, relative_volume = 1.2)
                    $ renpy.sound.play("/audio/soun_fx/sexslaps3.opus", channel="sfx1", loop=False, relative_volume = 0.7,fadein=2)
                    $ renpy.sound.play("/audio/soun_fx/handjob1.opus", channel="sfx3", loop=False, relative_volume = 0.7,fadein=2)
                    show hima_badend2 with flash:
                        yalign 0.6
                    bo"I'll fill your holes, over and over again..." with flash
                    bo"I'll fuck you. I'll rape you! I'll breed you... then your whore [hin_rel_mother]! And then every other woman in this rotten world!" with flash
                    $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                    show screen parallax1280("hima_badend2",1,0.5) with flash
                    call showscrollingimage from _call_showscrollingimage_54
                    "[hin_name] heard and saw, every morbid word, every disturbing act of her own [hin_rel_to_bo]'s doing..."
                    "Faced with an unbearable truth, she realized she had no choice but to act..."
                    call hidescrollingimage from _call_hidescrollingimage_55
                    scene black with dissolve
                    show hima_badend_hinata1 at dizzyflash with dissolve:
                        zoom 1 xalign 0.5 yalign 0.3
                    $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx2", loop=False, relative_volume = 1.4)
                    hin"I..."
                    $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx2", loop=False, relative_volume = 1.6)
                    $ renpy.sound.play("/audio/soun_fx/spank5.opus", channel="sfxstat", loop=False, relative_volume = 1.2)
                    $ renpy.sound.play("/audio/soun_fx/sexslaps3.opus", channel="sfx1", loop=False, relative_volume = 0.7,fadein=2)
                    $ renpy.sound.play("/audio/soun_fx/handjob1.opus", channel="sfx3", loop=False, relative_volume = 0.7,fadein=2)
                    show hima_badend_hinata1 with flash:
                        zoom 1.05 xalign 0.5 yalign 0.3
                    "Her [hin_rel_to_bo]'s palms repeatedly striking her daughter's body, the wet, sickening noises of his grotesque violation of her, his depraved taunts..."
                    $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx2", loop=False, relative_volume = 1.6)
                    show hima_badend_hinata1 at dizzyflashshort with dissolve:
                        zoom 1.1 xalign 0.5 yalign 0.3
                    "A cacophony of disturbing sounds and images, whirled in [hin_name]'s mind, rendering her momentarily paralyzed..."
                    $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx2", loop=False, relative_volume = 1.8)
                    show hima_badend_hinata1 at dizzyflashshort with dissolve:
                        zoom 1.15 xalign 0.5 yalign 0.3
                    "But one sound would reverberate, over and over again..."
                    $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx2", loop=False, relative_volume = 2.0)
                    $ renpy.sound.play("/audio/soun_fx/himawari/himascreamecho.opus", channel="sfx3", loop=False, relative_volume = 0.2)
                    show hima_badend_hinata1 at dizzyflashshort with dissolve:
                        zoom 1.2 xalign 0.5 yalign 0.3
                    "Her daughter's cry for help..."
                    "The scream she blissfully neglected, mistaking it for an innocent squabble between two siblings..."
                    $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx2", loop=False, relative_volume = 2.2)
                    show hima_badend_hinata1 with dissolve:
                        zoom 1.3 xalign 0.5 yalign 0.3
                    "That same haunting scream kept repeating a million times - 'If only... If only I acted sooner' [hin_name] lamented..."
                    "Something was brewing inside [hin_name]. An emotional storm, a seething emotion..."
                    $ renpy.sound.play("/audio/soun_fx/wakeup.opus", channel="sfx3", loop=False, relative_volume = 1.2)
                    with Shake((0, 0, 0, 0), 2, dist=10, peak_time=1.4, smoothness=50)
                    scene hima_badend_hinata2 with flash:
                        yalign 1.0
                    show hima_badend_hinata2:
                        easein 6 yalign 0.1
                    "A dark mix of self-loathing, contempt and disdain..."
                    "First for herself, then for her [hin_rel_to_bo], then for the cruel world..."
                    scene hinaq1bg 2
                    show shina horrifiedt at center:
                        zoom 0.6
                    with dissolve
                    hin"I-i-i have to..."
                    hin"T-there's no o-other w-way!"
                    show shina:
                        easeout 3 xpos -500 alpha 0.0
                    hin"I h-have to!" with vpunch
                    scene black with dissolve
                    $ renpy.sound.play("/audio/soun_fx/sexslaps3.opus", channel="sfx1", loop=False, relative_volume = 0.7,fadein=2)
                    $ renpy.sound.play("/audio/soun_fx/handjob1.opus", channel="sfx3", loop=False, relative_volume = 0.7,fadein=2)
                    show hima_badend2:
                        yalign 0.6 alpha 0.0 blur 20
                    show hima_badend2:
                        easein 5 alpha 1.0 blur 0
                    "[bo_name], absorbed by his never-ending lust to fornicate and impregnate his [him_rel], had yet to realize that his [hin_rel_mother] bore witness to his vile acts..."
                    $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                    show internal_vagcum 3:
                        zoom 0.5 xalign 1.0 yalign 0.0
                    bo"T-this is the... t-tenth time I came in you, [him_name]!" with flash
                    $ renpy.sound.play("/audio/soun_fx/spank5.opus", channel="sfxstat", loop=False, relative_volume = 1.2)
                    bo"I can sense your womb warming up to me! That was the one that'll get you..." with flash
                    $ renpy.sound.play("/audio/soun_fx/fleshpierce.opus", channel="sfxstat", loop=False, relative_volume = 1.2)
                    scene black with flashred
                    $ renpy.sound.play("/audio/soun_fx/heartbeatdead.opus", channel="sfx3", loop=False, relative_volume = 1.2)
                    $ renpy.sound.stop(channel="sfx1")
                    stop music fadeout 1
                    bo"P..." with vpunch
                    scene black with vpunch
                    bo"P-preg...na... h-huh?"
                    "You glanced down only to see a bloodied hand erupting straight through your chest..."
                    $ renpy.sound.play("/audio/soun_fx/intro/bodythud.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                    "*Body thuds*!" with vpunch
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatacrying.opus", channel="sfx1", loop=False, relative_volume = 0.6)
                    $ playmusic("/audio/ost/loneliness.opus",1.1)
                    hin"*Whimpers*..."
                    "A child's life, to spare another's..."
                    "That was the decision [hin_name] was forced to make..."
                    "She gathered all the chakra she could muster into the tip of her fingers. With tears streaming down her face, she struck - a single lethal thrust through your heart. An instant-kill technique passed down the Hyuuga bloodline."
                    "She took her battered daughter and caressed her in her arms..."
                    "Your lifeless husk laid right next to them in a pool of your own blood..."
                    "."
                    ".."
                    "..."
                    "Hours crawled by before [him_name] awoken in the infirmary, her mother watching over her with haunted eyes..."
                    "But fate wasn't finished with its cruel twist..."
                    show himapregnant1 with dissolve:
                        yalign 1.0
                    show himapregnant1:
                        easein 3 yalign 0.0
                    "Within days, [him_name]'s body began changing in ways that defied nature itself. Her belly swelled with impossible speed, harboring something that shouldn't exist..."
                    show himapregnant2 with dissolve:
                        yalign 1.0
                    show himapregnant2:
                        easein 3 yalign 0.0
                    "One month. That's all it took for the embryo inside her to fully form - an inexplicable acceleration of life that no human was meant to endure."
                    "[him_name]'s young body buckled under the supernatural strain..."
                    show himapregnant2 with dissolve:
                        zoom 1.3 xalign 1.0 yalign 0.0
                    "Her screams echoed through the halls day and night, her agony growing until finally..."
                    show himapregnant2_1 with dissolve:
                        zoom 1.6 xalign 1.0 yalign 0.0
                    $ renpy.sound.play("/audio/soun_fx/devilbaby.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                    scene black with dissolve
                    "A baby boy emerged into the world, but not without a price. His first cry was an unholy sound. As he drew his first breath, [him_name] drew her last..."
                    "[hin_name], broken by the weight of her choices, vanished into her grief, never to be seen in the village again."
                    "..."
                    "The infant, left to the sterile care of the infirmary, carried an aura that made the nurses uneasy."
                    $ renpy.sound.play("/audio/soun_fx/ominous_sound.opus", channel="sfx2", loop=False, relative_volume = 0.9)
                    "It wasn't too long after, that the child was lost..."
                    "Thought to have been stolen, or killed at the hands of unknown instigators..."
                    $ renpy.sound.play("/audio/soun_fx/bassstart.opus", channel="sfx1", loop=False, relative_volume = 1, fadein = 0.05)
                    queue sfx1 ("audio/soun_fx/introbass3.opus") volume 0.4 loop
                    show disclameimerintro with Fade(0.5,0,3):
                        zoom 2.0 xalign 0.6 yalign 0.3
                    show disclameimerintro:
                        easeout 30 subpixel True zoom 1.0 xalign 0.492 yalign 0.3
                    pause 2
                    "Years later, when the Shinobi world lay in ruins, survivors whispered of a child with eyes like blood and the spirit of a fox - a harbinger of their destruction..."
                    $ renpy.end_replay()
                    menu:
                        "Years later, when the Shinobi world lay in ruins, survivors whispered of a child with eyes like blood and the spirit of a fox - a harbinger of their destruction..."
                        "Return to reality...":
                            dev"You died, your [him_rel] died, your [hin_rel]... probably died. The shinobi world is no more, but..."
                            dev"At least you fucked [him_name]! :)"
                            dev"Please stop asking 'when can I sex her!' or I'll write even more depressing shit!"
                            dev"But don't worry, this isn't canon..."
                            dev"Look, I'll show you a magic trick!"
                            $ percentage = 50
                            $ playmusic("audio/ost/house2.opus",0.6)
                            $ renpy.sound.play("/audio/soun_fx/wakeup.opus", channel="sfx1", loop=False, relative_volume = 1.2)
                            with Shake((0, 0, 0, 0), 2, dist=10, peak_time=1.4, smoothness=50)
                            scene h_wrestle1_ass3_grope4 with flash
                            show screen scrollable_scene(initial_ypos=1.0,imagetoadd="h_wrestle1_ass3_grope4", facetoadd="h_wrestle1_assface1") with flash
                            bot"H-huh... Déjà vu?"
                            jump h_wrestlefinalmenu

                        "Exit game! (Lord knows you need it)":
                            $ renpy.quit()


                    jump h_wrestlefinalmenu
                
            
        "Grope her!":
            hide screen scrollable_scene
            show screen scrollable_scene(initial_ypos=0.0,imagetoadd="h_wrestle1_ass3", facetoadd="h_wrestle1_assface1")
            with dissolve
            bot"Hehehe! With her looking like that..."
            hide screen scrollable_scene
            hide screen scrollingtext
            show screen scrollable_scene(initial_ypos=1.0,imagetoadd="h_wrestle1_ass3", facetoadd="h_wrestle1_assface1")
            with dissolve
            bot"Surely she wouldn't mind if i..."
            hide screen scrollingtext
            show screen scrollable_scene(initial_ypos=1.0,imagetoadd="h_wrestle1_ass3_grope1", facetoadd="h_wrestle1_assface1")
            with dissolve
            bot"...!" with vpunch
            bo"I gotta give it to you, all that exercising surely helped develop this area down here..."
            show hatred_choice onlayer screens with dissolve
            $ config.menu_include_disabled = False
            $ config.menu_include_disabled = True
            menu h_wrestlefinalmenu2:
                bo"I gotta give it to you, all that exercising surely helped develop this area down here..."
                "Play with her ass" if percentage <80:
                    hide screen scrollable_scene
                    show screen scrollable_scene(initial_ypos=1.0,imagetoadd="wrestle_gropeass", facetoadd="h_wrestle1_assface1")
                    with dissolve
                    $ config.menu_include_disabled = False
                    $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    bo"That's a firm ass you have on you..."
                    bot"My god! To think my [him_rel] had an ass like that on her... I had no idea!"
                    call increaselust(10) from _call_increaselust_94
                    bot"F-fuck! I am getting the urge to shove something else in there..."
                    hide screen scrollable_scene
                    show screen scrollable_scene(initial_ypos=0.0,imagetoadd="wrestle_gropeass", facetoadd="h_wrestle1_assface1")
                    with dissolve
                    $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    him"*Gasping for air*... W-what the..."
                    hide screen scrollable_scene
                    show screen scrollable_scene(initial_ypos=0.0,imagetoadd="wrestle_gropeass", facetoadd="h_wrestle1_assface2")
                    with dissolve
                    $ renpy.sound.play("/audio/soun_fx/himawari/kyaa.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                    him"*Gasp*!" with vpunch
                    hide screen scrollable_scene
                    scene black with vpunch
                    bo"Ow-ouch!" with vpunch
                    "[him_name] regained her awareness... In an instant, she raised her heel and kicked you in the balls..."
                    him"MOOOOOOM!!!" with vpunch

                "Spank her" if percentage <80:
                    bo"That's a firm ass you have on you..."
                    $ config.menu_include_disabled = False
                    hide screen scrollable_scene
                    show h_wrestle1_ass3_grope3:
                        yalign 1.0
                    with dissolve
                    bo"Too bad your training didn't help develop your physical abilities..."
                    show h_wrestle_spank with moveinleft
                    $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                    with vpunch
                    hide h_wrestle_spank
                    show h_wrestle1_ass3_grope4 
                    with dissolve
                    bo"...Bitch!"
                    hide screen scrollable_scene
                    show screen scrollable_scene(initial_ypos=0.0,imagetoadd="h_wrestle1_ass3_grope4", facetoadd="h_wrestle1_assface2")
                    with dissolve
                    $ renpy.sound.play("/audio/soun_fx/himawari/kyaa.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                    him"*Gasp*!" with vpunch
                    hide screen scrollable_scene
                    scene black with vpunch
                    bo"Ow-ouch!" with vpunch
                    "[him_name] regained her awareness... In an instant, she raised her heel and kicked you in the balls..."
                    him"MOOOOOOM!!!" with vpunch

                "{color=[hatredcolor]}!?! *The beast rumbles...*{/color}" (secrethatred = True) if percentage >=80:
                    $ config.menu_include_disabled = False

                    if v17_update == True:
                        pass
                    else:
                        $ notification("Exclusive supporters scene")
                    jump hima_gameover_wrestling
                    
                
                
        
 

    hide screen scrollable_scene
    show int3 with dissolve
    bo"N-not... fair...! *Wheezing*"
    show int3_1 with dissolve
    if quest_him.is_state("him1H_1", "pending") and not _in_replay:
        $ quest_him.change_quest_title("him1H_1",f"Wrestle with {him_name} and serve her a 'punishment'")
        $ notification (f"{him_name} Hatred objective completed")
        $ quest_him.check("him1H_1", "completed")
    him"Hands off of me, loser! I am telling [hin_rel] you... y-you...!" with vpunch
    bo"You'll tell her w-what... *Wheezing* T-that w-was... y-your punishment! You f-freaking brat..."
    $ change_music_volume(0.5, 2.0)
    "[him_name] walked all over you and turned down your music..."
    call changeObedience("Himawari", 1) from _call_changeObedience_81
    him"Y-you went way too far! Y-you t-touched my... Freaking p-perv!"
    bo"Y-you had the c-chance to give up e-earlier... *Wheezing*..."
    bo"...Y-you B-bitch! *Painful groans* Aw-w..."
    $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.8)
    him"Hmph!"
    scene black
    $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx2", loop=False, relative_volume = 0.7)
    call changeRespect("Himawari", -1) from _call_changeRespect_121
    him"...Better luck next time, weakling!" with vpunch
    bo"*Groans* Next time... I'll g-get you for sure..."
    $ renpy.end_replay()
    $ d_wrestle3_stomach_finishingblow = True
    $ hima_wrestling_won = True
    jump action_taken

label hate_wrestle_fishhook:
   
    hide screen scrollable_scene
    hide screen scrollingtext
    show h_wrestle2_1:
        zoom 1.2 yalign 0.0 xalign 0.5
    with dissolve
    bo"What's up with that stupid look on your face, [him_name]..."
    scene black with dissolve
    him"*Exhausted breathing* Y-you..."
    bo"I thought you were strong..."
    show h_wrestle5 with dissolve
    bo"Yet here you are looking like a stupid little piggie!" with vpunch
    call changeHatred(1) from _call_changeHatred_104
    bo"How's that, you bitch..." with vpunch
    bo"The same [him_rel_to_bo] you so often like to look down upon now has you bound in a fish hook and there's nothing you can do about it!"
    him"Awe ou... uin uid!!"
    show h_wrestle5_1 with dissolve:
        zoom 1.2 xalign 1.0 yalign 1.0
    "You pushed your fingers deeper into her mouth and pulled even harder..." with vpunch
    "[him_name]'s eyes were tearing up, her saliva drooling down your fingers..."
    "All she could do was mutter a series of incomprehensible vowels"
    him"I ieh ow ihner ohh!! Aaaa!!" with vpunch
    bo"W-what's that? You are babbling like a baby!"
    bo"...Have something to say now little piggie?"
    $ renpy.sound.play("/audio/soun_fx/himawari/kyaa.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    scene black
    him"*Gasp*!" with vpunch
    hide screen scrollable_scene
    bo"Ow-ouch!" with vpunch
    "[him_name] bit down on your fingers! You pulled back and in an instant, she raised her heel and kicked you in the balls..."
    him"MOOOOOOM!!!" with vpunch
    
    hide screen scrollable_scene
    show int3 with dissolve
    bo"N-not... fair...! *Wheezing*"
    show int3_1 with dissolve
    $ renpy.end_replay()
    if quest_him.is_state("him1H_1", "pending"):
        $ quest_him.change_quest_title("him1H_1",f"Wrestle with {him_name} and serve her a 'punishment'")
        $ notification (f"{him_name} Hatred objective completed")
        $ quest_him.check("him1H_1", "completed")
    him"Hands off of me, loser! I am telling [hin_rel] you... y-you...!" with vpunch
    bo"You'll tell her w-what... *Wheezing* T-that w-was... y-your punishment! You f-freaking brat..."
    $ change_music_volume(0.5, 2.0)
    "[him_name] walked all over you and turned down your music..."
    call changeObedience("Himawari", 1) from _call_changeObedience_82
    him"Y-you went way too far! Y-you put y-your d-dirty hands in m-my mouth! Freaking p-perv!"
    bo"Y-you had the c-chance to give up e-earlier... *Wheezing*..."
    bo"...Y-you B-bitch! *Painful groans* Aw-w..."
    $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.8)
    him"Hmph!"
    scene black
    $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx2", loop=False, relative_volume = 0.7)
    call changeRespect("Himawari", -1) from _call_changeRespect_122
    him"...Better luck next time, weakling!" with vpunch
    bo"*Groans* Next time... I'll g-get you for sure..."
    $ d_wrestle3_stomach_finishingblow = True
    $ hima_wrestling_won = True
    jump action_taken



    $ renpy.sound.play("audio/soun_fx/attributeslost.opus", channel="sfxstat", loop=False, relative_volume=1)
    hide screen scrollingtext
    show screen scrollingtext(f"Strength check{{color=#FF0000}} failed{{/color}}")
    show int2_tr at smallshake
    $ renpy.pause(0.6, hard=True)
    "You tried to push [him_name] away, but you slipped up and..."
    hide screen scrollable_scene
    scene black
    bo"Aw-Ouch!" with vpunch
    show int3 with dissolve
    "...She kicked you in the balls!"
    bo"N-not... fair...! *Wheezing*"
    show int3_1 with dissolve
    him"Hands off of me, loser!" with vpunch
    if pullpants_d_wrestle3_pants == True:
        him"I am also telling [hin_rel] you tried to pull my shorts down!"
    $ change_music_volume(0.5, 2.0)
    "[him_name] walked all over you and turned down your music..."
    him"And stay down!"
    bo"Y-you... B-bitch! *Painful groans* Aw-w..."
    $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.8)
    him"Hmph!"
    scene black
    $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx2", loop=False, relative_volume = 0.7)
    call changeRespect("Himawari", -1) from _call_changeRespect_123
    him"...Better luck next time, weakling! Teehee!" with vpunch
    bo"*Groans* Next time... I'll g-get you for sure..."
    jump action_taken




label hate_wrestle_lowerpants:
    hide screen scrollable_scene
    hide screen scrollingtext
    show screen scrollable_scene(initial_ypos=1.0,imagetoadd="h_wrestle1_ass2", facetoadd="h_wrestle1_face")
    with dissolve
    him"*Gasp* H-hey! S-stop-"
    bo"Consider this..."
    hide screen scrollable_scene
    hide screen scrollingtext
    show screen scrollable_scene(initial_ypos=1.0,imagetoadd="h_wrestle1_ass3")
    with dissolve
    bo"...Your punishment!" with vpunch
    bo"N-nice matching panties, you bitch!"
    him"H-HEY! I am telling [hin_rel]!"
    call increaselust(5) from _call_increaselust_95
    bot"*Gulp* What an ass!"
    bo"A little disciplinary spanking never hurt anyone, [hin_rel] would concur!"
    him"I s-said stop, you freaking pervert!" with vpunch
    "You raised your hand in preparation of serving some 'disciplinary' spanking, but..."
    hide screen scrollable_scene
    scene black
    call changeRespect("Himawari", -1) from _call_changeRespect_124
    bo"Aww-ouch!" with vpunch
    him"You are j-just looking for ways to touch me i-inappropriately, aren't you... you weirdo!" with vpunch
    "[him_name] recovered just in time to suddenly raise her heel and..."
    jump l0_opportunity2_lose_jumpbed








#
#
#
#dom
#
#

label d_pinarms1:
    hide screen scrollable_scene
    hide screen scrollingtext
    show screen scrollable_scene(initial_ypos=0.0,imagetoadd="wrestle1_1")
    with dissolve
    him"L-let me go.. Mhh! Grrrr!"
    hide screen scrollable_scene
    show screen scrollable_scene(initial_ypos=0.0,imagetoadd="wrestle1_3")
    with dissolve
    bo"I don't think so!"
    him"I said..."
    $ renpy.sound.play("/audio/soun_fx/countdown.opus", channel="sfx2", loop=False, relative_volume = 0.9)
    hide screen scrollable_scene
    show screen scrollingtext("Let... me... go!")
    show wrestle1_3:
        yalign 0.0
    show halfblack
    with dissolve
    pause 1
    hide halfblack with Dissolve(3)
    show screen scrollable_scene(initial_ypos=0.0,imagetoadd="wrestle1_3")

    if is_opportunity_unlocked("l0_opportunity3", strength):
        call screen strength_minigame2("l0_opportunity3_win", "l0_opportunity2_lose", "wrestle1_3", 0.0,False,strengthlevel)
    else:
        call screen strength_minigame2("l0_opportunity3_win", "l0_opportunity2_lose", "wrestle1_3", 0.0,True,strengthlevel)
            
    label l0_opportunity3_win:
    hide screen scrollable_scene
    show screen scrollable_scene(initial_ypos=0.0,imagetoadd="wrestle1_2")
    with dissolve
    bo"Admit your defeat!"
    him"N-never! Mhh-hg! Grr!"
    hide screen scrollable_scene
    with dissolve
    bo"Then you give me no other choice but to use your weakness against you!"
    him"What would you know about any weakness of mine, you imbecile. Get off of me already!"
    bo"Hehe..."
    show screen scrollable_scene(initial_ypos=0.0,bgtoadd=None, imagetoadd="wrestle1_2", facetoadd=None,mask1="wrestle1_arms", hovertext1="Keep holding her arms", jump1="wrestle1_arms_label2", mask2="wrestle1_face", hovertext2="Abuse her 'weakness'", jump2="wrestle1_face_label2", mask3="wrestle1_stomach", hovertext3="Abuse her weakness!", jump3="wrestle1_stomach_label2") with dissolve
    show screen scrollingtext("Expose her weakness!")
    $ ui.interact()




label d_stomach1:
    hide screen scrollable_scene
    show wrestle1_tickle1
    with dissolve
    pause 0.2
    show screen scrollable_scene(initial_ypos=0.0,imagetoadd="wrestle1_tickle1") with dissolve
    him"Where do you t-think you are putting your hands at!"
    hide screen scrollable_scene
    show screen scrollable_scene(initial_ypos=1.0,imagetoadd="wrestle1_stomachfail")
    with dissolve
    bo"I am simply holding you down! Too weak to escape, aren't you!?"
    him"Get off of me, y-you monkey!"
    call increaselust(5) from _call_increaselust_96
    "You were strangely aroused by how handsy the situation got. In your moment of distraction, you unintentionally left an opening for [him_name] to capitilize on..."
    bo"Hehe... You have nowhere to go now!" with vpunch
    him"You are so incredibly stupid, it's not even funny..."
    hide screen scrollable_scene
    scene black
    him"My hands are free idiot!" with vpunch
    "She punched you in the face and..."
    jump l0_opportunity2_lose_jumpbed
    
label wrestle1_arms_label2: #done
    hide screen scrollable_scene
    hide screen scrollingtext
    show screen scrollable_scene(initial_ypos=0.0,imagetoadd="wrestle1_3")
    with dissolve
    him"Stop p-pressing so hard! Mhh-grr!"
    bo"You sure you don't wanna give up? I'd hate to use your weakness against you..."
    him"I know you are bluffing, stupid... Now let me go!"
    bo"Hehe..."
    hide screen scrollable_scene
    show screen scrollable_scene(initial_ypos=0.0,bgtoadd=None, imagetoadd="wrestle1_2", facetoadd=None,mask1="wrestle1_arms", hovertext1="Keep holding her arms", jump1="wrestle1_arms_label2", mask2="wrestle1_face", hovertext2="Abuse her 'weakness'", jump2="wrestle1_face_label2", mask3="wrestle1_stomach", hovertext3="Abuse her weakness!", jump3="wrestle1_stomach_label2")
    with dissolve

    show screen scrollingtext("Expose her weakness!")
    $ ui.interact()

label wrestle1_face_label2: #face
    hide screen scrollable_scene
    hide screen scrollingtext
    show screen scrollable_scene(initial_ypos=0.0,imagetoadd="wrestle1_1")
    with dissolve
    him"L-let me go! Othewise I am telling [hin_rel]..."
    bo"Not until you admit your defeat!"
    bo"Besides, you'll tell [hin_rel] what, that you tried to fight me and order me around?"
    him"Grrr!"
    bo"Come on, just say that I am stronger, say that I am better than you!"
    him"Never!"
    bo"Then you leave me no choice..."
    hide screen scrollable_scene
    show screen scrollable_scene(initial_ypos=0.0,imagetoadd="wrestle1_mouth1")
    with dissolve
    him"Shtop it! Wva aa you-!?" with vpunch
    hide screen scrollable_scene
    show screen scrollable_scene(initial_ypos=0.0,imagetoadd="wrestle_mouthanim")
    with dissolve
    bo"You always hated when other people touched your face or pinched your cheeks..."
    bo"Next time you come in here making demands, I am thinking I have a nose hook ready for you..."
    him"Pfugg -ou, i-iot! I shoul -ite orh fineh offh!" with vpunch
    bo"Or maybe I should... Did you know fish-hooking is prohibited in combat sports? Apparently it can lead to severe injuries...!"
    bo"I am kidding of course, I would never hurt you... I think!"
    "You inserted your thumb in [him_name]'s orifice and kept stretching her mouth wide open as you kept throwing playful, but provoking insults at her..."
    "[him_name] was equal parts annoyed and embarassed after being overpowered by you. Her expression, along with her now flushed face betrayed her feeble attempts to maintain any semblance of superiority, but..."
    "You accidentely gave an opening to her by freeing her arms..."
    hide screen scrollable_scene
    scene black
    "[him_name] bit down on your finger!" with vpunch
    bo"Argh! You b-bitch-" with vpunch
    him"W-why would you ever put your dirty hands on me like that, you freaking imbecile!"
    call changeRespect("Himawari", -2) from _call_changeRespect_125
    "She pushed you away and..."
    him"Take this! you perverted idiot!" with vpunch
    jump l0_opportunity2_lose_jumpbed










    hide screen scrollable_scene
    show screen scrollable_scene(initial_ypos=0.0,bgtoadd=None, imagetoadd="wrestle1_2", facetoadd=None,mask1="wrestle1_arms", hovertext1="Keep holding her arms", jump1="wrestle1_arms_label2", mask2="wrestle1_face", hovertext2="Abuse her 'weakness'", jump2="wrestle1_face_label2", mask3="wrestle1_stomach", hovertext3="Abuse her weakness!", jump3="wrestle1_stomach_label2")
    with dissolve
    show screen scrollingtext("Expose her weakness!")
    $ ui.interact()

label wrestle1_stomach_label2: #tickle
    hide screen scrollable_scene
    hide screen scrollingtext
    show screen scrollable_scene(initial_ypos=1.0,imagetoadd="wrestle1_tickle1")
    with dissolve
    him"W-what do you think you are d-doing!"
    bo"You won't surrender, so..."
    bo"It's time I resort to other measures... I am afraid I'll have to use your weakness against you!"
    "You grinned as you playfully raised [him_name]'s top just enough to expose her stomach..."
    "She was still oblivious to what your plan was, but the constant wiggle of your fingers across her ribs would quickly betray your plans..."
    him"N-no... Not that! Heh-he...!"
    hide screen scrollable_scene
    show screen scrollable_scene(initial_ypos=1.0,imagetoadd="wrestle1_stomachfail")
    with dissolve
    bo"Ooooh? My dear [him_rel]... Is that panic I sense settling in?"
    him"Stop it you-!"
    hide screen scrollable_scene
    show screen scrollable_scene(initial_ypos=0.0,imagetoadd="wrestle1_tickle2")
    with dissolve
    "Before she could even mutter her protests, you started running your fingers across her stomach..."
    him"Heh-he-.. S-stop! HAAA-HA!"
    hide screen scrollable_scene
    show screen scrollable_scene(initial_ypos=1.0,imagetoadd="wrestle1_tickle2")
    with dissolve
    bo"You think I'd forget how ticklish you are?"
    bo"This is your true weakness!"
    him"S-stop! *Giggles*"
    "[him_name] gasped for air between her fit of uncontrollable giggles..."
    him"Y-you are the absolute worst! He-heh-haha! S-stop!"
    bo"I am not gonna let up now! You'll pay for your behaviour..."
    "Your constantly dancing fingers across her navel were enough to paralyze [him_name]..."
    "She tried to wiggle backwards to avoid your tickling..."





label d_wrestle2_start:
    hide screen scrollable_scene
    hide screen scrollingtext
    show screen scrollable_scene(initial_ypos=1.0,imagetoadd="wrestle2_grope1")
    with dissolve
    "But in doing so, she only gave you more room to work with..."
    "You eased up, giving her a small moment of reprieve..."
    "Despite her protests, her helpless giggles and attempts to squirm away betrayed her helplesness..."
    him"I h-hate you... s-stupid I-idiot!"
    bo"Hehe! Your face is turning red, little sis..."
    him"This isn't funny, get off me already!"
    hide screen scrollable_scene
    show screen scrollable_scene(initial_ypos=0.0,bgtoadd=None, imagetoadd="wrestle2", facetoadd=None,mask1="wrestle2_armpits", hovertext1="Finish her off!", jump1="d_wrestle2_armpits", mask2="wrestle2_face", hovertext2="You look flustered!", jump2="d_wrestle2_face", mask3="wrestle2_stomach", hovertext3="Raise her top", jump3="d_wrestle2_stomach")
    with dissolve

    show screen scrollingtext("Expose her true weakness!")
    $ ui.interact()
        






label d_wrestle2_armpits:
    hide screen scrollable_scene
    hide screen scrollingtext
    show screen scrollable_scene(initial_ypos=0.0,imagetoadd="wrestle2_armpits1")
    with dissolve
    default him_ticklearmpits = False
    $ him_ticklearmpits = True
    bo"Your real weakness has always been...-"
    him"Don't even think about-"
    hide screen scrollable_scene
    hide screen scrollingtext
    show screen scrollable_scene(initial_ypos=0.0,imagetoadd="wrestle_armpitsanim", facetoadd="wrestle2_face1")
    with dissolve
    him"Heh-he-eh.. Ha-HAHA!! S-stop!! Hehe-heHA-HA!" with vpunch
    "[him_name] burst into a spur of uncontrollable giggles. You kept mercilessly running your fingers across her armpits..."
    bo"What's that? I can't hear anything you are saying! You sure you don't wanna surrender yet?"
    him"Heh-he-eh... P-please... Ha-HAHA!! S-stop!! Hehe-heHA-HA! I surren- hahaha!" with vpunch
    bo"You... what?"
    him" P-please... Ha-hehe-he!! S-stop!! I surrender-haha-ha!" with vpunch
    hide screen scrollable_scene
    show screen scrollable_scene(initial_ypos=0.0,imagetoadd="wrestle2_armpits2", facetoadd="wrestle2_face2")
    with dissolve
    "You stopped tickling for a moment..."
    bo"Did I hear you say what I think you did..."
    him"*Heavy breathing* You...  asshole..."
    bo"Come on [him_name], say the words... Say 'I admit defeat my dear [him_rel_to_bo]! I am sorry for disrespecting you and making demands!'!"
    him"I... *Heavy breathing*"
    "[him_name] was still trying to catch her breath after enduring your excessive tickling..."


    hide screen scrollable_scene
    show screen scrollable_scene(initial_ypos=0.0,bgtoadd=None, imagetoadd="wrestle2_armpits2", facetoadd="wrestle2_face2",mask2="wrestle2_face", hovertext2="You look flustered!", jump2="d_wrestle2_face", mask3="wrestle2_stomach", hovertext3="Raise her top!", jump3="d_wrestle2_stomach")
    with dissolve
    show screen scrollingtext("Expose her true weakness!")
    $ ui.interact()

label d_wrestle2_stomach:
    hide screen scrollable_scene
    hide screen scrollingtext
    if him_ticklearmpits == True:
        show screen scrollable_scene(initial_ypos=1.0,imagetoadd="wrestle2_grope1", facetoadd="wrestle2_face2")
        with dissolve
        him"O-okay okay! *Heavy breathing* You win..."
        show screen scrollable_scene(initial_ypos=1.0,imagetoadd="wrestle2_grope2", facetoadd="wrestle2_face2")
        with dissolve
        bo"I am not hearing what I want to hear..."
        "You pressed on in her moment of weakness and once again started tickling her stomach!"
        "But this time, you opportunistically attempted to sneakily raise her top..."
        him"I... Hehe-heha- said... ha-ahahaha!" with vpunch
        bot"Now's my chance!" with vpunch
        show screen scrollable_scene(initial_ypos=1.0,imagetoadd="wrestle2_grope3", facetoadd="wrestle2_face2")
        with dissolve
        him"H-hey... Hehe-heha-ha-ahahaha!" with vpunch
        "[him_name] kept trying to wiggle away from you to escape your tickling, but in doing so..."
        hide screen scrollable_scene
        show screen scrollable_scene(initial_ypos=0.2,bgtoadd="bg wrestle", imagetoadd="wrestle3")
        with dissolve
        "Her top kept sliding upwards, allowing you a view of her fully exposed stomach..."
        bot"*Gulp* I can almost see her boobs!"
        him"Hehe-he... *Heavy breathing* No m-more, please..."
        hide screen scrollable_scene
        show screen scrollable_scene(testfix_xalign=0.0,initial_ypos=0.4,bgtoadd="bg wrestle", imagetoadd="wrestle3", facetoadd=None,mask2="wrestle3_stomach", hovertext2="Deliver the finishing blow!", jump2="d_wrestle3_stomach", mask3="wrestle3_pants", hovertext3="Lower her pants!", jump3="d_wrestle3_pants")
        show screen scrollingtext("Deliver the finishing blow!")
        with dissolve
        $ ui.interact()


        
    else:
        show wrestle2_grope1:
            yalign 1.0
        with dissolve
        bo"I bet you are real ticklish up here..."
        show screen scrollable_scene(initial_ypos=0.0,imagetoadd="wrestle2_grope1", facetoadd="wrestle2_face2")
        with dissolve
        him"W-what do you think you are doing!"
        bot"It's about time I check what's under here!"
        hide screen scrollable_scene
        show screen scrollable_scene(initial_ypos=1.0,imagetoadd="wrestle2_grope2", facetoadd="wrestle2_face2")
        with dissolve
        bo"What do you mean, I am just tickling you!"
        him"L-let me go! Othewise I am telling [hin_rel]..."
        show screen scrollable_scene(initial_ypos=1.0,imagetoadd="wrestle2_grope3", facetoadd="wrestle2_face2")
        with dissolve
        him"H-hey!" with vpunch
        bot"...Just a little bit more!"
        bo"You'll tell [hin_rel] what, that you tried to fight me and order me around?"
        hide screen scrollable_scene
        scene black
        "You left an opening for [him_name] to capitalize on..." with vpunch
        bo"Argh! You b-bitch-" with vpunch
        him"W-why would you ever put your dirty hands on me like that, you freaking imbecile!"
        call changeRespect("Himawari", -2) from _call_changeRespect_126
        "She pushed you away and..."
        him"Take this! you perverted idiot!" with vpunch
        jump l0_opportunity2_lose_jumpbed

label d_wrestle2_face:
    hide screen scrollingtext
    if him_ticklearmpits == True:
        hide screen scrollable_scene
        show screen scrollable_scene(initial_ypos=0.0,imagetoadd="wrestle2_armpits2",facetoadd="wrestle2_face2")
        with dissolve
        bot"That stupid look on her face... I got her cornered!"
        bot"Now would be the time to make a risky move, maybe I can..."
        bo"Looks like you are having trouble breathing, you sure you don't wanna say the words?"
        him"I... *Heavy breathing*"
        hide screen scrollable_scene
        show screen scrollable_scene(initial_ypos=0.0,bgtoadd=None, imagetoadd="wrestle2_armpits2", facetoadd="wrestle2_face2",mask2="wrestle2_face", hovertext2="You look flustered!", jump2="d_wrestle2_face", mask3="wrestle2_stomach", hovertext3="Raise her top!", jump3="d_wrestle2_stomach")
        with dissolve
        show screen scrollingtext("Expose her true weakness!")
        $ ui.interact()
    else:  
        hide screen scrollable_scene
        show screen scrollable_scene(initial_ypos=0.0,imagetoadd="wrestle2")
        with dissolve 
        bo"What's up with your face [him_name]!"
        bo"You look like you are running into some trouble, hehe! Wanna surrender now?"
        hide screen scrollable_scene
        show screen scrollable_scene(initial_ypos=0.0,imagetoadd="wrestle2",facetoadd="wrestle2_face3")
        with dissolve 
        him"Hnnng! Mhhhhmmm! Move your dirty s-sweaty bum off me, you weirdo!"
        "[him_name] made a few feeble attempts to wiggle away from you, but your body weight proved to be too much for her to push off. You held her in place by locking her legs beneath your crotch..."
        bo"Haaaha! Still clinging on to your silly, futile insults..."
        bo"I am afraid you leave me no choice but to use my secret weapon... It's time I reveal your true weakness!"
        hide screen scrollable_scene
        show screen scrollable_scene(initial_ypos=0.0,imagetoadd="wrestle2")
        with dissolve 
        him"Y-you are not thinking of... that!? I'll punch you in the face!"
        hide screen scrollable_scene
        show screen scrollable_scene(initial_ypos=0.0,bgtoadd=None, imagetoadd="wrestle2", facetoadd=None,mask1="wrestle2_armpits", hovertext1="Finish her off!", jump1="d_wrestle2_armpits", mask2="wrestle2_face", hovertext2="You look flustered!", jump2="d_wrestle2_face", mask3="wrestle2_stomach", hovertext3="Raise her top", jump3="d_wrestle2_stomach")
        with dissolve
        $ ui.interact()



label d_wrestle3_stomach:
    default d_wrestle3_stomach_finishingblow = False
    $ d_wrestle3_stomach_finishingblow = True
    $ hima_wrestling_won = True
    hide screen scrollable_scene
    show screen scrollable_scene(initial_ypos=0.5,bgtoadd="bg wrestle",imagetoadd="wrestle3_grope1", facetoadd="wrestle3_face1")
    with dissolve
    bo"And now for my ultimate finishing move..."
    hide screen scrollable_scene
    show screen scrollable_scene(initial_ypos=0.2,bgtoadd="bg wrestle",imagetoadd="wrestle_stomachanim", facetoadd="wrestle3_face3")
    with dissolve
    $ renpy.sound.play("/audio/soun_fx/tickle1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    bo"Hissatsu! Ultimate belly tickling technique!" with vpunch
    him"N-no, no-nononono! Heh-eh-eeh..."
    him"HEH-HE-HE-HE! HA-HAHAA-AH! P-please! HeHEHEhe-"
    bo"How's this, you brat..."
    him"Hehehe-heheh! E-enough-ha-haha!"
    bo"Surrender now! Submit to my prowess! Hehehe..."
    him"I surrend-eheh! I surrender! Hahah-ha!"
    bot"...Now's my chance!"
    hide screen scrollable_scene
    show screen scrollable_scene(testfix_xalign=0.0,initial_ypos=0.0,bgtoadd="bg wrestle", imagetoadd="wrestle_stomachanim", facetoadd="wrestle3_face3",mask1="wrestle3_grope", hovertext1="Try to grope her tits!", jump1="d_wrestle3_grope", mask2="wrestle3_pants", hovertext2="Pull her pants down!", jump2="d_wrestle3_pants")
    with dissolve
    $ ui.interact()


label d_wrestle3_pants:
    default pullpants_d_wrestle3_pants = False
    $ pullpants_d_wrestle3_pants = True
    

    if d_wrestle3_stomach_finishingblow == True:
        show screen scrollable_scene(initial_ypos=1.0,bgtoadd="bg wrestle",imagetoadd="wrestle3_1", facetoadd="wrestle3_face3")
        with dissolve
        bo"I can't hear you over your squeaky screeching!"
        hide screen scrollable_scene
        show screen scrollable_scene(initial_ypos=1.0,bgtoadd="bg wrestle",imagetoadd="wrestle3_pants1", facetoadd="wrestle3_face3")
        with dissolve
        him"*Giggles* Heheh-hehe H-hey...!"
        "You tried pulling [him_name]'s shorts whilst she was still uncontrollably giggling..."
        him"I s-said I s-surrender! Hehe-heh" 
        hide screen scrollable_scene
        show screen scrollable_scene(initial_ypos=0.0,bgtoadd="bg wrestle",imagetoadd="wrestle3_pants2", facetoadd="wrestle3_face2")
        with dissolve
        call changeObedience("Himawari",1) from _call_changeObedience_83
        him"H-hey... T-that's not tickling!"
        hide screen scrollable_scene
        show screen scrollable_scene(initial_ypos=1.0,bgtoadd="bg wrestle",imagetoadd="wrestle3_pants2", facetoadd="wrestle3_face2")
        with dissolve
        bot"I can see her black p-panties peeking through her waistline!"
        hide screen scrollable_scene
        scene black
        bo"A-aw- ouch!" with vpunch
        him"What do you t-think you are doing!"
        him"W-what's with the stupid look on your face! C-cut it out..." with vpunch
        show int3 with dissolve
        $ l0_opportunity1_lose_1sttime = True
        "[him_name] kicked you in the balls and pushed you aside..."
        bo"N-not... fair...! *Wheezing*"
        $ hima_wrestling_won = True
        if quest_him.is_state("him1L_1", "pending") and not _in_replay:
            $ quest_him.change_quest_title("him1L_1",f"Wrestle with {him_name} and have her admit 'defeat'")
            $ notification (f"{him_name} Love objective completed")
            $ quest_him.check("him1L_1", "completed")
        him"Congrats idiot! You win... H-happy now?" with vpunch
        show int3_1 with dissolve
        him"Or so you'd like to think anyway!"
        $ change_music_volume(0.5, 2.0)
        "[him_name] walked all over you and turned down your music..."

        him"N-next time I won't go this easy on y-you if you pull off your stupid stunts again... "
        bo"Y-you... B-bitch! *Painful groans* Aw-w..."
        $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.8)
        him"Hmph!"
        scene black
        $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx2", loop=False, relative_volume = 0.7)
        him"...Better luck next time, weakling! Teehee!" with vpunch
        bo"*Groans* Next time... I'll g-get you for sure..."
        $ renpy.end_replay()
        jump action_taken
    else:

        show screen scrollable_scene(initial_ypos=1.0,bgtoadd="bg wrestle",imagetoadd="wrestle3_1")
        with dissolve
        bo"S-stop? I am only getting started!"
        hide screen scrollable_scene
        show screen scrollable_scene(initial_ypos=1.0,bgtoadd="bg wrestle",imagetoadd="wrestle3_pants1", facetoadd="wrestle3_face2")
        with dissolve
        him"*Heavy breathing* H-hey...!"
        "You grabbed [him_name]'s shorts and started pulling them down, but..."
        hide screen scrollable_scene
        show screen scrollable_scene(initial_ypos=0.0,bgtoadd="bg wrestle",imagetoadd="wrestle3_pants1", facetoadd="wrestle3_face2")
        with dissolve
        him"What do you t-think you are doing you creep!" 
        bo"I am j-just..."
        hide screen scrollable_scene
        scene black
        "[him_name] recovered just in time to..." with vpunch
        bo"Argh! You b-bitch-" with vpunch
        him"W-why would you ever put your dirty hands on me like that, you freaking imbecile!"
        call changeRespect("Himawari", -1) from _call_changeRespect_127
        "She pushed you away and..."
        him"Take this! you perverted idiot!" with vpunch
        jump l0_opportunity2_lose_jumpbed
    


label d_wrestle3_grope:

    hide screen scrollable_scene
    show screen scrollable_scene(initial_ypos=0.5,bgtoadd="bg wrestle",imagetoadd="wrestle3_grope2", facetoadd="wrestle3_face3")
    with dissolve
    bo"I can't hear you over your squeaky screeching!"
    him"I s-said I s-surrender! Hehe-hehe-"
    bot"Just one small movement and I'll be touching her tits! M-maybe she'll think it's part of the tickling!"
    hide screen scrollable_scene
    show screen scrollable_scene(initial_ypos=0.3,bgtoadd="bg wrestle",imagetoadd="wrestle3_grope3", facetoadd="wrestle3_face3")
    with dissolve
    him"*Giggles* Heheh-hehe H-hey...!" with vpunch
    call increaselust(10) from _call_increaselust_97
    bot"I am feeling them! I am feeling her underboob grazing my fingertips!"
    hide screen scrollable_scene
    show screen scrollable_scene(initial_ypos=0.3,bgtoadd="bg wrestle",imagetoadd="wrestle_gropetits")
    with dissolve
    him"I s-said I s-surrender! Hehe-heh"
    bo"D-do you now... Say you are sorry too!"
    bot"So s-soft... I should try going all the way up!"
    himt"W-what is he... Is he trying to t-touch me i-inappropriately!?"
    hide screen scrollable_scene
    show screen scrollable_scene(initial_ypos=0.0,bgtoadd="bg wrestle",imagetoadd="wrestle3_grope3", facetoadd="wrestle3_face2")
    with dissolve
    call changeObedience("Himawari",1) from _call_changeObedience_84
    him"Heh-hehe... H-hey! T-that's not tickling!"
    bo"W-what? Of c-course it is... What else could it b-be!"
    
    hide screen scrollable_scene
    scene black
    bo"A-aw- ouch!" with vpunch
    him"What do you t-think you are doing!"
    him"And w-what's with the stupid look on your face! C-cut it out..." with vpunch
    show int3 with dissolve
    $ l0_opportunity1_lose_1sttime = True
    "[him_name] kicked you in the balls and pushed you aside..."
    bo"N-not... fair...! *Wheezing*"
    $ hima_wrestling_won = True
    if quest_him.is_state("him1L_1", "pending"):
        $ quest_him.change_quest_title("him1L_1",f"Wrestle with {him_name} and have her admit 'defeat'")
        $ notification (f"{him_name} Love objective completed")
        $ quest_him.check("him1L_1", "completed")
    him"Congrats idiot! You win... H-happy now?" with vpunch
    show int3_1 with dissolve
    him"Or so you'd like to think anyway!"
    $ change_music_volume(0.5, 2.0)
    "[him_name] walked all over you and turned down your music..."

    him"N-next time I won't go this easy on y-you if you pull off your stupid stunts again... "
    bo"Y-you... B-bitch! *Painful groans* Aw-w..."
    $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.8)
    him"Hmph!"
    scene black
    $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx2", loop=False, relative_volume = 0.7)
    him"...Better luck next time, weakling! Teehee!" with vpunch
    bo"*Groans* Next time... I'll g-get you for sure..."
    $ d_wrestle3_stomach_finishingblow = True
    jump action_taken
    


screen scrollable_scene(testfix_xalign=0.5,initial_ypos=0.0,bgtoadd=None, imagetoadd=None, facetoadd=None,mask1=None, hovertext1=None, jump1=None, mask2=None, hovertext2=None, jump2=None, mask3=None, hovertext3=None, jump3=None):
    use actionbuttonshouse
    viewport:
        # Match the game's resolution
        xsize 1280
        ysize 720
        # Set the scrolling to vertical only
        yinitial initial_ypos
        draggable True
        # Adjust these values to control scroll speed
        edgescroll (275, 800)
        
        fixed:
            xsize 1280
            ysize 1280  # Full height of your images
            if bgtoadd is not None:
                add bgtoadd xalign 0.5 ypos 0
                
            if imagetoadd is not None:
                add imagetoadd xalign testfix_xalign ypos 0
                on "show" action Function(mark_screen_image_gallery, imagetoadd)
            if facetoadd is not None:
                add facetoadd xalign testfix_xalign ypos 0

            if mask1 is not None:
                imagebutton:
                    hover_sound "audio/soun_fx/select2.opus"
                    activate_sound "audio/soun_fx/select4.opus"
                    idle "idle1"  #image in ui / needs to be seperate for correct images to be displayed when hovering
                    hover mask1
                    focus_mask mask1
                    hovered [Show("displayTextScreen", displayText = hovertext1)]
                    unhovered [Hide("displayTextScreen")]
                    action [Hide("scrollable_scene_hotzones"),Hide("displayTextScreen"), Jump(jump1)]
            if mask2 is not None:
                imagebutton:
                    hover_sound "audio/soun_fx/select2.opus"
                    activate_sound "audio/soun_fx/select4.opus"
                    idle "idle2"
                    hover mask2
                    focus_mask mask2
                    hovered [Show("displayTextScreen", displayText = hovertext2)]
                    unhovered [Hide("displayTextScreen")]
                    action [Hide("scrollable_scene_hotzones"),Hide("displayTextScreen"), Jump(jump2)]
            if mask3 is not None:
                imagebutton:
                    hover_sound "audio/soun_fx/select2.opus"
                    activate_sound "audio/soun_fx/select4.opus"
                    idle "idle3"
                    hover mask3
                    focus_mask mask3
                    hovered [Show("displayTextScreen", displayText = hovertext3)]
                    unhovered [Hide("displayTextScreen")]
                    action [Hide("scrollable_scene_hotzones"),Hide("displayTextScreen"), Jump(jump3)]
