

label v1_secret_himawarisecretscene:
$ initialize_replay_defaults()
scene black with dissolve
$ renpy.sound.play("/audio/soun_fx/footsteps.opus", channel="sfx2", loop=False, relative_volume = 0.8)
scene bg day with dissolve:
    zoom 0.70
show boruto normal at center with dissolve
"You hear someone running through the living room"
$ snacksininv = inventory.find_item_by_name("Snacks")
bot"Must be [him_name]... It's right around the time she comes back from school."
bot"Why the hell is she running around all the time!"
menu:
    bot"Why the hell is she running around all the time!"
    "Block her way!":
        show boruto sceeming with dissolve
        "Right as [him_name] was about to cut the corner you..."
        show boruto:
            easein 1 xpos -1000
        pause 1
        scene black with vpunch
        $ renpy.sound.play("/audio/soun_fx/himawari/kyaa.opus", channel="sfx2", loop=False, relative_volume = 0.5)
        show himaintro stand1_1 with dissolve
        show himaintro:
            easein 2 subpixel True yalign 0.2
        pause 2
        $ notification(f"{him_name}'s School outfit unlocked")
        show himaintro stand1_2 with dissolve
        him"U-gh!" with vpunch
        him"Watch where you are going you m-monkey!" with vpunch
        scene bg lr_day:
            blur 20
        show himaintro stand1_2:
            zoom 0.65 xalign 0.5 yalign 0.4
        with dissolve
        menu:
            him"Watch where you are going you m-monkey!" 
            "{color=[hatredcolor]}You are the one at fault, bitch!{/color}":
                call changeHatred(1) from _call_changeHatred_5
                bo"Why the fuck are you speed-demoning around the goddamn living room you bitch!"
                bo"How the fuck is this my fault!?" with vpunch
                show himaintro stand1_3 with dissolve
                him"You are such a shitty [him_rel_to_bo], you know that...?"
                menu:
                    him"You are such a shitty [him_rel_to_bo], you know that...?"
                    "{color=[dominancecolor]}Takes one to know one{/color}":
                        bo"Takes a shit [him_rel] to know a shit [him_rel_to_bo]!"
                        call changeDominance(1) from _call_changeDominance_6
                        bo"Now stop being a little bitch and cover yourself up, your panties are in full display..."
                        show himaintro stand2_1 with dissolve:
                            zoom 1.0 xalign 0.5 yalign 1.0
                        show himaintro:
                            easein 2 yalign 0.1
                        him"Why can't you just say sorry and help me up like a normal person!" with vpunch
                        him"And why are you even watching there to begin with! Freaking perv..."
                        scene black with vpunch
                        him"Wait a second... Is this what I think it is?"
                        "[him_name] gets up on her feet..."
                        
                        scene bg lr_day:
                            blur 20
                        show himaintro stand3_3 with dissolve
                        with dissolve
                        show himaintro:
                            easein 2 subpixel True yalign 0.1
                        him"I know what this is about..."
                        "Unbeknownst to [him_name]. one of her shirt's buttons came lose, her cleavage now in full display to you..."
                        him"You are jealous... aren't you?"
                        jump introhima_final

                    "Stare at her legs":
                        jump introstarelegs

                    "{color=[hatredcolor]}Slut-shame her":
                        bo"A shitty [him_rel_to_bo] for a slutty [him_rel]! Just what you deserve!"
                        show himaintro stand2_1 with dissolve:
                            zoom 1.0 yalign 1.0
                        show himaintro:
                            easein 2 subpixel True yalign 0.2
                        label introhima_slutshame:
                        him"I am n-not a s-slut! You dumb-fuck..." with vpunch
                        show himaintro with dissolve:
                            zoom 0.65 xalign 0.5 yalign 0.4
                        "[him_name] takes a more reserved posture after realizing she unwillingly exposed her bottom to you..."
                        bo"Oh yeah? Then explain what the fuck this shit is that you are wearing at school..."
                        show himaintro with dissolve:
                            zoom 1 xalign 1.0 yalign 1.0
                        bo"What's up with the mini-skirt and why are your... socks the size of my penis?"
                        show himaintro:
                            easein 2 subpixel True yalign 0.1
                        him"First of all those aren't socks you god-damned buffoon! They are thigh-highs and they are cute and sexy..."
                        him"All the boys say they love how I look in them."
                        show himaintro with dissolve:
                            zoom 0.65 xalign 0.5 yalign 0.4
                        him"Secondly, your willy is more likely the size of my pinky than my socks. Freaking weirdo!"
                        scene black with dissolve
                        bo"You wanna find out then you slut?" with vpunch
                        "[him_name] gets up on her feet..."
                        
                        scene bg lr_day:
                            blur 20
                        show himaintro stand3_3 with dissolve
                        with dissolve
                        show himaintro:
                            easein 2 subpixel True yalign 0.1
                        him"Oooh? I know what this is about..."
                        "Unbeknownst to [him_name]. one of her shirt's buttons came lose, her cleavage now in full display to you..."
                        him"You are jealous... aren't you?"
                        label introhima_final:
                        show himaintro stand3_4 with dissolve:
                            zoom 1.1 yalign 0.1
                        him"You hate the fact that your pretty little [him_rel] gets all the attention..."
                        show himaintro stand3_4 with dissolve:
                            zoom 0.55 yalign 0.25
                        him"You know... All the boys at school say the nicest things, they buy me little gifts and do anything I ask of them!"
                        him"I am sure a loser such as you envies my popularity!"
                        him"Is that it, you big fat loser?" with vpunch
                        menu:
                            him"Is that it, you big fat loser?"
                            "You are so naive...":
                                bo"You are so naive, [him_name]... None of these boys care about you. They simply want to-"
                                scene bg lr_day:
                                    zoom 0.68
                                show himaschoolt angry at right:
                                    zoom 0.55
                                show boruto surprised2 at left
                                with dissolve
                                him"And what would you know about that you useless [him_rel_to_bo]!" with vpunch
                                show himaschoolt angry:
                                    easein 1 xpos 1100
                                him"Do YOU care about me? Do you even care about [hin_rel]!?" with vpunch
                                show himaschoolt angry:
                                    easein 1 xpos 100
                                him"Stay away from me... Pretentious loser!" with vpunch
                                call changeLove("Himawari", -1) from _call_changeLove_6
                                show boruto suspicious with dissolve
                                bot"..."
                                menu:
                                    bot"..."
                                    "I think I understand now...":
                                        show boruto worried2 with dissolve
                                        bot"I think I get what's up with [him_name]..."
                                        bot"She is looking for affirmation... m-my, affirmation?"
                                        bot"Maybe... I am not sure."
                                        bot"She certainly sounded like she hid some deep rooted insecurities just now..."
                                        bot"I'll have to show her that I care about her if she's ever going to bring those walls of hers down."

                                    "{color=[hatredcolor]}Ha! Serves her right...{/color}":
                                        show boruto sceeming with dissolve
                                        bot"Ha! Dumb bitch..."
                                        bot"Does she really think I would ever give a fuck about her with how she acts?"
                                        show boruto sceeming2 with dissolve
                                        call changeHatred(1) from _call_changeHatred_6
                                        bot"I mean... I do give a fuck! Just not the one she'd like..."
                                    
                            "{color=[hatredcolor]}They just want to get in your pants you dumb bitch!{/color}":
                                bo"They are just trying to get in your pants you dumb bitch!"
                                call changeHatred(1) from _call_changeHatred_7
                                bo"We boys know a slut when we see one and you fit the bill perfectly!"
                                scene bg lr_day:
                                    zoom 0.68
                                show himaschoolt angry at right:
                                    zoom 0.55
                                show boruto sceeming2 at left
                                with dissolve
                                him"Stop calling me the s-word you retard!" with vpunch
                                bo"Then stop dressing like a..."
                                show boruto sceeming3 with dissolve
                                call changeHatred(1) from _call_changeHatred_8
                                bo"SLUT!" with vpunch
                                show boruto sceeming2 with dissolve
                                bo"That's what you are you little shit-stain!"
                                show himaschoolt at smallshake
                                show himaschoolt:
                                    easein 1 xpos 1000
                                him"You really are the worst... you know that!?"
                                call changeLove("Himawari", -1) from _call_changeLove_7
                                show himaschoolt:
                                    easeout 1 xpos 0
                                him"The absolute shittiest of [him_rel_to_bo]s! Don't talk to me!"
                                bo"Sluts aren't there to be talked to anyway..."
                                $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                him"Hmph!"
                                show boruto sceeming3 with dissolve
                                call borutoevil2 from _call_borutoevil2
                                call changeHatred(1) from _call_changeHatred_9
                                bot"They are only there to be fucked with!"
                                
                            

                        

                    
                

            "Stare at her legs...":
                label introstarelegs:
                    show himaintro stand1_3 with dissolve:
                        zoom 1.0 xalign 1.0 yalign 1.0
                    bot"...Is this what [him_name] wears at school nowdays?"
                    bot"That skirt is definitely too revealing..."
                    show himaintro stand1_3 with dissolve:
                        zoom 1.2 xalign 1.0 yalign 1.0
                    bot"And those... socks?"
                    show himaintro stand1_3 with dissolve:
                        easein 10 xalign 0.5 yalign 0.7
                    bot"I don't know what they are for but they sure are sexy..."
                    call increaselust(10) from _call_increaselust_10
                    bot"Fuck me... Every single boy at school must be thinking about her in that way..."
                    bot"What is she even trying to achieve dressing up like this..."
                    him"Are you..."
                    show himaintro stand1_3 with dissolve:
                        zoom 1.0 xalign 0.0 yalign 0.0
                    pause 0.5
                    show himaintro stand2_1 with dissolve:
                        zoom 1.0 xalign 0.5 yalign 1.0
                    show himaintro:
                        easein 2 yalign 0.1
                    
                    him"Are you staring at me you perv!?" with vpunch
                    show himaintro stand2_1 with dissolve:
                        zoom 0.65 xalign 0.5 yalign 0.2
                    bo"..."
                    menu:
                        him"Are you staring at me you perv!?" with vpunch
    
                        "{color=[hatredcolor]}Slut-shame her{/color}":
                            bo"How can I not when you dress like a god-damned slut!" with vpunch
                            jump introhima_slutshame
                        "{color=[obediencecolor]}Hard not to! You are pretty hot, I'll give you that...{/color}":
                            bo"You lean into that a little bit too well [him_name]! You are hot, you know that?"
                            call changeRespect("Himawari", -1) from _call_changeRespect_18
                            show himaintro stand2_1:
                                zoom 0.8 xalign 0.5 yalign 0.2
                            him"I am your [him_rel] you freaking perv!" with vpunch
                            him"I don't need you telling me that!"
                            show himaintro stand2_1 with dissolve:
                                zoom 0.65 xalign 0.5 yalign 0.2
                            bo"[him_rel] or not, doesn't make it any less true. You are still a bitch though, don't let it get to your head!"
                            call changeObedience("Himawari", 1) from _call_changeObedience_17
                            scene black with vpunch
                            him"Y-you...!"
                            "[him_name] gets up on her feet..."
                            scene bg lr_day:
                                blur 20
                            show himaintro stand3_3 with dissolve
                            with dissolve
                            show himaintro:
                                easein 2 subpixel True yalign 0.1
                            him"Oooh? I know what this is about..."
                            "Unbeknownst to [him_name]. one of her shirt's buttons came lose, her cleavage now in full display to you..."
                            him"That look... It's the same as every single boy's look at school..."
                            him"They always look all over me with their puppy eyes..."
                            jump introhima_final
                        




            "I am sorry. Here, let me help...":
                bo"I am sorry... Here, let me help you up!"
                show himaintro stand2 with dissolve
                show himaintro:
                    easein 2 subpixel True yalign 0.2
                pause 1
                call changeRespect("Himawari", 1) from _call_changeRespect_19
                him"T-thanks..."
                scene black with dissolve
                "You extend an arm and help [him_name] to her feet..."
                him"...so? You want something?"
                jump introgreether

            


    "Greet her":
        bot"I should say hello..."
        show boruto normal:
            easein 1 xpos -1000
        pause 0.5
        label introgreether:
        scene himaintro stand3_3 with dissolve
        show himaintro:
            easein 2 subpixel True yalign 0.1
        pause 2
        $ notification(f"{him_name}'s School outfit unlocked")
        bot"W-why is her shirt u-unbuttoned..." with vpunch
        scene bg lr_day:
            zoom 0.68
        show himaschoolt smug at right:
            zoom 0.55
        show boruto surprised2 at left
        with dissolve
        him"What are you staring at... loser?"
        menu:
            him"What are you staring at... loser?"
            "{color=[obediencecolor]}Staying cool, aren't you?{/color}":
                show boruto snob
                bo"Staying cool, aren't you [him_name]?"
                him"What do you mean..."
                bo"Might wanna check your shirt!"
                show himaschoolt normal at right with dissolve:
                    zoom 0.55
                show himaschoolt normal at smallshake:
                    zoom 0.55
                call changeObedience("Himawari", 1) from _call_changeObedience_18
                him"O-oh! Must have come unbuttoned on its own..."
                show himaschoolt smug at right:
                    zoom 0.55
                show himaschoolt:
                    easein 1 xalign 0.6
                him"I am home anyway, aren't I?"
                show himaschoolt:
                    easeout 1 xpos -200
                him"I should be able to cool off without perverts staring at my boobs!"
                menu himaintro_smenu:
                    him"I should be able to cool off without perverts staring at my boobs!"
                    "[him_name] wait. I've got something for you..." (secretlove = True) if snacksininv!= None:
                        label testing:
                        show boruto surprised2
                        bo"[him_name], wait! I've got something for you..."
                        show himaintro stand3_1 with dissolve
                        show himaintro:
                            easein 2 subpixel True yalign 0.2
                        him"You've got something... for me?"
                        bo"I haven't forgotten you know..."
                        show himaintro stand3_0 with dissolve:
                            zoom 1.1 xalign 0.5 yalign 0.1
                        bo"What you've asked for the other day, I got them for you."
                        bo"A lot has happened since then... You know, with my condition and all."
                        bo"I am sorry I couldn't give this to you sooner..."
                        call useItem(snacks,1) from _call_useItem_1
                        label replay_testing:
                        $ initialize_replay_defaults()
                        scene black with dissolve
                        him"..."
                        show bg lr_day:
                            blur 20
                        show himasecret_0:
                            zoom 1 xalign 0.5 yalign 1.0
                        with dissolve
                        show himasecret_0:
                            easein 3 subpixel True yalign 0.05
                        "[him_name] threw herself in your arms and slid one of her hands under your pits and around your back."
                        "You awkwardly placed yours around her waist in disbelief..."
                        him"I knew you weren't THAT useless..."
                        show himasecret_0 with dissolve:
                            zoom 0.8 xalign 0.5 yalign 0.2
                        him"You are still a shit, bozo, assface, stupid, ugly brother... Did I say stupid?"
                        bo"Uuuuh..."
                        show himasecret_0_1 with dissolve:
                            zoom 1.2 xalign 0.5 yalign 0.0
                        call changeLove("Himawari", 2) from _call_changeLove_8
                        him"But at least now I know that you care..."
                        him"Even if it's just a little."
                        show himasecret_0_1 with dissolve:
                            zoom 0.8 xalign 0.5 yalign 0.2
                        him"It's not even about the snacks you know..."
                        scene bg lr_day:
                            blur 20
                        show himasecret_1:
                            zoom 1 xalign 0.5 yalign 1.0
                        with dissolve
                        show himasecret_1:
                            easein 3 subpixel True yalign 0.05
                        pause 1
                        him"But I am not getting into that right now!"
                        show himasecret_1 with dissolve :
                            zoom 0.65 xalign 0.5 yalign 0.2
                        bot"Is she... okay?"
                        "[him_name]'s extremely rare affectionate demeanor left you perplexed."
                        "Was a single gift all it took to win back her good graces? Or could something else be at play..."
                        "Your moment of conteplation would be cut short..."
                        $ renpy.sound.play("/audio/soun_fx/mosquito.opus", channel="sfx2", loop=False, relative_volume = 0.75)
                        show flybug with dissolve:
                            zoom 0.1 xpos -100 yalign 0.3
                        show flybug:
                            easein 2 zoom 0.08 xpos 1000 yalign 0.5 xzoom -1
                        pause 2
                        show flybug:
                            easein 1 zoom 0.06 xpos 300 yalign 0.7 xzoom -1
                        pause 1
                        show flybug:
                            easeout 1 zoom 0.05 pos (627, 0.72) xzoom -1 
                        stop sfx2 fadeout 1   

                        "As [him_name] was pulling away, a tiny little fly buzzed through the air and landed on her skirt..."
                        bo"[him_name] wait! Stay extremely still..." with vpunch
                        him"W-why... what's going on?"
                        bo"Did you hear that?"
                        him"Hear what...?"
                        bo"Well... about the thing you have with bugs..."
                        him"B-BUGS!?" with vpunch
                        bot"[him_name] has an extreme phobia of bugs. What if I..."
                        
                        menu:
                            bot"[him_name] has an extreme phobia of bugs. What if I..."
                            "{color=[dominancecolor]}Try something stupid that might just work{/color}":
                                scene bg lr_day:
                                    blur 20
                                show himasecret_1_1:
                                    zoom 0.65 xalign 0.5 yalign 0.2
                                show flybug:
                                    zoom 0.05 pos (627, 0.72) xzoom -1 
                                    

                                with dissolve
                                bo"Listen to me and listen carefully..."
                                scene himasecret_1_1
                                show flybug:
                                    zoom 0.1 pos (581, 0.33) xzoom -1
                                    

                                with dissolve
                                bo"There's a... HUGE bug, on your...  back. But if you stay still-"
                                $ renpy.sound.play("/audio/soun_fx/himawari/himascared2.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                                him"A B-B-B-BUG?" with vpunch
                                him"T-take it off me! T-TAKE IT OFF!" with vpunch
                                scene bg lr_day:
                                    blur 20
                                scene himasecret_1_1:
                                    zoom 1.2 xalign 0.5 yalign 0.1
                                with dissolve
                                bo"Shhh! I promise you I will..."
                                show himasecret_1_1:
                                    zoom 1.2 xalign 0.5 yalign 0.7
                                show flybug:
                                    zoom 0.1 pos (627, 0.60) xzoom -1 
                                with dissolve
                                pause 0.7
                                scene bg lr_day:
                                    blur 20
                                show himasecret_1_1:
                                    zoom 0.6 xalign 0.5 yalign 0.5
                                show flybug:
                                    zoom 0.05 pos (627, 0.65) xzoom -1 
                                with dissolve
                                bo"But you have to stay still..."
                                show himasecret_1_2 behind flybug with dissolve:
                                    zoom 0.6 xalign 0.5 yalign 0.5
                                bo"Easy does it..."
                                bo"...Aaaaand!"
                                show himasecret_1_2:
                                    zoom 0.9 xalign 0.5 yalign 0.8
                                show flybug:
                                    zoom 0.07 pos (600, 0.57) xzoom -1
                                with dissolve
                                bo"Oh! It moved down to your..."
                                show himaintro_s 1 with Dissolve(0.3):
                                    zoom 0.9 xalign 0.5 yalign 0.8
                                show himaintro_s 2 with Dissolve(0.2):
                                    zoom 0.9 xalign 0.5 yalign 0.8
                                $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                with vpunch
                                show himaintro_s 3 with Dissolve(0.4):
                                    zoom 0.9 xalign 0.5 yalign 0.8
                                $ renpy.sound.play("/audio/soun_fx/himawari/kyaa.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                                call changeDominance(1) from _call_changeDominance_7
                                bo"Your back! I think I got it..." with vpunch
                                him"O-ouchie!" with vpunch
                                him"T-that's n-n-not my b-back! Y-you IDIOT!" with vpunch
                                bo"It moved down here! what was I supposed to do?"
                                him"Is i-i-i-it g-gone?"
                                scene bg lr_day:
                                    blur 20
                                show himaintro_s 3:
                                    zoom 0.6 xalign 0.5 yalign 0.5
                                with dissolve
                                bo"Here, let me show you..."
                                show himaintro_s 4 with Dissolve(1):
                                    zoom 0.6 xalign 0.5 yalign 0.5
                                "You slowly slid your fingers up her buttock under the premise of your silly ruse..."
                                show himaintro_s 4 with Dissolve(1):
                                    zoom 1.0 xalign 0.5 yalign 1.0
                                "A visible bruise would be revealed beneath [him_name]'s slightly raised skirt."
                                show himaintro_s 4 with dissolve:
                                    zoom 0.6 xalign 0.5 yalign 0.5
                                bot"Fuck me... [him_name] certainly has an ass on her!"
                                bot"I couldn't pass up an opportunity like this..."
                                bot"Hopefully the fly is in my hand, or I am about to get shit on!"
                                show himasecret_1_3s with dissolve:
                                    zoom 1.0 xalign 0.5 yalign 1.0
                                show himasecret_1_3s:
                                    easein 2 xalign 0.5 yalign 0.1
                                pause 1
                                him"S-so...!?" with vpunch
                                call changeObedience("Himawari",1) from _call_changeObedience_19
                                him"M-move your h-hand away and show me!" with vpunch
                                scene bg lr_day:
                                    zoom 0.68
                                show himasecret_1_3s:
                                    zoom 0.6 xalign 0.5 yalign 0.5
                                with dissolve
                                bo"R-right..."
                                show black with vpunch
                                him"From a distance!" with vpunch
                                scene bg lr_day:
                                    zoom 0.68
                            
                                show himaschoolt normal:
                                    zoom 0.55 ypos 26
                                show boruto sceeming behind himaschoolt
                                with dissolve
                
                                show himaschoolt:
                                    easein 0.5 xpos -150
                                him"I don't want to see a yucky bug up-close!"
                                show boruto surprised2 with dissolve
                                bot"Here goes nothing..."
                                show boruto surprised3 with dissolve
                                "You open your palm and..."
                                bo"T-there..."
                                him"Th-..."
                                show himaschoolt angry with dissolve
                                show himaschoolt at shake
                                call changeRespect("Himawari",-1) from _call_changeRespect_20
                                him"T-THAT'S A TEENY-TINY FLY YOU RETARD!" with vpunch
                                call changeObedience("Himawari",1) from _call_changeObedience_20
                                him"Y-you didn't have to go t-that far for a f-fly!"
                                show himaschoolt:
                                    easeout 2 xpos -1000
                                him"*Scoffs* I am n-not scared of t-tiny flies you i-idiot..."
                                bo"O-okay..."
                                him"I AM NOOOT!" with vpunch
                                himt"Yuck, yuck, YUCK!"
                                bot"Well..."
                                show boruto surprised2 with dissolve
                                bot"That went much better than I expected!"
                                show boruto sceeming with dissolve
                                bot"I wonder if I could make some use out of this phobia of hers in the future..."
                                scene black with dissolve
                                $ renpy.end_replay()
                                $ notification (f"{him_name} Love objective completed")
                                $ quest_him.check("him1L_4", "completed")
                                bot"Didn't [na_rel] know a guy who's a bug master or something?"










                                
                                
                            "{color=[obediencecolor]}'Help her' get rid of the bug{/color}":
                                scene bg lr_day:
                                    blur 20
                                show himasecret_1_1:
                                    zoom 0.65 xalign 0.5 yalign 0.2
                                show flybug:
                                    zoom 0.05 pos (627, 0.72) xzoom -1 
                                    

                                with dissolve
                                bo"Listen to me and listen carefully..."
                                scene himasecret_1_1
                                show flybug:
                                    zoom 0.1 pos (581, 0.33) xzoom -1
                                    

                                with dissolve
                                bo"There's a... HUGE bug, on your...  back."
                                $ renpy.sound.play("/audio/soun_fx/himawari/himascared2.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                                him"A B-B-B-BUG?" with vpunch
                                him"T-take it off me! T-TAKE IT OFF!" with vpunch
                                scene bg lr_day:
                                    blur 20
                                scene himasecret_1_1:
                                    zoom 1.2 xalign 0.5 yalign 0.1
                                with dissolve
                                bo"I will, but I might have to touch your... back!"
                                show himasecret_1_1:
                                    zoom 1.2 xalign 0.5 yalign 0.7
                                show flybug:
                                    zoom 0.1 pos (627, 0.60) xzoom -1 
                                with dissolve
                                him"Just t-take it off me please! Do w-whatever it takes..."
                                pause 0.7
                                scene bg lr_day:
                                    blur 20
                                show himasecret_1_1:
                                    zoom 0.6 xalign 0.5 yalign 0.5
                                show flybug:
                                    zoom 0.05 pos (627, 0.65) xzoom -1 
                                with dissolve
                                bo"O-okay, but you have to stay still! Otherwise it might move on to your legs..."
                                show himasecret_1_2 behind flybug with dissolve:
                                    zoom 0.6 xalign 0.5 yalign 0.5
                                him"M-my l-l-l-l-legs!? P-please do something!"
                                bo"I got it..."
                                bo"...Aaaaand!"
                                show himasecret_1_2:
                                    zoom 0.9 xalign 0.5 yalign 0.8
                                show flybug:
                                    zoom 0.07 pos (600, 0.57) xzoom -1
                                with dissolve
                                bo"Oh! It moved down to..."
                                menu:
                                    bo"Oh! It moved down to..."
                                    "{color=[obediencecolor]}'Your Ass!'{/color}":
                                        show himaintro_g 1 with dissolve
                                        bo"Your ass!" with vpunch
                                        call changeObedience("Himawari",1) from _call_changeObedience_21
                                        him"M-m-my ass!?" with vpunch
                                        bo"I think I got it..."
                                        him"W-where do you think you are t-touchi-"
                                        menu himasecret_intro:
                                            him"W-where do you think you are t-touchi-"
                                            "{color=[obediencecolor]}I think it slipped further down...{/color}":
                                                bo"I am not sure I caught it. I think it slipped further down!"
                                                him"W-W-WHAT!? P-p-please take it off of me!" with vpunch
                                                show himaintro_g 2 with dissolve
                                                bo"T-there! That should do it..." with vpunch
                                                "You sank your fingers in [him_name]'s meaty buttocks under the premise of your silly ruse..."
                                                him"D-d-did you get it!?" with vpunch
                                                call changeObedience("Himawari",1) from _call_changeObedience_22
                                                him"Now m-move your hands away!"
                                                menu himakeepgoingmenu:
                                                    him"Now m-move your hands away!"
                                                    "{color=[hatredcolor]}Keep going!{/color}":
                                                        
                                                        bo"Oh no! It's moving down your thighs!" with vpunch
                                                        him"W-WHAT!?" with vpunch
                                                        show intro_hima1 with dissolve
                                                        bo"Don't worry... I can still catch it!"
                                                        $ renpy.sound.play("/audio/soun_fx/himawari/kyaa.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                                                        him"Kyaa!" with vpunch
                                                        call changeHatred(1) from _call_changeHatred_10
                                                        bot"[him_name] is such a dumb bitch when it comes to sex-stuff! I can't believe she is so oblivious to what I am doing..."
                                                        "You kept digging your hands around her buttocks and started playing around with it..."
                                                        "Up and down, right and left, you made sure to feel every nook and cranny of it..."
                                                        call changeObedience("Himawari",1) from _call_changeObedience_23
                                                        him"W-what are you d-doing! D-d-d-did you c-catch it!?" with vpunch
                                                        bo"I... think so!"
                                                        menu:
                                                            bo"I... think so!"
                                                            "{color=[hatredcolor]}But just to make sure, I have to...{/color}":
                                                                bo"But just to make sure..."
                                                                show intro_hima2 with dissolve
                                                                "You maniacally digged your fingers in [him_name]'s buttocks..."
                                                                him"H-HEY! S-STOP IT!" with vpunch
                                                                call changeRespect("Himawari", -1) from _call_changeRespect_21
                            
                                                                bo"I am just making sure [him_name]!" with vpunch
                                                                him"N-no you aren't! You are just perving!"
                                                                scene bg lr_day:
                                                                    blur 20
                                                                show himasecret_1_2:
                                                                    zoom 0.6 xalign 0.5 yalign 0.5
                                                                show flybug:
                                                                    zoom 0.05 pos (627, 0.65) xzoom -1 
                                                                with dissolve
                                                                "As she started pulling away you..."
                                                                bo"There!"
                                                                
                                                                show himasecret_1_2:
                                                                    zoom 0.9 xalign 0.5 yalign 0.8
                                                                show flybug:
                                                                    zoom 0.07 pos (600, 0.57) xzoom -1
                                                                with dissolve
                                                            
                                                                show himaintro_s 1 with Dissolve(0.3):
                                                                    zoom 0.9 xalign 0.5 yalign 0.8
                                                                show himaintro_s 2 with Dissolve(0.2):
                                                                    zoom 0.9 xalign 0.5 yalign 0.8
                                                                $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                                                with vpunch
                                                                show himaintro_s 3 with Dissolve(0.4):
                                                                    zoom 0.9 xalign 0.5 yalign 0.8
                                                                $ renpy.sound.play("/audio/soun_fx/himawari/kyaa.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                                                                call changeDominance(1) from _call_changeDominance_8
                                                                bo"This should seal the deal!" with vpunch
                                                                him"O-OUCH!" with vpunch
                                                                scene black with vpunch
                                                                call changeRespect("Himawari", -1) from _call_changeRespect_22
                                                                him"YOU F-FREAKING PERVERT!" with vpunch
                                                                scene bg lr_day:
                                                                    zoom 0.68
                                                            
                                                                show himaschoolt angry:
                                                                    zoom 0.55 ypos 26
                                                                show boruto sceeming behind himaschoolt
                                                                with dissolve
                                                
                                                                show himaschoolt:
                                                                    easein 0.5 xpos -150
                                                                call changeLove("Himawari",-1) from _call_changeLove_9
                                                                him"There was never a b-b-bug in the first place, was there!?"
                                                                show boruto sceeming3 with dissolve
                                                                "You open your palm and show her the dead fly..."
                                                                show boruto:
                                                                    easein 0.3 xpos 400
                                                                bo"Here it is!" with vpunch
                                                                show himaschoolt:
                                                                    easein 0.4 xpos -1000
                                                                him"KYAAAAAAAA!!" with vpunch
                                                                call changeObedience("Himawari", 1) from _call_changeObedience_24
                                                                him"Y-y-y-you shouldn't have gone that far for it, YOU RETARD!" with vpunch
                                                                call changeHatred(1) from _call_changeHatred_11
                                                                bot"She is so gullible and stupid!"
                                                                show boruto sceeming2 with dissolve
                                                                bot"I bet she doesn't even know what a cock looks like!"
                                                                $ renpy.end_replay()
                                                                $ notification (f"{him_name} Hatred objective completed")
                                                                $ quest_him.check("him1H_4", "done")
                                                                bot"I wonder in what other ways I can mess with her..."
                                                                

                                                            "Here, wanna see?":
                                                                bo"Yep, I got it!"
                                                                jump himaintro_groppend
                                                            

                                                    "Of course...":
                                                        bo"Of course..."
                                                        jump himaintro_groppend
                                                    

                                            "Sorry, It just moved down there":
                                                label himaintro_groppend:
                                                bo"Sorry about that but I had to get it off of you, right?"
                                                $ renpy.sound.play("/audio/soun_fx/himawari/himascoff1.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                                                hin"Hmph!"
                                                scene bg lr_day:
                                                    zoom 0.68 blur 20
                                                show himasecret_1_3:
                                                    zoom 0.6 xalign 0.5 yalign 0.5
                                                with dissolve
                                                bo"Here... wanna see?"
                                                call changeObedience("Himawari",1) from _call_changeObedience_25
                                                show himasecret_1_3 with dissolve:
                                                    zoom 0.75 xalign 0.5 yalign 0.1
                                                him"M-move your h-hand away and show me!" with vpunch
                                                
                                                bo"R-right..."
                                                show black with vpunch
                                                him"From a distance!" with vpunch
                                                scene bg lr_day:
                                                    zoom 0.68
                                            
                                                show himaschoolt normal:
                                                    zoom 0.55 ypos 26
                                                show boruto sceeming behind himaschoolt
                                                with dissolve
                                
                                                show himaschoolt:
                                                    easein 0.5 xpos -150
                                                him"I don't want to see a yucky bug up-close!"
                                                show boruto surprised2 with dissolve
                                                bot"Here goes nothing..."
                                                show boruto surprised3 with dissolve
                                                "You open your palm and..."
                                                bo"T-there..."
                                                him"Th-..."
                                                show himaschoolt angry with dissolve
                                                show himaschoolt at shake
                                                call changeRespect("Himawari",-1) from _call_changeRespect_23
                                                him"T-THAT'S A TEENY-TINY FLY YOU RETARD!" with vpunch
                                                call changeObedience("Himawari",1) from _call_changeObedience_26
                                                him"Y-you didn't have to go t-that far for a f-fly!"
                                                show himaschoolt:
                                                    easeout 2 xpos -1000
                                                him"*Scoffs* I am n-not scared of t-tiny flies you i-idiot..."
                                                bo"O-okay..."
                                                him"I AM NOOOT!" with vpunch
                                                himt"Yuck, yuck, YUCK!"
                                                bot"Well..."
                                                show boruto surprised2 with dissolve
                                                bot"That went much better than I expected!"
                                                show boruto sceeming with dissolve
                                                bot"I wonder if I could make some use out of this phobia of hers in the future..."
                                                scene black with dissolve
                                                $ renpy.end_replay()
                                                $ notification (f"{him_name} Love objective completed")
                                                $ quest_him.check("him1L_4", "completed")
                                                bot"Didn't [na_rel] know a guy who's a bug master or something?"
                                                
                                                
                                            
                                        
                                    "{color=[obediencecolor]}'Your lower back'{/color}":
                                        show himaintro_g 1 with dissolve
                                        bo"Your lower b-back!" with vpunch
                                        call changeObedience("Himawari",2) from _call_changeObedience_27
                                        him"T-that's m-m-my ass you IDIOT!" with vpunch
                                        bo"I think I got it..."
                                        him"W-where do you think you are t-touchi-"
                                        jump himasecret_intro
                            

                            "I really shouldn't...":
                                bot"I really shouldn't try anything stupid."
                                $ renpy.sound.play("/audio/soun_fx//mosquito.opus", channel="sfx2", loop=False, relative_volume = 0.4)

                                show flybug:
                                    easeout 2 xpos -1000
                                
                                bot"Oh, lucky you! It just flew away..."
                                stop sfx2 fadeout 1
                                scene black with dissolve
                                scene bg lr_day:
                                    zoom 0.68
                            
                                show himaschoolt normal:
                                    zoom 0.55 ypos 26
                                show boruto surprised2 behind himaschoolt
                                with dissolve
                
                                show himaschoolt:
                                    easein 0.5 xpos -150
                                him"I-i-i-is it g-gone?"
                                show boruto smirk with dissolve
                                bo"It's gone you silly goose, you can relax!"
                                show himaschoolt at smallshake
                                him"A-are you sure!?"
                                show boruto smirk2 with dissolve
                                bo"It was just a fly. I saw it flying away anyway, stop shitting your pants!"
                                show himaschoolt at shake
                                him"You know I hate bugs, flies and anything tiny with yucky crawling stick-legs!"
                                show himaschoolt smug with dissolve
                                $ renpy.sound.play("/audio/soun_fx/himawari/loserlaugh.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                                him"Kinda like you now that I think about it! You and your little chicken-legs! *Giggles*"
                                menu:
                                    him"Kinda like you now that I think about it! You and your little chicken-legs! *Giggles*"
                                    "{color=[lovecolor]}And here I thought we were getting somewhere...{/color}":
                                        show boruto worried2 with dissolve
                                        bo"And here I was thinking we were getting somewhere..."
                                        him"I know, I know... I am sorry!"
                                        him"Don't start sulking on me now..."
                                        show boruto smirk with dissolve
                                        him"Your legs are still smaller than mine though! You should consider hitting the gym soon..."
                                        show boruto snob with dissolve
                                        bo"Not everyone spends five hours on the daily training their legs you gym-demon..."
                                        bo"You can take your trunk-like legs and stick them up your bum!"
                                        him"I'll allow you that one insult because I fired first."
                                        call changeLove("Himawari", 1) from _call_changeLove_10
                                        show himaschoolt normal with dissolve
                                        him"But on a serious note... I'll be leaving my door open, you can come by and chat every now and then."
                                        show boruto surprised2 with dissolve
                                        bo"Y-yeah, there's something I wanted to talk to you about. It's about [hin_rel]..."
                                        him"[hin_rel]?"
                                        show himaschoolt:
                                            easein 1 xpos -1000
                                        him"I have to get out of this outfit first. I am getting way too sweaty..."
                                        him"We can talk later if you want..."
                                        show boruto worried with dissolve
                                        bo"Right..."
                                    "{color=[hatredcolor]}Get angry, insult her and storm off!{/color}":
                                        show boruto pissy with dissolve
                                        call changeHatred(1) from _call_changeHatred_12
                                        bo"I'll shove these stick-legs up your ass you stupid bitch!"
                                        show boruto:
                                            easein 1 xpos -1000
                                        bo"My fault for thinking about you in the first place!"
                                        call changeRespect("Himawari", -1) from _call_changeRespect_24
                                        him"It was just a joke you imbecile!"
                                        show himaschoolt normal with dissolve
                                        himt"Is he like that because of his thing [hin_rel] talked to me about?"
                                        himt"Maybe I should apologize..."
                                        show himaschoolt smug with dissolve
                                        himt"Or not! He is still a piece of shit after all..."
                                $ renpy.end_replay()

                                    
                                
                            

                        
                    "{color=[hatredcolor]}I wasn't staring you bitch!{/color}":
                        show boruto angry with dissolve
                        bo"I wasn't staring you bi-"
                        him"Sure, sure! I am off!" with vpunch
                        call changeHatred(1) from _call_changeHatred_13
                        bot"Bitch!"
                        $ renpy.end_replay()
                    "I was just looking out for you...":
                        show boruto surprised2 with dissolve
                        bo"I was just looking out for y-"
                        him"Sure, sure! I am off!" with vpunch
                        bot"This damned girl..."
                        $ renpy.end_replay()

                    


                
                    
                
            "Why would I stare...":
                show boruto smirk with dissolve
                bo"I'd rather stare at dry paint on a wall than stare at you. I was just waiting for you to say something..."
                bo"Don't you say hello when you enter a house?"
                show himaschoolt smug at right:
                    zoom 0.55
                him"Not to you I don't! Teehee!"
                show boruto angry with dissolve
                show himaschoolt:
                    easein 1 xalign 0.6
                him"See you around, loser!"
                show himaschoolt:
                    easeout 1 xpos -200
                him"And stop staring!"
                jump himaintro_smenu
                
                

            
        
$ renpy.end_replay()
jump action_taken