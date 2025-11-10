default v21_hinatadate_daycounter = 3 # Counter for the number of days since the last date, to prevent spamming - 1 date per two days
default v21_hinatadate_progression = 0 # Allows control over replayable progression and some flavour dialogue outside of scene according to previous date - 1 normal replay, 2 sakura footrub, 3 hinata stargazing, 4 hinata fall asleep
default v21_sakuradinner_footdenied = False
default v21_dinnerdate_hinata_assgrabbed = False
default v21_dinnerdate_sakura_assgrabbed = False

    # Start of the scene sequence at 'lr_massage_menu'
    # Requirement: Day 14+
    # Requirement: Love/Hate path chosen

label v21_hinatadate_quest_start:
    bo "Is everything alright, [hin_rel]? You seem a little... distant."
    scene hina nightmassage2 with dissolve:
        zoom 1.25 xalign 0.5 yalign 1.0
    show hina nightmassage2:
        easein 5 yalign 0.0
    hin "Oh! [bo_name]... Yes dear, I'm fine."
    hin "It's just... with everything that's been happening..."
    bo "With the Daimyo's demands and [na_rel]'s absence you mean?"
    hin "Y-yeah... I've just been trying to wrap my head around it all."
    hin "The circumstances are definitely not ideal, putting us in quite the predicament."
    hin "Maybe it's time for me to pick up some work alongside my housekeeping..."
    hint "But what would that job be..." with dissolve
    "Her voice trails off as she is lost again in thought."
    bo "... [hin_rel]?"
    menu:
        "{color=[lovecolor]}Try to calm her down{/color}":
            bo "I know you're strong, but not even you can handle everything at once."
            bo "You shouldn't stress yourself out like this so much!"
            hin "I know, You're right about that. It's definitely not healthy..."
            hin "But right now I don't have much of a choice, my focus is on finding a better solution for all of us."
            bo "I get it [hin_rel], but you also need to take care of yourself."
            hin "There will be time for that once all this has passed."
            hin "Now if you'll excuse me [bo_name], I'm going to go lay down a bit."
            bo "Of course, [hin_rel]. Get some rest if you need to."
            scene black with dissolve
            call changeLove("Hinata", 1) from _call_changeLove_69 
            "[hin_name] gives you a gentle smile before heading upstairs to retire to her bedroom."
            scene bg lr night:
                zoom 0.69
            show boruto normal at center
            with dissolve
            bo "..."
            bo "It's not like [hin_rel] to be so disconnected."
            show boruto worried with dissolve
            bo "I know things aren't that great right now, but I'm more worried about her."
            bo "I should find a way to raise her spirits and take her mind off things a bit."
            show boruto smirk with dissolve
            bo "An evening dedicated to making her smile again sounds perfect."
            bo "I bet Auntie Sakura will know how to help with that. She knows [hin_rel] better than anyone!"
            $ notification ("Quest updated")
            if quest_hin.is_state("1_hin2L", "pending"):
                $ quest_hin.check("1_hin2L", "in progress")
            bo "I should go ask her when I find the time, maybe we could even go visit her together."
            scene black with fade
            bot "Hang in there [hin_rel]..."
            jump action_taken

        "{color=[hatredcolor]}Scold her for being dramatic{/color}":
            bo "Don't you think you're overreacting a little?"
            bo "It's not that deep, we'll just deal with things as they come along."
            hin "I wish it was that simple [bo_name], something about this all just doesn't sit right with me..."
            bo "I thought you were stronger than that [hin_rel], but here you are, worrying about every minor inconvenience."
            bo "It's a little pathetic, I'm not going to lie, I expected more from you!"
            hin "P-pathetic?!" with vpunch
            hin "[bo_name]! Watch your tone when addressing your [hin_rel_mother]!"
            bo "Alright, alright... Calm down already..."
            bo "I just don't get what you're so worried about."
            bo "It's me who's busting my ass anyway!"
            hin "Language! I think you're gravely mistaken for minimizing all these events in such a manner..."
            hin "If you were a little older, a little wiser, you'd understand how fast things can spiral out of control. You shouldn't discount my concerns like that!"
            bo "How dramatic, I guess it must be that time of the month again for you..."
            $ renpy.sound.play("/audio/soun_fx/mgsalert.opus", channel="sfx3", loop=False, relative_volume = 0.9)
            hin "Excuse me?!" with vpunch
            scene black with dissolve
            "[hin_name] gets up from the couch and glares at you with a piercing look, clearly not amused by your comments."
            scene bg lr night:
                zoom 0.69
            show shina angry at left
            show boruto smirk at right
            with dissolve
            show shina at smallshake
            hin "I don't know what's gotten into you tonight but I'm not in the mood to entertain this behavior any longer!"
            show shina assertive with dissolve
            hin "I need to go lay down, tidy up after yourself when you're done here."
            show shina with dissolve:
                xzoom -1 
            show shina:
                easeout 2 xpos -600
            "[hin_name] swiftly turns her back to you before stomping back upstairs to retire to her bedroom."
            show boruto smirk2 with dissolve
            show boruto:
                easein 1 xalign 0.5
            bot "She's pretty easy to rile up, isn't she?"
            bot "Everything going on must be overwhelming and making her sensitive."
            show boruto sceeming with dissolve
            call changeHatred(1,statlevel=2) from _call_changeHatred_222
            bot "I wonder if I could use this to my advantage somehow..."
            bot "I'll see if I can come up with a way for her to 'relax' and lower her guard."
            bot "Nothing loosens up a woman more than a fun night out!"
            show boruto sceeming 2 with dissolve
            bot "I bet Auntie Sakura could help with that. She knows [hin_rel] better than anyone!"
            bot "She's always been the adventurous one, and knows how to have a good time. Hehe..."
            if wine_counter >= 1:
                bo "Spending time with her late at night has been a blast! She's so hot..."
            
            if quest_hin.is_state("2_hin2H", "pending"):
                $ notification ("Quest updated")
                $ quest_hin.check("2_hin2H", "in progress")
            bot "I should go ask her when I find the time, maybe we could even go visit her together."
            scene black with fade
            bot "Just you wait [hin_rel]..."
            jump action_taken




label v21_hinatadate_quest_start_sakura:
    # Requirement: Completed at least one wine date with Sakura - wine_counter >=1
    show boruto normal with dissolve
    bo "Actually Auntie, I came to talk to you about [hin_rel]!"
    show sakura shy with dissolve
    saku "Oh, about [hin_name]? Why sweetie, is something going on between the two of you?"
    show sakura angry with dissolve
    saku "You better not be giving her a hard time young man!" with vpunch
    show boruto embarassed with dissolve
    bo "N-no, no it's nothing like that!"
    show sakura teasing with dissolve
    saku "Okay goodie, I thought I was going to have to spank that tushy of yours for a second! *giggle*"
    show boruto sceeming with dissolve
    bot "You're the one with the tight spankable ass Auntie, but that's not what I'm here for today..." with dissolve
    show boruto smirk with dissolve
    bo "She's been under a lot of stress lately, so I've been thinking..."
    bo "I'd like to do something special for her and... you! \nTo help her loosen up a bit."
    bo "I wanted to include you too, since you've been such a supportive friend to the both of us!"
    show sakura at smallshake
    saku "How exciting! Of course, sweetie! I'm all ears, what were you thinking exactly?"
    show boruto smirk with dissolve
    bo "Perhaps a fun night out... to take our minds off things for a while."
    saku"Oooh...?"
    bo "We could come over for dinner. I'll bring your favorite wine, like last time!{p}We'll spend the night with some good food, and even greater company."
    show sakura greet with dissolve
    saku "Oh, that's a wonderful idea, [bo_name]! Count me in!"
    show sakura normal with dissolve
    saku "She's probably cooped up at home all day doing nothing but chores."
    show sakura teasing with dissolve
    saku "It's enough to make a woman lose her mind, ya know? \nDon't ask me how I know! *winks*"
    show boruto laughing with dissolve
    bo "I can only imagine..."
    show boruto sceeming with dissolve
    bot "I've seen that crazy side of yours already, Auntie. It turns me the fuck on!" with dissolve
    show sakura normal
    with dissolve
    saku "You've come to the right person though, [bo_name]!"
    saku "I'll gladly host dinner at my place for you cuties, I make a mean Tofu you know!"
    show sakura teasing with dissolve
    saku "But a nice dinner needs some excellent wine to go along with it! That always helps a woman unwind..."
    saku "Be sure to pick up some more of that good stuff, you remember which one I like, right? Hihi..."
    show boruto laughing with dissolve
    bo "Of course! How could I ever forget..."
    show boruto smirk with dissolve
    bot "That wine turned Auntie into an insatiable cougar! I wonder how it would affect [hin_rel]..." with dissolve
    bot "She usually never drinks, and always in moderation when she does."
    bot "But with Sakura around being the bad influence that she is..."
    show boruto smirk2 with dissolve
    bot "Who knows what might happen?" with vpunch
    show boruto smirk 
    show sakura normal 
    with dissolve
    saku "A handsome young man wining and dining two lonely yet beautiful women at the same time..."
    saku "You think you can handle us both for one night [bo_name]?"
    show boruto embarassed with dissolve
    bo "If I can handle you, I can handle anyone Auntie. I haven't heard a complaint from you yet!"
    show sakura teasing with dissolve
    saku "No, no you haven't... *giggle*"
    show sakura normal 
    show boruto smirk 
    with dissolve
    saku "So it's settled then, dinner and drinks here for the three of us!"
    saku "I'll make sure to prepare something special for [hin_name], and you're in charge of the wine mister."
    bo "Sounds good to me!"
    show sakura greet with dissolve
    saku "Oh and one more thing, some friendly advice if you will..."
    show sakura normal with dissolve
    saku "When a woman looks good, she {i}feels{/i} good too!"
    saku "Get [hin_name] to doll herself up a bit, will ya? I'll make sure to dress up for the occasion too!"
    saku "As modest as your [hin_rel_mother] is, even she would appreciate a gesture from you, and a reason to feel like a woman once more."
    saku "And with [na_name] not around, she probably hasn't had a reason to dress up in a while..."
    show boruto sad with dissolve
    bo "That's true, I can't even remember the last time I saw her in anything other than her training gear or sweater."
    show sakura greet with dissolve
    saku "Exactly, so that's where you come in! You have to step up and be the man of the house now!"
    saku "Encourage her and give her an excuse to let go a little and feel beautiful again."
    show sakura teasing with dissolve
    saku "Maybe guide her towards something elegant, yet comfortable? So that we can be matching!"
    show boruto normal with dissolve
    bot "Hmm, I recall seeing a dress that would suit [hin_rel] nicely at Tenten's shop. I should look into it..." with dissolve
    show boruto smirk with dissolve
    bo "I promise you won't be disappointed, you'll both look stunning and feel amazing."
    saku "Look at you, all confident and ready to impress! I like it!"
    show sakura normal with dissolve
    saku "Just make sure to have everything prepared, and then pop in together whenever you're ready."
    saku "I'll be waiting for you!"
    show boruto laughing with dissolve
    bo "Sure thing, see you soon then!"
    show sakura greet with dissolve
    show boruto:
        easeout 3 xpos -800
    saku "Bye sweetie!"

    if day_part == 0 or day_part == 1 or day_part == 2:
        $ renpy.sound.play("/audio/soun_fx/doorclose.opus", channel="sfx2", loop=False, relative_volume = 1.0)
        scene black with fade
        scene inohouse day 
        show boruto normal at center
        with dissolve
    else:
        $ renpy.sound.play("/audio/soun_fx/doorclose.opus", channel="sfx2", loop=False, relative_volume = 1.0)
        scene black with fade
        scene inohouse night
        show boruto normal at center
        with dissolve

    bo "Okay, this seems simple enough."
    bo "I just need to get some wine and find a dress to surprise [hin_rel] with, and Auntie will take care of everything else!"
    $ notification ("Quest updated")
    if quest_hin.is_state("1_hin2L", "in progress"):
        $ quest_hin.check("1_hin2L", "completed")
        $ quest_hin.check("2_hin2L", "in progress")
    if quest_hin.is_state("2_hin2H", "in progress"):
        $ quest_hin.check("2_hin2H", "completed")
        $ quest_hin.check("3_hin2H", "in progress")
    $ inventoryShop.update_item(f"Black Dress", price=100)

    show boruto smirk with dissolve
    bo "I can't wait to see how hot they look together all dressed up, this is going to be fun!"
    bo "Tenten should have everything at the shop I need to make it happen, as long as I have the cash for it."
    show boruto:
        easeout 3 xpos -200
    pause 0.5
    scene black with dissolve
    bo "No time to waste!"
    jump action_taken


label v21_hinatalovelevel2_date:

    # Requirements: Spoken to Sakura, have wine, dress, (v21_hinatadate_daycounter >= 3)
    # Auto trigger the first time when you enter living room with everything ready
    bo "Hey [hin_rel] guess what, I have a surprise for you!"
    hin "A s-surprise? [bo_name], what is it?"
    bo "Close your eyes for me!"
    scene black with dissolve
    hin "What are you up to this time..."
    $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    bo "No peeking!"
    hin "O-okay..."
    if not _in_replay and hinata_love.level < 2: 
        call useItem(blackdress,1) from _call_useItem_12
    scene v21_love_presenting with dissolve:
        yalign 1.0
    show v21_love_presenting:
        easein 5 yalign 0.0
    bo "Ta-daa!"
    hin"A... dress?"
    bo "I made sure to pick something modest that fits your style."
    if chosen_hate_path:
        bot "Or rather emphasize your slutty curves!"
    scene bg lr night:
        zoom 0.69
    show boruto snob at left
    show shina surprised at right
    with dissolve
    bo"So... what do you think?"
    show shina shy2 with dissolve
    hin "Oh, [bo_name]... It's a beautiful dress! But... why? W-what's this for exactly?"
    if chosen_hate_path:
        bo "Just thought you'd like something else besides your everyday rugs! And you know, maybe as an apology for my act lately..."
        bot "I know how easy you let things go, [hin_rel]! Now be a good little slut and dress up for me!"
    else:
        bo "Well it's for you to wear silly! What else?"
    show shina shy with dissolve
    "Her face lights up with excitement for a brief second before falling back into uncertainty."
    show shina shy2 with dissolve
    hin "This looks expensive though! Where did this even come from?"
    show shina at smallshake
    hin "You know that we really shouldn't be spending money like this right now..."
    bo "Don't worry about that at all! I have it all covered. Besides..."
    bo "With all that's going on, I thought you could use a break and so, I've prepared a special night for you!"
    show shina concerned with dissolve
    hin "A special night? You shouldn't have put in that effort for me, you are making your [hin_rel_mother] blush!"
    show shina smiling with dissolve
    hin "So... what were you thinking exactly? A date? *Giggles*"
    if chosen_hate_path:
        bo "Is that an invitation?"
        show shina at smallshake
        hin"It's just a joke, s-silly..."
        bot"Shame... Well maybe I should get you shit-faced drunk anyway, and then it'd be more than a 'date'!"
        hin"So, you were saying...?"
    else:
        bo "Not quite, but..."
    bo "Auntie Sakura is hosting dinner for us tonight, and I wanted you to look your absolute best!"
    show shina shy2 with dissolve
    hin "O-oh... Dinner at Sakura's, eh? You should have told me earlier so I could prepare!"
    bo "Well then it wouldn't be much of a surprise now, would it?"
    bo "Come on, the night won't wait around for us! You should go get ready now!"
    bo "I'll wait for you down here and then we can make our way there together."
    show shina shy with dissolve
    hin "I don't k-know about this dress though... Is it not too much for a dinner party?"
    bo "Not at all, in fact it was Sakura's idea to dress up, and you know she won't be holding back herself, so..."
    show shina shy with dissolve
    hin "Is that right..."
    bo "You'll look stunning, and I know Auntie Sakura will love to see you glowing too."
    hin "Hmm..."
    if chosen_hate_path:
        bot "Come on, [hin_rel]! Stop being a cocktease and slide into that dress!" with dissolve
        bot "Can't wait to see how your ass sticks out behind that tight waistline!"
    else: 
        bot "She is considering it! I can't wait to see all your curves pop out [hin_rel]!" with dissolve
    show shina smiling with dissolve
    hin "Alright then, wouldn't hurt to try it on anyways... Give me some time to dress up before we get going, will you?"
    hide shina with dissolve
    "She disappears upstairs into her room for a while..."
    scene black with dissolve
    bot "Can't wait to see how her ass sticks out behind that tight waistline!"
    "..."
    $ renpy.sound.play("/audio/soun_fx/heels1.opus", channel="sfx2", loop=False, relative_volume = 1.2)
    pause 0.3
    stop sfx2 fadeout 6
    "After some time, you hear her footsteps echoing from the staircase, your heart starts racing in anticipation..."
    bot"Is that her in heels I am hearing? You are going all out, aren't you [hin_rel]!"
    label hinata_blackdress_firstdatenight_reveal:
    $ initialize_replay_defaults()    
    scene v21_hinatablackdress_front with dissolve:
        yalign 1.0 zoom 1.25
    show v21_hinatablackdress_front:
        easein 7 subpixel True yalign 0.1
    default hinatadress_outfit_unlocked = False
    $ hinatadress_outfit_unlocked = True
    $ notification(f"{hin_name}'s formal dress outfit unlocked!")
    hin "S-so... How do I look?"
    hin "I haven't worn something like this in ages..."
    call showscrollingimage from _call_showscrollingimage_297
    show screen parallax1280("v21_hinatablackdress_front",1.25,1.0,True) with dissolve
    hin "Do you think the heels go well with this dress? I didn't know what else to throw on..."
    call increaselust(10) from _call_increaselust_291
    bot "Holy shit... [hin_rel] looks incredible! A real certified MILF!"
    hide screen parallax1280
    show screen parallax1280("v21_hinatablackdress_front",1.25,0.5,True)
    with dissolve
    bot "Look at that tight waistline, leaving almost nothing left for imagination!"
    bot "I'd love to bury my face in those puppies and let my hands wander up those juicy thighs..."
    if chosen_hate_path:
        bot "I wonder what color panties she has on right now, I bet I could catch a glimpse if she bends over!"
    else:
        bot"You are fucking perfect, [hin_rel]!"
    hin "...[bo_name_stutter]?"
    hin "You hate it, don't you! I knew this was a mistake..."
    bo "N-no, not at all [hin_rel]! You are definitely breathtaking!"
    bo "The heels are great of course, but that dress absolutely looks like it was made for you!"
    hin "R-really? You think so?"
    bo "Without a doubt! You'll be putting smiles on anyone who looks your way tonight!"
    call increaselust(10) from _call_increaselust_292
    bot "And putting a rock hard erection in my pants!" with vpunch
    menu:
        "{color=[obediencecolor]}Give it a twirl, let's see the whole outfit!{/color}":
            bo "Do a quick twirl for me, let's see the whole outfit!"
            bot "Her ass probably looks divine in it too, all that junk in that trunk must be accentuated perfectly!"
            call checkObedience(20, "v21_twirlobediencefail", "Hinata", 1) from _call_checkObedience_63
            hin"A t-twirl? I don't know about that, [bo_name]..."
            bo "Come on, what's the big deal!"
            bo "I just want to admire you and the dress I picked for ya, see if I made the right choice..."
            show screen parallax1280("blackscreen",1.25,0.5,True) with dissolve
            hin"Hmmm, It does feel a little tight around my waist..."
            hide screen parallax1280
            show screen parallax1280("v21_hinatablackdress_back",1.25,0.5,True)
            with dissolve
            call increaselust(10) from _call_increaselust_293
            call changeObedience(1) from _call_changeObedience_180
            hin"I hope it doesn't look like how it feels down there, otherwise it may be a bit too m-much..."
            bot "There's that ass that I know and love!" with dissolve
            bot "I gotta stop myself from just drooling all over for it... \nBut fuck does it look good!"

            if chosen_hate_path:
                call checkHatred(0,"none",statlevel=2) from _call_checkHatred_50
                menu:
                    bot"On second thought..."
                    "{color=[hatredcolor]}Slap that ass!{/color}":
                        pass
                hide screen parallax1280
                show screen parallax1280("v21_hinatablackdress_back_spank1",1.25,0.8,True)
                with dissolve
                bot "Fuck it, I paid good money for this, I deserve to enjoy it!"
                hide screen parallax1280
                show screen parallax1280("v21_hinatablackdress_back_spank1",1.25,0.1,True)
                with dissolve
                hin"Uhm... Is s-something wrong?"
                bo "No, It's just that..."
                hide screen parallax1280
                show screen parallax1280("v21_hinatablackdress_back_spank2",1.25,0.6,True)
                with dissolve
                pause 0.3
                $ renpy.sound.play("/audio/soun_fx/spank5.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                hide screen parallax1280
                show screen parallax1280("v21_hinatablackdress_back_spank3",1.25,0.6,True)
                with dissolve                      
                pause 0.1
                $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                hide screen parallax1280
                show screen parallax1280("v21_hinatablackdress_back_spank3",1.25,0.7,True)
                with dissolve
                bo"You look fucking incredible!" with vpunch
                hide screen parallax1280
                show screen parallax1280("v21_hinatablackdress_back_spank3",1.25,0.0,True)
                with dissolve
                hin "[bo_name_stutter]!?" with vpunch
                show screen parallax1280("blackscreen",1.25,1.0,True) with vpunch
                hin "What do you think you're doing?!"
                call changeHatred(1, "v21_hinatadate_hatepathgrope",1,2) from _call_changeHatred_223
                bo "Just enjoying my gift a bit, that's all! Hehe..."
                hide screen parallax1280
                show screen parallax1280("v21_hinatablackdress_front",1.25,0.2)
                with dissolve
                label v21_dinnerdate_hatepath_abruptend:
                call changeRespect("Hinata",-1) from _call_changeRespect_272
                hin "I knew this was a mistake, you're out of control [bo_name]!" with vpunch
                hin "Cancel everything tonight, we will not be going anywhere with you acting like this!"
                bo "W-wait! You can't just cancel dinner!"
                show screen parallax1280("blackscreen",1.25,1.0,True) with vpunch
                call changeRespect("Hinata",-1) from _call_changeRespect_273
                hin "I can, and I just did!" with vpunch
                scene black with dissolve
                call hidescrollingimage() from _call_hidescrollingimage_243
                "[hin_name] storms back upstairs to her room, furious at how you have treated her."
                scene bg lr night
                show boruto angry at center
                with dissolve
                bot "Fuck [hin_rel], just like that it's all over?"
                show boruto at smallshake
                bot "What's the big deal anyway, can't she take a compliment?"
                # $ notification("Quest updated!")
                if quest_hin.is_state("3_hin2H", "in progress"):
                    $ notification ("Quest updated")
                    $ quest_hin.check("3_hin2H", "completed")
                    $ quest_hin.check("4_hin2H", "in progress") 
                show boruto sceeming with dissolve
                bot "I guess I'll just have to be more careful next time I get her into that dress..."
                bot "Fuck though, that ass felt as good as it looked!"
                bot "Next time you won't get away from me that easily..."
                scene black with dissolve
                bot "Ughh... Women..."
                $ renpy.end_replay()
                jump action_taken


            hin "Does it look okay from the back too? It was hard for me to tell in the mirror."
            bo "It's stunning! It wraps around you in all the right ways. This dress was made for you, [hin_rel]!"
            hin "O-oh, that's sweet of you to say, thank you. I'm just glad that it fits nicely."
            show screen parallax1280("v21_hinatablackdress_front",1.25,1.0) with dissolve
            hin "I was a little worried about it being too tight. Turns out you really know your [hin_rel]'s style and fit, don't you? *Giggles*"
            bo"You bet!"
            bot "Tight is just the way I like you [hin_rel]!" with dissolve
            hin"In that case..."
            show screen parallax1280("v21_hinatablackdress_front",1.25,0.2) with dissolve
            hin "Are you ready to go? We shouldn't leave Sakura waiting too long if she's expecting us."
            bo "Yes! Ready and excited for the night!"
            bo "Let's go!"

        "{color=[lovecolor]}Ready to start heading out?{/color}":
            bo "You're all done then [hin_rel]? Ready to start heading out?"
            hin "I think so! We shouldn't leave Sakura waiting too long if she's expecting us."
            bo "Yeah it won't take too long to get there."
            bo "Let's go!"

    scene black
    call hidescrollingimage("Click twice to leave the house together!") from _call_hidescrollingimage_244


    label v21_hinatalovelevel2_date_walk:
        $ renpy.sound.play("/audio/soun_fx/doorclose.opus", channel="sfx2", loop=False, relative_volume = 1.0)
        hin "It's been so long since I've walked in heels, I hope I don't fall..."
        scene v21_hinata_datewalk1 with dissolve:
            yalign 1.0
        show v21_hinata_datewalk1:
            easein 5 subpixel True yalign 0.5
        bo "Don't worry, I'll be right here to catch you if you do!"
        bot "It's definitely not just an excuse to have my hand hovering around your waist!" with dissolve
        bot "Just a few inches lower... The temptation is so hard to resist."
        menu:
            "{color=[impulsecolor]}'Accidentally' grope her ass!{/color}":
                scene v21_hinata_datewalk1_grope with dissolve
                $ renpy.sound.play("/audio/soun_fx/grope1.opus",channel="sfx4",loop=False,relative_volume=0.5)
                $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                hin "H-hey, w-watch where your hands are going!" with vpunch
                show v21_hinata_datewalk1 with dissolve:
                    yalign 0.5
                bo "Oh sorry, [hin_rel]! I meant to just hold your waist."
                bot "What a perfect ass it is, a real treat..."
                call changeHatred(1) from _call_changeHatred_224
                bot "I just can't help myself! Those soft cheeks belong in my hands..."
                call changeRespect("Hinata", -2) from _call_changeRespect_274
                hin "You can't tell the difference between my waist and my butt?"
                bo "I-I mean, I guess I'm just pretty excited for dinner and lost a bit of focus!"
                bo "Relax already [hin_rel]!"
                hin "Don't patronize me [bo_name], j-just try to control yourself tonight."
                hin "Let's not ruin the moment with these kind of antics, shall we?"

            "{color=[lovecolor]}Remain a gentleman{/color}":
                show v21_hinata_datewalk1_grope with dissolve:
                    zoom 1.02
                hin"Be there to catch me, eh?"
                hin"Quite the gentleman you've grown up to be! *Giggles*"
                bo "Of course! I would never let anything happen to you!"
                call changeRespect("Hinata", 1) from _call_changeRespect_275
                hin "Been a minute since I've last heard those words..."
                hin "But it is comforting seeing you step up ever since [na_name] went missing."
                hin"It can't be easy with all you are having to deal with given your... condition."
                hin "Thank you, [bo_name]..."
                bo "Of course! Anything for you [hin_rel]..."
                bo"I just want you to feel safe, perhaps even enjoy yourself at times! It's been a while since I've last seen a genuine smile on your face..."
                if hinata_love.level == 1:
                    call changeLove("Hinata", 1,"v21_dinnerdatewalk_gentleman",1 ,statlevel=1) from _call_changeLove_70
                else:
                    call changeLove("Hinata", 1,"v21_dinnerdatewalk_gentleman2",1 ,statlevel=2) from _call_changeLove_71
                hin "Well, it's definitely working I must say!"

        show v21_hinata_datewalk1:
            easein 5 subpixel True yalign 0.0
        hin "It's such a beautiful night out, it feels really nice to get outside the house for a change!"
        
        scene v21_hinata_datewalk2 with dissolve:
            yalign 1.0
        show v21_hinata_datewalk2:
            easein 6 subpixel True yalign 0.1
        "[hin_name] abruptly stops you, taking a moment to marvel at the starry sky..."
        if chosen_hate_path:
            bo "It's alright I guess..."
            bot "I'd much rather be at the beach watching all the hotties in their bikinis, but [hin_rel]'s ass makes up for that atleast."
        if chosen_love_path:
            bo "It really is, look at all the stars that came out to shine just for us."
            bo "I'm so glad we came out to witness this together."
        hin "You know, I've always loved the night sky! I find that it's so calming..."
        hin "There's just something about staring up at the universe that makes me feel so small and peaceful..."
        hin "Like I'm just a tiny part of something much bigger, and that our troubles seem so insignificant in comparison."
        show v21_hinata_datewalk3 with dissolve:
            yalign 1.0
        show v21_hinata_datewalk3:
            easein 8 yalign 0.0
        "She grabs your hand and pauses briefly..."
        hin "It's a nice thought, isn't it?"
        if chosen_hate_path:
            bo"I guess..."
            bot "Yeah, sure... Whatever helps you sleep at night."
        if chosen_love_path:
            bo "I've never really thought of it that way... But I guess it makes sense."
            bo "The universe is massive, and we're just tiny specks of dust in the grand scheme of things."
        show v21_hinata_datewalk1 with dissolve:
            easein 5 subpixel True yalign 0.5
        if chosen_hate_path:
            bo "What's next, are you going to start quoting poetry at me?"
            bo "Just do me a favour and consider not boring me to death with women's tangents on star signs."
            hin "That's astrology [bo_name], it has nothing to do with astronomy! You silly goose..."
            hin "*Sigh* Why do I even bother..."
        if chosen_love_path:
            bo "I find it ironic though, you're always telling me to keep my head out of the clouds but yours is up in space!"
            hin "That's because you always have a tendency get ahead of yourself! A character flaw you inherited from your [na_rel] no doubt."
            bo "I guess so... *chuckle*"
            bo "It's nice though to just take a moment to appreciate the beauty around us."
            bot"That would be you, [hin_rel]..." with dissolve
            hin "*Sigh* It really is! Alas, all good things must come to an end..."
        scene black with dissolve
        hin "Come on, we're almost there now!"
        jump v21_hinatalovelevel2_date_dinner


label v21_twirlobediencefail:
    hin "A t-twirl? Is that really necessary right now [bo_name]?"
    bot "Damn, she's not comfortable enough to show off a little for me..."
    if chosen_hate_path:
        call checkHatred(0,None,statlevel=2) from _call_checkHatred_51
        bo "I just wanted to get the full experience [hin_rel], is that too much to ask for?"
        bo "I bet your ass looks really nice in that dress!"
        hin "M-my w-what...?!"
        jump v21_dinnerdate_hatepath_abruptend
    bot "I'll have to try sneak a peek later when she's not looking instead!"
    call changeRespect("Hinata", -1) from _call_changeRespect_276
    hin "W-why would you even ask that?"
    hin "We should probably just get going..."
    hin "It would be rude to leave Sakura waiting too long if she's expecting us."
    bo "Y-yeah, you're right [hin_rel]..."
    bo "Let's go then!"
    jump v21_hinatalovelevel2_date_walk


label v21_hinatalovelevel2_date_dinner:
    $ renpy.sound.play("/audio/soun_fx/dooropen.opus", channel="sfx3", loop=False, relative_volume = 0.6)
    $ v21_hinatadate_progression = 1
    if not _in_replay and hinata_love.level < 2:
        call useItem(wine,1) from _call_useItem_13
    "You finally arrive at the Uchiha residence, greeted at the door by an enthusiastic Sakura waiting at the front door."
    scene v21_sakura_greeting with dissolve:
        yalign 1.0
    show v21_sakura_greeting:
        easein 5 subpixel True yalign 0.2
    saku "There you are, I was wondering when you'd show up!"
    bot "Damn! Auntie's definitely not one to shy away from a sexy dress!"
    bot "Red looks so good on her too, a real crimson goddess of desire!"
    scene black
    hin"Sa... Sakura!?" with vpunch
    scene inohouse night
    show dhina shy1 at left
    show sakurad normal1 at right
    with dissolve
    saku "Oh? Why the long face, [hin_name]... you look absolutely stunning!"
    hin "Th-thank you, I am just a bit s-surprised! *Nervous giggle*"
    hin "You look amazing as always too, if not a bit... r-revealing!"
    show sakurad normal2 with dissolve
    saku "I love your dress, it suits you so well! Didn't know you still had it in you! *Teasing giggles*"
    show dhina normal1 with dissolve
    hin "All credit goes to [bo_name] for picking this for me. It was his idea from the get-go."
    saku "Aww, how thoughtful! Spoiling your [hin_rel_mother] like that... I'm a bit jealous even!"
    saku "I wish I had someone around to care for me like that!"
    show sakurad normal1 with dissolve
    saku "Think you can handle another [hin_rel_mother] to treat expensive gifts to [bo_name]? *Teasing giggles!*"
    bo "You know me, I always aim to please!"
    saku "That you do!"
    scene v21_sakura_greeting2 with dissolve:
        yalign 0.8
    show v21_sakura_greeting2:
        easein 5 subpixel True yalign 0.2
    saku "Come in, come in! Make yourselves at home!"
    saku "Dinner is basically ready, so just take a seat and relax while I serve everything up."
    scene black with fade
    "You follow Sakura inside and into the dining room, the scent of delicious food wafting through the air."
    bo "Wow, it smells amazing in here!"
    hin "It really does! Sakura, you've outdone yourself this time."
    saku "Thank you dear! Just wait till you try it!"
    scene v21_hinatasakura_dinnertable with dissolve:
        yalign 1.0
    show v21_hinatasakura_dinnertable:
        easein 5 subpixel True yalign 0.2
    "You take a seat opposite of Sakura at the dining table, as she lays out an assortment of food before the two of you."
    bo "This looks incredible!"
    saku "Of course, only the best for my special guests!"
    saku "What you see in front of you is a pure labor of love."
    saku "Grilled yakizakana and sashimi fillets from the finest fish market in Konoha, seasoned lightly and topped with a delicate citrus sauce."
    saku "And to supplement it, some delicious deep-fried tempura on top of freshly steamed rice."
    hin "As far as home-cooked meals go, this is definitely top tier luxury."
    hin "You really shouldn't have Sakura, but thank you for your generous hospitality!"
    saku "Don't even mention it! Now dig in before it gets cold!"
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/stomachgrowl.opus", channel="sfx1", loop=False, relative_volume = 1.0)
    "The growls from your stomach echo in the room as you fail to contain them any longer, and you immediately start devouring the delicious food before you."
    $ renpy.sound.play("/audio/soun_fx/chopsticks_clinking.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    "The sound of chopsticks clinking against plates and light conversation with half-filled mouths ensues, as the evening hours go by."
    scene v21_hinatasakura_dinnertable_var3 with dissolve:
        yalign 0.2
    show v21_hinatasakura_dinnertable_var3:
        ease 2 subpixel True zoom 1.1 xalign 0
    saku "...- I know what you mean, we've also had to tighten our belts a bit lately around here."
    saku "It's been tough with the village's finances in disarray and the Daimyo breathing down our necks."
    show v21_hinatasakura_dinnertable_var3:
        ease 2 subpixel True xalign 1.0
    hin "Something just isn't right... He is up to no good! But who would dare to stand up against him?"
    scene v21_hinatasakura_dinnertable_var2 with dissolve:
        yalign 0.2 zoom 1.1 xalign 1.0
    bo "Nobody really wants to be the one to rock the boat, it's always risky to challenge authority."
    show v21_hinatasakura_dinnertable_var2:
        ease 2 subpixel True yalign 0.2 zoom 1.1 xalign 0.0
    saku "Yeah it's quite the sticky situation..."
    saku "We need to keep our eyes and ears open, and be ready to act if things take a turn for the worse."
    scene v21_hinatasakura_dinnertable_var3 with dissolve:
        yalign 0.2
    saku "If only our lousy husbands were more reliable... They never seem to be around when we need them the most!"
    hin "Tell me about it! It feels like they're always off on some important mission or some political altercation."
    hin "It gets quite lonely sometimes... And as frustrating as it can be, I can't help but miss [na_name]."
    saku "I know, I miss Sasuke too. But at least you still have your little man of the house around to fill that void..."
    show v21_hinatasakura_dinnertable_tease with dissolve
    saku "...Isn't that right?" with vpunch
    show v21_hinatasakura_dinnertable_var2 with dissolve:
        yalign 0.2
    bo "I do my b-best!"
    bot"Was that... Auntie's foot!? What is she trying to do..." with dissolve
    scene v21_hinatasakura_dinnertable_var3 with dissolve:
        yalign 0.2
    saku "Our household has been a bit too quiet without a man prancing about..."
    saku "Although this little guy helps break that monotony when he is around!"
    scene v21_hinatasakura_dinnertable_tease with dissolve:
        yalign 1.0
    saku "I might have to steal him from you more often to get him to come spend time with us instead! *Teehee*!" with vpunch
    call increaselust(10) from _call_increaselust_294
    bot"W-what the! Is she trying to..." with vpunch
    show v21_hinatasakura_dinnertable_tease with dissolve:
        yalign 0.2
    hin"Stop it, you! *Giggles* You are making [bo_name] blush..."
    bot"You have no idea, [hin_rel]..."
    if sarada_sparring_wincounter > 0:
        saku "Especially since he's been training with Sarada again recently..."
        saku "You should see the looks they give each other, it's adorable! I almost feel a bit left out!"
        bo "H-hey! I'm right here you know!"
        saku "Oh, are you? I only just noticed! *wink*"
    scene v21_hinatasakura_dinnertable_var3 with dissolve:
        yalign 0.2
    saku "What do you think [bo_name]? Is an old lady like me worth your time and thoughts at all?"
    show v21_hinatasakura_dinnertable_tease with dissolve:
        yalign 0.2
    "Sakura smiles at you mischievously while awaiting your reply, when suddenly..."
    show v21_hinatasakura_dinnertable_tease with dissolve:
        zoom 1.3 xalign 1.0
    bot"Ow f-fuck!" with vpunch
    scene v21_sakura_footrub with dissolve
    call increaselust(10) from _call_increaselust_295
    bot "Auntie is rubbing my cock!"
    bot"F-fuck! What should I do!?"
    $ v21_sakuradinner_footdenied = False #initialize
    menu :
        bot"F-fuck! What should I do!?"
        "{color=[impulsecolor]}It takes two to tango!{/color}":
            scene v21_hinatasakura_dinnertable with dissolve:
                yalign 0.0
            bot"I am not passing on your offer, you slutty sex-deprived cougar!"
            scene v21_sakura_footrub with dissolve
            bo "Of c-course, there's always enough of me for both of you!"
            scene v21_sakura_footrub2 with dissolve
            bo "Especially when I am blessed with... 'treats' like this from my Auntie!" with vpunch
            scene black with vpunch
            "You unclasp Sakura's footwear and push her foot against your groin as if to say: 'I know what you are doing!'"
            $ renpy.sound.play("/audio/soun_fx/heelsfalling.opus", channel="sfx2", loop=False, relative_volume = 1.0)
            "Her heel falls on the floor, leaving an audible sign of your mischief..." with vpunch
            scene v21_hinatasakura_dinnertable with dissolve:
                yalign 0.0
            saku"O-oh, oops!" with vpunch
            show v21_hinatasakura_dinnertable with dissolve:
                zoom 1.2 xalign 0.6
            hin"Did you... drop your heels, Sakura? I could fetch them for you if you like..."
            scene v21_hinatasakura_dinnertable with dissolve:
                yalign 0.0
            saku "Don't worry about it love, just resting my feet a bit is all!"
            scene black with dissolve
            show v21_sakurafj_anim1 with dissolve:
                xalign 0.5 yalign 0.0
            show v21_sakurafj_anim1:
                easein 5 yalign 1.0
            saku "You know how it gets walking around in those..."
            saku "Prepping dinner wearing heels was quite tiring, so you two better leave this table clean!"
            hin "*Giggles* I see! Don't you worry, I am sure [bo_name] has something to say about that!"
            show v21_sakurafj_anim2 with dissolve:
                xalign 0.5 yalign 1.0
            saku"Well? Do you have something to say then, [bo_name]?" with vpunch
            show v21_sakura_footy1 with dissolve
            $ renpy.sound.play("/audio/soun_fx/grabsound.opus",channel="sfx4",loop=False,relative_volume=0.5)
            "Sakura deviously pushed her foot up and down your groin, awaiting your reply..."
            scene v21_hinatasakura_dinnertable with dissolve:
                yalign 0.2
            bo"I am not leaving any of it go to waste, Auntie!" with vpunch
            $ renpy.sound.play("/audio/soun_fx/grabsound.opus",channel="sfx4",loop=False,relative_volume=0.5)
            show screen image_with_border("v21_sakura_footy1_cutout",0.5,1.0,0) with dissolve
            saku "Oh m-my! That you cannot do, huh?" with vpunch
            "The two of you kept unbreakable eye contact knowing full well what you were doing, harmlessly excluding [hin_name] from your antics..."
            hide screen image_with_border with dissolve
            bot "Thought I'd get flustered, eh?"
            call changeHatred(1) from _call_changeHatred_225
            bot "Two can play at this game, Auntie!"
            bot "That pussy of yours is the ultimate snack though. I can't wait to see more of it again, you teasing devil!"

        "{color=[lovecolor]}This is not the time to do this!{/color}":
            $ v21_sakuradinner_footdenied = True
            bot "We shouldn't be doing this right now, not with [hin_rel] sitting so close!"
            bot "It's so disrespectful to her, I can't go through with it."
            bo "There's a time and place for everything, and [hin_rel] will always come first of course!"
            bot "Tonight is all about her, I should shift my focus and not screw this up."
            scene v21_sakura_footrub2 with dissolve
            bot "I'll have my way with you another time Auntie, don't you worry!"
            scene black with dissolve
            $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx3", loop=False, relative_volume = 0.7) 
            "You gently brush her foot away, trying to regain your composure."
            "A brief look of disappointment flashes across Sakura's face as she realizes her advances are being denied."
            scene v21_hinatasakura_dinnertable_var3 with dissolve:
                yalign 0.2
            saku "It's understandable, although I can't help but feel a little disappointed."
            saku "Family does come first though, I suppose."
            show v21_hinatasakura_dinnertable_var2 with dissolve:
                yalign 0.2
            bo "It's nothing personal of course..."
            show v21_hinatasakura_dinnertable_var2 with dissolve:
                zoom 1.2 xalign 0.6 yalign 0.2
            hin "Well I for one, definitely have no complaints!"
            if hinata_love.level == 1:
                call changeLove("Hinata", 1, "v21_dinnerdate_denysakurafootrub", 1, 1) from _call_changeLove_72
            else:
                call changeLove("Hinata", 1, "v21_dinnerdate_denysakurafootrub2", 1, 2) from _call_changeLove_73
            hin "[bo_name] has always been there for me whenever I need him."
            scene v21_hinatasakura_dinnertable_var2 with dissolve:
                yalign 0.2
        
    saku "Our little hero, always there to save a damsel in distress!"
    saku "I think it's time we celebrate such bravery with some wine!"
    show v21_hinatasakura_dinnertable with dissolve:
        zoom 1.2 xalign 0.6 yalign 0.2
    hin "W-wine? We'll still need to make our way home, I'm not sure if it's a good idea to drink..."
    saku "Nonsense, just a little won't hurt! Besides, it's a special occasion!"
    saku "I won't take no for an answer, we could all use a drink to loosen up a little!"
    hin "A-alright, fine. But only a little bit, and while it's still early!"
    saku "See, I knew you'd come around! The night is young dear... *giggle*"
    scene black with fade
    $ renpy.sound.play("/audio/soun_fx/winepoured.opus",channel="sfx4",loop=False,relative_volume=1)
    "Sakura gets up to pour the wine you have supplied into glasses, already giggling in anticipation."
    if not v21_sakuradinner_footdenied:
        bot "Auntie is such a tease, stopping now just when it was starting to feel good..."
        bot "Or is she? Maybe there's more to come!"
    $ renpy.sound.play("/audio/soun_fx/wineglassclink.opus",channel="sfx4",loop=False,relative_volume=1)
    "The three of you enjoy a few glasses of wine, the atmosphere becoming more relaxed and intimate as the alcohol flows."
    scene v21_sakuradinnerdate_wine with dissolve:
        yalign 0.2
    saku "-... And that was the last time he ever tried to sneak up on me!"
    hin "I can't believe he thought he could get away with it!"
    # saku "I know right? I mean, who does he think I am? Some kind of pushover?"
    # bo "You definitely showed him! He'll think twice before trying that again."
    # saku "Damn right I did! And you know what? I think he secretly enjoyed it, that perv!"
    saku "If someone is going to try stealing my panties, they better be ready for the consequences!"
    saku "Or at the very least, be handsome enough for me not to mind! *wink*"
    show v21_sakuradinnerdate_wine with dissolve:
        zoom 1.2 xalign 0.6
    hin "S-Sakura...! You're the worst!" with vpunch
    saku "What?! It's true and you know it!"
    # saku "I think [bo_name] here would agree with me too."
    # bo "I mean, I can't say I disagree... *chuckle*"
    scene v21_sakuradinnerdate_wine with dissolve:
        yalign 0.2
    saku "Take [bo_name] for example, he's quite the looker!"
    saku "He probably gets away with a lot from the ladies himself! *giggle*"
    show v21_sakuradinnerdate_wine with dissolve:
        zoom 1.2 xalign 0.6
    bo "I, uh... No comment on that!"
    hin "You're both terrible!"
    show v21_sakuradinnerdate_wine with dissolve:
        zoom 1.2 xalign 0.2
    saku "Terribly frustrated maybe, yeah! Hihi..."
    scene v21_sakuradinnerdate_wine with dissolve:
        yalign 0.2
    # saku "Aren't we [bo_name]?"
    # bo "We sure are!"
    saku "But what about you, [hin_name]..."
    saku "How are you holding up? It can't be easy dealing with all that's on your plate..."
    saku "And if that weren't enough, you now have to deal with [bo_name]'s newfound condition..."
    if not v21_sakuradinner_footdenied:
        # saku "...Don't you?"
        scene black with dissolve
        "Sakura shifts her gaze to you with a playful smile, her eyes sparkling with mischief."
        "You can't help but feel a bit flustered under her intense look, and only moments later you feel something else entirely under the table again."
        show v21_sakurafj_anim2 with dissolve:
            xalign 0.5 yalign 1.0
        bot "She's back at it again, even with [hin_rel] being right here!"
        $ renpy.sound.play("/audio/soun_fx/grabsound.opus",channel="sfx4",loop=False,relative_volume=0.5)
        show v21_sakura_footy1 with dissolve:
            yalign 1.0 xalign 0.5
    hin "You really shouldn't tease the boy so much, he's still working on his self-control."
    saku "Aren't we all? Temptation makes us do crazy things sometimes!" with vpunch
    saku "And you know me, I can't help myself! Being a tease just comes naturally."
    if not v21_sakuradinner_footdenied:
        scene v21_sakuradinnerdate_wine:
            yalign 0.2
        show screen image_with_border("v21_sakura_footy1_cutout",0.5,1.0,0) 
        with dissolve
    saku "Especially with Sasuke and [na_name] away, we both don't have much of an outlet for our... frustrations!"
    show v21_sakuradinnerdate_wine with dissolve:
        zoom 1.2 xalign 0.8
    hin "S-Sakura!" with vpunch
    hin "While you're not wrong, I don't think [bo_name] needs to hear any of that!"
    show v21_sakuradinnerdate_wine with dissolve:
        xalign 0.2
    saku "He's an adult now, I think he can handle more than you give him credit for...*giggle*"
    # hin "I-I don't even want to think about that right now!"
    scene v21_sakuradinnerdate_wine with dissolve:
        yalign 0.2
    hin "But it is true, his [na_rel]'s absence is definitely felt."
    hin "I just hope we can manage to cope with everything until he returns..."
    # hin "Besides the l-loneliness... Our life circumstances have been quite overwhelming without his support."
    # saku "I don't know how much support those stubborn men provide, but waking up every morning to an empty bed is driving me insane!"
    saku "I swear, if Sasuke doesn't come back soon I might just have to find a young stud to replace him with!"
    if not v21_sakuradinner_footdenied:
        scene black
        hide screen image_with_border
        show v21_sakura_footy1_cutout:
            yalign 1.0 xalign 0.5
        with dissolve
    saku "A woman has needs ya know? *giggle*"
    hin "S-Sakura! Don't even joke like that, it's not appropriate!" with vpunch
    saku "Oh come on, lighten up a little! We're just having some fun!"
    saku "Aren't we [bo_name]?"
    if not v21_sakuradinner_footdenied:
        scene v21_sakuradinnerdate_wine with dissolve:
            yalign 0.2
        bot "You naughty girl... How do you even keep a straight face while rubbing my cock like that?!"
        show screen image_with_border("v21_sakura_footy1_cutout",0.5,1.0,0) 
        with dissolve
        $ v21_hinatadate_progression = 2
        call increaselust(20) from _call_increaselust_296
        bot "It's making me so fucking hard knowing she can't resist me..."
    # bo "Y-yeah of course, a little fun never hurt anyone!"
    # hin "It's all fun and games until someone gets hurt!"
    # hin "I've been constantly trying to keep the boy out of trouble lately..."
    # saku "Well personally, I think a little trouble could be good for him!"
    # hin "Only you would ever say something like that Sakura!"
    # saku "Well, it's true! It keeps things unpredictable and builds character!"
    # if not v21_sakuradinner_footdenied:
        bot "She's really being persistent, but what if [hin_rel] picks up on it or notices?"
        bot "I have to admit though, the danger of getting caught makes this even more exciting!"
        menu v21_hinatalovelevel2_date_dinner_footrubmenu:
            "{color=[lovecolor]}It feels good but that's enough!{/color}":
                $ v21_sakuradinner_footdenied = True
                bo "We're both really enjoying the evening, but there's a time and place for everything."
                scene black
                hide screen image_with_border
                show v21_sakura_footy1_cutout:
                    yalign 1.0 xalign 0.5
                with dissolve
                bot "Let's not push our luck, not with [hin_rel] sitting so close!"
                # bot "It's so disrespectful to her, I can't go through with it."
                # bot "Tonight is all about her, I should shift my focus and not screw this up."
                bot "I'll have my way with you another time Auntie, don't you worry!"
                scene black with dissolve
                $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx3", loop=False, relative_volume = 0.7) 
                "You gently brush her foot away, trying to regain your composure."
                scene v21_sakuradinnerdate_wine with dissolve:
                    yalign 0.2
                bo "[hin_rel] helps keep me grounded and safe, she always knows best!"
                "A brief look of disappointment flashes across Sakura's face as she realizes her advances are being denied."
                saku "It's understandable, although I can't help but feel a little disappointed."
                saku "Think of all the excitement you could be missing out on!"
                scene v21_sakuradinnerdate_wine with dissolve:
                    zoom 1.2 xalign 0.6 yalign 0.2
                hin "Well I for one, definitely have no complaints!"
                hin "[bo_name] has always been reasonable and understanding."
                if hinata_love.level == 1:
                    call changeLove("Hinata", 1, "v21_dinnerdate_denysakurafootrub", 1, 1) from _call_changeLove_74
                else:
                    call changeLove("Hinata", 1, "v21_dinnerdate_denysakurafootrub2", 1, 2) from _call_changeLove_75
                hin "I'm very proud of him!"
                bo "Life is all about striking the right balance!"
                # hin "Well said [bo_name], I couldn't agree more."
                scene v21_sakuradinnerdate_wine with dissolve:
                    yalign 0.2
                saku "Fair enough, we will have to agree to disagree then!"
                saku "At your age, I was out and about having a blast and creating unforgettable memories!"
                pass
            "{color=[impulsecolor]}More...!{/color}":
                bot "I... I need this..."
                bot "I know this is just the curse hungering for more but..."
                bot "It feels too good to pass up!" with vpunch
                scene black 
                hide screen image_with_border
                with dissolve
                show v21_sakurafj_anim1 with dissolve:
                    xalign 0.5 yalign 0.5
                show v21_sakurafj_anim1:
                    easein 2 yalign 1.0 
                bot "I'm sorry [hin_rel], but I can't help myself..."
                call changeHatred(1) from _call_changeHatred_226
                $ renpy.sound.play("/audio/soun_fx/zipper.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                show v21_sakurafj_pullout:
                    xalign 0.5 yalign 1.0
                bot "My cock NEEDS this!" with vpunch
                show v21_sakurafj_pullout:
                    easein 0.5 yalign 0.0
                saku "*Sharp gasp*!" with vpunch
                bo "Nothing wrong with a little fun and getting into some trouble!"
                "Even Sakura got caught off-guard by your brazen move. She flinched, but only for a second..."
                scene black
                show v21_sakurafj_pullout_anim1:
                    xalign 0.5 yalign 1.0
                with dissolve
                saku "S-settle down, hotshot!"
                show v21_sakurafj_pullout_anim2 with dissolve:
                    xalign 0.5 yalign 1.0
                saku "You know, I used to have a really hard time babysitting you when you were younger."
                $ renpy.sound.play("/audio/soun_fx/grabsound.opus",channel="sfx4",loop=False,relative_volume=0.5)
                show v21_sakura_footy2 with dissolve:
                    xalign 0.5 yalign 1.0
                saku "You were always so full of energy and mischief! A real naughty boy!"
                bot "Fuck yeah, she's stroking my cock with her foot!" with vpunch
                scene v21_sakuradinnerdate_wine:
                    yalign 0.2
                show screen image_with_border("v21_sakura_footy2_cutout",0.5,1.0,0) 
                with dissolve
                # scene v21_hinatasakura_dinnertable with dissolve:
                    # yalign 0.0
                bo "What can I say, I was just keeping you on your toes!"
                saku "That you were! *giggle*"
                hin "He gets that from his [na_rel] unfortunately, it's not something they ever grow out of either!"
                saku "He's still quite the handful, isn't he?"
                bot "More like a footful in this case hehe..."
                bot "Keep rubbing that cock Auntie, I can tell you're enjoying this!"
                hin "I keep them both in line as much as possible, but I'd be lying if I said it was always easy."
                saku "[bo_name]! Don't be giving your dear [hin_rel_mother] a hard time, ya hear!"
                scene black
                hide screen image_with_border
                show v21_sakura_footy2_cutout:
                    yalign 1.0 xalign 0.5
                with dissolve
                saku "Otherwise I'll drag you over here and give {i}you{/i} a hard time instead!"
                bo "Is that a promise? *smirk*"
                saku "Maybe... if you're lucky! *giggle*"
                show v21_sakura_footy2_cutoutfast:
                    yalign 1.0 xalign 0.5
                bot "Yes, that's it... Go faster Auntie!"
                bot "Fuck it feels good!" with vpunch
                scene v21_sakuradinnerdate_wine:
                    yalign 0.2
                show screen image_with_border("v21_sakura_footy2_cutoutfast",0.5,1.0,0) 
                with dissolve
                hin "What are you two blabbering about now, I think the wine is getting to your heads."
                saku "Oh, we haven't had nearly enough for that yet!"
                # bo "Speak for yourself, I'm feeling pretty relaxed!"
                # saku "Are you now?"
                # bo "Absolutely! But if I keep drinking like this, my head might just explode!"
                # hin "Maybe it's time we wrap it up then? You shouldn't push yourself too hard [bo_name]!"
                saku "Let the boy enjoy himself a bit more! It's not every day we get to unwind like this."
                scene black
                hide screen image_with_border
                show v21_sakura_footy2_cutoutfast:
                    yalign 1.0 xalign 0.5
                with dissolve
                bot "[hin_rel] is on the verge of discovering us, and Auntie is relentless and playing with fire!"
                bot "I can feel the tension rising... I won't last much longer..."
                scene v21_sakuradinnerdate_wine:
                    yalign 0.2
                show screen image_with_border("v21_sakura_footy2_cutoutfast",0.5,1.0,0) 
                with dissolve
                bo "Y-yeah, just a little more. Don't worry [hin_rel], I can handle it!"
                saku "See, he's having fun, I always take good care of him when he's here!"
                hin "O-okay if you say so..."
                scene black
                hide screen image_with_border
                show v21_sakura_footy2_cutoutfast:
                    yalign 1.0 xalign 0.5
                with dissolve
                "You sip on some wine to mask your face from the inevitable climax and desperately stifle any moans or heavy breaths that try to escape your mouth."
                scene black with dissolve
                "Ready to release, you grab Sakura's foot and ensure to cover it all with your sticky cum."
                show v21_sakurafj_cum:
                    xzoom -1 yalign 1.0 xalign 0.5
                with flash
                $ renpy.sound.play("/audio/soun_fx/cum4.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                bo "*Groans*" with flash
                call decreaselust(50) from _call_decreaselust_147
                bo "Mmm... Yeah... That's good, hits just the right spot..."
                show v21_sakurafj_cum_end with dissolve:
                    xzoom -1 yalign 1.0 xalign 0.5
                "Visibly aroused by the feeling of it dripping off her foot, Sakura can't help but briefly touch herself out of pure excitement."
                saku "Mmmm... ♡"
                saku "You really handle your wine well [bo_name], don't you? I'm quite impressed! *giggle*"
                bo "I guess I just know my limits well."
                hin "Somehow I doubt that! You've gotten all red and seem to be out of breath suddenly."
                bot "Fuck, is [hin_rel] noticing something going on?" with dissolve
                bot "Gotta play it cool..."
                scene v21_sakuradinnerdate_wine with dissolve:
                    yalign 0.2 xalign 0.8 zoom 1.2
                bo "I'll be fine... Just a little light-headed, don't worry about me!"
                hin "Well at this rate, I wouldn't be surprised if you didn't have any memory of what happened here in the morning."
                pass
    else:
        bo "Fun is great and all, but we've been having more trouble than we would have liked lately."
        saku "There's always room for a little more! *giggle*"
        saku "Life is all about the memories we create, after all!"
    
    scene black with dissolve
    bo"Right...."
    saku"Enough about that! I've got a brilliant idea..."
    hin"Oh n-no! I've heard those words before from you. I've got to say it usually doesn't end well for either one of us! *Giggles*"
    if not v21_sakuradinner_footdenied:
        saku"You'll see! You condescending prick..." with vpunch
        hin"H-hey! Uncalled for..."
        saku"I am just playing with you, you silly lily!"
        $ renpy.sound.play("/audio/soun_fx/hinata/hinatasigh1.opus", channel="sfx3", loop=False, relative_volume = 0.4)
        hin"*Sigh...*"
        saku "Right! Let's 'clean' up a little first, shall we?"
        "Sakura smirks at you mischievously. You knew full well what she was insinuating.{p}Right then and there, a non-verbal agreement was made to safeguard your secrets."
        bo "Of course, Auntie. Let me help with that..."
        "You take a moment to clean the table up, and yourselves... disposing any evidence of your wrongdoings, before rejoining their company."
    else:
        saku"Oh come on, I am not that bad of an influence! Am I? *Giggles*"
        "You spent some time cleaning up..."

    saku"Ta-daa!"
    scene 00348-3556607002 with dissolve:
        yalign 1.0
    show 00348-3556607002:
        easein 10 yalign 0.2
    "Sakura fetches the wine you brought with you and refills all your glasses!"
    hin"More wine... huh? So much for your brilliant ideas..."
    saku"Come on, [hin_name]! Loosen up a bit, will ya? Always so stiff..."
    saku"Besides, today marks the start of something special for us both!"
    hin"It does?"
    saku"Yes!{p}I formally declare today as the annual 'Drink yourself to death, and curse your husbands to hell and back' Day!"
    scene black
    saku"KANPAIII!!" with vpunch
    hin"S-sakura!?"
    scene 00348-3556607002 with dissolve:
        yalign 1.0
    show 00348-3556607002:
        easein 10 yalign 0.2
    saku"Relaaax! I am only joking of course...{p}M-mostly!"
    saku"Aren't you tired of those two idiots too?{p}Always away on some stupid mission of theirs, neglecting their wives, their children even!"
    hint"Poor Sakura. She's feeling Sasuke's absence as much as I am feeling [na_name]'s. This is just how she copes, isn't it?"
    saku"*Sigh...* "
    saku"I say today is the day we break free of that burden!{p}From now on, we'll stop sulking about them, and start having some fun!"
    scene black with vpunch
    saku"So come on, drink up! You too [bo_name]!"
    saku"Ya-hooo!" with vpunch
    hin"Okay, okay! But only for this occasion!"
    "The two of them spend some time reminiscing about their younger days, and how their relationships came to be..."
    saku"And then... *Uncontrollably laughing*"
    scene 00348-3556607002 with dissolve:
        yalign 1.0
    show 00348-3556607002:
        easein 10 yalign 0.2
    saku"And then he said the dumbest thing I've ever heard, and poked my forehead like I was some child!" with vpunch
    "*All three laughing*" with vpunch
    saku"As stupid as he is, I can't help but feel endeared by his social ineptitude!"
    hin"Even then, I doubt Sasuke could ever match [na_name]'s clumsiness! *Giggles*"
    saku"Lucky for us, [bo_name] has inherited the best of you both!{p}We at least have someone competent to keep us company!"
    hin"That we do!"
    scene black with dissolve
    "The conversation carries on for a while, bringing back memories of old for the two of them..."
    bo "Speaking of memories..."
    bo "Check this out!" with vpunch
    scene bg lr uchiha
    show sakurad normal1 at left
    show dhina normal1 at right
    with dissolve
    bo "I brought my camera along with me tonight. I thought it would be fun to capture some photos of us to remember this night!"
    hin"Oh y-yeah! I was wondering what was up with all the equipment back at home lately..."
    show sakurad at smallshake
    saku "A photoshoot? How fun, *Hic!* count me in!" with vpunch
    show sakurad normal2 with dissolve
    saku "Come on, [hin_name], it's time to pose! *Giggles playfully*"
    show dhina shy2 with dissolve
    hin "S-sure, I don't see why not."
    scene black with dissolve
    bo "Alright then, which one of you pretty ladies will go firs-"
    saku "Me, me, me!"
    "Sakura rushes into the frame as soon as you point the lens towards them.."
    # bo "Let's get a close up shot of each of you beautiful ladies first."
    # bo "You're both looking so lovely tonight!"
    bo"Show me what you got then, Auntie!"
    scene v21_sakura_photo with dissolve:
        yalign 1.0
    show v21_sakura_photo:
        easein 4 yalign 0.0
    pause 3
    # CG of sakura maybe something like "sakurwine drinking2" in her dress = v21_sakura_photo
    call showscrollingimage from _call_showscrollingimage_298
    show screen camera1280("v21_sakura_photo", 1, 0.0)
    show screen camera_ui("Sakura_winedinnerdate", False)
    with dissolve
    "She strikes a seductive pose, holding her wine glass up with a flirtatious smile."
    hint"Isn't Sakura being a little... extra around [bo_name]?"
    hint "She knows about his condition, doesn't she?"
    bo "N-nice one Auntie! Now smile, and..."
    show screen camera_ui("Sakura_winedinnerdate") with dissolve
    $ ui.interact()
    hide screen camera_ui
    hide screen camera1280 
    hide scrollingimage onlayer screens
    show v21_sakura_photo:
        yalign 0.2
    with dissolve
    "You capture the moment perfectly, Sakura looking radiant in her red dress."
    scene bg lr uchiha
    show sakurad normal1 at left
    show dhina normal1 at right
    with dissolve
    bo "Awesome, it looks great! The light really captures the glint in your eyes Auntie."
    saku "You're too sweet! I really do love how it turned out, I look like a bombshell... *Hic!*" with vpunch
    bo "Now your turn, [hin_rel]!"
    scene black with dissolve
    "You turn the camera towards [hin_name], who looks a bit reserved but still excited to be part of the moment."
    scene v21_hinata_photo with dissolve:
        yalign 1.0
    show v21_hinata_photo:
        easein 4 yalign 0.0
    pause 3
    "She takes a deep breath and smiles, striking a rather neutral but cute pose."
    hin "I-Is this okay?"
    call showscrollingimage from _call_showscrollingimage_299
    show screen camera1280("v21_hinata_photo", 1, 0.0)
    show screen camera_ui("Hinata_winedinnerdate", False)
    with dissolve
    bo "It's perfect, don't be shy! Just be yourself, you look so beautiful!"
    show screen camera_ui("Hinata_winedinnerdate") with dissolve
    $ ui.interact()
    hide screen camera_ui
    hide screen camera1280 
    hide scrollingimage onlayer screens
    show v21_hinata_photo:
        yalign 0.2
    with dissolve
    "You snap the photo and marvel at it for a while...{p}You can't help but smile at how gorgeous she looks in her black dress."
    scene bg lr uchiha
    show sakurad normal1 at left
    show dhina normal1 at right
    with dissolve
    hin "We both look great, don't we Sakura! I didn't know you had such a talent for photography [bo_name]..."
    show sakurad teasing1 with dissolve
    saku"Right!?"
    bo "It's easy when you have such photogenic models to work with, the beauty just comes out naturally!"
    show sakurad normal2 with dissolve
    saku"That's right! Let it be known... *Hic!* That age is just a number!"
    show dhina shy1 with dissolve:
        xzoom -1
    hin "O-oh stop it you two! You're making me blush..."
    bo "Now one final picture with all of us together! I'll set the camera up with a timer."
    scene black with dissolve
    "You place the camera at an elevated angle on a nearby table, setting the timer for a minute."
    bo "Okay ladies, everyone get close together here to be in the shot!"
    scene v21_ending_photo with dissolve:
        xzoom -1 yalign 1.0
    show v21_ending_photo:
        easein 4 yalign 0.3
    "You position yourself between Sakura and [hin_name], wrapping your arms around their waists."
    saku "Big smiles everyone! Let's see all those teeth!"
    bo "Try not to move too much until you see the flash, it'll only be a few seconds!"
    show v21_ending_photo:
        easein 4 yalign 0.8
    bot "Being between two beautiful women like this is quite the privilege..."
    bot "I could maybe take advantage of the situation!"
    bot "Those asses look like they could use some attention..."
    $ v21_dinnerdate_hinata_assgrabbed = False #initialize
    $ v21_dinnerdate_sakura_assgrabbed = False

    menu:
        "Sakura deserves some payback!":
            bot "Time for a little payback."
            bot "You thought you were going to be the only one getting frisky tonight Auntie?"
            $ v21_dinnerdate_sakura_assgrabbed = True
            show v21_ending_photo_sakuragrope with dissolve:
                xzoom -1 yalign 0.8
            $ renpy.sound.play("/audio/soun_fx/grabsound.opus",channel="sfx4",loop=False,relative_volume=0.5)
            saku "You little- *Giggles*" with vpunch
            hin "H-huh?"
            pass

        "Caress [hin_name]'s ass":
            $ v21_dinnerdate_hinata_assgrabbed = True
            bot "[hin_rel] is so perfectly round and soft... I can't resist!"
            bo "A bit closer you two, just in case!"
            hin "H-how much closer can I even get-..."
            show v21_ending_photo_hinatagrope with dissolve:
                xzoom -1 yalign 0.8
            $ renpy.sound.play("/audio/soun_fx/grabsound.opus",channel="sfx4",loop=False,relative_volume=0.5)
            hin "*Gasp!*" with vpunch
            bot "Sounds like she definitely noticed! Hehe..."
            bo "Okay, that should be good!"
            pass

        "Just take the picture":
            bot "Let's not push my luck, I'm sure there'll be plenty more opportunities."
            pass

    bo "Alright, everyone say cheese!"
    saku "Cheese!"
    hin "Cheese!"
    $ renpy.sound.play("audio/soun_fx/takephoto.opus", channel="sfx3", loop=False, relative_volume = 0.6)
    if v21_dinnerdate_sakura_assgrabbed:
        scene v21_sakura_endingphoto1_sakura with longerflash:
            yalign 0.8
        show v21_sakura_endingphoto1_sakura:
            easein 3 yalign 0.1
    elif v21_dinnerdate_hinata_assgrabbed:
        scene v21_sakura_endingphoto1_hinata with longerflash:
            yalign 0.8
        show v21_sakura_endingphoto1_hinata:
            easein 3 yalign 0.1
    else:
        scene v21_ending_photo with longerflash:
            xzoom -1 yalign 0.8
        show v21_ending_photo:
            easein 3 yalign 0.1
    "The flash goes off, immortalizing the moment of the three of you."
    saku "Did you get it? How thrilling!"
    bo "Let's take a look!"
    scene black with dissolve
    "You gather around the camera to check out the photo, all of you smiling and laughing at the memories captured tonight."
    scene bg lr uchiha
    show sakurad normal1 at left
    show dhina shy1 at right:
        xzoom -1
    with dissolve
    saku "Look at you guys, you're so cute! I love it!"
    hin "You clearly outshine us all with your smile, Sakura."
    bo "Nonsense, it's a perfect photograph with two of the most beautiful women in the region!"
    bo "I think we make a pretty good team together!"
    show sakurad teasing1 with dissolve
    saku "That we do! *Giggles*"
    show dhina shy2 with dissolve:
        xzoom -1
    hin "We should frame this, I'd love to look back on it in the future!"
    bo "Definitely! I'll make sure to print it out and arrange it for you [hin_rel]."
    scene black with fade
    "You take a few moments to appreciate the bond you share with [hin_name] and Sakura."
    "Soon enough, the night winds down and the two of you say your goodbyes to Sakura."
    scene v21_sakura_farewell with dissolve: #Don't add to galery, zoomed in to hide jank
        zoom 1.2 xalign 1.0 yalign 1.0
    show v21_sakura_farewell:
        easein 4 subpixel True yalign 0.1
    saku "Don't be strangers now, okay? We should arrange fun nights out like this more often!"
    saku "I had such a great time tonight!"
    hin "Me too! Thanks so much for having us."
    saku "The pleasure was all mine! Or at least most of it... *giggle*"
    bo "See you again soon Auntie!"
    scene black with fade
    $ renpy.sound.play("/audio/soun_fx/doorclose.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    "You both wave goodbye to Sakura before starting to head back home."
    jump v21_hinatalovelevel2_date_walkback

label v21_hinatalovelevel2_date_walkback:

    scene v21_hinata_datewalkback1 with dissolve:
        yalign 1.0
    show v21_hinata_datewalkback1:
        easein 5 subpixel True yalign 0.2
    "You walk along the path with [hin_name], reflecting on the wonderful time you had tonight at dinner."
    "The night air is cool with a slight breeze, providing a refreshing contrast to your alcohol-warmed skin."
    hin "That was... nice! Thank you, [bo_name]!"
    hin "Although I am feeling a little light-headed..."
    bo "You aren't having trouble walking in those heels, are you? You were never a good drinker in the first place!"
    show v21_hinata_datewalkback1:
        easein 4 subpixel True yalign 1.0 zoom 1.5 xalign 0.3
    bot "Not to mention that tight dress I got for you, restricting your movements..."
    bot "Look at that firm ass popping out!"
    bot "Money well spent, if I do say so myself!"
    show v21_hinata_datewalkback1:
        easein 4 subpixel True yalign 0.2
    hin "Oh, I'll be f-fine... I'm just not used to being this t-tipsy... *Hic!*"
    hin "I'm sure everything will stop spinning eventually! *Giggles*"
    hin "Besides, I have you here to help me if I stumble, I couldn't be in safer hands!"
    menu:
        "Hold her closer":
            show screen parallax1280("v21_hinata_datewalkback2",1,0.0) with dissolve
            call showscrollingimage from _call_showscrollingimage_300
            bo "I'll always be there for you, [hin_rel]!"
    "[hin_name] wraps her arm around your neck, leaning in a little closer to you..."
    "You can feel her warmth against your skin, the scent of her perfumed hair filling the air around you."
    hin "What a gentleman you are..."
    if v21_dinnerdate_hinata_assgrabbed == True:
        hin "Except when you decide to get all h-handsy!"
        hin "Don't think I didn't notice you when we were taking that picture together..."
        bo "Oh, come on! I was just trying to help you pose!"
        hin "S-sure you were..."
        hin "We'll work on those i-impulses of yours, don't worry."
        hin "Once you get them under control, then... W-well..."
    hin "Any woman would be lucky to have you by their side!"
    bo "Any woman, huh? That sounds like it includes you too!"
    hin "Oh s-stop it [bo_name], *Hic!* you know what I meant!"
    bo "Well lucky for you, today you can have me all to yourself!"
    hin "Ha! You're such a charmer... not! *giggles*"
    hin "Honestly, you and your [na_rel] are competing for the worst one-liners I've ever heard!"
    # hin "Maybe under different circumstances, I might have too..."
    hin "Mmm... Thinking about him just makes my head s-spin even more... *Hic!*"
    show screen parallax1280("blackscreen") with Dissolve(1)
    "[hin_name]'s eyes start to droop, her body giving in to the effects of the wine as her walking slows down."
    bo "H-hey, you feeling alright [hin_rel]?"
    hin "Y-yeah, just a little dizzy... I think I might need t-to sto-..."
    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    hin "Whoa...!" with vpunch
    hide screen parallax1280
    show screen parallax1280("v21_hinata_walkback_kiss1",1,0.2) 
    with dissolve
    "You quickly catch her as she loses her footing, pulling her into a supportive hug."
    bo "Careful there, you almost took a tumble!"
    "[hin_name] stares into your eyes with a soft smile, her cheeks flushed and her breath slightly unsteady."
    hin "S-so strong... Just like your [na_rel]...*Hic!*"
    hin "Y-you know, I m-miss him so much... His t-touch... His warmth..."
    show screen parallax1280("blackscreen") with Dissolve(1)
    "Her eyes close again briefly as she leans into your embrace, seeking comfort in her vulnerable state."
    $ renpy.sound.play("/audio/soun_fx/hinata/hinatasigh1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    hin "I... I can almost f-feel it now... R-right here..."
    hide screen parallax1280
    show screen parallax1280("v21_hinata_datewalkback_kiss2",1,0) 
    with Dissolve(1)
    $ renpy.sound.play("/audio/soun_fx/kiss2.opus", channel="sfx2", loop=True, relative_volume = 1)
    "You give in to temptation and make your move! Her lips find yours and lock into deep and passionate kisses."
    hin "Mmm... [na_name]...? ♡"
    "The two of you share this brief tender moment, like lost lovers reunited under the night sky."
    bo "[hin_rel]... ♡"
    show screen parallax1280("blackscreen") with fade
    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp1.opus", channel="sfx2", loop=False, relative_volume = 0.6)
    "Hearing your voice, [hin_name] snaps out of her daze and pulls away, finally realizing it is not her husband returning her kiss."
    hide screen parallax1280
    show screen parallax1280("v21_hinata_datewalkback_kiss3",1,0.3) 
    with dissolve
    hin "[bo_name_stutter]... I am s-sorry! I spaced out...*Hic!*" with vpunch
    bot"I... kissed her! Wait... she k-kissed me!?" with vpunch
    bot"And now her boobs are pressed against me!" with vpunch
    hin "I t-thought... O-oh... N-never mind!"
    bo "I-it's okay, [hin_rel]. You just had a little too much to drink, that's a-all!"
    hin "Y-yes... It would s-seem so!"
    bo "Are you... feeling alright? I worry about you, you know..."
    hide screen parallax1280
    show screen parallax1280("v21_hinata_datewalkback_kiss4",1,0.3) 
    with dissolve
    "She stops you for a second, softly pulling away from you, but recognizes a glint of truthful concern reflecting in your eyes."
    hin "[bo_name], Let me do all the worrying for the both of us, o-okay?"
    hin "I can handle m-myself. I just had an extra d-drink or two!"
    hin"You know I love you, but that  was an accident... okay? *Hic!*"
    show screen parallax1280("blackscreen",1,0.3) 
    hin "N-now come... Give your old [hin_rel_mother] a hug!" with vpunch
    show screen parallax1280("v21_hinata_datewalkbackhug1",1,0.5) with dissolve
    "You wrap your arms around her, as she willingly lets her weight drop against yours.{p}Your hands quickly wrapped around her waist, holding her upright despite her drowsiness."
    "You find comfort in each other's embrace for a few seconds longer before pulling away a few inches."
    if hinata_love.level > 1:
        call changeLove("Hinata",1,"v21_hinatadatewalkback2",1,2) from _call_changeLove_76
    else:
        call changeLove("Hinata",1,"v21_hinatadatewalkback1",1) from _call_changeLove_77
    hin "You're the best [hin_rel_to_bo] I could have ever asked for..."
    hin"Th-thank you for tonight...*Hic!*"
    bo "Well I happen to be the only one you've got, so I definitely hope so!"
    show screen parallax1280("blackscreen") with dissolve
    "[hin_name] lets out a content sigh, a smile spreading across her face."
    hin "Enough of that now...{p}I really need to lay down for a bit...*Hic!*{p}We are not far from home now, come on."
    bo "Yeah it's been... quite the night."
    bo "Let's get you back home so you can rest."
    hide screen parallax1280
    show screen parallax1280("v21_hinata_datewalkback3",1,0.9) 
    with dissolve
    "You walk the final stretch back in comfortable silence, occasionally stealing awkward glances and smiles at each other."
    if chosen_love_path and hinata_love.level == 1:
        $ notification (f"{hin_name}'s love level has reached level 2! The stat has been reset to 0.")
        $ hinata_love.level = 2
        $ hinata_love.value = 0
    $ v21_hinatadate_daycounter = 0 # Day counter used to track days, resets after each date and doesn't allow dates on same weekend
    if chosen_love_path:
        bot "What a perfect end to a perfect evening."
        bot "[hin_rel] is practically glowing with happiness, this was such a good idea!"
        bot "I even got to share a kiss with her for my troubles, can't complain about that!"
        bot "She doesn't need to know what me and Auntie have been up to though, it would probably really upset her..."
        if quest_hin.is_state("2_hin2L", "in progress"):
            $ notification ("Quest updated")
            $ quest_hin.check("2_hin2L", "completed")
            $ quest_hin.check("3_hin2L", "in progress")
            $ quest_hin.check("hin2L_2", "in progress")
        bot "Next time, maybe I should arrange the night just between the two of us and spend some quality time together alone at home."
        show screen parallax1280("blackscreen") with dissolve
        bot "Yeah that sounds nice..."
    scene black
    call hidescrollingimage("Click twice to end the night!") from _call_hidescrollingimage_245
    $ renpy.sound.play("/audio/soun_fx/doorclose.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    "You finally reach the front door of your house. [hin_name] bids you good night, and beelines to her bedroom."
    bot"We might be getting somewhere, [hin_rel]...{p}Fuck! Now all I can think about is our next night out together..."
    $ renpy.end_replay()
    jump action_taken
