default high_score = 0

screen workmenutopright():
    imagebutton:
        xalign 0.98 yalign 0.02
        auto "images/ui/workmenu2_%s.webp"
        hovered Show("displayTextScreen", displayText = "Open Work Menu")
        unhovered [Hide("displayTextScreen")]
        action [SetVariable("selected_workmenu", "yoruichi"),Show("workmenu")]
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"
        


label work:
    call hidemarketUI from _call_hidemarketUI_9
    default workupdatedquest = False
    default showuptowork = 0
    default spyworkmapcounter = 0 # used to ontrol flow when entering work's map
    #
    if day_part == 3:
        call hideUI from _call_hideUI_56
        $ playmusic("/audio/ost/kumogakure.opus", 0.5)
        hide screen housemap
        call hideButtons from _call_hideButtons_8
        scene black with dissolve
        scene ramen worknight with dissolve
        if quest.is_state("job_3", "in progress") : #first time spying

            bot"There is nothing to do here at this time... I think?"
            $ renpy.sound.play("/audio/soun_fx/intro/introwoman1.opus", channel="sfx3", loop=False, relative_volume = 0.8)
            bot"Wait a second... I can hear strange faint sounds from upstairs!"
            bot"It must be Obo and Yoru..."
            bot"Yoru sounds like she is... distressed!"
            bot"What the hell is going on..."
            bot"Shall I go upstairs and investigate?"
            menu:
                bot"Shall I go upstairs and investigate?"
                "Yes":
                    $ spyworkmapcounter +=1
                    bot"I have to! But I need to be careful... wouldn't want to get caught."
                    scene black with dissolve
                    bot"This place sure is bigger than it would first appear. It looks like the ground floor was repurposed to be a ramen shop..."
                    show ramenshop stairs with dissolve
                    bot"But the upper floor seems to be an old house of sorts..."
                    bot"Obo and Yoru must be staying here during the night..."
                    show screen workmap_staircase
                    "Search around to find points of interest"
                    $ ui.interact()
                "Return":
                    jump market

        elif quest.is_state("job_4", "in progress") : #second time spying
            scene ramen worknight with dissolve
            $ renpy.sound.play("/audio/soun_fx/intro/introwoman1.opus", channel="sfx3", loop=False, relative_volume = 0.8)
            bot"Am I really about to do this again, knowing what's going on...?"
            bot"But maybe I can find out some useful information..."
            menu:
                bot"But maybe I can find out some useful information..."
                "Go upstairs":
                    $ spyworkmapcounter = 2
                    bot"Fuck... here goes nothing."
                    show ramenshop stairs with dissolve
                    show screen workmap_staircase
                    "Search around to find points of interest"
                    $ ui.interact()
                "Leave":
                    bo"I'd rather not see that again..."
                    jump market
        elif quest.is_state("job_4", "completed") : #second time spying
            scene ramen worknight with dissolve
            $ renpy.sound.play("/audio/soun_fx/intro/introwoman1.opus", channel="sfx3", loop=False, relative_volume = 0.8)
            bot"What am I doing here knowing what's going on...?"
            bot"But what if I missed some crucial information..."
            menu:
                bot"But what if I missed some crucial information..."
                "Go upstairs":
                    bot"Fuck... here goes nothing."
                    show ramenshop stairs with dissolve
                    show screen workmap_staircase
                    "Search around to find points of interest"
                    $ ui.interact()
                "Leave":
                    bo"I'd rather not see that again..."
                    jump market
                
        else:
            bot"This place is closed during nights..."
            bot"Strange... Given how popular it seems to be during daytime."
            bot"In any case, there's nothing for me to do here right now... I think?"
            menu:
                bot"In any case, there's nothing for me to do here right now... I think?"
                "Return":
                    jump market
                



        
    else:
        call hideUI from _call_hideUI_57
        scene ramenintro with dissolve
        show boss normal at center with dissolve
        obo"Oh? Look who decided to show up..."
        obo"Ready to get some work done kid?"
        menu ramenshop_obo_startingmenu:
            obo"Ready to get some work done kid?"
            "Start shift":
                bo"On with it then!"
                obo"You'll be manning the kitchen post along with Yoru. I will be out handling everything else."
                jump ramenkitchen
            #todo
            # "1sttime": #hide after 1st time
            #     bo"On with it then!"
            #     obo"You'll be manning the kitchen post along with Yoru. I will be out handling everything else."
            #     jump ramenkitchen

            # "Invite [hin_name] to work":
            #     bo"On with it then!"
            #     obo"You'll be manning the kitchen post along with Yoru. I will be out handling everything else."
            #     jump ramenkitchen

            "Ask about [hin_name]" (advancement_event=True) if v21ramenintro_progression == 1:
                $ v21ramenintro_progression = 2
                jump v21_ramenintro_firstdaytalk

            "Work another shift with [hin_name]" if v21ramenintro_progression == 2:
                dev "Work in progress, check back soon!"
                jump ramenshop_obo_startingmenu


            "Maybe later":
                bo"Maybe later old man..."
                scene black with dissolve
                jump market
            
default ramenkitchenintrotalk = False #used at the end of start_qte label to jump to shiftend after completing all tutorials
label ramenkitchen:
    scene ramenkitchen with dissolve
    show boruto normal at left with dissolve
    show yoru normal at right with dissolve
    if ramenkitchenintrotalk == False:
        bo"Hello, we've met before, remember me?"
        yo"There's work to be done kid. This is not the time to chit-chat..."
        yo"I'll tell you one thing and one thing only. So long as Obo isn't around, this place is my domain..."
        show yoru lookingbackt with dissolve:
            zoom 0.5 ypos 1.05
        yo"And in my domain, you'll follow my rules. Understood?"
        menu:
            yo"And in my domain, you'll follow my rules. Understood?"
            "You got it, ma'am!":
                show boruto embarassed with dissolve
                show yoru lookingbackt:
                    easeout 2 xpos 1.90
                bo"Your wish is my command, Ma'am!"
                show boruto worried with dissolve
                bot"Off she goes..."
                "She quickly sheered away paying no attention to you or your reply..."
            "How about you follow mine!?":
                show boruto sceeming3 with dissolve
                show yoru lookingbackt:
                    easeout 2 xpos 1.90
                bo"How about you follow my rules instead!" with vpunch
                "She quickly sheered away paying no attention to you or your reply..."
                show blackscreen with dissolve
                show screen genericparallaxramen("yoru lookingback") with vpunch
                "Or so you thought..."
                "As she kept an eye on you while seductively walking away..."
                "Click twice to continue"
                window hide
                $ ui.interact()
                hide screen genericparallaxramen
                show boruto normal with dissolve
                hide blackscreen with dissolve
            "I am just here to get paid, lady...":
                show boruto snob with dissolve
                show yoru lookingbackt:
                    easeout 2 xpos 1.90
                bo"I am just here to make some money, lady..."
                "She quickly sheered away paying no attention to you or your reply..."
    $ ramenkitchenintrotalk = True
    show screen workmenutopright
    menu ramenkitchenmenu:
        "You take some time along with Yoruichi to prepare for this shift..."
        "Let's get to work":
            if yoruichi_relationship == "Passive":
                show yoru lookingbackt at right with dissolve:
                    zoom 0.5 ypos 1.05
                yo"Remember... my kitchen, my rules. Follow my lead!"
                hide yoru with dissolve
                hide boruto with dissolve
            elif yoruichi_relationship == "Formal":
                show yoru lookingbackt at right with dissolve:
                    zoom 0.5 ypos 1.05
                if yoru_kneeled == True and yoru_kneeled_talk ==2:
                    yo"Get to work, kid!"
                    bot"She is still pissy..."

                elif yoru_kneeled == True:
                    yo"Get to work! You piece of shit..."
                    bot"Heh! She still thinks she owns this place! Not for long you whore..."
                else:
                    yo"Come on kid, we have work to do!"
                hide yoru with dissolve
                hide boruto with dissolve

            elif yoruichi_relationship == "Apprehensive":
                show boruto sceeming2 with dissolve
                show yoru lookingbackt at right with dissolve:
                    zoom 0.5 ypos 1.05
                bo"Come on Yoru, get your ass to work!"
                yo"...*scoffs*"
                hide yoru with dissolve
                hide boruto with dissolve

            elif yoruichi_relationship == "Obedient":
                show yoru lookingbackt at right with dissolve:
                    zoom 0.5 ypos 1.05
                show boruto snob with dissolve
                bo"Is my pretty girl ready for work?"
                yo"Y-yes..."
                hide yoru with dissolve
                hide boruto with dissolve
            elif yoruichi_relationship == "Unwillingly Obedient":
                show boruto sceeming2 with dissolve
                show yoru lookingbackt at right with dissolve:
                    zoom 0.5 ypos 1.05
                bo"Come on Yoru! Get your pretty ass to work!"
                yo"Y-yes [bo_name]..."
                hide yoru with dissolve
                hide boruto with dissolve
            
            else:
                show boruto sceeming2 with dissolve
                show yoru lookingbackt at right with dissolve:
                    zoom 0.5 ypos 1.05
                yo"..."
                hide yoru with dissolve
                hide boruto with dissolve
            jump start_qte


        "Interact with Yoruichi":
            default yoruinteract_afteroboquest = False
            #one time events ------------------------------------------------------------------------------------------

            #obo quest 1
            if (yorudontdoanything1 == True or yorudontdoanything2 == True) and yoruinteract_afteroboquest == False:
                show boruto worried2 at left with dissolve
                bo"Hey Yoru, About what happened..."
                show yoru shy2 at right with dissolve
                yo"T-thank you for trying to help kid but..."
                show yoru shy with dissolve
                yo"I am.. e-embarassed about what happened. Give me some time okay?"
                show yoru normal with dissolve
                yo"Let's focus on the task at hand for now, we can talk about it next time..."
                hide boruto
                hide yoru
                with dissolve
                $ yoruinteract_afteroboquest = True
                $ yoruichiinteractiontaken = True
                jump ramenkitchenmenu
            elif (yorudontdoanything1 == False and yoruinteract_afteroboquest == False) and score_3_claimed == True:
                if yoru_kneeled == True:
                    show boruto sceeming2 at left with dissolve
                    bo"Where's my kitchen's whore at!"
                    show yoru angry3 at right with dissolve
                    yo"Fuck off kid! You have the nerve to approach me after what you've done?"
                    yo"Don't talk to me you piece of shit!"
                    hide yoru with dissolve
                    bot"She has no idea what I have in store for her!"
                    bot"But I might have to find out something about her before that..."
                    hide boruto with dissolve
                    $ yoruinteract_afteroboquest = True
                    $ yoruichiinteractiontaken = True
                else:

                    show boruto snob at left with dissolve
                    bo"Where's my obedient pretty girl at?"
                    show yoru shy at right with dissolve
                    yo"Is that it then kid? Are you going to be just another asshole I'll have to deal with?"
                    menu:
                        yo"Is that it then kid? Are you going to be just another asshole I'll have to deal with?"
                        "I'll be more than an asshole!":
                            bo"You'll soon come to find out..."
                            show boruto sceeming3 with dissolve
                            call borutoevil2 from _call_borutoevil2_5
                            call changeHatred(1,"none") from _call_changeHatred_51
                            bo"I'll be much more than an asshole!"
                        "Depends on you...":
                            show boruto sceeming with dissolve
                            bo"Not if I don't have to be one."
                            show boruto sceeming2 with dissolve
                            bo"You'll be the one deciding that!"
                    show yoru normal with dissolve
                    yo"What d-does that even mean... You are just a kid, get a grip!"
                    yo"Focus on the task at hand for now, we'll talk another time."
                    hide yoru with dissolve
                    bot"She has no idea what I have in store for her!"
                    hide boruto with dissolve
                    $ yoruinteract_afteroboquest = True
                    $ yoruichiinteractiontaken = True
                    jump ramenkitchenmenu
                    
            #----------------------------------------------
            #----------------------------------------------
            #----------------------------------------------

            if yoruichiinteractiontaken == True:
                "You can only interact with Yoruichi once per shift"
                jump ramenkitchenmenu


            if yoruichi_relationship == "Passive":
                show boruto smirk at left with dissolve
                bo"Hey Yoruichi!"

                show yoru normal at right with dissolve:
                    zoom 1.0
                yo"I thought I told you already kid, this is no time to chit-chat..."
                show yoru angry with dissolve
                yo"Keep it shut and get ready to work!"
                hide yoru with dissolve
                show boruto worried with dissolve
                bot"Damn... I guess I'll have to earn her trust somehow."
                jump ramenkitchenmenu
            else:
                jump yoruichiinteractions

        "Skip shift" if allmoneypaid == True:
            "Skipping this shift will advance the time and grant you a 5$ flat payment."
            menu:
                "Skipping this shift will advance the time and grant you a 5$ flat payment."
                "Skip":
                    scene black with dissolve
                    call changeMoney(5) from _call_changeMoney_10
                    "You put in the bare minimum effort and leave as soon as you can..."
                    jump action_taken
                "Return":
                    jump ramenkitchenmenu
                
        "Information":
            # $ selected_workmenu = "yoruichi"
            $ update_yoruichi_objectives()  #run function to check yoruichi objectives
            show screen workmenu
            jump ramenkitchenmenu
        
        # "test relationships, remove when done":
        #     menu:
        #         "relationship status"

        #         "obedient":
        #             $ yoruichi_relationship = "Obedient"
        #         "unwillingly obedient":
        #             $ yoruichi_relationship = "Unwillingly Obedient"
        #         "apprehensive":
        #             $ yoruichi_relationship = "Apprehensive"
        #         "formal":
        #             $ yoruichi_relationship = "Formal"
        #     jump ramenkitchenmenu
                

        # "test leave, remove when done":
        #     jump action_taken

        








label shiftend:
    scene ramen workend with dissolve
    show boruto normal with dissolve
    bot"I am done for the day. I should head home..."  
    # $ showuptowork +=1     
    # if showuptowork > 4:
        
    #     if workupdatedquest == False:
    #         bo"Man... this shit really does not pay much for the effort it takes."
    #         $ quest.check("job_2", "completed")
    #         $ quest.check("job_3", "in progress")
    #         $ notification("Quest updated")
    #         bo"I need to look into an alternative method of making money..."
    #         $ workupdatedquest = True
    scene black with dissolve
    jump action_taken


label score_1: #obo's gift
    scene ramenkitchen with dissolve
    show boruto normal at left with dissolve
    show boss normal at right with dissolve
    obo"I've been watching you work kid, you are not as bad as I initially thought."
    show boss angry2 with dissolve
    obo"But you are still shite! Keep grinding and I might have a little something for you."
    bo"..."
    show boss normal with dissolve
    default obotrickquestion = False
    obo"How's Yoru been treating you?"
    menu :
        obo"How's Yoru been treating you?"
        "She doesn't talk much...":
            show boruto worried with dissolve
            bo"She doesn't talk too much, does she?"
            show boss laugh2 with dissolve
            obo"Not to twerps she doesn't! Haa-haa!"
            show boss normal with dissolve
            obo"You'll have to prove yourself first kid..."
        "She is... alright I guess":
            show boruto worried with dissolve
            bo"I wouldn't know, she said maybe three words? She is alright I guess."
            show boss angry2 with dissolve
            obo"She has what... 20 years on you kid? What do you want her to do. Recite bed-time children's stories to you?"
            show boss normal with dissolve
            obo"Be happy she tolerates you in her kitchen..."
            show boruto normal with dissolve
            obo"You'll get to know her better if she wants you to and not before."

        "She is a bit of a bitch!":
            show boruto angry with dissolve
            bo"She doesn't say shit old man. In fact she is a bit of a bitch with a bossy atittude."
            show boss angry2 with dissolve
            obo"Hey Kid..."
            show boss angry3 with vpunch:
                easein 0.4 xalign 0.8 zoom 1.05
            obo"That's my wife you are talking about!"
            show boss angry3 with vpunch:
                easein 0.4 xalign 0.7 zoom 1.1
            obo"You wanna say that again?"
            menu:
                obo"You wanna say that again?"
                "Yoru is a BITCH!":
                    show boruto snob with dissolve
                    bo"Yoru is a BITCH!" with vpunch
                    show boss angry2 at right with dissolve:
                        zoom 1.0
                    obo"Ooooh...?"
                    obo"Not too shabby kid, you speak your mind as any man should."
                    show boss laugh with dissolve
                    obo"You are not wrong, Yoru can be a bitch... That is if she is left without a leash and a collar..."
                    show boss angry3 with vpunch
                    obo"Which is why I am responsible for keeping her disciplined and in check."
                    show boss laugh with dissolve
                    obo"You keep up the good job and you too might be able to tame her in due time!"
                    jump trickquestionpass
                "Uhh... I take it back!":
                    show boruto worried with dissolve
                    bo"Uhhhm sorry old man, I take that back."
                    show boss angry2 at right with dissolve:
                        zoom 1.0
                    obo"I was right when I said your balls have yet to drop..."
            show boss laugh with dissolve
            $ obotrickquestion = True
            obo"Haa-haa! You can relax, I was testing you kid!"
            show boruto surprised2 with dissolve
            bo"T-testing...me? For what?"
    if obotrickquestion == False:
        label trickquestionfailed:
            show boss normal with dissolve
            obo"But also, that was a trick question and you failed."
            show boruto normal with dissolve
            bo"...huh?"
    show boss normal with dissolve
    label trickquestionpass:
        obo"In any case, I have a little something for you kid! For your contribution until now..."
        call getItem(condoms,1) from _call_getItem_3
        obo"Here, have this!"
        show boruto surprised3 with dissolve
        bo"A... condom?"
        menu:
            bo"A... condom?"
            "What am I supposed to do with this?":
                show boruto surprised2 with dissolve
                bo"W-what the hell am I supposed to do with this?"
                show boss angry2 with dissolve
                obo"Hmm... Let me think kid. Oh I know!-"
                show boss angry3 with vpunch
                obo"Maybe shove it up your ass so I can rail you tonight?"
                show boruto smirk with dissolve
                bo"Another one of your shitty gay jokes? I can already read right through you old fart!"
                show boss laugh with dissolve
                obo"Haa-haaaa! Ya got me..."
                obo"I don't know kid, I stole that from the cute shopkeeper next door. I have no use for rubbers. I am a hardcore raw-dogging advocate."
                obo"I suppose you can try getting your little prick wet with it..."
                hide boss with dissolve
                obo"Haa-ha-haaaaa"
            "Is this so I can rail your wife?":
                show boruto smirk2 with dissolve
                bo"Is this so I can rail your wife you old fart?"
                show boss laugh2 with dissolve
                show boruto snob with dissolve
                obo"Haa-haa... Be my guest kid. Although..."
                show boss laugh with dissolve
                obo"Yoru wouldn't let you touch her with a 10-foot pole!"
                obo"Haa-haaaa-ha!"
    hide boss with dissolve
    obo"Get back to work kid, there's shit to be done around here!"
    bot"This guy keeps getting weirder and weirder..."    
    jump ramenkitchenmenu

label score_2: #yoruichi's story 1
    show yoru shy at right with dissolve
    yo"Hey kid..."
    show boruto surprised2 at left with dissolve
    bo"Huh? So you do speak after all..."
    show boruto smirk with dissolve
    yo"When I need to and not before..."
    yo"Listen, I've seen how you keep looking at me these past few days..."
    show boruto surprised3 with dissolve
    bo"O-Oh I-" with vpunch
    yo"You must be curious... about everything."
    menu :
        yo"You must be curious... about everything."
        "Y-yeah, just c-curious":
            show boruto surprised2 with dissolve
            bo"Y-yeah, just curious is all. You got that r-right..."
            show boruto worried with dissolve
        "Oh I am more than curious about you, Yoru!":
            show boruto sceeming2 with dissolve
            bo"Oh I am more than curious about you.. Yoru!"
            yo"...H-huh?"
            show boruto snob with dissolve
            "Your insinuation went over her head..."
    show yoru normal with dissolve
    yo"Kids and their curiosities... they must be satisfied or else they turn into pests."
    yo"I Know you have questions to ask and given the effort you put in my kitchen, I think it's only fair you get to ask them..."
    show yoru shy2 with dissolve
    yo"I am not a cold-hearted bitch you know... It's just that, there's a lot on my mind right now."
    show yoru obedient with dissolve
    yo"Ask away if you have to... I owe you at least a few answers."
    $ yorumenu1 = []
    menu yoruintromenu1:
        set yorumenu1
        yo"Ask away if you have to... I owe you at least a few answers."
        "Why are you working here...":
            bo"So uuh, What's your background, why are you working here? You seem like you could take care of yourself in better ways..."
            show yoruflashintro1 with flash
            show yoruflashintro1:
                easein 4 zoom 0.8 xalign 0.5 yalign 0.5
            yo"Hmph. Funny you say that..."
            yo"I wasn't always like... this, you know..."
            yo"But that's a story for another time..."
            hide yoruflashintro1 with dissolve
            show yoru shy with dissolve
            yo"I am not from around these places kid. You could probably already tell from my skin color..."
            yo"People in your village... they seem to have an issue with my looks, something about my skin-color and looking like I am from an opposing village... or something?"
            show boruto surprised2 with dissolve
            bo"Kumogakure... The land of lightning. The same people that my [hin_rel] ran into problems with..."
            show boruto worried with dissolve
            bo"It's true that you resemble their appearance. With us and Kumogakure being at odds, people must be associating your looks with them..."
            show yoru obedient with dissolve
            yo"Evidently..."
            yo"So when I first came here, they'd spit in my face and call me names..."
            yo"Obo was the only one who showed some... interest."
            yo"Seeing how we shared appearances... I thought he could help, and so I trusted him."
            bo"That makes sense, Obo gets a pass from all the discrimination due to his teddy bear looks and the fact that he keeps people's bellies full..."
            show yoru shy2 with dissolve
            yo"T-teddy bear looks...? He is not what he seems kid..."
            menu:
                yo"T-teddy bear looks...? He is not what he seems kid..."
                "So did he help?":
                    bo"I can tell that much. So...? Did Obo help?"
                "What do you mean?":
                    bo"I can see he acts strange at times... But what do you mean by that?"
            show yoru obedient with dissolve
            yo"I don't want to get into that right now kid..."
            default yoruintro2continue = False
            $ yoruintro2continue = True 
            jump yoruintromenu1
        "What's up with you and Obo, he seems weird":
            bo"What's up with Obo... He is a strange guy, isn't he?"
            show yoru normal with dissolve
            yo"Strange... is one way to put it."
            yo"Obo is an asshole, but without him I'd be left begging in the streets or more likely, dead..."
            bo"..."
            show yoru normal2 with dissolve
            yo"Listen kid, I owe some dangerous people a lot of money. I had to run far away from home or risk my head being mounted on a spike."
            yo"Obo offered me a place to stay and a job where I'd be hidden from the spotlight, so long as I worked back here in the kitchen for him."
            show yoru shy2 with dissolve
            yo"I have no choice but to endure this fate. At least up until I can make ends meet"
            menu:
                bo"..."
                "Working for him wasn't his only demand, was it?":
                    bo"Working for Obo wasn't his only demand, was it?"
                    show yoru shy with dissolve
                    yo"It... wasn't."
                    yo"He said I'd have to stay with him here during nights and eventually he demanded that we got married."
                "But why marry him?":
                    bo"But why marry him if he is an asshole?"
                    show yoru normal with dissolve
                    yo"You are so naive, kid..."
                    show yoru normal2 with dissolve
                    yo"Why else... He demanded it. I was forced into it..."
                    yo"Do you think I enjoy being around a greasy old fat man?"
            show yoru obedient with dissolve
            yo"During nights Obo turns into..."
            show yoru shy with dissolve
            yo"N-nevermind... Bottom line is, I have no choice but to obey Obo's demands."
            $ notification("Quest Updated")
            $ quest.check("job_2", "completed")
            $ quest.check("job_3", "in progress")
            bot"Obey...? But why? Hmm... I should investigate this place during nights and find out what Yoru meant by that..."
            show boruto normal with dissolve
            default yoruintro1continue = False
            $ yoruintro1continue = True     
            jump yoruintromenu1

        "You are hot as fuck! Come with me instead" if yoruintro1continue == True and yoruintro2continue == True:
            show boruto sceeming with dissolve 
            bo"You are hot as fuck Yoru, come with me instead!"
            show yoru disgust with dissolve
            yo"I see Obo's shitty humour has rubbed on to you..."
            show yoru normal with dissolve
            yo"Don't be joking with me like that kid, you don't know me."
            show boruto sceeming2 with dissolve 
            bot"Who said I am joking..."
        "Continue" if yoruintro1continue == True and yoruintro2continue == True:
            bo"Thanks for opening up a little bit..."
            pass
    yo"We've said enough... Let's get back to work"
    $ notification("Yoruichi's relationship changed to 'Formal'")
    $ yoruichi_relationship = "Formal"
    $ shifts_completed = 0
    hide yoru with dissolve
    "From now on, Yoruichi's relationship status will be altered based on your actions."
    hide boruto with dissolve
    $ yoruichiinteractiontaken = True  
    jump ramenkitchenmenu


label score_3: #yoruichi's story 2 (yoruichi score)
    $ initialize_replay_defaults()
    if _in_replay:
        show ramenkitchen
    default yoru_kneeled = False
    hide yoru with dissolve
    show boss angry at right with dissolve
    show boruto normal at left with dissolve
    obo"I'll be damned kid... You are outperforming Yoruichi herself!"
    show boss angry2 with dissolve
    obo"To think she's been working here for more than a year, trained by yours truly and even so, still outmatched by a twerp."
    show boss angry3 with dissolve
    obo"This is cause for punishment, don't you think?"
    menu:
        obo"This is cause for punishment, don't you think?"
        "She deserves it!":
            show boruto sceeming2 with dissolve
            call changeHatred(1,"none") from _call_changeHatred_52
            bo"You are right, she deserves it!"
            show boruto sceeming with dissolve
            bo"I've been here for only a few days and I am already more useful than she is!"
            show boss angry2 with dissolve
            obo"We are on the same page kid!"
            show boruto normal with dissolve
        "There's no need for that...":
            bo"There's no need for th-"
    with Shake((0, 0, 0, 0), 0.7, dist=20, peak_time=0.7, smoothness=50)
    obo"YOOOOOOOOOOOOORUUUUUUUUUUUUUUUUUUUUUUUUUUUU"
    show yoru shy2 at center with dissolve
    yo"Y-yes... Obo?"
    obo"I thought we had a deal, had we not?"
    yo"Deal? W-what deal..."
    show boss angry3 with vpunch
    obo"Did I not say you could work here so long as you were useful?"
    yo"Y-yes..."
    show boss angry with dissolve
    obo"Then how do you explain getting outperformed by an [bo_age] old child...?"
    show boss angry3 with vpunch
    obo"HUH!?"
    show yoru shy3 with dissolve
    yo"I am s-sorry Obo, I'll try harder..."
    obo"That, you will..."
    obo"But until then, I reckon this is cause for punishment..."
    show boss:
        easein 0.3 xpos 0.90
    $ renpy.sound.play("/audio/soun_fx/intro/spank5instant.opus", channel="sfx3", loop=False, relative_volume = 0.5)
    show yoru at smallshake
    obo"Don't you think!?" with vpunch
    yo"P-punishment...?"
    obo"You see... being useless in my kitchen is a big no-no, It's only natural you make yourself 'useful' in other ways... Right kid?"
    menu:
        obo"You see... being useless in my kitchen is a big no-no, It's only natural you make yourself 'useful' in other ways... Right kid?"
        "W-what!?... Are you asking me?":
            show boruto surprised3 with vpunch
            bo"W-what!? Are you asking me to p-punish Yoru?"
            obo"It's only fitting that you are the one to do it... Don't you think?"
        "I concur!":
            show boruto sceeming with dissolve
            bo"It's only fair..."
            obo"Yoru's punishment is in your hands little twerp!"
    show boss angry2 with dissolve
    show boruto surprised2 with dissolve
    obo"She is to obey your every word, no matter the command."
    yo"O-obo!?"
    obo"The only rules are..."
    obo"No touching allowed. everything else is permitted!"
    show boss laugh with dissolve
    obo"You get a total of three commands kid, don't waste them!"
    yo"O-obo please... He is just a kid!"
    show boss angry2 with vpunch
    obo"And yet he bested you... What does that make you Yoru?"
    show boss angry3 with vpunch
    obo"Huh!?"
    obo"You will obey the twerp's commands..."
    $ renpy.sound.play("/audio/soun_fx/intro/spank5instant.opus", channel="sfx3", loop=False, relative_volume = 0.5)
    show yoru at smallshake
    obo"Or tonight's punishment will be even more severe!" with vpunch
    bot"Obo is insane..."
    obo"Come on kid, show me where your imagination can reach!"
    show boss:
        easein 1 xpos 1.40
    show yoru:
        easein 1 xalign 0.8
    show boruto surprised2 with dissolve
    bo"Uhh... Yoru..."
    default yorudontdoanything1 = False #if boruto tried to save yoru once
    default yorudontdoanything2 = False #if boruto tried to save yoru twice
    $ config.menu_include_disabled = True # show conditional menu choices, set to false at end to hide again
    menu yorucommands:
        bo"Uhh... Yoru..."
        "You don't have to do anything..." if yorudontdoanything1 == False:
            show boruto worried with dissolve
            bo"Yoru... You don't have to do anything. This wasn't what I imagined it to be."
            obo"Kid, You are dissapointing..."
            obo"I'll give you one last chance and trust me when I say... You'll be sparing Yoru from a much worse fate than this!"
            menu:
                obo"I'll give you one last chance and trust me when I say... You'll be sparing Yoru from a much worse fate than this!"
                "Come on Obo. Does she really deserve this?":
                    bo"Come on Obo. Does Yoru really deserve this treatment?"
                    bo"I am sure she is trying her best..."
                    $ yorudontdoanything2 = True
                    yo"[bo_name_stutter]..."
                    show boss angry2 behind yoru:
                        easein 1 xpos 1.1
                    obo"*Sigh*"
                    show yoru shy2 with dissolve
                    obo"You are right kid... She doesn't deserve this."
                    show yoru at smallshake
                    $ renpy.sound.play("/audio/soun_fx/intro/spank5instant.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                    show boss angry3 with vpunch
                    
                    show yoru shy with dissolve
                    obo"She deserves worse!"
                    yo"N-no..."
                    obo"Tonight, I'll be handling that myself since you proved yourself to be a pansy little twerp!"
                    obo"Get back to work, both of you!" with vpunch
                    hide boss with dissolve
                    bo"I am sorry Yoru... I didn't know what to do."
                    show yoru shy2 with dissolve
                    yo"At least you tried kid... T-thank you for that."
                    bo"Is this what you meant last time we talked? About Obo during nights..."
                    show yoru shy3 with dissolve
                    yo"P-please... let's not get into that. I'll be alright, okay?"
                    show yoru normal with dissolve
                    yo"Besides, Obo is nothing compared to my alternative options..."
                    yo"Don't go worrying about me, Come on! Let's get back to work..."
                    hide yoru with dissolve
                    bot"Fuck! This poor girl... there must be a way for her out of this!"
                    show boruto worried2 with dissolve
                    bot"I'll have to see if I can help somehow..."
                    bot"Can I even help given my condition...?"
                    bot"Shit... I'll need to be careful!"
                    hide boruto with dissolve
                    $ config.menu_include_disabled = False
                    $ renpy.end_replay()
                    jump ramenkitchenmenu
                    
                "O-okay then...":
                    
                    show boruto worried2 with dissolve
                    bo"O-okay then..."
                    bo"What sort of commands do I give then..."
                    show boss angry2 with dissolve
                    obo"You should know the answer to that, kid..."
                    $ yorudontdoanything1 = True
                    jump yorucommands
                
            

        "Turn around, I want to see your ass":
            if yorudontdoanything1 == True:
                show boruto worried2 with dissolve
                speech_bubble_bo "O-okay then... I am sorry Yoru but can you turn around and show your bottom?" (300, 300, "righttop")
            else:
                show boruto sceeming2 with dissolve
                speech_bubble_bo"You've seen how I look at you Yoru... You know what I want!"  (300, 300, "righttop")
                show yoru shy with dissolve
                speech_bubble_yo"..." (850, 300, "righttop")
                speech_bubble_bo"Turn around and show me that fat ass of yours!"  (300, 300, "righttop")
            show yoru shy with dissolve
            speech_bubble_yo"M-my... behind?" (850, 300, "righttop")
            obo"Do it!" with vpunch
            speech_bubble_yo "...O-okay" (850, 300, "righttop")
            hide yoru
            show yoruichi assjiggle1 at right:
                zoom 0.36
            with dissolve
            pause 1
            speech_bubble_yo "I-is this e-enough...?" (850, 300, "righttop")
            if yorudontdoanything1 == True:
                show boruto surprised2 with dissolve
                speech_bubble_bo "That's... beautiful..." (300, 300, "righttop")
                bot"Even through her loose long skirt... The outline of her ass is divine!"
                show boruto worried2 with dissolve
            else:
                show boruto sceeming2 with dissolve
                speech_bubble_bo"Such a beautiful sight Yoru..." (300, 300, "righttop")
                call increaselust(10) from _call_increaselust_46
                show boruto sceeming3 with dissolve
                speech_bubble_bo"But nowhere near enough to satisfy my urges!" (300, 300, "righttop")
                show boruto sceeming2 with dissolve
            menu yorustare1:
                "..."
                "Stare":
                    default yorustarecounter = 0
                    show halfblack with dissolve
                    hide yoruichi
                    show yoruichi assjiggle1 at right with dissolve:
                        zoom 0.5
                    if yorustarecounter == 0:
                        bot"What an incredible sight..."
                    else:
                        bot"I could stare all day..."
                    pause 1
                    hide halfblack with dissolve
                    show yoruichi assjiggle1 with dissolve:
                        zoom 0.36
                    if yorustarecounter == 0:
                        speech_bubble_yo"P-please... Stop staring" (850, 300, "righttop")
                    elif yorustarecounter == 1:
                        speech_bubble_yo"This is... embarassing." (850, 300, "righttop")
                    elif yorustarecounter == 2:
                        speech_bubble_yo"S-stop it, please!" (850, 300, "righttop")
                        obo"Get a grip kid!"
                    else:
                        speech_bubble_yo"H-humiliating..." (850, 300, "righttop")
                        obo"That's enough staring, move on with the 2nd command!" with vpunch
                        jump secondcommand
                    $ yorustarecounter += 1
                    jump yorustare1
                "Proceed with 2nd command...":
                    hide halfblack with dissolve
                    show yoruichi assjiggle1 with dissolve:
                        zoom 0.36
                    pass
            label secondcommand:
            speech_bubble_bo "Next, I want you to..." (300, 300, "righttop")
            menu:
                speech_bubble_bo"Next, I want you to..." (300, 300, "righttop")
                "Make your ass jiggle!":
                    if yorudontdoanything1 == True:
                        show boruto surprised2 with dissolve
                        speech_bubble_bo"Can you uuuh... make it jiggle a little bit?"  (300, 300, "righttop")
                    else:
                        show boruto sceeming2 with dissolve
                        speech_bubble_bo"Make that fat ass jiggle for me!"  (300, 300, "righttop")
                    speech_bubble_yo"J-jiggle!?" (850, 300, "righttop")
                    obo"You heard the boy!" with vpunch
                    show yoruassjiggleanim at right with dissolve
                    hide yoru ass
                    default yorustarecounterjiggle = 0
                    label repeatjiggle:
                    pause 2
                    speech_bubble_yo"L-Like... this...?" (850, 300, "righttop")
                    pause 1
                    if yorudontdoanything1 == True:
                        speech_bubble_bo"B-beautiful..." (300, 300, "righttop")
                    else:
                        speech_bubble_bo"Now that's an ass worth dying for!" (300, 300, "righttop")
                    speech_bubble_yo"..." (850, 300, "righttop")
                    menu jigglingmenu:
                        speech_bubble_yo"..."
                        "Keep it jiggling until I say stop!" if yorustarecounterjiggle <=2:
                            if yorudontdoanything1 == True:
                                speech_bubble_bo"I c-cant help but watch..." (300, 300, "righttop")
                                speech_bubble_yo"H-how much longer... This is embarrasing." (850, 300, "righttop")
                            else:
                                speech_bubble_bo"I could watch you do that all day..." (300, 300, "righttop")
                                speech_bubble_bo"Keep that going until I say stop!" (300, 300, "righttop")
                                speech_bubble_yo"..." (850, 300, "righttop")


                            menu yorustarejiggle:
                                "..."
                                "Stare":
                                    show halfblack with dissolve
                                    hide yoruassjiggleanim
                                    hide yoruichi
                                    show yoruassjiggleanim at right with dissolve:
                                        zoom 1.5
                                    if yorustarecounterjiggle == 0:
                                        bot"Fuck me... that ass is mesmerizing!"
                                    else:
                                        bot"I could watch her play with her ass forever..."
                                    pause 1
                                    hide halfblack with dissolve
                                    show yoruassjiggleanim at right with dissolve:
                                        zoom 1.0
                                    if yorustarecounterjiggle == 0:
                                        speech_bubble_yo"P-please... this is w-weird!" (850, 300, "righttop")
                                    elif yorustarecounterjiggle == 1:
                                        speech_bubble_yo"W-why do I have to do this for a kid?" (850, 300, "righttop")
                                    elif yorustarecounterjiggle == 2:
                                        speech_bubble_yo"So e-embarassing..." (850, 300, "righttop")
                                        obo"Kid... you are salivating!"
                                    else:
                                        speech_bubble_yo"..." (850, 300, "righttop")
                                        obo"That's enough jiggling! Pick your jaw off of the floor and move to your final command kid!" with vpunch
                                        jump jigglingmenu
                                    $ yorustarecounterjiggle += 1
                                    jump yorustarejiggle
                                "Proceed with final command...":
                                    hide halfblack
                                    hide yoruassjiggleanim
                                    show yoruichi assjiggle1 at right with dissolve:
                                        zoom 0.36
                                    jump endingafterjiggle 
                        "That's enough. Next I want you to raise your skirt!":
                            label endingafterjiggle:
                            hide yoruassjiggleanim
                            show yoruichi assjiggle1 at right:
                                zoom 0.36
                            with dissolve
                            speech_bubble_bo"You can stop now..." (300, 300, "righttop")
                            label commandafterjiggle:
                            if yorudontdoanything1 == True:
                                speech_bubble_bo"Now raise your skirt up a little bit..." (300, 300, "righttop")
                            else:
                                speech_bubble_bo"Next, I want you to raise that skirt up for me!" (300, 300, "righttop")
                            hide yoruichi
                            show yoru ass2 at right with dissolve:
                                zoom 0.36
                            show boruto surprised3 with dissolve
                            call increaselust(10) from _call_increaselust_47
                            pause 4
                            speech_bubble_yo"..." (850, 300, "righttop")
                            speech_bubble_yo"I can't show a-any more... You are just a k-kid!" (850, 300, "righttop")
                            show boss angry3 behind yoru:
                                easein 0.5 xalign 0.9
                            pause 0.3
                            scene black with vpunch
                            $ renpy.sound.play("/audio/soun_fx/intro/spank5instant.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                            pause 0.5
                            obo"You won't have to Yoru! That was your third command kid..."
                            show ramenkitchen
                            show boruto normal at left
                            show yoru shy at center:
                                xalign 0.7
                            show boss angry2 behind yoru at right:
                                xpos 1.1
                            with dissolve 
                            show yoru shy2 with dissolve:
                                zoom 1.0
                                
                            obo"Haven't even managed to see any skin... you fucked this one up, didn't you little twerp!"
                            show boss laugh with dissolve
                            obo"Haa-ha-haa!"
                            if yorudontdoanything1 == True:
                                speech_bubble_bo"..."
                                show boruto worried with dissolve
                                bot"Obo seems to enjoy humiliating Yoru..."
                                show boruto angry with dissolve
                                bot"Piece of shit..."
                            else:
                                show boruto snob with dissolve
                                speech_bubble_bo"Still had some fun!"
                            jump threecommandsending
                            

                        

                "Raise your skirt!":
                    if yorudontdoanything1 == True:
                        speech_bubble_bo"Raise your skirt up a little bit..." (300, 300, "righttop")
                    else:
                        speech_bubble_bo"Raise that skirt up for me!" (300, 300, "righttop")
                    hide yoruichi
                    show yoru ass2 at right:
                        zoom 0.36
                    show boruto surprised3
                    with dissolve
                    call increaselust(10) from _call_increaselust_48
                    pause 4
                    speech_bubble_yo"..." (850, 300, "righttop")
                    speech_bubble_yo"I can't show a-any more... You are just a k-kid!" (850, 300, "righttop")

                    menu yorustare2:
                        "..."
                        "Stare":
                            default yorustarecounter2 = 0
                            show halfblack with dissolve
                            hide yoru
                            show yoru ass2 at right with dissolve:
                                zoom 0.5
                            if yorustarecounter2 == 0:
                                bot"Her legs... They are so toned, and sexy..."
                            elif yorustarecounter2 == 1:
                                bot"Fuck me! She is amazing. You can tell she is putting in work to maintain a physique like that in her fourties..."
                            else:
                                bot"She is so fucking hot..."
                            pause 1
                            hide halfblack with dissolve
                            show yoru ass2 with dissolve:
                                zoom 0.36
                            if yorustarecounter2 == 0:
                                speech_bubble_yo"W-why are you s-staring like that..." (850, 300, "righttop")
                            elif yorustarecounter2 == 1:
                                speech_bubble_yo"To think I h-have to do this for a kid..." (850, 300, "righttop")
                            elif yorustarecounter2 == 2:
                                speech_bubble_yo"I'm a-ashamed of myself..." (850, 300, "righttop")
                                speech_bubble_bo"Don't be, you are stunning!" (300, 300, "righttop")
                                obo"Don't stare too long kid! Heh!"
                            else:
                                speech_bubble_yo"..." (850, 300, "righttop")
                                obo"That's enough! Move on to your final command kid..." with vpunch
                                jump assfinalcommand
                            $ yorustarecounter2 += 1
                            jump yorustare2
                        "Proceed with the final command...":
                            hide halfblack with dissolve
                            show yoru ass2 with dissolve:
                                zoom 0.36
                            pass
                    label assfinalcommand:
                    obo"One command left kid..." 
                    menu:
                        obo"One command left kid..."
                        "Expose your bare ass!":
                            if yorudontdoanything1 == True:
                                show boruto worried2 with dissolve
                                bot"I must admit that I am at the very least... curious."
                                speech_bubble_bo"Can you r-raise your skirt all the way up?" (300, 300, "righttop")
                            else:
                                show boruto sceeming3 with dissolve
                                speech_bubble_bo"It's time you expose your bare ass for all to see!" (300, 300, "righttop")
                                show boruto sceeming2 with dissolve
                            show yoru ass2 with dissolve:
                                xzoom -1
                            speech_bubble_yo"O-obo...? D-do I have to...? P-please..." (850, 300, "righttop")
                            obo"Don't look at me Yoru! The kid has spoken..." 
                            show yoru ass2 with dissolve:
                                xzoom 1
                            speech_bubble_yo"D-dont... stare..." (850, 300, "righttop")
                            show yoru ass3 with dissolve:
                                zoom 0.36
                            pause 1
                            show boruto surprised3 with dissolve
                            call increaselust(10) from _call_increaselust_49
                            pause 1
                            if yorudontdoanything1 == True:
                                bot"...!" with vpunch
                                bot"Yoru's got an ass of a goddess!"
                                obo"Pick your jaw up from the floor kid..."
                                show boss angry3 behind yoru:
                                    linear 0.4 xalign 0.9
                                pause 0.35
                                scene black with vpunch
                                $ renpy.sound.play("/audio/soun_fx/intro/spank5instant.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                obo"My little whore left you stunned... Didn't she?"

                            else:
                                with vpunch
                                speech_bubble_bo"Holy s-shit!"(300, 300, "righttop")
                                
                                speech_bubble_bo"Your ass is majestic Yoru..." (300, 300, "righttop")
                                show boruto sceeming2 with dissolve
                                speech_bubble_bo"To think that a mature forty year old lady like you though wears a slutty thong in the kitchen..." (300, 300, "righttop")
                                speech_bubble_bo"You are one foxy cougar... aren't you?" (300, 300, "righttop")
                                obo"Say it the way it should be said kid..."
                                show boss angry3 behind yoru:
                                    linear 0.5 xalign 0.9
                                pause 0.4
                                scene black with vpunch
                                $ renpy.sound.play("/audio/soun_fx/intro/spank5instant.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                obo"A whore! Is what she is..."
                                obo"But that was your third command kid."
                            jump threecommandsending






                        "Bend over for me!":
                            if yorudontdoanything1 == True:
                                show boruto worried2 with dissolve
                                bot"I know I shouldn't be treating her like this..."
                                bot"But she is just so hot!"
                                speech_bubble_bo"Can you lean forwards a little bit more?" (300, 300, "righttop")
                            else:
                                show boruto sceeming2 with dissolve 
                                speech_bubble_bo"Just a kid you say, Yoru...?" (300, 300, "righttop")
                                speech_bubble_yo"..." (850, 300, "righttop")
                                show boruto sceeming3 with dissolve
                                speech_bubble_bo"Then why don't you bend over for me and make that ass stick out!" (300, 300, "righttop")
                            speech_bubble_yo"D-do I have to...?" (850, 300, "righttop")
                            if yorudontdoanything1 == True:
                                obo"Yoru!" with vpunch
                            else:
                                call changeHatred(1,"none") from _call_changeHatred_53
                                call borutoevil2 from _call_borutoevil2_6
                                show boruto sceeming4 with dissolve
                                speech_bubble_bo"Do it... Bitch!" (300, 300, "righttop")
                                speech_bubble_yo"Y-you... don't have to be v-vulglar." (850, 300, "righttop")
                            speech_bubble_yo"..." (850, 300, "righttop")
                            show yoru ass2_1 with dissolve:
                                zoom 0.36
                            show boruto surprised3 with dissolve
                            call increaselust(10) from _call_increaselust_50
                            pause 4
                            speech_bubble_bo"Such an unbelievable ass on you... Are you really in your fourties?" (300, 300, "righttop")
                            speech_bubble_yo"P-please... This is embarassing!" (850, 300, "righttop")
                            show boss angry3 behind yoru:
                                easein 0.5 xalign 0.9
                            pause 0.3
                            scene black with vpunch
                            $ renpy.sound.play("/audio/soun_fx/intro/spank5instant.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                            obo"As it should have been! That was your third command kid..."
                            pause 0.5
                            show ramenkitchen
                            show boruto normal at left
                            show yoru shy at center:
                                xalign 0.7
                            show boss angry2 behind yoru at right:
                                xpos 1.1
                            with dissolve 
                            show yoru shy2 with dissolve:
                                zoom 1.0
                                
                            obo"Haven't even managed to see any skin... you fucked this one up, didn't you little twerp!"
                            show boss laugh with dissolve
                            obo"Haa-ha-haa!"
                            if yorudontdoanything1 == True:
                                bo"..."
                                show boruto worried with dissolve
                                bot"Obo seems to enjoy humiliating Yoru..."
                                show boruto angry with dissolve
                                bot"Piece of shit..."
                            else:
                                show boruto snob with dissolve
                                bo"Still had some fun!"
                            jump threecommandsending

                        

                
                
            
        "Lower that apron of yours, I want to see your tits":
            if yorudontdoanything1 == True:
                show boruto worried with dissolve
                bo"O-okay then..."
                bo"Sorry Yoru but... can you lower your apron and expose your chest?"
                show yoru shy with dissolve
            else:
                show boruto sceeming with dissolve
                bo"I've been staring at your tits every single day since I started working alongside you Yoru!"
                show boruto sceeming2 with dissolve
                show yoru shy with dissolve
                bo"Lower that apron and expose your tits!"

            yo"My... c-chest?"
            obo"You heard the kid, do it!" with vpunch
            show yoru tits1 at right with dissolve:
                zoom 0.4 pos (0.98, 1.05)  


            yo"Is this good e-enough?"
            if yorudontdoanything1 == True:
                show boruto surprised2 with dissolve
                bo "..."
                bot"As much as I don't enjoy doing this to her, I can't deny the fact that she is... gifted."
                bot"I want to see more..."
                show boruto worried2 with dissolve
            else:
                show boruto sceeming2 with dissolve
                bo"Now that's a sexy rack..."
                call increaselust(10) from _call_increaselust_51
                show boruto sceeming3 with dissolve
                bo"Your shirt can barely contain your tits! Maybe we should mend that..."
                yo"W-what are you saying, kid!?"
                show boruto sceeming2 with dissolve
                obo"One step at a time kid..."
            obo"Move on with your second command twerp!"
            bo"How about you..."
            default yoru_tits_extracommand = False
            default yoru_tits_showthemofffinal = False
            menu:
                bo"How about you..."
                "Lower your shirt":
                    if yorudontdoanything1 == True:
                        show boruto surprised2 with dissolve
                        bo"Can you uuuh... lower your shirt?" 
                    else:
                        show boruto sceeming2 with dissolve
                        bo"Come on, you know what to do next... Start getting rid of that shirt!"
                    yo"M-my shirt?"
                    obo"Do as the boy says!" with vpunch
                    yo"...D-damn it!"
                    yo"I can't believe I h-have to do this in front of a kid..."
                    if yorudontdoanything1 == True:
                        show boruto worried2 with dissolve
                        bo"I am an adult... you know"
                        yo"Still a kid to me..." 
                        show yoru tits2_1 at right with dissolve:
                            zoom 0.4
                        yo"T-there... happy now?"
                        bot"Beautiful. But..."
                        bot"Not exactly what I asked for... shall I push her to lower her shirt all the way?"
                        menu:
                            bot"Not exactly what I asked for... shall I push her to lower her shirt all the way?"
                            "{color=[hatredcolor]}That is not what I asked for, Yoru...{/color}":
                                bot"Fuck it! I am tired of playing the nice guy anyway!"
                                show boruto sceeming3 with dissolve
                                call borutoevil2 from _call_borutoevil2_7
                                call changeHatred(1,"none") from _call_changeHatred_54
                                bo"Yoru, that's...."
                                yo"W-what's with the weird look on your face!?"
                                $ yorudontdoanything1 = False
                                jump isaidgetridofit
                            "I will allow it...":
                                bo"Not exactly what I ordered, but I will allow it."
                                yo"..."
                                obo"That's a command wasted kid..."
                                
                                obo"Move on to the last one then"
                                bo"O-okay... So uhh"
                                menu:
                                    bo"O-okay... So uhh"
                                    "Remove your shirt but...":
                                        show boruto worried with dissolve
                                        bo"Can you... r-remove your shirt next?"
                                        show yoru tits4_tsk with dissolve
                                        yo"M-my shirt?"
                                        show yoru tits4_1 with dissolve
                                        show yoru at smallshake
                                        yo"...D-damn it!"
                                        yo"I can't believe I h-have to do this in front of a kid..."

                                        show boruto worried2 with dissolve
                                        bo"You can c-cover your breasts with your hands if you'd like..."
                                        show boruto suspicious with dissolve
                                        show yoru tits2_0 at right with dissolve:
                                            zoom 0.4
                                        yo"That... doesn't make it any e-easier!"
                                        obo"I am getting tired of this wishy-washy shit. Move on now!" with vpunch
                                        yo"C-come on Obo... do I really have to?"
                                        obo"Don't look at me, the kid has spoken!"
                                        show yoru tits2_2 at right with dissolve:
                                            zoom 0.37
                                        yo"I r-really hope you aren't enjoying t-this kid..."
                                        menu:
                                            yo"I r-really hope you aren't enjoying t-this kid..."
                                            "I am not":
                                                bo"I am not"
                                                yo"Doesn't s-seem like it to me!"
                                                bot"She sees right through me..."
                                            "I am not but... you are just so beautiful!":
                                                bo"I am not, but..."
                                                bo"I can't deny that your beauty is having an effect on me..."
                                        show yoru tits4_1 at right with dissolve:
                                            zoom 0.4
                                        yo"Just... d-don't stare!"
                                        show yoru at smallshake
                                        yo"*Tsk*..."
                                        show yoru tits5 at right with dissolve:
                                            zoom 0.4
                                        yo"..."
                                        show yoru tits5_1 at right with Dissolve(1):
                                            zoom 0.37
                                        yo"T-there... h-happy now?"
                                        bo"..."
                                        bo"That should be enough... right Obo?"
                                        show yoru tits5_2 at right with Dissolve(1):
                                            zoom 0.37
                                        yo "{size=14}Thanks for t-trying kid...{/size}"
                                        show boruto surprised3 with dissolve
                                        with vpunch
                                        "Yoru in a slightly less sheltered stance, quitely mouths off her thanks to you so that Obo doesn't take notice of it."


                                        show boss angry3 behind yoru:
                                            easein 0.5 xalign 0.9
                                        pause 0.3
                                        scene black with vpunch
                                        $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                        pause 0.5
                                        obo"That's enough!"
                                        obo"Go get dressed!" with vpunch
                                        $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                                        "..."
                                        show ramenkitchen
                                        show boruto normal at left
                                        show yoru shy at center:
                                            xalign 0.7
                                        show boss angry2 behind yoru at right:
                                            xpos 1.1
                                        with dissolve 
                                        show yoru shy2 with dissolve:
                                            zoom 1.0
                                            
                                        obo"You could do much better than that kid..."
                                        show boss laugh with dissolve
                                        obo"Haa-ha-haa!"
                                        if yorudontdoanything1 == True:
                                            bo"..."
                                            show boruto worried with dissolve
                                            bot"Obo seems to enjoy humiliating Yoru..."
                                            show boruto angry with dissolve
                                            bot"Piece of shit..."
                                        else:
                                            show boruto snob with dissolve
                                            bo"Still had some fun!"
                                        jump threecommandsending


                                    "Show them off a little bit":
                                        bot"I should take it easy on her..."
                                        $ yoru_tits_showthemofffinal = True
                                        jump showthemoffalittlebit
                                    
                            
                        
                    else:
                        show boruto sceeming3 with dissolve
                        bo"I am an adult bitch! Now do as I say!"
                        show boruto sceeming2 with dissolve
                        yo"Y-you... don't have to be v-vulglar."
                        obo"Heh! Nice one kid!"
                        show yoru tits2_1 at right with dissolve:
                            zoom 0.4
                        yo"T-there... happy now?"
                        label isaidgetridofit:
                        bo"No fair... I said to get rid of it, didn't I?"
                        show yoru tits2_0 at right with dissolve:
                            zoom 0.4
                        yo"W-what!? O-obo please... He is just a kid!"
                        obo"This one is on you twerp!"
                        bo"I said..."
                        show boruto sceeming3 with dissolve
                        bo"Get RID OF IT!" with vpunch
                        show yoru tits2_2 at right with dissolve:
                            zoom 0.4
                        yo"N-no..."
                        bo"...Obo? What are the rules again?"
                        show yoru tits4_tsk at right with dissolve:
                            zoom 0.4
                        obo"She obeys your every command kid!"
                        obo"I would say I don't make the rules..."
                        obo"But I do!" with vpunch
                        obo"Undress! Yoru..." with vpunch
                        show yoru tits4_1 at right with dissolve:
                            zoom 0.4
                        show yoru at smallshake
                        yo"*Tsk*..."
                        show yoru tits5 at right with dissolve:
                            zoom 0.4
                        yo"Y-you are both... d-depraved perverts!"
                        show yoru tits5_0 at right with dissolve:
                            zoom 0.4
                        yo"T-there... h-happy now?"
                        bo"Happy? Don't I have one last command, old man?"
                        obo"That you do kid! Move on with it!"
                        jump yorutitsfinalcommand


                        



                "Show them off a little bit":
                    $ yoru_tits_extracommand = True
                    if yorudontdoanything1 == True:
                        show boruto surprised2 with dissolve
                        label showthemoffalittlebit:
                        bo"Can you maybe show them off a little bit?"
                        yo"S-show them off? H-how..."
                        menu:
                            yo"S-show them off? H-how..."
                            "Squeeze them with your elbows":
                                label asjdhaskjkjasd:
                                    bo"You could... s-squeeze them with your elbows."
                                    yo"L-like..." 
                                    show yoru tits3_2 at right with dissolve:
                                        zoom 0.4
                                    yo"...this?"
                                    show boruto suspicious with dissolve
                                    bo"Good girl..."
                                    yo"H-huh?"
                                    show boruto surprised2 with vpunch
                                    bo"I m-mean yes! Like that! You did good, girl!"
                                    yo"So embarassing..."
                                    bot"Fuck... that slipped out! I am enjoying this a bit too much..."
                                    show boruto worried2 with dissolve
                                    bo"Can you also trying pushing your chest out and upwards?"
                                    yo"..."
                                    show yoru tits3_1 at right with dissolve:
                                        zoom 0.37 pos (0.98, 1.05) 
                                    yo"Is t-this... what you wanted?"
                                    bot"She is so sexy when she's following my every word..."
                                    bot"Shall I put that to the test...?"
                                    menu shalliputthattothetest:
                                        bot"Shall I put that to the test...?"
                                        "Now repeat both movements until I say stop":
                                            bot"I just can't resist the feeling of her obeying me..."
                                            show boruto sceeming with dissolve
                                            bo"Now keep repeating both of those movements until I tell you to stop..."
                                            yo"W-what?" with vpunch
                                            yo"Aren't you enjoying t-this a little too much kid?"
                                            obo"Do as he says Yoru!" with vpunch
                                            yo"..."
                                            hide yoru
                                            show yoru_showofftitsanim
                                            with dissolve
                                            yo"T-this is... h-humiliating!"
                                            bo"..."
                                            bot"Fuck me... Yoru's so hot!"
                                            menu yoru_showofftitsanim:
                                                bot"Fuck me... Yoru's so hot!"
                                                "Stare":
                                                    default yorustaretits = 0
                                                    show halfblack with dissolve
                                                    hide yoru_showofftitsanim
                                                    hide yoru
                                                    show yoru_showofftitsanim at right with dissolve:
                                                        zoom 1.3
                                                    show boruto surprised2 with dissolve
                                                    if yorustaretits == 0:
                                                        bot"I can't believe she is 40 years old. Her body is amazing for her age..."
                                                    else:
                                                        bot"I could watch her move her tits around all day..."
                                                    pause 1
                                                    hide halfblack with dissolve
                                                    show yoru_showofftitsanim at right with dissolve:
                                                        zoom 1.0
                                                    if yorustaretits == 0:
                                                        yo"P-please... this is w-weird!"
                                                    elif yorustaretits == 1:
                                                        yo"W-why do I have to do this for a kid?"
                                                    elif yorustaretits == 2:
                                                        yo"So e-embarassing..." 
                                                        obo"Kid... you are salivating!"
                                                    else:
                                                        yo"..." 
                                                        obo"That's enough! Pick your jaw off of the floor and move on kid!" with vpunch
                                                        if yoru_tits_showthemofffinal == True:
                                                            jump yorutitsending
                                                        else:
                                                            jump youcanstopnow
                                                    $ yorustaretits += 1
                                                    jump yoru_showofftitsanim
                                                "You can stop now":
                                                    label youcanstopnow:
                                                    show boruto worried2 with dissolve
                                                    bo"Ok then, you can stop posing..."
                                                    hide yoru_showofftitsanim
                                                    show yoru tits4_1 at right with dissolve:
                                                        zoom 0.4
                                                    yo"H-how much more do I have to endure..."
                                                    if yoru_tits_showthemofffinal == True:
                                                            jump yorutitsending
                                                    label lasttitscommandgood:
                                                    bot"My last command... She must know what's coming."
                                                    bo"How about you..."
                                                    menu:
                                                        bo"How about you..."
                                                        "Remove your shirt...":
                                                            pass
                                                        
                                                    show boruto worried with dissolve
                                                    bo"Sorry Yoru but... It's time you remove your shirt."
                                                    show yoru tits4_tsk with dissolve
                                                    yo"M-my shirt?"
                                                    obo"Do as the boy says!" with vpunch
                                                    show yoru tits4_1 with dissolve
                                                    show yoru at smallshake
                                                    yo"...D-damn it!"
                                                    yo"I can't believe I h-have to do this in front of a kid..."

                                                    show boruto worried2 with dissolve
                                                    bo"You keep saying I am a kid... I am an adult you know, I've seen tits before."
                                                    show yoru tits4_tsk with dissolve
                                                    yo"*Tsk*... You are still a kid to me!"
                                                    show yoru tits2_0 at right with dissolve:
                                                        zoom 0.4
                                                    yo"T-there... happy now?"
                                                    obo"The kid said to remove it, didn't he Yoru?"
                                                    show yoru tits2_1 at right with dissolve:
                                                        zoom 0.4
                                                    yo"W-what!? O-obo please... He is just a kid!"
                                                    obo"This one is on you twerp!"
                                                    bo"It'll be over after this Yoru..."
                                                    show yoru at smallshake
                                                    yo"D-damn it!"
                                                    show yoru tits2_2 at right with dissolve:
                                                        zoom 0.37
                                                    yo"I am not whoring myself out in front of a kid..."
                                                    obo"I would say I don't make the rules..."
                                                    show yoru tits4_tsk at right with dissolve:
                                                        zoom 0.4
                                                    obo"But I do!" with vpunch
                                                    obo"Undress! Yoru..." with vpunch
                                                    show yoru tits4_1 at right with dissolve:
                                                        zoom 0.4
                                                    show yoru at smallshake
                                                    yo"*Tsk*..."
                                                    show yoru tits5 at right with dissolve:
                                                        zoom 0.4
                                                    yo"Y-you are both... d-depraved perverts!"
                                                    bot"Can't deny that..."
                                                    show yoru tits5_1 at right with Dissolve(1):
                                                        zoom 0.37
                                                    yo"T-there... h-happy now?"
                                                    show yoru tits5_0 with dissolve
                                                    yo"I can't s-show anymore...-"
                                                    show boss angry3 behind yoru:
                                                        easein 0.5 xalign 0.9
                                                    pause 0.3
                                                    scene black with vpunch
                                                    $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                                    pause 0.5
                                                    obo"You won't have to Yoru! That was your third command kid..."
                                                    obo"Go get dressed!" with vpunch
                                                    $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                                                    "..."
                                                    pause 0.5
                                                    show ramenkitchen
                                                    show boruto normal at left
                                                    show yoru shy at center:
                                                        xalign 0.7
                                                    show boss angry2 behind yoru at right:
                                                        xpos 1.1
                                                    with dissolve 
                                                    show yoru shy2 with dissolve:
                                                        zoom 1.0
                                                        
                                                    obo"Haven't even managed to see any skin... you fucked this one up, didn't you little twerp!"
                                                    show boss laugh with dissolve
                                                    obo"Haa-ha-haa!"
                                                    if yorudontdoanything1 == True:
                                                        bo"..."
                                                        show boruto worried with dissolve
                                                        bot"Obo seems to enjoy humiliating Yoru..."
                                                        show boruto angry with dissolve
                                                        bot"Piece of shit..."
                                                    else:
                                                        show boruto snob with dissolve
                                                        bo"Still had some fun!"
                                                    jump threecommandsending
                                                    


                                                
                                        "I shouldn't":
                                            bot"Nah, that might be too embarassing for her..."
                                            # if yoru_tits_showthemofffinal == True:
                                            jump youcanstopnow

                                        
                                    


                            "Push your chest out and upwards":
                                bo"You could... p-push them out and upwards? You know... hold your chest up high."
                                yo"L-Like..." 
                                show yoru tits3_1 at right with dissolve:
                                    zoom 0.37
                                yo"...this?"
                                show boruto suspicious with dissolve
                                bo"Good girl..."
                                yo"H-huh?"
                                show boruto surprised2 with vpunch
                                bo"I m-mean yes! Like that... You did good, girl!"
                                yo"...so embarassing"
                                bot"Fuck... that slipped out! I am enjoying this a bit too much..."
                                show boruto worried2 with dissolve
                                bo"Can you also trying squeezing them together with your elbows?"
                                yo"..."
                                show yoru tits3_2 at right with dissolve:
                                    zoom 0.4
                                bo"Is t-this... what you wanted?"
                                bot"She is so sexy when she's following my every word..."
                                bot"Shall I put that to the test...?"
                                jump shalliputthattothetest

                             
                    else:
                        show boruto sceeming2 with dissolve
                        bo"Would be a shame to not show off a rack like that!"
                        bo"Come on girl, put them on display!"
                        yo"P-put them on d-display!? ...How?" with vpunch
                        menu:
                            yo"P-put them on d-display!? ...How?"
                            "Squeeze them with your elbows":
                                label jhskdfhsjkdhfksj:
                                    bo"You could squeeze those tits with your elbows for starters..."
                                    yo"L-Like..." 
                                    show yoru tits3_2 at right with dissolve:
                                        zoom 0.39 ypos 1.02
                                    yo"...this?"
                                    show boruto sceeming with dissolve
                                    bo"Good girl..."
                                    yo"Can you... not t-talk like that?"
                                    show boruto sceeming3 with dissolve 
                                    bo"I'll talk to you however I damn please!" with vpunch
                                    yo"..."
                                    show boruto sceeming2 with dissolve
                                    bo"You are not done yet, bitch!"
                                    show yoru at smallshake
                                    yo"H-hey!"
                                    show boruto sceeming with dissolve
                                    bo"Now push your shoulders back and your rack out..."
                                    bo"Just like a whore proud of her tits would!"
                                    yo"...O-obo?"
                                    obo"What are you looking at me for!?... You proud whore!?" with vpunch
                                    obo"Haa-haa-ha! The kid has style!"
                                    obo"Do as he says!" with vpunch
                                    yo"..."
                                    show yoru tits3_1 at right with Dissolve(1):
                                        zoom 0.37 ypos 1.02 xpos 0.97
                                    yo"Ugh... Y-you perverts!"
                                    yo"Will this... be all t-then?"
                                    show boruto sceeming2 with dissolve
                                    bo"No it won't! In fact, I enjoyed your little posing a little bit too much..."
                                    bo"How about you keep repeating both poses until I tell you to stop!"
                                    yo"W-what!? T-that's embarassing..."
                                    bo"Start moving and don't stop until I tell you to!"
                                    hide yoru
                                    show yoru_showofftitsanim
                                    with dissolve
                                    yo"T-this is... h-humiliating!"
                                    bo"..."
                                    bo"That's it... Keep moving!"
                                    menu yoru_posing:
                                        bo"That's it... Keep moving!"
                                        "Stare":
                                            default yorustaretitsevil = 0
                                            show halfblack with dissolve
                                            hide yoru_showofftitsanim
                                            hide yoru
                                            show yoru_showofftitsanim at right with dissolve:
                                                zoom 1.3
                                            if yorustaretitsevil == 0:
                                                bot"I can't believe this bitch is 40 years old. Her body is practically perfect!"
                                            else:
                                                bot"I could watch her shake her rack forever..."
                                            pause 1
                                            hide halfblack with dissolve
                                            show yoru_showofftitsanim at right with dissolve:
                                                zoom 1.0
                                            if yorustaretitsevil == 0:
                                                yo"C-can I stop yet?"
                                            elif yorustaretitsevil == 1:
                                                yo"W-why do I have to h-humiliate myself like this?"
                                            elif yorustaretitsevil == 2:
                                                yo"P-please... no more!"
                                                obo"Kid... you are salivating!"
                                            else:
                                                yo"..."
                                                obo"That's enough! Pick your jaw off of the floor and move on kid!" with vpunch
                                                if yoru_tits_showthemofffinal == True:
                                                    jump yorutitsending
                                                else:
                                                    jump youcanstopnowevil
                                            $ yorustaretitsevil += 1
                                            jump yoru_posing
                                        "You can stop now":
                                            label youcanstopnowevil:
                                            bo"You've paraded your tits around enough, let's move on!"
                                            hide yoru_showofftitsanim
                                            show yoru tits4_1 at right with dissolve:
                                                zoom 0.4
                                            yo"H-how much more do I have to endure..."
                                            if yoru_tits_showthemofffinal == True:
                                                    jump yorutitsending

                                            bo"How about you..."
                                            menu:
                                                bo"How about you..."
                                                "Remove your shirt!":
                                                    pass
                                             
                                            show boruto sceeming2 with dissolve
                                            bo"Come on, you know what to do next... Start getting rid of that shirt!"
                                            show yoru tits4_tsk with dissolve
                                            yo"M-my shirt?"
                                            obo"Do as the boy says!" with vpunch
                                            show yoru tits4_1 with dissolve
                                            show yoru at smallshake
                                            yo"...D-damn it!"
                                            yo"I can't believe I h-have to do this in front of a kid..."

                                            show boruto sceeming3 with dissolve
                                            bo"I am an adult bitch! Now do as I say!"
                                            show boruto sceeming2 with dissolve
                                            show yoru tits4_tsk with dissolve
                                            yo"Y-you... don't have to be v-vulglar."
                                            obo"Heh! Nice one kid!"
                                            show yoru tits2_0 at right with dissolve:
                                                zoom 0.4
                                            yo"T-there... happy now?"
                                            bo"No fair... I said to get rid of it, didn't I?"
                                            show yoru tits2_1 at right with dissolve:
                                                zoom 0.4
                                            yo"W-what!? O-obo please... He is just a kid!"
                                            obo"This one is on you twerp!"
                                            bo"I said..."
                                            show boruto sceeming3 with dissolve
                                            bo"Get RID OF IT!" with vpunch
                                            show yoru tits2_2 at right with dissolve:
                                                zoom 0.37
                                            yo"N-no..."
                                            bo"...Obo? What are the rules again?"
                                            show yoru tits4_tsk at right with dissolve:
                                                zoom 0.4
                                            obo"She obeys your every command kid!"
                                            obo"I would say I don't make the rules..."
                                            obo"But I do!" with vpunch
                                            obo"Undress! Yoru..." with vpunch
                                            show yoru tits4_1 at right with dissolve:
                                                zoom 0.4
                                            show yoru at smallshake
                                            yo"*Tsk*..."
                                            show yoru tits5 at right with dissolve:
                                                zoom 0.4
                                            yo"Y-you are both... d-depraved perverts!"
                                            show yoru tits5_1 at right with Dissolve(1):
                                                zoom 0.37
                                            yo"T-there... h-happy now?"
                                            bo"Come on! What's the point if you hide the goods with your hands?"
                                            show yoru tits5_0 with dissolve
                                            yo"I can't s-show you my...-"
                                            show boss angry3 behind yoru:
                                                easein 0.5 xalign 0.9
                                            pause 0.3
                                            scene black with vpunch
                                            $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                            pause 0.5
                                            obo"You won't have to Yoru! That was your third command kid..."
                                            obo"Go get dressed!" with vpunch
                                            $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                                            "..."
                                            show ramenkitchen
                                            show boruto normal at left
                                            show yoru shy at center:
                                                xalign 0.7
                                            show boss angry2 behind yoru at right:
                                                xpos 1.1
                                            with dissolve 
                                            show yoru shy2 with dissolve:
                                                zoom 1.0
                                                
                                            obo"Haven't even managed to see a tiddie... you fucked this one up, didn't you little twerp!"
                                            show boss laugh with dissolve
                                            obo"Haa-ha-haa!"
                                            if yorudontdoanything1 == True:
                                                bo"..."
                                                show boruto worried with dissolve
                                                bot"Obo seems to enjoy humiliating Yoru..."
                                                show boruto angry with dissolve
                                                bot"Piece of shit..."
                                            else:
                                                show boruto snob with dissolve
                                                bo"Still had some fun!"
                                            jump threecommandsending
                                            
                          
            label yorutitsending:
                obo"Oh, but I forgot!"
                show boss angry3 behind yoru:
                    easein 0.5 xalign 0.9
                        
                pause 0.3
                scene black with vpunch
                $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                pause 0.5
                obo"That was your final command kid!"
                show ramenkitchen
                show boruto normal at left
                show yoru shy at center:
                    xalign 0.7
                show boss angry2 behind yoru at right:
                    xpos 1.1
                with dissolve 
                show yoru shy2 with dissolve:
                    zoom 1.0
                    
                obo"Haven't even managed to see anything worthwhile... you fucked this one up real good, didn't you little twerp!"
                show boss laugh with dissolve
                obo"Haa-ha-haa!"
                if yorudontdoanything1 == True:
                    bo"..."
                    show boruto worried with dissolve
                    bot"Obo seems to enjoy humiliating Yoru..."
                    show boruto angry with dissolve
                    bot"Piece of shit..."
                else:
                    show boruto snob with dissolve
                    bo"Still had some fun!"
                jump threecommandsending


            label secondorlasttits:
                yo"..."
                bo"Next, I want you to..."
                menu:
                    bo"Next, I want you to..."
                    "Choice 1":
                        "fill"
                    "Choice 2":
                        "fill"
                    







                if yoru_tits_extracommand == True:
                    obo"That was your final command!"


                    jump threecommandsending
                else:
                    jump yorutitsfinalcommand
            
            label yorutitsfinalcommand:
                bo"For my final command, I want you to..."
                menu:
                    bo"For my final command, I want you to..."
                    "Move your hands away!":
                        bo"I am sure you know what's next..."
                        show yoru tits5_1 with dissolve
                        yo"No..."
                        show boruto sceeming4 with dissolve
                        bo"Do I have to say it?" with vpunch
                        yo"Please don't make me do that..."
                        bo"Do it! Move your hands away!"
                        show yoru tits5_2 with dissolve:
                            ypos 1.05
                        yo"Y-you are... despicable!"
                        bo"Show your tits you whore!"
                        show yoru tits6 with Dissolve(1):
                            zoom 0.37 ypos 1.00
                        show boruto sceeming2 with dissolve
                        yo"T-there..."
                        bo"D-damn... that's a pretty pair for a 40 year old hag..."
                        yo"..."
                        yo"...C-can I go now? This is h-humiliating..."
                        show boss angry3 behind yoru:
                            easein 0.5 xalign 0.9
                        pause 0.3
                        scene black with vpunch
                        $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                        pause 0.5
                        obo"Nice work you whore, you got the kid all excited!"
                        obo"Now go get dressed!" with vpunch
                        $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                        "..."
                        show ramenkitchen
                        show boruto normal at left
                        show yoru shy at center:
                            xalign 0.7
                        show boss angry2 behind yoru at right:
                            xpos 1.1
                        with dissolve 
                        show yoru shy2 with dissolve:
                            zoom 1.0
                            
                        obo"Nice job kid! You even managed to see a tiddie, probably your first too!"
                        show boss laugh with dissolve
                        obo"Haa-ha-haa!"
                        if yorudontdoanything1 == True:
                            bo"..."
                            show boruto worried with dissolve
                            bot"Obo seems to enjoy humiliating Yoru..."
                            show boruto angry with dissolve
                            bot"Piece of shit..."
                        else:
                            show boruto snob with dissolve
                            bo"I reckon that'll be a common occurrence from now on!"
                        jump threecommandsending






                        jump threecommandsending

                    "Kneel and look straight into my eyes!":
                        bo"Get on your knees!"
                        yo"W-what!? I am not doing that..." with vpunch
                        bo"Oh you are..."
                        show boruto sceeming3 with dissolve
                        bo"And not only will you kneel, you'll be looking straight into my eyes as you do!"
                        show yoru tits5_1 with dissolve
                        yo"No..."
                        show boruto sceeming4 with dissolve
                        bo"On your knees!" with vpunch
                        yo"...Obo?"
                        obo"Well within the rules... Proceed!"
                        show blackscreen with dissolve
                        yo"..."
                        show yorusecretabove0 with dissolve
                        bo"Now that's a pretty sight..."
                        call increaselust(10) from _call_increaselust_52
                        yo"Do you e-enjoy humiliating me you prick!?"
                        menu:
                            yo"Do you e-enjoy humiliating me you prick!?"
                            "More than you know!" (secrethatred = True) if percentage >= 100:
                                $ yoru_kneeled = True
                                bo"I do... more than you realize!"
                                bot"Fuck it! I can't take this anymore"
                                "You locked yourself out of options by being too lustful."
                                bo"Hey Obo!" with vpunch
                                bo"You said anything's allowed as long as no touching is involved, right!?"
                                obo"That's right!"
                                bo"Then you wouldn't mind if I..."
                                scene black with dissolve
                                $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                                show yorusecretintro1 with dissolve
                                bo"Did this!?" with vpunch
                                yo"W-what the... fuck!?"
                                yo"O-obo!?" with vpunch
                                obo"Kid..."
                                show yorusecretintro0 with dissolve:
                                    zoom 1.3 xalign 1.0 yalign 0.0
                                obo"You are just as crazy as I am!" with vpunch
                                show yorusecretintro0 with dissolve:
                                    zoom 1.0 xalign 0.5 yalign 0.5
                                obo"Go ahead! This will be fun... haa-haa-haa!"
                                jump yoruintro_kneel



                            "How perceptive of you!" if percentage < 100:
                                bo"How perceptive of you! You are smarter than I thought..."
                                yo"And you are an even bigger asshole than I though!"
                            "I am just following your husband's lead" if percentage < 100:
                                bo"Not really! I am just following Obo's lead..."
                                yo"A convenient excuse!"
                            
                        scene black with dissolve
                        obo"Alright enough of this. Get up!"
                        show ramenkitchen
                        show boruto sceeming2 at left
                        show yoru tits5_1 at right:
                            zoom 0.4
                        with dissolve
                        show boss angry3 behind yoru:
                            xpos 2.0
                        show boss angry3 behind yoru:
                            easein 0.5 xalign 0.9
                        pause 0.3
                        scene black with vpunch
                        $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                        pause 0.5
                        obo"Nice work you whore, you got the kid all excited!"
                        obo"Now go get dressed!" with vpunch
                        $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                        "..."
                        show ramenkitchen
                        show boruto normal at left
                        show yoru shy at center:
                            xalign 0.7
                        show boss angry2 behind yoru at right:
                            xpos 1.1
                        with dissolve 
                        show yoru shy2 with dissolve:
                            zoom 1.0
                            
                        obo"That was your final command kid, an interesting choice I have to say!"
                        show boss laugh with dissolve
                        obo"Haa-ha-haa!"
                        if yorudontdoanything1 == True:
                            bo"..."
                            show boruto worried with dissolve
                            bot"Obo seems to enjoy humiliating Yoru..."
                            show boruto angry with dissolve
                            bot"Piece of shit..."
                        else:
                            show boruto snob with dissolve
                            bo"Heh..."


                        jump threecommandsending

                    "Push the rules to the limit!" (secrethatred = True) if percentage >= 100:
                        $ yoru_kneeled = True
                        bot"Fuck it! I can't take this anymore"
                        "You locked yourself out of options by being too lustful."
                        bo"Hey Obo!" with vpunch
                        bo"You said anything's allowed as long as no touching is involved, right!?"
                        obo"That's right!"
                        show boruto sceeming3 with dissolve
                        bo"This will be fun!"
                        bo"Get on your knees!" with vpunch
                        show yoru at smallshake
                        yo"W-what!? I am not doing that..."
                        bo"Oh you are..."
                        show boruto sceeming3 with dissolve
                        bo"And not only will you kneel, you'll be looking straight into my eyes as you do!"
                        show yoru tits5_1 with dissolve
                        yo"No..."
                        show boruto sceeming4 with dissolve
                        bo"On your knees!" with vpunch
                        yo"...Obo?"
                        obo"Well within the rules... Proceed!"
                        show blackscreen with dissolve
                        yo"..."
                        show yorusecretabove0 with dissolve
                        bo"Now that's a pretty sight..."
                        bo"Then you wouldn't mind if I..."
                        scene black with dissolve
                        $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                        show yorusecretintro1 with dissolve
                        bo"Did this!?" with vpunch
                        yo"W-what the... fuck!?"
                        yo"O-obo!?" with vpunch
                        obo"Kid..."
                        show yorusecretintro0 with dissolve:
                            zoom 1.3 xalign 1.0 yalign 0.0
                        obo"You are just as crazy as I am!" with vpunch
                        show yorusecretintro0 with dissolve:
                            zoom 1.0 xalign 0.5 yalign 0.5
                        obo"Go ahead! This will be interesting... haa-haa-haa!"
                        jump yoruintro_kneel



        

            
        

    




    label threecommandsending:
        scene black with dissolve
        pause 0.5
        show ramenkitchen
        show boruto normal at left
        show yoru shy at center:
            xalign 0.7
        show boss laugh behind yoru at right:
            xpos 1.1
        with dissolve
        obo"Heh! Kid's got you wrapped around his finger... eh, Yoru!?"
        yo"..."
        obo"If you and him keep this up... I'll have the kid be your boss in no time!"
        obo"If you don't want that, you better step it up, Yoru!"
        $ renpy.sound.play("/audio/soun_fx/intro/spank5instant.opus", channel="sfx3", loop=False, relative_volume = 0.5)
        show yoru at smallshake
        show boss angry3 with vpunch:
            easein 0.2 xalign 0.94
        obo"Now get your ass back to work!"
        show yoru shy2 with dissolve
        obo"Me and the kid here are going to have a men's only conversation..."
        hide yoru with dissolve
        yo"Y-yes Obo..."
        obo"I can see it in your eyes kid... you enjoyed that, didn't you?"
        menu:
            obo"I can see it in your eyes kid... you enjoyed that, didn't you?"
            "Not as much as you did, you sleazy old fuck!":
                show boruto snob with dissolve
                bo"Not as much as you did, you sleazy old fuck!"
                bo"Are you enjoying parading your wife around?"
                obo"Only to those deservant of it! Besides..."
                obo"You've got to admit... Yoru's too hot to be kept for one man's pleasure, don't you think?"
                menu:
                    obo"You've got to admit... Yoru's too hot to be kept for one man's pleasure, don't you think?"
                    "You are batshit insane!":
                        show boruto angry with dissolve
                        bo"You are batshit insane!"
                        show boss laugh with dissolve
                        obo"Hah! You've seen nothing yet kid..."
                    "Damn right she is!" if yorudontdoanything1 == False:
                        show boruto sceeming2 with dissolve
                        call changeHatred(1,"none") from _call_changeHatred_55
                        call borutoevil from _call_borutoevil_2
                        bo"Damn right she is!"
                        bo"Mind sharing some more, old man!?"
                        obo"All in due time, kid..."
                    
            "I want more!" if yorudontdoanything1 == False:
                show boruto sceeming2 with dissolve
                call changeHatred(1,"none") from _call_changeHatred_56
                call borutoevil2 from _call_borutoevil2_8
                bo"I want more, old man!"
                bo"You've given me a taste and now I am addicted!"
                obo"All in due time, kid..."
            "She doesn't deserve this..." if yorudontdoanything1 == True:
                show boruto worried with dissolve
                bo"She doesn't deserve this, Obo..."
                bo"She is just trying to make ends meet!"
                show boss angry2 with dissolve
                obo"That's not your call to make kid... Don't make me regret trusting you."
        show boss angry with dissolve
        show boruto normal with dissolve
        obo"But I'll tell you what kid... You keep working like that and soon enough, you'll be Yoru's boss!"
        obo"In fact, if you outperform my Head Chef's performance, I will grant you full authority of the kitchen!"
        show boruto surprised3 with dissolve
        obo"Meaning that... Yoru will be yours to do with as you please." with vpunch
        menu:
            obo"Meaning that... Yoru will be yours to do with as you please."
            "Maybe I can use that to help her..." if yorudontdoanything1:
                show boruto worried2 with dissolve
                bot"Maybe I can use that to help her somehow..."
                show boruto normal with dissolve
                bo"I'll hold you to that then old man..."
                obo"Haa-ha-haaa!"
                show boss laugh2 with dissolve
                obo"I am good for my word kid!"
                show boss angry2 with dissolve
                obo"Besides, it's the least I could offer... I need your skills around here kid!"

            "Yoru will be my obedient little bitch!" if not yorudontdoanything1:
                show boruto sceeming2 with dissolve
                bo"Are you sure about that you old fuck...?"
                show boruto sceeming3 with dissolve
                call borutoevil2 from _call_borutoevil2_9
                call changeHatred(1,"none") from _call_changeHatred_57
                bo"I might just have your wife be my obedient little slut!" with vpunch
                show boss laugh with dissolve
                obo"Haa-ha-haaa!"
                show boss laugh2 with dissolve
                obo"Which is why you are the right man for the job!"
                show boss angry2 with dissolve
                obo"Besides, it's the least I could offer... After all, I do need your skills around here kid!"

            "I'll steal this old fuck's wife!" if not yorudontdoanything1:
                show boruto sceeming2 with dissolve
                bo"You sure about that you old fuck...?"
                show boruto sceeming3 with dissolve
                call borutoevil2 from _call_borutoevil2_10
                call changeHatred(1,"none") from _call_changeHatred_58
                bo"I might just steal your sexy wife and make her my personal cocksleeve!" with vpunch
                show boss laugh with dissolve
                obo"Haa-ha-haaa!"
                show boss laugh2 with dissolve
                obo"Relax kid, you might be able to boss her around, but she obeys me!"
                show boss angry2 with dissolve
                obo"You can have some fun with her, it's the least I could offer... After all, I do need your skills around here kid!"
                show boruto sceeming2 with dissolve
                bot"Just you wait you old fuck... You'll be a cuck before you realize it!"

        show boss angry2 with dissolve
        obo"But first... let's see you getting there."
        obo"Talk to me again when you meet my expectations kid!"
        hide boss with dissolve
        if yorudontdoanything1 == True:
            show boruto worried with dissolve
            bot"What the hell have I gotten myself into..."
            show boruto worried2 with dissolve
            bot"Can I even do something for Yoru?"
            bot"Will my condition complicate things...?"
            bot"Fuck... I'll have to be careful."
        else:
            show boruto snob with dissolve
            bot"I can't believe the old man is offering his sexy wife to me..."
            show boruto sceeming2 with dissolve
            bot"I'll have her satisfying my needs in no time!"
        hide boruto with dissolve
        $ config.menu_include_disabled = False
        $ renpy.end_replay()
        jump ramenkitchenmenu


label score_4: #obo's story 1 ((head chef score))
    scene ramenkitchen with dissolve
    show boss angry2 at right with dissolve
    show boss at smallshake
    obo"Kid!"
    obo"Come over here, I have to speak with you..."
    show boruto normal at left with dissolve
    bo"What's up old man..."
    obo"Ugh..."
    obo"I don't know how to tell you this but, uh..."
    obo"...U-uuuuuuhh!"
    menu:
        obo"I don't know how to tell you this but, uh..."
        "Out with it you old fuck!":
            show boruto angry2 with dissolve
            bo"Out with it already, you old fuck!"
        "Having a brain aneurysm?":
            show boruto snob with dissolve
            bo"Your age finally caught up with you I see. Having a brain aneurysm, are you?"
        "(What the hell?)":
            show boruto worried with dissolve
            bot"Why does Obo look so worried. What the hell is going on?"
    obo"Kid..."
    show boss scared:
        easein 0.3 xalign 0.5
    show boruto:
        easein 0.3 xpos -1000
    obo"You are not gonna leave me a-alone! Are you?" with vpunch
    show boss scared at center with vpunch:
        zoom 1.5 yalign 0.0
    obo"P-please! Tell me you are gonna stay here!"
    show boss scared at center with vpunch:
        zoom 1.7 yalign 0.0
    obo"I need you around this place!"
    show boss scared at center with vpunch:
        zoom 1.8 yalign 0.0
    obo"You'll s-stay. Won't you?"
    show boss angry3 at center with vpunch:
        zoom 1.9 yalign 0.0
    obo"Big daddy Obo needs you!"
    show boss laugh2 with dissolve
    bo"God damn it old man. I thought something serious was going on..."
    show boss at shake
    obo"Bwaaa-haaa-haa!"
    obo"The look on your face, you know I like to fuck with you twerp!"
    obo"Figuratively of course..."
    show boss angry3 with vpunch
    obo"Maybe literally too now that I think about it!"
    bo"*Sigh*..."
    show boss laugh2 with dissolve
    obo"Okay, okay... Enough fucking around."
    show boss angry2 with dissolve
    obo"Look kid, I was only half joking..."
    obo"The work you are putting around this place is praiseworthy..."
    obo"Immaculate even. You are matching my head chef's performance."
    obo"But uuh, I don't know how to compensate your efforts. I am running into some financial troubles myself you see..."
    obo"Is there any other way I can convince you to stick around?"
    menu:
        obo"Is there any other way I can convince you to stick around?"
        "{color=[dominancecolor]}Your wife would be nice!{/color}":
            bo"Your wife would be nice!"
            call changeDominance(1) from _call_changeDominance_59
            bo"We've been getting to know each other, you know..."
            show boss laugh2 with dissolve
            obo"Haa-haa! What you do with Yoru is your business..."
            show boss angry2 with dissolve
            obo"But don't push your luck, kid!"
        "More money would be nice!":
            bo"More money would be nice..."
            obo"I know, I know! This is as much as I can afford right now..."
            call changeMoney(20) from _call_changeMoney_9
            obo"I would pay you more if I could. I have financial obligations way beyong this place, kid."
            obo"I can't disclose what those are, but I have an important task I have to complete. One that requires all the money I can get..."
        "It's cool! I like this place anyway...":
            bo"Don't worry about it. I am enjoying my time here anyway..."
            obo"Glad to hear that but I'd still like to be convincing if I could..."
    obo"In any case..."
    obo"I was thinking that I could at least extend my appreciation in other ways..."
    obo"Did you happen to learn anything about my uh, side hustles, while you got to know Yoru?"
    if ramennightscenescounter >= 2:
        bot"Is he talking about the photography stuff?"
        menu:
            bot"Is he talking about the photography stuff?"
            "{color=[hatredcolor]}Oh yeah! She told me all about it...{/color}":
                default yoru_toldboruto_sidehustle = False
                $ yoru_toldboruto_sidehustle = True
                bo"You mean your photography gear and all?"
                bo"She told me all about it!"
                bo"Apparently you are some great practitioner who shoots movies and stuff, right?"
                bo"Sometimes you shoot stuff with her even..."
                show boss angry3 with dissolve
                obo"...Yoru told you that?"
                call changeHatred(1) from _call_changeHatred_97
                bo"Certainly did!"
                "Obo mouths something under his breath. He seemed visibly annoyed..."
                obo"{size=*0.8}...That bitch!{/size}"
                show boss laugh2 with dissolve
                obo"Yeah, something of that sort!"

            "Side... hustles?":
                bot"Probably best to avoid mentioning it..."
                bot"Yoru never mentioned it anyway, I only happened to come across his stuff when I was sneaking upstairs..."
                bo"Side... hustles?"
    else:
        bo"Side hustles? You keep yourself busy, don't you, Old man..."
    obo"You see, I am something of a known professional in the field of photography..."
    obo"I shoot... plenty of stuff! But mostly modeling gigs with pretty girls promoting some posh brand's sponsored products."
    obo"It pays good money and comes with a few extra benefits here and there!"
    bo"Okay... Why are you telling me all this?"
    obo"I was thinking that I could show you the ropes, maybe teach you a thing or two. Who knows, we could work together in the future too!"
    bo"I wouldn't even know where to start..."
    obo"I'll tell you what!"
    obo"You know the girl next door? The one she sells the condoms I gifted you the other day!"
    obo"Cute, Asian-looking girl..."
    bo"S-sure..."
    show boss angry2 with dissolve
    obo"She also sells other stuff, including a professional grade camera, but she is fucking clueless when it comes to pricing."
    obo"She owes me a favor or two so I'll have her lower the price of it just for you..."
    obo"I also have connections with luxurious brands and shops around this place."
    "Obo hands you a nice looking referral card to a clothing shop..."
    obo"Visit this place and tell them Obo sent you. They'll treat you like royalty!"
    obo"That should be enough to get you started..."
    obo"If you can show me a couple nice looking pictures with pretty-looking ladies, I might even refer you to more exclusive places!"
    bo"I don't know about all of that, but..."
    bo"T-thanks... I suppose?"
    show boss laugh2 with dissolve
    obo"I'll be waiting to hear about your progress!"
    hide boss with dissolve
    obo"And don't quit on me you wankstain!"
    default bohim_2_started = False

    if quest.exists("bohim_2"):
        if quest.is_state("bohim_2", "pending"):
            $ notification("Quest objective completed")
            $ bohim_2_started = True
            $ camera = Item(name="Camera", info="A camera device used by professional photographers", price=75, quantity=1)
            $ inventoryShop.update_item(f"Camera", price=75, quantity=1)
            $ quest.check("bohim_2", "unlocked")
            $ quest.add([
                Quest("1_bohim_2", _("Inform [him_name] of her [hin_rel_mother]'s financial troubles"), ("A plan for [him_name]"), "in progress"),
                Quest("2_bohim_2", _("Convince [him_name] to work with you"), ("A plan for [him_name]")),
                Quest("3_bohim_2", _("Purchase a camera and convince Yoru to help you"), ("A plan for [him_name]")),
                Quest("4_bohim_2", _("Have your first session with [him_name]"), ("A plan for [him_name]")),
            ])
    bot"Pretty pictures, with pretty girls..."
    bot"Maybe this is how I can make some extra cash!"
    bot"There's two such girls right at home! I wonder if I could convince them to work with me..."
    bot"Knowing [hin_rel] she'd be quite reluctant to the idea. [him_name] on the other hand..."
    bot"She is quite self-absorbed in her own image, this would be right up her alley! If I could just convince her that she could make money working with me..."
    bot"Hehe! I am getting some interesting ideas!"
    jump ramenkitchenmenu



label score_5: #obo's story 1 ((head chef score))
    
    jump ramenkitchenmenu


label score_6: #obo's story 1 ((head chef score))
    
    jump ramenkitchenmenu



label score_7: #obo's story 1 ((head chef score))
    
    jump ramenkitchenmenu




label score_8: #obo's story 1 ((head chef score))
    
    jump ramenkitchenmenu





























default showarrow = False
default mapintrotutorial = False
default showmapbuttons = False
default showmapaftertutorial = False


label ramenintro:
    call hidemarketUI from _call_hidemarketUI_10
    if mapintrotutorial == True:
        jump work
    scene black with dissolve
    call hideUI from _call_hideUI_58
    
    $ renpy.sound.play("/audio/soun_fx/backgroundchatting.opus", channel="sfx2", loop=True, fadein = 1, relative_volume = 0.5)
    show ramenintro with Dissolve(2)
    show boruto surprised2 at left with dissolve
    bo"This place is packed..."
    bo"Surely they'd have a use for a pair of extra hands..."
    bo"If only I could find the guy in charge..."
    show boss angry2 at right with vpunch
    obo"A use for an extra pair of hands you say?"
    show boss angry3 with vpunch:
        easein 0.5 xalign 0.8 yalign 0.99 zoom 1.05
    obo"How about I chop 'em up and use 'em for stew!"
    show boss angry3 with vpunch:
        easein 0.5 xalign 0.7 yalign 0.99 zoom 1.1
    obo"Hmmm, Kid?"
    show boruto surprised with dissolve
    menu:
        obo"How about I chop 'em up and use 'em for stew!"
        "W-what the hell?":
            show boruto surprised2 with dissolve
            bo"W-what the hell?"
        "Who the fuck are you old man?":
            show boruto angry2 with dissolve
            bo"Who the fuck are you old man...?"
        
    
    show boss laugh2 at right with dissolve:
        zoom 1.0
    obo"*chuckles*"
    obo"Ha-ha-haaa! Relax kid, I was just messing around witcha!"
    obo"But you see, my aerodynamic-shaped shiny bald head allows me to pick up sound waves through the very fabric of existence."
    show boruto normal with dissolve
    bot"What a weird dude..."
    obo"Imagine my surprise when I picked up your interest in helping around here."
    show boss angry3 with vpunch:
        easein 0.5 xalign 0.8 yalign 0.99 zoom 1.05
    show boruto surprised2 with dissolve
    obo"YOU!?"
    show boss angry3 with vpunch:
        easein 0.5 xalign 0.7 yalign 0.99 zoom 1.1
    obo"USEFUL?" with vpunch

    obo"How exactly do you reckon that'll be the case, given how puny you look?"
    menu:
        obo"How exactly do you reckon that'll be the case, given how puny you look?"
        "Care to find out right now?":
            show boruto snob with dissolve
            bo"You wanna put that to the test then?"
            show boss angry2 at right with dissolve:
                zoom 1.0
            obo"Ooooh?"
            show boss angry with dissolve
            obo"Is that the confidence of a capable man? Or simply a kid's facade!"
            obo"Let's find out then, shall we?"
        "Listen old fart, I don't give two fucks about this job...":
            show boruto angry with dissolve
            bo"Listen up you old fart, this job means nothing to me. In fact, I don't give two flying fu-"
            show boss laugh2 with vpunch:
                zoom 1.0
            obo"Haa-haa-haaaaa!" with vpunch
            obo"It was but a jest, little kid! Don't get too worked up..."
            show boss normal with dissolve
            obo"Let's find out if you have what it takes then, shall we?"
            obo"Come on, let me show you to to the kitchen..."
    show boss:
        easeout 1 xpos -1000
    show boruto:
        easeout 1 xpos -1000
    scene black with dissolve
    show ramenkitchen with dissolve
    show boruto surprised2 at left with dissolve
    show boss normal at right with dissolve
    obo"This will be your post kid..."
    bo"Nice place you got gramps."
    obo"Don't get excited yet, you've yet to prove yourself."
    show boruto normal with dissolve
    show boss:
        easeout 2 xpos 200
    obo"One more thing, I'll have to introduce you to your co-worker and 2nd in command around this place!"
    "Obo takes a deep breath"
    show boruto surprised2:
        easein 0.1 xpos-0.10
    with Shake((0, 0, 0, 0), 0.7, dist=20, peak_time=0.7, smoothness=50)
    obo"YOOOOOOOOOOOORUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU!!!"
    show boss at right with dissolve:
        xpos 1.05
    show yoru normal at center with dissolve
    obo"Sorry about that, my wife is a little bit hard of hearing, ya know?"
    show yoru shy2 with dissolve
    yo"...Hello"
    show boruto normal with dissolve
    menu:
        yo"..."
        "I can think of one reason why that is...":
            show boruto smirk2 with dissolve
            bo"I can think of at least one reason why that might be the case... Heh!"
            show boss laugh2 behind yoru with dissolve
            obo"Good one kid."
            show boss:
                easein 1 xpos 0.95
            obo"But you'll soon come to find out, my wife ain't just another woman..."
            $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            show yoru at smallshake
            with vpunch
            pause 0.1
            show yoru shy at smallshake with dissolve
            obo"Isn't that right, Yoru?"
            show boruto surprised3 with dissolve
            yo"I s-suppose so..."
            bot"Huh? What does that even mean... And did he just smack her ass?"
        "Damn, she a hottie!":
            show boruto snob with dissolve
            bo"Damn! Aren't you a hottie!"
            show yoru obedient with dissolve
            yo"..."
            show boss laugh2 behind yoru with dissolve
            obo"Ain't she?"
            bo"She's more than your shiny bald head warrants old man..."
            show boss laugh:
                easein 1 xpos 0.95
            obo"Haa-haa-ha!"
            obo"Take good care of the kitchen and she might even look up to you, kid!"
            $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            show yoru at smallshake
            with vpunch
            pause 0.1
            show yoru shy with dissolve
            obo"Isn't that right, Yoru?" with vpunch
            show boruto surprised3 with dissolve
            yo"Y-yes, Obo..."
        "Hello, Nice to meet you!":
            show boruto smirk with dissolve
            bo"Hello, lady. Nice to meet you. I am [bo_name]!"
            yo"Nice to meet you. You can call me Yoru."
            bot"She seems nice..."
            show boss laugh2 behind yoru with dissolve
            obo"Don't get too close now you two. The kid might not be around for much longer."
            show boss:
                easein 1 xpos 0.95
            obo"But if you take good care of the kitchen instead, Yoru here might even look up to you, kid!"
            $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            show yoru at smallshake
            with vpunch
            pause 0.1
            show yoru shy with dissolve
            obo"Isn't that right, Yoru?" with vpunch
            show boruto surprised3 with dissolve
            yo"Y-yes, Obo..."

    show boss angry3 with dissolve
    show boss angry3 at smallshake
    obo"Now back to the kitchen, woman!" with vpunch
    hide yoru with dissolve
    yo"Y-yes!"
    bot"S-something's fishy here... I can feel it."
    show boruto worried with dissolve
    menu:
        yo"Y-yes!"
        "Sneak a peek as his wife walks away":
            scene black with dissolve
            show yoru lookingback with dissolve:
                zoom 0.6 xalign 0.5 yalign 1.0
            show yoru:
                easeout 3 yalign 0.1
            pause 3
            show screen genericparallaxramen("yoru lookingback")
            bot"Is s-she looking at me?" with vpunch
            "You can look up and down by hovering your cursor in the corresponding direction"
            "Or you can tap and drag if you are on a mobile device"
            bot"This girl's packing! What's she doing with this old fart anyway..."
            bot"Her ass is so... inviting."
            bot"Can't blame gramps can I? I would give her a little love tap too if I had the chance!"
            "Click twice to continue"
            window hide
            $ ui.interact()
            hide screen genericparallaxramen
            show ramenkitchen
            show boss angry3 at center with vpunch:
                zoom 1.5 yalign 0.0
            obo"Hey kid! I can see you eye-fucking my wife ya know..."
            show boss angry3 at center with vpunch:
                zoom 1.7 yalign 0.0
            obo"Cut it off or it's your little white ass that's gonna take some fucking..."
            show boss angry3 at center with vpunch:
                zoom 1.8 yalign 0.0
            obo"And not the eye-fucking kind!"
            show boss angry3 at center with vpunch:
                zoom 1.9 yalign 0.0
            menu:
                obo"Cut it off or it's your little white ass that's gonna take some fucking..."
                "Not before your fat black ass gets railed old man!":
                    bo"That is if I don't rail your fat black ass first, you old fuck!"
                    show boss laugh2 at right:
                        zoom 1.0 yalign 0.0
                    show boruto angry at left
                    with dissolve
                    obo"*Chuckles*"
                    "Obo let's out a hearty laugh!"
                    obo"Haa-haa-haaaa!"
                    show boruto smirk with dissolve
                    obo"Finally! Someone around here who gets my humor!"
                    obo"I am taking a liking to you kid, don't fuck this one up now or I'll miss your little white ass!"
                    show boruto worried with dissolve
                    bo"..."
                    bot"This old man sure is weird..."

                "Okay, Okay!":
                    bo"Okay, okay!"
                    show boss angry3 at center with vpunch:
                        zoom 2.0 yalign 0.0
                    obo"Your balls haven't dropped yet, have they kid?"
                    show boss laugh2 at right:
                        zoom 1.0 yalign 0.0
                    show boruto normal at left
                    with dissolve
                    obo"Haa-haa-ha!"
                    obo"You can relax kid, I am just fucking around with you!"
                    obo"Don't worry you can take a look or two. My wife has that effect on men after all, let alone twerps like you!"
            obo"I'll tell you what kid... You prove yourself to be useful around here and I might just let you have more than a look..."
            show boruto surprised3 with dissolve
            obo"What do you say, kid?"
            menu:
                obo"What do you say, kid?"
                "I am not gonna pass that chance up":
                    show boruto snob with dissolve
                    bo"Gonna hold you to that, old man!"
                "You are crazy, you old fuck":
                    show boruto smirk with dissolve
                    bo"You are crazy, you old fuck."
                    show boss normal with dissolve
                    obo"What's life without a little spice, kid. You'll come to realize that soon enough!"
        "Don't":
            pass
        
            
    #jump here for testing inside qte_start
    label resettechtest:
        show boss angry2 at right with dissolve
        show boruto normal at left with dissolve
        obo"Enough yapping kid, it's time to see if you have what it takes!"
        obo"Working a ramen kitchen isn't as simple as one might think... Make sure you read the information leaflet before you give it a shot!"
        obo"If you perform well enough I'll let you work around here, deal?"
        show boss angry with dissolve
        obo"Oh and this is just a test, I ain't paying shit for some twerp's first attempt, nor am I keeping score..."
        hide boruto
        hide boss
        with dissolve
        show screen workmenutopright
        jump start_qte
     
        
#first time work intro / otherwise skip and jump to work
label shiftendtutorial:
    if mapintrotutorial == True:
        jump work
    else:
        label endofworktutorial:

            show boruto normal at left with dissolve
            show boss normal at right with dissolve
            
            if finalscore > 3500:
                show boss scared with vpunch
                obo"W-what the hell!? Kid... you sure you've never done this before?"
                show boss laugh with dissolve
                obo"You aren't... cheating are you? Turning time back or something... like the guy dodging bullets from that one famous movie?"
                show boruto smirk with dissolve
                bo"What can I say, guess I am gifted!"
                show boss angry2 with dissolve
                obo"In any case. I certainly have a use for someone like you around here..."
            elif finalscore > 3000:
                show boss angry3 with dissolve
                obo"That's... your first time?"
                show boss laugh with dissolve
                obo"Impressive, kid... you are almost as good as Yoru!"
                show boruto smirk with dissolve
                show boss angry2 with dissolve
                obo"In any case. I could use your skills around this place..."

            elif finalscore > 2000:
                show boss angry3 with dissolve
                obo"That was pretty good for your first time, kid! You can certainly pull your own weight..."
                obo"You've earned yourself a post around here."

            elif finalscore > 1000:
                show boss angry with dissolve
                obo"Can't expect much more from a total twerp can I?"
                obo"That was barely enough to warrant another shot at this kid..."

            elif finalscore > 500:
                show boss angry with dissolve
                obo"Kid... You've barely done more than what my five year old niece could do."
                obo"But I am not one to deny an aspiring kid a second chance..."
            else:
                show boss angry3 with vpunch
                obo"Is this some sort of joke, kid!?"
                show boss angry2 with dissolve
                obo"That performance was a load of horseshit. In fact I don't think I've ever seen someone do worse than that..."
                obo"But I am not one to deny an aspiring kid a second chance..."

            show boss angry2 with dissolve
            if finalscore <1000:
                obo "You don't have much leverage to bargain with, kid. You have no skillset, no credentials and you probably haven't even finished school yet."
            obo "I can't promise you much, but if you show up around this place during mornings and evenings, I might have some work for you."
            obo "Your payment will be dependent on how useful you prove yourself to be."
            show boruto snob with dissolve
            $ high_score = 0
            bo"Alright, when do I start old man?"
            $ quest.check("job_1", "completed")
            $ quest.check("job_2", "in progress")
            $ notification("Quest updated")
            show boss angry with dissolve
            obo "You can start tomorrow, Show up, or don't. I don't particularly care..."
            obo "But if you do show up, put some effort into it kid and maybe I'll make it worth your while in more ways than one!"
            menu:
                obo "But if you do show up, put some effort into it kid and maybe I'll make it worth your while in more ways than one!"
                "Alright you old fart. See you tomorrow!":
                    show boruto snob with dissolve
                    bo"You got it you old fart. I'll see you tomorrow then..."
                    show boss angry3 with vpunch
                    obo"This old fart will beat your face in, kid!"
                    show boss laugh2 with dissolve
                    obo"Haa-haa-ha! I jest of course... What kind of monster would beat up kids!"
                    show boruto worried
                    show boss angry3 with vpunch:
                        easein 0.5 xalign 0.8 yalign 0.99 zoom 1.05
                    obo"OR AM I, KID?" with vpunch
                    show boss laugh2 with dissolve
                    show boruto smirk with dissolve
                    obo"*Chuckles*"
                    obo"See you tomorrow then!"
                    hide obo with dissolve
                    bot"This fucking guy..."
                    show boruto smirk2 with dissolve
                    bot"Is he running a circus or a ramen shop, I can't quite tell."
                "I'll see what I can do...":
                    show boruto worried with dissolve
                    bo"I'll see what I can do..."
                    show boss laugh with dissolve
                    obo"Don't get lost in the sauce, kid!"
                    obo"I hope to see you around soon!"
                
            
            jump action_taken



         
screen genericparallaxramen(baseImage):
    on "show" action Function(mark_screen_image_gallery, baseImage)
    key "K_SPACE" action Return()
    button:
        action Return()

    viewport:
        area (320, 0, 1.5, 1.5)
        edgescroll (340, 550)
        add baseImage subpixel True zoom 0.7
        draggable True