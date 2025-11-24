default v21_hatredhandjob_cumonface = False
default hatredlevel2_handjobcounter = 0
# hatredlevel2_handjobcounter unlocks: 0 - intro, 1 - normal repeat or ball stimulation, 2 - trick her to cum on face, 3 - cuddle handjob and grope option

# Stat acquisition:
# Level 2 hatred point acquisition here total: 6
# Level 2 Hinata obedience point acquisition here total: 1
# Level 2 dominance point acquisition here total: 1

# '$ wakeup_toggle1 = True' if you want Hinata comes to the bedroom in the morning again


##########################################
# Requirements: Day 14, on Kurama hate/love path, Hinata's hospitality quest completed
##########################################

label hatredlevel2_intro:

    $ initialize_replay_defaults()
    scene bg day:
        zoom 0.70
    show hinaq1bg
    show hina quest1_4t
    show bobedx 3:
        matrixtransform ScaleMatrix(1.0, 0.6, 1.0)*OffsetMatrix(1.0, 238.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)
        alpha 1
    with dissolve

    call randomCheck(True,f"{{color={hatredcolor}}}Hatred {{/color}}check{{color=#00ff00}} passed{{/color}}") from _call_randomCheck_12
    hin "Oh s-sorry there, I didn't mean to wake you!"
    bot "Enough is enough, I need more than just these silly games!"
    show bobedx 6 zorder 100 with dissolve:
        matrixtransform ScaleMatrix(1.0, 0.6, 1.0)*OffsetMatrix(1.0, 238.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)
        alpha 1.00
    bot "If I play my cards right, I'm sure I can get more out of her than just watching her!"
    bot "I can't just force her outright to do whatever I want, but a little emotional manipulation here and there should do the trick."
    bot "Let's see how she responds to a bit of pressure and guilt tripping."
    bot "Time to take things to the next level!" with vpunch
    show bobedx 3 zorder 100 with dissolve:
        matrixtransform ScaleMatrix(1.0, 0.6, 1.0)*OffsetMatrix(1.0, 238.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)
        alpha 1.00
    bo "Listen [hin_rel], we really need to sit down and discuss all of this, because this can't go on any longer!"
    show bobedx 3 with dissolve:
        alpha 0.20
    hin "[bo_name] I already said I'm sorry and that I wasn't trying to wake you up..."
    show hina quest1_1t with dissolve
    show hina quest1_1t:
        easein 2 xalign 0
    hin "It's really not that big of a deal, go back to sleep if you're still tired!"
    show hina quest2_1 with dissolve:
        xzoom -1
        easein 2 xpos -0.25
    hin "I'm just trying to keep things in order around here to help you be more comfortable."
    show bobedx 3 zorder 100 with dissolve:
        alpha 1.00
    bot"Then why the fuck are you flaunting your ass around like that, unless..."
    bo "Not a big deal? Comfortable?"
    show hina quest2_1 with dissolve:
        xzoom 1 xpos -0.25
    show hina quest2_1:
        easein 2 xpos 0
    bo "You think I'm {i}comfortable{/i} with anything that's going on around here lately?"
    show bobedx 6 zorder 100 with dissolve
    bo "With what my life has become recently and how I'm controlled by a curse that I never asked for?"
    show bobedx:
        alpha 0.4
    show hina quest1_4t with dissolve
    hin "I-I know it's been hard for you dear, but I'm here for you to help you through all of this."
    show bobedx 3 with dissolve
    bo "Well you're not being of much help with words alone..." with vpunch
    show bobedx 6 zorder 100 with dissolve
    bo "In fact, not only are you not helping - it seems that most of the time you're making it even worse!"
    hide hina
    hide shina
    show shina shy at center
    with dissolve
    show shina shy at smallshake
    hin "W-worse? What do you mean by that? Am I doing something wrong?"
    show bobedx 3 with dissolve
    bo "You don't even realize what's going on, do you?"
    bo "I put myself out there and give you everything I can, I've helped you and this whole household with so many things!"
    if ch1_dy_200paid == True or toji_pay300 == True:
        bo "I work my ass off to try to come up with the money to pay our debts that you and [na_rel] left us with!"
    show bobedx 6 zorder 100 with dissolve
    bo "I've listened to you and tried to protect [him_name] by keeping her out of everything just like you asked me to!"
    bo "I do everything in my power to keep you happy, but what do I get in return?"
    bo "Nothing but judgment and sour looks for something out of my control!" with vpunch
    show shina surprised2 with dissolve
    hin "N-no, don't say that... Come on, you know that's not true [bo_name]!"
    show bobedx 3 zorder 100 with dissolve
    bo "You hardly even want to even look at me when I have my impulses, you just try to ignore and avoid me!"
    show bobedx 6 zorder 100 with dissolve
    bo "It makes me feel so dirty and worthless while I struggle with my urges!"
    bo "Do you even care about me?!" with vpunch 
    show bobedx 3 zorder 100 with dissolve
    bo "Or am I just such an embarrassment and burden that you don't want anything to do with me anymore...?"
    show shina worried with dissolve
    hin"[bo_name_stutter]! Of course not..."
    show shina surprised with dissolve
    show shina at smallshake
    hin "I-I do care about you, I really do! You know that!"
    bot "Hehe... The foundations have been laid out, time to see if I've whittled her down enough for her to take the bait."
    bot "You can try to resist and keep your distance all you want [hin_rel] but..."
    call changeHatred(1) from _call_changeHatred_216
    bot "I will wear you down and break you eventually!" with vpunch
    show shina shy with dissolve
    hin "I-I just, I am not sure how to, you know..."
    hin "Given your condition's intricacies, it can feel quite inappropriate for me as your [hin_rel_mother]..."
    show shina shy2 with dissolve
    hin "I am trying to give you some time alone, and adequate personal space..."
    hin "But I never meant to make you feel like a burden or that I don't want anything to do with you!"
    show shina shy with dissolve
    hin "I... I had no idea you felt that way, I'm so sorry [bo_name]!"
    show bobedx 6 zorder 100 with dissolve:
        alpha 1.00
    bot "That's right, let the guilt and shame sink in..."
    show shina concerned with dissolve
    show shina at smallshake
    hin"Is there... something more I could do f-for you?"
    $ renpy.sound.play("/audio/soun_fx/clothes_undress.opus", channel="sfx3", loop=False, relative_volume = 0.7)
    show bobedx 1_1 with dissolve:
        alpha 1.0
    call increaselust(10) from _call_increaselust_284
    "You carefully undress beneath your bedsheets, unbeknownst to [hin_name]..."
    bot "You gargling on my cock would be nice for starters, but I can't push you too far, too fast, can I?"
    show bobedx with dissolve:
        alpha 0.2
    bot "But that's not to say that today won't be a start! I'll make you mine, [hin_rel]!"
    bot"Just a little more pull on her motherly instincts should do the trick!"
    bo "Well that's what it looks like to me, and I can't keep going on like this!" with vpunch
    bo "I feel like I'm drowning in this sea of expectations, alone, abandoned...."
    bo "I can't breathe, I can't think, I can't do anything right!" with vpunch
    bo "I need you to see how much I'm struggling!"
    bo "I can't keep pretending that everything is okay when it's obviously not!"
    show shina shy with dissolve
    hin "Oh [bo_name]... I had no idea you had all this weight on your shoulders..."
    bo "I just really need you right now..."
    bo "I need you to be there for me, not against me!"
    hin "I'm right here, I promise. We'll get you through this together..."
    hin "I do understand that it's difficult for all of us, but it must be especially hard for you!"
    bot "Damn right, if only you knew just how HARD it is for me right now hehe..."
    bot "I think it's about time to show you EXACTLY how hard it is!"
    show bobedx 2 with dissolve:
        alpha 0.8
    bo"You asked before what more you could do for me, right...?"
    show shina concerned with dissolve
    hint"Is he g-grabbing his thing beneath those sheets? I hope this isn't what I think it is..."
    hin"Y-yes... Do you have something in mind?"
    menu hatredlevel2_intro_menu:
        hin"Y-yes... Do you have something in mind?"
        "{color=[hatredcolor]}No more jerking off alone!{/color}":
            call randomCheck(True,f"{{color={hatredcolor}}}Hatred {{/color}}check{{color=#00ff00}} passed{{/color}}") from _call_randomCheck_20
            bo "You say you're here for me, but I feel so alone in all of this..."
            show bobedx at smallshake
            bo "Even now, do you have any idea how much it hurts and throbs?"
            show shina surprised4 with dissolve
            bo "No, of course you don't..."
            show shina at smallshake
            hint"T-throbbing!?" with vpunch
            hin "You mean, y-your condition is-"
            show shina concerned with dissolve
            bo "Yes, right now! {p}Especially in the mornings, every day I feel like I'm about to burst!" with vpunch
            bo "It gets so bad that I can't even think straight sometimes..."
            show shina at smallshake
            hin "I-I'm so sorry, I didn't know!"
            hint"That does explain his aggressive and impulsive demeanor in the mornings. But..."
            show bobedx 1_1 with dissolve
            bo "I need you to be more considerate of my needs and struggles!"
            $ renpy.sound.play("/audio/soun_fx/clothes_undress.opus", channel="sfx3", loop=False, relative_volume = 0.7)
            show bobedx f1 zorder 100 with Dissolve(1)
            show shina surprised3 with dissolve
            bo "Look at me, I'm a mess!"
            show shina at smallshake
            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            hin "*Gasp*!" with vpunch
            hin "H-hey...! You can't just-..."
            bo "I never asked for this!" with vpunch
            bo "I never wanted to be in this situation!"
            show shina concerned
            show bobedx f2
            with dissolve
            bo "I just wanted to be happy, to be loved, to be accepted!"
            bo "But all I feel is anger, frustration, and pain!"
            bo "I need help! I need {i}your{/i} help [hin_rel], please..."
            scene black with dissolve
            $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 0.7)
            hin"[bo_name_stutter]..."
            "Clearly flustered, [hin_name] makes small hesitant steps towards you..."  
            scene v21_hinatahate_hand grab_c with dissolve: 
                yalign 1.0
            show v21_hinatahate_hand grab_c:
                easein 5 subpixel True yalign 0.3
            "She awkwardly takes a seat next to you on the bed, intentionally leaving a gap between the two of you trying to avoid the implications that are quickly arising..."
            show screen parallax1280 ("v21_hinatahate_hand grab_c",1,0.4) with dissolve 
            call showscrollingimage from _call_showscrollingimage_280
            hin"..."
            bo"..."
            "She takes some time to think, trying to figure out the right words to say, but there is no world, imagined or real, where this would ever be the right thing to do."
            hin "Uhm... I..."
            hin"I don't know what to say, but I'm here to support you, [bo_name_stutter]. In any way that I can..."
            hin "I want to help, but I don't really know how... {p}W-what is it that you expect me to do?"
            hide screen parallax1280
            show screen parallax1280 ("v21_hinatahate_hand grab_c_2",1,0.5)
            with dissolve 
            bo "Come on [hin_rel], helping me is the {i}least{/i} you could do for me..."
            bo "You make everything seem so complicated..."
            bo "But it really isn't. I think for the first step... {p}You just need to {i}understand{/i}!"
            hin"..."
            scene black
            call hidescrollingimage("Click twice to make her understand!") from _call_hidescrollingimage_223
            scene v21_hinatahate_hand grab 3a_2 with dissolve:
                yalign 1.0
            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            hin"*Gasps*" with vpunch
            show screen parallax1280 ("v21_hinatahate_hand grab 3a_2",1,0.2) with dissolve 
            call showscrollingimage from _call_showscrollingimage_281
            bo  "And to understand, you have to feel what I feel... what I need!" with vpunch
            hin"[bo_name]! We can't! I am your [hin_rel_mother]!"
            bo "You heard Lady Tsunade yourself, she was very clear..."
            bo "I have to be relieved of this pain, or bad things happen."
            bo "You don't want bad things to happen, {i}do you{/i}?!" with vpunch
            hin "N-no, of course not! But..."
            hide screen parallax1280
            show screen parallax1280 ("v21_hinatahate_hand grab 3a",1,0.2)
            with dissolve
            hin "We shouldn't be doing this, it's... w-wrong!"
            "[hin_name] hesitantly wrapped her palm gently around your shaft..."
            call increaselust(10) from _call_increaselust_285
            bot"Holy shit, it's w-working! F-fuck, just her touch alone is enough to send me!"
            bo"Can you feel it's warmth? The constant throbbing? It hurts, [hin_rel]..."
            hin"Y-yes, but..."
            hint"He wasn't lying, it's burning hot, emanating heat! I've never felt something this intense before, not even when I... with [na_name]."
            hint"If it's this intense to the touch, I can't imagine how it must feel for [bo_name], my poor boy!{p}But still..."
            hin "There has to be another way. Surely you can take care of it yourself, can't y-you?"
            bot"Now for the finishing act! Just a little more gentle manipulation and I'll have you where I want you [hin_rel]!"
            hide screen parallax1280
            show screen parallax1280 ("v21_hinatahate_hand grab 3a_3",1,0.2)
            with dissolve
            bo "I've tried! I can't do it alone anymore!"
            bo "The more I try, the worse it gets..."
            bo "It's not just about the physical act, it's about the emotional support!"
            bo "All I can think of is how much you disapprove of me and it destroys me..."
            hin"I never said I diss-"
            bo "Please, I need you to show me that it's normal..." with vpunch
            bo "I need to know that everything will be alright..."
            bot "Come on [hin_rel], stop fighting it!"
            hide screen parallax1280
            show screen parallax1280 ("v21_hinatahate_hand grab 3a_3",1,1.0)
            with dissolve
            bot "Just look at how your [hin_rel_to_bo]'s cock yearns for you!{p}Give in to me!"
            scene v21_hinatahate_hand grab 3a_3b with Dissolve(1):
                yalign 0.3 
            hint "I know this is wrong, I know I shouldn't even be thinking about it! But if it's the only way I can help then..."
            if toji_pay300 == True or toji_defeated == True:
                hint "Besides, it wouldn't be the first time I help him, only this time he is wide awake! He was never supposed to know..."
                hint "Am I really thinking about going down this path?"
            hint "I suppose there is no other way, [bo_name] wouldn't be asking for help if it wasn't absolutely necessary, right?"
            bo"...[hin_rel_stutter]?"
            hint "Just this one time then. After this, I'll make sure to protect him from even myself, so that this doesn't have to happen again..."
            hint "Oh [na_name]... I wish you were here to help us!"
            hint "I guess it's all up to me now to make things right..."
            scene black
            call hidescrollingimage from _call_hidescrollingimage_224
            hin"Then..."
            $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 0.7)
            show screen parallax1280 ("v21_hinatahate_onbed1",1,0.2) with dissolve
            call showscrollingimage from _call_showscrollingimage_282
            hin"...I'll try to help, this one time only, okay?"
            bo"R-right..."
            bot"Holy shit! She actually fell for my ploy!{p}This one time? You have no idea [hin_rel]... this is just the start!" with vpunch
            hide screen parallax1280
            show screen parallax1280 ("v21_hinatahate_onbed1_2",1,0.7)
            with dissolve
            hin "I don't disapprove of you, [bo_name]. I am just, concerned..." with vpunch
            bot"F-fuck! Come on [hin_rel], keep stroking me! I better keep this charade up as long as I can..."
            hin "I know this isn't easy on you, but it isn't for me either!"
            show screen parallax1280 ("v21_hinatahate_onbed1_1",1,1.2) with dissolve
            bot"You have no idea, do you [hin_rel]!? Hehe..."
            hin "But as long as we both s-stay calm, and understanding of each other then..."
            scene black
            call hidescrollingimage() from _call_hidescrollingimage_225
            scene v21_hinatahate_handyanim_a with dissolve:
                yalign 1.0  
            show v21_hinatahate_handyanim_a:
                easein 3 subpixel True yalign 0.5
            hin "...Everything will be alright, I p-promise!"
            show v21_hinatahate_handyanim_a2 with dissolve:
                yalign 0.5
            bot"Oh f-fuck! She just stroked me!" with vpunch
            hin "I'm your [hin_rel_mother] after all, and I'll always be here for you!"
            $ renpy.sound.play("/audio/soun_fx/handjob4.opus", channel="sfx3", loop=False, relative_volume = 0.6)
            show v21_hinatahate_handyanim_anim at custom_vpunch_repeat(2) with dissolve:
                yalign 0.5
            bot"[hin_rel] is jerking me off willingly!"
            hint "This is so surreal, I can't believe I'm actually doing this..."
            hint "But I need to be stay strong... {p}I have to let him know that I'll be there for him, no matter what..."
            bo "Y-yeah... We're in this together!"
            bot "That's right [hin_rel]! Whatever helps you sleep at night knowing you jerked your [hin_rel_to_bo] off!"
            bot "Just keep stroking that cock for me!"
            hin "I-is this alright? Is it helping?"
            bo "Ahh... yes! That f-feels nice [hin_rel]..."
            hin"N-nice...? I thought you a-are in pain...."
            bo "I am, and you are helping ease it! Keep it going just like that..."
            hin"Okay, if you think it h-helps..."
            bot"I am going to turn you into my own personal handjob machine [hin_rel]!"
            scene v21_hinatahate_onbed1_2 with dissolve:
                yalign 0.3
            hin "Is this n-normal? It feels so h-hard and tense!"
            hin "Should we book an appointment at the infirmary to get it checked out?"
            show screen parallax1280("v21_hinatahate_handyanim_anim",1,0.5) with dissolve
            call showscrollingimage from _call_showscrollingimage_283
            bo "N-no! No need..."
            bo "This is how it always is when it hurts..."
            bo "You're making it feel better though, don't stop!"
            hin "I... I am trying, but this is quite uncomfortable..."
            show screen parallax1280("blackscreen",1,0.5) with dissolve
            hin"Think you can lay back a little bit?"
            hide screen parallax1280
            show screen parallax1280("v21_hinatahate_handylookupsad",1,0)
            with dissolve
            bot"Don't mind if I do!" with vpunch
            hint"It barely fits in my palm..."
            hint "I had no idea men's things could get so... hardened."
            hint"I can even feel it pulsating every time I r-rub it..."
            hint "I've never felt anything like this with [na_name] before..."
            show screen parallax1280("v21_hinatahate_handylookupsad",1) with dissolve
            hint "I had no idea it was this difficult, this painful... To think he's been dealing with it on his own for so long!"
            hint "I need to be a better [hin_rel_mother] for him, even if it means that..."
            scene black
            call hidescrollingimage from _call_hidescrollingimage_226
            $ renpy.sound.play("/audio/soun_fx/handjob5.opus", channel="sfx2", loop=True, relative_volume = 0.5)
            show v21_hinatahate_handyanim_animfast at custom_vpunch_repeat(1.1) with dissolve
            bot"Oh f-fuck!" with vpunch
            hint"Even if it means that sometimes, I'll have to take care of his t-troubles..."
            bot "She's really getting into it now, stroking me with both hands!"
            bot "I'm liking this side of you, [hin_rel]!"
            bot "I wonder how far I can manipulate you! A few weeks ago you would look away if I was in my underwear..."
            bot"Now you are sitting on your knees, stroking my cock! I can't wait to unleash all this pent-up lust all over you!"
            bo "Ahh... Yes... Just like that! Keep it going [hin_rel]!"
            hin" P-please... No n-need for commentary!"
            hint "T-this is so embarrassing... H-how did we even end up in this situation?!"
            hint "I need to stay strong and get this over with... For both of our sakes!"
            stop sfx2 fadeout 2
            scene v21_hinatahate_handy2b with dissolve:
                yalign 0.3
            hin "We're going to get it all of your system, don't worry!"
            hin "We'll deal with this c-curse, together! We won't let it tear this household apart!"
            bot "Fuck me, I'd love to tear YOU apart right now with this hard cock!"
            bot "Maybe soon... One step at a time!"
            scene v21_hinatahate_handy2b_1 with dissolve:
                yalign 0.3
            bo "Y-yes... I'm getting c-close..."
            scene v21_hinatahate_handy2b_2 with dissolve:
                yalign 0.3
            hint "Oh heavens, he is s-squirming! is he about to climax? {p}I h-have to be careful not to make a mess!"
            if toji_pay300 == True or toji_defeated == True:
                hint "I don't want it all over me and my face like last time!"
            hint "No turning back now..."
            bo "O-oh fuck [hin_rel]...! You're so fucking-..." with flash
            bo "-AAAAH!" with flash 
            $ renpy.sound.play("/audio/soun_fx/cum2.opus", channel="sfx2", loop=False, relative_volume = 0.3)
            scene v21_hinatahate_handy2b_2c with flash 
            pause 0.2
            $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx2", loop=False, relative_volume = 0.3)
            scene v21_hinatahate_handy2b_2c2 with flash 
            pause 0.2
            $ renpy.sound.play("/audio/soun_fx/cum4.opus", channel="sfx2", loop=False, relative_volume = 0.3)
            scene v21_hinatahate_handy2b_2c3 with flash 
            pause 0.7
            call decreaselust (50) from _call_decreaselust_136
            show v21_hinatahate_handy2b_2c3:
                easein 4 yalign 0.1
            hint "W-what the... t-this amount cannot be normal! {p}S-shoot! It's all over my h-hands too..."
            bo"*Heavy breathing*"
            hint "I need to stay calm. It's... over, right?"
            scene v21_hinatahate_povonbed2_bc with dissolve:
                yalign 1.0
            show v21_hinatahate_povonbed2_bc:
                easein 5.0 subpixel True yalign 0.0
            hin "T-there... are you f-feeling better?"
            bo "Ahh... What a relief!"
            bot "Look at her still trying to comfort me even with my cum all over her delicate hand..."
            bot "You are so fucking hot [hin_rel]... Even more so when you are clueless, bending to my will! Hehehe...."
            hin"...[bo_name_stutter]?" with vpunch
            bo"Y-yeah! Thanks for your 'help', [hin_rel]!"
            scene black with dissolve
            "[hin_name] fetches a hand towel and quickly cleans herself up before she turns to address you..."
            scene v21_hinatahate_handylookupthinking_b with dissolve:
                yalign 0.0
            show v21_hinatahate_handylookupthinking_b:
                easein 4 yalign 0.3
            bo "It feels so much fucking better now... all thanks to you!"
            hin "N-no need to use foul language! But I'm glad you're feeling better..."
            hin "Is it over now? Has all the pain subsided?"
            $ renpy.sound.play("/audio/soun_fx/horror.opus", channel="sfx2", loop=False, relative_volume = 0.5) 
            call changeHatred(1) from _call_changeHatred_217
            show v21_hinatahate_handylookupthinking_b1 with dissolve:
                zoom 1.1 yalign 0.7 xalign 1.0
            bot "Nothing is over... This is just the beginning for you! Hehehe..."
            scene v21_hinatahate_handylookupthinking_b1 with dissolve:
                yalign 0.3
            bo "Y-yeah, it's all better now..."
            bo "Thanks [hin_rel]... This means more to me than you can imagine."
            bo "I'm glad I have you to take care of me! I now know I can trust you with everything..."
            hin "[bo_name]..."
            bo "I'll let you know if I need more help, it makes me feel so much safer knowing that you're here for me."
            hin "...M-more help?"
            hint"I knew he'd get the wrong idea..."
            hint "I will have to figure out some other way of helping. This cannot be a recurring act..."
            hint "What have I gotten myself into..."
            scene v21_hinatahate_handylookupthinking_b with dissolve:
                yalign 0.2
            bo "Y-yeah some mornings are tough, but with your help I'm sure I can get through them a lot easier!"
            hin "I-I see... Although today was an e-exception. We cannot do that again. Not unless it's absolutely necessary, a last resort..."
            if not _in_replay:
                $ notification ("Wake-up event options unlocked")
                $ quest_hin.check("1_hin2H", "in progress")
                bo"Right..."
                if hatred.level == 1 and chosen_hate_path == True:
                    $ notification("Your Hatred has advanced to level 2!")
                    $ hatred.level += 1
                    $ hatred.value = 0
            bot"Hehe!"
            hin "*Sigh*... Let's both do our best to get through this, alright?"
            scene hina leavebobedroom with dissolve
            hin "I left a towel for you. Please clean after yourself and drop it in the laundry basket, okay?"
            bo "Okay... Thanks for everything, [hin_rel]!"
            scene black with fade
            $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            "You get yourself cleaned up and get dressed, while [hin_name] takes the laundry away."
            bot "Hehe... I like where this is going, I can feel her resolve slowly weakening already."
            $ hatredlevel2_handjobcounter += 1
            $ renpy.end_replay()
            $ quest_hin.check("hin2H_2", "in progress")
            $ notification("New quest discovered")
            bot "I wonder what I can get away with next time!"
            jump wakeupend

# Not unlockable at all here yet, but visible so players know to repeat the scene
        "{color=[hatredcolor]}???{/color}" if hatredlevel2_handjobcounter <1:
            "Complete previous options first to make [hin_name] more comfortable."
            jump hatredlevel2_intro_menu

        "{color=[hatredcolor]}???{/color}" if hatredlevel2_handjobcounter <2:
            "Complete previous options first to make [hin_name] more comfortable."
            jump hatredlevel2_intro_menu

        "{color=[obediencecolor]}???{/color}" if hatredlevel2_handjobcounter <3:
            "Complete previous options first to make [hin_name] more comfortable."
            jump hatredlevel2_intro_menu


label hatredlevel2_handjob_repeatable:

    $ initialize_replay_defaults()
    scene bg day:
        zoom 0.70
    show hinaq1bg
    show hina quest1_4t
    show bobedx 3 zorder 100:
        matrixtransform ScaleMatrix(1.0, 0.6, 1.0)*OffsetMatrix(1.0, 238.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)
        alpha 1
    with dissolve
    
    call checkHatred(0, "none", 2) from _call_checkHatred_39
    bo "I need help with the curse again, it's getting really bad!"
    hide hina
    hide shina
    show shina surprised2 at center
    with dissolve
    hin "Oh no, is it happening a-again? Are you alright?!"
    bot "Of course I'm alright hehe, I just want you to jerk me off again [hin_rel]!"
    if hatredlevel2_handjobcounter <3:
        bot "I can tell she is still hesitant, but I'm sure I can get her to 'help' me out again..."
    else:
        bot "[hin_rel] has done this so many times now, she should be used to 'helping' me out by now hehe..."
    bo "I-I'm trying to get through it but I really need you right now..."
    show shina worried
    show bobedx 3 zorder 100:
        alpha 1.00
    with dissolve
    hint "My poor boy, that darn curse is getting to him again!"
    hint "But what does he mean by 'help'? I hope it's not what I think it is..."
    if hatredlevel2_handjobcounter <3:
        hint "It was supposed to be a one-time thing for emergencies only!"
        hint "I can't keep doing this!" with vpunch
        hint "But what other options do we have...?"
    else:
        hint "I worry about him so much whenever this happens, but this is so wrong!"
        hint "We have to expel the curse's effect though..."
    show shina at smallshake
    hin "[bo_name] this isn't right you know..."
    hin "You can't just expect me to help you with this every time it happens!"
    hin "Show me where it hurts today though and I'll take a look. {p}I-is it down there again?"
    show bobedx 6 zorder 100 with dissolve
    bo "Y-yeah... And it's really bad today..."
    bot "I bet I'll get [hin_rel] to eventually like it almost as much as I do..."
    bot "Look at how she plays coy but still reluctantly asks to see my cock again!"
    $ renpy.sound.play("/audio/soun_fx/clothes_undress.opus", channel="sfx3", loop=False, relative_volume = 0.7)
    show bobedx f1 zorder 100 with Dissolve(1)
    bo "Look at this [hin_rel], I'm a mess!"
    show shina surprised5 with dissolve
    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    hin "*Gasp*!" with vpunch
    hin "H-hey...! You can't jus-..."
    show shina concerned with dissolve
    hint "Does he really have to take it all out like that every time without even a warning?!"
    hint "*sigh* Deep breaths... {p}Get it over with for his sake, he doesn't know any better..."
    scene black with fade
    hin "A-alright, let's get you all taken care of [bo_name]..."
    $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 0.7)
    scene v21_hinatahate_hand grab_c with dissolve: 
        yalign 1.0
    show v21_hinatahate_hand grab_c:
        easein 5 subpixel True yalign 0.3
    "She awkwardly takes a seat next to you on the bed, ashamed at what is inevitably about to happen again..."
    hint "My sweet boy, look at what you're forced to going through..."
    hint "I wish I could just take it all away for you, instead I have to sit and watch you suffer!"
    hint "Under normal circumstances doing any of this would be unthinkable and out of the question but..."
    hint "Giving you a helping hand is the least I can do! \nIt was the doctor's orders after all!"
    hin "Are you feeling alright? It looks pretty tense down there..."
    show v21_hinatahate_hand grab_c_2 with dissolve
    show v21_hinatahate_hand grab_c_2:
        easein 3 subpixel True yalign 0.3
    bo "Y-yeah... It hurts just like the other times but I'm keeping it together!"
    hin "O-okay, if you feel anything different or if it gets worse let me know, okay sweetie?"
    bo "Sure [hin_rel], I will!"
    hin "Let's just take it slow and see how it goes..."
    scene black with dissolve
    "She takes a deep breath and slowly wraps her hand around your shaft, feeling the warmth and tension on her palm."
    scene v21_hinatahate_handyanim_a with dissolve:      
        yalign 1.0  
    show v21_hinatahate_handyanim_a:
        easein 5 subpixel True yalign 0.5 
    hint "It doesn't feel much different from the last time, I can still feel that scorching heat radiating from it..."
    hint "These episodes seem really intense, I can't imagine how he gets through them..."
    bo "Ahh yeah, that feels good..."
    bot "Go on [hin_rel], I know deep down you want to!"
    $ renpy.sound.play("/audio/soun_fx/handjob4.opus", channel="sfx3", loop=False, relative_volume = 0.6)
    show v21_hinatahate_handyanim_anim at custom_vpunch_repeat(2) with dissolve:
        yalign 0.5
    hin "I-is this alright? Is it helping?"
    bo "Y-yeah, keep going just like that..."
    bo "You know... I really appreciate you doing this for me [hin_rel]!"
    bo "It really helps and lets me regain a lot of control around my actions and emotions..."
    hin "O-of course, that's w-why I'm here!"
    hin "We're gonna get you through this, o-okay? One day at a time..."
    hin "You can always count on me [bo_name], for w-whatever you need!"

    menu hatredlevel2_handjob_repeatablemenu:
        hin "You can always count on me [bo_name], for w-whatever you need!"
        "{color=[hatredcolor]}This is exactly what I need!{/color}":
            bo "This is exactly what I need right now..."
            bot "I won't push you for more this time [hin_rel], just keep doing what you're doing!"
            bot "Keep jerking it off like that so I can cum all over your hand again!"
            bo "I just need all this pressure out of my system, and I can feel it getting better already!"
            hin "O-okay... We'll get it all out again, d-don't worry!"
            bo "You're making it feel a lot more relaxed, don't stop!"
            show screen parallax1280("v21_hinatahate_handylookupsad",1,0) with dissolve
            call showscrollingimage from _call_showscrollingimage_284
            hint "This is so crazy, I can't believe I'm actually doing this again..."
            hint "How is he ALWAYS so firm when he asks for help?!"
            hint "It's like a slab of granite rock in my hand, left out in the sun and scorching hot to the touch!"
            show screen parallax1280("v21_hinatahate_handylookupsad",1) with dissolve
            hint "Has he been forced to walk around like this when he can't take care of himself?"
            hint "The poor thing, and to think I had been letting him deal with it on his own..."
            hint "I need to be a better [hin_rel_mother] for him!"
            scene black
            call hidescrollingimage from _call_hidescrollingimage_227
            $ renpy.sound.play("/audio/soun_fx/handjob5.opus", channel="sfx2", loop=True, relative_volume = 0.5)
            show v21_hinatahate_handyanim_animfast at custom_vpunch_repeat(1.1) with dissolve
            bot "Oh shit, she's speeding up and really getting into it now!"
            bot "I'm liking this side of her that I've awoken..."
            bot "Manipulating her to willingly please me and help release all this cum I've built up for her!"
            bo "Ahh... Yes... Just like that..."
            hint "T-this is so embarassing... Having to hear him moaning and talking like this to me again..."
            hint "H-how do we keep ending up in this situation?!"
            hint "I need to stay strong and get this over with... For both of our sakes!"
            scene v21_hinatahate_handy2b at custom_vpunch_repeat(2) with dissolve:
                yalign 0.3
            hin "I-it's alright sweetie, you're safe here..."
            hin "We j-just need to get it all o-out!"
            scene v21_hinatahate_handy2b_1 at custom_vpunch_repeat(2) with dissolve:
                yalign 0.3
            bo "Y-yeah... I'm getting c-close..."
            scene v21_hinatahate_handy2b_2 at custom_vpunch_repeat(2) with dissolve: 
                yalign 0.3
            hint "Good grief, is he ready to release? {p}I need to be careful where everything goes!"
            if toji_pay300 == True or toji_defeated == True or v21_hatredhandjob_cumonface == True:
                hint "I don't want it all over me and my face like that other time!"
            hint "No turning back now..."
            bo "O-oh fuck [hin_rel]...! You're so fucking-..." with flash
            bo "-AAAAH!" with flash 
            $ renpy.sound.play("/audio/soun_fx/cum2.opus", channel="sfx2", loop=False, relative_volume = 0.3)
            scene v21_hinatahate_handy2b_2c with flash 
            pause 0.2
            $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx2", loop=False, relative_volume = 0.3)
            scene v21_hinatahate_handy2b_2c2 with flash 
            pause 0.2
            $ renpy.sound.play("/audio/soun_fx/cum4.opus", channel="sfx2", loop=False, relative_volume = 0.3)
            scene v21_hinatahate_handy2b_2c3 with longerflash 
            pause 0.7
            hint "What the heck, why is it always so much and so sticky?! {p}Ughh, look at how it gets everywhere!"
            bo "*groans* Ah yeah..."
            call decreaselust (50) from _call_decreaselust_137
            hint "We're done now at least, it's okay... I need to stay calm..."
            scene v21_hinatahate_povonbed2_bc with dissolve: 
                yalign 1.0
            show v21_hinatahate_povonbed2_bc:
                easein 5 subpixel True yalign 0.0
            hin "T-there... are you f-feeling better?"
            bot "Look at her still trying to comfort me even with my cum all over her delicate hand..."
            bot "You are so fucking hot [hin_rel]... Even more so when you are clueless, bending to my will! Hehehe...."
            hin"...[bo_name_stutter]?" with vpunch
            bo "Oh uhm... Y-yeah [hin_rel], what a relief!"
            scene black with dissolve
            "[hin_name] fetches a hand towel and quickly cleans herself up before she turns to address you..."
            scene v21_hinatahate_handylookupthinking_b with dissolve:
                yalign 0.0
            show v21_hinatahate_handylookupthinking_b:
                easein 4 yalign 0.3
            bo "It feels so much fucking better now... all thanks to you!"
            hin "N-no need to use foul language! But I'm glad you're feeling better..."
            hin "Is it over now? Has all the pain subsided?"
            $ renpy.sound.play("/audio/soun_fx/horror.opus", channel="sfx2", loop=False, relative_volume = 0.5) 
            call changeHatred(1) from _call_changeHatred_218
            show v21_hinatahate_handylookupthinking_b1 with dissolve:
                zoom 1.1 yalign 0.7 xalign 1.0
            bot "Nothing is over... This is just the beginning for you! Hehehe..."
            scene v21_hinatahate_handylookupthinking_b1 with dissolve:
                yalign 0.3
            bo "Y-yeah it's all better now..."
            bo "Thanks [hin_rel]... This means more to me than you can imagine."
            bo "I'm glad I have you to take care of me! I know now that I can trust you with everything..."
            hin "[bo_name]..."
            hin "Of course, you can always trust me! You're my sweet [hin_rel_to_bo], I'm glad to have you too!"
            bo "I'll let you know if I need more help, it makes me feel so much safer knowing that you're here for me."
            hin "M-more help...?"
            hint"I knew he'd get the wrong idea, he's getting way too comfortable asking for help..."
            hint "I don't want him to think this is normal, I can't keep doing this!"
            hint "What have I gotten myself into..."
            scene v21_hinatahate_handylookupthinking_b with dissolve:
                yalign 0.0
            hin "[bo_name] just remember, this is for emergencies ONLY!"
            hin "You can't rely on me to help like this all the time, o-okay? \nIt's just not r-right!"
            bo"Right... Yeah, I get it..."
            bot"Hehe!"
            hin "*Sigh*... Let's just both do our best to get through this, alright?"
            scene black with dissolve
            hint "Why do I feel like whenever I talk it goes in one ear and out the other with him..."
            scene hina leavebobedroom with dissolve
            hin "I left a towel for you. Please clean after yourself and drop it in the laundry basket, okay?"
            bo "Okay... Thanks for everything, [hin_rel]!"
            scene black with fade
            $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            "You get yourself cleaned up and get dressed, while [hin_name] takes the laundry away."
            bot "Hehe... This is becoming a regular thing and I'm loving it!"
            bot "I can feel her resolve slowly weakening already..."
            bot "I wonder if I can get away with more next time!"
            if hatredlevel2_handjobcounter <=1:
                $ hatredlevel2_handjobcounter += 1
            $ renpy.end_replay()
            jump wakeupend

        "{color=[hatredcolor]}My balls need some attention!{/color}" if hatredlevel2_handjobcounter >=1:
            if hatredlevel2_handjobcounter <=1:
                $ hatredlevel2_handjobcounter += 1
            bot "My balls are so full and in need of draining, and you're the perfect little candidate for giving them the attention they need..."
            bo "I uhm... I actually do need something!"
            bo "Something feels off [hin_rel], I have a really sharp pain today, but it's a bit lower down!"
            scene v21_hinatahate_handyanim_b with dissolve
            hin "L-lower? Somewhere here around your thighs?"
            hin "Sore muscles perhaps? Sounds like you pushed yourself too hard during training!"
            bo "N-no, not that far below..."
            bo "It's... my balls!" with vpunch
            hin "H-huh!? You mean... down t-there?" with vpunch
            scene v21_hinatahate_handyanim_c with dissolve
            bo"It feels like everything is clogged up and blocked! I can't e-even help myself to a release like this..."
            hin "S-should we go see someone about it, this sounds pretty serious [bo_name]!"
            bo "No! N-no need [hin_rel], I think it just needs some massaging to get the blood flowing there too."
            bo "It's probably just a circulation issue because of how little blood is left when I'm hard or something."
            hin "Circulation issues? I g-guess that sort of makes sense..."
            bot "So many questions, just caress my ballsack already!"
            show screen parallax1280("v21_hinatahate_handywithballs_a",1,1.0) with dissolve
            call showscrollingimage from _call_showscrollingimage_285
            hin "W-where does it hurt exactly, around here?" with vpunch
            bot"O-oh...? So eager to assist, [hin_rel]!"
            bot"As long as you think I am in pain, hehe!"
            bo "Y-yeah, it's a bit towards the back so make sure you're getting it close to the base too..."
            hide screen parallax1280
            show screen parallax1280("v21_hinatahate_handywithballs_b",1,1.0)
            with dissolve
            hin"...H-here?"
            bo "I t-think it just needs everything pushed upwards because it's been storing semen for too long."
            bot "What the hell am I even saying?"
            bot "Whatever, as long as she keeps fondling my cock like that, it doesn't matter!"
            call changeRespect("Hinata", -1) from _call_changeRespect_241
            hint "Is this some sort of joke he's playing on me?"
            hint "I thought it was a circulation issue... Now he's talking about s-semen...?"
            hint "It can't be... He's probably just confused, and in pain!"
            hint "If this doesn't help we will definitely need to go get it checked by Lady Tsunade!"
            hide screen parallax1280
            show screen parallax1280("v21_hinatahate_handywithballs_anim",1,1.0)
            with dissolve
            hin "H-how is this? Is it feeling a bit better?"
            bo "Yeah, that feels good..."
            bo "I think I can feel everything slowly going back to normal already, just keep going!"
            hin "O-okay, that's a relief!"
            hin "It almost sounded like you were describing testicular torsion, which is a serious issue you know!"
            hin "It would need emergency care to prevent permanent damage!"
            bo "H-huh, what's that? N-no, no, I don't think it's that serious!"
            bot "What the fuck even is testicular torsion that she's scaring me with?" 
            bot "Just shut the fuck up already so I can enjoy this [hin_rel]!"
            bot "The only thing wrong with me is that I haven't blown my load all over you yet! Hehehe..."

            menu hatredlevel2_handjob_balls:
                "{color=[dominancecolor]}Take control and cum on her{/color}":
                    call checkDominance(0, "hatredlevel2_handjob_balls", 2) from _call_checkDominance_61
                    bot "Time to take matters into my own hands..."
                    bot "I'll make her keep giving me all her attention and then give her a surprise gift at the last second."
                    bot "Everyone loves a good surprise, right?"
                    bo "Ahhh... Yeah, just like that [hin_rel]."
                    bo "A little more, I can feel everything starting to flow again..."
                    hin "O-oh, okay..."
                    hin "We d-don't want anything blocked, it has to go out s-somewhere I guess..."
                    hint "I'm no doctor, but this really doesn't seem right!"
                    hint "How in the world did I end up in this position with his balls in my hand?!"
                    hin "A-are you sure this is right, do you need me to do it differently?"
                    bo "It f-feels right, yeah... Could you use your left hand to help guide everything out too?"
                    hin "U-up here? I-I guess I can try..."
                    hide screen parallax1280
                    show screen parallax1280("v21_hinatahate_handywithballs_anim",1,1.0,transformeffect=custom_vpunch_repeat(2))
                    with dissolve
                    $ renpy.sound.play("/audio/soun_fx/handjob4.opus", channel="sfx2", loop=True, relative_volume = 0.5)
                    hin "Like this? I-I'm not sure if I'm doing it right..."
                    bo "Y-yeah, it's perfect like that, keep doing what you're doing..."
                    bot "This is so hot, watching my [hin_rel] give my balls attention while she jerks me off!"
                    bot "And she's not even complaining, only asking if she's doing a good job hehe..."
                    bot "I'll show you just how great you're doing, when I reward you with my cum!"
                    $ renpy.sound.play("/audio/soun_fx/handjob5.opus", channel="sfx2", loop=True, relative_volume = 0.5)
                    hide screen parallax1280
                    show screen parallax1280("v21_hinatahate_handywithballs_animfast",1,1.0,transformeffect=custom_vpunch_repeat(1.1))
                    with dissolve
                    hint "There's no time to lose, I just have to remember that it's a medical necessity!"
                    hint "This whole ordeal is embarassingly awkward, but I need to release the obstruction before it causes any further damage!"
                    bo "Ahh... Yes... Just like that..."
                    hin "E-everything alright, is the pain bearable...?"
                    bo "Y-yes, it's all good... I'm getting c-close..."
                    hint "Good grief, is he ready to release? {p}I hope he has it all under control!"
                    if toji_pay300 == True or toji_defeated == True or v21_hatredhandjob_cumonface == True:
                        hint "I don't want it all over me and my face like that other time!"
                    hint "No turning back now..."
                    call changeDominance(1, "v021_hin_ballscumonherdom", 1, statlevel=2) from _call_changeDominance_131
                    bot "Hell yeah, time to get up and cover you with as much of my cum as I can [hin_rel]!"
                    bot "Just need to get the right angle at the last second a-and...-"
                    scene v21_hinatahate_finish_surprised with dissolve:
                        yalign 1.0
                    call hidescrollingimage("Click twice to reward [hin_name] with your cum!") from _call_hidescrollingimage_228
                    show v21_hinatahate_finish_surprised:
                        easein 5 subpixel True yalign 0.0
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    hin "H-huh? What are you doing?!"
                    bo "O-oh fuck [hin_rel]...! You're so fucking se-..." with vpunch
                    bo "-... AAAAH!" with flash 
                    $ renpy.sound.play("/audio/soun_fx/cum2.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                    scene v21_hinatahate_finish_surprised_cum1 with flash: 
                        yalign 0.0
                    hin "H-hey! Watch it!" with vpunch
                    $ renpy.sound.play("/audio/soun_fx/cum4.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                    scene v21_hinatahate_finish_surprised_cum2 with flash: 
                        yalign 0.0
                    bo "AGHHHH!"
                    call decreaselust (50) from _call_decreaselust_138
                    scene v21_hinatahate_finish_angry_cum0 with dissolve: 
                        yalign 0.0
                    hin "What in the hell do you think you're doing?!"
                    show screen parallax1280("v21_hinatahate_finish_angry_cumend", 1,0.0) with dissolve
                    call showscrollingimage from _call_showscrollingimage_286
                    hin "Damn it, [bo_name]! You need to be more careful!"
                    hint "What has gotten into this boy?!"
                    hint "Ughh, and I still can't believe how much it gets everywhere!"
                    bo "S-sorry..."
                    $ renpy.sound.play("/audio/soun_fx/horror.opus", channel="sfx2", loop=False, relative_volume = 0.5) 
                    call changeHatred(1,"v021_hin_ballscumonher",1, statlevel = 2) from _call_changeHatred_203
                    bot "Sorry for not getting any inside that mouth of yours for you to swallow is what I mean! Hehe..."
                    hin "Ughh disgusting... Why the hell would you suddenly stand up like that?"
                    bo "It w-was, uhm..."
                    bo "It was to unblock everything, I think sitting down was obstructing it and making it worse..."
                    bo "Y-yeah see, I got up and everything instantly flowed normally again!"
                    call changeRespect("Hinata",-3) from _call_changeRespect_269
                    hin "Am I supposed to believe that now?"
                    hin "What a ridiculously foolish thing to do, I knew this was a mistake!"
                    scene black
                    call hidescrollingimage from _call_hidescrollingimage_229
                    "[hin_name] frantically grabs a nearby cloth to quickly wipe herself clean of your sticky release."
                    scene v21_hinatahate_facewipecloth with dissolve:
                        yalign 1.0
                    show v21_hinatahate_facewipecloth:
                        easein 4 subpixel True yalign 0.3
                    bot "She is NOT happy about that, but I don't care haha... That was great!"
                    bot "Look at her desperately trying to restrain herself while my cum covers her face..."
                    bot "She's so clueless as to what is going on! But still so fucking hot!"
                    hint "This is completely unacceptable! I can't believe he's done this to me!"
                    scene v20hin_handy end1_2 with dissolve:
                        yalign 0.3
                    hint "Could it really be that he has absolutely zero control over himself..."
                    hint "I refuse to put up with this though if I am to help him, it's disgusting!"
                    hint "It's over now at least, I should stay calm and not make a scene but..."
                    hint "I need to get out of here, I can't stand the sight of him right now!"
                    scene black with dissolve
                    bo "[hin_rel]? I'm sorry, I didn't mean to-..."
                    "[hin_name] quickly gathers the dirty laundry and starts heading out of the room."
                    scene hina leavebobedroom with dissolve
                    hin "I don't want to hear it [bo_name]!" with vpunch
                    hin "Get yourself out of bed and cleaned up!"
                    bo "O-okay... Thanks [hin_rel] for helpi-..."
                    $ renpy.sound.play("/audio/soun_fx/footsteps.opus", channel="sfx1", loop=False, relative_volume = 0.9)
                    scene black with fade
                    "She storms out the room without even giving you the chance to finish your sentence."
                    bot "She seems pretty pissed off, maybe it was too much for her to handle."
                    bot "[hin_rel] follows instructions so well though, what a good little cock pleaser she is hehe..."
                    $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    "You clean yourself and get dressed with fresh clothes, ready to officially start the day."
                    if hatredlevel2_handjobcounter < 3:
                        bot "This is becoming a regular thing and I'm loving it! I can feel her resolve slowly weakening already."
                    else:
                        bot "I've got her wrapped around my finger now, she can't resist me anymore!"
                    $ v21_hatredhandjob_cumonface = True
                    bot "I wonder what else I can get away with next time!"
                    $ renpy.end_replay()
                    jump wakeupend
                
                "Let her finish helping you normally":
                    bot "Let's not get too carried away with this, I don't want to upset her too much and scare her off!"
                    bo "Ahhh... It's so much better now thanks, I can feel everything flowing again!"
                    bo "Seems like it just needed your delicate touch to get everything back on track."
                    hin "O-oh, so no more pain? Everything okay now?"
                    hin "That was weird, but I guess I'm just thankful it wasn't anything more serious..."
                    hint "Hopefully I never have to do anything like this again, it's so inappropriate and awkward!"
                    hint "And we still have the underlying i-issue to deal with, he doesn't look relaxed at all!"
                    call hidescrollingimage from _call_hidescrollingimage_230
                    scene v21_hinatahate_handyanim_c with dissolve:
                        yalign 1.0 
                    hint "*sigh* I can never seem to catch a break with him, but he needs this..."
                    $ renpy.sound.play("/audio/soun_fx/handjob5.opus", channel="sfx2", loop=True, relative_volume = 0.5)
                    show v21_hinatahate_handyanim_animfast at custom_vpunch_repeat(1.1) with dissolve
                    "[hin_name] firmly grasps your shaft with a newly-found resolve and starts stroking it with a steady rhythm."
                    hint "I've made it this far, I can't let him down now!"
                    hint "This wretched pressure and heat has to be addressed, before something else happens to him."
                    bot "She's really getting into it now, stroking me with both hands!"
                    bot "I'm liking this side of you, [hin_rel]!"
                    bot "I find it so amusing to manipulate you to willingly please me and help release all this pent-up lust!"
                    bo "Ahh... Yes... Just like that... *Soft moans*"
                    hint "T-this is so embarrassing... Having to hear my [hin_rel_to_bo]'s moans. Talking like this around me again..."
                    hint "H-how do we keep ending up in this situation?!"
                    hint "I need to stay strong and get this over with... For both of our sakes!"
                    scene v21_hinatahate_handy2b_2 at custom_vpunch_repeat(2) with dissolve:
                        yalign 0.3
                    hin "I-it's alright sweetie, you're safe now..."
                    hin "We j-just need to get it all o-out of your system!"
                    scene v21_hinatahate_handy2b_1 at custom_vpunch_repeat(2) with dissolve:
                        yalign 0.3
                    bo "Y-yeah... I'm getting c-close..."
                    scene v21_hinatahate_handy2b_2 at custom_vpunch_repeat(2) with dissolve: 
                        yalign 0.3
                    hint "Oh gosh, i-is he almost r-ready? {p}I have to be careful not to make a m-mess!"
                    if toji_pay300 == True or toji_defeated == True or v21_hatredhandjob_cumonface == True:
                        hint "I don't want it all over me and my face like that other time!"
                    hint "No turning back now..."
                    bo "O-oh fuck [hin_rel]...! You're such a sl-..."
                    bo "-... AAAAH!" with vpunch 
                    $ renpy.sound.play("/audio/soun_fx/cum2.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                    scene v21_hinatahate_handy2b_2c with flash 
                    pause 0.2
                    $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                    scene v21_hinatahate_handy2b_2c2 with flash 
                    pause 0.2
                    $ renpy.sound.play("/audio/soun_fx/cum4.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                    scene v21_hinatahate_handy2b_2c3 with longerflash 
                    pause 0.7
                    call decreaselust (50) from _call_decreaselust_139
                    hint "W-what the... W-where does all of this come from every time! {p}Crap, I didn't want a-any of it on my h-hands again!"
                    bo"*Heavy breathing*"
                    hint "I need to stay calm. It's... over, right?"
                    scene v21_hinatahate_povonbed2_bc with dissolve:
                        yalign 1.0
                    show v21_hinatahate_povonbed2_bc:
                        easein 5.0 subpixel True yalign 0.0
                    hin "T-there... are you f-feeling better?"
                    bot "Look at her still trying to comfort me even with my cum all over her delicate hand..."
                    bot "You are so fucking hot [hin_rel]... Even more so when you are clueless, bending to my will! Hehehe...."
                    hin"...[bo_name_stutter]?" with vpunch
                    bo"Y-yeah! Thanks for your 'help', [hin_rel]!"
                    scene black with dissolve
                    "[hin_name] fetches a hand towel and quickly cleans herself up before she turns to address you..."
                    scene v21_hinatahate_handylookupthinking_b with dissolve:
                        yalign 0.0
                    show v21_hinatahate_handylookupthinking_b:
                        easein 4 yalign 0.3
                    bo "It feels so much fucking better now... all thanks to you!"
                    hin "N-no need to use foul language! But I'm glad you're feeling better..."
                    hin "Is it over now? Has all the pain subsided?"
                    $ renpy.sound.play("/audio/soun_fx/horror.opus", channel="sfx2", loop=False, relative_volume = 0.5) 
                    call changeHatred(1, "v021_hin_ballsonherown", 1, statlevel=2) from _call_changeHatred_219
                    bot "It's not even close to being over, I've still got plenty more in store for you! Hehehe..."
                    bo "Y-yeah it's all better now..."
                    bo "Thanks [hin_rel]... This means more to me than you can imagine."
                    bo "I'm glad I have you to take care of me! I now know that I can trust you with everything..."
                    hin "[bo_name]..."
                    bo "I'll let you know if I need more help, it makes me feel so much safer knowing that you're here for me."
                    hin "...M-more help?"
                    hint"I don't know how much more of this I can tolerate..."
                    hint "I have to figure out some other way of assisting him. This is already too much!"
                    hint "What have I gotten myself into..."
                    scene v21_hinatahate_handylookupthinking_b1 with dissolve:
                        yalign 0.0
                    hin "L-look, this can't be your primary way of coping with everything."
                    hin "You need to find healthier outlets to your frustrations and emotions, [bo_name]!"
                    hin "Don't bottle it up inside and suffer on your own, but don't think we can keep doing this together o-okay?"
                    bo"Right..."
                    bot"Hehe!"
                    hin "*Sigh*... Let's both do our best to get through this, alright?"
                    scene black with dissolve
                    hint "It's always the same when trying to talk to him, it goes in one ear and immediately out the other..."
                    scene hina leavebobedroom with dissolve
                    hin "I left a towel for you. Please clean after yourself and drop it in the laundry basket, okay?"
                    bo "Okay... Thanks for everything, [hin_rel]!"
                    scene black with fade
                    $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    "You get yourself cleaned up and get dressed, while [hin_name] takes the laundry away."
                    if hatredlevel2_handjobcounter < 3:
                        bot "Hehe... This is becoming a regular thing and I'm loving it! I can feel her resolve slowly weakening already."
                    else:
                        bot "I've got her wrapped around my finger now, she can't resist me anymore!"
                    $ v21_hatredhandjob_cumonface = True
                    bot "I wonder what else I can get away with next time!"
                    $ renpy.end_replay()
                    jump wakeupend
        
        "{color=[hatredcolor]}I'm going to cum all over that pretty little face of yours!{/color}" if hatredlevel2_handjobcounter >=2:
            if hatredlevel2_handjobcounter ==2:
                $ hatredlevel2_handjobcounter += 1
            bot "Hehe... Time for my masterpiece! I bet I can get her whole face plastered with my cum this time!"
            bo "You're all I need right now, even just seeing your face calms me down a lot [hin_rel]!"
            hint "My f-face? What does he mean by that...?"
            bo "I just need all this pressure out of my system, and thanks to your help I feel it getting better already!"
            hin "O-okay... As long as it's h-helping!"
            show screen parallax1280("v21_hinatahate_handylookupsad",1,0) with dissolve
            call showscrollingimage from _call_showscrollingimage_287
            hint "This is beyond twisted, I can't believe I'm actually doing this again..."
            hint "He's my sweet [hin_rel_to_bo] and everything, and I do feel responsible for him but..."
            hint "This is far beyond the scope of how I should be acting around him!"
            hint "This pressure must be so painful for him though, I can feel that familiar overbearing tension again!"
            hint "He looks even more on edge today than usual, maybe it's a particularly bad day for him..."
            hint "I should try to be more sympathetic and understanding, but I still can't shake the feeling of how wrong this is!"
            scene black
            call hidescrollingimage from _call_hidescrollingimage_231
            $ renpy.sound.play("/audio/soun_fx/handjob5.opus", channel="sfx2", loop=True, relative_volume = 0.5)
            show v21_hinatahate_handyanim_animfast at custom_vpunch_repeat(1.1) with dissolve
            bot "Oh shit, she's speeding up and really getting into it now!"
            bot "I'm liking this side of her that I've awoken..."
            bot "Manipulating her to willingly please me and help release all this cum I've built up for her!"
            bot "If only you knew where exactly I'm planning to finish today on you! Hehehe..."
            call changeHatred(1,"v021_hin_cumfonface",1, statlevel =2) from _call_changeHatred_204
            bot "Work for it [hin_rel], work that cock till I get all my cum dripping down your whole face!"
            bo "Ahh... Yes... Just like that..."
            hint "T-this is so embarassing... Having to hear him moaning and talking like this around me..."
            hint "H-how did we even end up in this situation?!"
            hint "I need to stay strong and get this over with... For both of our sakes!"
            scene v21_hinatahate_handy2b at custom_vpunch_repeat(2) with dissolve:
                yalign 0.3
            hin "I-it's alright sweetie, you're safe now..."
            hin "We j-just need to get it all o-out!"
            bo "Y-yeah... I'm getting c-close..."
            bot "Okay, now's my chance! It's now or never..." with vpunch
            scene v21_hinatahate_handy2b_1 at custom_vpunch_repeat(2) with dissolve:
                yalign 0.3
            bo "W-wait [hin_rel]! S-something isn't right...!"
            stop sfx2 fadeout 2
            scene v21_hinatahate_sittinghandy1 with dissolve:
                yalign 1.0
            show v21_hinatahate_sittinghandy1:
                easein 5 subpixel True yalign 0.3
            hin "Wh-what? What's wrong [bo_name], are you okay?!"
            hint "He looks like he's in pain! What's happening?!"
            bot "Time to clench it a bit... Hoooold it..."
            bo "I-I don't know, something feels off down there... close to m-my balls!"
            bo "L-like it's swollen and sensitive! F-fuck, it hurts down there!"
            scene v21_hinatahate_checkcloser1 with dissolve:
                yalign 0.5
            hin "A-are you serious? And it hurts?! W-where?!"
            scene v21_hinatahate_checkcloser1 with dissolve:
                zoom 1.1 yalign 0.5 xalign 1.0
            bot "HOOOLD IT!! JUST A LITTLE CLOSER!" with vpunch
            scene v21_hinatahate_checkcloser1 with dissolve:
                yalign 0.5
            bo "T-this side over here, it's burning a bit! C-can you give it a quick look and see if it looks weird to you?"
            scene v21_hinatahate_checkcloser2 with dissolve:
                xzoom -1.0 yalign 0.5
            hin "W-where exactly, is it something on your thigh maybe? \nO-or somewhere els-...?"
            bot "Aaaand... NOW!!" with vpunch
            $ renpy.sound.play("/audio/soun_fx/cum2.opus", channel="sfx2", loop=False, relative_volume = 0.3)
            scene v21_hinatahate_checkcloser2_1 with flash:
                xzoom -1.0 yalign 0.5
            bo "AAAAH! Fuuuu-..." with flash
            $ renpy.sound.play("/audio/soun_fx/cum4.opus", channel="sfx2", loop=False, relative_volume = 0.3)
            scene v21_hinatahate_checkcloser2_2 with longerflash:
                xzoom -1.0 yalign 0.5
            call decreaselust (50) from _call_decreaselust_140
            hin "*Gasp!* W-what the...!" with vpunch
            bot "Bullseye! [hin_rel]'s face is covered with my dripping cum!"
            bot "Now THIS is an image I could get used to seeing every morning!"
            hin"Did you j-just..."
            scene v21_hinatahate_checkcloser2_3 with vpunch:
                xzoom -1.0 yalign 0.5
            hin "EXPLAIN YOURSELF!"
            bo "Oops... *nervous chuckle*"
            hin "What in the hell do you think you're doing [bo_name]?!"
            hint "What has gotten into this boy?!"
            hint "Ughh, he's gotten it all over my face and hair, how utterly revolting!"
            hin "I asked you a question! What the hell was that?!" with vpunch
            bo "S-sorry, I just couldn't hold it anymore!"
            bo "I don't know what happened, it just felt like I was about to explode and then it came right out!"
            hin "Well you could have at least tried to warn me before you did something as foolish as that!"
            hin "Now look at me, this is disgusting...!"
            call changeRespect("Hinata", -4) from _call_changeRespect_242
            hin "I understand that you need help, but this is just too much!"
            hin "You have to learn to control yourself better, you can't blame the curse on everything!"
            bot "Don't you worry about that! Everything is under my full control, especially YOU [hin_rel]!"
            bo "Y-yeah, I know... You're right... I didn't mean to-..."
            hin "Save it, I don't want to hear it right now!" with vpunch
            hint "Ughh, this is ridiculous!"
            scene black with dissolve
            "[hin_name] frantically grabs a nearby cloth to quickly wipe herself clean of your sticky release."
            scene v21_hinatahate_facewipecloth with dissolve:
                yalign 1.0
            show v21_hinatahate_facewipecloth:
                easein 4 subpixel True yalign 0.3
            bot "She is NOT happy about that, but I don't care haha... That was perfect!"
            bot "Turning her beautiful face into my personal canvas and painting it all with my cum!"
            bot "She's so clueless as to what is going on! But still so fucking hot!"
            hint "This is completely unacceptable! I can't believe he's done this to me!"
            scene v20hin_handy end1_2 with dissolve:
                yalign 0.3
            hint "Could it really be that he has absolutely zero control over himself..."
            hint "I refuse to put up with this though if I am to help him, it's disgusting!"
            hint "It's over now at least, I should stay calm and not make a scene but..."
            hint "I need to get out of here, I can't stand the sight of him right now!"
            scene black with dissolve
            bo "[hin_rel]? I'm sorry, I didn't mean to-..."
            "[hin_name] quickly gathers the dirty laundry and starts heading out of the room."
            scene hina leavebobedroom with dissolve
            hin "I don't want to hear it [bo_name]!" with vpunch
            hin "Get yourself out of bed and cleaned up!"
            bo "O-okay... Thanks [hin_rel] for helpi-..."
            $ renpy.sound.play("/audio/soun_fx/footsteps.opus", channel="sfx1", loop=False, relative_volume = 0.9)
            scene black with fade
            "She storms out the room without even giving you the chance to finish your sentence."
            bot "She seems pretty pissed off, maybe it was too much for her to handle."
            bot "I can't believe that actually worked though, she didn't even see it coming! *chuckle*"
            $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            "You clean yourself and get dressed with fresh clothes, clearly proud of your actions this morning."
            if hatredlevel2_handjobcounter < 3:
                bot "This is becoming a regular thing and I'm loving it! I can feel her resolve slowly weakening already."
            else:
                bot "I've got her wrapped around my finger now, she can't resist me anymore!"
            $ v21_hatredhandjob_cumonface = True
            bot "I wonder what else I can get away with next time!"
            $ renpy.end_replay()
            jump wakeupend

        "{color=[obediencecolor]}Make her get on the bed with you{/color}" if hatredlevel2_handjobcounter >=3:
            call checkObedience(0, "hatredlevel2_handjob_repeatablemenu", "Hinata", 2) from _call_checkObedience_38
            bot "It's time to test [hin_rel]'s limits! Let's try a different approach..."
            bot "I want that smoking hot body of yours on me while you are jerking me off today!"
            if hatredlevel2_handjobcounter ==3:
                bot "I just gotta find a way to get you to agree to it..."
                bot "Time to deploy some good old-fashioned manipulation and guilt tripping!"
            else:
                bot "I'll just get her to do it again like last time, she seems to be getting more receptive to my needs already!"
                jump v21_onbed_repeatable_jump
            bo "This feels really good [hin_rel], you always take such good care of me!"
            bo "But I never asked you how you feel about it, do you even like doing this for me?"
            hin "H-huh? W-well, it's not like I enjoy this exactly [bo_name]..."
            scene v21_hinatahate_handy2b at custom_vpunch_repeat(2) with dissolve:
                yalign 0.3
            hint "W-where is this coming from now? Why would he ask that...?"
            hint "It's true that I'm not comfortable at all with the current situation, but I should reassure him that I'm here for him no matter what!"
            hin "N-no, that's not it! I do want to help you, I just don't know how to feel about all this sometimes..."
            hin "You're my [hin_rel_to_bo] and I care about you, but this is so inappropriate and strange to me..."
            scene v21_hinatahate_handy2b at custom_vpunch_repeat(2) with dissolve:
                yalign 0.3
            hin "I know this is just the curse putting us in these tough unorthodox spots, but it's still quite repulsive!"
            call changeHatred(1, "v021_hin_onbedtogether", 1, statlevel=2) from _call_changeHatred_220
            bot "Repulsive? I find using you to be quite exciting actually! Hehehe..."
            bot "I need to get a bit creative here to get her to do what I want today, but I think I can pull this off!"
            bo "R-remember when I was younger and I used to come to you for help with my nightmares?"
            scene v21_hinatahate_handy2b at custom_vpunch_repeat(2) with dissolve:
                yalign 0.3
            hin "Of course I remember sweetie!"
            hin "You used to have really bad dreams about losing me and your [na_rel], right?"
            hin "You would run to me sobbing and inconsolable, and I would tuck you in bed with me and hold you until you fell asleep again."
            bo "Y-yeah, I remember that too... You always made me feel so safe and secure when you were around me."
            bo "Everything happening right now is like I'm living in one of those nightmares, except it's all so real now!"
            bo "And I'm so scared that I might push everyone I care about away."
            scene v21_hinatahate_handyanim_anim at custom_vpunch_repeat(2) with dissolve:
                yalign 0.5
            hin "Oh [bo_name], you shouldn't worry yourself about such things!"
            hin "I'm right here to take care of you, aren't I?!"
            hin "Don't let such fears consume you, you're safe here with me..."
            bo "Mmm... Yeah, I hope so..."
            label v21_onbed_repeatable_jump:
            scene v21_hinatahate_handy2b with dissolve: 
                yalign 0.3
            bo "I have a small request though, if you don't mind..."
            bo "Would it be ok if you held me a bit closer, just like the old times?"
            scene v21_hinatahate_handy2b_2 with dissolve:
                zoom 1.25 xalign -0.0 yalign 0.25 
            hin "O-oh, r-right now? You're not a child anymore t-though, I don't know about that..."
            if hatredlevel2_handjobcounter ==3:
                hint "He wants me to h-hold him closer?!"
                hint "That sounds so inappropriate!"
            else:
                hint "He wants me to hold him in my arms again? I guess he found it really helpful the last time..."
            scene v21_hinatahate_handy2b with dissolve: 
                yalign 0.3
            bo "Yeah... I just really want that feeling of safety right now!"
            bo "Your words are always very soothing, but sometimes they're not enough..."
            bo "Nothing compares to a [hin_rel_mother]'s hug when trying to chase away the darkness."
            bo "I could really use one now [hin_rel]!"
            hin "I-I don't know [bo_name]..."
            hint "It feels so wrong to be any closer to him while doing this with him..."
            hint "But he's practically begging, and I don't want to let him down when he's so vulnerable and scared."
            hint "I just hope this doesn't make everything worse somehow!"
            scene v21_hinatahate_handy2b with dissolve: 
                yalign 0.3
            hin "I-I guess I can try holding you a bit, if you think it will make you feel better..."
            scene black with dissolve
            hin "Make some room for your old [hin_rel_mother] then..."
            scene v21_hinatahate_onbed3 with fade:
                subpixel True yalign 0.8
            bot "Woah, she's right on top of me!" with vpunch
            bo "Mmm... This is nice [hin_rel]..."
            show v21_hinatahate_onbed3 with Dissolve(1):
                subpixel True pos (-636, 1.0) yanchor 0.8 zoom 1.5 
            show v21_hinatahate_onbed3:
                easein 10.0 subpixel True pos (0, 1.45) 
            bot "This is just too easy...!"
            bot "Like a little marionette, dancing to the pull of your strings."
            bot "I've got you wrapped around my little finger, ready to do whatever I want with you!"
            bot "Those juicy breasts on my face are even softer than these pillows, and the aroma off your smooth glistening skin turns me the fuck on!"
            bot "All while you touch me and take care of me..."
            bot "I could just lie here forever!"
            scene v21_hinatahate_onbed2 with dissolve:
                yalign 0.2 
            hin "H-how is this [bo_name]? Is it helping you at all?"
            bo "Y-yeah, it feels super nice having you close..."

            menu hatredlevel2_handjob_onbed_repeatablemenu:
                "{color=[hatredcolor]}Encourage her to finish you off{/color}":
                    if hatredlevel2_handjobcounter == 3:
                        $ hatredlevel2_handjobcounter += 1
                    scene v21_hinatahate_onbed4 with dissolve:
                        yalign 1.0
                    show v21_hinatahate_onbed4:
                        easein 5 subpixel True yalign 0.35    
                    bot "You look so delicious from this angle [hin_rel], I'd eat eat you up right this second, if only you'd let me!"
                    bot "You really know how to turn me on with that body of yours. Keep rubbing those massive tits of yours on me, you sexy MILF!"
                    bot "You belong to me now, you just don't know it yet!"
                    bot "Soon I will get to ravage every inch of your body and make you scream my name in pleasure!"
                    label v21_onbed_repeatable_jump2:
                    hin "E-everything okay [bo_name]? You spaced out a bit, you're not feeling faint or anything, are you?"
                    hin "I-is it your condition making you uncomfortable? We'll get all the pressure out, don't worry!"
                    bo "Y-yeah... I-I'm trying to [hin_rel], don't stop now!"
                    scene v21_hinatahate_onbed2 at custom_vpunch_repeat(2) with dissolve: 
                        yalign 0.2 
                    $ renpy.sound.play("/audio/soun_fx/handjob1.opus", channel="sfx2", loop=True, relative_volume = 0.5)
                    hint "The curse has made all his old childhood nightmares resurface, the poor thing..."
                    hint "And to think I had been letting him deal with it on his own!"
                    hint "I had no idea it was this bad, I should be a lot more attentive to his needs!"
                    show screen parallax1280 ("v21_hinatahate_onbed4_anim",1,0.5, transformeffect=custom_vpunch_repeat(timer=1.1)) with dissolve
                    $ renpy.sound.play("/audio/soun_fx/handjob3.opus", channel="sfx2", loop=True, relative_volume = 0.5)
                    call showscrollingimage from _call_showscrollingimage_288
                    bot "Oh shit, she's speeding up and really getting into it now!"
                    bot "Look at how far you've come [hin_rel], willing to please me while sharing my bed..."
                    bot "Keep helping me release all this cum I've built up just for you!"
                    bo "Ahh... Yes... Just like that..."
                    hint "My poor little boy... H-how did we even end up in this situation?!"
                    hint "I need to stay strong for both of our sakes, no matter what the world throws at us!"
                    hin "I-it's alright sweetie, you're safe now..."
                    hin "We j-just need to get it all o-out!"
                    bo "Y-yeah... I'm getting c-close..."
                    bot"I'll smear her with it, I want to feel her warmth!"
                    hint "Oh gosh, is he reaching his limits already? I need to be careful to not release it everywhere."
                    if toji_pay300 == True or toji_defeated == True or v21_hatredhandjob_cumonface == True:
                        hint "I don't want it all over me and my face like that other time!"
                    scene v21_hinatahate_onbed4:
                        yalign 0.35    
                    call hidescrollingimage("Click twice to cum!") from _call_hidescrollingimage_232
                    stop sfx2 fadeout 2
                    bo "O-oh fuck [hin_rel]...! You're so fucking-..."
                    bo "-... AAAAH!" with flash 
                    $ renpy.sound.play("/audio/soun_fx/cum4.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                    scene v21_hinatahate_onbed4cum with flash:
                        yalign 0.35
                    bo "*Moans loudly* A-aaahh!!" with vpunch
                    call decreaselust (50) from _call_decreaselust_141
                    scene black with fade
                    hin"[bo_name_stutter]! W-what has gotten into you!?"
                    show v21_hinatahate_onbedcuddle1_evil with dissolve:
                        yalign 1.0
                    show v21_hinatahate_onbedcuddle1_evil:
                        easein 5 subpixel True yalign 0.2
                    hin"You can't j-just spill it everywhere!"
                    bo"I just had to feel your embrace, [hin_rel]! I was scared, I'm sorry..."
                    hint"D-darn it! This has gone way too far, but I can't turn on him now. Not when he needs me the most..."
                    hin"... *Sigh*"
                    hin"You soiled my clothes, and your bedsheets, you d-dummy!"
                    scene black with dissolve
                    "[hin_name] pulls you closer into a tight embrace, trying to provide you with some extra comfort."
                    show screen parallax1280("v21_hinatahate_onbedcuddle2_evil",1,0.0) with dissolve
                    call showscrollingimage from _call_showscrollingimage_289
                    hin "There, there... That should do it..."
                    hin "Everything is going to be okay!"
                    bot "Look at her, still trying to comfort me even after I came all over her clothes!"
                    bot "She's so oblivious as to what is going on! But still so fucking hot!"
                    hin "How are you feeling? Has all the pain and fear subsided for now?"
                    $ renpy.sound.play("/audio/soun_fx/horror.opus", channel="sfx2", loop=False, relative_volume = 0.5) 
                    call changeHatred(1,"v021_hin_bedtogether",1, statlevel = 2) from _call_changeHatred_205
                    bot "Fear? I'm not the one that should be scared [hin_rel], if only you knew what else I have planned in store for you hehe..."
                    bo "Y-yeah it's all better now..."
                    bo "Thanks [hin_rel]... This means more to me than you can imagine."
                    hin "You're a handful sometimes, but you're still my sweet [hin_rel_to_bo], I'm glad to have you around!"
                    bo "I'll let you know if I need more help, it makes me feel so much safer knowing that you're here for me."
                    hin "M-more help? *sigh*"
                    hint "I keep telling myself that it'll be the last time, but somehow I always end up here again..."
                    hin "J-just try not to bottle it all up inside and suffer on your own, okay?"
                    scene black with dissolve
                    call hidescrollingimage("Click twice to let her go.") from _call_hidescrollingimage_233
                    hin "O-okay well! You seem back to your old self again, so I'm going to go get started on everything that needs to be done."
                    hin "As much as I'd love to stay here and comfort you all morning..."
                    scene hina leavebobedroom with dissolve
                    hin "...I still have chores to do!"
                    hin "I left a towel for you. Please clean after yourself and drop it in the laundry basket, okay?"
                    bo "Okay... Thanks for everything, [hin_rel]!"
                    scene black with fade
                    $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    "You get yourself cleaned up and get dressed, while [hin_name] takes the laundry away."
                    bot "I've got her wrapped around my finger now, she can't resist me anymore!"
                    if quest_hin.check("hin2H_1", "in progress"):
                        $ notification("Quest updated")
                        $ quest_hin.check("hin2H_1", "completed")
                        $ quest_hin.check("1_hin2H", "completed")                        
                    bot "I wonder what else I could get her to do for me in the future..."
                    $ renpy.end_replay()
                    jump wakeupend

                "{color=[hatredcolor]}I need to grope those juicy tits!{/color}" if hatredlevel2_handjobcounter >=3:
                    call checkObedience(0,"hatredlevel2_handjob_onbed_repeatablemenu", "Hinata", 2) from _call_checkObedience_61
                    if hatredlevel2_handjobcounter == 3:
                        $ hatredlevel2_handjobcounter += 1
                    scene v21_hinatahate_onbed4 with dissolve:
                        yalign 1.0
                    show v21_hinatahate_onbed4:
                        easein 5 subpixel True yalign 0.3    
                    bot "Today I'm not holding back, I want to enjoy those melons of yours [hin_rel]!"
                    bot "I need them to keep my hands busy while you're jerking me off..."
                    show v21_hinatahate_onbed4:
                        yalign 0.3    
                    show v21_hinatahate_onbed4:
                        subpixel True xpos -200 ypos -0.25 zoom 1.3 
                    with Dissolve(1)
                    bot "I mean, just look at them! How could I ever resist?"
                    bot "They're practically begging for attention!"
                    scene v21_hinatahate_onbed4 with dissolve:
                        yalign 0.3    
                    bot "I have no idea what I could possibly say to justify wanting to give them a little squeeze, but maybe that won't matter anymore..."
                    bot "She's been jerking me off so many mornings now that hopefully she'll just go along with it..."
                    bot "Maybe she might not even notice!"
                    scene v21_hinatahate_onbedgrope1_2 with dissolve:
                        yalign 0.5
                    $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                    hin "...[bo_name_stutter]?!" with vpunch
                    hin "W-what do you think you are doing exactly?!"
                    bot "Well shit... So much for not noticing..."
                    bot "Ah I'm sure it's fine, let me just focus on enjoying myself here!"
                    $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                    hin "Y-you can't just t-touch me like that, stop it!" with vpunch
                    bo "Mmmm..."
                    menu:
                        hin "Y-you can't just t-touch me like that, stop it!"
                        "{color=[hatredcolor]}Squeeze!{/color}":
                            pass
                        
                    bot "Who says I can't?! Watch me..." with vpunch
                    scene v21_hinatahate_onbedgrope1_2_angry_anim with dissolve:
                        yalign 0.5
                    $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                    hin "Hello?! Are you even listening to me?!"
                    bot"I sure am, but fuck do these feel good, [hin_rel]..."
                    call changeRespect("Hinata", -2) from _call_changeRespect_270
                    hin "...[bo_name_stutter]?!" with vpunch
                    bot "Shut up already and let me do my thing..."
                    hint "What in the world is he doing?! He's not even responding to me!"
                    hint "Since when does he think I'm okay with him groping me like this?!"
                    hin "[bo_name], can you hear me?!" with vpunch
                    bo "Mmmm-..."
                    scene v21_hinatahate_onbedgrope1_2 with dissolve:
                        yalign 0.5
                    hint "It's been affecting him in so many weird ways, I guess this is just another one of them..."
                    hint "Did he zone out or fall asleep perhaps?"
                    hint "It's as if his brain shut down and he's just going through the motions now..."
                    hint "I-I don't know what to do though... Should I just let him keep doing this to me?!"
                    hint "This can't be normal..."
                    bot "Oh yeah, these are so soft and squishy!"
                    bot "Did she just give in and let me do it? She's not putting up much of a fight!"
                    hint "It's almost like he's in a trance, maybe he's not aware of what he's doing?"
                    scene v21_hinatahate_onbedgrope1_2 with dissolve: 
                        yalign 0.5
                    hint "It could be dangerous to try and stop him now, I don't want to startle or upset him!"
                    call changeObedience("Hinata", 1, "v21_hinata_handjob_onbedgrope1", 1,2) from _call_changeObedience_177
                    hint "M-maybe I'll give him a second, till he calms down and comes back to his senses?"
                    bot "She's not pushing me away just yet, time to bury my face in these lovely funbags of hers!"
                    scene v21_hinatahate_onbedgrope2 with dissolve
                    $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                    bot "Oh yeah, this is the stuff!" with vpunch
                    bot "Free those tits a bit for better access! I wish I could suck on those nipples too..."
                    bot "[hin_rel] is so fucking hot!"
                    scene v21_hinatahate_onbedgrope2 with dissolve:
                        yalign 0.5
                    hint "I-is he trying to put my breast in his m-mouth?!" with vpunch
                    hint "I don't care if he doesn't realize what he's doing to me, this is not appropriate..."
                    $ renpy.sound.play("/audio/soun_fx/grope1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                    hint "I can feel his hand squeezing quite hard too, I need to put a stop to this!"
                    hin "[bo_name], please... Y-you're hurting me!"
                    hin "Snap out of it!" with vpunch
                    bot "Ughhh, fine! I shouldn't upset her too much if I want to do this again..."
                    bot "Party pooper..."
                    scene v21_hinatahate_onbedgrope2_openeyes with dissolve:
                        yalign 0.7
                    bo "H-huh? What's wrong? [hin_rel]?"
                    hint "He's opening his eyes, finally!"
                    hint "Was he really asleep this whole time?!"
                    scene v21_hinatahate_onbed4 with dissolve:
                        yalign 1.0
                    show v21_hinatahate_onbed4:
                        easein 5 subpixel True yalign 0.3    
                    jump v21_onbed_repeatable_jump2

        "{color=[hatredcolor]}???{/color}" if hatredlevel2_handjobcounter <1:
            "Complete previous options to make [hin_name] more comfortable for this option."
            jump hatredlevel2_handjob_repeatablemenu

        "{color=[hatredcolor]}???{/color}" if hatredlevel2_handjobcounter <2:
            "Complete previous options to make [hin_name] more comfortable for this option."
            jump hatredlevel2_handjob_repeatablemenu

        "{color=[obediencecolor]}???{/color}" if hatredlevel2_handjobcounter <3:
            "Complete previous options to make [hin_name] more comfortable for this option."
            jump hatredlevel2_handjob_repeatablemenu