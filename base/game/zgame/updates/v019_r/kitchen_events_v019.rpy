label kitchen_events_gethandsy:
    $ initialize_replay_defaults()
    show screen parallax1280("hinkitchen approach1", menuenabled=True,initial_ypos=1.0) with dissolve
    call showscrollingimage from _call_showscrollingimage_173
    bot"Is it even possible to resist s-staring at it?"
    bot"Wearing those tight yoga pants, with an ass like that... It feels like it's almost sinful - for you to wear those, and for me to not appreciate your ass [hin_rel]!"
    default hinata_kitchen_approachgrab = False
    menu approach_kitchenmenu:
        bot"It feels like it's almost sinful - for you to wear those, and for me to not appreciate your ass [hin_rel]!"
        "{color=[obediencecolor]}Grab it!{/color}":
            bot"If there is a god, he would understand why I have to do this!"
            hide screen parallax1280
            show screen parallax1280("hinkitchen approach1_1", menuenabled=False,initial_ypos=0.2)
            with dissolve
            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp3.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            hin"*Gasp!* [bo_name_stutter]!?" with vpunch
            scene black
            call hidescrollingimage from _call_hidescrollingimage_102
            show kitchen day
            show blackscreen:
                alpha 0.95
            with dissolve
            if hinata_obedience >= 20:
                call checkObedience(20,"none","Hinata") from _call_checkObedience_33
                $ hinata_kitchen_approachgrab = True
                show hinkitchen approach_good1t with dissolve:
                    xalign 0.5 zoom 0.89 yalign 0.95
                hin"[bo_name_stutter]... A-are you feeling unwell again?"
                "To your surprise, [hin_name] turned around and softly comforted you with a hug..."
                hin"I've been a bit dismissive of you lately. I am s-sorry..."
                menu:
                    hin"I've been a bit dismissive of you lately. I am s-sorry..."
                    "{color=[obediencecolor]}Reach for her ass{/color}":
                        hide hinkitchen
                        show approach_goodt
                        with dissolve
                        pass
                hint"A-again! B-but..." with vpunch 
                hin"I k-know you are dealing with a lot, I don't want to make things harder for you, okay?"
                bot"[hin_rel_stutter]... is okay with t-this?" with vpunch
                hin"You need something, you let your [hin_rel_mother] know, okay? But..."
                hin"You can't just keep doing this. It's not right... y-you know?"
                bot"She's right, but I can't back down now!"
                bo"But [hin_rel]..."
                show approach_goodt with dissolve:
                    xalign 0.5 zoom 0.99 yalign 0.95
                bo"All I can think about all day is this s-stupid condition of mine, and how to deal with it..."
                show approach_goodt with dissolve:
                    xalign 0.5 zoom 1.05 yalign 0.95
                bo"It feels like hell on earth, losing my mind day by day..."
                show approach_goodt with dissolve:
                    xalign 0.5 zoom 1.1 yalign 0.95
                bo"The only thing in this cruel existence that comforts me..."
                hide approach_goodt
                show him_kitchen_gropeass1:
                    xalign 0.5 zoom 1.2 yalign 0.95
                with dissolve
                $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                bo"Is you, [hin_rel]..."
                bot"And your beautiful, bouncy ass!" with vpunch
                call changeObedience("Hinata", 1) from _call_changeObedience_137
                $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                hin"W-when you put it like that..."
                hin"I understand how difficult it must be for you, and I am g-glad I can comfort you. But still [bo_name]... not like this!"
                $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                show him_kitchen_gropeass1 with dissolve:
                    xalign 0.5 zoom 1.25 yalign 0.95
                hint"There must another way to provide comfort..." with vpunch
                "[hin_name] kept her arms wrapped around you for some time, lost in her own thoughts. You kept lightly feeling her bottom..."
                $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                show him_kitchen_gropeass1 with dissolve:
                    xalign 0.5 zoom 1.3 yalign 0.95
                hint"How can a [hin_rel_mother] accept something like this. Does [bo_name] really find solace in an old woman's b-body? Let alone his own [hin_rel_mother]'s?"
                bot"This is unreal! [hin_rel]'s just sitting there silently, while I am squeezing her ass!"
                hint"W-what do I even do! Knowing his pain, his condition..."
                bot"S-she must be doing this for me... D-does she pity me? Are her motherly instincts strong enough to break down her own inhibitions?"
                $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                show him_kitchen_gropeass1 with dissolve:
                    xalign 0.5 zoom 1.35 yalign 0.95
                hint"F-first in his bedroom, then this..." with vpunch
                hint"I've seen what the curse does to him. I can't stand seeing him suffer any more, especially not because of me."
                bot"M-maybe I could use this somehow! My 'unfortunate' condition... Perhaps it can turn out to be a fortunate one instead."
                $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                show him_kitchen_gropeass1 with dissolve:
                    xalign 0.5 zoom 1.4 yalign 0.95
                call changeObedience("Hinata", 1) from _call_changeObedience_138
                hint"But if it's just watching... if it's just some occasional... t-touching, then maybe I could find a safe way to help my boy through this."
                scene black with dissolve
                hin"O-okay, I've made up my mind..."
                show kitchen day
                show boruto surprised2 at left:
                    zoom 0.95
                show shina shy at center
                show shina:
                    easein 1 xalign 0.9
                with dissolve
                bo"A-about what?"
                show shina surprised2 with dissolve
                hint"Shoot! D-did I say that out loud?" with vpunch
                show shina concerned with dissolve
                hin"N-nothing, sorry! I was lost in my thoughts for a while."
                show shina shy with dissolve
                hin"But [bo_name], listen..."
                hin"If you are ever feeling down, if it truly feels like your life is 'A living hell', then..."
                show shina concerned with dissolve
                hin"You know you can always come to me, and I promise you, we'll find a way through it..."
                hin"You are my [hin_rel_to_bo], no matter what!"
                show boruto worried2 with dissolve
                bo"I know. T-thank you [hin_rel]..."
                show shina shy2 with dissolve
                hin"Good. I trust that you are feeling better by n-now?"
                show boruto embarassed with dissolve
                bo"I am! You are the best, [hin_rel]!"
                show shina shy with dissolve
                hin"I am glad, Now if you don't mind..."
                hide shina with dissolve
                hin"I have lunch to prepare."
                hide boruto with dissolve
                scene kitchen day hinata with fade
                bot"'Come to me and we'll find a way a through it!' ...D-does that mean what I think it means?"
                scene black with dissolve
                jump action_taken

            else:
                call checkObedience(20,"none","Hinata") from _call_checkObedience_34
                show approach_grope 1t with dissolve:
                    fit "contain"
                hin"T-that's enough, [bo_name_stutter]!"
                show approach_spank 1_1t with dissolve:
                    fit "contain"
                scene black with vpunch
                call checkObedience(20,"none","Hinata") from _call_checkObedience_35
                "[hin_name] shoved you back with her shoulder..."
                show kitchen day
                show boruto surprised2 at left:
                    zoom 0.95
                show shina serious:
                    xalign 0.7
                show shina:
                    easein 1 xalign 0.9
                with dissolve
                call changeRespect("Hinata", -1) from _call_changeRespect_227
                hin"[bo_name_stutter]! I thought I told you already. You can't be sneaking up on me like that! Let alone t-touching your [hin_rel_mother] like t-that!" with vpunch
                bo"S-sorry [hin_rel]! It's j-just that, my condition, I lost control for a second..."
                show shina shy2 with dissolve
                hin"I know, I know. But You have to be b-better, [bo_name]. You promised, remember?"
                show boruto embarassed with dissolve
                bot"I did?"
                show shina assertive with dissolve
                hin"You promised that you'll do your best to fight it!" with vpunch
                show boruto surprised2 with dissolve
                bo"But I am doing my best!"
                hin"Not enough, by the looks of it! Do better, [bo_name]. Be better!"
                bo"..."
                hide shina with dissolve
                hin"If you don't mind, I have to get back to preparing lunch..."
                hide boruto with dissolve
                scene kitchen day hinata with fade
                bot"Fuck! [hin_rel]'s really stern when it comes to t-touching her..."
                bot"Maybe she'd be more receptive if I found a way to evoke her motherly instincts...?"
                scene black with dissolve
                jump action_taken
            
        "{color=[lovecolor]}????{/color}" if hinata_kitchen_approachgrab == False:
            "Complete previous options to unlock!"
            jump approach_kitchenmenu

        "{color=[hatredcolor]}????{/color}" if hinata_kitchen_approachgrab == False:
            "Complete previous options to unlock!"
            jump approach_kitchenmenu
        
        "{color=[hatredcolor]}'Appreciate' her ass!{/color}" if hinata_kitchen_approachgrab == True:
            call checkHatred(30, "approach_kitchenmenu") from _call_checkHatred_31
            bot"You did say I could come to you when I am feeling bad [hin_rel]..."
            hide screen parallax1280
            show screen parallax1280("hinkitchen approach1_1", menuenabled=False,initial_ypos=0.2)
            with dissolve
            bot"And right now, I feel like your sexy ass could be of some help!"
            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp3.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            hin"*Gasp!* [bo_name_stutter]!?" with vpunch
            scene black
            call hidescrollingimage from _call_hidescrollingimage_103
            show kitchen day
            show blackscreen:
                alpha 0.95
            show approach_grope 1_1t with dissolve:
                xalign 0.5 zoom 0.89 yalign 0.95
            bo"S-sorry [hin_rel]. I am feeling a bit unwell..."
            hin"Y-you are?"
            show approach_goodt
            hide approach_grope
            with dissolve
            bot"All I gotta do is put on a little sad face and make up a sob story! Time to play the strings of her motherly instincts..."
            hide approach_goodt
            show him_kitchen_gropeass1:
                xalign 0.5 zoom 0.89 yalign 0.95
            with dissolve
            $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
            bo"This morning... I woke up and it felt like hell on earth [hin_rel]..."
            hin"W-was the... pain back?"
            bo"The pain..."
            show screen parallax1280("hinkitchen approach_grope 1") with dissolve
            call showscrollingimage from _call_showscrollingimage_174
            bo"...The dark thoughts, everything [hin_rel]!"
            "You leaned over her shoulder reaching for her ass. The evil smirk on your face intentionally concealed from her, as you recited false stories to lower her inhibitions..."
            bo"I had to spend hours in the bathroom, battling my demons..."
            hin"[bo_name]... I am sorry you had to go through that!"
            bo"The only thing that helped me through it..."
            menu hin_randommenu_12312398:
                bo"The only thing that helps me through it..."
                "{color=[obediencecolor]}Grope her!{/color}":
                    label gropherher_kitchen_jump_hin:
                    hide screen parallax1280
                    show screen parallax1280("hinkitchen kitchen_gropeass2",initial_ypos=1.0, menuenabled=True)
                    with dissolve
                    $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                    bo"...Is thinking about you, [hin_rel]!" with vpunch
                    bot"Or rather, your sexy ass!" with vpunch


                    hin"I... I  am g-glad you got through it, but... is t-this necessary?"
                    menu:
                        hin"I... I  am g-glad you got through it, but... is t-this necessary?"
                        "{color=[obediencecolor]}Squeeze that ass!{/color}":
                            pass
                    hide screen parallax1280
                    show screen parallax1280("hinkitchen approach_grope 2",1.1,initial_ypos=1.0)
                    with dissolve
                    $ renpy.sound.play("/audio/soun_fx/grope1.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                    bo"W-without you in my life, without your help... I don't think I'd be able to keep on living like this."
                    bot"Fuck! Does that feel good... You have such a lewd body on you, [hin_rel]..." with vpunch
                    hin"[bo_name_stutter], don't say that!" with vpunch
                    show hinkitchen kitchen_gropeass2_1 with dissolve
                    hide screen parallax1280
                    show screen parallax1280("hinkitchen kitchen_gropeass2_1",1,initial_ypos=1.0)
                    with dissolve
                    $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                    call changeObedience("Hinata", 1) from _call_changeObedience_139
                    hint"He... H-he is squeezing my butt! Is t-this really what h-helps him?"
                    hin"...[bo_name_stutter]?"
                    bo"S-sorry. Just wanted to thank you once again."
                    hide screen parallax1280
                    show screen parallax1280("hinkitchen kitchen_gropeass2_1",1.2,initial_ypos=1.0)
                    with dissolve
                    bo"I'd be so lost without your help... [hin_rel]!"
                    scene black
                    call hidescrollingimage from _call_hidescrollingimage_104
                    show kitchen day
                    show boruto snob at center:
                        zoom 1 xalign 0.7
                    show shina surprised2 at center
                    with dissolve
                    "[hin_name] lightly pushed her shoulder against your chest, as if it to get you to stop..."
                    show screen image_with_border("approach_cutout",1) with dissolve
                    
                    $ renpy.sound.play("/audio/soun_fx/grope1.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                    bot"I swear it on my life! In due time, your ass will be mine to play with as I damn please [hin_rel]!" with vpunch
                    "You squeezed her ass one last time before you let go..." with vpunch
                    hide screen image_with_border
                    show shina:
                        easein 1 xalign 0.0
                    call changeObedience("Hinata",1) from _call_changeObedience_140
                    hin"I am g-glad you are feeling better now..." with vpunch

                    bo"All thanks to you, [hin_rel]!"
                    show shina shy with dissolve
                    hin"Right, w-well... I have to get back to work."
                    hide shina with dissolve
                    hin"Stay safe, okay?"
                    hide boruto with dissolve
                    bo"You too!"
                    show kitchen hinata day with dissolve
                    bot"Otherwise, I won't get my chance to play with you, my sweet [hin_rel_mother]" with vpunch
                    jump action_taken


                    
                        
                "{color=[hatredcolor]}Spank that bitch!{/color}":
                    call checkHatred(30,"hin_randommenu_12312398") from _call_checkHatred_32
                    hide screen parallax1280
                    show screen parallax1280("hinkitchen approach_grope 2",1.0,initial_ypos=1.0)
                    with dissolve
                    bo"...Was you [hin_rel]!"
                    hide screen parallax1280
                    show screen parallax1280("hinkitchen approach_spank 1",1.0,initial_ypos=1.0)
                    with dissolve
                    bot"More like, you and your sweet, jiggly ass!"
                    bo"W-without you in my life, without your help... I don't think I'd be able to keep on living like this!"
                    hin"[bo_name_stutter], don't say that!" with vpunch
                    show screen parallax1280("hinkitchen approach_spank 1_1",1.0,initial_ypos=1.0) with dissolve
                    bo"Don't worry [hin_rel], I don't plan on dying just yet..."
                    call changeHatred(1) from _call_changeHatred_180
                    bot"Not before I get the chance to have my way with you!" with vpunch
                    hin"I... I  am g-glad you are working through it, but... is t-this necessary?"
                    scene black with dissolve
                    call hidescrollingimage("Click twice to spank her ass!") from _call_hidescrollingimage_105
                    show hinkitchen approach_spank 1_1 with dissolve:
                        yalign 0.0
                    show hinkitchen approach_spank 1_1:
                        easein 1 yalign 1.0
                    bo"Necessary? No, but it is mandatory to..."
                    show hinkitchen approach_spank 1 with Dissolve(0.2)
                    $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                    show hinkitchen approach_spank 1_2 with Dissolve (0.2)
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                    show hinkitchen approach_spank 1_2:
                        easein 0.2 yalign 0.0
                    bo"...To say thank you! For all you'are doing for me..." with vpunch
                    show hinkitchen approach_spank 1_2:
                        easein 0.2 yalign 1.0
                    bot"Look at that fat ass of your jiggle [hin_rel]!"
                    scene black with vpunch
                    hin"O-okay, that's enough!" with vpunch

                    show kitchen day
                    show boruto snob at center:
                        zoom 1 xalign 0.7
                    show shina surprised5 at center
                    with dissolve
                    "[hin_name] tried to shove you away with her shoulder, as if it to get you to stop..."
                    show screen image_with_border("approach_cutout",1) with dissolve
                    
                    $ renpy.sound.play("/audio/soun_fx/grope1.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                    bot"I swear it on my life! In due time, your ass will belong to me [hin_rel]!" with vpunch
                    "You squeezed her ass one last time before you let go..." with vpunch
                    call changeHatred(1) from _call_changeHatred_181
                    bot"You'll be leaving the bedroom sore after I am done having my way with you!"
                    hide screen image_with_border
                    show shina surprised3:
                        easein 0.5 xalign 0.0
                    hin"[bo_name_stutter]! I said that's enough!" with vpunch

                    bo"S-sorry [hin_rel]! My condition... It flared up for a second there!"
                    show shina concerned with dissolve
                    hin"B-but... W-why would you hit your [hin_rel_mother]'s butt like t-that!"
                    bo"I was just t-thanking you [hin_rel]. It's not that deep..."
                    show shina shy with dissolve
                    hin"R-right, w-well... Words alone will suffice in the future, okay?" with vpunch
                    hin"But I do hope you are feeling better after this morning. It sounds like you were dealing with a lot..."
                    hide shina with dissolve
                    hin"Stay safe, okay?"
                    hide boruto with dissolve
                    bo"You too!"
                    show kitchen hinata day with dissolve
                    bot"Otherwise, I won't get my chance to use you, my sweet [hin_rel_mother]..." with vpunch
                    jump action_taken

                




        "{color=[lovecolor]}Hug her{/color}" if hinata_kitchen_approachgrab == True:
            scene black
            hide screen parallax1280
            show screen parallax1280("hinkitchen approach1", menuenabled=False,initial_ypos=0.1)
            with dissolve
            call hidescrollingimage from _call_hidescrollingimage_106
            bo"[hin_rel]..."
            show kitchen day
            show blackscreen:
                alpha 0.95
            with dissolve
            show hinkitchen approach_good1t with dissolve:
                xalign 0.5 zoom 0.89 yalign 0.95
            hin"[bo_name_stutter]... A-are you feeling unwell again?"
            call changeLove("Hinata",1,"kitchenhug2") from _call_changeLove_47
            hin"It'll be okay. I am here for you..."
            menu:
                hin"It'll be okay. I am here for you..."
                "{color=[lovecolor]}'Cry' on her chest{/color}":
                    label cryonherchest_motro_replay:
                    $ initialize_replay_defaults()
                    show approach_motorboat 1 with dissolve:
                        fit "contain" xalign 0.5
                    bo"I am struggling [hin_rel]... I am losing grip... *Sniffles*" with vpunch
                    if hinata_love >=4:
                        hin"T-there, there..."
                        hin"Everything will turn out to be fine, you'll see..."
                        bo"T-thank you [hin_rel]... *Sniffles*"
                        show approach_motorboat 1_1 with dissolve:
                            zoom 1.1
                        bot"[hin_rel]'s boobies!"
                        bot"If I could just pull down her sweater a little bit..."
                        "Your hand creeps upwards, rubbing [hin_name]'s back..."
                        show approach_motorboat 2 with dissolve
                        "...Enough to have her sweater slide off her shoulder!"
                        bot"She smells so nice... I could die happy with my face buried in [hin_rel]'s tits!"
                        call checkLove(4,"none","Hinata") from _call_checkLove_6
                        show approach_motorboat 3_1 with dissolve:
                            zoom 1.0
                        hint"O-oh! He's clinging on my back. He's so a-affectionate lately..." with vpunch
                        show approach_motorboat 3_2 with dissolve:
                            zoom 1.1 yalign 0.0
                        hin"M-my sweet boy..."
                        scene black
                        show approach_motorboat 4t with dissolve:
                            yalign 1.0
                        show approach_motorboat 4t:
                            easein 3 yalign 0.0
                        "[hin_name] wrapped her hands around your shoulders and gave you a reassuring hug..."
                        hin"It won't be easy, but..."
                        bo"*Sniffles*" with vpunch
                        hin"With enough effort, enough determination, We'll work through it. Together..."
                        show approach_motorboat 4_1t with dissolve:
                            yalign 0.0
                        bot"Hehe... Your boobs alone are enough to brighten my days [hin_rel]!"
                        menu:
                            bot"Hehe... Your boobs alone are enough to brighten my days [hin_rel]!"
                            "{color=[lovecolor]}I love you, [hin_rel]{/color}":
                                show approach_motorboat 4t with dissolve:
                                    yalign 0.0
                                bo"I love you [hin_rel]..."
                                show approach_motorboat 6t with dissolve:
                                    yalign 0.0
                                $ renpy.sound.play("/audio/soun_fx/hinata/kisscheek.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                                "She leaned in and kissed your forehead..."
                                hint"M-my sweater! [bo_name_stutter]'s sniffling on my bare c-chest..." with vpunch
                                show approach_motorboat 6t:
                                    easein 3 yalign 0.8
                                "She softly pushed you away, concerned about the closeness of it all."
                                scene black with vpunch
                                hin"T-there, there..."
                                show kitchen day
                                show boruto surprised2 at center:
                                    zoom 1 xalign 0.8
                                show shina concerned at center
                                with dissolve
                                show shina:
                                    easein 1 xalign 0.2
                                call changeLove("Hinata",1,"motorboatkitchen",1) from _call_changeLove_48
                                hin"You know that I love you too, right? No matter what..."
                                show boruto worried2 with dissolve
                                bo"I know..."
                                show shina shy with dissolve
                                hin"We'll get through this, I promise! If you need anything, I'll always be here for you, okay?"
                                bo"T-thanks [hin_rel]..."
                                hide shina with dissolve
                                hin"Now I have to get back to preparing lunch if you don't mind!"
                                scene kitchen day hinata with fade
                                bot"B...boobies..."
                                scene black with dissolve
                                bot"...Are paradise!"
                                jump action_taken

                            "{color=[obediencecolor]}Bury your face in them!{/color}":
                                bot"How can I not..."
                                show approach_motorboat 5t with dissolve:
                                    yalign 0.0
                                
                                hin"...[bo_name_stutter]?" with vpunch
                                bo"*Sniffles Loudly*" with vpunch
                                bot"Nothing wrong with some fake tears if it is to feel your soft boobies all over my face!"
                                hint"Is he c-crying? B-but... M-my sweater! He is resting his head on m-my bare chest..."
                                show approach_motorboat 5t with dissolve:
                                    easein 1 yalign 1.0
                                pause 0.8
                                show approach_motorboat 6t with dissolve:
                                    yalign 0.0
                                hin"D-don't cry! T-there, there..."
                                menu:
                                    hin"D-don't cry! T-there, there..."
                                    "{color=[obediencecolor]}Grope her ass{/color}":
                                        hin"...Are you feeling b-better?"
                                        scene black
                                        show him_kitchen_gropeass1 with dissolve:
                                            xalign 0.5 zoom 0.99 yalign 0.95
                                        $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                                        bo"I am... *Sniffles* Thanks to you [hin_rel]."
                                        hint"Is he... s-squeezing m-my butt?"
                                        show kitchen day
                                        show boruto worried2 at center:
                                            zoom 1 xalign 0.7
                                        show shina surprised2 at center
                                        with dissolve
                                        "[hin_name] lightly pushed her shoulder against your chest, as if it to get you to stop..."
                                        show screen image_with_border("approach_cutout",1) with dissolve
                                        "You copped one more feel of it before letting go..."
                                        hide screen image_with_border with dissolve
                                        show shina concerned with dissolve:
                                            easein 1 xalign 0.2
                                        hin"[bo_name_stutter] just now, y-your hands..."
                                        hint"M-maybe now's not the time to make him feel even worse..."
                                        show shina shy with dissolve
                                        $ renpy.sound.play("/audio/soun_fx/hinata/hinatasigh3.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                        hin"*Sigh* N-nevermind..."
                                        hin"Are you feeling any better?"
                                        show boruto snob with dissolve
                                        bot"Stuffing my face in your tits, and grabbing your sexy ass, what do you think [hin_rel]?"
                                        bo"I am! You are the best at comforting me [hin_rel]!"
                                        call changeObedience("Hinata",1) from _call_changeObedience_141
                                        hin"R-right, well... You need anything, I'll always be here for you, okay?"
                                        bot"You bet I'll be back for more!"
                                        hide shina with dissolve
                                        hin"Now I have to get back to preparing lunch if you don't mind."
                                        scene kitchen day hinata with fade
                                        bot"[hin_rel] is slowly getting comfortable with my advances..."
                                        scene black with dissolve
                                        jump action_taken

                                    "Play it safe":
                                        "She softly pushed you away, concerned about the closeness of it all."
                                        scene black with vpunch
                                        hin"T-there, there..."
                                        show kitchen day
                                        show boruto surprised2 at center:
                                            zoom 1 xalign 0.8
                                        show shina concerned at center
                                        with dissolve
                                        show shina:
                                            easein 1 xalign 0.2
                                        call changeRespect("Hinata",1,"motorboatkitchen",1) from _call_changeRespect_228
                                        hin"You know that I care for you, right? No matter what..."
                                        show boruto worried2 with dissolve
                                        bo"I know..."
                                        show shina shy with dissolve
                                        hin"We'll get through this, I promise! If you need anything, I'll always be here for you, okay?"
                                        bo"T-thanks [hin_rel]..."
                                        hide shina with dissolve
                                        hin"Now I have to get back to preparing lunch if you don't mind!"
                                        scene kitchen day hinata with fade
                                        bot"B...boobies..."
                                        scene black with dissolve
                                        bot"...Are paradise!"
                                        jump action_taken
                                    

                        
                    else:
                        hin"T-there, there..."
                        hin"Everything will turn out to be fine, you'll see..."
                        bo"T-thank you [hin_rel]... *Sniffles*"
                        show approach_motorboat 1_1 with dissolve:
                            zoom 1.1
                        bot"[hin_rel]'s boobies!"
                        bot"If I could just pull down her sweater a little bit..."
                        "Your hand creeps upwards, rubbing [hin_name]'s back..."
                        show approach_motorboat 2 with dissolve
                        "...Enough to have her sweater slide off her shoulder!"
                        bot"She smells so nice... I could die happy with my face buried in [hin_rel]'s tits!"
                        call checkLove(4,"none","Hinata") from _call_checkLove_7
                        show approach_motorboat 3_1 with dissolve
                        hint"M-my sweater!" with vpunch
                        scene black with vpunch
                        hin"[bo_name_stutter]... T-that's a bit too close for comfort..."
                        show kitchen day
                        show boruto surprised2 at center:
                            zoom 1 xalign 0.8
                        show shina concerned at center
                        with dissolve
                        "[hin_name] broke the hug, concerned about the closeness of it all..."
                        show shina:
                            easein 1 xalign 0.2
                        hin"Y-you'll be alright, I promise..."
                        show shina shy with dissolve
                        hin"You need anything, I'll always be here for you, okay?"
                        bo"T-thanks [hin_rel]..."
                        hide shina with dissolve
                        hin"Now I have to get back to preparing lunch if you don't mind."
                        scene kitchen day hinata with fade
                        bot"B...boobies..."
                        scene black with dissolve
                        bot"...Are paradise!"
                        jump action_taken
                        
                "{color=[obediencecolor]}Grope her{/color}":
                    bo"I've been having a really tough time lately..."
                    hide hinkitchen approach_good1t
                    show him_kitchen_gropeass1
                    with dissolve
                    $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                    hin"I am s-sorry, [bo_name]. I wish I could help..."
                    bo"You a-are helping in a way [hin_rel]..."
                    bo"The only thing that helps me battle my demons..."
                    call showscrollingimage from _call_showscrollingimage_175
                    jump gropherher_kitchen_jump_hin

            
        


label kitchen_events_gethandsy2:
    bot"It needs some attention!"
    show hinata ktichen_approach2 with fade
    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp3.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    $ renpy.sound.play("/audio/soun_fx/grope1.opus", channel="sfx3", loop=False, relative_volume = 0.6)
    hin"*Gasp!* [bo_name_stutter]!?" with vpunch
    bo"Hey [hin_rel]..."
    scene black with vpunch

    show hinkitchen approach_spank 1 with dissolve:
        yalign 0.0
    show hinkitchen approach_spank 1:
        easein 2 yalign 0.9
    hin"You scared me, [bo_name_stutter]! Is something... w-wrong?"
    bot"O-oh? She didn't even push me away this time!"
    bo"S-sorry [hin_rel]! I was just thinking if you could..."
    menu kitchenlunch_prepare123:
        bo"S-sorry [hin_rel]! I was just thinking if you could..."
        "{color=[obediencecolor]}Prepare some lunch...{/color}":
            show hinkitchen approach_grope 2 with dissolve:
                yalign 0.65
            $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
            bo"...Prepare some lunch for us! You know, to eat together for once..."
            hin"I will, I w-will... but only if you sit down on the table and be a good boy!" with vpunch
            menu:
                hin"I will, I w-will... but only if you sit down on the table and be a good boy!"
                "Be respectful...":
                    show hinkitchen approach_spank 1 with dissolve:
                        yalign 1.0
                    bo"Thanks, [hin_rel]. You are the best!"
                    scene black with dissolve
                    call changeRespect("Hinata", 1) from _call_changeRespect_229
                    "You sit down and wait for [hin_name] to finish cooking..."
                "{color=[obediencecolor]}I'll be a good boy!{/color}":
                    bo"For you, [hin_rel]..."
                    $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                    show hinkitchen kitchen_gropeass2_1:
                        yalign 0.0
                    bo"I'll be as good as you want me to!" with vpunch
                    hint"*Gasps* W-what does he think he is..."
                    bot"If you keep letting me feel your ass that is! Hehe..." with vpunch
                    scene black with vpunch
                    hin"[bo_name_stutter]! That's enough!" with vpunch
                    call changeRespect("Hinata", -1) from _call_changeRespect_230
                    hin"I told you to sit and wait for lunch to be ready! Otherwise, no lunch for you..."
                    bo"Right, right..."
                    "You sit down and wait for [hin_name] to finish cooking..."
            jump kitchen_events_eatafternoon

                

        "{color=[hatredcolor]}Prepare some lunch!{/color}":
            call checkHatred(30, "kitchenlunch_prepare123") from _call_checkHatred_33
            show screen parallax1280("hinkitchen approach_spank 1_1",1.0,initial_ypos=1.0) with dissolve
            call showscrollingimage from _call_showscrollingimage_176
            bo"...You know, maybe make me a sandwich or something!"
            hin"A sandwich...?"
            scene black
            call hidescrollingimage("Click twice to spank her ass!") from _call_hidescrollingimage_107
            show hinkitchen approach_spank 1_1 with dissolve:
                yalign 0.0
            show hinkitchen approach_spank 1_1:
                easein 1 yalign 1.0
            bo"You heard me..."
            show hinkitchen approach_spank 1 with Dissolve(0.2)
            $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.6)
            show hinkitchen approach_spank 1_2 with Dissolve (0.2)
            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx2", loop=False, relative_volume = 0.6)
            with vpunch
            pause 0.3
            show hinkitchen approach_spank 1_2:
                easein 0.2 yalign 0.0
            bo"Get to work, [hin_rel]!" with vpunch
            show hinkitchen approach_spank 1_2:
                easein 0.2 yalign 1.0
            bot"Look at that fat ass of your bounce up and down [hin_rel]!"
            scene black with vpunch
            hin"O-okay, that's enough!" with vpunch
            scene kitchen day
            show shina serious at center with dissolve
            call changeRespect("Hinata", -2) from _call_changeRespect_231
            hin"I won't have any more of your disrespect, [bo_name]!"
            show shina assertive with dissolve
            hin"There will be no lunch for you, nor today, nor ever if you keep acting like a brat! Am I understood?" with vpunch
            bo"It was just a joke, [hin_rel]! Relax..."
            hin"Out of my kitchen. Now!" with vpunch
            scene black with dissolve
            bot"S-scary... We'll see how long that lasts for [hin_rel]!"

            jump action_taken


default generictalk_work = True
default generictalk_school = True
default generictalk_life = True
default generictalk_politics = True


label dropcutlery:
    default droppedcutlery_counter = 0

    scene black with vpunch
    $ renpy.sound.play("/audio/soun_fx/dropfork.opus", channel="sfx2", loop=False, relative_volume = 0.6)

    if droppedcutlery_counter == 0:
        $ droppedcutlery_counter += 1
        bo"Oops!" with vpunch
        if eating_hinata_annoyed == 0:
            show eattogether1 peek0 with dissolve:
                fit "contain" zoom 1.02 yalign 1.0
        elif eating_hinata_annoyed >= 1:
            show eattogether1 peek0_1 with dissolve:
                fit "contain" zoom 1.02 yalign 1.0
        bo"Clumsy me! Dropped my fork..."
        bot"Totally not on purpose! Hehe..."
        him"More like, stupid you!" with vpunch
        hin"[him_name]! Stop it..." with vpunch
        hin"Be more careful [bo_name]... Did you find it or shall I get you another?"
        menu:
            hin"Be more careful [bo_name]... Did you find it or shall I get you another?"
            "Mess with [hin_name]":
                bo"It's under your chair [hin_rel]!"
                bo"Let me just..."
                menu takeoffsandals_menu:
                    bo"Let me just..."
                    "Take off her sandals":
                        $ eating_hinata_annoyed +=1
                        default droppedcutlery_removesandals = False
                        $ droppedcutlery_removesandals = True
                        show eating_table_hand with dissolve:
                            xalign 0.1 ypos -150
                        with dissolve
                        bo"I'll get you comfortable, [hin_rel]!"
                        scene eattogether1 peek0_1 with fade:
                            fit "contain" zoom 1.02 yalign 1.0
                        hin"H-hey, that t-tickles! W-what is that for? *Giggles*"
                        bot"Now you can get real comfy!"
                        scene black
                        hin"Oo-h! That reminds me..." with vpunch
                        show eattogether1 intermission with dissolve
                        hin"I've got something else in store for you two!"
                        scene hin_kitchen foodready1_1 with dissolve:
                            yalign 0.0
                        show hin_kitchen with dissolve:
                            easein 6 yalign 1.0
                        him"Is it what I think it is!?" with vpunch
                        hin"Stuffed bagel rolls! Been a while since we last indulged ourselves hasn't it?"
                        show hin_kitchen with dissolve:
                            yalign 0.0
                        him"Yaaay! Gimme gimme!" with vpunch
                        scene black with dissolve
                        bo"Nice one [hin_rel]!"
                        him"Hands off, they are all mine!" with vpunch
                        hin"[him_name]! One each, okay?"
                        jump table_talking_points

                        
                        


                    "????" if droppedcutlery_removesandals == False:
                        "Complete previous option to unlock!"
                        jump takeoffsandals_menu
                    
            "Mess with [him_name]":
                bo"It's under your chair [him_name]!"
                menu movelegskitch_menu:
                    bo"It's under your chair [him_name]!"
                    "Can you move your legs a bit?":
                        $ eating_himawari_annoyed +=1
                        default droppedcutlery_movelegs = False
                        $ droppedcutlery_movelegs = True
                        bo"Can you move your legs to the side so I can reach it?"
                        scene eattogether1 peek2_1 with fade
                        him"Did you find your damn fork yet?"
                        hin"[him_name], language!" with vpunch
                        bot"Hehe! Thanks for the nice view of your panties, you stupid brat..."
                        scene black with vpunch
                        $ renpy.sound.play("/audio/soun_fx/himawari/himagasp3.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                        scene eattogether1 intermission with dissolve
                        "[him_name] only just realized her panties would be clearly visible to you..."
                        him"W-what the heck are you still doing under the table you w-weirdo!" with vpunch
                        scene black
                        hin"[him_name]! No more cussing or you won't be allowed to have any of my specialty..." with vpunch
                        show eattogether1 intermission with dissolve
                        hin"I've been preparing something else for you two, if only you would stop fighting..."
                        scene hin_kitchen foodready1_1 with dissolve:
                            yalign 0.0
                        show hin_kitchen with dissolve:
                            easein 6 yalign 1.0
                        him"Is it what I think it is!?" with vpunch
                        hin"Stuffed bagel rolls! Been a while since we last indulged ourselves hasn't it?"
                        scene hin_kitchen foodready1_1 with dissolve:
                            yalign 1.0
                        him"Yaaay! Gimme gimme!" with vpunch
                        scene black with dissolve
                        bo"Nice one [hin_rel]!"
                        him"Hands off, they are all mine!" with vpunch
                        hin"[him_name]! One each, okay?"
                        jump table_talking_points
                    "????" if droppedcutlery_movelegs == False:
                        "Complete previous option to unlock!"
                        jump movelegskitch_menu

    else:
        $ droppedcutlery_counter += 1
        bo"Oops!" with vpunch
        if eating_hinata_annoyed == 0:
            show eattogether1 peek0 with dissolve:
                fit "contain" zoom 1.02 yalign 1.0
        elif eating_hinata_annoyed >= 1:
            show eattogether1 peek0_1 with dissolve:
                fit "contain" zoom 1.02 yalign 1.0
        bo"Clumsy me! Dropped my fork... again!"
        bot"Totally not on purpose of course!"
        hin"What's wrong with you [bo_name], feeling stressed?"
        him"He is probably just-"
        hin"[him_name]! Don't..." with vpunch
        $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.8)
        him"Hmph!" with vpunch
        menu:
            him"Hmph!"
            "Mess with [hin_name]":
                
                bo"It's under your chair [hin_rel]!"
                bo"Let me just..."
                menu randomassmenu12348949:
                    bo"Let me just..."
                    "Find an excuse to eat her feet!":
                        $ eating_hinata_annoyed +=1
                        bo"[hin_rel_stutter], your foot has some... s-stain on it."
                        hin"H-huh? A stain...?"
                        show eattogether1 peek0_3 with dissolve
                        bo"Let me just..."
                        $ renpy.sound.play("/audio/soun_fx/suck3.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                        show eattogether1 peek0_2 with dissolve
                        bo"R-rub it off with this napkin for you!"
                        $ renpy.sound.play("/audio/soun_fx/suck2.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                        hin"H-hey, that t-tickles! And it feels... s-slimy! *Giggles*" with vpunch
                        bot"[hin_rel]'s feet, they are just so pretty!"
                        $ renpy.sound.play("/audio/soun_fx/suck1.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                        bot"Why am I such a-"
                        scene black with vpunch
                        him"MOOOOOOM!" with vpunch
                        $ renpy.sound.play("/audio/soun_fx/horror.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                        show eattogether_hima_annoyed with dissolve:
                            fit "contain"
                        call changeRespect("Himawari", -2) from _call_changeRespect_232
                        him"I knew it! [bo_name] is just p-perving on us!" with vpunch
                        him"He had... he had his m-mouth on your foot! What the hell!?"
                        bot"F-fucking brat!"
                        scene black with vpunch
                        hin"H-his mouth?"
                        show eattogether_hina_annoyed with dissolve:
                            xalign 0.5
                        show eattogether_hina_annoyed:
                            easein 3 yalign 1.0
                        hin"Is that true [bo_name]? You said you were using a napkin!" with vpunch
                        bo"N-no I was just-"
                        hin"So that's why it felt slimy!" with vpunch
                        scene black
                        show kitchen day
                        show shina assertive
                        with dissolve
                        call changeRespect("Hinata", -1) from _call_changeRespect_233
                        hin"Good g-grief, [bo_name]! Was that some twisted joke of yours?"
                        hide shina with dissolve
                        hin"*Sigh...*"
                        show himaschoolt smug at right with dissolve:
                            zoom 0.55
                        him"Hehe... LOSER!" with vpunch
                        hide himaschoolt with dissolve
                        bot"Damned brat! Always ruining the fun..."
                        "Both girls left the kitchen, leaving you alone."
                        scene black with dissolve
                        jump kitchen_talk_end
                        

                        
                        


                    "{color=[obediencecolor]}Can you fetch it for me [hin_rel]?{/color}":
                        "You intentionally move your fork towards [hin_name]'s side..."
                        bo"It's on your side [hin_rel]. Think you can fetch it for me?"
                        if hinata_obedience >= 25:
                            call checkObedience(25,"randomassmenu12348949","Hinata") from _call_checkObedience_36
                            scene black with dissolve
                            hin"S-sure thing! Just a sec..."
                            show eattogether1 peek3 with dissolve:
                                fit "contain"
                            call increaselust(10) from _call_increaselust_254
                            bot"Good g-gods! Look at that ass! Day by day, she is turning into quite the obedient [hin_rel_mother]..."
                            hin"Found it!" with vpunch
                            scene black with dissolve
                            bot"Still ways to go though [hin_rel]!"
                            jump table_talking_points

                        else:
                            call checkObedience(25,"randomassmenu12348949","Hinata") from _call_checkObedience_37
                            hin"I don't think so young man. Better scooch over there yourself! *Giggles*"
                            scene black with dissolve
                            bo"F-fine..."
                            jump table_talking_points

                                                
            "Mess with [him_name]":
                $ eating_himawari_annoyed +=1
                bo"It's under your chair [him_name]!"
                bo"Wait a second... there's a bug on your legs!" with vpunch
                show eattogether1 peek2_1 with fade:
                    zoom 1.2 xalign 1.0 yalign 0.8
                him"A b-b-b-bug!?" with vpunch
                bot"Heheh! I knew this would work..."
                scene black
                show eattogether_hima_annoyed0:
                    xalign 0.5
                with dissolve
                him"Wait a second..."
                $ renpy.sound.play("/audio/soun_fx/horror.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                show eattogether_hima_annoyed with dissolve:
                    fit "contain"
                call changeRespect("Himawari", -2) from _call_changeRespect_234
                him"I was right, Mom!  [bo_name] is just p-perving on us!" with vpunch
                him"There's not even a bug to be found! He was just staring on me!"
                bot"F-fucking brat!"
                hin"Is that true [bo_name]?" with vpunch
                scene black
                show kitchen day
                show shina assertive
                with dissolve
                bo"It was just a prank to get back to her. Of course I wasn't staring..."
                call changeRespect("Hinata", -1) from _call_changeRespect_235
                hin"Good g-grief, [bo_name]! That doesn't make it any better!" with vpunch
                hin"And to think I took your side before..."
                hide shina with dissolve
                $ renpy.sound.play("/audio/soun_fx/hinata/hinatasigh3.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                hin"*Sigh...*"
                show himaschoolt smug at right with dissolve:
                    zoom 0.55
                him"Hehe... LOSER!" with vpunch
                hide himaschoolt with dissolve
                bot"Damned brat! Always ruining the fun..."
                "Both girls left the kitchen, leaving you alone."
                scene black with dissolve
                jump kitchen_talk_end

                


    
    

label kitchen_talk_end:
    $ droppedcutlery_counter = 0
    $ droppedcutlery_removesandals = False
    $ droppedcutlery_movelegs = False
    $ eating_himawari_annoyed = 0
    $ eating_hinata_annoyed = 0
    $ eating_talk_counter = 0

    jump action_taken

label table_talking_points:
    default eating_himawari_annoyed = 0 #eating ends at 2
    default eating_hinata_annoyed = 0 #eating ends at 2
    default eating_talk_counter = 0  #eating ends at 3
    
    # hinata_slipped_banana (If True Hinata slipped)
    # hinata_slipped_banana_slepttogether
    # hinata_slipped_banana_usedher
    # hinata_slipped_banana_carriedfail
    # hinata_slipped_banana_carriedsuccess
    # yoru_1st_photoshoot = True Yoruichi modeling done
    # blindfoldrepeat if 1/2 = Himawari tasted, if 3 = Himawari sucked
    # if highscore > 1 = work
    # talkedaboutmother = Himawari shoping, talked about debt
    # tsunade_discovery_seen = True (Tsunade discovery)
    # tenten_date_counter >= 1 (Went on tenten date)
    
    default discussed_work = False
    default discussed_school = False
    default discussed_life = False
    default discussed_politics = False


    scene hin_kitchen table1_1:
        fit "contain"
    if eating_himawari_annoyed == 1:
        show hima_eat1:
            fit "contain"
        with fade
        "[him_name] seemed annoyed..."


        jump kitchen_talk_end
    "Some light conversation takes place..."
    with fade
    # Check if all enabled topics have been discussed
    $ all_discussed = True

    # Only check topics that are currently enabled
    if generictalk_work and not discussed_work:
        $ all_discussed = False
    if generictalk_school and not discussed_school:
        $ all_discussed = False
    if generictalk_life and not discussed_life:
        $ all_discussed = False
    if generictalk_politics and not discussed_politics:
        $ all_discussed = False

    if eating_talk_counter >= 3:
        hin"Right. Let's wrap up then, shall we?"
        call changeRespect("Hinata", 1) from _call_changeRespect_236
        hin"Thank you both for sitting down together for once, and not ripping each other out to pieces!"
        scene black with vpunch
        him"Hmph! I am outie! Thanks for the food mama!" with vpunch
        bo"I'll be going too, thanks [hin_rel]..."
        hin"Of course!" 
        jump kitchen_talk_end




    #todo all one time convos go here
    if eating_talk_counter >= 1:
        $ eating_talk_counter += 1 #Increase counter here to avoid clutter in labels


        # high_score
        if high_score >= 2 and high_score_talked == False:
            default high_score_talked = False
            $ high_score_talked = True
            call conversation_highscore1 from _call_conversation_highscore1

        # hinata_slipped_banana_slepttogether
        elif hinata_slipped_banana_slepttogether == True and hinata_slipped_banana_slepttogether_talked == False:
            default hinata_slipped_banana_slepttogether_talked = False
            $ hinata_slipped_banana_slepttogether_talked = True
            call conversation_hinata_slipped_banana_slepttogether from _call_conversation_hinata_slipped_banana_slepttogether
        # hinata_slipped_banana_usedher
        elif hinata_slipped_banana_usedher == True and hinata_slipped_banana_usedher_talked == False:
            default hinata_slipped_banana_usedher_talked = False
            $ hinata_slipped_banana_usedher_talked = True
            call conversation_hinata_slipped_banana_usedher from _call_conversation_hinata_slipped_banana_usedher
        # hinata_slipped_banana_carriedfail
        elif hinata_slipped_banana_carriedfail == True and hinata_slipped_banana_carriedfail_talked == False:
            default hinata_slipped_banana_carriedfail_talked = False
            $ hinata_slipped_banana_carriedfail_talked = True
            call conversation_hinata_slipped_banana_carriedfail from _call_conversation_hinata_slipped_banana_carriedfail
        # hinata_slipped_banana_carriedsuccess
        elif hinata_slipped_banana_carriedsuccess == True and hinata_slipped_banana_carriedsuccess_talked == False:
            default hinata_slipped_banana_carriedsuccess_talked = False
            $ hinata_slipped_banana_carriedsuccess_talked = True
            jump conversation_hinata_slipped_banana_carriedfail
        # yoru_1st_photoshoot
        elif yoru_1st_photoshoot == True and yoru_1st_photoshoot_talked == False:
            default yoru_1st_photoshoot_talked = False
            $ yoru_1st_photoshoot_talked = True
            jump conversation_yoru_1st_photoshoot
        # blindfoldrepeat 1
        elif blindfoldrepeat == 1 and blindfoldrepeat1_talked == False:
            default blindfoldrepeat1_talked = False
            $ blindfoldrepeat1_talked = True
            jump conversation_blindfoldrepeat1

        # blindfoldrepeat 1
        elif blindfoldrepeat >= 2 and blindfoldrepeat3_talked == False:
            default blindfoldrepeat3_talked = False
            $ blindfoldrepeat3_talked = True
            jump conversation_blindfoldrepeat3
        
        # talkedaboutmother
        elif talkedaboutmother == True and talkedaboutmother_talked == False:
            default talkedaboutmother_talked = False
            $ talkedaboutmother_talked = True
            jump conversation_talkedaboutmother
        # tsunade_discovery_seen
        elif tsunade_discovery_seen == True and tsunade_discovery_seen_talked == False:
            default tsunade_discovery_seen_talked = False
            $ tsunade_discovery_seen_talked = True
            jump conversation_tsunade_discovery_seen
        # tenten_date_counter >= 1 (Went on tenten date)
        elif tenten_date_counter >= 1 and tenten_date_counter_talked == False and tenten_lake_date_fail_permanent != True:
            default tenten_date_counter_talked = False
            $ tenten_date_counter_talked = True
            jump conversation_tenten_date_counter1

        else:
            pass #Continue with generic conversation


    #end
    #----------
    #----------
    #----------
    #----------
    #----------
    #----------
    #----------
    #----------

    # Create a list to store available conversation topics
    $ available_topics = []

    # Add topics to the list only if their corresponding variable is True
    if generictalk_work and high_score >= 2:
        $ available_topics.append("work")
    if generictalk_school:
        $ available_topics.append("school")
    if generictalk_life:
        $ available_topics.append("life")
    if generictalk_politics:
        $ available_topics.append("politics")



    if not available_topics:
        # If no topics are available, handle accordingly
        
        # Reset all conversation flags to True to enable retalk after cycle
        $ generictalk_work = True
        $ generictalk_school = True
        $ generictalk_life = True
        $ generictalk_politics = True
        
        # Reset discussion trackers
        $ discussed_work = False
        $ discussed_school = False
        $ discussed_life = False
        $ discussed_politics = False
        $ all_discussed = False
        
        "Conversation runs dry..."
        jump kitchen_talk_end
    else:
        # Randomly select a topic from the available ones
        $ chosen_topic = renpy.random.choice(available_topics)

        # Mark the topic as discussed and jump to the appropriate label
        if chosen_topic == "work":
            $ discussed_work = True
            $ generictalk_work = False
            $ eating_talk_counter+= 1
            jump conversation_work
        elif chosen_topic == "school":
            $ eating_talk_counter+= 1
            $ discussed_school = True
            $ generictalk_school = False
            jump conversation_school
        elif chosen_topic == "life":
            $ eating_talk_counter+= 1
            $ discussed_life = True
            $ generictalk_life = False
            jump conversation_life
        elif chosen_topic == "politics":
            $ eating_talk_counter+= 1
            $ discussed_politics = True
            $ generictalk_politics = False
            jump conversation_politics

label kitchen_events_eatafternoon:
    $ initialize_replay_defaults()
    $ renpy.sound.play("/audio/soun_fx/sizzle.opus", channel="sfx2", loop=False, relative_volume = 0.6)
    "*Pans Sizzling*"
    "A few minutes pass..."
    scene hin_kitchen foodready1 with dissolve:
        yalign 1.0
    show hin_kitchen foodready1:
        easein 4 yalign 0.0
    hin"Food's ready!"
    show screen parallax1280("hin_kitchen foodready1")
    call showscrollingimage from _call_showscrollingimage_177
    him"Is that... onigiri I am smelling?"
    show screen parallax1280("blackscreen") with dissolve
    hin"Oh, [him_name]! Back from the academy?"
    show screen parallax1280("hin_kitchen foodready1_him") with dissolve
    him"My second favorite! Can't wait to dig in!"
    hin"Come, join us! Your [him_rel_to_bo] is here too for once!"
    show screen parallax1280("blackscreen") with vpunch
    him"...M-meh!"
    show screen parallax1280("hin_kitchen table1", zoom=0.82) with dissolve
    hin"Come on [him_name], don't be like that... It's not often us three have lunch together these days!"
    $ generictalk_work = True
    $ generictalk_school = True
    $ generictalk_life = True
    $ generictalk_politics = True
    hin"Let's make the best of it, shall we?"
    $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.6)
    him"Hmph!" with vpunch
    scene black
    call hidescrollingimage("Click twice to start eating.") from _call_hidescrollingimage_108

    jump table_talking_points

#Generic conversations

label conversation_work:
    hin"How's work, [bo_name]?"
    bo"Tiring! Although money's starting to roll in, so I am not complaining!"
    hin"Hmm. Don't burn yourself out for the sake of money thought, alright?"
    hin"And of course, I appreciate you taking up responsibilities and helping out our household!"


    menu:
        "..."
        "Drop your cutlery":
            jump dropcutlery
            
        "Continue the Conversation":
            pass
        
    jump table_talking_points

label conversation_school:
    hin"How's Ninja Academy going for you, [him_name]?"
    him"It's great! Chunin exams are coming up soon, so I am doing my best to prepare for 'em!"
    hin"We can spar together you know! Your [hin_rel] was among the first of her peers to be promoted to Chunin back in my days, you know that?"
    him"Yes mom, you've told us so a million times..."
    hin"*Giggles!*" with vpunch



    menu:
        "..."
        "Drop your cutlery":
            jump dropcutlery
            
        "Continue the Conversation":
            pass

    jump table_talking_points
    
        
label conversation_life:
    hin"So... how are you two holding up?"
    bo"I am managing..."
    him"I am alright. I just wish dad wasn't gone for so long, all the time..."
    bo"What about you, [hin_rel]?"
    hin"Well, you know... I am missing [na_name] too, but..."
    hin"We all know the importance of what he does, right [him_name]?"
    him"Right..."
    hin"Without his appeasement efforts, who knows where we'd stand nowadays..."
    hin"Although I do think it's time for someone else to pick up the mantle of the Hokage!"
    hin"Otherwise, when does a lonely housewife get to enjoy time with her husband, ya know? *Giggles*"

    menu:
        "..."
        "Drop your cutlery":
            jump dropcutlery
            
        "Continue the Conversation":
            pass

    jump table_talking_points

label conversation_politics:
    hin"I wanted you two to know that things seem to be getting a bit heated lately..."
    him"What do you mean Mom? Like... war, and stuff?"
    hin"Hopefully not, but it's best we stay vigilant, alright?"

    menu:
        "..."
        "Drop your cutlery":
            jump dropcutlery
            
        "Continue the Conversation":
            pass

    jump table_talking_points

    

#One time conversations



label conversation_hinata_slipped_banana_slepttogether:
    hin"[bo_name]... Remember that time I slipped when coming out of the bathroom?"
    bo"Y-yeah... W-what about it?"
    hin"To think I am losing my balance to old age... *Sigh*"
    him"You weren't hurt, r-right mama?"
    hin"Of course not! [bo_name] made sure of that. He actually picked me up while I was drowsy and carried me all the way to my bedroom!"
    him"He d-did?"
    hin"Indeed! Such a strong man he is, right? Loving too..."
    hin"But it's probably best that we don't let [him_name] in on that, right [bo_name]?"
    hin"We did have a bit of a moment after that..."
    him"A m-moment? What does that mean...." with vpunch
    hin"*Giggles*! Let's just say that your [him_rel_to_bo] is much more caring than what you give him credit for!" with vpunch
    him"Y-yeah right..."



    menu:
        "..."
        "Drop your cutlery":
            jump dropcutlery
            
        "Continue the Conversation":
            pass

    jump table_talking_points


label conversation_hinata_slipped_banana_usedher:
    hin"[bo_name]... Remember that time I slipped when coming out of the bathroom?"
    bo"Y-yeah... W-what about it?"
    hin"To think I am losing my balance to old age... *Sigh*"
    him"You weren't hurt, r-right mama?"
    hin"Of course not! [bo_name] made sure of that. He was waiting for me to recover for quite some time!"
    bot"Not exactly, I had some fun with you instead [hin_rel]! But it's best you never learn that..."
    

    menu:
        "..."
        "Drop your cutlery":
            jump dropcutlery
            
        "Continue the Conversation":
            pass

    jump table_talking_points

label conversation_hinata_slipped_banana_carriedfail:
    hin"[bo_name]... Remember that time I slipped when coming out of the bathroom?"
    bo"Y-yeah... S-sorry about what happened after!"
    hin"To think I am losing my balance to old age... *Sigh*"
    him"You weren't hurt, r-right mama?"
    hin"Of course not! Although [bo_name] here did try to carry me to my bedroom, but ended up dropping me on the floor... AGAIN! *Giggles*"
    call changeRespect("Himawari", -1) from _call_changeRespect_237
    him"Trying to carry [hin_rel]? With your scrawny build? What are you s-stupid?" with vpunch
    hin"Come on [him_name]! Spare your [him_rel_to_bo] the ridicule! It was a valiant effort, Knightly even!"
    hin"Although it did end up pretty badly I have to say! *Giggles!*"
    bo"*Sigh...*"



    menu:
        "..."
        "Drop your cutlery":
            jump dropcutlery
            
        "Continue the Conversation":
            pass

    jump table_talking_points

label conversation_hinata_slipped_banana_carriedsuccess:
    hin"[bo_name]... Remember that time I slipped when coming out of the bathroom?"
    him"You weren't hurt, r-right mama?"
    hin"Of course not! Your [him_rel_to_bo] here came to my rescue. He picked me up and carried me to my bedroom, can you believe that?"
    him"He d-did?"
    hin"Indeed! Such a strong man he is, right?"
    him"Hmph!" with vpunch
    hin"Thank you [bo_name] that was really nice of you..."
    hin"To think I am losing my balance to old age... *Sigh*"



    menu:
        "..."
        "Drop your cutlery":
            jump dropcutlery
            
        "Continue the Conversation":
            pass

    jump table_talking_points

label conversation_yoru_1st_photoshoot: # True Yoruichi modeling done
    hin"[bo_name]...?"
    bo"...Yes?"
    hin"You still haven't told us about your new... friend!"
    hin"You know, pretty lady, dark skin... purple hair..."
    hin"Me and you [him_rel] are dying to hear more, right [him_name]?"
    him"N-not... r-really!" with vpunch
    hin"*Giggles* So? What is she to you [bo_name]?"
    bo"We are just getting to know one another. Not ready to share gossip yet..."
    hin"Aww, what a shame!"
    hin"Give her our regards next time you see her, okay?"

    menu:
        "..."
        "Drop your cutlery":
            jump dropcutlery
            
        "Continue the Conversation":
            pass

    jump table_talking_points

label conversation_blindfoldrepeat1: #tasted
    him"Did you finish refining your recipe yet [bo_name]?"
    bo"Huh, what recipe?"
    him"The one you had me try the other day, stupid!" with vpunch
    bot"Oh s-shit, she  is probably referring to when she sucked my cock!"
    hin"Oooh? Working on a recipe now are you? Is that for your work at the ramen shop?"
    bo"S-something like that... I had [him_name] give me her opinion a while ago."
    hin"Maybe I can help too if you'd like!" with vpunch
    bo"Eh-eheh! *Nervous Chuckle* M-maybe..."
    bot"I'd love that [hin_rel]! But I don't think you'd be as gullible as [him_name]..."




    menu:
        "..."
        "Drop your cutlery":
            jump dropcutlery
            
        "Continue the Conversation":
            pass

    jump table_talking_points

label conversation_blindfoldrepeat3: #sucked
    him"Hey [bo_name]!" with vpunch
    bo"W-what do you want..."
    him"When will I get to have another taste of your recipe?" with vpunch
    bo"Soon enough, if you behave..."
    bot"Hungry for my cock now, are you little [him_rel]! If only you knew..."
    hin"Me too, me too!"
    bo"W-well, maybe once it's perfected [hin_rel]... *Nervous Chuckle*"
    bot"Absolutely not you, [hin_rel]! You'd be on my case immediately!"



    menu:
        "..."
        "Drop your cutlery":
            jump dropcutlery
            
        "Continue the Conversation":
            pass

    jump table_talking_points

label conversation_highscore1: #went to work at least once
    bo"I got a job recently!"
    hin"Oh yeah, you mentioned something about it before! The ramen shop, right?"
    bo"Yep! I am making some good money too"
    him"We'll see how long that lasts..."
    hin"[him_name]... Your [him_rel_to_bo] is picking up responsibilities. You should be encouraging him, not demeaning him!"
    $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.7)
    him"Hmph!" with vpunch
    hin"So? Met anyone interesting there? Spill the beans!"
    bo"The owner is a bit of a weirdo, and there's a woman too..."
    hin"Oh... A girl? Someone around your age?"
    if yoru_1st_photoshoot == True:
        bo"More like double my age! You met her actually..."
        hin"Oooooh? The pretty purple-haired lady?"
        hin"Me and [him_name] would like to know more about her, you know!"
        him"N-not... r-really!"
        bo"Yeah well, maybe some other time!"
    else:
        bo"Not exactly. I am not too sure about her yet, we haven't spoken much..."
        him"No wonder, who would talk to you anyway... *Teehee!*"
        hin"[him_name]... *Sigh*"




    menu:
        "..."
        "Drop your cutlery":
            jump dropcutlery
            
        "Continue the Conversation":
            pass

    jump table_talking_points

label conversation_talkedaboutmother: #Himawari shopping, talked about debt
    him"[bo_name_stutter]... About the thing we discussed when you took me shopping, should we..."
    "You kick [him_name]'s legs under the table!" with vpunch
    bo"N-no! We said it's confidential, remember?"
    bot"I spilled [hin_rel]'s secret in regards to her financial difficulties to [him_name]. It's best if [hin_rel] doesn't catch wind of that..."
    him"..."
    hin"Oooh? Now I am curious! And did I hear that you two went shopping together?" with vpunch
    bo"Y-yeah. I just wanted to buy [him_name] a little something for her birthday..."
    him"Nothing special moma. Just some cheap clothes!"
    bo"It wasn't cheap at all, you brat..."
    him"Hmph!" with vpunch
    hin"Look at you two! Finally acting like siblings would..."

    menu:
        "..."
        "Drop your cutlery":
            jump dropcutlery
            
        "Continue the Conversation":
            pass

    jump table_talking_points

label conversation_tsunade_discovery_seen: #(Tsunade 1st discovery) 
    hin"[bo_name], how's your check-ups with Lady Tsunade going? Everything alright?"
    bo"You could say that..."
    bot"I don't think I should ever let [hin_rel] or [him_name] know about her most recent discovery!"
    bo"She's been helping a lot. In various ways..."
    hin"I am glad! You should be vigilant with your visits to her, okay? There's no one better when it comes to medicine than her."
    hin"I am sure you'll get better in no time with her help!"
    bo"Oh she's helping alright!"



    menu:
        "..."
        "Drop your cutlery":
            jump dropcutlery
            
        "Continue the Conversation":
            pass

    jump table_talking_points

label conversation_tenten_date_counter1: #(Went on tenten date)
    bo"I met someone recently [hin_rel]. You two might know each other..."
    hin"Ooooh? A new friend? Is it a girl?"
    bo"Remember Tenten from when you were young?"
    hin"Oh y-yes! Faintly, but I do. We used to be in the same academy class when we were little. Ran some missions together too!"
    bo"Well, me and her... we've been getting a bit close lately!"
    hin"*Gasps!* You don't mean..." with vpunch
    hin"She's almost my age, [bo_name]. N-not that there's anything wrong with that, but..."
    bo"Well, she's nice to me, and I think she likes me, so..."
    bo"Nothing wrong with that, right?"
    hin"If she's what makes you happy, then I am happy!"
    him"He is probably just lying mom! What sort of girl would take interest into you anyway!"
    bo"You are just jealous..."
    hin"Tenten was actually quite the looker back then, quite resourceful too!"
    hin"We should plan a meet-up sometime soon!"
    bo"Y-yeah well, we'll see about that."

    menu:
        "..."
        "Drop your cutlery":
            jump dropcutlery
            
        "Continue the Conversation":
            pass

    jump table_talking_points

