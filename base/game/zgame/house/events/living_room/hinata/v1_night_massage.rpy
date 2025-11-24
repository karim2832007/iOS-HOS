
default unlocklvl2hatredevent = False




label v1_night_massage:
    $ current_event = "v1_night_massage"
    scene bg lr hinanight massage
    show screen v1_night_massage_screen
    with dissolve
    call enabletalk from _call_enabletalk
    call showUIhouse from _call_showUIhouse_2
    $ ui.interact()










label v1_night_massage_talk:
    hide screen v1_night_massage_screen

    # v21 First dinner date auto trigger

    if quest_hin.exists("1_hin2L") or quest_hin.exists("2_hin2H"):
        if (quest_hin.is_state("1_hin2L", "pending") or quest_hin.is_state("2_hin2H", "pending")):
            $ unlocklvl2hatredevent = True

    if quest_hin.exists("2_hin2L") or quest_hin.exists("3_hin2H"):
        if v21_hinatadate_progression == 0 and (quest_hin.is_state("2_hin2L", "in progress") or quest_hin.is_state("3_hin2H", "in progress")):
            $ wine_in_inventory = inventory.find_item_by_name("Wine")
            $ blackdress_in_inventory = inventory.find_item_by_name("Black Dress")
            if wine_in_inventory!= None and blackdress_in_inventory!= None: 
                bot "There she is, always so lost in thought lately..."
                bot "I have everything I need for her surprise, should I go through with it tonight?"
                menu:
                    "Yes, go for it!":
                        bot "Alright, here goes nothing!"
                        jump v21_hinatalovelevel2_date
                    "No, it's not the right time...":
                        bot "Tonight doesn't seem like the right time for it, there's no harm in waiting a little longer."
                        pass
            elif wine_in_inventory== None or blackdress_in_inventory== None:
                bot "If I want to surprise [hin_rel], I better make sure I have everything I need first!"
                "Purchase a black dress and a bottle of wine from the shop."
                pass

    # ----------------------------

    bo"Hey [hin_rel], can I join you?"
    hin"S-sure..."
    if hinatapillsedated == True:
        bot"I wonder if she'll mention anything about last time..."
    if (chosen_hate_path or chosen_love_path) and day_number >= 14 and unlocklvl2hatredevent:
        $ notification("New dialogue option available")
        bot "She seems a bit lost in thought, I should ask if something is wrong..."
    show lr nightmassage1 with fade
    default lr_massagecounter = 0
    $ pillsinv = inventory.find_item_by_name("Pills")
    menu lr_massage_menu:
        hin"S-sure..."
        "Have a conversation...":
            scene black with dissolve
            "You take a sit alongside [hin_name]..."
            show bg lr night:
                blur 20
            show hina nightmassage1:
                zoom 0.7 xalign 0.5 yalign 0.5
            with dissolve
            hin"So... Is there something you wanted to talk about?"
            menu lr_massage_menu_talk:
                hin"So... Is there something you wanted to talk about?"
                "Small talk":
                    scene black with dissolve
                    "You spend some time talking about menial every-day stuff with [hin_name]..."
                    show hina nightmassage3 with dissolve:
                        zoom 1.25 xalign 0.5 yalign 1.0
                    show hina nightmassage3:
                        easein 5 yalign 0.0
                    hin"And [bo_name]..."
                    call changeRespect("Hinata",1) from _call_changeRespect_25
                    hin"T-thanks for taking some time to talk with me. I think it really helps the both of us..."
                    bo"Of course..."
                    $ hinatapillsedated = False
                    jump action_taken

                "(locked)" if day_number<7:
                    "Advance the story to unlock..."
                    jump lr_massage_menu_talk
                "The Daimyo encounter..." if aboutthosemenandthedaimyo == True:
                    bo"About what happened the other day..."
                    jump massagetalkmenu
                "About those men and the Daimyo..." if day_number>=7 and aboutthosemenandthedaimyo == False:
                    default aboutthosemenandthedaimyo = False
                    $ aboutthosemenandthedaimyo = True
                    bo"[hin_rel]..."
                    hin"...Y-yes?"
                    bo"About those men the other day..."
                    hin"*Soft chuckle* Come on, [bo_name]! You are acting as if they did something bad to me..."
                    bo"Well... did they?"
                    hint"I can't let [bo_name] or [him_name] worry about this. Although I have my concerns about those men, it's best I re-assure [bo_name] for now..."
                    hin"Of c-course not! I imagine that was standard procedure..."
                    hin"They are just simple debt collectors employed by the Daimyo himself after all..."
                    if ch1_d7_hatredpath == True:
                        bot"It seems like she's trying to hide her true feelings from me..."
                        bot"Shall I press on?"
                        menu pressonmenu:
                            bot"Shall I press on?"
                            "{color=[dominancecolor]}Put her on the spot{/color}":
                                call checkDominance(6,"pressonmenu") from _call_checkDominance_2
                                bot"If I am to have her be dependent on me, I have to break through her protective act!"
                                bo"I can see that you are putting on an act [hin_rel]..."
                                bo"Your voice is shaky, your jittery movements..."
                                bo"They give it away, I know you better than that..."
                                hin"[bo_name_stutter]..."
                                bo"I am not a kid anymore [hin_rel]..."
                                bo"I can see you are in a tough spot, and I want to help, If only you would let me!"
                                hin"*Sigh* I... I know [bo_name_stutter], you are r-right."
                                hin"I just don't want to burden you with my own troubles..."
                                call changeDominance(1) from _call_changeDominance_39
                                bo"Your trouble, is my trouble [hin_rel]. But you have to be willing to accept my help first!"
                                hin"And h-how would you go about helping [bo_name]? How would we make all that money?"
                                bo"You see, I have a few ideas in mind..."
                                bo"I am already making some money working at my new job, but nowhere near enough to be able to support you..."
                                bo"But I was thinking... What if I could find a way for you to make some money without having to leave the house?"
                                hin"You can... do that?"
                                bo"Maybe! But I still have to give it some thought..."
                                bo"I'll talk to you about it when I am ready, okay?"
                                hin"O-okay..."
                                hin"Is there anything else you wanted to talk about?"
                            "Drop it...":
                                bot"M-maybe not... [hin_rel] is already struggling as is."
                                bo"You are probably right..."
                                bo"..."
                                hin"Is there anything else you wanted to talk about?"
                    menu massagetalkmenu:
                        hin"Is there anything else you wanted to talk about?"
                        "About the Daimyo..." (greyed_out = (aboutthedaimyo_massage>=1)):
                            default aboutthedaimyo_massage = 0
                            $ aboutthedaimyo_massage = 1
                            bo"The Daimyo, did you really meet him?"
                            hin"I did..."
                            bo"I am curious! How was the most powerful man in Konoha... What did he look like? Is he strong?"
                            if daimyomeeting_counter >= 3 and ch1_dy_200paid == False:
                                hin"Uuh..."
                                show daimyo apo2_1 with flash
                                show daimyo apo2_1:
                                    easein 1.5 alpha 0.0
                                hin"He is not... what one would expect."
                                
                                hin"Sleazy and corrupt is how I'd describe him."
                                hin"He treats everyone as if they are beneath him, me and your [na_rel] were not exceptions..."
                                bo"What a piece of shit..."
                                hide daimyo
                                hin"[bo_name_stutter], l-language!"
                                bo"Sounds like he deserves as much! He didn't do anything to you, did he?"
                                show daimyo apologize final1 with flash
                                show daimyo apologize final1:
                                    easein 1.5 alpha 0.0
                                hin"N-no..."
                                hin"I just had to... apologize, for failing to meet our obligations to him."
                                bo"Hmm, we best make sure that won't be the case then in the future..."
                                hin"Indeed..."
                                $ hinatapillsedated = False
                                jump action_taken
                            else:
                                hin"He is not... what one would expect."
                                hin"Sleazy and corrupt is how I'd put it..."
                                hin"He treats everyone as if they are beneath him, me and your [na_rel] were not exceptions..."
                                bo"What a piece of shit..."
                                hin"[bo_name_stutter], l-language!"
                                bo"Sounds like he deserves as much! He didn't do anything to you, did he?"
                                hin"Not really, but he did sound quite threatening when it comes to our debt obligations..."
                                bo"Hmm, we best make sure we stay vigilant then..."
                                hin"Indeed..."
                                $ hinatapillsedated = False
                                jump action_taken


                        "About [na_rel]..." if aboutnaruto_massage == 0:
                            default aboutnaruto_massage = 0
                            $ aboutnaruto_massage = 1
                            bo"[na_rel]... You said he was detained? By who? More importantly... why?"
                            hin"The Daimyo wouldn't share more details. Although he did say it had to do with some political altercations..."
                            hin"But like I said, it's all probably a huge misunderstanding! I am s-sure your [na_rel] would never get caught up in something like that..."
                            bo"[hin_rel]..."
                            show hina nightmassage3 with dissolve
                            hin"Aww..."
                            hin"Are you worried about your [hin_rel_mother]?"
                            scene black with dissolve
                            "[hin_name] stands up to comfort you..."
                            label aboutnaruto_massagelabel:
                            scene bg lr night:
                                zoom 0.69
                            show boruto worried at left
                            show shina worried at right
                            with dissolve
                            hin"Don't be! I am sure everything will turn out to be okay! Just like it always does..."
                            menu:
                                bo"[hin_rel]..."
                                "{color=[dominancecolor]}You know you can rely on me, right?{/color}":
                                    bo"You know you can rely on me, right?"
                                    show shina smiling with dissolve:
                                        xzoom -1
                                    show shina smiling:
                                        easein 1 xalign 0.5
                                    if aboutnaruto_massage == 1:
                                        hin"*Giggles* That much you've already let me know..."
                                    else:
                                        hin"*Giggles* My grown up boy..."
                                    scene hina_massage_conversehug1 with dissolve
                                    if aboutnaruto_massage == 1:
                                        hin"*Giggles* My little man of the house!"
                                    else:
                                        hin"Ready to step up and be the man of the house now, are you?"
                                    bo"As much as you are trying to hide it... It would seem you need me to be."
                                    menu:
                                        bo"As much as you are trying to hide it... It would seem you need me to be."
                                        "{color=[obediencecolor]}Make an inconspicuous move...{/color}":
                                            bo"Right now you need someone, [hin_rel]..."
                                            show hina_massage_conversehug2 with dissolve:
                                                zoom 1.3 yalign 1.0 xalign 0.5
                                            bo"Let me be that someone..."
                                            call checkObedience(16, "asmuchhugfail", "Hinata") from _call_checkObedience_10
                                            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                            hin"*Gasp*"
                                            if aboutnaruto_massage == 1:
                                                call changeObedience("Hinata", 1, "asmuchhugfail",2) from _call_changeObedience_59
                                                hint"H-he's still doing that!"
                                                bo"Will you do that, [hin_rel]?, Will you lean on me for help if you need to?"
                                                hin"V-very valiant of you... I'll keep trying, okay?"
                                            else:
                                                call changeObedience("Hinata", 1, "asmuchhugfail",2) from _call_changeObedience_60
                                                hint"T-this again!?"
                                                bo"If you cannot lean on me for help, then on who else would you lean on [hin_rel]..."
                                                hin"V-very valiant of you... I w-will try, okay?"
                           
                                            show hina_massage_conversehug2 with dissolve:
                                                zoom 1.2
                                            if aboutnaruto_massage == 1:
                                                bot"She's putting up with my advances, I am certain of it..."
                                                bot"Fuck! The things I'd do to your ass [hin_rel]..."
                                                bot"Shall I try pushing it further?"
                                            else:
                                                bot"Damn... Has she not noticed my hand on her ass, or is she finally warming up to me?"
                                                bot"Fuck! The things I'd do to your ass [hin_rel]..."
                                                bot"Shall I try pushing it further?"
                        
                                            menu:
                                                bot"Shall I try pushing it further?"
                                                "{color=[hatredcolor]}(Your ass will be mine, [hin_rel]!){/color}":
                                                    bo"I'll always be here for you, [hin_rel]..."
                                                    hin"T-thank you..."
                                                    show hina_massage_conversehug3:
                                                        zoom 1.6 xalign 0.5 yalign 0.0
                                                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                                    bot"As long as you and your ass are here for me!" with vpunch
                                                    show hina_massage_conversehug3 with dissolve:
                                                        zoom 1.4 xalign 0.5 yalign 1.0
                                                    call changeHatred(1) from _call_changeHatred_79
                                                    hin"[bo_name_stutter]!?"
                                                    "You raised [hin_name]'s ass and pushed her towards you, almost preventing her from breaking away..."
                                                    bo"I told you didn't I, you can lean onto me!"
                                                    hin"W-what are you saying, [bo_name]! Let..."
                                                    scene black with dissolve
                                                    call changeRespect("Hinata", -2) from _call_changeRespect_95
                                                    hin"...Go of me!" with vpunch
                                                    scene bg lr night:
                                                        zoom 0.69
                                                    show boruto bonerevil3 at left
                                                    show shina surprised5:
                                                        xalign 0.5
                                                    with dissolve
                                                    show shina:
                                                        easein 1 xalign 0.8 ypos -24
                                                    call increaselust(40) from _call_increaselust_66
                                                    show shina at smallshake
                                                    hint"H-his condition..."
                                                    show shina angry with dissolve
                                                    if aboutnaruto_massage == 1:
                                                        hin"One day you say you want to help, the n-next you act like this!?"
                                                        hin"Even after last time!?" with vpunch
                                                    else:
                                                        hin"F-first you say you want to help, and t-then you act like this!?"
                                                    call changeRespect("Hinata", -2) from _call_changeRespect_96
                                                    hin"I know your condition is t-troubling you, but you cannot be acting out like this!"
                                                    hide shina with dissolve
                                                    hin"I am having another talk with Lady Tsuande!"
                                                    hin"And p-please, take care of your condition!" with vpunch
                                                    bot"God damn it! All my condition's good for is giving me blue balls!"
                                                    bot"Fuck! I need to find some sort of release, and fast..."
                                                    hide boruto with dissolve
                                                    jump action_taken
                                                "{color=[lovecolor]}(Probably a bad idea...){/color}":
                                                    bot"Nah, that's probably a bad idea. I am already pushing my luck..."
                                                    scene hina_massage_conversehug1 with dissolve
                                                    bo"I'll always be here for you, [hin_rel]..."
                                                    hint"M-must have been accidental, he is still my sweet boy after all!"
                                                    call changeLove("Hinata", 1,"asmuchhugfail", 2) from _call_changeLove_32
                                                    hin"And I'll be here for you!"
                                                    scene black with dissolve
                                                    "You let go of each other..."
                                                    scene bg lr night:
                                                        zoom 0.69
                                                    show boruto normal at left
                                                    show shina smiling:
                                                        xalign 0.5 xzoom -1
                                                    with dissolve
                                                    show shina:
                                                        easein 1 xalign 0.8 ypos -28
                                                    hin"Thanks for taking some time to talk with me, and comfort me..."
                                                    call changeRespect("Hinata", 1) from _call_changeRespect_97
                                                    hin"I appreciate that!"
                                                    bo"Of course, [hin_rel]!"
                                                    hide boruto with dissolve
                                                    bo"Talk to you later!"
                                                    jump action_taken
                                                    label asmuchhugfail:
                                                        hint"W-what is he doing!?"
                                                        bo"Will you do that, [hin_rel]?, Will you lean on me for help if you need to?"
                                                        hin"Uhm... C-can you let go of me [bo_name]?"
                                                        scene hina_massage_conversehug1 with dissolve
                                                        bo"O-oh, O-okay..."
                                                        scene black with dissolve
                                                        "You let go of her..."
                                                        scene bg lr night:
                                                            zoom 0.69
                                                        show boruto surprised2 at left
                                                        show shina shy:
                                                            xalign 0.5 xzoom -1
                                                        with dissolve
                                                        show shina:
                                                            easein 1 xalign 0.8 ypos -28
                                                        hin"I d-don't know if I can do that yet, with your c-condition and everything..."
                                                        call changeRespect("Hinata", -1) from _call_changeRespect_98
                                                        show boruto worried with dissolve
                                                        bot"Fuck! she must have felt me grabbing her ass..."
                                                        hin"But I appreciate you trying... Okay?"
                                                        bo"Of course, [hin_rel]!"
                                                        hide boruto with dissolve
                                                        bo"Talk to you later, I guess..."
                                                        $ hinatapillsedated = False
                                                        jump action_taken
                                                
                                        "Don't":
                                            bo"If you cannot lean on me for help, then on who else would you lean on [hin_rel]..."
                                            hin"V-very valiant of you... I w-will try, okay?"
                                            scene black with dissolve
                                            "You let go of each other..."
                                            scene bg lr night:
                                                zoom 0.69
                                            show boruto normal at left
                                            show shina smiling:
                                                xalign 0.5 xzoom -1
                                            with dissolve
                                            show shina:
                                                easein 1 xalign 0.8 ypos -28
                                            hin"Thanks for taking some time to talk with me, and comfort me..."
                                            call changeRespect("Hinata", 1) from _call_changeRespect_99
                                            hin"I appreciate that!"
                                            bo"Of course, [hin_rel]!"
                                            hide boruto with dissolve
                                            bo"Talk to you later!"
                                            $ hinatapillsedated = False
                                            jump action_taken
                                        
                                "You are right, I am sure he'll be back soon":
                                    bo"You are probably right, I am sure [na_name] will be back soon..."
                                    show shina smiling with dissolve
                                    hin"He will!"
                                    hin"Thanks for taking some time to talk with me, and comfort me..."
                                    call changeRespect("Hinata", 1) from _call_changeRespect_100
                                    hin"I appreciate that!"
                                    bo"Of course, [hin_rel]!"
                                    hide boruto with dissolve
                                    bo"Talk to you later!"
                                    $ hinatapillsedated = False
                                    jump action_taken
                                
                        "[na_rel]... He is still away" if aboutnaruto_massage>=1:
                            bo"[na_rel]... He is still away."
                            hin"H-he is... are you worried about him?"
                            bo"Worried about [na_name]? Heck no! I am sure he'll be fine!"
                            bo"You on the other hand, you must be feeling lonely..."
                            show hina nightmassage3 with dissolve
                            hin"Aww..."
                            hin"Are you worried about your [hin_rel_mother]?"
                            scene black with dissolve
                            "[hin_name] stands up to comfort you..."
                            jump aboutnaruto_massagelabel

                        

                    jump lr_massage_menu_talk


                
        "{color=[obediencecolor]}You didn't have to sit-up you know...{/color}":
            if lr_massagecounter == 100:
                bo"You didn't have to sit-up you know..."
                hin"Oh? Do you have something in mind?"
                label jumpfromfeetmassage:
                bo"I was thinking I could help you relax a little bit..."
                scene black with dissolve
                bo"Just have to let me, and you..."
                scene fm2_start with dissolve
                bo"Get comfortable!"
                hin"C-comfortable, eh?"
                hin"How would you go about doing that..."
                menu couchmasssage1:
                    hin"How would you go about doing that..."
                    "{color=[obediencecolor]}Uhhh, I was thinking...{/color}" if massageknowledge == 0:
                        bot"I didn't even expect to get this far..."
                        bot"It would seem [hin_rel] is opening up to me a little bit!"
                        show fm2_start_1 with dissolve
                        with vpunch
                        bo"Uuuh, what if you let me massage your legs a little bit..."
                        "You tried to inconspicuously place your hands on [hin_name]'s legs, but your sudden advances caught her off guard."
                        call changeObedience("Hinata", 1,"couchmasssage1") from _call_changeObedience_61
                        hint"Where is he placing his r-right hand at!"
                        hin"M-m-maybe some other time, I still have a few chores I have to tace care of..."
                        show fm2_start_2 with dissolve
                        bot"Shit! Did I move to fast?"
                        bot"But her ass felt so nice! How do I convince her to let me offer her a full body massage..."
                        hin"D-do you mind?"
                        scene fm2_start with dissolve
                        bo"O-oh... M-maybe some other time then!"
                        scene black with dissolve
                        hin"Maybe..."
                        jump action_taken

                    "{color=[hatredcolor]}Use the pills!{/color}" if lr_massagecounter >= 100 and pillsinv != None and pillsusedatleastonce == True:
                        bot"What if I..."
                        bo"On second thought..."
                        bo"What would you say if I prepared your favorite Chai tea to go along with a nice massage?"
                        show fm2_start_face2 with dissolve
                        hin"O-oh! Just like last time?"
                        bo"Precisely like last time!"
                        hin"Y-you... you would do all that for me!?"
                        show fm2_start_1 with dissolve
                        bo"Of course! I'd do that and much more for you, [hin_rel]!" with vpunch
                        hin"O-oh!"
                        bo"Would you give me some space then?"
                        call changeObedience("Hinata", 1) from _call_changeObedience_62
                        hin"R-right! I'll be patiently waiting then!"
                        scene black with dissolve
                        scene bg lr hinanight massage with dissolve
                        show boruto sceeming2 at center with dissolve
                        bot"Hehe!"
                        show boruto sceeming3 with dissolve
                        bot"This could present an interesting opportunity!"
                        show boruto:
                            easein 2 xpos -1000
                        pause 1
                        scene kitchen night with dissolve
                        show boruto sceeming3 at center with dissolve
                        scene black with dissolve
                        call useItem(pills,1) from _call_useItem_2
                        "You spent some time washing the dishes and preparing [hin_name]'s favorite drink... with an extra ingredient mixed in!" 
                        scene bg lr hinanight massage with dissolve
                        show boruto sceeming2 at left with dissolve
                        bot"Here we go!"
                        bo"One steaming Chai tea, made with love for the best [hin_rel_mother] in the world!"
                        show boruto:
                            easein 0.5 xalign 0.5
                        scene black with dissolve
                        "You hand over the spiked drink to [hin_name]..."
                        scene bg lr hinanight massage:
                            blur 10

                        show hina nightmassage_tea:
                            yalign 0.0 xalign 0.5
                        with dissolve
                        hin"T-thank you so much, [bo_name]!"
                        hin"Lord knows I could use this moment of reprieve..."
                        
                        show hina nightmassage_tea2 with dissolve:
                            zoom 1.24 xalign 0.5 yalign 1.0
                    
                        show hina:
                            easein 0.5 yalign 0.0
                        hin"Such a nice blend of sweetness and spice!"
                    
                        hin"Tastes just as good as the last time. Thank you!"
                        bo"Of course!"
                    
                        bo"Now, would you please lay on the sofa like you were before for me?"
                        scene black with dissolve
                        hin"Y-yes my little masseur expert!"
                        show fm2_start_2 with dissolve
                        bo"Now sit back and allow me to work my magic!"
                        show fm2_start_2_pills1 with dissolve
                        hin"Y-you do that... I'll just... relax a little bit..."
                        bot"She's already feeling it!"
                
                        bo"You see, to promote blood circulation, it's important that I make moves that..."
                        show fm2_start_1
                        show fm2_start_2_pills2_face
                        with dissolve
                        bo"Stroke upwards towards the heart..." with vpunch
                        hin"Y-yes... I'm a little bit... t-tired..."
                        bot"She hasn't even menitoned me reaching for her ass!"
                        scene hin_legmassageanim1
                        show fm2_start_2_pills2_face
                        with dissolve
                        bo"It's ok [hin_rel], I'll take care of you..."
                        hin"O-okay..."
                        "You spent some time stroking [hin_name]'s legs and taking every opportunity to cop a feel of her ass..."
                        scene black with dissolve
                        hin"I... n-need to..."
                        show fm2_start2 with dissolve
                        hin"...S-sleep... f-for a..."
                        show fm2_start2 with dissolve:
                            zoom 1.3 xalign 1.0 yalign 1.0
                        hin"...*Snorts*" with vpunch
                        bo"S-sure!" with dissolve
                        bot"She's almost completely out!"
                        bo"You wouldn't mind if I..."
                        show fm2_start2_5 with dissolve:
                            zoom 1.3 xalign 1.0 yalign 1.0
                        bo"Massaged your b-back a little bit... Right?"
                        hin"...U-uh *Snorts*"
                        call increaselust(10) from _call_increaselust_67
                        bot"I'll never get another opportunity like this..."
                        "Click twice to make a move!"
                        call clicktwice from _call_clicktwice_5
                        show hin_massagegrope1 with dissolve:
                            zoom 1.3 xalign 1.0 yalign 1.0
                        call increaselust(40) from _call_increaselust_68
                        bot"Fuck me! What an ass she has on her..."
                        bot"S-softer than anything I've touched before..."
                        bo"[hin_rel_stutter]...?"
                        hin"..."
                        show fm2_start2_5_1:
                            zoom 1.3 xalign 1.0 yalign 1.0
                        show fm2_mast3_face1:
                            zoom 1.3 xalign 1.0 yalign 1.0
                        with dissolve
                        bot"Fuck it! Might as well use the opportunity..."
                        scene black with vpunch
                        $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                        bot"Hehe..."
                        show fm2_mast1:
                            zoom 1.3 xalign 1.0 yalign 1.0
                        show fm2_mast3_face1 zorder 100:
                            zoom 1.3 xalign 1.0 yalign 1.0
                        with dissolve
                        bot"I can't make any sudden movements in this position, but if I carefully slide my cock in between her shins..."
                        show hin_massagegrope1_masturbate with dissolve:
                            zoom 1.3 xalign 1.0 yalign 1.0
                        $ renpy.sound.play("/audio/soun_fx/jerkoffclothes.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                        $ renpy.sound.play("/audio/soun_fx/groperepeat3.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                        bot"I am sure I can relieve myself from some of my 'frustrations'!"
                        "You start carefully masturbating while groping [hin_name]'s ass."
                        bot"Should be easy enough when I can freely grope [hin_rel]'s glorious ass!"
                        show fm2_mast3_face2 zorder 101 with vpunch:
                            zoom 1.3 xalign 1.0 yalign 1.0
                        hin"[bo_name_stutter]...?" with vpunch
                        bot"S-shit!"
                        bo"Y-yes [hin_rel_stutter]?"
                        hin"N-not so..."
                        hin"... *Snorts*"
                        hide fm2_mast3_face2 with dissolve
                        bo"A-as you wish!"
                        bot"F-fuck, I am not a-about to stop now...!"
                        bot"I am... c-cumming!"
                        scene fm2_mast2_2:
                            zoom 1.3 xalign 1.0 yalign 1.0 
                        show fm2_mast3_face2 zorder 100:
                            zoom 1.3 xalign 1.0 yalign 1.0
                        show fm2_start_2_cumpro:
                            zoom 1.3 xalign 1.0 yalign 1.0
                        $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                        with flash
                        $ renpy.sound.play("/audio/soun_fx/grope2.opus", channel="sfx3", loop=False, relative_volume = 0.9)
                        bo"*Silent grunt* U-ugh!"
                        call changeHatred(2) from _call_changeHatred_80
                        "You squeezed [hin_name]'s ass as hard as you could while climaxing!"
                        show fm2_mast3:
                            zoom 1.3 xalign 1.0 yalign 1.0 
                        hide fm2_mast2_2
                        with flash
                        call decreaselust(40) from _call_decreaselust_65
                        "A large amount of semen covered her feet, while you tried your best to stay silent, alas..."
                        bot"F-fuck! There's m-more coming!"
                        show fm2_mast3_1:
                            zoom 1.3 xalign 1.0 yalign 1.0
                        hide fm2_mast3
                        show fm2_start_2_cumpro zorder 1000:
                            zoom 1.3 xalign 1.0 yalign 1.0
                        $ renpy.sound.play("/audio/soun_fx/cum2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                        with flash
                        hide fm2_start_2_cumpro with dissolve
                        call decreaselust(40) from _call_decreaselust_66
                        $ renpy.sound.play("/audio/soun_fx/panting.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                        hide fm2_mast3_face2
                        hide fm2_mast3_face1
                        with dissolve
                        bot"*Panting*"
                        bot"D-damn it! [hin_rel]'s ass is irresistible..."
                        bot"I can't keep doing this to her, I have to find other ways to satisfy my desires..."
                        bot"Or perhaps [hin_rel] would satisfy them in the future!"
                        bot"F-fuck me, it felt so good..."
                        bot"But how the hell do I get out of t-this..."
                        bot"I should try my best to clean up before she wakes up..."
                        bo"Uuuh... D-don't mind me [hin_rel]..."
                        scene black with dissolve

                        "You carefully clean up as much of the semen as you could off [hin_name]'s legs and leave her laying on the couch..."
                        scene bg lr hinanight massage with dissolve
                        show boruto bonersurprised with dissolve:
                            xalign 0.3
                        bot"Time to get out of here!"
                        scene black with dissolve
                        $ pillsusedatleastonce = True
                        $ hinatapillsedated = True
                        jump action_taken











                    "{color=[obediencecolor]}Use your newfound knowledge!{/color}" if massageknowledge >= 1:
                        bo"You just have to sit back and relax..."
                        bot"Now according to my newfound knowledge..."
                        label usenewfoundknowledge:
                        $ initialize_replay_defaults()
                        show fm2_start_2 with dissolve
                        bo"You see, our legs are the foundation of our mobility and given the constant demands of movement, leg muscles are extremely prone to tension, stiffness, and fatigue."
                        bo"One easy way to relief such tension is by stimulating blood circulation. But since our legs are the furthest from our hearts, to do so one would have to..."
                        show fm2_start_1 with dissolve
                        bo"Stroke upwards towards the heart..."
                        "You use your deep knowledge of the subject to inconspicuously place your hand on [hin_name]'s upper thighs..."
                        show hin_legmassageanim1 with dissolve
                        hin"O-oh! S-since when did you get so knowledgeable..."
                        bo"I told you, didn't I? I've been studying this stuff..."
                        hin"I do have to concede to you, your movements are quite... e-effective!"
                        hin"It truly does feel like it helps..."
                        bo"R-right?"
                        scene black with dissolve
                        hin"Can I just... get a little bit more comfortable?"
                        show fm2_start2 with dissolve
                        bo"S-sure!" with dissolve
                        show fm2_start2 with dissolve:
                            zoom 1.2 xalign 1.0 yalign 1.0
                        hin"Maybe you can work on my calfs a little bit too..."
                        bot"F-fuck! [hin_rel]'s legs are pressing against my crotch..."
                        call increaselust(10) from _call_increaselust_69
                        bot"Is she oblivious to what this does to me? I mean..."
                        bot"Her sexy, athletic legs are brushing against my cock! How am I supposed to not get an erection..."
                        hin"S-so...? Are you waiting for something?"
                        show fm2_start2_2 with dissolve:
                            zoom 1.2 xalign 1.0 yalign 1.0
                        bo"R-right on it!"
                        show fm2_start2_3 with dissolve:
                            zoom 1.2 xalign 1.0 yalign 1.0
                        bot"[hin_rel]'s ass is just a few inches away!"
                        show hin_legmassageanim2 with dissolve:
                            zoom 1.2 xalign 1.0 yalign 1.0
                        bot"Shall I try going up there?"
                        bot"Maybe I shall warm her up a little bit before that..."
                        bo"This technique is called 'Effleurage'. The light, soothing stroking motions are supposed to help the muscles relax..."
                        hin"A-ah... *Exhales*"
                        bo"But if you really want to penetrate deeper layers of muscle tissue..."
                        menu depperlayers:
                            bo"But if you really want to penetrate deeper layers of muscle tissue..."
                            "{color=[dominancecolor]}Make a ballsy move!{/color}":
                                call checkDominance(8, "depperlayersfail") from _call_checkDominance_3
                                bo"Then you have to apply a little bit of pressure. Something like..."
                                show fm2_start2_5 with dissolve:
                                    zoom 1.2 xalign 1.0 yalign 1.0
                                with vpunch
                                bo"This..."
                                call checkObedience(15,"depperlayersfailhin", "Hinata") from _call_checkObedience_11
                                
                                hin"O-oh!" with vpunch
                                show hin_legmassageanim3 with dissolve:
                                    zoom 1.2 xalign 1.0 yalign 1.0
                                hint"Did he just... move his hand to my glutes?"
                              
                                bo"This technique is called 'Petrissage'..."
                                bo"The pinching and kneading motions are essential in treating muscle knots and spasms..."
                                bo"It might hurt a little bit, but the deep pressure strokes are what really make a difference..."
                                hin"A-ahh... *Exhales* I s-see..."
                                bot"And also what allows me to feel your magnificent ass [hin_rel]!"
                                bot"Holy shit! I can't believe you are just sitting there almost moaning while I keep copping a feel of your ass..."
                                hin"[bo_name_stutter]...?"
                                call increaselust(10) from _call_increaselust_70
                                hin"It feels good, and it seems like you really know your s-stuff but..."
                                call changeObedience("Hinata", 1, "depperlayers", 3) from _call_changeObedience_63
                                
                                if percentage >= 80:
                                    call checkLust(80) from _call_checkLust_3
                                    bot"F-fuck! I am g-getting a huge erection right now..."
                                    bot"I can't take this shit any longer!"
                                    show fm2_mast2_1 with dissolve
                                    bo"I'll be d-done in just a minute [hin_rel]..."
                                    hin"S-sure but..."
                                    hin"Isn't t-this massage a l-little bit too t-touchy?"
                                    bo"It's like I s-said..."
                                    show hin_massagegrope1_masturbate with dissolve
                                    bo"Petrissage..." with vpunch
                                    bo"...Effleurage" with vpunch
                                    bot"I am about to..." with flash
                                    bot"F-fucking explode" with flash
                                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                                    scene black with vpunch
                                    hin"[bo_name_stutter]!!?" with vpunch
                                    show fm2_start_1 with vpunch:
                                        zoom 1.5 xalign 0.0
                                    hin"*Gasps* W-WHY IS Y-YOUR..."
                                    scene black with vpunch
                                    hin"G-get off me r-right this moment!"
                                    scene bg lr night:
                                        zoom 0.69
                                    show boruto bonersurprised at right
                                    show shina surprised3 at left
                                    with dissolve
                                    bo"[hin_rel_stutter]! It's n-not what you think!"
                                    hin"W-what were you t-thinking, [bo_name_stutter]!"
                                    bo"It.. it just happened on its own! My t-thing just poked through my pants!"
                                    hin"D-don't lie to me [bo_name_stutter]! I saw what you were d-doing with it!"
                                    call changeRespect("Hinata", -5) from _call_changeRespect_101
                                    hin"H-have you no shame? No self control!?"
                                    call changeRespect("Hinata", -5) from _call_changeRespect_102
                                    hin"I am your [hin_rel] for goodness's sake!"
                                    bo"But [hin_rel], it was accidental! A-and my condi-"
                                    hin"This conversation is over!" with vpunch
                                    hin"I won't hear any more of your excuses!" with vpunch

                                    hide shina with dissolve
                                    hin"You better take care of your condition, or I will lock you in the infirmary until you get better!"
                                    hin"Lady Tsunade will hear of this too!"
                                    if tsunadeintroduction == False:
                                        $ tsunadeintroduction = True
                                        $ notification ("Infirmary unlocked")
                                        "You can now visit the Infirmary during mornings or evenings using the map."
                                    bot"S-shit! I really fucked this one up. [hin_rel] must have lost any respect she had for me..."
                                    call increaselust(10) from _call_increaselust_71
                                    bot"And I didn't even get to blow my load!"
                                    bot"Fuck!... I should be more careful with how I manage my condition..."
                                    hide boruto with dissolve
                                    dev"Allowing your condition to run rampart will sometimes result in events that will have those close to you losing their respect for you."
                                    dev"Allowing their respect to fall in negative values might prevent you from taking certain actions."
                                    dev"You can earn respect back by making sensible decisions, helping, or providing gifts to any of the girls."
                                    jump action_taken

                                else:
                                    pass
                                hin"But this might be a little too... t-touchy for my preference!"
                                
                                bo"O-oh, I am sorry! I was just making sure I cover all the key areas..."
                                scene fm2_start2_4 with dissolve
                                hin"You don't have to apologize..."
                                scene black with dissolve
                                "[hin_name] turns around..."
                                show fm2_start_2 with dissolve
                                hin"T-thanks for helping, but I have to get back to taking care of some chores..."
                                bo"Anytime..."
                                if quest_hin.exists("hin1L_2") and not _in_replay: #check if quest exists
                                    if quest_hin.is_state("hin1L_2", "pending"): #check quest state
                                        
                                        $ quest_hin.check("hin1L_2", "done") #update hinata shower quest to strikethrough if already completed
                                        $ quest_hin.check("hin1L_2", "done")
                                        $ notification (f"{hin_name} Love objective completed")
                                hin"I am seeing the effort you are putting into m-managing your condition..."
                                call changeLove("Hinata", 1, "depperlayers") from _call_changeLove_33
                                hin"T-thank you for that. Keep it up, Okay?"
                                bo"Y-yeah... Let me know if I can help some more in the future!"
                                call changeRespect("Hinata", 1) from _call_changeRespect_103
                                show fm2_start with dissolve
                                hin"I'll... keep that in mind."
                                show black with dissolve
                                bot"Fuck me... I am this close to having [hin_rel] asking for full body massages!"
                                bot"I wonder how far I could go with this..."
                                jump action_taken
                                label depperlayersfail:
                                    bot"Uuuuh... I don't know if I should do that. Probably a bad idea..."
                                    jump depperlayers
                                label depperlayersfailhin:
                                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp3.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                    hin"*Gasp* [bo_name_stutter]!"
                                    show hin_legmassageanim2 with dissolve:
                                        zoom 1.2 xalign 1.0 yalign 1.0
                                    hint"Did he just... p-pinch my glutes?"
                                    bo"W-what's wrong, [hin_rel]?"
                                    hin"T-that's enough for now..."
                                    show black with dissolve
                                    "[hin_name] quickly turns around..."
                                    show fm2_start_2 with dissolve
                                    hin"T-thanks for trying to help but I have to get back to taking care of some chores..."
                                    bo"O-oh... Okay."
                                    bo"Let me know if I can help some more in the future..."
                                    call changeRespect("Hinata", -1) from _call_changeRespect_104
                                    hin"Ok, but do you m-mind?"
                                    show fm2_start with dissolve
                                    bo"R-right... My bad!"
                                    show black with dissolve
                                    bot"Shit... Guess I moved too fast!"
                                    $ hinatapillsedated = False
                                    $ renpy.end_replay()
                                    jump action_taken




                            "Keep your current pace...":
                                bo"You have to apply some extra pressure..."
                                bo"Would you like for me to do that...?"
                                hin"I don't think s-so... B-but you can keep doing what you are doing..."
                                hin"I have to say... it f-feels quite nice."
                                "You spent some time massaging [hin_name]'s legs..."
                                scene black with dissolve
                                "[hin_name] turns around..."
                                show fm2_start_2 with dissolve
                                hin"T-thanks for helping, but I have to get back to taking care of some chores..."
                                bo"Anytime..."
                                bo"Let me know if I can help some more in the future..."
                                call changeRespect("Hinata", 1) from _call_changeRespect_105
                                show fm2_start with dissolve
                                hin"I'll... keep that in mind."
                                show black with dissolve
                                bot"I wonder how far I could go with this..."
                                $ hinatapillsedated = False
                                $ renpy.end_replay()
                                jump action_taken
                            




                        
                    "{color=[obediencecolor]}(Hint){/color}" if massageknowledge < 1:
                        "Increase your knowledge of massage techniques to unlock this option!"
                        "Maybe the shop could have a useful item for that..."
                        jump couchmasssage1
                    

            $ lr_massagecounter += 1
            bo"You didn't have to sit-up you know... I understand you are tired."
            hin"But then there would be no space for you..."
            show hina nightmassage_feet1 with dissolve
            bo"Of course there would, you'd just have to lay your feet on my lap..."
            call changeObedience("Hinata", 1, "v1_night_massage_talk") from _call_changeObedience_28
            show hina nightmassage_feet1 with dissolve:
                zoom 1.2 xalign 0.5 yalign 1.0
            hin"M-my feet... on your lap?"
            hide hina nightmassage_feet1 with dissolve
            scene hina nightmassage2 with dissolve:
                zoom 1.25 xalign 0.5 yalign 1.0
            show hina nightmassage2:
                easein 5 yalign 0.0
            hin"As much as I am tired..."
            hin"I... I don't think that's a good idea [bo_name_stutter]..."
            hin"Besides, I have some chores to take care of before I call it a night so..."
            hin"I'll see you later, okay?"
            $ hinatapillsedated = False
            jump action_taken
        "{color=[obediencecolor]}Offer some stress relief...{/color}" if lr_massagecounter >= 1:
            bo"Come on [hin_rel], I know you are tired. I could help you relieve some stress if you wanted..."
            if lr_massagecounter >= 100:
                hin"You mean like last time, w-with my feet?"
                menu offersomestressreliefmenu:
                    hin"You mean like last time, w-with my feet?"
                    "Sure!":
                        bo"Sure! If you'd like that..."
                        hin"Hmm... I don't see why not!"
                        hin"It felt pretty good last time..."
                        show hina nightmassage3 with dissolve:
                            zoom 1.25 xalign 0.5 yalign 1.0
                        show hina nightmassage3:
                            easein 5 yalign 0.0
                        bo"Right?"
                        hin"Shall I put my feet up then?"
                        bo"Getting into it, aren't you [hin_rel]!"

                        hin"*Giggles* Come on then, show me that renowned technique of yours..."
             
                        show fm_start_1 with dissolve
                        bo"Ready?"
                        hin"Go on then!"
                        show fm_start
                        show fm_start_face1
                        with dissolve
                        hin"A-ah!..."
                        bot"[hin_rel] is a bit more open to my advances if I am not an asshole..."
                        show fm_start_face1 with dissolve
                        show hin_footmassageanim1 with dissolve
                        bot"I wonder how much further can I push her..."
                        bo"Shall I keep going?"
                        hin"A-ah! Y-yes please. It f-feels nice..."
                        bo"I am somewhat of an expert after all..."
                        hin"I wouldn't go that far... *Giggles*"
                        bo"Oh yeah? I bet you'd be begging for more if I showed you more of my expertise!"
                        if massageknowledge == 1:
                            hin"You really are getting better at this, I'll give you that much, but..."
                        hin"M-maybe some other time..."
                        "You spent some time taking helping [hin_name] some stress..."
                        "Click twice to continue."
                        call clicktwice from _call_clicktwice_6
                        scene fm_start_1 with dissolve
                        hin"But thank you for providing some relief again!"
                        scene hina nightmassage3 with dissolve:
                            zoom 1.25 xalign 0.5 yalign 1.0
                        show hina nightmassage3:
                            easein 2 yalign 0.0
                        call changeRespect("Hinata",1) from _call_changeRespect_106
                        hin"I really needed that after a stressful day..."
                        bo"Of course! Let me know if I can help with more than just your feet..."
                        if massageknowledge == 1:
                            hin"Hmm, you know what...?"
                            hin"Would you mind if you worked on my legs just a tiny bit?"
                            bo"Of course!"
                            scene black with dissolve
                            bot"Oh shit! I didn't expect her to take initiative herself..."
                            hin"Come on then, sit along with me!"
                        
                            jump usenewfoundknowledge
                        hin"I'll have to think about that but I might have to take you up on your services some time soon again! *Giggles*"
                        scene black with dissolve
                        bot"It feels like I am close to convincing her to let me 'help' her some more..."
                        bot"I shall check the store, maybe there's something that'll be of use..."
                        $ hinatapillsedated = False
                        jump action_taken


                    "{color=[obediencecolor]}I was thinking something more...{/color}":
                        bo"I had something else in mind..."
                        bo"Maybe you could lay down like you were..."
                        hin"L-lay down?"
                        jump jumpfromfeetmassage
                    "{color=[hatredcolor]}(Hint){/color}" if lr_massagecounter >= 100 and pillsinv == None and pillsusedatleastonce == False:
                        bot"Fuck! I want to feel more of [hin_rel], but I am sure she'd push me away..."
                        bot"What If I could get her to be a little extra 'tired', or even asleep!"
                        bot"Hehe! I am getting some wicked ideas! I should check the shop and see if there's anything that might be useful..."
                        jump offersomestressreliefmenu

                    "{color=[hatredcolor]}Sedate her again!{/color}" if lr_massagecounter >= 100 and pillsinv == None and pillsusedatleastonce == True:
                        bot"Fuck me! I want to defile [hin_rel] once again, but those pills are so expensive..."
                        "You have no pills to use..."
                        jump offersomestressreliefmenu
                    "{color=[hatredcolor]}Use the pills!{/color}" if lr_massagecounter >= 100 and pillsinv != None:
                        
                        default pillsusedatleastonce = False
                        bo"I was thinking something... more than that!"
                        if pillsusedatleastonce == True:
                            bo"I could take care of some chores and prepare your favourite tea! Just like last time..."
                            hin"R-really? Y-you'd do all that for me again?"
                        else:
                            bo"You see, you deserve a little break every now and then with all the chores you get done by yourself..."
                            hin"...Oh?"
                            bo"How about I prepare your favourite chai tea for once, I'll wash the dishes too while I am at it, and then I'll join you and give you another one of my renowned massages!"
                            hin"Y-you... you would do all that for me!?"
                        bo"Of course! I'd do that and much more for you, [hin_rel]!"
                        call changeRespect("Hinata", 1) from _call_changeRespect_107
                        if pillsusedatleastonce == True:
                            hin"Last time I got so lost in the moment! I think I might have relaxed a little bit too much during your massage! *Giggles*"
                            hin"I don't remember much from that night..."
                            hin"But I do remember waking up later that night feeling rejuvenated!"
                            menu:
                                hin"But I do remember waking up later that night feeling rejuvenated!"
                                "{color=[hatredcolor]}Oh yeah! I made sure of that...{/color}":
                                    bo"Oh yeah? I made sure I gave you a thorough massage that day! *Hehe*"
                                    bo"It would seem it worked wonders on you!"
                                    hin"I g-guess so! Thanks for that..."
                                    call changeHatred(1) from _call_changeHatred_81
                                    bot"She has no idea she was covered in my semen!"
                                    bo"Another one of those then?"
                                    
                                "{color=[obediencecolor]}I suppose I am that good with my hands, eh?{/color}":
                                    bo"I suppose I am that good with my hands then, wouldn't you say so [hin_rel]?"
                                    call changeObedience("Hinata", 1) from _call_changeObedience_64
                                    hin"E-evidently! Y-you were doing a great job!"
                                    bo"Hehe! T-thanks!"
                                    bot"She has no idea she was covered in my semen!"
                                    bo"Another one of those then?"
                                
                        else:
                            pass
                        hin"How nice of you! I'll be waiting anxiously then!"
                        bo"I'll be back in just a few minutes!"
                        scene bg lr hinanight massage with dissolve
                        show boruto sceeming2 at center with dissolve
                        bot"Hehe!"
                        show boruto sceeming3 with dissolve
                        bot"My plan is in motion!"
                        show boruto:
                            easein 2 xpos -1000
                        pause 1
                        scene kitchen night with dissolve
                        show boruto sceeming3 at center with dissolve
                        bot"These fucking pills better work..."
                        scene black with dissolve
                        call useItem(pills,1) from _call_useItem_3
                        label replay_hinatafootjobpills:
                        $ initialize_replay_defaults()
                        "You spent some time washing the dishes and preparing [hin_name]'s favourite drink... with an extra ingredient mixed in!" 
                        scene bg lr hinanight massage with dissolve
                        show boruto sceeming2 at left with dissolve
                        bot"Here we go!"
                        bo"One steaming Chai tea, made with love for the best [hin_rel_mother] in the world!"
                        show boruto:
                            easein 0.5 xalign 0.5
                        scene black with dissolve
                        "You hand over the spiked drink to [hin_name]..."
                        scene bg lr hinanight massage:
                            blur 10

                        show hina nightmassage_tea:
                            yalign 0.0 xalign 0.5
                        with dissolve
                        hin"T-thank you so much, [bo_name]!"
                        hin"Lord knows I could use this moment of reprieve..."
                        scene black
                        hin"BUT!" with vpunch
                        bot"O-oh shit! Is she onto me!?"
                        show hina nightmassage_tea2 with dissolve:
                            zoom 1.24 xalign 0.5 yalign 1.0
                        
                        hin"Oooooh....?"
                        show hina:
                            easein 0.5 yalign 0.0
                        hin"Such a nice blend of sweetness and spice!"
                        hin"Made with so much love by my boy! It warms my little heart!"
                        scene hina nightmassage_tea with dissolve:
                            zoom 1.26 xalign 0.5 yalign 1.0
                        "[hin_name] takes a few more sips of the tea you served her..."
                        show hina:
                            easein 2 yalign 0.0
                        
                        if pillsusedatleastonce == True:
                            hin"Tastes just as good as the last time, thanks!"
                            bo"Of course!"
                        else:
                

                            hin"I was skeptical at first, but it would seem you are a man of many talents, aren't you [bo_name]? *Giggles*"
                            bo"Haha *Nervous laughter* It w-would appear s-so!"
                            bot"Phew! Everything's going according to plan so far..."
                        bo"Now, for the main event! Are you ready for one of my renowned massages?"
                        scene black with dissolve
                        hin"Y-yes please!"
                        hin"I just have to put up my feet up like last time..."
             
                        show fm_start_1 with dissolve
                        hin"...Right?"
                        bo"Ready?"
                        hin"Go on then!"
                        show fm_start
                        show fm_start_face1
                        with dissolve
                        if pillsusedatleastonce == True:
                            bot"Fuck me! I am already excited thinking about last time... Hopefully this shit works, and fast!"
                        else:
                            bot"Fuck! Will this shit even work? She took quite a few sips, but it doesn't seem to be having any effect yet..."
                        hin"A-ah!... *Soft Moan*"
                        call increaselust(10) from _call_increaselust_72
                        if pillsusedatleastonce == True:
                            bot"I can't get enough of [hin_rel]'s little moans..."
                        else:
                            bot"Although [hin_rel]'s soft moans are certainly having an effect on me!"
                        show fm_start_face1 with dissolve
                        show hin_footmassageanim1 with dissolve
                        hin"A-ah.. It's been so long since I've had a chance to just sit back and relax."
                        hin"T-thank you for doing this for me, [bo_name]..."
                        bo"Don't even mention it..."
                        hin"All this build up s-stress, It feels like it's accumulating..."
                        hin"Day..."
                        show fm_start_face2 with dissolve
                        hin"By... Day..."
                        bot"Is she..."
                        bo"I know that feeling, [hin_rel]..."
                        hin"A-ah... *Soft Moan*"
                        bo"Just sit back and enjoy... I'll take care of you!"
                        hin"...I... am... r-really... t-tired..."
                        bot"Shit! It's really working! [hin_rel]'s on the brink of falling asleep!"
                        hin"...[bo_name_stutter]?"
                        hin"W-where... am... I?"
                        bot"S-she's completely gone!"
                        menu:
                            bot"S-she's completely gone!"
                            "{color=[hatredcolor]}Fucking finally! It's time I get what I want!{/color}":
                                $ hinatapillsedatedregret == False
                                bot"Fucking finally! Enough of your god-damned teasing [hin_rel]!"
                                bot"Every time you woke me up shaking your ass around my room..."
                                bot"Every time you hugged me and pressed your enormous tits against my chest..."
                                bot"Every time I blew my load thinking about you..."
                                if introsecrethatredcummed == True:
                                    bot"Even that time I sneaked into your bedroom and covered you in my semen..."
                                if secretscenelovehandjob == True:
                                    bot"Even that time you jerked me off in the shower..."
                                bot"All I could ever think about is using every part of you for my pleasure!"
                                scene black with dissolve
                                bot"Today I finally get the chance to do just that!"
                                $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                "You hastily took off your pants!"
                                show 0footjob with dissolve
                                bot"Look at how my cock yearns for you, [hin_rel]!"
                                bot"But I won't fuck this up... I'll be smart about it!"
                                bot"And little by little, every part of you will be used to satisfy my desires..."
                                scene black with dissolve
                                bot"Starting with your sexy little feet!"
                                scene 01footjob with dissolve
                                "You carefully slid your cock with discreet movements in between [hin_name]'s feet..."
                                hin"A-ah..."
                                bot"S-shit!" with vpunch
                                hin"[bo_name_stutter]... K-keep g-going..."
                                bot"Heh... She must be thinking my cock rubbing in between her feet are my hands!"
                                bo"Don't mind if I do, [hin_rel]..."
                                scene 1footjob with dissolve
                                bo"Y-you just sit there and relax!"
                                bot"Holy fuck! I can't believe I am using [hin_rel]'s feet like this!"
                                bot"Her toes pressing against my cock feel... it feels so good! Now I just need to thrust my cock between her feet..."
                                bot"But what if she woke up... I'd be as good as dead!"
                                hin"A-ah... *Tired Moans*"
                                call increaselust(100) from _call_increaselust_73
                                bot"Fuck me! I can't take this anymore! Here goes nothing!"
                                "Click twice to thrust..."
                                call clicktwice from _call_clicktwice_7
                                show 4footjob with dissolve
                                "You thrust your cock in between [hin_name]'s feet while pressing them together to forcibly squeeze your shaft in between her toes..." with vpunch
                                bot"F-fuck... I need m-more!"
                                hin"..."
                                bot"You'll never know or feel a thing either way by the looks of it [hin_rel]..."
                                bot"Might as well take the chance and fuck your feet!"
                                scene hin_footjob1 with dissolve
                                bot"T-that's it, [hin_rel]!"
                                bot"You keep working your s-sexy feet around your [hin_rel_to_bo]'s cock..."
                                hin"... [bo_name_stutter]..."
                                bot"Fuck! She's still somewhat conscious..."
                                bot"But I can't stop now, [hin_rel]! I don't care if I die..."
                                bot"I just need to feel your touch, I just need to..."
                                hide hin_footjob1
                                show 4footjob
                                with dissolve
                                bot"I n-need to make y-you mine!" with vpunch
                                scene hin_footjob2 with dissolve
                                "As you near climax, you take another powerful thrust, and start frantically moving your pelvis faster and faster..."
                                hin"Y-you... S-slower... S-softer... P-please!"
                                bo"*Silent Moan*"
                                scene hin_footjob2 at custom_blur with dissolve
                                show gettingdizzy with dissolve
                                bot"A-ah... S-shut up, [hin_rel]! I am getting f-fucking dizzy..."
                                bot"I am a-about to..."
                                "Click twice to climax..."
                                show 2footjob_cum0 with flash
                                bo"[hin_rel_stutter]...!"
                                hin"...U-uh... *Soft Moans*"
                                $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                show 2footjob_cum1 with longerflash
                                hide gettingdizzy with dissolve
                                bo"F-fuck...!"
                                $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                show 2footjob_cum2 with flash
                                show 2footjob_cum2 with dissolve:
                                    zoom 1.4 xalign 1.0 yalign 0.0
                                "You shot a violent load that reached across [hin_name]'s body, covering parts of her face..."
                                $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                show 2footjob_cum3 with flash:
                                    zoom 1.2 yalign 0.4 xalign 1.0
                                
                                "And dripping down her breasts..."
                                scene 2footjob_cum3 with dissolve
                                call decreaselust(50) from _call_decreaselust_67
                                hin"U-uh...[bo_name_stutter]...?"
                                bot"S-shit...! B-but I am not done yet!"
                                scene black with vpunch
                                "You let go of her feet and laid back to avoid covering more of her body knowing that more was coming..."
                                $ renpy.sound.play("/audio/soun_fx/cum9.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                scene 01footjob_cumface zorder 100
                                show 01footjob_cum0
                                with flash
                                bo"A-ah! *Moans*"
                                $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                show 01footjob_cum2 with flash
                                call decreaselust(20) from _call_decreaselust_68
                                $ renpy.sound.play("/audio/soun_fx/cum2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                show 01footjob_projectile with flash
                                pause 0.5
                                hide 01footjob_projectile
                                show 01footjob_cum3
                                with dissolve
                                call decreaselust(20) from _call_decreaselust_69
                                "Instead, your massive load shot up into the air and covered [hin_name]'s feet..."
                                bot"...[hin_rel_stutter]!"
                                $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                show 01footjob_projectile with flash
                                pause 0.5
                                hide 01footjob_projectile
                                show 01footjob_cum4
                                with dissolve
                                call decreaselust(20) from _call_decreaselust_70
                                $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                bot"*Panting*"
                                bot"O-oh f-fuck! What an absolute relief..."
                                hin"U-uh... *Snorts*"
                                if quest_hin.exists("hin1H_2") and not _in_replay: #check if quest exists
                                    if quest_hin.is_state("hin1H_2", "pending"): #check quest state
                                        
                                        $ quest_hin.check("hin1H_2", "done") #update hinata shower quest to strikethrough if already completed
                                        $ quest_hin.check("hin1H_2", "done")
                                        $ notification (f"{hin_name} Hatred objective completed")
                                bot"But now [hin_rel]'s covered in my semen... W-what the fuck do I do?"
                                bot"I can't believe I've done this to her..."
                                bo"*Heavy breathing*"
                                "You take a few heavy breaths contemplating your actions..."
                                "Click twice to continue!"
                                call clicktwice from _call_clicktwice_8
                                bot"But fuck me, it felt good!"
                                call changeHatred(2) from _call_changeHatred_82
                                bot"...This is only the beginning!"
                                bot"I should try my best to clean up before she wakes up..."
                                scene black with dissolve
                                "You carefully clean up as much of the semen off [hin_name]'s feet and carefully lay her on the couch..."
                                scene bg lr hinanight massage with dissolve
                                show boruto bonersurprisedred with dissolve:
                                    xalign 0.3
                                bot"Time to get out of here!"
                                scene black with dissolve
                                $ renpy.end_replay()
                                $ pillsusedatleastonce = True
                                default hinatapillsedated = False
                                $ hinatapillsedated = True
                                jump action_taken






                            "W-what have I done...?":
                                default hinatapillsedatedregret = False
                                $ hinatapillsedatedregret = True
                                $ hinatapillsedated =True
                                bot"W-what the fuck have I done! Did I really just sedate [hin_rel]?"
                                bot"Is this who I am now?"
                                scene bg lr hinanight massage with dissolve
                                show boruto surprised2 at left with dissolve
                                bot"I can't be doing this..."
                                call changeHatred(-5) from _call_changeHatred_83
                                bot"Not to [hin_rel]! This is not who I am!"
                                hide boruto with dissolve
                                bot"I won't let myself descend into madness..."
                                "You leave [hin_name] untouched in her sedated state and go off to reflect upon your actions..."
                                scene black with dissolve
                                $ renpy.end_replay()
                                jump action_taken

                            




                        
                        jump action_taken
                        
                    







            call changeObedience("Hinata", 1, "v1_night_massage_talk", 2) from _call_changeObedience_29
            show hina nightmassage_feet1 with dissolve
            hin"H-huh? Relieve stress how...?"
            show hina nightmassage_feet2 with dissolve
            "You let your mind stray for a bit..."
            bo"W-well, uuuh..."
            show hina nightmassage_feet2 with dissolve:
                easein 3 zoom 1.1 xalign 1.0 yalign 1.0
            bo"I am pretty good at massages you know..."
            bo"I could help you relax while you are lying on the sofa..."
            bo"I am sure your feet are all cramped up and tired from all the chores you do every day..."
            show hina nightmassage3 with dissolve:
                zoom 1.25 xalign 0.5 yalign 1.0
            show hina nightmassage3:
                easein 5 yalign 0.0
            hin"Ooooh? Since when is my [hin_rel_to_bo] a massage expert..."
            menu stressreliefmenu:
                hin"Ooooh? Since when is my [hin_rel_to_bo] a massage expert..."
                "Come up with an elaborate lie" (greyed_out = True,threshold_value_grey=1, int_value_grey=stressreliefmenu_lie):
                    default stressreliefmenu_lie = 0
                    $ stressreliefmenu_lie += 1
                    bo"I am serious! I even had somewhat of a reputation for being THE massage guy back in school..."
                    hin"Did you now..."
                    bo"Yep! Everyone would come up to me and ask for one of my renowned shoulder massages after our Taijutsu classes."
                    bo"Just a few minutes of me doing my thing and they'd leave with rejuvenated muscles!"
                    hin"Huh... I might have to take you up on your offer at some point then!"
                "{color=[dominancecolor]}I've got pretty strong hands you know...{/color}"(greyed_out = True,threshold_value_grey=1, int_value_grey=stressreliefmenu_hands):
                    default stressreliefmenu_hands = 0
                    $ stressreliefmenu_hands += 1
                    bo"I've got pretty strong hands you know..."
                    bo"I did master the Rasengan in only a few days, didn't I? It took [na_rel] months!"
                    bo"Not to mention the reputation I have for my Taijutsu proficiency..."
                    call changeDominance(1,"stressreliefmenu", 1) from _call_changeDominance_9
                    hin"...Do you now? *Giggles*"
                    hin"Maybe we'll have to put that to the test then sometime soon..."
                "{color=[obediencecolor]}Have you considered my offer?{/color}" if stressreliefmenu_hands >= 1 and stressreliefmenu_lie >= 1:
                    #add shop items
                    if lr_massagecounter != 100:
                        $ massagebooklvl1 = Item(name="Massage Tips Volume 1", info="An informative guide on massage techniques", price=75, quantity=1)
                        $ inventoryShop.add_item(massagebooklvl1, 1)
                        $ inventoryShop.update_item(f"Pills", info=f"A bottle of prescription pills. Thought to be a strong sedative", price=50)
                    $ lr_massagecounter = 100

                    bo"I can show you if you'd like! Have you considered my offer?"
                    hin"Hmm..."
                    show hina:
                        easein 2 yalign 1.0
                    hin"If it's just my feet, I don't see why not..."
                    hin"Lord knows I could use it!"
                    bo"You'll be asking for more after I show you my technique!"
                    show hina nightmassage1 with dissolve
                    show hina nightmassage1:
                        easein 2 yalign 0.3
                    hin"*Giggles* Come on then, show me that renowned technique of yours..."
                    bo"Was that sarcastic, [hin_rel]...?"
                    show hina nightmassage1:
                        easein 2 yalign 1.0
                    bo"Alright then, if my words won't convince you, then I'll let my hands speak for me."
                    show hina nightmassage_feet1 with dissolve:
                        xalign 1.0
                    bo"Put your feet up for me, will you?"
                    hin"Like..."
                    show fm_start_1 with dissolve
                    hin"...this?"
                    bo"Just like that, you see..."
                    bo"There's a very particular spot where tension tends to build up when you are standing all day taking care of house chores..."
                    bo"If you apply some pressure to that spot, then..."
                    show fm_start
                    show fm_start_face1
                    with dissolve
                    hin"A-ah!..."
                    hin"It hurts, a little bit..."
                    hide fm_start_face1 with dissolve
                    hin"but it also felt good!"
                    bo"Right? There's two improtant zones that are prone to built-up tension. The arch of the foot, the spot I am pressing right now is one of them, the other one is..."
                    scene fm_start_1
                    show fm_start_face2
                    with dissolve
                    hin"Owie!"
                    scene fm_start_1 with dissolve
                    bo"The ball of the foot... It might hurt a little bit at first, but after a few rounds of pressure point repetitions, you'll feel so relieved, that you'll quickly forget about the minor pain..."
                    show fm_start with dissolve
                    bo"Shall I keep going?"
                    show fm_start_face1 with dissolve
                    show hin_footmassageanim1 with dissolve
                    hin"A-ah! Y-yes please... I am already feeling some relief. You really k-know your stuff, don't you?"
                    bo"I told you, haven't I?"
                    bo"I used to study this stuff. Back when I used to train as hard as I did to surpass dad, I would get cramped up all the time..."
                    bo"So I taught myself some techniques to help..."
                    hin"Hmmm... I can see that, but..."
                    hin"Don't you find doing this to others a bit weird, especially when you have to touch their feet?"
                    bo"...Weird? In what way?"
                    hin"Y-you know, people's feet are generally gross... But I guess that's just me and my mild case of germophobia! *Awkward Giggle*"
                    bo"I get what you are saying, but..."
                    menu:
                        bot"I am not much of a feet person myself, but after that day..."
                        "I am aroused by [hin_rel]'s feet...":
                            bo"I don't think feet are gross. Yours are sort of pretty even..."
                            hin"P-pretty!?"
                            call increaselust(10) from _call_increaselust_74
                            bot"Sexy even! But you'd surely not appreciate me saying that..."
                        "I don't mind them as much":
                            bo"Me personally, I don't mind them as much..."
                            hin"Hmm..."
                    bo"Besides, you take like ten showers per day and have pedicures every week or so!"
                    bo"There's no way I'd be grossed out by any part of you, [hin_rel]..."
                    hin"I s-suppose you are right..."
                    scene fm_start_1 with dissolve
                    bo"That should do it for your feet. Feeling better?"
                    hin"It truly does feel like it helped. Thanks for that!"
                    scene hina nightmassage3 with dissolve:
                        zoom 1.25 xalign 0.5 yalign 1.0
                    show hina nightmassage3:
                        easein 2 yalign 0.0
                    call changeLove("Hinata",1) from _call_changeLove_34
                    hin"I might have to take you up on your services some time soon again! *Giggles*"
                    bo"I could help with more than just your feet you know..."
                    hin"I am not sure about that... We'll see, Okay?"
                    scene black with dissolve
                    bot"Not too bad! I might be able to convince her to let me take care of her if I play my cards right!"
                    jump action_taken



                       
            hin"I'll have to think about it, okay?"
            scene black with dissolve
            bo"Sure thing!"
            bot"Not too bad! I might get a shot at this..."
            jump action_taken
        "(Locked)" if lr_massagecounter < 1:
            dev"Complete previous option first."
            jump lr_massage_menu

        "Is everything alright...?" (advancement_event=True) if day_number>=14 and (chosen_hate_path or chosen_love_path) and unlocklvl2hatredevent == True:
            if chosen_hate_path and hatred.level == 1:
                call randomCheck(False,"You do not meet the requirements for this event yet.") from _call_randomCheck_17
                "Advance to Hatred Level 2 first to unlock this option in the Hate Path."
                jump lr_massage_menu
            jump v21_hinatadate_quest_start



        "???" (advancement_event=True) if unlocklvl2hatredevent and chosen_hate_path == False and chosen_love_path == False:
            call randomCheck(False,"You do not meet the requirements for this event yet.") from _call_randomCheck_18
            if day_number>=14 and (chosen_hate_path == False and chosen_love_path == False):
                "Unlock this option by choosing to embrace a path of love after visiting Kushina in your dreams."
            elif day_number<14:
                "Advance the story beyond Day 14 to unlock."
            jump lr_massage_menu

        "Have another dinner date together (Replay)" if v21_hinatadate_progression >= 1 and chosen_love_path:
            $ wine_in_inventory = inventory.find_item_by_name("Wine")
            # if v21_hinatadate_daycounter >= 3 and wine_in_inventory!= None:
            if hinata_love.level >= 2:
                scene black with dissolve
                jump v21_hinatalovelevel2_date
                
            elif wine_in_inventory != None and v21_hinatadate_daycounter < 3:
                bot "I should wait a few days and get more wine before I try to spend some quality time with [hin_rel] again..."
                jump lr_massage_menu
            elif wine_in_inventory == None:
                bot "I should get more wine first if I want to spend some quality time with [hin_rel] again..."
                jump lr_massage_menu
            else:
                bot "I should wait a few days before I try to spend some more time with [hin_rel] again..."
                jump lr_massage_menu





screen v1_night_massage_screen:
    imagebutton:
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"
        idle "bg lr hinanight massage"  #image in ui / needs to be seperate for correct images to be displayed when hovering
        hover "bg lr hinanight massagehover"
        focus_mask "bg lr hinanight massagehover mask"
        mouse "handsmall"
        hovered [Show("displayTextScreen", displayText = "Interact with [hin_name]")]
        unhovered [Hide("displayTextScreen")]
        action [Hide("displayTextScreen"), Jump("livingroomtalkmenu")]