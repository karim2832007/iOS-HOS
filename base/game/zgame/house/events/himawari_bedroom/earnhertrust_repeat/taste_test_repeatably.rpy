label repeatable_tastetest:
    show boruto snob with dissolve
    bo"Ready to have another go at the blind taste test?"
    if himawari_respect <= 0:
        him"Oh that..."
        him"No, I am not in the mood for it..." with vpunch
        show boruto surprised2 with dissolve
        bo"W-what? Why... what happened? Don't you want another go at the prize money?"
        call checkRespect(0,"Himawari") from _call_checkRespect_4
        him"Something's telling me that money may not even be real at all... Not to mention how weird you've been acting lately..."
        bo"What? Of course it's real..."
        him"Hmph! Talk to me about it some other time and I might reconsider..."
        show boruto snob with dissolve
        bot"Damn it! So close..."
        show boruto normal with dissolve
        bo"I understand. Don't worry about it, we can go at your pace..."
        him"Mhmm... I'll talk to you later I guess..."
        hide hima with dissolve
        scene black with dissolve
        jump action_taken
    

    else:
        jump repeatable_tastetest_start

label repeatable_tastetest_start:
    
    if blindfoldrepeat == 3:
        show hima shy with dissolve
        him"Oh, that! Did you finally refine your recipe? Can I have another taste?"
        bo"Of course! Your feedback is important to me..."
        bo"In fact, this may be the tastiest my recipe has ever been. Your input has been invaluable, yet again!"
        show hima smugshy with dissolve
        him"Hee-heeee! I told you my palate is cultured! You should be grateful I am lending it to the likes of you... Teehee!"
        bo"I sure am..."
        him"Come on, let's get on with it! Today I am winning the prize for sure!"
        show boruto:
            easein 1 xalign 0.6
        bo"Not so fast! You'll have to put this on first..."
        label replay_blindfoldtaste3:
        $ initialize_replay_defaults()
        scene black with dissolve
        bo"I need a moment to make the necessary preparations..."
        show himablindfold 1_1 with dissolve
        him"Let me know when you are ready!"
        bot"There she goes again..."
        bot"I can't get enough of my innocent little [him_rel] sitting on her knees like that..."
        call increaselust(10) from _call_increaselust_113
        $ renpy.sound.play("/audio/soun_fx/heartbeatlong.opus", channel="sfx2", loop=False, relative_volume = 1.0)
        bot"My heart is already beating like crazy in anticipation..."
        show himablindfold with dissolve:
            alpha 0.2
        show boruto_blindfold_cut with dissolve:
            xpos -0.2 ypos -0.36
        bot"Still so blissfully unaware..."
        hide boruto_blindfold_cut
        show himablindfold:
            alpha 1
        with dissolve
        bo"Alright, you ready?"
        him"Y-yeah!" with vpunch
        bot"This is it... today we are going all the way!"
        scene black with dissolve
        bo"You should face towards me..."
        him"Like this?"
        show screen parallax1280("hima_finalbefore",1.25,0.0) with dissolve
        call showscrollingimage from _call_showscrollingimage_67
        bo"Just like last time, we are skipping straight to the main course..."
        him"Come on, let's get started already!"
        him"*Aaaaah...*"
        call increaselust(10) from _call_increaselust_114
        bo"You seem to be in quite the mood..."
        him"I am ready to win the m-money- *Ahem* I mean... help of course!"
        bo"You little devil..."
        him"Teehee!" with vpunch
        bot"I suppose I am not the only one with devious thoughts..."
        call hidescrollingimage from _call_hidescrollingimage_68

        show hima_drool00 with dissolve:
            xalign 0.0 zoom 0.53
        himt"Today I'll get it right for sure!"
        show hima_finalbefore2 with dissolve:
            ypos -0.50
        $ renpy.sound.play("/audio/soun_fx/heartbeatlong.opus", channel="sfx2", loop=False, relative_volume = 1.0)
        bo"Right... Remember, no biting, and no reaching for it with your hands!"
        him"This odor... I am getting used to its intensity..."
        bo"A-are you now..." with vpunch
        him"Y-yeah! At first it was somewhat unpleasant, but..."
        him"I think I am enjoying it by now..."
        bo"I am s-sure you are..."
        bo"Ready to give it a go?"
        him"Mhm..."
        him"And don't try pulling it away like that other time!" with vpunch
        hide hima_finalbefore2 with dissolve
        bo"R-right..."
        bo"Here it comes...!"
        show hima_drool00:
            alpha 0.20
        show hima_liclharden1:
            xalign 1.0 zoom 0.65 xzoom -1
        with dissolve
        $ renpy.sound.play("/audio/soun_fx/lickpenis1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
        him"Mh...mhm... *Indulgent licks*..."
        call increaselust(10) from _call_increaselust_115
        $ renpy.sound.play("/audio/soun_fx/lickpenis1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
        him"Mmh..."
        show hima_liclharden1 with dissolve:
            xalign 0.0 zoom 0.65 xzoom -1
        show hima_liclharden2 with Dissolve(1):
            xalign 0.0 zoom 0.65 xzoom -1
        $ renpy.sound.play("/audio/soun_fx/lickpenis1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
        him"Mh...mhm... *Indulging licks*..."
        him"It's... It's tastier than before!"
        bo"Y-yeah... thanks to y-your feedback..."
        call increaselust(10) from _call_increaselust_116
        himt"But I still have no clue what it might be..."
        bot"F-fuck, I am getting hard as a rock feeling her tongue circling around the glans..."
        himt"I only know that..."
        $ renpy.sound.play("/audio/soun_fx/lickpenis1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
        himt"...I want to taste more of it!" with vpunch
        him"Mh...mhm... *Indulging licks*..."
        bot"But I need to h-hold on a little while longer!"
        scene black with fade
        show hima_liclharden3:
            xalign 0.0 zoom 0.65 xzoom -1
        with dissolve
        him"It got... warmer, thicker too I t-think, much faster than before..."
        him"Is that because of your refinement after my feedback?"
        bo"Y-you bet..."
        bot"F-fuck! I am rock hard! Looking down at her gazing towards my cock..."
        call increaselust(10) from _call_increaselust_117
        bot"I could use a b-break... Otherwise I might get off before the f-fun even begins!"
        him"...In that case, can I have a proper taste now?" with vpunch
        bo"S-sure, but first..."
        scene black with vpunch
        him"Come on already..."
        show himavid with dissolve:
            xalign 0.0 zoom 1
        him"Are you t-teasing me? Hurry it up... *Aaaaahhh...*"
        menu repeatableblindfoldmenufinal:
            him"Are you t-teasing me? Hurry it up... *Aaaaahhh...*"
            "Give her what she asked for...":
                scene black with dissolve
                bo"As you wish..."
                show hima_start1_1 with dissolve:
                    xalign 0.5 zoom 1.1 yalign 1.0
                show hima_start1_1:
                    easein 5 yalign 0.0
                "[him_name] leaned forward, ready for another taste..."
                scene black with dissolve
                show hima_deny1 with dissolve:
                    xalign 0.15 zoom 0.53
                $ renpy.sound.play("/audio/soun_fx/lickpenis1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                bot"She's willingly slurping up my cum drip..."
                him"Mmm... It t-tastes..."
                show hima_deny1:
                    alpha 0.2
                show hima_deny2:
                    xalign 0.85 zoom 0.53
                with dissolve
                him"...N-nicer than before!"
                him"It's growing on me, I think..." with vpunch
                bot"My cock is t-throbbing right above her face... My cum is dripping all over her face!"
                him"Careful though! Y--you are spilling some of it on me..." with vpunch
                bo"S-sorry, it can get a bit m-messy! But maybe..."
                bo"You could prevent that by giving it a proper taste..."
                bo"I won't pull it b-back this time..."
                $ renpy.sound.play("/audio/soun_fx/lickpenis1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                scene black with flash
                him"...I was planning on it!" with vpunch
                $ renpy.sound.play("/audio/soun_fx/suck2.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                bot"Oh f-fuck! M-my little [him_rel]..." with vpunch
                show hima_deny3 with flash:
                    zoom 1.5 xalign 0.5 yalign 0.6
                $ renpy.sound.play("/audio/soun_fx/suck1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                show hima_deny3 with flash:
                    zoom 1.5 xalign 0.5 yalign 0.4
                bot"S-she's..."
                $ renpy.sound.play("/audio/soun_fx/suck3.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                show hima_deny3 with flash:
                    zoom 1.5 xalign 0.5 yalign 0.2
                bot"[him_name]'s s-sucking on my..." with flash
                $ renpy.sound.play("/audio/soun_fx/suck2.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                show hima_deny3 with flash:
                    zoom 1.5 xalign 0.5 yalign 0.0
                bo"*Silent moan* Y-you are squeezing the s-syrup out of it..." with flash
                bot"Hngh... I am a-about... to fill h-her mouth w-with..."
                himt"O-oh? I see now! The more I suck on it..." with vpunch
                $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                scene black with flash
                call decreaselust(50) from _call_decreaselust_80
                show hima_repeat1 with flash:
                    xalign 0.5
                $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                himt"...The more the s-syrup is that comes out!"
                $ renpy.sound.play("/audio/soun_fx/swallow.opus", channel="sfx2", loop=False, relative_volume = 1.4)
                him"*Gulp*... And the taste of it is..."
                $ renpy.sound.play("/audio/soun_fx/swallow.opus", channel="sfx2", loop=False, relative_volume = 1.4)
                bot"D-did she just... F-fuck! T-there's more c-coming!" with flash
                $ renpy.sound.play("/audio/soun_fx/cum11.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                show hima_repeat1 with flash:
                    xalign 0.0 zoom 0.6
                call decreaselust(50) from _call_decreaselust_81
                $ renpy.sound.play("/audio/soun_fx/swallow.opus", channel="sfx2", loop=False, relative_volume = 1.4)
                him"*Gulp*..."
                $ renpy.sound.play("/audio/soun_fx/pop.mp3", channel="sfx2", loop=False, relative_volume = 1.0)
                show hima_repeat1 with dissolve:
                    alpha 0.3
                show hima_drool3 with flash:
                    xalign 1.0 zoom 0.7 yalign 1.0
                $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                show hima_drool3:
                    easein 6 yalign 0.35
                "With a soft groan, you pulled away as silently as you could, holding in your ragged breath so as to not give yourself away..."
                "Your release flooded her mouth, leaving behind strands of semen dripping down from her soft, wet lips..."
                bot"Did I j-just... empty my balls in my [him_rel]'s mouth!?" with vpunch
                "[him_name] was left wondering what just transpired. The deafening silence, along with the strong odor of your semen filling the entire room left her perplexed..."
                scene black with dissolve
                "More than perplexed, she seemed..."
                show hima_cumtaste1 with dissolve:
                    zoom 1.2 xalign 0.5 yalign 1.0
                "intrigued!...Evident by her efforts to gather what little of what she thought was your special 'syrup' that spilled across her face..."
                show hima_cumtaste2 with dissolve:
                    zoom 1.2 xalign 0.5 yalign 1.0
                "She scooped up the strands of semen from her face, and with her delicate fingers she pushed it all right onto her tongue to properly taste..."
                $ renpy.sound.play("/audio/soun_fx/swallow.opus", channel="sfx2", loop=False, relative_volume = 1.4)
                show hima_cumtaste3 with dissolve:
                    zoom 1.2 xalign 0.5 yalign 1.0
                him"*Gulp*... I knew it!" with vpunch
                scene black with vpunch
                bo"Y-you knew what exactly...?" with vpunch
                show himablindfold 1_1 with dissolve
                him"I may know exactly what that was!" with vpunch
                bo"Do you now...?"
                bot"There's no way she'd be this calm if she did..."
                him"I am sure of it!" with vpunch
                him"But I am not telling until I can get this blindfold off! I want to watch the panic settle in on you as I siphon your money!"
                him"Hee-hee-heee!" with vpunch
                bo"You sly d-devil... Give me a second to c-clean up and hide all my s-stuff before you do that!"
                scene black with dissolve
                "You quickly got rid of all the 'evidence' while [him_name] patiently awaited for your call..."
                bo"You can take it off now..."
                if day_part == 3:
                    show himawari_bedroom_2
                else:
                    show himawari_bedroom_1
                show hima smugshy at right:
                    zoom 0.34
                with dissolve
                show boruto surprised2 at left with dissolve
                him"Hee-heee.... "
                "Without wasting a second, [him_name] took off the blindfold, revealing her mischievous expression..."
                bo"So... Do you actually know what that was?"
                show hima at smallshake
                him"I k-know exactly what that was!" with vpunch
                bo"Y-you do...?"
                show hima at smallshake
                him"Of course!"
                show hima at smallshake
                him"It was..."
                bo"...?"
                show hima worried2 with dissolve
                him"It w-was..."
                show boruto snob with dissolve
                bot"She has absolutely no idea..."
                show hima at smallshake
                bo"It w-was a... a...-"
                bo"Come on, just give up already..."
                show hima embarassed with dissolve
                him"I have no c-clue what that was! P-please..."
                show hima at smallshake
                him"Can't you just t-tell me?"
                show hima worried2 with dissolve
                show boruto at smallshake
                bo"Bwahaha! I can't do that of course..."
                him"C-come on, p-please? I just want to know..."
                him"The curiosity is killing me!" with vpunch
                bo"You know I can't do that. It defeats the purpose of the test..."
                bo"Besides don't you want another shot at the prize money?"
                show hima at smallshake
                him"I do! But... I also want to know what that was!"
                him"The taste is kinda growing on me..."
                him"A little more refinement and this could easily make my top three favorite snack list!"
                show boruto surprised2 with dissolve
                bo"Y-your favorite s-snack list, h-huh...?"
                show boruto snob with dissolve
                bo"Was it that good...?"
                show hima smug2 with fade
                him"Don't let it stroke your ego! It's only as good as it is because of me!" with vpunch
                show boruto normal with dissolve
                bo"I'll give it to you, your feedback was... helpful!"
                show boruto snob with dissolve
                bot"Might as well let her have this one..."
                show hima at smallshake
                him"You bet! You should be glad I am lending my palate to the likes of you..."
                show boruto embarassed with dissolve
                bo"Heh-he... What would I ever do without you..."
                show hima smugshy with dissolve
                him"Hmph! Maybe you should pay me a royalty fee whenever you put that out at that restaurant you work at..."
                show boruto snob with dissolve
                bo"Don't get ahead of yourself, [him_name]..."
                bo"It's still my recipe you know..."
                show hima shy with dissolve
                him"I know, I know! B-but really..."
                him"How did you... come up with that?"
                him"The taste somehow keeps getting more and more intense..."
                him"It was similar to a popsicle, as you previously mentioned. But instead of slowly losing its flavor like a popsicle would..."
                him"It worked the complete opposite way! The intensity of it only grew and grew, up until I managed to somehow squeeze whatever that s-syrup was out of it..." with vpunch
                him"That explosion of fragnance after s-sucking on it for a while... it was... incredible!"
                him"The after-taste is stuck on my mind... I want m-more..."
                him"The most puzzling thing is that... I have never tasted anything similar before!"
                show boruto embarassed with dissolve
                bo"*Nervous laughter* Ha...ha-ha... W-what can I say... Trade secrets!" with vpunch
                show boruto surprised3 with dissolve
                bot"H-holy s-shit! My bratty, little [him_rel] just tasted me in the most intimate of ways and... and..."
                bot"S-she says she wants m-more!? Is she... getting addicted to the taste of my cum!?" with vpunch
                show hima worried2 with dissolve
                bot"What the fuck is going on!"
                show hima at smallshake
                him"...S-so?" with vpunch
                him"Why are you standing there saying nothing! You look kinda flushed too..." with vpunch
                show boruto embarassed with dissolve
                bo"F-flushed!? No! Just surprised..."
                bo"I never thought I could come up with something that would satisfy your appetite..."
                show boruto snob with dissolve
                bo"I am glad I did, and I am happy you were the one to help me do it!"
                him"Y-you are welcome..."
                call changeRespect("Himawari",2) from _call_changeRespect_165
                him"I am also glad you v-valued my opinions for once."
                him"I always t-thought you never paid attention to me or what I had to say..."
                show boruto surprised2 with dissolve
                bo"You know that's not true!"
                bo"I mean, look at what we've achieved together..."
                bo"I would never be able to improve my recipe if it weren't for you..."
                him"I g-guess so..."
                show boruto snob with dissolve
                bo"Perhaps it's time we both started trusting each other a little bit more..."
                show hima at smallshake
                him"M-maybe so... I'll consider that!"
                bo"Hmm..."
                bo"That settles it then!" with vpunch
                him"S-settles what exactly?"
                bo"We are done for today, but... From now on, you are to be my trusted assistant!"
                bo"I'll keep working on things and I'll be coming to you whenever I am in need of your opinion..."
                bo"Would you be willing to fulfil that role?"
                him"Your... trusted a-assistant, huh..."
                show hima smugshy with dissolve
                him"I am tempted, even more so if there is something in it for me! Teehee!" with vpunch
                him"But if it means I get to have another taste of... whatever t-that is sometime soon, then I am in!"
                bo"You bet!"
                him"Yahoo! Can't wait!" with vpunch
                show boruto:
                    easein 1.5 xpos -800
                bo"I'll see you around..."
                scene black with dissolve
                bot"To think my stupid ploy would work this well..."
                bot"Maybe she'd be more comfortable with the modelling thing now..."
                $ renpy.end_replay()
                default blindfoldfinished = False
                $ blindfoldfinished = True
                $ blindfoldrepeat = 3
                jump action_taken
                

                
            "{color=[obediencecolor]}Toy with her...{/color}":
                bot"Looking at her like that..."
                show boruto naked3 at dizzyflashshort:
                    zoom 0.8 xpos 0.41 yalign 1.0
                with dissolve
                bot"She gets me excited! I get this urge to toy around with her..."
                menu hima_toyaround:
                    bot"She gets me excited! I get this urge to toy around with her..."
                    "{color=[obediencecolor]}Jerk off in front of her...{/color}" if himatest1 <3:
                        default himatest1 = 0
                        $ himatest1 +=1
                        if himatest1 == 1:
                            bot"How can I resist this beautiful sight..."
                            hide boruto with dissolve
                            show hima_start1_1 with dissolve:
                                zoom 0.6 xalign 1.0
                            $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                            show hima_start1_2 with dissolve:
                                zoom 0.6 xalign 1.0
                            call increaselust(10) from _call_increaselust_118
                            show hima_drool2_shy with dissolve:
                                xalign 0.0 yalign 0.3 zoom 0.52
                            hide hima_start1_2
                            hide hima_start1_1
                            with dissolve
                            him"W-what's taking so long, and..."
                            him"What's that weird slimy sound I am hearing..." with vpunch
                            $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                            show cutout_bo2 with dissolve:
                                xalign 1.0 yalign 0.0
                            bo"Some last minute p-preparations... Don't worry about that!"
                            hide cutout_bo2
                            show hima_drool1:
                                xalign 0.0 yalign 0.3 zoom 0.52
                            with dissolve
                            him"Oh, adding glazing or something...?"
                            $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                            bo"S-something like that..."
                            him"Come on... H-hurry it up already!"
                            hide hima_drool1
                            hide hima_drool2_shy
                            with dissolve
                            show boruto naked3 with dissolve:
                                zoom 0.8 xpos 0.41 yalign 1.0
                            jump hima_toyaround
                        elif himatest1 == 2:
                            bo"Just a little w-while longer, [him_name]..."
                            hide boruto with dissolve
                            $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                            show hima_start1_2 with dissolve:
                                zoom 0.6 xalign 1.0
                            call increaselust(10) from _call_increaselust_119
                            show hima_drool2_shy with dissolve:
                                xalign 0.0 yalign 0.3 zoom 0.52
                            hide hima_start1_2
                            hide hima_start1_1
                            with dissolve
                            show hima_drool2_shy with dissolve:
                                xalign 0.0 yalign 0.3 zoom 0.52
                            him"I am g-growing impatient! C-come on..."
                            $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                            himt"That weird sound again..."
                            show cutout_bo2 with dissolve:
                                xalign 1.0 yalign 0.0
                            bo"I'll be... right t-there with you soon..."
                            hide cutout_bo2
                            show hima_drool1:
                                xalign 0.0 yalign 0.3 zoom 0.52
                            with dissolve
                            himt"What could be taking him so long..."
                            hide hima_drool1
                            hide hima_drool2_shy
                            with dissolve
                            show boruto naked3 with dissolve:
                                zoom 0.8 xpos 0.41 yalign 1.0
                            jump hima_toyaround

                        elif himatest1 == 3:
                            bo"[him_name]..."
                            hide boruto with dissolve
                            $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                            show hima_start1_2 with dissolve:
                                zoom 0.6 xalign 1.0
                            call increaselust(10) from _call_increaselust_120
                            show hima_drool2_shy with dissolve:
                                xalign 0.0 yalign 0.3 zoom 0.52
                            hide hima_start1_2
                            hide hima_start1_1
                            with dissolve
                            show hima_drool2_shy with dissolve:
                                xalign 0.0 yalign 0.3 zoom 0.52
                            him"Huh? What is it..."
                            $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                            bo"*Silent moan*... Are you ready for it?"
                            him"Y-yeah!"
                            himt"It keeps going and going..."
                            himt"I get this urge to peek under the b-blindfold..."
                            himt"My curiosity is killing me... Maybe..."
                            call changeObedience("Himawari",1,"himatest1",2) from _call_changeObedience_97
                            himt"N-no! I can't do that... That would be c-cheating!" with vpunch
                            show cutout_bo3 with dissolve:
                                xalign 1.0 yalign 0.0
                            bo"It s-hould be ready now, sorry for the wait..."
                            hide cutout_bo3
                            show hima_drool1:
                                xalign 0.0 yalign 0.3 zoom 0.52
                            with dissolve
                            him"F-finally... Bring it on!"
                            hide hima_drool1
                            hide hima_drool2_shy
                            with dissolve
                            show boruto naked3 with dissolve:
                                zoom 0.8 xpos 0.41 yalign 1.0
                            bot"I don't think I can jerk off any longer, otherwise I'll bust on the spot!"
                            jump hima_toyaround

                    "{color=[obediencecolor]}Test her throat's capacity...{/color}" if himatest2 == False:
                        default himatest2 = False
                        $ himatest2 = True
                        if hima_throatgoat == True:
                            bot"I've already put her to the test before, but..."
                            bot"I am dying to find out if my theory about her... abilities, is true!" with vpunch
                        else:
                            pass
                        scene black with dissolve
                        bo"*Ahem*... Before we continue, there's something I need to confirm..." with vpunch
                        show hima_finalbefore_angry with dissolve:
                            zoom 1.2 yalign 0.7 xalign 0.5
                        show hima_finalbefore_angry:
                            easein 4 yalign 0.1
                        him"...Huh? C-confirm what?"
                        bo"You see, my recipe is best enjoyed in its entirety..."
                        bo"For that to happen, one must be capable of..."
                        show hima_banana1 with dissolve:
                            zoom 1.2 yalign 0.7 xalign 0.5
                        show hima_banana1:
                            easein 2 yalign 0.1
                        $ renpy.sound.play("/audio/soun_fx/hima_gag.opus", channel="sfx2", loop=False, relative_volume = 1.2)
                        bo"...At least this much!" with vpunch
                        $ renpy.sound.play("/audio/soun_fx/hima_gag2.opus", channel="sfx2", loop=False, relative_volume = 1.2)
                        him"*Huuk!*" with vpunch
                        "The sudden oral intrusion caught [him_name] by surprise, but she seemed to maintain her composure..."
                        if hima_throatgoat == False:
                            bot"Holy S-shit... She is handling it fairly well! Not even an audible gag..."
                        else:
                            bot"Not even an audible gag... Just as I thought!"
                        bot"My little [him_rel] might have talents beyond her comprehension..."
                        $ hima_throatgoat = True
                        scene black with vpunch
                        $ renpy.sound.play("/audio/soun_fx/hima_gag2.opus", channel="sfx2", loop=False, relative_volume = 1.2)
                        him"*Gasps* H-hey...!" with vpunch
                        show hima_drool3 with dissolve:
                            xalign 0.0 zoom 0.53
                        "You pulled the banana out of her throat, leaving behind a sloppy mess..."
                        call checkObedience(15,"failbanana","Himawari") from _call_checkObedience_15
                        him"W-what was that for!"
                        bo"I told you... I had to run a quick test by you..."
                        show hima_drool3 with dissolve:
                            alpha 0.2
                        show hima_drool2_shy with dissolve:
                            xalign 1.0 zoom 0.53
                        him"What kind of test is putting a banana in my mouth in the first place..."
                        bo"*Ahem* You see...-" with vpunch
                        call changeObedience("Himawari",1,"throatgoat",2) from _call_changeObedience_98
                        him"...Well? D-did I pass?" with vpunch
                        bo"...With flying colors!"
                        bo"You'll certainly be able to handle my recipe without breaking a sweat!"
                        him"Hmm..."
                        him"I guess I should be glad about it t-then..."
                        show hima_drool1 with dissolve:
                            xalign 1.0 zoom 0.53
                        him"Come on! Let's get on w-with it then..."
                        scene black with dissolve
                        show boruto naked3 with dissolve:
                            zoom 0.8 xpos 0.41 yalign 1.0
                        bot"She really has no gag reflex or something..."
                        bot"In that case, maybe..."
                        show himavid with dissolve:
                            xalign 0.0 zoom 1
                        jump hima_toyaround

                        label failbanana:
                        show hima_drool2_angry with dissolve:
                            xalign 1.0 zoom 0.53
                        him"W-what the hell was that for!" with vpunch
                        bo"I t-told you... I had to confirm your capabilities..."
                        call changeRespect("Himawari", -2) from _call_changeRespect_166
                        him"Don't just s-shove things in my mouth you d-damned imbecile!" with vpunch
                        him"You k-keep trying stupid things and I'll shove this blindfold up your bum..."
                        him"And steal your money too while I am at it!" with vpunch
                        him"...You g-got it!?"
                        bo"R-right, right... I am sorry!"
                        show hima_drool2_angry with dissolve:
                            alpha 0.2
                        show hima_drool1 with dissolve:
                            xalign 1.0 zoom 0.53
                        him"N-now hurry up and give me t-the real thing! Not the f-freaking banana!"
                        bo"A-as you command..."
                        scene black with dissolve
                        show boruto naked3 with dissolve:
                            zoom 0.8 xpos 0.41 yalign 1.0
                        bot"Little does she know..."
                        show himavid with dissolve:
                            xalign 0.0 zoom 1
                        jump hima_toyaround



                    "{color=[obediencecolor]}Make her act like a pet...{/color}" if himatest3 == False:
                        default himatest3 = False
                        $ himatest3 = True
                        bo"Before we get on with it, I was thinking..."
                        bo"I wanted to test how strong the scent my recipe omits is..."
                        bo"Do you think you can spot where I am just by the trailing... aroma?"
                        scene black with dissolve
                        show hima_drool2_shy with dissolve:
                            xalign 0.5 zoom 0.53
                        him"I b-bet I could do that easily!"
                        bo"Are you sure about that? Why don't you try crawling towards the odor then..."
                        scene black with dissolve
                        him"...Easy!"
                        scene hima_crawl2 with dissolve
                        him"It comes from..."
                        call checkObedience(18,"crawlfailhima","Himawari") from _call_checkObedience_16
                        scene hima_crawl1 with dissolve
                        him"*Sniff Sniff*"
                        himt"That odor... It's... so strong..."
                        scene black
                        show hima_crawl3
                        with dissolve
                        call changeObedience("Himawari",1,"crawlhimatest",1) from _call_changeObedience_99
                        him"...This way!" with vpunch
                        call increaselust(10) from _call_increaselust_121
                        bot"F-fuck, that's so hot! [him_name] on all fours, her tank top's strap barely hanging on..."
                        scene black
                        show hima_crawl
                        with dissolve
                        bot"Her cute little titties are almost in sight!" with vpunch
                        him"It's... right around here, isn't it?"
                        menu:
                            him"It's... right around here, isn't it?"
                            "Encourage her":
                                show hima_crawl with dissolve:
                                    alpha 0.2
                                show boruto naked3 with dissolve:
                                    zoom 0.8 xpos 0.41 yalign 1.0
                                bo"Almost there..."
                                bo"Keep it up!"
                                hide boruto
                                show hima_crawl:
                                    alpha 1.0
                                with dissolve
                                call changeRespect("Himawari", -1) from _call_changeRespect_167
                                him"Your voice is giving it away you idiot!" with vpunch
                                scene black with dissolve
                                bo"Oops! My bad..." with vpunch
                                him"It's..."
                                show hima_crawl2_1 with dissolve
                                him"It's right here, isn't it?"
                            
                            "Stay silent while thinking about her...":
                                bot"..."
                                bot"My little [him_rel] on all fours, crawling towards my dripping cock, completely unbeknownst to her..."
                                call increaselust(10) from _call_increaselust_122
                                bot"How can I not be aroused by the sight!"
                                bot"She is just so easy to toy around with..."
                                bot"I kind of feel-"
                                scene black with vpunch
                                him"R-right here..."
                                show hima_crawl2_1 with dissolve
                                him"...Isn't it?"
                            "Ask her to bark like a puppy!":
                                bo"Look at you going! like a little excited puppy!"
                                bo"Maybe you could bark for me too while you are at it!"
                                call changeRespect("Himawari", -1) from _call_changeRespect_168
                                him"S-shut up you god-damned idiot! I am not your pet!" with vpunch
                                scene black with vpunch
                                him"Your voice also gave it away!" with vpunch
                                call changeRespect("Himawari", -1) from _call_changeRespect_169
                                him"*Groans* Y-you are so stupid! Sucked the fun out of it..." with vpunch
                                scene black with dissolve
                                bo"You are r-right. I am sorry..." with vpunch
                                $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                him"Hmph!" with vpunch
                                show hima_crawl2_1 with dissolve
                                him"It's right here, isn't it?"
                            "{color=[obediencecolor]}Tease her playfully!{/color}":
                                bo"You are really getting into this, aren't you?"
                                bo"Almost like an excited little puppy!"
                                call checkObedience(20,"crawlfailhima2","Himawari") from _call_checkObedience_17
                                him"Like a p-puppy... huh?"
                                show hima_crawl2_1 with dissolve
                                him"Then..."
                                show hima_crawl2_2 with dissolve:
                                    zoom 1.3 xalign 1.0 yalign 0.0
                                him"*Wharf Wharf*!" with vpunch
                                bo"[him_name]... what are you-"
                                show hima_crawl2_2 with dissolve:
                                    zoom 1.4 xalign 1.0 yalign 0.0
                                him"*Wharf!* Can I have my food please... master?"
                                call increaselust(100) from _call_increaselust_123
                                bot"I can't anymore... I am about to fucking explode!"
                                scene black with vpunch
                                $ renpy.sound.play("/audio/soun_fx/himawari/loserlaugh.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                                him"Teehee~!" with vpunch
                                "[him_name] burst into playful giggles..."
                                show cutout_bo1 with dissolve:
                                    yalign 0.3 xalign 0.5
                                him"Bwahaha! I can practically see your stupid embarassed face!"
                                him"What's wrong! Cat got your tongue?" with vpunch
                                bo"You sly little p-puppy..."
                                show cutout_bo2 with dissolve:
                                    yalign 0.3 xalign 0.5
                                bo"I am not embarassed at all, quite the opposite..."
                                scene hima_crawl2_1 with dissolve 
                                bot"You might have awakened something in me!" with vpunch
                                call changeObedience("Himawari",1) from _call_changeObedience_100
                                him"The opposite? W-what does that even mean. Did you find that f-funny or something? Weirdo..."
                                him"N-nevermind all that!" with vpunch
                                him"This odor... It's right in front of me, isn't it?"
                                jump test678




                                label crawlfailhima2:
                                call changeRespect("Himawari", -1) from _call_changeRespect_170
                                him"Shhhh!"
                                him"Your voice is giving it away you idiot!" with vpunch
                                scene black with dissolve
                                bo"Oops! My bad..." with vpunch
                                him"It's..."
                                show hima_crawl2_1 with dissolve
                                him"It's right here, isn't it?"
                            
                        



                        label test678:
                        bo"You are exactly right..."
                        him"I knew it! The smell is way too telling..."
                        bo"G-good girl..."
                        him"Hmph! Can I finally taste it now...?" with vpunch
                        bo"S-sure... Scooch a little closer first..."
                        show hima_crawl2_2 with dissolve:
                            zoom 1.3 xalign 1.0 yalign 0.0
                        him"*Aaaaah...*"
                        call increaselust(10) from _call_increaselust_124
                        bot"G-gods..."
                        scene black with dissolve
                        show boruto naked3 with dissolve:
                            zoom 0.8 xpos 0.41 yalign 1.0
                        bot"I can't hold back anymore..."
                        show himavid with dissolve:
                            xalign 0.0 zoom 1
                        jump hima_toyaround

                        jump hima_toyaround

                        label crawlfailhima:
                        show hima_crawl1 with dissolve
                        him"Wait a second..."
                        bo"Huh? W-what's wrong..."
                        scene black with vpunch
                        him"Y-you... w-weirdo!" with vpunch
                        show hima_drool2_angry with dissolve:
                            xalign 0.0 zoom 0.53
                        him"I am not about to crawl on the floor like some dog while you sit there and watch!" with vpunch
                        call changeRespect("Himawari", -2) from _call_changeRespect_171
                        him"You t-tried to trick me into doing that, didn't you!?"
                        bo"W-what? Of course not..." with vpunch
                        him"Sure you didn't... I could sense your creepy smirk even with the blindfold on..."
                        him"You weirdo!" with vpunch
                        bo"W-whatever you say..."
                        show hima_drool2_shy with dissolve:
                            xalign 0.0 zoom 0.53
                        hide hima_drool2_angry
                        $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                        him"Hmph! Idiot..." with vpunch
                        show hima_drool2_shy with dissolve:
                            alpha 0.2
                        show hima_drool1 with dissolve:
                            xalign 1.0 zoom 0.53
                        him"N-now hurry up and get to the real thing! I am tired of your stupid shenanigans..."
                        bo"A-as you wish..."
                        scene black with dissolve
                        show boruto naked3 with dissolve:
                            zoom 0.8 xpos 0.41 yalign 1.0
                        bot"F-fuck... I'll try that again when she gets a little bit more into it..."
                        show himavid with dissolve:
                            xalign 0.0 zoom 1
                        jump hima_toyaround
                        


                    "Return":
                        jump repeatableblindfoldmenufinal
                    
                jump repeatableblindfoldmenufinal


            "{color=[hatredcolor]}Indulge her with disregard!{/color}"(secrethatred = True) if blindfoldfull == True and hatred >= 30 and percentage >= 80:
                if v17_update == True:
                    pass
                else:
                    $ notification("Exclusive supporters scene")
                bo"...As you wish!" with vpunch
                $ blindfoldfinished = True
                label replay_blindfoldtaste_hate:
                $ initialize_replay_defaults()
                scene black with dissolve
                show hima_start1_1 with dissolve:
                    xalign 0.5 zoom 1.1 yalign 1.0
                show hima_start1_1:
                    easein 5 yalign 0.0
                bo"I'll not be the one to deprive you of what you crave..."
                him"*A-aaahh...*"
                "[him_name] leaned forward, ready for another taste..."
                bot"Look at her fucking face! Dripping with excitement..."
                show hima_start1_2 with dissolve:
                    xalign 0.5 zoom 1.15 yalign 0.0
                bot"How can I resist shoving it in there!" with vpunch
                bo"Today, I am thinking I'll reveal a secret to you..."
                scene black with dissolve
                show hima_deny2 with dissolve:
                    xalign 0.15 zoom 0.53
                him"A... s-secret?" with vpunch
                "You let your cum-dripping cock hanging right above [him_name] as you looked down on her, imagining what it would look like inside of her..."
                himt"I can smell it, he is holding it right above m-me..."
                bo"A secret, yes!"
                bo"You see..."
                show hima_repeat1:
                    xalign 0.85 zoom 0.6
                show hima_deny2:
                    alpha 0.2
                with dissolve
                "You pushed the tip inside her mouth..."
                bo"The more suction one applies to my recipe..."
                $ renpy.sound.play("/audio/soun_fx/hima_gag.opus", channel="sfx2", loop=False, relative_volume = 1.2)
                show hima_repeat2 with dissolve:
                    xalign 0.85 zoom 0.6
                bo"The more syrup one can extract from it!"
                "You grabbed the top of her head and lightly pushed her towards you, forcing most of the shaft inside her mouth..."
                bo"See if you can squeeze all of the... syrup out with just your mouth!" with vpunch
                scene black
                $ renpy.sound.play("/audio/soun_fx/hima_gag2.opus", channel="sfx2", loop=False, relative_volume = 1.2)
                show hima_repeat2 with flash:
                    zoom 1.2 xalign 0.5 yalign 0.0
                pause 0.2
                show hima_repeat2 with flash:
                    zoom 1.4 xalign 0.5 yalign 1.0
                pause 0.4
                show hima_repeat2:
                    easein 5 yalign 0.05
                himt"T-that idiot! He thinks he can..."
                $ renpy.sound.play("/audio/soun_fx/hima_gag.opus", channel="sfx2", loop=False, relative_volume = 1.2)
                him"Mmmhhm..." with vpunch
                himt"P-put his hands on me..."
                himt"But the taste is... He is r-right!"
                bot"F-fuck! The back of her throat feels even better than her t-tongue!"
                bot"I can't believe I have my rock-hard cock half buried in my [him_rel]'s mouth. The best p-part is..."
                bot"She has no fucking idea! To top it all off..." with vpunch       
                bot"This little brat's throat seems unbothered by my s-size...!"
                call changeHatred(1) from _call_changeHatred_119
                bot"[him_name], you little bitch... I never knew you were as talented as you are!"
                bot"You keep this up any longer and I'll-"
                $ renpy.sound.play("/audio/soun_fx/pop.mp3", channel="sfx2", loop=False, relative_volume = 1.0)
                $ renpy.sound.play("/audio/soun_fx/gaspforair1.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                scene black
                show hima_deny2 with flash:
                    xalign 0.1 zoom 0.53
                "[him_name] pulled away in mild frustration..."
                show cutout_bo1 with dissolve:
                    xalign 0.9 yalign 0.5
                him"H-hey you a-asshole! Who s-said you can push on my h-head like that..." with vpunch
                bo"I was only t-trying to help... Will you relax?"
                $ renpy.sound.play("/audio/soun_fx/himawari/himascoff1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                him"Hmph! Just... let me have a go at it at my leisure..." with vpunch
                show cutout_bo2 with dissolve:
                    xalign 0.9 yalign 0.5
                him"Although I admit, you weren't lying..."
                him"It was more... intense like that. It was almost as if it were pulsating inside my mouth..."
                him"And it kept releasing more and more of that s-syrup..."
                show cutout_bo3 with dissolve:
                    xalign 0.9 yalign 0.5
                bo"...R-right?"
                call changeHatred(1) from _call_changeHatred_120
                bot"Such a brainless cum-slut..."
                show hima_finalbefore with dissolve:
                    zoom 1.3 xalign 0.5 yalign 0.8
                show hima_finalbefore:
                    easein 3 yalign 0.0
                bot"And a sexy little vixen..." with vpunch
                bot"Her innocence only makes this more enticing!"
                menu:
                    bot"Her innocence only makes this more enticing!"
                    "{color=[hatredcolor]}Degrade her!{/color}":
                        bo"It released syrup, huh...?"
                        him"Mhm!" with vpunch
                        $ renpy.sound.play("/audio/soun_fx/growl1.opus", channel="sfx3", loop=False, relative_volume = 0.9)    
                        show kurama1 with flash
                        show kurama1:
                            easein 2 alpha 0.0
                        bot"I get this extreme urge to d-degrade her..."
                        bot"Just looking at her... My little [him_rel] is just..."
                        call changeHatred(1) from _call_changeHatred_121
                        bot"She's just such a dumb little slut!" with vpunch
                        bo"Yeah, the syrup can spout out at any moment!"
                        "You pooled up your saliva and planned on silently spitting it out across her face, pretending to accidentely spill more of the 'syrup' on her..."
                        $ renpy.sound.play("/audio/soun_fx/spit1.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                        show spitfx1:
                            zoom 1.1 xalign 0.5 yalign 0.05
                        show spitmark1:
                            xalign 0.62 yalign 0.22 zoom 0.15
                        with dissolve and flash
                        show hima_finalbefore_angry:
                            zoom 1.3 xalign 0.5 yalign 0.0
                        hide spitfx1
                        show spitmark1 zorder 1:
                            xalign 0.62 yalign 0.25 zoom 0.15 alpha 0.6
                        with dissolve
                        him"H-hey, what the heck was that, careful!" with vpunch
                        bo"Oops, sorry! My bad..." with vpunch
                        him"Don't just s-spill it on me, idiot!" with vpunch
                        bot"You look even better with my spit on your face, you bitch!" with vpunch
                        show blackscreen
                        hide spitmark1
                        hide spitfx1
                        with dissolve
                        him"Hmph! You d-dummy..." with vpunch
                        show hima_cumtaste1 with dissolve:
                            zoom 1.2 xalign 0.5 yalign 1.0
                        "[him_name] slid her fingers across her face and scooped up your saliva, tasting it in the process..."
                        show hima_cumtaste2 with dissolve:
                            zoom 1.2 xalign 0.5 yalign 1.0
                        him"Is this really the s-same syrup as before? It's almost... t-tasteless..."
                        bo"*Nervous chuckle* Heh. Must be bacause of the low quantity of it..." with vpunch
                        him"Hmmm... Then..."


                    "{color=[obediencecolor]}That syrup... you can have more of it!{/color}":
                        bo"That syrup... Would you like more of it?"
                        him"Mhm... *Affirmative Hum*"
                        bo"Then you are gonna have to try sucking on it like you did before..."
                        call changeObedience("Himawari", 1,"him_ob34",1) from _call_changeObedience_101
                        himt"S-so that's how it works..."
                hide blackscreen
                hide spitmark1
                hide hima_finalbefore_angry
                hide spitfx1
                hide hima_finalbefore
                hide hima_cumtaste1
                hide hima_cumtaste2
                with dissolve
                him"Then... I'll try that again!" with vpunch
                hide cutout_bo3
                hide cutout_bo2
                with dissolve
                bo"Y-you will...?" with vpunch
                hide cutout_bo1 with dissolve
                him"Yeah! But this time, let me have at it at my own pace..." with vpunch
                bo"Sure..."
                $ renpy.sound.play("/audio/soun_fx/lickpenis1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                show hima_deny1 with dissolve:
                    xalign 0.11 zoom 0.53
                himt"So... If I do this..."
                show hima_suck1 with dissolve:
                    xalign 1.0 yalign 0.5 zoom 0.5
                himt"And then..."
                $ renpy.sound.play("/audio/soun_fx/suck2.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                show hima_deny3 with flash:
                    zoom 1.5 xalign 0.5 yalign 0.6
                $ renpy.sound.play("/audio/soun_fx/suck1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                show hima_deny3 with flash:
                    zoom 1.5 xalign 0.5 yalign 0.4
                bot"Oh f-fuck!" with vpunch
                bot"S-she's..."
                $ renpy.sound.play("/audio/soun_fx/suck3.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                show hima_deny3 with flash:
                    zoom 1.5 xalign 0.5 yalign 0.2
                bot"[him_name]'s s-sucking me dry!" with flash
                show hima_deny3 with flash:
                    zoom 1.5 xalign 0.5 yalign 0.0
                bot"My bratty little [him_rel]... That's it! Keep sucking your big [him_rel_to_bo] off."
                bot"She is so fucking hot like this, confused but enjoying it! Completely unaware of the twisted intimacy that's taking place..."
                himt"That t-taste... it's..." with vpunch
                bot"There's no way I can resist. I can't help myself..."
                bot"Her soft little puckered lips are wrapped around my cock, I just have to..."
                $ renpy.sound.play("/audio/soun_fx/growl1.opus", channel="sfx3", loop=False, relative_volume = 0.9)    
                show kurama1 with flash
                show kurama1:
                    easein 2 alpha 0.0
                beast"TAKE HER!"
                bot"I h-have to...!" with vpunch
                $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                scene black with flash
                bot"Something c-compels me to...!" with vpunch
                $ renpy.sound.play("/audio/soun_fx/suck2.opus", channel="sfx3", loop=False, relative_volume = 0.9)
                $ renpy.sound.play("/audio/soun_fx/hima_gag2.opus", channel="sfx2", loop=False, relative_volume = 1.4)
                show hima_force1 with flash
                him"!" with vpunch
                himt"*Gag* ...A-again?"
                "This time with both hands, you grabbed [him_name]'s head and pushed your hips forward, burying your shaft inside of her..."
                himt"Why d-does he keep g-grabbing on-"
                show hima_force1_1 with dissolve
                $ renpy.sound.play("/audio/soun_fx/hima_gag.opus", channel="sfx2", loop=False, relative_volume = 1.1)
                bo"Don't worry [him_name]... This is standard procedure!" with vpunch
                himt"*Gag* S-standard procedure? I can almost feel it at the back of m-my...-" with vpunch
                "Little by little... your restraint seemed to slip away!"
                show hima_force2 with dissolve
                "As you felt the deeper layers of her orfices tightly wrapping around your manhood, your lust to violate her throat only grew stronger and stronger..." with vpunch
                hide hima_force2 with dissolve
                "You didn't just want her to taste you; You wanted her to be part of your dark game, to see her reaction after you released your deepest, darkest desires in her..."
                show hima_force1_1 with dissolve:
                    zoom 1.15
                "You moved your hands closer and guided her head towards you. With a low growl you said..."
                bo"Don't stop t-tasting it [him_name], you are about to discover..."
                show hima_force1_2 with dissolve
                $ renpy.sound.play("/audio/soun_fx/hima_gag2.opus", channel="sfx2", loop=False, relative_volume = 1.1)
                $ renpy.sound.play("/audio/soun_fx/suck2.opus", channel="sfx3", loop=False, relative_volume = 0.9)
                bo"... the secret of my recipe!" with vpunch
                him"*Gulp*!" with vpunch
                himt"W-what is he trying to do!"
                "With one last calculated movement of your hips, you pushed your manhood as deep as possible..."
                "You were still mindful of her face coming in contact with your navel or your testicles, as that could potentially give you away..."
                himt"It's.. d-definitely at the back of my... m-mouth..." with vpunch
                himt"Not p-painful, but... uncomfortable!"
                bot"I want her to know me... I want her to taste me in the most intimate of ways!"
                bot"I need to know how far I can push her!"
                bot"I can't hold back any longer!" with vpunch
                menu:
                    bot"I can't hold back any longer!" 
                    "{color=[hatredcolor]}Violate her throat{/color}" (secrethatred = True):
                        pass
                $ renpy.sound.play("/audio/soun_fx/bj3.opus", channel="sfx3", loop=False, relative_volume = 0.9)
                show hima_bj_blind with flash
                bo"It's... It's c-coming any second now [him_name]..."
                bo"The s-syrup is about to spout out!" with vpunch
                himt"T-this definitely isn't standard procedure!"
                himt"He is m-moving the thing while it's inside me! B-but... but-"
                bo"Remember what I told y-you...?"
                bo"The more intensely you s-suck on it..."
                bo"The more of the secret s-syrup you'll be able to extract!" with vpunch
                $ renpy.sound.play("/audio/soun_fx/bj3.opus", channel="sfx3", loop=False, relative_volume = 0.9)
                himt"As h-handsy as this f-freaking idiot thinks he can get... h-he may be right!"
                himt"I can f-feel the syrup dripping around and f-filling the insides of m-my mouth..."
                bo"With this technique I am showing you..."
                bo"You are b-bound to taste the best it has to offer!"
                menu:
                    bot"I can't hold back any longer!" 
                    "{color=[hatredcolor]}Fill up her throat!{/color}" (secrethatred = True):
                        pass
                bot"F-fffuck! F-fuck Fuck fuck! Her throat feels so god-damn tight!"
                bot"I n-need to... I NEED TO!!" with vpunch
                $ renpy.sound.play("/audio/soun_fx/growl1.opus", channel="sfx3", loop=False, relative_volume = 0.9)    
                show kurama1 with flash
                show kurama1:
                    easein 2 alpha 0.0
                $ renpy.sound.play("/audio/soun_fx/bj2.opus", channel="sfx2", loop=False, relative_volume = 0.9)
                show hima_bj_blind2 with flash
                beast"Yes, YES! *Growls*"
                beast"Give yourself to me..."
                "Moments away from reaching climax, you started frantically moving your hips faster and faster..."
                "Almost involuntarily, your hips kept pistoning back and forth, rapidly pushing your cock inside and outside [him_name]'s throat..."
                "All it took is mere seconds before you reached the absolute peak of pleasure; The sensation of her mouth, the innocence of her confusion, it was all too much..."
                "Click twice to fill up her throat!"
                call clicktwice from _call_clicktwice_16
                bot"I am a-about to..." with flash
                bot"[him_name]... I hope you are ready to taste my semen you b-bitch!" with vpunch
                $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                hide hima_bj_blind2
                hide hima_bj_blind
                scene hima_force1 with flash
                bot"I am about to f-fill your throat with my c-cum!" with vpunch
                $ renpy.sound.play("/audio/soun_fx/throatcum.opus", channel="sfx1", loop=False, relative_volume = 0.6)
                show hima_force1_2 with flash
                bot"Hnng!" with vpunch
                show hima_force3_1 with flash
                pause 0.2
                $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                show hima_force3 with flash
                call decreaselust(100) from _call_decreaselust_82
                "With one last hip thrust, you unleashed every bit of pent up lust you had festering inside of you..."
                "Your release flooded the insides of [him_name]'s throat. Her surprise was palpable, evident by her sudden widened expression as the taste and texture of what you offered registered..."
                $ renpy.sound.play("/audio/soun_fx/throatpie.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                show hima_force1_1 with flash
                "She started pulling back, a mix of surprise and discontent flashing across her features as she started swallowing reflexively..."
                himt"T-there's so much of it spurting out this time! *Gulp*" with vpunch
                himt"I... k-keep swallowing it as it pours inside of me..."
                himt"The t-taste of it is... it's..."
                himt"...B-beautiful!" with vpunch
                scene hima_force1 with dissolve
                bot"*Silent panting* H-holy s-shit! I just emptied my b-balls inside my [him_rel]'s mouth..."
                bot"[him_name] just s-sucked me dry... She d-drained every last drop from my b-balls!"
                $ renpy.sound.play("/audio/soun_fx/pop.mp3", channel="sfx2", loop=False, relative_volume = 1.0)
                show hima_suck1 with flash
                $ renpy.sound.play("/audio/soun_fx/gaspforair1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                himt"But if this i-idiot thinks he can do w-whatever he wants, then..."
                "[him_name] took a moment to catch her breath..."
                scene black
                show hima_drool3:
                    xalign 0.0 zoom 0.53
                with dissolve
                bot"The fact that she has no idea what she just did is the cherry on top!"
                call changeHatred(1) from _call_changeHatred_122
                bot"She really is a guilable as I thought! Stupid little bi-"
                him"Y-you..." with vpunch
                show hima_drool3:
                    alpha 0.2
                show hima_drool2_angry:
                    xalign 1.0 zoom 0.53
                with dissolve
                him"You f-freaking idiot! W-what the hell was that for!" with vpunch
                bot"Aww, shit! Better find a good excuse..."
                bo"I was j-just..."
                call changeRespect("Himawari",-3) from _call_changeRespect_172
                him"I t-told you to let me try it at my own pace! Y-you freaking jerk..." with vpunch
                bo"I am s-sorry... I just wanted to show you the best way to... e-enjoy it!"
                bo"That's the secret I wanted to reveal to you..."
                bo"It t-tasted good... didn't it?"
                hide hima_drool2_angry
                show hima_drool2_shy:
                    xalign 1.0 zoom 0.53
                with dissolve
                call changeObedience("Himawari", 1) from _call_changeObedience_102
                him"A-and so what if it did... D-dummy!" with vpunch
                him"That doesn't mean you can p-push it around inside my mouth..."
                call changeRespect("Himawari",-3) from _call_changeRespect_173
                him"Let alone p-push on my head! Who told you you can do that!" with vpunch
                bo"Y-you are right, you are right..."
                bo"I am sorry, Okay? It won't happen again..."
                $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                him"Hmph! It b-better not..." with vpunch
                scene black with dissolve
                $ renpy.sound.play("/audio/soun_fx/clothes_undress.opus", channel="sfx3", loop=False, relative_volume = 1)
                "As you started cleaning up the evidence, you noticed [him_name]..."
                show hima_cumtaste1 with dissolve:
                    zoom 1.2 xalign 0.5 yalign 1.0
                "She was gathering up what little amounts of semen that was left stranded around her mouth..."
                show hima_cumtaste2 with dissolve:
                    zoom 1.2 xalign 0.5 yalign 1.0
                "She scooped up the strands of semen from her face, and with her delicate fingers she pushed it all right onto her tongue to properly taste..."
                $ renpy.sound.play("/audio/soun_fx/swallow.opus", channel="sfx2", loop=False, relative_volume = 1.4)
                show hima_cumtaste3 with dissolve:
                    zoom 1.2 xalign 0.5 yalign 1.0
                himt"*Gulp*... W-whatever this is..."
                himt"I want more of it!" with vpunch
                scene black with vpunch
                show cutout_bo1 with dissolve:
                    xalign 0.5 yalign 0.5
                bot"M-my gods! She really can't get enough of it, huh..."
                show cutout_bo2 with dissolve:
                    xalign 0.5 yalign 0.5
                bot"All that nagging of hers won't do her much good if she gets addicted to my taste..."
                show cutout_bo3 with dissolve:
                    xalign 0.5 yalign 0.5
                bo"S-so... How did that taste... [him_name]? Was it better than before?" with vpunch
                scene himablindfold 1_1 with dissolve
                him"N-none of your business..." with vpunch
                bo"Come on... you are supposed to help me refine the recipe!"
                him"Tough luck, idiot! Maybe next time don't act all weird..."
                bo"I see... Maybe I should look for another assistant then..."
                bo"I'll be gone in a second, you can take the blindfold off whenever you want..."
                him"."
                scene black with dissolve
                him".."
                him"..." with vpunch
                show himablindfold 1 with dissolve
                him"H-hey w-wait a second..." with vpunch
                bot"...So predictable!"
                him"I didn't say that I want to stop h-helping you..."
                him"Only that you were an idiot and acted weird this time around!" with vpunch
                bo"Yeah and I apologized, so..."
                bo"Are you going to help or not..."
                scene black with vpunch
                $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                him"Hmph! ...F-fine! Let me take this thing off first..." with vpunch
                scene black with dissolve
                "You made sure to hide any evidence before [him_name] took the blindfold off..."
                if day_part == 3:
                    show himawari_bedroom_2
                else:
                    show himawari_bedroom_1
                show hima worried2 at right:
                    zoom 0.34
                with dissolve
                show boruto snob at left with dissolve
                him"..."
                bo"So... How did that taste? Do you have a guess as to what it was?"
                show hima at smallshake
                him"I k-know exactly what that was!" with vpunch
                bo"Don't lie... You have no idea what that was!"
                show hima embarassed with dissolve
                him"*Frustrated groan* Gaaaah! Can't you just t-tell me?" with vpunch
                bo"Of course not, that defeats the purpose..."
                bo"Did you enjoy it that much...?"
                show hima at smallshake
                him"It was... a-alright..."
                bo"Just... alright?"
                show hima worried2 with dissolve
                him"It was good! Okay? I am just confused by it all..."
                him"What kind of food could taste like that..."
                him"And what kind of food could require that sort of... consumption, to be enjoyed in its entirety!"
                show hima mad with dissolve
                him"Garh! I just want to know what that was!" with vpunch
                bo"Perhaps you'll find out next time..."
                show hima at smallshake
                him"D-darn it! Here's my advice for your s-stupid recipe!"
                him"W-would be nice if that s-syrup could come out without you having to m-mess with me!"
                bo"What if I told you there's a way for that to happen..."
                show hima worried2 with dissolve
                him"T-there is...?"
                show boruto:
                    easein 2 xpos -1000
                bo"Indeed! But you are gonna have to find out for yourself next time!"
                show hima mad with dissolve
                him"Garrh! *Fuming* Y-you..."
                bo"Catch you around!"
                show hima at shake
                himt"M-maybe I'll just cheat and remove the blindfold n-next time!"
                himt"But he would never stop ridiculing me for that... D-damn idiot! He gets on my nerves so much..."
                $ renpy.end_replay()
                if quest_him.is_state("him1H_2", "pending"):
                    $ quest_him.change_quest_title("him1H_2",f"Trick {him_name} into tasting your 'syrup'")
                    $ notification (f"{him_name} Hatred objective completed")
                    $ quest_him.check("him1H_2", "completed")
                scene black with dissolve
                jump action_taken
                default v17_update = True
                




                
                    
                    
                
            "{color=[lovecolor]}Indulge her with care...{/color}" (secretlove = True)  if blindfoldfull == True and himawari_love >= 3 and percentage >= 80:
                if v17_update == True:
                    pass
                else:
                    $ notification("Exclusive supporters scene")
                $ blindfoldfinished = True
                bo"If that is your wish..."
                label replay_blindfoldtaste_love:
                $ initialize_replay_defaults()
                scene black with dissolve
                show hima_start1_1 with dissolve:
                    xalign 0.5 zoom 1.1 yalign 1.0
                show hima_start1_1:
                    easein 5 yalign 0.0
                bo"Then I will happily indulge you..."
                him"*A-aaahh...*"
                "[him_name] leaned forward, eager for another taste..."
                bot"In all her innocence... She looks real pretty sitting there like that..."
                show hima_start1_2 with dissolve:
                    xalign 0.5 zoom 1.15 yalign 0.0
                bot"How could I ever resist her invitations, even knowing that there's deception at play..."
                bot"But perhaps there's a way to make this enjoyable for her..."
                bo"[him_name]... Today, I am thinking I'll let you in on a little secret..."
                scene black with dissolve
                show hima_deny2 with dissolve:
                    xalign 0.15 zoom 0.53
                him"A... s-secret?" with vpunch
                "You let your cum-dripping cock hanging right above [him_name] as you watched her giddily awaiting for you..."
                himt"I can smell it, he is holding it right above m-me..."
                bo"An important secret, yes..."
                him"Now I am intrigued... P-please, do tell!"
                bo"You see..."
                bo"Previously you tried licking it, like you would a popsicle, right...?"
                him"Y-yeah...? Should I have..."
                show hima_deny1 with dissolve:
                    xalign 0.15 zoom 0.53
                $ renpy.sound.play("/audio/soun_fx/lickpenis1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                him"...Not?" with vpunch
                bot"F-fuck... I am already pretty close to my limit..."
                hide hima_deny1 with dissolve
                bo"N-no, you s-should do that if you want.. But..."
                show hima_deny1 with dissolve:
                    xalign 0.15 zoom 0.53
                $ renpy.sound.play("/audio/soun_fx/lickpenis1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                him"T-then... *Indulgent licking*..."
                bo"B-but what if I told you the best way to experience the most it has to offer is to t-think of it more like a... lollipop..."
                bo"The h-harder you suck on it, the m-more of that special s-syrup it may produce..."
                hide hima_deny1 with dissolve
                him"So you are saying that if I do this instead..."
                show hima_deny1 with dissolve:
                    xalign 0.15 zoom 0.53 
                "Without hesitation, [him_name] traced the tip of your shaft with her tongue by rising on her knees and..."
                hide hima_deny2
                show hima_repeat1:
                    xalign 0.85 zoom 0.6
                show hima_deny1:
                    alpha 0.2
                with dissolve
                "She let the tip drop straight into her mouth..."
                bo"Y-yeah... Just like that! Now try s-sucking on it as if it were something between a lollipop and a popsicle..."
                scene black with dissolve
                "[him_name] took your 'advice'..."
                $ renpy.sound.play("/audio/soun_fx/suck2.opus", channel="sfx1", loop=False, relative_volume = 1.2)
                show hima_suck4 with flash
                "And she tightened her lips around your cock..."
                $ renpy.sound.play("/audio/soun_fx/suck4.opus", channel="sfx2", loop=False, relative_volume = 1.2)
                bot"F-fuck! She r-really is..." with flash
                $ renpy.sound.play("/audio/soun_fx/suck5.opus", channel="sfx3", loop=False, relative_volume = 1.2)
                bot"My little [him_rel] is s-sucking on my cock!" with flash
                $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx1", loop=False, relative_volume = 0.6)
                bot"I am l-losing all control!" with flash
                $ renpy.sound.play("/audio/soun_fx/cum2.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                show hima_suck2_1 with flash
                call decreaselust(50) from _call_decreaselust_83
                bot"F-fuck!" with vpunch
                "A large spurt of semen violently escaped you, quickly filling [him_name]'s mouth..."
                "Some of it even managed to burst through the tight little gaps left between her puckered lips..."
                $ renpy.sound.play("/audio/soun_fx/heartbeatlong.opus", channel="sfx3", loop=False, relative_volume = 1.0)
                "Your heart started beating erattically, fearing that [him_name] was tipped off, that she got scared..."
                $ renpy.sound.play("/audio/soun_fx/suck7.opus", channel="sfx1", loop=False, relative_volume = 1.2)
                show hima_suck2 with dissolve
                "She was caught by surprise and pulled her lips ever so slightly backwards..."
                himt"T-this taste!" with vpunch
                himt"He wasn't lying! It's..."
                show hima_bj_blindlove1 with dissolve
                $ renpy.sound.play("/audio/soun_fx/bjair1.opus", channel="sfx1", loop=False, relative_volume = 1.2)
                "[him_name], caught in the moment, continued to taste, to explore with her tongue, unaware of the true nature of what she was doing..."
                "As soon as you realized what was happening, another wave of extreme arousal captivated you..."
                $ renpy.sound.play("/audio/soun_fx/bjair2.opus", channel="sfx1", loop=False, relative_volume = 1.2)
                call increaselust(50) from _call_increaselust_125
                bot"H-holy fuck! She is s-sucking my cum straight from the source..."
                himt"This t-taste it's... it's beautiful!"
                himt"It keeps pouring as I keep s-sucking on it..."
                show hima_suck1 with flash
                $ renpy.sound.play("/audio/soun_fx/pop.mp3", channel="sfx2", loop=False, relative_volume = 1.2)
                pause 0.2
                $ renpy.sound.play("/audio/soun_fx/gaspforair1.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                "*Pop*... [him_name] loosened the tight grip of her lips..."
                him"Y-you..."
                "She pulled back to gasp for air and looked up towards you with hints of confusion, along with something else..."
                bot"S-she...she swallowed most of it!" with vpunch
                bot"Thank the heavens she s-stopped when she did, or I would unload an unholy amount of s-semen right inside of her mouth..."
                scene black with dissolve
                show hima_start1 with dissolve:
                    xalign 0.5 zoom 1.1 yalign 1.0
                show hima_start1:
                    easein 5 yalign 0.0
                him"Y-you weren't kidding!" with vpunch
                bo"Of c-course not..."
                him"As soon as I started sucking on it, it's like I could squeeze infinite amounts of s-syrup out of it..."
                him"And the t-taste of it, it was..."
                show hima_start1_1 with dissolve:
                    xalign 0.5 zoom 1.1 yalign 0.1
                show hima_start1_1:
                    easein 4 yalign 1.0
                him"It was amazing!" with vpunch
                him"Can I try that one more time?"
                bot"A-are you kidding me!?" with vpunch
                bo"Of course y-you can..."
                him"Yaay!" with vpunch
                show hima_start1_1 with dissolve:
                    xalign 0.5 zoom 1.1 yalign 0.1
                bo"...A-are you ready?"
                show hima_start0 with dissolve:
                    xalign 0.5 zoom 1.1 yalign 0.1
                him"Yea! *Aaaah...*"
                scene black with dissolve
                show hima_repeat1 with dissolve:
                    xalign 0.1 zoom 0.6
                bo"H-here it comes..."
                show hima_repeat1:
                    alpha 0.2
                show hima_repeat2:
                    xalign 0.9 zoom 0.6
                with dissolve
                bo"Try s-sucking on it, just like you did before..."
                "You lightly pressed on top of her head to guide her movements, managing to bring most of your shaft halfway through her mouth..."
                show hima_force1 with dissolve:
                    zoom 1.5 xpos 0.5 yalign 1.0
                "Surprisingly, [him_name] stayed calm and followed your guidance..."
                show hima_bj_blindlove2 with dissolve:
                    zoom 1.5 xpos 0.5 yalign 1.0
                "You started gently moving your hips back and forth, while [him_name] moved her tongue around, tasting every nook and cranny she could..."
                himt"It's... It's moving inside of m-my mouth!"
                bot"Oh... m-my... l-lord..." with flash
                $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                bot"There's... n-no way I can hold off any l-longer..." with flash
                bot"She is just so fucking pretty like this, confused but... f-fully enjoying it! Completely unaware of the twisted intimacy that's taking place..."
                bo"It might shoot out a-any second now, don't be s-surprised..."
                bot"I am about to f-fill her mouth with my c-cum!" with flash
                $ renpy.sound.play("/audio/soun_fx/throatcum.opus", channel="sfx1", loop=False, relative_volume = 0.6)
                show hima_force1_2 with longerflash:
                    zoom 1.5 xpos 0.5 yalign 1.0
                call decreaselust(100) from _call_decreaselust_84
                bot"Hnng-hnnn!" with vpunch
                "With one last hip thrust, you unleashed every bit of pent up lust you had building up inside of you..."
                "Your release flooded the insides of [him_name]'s throat. Her surprise was palpable, evident by her sudden widened expression as the taste and texture of what you offered registered..."
                $ renpy.sound.play("/audio/soun_fx/throatpie.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                show hima_force1_1 with flash:
                    zoom 1.5 xpos 0.5 yalign 1.0
                "She started pulling back, a mix of surprise and... something else, flashing across her features as she started swallowing reflexively..."
                himt"T-there's so much of it spurting out this time! *Gulp*" with vpunch
                himt"I... k-keep swallowing it as it pours inside of me..."
                himt"The t-taste of it is... it's..."
                himt"...a-addicting!"
                bot"*Silent panting* H-holy s-shit! I just emptied my b-balls inside my [him_rel]'s mouth..."
                bot"[him_name] just s-sucked me dry... She d-drained every last drop out of me!"
                bot"And she's still gripping my cock with her soft little lips..."
                call increaselust(5) from _call_increaselust_126
                $ renpy.sound.play("/audio/soun_fx/pop.mp3", channel="sfx2", loop=False, relative_volume = 1.0)
                show hima_suck1 with flash
                $ renpy.sound.play("/audio/soun_fx/suck1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                "[him_name] pulled back, strands of semen still hanging from both, her mouth, and your cock..."
                "She looked up to you in complete surprise, her cheeks stained with a deep blush as she tried to process what she just tasted..."
                him"It... It was l-like it was moving inside of my mouth on its own..."
                him"...D-did you do that!?" with vpunch
                menu:
                    him"...D-did you do that!?"
                    "N-no, it just does that on its own..." if didyoudothat_own == False and didyoudothat_yes == False :
                        bo"W-what? N-no! It does that on its own..."
                        him"it... d-does!? How?" with vpunch
                        bo"Can't tell... T-trade secrets... *Nervous chuckle*"
                        him"Hmm... Not s-sure if I can believe that..."
                        default didyoudothat_own = False
                        $ didyoudothat_own = True
                    "Y-yeah, I tried to give you the best possible experience..." if didyoudothat_own == False and didyoudothat_yes == False:
                        bo"I... I did! I t-tried to give you the best experience I could..."
                        call changeObedience("Himawari", 1) from _call_changeObedience_103
                        him"It w-was... intense!" with vpunch
                        default didyoudothat_yes = False
                        $ didyoudothat_yes = True
                    "N-no, it just does that on its own..." if didyoudothat_own == True:
                        bo"W-what? N-no! It does that on its own..."
                        him"it... d-does!? How?" with vpunch
                        bo"Can't tell... T-trade secrets *Nervous chuckle*"
                        him"Hmm..."
                     
                    "Y-yeah, I tried to give you the best possible experience..." if didyoudothat_yes == True:
                        bo"I... I did! I t-tried to give you the best experience I could..."
                        him"It w-was... intense!" with vpunch
                     
                scene black with dissolve
                him"But, I would prefer if I could..."
                $ renpy.sound.play("/audio/soun_fx/suck7.opus", channel="sfx1", loop=False, relative_volume = 1.2)
                show hima_suck2 with flash
                him"T-taste it at my own leisure..."
                show hima_bj_blindlove1 with dissolve
                $ renpy.sound.play("/audio/soun_fx/bjair1.opus", channel="sfx1", loop=False, relative_volume = 1.2)
                himt"The s-smell is so enticing..."
                "Entranced by the strong odor of your semen, [him_name] would once again start sucking what little residue of it remained around your cock..."
                "You watched as she innocuously did her best to suck what was left of you..."
                call increaselust(10) from _call_increaselust_127
                bot"[him_name]..."
                bo"I..."
                "Guilt, but mostly desire sparred within you, you wanted to say something but, the words died before they left your lips..."
                scene black
                bot"...!" with vpunch
                $ renpy.sound.play("/audio/soun_fx/suck5.opus", channel="sfx1", loop=False, relative_volume = 1.2)
                show hima_suck3 with flash
                "With one voluntary move, [him_name] took almost your entire shaft in her mouth..."
                himt"*Slurp*... Mmm... Is there no m-more of it?"
                bot"S-she... She is sucking me d-dry!" with vpunch
                $ renpy.sound.play("/audio/soun_fx/suck4.opus", channel="sfx1", loop=False, relative_volume = 1.2)
                show hima_suck4 with Dissolve(1)
                "She slowly pulled back, after ensuring she tasted every drop of semen she could get her tongue around..."
                "Her lips slid across your shaft, revealing how she left your knob almost completely spotless..."
                $ renpy.sound.play("/audio/soun_fx/pop.mp3", channel="sfx2", loop=False, relative_volume = 1.0)
                show hima_suck4_1 with flash
                $ renpy.sound.play("/audio/soun_fx/suck1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                "All that was left behind was her saliva spread across your cock..."
                bot"D-did she just..." with vpunch
                bot"S-she slurped up every last drop..."
                bot"She s-swallowed all of it!" with vpunch
                him"I think..."
                scene black with dissolve
                show hima_drool3 with dissolve:
                    xalign 0.0 zoom 0.53
                him"I got everything out of it..."
                show hima_drool3:
                    alpha 0.2
                show hima_drool1:
                    xalign 1.0 zoom 0.53
                with dissolve
                him"Is there... no m-more of it?"
                bot"M-more!?" with vpunch
                bo"I am afraid not... *Nervous laughter*"
                bo"You've depleted just about all of it..."
                show hima_drool2_shy with dissolve:
                    xalign 1.0 zoom 0.53
                him"Shame... That t-tasted amazing!" with vpunch
                him"Is it because of the secret you s-showed me?"
                bo"Very well could be..."
                him"I am going to need more of t-that... and soon!" with vpunch
                bo"R-right..."
                show hima_droolcheck with dissolve:
                    xalign 1.0 zoom 0.6
                bo"Here, you missed a speckle..."
                scene black with dissolve
                him"O-oh..."
                show hima_open with dissolve:
                    zoom 1.05 xalign 0.5 yalign 0.5
                show hima_open:
                    easein 3 yalign 0.3
                him"T-thanks..."
                bot"There was a time she'd bite my finger off if I ever touched her face, but now..."
                bot"She's so... docile, and so... pretty..."
                scene black
                bot"F-fuck... What am I thinking..." with vpunch
                bot"What am I even doing... *Sigh*..."
                bot"This feels wrong..."
                $ renpy.sound.play("/audio/soun_fx/clothes_undress.opus", channel="sfx3", loop=False, relative_volume = 1)
                "You quickly dressed yourself and hid any evidence of your ploy..."
                show himablindfold 1_1 with dissolve
                him"W-why are you so quiet all of a sudden..." with vpunch
                bo"O-oh, sorry... I was just, cleaning up my s-stuff..."
                bo"Wouldn't want to reveal my recipe's secrets..."
                him"But you already shared one of its secrets... Teehee!" with vpunch
                bo"...I did? Remind me which one was that again?"
                scene himablindfold 1 with fade
                him"How did you already forget you dummy! You said the best way to consume it was to s-suck on it..."
                him"And you were right! It tasted amazing! Not only that..."
                him"I think you may have given away what it was by doing that!" with vpunch
                bo"I did?..."
                bot"There's no way she would be this calm if she actually knew what it was..."
                scene black with dissolve
                him"I am not telling until I can get this off and watch as the panic settles into your eyes!"
                him"The prize money is mine! Hee-hee-heee!" with vpunch
                bo"You little devil..."
                scene black with dissolve
                "You quickly got rid of all the 'evidence' while [him_name] patiently awaited for your call..."
                bo"You can take it off now..."
                if day_part == 3:
                    show himawari_bedroom_2
                else:
                    show himawari_bedroom_1
                show hima worried2 at right:
                    zoom 0.34
                with dissolve
                show boruto surprised2 at left with dissolve
                him"That was..."
                show hima at smallshake
                him"T-that was..." with vpunch
                bo"...It was?"
                show hima embarassed with dissolve
                show hima at smallshake
                him"I... M-maybe... A s-strange lollipop!?"
                show hima at smallshake
                him"I have no c-clue! But I wanna know..."
                show hima at shake
                him"I wanna know, I wanna know I wanna know I-WANNA-KNOW!" with vpunch
                show hima worried2 with dissolve
                him"Can you p-please tell me?"
                show boruto snob with dissolve
                bo"You know I can't do that..."
                bot"For your own good too..."
                show hima at smallshake
                him"I k-know... But really, what even was that..."
                him"It felt as if it were alive while I was s-sucking on it..."
                him"It was pulsating and constantly releasing more of that honey-like s-syrup while it was... inside of me..."
                him"How did you even come up with something like that..."
                him"First the clothing store clerk says you are some kind of m-modelling expert..."
                him"Now you are coming up with your own fascinating recipes..."
                him"What has happened to you..."
                bo"*Nervous chuckle* Heh, what can I say... Life happened, I suppose?"
                show hima:
                    easein 1 xalign 0.5
                him"In truth..."
                show hima:
                    easein 1 xalign 0.3
                pause 0.5
                scene black with dissolve
                him"I don't really care what happened..."
                if day_part == 3:
                    show himawari_bedroom_2
                else:
                    show himawari_bedroom_1
                show himahug2t
                with dissolve
                him"Only that it did..."
                him"You are almost unrecognizable..."
                call changeLove("Himawari",2,"blindlove1",1) from _call_changeLove_44
                him"Thanks for trusting me with helping you out with this..."
                him"Turns out you got something great on your hands, all because of me! Teehee..."
                bo"*Nervous chuckle* Heh, T-thank you for all your... help..."
                show hima_kiss1 with dissolve
                him"Maybe you should pay me royalties whenever you start selling that!"
                call changeRespect("Himawari", 2) from _call_changeRespect_174
                him"Teehee!"
                $ renpy.sound.play("/audio/soun_fx/hinata/kisscheek.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                show hima_kiss1_1 with dissolve:
                    zoom 1.1 xalign 0.0
                him"*Kiss*"
                bot"If only she knew... She would hate my guts..."
                hide hima_kiss1_1
                show hima_kiss1
                with dissolve
                him"But you still..."
                scene black with dissolve
                if day_part == 3:
                    show himawari_bedroom_2
                else:
                    show himawari_bedroom_1
                show hima smugshy at right:
                    zoom 0.34 xalign 0.5
                show boruto surprised2 at left
                with dissolve
                show hima:
                    easein 1 xalign 0.8
                him"You still smell like rotten fish!"
                show hima worried2 with dissolve
                him"But really, can I taste that again sometime? Even if I have no more feedback left to give..."
                show hima at smallshake
                him"I could do with another chance to guess what it was I s-suppose..."
                bot"Well, f-fuck..."
                bot"Seems like I brought this upon myself..."
                bot"There's no way I can ever let her know what that was, but..."
                bot"It seems like my [him_rel] is now enamored by the taste of my semen..."
                show boruto normal with dissolve
                bo"Uhm... M-maybe?"

                him"...M-maybe?" with vpunch
                show hima mad with dissolve
                him"After all I've done to help you..." with vpunch
                show boruto surprised2 with dissolve
                bo"N-no, I meant... I'll have to prepare a new p-prototype first!"
                show boruto:
                    easein 2 xpos -1000
                bo"You can taste it again when that is ready! See you around!"
                show hima mad with dissolve
                him"Garrh! *Fuming* Y-you..."
                show hima at shake
                himt"M-maybe I'll just cheat and remove the blindfold n-next time!"
                himt"But then he would never let me live that down... D-damned idiot! He gets on my nerves so much..."
                $ renpy.end_replay()
                if quest_him.is_state("him1L_2", "pending"):
                    $ quest_him.change_quest_title("him1L_2",f"'Convince' {him_name} to taste your 'syrup'")
                    $ notification (f"{him_name} Love objective completed")
                    $ quest_him.check("him1L_2", "completed")
                scene black with dissolve
                jump action_taken



        
        

    else:
        pass
    #first time repeat
    show hima shy with dissolve
    him"Oh, that! Did you refine your recipe?"
    bo"Of course! Your feedback is important to me..."
    bo"In fact, this may be the tastiest my recipe has ever been. Your input has been invaluable!"
    show hima smugshy with dissolve
    him"Hee-heeee! I told you my palate is cultured!"
    bo"Sure is..."
    him"Now let's get on with it! Today I am winning the prize you promised!"
    show boruto:
        easein 1 xalign 0.6
    bo"Not so fast! You'll have to put this on first..."
    scene black with dissolve
    bo"I need a moment to make the necessary preparations..."
    show himablindfold 1_1 with dissolve
    him"Let me know when you are ready!"
    bot"There she goes again..."
    bot"My innocent little [him_rel] sitting on her knees..."
    call increaselust(10) from _call_increaselust_128
    $ renpy.sound.play("/audio/soun_fx/heartbeatlong.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    bot"My heart is already beating like crazy..."
    show himablindfold with dissolve:
        alpha 0.2
    show boruto_blindfold_cut with dissolve:
        xpos -0.2 ypos -0.36
    bot"So blissfully unaware..."
    hide boruto_blindfold_cut
    show himablindfold:
        alpha 1
    with dissolve
    bo"Alright, you ready?"
    him"Y-yeah!" with vpunch
    bot"Can I really risk going all the way this time...?"
    scene black with dissolve
    bo"You should face towards me..."
    him"Is here fine...?"
    show screen parallax1280("hima_finalbefore",1.25,0.0) with dissolve
    call showscrollingimage from _call_showscrollingimage_68
    bo"Just like last time, we are skipping straight to the main course..."
    him"Come on, let's get started already!"
    him"*Aaaaah...*"
    call increaselust(10) from _call_increaselust_129
    bo"You seem to be in quite the mood..."
    him"I am ready to win the m-money- *Ahem* I mean... help of course!"
    bo"You little devil..."
    him"Teehee!" with vpunch
    bot"I suppose I am not the only one with devious thoughts..."
    call hidescrollingimage from _call_hidescrollingimage_69

    show hima_drool00 with dissolve:
        xalign 0.0 zoom 0.53
    himt"Today I'll get it right for sure!"
    show hima_finalbefore2 with dissolve:
        ypos -0.50
    $ renpy.sound.play("/audio/soun_fx/heartbeatlong.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    bo"Right... Remember, no biting, and no reaching for it with your hands like last time!"
    him"This odor... I am getting used to its intensity..."
    bo"A-are you now..." with vpunch
    him"Y-yeah! At first it was somewhat unpleasant, but..."
    him"The more I am exposed to it, the more I am getting used to the intensity of it!"
    bot"*Gulp* Is this... normal?"
    bot"I would wager that most girls would be appalled, but [him_name]..."
    bot"My little [him_rel] is totally into it!" with vpunch
    bo"Uuh, right, the intensity..."
    bo"Ready to give it a go?"
    him"Mhm..."
    hide hima_finalbefore2 with dissolve
    bot"F-fuck... Here goes nothing!"
    show hima_drool00:
        alpha 0.20
    show hima_liclharden1:
        xalign 1.0 zoom 0.65 xzoom -1
    with dissolve
    $ renpy.sound.play("/audio/soun_fx/lickpenis1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    him"Mh...mhm... *Reluctant licks*..."
    bo"My recipe is best treated with... delicate care..."
    bo"Think of it like a... popsicle of sorts..."
    call increaselust(10) from _call_increaselust_130
    $ renpy.sound.play("/audio/soun_fx/lickpenis1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    him"Mm..."
    bo"The only difference is..."
    bo"Unlike an ice cream, the more you... consume of it, the more intense it can get..."
    bo"The warmth of it, the texture, the size, and the... s-syrup you tasted last time are all fluctuating variables that can change based on how the recipe is prepped..."
    scene black with dissolve
    "[him_name] pulled back with a confused look on her face..."
    show hima_finalbefore2 with dissolve:
        ypos -0.50
    bo"S-so... Any takeaways?"

    him"D-darn it!" with vpunch
    him"You are confusing me even more with your stupid commentary!"
    him"Just... shut up and let me have another t-taste!"
    bo"*Nervous laughter* A-s you wish..."
    scene black with dissolve
    show hima_liclharden1 with dissolve:
        xalign 0.0 zoom 0.65 xzoom -1
    show hima_liclharden2 with Dissolve(1):
        xalign 0.0 zoom 0.65 xzoom -1
    $ renpy.sound.play("/audio/soun_fx/lickpenis1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    him"Mh...mhm... *Indulging licks*..."
    call increaselust(10) from _call_increaselust_131
    himt"H-he wasn't lying... It feels like it's warmer, and bigger than before..."
    bot"F-fuck, I am getting hard as a rock feeling her tongue circling around the glans..."
    himt"But... how?"
    himt"Some s-sort of baked dessert maybe?"
    $ renpy.sound.play("/audio/soun_fx/lickpenis1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    himt"This t-taste is..."
    him"Mh...mhm... *Indulging licks*..."
    himt"Feels slimy, but... it's getting more intense the longer I taste it..."
    hide hima_liclharden1
    show hima_liclharden2:
        alpha 0.3
    show hima_liclharden3:
        xalign 1.0 zoom 0.65 xzoom -1
    with dissolve
    himt"It's sort of... getting interesting!"
    bot"F-fuck! I am rock hard! Looking down at her gazing towards my cock..."
    call increaselust(20) from _call_increaselust_132
    bot"It's way too sensual, but..."
    bot"I need to hold on a little bit longer!"
    bot"I should look for a way to extend this..."
    show hima_liclharden4 with dissolve:
        xalign 1.0 zoom 0.65 xzoom -1
    him"Maybe one more taste-"
    scene black with vpunch
    bo"H-hold on!" with vpunch
    him"W-what? Why..."
    bo"I need to..." 
    $ renpy.sound.play("/audio/soun_fx/clothes_undress.opus", channel="sfx3", loop=False, relative_volume = 1)
    bo"...Complete the final preparations!"
    "You removed your pants under the pretense of preparing your 'recipe'..."
    show hima_start1 with dissolve:
        xalign 0.5 zoom 1.1 yalign 1.0
    show hima_start1:
        easein 5 yalign 0.0
    "Your erect manhood stood inches away from [him_name]'s face. Her warm breath kept breezing against your glans as your cock kept producing seemingly endless foot-long strands of cum..."
    show hima_start1:
        easein 2 yalign 1.0
    "Your so called special 'syrup', dripped all the way down to where [him_name] kept her hands. The aroma of it would only excite her more..."
    show hima_start1 with dissolve:
        xalign 0.5 zoom 1.1 yalign 0.0
    him"...What's taking so long? Come on, hurry up! I think I am close to figuring it out!" with vpunch
    bo"Y-you are...?"
    him"I a-am! But..."
    show hima_start0 with dissolve:
        xalign 0.5 zoom 1.53 yalign 0.15
    him"I could use one final taste before I lock in my answer..." with vpunch
    menu repeatableblindfoldmenu:
        him"I could use one final taste before I lock in my answer..." 
        "Give her what she asked for...":
            default blindfoldfull = False
            $ blindfoldfull = True
            scene black with dissolve
            bo"As you wish..."
            show hima_start1_1 with dissolve:
                xalign 0.5 zoom 1.1 yalign 1.0
            show hima_start1_1:
                easein 5 yalign 0.0
            "[him_name] leaned forward, ready for another taste..."
            scene black with dissolve
            show hima_deny1 with dissolve:
                xalign 0.15 zoom 0.53
            $ renpy.sound.play("/audio/soun_fx/lickpenis1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
            bot"F-fuck! I can't believe she's slurping up my cum drip..."
            call increaselust(10) from _call_increaselust_133
            him"Mmm... Is this the same syrup from last time...?"
            bo"Y-yeah..."
            show hima_deny1:
                alpha 0.2
            show hima_deny2:
                xalign 0.85 zoom 0.53
            with dissolve
            him"It's..."
            him"The taste..."
            him"It's really growing on me..."
            bot"I am at my d-damn limit!"
            call increaselust(10) from _call_increaselust_134
            bot"My cock is t-throbbing right above her face... My cum is dripping all over her face!"
            him"Careful though, you are spilling some on my face!" with vpunch
            bo"S-sorry, it can get a bit m-messy! Y-you did ask for more of it though..."
            him"I did, and turns out..."
            show hima_deny1:
                alpha 1.0
            show hima_deny2:
                xalign 0.85 zoom 0.53 alpha 0.2
            with dissolve
            $ renpy.sound.play("/audio/soun_fx/lickpenis1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
            him"...I was right!"
            call increaselust(10) from _call_increaselust_135
            bot"F-fuck! I am a-about to..."
            him"Mh...mhm... *Indulging licks*..."
            him"Mhm... *slurp* This time... I'll make sure..."
            scene black with flash
            him"...to get a proper taste of it!" with vpunch
            $ renpy.sound.play("/audio/soun_fx/suck2.opus", channel="sfx2", loop=False, relative_volume = 1.0)
            bo"W-wait!" with vpunch
            show hima_deny3 with flash:
                zoom 1.5 xalign 0.5 yalign 0.6
            $ renpy.sound.play("/audio/soun_fx/suck1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
            show hima_deny3 with flash:
                zoom 1.5 xalign 0.5 yalign 0.4
            bot"S-she's..."
            $ renpy.sound.play("/audio/soun_fx/suck3.opus", channel="sfx2", loop=False, relative_volume = 1.0)
            show hima_deny3 with flash:
                zoom 1.5 xalign 0.5 yalign 0.2
            bot"[him_name]'s s-sucking on my..." with flash
            show hima_deny3 with flash:
                zoom 1.5 xalign 0.5 yalign 0.0
            himt"O-oh..h? I see now!" with vpunch
            $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx2", loop=False, relative_volume = 0.6)
            scene black with flash
            call decreaselust(20) from _call_decreaselust_85
            bot"F-fuck!" with vpunch
            show hima_repeat1 with flash:
                xalign 0.5
            $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx3", loop=False, relative_volume = 0.6)
            bot"F-fuck! I h-have to..." with flash
            "On the precipice of the greatest release of your lifetime, panic quickly settled in..."
            $ renpy.sound.play("/audio/soun_fx/pop.mp3", channel="sfx2", loop=False, relative_volume = 1.0)
            hide hima_repeat1
            show hima_drool3 with flash:
                xalign 0.0 zoom 0.7 yalign 1.0
            $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx3", loop=False, relative_volume = 0.6)
            show hima_drool3:
                easein 6 yalign 0.35
            call decreaselust(80) from _call_decreaselust_86
            "You quickly pulled away the moment your cock started pulsating inside her mouth, leaving trails of a sloppy mess, hanging from her face..."
            "An audible, wet *Pop* was heard as soon as the head escaped the tight grip of [him_name]'s lips..."
            him"H-hey! What was that!" with vpunch
            him"What's going on!" with vpunch
            show cumhand with dissolve:
                zoom 1.2 xalign 1.0 yalign 1.0
            $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            bo"*Panting*"
            bot"F-fuck... FUCK!" with vpunch
            bot"I panicked! I had to pull out..."
            bot"But I am pretty s-sure she felt some of it while I was inside her..."
            show hima_drool2_shy with dissolve:
                xalign 0.0 zoom 0.7 yalign 0.4
            him"Answer me you weasel!" with vpunch
            bot"Fuck! Did that g-give me away...?"
            hide cumhand
            show boruto naked2:
                zoom 0.8 xpos 0.41 yalign 1.0
            with dissolve
            bo"Uuuh, I had to pull it back...!" with vpunch
            bo"I thought... you were about to bite on it and r-ruin my recipe! We said no b-biting, remember?" with vpunch
            show hima_drool2_angry with vpunch:
                xalign 0.0 zoom 0.7 yalign 0.4
            him"I wasn't going to bite on it, you idiot!" with vpunch
            hide hima_drool2_angry with dissolve
            him"I was just about to have a proper taste of it..."
            him"And right when I managed to squeeze some of the syrup out..."
            him"You pulled it away!" with vpunch
            bot"...!" with vpunch
            $ renpy.sound.play("/audio/soun_fx/clothes_undress.opus", channel="sfx3", loop=False, relative_volume = 1)
            hide boruto with dissolve
            "You quickly and silently dressed back up as you contemplated what just happened..."
            bot"My d-days... Did I panic over nothing?"
            bot"She has no idea what cum even tastes like..."
            bot"Even better, she might be enjoying tasting me!" with vpunch
            bo"Y-you are right, I am sorry! I... might have panicked a little bit! Heh-eh *Nervous laughter*"
            $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            him"Hmph!" with vpunch
            image himavid = Movie(play="images/video/hima_testanim.webm")
            scene black with dissolve
            him"So..."
            show hima_drool2_shy with dissolve:
                xalign 0.0 zoom 0.53
            him"Can I..."
            show hima_drool2_shy:
                alpha 0.2
            show himavid:
                xalign 1.0
            with dissolve
            him"...FINALLY, have a proper taste?" with vpunch
            bot"!" with vpunch
            him"Pretty please... *Aaaaahh...*"
            call increaselust(10) from _call_increaselust_136
            bot"My l-lord! She really seems to be getting into it..."
            bot"This is unfathomable! My little [him_rel]..."
            bot"M-my little [him_rel]... She is..."
            menu:
                bot"M-my little [him_rel]... She is..."
                "{color=[hatredcolor]}A cock-lusting whore!{/color}" if hatred>=30:
                    call changeHatred(1) from _call_changeHatred_123
                    bot"She is a cock-lusting whore!"
                    bot"I mean, look at her! Sitting there all demure and willing to 'help'! What else am I supposed to do..."
                    bot"Don't worry my sweet [him_name], next time..."
                    bot"I'll be emptying my balls right down your throat!" with vpunch
                "So precious... and naive!":
                    bot"She is just so precious... and naive!"
                    bot"It feels weird taking advantage of her naivety, but..."
                    bot"How can I not when she sits there so patiently, so willing to 'help'..."
                    bot"Who am I to deprive her of that satisfaction?"
                    bot"She seems to be having fun after all!"
                "This isn't right!":
                    bot"She is... so p-precious. So innocent..."
                    bot"What I am doing to her isn't right, even if she seems to be having fun..."
                    call changeHatred(-2) from _call_changeHatred_124
                    bot"If I keep taking advantage of her like this... I'll only grow to be worse."
                    bot"If I really care about her and [hin_rel]..."
                    call changeHatred(-2) from _call_changeHatred_125
                    bot"I have to find other ways for us to get closer..."
            bot"This curse of mine is making me go crazy..."
            scene black with vpunch
            him"[bo_name_stutter]...?"
            show hima_finalbefore with dissolve:
                        zoom 1.25 yalign 0.0 
            bo"*Ahem!* I would for you to have another taste of it, but..." with vpunch
            bo"Uuuh, I need some time to recharge f-first..."
            show hima_finalbefore_angry with dissolve:
                        zoom 1.25 yalign 0.0
            him"R-recharge...?"
            bot"S-shit!" with vpunch
            bo"I mean... re-adjust the recipe of course!"
            bo"We've been at it for a while now, it's losing some of its culinary properties..."
            scene himablindfold 1 with dissolve
            him"Hmm...."
            bo"It's best we take a break and analyze your feedback for now..."
            bo"After we do that, I'll incorporate your input and have you try it again next time... Deal?"
            him"*Disappointed Sigh*..."
            show himablindfold 1_1 with fade
            him"F-fine... Let me know when I can take this thing off."
            bo"Give me a second to hide the recipe first!" with vpunch
            bo"You wouldn't want to cheat yourself out of the prize money by accidentely taking a peek..."
            him"I will not! I am still gunning for the prize you know!" with vpunch
            bo"In the meantime, feel free to describe what you've tasted and give any feedback you think could be helpful..."
            "You spend some time hiding the 'evidence' while [him_name] recounted the experience..."
            him"It's as you said! The size of it, the warmth, even the texture..."
            him"It all seemed to vary at a moments whim! It was as if it's a living, breathing thing!"
            bo"R-right...?" with vpunch
            bot"*Nervous chuckle*"
            him"I could have sworn I felt it pulsate with life at times..."
            him"You said It was comparable to a popsicle, so I tried to suck on it a little bit..."
            him"And right when I did, I think I squeezed out some of the inner filling of it!"
            him"It felt warm and salty but also... kind of sweet at the same time!"
            him"Right as it was getting interesting, you pulled it away from me!" with vpunch
            call increaselust(10) from _call_increaselust_137
            bot"G-good heavens..."
            bo"Indeed you did squeeze some of it, for that is the intention and the secret behind my recipe..."
            bo"My recipe is special in that regard, just like a popsicle, it may hide some of its flavor deep within it..."
            bo"The more it heats up, and the more one sucks on it..."
            bo"The more of its filling and syrup you'll be able to extract from it."
            him"Aha! So t-that's why it felt like that towards the end!" with vpunch
            him"W-well, my feedback to you would be to maybe have your recipe be sufficiently heated up from the get-go..."
            him"That way the consumer can get to the tasty part quicker!"
            bo"T-that's really insightful feedback [him_name]! Thanks for that..."
            bo"Although heating it up and maintaining the heat may be a challenge in of itself... I am sure I can come up with a few solutions!"
            him"You said it yourself... 'The more heated it is, the more flavor one can extract from it'... or something, right?"
            bo"Indeed! In fact, I am thinking of naming it 'Hot-Cream'! Just like an ice cream, but hot instead of cold! Genius, right?"
            him"That sounds utterly stupid! *Giggles*  Although it does have a certain charm to it I suppose..."
            him"More importantly... You just gave away that it's some sort of dessert!" with vpunch
            bo"I did? Oops..."
            bot"It's not like she has any idea what it could be..."
            him"You did, in fact..." with vpunch
            him"I may know exactly what that was!" with vpunch
            bo"Y-you do...?"
            him"Yeah!" with vpunch
            him"But I am not telling until I can get this blindfold off! I want to see the fear in your eyes as I siphon all the money from your pockets!"
            him"Hee-hee!"
            bo"R-right... I just got done anyway so..."
            scene black with dissolve

            if day_part == 3:
                show himawari_bedroom_2
            else:
                show himawari_bedroom_1
            show hima smugshy at right:
                zoom 0.34
            with dissolve
            him"Hee-heee.... "
            show boruto surprised2 at left with dissolve
            "Without wasting a second, [him_name] took off the blindfold, revealing her mischievous expression..."
            bo"So... Do you actually know what that was?"
            show hima at smallshake
            him"Hee-heee.... I know exactly what that was!" with vpunch
            bo"Y-you do...?"
            show hima at smallshake
            him"Of course!"
            him"The wet, slimy feel of it... The sweet aroma..."
            him"On top of that, knowing that it's a dessert, it must surely be..."
            him"S-some sort of Crème Brûlée! N-no wait..." with vpunch
            show hima worried2 with dissolve
            him"M-maybe a Panna Cotta...?"
            show boruto snob with dissolve
            bo"Th-"
            him"N-no wait! My final answer is..." with vpunch
            show boruto laughing2 with dissolve
            bo"Bwahahah! You can't just list every dessert in the world..."
            show hima embarassed with dissolve
            him"..."
            show hima at smallshake
            him"...Was I wrong again?"
            bot"I can't believe I keep thinking she has any chance to begin with. She is so utterly clueless..."
            show hima worried2 with dissolve
            show boruto at smallshake
            bo"Bwahaha..."
            him"H-hey... cut it out already!"
            show boruto snob with dissolve
            bo"I am s-sorry! Haha... It was neither of the ten desserts you just listed..."
            show hima mad with dissolve
            him"Hmph! D-darn it..." with vpunch
            show hima at smallshake
            him"You aren't lying, are you?"
            bo"Come on... Think about it for a second. It tasted like nothing you've mentioned before, didn't it?"
            him"Hmph! M-maybe not..."
            himt"D-damn it! I thought I'd get it for sure this time..."
            show hima worried2 with dissolve
            him"...When will I have another c-chance to try that then?"
            bo"As soon as I incorporate your valuable feedback into the refinement of my recipe!"
            bo"Thanks for your insight!"
            him"Y-you are welcome..."
            call changeRespect("Himawari",1) from _call_changeRespect_175
            him"Thanks for valuing my opinion so much..."
            show boruto:
                easein 1.5 xpos -800
            bo"Don't sweat it! I'll see you soon..."
            scene black with dissolve
            $ blindfoldrepeat = 3
            jump action_taken
            

            









        "{color=[obediencecolor]}Toy with her...{/color}" if blindfoldfull == True:
            "fill"
            jump repeatableblindfoldmenu
        "{color=[obediencecolor]}????{/color}" if blindfoldfull == False:
            "Complete previous options first..."
            jump repeatableblindfoldmenu

        "{color=[hatredcolor]}Indulge her with disregard!{/color}"(secrethatred = True) if blindfoldfull == True and hatred >= 30:
            pass
        "{color=[lovecolor]}Indulge her with care...{/color}" (secretlove = True)  if blindfoldfull == True and himawari_love >= 3:
            pass
    "test"
        
