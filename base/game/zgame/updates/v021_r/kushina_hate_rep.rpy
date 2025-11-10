default kushina_topless = False
default kushina_nude = False
label kushina_break_resistance:
    ku"[bo_name_stutter], listen to me!"
    label break_resistance_repeat:
    if kushina_resistance_actionstaken >=2:
        $ kushina_resistance_actionstaken = 0
        $ kushina_topless = False
        $ kushina_nude = False
        ku"E-enough! I won't let this go on any longer!" with vpunch
        $ renpy.sound.play("/audio/soun_fx/wakeup.opus", channel="sfx3", loop=False, relative_volume = 0.6)

        show kushina_dream wakeup at brightreveal:
            matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 
        with longerflash
        with Shake((0, 0, 0, 0), 1.5, dist=20, peak_time=0.8, smoothness=50)
        pause 0.3
        scene kushina_dream wakeup with dissolve
        "Kushina used what little chakra she could muster to break away."
        call changeHatred(1,statlevel=2) from _call_changeHatred_227
        bo"*Snoring... angrily!*" with vpunch
        scene black with dissolve
        
        jump action_taken
    else:
        pass
    ku"You have to snap out of it. Kurama's trying to take hold of you!"
    ku"This isn't who you are!"
    default kushina_resistance_counter = 0
    menu kushina_testjumpmenu:
        ku"This isn't who you are!"
        "Grope her tits":
            if kushina_topless == False:
                bot"You know, you are pretty sexy for your age Kushina!"
                ku"H-hey, I can read your thoughts, r-remember!?" with vpunch
                ku"You have to snap out of it!"
                bot"You are right, maybe I will..."
                scene v21_kushina_hate_tits_groped1 with dissolve:
                    yalign 1.0
                show v21_kushina_hate_tits_groped1:
                    easein 4 yalign 0.5
                bot"...Right after I cop a feel of your saggy tits!" with vpunch
                $ renpy.sound.play("audio/soun_fx/grabsound.opus", channel="sfx3", loop=False, relative_volume = 1.5)
                show v21_kushina_gropetits_clothed1 with dissolve:
                    yalign 0.5
                ku"H-hey, stop that right now!" with vpunch
                bot"Don't think I will!{p}That's a nice rack, granny! Not as saggy as I thought..."
                $ renpy.sound.play("audio/soun_fx/grabsound.opus", channel="sfx3", loop=False, relative_volume = 1.5)
                call changekushina(3) from _call_changekushina
                ku"Th-that's enough!{p}What would your [na_rel] think of you, you idiot!" with vpunch
                bot"Don't care!"
                ku"I said..."
                $ renpy.sound.play("/audio/soun_fx/eyejougan.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                scene black with flash
                ku"That's enough!" with vpunch
                beast"Always used to resist, that one..."
                beast"Keep chipping away at her, kid.{p}Her chakra won't last for much longer while we cooperate!"
                scene v21_kushina_hate_bg
                show v21_kushina_hate_t standing:
                    zoom 0.75 xalign 0.5
                with dissolve
                ku"Arrh! *Scoffs*"
                beast"Deplete her resistances and I shall reward you..{p}With her!" with vpunch
                ku"Y-you are lucky you are under the influence of that bastard!{p}Otherwise I'd beat some sense into you myself!"
                bot"Right... hehe!"
                ku"Hey, you aren't paying attention to his deranged whispers, are you?" with vpunch
                

            else:
                bot"Your bare tiddies are a marvel to behold!"
                ku"H-hey, you aren't supposed to stare at your granny, you pervert!" with vpunch
                ku"Try to snap out of his influence, you can do it!"
                bot"I wasn't planning on just staring..."
                ku"H-huh!?" with vpunch
                scene v21_kushina_hate_tits_groped1topless with dissolve:
                    yalign 1.0
                show v21_kushina_hate_tits_groped1topless:
                    easein 4 yalign 0.5
                ku"What the-"
                bot"I can see why Kurama has a hard time with you. You are hard to resist, granny!" with vpunch
                $ renpy.sound.play("audio/soun_fx/grabsound.opus", channel="sfx3", loop=False, relative_volume = 1.5)
                show v21_kushina_gropetits_naked1 with dissolve:
                    yalign 0.5
                ku"You" with vpunch
                $ renpy.sound.play("audio/soun_fx/grabsound.opus", channel="sfx3", loop=False, relative_volume = 1.5)
                bot"Don't think I will!{p}Look at them bounce!"
                call changekushina(3) from _call_changekushina_1
                ku"Kurama... you shitty fox!" with vpunch
                $ renpy.sound.play("/audio/soun_fx/eyejougan.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                scene black with flash
                ku"I'll kill you!" with vpunch
                $ renpy.sound.play("/audio/soun_fx/growl1.opus", channel="sfx3", loop=False, relative_volume = 0.9)
                beast"He-he-he..."
                scene v21_kushina_hate_closeup:
                    yalign 0.5      
                beast"Keep chipping away at her, kid.{p}Deplete her resistances and I shall reward you!" with vpunch
                beast"Deplete her resistances and I shall reward you..{p}With her!" with vpunch
                ku"Y-you are lucky you are under the influence of that bastard!{p}Otherwise I'd beat some sense into you myself!"
                bot"Right... hehe!"
                ku"To think you'd be brazen enough to touch a woman like that... let alone me!"
                ku"Has your [na_rel] taught you anything!?"


            $ kushina_resistance_actionstaken +=1
            if kushina_resistance_counter == 0: #increase to 1
                $ kushina_resistance_counter +=1
            jump break_resistance_repeat
        "Grope her ass":
            if kushina_nude == False:
                bot"There's something you have that interest me, granny!"
                ku"Hmm?" with vpunch
                ku"You have to stay focused, [bo_name]!"
                beast"I know exactly what you are talking about, kid..."
                scene v21_kushina_hate_bg
                show v21_kushina_hate_t behindass:
                    zoom 0.75
                with dissolve
                ku"H-hey! What's the big idea?"
                bot"Can't stay focused, when that ass is calling for me!" with vpunch
                ku"Wh-what!?" with vpunch
                $ renpy.sound.play("audio/soun_fx/grabsound.opus", channel="sfx3", loop=False, relative_volume = 1.5)
                scene v21_kushina_hate_ass_groped1 with dissolve:
                    yalign 1.0
                show v21_kushina_hate_ass_groped1:
                    easein 3 yalign 0.7
                ku"H-hey, stop that right now!" with vpunch
                scene v21_kushina_gropeass_clothed1 with dissolve:
                    yalign 0.7
                bot"Don't think I will!{p}Your ass is pretty firm for your age, granny!"
                call changekushina(4) from _call_changekushina_2
                $ renpy.sound.play("audio/soun_fx/grabsound.opus", channel="sfx3", loop=False, relative_volume = 1.5)
                ku"Th-that's enough!{p}You can't be touching me there like that! We share a sacred bond, me and you!" with vpunch
                bot"Don't give a fuck!"
                ku"I said..."
                $ renpy.sound.play("/audio/soun_fx/eyejougan.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                scene black with flash
                ku"That's enough!" with vpunch
                beast"Always used to resist, that one..."
                beast"Keep chipping away at her, kid.{p}Her chakra won't last for much longer while we cooperate!"
                if kushina_topless == False:
                    scene v21_kushina_hate_bg
                    show v21_kushina_hate_t standing:
                        zoom 0.75 xalign 0.5
                    with dissolve

                else:
                    scene v21_kushina_hate_closeup with dissolve:
                        yalign 0.5
        
                ku"Arrh! *Scoffs*"
                beast"Deplete her resistances and I shall reward you...{p}With her!" with vpunch
                ku"Y-you are lucky you are under the influence of that bastard!{p}Otherwise I'd beat some sense into you myself!"
                bot"Right... hehe!"
                ku"Hey, you aren't paying attention to his deranged whispers, are you?" with vpunch
                

            else:
                show v21_kushina_hate_closeup_naked:
                    easein 1 yalign 0.9
                bot"I wonder how your bare ass looks from behind, granny..."
                show v21_kushina_hate_closeup_naked:
                    easein 1 yalign 0.5
                ku"H-hey, stop thinking about perverted stuff for a minute, and focus on resisting the beast's influence!" with vpunch
                bot"Can't focus on that, when you sit there butt naked!"
                scene black with vpunch
                ku"H-huh!?"
                scene v21_kushina_hate_ass_groped1naked with dissolve:
                    yalign 1.0
                show v21_kushina_hate_ass_groped1naked:
                    easein 4 yalign 0.6
                ku"What the-" with vpunch
                $ renpy.sound.play("audio/soun_fx/grabsound.opus", channel="sfx3", loop=False, relative_volume = 1.5)
                bot"Especially when you present your spent up holes for all to see!" with vpunch
                ku"Let go of me right now!" with vpunch
                $ renpy.sound.play("audio/soun_fx/grabsound.opus", channel="sfx3", loop=False, relative_volume = 1.5)
                show v21_kushina_hate_ass_groped1naked with dissolve:
                    zoom 1.2 yalign 0.8 xalign 0.5
                bot"How about I slide my cock in you right now instead!" with vpunch
                call changekushina(8) from _call_changekushina_3
                ku"*Gasp!* That's... Kurama speaking for you, isn't!?{p}You shitty fox..." with vpunch
                $ renpy.sound.play("/audio/soun_fx/eyejougan.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                scene black with flash
                ku"I'll kill you!" with vpunch
                $ renpy.sound.play("/audio/soun_fx/growl1.opus", channel="sfx3", loop=False, relative_volume = 0.9)
                beast"He-he-he..."
                scene v21_kushina_hate_closeup_naked with dissolve:
                    yalign 0.6     
                beast"Keep chipping away at her, kid.{p}Deplete her resistances and I shall reward you!" with vpunch
                beast"Deplete her resistances and I shall reward you..{p}With her!" with vpunch
                ku"Y-you are lucky you are under the influence of that bastard!{p}Otherwise I'd beat some sense into you myself!"
                bot"Right... hehe!"
                ku"To think you'd be brazen enough to touch a woman like that... let alone me!"
                ku"Has your [na_rel] taught you anything!?"


            $ kushina_resistance_actionstaken +=1
            if kushina_resistance_counter == 0: #increase to 1
                $ kushina_resistance_counter +=1
            call changekushina(4) from _call_changekushina_4
            jump break_resistance_repeat
        "Expose her tits!" if kushina_resistance_counter >=1 and kushina_topless == False:
            $ kushina_topless = True
            bot"Last time, you said that this plane bends to my will, right?"
            ku"N-not exactly-"
            beast"Yes!" with vpunch
            beast"Simply think it, and I'll make it real!{p}So long as this bitch's chakra allows for it!"
            ku"You are only capable of conceptualizing things that-"
            bot"Don't care!{p}Take your top off!" with vpunch
            scene v21_kushina_hate_closeup with flash:
                yalign 0.5
            call changekushina(5) from _call_changekushina_5
            ku"What the-!{p}What are you even thinking about, you idiot!" with vpunch
            bot"It's working! Nice advice, Kurama!"
            bot"And even nicer tiddies, Kushina!" with vpunch
            ku"It can't be..."
            ku"[bo_name_stutter], please! Resist the beast's advances!"

            if kushina_resistance_counter == 1: #increase to 2
                $ kushina_resistance_counter +=1
            jump break_resistance_repeat
        "Expose her ass!" if kushina_resistance_counter >=1 and kushina_topless == True and kushina_nude == False:
            $ kushina_nude = True
            bot"So if that worked, then..."
            bot"Show me your pussy, granny!" with vpunch
           
            scene v21_kushina_hate_closeup_naked with flash:
                yalign 1.0
            call changekushina(7) from _call_changekushina_6

            ku"You freaking p-perv..."
            show v21_kushina_hate_closeup_naked:
                easein 0.5 yalign 0.5
            ku"Why would you think of something like that!" with vpunch
            bot"F-fuck! It's true...{p}I can bend this realm to my will!"
            bot"I wonder what else I could have you do for me, granny..." with vpunch
            ku"It can't be..."
            ku"[bo_name_stutter], please! Resist the beast's advances!"

            if kushina_resistance_counter == 1: #increase to 2
                $ kushina_resistance_counter +=1
            jump break_resistance_repeat
        
        "???" if kushina_resistance_counter >=2 and kushina_topless == False:
            "Maybe if she was topless first..."
            jump kushina_testjumpmenu
        "Slap her tits!!" if kushina_resistance_counter >=2 and kushina_topless == True:
            scene v21_kushina_hate_closeup_naked with dissolve:
                yalign 0.2
            bot"I can't believe you were flaunting those tits around the very first day we met, granny..."
            ku"I wasn't, you idiot!{p}This is just how you envisioned me in your mind in the first place!"
            bot"You say that, but..."
            show v21_kushina_handslap_tit with moveinleft:
                yalign 0.2
            $ renpy.sound.play("/audio/soun_fx/intro/spank4.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            with flash
            show v21_kushina_hate_closeup_titslap1 with dissolve:
                yalign 0.2
            pause 0.1
            hide v21_kushina_handslap_tit
            show v21_kushina_hate_closeup_titslap1_1:
                yalign 0.2
            with dissolve
            call changekushina(7) from _call_changekushina_7
            ku"*Gasp!* H-hey!!"
            bot"I don't buy that! Just look at these saggy tits of yours bouncing around!" with vpunch
            scene v21_kushina_hate_closeup_naked with dissolve:
                yalign 0.2
            ku"I won't tolerate more of this disrespect..."
            bot"We'll see about that..."
            $ kushina_resistance_actionstaken +=1
            if kushina_resistance_counter == 2: #increase to 3
                $ kushina_resistance_counter +=1
            jump break_resistance_repeat

        "???" if kushina_resistance_counter >=2 and kushina_nude == False:
            "Maybe if she was nude first..."
            jump kushina_testjumpmenu
        "Spank her ass!!" if kushina_resistance_counter >=2 and kushina_nude == True:
            "fill"


            $ kushina_resistance_actionstaken +=1
            if kushina_resistance_counter == 2: #increase to 3
                $ kushina_resistance_counter +=1
            call changekushina(5) from _call_changekushina_8
            jump break_resistance_repeat
        "{color=[hatredcolor]}Slap her!{/color}" if kushina_resistance_counter >=3 and kushina_topless == True:
            scene v21_kushina_hate_closeup_naked with dissolve:
                yalign 0.2
            bot"Surely you must have realized by now, right...?"
            ku"R-realized what exactly?"
            bot"And here I thought you were smarter than I am..."
            show v21_kushina_handslap_face with moveinleft:
                yalign 0.2
            $ renpy.sound.play("/audio/soun_fx/intro/spank4.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            with flash
            show v21_kushina_hate_closeup_slap with dissolve:
                yalign 0.2
            hide v21_kushina_handslap_face
            with dissolve
            call changeHatred(1,statlevel=2) from _call_changeHatred_228
            bot"Guess it runs in the family then, you dumb bitch!" with vpunch
            ku"Y-you... Why would you do that!?{p}You slapped me!" with vpunch
            bot"Don't you see? This is who I am! Kurama is just an accomplice to MY wishes!{p}And right now... I wish for you to such my fucking cock, bitch!"
            call changekushina(10) from _call_changekushina_9
            scene v21_kushina_hate_closeup_titslap1 with dissolve:
                yalign 0.2
            ku"N-no... NO!" with vpunch
            ku"I know this is his doing... I won't give up on you that easily, [bo_name_stutter]!"
            $ kushina_resistance_actionstaken = 0
            $ kushina_topless = False
            $ kushina_nude = False
            $ renpy.sound.play("/audio/soun_fx/wakeup.opus", channel="sfx3", loop=False, relative_volume = 0.6)

            show kushina_dream wakeup at brightreveal:
                matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 
            with longerflash
            with Shake((0, 0, 0, 0), 1.5, dist=20, peak_time=0.8, smoothness=50)
            pause 0.3
            scene kushina_dream wakeup with dissolve
            ku"You have to try harder! You can fend Kurama off, just like your [na_rel] did, Just like I did before you!" with vpunch
            "distraught by your actions, Kushina used what little chakra she could muster to break away."
            call changeHatred(1,statlevel=2) from _call_changeHatred_229
            bo"*Snoring... angrily!*" with vpunch
            scene black with dissolve
            jump action_taken
           
        
        "Return":
            jump kushina_starting_menu_repeat

            
        
        