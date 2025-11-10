
label ch1_d1_moneyproblems:
    $ hin_location = "livingroom"
    $ him_location = "school"
    show boruto normal with dissolve
    bo"I usually sleep for longer, but there's some commotion in the living room."
    show boruto worried with dissolve
    bo"I should check what's going on..."
    call screen housemap
    $ ui.interact()

default ch1_d1_moneyproblems_completion = False 
label ch1_d1_moneyproblems_mainstory:
    default borutoknockedouthatred = False
    default borutoknockedoutlove = False
    default hinatagropedmoneyprobs = False
    default hinatagropedmoneyprobsstart = False
    default handpushed = False
    default moneyprobshardgroped = False
    if day_number == 1 and ch1_d1_moneyproblems_completion == False:
        $ ch1_d1_moneyproblems_completion = True
        $ completed_intro += 1
        label replay_ch1_d1_moneyproblems_mainstory:
        $ initialize_replay_defaults()
        scene hina opendoor1 with dissolve
        hin"Y-yes I understand. B-but you see, my husband is away..."
        dm "Even so, these premises are on a lease! Someone has to pay for it, one way or another..."
        menu:
            bot"Huh? Something about a lease and payments?"
            "Listen in":
                show hina opendoor1_1 with dissolve
                "Still unnoticed by [hin_name], you sneakily approach from behind."
                bot"I need to find out what's going on..."
          
            
        dm "We have been lenient enough already, but your payments keep falling further and further behind."
        hin"But I have already told you, [na_name] is away... This will all be taken care of as soon as he is back!"
        dm "We are well aware of [na_name]'s circumstances. I am afraid that changes nothing..."
        dm "If you don't find a way to cover the installments, we will be forced to look into... alternative solutions."
        bot"[hin_rel] never told us anything about this..."
        menu:
            bot"What should I do..."
            "{color=[hatredcolor]}Grope her!{/color}":
                if introsecrethatredcummed == True or secretscenelovehandjob == True:
                    bot"After what happened yesterday, I need to feel more of her..."
                $ hinatagropedmoneyprobsstart = True
                bot"[hin_rel] hasn't realized I am here yet. What if I..."
                $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                show hinagropemoneyproblems with vpunch
                call changeHatred(1, "none") from _call_changeHatred_46
                $ renpy.sound.play("/audio/soun_fx/grope1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                bot"Did this!"
                show hinagropemoneyproblems:
                    zoom 1.7 xalign 0.5 yalign 0.7
                "You used the opportunity to cop a feel of [hin_name]'s ass, knowing she couldn't make a scene in that moment."
                bot"My lord, so... squishy. I just want to give it a little-"
                hide hinagropemoneyproblems
                pause 0.3
                menu:
                    bot"My lord, so... squishy. I just want to give her a little-"
                    "Give her a little 'love' tap":
                        pass
                    
                    
                $ renpy.sound.play("/audio/soun_fx/spank4.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                show hina opendoor1_4 with dissolve
                $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                hin"Aaah!" with vpunch
                show hina opendoor1_5 with dissolve:
                    zoom 1.3
                "She let out a loud squeel and pushed your hand away..."
                scene black with dissolve
                "You pushed the front-door open to reveal yourself to whoever was behind it..."
                scene bg porch with dissolve
                show demandingmen badguys1 with dissolve
                dm "Huh!? What gives woman, why the loud squeels! Is this some sort of ploy to try and get out of this?"
                show demandingmen badguys1:
                    easein 0.6 xpos 0.99
                show shina surprised3 at left with dissolve
                show boruto sceeming at left behind shina with dissolve:
                    xalign 0.3
                call changeRespect("Hinata", -1, "none") from _call_changeRespect_80
                hin"N-no! I am sorry, I was  s-startled by..."
                menu:
                    hin"N-no! I am sorry, I was  s-startled by..."
                    "{color=[dominancecolor]}'Your husband'{/color}":
                        "You cut her off before she could finish her sentence..."
                        call changeDominance(1,"none") from _call_changeDominance_32
                        show boruto smirk2 with dissolve
                        bo"Your husband! Right honey?" with vpunch
                        show shina surprised5 with dissolve
                        hint"What the hell is he doing! I have no choice but to play along with his stupid plan..."
                        jump husbandpath
                        
                    "{color=[lovecolor]}Step in and protect her{/color}":
                        hin"N-no! I am sorry, I was  s-startled by my [hin_rel_to_bo]..."
                        show shina concerned behind boruto
                        bo"Let me handle this [hin_rel]..."
                        jump stepinandprotecther
                    
                label talktodm:
                    show boruto surprised with dissolve
                    bot"O-oh shit! These guys look... menacing."
                    show boruto normal with dissolve
                
                    bot"But they also look... non-native. Something smells fishy here"
                    bot"S-should I say something?"
                    menu:
                        bot"S-should I say something?"
                        "{color=[lovecolor]}Try to defend [hin_name]{/color}":
                            show boruto angry with dissolve
                            bo"[hin_rel], are these people harassing you?"
                            hin"Don't worry abo-"
                            show boruto pissy with dissolve:
                                easein 0.3 xpos 0.20
                            bo"Hey y-you! Aren't you ashamed of extorting a woman? Why don't you pick on someone your own s-size!"
                            show shina:
                                easein 0.3 xpos -0.20
                            show boruto pissy:
                                easein 0.3 xpos 0.10
                            show demandingmen badguys1:
                                easein 0.6 xpos 0.75
                            dm "And who's that going to be little man..."
                            show demandingmen badguys2 with dissolve
                            dm "Surely you did not mean... yourself!? Hahahah *Cackling*"
                            call changeRespect("Hinata", 2, "none") from _call_changeRespect_81
                            show boruto angry with dissolve
                            hin"[bo_name_stutter]..."
                            bot"Fucking assholes..."
                            dm "Listen here little twerp... This is no extortion at all, we are only doing our jobs here. Mandated by the bureau itself."
                            show demandingmen badguys1 with dissolve
                            dm "You have a problem with that, try your luck with them. Heh!"
                            menu:
                                dm "You have a problem with that, try your luck with them. Heh!"
                                "...":
                                    bo"..."
                                "I might do just that":
                                    bo"I might do just that and expose your obvious farce..."
                                    dm"Heh! Be my guest, kid. You'd be only wasting your time."
                                "{color=[dominancecolor]}How about I try my luck with you idiots!{/color}":
                                    show boruto angry2:
                                        easein 0.3 xpos 0.20
                                    call changeDominance(1) from _call_changeDominance_33
                                    bo"How about I try my luck with you idiots!"
                                    show demandingmen badguys2:
                                        linear 0.2 xpos 0.5
                                    pause 0.4
                                    scene black with vpunch and flash
                                    pause 0.5
                                    dm"I've had it with this kid..."
                                    "A quick flick of his fingers to your forehead puts you to sleep..."
                                    show bg porch
                                    show shina surprised5 at left:
                                        zoom 0.95 ypos 1.05
                                    show demandingmen badguys2 behind shina:
                                        zoom 1.1 xpos 240
                                    with dissolve
                                    show shina at smallshake
                                    hin"W-what did you do! Y-"
                                    dm"Heh! Don't fret woman. I softened the blow, the child will be fine. You better teach him some manners otherwise next time I won't be as lenient..." with vpunch
                                    show shina angry3 with dissolve
                                    hin"You think I'll let this go you charlatans!? You attacked my son!"
                                    show shina assertive with dissolve
                                    hin"The Hokage will hear of this, there will be consequences!"
                                    show demandingmen badguys1 with dissolve:
                                        easein 0.5 xpos 170
                                    dm"C-consequences...?"
                                    show demandingmen badguys1:
                                        easein 0.5 xpos 150
                                    dm"From the Hokage himself?"
                                    show demandingmen badguys1:
                                        easein 0.5 xpos 130
                                    dm"Whatever shall we do..."
                                    show demandingmen badguys2:
                                        easein 0.3 xpos 30
                                    show shina concerned at smallshake
                                    dm"HA! Don't make me laugh woman!" with vpunch
                                    show demandingmen badguys2:
                                        easein 2 subpixel True xpos -100
                                    dm"Listen here, Little lady of the leaf..."
                                    show shina surprised4 at smallshake
                                    "The big man leans over [hin_name]'s shoulder..."
                                    show interhina1 with dissolve
                                    "And whispers in her ear with a threatening tone..."
                                    dm"When the Hokage hears of this, please do let him know that his [hin_rel_to_bo] was the aggressor in the first place..."
                                    dm"Perhaps we could settle that in court if you'd prefer to continue carelessly throwing accusations around!" with vpunch
                                    show interhina1 with dissolve:
                                        zoom 1.1 xalign 0.0
                                    dm"More importantly, do inform the Hokage that the Raikage himself wants to have a word with him..."
                                    show interhina2 with vpunch:
                                        zoom 1.0 xalign 0.0 yalign 0.4
                                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp3.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                    hin"*Gasps*"
                                    "Having felt his coarse hand at the back of her neck, [hin_name] let out a sharp audible gasp trying to conceal her obvious anxiety..."
                                    "The man brazenly brushed the back of her ear and run his coarse fingers through her hair while softly directing her gaze towards him."
                                    "[hin_name] could not believe that a man who knew full well of her marital status to [na_name], would so carelessly push himself on her..."
                                    "She could sense a certain kind of fear that would very rarely inhibit her..."
                                    "And so, she stood motionless while the threatening man's breath kept brushing across her cheek..."
                                    show interhina2 with vpunch:
                                        zoom 1.1 xalign 0.0 yalign 0.4
                                    dm"Until then, make sure you start conforming to your obligations. Otherwise..."
                                    show interhina2 with dissolve:
                                        zoom 1.2 xalign 0.0 yalign 0.4
                                    dm"It is not us who will suffer the consequences..."
                                    show interhina2_1 with dissolve:
                                        zoom 1.5 xalign 0.5 yalign 0.4
                                    dm"I am afraid that'll be you missy!" with vpunch
                                    scene interhina2_1 with dissolve
                                    scene black with vpunch
                                    dm"Toji! Enough..."
                                    show hina closet5t with dissolve
                                    "The man took one last good look at [hin_name]'s bottom before backing off..."
                                    hide hina with dissolve
                                    scene bg porch
                                    show demandingmen badguys2
                                    show demandingmen badguys2:
                                        easein 0.8 xpos 0.8
                                    show shina surprised4 at left:
                                        zoom 0.9
                                    with dissolve
                                    dm"I truly hope you get to see your husband soon... *Chuckles*"
                                    
                                    dm"Although, something's telling me that'll take a while..."
                                    show demandingmen:
                                        easeout 1 xpos 2000
                                    dm"We'll see you soon, Lady of the leaf!"
                                    pause 0.3
                                    show shina concerned:
                                        easein 0.5 xalign 0.5
                                    hin"H-hey wait! What does that mean!"
                                    hin"..."
                                    
                                    hide demandingmen with dissolve
                                    $ borutoknockedoutlove = True
                                    jump moneyproblemsend
                                    
                                
                            dm "We will be back next week. If you can't make the payment, know that there will be... consequences!"
                            label menleavelove:
                                hide demandingmen with dissolve
                                show shina at left
                                show boruto normal at right
                                with dissolve
                                hin"Y-you didn't have to do that [bo_name]..."
                                hin"Don't put yourself in danger for me!"
                                bo"If not for you, then who else [hin_rel]..."
                                show boruto smirk with dissolve
                                bo"Besides, what danger? I could probably take these guys on!"
                                call changeLove("Hinata",1, "none") from _call_changeLove_21
                                hin"I don't think violence is how you solve a problem like this... B-but thank you, for standing up for me."
                                hin"Come on, Let's go inside..."
                                scene black with dissolve
                                call narutointermission from _call_narutointermission
                                jump moneyprobendingconv
                        "Question their motives":
                            bo"Who the hell are you people and why are you here..."
                            show shina:
                                easein 0.3 xpos -0.20
                            show boruto normal:
                                easein 0.3 xpos 0.10
                            show demandingmen badguys1:
                                easein 0.6 xpos 0.75
                            dm "Relax little man... We are only doing our jobs here."
                            menu:
                                bot"..."
                                "Poke fun at them...":
                                    show boruto sceeming with dissolve
                                    bo"And why would two gorilla-looking men have a job to do in Konoha. You two look like you came straight from the close-by jungle."
                                    show demandingmen badguys2 with dissolve
                                    dm "Don't overstep your boundaries little twerp, lest you want more problems to deal with."
                                    show boruto angry with dissolve
                                    dm "We are mandated to carry out our duties by the bureau itself."
                                    dm "You have a problem with that, try your luck with them, Heh!"
                                    bo"..."
                                    show demandingmen badguys1 with dissolve
                                    dm "We will be back next week. If you can't make the payment, know that there will be... consequences!"
                                    hide demandingmen with dissolve
                                    jump menleavelove
                                "Jobs? You don't look like natives to me":
                                    show boruto worried with dissolve
                                    bo"You don't look like locals to me, why would you be responsible for something like this?"
                                    dm "Well, you got us... Time to pack our things and go back to our place, eh Toji?"
                                    show demandingmen badguys2 with dissolve
                                    dm"*Cackling*... Listen here boy, we are  mandated to carry out our duties by the bureau itself."
                                    "Toji""You have a problem with that, take it up with them... Understood?"
                                    show boruto angry with dissolve
                                    bot"..."
                                    show demandingmen badguys1 with dissolve
                                    dm "We will be back next week. If you can't make the payment, know that there will be... consequences!"
                                    hide demandingmen with dissolve
                                    jump menleavelove
                                
                        "{color=[dominancecolor]}What are you retards babbling about{/color}":
                            show boruto sceeming with dissolve
                            call changeDominance(1, "none") from _call_changeDominance_34
                            bo"What are you retards babbling about. I can see straight through your farce..."
                            show shina surprised2:
                                easein 0.3 xpos -0.20
                            show boruto sceeming:
                                easein 0.3 xpos 0.10
                            show demandingmen badguys2:
                                easein 0.6 xpos 0.65
                            dm"What did you call us you little twerp!? Huh!?" with vpunch
                            show demandingmen badguys2:
                                easein 0.6 xpos 0.75
                            dm"Take it easy, Toji. The little kid's just running his mouth... besides, I don't think we have authority to beat him up... yet."
                            show demandingmen badguys1 with dissolve:
                                easein 0.6 xpos 0.75
                            dm"Hah! Stupid kid..."
                            "The smaller one of the two stops the other from turning violent..."
                            dm"We have full authority to exercise our duties by the bureau itself..."
                            menu:
                                dm"We have full authority to exercise our duties by the bureau itself..."
                                "{color=[hatredcolor]}Piss off before I kill you!{/color}":
                                    call changeHatred(1,"none") from _call_changeHatred_47
                                    show boruto angry2 with dissolve
                                    bo"And I have full authority to kill you myself next time I see you here you gorilla-looking like bozos."
                                    show shina surprised3 with dissolve
                                    show boruto angry2:
                                        easein 0.3 xpos 0.20
                                    bo"Now piss off!" with vpunch
                                    show demandingmen badguys2:
                                        linear 0.2 xpos 0.5
                                    pause 0.4
                                    scene black with vpunch and flash
                                    pause 0.5
                                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                                    hin"[bo_name_stutter]!" with vpunch
                                    dm"I've had it with this kid..."
                                    "A quick flick of his fingers to your forehead puts you to sleep..."
                                    show bg porch
                                    show shina surprised5 at left:
                                        zoom 0.95 ypos 1.05
                                    show demandingmen badguys2 behind shina:
                                        zoom 1.1 xpos 240
                                    with dissolve
                                    show shina at smallshake
                                    hin"W-what did you do! Y-"
                                    dm"Heh! Don't fret woman. I softened the blow, the child will be fine. You better teach him some manners otherwise next time I won't be as lenient..." with vpunch
                                    show shina angry3 with dissolve
                                    hin"You think I'll let this go you charlatans!? You attacked my son!"
                                    show shina assertive with dissolve
                                    hin"The Hokage will hear of this, there will be consequences!"
                                    show demandingmen badguys1 with dissolve:
                                        easein 0.5 xpos 170
                                    dm"C-consequences...?"
                                    show demandingmen badguys1:
                                        easein 0.5 xpos 150
                                    dm"From the Hokage himself?"
                                    show demandingmen badguys1:
                                        easein 0.5 xpos 130
                                    dm"Whatever shall we do..."
                                    show demandingmen badguys2:
                                        easein 0.3 xpos 30
                                    show shina concerned at smallshake
                                    dm"HA! Don't make me laugh woman!" with vpunch
                                    show demandingmen badguys2:
                                        easein 2 subpixel True xpos -100
                                    dm"Listen here, Little lady of the leaf..."
                                    show shina surprised4 at smallshake
                                    "The big man leans over [hin_name]'s shoulder..."
                                    show interhina1 with dissolve
                                    "And whispers in her ear with a threatening tone..."
                                    dm"When the Hokage hears of this, please do let him know that his [hin_rel_to_bo] was the aggressor in the first place..."
                                    dm"Perhaps we could settle that in court if you'd prefer to continue carelessly throwing accusations around!" with vpunch
                                    show interhina1 with dissolve:
                                        zoom 1.1 xalign 0.0
                                    dm"More importantly, do inform the Hokage that the Raikage himself wants to have a word with him..."
                                    show interhina2 with vpunch:
                                        zoom 1.0 xalign 0.0 yalign 0.4
                                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp3.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                    hin"*Gasps*"
                                    "Having felt his coarse hand at the back of her neck, [hin_name] let out a sharp audible gasp trying to conceal her obvious anxiety..."
                                    "The man brazenly brushed the back of her ear and run his coarse fingers through her hair while softly directing her gaze towards him."
                                    "[hin_name] could not believe that a man who knew full well of her marital status to [na_name], would so carelessly push himself on her..."
                                    "She could sense a certain kind of fear that would very rarely inhibit her..."
                                    "And so, she stood motionless while the threatening man's breath kept brushing across her cheek..."
                                    show interhina2 with vpunch:
                                        zoom 1.1 xalign 0.0 yalign 0.4
                                    dm"Until then, make sure you start conforming to your obligations. Otherwise..."
                                    show interhina2 with dissolve:
                                        zoom 1.2 xalign 0.0 yalign 0.4
                                    dm"It is not us who will suffer the consequences..."
                                    show interhina2_1 with dissolve:
                                        zoom 1.5 xalign 0.5 yalign 0.4
                                    dm"I am afraid that'll be you missy!" with vpunch
                                    scene interhina2_1 with dissolve
                                    scene black with vpunch
                                    dm"Toji! Enough..."
                                    show hina closet5t with dissolve
                                    "The man took one last good look at [hin_name]'s bottom before backing off..."
                                    hide hina with dissolve
                                    scene bg porch
                                    show demandingmen badguys2
                                    show demandingmen badguys2:
                                        easein 0.8 xpos 0.8
                                    show shina surprised4 at left:
                                        zoom 0.9
                                    with dissolve
                                    dm"I truly hope you get to see your husband soon... *Chuckles*"
                                    
                                    dm"Although, something's telling me it could take a while until you do..."
                                    show demandingmen:
                                        easeout 1 xpos 2000
                                    dm"We'll see you soon, Lady of the leaf!"
                                    pause 0.3
                                    show shina concerned:
                                        easein 0.5 xalign 0.5
                                    
                                    hin"H-hey wait! What does that mean!"
                                    hin"..."
                                    hide demandingmen with dissolve
                                    $ borutoknockedouthatred = True
                                    jump moneyproblemsend



            "{color=[lovecolor]}Step in and protect her{/color}":
                bo"[hin_rel], let me handle this."
                scene black with dissolve
                "You pushed the front-door open to reveal yourself to whoever was behind it..."
                scene bg porch with dissolve
                show demandingmen badguys1 with dissolve
                show demandingmen badguys1:
                    easein 0.6 xpos 0.99
                label stepinandprotecther:
                    show shina concerned at left with dissolve
                    show boruto normal at left with dissolve:
                        xalign 0.3
                    hin"[bo_name_stutter]... you weren't supposed to be here."
                    bo"I am now, don't worry, I'll take care of this"
                    call changeLove("Hinata", 1 ,"none") from _call_changeLove_22
                    hin"..."
                    show demandingmen badguys1:
                        easein 0.6 xpos 0.75
                    show shina concerned at left:
                        easein 0.3 xpos -0.20
                    show boruto normal:
                        easein 0.3 xpos 0.10
                    dm"What's up kid, no school for you this morning? Heh!"
                    jump talktodm
                
            "{color=[dominancecolor]}Step in pretending you are the husband{/color}":
                bot"I hope this works or I'll look extremely stupid..."
                "You pushed the front-door open to reveal yourself to whoever was behind it..."
                scene bg porch with dissolve
                show demandingmen badguys1 with dissolve
                label husbandpath:
                    show demandingmen badguys1:
                        easein 0.6 xpos 0.99
                    show shina shy at left with dissolve
                    show boruto snob at left behind shina with dissolve:
                        xalign 0.3
                    bo"Who dares to harass my lovely wife..."
                    dm"Your... Wife?"
                    show boruto smirk:
                        easein 0.3 xpos 0.26
                    show shina concerned with dissolve

                    show shinapretend1:
                        zoom 0.5 xalign 0.9 yalign 0.1
                    
                    show cutoutborder_white:
                        zoom 0.75 pos (559, -109)
                    with dissolve
                    call changeDominance(1,"none") from _call_changeDominance_35
                    "You confidently grab [hin_name]'s waist, pretending to be her husband..."
                    hin"[bo_name_stutter], w-what are you-"
                    bo"It's okay, [hin_name]... Let me handle this"
                    hide shinapretend1
                    hide cutoutborder_white
                    with dissolve
                    
                    dm"Hey kid, we know who you a-"
                    menu:
                        dm"Hey kid, we know who you a-"
                        "{color=[obediencecolor]}Lower your hand and keep up the facade{/color}":
                            $ hinatagropedmoneyprobs = True
                            show boruto sceeming with dissolve
                            bo"You try and extort my lovely wife? Then you have a problem with me!"
                            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp4.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                            show shina surprised2 at shake
                            hin"A-ah!"
                            show shinapretend2:
                                zoom 0.5 xalign 0.9 yalign 0.1
                            
                            show cutoutborder_white:
                                zoom 0.75 pos (559, -109)
                            with dissolve
                            "You lower your hand and firmly place it on your [hin_rel]'s bottom. As both parties were facing each other, your move would not be immediately obvious to them..."
                            call checkObedience(4,"none","Hinata") from _call_checkObedience_9
                            if hinata_obedience >= 4:
                                hin"W-what are you doing, [bo_name_stutter]?"
                                call changeObedience("Hinata", 2, "none") from _call_changeObedience_49
                                show shina surprised4 with dissolve and vpunch
                                show hinagropemoneyproblems2:
                                    zoom 0.5 xalign 0.9 yalign 0.1
                                $ renpy.sound.play("/audio/soun_fx/groperepeat1.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                                "[hin_name] put up with your... plan. Even while you used the opportunity to feel her up as much as you could..."
                                bo"It's ok, my dear wife... let me deal with this."
                                hide shinapretend2
                                hide cutoutborder_white
                                hide hinagropemoneyproblems2
                                with dissolve
                            else:
                                show shina angry with dissolve
                                show shinapretend4 with dissolve:
                                    zoom 0.5 xalign 0.9 yalign 0.1
                                hin"S-stop it, [bo_name_stutter]!"
                                call changeLove("Hinata", -1, "none") from _call_changeLove_23
                                
                                "She pushes your hand away in discontent..."
                                show shina shy2 with dissolve
                                $ handpushed = True
                                hide shinapretend4
                                hide shinapretend2
                                hide cutoutborder_white
                                with dissolve
                                show shina shy2
                                show boruto surprised with dissolve
                                bot"Shit, I fucked up! But I am in too deep now..."
                                bo"It's o-okay, my w-wife... let me deal with this."
                            show demandingmen badguys1:
                                easein 0.6 xpos 0.75
                            show shina concerned at left:
                                easein 0.3 xpos -0.20
                            show boruto normal:
                                easein 0.3 xpos 0.10
                            dm"There's nothing to deal with here little guy..."
                            dm"As I was saying, we know who you are. Besides, your... wife here *chuckles* already told us her husband was away..."
                            show boruto surprised with dissolve
                            if handpushed == False:
                                show shinapretend4:
                                    zoom 0.5 xalign 0.9 yalign 0.1
                                show cutoutborder_white:
                                    zoom 0.75 pos (559, -109)
                                with dissolve
                                call changeRespect("Hinata", -1, "none") from _call_changeRespect_82
                                "[hin_name] pushes your hand away..."
                                hide shinapretend4
                                hide cutoutborder_white
                                with dissolve
                            bot"I am such an idiot..."
                            show demandingmen badguys2 with dissolve
                            dm"Unless you mean to tell us that she is a... common whor-"
                            dm"Ahem!" with vpunch
                            show demandingmen badguys1 with dissolve
                            show boruto angry with dissolve
                            
                            "The smaller of the two stopped the bigger one mid-sentence..."
                            dm"Let us all drop the charades, shall we?"
                            jump whatdidyousayaboutmy


                            
                        "{color=[hatredcolor]}Use the opportunity to grope her!{/color}":
                            $ hinatagropedmoneyprobs = True 
                            $ moneyprobshardgroped = True
                            bo"You idiots think you can mess with my wife?"
                            show boruto sceeming with dissolve
                            show shina surprised2 with dissolve
                            bo"Only I get to do that!" with vpunch
                            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                            show shina surprised3 at shake
                            show boruto sceeming2 with dissolve
                            hin"[bo_name_stutter]!?"
                            show shinapretend2:
                                zoom 0.5 xalign 0.9 yalign 0.1
                            
                            show cutoutborder_white:
                                zoom 0.75 pos (559, -109)
                            with dissolve
                            
                            "As both parties were facing each other, your bold move would not be immediately obvious to them.."
                            call changeRespect("Hinata", -2 ,"none") from _call_changeRespect_83
                            "[hin_name] was irritated, both by your comments and your actions, but she couldn't protest right then and there..."
                            show hinagropemoneyproblems2:
                                zoom 0.5 xalign 0.9 yalign 0.1
                            
                            show boruto sceeming3 with dissolve
                            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp4.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                            show shina surprised5 with vpunch
                            $ renpy.sound.play("/audio/soun_fx/groperepeat1.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                            "You took the opportunity to go as far as you could given the circumstances..."
                            hin"A-ah!" with vpunch
                            "[hin_name] recoiled upwards as you started forcibly playing with her ass"
                            bo"It's okay, dear wife. I am in control now!"
                            hide hinagropemoneyproblems2
                            hide cutoutborder_white
                            hide shinapretend2
                            with dissolve
                            show demandingmen badguys1:
                                easein 0.6 xpos 0.75
                            show shina concerned at left:
                                easein 0.3 xpos -0.20
                            show boruto normal:
                                easein 0.3 xpos 0.10
                            dm"Kid... as I was saying, we know who you are. Besides, your... wife here already told us her husband was away..."
                            show boruto surprised with dissolve
                            show shinapretend4:
                                zoom 0.5 xalign 0.9 yalign 0.1
                            
                            show cutoutborder_white:
                                zoom 0.75 pos (559, -109)
                            with dissolve
                            call changeLove("Hinata", -2, "none") from _call_changeLove_24
                            "[hin_name] pushes your hand away..."
                            hide shinapretend4
                            hide cutoutborder_white
                            with dissolve
                            hint"Y-you idiot!"
                            bot"Shit! I really fucked this one up..."
                            show demandingmen badguys2 with dissolve
                            show boruto angry with dissolve
                            dm"Unless you mean to tell us that she is a... common whor-"
                            dm"Ahem!" with vpunch
                            show demandingmen badguys1 with dissolve
                            show boruto angry with dissolve
                            "The smaller of the two stopped the bigger one mid-sentence..."
                            dm"Let us all drop the charades, shall we?"
                            jump whatdidyousayaboutmy
                           
                        "{color=[lovecolor]}'You'll have to deal with me now'{/color}":
                            $ hinatagropedmoneyprobs = False
                            show boruto angry with dissolve
                            bo"You mess with my wife you mess with me!"
                            bo"You are dealing with someone your size now..."
                            show shina:
                                easein 0.3 xpos -0.20
                            show boruto angry:
                                easein 0.3 xpos 0.10
                            show demandingmen badguys1:
                                easein 0.6 xpos 0.75
                            dm "And who exactly is that little man..."
                            show demandingmen badguys2 with dissolve
                            dm "Surely you did not mean... yourself!? Hahahah *Cackling*"
                            call changeRespect("Hinata", 1, "none") from _call_changeRespect_84
                            show boruto angry with dissolve
                            hin"[bo_name_stutter]..."
                            bot"Fucking assholes..."
                            dm "Listen here little twerp... This is no extortion at all, we are only doing our jobs here. Mandated by the bureau itself."
                            show demandingmen badguys2 with dissolve
                            dm"Besides... we know exactly who you are, and you definitely are no husband to anyone! *Cackling*" with vpunch
                            dm"Unless you mean to tell us that your [hin_rel] here is a common whor-"
                            dm"Ahem!" with vpunch
                            show demandingmen badguys1 with dissolve
                            show boruto angry with dissolve
                            "The smaller of the two stopped the bigger one mid-sentence..."
                            dm"Let us all drop the charades, shall we?"
                            menu whatdidyousayaboutmy:
                                dm"Let us all drop the charades, shall we?"
                                "{color=[dominancecolor]}What did you say about my [hin_rel]?{/color}":
                                    show boruto angry:
                                        easein 0.3 xpos 0.15
                                    bo"What did you call my [hin_rel] again, you big fat fuck?"
                                    show shina surprised2 with dissolve
                                    hin"[bo_name], stop it..."
                                    show demandingmen badguys2 with dissolve
                                    dm"It was just a joke little man, relax..."
                                    show boruto angry2:
                                        easein 0.3 xpos 0.20
                                    call changeDominance(1,"none") from _call_changeDominance_36
                                    bo"You don't get to disrespect my [hin_rel] like that!" with vpunch
                                    bo"I'll beat your fucking face in motherfucker!" with vpunch
                                    show demandingmen badguys1:
                                        linear 0.2 xpos 0.5
                                    pause 0.4
                                    scene black with vpunch and flash
                                    dm"You ain't beating shit, little twerp!"
                                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                                    hin"[bo_name_stutter]!" with vpunch
                                    pause 0.5
                                    "A quick flick of his fingers to your forehead puts you to sleep..."
                                    show bg porch
                                    show shina surprised5 at left:
                                        zoom 0.95 ypos 1.05
                                    show demandingmen badguys2 behind shina:
                                        zoom 1.1 xpos 240
                                    with dissolve
                                    show shina at smallshake
                                    hin"W-what did you do! Y-"
                                    dm"Heh! Don't fret woman. I softened the blow, the child will be fine. You better teach him some manners otherwise next time I won't be as lenient..." with vpunch
                                    show shina angry3 with dissolve
                                    hin"You think I'll let this go you charlatans!? You attacked my son!"
                                    show shina assertive with dissolve
                                    hin"The Hokage will hear of this, there will be consequences!"
                                    show demandingmen badguys1 with dissolve:
                                        easein 0.5 xpos 170
                                    dm"C-consequences...?"
                                    show demandingmen badguys1:
                                        easein 0.5 xpos 150
                                    dm"From the Hokage himself?"
                                    show demandingmen badguys1:
                                        easein 0.5 xpos 130
                                    dm"Whatever shall we do..."
                                    show demandingmen badguys2:
                                        easein 0.3 xpos 30
                                    show shina concerned at smallshake
                                    dm"HA! Don't make me laugh woman!" with vpunch
                                    show demandingmen badguys2:
                                        easein 2 subpixel True xpos -100
                                    dm"Listen here, Little lady of the leaf..."
                                    show shina surprised4 at smallshake
                                    "The big man leans over [hin_name]'s shoulder..."
                                    show interhina1 with dissolve
                                    "And whispers in her ear with a threatening tone..."
                                    dm"When the Hokage hears of this, please do let him know that his [hin_rel_to_bo] was the aggressor in the first place..."
                                    dm"Perhaps we could settle that in court if you'd prefer to continue carelessly throwing accusations around!" with vpunch
                                    show interhina1 with dissolve:
                                        zoom 1.1 xalign 0.0
                                    dm"More importantly, do inform the Hokage that the Raikage himself wants to have a word with him..."
                                    show interhina2 with vpunch:
                                        zoom 1.0 xalign 0.0 yalign 0.4
                                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp3.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                    hin"*Gasps*"
                                    "Having felt his coarse hand at the back of her neck, [hin_name] let out a sharp audible gasp trying to conceal her obvious anxiety..."
                                    "The man brazenly brushed the back of her ear and run his coarse fingers through her hair while softly directing her gaze towards him."
                                    "[hin_name] could not believe that a man who knew full well of her marital status to [na_name], would so carelessly push himself on her..."
                                    "She could sense a certain kind of fear that would very rarely inhibit her..."
                                    "And so, she stood motionless while the threatening man's breath kept brushing across her cheek..."
                                    show interhina2 with vpunch:
                                        zoom 1.1 xalign 0.0 yalign 0.4
                                    dm"Until then, make sure you start conforming to your obligations. Otherwise..."
                                    show interhina2 with dissolve:
                                        zoom 1.2 xalign 0.0 yalign 0.4
                                    dm"It is not us who will suffer the consequences..."
                                    show interhina2_1 with dissolve:
                                        zoom 1.5 xalign 0.5 yalign 0.4
                                    dm"I am afraid that'll be you missy!" with vpunch
                                    scene interhina2_1 with dissolve
                                    scene black with vpunch
                                    dm"Toji! Enough..."
                                    show hina closet5t with dissolve
                                    "The man took one last good look at [hin_name]'s bottom before backing off..."
                                    hide hina with dissolve
                                    scene bg porch
                                    show demandingmen badguys2
                                    show demandingmen badguys2:
                                        easein 0.8 xpos 0.8
                                    show shina surprised4 at left:
                                        zoom 0.9
                                    with dissolve
                                    dm"I truly hope you get to see your husband soon... *Chuckles*"
                                    
                                    dm"Although, something's telling me that'll take a while..."
                                    show demandingmen:
                                        easeout 1 xpos 2000
                                    dm"We'll see you soon, Lady of the leaf!"
                                    pause 0.3
                                    show shina concerned:
                                        easein 0.5 xalign 0.5
                                    
                                    hin"H-hey wait! What does that mean!"
                                    hin"..."
                                    hide demandingmen with dissolve
                                    $ borutoknockedoutlove = True
                                    jump moneyproblemsend

                                "..." if hinatagropedmoneyprobs == False:
                                    bo"..."
                                
                            dm"Listen kid, your... [hin_rel_mother] here is in deep trouble and there's nothing you can do about it"
                            dm"We have full authority to exercise our duties by the bureau itself..."
                            dm"You have a problem with that, take it up with them... Understood?"
                            dm "We will be back next week. If you can't make the payment, know that there will be... consequences!"
                            hide demandingmen with dissolve
                            jump menleavelove


                
    label moneyproblemsend:
        
        scene black with dissolve
        call narutointermission from _call_narutointermission_1
        if borutoknockedoutlove == True or borutoknockedouthatred == True:
            "[hin_name] drags you back inside after the men left..."
            if borutoknockedoutlove == True or borutoknockedouthatred == True:
                scene inside1 with dissolve
                hin"[bo_name]!" with vpunch
                hin"[bo_name_stutter] please! Wake up!"
                scene black with dissolve
                show inside2:
                    blur 15 zoom 1.3 subpixel True
                call blink("...", hin_rel + "...?","...") from _call_blink_2
                show inside2:
                    easein 2 xalign 0.5 yalign 0.8 blur 5 zoom 1.3 subpixel True
                hin"Oh thank the heavens!"
                bot"Right... I got knocked out."
                bot"And now... [hin_rel] is on top of me...?"
                show inside2:
                    easein 3 xalign 0.5 yalign 0.9 blur 0 zoom 1.3 subpixel True
                bot"Damn..."
                call increaselust(10) from _call_increaselust_43
                bot"Her and her oversized sweater. To think this is how I'd finally see what's beneath it..."
                hin"[bo_name]! Can you hear me?"
                bot"[hin_rel]'s tits, they are fucking sublime. She could knock me out anytime if this is what it'd be like..."
                show inside3 with dissolve:
                    xalign 0.5 yalign 0.95 zoom 1.35
                call increaselust(10) from _call_increaselust_44
                bot"Shit, I am getting a massive boner from feeling her body's warmth..."
                bot"Maybe I can pretend I am dreaming or something..."
                hin"Please, say something!"
                menu:
                    hin"Please, say something!"
                    "{color=[dominancecolor]}Grab her chest{/color}":
                        show inside3 with dissolve:
                            xalign 0.5 yalign 0.5 zoom 1.0
                        bo"Where..."
                        show inside5 with vpunch
                        call changeDominance(1, "none") from _call_changeDominance_37
                        pause 2
                        bo"...Am I?"
                        show inside6 with dissolve:
                            zoom 1.1 xalign 0.01 yalign 0.01
                        $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp3.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                        hin"[bo_name_stutter]!?" with vpunch
                        show inside6 with dissolve:
                            zoom 1.2 xalign 0.01 yalign 0.01
                        hin"Y-you a-are home! it's me your [hin_rel]..."
                        show inside6 with dissolve:
                            zoom 1.2 xalign 1.0 yalign 1.0
                        bot"Feels so soft... and squishy! I don't want to ever let go..."
                        scene black with dissolve
                        bot"But I don't want [hin_rel] to get suspicious..."
                        "[hin_name] quickly got up, recoiling back from your unexpected move..."
                        bo"O-oh... M-my head hurts a bit still..."
                        

                    "I am okay [hin_rel], but... my condition":
                        show inside3:
                            easein 3 xalign 0.5 yalign 0.01 blur 0 zoom 1.1 subpixel True
                        bot"Nah I shouldn't worry her any more than I already am..."
                        bo"I am okay, [hin_rel]..."
                        show inside3 with dissolve:
                            zoom 1.0 xalign 0.5 yalign 0.5
                        hin"[bo_name]! Are you alright!?"
                        show inside4 with dissolve:
                            easein 3 xalign 0.5 yalign 0.99 blur 0 zoom 1.4 subpixel True
                        pause 1
                        bo"Yeah but uuh... could you maybe not be on top of me? I might have a small problem with my... condition"
                        show inside6 with dissolve:
                            zoom 1.5 xalign 0.01 yalign 0.01
                        $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                        hin"O-oh!" with vpunch
                        scene black with dissolve
                        show shina concerned behind black
                        hin"I am s-sorry! I- I didn't even consider that..."
                        scene bg lr_day with dissolve
                        show boruto surprised2 at left with dissolve
                        show shina concerned behind boruto
                        show shina surprised3 with dissolve:
                            easein 1 xpos 0.55
                        "[hin_name] quickly gets up and away from you realizing what she involuntarily caused..."
                        show boruto worried2 with dissolve
                        bo"I should be fine... [hin_rel]. I'll be taking care of that later..."
                        call changeObedience("Hinata", 1, "none") from _call_changeObedience_50
                        show shina concerned with dissolve
                        hin"O-okay..."

                    "Stay silent...":
                        show inside3 with dissolve:
                            xalign 0.5 yalign 0.5 zoom 1.0
                        bot"If I say nothing maybe she'll stay on top of me..."
                        bot"But my erection is growing bigger, it's almost rubbing against her stomach..."
                        hin"Come on [bo_name]! Can you not hear me!?"
                        show inside4 with dissolve:
                            easein 3 xalign 0.5 yalign 0.8 zoom 1.2
                        call increaselust(10) from _call_increaselust_45
                        show inside6 with dissolve:
                            xalign 0.5 yalign 0.01 zoom 1.5
                        $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                        hin"O-oh!" with vpunch
                        call changeObedience("Hinata", 1, "none") from _call_changeObedience_51
                        scene black with dissolve
                        bot"Shit! She got up... She must have felt it."
                        bo"Uhh... [hin_rel]...?"
                scene bg lr_day with dissolve:
                    zoom 0.68
                show boruto sad at left
                show shina concerned at right:
                    xzoom -1
                with dissolve
                hin"H-how are you feeling? You've been out cold for a few minutes..."
                bo"I am okay [hin_rel]... Are they gone? What happened with those men?"
                show shina angry3:
                        easein 0.3 xpos 0.75
                show boruto surprised
                hin"YOU FREAKING IDIOT!" with vpunch
                
                show shina shy2 with dissolve
                show boruto worried2 with dissolve
                hin"What were you thinking! Putting youself in danger like that..."
                show shina concerned with dissolve
                hin"You almost had me worried to death!"
                menu:
                    hin"You almost had me worried to death!"
                    "I am sorry...":
                        show boruto sad2 with dissolve
                        bo"I am sor-"
                    "It wasn't a big deal...":
                        show boruto embarassed with dissolve
                        bo"It wasn't-"
                show shina angry2 with dissolve
                show boruto surprised2
                hin"Don't apologize yet you idiot!" with vpunch
                show shina assertive with dissolve
                hin"You have some explaining to do..."
                show boruto worried2 with dissolve
                bo"I know [hin_rel], I shouldn't have intervened..."
                if hinatagropedmoneyprobsstart == True:
                    show boruto surprised2 with dissolve
                    hin"It's not about that, you jerk! Did you think I would forget how you... s-startled me!?"
                    hin"Why would you do that [bo_name]! I told you already... you can't be touching me like that"
                    menu:
                        hin"Why would you do that [bo_name]! I told you already... you can't be touching me like that"
                        "I though it would be funny!":
                            show boruto embarassed with dissolve
                            bo"I thought it would be funny to surprise you!"
                            call changeRespect("Hinata", -1, "none") from _call_changeRespect_85
                            show shina angry2
                            show boruto surprised2 with dissolve
                            hin"F-funny!?" with vpunch
                            show shina angry3 at shake
                            hin"I am your [hin_rel] you idiot! That's not funny, it's stupid and wrong! I won't tolerate any more of it..."
                            if hinatagropedmoneyprobs == True:
                                hin"And even if you thought that, how do you explain what you did next..."
                                hin"How did you ever think pretending to be my husband and putting your hands on me like t-that was a good idea?"
                                menu handpushedmenu:
                                    hin"How did you ever think pretending to be my husband and putting your hands on me like t-that was a good idea?"
                                    "I was only trying to help...":
                                        bo"I was only trying to help [hin_rel]..."
                                        if handpushed == True:
                                            call changeLove("Hinata", -1, "none") from _call_changeLove_25
                                            hin"H-help!? You took advantage of the situation [bo_name]!"
                                            hin"Never try anything like that again!"
                                        elif moneyprobshardgroped == True:
                                            show shina angry with dissolve
                                            call changeRespect("Hinata", -1, "none") from _call_changeRespect_86
                                            hin"You were not [bo_name]!"
                                            call changeLove("Hinata", -1, "none") from _call_changeLove_26
                                            show shina angry2
                                            hin"You took advantage of the situation... and me!" with vpunch
                                        else:
                                            call changeObedience("Hinata", 1, "none") from _call_changeObedience_52
                                            show shina concerned with dissolve
                                            hin"That you were... I s-suppose. But still!"
                                            hin"You took it too far [bo_name]! Don't try anything like that again, please..."
                                    "I had to make it believable...":
                                        show boruto suspicious with dissolve
                                        bo"Even though my plan failed, I had to make it seem believable [hin_rel]..."
                                        if handpushed == True:
                                            call changeLove("Hinata", -1, "none") from _call_changeLove_27
                                            hin"B-believable? It was stupid from the getgo [bo_name]!"
                                            hin"Never try something like that again!"
                                        elif moneyprobshardgroped == True:
                                            show shina angry with dissolve
                                            call changeRespect("Hinata", -1, "none") from _call_changeRespect_87
                                            hin"That's a lie and you know it, [bo_name]!"
                                            call changeLove("Hinata", -1, "none") from _call_changeLove_28
                                            show shina angry2
                                            show boruto sad2 with dissolve
                                            hin"You took advantage of the situation... and me!" with vpunch
                                        else:
                                            call changeObedience("Hinata", 1, "none") from _call_changeObedience_53
                                            show shina concerned with dissolve
                                            show boruto sceeming with dissolve
                                            hin"B-believable? I s-suppose that's one way to think about it. But still!"
                                            hin"You took it too far [bo_name]! Don't try anything like that again, please..."
                                if borutoknockedouthatred == True or borutoknockedoutlove == True:
                                    jump moneyprobfaintend
                                else:
                                    jump moneyprobnofaintend
                            else:
                                if borutoknockedouthatred == True or borutoknockedoutlove == True:
                                    jump moneyprobfaintend
                                else:
                                    jump moneyprobnofaintend
                        "Come up with an excuse...":
                            show boruto surprised with dissolve
                            bo"U-uh... I wanted to let you know I was there. I was still sleepy, must have been accidental."
                            call changeRespect("Hinata", -2, "none") from _call_changeRespect_88
                            show shina angry2
                            hin"I am not buying that [bo_name]! We talked about this, you have to control yourself. I won't tolerate any more of this stupidity."
                            show boruto worried with dissolve
                            if hinatagropedmoneyprobs == True:
                                hin"And even if it was accidental that time, how do you explain what you did next..."
                                hin"How did you ever think pretending to be my husband and putting your hands on me like t-that was a good idea?"
                                jump handpushedmenu
                            else:
                                if borutoknockedouthatred == True or borutoknockedoutlove == True:
                                    jump moneyprobfaintend
                                else:
                                    jump moneyprobnofaintend
                elif hinatagropedmoneyprobs == True:
                    show shina shy with dissolve       
                    hin"Why did you..."
                    hin"How did you ever think pretending to be my husband and putting your hands on me like t-that was a good idea?"
                    jump handpushedmenu

            else:
                label moneyprobfaintend:
                    show boruto worried with dissolve
                    bo"I know [hin_rel] I acted somewhat irrationally because of my condition..."
                    bo"I shouldn't have done that, I am sorry..."
                    show shina shy2 with dissolve
                    if secretscenelovehandjob == True:
                        hint"Did I accidentally gave him the wrong idea with what I d-did yesterday...?"
                    hin"*Sigh*"
                    show boruto worried2 with dissolve
                    bo"But more importantly, did those men leave you alone?"
                    hin"They did, but..."
                    show shina shy with dissolve
                    hin"They also said that they'll be back next week and that if I don't pay what we owe there might be consequences..."
                    jump afterfaintmoneyprob

            
    
        else:
            label moneyprobendingconv:
                scene black with dissolve
                show bg lr_day with dissolve:
                    zoom 0.68
                show boruto sad at left with dissolve
                show shina shy at right with dissolve:
                    xzoom -1
                hin"You have some explaining to do..."
                bo"I know [hin_rel], I shouldn't have intervened..."
                if hinatagropedmoneyprobsstart == True:
                    show shina angry with dissolve
                    hin"It's not about that! Did you think I would forget how you... s-startled me!?"
                    hin"Why would you do that [bo_name]! I told you you can't be touching me like that"
                    menu:
                        hin"Why would you do that [bo_name]! I told you you can't be touching me like that"
                        "I though it would be funny!":
                            show boruto smirk with dissolve
                            bo"I thought it would be funny to surprise you!"
                            call changeRespect("Hinata", -1, "none") from _call_changeRespect_89
                            show shina angry2
                            show boruto worried
                            hin"F-funny!?" with vpunch
                            show shina angry3 at shake
                            hin"I am your [hin_rel] you idiot! That's not funny, it's stupid and wrong! I won't tolerate any more of it..."
                            if hinatagropedmoneyprobs == True:
                                hin"And even if you thought that, how do you explain what you did next..."
                                hin"How did you ever think pretending to be my husband and putting your hands on me was a good idea?"
                                jump handpushedmenu
                               
                            else:
                                show boruto worried with dissolve
                                bo"I know [hin_rel]. I acted somewhat irrationally because of my condition..."
                                bo"I shouldn't have done that."
                        "Come up with an excuse...":
                            show boruto surprised with dissolve
                            bo"U-uh... I wanted to let you know I was there. I was still sleepy, must have been accidental."
                            call changeRespect("Hinata", -2, "none") from _call_changeRespect_90
                            show shina angry2
                            hin"I am not buying that [bo_name]! We talked about this, you have to control yourself. I won't tolerate any more of this stupidity."
                            if hinatagropedmoneyprobs == True:
                                hin"And even if it was accidental that time, how do you explain what you did next..."
                                hin"How did you ever think pretending to be my husband and putting your hands on me was a good idea?"
                                jump handpushedmenu
                            else:
                                show boruto worried with dissolve
                                bo"I know [hin_rel]. I acted somewhat irrationally because of my condition..."
                                bo"I shouldn't have done that."
                elif hinatagropedmoneyprobs == True:       
                    hin"Why did you..."
                    hin"How did you ever think pretending to be my husband and putting your hands on me like t-that was a good idea?"
                    jump handpushedmenu
                label moneyprobnofaintend:
                    if moneyprobshardgroped == True:
                        show boruto worried with dissolve
                        bo"You are right, [hin_rel]. I acted somewhat irrationally because of my condition..."
                        bo"I shouldn't have done that, I am sorry..."
                        if secretscenelovehandjob == True:
                            hint"Did I accidentally gave him the wrong idea with what I d-did yesterday...?"
                    jump afterfaintmoneyprob
            
    label afterfaintmoneyprob:

        scene black with dissolve
        show bg lr_day with dissolve:
            zoom 0.68
        show boruto sad at left with dissolve
        show shina shy2 at right with dissolve:
            xzoom -1
        hin"Darn it!"
        hin"[bo_name]..." 
        show shina concerned with dissolve
        hin"You weren't supposed to hear about any of this! I didn't want you to know..."
        menu:
            hin"You weren't supposed to hear about any of this! I didn't want you to know..."
            "{color=[lovecolor]}But I want to help!{/color}":
                default ib_wanttohelp = False
                $ ib_wanttohelp = True
                show boruto worried with dissolve
                bo"But I could help you [hin_rel]. I want to help!"
                show boruto smirk with dissolve
                bo"You know, I have been thinking I could put school on hold for a while, pick up a job or something."
                show shina shy2 with dissolve
                hin"[bo_name]... you can't do that..."
                show boruto suspicious with dissolve
                bo"I am afraid you have no say on this [hin_rel]. It is my decision."
                show boruto normal with dissolve
                bo"Besides, I'd hate seeing you stressed out when I could be helping in any way I can."
                call changeLove("Hinata", 1 ,"none") from _call_changeLove_29
                show shina shy with dissolve
                hin"[bo_name]..."
            "{color=[hatredcolor]}(Maybe I can use this...){/color}":
                show boruto suspicious with dissolve
                bot"[hin_rel] is desperate..."
                show boruto sceeming with dissolve
                bot"If she keeps running into financial trouble, I could maybe coerce her into doing things she would otherwise not..."
                show boruto worried with dissolve
                bo"It sounds like we are in trouble [hin_rel]..."
                bo"Will we be okay?"
                show shina shy2 with dissolve
                hin"Y-yes, I will find a way to get us through this."
        show boruto suspicious with dissolve
        bo"I am sure you noticed too... but those people look nothing like locals."
        bo"Are you sure this isn't just some elaborate ploy?"
        show shina normal with dissolve
        hin"I have thought about that too... Their attire and skin-color is very resemblant of Kumogakure. A village within the land of lightning."
        show ninjawar3 with dissolve:
            zoom 0.5
        hin"Our nation used to be at odds with them during the last Ninja War, but we are supposed to be at peace for now. Although tensions are still definitely running high..."
        show warhinaintro4 with dissolve:
            zoom 0.5
        hin"I even had an encounter with them a few years ago..."
        bo"Did you beat their asses?"
        hin"Naturally... but those were simple Genin shinobi."
        hide ninjawar3
        hide warhinaintro4 with dissolve
        hin"These two from earlier looked much stronger than Genin-ranked shinobi..."
        show boruto normal with dissolve
        bo"That makes them even more suspicious... Have you looked into them at all?"
        show shina serious with dissolve
        $ config.menu_include_disabled = True
        hin"Y-yes... I was skeptical too, but when I talked with our stand-in chief, he surprisingly said they had approval from the daimyō's himself..."
        hin"Seeing how the daimyō is the highest form of authority, I don't see how this would be a farce..."
        menu:
            hin"Seeing how the daimyō is the highest form of authority, I don't see how this would be a farce..."
            "Still, Something feels off [hin_rel]...":
                show boruto suspicious with dissolve
                bo"Still, something feels off [hin_rel]..."
                bo"The way they acted was strange."
                show shina worried with dissolve
                hin"I know [bo_name], but we can't do anything about it right now so please, don't try anything stupid, okay?"
                show boruto worried2 with dissolve
                bo"I am just worried about you [hin_rel]. They also mentioned consequences if we don't find the money, did they not?"
            "{color=[hatredcolor]}Well, shoot... You better find the money then{/color}" if ib_wanttohelp == False:
                show boruto sceeming with dissolve
                bo"Well, shoot... You better find the money then."
                show shina shy2 with dissolve
                hin"Y-yes... I'll see what I can do."
                call changeHatred(2,"none") from _call_changeHatred_48
                call borutoevil2 from _call_borutoevil2_3
                bot"Or don't... It'll be much easier for me to manipulate you that way!"
                show boruto suspicious with dissolve
                bo"Who knows what they meant when they said that there will be consequences..."
        show shina concerned with dissolve
        hin"We shouldn't be thinking about that... besides, what's the worst they could do, increase the debt?"
        show shina shy2 with dissolve
        hin"[na_name] will handle that as soon as he returns..."

        hin"And [bo_name]..."
        show shina assertive with dissolve
        hin"I don't want [him_name] worrying about this and getting distracted from her studies..."
        hin"So please, she hears nothing about it, got it?"
        menu:
            hin"So please, she hears nothing about it, got it?"
            "Of course...":
                bo"Of course..."
            "{color=[hatredcolor]}Hmm... I am getting ideas!{/color}":
                call changeHatred(2, "none") from _call_changeHatred_49
                call borutoevil2 from _call_borutoevil2_4
                bot"I can probably use this against [him_name]!"
                bot"Maybe I could guilt trip her into doing things to 'help' [hin_rel]'s finances."
                show boruto suspicious with dissolve
                bo"Uuuuh, yeah, you got it!"
        hin"Good."
        show shina angry with dissolve
        hin"Speaking of studies... you should have been at school too!"
        show boruto embarassed with dissolve
        bo"Uh.. hehe!"
        show shina shy with dissolve
        hin"Considering the circumstances, I will cut you some slack this time."
        show shina shy2 with dissolve
        hin"I need to take a shower, let's talk about this another time..."
        $ config.menu_include_disabled = False
        jump freeroamstart

label freeroamstart:
    $ renpy.end_replay()
    $ hin_location = "bathroom"
    $ showmapaftertutorial = True
    default journalintro = False
    jump livingroom


label narutointermission:
    $ playmusic("audio/ost/eot.opus",0.6)
    "Meanwhile, in a far away place..."
    show desertintro1 with dissolve
    "Two figures stood motionless, encircled by what must have been close to a hundred battle-ready shinobi."
    "Surrounding them were vast, endlessly spanning deserts that stretched in all directions from what seemed to be the outskirts of a village hidden amidst the sand."
    show desertintro1:
        easein 20 subpixel True zoom 2 xalign 0.5 yalign 1.0
    "A deep, distant voice would echo through the barren landscape..."
    "Dinstant shadowy figure" "You are hereby accused of the following treasonous acts against the Lightning Nation:"
    "Dinstant shadowy figure" "-Interception and falsification of diplomatic correspondence between the Lightning Nation and the rest of the world."
    "Dinstant shadowy figure" "-Infiltration and disruption of the Daimyo's affairs through the use of forbidden shadow clone jutsu."
    "Dinstant shadowy figure" "-Maintaining a secret intelligence ANBU squad within our territory in an attempt to exploit our vulnerabilities."
    "Dinstant shadowy figure" "-Attempting to incite civil unrest through the use of disguised infiltrators among our civilian population."
    show raikageintro1 with dissolve:
        zoom 1.2 xalign 0.5 yalign 1.0
    show raikageintro1:
        easein 3 subpixel True xalign 0.5 yalign 0.0
    "Raikage" "With that... the Raikage sentences the accused to imprisonment until all disputes are resolved."
    "Raikage" "In the instance that the accusations are found to be true, the accused shall be..."
    show raikageintro1 with dissolve:
        zoom 1.5 xalign 0.5 yalign 0.0
    "Raikage" "Executed!" with vpunch
    show raikageintro1 with dissolve:
        zoom 1.0 xalign 0.5 yalign 0.5
    "Raikage" "The accused is asked to stand down, drop his weapons and surrender to Kumogakure's personnel!"

    scene black with dissolve
    "The Accused" "After everything I've done for your nation..."
    $ renpy.sound.play("/audio/soun_fx/drawweapon.opus", channel="sfx2", loop=False, relative_volume = 0.7)
    "The Accused" "To accuse me with your bogus allegations is a low that I did not expect even from you, Raikage!"
    show nintroflash with flash
    $ renpy.sound.play("/audio/soun_fx/dropweapon.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    "The Accused" "You can have my weapons..."
    show nintro0 with dissolve:
        zoom 1.3 xalign 0.5 yalign 0.0
    "The Accused" "I don't suppose I'll need them."
    show nintro0 with dissolve:
        zoom 1.4 xalign 0.5 yalign 0.0
    "The Accused" "You know..."
    "The Accused" "The scorching sun in Kumogakure can really mess with your critical thinking, can it not?"

    show nintro1 with dissolve
    $ renpy.sound.play("/audio/soun_fx/jacketdrop2.opus", channel="sfx2", loop=False, relative_volume = 1.5)
    "The Accused" "We best make sure we stay cool..."
    show nintro1 with dissolve:
        zoom 1.1 xalign 0.5 yalign 0.0
    "The Accused" "Although, something's telling me you lot are way past that point!"
    show raikageintro1 with dissolve:
        zoom 1.2 xalign 0.5 yalign 1.0
    show raikageintro1:
        easein 3 subpixel True xalign 0.5 yalign 0.0
    "Raikage" "Add another transgression to the accusee's list..."
    "Raikage" "That of resisting lawful arrest!"
    show raikageintro1_1 with dissolve:
        zoom 1.5 xalign 0.5 yalign 0.0
    "Raikage" "CAPTURE HIM!" with vpunch
    scene nintro1 with dissolve
    stop music fadeout 8
    $ renpy.sound.play("/audio/soun_fx/howlingwind.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    "The Accused" "Then again, I've been looking for an excuse to get some rust off my rugged bones..."
    
    show nintro1 with dissolve:
        zoom 1.2 xalign 1.0 yalign 1.0
    window hide
    pause 1
    "The Accused" "My hand ain't what it used to be..."
    show nintro2 with dissolve
    "The Accused" "And my body may be slowly withering..."
    show nintro2 with dissolve:
        zoom 1.1 xalign 0.4 yalign 0.0
    show nintro2:
        easein 4 subpixel True zoom 1.3 xalign 0.4 yalign 0.0
    "The Accused" "But make no mistake..."
    $ renpy.music.play("/audio/ost/kokuten.opus", channel="music", loop=False, relative_volume = 0.8)
    pause 0.3
    scene nintro2_1 with Dissolve(0.2):
        zoom 1.5 xpos -270 yalign 0.0
    na"This old man can still put up fight!" with vpunch
    $ renpy.sound.play("/audio/soun_fx/wind3.opus", channel="sfx1", loop=False, relative_volume = 0.7)
    scene nintro1 with flash
    $ renpy.sound.play("/audio/soun_fx/jacketdrop1.opus", channel="sfx3", loop=False, relative_volume = 1.5)
    show narutointro1 at brightrevealzoom, halfzoom
    with flash
    na"...Bring it then! I'll show you why the Hokage is revered as the strongest among all Kage!"
    na"To even consider that I'd bend to your machinations shows how foolish you are, Raikage!"
    scene narutointro1 with dissolve:
        zoom 0.7 xalign 0.4 yalign 0.2
    pause 0.2
    $ renpy.sound.play("/audio/soun_fx/jacketdrop3.opus", channel="sfx3", loop=False, relative_volume = 1.5)
    show narutointro2 with flash
    $ renpy.sound.play("/audio/soun_fx/wind1.opus", channel="sfx1", loop=False, relative_volume = 0.7)
    show narutointro2:
        easein 2 zoom 0.7 xalign 0.4 yalign 0.0
    na"Get this through your thick fucking skulls..."
    scene narutointro2 at halfzoom with dissolve
    na"Ideals aren't struck down when their conveyors are, neither when they are killed!"
    show narutointro2_1 with flash:
        zoom 0.65 xalign 0.4 yalign 0.0
    $ renpy.sound.play("/audio/soun_fx/eyejougan.opus", channel="sfx3", loop=False, relative_volume = 0.5)
    na"Quite the opposite! Killing me will only serve to embolden those that believe in what you so vehemently want to see destroyed!"
    show narutointro2_2 with dissolve:
        zoom 0.7 xalign 0.4 yalign 0.0
    show narutointro2_2:
        easein 10 subpixel True zoom 1 xalign 0.4 yalign 0.0
    na"Concordance shall be ever-enduring! With, or without me..."
    na"The world will continue its march towards a better tomorrow. With..."
    na"Or without me!" with vpunch
    na"COME NOW! Witness the power of my conviction." with vpunch
    na"Allow me to instruct you on what it means to fight for something you truly believe in!"
    show narutointro2_2:
        easein 3 alpha 0.0
    $ renpy.sound.play("/audio/soun_fx/armycharge.opus", channel="sfx3", loop=False, relative_volume = 1)
    with Shake((0, 0, 0, 0), 2, dist=20, peak_time=2.5, smoothness=50)
    scene black with flash
    stop music fadeout 4
    stop sfx2 fadeout 3
    "..."
    $ playmusic("audio/ost/house2.opus",0.6)
    "Back in Konoha..."
    return
    



label kushinadream:
    $ initialize_replay_defaults()
    $ renpy.sound.play("/audio/ost/sleep.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    scene black with fade

    pause(1)
    "You fall into a deep slumber..."
    show dreamvignette zorder 100 with dissolve
    "A... not so lucid dream captivates your senses..."
    play music"/audio/ost/dreaming.opus" volume 0.5
    $ renpy.sound.play("/audio/soun_fx/wind3.opus", channel="sfx3", loop=False, relative_volume = 0.8)
    show dreamkushina0 at brightreveal
    with flash
    ku"Hey, focus up!"
    ku"Come on... I don't have much time!"
    ku"I said..."
    $ renpy.sound.play("/audio/soun_fx/growl1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
    scene dreamkushina1
    show kurama1
    show kurama1:
        easein 2 alpha 0.0
    with flash
    ku"FOCUS UP!" with vpunch
    ku"I have something important to tell you..."
    menu:
        ku"I have something important to tell you..."
        "Stare...":
            scene dreamkushina2 with flash
            ku"D-damn you!"
            ku"Always so un-cooperative..."
            ku"G-get up or I swear on my life..."
        "Focus on her...":
            scene dreamkushina0 with dissolve
            ku"Good..."
    scene dreamkushina0:
        zoom 1.2 xalign 0.5 yalign 0.0
    show dreamvignette zorder 100
    with dissolve
    ku"Now!" with vpunch
    show dreamkushina3 with flash
    show dreamkushina3:
        easein 3 yalign 0.2
    ku"I know you are t-there!"
    ku"I can sense your overflowing chakra..."
    ku"I know you can listen to me!"
    show dreamkushina3 with dissolve:
        zoom 1.1
    ku"Yes, YOU!" with vpunch
    show dreamkushina3 with dissolve:
        zoom 1.0
    ku"Behind the... t-thing!"
    call showscrollingimage from _call_showscrollingimage_305
    show screen parallax1280("dreamkushina3") with dissolve
    "You can move your cursor or drag the screen up and down."
    ku"There's a bond that binds us Jinchūriki you know... even in the afterlife."
    ku"I've been watching how you treat my grandson... The things you made him do..."
    ku"First me, then my son and now my grandson..."
    call hidescrollingimage from _call_hidescrollingimage_249
    ku"HAVE YOU NO SHAME?" with vpunch
    
    show kuramaprison at dizzy
    with flash
    $ renpy.sound.play("/audio/soun_fx/growl2.opus", channel="sfx3", loop=False, relative_volume = 0.9)
    beast"DAMN YOU WOMAN!" with vpunch
    beast"You dare speak to me of shame!?" with vpunch
    beast"You dare point your finger at me when YOUR people have kept me SHACKLED in perpetuity?!"
    beast"When YOUR shitty species have tormented me for millennia..." with vpunch
    beast"And still... I sit here imprisoned."
    beast"STILL... I bide my time until the day I return only that which you have shown me..." with vpunch
    show kuramaprison:
        linear 5 alpha 0.0
    $ renpy.sound.play("/audio/soun_fx/growl3.opus", channel="sfx3", loop=False, relative_volume = 0.7)
    beast"Treacherous, PUNY humans! You shall know unending pain and suffering at my hand!" with vpunch
    beast"Just as I did at yours..."

    ku"I won't have you tormenting my grandson!"
    show dreamkushina_end0 with dissolve:
        yalign 1.0
    show dreamkushina_end0:
        easeout 4 yalign 0.0
    ku"Not like you tormented me..."
    ku"You hear me!?" with vpunch
    show screen parallax1280("dreamkushina_end0")
    "You can move your cursor or drag the screen up and down."
    "Click twice to continue"
    $ ui.interact()
    hide screen parallax1280
    show dreamkushina_end2:
        yalign 0.0
    with flash
    ku"I am keeping an eye on you, Kyuubi..."
    ku"You even dare thinking about trying anything funny and I swear..."
    scene dreamkushina_end2 with dissolve:
        yalign 1.0
    show dreamvignette zorder 100 with dissolve
    show dreamkushina_end2:
        easeout 4 yalign 0.0
    ku"You'll be dealing with me!"
    ku"You hear that?" with vpunch
    show screen parallax1280("dreamkushina_end2")
    "You can move your cursor or drag the screen up and down."
    menu:
        ku"You'll be dealing with me, You hear that?!"
        "{color=[hatredcolor]}????{/color}":
            hide screen parallax1280
            $ renpy.sound.play("/audio/soun_fx/eye4s.opus", channel="sfx3", loop=False, relative_volume = 0.3)    
            show kurama1 with flash
            show kurama1:
                easein 2 alpha 0.0
            scene dreamkushina_end2 with dissolve:
                yalign 0.5
            beast"...You impudent WHORE!" with vpunch
            beast"If only I wasn't sealed, I would ravage you myself!"
            show dreamkushina_end2:
                easein 2 yalign 1.0
            beast"No matter! Your womb already served its purpose..."
            beast"And so shall those that come after yours!" with vpunch
            beast"You filthy, red-haired human bitch!" with vpunch

            call changeHatred(1) from _call_changeHatred_50
            beast"I'll just have to settle with the bastard kid of yours for now..."
            
        "...":
            hide screen parallax1280
            $ renpy.sound.play("/audio/soun_fx/eye4s.opus", channel="sfx3", loop=False, relative_volume = 0.3)    
            show kurama2 with flash
            show kurama2:
                easein 2 alpha 0.0
            show dreamkushina_end2:
                easein 2 yalign 1.0
            beast"Puny woman..."
            beast"You have no idea what awaits you and your family..."

    $ renpy.sound.play("/audio/soun_fx/wind1.opus", channel="sfx3", loop=False, relative_volume = 0.8)
    scene dreamkushina_end3 with flash:
        yalign 0.0
    show dreamkushina_end3:
        easein 2 xalign 0.5 yalign 0.7
    $ renpy.sound.play("/audio/soun_fx/growl1.opus", channel="sfx2", loop=False, relative_volume = 0.6) 
    beast "All in due time..."
    beast"*Growls*"
    scene beach bg at brightrevealzoom
    with flash
    show dreamkushina00 with dissolve:
        alpha 1.0
    show dreamkushina00:
        easein 8 alpha 0.0
    ku"And [bo_name]... When you feel like everything's lost, Look for me deep within your subconsciousness."
    ku"I'll be there to serve as your guiding light..."
    bot"zZz..."
    "Girl" "Mom... Can we leave now?"
    "Mature Lady" "Leave? But we just got here, Sarada..."
    show sarada 2 at right with dissolve
    sara"Ugh... You know I hate the sun, not to mention the sand that keeps getting in between my toes!"
    show sakura 1 at left with dissolve:
        ypos 1.03
    saku"Come on, Sarada! Have a little bit of fun for once..."
    saku"Besides, your poor fair skin is never going to get a tan if you don't take that jacket off every one in a while..."
    saku"We are at the beach for goodness' sake!"
    show sakura at smallshake
    saku"Who wears a jacket at the beach? *Giggles*"
    show sarada 1 at right with dissolve
    sara"*Sigh...*"
    sara"I knew I shouldn't have come with you..."
    saku"Here's the deal! I'll go first..."
    show sakura 2 at left with dissolve
    saku"And you'll follow!"
    saku"My pants have gotten wet anyway and I've been looking to tan up!"
    show sakura 2:
        easein 1 xpos -600
    saku"Come on! It'll be fun!"
    show sarada 2 at right with dissolve
    show sarada at smallshake
    sara"H-hey, wait!"
    show sarada at smallshake
    sara"I haven't agreed to that!"
    show dreamsakura with dissolve:
        yalign 1.0 xalign 0.5 zoom 0.8
    show dreamsakura:
        easein 4 yalign 0.1
    saku"Too late now! A deal's a deal..."
    show dreamsakura with dissolve:
        yalign 0.2 xalign 0.5 zoom 0.67
    saku"You know... boys like a nice looking tan on us girls!"
    show screen parallax1280("dreamsakura", 0.67) with dissolve
    "You can move your cursor or drag the screen up and down."
    sara"Another reason to avoid the sun then!" with vpunch
    sara"Hmph!"
    saku"Like father like daughter I suppose... *Giggles*"
    saku"Well, you can sit there and sulk while your mother enjoys some much needed sun!"
    saku"Or you can come and join the fun! The choice is yours..."
    "Click twice to continue"
    $ ui.interact()
    hide screen parallax1280
    scene beach bg
    show sarada 1 at center
    with dissolve
    sara"Darn it..."
    show sarada 2 with dissolve
    sara"Tannings, suns and boys..."
    sara"All things that you know I hate, mom..."
    show sarada at smallshake
    sara"There's more important things to me than snotty boys..."
    sara"I have to get stronger... There's no time for me to waste!"
    saku"There'll be ample time for that later Sarada."
    saku"Besides, we are at peace now! The Shinobi world is not what it used to be, [na_name] made sure of that!"
    saku"Come now! Join me for just a few minutes and then we'll get going, deal?"
    show sarada 1 with dissolve
    sara"Ughh! *Sulks*"
    show sarada 2 with dissolve
    show sarada:
        easein 2 xpos -500
    sara"Fiiineee.... *Scoffs*"
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/clothes_undress.opus", channel="sfx3", loop=False, relative_volume = 1)
    sara"But I'll be lying under the umbrella!"
    show dreamsarada1 with dissolve:
        yalign 1.0 zoom 0.5
    show dreamsarada1:
        easein 5 yalign 0.0
    sara"I can't have the sun ruining my skin..."
    saku"You really are the spitting image of your father... Both in character and in appearance!"
    show dreamsakura with dissolve:
        yalign 0.2 xalign 0.5 zoom 0.67
    saku"Have you even inherited a single trait of mine?"
    sara"Definitely not your c-chest, I'll tell you that much."
    show dreamsakura with dissolve:
        yalign 0.35 xalign 0.5 zoom 0.67
    sara"And by the way... your n-nipples are poking through your swimsuit..."
    show screen sakuraparallax
    show screen sakuraparallaxbutton
    with dissolve
    saku"Must be the cold breeze... Besides, it's just me and you around!"
    saku"{size=15}Or maybe I am missing that stupid father of yours a little bit too much...{/size}"
    hide screen sakuraparallaxbutton
    hide screen sakuraparallax
    show screen saradaparallax
    show screen saradaparallaxbutton
    with dissolve
    saku"Do I sense some intricate insecurity of yours surfacing, Sarada?"
    saku"There's nothing wrong with small boobs, you know!"
    sara"M-mom!" with vpunch
    saku"I am serious, Sarada! There's more to us women than our chests you know..."
    saku"You carry much more beauty than you know. Both, inside of you and outside..."
    scene black with vpunch
    hide screen sakuraparallaxbutton
    hide screen sakuraparallax
    hide screen saradaparallaxbutton
    hide screen saradaparallax
    $ renpy.sound.play("/audio/soun_fx/clothes_undress.opus", channel="sfx3", loop=False, relative_volume = 1)
    sara"O-ok, that's enough! I am putting my clothes back on..." with vpunch
    $ renpy.sound.play("/audio/soun_fx/eyesharingan2.opus", channel="sfx3", loop=False, relative_volume = 0.2)
    scene dreamsarada2 with flash:
        zoom 1.2 xalign 0.5 yalign 0.0
    show dreamsarada2:
        easein 3 zoom 1.0 xalign 0.5 yalign 1.0
    
    sara"This quickly got awkward..."
    scene dreamsarada2 with dissolve:
        zoom 1.1 xalign 0.5 yalign 0.0
    sara"I knew I shouldn't have come here after all..."
    show screen parallax1280("dreamsarada2") with dissolve
    saku"*Giggles* Oh to be young and free again..."
    saku"How I wish to have sand in between my toes and my small boobs to be my biggest concerns!"
    sara"M-mom, stop it!" with vpunch
    saku"Sooner than you realize, you'll come to grow into a strong and beautiful woman Sarada..."
    saku"You'll have important responsibilities and people looking up to you... Not simply because of your beauty, but because of your strength too, just like your mom here! *Giggles*"
    saku"And when you do, you'll realize that these were the moments worth cherishing all along!"
    sara"*Scoffs*... C-can we go now?"
    dev"You've just seen two (Or three!?) possible character additions to HoS!"
    dev"If you'd like to see specific characters make their appearances in future updates, make sure to join {a=https://discord.gg/MVKJPEWtNy}Discord{/a} and voice your preference!"
    dev"Even better, consider supporting HoS over at {a=https://subscribestar.adult/cutepercentage}SubscribeStar{/a} which will grant you early access to future updates, as well as voting power that can determine the future of HoS!"
    $ renpy.end_replay()
    "An important message follows regarding the future of HoS!"
    hide screen parallax1280 with dissolve
    show endscreen1 with dissolve
    show endscreen10 with dissolve
    call clicktwice from _call_clicktwice 
    $ renpy.sound.play("/audio/soun_fx/eyejougan.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    show endscreen11 at endcreen_text
    with dissolve
    $ renpy.pause(1, hard=True)
    call clicktwice from _call_clicktwice_1
    scene endscreen1 with dissolve
    show endscreen2 with dissolve
    show endscreen3 at endcreen_text
    call clicktwice from _call_clicktwice_2
    show endscreen4 at endcreen_text
    show endscreen5 at endcreen_text
    show endscreen6 at endcreen_text

    $ renpy.sound.play("/audio/soun_fx/wind2.opus", channel="sfx1", loop=False, relative_volume = 0.8)
    show endscreen7 at endcreen_text
    show endscreen8 at endcreen_text
    $ renpy.pause(0.7, hard=True)
    call clicktwice from _call_clicktwice_3
    $ renpy.sound.play("/audio/soun_fx/wind3.opus", channel="sfx3", loop=False, relative_volume = 0.8)
    scene endscreen1
    with dissolve
    show endscreen9 at endcreen_text
    $ renpy.pause(1, hard=True)
    call clicktwice from _call_clicktwice_4
    scene black with dissolve
    dev"CutePercentage here with a friendly reminder to follow my {a=https://subscribestar.adult/cutepercentage}SubscribeStar (There's a free tier!){/a} or join my {a=https://discord.gg/MVKJPEWtNy}Discord{/a} where I'll be lurking daily and posting updates!{p}You can do so by clicking the blue words above!"

    dev"If you had fun, drop a positive review on  {a=https://cutepercentage.itch.io/house-of-shinobi}Itch.io{/a} or that other website. It really helps!"
    $ renpy.sound.play("/audio/soun_fx/wakeup.opus", channel="sfx2", loop=False, relative_volume = 1.6)
    $ renpy.sound.play("/audio/soun_fx/wind3.opus", channel="sfx1", loop=False, relative_volume = 0.8)
    $ renpy.sound.play("/audio/soun_fx/growl3.opus", channel="sfx3", loop=False, relative_volume = 0.8)
    stop music fadeout 2
    pause 0.1
    show black with dissolve
    $ playmusic("/audio/ost/house2.opus", 0.5)
    show kuramaprison:
        alpha 0.0 zoom 1.2 xalign 0.5 yalign 0.5
    show  kuramaprison:
        easein 1.5 alpha 1.0
    with Shake((0, 0, 0, 0), 1.5, dist=40, peak_time=0.9, smoothness=50)
    scene black with longerflash
    bot"F-feels like I have dreamt of something important..."
    bot"But I can't recall anything..."
    bot"Oh well, back to sleep..."
    return

    



    
default ch1_d7_hatredpath = False #Toggled if (wait to see what happens || dont help 2nd payment)
default ch1_dy_200paid = False #Toggled if you offer to cover the payment
default ch1_dy_love_nopay = False #Toggled if dominant but fail to pay
label ch1_d7_moneyproblems_mainstory:
    show eyeclosed
    show hinaq1bg 2 behind eyeclosed:
        blur 6

    call blink("Ugh...", "What's up with the commotion downstairs...","O-oh shit!") from _call_blink_4
    scene black with dissolve
    bot"Must be those threatening men again..."
    $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    show bg bb day with dissolve
    show boruto surprised2 with dissolve
    bot"I should hurry downstairs and see what's going on!"
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/footsteps.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    scene hina opendoor1 with dissolve
    dm"Damn you woman! What is it that you don't understand!?" with vpunch
    bot"Things are escalating quickly!"
    scene hina opendoor1_1 with dissolve
    bot"But I made it just in time to..."
    show hatred_choice with dissolve
    $ renpy.sound.play("/audio/soun_fx/heartbeatlong.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    "When an important choice is available to you, the screen will flash with a color relating to that option."
    "Such options will often lock you to a specific path that can significantly alter future events."
    menu ch1_d7_moneyproblems_menu1:
        bot"But I made it just in time to..."    
        "Step in":
            hide hatred_choice with dissolve
            bot"I am not about to sit here and let these assholes have their way..."
            if borutoknockedouthatred == True or borutoknockedoutlove == True:
                bot"But I should be careful. I did get knocked out last time when I tried stepping in..."
            menu:
                bot"But I should be careful..."
                "{color=[dominancecolor]}It's ok [hin_rel], I got this!{/color}":
                    call checkDominance(8, "ch1_d7_moneyproblems_menu1") from _call_checkDominance_11
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    show hinagropemoneyproblems with vpunch
                    $ renpy.sound.play("/audio/soun_fx/grope1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                    bo"It's ok [hin_rel], I got this!"
                    show hinagropemoneyproblems:
                        zoom 1.7 xalign 0.5 yalign 0.7
                    call changeDominance(1, "none") from _call_changeDominance_57
                    "You used the opportunity to cop a feel of [hin_name]'s ass..."
                    hin"[bo_name_stutter]!?"
                    scene black with vpunch
                    "[hin_name] quickly pushed your hand away..."
                    scene bg porch with dissolve
                    show demandingmen badguys1 with dissolve
                    if borutoknockedouthatred == True or borutoknockedoutlove == True:
                        dm"Kid, did you not learn your lesson last time?"
                    show demandingmen badguys1:
                        easein 0.6 xpos 0.99
                    show shina surprised3 at left with dissolve:
                        zoom 0.95
                    show boruto sceeming at left behind shina with dissolve:
                        xalign 0.3
                    jump ch1_d7thinkcarefully

                "What's going on, [hin_rel]?":
                    bo"What's going on, [hin_rel]?"
                    scene bg porch with dissolve
                    show demandingmen badguys1 with dissolve:
                        zoom 1.05 ypos -27
                    if borutoknockedouthatred == True or borutoknockedoutlove == True:
                        to"Kid, did you not learn your lesson last time? Don't try anything stupid, lest you want to get knocked-out again..."
                    show demandingmen badguys1:
                        easein 0.6 xpos 0.45
                    show shina surprised3 at left with dissolve:
                        zoom 0.95
                    show boruto sceeming at left behind shina with dissolve:
                        xalign 0.3
                    label ch1_d7thinkcarefully:
                    dm"This is a conversation for grownups. Step aside, twerp!"
                    show shina concerned with dissolve
                    hin"[bo_name]... S-stay calm, okay? They are just here for the money..."
                    bo"Do you have what they are asking for?"
                    hin"I only have enough to cover g-groceries..."
                    show both_choice with dissolve
                    $ renpy.sound.play("/audio/soun_fx/heartbeatlong.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    menu paydebt1:
                        hin"I only have enough to cover g-groceries..."
                        "{color=[dominancecolor]}You heard her, shitheads!{/color}":
                            hide both_choice with dissolve
                            call changeDominance(1) from _call_changeDominance_58
                            $ ch1_dy_love_nopay = True
                            bo"You heard her, shitheads!"
                            bo"Are you really about to extort a woman's grocery money?"
                            dm"I am afraid that's not how any of this works kid!"
                            dm"Unlike you, grown up people have responsibilities... Failing to meet them WILL result in consequences!"
                            show boruto worried with dissolve
                            bot"Motherfuckers..."
                            bo"...What sort of consequences?"
                            dm"You've had your warning, if your [hin_rel_mother] here can't cover her debts..."
                            show demandingmen:
                                linear 0.4 xalign 0.3
                            show boruto:
                                linear 0.3 xalign -2.0
                            with vpunch
                            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp4.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                            show shina surprised4 at smallshake
                            dm"She'll have to pay in other ways!"
                            scene black with vpunch
                            bo"U-ugh!"
                            "The men easily pushed you away and restrained [hin_name]'s hands..."
                            scene bg porch
                            show mp_v1_0introt
                            with dissolve
                            bo"What do you think you are doing you assholes!"
                            dm"Kid... you try anything stupid, not only will you get knocked down, your [hin_rel_mother] here will also pay the price of your mindless actions..."
                            show mp_v1_0introt 1 with dissolve
                            hin"I'll be okay, [bo_name]..."
                            hin"I am the Hokage's wife, am I not?"
                            hin"They can't hurt me even if they tried!"
                            hin"Please let [him_name] know that I'll be handling some chores outside the house if she returns before me..."
                            show mp_v1_0introt with dissolve
                            hin"Okay?"
                            bot"I know when you put on that fake smile [hin_rel]..."
                            bot"You are trying to appear strong... aren't you?"
                            show mp_v1_0introt:
                                easeout 2 xpos 1500 alpha 0.0
                            bo"Wait! You bastards!" with vpunch
                            dm"Trust me when I say, kid..."
                            $ renpy.sound.play("/audio/soun_fx/intro/evilmenlaugh.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                            dm"You don't want to try following us, or else..."
                            bot"Is there nothing I can do...?"
                            scene bg porch with dissolve
                            show boruto angry with dissolve
                            bot"Fuck...!"
                            bot"I didn't expect things to escalate as quickly as they did..."
                            jump ch1_day7_konohaoutskirts
                            

                            


                        "{color=[hatredcolor]}What a shame...{/color}":
                            hide both_choice with dissolve
                            $ ch1_d7_hatredpath = True
                            bot"Once [hin_rel] becomes desperate for money, I am sure she'd be a bit more willing to accommodate me rather than deal with these idiots!"
                            bot"Hehe!"
                            bo"What a shame... Is there anything else we can do?"
                            dm"There's nothing you can do, kid! Your [hin_rel_mother] on the other hand..."
                            show demandingmen:
                                linear 0.4 xalign 0.3
                            show boruto:
                                linear 0.3 xalign -2.0
                            with vpunch
                            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp4.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                            show shina surprised4 at smallshake
                            dm"I am sure we can work something out with her!"
                            scene black with vpunch
                            bo"U-ugh!"
                            "The men easily pushed you away and restrained [hin_name]'s hands..."
                            scene bg porch
                            show mp_v1_0introt
                            with dissolve
                            bo"If she doesn't return home safe you'll be dealing with me, assholes!"
                            dm"The wind is enough to deal with the likes of you, twerp! Don't try anything stupid..."
                            show mp_v1_0introt 1 with dissolve
                            hin"I'll be okay, [bo_name]..."
                            hin"I am the Hokage's wife, am I not?"
                            hin"They can't hurt me even if they tried!"
                            hin"Please let [him_name] know that I'll be handling some chores outside the house if she returns before me..."
                            show mp_v1_0introt with dissolve
                            hin"Okay?"
                            bot"Fuck... Should I really have done this?"
                            bot"Poor [hin_rel_mother]... She's still trying to appear strong."
                            show mp_v1_0introt:
                                easeout 2 xpos 1500 alpha 0.0
                            bot"Well... I've made my choice. What's the worst that can happen?" with vpunch
                            $ renpy.sound.play("/audio/soun_fx/intro/evilmenlaugh.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                            bot"Surely they wouldn't do anything to the Hokage's wife... right?"
                            bot"Who knows, maybe this will work in my favor if [hin_rel] grows dependent on me for money!"
                            jump ch1_day7_konohaoutskirts

                        "{color=[lovecolor]}Don't Worry, [hin_rel]... ({color=#85bb65}-$200{/color})":
                
                            call checkMoney(200, "paydebt1") from _call_checkMoney_1
                            hide both_choice with dissolve
                            $ ch1_dy_200paid = True
                            bo"Hold the fuck up, you assholes!"
                            # call changeMoney(-200)
                            bo"Is this what you want?"
                            call changeLove("Hinata", 1) from _call_changeLove_38
                            hin"[bo_name_stutter]!? H-how did you even come across that much money..."
                            $ quest.check("job2_1", "completed")
                            $ quest.check("job2_2", "in progress")
                            $ notification("Quest updated")
                            dm"That'll settle your previously outstanding amount, but..."
                            dm"We have to inform you that the Daimyo has ordered that the owed amount be doubled in the coming weeks!"
                            show boruto surprised2 with dissolve
                            hin"D-doubled!?" with vpunch
                            bo"What the fuck is the Daimyo thinking... Does he want the village to starve to death?"
                            show shina assertive with dissolve
                            hin"I won't stand for this! Let me talk to the Daimyo himself!"
                            dm"You are in luck, woman!"
                            dm"The Daimyo has arranged for you to attend his manor. 'The Hokage's consort deserves... delicate treatment' were his exact words."
                            hin"Am I to meet with him r-right now?"
                            dm"Indeed you are! We'll serve as your guide to his premises..."
                            bo"[hin_rel], you don't have to go..."
                            show boruto angry with dissolve
                            bo"We've paid your ask, haven't we?"
                            bo"If she must go, then I am coming with you!" with vpunch
                            dm"The Daimyo's orders are absolute, kid! The Hokage's consort, and only her, shall appear before his lordship."
                            dm"There's no need for concern..."
                            dm"We are under strict orders to treat the Hokage's consort with respect, given that she stays vigilant with her obligations of course..."
                            dm"Now, follow us! Lady of the leaf..."
                            show shina:
                                easein 2 xalign 0.6
                            hin"..."
                            scene bg porch
                            show mp_v1_0introt
                            with dissolve
                            bo"[hin_rel]!"
                            show mp_v1_0introt 1 with dissolve
                            hin"I'll be okay, [bo_name]..."
                            hin"I am the Hokage's wife, am I not?"
                            hin"They can't hurt me even if they tried!"
                            hin"Please let [him_name] know that I'll be handling some chores outside the house if she returns before me..."
                            show mp_v1_0introt with dissolve
                            hin"Okay?"
                            show mp_v1_0introt:
                                easeout 2 xpos 1500 alpha 0.0
                            bot"Fuck! I can't risk following them..." with vpunch
                            bot"But I have to figure out what's going on... I can't allow these fuckers to keep extorting us like this!"

                            jump ch1_day7_konohaoutskirts
                            
                        
                    
            
        "{color=[hatredcolor]}Wait and see how this plays out...{/color}":
            $ ch1_d7_hatredpath = True
            hin"I... I don't have the money! What would you have me do?"
            dm"Then you are coming with us!" with vpunch
            scene black with vpunch
            hin"H-hey! Let me go!"
            "You go outside to see what's happening..."
            scene bg porch
            show mp_v1_0introt
            with dissolve
            bot"Fuck... Should I really have done nothing?"
            show mp_v1_0introt:
                easeout 2 xpos 1500 alpha 0.0
            bot"Well, shit! I've made my choice. What's the worst that can happen?" with vpunch
            $ renpy.sound.play("/audio/soun_fx/intro/evilmenlaugh.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            bot"Surely they wouldn't do anything to the Hokage's wife... right?"
            bot"Who knows, maybe this will work in my favor if [hin_rel] grows dependent on me for money!"
            jump ch1_day7_konohaoutskirts


        

    label ch1_day7_konohaoutskirts:
        scene black with dissolve
        $ playmusic("audio/ost/Senya.opus",0.5)
        $ quest.check("job2_1", "done")
        $ quest.check("job2_2", "in progress")
        $ notification("Quest updated")
        label replay_ch1_day7_konohaoutskirts:
        $ initialize_replay_defaults()
        "Meanwhile, somewhere in the outskirts of Konoha..."
        show bg konoha1
        show mp_v1_1
        with dissolve
        to"Stop flailing your arms around woman!"
        hin"Then stop holding on to my arms!"
        scene bg konoha1
        show demandingmen normal badguys2
        show shina restrained:
            zoom 1.01


        with fade
        to"Have you considered not putting yourself in this position in the first place?"
        to"You dumb wh-"
        show demandingmen at smallshake
        ko"Toji!" with vpunch
        scene black with dissolve
        to"Bah! I know, I know Koji... Daimyo's orders and all!"
        to"But that doesn't mean I'll let this damned woman do as she pleases!"
        scene bg konoha1
        show mp_v1_3:
            xpos 0.30
        with dissolve
        hin"H-hey! What's that for!?"
        to"An item of particular usefulness when defiant bitches like you keep resisting!" with vpunch
        show mp_v1_3:
            easeout 0.3 xpos 0.0
        pause 0.3
        show mp_v1_3 at smallshake
        to"Now keep it shut and keep walking!"
        hin"Don't push me around! And get your hands off of me!"
        scene bg konoha1
        show mp_v1_2
        with dissolve
        to"So long as you behave..."
        hin"The Hokage will hear of this, imbeciles!"
        to"Watch your tongue, little lady..."
        to"And keep walking!" with vpunch
        show mp_v1_2:
            easeout 2 xpos -0.2
        to"The Hokage this, the Hokage that..."
        to"I don't see him around much... Do you, Koji?"
        ko"I don't think so Toji..."
        dm"Hahahahaha!"
        scene bg konoha2
        show mp_v1_2:
            xpos 0.30
        with dissolve
        to"Almost there now..."
        hint"...Shoot!"
        hint"Shall I try making a run for it?"
        hint"These two look strong, but their big frames would surely slow them down!"
        hint"I am almost certain I can outrun them with my athletic abilities..."
        to"Oi!" with vpunch
        scene bg konoha2
        show mp_v1_3:
            xpos 0.30
        with dissolve
        to"Keep moving!" with vpunch
        show mp_v1_3:
            easein 0.5 xpos 0.0
        hin"I said don't touch me!" with vpunch
        to"You are not in a position to make demands!"
        to"Hey Koji! I am this close to losing my cool with this bi-"
        ko"Daimyo's orders, Toji! You know how it is..." with vpunch
        to"Yes yes! But, Surely we could..."
        scene bg konoha2
        show mp_v1_spank 1
        with dissolve
        to"Discipline a resisting bitch! Can't we!?" with vpunch
        show mp_v1_spank 0 with Dissolve(0.3)
        # show mp_v1_spank 2 with Dissolve(0.3)
        show mp_v1_spank 3 with Dissolve(0.3)
        $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.5)
        $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
        pause 0.3
        show mp_v1_spank 4 with Dissolve(0.3)
        pause 0.3
        scene bg konoha2
        show bruise1
        with dissolve
        to"I said, keep moving!" with vpunch
        hin"Aarh!" with vpunch
        hin"Y-you bastard! You will pay for this!"
        to"Shut it, woman! You deserved at least this much!" with vpunch
        hin"Lay your hands on me one more time and I-"
        to"You'll do what... you puny bitch!" with vpunch
        ko"Enough, Toji!" with vpunch
        ko"If you go any further, the Daimyo might just cut off your hands himself—if this feisty lady doesn't do it first..."
        to"Oh please..."
        to"This... Lady here is lucky she's under the protection of the Daimyo..."
        to"Or lord knows I'd have my way with her!"
        hin"You try anything f-funny and I'd beat you to a pulp!"
        to"Hah! I'd love to see you trying..." with vpunch
        ko"Enough!" with vpunch
        scene black with dissolve
        ko"We are almost there..."
        scene palace with dissolve
        show bruise1 with dissolve
        ko"Before we enter his lordship's premises, consider this advice for your own well-being, Lady of the leaf..."
        ko"In his palace you, we, and everyone else obey the Daimyo's word. It doesn't matter if you are the Hokage's consort or the Hokage himself..."
        ko"We are all subjects to his highness, and even though he might not look it..."
        ko"His temperament is even shorter than my colleague's over here..."
        scene palace
        show demandingmen normal badguys2
        show shina restrained:
            zoom 1.01
        with fade
        hin"..."
        ko"Now gather your spirits, and do your best to not disappoint!"
        hide demandingmen
        hide shina
        with dissolve
        "[hin_name] stood across what seemed to be a massive acre of land, capable of housing hundreds, if not thousands of people..."
        "High walls and a tall gate, prohibited entry to anyone who would look into breaking in."
        show palace with dissolve:
            zoom 1.2 xalign 0.5 yalign 0.5
        "And even if someone were to sneak inside, they would quickly find themselves facing the Daimyo's elite guard."
        to"OPEN THE GATES!" with vpunch
        "Guard" "Under what occasion?"
        to"The Hokage's consort is here, as requested by the Daimyo himself!"
        scene black with dissolve
        $ renpy.sound.play("/audio/soun_fx/gateopening.opus", channel="sfx3", loop=False, relative_volume = 0.5)
        "The gate was raised up only to reveal..."
        show palace3 with dissolve
        "What seemed like a small village, hidden beneath the tall walls."
        "A golden-coated palace stood atop the end of a long staircase while a rocky pathway seemed to lead towards a hot spring area."
        show demandingmen normal badguys2
        show shina restrained:
            zoom 1.01
        with dissolve
        hint"This place is unnecessarily large! Is this how a Daimyo lives?"
        to"Keep moving!" with vpunch
        hide demandingmen
        hide shina
        with dissolve
        "Through the rocky pathway leading to the hot springs, appeared an elegant figure..."
        scene rangi_intro with dissolve:
            zoom 0.7 xalign 0.5 yalign 1.0
        show rangi_intro:
            easein 5 yalign 0.0
        mada "Hands off the consort, you brutes!"
        dm"Y-yes Madame!" with vpunch
        show rangi_intro with dissolve:
            zoom 0.63 yalign 0.0
        show screen parallax1280("rangi_intro", 0.63) with dissolve
        call showscrollingimage from _call_showscrollingimage_21
        mada "Good little puppies!"
        mada "Now leave us alone! The consort is to be in my care until the Daimyo requests for her presence..."
        call hidescrollingimage from _call_hidescrollingimage_28
        $ renpy.end_replay()
        label replay_rangikuintro:
        $ initialize_replay_defaults()
        scene palace3
        show demandingmen normal badguys1:
            xzoom -1 zoom 1.2 xpos -0.6
        show shina restrained:
            zoom 1.01
        with dissolve
        show rangi angry at right with dissolve:
            zoom 0.58
        mada "Off you go!" with vpunch
        show demandingmen:
            easeout 1 xpos -1.4
        dm"H-hai!" with vpunch
        hide demandingmen with dissolve
        hin"..."
        show rangi normal2 with dissolve
        mada "Excuse their barbaric nature, Lady [hin_name]..."
        mada "It's all those imbeciles know. Sometimes, I wonder what good they are to his highness..."
        hin"W-who are you...? Why do you know m-my name?"
        mada "I am but a concubine to his highness, a trusted one mind you. I am tasked with knowing everything there is to know about the Daimyo's affairs."
        mada "You now happen to be one such affair, my Lady. You can call me Madame. Nothing less, nothing more."
        hin"..."
        mada "I've been instructed to prepare you for an audience with his highness..."
        hin"P-prepare me... how? What's the meaning of all this!"
        show rangi behind shina:
            easein 2 xalign 0.4
        mada "You shan't worry when you are in my care, Lady [hin_name]..."
        mada "Here... Allow me to untie your hands."
        scene palace3
        show hin_rangi
        with dissolve

        mada "These animals... Did they put your hands on you, Lady [hin_name]?"
        hin"The b-big one... H-he hit my..."
        scene black with dissolve
        mada "*Groans*... Don't worry. I'll make sure he pays a hefty price for that!"
        "The seemingly well-intentioned woman untied [hin_name]'s hands..."
        scene palace3
        show rangi normal at right:
            zoom 0.58
        show shina shy:
            xalign 0.4 ypos 0.01
        with dissolve
        hin"T-thank you, Madame..."
        show rangi with dissolve:
            xzoom -1
        mada "Now please follow me, Lady [hin_name]!"
        show rangi:
            easeout 1 xpos 1.5
        show shina shy2 with dissolve
        hin"W-wait! Where are we going!?"
        mada "You'll find out soon enough!"
        hint"What have I gotten myself into..."
        hide shina with dissolve
        show palace3 with dissolve:
            zoom 1.3 xalign 0.5 yalign 0.7
        "[hin_name] walks through the rocky pathway..."
        scene bg onsen1 with dissolve
        "Until she finds herself in an open air onsen enclosed by tall wooden fences, but still observable from the high buildings above, especially the palace..."
        show shina shy2 at left with dissolve
        hint"S-so... beautiful..."
        show rangi normal2 at right with dissolve:
            zoom 0.58
        mada "Girls, prepare the Lady for a bath!" with vpunch
        "Girls" "Right away, Madame!"
        hide rangi with dissolve
        show shina concerned with dissolve
        hin"W-what? Right now!?" with vpunch
        scene black with vpunch
        hin"H-hey!"
        show screen parallax1280("bh undress1") with dissolve
        call showscrollingimage from _call_showscrollingimage_22
        "Two of Madame's servants quickly surrounded [hin_name] and started undressing her..."
        "Red haired girl" "You shan't worry my lady, we are here to help..."
        hin"B-b-ut we are in the open! Am I to undress r-right here!?"
        mada "Girls! Take the Lady to the private quarters!" with vpunch
        call hidescrollingimage from _call_hidescrollingimage_29
        scene black with dissolve
        "Red haired girl" "Here, allow me to..."
        show screen parallax1280("bh undress2") with dissolve
        call showscrollingimage from _call_showscrollingimage_23
        $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
        hin"*Gasp* W-wait..."
        menu :
            hin"*Gasp* W-wait..."
            "I can undress myself!":
                hin"P-please, I can undress myself!"
                "Red haired girl" "Are you sure my Lady? We are only here to help..."
                mada "You heard her, girls! Leave the Lady be!" with vpunch
                "Girls" "Yes Madame!"
                call hidescrollingimage from _call_hidescrollingimage_30
                scene bg onsen1 with dissolve
                show shina concerned at left with dissolve
                show rangi normal at right with dissolve:
                    zoom 0.58
                mada "So overprotective, Lady [hin_name]..."
                mada "But I understand! Our bodies are ours and ours alone!"
                mada "We, and only we shall determine who, and how they come in contact with it..."
                hin"R-right..."
                mada"Well then, are you waiting for something, my Lady?"
                show shina shy with dissolve
                hin"Am I to u-undress r-right here?"
                mada"Why yes! It's just me and you around, you are not afraid of me, are you my Lady?"
                show shina shy2 with dissolve
                hin"Afraid is not the word..."
                show bh selfundress1 with dissolve:
                    zoom 0.85 xalign 0.5 yalign 1.0
                show bh:
                    easein 3 yalign 0.1
                pause 2.8
                show screen parallax1280("bh selfundress1", 0.85) with dissolve
                call showscrollingimage from _call_showscrollingimage_24
                hin"M-more like, weary..."
                mada"Weary I can understand..."
                show screen parallax1280("bh selfundress2", 0.85) with dissolve
                mada"Although I do hope you find it in you to trust me in due time..."
                hin"..."
                scene black with dissolve
                call hidescrollingimage from _call_hidescrollingimage_31


            

            "{color=[obediencecolor]}Allow them to continue...{/color}":
                "Red haired girl" "Shall I proceed, my Lady?"
                call changeObedience("Hinata") from _call_changeObedience_72
                hin"O-okay..."
                show screen parallax1280("bh undress3") with dissolve
                call showscrollingimage from _call_showscrollingimage_25
                "Red haired girl" "There's no need for concern, no one can see us here..."
                hin"Y-yes but... your hands!"
                hin"T-they are in my bra..."
                "Red haired girl" "Why yes, the underwear must be taken off too!"
                show screen parallax1280("bh undress4") with dissolve
                call showscrollingimage from _call_showscrollingimage_26
                "Blonde girl" "But before that, let's take off your pants, shall we my Lady?"
                hin"I... s-suppose so."
                hint"I was not expecting to find myself naked when I woke up this morning..."
                hint"I should have worn something more..."
                $ ui.interact()
                show screen parallax1280("bh undress5") with dissolve
                call showscrollingimage from _call_showscrollingimage_27
                hint"M-modest..."
                hin"T-that's enough! Allow me to lower my own pants, p-please!"
                "Blonde girl" "As you wish, my Lady!"
                $ ui.interact()
                show screen parallax1280("bh undress6") with dissolve
                call showscrollingimage from _call_showscrollingimage_28
                hin"T-thank you, but..."
                hin"My underwear s-stays on..."
                "Blonde girl" "If that is your wish my Lady, then so be it..."
                "Red haired girl" "Such a shame that is, my Lady..."
                "Red haired girl" "The Madame might have something to say about that..."
                "Red haired girl" "She is one that likes to revel in the beauty of our bodies..."
                "Red haired girl" "Especially one as beautiful as yours my Lady!"
                hin"..."
                "Blonde girl" "Let's present you to the Madame then, shall we?"
                call hidescrollingimage from _call_hidescrollingimage_32
                scene black with dissolve




        scene bg onsen1 with dissolve
        show bh onsen1t at left with dissolve:
            zoom 0.65
        
        hin"W-what now..."
        show rangi normal at right with dissolve:
            zoom 0.58
        
        mada "Are you sure you want to keep your undergarments on?"
        mada "The hot springs are best enjoyed when the naturally steamed water brushes against one's naked skin..."
        show bh at smallshake
        hin"I w-will be fine like this..."
        mada "So reserved, Lady [hin_name]..."
        mada "You mustn't worry when you are in my care..."
        mada "But if that's what you wish for, then walk towards the springs where I'll be joining you shortly..."
        hin"..."
        hide bh with dissolve
        hin"I'll be going then..."
        scene bh c1 with dissolve
        mada "Don't let me keep you from it, my Lady..."
        mada "You should dip your toes in, get acclimated to the steaming water..."
        mada "We are to fully submerge ourselves in it once I have made the necessary preparations..."
        scene black with dissolve
        $ renpy.sound.play("/audio/soun_fx/splash1.opus", channel="sfx3", loop=False, relative_volume = 1)
        "[hin_name] sat on the edge of the wooden platform and dipped her legs in the steaming water as instructed by the Madame..."
        scene bh c2 with dissolve
        hint"The springs are so warm, yet so relaxing..."
        hint"But I should not lose focus just yet. Madame seems friendly and kind but..."
        hint"I can't blindly place my trust in her, or anyone else in this place for that matter..."
        hint"Lest I forget, she did mention she is a concubine to the Daimyo..."
        hint"As far as I am concerned her motives are likely to be aligned with those two threatening men from before..."
        hin"And what are those preparations for if I may ask, M-Madame?"
        show bh rangi 1intro with dissolve:
            zoom 0.63 xalign 0.5 yalign 1.0
        show bh:
            easein 2 subpixel True yalign 0.0
        pause 1.8
        show screen parallax1280("bh rangi 1intro",0.63) with dissolve
        call showscrollingimage from _call_showscrollingimage_29
        mada "I shall answer all your questions as soon as I ready myself for you, Lady [hin_name]"
        hin"R-ready yourself... f-for me?"
        call hidescrollingimage from _call_hidescrollingimage_33
        scene bg onsen1 with dissolve
        show bh rangi 1t with dissolve:
            zoom 0.65
        show bh rangi 2t with dissolve:
            zoom 0.65
        mada "Why yes, for I am the one responsible for preparing you, am I not?"
        mada "But as I said before, you shan't keep your guard up when it comes to me, Lady [hin_name]..."
        show bh rangi 3t with dissolve:
            zoom 0.65
        mada "I might be serving the Daimyo in some capacity, but don't mistake me for those simpletons you had to deal with..."
        show bh rangi 4intro with dissolve:
            zoom 0.63 xalign 0.5 yalign 1.0
        show bh:
            easein 2 subpixel True yalign 0.0
        pause 1.8
        show screen parallax1280("bh rangi 4intro",0.63) with dissolve
        call showscrollingimage from _call_showscrollingimage_30
        mada "Not everyone who serves the Daimyo is cut from the same cloth..."
        mada "In fact, me and you are not as different as you'd think we are..."
        "The Madame's outward confidence brimmed from her posture as she nonchalantly stood in front of [hin_name], stripped of all her clothing..."
        "She seductively walked towards the springs where [hin_name] was sitting..."
        call hidescrollingimage from _call_hidescrollingimage_34
        scene bg onsen1
        show bh rangi 4t with dissolve:
            zoom 0.65
        show bh:
            easeout 2 xpos 1600 alpha 0.3
        mada "You see..."
        $ renpy.sound.play("/audio/soun_fx/splash1.opus", channel="sfx3", loop=False, relative_volume = 1)
        scene bh c3 with dissolve
        hin"O-oh!" with vpunch
        mada "I've taken a liking to you, Lady [hin_name]..."
        mada "You remind me a lot of who I used to be... Who I would like to be once again..."
        mada "Before this cruel world gobbled me up, chewed me to pieces and spat me out to where I am today..."
        mada "I can see clearly that behind your reserved mannerisms, there lies a strong woman..."
        mada "A woman of self-respect, unbreakable morals and a resilient will to remain pure..."
        mada "All things that I strived for myself, but never managed to achieve..."
        hin"Madame..."
        scene bh c4 with fade
        $ renpy.sound.play("/audio/soun_fx/splash2.opus", channel="sfx3", loop=False, relative_volume = 1)
        mada "And even though I find myself where I am today..."
        mada "I have not yet given up hope that one day, I can be a little more like you, and a little less like me..."
        hin"You are giving me too much credit, Madame. Besides, how can you assume as much about someone you have only just met?"
        mada "We can work on that you know..."
        hin"H-huh?"
        mada "Getting to know one another..."
        hin"O-oh..."
        mada "Lady [hin_name], I know you might be having trouble trusting me given our circumstances, along with the fact that we've only just met, but..."
        mada "Consider this advice; if not from a friend, then from someone who appreciates your purity and wants for you to keep it..."
        mada "This world is riddled with people pretending to be something they are not. People that want to revel in their self-appointed morality, with complete disregard to anyone but themselves and their twisted ideals."
        mada "In the end, most of everyone partakes in this circus of masquerade and false pretenses that is our world. Hiding behind their carefully sculpted masks serving only to conceal their evil motives and aspirations..."
        mada "Those are the men you'll find occupying this place, including the Daimyo himself..."
        mada "They all partake in this masquerading circus. They will all justify their actions under whatever pretense they can come up with..."
        mada "And when they achieve what they want at the expense of everyone else, they will pat themselves on their backs and sing each other's praises."
        mada "We've both seen such men before, I am sure you can tell them apart just as well as I can, but..."
        mada "What I haven't seen before is someone like you, brimming with a radiant, almost dazzling purity. Completely unmasked and utterly unwilling to play this stupid game of masquerade..."
        mada "That is your strength, but also your weakness Lady [hin_name]..."
        mada "The moment those men or, Lord forbid, the Daimyo himself take note of your purity..."
        mada "Like beasts and savages, they'll quickly pounce on you and try to strip it away from you."
        hin "How would you have me handle the situation then..."
        mada "You won't like my advice, but you'll have to hear it regardless. For your own sake, Lady [hin_name]..."
        mada "Perhaps it's time for you to play this game of masquerade..."
        mada "Mayhaps it's time for you to wear your own mask, a mask that'll keep you safe from all those who seek to take advantage of you."
        mada "You cannot rely on your marital status with the Hokage to protect you from everything, not anymore..."
        mada "And you certainly can't allow these men to walk all over you..."
        mada "Do you understand what I am saying, Lady [hin_name]?"
        hin"I t-think so, but I also don't know how much I can do without my husband's help..."
        mada "Do you see now, where exactly the source of your weakness lies in?"
        mada "Your over-reliance to the Hokage has grown into comfort, and comfort has grown into weakness..."
        mada "These men can see that, they smell blood in the water..."
        mada "You can't allow them to see that, you can't be saying things like 'My husband will take care of it'..."
        hin"So... you know about my problems?"
        mada "I know much more than I let on, for that is my job..."
        hin"Then do you happen to know what the Daimyo is planning? Why is he working with Kumogakure's men in the first place..."
        mada "I am not certain of what exactly that is yet, but one thing I know for certain is..."
        mada "Whatever it is they are planning, it does not bode well for you, Lady [hin_name]..."
        mada "Which is exactly why it's time for you to play their game. It's time for you to get out of your comfort zone..."
        mada "You have to appear strong when you are weak..."
        mada "Likewise, appear weak when you are strong..."
        mada "That, is how you best these men, [hin_name]!"
        mada "Deception, manipulation and your wits are the only things that'll keep you safe."
        hin"But I am not one for deception and manipulation. I am not even sure I could do that if I tried..."
        scene black with dissolve
        mada "*Sigh*"
        $ renpy.sound.play("/audio/soun_fx/splash2.opus", channel="sfx3", loop=False, relative_volume = 1.5)
        mada "Which is why I am here, Lady [hin_name]!"
        "The Madame playfully pulled [hin_name] into the hot springs..."
        show bh onsen1 with dissolve:
            yalign 0.0
        show bh onsen1:
            easein 2 yalign 1.0
        pause 1.8

        show screen parallax1280("bh onsen1") with dissolve
        call showscrollingimage from _call_showscrollingimage_31
        hin"H-hey! At least warn me or something! P-please!"
        call hidescrollingimage from _call_hidescrollingimage_35
        scene black with vpunch
        $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx3", loop=False, relative_volume = 0.8)
        hin"*Gasps*"
        hin"M-Madame!?" with vpunch
        show bh grope2 with dissolve
        mada "There won't always be a warning for everything that befalls you Lady [hin_name]..."
        show rangi_grope1 with dissolve
        mada "The question is, are you prepared to handle unforeseen circumstances?"
        "The Madame softly rubbed and pinched [hin_name]'s nipples as she carefully ran her fingers across her black-laced underwear..."
        hin"W-what exactly is it that you are d-doing?"
        mada "I am measuring you, Lady [hin_name]! In more ways than one..."
        mada "You have a truly astounding body on you..."
        mada "That can be an asset, but more often that not, it can also be a curse..."
        mada "You've seen, how these men look at you, haven't you?"
        mada "They lust for what they see, but much more than that, they lust for the feeling of power over the Hokage's wife..."
        mada "They long for the day where you'll be be bequeathed to them. They pray for a day where not only will your body belong to them, but your will, your thoughts even your desires would be theirs to do with as they please."
        mada "You mustn't give them any ground whatsoever lady [hin_name]..."
        mada "Do you trust me enough to teach you how?"
        hin"..."
        hin"I don't know yet... Maybe I would if you s-stopped t-touching my chest?"
        scene black with dissolve
        $ renpy.sound.play("/audio/soun_fx/splash1.opus", channel="sfx3", loop=False, relative_volume = 1.2)
        mada "*Giggles*"
        mada "I am afraid some more... 'touching' might be required my Lady..."
        mada "Follow me, it's time I prepare you in the way the Daimyo requested you..."
        show bh selfundress7 with dissolve
        mada "But I shall also prepare you in how to deal with someone like him..."
        mada "Pay close attention now my Lady, for this might be the only help you receive from anyone in this place..."
        mada "You see... the Daimyo is a lot of things, but a fool isn't one of them."
        mada "He knows he can't touch you, given your marital status to the Hokage."
        if ch1_dy_200paid == True:
            mada "And as long as you stay vigilant with your financial obligations to him, which I am given to understand you have..."
            mada "He won't have any means of extorting you."
        else:
            mada "But the fact that you find yourself here today, means that he has found a point of weakness in you."
            mada "A weakness he wants to exploit to extort from you everything you hold dear..."
        show bh selfundress8 with dissolve 
        mada "Today he'll try to rid you of what he calls a 'commoners' stench and attempt to cultivate a feeling of submission within you."
        mada "He'll have you lathered up in exotic ointments and dress you up as he likes..."
        mada "But..."
        scene black with dissolve
        $ renpy.sound.play("/audio/soun_fx/splash1.opus", channel="sfx3", loop=False, relative_volume = 1.2)
        "The Madame walked through the waters and approached [hin_name] once again, ready to lather her body up as ordered by the Daimyo..."
        show bh grope2 with dissolve
        mada "You must not allow him to plant the seed of submission within you..."
        mada "Now if you'll excuse me..."
        $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp3.opus", channel="sfx3", loop=False, relative_volume = 0.8)
        show bh grope5 with fade
        hin"M-Madame!?"
        mada "I'll have to rid you of your under-garments if I am to properly apply this ointment on you..."
        mada "Have no concern Lady [hin_name], this procedure is meant to relieve the built up stress and tension you must surely be feeling by now..."
        mada "You shan't worry about your clothes either, I'll have them washed and ready for you to wear as soon as your audience with the Daimyo is over."
        mada "But until then..."
        show rangi_grope2 with dissolve
        mada "You must allow for me to perform my duties..."
        mada "This ointment I am applying all over your body, It's meant to elicit a particular smell the Daimyo finds... arousing."
        hin"A-arousing!?" with vpunch
        mada "Yes, but... all you have to do is heed my advice."
        mada "Your encounter with the Daimyo will be a game of push and pull..."
        mada "Do not bend over to any of his unreasonable demands..."
        mada "Instead, pull where you need to, and let him push only where he has ground to stand on..."
        mada "Makes sense?"
        hin"I won't allow someone as sleazy as what you make this Daimyo sound like walk all over me, Madame..."
        hin"T-thank you for your advice, it seems I was mistaken to distrust you..."
        mada "Being weary was the right call, my lady..."
        mada "But sometimes... Built-up stress can make us misjudge situations, or do things we would otherwise not..."
        scene bh stomach with dissolve
        "The Madame moved one of her hands lower onto [hin_name]'s abdomen..."
        mada "It's important that we find ways to relieve ourselves from that stress..."
        show bh stomach with dissolve:
            zoom 1.3 xalign 0.5 yalign 1.0
        mada "I could assist you with that if you'd like..."
        show bh stomach1 with dissolve
        $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp1.opus", channel="sfx3", loop=False, relative_volume = 0.8)
        $ renpy.sound.play("/audio/soun_fx/splash1.opus", channel="sfx2", loop=False, relative_volume = 1.1)
        "The Madame moved her hand even lower into the water, now brushing against the edges of [hin_name]'s erogenous regions..."
        
        scene bh stomach1 with dissolve
        mada "Do you trust me enough for that, Lady [hin_name]?"
        menu:
            mada "Do you trust me enough for that, Lady [hin_name]?"
            "{color=[obediencecolor]}Y-yes...{/color}":
                hin"B-but w-we are out in the open!"
                mada "There's no need to worry about that, it's just me and you here..."
                hin"If you s-say so..."
                mada "Follow me, Lady [hin_name]. It's best we proceed in less shallow waters..."
                label rangi_mast_jump:
                scene black with dissolve
                hin"O-okay then..."
                $ renpy.sound.play("/audio/soun_fx/splash2.opus", channel="sfx3", loop=False, relative_volume = 1.4)
                mada "Now, if you will allow me, I shall relieve you of the excess stress that troubles you..."
                scene bh cum0 with dissolve
                hin"M-Madame..."
                mada "Relax, [hin_name]... Take deep breaths, close your eyes and allow your body to loosen up."
                $ renpy.sound.play("/audio/soun_fx/femalemast1.opus", channel="sfx3", loop=False, relative_volume = 1.4)
                scene rangi_mast with dissolve:
                    zoom 1.2 xalign 0.7 yalign 0.9
                with vpunch
                hin"*Moans* I will... try."
                "[hin_name] let out a few soft moans as the Madame gently slid her fingers around [hin_name]'s overly sensitive clit."
                "[hin_name] would struggle letting her body relax and instead, involuntarily squeezed her thighs together, almost preventing herself from reveling in pleasure..."
                scene rangi_mast with dissolve
                mada "You are so incredibly tense. Do you not... help yourself at times, Lady [hin_name]?"
                hin"T-that would be indecent t-to my h-husband... Would it n-not?"
                hin"B-but somehow it feels d-different, when another w-woman is..."
                hin"*Moans!*"
                hin"W-when another w-woman is... h-helping."
                $ renpy.sound.play("/audio/soun_fx/femalecum2.opus", channel="sfx3", loop=False, relative_volume = 1.5)
                scene rangi_mast with dissolve:
                    zoom 1.2 xalign 0.7 yalign 0.9
                with vpunch
                "The Madame looked for moments where [hin_name] would relax her thighs and opportunistically slid her fingers inside [hin_name]'s vagina."
                mada "You shan't leave yourself unsatisfied for so long my lady..."
                mada "You are so exceedingly wet down there, the tension you must be feeling must have been eating you alive..."
                mada "That cannot be healthy. Not for the body, nor for the mind..."
                hin"*Soft moans*"
                hin"...Ah...M-Madame..."
                mada "Your muscles have finally loosened up..."
                mada "I want you to try something, Lady [hin_name]..."
                mada "You see... As much as I want to satisfy you, no one knows our bodies better than ourselves do."
                mada "I want you to try lying down over there in the shallow waters..."
                mada "And I want you to give yourself the pleasure you deserve."
                $ renpy.sound.play("/audio/soun_fx/femalemast3.opus", channel="sfx3", loop=False, relative_volume = 1.8)
                hin"The p-pleasure... I d-deserve?"
                hin"I h-haven't done that in so long. I am not even s-sure If I can do that without your h-help..."
                mada "We won't know until you try, my Lady..."
                mada "Come on, I'll be right there with you!"
                hin"..."
                scene bh cum1 with dissolve:
                    yalign 0.0 subpixel True
                show bh cum1:
                    easein 3 yalign 0.7
                pause 2.5
                show screen parallax1280("bh cum1") with dissolve
                call showscrollingimage from _call_showscrollingimage_32
                hin"It f-feels so wrong d-doing this out in the open..."
                $ renpy.sound.play("/audio/soun_fx/femalemastmoan1.opus", channel="sfx3", loop=False, relative_volume = 1.1)
                show screen parallax1280("hin_mast_onsen1") with dissolve
                call showscrollingimage from _call_showscrollingimage_33
                hin"And yet... It f-feels so g-good!"
                "[hin_name] still reserved, but now fully immersed in her own desires, started playing with herself..."
                "An overwhelming feeling of pleasure, a feeling that was all but forgotten to her would now deeply burrow in her thoughts."
                "As much as [hin_name] thought the act indecent, that same feeling demanded from herself to see this to its end. She was now determined to bring herself to climax."
                mada "Yes, Lady [hin_name]! it does feel good, doesn't it?"
                mada "We must be able to satisfy our own desires, otherwise our minds turn hazy..."
                mada "Our thinking loses its edge, and we make stupid decisions we would otherwise not."

                hin"I... S-something's c-coming out!"
                $ renpy.sound.play("/audio/soun_fx/femalemastmoan1.opus", channel="sfx3", loop=False, relative_volume = 1.3)
                call hidescrollingimage from _call_hidescrollingimage_36
                scene black with dissolve
                scene bh cum1_2 with dissolve:
                    yalign 0.0
                show bh cum1_2 with dissolve:
                    yalign 0.5
                hin"*Audible Moans*"
                show bh cum2 with flash:
                    yalign 0.0
                $ renpy.sound.play("/audio/soun_fx/femalecum1.opus", channel="sfx2", loop=False, relative_volume = 1.2)
                hin"Uuuh... *Moans* Aaah!" with vpunch
                show bh cum2 with flash:
                    yalign 0.7
                pause 0.2
                scene bh cum2 with dissolve:
                    yalign 0.0 subpixel True
                show bh cum2:
                    easein 3 yalign 0.7
                pause 2.5
                show screen parallax1280("bh cum2") with dissolve
                call showscrollingimage from _call_showscrollingimage_34
                call hidescrollingimage from _call_hidescrollingimage_37
                mada "Yes, that's it! Let it all out!"
                $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx3", loop=False, relative_volume = 0.4)
                $ renpy.sound.play("/audio/soun_fx/femalemastmoan2.opus", channel="sfx2", loop=False, relative_volume = 1.8)
                $ renpy.sound.play("/audio/soun_fx/femalegrunt1.opus", channel="sfx1", loop=False, relative_volume = 0.4)
                show bh cum3 with flash:
                    zoom 0.63 xalign 0.5
                hin"*Loud Moans*"
                "A large amount of fluid oozed out as the Madame stepped in to help [hin_name] reach climax!"
                show bh cum3 with flash:
                    zoom 0.63 xalign 0.5 yalign 0.25
                hin"MMmhh...Aah!♡!"
                hin"It f-feels l-like ♡...!♡?"
                show bh cum3 with dissolve:
                    zoom 0.63 xalign 0.5 yalign 0.7
                mada "Now rub the clit, Lady [hin_name]!" with flash
                mada "Allow the fluid to shoot out!" with flash
                $ renpy.sound.play("/audio/soun_fx/cum0.opus", channel="sfx3", loop=False, relative_volume = 0.4)
                $ renpy.sound.play("/audio/soun_fx/femaleclimax.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                show bh cum4 with flash:
                    zoom 0.63 xalign 0.5 yalign 1.0 subpixel True
                hin"Aaah!? ♡ Aah!! ♡" with vpunch
                show bh cum4 with flash:
                    easein 3 yalign 0.1
                pause 2.7
                show screen parallax1280("bh cum4", 0.63) with dissolve
                call showscrollingimage from _call_showscrollingimage_35
                hin"*Orgasmic Moans* Aaah!? ♡ Mmhmhm!!♡"
                "[hin_name] kept rubbing her clit as instructed by the Madame while her fluids kept shooting out of her vagina like a fountain."
                "Her muscles started convulsing as the orgasmic feeling she was experiencing rippled throughout her body..."
                hin"*Heavy breathing*"
                show screen parallax1280("bh cum4_1", 0.63) with dissolve
                call showscrollingimage from _call_showscrollingimage_36
                $ renpy.sound.play("/audio/soun_fx/cum0.opus", channel="sfx3", loop=False, relative_volume = 0.4)
                $ renpy.sound.play("/audio/soun_fx/femalecum2.opus", channel="sfx2", loop=False, relative_volume = 1.4)
                $ renpy.sound.play("/audio/soun_fx/femalegrunt1.opus", channel="sfx1", loop=False, relative_volume = 0.4)
                hin"Aaah!? ♡ Aah!! ♡" with flash
                "Another wave of orgasms shot through [hin_name]'s entire body, as she watched in awe while her pussy produced amounts of fluid she's never seen before."
                "The orgasm she felt was strong enough to make her question all her previous sexual encounters."
                call hidescrollingimage from _call_hidescrollingimage_38
                show bh cum5 with flash:
                    zoom 0.63 xalign 0.5 yalign 1.0 subpixel True
                show bh cum5:
                    easein 3 yalign 0.1
                pause 2.7
                show screen parallax1280("bh cum5_1", 0.63) with dissolve
                call showscrollingimage from _call_showscrollingimage_37
                "[hin_name] leaned backwards in an attempt to limit her body's convulsions while trying to catch her breath..."
                mada "Look at you, Lady [hin_name]! I don't think I've ever seen someone had an orgasm as strong as yours before..."
                mada "Even after that impressive feat of squirting, your pussy juices are still flowing down my springs..."
                mada "Naughty girl! *Giggles Playfully*"
                call hidescrollingimage from _call_hidescrollingimage_39
                show screen parallax1280("bh cum6", 0.63) with dissolve
                call showscrollingimage from _call_showscrollingimage_38
                hin"*Panting* M-Madame... W-what just happened?"
                hin"I... I've never felt like t-this b-before..."
                mada "You cannot be serious... Can you, my Lady?"
                hin"W-what do you mean..."
                mada "You don't mean to tell me that..."
                mada "Throughout your life, a lady as beautiful and as long-lived as yourself has never felt an orgasm before?"
                mada "What the hell is that stupid husband of yours good for then!?" with vpunch
                hin"W-what!? [na_name] is l-loving and c-caring, b-but-"
                mada "Your husband [hin_name]! Is he stupid, or impotent!? Which one is it..." with vpunch
                hin "P-please Madame, He is neither... I think."
                hin"It's just that... He isn't around much..."
                hin"And when he is, we simply do the deed. He p-puts his thing inside and a few seconds later we are d-done..."
                mada "A few... s-seconds!?" with vpunch
                hin"I've n-never been with anyone else and I don't touch myself m-much, so..."
                call hidescrollingimage from _call_hidescrollingimage_40
                show bh cumfinal with dissolve:
                    zoom 0.63 xalign 0.5 yalign 1.0 subpixel True
                show bh cumfinal:
                    easein 3 yalign 0.1
                pause 2.7
                show screen parallax1280("bh cumfinal", 0.63) with dissolve
                call showscrollingimage from _call_showscrollingimage_39
                mada "Good lord, Lady [hin_name]!" with vpunch
                mada "Have you went your entire life feeling nothing but a few seconds of your husband's prick!?" with vpunch
                hin"Is t-that... bad?"
                mada "Why y-yes, It's bad!" with vpunch
                mada "Don't you want to feel what you felt here today again?"
                hin"Y-yes... If it's with my husband!"
                mada "Then you better tell that stupid husband of yours to satisfy your needs, or I will drag myself to your bedroom and do it myself!" with vpunch
                hin"*Soft Giggle* M-Madame, stop it..."
                mada "*Scoffs* Look at you lying there like a princess from a fairy tale, even the cherry blossoms are drawn to your unadulterated purity."
                mada "So ignorant of all the pleasure life can give us, if only you would seek it!"
                mada "*Sigh*"
                mada "Well... I am glad I could at least introduce you to something you've never experienced before..."
                
                mada "But am afraid we are running out of time. Wash yourself and meet me at the patio my Lady."
                hin"I'll be there in a second..."
                hint"So it's time to meet this Daimyo..."
                hint"It's a good thing I met the Madame when I did. Thanks to her, I feel so much better now..."
                hint"If I heed her advice, I am sure there'll be nothing to worry about!"
                scene black
                call hidescrollingimage from _call_hidescrollingimage_41

            "N-no!":
                hin"N-no! I don't even know you, p-please..."
                scene bh stomach with dissolve
                mada "Such a shame, I thought we could be good friends, me and you..."
                hin"M-maybe... but you are m-moving too fast!"
                mada "Please excuse me my Lady... I did not mean to intrude over your personal boundaries."
                hint"She really doesn't seem like a bad person. Why else would she give me all the advice she did?"
                hint"Maybe it's best if I k-keep her close...?"
                menu:
                    hint"Maybe it's best if I k-keep her close...?"
                    "{color=[obediencecolor]}If y-you promise to be g-gentle...{/color}":
                        hin"No I..."
                        hin"I am s-sorry, I over-reacted."
                        hin"If you p-promise to be g-gentle, then..."
                        $ renpy.sound.play("/audio/soun_fx/splash1.opus", channel="sfx3", loop=False, relative_volume = 1.1)
                        scene bh stomach1 with dissolve
                        mada "Are you sure, my Lady?"
                        hin"I... don't know..."
                        mada "Then let us proceed cautiously. You can let me know if you would like for me to stop..."
                        jump rangi_mast_jump
                    "You did not intrude, but...":
                        hin"You didn't intrude, Madame..."
                        hin"But I just can't do something like that..."
                        mada "I understand, you needn't justify yourself to me, my Lady..."
                        mada "But am afraid we are running out of time. Wash yourself and meet me at the patio my Lady."
                        scene black with dissolve
                        jump madameending

        label madameending:
        scene black with dissolve
        $ renpy.sound.play("/audio/soun_fx/splash2.opus", channel="sfx3", loop=False, relative_volume = 1.1)
        show bg onsen1 with dissolve
        show bh rangi 2t at right with dissolve:
            zoom 0.56
        mada "I hope [hin_name] can deal with what is to come..."
        show bh rangi 1t at right with dissolve:
            zoom 0.56
        mada "There she is..."
        show bh:
            easein 1 xalign 0.2
        mada "Here, Lady [hin_name]. Use this towel to dry yourself up..."
        scene black with dissolve
        show hinata towelintro1 with dissolve:
            zoom 0.83 yalign 1.0 xalign 0.5
        show hinata:
            easein 2 yalign 0.1
        pause 1.9
        show screen parallax1280("hinata towelintro1", 0.83) with dissolve
        call showscrollingimage from _call_showscrollingimage_40
        hin"T-thank you..."
        show screen parallax1280("hinata towelintro", 0.83) with dissolve
        scene black with dissolve
        "[hin_name] took a moment to pat herself dry..."
        mada "Make sure you wrap that towel around your body as tight as you can. You are going to need it to hold for quite some time I am afraid..."
        hin"W-what? ...But why?"
        call hidescrollingimage from _call_hidescrollingimage_42
        show bg onsen1 with dissolve
        show rangibu at right with dissolve:
            zoom 0.56
        show thina b1 at left with dissolve
        mada "The Daimyo..."
        show thina shy with dissolve
        hin"W-what about him?"
        mada "He wants you to appear before him in nothing but the towel..."
        hin"W-what!?" with vpunch
        mada "I am sorry, I wish there was something I could do to help..."
        hin"W-without any under-garments?"
        mada "Yes..."
        hin"And w-with the towel being this s-short!?" with vpunch
        show thina b2 with dissolve
        hin"It barely covers my behind..."
        show thina shy2 with dissolve
        hin"Same for my chest..."
        mada "Remember what I said, Lady [hin_name]..."
        mada "He'll play his little game but..."
        mada "You have to appear strong, even while you are feeling weak! Now is that moment..."
        show thina shy with dissolve
        hin"I can't! N-not like this..."
        mada"Remember, he can't touch you! He might be the Daimyo, but you are the Hokage's consort!"
        show rangi angry at right:
            zoom 0.56
        hide rangibu
        with dissolve
        mada"You are strong, aren't you [hin_name]!?"
        show thina angry with dissolve
        hin"I am!"
        mada"Then muster up your courage and show that to anyone who'd question it!"
        hin"Y-you are right! I'll do my best..."
        show rangi normal behind thina with dissolve
        mada"Good!"
        show rangi:
            easein 1 xalign 0.4
        mada"Then let us make our way to his chambers, shall we?"
        hin"Y-yes!"
        show thina:
            easein 1 xalign -1.5
        show rangi:
            easein 1 xalign -0.5
        scene black with dissolve
        $ renpy.end_replay()
        label replay_daimyointroduction:
        $ initialize_replay_defaults()
        scene palace3 with dissolve
        show rangi angry at right:
            zoom 0.56
        show thina shy
        with dissolve
        "The two of them walked through multiple corridors and long hallways..."
        hin"Everyone's staring at us, Madame..."
        mada"Not us... Just you, Lady [hin_name]."
        mada"Can you blame them?"
        "Barefoot and in nothing but a towel, [hin_name] would inevitably draw the looks of servants, guards and anyone else who happened to be in the viscinity..."
        hin"It's so e-embarassing..."
        mada"Pay them no attention, my Lady..."
        mada"Let's keep moving, we are almost there."
        show thina:
            easein 1 xalign -1.5
        show rangi:
            easein 1.5 xalign -1.2
        hin"O-okay..."
        scene black with dissolve
        hint"Come on, [hin_name]! Stay focused..."
        scene palace2 with dissolve
        show rangi normal at right:
            zoom 0.56
        show thina shy
        with dissolve
        hint"I am losing my cool, this isn't good..."
        "You made it atop the golden palace. One more staircase stood before you and the Daimyo's chambers."
        mada"Stay calm, Lady [hin_name]! Remember what we discussed..."
        mada"Once we climb this staircase, you'll be on your own."
        hin"I can do this..."
        mada"Alright then, let us proceed..."
        hide thina with dissolve
        hide rangi with dissolve
        "The sound of [hin_name]'s bare feet hitting the wooden stairs alerted the guards standing outside the Daimyo's chambers..."
        "Guards" "Who goes there!" with vpunch
        show daimyo dm1 with dissolve
        $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp1.opus", channel="sfx3", loop=False, relative_volume = 1.0)
        hint"*Silent Gasp*"
        show halfblack with dissolve
        show thina annoyed at left with dissolve
        hint"These two... Darn it!"
        hint"To think that even them get to see me like this..."
        show rangi angry at right with dissolve:
            zoom 0.56
        mada"Move aside, you imbeciles. Lady [hin_name] is expected by his highness..."
        hide thina
        hide rangi
        hide halfblack
        with dissolve
        $ renpy.sound.play("/audio/soun_fx/catcall.opus", channel="sfx3", loop=False, relative_volume = 1.0)
        show daimyo dm2 with dissolve:
            zoom 1.2 xalign 1.0 yalign 0.0
        ko"*Wolf Whistle*"
        ko"Looking real nice, Ladies..."
        ko"Especially the Lady of the Leaf..."
        dm"Hehehe..."
        "The Madame leaned in close to [hin_name]'s ear and whispered..."
        mada"{size=*0.8}Pay them no attention my Lady. Remember everything we've talked about...{/size}"
        mada"Let her through!" with vpunch
        dm"With... pleasure!"
        mada"And keep your hands to yourselves, or the Daimyo hears of your transgressions!"
        show daimyo dm2 with dissolve:
            zoom 1.4 xalign 0.5 yalign 0.5
        "Both men would violate [hin_name]'s body with their eyes as she walked between the small gap they intentionally left between the two of them..."
        scene black with dissolve
        show hinata towel annoyed at center with dissolve:
            zoom 0.8
        "[hin_name]'s shoulders would brush against the men's while their gazes fixated on her almost nude appearance. [hin_name] could tell, but there was naught she could do..."
        hide hinata with dissolve


        label daimyomeeting:
            default daimyomeeting_insultappearance = False #Hinata disrespects daimyo's appearance
            default daimyomeeting_ignorecompliment = False #Hinata ignore daimyo's compliment by staying silent
            default daimyomeeting_declinedoffer = False #Hinata declines Daimyo's offer for Himawari
            default daimyomeeting_confusedwhyhere = False #daimyo asks why Hinata is here and Hinata is confused

            default daimyomeeting_counter = 0

            $ renpy.sound.play("/audio/soun_fx/doorclose.opus", channel="sfx3", loop=False, relative_volume = 1.0)
            "Her focus was on the real challenge that lay ahead..."
            
            show daimyo 1 with Dissolve(2)
            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp4.opus", channel="sfx3", loop=False, relative_volume = 1.0)
            hin"*Gasps*" with vpunch
            "As much as [hin_name] tried to hide her surprise, the repulsive appearance of the man before her left her utterly speechless. A single audible gasp escaped her lips before she managed to contain a reaction of disgust that almost made her gag..."
            hint"How could a man of such importance, such wealth even... be so unkempt?'"
            "One would expect nobility to be a defining trait of someone as highly situated as the Daimyos are."
            "A title reserved for only five of the most important men across the world. Men that are in charge of entire Nations..."
            "Instead, [hin_name] stood before a gluttonous, unshaven, greasy old man, who slouched in his oversized throne, in nothing but his underwear. His face, bloated and riddled with unpleasant bumps and dark spots."
            show halfblack
            show thina angry at right:
                zoom 1.1 xpos 1.15
            with dissolve
            "[hin_name] mustered as much confidence as she could and faced the Daimyo directly..."
            hint"T-this... is the Daimyo!?"
            
            "Her surprised was clearly painted on her face. The Daimyo would surely be able to tell what she was thinking..."
            hint"W-why is he naked?"
            hint"Not to mention how s-sleazy he looks, dirty even..."
            hint"Is this really who Madame refers to as 'His Highness'?"
            hint"And to think she even lays with him..."
            hide halfblack with dissolve
            da"Oooo-hoo-hoooo...!"
            da "So this is the famous Lady of the Leaf, consort to the Hokage..."
            da "Lady [hin_name], was it? Your reputation preceeds you, my lady... For I have never seen a woman of such lustrous beauty as yours!"
            menu:
                da "Lady [hin_name], was it? Your reputation preceeds you, my lady... For I have never seen a woman of such lustrous beauty as yours!"
                "Thank him...":
                    show thina annoyed with dissolve
                    hin"T-thank you, your highness..."
                    da"You shan't thank me just yet, my Lady."
                    da"There is a lot the two of us must discuss before we exchange... pleasantries!"
                "Stay silent":
                    show thina annoyed with dissolve
                    $ daimyomeeting_ignorecompliment = True
                    $ daimyomeeting_counter +=1
                    hin"..."
                    da"Silence is an alluring trait, my lady. But do be careful of how you use it, or it might just invite more curiosity, and curiosity can be far more perilous than words..."
                    da"Hee-Heee... *Wheezing* Hee... "
            da"If I may ask, was there a reason you were surprised when you first stepped into my chambers? Do you perhaps find my choice of clothing to be questionable?"
            menu:
                da"If I may ask, was there a reason you were surprised when you first stepped into my chambers? Do you perhaps find my choice of clothing to be questionable?"
                "Lie...":
                    $ daimyomeeting_insultappearance = True
                    $ daimyomeeting_counter += 1
                    hin"I wasn't surprised m-my lord..."
                    da"Are you sure my Lady? I could have sworn I heard a gasp as soon as you walked into my chambers..."
                    da"Could that be the imagination of an old man playing tricks on him? Hmm?"
                    show thina angry with dissolve
                    hin"M-mayhaps, my lord..."
                    da"Or could the Lady be lying to me..." with vpunch
                    show thina shy with dissolve
                    hin"I w-would never! M-my lord..."
                    da"Careful now my Lady... I don't take kindly to liars, much less so with those that would insult my appearance!"
                    show thina annoyed with dissolve
                    hin"..."
                "I was surprised by your attire":
                    hin"Y-yes, I was surprised by your attire..."
                    da"As I have suspected then..."
                    da"I appreciate your honesty, Lady [hin_name]!"
                "I was surprised by your appearance":
                    $ daimyomeeting_insultappearance = True
                    $ daimyomeeting_counter += 1
                    hin"N-no! I was surprised by your appearance..."
                    da"My appearance? Is there something wrong with the way I look, my Lady?"
                    show thina shy with dissolve
                    hin"O-of course not! It's just that, I was expecting noble-like attire..."
                    hin"But there's nothing wrong with your looks m-my lord!"
                    show daimyo 4 with fade
                    da"O-oooh? Do you mean to say that you find me attractive, my Lady?"
                    "The Daimyo leaned forward in excitement awaiting [hin_name]'s reply..."
                    menu:
                        da"O-oooh? Do you mean to say that you find me attractive, my Lady?"
                        "{color=[obediencecolor]}Y-yes (Lie){/color}":
                            hint"W-what have I done!"
                            hint"I should probably lie on this occasion to avoid angering him..."
                            call changeObedience("Hinata", 1) from _call_changeObedience_73
                            show thina thinking with dissolve
                            hin"Y-yes my lord. Y-you are quite pleasing to the eye..."
                            da"Ooo-hoo-hooo!"
                            scene daimyo 4_1 with dissolve:
                                zoom 1.2 xalign 0.5 yalign 1.0
                            da"Pleasing to the eye, am I?"
                            da"Can you feel the tension building up between the two of us, my Lady?"
                            da"Perhaps we should do something about that! If your husband wouldn't mind of course..."
                            scene daimyo 4_1
                            show thina shy at right:
                                zoom 1.1 xpos 1.15
                            with dissolve
                            hint"!!" with vpunch
                            show thina thinking with dissolve
                            call changeObedience("Hinata", 1) from _call_changeObedience_74
                            hin"I-i-i d-don't think that's a good idea, m-my lord!"
                     
                            da"Heeee-Heee! *Wheezing*"
                            da"I only jest of course, my lady! Excuse my inappropriate comments!"
                            show daimyo 3 with fade
                            da"I see you are a woman that does not hesitate to lie if it serves your agenda, isn't that right... Lady [hin_name]?"
                            hin"..."
                            da"Do be careful on how you proceed, for there's one thing I despise more than peasantry..."
                            da"And that is filthy, peasant liars!" with vpunch
                            show daimyo 1 with fade
                            da"I shall see past this one occasion given your well-intentioned comments. But please, do speak truthfully with me from this moment onwards my Lady..."
                            hin"Y-yes my lord..."
                            $ daimyomeeting_counter += -1
                            
                        "No!":
                            hin"F-forgive me my l-lord... but I am already betrothed to my h-husband!"
                            show daimyo 3 with fade
                            da"Ah... yes! Your husband! How could I forget! Silly me..."
                            show daimyo 1 with fade
                            da"But who knows what the future holds! Relationships come and go and broken hearts are all that lie in their wake..."
                            da"Which is why I am polygamous myself! You should perhaps consider that my Lady..."
                            show thina annoyed with dissolve
                            hin"..."
                            da"Food for thought! We have more pressing matters to attend..."

                
            show blackscreen with dissolve
            hide blackscreen with dissolve
            da"So what, if I am in my underwear. Don't you do the same at your home?"
            show thina annoyed with dissolve
            hin"Of c-course not! I have children..."
            da"Oh yes, children! I have plenty of those myself you know..."
            da"More than twenty of them I wager, but I wouldn't know, I lose track of them..."
            da"I believe you've met one of my concubines responsible for some of them, have you not?"
            da"I forget her name but, her wavy ginger colored hair makes her easily recognizable..."
            hin"The Madame, Y-yes... I've met with her."
            da"The 'Madame'... *chuckles* She likes to call her self that. Gives her an unjustified feeling of empowerment I imagine..."
            da"Has she treated you well, that one?"
            hin"S-she did..."
            da"Of course she did. A heart of gold in that woman..."
            da"Bundled with the body of a whore! *Wheezing Laughter*" with vpunch
            da"You can see why I've taken a liking to that one..."
            da"Three daughters she bore for me, can you believe that? All three as beautiful as their mother!"
            da"Or so I'd think. It's been years since I last saw any of my children. A man of my stature has no time to pamper children..."
            da"Not until the boys grow into fine warriors, and the girls into... beautiful, charming women."
            da"Hee-hee-heeeee..."
            da"But enough about my children, let's talk about yours!"
            if him_age == '18':
                da"A young boy and an eighteen year old girl, isn't that right?"
            else:
                da"A young boy and a [him_age] year old girl, isn't that right?"
            hin"*Gasps*"
            hint"H-how does he know as much as he does!?"
            da"The boy isn't of much interest to me. But your daughter..."
            da"Hi... Mi... Ha... W-what was her name again? Help an old man out my Lady, will you?"
            hint"D-darn it! I can't think of a way to avoid his question..."
            $ him_name_stutter = format_name_with_prefix(him_name)
            hin"H-her name is... [him_name_stutter]."
            da"Ah, yes! [him_name]..."
            da"A pretty name for a pretty girl, just like her mother!"
            da"I've been thinking you know..."
            if ch1_dy_200paid == False:
                
                da"It would seem like you are running into some financial troubles, given how you failed to meet your obligations to me..."
                da"And while you yourself are old, used and cumbersome..."
                da"Your daughter is quite young and ripe for... work!"
                da"I am a benevolent ruler you see! I could offer [him_name] a post in my manor where she'd be compensated handsomely for her efforts!"
                da"Given her own willingness of course... She could help in my kitchens, scrub the floors, assist in the hot springs, or..."
                da"She could even work directly for me if she would prefer! What say you, Lady [hin_name]... Would you consider my generous offer?"
                menu daimyojoboffer:
                    da"She could even work directly for me if she would prefer! What say you, Lady [hin_name]... Would you consider my generous offer?"
                    "I will keep that in mind (Lie)":
                        hin"I appreciate your g-generous offer m-my lord..."
                        hin"I will keep that in mind..."
                        da"You do that, my Lady! *Wheezing laughter*"
                        hint"I would never, ever consider that!" with vpunch 
                        hint"But I need to tread carefully around this man..."
                    "N-never!":
                        hin"I will h-have to humbly d-decline your g-generous offer my lord..."
                        hin"[him_name_stutter] is still young, she should remain focused on her studies..."
                        da"Heeee-heee-heeee! Studies, of course! An important aspiration..."
                        da"You and your daughter are of course allowed to pursue your own aspirations, so long as you fulfil your obligations to me, Lady [hin_name]..."
                        da"Otherwise, I'd have to find creative ways for you to pay off your debts and lest you know, my creativity knows no bounds..."
                        da"Do I make my self clear, my Lady?"
                        hin"Y-yes..."
                        $ daimyomeeting_declinedoffer = True
                        $ daimyomeeting_counter += 1
                    
            else:
                da"If your household is ever in need of some additional income, I certainly have a use for someone as pretty as your daughter..."
                da"I am a benevolent ruler you see! I could offer [him_name] a post in my manor where she'd be compensated handsomely for her efforts... and her appearance!"
                da"Given her own willingness of course... She could help in my kitchens, scrub the floors, assist in the hot springs, or..."
                da"She could even work directly for me if she would prefer! What say you, Lady [hin_name]... Would you consider my humble offer?"
                jump daimyojoboffer





            #after job offer
            "The Daimyo stares at [hin_name] for a few moments..."
            da"Hmm..."
            da"...Excellent!" with vpunch
            da"Let's move on to more pressing matters, shall we?"
            hin"..."
            da"I see before me the Lady of the Leaf, consort to the Hokage, and bearer of the famous Hyuuga bloodline..."
            da"By all intents and purposes, a powerful woman! Alas..."
            da"All I am met with, is stark silence and a jittery stance. Is there something wrong... my lady?"
            da"Are you perchance confused as to why you find yourself standing before me?"
            menu:
                da"Are you perchance confused as to why you find yourself standing before me?"
                "I was forced to be here!":
                    if ch1_dy_200paid == True:
                        hin"I... I was forced to be here!"
                        hin"We have paid our debt to you, have we not!?" with vpunch
                        da"Oooo-hoo-hoooo! There she is!"
                        da"The fierce Kunoichi I've heard stories about..."
                        da"You hide your fangs well, my Lady!"
                        hin"..."
                        da"Forced indeed you were, but not for nefarious reasons!"
                        da"Given your status as consort to the Hokage, I thought I'd do you a small favor..."
                        da"I simply thought it fair, to inform the Lady of a few... precarious matters that might concern you. Which is why I summoned you!"
                        
                    else:
                        hin"I... I was forced to be here!"
                        da"Forced? I thought you a woman of intelligence and perception, was I mistaken my Lady?"
                        hin"..."
                        da"Have you not failed to comply with multiple warnings in regards to your debts to me...?"
                        da"Did you perhaps think your disservice would go unpunished because of your marital status to the Hokage?"
                        da"*Tsk tsk tsk* You disappoint me, my Lady..."
                        da"You should be counting your blessings for being able to freely roam my palace..."
                        $ daimyomeeting_confusedwhyhere = True
                        $ daimyomeeting_counter += 1

                "You tell me, why am I here?" if ch1_dy_200paid == True:
                    hin"You tell me, have we not paid our debts to you!?"
                    hin"So why am I here!"
                "Is it because of our debt to you?" if ch1_dy_200paid == False:
                    hin"Is it because of our debt to you?"
                    da"Why Yes! How perceptive of you..."
                    da"But one would assume that the punishment for failing to meet your obligations to me would be much more severe than what you are going through, wouldn't you agree my Lady?"
                    hin"..."
                    da"Oh yes, your insistence with staying silent is one that I quickly tire off, my Lady..."
                    da"But I'll refrain, for now..."
                    

                "...":
                    hin"..."
                    if daimyomeeting_ignorecompliment == True:
                        da"*Groans* The silent treatment again..."
                        da"You keep disappointing, my Lady! I though I already told you, didn't I?"
                        da"Your silence only serves to irk me more and more..."
                        da"I can only fill your utter silence with my own assumptions..."
                        da"And right now, my assumptions are telling me you are playing a dirty game with me, aren't you my Lady?"
                        hin"N-no, my lord! I am simply at a loss for words before you..."
                        da"Hmm..."
                    else:
                        da"Silence is an alluring trait, my lady. But do be careful of how you use it, or it might just invite more curiosity, and curiosity can be far more perilous than words..."
                        da"Hee-Heee... *Wheezing* Hee... "

                
                
            show daimyo 3 with fade
            da"But you see, there's a more important reason than your debts for which you find yourself standing before me..."
            da"Given your status as consort to the Hokage, I thought I'd do you a small favor..."
            da"I simply thought it fair, to inform the Lady of a few... precarious matters that might concern you. That is why I summoned you, Lady [hin_name]."
            hin"P-precarious... matters?"

            if ch1_dy_200paid == False:
                $ daimyomeeting_counter += 1 #Adds 1 to anger counter if not paid
                da"Yes indeed, precarious matters that might even involve your husband!"
                hin"[na_name]!? W-what do you know of him... answer me please!"

                if daimyomeeting_counter >= 3:
                    label daimyo_cruelapology:
                        $ initialize_replay_defaults()
                        $ notification(f"{hin_name} has angered the Daimyo")
                        show screen scrollingtext(f"{hin_name} has angered the Daimyo")
                        da"Making demands now, are you...?"
                        scene daimyo 3_1 with dissolve:
                            zoom 1.2 xalign 0.5 yalign 0.1
                        da"You insolent worm!" with vpunch
                        da"I invite you into my chambers with every willingness to help, being as courteous as one can be, and yet..." with vpunch
                        scene daimyo 3_1
                        show thina annoyed at right:
                            zoom 1.1 xpos 1.15
                        with dissolve

                        da"All I am met with is a constant barrage of disrespect!" with vpunch
                        show thina shy with dissolve
                        hin"I meant n-none! M-my lord..."
                        da"You meant none!? Allow me recount your transgressions then!" with vpunch
                        da"First..."
                        if daimyomeeting_insultappearance == True:
                            da"You dared to insult my appearance and attempt to hide that behind a feeble lie!"
                            da"If that were not enough..."
                        if daimyomeeting_ignorecompliment == True:
                            da"You utterly and completely ignored my compliments to you. Instead, you treated me only to your complete and utter silence!"
                            da"Am I perhaps beneath you, my Lady? Am I undeserving of even your words!?"
                        if daimyomeeting_declinedoffer == True:
                            da"You even declined my generous employment offer for your daughter..."
                        if daimyomeeting_confusedwhyhere == True:
                            da"And if all that were not enough. You act as if you don't even know why you find yourself standing before me!"
                        label faildaimyoapology:
                        da"*Groans*..."
                        da"Disrespectful on every conceivable level. Shameless, really..."
                        hin"Again, m-my lord... I did not mean any disres-"
                        da"SILENCE!" with vpunch
                        da"You will stay quiet, for every word you have spoken up until now was a dagger that pierced my generous heart..."
                        da"This will be my last warning to you..."
                        da"You so much as dare show another sign of disrespect and I swear you will find yourself imprisoned in my dungeons..."
                        da"Do I make myself clear, my Lady?"
                        menu:
                            da"Do I make myself clear, my Lady?"
                            "Y-yes...":
                                hin"Y-yes, my lord..."

                            "...":
                                hin"..."
                                da"Heee-hee-hee.. You've taken my plea for silence quite literally I see..."
                        show daimyo 1 with dissolve
                        da"Excellent!"
                        da"Now, I believe you owe me an apology..."
                        da"How would you go about providing it, my Lady...?"
                        $ daimyoapologizemenu = []
                        menu daimyoapologize:
                            set daimyoapologizemenu
                            da"How would you go about providing an apology, my Lady...?"
                            "'I apologize...'":
                                hint"Would a simple spoken apology suffice?"
                                show thina annoyed with dissolve
                                hin"I apologize, my Lord..."
                                da"Heee-heee-hee... You think simple words can absolve you of your transgressions?"
                                da"Surely you can think of something more..."
                                jump daimyoapologize
                            "Courteously bow":
                                hint"I don't know what he expects from me..."
                                hint"Maybe..."
                                show thina bow1 with dissolve:
                                    xzoom -1
                                hint"This will satisfy him?"
                                hin"My sincerest apologies, your highness!"
                                da"A fine bow, my Lady!"
                                da"But surely you can go a little lower than that, can't you?"
                                hint"I suppose a low bow isn't the worst he could ask for..."
                                show thina bow2 with dissolve
                                hin"Y-you are right, my lord..."
                                da"Indeed I am! For a deeper bow tells of deeper respect!"
                                da"Go on then, my Lady! Show me..."
                                da"Is this a bow of respect? A bow fitting of the apology you owe to me?"
                                hint"D-Damn him!"
                                show thina bow3 with Dissolve(1)
                                pause 1.5
                                hin"It was not. My apologies your highness..."
                                hin"Is this more to your satisfaction?"
                                show daimyo 4 with fade
                                da"Heee-heee-heee..."
                                show daimyo 4_1 with dissolve
                                da"My Lady... I fear there might have been a misunderstanding on your part..."
                                da"Raise your head and look me straight into my eyes..."
                                show thina bow1 with dissolve
                                hin"...M-my Lord?"
                                "[hin_name] had yet to realize the Daimyo's excitement..."
                                da"Move over to the middle for me, would you?"
                                show thina bow1 with dissolve:
                                    easein 2 xalign 0.5
                                da"Good, good. Now..."
                                da"We are only going to do this one more time..."
                                da"If you fail to provide a sufficient apology, you'll spend the rest of the day... and the night, in my dungeons."
                                hint"W-what!?" with vpunch
                                hin"W-what am I to do, my L-lord!?"
                                da"Have I not been clear my Lady? A bow of greater depth, shows greater remorse..."
                                show thina bow3 with Dissolve(1)
                                hint"What does he want me to do! Kneel before him?"
                                da"Deeper!" with vpunch
                                hint"D-darn it!... D-do I really have to do this?"
                                hint"If it's just kneeling then..."
                                scene daimyo apologize 1 with dissolve:
                                    subpixel True yalign 1.0
                                show daimyo:
                                    easein 2 yalign 0.0
                                pause 1.8
                                show screen parallax1280("daimyo apologize 1") with dissolve
                                call showscrollingimage() from _call_showscrollingimage_41
                                hint"B-but my towel... It's slowly c-coming undone!"
                                call hidescrollingimage from _call_hidescrollingimage_43
                                scene daimyo apo1 with dissolve:
                                    zoom 1.1 xalign 0.5 yalign 1.0
                                da"For a cunning Kunoichi, it sure took you a while to familiarize yourself with the concept of an apology..."
                                da"Make your way a little closer to me, would you my Lady?"
                                scene daimyo apologize 2_1 with dissolve
                                hint"..."
                                scene daimyo apo2 with dissolve
                                da"I am an old man you see... My eyesight escapes me by the day."
                                scene daimyo apo2_1 with dissolve
                                "[hin_name] hesitantly crawled a tiny distance closer to the Daimyo..."
                                da"Which is why I wear my custom made sunglasses..."
                                da"Through these lenses, I can still appreciate the world and all it's... beauty!"
                                da"Even if all I can see are faint shadows..."
                                if ch1_dy_200paid == True:
                                    da"Given that you have at least been vigilant with your debt to me, I shall accept your apology as is, my Lady..."
                                    da"You may rise..."
                                    scene daimyo apo3 with dissolve
                                    da"But a word of warning if I may..."
                                    scene black with dissolve
                                    show daimyo 3
                                    show thina bow2 at right:
                                        zoom 1.1 xpos 1.15
                                    with dissolve
                                    
                                    da"Do not mistake my benevolence for weakness! Next time you disrespect me, I will have you pay a hefty price. Am I making myself clear?"
                                    show thina shy with dissolve
                                    hin"Y-yes, your highness..."
                                    da"Very well!"

                                    jump completeapology
                                scene daimyo apo3 with dissolve
                                "As much as [hin_name] hated the situation she brought upon her self, there was naught she could do. Lest she found herself imprisoned..."
                                "'Disobeying the Daimyo at this moment would be much more foolish than simply obeying his overzealous demands'. Is what [hin_name] would tell herself to rationalize her actions..."
                                scene black with dissolve
                                da"*Slouching Groans*"
                                "The Daimyo stood up, his audible groans would alert [hin_name] of his movement..."
                                show screen parallax1280("daimyo apologize final2", 1.25) with dissolve
                                call showscrollingimage() from _call_showscrollingimage_42
                                "[hin_name] kept her head low, intentionally avoiding the Daimyo's gaze, knowing that he could claim it a sign of disrespect..."
                                "But in her realization of the Daimyo's sudden movement, she quickly reached for her loosely hanging towel in an attempt to cover her almost fully exposed erogenous zones..."
                                hint"W-what's he doing, why is he standing up!"
                                hint"And this towel... It's about to give up on me, not to mention my knees scraping against the hard wood! I am getting tired... and s-sweaty!"
                                hint"What shall I do!?"
                                da"Do you believe your apology to be satisfactory, my Lady...?"
                                hin"I... b-believe so."
                                da"You... believe so?"
                                scene black with dissolve
                                call hidescrollingimage from _call_hidescrollingimage_44
                                scene daimyo apologize stomp1 with vpunch:
                                    zoom 1.25 xalign 0.5 yalign 0.0
                                $ renpy.sound.play("/audio/soun_fx/intro/gruntwoman1.opus", channel="sfx3", loop=False, relative_volume = 1.0)
                                show daimyo:
                                    easein 2 yalign 1.0
                                pause 1.8
                                show screen parallax1280("daimyo apologize stomp1", 1.25) with dissolve
                                call showscrollingimage() from _call_showscrollingimage_43
                                da"Then allow my... hand — To instruct you on how to properly apologize!"
                                hin"*Grunts*"
                                
                                scene black
                                call hidescrollingimage from _call_hidescrollingimage_45
                                scene daimyo apologize stomp1_1 with vpunch:
                                    zoom 1.25 xalign 0.5 yalign 0.8
                                $ renpy.sound.play("/audio/soun_fx/intro/gruntwoman2.opus", channel="sfx3", loop=False, relative_volume = 1.0)
                                
                                da"This is called a dogeza. It's when one's face meets the floor to express their remorse, and the only way I accept apologies from peasants..."
                                show screen parallax1280("daimyo apologize stomp1_1", 1.25) with dissolve
                                call showscrollingimage() from _call_showscrollingimage_44
                                scene black
                                call hidescrollingimage() from _call_hidescrollingimage_46
                                scene daimyo apologize stomp2 with vpunch:
                                    zoom 1.25 xalign 0.5 yalign 0.0
                                show screen parallax1280("daimyo apologize stomp2", 1.25) with dissolve
                                call showscrollingimage() from _call_showscrollingimage_45
                                da"You will keep your head as low as my hand holds it for the rest of our audience..."
                                da"This is the only way I will accept your contrition and the only way I'll consider my sharing of information regarding your husband and what the future holds..."
                                da"I will consider your silence an affirmation of your compliance..."
                                hin"..."
                                hint"Such a heinous man!"
                                hint"But I have to endure this maltreatment, for [na_name]'s sake!"
                                da"Excellent!"
                                da"Before we continue..."
                                da"A dogeza apology isn't complete without the subject's complete prostration..."
                                da"I'll remove my foot- A-ahem! *Cough*! My hand from your head, but remember our agreement..." with vpunch                                
                                da"Your torso remains glued to the floor, or your apology will be discarded!"
                                hint"B-bastard!" with vpunch
                                
                                scene black
                                call hidescrollingimage from _call_hidescrollingimage_47
                                
                                "The Daimyo releases [hin_name] from his grasp and returns to his throne..."
                                show screen parallax1280("daimyo apologize 3") with dissolve
                                call showscrollingimage() from _call_showscrollingimage_46
                                hint"T-the towel..."
                                hint"I'm a-afraid of even making a move to readjust it."
                                hint"T-this man is deranged. I can feel an ominous aura in his every word..."
                                hint"I h-have to be careful..."
                                da"Your hands my lady..."
                                hint"M-my hands...?"
                                da"One's hands must be extended above one's head for a dogeza apology to be complete..."
                                show screen parallax1280("daimyo apologize 4") with dissolve
                                call showscrollingimage() from _call_showscrollingimage_47
                                hin"..."
                                da"Now that's proper form, my Lady! Bravo!"
                                da"Bravo! You've earned yourself an explanation..."
                                da"But please do keep your form intact as per our agreement, or else..."
                                hint"H-how much longer do I have to endure this h-humiliative ritual of his..."
                                hint"My knees hurt and my back aches, but..."
                                hint"If he is to share what he knows of [na_name]... Then I will persevere!"
                                call hidescrollingimage from _call_hidescrollingimage_48
                                show daimyo apo4 with dissolve
                                pause 1
                                da"Now before I proceed to explain a few things to you, it's very important for you to understand mine, yours, and your husband's role in all of this..."
                                da"Given how you've proven yourself to be uuh, not as intelligent as I've heard you were, I'll keep things exceptionally simple! A favor if you will, just for you my Lady..."
                                show daimyoapologize 4t with dissolve:
                                    zoom 0.71 xalign 0.0 yalign 1.0
                                hint"So demeaning... Who does he think he is to insult my intelligence!"
                                da"I, the Daimyo, I am a ruler..."
                                da"You and your husband my Lady, along with everybody else in this godforsaken nation are but simple cattle for me to shepherd into a brighter future..."
                                show daimyoapologize at smallshake
                                hint"C-cattle? He cannot be serious! ...Is that how you thinks of his Nation's people?"
                                da"But you see... a ruler is only as powerful as the loyalty of their subjects is."
                                da"At this very moment, my Lady..."
                                scene daimyo apo4_1 with dissolve:
                                    zoom 1.2 xalign 0.5 yalign 0.7
                                da"I find your own subjection to me quite pleasing! Your husband's on the other hand..."
                                scene daimyo apo4_1 with dissolve
                                da"Is disappointing, to say the least..."
                                show daimyoapologize 4t:
                                    zoom 0.71 xalign 0.0 yalign 1.0
                                hint"W-what!? How?" with vpunch
                                da"For years now I have suffered through my efforts of upholding this fragile state of peace you all get to bask in..."
                                da"At the expense of who! I ask you my Lady..." with vpunch
                                hint"[na_name]'s the one doing everything he can to uphold peace, not you!"
                                da"At the expense of me, of course!" with vpunch
                                da"My gold coffers are running dry trying to sustain a weakened Nation!"
                                da"And as if that were not enough, enemy nations are smelling blood in the water! They are banging on my doors seeking economic and territorial appeasement deals..."
                                da"They think I am theirs to play like a damn fiddle!"
                                da"*Groans* We've become the laughing stock of the entire Shinobi World, and one man's responsible for it..."
                                da"Do you know who's fault is that, my Lady...?"
                                hint"He cannot possibly mean..."
                                da"YOUR FUCKING MORON HUSBAND'S!" with vpunch
                                hint"N-no..."
                                da"Imagine my surprise when I heard that the Hokage, supposedly the beacon of peace, got caught up in a political altercation with an opposing nation..."
                                da"Rumor has it your husband was plotting behind my back... behind everyone's backs, potentially attempting to incite war!"
                                scene daimyo apo2_1 with dissolve
                                hin"N-no! That cannot be true! [na_name] would never do t-" with vpunch
                                $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp2.opus", channel="sfx3", loop=False, relative_volume = 1.0)
                                da"SHUT IT! You uncivilized bitch!" with vpunch
                                scene daimyo apo4_1 with dissolve
                                da"Head down or I swear  I'll be the one to personally drag you and shackle you in my dungeons!" with vpunch
                                "[hin_name] had yet to realize the Daimyo was getting 'excited' while playing his disingenuous mind games with her..."
                                hint"W-what on earth is going on! The Daimyo has to be plotting something himself, there's no other reasonable explanation!"
                                da"I suppose I can understand your emotional outburst, given your strong bond with your husband..."
                                da"I shall excuse you for just this one time and one time only."
                                da"Besides my Lady... you shouldn't worry so much, should you? The Hokage is a strong man after all."
                                da"From what I have been informed, he isn't dead... yet. *Chuckles*"
                                da"He is simply being momentarily detained until all necessary investigations are conducted..."
                                da"Until then, it's best we all stay calm..."
                                da"But you see, I can't have the Hokage drag my name, or my Nation's reputation through mud and smear it with his shit!"
                                da"One day he preaches peace, the next he incites political and civil unrest!"
                                da"If that simpleton has no idea how to navigate this savage world, then I shall take matters into my own hands..."
                                da"You see..."
                                da"To a smarter man such as myself, it is as clear as day that idealistic peace was a fool's errand from the very beginning."
                                da"Peace was a curse of our own infliction! Slowly draining the life out of men with ambition, men with vision!"
                                da"While peasants such as yourself parade it around, happy with your little scraps handed to you, content with your meager lots..."
                                da"Those with influence like myself are left to deal with its consequences and pay the cost of it!"
                                da"My armies grow restless, My cattle fat and lazy! I mean, look at you... Senile and disrespectful on every count."
                                da"What good is my influence if I cannot exercise it to grow my wealth. What good are my armies if there are no borders to push, no battles to be fought!"
                                da"And what good is a ruler with subjects as useless as you and your husband turned out to be... *Groans*"
                                da"Peace is clearly a plague, and I will be its cure!"
                                da"Our nation shall ready itself for war once again! It's time we reclaim what is rightfully ours..."
                                da"I won't stand for complacency any longer. I won't allow opposing nations to step all over us. There will be no more appeasement, no more diplomacy and treaties!"
                                da"The world shall be set aflame once again... and when it does, I shall be there to reap the benefits! For war is what stirs the markets, war is what creates need..."
                                da"And where there's need, there's money to be made and influence to be had!"
                                da"Heee-heee-heeee..."
                                da"I am sure you tire of my monologue, my Lady..."
                                da"I shall leave you with this..."
                                da"War is an expensive undertaking. If I am to prepare for it, taxing my subjects is the only reasonable approach..."
                                da"Seeing how peace was an expenditure for me, and a blessing for you..."
                                da"I think it only fair that our roles shall now be reversed!"
                                da"I believe I've said enough for even you to understand why taxes must be paid in full, by all..."
                                da"Next time you fail to comply with my newfound policies, I shall consider it an act of treason. Your punishment will of course be proportionate to the severity of your crime..."
                                da"And if you are looking for someone to blame for what has befallen us all, look no further than the 'man' you call your husband..."
                                da"GUARDS!" with vpunch
                                scene black with dissolve
                                da"Sweep this filth from my floors and toss it out of my palace!"
                                $ renpy.sound.play("/audio/soun_fx/doorclose.opus", channel="sfx3", loop=False, relative_volume = 1.0)
                                
                                "Guards" "At once, your highness!"
                                hint"N-no! I am still indecent!"
                                show daimyo dm1 with dissolve
                                "The two men entered the room before [hin_name] could gather herself up and get on her feet..."
                                show daimyo apologize final1 with dissolve
                                pause 1
                                "[hin_name] hasitently looked up to the Daimyo trying to measure whether she should break her bow and fix her towel now that her audience with the Daimyo was seemingly called off."
                                "She was clearly emotionally charged, a few tears escaped her as she tried her best to muster the courage needed to maintain some dignity..."
                                "The Daimyo appeared indefferent to her situation..."
                                menu:
                                    "The Daimyo appeared indefferent to her situation..."
                                    "{color=[obediencecolor]}Keep bowing...{/color}":
                                        default keepboying = False
                                        $ keepboying = True
                                        hint"I-I I don't know w-what to do! But I can't risk angering him any f-further..."
                                        show daimyo apologize 4 with dissolve
                                        "[hin_name] kept bowing in fear of further angering the Daimyo..."
                                        "The two familiar men entered the room..."
                                        
                                        show screen parallax1280("daimyo apologize 4") with dissolve
                                        call showscrollingimage() from _call_showscrollingimage_48
                                        "They would find [hin_name] in complete prostration, both of her holes clearly visible to whoever happened to be behind her..."
                                        "The two men silently whispered to each other..."
                                        to"Ohoo-hoo! Are you seeing what I am seeing Koji?"
                                        ko"Indeed I am, Toji..."
                                        to"This bitch is begging to be ravaged! Just look at her... Can you Imagine stuffing both of those holes with our cocks?"
                                        call hidescrollingimage from _call_hidescrollingimage_49
                                        show daimyo dm2 with dissolve
                                        show daimyo dm3 with Dissolve(1):
                                            zoom 1.2 xalign 1.0 yalign 1.0
                                        show daimyoapologize 4t with dissolve:
                                            zoom 0.71 xalign 0.0 yalign 1.0
                                        to"I don't know much longer I can go without tearing this whore's clothes apart and impaling her with my cock."
                                        to"I sure hope the Daimyo's plan works out..."
                                        "[hin_name] couldn't quite make out the men's whispers, but she knew she was the subject of them..."
                                        hint"I can h-hear those two whispering b-behind me..."
                                        call changeObedience("Hinata", 1) from _call_changeObedience_75
                                        hint"To think that even those b-bastards get to see me like this..."
                                        hint"D-darn it! This is so d-degrading..."
                                        scene daimyo apologize 4 with dissolve:
                                            yalign 0.0
                                        da"How much longer do you plan on cleaning my floors with your body, you simpleton!"
                                        scene black
                                        show daimyo apologize final2
                                        with dissolve
                                        da"You may rise!" with vpunch
                                        "[hin_name] quickly reached for her towel and covered herself up..."
                                        scene daimyo apologize 2_1 with dissolve              
                                        hint"I'll g-get back at them... I won't s-stand for such treatment, not for myself... not for anyone else!"
                                        scene daimyo dm3 with dissolve
                                        to"*Tsk* Show's over..."
                                        da"Toji, Koji!" with vpunch
                                        scene daimyo dm3 with dissolve
                                        show daimyo with dissolve:
                                            zoom 1.2 xalign 1.0 yalign 1.0
                                        pause 1
                                        da"Contain your... excitement."
                                        da"Remember! We only act as soon as we receive word..."
                                        scene black with vpunch
                                        dm"HAI!"
                                        scene daimyo apo3 with dissolve
                                        scene daimyo 2
                                        show thina b1 at right:
                                            zoom 1.1
                                        with Dissolve(1)
                                        da"Excellent... Hee-hee-heeeee!"
                                        "[hin_name] still emotionally charged, and concerned about her indescent exposure to the three men, had yet to piece together the meaning of their exchanged words..."
                                        show thina annoyed with dissolve
                                        "What did not elude her, was the Daimyo's obvious excitement..."
                                        hint"What a t-truly deplorable man... I bet he's g-getting excited simply thinking about ways to extend his influence..."
                                        show thina at smallshake
                                        hint"D-disgusting..."
                                        da"Something's telling me this won't be our last encounter..."
                                        da"Although, that's entirely in your own hands.. Don't forget your debts, my Lady!"
                                        scene black with dissolve
                                        da"Heee-heee-heee..."
                                        $ renpy.sound.play("/audio/soun_fx/doorclose.opus", channel="sfx3", loop=False, relative_volume = 1.0)
                                        "The two men escorted [hin_name] outside the Daimyo's chambers..."
                                        jump daimyoending







                                    "Cover yourself":
                                        show daimyo apologize final2:
                                            zoom 1.23 yalign 0.0
                                        with dissolve
                                        hin"I can't let anyone else see me like this!"
                                        show daimyo apologize final2 with dissolve:
                                            zoom 1.23 yalign 1.0
                                        "[hin_name] quickly reached for her towel and covered herself up..."
                                        scene daimyo apologize 2_1 with dissolve              
                                        hint"I'll g-get back to him somehow... I won't s-stand for such treatment, not for myself... not for anyone else!"
                                        scene black with dissolve
                                        "[hin_name] rised to her feet, only to realize..."
                                        scene daimyo 2 with dissolve
                                        da"Hee-hee-hee..."
                                        da"There's some fight left in you, isn't there..."
                                        show thina shy2 at right with dissolve:
                                            zoom 1.05
                                        show thina at smallshake
                                        $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp2.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                                        hint"*Gasp*"
                                        hint"Is that...!?"
                                        "[hin_name] would now realize that the Daimyo found some deranged satisfaction from her ordeal..."

                                        scene daimyo dm2 with dissolve
                                        to"Ohoo-hoo! Are you seeing what I am seeing Koji?"
                                        show hinata btowel2_bg with dissolve:
                                            zoom 0.71 xalign 0.0 yalign 1.0
                                        ko"Indeed I am, Toji..."
                                        to"This bitch is begging to be ravaged! Just look at her... Can you Imagine stuffing that juicy ass of hers with our cocks?"
                                        show daimyo dm3 with Dissolve(1):
                                            zoom 1.2 xalign 1.0 yalign 1.0
                                 
                                        to"I don't know much longer I can go without tearing this whore's clothes apart and impaling her with my cock."
                                        to"I sure hope the Daimyo's plan works out..."
                                        show hinata btowel2_bg2 with dissolve:
                                            zoom 0.71 xalign 0.0 yalign 1.0
                                        "[hin_name] quickly covered herself up as best she could..."
                                        "She couldn't quite make out the men's whispers, but she knew she was the subject of them..."
                                        hint"I can h-hear those two whispering b-behind me..."


                                        da"Toji, Koji!" with vpunch
                                        scene daimyo dm3 with dissolve
                                        show daimyo with dissolve:
                                            zoom 1.2 xalign 1.0 yalign 1.0
                                        pause 1
                                        da"Contain your... excitement."
                                        da"Remember! We only act as soon as we receive word..."
                                        scene black with vpunch
                                        dm"Hai!"
                                        scene daimyo 2
                                        show thina b1 at right:
                                            zoom 1.1
                                        with Dissolve(1)
                                        da"Excellent... Hee-hee-heeeee!"
                                        "[hin_name] still emotionally charged, and concerned about her indescent exposure to the three men, had yet to piece together the meaning of their exchanged words..."
                                        show thina annoyed with dissolve
                                        "What did not elude her, was the Daimyo's obvious excitement..."
                                        hint"What a t-truly deplorable man... I bet he's g-getting excited simply thinking about ways to extend his influence..."
                                        show thina at smallshake
                                        hint"D-disgusting..."
                                        da"Something's telling me this won't be our last encounter..."
                                        da"Although, that's entirely in your own hands.. Don't forget your debts, my Lady!"
                                        scene black with dissolve
                                        da"Heee-heee-heee..."
                                        $ renpy.sound.play("/audio/soun_fx/doorclose.opus", channel="sfx3", loop=False, relative_volume = 1.0)
                                        "The two men escorted [hin_name] outside the Daimyo's chambers..."
                                        jump daimyoending
                        



                            "Stay silent...":
                                hint"I have no idea what he expects me to do..."
                                hin"..."
                                da"Hmmm? Would you rather I pick your apology for you, my Lady?"
                                show thina shy with dissolve
                                hin"N-no..."
                                da"Then think of something appropriate!" with vpunch
                                jump daimyoapologize
                            



                
                else:
                    da"All in due time, my lady..."
                    da"First, I believe you owe me an apology..."
                    hint"Is he referring to the debt obligations? Should I apologize?"
                    menu:
                        hint"Is he referring to the debt obligations? Should I apologize?"
                        "Apologize":
                            show thina annoyed with dissolve
                            hin"I apologize, my Lord..."
                            da"Heee-heee-hee... You think simple words can absolve you of your transgressions?"
                            da"Surely you can think of something more..."
                            hint"I don't know what he expects from me..."
                            hint"Maybe..."
                            show thina bow1 with dissolve:
                                xzoom -1
                            hint"This will satisfy him?"
                            hin"My sincerest apologies, your highness!"
                            da"A fine bow, my Lady!"
                            da"But surely you can go a little lower than that, can't you?"
                            menu:
                                da"But surely you can go a little lower than that, can't you?"
                                "Take a deeper bow":
                                    pass
                                # "Stand your ground":
                                #     hin"There will be no need for that. Have I not stayed true to my obligations, my lord?"
                                #     da"*Groans*"
                                #     da"I suppose you have..."
                                #     da"Let us move on to more pressing matters then, shall we?"
                                
                            hint"I suppose a low bow isn't the worst he could ask for..."
                            show thina bow2 with dissolve
                            hin"Y-you are right, my lord..."
                            da"Indeed I am! For a deeper bow tells of deeper respect!"
                            da"Go on then, my Lady! Show me..."
                            da"Is this a bow of respect? A bow fitting of the apology you owe to me?"
                            hint"D-Damn him!"
                            show thina bow3 with Dissolve(1)
                            pause 1.5
                            hin"It was not. My apologies your highness..."
                            hin"Is this more to your satisfaction?"
                            show daimyo 4 with fade
                            da"Heee-heee-heee..."
                            show daimyo 4_1 with dissolve
                            da"Indeed it is... to my satisfaction!"
                            da"You may rise, my lady. You apology has been accepted!"
                            show thina bow1 with dissolve
                            hin"..."
                            "[hin_name] had yet to realize the Daimyo's excitement..."
                            da"Good, good. Now..."
                            da"Let us move on to more pressing matters then, shall we?"
                            jump completeapology
            
                        "I have nothing to apologize for!":
                            show thina annoyed with dissolve
                            hin"I have nothing to apologize for, not after the mistreatment I've endured at the hands of your men!"
                            da"Mis...treatment?"
                            da"You should be counting your blessings! You filth!" with vpunch
                            show thina shy with dissolve
                            hin"*Gasp"
                            da"Have you not failed to meet your obligation to me?" with vpunch

                            jump faildaimyoapology
                            

            else:  #if paid debt
                da"Yes indeed, precarious matters that might even involve your husband!"
                hin"[na_name]!? W-what do you know of him... answer me please!"
                if daimyomeeting_counter >= 3:
                    jump daimyo_cruelapology
                
                else:
                    da"Hee-heee!"
                    da"All in due time my lady..."
                    jump completeapology


    label completeapology:
        show thina angry with dissolve:
            xzoom 1
        da"Now before I proceed to explain a few things to you, it's very important for you to understand mine, yours, and your husband's role in all of this..."
        da"Given how you've proven yourself to be fairly competent, I'll let you in on a few secrets! A favor if you will, just for you my Lady..."
        hint"S-secrets?"
        da"I, the Daimyo, I am a ruler..."
        da"You and your husband my Lady, along with everybody else in this godforsaken nation are but simple cattle for me to shepherd into a brighter future..."
        show thina annoyed with dissolve
        hint"C-cattle? He cannot be serious! ...Is that how you thinks of his Nation's people?"
        da"But you see... a ruler is only as powerful as the loyalty of their subjects is."
        da"At this very moment, my Lady..."
        da"I find your own loyalty to me quite pleasing!"
        scene black with dissolve
        da"Your husband's on the other hand..."
        show na_prison1 with flash:
            alpha 0.38 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.05)*SaturationMatrix(1.03)*BrightnessMatrix(0.01)*HueMatrix(0.0) 
        show na_prison1:
            easein 3 zoom 0.8 alpha 0.0 xalign 0.5
        pause 1


        show daimyo 3_1 with Dissolve(1)
        da"Is disappointing, to say the least..."
        show thina thinking with dissolve:
            zoom 1.1 xpos 650 ypos -60
        hint"W-what!? How?" with vpunch
        da"For years now I have suffered through my efforts of upholding this fragile state of peace you all get to bask in..."
        da"At the expense of who! I ask you my Lady..." with vpunch
        hin"I..."
        da"At the expense of me, of course!" with vpunch
        show thina annoyed with dissolve
        hint"[na_name]'s the one doing everything he can to uphold peace, not you!"
        da"My gold coffers are running dry trying to sustain a weakened Nation!"
        da"And as if that were not enough, enemy nations are smelling blood in the water! They are banging on my doors seeking economic and territorial appeasement deals..."
        da"They think I am theirs to play like a damn fiddle!"
        da"*Groans* We've become the laughing stock of the entire Shinobi World, and one man's responsible for it..."
        da"Do you know who's fault is that, my Lady...?"
        show thina angry with dissolve
        hint"He cannot possibly mean..."
        da"YOUR FUCKING MORON HUSBAND'S!" with vpunch
        show thina annoyed with dissolve
        hint"N-no..."
        da"Imagine my surprise when I heard that the Hokage, supposedly the beacon of peace, got caught up in a political altercation with an opposing nation..."
        da"Rumor has it your husband was plotting behind my back... behind everyone's backs, potentially attempting to incite war!"
        show thina angry with dissolve
        hin"N-no! That cannot be true! [na_name] would never do that!" with vpunch
        da"My Lady..."
        da"Are you by chance implying that I am lying?"
        show thina shy with dissolve
        hin"N-no! It's just..."
        # $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp2.opus", channel="sfx3", loop=False, relative_volume = 1.0)
        # da"SHUT IT! You uncivilized bitch!" with vpunch
        # scene daimyo apo4_1 with dissolve
        # da"Head down or I swear  I'll be the one to personally drag you and shackle you in my dungeons!" with vpunch
        # "[hin_name] had yet to realize the Daimyo was getting 'excited' while playing his disingenuous mind games with her..."
        # hint"W-what on earth is going on! The Daimyo has to be plotting something himself, there's no other reasonable explanation!"
        # da"I suppose I can understand your emotional outburst, given your strong bond with your husband..."
        # da"I shall excuse you for just this one time and one time only."
        da"Hmph! *Groans*" with vpunch
        da"Besides my Lady... you shouldn't worry so much, should you? The Hokage is a strong man after all."
        da"From what I have been informed, he isn't dead... yet. *Chuckles*"
        scene black with dissolve
        da"He is simply being..."
        show na_prison2 with flash:
            alpha 0.38 additive 0.0 blur 0.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.05)*SaturationMatrix(1.03)*BrightnessMatrix(0.01)*HueMatrix(0.0) 
        show na_prison2:
            easein 4 zoom 0.8 alpha 0.0 xalign 0.5
        da"Momentarily detained until all necessary investigations are conducted..."
        da"Until then, it's best we all stay calm..."
        show daimyo 3 with Dissolve(1)
        da"But you see, I can't have the Hokage drag my name, or my Nation's reputation through mud and smear it with his shit!"
        da"One day he preaches peace, the next he incites political and civil unrest!"
        da"If that simpleton has no idea how to navigate this savage world, then I shall take matters into my own hands..."
        da"You see..."
        da"To a smarter man such as myself, it is as clear as day that idealistic peace was a fool's errand from the very beginning."
        da"Peace was a curse of our own infliction! Slowly draining the life out of men with ambition, men with vision!"
        da"While peasants such as yourself parade it around, happy with your little scraps handed to you, content with your meager lots..."
        da"Those with influence like myself are left to deal with its consequences and pay the cost of it!"
        da"My armies grow restless, My cattle fat and lazy! I mean, look at you... Senile and disrespectful on every count."
        da"What good is my influence if I cannot exercise it to grow my wealth. What good are my armies if there are no borders to push, no battles to be fought!"
        da"And what good is a ruler with subjects as useless as your husband turned out to be... *Groans*"
        da"Peace is clearly a plague, and I will be its cure!"
        show daimyo 4 with dissolve
        da"Our nation shall ready itself for war once again! It's time we reclaim what is rightfully ours..."
        da"I won't stand for complacency any longer. I won't allow opposing nations to step all over us. There will be no more appeasement, no more diplomacy and treaties!"
        da"The world shall be set aflame once again... and when it does, I shall be there to reap the benefits! For war is what stirs the markets, war is what creates need..."
        scene daimyo 1 with dissolve
        da"And where there's need, there's money to be made and influence to be had!"
        da"Heee-heee-heeee..."
        show thina annoyed with dissolve:
            zoom 1.1 xpos 650 ypos -60
        hint"Despicable..." with vpunch
        da"I am sure you tire of my monologue, my Lady..."
        da"I shall leave you with this..."
        da"War is an expensive undertaking. If I am to prepare for it, taxing my subjects is the only reasonable approach..."
        da"Seeing how peace was an expenditure for me, and a blessing for you..."
        da"I think it only fair that our roles shall now be reversed!"
        da"I believe I've said enough for even you to understand why taxes must be paid in full, by all..."
        show daimyo 2 with dissolve
        da"Know that if you fail to comply with my newfound policies, I shall consider it an act of treason. Your punishment will of course be proportionate to the severity of your crime..."
        show thina shy2 with dissolve
        hint"W-what the heck is w-wrong with him!"
        show thina annoyed with dissolve
        hint"W-why is his..."
        da"And if you are looking for someone to blame for what has befallen us all, look no further than the 'man' you call your husband..."
        da"GUARDS!" with vpunch
        scene black with dissolve
        da"Escort this peasant outside of my palace!"
        $ renpy.sound.play("/audio/soun_fx/doorclose.opus", channel="sfx3", loop=False, relative_volume = 1.0)
        
        "Guards" "At once, your highness!"
        show daimyo dm1 with dissolve
        "The two familiar men entered the room to escort [hin_name] outside the Daimyo's chambers..."
        show hinata btowel2_bg2 with dissolve:
            zoom 0.71 xalign 0.0 yalign 1.0
        to"I don't know much longer I can go without tearing this whore's clothes apart and impaling her with my cock."
        to"I sure hope the Daimyo's plan works out..."
        show daimyo dm3 with Dissolve(1):
            zoom 1.2 xalign 1.0 yalign 1.0
    
        hint"I can h-hear those two whispering b-behind me..."


        da"Toji, Koji!" with vpunch
        scene daimyo dm3 with dissolve
        pause 0.5
        da"Contain your... excitement."
        da"Remember! We only act as soon as we receive word..."
        scene black with vpunch
        dm"Hai!"
        show thina thinking with dissolve
        hint"[na_name]..."
        show thina angry with dissolve
        hint"They must be plotting something, I must find out what..."
        
        hide thina with dissolve

    label daimyoending:
        scene palace2                
        show demandingmen normal badguys2:
            xzoom -1 zoom 1.09 ypos -10 xpos -565
        show thina annoyed at right:
            zoom 1.03
        with dissolve
        if keepboying == True:
            to"That was a nice display of your... assets, you put on out there!"
            hin"D-don't talk to me!"
            to"You can keep riding your high horse for a little while longer, little Lady of the leaf..."
            to"But soon enough... *Chuckles*"

        else:
            to"I hope you enjoyed your audience with his highness, my Lady..."
            to"We'd love to see you pay another visit to him... and us, in the coming days!"
            to"Especially when you are dressed, or rather... undressed like this! *Chuckles*..."

        show rangi angry:
            zoom 0.58 xpos 2000
        show rangi angry:
            easein 1 xalign 0.7
        pause 0.5
        show demandingmen:
            easein 0.3 xpos -620
        mada"Leave her be, I'll handle things from here." with vpunch
        to"As you wish..."
        show demandingmen:
            easeout 1.3 xpos -1700
        to"{size=*0.7}Fucking orange haired bitch...{/size}"
        scene black with dissolve
        scene palace2
        show thina shy at right
        show rangibu at left:
            zoom 0.58 xzoom -1
        with dissolve
        hin"D-did you wait for me outside all this time?"
        hide rangibu
        show rangi normal at left:
            zoom 0.58 xzoom -1
        with dissolve
        mada"I did what I had to. Let's get you dressed up, shall we?"
        show thina thinking with dissolve
        hin"I was wrong to be skeptical about you, Madame..."
        hin"T-thank you, for everything..."
        scene black with dissolve
        mada"Follow me, Lady [hin_name]..."
        "The Madame brought [hin_name] back to the onsen area where she made sure to have freshly washed clothes ready for her to wear..."

        scene bg onsen1 with dissolve
        show shina concerned at left with dissolve
        show rangi normal at right with dissolve:
            zoom 0.58
        "[hin_name] would share as much as she was comfrotable about her encounter with the Daimyo to the Madame..."
        scene bg onsen1
        show shina concerned at left
        show rangi normal2 at right:
            zoom 0.58
        with fade
        mada"His highness prepares for war... huh?"
        hide rangi
        show rangi angry at right:
            zoom 0.58
        with dissolve
        mada"That much I already suspected, but had no direct confirmation of up until now..."
        mada"But war with who? More importantly... why?"
        hin"I have no idea. All he went on about is how this peaceful period is costing him money and influence..."
        hin"Are those really reasons for a ruler to condemn his nation to the atrocities of war?"
        hin"Is this the kind of man you trust enough to sleep with? To raise three daughters with?"
        mada"He even spoke to you of our children, huh?"
        mada"My Lady... some things I have control over, others I do not..."
        hin"Madame..."
        mada"Let's leave it at that. Please..."
        hin"..."
        show rangi normal at right with dissolve:
            zoom 0.58
        mada"What about you, Lady [hin_name]..."
        hin"W-what about me..."
        mada"How did the Daimyo treat you, did you follow my advice?"

        if daimyomeeting_counter >= 3:
            hin"Oh,I tried. But... I think I've angered him with how I answered some of his questions."
            hin"He had me get on my knees and apologize. It seemed like he wanted me to feel as if I am beneath him. It was... degrading!"
            mada"*Sigh* I am sorry, my Lady. The Daimyo can be... overbearing."
            mada"But he didn't overstep his boundaries... did he?"
            hin"N-no... Although, it was clear he found some enjoyment in m-my humiliation..."
            hin"I can see what you meant when you said he'd play his stupid little games. He said the meanest things while putting up a pretentious act of courtesy..."
            mada"Sounds exactly like him..."
            mada"You should be careful, my Lady. I hope that you won't ever have the misfortune of meeting him again..."
            mada"And if you do, do your best to comply and cater to his reasonable demands. Remember, only antagonize him if he clearly oversteps!"

            
        else:
            hin"I tried. I think it went okay..."
            hin"Although the Daimyo did go on to insult my husband and try to blame him for his own shortcomings..."
            mada"Sounds exactly like him..."
            mada"You should be careful, my Lady. I hope that you won't ever have the misfortune of meeting him again..."
            mada"And if you do, do your best to comply and cater to his reasonable demands. Remember, only antagonize him if he clearly oversteps!"
        mada"You saw how he acts, spontaneous and overzealous. He'll be quick to act in any way he sees fit when there's no one around to keep him in check..."
        mada"You don't want to anger a man like that, especially given his status as the Daimyo of our nation..."
        hin"I understand..."
        mada"I am sure you have a lot to think about, as do I..."
        mada"Shall I escort you outside the premises my Lady?"
        hin"If it's of no bother to you..."
        scene black with dissolve
        mada"But of course. Follow me..."
        "The Madame accompanied [hin_name] throughout the Daimyo's lands, making sure no one would disturb her peace..."
        scene palace
        show shina concerned at left with dissolve
        show rangi normal at right with dissolve:
            zoom 0.58
        mada"Will you be okay by yourself from here on out, Lady [hin_name]?"
        hin"Of course. Thank you for everything, Madame..."
        mada"Don't even think about it."
        mada"I hope you won't find your way around these places again, but if you do..."
        mada"Do pay me a visit, alright?"
        show shina shy with dissolve
        hin"Will do! Will you be okay... Madame?"
        mada"*Giggles* Look at us..."
        mada"Like two old grandmas exchanging their farewells!"
        mada"I told you, didn't I? I'll find my way around my own troubles. Especially now that I have a friend like you to look up to..."
        mada"Let's both draw courage from each other and do our best to forge our own paths."
        show shina smiling with dissolve
        hin"You got it! Stay well, Madame..."
        scene black with dissolve
        mada"You too, [hin_name]..."
        "[hin_name] makes her way back home..."
        $ renpy.end_replay()
        scene bg porch with dissolve
        show shina shy at right with dissolve
        $ playmusic("audio/ost/house2.opus",0.6)
        hint"[bo_name] must be worried sick..."
        show shina:
            easeout 2 xpos -1500
        hint"..."
        $ renpy.sound.play("/audio/soun_fx/dooropen.opus", channel="sfx3", loop=False, relative_volume = 0.6)
        scene bg lr_day with dissolve:
            zoom 0.68
        show shina shy at right with dissolve
        scene bg bb day
        show boruto surprised2 at center with dissolve
        bot"Must be [hin_rel]!"
        if ch1_d7_hatredpath == True:
            call borutoevil2 from _call_borutoevil2_17
            call changeHatred(1) from _call_changeHatred_96
            show boruto smirk2 with dissolve
            bot"I wonder if my plan worked!"
        if ch1_dy_200paid == True:
            bot"Hopefully nothing bad came of this..."
        scene black with dissolve
        bot"Time to find out what's going on"
        scene bg lr_day with dissolve:
            zoom 0.68
        show shina shy at left with dissolve
        show boruto surprised2 at right with dissolve
        bo"[hin_rel]! What happened? Are you okay?"
        show boruto angry with dissolve
        bo"Did those men hurt you?"
        show blackscreen with dissolve
        show boruto surprised2
        "[hin_name] recounts her encounter with the Daimyo to you..."
        hide blackscreen with dissolve
        bo"[na_rel] is detained!?" with vpunch
        bo"And the Daimyo is preparing for war? What the FUCK is going on [hin_rel]..."
        show shina serious with dissolve
        hin"Language, [bo_name]!"
        show shina shy2 with dissolve
        hin"Look... I don't know what's going on exactly and I am sure whatever is going on with [na_name] is probably a huge misunderstanding."
        hin"I will ask around and find out what's going on but in the meantime..."
        hin"We best stay vigilant with the Daimyo's demands..."
        bo"[hin_rel]! Are we really going to let the Daimyo extort us of everything we have?"
        hin"We have no other choice [bo_name]..."
        hin"The Daimyo's rule is absolute, you know that..."
        bo"But what are we going to do about the money..."
        show shina shy with dissolve 
        hin"I don't know... yet."
        hin"If you have any ideas do let me know please!"
        show boruto normal with dissolve
        bo"I'll figure something out..."
        hin"Let's talk about it later, I have to get back to work!"
        hide shina with dissolve
        if ch1_d7_hatredpath == True:
            show boruto sceeming with dissolve
            bot"Hehe! My plan is in motion..."

        

    jump action_taken




init python:
    import os
    from collections import defaultdict
    import pickle

    config.searchpath.append(os.path.join(config.savedir, 'captured'))
    
    def get_save_directory():
        captures_dir = os.path.join(renpy.config.savedir, 'captured').replace('\\', '/')
        if not os.path.exists(captures_dir):
            os.makedirs(captures_dir)
        return captures_dir

    def get_display_path(filepath):
        """Convert to relative path for display"""
        if filepath is None:
            return None
        parts = filepath.replace('\\', '/').split('/')
        try:
            if 'captured' in parts:
                idx = parts.index('captured')
                return '/'.join(parts[idx+1:])
        except:
            pass
        return filepath.replace('\\', '/')

    def get_absolute_path(filepath):
        if filepath is None:
            return None
        if os.path.isabs(filepath):
            return filepath.replace('\\', '/')
        return os.path.join(get_save_directory(), filepath).replace('\\', '/')

    def verify_photo_exists(filepath):
        try:
            abs_path = get_absolute_path(filepath)
            return os.path.isfile(abs_path)
        except:
            return False
    
    def cleanup_photo_albums():
        for model_name in list(photo_albums.keys()):
            valid_photos = [photo for photo in photo_albums[model_name] if verify_photo_exists(photo)]
            if valid_photos:
                photo_albums[model_name] = [get_display_path(p) for p in valid_photos]
            else:
                del photo_albums[model_name]

    def load_photo_albums():
        try:
            save_path = os.path.join(renpy.config.savedir, "photo_albums.dat").replace('\\', '/')
            if os.path.exists(save_path):
                with open(save_path, "rb") as f:
                    albums = pickle.load(f)
                    if not isinstance(albums, defaultdict):
                        albums = defaultdict(list, albums)
                    for model in albums:
                        albums[model] = [get_display_path(p) for p in albums[model]]
                    return albums
        except Exception as e:
            renpy.notify(f"Error loading albums: {str(e)}")
        return defaultdict(list)

    def save_photo_albums():
        try:
            cleanup_photo_albums()
            save_path = os.path.join(renpy.config.savedir, "photo_albums.dat").replace('\\', '/')
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            with open(save_path, "wb") as f:
                pickle.dump(photo_albums, f)
        except Exception as e:
            renpy.notify(f"Error saving albums: {str(e)}")

    def take_camera_shot(model_name):
        if model_name is None:
            return
        
        try:
            captures_dir = get_save_directory()
            os.makedirs(captures_dir, exist_ok=True)
            
            model_dir = os.path.join(captures_dir, model_name).replace('\\', '/')
            os.makedirs(model_dir, exist_ok=True)
            
            photo_count = len(photo_albums[model_name])
            filename = f"{model_name}_photo{photo_count + 1}.png"
            
            rel_path = os.path.join(model_name, filename).replace('\\', '/')
            abs_path = os.path.join(model_dir, filename).replace('\\', '/')
            
            renpy.screenshot(abs_path)
            renpy.free_memory()
            
            if verify_photo_exists(rel_path):
                photo_albums[model_name].append(rel_path)
                save_photo_albums()
            else:
                renpy.notify("Failed to save screenshot")
            
        except Exception as e:
            renpy.notify(f"Screenshot error: {str(e)}")

    # Initialize
    photo_albums = load_photo_albums()
    cleanup_photo_albums()


label take_photo_sequence:
    hide screen displayTextScreen
    hide screen camera_ui
    $ quick_menu = False
    with Dissolve(0.2)
    pause 0.2
    if not _in_replay:
        $ take_camera_shot(selected_model)
    $ renpy.sound.play("audio/soun_fx/takephoto.opus", channel="sfx3", loop=False, relative_volume = 0.8)
    with flash
    $ quick_menu = True
    return

screen camera_ui(model_name,showbutton=True):
    add "cameraui" xalign 0.5 yalign 0.5
    if showbutton == True:
        imagebutton:
            xalign 0.1 yalign 0.5
            auto "images/v4/yoruichi/model1/cameraui/camerabutton_%s.png"
            hovered Show("displayTextScreen", displayText = "Snap a picture!")
            unhovered [Hide("displayTextScreen")]
            action [
                SetVariable("selected_model", model_name),
                Call("take_photo_sequence")
            ]
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"

screen camera1280(baseImage, zoom=1, initial_ypos=0.0):
    on "show" action Function(mark_screen_image_gallery, baseImage)
    viewport:
        area (0, 0, 1.5, 1.5)
        edgescroll (300, 550)
        yinitial initial_ypos
        add baseImage subpixel True zoom(zoom) 
        draggable True
style photo_button_text:
    color "#fff"
    hover_color "#0ff"
    size 30

style photo_button:
    padding (20, 10)
    background "#333"
    hover_background "#555"


default persistent.discovered_models = set()


screen photo_album():
    modal True
    zorder 1000
    $ renpy.hide_screen("say")
    
    default current_model = None
    default current_photo_index = 0
    
    add "black"
    
    if current_model is None:
        frame:
            background "#0008"
            margin (50, 50)
            
            viewport:
                draggable True
                mousewheel True
                scrollbars "vertical"
                ysize 700
                
                vbox:
                    spacing 20
                    xalign 0.5
                    yalign 0.5
                    
                    text "Camera Reel" size 40 xalign 0.5 color "#fff"
                    
                    $ model_images = {
                        "Yoruichi": "yorucombat annoyed",
                        "Hinata": "shina concerned",
                        "Himawari": "hima mad", 
                        "Sarada": "sarada angry3t"
                    }
                    
                    $ rows = (len(model_images) + 3) // 4
                    grid 4 rows:
                        spacing 20
                        xalign 0.5
                        
                        for model in model_images.keys():
                            $ photo_count = len(photo_albums.get(model, []))
                            
                            # Add model to discovered set if they have photos
                            if photo_count > 0:
                                $ persistent.discovered_models.add(model)
                                
                            frame:
                                background "#242424"
                                padding (2, 2)
                                margin (5, 5)
                                
                                fixed:
                                    xysize (250, 400)
                                    
                                    # Show model image based on discovery state
                                    if model in persistent.discovered_models:
                                        if photo_count > 0:
                                            imagebutton:
                                                idle Transform(model_images[model], size=(250, 400), alpha=0.8)
                                                hover Transform(model_images[model], size=(250, 402), alpha=1.0)
                                                action [
                                                    SetScreenVariable("current_model", model),
                                                    SetScreenVariable("current_photo_index", 0)
                                                ]
                                                hover_sound "audio/soun_fx/select2.opus"
                                                activate_sound "audio/soun_fx/select4.opus"
                                        else:
                                            add Transform(model_images[model]):
                                                size (250, 400)
                                                alpha 0.2
                                                matrixcolor TintMatrix("#000000")
                                    else:
                                        add Transform(model_images[model]):
                                            size (250, 400)
                                            alpha 0.2
                                            matrixcolor TintMatrix("#000000")
                                    
                                    # Show model name or ???? based on discovery state
                                    text (model if model in persistent.discovered_models else "????"):
                                        xalign 0.5
                                        yalign 0.5
                                        size 24
                                        color "#fff"
                                        outlines [(2, "#000", 0, 0)]
                                    
                                    text f"({photo_count} photos)":
                                        xalign 0.5
                                        yalign 0.9
                                        size 20
                                        color "#fff"
                                        outlines [(2, "#000", 0, 0)]

        textbutton "{color=#000}Return{/color}" style "powerup_button":
            action Hide("photo_album")
            xalign 0.5
            yalign 0.98
            background "#fff8"
            hover_background "#fffa"
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            
    else:
        # Photo viewing section remains unchanged
        frame:
            background None
            xfill True
            yfill True
            
            vbox:
                xfill True
                yfill True
                spacing 20
                $ photo_text = str(current_model) + " - Photo " + str(current_photo_index + 1) + "/" + str(len(photo_albums[current_model]))
                
                button:
                    xfill True
                    yfill True
                    action SetScreenVariable("current_photo_index", 
                        (current_photo_index + 1) % len(photo_albums[current_model]))
                    background None
                    
                    add photo_albums[current_model][current_photo_index]:
                        align (0.5, 0.5)
                        fit "contain"
            
        frame:
            xfill True
            yalign 1.0
            background "#0008"
            padding (20, 20)
            
            hbox:
                xalign 0.5
                spacing 60
                
                textbutton "<< Previous":
                    style "powerup_button"
                    text_size 30
                    text_color "#000"
                    action SetScreenVariable("current_photo_index", 
                        (current_photo_index - 1) % len(photo_albums[current_model]))
                    hover_background "#fffa"
                    background "#fff8"
                    hover_sound "audio/soun_fx/select2.opus"
                    activate_sound "audio/soun_fx/select4.opus"
                
                textbutton "Back to Albums":
                    style "powerup_button"
                    text_size 30
                    text_color "#000"
                    action SetScreenVariable("current_model", None)
                    hover_background "#fffa"
                    background "#fff8"
                    hover_sound "audio/soun_fx/select2.opus"
                    activate_sound "audio/soun_fx/select4.opus"
                
                textbutton "Next >>":
                    style "powerup_button"
                    text_size 30
                    text_color "#000"
                    action SetScreenVariable("current_photo_index", 
                        (current_photo_index + 1) % len(photo_albums[current_model]))
                    hover_background "#fffa"
                    background "#fff8"
                    hover_sound "audio/soun_fx/select2.opus"
                    activate_sound "audio/soun_fx/select4.opus"
        
        text photo_text:
            size 30 
            xalign 0.5
            yalign 0.02
            outlines [ (2, "#000", 0, 0) ]
            color "#fff"



init python:
    def mark_screen_image_gallery(baseImage):
        # Try both shown_as and display_name variations
        renpy.show(baseImage, layer="transient")
        renpy.hide(baseImage, layer="transient")
        return



screen parallax1280(baseImage, zoom=1, initial_ypos=0.0, menuenabled=False, facetoadd=None, imgtoadd=None,transformeffect=None):
    on "show" action Function(mark_screen_image_gallery, baseImage)
    key "K_SPACE" action Return()
    if menuenabled == False:
        button:
            action Return()
            
    viewport id "parallax_viewport123" at (transformeffect if transformeffect else None):
        area (0, 0, 1.5, 1.5)
        edgescroll (300, 550)
        yinitial initial_ypos
        draggable True
        add baseImage:
            subpixel True
            yalign initial_ypos
            zoom zoom
        if facetoadd is not None:
            add facetoadd:
                subpixel True
                yalign initial_ypos
                zoom zoom
        if imgtoadd is not None:
            add imgtoadd:
                subpixel True
                yalign initial_ypos
                zoom zoom


    
   

default parallax_zoom_states = [0.0, 0.0] 

screen parallaxcentered(baseImage, zoom=1, initial_ypos=0.0, menuenabled=False, zoom_states=[1.2, 0.8]):
    on "show" action Function(mark_screen_image_gallery, baseImage)
    default screen_zoom_index = 0
    
    key "K_SPACE" action Return()
    if menuenabled == False:
        button:
            action Return()
    
    imagebutton:
        xalign 0.0 yalign 0.3
        hovered Show("displayTextScreen", displayText = "Change Zoom level")
        unhovered [Hide("displayTextScreen")]
        
        idle (im.Scale("ui/return_button_idle.png", 100, 100) if screen_zoom_index == 0 else im.Scale("ui/return_button_hover.png", 100, 100))
        action [
            SetScreenVariable("screen_zoom_index", 1 - screen_zoom_index)
        ]
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"
            
    viewport:
        xfill True
        yfill True
        edgescroll (300, 550)
        yinitial initial_ypos
        draggable True
        
        frame:
            background None
            xfill True
            xalign 0.5
            padding (0, 0, 0, 0)
            margin (0, 0, 0, 0)
            add baseImage:
                subpixel True
                xalign 0.5
                zoom zoom * zoom_states[screen_zoom_index]


screen sakuraparallax():
    imagebutton:
        xalign 0.95 yalign 0.05
        auto "images/ui/return_button_%s.png"
        hovered Show("displayTextScreen", displayText = "Switch to Sarada")
        unhovered [Hide("displayTextScreen")]
        action [Show("saradaparallax"), Hide("saradaparallax"), Hide("displayTextScreen")]
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"

    key "K_SPACE" action Return()
    button:
        action Return()

    viewport:
        area (0, 0, 1.5, 1.5)
        edgescroll (300, 550)
        add "dreamsakura" subpixel True zoom 0.68
        draggable True

screen saradaparallax():
    key "K_SPACE" action Return()
    button:
        action Return()

    viewport:
        area (0, 0, 1.5, 1.5)
        edgescroll (300, 550)
        add "dreamsarada1" subpixel True zoom 0.5
        draggable True

screen sakuraparallaxbutton:
    zorder 500
    imagebutton:
        xalign 0.95 yalign 0.05
        auto "images/ui/return_button_%s.png"
        hovered Show("displayTextScreen", displayText = "Switch to Sarada")
        unhovered [Hide("displayTextScreen")]
        action [Show("saradaparallax"), Show("saradaparallaxbutton"), Hide("sakuraparallax"), Hide("displayTextScreen"), Hide("sakuraparallaxbutton")]
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"

screen saradaparallaxbutton:
    zorder 500
    imagebutton:
        xalign 0.95 yalign 0.05
        auto "images/ui/return_button_%s.png"
        hovered Show("displayTextScreen", displayText = "Switch to Sakura")
        unhovered [Hide("displayTextScreen")]
        action [Show("sakuraparallax"), Show("sakuraparallaxbutton"), Hide("saradaparallax"), Hide("displayTextScreen"), Hide("saradaparallaxbutton")]
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"

screen hidescreen1280button:
    zorder 500
    imagebutton:
        xalign 0.95 yalign 0.05
        auto "images/ui/return_button_%s.png"
        hovered Show("displayTextScreen", displayText = "Switch to full view")
        unhovered [Hide("displayTextScreen")]
        action [Hide("hidescreen1280button"), Hide("parallax1280"), Hide("displayTextScreen")]
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"





screen parallax1280peek(baseImage, overlay_image, zoom = 1):
    on "show" action Function(mark_screen_image_gallery, baseImage)
    key "K_SPACE" action Return()
    
    button:
        action Return()
        xsize 1920
        ysize 1080
        background None

    viewport:
        area (0, 0, 1.5, 1.5)
        edgescroll (300, 550)
        add baseImage subpixel True zoom(zoom)
        draggable True

    # Overlay the transparency image directly
    add overlay_image:
        zoom 0.69
        xalign 0.5
        yalign 0.5

        
            
 