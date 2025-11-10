label hima_earnhertrust:
    default firsttime_earnhertrust = False
    if firsttime_earnhertrust == True:
        jump repeatable_earnhertrust
    if money >= 10:
        pass
    else:
        "You need at least $10 to attempt this..."
        jump himastretchingmenu
    show boruto snob with dissolve
    bot"Let's see, how do I do this..."
    bot"I know [him_name] is materealistic in some ways..."
    bot"If I show her that I am making a lot of money and perhaps even shower her with some of it, I am sure she'd quickly change her tune..."
    bot"She also seems to like it when I involve her in things, despite how she often acts..."
    bo"So uh, remember when I told you I've been putting in hours in a local restaurant?"
    him"Yeah, so?"
    bo"Turns out the owner of the place really likes me. He says I've been performing better than even his Chefs!"
    him"Why am I having trouble believing that knowing how useless you are..."
    bo"I am not saying that to boast [him_name]..."
    bo"The truth is, I've been making quite the sum working there..."
    bo"The owner trusts me enough to pay me a hefty sum for my efforts..."
    bo"A sum that I plan on using to help [hin_rel] with her troubles..."
    bo"But I am also thinking about you, you know..."
    him"Reaaally now..."
    bo"I am serious, [him_name]..."
    bo"I want you to have nice things, and I know you want to contribute with [hin_rel]'s troubles too, so..."
    call changeMoney(-10) from _call_changeMoney_11
    bo"Here, you can have this..."
    show hima worried2 with dissolve
    him"T-ten m-monies!? F-for me?" with vpunch
    bo"Yep!"
    him"R-really!? With no catch at all?"
    menu:
        him"R-really!? With no catch at all?"
        "Well.. Maybe a kiss on the cheek!":
            bo"Well, maybe a little kiss on the cheek to show your appreciation!"
            him"Hmm..."
            show hima:
                easein 0.6 xalign 0.4
            pause 0.4
            show blackscreen with dissolve
            him"I s-suppose I can do that much!"
            show hima_kiss1 with dissolve
            him"You are even uglier than usual up close..."
            bo"Hehe!"
            $ renpy.sound.play("/audio/soun_fx/hinata/kisscheek.opus", channel="sfx2", loop=False, relative_volume = 0.6)
            show hima_kiss1_1 with dissolve:
                zoom 1.1 xalign 0.0
            him"*Kiss*"
            hide hima_kiss1_1
            show hima_kiss1
            with dissolve
            call changeRespect("Himawari", 2) from _call_changeRespect_128
            him"There, happy now?"
            hide hima_kiss1
            hide blackscreen
            show hima smugshy:
                easein 0.6 xalign 0.8
            with dissolve
            bo"It's nice to see you not being a devil spawn for once..."
            him"Right back at you..."
            "*Both giggling*"

            


        "No catch at all...":
            bo"No catch at all..."
            him"I... I don't know what to say!"
            bo"Try a 'thank you' for once, you devil spawn!"
            show hima smugshy with dissolve
            him"I am sorry, I am just not used to you acting like a half decent human being!"
            show hima at smallshake
            him"Teehee!"
            call changeRespect("Himawari", 3) from _call_changeRespect_129
            him"But really, thank you!"

            
        "{color=[hatredcolor]}(There is a catch, you just don't know it!){/color}" if hatred >= 15:
            call checkHatred(15,None) from _call_checkHatred_13
            show boruto sceeming with dissolve
            bot"Of course there is a catch, you bitch..."
            call changeHatred(1) from _call_changeHatred_105
            bot"You are just to stupid to see through my ploy! Hehe..."
            bo"No catch at all! Besides a kiss on the cheek for your considerate [him_rel_to_bo]!"
            bo"Surely you can do that much... right?"
            show hima:
                easein 0.6 xalign 0.4
            pause 0.4
            show blackscreen with dissolve
            him"I s-suppose that's not the worst you could ask for..."
            bot"You are right on that count! Maybe I should ask you to suck my dick next time, bitch!"
            show hima_kiss1 with dissolve
            him"You are even uglier than usual up close..."
            bo"Look who's talking!"
            $ renpy.sound.play("/audio/soun_fx/hinata/kisscheek.opus", channel="sfx2", loop=False, relative_volume = 0.6)
            show hima_kiss1_1 with dissolve:
                zoom 1.1 xalign 0.0
            him"*Kiss*"
            hide hima_kiss1_1
            show hima_kiss1
            with dissolve
            call changeRespect("Himawari", 1) from _call_changeRespect_130
            him"There, happy now?"
            hide hima_kiss1
            hide blackscreen
            show hima smugshy:
                easein 0.6 xalign 0.8
            with dissolve
            bo"It's nice to see you not being a devil spawn for once..."
            him"Right back at you..."
            "*Both giggling*"
    show blackscreen with dissolve
    show hima shy
    "..."
    hide blackscreen with dissolve
    him"Ten whole m-monies... Imagine all the snackies I can buy with it!" with vpunch
    show hima worried2 with dissolve
    him"Although it's probably best to save it for [hin_rel]..."
    bo"It's your money now. You get to decide what to do with it, but imagine this..."
    bo"If we were to work together you wouldn't have to decide between the two..."
    bo"We could help [hin_rel], AND you could buy enough snacks to satisfy your heart's content!"
    him"That sounds nice and all but... How much money are we even talking about?"
    bo"Who knows. Hundreds... thousands, depends on how good you are at your job."
    him"Th... Th-thousands!?" with vpunch
    bo"Let's not get ahead of our selves just yet, we have to put in the work first..."
    bo"But I'll tell you what..."
    bo"You keep being less of a demon spawn and I might have a little something for you here and there, deal?"
    him"I'll try..."
    show hima smugshy with dissolve
    him"As long as you keep being less useless too!"
    show hima:
        ease 2 xpos -1000
    him"Teehee! I am outa here, I've got things to do!"
    show boruto normal with dissolve
    bo"*Sigh*..."
    show boruto sceeming with dissolve
    bot"Not a bad first step!"
    bot"I'll keep this up for a while, see where it gets us..."
    $ firsttime_earnhertrust = True
    jump action_taken


label repeatable_earnhertrust:
    bot"What should I try this time..."
    menu repeatable_earnhertrust_menu:
        bot"What should I try this time..."
        "{color=[obediencecolor]}Offer her some money...{/color}":
            jump repeatable_offermoney
        "{color=[obediencecolor]}????{/color}" if earnhertrust2 == False:
            "Complete previous options to unlock..."
            jump repeatable_earnhertrust_menu
        "{color=[obediencecolor]}There's something you can help me with...{/color}" if earnhertrust2 == True and blindfoldrepeat == 0:
            jump repeatable_blindfold
        "{color=[obediencecolor]}Ready for the blind taste test?{/color}" if earnhertrust2 == True and blindfoldrepeat == 1:
            jump repeatable_blindfold
        "{color=[obediencecolor]}I refined my recipe, ready for another go?{/color}" if earnhertrust2 == True and blindfoldrepeat >= 2:
            jump repeatable_tastetest
        "{color=[obediencecolor]}????{/color}" if blindfoldfinished == False and blindfoldrepeat < 3:
            "Complete the previous options to unlock."
            jump repeatable_earnhertrust_menu
        "{color=[obediencecolor]}????{/color}" if blindfoldfinished == False and blindfoldrepeat == 3:
            "Show her your 'refined recipe' one more time to unlock!"
            jump repeatable_earnhertrust_menu

        "{color=[obediencecolor]}Ready for your modelling session?{/color}" if hima_accepted_modelling == True and yoruichi_modelling_completed==True:
            if himamodel_firsttime == True:       
                jump himawari_modelling_session #tutorial
            else:
                $ hima_talked_modelling = True #random fix
                jump himawari_modelling_session_repeatable

        "{color=[obediencecolor]}About the modelling thing we discussed...{/color}" if blindfoldfinished == True and (hima_accepted_modelling == False):
            default yoruichi_modelling_completed = False
            default hima_accepted_modelling = False
            if hima_talked_modelling == True and yoruichi_modelling_completed == False:
                bo"About the modelling thing we discussed..."
                bo"Are you ready to start?"
                show hima mad with dissolve
                him"You still haven't showed me what we agreed on!" with vpunch
                him"Don't try to push me into it... I-idiot!" with vpunch
                bo"R-right, I forgot..."
                bot"Oops! I'll have to show her I am experienced first..."
                bot"I should try asking Yoru for help..."
                show hima smugshy with dissolve
                jump himastretchingmenu
            else:
                pass

            if yoruichi_modelling_completed == True and hima_talked_modelling == True:
                $ hima_accepted_modelling = True
                $ hima_talked_modelling = True
                jump himawari_modelling_session            
            bo"You know, I was thinking..."
            him"A rare occurrence! Teehee!" with vpunch
            bo"Come on, I am serious..."
            bo"We've been doing a lot better lately, me and you..."
            him"Only slightly! Don't think we are all buddy-buddy now because I talk to you a bit..."
            bo"Come on... Don't you think it's time we start working together?"
            bo"Imagine the things we could do... The money we could make!"
            show hima worried2 with dissolve
            him"Work... t-together? You mean... the m-modelling thing?"
            show boruto snob with dissolve
            bo"Y-yeah..."
            him"I... I am still thinking about that... "
            him"It just feels like a big leap, doesn't it?"
            him"I mean... me? Modelling for... you?"
            him"It sounds and feels w-wrong!" with vpunch
            show boruto normal with dissolve
            bo"What's wrong with taking a few pictures. We don't have the leisure of time you know..."
            bo"[hin_rel] is still-"
            show hima mad with dissolve
            show boruto surprised2 with Dissolve(0.2)
            him"Don't try guilt-tripping me into it you dummy!" with vpunch
            show hima worried2 with dissolve
            himt"But he is right on that count. [hin_rel]'s debt problem won't go away on its own..."
            himt"We need to... I need to do s-something to help!" with vpunch
            show hima embarassed with dissolve
            show hima at shake
            him"Mmmmmrraaaah! *Fuming*" with vpunch
            label fine_modeling_agreed_himawari:
            him"F-fine, okay!? I will do it..." with vpunch
            show boruto surprised2 with dissolve
            bo"Y-you will?" with vpunch
            show hima worried2 with dissolve
            him"On one condition..."
            show boruto normal with dissolve
            bo"..."
            him"I'll only m-model for you if you can first prove that this isn't some s-stupid elaborate ploy of yours..."
            him"You'll have to show me that you actually know w-what you are doing..."
            him"You'll have to show me that I can t-trust you!" with vpunch
            him"F-fair enough?"
            show boruto surprised2 with dissolve
            bo"A.. p-ploy? Come on [him_name], do you still not trust your big [him_rel_to_bo]?"
            him"..."
            show hima mad with dissolve
            him"Can you do that or not!" with vpunch
            bot"S-shit! I'll have to figure something out..."
            bot"Yoru... Maybe I can convince her to help me out with this one..."
            show boruto snob with dissolve
            bo"Of c-course I can!"
            bo"It's the least you could ask for..."
            bo"Maybe I can introduce you to one of my models sometime soon...?"
            bo"Would that be enough to convince you...?"
            show hima worried2 with dissolve
            him"A r-real m-model?" with vpunch
            him"There's no way y-you..."
            show hima smugshy with dissolve
            if quest.exists("bohim_2"):
                if quest.is_state("3_bohim_2", "pending") or quest.is_state("2_bohim_2", "in progress") or quest.is_state("2_bohim_2", "pending") :
                    $ quest.change_quest_title("2_bohim_2",f"Convince {him_name} to work with you")
                    $ quest.change_quest_title("3_bohim_2",f"Purchase a camera and convince Yoru to help you")
                    $ quest.change_quest_title("4_bohim_2",f"Have your first session with {him_name}")
                    $ notification (f"Quest objective completed")
                    $ quest.check("2_bohim_2", "completed")
                    $ quest.check("3_bohim_2", "in progress")
            him"Hmph! F-fine then... I'll work with you after you introduce me to them!"
            bo"Then let that be a promise between us!"
            him"S-sure..."
            himt"There's no way [bo_name_stutter] works with a real model..."
            show boruto:
                easein 1 xpos -1000
            bo"See you soon!"
            himt"...R-right?"
            hide hima with dissolve
            himt"Him... with a model? Ha!" with vpunch
            default hima_talked_modelling = False
            $ hima_talked_modelling = True
            jump action_taken
        "Return":
            jump himastretchingmenu
        

label repeatable_offermoney:
    if money >= 10:
        pass
    else:
        "You need at least $10 to attempt this..."
        jump himastretchingmenu
    bo"[him_name], I've got something for you..."
    him"Do you now..."
    if himawari_respect >= 0:
        call checkRespect(0,"Himawari") from _call_checkRespect
        if hima_forcekiss > 0:
            him"Need I remind you what you did last time?"
            show hima mad with dissolve
            him"I am not talking to you until you apologize first!"
            show boruto embarassed with dissolve
            bo"Are you talking about the kiss? Come on [him_name]..."
            show boruto snob with dissolve
            bo"Are you really that prude? It was just a silly little prank, it meant nothing..."
            bo"But alright, I am sorry..."
            show hima smugshy with dissolve
            $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            him"Hmph! You better be!"
            him"Anyways..."
            $ hima_forcekiss = 0

        if himawari_fristkiss == True and kissapology == False:
            default kissapology = False
            $ kissapology = True
            him"Need I remind you what you did last time?"
            show hima mad with dissolve
            him"I am not talking to you until you apologize first!"
            show boruto embarassed with dissolve
            bo"Are you talking about the kiss? Come on [him_name]..."
            show boruto snob with dissolve
            bo"Are you really that prude? It was just a silly little prank, it meant nothing..."
            bo"But alright, I am sorry..."
            show hima smugshy with dissolve
            $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            him"Hmph! You better be!"
            him"Anyways..."
        if forcegrope_1sttime == True and gropeapology == False:
            default gropeapology = False
            $ gropeapology = True
            him"Need I remind you what you did last time?"
            show hima mad with dissolve
            him"I am not talking to you until you apologize first!"
            show boruto embarassed with dissolve
            bo"Are you talking about the hug? Come on [him_name]..."
            show boruto snob with dissolve
            bo"Are you really that prude? It was just a silly little prank, it meant nothing..."
            bo"But alright, I am sorry..."
            show hima smugshy with dissolve
            $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            him"Hmph! You better be!"
            him"And I am not prude or stupid you buffoon, that wasn't a prank at all! You touch me again like that and I'll cut your hands off!"
            him"Anyways..."
        pass
    else:
        show hima mad with dissolve
        call checkRespect(0,"Himawari") from _call_checkRespect_1
        show boruto surprised2 with dissolve
        him"Well I don't care! I don't want to talk to you right now..." with vpunch
        "[him_name] has no respect for you. Try to earn some of it back by giving her gifts or serving her interests..."
        jump repeatable_earnhertrust_menu
    him"And what may that something be...?"
    show boruto snob with dissolve
    bo"I've been making bank recently... I thought I'd spoil my little [him_rel] a little more!"
    call changeMoney(-10) from _call_changeMoney_12
    bo"Here, you can have this..."
    show hima shy with dissolve
    him"T-ten more m-monies!?" with vpunch
    show hima worried2 with dissolve
    him"A-are you s-sure I can just take this from you?"
    menu:
        him"A-are you s-sure I can just take this from you?"
        "{color=[obediencecolor]}I'd be more convinced with a kiss!{/color}":
            bo"I'd be more convinced with a kiss..."
            bo"You know, to show your appreciation!"
            call checkObedience(5,"hima_offermoney_fail","Himawari") from _call_checkObedience_12
            if himawari_fristkiss == True:
                him"Another k-kiss, huh?"
                him"I s-suppose I can do that much... But don't try anything stupid!"
            else:
                him"A k-kiss, huh?"
                him"I s-suppose I can do that much... if it's on the cheek!"
            show hima:
                easein 0.6 xalign 0.4
            pause 0.4
            show blackscreen with dissolve
            bo"Sure..."
            show hima_kiss1 with dissolve
            him"I can't get over how ugly you are up close..."
            menu repeatablekiss:
                him"I can't get over how ugly you are up close..."
                "Let her kiss your cheek...":
                    default unlockkissdom = False
                    $ unlockkissdom = True
                    $ renpy.sound.play("/audio/soun_fx/hinata/kisscheek.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                    show hima_kiss1_1 with dissolve:
                        zoom 1.1 xalign 0.0
                    him"*Kiss*"
                    hide hima_kiss1_1
                    show hima_kiss1
                    with dissolve
                    call changeObedience("Himawari",1,"himakissrepeatable",2) from _call_changeObedience_85
                    him"T-there, happy now?"
                    hide hima_kiss1
                    hide blackscreen
                    show hima smugshy:
                        easein 0.6 xalign 0.8
                    with dissolve
                    bo"It's nice to see you not being a devil spawn for once..."
                    him"Right back at you..."
                    "*Both giggling*"
                    call changeRespect("Himawari", 2) from _call_changeRespect_131
                    him"But thank you for this... I'll save it up and help [hin_rel] with it when needed!"
                    bo"No worries..."
                    show hima:
                        easein 2 xpos -1000
                    him"Anyways, My money now! Yahoooo! I am rich!" with vpunch
                    bo"*Sigh*..."
                    jump action_taken
                "{color=[dominancecolor]}????{/color}" if unlockkissdom == False:
                    "Complete previous options to unlock..."
                    jump repeatablekiss
                "{color=[dominancecolor]}Pull the oldest trick in the book...{/color}" if unlockkissdom == True:
                    call checkDominance(3,"repeatablekiss") from _call_checkDominance_13
                    default himawari_fristkiss = False
                    bot"Hehe... I wonder how she'd react to this!"
                    bot"When the time is right..."
                    label replay_himakiss:
                    $ initialize_replay_defaults()
                    if _in_replay:
                        $ himawari_fristkiss = True
                    show hima_kiss1_1 with dissolve:
                        zoom 1.1 xalign 0.0
                    bot"Now!" with vpunch
                    call changeDominance(1,"repeatablekiss",3) from _call_changeDominance_65
                    $ renpy.sound.play("/audio/soun_fx/hinata/kisscheek.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                    show kiss1_trick with dissolve
                    him"!!" with vpunch
                    if himawari_fristkiss == True:
                        menu:
                            bot"Our lips are locked! I am tempted to try something more..."
                            "Drop the prank...":
                                default hima_forcekiss = 0
                                $ hima_forcekiss = 1
                                hide hima_kiss1
                                hide hima_kiss1_1
                                hide kiss1_trick
                                hide blackscreen
                                show hima embarassed:
                                    easein 0.6 xalign 0.8
                                with dissolve
                                show hima at shake
                                him"*Ptoo Ptooey*! Yuuck!! *Ptoo*!!"
                                show hima at smallshake
                                call changeRespect("Himawari", -1) from _call_changeRespect_132
                                him"What the hell are you doing you freaking idiot!!" with vpunch
                                show hima mad with dissolve
                                him"Are you just looking for excuses to do weird t-thing to me!?"
                                show boruto embarassed with dissolve
                                bo"It was just a silly prank, relax..."
                                show hima embarassed with dissolve
                                call changeObedience("Himawari",1,"himakisslips2",4) from _call_changeObedience_86
                                him"You better s-stop with your stupid pranks then, or we are going back to square one!"
                                show hima:
                                    easein 2 xpos -1000
                                $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                him"Hmph! I'll r-remember this..." with vpunch
                                show boruto snob with dissolve
                                bot"Hehe, she isn't even raising that much of a fuss anymore..."
                                $ earnhertrust2 = True
                                $ renpy.end_replay()
                                jump action_taken

                            "{color=[obediencecolor]}Kiss her lips...{/color}":
                                bot"Let's make this a real kiss!"
                                $ renpy.sound.play("/audio/soun_fx/hinata/kisscheek.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                                show kiss1_trick2 with dissolve:
                                    zoom 1.1 xalign 0.9 yalign 0.8
                                "You puckered your lips around hers before she could react..."
                                $ hima_forcekiss = 2
                                hide hima_kiss1
                                hide kiss1_trick2
                                hide hima_kiss1_1
                                hide kiss1_trick
                                hide blackscreen
                                show hima embarassed:
                                    easein 0.6 xalign 0.8
                                with dissolve
                                show hima at shake
                                him"*Ptoo Ptooey*! Yuuck!! *Ptoo*!!"
                                show hima at smallshake
                                him"D-did you just..."
                                show hima mad with dissolve
                                call changeRespect("Himawari", -2) from _call_changeRespect_133
                                him"Y-you... W-what the hell did you just do to me!!" with vpunch
                                show hima embarassed with dissolve
                                call changeObedience("Himawari",1,"himakisslips2",4) from _call_changeObedience_87
                                him"Y-you... y-you actually kissed me!"
                                show boruto embarassed with dissolve
                                bo"D-did I...? Hahaha! It was a prank... *Nervous laughter*"
                                show hima mad with dissolve
                                him"I am telling [hin_rel]!" with vpunch
                                show hima:
                                    easein 2 xpos -1000
                                him"You freaking weirdo!"
                                show boruto surprised2 with dissolve
                                bot"Heh, I actually kissed her for real, this time..."
                                show boruto snob with dissolve
                                bot"Although she wasn't into it, A kiss is a kiss!"
                                default earnhertrust2 = False
                                $ earnhertrust2 = True
                                $ renpy.end_replay()
                                jump action_taken
                                


                            "{color=[hatredcolor]}Force a french kiss!{/color}":
                                default forcekiss_1sttime = False
                                bot"Fuck it, it's now or never!"
                                $ renpy.sound.play("/audio/soun_fx/hinata/kisscheek.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                                show kiss1_trick2 with dissolve:
                                    zoom 1.1 xalign 0.9 yalign 0.8
                                "You puckered your lips around hers and..."
                                hide blackscreen
                                show kiss_force1
                                with dissolve
                                "You slipped your tongue inside her mouth..." with vpunch
                                himt"!!!" with vpunch
                                show blackscreen with vpunch
                                him"*Gasp* W-what are you-!!"
                                hide blackscreen
                                show kiss_force2
                                with dissolve
                                "[him_name] tried to back off, but you pushed your hand behind her head and forced your tongue deeper into her mouth..."
                                show kiss_force2:
                                    zoom 1.1 xalign 0.5 yalign 1.0
                                him"Mhmm-mmm" with vpunch
                                bot"How's this for a kiss, you brat!"
                                show kiss_force2_1 with dissolve:
                                    zoom 1.1 yalign 0.0 xalign 0.5
                                bot"Although I gotta give it to her, she tastes... kinda nice!"
                                "[him_name] has had enough. She grabbed your arm and raised her knee to try and push you away..." 
                                show blackscreen with vpunch
                                him"*Grunts* Eh-mhm!" with vpunch
                                hide hima_kiss1
                                hide kiss1_trick2
                                hide hima_kiss1_1
                                hide kiss1_trick
                                hide blackscreen
                                hide kiss_force2
                                hide kiss_force2_1
                                hide kiss_force1
                                show hima embarassed:
                                    easein 0.6 xalign 0.8
                                with dissolve
                                show hima at shake
                                him"*Ptoo Ptooey*! Yuuck!! *Ptoo*!!"
                                show hima at smallshake
                                if forcekiss_1sttime == False:
                                    him"D-did you just..."
                                    show hima mad with dissolve
                                    call changeRespect("Himawari", -5) from _call_changeRespect_134
                                    him"Y-you... W-what the fuck was that you retarded p-pervert!" with vpunch
                                    show boruto embarassed with dissolve
                                    bo"Hahaha, It was just a prank... *Nervous laughter*"
                                    show boruto sceeming with dissolve
                                    bo"Thought I'd show you what a real kiss is since you seemed to have no idea..."
                                    show hima at smallshake
                                    him"That was not a p-prank you stupid asshole! Y-you went way too far!"
                                    show hima embarassed with dissolve
                                    call changeObedience("Himawari",2,"himakisstongue",2) from _call_changeObedience_88
                                    him"Y-you... y-you kissed me and... a-and... you pushed your tongue into me!"
                                    show boruto embarassed with dissolve
                                    bo"Did I... Hehe *Nervous laughter*"
                                    call changeRespect("Himawari", -6) from _call_changeRespect_135
                                    him"Don't p-play stupid...Y-you... you r-raped me!"
                                    show boruto at smallshake
                                    bo"Now you are just exaggerating! Don't have to go that far, It was a... joke!"
                                    show hima mad with dissolve
                                    him"I am telling [hin_rel]!" with vpunch
                                    show hima:
                                        easein 2 xpos -1000
                                    him"You freaking perverted weirdo!"
                                    show boruto surprised2 with dissolve
                                    bot"Oops, might have gone too far, too fast..."
                                    show boruto snob with dissolve
                                    bot"But it was worth it! I definitely stole her first kiss, and I got to taste her along with it..."
                                    bot"For how much she runs her mouth, she sure did taste nice..."
                                    $ forcekiss_1sttime = True
                                    $ earnhertrust2 = True
                                    $ renpy.end_replay()
                                    jump action_taken
                                else:
                                    him"I... I can't believe I trusted you again..."
                                    show hima mad with dissolve
                                    call changeRespect("Himawari", -5) from _call_changeRespect_136
                                    him"W-why did you do that you retarded p-pervert!" with vpunch
                                    show boruto embarassed with dissolve
                                    bo"Hahaha, It was just a prank... *Nervous laughter*"
                                    show boruto sceeming with dissolve
                                    bo"Thought I'd help you practice your kissing since you are such a prude... "
                                    show hima at smallshake
                                    him"That was not a p-prank you stupid asshole! Y-you went way too far!"
                                    show hima embarassed with dissolve
                                    call changeObedience("Himawari",2,"himakisstongue",2) from _call_changeObedience_89
                                    him"And I don't need to practice anything, certainly not with you! Asshole..."
                                    show boruto embarassed with dissolve
                                    bo"Sure, sure... It wasn't a big deal anyway..."
                                    call changeRespect("Himawari", -6) from _call_changeRespect_137
                                    him"Don't p-play stupid...Y-you... you r-raped me!"
                                    show boruto at smallshake
                                    bo"Now you are just exaggerating! Don't have to go that far, It was a... joke!"
                                    show hima mad with dissolve
                                    him"I am telling [hin_rel]!" with vpunch
                                    show hima:
                                        easein 2 xpos -1000
                                    him"You freaking perverted weirdo!"
                                    show boruto surprised2 with dissolve
                                    bot"Well, shit... Here we go again!"
                                    show boruto snob with dissolve
                                    bot"But it was worth it! She tasted even better than before..."
                                    $ forcekiss_1sttime = True
                                    $ earnhertrust2 = True
                                    $ renpy.end_replay()
                                    jump action_taken




                    else:
                        #dominance first trick kiss
                        $ himawari_fristkiss = True
                        hide hima_kiss1
                        hide hima_kiss1_1
                        hide kiss1_trick
                        hide blackscreen
                        show hima embarassed:
                            easein 0.6 xalign 0.8
                        with dissolve
                        show hima at shake
                        him"*Ptoo Ptooey*! Yuuck!! *Ptoo*!!"
                        show hima at smallshake
                        him"W-what..."
                        show hima mad with dissolve
                        call changeRespect("Himawari", -1) from _call_changeRespect_138
                        him"What the HELL are you doing you freaking idiot!!" with vpunch
                        show boruto embarassed with dissolve
                        bo"It was just a silly prank, relax..."
                        show hima at smallshake
                        him"R-relax!?" with vpunch
                        him"You... Y-you! Our l-lips... T-they t-touched!!"
                        show boruto snob with dissolve
                        bo"Ooooh? Did I steal your first kiss or something, hehe..."
                        show hima embarassed with dissolve
                        him"T-that... *Fuming*..."
                        show hima mad with dissolve
                        him"THAT W-WASN'T MY F-FIRST KISS!!" with vpunch
                        menu:
                            him"THAT W-WASN'T MY F-FIRST KISS!!"
                            "{color=[hatredcolor]}Tease her!{/color}":
                                bo"That was definitely it, judging by your reaction. Hahaha!"
                                call changeHatred(1) from _call_changeHatred_106
                                bo"Having your first kiss with you [him_rel_to_bo]... You are really desperate, aren't you [him_name]?"
                                show hima at smallshake
                                call changeRespect("Himawari", -1) from _call_changeRespect_139
                                him"No one w-would ever kiss you, asshole!"
                                bo"No one would ever kiss YOU! You are lucky I did..."
                                him"*Fuming* Grrrr!!!!" with vpunch

                            "Apologize":
                                bo"I am sure it wasn't..."
                                bo"I apologize, it was just a silly prank, okay? It wasn't even a real kiss, our lips just touched..."
                                call changeObedience("Himawari",1) from _call_changeObedience_90
                                him"Y-you freaking d-dummy! Don't ever try anything like that again!"
                        show hima:
                            easein 2 xpos -1000
                        $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                        him"Hmph! I'll r-remember this..." with vpunch
                        show boruto surprised2 with dissolve
                        bot"Heh, I just... sort of kissed my [him_rel]..."
                        bot"Now that I think about it, that was my first kiss too..."
                        show boruto snob with dissolve
                        bot"Although a shitty one! Maybe next time I'll make it a little bit more interesting..."
                        $ earnhertrust2 = True
                        jump action_taken
                            
                        

                        

                        
                            


                
            $ renpy.sound.play("/audio/soun_fx/hinata/kisscheek.opus", channel="sfx2", loop=False, relative_volume = 0.6)
            show hima_kiss1_1 with dissolve:
                zoom 1.1 xalign 0.0
            him"*Kiss*"
            hide hima_kiss1_1
            show hima_kiss1
            with dissolve
            call changeRespect("Himawari", 2) from _call_changeRespect_140
            him"There, happy now?"
            hide hima_kiss1
            hide blackscreen
            show hima smugshy:
                easein 0.6 xalign 0.8
            with dissolve
            bo"It's nice to see you not being a devil spawn for once..."
            him"Right back at you..."
            "*Both giggling*"
        "{color=[obediencecolor]}I'd be more convinced with a hug!{/color}":
            jump himahugrepeatable
        "Don't worry about it!":
            bo"Don't even worry about it, it's your money now..."
            call changeRespect("Himawari", 3) from _call_changeRespect_141
            him"R-really!? Thank you for this... I'll save it up and help [hin_rel] with it when needed!"
            bo"No worries..."
            show hima smugshy with dissolve
            show hima:
                easein 2 xpos -1000
            him"Anyways, My money now! Yahoooo! I am rich!" with vpunch
            bo"*Sigh*..."
            jump action_taken





    label hima_offermoney_fail:
        show hima smugshy with dissolve
        show boruto surprised2 with dissolve
        him"You are pushing your luck! T-that was an one time thing only..."
        show hima shy with dissolve
        call changeRespect("Himawari", 2) from _call_changeRespect_142
        him"But thank you for this... I'll save it up and help [hin_rel] with it when needed!"
        bo"No worries..."
        show hima smugshy with dissolve
        show hima:
            easein 2 xpos -1000
        him"Anyways, My money now! Yahoooo! I am rich!" with vpunch
        bo"*Sigh*..."
        jump action_taken

    


label himahugrepeatable:
    bo"I'd be more convinced with a hug..."
    bo"I deserve at least that much, no?"
    call checkObedience(7,"hima_offermoney_fail","Himawari") from _call_checkObedience_13
    if himawari_fristhug == True:
        him"Another hug, huh? You've been getting realy touchy touchy lately..."
        him"But I s-suppose I can do that much... Assuming you don't try anything stupid!"
    else:
        default himawari_fristhug = False
        him"A h-hug? Since when are you one for hugs..."
        him"I s-suppose a hug isn't the worst you could ask for..."
        $ himawari_fristhug = True
    show hima:
        easein 0.6 xalign 0.4
    pause 0.4
    scene black with dissolve
    bo"..."
    if day_part == 3:
        show himawari_bedroom_2
    else:
        show himawari_bedroom_1
    show himahug1_1
    with dissolve
    him"Eheh... I am not used to this, and you kinda stink!"
    menu repeatablehug:
        him"Eheh... I am not used to this, and you kinda stink!"
        "Joke around with her":
            default unlockhugdom = False
            $ unlockhugdom = True
            bo"At least I don't stink as much as you do..."
            show himahug1_1 at smallshake
            call changeObedience("Himawari",1,"himahugrepeatable",2) from _call_changeObedience_91
            him"S-stop it, you clown ass bozo... *Giggles*"
            scene black with dissolve
            "The hug only lasted for a second..."
            if day_part == 3:
                show himawari_bedroom_2
            else:
                show himawari_bedroom_1
            show hima smugshy:
                zoom 0.34 xalign 0.4
            show boruto surprised2 at left
            with dissolve
            show hima smugshy:
                easein 0.6 xalign 0.8
            with dissolve
            bo"It's nice to see you not being a devil spawn for once..."
            him"Right back at you..."
            "*Both giggling*"
            him"Don't think I am warming up to you or anything! You are still a shit-stain for what it's worth..."
            call changeRespect("Himawari", 2) from _call_changeRespect_143
            him"But thank you for this... I'll save it up and help [hin_rel] with it when needed!"
            bo"No worries..."
            show hima:
                easein 2 xpos -1000
            him"Anyways, My money now! Yahoooo! I am rich!" with vpunch
            bo"*Sigh*..."
            jump action_taken
        "{color=[dominancecolor]}????{/color}" if unlockhugdom == False:
            "Complete previous options to unlock..."
            jump repeatablehug
        "{color=[lovecolor]}????{/color}" if unlockhugdom == False:
            "Complete previous options to unlock..."
            jump repeatablehug
        "{color=[dominancecolor]}Pull her closer!{/color}" if unlockhugdom == True:
            call checkDominance(5,"repeatablehug") from _call_checkDominance_14
            bo"I stink now, do I..."
            scene black
            bo"Take another whiff then!" with vpunch
            show himadhug1 with dissolve
            call changeObedience("Himawari",1,"himahugrepeatable",4) from _call_changeObedience_92
            him"H-hey... quit messing around!"
            call changeDominance(1,"repeatablehug",2) from _call_changeDominance_66
            bo"Do I stink now too, you devil spawn?" with vpunch
            him"Even worse than before! *Giggles*"
            show himadhug1 with dissolve:
                zoom 1.1 xalign 0.5
            bo"Are you sure about that!?" with vpunch 
            "You playfully pull her closer..."
            him"Okay, o-okay! I get it... You aren't that stinky! *Giggles*"
            him"Only a little bit, Teehe! Now let me go please..."
            menu:
                him"Only a little bit, Teehe! Now let me go please..."
                "Let her go...":
                    scene himadhug1 with dissolve
                    bo"Calling me stinky... Hmph! Know your place little girl! Hehe..."
                    scene black with dissolve
                    if day_part == 3:
                        show himawari_bedroom_2
                    else:
                        show himawari_bedroom_1
                    show hima smugshy:
                        zoom 0.34 xalign 0.4
                    show boruto snob at left
                    if day_part == 3:
                        show himawari_bedroom_2
                    else:
                        show himawari_bedroom_1
                    with dissolve
                    show hima:
                        easein 0.6 xalign 0.8
                    him"I am just messing with ya!"
                    him"Teehee!"
                    bo"You little shit..."
                    call changeRespect("Himawari", 2) from _call_changeRespect_144
                    show hima smugshy with dissolve
                    him"But thank you for the money! I'll save it up and help [hin_rel] with it when needed!"
                    bo"No worries..."
                    show hima:
                        easein 2 xpos -1000
                    him"Anyways, My money now! Yahoooo! I am rich!" with vpunch
                    bo"*Sigh*..."
                    $ earnhertrust2 = True
                    jump action_taken
                "{color=[dominancecolor]}Make an inconspicuous move...{/color}":
                    scene himadhug1 with dissolve
                    bot"I wanna see how she reacts to this..."
                    scene himadhug1_1 with dissolve
                    bo"Calling me stinky... Hmph! Know your place little girl! Hehe..." with vpunch
                    scene himadhug1_1 with dissolve:
                        zoom 1.1 xalign 0.5 yalign 0.0 
                    him"*Gasps*..."
                    "You dropped your hand down on her ass..."
                    show himahug grope1 with dissolve
                    himt"I-is he touching m-my behind?!" with vpunch
                    bot"So firm... I get the urge to-"
                    scene black
                    him"H-hey!"with vpunch
                    if day_part == 3:
                        show himawari_bedroom_2
                    else:
                        show himawari_bedroom_1
                    show hima mad:
                        zoom 0.34 xalign 0.4
                    show boruto surprised2 at left
                    with dissolve
                    show hima:
                        easein 0.6 xalign 0.8
                    bo"Huh... What's wrong all of a sudden!?"
                    him"D-don't play stupid! You know what you did..." with vpunch
                    bo"W-what are you talking about... the h-hug?"
                    show hima worried2 with dissolve
                    himt"Could he really have done it by accident...?"
                    show hima at smallshake
                    him"Not the hug you idiot...Hmph! W-whatever..."
                    call changeRespect("Himawari", 1) from _call_changeRespect_145
                    him"T-thanks for the money I suppose..."
                    bo"No worries..."
                    show hima:
                        easein 2 xpos -1000
                    him"*Mutters under her breath*..." with vpunch
                    show boruto snob with dissolve
                    bot"Hehe! She is so easy to fuck around with..."
                    $ earnhertrust2 = True
                    jump action_taken
                "{color=[hatredcolor]}Grope her ass!{/color}":
                    if forcegrope_1sttime == False:
                        scene himadhug1 with dissolve
                        bot"I've had it with her!"
                        scene himadhug1_1 with dissolve
                        bo"Calling me stinky... Hmph! Know your place little girl! Hehe..." with vpunch
                        scene himadhug1_1 with dissolve:
                            zoom 1.1 xalign 0.5 yalign 0.0 
                        him"*Gasps*..."
                        "You dropped your hand down on her ass..."
                        show himahug grope1 with dissolve
                        himt"I-is he touching m-my behind?!" with vpunch
                        show hima_gropeass_hug with dissolve
                        $ renpy.sound.play("/audio/soun_fx/himawari/kyaa.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                        bot"So firm... I just need to give it a little squeeze!"
                        scene black
                        him"S-stop that right now!"with vpunch
                        if day_part == 3:
                            show himawari_bedroom_2
                        else:
                            show himawari_bedroom_1
                        show hima mad:
                            zoom 0.34 xalign 0.4
                        show boruto surprised2 at left
                        with dissolve
                        show hima:
                            easein 0.6 xalign 0.8
                        bo"Huh... What's wrong all of a sudden!?"
                        call changeRespect("Himawari", -5) from _call_changeRespect_146
                        him"D-don't play stupid! You just g-grabbed m-my... m-my..." with vpunch
                        show boruto sceeming2 with dissolve
                        bo"Your ass? Yeah, because you called me stinky!"
                        call changeHatred(1) from _call_changeHatred_107
                        bo"It's you and your ass that stinks, bitch!"
                        show hima at smallshake
                        him"You are the absolute w-worst! I thought you were being nice lately..."
                        show hima at smallshake
                        him"Turns out you were just being a perv all along!"
                        call changeRespect("Himawari", -6) from _call_changeRespect_147
                        him"To h-hell with you, and your money!"
                        show hima:
                            easein 2 xpos -1000
                        him"I am telling [hin_rel] you are being all weird and perverted!" with vpunch
                        show boruto snob with dissolve
                        bot"Oops, might have gone too far, too fast..."
                        show boruto sceeming2 with dissolve
                        bot"But it was worth it! That ass will be mine soon enough anyway..."
                        default forcegrope_1sttime = False
                        $ forcegrope_1sttime = True
                        $ gropeapology = False
                        $ earnhertrust2 = True
                        jump action_taken
                    else:
                        scene himadhug1 with dissolve
                        bot"Another excuse to grab that ass!!"
                        scene himadhug1_1 with dissolve
                        bo"Calling me stinky... Hmph! I though I told you..." with vpunch
                        him"*Gasps*..."
                        "You dropped your hand down on her ass..."
                        show himahug grope1 with dissolve
                        bo"Know your place, little girl!" with vpunch
                        him"C-cut it out! You retard..." with vpunch
                        show hima_gropeass_hug with dissolve
                        $ renpy.sound.play("/audio/soun_fx/himawari/kyaa.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                        bo"Not before you apologize!" with vpunch
                        scene black
                        him"S-stop that right now!"with vpunch
                        if day_part == 3:
                            show himawari_bedroom_2
                        else:
                            show himawari_bedroom_1
                        show hima mad:
                            zoom 0.34 xalign 0.4
                        show boruto surprised2 at left
                        with dissolve
                        show hima:
                            easein 0.6 xalign 0.8
                        bo"Here we go again..."
                        call changeRespect("Himawari", -5) from _call_changeRespect_148
                        him"You just g-grabbed m-my... m-my..." with vpunch
                        show boruto sceeming2 with dissolve
                        bo"Your ass? Yeah, because you called me stinky!"
                        call changeHatred(1) from _call_changeHatred_108
                        bo"I thought I told you to stay in your lane!"
                        show hima at smallshake
                        him"You are the absolute w-worst! I was wrong to trust you again!"
                        show hima at smallshake
                        him"Turns out you were just being a perv again!"
                        call changeRespect("Himawari", -6) from _call_changeRespect_149
                        him"To h-hell with you, and your money!"
                        show hima:
                            easein 2 xpos -1000
                        him"I am telling [hin_rel] you are being all weird and perverted!" with vpunch
                        show boruto snob with dissolve
                        bot"Oops, might have gone too far, too fast..."
                        show boruto sceeming2 with dissolve
                        bot"But it was worth it! That ass will be mine soon enough anyway..."
                        $ forcegrope_1sttime = True
                        $ gropeapology = False
                        $ earnhertrust2 = True
                        jump action_taken
                




        "{color=[lovecolor]}Pull her closer...{/color}" if unlockhugdom == True:
            bo"I stink now, do I..."
            scene black with vpunch
            call checkLove(4,"hima_faillovehug","Himawari") from _call_checkLove_4
            if day_part == 3:
                show himawari_bedroom_2
            else:
                show himawari_bedroom_1
            show himahug2t with dissolve
            him"O-oh..."
            bo"At least know that this stinky [him_rel_to_bo] cares about you, okay?"
            him"I..."
            scene black with dissolve
            call changeLove("Himawari",1,"hima_hug_love1") from _call_changeLove_41
            him"I know you do..."
            show himahug2_1 with dissolve
            "[him_name] pulled her self closer and tightly wrapped her arms around your neck..."
            bo"O-oh!"
            him"T-thank you, for everything you've been doing lately..."
            menu:
                him"T-thank you, for everything you've been doing lately..."
                "Don't even mention it...":
                    bo"Don't even mention it..."
                    him"What if..."
                    show hima_kiss1 with dissolve
                    him"...I want to mention it!"
                    $ renpy.sound.play("/audio/soun_fx/hinata/kisscheek.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                    show hima_kiss1_1 with dissolve:
                        zoom 1.1 xalign 0.0
                    him"*Kiss*"
                    hide hima_kiss1_1
                    show hima_kiss1
                    with dissolve
                    call changeRespect("Himawari", 3) from _call_changeRespect_150
                    him"Although you still smell, and you are ugly..."
                    him"But at least you aren't what I thought you were..."
                    if day_part == 3:
                        show himawari_bedroom_2
                    else:
                        show himawari_bedroom_1
                    show hima smugshy:
                        zoom 0.34 xalign 0.4
                    show boruto snob at left
                    if day_part == 3:
                        show himawari_bedroom_2
                    else:
                        show himawari_bedroom_1
                    with dissolve
                    show hima:
                        easein 0.6 xalign 0.8
                    him"Teehee!"
                    bo"You little shit..."
                    show hima smugshy with dissolve
                    him"And thank you for the money! I'll save it up and help [hin_rel] with it when needed!"
                    bo"No worries..."
                    show hima:
                        easein 2 xpos -1000
                    him"Anyways, My money now! Yahoooo! I am rich!" with vpunch
                    bo"*Sigh*..."
                    $ earnhertrust2 = True
                    jump action_taken



                
                "{color=[obediencecolor]}Make a move...{/color}":
                    bo"Anything for you and [hin_rel]..."
                    show himahug2_2 with dissolve
                    bo"Let me know if you need anything more, okay?"
                    himt"Is h-he...!"
                    show himahug grope1 with dissolve
                    "You inconspicuously dropped your arm on her ass..."
                    call changeObedience("Himawari",1,"gropehima_hug1",1) from _call_changeObedience_93
                    himt"Is he t-touching me d-down there!?"
                    scene black with vpunch
                    him"O-okay, I g-got it..."
                    himt"P-probably by accident... I hope at least..."
                    if day_part == 3:
                        show himawari_bedroom_2
                    else:
                        show himawari_bedroom_1
                    show hima worried2:
                        zoom 0.34 xalign 0.4
                    show boruto snob at left
                    if day_part == 3:
                        show himawari_bedroom_2
                    else:
                        show himawari_bedroom_1
                    with dissolve
                    show hima:
                        easein 0.6 xalign 0.8
                    him"T-thanks for c-caring... and the money of course..."
                    call changeRespect("Himawari", 1) from _call_changeRespect_151
                    bo"No worries..."
                    show hima:
                        easein 2 xpos -1000
                    show boruto surprised2 with dissolve
                    bot"She didn't even mention it!"
                    bot"Am I finally getting somewhere with her?"
                    show boruto snob with dissolve
                    bot"Hmm... I wonder how far could I push my luck with her..."
                    $ earnhertrust2 = True
                    jump action_taken

                
                
            


            label hima_faillovehug:
                if day_part == 3:
                    show himawari_bedroom_2
                else:
                    show himawari_bedroom_1
                show himahug2t with dissolve
                him"H-hey!"
                bo"At least know that this stinky [him_rel_to_bo] cares about you, okay?"
                him"*Giggles* R-relax big guy!"
                him"What do you think gives you the right to get this close to me, hm?"
                him"Has my kindness gotten to your head?"
                bo"N-no, I..."
                scene black with vpunch
                him"Teehee!"
                if day_part == 3:
                    show himawari_bedroom_2
                else:
                    show himawari_bedroom_1
                show hima smugshy:
                    zoom 0.34 xalign 0.4
                show boruto surprised2 at left
                with dissolve
                show hima:
                    easein 0.6 xalign 0.8
                him"I am just messing with ya!"
                show hima worried2 with dissolve
                call changeLove("Himawari",1,"hima_failhug") from _call_changeLove_42
                him"But... t-thank you... for c-caring!"
                bo"Of course..."
                call changeRespect("Himawari", 2) from _call_changeRespect_152
                show hima smugshy with dissolve
                him"And thank you for the money! I'll save it up and help [hin_rel] with it when needed!"
                bo"No worries..."
                show hima:
                    easein 2 xpos -1000
                him"Anyways, My money now! Yahoooo! I am rich!" with vpunch
                bo"*Sigh*..."
                $ earnhertrust2 = True
                jump action_taken

                

        

    
label repeatable_blindfold:
    default blindfoldintroduction = False
    
    if blindfoldintroduction == False:
        $ blindfoldintroduction = True
        show boruto sceeming with dissolve
        bot"I've just had an incredibly risky idea pop into my mind, but if it pays off..."
        show boruto snob with dissolve
        bo"Yeah, I was thinking there's something you could help me with..."
        him"Oooh? And why would I help you in the first place..."
        bo"Because there may be something in it for you too!"
        him"Do tell!"
        bo"Remember the restaurant I work at?"
        him"Yeah, you've been going on about it non-stop. What of it..."
        bo"I already told you I've been earning the trust of the owner there..."
        bo"What I didn't tell you is that wants me to pick up more responsibilities, for more money..."
        bo"In fact, he asked me to come up with some new menu items..."
        show hima shy with dissolve
        him"Did he now..."
        bo"You see, I've been working on a recipe of mine for a while now. It's almost ready now but..."
        bo"I thought I could run it by you before I finalize it..."
        him"M-me...? You think I could help with that?"
        bo"Seeing how you eat all freaking day, I think you just might be the perfect person for the job..."
        show hima worried2 with dissolve
        him"I eat because of my training, you dummy..."
        show hima smugshy with dissolve
        him"My diet is extremely meticulous, I wouldn't wanna ruin it with your crappy recipes..."
        him"So how are you going to make it worth my while..."
        bo"First of all, this recipe is heavy on protein, which means it's right up your alley!"
        show hima at smallshake
        him"Hmm... And what else?"
        bo"I'll make this fun for you..."
        bo"All you have to do is perform a blind taste test on my recipe. You are to give your honest opinion on what you think could be improved, as well as what ingredients you think are used..."
        bo"If you can correctly guess the ingredients, I'll even pay you a $100!"
        show hima shy with dissolve
        him"A h-hundred!?" with vpunch
        him"C-can you even a-afford that...?"
        bot"I can't, but there's no way you are guessing what I am having you taste..."
        bo"Sure can!" with vpunch
        bo"So what do you think? It's a win win for you..."
        bo"You get to help me potentially make more money by perfecting my recipe, and there's a chance you get paid for it as well!"
        show hima worried2 with dissolve
        him"I am in!" with vpunch
        him"T-tell me what do I h-have to do..."
        bo"Give me some time to prepare everything I need for the test first and I'll talk to you soon, okay?"
        him"Y-yeah..."
        hide boruto with dissolve
        hide hima with dissolve
        $ blindfoldinv = inventory.find_item_by_name("Blindfold")
        if blindfoldinv!= None:
            bot"I already have the blindfold ready... I'll prepare the ingredients and talk with her again about this!"
        else:
            bot"I am going to need a blindfold for this to work, I should check the shop first..."
        scene black with dissolve
        jump action_taken
    else: #blindfold start

        if blindfoldrepeat == 1:
            show boruto snob with dissolve
            bo"Ready to have another go at the blind taste test?"
            if himawari_respect >= 0:
                show hima happy with dissolve
                him"Oh that!"
                him"Uhm... Sure!"
                him"Don't forget your promise... Today will be my payday!"
                bo"You are supposed to be helping first, money comes later..."
                him"Yea yeah, whatever... Bring it on!"
                show boruto:
                    easein 1 xalign 0.6
                bo"Not so fast... You'll have to put this on first."
                label replay_blindfoldtaste2:
                $ initialize_replay_defaults()
                scene black with dissolve
                bo"I need a moment to make the necessary preparations..."
                show himablindfold 1_1 with dissolve
                him"Let me know when you are ready!"
                bot"There she goes again..."
                bot"My innocent little [him_rel] sitting on her knees..."
                call increaselust(10) from _call_increaselust_101
                $ renpy.sound.play("/audio/soun_fx/heartbeatlong.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                bot"My heart is already beating like crazy..."
                show himablindfold with dissolve:
                    alpha 0.2
                show boruto_blindfold_cut with dissolve:
                    xpos -0.2 ypos -0.36
                bot"So blissfully unaware of my machinations..."
                hide boruto_blindfold_cut
                show himablindfold:
                    alpha 1
                with dissolve
                bo"Alright, you ready?"
                him"Y-yeah!" with vpunch
                bo"Scooch over towards me then..."
                scene black with dissolve
                him"One sec..."
                him"Is here fine...?"
                show screen parallax1280("hima_finalbefore",1.25,0.0) with dissolve
                call showscrollingimage from _call_showscrollingimage_55
                him"Aaahh..."
                call increaselust(10) from _call_increaselust_102
                bo"Yeah, t-that'll do nicely..."
                bo"This time, we will of course skip straight to my secret recipe since you already proved that your palate is fairly competent..."
                bo"The same rules from last time still apply... Do you remember those?"
                show screen parallax1280("hima_finalbefore_angry",1.25,0.0) with dissolve
                him"Uh-uh... No biting!"
                him"Although I am curious why that is... What kind of food am I supposed to judge if I can't even chew on it!"
                bo"W-well... Uh..." with vpunch
                bo"You can think of something similar to an ice cream. You wouldn't bite an ice cream, would you?"
                him"Hmm..."
                bo"Besides, this is my only p-prototype, and it's expensive!"
                bo"You better not ruin it, or you are paying for it out of your pocket..."
                call hidescrollingimage("Click twice to begin the taste test...") from _call_hidescrollingimage_56
                scene black with dissolve
                him"Ha! Knowing you, it's probably worth less than the air we breathe..." with vpunch
                show hima_drool00 with dissolve:
                    xalign 0.0 zoom 0.53
                him"Come on then, let me have a taste..."
                show hima_finalbefore2 with dissolve:
                    ypos -0.50
                $ renpy.sound.play("/audio/soun_fx/heartbeatlong.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                bo"Right... Remember, no biting!"
                him"There it is... That same musky smell as last time!"
                bo"...M-musky!?" with vpunch
                him"Y-yeah! But not particularly unpleasant. Just... weird, or unfamliar..."
                bo"R-right..."
                bo"Start slow, give it a few licks and describe the taste..."
                him"Mhm..."
                hide hima_finalbefore2 with dissolve
                bot"F-fuck... Here goes nothing!"
                show hima_drool00:
                    alpha 0.20
                show hima_liclharden1:
                    xalign 1.0 zoom 0.65 xzoom -1
                with dissolve
                $ renpy.sound.play("/audio/soun_fx/lickpenis1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                him"Mh...mhm... *Reluctant licks*..."
                bot"F-fuck... She is actually tasting it!"
                bot"My little [him_rel] is tasting my cock and she has no idea!"
                $ renpy.sound.play("/audio/soun_fx/lickpenis1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                call increaselust(10) from _call_increaselust_103
                him"Mm..."
                "The texture was unlike anything [him_name] anticipated. It was fleshy, warm, and pulsating as if it were alive..."
                "Her demeanor quickly turned timid as the taste slowly registered - Salty, musky, but wholly unfamiliar to her..."
                scene black with dissolve
                "She pulled back after a few more exploratory licks..."
                show hima_finalbefore2 with dissolve:
                    ypos -0.50
                bo"S-so...? First opinions?"
                him"I..."
                him"I don't know! it was..."
                him"Kind of warm, a bit salty, and with a... strong, earthly odor..."
                bo"E-earthly, huh...?" with vpunch
                him"Y-yeah... Like a... strange vegetable. Artificially sweetened or something!"
                him"Whatever it is, it's intense, but I am not sure if I like it or not..."
                him"...Yet"
                bo"You see... My recipe is quite special in that regard..."
                him"Is it now..."
                bo"The more you taste of it, the more intense it can get..."
                bo"Perhaps another try can help you figure it out..."
                him"S-sure! I was planning on it anyway..."
                him"I am still eyeing the prize money you know!"
                bo"*Nervous laughter* Heh-he... You are getting ahead of yourself..."
                bo"...H-here it comes!"
                scene black with dissolve
                him"Aaaah..."
                show hima_liclharden1 with dissolve:
                    xalign 0.0 zoom 0.65 xzoom -1
                show hima_liclharden2 with Dissolve(1):
                    xalign 0.0 zoom 0.65 xzoom -1
                $ renpy.sound.play("/audio/soun_fx/lickpenis1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                him"Mh...mhm... *Indulging licks*..."
                call increaselust(10) from _call_increaselust_104
                bot"F-fuck, I am growing hard as diamonds just by feeling her tongue circling around the glans..."
                bot"I don't think I can hold out much longer... This whole ordeal is way too arousing!"
                $ renpy.sound.play("/audio/soun_fx/lickpenis1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                himt"This t-taste is..."
                him"Mh...mhm... *Indulging licks*..."
                himt"Feels slimy and yucky, but..."
                hide hima_liclharden1
                show hima_liclharden2:
                    alpha 0.3
                show hima_liclharden3:
                    xalign 1.0 zoom 0.65 xzoom -1
                with dissolve
                himt"It's sort of... growing on me!"
                call increaselust(20) from _call_increaselust_105
                bot"F-fuck! I am rock hard! Looking down at her gazing towards my cock with her little tongue hanging out her mouth..."
                call increaselust(20) from _call_increaselust_106
                bot"A few more touches and I am going to lose all control!"
                bot"I need a break, otherwise I'll explode right on her f-face..."
                him"Hmm..."
                bo"A-are you done tasting it?"
                him"I think I need..."
                show hima_liclharden4 with dissolve:
                    xalign 1.0 zoom 0.65 xzoom -1
                $ renpy.sound.play("/audio/soun_fx/lickpenis1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                him"One last taste before I lock in my answer..."
                "[him_name] indulged one last time. This time, she made sure to garner as much information as she could by having her tongue spread around the entire surface of what she was tasting..."
                bo"W-wait, No! Hold on a s-second!" with flash
                scene hima_liclharden4 with flash:
                    zoom 1.55 xalign 0.5 yalign 1.0 xzoom -1
                $ renpy.sound.play("/audio/soun_fx/lickpenis1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                "She raised her hand and reached for it..." with flash
                show hima_liclharden4:
                    easein 2 yalign 0.1
                show layer master at dizzyflashshort
                bo"W-wait, stop!" with vpunch
                bot"F-fuck! W-what is she doing!?"
                scene hima_liclharden4 with flash:
                    zoom 1.55 xalign 0.5 yalign 1.0 xzoom -1
                bot"I am about t-to..." with vpunch
                him"What's wrong...?"
                scene hima_liclharden4 with flash:
                    zoom 1.55 xalign 0.5 yalign 0.5 xzoom -1
                $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                scene black with longerflash
                call decreaselust(100) from _call_decreaselust_79
                bot"F-fuck...!"
                him"H-huh... What's that on my..."
                $ renpy.sound.play("/audio/soun_fx/heartbeatlong.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                bot"F-fuck!" with vpunch
                show cumhand with dissolve
                show layer master at dizzyflashshort
                bot"That was... c-close!"
                "You quickly backed off, pulled your pants up, and and tried to prevent any of your expulsion from hitting [him_name]'s face as you knew that would raise suspicion. But..."
                show hima_cumtaste0 with dissolve:
                    zoom 1.1 xalign 0.5 yalign 1.0
                him"W-what just happened! And..."
                show hima_cumtaste0:
                    easein 0.8 yalign 0.1
                him"W-what's this on my face..." with vpunch
                "But one small speckle went through your attempt to stop it, and landed straight on [him_name]'s cheek..."
                bot"F-fuck! But it's just a tiny amount..." with vpunch
                bot"Hopefully it isn't enough to tip her off..."
                bo"I saw you reaching over with your hand, you almost broke the r-rules!"
                him"I didn't! I was just looking for some support to brace myself!" with vpunch
                him"I was trying to get a better taste of it!" with vpunch
                bo"Whatever that was, we agreed on no h-hands!"
                scene black with dissolve
                "You made sure to cover up the scene of the crime while explaining yourself..."
                bo"Because of that, I p-panicked and accidentally spilled some of my... secret syrup on your fa-"
                show hima_cumtaste1 with vpunch:
                    zoom 0.6
                him"You mean... this?" with vpunch
                "[him_name] pushed the tiny amount of 'syrup' from her cheek onto her tongue..."
                show cutout_bo1 with dissolve:
                    xalign 1.0 yalign 0.0
                show hima_cumtaste1 with dissolve:
                    alpha 0.3
                bot"S-shit! I thought she would just clean that off..."
                show cutout_bo1:
                    alpha 0.3
                show hima_cumtaste2:
                    zoom 0.6
                $ renpy.sound.play("/audio/soun_fx/swallow.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                him"*Gulp*" with vpunch
                hide hima_cumtaste1
                show hima_cumtaste2:
                    alpha 0.3
                show cutout_bo1:
                    alpha 1.0
                with dissolve
                bot"Did she just... swallow my cum!?"
                show hima_cumtaste2:
                    alpha 1.0
                show cutout_bo1:
                    alpha 0.3
                with dissolve
                him"Secret syrup... huh?"
                show hima_cumtaste3 with vpunch:
                    zoom 0.6
                hide hima_cumtaste2
                him"It was... mildly interesting! Nothing more, nothing less..."
                bot"W-wait a second..."
                show hima_cumtaste3:
                    alpha 0.3
                show cutout_bo2:
                    xalign 1.0 yalign 0.0
                with dissolve
                bo"Mildly... interesting?"
                bo"You mean... you didn't hate the taste of it?"
                bot"More importantly, she doesn't have any idea what it is!" with vpunch
                show hima_cumtaste2:
                    alpha 1.0 zoom 0.6
                show cutout_bo2:
                    alpha 0.3
                show cutout_bo1:
                    alpha 0.0
                with dissolve
                him"...Hate the taste of it? I thought this was your super secret tasty recipe or something! Why would your first thought be that..."
                show hima_cumtaste3:
                    alpha 0.0
                show hima_cumtaste2:
                    alpha 0.3
                show cutout_bo2:
                    alpha 0.0
                show cutout_bo1:
                    alpha 1.0
                with dissolve
                bo"*Ahem* Y-you know... With you hating everything that isn't overly sweet, I just thought you'd have trouble with this one..." with vpunch
                show hima_cumtaste2:
                    alpha 1.0
                show cutout_bo1:
                    alpha 0.3
                with dissolve
                him"No trouble at all. I even found the taste interesting as I said before..."
                him"It's just... the quantity of the syrup was just too little to form a definitive opinion on that part..."
                show hima_cumtaste2:
                    alpha 0.3
                show cutout_bo1:
                    alpha 1.0
                with dissolve
                bo"It was..."
                show cutout_bo2 with dissolve:
                    alpha 1.0
                bo"...too little?"
                show hima_cumtaste2:
                    alpha 1.0
                show cutout_bo2:
                    alpha 0.3
                hide cutout_bo1
                with dissolve
                him"Y-yeah... You said you wanted feedback on your recipe, didn't you?"
                show hima_cumtaste3 zorder 1000 with dissolve:
                    alpha 1.0
                him"There's my feedback!" with vpunch
                him"Add more syrup!" with vpunch
                hide hima_cumtaste2
                show hima_cumtaste3:
                    alpha 0.3
                show cutout_bo2:
                    alpha 1.0
                with dissolve
                bo"More syrup, eh?"
                show cutout_bo3:
                    xalign 1.0 yalign 0.0
                bo"That should be an easy fix!" with vpunch
                bo"I'll refine my recipe based on your valuable feedback, thanks [him_name]!"
                scene black with dissolve
                bot"This is so surreal. My plan is coming along better than I ever anticipated it could..."
                bot"All my suspicions regarding [him_name] were true! She really is utterly clueless..."
                show hima_drool2_shy with dissolve:
                    xalign 0.0 zoom 0.53
                him"H-hey! We aren't done yet, are we?" with vpunch
                him"There's still the guessing part left..."
                show cutout_bo1 with dissolve:
                    xalign 1.0 yalign 0.0
                bo"Oh r-right. Sorry, I got caught up on improving my recipe..."
                hide cutout_bo1
                show hima_drool1:
                    xalign 1.0 zoom 0.52
                show hima_drool2_shy:
                    alpha 0.2
                with dissolve
                him"So can I have another taste before I take my guess..." with vpunch
                call increaselust(10) from _call_increaselust_107
                scene hima_drool1:
                    zoom 1.22 yalign 1.0
                show hima_drool1:
                    easein 5 yalign 0.2
                bot"My h-heavens... She's already looking like a cock-craving fiend, and she doesn't even know about it!"
                bot"But it would be too risky to keep this going right now..."
                bot"My hand is still covered in cum... Besides, I need some time to recharge!"
                call showscrollingimage from _call_showscrollingimage_56
                show screen parallax1280("hima_drool1",1.22,1.0)
                with dissolve
                bo"[him_name]... I'd love to give you another taste at it, but you are going to have to wait until next time..."
                bo"The prototype is getting cold, and it's losing its tasty culinary properties too after all this time. Besides, I have to refine it based on your observations..."
                hide screen parallax1280
                show screen parallax1280("hima_drool2_shy",1.22,0.2)
                with dissolve
                him"Mmmmm! *Disgruntled remark*"
                bo"You can still take a shot at guessing what it was of course!"
                show hima_drool2_shy:
                    zoom 1.22 yalign 0.2
                call hidescrollingimage from _call_hidescrollingimage_57
                $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                him"Hmph! Fine..." with vpunch
                bo"You have until I am back to lock in your guess..."
                bo"Gotta hide my secret recipe!"
                him"Sure..."
                $ renpy.sound.play("/audio/soun_fx/doorclose.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                bot"And clean up of course, hehe!"
                show bg day:
                    zoom 0.69
                show boruto snob at center with dissolve
                bot"I can't believe this stupid ass plan of mine worked so brilliantly!"
                bot"I may be a freaking genius, or..."
                bot"More than likely, It's just [him_name] being too innocent for her own good..."
                if hatred >= 30:
                    call borutoevil2 from _call_borutoevil2_18
                    bot"Now that I've confirmed my suspicions, she's mine to toy around with as I please!"
                    call changeHatred(1) from _call_changeHatred_115
                    bot"Why not, take advantage of that innocence after all..."
                    bot"She's been acting like a bitch to me for so long! It's nigh time she reaps what she sowed..."
                elif himawari_love >= 3:
                    show boruto worried2 with dissolve
                    bot"It feels...wrong, taking advantage of her innocence like that..."
                    bot"But... there's no harm in it, is there? It's not like she gets nothing out of it..."
                    bot"Besides, she even seems to enjoy the fact that I involve her in more things..."
                    bot"Even if those things are products of my perversion..."
                    bot"Bah! The more I think about it the more I realize how insane it all sounds..."
                else:
                    bot"So what if I take some advantage of that..."
                    bot"It's not like I am harming her or anything..."
                    bot"Besides, she seems to be enjoying the fact that I involve her in things..."
                    bot"Even if those things are a product of my perversion... Hehe!"
                show boruto normal with dissolve
                bot"In any case, enough time has passed..."
                scene black with dissolve
                bot"I should head back in there..."
                $ renpy.sound.play("/audio/soun_fx/dooropen.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                show himablindfold 1_1 with dissolve
                him"Is t-that you?"
                bo"Yeah, but... Why are you still wearing the blindfold?"
                show himablindfold 1 with fade
                him"I just... don't want you to think I am cheating!" with vpunch
                him"That way you don't find a stupid excuse to weasel your way out of our deal when I evidently win the prize!"
                menu:
                    him"That way you don't find a stupid excuse to weasel your way out of our deal when I evidently win the prize!"
                    "{color=[hatredcolor]}(Obedient little whore!){/color}" if hatred>=25:
                        bot"That's my obedient little whore! Little does she know..."
                        call changeHatred(1) from _call_changeHatred_116
                        bot"She'll never even have a chance to win that money. All she'll get instead is my cock down her throat! Hehehe..."
                        bo"Something's telling me you won't be winning that money any time soon... Hehe!"
                        $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                        him"Hmph! We'll see about that!" with vpunch
                    "{color=[dominancecolor]}Tease her{/color}" if dominance>=15:
                        bo"If I didn't know you any better, I'd think you are some kind of a bastion of morality!"
                        call changeDominance(1) from _call_changeDominance_67
                        bo"Sitting there like an obedient little girl really paints a different picture than the typical demon-act you like to put on! Hehe..."
                        him"S-shut up, stupid..." with vpunch
                    "'Smart girl!'":
                        bo"Smart girl! Although I would never cheat you out of your hard-earned money..."
                        call changeRespect("Himawari", 1) from _call_changeRespect_159
                        him"Teehee! You bet!"
                him"Can I take the blindfold off now?"
                scene black with dissolve
                bo"Sure..."
                if day_part == 3:
                    show himawari_bedroom_2
                else:
                    show himawari_bedroom_1
                show hima shy at right:
                    zoom 0.34
                with dissolve
                him"At last, let there be light!"
                show boruto snob at left with dissolve
                bo"So... Do you have a guess as to what that was?"
                show hima smugshy with dissolve
                him"Hee-heee.... Not only do I have a guess..."
                him"I have the exact answer down to the T!"
                show boruto surprised2 with dissolve
                bo"Y-you do...?"
                show hima at smallshake
                him"Of course!"
                him"The wet, slimy feel of it... The lumpy texture..."
                bot"She can't possibly..."
                him"It was a sweetened corn stick infused with that syrup you spilled on me..." with vpunch
                him"Wasn't it!?" with vpunch
                show boruto laughing2 with dissolve
                bo"Bw...Bwahahahaha!" with vpunch
                show hima embarassed with dissolve
                him"..."
                show hima at smallshake
                him"...Am I wrong?"
                bo"I can't believe I was scared there for a second..."
                show hima worried2 with dissolve
                show boruto at smallshake
                bo"Bwahaha..."
                him"H-hey... cut it out!"
                show boruto snob with dissolve
                bo"I am s-sorry! Haha... You are just so far off It made me burst into laughter!"
                show hima mad with dissolve
                him"How do I know you aren't playing me off!" with vpunch
                show hima at smallshake
                him"For all I know, you could be lying to weasel your way out of paying me!"
                bo"Come on... Think about it for a second. You said it had a lumpy texture..."
                bo"Which you aren't wrong about, but... Would a corn cob really feel like what you've tasted?"
                show hima worried2 with dissolve
                him"Hmph! M-maybe not..."
                himt"D-damn it! I thought I had that..."
                him"...Will I have another c-chance to try that then?"
                bot"Are you kidding me!?"
                bo"Of course you will...!" with vpunch
                bo"After I incorporate your helpful advice into the refinement of my recipe!"
                bo"Thanks for your insight!"
                him"Y-you are welcome..."
                call changeRespect("Himawari",1) from _call_changeRespect_160
                him"Thanks for valuing my opinion, I suppose..."
                show boruto:
                    easein 1.5 xpos -800
                bo"Don't sweat it! I'll see you soon..."
                scene black with dissolve
                bot"I can't fathom how well this is going..."
                bot"Our next session will surely be interesting..."
                $ renpy.end_replay()
                $ blindfoldrepeat = 2
                jump action_taken


            else:
                him"Oh that..."
                him"No, I am not in the mood for it..." with vpunch
                show boruto surprised2 with dissolve
                bo"W-what? Why... what happened? Don't you want another go at the prize money?"
                call checkRespect(0,"Himawari") from _call_checkRespect_2
                him"Something's telling me that money may not even be real at all... Not to mention how weird you've been acting lately..."
                bo"What? Of course it's real..."
                him"Hmph! Talk to me about it some other time and I might reconsider..."
                show boruto snob with dissolve
                bot"Damn it! So close..."
                show boruto normal with dissolve
                bo"I understand. Don't worry about it, we can go at your pace..."
                him"Mhmm... I'll talk to you later I guess..."
                hide hima with dissolve
                scene black with dissolve
                jump action_taken


        bo"Are you ready to help with my recipe?"
        show hima worried2 with dissolve
        show hima at smallshake
        him"Oh, that..."
        him"Uhmm, sure. Just tell me what you need me to do..."
        show boruto snob with dissolve
        bo"For starters..."
        show boruto:
            easein 1 xalign 0.4
        bo"You are gonna have to wear this..."
        $ blindfoldinv = inventory.find_item_by_name("Blindfold")
        if blindfoldinv!= None:
            call useItem(blindfold,1) from _call_useItem_5
        else:
            show boruto embarassed with dissolve
            bo"Wait... S-shit! I forgot the blindfold..." with vpunch
            show hima mad with dissolve
            him"W-what do you mean you forgot the blindfold you idiot! That's the whole point of a blind taste test..."
            bo"Hahaha *Awkward laughter*..."
            show boruto:
                easein 1 xpos -1000
            bo"Y-you are right, I am sorry! I'll be back some time soon..."
            show hima at smallshake
            him"Stop wasting my time, you clown ass spiky head!"
            hide hima with dissolve
            him"Hmph!"
            scene black with dissolve
            bot"I should check the shop and purchase a blindfold..."
            jump action_taken
            
        him"A b-blindfold, huh..."
        him"I guess they don't call it a blind taste test for nothing..."
        bo"You are not as stupid as I thought you were... Hehe!"
        show hima mad with dissolve
        him"Cut it out or I am quiting the job on the spot..."
        show boruto embarassed with dissolve
        bo"I am only joking of course, relax..."
        show hima worried2 with dissolve
        $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
        him"Hmph!"
        show boruto normal with dissolve
        him"...So, I just have to wear this?"
        bo"Yep. I'll prepare the ingredients, you sit here and wait for me, alright?"
        hide boruto with dissolve
        show hima shy with dissolve
        him"W-will do..."
        scene black with dissolve
        "You quickly pick up a few household food items to prepare for the blind taste test..."
        show bg day:
            zoom 0.69
        show boruto sceeming at center with dissolve
        bot"Hehehe... This is going exactly according to plan!"
        show boruto:
            easein 1.5 xpos 1300
        label replay_blindfoldtaste1:
        $ initialize_replay_defaults()
        if _in_replay:
            $ himawari_respect = 5
        scene black with dissolve
        "You make your way back to [him_name]'s bedroom"
        bot"D-damn!" with vpunch
        show himablindfold 1_1 with dissolve
        bot"S-she's looking so... p-pretty, sitting there like that."
        bot"The way she innocuously sits on her legs like that with her skimpy shorts and her bare feet hanging out..."
        call increaselust(20) from _call_increaselust_98
        bot"Why sit on the floor in the first place..."
        bot"But I am not complaining. She is... k-kinda cute!"
        him"H-hey!" with vpunch
        him"I can hear you walking around... Why are you s-saying nothing?"
        bo"O-oh, sorry!" with vpunch
        bo"I was just p-preparing my ingredients..."
        bo"And by the way, you are facing the wrong way..."
        him"Oh, oopsies!"
        scene black with dissolve
        him"I can't see a thing after all, Teehee!"
        show himablindfold 2 with dissolve
        show himablindfold 2:
            easein 3 yalign 0.0
        him"Is t-this better? Aaaaah..."
        bo"Y-yeah... You ready?"
        him"Uh-Aaah...."
        call increaselust(20) from _call_increaselust_99
        bot"My g-god... This is way too arousing..."
        bo"O-okay t-then... Here comes the first test!"
        show screen parallax1280("himablindfold 2") with dissolve
        call showscrollingimage from _call_showscrollingimage_57
        if himawari_respect >= 0:
            default blindfoldrepeat = 0
            $ blindfoldrepeat = 1
            bo"This one should be right up your alley..."
            bo"An easy test just to see if your taste buds are shot!"
            him"Shot? You wish you had a palate as refined as mine bozo! Now hurry it up..."
            call hidescrollingimage("Click twice to start the taste test...") from _call_hidescrollingimage_58
            scene black
            show hima_drool00:
                xalign 0.5 zoom 1.2 yalign 1.0
            with dissolve
            show hima_drool00:
                easein 2 yalign 0.1
            bo"Hehe, we'll see about that..."
            show hima_drool00 with dissolve:
                xalign 0.0 zoom 0.53
            bo"Open up..."
            show hima_pop1 with dissolve:
                xalign 1.0 zoom 0.53
            him"Aaah..."
            show cutout_bo1 with dissolve:
                xalign 0.5 yalign 0.0 zoom 0.5
            bot"Does she have to vocalize the 'Ah' sound every time? It's... sort of setting me off!"
            bot"I can't with her any more... The way she sits on her knees, her arms between her legs..."
            show bo_erection1_cutout with dissolve:
                xalign 0.5 yalign 0.7 zoom 1.1
            bot"She just blends cute and sexy so freaking well..."
            bot"It's a good thing she is blindfolded, otherwise she'd turn into a demon as soon as she saw my raging erection dangling right in front of her face..."
            show screen parallax1280("hima_pop2") with dissolve
            call showscrollingimage from _call_showscrollingimage_58
            $ renpy.sound.play("/audio/soun_fx/sucking.mp3", channel="sfx2", loop=False, relative_volume = 1.0)
            bot"Something about having [him_name] blindfolded and on her knees, while she is looking up towards me..."
            bot"I can't hide that I am enjoying seeing her like this..."
            call increaselust(10) from _call_increaselust_108
            bot"Once a fiery brat, now laying dormant on its knees..."
            bot"And I even get a nice view of her little tits!"
            bot"I am such a perv... But can you  blame me?"
            bot"Will I really be able to pull off what I am thinking with her?"
            "She swirled her tongue around the candy, the cherry flavor sharp and sweet..."
            him"Mmmhm.. Yum..."
            bo"Hey, aren't you enjoying that a little bit too much? It's a taste test, not a devouring test!"
            $ renpy.sound.play("/audio/soun_fx/pop.mp3", channel="sfx2", loop=False, relative_volume = 1.0)
            hide screen parallax1280
            show screen parallax1280("hima_pop3",1,0.4)
            with dissolve
            "*Pop!* You pulled the stick out of her mouth. It left her lips wet and sticky..."
            "But a mischievous smirk would quickly form on [him_name]'s face..."
            show screen parallax1280("hima_pop3_2") with dissolve
            him"Ha! I know exactly what that was..."
            him"Reminds me of my childhood. Sweet, a little tart, and definitely sticky! It's a... "
            him"Cherry flavored lollipop!" with vpunch
            bo"Correct! One out of three, two more to go!"
            him"Easy!"
            bo"Heh! This next one won't be as easy!"
            him"Hehe! The hundred you promised will be  mine soon!"
            him"I'll buy so many clothes, and so much candy! Yaahoo!"
            bo"We'll see about that... Here comes the next item!"
            hide screen parallax1280
            show screen parallax1280("hima_pop3_1",1,0.4)
            with dissolve
            him"R-right! Aaahh..."
            scene black
            call hidescrollingimage("Click twice to continue with the taste test...") from _call_hidescrollingimage_59
            hide screen parallax1280
            with dissolve
            show hima_drool0:
                xalign 0.0 zoom 0.52
            with dissolve
            him"Come on, hurry up already!"
            "Previously reluctant, [him_name] was now getting excited at the thought of possibly winning the promised prize..."
            show cutout_bo1 with dissolve:
                xalign 1.0 yalign 0.0
            bo"G-getting into it, aren't you?"
            bot"Shall I test her a little bit more?"
            menu:
                bot"Shall I test her a little bit more?"
                "{color=[obediencecolor]}I am gonna need you to...{/color}":
                    show cutout_bo2 with dissolve:
                        xalign 1.0 yalign 0.0
                    bo"For this next one, you are going to have to scooch towards me and open your mouth as wide as you can..."
                    call checkObedience(12,"testalittlebitmorefail","Himawari") from _call_checkObedience_14
                    him"Hmmm...?"
                    him"Will this..."
                    show hima_drool1 with dissolve:
                        xalign 0.0 zoom 0.52
                    call changeObedience("Himawari",1) from _call_changeObedience_95
                    him"...Be enough?"
                    menu:
                        him"Will this... be enough?"
                        "{color=[obediencecolor]}Tease her...{/color}":
                            bo"I prefer it when you act like my obedient little puppy as opposed to a barking hound! Maybe you'd like a little head pat as your reward?"
                            call changeObedience("Himawari", 1) from _call_changeObedience_96
                            him"Don't even think about touching my head you weirdo! And I am n-not your p-puppy!"
                            call changeRespect("Himawari",-1) from _call_changeRespect_161
                            him"I am simply trying to get this over with and take your money! You d-dummy..."
                            him"Get on with it!" with vpunch
                            bo"Hehe! Still ways to go until you can do that..."
                        "Perfect!":
                            bo"Perfect! That'll do..."
                        "{color=[hatredcolor]}(Looking like a cock-craving bitch!){/color}" if hatred >= 20:
                            bo"That'll do little [him_rel]! You are looking..."
                            call changeHatred(1) from _call_changeHatred_117
                            show cutout_bo3 with dissolve:
                                xalign 1.0 yalign 0.0
                            bot"Like a god-damned cock-craving bitch!"
                            bot"You'd look even better with my cock shoved down your-"
                            hide cutout_bo3
                            hide cutout_bo2
                            show cutout_bo1:
                                xalign 1.0 yalign 0.0
                            with dissolve
                            him"I am looking like... what? And don't call me your little [him_rel]! It sounds... weird!" with vpunch
                            bo"Sure... I was just saying you are looking ready for the next item!"
                            him"I am! Bring it on..."

                    jump testalittlebitmoreafter
                    label testalittlebitmorefail:
                    hide cutout_bo2
                    hide cutout_bo1
                    with dissolve
                    show hima_drool2_shy with dissolve:
                        xalign 0.0 zoom 0.52
                    him"What d-do you think this is you weirdo? Just hurry up and get the test going already..." with vpunch
                    hide cutout_bo1 with dissolve
                    bo"F-fine... I was only trying to help..."
                    $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                    him"Hmph!" with vpunch
                    him"Bring on the next item, I am about to be rich with your promised hundred!"
                    hide hima_drool2_shy with dissolve
                    bo"Still ways to go for that..."


                        

                "(I shouldn't push my luck...)":
                    hide cutout_bo2 with dissolve
                    bot"I shouldn't push my luck..."
            label testalittlebitmoreafter:
            hide cutout_bo2
            hide cutout_bo3
            hide cutout_bo1
            with dissolve
            bo"Here it comes..."
            him"Aaaah..."
            show hima_drool0:
                alpha 0.3
            show hima_banana0:
                    xalign 1.0 zoom 0.52
            with dissolve
            bo"How about this then..."
            him"Mmm..."
            him"Soft and sweet, but..."
            "[him_name] takes a few reluctant licks before..."
            show hima_banana01 with dissolve:
                xalign 0.5 yalign 0.2 zoom 1.22
            "She chomps down on the banana in mild frustration..." with vpunch
            bot"S-shit... Wouldn't want that to happen to my prized possession!"
            bot"But I know exactly how to handle this..."
            scene black with dissolve
            bot"Surely [him_name] wouldn't give up this easily knowing how competitive she can get..."
            "You pulled the banana away from her mouth after she took a bite..."
            show cutout_bo1 zorder 1000 with dissolve:
                    ypos 0.6 xzoom 0.6 yzoom 0.32 zoom 3.28 
            bo"What's wrong, having trouble with this one?"
            bo"I suppose the test is over before it even begun..."
            bo"Lucky me! Guess I am keeping my hundred..."
            show hima_drool1 with vpunch:
                zoom 1.21 xalign 0.5 ypos -1.70
            show cutout_bo2 zorder 1001 with dissolve :
                    ypos 0.6 xzoom 0.6 yzoom 0.32 zoom 3.28 
            him"N-no, w-wait!" with vpunch
            show cutout_bo2 zorder 1001 with dissolve :
                    ypos 0.6 xzoom 0.6 yzoom 0.32 zoom 3.28 
            him"I just need another b-bite before I confirm my answer..."
            scene black
            show hima_drool2:
                xalign 0.5 zoom 1.22 yalign 1.0
            with dissolve
            show hima_drool2:
                easein 2 yalign 0.1
            bot"I knew you wouldn't give up that easily!"
            bot"I better use this opportunity to set down a few ground rules. For my... safety!"
            show screen parallax1280("hima_drool2",1.22,0.1)
            call showscrollingimage from _call_showscrollingimage_59
            with dissolve
            bo"Another bite, huh?"
            bo"You know taste tests are usually an one-off type of deal..."
            him"S-so what!? Just let me have another try you dork!" with vpunch
            him"You said you needed my help with your secret recipe or w-whatever... didn't you?"
            bo"I do, but only if my subject is capable of helping in the first place..."
            scene black
            hide screen parallax1280
            show screen parallax1280("hima_drool2_shy",1.22,0.1)
            with dissolve
            $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            him"Hmph! W-whatever... I don't need t-the money anyway!"
            bo"Ffffine! I'll give you another shot..."
            call hidescrollingimage from _call_hidescrollingimage_60
            show hima_drool2_shy with dissolve:
                xalign 0.0 zoom 0.53
            him"R-really!?"
            bo"I will, but first..."
            $ hima_intromenutwo = []
            menu hima_intromenu2:
                set hima_intromenutwo
                bo"I will, but first..."
                "You have to bark for me like a dog!":
                    bo"I'll give you another shot, but first you have to bark for me like a dog!"
                    show hima_drool2_angry:
                        xalign 1.0 zoom 0.53
                    show hima_drool2_shy:
                        alpha 0.3
                    with dissolve
                    call changeRespect("Himawari",-1) from _call_changeRespect_162
                    him"Are you... slow in the head you s-stupid idiot!?" with vpunch
                    him"You might be a major clown but this isn't a circus and I am not your animal!"
                    show hima_drool1 with dissolve:
                        xalign 1.0 zoom 0.53
                    him"Now hurry up and get this over with! You are starting to annoy me..."
                    hide hima_drool2_angry with dissolve
                    jump hima_intromenu2
                "'Take out your cock'" if takeoutcock_hima == False:
                    default takeoutcock_hima = False
                    $ takeoutcock_hima = True
                    bo"I need to make some preparations first..."
                    show bo_erection3_cutout with dissolve:
                        xalign 0.5 yalign 0.5 zoom 1.05
                    bo"...In case you pass this second test. My prototype has to be ready..."
                    bo"And the preparation it takes is..."
                    hide bo_erection3_cutout with dissolve
                    $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                    bo"...Quite meticulous!"
                    "You started jerking off right in front of your unsuspecting [him_rel]..."
                    show hima_drool1 with dissolve:
                        xalign 1.0 zoom 0.53
                    him"S-sure... R-ready when you are!"
                    call increaselust(10) from _call_increaselust_109
                    bot"S-shit... I am losing my mind!"
                    jump hima_intromenu2

                "'Keep jerking off...'" if takeoutcock_hima == True:
                    default keepjerking_hima = 0
                    if keepjerking_hima == 0:
                        bo"Give me just a s-second..."
                        show bo_erection3_cutout with dissolve:
                            xalign 0.5 yalign 0.5 zoom 1.05
                        bo"...Still preparing the prototype!"
                        hide bo_erection3_cutout with dissolve
                        $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                        bot"This whole ordeal is just a massive turn on..."
                        bot"My unsuspecting [him_rel] sitting on her knees, blindly trusting me..."
                        bot"All I can think about is betraying that trust..."
                        show hima_drool1 with dissolve:
                            alpha 0.3
                        show hima_drool2_shy with dissolve:
                            alpha 1.0
                        him"What's taking so long! Now you are just making me curious..."
                        call increaselust(10) from _call_increaselust_110
                        bo"Don't worry, you'll get a taste soon enough!"
                        show hima_drool2_shy with dissolve:
                            alpha 0.3
                        show hima_drool1 with dissolve:
                            xalign 1.0 zoom 0.53 alpha 1.0
                        him"Come on, hurry up! I don't have all day you know..."
                        $ keepjerking_hima = 1
                        jump hima_intromenu2
              
                "'Approach her...'" if takeoutcock_hima == True:
                    bo"You still have to correctly guess what the second item is before you can taste my recipe and have a shot at the hundred I promised..."
                    him"F-fine... Bring it on!"
                
            show hima_drool2_shy:
                alpha 0.3
            show hima_drool1:
                xalign 1.0 zoom 0.53
            with dissolve
            him"Aaah..."
            bo"Here it comes!"
            show hima_banana0 with dissolve:
                xalign 0.5 yalign 0.2 zoom 1.22
            bot"She better get this one right, or my whole plan collapses..."
            him"Mhmmm... Y-yesh... I know thish one... I think..."
            bot"Come on! How busted must one's palate be to not be able to tell apart a banana..."
            bot"I guess it can happen when all you eat is sweets and candy..."
            bot"Maybe she could use a little help..."
            menu:
                bot"Maybe she could use a little help..."
                "{color=[hatredcolor]}Force the banana down her throat!{/color}" if hatred>=15:
                    bot"Might as well figure out her tolerance for what's to come!"
                    bo"You seem to be having a little trouble with this one..."
                    him"N-no... I know thish-"
                    scene black
                    bo"Maybe this would help you figure it out!" with vpunch
                    show hima_banana1 with dissolve:
                        xalign 0.5 yalign 0.0 zoom 1.25
                    $ renpy.sound.play("/audio/soun_fx/hima_gag.opus", channel="sfx2", loop=False, relative_volume = 1.2)
                    "Without warning, you shoved the banana halfway into her mouth..."
                    show screen parallax1280("hima_banana1",1.25,1.0) with dissolve
                    call showscrollingimage from _call_showscrollingimage_60
                    "[him_name] arched her back and braced her arms at her sides. To your surprise, she seemed to handle the sudden oral intrusion fairly well..."
                    him"Mhm...!" with vpunch
                    bot"H-holy shit! She hasn't even gagged with half this thing shoved down her throat!"
                    bot"Could she..."
                    bot"Could [him_name] have no gag reflex at all!?" with vpunch
                    call increaselust(10) from _call_increaselust_111
                    bot"My d-days... My little [him_rel] might have talents I never could have dreamt about..."
                    call changeHatred(1) from _call_changeHatred_118
                    bot"Hell, she might even turn out to be a throat GOAT with some training!" with vpunch
                    bot"F-fuck me! My cock is throbbing with anticipation just mere inches away from her face..."
                    bot"I am moments away from cumming just by thinking about shoving it in there!"
                    default hima_throatgoat = False
                    $ hima_throatgoat = True
                    call hidescrollingimage from _call_hidescrollingimage_61
                    hide screen parallax1280
                    scene black
                    with vpunch
                    "[him_name] jolts her head backwards, freeing her mouth from your intrusion and muttering in mild frustration..."
                    show screen parallax1280("hima_finalbefore_angry",1.25,0.0) with dissolve
                    call showscrollingimage from _call_showscrollingimage_61
                    him"What was t-that for...!" with vpunch
                    bo"I just thought I s-should give you a helping hand..."
                    call changeRespect("Himawari",-2) from _call_changeRespect_163
                    him"Don't just push t-things into my mouth you idiot!" with vpunch
                    him"At the very least, you could give me a heads up or something..."
                    him"What if it was something yucky and I... puked all over you or something!"
                    call hidescrollingimage from _call_hidescrollingimage_62
                    scene black with dissolve
                    "You slightly pulled back to avoid raising suspicion..."
                    bo"You are right, I am sorry! You don't have to get THAT graphic..."
                    show hima_pop3_2 with dissolve
                    show hima_pop3_2:
                        easein 8 yalign 0.4
                    bot"Although who knows... Maybe the sloppy mess would be a sight to behold!"
                    him"Heee-heeeee..."
                    bot"She really is unfazed after having that banana shoved down her throat, huh..."
                    bot"And what's with the smirk on her face..."
                    him"I'll let it slide this time, only because you are about to pay me all that money you promised!" with vpunch
                    

                    

                "Offer a hint":
                    bo"...So? I can give you a small hint if you'd like..."
                    scene black with vpunch
                    him"What...? No!"
                    "[him_name] jolts her head backwards in mild frustration..."
                    show screen parallax1280("hima_finalbefore_angry",1.25,0.0) with dissolve
                    call showscrollingimage from _call_showscrollingimage_62
                    "[him_name] arched her back and braced her arms at her sides and turned her gaze towards you..."
                    him"I don't even need the hint to begin with!" with vpunch
                    bo"O-okay! You don't have to get so worked up over it..."
                    bot"F-fuck me! My cock is throbbing with anticipation just mere inches away from her face..."
                    show hima_finalbefore_angry:
                        zoom 1.25 yalign 0.0
                    call hidescrollingimage from _call_hidescrollingimage_63
                    scene black
                    with vpunch
                    "You slightly pulled back to avoid raising suspicion..."
                    show hima_pop3_1 with dissolve
                    show hima_pop3_1:
                        easein 7 yalign 0.4
                    bo"I just thought you could use some help..."
                    call changeRespect("Himawari", 1) from _call_changeRespect_164
                    him"No, I know... And I appreciate the sentiment, but..."
                    him"If I am gonna earn the money you promised I want to do that fair and square!"
                    show hima_pop3_2 with dissolve:
                        yalign 0.4
                    him"That way you can't find some stupid excuse to weasel your way out of it when I evidently do! Teehee!"
                    bo"I would never! I am a man of my word..."
                    him"Besides..."



                    
                








            him"I know exactly what that was!" with vpunch
            bot"Heh! Little does she know... That's precisely what I wanted to hear!"
            bo"Oh yeah? What was it then..."
            him"Soft, fruity, slightly creamy aaaand, completely and utterly unripe!"
            him"That was an underriped banana of course!" with vpunch
            him"Which is why I had trouble with it initially! Next time pick a properly ripened one you dummy..."
            bo"*Nervous laughter* He-heh... My bad I suppose..."
            bo"I just picked whatever [hin_rel] picked herself from the market. You know how she can be when it comes to food..."
            bo"If it ain't fresh, it goes straight to the trash..."
            him"Sounds like her alright! More importantly, I was right wasn't I!?"
            bo"Two out of three! But you aren't done just yet..."
            him"Yaahoo!" with vpunch
            him"Get ready to kiss your money goodbye!"
            bo"We'll see about that. The real challenge still awaits you!"
            bot"I better set some ground rules for what's to come, lest I find my crown jewel chomped in half..."
            show hima_pop3 with fade:
                yalign 0.4
            him"Bring it on already!"
            show screen parallax1280("hima_pop3",1,0.2) with dissolve
            call showscrollingimage from _call_showscrollingimage_63
            bo"Heh... G-getting into it, aren't you?"
            bo"Just give me a s-second... I still have to make the final preparations..."
            bot"F-fuck... I am getting way too aroused watching her impatiently sit there with her little tongue hanging out her mouth..."
            bot"I thought I'd be ready to seize the moment, but..."
            call increaselust(10) from _call_increaselust_112
            $ renpy.sound.play("/audio/soun_fx/heartbeatlong.opus", channel="sfx2", loop=False, relative_volume = 1.0)
            bot"My heart is beating so fast, and so loud! I am getting overly anxious..."
            bot"I am taking a massive risk trying to pull this off..."
            bot"Hopefully [him_name] doesn't pick up on my anxiety..."
            call hidescrollingimage from _call_hidescrollingimage_64
            scene black
            him"H-hey, hurry it up!" with vpunch

            bo"O-okay, okay! Will you r-relax?"
            him"I am totally relaxed! Unlike you...!"
            bot"S-shit! Is she already picking up on my anxiety!?" with vpunch
            him"Afraid of losing your money...? Teehee!"
            show hima_finalbefore with dissolve:
                zoom 1.25 xalign 1.0
            show hima_finalbefore:
                easein 3 yalign 0.2
            bo"*Nervous laughter* Heh! Of c-course not..."
            bo"Just making the final preparations. Get ready..."
            him"Aaahh..."
            bot"If I don't take a leap of faith now..."
            bot"Then I'll never forgive myself!"
            show screen parallax1280("hima_finalbefore",1.25,1.0) with dissolve
            call showscrollingimage from _call_showscrollingimage_64
            bot"If my intuition is right..."
            bot"[him_name] is certainly a virgin. Not only that, but..."
            bot"Regardless of her outwards antics, she is extremely reserved when it comes to sex stuff..."
            bot"She was raised by her [hin_rel] after all..."
            bot"And [hin_rel] would be a secluded monk if it weren't for [na_rel]..."
            bot"This is still a massive gamble of course, but..."
            bot"With the blindfold on, and with the taste test premise I laid down, there's very little chance she can tell what's she's about to taste!"
            $ renpy.sound.play("/audio/soun_fx/heartbeatlong.opus", channel="sfx2", loop=False, relative_volume = 1.0)
            bot"Fuck it! Worst case she loses her shit, tells [hin_rel], and they both strangle the life out of me. I get to live my pervy fantasies in heaven... or hell!"
            call hidescrollingimage from _call_hidescrollingimage_65
            scene black with dissolve
            bot"Here goes nothing..."
            "You lowered your pants and..."
            show hima_finalbefore2 with dissolve:
                yalign 1.0
            show hima_finalbefore2:
                easein 2 yalign 0.3
            pause 1.8
            show screen parallax1280("hima_finalbefore2",1.0,0.3) with dissolve
            call showscrollingimage from _call_showscrollingimage_65
            "You inched ever so slightly closer to her face, the smell would surely become apparent to [him_name] from that distance..."
            bo"Right, the preparations are complete..."
            himt"What's with this weird odor..."
            bo"You now get the special privilege of tasting my super secret recipe!"
            him"If it's anything disgusting... I am going to kill you!" with vpunch
            bo"D-disgusting? As if!" with vpunch
            bo"It's tasty... and e-expensive! In fact, you aren't allowed to bite on this one..."
            bo"You can smell, taste, and feel it... But you cannot chew on it or use your hands! You got it?"
            $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            him"Hmph! Fine..." with vpunch
            bo"Remember, you are supposed to help me with refining and improving the recipe! Correctly guessing the ingredients is just an extra little challenge for you..."
            bo"You can start by describing the smell..."
            bo"Can you tell what this might be?"
            him"It's... It's a strong odor, a strange one too, but..."
            him"Not unpleasant... I think. It's hard to tell!"
            bot"God, she's so close to it! My cock is throbbing with anticipation..."
            bot"She is going to taste me soon and she doesn't even know it!"
            $ renpy.sound.play("/audio/soun_fx/heartbeatlong.opus", channel="sfx2", loop=False, relative_volume = 1.0)
            bot"My heart is freaking racing..."
            him"Hmm..."
            "[him_name]'s gaze was fixated on what was in front of her, allured by the strange odor that filled her nostrils..."
            him"Wait a second..." with vpunch
            bo"H-huh... W-why? What's going on..."
            him"I..."
            "[him_name]'s pulse quickened, her senses seemed to be on high alert. You could tell she was on the precipice of some sort of an emotional outburst..."
            scene black
            hide screen parallax1280
            hide scrollingimage onlayer screens
            him"This isn't what I think it is... right?" with vpunch
            "You quickly stepped back in fear of what could potentially transpire..."
            bot"S-shit! Shit, shit, fuck, FUCK! Is she o-onto me!?"
            show screen parallax1280("hima_finalbefore_angry",1.25,0.0) with dissolve
            call showscrollingimage from _call_showscrollingimage_66
            "[him_name] seemed agitated, but she still laid dormant on the floor..."
            him"It must be... I know exactly what that is!" 
            bo"Y-you... do?"
            him"I do! You scheming weasel!" with vpunch
            bot"F-fuck, fuck FUCK!"
            call hidescrollingimage("Click twice to sneakily run away!") from _call_hidescrollingimage_66
            scene black with dissolve
            $ renpy.sound.play("/audio/soun_fx/clothes_undress.opus", channel="sfx3", loop=False, relative_volume = 1)
            "You quickly pulled your pants up and sneakily made your way out of the room..."
            "[him_name] unaware of your antics, kept murmuring something behind you..."
            him"That weird, musky smell... The strong earthly aroma it induced..."
            him"That has to be..."
            $ renpy.sound.play("/audio/soun_fx/doorclose.opus", channel="sfx2", loop=False, relative_volume = 1.0)
            show bg day:
                zoom 0.69
            show boruto bonersurprised  at center
            with dissolve
            bot"I am as good as dead, aren't I?"
            show boruto at smallshake
            bot"There's no way I am getting out of this mess alive...."
            bot"All that's left is for me to await my demise..."
            hide boruto with dissolve
            bot"Fuck, fuck, FUCK!" with vpunch
            scene black with dissolve
            "Meanwhile..."
            show hima_finalbefore_angry with dissolve:
                zoom 1.25 yalign 0.0
            him"That weird, musky smell... The strong earthly aroma it induced..."
            him"That has to be..."
            him"...S-some kind of a sweetened vegetable!" with vpunch
            him"."
            him".."
            him"..."
            him"...R-right?"
            scene black with dissolve
            $ renpy.sound.play("/audio/soun_fx/doorclose.opus", channel="sfx2", loop=False, relative_volume = 1.0)
            him"Wait a sec..."
            show hima_drool2_shy with dissolve:
                xalign 0.0 zoom 0.53
            himt"Was that the door I just heard...?"
            him"[bo_name_stutter]...?"
            him"."
            him".."
            him"..."
            him"Y-you..."
            show hima_drool2_angry:
                xalign 1.0 zoom 0.53
            show hima_drool2_shy:
                alpha 0.2
            with dissolve
            him"You f-freaking t-thief!" with vpunch
            him"Come back here and give me my money!" with vpunch
            scene black with dissolve
            show bg bb day with dissolve
            show boruto worried2 at center with dissolve
            $ renpy.sound.play("/audio/soun_fx/footsteps.opus", channel="sfx2", loop=False, relative_volume = 0.9)
            bot"Right about now she must be making her way to the kitchen to arm herself with a knife..."
            bot"I can hear her trampling around the place..."
            bot"Here she comes..."
            scene bg day:
                zoom 0.69
            show hima mad at center:
                zoom 0.34
            with dissolve
            him"Where are you hiding, you weasel!"
            show hima:
                easein 1 xpos -1000
            pause 0.8
            scene black with dissolve



            #1st ending
            #brotuo runs off to bedroom
            scene bg bb day with dissolve
            show boruto surprised2 at left with dissolve
            show hima mad:
                xpos 2000 zoom 0.34
            show hima:
                easein 0.5 xpos 700
            pause 0.5
            
            him"Found y-you, thief! Hold it right there!" with vpunch
            bot"This is it. My life's over..."
            show hima at smallshake
            him"Trying to weasel your way out of our deal!?"
            show boruto surprised3 with dissolve
            bot"The d-deal? Wait a second..." with vpunch
            bo"N-no! I was just having second thoughts... Didn't want you to ruin my one and only prototype."
            show hima at smallshake
            him"Be honest you rat! You run away because you knew I could tell what that... thing was! Didn't you?"
            show boruto surprised2 with dissolve
            bo"O-oh yeah? What was it then if you are so certain..."
            him"The earthly smell gave it away! It's some sort of..."
            him"A V-vegetable! R-right!?" with vpunch
            bot"A... vegetable?"
            show boruto laughing2 with dissolve
            bo"Bwaaahahahahha!" with vpunch
            show boruto at smallshake
            bo"A v-vegetable...?"
            him"W-why are you laughing like that! I am right, aren't I?!"
            show boruto snob with dissolve
            bot"She really has no fucking idea at all! My intuition was right!"
            bo"R-right!? You are no where close! And even if you were, a vegetable is way too broad of a term..."
            show hima worried2 with dissolve
            him"Y-yeah well, that's because you run away before I even got to taste it, you idiot!" with vpunch
            him"You owe me another try!" with vpunch
            show boruto embarassed with dissolve
            bo"Y-you are right... I am sorry! You can have another go at it next time!"
            show hima at smallshake
            him"With the money bet still on the line... r-right!?"
            show boruto snob with dissolve
            bo"Of course, I promise!"
            show hima smugshy with dissolve
            $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.6)
            him"Hmph! I'll forgive you for running away this time then..." with vpunch
            show hima:
                easein 0.7 xpos 400
            him"Here, you forgot this..."
            if not _in_replay:
                call getItem(blindfold,1) from _call_getItem_5
            him"But next time, you better stay true to your promise! That money will belong to me soon..."
            show hima:
                easein 1 xpos 2000
            him"Teehee!" with vpunch
            show boruto at smallshake
            bo"Bwahaha!"
            bot"Guess all my fears were unwarranted... She really is completely clueless!"
            bot"I can't wait until next time! Knowing her lack of experience, I might be able to move forward with my plan..."
            bo"Hehe..."
            $ renpy.end_replay()
            jump action_taken



                




        else:
            label blindfoldrespectfail:
            him"..."
            call hidescrollingimage("Click twice to start the taste test...") from _call_hidescrollingimage_67
            scene black
            him"W-wait!" with vpunch
            if day_part == 3:
                show himawari_bedroom_2
            else:
                show himawari_bedroom_1
            show hima worried2:
                zoom 0.34 xalign 0.4
            show boruto surprised2 at left
            with dissolve
            show hima:
                easein 0.6 xalign 0.8
            with dissolve
            call getItem(blindfold,1) from _call_getItem_4
            him"Take t-this back p-please..."
            bo"W-what? Why... what happened?"
            bo"I thought you wanted to help..."
            him"I do, b-but..."
            call checkRespect(0,"Himawari") from _call_checkRespect_3
            him"Something just f-feels off. Not to mention how weird you've been acting lately..."
            him"I just need some time, okay?"
            him"Talk to me about it some other time and I might reconsider..."
            show boruto snob with dissolve
            bot"Damn it! So close..."
            show boruto normal with dissolve
            bo"I understand. Don't worry about it, we can go at your pace. Thanks for trying to help anyway..."
            him"Mhmm... I'll talk to you later I guess..."
            hide hima with dissolve
            call changeRespect("Himawari", 1) from _call_changeRespect_153
            him"T-thanks for being understanding..."
            scene black with dissolve
            jump action_taken
        



