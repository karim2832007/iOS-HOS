label livingroom_morning:
    call resetbuttons from _call_resetbuttons_18
    call hideUI from _call_hideUI_33
    if hin_location == "livingroom" and him_location == "livingroom":
        scene bg lr_day with dissolve:
            zoom 0.67
        call enabletalk from _call_enabletalk_46
    elif hin_location == "livingroom":
        if day_number == 1 and ch1_d1_moneyproblems_completion == False:
            scene bg lr_day with dissolve:
                zoom 0.67
            call ch1_d1_moneyproblems_mainstory from _call_ch1_d1_moneyproblems_mainstory
        scene bg lr_day with dissolve:
            zoom 0.67
        call enabletalk from _call_enabletalk_47
    elif him_location == "livingroom":
        scene bg lr_day with dissolve:
            zoom 0.67
        call enabletalk from _call_enabletalk_48

    elif day_number == 1 and ch1_d1_moneyproblems_completion == True and journalintro == False:
            $ journalintro = True
            scene bg lr_day with dissolve:
                zoom 0.67
            jump journaltutorial #freeroam start
    else:
        scene bg lr_day with dissolve:
            zoom 0.67

    call showUIhouse from _call_showUIhouse_60
    $ ui.interact()

label livingroom_evening:
    call hideUI from _call_hideUI_34
    call resetbuttons from _call_resetbuttons_19
    if hin_location == "livingroom" and him_location == "livingroom":
        scene bg lr_day with dissolve:
            zoom 0.67
        call enabletalk from _call_enabletalk_49


    elif hin_location == "livingroom":
        scene bg lr_day with dissolve:
            zoom 0.67
        call enabletalk from _call_enabletalk_50


    elif him_location == "livingroom":
        default himaintrotutorial = False #bump
        default himaintrotutorial2 = False #clothing shop
        if himaintrotutorial == False:
            $ himaintrotutorial = True
            jump v1_secret_himawarisecretscene #V1 Hima secretscene
            # ----------------------------------------------------------------------
            # ----------------------------------------------------------------------
        elif himaintrotutorial2 == False:
            scene bg lr_day:
                zoom 0.67
            show himaschoolt smug at right:
                zoom 0.55
            with dissolve
            him"Sup, loser..."
            jump lr_visitshop
            call showUIhouse from _call_showUIhouse_61
            $ ui.interact()
        else:
            scene bg lr_day:
                zoom 0.67
            show himaschoolt normal at right:
                zoom 0.55
            with dissolve
            call showUIhouse from _call_showUIhouse_68
            call enabletalk from _call_enabletalk_55
            $ ui.interact()
              
            
        scene bg lr_day with dissolve:
            zoom 0.67
        call enabletalk from _call_enabletalk_51


        
    else:
        scene bg lr_day with dissolve:
            zoom 0.67

    call showUIhouse from _call_showUIhouse_62
    $ ui.interact()

label livingroom_night:
    call hideUI from _call_hideUI_35
    call resetbuttons from _call_resetbuttons_20
    if hin_location == "livingroom" and him_location == "livingroom":

        
        scene bg lr night with dissolve:
            zoom 0.67
        call enabletalk from _call_enabletalk_52
    elif hin_location == "livingroom":

        if hin_location == "livingroom": #change if clause if needed in future / massage scene
            jump v1_night_massage

        scene bg lr night with dissolve:
            zoom 0.67
        call enabletalk from _call_enabletalk_53
    elif him_location == "livingroom":
        scene bg lr night with dissolve:
            zoom 0.67
        call enabletalk from _call_enabletalk_54
        
    else:
        scene bg lr night with dissolve:
            zoom 0.67

    call showUIhouse from _call_showUIhouse_63
    $ ui.interact()

label livingroomtalkmenu:
    call hideUI from _call_hideUI_36
    menu:
        "..."
        "Talk to [hin_name]" if hin_location == "livingroom":
            if current_event == "v1_night_massage": # hinata massage event
                jump v1_night_massage_talk
            call showUIhouse from _call_showUIhouse_64
            $ ui.interact()
        "Talk to [him_name]" if him_location == "livingroom":
            menu:
                bo"..."
                "About the modeling thing...":
                    dev"Coming very soon!"
                "Return":
                    pass
                
            call showUIhouse from _call_showUIhouse_65
            $ ui.interact()
        "Return":
            call showUIhouse from _call_showUIhouse_66
            $ ui.interact()
































label lr_visitshop:

    menu:
        him"Sup, loser..."
        "...Are you doing anything?" if bohim_2_started == False:
            show boruto snob at left with dissolve
            bo"Are you doing anything or just standing there looking ugly?"
            him"Oh I am certainly doing stuff! Just not with you, loser!"
            hide himaschoolt with dissolve
            him"Teehee!"
            show boruto surprised2 with dissolve
            bot"I'll never get anywhere with her like this..."
            "Complete 'Obo's Story 1' (4200 score) in the ramen shop to approach [him_name]..."
            $ him_location = "none"
        "{color=[obediencecolor]}Talk to her about your [hin_rel_mother]{/color}" if bohim_2_started == True:
            bot"Regardless of how I feel about [him_name], I'll have to be careful about how I approach her from now on if I want to convince her to work with me..."
            show boruto surprised2 at left with dissolve
            bo"[him_name], do you have a minute?"
            him"A minute is all you get! I won't waste more time on the likes of you..."
            show boruto worried with dissolve
            bo"*Sigh*..."
            bo"This is serious [him_name]. It concerns [hin_rel]..."
            show himaschoolt normal with dissolve
            him"[hin_rel_stutter]?" with vpunch
            him"What's wrong with her!?" with vpunch
            bo"I'll tell you all about it, but perhaps it's best we do that elsewhere..."
            bo"I know for a fact she would stress out if she picks up our conversation..."
            show himaschoolt angry with dissolve
            him"Now you are stressing ME out, [bo_name]!" with vpunch
            show boruto laughing2 with dissolve
            bo"I know, I know. Look, It's nothing we can't work ourselves out of. I promise it'll be fine, but I need you to work with me on this one, okay?"
            show boruto normal with dissolve
            bo"Besides, I have a surprise for you! Come on, let's take a walk!"
            hide boruto with dissolve
            show himaschoolt at smallshake
            him"Mmmh!"
            him"...Fine!"
            hide himaschoolt with dissolve
            him"Only because this concerns [hin_rel]!"
            $ renpy.sound.play("/audio/soun_fx/dooropen.opus", channel="sfx3", loop=False, relative_volume = 0.6)
            label replay_visitclothingstore:
            $ initialize_replay_defaults()
            scene black with dissolve
            "[him_name] reluctantly follows you outside..."
            $ playmusic("audio/ost/market.opus",0.6)
            scene bg konoha2 with dissolve
            show himaschoolt normal at right with dissolve:
                zoom 0.55
            him"So...? Where are we going? And what's wrong with [hin_rel]!"
            show boruto normal at left with dissolve
            bo"Where we are going is a surprise..."
            bo"It might even take as a while, but I promise I'll make it worth your while..."
            scene black with dissolve
            bo"Come on, Let's walk!"

            show hima_storewalk1 with dissolve
            $ renpy.sound.play("/audio/soun_fx/walkingforest.opus", channel="sfx3", loop=False, relative_volume = 0.2)
            bo"As for [hin_rel]..."
            bo"I happened to have overheard an important conversation of hers..."
            show hima_storewalk3 with dissolve
            bot"The wind is lifting her s-skirt up..."
            him"...What kind of conversation?" with vpunch
            bot"Makes for a nice view anyway..."
            him"And how did you overhear it!" with vpunch
            scene hima_walkstore_an with dissolve
            bo"Relax... I wasn't peeping or anything..."
            bo"It was one morning when you were away at school..."
            $ renpy.sound.play("/audio/soun_fx/walkingforest.opus", channel="sfx1", loop=False, relative_volume = 0.4)
            bo"I woke up to some commotion happening at our front door, so I went to see what was going on..."
            bo"[hin_rel] was right there with two menacing looking men threatening her about some sort of debt obligations that were left unpaid..."
            him"D-debt...? Is that serious? What kind of threats!" with vpunch
            bo"I don't know exactly but... Those men worked under the Daimyo. They even said [hin_rel] would have to find other ways to pay if she can't come up with the money..."
            bo"All I know is that they looked and sounded very threatening."
            him"The D-daimyo!? T-then, what are we going to do! This is serious [bo_name]..." with vpunch
            bo"I know, I have a plan..."
            bo"And I might need your help with it."
            him"You... A plan?"
            him"I am not sure I am convinced!" with vpunch
            bo"Just hear me out... Okay?"
            him"Hmph!" with vpunch
            bo"You know [hin_rel] will never ask anything from us. She's too humble for that, but we also know that she is a bit clumsy with money and would be hard pressed to hold a demanding job as things stand..."
            bo"Not to mention that [na_rel] is away for a while now... We don't even know when he'll return."
            bo"And so, these past few days I've been secretly working my ass off at a local restaurant..."
            bo"I am making decent money. Maybe even enough to cover some of [hin_rel]'s debts..."
            him"R-really? You can do that!?"
            bo"Well, I am t-trying but... The reality is that we are probably going to need much more than what I am currently making right now..."
            himt"I had no idea he was so thoughtful..."
            $ renpy.sound.play("/audio/soun_fx/walkingforest.opus", channel="sfx1", loop=False, relative_volume = 0.4)
            bo"Which is where you could come in..."
            him"M-me? But you know I can't work. School and studies take up all of my time. I c-can't just drop out, can I?"
            him"Unless [hin_rel] really needs me to... T-then I'd do even that!"
            bo"You don't have to worry about that... I think."
            bo"There's other ways you can help. Methods that would require very little of your time, and would make us enough money to cover [hin_rel]'s debts!"
            him"Really? How!" with vpunch
            bo"Let's not get ahead of ourselves..."
            bo"It will all depend on you. Where we are going is actually quite relevant in that regard..."
            him"Well.. I appreciate your willigness to help [hin_rel], and I want to help too, but..."
            him"I hope you are being genuine!" with vpunch
            him"I am not sure if I appreciate all this secrecy! I hope you aren't thinking of anything stupid!"
            bo"I told you, it's a surprise!"
            bo"I haven't forgotten that your birthday is due in a few days you know..."
            scene black with dissolve
            him"M-my birthday? Since when do you care about that!" with vpunch
            him"Now I am even more intrigued!"
            bo"Come on, let's go inside!"
            $ renpy.sound.play("/audio/soun_fx/shopbell.opus", channel="sfx1", loop=False, relative_volume = 1.0)
            $ playmusic("/audio/ost/house1.opus", volume=0.7)
            show bg clothingstore with dissolve
            show clothing shopkeep at center with dissolve:
                zoom 0.73
            "Elegant shop clerk" "Welcome to our establishment, monsieur! How can I be of assistance..."
            himt"*Gasps* So pretty... And well dressed. Is this a... clothing shop?"
            himt"But, what are we doing here... We can't even afford any of this stuff..."
            bot"Here goes nothing..."
            "You handed over Obo's referal card hoping this isn't some stupid prank of his..."
            "[him_name] stood right behind you still confused by the entire ordeal..."
            "But you could sense a sense of excitement form her jittery demeanor..."
            bot"Worst case, I'll just have to gift [him_name] something to make this worth my while..."
            "Elegant shop clerk" "Referred by monsieur Obo himself I see."
            "Elegant shop clerk" "You must be an important person in the fashion industry, monsieur!"
            scene black with dissolve
            "Elegant shop clerk" "Please, follow me!"
            himt"Important p-person?" with vpunch
            himt"IN THE F-FASHION INDUSTRY?" with vpunch

            show bg clothingstore with dissolve
            show clothing shopkeep at right with dissolve:
                zoom 0.73
            show boruto snob with dissolve:
                xalign 0.3
            show himaschoolt normal behind boruto with dissolve:
                zoom 0.55 xalign -0.2 ypos 23
            himt"Is this some elaborate prank?" with vpunch
            "Elegant shop clerk" "Monsieur [bo_name], was it?"
            "Elegant shop clerk" "This entire floor is yours to do with as you see fit!"
            bot"This is going even better than I expected!"
            "Elegant shop clerk" "You and your consort can freely try any of the items on display. Any purchase made will of course be heavily discounted."
            him"C...Consort!?" with vpunch
            show himaschoolt angry with dissolve
            him"I am h-his [him_rel]!"
            "Elegant shop clerk" "Forgive me, Mademoiselle!"
            show himaschoolt normal with dissolve
            "Elegant shop clerk" "Consort or [him_rel], matters not. Monsieur [bo_name] has made an excellent selection for his modelling subject regardless!"
            "Elegant shop clerk" "I shall leave you in private now. Please enjoy your stay, courtesy of the house itself!"
            him"M-modelling subject!?" with vpunch
            hide clothing with dissolve
            show boruto surprised2 with dissolve
            bo"Uuuh..."
            scene black with vpunch
            him"Nevermind all that! I have no time to waste!"
            "As soon as the clerk left the floor, [him_name] started running up and down the floor in excitement..."
            show hima_clothestore 0 with dissolve
            him"All these clothes... I can try them all on?"
            him"I can't believe this! All my favourite brands, all these super expensive clothes!"
            scene black
            him"YAA-HOO!" with vpunch
            scene hima_clothestore 2 with dissolve
            him"Awww, so cute! I am going to cry from excitement!"
            him"I'll try this... and this... and this..."
            him"And this, and this, and this, and this, and this, and this!" with vpunch
            bot"Heh... We were always stranded for money so [him_name] and [hin_rel] could never afford much clothing to begin with..."
            scene black with vpunch
            "[him_name] stops herself from getting overly excited and drops a bunch of the clothing she was planning to try on..."
            scene bg clothingstore with dissolve

            show boruto snob with dissolve:
                xalign 0.2
            show himaschoolt normal at right:
                zoom 0.55
            him"[bo_name]... What's going on?"
            him"What was that about being an important person in the f-fashion industry!?" with vpunch
            him"And why are we getting this special treatment..."
            him"Why did you never tell anyone about this!"
            menu:
                him"Why did you never tell anyone about this!"
                "{color=[lovecolor]}I told you, I wanted it to be a surprise!{/color}":
                    bot"The stars aligned, really... But might as well use the opportunity!"
                    bo"I told you didn't I?"
                    bo"I wanted it to be a surprise for my lovely [him_rel]!"
                    show himaschoolt:
                        easein 1 xalign 0.5
                    him"All this time I thought you..."
                    show himaschoolt:
                        easein 2 xpos -1000
                    call changeLove("Himawari", 1) from _call_changeLove_35
                    show boruto surprised2 with dissolve
                    him"Nevermind! But t-thank you for this!"

                "{color=[obediencecolor]}Don't get too excited now...{/color}":
                    bo"We all have secrets, [him_name]..."
                    bo"Don't get too excited now, I will only buy you a single item for your birthday..."
                    bo"And that's if I approve of how it looks first!"
                    him"Hmmm...."
                    show himaschoolt:
                        easein 2 xpos -1000
                    him"You won't find me saying no to that!"
                    call changeObedience("Himawari", 1) from _call_changeObedience_65
                    show boruto surprised2 with dissolve
                "{color=[dominancecolor]}I am a man of many talents!{/color}":
                    bo"I am a man of many talents, [him_name]..."
                    him"Is that right..."
                    call changeDominance(1) from _call_changeDominance_40
                    bo"I want you and [hin_rel] to be able to rely on me..."
                    bo"So go ahead, pick something you like!"
                    bo"I'll buy it for your birthday..."
                    himt"This all feels a bit off, but..."
                    show himaschoolt:
                        easein 2 xpos -1000
                    him"You won't find me saying no to that!"
                    show boruto surprised2 with dissolve

                
            "[him_name] ran straight past you and got back to browsing clothes..."
            bo"Remember, you only get to choose one item for your birthday!"
            show hima_clothestore 2 with dissolve
            him"My favourite sporting brand!" with vpunch
            himt"I NEED to try this on, I really need a new set of clothes for my workouts!"
            scene black with dissolve
            him"[bo_name]! I am trying some sports clothing on, wait for me outside!"
            scene bg fitting room with dissolve
            bo"I'll be right here..."
            bo"Don't take years please! I have to get back to work!"
            bot"."
            bot".."
            bot"That mannequin, it's kinda spooky with how lifelike it looks..."
            bot"The dress on display sure is sexy though..."
            bot"I wonder if [him_name] would be willing to try that out for me..."
            bot"Unlikely of course, but maybe I could convince her!"
            bot"..."
            menu:
                bot"..."
                "Check what's going on...":
                    show bg fitting room2 with dissolve
                    him"I am not d-done yet! I can hear you walking around..."
                    bo"Just checking out the place..."
                    bot"I imagine taking off ten layers of clothing would take anyone a while..."
                    menu:
                        bot"I imagine taking off ten layers of clothing would take anyone a while..."
                        "Take a peek!":
                            bot"I have to entertain myself somehow..."
                            scene black with dissolve
                            "You sneakily approached the changing room..."
                            show screen parallax1280peek("himclothe_peek","bg horizontal") with dissolve
                            "You peek through a very small opening in the curtains..."
                            bot"D-damn... I can barely see anything, but even so..."
                            him"Hmm... It's cute, but..."
                            him"It might be too short down there...."
                            him"Although the sports bra would certainly help with holding my boobs in place now that they've grown a bit..."
                            him"That tank top I wear was quite problematic in that area."
                            him"I wonder if [hin_rel] would approve of me wearing this..."
                            him"Not to mention that loser [him_rel_to_bo_default] of mine..."
                            him"He might be trying a little bit more lately, but I am still not sure about him..."
                            him"What if he acts all p-pervy..."
                            bot"Me? Pervy? I would never!"
                            bot"But fuck me! [him_name] really has something to her. She's certainly an annoying little bitch still, but a sexy one nonetheless!"
                            him"I guess I'll have to show him this before he buys it for me..."
                            bot"Hell yeah!" with vpunch
                            him"A chance to see if he reacts properly!"
                            bot"Oh shit! Time to get out of here!"
                            call hidescrollingimage from _call_hidescrollingimage
                            hide screen parallax1280peek with dissolve
                            show bg fitting room2 with dissolve
                            him"[bo_name]?"
                            bo"*Cough* *Cough* Uhm... Yes?"
                            him"I think I need a second opinion..."
                            bo"Feel free to step outside..."
                            bot"Hehe... Time to take a better look at you!"
                            jump tryburuma
                            
                        "Just wait...":
                            bo"."
                            bo".."
                            bo"..."
                            bo"This is why marriages don't last!"
                            show bg fitting room2 with dissolve:
                                zoom 1.3 xalign 0.5 yalign 0.1
                            him"Uuumm...."
                            him"[bo_name]?"
                            bo"Yes?"
                            him"I think I need a second opinion..."
                            bo"Feel free to step outside..."
                            jump tryburuma

                "Just wait...":
                    bo"."
                    bo".."
                    bo"..."
                    bot"I hate this part of shopping with women..."
                    him"Uuumm...."
                    him"[bo_name]?"
                    bo"Yes?"
                    him"I think I need a second opinion..."
                    bo"Coming in then!"
                    jump tryburuma
                
            



             




            scene bg clothingstore with dissolve
    call showUIhouse from _call_showUIhouse_69
    $ ui.interact()


label tryburuma:
    him"O-okay..."
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/curtainopening.opus", channel="sfx1", loop=False, relative_volume = 0.6)
    "[him_name] pushes the curtain aside..."
    show screen parallax1280("opinion1_him") with flash
    call showscrollingimage from _call_showscrollingimage
    show bg fitting room3
    bot"D-damn..."
    bot"The buruma part is even shorter than I though it would be..."
    bot"And her small breasts are filling the sports bra nicely..."
    show opinion1_himt:
        zoom 0.7 xalign 0.5
    him"...S-so? What do you think?"
    call hidescrollingimage from _call_hidescrollingimage_1
    menu tryburuma_menu:
        him"...S-so? What do you think?"
        "Suits you!":
            bo"I think it suits you!"
            show opinion1_himt at smallshake
            him"R-really?"
            him"I don't know..."
        "...M-meh":
            bo"M-meh... It's alright, I suppose..."
            call changeRespect("Himawari",-1) from _call_changeRespect_108
            him"C-come on! Give me something more than 'Meh'..."
        "{color=[hatredcolor]}Could be a little bit more revealing...{/color}":
            call checkHatred(20, "tryburuma_menu") from _call_checkHatred_6
            bo"Could use some shortening around the chest and bum area..."
            call changeObedience("Himawari", 1) from _call_changeObedience_66
            him"W-what!?-"
            bo"Just to accentuate your atheltic body a little bit better, nothing extreme..."
            him"A-are you serious?"
            him"I was thinking the exact opposite!"
            call changeHatred(1) from _call_changeHatred_84
            bot"Yeah no shit bitch! I just want to stare at your slutty little body..."
        "{color=[dominancecolor]}I think it was made for you!{/color}":
            call checkDominance(10,"tryburuma_menu") from _call_checkDominance_4
            bo"I think it was literally made for you. It emphasizes your athletic body in all the right places!"
            him"Y-you really think so?"
            call changeDominance(1) from _call_changeDominance_41
            bo"For sure. Don't you see it too?"
            him"Hmm..."
    show opinion1_himt at smallshake 
    him"Me personally I was thinking that it m-might be too revealing. Especially on the lower part..."
    bo"Can't say for certain without seeing you in a few different profiles..."
    him"P-profiles? Is that some fashion terminology I am unfamiliar with?"
    bot"Time to make up some bullshit!"
    bo"You've heard the clerk. I am a bit of a fashion expert. I can only make conclusive calls when I observe my subject in different poses."
    bo"Nothing serious, just pretend you are about to start a workout and strike a few poses..."
    him"E-easy enough. Something like..."
    hide opinion1_himt
    show opinion2_himt:
        zoom 0.7 xalign 0.5
    with dissolve
    him"...This?"
    bo"Sort of..."
    bo"But you have to exude confidence for a clothing item to really shine through..."
    him"I don't know if I can do that... This might not be the one for me..."
    him"I love the brand, and I think it's cute. All the best athletes wear this same set too, but..."
    menu:
        him"I love the brand, and I think it's cute. All the best athletes wear this same set too, but..."
        "{color=[dominancecolor]}Offer a 'comforting' touch...{/color}":
            bo"[him_name], stop it!" with vpunch
            him"W-what do you mean..."
            show opinion2_himt 2 with dissolve
            call changeDominance(1) from _call_changeDominance_42
            "You placed your arm on her shoulder..."
            bo"Those very athletes you look up to..."
            $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
            show hima_walkstore_grab1:
                zoom 0.7 xalign 0.5
            hide opinion2_himt
            with dissolve
            show hima_walkstore_grab1 at smallshake
            "And you started rubbing her hand in a comforting manner..."
            "[him_name] was surprised by your touch, but chose to put up with it given the circumstances..."
            bo"There's nothing seperating you from them, you know..."
            bo"I've seen the effort you put into your training."
            bo"Even one look at you is enough to understand the commitmnet that goes into what you do..."
            bo"So I say, why not show the fruit of your labors?"
            bo"Why shy away of what you've worked so hard to achieve..."
            him"I k-know... You are not w-wrong. But still..."
            menu:
                him"I k-know... You are not w-wrong. But still..."
                "{color=[dominancecolor]}Keep going further...{/color}":
                    bo"I for one..."
                    hide hima_walkstore_grab1
                    show opinion2_himt 3:
                        zoom 0.7 xalign 0.5
                    with dissolve
                    call checkDominance(13,"opinion2_himt_fail") from _call_checkDominance_5
                    show opinion2_himt 3 at smallshake
                    "You moved your hand down to her stomach..."
                    hide opinion2_himt
                    show hima_walkstore_grab2:
                        zoom 0.7 xalign 0.5
                    with dissolve
                    $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                    "And repeatedly, but gently patted her abdominal area..."
                    bo"I think you've sculpted your body to perfection..."
                    bo"You should be proud of it. Your abs alone are strong enough to crack rocks with..."
                    him"Okay, okay! I t-think you are right but..."
                    call changeObedience("Himawari", 2) from _call_changeObedience_67
                    him"Is the touching necessary?"
                    call changeDominance(1) from _call_changeDominance_60
                    bo"Not really! Just admiring your hard work..."
                    hide hima_walkstore_grab2
                    show opinion2_himt 2:
                        zoom 0.7 xalign 0.5
                    with dissolve
                    him"I think you might be right. Maybe I was overthinking it..."
                    jump endburuma
                    label opinion2_himt_fail:
                        "You moved your hand down to her stomach, but..."
                        bo"Think you are doing a great job! Your abs are lookin-"
                        show opinion1_himt with dissolve
                        show opinion1_himt at smallshake
                        call changeRespect("Himawari", 2) from _call_changeRespect_109
                        him"Okay! I get your point, so enough with the touching!" with vpunch
                        bot"Shit! Did I say some stupid shit?"
                        jump endburuma
                "So own it!":
                    bo"Own it, [him_name]! Since when were you one to act like this anyway..."
                    hide hima_walkstore_grab1
                    hide opinion2_himt
                    show opinion1_himt:
                        zoom 0.7 xalign 0.5
                    with dissolve
                    him"Hmph! I think you are right. But you see..."
                

        "{color=[obediencecolor]}Re-assure her...{/color}":
            bo"No buts!"
            bo"I assure you this is nothing out of the ordinary..."
            bo"You said it yourself! All the best athletes at the Shinobi olympics wear burumas just like this one..."
            bo"Are you not an athlete too...?"
            hide opinion1_himt
            show opinion2_himt beh
            with dissolve
            him"I a-am!" with vpunch
            bo"Indeed you are! A pretty one too. So stop second guessing yourself and start enjoying the fruits of your labour!"
            call changeObedience("Himawari", 1) from _call_changeObedience_68
            him"Mmmmph...! *Annoyed hum*" with vpunch
            show opinion1_himt:
                zoom 0.7 xalign 0.5
            hide opinion2_himt
            with dissolve
            him"Okay! But you see..."
        
        "{color=[hatredcolor]}Re-assure her...{/color}":
            bo"No buts!"
            bot"Besides the one butt I'd make an exception for!"
            call changeHatred(1) from _call_changeHatred_98
            bot"YOURS!" with vpunch
            bot"I better convince her that it's normal wearing these slutty sportswear so I can enjoy her parading around like a whore at home!"
            
            bo"I assure you this is nothing out of the ordinary..."
            bo"You said it yourself! All the best athletes at the Shinobi olympics wear burumas just like this one..."
            bo"Are you not an athlete too...?"
            hide opinion1_himt
            show opinion2_himt beh
            with dissolve
            him"I a-am!" with vpunch
            bo"Indeed you are! A pretty one too. So stop second guessing yourself and start enjoying the fruits of your labour!"
            call changeObedience("Himawari", 1) from _call_changeObedience_76
            him"Mmmmph...! *Annoyed hum*" with vpunch
            show opinion1_himt:
                zoom 0.7 xalign 0.5
            hide opinion2_himt
            with dissolve
            him"Okay! But you see..."
        

label endburuma:
    hide hima_walkstore_grab2
    hide opinion2_himt
    show opinion1_himt ass1:
        zoom 0.7 xalign 0.5
    with dissolve
    him"M-my main concern is this..."
    bot"...!" with vpunch
    bo"N-nothing wrong with that. Looks nice even!"
    show opinion1_himt ass1 at smallshake
    him"That's not the problem!"
    him"What if I have to do an exercise that would have me..."
    show opinion1_himt ass2 with dissolve
    him"...Leaning down. It feels like the bloomers will slip off and r-reveal things they shouldn't!"
    show opinion1_himt ass3 with dissolve
    him"Am I just paranoid?"
    menu:
        him"Am I just paranoid?"
        "{color=[obediencecolor]}You kinda are...{/color}":
            bo"You kinda are paranoid..."
            bo"Burumas are made specifically to enhance athletic performance."
            bo"That's why they are skin tight and grasp your skin as tight as they do..."
            bo"Why do you think track and field athletes use them when running?"
            call changeObedience("Himawari", 1) from _call_changeObedience_69
            show opinion1_himt ass2 with dissolve
            show opinion1_himt ass2 at smallshake
            him"Now that you mention it..."
            show opinion1_himt ass1 with dissolve
            him"I think you are right! They do fit really well..."
            him"Must be the reason why athletes choose to wear these..."
            bo"...Right? So enough sulking!"
        "{color=[dominancecolor]}Can I be honest with you?{/color}":
            bo"Can I be honest with you [him_name]?"
            him"Sure..."
            bo"There's not much difference between your casual clothing and this..."
            call changeDominance(1) from _call_changeDominance_43
            bo"If anything, the loose pink shorts you wear home are probably revealing more than what tight burumas specifically made to enhance athletic performance would..."
            show opinion1_himt ass1 with dissolve
            him"You make a good point..."
            show opinion1_himt ass2 with dissolve
            show opinion1_himt ass2 at smallshake
            him"I guess I am just not used to the tightness of them..."
            show opinion1_himt ass3 with dissolve
            him"But now that you mention it, that's probably for the better, and they do feel kind of nice..."



    
    hide opinion1_himt
    show opinion2_himt beh:
        zoom 0.7 xalign 0.5
    with dissolve
    him"Hmm...! I think I decided then..."
    hide opinion2_himt beh
    show opinion1_himt:
        zoom 0.7 xalign 0.5
    with dissolve
    him"I want this!" with vpunch
    scene black with dissolve
    "Despite the occasion, a sudden melancholic look has captured [him_name]'s face..."
    show opinion_final
    show screen parallax1280("opinion_final") with dissolve
    call showscrollingimage from _call_showscrollingimage_1
    him"I'll put my shirt back on and we can get going. Don't want to have [hin_rel] worried about us..."
    bo"Sure..."
    bot"What's up with her sad expression though..."
    him"I was thinking..."
    him"Is it okay to spend your money on birthday gifts when [hin_rel] needs it more than I do...?"
    bo"I told you haven't I? This is part of my plan to help [hin_rel]!"
    him"But you still haven't told me what that plan is..."
    default v14_lockedscene2 = None
    call hidescrollingimage from _call_hidescrollingimage_2
    $ renpy.end_replay()
    menu burumafinalmenu:
        him"You still haven't told me what that plan is..."

        "{color=[lovecolor]}It's better if I show you...{/color}":
            call checkLove(3,"burumafinalmenu","Himawari") from _call_checkLove_3
            if v14_lockedscene2 == None:
                jump trydress_love
            else:
                label trydress_love:
                    $ initialize_replay_defaults()
                    show screen parallax1280("opinion_final") with dissolve
                    call showscrollingimage from _call_showscrollingimage_49
                    bo"I suppose it's time I fill you in..."
                    $ notification("Previously exclusive scene")
                    bo"You see, my plan might involve you being comfortable trying on some new clothes..."
                    him"...H-huh? Trying on clothes?"
                    him"How will that be of any help to [hin_rel]..."
                    bo"Did you not pay attention to what the clerk said before?"
                    show opinion_final:
                        easein 2 yalign 0.5
                    him"...G-get to the point!"
                    bo"'You have an eye for picking your modeling subjects, Monsooour [bo_name]!' Or something..."
                    call changeObedience("Himawari", 1) from _call_changeObedience_77
                    show opinion_final:
                        easein 1 yalign 0.1
                    him"You want me... to model for you?"
                    show screen parallax1280("opinion_final") with dissolve
                    call showscrollingimage from _call_showscrollingimage_50
                    bo"Come, it's better if I show you..."
                    call hidescrollingimage from _call_hidescrollingimage_6
                    scene black with dissolve
                    bo"You see..."
                    show bg fitting room with dissolve
                    show boruto normal at left with dissolve
                    show opinion1_himt at right with dissolve:
                        zoom 0.7
                    bo"I want to help you become a classy and coveted model..."
                    bo"One that wears dresses like these and promotes the most luxurious of brands..."
                    show boruto embarassed with dissolve
                    bo"You certainly have the attitude for it, maybe the looks too!"
                    bo"So why not give it a shot, starting with this dress!"
                    him"You really think this is a good idea?"
                    show boruto snob with dissolve
                    bo"Why not!"
                    show opinion1_himt:
                        easein 0.5 xalign 1.1
                    him"And you want me to try that dress on?"
                    bo"Yup!"
                    him"That's..."
                    scene black with vpunch
                    him"Almost laughable!"
                    him"Teehehe!" with vpunch
                    "[him_name]'s spirits were lifted once more..."
                    bo"H-hey! I am being serious you know..." with vpunch
                    show bg fitting room
                    show boruto surprised2 at left
                    show opinion2_himt beh at right:
                        zoom 0.7
                    hide opinion1_himt
                    with dissolve
                    him"S-so you really think I could help [hin_rel] w-with this modeling thing? *Nervous Laughter* Heh-heh..."
                    show boruto snob with dissolve
                    bo"There's nothing to lose by at least trying..."
                    show opinion2_himt beh at smallshake
                    him"B-but..."
                    show opinion2_himt beh at smallshake
                    him"There's no way I am wearing stuff like that in front of you!" with vpunch
                    him"It's way too r-revealing! And you are a p-perv, and stupid and weird!"
                    menu:
                        him"It's way too r-revealing! And you are a p-perv, and stupid and weird!"
                        "{color=[dominancecolor]}I am our only hope...{/color}":
                            bo"You can keep pretending I am all these things, but you cannot deny that right now I am the one with a plan..."
                            call checkDominance(15,"manwithaplan_him") from _call_checkDominance_12
                            if dominance <= 15:
                                label manwithaplan_him:
                                    him"...And?"
                                    "Your argument did not sound convincing enough to [him_name]..."
                                    him"Am I supposed to just jump into this m-modelling thing?"
                                    him"I need some t-time first to think things through..."
                                    him"M-maybe there's another way to help..."
                                    show boruto normal with dissolve
                                    bo"I am not so certain about that myself, but..."
                                    bo"You don't want to try on the dress right now? Fine by me..."
                                    bo"I still think you'd make a great model regardless!"
                                    call changeRespect("Himawari", 1) from _call_changeRespect_113
                                    him"...Of c-course I would!" with vpunch
                                    show opinion2_himt beh at smallshake
                                    him"Unlike yours, my face doesn't look like it's been ran over by a bulldozer!"
                                    bo"...Good one. Now get changed and let's get out of here!"
                                    hide boruto with dissolve
                                    him"O-okay..."
                                    hide opinion2_himt with dissolve
                                    show blackscreen with dissolve
                                    bo"I'll go pay for your stuff..."
                                    jump endendclothes

                            else:
                                him"That doesn't mean I have to jump straight into this m-modelling thing!" with vpunch
                                bo"The sooner the better, right? We have to help [hin_rel]..."
                                him"Stop with the 'helping' argument already! This is starting to sound like extortion..."
                                show boruto surprised2 with dissolve
                                bo"You know I didn't mean it like that! I am truly just trying to help..."
                                himt"Am I overthinking this?"
                                him"Uhm..."
                                hide opinion2_himt beh with dissolve
                                him"I'll t-try it... Just give me some time, okay?"
                                show boruto snob with dissolve
                                bot"Hell yeah!"
                                scene black with dissolve
                                scene bg fitting room2 with dissolve
                                him"I am sorry I lashed out on you..."
                                him"It's just that... things are moving way too fast for my liking..."
                                him"First you tell me about [hin_rel]'s troubles... Now I have to suddenly consider this modelling thing..."
                                him"Ugh!" with vpunch
                                him"You probably paid off the clerk to say all these things, didn't you?"
                                bo"What? No..."
                                him"I really hope this isn't a crappy prank of yours..."
                                bo"It's not..."
                                him"*Scoffs*..."
                                him"I am coming out! P-please don't be an idiot..."
                                scene black with dissolve
                                "[him_name] pushes the curtain aside..."
                                $ renpy.sound.play("/audio/soun_fx/curtainopening.opus", channel="sfx1", loop=False, relative_volume = 0.6)
                                show screen parallax1280("clothdress intro") with flash
                                call showscrollingimage from _call_showscrollingimage_51
                                bot"."
                                bot".."
                                bot"...Holy s-shit!"
                                show bg fitting room3
                                show clothdress introt:
                                    zoom 0.72 xalign 0.5
                                him"T-there you go... Happy now?"
                                bo"Happy? You haven't even posed for me yet..."
                                call hidescrollingimage from _call_hidescrollingimage_50
                                him"P-pose...? Come on [bo_name]! You know I am uncomfortable in this..."
                                him"What's with the thigh s-slits and all the jewelerry!"
                                him"Not to mention how tight it is around my midriff..."
                                him"This dress is... too m-much! Where would one even wear something like this at?"
                                bo"And therein lies the problem..."
                                bo"I can't have you feeling uneasy if we are to work together..."
                                show clothdress at smallshake
                                him"Who said we'll work together a-anyway..."
                                bo"I don't see you coming up with any other idea..."
                                show clothdress 0t with dissolve
                                him"...Goodness's sake [bo_name]!"
                                him"Let's get this over with... What do you need me to do?"
                                bo"For starters, why don't you stop hiding your chest..."
                                him"But the d-dress is..."
                                bo"What have I told you before, [him_name]..."
                                bo"A model's strength lies in their confidence."
                                bo"You don't wanna be weak, do you?"
                                show clothdress 1t with dissolve
                                him"You s-sound like a damned villain from one of those movies..."
                                menu:
                                    him"You s-sound like a damned villain from one of those movies..."
                                    "{color=[obediencecolor]}Morel like a hero that saves the damzel!{/color}":
                                        bo"More like a hero that saves the damzel..."
                                        bo"You certainly look like a damzel in need of saving right now!"
                                        show clothdress introt with dissolve
                                        him"You c-could never! Dumbass..."
                                        call changeObedience("Himawari",1) from _call_changeObedience_78
                                        him"..."
                                    "{color=[dominancecolor]}And you look like a villain's muse!{/color}":
                                        call changeDominance(1) from _call_changeDominance_61
                                        bo"And you could pass for a muse of such a villain with that dress on you!"
                                        bo"Perhaps I'll be the villain and you'll be my muse! *Haha!*"
                                        show clothdress at smallshake
                                        him"That's... the stupidest thing I've ever heard!"
                                    
                                bo"*Sigh*..."
                                bo"Look, don't get me wrong. You look nice and all, but right now you aren't selling me the dress..."
                                him"N-not my problem..."
                                bo"How do you reckon we'll secure any deals if you act like this..."
                                him"..."
                                show clothdress at smallshake
                                him"Get to the point already!"
                                bo"Alright then, I'll let you in on one of the industry's secrets..."
                                bo"Keeping your shoulders raised and tilting your head downwards is the easiest way to draw attention away from the subject, and onto the item."
                                bo"Try striking a pose like that and hold one of your arms to your waist..."
                                him"What, you think you are some sort of expert now?"
                                bo"Just try it..."
                                show clothdress pose1t with dissolve
                                bo"See...? Much better!"
                                show clothdress at smallshake
                                him"So says you!"
                                bo"Indeed! Since I am the expert here!"
                                bo"Come on...  You can do better than that!"
                                show clothdress pose0 with dissolve
                                him"Uuumm, I don't know what to do!"
                                bo"Try placing one of your legs in front of you and rest your palm on it. Remember to keep your shoulders elevated..."
                                show clothdress at smallshake
                                him"Something like..."
                                show clothdress pose2t with dissolve
                                him"This?"
                                bo"Not too bad! You are getting the hang of it..."
                                him"..."
                                bo"For this final pose, I want you to improvise..."
                                bo"Imagine you are trying to sell this dress, what pose would you strike?"
                                him"I have no idea..."
                                him"Maybe..."
                                show clothdress pose3t with dissolve
                                him"This?"
                                bo"See...? You can really lean into the role if you try a little bit."
                                show clothdress 0t with dissolve
                                call changeObedience("Himawari", 1) from _call_changeObedience_79
                                him"W-who said I want to lean into it..."
                                bo"I can't force you of course, but It would seem you are a natural..."
                                bo"I am certain you could make a fortune in this field if you trusted me a little bit more..."
                                show clothdress 2t with dissolve        
                                him"*Scoffs*..."
                                him"I've had enough of this silly parade of yours..."
                                him"Can we please go?"
                                menu:
                                    him"Can we please go?"
                                    "Alright, you've done well enough...":
                                        bo"Alright. I've seen enough. I am certain you could fit the bill..."
                                        show clothdress end2t with dissolve
                                        him"I will never get used to this..."
                                        show clothdress 2t with dissolve
                                        him"I am taking this thing off!"
                                        hide clothdress with dissolve
                                    "{color=[dominancecolor]}There's something you still haven't shown me yet...{/color}":
                                        bo"There's something you haven't shown me yet..."
                                        show clothdress 2t with dissolve
                                        him"H-huh?"
                                        bo"Do I have to spell it out for you?"
                                        him"I don't know what you are talking a-about..."
                                        bo"You haven't turned around for me, have you!?" with vpunch
                                        show clothdress end1t with dissolve
                                        him"I am not about to show you my bum!" with vpunch
                                        show clothdress at smallshake
                                        him"You freaking bum!"
                                        hide clothdress with dissolve
                                        him"Don't test your luck with me!"
                                        "[him_name] carefully took small steps backwards and entered the fitting room..."
                                        menu:
                                            "[him_name] carefully took small steps backwards and entered the fitting room..."
                                            "{color=[hatredcolor]}Peek inside!{/color}":
                                                show boruto sceeming2 at center with dissolve
                                                bot"I am not about to leave without taking a good look at your ass. You sexy little thing!"
                                                scene black with dissolve
                                                "You sneakily approached the changing room..."
                                                show screen parallax1280peek("clothdress peekt","bgp peak2") with dissolve
                                                "You peek through a very small opening in the curtains..."
                                                bot"...!" with vpunch
                                                him"Damned idiot..."
                                                him"Since when did he become so..."
                                                him"UUgh!" with vpunch
                                                him"He is getting on my nerves..." with vpunch
                                                him"But if he is trying to help [hin_rel], then..."
                                                him"I also have to try my best!"
                                                bot"You'll try your best..."
                                                bot"And little by little..." 
                                                bot"I'll make you mine!" with vpunch
                                                call hidescrollingimage from _call_hidescrollingimage_51
                                                hide screen parallax1280peek with dissolve
                                                scene black with dissolve
                                                "You sneakily took a few steps backwards to avoid raising suspicion..."
                                            "Don't":
                                                bot"Meh... I've had enough fun for today!"
                                show boruto surprised2 at center
                                with dissolve
                                bo"I a-am going to pay for your stuff, I'll be waiting for you outside..."
                                scene black with dissolve
                                jump endendclothes

                        "{color=[lovecolor]}*Laugh* You'll set the pace of course...{/color}":
                            show boruto laughing2 with dissolve
                            bo"*Laughs* There's the [him_name] I know!"
                            bo"Always something good to say about your [him_rel_to_bo_default]..."
                            him"Hmph! Then prove me wrong..."
                            show boruto normal with dissolve
                            bo"I'd like to do that, but I'll need you to at least give me a chance..."
                            bo"I don't want to force you to do something you don't feel comfortable doing..."
                            bo"So we'll move at your own pace, alright?"
                            bo"You don't want to try on the dress right now? Fine by me..."
                            bo"I still think you'd make a great model regardless!"
                            call changeLove("Himawari", 1) from _call_changeLove_39
                            him"...Of c-course I would!" with vpunch
                            show opinion2_himt beh at smallshake
                            him"Unlike yours, my face doesn't look like it's been ran over by a bulldozer!"
                            bo"...Good one. Now get changed and let's get out of here!"
                            hide boruto with dissolve
                            him"O-okay..."
                            show blackscreen with dissolve
                            "."
                            ".."
                            "..."
                            him"[bo_name], w-wait..." with vpunch
                            hide boruto
                            hide opinion2_himt
                            with dissolve
                            hide blackscreen 
                            show opinion2_himt beh at center:
                                zoom 0.7
                            him"I..." with vpunch
                            bo"What's wrong?"
                            him"I'll try on the dress..."
                            bo"You really don't ha-"
                            hide opinion1_himt
                            hide opinion2_himt
                            show opinion1_himt at center:
                                zoom 0.7
                            with dissolve
                            him"Only because I want to see how it would look on me!" with vpunch
                            show opinion1_himt at smallshake
                            him"You are not allowed to look!"
                            bo"But that defeats the entire purpose of wearing it...."
                            hide opinion1_himt with dissolve
                            "[him_name] ignores your remark and skittishly goes to check out the dress..."
                            him"It'll take a while to wear this thing..." 
                            scene black with dissolve
                            "But she also seemed somewhat giddy..."
                            bo"*Sigh*..."
                            show bg fitting room2 with dissolve
                            him"Don't even think about peeking you perv!" with vpunch
                            bo"W-why would I ever consider doing that..."
                            him"I don't know! Maybe because you are a perv who makes weird comments about my bum!?"
                            if not _in_replay:
                                if quest_him.is_state("him1L_4", "completed") == True or quest_him.is_state("him1H_4", "completed") == True:
                                    him"Remember that time you pretended there was a b-bug on me!?"
                                    bo"Pretended? It was literally right there! I showed it to you!"
                                    him"Yeah y-yeah, s-sure! J-just don't peek!" with vpunch
                                else:
                                    bo"I... *Sigh*"
                                    him"Don't peek!" with vpunch
                            menu:
                                him"Don't peek!"
                                "Peek!":
                                    show boruto sceeming2 at center with dissolve
                                    bot"I am not about to leave without at least taking a look..."
                                    scene black with dissolve
                                    "You sneakily approached the changing room..."
                                    show screen parallax1280peek("clothdress intro","bgp peak2") with dissolve
                                    bot"...!" with vpunch
                                    
                                    him"This dress... It's..."
                                    him"S-so pretty!" with vpunch
                                    bot"D-damn... She looks fucking incredible!"
                                    him"But also not something I'd ever wear!"
                                    him"The way it tightly wraps around my midriff, the thigh slits..."
                                    him"It's all a bit too much..."
                                    him"I could never wear this in front of [bo_name]..."
                                    him"...Model for him? Is he s-stupid?"
                                    show screen parallax1280peek("clothdress peekt","bgp peak2") with dissolve
                                    him"There's no way I am walking out there looking like this. I am taking this thing off!"
                                    bot"Holy shit! The ass she has on her..." with vpunch
                                    him"Damned idiot..."
                                    him"Since when did he become so..."
                                    him"Ugh!" with vpunch
                                    him"This is getting on my nerves..." with vpunch
                                    him"But if he is trying to help [hin_rel], then..."
                                    him"I also have to try my best!"
                                    him"But I s-sure hope he isn't getting any weird ideas..."
                                    hide screen parallax1280peek
                                    scene black with vpunch
                                    him"Why do I feel like he'd be behind the curtain if I opened it right now!" with vpunch
                                    bot"O-oh shit! Better get out of here..."
                                    "You sneakily took a few steps backwards to avoid raising suspicion..."
                                    scene bg fitting room2
                                    show boruto surprised2 at center
                                    with dissolve
                                    bo"I a-am going to pay for your stuff, I'll be waiting for you outside..."
                                    scene black with dissolve
                                    jump endendclothes
                                    
                                "I would never...":
                                    bo"I would never..."
                                    him"Hmmm...."
                                    him"Are you sure about that...?"
                                    bo"W-what!?" with vpunch
                                    bot"Is she playing games with me?"
                                    him"Because I think I am looking really pretty in this thing..."
                                    bo"Damn it [him_name]... Do you always have to tease me?"
                                    $ renpy.sound.play("/audio/soun_fx/curtainopening.opus", channel="sfx1", loop=False, relative_volume = 0.6)
                                    scene bg fitting room3
                                    show clothdress end2t at center:
                                        zoom 0.7
                                    with longerflash
                                    call changeLove("Himawari", 1) from _call_changeLove_40
                                    him"I wasn't teasing you..."
                                    bo"[him_name]..."
                                    him"S-so...?"
                                    him"...What do you t-think?"
                                    menu:
                                        him"...What do you t-think?"
                                        "{color=[obediencecolor]}That's a killer look for you!{/color}":
                                            bo"That suits you perfectly [him_name]! It's a killer look for you..."
                                            hide clothdress
                                            show clothdress pose0 at center:
                                                zoom 0.6
                                            with dissolve
                                            call changeObedience("Himawari", 1) from _call_changeObedience_80
                                            him"Y-you really think so?"
                                            bo"Absolutely!"
                                            him"It's way too... out there for me."
                                            him"It makes me feel uncomfortable..."
                                            hide clothdress with dissolve
                                            him"That's all you get!"
                                            him"I am taking this thing off. It was a bad idea to begin with..."
                                            bo"S-sure..."
                                            bot"Holy shit, did she look amazing..."
                                        "{color=[dominancecolor]}You look like a goddess!{/color}":
                                            call changeDominance(1) from _call_changeDominance_62
                                            bo"It's as if a goddess descended from the heavens above..."
                                            bo"You look incredible!"
                                            show clothdress pose1t at center:
                                                zoom 0.7
                                            with dissolve
                                            him"Eh-eh. You are being overly d-dramatic..."
                                          
                                            him"Not to mention that's weird coming from you!" with vpunch
                                            hide clothdress with dissolve
                                            him"That's all you get! I am taking this thing off..."
                                            bo"S-sure..."
                                            bot"Holy shit, did she look amazing..."
                                            menu:
                                                bot"Holy shit, did she look amazing..."
                                                "I need another look!":
                                                    show boruto surprised2 at center with dissolve
                                                    bot"Don't think I can resist another look at her after that..."
                                                    scene black with dissolve
                                                    "You sneakily approached the changing room..."
                                                    show screen parallax1280peek("clothdress peekt","bgp peak2") with dissolve
                                                    "You peek through a very small opening in the curtains..."
                                                    bot"...!" with vpunch
                                                    him"There's no way I'd ever wear this..."
                                                    him"Especially not to model f-for him!"
                                                    him"Since when did he become so..."
                                                    him"Ugh!" with vpunch
                                                    him"This is getting on my nerves..." with vpunch
                                                    him"But if he is trying to help [hin_rel], then..."
                                                    him"I also have to try my best!"
                                                    bot"D-damn... The ass she has on her!"
                                                    him"But I s-sure hope he isn't getting any weird ideas..."
                                                    call hidescrollingimage from _call_hidescrollingimage_52
                                                    hide screen parallax1280peek with dissolve
                                                    scene black with dissolve
                                                    "You sneakily took a few steps backwards to avoid raising suspicion..."
                                                "Better go pay for her stuff...":
                                                    pass
                                    scene bg fitting room2
                                    show boruto surprised2 at center
                                    with dissolve
                                    bo"I a-am going to pay for your stuff, I'll be waiting for you outside..."
                                    scene black with dissolve     
                                    jump endendclothes

                                        
                                



                        "{color=[hatredcolor]}That's it! I've had it with you...{/color}":
                            show boruto angry2 with dissolve
                            bo"That's it! I've had it with you..." with vpunch
                            bo"Here I am trying to help, and all I get is your shitty bratty attitude!"
                            hide opinion2_himt beh
                            show opinion2_himt at right:
                                zoom 0.7
                            with dissolve
                            bo"I am not buying you shit, I am done! Put your damn clothes on so we can leave..."
                            show opinion1_himt at right:
                                zoom 0.7
                            hide opinion2_himt
                            with dissolve
                            him"W-what? N-no... Wait!" with vpunch
                            bo"You either try that on, or we leave with nothing and you can try helping [hin_rel] on your own!" with vpunch
                            jump jumphatreddress


                        
                    bo"Nope! It's exactly the type of dress an elegant model would pose with..."
                    bo"If you'll end up as one, I have to make sure you are up to the task."
                    bo"You either try that on, or we leave with nothing and you can try helping [hin_rel] on your own!" with vpunch
                    show opinion2_himt at smallshake
                    call changeRespect("Himawari", -1) from _call_changeRespect_114 
                    him"And here I thought you were doing something nice for once..."
                    call changeHatred(1) from _call_changeHatred_99
                    bo"Oh I am doing something nice, you are just being a bit too prudish and unappreciative!"
                    bo"So which one will it be..."
                    hide opinion2_himt
                    show opinion1_himt at right:
                        zoom 0.7
                    with dissolve
                    him"F-fine! You freaking idiot..."
                    hide opinion1_himt with dissolve
                    scene black with dissolve
                    him"W-wait outside!"
                    bo"Don't mind If I do..."
                    scene bg fitting room2 with dissolve
                    him"You probably paid off the clerk to say all these things, didn't you?"
                    bo"Hah! You keep telling yourself that..."
                    bo"You'll see when I start raking in the money..."
                    bo"You'll be begging for my help!"
                    him"*Scoffs*..."
                    him"I am coming out! P-please don't be an idiot..."
                    scene black with dissolve
                    "[him_name] pushes the curtain aside..."
                    $ renpy.sound.play("/audio/soun_fx/curtainopening.opus", channel="sfx1", loop=False, relative_volume = 0.6)
                    show screen parallax1280("clothdress intro") with flash
                    call showscrollingimage from _call_showscrollingimage_52
                    bot"."
                    bot".."
                    bot"...Holy s-shit!"
                    show bg fitting room3
                    show clothdress introt:
                        zoom 0.72 xalign 0.5
                    him"T-there you go... Happy now?"
                    bo"Happy? You haven't even posed for me yet..."
                    call hidescrollingimage from _call_hidescrollingimage_53
                    him"P-pose...? Come on [bo_name]! You know I am uncomfortable in this..."


        "{color=[hatredcolor]}Blackmail her!{/color}":
            if v14_lockedscene2 == None:
                pass
            label replay_trydress_hatred:
            $ initialize_replay_defaults()
            show screen parallax1280("opinion_final") with dissolve
            call showscrollingimage from _call_showscrollingimage_2
            bo"Alright, I guess it's time I fill you in!"
            $ notification("Previously exclusive scene")
            bo"For starters, I am not buying you anything yet..."
            bo"Not before you prove your worth to me anyway!" with vpunch
            him"Prove my worth? What are you on about [bo_name]... I thought this was a birthday gift!"
            bo"It will be, just as soon as you try on a dress that my eyes were drawn to the moment we stepped in here!"
            him"If it's just a dress... I don't see why not."
            call hidescrollingimage from _call_hidescrollingimage_3
            scene black with dissolve
            bo"Not just any dress... Follow me!"
            "..."
            show bg fitting room with dissolve
            show boruto sceeming2 at left with dissolve
            bo"This dress!" with vpunch
            show opinion1_himt at right with dissolve:
                zoom 0.7
            him"You want me to... try that on?"
            bo"Yep!"
            him"The one the m-mannequin wears!?"
            bo"Yyyeep!"
            him"B-but..."
            show opinion2_himt at right:
                zoom 0.7
            hide opinion1_himt
            with dissolve
            him"It's way too.. r-revealing!"
            show boruto snob with dissolve
            bo"Nope! It's exactly the type of dress an elegant model would pose with..."
            bo"If you'll end up as one, I have to make sure you are up to the task."
            bo"You either try that on, or we leave with nothing and you can try helping [hin_rel] on your own!" with vpunch
            show opinion2_himt at smallshake
            label jumphatreddress:
            call changeRespect("Himawari", -1) from _call_changeRespect_110
            him"And here I thought you were doing something nice for once..."
            call changeHatred(1) from _call_changeHatred_85
            bo"Oh I am doing something nice, you are just being a bit too prudish and unappreciative!"
            bo"So which one will it be..."
            hide opinion2_himt
            show opinion1_himt at right:
                zoom 0.7
            with dissolve
            him"F-fine! You freaking idiot..."
            hide opinion1_himt with dissolve
            scene black with dissolve
            him"W-wait outside!"
            bo"Don't mind If I do..."
            scene bg fitting room2 with dissolve
            him"You probably paid off the clerk to say all these things, didn't you?"
            bo"Hah! You keep telling yourself that..."
            bo"You'll see when I start raking in the money..."
            bo"You'll be begging for my help!"
            him"*Scoffs*..."
            him"I am coming out! P-please don't be an idiot..."
            scene black with dissolve
            "[him_name] pushes the curtain aside..."
            $ renpy.sound.play("/audio/soun_fx/curtainopening.opus", channel="sfx1", loop=False, relative_volume = 0.6)
            show screen parallax1280("clothdress intro") with flash
            call showscrollingimage from _call_showscrollingimage_3
            bot"."
            bot".."
            bot"...Holy s-shit!"
            show bg fitting room3
            show clothdress introt:
                zoom 0.72 xalign 0.5
            him"T-there you go... Happy now?"
            bo"Happy? You haven't even posed for me yet..."
            call hidescrollingimage from _call_hidescrollingimage_4
            him"P-pose...? Come on [bo_name]! You know I am uncomfortable in this..."
            him"What's with the thigh s-slits and all the jewelry!"
            him"Not to mention how tight it is around my midriff..."
            him"This dress is... too m-much! Where would one even wear something like this at?"
            bo"And therein lies the problem..."
            bo"I can't have you feeling uneasy if we are to work together..."
            show clothdress at smallshake
            him"Who said we'll work together a-anyway..."
            bo"I don't see you coming up with any other idea..."
            bo"It's either this, or we live knowing [hin_rel]'s in constant danger. Can you live with that?"
            show clothdress 0t with dissolve
            him"...Goodness's sake [bo_name]!"
            him"Let's get this over with... What do you need me to do?"
            bo"For starters, why don't you stop hiding your chest..."
            him"But the d-dress is..."
            bo"What have I told you before, [him_name]..."
            bo"A model's strength lies in their confidence."
            bo"You don't wanna be weak, do you?"
            show clothdress 1t with dissolve
            him"You s-sound like a damned villain from one of those movies..."
            menu:
                him"You s-sound like a damned villain from one of those movies..."
                "{color=[hatredcolor]}Villains do much worse than this...{/color}":
                    bo"Villains do much worse than this, you know..."
                    show clothdress introt with dissolve
                    him"Don't even joke like that, dumbass!"
                    call changeHatred(1) from _call_changeHatred_86
                    bot"Who said I am joking..."
                "{color=[dominancecolor]}And you look like a villain's muse!{/color}":
                    call changeDominance(1) from _call_changeDominance_44
                    bo"And you could pass for a muse of such a villain with that dress on you!"
                    bo"Perhaps I'll be the villain and you'll be my muse! *Haha!*"
                    show clothdress at smallshake
                    him"That's... the stupidest thing I've ever heard!"
                
            bo"*Sigh*..."
            bo"Look, don't get me wrong. You look nice and all, but right now you aren't selling me the dress..."
            him"N-not my problem..."
            bo"I am afraid it is... We aren't leaving until I reach my conclusion for your qualities..."
            him"..."
            show clothdress at smallshake
            him"Get to the point already!"
            bo"Alright then, I'll let you in on one of the industry's secrets..."
            bo"Keeping your shoulders raised and tilting your head downwards is the easiest way to draw attention away from the subject, and onto the item."
            bo"Try striking a pose like that and hold one of your arms to your waist..."
            him"What, you think you are some sort of expert now?"
            bo"Just try it..."
            show clothdress pose1t with dissolve
            bo"See...? Much better!"
            show clothdress at smallshake
            him"So says you!"
            bo"Indeed! Since I am the expert here!"
            bo"Come on...  You can do better than that!"
            show clothdress pose0 with dissolve
            him"Uuumm, I don't know what to do!"
            bo"Try placing one of your legs in front of you and rest your palm on it. Remember to keep your shoulders elevated..."
            show clothdress at smallshake
            him"Something like..."
            show clothdress pose2t with dissolve
            him"This?"
            bo"Not too bad! You are getting the hang of it..."
            him"..."
            bo"For this final pose, I want you to improvise..."
            bo"Imagine you are trying to sell this dress, what pose would you strike?"
            him"I have no idea..."
            him"Maybe..."
            show clothdress pose3t with dissolve
            him"This?"
            bo"[him_name]..."
            menu:
                bo"[him_name]..."
                "{color=[hatredcolor]}You are one gifted whore-! {/color}":
                    bo"Y-you are one gifted who-" with vpunch 
                    bot"Ahem!"
                    bo"You did excellent..."
                "{color=[obediencecolor]}You are a natural...{/color}":
                    bo"See...? You can really lean into the role if you try a little bit."
                    show clothdress 0t with dissolve
                    call changeObedience("Himawari", 1) from _call_changeObedience_70
                    him"W-who said I want to lean into it..."
                    bo"I can't force you of course, but It would seem you are a natural..."
                    bo"I am certain you could make a fortune in this field if you trusted me a little bit more..."
            show clothdress 2t with dissolve        
            him"*Scoffs*..."
            him"I've had enough of this silly parade of yours..."
            him"Can we please go?"
            menu:
                him"Can we please go?"
                "Alright, you've done well enough...":
                    bo"Alright. I've seen enough. I am certain you could fit the bill..."
                    show clothdress end2t with dissolve
                    him"I will never get used to this..."
                    show clothdress 2t with dissolve
                    him"I am taking this thing off!"
                    hide clothdress with dissolve
                "{color=[hatredcolor]}There's something you still haven't shown me yet...{/color}":
                    bo"There's something you haven't shown me yet..."
                    show clothdress 2t with dissolve
                    him"H-huh?"
                    bo"Do I have to spell it out for you?"
                    him"I don't know what you are talking a-about..."
                    bo"You haven't turned around for me, have you!?" with vpunch
                    show clothdress end1t with dissolve
                    him"I am not about to show you my bum!" with vpunch
                    show clothdress at smallshake
                    him"You freaking bum!"
                    hide clothdress with dissolve
                    him"Don't test your luck with me!"
                    "[him_name] carefully took small steps backwards and entered the fitting room..."
                    menu:
                        "[him_name] carefully took small steps backwards and entered the fitting room..."
                        "{color=[hatredcolor]}Peek inside!{/color}":
                            show boruto sceeming2 at center with dissolve
                            bot"I am not about to leave without taking a good look at your ass you bitch!"
                            scene black with dissolve
                            "You sneakily approached the changing room..."
                            show screen parallax1280peek("clothdress peekt","bgp peak2") with dissolve
                            "You peek through a very small opening in the curtains..."
                            bot"...!" with vpunch
                            him"Damned idiot..."
                            him"Since when did he become so..."
                            him"UUgh!" with vpunch
                            him"He is getting on my nerves..." with vpunch
                            him"But if he is trying to help [hin_rel], then..."
                            him"I also have to try my best!"
                            bot"Yes, you little whore!"
                            bot"You'll try your best..."
                            bot"And little by little..." 
                            bot"I'll make you mine!" with vpunch
                            call hidescrollingimage from _call_hidescrollingimage_5
                            hide screen parallax1280peek with dissolve
                            scene black with dissolve
                            "You sneakily took a few steps backwards to avoid raising suspicion..."
                        "Don't":
                            bot"Meh... I've had enough fun for today!"

            scene black with dissolve
            $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            bo"I'll go pay for your stuff and wait outside while you take off that dress..."
            him"S-sure..."
            scene bg clothingstore with dissolve
            show clothing shopkeep at center with dissolve:
                zoom 0.73
            "Elegant shop clerk" "Monsieur, [bo_name]! Found something you like?"
            bo"I'd like to pay for this..."
            "Elegant shop clerk" "Now that the lady is occupied..."
            "Elegant shop clerk" "Monsieur Obo's referrals are not an everyday occurrence..."
            "Elegant shop clerk" "I shall put this item on the house's tab, fully expecting that you will be a valuable partner in the future!"
            "Elegant shop clerk" "I shall of course still grant you a receipt, for appearance’s sake!"
            him"[bo_name]. Are we good to go?"
            "The shop clerk proclaims loudly so that [him_name] would hear..."
            "Elegant shop clerk" "An expensive, but quality purchase Monsieur [bo_name]! That would be two hundred!" with vpunch
            bot"Is this guy the world's best wingman or something?"
            bot"How does Obo have this much pull anyway!"
            bo"Thank you sir!"
            hide clothing with dissolve
            scene black with dissolve
            $ playmusic("audio/ost/market.opus",0.6)
            "You left the store..."
            scene bg konoha2 with dissolve
            show himaschoolt normal at right with dissolve:
                zoom 0.55
            him"Two hundred!?" with vpunch
            show boruto snob at left with dissolve
            bo"You heard him..."
            him"[bo_name]! A-are you sure about this? We can refund the item you know..."
            bo"That's not happening..."
            him"How did you even get that much money!" with vpunch
            bo"I told you already. I've been working my ass off for [hin_rel]'s sake..."
            bo"Maybe yours too if you stopped being such a prude!"
            hide boruto with dissolve
            show himaschoolt angry with dissolve
            him"P-prude!?" with vpunch
            bo"Come on, let's walk home!"
            scene black with dissolve
            "..."
            show hima_walkstore_an with dissolve
            $ renpy.sound.play("/audio/soun_fx/walkingforest.opus", channel="sfx1", loop=False, relative_volume = 0.4)
            him"So you were serious... huh?"
            him"About the modeling thing..."
            bo"Of course! It's not a surefire way of making money of course..."
            bo"But with my knowledge and connections, along with your willingness of course, I think we could make quite the sum me and you!"
            bo"Besides, we have nothing to lose by at least trying, right?"
            him"I guess..."
            him"But what does modeling even entail for me..."
            him"Is it just... pictures and s-stuff?"
            bo"Pictures, poses, you know! The whole shebang!"
            him"Wouldn't that be... w-weird?"
            bo"Weird how?"
            him"With us being... y-you know..."
            bo"We won't be filming lingerie shoots or porno or anything!"
            him"[bo_name_stutter]! Don't even joke about stuff like that you stupid clown..." with vpunch
            bot"You have no idea the stuff I am thinking I'll have you do for me!"
            him"..."
            him"So... Just clothing brands and stuff?"
            bo"Maybe that... maybe a swim-suit or two. Maybe the dress you tried on! Who knows... Depends on what kind of deals I happen to secure..."
            him"Uhmm.. *Nervous laughter* S-swimsuits?"
            himt"A-and that dress!?" with vpunch
            himt"Is he fucking stupid? There's no way I am wearing that kind of stuff in front of him!"
            bo"Let's not get ahead of ourselves though. I am still figuring things out."
            bo"I'll keep you in the know, but for now don't mention any of this stuff to [hin_rel]..."
            bo"You know she'd stress out even more thinking that she's troubling us somehow..."
            him"I g-guess you are right about that..."
            scene black with dissolve
            "You've reached your home..."
            show bg porch
            show himaschoolt normal at right with dissolve:
                zoom 0.55
            show boruto snob at left with dissolve
            bo"I'll see you around then?"
            him"Y-yeah..."
            call changeRespect("Himawari", 1) from _call_changeRespect_111
            him"And thanks for the gift.."
            call changeLove("Himawari", 1) from _call_changeLove_36
            him"And for trying to help [hin_rel]..."
            hide boruto with dissolve
            bo"Don't stress it!"
            $ renpy.end_replay()
            $ talkedaboutmother = True
            $ quest.check("1_bohim_2", "completed")
            $ quest.check("2_bohim_2", "in progress")
            $ notification("Quest updated")
            $ himaintrotutorial2 = True
            jump action_taken
                        

                
                




        "{color=[obediencecolor]}You are about to be my modeling partner!{/color}":
            bo"Did you not pay attention to what the clerk said before?"
            show opinion_final:
                easein 2 yalign 0.5
            him"...Huh?"
            bo"'You have an eye for picking your modeling subjects, Monsooour [bo_name]!' Or something..."
            call changeObedience("Himawari", 1) from _call_changeObedience_71
            show opinion_final:
                easein 1 yalign 0.1
            him"You want me... to model for you?"
            bo"I don't see why not..."
            scene black with dissolve
            him"That's..."
            scene black with vpunch
            him"Almost laughable!"
            him"Teehehe!"
            "[him_name]'s spirit was lifted once more..."
            bo"Hey, I am serious you know!"
            $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            him"Let me just put my clothes back on and we can talk about it..."
            bo"I'll go pay for your stuff and wait outside..."
            label endendclothes:
            him"Okay!"
            scene bg clothingstore with dissolve
            show clothing shopkeep at center with dissolve:
                zoom 0.73
            "Elegant shop clerk" "Monsieur, [bo_name]! Found something you like?"
            bo"I'd like to pay for this..."
            "Elegant shop clerk" "Now that the lady is occupied..."
            "Elegant shop clerk" "Monsieur Obo's referrals are not an everyday occurrence..."
            "Elegant shop clerk" "I shall put this item on the house's tab, fully expecting that you will be a valuable partner in the future!"
            "Elegant shop clerk" "I shall of course still grant you a receipt, for appearance’s sake!"
            him"[bo_name]. Are we good to go?"
            "The shop clerk proclaims loudly so that [him_name] would hear..."
            "Elegant shop clerk" "An expensive, but quality purchase Monsieur [bo_name]! That would be two hundred!"
            bot"Is this guy the world's best wingman or something?"
            bot"How does Obo have this much pull anyway!"
            bo"Thank you sir!"
            hide clothing with dissolve
            scene black with dissolve
            $ playmusic("audio/ost/market.opus",0.6)
            "You left the store..."
            scene bg konoha2 with dissolve
            show himaschoolt normal at right with dissolve:
                zoom 0.55
            him"Two hundred!?" with vpunch
            show boruto snob at left with dissolve
            bo"You heard him..."
            him"[bo_name]! A-are you sure about this? We can refund the item you know..."
            bo"That's not happening..."
            him"How did you even get that much money!" with vpunch
            bo"I told you already. I've been working my ass off for [hin_rel]'s sake..."
            hide boruto with dissolve
            bo"Come on, let's walk home!"
            scene black with dissolve
            "..."
            show hima_walkstore_an with dissolve
            $ renpy.sound.play("/audio/soun_fx/walkingforest.opus", channel="sfx1", loop=False, relative_volume = 0.4)
            him"So you were serious... huh?"
            him"About the modeling thing..."
            bo"Of course! It's not a surefire way of making money of course..."
            bo"But with my knowledge and connections, along with your willingness of course, I think we could make quite the sum me and you!"
            bo"Besides, we have nothing to lose by at least trying, right?"
            him"I guess..."
            him"But what does modeling even entail for me..."
            him"Is it just... pictures and s-stuff?"
            bo"Pictures, poses, you know! The whole shebang!"
            him"Wouldn't that be... w-weird?"
            bo"Weird how?"
            him"With us being... y-you know..."
            bo"We won't be filming lingerie shoots or porno or anything!"
            him"[bo_name_stutter]! Don't even joke about stuff like that you stupid clown..." with vpunch
            him"..."
            him"So... Just clothing brands and stuff?"
            bo"Maybe that... maybe a swim-suit or two. Depends on what kind of deals I happen to secure..."
            himt"Swim-suits... Eh-eh..."
            bo"Let's not get ahead of ourselves though. I am still figuring things out."
            bo"I'll keep you in the know, but for now don't mention any of this stuff to [hin_rel]..."
            bo"You know she'd stress out even more thinking that she's troubling us somehow..."
            him"I g-guess you are right about that..."
            scene black with dissolve
            "You've reached your home..."
            show bg porch
            show himaschoolt normal at right with dissolve:
                zoom 0.55
            show boruto snob at left with dissolve
            bo"I'll see you around then?"
            him"Y-yeah..."
            call changeRespect("Himawari", 1) from _call_changeRespect_112
            him"And thanks for the gift.."
            call changeLove("Himawari", 1) from _call_changeLove_37
            him"And for trying to help [hin_rel]..."
            hide boruto with dissolve
            bo"Don't stress it!"
            $ renpy.end_replay()

            default talkedaboutmother = False
            $ talkedaboutmother = True
            $ quest.check("1_bohim_2", "completed")
            $ quest.check("2_bohim_2", "in progress")
            $ notification("Quest updated")
            $ himaintrotutorial2 = True
            jump action_taken
            





            
        

