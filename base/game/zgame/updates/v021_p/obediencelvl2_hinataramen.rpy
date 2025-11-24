# 0 = initial chat with Hinata, 1 = opens first day of work, 2 = opens repeat shifts WIP
default v21ramenintro_progression = 0

label ntrwarning_skip:
    $ notification("Skipped due to optional preferences")
    return


label v21_ramenintro_talk:

    $ renpy.sound.play("/audio/soun_fx/doorclose.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    scene bg lr_day:
        zoom 0.68
    show boruto angry at right
    show shina worried at left
    with dissolve
    bo "Those goons are relentless!"
    show boruto at smallshake
    bo "They're going to keep coming back for their money till they bleed us dry!"
    show boruto worried with dissolve
    bo "I don't know how sustainable this is going to be [hin_rel]..."
    show shina surprised with dissolve

    hin "I k-know... I'm sorry [bo_name]... This is all my fault!"
    show shina worried with dissolve
    hin "I feel so bad for dragging you into this mess..."
    show boruto surprised2 with dissolve
    bo "It's not your fault, but we need to figure something out fast!"
    show boruto worried
    show shina shy
    with dissolve
    hin "I a-agree... It's time that I stopped waiting idly for your [na_rel] to show up and help me..."
    show shina assertive with dissolve
    hin "I... I need to find a solution myself and fix this mess!"
    show boruto normal with dissolve
    bo "Have you considered finding a job for some extra money? Maybe somewhere here in the village?"
    show shina worried with dissolve
    hin "That could potentially help, I also shouldn't rely on only you to work forever..."
    show shina serious with dissolve
    show shina at smallshake
    hin "Any extra money would be beneficial to go towards these cursed debts!"
    bo "What kind of job would you look for though?"
    show boruto smirk with dissolve
    bo "Maybe you could come try work with me at the ramen shop?"
    show shina concerned with dissolve
    hin "The r-ramen shop? You think they'd hire me too?"
    show boruto embarassed with dissolve
    bo "Why not? We could become work buddies there!"
    show boruto smirk with dissolve
    bo "I could have a word with the owner next time I'm there and see what he thinks about it."
    bo "Things have gotten a bit busy there lately so they could probably use the help!"
    show shina shy with dissolve
    hin "I g-guess it's worth a try! I can't just sit around here and do nothing..."
    $ notification("Quest updated")
    $ quest.check("job2_3", "completed")
    $ quest.add([
        Quest("job2_4", ("Help [hin_name] get started at the ramen shop"), ("[hin_name]'s debts"), "in progress"),
        Quest("job2_5", ("Work a few shifts with [hin_name]"), ("[hin_name]'s debts"), "pending", wip=True),
    ])
    show boruto smirk2 with dissolve
    bo "Great! I'll ask him and let you know what he thinks about it."
    show boruto laughing with dissolve
    bo "Don't worry, we'll make it work [hin_rel], one way or another. We won't let those thugs push us around!"
    show shina shy with dissolve
    hin "Th-thank you [bo_name]... You know, I really appreciate everything that you do for us..."
    show shina with dissolve:
        xzoom -1
    hin "I just hope you're right... We {i}have{/i} to make it work somehow..."
    show shina:
        easeout 3 xpos -1000
    pause 0.8
    scene black with dissolve
    hin "For both our sakes..."
    "You can now have [hin_name] pick up work over at the ramen shop. {p}Speak to Obo once you visit the ramen shop to do so."
    jump action_taken




label v21_ramenintro_firstdaytalk:
    show boss:
        easein 2 xalign 1.0
    show boruto laughing at left with dissolve
    bo "Hey you old fart, I actually came to ask you something important..."
    show boss angry3 with dissolve
    obo "Forget it twerp, you ain't getting no stinkin' raise! \nMoney doesn't grow on trees y'know!" with vpunch
    show boruto embarassed with dissolve
    bo "N-no, it's not that... I was wondering if you were looking to perhaps hire more help around here?"
    show boss normal with dissolve
    obo "Hire more help? Hmph, now why would I do that? I'm doing just fine on my own here!" 
    show boss angry2 with dissolve
    obo "Are you trynna call me fat and lazy or something!? \nI'll break you in half kid!" with vpunch
    show boruto surprised2 with dissolve
    bo "N-no, of course not! Chill the fuck out already!"
    show boss laugh with dissolve
    obo "I'm just playin' with ya! Don't shit yer pants now! Baha-hahah!"
    show boss at smallshake
    obo "I would only break a leg at most so that you could still work the kitchen for me!"
    show boruto embarassed with dissolve
    bo "R-right... I had almost forgotten how unhinged you actually are!"
    show boruto surprised2 with dissolve
    bo "Well anyway, like I was saying..." 
    bo "My [hin_rel] is looking for a job to make a little extra cash, and I thought maybe she could help out here at the shop?"
    show boss scared with dissolve:
        xzoom -1
    obo "Yer what now? You trynna turn this into a family business or somethin'? You gonna bring your granny next here too?"
    show boruto pissy with dissolve
    bo "Huh? No, of course not, get a grip you shrivelled up shrimp-dicked bald cunt!"
    show boruto at smallshake
    bo "I'm being serious, it's not like I'm asking you to adopt her or anything! Money is just a bit tight for us..."
    show boruto angry with dissolve
    bo "I just thought it could be a good opportunity, both for her and your sorry old wrinkled ass..."
    show boss laugh with dissolve:
        xzoom 1
    obo "Ha-haa! You've got spirit kid, I'll give you that! Does she have a mouth on her too?"
    show boss normal with dissolve
    obo "Look, business is business. If she can pull her weight, I won't turn her away."
    show boss angry2 with dissolve
    obo "Lately new customers have been pouring in and we've been short-staffed anyway, so it might not be a bad idea to bring her on."
    show boruto laughing with dissolve
    bo "Great! See that wasn't so hard, now was it? I'll let [hin_rel] know right away then!"
    show boss angry3 with dissolve
    obo "Now hold up just a second punk!"
    show boss at smallshake
    obo "Make sure she knows what she's getting into, cuz this ain't no daycare center to babysit her!"
    show boruto smirk with dissolve
    bo "Of course! I'll make sure she's prepared and doesn't disappoint."
    show boss laugh with dissolve
    obo "Good! Go fetch her then so I can take a look with what I'm working with..."
    show boruto surprised2 with dissolve
    bo "W-wait, you mean right now?!" 
    show boss angry with dissolve
    obo "Well does she want to work or not?! I ain't got all day to sit around and just talk about it!" with vpunch
    show boss angry2 with dissolve
    obo "She can start immediately! Bring her in before I change my mind!"
    show boruto sceeming with dissolve
    bo "Alright, alright, don't give yourself an aneurysm. I'll go get her!"
    show boruto:
        easeout 2 xpos -1000
    bo "Sheesh, what a grumpy old bastard..."
    show boss normal with dissolve
    show boss:
        easein 3 xalign 0.5
    obo "His [hin_rel] eh? Well I don't care who she is, she better be able to take the heat!"
    show boss laugh with dissolve
    obo "I know just what outfit to put her in too, one of Yoru's old sexy rags... Heh heh heh..."
    show boss at smallshake
    obo "I hope she has the {i}assets{/i} to pull it off! Bah-hahah!"
    show boss with dissolve:
        xzoom -1
    show boss:
        easeout 3 xpos 3000
    pause 0.3
    scene black with dissolve
    obo "Now where did I leave that uniform..."
    "..."

    "Meanwhile outside..."
    if day_part >= 3:
        scene bg ramenshop night
    else:
        scene bg ramenshop 
    show boruto smirk at right 
    with fade
    show boruto:
        easein 2 xalign 0.5
    bot "Well that was a lot easier than I thought..."
    show boruto suspicious with dissolve
    bot "Almost too easy actually..."
    show boruto at smallshake
    bot "Obo is not exactly the most trustworthy guy around, I hope he doesn't have any weird ideas in that thick skull of his..."
    show boruto normal with dissolve
    bot "I guess I shouldn't complain though, it was my idea after all!"
    if chosen_love_path:
        show boruto smirk with dissolve
        bot "The money will definitely help us out, but I'm looking forward to just having [hin_rel] around me more."
    if chosen_hate_path:
        show boruto sceeming2 with dissolve
        bot "Who knows, maybe when nobody is looking, I can sneak in a little fun with [hin_rel]..."
    show boruto smirk2 with dissolve
    bot "Let's bring her in and get the ball rolling."
    show boruto:
        easeout 2 xpos -1000
    pause 0.3
    scene black with dissolve
    bot "This is going to be interesting..."

    "You head back home and find [hin_name] doing her usual chores."
    "After quickly briefing her on the situation, you both return together to the ramen shop."

    label v21_initial_ramenintro_start:
    $ initialize_replay_defaults()

    scene ramenintro
    show shina shy at left
    show boruto normal at right
    with dissolve
    hin "Are you sure about this [bo_name]? This feels so incredibly abrupt..."
    show shina shy2 with dissolve
    hin "I don't even know if I'm cut out for this kind of work..."
    show boruto smirk with dissolve
    bo "Relax [hin_rel], I'm sure you'll do great!"
    show boruto smirk2 with dissolve
    bo "How hard can it be to serve some ramen and clear some tables, right?"
    bo "Just keep a smile on your face and don't let the customers get to you!"
    show shina worried with dissolve
    hin "Let them g-get to me? W-what do you mean by that exactly?"
    show boruto laughing2 with dissolve
    bo "Oh you know... People can be real jerks sometimes, but you'll be fine..."
    show boruto smirk with dissolve:
        xzoom -1
    show boruto:
        easein 1 xalign 0.9
    bo "Oh look, there's the owner coming now!"
    show boss normal with dissolve:
        xalign 2.0
    show boss:
        easein 2 xalign 1.0
    show boruto:
        easein 2 xalign 0.4
    show shina shy behind boruto
    with dissolve
    bo "Hey boss, I'm back and I brought along your potential new employee!"
    show boss angry3 with dissolve
    obo "It's about time, what took you so long? We're starting to get busy around here!"
    show boss laugh with dissolve
    obo "So you must be the potential new help I've been hearing about... \nCome forward, don't be shy!"
    show shina:
        easein 2 xalign 0.4
    show boruto behind shina:
        easein 2 xalign 0.0
    with dissolve
    hin "H-hello, yes... You must be Obo, the owner of this wonderful ramen shop?"
    show shina smiling with dissolve
    hin "It's a pleasure to meet you, I'm [hin_name]..."
    show boss concerned with dissolve
    obo "Wait a second... Aren't you... Hmmm..."
    "Obo instantly recognizes [hin_name], former heiress of the Hyuga clan and the current wife of the Hokage himself!"
    "Excitement flashes across his face as he realizes the implications of someone of her stature working at his shop, but he quickly conceals it in front of you."
    show shina shy with dissolve
    hin "I'm [bo_name]'s [hin_rel], yes! I heard from him that you were open to having me on board here, is that r-right?"
    show boss laugh with dissolve
    obo "Yes of course! There's always room for another hard worker here!"
    obo "Your kid seems to manage just fine, so I don't see why you wouldn't be able to take on a few shifts here yourself."
    show boruto smirk2
    show boruto at smallshake
    bo "She's perfectly capable, you'll see!"
    show shina normal
    show boruto smirk
    with dissolve
    hin "Y-yes, of course, I'll do my best around here for whatever is needed of me!"
    show boss at smallshake
    obo "Sounds like music to my ears!"
    show boss normal with dissolve
    obo "Before we go any further, there's a few things we need to go over though..."
    show boss angry2 with dissolve
    obo "This is a ramen shop, not some fancy restaurant. We don't cater to no snobs or the upper class here!" with vpunch
    obo "So expect the crowd to be rowdy and loud, and don't be surprised if some of them get out of line..."
    show boss angry3 with dissolve
    obo "Is that going to be an issue for you?"
    show shina worried with dissolve
    hin "I-I don't think so... How rowdy are we talking exactly? You make it sound dangerous..."
    show boss angry2 with dissolve
    obo "All I'm saying is that you need to be able to keep your cool and deal with anything that happens."
    obo "I'll always be around to have your back if things get rough too, of course."
    show shina shy with dissolve
    hin "I u-understand... I'll do my best to stay professional!"
    show boss laugh with dissolve
    obo "Good, that's the spirit!" with vpunch
    obo "You'll be working the front here with me! Mostly taking orders, serving food and cleaning tables."
    show shina assertive with dissolve
    hin "I see, okay... That sounds manageable enough!"
    show boss at smallshake
    obo "Also you're going to be wearing a uniform, and I expect you to wear it with pride and dignity!"
    obo "I have it prepared for you in the back room already."
    show shina surprised with dissolve
    hin "A u-uniform...? U-um, what kind of uniform would that be exactly?"
    show shina worried with dissolve
    obo "It's a traditional outfit, nothing fancy but it gets the job done! \nYou'll see for yourself soon enough..."
    show boss normal with dissolve
    obo "Now... Follow me and I'll show you where to try it on. We need to make sure it fits you properly first!"
    show shina shy with dissolve
    hin "Y-yes sir, lead the way...!"
    show boruto suspicious with dissolve
    bot "He's taking her to the back room to get changed? They'll be alone there together..."
    bot "I know full well what this perverted old dog is capable of, even if he's not showing it right now." with vpunch
    bot "Maybe I shouldn't be leaving them alone together just in case..."
    menu v21_hinataramen_intromenu:
        bot "Maybe I shouldn't be leaving them alone together just in case..."
        "{color=[dominancecolor]}Nobody touches [hin_rel] except me!{/color}":
            call checkDominance(10,"v21_hinataramen_intromenu",1) from _call_checkDominance_68
            show boruto angry with dissolve
            bot "I don't trust him, there's no way I'm letting that creep get anywhere near [hin_name]!"
            bot "I'll be keeping a close eye on them, just in case."
            show boruto normal 
            show shina behind boruto
            with dissolve
            show boruto normal:
                easein 2 xalign 0.4
            show shina:
                easein 2 xalign 0.0
            bo "I'll come with, just to make sure everything's alright."
            show boss angry2 with dissolve
            obo "What are you, a lost puppy? Don't you have preparations to make in the kitchen or something?"
            show boruto sceeming with dissolve
            bo "Yoru will be fine on her own for a bit, I'll get to it when we're done."
            if yoruichi_modelling_completed == True:
                hint "Yoru...? Where have I heard that name before..."
            show boss at smallshake
            obo "You're leaving my wife to do all the work while you just hang around here kid?"
            show boss angry3 with dissolve
            obo "I don't pay you to be my shadow everywhere I go!" with vpunch
            if yoruichi_modelling_completed == True:
                hint "Wait... Isn't that the pretty woman that [bo_name] brought home the other day?"
                if yorugroped_intro == True:
                    hint "He introduced her as his girlfriend! But she is also Obo's wife?!" with vpunch
                    hint "What in the world is going on here... He must have just been messing with me..."
                if yorugroped_intro == False:
                    hint "He introduced her as a model! But she is also Obo's wife and working with them?" with vpunch
                    hint "What in the world is going on here..."
                hint "She seemed nice though, maybe I can get to meet her again at some point..."
            show boruto angry with dissolve
            bo "Relax Obo, I'm just going to make sure she settles in for her first day."
            show boss laugh with dissolve
            obo "Bah hahah! I'm just busting your balls kid, you can tag along if you want." with vpunch
            show boss normal with dissolve:
                xzoom -1
            obo "Right this way miss [hin_name]! Let's not waste any more time!"
            show boss:
                easeout 3 xpos 3000
            show shina:
                easeout 3 xpos 3000
            show boruto suspicious with dissolve
            bot "What are you up to, you old fuck...?"
            show boruto:
                easeout 3 xpos 3000
            pause 0.3
            jump v21_ramenintro_hinata_domfollow

        "She'll be fine, she can handle herself":
            show boruto smirk with dissolve
            bot "Ah, I'm sure she can handle herself just fine..."
            bot "I don't need to be hovering over her every second of the day and constantly holding her hand!"
            show boruto normal with dissolve
            show boruto normal at smallshake
            bo "I'll let you two handle things from here then, I'm going to see if Yoru needs any help in the kitchen."
            if yoruichi_modelling_completed == True:
                hint "Yoru...? Where have I heard that name before..."
            show boss laugh with dissolve
            obo "Good thinking kid, keep my wife company while we take care of... business!"
            if yoruichi_modelling_completed == True:
                hint "Wait... Isn't that the pretty woman that [bo_name] brought home the other day?"
                if yorugroped_intro == True:
                    hint "He introduced her as his girlfriend! But she is also Obo's wife?!" with vpunch
                    hint "What in the world is going on here... He must have just been messing with me..."
                if yorugroped_intro == False:
                    hint "He introduced her as a model! But she is also Obo's wife and working with them?"
                    hint "What in the world is going on here..."
                hint "She seemed nice though, maybe I can get to meet her again at some point..."
            show boruto smirk with dissolve
            bo "I'll come check up on you soon [hin_rel], good luck!"
            show shina shy with dissolve:
                xzoom -1
            hin "Y-yes, okay... Th-thank you [bo_name]..."
            show boss normal with dissolve:
                xzoom -1
            obo "Right this way miss [hin_name]! Let's not waste any more time!"
            show boss:
                easeout 3 xpos 3000
            show shina:
                xzoom 1
                easeout 3 xpos 3000
            show boruto:
                easein 3 xalign 0.5
            "You watch as they leave together, headed towards the far back of the establishment."
            bot "I wonder what the uniform looks like, I'll keep my eye out for it when they come back out."
            show boruto sceeming with dissolve
            bot "Waitresses are always so hot, I bet she'll look amazing in it!" with vpunch
            show boruto:
                easeout 3 xpos 3000
            pause 0.3
            scene black with dissolve
            "You make your way to the kitchen to check on Yoruichi and help prepare some of the food orders."
            "..."
            "Some time passes, and you still haven't seen or heard anything from [hin_name] and Obo."
            scene ramenkitchen
            show boruto worried at center
            with dissolve
            bot "I wonder what's taking them so long..."
            show boruto surprised2 with dissolve
            bot "Are they really still in the back room? I hope everything's alright!" with vpunch
            show boruto suspicious with dissolve
            bot "Maybe I should go check on them..."
            show boruto:
                easeout 3 xpos -3000
            pause 0.3
            scene black with dissolve
            "You make your way towards the rear end of the shop, looking for any sign of them."
            scene v21_boruto_rameneavesdrop with dissolve
            "You reach the far back room and place your ear to the door, trying to hear if there's anything going on inside."
            bot "Are they in here? I can't seem to hear anything..."
            bot "I don't want to barge in on them if they're busy, but I should at least make sure everything's okay..."
            scene black with dissolve
            "You lower your head to the keyhole and try to take a peek inside..."


            show screen peeking1024("v21_obo_helping_hinata")
            show screen peaking_overlay("bgp peak_updown")
            show layer screens at dizzyflash
            with longerflash
            call showscrollingimage from _call_showscrollingimage_301
            $ renpy.sound.play("/audio/soun_fx/heartbeatlong.opus", channel="sfx2", loop=True, relative_volume = 0.5)
            bot "Huh...?"
            "To your surprise, you see Obo kneeling in front of [hin_name], touching and grabbing her garments."
            "She appears to now be dressed in a very flimsy and revealing purple outfit, her breasts practically spilling out inches away from his face!"
            bot "W-what the hell?!" with vpunch
            bot "That's what he is having her wear?!"
            bot "It's kinda hot but... What the fuck is he doing inside there with [hin_rel]?!"
            bot "That bastard can't keep his hands to himself!"
            scene black with dissolve
            call hidescrollingimage("Click twice to stop peeking!") from _call_hidescrollingimage_246
            stop sfx2 fadeout 2
            bot "I need to do something... But what?!" with vpunch
            "You return to the kitchen before making any rash decisions to contemplate how to proceed."

            scene ramenkitchen
            show boruto angry at center
            with dissolve
            bot "I knew that turd was up to no good!"
            bot "Trying to get all over her at the first opportunity..."
            show boruto angry2 with dissolve
            bot "[hin_rel] was just letting him do it too, why was she allowing it?!" with vpunch
            show boruto suspicious with dissolve
            bot "What should I even do..."
            show boruto angry with dissolve
            bot "If I confront him, it might ruin her chances of working here... \nOr maybe even get me fired too!"
            show boruto at smallshake
            bot "But if I don't do anything, who knows what Obo is capable of doing..." 
            show boruto furious with dissolve
            bot "FUCK!" with vpunch
            show boruto angry with dissolve
            bot "I'll have to just keep an eye on things for now..."
            bot "[hin_rel] is no pushover, she can handle herself if things get out of hand."

            show boruto worried with dissolve
            bot "Or at least I hope so..."
            scene black with dissolve
            bot "[hin_rel]..."
            bot "What have I gotten you into?"
            "You keep yourself busy, vigilant and on edge, preoccupied with the orders that have started to flood in as customers start to fill up the tavern."
            "..."
            "Soon after, Obo and [hin_name] finally emerge from the back room, trays of drinks thrust into her hands and ready to start her first day of work."
            jump v21_ramenintro_firstday


label v21_ramenintro_hinata_domfollow:
    scene black with dissolve
    "You follow them to the back of the establishment, where Obo leads [hin_name] to the door of a secluded room past the kitchen."
    scene ramenkitchen with dissolve
    show boss normal at right behind shina with dissolve:
        xpos 1500
    show shina shy:
        xzoom -1 xpos 2000
    show boruto normal:
        xpos 2000
    show boss:
        easein 2 xalign 1.0
    obo "Nobody will bother you back here, the outfit should be on the counter inside so take your time getting changed."
    show shina:
        easein 1.8 xalign 0.0
    hin "O-okay, in here...?"
    hin "I'll just be a moment then."
    show shina:
        easeout 2 xpos -2000
    show boss:
        easein 2 xalign 0.0
    show boruto normal:
        easein 2 xalign 1.0
    pause 0.2
    $ renpy.sound.play("/audio/soun_fx/doorclose.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    "You wait outside with Obo as [hin_name] enters and shuts the door behind her."
    show boss angry2 with dissolve:
        xzoom -1
    "Obo starts silently eyeing you up and down, clearly irritated of your presence here."
    show boruto angry with dissolve
    bot "The fuck is this ugly asshat staring at me for?"
    show boruto surprised2 with dissolve
    "After a few moments, you hear [hin_name] call out to you."
    hin "[bo_name_stutter]? Could you come inside and take a look?"
    show boruto smirk with dissolve
    bo "Of course, coming [hin_rel]!"
    show boruto:
        easeout 2 xpos -2000
    pause 0.4
    show boss with dissolve:
        xzoom 1
    pause 0.2
    $ renpy.sound.play("/audio/soun_fx/doorclose.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    scene black with dissolve
    "You step inside the back room, closing the door behind you."
    show v21_ramen_domdressreveal:
        yalign 1.0 xalign 0.5
    with dissolve
    show v21_ramen_domdressreveal:
        ease 7 subpixel True yalign 0.1
    "Before you, [hin_name] is now standing in a very revealing and flimsy purple outfit."
    "She gazes at you with clear uncertainty in her eyes, trying to gauge your reaction to her garments."
    show screen parallax1280("v21_ramen_domdressreveal",1,0.1) with dissolve
    call showscrollingimage from _call_showscrollingimage_302
    bo "Whoa... That's what he had prepared for you?!" with vpunch
    bot "No wonder he didn't seem to want me around, Obo was probably hoping to get a private show out of her changing into this..."
    call increaselust(10) from _call_increaselust_297
    bot "She looks so fucking hot!" with vpunch
    bot "I have to stop myself from staring or she might get uncomfortable..."
    bot "But damn, I want to run my hands all over her body right now!" with vpunch
    hin "Y-yes, that's what he put here for me... \nIs this n-normal for this kind of work?"
    hin "I feel so... E-exposed..."
    bo "It's definitely not what I expected, but I do think it looks great on you!"
    bot "Those tits look even softer than usual, and her smooth thighs are completely visible up to her ass almost!" with dissolve
    bot "It puts everything on display! Nothing holding back at all..." with vpunch
    hin "R-really? And I'm supposed to be serving food and drinks with everyone looking at me like t-this?"
    bot "She has a point, is this just Obo's sick idea to get her oggled by all the customers?"
    bot "Even I'm not comfortable with her being in front of all those strangers like this... And I'm not even the one wearing the damn thing!"
    bo "Well, I guess it's not the most practical outfit [hin_rel]..."
    bo "But hey, it's part of the job right? I guess you need to look appealing to attract customers and all that."
    hin "I s-suppose so..."
    scene v21_boruto_helping_hinata with dissolve:
        yalign 1.0
    bo "Here let me help you out with it..."
    call hidescrollingimage("Click twice to adjust her outfit!") from _call_hidescrollingimage_247
    "You kneel down in front of her and adjust her apron for her, making sure it's on properly."
    bo "There, that should do it. Keep it all tightly wrapped up!"
    hin "[bo_name_stutter]..."
    hin "Do you t-think me working here is a good idea? I'm starting to have some doubts..."
    bo "You'll be fine [hin_rel], just give it a chance! \nWe could really use the extra money right now."
    show v21_boruto_helping_hinata:
        ease 5 subpixel True yalign 0.2
    hin "Yeah I g-guess, I have to at least try since I've come this far."
    hin "Thank you for being here with me sweetie..."
    hin "It's nice having you around to support me."
    bo "Of course [hin_rel], I'll always keep you close!"
    if dominance.level ==1:
        call changeDominance(1,"v21_ramenintro_hinatadomfollow1",1) from _call_changeDominance_132
    else:
        call changeDominance(1,"v21_ramenintro_hinatadomfollow2", 1, 2) from _call_changeDominance_133
    bot "Away from trouble, and away from anyone that tries to take what's mine away from me!" with vpunch
    scene black with dissolve
    obo "Hey! What's the hold-up, you two done in there yet?!" with vpunch
    $ renpy.sound.play("/audio/soun_fx/dooropen.opus", channel="sfx3", loop=False, relative_volume = 0.6)
    "Obo's impatient voice calls out from outside the door, as you scramble to your feet and follow [hin_name] back to him."
    scene ramenkitchen 
    show boss normal at right
    with dissolve
    show rhina normal1:
        xzoom -1 xpos -2000
    show boruto normal behind rhina:
        xzoom -1 xpos -2000
    show rhina:
        easein 2 xalign 0.3
    show boruto normal:
        easein 3 xalign 0.0
    hin "All done, sorry for the wait!"
    obo "The outfit looks like it fits, so it's time to get to work!"
    show boss angry2 with dissolve:
        xzoom 1
    obo "Customers are getting restless!" with vpunch
    show boruto surprised2 with dissolve:
        xzoom -1 
    bo "Y-yeah, we're ready. I'll go ahead and get started here in the kitchen."
    show boruto smirk with dissolve
    bo "I'll catch you later [hin_rel], good luck!"
    show rhina smiling1 with dissolve
    hin "Y-yes... Th-thank you [bo_name]... See you soon!"
    show boruto:
        easeout 2 xpos 2000
    show rhina:
        easein 1 xalign 0.0
    show boss angry3 with dissolve
    obo "Good boy! Now get to it!" with vpunch
    show boss laugh with dissolve:
        xzoom 1
    obo "As for you miss [hin_name], let's get you out there and making me some money! Baha-hahah!"
    show boss at smallshake
    "You take your leave and begin your shift in the kitchen to start helping out with the orders."
    show rhina thinking1 with dissolve
    show boss at smallshake
    "[hin_name] stays a while longer to receive her instructions for the day from Obo, absorbing as much information as she can."
    scene black with dissolve
    "She then takes a deep breath before exiting the kitchen to prepare herself for what's to come."
    "Heading out to the front of the shop with trays of drinks, [hin_name] is ready to start her first shift!"

    
label v21_ramenintro_firstday:
    $ renpy.sound.play("/audio/soun_fx/backgroundchatting.opus", channel="ambience", loop=True, fadein = 1, relative_volume = 0.5)
    stop music fadeout 2
    show v21_hinata_ramenintro_serve with dissolve:
        fit "contain" xalign 0.05
    "The moment [hin_name] stepped out of the kitchen, the crowd's murmurs started growing louder and louder..."
    "The tavern, now full of customers, buzzes with excitement and chatter at the sight of her."
    "Customer Whispering" "H-hey! Isn't that..."
    "Customer talking" "Her... at a place like this? Impossible..."
    show v21_hinata_ramenintro_serve_1:
        zoom 0.58 xalign 0.95
    show v21_hinata_ramenintro_serve:
        alpha 0.3
    with dissolve
    "Handsy Customer" "I wouldn't mistake those curves for anyone else's..."
    "Handsy Customer" "It really is her!"
    "Drunken Customer" "It's true! Lady [hin_name] is our barmaid! *Hic!*"
    scene black with vpunch
    $ renpy.sound.play("/audio/soun_fx/wineglassclink.opus",channel="sfx4",loop=False,relative_volume=1)
    "Drunken Customer" "A cause for celebration, another round on me!" with vpunch
    show bg ramenwork with dissolve:
        zoom 0.96
    show bg:
        blur 5
    show rhina working_normal1 at left
    with dissolve
    hint"So m-many people! W-what are they all saying...?"
    show rhina at smallshake
    hint"It feels like everyone is staring at me!"
    show rboy angry1 at right behind rhina with dissolve:
        xpos 2000
    show rboy:
        easein 2 xpos 1300
    "???" "Lady [hin_name]... Is it not?"
    hint"H-huh? A young boy...?"
    show rhina working_smiling1 with dissolve
    hin"Y-yes that's me... And you are?"
    "???" "I have no name..."
    show rhina working_normal1 with dissolve
    hin"H-huh?"
    "???" "My moma is dead, my father has disowned me..."
    show rhina working_sad1 with dissolve
    hint"Poor boy! To be left alone orphaned in this world..."
    hint "He looks so sad... But why is he coming up to me of all people?"
    show rboy at smallshake
    "???" "If that were not enough, your [hin_rel_to_bo]..."
    show rhina working_normal1 with dissolve
    hin"[bo_name]? Are you two... f-friends?"
    show rboy crying1 with dissolve
    "???" "Friends? No... *Sniffles*"
    hint"Is he... c-crying?"
    "???" "Your [hin_rel_to_bo] is..."
    show rboy at smallshake
    "???" "He is a big meanie and a bully! *Sniffles*"
    hin"Are you s-sure? [bo_name] would never-" with vpunch
    show rboy:
        easein 1.5 xpos 600
    pause 0.8
    scene black with dissolve
    if persistent.netorareoptional == True: #if NTR disabled
        call ntrwarning_skip from _call_ntrwarning_skip
        scene black with dissolve
        "The boy leans in for a comforting hug..."
        hin"There, there... Everything will be alright!"
    else:
        show v21_ramenboy_intro_1 with dissolve:
            yalign 0.0
        show v21_ramenboy_intro_1:
            easein 5 yalign 1.0
        hin"H-hey, wait a second! I am working right now..."
        hint "What is going on...?"
    if persistent.netorareoptional == True: #if NTR disabled
        "???" "*Sniffles* He is a bully! He made my life a living hell... But you are nice, aren't you?"
        hint "This boy... His hand is on my- what is he trying to do..."
        hin"It's okay, you don't have to cry. I'll talk to him about it, you two will be friends in no time!"
        "???" "T-thank you, nice lady. *sniffles* But it's not fair that he has a moma as pretty as you!"
        hin"H-huh...?"
        "???" "Can you be my moma too!?" with vpunch
        hint "I don't know who this is, but he's getting a little too close for comfort..."
        hin"Please let go of me, I'm working right now..."
        $ renpy.sound.play("/audio/soun_fx//glasssmash.opus", channel="sfx3", loop=False, relative_volume = 0.3)
        "The scheming young man releases [hin_name] from his embrace, but not before bumping into her causing her to drop her tray!"
    else:
        "???" "*Sniffles* He is a bully! He made my life a living hell... \nBut you are nice, aren't you?"
        hint "This boy... His hand is on my-... What is he trying to do..."
        hin"It's okay, you don't have to cry. I'll talk to him about it, you two will be friends in no time!"
        "???" "T-thank you, nice lady. *sniffles* But it's not fair that he has a moma as pretty as you!"
        hin"H-huh...?"
        show v21_ramenboy_intro_2 with dissolve
        $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx3", loop=False, relative_volume = 1.1)
        $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx2", loop=False, relative_volume = 0.6)
        "???" "Can you be my moma too!?" with vpunch
        scene black with vpunch
        $ renpy.sound.play("/audio/soun_fx//glasssmash.opus", channel="sfx3", loop=False, relative_volume = 0.3)
        "The scheming young man slid his fingers where they didn't belong, startling [hin_name] and causing her to drop her tray!"
    show bg ramenwork with dissolve:
        zoom 0.96
    show bg:
        blur 5
    show rboy smirk1 at center
    if persistent.netorareoptional == True: #if NTR disabled
        show rhina angry2 at right behind rboy
    else:
        show rhina ass2 at right behind rboy
    show rboy:
        easeout 2 xpos -2000
    with dissolve
    "???" "Hihihi! I am outie!"
    show rhina angry2 with dissolve:
        easein 3 xalign 0.5
    hin "Hey kid! What the hell was that?!" with vpunch
    show rhina serious1 with dissolve
    hint "Great, now look at the mess I've made..."
    hint "What a disaster to have on my first day!" with vpunch
    show rhina concerned1 with dissolve
    hint "I better start cleaning this up before Obo gets mad..."
    scene black with dissolve
    hint "Unbelievable... *sigh*"


    label v21_ramenintro_firstday_clean:
        scene black
        show v21_hinata_ramenintro_clean with dissolve:
            fit "contain" xalign 0.05
        "[hin_name] kneels down to start cleaning up the spilled drinks and broken glass from the floor."
        "Very conscious of the eyes of the customers on her, she tries to hurry and get the mess cleaned up as quickly as possible."
        "Whispering Customers" "Look at her go..."
        "Customer Behind" "She's putting on a show just for me!"
        show v21_hinata_ramenintro_clean2:
            zoom 0.58 xalign 0.95
        show v21_hinata_ramenintro_clean:
            alpha 0.3
        with dissolve
        "Drunken Customer" "That juicy ass on display can only mean one thing...*Hic!*"
        $ renpy.sound.play("/audio/soun_fx/wineglassclink.opus",channel="sfx4",loop=False,relative_volume=1)
        "Drunken Customer" "Another round for everyone on me!" with vpunch
        "Crowd Cheering" "Hoorah!" with vpunch
        "Feeling humiliated and painfully aware of how little her outfit covers, [hin_name] scrambles to finish before she has to endure any more of the crowd's chants."
        scene black with dissolve
        hint "It's alright, just ignore them and do your job, come on..."
        show v21_hinata_ramenintro_serve_3 with dissolve:
            fit "contain" xalign 0.05
        "Having finished she climbs back to her feet and starts to fetch more drinks for the customers."
        "Random Customer" "There she is again, we missed you baby!"
        "Rude Customer" "Yeah don't leave us hanging, shake that ass for us!"
        "Perverted Customer" "You think she'd spit in my beer if I asked her to?"
        show v21_hinata_ramenintro_serve_4:
            zoom 0.58 xalign 0.95
        show v21_hinata_ramenintro_serve_3:
            alpha 0.3
        with dissolve
        hint "Obo wasn't lying, the crowd really does get out of hand..."
        hint "I wonder if this is what every shift here is like?"
        hint "I guess I'll just have to get used to it..."
        scene black with dissolve
        "Handsy Customer" "Hey sexy, can I order a side dish of you?"
        show v21_hinata_ramenintro_customer_grope with vpunch:
            fit "contain" xalign 0.5
        $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx2", loop=False, relative_volume = 0.6)
        $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx2", loop=False, relative_volume = 1.1)
        "Fueled by the crowd's energy, one particular elderly customer decides to take things a step further and grabs [hin_name]'s ass as she passes by."
        "Handsy Customer" "Fuck yeah, that's some premium ass right there!"
        $ renpy.sound.play("/audio/soun_fx/oldman_laugh9.opus", channel="sfx2", loop=False, relative_volume = 0.5)
        "Handsy Customer" "Hehehe... So how much are you gonna cost me, sugar tits?"
        show v21_hinata_ramenintro_customer_slap with flash:
            fit "contain" xalign 0.5 yalign 0.5
        show v21_hinata_ramenintro_customer_grope:
            alpha 0.3
        with vpunch
        $ renpy.sound.play("/audio/soun_fx/slapecho.opus", channel="sfx2", loop=False, relative_volume = 1.5)
        "[hin_name] immediately spins around, her eyes blazing with anger as the resulting slap echoes across the whole room."
        "Handsy Customer" "Oiii...!"
        hin "How dare you put your hands on me?! I will not tolerate this for even one second!" with vpunch
        scene bg ramenwork
        show rhina angry2 at right
        show rold caught1 at left:
            xzoom -1
        with dissolve
        "Handsy Customer" "Oh come on sweet cheeks, you can't tell me you didn't like it!"
        show rold at smallshake
        "Handsy Customer" "I like 'em feisty! Come give daddy another handful of that ass!"
        show rhina angry3 behind boss with dissolve
        hin "You filthy swine! I should kill you right where you sta-..."
        show boss angry2:
            xpos 2000
        show boss:
            easein 1 xalign 0.8
        obo "What in the nine hells is going on here?!" with vpunch
        show boss:
            xzoom -1 
            ease 1 xalign 0.3
        show rhina angry1
        show rold normal1
        with dissolve
        hin "This impotent rat here thought he could touch me as he pleases!"
        show rhina angry2 with dissolve
        hin "I will not have any grubby hands on me without breaking their attached limbs!" with vpunch
        show boss angry with dissolve
        show boss:
            ease 1 xalign 0.6
        obo "Is this true? You've been harassing my new employee tonight?"
        show rold pervert1 with dissolve
        "Handsy Customer" "Well what's the point of showing all that cake if I can't have a taste? Mmmmm..."
        show rold at smallshake
        "Handsy Customer" "And oh boy, do I love my desserts!"
        show boss angry3:
            xzoom 1
        with dissolve
        obo "That's it, you're done!" with vpunch
        show rold caught1 with dissolve
        show boss:
            ease 1 xalign 0.4
        show rold:
            ease 1 xalign -0.2
        obo "Get the hell out of my shop before I snap you in half like a twig!"
        show rold at smallshake
        "Handsy Customer" "W-what?! I pay good money to come here and enjoy myself!"
        show rold pervert1 with dissolve
        "Handsy Customer" "Is nowhere safe anymore to enjoy the sweet fruits of life? \nWhat has society come to?! Hehehe..."
        show rold:
            ease 1 xpos -2000
        show boss:
            ease 1 xalign 0.0
        obo "I said get out!" with vpunch
        show boss normal with dissolve:
            xzoom -1
        obo "I'm sorry miss [hin_name], I should have been keeping a closer eye on things..."
        obo "Are you alright?"
        show rhina angry1 with dissolve
        hin "I could be a lot better, that's for sure!"
        show rhina at smallshake
        hin "Is this what I'm going to have to put up with every shift here?! \nLike an animal at the zoo to be pet by anyone who wants it enough?"
        show boss angry2 with dissolve:
            ease 1 xalign 0.2
        obo "I assure you, I do not condone that kind of behavior in my establishment!"
        show boss with dissolve:
            xzoom 1
            ease 1 xalign 0.0
        obo "While it is true that waitresses often flirt and physically tease customers to get tips from drunk men with more cash than sense..."
        show boss at smallshake
        obo "I will not allow anyone to take advantage of my employees against their consent!"
        show rhina thinking1 with dissolve
        hin "C-consent? They w-willingly allow themselves to be defiled like that for extra money...?"
        show rhina serious1 with dissolve
        hin "I could never imagine myself stooping to that level... \nI'm starting to think this is not the right job for me after all."
        show boss normal with dissolve:
            xzoom -1
        obo "Nonsense! Yer doing a great job so far, and you have my word that you will never have to put up with anything you don't want to."
        show boss:
            ease 1 xalign 0.3
        $ renpy.sound.play("/audio/soun_fx/backgroundchatting.opus", channel="ambience", loop=True, relative_volume = 0.3)
        obo "Come on, let's not stand around and wait for the grass to grow. \nYour shift is coming to an end, but it's not over yet!"
        show boss behind rhina:
            easeout 2 xpos 3000
        show rhina:
            easeout 2 xpos 3000
        pause 0.3
        scene black with dissolve
        $ renpy.music.set_volume(0.5, delay=2, channel='ambience')        
        "[hin_name] reluctantly resumes her duties and continues bringing out food and beverages to customers."
        "Having seen the outburst and full spectacle, the crowd has quieted down considerably, and she manages to get through the rest of her shift without any more incidents."
        "Obo's words continue circling in her mind as she internally contemplates the situation she finds herself in."
        stop ambience fadeout 2
        $ renpy.end_replay()




    $ playmusic("/audio/ost/market.opus", volume=0.7)
    "Meanwhile..."

    scene bg ramentoilet
    show rboy smirk1 at center
    with dissolve
    "???" "Turns out this little mission may end up being fun after all!"
    "???" "I had no idea the target's [hin_rel] was so fucking hot!"
    scene black with dissolve
    "???" "Hihihi..."


label v21_ramenintro_firstday_end:
    scene v21_hinata_ramenintro_shiftend with dissolve:
        yalign 1.0
    show v21_hinata_ramenintro_shiftend:
        easein 5 yalign 0.1 subpixel True
    default hinata_maidoutfit_unlocked = False
    if hinata_maidoutfit_unlocked == False:
        $ notification(f"{hin_name}'s maid outfit unlocked!")
    $ hinata_maidoutfit_unlocked = True
    "As the night comes to a close, [hin_name] finally finishes her last assigned cleaning duties."
    "Her mind still processing everything that had occurred during her first shift, she sighs in relief as she looks forward to finally returning home to rest."
    hint "Is this really what it's going to take to support my family...?"
    hint "Must I allow myself to be subjected to this debacle daily?"
    hint "Although it's not like I have much of a choice right now..."
    hint "At the very least, Obo seems like a nice man.{p}He did stand up for me back there..."
    $ notification (f"{hin_name}'s Obedience Level has reached level 2! The stat has been reset to 0.")
    $ hinata_obedience.level = 2
    $ hinata_obedience.value = 0
    hint"*Sigh...*"
    hint "Nothing is more important than keeping [bo_name] and [him_name] safe!"
    hint "No matter the cost, I must endure it for their sake!" with vpunch
    scene black with dissolve
    hint "Gods have mercy on us all..."
    "..."
    scene ramenkitchen
    show boruto smirk at right with dissolve
    bo "There you are!"
    show rhina shy2 at left with dissolve:
        zoom 1.05
    hin"[bo_name_stutter]..."
    hint"To be working around my [hin_rel_to_bo] dressed like this...{p}It cannot be right!"
    show boruto smirk2 with dissolve
    bot"That outfit. [hin_rel] is looking fucking sexy in it!{p}I hope people around this place won't get as excited as I am!"
    bo "Hey [hin_rel], done for the day? How did it go?"
    show rhina shy1 
    show boruto surprised2 
    with dissolve
    hin "H-horribly... *Sigh*"
    show rhina shy2 with dissolve

    hin "I-I... I don't really want to talk about it right now [bo_name]..."
    hin "I just want to get out of this uniform and go home."
    show boruto worried with dissolve
    bo "Oh... Okay, I understand. You must be exhausted after your first day."
    bot "Damn, she looks like she went through hell..." with dissolve
    bot "What happened to her?!" with vpunch
    bot "I should probably be more aware of what goes on around here next time... Maybe I can step in and make it easier for her."
    show boruto angry with dissolve
    bot "That bastard Obo better not be behind all this!" with vpunch
    show rhina shy1 with dissolve
    hin "[bo_name_stutter]... \nC-can we just go home now please?"
    show boruto smirk with dissolve
    bo "Of course [hin_rel]! Come, let's get out of here!"
    $ notification("Quest updated")
    if not _in_replay:
        $ quest.check("job2_4", "completed")
        $ quest.check("job2_5", "in progress")
    show boruto behind rhina:
        easein 2 xalign 0.5
    bo "Hang in there [hin_rel], everything's going to be alright!"
    show rhina:
        xzoom -1
        easeout 2 xpos -2000
    show boruto:
        easeout 2 xpos -2000
    pause 0.3
    scene black with dissolve
    "You and [hin_name] leave the ramen shop after she finishes getting changed out of her work outfit, heading straight home for the night."
    "You can now have [hin_name] pick up work over at the ramen shop. {p}Speak to Obo once you visit the ramen shop to do so."
    jump action_taken

    







#     #todo toilet scene (I will pr)
#     scene bg ramentoilet
#     show rhina shy2 at center
#     with dissolve
#     hint"Unisex bathrooms, eh? Lucky no one is here..."
#     scene black with dissolve
#     hint"I better make this quick..."
#     scene p0 with dissolve:
#         yalign 0.0
#     show p0:
#         easein 5 yalign 1.0
#     hint"Y-yuck! Cracked walls, and... what is up with the holes?"
#     call showscrollingimage
#     show screen parallax1280("p0",1,0.5) with dissolve
#     hint"At least the toilet seems clean..."
#     $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 0.7)
#     hide screen parallax1280
#     show screen parallax1280("p0_1",1,0.0)
#     with dissolve
#     hint"..."
#     call hidescrollingimage
#     "blabla"


