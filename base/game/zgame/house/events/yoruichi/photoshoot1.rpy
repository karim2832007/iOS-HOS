label yoru_first_photoshoot:
    $ initialize_replay_defaults()
    default yoru_1st_photoshoot = False
    $ yoru_1st_photoshoot = True
    $ yoruichi_modelling_completed = True
    scene black with dissolve
    scene ramen workend
    show yoru shy3:
        xpos -1000
    show boruto snob:
        xpos -1000
    show boruto:
        easein 1 xalign 0.3
    pause 0.1
    show yoru:
        easein 1.2 xalign -0.1
    bo"Obo, you fat fuck! Show yourself..." with vpunch
    show boss laugh2 at right with dissolve
    obo"I bet this fat man could beat your ass and rail it after, little twerp..."
    show boss at smallshake
    obo"Haa-haa-haa! Careful how you address me kid!"
    show boss angry2 with dissolve
    obo"What's up with you two looking at me like that... What, are you some kind of lovebirds?"
    menu:
        obo"What's up with you two looking at me like that... What, are you some kind of lovebirds?"
        "{color=[dominancecolor]}We fucked once or twice...{/color}":
            show boruto sceeming with dissolve
            show boruto:
                easein 1 xalign 0.22
            bo"We may have..."
            show yorucutout_waist:
                zoom 0.25 xalign 0.5 yalign 1.0
            
            show cutoutborder_white:
                zoom 0.75 xalign 0.5 ypos 0.11
            with dissolve
            bo"Fucked once or twice!" with vpunch
            show boruto sceeming2 with dissolve
            show yoru disgust at smallshake with dissolve
            $ renpy.sound.play("/audio/soun_fx/groperepeat1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            show yoru_gropeass1_anim1 with dissolve:
                zoom 0.25 xalign 0.5 yalign 1.0
            call changeDominance(1) from _call_changeDominance_68
            yo"{size=*0.8}*Whispers* W-what the fuck are you doing, you-!{/size}" with vpunch
            show boss angry3 with dissolve
            "You secretly groped Yoru's ass behind Obo's back..."
            obo"Is that so, Yoru..."
            obo"I always knew you were a whore, but-"
            hide cutoutborder_white
            hide yoru_gropeass1_anim1
            hide yorucutout_waist
            show boruto surprised2
            $ renpy.sound.play("/audio/soun_fx/spank4.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            yo"We have not!" with vpunch
            "She angrily slapped your hand away..."
            show boruto snob with dissolve
            show boss laugh2 with dissolve
            obo"Haa-haa-haa! I knew of course..."
            obo"My wife would never sleep with a twerp like you..."
            bot"We'll see about that you old fuck..."
        "And what if we were, old man?":
            show boruto sceeming with dissolve
            bo"And what if we were, old man..."
            bo"Would you have anything to say about it?"
            show boss angry3 with dissolve
            obo"Hey kid, that's my prized possession standing next to you..."
            obo"Careful what you insinuate... you got it?" with vpunch
            bo"Possession, huh? Is that how you think of her...?"
            show boss:
                easein  0.5 xalign 0.9 zoom 1.05
            obo"Got a problem with that, kid?" with vpunch
            show boss:
                easein  0.5 xalign 0.85 zoom 1.1
            obo"Maybe you wanna take this outside, HUH?" with vpunch
            menu:
                obo"Maybe you wanna take this outside, HUH?"
                "Sure!":
                    bo"Sure-"
                    
                "Uuuh, I was just joking!":
                    show boruto surprised2 with dissolve
            show boss laugh2 with dissolve
            show boss:
                easein 0.7 xalign 0.95 zoom 1.05
            obo"Baa-haa-haa!" with vpunch
            obo"I got you scared shitless with that one, didn't I kid?"
            show boruto snob with dissolve
            bo"Not really..."

        "Nothing like that...":
            bo"Nothing of that sort. You don't have to worry old man..."
            obo"Good..."
    obo"Now which one of you will tell me what's going on between youse..."
    bo"Nothing much... But me and Yoru will be off somewhere after our shift..."
    bo"Will that be a problem, old man?"
    show boss angry3 with dissolve
    obo"Is that right... Yoru?"
    show yoru shy3 with dissolve
    yo"Y-yes... But only for a bit!" with vpunch
    show boss laugh2 with dissolve
    obo"Bwa-haa-haa!" with vpunch
    obo"You don't have to sound so scared, my love. It's not like you are on a leash now, are you?"
    obo"You two can do as you like, so long as Yoru is back by nightfall..."
    obo"You got it, kid?" with vpunch
    bo"Sure thing..."
    show boss angry3 with dissolve
    obo"Now get back to work! Both of you!" with vpunch
    bo"Aye aye..."
    hide boruto with dissolve
    show boss:
        easein 0.3 xalign 0.7
    with vpunch
    "Obo gave Yoru a menacing look before she nervously turned around to join you..."
    show yoru shy with dissolve
    with vpunch
    hide yoru with dissolve
    scene black with dissolve
    "..."
    scene ramenkitchen
    show boruto normal at left
    show yoru obedient at right
    with dissolve
    bo"See? Easy as that..."
    yo"..."
    show yoru lookingbackt at right with dissolve:
        zoom 0.5 ypos 1.05
    yo"Let's get to work... I'll meet with you after our shift ends..."
    hide yoru with dissolve
    scene black with dissolve
    call changeMoney(15) from _call_changeMoney_13
    "You spent some time working the shift..."
    "..."
    scene ramenkitchen
    show boruto normal at left
    show yoru obedient at right
    with dissolve
    bo"Ready to get out of this place for once?"
    show yoru normal with dissolve
    yo"I am not going out there with these greasy rags on me kid..."
    yo"You'll wait for me here..."
    show yoru lookingbackt at right with dissolve:
        zoom 0.5 ypos 1.05
    yo"I'll take a shower and join you shortly..."
    show boruto snob with dissolve
    bo"Yes, Madam..."
    hide yoru with dissolve
    show yoru lookingback with dissolve:
        zoom 1.45 xalign 0.5 yalign 1.0
    show yoru:
        easein 10 yalign 0.1
    bot"I can't believe I managed to convince this hot piece of ass to model for me..."
    bot"To be fair, I sort of coerced her into it, but it's not like she isn't gaining anything out of it..."
    bot"I am still paying her a lot of money, and she gets some time away from Obo to go along with it..."
    show yoru:
        easein 1 yalign 0.85
    bot"Perhaps this will be an opportunity to get 'closer' with her! Hehe..."
    bot"But I should still be careful. Wouldn't want to fuck this opportunity up..."
    hide yoru with dissolve
    show boruto normal with dissolve
    bot"Obo is still an unknown variable in all this. Yoruichi being a Shinigami, even if powerless for the time being, further complicates things..."
    show boruto snob with dissolve
    bot"Argh! Thinking isn't my strong suit! I'll just go with the flow for now and see where that takes me..." with vpunch
    scene black with dissolve
    bot"All that's left is to wait for her..."
    bot"."
    bot".."
    bot"..."
    scene ramenkitchen
    show boruto normal at left
    with dissolve
    bot"I wonder what [him_name] will think of Yoru..."
    show boruto snob with dissolve
    bot"I should probably let Yoru know about our situation in advance..."
    bot"She is supposed to act like my..."
    "As you were finishing your thought, Yoru was making her way down the stairs after finishing her shower..."
    show boruto surprised2 with dissolve
    bot"She is supposed to act like m-my..." with vpunch
    show boruto surprised3 with dissolve
    bot"M-my..." with vpunch
    show 02064 with dissolve:
        zoom 1.1 xalign 0.5 yalign 1.0
    show 02064:
        easein 5 yalign 0.0
    bot"M-my... m-model..." with vpunch
    call increaselust(10) from _call_increaselust_138
    show screen parallax1280("02064",1.1) with dissolve
    call showscrollingimage from _call_showscrollingimage_69
    bot"Ho...ly...FUCK!" with vpunch
    bot"I mean... I've seen parts of her in nude before, but..."
    bot"This is something else!" with vpunch
    bot"I knew she was b-beautiful... and m-muscular, but the way her leotard wraps around her curves is majestic!"
    bot"Looking at how her toned core muscles protrude through the tight material is so fucking sexy..."
    bot"Her nipples, even her cameltoe are almost poking out..."
    bot"Is that what she wears casually...?"
    bot"Or did she dress up just for me! Heh-hehe..." with vpunch
    call hidescrollingimage from _call_hidescrollingimage_70
    scene ramenkitchen
    show boruto surprised2 at left
    show yoruc annoyed:
        xpos 2500
    with dissolve
    show yoruc:
        easein 1 xpos 700
    "With a newfound air of confidence, along with hints of superiority, Yoru turned to address you..."
    yo"You have a weird look on your face, kid..."
    bo"Y-your outfit..."
    show yoruc snob with dissolve
    yo"Ah yes... Another reason why I can't freely roam this world of yours..."
    yo"It would seem that being hated, spat on and hunted for what I am is not enough around your places..."
    yo"The few amongst you that aren't trying to kill me, are staring at me like some sort of depraved beasts..."
    yo"This is just about the only way I can feel some confidence, the only way I can feel like my older self around this depressing world of yours. Even if it's for a fleeting moment..."
    yo"And even so your people want to strip from me, even this simple gesture... For what? because I take pride in wearing my casual combat outfit...?"
    bo"That's... anything but c-casual!"
    menu:
        bo"That's anything but c-casual!"
        "{color=[hatredcolor]}You look like a top-tier whore!{/color}":
            show boruto sceeming2 with dissolve
            call changeHatred(1) from _call_changeHatred_126
            bo"You look like a top-tier whore!" with vpunch
            show boruto sceeming2 with dissolve
            bo"That'll do nicely for our little modelling session..."
            yo"I expected nothing less from you..."
        "You are... beautiful":
            bo"Those kitchen rags hide your true self really well..."
            bo"Yoru, y-you are... beautiful!"
            yo"You are only saying that because of how your kind thinks..."
        
    show yoruc annoyed with dissolve
    yo"Are you humans really that simple? Is everything you see, and everything you think of related to sex?"
    show boruto snob with dissolve
    bo"Unlike you ever-living gods, we humans exist to procreate after all! We'd be extinct otherwise..."
    yo"Hmph! When you live for as many years as we do..." with vpunch
    $ renpy.sound.play("/audio/soun_fx/transform.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    scene black with flash
    yo"Sex means nothing!" with vpunch
    "In an instant, Yoru disappeared into a puff of smoke..."
    $ renpy.sound.play("/audio/soun_fx/meow1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    show yoru cat with dissolve
    "Pussy""Meow!"
    bo"."
    bo".."
    "Pussy""You want this pussy, puny human?"
    bo"...!" with vpunch
    "Pussy""Then come and get it! Meow!" with vpunch
    scene black with vpunch
    bo"Y-yoru!?" with vpunch
    scene ramenkitchen
    show boruto surprised3 at center
    show yoru cat2t behind boruto:
        zoom 0.25 xpos 1196 ypos 554
    with dissolve
    $ renpy.sound.play("/audio/soun_fx/meow2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    show yoru:
        easein 2 xpos -1000
    yo"*Meow!* What's wrong... Can't keep up with me?"
    hide yoru with dissolve
    show yoru cat2t behind boruto:
        zoom 0.25 xpos -1000 ypos 554 xzoom -1
    show yoru:
        easein 1.5 xpos 1300 xzoom -1
    "It would appear Yoruichi had the ability to transform herself into a cat..."
    hide yoru with dissolve
    show yoru cat2t behind boruto:
        zoom 0.25 xpos 1300 ypos 554
    show yoru:
        easein 1.5 xpos -1100
    yo"Can't get the pussy, can you? Scumbag human!"
    "She started sprinting around the kitchen, hurling insults at you in a playful manner..."
    hide yoru with dissolve
    show yoru cat2t behind boruto:
        zoom 0.25 xpos -1000 ypos 554 xzoom -1
    show yoru:
        easein 1.5 xpos 1300 xzoom -1
    bo"What the fuck is going on!"
    bo"I thought you said you lost your p-powers..."
    hide yoru with dissolve
    show yoru cat2t behind boruto:
        zoom 0.25 xpos 1300 ypos 554
    show yoru:
        easein 1.5 xpos -1100
    yo"*Meow!* Maybe I did, maybe I didn't..."
    show yoru:
        easein 2 xpos -1000 xzoom 1
    bot"She r-really is a god..."
    bot"Did I... underestimate her powers?" with vpunch
    scene black with flash
    $ renpy.sound.play("/audio/soun_fx/hiss.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    yo"Meow!" with vpunch
    scene ramenkitchen
    show boruto cat at center
    with dissolve
    "Yoru jumped on your shoulder..."
    yo"*Hiss* In reality, You'll never know..."
    yo"You proved yourself to be... *Meow*, untrustworthy..."
    bo"*Nervous laughter* Heh...hehe! Don't claw my face off, p-please..."
    $ renpy.sound.play("/audio/soun_fx/meow1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    yo"If you play nice... *Meow*"
    yo"Now get a move on!" with vpunch
    show boruto:
        easein 2 xpos -1500
    bo"R-right!" with vpunch
    $ playmusic("/audio/ost/market.opus", 0.6)
    scene black with dissolve
    scene bg ramenshop
    show boruto cat at center
    with dissolve
    bo"It'll be a while until we make it to my place..."
    $ renpy.sound.play("/audio/soun_fx/meow1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    yo"*Meow* I don't mind... It's not often I get to see and breathe the countryside..."
    bo"Heh... Might as well use the opportunity to... c-clear the air between us?"
    bot"Better be careful around her, it would seem there is more to her than I initially thought..."
    yo"*Growls* Hiss... I'd prefer to be left unbothered, but..."
    yo"Talk, if you must..."
    hide boruto with dissolve
    $ renpy.sound.play("/audio/soun_fx/walkingforest.opus", channel="sfx3", loop=False, relative_volume = 0.2)
    scene bg konoha2 with fade
    show boruto cat at center with dissolve
    $ yorucatmenu1 = []
    menu yoru_cattalk_menu:
        set yorucatmenu1
        yo"Talk, if you must..."

        "We are here. Are you going to..." if yoru_cattalk_menu_counter >=3:
            bo"We've  made it to my place..."
            $ renpy.sound.play("/audio/soun_fx/meow2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            yo"*Anxious Meow!* Good! Take me to your p-place, quick!" with vpunch
            bo"H-hold on... about what we discussed... are you planning on staying like that or do I-"
            $ renpy.sound.play("/audio/soun_fx/hiss.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            yo"*H-hiss!!* Of c-course I am staying like this..." with vpunch
            yo"I told you, I am n-not going to be your social butterfly!"
            bo"F-fine, sheesh..."
            show boruto:
                easein 0.3 xalign 0.2
            pause 0.2
            bo"Don't have to sound so-!" with vpunch
            $ renpy.sound.play("/audio/soun_fx/transform.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            scene black with flash
            yo"D...D-damn it!" with vpunch
            "A sudden puff of smoke clouded the area around you..."
            show yoru_failcat1 with dissolve
            show yoru_failcat1:
                easein 5 yalign 0.6
            with vpunch
            "As it cleared, it revealed a tired looking Yoruichi, still maintaining a feline stance on the ground..."
            bot"!" with vpunch
            bot"She must have problems sustaining her feline form for long periods of time, meaning..."
            bot"Hehe... Turns out she might be 'almost' powerless, after all..."
            yo"W-what are you looking at me for! I am just taking a small break..." with vpunch
            bo"You sure? You are looking kind of... exhausted!"
            yo"*Concealed Panting*... Exhausted?"
            yo"N-not... really..."
            show yoru_failcat2_1 with dissolve
            show yoru_failcat2_1:
                easein 5 yalign 0.6
            yo"I was just about to go..."
            $ renpy.sound.play("/audio/soun_fx/transform.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            scene black with flash
            yo"...Back to my f-feline form!" with vpunch
            bot"."
            show yoru_failcat2 with dissolve
            show yoru_failcat2:
                easein 5 yalign 0.6
            bot".."
            bo"...!" with vpunch
            bot"She really is powerless!"
            bo"Something wrong...? Thought you were turning into a cat again..."
            show yoru_failcat2 with dissolve:
                zoom 0.7 xalign 0.5 yalign 0.6
            yo"I..."
            show yoru_failcat3 with dissolve:
                yalign 0.0
            show yoru_failcat3:
                easein 2 yalign 1.0
            yo"I changed my mind! M-maybe I should meet this [him_rel] of yours after all..."
            show screen parallax1280("yoru_failcat3") with dissolve
            call showscrollingimage from _call_showscrollingimage_70
            bo"You changed your mind now... Did you?"
            bot"I don't buy that of course but, it's better if I don't make her feel uncomfortable..."
            bot"...at least not right now!"
            bo"I am glad you did! Although..." with vpunch
            bo"It's probably for the best if you got off the floor. Wouldn't want my family to think you are my pet, would you? You freaky cat lady..."
            hide screen parallax1280
            show screen parallax1280("yoru_failcat3_1",1,0.2)
            with dissolve
            yo"Tsk! You are lucky I..." with vpunch
            yo"N-nevermind..."
            call increaselust(5) from _call_increaselust_139
            bo"Good kitty!" with vpunch
            call hidescrollingimage from _call_hidescrollingimage_71
            scene bg porch
            show boruto snob at left with dissolve
            bo"You ready?"
            "Yoru pats herself clean from the dirt on her knees and gets up..."
            show yoruc snob at right with dissolve
            yo"Let's go inside..."
            hide boruto with dissolve
            hide yoruc with dissolve
            $ renpy.sound.play("/audio/soun_fx/dooropen.opus", channel="sfx3", loop=False, relative_volume = 0.6)
            scene black with dissolve
            bo"I am home..." with vpunch
            $ playmusic("audio/ost/house2.opus",0.6)
            show bg lr_day with dissolve:
                zoom 0.68
            show boruto snob with dissolve:
                xpos 160
            show yoruc annoyed with dissolve:
                xpos -150
            hin"Oh, [bo_name]! Just a second..."
            bo"Just follow my lead, alright?"
            yo"Tsk!" with vpunch
            show shina shy:
                xpos 2000
            show shina:
                easein 1 xpos 800
            hin"Welcome back, How was..."
            show shina surprised with dissolve
            hin"[bo_name_stutter]!?" with vpunch
            hin"You didn't tell me y-you...-"
            show yoruc normal with dissolve
            yo"Apologies for the intrusion, my lady..."
            show shina shy2 with dissolve:
                ypos -30
            hin"No need to apologize at all!" with vpunch
            hin"I was simply not expecting guests today, you'll have to forgive my lack of hospitality!"
            show shina shy with dissolve
            $ renpy.sound.play("/audio/soun_fx/footsteps.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            "Hearing the commotion, [him_name]'s curiosity was piqued. She quickly made her way to the living room..."
            hin"Will you please make the introductions, [bo_name_stutter]?"
            show hima worried2 behind shina:
                xpos 2000 zoom 0.34
            show hima:
                easein 1 xpos 900
            show shina:
                easein 1 xpos 600
            him"[hin_rel]? Is everything...-" with vpunch
            show hima surprised with dissolve:
                xpos 930 zoom 0.34
            him"...A-alright?"
            himt"Who the heck is that!" with vpunch
            hin"You are just in time [him_name]... [bo_name] was about to make the introductions!"
            himt"She is so... pretty! Who is she to [bo_name_stutter] anyway!"
            bo"Yoru, meet my [hin_rel], [hin_name]. Next to her is my [him_rel], [him_name]..."
            show yorucombatcutout_ass with dissolve:
                zoom 0.4 xalign 0.0 yalign 1.0
            bo"[hin_rel], [him_name], this is Yoru. She is my..."
            menu yoruintromenuh1:
                bo"[hin_rel], [him_name], this is Yoru..."
                "{color=[dominancecolor]}She is my model{/color}":
                    call checkDominance(15,"yoruintromenuh1") from _call_checkDominance_15
                    show boruto:
                        easein 0.5 xpos 120
                    hide yorucombatcutout_ass with dissolve
                    show yorucombatcutout_waist1 with dissolve:
                        zoom 0.4 xalign 0.0 yalign 1.0
                    call changeDominance(1) from _call_changeDominance_69
                    bo"She is my model!"
                    bo"We are working on something together..."
                    hide yoru_combatcutout_gropeanim1
                    hide yorucombatcutout_grope1
                    hide yorucombatcutout_waist1
                    hide yorucombatcutout_ass
                    show yoruc annoyed with dissolve
                    yo"Nice to meet you, [hin_name]-san, [him_name]-chan..."
                    show shina surprised with dissolve
                    hin"Explains your good looks Yoru-san! The pleasure is ours..."
                    show hima worried2 with dissolve
                    him"N-nice to meet you too..."
                    call changeObedience("Himawari", 1) from _call_changeObedience_104
                    himt"A r-real model, huh? He really wasn't lying about that..."
                    show shina smiling with dissolve
                    hin"You should have said something earlier [bo_name]! I would have prepared something for you and your friend!"
                    show yoruc at smallshake
                    yo"I appreciate your hospitality, lady [hin_name]. I unfortunately won't be staying for much longer..."
                "{color=[obediencecolor]}A friend who works as a model...{/color}":
                    hide yorucombatcutout_ass
                    bo"She is a good friend of mine who works as a model..."
                    bo"We are working on something together..."
                    show yoruc annoyed with dissolve
                    yo"Nice to meet you, [hin_name]-san, [him_name]-chan..."
                    show shina surprised2 with dissolve
                    hin"T-the pleasure is ours!" with vpunch
                    show hima worried2 with dissolve
                    him"N-nice to meet you too..."
                    call changeObedience("Himawari", 1) from _call_changeObedience_105
                    himt"A r-real model, huh? He really wasn't lying about that..."
                    show shina smiling with dissolve
                    hin"You should have said something earlier [bo_name]! I would have prepared something for you and your friend!"
                    show yoruc at smallshake
                    yo"I appreciate your hospitality, lady [hin_name]. I unfortunately won't be staying for much longer..."
                "{color=[hatredcolor]}My girlfriend!{/color}":
                    show boruto:
                        easein 0.5 xpos 120
                    show yorucombatcutout_waist1 with dissolve:
                        zoom 0.4 xalign 0.0 yalign 1.0
                    bo"She is my..."
                    call changeHatred(1) from _call_changeHatred_127
                    show yorucombatcutout_grope1 with dissolve:
                        zoom 0.4 xalign 0.0 yalign 1.0
                    bo"Girlfriend! Among a few other things... Today she's here to help me with something I am working on!" with vpunch
                    $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                    show yoru_combatcutout_gropeanim1:
                        zoom 0.4 xalign 0.0 yalign 1.0
                    "'Play along...' You quietly whispered in her ear, as you discreetly started lightly groping her ass..."
                    "Your threats were implicit..."
                    "In complete disbelief, both [hin_name] and [him_name] exclaimed..."
                    "Both" "G-girlfriend!?" with vpunch
                    hide yoru_combatcutout_gropeanim1
                    hide yorucombatcutout_grope1
                    hide yorucombatcutout_waist1
                    hide yorucombatcutout_ass
                    show boruto:
                        easein 0.4 xpos 150
                    show yoruc annoyed with dissolve
                    yo"*Tsk!*"
                    "Yoru pushed your hand away and made a quiet sound of disapproval, but ultimately..."
                    yo"Nice to meet you, [hin_name]-san, [him_name]-chan..."
                    show shina surprised2 with dissolve
                    hin"T-the pleasure is ours!" with vpunch
                    show hima worried2 with dissolve
                    him"N-nice to meet you too..."
                    show shina smiling with dissolve
                    hin"You should have said something earlier [bo_name]! I would have prepared something for you and your friend!"
                    show yoruc at smallshake
                    yo"I appreciate your hospitality, lady [hin_name]. I unfortunately won't be staying for much longer..."
                    
                    default yorugroped_intro = False
                    $ yorugroped_intro == True

            label beforemodelrepeat:
            yo"{size=*0.8}*Whispers* Wrap this up kid! I didn't sign up for introductions...{/size}" 
            bo"[hin_rel], [him_name]... Unfortunately introductions have to be cut short for now!"
            show boruto:
                easein 2.5 xpos 2000
            show shina surprised with dissolve
            bo"Yoru has to be somewhere soon and we are in a bit of a hurry!" with vpunch
            show yoruc normal with dissolve
            show yoruc:
                easeout 2.5 xpos 2000
            yo"Please excuse my intrusion!"
            "Both" "Oh..."
            pause 1
            show shina shy at left with dissolve
            show hima:
                easein 1 xalign 0.8
            him"."
            hin".."
            him"..."
            "both""Did you see her!?" with vpunch
            hin"She was..."
            him"...so pretty! Almost otherworldly even..." with vpunch
            hin"Right?" with vpunch
            if yorugroped_intro == True:
                him"How did that idiot even..."
                him"He s-said, Yoru is his... g-girlfriend!?"
                show hima mad with dissolve
                him"H-hoW!? He is stupid, ugly and... and-" with vpunch
            else:
                him"How did that idiot even become friends with someone like her..."
                him"She is so well-spoken, kind, she even works as a model! Meanwhile..."
                show hima mad with dissolve
                him"[bo_name] is just a c-clown!" with vpunch
            show shina smiling with dissolve
            hin"*Giggles* [him_name]... Your [him_rel_to_bo] is actually quite the catch himself you know...."
            hin"He has always been a pretty boy! Strong, caring and thoughtful..."
            show shina shy with dissolve
            hin"He might be having his issues with his recent diagnosis, but I am sure he's doing his best to help himself, and us..."
            hin"Cut him some slack, alright?"
            $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            him"Hmph!" with vpunch
            show hima worried2 with dissolve
            scene black with dissolve
            "[hin_name] and [him_name] spent some time gossiping about your new friend..."
            scene bg bb day
            show boruto snob at left
            show yoruc annoyed at right
            with dissolve
            if yorugroped_intro == True:
                yo"Your girlfriend!? You think you can get handsy with me kid? Don't push your luck..." with vpunch
                bo"Relax, will you? I was just trying to get us through the introductions..."
                yo"Sure you were..."
            else:
                yo"Your [hin_rel] and [him_rel] seemed like nice people..."
                yo"Whatever happened to you, kid..."
                bo"Cold, Yoru... I am helping you after all, aren't I?"
                yo"Sure you are..."
            yo"So... what now?"
            yo"How do you plan on making us any money from your bedroom, kid..."
            bo"You'll find out soon enough..."
            show boruto:
                easein 2 xpos -600
            bo"For starters, why don't you make yourself comfortable at your working environment..."
            scene black with dissolve
            yo"And that is... your bedroom?"
            show bg modelling:
                yalign 1.0
            with dissolve
            show boruto snob at right with dissolve
            show yoruc annoyed at left with dissolve
            bo"Not quite! I've prepared this space specifically for your modelling and my directing aspirations..."
            bo"Spacious, plain, and graced by natural lighting. Here is where I'll build my kingdom, with you in the spotlight!"
            yo"Eh, I'll believe it when I see it..." with vpunch
            yo"What's the mattress on the side for...?"
            bo"Just a prop, for now! Or something to be used to enhance some of our shots..."
            bo"Besides, wouldn't want you to tire yourself out..."
            $ renpy.screenshot("test.png")
            hide boruto with dissolve
            bo"You can take a seat over there until I prepare my equipment..."
            yo"Hmph... Fine..."
            hide yoruc with dissolve
            scene black with dissolve
            "Yoru takes a seat at the mattress while you prepare your equipment..."
            show yorum_intro0 with dissolve:
                yalign 1.0
            show yorum_intro0:
                easein 4 yalign 0.1
            yo"You've given this some thought after all..."
            bo"Wait till you see this..."

            scene bg modelling with dissolve:
                yalign 1.0 blur 5
            show boruto snob at center with dissolve
            bo"I don't know about your place, but here in our world, these little machines are practically small miracles..."
            hide boruto with dissolve
            scene black with dissolve
            show screen camera1280("yorum_intro0") with dissolve
            show screen camera_ui("Yoruichi",False) with dissolve
            # call showscrollingimage
            bo"To be able to capture and freeze any moment in time... It's a power like no other!"
            "Pan the camera to capture Yoru's face or... other features of hers!"
            yo"A c-camera... isn't it?"
            yo"I've only seen one before at Obo's place..."
            yo"But he never really told me what it's all about..."
            bo"Ready... and..."
            show expression FocusEffect("idle1", 180, 350, 100, 0.7) as focus_effect onlayer screens with dissolve
            show screen camera_ui("Yoruichi")
            hide expression FocusEffect as focus_effect onlayer screens
            with dissolve
            $ ui.interact()
            show screen camera_ui("Yoruichi",False) with dissolve
            bo"They are exceptionally rare after all, not to mention expensive..."
            yo"That flash just now... What was it?" with vpunch
            bo"That flash was the beginning of our lucrative relationship..."
            bo"Our very first photo shoot!" with vpunch
            hide screen camera_ui
            hide screen camera1280
            scene black
            with dissolve
            yo"Photo... shoot?"
            bo"Here, Wanna see?"
            show yorum_intro1 with dissolve:
                yalign 1.0
            show screen photo_album with dissolve
            yo"..."
            show yorum_intro1:
                easein 2 yalign 0.0
            bo"That's a picture of you. Forever captured and preserved for everyone to marvel at until the end of time..."
            yo"I-interesting... Although I don't think I understand how any of this w-works..."
            bo"You don't have to! That's why I am here after all!"
            bo"With my knowledge, along with my direction and your beauty, I sense an opportunity like no other..."
            yo"Beauty, huh? What makes you think other people see what you do. Have you forgotten how your kind treats me?"
            yo"I am practically worth less than dirt to them..."
            bo"See, you don't know people like I do Yoru..."
            bo"People fear what they don't understand, and act like they despise what they can't have..."
            bo"Regardless of how they might treat you, I bet you there's no man on earth, maybe woman too, who would look at you and not stare for a second..."
            scene black with dissolve
            "Yoru seemed overwhelmed by your suggestion. She shifted her posture and said..."
            show yorum_intro2 with dissolve:
                yalign 1.0
            show yorum_intro2:
                easein 3 yalign 0.1
            yo"...Because of what I am?"
            bo"Because of how you look!" with vpunch
            bo"Which is exactly why I think your pictures could net us a fortune!"
            show screen parallax1280("yorum_intro2") with dissolve
            call showscrollingimage from _call_showscrollingimage_71
            yo"How can you be so certain of that..."
            bo"Think of it like this... If I am right and people fear you for what you are, but lust over how you look, then..."
            bo"Would a picture of you not be the closest they can get to you without risk? It's the perfect business opportunity!"
            bo"In fact, I am pretty sure that's exactly how Obo makes use of his own gear..."
            bo"He is using you, Yoru! He makes money of your own appearance and leaves nothing for you. You have nothing to show for it..."
            yo"..."
            yo"That... b-bastard!" with vpunch
            call hidescrollingimage from _call_hidescrollingimage_72
            scene black with dissolve
            "Yoru gets up and starts pacing around the room in frustration..."
            show bg modelling:
                yalign 1.0
            show boruto snob at right with dissolve
            show yoruc annoyed at left with dissolve
            with dissolve
            yo"I knew he was using his own stuff for w-work or something. But I never thought one could profit from something like this!" with vpunch
            bo"Right? Its about time you stop relying on him..."
            yo"*Groans* Aaarh! And do what... rely on a kid instead?" with vpunch
            show boruto normal with dissolve
            bo"On yourself, Yoru..."
            show yoruc normal with dissolve
            show boruto snob with dissolve
            bo"And then me! Not just a kid, your director and business partner..."
            show yoruc snob with dissolve
            yo"Hmph! The idea is almost laughable..."
            scene black with dissolve
            $ renpy.sound.play("/audio/soun_fx/heels1.opus", channel="sfx2", loop=False, relative_volume = 0.8)
            "Once again, Yoru started pacing your room..."
            show yoru_modelstart with dissolve:
                zoom 1.65 xalign 1.0 yalign 1.0
            show yoru_modelstart:
                easein 4 yalign 0.1
            "But this time she seemed at ease, lost in her own thoughts..."
            show yoru_modelstart with dissolve:
                zoom 1.65 xalign 0.0 yalign 1.0
            show yoru_modelstart:
                easein 4 yalign 0.1
            yo"Hmm..."
            yo"...Equal partners then?"
            bo"Of course!"
            yo"Then I'll trust you this one time, kid. But if you ever cross me..."
            scene yoru_modelstart with dissolve:
                yalign 1.0
            show yoru_modelstart:
                easein 2 yalign 0.1
            bo"I would never cross a god, Yoru... Even one whose secrets I know! Heh..."
            show screen parallax1280("yoru_modelstart",1,0.2,True) with dissolve
            yo"*Groans*! Just tell me what do I have to do, kid..."
            bo"One more thing before we start..."
            bo"From now on you will address me as Director [bo_name]. I don't wanna hear 'Kid' another time... got it?"
            yo"Your name alone will do..."
            default yoru_picture_counter = 0
            $ yoru_picture_counter +=1
            menu yoru_intromodelmenu:
                yo"What do I do next, [bo_name]..."
                
                "Let's start with a frontal medium shot!":
                    bo"Let's start with something simple to ease you into it..."
                    yo"Sure..."
                    hide screen parallax1280
                    show yoru_frontalstart:
                        yalign 1.0 xalign 0.5
                    with dissolve
                    show yoru_frontalstart:
                        easein 2 yalign 0.0
                    bo"How about a frontal medium shot..."
                    yo"Speak plainly Ki-, [bo_name]..."
                    bo"Caught yourself there, huh? I like that..."
                    bo"A medium shot is a picture that focuses on the subject's waist line and above..."
                    bo"I see... Now what?"
                    menu :
                        yo"..."
                        "Strike a dynamic pose..." if yoru_frontal_dynamic == False:
                            default yoru_frontal_dynamic = False
                            $ yoru_frontal_dynamic = True
                            bo"Now you strike a pose!"
                            bo"Given your current attire, let's compliment your body's features with a dynamic combat pose..."
                            bo"Plenty of movement, muscle flexing, and a daring look... think you can pull that off?"
                            show yoru_frontal_dynamicpose with dissolve:
                                yalign 1.0
                            show yoru_frontal_dynamicpose:
                                easein 2 yalign 0.0
                            yo"Something like..."
                            yo"...This?"
                            show screen camera1280("yoru_frontal_dynamicpose") with dissolve
                            show screen camera_ui("Yoruichi",False) with dissolve
                            bo"You are a natural, Yoru!"
                            bo"Now hold that pose for me, and..."
                            show screen camera_ui("Yoruichi",True) with dissolve
                            $ ui.interact()
                            show screen camera_ui("Yoruichi",False) with dissolve
                            bo"Excellent..."
                            show screen camera1280("yoru_frontalstart") with dissolve
                            yo"That flash... It means you got a picture, right?"
                            bo"Indeed, a great one too!"
                            yo"In that case, I'll allow you a few more flashes."
                            yo"I'll keep following your 'directions', but if you fail to make any money with these first few flashes..."
                            yo"Then this will be our last session together! I am not in the business of wasting my time... You got that?"
                            bo"Making the rules now, are you?"
                            bo"Fine, I'll play along, for now..."
                            bo"But If I only get a few more flashes, then it's time to amp up the heat!" with vpunch
                            bo"Are you ready for the next one?"
                            yo"..."

                        "Strike a confident pose..." if yoru_frontal_confident == False:
                            default yoru_frontal_confident = False
                            $ yoru_frontal_confident = True
                            bo"Now you strike a pose!"
                            bo"Let's have you pose in a confident manner. Flick your hair, and stare straight into the lens with a serious expression..."
                            show yoru_frontal_confidentpose with dissolve:
                                yalign 1.0
                            show yoru_frontal_confidentpose:
                                easein 2 yalign 0.0
                            yo"Something like..."
                            yo"...This?"
                            show screen camera1280("yoru_frontal_confidentpose") with dissolve
                            show screen camera_ui("Yoruichi",False) with dissolve
                            bo"You are a natural, Yoru!"
                            bo"Now hold that pose for me, and..."
                            show screen camera_ui("Yoruichi",True) with dissolve
                            $ ui.interact()
                            show screen camera_ui("Yoruichi",False) with dissolve
                            bo"Excellent..."
                            show screen camera1280("yoru_frontalstart") with dissolve
                            yo"That flash... It means you got a picture, right?"
                            bo"Indeed, a great one too!"
                            yo"In that case, I'll allow you a few more flashes."
                            yo"I'll keep following your 'directions', but if you fail to make any money with these first few flashes..."
                            yo"Then this will be our last session together! I am not in the business of wasting my time... You got that?"
                            bo"Making the rules now, are you?"
                            bo"Fine, I'll play along, for now..."
                            bo"But If I only get a few more flashes, then it's time to amp up the heat!" with vpunch
                            bo"Are you ready for the next one?"
                            yo"..."
                        
                "Let's start with a rear full shot!":
                    bo"Let's start with something simple to ease you into it..."
                    yo"Sure..."
                    bo"How about a rear full shot..."
                    yo"Speak plainly Ki-, [bo_name]..."
                    bo"Caught yourself there, huh? I like that..."
                    bo"A full rear shot is a picture that focuses on the subject's full body... from the rear of course!"
                    hide screen parallax1280
                    show yoru_rearstart:
                        yalign 0.0 xalign 0.5
                    with dissolve
                    show yoru_rearstart:
                        easein 2 yalign 1.0
                    yo"The rear, huh? I see... Now what?"
                    bot"The ass on this woman..."
                    show screen camera1280("yoru_rearstart") with dissolve
                    show screen camera_ui("Yoruichi",False) with dissolve
                    menu:
                        yo"..."
                        "Stay exactly as you are..." if yoru_rear_stay == False:
                            default yoru_rear_stay = False
                            $ yoru_rear_dynamic = True
                            bo"You know what? I think you might have accidentally struck perfection..."
                            yo"I... did?"
                            bo"Stay exactly as you are..."
                            bo"We are going to turn this into a medium shot instead..."
                            bo"And..."
                            show screen camera_ui("Yoruichi",True) with dissolve
                            $ ui.interact()
                            show screen camera_ui("Yoruichi",False) with dissolve
                            bo"I knew you were a natural..."
                            yo"That flash... It means you got a picture, right?"
                            bo"Indeed, a great one too!"
                            yo"In that case, I'll allow you a few more flashes."
                            yo"I'll keep following your 'directions', but if you fail to make any money with these first few flashes..."
                            yo"Then this will be our last session together! I am not in the business of wasting my time... You got that?"
                            bo"Making the rules now, are you?"
                            bo"Fine, I'll play along, for now..."
                            bo"But If I only get a few more flashes, then it's time to amp up the heat!" with vpunch
                            bo"Are you ready for the next one?"
                            yo"..."

                        "Strike a dynamic pose..." if yoru_rear_dynamic == False:
                            default yoru_rear_dynamic = False
                            $ yoru_rear_dynamic = True
                            bo"Now you strike a pose!"
                            bo"Given your current attire, let's compliment your body's features with a dynamic combat pose..."
                            bo"Plenty of movement, muscle flexing, and a daring look... think you can pull that off?"
                            hide screen camera1280
                            hide screen camera_ui
                            with dissolve
                            show yoru_rear_dynamic with dissolve:
                                yalign 1.0
                            show yoru_rear_dynamic:
                                easein 2 yalign 0.0
                            yo"Something like..."
                            yo"...This?"
                            show screen camera1280("yoru_rear_dynamic") with dissolve
                            show screen camera_ui("Yoruichi",False) with dissolve
                            bo"You are a natural, Yoru!"
                            bo"Now hold that pose for me, and..."
                            show screen camera_ui("Yoruichi",True) with dissolve
                            $ ui.interact()
                            show screen camera_ui("Yoruichi",False) with dissolve
                            bo"Excellent..."
                            show screen camera1280("yoru_rearstart") with dissolve
                            yo"That flash... It means you got a picture, right?"
                            bo"Indeed, a great one too!"
                            yo"In that case, I'll allow you a few more flashes."
                            yo"I'll keep following your 'directions', but if you fail to make any money with these first few flashes..."
                            yo"Then this will be our last session together! I am not in the business of wasting my time... You got that?"
                            bo"Making the rules now, are you?"
                            bo"Fine, I'll play along, for now..."
                            bo"But If I only get a few more flashes, then it's time to amp up the heat!" with vpunch
                            bo"Are you ready for the next one?"
                            yo"..."

                        "Strike a confident pose..." if yoru_rear_confident == False:
                            default yoru_rear_confident = False
                            $ yoru_rear_confident = True
                            bo"Now you strike a pose!"
                            bo"Let's have you pose in a confident manner. Imagine this scenario..."
                            bo"Someone's calling out your name and you are looking over your shoulder to check who it is..."
                            bo"Your look pierces through whoever called out with its brimming confidence..."
                            bo"Think you can do that?"
                            hide screen camera1280
                            hide screen camera_ui
                            with dissolve
                            show yoru_rear_casual with dissolve:
                                yalign 1.0
                            show yoru_rear_casual:
                                easein 2 yalign 0.0
                            yo"Something like..."
                            yo"...This?"
                            show screen camera1280("yoru_rear_casual") with dissolve
                            show screen camera_ui("Yoruichi",False) with dissolve
                            bo"You are a natural, Yoru!"
                            bo"Now hold that pose for me, and..."
                            show screen camera_ui("Yoruichi",True) with dissolve
                            $ ui.interact()
                            show screen camera_ui("Yoruichi",False) with dissolve
                            bo"Excellent..."
                            show screen camera1280("yoru_frontalstart") with dissolve
                            yo"That flash... It means you got a picture, right?"
                            bo"Indeed, a great one too!"
                            yo"In that case, I'll allow you a few more flashes."
                            yo"I'll keep following your 'directions', but if you fail to make any money with these first few flashes..."
                            yo"Then this will be our last session together! I am not in the business of wasting my time... You got that?"
                            bo"Making the rules now, are you?"
                            bo"Fine, I'll play along, for now..."
                            bo"But If I only get a few more flashes, then it's time to amp up the heat!" with vpunch
                            bo"Are you ready for the next one?"
                            yo"..."
            jump yoru_repeatmodelling
                



            








        "About your transformation powers...":
            default yoru_cattalk_menu_counter = 0
            $ yoru_cattalk_menu_counter += 1
            bo"So... about your powers, I thought you said you lost your Shinigami powers..."
            $ renpy.sound.play("/audio/soun_fx/hiss.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            yo"I didn't... *Growls* Hiss!" with vpunch
            bot"She is either bluffing, or lying to me..."
            bo"Can you... transform into anything you like? If so, why a cat...?"
            $ renpy.sound.play("/audio/soun_fx/meow1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            yo"I like felines! *Meow*..."
            yo"In truth, it's simply my means of staying under the radar and avoiding confrontation..."
            yo"I've told you how people act towards me before..."
            $ renpy.sound.play("/audio/soun_fx/meow2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            yo"But like this, I can Inconspicuously *Meow* at bumbling idiots like yourself and be left alone..."
            $ renpy.sound.play("/audio/soun_fx/hiss.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            yo"*Growls* Hissss!" with vpunch
            show boruto at smallshake
            bo"Message received..." with vpunch
            hide boruto with dissolve
            $ renpy.sound.play("/audio/soun_fx/walkingforest.opus", channel="sfx3", loop=False, relative_volume = 0.2)
            if yoru_cattalk_menu_counter == 1:
                scene bg konoha1 with fade
            elif yoru_cattalk_menu_counter == 2:
                scene inohouse day with fade
            elif yoru_cattalk_menu_counter == 3:
                scene bg porch with fade
            else:
                scene bg porch with fade
            show boruto cat at center with dissolve
            jump yoru_cattalk_menu


        "Your outfit, it's important to you, isn't it...?":
            $ yoru_cattalk_menu_counter += 1
            bo"Your outfit... You said something about it reminding you of your older self..."
            bo"It's important to you, isn't it?"
            yo"It's just what I wore back when I used to serve as the Captain of a Shinigami squad..."
            yo"That is, until I got exiled... The only thing that remains from that time is this outfit..."
            yo"The material it's made of is infused with my reiatsu. Wearing it gives me the ability  to push my body to it's absolute limits; If and when needed..."
            yo"But nowdays, it simply serves as memorabilia of days old..."
            $ renpy.sound.play("/audio/soun_fx/meow2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            yo"It's... comforting... *Sad Meow :(*"
            bo"R-rei...jutsu?"
            yo"*Sigh* You wouldn't get it..."
            yo"Look kid, point being... I wear it because I am comfortable in it! And yes, it's important to me..."
            yo"In any case, it's just some casual clothing, I don't understand why you humans act the way you do... "
            bo"I think our definition of 'casual' might differ from your kind's..."
            yo"I've come to realize that when I first met with Obo..."
            yo"He immediately prohibited me from wearing my outfit while working at his place. 'For your own safety', he said... But I reckon it was something else..."
            yo"As every customer of his would stare at me with lust in their eyes..."
            yo"The same way you did just moments ago *Meow!*" with vpunch
            bo"I wasn't c-complaining, just curious..."
            $ renpy.sound.play("/audio/soun_fx/hiss.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            yo"Hiss! Not my concern if your kind is comprised of simple-minded, sex-deprived pests. *Meow*!" with vpunch
            $ renpy.sound.play("/audio/soun_fx/meow1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            yo"This is what I am comfortable wearing, so this is what I'll wear! *Angry Meow!*" with vpunch
            bo"G-got it!"
            yo"*Growls* Hiss! Enough about this! Keep walking..." with vpunch
            bo"R-right..."
            hide boruto with dissolve
            $ renpy.sound.play("/audio/soun_fx/walkingforest.opus", channel="sfx3", loop=False, relative_volume = 0.2)
            if yoru_cattalk_menu_counter == 1:
                scene bg konoha1 with fade
            elif yoru_cattalk_menu_counter == 2:
                scene inohouse day with fade
            elif yoru_cattalk_menu_counter == 3:
                scene bg porch with fade
            else:
                scene bg porch with fade
            show boruto cat at center with dissolve
            jump yoru_cattalk_menu
        "(I should mention [him_name]...)":
            $ yoru_cattalk_menu_counter += 1
            bo"Hey uuuh, there's someone I would like for you to meet when we get to my place..."
            yo"Kid... I am not about to turn into a social butterfly for you. I've only agreed to do the photo shoot, nothing less, nothing more..."
            bo"Come on, it's only gotta be a small exchange of words with her! Besides, I am pretty sure you and her would make good friends..."
            $ renpy.sound.play("/audio/soun_fx/meow2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            yo"...H-her? *Curious M-meow*..."
            bo"How did that pique your interest... Are you into girls or something?"
            $ renpy.sound.play("/audio/soun_fx/hiss.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            yo"Shut it, kid... *Hiss*!" with vpunch
            yo"So... Who's this her you are referring to?"
            bo"Her name is [him_name]. She is my [him_rel]..."
            bo"I just need you to exchange pleasantries with her and maybe..."
            bo"Throw in a good word or two about how skilled of a director I am, and how 'professional' our relationship is..."
            bot"Hehe!"
            yo"Kid... What are you trying to achieve here, hmm? Why would I lie to your [him_rel] like that..."
            bo"Lie? Come on, that's a stretch. You are working with me after all, are you not?"
            bo"Besides, it's not like it's costing you anything, right?"
            yo"...I would prefer staying like this. No one has to see me unless absolutely necessary..."
            bo"Come on, Yoru! Help me, so that I can help you... Don't force me to remind you of your circumstances..."
            $ renpy.sound.play("/audio/soun_fx/meow1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            yo"...*Concerned M-meow*!" with vpunch
            yo"Keep walking, kid! *Growls*..." with vpunch

            hide boruto with dissolve
            bot"Bah! Worst case I'll have to use our pictures to convince [him_name]..."
            $ renpy.sound.play("/audio/soun_fx/walkingforest.opus", channel="sfx3", loop=False, relative_volume = 0.2)
            if yoru_cattalk_menu_counter == 1:
                scene bg konoha1 with fade
            elif yoru_cattalk_menu_counter == 2:
                scene inohouse day with fade
            elif yoru_cattalk_menu_counter == 3:
                scene bg porch with fade
            else:
                scene bg porch with fade
            show boruto cat at center with dissolve
            jump yoru_cattalk_menu
        
label yoru_first_photoshoot_love:
    $ initialize_replay_defaults()
    if _in_replay:
        $ yoruichi_relationship = "Obedient"
    $ yoru_1st_photoshoot = True
    $ yoruichi_modelling_completed = True
    scene black with dissolve
    scene ramen workend
    show yoru shy3:
        xpos -1000
    show boruto snob:
        xpos -1000
    show boruto:
        easein 1 xalign 0.3
    pause 0.1
    show yoru:
        easein 1.2 xalign -0.1
    bo"Obo, you fat fuck! Show your self..." with vpunch
    show boss laugh2 at right with dissolve
    obo"I bet this fat man could beat your ass and rail it after. You little twerp..."
    show boss at smallshake
    obo"Haa-haa-haa! Careful how you address me kid!"
    show boss angry2 with dissolve
    obo"What's up with you two looking at me like that... What, are you some kind of lovebirds?"
    menu:
        obo"What's up with you two looking at me like that... What, are you some kind of lovebirds?"
        "{color=[dominancecolor]}We fucked once or twice...{/color}":
            show boruto sceeming with dissolve
            show boruto:
                easein 1 xalign 0.22
            bo"We may have..."
            show yorucutout_waist:
                zoom 0.25 xalign 0.5 yalign 1.0
            
            show cutoutborder_white:
                zoom 0.75 xalign 0.5 ypos 0.11
            with dissolve
            bo"Fucked once or twice!" with vpunch
            show boruto sceeming2 with dissolve
            show yoru disgust at smallshake with dissolve
            $ renpy.sound.play("/audio/soun_fx/groperepeat1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            show yoru_gropeass1_anim1 with dissolve:
                zoom 0.25 xalign 0.5 yalign 1.0
            call changeDominance(1) from _call_changeDominance_70
            yo"{size=*0.8}*Whispers* [bo_name_stutter]!? W-what are you doing, you-!{/size}" with vpunch
            show boss angry3 with dissolve
            "You secretly groped Yoru's ass behind Obo's back..."
            obo"Is that so, Yoru..."
            obo"I always knew you were a whore, but-"
            hide cutoutborder_white
            hide yoru_gropeass1_anim1
            hide yorucutout_waist
            show boruto surprised2
            $ renpy.sound.play("/audio/soun_fx/spank4.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            yo"We have not!" with vpunch
            "She slapped your hand away..."
            show boruto snob with dissolve
            show boss laugh2 with dissolve
            obo"Haa-haa-haa! I knew of course..."
            obo"My wife would never sleep with a twerp like you..."
            bot"We'll see about that you old fuck..."
        "And what if we were, old man?":
            show boruto sceeming with dissolve
            bo"And what if we were, old man..."
            bo"Would you have anything to say about it?"
            show boss angry3 with dissolve
            obo"Hey kid, that's my prized possession standing next to you..."
            obo"Careful what you insinuate... you got it?" with vpunch
            bo"Possession, huh? Is that how you think of her...?"
            show boss:
                easein  0.5 xalign 0.9 zoom 1.05
            obo"Got a problem with that, kid?" with vpunch
            show boss:
                easein  0.5 xalign 0.85 zoom 1.1
            obo"Maybe you wanna take this outside, HUH?" with vpunch
            menu:
                obo"Maybe you wanna take this outside, HUH?"
                "Sure!":
                    bo"Sure-"
                    
                "Uuuh, I was just joking!":
                    show boruto surprised2 with dissolve
            show boss laugh2 with dissolve
            show boss:
                easein 0.7 xalign 0.95 zoom 1.05
            obo"Baa-haa-haa!" with vpunch
            obo"I got you scared shitless with that one, didn't I kid?"
            show boruto snob with dissolve
            bo"Not really..."

        "Nothing like that...":
            bo"Nothing of that sort. You don't have to worry old man..."
            obo"Good..."
    obo"Now which one of you will tell me what's going on between youse..."
    bo"Nothing much... But me and Yoru will be off somewhere after our shift..."
    bo"Will that be a problem, old man?"
    show boss angry3 with dissolve
    obo"Is that right... Yoru?"
    show yoru shy3 with dissolve
    yo"Y-yes... But only for a bit!" with vpunch
    show boss laugh2 with dissolve
    obo"Bwa-haa-haa!" with vpunch
    obo"You don't have to sound so scared, my love. It's not like you are on a leash now, are you?"
    obo"You two can do as you like, so long as Yoru is back by nightfall..."
    obo"You got it, kid?" with vpunch
    bo"Sure thing..."
    show boss angry3 with dissolve
    obo"Now get back to work! Both of you!" with vpunch
    bo"Aye aye..."
    hide boruto with dissolve
    show boss:
        easein 0.3 xalign 0.7
    with vpunch
    "Obo gave Yoru a menacing look before she nervously turned around to join you..."
    show yoru shy with dissolve
    with vpunch
    hide yoru with dissolve
    scene black with dissolve
    "..."
    scene ramenkitchen
    show boruto normal at left
    show yoru obedient at right
    with dissolve
    bo"See? Easy as that..."
    yo"..."
    show yoru lookingbackt at right with dissolve:
        zoom 0.5 ypos 1.05
    yo"Let's get to work... I'll meet with you after our shift ends..."
    hide yoru with dissolve
    scene black with dissolve
    call changeMoney(15) from _call_changeMoney_14
    "You spent some time working the shift..."
    "..."
    scene ramenkitchen
    show boruto normal at left
    show yoru obedient at right
    with dissolve
    bo"Ready to get out of this place for once?"
    show yoru normal with dissolve
    yo"I am not going out there with these greasy rags on me..."
    yo"You'll wait for me here..."
    show yoru lookingbackt at right with dissolve:
        zoom 0.5 ypos 1.05
    yo"I'll take a shower and join you shortly..."
    show boruto snob with dissolve
    bo"Of course..."
    hide yoru with dissolve
    show yoru lookingback with dissolve:
        zoom 1.45 xalign 0.5 yalign 1.0
    show yoru:
        easein 10 yalign 0.1
    bot"I can't believe I managed to convince someone as hot as her to model for me..."
    bot"I am even starting to feel a certain way around her..."
    show yoru:
        easein 1 yalign 0.85
    bot"Perhaps this will be an opportunity to get 'closer' with her..."
    bot"But I should still be careful with how I handle my condition around her. Wouldn't want to blow up my chances with her..."
    hide yoru with dissolve
    show boruto normal with dissolve
    bot"Obo is still an unknown variable in all this. Yoruichi being a Shinigami, even if powerless for the time being, further complicates things..."
    show boruto snob with dissolve
    bot"Argh! Thinking isn't my strong suit! I'll just go with the flow for now and see where that takes me..." with vpunch
    scene black with dissolve
    bot"All that's left is to wait for her..."
    bot"."
    bot".."
    bot"..."
    scene ramenkitchen
    show boruto normal at left
    with dissolve
    bot"I wonder what [him_name] will think of Yoru..."
    show boruto snob with dissolve
    bot"I should probably let Yoru know about our situation in advance..."
    bot"She is supposed to act like my..."
    "As you were finishing your thought, Yoru was making her way down the stairs after finishing her shower..."
    show boruto surprised2 with dissolve
    bot"She is supposed to act like m-my..." with vpunch
    show boruto surprised3 with dissolve
    bot"M-my..." with vpunch
    show 02064 with dissolve:
        zoom 1.1 xalign 0.5 yalign 1.0
    show 02064:
        easein 5 yalign 0.0
    bot"M-my... m-model..." with vpunch
    call increaselust(10) from _call_increaselust_140
    show screen parallax1280("02064",1.1) with dissolve
    call showscrollingimage from _call_showscrollingimage_72
    bot"Ho...ly...FUCK!" with vpunch
    bot"I mean... I've seen parts of her in nude before, but..."
    bot"This is something else!" with vpunch
    bot"I knew she was b-beautiful... and m-muscular, but the way her leotard wraps around her curves is majestic!"
    bot"Looking at how her toned core muscles protrude through the tight material is so fucking sexy..."
    bot"Her nipples, even her cameltoe are almost poking out..."
    bot"Is that what she wears casually...?"
    bot"Or did she dress up just for me! Heh-hehe..." with vpunch
    call hidescrollingimage from _call_hidescrollingimage_73
    scene ramenkitchen
    show boruto surprised2 at left
    show yoruc annoyed:
        xpos 2500
    with dissolve
    show yoruc:
        easein 1 xpos 700
    "With a newfound air of confidence, along with hints of superiority in her voice, Yoru turned to address you..."
    yo"You have a weird look on your face, kid..."
    bo"Y-your outfit..."
    show yoruc snob with dissolve
    yo"Ah yes... Another reason why I can't freely roam this world of yours..."
    yo"It would seem that being hated, spat on and hunted for what I am is not enough around your places..."
    yo"The few amongst you that aren't trying to kill me, are staring at me like some sort of depraved beasts..."
    yo"This is just about the only way I can feel some confidence, the only way I can feel like my older self around this depressing world of yours. Even if it's for a fleeting moment..."
    yo"And even so your people want to strip from me, even this simple gesture... For what? because I take pride in wearing my casual combat outfit...?"
    bo"That's... anything but c-casual!"
    menu:
        bo"That's anything but c-casual!"
        "{color=[dominancecolor]}You look incredibly sexy!{/color}":
            show boruto snob with dissolve
            call changeDominance(1) from _call_changeDominance_71
            bo"You look like the sexiest pin-up girl I've ever laid eyes on..." with vpunch
            bo"That'll do nicely for our modelling session..."
            yo"S-stop it, kid..."
        "You are... beautiful":
            bo"Those kitchen rags hide your true self really well..."
            bo"Yoru, y-you are... beautiful!"
            yo"You are only saying that because of how your kind thinks..."
        
    show yoruc annoyed with dissolve
    yo"Are you humans really that simple? Is everything you see, and everything you think of related to sex?"
    show boruto snob with dissolve
    bo"Unlike you ever-living gods, we humans exist to procreate after all! We'd be extinct otherwise..."
    yo"Such a shallow existence. I almost pity your kind! When you live for as many years as we do..." with vpunch
    $ renpy.sound.play("/audio/soun_fx/transform.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    scene black with flash
    yo"Sex is just something you do for fun!" with vpunch
    "In an instant, Yoru disappeared into a puff of smoke..."
    $ renpy.sound.play("/audio/soun_fx/meow1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    show yoru cat with dissolve
    "Pussy""Meow!"
    bo"."
    bo".."
    "Pussy""You want this pussy, puny human?"
    bo"...!" with vpunch
    "Pussy""Then come and get it! Meow!" with vpunch
    scene black with vpunch
    bo"Y-yoru!?" with vpunch
    scene ramenkitchen
    show boruto surprised3 at center
    show yoru cat2t behind boruto:
        zoom 0.25 xpos 1196 ypos 554
    with dissolve
    $ renpy.sound.play("/audio/soun_fx/meow2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    show yoru:
        easein 2 xpos -1000
    yo"*Meow!* What's wrong... Can't keep up with me?"
    hide yoru with dissolve
    show yoru cat2t behind boruto:
        zoom 0.25 xpos -1000 ypos 554 xzoom -1
    show yoru:
        easein 1.5 xpos 1300 xzoom -1
    "It would appear Yoruichi had the ability to transform herself into a cat..."
    hide yoru with dissolve
    show yoru cat2t behind boruto:
        zoom 0.25 xpos 1300 ypos 554
    show yoru:
        easein 1.5 xpos -1100
    yo"Can't get the pussy, can you, little human!"
    "She started sprinting around the kitchen, hurling insults at you in a playful manner..."
    hide yoru with dissolve
    show yoru cat2t behind boruto:
        zoom 0.25 xpos -1000 ypos 554 xzoom -1
    show yoru:
        easein 1.5 xpos 1300 xzoom -1
    bo"What the fuck is going on!"
    bo"I thought you said you lost your p-powers..."
    hide yoru with dissolve
    show yoru cat2t behind boruto:
        zoom 0.25 xpos 1300 ypos 554
    show yoru:
        easein 1.5 xpos -1100
    yo"*Meow!* Maybe I did, maybe I didn't..."
    show yoru:
        easein 2 xpos -1000 xzoom 1
    bot"She r-really is a god..."
    bot"Did I... underestimate her powers?" with vpunch
    scene black with flash
    $ renpy.sound.play("/audio/soun_fx/hiss.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    yo"Meow!" with vpunch
    scene ramenkitchen
    show boruto cat at center
    with dissolve
    "Yoru jumped on your shoulder..."
    yo"*Hiss* In reality, You'll never know..."
    yo"Or maybe you will, if you keep being a good boy..."
    bo"*Nervous laughter* Heh...hehe! Don't claw my face off, p-please..."
    $ renpy.sound.play("/audio/soun_fx/meow1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    yo"If you play nice... *Meow*"
    yo"Now get a move on!" with vpunch
    show boruto:
        easein 2 xpos -1500
    bo"R-right!" with vpunch
    $ playmusic("/audio/ost/market.opus", 0.6)
    scene black with dissolve
    scene bg ramenshop
    show boruto cat at center
    with dissolve
    bo"It'll be a while until we make it to my place..."
    $ renpy.sound.play("/audio/soun_fx/meow1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    yo"*Meow* I don't mind... It's not often I get to see and breathe the countryside..."
    yo"Thank you for this opportunity, [bo_name]... And for trying to help..."
    yo"Your kind makes it difficult for me to trust any human, but... I do enjoy your company from time to time..."
    bo"Heh... Might as well use the opportunity to get to know each other a little bit better?"
    yo"*Growls* Hiss... I'd prefer silence, but..."
    yo"Talk, if you must..."
    hide boruto with dissolve
    $ renpy.sound.play("/audio/soun_fx/walkingforest.opus", channel="sfx3", loop=False, relative_volume = 0.2)
    scene bg konoha2 with fade
    show boruto cat at center with dissolve
    $ yorucatmenul1 = []
    menu yoru_cattalk_menu_love:
        set yorucatmenul1
        yo"Talk, if you must..."

        "We are here. Are you going to..." if yoru_cattalk_menu_counter >=3:
            bo"We've made it to my place..."
            $ renpy.sound.play("/audio/soun_fx/meow2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            yo"*Anxious Meow!* Good! Take me to your p-place, quick!" with vpunch
            bo"H-hold on... about what we discussed... are you planning on staying like that or do I-"
            $ renpy.sound.play("/audio/soun_fx/hiss.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            yo"*H-hiss!!* Of c-course I am staying like this..." with vpunch
            yo"I told you, I am n-not going to be your social butterfly!"
            bo"F-fine, sheesh..."
            show boruto:
                easein 0.3 xalign 0.2
            pause 0.2
            bo"Don't have to sound so-!" with vpunch
            $ renpy.sound.play("/audio/soun_fx/transform.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            scene black with flash
            yo"D...D-damn it!" with vpunch
            "A sudden puff of smoke clouded the area around you..."
            show yoru_failcat1 with dissolve
            show yoru_failcat1:
                easein 5 yalign 0.6
            with vpunch
            "As it cleared, it revealed a tired looking Yoruichi, still maintaining a feline stance on the ground..."
            bo"Y-yoru?" with vpunch
            bot"She must have problems sustaining her feline form for long periods of time, meaning..."
            bot"She likely is 'almost' powerless, after all..."
            yo"W-what are you looking at me for! I am just taking a small break..." with vpunch
            bo"I am... s-sorry. Your transformation caught me off-guard..."
            bo"Is everything, okay? You are looking a bit exhausted..."
            yo"*Concealed Panting*... Exhausted?"
            yo"N-not... really..."
            show yoru_failcat2_1 with dissolve
            show yoru_failcat2_1:
                easein 5 yalign 0.6
            yo"I was just about to go..."
            $ renpy.sound.play("/audio/soun_fx/transform.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            scene black with flash
            yo"...Back to my f-feline form!" with vpunch
            bot"."
            show yoru_failcat2 with dissolve
            show yoru_failcat2:
                easein 5 yalign 0.6
            bot".."
            bo"...!" with vpunch
            bot"She really is powerless..."
            bo"You know... You don't have to hide anything from-"
            show yoru_failcat2 with dissolve:
                zoom 0.7 xalign 0.5 yalign 0.6
            yo"I..." with vpunch
            show yoru_failcat3 with dissolve:
                yalign 0.0
            show yoru_failcat3:
                easein 2 yalign 1.0
            yo"I changed my mind! M-maybe I should meet this [him_rel] of yours after all..."
            show screen parallax1280("yoru_failcat3") with dissolve
            call showscrollingimage from _call_showscrollingimage_73
            bo"You did? I appreciate that..."
            bot"I know she is probably lying, but it's better if I don't make her feel uncomfortable..."
            bo"Although it's probably for the best if you got off the floor. Wouldn't want my family to think you are some weird pet-play enthusiast, would you?"
            hide screen parallax1280
            show screen parallax1280("yoru_failcat3_1",1,0.2)
            with dissolve
            yo"P-petplay? What even is that, kid!" with vpunch
            yo"*Sigh*... Do I even want to know?"
            yo"N-nevermind all that! Let's get moving..."
            call increaselust(5) from _call_increaselust_141
            bo"Good kitty!" with vpunch
            call hidescrollingimage from _call_hidescrollingimage_74
            scene bg porch
            show boruto snob at left with dissolve
            bo"You ready?"
            "Yoru pats herself clean from the dirt on her knees and gets up..."
            show yoruc snob at right with dissolve
            yo"Let's go inside..."
            hide boruto with dissolve
            hide yoruc with dissolve
            $ renpy.sound.play("/audio/soun_fx/dooropen.opus", channel="sfx3", loop=False, relative_volume = 0.6)
            scene black with dissolve
            bo"I am home..." with vpunch
            $ playmusic("audio/ost/house2.opus",0.6)
            show bg lr_day with dissolve:
                zoom 0.68
            show boruto snob with dissolve:
                xpos 160
            show yoruc annoyed with dissolve:
                xpos -150
            hin"Oh, [bo_name]! Just a second..."
            bo"Just follow my lead, alright?"
            yo"S-sure..." with vpunch
            show shina shy:
                xpos 2000
            show shina:
                easein 1 xpos 800
            hin"Welcome back, How was..."
            show shina surprised with dissolve
            hin"[bo_name_stutter]!?" with vpunch
            hin"You didn't tell me y-you...-"
            show yoruc normal with dissolve
            yo"Apologies for the intrusion, my lady..."
            show shina shy2 with dissolve:
                ypos -30
            hin"No need to apologize at all!" with vpunch
            hin"I was simply not expecting guests today, you'll have to forgive my lack of hospitality!"
            show shina shy with dissolve
            $ renpy.sound.play("/audio/soun_fx/footsteps.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            "Hearing the commotion, [him_name]'s curiosity was piqued. She quickly made her way to the living room..."
            hin"Will you please make the introductions, [bo_name_stutter]?"
            show hima worried2 behind shina:
                xpos 2000 zoom 0.34
            show hima:
                easein 1 xpos 900
            show shina:
                easein 1 xpos 600
            him"[hin_rel]? Is everything...-" with vpunch
            show hima surprised with dissolve:
                xpos 930 zoom 0.34
            him"...A-alright?"
            himt"Who the heck is that!" with vpunch
            hin"You are just in time [him_name]... [bo_name] was about to make the introductions!"
            himt"She is so... pretty! Who is she to [bo_name_stutter] anyway!"
            bo"Yoru, meet my [hin_rel], [hin_name]. Next to her is my [him_rel], [him_name]..."
            show yorucombatcutout_ass with dissolve:
                zoom 0.4 xalign 0.0 yalign 1.0
            bo"[hin_rel], [him_name]... this is Yoru..."
            menu yoruintromenuh1_love:
                bo"[hin_rel], [him_name], this is Yoru..."
                "{color=[dominancecolor]}She is my model{/color}":
                    call checkDominance(15,"yoruintromenuh1_love") from _call_checkDominance_16
                    show boruto:
                        easein 0.5 xpos 120
                    hide yorucombatcutout_ass with dissolve
                    show yorucombatcutout_waist1 with dissolve:
                        zoom 0.4 xalign 0.0 yalign 1.0
                    call changeDominance(1) from _call_changeDominance_72
                    bo"She is my model!"
                    bo"We are working on something together..."
                    hide yoru_combatcutout_gropeanim1
                    hide yorucombatcutout_grope1
                    hide yorucombatcutout_waist1
                    hide yorucombatcutout_ass
                    show yoruc annoyed with dissolve
                    yo"Nice to meet you, [hin_name]-san, [him_name]-chan..."
                    show shina surprised with dissolve
                    hin"Explains your good looks Yoru-san! The pleasure is ours..."
                    show hima worried2 with dissolve
                    him"N-nice to meet you too..."
                    call changeObedience("Himawari", 1) from _call_changeObedience_106
                    himt"A r-real model, huh? He really wasn't lying about that..."
                    show shina smiling with dissolve
                    hin"You should have said something earlier [bo_name]! I would have prepared something for you and your friend!"
                    show yoruc at smallshake
                    yo"I appreciate your hospitality, lady [hin_name]. I unfortunately won't be staying for much longer..."
                "{color=[obediencecolor]}A friend who works as a model...{/color}":
                    hide yorucombatcutout_ass
                    bo"She is a good friend of mine who works as a model..."
                    bo"We are working on something together..."
                    show yoruc annoyed with dissolve
                    yo"Nice to meet you, [hin_name]-san, [him_name]-chan..."
                    show shina surprised2 with dissolve
                    hin"T-the pleasure is ours!" with vpunch
                    show hima worried2 with dissolve
                    him"N-nice to meet you too..."
                    call changeObedience("Himawari", 1) from _call_changeObedience_107
                    himt"A r-real model, huh? He really wasn't lying about that..."
                    show shina smiling with dissolve
                    hin"You should have said something earlier [bo_name]! I would have prepared something for you and your friend!"
                    show yoruc at smallshake
                    yo"I appreciate your hospitality, lady [hin_name]. I unfortunately won't be staying for much longer..."
                "{color=[hatredcolor]}My girlfriend!{/color}":
                    show boruto:
                        easein 0.5 xpos 120
                    show yorucombatcutout_waist1 with dissolve:
                        zoom 0.4 xalign 0.0 yalign 1.0
                    bo"She is my..."
                    call changeHatred(1) from _call_changeHatred_128
                    show yorucombatcutout_grope1 with dissolve:
                        zoom 0.4 xalign 0.0 yalign 1.0
                    bo"Girlfriend! Among a few other things... Today she's here to help me with something I am working on!" with vpunch
                    $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                    show yoru_combatcutout_gropeanim1:
                        zoom 0.4 xalign 0.0 yalign 1.0
                    "'Play along...' You quietly whispered in her ear, as you discreetly started lightly groping her ass..."
                    "In complete disbelief, both [hin_name] and [him_name] exclaimed..."
                    "Both" "G-girlfriend!?" with vpunch
                    hide yoru_combatcutout_gropeanim1
                    hide yorucombatcutout_grope1
                    hide yorucombatcutout_waist1
                    hide yorucombatcutout_ass
                    show boruto:
                        easein 0.4 xpos 150
                    show yoruc annoyed with dissolve
                    yo"*Tsk!*"
                    "Yoru pushed your hand away and made a quiet sound of disapproval, but ultimately..."
                    yo"Nice to meet you, [hin_name]-san, [him_name]-chan..."
                    show shina surprised2 with dissolve
                    hin"T-the pleasure is ours!" with vpunch
                    show hima worried2 with dissolve
                    him"N-nice to meet you too..."
                    show shina smiling with dissolve
                    hin"You should have said something earlier [bo_name]! I would have prepared something for you and your friend!"
                    show yoruc at smallshake
                    yo"I appreciate your hospitality, lady [hin_name]. I unfortunately won't be staying for much longer..."
                    
                    $ yorugroped_intro == True

            label beforemodelrepeat_love:
            yo"{size=*0.8}*Whispers* Wrap this up kid! I didn't sign up for introductions...{/size}" 
            bo"[hin_rel], [him_name]... Unfortunately introductions have to be cut short for now!"
            show boruto:
                easein 2.5 xpos 2000
            show shina surprised with dissolve
            bo"Yoru has to be somewhere soon and we are in a bit of a hurry!" with vpunch
            show yoruc normal with dissolve
            show yoruc:
                easeout 2.5 xpos 2000
            yo"Please excuse my intrusion!"
            "Both" "Oh..."
            pause 1
            show shina shy at left with dissolve
            show hima:
                easein 1 xalign 0.8
            him"."
            hin".."
            him"..."
            "both""Did you see her!?" with vpunch
            hin"She was..."
            him"...so pretty! Almost otherwordly even..." with vpunch
            hin"Right?" with vpunch
            if yorugroped_intro == True:
                him"How did that idiot even..."
                him"He s-said, Yoru is his... g-girlfriend!?"
                show hima mad with dissolve
                him"H-hoW!? He is stupid, ugly and... and-" with vpunch
            else:
                him"How did that idiot even become friends with someone like her..."
                him"She is so well-spoken, kind, she even works as a model! Meanwhile..."
                show hima mad with dissolve
                him"[bo_name] is just a c-clown!" with vpunch
            show shina smiling with dissolve
            hin"*Giggles* [him_name]... Your [him_rel_to_bo] is actually quite the catch himself you know...."
            hin"He has always been a pretty boy! Strong, caring and thoughtful..."
            show shina shy with dissolve
            hin"He might be having his issues with his recent diagnosis, but I am sure he's doing his best to help himself, and us..."
            hin"Cut him some slack, alright?"
            $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            him"Hmph!" with vpunch
            show hima worried2 with dissolve
            scene black with dissolve
            "[hin_name] and [him_name] spent some time gossiping about your new friend..."
            scene bg bb day
            show boruto snob at left
            show yoruc annoyed at right
            with dissolve
            if yorugroped_intro == True:
                yo"Your girlfriend!? I don't appreciate being put on the spot like that, kid..." with vpunch
                bo"You are right, I am sorry! I was just trying to get us through the introductions..."
                show yoruc snob with dissolve
                yo"Don't ever do that again please..."
            else:
                show yoruc snob with dissolve
                yo"Your [hin_rel] and [him_rel] seemed like nice people..."
                yo"Maybe there still is some hope for your kind after all..."
                bo"Cold, Yoru... I am helping you after all, aren't I?"
                yo"I know, just poking some fun at you!"
            yo"So... what now?"
            yo"How do you plan on making us any money from your bedroom, kid..."
            bo"You'll find out soon enough..."
            show boruto:
                easein 2 xpos -600
            bo"For starters, why don't you make yourself comfortable at your working enviroment..."
            scene black with dissolve
            yo"And that is... your bedroom?"
            show bg modelling:
                yalign 1.0
            with dissolve
            show boruto snob at right with dissolve
            show yoruc annoyed at left with dissolve
            bo"Not quite! I've prepared this space specifically for your modelling and my directing aspirations..."
            bo"Spacious, plain, and graced by natural lighting. Here is where I'll build my kingdom, with you in the spotlight!"
            yo"Eh, I'll believe it when I see it..." with vpunch
            yo"What's the mattress on the side for...?"
            bo"Just a prop, for now! Or something to be used to enhance some of our shots..."
            bo"Besides, wouldn't want you to tire yourself out..."
            $ renpy.screenshot("test.png")
            hide boruto with dissolve
            bo"You can take a seat over there until I prepare my equipment..."
            yo"How thoughtful of you..."
            hide yoruc with dissolve
            scene black with dissolve
            "Yoru takes a seat at the mattress while you prepare your equipment..."
            show yorum_intro0 with dissolve:
                yalign 1.0
            show yorum_intro0:
                easein 4 yalign 0.1
            yo"You've given this some thought after all..."
            bo"Wait till you see this..."

            scene bg modelling with dissolve:
                yalign 1.0 blur 5
            show boruto snob at center with dissolve
            bo"I don't know about your place, but here in our world, these little machines are practically small miracles..."
            hide boruto with dissolve
            scene black with dissolve
            show screen camera1280("yorum_intro0") with dissolve
            show screen camera_ui("Yoruichi",False) with dissolve
            # call showscrollingimage
            bo"To be able to capture and freeze any moment in time... It's a power like no other!"
            "Pan the camera to capture Yoru's face or... other features of hers!"
            yo"A c-camera... isn't it?"
            yo"I've only seen one before at Obo's place..."
            yo"But he never really told me what it's all about..."
            bo"Ready... and..."
            show expression FocusEffect("idle1", 180, 350, 100, 0.7) as focus_effect onlayer screens with dissolve
            show screen camera_ui("Yoruichi")
            hide expression FocusEffect as focus_effect onlayer screens
            with dissolve
            $ ui.interact()
            show screen camera_ui("Yoruichi",False) with dissolve
            bo"They are exceptionally rare after all, not to mention expensive..."
            yo"That flash just now... What was it?" with vpunch
            bo"That flash was the beginning of our lucrative relationship..."
            bo"Our very first photo shoot!" with vpunch
            hide screen camera_ui
            hide screen camera1280
            scene black
            with dissolve
            yo"Photo... shoot?"
            bo"Here, Wanna see?"
            show yorum_intro1 with dissolve:
                yalign 1.0
            show screen photo_album with dissolve
            yo"..."
            show yorum_intro1:
                easein 2 yalign 0.0
            bo"That's a picture of you. Forever captured and preserved for everyone to marvel at until the end of time..."
            yo"I-interesting... Although I don't think I understand how any of this w-works..."
            bo"You don't have to! That's why I am here after all!"
            bo"With my knowledge, along with my direction and your beauty, I sense an opportunity like no other..."
            yo"Beauty, huh? What makes you think other people see what you do. Have you forgotten how your kind treats me?"
            yo"I am practically worth less than dirt to them..."
            bo"See, you don't know people like I do Yoru..."
            bo"People fear what they don't understand, and act like they despise what they can't have..."
            bo"Regardless of how they might treat you, I bet you there's no man on earth, maybe woman too, who would look at you and not stare for a second..."
            scene black with dissolve
            "Yoru seemed overwhelmed by your suggestion. She shifted her posture and said..."
            show yorum_intro2 with dissolve:
                yalign 1.0
            show yorum_intro2:
                easein 3 yalign 0.1
            yo"...Because of what I am?"
            bo"Because of how you look, Yoru! You are so exotically beautiful..." with vpunch
            bo"Which is exactly why I think your pictures could net us a fortune!"
            show screen parallax1280("yorum_intro2") with dissolve
            call showscrollingimage from _call_showscrollingimage_74
            yo"How can you be so certain of that..."
            bo"Think of it like this... If I am right and people fear you for what you are, but lust over how you look, then..."
            bo"Would a picture of you not be the closest they can get to you without risk? It's the perfect business opportunity!"
            bo"In fact, I am pretty sure that's exactly how Obo makes use of his own gear..."
            bo"He is using you, Yoru! He makes money of your own appearance and leaves nothing for you..."
            yo"..."
            yo"That... b-bastard!" with vpunch
            call hidescrollingimage from _call_hidescrollingimage_75
            scene black with dissolve
            "Yoru gets up and starts pacing around the room in frustration..."
            show bg modelling:
                yalign 1.0
            show boruto snob at right with dissolve
            show yoruc annoyed at left with dissolve
            with dissolve
            yo"I knew he was using his own stuff for w-work or something. But I never thought one could profit from something like this!" with vpunch
            bo"Right? Its about time you stop relying on him..."
            yo"*Groans* Aaarh! And do what... rely on a kid instead?" with vpunch
            show boruto normal with dissolve
            bo"On yourself, Yoru..."
            show yoruc normal with dissolve
            show boruto snob with dissolve
            bo"And then me! Not just a kid, your director and business partner..."
            show yoruc snob with dissolve
            yo"On myself, huh..."
            scene black with dissolve
            $ renpy.sound.play("/audio/soun_fx/heels1.opus", channel="sfx2", loop=False, relative_volume = 0.8)
            "Once again, Yoru started pacing your room..."
            show yoru_modelstart with dissolve:
                zoom 1.65 xalign 1.0 yalign 1.0
            show yoru_modelstart:
                easein 4 yalign 0.1
            "But this time she seemed at ease, lost in her own thoughts..."
            show yoru_modelstart with dissolve:
                zoom 1.65 xalign 0.0 yalign 1.0
            show yoru_modelstart:
                easein 4 yalign 0.1
            yo"Being able to rely on myself does have a nice ring to it..."
            yo"And something's strangely comforting about you, [bo_name]..."
            yo"...Equal partners then?"
            bo"Equal partners!"
            yo"Then I'll place my trust in you kid. But if you ever cross me..."
            scene yoru_modelstart with dissolve:
                yalign 1.0
            show yoru_modelstart:
                easein 2 yalign 0.1
            bo"I would never cross a god, Yoru... Even one whose secrets I know! Heh..."
            show screen parallax1280("yoru_modelstart",1,0.2,True) with dissolve
            yo"Heh! There's so much you don't know about me, kid..."
            bo"Perhaps it's time we change that then. But before we embark on that journey..."
            bo"I want one last thing from you before we start..."
            yo"Sure..."
            bo"From now on you will address me as Director [bo_name]. If I hear 'kid' another time, I might just lose my mind..."
            yo"*Giggles* Director? Your name alone will do, [bo_name]..."
            $ yoru_picture_counter +=1
            menu:
                yo"What do I do next, [bo_name]..."
                
                "Let's start with a frontal medium shot!":
                    bo"Let's start with something simple to ease you into it..."
                    yo"Sure..."
                    hide screen parallax1280
                    show yoru_frontalstart:
                        yalign 1.0 xalign 0.5
                    with dissolve
                    show yoru_frontalstart:
                        easein 2 yalign 0.0
                    bo"How about a frontal medium shot..."
                    yo"Speak plainly Ki-, [bo_name]..."
                    bo"Caught yourself there, huh? I like that..."
                    bo"A medium shot is a picture that focuses on the subject's waist line and above..."
                    bo"I see... Now what?"
                    menu :
                        yo"..."
                        "Strike a dynamic pose..." if yoru_frontal_dynamic == False:
                            $ yoru_frontal_dynamic = True
                            bo"Now you strike a pose!"
                            bo"Given your current attire, let's compliment your body's features with a dynamic combat pose..."
                            bo"Plenty of movement, muscle flexing, and a daring look... think you can pull that off?"
                            show yoru_frontal_dynamicpose with dissolve:
                                yalign 1.0
                            show yoru_frontal_dynamicpose:
                                easein 2 yalign 0.0
                            yo"Something like..."
                            yo"...This?"
                            show screen camera1280("yoru_frontal_dynamicpose") with dissolve
                            show screen camera_ui("Yoruichi",False) with dissolve
                            bo"You are a natural, Yoru!"
                            bo"Now hold that pose for me, and..."
                            show screen camera_ui("Yoruichi",True) with dissolve
                            $ ui.interact()
                            show screen camera_ui("Yoruichi",False) with dissolve
                            bo"Excellent..."
                            show screen camera1280("yoru_frontalstart") with dissolve
                            yo"That flash... It means you got a picture, right?"
                            bo"Indeed, a great one too!"
                            yo"In that case, I'll allow you a few more flashes."
                            yo"I'll keep following your directions, but if you fail to make any money with these first few flashes..."
                            yo"Then I am not sure this will be worth much of my time... Fair enough?"
                            bo"A reasonable ask..."
                            bo"But If I only get a few more flashes, then it's time to amp up the heat!" with vpunch
                            bo"Are you ready for the next one?"
                            yo"Let's do it..."

                        "Strike a confident pose..." if yoru_frontal_confident == False:
                            $ yoru_frontal_confident = True
                            bo"Now you strike a pose!"
                            bo"Let's have you pose in a confident manner. Flick your hair, and stare straight into the lens with a serious expression..."
                            show yoru_frontal_confidentpose with dissolve:
                                yalign 1.0
                            show yoru_frontal_confidentpose:
                                easein 2 yalign 0.0
                            yo"Something like..."
                            yo"...This?"
                            show screen camera1280("yoru_frontal_confidentpose") with dissolve
                            show screen camera_ui("Yoruichi",False) with dissolve
                            bo"You are a natural, Yoru!"
                            bo"Now hold that pose for me, and..."
                            show screen camera_ui("Yoruichi",True) with dissolve
                            $ ui.interact()
                            show screen camera_ui("Yoruichi",False) with dissolve
                            bo"Excellent..."
                            show screen camera1280("yoru_frontalstart") with dissolve
                            yo"That flash... It means you got a picture, right?"
                            bo"Indeed, a great one too!"
                            yo"In that case, I'll allow you a few more flashes."
                            yo"I'll keep following your directions, but if you fail to make any money with these first few flashes..."
                            yo"Then I am not sure this will be worth much of my time... Fair enough?"
                            bo"A reasonable ask..."
                            bo"But If I only get a few more flashes, then it's time to amp up the heat!" with vpunch
                            bo"Are you ready for the next one?"
                            yo"Let's do it..."
                        
                "Let's start with a rear full shot!":
                    bo"Let's start with something simple to ease you into it..."
                    yo"Sure..."
                    bo"How about a rear full shot..."
                    yo"Speak plainly Ki-, [bo_name]..."
                    bo"Caught yourself there, huh? I like that..."
                    bo"A full rear shot is a picture that focuses on the subject's full body... from the rear of course!"
                    hide screen parallax1280
                    show yoru_rearstart:
                        yalign 0.0 xalign 0.5
                    with dissolve
                    show yoru_rearstart:
                        easein 2 yalign 1.0
                    yo"The rear, huh? I see... Now what?"
                    bot"The ass on this woman..."
                    show screen camera1280("yoru_rearstart") with dissolve
                    show screen camera_ui("Yoruichi",False) with dissolve
                    menu:
                        yo"..."
                        "Stay exactly as you are..." if yoru_rear_stay == False:
                            $ yoru_rear_dynamic = True
                            bo"You know what? I think you might have accidentally struck perfection..."
                            yo"I... did?"
                            bo"Stay exactly as you are..."
                            bo"We are going to turn this into a medium shot instead..."
                            bo"And..."
                            show screen camera_ui("Yoruichi",True) with dissolve
                            $ ui.interact()
                            show screen camera_ui("Yoruichi",False) with dissolve
                            yo"That flash... It means you got a picture, right?"
                            bo"Indeed, a great one too!"
                            yo"In that case, I'll allow you a few more flashes."
                            yo"I'll keep following your directions, but if you fail to make any money with these first few flashes..."
                            yo"Then I am not sure this will be worth much of my time... Fair enough?"
                            bo"A reasonable ask..."
                            bo"But If I only get a few more flashes, then it's time to amp up the heat!" with vpunch
                            bo"Are you ready for the next one?"
                            yo"Let's do it..."

                        "Strike a dynamic pose..." if yoru_rear_dynamic == False:
                            $ yoru_rear_dynamic = True
                            bo"Now you strike a pose!"
                            bo"Given your current attire, let's compliment your body's features with a dynamic combat pose..."
                            bo"Plenty of movement, muscle flexing, and a daring look... think you can pull that off?"
                            hide screen camera1280
                            hide screen camera_ui
                            with dissolve
                            show yoru_rear_dynamic with dissolve:
                                yalign 1.0
                            show yoru_rear_dynamic:
                                easein 2 yalign 0.0
                            yo"Something like..."
                            yo"...This?"
                            show screen camera1280("yoru_rear_dynamic") with dissolve
                            show screen camera_ui("Yoruichi",False) with dissolve
                            bo"You are a natural, Yoru!"
                            bo"Now hold that pose for me, and..."
                            show screen camera_ui("Yoruichi",True) with dissolve
                            $ ui.interact()
                            show screen camera_ui("Yoruichi",False) with dissolve
                            bo"Excellent..."
                            show screen camera1280("yoru_rearstart") with dissolve
                            yo"That flash... It means you got a picture, right?"
                            bo"Indeed, a great one too!"
                            yo"In that case, I'll allow you a few more flashes."
                            yo"I'll keep following your directions, but if you fail to make any money with these first few flashes..."
                            yo"Then I am not sure this will be worth much of my time... Fair enough?"
                            bo"A reasonable ask..."
                            bo"But If I only get a few more flashes, then it's time to amp up the heat!" with vpunch
                            bo"Are you ready for the next one?"
                            yo"Let's do it..."

                        "Strike a confident pose..." if yoru_rear_confident == False:
                            $ yoru_rear_confident = True
                            bo"Now you strike a pose!"
                            bo"Let's have you pose in a confident manner. Imagine this scenario..."
                            bo"Someone's calling out your name and you are looking over your shoulder to check who it is..."
                            bo"Your look pierces through whoever called  out with its brimming confidence..."
                            bo"Think you can do that?"
                            hide screen camera1280
                            hide screen camera_ui
                            with dissolve
                            show yoru_rear_casual with dissolve:
                                yalign 1.0
                            show yoru_rear_casual:
                                easein 2 yalign 0.0
                            yo"Something like..."
                            yo"...This?"
                            show screen camera1280("yoru_rear_casual") with dissolve
                            show screen camera_ui("Yoruichi",False) with dissolve
                            bo"You are a natural, Yoru!"
                            bo"Now hold that pose for me, and..."
                            show screen camera_ui("Yoruichi",True) with dissolve
                            $ ui.interact()
                            show screen camera_ui("Yoruichi",False) with dissolve
                            bo"Excellent..."
                            show screen camera1280("yoru_frontalstart") with dissolve
                            yo"That flash... It means you got a picture, right?"
                            bo"Indeed, a great one too!"
                            yo"In that case, I'll allow you a few more flashes."
                            yo"I'll keep following your directions, but if you fail to make any money with these first few flashes..."
                            yo"Then I am not sure this will be worth much of my time... Fair enough?"
                            bo"A reasonable ask..."
                            bo"But If I only get a few more flashes, then it's time to amp up the heat!" with vpunch
                            bo"Are you ready for the next one?"
                            yo"Let's do it..."
                    jump yoru_repeatmodelling
                



            








        "About your transformation powers...":
            $ yoru_cattalk_menu_counter += 1
            bo"So... about your powers, I thought you said you lost your Shinigami powers..."
            $ renpy.sound.play("/audio/soun_fx/meow2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            yo"I... did? *Confused Meow*" with vpunch
            yo"Must have misspoken..."
            bot"She is probably keeping that secret for her own safety..."
            bo"Can you... transform into anything you like? If so, why a cat...?"
            $ renpy.sound.play("/audio/soun_fx/meow1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            yo"I like felines! *Meow*..."
            yo"In truth, it's simply my means of staying under the radar and avoiding confrontation..."
            yo"I've told you how people act towards me before..."
            $ renpy.sound.play("/audio/soun_fx/meow2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            yo"But like this, I can Inconspicuously *Meow* at bumbling idiots and be left alone..."
            $ renpy.sound.play("/audio/soun_fx/hiss.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            yo"*Growls* Hissss!" with vpunch
            show boruto at smallshake
            yo"Like this, see?"
            bo"I would hope that I am not one of those bumbling idiots then... Heh!" with vpunch
            yo"Of course not, for now..."
            $ renpy.sound.play("/audio/soun_fx/meow1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            yo"*Loving Meow* You get the nicer sounding meows, up until you lose my respect..."
            yo"But you have to understand, I need to stay like this to avoid the discrimination I am facing from your kind..."
            bo"Of course. I am just hoping that one day you'll be able to freely roam without having to worry about that..."
            $ renpy.sound.play("/audio/soun_fx/meow2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            yo"*Shy M-meow...*"
            hide boruto with dissolve
            $ renpy.sound.play("/audio/soun_fx/walkingforest.opus", channel="sfx3", loop=False, relative_volume = 0.2)
            if yoru_cattalk_menu_counter == 1:
                scene bg konoha1 with fade
            elif yoru_cattalk_menu_counter == 2:
                scene inohouse day with fade
            elif yoru_cattalk_menu_counter == 3:
                scene bg porch with fade
            else:
                scene bg porch with fade
            show boruto cat at center with dissolve
            jump yoru_cattalk_menu_love


        "Your outfit, it's important to you, isn't it...?":
            $ yoru_cattalk_menu_counter += 1
            bo"Your outfit... You said something about it reminding you of your older self..."
            bo"It's important to you, isn't it?"
            yo"It's just what I wore back when I used to serve as the Captain of a Shinigami squad..."
            yo"That is, until I got exiled... The only thing that remains from that time is this outfit..."
            yo"The material it's made of is infused with my reiatsu. Wearing it gives me the ability  to push my body to it's absolute limits; If and when needed..."
            yo"But nowadays, it simply serves as memorabilia of days old..."
            $ renpy.sound.play("/audio/soun_fx/meow2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            yo"It's... comforting... *Sad Meow :(*"
            bo"R-rei...jutsu?"
            yo"*Sigh* You wouldn't get it..."
            yo"Look kid, point being... I wear it because I am comfortable in it! And yes, it's important to me..."
            yo"In any case, it's just some casual clothing, I don't understand why you humans act the way you do... "
            bo"I think our definition of 'casual' might differ from your kind's..."
            yo"I've come to realize that when I first met with Obo..."
            yo"He quickly prohibited me from wearing my outfit while working at his place. 'For your own safety', he said... But I reckon it was something else..."
            yo"As every customer of his would stare at me with lust in their eyes..."
            yo"The same way you did just moments ago *Meow!*" with vpunch
            bo"I wasn't c-complaining or anything. Just... admiring your beauty!"
            $ renpy.sound.play("/audio/soun_fx/hiss.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            yo"Hiss! Not my concern if your kind is comprised of simple-minded, sex-deprived pests. *Meow*!" with vpunch
            $ renpy.sound.play("/audio/soun_fx/meow1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            yo"This is what I am comfortable wearing, so this is what I'll wear! *Angry Meow!*" with vpunch
            bo"G-got it!"
            yo"*Growls* Hiss! Enough about this! Keep walking..." with vpunch
            bo"R-right..."
            hide boruto with dissolve
            $ renpy.sound.play("/audio/soun_fx/walkingforest.opus", channel="sfx3", loop=False, relative_volume = 0.2)
            if yoru_cattalk_menu_counter == 1:
                scene bg konoha1 with fade
            elif yoru_cattalk_menu_counter == 2:
                scene inohouse day with fade
            elif yoru_cattalk_menu_counter == 3:
                scene bg porch with fade
            else:
                scene bg porch with fade
            show boruto cat at center with dissolve
            jump yoru_cattalk_menu_love
        "(I should mention [him_name]...)":
            $ yoru_cattalk_menu_counter += 1
            bo"Hey, there's someone I would like for you to meet when we get to my place..."
            yo"Kid... I am not about to turn into a social butterfly for you. I've only agreed to do the photo shoot, nothing less, nothing more..."
            bo"Come on, it's only gotta be a small exchange of words with her! Besides, I am pretty sure you and her would make good friends..."
            $ renpy.sound.play("/audio/soun_fx/meow2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            yo"...H-her? *Curious M-meow?*..."
            bo"How did that pique your interest... Are you into girls or something?"
            $ renpy.sound.play("/audio/soun_fx/hiss.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            yo"Shut it, kid... *Hiss*!" with vpunch
            yo"So... Who's this her you are referring to?"
            bo"Her name is [him_name]. She is my [him_rel]..."
            bo"I just need you to exchange pleasantries with her and maybe..."
            bo"Throw in a good word or two about how skilled of a director I am, and how 'professional' our relationship is..."
            bot"Hehe!"
            yo"Kid... What are you trying to achieve here. Why would I lie to your [him_rel] like that..."
            bo"Lie? Come on, that's a stretch. We'll be working together after all..."
            bo"It's just a little favor, to help mend my relationship with my [him_rel]..."
            yo"I would prefer staying like this, but... I will consider your proposal."
            bo"Thank you. I appreciate that..."
            bo"Maybe you two will even hit it off!"
            $ renpy.sound.play("/audio/soun_fx/meow1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            yo"M-meow*!" with vpunch
            yo"Keep walking, kid! *Growls*..." with vpunch
            hide boruto with dissolve
            bot"Worst case, I'll have to use our pictures to convince [him_name]..."
            $ renpy.sound.play("/audio/soun_fx/walkingforest.opus", channel="sfx3", loop=False, relative_volume = 0.2)
            if yoru_cattalk_menu_counter == 1:
                scene bg konoha1 with fade
            elif yoru_cattalk_menu_counter == 2:
                scene inohouse day with fade
            elif yoru_cattalk_menu_counter == 3:
                scene bg porch with fade
            else:
                scene bg porch with fade
            show boruto cat at center with dissolve
            jump yoru_cattalk_menu_love

        







label yoru_repeatmodelling:
    hide screen camera_ui
    hide screen camera1280
    if yoru_picture_counter >= 5:
        label yoru_model_goodending:
        scene black with dissolve
        yo"*Exhales*..."
        show yorum_intro1 with dissolve:
            yalign 1.0
        show yorum_intro1:
            easein 5 yalign 0.0
        if yoruichi_relationship == "Obedient":
            yo"I think that should wrap up today's session..."
            bo"Today's session you say... Does that mean you'd be interested in more...?"
            yo"That's dependent on two things, [bo_name]..."
            yo"First, can you really make us money out of this or was that all a facade..."
            bo"Yoru, I-"
            show yorum_intro1 with Dissolve(0.3):
                    zoom 1.05 xalign 0.5 yalign 0.0
            yo"Shut up until I am finished!" with vpunch
            yo"Secondly..."
            call checkLust(80) from _call_checkLust_4
            menu:
                yo"Secondly..."
                "!" (secretlove = True) if percentage >= 80:
                    pass
                
                
            if percentage >=80:
                label replay_yoru_firstphotoshoot_footjob:
                $ initialize_replay_defaults()
                show yorum_intro1_shy with dissolve:
                    zoom 1.1 xalign 0.5 yalign 0.0 subpixel True
                show yorum_intro1_shy:
                    easein 12 yalign 0.7
                yo"Will you be able to conduct yourself like a gentleman...?"
                yo"Will you continue treating me with respect, and care...?"
                yo"Will I really be able to trust you...?"
                show yorum_intro1_shy with dissolve:
                    zoom 1.2 xalign 0.5 yalign 0.0 subpixel True
                yo"Because from what I can see..."
                show yorum_intro1_shy with dissolve:
                    zoom 1.4 xalign 0.5 yalign 0.0 subpixel True
                scene black
                yo"It seems you may be running into some... issues on that front!" with vpunch
                "Yoru raised her feet towards you and pointed them at something that seemed off to her..."
                show yoru_p1_footjob1 with dissolve
                yo"...Care to explain this?" with vpunch
                show yoru_p1_footjob1:
                    easein 0.7 yalign 0.05
                bot"S-shit! How the fuck did I not realize my..."
                show yoru_p1_footjob1:
                    easein 1 yalign 0.8
                bo"Y-yoru, I..." with vpunch
                bo"It's not what you think..."
                bo"R-remember what I said about-"
                show yoru_p1_footjob1:
                    easein 1 zoom 1.2 yalign 0.4 xalign 1.0
                yo"Your condition... right?" with vpunch
                show yoru_p1_footjob1:
                    easein 4 zoom 1.0 yalign 1.0 xalign 0.5
                yo"[bo_name]... Is that going to be a problem if we keep working together?"
                menu:
                    yo"[bo_name]... Is that going to be a problem if we keep working together?"
                    "No Ma'am!":
                        bo"No Ma'am! Believe me, I am trying my best, but-"
                    "{color=[dominancecolor]}It's not easy for me when you look as sexy as you do...{/color}":
                        bo"I am t-trying Yoru, believe me..."
                        yo"Hmm...?"
                        bo"it's not easy on me when you you look as beautiful as you do..."
                        scene black with dissolve
                        bo"When you are as sexy as you are..."
                        call changeDominance(1) from _call_changeDominance_73
                        "You lightly brushed your hand across her feet..."
                        yo"Careful now...!" with vpunch
                        "She carefully pushed her foot against your stomach, just enough to push you away and stop your hands from trailing her feet..."
                        bo"Didn't mean to startle you..."
                scene black with dissolve
                yo"Shut up, [bo_name]..." with vpunch
                yo"To be honest with you..."
                $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                bot"!" with vpunch
                show yoru_p1_footjob2_shy with dissolve:
                    xalign 0.0 yalign 1.0
                "She pulled down your pants with her feet, exposing your raging erection..."
                bo"Y-yoru?" with vpunch
                show yoru_p1_footjob2_shy:
                    easein 10 zoom 1.0 yalign 0.1 xalign 0.8
                yo"I thought that entire 'rare diagnosis' bullshit was just an excuse to justify your perverse ambitions..."
                yo"But little by little, I've come to realize that you aren't as dishonest as I thought you were..."
                yo"You aren't like the rest of your kind..."
                show yoru_p1_footjob1 with dissolve:
                    zoom 1.4 xalign 0.0 yalign 0.0
                bo"It wasn't a lie, Yoru..."
                scene yoru_p1_footjob2_shy with dissolve:
                    xalign 0.0 yalign 1.0
                bo"I've lost my self to my condition before. Even when I was around people I loved..."
                show yoru_p1_footjob2_shy:
                    easein 3 zoom 1.0 yalign 0.1 xalign 0.8
                bo"When that happens, I... I become worse than even the most vile of humans..."
                show yoru_p1_footjob2_shy at paizuri_ease
                $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 0.8)
                yo"So if I understand correctly, what you are saying is..."
                show yoru_p1_footjob2_shy at paizuri_ease
                "Yoru started reluctantly fiddling your cock with her feet..."
                bot"F-fuck... she is actually-" with vpunch
                yo"If this... is left untreated, you'll turn into just another piece of shit like the rest of your kind?"
                show yoru_p1_footjob2 with dissolve:
                    zoom 1.1 yalign 0.1 xalign 0.8
                yo"!" with vpunch
                bo"Y-you got that r-right..."
                call increaselust(20) from _call_increaselust_142
                "Yoru's light touch sent you over the edge. Your raging erection, caught even someone with her experience by surprise..."
                show yoru_p1_footjob2:
                    easein 5 zoom 1.0 yalign 0.8 xalign 0.1
                "But that didn't dissuade her..."
                yo"In that case..."
                yo"I am considering the possibility of h-helping you manage your... condition..."
                bo"Y-yoru-"
                scene yoru_p1_footjob2_shy with dissolve:
                    zoom 1.2 xalign 1.0 yalign 0.3
                yo"But!" with vpunch
                yo"You have to promise me, [bo_name]..."
                yo"You won't betray my trust... You won't be like the rest..."
                scene black with dissolve
                bo"...I p-promise..."
                yo"Then..."
                "She wrapped her legs around your waist and pulled you a little closer to her..."
                show yoru_p1_footjob3 with dissolve
                "Her toes were now firmly placed around your shaft, gripping it with just enough pressure for it to be pleasurable, but not painful..."
                show yoru_p1_footjob3 at paizuri_ease
                "She started working it with delicate, soft movements..."
                show yoru_p1_footjob3 at paizuri_ease
                yo"I don't mind occasionally helping out with your condition..."
                show yoru_p1_footjob3 at paizuri_ease
                bot"F-fuck! H-how is she so g-good at this..."
                show yoru_p1_footjob3 at paizuri_ease
                bot"Yoru... A shinigami... A real life god is working my cock with her feet, and it feels fucking amazing!"
                show yoru_p1_footjob3 at paizuri_ease
                yo"You have been nice to me, and you are trying to help, so..."
                yo"It's only fair I help you in return..."
                bo"Y-yoru, I...-" with flash
                show yoru_p1_footjob3:
                    easein 3 yalign 0.2
                yo"It seems your demeanor is not the only thing that differs from your kind's..."
                show yoru_p1_footjob3 at paizuri_ease
                yo"Your manhood seems to be... quite potent itself!"
                show yoru_p1_footjob3:
                    easein 3 yalign 1.0
                yo"It's not often a human lasts as long as you do with me..."
                show yoru_p1_footjob3 at paizuri_ease
                bot"I need to h-hold on a little bit longer!" with flash
                show yoru_p1_footjob3 at paizuri_ease
                yo"Mind if you got a little closer?"
                show yoru_p1_footjob3 at paizuri_ease
                yo"I wouldn't mind a better look at it..."
                scene black with vpunch
                bo"As you w-wish..."
                show yoru_p1_footjob4 with dissolve:
                    yalign 0.0
                show yoru_p1_footjob4:
                    easein 4 yalign 1.0
                yo"You can move in a little bit closer, I won't scratch you..."
                show yoru_p1_footjob4 with dissolve:
                    yalign 1.0
                show yoru_p1_footjob4_1 with dissolve:
                    yalign 1.0
                show yoru_p1_footjob4_1 at paizuri_ease
                bo"R-right..."
                yo"Good boy..." with vpunch
                menu yoru_photo_fjmenu:
                    yo"Good boy..."
                    "{color=[dominancecolor]}Start thrusting...{/color}":
                        call checkDominance(25,"yoru_photo_fjmenu") from _call_checkDominance_17
                        bo"Then you wouldn't mind if I..."
                        show yoru_photo_fj1 with dissolve
                        yo"Oh! I was... planning on taking care of it for you..."
                        bo"D-don't worry... You can rest for a while!"
                        show yoru_photo_fj2 with dissolve
                        $ renpy.sound.play("/audio/soun_fx/sexslapsslow1.opus", channel="sfx1", loop=False, relative_volume = 0.8)
                        call changeDominance(1) from _call_changeDominance_74
                        "You grabbed one of her feet and started thrusting with intent!" with vpunch
                        "Your thighs kept hitting against her own, making an audible 'Plap!' sound, whenever the two of you came in contact..."
                        bo"Wouldn't want to... t-tire you out, my sweet little kitten..."
                        yo"[bo_name]... Don't get the w-wrong idea..."
                        "Yoru seemed slightly annoyed by your initiative..."
                        yo"There's no satisfaction for me in this. I am only doing it f-for your own sake..."
                        scene black with vpunch
                        "She lightly kicked your abdomen away so that you would fall on your knees..."
                        yo"So sit back, and let me take care of it for you... alright?"



                    "Let her continue...":
                        bo"I am... c-close..."
                        yo"Don't worry, I'll take care of you..."
                        yo"I just had to take a better look at it first..."
                        show yoru_photo_fj1 with dissolve
                        "Absorbed in the pleasure of her feet's grip, you unconsciously started slowly thrusting..."
                        bo"Y-yoru... I-"
                        yo"It seems you are getting impatient, aren't you?"
                        scene black with vpunch
                        "She lightly kicked your abdomen away so that you would fall on your knees..."
                        yo"Sit back, and let me take care of it for you... alright?"
                                      
                show yoru_p1_footjob5 with dissolve:
                    zoom 1.23 yalign 1.0 xalign 1.0
                "You both fell back away from each other..."
                "Yoru was on her back, and you were on your knees..."
                yo"I was right to take a closer look at your manhood..."
                show yoru_p1_footjob5_1 with dissolve:
                    zoom 1.23 yalign 1.0 xalign 1.0
                scene yoru_p1_footjob5 with dissolve:
                    zoom 1.23 yalign 1.0 xalign 1.0
                show yoru_p1_footjob5 at paizuri_ease
                yo"It's quite pretty, really..."
                show yoru_photo_fj_f1 with dissolve:
                    zoom 1.23 yalign 1.0 xalign 1.0
                "Her feet gripped your cock in a way that clearly conveyed her intentions..."
                "She was ready for your release... She wanted you to have it..."
                bot"F-fuck! She's gonna make me..." with flash
                scene black with dissolve
                yo"But [bo_name]..."
                show yoru_p1_footjobpre5:
                    alpha 0.3 xalign 0.5 yalign 0.0
                show yoru_p1_footjobpre5:
                    linear 2 alpha 1.0
                with dissolve
                show yoru_p1_footjob5 with Dissolve(1):
                    xalign 0.5 yalign 0.0
                $ renpy.sound.play("/audio/soun_fx/femalemast1.opus", channel="sfx3", loop=False, relative_volume = 1.4)
                yo"Let me be clear on one thing..."
                bot"!" with vpunch
                bot"S-she... Is she t-touching herself?" with vpunch
                show screen parallax1280("yoru_photo_fj_f1") with dissolve
                call showscrollingimage from _call_showscrollingimage_75
                yo"I told you before that us Shinigami, find very little to sex..."
                yo"When one lives for thousands of years, sex quickly becomes meaningless, boring even. It ends up being something you do occasionally as a distraction..."
                yo"Make no m-mistake..."
                yo"I will be helping you manage your condition at times, but..."
                $ renpy.sound.play("/audio/soun_fx/femalemast2.opus", channel="sfx2", loop=False, relative_volume = 1.4)
                yo"I am not interested in bedding with you..." with flash
                yo"Am I making myself clear?"
                bot"T-then why is she..." with flash
                $ renpy.sound.play("/audio/soun_fx/femalemastmoan1.opus", channel="sfx3", loop=False, relative_volume = 1.4)
                yo"There will be...*Moans*...no penetrative sex involved, you understand?"
                "Yoru made her intentions clear to you..."
                bot"I can't e-even process the words she's saying... I.. I am about to!" with flash
                "...Or so she thought. Your mind was submerged in the ecstatic feeling that was culminating inside you..."
                bo"Y-yoru...! *Moans*" with flash
                scene yoru_p1_footjob5_2
                call hidescrollingimage("Click twice to cum") from _call_hidescrollingimage_76
                $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                bo"I am c-cumming! *Moans*" with flash
                $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                show yoru_p1_footjob5_3 with flash:
                    yalign 0.9
                pause 0.5
                $ renpy.sound.play("/audio/soun_fx/cum2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                show yoru_p1_footjob5_3 with flash:
                    yalign 0.0
                pause 0.5
                $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                show yoru_p1_footjob5_3 with flash:
                    yalign 0.5
                call decreaselust(100) from _call_decreaselust_87
                show screen parallax1280("yoru_p1_footjob5_3") with flash
                call showscrollingimage from _call_showscrollingimage_76
                yo"*Moans* Ahh..."
                $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                bo"*Panting...*"
                show yoru_p1_footjob5_3
                call hidescrollingimage from _call_hidescrollingimage_77
                "Yoru seemed to be caught in the moment. She kept touching herself through her clothing, even after being covered in your semen..."
                show yoru_p1_footjob5_3 with dissolve:
                    zoom 1.2 xalign 0.5 yalign 0.7
                "Her juices would even flow down and through her tight clothing..."
                "It was clear she was finding enjoyment in what just transpired, despite her previous statement."
                "It wasn't long before she caught herself in the act and immediately, her demeanor changed..."
                scene black with vpunch
                yo"F-fuck! W-what am I doing!" with vpunch
                bo"Y-yoru...?"
                yo"What even is all of this, [bo_name]..."
                bo"I am sorry, it just... shot out-"
                yo"Ugh! This distinct human smell, stuck on my precious clothes... This gunk of yours is disgusting!" with vpunch
                $ renpy.sound.play("/audio/soun_fx/transform.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                show yorum_intro2 with flash
                show yorum_intro2:
                    easein 5 yalign 0.2
                yo"You are lucky I can get rid of it with my reiatsu..."
                yo"W-what are you standing there looking at me like that. Dress up! I have to get going..."
                bo"Can we... t-talk first?"
                yo"*Sigh..."
                yo"I knew you'd get the wrong idea..."
                yo"I told you already, [bo_name]..."
                yo"There won't be anything more than an equivalent exchange between the two of us, understand?"
                yo"I MAY keep helping, if you keep being... the way you are..."
                bo"Then why were you-"
                $ renpy.sound.play("/audio/soun_fx/transform.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                show blackscreen with flash
                hide yoruc
                scene bg modelling
                show boruto surprised2 at left
                show yoru cat2t behind boruto:
                    zoom 0.25 xpos 930 ypos 532
                hide blackscreen with dissolve
                $ renpy.sound.play("/audio/soun_fx/meow1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                yo"*Angry meow!*" with vpunch
                show boruto snob with dissolve
                
                bo"...Touching yourself?"
                $ renpy.sound.play("/audio/soun_fx/meow2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                yo"*Confused Meow?*"
                bot"She was! W-wasn't she?"
                bo"."
                yo".."
                bo"..."
                $ renpy.sound.play("/audio/soun_fx/hiss.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                yo"*Angry meow!*" with vpunch
                bo"The hell you Meowing at me for, you crazy cat lady!"
                yo"Hurry up and take me outside! I have to get back to Obo's before he becomes suspicious..." with vpunch
                yo"And I am not about to have any more conversation with your relatives... or you!"
                show yoru:
                    easeout 0.7 xpos 300
                pause 0.3
                hide yoru
                show boruto cat
                with fade
                yo"You try anything and I'll claw your neck off!" with vpunch
                bo"Will you relax, what even happened to you..."
                $ renpy.sound.play("/audio/soun_fx/meow1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                yo"*Furious meow!*" with vpunch
                show boruto:
                    easein 1 xpos 1500
                bo"Fine, Fine... I get it!"
                $ renpy.sound.play("/audio/soun_fx/dooropen.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                scene black with dissolve
                "You quietly escorted Yoru downstairs, but..."
                him"[bo_name_stutter]! Wait a second..." with vpunch
                show bg lr_day with dissolve:
                    zoom 0.68
                show boruto cat at left with dissolve
                $ renpy.sound.play("/audio/soun_fx/meow2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                yo"Damn it! *Annoyed Meow!*" with dissolve
                show hima worried2 at right with dissolve:
                    zoom 0.34
                bo"What do you want, [him_name]..."
                him"Did your friend already leave? I thought I'd get a chance to talk with her..."
                show hima surprised with dissolve
                show hima:
                    easein 0.5 xalign 0.5
                him"Wait a second..."
                scene black with vpunch
                him"*Gasps!*"
                show himapet1 with dissolve
                $ renpy.sound.play("/audio/soun_fx/meow2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                him"Is that-" with vpunch
                yo"*Concerned M-meow?*"
                him"Awwww! A fluffy little kitty cat! Who's the cute little guy on your shoulder!" with vpunch
                menu:
                    him"Awwww! A fluffy little kitty cat! Who's the cute little guy on your shoulder!"
                    "Just a stray I am caring for...":
                        bo"Just a stray kitty I am caring for..."
                        bo"I was just about to take her outside..."
                        call changeRespect("Himawari",2) from _call_changeRespect_176
                        him"Aww, how unlike you! Can I please pet her?"
                        show himapet2 with dissolve
                    "It's Yoru!":
                        bo"Oh this little kitty? It's Yoru of course..."
                        $ renpy.sound.play("/audio/soun_fx/hiss.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                        yo"*Angry Meow!*" with vpunch
                        him"...Huh?"
                        bo"*Nervous laughter* Heh-eh... Just a silly joke!"
                        him"What kind of stupid joke is that, you dummy! Even the kitty knows better than that..."
                        him"Look at her, such a little cutie! Can I pet her please?"
                        show himapet2 with dissolve
                him"Pretty pleaaaase... Here kitty, kitty!"
                $ renpy.sound.play("/audio/soun_fx/hiss.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                scene black with vpunch
                yo"*Menacing M-meow!*" with vpunch
                show bg lr_day:
                    zoom 0.68
                show boruto cat at left
                show hima mad at right:
                    zoom 0.34
                with dissolve
                him"W-what the hell is wrong with your kitty... She's so feral!"
                bo"Yeah, well... I am working on it. She'll be tamed soon enough!"
                $ renpy.sound.play("/audio/soun_fx/meow2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                yo"*Confused Meow?*" with vpunch
                bo"In any case, Yoru left a while ago, and I gotta go too!"
                show boruto:
                    easein 1 xpos -1000
                bo"See ya later!"
                him"Hmph!"
                scene black with dissolve
                "You bring Yoru to your porch as requested..."
                scene bg porch
                show boruto cat at center
                with dissolve
                bo"There you go..."
                bo"Will you be able to make it there on your own? What if your form breaks before you get there..."
                yo"I'll figure it out myself!" with vpunch
                yo"But... thanks for the offer."
                scene blackscreen with vpunch
                "She pounced off your shoulder..."
                scene bg porch
                show boruto surprised2
                with dissolve
                yo"I'll... see you soon?"
                bo"Of course..."
                $ renpy.sound.play("/audio/soun_fx/meow1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                "She started strolling away with happy little hops..."
                show boruto snob with dissolve
                if not _in_replay:
                    if quest.exists("bohim_2"):
                        if quest.is_state("3_bohim_2", "in progress"):
                            $ notification("Quest objective completed")
                            $ quest.change_quest_title("3_bohim_2",f"Purchase a camera and convince Yoru to help you")
                            $ quest.change_quest_title("4_bohim_2",f"Have your first session with {him_name}")
                            $ quest.check("3_bohim_2", "completed")
                            $ quest.check("4_bohim_2", "in progress")
                bot"That went... well!"
                bot"Pretty sure that if I can find a way to make money out of this..."
                bot"Our relationship will only grow more intimate..."
                show boruto embarassed with dissolve
                bot"How the hell did I even pull this off with someone like her..."
                bot"*Nervous chuckle* Heh-eh!"
                $ renpy.end_replay()
                default yoruichi_unlock_obedient_interactions = False
                $ yoruichi_unlock_obedient_interactions = True

                default yoruichi_modelling_love_complete = False
                $ yoruichi_modelling_love_complete = True
                jump action_taken

            

            else:
                show yorum_intro1_shy with dissolve:
                    zoom 1.1 xalign 0.5 yalign 0.0 subpixel True
                show yorum_intro1_shy:
                    easein 8 yalign 0.7
                $ yoruichi_modelling_love_complete = True
                yo"Will you be able to conduct yourself like a gentleman...?"
                yo"Will you continue treating me with respect, and care...?"
                yo"Will I really be able to trust you...?"
                show yorum_intro1_shy with dissolve:
                    yalign 0.1
                yo"I don't want this to turn into something more than work, [bo_name]..."
                yo"Do you understand what I am saying...?"
                bo"I... think so?"

                show yorum_intro2 with dissolve
                show yorum_intro2:
                    easein 5 yalign 0.2
                bo"But this was fun, wasn't it?"
                yo"*Sigh..."
                yo"...M-maybe a little bit!"
                bo"I am glad! Then let's do it aga-"
                $ renpy.sound.play("/audio/soun_fx/transform.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                show blackscreen with flash
                hide yoruc
                scene bg modelling
                show boruto surprised2 at left
                show yoru cat2t behind boruto:
                    zoom 0.25 xpos 930 ypos 532
                hide blackscreen with dissolve
                $ renpy.sound.play("/audio/soun_fx/meow1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                yo"*Angry meow!*" with vpunch
                bo"W-what's that for..."
                $ renpy.sound.play("/audio/soun_fx/meow2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                yo"*Meow!*" with vpunch
                show boruto snob with dissolve
                bo"I don't speak Cat-annese, you crazy cat lady!"
                $ renpy.sound.play("/audio/soun_fx/hiss.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                yo"*Angry meow!*" with vpunch
                show boruto embarassed with dissolve
                bo"I get it, I get it...It was a joke!"
                yo"Hurry up and take me outside! I have to get back to Obo's before he becomes suspicious..." with vpunch
                yo"And I am not about to have any more conversation with your relatives... or you!"
                show yoru:
                    easeout 0.7 xpos 300
                pause 0.3
                hide yoru
                show boruto cat
                with fade
                yo"You try anything and I'll claw your neck off!" with vpunch
                bo"Will you relax, what even happened to you..."
                $ renpy.sound.play("/audio/soun_fx/meow1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                yo"*Furious meow!*" with vpunch
                show boruto:
                    easein 1 xpos 1500
                bo"Fine, Fine... I get it!"
                $ renpy.sound.play("/audio/soun_fx/dooropen.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                scene black with dissolve
                "You quietly escorted Yoru downstairs, but..."
                him"[bo_name_stutter]! Wait a second..." with vpunch
                show bg lr_day with dissolve:
                    zoom 0.68
                show boruto cat at left with dissolve
                $ renpy.sound.play("/audio/soun_fx/meow2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                yo"Damn it! *Annoyed Meow!*" with dissolve
                show hima worried2 at right with dissolve:
                    zoom 0.34
                bo"What do you want, [him_name]..."
                him"Did your friend already leave? I thought I'd get a chance to talk with her..."
                show hima surprised with dissolve
                show hima:
                    easein 0.5 xalign 0.5
                him"Wait a second..."
                scene black with vpunch
                him"*Gasps!*"
                show himapet1 with dissolve
                $ renpy.sound.play("/audio/soun_fx/meow2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                him"Is that-" with vpunch
                yo"*Concerned M-meow?*"
                him"Awwww! A fluffy little kitty cat! Who's the cute little guy on your shoulder!" with vpunch
                menu:
                    him"Awwww! A fluffy little kitty cat! Who's the cute little guy on your shoulder!"
                    "Just a stray I am caring for...":
                        bo"Just a stray kitty I am caring for..."
                        bo"I was just about to take her outside..."
                        call changeRespect("Himawari",2) from _call_changeRespect_177
                        him"Aww, how unlike you! Can I please pet her?"
                        show himapet2 with dissolve
                    "It's Yoru!":
                        bo"Oh this little kitty? It's Yoru of course..."
                        $ renpy.sound.play("/audio/soun_fx/hiss.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                        yo"*Angry Meow!*" with vpunch
                        him"...Huh?"
                        bo"*Nervous laughter* Heh-eh... Just a silly joke!"
                        him"What kind of stupid joke is that, you dummy! Even the kitty knows better than that..."
                        him"Look at her, such a little cutie! Can I pet her please?"
                        show himapet2 with dissolve
                him"Pretty pleaaaase... Here kitty, kitty!"
                $ renpy.sound.play("/audio/soun_fx/hiss.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                scene black with vpunch
                yo"*Menacing M-meow!*" with vpunch
                show bg lr_day:
                    zoom 0.68
                show boruto cat at left
                show hima mad at right:
                    zoom 0.34
                with dissolve
                him"W-what the hell is wrong with your kitty... She's so feral!"
                bo"Yeah, well... I am working on it. She'll be tamed soon enough!"
                $ renpy.sound.play("/audio/soun_fx/meow2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                yo"*Confused Meow?*" with vpunch
                bo"In any case, Yoru left a while ago, and I gotta go too!"
                show boruto:
                    easein 1 xpos -1000
                bo"See ya later!"
                him"Hmph!"
                scene black with dissolve
                "You bring Yoru to your porch as requested..."
                scene bg porch
                show boruto cat at center
                with dissolve
                bo"There you go..."
                bo"Will you be able to make it there on your own? What if your form breaks before you get there..."
                yo"I'll figure it out myself!" with vpunch
                yo"But... thanks for the offer."
                scene blackscreen with vpunch
                "She pounced off your shoulder..."
                scene bg porch
                show boruto surprised2
                with dissolve
                yo"I'll... see you soon?"
                bo"Of course..."
                $ renpy.sound.play("/audio/soun_fx/meow1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                "She started strolling away in happy little hops..."
                show boruto snob with dissolve
                if not _in_replay:
                    if quest.exists("bohim_2"):
                        if quest.is_state("3_bohim_2", "in progress"):
                            $ notification("Quest objective completed")
                            $ quest.change_quest_title("3_bohim_2",f"Purchase a camera and convince Yoru to help you")
                            $ quest.change_quest_title("4_bohim_2",f"Have your first session with {him_name}")
                            $ quest.check("3_bohim_2", "completed")
                            $ quest.check("4_bohim_2", "in progress")
                bot"That went... well!"
                bot"Pretty sure that if I can find a way to make money out of this..."
                bot"Our relationship may grow in more... interesting ways!"
                $ renpy.end_replay()
                jump action_taken



        else:
            yo"I've had enough of this..."
            bo"Come on, one last shot perhaps? Things were just starting to get interesting..."
            yo"You've already had enough shots, [bo_name]..."
            yo"We've made a deal, remember? Besides, I am getting tired from all the posing..."
            bo"We made a deal now, did we..."
        show yorum_intro1_surprised with dissolve:
            yalign 0.0 zoom 1.1 xalign 0.5
        "Yoru's eyes darted downwards towards something and in an instant, she turned peach-red in complete surprise..." with vpunch
        yo"Ki-... [bo_name_stutter], how long have you-"
        scene black with vpunch
        bo"Oh, did this startle you?" with vpunch
        scene bg modelling
        show boruto bonerevil at left
        with dissolve
        bo"I told you about my condition, remember?"
        show yoruc annoyed at right with dissolve
        bo"Can't exactly blame me when my model looks as sexy as you do!"
        yo"I am not interested in seeing your little willy pop up whenever we work together..."
        show yoruc:
            easein 2 xpos 1600 ypos 740
        pause 1
        show yoru_rear_sexy1_2 with dissolve:
            yalign 0.5
        show yoru_rear_sexy1_2:
            easein 3 yalign 0.1
        yo"You better find a way to be dealing with your urges if we are to continue working together!"
        show yoru_rear_sexy1_2 with dissolve:
            yalign 0.9
        bot" You should be happy I am maintaining composure you bitch!"
        bot"I don't even know why I am being nice with her..."
        bot"I am pretty sure her powers are long gone, combined with what I know about her, maybe..."
        menu yoru_photo_h_goodending:
            bot"I am pretty sure her powers are long gone, combined with what I know about her, maybe..."
            "{color=[hatredcolor]}Blackmail her!{/color}":
                if v17_update == True:
                    pass
                else:
                    $ notification("Exclusive supporters scene")


                call checkHatred(30,"yoru_photo_h_goodending") from _call_checkHatred_16
                
                bot"Fuck this bitch! Who does she think she is to make demands of me..."
                show yoru_rear_sexy1_2:
                    easein 0.5 yalign 0.1
                yo"Did you hear me, kid? You better be in control of your urges..." with vpunch
                bo"Oh I heard you alright, you little roaring kitty..."
                bo"Unfortunately for you, your demands have been..."
                scene black with vpunch
                bo"Rejected!" with vpunch
                show yoru_photo_h_end1 with dissolve
                "You lunged on her! Holding on to her hips as tight as you could..."
                show yoru_photo_h_end1 with dissolve:
                    easein 4 yalign 0.1
                yo"What the hell do you think you are doing kid!"
                bo"What do you think I am doing, you-" with vpunch
                if is_opportunity_unlocked("l1_opportunity3", strength):
                    pass
                else:
                    default yoru_fail_blackmail = False
                    $ yoru_fail_blackmail = True
                    show yoru_photo_h_end1:
                        easein 0.5 yalign 0.9
                    yo"Kid..." with vpunch
                    bot"Oh s-shit! Where is her s-strength coming from!" with vpunch
                    "In a sudden display of power, Yoru pushed against your tight grip..."
                    show yoru_photo_h_end1:
                        easein 0.5 yalign 0.1
                    yo"How brazen must one be to put his hands on a Shinigami like this..."
                    bot"F-fuck, she is way too strong!" with vpunch
                    yo"You really are..."
                    scene black with vpunch
                    yo"Out of your fucking mind... You damned brat!" 
                    jump yoru_badending
                show yoru_photo_h_end1:
                    easein 0.5 yalign 0.9
                bo"Oh...? Where is this strength coming from, Yoru..." with vpunch
                show yoru_photo_h_end1:
                    easein 0.5 yalign 0.1
                yo"A-are you forgetting you are messing with a Shinigami, you damned brat..."
                bo"It would seem to me, that a Shinigami is being outmatched by a mere human..."
                yo"D-don't push your luck, kid..."
                bo"In fact, I would bet that the shinigami in question might even be almost entirely powerless..."
                yo"I am simply holding back, kid..."
                yo"I may still spare you a life of suffering and disease if you take your hands off me..."
                bo"So benevolent of you..."
                scene black with dissolve
                bo"Alright then, there... "
                bo"I might have gotten carried away..."
                "You let go..."
                show yoru_rear_sexy1 with dissolve:
                    yalign 0.0
                show yoru_rear_sexy1:
                    easein 2 yalign 1.0
                yo"As stupid as you are, it would seem your brain is at least functional..."
                "Yoru patted her thighs clean while facing away from you..."
                $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                "You took the chance to get rid of your clothes..."
                bo"My brain is indeed functional, which is why..."
                scene black with vpunch
                yo"*Gasp*!" with vpunch
                show yoru_photo_h_end2 with dissolve:
                    yalign 1.0
                bo"I am betting this pretentious act of yours is just a shitty bluff!" with vpunch
                show yoru_photo_h_end2:
                    easein 2 yalign 0.0
                bo"Tell me I am wrong..."
                show screen parallax1280("yoru_photo_h_end2",1)
                call showscrollingimage from _call_showscrollingimage_77
                show screen hidescreen1280button
                with dissolve
                scene bg modelling
                show yoru_photo_h_end2t:
                    zoom 0.6 xalign 0.5 yalign 0.5
                yo"Kid, are you insane?" with vpunch
                yo"I'll give you one final chance to save yourself from certain death!" with vpunch
                bo"One final chance, you say...?"
                yo"..."
                bo"How about I..."
                hide screen parallax1280
                show screen parallax1280("yoru_photo_h_end3",1,0.3)
                show screen hidescreen1280button
                with dissolve
                scene bg modelling
                show yoru_photo_h_end3t:
                    zoom 0.6 xalign 0.5 yalign 0.5
                bo"Give you a final chance instead to admit this is all a facade!" with vpunch
                "You assertively moved one of your hands to her breasts..."
                yo"..."
                bo"Care to explain how your transformation only holds for a few minutes at best...?"
                yo"."
                hide screen parallax1280
                show screen parallax1280("yoru_photo_h_end4",1,0.3)
                show screen hidescreen1280button
                with dissolve
                scene bg modelling
                show yoru_photo_h_end4t:
                    zoom 0.6 xalign 0.5 yalign 0.5
                bo"Care to explain how Obo has such a strong hold over you?" with vpunch
                yo".."
                bo"Have you no words, little kitty?"
                yo"..."
                yo"...Y-you are right, you piece of shit!" with vpunch
                yo"I am not what I used to be. I lied to p-protect myself... H-happy now?"
                hide screen parallax1280
                show screen parallax1280("yoru_photo_h_end5",1,0.3)
                show screen hidescreen1280button
                with dissolve
                scene bg modelling
                show yoru_photo_h_end5t:
                    zoom 0.6 xalign 0.5 yalign 0.5
                bo"There it is... What is that hard to admit?" with vpunch
                yo"Don't just push your thing between my thighs, you damned brat!" with vpunch
                hide screen parallax1280
                show screen parallax1280("yoru_photo_h_end4",1,0.3)
                show screen hidescreen1280button
                with dissolve
                scene bg modelling
                show yoru_photo_h_end4t:
                    zoom 0.6 xalign 0.5 yalign 0.5
                bo"You say that, but...It seems to me your nipples are almost piercing through your clothes, Yoru..."
                bo"Are you trying to hide something else from me?"
                hide screen parallax1280
                show screen parallax1280("yoru_photo_h_end5",1,1.0)
                show screen hidescreen1280button
                with dissolve
                scene bg modelling
                show yoru_photo_h_end5t:
                    zoom 0.6 xalign 0.5 yalign 0.5
                bo"Are you perhaps enjoying this, you dirty little kitty cat..." with vpunch
                "You made a sudden, powerful thrust, bringing most of your shaft through her thighs, now brushing against her crotch..."
                yo"Like I would ever, you creep..."
                "Yoru had no other choice but to give in to your primitive demands..."
                "You held her hip with one hand, and groped her breast with another while thrusting your fully erect cock in between her thighs..."
                "By now, she knew she was severely disadvantaged. Instead of trying to intimidate you, she resorted to protecting her erogenous zones instead..."
                bo"You did say sex means nothing to you Shinigami, given how you live as long as you do..."
                bo"It seems to me, you are either lying about that too!"
                bo"And even if it does mean nothing to you, then I don't see why you'd have issue with arranging a little exchange between us..." with vpunch
                hide screen parallax1280
                show screen parallax1280("yoru_photo_thighjob",1,1.0,True)
                show screen hidescreen1280button
                with dissolve
                scene bg modelling
                show yoru_photo_thighjobt:
                    zoom 0.6 xalign 0.5 yalign 0.5
                yo"An e-exchange? What are you talking about, kid! S-stop moving so harshly you little runt!"
                bo"An exchange, yes!" with vpunch
                bo"I'll consider the possibility of helping you make some money and escape Obo's clutches, but in exchange..."
                bo"You'll assist me in managing my condition... You remember about that, don't you?"
                yo"T-that's absurd, kid! You are p-practically coercing me into this!"
                bo"I am offering you your freedom, in exchange for something you claim means nothing to you..."
                bo"I think that's more than fair, isn't it?"
                yo"You are being unreasonable. Your condition is messing with your head!"
                show yoru_photo_thighjob2:
                    yalign 1.0
                hide screen hidescreen1280button
                with dissolve
                bo"Then keep it shut and help me manage it!" with vpunch
                yo"*Groans* Ugh...Ah..I am not going to allow you to use me whenever you have a flare up, kid!"
                bo"Yoru... My sweet, little kitty cat. With a body like this..."
                bo"I am thinking modelling might not be your calling after all..."
                bo"Hips as wide as yours, a perfectly flat and toned stomach, a chest as firm and easily aroused as yours..."
                bo"A whore is what I should turn you into, not a model!"
                yo"D-deplorable! I will never whore myself out, especially for someone like you..."
                menu:
                    yo"D-deplorable! I will never whore myself out, especially for someone like you..."
                    "{color=[hatredcolor]}You were made to be used!{/color}":
                        bo"Everything about you begs for people to use you..."
                        bo"The way you dress, your long-gone powers, your defiant demeanor, but more importantly..."
                        call changeHatred(1) from _call_changeHatred_129
                        bo"Your whore-like body, you were made to be used, Yoru!" with vpunch
                        yo"E-enough of this!" with vpunch
                        pass
                    "We'll see about that...":
                        bo"We'll see about that..."
                        pass
                    "{color=[dominancecolor]}You are already my whore!{/color}":
                        bo"Oh don't you worry Yoru..."
                        hide screen parallax1280
                        hide scrollingimage onlayer screens
                        label replay_yoru_firstphotoshoot_blackmail:
                        $ initialize_replay_defaults()
                        scene black
                        with vpunch
                        yo"*Gasps*!"
                        bo"I wasn't planning on whoring you out anyway..."
                        show screen parallax1280("yoru_photo_behind1_1",1,0.7) with dissolve
                        "You turned her around so she could face you when you said..."
                        hide screen parallax1280
                        show screen parallax1280("yoru_photo_behind1_1",1,0.0)
                        with dissolve
                        bo"Because I want you to be my whore, and my whore only!" with vpunch
                        yo"That... will never happen either!" with vpunch
                        hide screen parallax1280
                        show yoru_photo_thighjob_behind:
                            yalign 0.85
                        with dissolve
                        bo"As much as you say that, your thighs are gripping me so hard, Yoru..."
                        bo"I can even feel your perky nipples rubbing against my chest even..."
                        bo"I could make this much more interesting for you, you know..."
                        yo"I will n-never do anything like that w-with you!" with vpunch
                        show yoru_photo_thighjob_behind2 with dissolve:
                            yalign 0.85
                        "You started thrusting even faster!"
                        bo"T-then..."
                        bo"M-me and you will have to s-settle..." with flash
                        $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                        show yoru_photo_behind1_2 with flash:
                            yalign 0.85
                        bo"W-with this!"
                        $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                        show yoru_photo_behind1_3 with longerflash:
                            yalign 0.85
                        call decreaselust(100) from _call_decreaselust_88
                        bo"Aah-ugh! *Loud Moans*..."
                        yo"Did you just..."
                        bo"*Panting*... I feel, much better now..."
                        bo"Thanks for help-"
                        scene black with vpunch
                        yo"H-helping!? You forced me into it you animalistic runt..." with vpunch
                        bo"Eh, sometimes my condition takes hold of me..."
                        bo"It wasn't a big deal anyway, it's not like I... you know..."
                        bo"There was no penetration involved!"
                        $ renpy.sound.play("/audio/soun_fx/transform.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                        scene bg bb day
                        show boruto snob at left
                        show yoruc annoyed at right
                        with flash
                        yo"You are lucky I can remove this spunk of yours from my skin with my powers..."
                        bo"Cool trick, but..."
                        show boruto:
                            easein 1 xalign 0.5
                        bo"Let me remind you that you are the lucky one here..."
                        show boruto:
                            easein 1 xalign 0.7
                        bo"You keep being a good little kitty, and I'll keep being nice to you..."
                        scene black with vpunch
                        yo"You are out of your mind, kid!"
                        default yoru_success_blackmail = False
                        $ yoru_success_blackmail = True
                        jump yoru_badending
                bo"As much as you are trying to hide it..."
                bo"All this time, your thighs have been squeezing me so sensually, with such force..."
                bo"I can even feel your sensitive nipples poking against my fingers..."
                bo"Even down there..."
                bo"Is that dampness I am feeling every time I thrust my cock against your womanhood?"
                yo"Y-you are insane kid. You are imagining things!" with vpunch
                hide screen parallax1280
                show screen parallax1280("yoru_photo_h_end_cum1",1,0.0,False)
                show screen hidescreen1280button
                with dissolve
                scene bg modelling
                show yoru_photo_h_end_cum1t:
                    zoom 0.6 xalign 0.5 yalign 0.5
                bo"Whatever the case..."
                bo"I am c-certainly not imagining..." with flash
                bo"How Incredible it f-feels to be fucking your t-thighs!" with flash
                hide screen parallax1280
                hide screen camera1280
                hide screen camera_ui
                hide scrollingimage onlayer screens
                with dissolve
                "You take one final thrust before..."
                
                scene bg modelling
                show yoru_photo_h_end4t:
                    zoom 0.6 xalign 0.5 yalign 0.5
                with dissolve
                scene bg modelling
                show yoru_photo_h_end_cum1t:
                    zoom 0.6 xalign 0.5 yalign 0.5
                with dissolve
                show yoru_photo_h_end_cum1t at paizuri_ease
                pause 0.3
                $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                scene bg modelling
                show yoru_photo_h_end_cum1_2t with flash:
                    zoom 0.6 xalign 0.5 yalign 0.5
                bo"*Loud Moans* Aaarh!" with flash
                bo"I..."
                $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                show yoru_photo_h_end_cum1_1t with longerflash:
                    zoom 0.6 xalign 0.5 yalign 0.5
                call decreaselust(100) from _call_decreaselust_89
                bo"...Did I imagine this too? *Panting*"
                bo"*Panting*... I feel, much better now..."
                bo"Thanks for help-"
                scene black with vpunch
                "She pushed you away..."
                yo"H-helping!? You forced me into it you animalistic runt..." with vpunch
                bo"Eh, sometimes my condition takes hold of me..."
                bo"It wasn't a big deal anyway, it's not like I... you know..."
                bo"There was no penetration involved!"
                $ renpy.sound.play("/audio/soun_fx/transform.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                scene bg bb day
                show boruto snob at left
                show yoruc annoyed at right
                with flash
                yo"You are lucky I can remove this spunk of yours from my skin with my powers..."
                bo"Cool trick, but..."
                show boruto:
                    easein 1 xalign 0.5
                bo"Let me remind you that you are the lucky one here..."
                show boruto:
                    easein 1 xalign 0.7
                bo"You keep being a good little kitty, and I'll keep being nice to you..."
                scene black with vpunch
                yo"You are out of your mind, kid!"
                $ yoru_success_blackmail = True
                jump yoru_badending
                



                
            "{color=[dominancecolor]}Speaking of deals...{/color}":
                show yoru_rear_sexy1_2:
                    easein 0.5 yalign 0.1
                yo"Did you hear me, kid? You better be in control of your urges..." with vpunch
                bo"Oh I am, Yoru..."
                scene black with vpunch
                bo"For the most part..." with vpunch
                show yoru_photo_h_end1 with dissolve
                "You palced your hands on her hips and whispered in her ear..."
                show yoru_photo_h_end1 with dissolve:
                    easein 4 yalign 0.1
                bo"Speaking of deals..."
                yo"Kid, careful what you say next..."
                bo"I don't recall our agreement being so one-sided..."
                bo"You know, I'd be much more willing to uphold our deal if you offered something in return..."
                yo"...And what would that something be?"
                bot"She must know what I am talking about..."
                call checkDominance(25,"yoru_badending") from _call_checkDominance_18
                label replay_yoru_firstphotoshoot_dominance:
                $ initialize_replay_defaults()
                bo"That would be..."
                show screen parallax1280("yoru_photo_h_end1",1,1.0)
                call showscrollingimage from _call_showscrollingimage_78
                show screen hidescreen1280button
                with dissolve
                scene bg modelling
                show yoru_photo_h_end1t:
                    zoom 0.6 xalign 0.5 yalign 0.5
                bo"You of course! Along with your compliance..."
                yo"[bo_name], your wording is... concerning!"
                yo"Are you really trying to help me? Or are you just looking for something from me..."
                bo"Both can be true at the same time, Yoru..."
                bo"I do have your best interests in mind..."
                bo"But I also have a fundamental need to manage my condition..."
                hide screen parallax1280
                show screen parallax1280("yoru_photo_h_end2",1,0.3)
                show screen hidescreen1280button
                with dissolve
                scene bg modelling
                show yoru_photo_h_end2t:
                    zoom 0.6 xalign 0.5 yalign 0.
                bo"...And for you to be the one to help me with that!"
                yo"*Gasp!*"
                yo"[bo_name]!? You cannot be serious..." with vpunch
                yo"You want me to... help you with that?" with vpunch
                yo"Kid, you are messing with a Shinigami..." with vpunch
                yo"..."
                bo"Come on, Yoru! Enough of the Shinigami charade..."
                hide screen parallax1280
                show screen parallax1280("yoru_photo_h_end3",1,0.3)
                show screen hidescreen1280button
                with dissolve
                scene bg modelling
                show yoru_photo_h_end3t:
                    zoom 0.6 xalign 0.5 yalign 0.5
                bo"I already know your secrets..." with vpunch
                "You assertively moved one of your hands to her breasts..."
                yo"..."
                bo"Care to explain how your transformation only holds for a few minutes at best...?"
                yo"."
                hide screen parallax1280
                show screen parallax1280("yoru_photo_h_end4",1,0.3)
                show screen hidescreen1280button
                with dissolve
                scene bg modelling
                show yoru_photo_h_end4t:
                    zoom 0.6 xalign 0.5 yalign 0.5
                bo"Care to explain how Obo has such a strong hold over you?" with vpunch
                yo".."
                bo"In truth, you don't have to... Because I already know!"
                bo"You are powerless, Yoru..."
                yo"..."
                bo"Don't worry, I don't plan on using that against you..."
                bot"Yet..."
                yo"Y-you are right, I am not what I used to be. I lied to p-protect myself... H-happy now?"
                hide screen parallax1280
                show screen parallax1280("yoru_photo_h_end5",1,0.3)
                show screen hidescreen1280button
                with dissolve
                scene bg modelling
                show yoru_photo_h_end5t:
                    zoom 0.6 xalign 0.5 yalign 0.5
                bo"You don't have to protect yourself from me..."
                bo"Not if you help me manage my condition that is!"
                yo"Don't just push your thing between my thighs! It's... disgusting!" with vpunch
                hide screen parallax1280
                show screen parallax1280("yoru_photo_h_end4",1,0.3)
                show screen hidescreen1280button
                with dissolve
                scene bg modelling
                show yoru_photo_h_end4t:
                    zoom 0.6 xalign 0.5 yalign 0.5
                bo"You say that, but...It seems to me your nipples are almost piercing through your clothes, Yoru..."
                bo"Are you hiding something else from me?"
                hide screen parallax1280
                show screen parallax1280("yoru_photo_h_end5",1,1.0)
                show screen hidescreen1280button
                with dissolve
                scene bg modelling
                show yoru_photo_h_end5t:
                    zoom 0.6 xalign 0.5 yalign 0.5
                bo"Are you perhaps enjoying this, you dirty little kitty cat..." with vpunch
                "You made a sudden, powerful thrust, brining most of your shaft through her thighs, now brushing against her crotch..."
                yo"Like I would ever enjoy something like this..."
                "Yoru gave in to your primitive advances..."
                "You held her hip with one hand, and groped her breast with another while thrusting your fully erect cock in between her thighs..."
                bo"You did say sex means nothing to you Shinigami, given how you live as long as you do..."
                bo"What if we made it mean something between the two of us..."
                bo"A tool to bolster our partnership..."
                bo"A method from which we can both get what we ultimately want!"
                hide screen parallax1280
                show screen parallax1280("yoru_photo_thighjob",1,1.0,True)
                show screen hidescreen1280button
                with dissolve
                scene bg modelling
                show yoru_photo_thighjobt:
                    zoom 0.6 xalign 0.5 yalign 0.5
                bo"You get an autonomous life, free from Obo and away from a shitty society that shunned you..."
                yo"What are you talking about, kid! S-stop moving so harshly you little..."
                bo"All I ask for, is your devotion to me..."
                yo"If only you weren't such a piece of s-shit..."
                yo"M-maybe then, I could consider this psychotic offer of y-yours..."
                bo"As much as you are trying to hide it..."
                bo"All this time, your thighs have been squeezing me so sensually, with such force..."
                bo"I can even feel your sensitive nipples poking against my fingers..."
                bo"Even down there..."
                bo"Is that dampness I am feeling every time I thrust my cock against your womanhood?"
                yo"Y-you are just imagining things..." with vpunch
                hide screen parallax1280
                show screen parallax1280("yoru_photo_h_end_cum1",1,0.0,False)
                show screen hidescreen1280button
                with dissolve
                scene bg modelling
                show yoru_photo_h_end_cum1t:
                    zoom 0.6 xalign 0.5 yalign 0.5
                bo"Whatever the case..."
                bo"I am c-certainly not imagining..." with flash
                bo"How Incredible it f-feels to be fucking your t-thighs!" with flash
                hide screen parallax1280
                hide screen camera1280
                hide screen camera_ui
                hide scrollingimage onlayer screens
                with dissolve
                "You take one final thrust before..."
                scene bg modelling
                show yoru_photo_h_end4t:
                    zoom 0.6 xalign 0.5 yalign 0.5
                with dissolve
                scene bg modelling
                show yoru_photo_h_end_cum1t:
                    zoom 0.6 xalign 0.5 yalign 0.5
                with dissolve
                show yoru_photo_h_end_cum1t at paizuri_ease
                pause 0.3
                $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                scene bg modelling
                show yoru_photo_h_end_cum1_2t with flash:
                    zoom 0.6 xalign 0.5 yalign 0.5
                bo"*Loud Moans* Aaarh!" with flash
                bo"I..."
                $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                show yoru_photo_h_end_cum1_1t with longerflash:
                    zoom 0.6 xalign 0.5 yalign 0.5
                call decreaselust(100) from _call_decreaselust_90
                bo"...Did I imagine this too? *Panting*"
                bo"*Panting*... I feel, much better now..."
                bo"Thanks for help-"
                scene black with vpunch
                "She pushed you away..."
                yo"That wasn't me h-helping. It was just you taking what you want..." with vpunch
                bo"You'll have to forgive me. Sometimes my condition takes hold of me..."
                bo"It wasn't a big deal anyway, it's not like I... you know..."
                bo"There was no penetration involved..."
                $ renpy.sound.play("/audio/soun_fx/transform.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                scene bg bb day
                show boruto snob at left
                show yoruc annoyed at right
                with flash
                yo"You are lucky I can remove this spunk of yours from my skin with my powers..."
                bo"Cool trick, but..."
                show boruto:
                    easein 1 xalign 0.5
                bo"Let me remind you that you are the lucky one here..."
                show boruto:
                    easein 1 xalign 0.7
                bo"You keep being a good little kitty, and I'll keep being nice to you..."
                scene black with vpunch
                yo"You are out of your mind, kid!"
                $ yoru_success_blackmail = True
                jump yoru_badending








            "I can control myself...":
                show yoru_rear_sexy1_2:
                    easein 0.5 yalign 0.1
                yo"Did you hear me, kid? You better be in control of your urges..." with vpunch
                bot"Then again, she is a god after all..."
                bo"You are right. Don't worry, I can control myself..."
                bo"For the most part!"
                yo"Hmph! You better, or else..."
                hide screen camera_ui
                hide screen parallax1280
                hide screen camera1280
                scene bg bb day
                show boruto angry2 at left
                show yoruc annoyed at right
                show blackscreen with vpunch
                jump yoru_model_neutralending
        
        "fill"
        jump action_taken
            



        
        
    scene yoru_modelstart:
        yalign 0.1
    with dissolve
    menu yoru_model_repeatable_menu:
        yo"...What next?"
        "Frontal shots":
            if yoru_frontal_dynamic == True and yoru_frontal_confident == True and yoru_frontal_sexy == True:
                "No more frontal shots available..."
                jump yoru_model_repeatable_menu
            bo"How about another frontal shot..."
            show yoru_frontalstart:
                yalign 1.0 xalign 0.5
            with dissolve
            show yoru_frontalstart:
                easein 2 yalign 0.0
            yo"Sure..."
            bo"But this time..."
            menu:
                bo"But this time..."
                "Strike a dynamic pose..." if yoru_frontal_dynamic == False:
                    $ yoru_frontal_dynamic = True
                    bo"I want you to strike a dynamic pose!"
                    bo"Given your current attire, let's compliment your body's features with a combat pose..."
                    bo"Plenty of movement, muscle flexing, and a daring look... think you can pull that off?"
                    show yoru_frontal_dynamicpose with dissolve:
                        yalign 1.0
                    show yoru_frontal_dynamicpose:
                        easein 2 yalign 0.0
                    yo"Something like..."
                    yo"...This?"
                    show screen camera1280("yoru_frontal_dynamicpose") with dissolve
                    show screen camera_ui("Yoruichi",False) with dissolve
                    bo"You are a natural, Yoru!"
                    bo"Now hold that pose for me, and..."
                    show screen camera_ui("Yoruichi",True) with dissolve
                    $ ui.interact()
                    show screen camera_ui("Yoruichi",False) with dissolve
                    bo"Excellent..."
                    show screen camera1280("yoru_frontalstart") with dissolve
                    yo"Another one down..."

                "Strike a confident pose..." if yoru_frontal_confident == False:
                    $ yoru_frontal_confident = True
                    bo"Let's have you pose in a confident manner. Flick your hair, and stare straight into the lens with a serious expression..."
                    show yoru_frontal_confidentpose with dissolve:
                        yalign 1.0
                    show yoru_frontal_confidentpose:
                        easein 2 yalign 0.0
                    yo"Something like..."
                    yo"...This?"
                    show screen camera1280("yoru_frontal_confidentpose") with dissolve
                    show screen camera_ui("Yoruichi",False) with dissolve
                    bo"You are a natural, Yoru!"
                    bo"Now hold that pose for me, and..."
                    show screen camera_ui("Yoruichi",True) with dissolve
                    $ ui.interact()
                    show screen camera_ui("Yoruichi",False) with dissolve
                    bo"Excellent..."
                    show screen camera1280("yoru_frontalstart") with dissolve
                    yo"Another one down..."

                "How about a sexy pose!" if yoru_frontal_sexy == False and yoru_heels_on == True:
                    default yoru_frontal_sexy = False
                    $ yoru_frontal_sexy = True
                    bo"Let's try something a little bit more interesting..."
                    bo"You are doing great already, but..."
                    if yoruichi_relationship == "Obedient":
                        bo"You need to be willing to capture some of your inherent beauty in... particular ways, if we are to make some serious money out of this..."
                        yo"I can already tell where this is going..."
                        bo"Will you be... comfortable doing those type of shots, you think?"
                        yo"Your kind is so laughably simple-minded..."
                    else:
                        bo"We won't be getting anywhere if you aren't willing to sell what the people really want..."
                        yo"I can already tell where this is going..."
                        bo"Can you know..."
                        yo"Your kind is so laughably simple-minded..."
                    show yoru_frontal_sexypose with dissolve:
                        yalign 1.0
                    show yoru_frontal_sexypose:
                        easein 2 yalign 0.0
                    if yoruichi_relationship == "Obedient":
                        yo"But because I trust you... I wouldn't mind a few of these shots. For now at least..."
                    else:
                        yo"It's almost sad, really..."
                    show screen camera1280("yoru_frontal_sexypose") with dissolve
                    show screen camera_ui("Yoruichi",False) with dissolve
                    if yoruichi_relationship == "Obedient":
                        bo"I appreciate you saying that..."
                        yo"That you are simple-minded? *Giggles*"
                        bo"That you trust me, you sly kitten..."
                        yo"Shut up... Come on then, take a 'sexy' picture of me..."
                        bo"It's true... We are simple-minded, and sex sells!"
                        bo"So I say, why not take advantage of that!"
                    else:
                        yo"But if this is going to be my ticket out of here, then I don't mind a few of these shots."
                        yo"Come on then, take a 'sexy' picture of me..."
                        bo"It's true... We are simple-minded, and sex sells!"
                        bo"So I say, why not take advantage of that!"
                    bo"Ready, and..."
                    menu:
                        bo"Ready, and..."
                        "Maybe a smile would be more fitting...":
                            bo"Actually, think you can try putting on a seductive smile for this one?"
                            show screen camera1280("yoru_frontal_sexypose_smile") with fade
                            yo"I can try..."
                            bo"Perfect! Ready, and..."
                        "Take the shot as is...":
                            pass
                        
                    show screen camera_ui("Yoruichi",True) with dissolve
                    $ ui.interact()
                    show screen camera_ui("Yoruichi",False) with dissolve
                    bo"Got it! This one may fetch a high price..."
                    show screen camera1280("yoru_frontalstart") with dissolve
                    yo"Another one down..."
                "How about a sexy pose! (Barefoot)" if yoru_heels_on == False and yoru_frontal_sexy_barefoot == False:
                    default yoru_frontal_sexy_barefoot = False
                    $ yoru_frontal_sexy_barefoot = True
                    if yoru_frontal_sexy == False and yoru_rear_sexy == False:
                        bo"Let's try something a little bit more interesting..."
                        bo"You are doing great already, but..."
                        if yoruichi_relationship == "Obedient":
                            bo"You need to be willing to capture some of your inherent beauty in... particular ways, if we are to make some serious money out of this..."
                            yo"I can already tell where this is going..."
                            bo"Will you be... comfortable doing those type of shots, you think?"
                            yo"Your kind is so laughably simple-minded..."
                        else:
                            bo"We won't be getting anywhere if you aren't willing to sell what the people really want..."
                            yo"I can already tell where this is going..."
                            bo"Can you know..."
                            yo"Your kind is so laughably simple-minded..."
                    else:
                        bo"Let's try another sexy pose, but this time without your heels on..."
                        show yoru_frontal_sexy_barefoot with dissolve:
                            yalign 1.0
                        yo"Do people really buy this stuff?"  
                        show yoru_frontal_sexy_barefoot:
                            easein 2 yalign 0.0
                        bo"You have no idea!"
                        show screen camera1280("yoru_frontal_sexy_barefoot") with dissolve
                        bo"Ready, and..."
                        show screen camera_ui("Yoruichi",True) with dissolve
                        $ ui.interact()
                        show screen camera_ui("Yoruichi",False) with dissolve
                        bo"Got it! This one may fetch a high price..."
                        yo"Another one down..."
                        $ yoru_picture_counter += 1
                        jump yoru_repeatmodelling
                    show yoru_frontal_sexy_barefoot with dissolve:
                        yalign 1.0
                    show yoru_frontal_sexy_barefoot:
                        easein 2 yalign 0.0
                    if yoruichi_relationship == "Obedient":
                        yo"But because I trust you... I wouldn't mind a few of these shots. For now at least..."
                    else:
                        yo"It's almost sad, really..."
                    show screen camera1280("yoru_frontal_sexypose") with dissolve
                    show screen camera_ui("Yoruichi",False) with dissolve
                    if yoruichi_relationship == "Obedient":
                        bo"I appreciate you saying that..."
                        yo"That you are simple-minded? *Giggles*"
                        bo"That you trust me, you sly kitten..."
                        yo"Shut up... Come on then, take a 'sexy' picture of me..."
                        bo"It's true... We are simple-minded, and sex sells!"
                        bo"So I say, why not take advantage of that!"
                    else:
                        yo"But if this is going to be my ticket out of here, then I don't mind a few of these shots."
                        yo"Come on then, take a 'sexy' picture of me..."
                        bo"It's true... We are simple-minded, and sex sells!"
                        bo"So I say, why not take advantage of that!"
                    bo"Ready, and..."
                    menu:
                        bo"Ready, and..."
                        "Maybe a smile would be more fitting...":
                            bo"Actually, think you can try putting on a seductive smile for this one?"
                            show screen camera1280("yoru_frontal_sexypose_smile") with fade
                            yo"I can try..."
                            bo"Perfect! Ready, and..."
                        "Take the shot as is...":
                            pass
                        
                    show screen camera_ui("Yoruichi",True) with dissolve
                    $ ui.interact()
                    show screen camera_ui("Yoruichi",False) with dissolve
                    bo"Got it! This one may fetch a high price..."
                    show screen camera1280("yoru_frontalstart") with dissolve
                    yo"Another one down..."


            $ yoru_picture_counter += 1
            jump yoru_repeatmodelling
        "Rear shots":
            bo"How about a rear shot next..."
            show yoru_rearstart:
                yalign 0.0 xalign 0.5
            with dissolve
            show yoru_rearstart:
                easein 2 yalign 1.0
            yo"The rear, huh? Now what?"
            bot"The ass on this woman..."
            show screen camera1280("yoru_rearstart") with dissolve
            show screen camera_ui("Yoruichi",False) with dissolve
            menu:
                yo"Now what?"
                "Stay exactly as you are..." if yoru_rear_stay == False:
                    $ yoru_rear_stay = True
                    bo"You know what? I think you might have accidentally struck perfection..."
                    yo"I... did?"
                    bo"Stay exactly as you are..."
                    bo"We are going to turn this into a medium shot instead..."
                    bo"And..."
                    show screen camera_ui("Yoruichi",True) with dissolve
                    $ ui.interact()
                    show screen camera_ui("Yoruichi",False) with dissolve
                    bo"I knew you were a natural..."
                    show screen camera1280("yoru_rearstart") with dissolve
                    yo"Another one down..."

                "Strike a dynamic pose..." if yoru_rear_dynamic == False:
                    $ yoru_rear_dynamic = True
                    bo"Now you strike a pose!"
                    bo"Given your current attire, let's compliment your body's features with a dynamic combat pose..."
                    bo"Plenty of movement, muscle flexing, and a daring look... think you can pull that off?"
                    hide screen camera1280
                    hide screen camera_ui
                    with dissolve
                    show yoru_rear_dynamic with dissolve:
                        yalign 1.0
                    show yoru_rear_dynamic:
                        easein 2 yalign 0.0
                    yo"Something like..."
                    yo"...This?"
                    show screen camera1280("yoru_rear_dynamic") with dissolve
                    show screen camera_ui("Yoruichi",False) with dissolve
                    bo"You are a natural, Yoru!"
                    bo"Now hold that pose for me, and..."
                    show screen camera_ui("Yoruichi",True) with dissolve
                    $ ui.interact()
                    show screen camera_ui("Yoruichi",False) with dissolve
                    bo"Excellent..."
                    show screen camera1280("yoru_rearstart") with dissolve
                    yo"Another one down..."

                "Strike a confident pose..." if yoru_rear_confident == False:
                    $ yoru_rear_confident = True
                    bo"Now you strike a pose!"
                    bo"Let's have you pose in a confident manner. Imagine this scenario..."
                    bo"Someone's calling out your name and you are looking over your shoulder to check who it is..."
                    bo"Your look pierces through whoever called out with its brimming confidence..."
                    bo"Think you can do that?"
                    hide screen camera1280
                    hide screen camera_ui
                    with dissolve
                    show yoru_rear_casual with dissolve:
                        yalign 1.0
                    show yoru_rear_casual:
                        easein 2 yalign 0.0
                    yo"Something like..."
                    yo"...This?"
                    show screen camera1280("yoru_rear_casual") with dissolve
                    show screen camera_ui("Yoruichi",False) with dissolve
                    bo"You are a natural, Yoru!"
                    bo"Now hold that pose for me, and..."
                    show screen camera_ui("Yoruichi",True) with dissolve
                    $ ui.interact()
                    show screen camera_ui("Yoruichi",False) with dissolve
                    bo"Excellent..."
                    show screen camera1280("yoru_rearstart") with dissolve
                    yo"Another one down..."
                "Strike a sexy pose!" if yoru_rear_sexy == False and yoru_heels_on == True:
                    default yoru_rear_sexy = False
                    hide camera1280
                    hide camera_ui
                    with dissolve
                    if yoru_frontal_sexy == False and yoru_rear_sexy == False:
                        bo"Let's try something a little bit more interesting..."
                        bo"You are doing great already, but..."
                        bo"We won't be getting anywhere if you aren't willing to sell what the people really want..."
                        yo"I can already tell where this is going..."
                        bo"Can you know..."
                        yo"Your kind is so laughably simple-minded..."
                        $ yoru_rear_sexy = True
                    else:
                        bo"Let's try another sexy pose..."
                    scene yoru_rear_sexy0 with dissolve:
                        yalign 1.0
                    yo"Do people really buy this stuff?"  
                    show yoru_rear_sexy0:
                        easein 2 yalign 0.0
                    bo"You have no idea!"
  
                    show screen camera1280("yoru_rear_sexy0") with dissolve
                    show screen camera_ui("Yoruichi",False) with dissolve
                    if yoru_frontal_sexy == False and yoru_rear_sexy == False:
                        yo"But if this is going to be my ticket out of here, then I don't mind a few of these shots."
                        yo"Come on then, take a 'sexy' picture of me..."
                        bo"It's true... We are simple-minded, and sex sells!"
                        bo"So I say, why not take advantage of that!!"
                    bo"Ready, and..."
                    menu:
                        bo"Ready, and..."
                        "Actually, maybe we should emphasize your... assets better!" if yoruichi_relationship == "Unwillingly Obedient":
                            bo"Actually, let's turn this into a medium shot instead..."

                            show screen camera1280("yoru_rear_sexy1") with dissolve
                            yo"Huh? Aren't you getting a bit too close...?"
                            bo"Come on Yoru. Give the people what they want..."
                            bo"Make your posterior stick out a little bit more!"
                            show screen camera1280("yoru_rear_sexy1_1") with dissolve
                            yo"*Groans* You people..."
                            bo"Perfect! Ready, and..."

                        "...!" if yoruichi_relationship == "Obedient":
                            bo"."
                            bo".."
                            bo"..."
                            yo"...Something wrong, [bo_name]?" with vpunch
                            bo"No, I-"
                            show screen camera1280("yoru_rear_cute") with dissolve
                            yo"Were you looking for some more... flair? *Giggles*" with vpunch
                            bo"N-not particularly... But this pose will do!"
                            yo"I am sure it will!"
                            yo"Come on, take the shot. You won't get another chance like this..."
                            bo"Will do! Ready, and..."
                        "Take the shot as is...":
                            pass
                        
                    show screen camera_ui("Yoruichi",True) with dissolve
                    $ ui.interact()
                    show screen camera_ui("Yoruichi",False) with dissolve
                    bo"Got it! This one may fetch a high price..."
                    show screen camera1280("yoru_rearstart") with dissolve
                    yo"Another one down..."

                "Strike a sexy pose! (Barefoot)" if yoru_rear_sexy_barefoot == False and yoru_heels_on == False:
                    default yoru_rear_sexy_barefoot = False
                    $ yoru_rear_sexy_barefoot = True
                    hide screen camera1280
                    hide screen camera_ui
                    with dissolve
                    if yoru_frontal_sexy == False and yoru_rear_sexy == False:
                        bo"Let's try something a little bit more interesting..."
                        bo"You are doing great already, but..."
                        bo"We won't be getting anywhere if you aren't willing to sell what the people really want..."
                        yo"I can already tell where this is going..."
                        bo"Can you know..."
                        yo"Your kind is so laughably simple-minded..."
                    else:
                        bo"Let's try another sexy pose, but this time without your heels on..."
                    scene yoru_rear_sexy_barefoot with dissolve:
                        yalign 1.0
                    yo"Do people really buy this stuff?"  
                    show yoru_rear_sexy_barefoot:
                        easein 2 yalign 0.0
                    bo"You have no idea!"
                    # show screen camera1280("yoru_rear_sexy0") with dissolve
                    # bo"Ready, and..."
                    # show screen camera_ui("Yoruichi",True) with dissolve
                    # $ ui.interact()
                    # show screen camera_ui("Yoruichi",False) with dissolve
                    # bo"Got it! This one may fetch a high price..."
                    # yo"Another one down..."    
                    # show yoru_rear_sexy0 with dissolve:
                    #     yalign 1.0
                    # show yoru_rear_sexy0:
                    #     easein 2 yalign 0.0
                    # yo"It's almost sad, really..."
                    show screen camera1280("yoru_rear_sexy_barefoot") with dissolve
                    show screen camera_ui("Yoruichi",False) with dissolve
                    if yoru_frontal_sexy == False and yoru_rear_sexy == False:
                        yo"But if this is going to be my ticket out of here, then I don't mind a few of these shots."
                        yo"Come on then, take a 'sexy' picture of me..."
                        bo"It's true... We are simple-minded, and sex sells!"
                        bo"So I say, why not take advantage of that!!"
                    bo"Ready, and..."
                    menu:
                        bo"Ready, and..."
                        "Actually, maybe we should emphasize your... assets better!":
                            bo"Actually, let's turn this into a medium shot instead..."

                            show screen camera1280("yoru_rear_sexy1") with dissolve
                            yo"Huh? Aren't you getting a bit too close...?"
                            bo"Come on Yoru. Give the people what they want..."
                            bo"Make your posterior stick out a little bit more!"
                            show screen camera1280("yoru_rear_sexy1_1") with dissolve
                            yo"*Groans* You people..."
                            bo"Perfect! Ready, and..."
                        "Take the shot as is...":
                            pass
                        
                    show screen camera_ui("Yoruichi",True) with dissolve
                    $ ui.interact()
                    show screen camera_ui("Yoruichi",False) with dissolve
                    bo"Got it! This one may fetch a high price..."
                    show screen camera1280("yoru_rearstart") with dissolve
                    yo"Another one down..."

            $ yoru_picture_counter += 1
            jump yoru_repeatmodelling
        "Get down on all fours...(Barefoot)" if yoru_picture_counter>=2 and yoru_heels_on == False:
            bo"I think it's time we try something else..."
            show yoru_rearstart:
                yalign 0.0 xalign 0.5
            with dissolve
            show yoru_rearstart:
                easein 2 yalign 1.0
            if yoru_knees_firsttime == False:
                if yoruichi_relationship == "Obedient":
                    yo"It is? I am curious what you came up with this time!"
                    yo"To be honest, I am kind of getting into this whole modelling thing..."
                    bo"I am glad you are enjoying yourself. Then, how about this..."
                    bo"Let's combine the two things you seem to be enjoying!"
                    yo"I am liking the sound of that!"
                    bo"I am thinking the feline look really suits you..."
                    bo"What would you say about a few shots in that stance? Think you can get down on your knees for this next one?"
                else:
                    yo"I am not sure I am liking the tone of your voice, [bo_name]..."
                    yo"What is it exactly that you are thinking..."
                    bo"I am thinking the feline look really suits you..."
                    bo"Think you can get down on your knees for this next one?"
                show yoru_rearstart:
                    easein 0.5 yalign 0.1
                if yoruichi_relationship == "Obedient":
                    yo"You want me to... get down on my knees?"
                    bo"Sure do. I think we can get a few great shots mimicking that feline look of yours..."
                    yo"Hmm..."
                else:
                    yo"My knees!?" with vpunch 
                    bo"Something wrong with that?"
                $ yoru_knees_firsttime = True
            else:
                bo"Think you can get on your knees again?"
                show yoru_rearstart:
                    easein 0.5 yalign 0.1
                if yoruichi_relationship == "Obedient":
                    yo"*Meow!* *Giggles* Just kidding, let's do it..."
                else:
                    yo"*Groans* Ugh..." with vpunch
                    yo"Fine... As long as you don't ask for anything weird!"

            show screen camera1280("yoru_knees_start_barefoot",1,1.0) with dissolve
            show screen camera_ui("Yoruichi",False) with dissolve
            yo"This doesn't feel too bad without the heels on, but..."
            yo"...Careful what you ask for next!"
            menu:
                yo"...Careful what you ask for next!"
                "Can you lie on your stomach for me?" if yoru_knees_stomach == False:
                    default yoru_knees_stomach = False
                    $ yoru_knees_stomach = True
                    bo"Let's make you comfortable then!"
                    bo"Think you can lie on your stomach and raise your feet behind your back?"
                    show screen camera1280("yoru_knees_stomach",1,0.5) with dissolve
                    yo"Will this do?"
                    bo"I knew you are a natural Yoru..."
                    if yoruichi_relationship == "Obedient":
                        yo"I am? I am just following your directions..."
                        bo"You really are!"
                    else:
                        yo"Just... Shut up and take the shot!"
                        bo"And..."
                    show screen camera_ui("Yoruichi",True) with dissolve
                    $ ui.interact()
                    show screen camera_ui("Yoruichi",False) with dissolve
                    yo"Not sure if I can get used to this..."
                    bo"You are doing great, and you are looking even better!"
                    yo"..."
                    yo"Ugh... Can I get off the floor now?"
                "Can you lie on your side for me?" if yoru_knees_side == False:
                    default yoru_knees_side = False
                    $ yoru_knees_side = True
                    bo"Let's make you comfortable then..."
                    bo"Think you can lie on your side while bracing yourself with both arms on the floor?"
                    bo"Look back toward the lens with a defiant look..."
                    show screen camera1280("yoru_knees_side1",1,0.5) with dissolve
                    yo"A defiant look?"
                    bo"Stay exactly as you are..."
                    if yoruichi_relationship == "Obedient":
                        bo"I think you look beautiful just as you are... Like an angry feral cougar!"
                        yo"S-stop it, you... Hurry up and take the shot!"
                        bo"Hehe! Just a silly joke..."
                        bo"And..."
                    else:
                        bo"I think your resting bitch face is practically perfect for this one..."
                        yo"Just... Shut up and take the shot!"
                        bo"Hehe! Just a silly joke..."
                        bo"And..."
                    show screen camera_ui("Yoruichi",True) with dissolve
                    $ ui.interact()
                    show screen camera_ui("Yoruichi",False) with dissolve
                    bo"This one came out nicely!"
                    yo"Good, can I get up now?"

                "Let's try a feline pose!" if yoru_knees_feline == False:
                    default yoru_knees_feline = False
                    $ yoru_knees_feline = True

                    if yoruichi_relationship == "Obedient":
                        bo"I think you'll enjoy this next one..."
                        yo"...Meaning?"
                        bo"Think you can get on all fours? Just like a feline would?"
                        yo"..."
                    else:
                        bo"I wanna see you in your natural stance Yoru..."
                        yo"...That being?"
                        bo"On all fours of course, just like a feline! You seemed to be enjoying that part of being a cat..."
                        yo"Damn it kid..."
                    show screen camera1280("yoru_knees_feline",1,1.0) with dissolve
                    if yoruichi_relationship == "Obedient":
                        $ renpy.sound.play("/audio/soun_fx/meow1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                        yo"*Meow* As you wish, director [bo_name]!"
                        bot"...! Is she... toying with me?" with vpunch
                        yo"*Giggles* Did that startle you?"
                        bo"N-not really... Although I do enjoy your total compliance..."
                        yo"Enjoying my compliance now, are you...?"
                        bo"Sure do. Especially when you look as beautiful as you do sitting there like a tamed little kitty would..."
                        yo"Hmph!" with vpunch
                    else:
                        yo"I could do without your snide remarks..." with vpunch
                        bo"I am just saying, you are quite literally in your element..."
                        bo"You look even better like that!"
                        yo"Your compliments mean nothing to me, hurry up and take the shot..."
                    label yoru_felinepose:
                    show screen camera1280("yoru_knees_feline",1,1.0) with dissolve
                    menu:
                        yo"Your compliments mean nothing to me, hurry up and take the shot..."
                        "Don't mind if I do!": 
                            pass
                        "How about a... pouncing pose!":
                            bo"Before that, think you can pull off a more aggressive pose?"
                            bo"Extend one of your legs backwards and pretend like you are about to pounce on someone!"
                            show screen camera1280("yoru_knees_feline2",1,1.0) with dissolve
                            yo"Something like this?"
                            menu:
                                yo"Something like this?"
                                "Perfect! And...":
                                    pass
                                "I changed my mind...":
                                    bo"You look great and all, but I think I changed my mind. Let's go back to your initial pose..."
                                    jump yoru_felinepose
                                

                        "How about a... sexy cougar pose!":
                            bo"Before that, think you can pull off a sexy cougar pose?"
                            if yoruichi_relationship == "Obedient":
                                yo"A w-what now? Are you having trouble staying grounded, [bo_name]?"
                                bo"I am serious Yoru... You know you have it in you. That feral, sexy image that could kill with its looks alone..."
                                bo"Think you can bring that out for me?"
                                yo"..."
                            else:
                                yo"What the hell even is that, [bo_name]..."
                                bo"Come on, you know you are sexy! Just bring that out confidently..."
                            show screen camera1280("yoru_knees_feline3",1,1.0) with dissolve
                            yo"You know I am uncomfortable doing this..."
                            bo"You better get comfortable then, because you look fucking sublime!"
                            yo"Just, shut up and take the shot already!"
                            menu:
                                yo"Just, shut up and take the shot already!"
                                "Perfect! And...":
                                    pass
                                "I changed my mind...":
                                    bo"You look incredible, but I think I changed my mind. Let's go back to your initial pose..."
                                    jump yoru_felinepose
                    bo"Perfect! And..."
                    show screen camera_ui("Yoruichi",True) with dissolve
                    $ ui.interact()
                    show screen camera_ui("Yoruichi",False) with dissolve
                    bo"What a snap..."
                    yo"Can I get up now...?"

                "Let's try to emphasize your (ass)ets!" if yoru_knees_ass == False:
                    default yoru_knees_ass = False
                    $ yoru_knees_ass = True
                    bo"Let's try to emphasize your strong features Yoru..."
                    yo"Strong features? How exactly do we do that..."
                    bo"Keep your back arched, lean forward and place your arms in between your legs..."
                    show screen camera1280("yoru_knees_ass1",1,1.0)
                    with dissolve
                    if yoruichi_relationship == "Obedient":
                        yo"Is there a reason you circled all the way behind me?"
                        bo"You should already know the answer to that, Yoru..."
                        yo"*Sigh*... If this idea of yours doesn't work out..." with vpunch
                        bo"Yoru... There's precisely zero chance this fails!"
                        bo"Not with you looking as sexy, and being as adhering as you are!"
                    else:
                        yo"Why are you circling around me kid..."
                        bo"Don't worry about me. You stay exactly as you are and I'll handle the rest... Hehe!"
                        yo"Hey! Where  are you focusing that camera at!" with vpunch
                        bo"I am just giving the people what they want..."
                    yo"Good grief! Just... take the shot already!" with vpunch
                    menu:
                        yo"Good grief! Just... take the shot already!"
                        "Don't mind if I do!":
                            bo"Don't mind if I do!"
                            pass
                        "...!" if yoruichi_relationship == "Obedient":
                            bot"I can't believe Yoru's letting me get this... close to her!"
                            bot"She even seems to be enjoying posing for me..."
                            bot"I wonder if she-"
                            yo"H-hey, Is there something wrong?" with vpunch
                            bo"No! I was just..."
                            show screen camera1280("yoru_knees_ass2",1,1.0) with dissolve
                            "Yoru raised her posterior and got a little bit closer to the lens to give you a better shot..." with vpunch
                            bo"Y-yoru?" with vpunch
                            yo"I know what this is about... you are too shy to ask for a close-up, aren't you?"
                            bo"Not what I was t-thinking, but..."
                            yo"Enough talking! Hurry up and take the shot..." with vpunch
                    bo"And..."
                    show screen camera_ui("Yoruichi",True) with dissolve
                    $ ui.interact()
                    show screen camera_ui("Yoruichi",False) with dissolve
                    show screen camera1280("yoru_knees_ass3",1,1.0) with dissolve
                    if yoruichi_relationship == "Obedient":
                        yo"I feel... d-dirty even posing for a shot like that..."
                        bo"I mean, I didn't exactly ask you too..."
                        yo"S-shut up..." with vpunch
                        bo"R-right..."
                        bot"Heh! Women... Mortals or gods makes no difference. Both are equally as confusing and undecided..."
                        yo"Can I get up now...?"
                        bo"Sure..."
                    else:

                        yo"Damn it, kid! If you think I'll let this devolve into you taking creepy shots of me, then you are in for a rude awakening..."
                        yo"You aren't too far off from Obo's treatment of me..."
                        bo"Don't compare me to the likes of him, Yoru..."
                        bo"I am doing this for the both of us..."
                        yo"Hmph! Sure you are..."
                        bo"You'll change your tune when the money starts rolling in..."
                        bo"Perhaps I'll keep most of it for myself seeing how you aren't too willing to cooperate!"
                        yo"S-shut up... I am doing my best!" with vpunch
                        yo"Can I get up now...?"
                "Let's try a traditional Seiza posture..." if yoru_knees_seiza == False:
                    default yoru_knees_seiza = False
                    $ yoru_knees_seiza = True
                    bo"Let's try a traditional Seiza posture next..."
                    yo"A Seiza, huh..."
                    show screen camera1280("yoru_knees",1,1.0) with dissolve
                    yo"A surprisingly reasonable request for once..."
                    yo"Will this do?"
                    menu yoruseizamenu:
                        yo"Will this do?"
                        "It will do!":
                            bo"Don't mind if I do!"
                            pass
                        "A nice pose, but it can get even better!":
                            bo"Your posing ability is surprisingly good Yoru. But..."
                            bo"There's much more to modeling than using your body alone!"
                            yo"...Meaning?"
                            hide screen camera1280
                            hide screen camera_ui
                            scene black with dissolve
                            bo"Let's try having you pose over here by the window..."
                            bo"The natural sun-light will highlight your side-profile while casting a shadow that enhances the aesthetics of this shot tenfolds!"
                            show screen camera1280("yoru_knees_1",1,1.0) with dissolve
                            bo"Try raising your arm as if you were trying to block the sunlight from reaching your face..."
                            show screen camera_ui("Yoruichi",False) with dissolve
                            yo"Like... this?"
                            bo"Exactly like that..."
                            yo"You are finally sounding like you know a thing or two, [bo_name]..."
                            bo"And you are finally starting to look like a real model yourself..."
                            bo"We keep this up and who knows, maybe we'll actually make something out of this, Yoru!"
                            yo"Maybe so... Now hurry up and take the shot!" with vpunch
                            
                        "A bit too casual to leave an impression...":
                            bo"Hmm... I am thinking it's a bit too casual to leave an impression."
                            yo"What do you suggest I do then..."
                            bo"Think you can spread your legs a little further apart? Drop your posterior down on the floor and raise your arms up to your head, as if you were adjusting your ponytail..."
                            show screen camera1280("yoru_knees_2",1,1.0) with dissolve
                            yo"Not quite a Seiza pose then, is it?" with vpunch
                            bo"Maybe so, but defenitely more aesthetically pleasing!"
                            yo"*Sigh*... Hurry up and take the shot!"
                    bo"Ready, and..."
                    show screen camera_ui("Yoruichi",True) with dissolve
                    $ ui.interact()
                    show screen camera_ui("Yoruichi",False) with dissolve
                    yo"Can I get up now...?"


            $ yoru_picture_counter += 1
            jump yoru_repeatmodelling
        "Get down on all fours..." if yoru_picture_counter>=2 and yoru_heels_on == True:
            bo"I think it's time we try something else..."
            show yoru_rearstart:
                yalign 0.0 xalign 0.5
            with dissolve
            show yoru_rearstart:
                easein 2 yalign 1.0
            default yoru_knees_firsttime = False
            if yoru_knees_firsttime == False:
                if yoruichi_relationship == "Obedient":
                    yo"It is? I am curious what you came up with this time!"
                    yo"To be honest, I am kind of getting into this whole modelling thing..."
                    bo"I am glad you are enjoying yourself. Then, how about this..."
                    bo"Let's combine the two things you seem to be enjoying!"
                    yo"I am liking the sound of that!"
                    bo"I am thinking the feline look really suits you..."
                    bo"What would you say about a few shots in that stance? Think you can get down on your knees for this next one?"
                else:
                    yo"I am not sure I am liking the tone of your voice, [bo_name]..."
                    yo"What is it exactly that you are thinking..."
                    bo"I am thinking the feline look really suits you..."
                    bo"Think you can get down on your knees for this next one?"
                show yoru_rearstart:
                    easein 0.5 yalign 0.1
                if yoruichi_relationship == "Obedient":
                    yo"You want me to... get down on my knees?"
                    bo"Sure do. I think we can get a few great shots mimicking that feline look of yours..."
                    yo"Hmm..."
                else:
                    yo"My knees!?" with vpunch 
                    bo"Something wrong with that?"
                $ yoru_knees_firsttime = True
            else:
                bo"Think you can get on your knees again?"
                show yoru_rearstart:
                    easein 0.5 yalign 0.1
                if yoruichi_relationship == "Obedient":
                    yo"*Meow!* *Giggles* Just kidding, let's do it..."
                else:
                    yo"*Groans* Ugh..." with vpunch
                    yo"Fine... As long as you don't ask for anything weird!"

            show screen camera1280("yoru_knees_start",1,1.0) with dissolve
            show screen camera_ui("Yoruichi",False) with dissolve
            yo"This isn't particularly comfortable with heels on, [bo_name]..."
            yo"...Careful what you ask for next!"
            menu:
                yo"...Careful what you ask for next!"
                "Can you lie on your stomach for me?" if yoru_knees_stomach_heels == False:
                    default yoru_knees_stomach_heels = False
                    $ yoru_knees_stomach_heels = True
                    bo"Let's make you comfortable then!"
                    bo"Think you can lie on your stomach and raise your feet behind your back?"
                    show screen camera1280("yoru_knees_stomach_heels",1,0.5) with dissolve
                    yo"Will this do?"
                    
                    bo"I knew you are a natural Yoru..."
                    if yoruichi_relationship == "Obedient":
                        yo"I am? I am just following your directions..."
                        bo"You really are!"
                    else:
                        yo"Just... Shut up and take the shot!"
                    bo"And..."
                    show screen camera_ui("Yoruichi",True) with dissolve
                    $ ui.interact()
                    show screen camera_ui("Yoruichi",False) with dissolve
                    yo"Not sure if I can get used to this..."
                    bo"You are doing great, and you are looking even better!"
                    yo"..."
                    yo"Ugh... Can I get off the floor now?"
                "Can you lie on your side for me?" if yoru_knees_side_heels == False:
                    default yoru_knees_side_heels = False
                    $ yoru_knees_side_heels = True
                    bo"Let's make you comfortable then..."
                    bo"Think you can shift your weight on your right hand?"
                    bo"Place your other hand on your thigh and look back toward the lens..."
                    show screen camera1280("yoru_knees_side1_heels",1,0.5) with dissolve
                    yo"Easy enough..."
                    bo"I knew you are a natural Yoru..."
                    yo"Just... Shut up and take the shot!"
                    bot"Hehe!"
                    
                    bo"And..."
                    show screen camera_ui("Yoruichi",True) with dissolve
                    $ ui.interact()
                    show screen camera_ui("Yoruichi",False) with dissolve
                    bo"This one came out nicely!"
                    yo"Not sure if I can get used to this..."
                    bo"You are doing great, and you are looking even better!"
                    yo"Ugh... Can I get up now?"

                "Stay exactly as you are..." if yoru_knees_stay == False:
                    default yoru_knees_stay = False
                    $ yoru_knees_stay = True
                    bo"Stay exactly as you are..."
                    bo"That fierce look on your face... You've struck perfection!"
                    bo"If I didn't know better, I'd be scared to approach you fearing that you may claw my face off..."
                    
                    yo"Maybe I should do exactly that..." with vpunch
                    bo"We both know you wouldn't!"
                    yo"*Scoffs*... Hmph!" with vpunch
                    bo"Ready, and..."
                    show screen camera_ui("Yoruichi",True) with dissolve
                    $ ui.interact()
                    show screen camera_ui("Yoruichi",False) with dissolve
                    bo"What a snap..."
                    yo"Can I get up now...?"
                


            $ yoru_picture_counter += 1
            jump yoru_repeatmodelling
        "????" if yoru_picture_counter <2:
            "Amp up the heat first..."
            jump yoru_model_repeatable_menu

        "Put your heels back on" if yoru_heels_on == False:
            $ yoru_heels_on = True
            bo"Can you put your heels back on please?"
            show yoru_takeoff_heels2 with dissolve:
                yalign 0.0
            show yoru_takeoff_heels2:
                easein 5 yalign 0.45
            yo"Get a grip, [bo_name]..."
            "She reached down to clasp her heels back on..."
            bo"I am a professional, Yoru..."
            bo"If I want you to put your heels back on, rest assured there's an important reason for that..."
            scene yoru_takeoff_heels with dissolve
            yo"There better be..."
            jump yoru_repeatmodelling
        

        "Take off your heels..." if yoru_picture_counter >=2 and yoru_heels_on == True:
            default yoru_heels_on = True
            $ yoru_heels_on = False
            bo"I think it's best if you take your heels off for this next one..."
            show yoru_takeoff_heels with dissolve
            yo"You want me to take off my heels?"
            bo"Sure do..."
            show yoru_takeoff_heels2 with dissolve:
                yalign 1.0
            show yoru_takeoff_heels2:
                easein 2 yalign 0.0
            pause 1.5
            show screen parallax1280("yoru_takeoff_heels2",1,1.0) with dissolve
            call showscrollingimage from _call_showscrollingimage_79
            yo"Fine... You better not be getting any strange ideas, [bo_name]..."
            "She reached down to unclasp her strappy heels..."
            bo"I am a professional, Yoru..."
            bo"If I want you to take of your heels, rest assured there's an important reason for that..."
            call hidescrollingimage from _call_hidescrollingimage_78
            hide screen parallax1280
            scene yoru_takeoff_heels with dissolve
            scene black with dissolve
            yo"There better be..."
            jump yoru_repeatmodelling

        # "Put your heels back on..." if yoru_picture_counter >=2 and yoru_heels_on == True:
        #     $ yoru_heels_on = True
        #     "fill"


            $ yoru_picture_counter += 1
            jump yoru_repeatmodelling

        "????" if yoru_picture_counter <3:
            "Keep amping the heat..."
            jump yoru_model_repeatable_menu
        "Get on the mattress..." if yoru_picture_counter >=3:
            if v17_update == True:
                pass
            else:
                $ notification("Exclusive supporters scene")

            $ yoru_mattress_firsttime = False
            if yoru_mattress_firsttime == False:
                
                bo"It's time to make some use out of that mattress..."
                show yoru_rearstart:
                    yalign 0.0 xalign 0.5
                with dissolve
                show yoru_rearstart:
                    easein 2 yalign 1.0
                if yoruichi_relationship == "Obedient":
                    yo"You want me... on the mattress?"
                else:
                    yo"Hey kid, you aren't thinking of anything weird, are you?"
                show screen camera1280("yoru_rearstart") with dissolve
                show screen camera_ui("Yoruichi",False) with dissolve
                if yoruichi_relationship == "Obedient":
                    bo"You don't have to worry, I just think it'd make for some great shots."
                    yo"Not sure if worried is the right word, [bo_name]..."
                    yo"Things are getting a bit... heated, don't you think?"
                    bo"I told you I'd amp up the heat when you imposed to me your limitations..."
                    yo"That you did, let's do it then!"
                else:
                    bo"It's '[bo_name]' to you, remember?"
                    bo"And of course I am being professional! What's wrong with lying on a mattress anyway..."
                    yo"You will excuse my assumptions after seeing how you act around me..."
                $ yoru_mattress_firsttime = True
            else:
                bo"Let's have you get on the mattress for this next one..."
                show yoru_rearstart:
                    yalign 0.0 xalign 0.5
                with dissolve
                show yoru_rearstart:
                    easein 2 yalign 1.0
                if yoruichi_relationship == "Obedient":
                    yo"The mattress again, huh?"
                    yo"Let's do it!"
                else:
                    yo"A-again? *Sigh*..."
                    yo"Just as long as you don't try anything weird..."

            show blackscreen onlayer screens with dissolve
            if yoruichi_relationship == "Obedient":
                "Yoru gets on the mattress you've set up. You sensed a hint of excitement in her demeanor..."
            else:
                "Yoru reluctantly gets on the mattress you've set up..."
            if yoru_heels_on == True:
                show screen camera1280("yoru_onbed_start_heels",1,1.0) with dissolve
            else:
                show screen camera1280("yoru_onbed_start",1,1.0) with dissolve
            hide blackscreen onlayer screens with dissolve
            bot"Damn..."
            bo"Looking good, Yoru!"
            yo"Come on then, prove to me you aren't just another jerk..."
            hide screen camera_ui
            show screen camera_ui("Yoruichi",False) with dissolve
            yo"What do I do next..."
            
            menu yoru_bedmenu:
                yo"What do I do next..."
                "Stay on your back..." if yoru_onback_photo == False:
                    default yoru_onback_photo = False
                    $ yoru_onback_photo = True
                    show screen camera1280("yoru_onbed_start",1,0.5) with dissolve
                    bo"You stay like that and..."
                    menu:
                        bo"You stay like that and..."
                        "Relax a little bit":
                            bo"Try to relax a little bit..."
                            show screen camera1280("yoru_bed_frontstart",1,0.5) with dissolve
                            if yoruichi_relationship == "Obedient":
                                yo"Wouldn't wanna get too relaxed now. *Giggles*"
                                bot"Is she... insinuating something?"
                                yo"..."
                            else:
                                yo"This is anything but relaxing, [bo_name]..."
                                yo"..."
                            menu:
                                yo"..."
                                "You are still a little tense...":
                                    bo"You are still looking a little tense..."
                                    bo"Think you can just let your head drop on the pillow and rest your arms close to your face?"
                                    yo"..."
                                    show screen camera1280("yoru_bed_front_above",1,0.5) with dissolve
                                    bo"You really are a natural at this..."
                                    if yoruichi_relationship == "Obedient":
                                        yo"Are you trying something funny? [bo_name]..."
                                        bo"Maybe..."
                                        bot"Fuck me... She is so hot!"
                                    else:
                                        yo"...Shut up and take the shot!"
                                "Just like that...":
                                    bo"Just like that..."
                                
                        "Try to look comfortable...":
                            bo"Try to look comfortable..."
                            bo"Rest your head on the pillow and rest your hands above your head..."
                            show screen camera1280("yoru_bed_front1",1,0.5) with dissolve
                            yo"Is this what you meant?"
                            menu:
                                yo"Is this what you meant?"
                                "Exactly like that!":
                                    bo"Exactly like that!"
                                    bo"You really are a natural at this..."
                                    if yoruichi_relationship == "Obedient":
                                        yo"Are you trying something funny? [bo_name]..."
                                        bo"Maybe..."
                                        bot"Fuck me... She is so hot!"
                                    else:
                                        yo"...Shut up and take the shot!"
                                "Let's add some flair...":
                                    bo"Not bad, but we can add some flair..."
                                    bo"Think you can shift your weight to one side?"
                                    bo"Keep your hands where they are but make sure they are visible..."
                                    show screen camera1280("yoru_bed_front2",1,0.5) with dissolve
                                    yo"I think I understand..."
                                    bo"You really are a natural at this..."
                                    if yoruichi_relationship == "Obedient":
                                        yo"Are you trying something funny? [bo_name]..."
                                        bo"Maybe..."
                                        bot"Fuck me... She is so hot!"
                                    else:
                                        yo"...Shut up and take the shot!"
                        

                                

                        
                "Turn around on your stomach..." if yoru_onstomach_photo == False:
                    default yoru_onstomach_photo = False
                    $ yoru_onstomach_photo = True
                    bo"I am going to need you to lie on your stomach instead..."
                    yo"You want me to... turn around?"
                    bo"Sure do!"
                    show screen camera1280("yoru_bed_rearstart",1,0.5) with dissolve
                    if yoruichi_relationship == "Obedient":
                        yo"What would someone think if they saw us like this, [bo_name]..."
                        bo"That we are two professionals, doing our jobs. You had something else in mind?"
                        bot"That ass is something else..."
                        call increaselust(50) from _call_increaselust_143
                        yo"Careful what you ask for next..."
                    else:
                        yo"I am not sure I am liking where this is going [bo_name]..."
                        bot"That ass is something else..."
                        yo"Careful what you ask for next..."
                    menu yoru_onstomach_menu:
                        yo"Careful what you ask for next..."
                        "Don't worry, that's all I needed from you!":
                            bo"Don't worry, this is all I needed from you..."
                            if yoruichi_relationship == "Obedient":
                                yo"Something's telling me that's not true..."
                                bot"Is she... flirting with me!?" with vpunch
                                call increaselust(50) from _call_increaselust_144
                            else:
                                yo"Good! Now hurry up and take the shot!" with vpunch
                        "{color=[dominancecolor]}Think you can spread your legs wide open?{/color}":

                            if yoruichi_relationship == "Obedient":
                                bo"This shot would look much better if you... spread your legs out for me!"
                                yo"Okay, now you are just playing around with me, aren't you? You damned brat..."
                                call checkDominance(15,"yoru_onstomach_menu") from _call_checkDominance_19
                                bo"What, No! I was just thinkin-"
                                # call checkDominance(15,"yoru_onstomach_menu")
                                # bo"I didn't mean it like that, Yoru..."
                                # bo"I am just thinking of optimal angles!"
                                # call changeDominance(1)
                                # bo"Trust me on this one, I bet it'll make us a lot of money..."
                                # yo"Kid... I won't be selling my body for a chance to make some money..."
                            else:
                                bo"This shot would look much better if you spread your legs out..."
                                yo"Are you fucking serious kid...?"
                                call checkDominance(15,"yoru_onstomach_menu") from _call_checkDominance_20
                                bo"I didn't mean it like that, Yoru..."
                                bo"I am just considering optimal angles!"
                                call changeDominance(1) from _call_changeDominance_75
                                bo"Trust me on this one, I bet it'll make us a lot of money..."
                                yo"Kid... I won't be selling my body for a chance to make some money..."
                            show screen camera1280("yoru_bed_rear1",1,0.5) with dissolve
                            if yoruichi_relationship == "Obedient":
                                yo"Less talking, more working!" with vpunch
                                bot"D-damn, she took me up even on that one!" with vpunch
                                bo"You look fucking sublime Yoru..."
                                yo"Anything else you'd like to see... Director [bo_name]?"
                                call increaselust(50) from _call_increaselust_145
                                call changeDominance(1) from _call_changeDominance_76
                                bo"This will do for now...You devious kitten!"
                                yo"*Giggles* Something's telling me that's not true..." with vpunch
                                bot"She... She is definitely flirting with me!"
                                yo"What are you sitting there for! Hurry up and take the shot!" with vpunch
                                bot"Or maybe not..."
                                bo"Right..."
                            else:
                                yo"You got it? This is far as I am willing to go..."
                                bo"You look fucking sublime Yoru..."
                                bot"I bet she'd be willing to whore herself soon after making some money with this... Heh!"
                                yo"What are you sitting there for! Hurry up and take the shot!" with vpunch
                                bo"Right..."
                        "Bring your legs together...":
                            bo"Think you can bring your legs closer together?"
                            bo"Look back towards me as if you were just waking up, with a look of mild annoyance..."
                            show screen camera1280("yoru_bed_rear0",1,0.5) with dissolve
                            if yoruichi_relationship == "Obedient":
                                bo"Excellent! I bet that defiant look of yours is going to awaken something in some people..."
                                yo"That's the look I'll be giving you when you keep saying stupid stuff like that, [bo_name]!"
                                yo"Now is there something else you need me to do?"
                                bo"N-no Ma'am!" with vpunch
                                yo"Something's telling me that's not true..."
                                bot"Is she... flirting with me!?" with vpunch
                                call increaselust(50) from _call_increaselust_146
                            else:
                                bo"Excellent! I bet that defiant look of yours is going to awaken something in some people..."
                                yo"What does that even mean. Just hurry up and take the shot!"
                                bo"Heh...Right on it!"

                "Turn on your side..." if yoru_bed_onside_photo == False:
                    default yoru_bed_onside_photo = False
                    $ yoru_bed_onside_photo = True
                    bo"Think you can turn on your side for this next one?"
                    yo"On my side, huh?"
                    show screen camera1280("yoru_bed_side2",1,0.5) with dissolve
                    yo"You mean, something like this?"
                    bo"You really have a gift, Yoru!"
                    if yoruichi_relationship == "Obedient":
                        bo"You are such a natural beauty, and your posing... it comes to you so naturally!"
                        yo"Kid, you aren't gonna undress me with your words. Hurry up and take the shot! *Giggles*"
                        bo"I am serious Yoru! if we take this seriously, we could do something great, me and you..."
                        yo"We'll see about that. For now..."
                    else:
                        bo"Posing comes to you naturally, and your beauty is unparalleled!"
                        yo"Kid, keep it shut..."
                        bo"I am just saying, if we take this seriously, we could do something great, me and you..."
                    yo"Just... tell me what to do next!"
                    menu yoru_bed_onside_menu:
                        yo"Just... tell me what to do next!"
                        "You do nothing! You are perfect just the way you are...":
                            bo"You do nothing next! You look perfect exactly as you are..."
                            yo"Good! Now hurry up and take the shot!" with vpunch
                        "{color=[dominancecolor]}Think you can pull off a seductive pose?{/color}":

                            if yoruichi_relationship == "Obedient":
                                bo"I think you could pull off an amazing seductive shot right about here..."
                                yo"And who exactly am I seducing, [bo_name]..."
                                bo"I'll leave that up to your discretion..."
                            else:

                                bo"I think you could pull off an amazing seductive shot right about here..."
                                yo"Are you serious kid...?"
                            call checkDominance(12,"yoru_bed_onside_menu") from _call_checkDominance_21
                            if yoruichi_relationship == "Obedient":
                                yo"You'll leave that to me? Then..."
                                yo"I'll pretend I am seducing a certain blonde kid, who likes to think he is some hot-shot modelling Director..."
                                yo"Would that fit your planned shot?"
                            else:
                                bo"As serious as one can be. You are drop-dead gorgeous Yoru..."
                                bo"Add a touch of seduction in your posing, and you'd have men and women alike swooning over you!"
                                yo"You are exaggerating..."
                            call changeDominance(1) from _call_changeDominance_77
                            if yoruichi_relationship == "Obedient":
                                bo"That is exactly what I was thinking too..."
                                bo"Show me then. How would you go about seducing someone like him?"
                                bo"Because I wager you might even have a shot at that..."
                            else:
                                bo"I am absolutely not!"
                                yo"...So, what do I do?"
                                bo"Can you try stretching out one of your legs while keeping the other bend?"
                                bo"Place one of your hands on your thigh, the other close to your mouth..."
                                bo"Keep your lips slightly parted and your eyelids low..."
                                bo"You manage all that, and we got ourselves a moneyshot!"
                                yo"So you say, but..."
                            show screen camera1280("yoru_bed_side3",1,0.5) with dissolve
                            yo"Is that the truth? Or just a hopeless ambition of yours..."
                            call increaselust(50) from _call_increaselust_147
                            bo"Just like that... You look fucking incredible!"
                            if yoruichi_relationship == "Obedient":
                                yo"Then shut up and take the  shot!" with vpunch
                                bo"R-right..."
                                bot"Fuck... I can't take all this teasing for much longer! I think I am losing control..."
                            else:
                                bo"Trust me on this one Yoru. A few more sessions together and I am sure we'll be making bank together in no time..."
                                yo"Then shut up and take the damn shot!" with vpunch
                                bo"Right..."
                        "Think you can try a playful pose?":
                            bo"Think you can try posing in a more playful manner?"
                            bo"Just like a kitty cat would..."
                            show screen camera1280("yoru_bed_side1",1,0.5) with dissolve
                            yo"Something like this?"
                            bo"I knew you'd pull this one off without any trouble..."
                            bot"Her nipples are poking through..."
                            bo"You are getting into this a little bit, aren't you you little kitty..."
                            if yoruichi_relationship == "Obedient":
                                yo"Maybe I am... *Meow!*"
                                yo"*Giggles* Now hurry up and take the shot already!"
                                call increaselust(50) from _call_increaselust_148
                                bot"Fuck... I can't take this for much longer! I think I am losing control..."
                            else:
                                yo"Don't call me that, [bo_name]..."
                                yo"Now shut up and take the shot..."

                        
                "Let's emphasize your... feet (Barefoot)" if yoru_heels_on == False and yoru_feet_photo == False:
                    default yoru_feet_photo = False
                    $ yoru_feet_photo = True
                    bo"Let's try something a little bit different..."
                    if yoruichi_relationship == "Obedient":
                        yo"Oh I can't wait to see what other silly ideas you have in store for me after literally getting me lying on a mattress for you..."
                        yo"What's next, stripping down to my underwear? *Giggles*"
                        bo"Not quite, but maybe an idea to explore in the future!"
                        yo"You wish!" with vpunch
                        yo"So what is this time..."
                        bo"We are going to try to emphasize your feet with this next one..."
                        yo"My f-feet!? Who would even want to look at that, [bo_name]!" with vpunch
                        bo"You'll have to trust me on this one! Just lie on your back and raise one of your feet, bringing it close to the camera..."
                        yo"S-seriously? You are..."
                    else:

                        bo"We are going to try to emphasize your feet with this next shot..."
                        yo"My feet!? Who the hell would want to look at that, [bo_name]..." with vpunch
                        bo"You'll have to trust me on this one! Just lie on your back and raise one of your feet close to the camera..."
                        yo"You people..."
                    show screen camera1280("yoru_bed_feet1",1,0.5) with dissolve
                    if yoruichi_relationship == "Obedient":
                        yo"Repulsive! *Sigh*..." with vpunch
                        bo"Heh! You'd be surprised at the amount of people that would love this..."
                        call increaselust(20) from _call_increaselust_149
                        yo"By the looks of it... You included!" with vpunch
                        bo"W-what are you talking about... I am not-"
                        yo"Kid, shut the fuck up and take the shot!" with vpunch
                        "Yoru took notice of something you have yet to realize yourself..."
                    else:
                        yo"You are repulsive..."
                        bo"Heh! You'd be surprised the amount of people who would pay to lick the sweat straight off your soles..."
                        yo"Kid, shut the fuck up and take the shot!" with vpunch
                    menu:
                        yo"Kid, shut the fuck up and take the shot!"
                        "{color=[dominancecolor]}I think we can get a better shot if...{/color}":
                            bo"I think this would be a much better shot if..."
                            hide screen camera_ui
                            show screen camera1280("yoru_bed_feet_wrong",1,0.5)
                            with dissolve
                            "You lowered the camera and instead took hold of her foot in order to re-adjust her posing..."
                            call checkDominance(15,"yoru_badending") from _call_checkDominance_22
                            yo"H-hey...!" with vpunch
                            bo"Don't be stressed! Just, move this foot over the other..."
                            show screen camera1280("yoru_bed_feet2",1,0.5) with dissolve
                            call changeDominance(1) from _call_changeDominance_78
                            bo"...Just like this! Good girl..."
                            yo"Y-you are pushing the line, kid..."
                            bo"Just relax, Yoru... This shot will be sublime!"
                        "Don't mind if I do!":
                            pass
                        "I think there's something wrong with your... foot" if yoruichi_relationship == "Unwillingly Obedient":
                            label yoru_feetwrong:
                            bo"Wait a second..."
                            bo"I think there's something wrong with your foot..."
                            yo"Huh? What the hell are you on about kid..."
                            hide screen camera_ui
                            show screen camera1280("yoru_bed_feet_wrong",1,0.5)
                            with dissolve
                            "You dropped the camera and instead took hold of her foot, pretending to be inspecting it..."
                            yo"Hey, watch it!" with vpunch
                            bo"I was right, your feet are..."
                            show screen camera1280("yoru_bed_feet_wrong2",1,0.5) with dissolve
                            $ renpy.sound.play("/audio/soun_fx/lickpenis1.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                            bo"Way too fucking sexy!" with vpunch
                            yo"Y-you..." with vpunch
                            "You let go of the camera and started licking Yoru's soles..."
                            label yoru_badending:
                            hide screen camera_ui
                            hide screen parallax1280
                            hide screen camera1280
                            scene black with vpunch
                            if yoru_success_blackmail == True:
                                "She punched you in the ribs and pushed you away!"
                                yo"That's for w-what you did to me, asshole!"
                            elif yoru_fail_blackmail == True:
                                "She easily pushed you away and kicked you in the face!"
                            else:
                                "She kicked you in the face!" with vpunch
                            bo"Ouch!"
                            scene bg bb day
                            show boruto angry2 at left
                            show yoruc annoyed at right
                            with dissolve
                            bo"That hurt, you bitch!"
                            yo"Piss off, you dirty creep! I knew you were up to no good from the first time we met..." with vpunch
                            yo"This session is over!" with vpunch
                            show boruto angry with dissolve
                            bo"My bad for trying to help in the first place..."
                            bo"Can't even take a little... joke!"
                            if yoru_success_blackmail == True:
                                yo"A joke? You call assaulting someone a joke?"
                                show boruto snob with dissolve
                                bo"Come on, that was fun, wasn't it?"
                                bo"Your body certainly had a positive reaction from what I could see..."
                                yo"Then you are either stupid, or blind..."
                                bo"We'll see if that's true soon enough, Yoru..."
                                yo"..."
                                bot"I'll have her begging for my cock in no time... Hehe!"

                            elif yoru_fail_blackmail == True:
                                yo"A joke? You call assaulting someone a joke?"
                                bo"M-maybe a lapse of judgement... I was just p-playing around anyway!"
                                bot"F-fuck... Turns out what little remains of her powers is still a significant amount..."
                                bot"I shouldn't push my luck too much with her... For now!"
                            else:
                                
                                yo"A joke? You call m-messing with other people's feet a joke?"
                            label yoru_model_neutralending:
                            $ renpy.sound.play("/audio/soun_fx/transform.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                            show blackscreen with flash
                            hide yoruc
                            show boruto surprised2
                            show yoru cat2t behind boruto:
                                zoom 0.25 xpos 930 ypos 532
                            hide blackscreen with dissolve
                            $ renpy.sound.play("/audio/soun_fx/meow1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                            yo"*Angry meow!*" with vpunch
                            show boruto snob with dissolve
                            bo"The hell you Meowing at me for, you crazy cat lady!"
                            yo"Hurry up and take me outside! I am going back to Obo's..." with vpunch
                            yo"And I am not about to have any more conversation with your relatives..."
                            show yoru:
                                easeout 0.7 xpos 300
                            pause 0.3
                            hide yoru
                            show boruto cat
                            with fade
                            yo"You try anything and I'll claw your neck off!" with vpunch
                            bo"Will you relax, you damned cat?"
                            $ renpy.sound.play("/audio/soun_fx/meow1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                            yo"*Furious meow!*" with vpunch
                            show boruto:
                                easein 1 xpos 1500
                            bo"Fine, Fine... I get it!"
                            $ renpy.sound.play("/audio/soun_fx/dooropen.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                            scene black with dissolve
                            "You quietly escorted Yoru downstairs, but..."
                            him"[bo_name_stutter]! Wait a second..." with vpunch
                            show bg lr_day with dissolve:
                                zoom 0.68
                            show boruto cat at left with dissolve
                            $ renpy.sound.play("/audio/soun_fx/meow2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                            yo"Damn it! *Annoyed Meow!*" with dissolve
                            show hima worried2 at right with dissolve:
                                zoom 0.34
                            bo"What do you want, [him_name]..."
                            him"Did your friend already leave? I thought I'd get a chance to talk with her..."
                            show hima surprised with dissolve
                            show hima:
                                easein 0.5 xalign 0.5
                            him"Wait a second..."
                            scene black with vpunch
                            him"*Gasps!*"
                            show himapet1 with dissolve
                            $ renpy.sound.play("/audio/soun_fx/meow2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                            him"Is that-" with vpunch
                            yo"*Concerned M-meow?*"
                            him"Awwww! A fluffy little kitty cat! Who's the cute little guy on your shoulder!" with vpunch
                            menu:
                                him"Awwww! A fluffy little kitty cat! Who's the cute little guy on your shoulder!"
                                "Just a stray I am caring for...":
                                    bo"Just a stray kitty I am caring for..."
                                    bo"I was just about to take her outside..."
                                    call changeRespect("Himawari",2) from _call_changeRespect_178
                                    him"Aww, how unlike you! Can I please pet her?"
                                    show himapet2 with dissolve
                                "It's Yoru!":
                                    bo"Oh this little kitty? It's Yoru of course..."
                                    $ renpy.sound.play("/audio/soun_fx/hiss.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                    yo"*Angry Meow!*" with vpunch
                                    him"What kind of stupid joke is that, you dummy! Even the kitty knows better than that..."
                                    him"Look at her, such a little cutie! Can I pet her please?"
                                    show himapet2 with dissolve
                            him"Pretty pleaaaase... Here kitty, kitty!"
                            $ renpy.sound.play("/audio/soun_fx/hiss.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                            scene black with vpunch
                            yo"Menacing M-meow!" with vpunch
                            show bg lr_day:
                                zoom 0.68
                            show boruto cat at left
                            show hima mad at right:
                                zoom 0.34
                            with dissolve
                            him"W-what the hell is wrong with your kitty... She's so feral!"
                            bo"Yeah, well... I am working on it. She'll be tamed soon enough!"
                            $ renpy.sound.play("/audio/soun_fx/meow2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                            yo"*Disapproving Meow!*" with vpunch
                            bo"In any case, Yoru left a while ago, and I gotta go too!"
                            show boruto:
                                easein 1 xpos -1000
                            bo"See ya later!"
                            him"Hmph!"
                            scene black with dissolve
                            "You bring Yoru to your porch as requested..."
                            scene bg porch
                            show boruto cat at center
                            with dissolve
                            bo"There you go, damned cat..."
                            bo"Will you be able to make it there on your own? What if your form breaks before you get there..."
                            yo"I'll figure it out myself!" with vpunch
                            yo"Don't think I'll be coming back here, kid!"
                            scene blackscreen with vpunch
                            "She pounced off your shoulder..."
                            scene bg porch
                            show boruto surprised2
                            with dissolve
                            yo"Not before you show me that you can actually make us money out of that!" with vpunch
                            $ renpy.sound.play("/audio/soun_fx/hiss.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                            "She started strolling away while hurling insults at you..."
                            yo"Meow! Damned idiot..."
                            show boruto snob with dissolve
                            if not _in_replay:
                                if quest.exists("bohim_2"):
                                    if quest.is_state("3_bohim_2", "in progress"):
                                        $ notification("Quest objective completed")
                                        $ quest.change_quest_title("3_bohim_2",f"Purchase a camera and convince Yoru to help you")
                                        $ quest.change_quest_title("4_bohim_2",f"Have your first session with {him_name}")
                                        $ quest.check("3_bohim_2", "completed")
                                        $ quest.check("4_bohim_2", "in progress")
                            bot"Heh! Whatever, crazy bitch..."
                            bot"Pretty sure I'll find a way to make some bread out of this..."
                            show boruto sceeming2 with dissolve
                            call changeHatred(1) from _call_changeHatred_130
                            bot"Worst case, I'll just have to use what I know against her!"
                            $ renpy.end_replay()
                            jump action_taken
                              
            bo"And..."
            show screen camera_ui("Yoruichi",True)
            with dissolve
            $ ui.interact()
            show screen camera_ui("Yoruichi",False) with dissolve
            bo"This will certainly fetch a high price..."
            show screen camera1280("yoru_rearstart") with dissolve
            yo"...It better!"
            hide screen parallax1280 with dissolve
            $ yoru_picture_counter += 1
            jump yoru_repeatmodelling
        




        