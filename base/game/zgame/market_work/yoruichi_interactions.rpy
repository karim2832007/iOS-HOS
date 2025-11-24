
default yoruichi_talk_progress_formal = 0
default yoruichi_talk_progress_apprehensive = 0
default yoruichi_talk_progress_obedient = 0
default yoruichi_talk_progress_unwillinglyobedient = 0
default yoruichi_approach_progress_unwillinglyobedient = 0
default yoruichi_approach_progress_obedient = 0
default yoruichiinteractiontaken = False
default oboatnights = False #spied obo during nights
default borutonicetoyoru = True #if relationship set to obedient before apprehgensive
default sharemoneywithyoru = False
default sharemoneywithyorucounter = 0
default yoru_kneeled_talk = 0
label yoruichiinteractions:
    if yoruichiinteractiontaken == True:
        yo"Enough, there's work to be done..."
        jump ramenkitchenmenu #return to initialmenu if already interacted on the day


    
    #Formal ---------------------------------------------------------------------------
    if yoruichi_relationship == "Formal":

        if yoru_kneeled == True and yoru_kneeled_talk == 2:
            show boruto sceeming2 at left with dissolve
            bo"Hey Yoruichi!"
            show yoru angry3 at right with dissolve
            yo"W-what do you want, kid!"

        elif yoru_kneeled == True:
            show boruto sceeming2 at left with dissolve
            bo"Yoruichi!"
            show yoru angry3 at right with dissolve
            yo"What the hell do you want from me!"

        else:
            show boruto smirk at left with dissolve
            bo"Hey Yoruichi..."
            show yoru shy at right with dissolve
            yo"What do you want kid?"
        menu yoruichiformalmenu:
            "..."
            "Talk with Yoruichi":
                if yoru_kneeled == True and yoru_kneeled_talk !=2:
                    if yoru_kneeled_talk == 0:
                        $ yoru_kneeled_talk = 1
                        show boruto sceeming3 with dissolve
                        bo"Let's talk!"
                        show yoru angry2 with dissolve
                        yo"You cannot be serious!"
                        yo"After what you've done to me?"
                        yo"Piss off!" with vpunch
                        hide yoru with dissolve
                        show boruto sceeming2 with dissolve
                        bot"Bitch... I'll have to try to bribe her or something!"
                        hide boruto with dissolve
                        $ yoruichiinteractiontaken = True
                        jump ramenkitchenmenu
                    elif yoru_kneeled_talk == 1:
                        $ yoru_kneeled_talk = 1
                        show boruto sceeming2 with dissolve
                        bo"Come on, let's talk! I have a proposition for you..."
                        show yoru angry2 with dissolve
                        yo"This again? After what you've done?"
                        show boruto sceeming with dissolve
                        $ yoruichiinteractiontaken = True
                        menu:
                            yo"This again? After what you've done?"
                            "'Apologize'":
                                show boruto sceeming with dissolve
                                bo"Okay look, I am sorry about what I did..."
                                bo"There's an explanation for that you know but I am sure you wouldn't want to hear about that anyway..."
                                show yoru angry3 with dissolve
                                yo"What possible explanation would there be for that you creep!"
                                
                                bot"I'll just put an act on for now..."
                                show boruto suspicious with dissolve
                                bo"You are right, I went too far. But listen, what If I could offer you something along with my apology..."
                                yo"And what would that be...?"
                                bo"I know you need the money more than I do and you know Obo pays me well for the work I get done."
                                bo"What would you say if I was willing to split my next shift's payment with you?"
                                bo"All I ask for is that you let bygones be bygones."
                                yo"Is that it then? You think you can just buy me off?"
                                menu :
                                    yo"Is that it then? You think you can just buy me off?"
                                    "Bluff":
                                        bo"Well, that's all I can offer you right now. Take it or leave it."
                                        bo"You wanna sit there and sulk about it then be my guest..."
                                        hide boruto with dissolve
                                        show yoru shy with dissolve
                                        yo"W-wait!" with vpunch
                                        show boruto sceeming at left with dissolve
                                        bot"I knew that would work!"
                                        yo"I'll... take your d-damn money! That is if you promise you'll never do anything like that again!"
                                        $ sharemoneywithyoru = True
                                        menu:
                                            yo"I'll... take your d-damn money! That is if you promise you'll never do anything like that again!"
                                            "I promise":
                                                bo"Fair enough, I promise."
                                                show yoru obedient with dissolve
                                                yo"Good!"
                                            "{color=[hatredcolor]}I... promise!{/color}":
                                                bot"What a stupid whore..."
                                                show boruto sceeming2 with dissolve
                                                call borutoevil2 from _call_borutoevil2_11
                                                call changeHatred(1,"none") from _call_changeHatred_59
                                                bo"Of course, I... promise!"
                                                show yoru obedient with dissolve
                                                yo"G-good..."
                                hide boruto
                                hide yoru
                                with dissolve
                                "You are now able to talk to Yoruichi. Your next shift's payment will be cut in half."
                                $ yoru_kneeled_talk = 2
                                $ yoruichiinteractiontaken = True
                                jump ramenkitchenmenu
                    
  

                            "Fine, no proposition for you then...":
                                show boruto sceeming2 with dissolve
                                bo"And here I thought you needed some money..."
                                show boruto sceeming3 with dissolve
                                bo"Fine! Have it your way then..."
                                hide boruto with dissolve
                                show yoru angry3 with dissolve
                                yo"W-wait..."
                                hide yoru with dissolve
                                jump ramenkitchenmenu
                            
                    # elif yoru_kneeled_talk == 2:
                           
                    #     jump yoruichiformaltalkmenu

                else:
                    show boruto normal with dissolve
                    bo"Let's talk..."
                    show yoru shy with dissolve
                    yo"About what?"
                menu yoruichiformaltalkmenu:
                    yo"About what?"
                    "How are you faring?":
                        default howareyoufaringcounter = 0
                        if howareyoufaringcounter == 0:
                            $ yoruichi_talk_progress_formal = 1
                            show boruto normal with dissolve
                            bo"How are you faring Yoru?"
                            show yoru normal at right with dissolve
                            yo"About as well as one can working a dead-end job under a deadbeat boss and husband..."
                            yo"But I already told you... I have no say in this, please don't bring it up again."
                            show boruto worried with dissolve
                            bo"I was just wondering if you are alright..."
                            hide yoru with dissolve
                            yo"*Sigh*"
                            bot"She is still avoiding me..."
                            hide boruto with dissolve
                            $ howareyoufaringcounter += 1
                        elif howareyoufaringcounter == 1:
                            show boruto normal with dissolve
                            bo"How are you doing, Yoru..."
                            show yoru normal at right with dissolve
                            yo"This again?"
                            yo"Stop trying to get close to me kid... We are just co-workers."
                            hide yoru with dissolve
                            yo"We are not friends..."
                            bot"She won't even talk to me..."
                            $ config.menu_include_disabled = True
                            menu:
                                bot"She won't even talk to me..."
                                "...Bitch!":
                                    show boruto angry2 with dissolve
                                    bot"Bitch... I'll get to her one way or another!"
                                "She must be dealing with a lot..." if yoru_kneeled != True:
                                    show boruto worried with dissolve
                                    bot"She must be dealing with a lot..."
                            $ config.menu_include_disabled = False
                            hide boruto with dissolve
                        
                                
                    
                    "You can be open with me, How's Obo treating you?" if yoruichi_talk_progress_formal >= 1:
                        show boruto normal with dissolve
                        bo"Yoru... You can be open with me. How's Obo been treating you?"
                        if spyworkmapcounter > 0:
                            bot"Of course I already know having seen what Obo does to her during nights..."
                            bot"But maybe asking her will provide some context..."
                        if score_3_claimed == True:
                            show yoru shy with dissolve
                            yo"You've seen it with your own eyes when Obo had you... do that to me!"
                            if yorudontdoanything1 == False and yorudontdoanything2 == False: #if harassed during obo quest
                                show yoru normal with vpunch
                                yo"In fact, you were an accomplice in that, you piece of shit!"
                                hide yoru with dissolve
                                yo"Don't talk to me!"
                                $ yoruichi_talk_progress_formal +=1
                                show boruto sceeming2 with dissolve
                                bot"Bitch... Just you wait!"
                                hide boruto with dissolve
                            else:
                                show yoru shy2 with dissolve
                                yo"Why would you even ask me that kid?"
                                show yoru shy with dissolve
                                yo"There's nothing you or I can do about it..."
                                hide yoru with dissolve
                                "She walked away in embarassment..."
                                show boruto worried with dissolve
                                bot"Why won't she let me help..."
                                bot"I might have to find out more before she's willing to open up to me..."
                                bot"Maybe I should find out more about what's going on during nights..."
                                $ yoruichi_talk_progress_formal +=1
                                hide boruto with dissolve
                        
                        else:
                            show yoru normal with dissolve
                            default youcanbeopenwithme = 0
                            if youcanbeopenwithme == 0:
                                yo"Kid... Who do you think you are? A therapist of sorts?"
                                yo"I am not about to open up to some [bo_age] old kid I've known for a few days."
                                yo"Stop pestering me!" with vpunch
                                hide yoru with dissolve
                                yo"*Scoffs*"
                                show boruto normal with dissolve
                                bo"Sheesh... I was just trying to help."
                                if spyworkmapcounter > 0:
                                    bot"Or maybe not... I should try a different approach."
                                $ yoruichi_talk_progress_formal +=1
                                $ youcanbeopenwithme +=1
                            else:
                                show yoru angry2 with dissolve
                                yo"God-fucking damn it enough with this make-pretend facade of yours kid!"
                                show yoru angry3 with dissolve
                                yo"Stay away from me!"
                                hide yoru with dissolve
                                show boruto worried with dissolve
                                bot"Why won't she let me help..."
                                bot"I might have to find out more before she's willing to open up to me..."
                                bot"Maybe I should find out more about what's going on during nights..."
                                hide boruto with dissolve
                                $ yoruichi_talk_progress_formal +=1


                    "(Locked)" if yoruichi_talk_progress_formal < 1:
                        "Options will become available as you uncover more of the story"
                        jump yoruichiformaltalkmenu
                    
                    "I've seen what happens during nights..." if yoruichi_talk_progress_formal >= 2 and ramennightscenescounter >=1:
                        if yoruichi_talk_progress_formal == 3:
                            show boruto worried at left with dissolve
                            show yoru shy2 with dissolve
                            bo"About what happens during nights..."
                            show yoru angry3 with dissolve
                            yo"How fucking dense are you kid..."
                            yo"There's nothing I have to say to you!"
                            hide yoru with dissolve
                            bot"Shit! I might have to learn more before I can get her to open up... Maybe I can keep spying during nights."
                            hide boruto with dissolve
                            $ yoruichiinteractiontaken = True
                            jump ramenkitchenmenu
                        show boruto worried at left with dissolve
                        bo"Yoru... I've seen what happens during nights..."
                        show yoru normal at right with dissolve
                        yo"You've... seen it? Seen what, kid? Seen how!?"
                        menu:
                            yo"You've... seen it? Seen what, kid? Seen how!?"
                            "Uhh... I might have snuck upstairs...":
                                bo"Uhh... I might have snuck upstairs during the night."
                                bo"I've seen... everything, Yoru."
                                bo"How can you let Obo do that to you?"
                                show yoru surprised with dissolve
                                yo"S-snuck upstairs!?"
                                show yoru angry3 with dissolve
                                yo"Are you fucking stupid kid!? You are putting both of us in grave danger with your antics!" with vpunch
                            "I've seen Obo throatfuck you like a cum-dump!":
                                show boruto sceeming with dissolve
                                bo"I've seen how Obo fucked your throat... I've seen it all, Yoru!"
                                show yoru scared2 with dissolve
                                bo"You really are his cum-dump... aren't you?"
                                bo"Why do you even allow him to step all over you like that?"
                                show yoru angry2
                                show boruto surprised2
                                with dissolve
                                yo"You... p-piece of shit!"
                        show yoru disgust with dissolve
                        yo"Do you think I have a choice!?"
                        show yoru disgust2 with vpunch
                        yo"Do you think I enjoy that!?" with vpunch
                        hide yoru with dissolve
                        yo"Stay away from me kid! You have no idea what you are dealing with!" with vpunch
                        "She walked away visibly shaken..."
                        bot"Was I too direct...?"
                        bot"I might have to find out more before I can..."
                        $ config.menu_include_disabled = True
                        $ yoruichi_talk_progress_formal = 3
                        menu:
                            bot"I might have to find out more before I can..."
                            "Help her..." if yoru_kneeled != True:
                                show boruto worried2 with dissolve
                                bot"Before I can help her..."
                                
                                bot"She is certainly hiding something from me... but what? More importantly, ...why? Does Obo have that much of a hold over her?"
                                bot"I should revisit this place during nights and see if I can figure out why exactly that is."
                                if ramennightscenescounter >= 2:
                                    bot"Unless... could it be the shinigami thing!?" with vpunch
                                    bot"I'll try bringing that up to her. See how she reacts..."
                            "Use her!":
                                show boruto sceeming2 with dissolve
                                bot"Before I can use her! She is definitely hiding something from me... but what?"
                                bot"I should revisit this place during nights and see if I can figure out what exactly that is."
                                if ramennightscenescounter >= 2:
                                    bot"Unless... could it be the shinigami thing!?" with vpunch
                                    bot"I'll try bringing that up to her. See how she reacts..."
                        $ config.menu_include_disabled = False
                            

                        
                    "So you are a... S-shinigami?" if yoruichi_talk_progress_formal >= 3 and ramennightscenescounter >=2:
                        $ yoruichi_talk_progress_formal = 4
                        show boruto surprised2 at left with dissolve
                        bo"So... A shinigami, huh?"
                        show yoru surprised with vpunch
                        show yoru at smallshake
                        yo"*Gasps!*"
                        show yoru shy with dissolve
                        yo"I... d-dont know what you are talking about..."
                        show boruto surprised3 with dissolve
                        bo"So it is true..."
                        show yoru:
                            easein 1 xpos -10
                        bo"Holy shit!" with vpunch
                        show boruto surprised2 with dissolve
                        bo"Wait! I have questions to ask!"
                        show boruto suspicious with dissolve
                        bot"It's clear by her reaction... it's true! She is a shinigami..."
                        bot"It's time I confront her about everything..."
                        hide boruto with dissolve
                        $ notification("All objectives completed")                   
                        "Interactions with Yoruichi are now unlocked. Your next interaction will advance your relationship based on your choice."

                    "(Locked)" if yoruichi_talk_progress_formal < 2:
                        "Options will become available as you uncover more of the story"
                        jump yoruichiformaltalkmenu

            "???" if yoruichi_talk_progress_formal <4:
                "Uncover Yoruichi's secret by exploring the ramen shop during nights and confront her about it to unlock."
                jump yoruichiformalmenu


            "Interactions":
                if score_3_claimed == True and yoruichi_talk_progress_formal >= 4:
                    show boruto normal at left with dissolve
                    show yoru shy at right with dissolve
                    bo"It seems you are insistent on hiding things from me..."
                    bo"You can't keep avoiding me Yoru... Not after what I've seen..."
                    bo"Not now that I know what I know..."
                    show yoru scared2 with dissolve
                    $ config.menu_include_disabled = True
                    yo"And what if I do keep avoiding you kid, what are you going to do... blackmail me?"
                    menu:
                        yo"And what if I do kid, what are you going to do... blackmail me?"
                        "No! I want to help..." if yoru_kneeled != True:
                            show boruto surprised2 with dissolve
                            call changeHatred(-1,"none") from _call_changeHatred_60
                            bo"W-what...? No! I want to help, Yoru..."
                            show yoru normal with dissolve
                            yo"Of what help could you possibly be kid? You are swimming  way out of your waters..."
                        "You'd kill me if I did...":
                            show boruto suspicious with dissolve
                            bo"Blackmail a shinigami? You'd kill me on the spot!"
                            show yoru shy with dissolve
                            yo"That's... not what shinigami do, kid..."
                        "If you leave me no choice...":
                            show boruto sceeming2 with dissolve
                            call changeHatred(1,"none") from _call_changeHatred_61
                            bo"If you leave me no choice..."
                            show yoru angry3 with dissolve
                            yo"What choice do I have you idiot! Your insistence on snooping around has forced my hand..."
                    show yoru angry3 with dissolve  
                    yo"God-fucking damn it!" with vpunch
                    show yoru scared with dissolve
                    yo"*Sigh*... Okay kid, you win!"
                    yo"If I don't tell you what you want to know you are just going to keep putting yourself and more importantly, me!~ In danger by snooping around anyway..."
                    yo"So ask your god-damned questions... I'll answer what I am able to, if you promise to stop spying on me and Obo and stay outside of my feet..."
                    $ yorumenu2 = []
                    menu yoruintromenu2:
                        set yorumenu2
                        yo"So ask your god-damned questions... I'll answer what I am able to, if you promise to stop spying on me and Obo and stay outside of my feet..."
                        "So... What the hell is a shinigami?":
                            default yoruintromenu2_1 = False
                            $ yoruintromenu2_1 = True
                            show boruto surprised2 with dissolve
                            bo"So... what exactly are you, what the hell is a shinigami?"
                            show yoru normal with dissolve
                            yo"Gods of death. Heralds of darkness, Evil incarnate..."
                            yo"We spread mortal disease, kill babies and reap human souls and harvest their remains..."
                            show boruto surprised3 with vpunch
                            bo"Huh!?" with vpunch
                            show yoru shy2 with dissolve
                            show boruto suspicious with dissolve
                            yo"That's just what your people think we are..."
                            show yoru shy with dissolve
                            yo"You can imagine why it would be problematic if my identity as a shinigami were to be known."
                            show yoru obedient with dissolve
                            yo"I've already told you how people treat me because of my skin-color. Now think how much worse it would be if people thought I also kill their babies and spread disease..."
                            show yoru shy2 with dissolve
                            yo"In reality... us shinigami, we are nothing more than guides."
                            show boruto surprised2 with dissolve
                            bo"G-guides...?"
                            yo"That's what we do... We escort the dead to what we call 'Soul Society', or what you mortals call, the afterlife..."
                            show boruto suspicious with dissolve
                            bo"That's... it?"
                            yo"Mostly..."
                            show yoru shy with dissolve
                            yo"We also possess a degree of spiritual powers. Some of us at least..."
                            show yoru obedient with dissolve
                            yo"I've lost most of mine when I was exiled from my place..."
                            menu:
                                yo"I've lost most of mine when I was exiled from my place..."
                                "So... you are powerless?":
                                    show boruto surprised2 with dissolve
                                    bo"So what you are saying is that... you are powerless?"
                                    yo"Essentially. I can still live for much longer than what you humans do. I can sustain injuries much more severe than what you can, but when it comes to combat prowess..."
                                    yo"I am... not what I used to be."
                                    menu:
                                        yo"I am... not what I used to be."
                                        "(I can use that!)":
                                            show boruto sceeming2 with dissolve
                                            call borutoevil from _call_borutoevil_3
                                            call changeHatred(1,"none") from _call_changeHatred_62
                                            bot"She just admitted to me she is worthless! Big mistake..."
                                            bot"I can do whatever I want with her without fearing for my life..."
                                            bot"hehehe!"
                                            show boruto suspicious with dissolve
                                            show yoru angry with dissolve
                                            yo"You have a weird look on your face kid... Don't get any ideas."
                                            show yoru angry3 with dissolve
                                            yo"I could still beat your ass with my bare hands were you to try anything stupid!"
                                            show boruto surprised2 with dissolve
                                            bo"Uh w-what? No... I was just thinking about what you said about living l-longer and sustaining injuries!"
                                            show yoru shy with dissolve
                                            show boruto suspicious with dissolve
                                            yo"Hmmm..."
                                            jump yoruintromenu2
                                        "I... see":
                                            show boruto suspicious with dissolve
                                            bo"I... see."
                                            bot"So she isn't much of a threat to Obo... or me."
                                            bot"Interesting..."
                                            jump yoruintromenu2

                                        
                                "I am sorry about that..." if yoru_kneeled != True:
                                    show boruto worried with dissolve
                                    bo"I am sorry about that..."
                                    yo"You reap what you sow kid... I've made my choices."
                                    yo"I still get to live much longer than what you humans do. I can sustain injuries much more severe than what you can, but when it comes to combat prowess..."
                                    yo"I am just... not what I used to be."
                                    bot"Interesting..."
                                    jump yoruintromenu2
                                

                        "You mentioned you are not from 'these places' before...":
                            default yoruintromenu2_2 = False
                            $ yoruintromenu2_2 = True
                            bo"You said that you are not from around our places before..."
                            show yoru shy2 with dissolve
                            yo"Yes... I used to serve as a captain of a shinigami squad back in my domain."
                            bot"Explains her muscular physique..."
                            yo"But I've long since been exiled for reasons I'd rather not disclose. I am no longer welcome there and if I were to be found, I'd be killed on the spot."
                            yo"Just another reason why I have to lay low, why my identity needs to be kept secret..."
                            show yoru shy with dissolve
                            yo"Do you realize the importance of that, kid?"
                            menu:
                                yo"Do you realize the importance of that, kid?"
                                "Makes sense...":
                                    show boruto worried with dissolve
                                    bo"That makes sense."
                                    bot"But why was she exiled... More importantly, why is she hesitant on saying why?"
                                    bot"I might have to look into that..."
                                "(I can use that to blackmail her!)":
                                    show boruto sceeming2 with dissolve
                                    call borutoevil from _call_borutoevil_4
                                    call changeHatred(1,"none") from _call_changeHatred_63
                                    bot"She is revealing all of her cards to me, hehehe!"
                                    bot"I can use that to blackmail the bitch! But all in due time, Obo might be a problem right now..."
                                    show boruto suspicious with dissolve
                                    bo"Uhh... yeah, sure!"
                                    show yoru obedient with dissolve
                                    yo"G-good..."
                            jump yoruintromenu2
                                    
                                

                        "Why does Obo have such a hold over you...":
                            default yoruintromenu2_3 = False
                            $ yoruintromenu2_3 = True
                            show boruto suspicious with dissolve
                            bo"Why does Obo have such a strong hold over you?"
                            bo"Why can't you just... run away?"
                            show yoru normal with dissolve
                            yo"I thought you were smarter than that kid..."
                            show yoru shy2 with dissolve
                            yo"I don't know how, but... he knows what I am."
                            yo"He threatened multiple times to let everyone know that I am a shinigami..."
                            show yoru shy with dissolve
                            yo"The moment I go against his word, is the moment I end up dead or imprisoned..."
                            show yoru obedient with dissolve
                            yo"He's also more than what he lets on, I think..."
                            yo"He knows people... I've seen him talk with important looking men."
                            yo"I don't know what exactly it is that he is... But he is certainly more than a ramen shop owner."
                            show boruto surprised2 with dissolve
                            bot"Oh yeah, the sword!"
                            menu :
                                bot"Oh yeah, the sword!"
                                "What about the sword he has upstairs!?":
                                    show boruto suspicious with dissolve
                                    bo"That must be connected with that sword he has laying around upstairs... Do you know anything about that?"
                                    show yoru shy2 with dissolve
                                    yo"He says it's... decorative or something."
                                    yo"Last time I asked him about it he said that 'Hopefully, he won't have to use it.'"
                                    show yoru shy with dissolve
                                    yo"I think that was a threat... but I am not sure."
                            bo"Maybe you can snoop around instead, see if you can find anything else!"
                            show yoru scared2 with dissolve
                            yo"I can't!"
                            bo"Why not? Don't you live here?"
                            show yoru shy with dissolve
                            yo"He doesn't let me roam around outside of the kitchen..."
                            show yoru obedient with dissolve
                            yo"And during nights I am... confined in his room. You've seen how he is."
                            yo"Besides, I am... scared of him kid. He knows too much about me and I know too little about him..."
                            bot"... She is not wrong"
                            jump yoruintromenu2

                        "So what's your end-game here?" if yoruintromenu2_1 == True and yoruintromenu2_2 == True and yoruintromenu2_3 == True:
                            show boruto normal with dissolve
                            bo"You certainly don't enjoy being around here... so what's your end-game then?"
                            show yoru normal with dissolve
                            yo"I told you already that I owe some dangerous people back in my place a lot of money..."
                            show yoru shy3 with dissolve
                            yo"If I ever want to go back, I'll have to gather enough money to pay them off first."
                            yo"And if not, I'll just have to gather enough to be able to run far away from here and lay low somewhere else."
                            yo"In either case, it's way too soon to start plotting an escape plan."
                            show yoru shy with dissolve
                            yo"I am still dependant on Obo's 'help' for now..."
                            show yoru angry with dissolve
                            yo"But when the time is right, I..."
                            show yoru angry2 with dissolve
                            show yoru at smallshake
                            yo"I will...!"
                            yo"..."
                            show boruto suspicious with dissolve
                            bot"She won't outright say the words in front of me, But I am sure she is thinking about revenge..."
                            bot"She is still careful about what she lets on. To be fair, why would she trust me... She knows nothing about me."
                            show yoru normal2 with dissolve
                            jump yoruchoice1
                    label yoruchoice1:   
                    # bo"But the truth is, I've been hiding something from you as well."
                    # bo"In good faith, I'll let you in on my secret and in return, you'll let me in yours..."
                    show boruto normal with dissolve
                    bo"I finally feel like I understand most of what's going on..."
                    show boruto smirk with dissolve
                    bo"Nice of you to open up..."
                    show yoru scared with dissolve
                    yo"It was never my intention kid. You... almost coerced me into it!"
                    show boruto normal with dissolve
                    bo"Be that as it may, I now know things about you..."
                    show yoru angry3 with dissolve
                    yo"You know nothing!"
                    bo"And you know nothing about me. I think it's only fair we mend that..."
                    show yoru normal with dissolve
                    show boruto suspicious with dissolve
                    bo"The truth is... I've been hiding something from you as well Yoru..."
                    "You are about to reveal to Yoruichi how your condition affects your thinking. The way you choose to do it will advance your relationship in one of two different states"
                    show yoru shy with dissolve
                    yo"W-what are you talking about..."
                    $ config.menu_include_disabled = False                 
                    menu formaapproachmenu:
                        yo"W-what are you talking about..."
                        "Approach her with good intentions":
                            show boruto suspicious behind yoru:
                                easein 1 xalign 0.5
                            if yoru_kneeled == True:
                                bo"You know... I've had a bit of a change of heart hearing your story."
                            bo"The way I see it, you have two options..."
                            bo"You either let yourself keep getting berated and degraded by some old fuck. Or... you choose to trust me and see where that'll get us."
                            bo"Which one will it be, Yoru?"
                            show yoru scared with dissolve
                            yo"You have no idea what you are getting yourself involved in..."
                            show yoru scared2 with dissolve
                            yo"Besides, you are just a kid. How could you even possibly be of any help?"
                            menu:
                                yo"Besides, you are just a kid. How could you even possibly be of any help?"
                                "I might have a plan...":
                                    bo"I might have a plan, Yoru..."
                                    yo"A... plan?"
                                    bo"Yes. A plan that would have you making more money than you could ever imagine, but more importantly..."
                                    bo"You'd be doing that away from Obo, without having to compromise your identity."
                                    show yoru surprised with dissolve
                                    yo"R-really!?" with vpunch
                                    show yoru obedient with dissolve
                                    yo"How...?"
                                    bo"Let's not get carried away, I am still working on it. For now, you are just going to have to trust me..."
                                    bo"You've heard what Obo said when he had me give out commands to you, right?"
                                    yo"Y-yes..."
                                    bo"That's right, he trusts me enough to grant me full authority over this kitchen and over you, Yoru..."
                                    bo"But I don't want to use that against you, instead we could use that in our favor..."
                                    bo"We'll play his little game.... I will pretend like I am enjoying the authority but in reality..."
                                    bo"We'd be plotting our own machinations behind his back."
                                    bo"For this to work... you are going to have to trust me Yoru."
                                    bo"And you'd also need to help me..."
                                    show yoru obedient with dissolve
                                    yo"H-help you... how? Why would you go to this length for... m-me?"
                                    menu:
                                        yo"H-help you... how? Why would you go to this length for... m-me?"
                                        "Because I like you":
                                            show boruto worried2 with dissolve
                                            bo"Because I like you Yoru..."
                                            show yoru obedient
                                            yo"You... like me?"
                                            bo"You are beautiful and you deserve more than what Obo will ever give you..."
                                        "Because you deserve better":
                                            show boruto worried2 with dissolve
                                            bo"Because I've seen how Obo treats you..."
                                            show yoru obedient
                                            yo"..."
                                            bo"A nice girl like you deserves better than that, Yoru..."
                                    bo"But things might not be so simple. Remember when I said you know nothing about me?"
                                    bo"I was recently diagnosed with a rare condition..."
                                    yo"A condition? Are you... dying, kid?"
                                    bo"Worse, I am afraid..."
                                    bo"It's more like an affliction, or a curse of sorts that leaves me almost permanently in a state of... arousal."
                                    show yoru surprised with dissolve
                                    yo"A-arousal!?" with vpunch
                                    show yoru shy with dissolve
                                    bo"PGAD, is what the doctor called it. A disorder of sorts that if left unchecked, slowly eats away at me and my morals..."
                                    bo"The longer I stay in that state, the more likely it is for me to turn into a psycopathic, violent and depraved person..."
                                    show yoru obedient with dissolve
                                    yo"Good grief... W-what do you want me to do with this information kid..."
                                    bo"I am sure you can see how being around someone as beautiful as you could affect my condition..."
                                    bo"I am just letting you know, the way I act might not always correlate with the way I am."
                                    bo"For now, I just need you to trust me..."
                                    show boruto suspicious behind yoru:
                                        easein 1 xalign 0.77 zoom 1.05
                                    bo"Can you do that for me?"
                                    menu:
                                        bo"Can you do that for me?"
                                        "Put your hand on her waist":
                                            show yorucutout_waist:
                                                zoom 0.25 xalign 0.1 yalign 0.1
                                            
                                            show cutoutborder_white:
                                                zoom 0.75 pos (-0.04,-109)
                                            with dissolve
                                            yo"If that is all..."
                                            yo"I suppose it's the least I could do for you."
                                            
                                        "Put your hand on her ass":
                                            show boruto sceeming with dissolve
                                            show yoru shy at smallshake with dissolve
                                            show yorucutout_ass:
                                                zoom 0.25 xalign 0.1 yalign 0.1
                                            
                                            show cutoutborder_white:
                                                zoom 0.75 pos (-0.04, -109)
                                            with dissolve
                                            
                                            yo"H-hey... I~"
                                            yo"I s-suppose I could do that f-for you..."
                                    $ notification ("Yoruichi's relationship changed")
                                    "Yoruichi's status is now 'Obedient'"
                                    $ yoruichi_relationship = "Obedient"
                                    $ shifts_completed = 0
                                    $ borutonicetoyoru = True
                                    hide yoru
                                    hide boruto
                                    hide cutoutborder_white
                                    hide yorucutout_ass
                                    hide yorucutout_waist
                                    with dissolve
                                    "Yoruichi will now listen to you, but if you push her too far her relationship might change to 'Apprehensive', In which case you'll have to earn her trust back."
                                    "There is still some content to see, but this is the end of Obo and Yoruichi's story for this version of the game."
                                    "In the future, you'll have the option of making a definitive choice that will cement your relationship with both, Yoruichi and Obo."

                                        
                                            
                        "{color=[hatredcolor]}Approach her threateningly{/color}":
                            show boruto sceeming2 behind yoru:
                                easein 1 xalign 0.5
                            
                            bo"You see Yoru... You've made one crucial mistake!"
                            show yoru shy at smallshake with dissolve
                            yo"H-huh?"
                            bo"You've revealed your hand to me, and it seems like..."
                            show boruto sceeming3 with dissolve
                            bo"The cards you've been dealt are SHIT!" with vpunch
                            show yoru scared2 with dissolve
                            yo"Kid... What are you talking about?"
                            show boruto sceeming with dissolve
                            bo"Tell me if I got this right..."
                            bo"So you are a a shinigami, in nothing but name!"
                            bo"With no godly powers, exiled from your home and hated by humans for what you are!"
                            bo"Your misfortune does not end there... as you happen to bear the same skin-complexion as the enemy of the village you found yourself in which only serves to further incite the discrimination you have to endure."
                            bo"As such, you let yourself get reeled in by someone you thought you could trust only for him to essentially imprison you in his quarters to use and abuse you in any way he pleases."
                            show boruto sceeming2 with dissolve
                            bo"That same person is now entrusting me, to do with you as I see fit..."
                            show boruto sceeming3 with dissolve
                            call borutoevil2 from _call_borutoevil2_12
                            call changeHatred(1,"none") from _call_changeHatred_64
                            bo"Do you see where I am going with this, Yoru!?"
                            show yoru obedient with dissolve
                            show yoru at smallshake
                            yo"Kid p-please... W-what are you saying!? I though I could t-trust you..."
                            menu:
                                yo"Kid p-please... W-what are you saying!? I though I could t-trust you..."
                                "{color=[hatredcolor]}Use what you know against her!{/color}":
                                    show boruto sceeming3 behind yoru:
                                        easein 1 xalign 0.85 zoom 1.05
                                    bo"I'll tell you what, you will be my obedient little bitch... And maybe I'll consider not exposing your secrets!"
                                    menu:
                                        bo"I'll tell you what, you will be my obedient little bitch... And maybe I'll consider not exposing your secrets!"
                                        "Grope her tits":
                                            hide boruto
                                            hide yoru
                                            show behindstart00 with dissolve:
                                                zoom 0.55 xalign 0.8 yalign 0.5
                                            show behindstart00 at smallshake
                                            yo"A-aarh!" with vpunch
                                            show behindstart00 at smallshake
                                            yo"W-what are you..."
                                            show behindstart00 at smallshake
                                            bo"Do we have an agreement!?"
                                            show blackscreen with vpunch
                                            hide behindstart00 with dissolve
                                            hide blackscreen
                                            show yoru angry3 at right
                                            show boruto sceeming2 at right behind yoru
                                            show boruto:
                                                easein 0.5 xalign 0.4
                                            with dissolve
                                            yo"I knew you were just another piece of shit, you are no different from Obo!"
                                            yo"You only pretended to care so you could use me..."
                                            show yoru lookingbackt with dissolve:
                                                zoom 0.5 ypos 1.04
                                            show yoru at smallshake
                                            yo"I am never trusting you again, stay away from me!"
                                            hide yoru with dissolve
                                            show boruto sceeming3 with dissolve
                                            bot"You'll belong to me before you know it you bitch!"
                                            hide boruto with dissolve

                                        "Grope her ass":
                                            show boruto sceeming3 behind yoru:
                                                easein 1 xalign 0.87 zoom 1.07
                                            pause 0.5
                                            show yorucutout_waist:
                                                zoom 0.25 xalign 0.1 yalign 0.1
                                            
                                            show cutoutborder_white:
                                                zoom 0.75 pos (-0.04,-109)
                                            with dissolve
                                            
                                            bo"Do we have an agreement?"
                                            show boruto sceeming2 with dissolve
                                            show yoru shy at smallshake with dissolve:
                                                xzoom -1
                                            $ renpy.sound.play("/audio/soun_fx/groperepeat1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                            show yoru_gropeass1_anim1:
                                                zoom 0.25 xalign 0.1 yalign 0.1
                                            
                                            show cutoutborder_white:
                                                zoom 0.75 pos (-0.04, -109)
                                            with dissolve
                                            show yoru at smallshake
                                            yo"W-what the hell are you doing!"
                                            bo"Using my plaything...!"
                                            show blackscreen with vpunch
                                            hide yoru_gropeass1_anim1
                                            hide cutoutborder_white
                                            hide yorucutout_waist
                                            hide blackscreen
                                            show yoru angry3 at right
                                            show boruto sceeming2 at right behind yoru
                                            show boruto:
                                                easein 0.5 xalign 0.4
                                            with dissolve
                                            yo"Don't touch me you little shit!"
                                            yo"I knew you were just another asshole, you are no different from Obo!"
                                            yo"You only pretended to care so you could use me..."
                                            show yoru lookingbackt with dissolve:
                                                zoom 0.5 ypos 1.04
                                            show yoru at smallshake
                                            yo"I am never trusting you again, stay away from me!"
                                            hide yoru with dissolve
                                            show boruto sceeming3 with dissolve
                                            bot"You'll belong to me before you know it you bitch!"
                                            hide boruto with dissolve
                                        
                                    $ notification ("Yoruichi's relationship changed")
                                    "Yoruichi's status is now 'Apprehensive'"
                                    $ yoruichi_relationship = "Apprehensive"
                                    $ shifts_completed = 0
                                    $ borutonicetoyoru = False
                                    "Yoruichi knows you have a hold over her but she despises you."
                                    hide yoru
                                    hide boruto
                                    hide cutoutborder_white
                                    hide yorucutout_ass
                                    hide yorucutout_waist
                                    with dissolve
                                    "You can try 'earning' back some of her trust by bribing her and offering money in which case her relationship might change to 'Unwillingly Obedient', but never 'Obedient'"
                                    "There is still some content to see, but this is the end of Obo and Yoruichi's story for this version of the game."
                                    "In the future, you'll have the option of making a definitive choice that will cement your relationship with both, Yoruichi and Obo."
                                    jump ramenkitchenmenu


                else:
                    "Option will become available as you uncover more of the story."
                    jump yoruichiformalmenu
    
        $ yoruichiinteractiontaken = True
        jump ramenkitchenmenu




    #Apprehensive ---------------------------------------------------------------------------
    elif yoruichi_relationship == "Apprehensive":
        show boruto sceeming at left with dissolve
        bo"Hey Yoru!"
        show yoru shy at right with dissolve
        yo"W-what do you want a-asshole!"
        menu yoruichiapprehensivemenu:
            "..."
            "Talk with Yoruichi":
                show boruto sceeming with dissolve
                bo"Come on, let's... talk!"
                show yoru scared2 with dissolve
                yo"After w-what you've done...?"
                menu yoruichiapprehensivetalkmenu:
                    yo"After w-what you've done...?"
                    "How's the kitchen's whore doing?":
                        if yoruichi_talk_progress_apprehensive >= 1:
                            show boruto sceeming2 with dissolve
                            bo"Is the kitchen's whore still defiant?"
                            show yoru angry3 with dissolve
                            yo"Stop calling me that!"
                            show boruto:
                                easein 1 xalign 0.8
                            bo"I'll call you whatever I damn please..."
                            show yoru obedient with dissolve
                            menu:
                                bo"I'll call you whatever I damn please..."
                                "Spank her":
                                    show yorucutout_spank0:
                                        zoom 0.25 xalign 0.1 yalign 0.1
                                    
                                    show cutoutborder_white:
                                        zoom 0.75 pos (-0.044,-108)
                                    with dissolve
                                    
                                    hide yorucutout_spank0
                                    hide cutoutborder_white
                                    with dissolve
                                    show cutoutborder_white:
                                        zoom 0.75 pos (-0.044,-108)
                                    show yorucutout_spank1 at smallshake:
                                        zoom 0.25 xalign 0.1 yalign 0.1
                                    $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                    show yoru at smallshake
                                    show yoru angry2
                                    show boruto sceeming3 with dissolve
                                    bo"You WHORE!"
                                    yo"That hurts!" with vpunch
                                    show blackscreen with vpunch
                                    hide yorucutout_spank0
                                    hide yorucutout_spank1
                                    hide yoru_gropeass1_anim1
                                    hide cutoutborder_white
                                    hide yorucutout_waist
                                    hide blackscreen
                                    show yoru angry3 at right
                                    show boruto sceeming2 at right behind yoru
                                    show boruto:
                                        easein 0.5 xalign 0.4
                                    with dissolve
                                    bo"If you want it to stop, you better start obeying me..."
                                    yo"*scoffs*"
                                    show yoru lookingbackt with dissolve:
                                        zoom 0.5 ypos 1.04
                                    yo"..."
                                    hide yoru with dissolve
                                    hide boruto with dissolve

                        else:
                            show boruto sceeming2 with dissolve
                            bo"How's the kitchen's whore doing?"
                            show yoru angry3 with dissolve
                            yo"You won't talk to me like that kid, I have 20 years on you... I could be your mother!"
                            show boruto:
                                easein 1 xalign 0.5
                            bo"And yet, all you are is an annoying bitch. But don't you worry, I have a plan for you..."
                            show boruto:
                                easein 1 xalign 0.8
                            show yoru obedient with dissolve
                            menu:
                                bo"And yet, all you are is an annoying bitch. But don't you worry, I have a plan for you..."
                                "Spank her":
                                    show yorucutout_spank0:
                                        zoom 0.25 xalign 0.1 yalign 0.1
                                    
                                    show cutoutborder_white:
                                        zoom 0.75 pos (-0.044,-108)
                                    with dissolve
                                    
                                    bo"And when my plan is set in motion..."
                                    hide yorucutout_spank0
                                    hide cutoutborder_white
                                    with dissolve
                                    show cutoutborder_white:
                                        zoom 0.75 pos (-0.044,-108)
                                    show yorucutout_spank1 at smallshake:
                                        zoom 0.25 xalign 0.1 yalign 0.1
                                    $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                    show yoru at smallshake
                                    show yoru angry2
                                    show boruto sceeming3 with dissolve
                                    bo"You'll be following my every word like a dog..."
                                    yo"That hurts!" with vpunch
                                    show blackscreen with vpunch
                                    yo"W-what the hell are you doing!"
                                    hide yorucutout_spank0
                                    hide yorucutout_spank1
                                    hide yoru_gropeass1_anim1
                                    hide cutoutborder_white
                                    hide yorucutout_waist
                                    hide blackscreen
                                    show yoru angry3 at right
                                    show boruto sceeming2 at right behind yoru
                                    show boruto:
                                        easein 0.5 xalign 0.4
                                    with dissolve
                                    bo"Just some pre-emptive training Yoru. Don't worry..."
                                    show boruto sceeming3 with dissolve
                                    bo"As long as you start obeying me... you won't have to go through too much of my 'training'"
                                    yo"You are disgusting..."
                                    show yoru lookingbackt with dissolve:
                                        zoom 0.5 ypos 1.04
                                    yo"I will never obey you."
                                    hide yoru with dissolve
                                    bot"We'll see about that, bitch!"
                                    hide boruto with dissolve
                                "Don't":
                                    bo"You better rethink your approach, or I'll have to change mine..."
                                    show yoru angry3 with dissolve
                                    yo"Don't threaten me kid... You try anything funny and I'll kick your teeth in!"
                                    hide yoru with dissolve
                                    show boruto sceeming with dissolve
                                    bot"I thought I'd give you a chance but it seems you'd rather learn the hard way Yoru..."
                                    bot"I won't be as nice next time!"
                                    hide boruto with dissolve
                            $ yoruichi_talk_progress_apprehensive = 1
                            
                    
                    "You know you can't keep this defiant act up for long..." if yoruichi_talk_progress_apprehensive >= 1:
                        $ yoruichi_talk_progress_apprehensive = 2
                        bo"You know you can't keep this defiant act up for much longer..."
                        show yoru obedient with dissolve
                        yo"..."
                        show boruto sceeming2 with dissolve
                        show boruto:
                            easein 1 xalign 0.5
                        bo"The silent treatment eh? Don't you worry Yoru, soon enough you'll be barking at my command!"
                        show yoru lookingbackt with dissolve:
                            zoom 0.51 ypos 1.04
                        yo"*Scoffs*"
                        show boruto:
                            easein 0.4 xalign 0.77
                        bo"You can't just turn around and show me your ass like that..." with vpunch
                        hide yoru 
                        hide boruto 
                        show yoru_turnaroundgrope:
                            zoom 0.7 xalign 0.88 ypos -110
                        with dissolve
                        show yoru_turnaroundgrope at smallshake
                        pause 1
                        bo"That's just an invitation!" with vpunch
                        show blackscreen with vpunch
                        yo"Get off me, kid!"
                        hide yoru_turnaroundgrope
                        show boruto sceeming2 at center
                        hide blackscreen
                        with dissolve
                        bot"You'll be mine soon!"
                        hide boruto with dissolve

                    "(Locked)" if yoruichi_talk_progress_apprehensive < 1:
                        "Options will become available as you keep interacting with Yoruichi"
                        jump yoruichiapprehensivetalkmenu
                    
                    "Changed your mind yet?" if yoruichi_talk_progress_apprehensive >= 2:
                        $ yoruichi_talk_progress_apprehensive = 3
                        show boruto sceeming with dissolve
                        show yoru shy with dissolve
                        bo"Changed your mind yet?"
                        show yoru obedient with dissolve
                        yo"N-no..."
                        show boruto:
                            easein 1 xalign 0.7
                        bo"Think of it like this... Would you rather obey me, or Obo..."
                        menu:
                            bo"Think of it like this... Would you rather obey me, or Obo..."
                            "Grope her":
                                show boruto sceeming3 behind yoru with dissolve:
                                    easein 1 xalign 0.87 zoom 1.07
                                pause 0.5
                                show yorucutout_waist:
                                    zoom 0.25 xalign 0.1 yalign 0.1
                                
                                show cutoutborder_white:
                                    zoom 0.75 pos (-0.04,-109)
                                with dissolve
                                
                                yo"W-what could you provide me that Obo can't..."
                                show boruto sceeming2 with dissolve
                                show yoru shy at smallshake with dissolve:
                                    xzoom -1
                                $ renpy.sound.play("/audio/soun_fx/groperepeat1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                show yoru_gropeass1_anim1:
                                    zoom 0.25 xalign 0.1 yalign 0.1
                                
                                show cutoutborder_white:
                                    zoom 0.75 pos (-0.04, -109)
                                with dissolve
                                show yoru at smallshake
                                bo"That's dependant on what you provide me first!"
                                bo"Don't you think?"
                                yo"..."
                                bo"You make yourself useful and I might even consider doing something about Obo for you..."
                                show blackscreen with vpunch
                                hide yoru_gropeass1_anim1
                                hide cutoutborder_white
                                hide yorucutout_waist
                                hide blackscreen
                                show boruto:
                                    easein 0.5 xalign 0.4
                                show yoru angry3 at right with dissolve
                                yo"E-Enough!"
                                
                                with dissolve
                            "Don't":
                                yo"W-what could you provide me that Obo can't..."
                                bo"That's dependant on what you provide me!"
                                bo"Don't you think?"
                                bo"You make yourself useful and I might even consider doing something about Obo for you..."
                                show yoru shy with dissolve
                                yo"I'll... t-think about it."
                        hide yoru with dissolve
                        bot"She is warming up to me, I can feel it."
                        bot"Soon enough, she'll be bouncing on my cock!"
                        hide boruto with dissolve
                            

                    "(Locked)" if yoruichi_talk_progress_apprehensive < 2:
                        "Options will become available as you keep interacting with Yoruichi"
                        jump yoruichiapprehensivetalkmenu
                    
            "Interactions":
                menu:
                    "Bribing Yoruichi at least three times will earn back her 'trust'\nCurrent bribes: [sharemoneywithyorucounter]"
                    "Bribe":
                        if sharemoneywithyorucounter == 0:
                            $ sharemoneywithyorucounter +=1
                            $ sharemoneywithyoru = True
                            show boruto sceeming with dissolve
                            bo"Hey come on... It wasn't that bad!"
                            bo"I'll tell you what, if I give you half of my payment this shift, will you forgive me?"
                            yo"Is that how you treat women, kid? You buy them off?"
                            menu:
                                yo"Is that how you treat women, kid? You buy them off?"
                                "Only the pretty ones I like":
                                    bo"Only pretty girls like you..."
                                    show boruto sceeming2 behind yoru:
                                        easein 1 xalign 0.85 zoom 1.07
                                    bo"Do you think I'd do this for anyone? I like you Yoru..."
                                    menu:
                                        bo"Do you think I'd do this for anyone? I like you Yoru..."
                                        "Grope her ass":
                                            show yoru shy at smallshake with dissolve
                                            $ renpy.sound.play("/audio/soun_fx/groperepeat1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                            show yoru_gropeass1_anim1:
                                                zoom 0.25 xalign 0.1 yalign 0.1
                                            
                                            show cutoutborder_white:
                                                zoom 0.75 pos (-0.04, -109)
                                            with dissolve
                                            show yoru at smallshake
                                            bo"And the girls I like, I also take care of!"
                                            show yoru obedient with dissolve
                                            yo"W-words are just words..."
                                            hide yoru_gropeass1_anim1
                                            hide cutoutborder_white
                                            with dissolve
                                            yo"You'll need to do more than that to earn my trust"
                                            hide boruto
                                            hide yoru
                                            with dissolve
                                "Only whores like you!":
                                    show boruto sceeming2 behind yoru:
                                        easein 1 xalign 0.6 zoom 1.02
                                    bo"I know you need the money..."
                                    show yorucutout_spank0:
                                        zoom 0.25 xalign 0.1 yalign 0.1
                                    
                                    show boruto sceeming3 behind yoru:
                                        easein 1 xalign 0.85 zoom 1.07
                                    show cutoutborder_white:
                                        zoom 0.75 pos (-0.044,-108)
                                    with dissolve

                                    bo"Don't you, you little...!"
                                    menu:
                                        bo"Don't you, you little...!"
                                        "Spank her!":
                                            pass
                                        
                                        
                                    hide yorucutout_spank0
                                    hide cutoutborder_white
                                    with dissolve
                                    show cutoutborder_white:
                                        zoom 0.75 pos (-0.044,-108)
                                    show yorucutout_spank1 at smallshake:
                                        zoom 0.25 xalign 0.1 yalign 0.1
                                    $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                    show yoru at smallshake
                                    show yoru angry2 with dissolve
                                    yo"Aah!" with vpunch
                                    bo"...Whore!"
                                    show boruto sceeming2 with dissolve
                                    
                                    hide yorucutout_spank0
                                    hide yorucutout_spank1
                                    hide yoru_gropeass1_anim1
                                    hide cutoutborder_white
                                    hide yorucutout_waist
                                    show yoru angry3 at right with dissolve
                                    yo"..."
                                    bo"I'll take your silence as a yes then!"
                                    hide yoru
                                    hide boruto
                                    with dissolve
                            "You'll split next shift's payment with Yoruichi..."

                                
                        elif sharemoneywithyorucounter == 1:
                            $ sharemoneywithyorucounter +=1
                            $ sharemoneywithyoru = True
                            bo"Still with that face, Yoru?"
                            bo"So cold... And here I thought we were friends."
                            show boruto sceeming2 behind yoru:
                                easein 1 xalign 0.80 zoom 1.02
                            bo"Do you need some more of my shift's payments?"
                            yo"..."
                            bo"Cat got your tongue?"
                            menu:
                                bo"Cat got your tongue?"
                                "Spank her":
                                    show boruto sceeming2 behind yoru:
                                        easein 1 xalign 0.85 zoom 1.07
                                    show yorucutout_spank0:
                                        zoom 0.25 xalign 0.1 yalign 0.1
                                    
                                    show cutoutborder_white:
                                        zoom 0.75 pos (-0.044,-108)
                                    with dissolve
                                    bo"Staying silent, eh?"
                                    menu:
                                        bo"Staying silent, eh?"
                                        "Spank her!":
                                            pass
                                        
                                    bo"I'll take that as a yes then!"
                                    hide yorucutout_spank0
                                    hide cutoutborder_white
                                    with dissolve
                                    show cutoutborder_white:
                                        zoom 0.75 pos (-0.044,-108)
                                    show yorucutout_spank1 at smallshake:
                                        zoom 0.25 xalign 0.1 yalign 0.1
                                    $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                    show yoru at smallshake
                                    show yoru angry2
                                    show boruto sceeming3 with dissolve
                                    yo"Aah!" with vpunch
                                    hide yorucutout_spank0
                                    hide yorucutout_spank1
                                    hide yoru_gropeass1_anim1
                                    hide cutoutborder_white
                                    hide yorucutout_waist
                                    show boruto sceeming2 with dissolve
                                    bo"Atta girl!"
                                    bo"I like you better when you aren't barking at me"
                                    show yoru angry3 at right with dissolve
                                    yo"*scoffs*"
                                    yo"M-make sure you pay me my s-share..."
                                    hide yoru
                                    hide boruto
                                    with dissolve

                               
                            "You'll split next shift's payment with Yoruichi..."
                                
                        elif sharemoneywithyorucounter == 2:
                            $ sharemoneywithyoru = True
                            bo"I know what that look on your face means Yoru..."
                            bo"You are practically begging for more money, aren't you?"
                            show boruto sceeming2 with dissolve
                            bo"I'll give you your share of this shift, so long as you promise that we'll go back to being... friends!"
                            bo"Can you do that for me?"
                            yo"O-Okay..."
                            menu:
                                yo"O-Okay..."
                                "Say the words!":
                                    show boruto sceeming2 behind yoru:
                                        easein 1 xalign 0.7 zoom 1.01
                                    show yoru obedient with dissolve
                                    bo"That wasn't a promise, was it?"
                                    bo"Say the words Yoru! I need to know you mean it..."
                                    show yoru shy with dissolve
                                    yo"I promise [bo_name]... We'll be f-friends."
                                    menu:
                                        yo"I promise [bo_name]... We'll be f-friends."
                                        "Spank her roughly!":
                                            show boruto sceeming3 behind yoru with dissolve:
                                                easein 1 xalign 0.85 zoom 1.07
                                            show yorucutout_spank0:
                                                zoom 0.25 xalign 0.1 yalign 0.1
                                            
                                            show cutoutborder_white:
                                                zoom 0.75 pos (-0.044,-108)
                                            with dissolve
                                            bo"Remember your promise..."
                                            hide yorucutout_spank0
                                            hide cutoutborder_white
                                            with dissolve
                                            show cutoutborder_white:
                                                zoom 0.75 pos (-0.044,-108)
                                            show yorucutout_spank2 at shake:
                                                zoom 0.25 xalign 0.1 yalign 0.1
                                            $ renpy.sound.play("/audio/soun_fx/spank8.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                            with vpunch
                                            show yoru at smallshake
                                            show yoru scared2 with dissolve
                                            yo"Aah!" with vpunch
                                            show boruto sceeming3 with dissolve
                                            hide yorucutout_spank0
                                            hide yorucutout_spank2
                                            hide cutoutborder_white
                                            hide yorucutout_waist
                                            with dissolve
                                            show boruto sceeming2 with dissolve
                                            bo"Atta girl!"
                                            show yoru shy with dissolve
                                            show boruto sceeming2 behind yoru with dissolve:
                                                easein 0.5 xalign 0.7 zoom 1.00
                                            bo"I trust that you won't be as defiant next time we see each other..."
                                            hide yoru
                                            hide boruto
                                            with dissolve
                                            
                                    

                                        
                                "That's my girl!":
                                    bo"That's my girl..."
                                    menu:
                                        bo"That's my girl..."
                                        "Spank her roughly":
                                            show boruto sceeming3 behind yoru with dissolve:
                                                easein 1 xalign 0.85 zoom 1.07
                                            show yorucutout_spank0:
                                                zoom 0.25 xalign 0.1 yalign 0.1
                                            
                                            show cutoutborder_white:
                                                zoom 0.75 pos (-0.044,-108)
                                            with dissolve
                                            bo"Let this be the day that marks the start of our new relationship!"
                                            hide yorucutout_spank0
                                            hide cutoutborder_white
                                            with dissolve
                                            show cutoutborder_white:
                                                zoom 0.75 pos (-0.044,-108)
                                            show yorucutout_spank2 at shake:
                                                zoom 0.25 xalign 0.1 yalign 0.1
                                            $ renpy.sound.play("/audio/soun_fx/spank8.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                            with vpunch
                                            show yoru at smallshake
                                            show yoru scared2 with dissolve
                                            yo"Aah!" with vpunch
                                            show boruto sceeming3 with dissolve
                                            hide yorucutout_spank0
                                            hide yorucutout_spank2
                                            hide cutoutborder_white
                                            hide yorucutout_waist
                                            with dissolve
                                            show boruto sceeming2 with dissolve
                                            bo"Atta girl!"
                                            show yoru shy with dissolve
                                            show boruto sceeming2 behind yoru with dissolve:
                                                easein 0.5 xalign 0.7 zoom 1.00
                                            bo"I trust that you won't be as defiant next time we see each other..."
                                            hide yoru
                                            hide boruto
                                            with dissolve
                                        "Spare her":
                                            bo"See? It's not so hard when you are cooperative..."
                                            show yoru obedient with dissolve
                                            yo"Y-yes, t-thank you."
                                            show boruto surprised2 with dissolve
                                            bot"Oh? I did not expect her to be... appreciative!"
                                            show boruto sceeming2 with dissolve
                                            show yoru lookingbackt with dissolve:
                                                zoom 0.5 ypos 1.04
                                            bot"I like where this is going!"
                                            hide yoru
                                            hide boruto
                                            with dissolve

                            "You'll split next shift's payment for the final time with Yoruichi..."
                            $ yoruichi_relationship = "Unwillingly Obedient"
                            $ shifts_completed = 0
                            $ sharemoneywithyorucounter = 0
                            $ notification ("Yoruichi's relationship changed")
                            "Yoruichi's status is now 'Unwillingly Obedient'."
                                

                    
                    "Return":
                        jump yoruichiapprehensivemenu
                    
                        
        $ yoruichiinteractiontaken = True
        hide yoru with dissolve
        jump ramenkitchenmenu


    #Unwillingly Obedient ---------------------------------------------------------------------------
    elif yoruichi_relationship == "Unwillingly Obedient":
        show boruto sceeming at left with dissolve
        bo"Hey Yoru!"
        show yoru shy at right with dissolve
        yo"W-what do you want..."
        menu yoruichiunwillinglyobedientmenu:
            "..."
            "Talk with Yoruichi":
                show boruto sceeming with dissolve
                bo"Let's... talk!"
                show yoru scared2 with dissolve
                yo"After w-what you've done...?"
                menu yoruichiunwillinglyobedienttalkmenu:
                    yo"After w-what you've done...?"
                    "How's the kitchen's whore doing?":
                        
                        show boruto sceeming2 with dissolve
                        bo"How is the kitchen's whore doing!?"
                        show yoru obedient with dissolve
                        if yoruichi_talk_progress_unwillinglyobedient == 1:
                            show yoru angry3 with dissolve
                            yo"Please, not this again. Can't you address me like any normal kid would?"
                            show boruto:
                                easein 1 xalign 0.5
                            bo"Oh I am sorry ma'am... Did I rusttle your jimmies?"
                            menu:
                                bo"Oh I am sorry ma'am... Did I rusttle your jimmies?"
                                "Spank her":
                                    show boruto sceeming2 behind yoru:
                                        easein 1 xalign 0.75 zoom 1.02
                                    bo"You'll have to excuse me..."
                                    show boruto sceeming2 behind yoru:
                                        easein 1 xalign 0.85 zoom 1.07
                                    show yorucutout_spank0:
                                        zoom 0.25 xalign 0.1 yalign 0.1
                                    
                                    show cutoutborder_white:
                                        zoom 0.75 pos (-0.044,-108)
                                    with dissolve                                    
                                    hide yorucutout_spank0
                                    hide cutoutborder_white
                                    with dissolve
                                    show cutoutborder_white:
                                        zoom 0.75 pos (-0.044,-108)
                                    show yorucutout_spank1 at smallshake:
                                        zoom 0.25 xalign 0.1 yalign 0.1
                                    $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                    show yoru at smallshake
                                    show yoru angry2
                                    show boruto sceeming3 with dissolve
                                    bo"I was not aware you had a choice on the matter!"
                                    yo"..." with vpunch
                                    hide yorucutout_spank0
                                    hide yorucutout_spank1
                                    hide yoru_gropeass1_anim1
                                    hide cutoutborder_white
                                    hide yorucutout_waist
                                    show boruto sceeming2 with dissolve
                                    bo"Now keep it shut and follow my orders!"
                                    show yoru angry3 at right with dissolve
                                    yo"*Scoffs*"
                                    hide yoru
                                    hide boruto
                                    with dissolve
                                    
                                
                                
                        else:
                            yo"You won't talk to me like that kid, I have 20 years on you! I could be your mother..."
                            show boruto:
                                easein 1 xalign 0.5
                            bo"And yet, all you are is an obnoxious bitch. But don't you worry, I have a plan for you..."
                            menu:
                                bo"And yet, all you are is an obnoxious bitch. But don't you worry, I have a plan for you..."
                                "Spank her":
                                    show boruto sceeming2 behind yoru:
                                        easein 1 xalign 0.75 zoom 1.02
                                    bo"And once my plan is set in motion..."
                                    show boruto sceeming2 behind yoru:
                                        easein 1 xalign 0.85 zoom 1.07
                                    show yorucutout_spank0:
                                        zoom 0.25 xalign 0.1 yalign 0.1
                                    
                                    show cutoutborder_white:
                                        zoom 0.75 pos (-0.044,-108)
                                    with dissolve
                                    yo"W-what are you doing..."
                                    
                                    hide yorucutout_spank0
                                    hide cutoutborder_white
                                    with dissolve
                                    show cutoutborder_white:
                                        zoom 0.75 pos (-0.044,-108)
                                    show yorucutout_spank1 at smallshake:
                                        zoom 0.25 xalign 0.1 yalign 0.1
                                    $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                    show yoru at smallshake
                                    show yoru angry2
                                    show boruto sceeming3 with dissolve
                                    yo"Aah!" with vpunch
                                    bo"You'll be obeying my every command!"
                                    hide yorucutout_spank0
                                    hide yorucutout_spank1
                                    hide yoru_gropeass1_anim1
                                    hide cutoutborder_white
                                    hide yorucutout_waist
                                    show boruto sceeming2 with dissolve
                                    bo"Atta girl!"
                                    bo"I like you better when you aren't barking..."
                                    show yoru angry3 at right with dissolve
                                    yo"*scoffs*"
                                    hide yoru
                                    hide boruto
                                    with dissolve

                        $ yoruichi_talk_progress_unwillinglyobedient = 1    
                    
                    "You know you can't keep this defiant act up for long..." if yoruichi_talk_progress_unwillinglyobedient >= 1:
                        $ yoruichi_talk_progress_unwillinglyobedient = 2
                        bo"You know you can't keep this defiant act up for much longer..."
                        show yoru obedient with dissolve
                        yo"..."
                        show boruto sceeming2 with dissolve
                        bo"The silent treatment eh?"
                        bo"Shame! Here I was coming up with a plan to help you out of this situation..."
                        bo"And you won't even talk to me? Have it your way..."
                        hide boruto with dissolve
                        show yoru shy with dissolve
                        yo"W-what? ... Wait!"
                        hide yoru with dissolve
                    "(Locked)" if yoruichi_talk_progress_unwillinglyobedient < 1:
                        "Options will become available as you uncover more of the story"
                        jump yoruichiunwillinglyobedienttalkmenu
                    
                    "I might have a plan for you!" if yoruichi_talk_progress_unwillinglyobedient >= 2:
                        $ yoruichi_talk_progress_unwillinglyobedient = 3
                        show boruto sceeming with dissolve
                        bo"I've been thinking Yoru..."
                        show yoru obedient with dissolve
                        yo"You do that? The thinking part I mean..."
                        show boruto angry with dissolve:
                            easein 1 xalign 0.5
                        bo"Are you making fun of me you bitch?"
                        show yoru shy2 with dissolve
                        yo"N-no?"
                        menu:
                            yo"N-no?"
                            "Punish her":
                                show boruto angry2 behind yoru with dissolve:
                                    easein 1 xalign 0.85 zoom 1.07
                                show yorucutout_spank0:
                                    zoom 0.25 xalign 0.1 yalign 0.1
                                
                                show cutoutborder_white:
                                    zoom 0.75 pos (-0.044,-108)
                                with dissolve
                                bo"Here I am, trying to help you..."
                                hide yorucutout_spank0
                                hide cutoutborder_white
                                with dissolve
                                show cutoutborder_white:
                                    zoom 0.75 pos (-0.044,-108)
                                show yorucutout_spank2 at shake:
                                    zoom 0.25 xalign 0.1 yalign 0.1
                                $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                with vpunch
                                show yoru at smallshake
                                show yoru scared2 with dissolve
                                yo"Aah!" with vpunch
                                bo"And this is what I get in return?"
                                hide yorucutout_spank0
                                hide yorucutout_spank2
                                hide cutoutborder_white
                                hide yorucutout_waist
                                with dissolve
                                yo"That hurt! You a-asshole!" with vpunch
                                show boruto sceeming with dissolve
                                bo"Then you better watch your tone with me..."
                                
                                
                            "Spare her":
                                bo"I'll let this go this one time but careful, Yoru..."
                                bo"You don't want to get on my bad side!"
                                show yoru angry3 with dissolve
                                yo"*Scoffs*"
                        
                        show boruto sceeming with dissolve
                        bo"As I was saying..."
                        bo"Your... talents. They are wasted in this kitchen."
                        bo"I might have a way out for you..."
                        bo"With which not only would you be getting away from this... You'd also be making more money than you'd know what to do with!"
                        show yoru angry3 with dissolve
                        yo"W-what!? How..." with vpunch
                        bo"You see, a hot piece of ass like you... I reckon that with my help, you'd easily be able to land some lucrative modeling gigs."
                        bo"And I am not talking about the kind of gigs Obo is extorting you for... That's not where the real money is!"
                        bo"Not to mention that unlike him, I'd be spliting the profits with you..."
                        yo"M-modeling gigs? And what would you know about that... you are just a kid."
                        show boruto sceeming2 with dissolve
                        bo"You are in luck Yoru because I happen to know all there is about it..."
                        bot"I am lying out of my fucking teeth but if I can convince her..."
                        bo"I've been studying to be a director for quite some time now and along with my [na_rel]'s connections throughout the lands, I am certain I can kickstart any girl's career in no time!"
                        yo"You can... do that!?"                        
                        show boruto sceeming with dissolve
                        bo"Indeed I can! Just as soon as I gather enough money to open up my own studio, but you see..."
                        bo"I am not just taking any girl that happens to fall upon my lap in a business like this... You'll have to earn my trust first!"
                        show yoru normal with dissolve
                        yo"Sounds nice and all... but talk to me again when you have a concrete plan in mind."
                        hide yoru with dissolve
                        bot"Heh, I think she is hooked on the idea!"
                        show boruto sceeming2 with dissolve
                        bot"Imagine the money I'd be making having a whore like Yoru working for me in that capacity..."
                        show boruto sceeming3 with dissolve
                        bot"I could even convince a few other girls to work for me! I have a few in mind...!"
                        show boruto sceeming with dissolve
                        bot"I'll have to give that some serious thought..."
                        hide boruto with dissolve

                    "(Locked)" if yoruichi_talk_progress_unwillinglyobedient < 2:
                        "Options will become available as you uncover more of the story"
                        jump yoruichiunwillinglyobedienttalkmenu
                    
            "Interactions":
                menu unwillinglyobedientinteractions:
                    "Yoruichi will cater to your 'needs', but if you push her too far she might hold that against you."
                    "Approach her":
                        show boruto sceeming2 behind yoru with dissolve:
                            easein 1 xalign 0.6 zoom 1.00
                        bo"Hey Yoru!"
                        show yoru shy2 with dissolve
                        yo"...[bo_name_stutter]?"
                        menu unwilling_approachmenu:
                            yo"...[bo_name_stutter]?"
                            "Try complimenting her":
                                bo"Don't mind me! I was just admiring your... assets"
                                yo"My a-assets?"
                                menu:
                                    yo"My a-assets?"
                                    "You know what I am talking about!":
                                        bo"Come on... you know what I am talking about!"
                                        show yoru shy with dissolve
                                        label iamseruous_unwilling:
                                        $ yoruichi_approach_progress_unwillinglyobedient = 1
                                        yo"I am just an old and rugged woman..."
                                        bo"A mature and sexy woman, is how I'd put it!"
                                        show yoru obedient with dissolve
                                        yo"..."
                                        bo"I am thinking you could probably make use of that sexy body of yours..."
                                        yo"W-what are you insinuating kid..."
                                        bo"Nothing nefarious... But I am serious when I say you have a gift Yoru. It would be a shame to not use it."
                                        bo"I'll tell you more once I finalize my plan..."
                                        menu:
                                            bo"I'll tell you more once I finalize my plan..."
                                            "Spank her":
                                                show boruto sceeming2 behind yoru:
                                                    easein 1 xalign 0.85 zoom 1.07
                                                show yorucutout_spank0:
                                                    zoom 0.25 xalign 0.1 yalign 0.1
                                                
                                                show cutoutborder_white:
                                                    zoom 0.75 pos (-0.044,-108)
                                                with dissolve
                                                bo"For now, keep helping around the kitchen looking sexy as you do..."
                                                hide yorucutout_spank0
                                                hide cutoutborder_white
                                                with dissolve
                                                show boruto sceeming with dissolve
                                                show cutoutborder_white:
                                                    zoom 0.75 pos (-0.044,-108)
                                                show yorucutout_spank1 at smallshake:
                                                    zoom 0.25 xalign 0.1 yalign 0.1
                                                $ renpy.sound.play("/audio/soun_fx/spank6.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                show yoru at smallshake
                                                bo"That'll be plenty motivation for me!"
                                                show yoru shy with dissolve
                                                show boruto sceeming with dissolve
                                                yo"I-is that all then?"
                                                call increaselust(10) from _call_increaselust_54
                                                if percentage >= 100:
                                                    jump yoruichi_lustscene1
                                                else:
                                                    hide yorucutout_spank0
                                                    hide yorucutout_spank1
                                                    hide yoru_gropeass1_anim1
                                                    hide cutoutborder_white
                                                    hide yorucutout_waist
                                                    show boruto sceeming with dissolve:
                                                        easein 1 xalign 0.5
                                                    bo"For the time being... I'll let you know if anything occurs."
                                                    hide boruto
                                                    hide yoru
                                                    with dissolve
                                            "Don't":
                                                bo"Until then, all you have to do is keep helping around the kitchen looking pretty as you do..."
                                                show yoru shy with dissolve
                                                show boruto sceeming with dissolve
                                                yo"I-is that all then?"
                                                
                                                bo"For the time being... I'll let you know if anything occurs."
                                                hide boruto
                                                hide yoru
                                                with dissolve
                                            
                                    "For an old hag, you have a 'godly' ass":
                                        show boruto sceeming2 with dissolve
                                        bo"Your assets, yes! For an old hag like yourself, you have a 'godly' ass on you."
                                        bo"Heh, get it!? With you being a Shinigami god and all..."
                                        show yoru normal with dissolve
                                        yo"Ugh! Not f-funny, kid..." with vpunch
                                        jump iamseruous_unwilling

                            "Make a ballsy move" if yoruichi_approach_progress_unwillinglyobedient >=1:
                                $ yoruichi_approach_progress_unwillinglyobedient = 2
                                show yoru shy2 with dissolve
                                bo"I still can't believe a woman like you is stuck in a place like this..."
                                yo"W-what do you mean..."
                                bo"You have an unreal body on you..."
                                menu:
                                    bo"You have an unreal body on you..."
                                    "Raise her skirt":
                                        show boruto:
                                            easein 0.5 xalign 0.8
                                        bo"It deserves something more than simple kitchen-work..."
                                        show yoru shy with dissolve
                                        $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                        show yorucutout_raise with dissolve:
                                            zoom 0.46 xalign 0.3 yalign 0.5
                                        
                                        show yoru at smallshake
                                        call increaselust(10) from _call_increaselust_55
                                        if percentage >= 100:
                                            jump yoruichi_lustscene1
                                        bo"I could give that to you... you know!"
                                        hide yorucutout_raise
                                        show boruto:
                                            easein 0.4 xalign 0.6
                                        show yoru angry3 at smallshake
                                        yo"S-stop it kid!" with vpunch
                                        show yoru lookingbackt with dissolve:
                                            zoom 0.5 ypos 1.04
                                        bo"Have it your way..."
                                        hide yoru with dissolve
                                        bot"You'll belong to me soon enough anyway!"
                                        hide boruto with dissolve
                                    
                                    

                            "Grope her" if yoruichi_approach_progress_unwillinglyobedient >=2:
                                $ yoruichi_approach_progress_unwillinglyobedient = 3
                                default yoru_firstexamination = False
                                if yoru_firstexamination == False:
                                    bo"I've been thinking about my plan..."
                                    bo"If I am to help you out with a modelling career..."
                                    bo"I'll need to have a solid idea of how your body could be used to promote a product, right?"
                                    yo"W-what's that supposed to mean..."
                                    show boruto sceeming3 with dissolve:
                                        easein 1 xalign 0.75
                                    bo"It means that I'll have to..."
                                    $ yoru_firstexamination = True
                                else:
                                    bo"My plan is slowly coming along but..."
                                    bo"I'll need some more information about you Yoru..."
                                    show yoru obedient with dissolve
                                    yo"T-this again...?"
                                    show boruto sceeming3 with dissolve:
                                        easein 1 xalign 0.75
                                    bo"It means that I'll have to..."
                                menu:
                                    bo"It means that I'll have to..."
                                    "Examine your tits":
                                        #repeatable
                                        default yoru_examinetits = 1
                                        if yoru_examinetits >= 4:
                                            $ yoru_examinetits = 3 #revert dialogue variable so that the last line is displayed
                                        
                                        hide yoru
                                        hide boruto
                                        $ renpy.sound.play("/audio/soun_fx/grope2.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                                        show yoru_behindstart_border onlayer screens:
                                            zoom 0.5 xalign 0.9 yalign 0.5
                                        show yoru_behindstart1:
                                            zoom 0.5 xalign 0.9 yalign 0.5
                                        with dissolve
                                        $ dialogue = renpy.call("get_dialogue", yoru_examinetits,
                                            f"I'll have to examine your measurements!",
                                            f"I'll have to examine your chest's measurements again!",
                                            f"I'll have to go through another one of our standard procedures!")
                                        with vpunch
                                        $ renpy.say(bo, dialogue)
                                        show yoru_behindstart1 at smallshake
                                        yo"H-hey!"
                                        $ renpy.sound.play("/audio/soun_fx/groperepeat3.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                                        show yoru_behindstart1anim with dissolve:
                                            zoom 0.5 xalign 0.9 yalign 0.5
                                        $ dialogue = renpy.call("get_dialogue", yoru_examinetits,
                                            f"The more I examine you, the better our chances will be to succeed...",
                                            f"I am sure I can put this... information to good use!",
                                            f"Such an amazing pair of tits on you...")
                                        $ renpy.say(bo, dialogue)
                                        show yoru_behindstart1anim at smallshake
                                        $ dialogue = renpy.call("get_dialogue", yoru_examinetits,
                                            f"I've s-seen how you are kid... This is just an e-excuse!",
                                            f"A-another one of y-your excuses!",
                                            f"P-please...")
                                        $ renpy.say(yo, dialogue)
                                        $ dialogue = renpy.call("get_dialogue", yoru_examinetits,
                                            f"Might be, or it might not! Only one way for you to find out and that's to trust me to deliver...",
                                            f"I told you before, didn't I? You'll just have to trust me!",
                                            f"I can't get enough of you!")
                                        $ renpy.say(bo, dialogue)
                                        bo"I can tell you one thing for certain Yoru..."
                                        $ dialogue = renpy.call("get_dialogue", yoru_examinetits,
                                            f"With a rack like this... I can bet you that a whole lot of swimsuit brands would be interested in advertising with you!",
                                            f"A rack like this will make us a fortune if you place your trust in me!",
                                            f"Me and you, we are going to make a fortune working together!")
                                        $ renpy.say(bo, dialogue)
                                        hide yoru_behindstart_border onlayer screens
                                        scene black with vpunch
                                        yo"E-enough of this!"
                                        call increaselust(10) from _call_increaselust_56
                                        if percentage >= 100:
                                            jump yoruichi_lustscene1
                                        show ramenkitchen
                                        show boruto sceeming2 at left
                                        show yoru obedient at right
                                        with dissolve
                                        $ dialogue = renpy.call("get_dialogue", yoru_examinetits,
                                            f"You better h-have a plan {bo_name_stutter}... If you are using me to satisfy your perverted desires I swear I will...",
                                            f"How much longer do I have to endure this for! Is your plan coming along or not?",
                                            f"W-what's going on with your p-plan...")
                                        $ renpy.say(yo, dialogue)
                                        bo"Relax Yoru... All in due time!"
                                        show yoru lookingbackt with dissolve:
                                            zoom 0.5 ypos 1.04
                                        yo"*Scoffs*"
                                        hide yoru with dissolve
                                        bot"I wonder how far I could push her with this modelling premise..."
                                        if yoru_examinetits == 1:
                                            bot"I can't believe she let me casually fondle her tits like that!"
                                        else:
                                            bot"I can't believe she keeps lettin me fondle her tits like that!"  
                                        hide boruto with dissolve
                                        $ yoru_examinetits += 1

                                    "Examine your ass":
                                        #repeatable
                                        default yoru_examineass = 1
                                        if yoru_examineass >= 3:
                                            $ yoru_examineass = 3 #revert dialogue variable so that the last line is displayed
                                        hide yoru
                                        hide boruto
                                        $ renpy.sound.play("/audio/soun_fx/grope2.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                                        show yoru_assgropet_border onlayer screens:
                                            zoom 0.7 xalign 0.9 ypos -0.30
                                        show yoru_assgropet1:
                                            zoom 0.7 xalign 0.9 ypos -0.30
                                        with dissolve
                                        $ dialogue = renpy.call("get_dialogue", yoru_examineass,
                                            f"I'll have to examine your measurements!",
                                            f"I'll have to examine your ass's measurements again!",
                                            f"I'll have to go through another one of our unique procedures!",)
                                        with vpunch
                                        $ renpy.say(bo, dialogue)
                                        show yoru_assgropet1 at smallshake
                                        yo"H-hey!"
                                        $ renpy.sound.play("/audio/soun_fx/groperepeat3.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                                        show yoru_gropeass1_anim2 with dissolve:
                                            zoom 0.7 xalign 0.9 ypos -0.30
                                        $ dialogue = renpy.call("get_dialogue", yoru_examineass,
                                            f"The more I examine you, the better our chances will be to succeed...",
                                            f"I am sure I can put this... information to good use!",
                                            f"Such an amazing ass on you...")
                                        $ renpy.say(bo, dialogue)
                                        show yoru_gropeass1_anim2 at smallshake
                                        $ dialogue = renpy.call("get_dialogue", yoru_examineass,
                                            f"I've s-seen how you are kid... This is just an e-excuse!",
                                            f"A-another one of y-your excuses!",
                                            f"P-please...")
                                        $ renpy.say(yo, dialogue)
                                        $ dialogue = renpy.call("get_dialogue", yoru_examineass,
                                            f"Might be, or it might not! Only one way for you to find out and that's to trust me to deliver...",
                                            f"I told you before, didn't I? You'll just have to trust me!",
                                            f"I can't get enough of your ass!")
                                        $ renpy.say(bo, dialogue)
                                        bo"I can tell you one thing for certain Yoru..."
                                        $ dialogue = renpy.call("get_dialogue", yoru_examineass,
                                            f"With an ass like this... I can bet you that a whole lot of swimsuit brands would be interested in advertising with you!",
                                            f"An ass like this will make us a fortune if you place your trust in me!",
                                            f"Me and you, we are going to make a fortune working together!")
                                        $ renpy.say(bo, dialogue)
                                        hide yoru_assgropet_border onlayer screens
                                        scene black with vpunch
                                        yo"E-enough of this!"
                                        call increaselust(10) from _call_increaselust_57
                                        if percentage >= 100:
                                            jump yoruichi_lustscene1
                                        show ramenkitchen
                                        show boruto sceeming2 at left
                                        show yoru obedient at right
                                        with dissolve
                                        $ dialogue = renpy.call("get_dialogue", yoru_examineass,
                                            f"You better h-have a plan {bo_name_stutter}... If you are using me to satisfy your perverted desires I swear I will...",
                                            f"How much longer do I have to endure this for! Is your plan coming along or not?",
                                            f"W-what's going on with your p-plan...")
                                        $ renpy.say(yo, dialogue)
                                        bo"Relax Yoru... All in due time!"
                                        show yoru lookingbackt with dissolve:
                                            zoom 0.5 ypos 1.04
                                        yo"*Scoffs*"
                                        hide yoru with dissolve
                                        bot"I wonder how far I could push her with this modelling premise..."
                                        if yoru_examineass == 1:
                                            bot"I can't believe she let me casually fondle her ass like that!"
                                        else:
                                            bot"I can't believe she keeps lettin me fondle her ass like that!"  
                                        hide boruto with dissolve
                                        $ yoru_examineass += 1
                                        hide boruto with dissolve
                                    

                            "(Locked)" if yoruichi_approach_progress_unwillinglyobedient <1:
                                "Unlocks after using preceding options"
                                jump unwilling_approachmenu

                            "(Locked)" if yoruichi_approach_progress_unwillinglyobedient <2:
                                "Unlocks after using preceding options"
                                jump unwilling_approachmenu

                        
   

                    "Sexual Favors" if hima_talked_modelling == False:
                        "Advance the story to unlock..."
                        dev"Perhaps trying to convince [him_name] to work with you will be of help..."
                        jump unwillinglyobedientinteractions
                    "{color=[obediencecolor]}Sexual Favors{/color}" if hima_talked_modelling == True:
                        bo"I was thinking..."
                        menu:
                            bo"I was thinking..."

                            "Time for our first photo shoot! ({color=#85bb65}-$50{/color})" if yoruichi_weekdaytalk_modelling == True:
                                bo"Everything's ready for our first photo shoot!"
                                if day_name == "Sunday" or day_name == "Saturday":
                                    $ camerainv = inventory.find_item_by_name("Camera")
                                    if camerainv!= None:
                                        yo"Not everything..."
                                        show yoru obedient with dissolve
                                        yo"The deal was that you pay up-front, remember?"
                                        call checkMoney(50, "yorufirstmodel_fail") from _call_checkMoney_2
                                        hide screen workmenutopright with dissolve
                                        bo"Of course, I am a man of my word after all..."
                                        bo"I believe this is a fair first payment, don't you think?"
                                        show yoru at smallshake
                                        yo"It'll do... Barely!" with vpunch
                                        yo"You still have to deal with Obo..."
                                        bo"Don't worry about that. I know exactly how to handle Obo..."
                                        jump yoru_first_photoshoot

                                        label yorufirstmodel_fail:
                                        show boruto surprised2 with dissolve
                                        bot"Ah, shit..."
                                        show boruto sceeming with dissolve
                                        bo"On second thought... something else came up!"
                                        show yoru lookingbackt at right with dissolve:
                                            zoom 0.5
                                        yo"Stop wasting my time you klutz!"
                                        hide yoru with dissolve
                                        bot"Well, shit! Better have some money ready next time..."
                                        jump ramenkitchenmenu


                                    else:
                                        bo"Wait a second..."
                                        show boruto surprised2 with dissolve
                                        bot"I forgot the fucking camera!"
                                        bo"Uuuuh, nevermind! Something else came up!" with vpunch
                                        show yoru lookingbackt at right with dissolve:
                                            zoom 0.5
                                        yo"Stop wasting my time you klutz!"
                                        hide yoru
                                        show boruto snob
                                        with dissolve
                                        bot"I should check the shop and buy a camera first..."
                                        jump ramenkitchenmenu
                                else:
                                    show yoru lookingbackt at right with dissolve:
                                        zoom 0.5
                                    yo"I told you I can only do that on weekends, you klutz!" with vpunch
                                    hide yoru
                                    show boruto surprised2
                                    with dissolve
                                    bot"Aw shit! I forgot..."
                                    bot"I'll talk to her again on Saturdays or Sundays..."
                                    jump ramenkitchenmenu




                            "My plan for you is ready..." if yoruichi_weekdaytalk_modelling == False:
                                show boruto snob with dissolve
                                bo"My plan for you may be ready to set in motion..."
                                show yoru obedient with dissolve
                                yo"Can I ask what that your 'plan' entails?"
                                bo"You should already know that based on our previous interactions..."
                                bo"I want you to model for me!"
                                show yoru normal with dissolve
                                yo"So is that it then? Your so called 'plan' is to simply follow in Obo's footsteps?"
                                menu:
                                    yo"So is that it then? Your so called 'plan' is to simply follow in Obo's footsteps?"
                                    "Follow his footsteps? Fuck Obo!":
                                        show boruto surprised2 with dissolve
                                        bo"Follow his footsteps? Of course not..."
                                        bo"I've seen how he treats you Yoru... Fuck Obo! He is an abusive piece of shit..." with vpunch
                                        bo"You won't have to worry about that when working with me..."
                                        show yoru disgust2 with dissolve
                                        yo"You say that, but you have been nothing but an annoying sex-pest these past few days..."
                                        show boruto snob with dissolve
                                        bo"I might have my own issues, but I am certainly nowhere near Obo's level..."
                                        show yoru angry with dissolve
                                        bo"Look, I am giving you a chance to take control of your fate, away from an abusive relationship..."
                                        bo"Surely I can't be a worse option than that piece of shit, right?"
                                        bo"Besides, unlike Obo, I fully intend on paying you fairly for your work..."

                                    "{color=[hatredcolor]}I am just 'borrowing' his handbook...{/color}":
                                        show boruto sceeming with dissolve
                                        bo"Follow in his footsteps? No, I am not an abusive piece of shit..."
                                        call changeHatred(1) from _call_changeHatred_134
                                        call borutoevil2 from _call_borutoevil2_19
                                        bot"For now at least!"
                                        bo"I am only borrowing some of his knowledge!"
                                        bo"He already introduced me to some of his peers you know..."
                                        bo"I am planning on using that to help you!"
                                        show yoru disgust2 with dissolve
                                        yo"You say that, but you have been nothing but an annoying sex-pest these past few days..."
                                        show boruto sceeming2 with dissolve
                                        bot"You don't know the half of it you whore!"
                                        bo"I might have my own issues, but I am certainly nowhere near Obo's level..."
                                        show yoru angry with dissolve
                                        bo"Look, I am giving you a chance to take control of your fate, away from an abusive relationship..."
                                        bo"Surely I can't be a worse option than that piece of shit, right?"
                                        bo"Besides, unlike Obo, I fully intend on paying you fairly for your work..."
                                yo"If you are willing to pay me f-fairly, then..."
                                yo"I may consider it..."
                                show boruto snob with dissolve
                                bo"Atta girl!"
                                show yoru normal with dissolve
                                yo"Don't get excited just yet..."
                                show yoru scared with dissolve
                                yo"You should know that Obo only allows me to leave this place during weekends..."
                                yo"That is if I have a good reason to in the first place..."
                                yo"And you'll have to pay me up-front!" with vpunch
                                bo"I'll see what I can do..."
                                bo"Don't worry about Obo, I'll find a way to to circumvent him if he has anything to say about it..."
                                bo"I'll talk to you on the weekend when I am ready then..."
                                default yoruichi_weekdaytalk_modelling = False
                                $ yoruichi_weekdaytalk_modelling = True
                                if quest.exists("bohim_2"):
                                    if quest.is_state("3_bohim_2", "pending"):
                                        $ notification("Quest discovered!")
                                        $ quest.change_quest_title("3_bohim_2",f"Purchase a camera and convince Yoru to help you")
                                        $ quest.check("3_bohim_2", "in progress")
                                $ yoruichiinteractiontaken = True
                                hide yoru with dissolve
                                jump ramenkitchenmenu

                                    
                            "Return":
                                jump unwillinglyobedientinteractions
                            
                        jump unwillinglyobedientinteractions
                    
 
              


                    # "Sexual Acts":
                    #     "WIP"
                    #     jump unwillinglyobedientinteractions
             

                    
                    "Return":
                        jump yoruichiunwillinglyobedientmenu
                    
                        
        $ yoruichiinteractiontaken = True
        hide yoru with dissolve
        jump ramenkitchenmenu



    #Obedient ---------------------------------------------------------------------------
    elif yoruichi_relationship == "Obedient":
        show boruto smirk at left with dissolve
        bo"Hey Yoru!"
        show yoru shy at right with dissolve
        yo"W-what do you need..."
        menu yoruichiobedientmenu:
            "..."
            "Talk with Yoruichi":
                show boruto smirk with dissolve
                bo"Let's talk..."
                show yoru shy2 with dissolve
                yo"A-about what?"
                menu yoruichiobedienttalkmenu:
                    yo"A-about what?"
                    "How's my pretty girl doing?":
                        $ yoruichi_talk_progress_obedient = 1
                        if yoru_1st_photoshoot == False:
                            show boruto smirk with dissolve
                            bo"How's my pretty girl doing?"
                            show yoru obedient with dissolve
                            yo"I am... okay. How's your plan coming along?"
                            show boruto surprised2 with dissolve
                            bo"O-oh yeah, about that..."
                            bo"I am still working on it."
                            show boruto smirk with dissolve
                            bo"I'll tell you all about it as soon as I get the ball rolling!"
                            show yoru shy with dissolve
                            yo"I am putting a lot of trust in you [bo_name]..."
                            show yoru obedient with dissolve
                            yo"Don't let me down..."
                            show boruto smirk2 with dissolve
                            bo"I won't. I told you already, you deserve more than this and I plan on giving you that."
                            show yoru shy with dissolve
                            yo"Nice sounding words, but are they real? Or are you just playing with me..."
                            hide yoru with dissolve
                            show boruto worried with dissolve
                            bot"Truth is, I have no plan at all... I was just trying to give her some hope."
                            show boruto worried2 with dissolve
                            bot"A girl as pretty as her..."
                            bot"Maybe I could look into setting up an advertising or modelling gig for her..."
                            show boruto surprised with dissolve

                            bot"In fact..." with vpunch
                            show boruto snob with dissolve
                            bot"Why don't I do that myself! I could probably look into setting up a small studio at home with the money I am making here..."
                            bot"Could come in handy for [hin_rel]'s financial troubles too..."
                            bot"Imagine the money I'd be making having girls like Yoru or [hin_rel] working for me in that capacity..."
                            show boruto normal with dissolve
                            bot"I'll have to give that some serious thought..."
                            hide boruto with dissolve
                        else:
                            show boruto smirk with dissolve
                            bo"How's my pretty girl doing?"
                            show yoru obedient with dissolve
                            yo"I am. okay, [bo_name]..."
                            yo"But... I think we should be careful about how we act around Obo..."
                            show boruto surprised2 with dissolve
                            bo"Yoru... You shouldn't worry about that."
                            show boruto smirk with dissolve
                            bo"Obo trusts me, remember?"
                            show yoru shy with dissolve
                            yo"You don't know him the way I do..."
                            show yoru obedient with dissolve
                            yo"You should be more careful..."
                            show boruto snob with dissolve
                            bo"Right, well... Obo has a problem with us being... friends? He'll have to deal with me..."
                            show yoru shy3 with dissolve
                            yo"Just... Stay safe, [bo_name]! Don't do anything stupid..."
                            show yoru shy2 with dissolve
                            yo"Let's get back to work"
                            hide yoru with dissolve
                            show boruto worried with dissolve
                            bot"I might have to do something about Obo and the way he treats her..."
                            hide boruto with dissolve

                            
                    
                    "I might have a job opportunity for you..." if yoruichi_talk_progress_obedient >= 1 and yoru_1st_photoshoot == False:
                        $ yoruichi_talk_progress_obedient = 2
                        bo"I might have a job opportunity for you..."
                        show yoru shy3 with dissolve
                        "Yoru's eyes lit up..."
                        show yoru at smallshake
                        yo"...You do?"
                        bo"I've been thinking you know..."
                        bo"A girl as beautiful as you are, your talents are wasted working in a kitchen like this..."
                        yo"..."
                        bo"I bet you could be earning much more money if we found ways to use that beauty of yours..."
                        show yoru shy with dissolve
                        yo"And, how exactly would we do that, kid?"
                        yo"Have you forgotten how your kind treats me based on my appearance alone?"
                        bo"I know but... If my theory is correct, there may be a reasonable explanation for that..."
                        bo"Listen, I am not planning on making you do something you are uncomfortable with, but..."
                        bo"If I can get my hands on the right tools, I am pretty sure we could be making a lot of money together..."
                        bo"The best part is, it would involve just you, and me..."
                        bo"You wouldn't have to put your self out there, not physically at least..."
                        yo"Sounds nice and all, but how do you plan to achieve something like that..."
                        bo"It's called..."
                        bo"Modelling... Under my direction of course!"
                        show yoru shy3 with dissolve
                        yo"I don't even know what that means, kid..."
                        bo"I'll explain more once I have everything ready..."
                        bo"For now, I just need you to trust me on this one, alright?"
                        yo"*Sigh*... It's not like I have a better choice..."


                    "(Locked)" if yoruichi_talk_progress_obedient < 1:
                        "Options will become available as you uncover more of the story"
                        jump yoruichiobedienttalkmenu
                    
    
                    "How was our first session together..." if yoru_1st_photoshoot == True:
                        bo"Just wanted to see how you felt about our first session together..."
                        yo"Oh, that. It was..."
                        show yoru shy3 with dissolve
                        yo"Sort of fun..."
                        show yoru obedient with dissolve
                        yo"I don't often get to be outside without having to worry about my life!"
                        yo"Thank you for trying to help, [bo_name]..."
                        bo"No worries! I am glad you had some fun too!"
                        bo"I'll see if I can find more opportunities for us..."
                        show yoru normal with dissolve
                        yo"Right. Don't forget why I am doing this, kid..."
                        hide yoruc with dissolve
                        yo"And no strange ideas, or requests!"
                        show boruto embarassed with dissolve
                        bo"R-right..."
                        show boruto normal with dissolve

                    
            "Interactions":
                #todo fill this menu
                menu obedientinteractions:
                    "Yoruichi will cater to your 'needs', but if you push her too far she might hold that against you."
                    "Approach her":
                        show boruto smirk behind yoru with dissolve:
                            easein 1 xalign 0.6 zoom 1.00
                        bo"Hey Yoru..."
                        show yoru shy2 with dissolve
                        yo"...[bo_name_stutter]?"
                        menu:
                            yo"...[bo_name_stutter]?"
                            "Compliment her":
                                bo"Every time I walk into this kitchen, I am dazzled by your radiant beauty..."
                                yo"Come on, that's just, cheesy..."
                                menu:
                                    yo"Come on, that's just, cheesy..."
                                    "I am serious...":
                                        bo"I am serious Yoru..."
                                        show yoru shy with dissolve
                                        label iamseruous:
                                        yo"I am just an old and rugged woman..."
                                        bo"A mature and well defined woman, is a better way to put it"
                                        show yoru obedient with dissolve
                                        yo"..."
                                        bo"I am thinking you could probably make use of that beauty of yours..."
                                        yo"W-what are you insinuating kid..."
                                        bo"Nothing nefarious... But I am serious when I say you have a gift Yoru. It would be a shame to not use it."
                                        bo"I'll tell you more once I finalize my plan..."
                                        menu:
                                            bo"I'll tell you more once I finalize my plan..."
                                            "Playfully spank her":
                                                show boruto smirk2 behind yoru:
                                                    easein 1 xalign 0.85 zoom 1.07
                                                show yorucutout_spank0:
                                                    zoom 0.25 xalign 0.1 yalign 0.1
                                                
                                                show cutoutborder_white:
                                                    zoom 0.75 pos (-0.044,-108)
                                                with dissolve
                                                bo"For now, keep helping around the kitchen looking pretty as you do..."
                                                hide yorucutout_spank0
                                                hide cutoutborder_white
                                                with dissolve
                                                show boruto snob with dissolve
                                                show cutoutborder_white:
                                                    zoom 0.75 pos (-0.044,-108)
                                                show yorucutout_spank1 at smallshake:
                                                    zoom 0.25 xalign 0.1 yalign 0.1
                                                $ renpy.sound.play("/audio/soun_fx/spank6.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                show yoru at smallshake
                                                bo"That'll be plenty motivation for me!"
                                                show yoru shy with dissolve
                                                show boruto smirk with dissolve
                                                yo"I-is that all then?"
                                                call increaselust(10) from _call_increaselust_58
                                                if percentage >= 100:
                                                    jump yoruichi_lustscene1
                                                else:
                                                    hide yorucutout_spank0
                                                    hide yorucutout_spank1
                                                    hide yoru_gropeass1_anim1
                                                    hide cutoutborder_white
                                                    hide yorucutout_waist
                                                    show boruto snob with dissolve:
                                                        easein 1 xalign 0.5
                                                    bo"For the time being... I'll let you know if anything occurs."
                                                    hide boruto
                                                    hide yoru
                                                    with dissolve
                                            "Don't":
                                                bo"Until then, all you have to do is keep helping around the kitchen looking pretty as you do..."
                                                show yoru shy with dissolve
                                                show boruto smirk with dissolve
                                                yo"I-is that all then?"
                                                
                                                bo"For the time being... I'll let you know if anything occurs."
                                                hide boruto
                                                hide yoru
                                                with dissolve
                                            
                                    "Might be, but it's also true":
                                        show boruto smirk2 with dissolve
                                        bo"Might be, but it's also the truth. You ARE dazzling Yoru..."
                                        show yoru normal with dissolve
                                        yo"Come on... *Giggles*"
                                        jump iamseruous

                            "Get handsy" if yoru_1st_photoshoot == True:
                                show boruto snob behind yoru with dissolve:
                                        easein 1 xalign 0.77 zoom 1.05
                                bo"I was just thinking about our next modelling shoot..."
                                menu:
                                    bo"I was just thinking about our next modelling shoot..."
                                    "Put your hand on her waist":
                                        show yorucutout_waist:
                                            zoom 0.25 xalign 0.1 yalign 0.1
                                        
                                        show cutoutborder_white:
                                            zoom 0.75 pos (-0.04,-109)
                                        with dissolve
                                        bo"When do you think we can have another session together?"
                                        yo"Whenever you prove to me there's money to be made, [bo_name]..."
                                        yo"I thought we were clear on that..."
                                        hide cutoutborder_white
                                        hide yorucutout_waist
                                        show yoru normal
                                        with dissolve
                                        yo"Talk to me again about it after you figure that out, Okay?"
                                        
                                    "Put your hand on her ass":
                                        show yoru shy at smallshake with dissolve
                                        bo"When do you think we can have another session together?"
                                        show yorucutout_ass:
                                            zoom 0.25 xalign 0.1 yalign 0.1
                                        
                                        show cutoutborder_white:
                                            zoom 0.75 pos (-0.04, -109)
                                        with dissolve                  
                                        yo"[bo_name]...?"
                                        bo"Yeah?"
                                        hide cutoutborder_white
                                        hide yorucutout_ass
                                        show yoru normal
                                        with dissolve
                                        "She pushed your hand away in mild annoyance..." with vpunch
                                        yo"I thought I made it clear to you before!"
                                        yo"There won't be more of it unless you figure out a way to make money out of it!"
                                        yo"And don't think me and you are close like that becuase we had one session together..."
                                        hide yoru with dissolve
                                        yo"Hmph!"
                                        
                                            
                            "???" if yoru_1st_photoshoot == False:
                                "Find a way to get closer with Yoru first..."
                                jump obedientinteractions



                    "Sexual Favors" if hima_talked_modelling == False:
                        "Advance the story to unlock..."
                        dev"Perhaps trying to convince [him_name] to work with you will be of help..."
                        jump obedientinteractions
                    "{color=[obediencecolor]}Sexual Favors{/color}" if hima_talked_modelling == True:
                        
                        bo"I was thinking..."
                        menu sdjkfh29:
                            bo"I was thinking..."

                            "{color=[obediencecolor]}I may need your help with... something!{/color}":
                                if yoruichi_unlock_obedient_interactions == False:
                                    "Find a way to get closer with Yoru during her photo shoot to unlock..."
                                    jump sdjkfh29
                                else:
                                    pass
                                show boruto snob with dissolve
                                show boruto:
                                    easein 1 xalign 0.5
                                bo"I really enjoyed our time together during our last photo shoot..."
                                yo"It was... alright..."
                                bo"You say that but..."
                                show boruto:
                                    easein 1 xalign 0.8
                                bo"I've seen how you were... touching yourself, Yoru!"
                                menu:
                                    bo"I've seen how you were... touching yourself, Yoru!"
                                    "Grope her tits!":
                                        bo"You enjoyed it too, didn't you?"
                                        bo"I could use your help again you know, and you could perhaps use mine!"
                                        yo"You have the wrong idea, [bo_name]. I wasn't... touching myself!"
                                        hide yoru
                                        hide boruto
                                        $ renpy.sound.play("/audio/soun_fx/grope2.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                                        show yoru_behindstart_border onlayer screens:
                                            zoom 0.5 xalign 0.9 yalign 0.5
                                        show yoru_behindstart1:
                                            zoom 0.5 xalign 0.9 yalign 0.5
                                        with dissolve
                                        bo"You enjoyed it too, didn't you?"
                                        with vpunch
                                        show yoru_behindstart1 at smallshake
                                        yo"H-hey!"
                                        $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                                        show yoru_behindstart1anim with dissolve:
                                            zoom 0.5 xalign 0.9 yalign 0.5
                                        bo"Tell me... am I mistaken Yoru?"
                                        show yoru_behindstart1anim at smallshake
                                        yo"Stop it, [bo_name]! Not in here..."
                                        bo"What's wrong with us getting closer..."
                                        bo"We've already been quite intimate with each other, have we not?"
                                        hide yoru_behindstart_border onlayer screens
                                        scene black with vpunch
                                        yo"E-enough of this!"
                                        call increaselust(10) from _call_increaselust_159
                                        if percentage >= 100:
                                            jump yoruichi_lustscene1
                                        show ramenkitchen
                                        show boruto surprised2 at left
                                        show yoru obedient at right
                                        with dissolve
                                        yo"I said... not in here, [bo_name]!" with vpunch
                                        show yoru normal with dissolve
                                        yo"I thought I made the dynamics of our... relationship clear!"
                                        yo"I may help, only if I want to, or if I have to!"
                                        yo"I appreciate your help, but don't get the wrong idea... okay?"
                                        show boruto snob with dissolve
                                        bot"There must be a way to break through her act..."
                                        bot"But all in due time!"
                                        bo"If you say so. Excuse me then..."
                                    "{color=[dominancecolor]}Grope her ass!{/color}":
                                        bo"You enjoyed it too, didn't you?"
                                        bo"I could use your help again you know, and you could perhaps use mine!"
                                        yo"You have the wrong idea, [bo_name]. I wasn't... touching myself!"
                                        show yoru shy with dissolve
                                        $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                        show yorucutout_raise with dissolve:
                                            zoom 0.46 xalign 0.3 yalign 0.5
                                        yo"H-hey!"
                                        
                                        $ renpy.sound.play("/audio/soun_fx/groperepeat1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                        show yoru_gropeass1_anim1:
                                                zoom 0.25 xalign 0.1 yalign 0.1
                                            
                                        show cutoutborder_white:
                                            zoom 0.75 pos (-0.04, -109)
                                        hide yorucutout_raise
                                        with dissolve
                                        call changeDominance(1,"yoruassgropeafterphotoshoot") from _call_changeDominance_79
                                        bo"Tell me... am I mistaken Yoru?"
                                        yo"{size=*0.8}*Whispers* Y-you are! More importantly, what if Obo sees us like this!{/size}" with vpunch
                                        show yoru at smallshake
                                        call increaselust(10) from _call_increaselust_160
                                        if percentage >= 100:
                                            jump yoruichi_lustscene1
                                        bo"Obo is the least of my concerns..."
                                        bo"All I can think about is you, and that evening we spent together..."
                                        hide yorucutout_raise
                                        hide yoru_gropeass1_anim1
                                        hide cutoutborder_white
                                        show boruto surprised2:
                                            easein 0.4 xalign 0.6
                                        show yoru angry3 at smallshake
                                        yo"Okay, that's enough! S-stop it kid!" with vpunch
                                        yo"I thought I made the dynamics of our... relationship clear!"
                                        yo"I may help, only if I want to, or if I have to!"
                                        show yoru shy3 with dissolve
                                        yo"I appreciate your help, but don't get the wrong idea... okay?"
                                        show boruto snob with dissolve
                                        bot"There must be a way to break through her act..."
                                        bo"If you say so..."
                                        show yoru lookingbackt with dissolve:
                                            zoom 0.5 ypos 1.04
                                        yo"..."
                                        hide yoru with dissolve
                                        bot"But all in due time!"
                                        hide boruto with dissolve
                                 
                                    



                            "It's time for our photo shoot! ({color=#85bb65}-$0{/color})" if yoruichi_weekdaytalk_modelling == True:
                                if yoru_1st_photoshoot == True:
                                    dev"This will repeat the events of the first photoshoot, but there's still plenty of hidden options and for you to discover in this event!"
                                    dev"Yoru's storyline will continue in future updates!"
                                bo"Everything's ready for our photo shoot!"
                                if day_name == "Sunday" or day_name == "Saturday":
                                    $ camerainv = inventory.find_item_by_name("Camera")
                                    if camerainv!= None:
                                        hide screen workmenutopright with dissolve
                                        yo"Not everything..."
                                        show yoru obedient with dissolve
                                        # yo"The deal was that you pay up-front, remember?"
                                        # call checkMoney(50, "yorufirstmodel_fail_love")
                                        # hide screen workmenutopright with dissolve
                                        # bo"Of course, I am a man of my word after all..."
                                        # bo"I believe this is a fair first payment, don't you think?"
                                        # show yoru at smallshake
                                        # yo"It'll do... Barely!" with vpunch
                                        yo"We still have to deal with Obo..."
                                        bo"Don't worry about that. I know exactly how to handle Obo..."
                                        bo"Come..."
                                        jump yoru_first_photoshoot_love

                                        label yorufirstmodel_fail_love:
                                        show boruto surprised2 with dissolve
                                        bot"Ah, shit..."
                                        show boruto sceeming with dissolve
                                        bo"On second thought... something else came up!"
                                        show yoru lookingbackt at right with dissolve:
                                            zoom 0.5
                                        yo"Stop wasting my time you klutz!"
                                        hide yoru with dissolve
                                        bot"Well, shit! Better have some money ready next time..."
                                        jump ramenkitchenmenu


                                    else:
                                        bo"Wait a second..."
                                        show boruto surprised2 with dissolve
                                        bot"I forgot the fucking camera!"
                                        bo"Uuuuh, nevermind! Something else came up!" with vpunch
                                        show yoru lookingbackt at right with dissolve:
                                            zoom 0.5
                                        yo"Stop wasting my time you klutz!"
                                        hide yoru
                                        show boruto snob
                                        with dissolve
                                        bot"I should check the shop and buy a camera first..."
                                        jump ramenkitchenmenu
                                else:
                                    show yoru lookingbackt at right with dissolve:
                                        zoom 0.5
                                    yo"I told you I can only do that on weekends, you klutz!" with vpunch
                                    hide yoru
                                    show boruto surprised2
                                    with dissolve
                                    bot"Aw shit! I forgot..."
                                    bot"I'll talk to her again on Saturdays or Sundays..."
                                    jump ramenkitchenmenu




                            "My plan for you is ready..." if yoruichi_weekdaytalk_modelling == False:
                                show boruto normal with dissolve
                                bo"My plan for you may be ready to set in motion..."
                                show yoru obedient with dissolve
                                yo"Can I ask what that your 'plan' entails?"
                                bo"You remember the job opportunity I talked to you about, don't you?"
                                show yoru shy3 with dissolve
                                yo"So you want me to... model for you?"
                                show boruto snob with dissolve
                                bo"That is exactly what I want you to do!"
                                yo"I hope this wasn't another one of Obo's ideas rubbing off on you..."
                                menu:
                                    yo"I hope this wasn't another one of Obo's ideas rubbing off on you..."
                                    "Obo's ideas? Fuck Obo!":
                                        show boruto surprised2 with dissolve
                                        bo"Yoru, I am nothing like Obo..."
                                        bo"I've seen how he treats you Yoru... Fuck Obo! He is an abusive piece of shit..." with vpunch
                                        bo"You won't have to worry about that when working with me..."
                                        show yoru obedient with dissolve
                                        yo"You say that, but..."
                                        yo"You will excuse me my concerns after seeing how your kind acts..."
                                        show boruto snob with dissolve
                                        bo"I might have my own issues, but I am certainly nowhere near Obo's level..."
                                        show yoru shy3 with dissolve
                                        bo"Allow me this chance to help you regain control of your own fate, away from an abusive relationship..."
                                        bo"Surely I can't be a worse option than that piece of shit, right?"
                                        bo"Besides, unlike Obo, I fully intend on paying you fairly for your work..."

                                    "{color=[dominancecolor]}I am just using Obo to get what I want...{/color}":
                                        show boruto snob with dissolve
                                        bo"Obo, huh...?"
                                        bo"You see... Obo is just another pawn I am using to get what I really want..."
                                        show yoru shy with dissolve
                                        yo"And what is it that you want, [bo_name]..."
                                        
                                        bo"Isn't it obvious?"
                                        call changeDominance(1) from _call_changeDominance_80
                                        bo"I want money, notoriety, and you along my side..."
                                        bo"I want Obo out of the picture, and you at the center of it!"
                                        show yoru shy3 with dissolve
                                        yo"That's..."
                                        yo"Wishful thinking, not to mention cheesy!"
                                        show yoru shy with dissolve
                                        yo"But I appreciate the thought, [bo_name]..."
                                        show boruto normal with dissolve
                                        bo"But seriously..."
                                        bo"He already introduced me to some of his peers you know..."
                                        bo"I am planning on using that to help you!"
                                        bo"Besides, unlike Obo, I fully intend on paying you fairly for your work..."
                                yo"If you are willing to pay me f-fairly, then..."
                                yo"I may consider it..."
                                show boruto snob with dissolve
                                bo"Atta girl!"
                                show yoru normal with dissolve
                                yo"Don't get excited just yet..."
                                show yoru scared with dissolve
                                yo"You should know that Obo only allows me to leave this place during weekends..."
                                yo"That is if I have a good reason to in the first place..."
                                bo"Don't worry about Obo, I'll find a way to to circumvent him if he has anything to say about it..."
                                bo"I'll talk to you on the weekend when I am ready then..."
                                $ yoruichi_weekdaytalk_modelling = True
                                if quest.exists("bohim_2"):
                                    if quest.is_state("3_bohim_2", "pending"):
                                        $ notification("Quest discovered!")
                                        $ quest.change_quest_title("3_bohim_2",f"Purchase a camera and convince Yoru to help you")
                                        $ quest.check("3_bohim_2", "in progress")
                                $ yoruichiinteractiontaken = True
                                hide yoru with dissolve
                                jump ramenkitchenmenu

                                    
                            "Return":
                                jump obedientinteractions
                            
                        # jump obedientinteractions
             

                    
                    "Return":
                        jump yoruichiobedientmenu
                    
                        
    $ yoruichiinteractiontaken = True
    hide yoru with dissolve
    jump ramenkitchenmenu


