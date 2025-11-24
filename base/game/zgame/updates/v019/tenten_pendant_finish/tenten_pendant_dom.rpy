# This file handles the scenario where Boruto extorts Tenten using her pendant on the Dominance path.

label tenten_pendant_dom:
    $ initialize_replay_defaults()
    show boruto snob at right with dissolve
    bo "I mean, if it's as important as you say..."
    bo "Perhaps... you could repay me in a different way."
    stop music
    $ renpy.sound.play("/audio/soun_fx/bassstart.opus",channel="sfx1",loop=False,relative_volume=0.5)
    $ renpy.sound.play("/audio/soun_fx/introbass3.opus",channel="sfx2",loop=True,relative_volume=0.7)
    scene tenten_pendantdangle1
    show pendant_anim
    with dissolve
    ten "W-what are you implying? A different kind of repayment?"
    jump tenten_extortion_menu_loop

label tenten_extortion_menu_loop:

    # Display the menu only if there are still options left
    menu tenten_extortion_demand:

        # Only show this option if it hasn't been chosen yet
        "Money." if not tenten_asked_money:
            bo "Maybe toss a coin to your favorite customer?"
            show tenten_pendantdangle_face with dissolve
            ten "I... I don't have that kind of money!"
            "She struggles to come up with something."
            call changeMoney(20) from _call_changeMoney_19 
            ten "There, that's all I can afford right now."
            ten "You know that since the war, business hasn't been exactly thriving..."
            menu:
                "Oh, Tenten..."
                "Return the money":
                    call changeMoney(-20) from _call_changeMoney_20
                    bo "I'm not here to rob you!"
                    bo "What kind of person do you think I am?"
                    hide tenten_pendantdangle_face with dissolve
                    bo "Wouldn't want to make things more difficult for you. There's other ways you can repay me, you know..."
                    ten "H-huh? T-thanks I suppose..."
                "I'm afraid that won't do":
                    bo "While I appreciate the gesture..."
                    bo "...I'm afraid a small 'repayment' such as this isn't what I had in mind."
                    bo "I am going to need a little something more... enticing..."
            $ tenten_asked_money = True

        # Only show this option if it hasn't been chosen yet
        "I want information." if not tenten_asked_info:
            bo "What's the real reason this is so important to you?"
            ten "I... I can't tell you! It's family business!"
            bo "Right. Then surely you have something else in mind for me..."
            $ tenten_asked_info = True

    # --- Check if all options have been selected and show last chance message if not ---
    if not (tenten_asked_money and tenten_asked_info):
        bo "Surely there's something you can think of... to repay my kind efforts..."

    if tenten_asked_money and tenten_asked_info:
        # Both options selected, set the combined flag (optional) and proceed
        $ tenten_all_options_exhausted = True
        jump tenten_final_demand_section
    else:
        jump tenten_extortion_menu_loop

label tenten_final_demand_section:
    bo "Come on Tenten... You said you'd do anything, didn't you? You haven't even made an effort to offer something yet."
    scene tenten_pendantdangle1_1
    show pendant_anim
    with dissolve
    ten "Uhm, w-well... I've seen how you've been staring at me..."
    ten "Not to mention your insistence on t-touching where you shouldn't!"
    ten "But maybe, just this once, I could show you s-something that interests you?"
    bo "That's more like it! Finally we're on the same page..."
    ten "I... I appreciate you finding it more than I can say, [bo_name]. Really. Although you should know, this is not what I had in mind when I said I'd do anything..."
    scene black with dissolve
    bo "Whatever you say miss!"
    show tenten_pendantdangle1_2 with dissolve
    bo "But first, we better close shop for now. Don't want our important deal to be interrupted by outsiders, do we?"
    "She nods curtly, her shoulders slumped as she walks stiffly to the door..."
    $ renpy.sound.play("/audio/soun_fx/lockdoor.opus", channel="sfx3", loop=False, relative_volume = 1)
    scene black with vpunch
    ten"Don't push your luck just because I'm compliant... y-you got it?"
    show tenten_pendantdangle1_3 with dissolve
    show tenten_pendantdangle1_3:
        easein 4 yalign 0.1
    "She returns, standing awkwardly, not sure where or how to begin."

    ten"And if you don't return my pendant by the end of this... c-charade, then-"
    jump tenten_extort_get_closer_dom

label tenten_extort_get_closer_dom:
    bo"Come on Tenten, you don't really think I am that kind of man, do you?" with vpunch
    bo "I swear, you'll have your pendant. All I ask is but a moment, to appreciate your..."
    bo"Radiant beauty! Will you step a little closer for me?"
    call showscrollingimage from _call_showscrollingimage_156
    show screen parallax1280("tenten_pendantdangle1_3",1.25,0.4) with dissolve
    "She complies silently, taking hesitant steps until she's just out of arm's reach, her eyes looking away."
    ten "...What now?"
    bo "Come on, you're a smart woman, you said you could show me something that would interest me. Surprise me!"
    jump tenten_extort_undress_start_dom

label tenten_extort_undress_start_dom:

    ten "This is indecent..."
    show screen parallax1280("blackscreen",1.25,0.4) with dissolve
    "Her hands slowly reach for the clasps or buttons of her top." 
    "Each movement is hesitant, yet she's reassured, thinking that this'll be the last of your wants..."
    $ renpy.sound.play("/audio/soun_fx/clothes_undress.opus", channel="sfx3", loop=False, relative_volume = 0.7)
    show screen parallax1280("tenten_pendantdangle1_4",1.25,0.3) with dissolve
    ten"C-come on... Y-you are just a kid! Don't you have better things to look at?"
    call increaselust(10) from _call_increaselust_232
    bo"Nothing better than your bare breasts at least!"
    bo "Come on, move your hands away..."
    show screen parallax1280("tenten_pendantdangle1_5",1.25,0.4) with dissolve
    ten"G-good lords! Is this e-enough?"
    bo "Keep going...."
    ten"M-more!?" with vpunch
    menu tenten_extort_undress_options_dom:
        ten"M-more!?"

        "Comment on her body":
            bo "You take good care of yourself, Tenten. Impressive. Now, let's see the rest."
            "She stiffens slightly at the compliment, unsure how to react..."
            ten "Are you satisfied yet?"
            bo"Not quite..."

        "{color=[dominancecolor]}Touch her{/color}" if dominance >= 10:
            bo "Allow me..."
            ten"Huh?"
            show screen parallax1280("tenten_pendantdangle1_5touch",1.25,0.4) with dissolve
            call changeDominance(1) from _call_changeDominance_111
            ten"H-hey! Who said you can-" with vpunch
            "You reach out smoothly, your fingers deliberately brushing against the bare skin of her waist pushing her dress's thigh slit upwards, almost exposing the rest of her..."
            show screen parallax1280("tenten_pendantdangle1_5",1.25,0.4) with dissolve
            ten "Hands off! I can undress m-myself!" with vpunch
            bo "Playing hard to get? Or are you actually teasing me too now?"
            ten "The deal was that you sit and watch! You can keep your hands to yourself..."
            call increaselust(10) from _call_increaselust_233
            bo"We'll see about that. Go on then..."

        "Stay silent and watch":
            bot"Watching her bend to my will, fulfilling her end of the bargain... I enjoy this feeling of control over her!"
            call increaselust(10) from _call_increaselust_234
            ten"..."
            bo"..."
            ten"S-so...?"
            bo"..."
            ten"Y-you want to see m-more of me... I take it then?"

    show screen parallax1280("tenten_pendantdangle1_6",1.25,0.4) with dissolve
    ten"This will be the end of it. R-right...?"
    bo "Perhaps... Come on. Your dress is barely hanging on. Let it drop, Tenten..."

    $ renpy.sound.play("/audio/soun_fx/clothes_undress.opus", channel="sfx3", loop=False, relative_volume = 0.7)
    scene black
    hide screen parallax1280 with dissolve
    "Tenten hesitantly lifts one foot after the other, letting the dress slide down across her legs and dropping on the floor..."
    show screen parallax1280("tenten_pendantdangle1_7",1.25,1.0) with dissolve
    "She lays in front of you completely bare. Her hands scrambling to hide as much as they could..."
    ten"..."
    bo"Beautiful..."
    ten "E-enjoying yourself?"
    bo"How could I not, when you look as radiant as you do..."
    ten"T-thanks, I s-suppose? But this is wholly uncomfortable..."
    ten"Can i dress now p-please?"
    bo"There's one more thing Tenten. I promise you, I'll return your pendant just as soon as you solve a problem of mine, just as I have solved yours."
    bo"Think you can do that for me?" 
    ten "C-come on [bo_name]! I t-thought this would be the end of it!"
    bo"One last favor, Tenten. I swear..."
    ten"Go on t-then. I'll hear you out. Only because you'll return my pendant..."
    bo"You have to understand, Tenten. Every time I've walked into your shop I was stricken by your beauty..."
    ten"Can you s-spare me the compliments, please? This is quickly becoming even more uncomfortable!"
    bo"The real problem lies within me. A c-curse..."
    ten"W-what are you talking about, [bo_name]..."
    ten"You said there's one m-more thing you needed from me. Get on w-with it please..."
    scene black
    call hidescrollingimage2("Click twice to reveal your 'problem'...") from _call_hidescrollingimage2_111
    bo"I need you to..."
    show tenten_pendantdangle1_8 with dissolve
    bo"Take care of my own problem..." with vpunch
    show tenten_pendantdangle1_8:
        easein 0.2 yalign 0.1
    ten"*Gasps*!" with vpunch
    ten"Good l-lords! Are you s-serious?"
    ten"That is way out of line!" with vpunch

    jump tenten_extort_bj_start_dom

label tenten_extort_bj_start_dom:
    bo"I wasn't lying Tenten, about my curse..."
    bo"If I don't find ways to settle my urges, I quickly lose control, I turn violent..."
    ten "I... I don't know if I can do that, [bo_name]... I said I'd show you, not-"
    show tenten_pendantdangle1_8:
        easein 0.2 yalign 1.0
    ten"B-besides, can you not take care of your 'problem' your self?" with vpunch
    bo"I wish it were that easy..."
    show tenten_pendantdangle1_8:
        easein 3.2 yalign 0.0
    bo "Come on Tenten. I went through a lot of trouble to get that pendant, you know. This will be the last of my asks, I swear..."
    ten"B-but, y-y-y-you said before the old weirdo just gave it to you!" with vpunch
    bot"I am f-fucking stupid, aren't I..."
    scene tenten_pendantdangle1_8 with dissolve:
        zoom 1.2 xalign 0.5 yalign 0.1
    bo"S-sort of, but still. An equivalent exchange. You'll solve my problem, I'll solve yours..."
    scene black with dissolve
    "Tenten laid motionless for a minute, lost in her thoughts..."
    $ renpy.sound.play("/audio/soun_fx/clothes_undress.opus", channel="sfx3", loop=False, relative_volume = 0.7)
    "You took the opportunity to get yourself comfortable by getting rid of your own garments..."
    scene tenten_pendantdangle1_8 with dissolve:
        zoom 1.5 xalign 0.6 yalign 1.0
    show tenten_pendantdangle1_8:
        easein 5 yalign 0.1
    "She finally snapped out of her contemplation, and looked at you before saying..."
    ten"...You p-promise, right?"
    bo"I am a man of my word!"
    scene black with dissolve
    ten"Then..."
    "Slowly, hesitantly, she lowered her head down towards your groin."
    show tenten_ext_bj_start with dissolve:
        xalign 0.1 zoom 0.57
    ten"Let's get this over with..."
    bot"On her knees, huh?"
    bo"A mature lady like yourself... You know what to do, right?"
    ten"I prefer you s-stay silent. In return..."
    show tenten_ext_bj_start:
        alpha 0.2
    show tenten_ext_bj1:
        xalign 0.9 zoom 0.57
    with dissolve
    ten"All it'll take is but a m-moment to take care of this."
    $ renpy.sound.play("/audio/soun_fx/lickpenis1.opus", channel="sfx3", loop=False, relative_volume = 1.0) 
    bo"Good girl..."
    show tenten_ext_bj1_1:
        xalign 0.1 zoom 0.57
    show tenten_ext_bj1:
        alpha 0.2
    with dissolve
    ten"!" with vpunch

    "She looked back at you after your comment as if to silence you, but..."
    scene black
    show tenten_ext_bj1_1:
        xalign 0.1 alpha 0.2 zoom 0.57
    show tenten_extort_bj_anim1:
        xalign 0.9 zoom 0.57
    with dissolve
    $ renpy.sound.play("/audio/soun_fx/lickpenis1.opus", channel="sfx3", loop=False, relative_volume = 1.0) 
    "She didn't stop there..."
    bo"O-oh, F-fuck! Keep that going..."
    menu tenten_extort_bj_options_dom:
        bot"Watching her service me out of obligation... It's a nice feeling."

        "{color=[hatredcolor]}Force her deeper!{/color}":# (supporter_scene = True)
            call checkHatred(25, "tenten_extort_bj_options_dom") from _call_checkHatred_24
            jump tenten_forceherdeeper
            # $ call_label_action("tenten_forceherdeeper")
            call supp_rew from _call_supp_rew_6
            jump tenten_extort_bj_options_dom
            show tenten_ext_bj1_pat with dissolve:
                xalign 0.9 zoom 0.57
            bo"Hey Tenten..."
            "She pauses for a second and looks up to you..."
            bo"I am getting kinda bored of your sloppy mouth work..."
            scene black
            show tenten_ext_bj1_push_glare:
                xalign 0.1 zoom 0.57
            with dissolve
            "Her look quickly changes into a defiant glare..."
            bo "Oh, Tenten. Don't look at me like that. You know this isn't over until I climax..." with vpunch
            ten"...!" with vpunch
            bo"And at this rate..."
            show tenten_ext_bj1_push:
                xalign 0.9 zoom 0.57 
            show tenten_ext_bj1_push_glare:
                alpha 0.2
            $ renpy.sound.play("/audio/soun_fx/hima_gag.opus", channel="sfx3", loop=False, relative_volume = 1.0)
            with dissolve
            ten "Mmph!!" with vpunch 
            bo"That's going to take forever!" with vpunch
            $ renpy.sound.play("/audio/soun_fx/gags/SDTGag23.opus", channel="sfx3", loop=False, relative_volume = 0.8)
            "You placed your hand firmly on the back of her head and pushed hard, forcing almost the entire shaft into her mouth..."with vpunch
            bo"In fact, If you aren't going to put that mouth of yours to proper work..."
            show tenten_ext_bj2:
                xalign 0.1 zoom 0.57
            show tenten_ext_bj1_push:
                alpha 0.2
            with dissolve
            $ renpy.sound.play("/audio/soun_fx/gags/SDTGag24.opus", channel="sfx3", loop=False, relative_volume = 1.0)
            bo"Then I'll have to do it myself!" with vpunch
            "Her glare grew more ominous than before, but that didn't deter you, in fact..."
            bo"When you look at me like that..."
            show tenten_extort_bj_anim2 with dissolve:
                xalign 0.1 zoom 0.57
            $ renpy.sound.play("/audio/soun_fx/gluck1.opus", channel="sfx3", loop=False, relative_volume = 1.6)
            "You grabbed each of her hair buns and started using them to push her head down on your cock..."
            bot"Atta girl! Now that's how you please your master!" with vpunch
            ten"Mhhm! *Choking Sounds*" with vpunch 
            bo"I am sure you have things you want to say to me..."
            bo"Too bad your mouth is occupied, eh?"
            bo"But I think you can do even better than this..."
            menu:
                bo"But I think you can do even better than this..."
                "{color=[hatredcolor]}Fuck her face harder!{/color}":
                    pass
                
            show tenten_extort_bj_anim2_1 with dissolve:
                xalign 0.1 zoom 0.57
            $ renpy.sound.play("/audio/soun_fx/gluck2.opus", channel="sfx3", loop=False, relative_volume = 1.6)
            call changeHatred(2) from _call_changeHatred_159
            "You start maniacally thrusting into her mouth, while simultaneously pushing her head harder and harder on to you!"
            bo"F-fuck... Tenten! Now t-this is what I call a s-service..." with flash 
            bo"Hang in there f-for me! Just a l-little more..."

            jump badending_tenten_extort_climax_dom

        "Tell her she's doing a good job":
            show tenten_ext_bj1_pat with dissolve:
                xalign 0.9 zoom 0.57
            "You gently pat her head, reassuring her to keep going..."
            bo "See? You are doing g-great, Tenten. *Moans Softly* K-keep it up..." 
            hide tenten_ext_bj1_pat with dissolve

            $ renpy.sound.play("/audio/soun_fx/bj3.opus", channel="sfx3", loop=False, relative_volume = 0.9)
            "She meets your eyes briefly with a glare..."
            menu randomtentenmenu32928:
                bot"Oh Tenten, that look of yours..."
                "{color=[hatredcolor]}Force her deeper!{/color}":# (supporter_scene = True)
                    call checkHatred(25, "randomtentenmenu32928") from _call_checkHatred_25
                    bot"It awakened something in me!"
                    jump tenten_forceherdeeper
                    # $ call_label_action("tenten_forceherdeeper")
                    call supp_rew from _call_supp_rew_7
                    jump randomtentenmenu32928
                "It's kinda cute...": 
                    bo "You know, when you look at me like that..."
                    bo "You look kinda cute, really!"
                    bo "Makes me want to keep you like this..."
                    $ renpy.sound.play("/audio/soun_fx/gags/SDTGag12.opus", channel="sfx3", loop=False, relative_volume = 0.9)
                    ten "*Gargling sounds*"
                    $ renpy.sound.play("/audio/soun_fx/gluck1.opus", channel="sfx3", loop=False, relative_volume = 1.44)
                    bo "Oh? I'm glad we both agree!"
                    bo"Look at you going at it..."
                    bo "Tenten... I think I may be falling for you!"
                    jump tenten_extort_climax_dom
                

        "Just enjoy it":
            $ renpy.sound.play("/audio/soun_fx/suck2.opus", channel="sfx3", loop=False, relative_volume = 1.0)
            bot"F-fuck! She is not half bad. Her technique is sloppy, but looking her sit there with her hands between her legs, working her m-mouth around my cock..."
            bot"She is extremely arousing. I can't h-hold on much longer..."
            $ renpy.sound.play("/audio/soun_fx/gluck1.opus", channel="sfx3", loop=False, relative_volume = 1.6)
            "Tenten continues her hesitant work, getting slightly less awkward with each passing moment." with vpunch
            bot "She's... actually trying!? Or just desperate to get this over with? Either way..." with vpunch
            bot"I can't hold on much longer!"
            bo "T-Tenten... I am c-close..." with flash
            $ renpy.sound.play("/audio/soun_fx/gags/SDTGag12.opus", channel="sfx3", loop=False, relative_volume = 1.0)
            "She flinches but keeps going, her lips moving a bit more deliberately around you."
            bot "I am a-about to..."
            $ renpy.sound.play("/audio/soun_fx/gags/SDTGag21.opus", channel="sfx3", loop=False, relative_volume = 1.0)
            bo "Ngh... Tenten... w-wait-!" with vpunch
            show tenten_ext_cum1 with flash:
                xalign 0.9 zoom 0.57
            $ renpy.sound.play("/audio/soun_fx/throatcum.opus", channel="sfx2", loop=False, relative_volume = 0.6)
            call decreaselust(100) from _call_decreaselust_111
            "Before she can react, you erupt inside her mouth, your release flooding her senses."
            show tenten_ext_cum1_1 with dissolve:
                xalign 0.9 zoom 0.57
            $ renpy.sound.play("/audio/soun_fx/gags/SDTGag10.opus", channel="sfx2", loop=False, relative_volume = 0.6)
            ten "*Gag!* Mmph!" with vpunch
            show tenten_ext_cum2 with dissolve:
                xalign 0.9 zoom 0.57
            $ renpy.sound.play("/audio/soun_fx/gags/SDTGag16.opus", channel="sfx2", loop=False, relative_volume = 0.6)
            "Her mouth overflows with cum, strings of semen running from her nose as she coughs."
            "Undeterred, she reaches for your cock with one of her hands, making sure to finish the job..."
            bot "F-fuck! She's t-taking it all!"
            scene black with Dissolve(1)           
            show tenten_ext_cum3 with dissolve:
                subpixel True 
                xalign 0.5 zoom 1 yalign 0.9
            show tenten_ext_cum3:
                subpixel True 
                ease 4 yalign 0.3
            "She finally pulls back and looks up to you with a strange look on her face..."
            bo"S-sorry, I couldn't react in time..."
            ten"*Heavy breathing*"
            "Tenten sat there silently for what seemed to be some time, taking slow, deep breaths..."
            bo "Ten...ten?"
            show tenten_ext_cum3_1 with dissolve:
                yalign 0.25 xalign 0.5
            $ renpy.sound.play("/audio/soun_fx/swallow.opus", channel="sfx3", loop=False, relative_volume = 1.4)

            ten"O-oh! *Swallows* We are d-done here, aren't we?" with vpunch
            bo "Did you just... swallow my entire load?"
            ten "W-what!? No! That's d-disgusting..." with vpunch
            bo "Couldn't ask for a better reward. Thanks, Tenten. You drained my balls like a succubus!"
            jump tenten_extort_aftermath_dom
            


label tenten_extort_climax_dom:
    
    bot "She's been surprisingly compliant!"
    bo "My c-condition... Your generous assistance, it's h-helping..."
    menu tenten_extort_climax_location_dom:
        bo "I am c-close... Don't stop now!"
        "Cum in her mouth":
            bo"In fact, I don't think I can-" with flash
            $ renpy.sound.play("/audio/soun_fx/throatcum.opus", channel="sfx3", loop=False, relative_volume = 0.6)
            $ renpy.sound.play("/audio/soun_fx/gags/SDTGag19.opus", channel="sfx1", loop=False, relative_volume = 0.9)
            show tenten_ext_cum1_1 with longerflash:
                xalign 0.9 zoom 0.57
            call decreaselust(50) from _call_decreaselust_112
            "Before she can react, you erupt inside her mouth, your release flooding her senses."
            $ renpy.sound.play("/audio/soun_fx/gags/SDTGag1.opus", channel="sfx1", loop=False, relative_volume = 0.6)
            ten "*Gag!* Mmph!" with flash
            $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx3", loop=False, relative_volume = 0.6)
            show tenten_ext_cum1 with flash:
                xalign 0.9 zoom 0.57
            $ renpy.sound.play("/audio/soun_fx/gags/SDTGag14.opus", channel="sfx1", loop=False, relative_volume = 0.9)
            "Enough of your semen pooled inside her mouth, it started shooting out of her nose!"
            show tenten_ext_cum2 with dissolve:
                xalign 0.9 zoom 0.57
            $ renpy.sound.play("/audio/soun_fx/gags/SDTGag16.opus", channel="sfx1", loop=False, relative_volume = 0.6)
            call decreaselust(50) from _call_decreaselust_113
            "Undeterred, she reaches for your cock with one of her hands, making sure to finish the job..."
            bot "Damn, she's holding it all in!"
            "She coughs and gags, struggling to contain your load in her mouth..."
            menu tenten_swallow_choice_dom:
                "She coughs and gags, struggling to contain your load in her mouth..."
                "Finish the job!":
                    bo "Swallow it, Tenten. You can do it!"
                    scene black with dissolve
                    $ renpy.sound.play("/audio/soun_fx/swallow.opus", channel="sfx3", loop=False, relative_volume = 1.4)
                    "She hesitantly swallows the entire load."
                    show tenten_ext_cum3_1 with dissolve:
                        yalign 0.5 xalign 0.5 zoom 1.25
                    pause(0.3)
                    show tenten_ext_cum3_1 with dissolve:
                        subpixel True 
                        ease 2.5 yalign 0.2
                    bo"Did you really swallow all that...?"
                    show tenten_ext_cum3_1:
                        easein 0.2 yalign 0.55
                    ten"N-no...?" with vpunch
                    bo"You really did... Can I see?"
                    ten"..."
                    "She glares at you silently for a while, but..."
                    show tenten_ext_cum3 with dissolve:
                        yalign 0.55 xalign 0.5 zoom 1.25
                    bo"Impressive! How I wish I could just keep admiring you forever..."
                    hide tenten_ext_cum3 with dissolve
                    ten"Enough! W-we are done here, are we not?" with vpunch
                    bo"Of course. You gave more than I asked for too!"
                    jump tenten_extort_aftermath_dom

                "Spit it out!":
                    scene black with dissolve
                    $ renpy.sound.play("/audio/soun_fx/spit2.opus", channel="sfx3", loop=False, relative_volume = 0.8)
                    ten "*HAWK TUAH!*"
                    $ renpy.sound.play("/audio/soun_fx/gags/SDTGag16.opus", channel="sfx1", loop=False, relative_volume = 0.6)
                    show tenten_ext_bj_forcespit2 with dissolve:
                        zoom 1.3 xalign 0.5 yalign 0.0
                    show tenten_ext_bj_forcespit2:
                        easein 3 yalign 1.0
                    "She makes a mess of spit and cum on the floor."
                    bo "Wasteful, but I do suppose you've delivered on my ask!"
                    ten"*Glares angrily* ..."
                    jump tenten_extort_aftermath_dom

        "Pull out and cum on her face":
            scene black with dissolve
            "You suddenly pull out and take aim towards her..."
            bo"It's c-coming out!"
            ten"H-hey! W-where are y-"
            $ renpy.sound.stop(channel="sfx1")
            $ renpy.sound.stop(channel="sfx2")
            $ renpy.sound.stop(channel="sfx3")
            $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.6)
            scene black
            show tenten_ext_cum4face1:
                xalign 0.1 zoom 0.57
            with flash
            call decreaselust(30) from _call_decreaselust_114
            bo"A-aah! *Moans*..."
            ten"Not on my f-face, you-" with vpunch
            show tenten_ext_cum4face1:
                alpha 0.2
            $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx2", loop=False, relative_volume = 0.6)
            show tenten_ext_cum4face1_1 with flash:
                xalign 0.9  zoom 0.57
            "You pull out just in time, spraying your release across her face. She flinches violently, reflexively screwing one of her eyes shut."
            call decreaselust(30) from _call_decreaselust_115
            "It takes her a moment to realize what just happened, before she..."
            $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.6)
            show tenten_ext_cum4face1_1:
                alpha 0.1
            show tenten_ext_cum4face1:
                alpha 0.1
            show tenten_ext_cum4face1_2:
                xalign 0.5 zoom 0.57
            with longerflash
            call decreaselust(50) from _call_decreaselust_116
            "You erupt violently, spraying your release across her face. She flinches reflexively, sealing one of her eyes shut."
            scene black
            show tenten_ext_cum4face1_2:
                zoom 1.2 xalign 0.5 yalign 1.0

            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp3.opus", channel="sfx2", loop=False, relative_volume = 0.6)
            show tenten_ext_cum4face1_2:
                easein 5 yalign 0.2
            ten "*Gasps*" with vpunch
            ten "W-what did you just d-do, you f-freak!" with hpunch
            show tenten_ext_cum4face1_2 with dissolve:
                ease 5 xalign 0.5 yalign 0.5 zoom 1.25
            bo "You were just... too pretty, I couldn't hold it in any longer!"
            ten "So you just cum all over my f-face?!" with vpunch
            show tenten_ext_cum4face1 with dissolve:
                xalign 0.5 yalign 0.3 zoom 1.35  
            bo "Now now, calm down... It's not that bad is it?"
            ten "Y-yes it is! Idiot..."
            ten"You could at least w-warn me!"
            bo "Yeah well, surprises are fun, aren't they?"

        "Pull out and cum on her body":
            scene black with dissolve
            "You pull back, aiming downwards towards her chest."
            show tenten_ext_cum4:
                xalign 0.5 yalign 0.7 zoom 1
            show tenten_ext_cum4 with flash:
                subpixel True
                ease 3 xalign 0.5 yalign 0.3 zoom 1
            bo "Stay right there... I'm so close!"
            ten "Y-you better be careful where you-"
            $ renpy.sound.stop(channel="sfx1")
            $ renpy.sound.stop(channel="sfx2")
            $ renpy.sound.stop(channel="sfx3")
            $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.6)
            scene black
            show tenten_ext_cum4_1:
                xalign 0.1 zoom 0.57
            with flash
            ten "H-hey! You almost hit m-my face with it, idiot!"
            bo "I'm... I'm not d-done yet..."
            $ renpy.sound.play("/audio/soun_fx/cum4.opus", channel="sfx2", loop=False, relative_volume = 0.6)
            show tenten_ext_cum4_2:
                xalign 0.9 zoom 0.57
            show tenten_ext_cum4_1:
                alpha 0.2
            with longerflash
            call decreaselust(100) from _call_decreaselust_117
            "She flinches, her face flushed red in embarrassment!"
            scene black with dissolve
            show tenten_ext_cum4_2:
                zoom 1.2 xalign 0.5 yalign 0.0
            show tenten_ext_cum4_2:
                easein 4 yalign 0.7
            bo"*Heavy breathing*"
            ten "W-what the... W-who's gonna clean up all this mess!"
            show tenten_ext_cum4_2:
                easein 4 yalign 0.3
            bo "Consider yourself lucky. I could have covered your pretty face instead..."
            bo "You should probably get yourself cleaned and dressed now..."

label tenten_extort_aftermath_dom:
    scene black with dissolve
    call hidescrollingimage2 from _call_hidescrollingimage2_112
    "Tenten scrambles away from you, quickly trying to clean herself up with a nearby cloth, relieved that it's finally over."
    "She takes some time to gather herself and her clothes..."
    show tenten_pendantdangle1_5 with dissolve:
        zoom 1.5 xalign 0.5 yalign 1.0
    show tenten_pendantdangle1_5:
        subpixel True
        easein 9 yalign 0.20
    ten "D-does that... adequately d-demonstrate my g-gratitude?"
    bo "Very much so. You needed a little push but... You kinda liked it too, didn't you?"
    show tenten_pendantdangle1_5:
        easein 0.3 zoom 1.7 yalign 0.3
    bo "I noticed how hard your nipples got..."
    show tenten_pendantdangle1_4 with dissolve:
        zoom 1.7 yalign 0.3 xalign 0.5
    ten "N-no! I did what I h-had to... For m-my... Parents!"
    bo "So what are you still standing there half naked for... primal instinct?"
    bo "Feel free to dress up. You did well!"
    scene black with dissolve
    "Lost for words, she didn't realize she was still subconsciously flaunting her curves."
    show tenten_pendantdangle1_3 with dissolve:
        zoom 1.25 xalign 0.5 yalign 0.8
    show tenten_pendantdangle1_3:
        easein 2 zoom 1.25 yalign 0.2
    "Embarrassed at the realization, she quickly pulls her dress up."
    ten "Y-you are really pushing the line, you know that?"
    bo "Come on Tenten, don't be so uptight!"
    bo "You know I'm just teasing you."
    bo "And as a man of my word, here's the pendant. You've earned it!"
    scene tenten_pendantdangle1
    show pendand_dangle_middle
    with dissolve
    "You proudly hand the pendant over to her."
    scene black with dissolve
    ten "{size=-4}*Mutters Silently* Damn brat...{/size}"
    ten "{size=-4}He thinks he can just boss me around and manipulate me?{/size}"
    bo "What was that?"
    ten "N-nothing, leave me be please!"
    "Trying not to push your luck, you make your way out."
    "Some time passes..."
    scene tenten_extort_ending with dissolve
    ten"At least I got you two back... *Tearing up*"
    ten"It was worth all the effort. Mother, father..."
    scene black with dissolve
    jump tenten_extort_leave_dom

label tenten_extort_leave_dom:
    stop sfx2 fadeout 2
    $ tenten_extorted = True
    $ tenten_pendant_returned = True
    if quest.exists("shop1_3"):
        if quest.is_state("shop1_3", "in progress"):
            $ quest.check("shop1_3", "completed")
            $ notification("Objective Completed: Find the shopkeeper's keepsake")

    scene black with dissolve
    $ renpy.end_replay()
    pause 1
    jump action_taken


label badending_tenten_extort_climax_dom:
    bo"A-ahrh! That look of yours is k-killing me, Tenten!" with flash
    bo"How can I resist f-filling your throat up!"
    menu:
        bo"How can I resist f-filling your throat up!"
        "{color=[hatredcolor]}Fill her throat!{/color}":
            pass
    bo"There's just no w-way I can't..."
    show tenten_ext_forcecum1 with dissolve:
        xalign 0.1 zoom 0.57
    $ renpy.sound.play("/audio/soun_fx/gags/SDTGag20.opus", channel="sfx3", loop=False, relative_volume = 1.0)
    bo"N-not when you are looking at me like t-that.." with flash
    "Your knees give in, bending down just before you explode. You dragged Tenten down with you..."
    "She braces herself on all fours, as you keep pushing on to her head, forcing her down on you..."
    $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
    $ renpy.sound.play("/audio/soun_fx/gags/SDTGag21.opus", channel="sfx1", loop=False, relative_volume = 1.0)
    bo"You'll... Take it like a c-champion, won't you? *Moans*" with flash
    $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx3", loop=False, relative_volume = 0.7)
    $ renpy.sound.play("/audio/soun_fx/gluckfinish.opus", channel="sfx1", loop=False, relative_volume = 1.0)
    show tenten_ext_forcecum1_1 with longerflash:
        xalign 0.1 zoom 0.57
    $ renpy.sound.play("/audio/soun_fx/cum2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
    bo"Aagh! *Loud Moans*" with flash
    scene black with dissolve
    show tenten_ext_forcecum1_1 with dissolve:
        zoom 1.5 xalign 0.5 yalign 0.0
    show tenten_ext_forcecum1_1:
        easein 6 yalign 0.9
    bo"T-there, there... *Heavy breathing*"
    bo"Wasn't so hard, w-was it...?"
    scene black with vpunch
    $ renpy.sound.play("/audio/soun_fx/gags/SDTGag18.opus", channel="sfx1", loop=False, relative_volume = 1.0)
    "You suddenly pull out of her mouth and let go of her head, causing Tenten to lose balance and fall forward..."
    scene tenten_ext_bj_forcespit1 with dissolve
    "Sprouting out of her nose, her mouth, Tenten spits out as much of your fluids as she could, before she angrily turns to address you..."
    ten"*Cough cough* Y-you b-bastard..."
    bo"Aww, come on Tenten... Don't look at me like that."
    bo"You knew what you were getting yourself into, did you not? I thought I made the implications pretty clear..."
    scene black with vpunch
    ten"*Cough cough*!" with vpunch
    show tenten_ext_bj_forcespit2 with dissolve
    ten"T-that... *Cough* wasn't..."
    ten"Our a-agreement!"
    ten"Give me my pendant and get the hell out of here, y-you creep!" with vpunch
    bo"As you wish!"
    scene black with vpunch
    bo"And thank you for your service!"
    "You drop the pendant next to Tenten, before you dress back up and leave her shop..."
    "Tenten takes some time to gather herself..."
    show tenten_pendantdangle1_6 with dissolve:
        zoom 1.5 xalign 0.5 yalign 1.0
    show tenten_pendantdangle1_6:
        subpixel True
        easein 9 yalign 0.5
    ten"Damned brat..."
    ten"He thinks he can just d-do something like that to me?"
    ten"I'll make sure to get back at him somehow..."
    scene black with vpunch
    "Some time passes..."
    scene tenten_extort_ending with dissolve
    ten"At least I got you two back... *Tearing up*"
    ten"It was worth all the effort. Mother, father..."
    scene black with dissolve
    jump tenten_extort_leave_dom
    