# tenten_pendant_extort_hatred.rpy
# This file handles the scenario where Boruto extorts Tenten using her pendant on the Hatred path.

label tenten_pendant_extort_start:
    $ initialize_replay_defaults()
    scene black with dissolve
    "You slowly pull the pendant from your pocket, letting it dangle from your fingers."
    ten "*Gasp!* That's it! That's my pendant! Oh, thank you, [bo_name]! Thank you so-"
    stop music
    $ renpy.sound.play("/audio/soun_fx/bassstart.opus",channel="sfx1",loop=False,relative_volume=0.5)
    $ renpy.sound.play("/audio/soun_fx/introbass3.opus",channel="sfx2",loop=True,relative_volume=0.7)
    scene tenten_pendantdangle1
    show pendant_anim
    hide ten
    hide boruto
    with dissolve
    bo "Not so fast, Tenten."

    ten "W-what? What do you mean?"
    bo "You expect me to just... Give it back? After all the trouble I went through?"
    bo "Don't be stupid, Tenten. You {b}owe{/b} me."
    bo "And that means I own YOU."
    jump tenten_extortion_menu_loop_hatred

label tenten_extortion_menu_loop_hatred:

    # Display the menu only if there are still options left
    menu tenten_extortion_demand_hatred:
        ten "W-what do you want from me, just get this over with!"
        # Only show this option if it hasn't been chosen yet
        "I want your money." if not tenten_asked_money:
            bo "I want your money. Everything you have. I spent tons on your shitty items."
            show tenten_pendantdangle_face with dissolve
            ten "I... I don't have that kind of money!"
            "She reluctantly scrapes together what little cash she has."
            call changeMoney(20) from _call_changeMoney_21
            menu:
                bo "Pathetic!"
                "Throw it back":
                    bo "You think you can wiggle your way out of this with *that*?"
                    bo "Is that how much your stupid trinket is really worth to you?"
                    bo "Or do you just take me for a fool?"
                    ten "Th-that's all I can afford right now!"
                    call changeMoney(-20) from _call_changeMoney_22
                    bo "Spare me your chump change."
                "Keep it":
                    bo "You call that a repayment? I'm offended."
                    ten "Th-that's all I can afford right now!"
                    bo "I'll take it as a down payment but..."
                    bo "You'll have to offer something much better than this scrap."
            $ tenten_asked_money = True
            
        # Only show this option if it hasn't been chosen yet
        "I want information." if not tenten_asked_info:
            bo "Spill it. Why is this junk so important?"
            ten "It's... It's personal! It belonged to my family!"
            bo "Family? Dead weight. Doesn't concern me."
            $ tenten_asked_info = True

    # --- Check if all options have been selected and show last chance message if not ---
    if not (tenten_asked_money and tenten_asked_info):
        "Tick-tock, Tenten. My patience is wearing thin. You said *anything*, didn't you?"

    if tenten_asked_money and tenten_asked_info:
        # Both options selected, set the combined flag (optional) and proceed
        $ tenten_all_options_exhausted = True
        jump tenten_final_demand_section_hatred
    else:
        jump tenten_extortion_menu_loop_hatred

label tenten_final_demand_section_hatred:
    bo "Well in that case, you leave me no other choice. I tried being a gentleman, but you wouldn't budge." 
    bo "Now here's the deal. I want..."
    bo "You, right here, right now."
    scene tenten_pendantdangle1_1
    show pendant_anim
    with dissolve
    ten "Wh-what?! You can't be serious!" with vpunch

    bo "Remember what you said? 'I'd do anything to have my pendant back'?"
    bo "You also JUST mentioned you barely scrape by and money isn't an option..."
    ten "I... I did say that. But what are you getting at?"
    bo "I went through some trouble getting this back. Risked quite a bit, you could say."
    call changeHatred(2, "tenten_extort_threat", 1) from _call_changeHatred_160
    bo "And looking at you now... I'm thinking of a different kind of 'anything'."
    scene tenten_pendantdangle1_1angry
    show pendant_anim
    with dissolve
    ten "You wouldn't dare! After I trusted you? After you pretended to be a friend?" with vpunch
    bo "Friendship doesn't pay the bills, Tenten. And this..."
    
    "You gesture vaguely towards her with a smirk."                                  ###
    bo "...this looks like it could be {i}very{/i} valuable repayment."              ###
    ten "Get out! Get out of my shop right now, you pig!" with hpunch                ###
    bo "Get out? Sure, I'm leaving then. But this little trinket?"
    $ renpy.sound.play("/audio/soun_fx/danglependant.opus", channel="sfx3", loop=False, relative_volume = 0.9)
    "You hold up the pendant again, dangling it mockingly."
    scene tenten_pendantdangle1_1fear
    show pendant_anim
    with dissolve
    bo "Maybe I'll just 'lose' it, you know, accidentally. Permanently."
    $ renpy.sound.play("/audio/soun_fx/growl1.opus", channel="sfx3", loop=False, relative_volume = 0.9)
    show kurama1 with flash:
        alpha 0.5
    show kurama1:
        easein 1.5 alpha 0.0
    bo "Or maybe... Maybe I'll sell it to some pawn shop. Wonder how much I'd get for scrap metal..."
    ten "N-no! Please! You can't! It's all I have left of them!" with vpunch
    ten "*Sniffles* Please, [bo_name]... Don't do this..."
    bo "Then you know what you have to do. Cooperate. Be a {i}good girl{/i} for me, and maybe... just maybe... you'll get your precious memory back."
    $ renpy.sound.play("/audio/soun_fx/woman_crying1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
    "Tears stream down her face as her shoulders slump in defeat. The sass drains out of her, replaced by a hollow fear."
    ten "*Sob*... W-what... what do you want me to do?"
    bot"Heh. Just like that. Broken already. Pathetic! But there may still be a use for you..."
    bo "That's the spirit!" with dissolve
    bo "Now, lock the door. No interruptions. This is between you and me."
    show tenten_pendantdangle1_2 with dissolve
    "Her face pales, but she turns and walks rigidly to the door, the click of the lock echoing in the silence."
    $ renpy.sound.play("/audio/soun_fx/lockdoor.opus", channel="sfx3", loop=False, relative_volume = 1)
    scene black with vpunch
    ten"Don't... don't push your luck! I won't forget this..."
    show tenten_pendantdangle1_3angry with dissolve
    show tenten_pendantdangle1_3angry:
        easein 4 yalign 0.1
    "She returns, standing stiffly, avoiding your gaze, radiating resentment."
    ten"And you will return my pendant when this... degradation... is over. Or else..."
    bo "You think YOU are in a position to be negotiating and making demands right now?"
    bo "You got all of this backwards. I suggest staying quiet until I ask you to talk from now on. 'Or else', as you said."
    jump tenten_extort_get_closer_hatred

label tenten_extort_get_closer_hatred:
    bo "Now... come closer. Don't make me tell you twice."
    "She takes a hesitant step forward, then another, stopping a few feet away, trembling slightly."
    call showscrollingimage from _call_showscrollingimage_157
    show screen parallax1280("tenten_pendantdangle1_3angry2",1.25,0.2) with dissolve
    bo "Such a pretty little thing you are, Tenten!"
    "She forces herself to look up, her eyes glistening with unshed tears and raw resentment..."
    ten "Please... just give it back. Do... do what you want quickly, and give it back."
    bo "Oh, I intend to enjoy this {i}thoroughly{/i}. We're doing this on my terms. And my terms are... I want to see {i}all{/i} of you begging for it."
    bo "So stop playing dumb and start stripping, you know what I want to see."
    jump tenten_extort_undress_start_hatred

label tenten_extort_undress_start_hatred:
    ten "You're disgusting..."
    show screen parallax1280("blackscreen",1.25,0.4) with dissolve
    "Her fingers tremble as they fumble with the fastenings of her top."
    "Every movement is laced with humiliation, her compliance bought solely by the pendant you dangle."
    $ renpy.sound.play("/audio/soun_fx/clothes_undress.opus", channel="sfx3", loop=False, relative_volume = 0.7)
    show screen parallax1280("tenten_pendantdangle1_4",1.25,0.3) with dissolve
    ten"Just... just hurry up and get this over with."
    call increaselust(10) from _call_increaselust_235
    bo"Impatient, are we? Don't rush perfection."
    bo "Hands away. Let me see what you're hiding."
    show screen parallax1280("tenten_pendantdangle1_5",1.25,0.4) with dissolve
    ten"There! Is t-this enough for you, you sicko?"
    bo "It's a start. Keep going."
    ten"What!? There's n-nothing else!" with vpunch
    menu tenten_extort_undress_options_hatred:
        ten"What!? There's n-nothing else!"

        "Comment on her body":
            bo "Not bad, Tenten. For a useless shopkeeper that is!"
            bo"Hurry it up! My patience is wearing thin..."
            "She flinches, visibly recoiling from your words."
            ten "Are you done degrading me yet?"
            bo"We're just getting started."

        "{color=[hatredcolor]}Grope her{/color}" if hatred >= 15:
            bo "Actually let me give you a hand..."
            ten"No!"
            show screen parallax1280("tenten_pendantdangle1_5touch",1.25,0.4) with dissolve
            call changeHatred(1) from _call_changeHatred_161
            ten"Get your filthy hands off m-me!" with vpunch
            "You grab her waist roughly, fingers digging in, yanking the slit of her dress higher, exposing her thigh."
            show screen parallax1280("tenten_pendantdangle1_5",1.25,0.4) with dissolve
            ten "Stop it! I said I'd do it!" with vpunch
            bo "Don't like being touched? Too bad. You belong to me right now."
            ten "Just... just let me do it myself..."
            call increaselust(10) from _call_increaselust_236
            bo"Then act like you mean it before my patience wears thin and I throw your trinket in the trash."

        "Stay silent and watch":
            bot"Just watching her forced to undress like this... knowing I broke her... It's exhilarating."
            call increaselust(10) from _call_increaselust_237
            ten"J-just stare then, you creep..."
            bo"Watch it, Tenten."
            ten"Fine! Fine! You want to see everything, don't you!?"  

    bo "Almost there... Don't keep me waiting."
    $ renpy.sound.play("/audio/soun_fx/clothes_undress.opus", channel="sfx3", loop=False, relative_volume = 0.7)
    show screen parallax1280("tenten_pendantdangle1_6",1.25,0.4) with dissolve
    "She still hesitates to take everything off."
    ten"This... This is the last thing. After this, you give it back. Promise me!"
    bo "Promises are for weaklings. Now drop the dress, slut."
    scene black
    "Terrified of frustrating you further, she hurries up."
    hide screen parallax1280 with dissolve
    $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx1", loop=False, relative_volume = 0.7)
    show screen parallax1280("tenten_pendantdangle1_7",1.25,1.0) with dissolve
    "Finally, she stands before you completely bare, attempting to cover her private parts in a futile attempt to hide her shame."
    ten"..."
    bo"Acceptable."
    ten "N-now give it back! Please!"
    bo"Not yet. You think showing me your body is enough? Pathetic."
    bo"You still owe me. There's one more 'service' you need to perform."
    ten "No! We had a deal! You said-"
    bo"I said you'd do *anything*. And right now, I have a problem only *you* can solve."
    ten "What... what are you talking about?"
    scene black
    call hidescrollingimage2("Click twice to show her exactly what needs servicing...") from _call_hidescrollingimage2_113
    bo"This problem..."
    show tenten_pendantdangle1_8 with dissolve
    bo"Needs your immediate attention." with vpunch
    show tenten_pendantdangle1_8:
        easein 0.2 yalign 0.1
    ten"*Sharp inhale*!" with vpunch
    ten"You... you can't be serious!"
    ten"You animal! That's disgusting!" with vpunch

    jump tenten_extort_bj_start_hatred

label tenten_extort_bj_start_hatred:
    bo"Disgusting? It's payment, Tenten. Your final payment."
    bo"You think I care about your feelings? Get on your knees."
    ten "I... I won't! This wasn't part of the deal!"
    show tenten_pendantdangle1_8:
        easein 0.2 yalign 1.0
    ten"Find some other whore to solve your 'problem'!" with vpunch
    bo"Other whores don't have what I want right now."
    show tenten_pendantdangle1_8:
        easein 3.2 yalign 0.0
    bo "You want this pendant back, or not? Last chance. Kneel, or I crush it right here."
    ten"N-no! Don't!" with vpunch
    bot"Got her. Fear works every time."
    scene tenten_pendantdangle1_8 with dissolve:
        zoom 1.2 xalign 0.5 yalign 0.1
    bo"Then you know what to do. Don't make me repeat myself."
    scene black with dissolve
    "Tenten's face crumples, tears welling in her eyes, but the fear of losing her pendant outweighs her disgust."
    $ renpy.sound.play("/audio/soun_fx/clothes_undress.opus", channel="sfx3", loop=False, relative_volume = 0.7)
    "You strip down completely, letting your clothes fall carelessly to the floor."
    scene tenten_pendantdangle1_8 with dissolve:
        zoom 1.5 xalign 0.6 yalign 1.0
    show tenten_pendantdangle1_8:
        easein 5 yalign 0.1
    "She watches you, paralyzed by dread, before finally lowering herself."
    ten"...Fine."
    bo"That's what I thought."
    scene black with dissolve
    ten"Just... make it quick."
    "She lowers her head towards your erection, hesitating."
    show tenten_ext_bj_start with dissolve:
        xalign 0.1 zoom 0.57
    ten"..."
    bot"Pathetic. Even kneeling, she resists."
    bo"Don't just stare at it, whore. Put your mouth to use."
    ten"Don't call me that!"
    show tenten_ext_bj_start:
        alpha 0.2
    show tenten_ext_bj1:
        xalign 0.9 zoom 0.57
    with dissolve
    ten"Just... shut up."
    $ renpy.sound.play("/audio/soun_fx/lickpenis1.opus", channel="sfx3", loop=False, relative_volume = 1.0)
    bo"Make me."
    show tenten_ext_bj1_1:
        xalign 0.1 zoom 0.57
    show tenten_ext_bj1:
        alpha 0.2
    with dissolve
    ten"!" with vpunch

    "Her glare hardens, but she reluctantly takes the tip into her mouth."
    scene black
    show tenten_ext_bj1_1:
        xalign 0.1 alpha 0.2 zoom 0.57
    show tenten_extort_bj_anim1:
        xalign 0.9 zoom 0.57
    with dissolve
    $ renpy.sound.play("/audio/soun_fx/lickpenis1.opus", channel="sfx3", loop=False, relative_volume = 1.0)
    "Her movements are clumsy, hesitant."
    bo"Is that the best you can do? Pathetic."
    menu tenten_extort_bj_options_hatred:
        bot"Watching her humiliate herself for me... This is exhilarating."

        "{color=[hatredcolor]}Force her deeper!{/color}":# (supporter_scene = True)
            call checkHatred(25, "tenten_extort_bj_options_hatred") from _call_checkHatred_26
            jump tenten_forceherdeeper_hatred
            # $ call_label_action("tenten_forceherdeeper_hatred")
            call supp_rew from _call_supp_rew_8
            jump tenten_extort_bj_options_hatred
            show tenten_ext_bj1_pat with dissolve:
                xalign 0.9 zoom 0.57
            bo"Enough playing around."
            "She flinches, looking up with fear."
            bo"Open wide!"
            scene black
            show tenten_ext_bj1_push_glare:
                xalign 0.1 zoom 0.57
            with dissolve
            $ renpy.sound.play("/audio/soun_fx/gags/SDTGag20.opus", channel="sfx3", loop=False, relative_volume = 1.0)
            "Her defiance is overshadowed by terror."
            bo "Don't test my patience, Tenten. You know what happens if you disobey." with vpunch
            ten"...!" with vpunch
            bo"Now swallow it. All of it."
            show tenten_ext_bj1_push:
                xalign 0.9 zoom 0.57
            show tenten_ext_bj1_push_glare:
                alpha 0.2
            $ renpy.sound.play("/audio/soun_fx/hima_gag.opus", channel="sfx3", loop=False, relative_volume = 1.0)
            with dissolve
            ten "Mmph!!" with vpunch
            bo"That's better. Much better." with vpunch
            "You grip the back of her head, shoving your cock down her throat."
            $ renpy.sound.play("/audio/soun_fx/gags/SDTGag18.opus", channel="sfx3", loop=False, relative_volume = 1.0)
            bo"You want to complain? Go ahead." with vpunch
            show tenten_ext_bj2:
                xalign 0.1 zoom 0.57
            show tenten_ext_bj1_push:
                alpha 0.2
            with dissolve
            $ renpy.sound.play("/audio/soun_fx/gags/SDTGag23.opus", channel="sfx3", loop=False, relative_volume = 1.0)
            bo"Oh, right. Can't talk with your mouth full, can you?" with vpunch
            "Her eyes water, glaring pure hatred, but you revel in her helplessness."
            bo"That look... it only makes me harder."
            show tenten_extort_bj_anim2 with dissolve:
                xalign 0.1 zoom 0.57
            $ renpy.sound.play("/audio/soun_fx/gluck1.opus", channel="sfx3", loop=False, relative_volume = 1.6)
            "You grab her hair buns like handles, fucking her face mercilessly."
            bot"Yeah, take it slut! This is what you get!" with vpunch
            ten"Mhhm! *Choking, gagging sounds*" with vpunch
            bo"Music to my ears!"
            bo"But I think you can take more..."
            menu:
                bo"But I think you can take more..."
                "{color=[hatredcolor]}Fuck her face harder!{/color}":
                    pass

            show tenten_extort_bj_anim2_1 with dissolve:
                xalign 0.1 zoom 0.57
            $ renpy.sound.play("/audio/soun_fx/gluck2.opus", channel="sfx3", loop=False, relative_volume = 1.6)
            call changeHatred(2) from _call_changeHatred_162
            "You increase the pace, slamming into the back of her throat with brutal force."
            bo"F-fuck... Tenten! Yeah, take it! Take all of it, you bitch!" with flash
            bo"Almost there... Don't you dare stop!"

            jump badending_tenten_extort_climax_hatred

        "Tell her she's doing a shitty job":
            show tenten_ext_bj1_pat with dissolve:
                xalign 0.9 zoom 0.57
            "You grab a handful of her hair, yanking her head back slightly."
            bo "Is this supposed to impress me? It feels like a dead fish flopping around."
            hide tenten_ext_bj1_pat with dissolve
            $ renpy.sound.play("/audio/soun_fx/bj3.opus", channel="sfx3", loop=False, relative_volume = 0.9)
            "She glares, tears threatening to spill."
            menu random_tentenmenu_12344832:
                bot"That pathetic look..."
                "{color=[hatredcolor]}Force her deeper!{/color}":# (supporter_scene = True)
                    call checkHatred(25, "random_tentenmenu_12344832") from _call_checkHatred_27
                    jump tenten_forceherdeeper_hatred
                    # $ call_label_action("tenten_forceherdeeper_hatred")
                    call supp_rew from _call_supp_rew_9
                    jump random_tentenmenu_12344832
                    bot"It just pisses me off! Make her work for it."
                    jump tenten_forceherdeeper_hatred
                "Maybe she needs 'motivation'...":
                    bo "You know, the longer you take, the more... creative I might get."
                    bo "Maybe I'll find other uses for that mouth. Or other holes."
                    $ renpy.sound.play("/audio/soun_fx/gags/SDTGag12.opus", channel="sfx3", loop=False, relative_volume = 0.9)
                    ten "*Gagging sounds intensify*"
                    bo "See? You understand. Now do it properly."
                    bo "I might just let you keep the pendant if you satisfy me..."
                    jump tenten_extort_climax_hatred


        "Just enjoy it":
            $ renpy.sound.play("/audio/soun_fx/suck2.opus", channel="sfx3", loop=False, relative_volume = 1.0)
            bot"F-fuck! Even her pathetic attempt feels good. Watching her forced submission..."
            bot"She's so fucking pathetic like this, working her mouth around my cock..."
            bot"The humiliation... I can't get enough. Almost there..."
            $ renpy.sound.play("/audio/soun_fx/bj3.opus", channel="sfx3", loop=False, relative_volume = 1.0)
            "Tenten continues, tears silently streaming down her face."
            bot "She hates this. Good. Her suffering makes it better."
            bo "*Moans* T-Tenten... Faster, slut!"
            $ renpy.sound.play("/audio/soun_fx/gags/SDTGag12.opus", channel="sfx3", loop=False, relative_volume = 0.9)
            "She obeys, choking slightly as she increases the pace."
            bot "Fuuuck... almost there... I am going to fill her throat up!"
            $ renpy.sound.play("/audio/soun_fx/gags/SDTGag21.opus", channel="sfx3", loop=False, relative_volume = 1.0)
            bo "H-here it comes you whore, get ready!"
            show tenten_ext_cum1_1 with flash:
                xalign 0.9 zoom 0.57
            $ renpy.sound.play("/audio/soun_fx/throatcum.opus", channel="sfx2", loop=False, relative_volume = 0.6)
            call decreaselust(100) from _call_decreaselust_118
            "You explode in her mouth, filling her orifices completely, semen pouring out of her mouth and nose alike."
            show tenten_ext_cum1 with dissolve:
                xalign 0.9 zoom 0.57
            $ renpy.sound.play("/audio/soun_fx/gags/SDTGag1.opus", channel="sfx2", loop=False, relative_volume = 0.6)
            ten "*Gag!* Mmph! *Choke*" with vpunch
            show tenten_ext_cum2 with dissolve:
                xalign 0.9 zoom 0.57
            $ renpy.sound.play("/audio/soun_fx/gags/SDTGag16.opus", channel="sfx2", loop=False, relative_volume = 0.6)
            "Semen overflows, dripping down her chin as she gags violently."
            bot "Perfect. Look at the mess you made, Tenten."
            scene black with Dissolve(1)
            show tenten_ext_cum3 with dissolve:
                subpixel True
                xalign 0.5 zoom 1 yalign 0.9
            show tenten_ext_cum3:
                subpixel True
                ease 5 yalign 0.5
            bo"Aww, Sorry! Did I make you choke?"
            bo "Look at you though! Covered in my seed. Suits you."
            "Tenten trembles, eyes shut tight, refusing to look at you."
            
            bo "You can speak now, whore. Or are you still gargling on my sugar-coated cum!"
            scene black with dissolve
            $ renpy.sound.play("/audio/soun_fx/spit2.opus", channel="sfx3", loop=False, relative_volume = 1.4)
            "She spits a thick glob of semen and saliva onto the floor."
            bo "Hey! Did I say you could spit?" with vpunch
            show tenten_ext_bj_forcespit2 with dissolve

            ten "S-Screw you..."
            ten "Are we d-done now!? You got what you wanted!"
            bo "Temper, temper... But I am a man of my word and you did your job adequately!"
            jump tenten_extort_aftermath_hatred



label tenten_extort_climax_hatred:

    bot "She held out longer than I expected."
    bo "My c-curse... it's almost satisfied... Thanks to you..."
    menu tenten_extort_climax_location_hatred:
        bo "Get ready... Here it comes..."

        "Cum in her mouth":
            show tenten_ext_cum1 with flash:
                xalign 0.9 zoom 0.57
            $ renpy.sound.play("/audio/soun_fx/throatcum.opus", channel="sfx2", loop=False, relative_volume = 0.6)
            call decreaselust(100) from _call_decreaselust_119
            "You unleash your load deep into her mouth without warning."
            $ renpy.sound.play("/audio/soun_fx/gags/SDTGag1.opus", channel="sfx2", loop=False, relative_volume = 0.6)
            ten "*Violent Gag!* Mmph!"
            show tenten_ext_cum1_1 with dissolve:
                xalign 0.9 zoom 0.57
            "Semen overflows, dripping from her lips."

            show tenten_ext_cum2 with dissolve:
                xalign 0.9 zoom 0.57
            $ renpy.sound.play("/audio/soun_fx/gags/SDTGag16.opus", channel="sfx2", loop=False, relative_volume = 0.6)
            bot "Look at that mess. Pathetic."
            "She coughs and sputters, trying not to vomit."
            menu tenten_swallow_choice_hatred:
                bot "Now, what to do with the leftovers..."
                "{color=[hatredcolor]}Make her swallow it.{/color}":
                    bo "Swallow it. Every last drop. Now."
                    scene black with dissolve
                    $ renpy.sound.play("/audio/soun_fx/swallow.opus", channel="sfx3", loop=False, relative_volume = 1.4)
                    "Tears stream down her face as she forces herself to swallow."
                    show tenten_ext_cum3_1:
                        yalign 0.5 xalign 0.5 zoom 1.25
                    pause(0.3)
                    show tenten_ext_cum3_1 with dissolve:
                        subpixel True
                        ease 2.5 yalign 0.4 zoom 1
                    bo"Filthy whore! Now open up... Let me inspect your work!"
                    show tenten_ext_cum3 with dissolve:
                        yalign 0.4 xalign 0.5 zoom 1
                    show tenten_ext_cum3:
                        subpixel True
                        ease 3 yalign 0.35 xalign 0.5 zoom 1.25
                    "She opens her mouth slowly, trembling, face flushed with shame."
                    bo"Clean. See? Obedience has its rewards."
                    bo"Now get dressed before I change my mind and decide I need another round."
                    scene black with dissolve
                    "She scrambles to her feet, glaring hatred, but says nothing."
                    jump tenten_extort_aftermath_hatred

                "{color=[hatredcolor]}Make her spit it out.{/color}":
                    bo "Spit it out. Right here on the floor. Like the animal you are."
                    scene black with dissolve
                    $ renpy.sound.play("/audio/soun_fx/spit2.opus", channel="sfx3", loop=False, relative_volume = 0.8)
                    ten "*HAWK TUAH!*"
                    "She spits the mess onto the floor, avoiding your eyes."
                    bo "Disgusting. Now clean it up!"
                    show tenten_ext_bj_forcespit2 with dissolve
                    ten "W-what?!"
                    call changeHatred(1) from _call_changeHatred_163
                    bo "Bwahahaha! Look at that stupid face of yours..."
                    bo"I was just kidding. You fulfilled your end of your bargain you filthy whore!"
                    jump tenten_extort_aftermath_hatred

        "Pull out and cum on her face":
            scene black with dissolve
            $ renpy.sound.stop(channel="sfx1")
            $ renpy.sound.stop(channel="sfx2")
            $ renpy.sound.stop(channel="sfx3")
            $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.6)
            show tenten_ext_cum4face1_2:
                xalign 0.5 yalign 0.7 zoom 1.25
            show tenten_ext_cum4face1_2 with flash:
                subpixel True
                ease 3 xalign 0.5 yalign 0.3 zoom 1.25
            "You yank out at the last second, coating her face in thick ropes of semen. She cries out, eyes squeezed shut."
            call decreaselust(100) from _call_decreaselust_120
            "She trembles, wiping furiously at her face."
            show tenten_ext_cum4face1_1:
                xalign 0.5 yalign 0.3 zoom 1.25
            show tenten_ext_cum4face1_1:
                ease 0.3 xalign 0.5 yalign 0.3 zoom 1.35
            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp3.opus", channel="sfx2", loop=False, relative_volume = 0.6)
            ten "*Choked sob*!" with vpunch
            ten "You... you monster! Get it off me!" with hpunch
            show tenten_ext_cum4face1_2 with dissolve:
                ease 5 xalign 0.5 yalign 0.5 zoom 1.25
            bo "Looks good on you. Adds character."
            ten "I hate you! I hate you!" with vpunch
            show tenten_ext_cum4face1 with dissolve:
                xalign 0.5 yalign 0.3 zoom 1.35
            bo "Your hatred only makes me harder. Now get dressed, whore."
            ten "D-don't call me that!"
            bo "Or what? Going to cry more? Get out."

        "Pull out and cum on her body":
            scene black with dissolve
            "You pull out, aiming for her chest and stomach."
            show tenten_ext_cum4:
                xalign 0.5 yalign 0.7 zoom 1
            show tenten_ext_cum4 with flash:
                subpixel True
                ease 3 xalign 0.5 yalign 0.3 zoom 1
            bo "Hold still... Target practice!"
            ten "N-no! Don't you dare-"
            $ renpy.sound.stop(channel="sfx1")
            $ renpy.sound.stop(channel="sfx2")
            $ renpy.sound.stop(channel="sfx3")
            $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.6)
            show tenten_ext_cum4_1:
                xalign 0.5 yalign 0.7 zoom 1.25
            show tenten_ext_cum4_1 with flash:
                subpixel True
                ease 3 xalign 0.5 yalign 0.3 zoom 1.25
            ten "Ah! Y-you missed my face, you pervert!"
            bo "Did I? Still more coming..."
            $ renpy.sound.play("/audio/soun_fx/cum4.opus", channel="sfx2", loop=False, relative_volume = 0.6)
            scene black
            show tenten_ext_cum4_2 with flash:
                subpixel True
                xalign 0.5 yalign 0.3 zoom 1
            call decreaselust(100) from _call_decreaselust_121
            "She flinches as you cover her torso in your seed."
            ten "Stop it! That's enough! Get off me!"
            bo "Fiiiine, fine, you crybaby."
            bo "Clean yourself up and get dressed. Your payment is complete."

label tenten_extort_aftermath_hatred:
    scene black with dissolve
    call hidescrollingimage2 from _call_hidescrollingimage2_114
    "Tenten scrambles away, wiping herself frantically, her body shaking with a mixture of disgust and fury."
    "She snatches her clothes and dresses quickly, avoiding your gaze."
    show tenten_pendantdangle1_5 with dissolve:
        zoom 1.5 xalign 0.5 yalign 1.0
    show tenten_pendantdangle1_5:
        subpixel True
        easein 9 yalign 0.20
    ten "There. Are you s-satisfied now, you bastard?"
    bo "For now. You performed adequately. Like a good little whore."
    show tenten_pendantdangle1_5:
        easein 0.3 zoom 1.7 yalign 0.3
    bo "Maybe you even liked it a little? Don't lie."
    show tenten_pendantdangle1_4 with dissolve:
        zoom 1.7 yalign 0.3 xalign 0.5
    ten "I despise you! Give me my pendant!"
    bo "Impatient, aren't we? Maybe I should keep it. As a reminder of our time together."
    scene black with dissolve
    "Terror fills her eyes again. She takes a step back."
    show tenten_pendantdangle1_3angry2 with dissolve:
        zoom 1.25 xalign 0.5 yalign 0.8
    show tenten_pendantdangle1_3angry2:
        easein 2 zoom 1.25 yalign 0.2
    ten "You... you promised!"
    bo "Relax. I'm just fucking with you."
    scene tenten_pendantdangle1_1fear
    show pendand_dangle_middle
    with dissolve
    bo "Here. Take your precious junk."
    scene black with vpunch
    "You toss the pendant carelessly at her feet."    
    ten "{size=-4}*Whispering* You'll pay for this... I swear... You'll pay...{/size}"
    bo "What was that? Speak up."
    ten "Get out! Get out of my shop! NOW!" with vpunch
    "You smirk, turning to leave. Her resentment leaves you satisfied for some sick, twisted reason..."
    "Some time passes..."
    scene tenten_extort_ending with dissolve
    ten"At least I got you back... *Sniffles* But at what cost?"
    ten"He... he won't get away with this. Mother, Father. I'll make him pay!"
    scene black with dissolve
    jump tenten_extort_leave_hatred

label tenten_extort_leave_hatred:
    stop sfx2 fadeout 2

    $ tenten_extorted = True
    $ tenten_pendant_returned = True
    
    scene black with dissolve
    if quest.exists("shop1_3"):
        if quest.is_state("shop1_3", "in progress"):
            $ quest.check("shop1_3", "completed")
            $ notification("Objective Completed: Find the shopkeeper's keepsake")
    $ renpy.end_replay()
    pause 1
    jump action_taken


label badending_tenten_extort_climax_hatred:
    bo"A-ahhh! That look... that FEAR! It's driving me insane, Tenten!" with flash
    bo"I'm going to break you!"
    menu:
        bo"I'm going to break you!"
        "{color=[hatredcolor]}Destroy her throat!{/color}":
            pass
    bo"I can't... I can't stop!"
    show tenten_ext_forcecum1 with dissolve:
        xalign 0.1 zoom 0.57
    $ renpy.sound.play("/audio/soun_fx/gags/SDTGag24.opus", channel="sfx3", loop=False, relative_volume = 1.0)
    bo"*Moans*! Take it! Take it ALL!" with flash
    "You lose all control, slamming into her throat with savage intensity, ignoring her choked gags and tears."
    $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx3", loop=False, relative_volume = 0.6)
    $ renpy.sound.play("/audio/soun_fx/gags/SDTGag14.opus", channel="sfx1", loop=False, relative_volume = 1.0)
    bo"Yeah... *Grunts* Like that! Swallow my seed, whore!" with flash
    $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx3", loop=False, relative_volume = 0.9)
    show tenten_ext_forcecum1_1 with longerflash:
        xalign 0.1 zoom 0.57
    $ renpy.sound.play("/audio/soun_fx/gags/SDTGag10.opus", channel="sfx1", loop=False, relative_volume = 1.0)
    $ renpy.sound.play("/audio/soun_fx/cum2.opus", channel="sfx3", loop=False, relative_volume = 0.6)
    bo"Aaaaargh! *Moans Loudly*" with flash
    scene black with dissolve
    show tenten_ext_forcecum1_1 with dissolve:
        zoom 1.5 xalign 0.5 yalign 0.0
    show tenten_ext_forcecum1_1:
        easein 6 yalign 0.9
    bo"Hah... hah... Pathetic."
    bo"Look at the mess you are..."
    scene black with vpunch
    $ renpy.sound.play("/audio/soun_fx/gags/SDTGag18.opus", channel="sfx1", loop=False, relative_volume = 1.0)
    "You rip your cock out of her mouth carelessly, letting her collapse onto the floor."
    scene tenten_ext_bj_forcespit1 with dissolve
    "She lies there, unresponsive, drool and semen mixing on the floor, eyes vacant."
    ten"*Shallow breaths*..."
    bo"Tch. Broken already? How disappointing."
    bo"Guess you weren't worth the effort after all."
    scene black with vpunch
    
    ten"..."
    show tenten_ext_bj_forcespit2 with dissolve
    ten"You will *Cough Cough* P-pay for this..."
    bo"Do not make empty threats, Tenten. Get up. I'm done with you."
    scene black with vpunch
    bo"Oh, and here's your trash back."
    "You drop the pendant on the floor before dressing and leaving without a backward glance."
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
    jump tenten_extort_leave_hatred