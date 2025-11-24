# Love variation mirrors the hatred path
# hatredlevel2_handjobcounter unlocks: 0 - intro, 1 - used for love check fail, **2 - skipped**, 3 - repeat or cuddle handjob, 4 - random wakeup event unlocked


# Stat acquisition:
# Level 2 love point acquisition here total: 4
# Level 2 hinata obedience point acquisition here total: 2

label hatredlevel2_intro_chosenlove:

    $ initialize_replay_defaults()
    scene bg day:
        zoom 0.70
    show hinaq1bg
    show hina quest1_4t
    show bobedx 3:
        matrixtransform ScaleMatrix(1.0, 0.6, 1.0)*OffsetMatrix(1.0, 238.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)
        alpha 1
    with dissolve

    call randomCheck(True,f"{{color={lovecolor}}}Love {{/color}}check{{color=#00ff00}} passed{{/color}}") from _call_randomCheck_21
    bot "[hin_rel] has always been there for me, and I know she cares about me deeply."
    show bobedx 6 zorder 100 with dissolve:
        matrixtransform ScaleMatrix(1.0, 0.6, 1.0)*OffsetMatrix(1.0, 238.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)
        alpha 1.00
    bot "Watching her drives me crazy though, and I'd love to have her help me a bit more with this curse!"
    bot "I can't just force her to though, and I'm sure she'd be really uncomfortable with anything inappropriate..."
    bot "But I can't help it, I have to try!" with vpunch
    show bobedx 3 zorder 100 with dissolve:
        matrixtransform ScaleMatrix(1.0, 0.6, 1.0)*OffsetMatrix(1.0, 238.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)
        alpha 1.00
    bo "Listen [hin_rel], we really need to sit down and discuss all of this a bit, I feel like I'm starting to really lose it!"
    show bobedx 3 with dissolve:
        alpha 0.20
    hin "[bo_name] I already said I'm sorry and that I wasn't trying to wake you up..."
    show hina quest1_1t with dissolve
    show hina quest1_1t:
        easein 2 xpos -360
    hin "It's really not that big of a deal, go back to sleep if you're still tired!"
    show hina quest2_1 with dissolve:
        xzoom -1 xpos -0.25
    hin "I'm just trying to keep things in order around here to help you be more comfortable."
    show bobedx 3 zorder 100 with dissolve:
        alpha 1.00
    bo "I know [hin_rel], and you're the best for that! But that's not what I meant..."
    show hina quest2_1 with dissolve:
        xzoom 1 xpos -0.25
    show hina quest2_1:
        easein 2 xpos 0
    bo "It's the whole deal with this curse and how it affects me every day!"
    show bobedx 6 zorder 100 with dissolve
    bo "My life has become such a mess recently and I feel like I'm losing my mind..."
    show hina quest1_4t with dissolve
    hin "I-I know it's been hard for you dear, but I'm here for you to help you through all of this."
    hin "You just have to be strong!"
    show bobedx 3 with dissolve:
        alpha 1.00
    bo "Well that's the thing [hin_rel]..." 
    bo "I don't know how much longer I can just be strong for..."
    show bobedx 6 zorder 100 with dissolve
    bo "I appreciate everything you do but..."
    bo "Things are getting worse!" with vpunch
    hide hina
    hide shina
    show shina shy at center
    with dissolve
    show shina shy at smallshake
    hin "W-worse? What do you mean by that?"
    show bobedx 3 with dissolve:
        alpha 1.00
    bo "Well... Everything has just been piling up, one issue on top of the other!"
    bo "I'm wearing myself really thin, trying to help with everything..."
    if ch1_dy_200paid == True or toji_pay300 == True:
        bo "All the hard work to make the money to pay our debts has been especially taking a toll!"
    show bobedx 6 zorder 100 with dissolve
    bo "I've also been stressing out with protecting [him_name] from the truth too, like you asked me to!"
    bo "And on top of that, I'm constantly on my toes to maintain control over my emotions and impulses on the daily!"
    bo "I-I just..."
    bo "I'm tired [hin_rel]!" with vpunch
    bo "Life is throwing so much at us right now... And at me especially!"
    show shina surprised2 with dissolve
    hin "Y-you're right... You know, life has a tendency to kick us when we're down, [bo_name]!"
    hin "But true strength from within is what allows us to pick ourselves back up again and keep going!"
    hin "We tend to focus on the negatives when we start to lose hope, and all those doubts and fears start to creep in."
    hin "But I need you to be strong for me right now, alright?"
    hin "Just do your best, and no matter what happens... I want you to know that I'm proud of you [hin_rel_to_bo]!"
    show bobedx 3 zorder 100 with dissolve:
        alpha 1.0
    bo "Are you really though...?"
    bo "Even when I'm acting up because of all my impulses?"
    show bobedx 6 zorder 100 with dissolve
    bo "I struggle a lot with my urges, they plant all these intense emotions and images into my head!"
    bo "It's extremely isolating sometimes, because I'm constantly afraid of what I might do next!" with vpunch 
    show bobedx 3 zorder 100
    show shina worried
    with dissolve
    bo "I honestly wouldn't blame you if you decided one day that you didn't want anything to do with me anymore..."
    show shina surprised with dissolve
    show shina at smallshake
    hin "H-hey, come on! Don't say that! I care about you [bo_name], you know that!"
    call changeLove("Hinata", 1, statlevel=1) from _call_changeLove_61
    hin "You've always been my sweet boy, and I have never stopped loving you!"
    show shina shy with dissolve
    hin "I-I just... Well..."
    hin "I just don't know how to help sometimes, it can feel quite inappropriate and overwhelming for me as your [hin_rel_mother]..."
    show shina surprised2 with dissolve
    show shina surprised2 at smallshake
    hin "But we will find a way, we always do!"
    show shina shy2 with dissolve
    hin "It pains me to hear you express these inner concerns though... I had no idea you felt that way, I'm so sorry [bo_name]!"
    show bobedx 6 zorder 100 with dissolve:
        alpha 1.00
    bot "[hin_rel] seems to be genuinely concerned about me, but I can tell it's a grey cloud looming above her too."
    bot "She doesn't like the way things are going one bit! But she will learn to accept it..."
    bot "You'll finally see me for the man I have become [hin_rel], instead of the innocent little boy you used to know!"
    show bobedx 6:
        alpha 0.2

    # show hinaq1bg:
    #     zoom 1.5 yalign 0.7 xalign 0.5
    # show shina:
    #     zoom 1.5 yalign 0.7 xalign 0.5
    # with Dissolve(1.0)
    bot "And fucking hell, the emotions you stir in me every time I look at you are just so intense!"
    bot "I want to forget about everything going on and just explore every inch of that body with my fingertips..."
    call increaselust(10) from _call_increaselust_286
    show hinaq1bg:
        zoom 1 yalign 0.0 xalign 0.0
    hide shina
    show shina shy2 at center
    with Dissolve(1.0)
    show bobedx 4 zorder 100:
        alpha 1.00
    # camera:
    #     subpixel True pos (0, 0) zoom 1.0 
    # with Dissolve(1.0)
    bot "Soon... Good things come to those who wait, and damn do you look good!"
    bo "I just can't keep pretending that everything is okay when it's obviously not [hin_rel]!"
    show shina worried with dissolve
    hin "Oh [bo_name]... I see all this weight on your shoulders, dragging you down..."
    hin "I want you to know that if your strength waivers and falters, I'm here for you to lean on!"
    show bobedx 6 zorder 100 with dissolve
    bot "I want to do a lot more than just to lean on you [hin_rel]!"
    bot "But perhaps this is an opening to finally be offered more help for my urges?"

    menu hatredlevel2_intro_chosenlove_menu:
        "{color=[lovecolor]}I can't do this alone!{/color}":
            bo "You say you're here for me, but I feel so alone in all of this [hin_rel]..."
            show bobedx at smallshake
            bo "Even now, I can feel it all gnawing at the back of my mind, trying to make me lose control!"
            show shina surprised4 with dissolve
            bo "The pain and throbbing down there, it's a constant reminder of my struggles!"
            show shina surprised4 at smallshake
            hin "W-wait, t-throbbing?!" with vpunch
            show shina concerned with dissolve
            bo "Yeah, especially in the mornings! I often feel like I'm about to burst!"
            bo "It gets so bad that I can't even think straight sometimes..."
            show shina shy with dissolve
            hint "That does explain why he seems a bit aggressive and so impulsive on some mornings..."
            bo "I need help with this... Please [hin_rel]..."
            label v21_handjob_lovecheckdelayedintro_jump:
            $ renpy.sound.play("/audio/soun_fx/clothes_undress.opus", channel="sfx3", loop=False, relative_volume = 0.7)
            show bobedx f1 zorder 100 with Dissolve(1)
            bo "Take a look at what's happening to me, I'm such a mess!"
            show shina surprised5 with dissolve
            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            hin "*Gasp*!" with vpunch
            hin "H-hey...! You can't jus-..."
            bo "I'm really sorry [hin_rel], I just don't know what else to do... It hurts so much!"
            bo "I never asked for this!" with vpunch
            bo "I never wanted to be like this, to be a burden to you..."
            show shina concerned
            show bobedx f2
            with dissolve
            bo "I just wish I could go back to my old self. To be happy again, to be loved, to be accepted as I am..."
            bo "But instead, all I feel is anger, frustration, and pain!"
            bo "I need someone, [hin_rel]... I need your s-support!"
            scene black with dissolve
            $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 0.7)
            "[hin_name] takes a seat next to you on the bed, still shook by your revelation, but determined to find a solution..."
            scene v21_hinatahate_hand grab_c with dissolve: 
                yalign 1.0
            show v21_hinatahate_hand grab_c:
                easein 5 subpixel True yalign 0.3
            hin "[bo_name_stutter], I'm here to support you, you know that..."
            hin "It's just... I don't really know how I can be of any h-help... You know, with how your condition affects you.{p}W-what is it exactly you expect me to do?"
            show v21_hinatahate_hand grab_c_2 with dissolve
            bo "I-... I don't know... I just wish things weren't as... complicated."
            bo "One thing is clear to me... I need {i}your help{/i}, [hin_rel]..."
            hin"..."
            hint "To even be considering this is... insane! B-but..."
            call checkLove(0, "v21_handjob_lovecheckfailjump","Hinata", statlevel=2) from _call_checkLove_20
            hint "If not me... Then who will step in and help...?"
            scene v21_hinatahate_hand grab lovestart with dissolve:
                yalign 0.3
            "[hin_name] faces towards you and tentatively grasps your curse-stricken manhood, concern and hesitation evident in her eyes."
            call increaselust(10) from _call_increaselust_287
            bot "[hin_rel] is actually touching me like this, I can't believe it!"
            bo "[hin_rel_stutter]..." with vpunch
            hin "Y-you said it hurts... r-right?"
            bo "R-right..."
            hin "That you feel alone, scared..."
            bo "..."
            hin "Well... You are not..."
            scene v21_hinatahate_hand grab 3a with dissolve: 
                yalign 0.3
            hin "Even if this isn't right... I'll t-try to help. This one time only..."
            scene v21_hinatahate_hand grab 3a_3b with Dissolve(1):
                yalign 0.3
            hint "Is this really what he w-wants? It's so w-wrong, how can he be ok with this?!"
            hint "I hate the fact that I'm even considering this! But if it's the only way I can help then..."
            if toji_pay300 == True or toji_defeated == True:
                hint "Besides, it wouldn't be the first time I help him, only this time he is wide awake! He was never supposed to know..."
                hint "Am I really about to go down this path?"
            hint "He wouldn't be asking if it wasn't absolutely necessary, r-right?"
            hint "Oh [na_name]... I wish you were here to help us!"
            hint "I guess it's all up to me now to make things right..."
            $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 0.7)
            show screen parallax1280 ("v21_hinatahate_onbed1_2",1,0.2) with dissolve 
            call showscrollingimage from _call_showscrollingimage_290
            hin "L-like I said, this is j-just a one-time only occurence, okay?"
            bo "R-right..."
            hin "I'm your [hin_rel_mother] afterall, it's my duty to p-protect you... Even from yourself!"
            hint "This is so crazy, I can't believe I'm actually doing this..."
            hint "I-I need to be strong... {p}I need to show him that I'm here for him no matter what!"
            bo "Y-yeah... We're in this together!"
            bot "I don't know what I did to deserve you [hin_rel], but the way you make me feel is incredible!"
            show screen parallax1280 ("v21_hinatahate_onbed1",1,0.2) with dissolve 
            bot "Especially with your hand on my hard cock like that!" with vpunch
            bot "This is so exciting!"
            scene black
            call hidescrollingimage from _call_hidescrollingimage_234
            scene v21_hinatahate_handyanim_a with dissolve: 
                yalign 1.0  
            show v21_hinatahate_handyanim_a:
                easein 3 subpixel True yalign 0.5 
            hin "I know this isn't easy on you, but it isn't for me either!"
            hin "But as long as we both s-stay calm, and understanding of each other then..."
            hin "...Everything will be alright, I p-promise!"
            show v21_hinatahate_handyanim_a2 with dissolve:
                yalign 0.5
            bot"Oh f-fuck! She just stroked me!" with vpunch
            bo "Ahh y-yeah, that sounds good to me [hin_rel]..."
            $ renpy.sound.play("/audio/soun_fx/handjob4.opus", channel="sfx3", loop=False, relative_volume = 0.6)
            show v21_hinatahate_handyanim_anim at custom_vpunch_repeat(2) with dissolve:
                yalign 0.5
            bot"[hin_rel] is jerking me off willingly!"
            hint "This is so surreal, I can't believe I'm actually doing this..."
            hint "But I need to be stay strong... {p}I have to let him know that I'll be there for him, no matter what..."
            hin "I-is this alright? Is it helping?"
            bot "It's not just alright, it's amazing! Keep stroking that hard cock for me!"
            bo "Y-yeah keep going, it feels nice..."
            hin"N-nice...? I thought you a-are in pain...."
            bo "I a-am! I just meant that it's relieving the pain a bit..."
            hin"Oh okay, if you think it h-helps..."
            scene v21_hinatahate_onbed1_2 with dissolve:
                yalign 0.3
            hin "Is this n-normal? It feels so h-hard and tense!"
            hin "Should we book an appointment at the infirmary to get it checked out?"
            show screen parallax1280("v21_hinatahate_handyanim_anim",1,0.5) with dissolve
            call showscrollingimage from _call_showscrollingimage_291
            bo "N-no! No need..."
            bo "This is how it always is when it hurts..."
            bo "You're making it feel better though, don't stop!"
            hin "I... I am trying, but this is quite uncomfortable..."
            show screen parallax1280("blackscreen",1,0.5) with dissolve
            hin"Think you can lay back a little bit?"
            hide screen parallax1280
            show screen parallax1280("v21_hinatahate_handylookupsad",1,0)
            with dissolve
            bot "Why not, I'll just lay back and let her do her thing!"
            hint"It barely fits in my palm..."
            hint "I had no idea men's things could get so... hardened."
            hint"I can even feel it pulsating every time I r-rub it..."
            hint "I've never felt anything like this with [na_name] before..."
            show screen parallax1280("v21_hinatahate_handylookupsad",1) with dissolve
            hint "I had no idea it was this difficult, this painful... To think he's been dealing with it on his own for so long!"
            hint "I need to be a better [hin_rel_mother] for him, even if it means that..."
            scene black
            call hidescrollingimage from _call_hidescrollingimage_235
            $ renpy.sound.play("/audio/soun_fx/handjob5.opus", channel="sfx2", loop=True, relative_volume = 0.5)
            show v21_hinatahate_handyanim_animfast at custom_vpunch_repeat(1.1) with dissolve
            bot"Oh f-fuck!" with vpunch
            hint"Even if it means that sometimes, I'll have to take care of his t-troubles..."
            bot "She's really getting into it now, stroking me with both hands!"
            bot "I'm really liking this side of her..."
            bot "Having her motherly instincts kick in to protect me with her bare hands! It's hot!"
            bot "Look at them go, up and down that hard shaft... She's so perfect!"
            bot "I'll repay the favor soon [hin_rel], I promise!"
            bo "Ahh... Yes... Just like that! Keep it going [hin_rel]!"
            hin" P-please... No n-need for commentary!"
            hint "T-this is so embarrassing... H-how did we even end up in this situation?!"
            hint "I need to stay strong and get this over with... For both of our sakes!"
            stop sfx2 fadeout 2
            scene v21_hinatahate_handy2b at custom_vpunch_repeat(2) with dissolve:
                yalign 0.3
            hin "We're going to get it all of your system, don't worry!"
            hin "We'll deal with this c-curse, together! We won't let it tear this household apart!"
            bot "She's right, this damned curse is so overbearing!"
            bot "Although maybe it was a blessing a disguise, it's bringing us so much closer together in a way!"
            bot "I would have never imagined that I'd be having [hin_rel] jerk me off like this under normal circumstances!"
            scene v21_hinatahate_handy2b_1 with dissolve:
                yalign 0.3
            bo "Y-yes... I'm getting c-close..."
            scene v21_hinatahate_handy2b_2 with dissolve: 
                yalign 0.3
            hint "Oh heavens, he is s-squirming! is he about to climax? {p}I h-have to be careful not to make a mess!"
            if toji_pay300 == True or toji_defeated == True:
                hint "I don't want it all over me and my face like last time!"
            hint "No turning back now..."
            bo "O-oh fuck! You're the best [hin_rel] ev-..."
            bo "-... AAAAH!" with vpunch 
            $ renpy.sound.play("/audio/soun_fx/cum2.opus", channel="sfx2", loop=False, relative_volume = 0.3)
            scene v21_hinatahate_handy2b_2c with flash 
            pause 0.2
            $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx2", loop=False, relative_volume = 0.3)
            scene v21_hinatahate_handy2b_2c2 with flash 
            pause 0.2
            $ renpy.sound.play("/audio/soun_fx/cum4.opus", channel="sfx2", loop=False, relative_volume = 0.3)
            scene v21_hinatahate_handy2b_2c3 with flash 
            pause 0.7
            call decreaselust (50) from _call_decreaselust_142
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
            bo "Ahh... It's good to get it all out!"
            bot "Look at her still trying to comfort me even with my cum all over her delicate hand..."
            bot "She's so caring and compassionate, on top of being so naturally beautiful!"
            bot "What would I do without her?!"
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
            call changeLove("Hinata", 1, statlevel=2) from _call_changeLove_62
            bo "Y-yeah it's all better now... All thanks to you [hin_rel]!"
            hin "[bo_name]..."
            bo "I'll let you know if I need more help, it makes me feel so much safer knowing that you're here for me."
            hin "...M-more help?"
            scene v21_hinatahate_handylookupthinking_b1 with dissolve: 
                yalign 0.0
            hint"I knew he'd get the wrong idea..."
            hint "I will have to figure out some other way of helping. This cannot be a recurring act..."
            hint "What have I gotten myself into..."
            scene v21_hinatahate_handylookupthinking_b with dissolve:
                yalign 0.0
            bo "Y-yeah some mornings are tough, but with your help I'm sure we can get through them a lot easier!"
            hin "I-I see... Although today was an e-exception. We cannot do that again. Not unless it's absolutely necessary, a last resort..."
            $ notification ("Wake-up event options unlocked")
            bo"Right..."
            bot "Hopefully she'll change her mind about that, I really enjoyed this!"
            hin "*Sigh*... Let's both do our best to get through this, alright?"
            scene hina leavebobedroom with dissolve
            hin "I left a towel for you. Please clean after yourself and drop it in the laundry basket, okay?"
            bo "Okay... Thanks for everything, [hin_rel]!"
            scene black with fade
            $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            "You get yourself cleaned up and get dressed, while [hin_name] takes the laundry away."
            bot "I can't believe that just happened!"
            bot "Cumming feels so much better when it's with her... and on her! Hahah..."
            bot "I hope it happens again soon... I can't wait!"
            $ renpy.end_replay()
            $ quest_hin.check("4_hin2L", "in progress")
            $ notification("Quest updated")
            $ hatredlevel2_handjobcounter = 3
            jump wakeupend

# Show repeatable options so players know to repeat the scene, hatred will never be accessible here
        "{color=[hatredcolor]}???{/color}" if hatredlevel2_handjobcounter <1:
            "This option is blocked for the love path!"
            jump hatredlevel2_intro_chosenlove_menu

        "{color=[hatredcolor]}???{/color}" if hatredlevel2_handjobcounter <2:
            "This option is blocked for the love path!"
            jump hatredlevel2_intro_chosenlove_menu

        "{color=[obediencecolor]}???{/color}" if hatredlevel2_handjobcounter <3:
            "Complete previous options first to make [hin_name] more comfortable."
            jump hatredlevel2_intro_chosenlove_menu




label hatredlevel2_handjob_chosenlove_repeatable:

    $ initialize_replay_defaults()
    scene bg day:
        zoom 0.70
    show hinaq1bg
    show hina quest1_4t
    show bobedx 3 zorder 100:
        matrixtransform ScaleMatrix(1.0, 0.6, 1.0)*OffsetMatrix(1.0, 238.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)
        alpha 1
    with dissolve

    bo "I need help with the curse again, it's getting really bad!"
    hide hina
    hide shina
    show shina surprised2 at center
    with dissolve
    hin "Oh no, is it happening a-again? Are you alright?!"
    if hatredlevel2_handjobcounter >2:
        bot "I'm kinda just craving more of her attention, but I can't tell her that!"
    if hatredlevel2_handjobcounter <4:
        bot "I can feel the tension in the air, she's still quite hesitant but maybe will still help..."
    else:
        bot "[hin_rel] has helped me a couple of times already, I'm sure she wouldn't mind doing it again..."
    bo "I-I'm trying to get through it but I really need you right now..."
    show shina worried
    show bobedx 3 zorder 100:
        alpha 1.00
    with dissolve
    hint "My poor boy, that darn curse is getting to him again!"
    hint "But what does he mean by 'help'? I hope it's not what I think it is..."
    if hatredlevel2_handjobcounter == 1:
        hint "I thought we went through this already, it's not right for him to ask for physical favors like this!"
        hint "He must really be desperate to be insisting on it..."
        jump v21_handjob_lovecheckdelayedintro_jump
    hint "I really shouldn't be doing this but what other options do we have?"
    hint "He needs me..." with vpunch
    if hatredlevel2_handjobcounter <4:
        hint "We've already crossed this line, but that doesn't make it any less inappropriate!"
        hint "It would be cruel to deny him when he's in pain, but I can't keep doing this!"
        hint "Be strong for him... {p}I've overcome a lot harder challenges in life than this, don't overthink and just do it!"
    else:
        hint "I worry about him so much whenever this happens, but this is so wrong!"
        hint "We have to expel the curse's effect though..."
    show shina at smallshake
    hin "[bo_name] this isn't right you know..."
    hin "You can't just expect me to help you with this every time it happens!"
    hin "Show me where it hurts today though and I'll take a look. {p}I-is it down there again?"
    show bobedx 6 zorder 100 with dissolve
    bo "Y-yeah... And it's really bad today..."
    bot "I wish I could get [hin_rel] to be more on board with this..."
    bot "Her touch is so soft and gentle, it makes me tingle just thinking about it!"
    bot "I can't push her too far though, I need to take it slow and make sure she's comfortable first."
    $ renpy.sound.play("/audio/soun_fx/clothes_undress.opus", channel="sfx3", loop=False, relative_volume = 0.7)
    show bobedx f1 zorder 100 with Dissolve(1)
    bo "Come take a look [hin_rel], I'm a mess!"
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
    "She takes a deep breath and slowly wraps her hand around your shaft, feeling the warmth and tension on her palm."
    scene v21_hinatahate_handyanim_a with dissolve:     
        yalign 1.0  
    show v21_hinatahate_handyanim_a:
        easein 5 subpixel True yalign 0.5 
    hint "It doesn't feel much different from the last time, I can still feel that scorching heat radiating from it..."
    hint "These episodes seem really intense, I can't imagine how he gets through them..."
    bo "Ahh yeah, that feels good..."
    bot "Go on [hin_rel], work your magic!"
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

    menu hatredlevel2_handjob_chosenlove_repeatablemenu:
        hin "You can always count on me [bo_name], for w-whatever you need!"
        "{color=[lovecolor]}You're all I'll ever need!{/color}":
            call randomCheck(True,f"{{color={lovecolor}}}Love {{/color}}check{{color=#00ff00}} passed{{/color}}") from _call_randomCheck_22
            bo "This is great [hin_rel], you're always what I need..."
            bo "I'm just grateful for everything you do for me!"
            bot "Keep working that shaft like that so I can cum all over your hand again!"
            bot "I always save it all for you..."
            bo "I just need all this pressure out of my system, and I can feel it getting better already!"
            hin "O-okay... We'll get it all out again, d-don't worry!"
            bo "You're making it feel a lot more relaxed, don't stop!"
            show screen parallax1280("v21_hinatahate_handylookupsad",1,0) with dissolve
            call showscrollingimage from _call_showscrollingimage_292
            hint "This is so crazy, I can't believe I'm actually doing this again..."
            hint "How is he ALWAYS so firm when he asks for help?!"
            hint "It's like a slab of granite rock in my hand, left out in the sun and scorching hot to the touch!"
            show screen parallax1280("v21_hinatahate_handylookupsad",1) with dissolve
            hint "Has he been forced to walk around like this when he can't take care of himself?"
            hint "The poor thing, and to think I had been letting him deal with it on his own..."
            hint "I need to be a better [hin_rel_mother] for him!"
            scene black
            call hidescrollingimage from _call_hidescrollingimage_236
            $ renpy.sound.play("/audio/soun_fx/handjob5.opus", channel="sfx2", loop=True, relative_volume = 0.5)
            show v21_hinatahate_handyanim_animfast at custom_vpunch_repeat(1.1) with dissolve
            bot "Oh shit, she's speeding up and really getting into it now!"
            bot "I'm really liking this side of her..."
            bot "Having her motherly instincts kick in to protect me with her bare hands! It's hot!"
            bot "Look at them go, up and down that hard shaft... She's so perfect!"
            bot "I'll repay the favor soon [hin_rel], I promise!"
            bo "Ahh... Yes... Just like that! Keep it going [hin_rel]!"
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
            bo "O-oh fuck! You're the best [hin_rel] ev-..."
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
            call decreaselust (50) from _call_decreaselust_143
            show v21_hinatahate_handy2b_2c3:
                easein 4 yalign 0.1
            hint "What the heck, why is it always so much and so sticky?! {p}Ughh, look at how it gets everywhere!"
            bo "*groans* Ah yeah..."
            hint "I need to stay calm. It's... over, right?"
            scene v21_hinatahate_povonbed2_bc with dissolve: 
                yalign 1.0
            show v21_hinatahate_povonbed2_bc:
                easein 5.0 subpixel True yalign 0.0
            hin "T-there... are you f-feeling better?"
            bo "Ahh... It's good to get it all out!"
            bot "Look at her still trying to comfort me even with my cum all over her delicate hand..."
            bot "She's so caring and compassionate, on top of being so naturally beautiful!"
            bot "What would I do without her?!"
            hin"...[bo_name_stutter]?" with vpunch
            bo"Y-yeah! Thanks for your help, [hin_rel]!"
            scene black with dissolve
            "[hin_name] fetches a hand towel and quickly cleans herself up before she turns to address you..."
            scene v21_hinatahate_handylookupthinking_b with dissolve:
                yalign 0.0
            show v21_hinatahate_handylookupthinking_b:
                easein 4 yalign 0.3
            bo "It feels so much fucking better now... all thanks to you!"
            hin "N-no need to use foul language! But I'm glad you're feeling better..."
            hin "Is it over now? Has all the pain subsided?"
            call changeLove("Hinata",1,"v021_hin_whatineedlove",1,2) from _call_changeLove_63
            bo "Y-yeah it's all better now... All thanks to you [hin_rel]!"
            bo "I'm just glad I have you to take care of me! I know that I can trust you with everything..."
            hin "[bo_name]..."
            hin "Of course, you can always trust me! You're my sweet [hin_rel_to_bo], I'm glad to have you too!"
            bo "I'll let you know if I need more help, it makes me feel so much safer knowing that you're here for me."
            hin "M-more help...?"
            scene v21_hinatahate_handylookupthinking_b1 with dissolve: 
                yalign 0.0
            hint "I knew he'd get the wrong idea, he's getting way too comfortable asking for help..."
            hint "I don't want him to think this is normal, I can't keep doing this!"
            hint "What have I gotten myself into..."
            scene v21_hinatahate_handylookupthinking_b with dissolve:
                yalign 0.0
            hin "[bo_name] just remember, this is for emergencies ONLY!"
            hin "You can't rely on me to help like this all the time, o-okay? \nIt's just not r-right!"
            bo "Right... Yeah, I get it..."
            bot "Craving you is always an emergency for me [hin_rel]! I'm already addicted to your touch!"
            hin "*Sigh*... Let's just both do our best to get through this, alright?"
            scene black with dissolve
            hint "Why do I feel like whenever I talk it goes in one ear and out the other with him..."
            scene hina leavebobedroom with dissolve
            hin "I left a towel for you. Please clean after yourself and drop it in the laundry basket, okay?"
            bo "Okay... Thanks for everything, [hin_rel]!"
            scene black with fade
            $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            "You get yourself cleaned up and get dressed, while [hin_name] takes the laundry away."
            bot "I'd love to turn this into a morning ritual!"
            bot "I'm obsessed with the thought of [hin_rel] pleasuring me like this regularly..."
            bot "I hope it happens again soon... I can't wait!"
            $ renpy.end_replay()
            jump wakeupend

        # Blocked options in love path
        "{color=[hatredcolor]}???{/color}" if hatredlevel2_handjobcounter >=1: 
            call randomCheck(False,f"{{color={hatredcolor}}}Hatred {{/color}}check{{color=#FF0000}} failed{{/color}}") from _call_randomCheck_23
            "This option is blocked for the love path!"
            jump hatredlevel2_handjob_chosenlove_repeatablemenu

        "{color=[hatredcolor]}???{/color}" if hatredlevel2_handjobcounter >=2:
            call randomCheck(False,f"{{color={hatredcolor}}}Hatred {{/color}}check{{color=#FF0000}} failed{{/color}}") from _call_randomCheck_24
            "This option is blocked for the love path!"
            jump hatredlevel2_handjob_chosenlove_repeatablemenu

        "{color=[obediencecolor]}Make her get on the bed with you{/color}" if hatredlevel2_handjobcounter >=3:
            call checkObedience(0, "hatredlevel2_handjob_chosenlove_repeatablemenu", "Hinata", 2) from _call_checkObedience_62 
            bot "Today let's try a different approach..."
            bot "I'm really craving that body of yours [hin_rel], I want to hold you so badly!"
            if hatredlevel2_handjobcounter ==3:
                bot "I respect your personal space, but I really want to jump in bed with you and cuddle up!"
                bot "I just gotta find a way to get you to agree to it..."
            else:
                bot "I'll just get her to do it again like last time, she seems to be getting a bit more receptive to my requests!"
                jump v21_onbed_repeatable_jump_chosenlove
            bo "This feels really good [hin_rel], you always take such good care of me!"
            bo "But I never ask you how you feel about it, do you even like doing this for me?"
            hin "H-huh? W-well, it's not like I enjoy this exactly [bo_name]..."
            scene v21_hinatahate_handy2b at custom_vpunch_repeat(2) with dissolve:
                yalign 0.3
            hint "W-where is this coming from now? Why would he ask that...?"
            hint "W-where is this coming from now? Why would he ask that...?"
            hint "It's true that I'm not comfortable at all with the current situation, but I should reassure him that I'm here for him no matter what!"
            hin "I do want to h-help you, I just don't know how to feel about all this sometimes..."
            hin "You're my [hin_rel_to_bo] and I care about you, but this is so inappropriate and strange to me..."
            scene v21_hinatahate_handy2b at custom_vpunch_repeat(2) with dissolve:
                yalign 0.3
            hin "I know this is just the curse putting us in these tough unorthodox spots, but it's still quite improper!"
            hin "I'm responsible for you though, and your well-being is one of my top priorities!"
            call changeLove("Hinata",1, "v021_hin_onbedtogetherlove", 1, statlevel=2) from _call_changeLove_64
            hin "If anything, I find you to be so sweet and charming, and I want you to know that I love you so much!"
            bo "O-oh... Thanks [hin_rel]... You always know how to put a smile on my face!"
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
            label v21_onbed_repeatable_jump_chosenlove:
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
            bot "This must be what it feels like to be in heaven..."
            bot "[hin_rel] is my guardian angel, taking such good care of me!"
            bot "Having those lovely breasts on my face is enough to put me in a trance, they're even softer than these fluffy pillows!"
            bot "And the aroma off her smooth glistening skin is overwhelming me, making me yearn for her even more!"
            bot "All while you touch me and provide me with the pleasure I crave..."
            bot "I could just lie here forever!"
            scene v21_hinatahate_onbed2 with dissolve: 
                yalign 0.2 
            hin "H-how is this [bo_name]? Is it helping you at all?"
            if hatredlevel2_handjobcounter < 4:
                $ hatredlevel2_handjobcounter = 4
            bo "Y-yeah, it feels amazing having you close..."

            menu hatredlevel2_handjob_onbed_chosenlove_repeatablemenu:
                "{color=[lovecolor]}She looks perfect from this angle!{/color}":
                    scene v21_hinatahate_onbed4 with dissolve:
                        yalign 1.0
                    show v21_hinatahate_onbed4:
                        easein 5 subpixel True yalign 0.35    
                    bot "Wow, just look at her!" with vpunch
                    bot "The way the light captures her face from this angle is just perfect!"
                    bot "I can see every little detail of her beautiful features, and her hair falling around the side of her face is just mesmerizing!"
                    bot "Those breasts of hers look so soft and inviting, I could just reach out and grasp them right now!"
                    bot "That little sweater working overtime to contain them..."
                    bot "Hugging her curves so perfectly, and highlighting every little bump and contour of her body!"
                    bot "I could just stare at her forever..."
                    label v21_onbed_repeatable_jump2_chosenlove:
                    hin "E-everything okay [bo_name]? You spaced out a bit, you're not feeling faint or anything, are you?"
                    hin "I-is it your condition making you uncomfortable? We'll get the pressure out, don't worry!"
                    bo "Y-yeah... I-I'm trying to [hin_rel], don't stop now!"
                    scene v21_hinatahate_onbed2 at custom_vpunch_repeat(2) with dissolve: 
                        yalign 0.2 
                    hint "The curse has made all his old childhood nightmares resurface, the poor thing..."
                    hint "And to think I had been letting him deal with it on his own!"
                    hint "I had no idea it was this bad, I should be a lot more attentive to his needs!"
                    show screen parallax1280 ("v21_hinatahate_onbed4_anim", transformeffect=custom_vpunch_repeat(timer=1.1)) with dissolve
                    $ renpy.sound.play("/audio/soun_fx/handjob3.opus", channel="sfx2", loop=True, relative_volume = 0.5)
                    call showscrollingimage from _call_showscrollingimage_293
                    bot "Oh shit, she's speeding up and really getting into it now!"
                    bot "That's it [hin_rel], seal this magical moment of us together on the bed with my hot cum..."
                    bot "Keep helping me release all this cum I've built up just for you!"
                    bo "Ahh... Yes... Just like that..."
                    hint "My poor little boy... H-how did we even end up in this situation?!"
                    hint "I need to stay strong for both of our sakes, no matter what the world throws at us!"
                    hin "I-it's alright sweetie, you're safe now..."
                    hin "We j-just need to get it all o-out!"
                    bo "Y-yeah... I'm getting c-close..."
                    hint "Oh gosh, is he reaching his limits already? I need to be careful to not release it everywhere."
                    if toji_pay300 == True or toji_defeated == True or v21_hatredhandjob_cumonface == True:
                        hint "I don't want it all over me and my face like that other time!"
                    scene v21_hinatahate_onbed4:
                        yalign 0.35    
                    call hidescrollingimage("Click twice to cum!") from _call_hidescrollingimage_237
                    bo "O-oh fuck! You're the best [hin_rel] ev-..."
                    bo "-... AAAAH!" with vpunch 
                    $ renpy.sound.play("/audio/soun_fx/cum4.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                    scene v21_hinatahate_onbed4cum with flash:
                        yalign 0.35
                    bo "*Moans loudly* A-aaahh!!" with vpunch
                    call decreaselust (50) from _call_decreaselust_144
                    scene black with fade
                    hin"[bo_name_stutter]! W-what has gotten into you!?"
                    show v21_hinatahate_onbedcuddle1_nonevil with dissolve:
                        yalign 1.0
                    show v21_hinatahate_onbedcuddle1_nonevil:
                        easein 5 subpixel True yalign 0.2
                    hin"You can't j-just spill it everywhere!"
                    bo"I just had to feel your embrace, [hin_rel]! I was scared, I'm sorry..."
                    call changeObedience("Hinata", 1, "v21_hinata_handjob_onbedgrope1love", 1,2) from _call_changeObedience_178
                    hint"D-darn it! This has gone way too far, but I can't turn on him now. Not when he needs me the most..."
                    hin"... *Sigh*"
                    hin"You soiled my clothes, and your bedsheets, you d-dummy!"
                    scene black with dissolve
                    "[hin_name] pulls you closer into a tight embrace, trying to provide you with some extra comfort."
                    show screen parallax1280("v21_hinatahate_onbedcuddle2_evil",1,0.0) with dissolve
                    call showscrollingimage from _call_showscrollingimage_294
                    hin "There, there... Come here..."
                    hin "Everything is going to be okay now that I'm here for you!"
                    bot "Look at her, still trying to comfort me even after I came all over her clothes!"
                    bot "She's so caring and compassionate, on top of being so naturally beautiful!"
                    bot "What would I do without her?!"
                    hin "How are you feeling? Has all the pain and fear subsided for now?"
                    bo "Y-yeah it's all better now... All thanks to you [hin_rel]!"
                    call changeLove("Hinata",1,"v021_hin_bedtogetherlove",1, statlevel = 2) from _call_changeLove_65 
                    hin "You're a handful sometimes, but you're still my sweet [hin_rel_to_bo], I'm glad to have you around!"
                    bo "I'll let you know if I need more help, it makes me feel so much safer knowing that you're here for me."
                    hin "M-more help? *sigh*"
                    hin "J-just try not to bottle it all up inside and suffer on your own, okay?"
                    hint "I keep telling myself that it'll be the last time, but somehow I always end up here again..."
                    hint "We're getting closer in ways I never thought possible, hopefully we're not crossing any lines here..."
                    scene black with dissolve
                    call hidescrollingimage("Click twice to let her go.") from _call_hidescrollingimage_238
                    hin "O-okay well! You seem back to your old self again, so I'm going to go get started on everything that needs to be done."
                    hin "As much as I'd love to stay here and comfort you all morning..."
                    scene hina leavebobedroom with dissolve
                    hin "...I still have chores to do!"
                    hin "I left a towel for you. Please clean up after yourself and drop it in the laundry basket, okay?"
                    bo "Okay... Thanks for everything, [hin_rel]!"
                    scene black with fade
                    $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    "You get yourself cleaned and get dressed, while [hin_name] takes the laundry away."
                    bot "She's so perfect! Spending time with her like this is amazing!"
                    if quest_hin.check("hin2L_2", "in progress"):
                        $ notification("Quest updated")
                        $ quest_hin.check("hin2L_2", "completed")
                        $ quest_hin.check("4_hin2L", "completed")                        
                        $ quest_hin.check("5_hin2L", "in progress")
                    bot "I can't wait to do more with her in the future..."
                    $ renpy.end_replay()
                    jump wakeupend

                "{color=[impulsecolor]}Grasp her breasts!{/color}" if hatredlevel2_handjobcounter >=3:
                    scene v21_hinatahate_onbed4 with dissolve:
                        yalign 1.0
                    show v21_hinatahate_onbed4:
                        easein 5 subpixel True yalign 0.3  
                    bot "I know I really shouldn't be doing this but..."  
                    bot "I'm tired of always having to control myself!" with vpunch
                    bot "Fuck boundaries, I'm not holding back..."
                    show v21_hinatahate_onbed4:
                        yalign 0.3    
                    show v21_hinatahate_onbed4:
                        subpixel True xpos -200 ypos -0.25 zoom 1.3 
                    with Dissolve(1)
                    bot "I mean, just look at them! How could I ever resist?"
                    bot "They're practically begging for attention!"
                    scene v21_hinatahate_onbed4 with dissolve:
                        yalign 0.3    
                    bot "[hin_rel]'s definitely not going to like it, but I can't help myself!"
                    bot "Nobody is perfect, maybe if I'm lucky she wont even notice it..."
                    scene v21_hinatahate_onbedgrope1_2 with dissolve:
                        yalign 0.5
                    $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                    hin "...[bo_name_stutter]?!" with vpunch
                    hin "W-what do you think you are doing exactly?!"
                    bot "Well shit... So much for not noticing..."
                    bot "They do feel so magnificently soft though! Even with my gentle touch I can feel their warmth surround my fingers..."
                    bot "Ah I'm sure it's fine, let me just focus on enjoying myself here!"
                    $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                    hin "Y-you can't just t-touch me like that, stop it!" with vpunch
                    menu:
                        hin "Y-you can't just t-touch me like that, stop it!"
                        "{color=[impulsecolor]}Squeeze!{/color}":
                            pass
                    bot "Sorry [hin_rel], but this is so much fun..."
                    scene v21_hinatahate_onbedgrope1_2_angry_anim with dissolve:
                        yalign 0.5
                    $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                    hin "Hello?! Are you even listening to me?!"
                    call changeRespect("Hinata", -2) from _call_changeRespect_271
                    hin "...[bo_name_stutter]?!" with vpunch
                    hint "What in the world is he doing?! He's not even responding to me!"
                    hint "Since when does he think I'm okay with him groping me like this?!"
                    hin "[bo_name], can you hear me?!"
                    scene v21_hinatahate_onbedgrope1_2_openeyes with dissolve:
                        yalign 0.5
                    bo "Huh? Oh, sorry [hin_rel] I was just... a bit distracted!"
                    hint "This must be the curse making him act upon his urges..."
                    hin "I know you're not in control of your actions right now, but there are still lines you shouldn't cross!"
                    hin "And this is definitely one of them!" with vpunch
                    bo "Y-yeah you're right [hin_rel], I'm sorry..."
                    hint "He's been craving physical contact with me more and more, his body finds comfort in me now..."
                    hint "I-I don't know what to do though... I can't just let him go wild and do whatever he wants!"
                    hin "*Ahem*... [bo_name], your hands are still on me!" with vpunch
                    bo "O-oh, s-sorry! *nervous chuckle*"
                    bot "Fun's over I guess..."
                    scene v21_hinatahate_onbed4 with dissolve:
                        yalign 1.0
                    show v21_hinatahate_onbed4:
                        easein 5 subpixel True yalign 0.3    
                    hin "I promised to be here for you and help out, but I need you to put in some effort too okay?"
                    hin "Let's not make this harder than it has to be..."
                    bot "She's right, I need to be more careful with my actions and not let the curse take control of me like that!"
                    bot "It's hurting the people I care about, and I would never want to hurt [hin_rel]!"
                    call changeHatred(1) from _call_changeHatred_221
                    bot "Why is it so hard to resist these urges though?!"
                    bot "I should be grateful for everything she does for me, not take advantage of her kindness and affection!"
                    bot "If I keep this up, I might really lose her... Or worse, lose MYSELF to this damn curse!"
                    $ renpy.end_replay()
                    jump v21_onbed_repeatable_jump2_chosenlove

        

label v21_handjob_lovecheckfailjump:
    hint "No, this is wrong!" with vpunch
    hint "I can't allow this to happen, why am I even entertaining this idea?!"
    hint "Emotional support is one thing, but b-beyond that is where I draw the line!"
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    "[hin_name] suddenly bolts upright and quickly gathers up the laundry she was collecting."
    hin "I'm s-sorry [bo_name], I should probably go..."
    bot "Huh? She's suddenly leaving just like that...?"
    scene hina leavebobedroom with dissolve
    hin "I have a lot of chores to get through today, so I'll give you some privacy to deal with your c-condition."
    bo "B-but [hin_rel]... Wait!"
    hin "I-I'll see you later, okay? I just need some time to think about everything..."
    $ renpy.sound.play("/audio/soun_fx/footsteps.opus", channel="sfx1", loop=False, relative_volume = 0.9)
    scene black with fade
    bot "Damn, that was not the outcome I was hoping for!" with vpunch
    bot "I guess I pushed her for more too soon..."
    bot "I should try again when she's more comfortable around me."
    bot "For now though, I'll just let her think it over..."
    $ hatredlevel2_handjobcounter = 1
    $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    "You pull yourself out of bed and put on some clothes, ready to officially start the day."
    bot "Let's see what else I can get up to today, maybe I can find something to take my mind off of this..."
    $ renpy.end_replay()
    jump wakeupend



############## Wakeup random handjob #################

# Implied pre-requisites through progression:  Obedience level 2

label v21_hinatawakeup_handjob:

    $ initialize_replay_defaults()

    call randomCheck(True, f"Something is happening to {{color=#FF3333}}{store.bo_name}{{/color}} while he is asleep!") from _call_randomCheck_25
    bot"ZzZz..."
    show eyeclosed
    show hinaq1bg behind eyeclosed:
        blur 6
    show shina concerned behind eyeclosed with dissolve:
        xpos 360 blur 6
    show bobedx 4:
        matrixtransform ScaleMatrix(1.0, 0.6, 1.0)*OffsetMatrix(1.0, 238.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)
        alpha 1
    show fullblack
    show eyehalfopen
    hide fullblack with dissolve
    hide eyeclosed with dissolve
    bot "Wait, wha-...?"
    pause 0.2
    show eyeclosed with dissolve
    bot "[hin_rel]...?"
    show eyefullopen
    hide eyeclosed with dissolve
    pause .2
    
    hide eyehalfopen with dissolve
    bot "Why is she staring at me like that?"
    bot "Something feels... odd."

    menu:
        "{color=[lovecolor]}Wait and see what she does next...{/color}":
            bot "This seems too real to be a dream..."
            bot "What's going on here?"

        "I'm just imagining things, I won't worry about it and just go back to sleep!":
            show eyehalfopen with dissolve
            bot "I'm probably still dreaming, why else would she randomly be standing there..."
            show eyeclosed with Dissolve(1)
            bot "It's too early to care about this right now anyway."
            scene black with dissolve
            bot "My eyes feel so heavy, maybe five more minut-... ZzZzz..."
            "You drift off back to sleep, and some time passes by..."
            "..."
            $ renpy.end_replay()
            jump wakeupquest
    label v21_hin_hj_potential_replay_jump_replace:
    hin "This... thing inside you. It's tearing you apart, eating you alive..."
    hin "And yet all I've done is stand by, watching you suffer. \nWhat kind of [hin_rel_mother] does that..."
    hin "Even as you sleep, I can see the discomfort it creates!"
    show shina serious with dissolve
    show shina at smallshake
    hin "I need to be more proactive and fight this head on!"
    hin "I can't just wait for my assistance to be requested, I need to deal with it before it reaches that point!"
    show shina shy with dissolve
    hin "I can only imagine what you're going through [bo_name]..."
    hin "Let me take care of you!"
    bot "Okay, this is getting weird, what is she mumbling to herself about...?"
    show eyehalfopen with dissolve
    bot "Must be another one of my vivid dreams, but that doesn't mean I can't enjoy it!"
    bot "Unless...?"
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 0.7)
    hin"My sweet, brave boy..."
    scene v20hin_handy 0_1_briefs with dissolve:
        yalign 1.0
    show v20hin_handy 0_1_briefs:
        easein 3 yalign 0.2
    hin"You're a brave warrior fighting for us..."
    hin "Pushing through that cursed pain while it shatters you and distorts your reality."
    hin"I should have never let it get this bad. S-stupid me! Argh!" with vpunch
    hin "I can't change the past, but the present is still in my hands!"
    show v20hin_handy 0_1_briefs:
        easein 4 subpixel True xpos -270 zoom 1.4
    call checkLust(50) from _call_checkLust_24
    hin"..."
    hin"Look at what this damn infliction has done to you..."
    hin "How it twists you into something... feral."
    hin "Offering nothing but pain and chaos to you and everyone around you."
    hin "I can't let you become that monster again. Not if I have any say in it!"
    hin"So if this is what it takes..."
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 0.7)
    "She tugs your pants down, her hands shaking..."
    hin"...then so be it, I have to be vigilant even while you sleep!" with vpunch
    bot"Woah, okay I felt that! This can't be a dream!"
    call showscrollingimage from _call_showscrollingimage_295
    show screen parallax1280("v20hin_handy 1_1_asleep",1,1.0,True) with dissolve
    bot "It is definitely r-real!"
    bot "She's grabbed onto my morning wood!"
    bot "Is she thinking of... t-that!?" with vpunch
    menu:
        "{color=[lovecolor]}Wake up!{/color}":
            bot "I can't miss this moment!"
            hide screen parallax1280
            show screen parallax1280("v20hin_handy 1_1_wakingup",1,0.0) with dissolve
            bo "[hin_rel_stutter]...?" 
            hide screen parallax1280
            show screen parallax1280("v20hin_handy 1_1_wakingup2",1,0.0) with dissolve
            bo "...Is everything alright?"
            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            show screen parallax1280("blackscreen",1,0.0)
            hin "*Gasp*!" with vpunch
            hin "[bo_name], y-you're awake!"
            "[hin_name] quickly retracted her hands and pulled away from you in shame..."
            call hidescrollingimage("Click twice to sit up...") from _call_hidescrollingimage_239
            "[hin_name] takes a seat next to you on the bed as you sit up straight, visibly embarrassed but still adamant on clearing up the air..."
            scene v21_hinatahate_hand grab_c_3 with dissolve: 
                yalign 1.0
            show v21_hinatahate_hand grab_c_3:
                easein 5 subpixel True yalign 0.45
            hin "I-I'm sorry, I didn't mean to disturb you!"
            bo "It's okay, you're not disturbing me!"
            bo "Is something w-wrong? Why am I naked? Was it... m-my thing acting up again?"
            show v21_hinatahate_hand grab_c with dissolve
            hin "O-oh, uhm... I was just c-checking up on you!"
            hin "You looked like you were having a r-rough time..."
            hin "So I thought I would take some initiative and ensure you were... n-normal!"
            show v21_hinatahate_hand grab_c_2 with dissolve
            bot "[hin_rel], I didn't know you had it in you!"
            bot "You can 'check up' on me any day of the week, you won't see me complaining!"
            bo "Th-that is considerate of you, thanks for looking out for me..."
            show v21_hinatahate_hand grab_c_3 with dissolve
            bo "I actually was having a really hard time sleeping, I get plagued by these weird dreams sometimes..."
            bo "It even makes me feel all weird down there, often waking up in p-pain!"
            bo "It seems you could tell us much, I've been trying to just deal with it on my own, but... you know how it is."
            show v21_hinatahate_hand grab_c with dissolve
            hin "Of course I can tell! You're my [hin_rel_to_bo], It's easy to tell when something's bothering you..."
            hin "Since you're a-awake though, I'm probably not needed here anymore..."
            hin "I'll let you t-take care of b-business, you seem like you need some privacy right now."
            bo "W-wait, no!" with vpunch
            show v21_hinatahate_hand grab_c_2 with dissolve
            bo "Maybe you could... help me again? You know, like last time?"
            hint "Y-you weren't supposed to wake up, you dummy! I can't just do that now..."
            hin "I just... don't feel comfortable with that idea right now. You know we can't be doing that..."
            hin"I am sorry, I should probably leave."
            bo "N-no, please stay! Can you at least... stay for a bit?"
            show v21_hinatahate_hand grab_c_3 with dissolve
            bo "I just really don't want to be alone right now..."
            show v21_hinatahate_hand grab_c with dissolve
            hin "I know it's not easy, [bo_name]..."
            hin "It's not easy for me either, you know..."
            hint "He seems so vulnerable and fragile right now..."
            hint "It breaks my heart to see him so troubled, can I really just... walk away?"
            hin "I-I suppose I can stay a little longer, but..."
            hin "I can't do that for you... o-okay? You are going to have to take care of it yourself."
            bot"No fun! But maybe..."
            bo"I know, I know. M-maybe we could cuddle for a bit, like the good old times... I am sure I'd feel better then!"
            scene black with fade
            hin "You should cover yourself up! Maybe then we could have a talk?"
            bo "S-sure, I can do that..."
            $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx3", loop=False, relative_volume = 0.7)
            show screen parallax1280("v21_hinatahate_lovehandjobend0",1,0)  with fade
            call showscrollingimage from _call_showscrollingimage_296
            hin "Hey uhm, I'm sorry I started you earlier today..."
            hin "I hope you can at least feel better now, even if it's for a little bit..."
            menu:
                hin "I hope you can at least feel better now, even if it's for a little bit..."
                "Dry hump her":
                    pass
                "Hug her tight":
                    bo "I-It's okay [hin_rel], I know you were just trying to... help!"
                    $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                    hide screen parallax1280
                    show screen parallax1280("v21_hinatahate_lovehandjobend1_1",1,0) 
                    with fade
                    bo "Besides, I'm always happy to see you in the mornings!" with vpunch
                    $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                    hin"...O-oh!" with vpunch
                    "You shift your posture in a more intimate manner, curling gently around her with your arms resting softly around her waistline..."
                    # hide screen parallax1280
                    # show screen parallax1280("v21_hinatahate_lovehandjobend2",1,0)
                    # with fade
                    bo"You might not know it, but simply the sight of you makes things easier for me..."
                    with vpunch
                    call increaselust(10) from _call_increaselust_288
                    hint"His t-thing...I can feel it poking m-my behind!"
                    hin"Hush now and rest..."
                    show screen parallax1280("v21_hinatahate_lovehandjobend1_2",1,0) with dissolve
                    hint"But I can't make a big deal out of that. Not now... not when I know how it affects him, how hard it is for him."
                    bo"..."
                    hin"There, there..."
                    call changeLove("Hinata",1) from _call_changeLove_66
                    show screen parallax1280("blackscreen",1,0) with dissolve
                    hin"Everything will be alright..."
                    "Time breezed by while you embraced her soft caress..."
                    show screen parallax1280("v21_hinatahate_lovehandjobend2",1,0) with dissolve
                    hin"...[bo_name_stutter]?"
                    hint"His nightmares must have been keeping him awake during the night! No wonder he fell asleep so easily..."
                    scene black 
                    call hidescrollingimage("Click twice to drift off to sleep.") from _call_hidescrollingimage_240
                    hin"I better leave you to it then..."
                    bo "ZzZz..."
                    hint "Sleep well, my dear [hin_rel_to_bo]."
                    "Some time passes..."
                    $ renpy.end_replay()
                    jump wakeupend

           
            hide screen parallax1280
            show screen parallax1280("v21_hinatahate_lovehandjobend1",1,0) 
            with fade
            call increaselust(10) from _call_increaselust_289
            bo"Everything feels better when you are around, [hin_rel]!" with vpunch
            hint"H-his thing! It's... rubbing against my thigh!"
            bo "Thanks for always being there for me!"
            hin"Uhm... are you still... in pain?"
            bo"A little bit, but..."
            $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
            show screen parallax1280("v21_hinatahate_lovehandjobend1",1,0,transformeffect=custom_ypunch_repeat(timer=1.5)) 
            bo"Cuddling with you... it takes my mind off the pain." with vpunch
            hin"I... s-see..."
            $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
            bo "I wouldn't be able to do this without you! Th-thank you, [hin_rel]!"
            hin "You don't have to thank me [bo_name], it's my duty as your [hin_rel_mother] after all..."
            hin "You should try and get some rest now... okay?"
            show screen parallax1280("blackscreen",1,0) with dissolve
            "[hin_name] slid to her side, looking to get off the bed, but..."
            show screen parallax1280("v21_hinatahate_lovehandjobend1_1",1,0,transformeffect=custom_ypunch_repeat(timer=1.5)) with dissolve
            $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
            bo"Stay for a little while longer, please...?"
            hin"Uhm..."
            hint"Is he... rubbing himself on me?"
            hin "Just a little longer then. Only until you fall back asleep, okay?"
            bo "S-sure [hin_rel], that would be nice..."
            hint"I can't scold him, not right now..."
            call increaselust(10) from _call_increaselust_290
            $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
            bo "I am still feeling a bit... tired." with vpunch
            bo"All these nightmares, the pain... I struggle to get much sleep at nights."
            hin "No wonder... Try to rest now, w-will you?"
            show screen parallax1280("v21_hinatahate_lovehandjobend2",1,0,transformeffect=custom_ypunch_repeat(timer=1.5)) with dissolve
            $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
            bo "Mhmm... I will... I love you [hin_rel]!"
            hin "I love you too [hin_rel_to_bo]..."
            bot"Your body's warmth... your smell..."
            bot"It's just... too much [hin_rel]!" with flash
            show screen parallax1280("v21_hinatahate_lovehandjobend3",1,0) with dissolve
            $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx3", loop=False, relative_volume = 0.6)
            with flash
            call decreaselust(100) from _call_decreaselust_145
            hin "*Sigh*..."
            bo"*Heavy breathing*..."
            show screen parallax1280("v21_hinatahate_lovehandjobend3_1",1,0) with dissolve
            hint "This curse is relentless, but I won't give it the satisfaction of breaking us..."
            call changeLove("Hinata",1,"v021_hin_wakeuprandomhandjobend",1, statlevel=2) from _call_changeLove_67
            hint "We'll find a way to overcome it, I know we will!" with vpunch
            hint "I won't let it destroy us, no matter what."
            bo "ZzZz..."
            scene black 
            call hidescrollingimage("Click twice to drift off to sleep.") from _call_hidescrollingimage_241
            hin "Sleep well, [bo_name]..."
            if hatredlevel2_handjobcounter ==4:
                $ hatredlevel2_handjobcounter +=1
            "Some time passes..."
            $ renpy.end_replay()
            jump wakeupend

        "{color=[lovecolor]}Pretend to be asleep!{/color}":
            bot "Hmm, waking up now might startle her!"
            bot "I'll just pretend to be asleep and let it happen..."
            hin"*Gulp*..."
            hin"I'll never get used to this, having my own [hin_rel_to_bo]'s p-penis like this, pulsing in my palm..."
            hin"It feels wrong in so many ways! Yet I know for a fact..."
            hin"This is how his curse affects him, and this is how I can s-stop it!"
            hide screen parallax1280
            show screen parallax1280("v20hin_handy 1_1_asleep",1,0.0)
            with dissolve
            hin"Even while sleeping it doesn't release its hold on him."
            hin"How he manages to persevere without a moment of rest is beyond my understanding..."
            hin"[bo_name_stutter]... I won't let this pain consume you, I promise!"
            hide screen parallax1280
            show screen parallax1280("v20hin_handy 2_1",1,0.5)
            with dissolve
            hin"I'll ensure that your mornings start off right..."
            hide screen parallax1280
            show screen parallax1280("v20hin_handy 2",1,0.5)
            with dissolve
            hin"I'll be the support you need, and ease all your discomfort..."
            hide screen parallax1280
            show screen parallax1280("v20hin_handy 2_1",1,0.5)
            with dissolve
            hin"A little motherly care is all you need!" with vpunch
            hide screen parallax1280
            show screen parallax1280("v20hin_handy 2",1,0.5)
            with dissolve
            hin"I can't turn you away any more. Not after everything you've been through!" with vpunch
            $ renpy.sound.play("/audio/soun_fx/handjob4.opus", channel="sfx3", loop=True, relative_volume = 0.5)
            show screen parallax1280("v020_hina_handjob1",1,0.5,transformeffect=custom_vpunch_repeat(timer=1.3)) with vpunch
            bot "Ahh... This is incredible!"
            bot "She's stroking me so nicely... And all on her own too!"
            bot "You're so amazing [hin_rel], those beautiful hands were made for my hard cock!"
            hin"We'll release all this evil inside of you..."
            hin"May it no longer torment you in this vulnerable..."
            hin"There's no harm in h-helping, it's not like it's something we haven't done before together!"
            hide screen parallax1280
            show screen parallax1280("v020_hina_handjob2",1,0.3, transformeffect=custom_vpunch_repeat(timer=1.1))
            with dissolve
            bo"Ah-ah! *Groans*..." with vpunch
            hin "Shh, shh... It's okay [bo_name]..."
            hin"Looks like you're beginning to wake up..."
            hin"I'll take care of it, I know it's hurting! Hang in there, please..."
            bot "I guess she knows that I'm awake now, but she doesn't seem to be stopping..."
            bot "She's not even skipping a beat, still going at it full force!"
            bo"Heavy breathing*... A-ah.... [hin_rel]!" with flash
            hin"My sweet boy... We a-are almost there, I can tell..."
            hide screen parallax1280
            show screen parallax1280("v20hin_handy 3_2",1,1.0)
            with dissolve
            stop sfx3 fadeout 1
            hin"I'm here for you now..."
            hin "I won't let you suffer alone anymore!"
            scene black
            hide screen parallax1280 with dissolve
            hin"Whenever you're ready, let it all out!"
            hide screen parallax1280
            $ renpy.sound.play("/audio/soun_fx/handjob4.opus", channel="sfx3", loop=True, relative_volume = 0.5)
            show screen parallax1280("v020_hina_handjob4",1,0.7,transformeffect=custom_vpunch_repeat(timer=2)) 
            with dissolve
            hin"Keeping it all contained could be d-dangerous..."
            hin"We're not doing that anymore, you hear!" 
            hin"It's all coming out, right now!" with vpunch
            hide screen parallax1280
            show screen parallax1280("v020_hina_handjob4fast",1,0.7,transformeffect=custom_vpunch_repeat(timer=1)) 
            with dissolve
            $ renpy.sound.play("/audio/soun_fx/handjob5.opus", channel="sfx3", loop=True, relative_volume = 0.5)
            hin"Come on... come on!" with vpunch
            bo "[hin_rel]... I-I can't hold it back much longer!"
            bo "It f-feels really good!"
            hin"All that blood circulating t-there for so long while you slept cannot be healthy..."
            hin"Your body needs to release it to rest!"
            bo "I-It's releasing, I can feel it coming!"
            stop sfx3 fadeout 2
            hide screen parallax1280
            show screen parallax1280("v20hin_handy end",1,0.7) 
            with dissolve
            bo"Ah-h... *moans*" with flash
            hin"Go ahead [bo_name]! It'll be alright... Just let it all out!"
            bo"A-ahh... Fu-u-...!" with vpunch
            $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.4)
            show screen parallax1280("v20hin_handy end1",1,0.5) with longerflash
            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx2", loop=False, relative_volume = 0.7)
            hin"*Gasp*!"
            call decreaselust (50) from _call_decreaselust_146
            scene black 
            call hidescrollingimage from _call_hidescrollingimage_242 
            show v20hin_handy end1_1 with dissolve:
                yalign 1.0
            show v20hin_handy end1_1:
                easein 5 yalign 0.1
            hin"G-good heavens!" with vpunch
            hin"What a mess...!"
            show v20hin_handy end1_2 with dissolve
            bo "S-sorry [hin_rel], I didn't mean to get it all over you like that!"
            hint "W-where does all that come from every time!?"
            hint "Every time I think I've seen it all, he surprises me with even more!"
            call changeObedience("Hinata",1,statlevel=2) from _call_changeObedience_179 
            hint "Somehow it always seems to end up on me too, I guess I should be used to it by now..."
            hin "I-it's okay [bo_name], I know you can't control it!"
            scene black with dissolve
            "[hin_name] quickly wipes herself clean of all your bodily fluids and regains her composure..."
            scene v21_hinatahate_handylookupthinking_b with dissolve:
                yalign 0.0
            show v21_hinatahate_handylookupthinking_b:
                easein 4 yalign 0.3
            bo "It feels so much fucking better now... all thanks to you!"
            hin "N-no need to use foul language! But I'm glad you're feeling better..."
            hin "Is it over now? Has all the discomfort subsided?"
            call changeLove("Hinata",1,"v021_hin_whatineedlove",1,2) from _call_changeLove_68
            bo "Y-yeah it's all better now... All thanks to you [hin_rel]!"
            bo "I don't even feel a thing actually, it's like it never happened!"
            bo "We should do this more often!"
            scene v21_hinatahate_handylookupthinking_b1 with dissolve: 
                yalign 0.0
            hin "W-wait, what?!"
            hin "I-I mean, I don't mind helping you out if absolutely necessary, but let's not get carried away..."
            bo "Right... Yeah, I get it..."
            hin "*Sigh*... Let's just both do our best to get through this, alright?"
            hin "Now... I have other matters of the house that need my attention, I think it's time I get started on them."
            scene black with dissolve
            hint "This is a dangerous path we are treading on, but I can't just leave him to suffer alone!"
            scene hina leavebobedroom with dissolve
            hin "I left a towel for you. Please clean after yourself and drop it in the laundry basket, okay?"
            bo "Okay... Thanks for everything, [hin_rel]!"
            scene black with fade
            $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            "You get yourself cleaned up and get dressed, while [hin_name] takes the laundry away."
            bot "What a rush! I can't believe [hin_rel] just came and jerked me off like that!"
            bot "While I was sleeping too!" with vpunch
            bot "I'm obsessed with the thought of her pleasuring me like this regularly now..."
            $ renpy.end_replay()
            if quest_hin.check("5_hin2L", "in progress"):
                $ notification("Quest updated")
                $ quest_hin.check("5_hin2L", "completed")                        
            bot "I hope it happens again soon... I can't wait!"
            jump wakeupend