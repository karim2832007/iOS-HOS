label hinatabedroomtraining:
    show boruto snob with dissolve
    bo"Mind If I joined in on your training?"
    if hinata_respect < 0:
        show shina concerned
        call checkRespect(0,"Hinata",None) from _call_checkRespect_5
        hin"I don't think that's a good idea right now..."
        bo"What... why?"
        hin"I just don't think it's the right time, okay?"
        hin"Maybe after your condition gets... better?"
        menu:
            hin"Maybe after your condition gets... better?"
            "I am trying...":
                show boruto worried with dissolve
                bo"I am trying [hin_rel]..."
                call changeRespect("Hinata",1) from _call_changeRespect_183
                hin"I know, I know..."
                show shina shy2 with dissolve
                hin"It'll get easier as time goes by, okay?"
                bo"I am not so sure about that..."
                hide boruto with dissolve
                bo"Anyway, I'll leave you to it then..."
                show shina concerned with dissolve
                hint"Poor boy... Am I being too harsh with him?"
                show shina serious with dissolve
                hint"As much as I hate seeing him like this, a line needs to be drawn somewhere!"
                hide shina with dissolve
                jump action_taken
            "{color=[obediencecolor]}Fine! I guess I'll just watch you then...{/color}":
                show boruto angry with dissolve
                bo"Fine! I'll just watch you then..." with vpunch
                show shina surprised with dissolve
                show shina at smallshake
                hin"W-watch me!? W-why would you want to watch me exercise..."
                show boruto snob with dissolve
                bot"You damn well know why [hin_rel]!"
                bo"Maybe I can give you a pointer or two... or s-something!"
                show shina concerned with dissolve
                hin"While I appreciate your desire to help, maybe there are complications to consider given your..."
                bo"What are you talking about [hin_rel]... You always exercise in the living room anyway. I've been watching you since forever!" with vpunch
                show shina at smallshake
                hin"*Sigh...* It's not like I could stop you even if I wanted... It's just a bit, weird! Don't you think so too?"
                bo"It's not weird at all..."
                hin"..."
                bo"..."
                show shina serious with dissolve
                hin"Don't just s-stand there staring at me! I still have to get changed!" with vpunch
                scene black with vpunch
                bo"R-right..."
                jump hinatawatchnormal
                
            "{color=[hatredcolor]}It could get better if we 'trained' together!{/color}" if hatred >=25:
                show boruto sceeming with dissolve
                bo"It could get better if we trained together, you know..." with vpunch
                show shina surprised with dissolve
                show shina at smallshake
                hin"T-thats... What is that even supposed to mean, [bo_name_stutter]!"
                bot"You damn well know what it means [hin_rel]!"
                show shina concerned with dissolve
                hin"Listen, we can't train together right now, okay? You are going to have to accept that..."
                show boruto sceeming2 with dissolve
                bo"Fine... I guess I'll have to find ways to deal with my condition then, huh?"
                show boruto:
                    easein 2 xpos -1000
                hin"..."
                hint"Was he implying something there...?"
                scene black with dissolve
                jump hinatawatchhate
            
    call checkRespect(0,"Hinata",None) from _call_checkRespect_6
    show shina surprised with dissolve
    if strength == 1 and strengthlevel>=20:
        show shina shy2 with dissolve
        hin"You want us to train together?" with vpunch
        bo"I've gotten pretty strong you know! Been taking my own training seriously lately!"
        show shina shy with dissolve
        hin"I noticed that much..."
        hin"Maybe this can be a nice opportunity to spend some time together..."
        hin"Give me a second to get dressed first, okay?"
        bo"S-sure!" with vpunch
    elif strength == 2:
        hin"This again, huh?" with vpunch
        bo"I am pretty sure I could teach you a thing or two at this point..."
        show shina smiling with dissolve
        hin"Don't get ahead of yourself now [bo_name]..."
        bo"Wanna put that to the test then?"
        show shina shy2 with dissolve
        hin"Give me a second to prepare myself first, okay?"
        bo"Alright!"
    elif strength >=3:
        hin"*Sigh*... Do you ever tire [bo_name]?" with vpunch
        bo"Not when I am with you!"
        show shina shy with dissolve
        hin"..."
        hin"Let me get ready first..."
        bo"Sure thing..."
    elif strengthtutorial == True:
        hin"You want us... to train together?"
        bo"Why not!"
        show shina concerned with dissolve
        hin"I don't know..."
        hint"Will his condition be a... problem?"
        hin"Uhm..."
        bo"Come on, it'll be fun!" with vpunch
        show shina shy2 with dissolve
        hin"I'll tell you what... If you can prove yourself to me, I'll consider it... okay?"
        bo"Prove myself how exactly..."
        hin"Let me get ready first and I'll let you know, alright?"
        show boruto normal with dissolve
        bo"Sure thing..."
    else:
        hin"[bo_name]... It's been years since you last trained yourself!"
        show boruto embarassed with dissolve
        bo"Uuuh, Heh-eh!"
        hin"Maybe I'd consider that if you took your own training a little bit more seriously..."
        hide shina with dissolve
        show boruto normal with dissolve
        bot"Maybe she'd be more open to the idea if I started working out a little bit..."
        scene black with dissolve
        "You can train in your bedroom to unlock different opportunities!"
        jump action_taken

        

    $ renpy.sound.play("/audio/soun_fx/doorclose.opus", channel="sfx3", loop=False, relative_volume = 1.0)
    scene black with dissolve
    "[hin_name] gets dressed for the occasion..."
    show hinata_bedroomtraining_active with dissolve:
        zoom 1.2 xalign 0.0 yalign 1.0 alpha 0.0
    show hinata_bedroomtraining_active:
        easein 3 alpha 1.0 yalign 0.0
    hin"Alright! You ready for this...?"
    bo"Let's get to it!"
    if radiostation == 1:
        $ playmusic("audio/ost/reversesituation.opus",0.6)
    elif radiostation == 2:    
        $ playmusic("audio/ost/lightningspeed.opus",0.7)
    elif radiostation == 3:
        $ playmusic("audio/ost/gym_Junkyousha.opus",0.8)
    elif radiostation == 4:
        $ playmusic("audio/ost/nightattack.opus",0.7)
    elif radiostation == 5:
        $ playmusic("audio/ost/kokuten.opus",0.6)
    elif radiostation == 6: 
        $ playmusic("audio/ost/borutotheme.opus",0.5)
    default hinata_training_unlocked = False
    if hinata_training_unlocked == False:
        scene hinata_bedroomtraining_active with dissolve
        hin"Not so fast, young man..." with vpunch
        hin"If you want us to to train together, you'll have to prove yourself to me!"
        bo"And how would I go about doing that, [hin_rel]?"
        hin"A physical test of course!" with vpunch
        bo"A test, huh? I am down!"
        show hinata_bedroomtraining_idle with dissolve
        hin"Since you are a man, and I am a woman a test of strength would be unfair! So..."
        show hinata_squatdown with dissolve
        hin"I propose a test of... endurance!" with vpunch
        show hinata_squatup with dissolve
        pause 0.2
        scene hinata_bedroomtraining_active with dissolve
        bo"Squats, huh? Now that would be unfair to me, don't you think so? You've been working on your glutes for twenty years now!"
        bot"No wonder [hin_rel]'s ass is so... firm!"
        hin"*Giggles* I didn't say the test would be easy..."
        show hinata_bedroomtraining_idle with dissolve
        hin"Out-squat me before the timer hits zero, and I'll allow you to train with me! Deal...?"
        menu hinatabedroom_training_menu:
            "..."
            "This will be a piece of cake!":
                bo"This will be a piece of cake!"
                scene hinata_bedroomtraining_active with dissolve
                hin"You wish!"
                if hinata_training_unlocked == True:
                    menu:
                        hin"You wish!"
                        "{color=[obediencecolor]}Move behind her...{/color}":
                            bo"You wouldn't mind if I..."
                            show hinata_squatbehindup with dissolve
                            bo"...moved back here, right?"
                            show hinata_squat_behindface with dissolve:
                                yalign 0.6
                            show hinata_squat_behindface:
                                easein 3 yalign 0.0
                            hin"A-any particular reason...?"
                            bo"Observing..."
                            scene hinata_squatbehindup with dissolve
                            hin"O-observing what e-exactly..."
                            bo"Your form of course! What else would I be observing..."
                            call changeObedience("Hinata",1) from _call_changeObedience_109
                            hin"O-oh..."
                            default hinata_squat_minigame_frombehind = False
                            $ hinata_squat_minigame_frombehind = True
                            hin"O-okay then! Ready, and..."
                            jump start_strength_minigame_hinata


                        "Stay in front...":
                            scene hinata_squatup with dissolve
                            hin"Ready, and..."
                            jump start_strength_minigame_hinata
                        
                else:
                    scene hinata_squatup with dissolve
                    hin"Ready, and..."
                    jump start_strength_minigame_hinata
                
            "Change Radio":
                menu:
                    bot"What should I put on..."
                    "[na_rel]'s favorite":
                    #reversesituaiton
                        $ radiostation = 1                 
                        $ playmusic("audio/ost/reversesituation.opus",0.75)
                        $ change_music_volume(0.8, 1.0)
                        bo"[na_rel]'s favorite... Not my style, but it will have to do!"
                    "[na_rel]'s CD":
                        #lightnign
                        $ radiostation = 2        
                        $ playmusic("audio/ost/lightningspeed.opus",0.85)
                        $ change_music_volume(0.8, 1.0)
                        bo"[na_rel] let me have this a while ago. Said he is way past those days..."
                    "Mysterious CD":
                        $ radiostation = 3 
                        $ playmusic("audio/ost/gym_Junkyousha.opus",0.99)
                        $ change_music_volume(0.8, 1.0)
                        bo"I don't even know where this one came from, but it bangs!"
                    "Root CD":
                        $ radiostation = 4 
                        $ playmusic("audio/ost/nightattack.opus",0.85)
                        $ change_music_volume(0.8, 1.0)
                        bo"[na_rel] said he doesn't even remember where he got this from. Sounds like old men's music, but it gets me going!"
                    "Mentor's CD":
                        $ radiostation = 5 
                        $ playmusic("audio/ost/kokuten.opus",0.75)
                        $ change_music_volume(0.8, 1.0)
                        bo"My mentor's CD. Much better than what [na_rel] listens to!"
                    "[bo_name]'s CD":
                        $ radiostation = 6
                        $ playmusic("audio/ost/borutotheme.opus",0.6)
                        $ change_music_volume(0.5, 1.0)
                        bo"The new shit! This is my jam!"
                jump hinatabedroom_training_menu

            "Information":
                $ selected_level = strength
                show screen gymmenu
                jump hinatabedroom_training_menu

       
    else:
        scene hinata_bedroomtraining_active with dissolve
        hin"I know you beat me once before, but I am not one to give up that easily!"
        hin"You'll have to beat me again before we proceed with training!"
        jump hinatabedroom_training_menu
        # hin"So... what did you have in mind when you said we should train together?"
        # jump hinata_stretching_wonmenu
        

        
    

        
    




label start_strength_minigame_hinata:
    $ renpy.sound.play("/audio/soun_fx/countdown.opus", channel="sfx2", loop=False, relative_volume = 0.9)
    if hinata_squat_minigame_frombehind == True:
        show hinata_squatbehindup
        show halfblack
        with dissolve
        show screen scrollingtext("Get ready to tap as fast as you can!")
        hide halfblack with Dissolve(3)
        $ pushups, ended_by_stamina, wonsquats = renpy.call_screen("strength_minigame_hinata", "hinata_squats_behind")
    else:
        show hinata_squatup
        show halfblack
        with dissolve
        show screen scrollingtext("Get ready to tap as fast as you can!")
        hide halfblack with Dissolve(3)
        $ pushups, ended_by_stamina, wonsquats = renpy.call_screen("strength_minigame_hinata")

    
    if ended_by_stamina:
        show hinata_squatdown_var with dissolve:
            yalign 1.0
        show hinata_squatdown_var:
            easein 3 yalign 0.1
        "You got exhausted after completing [pushups] squats!"
        bo"How are you... *Tired breathing*"
        hin"Aww, something wrong?"
        show hinata_squatdown with dissolve
        hin"Thought you said this would be a piece of cake!"
        show hinata_squatup with dissolve
        hin"I can keep going on forever!"
        show hinata_squat_win with dissolve:
            yalign 1.0
        show hinata_squat_win:
            easein 3 yalign 0.1
        bo"*Between breaths* I'll... get you for sure... next time!"
        hin"*Giggles* Sure you will! Here, need some help?"
        bo"I b-better get back to training I suppose..."
        scene black with dissolve
        call changeStrength(pushups/2) from _call_changeStrength_2
        bot"At least I feel like I've gotten stronger from this..."
        bot"And I got to see [hin_rel] squatting in her tight sportswear up close!"
        jump action_taken
    elif wonsquats:
        if hinata_squat_minigame_frombehind == True:
            show hinata_squatbehind_lose with dissolve:
                yalign 1.0
            show hinata_squatbehind_lose:
                easein 3 yalign 0.1
        else:
            show hinata_squat_lose with dissolve:
                yalign 1.0
            show hinata_squat_lose:
                easein 3 yalign 0.1
        hin"*Panting*"
        "You completed [pushups] squats and won the challenge!"
        if hinata_squat_minigame_frombehind == True:
            bot"*Panting* That ass is enough motivation to last me a lifetime of squats..."
            call increaselust(10) from _call_increaselust_161
        else:
            show screen parallax1280("hinata_squat_lose") with dissolve
            call showscrollingimage from _call_showscrollingimage_87
        scene black
        if hinata_training_unlocked == True:
            hin"*Panting* I can't believe I lost again..."
            bo"Heh! Easy..."
        else:
            hin"H-how... *Panting* Since when are you..."
            bo"Hehe! What's wrong [hin_rel], you are looking tired!"
            hin"I am e-exhausted! I gave it my all..."
            bo"You underestimated me... I told you I was getting stronger, didn't I?"
        $ hinata_training_unlocked = True
        if hinata_training_unlocked == False:
            call hidescrollingimage from _call_hidescrollingimage_82
            hide screen parallax1280
            with dissolve
        hide hinata_squat_lose
        hide screen parallax1280
        hide screen camera1280
        hide screen camera_ui
        hide scrollingimage onlayer screens
        with dissolve
        jump hinata_stretching_won

 
    else:
        show hinata_squat_win with dissolve:
            yalign 1.0
        show hinata_squat_win:
            easein 3 yalign 0.1
        hin"Phew! That was... *Panting* close!"
        bo"*Panting* I'll... get you for sure next time!"
        hin"*Giggles* Sure you will! Here, need some help?"
        scene black with dissolve
        bo"T-thanks... I b-better get back to training I suppose..."
        call changeStrength(pushups/2) from _call_changeStrength_3
        bot"At least I feel like I've gotten stronger from this!"
        bot"And I got to see [hin_rel] squatting in her tight sportswear up close!"
        jump action_taken

        



label hinata_stretching_won:
    scene black with dissolve
    "You both take a breather..."
    call changeStrength(pushups/2) from _call_changeStrength_4
    if hinata_training_unlocked == True:
        bot"I feel stronger!"
        hin"Aaarh! How do you keep besting me so easily!?" with vpunch
        show watch4 with dissolve:
            zoom 1.2 xalign 0.5 yalign 0.0
        show watch4:
            easein 7 zoom 1.0 xalign 0.5 yalign 0.5
        hin"There must be some secret to your training, right?"
        hin"*Sigh...* My legs are burning more than ever after that. Gotta give them a good stretch!" with vpunch
        call increaselust(10) from _call_increaselust_162
        bot"[hin_rel] is so damn hot..." with vpunch
        hin"You still haven't told me how you got so strong, so fast..."
    else:
        bot"I feel stronger... More importantly, does that mean [hin_rel] will now-"
        hin"Aaaah... I can't believe I lost!" with vpunch
        show watch4 with dissolve:
            zoom 1.2 xalign 0.5 yalign 0.0
        show watch4:
            easein 7 zoom 1.0 xalign 0.5 yalign 0.5
        hin"My legs are burning after that... Gotta give them a good stretch!" with vpunch
        call increaselust(10) from _call_increaselust_163
        bot"D-damn... [hin_rel] is so freaking a-athletic... and hot!" with vpunch
        hin"When... How did you even get that strong, this fast, [bo_name]?"
        bot"My condition might have had something to do with it but..."
        bo"Eheh... Hard work, training knowledge, and secrets that I may or may not be willing to pass on!"
        hin"Then you are going to have to pass on those so called 'secrets' of yours to me and your [him_rel]!"
        hin"So... what did you have in mind when you said we should train together?"
    menu hinata_stretching_wonmenu:
        hin"So... what did you have in mind when you said we should train together?"

        "I think I'll just watch you exercise instead..." if hinata_training_unlocked == True:
            bo"I think I'll just watch you exercise instead..." with vpunch
            hin"You want to... w-watch me exercise? Y-you sure you don't want to join me instead?"
            bo"I am quite spent myself! Maybe I can give you a pointer or two if I just... observed?"
            hin"Hmm... It's a bit weird having you just watching, but I suppose that's what trainers do! Don't they?"
            bo"Exactly..." with vpunch
            hin"I'll be wrapping up with my typical yoga stretching at my usual spot..."
            scene black with dissolve            
            bo"Right..."
            jump hinatawatchnormal

        "{color=[obediencecolor]}I could help you with your squat form!{/color}":
            default hinata_squat_1sttime = False
            jump hinata_squat_label

        "{color=[obediencecolor]}I could help you with some stretching tips...{/color}" if hinata_squat_1sttime == True:
            default hinata_stretch_1sttime = False

            jump hinata_stretch_label

        # "I could show you some advanced stretching exercices! (WIP)" if hinata_stretch_1sttime == True:
        #     default hinata_advancedstretch_1sttime = False
        #     dev"Not yet available"
        #     jump hinata_stretching_wonmenu


        "{color=[obediencecolor]}????{/color}" if hinata_squat_1sttime == False:
            "Complete previous options to unlock..."
            jump hinata_stretching_wonmenu

        # "{color=[obediencecolor]}????{/color}" if hinata_stretch_1sttime == False:
        #     "Complete previous options to unlock..."
        #     jump hinata_stretching_wonmenu



label hinata_squat_label:
    $ initialize_replay_defaults()
    bo"I could probably give you a tip or two when it comes to your squat form!"
    scene watch4 with dissolve:
        zoom 1.2 xalign 0.5 yalign 0.0
    hin"Hmmm...? You think there's something wrong with my form?"
    scene watch4 with dissolve
    bo"I think there's room for improvement!"
    scene black with dissolve
    hin"If you say so..."
    show hinata_bedroomtraining_idle with dissolve
    hin"You are the expert here!"
    show hinata_squatup with dissolve
    pause 0.2
    show hinata_squatdown with dissolve
    hin"You might even share some of your secrets with me, won't you?"
    hin"You see something wrong with my squat?"
    bo"Not great, not terrible!"
    show hinata_bedroomtraining_active with dissolve
    hin"Huh... Interesting! I was pretty sure I had the form nailed..."
    bo"There's a reason you lost, [hin_rel]! But I am gonna have to take another look before I confirm my suspicions..."
    scene hinata_bedroomtraining_idle with dissolve
    hin"Another look? Don't have to rub it in, you dummy..."
    scene black with dissolve
    "You circle around [hin_name] to take another look at her form, but this time..."
    show hinata_squat_behindface with dissolve:
        yalign 0.5
    show hinata_squat_behindface:
        easein 1 yalign 0.0
    hin"What are you looking for back there..."
    show hinata_squat_behindface:
        easein 3 yalign 0.7
    bo"Thought I told you I am going to need another look at your form..."
    hin"Y-you are a bit too close, aren't you?"
    show hinata_squatbehindup
    show borutosquatbehind:
        zoom 1.38 pos (0.39, -682)
    show borutosquatbehind:
        easein 2 alpha 0.3
    with dissolve
    bo"How else am I going to check up on your form [hin_rel]! Come on, it's not a big deal..."
    bo"Let's see it! You know what they say, ass to grass!"
    scene hinata_squat_behindface with dissolve:
        zoom 1.2 yalign 0.0
    hin"O-okay then... Don't have to be vulgar you know!"
    scene hinata_squatbehindup with dissolve
    show borutosquatbehind:
        zoom 1.38 pos (0.39, -682)
    show borutosquatbehind:
        easein 2 alpha 0.1
    with dissolve
    bo"It's just a figure of speech [hin_rel]... Come on then, ass to grass!"
    hin"*Sigh* H-here goes..."
    scene hinata_squatbehinddown_var with dissolve
    pause 0.4
    show hinata_squatbehinddown with dissolve
    call increaselust(10) from _call_increaselust_164
    bot"Such a perfect ass..."
    bo"Aaand up!"
    show hinata_squatbehindup with dissolve
    hin"Ha... ah!" with vpunch
    hin"*Exhales sharply* Phew..."
    hin"S-so...?"
    bot"That was practically perfect, but..."
    menu hinata_squathelp:
        bot"That was practically perfect, but..."

        "{color=[dominancecolor]}????{/color}" if hinata_squatcounter < 3 and dominanceanotherone == False:
            "Perhaps if [hin_name] was exhausted..."
            jump hinata_squathelp

        "{color=[dominancecolor]}Another one!{/color}" if hinata_squatcounter > 3 and dominanceanotherone == False:
            default dominanceanotherone = False
            $ dominanceanotherone = True
            bo"Another one, [hin_rel]!" with vpunch
            hin"[bo_name_stutter]! That's enough of your g-games..." with vpunch
            call checkDominance(20,"hinatasquatmad") from _call_checkDominance_23
            bo"Games? Answer me this [hin_rel]; When do you think form is most important..."
            hin"W-what does that have to do with you asking me to squat over and over again..."
            bo"It has everything to do with that! Form breaks when one gets tired [hin_rel]..."
            bo"And that's when it starts being pivotal to maintain it!"
            bo"Did you think I was just playing games?"
            call changeDominance(1) from _call_changeDominance_81
            hin"O-oh... I didn't realize you were thinking ahead!"
            hin"You could just s-say so in the first place you know..."
            bo"I won't hear any more complaints!" with vpunch
            bo"Now drop down and give me another one!"
            call changeObedience("Hinata",1) from _call_changeObedience_110
            hin"S-sheesh! Didn't now you are one of those hard-ass trainer types..."
            scene hinata_squatbehinddown_var with dissolve
            pause 0.4
            show hinata_squatbehinddown with dissolve
            pause 0.4
            show hinata_squatbehindup with dissolve
            hin"...M-more?"
            menu dominancesquatmenu:
                hin"...M-more?"
                "Ass to grass!":
                    bo"Ass to grass!" with vpunch
                    scene hinata_squatbehinddown_var with dissolve
                    pause 0.4
                    show hinata_squatbehinddown with dissolve
                    pause 0.4
                    show hinata_squatbehindup with dissolve
                    hin"I am... *Heavy breathing*... getting tired!"
                    bot"I'll never tire of watching that ass!"
                    jump dominancesquatmenu
                "Keep going until your form breaks!":
                    bo"Now keep going until your form breaks! Chop chop..."
                    show hinata_squats_behind1 with dissolve
                    hin"H-here goes nothing..."
                    hin"One..."
                    hin"Two!"
                    bot"[hin_rel]'s quick to follow my word if she thinks I know what I am doing..."
                    call increaselust(10) from _call_increaselust_165
                    show hinata_squats_behind2 with dissolve
                    hin"...Ah! *Heavy breathing*..."
                    hin"...T-twenty! Ah..."
                    bot"I wonder what else she'd let me show her if I can find ways to make her believe I know stuff!"
                    hin"Ah... *Panting* eh..!" with vpunch
                    show hinata_squats_behind3 with dissolve
                    hin"...Ah! F-forty..." with vpunch
                    hin"...Eh... *Heavy breathing* Ah!"
                    bot"Even when exhausted, her form is immaculate..."
                    hin"Ah!... F...F-fifty! e-eh... [bo_name_stutter]...?"
                    scene black with vpunch
                    "[hin_name] utterly exhausted, fell on her training mat to catch a breather..."
                    show hinata_exhausted with dissolve:
                        yalign 1.0 xalign 0.5
                    show hinata_exhausted with dissolve:
                        easein 5 yalign 0.1
                    hin"*Exhausted Panting*..."
                    hin"I... *Heavy breathing* I don't think I can... go on any longer!"
                    hin"Let's c-call it... a d-day! *Panting*"
                    menu:
                        hin"Let's c-call it... a d-day! *Panting*"
                        "You could use some stretching!":
                            bo"It seems your body quickly tensed up [hin_rel]..."
                            bo"You could really use some stretching..."
                            bo"Perhaps I could share a few of my secret with you!"
                            jump youcouldusesomestretching
                        "What about your form...":
                            bo"W-what about your form..."
                            hin"I wouldn't even be able to process... *Heavy breathing* your feedback..."
                            hin"Maybe... n-next time?"
                            show screen parallax1280("hinata_exhausted",1.5,0.5) with dissolve
                            call showscrollingimage from _call_showscrollingimage_88
                            bot"Shit... Did I push her too hard?"
                            call hidescrollingimage from _call_hidescrollingimage_83
                            hide screen parallax1280
                            scene black
                            with dissolve
                            bo"I'll leave you to it then..."


                        

                "{color=[dominancecolor]}????{/color}" if hinata_squatcounter < 3:
                    "Perhaps [hin_name] should get tired first..."
                    jump dominancesquatmenu
                "That's enough...":
                    bo"That's enough. I think I've gathered all the information I needed..."
                    hin"G-good. I was getting tired anyway!"
                    hin"So... W-what did you think about my form?"
                    jump hinata_squathelp
                

        "Can you show me one more?" if hinata_squatcounter <= 3:
            default hinata_squatcounter = 1
            if hinata_squatcounter == 3:
                bo"Another one!"
                hin"[bo_name_stutter]! Are you playing games?" with vpunch
                bo"Just observing some further intricacies..."
                hin"Aren't you... o-observing a little bit too much?"
                scene hinata_squatbehinddown_var with dissolve
                pause 0.4
                show hinata_squatbehinddown with dissolve
                pause 0.4
                show hinata_squatbehindup with dissolve
                hin"That'll be all... Now tell me what you think is wrong please!"
            if hinata_squatcounter == 2:
                bo"I am going to have to see one more..."
                hin"...Is s-something wrong?"
                bo"Just observing some further intricacies..."
                hin"Aren't you... o-observing a little bit too much?"
                scene hinata_squatbehinddown_var with dissolve
                pause 0.4
                show hinata_squatbehinddown with dissolve
                bot"I am observing just enough, [hin_rel]!"
                show hinata_squatbehindup with dissolve
                hin"Was that good?"
                bo"Not too shabby..."
            if hinata_squatcounter == 1:
                bo"Think you can do one more?"
                hin"A-another one...?"
                bo"Just observing some intricacies, if you don't mind..."
                hin"Hmnmm.... F-fine..."
                scene hinata_squatbehinddown_var with dissolve
                bot"That ass..."
                pause 0.4
                show hinata_squatbehinddown with dissolve
                pause 0.4
                show hinata_squatbehindup with dissolve
                hin"Something like that?"
                bo"Not too bad..."
            $ hinata_squatcounter += 1
            jump hinata_squathelp
        "{color=[obediencecolor]}Let's go through each step{/color}":
            bot"It'd be no fun if I said her form is perfect..."
            show borutosquatbehind:
                zoom 1.38 pos (0.39, -682)
            show borutosquatbehind:
                easein 2 alpha 0.1
            with dissolve
            bo"Let's go through each step individually and I'll let you know what I think..."
            hin"O-okay..." with vpunch
            scene squatform1 with dissolve:
                zoom 1.1 xalign 0.6 yalign 0.0
            bo"First, you want your hips just about where you have them..."
            hin"M-my hips...?" with vpunch
            menu:
                hin"M-my hips...?"
                "{color=[obediencecolor]}Yes, but a tad bit closer...{/color}":
                    bo"Yes, but bring them a little bit..."
                    show squatform1_1 with dissolve
                    bo"Closer! Like this..." with vpunch
                    call increaselust(10) from _call_increaselust_166
                    hin"Uhm..."
                    bot"She's letting me feel her ass!"
                    call checkObedience(20,"hinatasquatmad","Hinata") from _call_checkObedience_19
                    hin"Y-your... hands?"
                    scene squatform1_1 with dissolve:
                        zoom 1.1 xalign 0.6 yalign 0.0
                    bo"What about them? Your glutes play a central role to mastering the squat..."
                    bo"You should be feeling some of the burn right about here when you reach the bottom position..."
                    scene squatform1 with dissolve
                    hin"Oh, I s-see..."
                    call changeObedience("Hinata",1) from _call_changeObedience_111
                    hint"I suppose that's part of the process..."
                    bo"Now bend your knees and bring your hips a little lower..."
                "Now go a little lower...":
                    bo"Now bend your knees and bring your hips a little lower..."
            bo"The descent should be controlled, with a simultaneous hip hinge and knee bend..."
            show squatform2_3pull with dissolve
            bo"Just like this..."
            bot"My lord..."
            hin"Uhm... N-now what?"
            bo"Right about here is when you should be bracing your core. Before you reach full depth, make sure you draw a deep breath and brace your abdominal muscles. This will stabilize your spine..."
            hin"Y-you really know your stuff, don't you..."
            menu squatmenu2:
                hin"Y-you really know your stuff, don't you..."
                "Put your hands on her thighs...":
                    show squatform2 with dissolve
                    bo"Of course I do! How do you reckon I got as strong as I did in such a short amount of time?"
                    hin"..." with vpunch
                    hin"I s-suppose so. What next?"
                    bo"Now for the part where most fail to comprehend..."
                    bo"See how your posterior is currently above your knee line?"
                    hin"Y-yeah...?"
                    bo"You'll have to drop your hips lower than your knee line, as close to the floor as possible..."
                    bo"Given your mobility, I am sure you have no issue doing so, but try to maintain complete balance by having your heel and toes maintain contact with the ground..."
                    hin"A bit c-complicated, but I think I got it..."
                    bo"To simplify, ass to grass [hin_rel]!" with vpunch
                    

                "{color=[dominancecolor]}Put your hands on her ass!{/color}":
                    call checkDominance(20,"squatmenu2") from _call_checkDominance_24
                    bot"Fuck... I can't resist it!"
                    bot"Will I be able to bullshit my way out of..."
                    show squatform2_1 with dissolve
                    bot"This!" with vpunch
                    hin"[bo_name_stutter]! W-what are you doing!" with vpunch
                    show hinata_squatbehinddown_var with dissolve
                    bo"Oh, did I startle you?"
                    hin"Y-you can't just grab my p-posterior like that!"
                    bo"That wasn't my intention... I was about to show you one of those secrets you wanted me to share..."
                    call checkObedience(25,"hinatasquatmad","Hinata") from _call_checkObedience_20
                    bo"If you would like me to do that of course..."
                    hin"N-now I am intrigued..."
                    bo"It'll be worth it, I promise!"
                    call changeObedience("Hinata",1) from _call_changeObedience_112
                    hin"L-let's see it then..."
                    scene squatform2_1 with dissolve
                    bo"You see..."
                    $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                    show hinata_squatgrope1 with dissolve
                    bo"This muscle right here, the gluteus maximus, plays an important part in pacing yourself when squating..."
                    "You started groping her ass under the pretense of your 'secret'..."
                    hin"H-how so..."
                    bot"My god! This is the first time she willingly let me touch her like this..."
                    $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                    call increaselust(10) from _call_increaselust_167
                    bot"What an amazing feeling. I get this urge to bury my face in there and lick the sweat straight from-"
                    hin"...H-hello?" with vpunch
                    bo"*Ahem!* As I was s-saying..." with vpunch
                    bo"Most people tire themselves out by loading most of the effort to their quads and hamstrings..."
                    $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                    bo"Instead, when you reach for depth on this next step, I want you to try to spread the load evenly between your legs and your glutes..."
                    call changeDominance(1) from _call_changeDominance_82
                    bo"Meaning, this part right here!" with vpunch
                    hin"Okay, I think I g-got it! Can you stop t-that now...?"
                    scene hinata_squatbehinddown_var with dissolve
                    bo"You'll have to show me then! Let's see it..."
                    bo"Ass to grass!" with vpunch


                    
                "{color=[obediencecolor]}Touch her pussy!{/color}":
                    bot"D-damn it! I am getting intrusive thoughts..." with vpunch
                    show squatform2_3pull with dissolve:
                        zoom 1.2 xalign 0.5 yalign 1.0
                    bot"I can even see her pussy lips through her tight yoga pants..."
                    bot"I get this urge to stick my fingers in there..."
                    bot"And take a whiff of her pussy juices!" with vpunch
                    scene squatform2_2 with dissolve
                    show squatform2_2 with dissolve:
                        zoom 1.2 xalign 0.5 yalign 1.0
                    call increaselust(10) from _call_increaselust_168
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp4.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    scene black with vpunch
                    call changeObedience("Hinata",1) from _call_changeObedience_113
                    hin"[bo_name_stutter]! W-what was that! Did you j-just touch my..." with vpunch
                    bo"It's not w-what you think! T-there was a... b-bug on your pants! I just brushed it off!"
                    call changeRespect("Hinata", -1) from _call_changeRespect_184
                    hin"Then l-let me know in advance and I'll do that my self! You i-idiot..." with vpunch
                    bo"You are right! I am sorry..."

                    jump hinatasquatmad


                "{color=[hatredcolor]}Pull a stupid prank on her!{/color}":
                    call checkHatred(30,"squatmenu2") from _call_checkHatred_19
                    bo"Right...?"
                    bo"There's another secret I am willing to share with you..."
                    hin"Oh, I can't wait..."
                    bo"You see... I always exercise without my shirt on. Do you know why?"
                    show squatform2_4pull with dissolve
                    hin"W-wait a second..."
                    bo"Because the body is meant to move freely!" with vpunch
                    show squatform2_4pull2 with dissolve
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp4.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    show squatform2_4pull3 with dissolve
                    scene black with vpunch
                    hin"*Gasp*!" with vpunch
                    call changeHatred(1) from _call_changeHatred_135
                    bo"How's that for a secret!" with vpunch
                    call changeRespect("Hinata", -3) from _call_changeRespect_185
                    hin"You s-stupid p-prankster! Do not ever try anything like that again!" with vpunch
                    scene black with vpunch
                    $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                    "[hin_name] left the room in total frustration..."
                    bot"Whatever, I'll just pretend it was a harmless prank!"
                    show squatform2_4pull3 with dissolve
                    bot"Seeing that beautiful fat ass of hers up close was worth it!"
                    call increaselust(10) from _call_increaselust_169
                    bot"Her black lace trim panties, the sweat dripping down her butt cheeks - The image is burned in to my mind..."
                    scene black with dissolve
                    $ renpy.end_replay()
                    jump action_taken


            show squatform3 with dissolve
            hin"Y-you gotta stop saying t-that..."
            bo"That's some impressive depth, [hin_rel]!" with vpunch
            call changeObedience("Hinata",1) from _call_changeObedience_114
            hin"Uhm... T-thank you, I suppose?"
            hin"Is this what you wanted to see...?"
            menu squatmenu3:
                hin"Is this what you wanted to see...?"
                "Perfect form, [hin_rel]!":
                    pass
                "{color=[obediencecolor]}Test her limits...{/color}":
                    bo"You've got it down almost perfectly..."
                    hin"...Almost?"
                    show squatform3_1 with dissolve
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp4.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    bo"You are missing the final piece of the puzzle..." with vpunch
                    call checkObedience(30,"hinatasquatmad","Hinata") from _call_checkObedience_21
                    hin"I a-am...?" with vpunch
                    bo"You see... while you reach optimal depth, the way your weight is distributed seems imbalanced..."
                    hin"H-how so..."
                    bo"You are almost shifting your weight forward and onto your toes..."
                    bo"Instead, Your weight should be balanced over your core! That way..."
                    $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                    show hinata_squatgrope2 with dissolve
                    bo"You can shift some of the strain to this area down here..."
                    hint"!" with vpunch
                    call changeObedience("Hinata",1) from _call_changeObedience_119
                    hint"H-he is definitely t-touching my behind! Is this really even about f-form at this point?"
                    bo"If you aren't feeling some of the burn in your glutes, you are doing something wrong!"
                    call increaselust(10) from _call_increaselust_170
                    bot"A perfect blend of firmness and squishiness... What an amazing feeling!" with vpunch
                    bot"She isn't even bothered when I grab a handful! Does she really think all this is abour her form?"
                    scene squatform3_2spank0 with dissolve
                    hin"I u-understand... I t-think! Can we move on please?" with vpunch
                    bo"Right..."
                    bot"Fuck me! The things I'd do to that ass if it were mine to toy with as I pleased..."



                "{color=[hatredcolor]}Spank her!{/color}":
                    call checkHatred(35,"squatmenu3") from _call_checkHatred_20
                    bo"This is exactly what I wanted to see!" with vpunch
                    bot"Your ass is looking fucking amazing like this, [hin_rel]!"
                    hin"O-okay... What's next then?"
                    show squatform3_2spank0 with dissolve
                    bot"I just have to show it some love!"
                    bo"Next..."
                    show h_wrestle_spank with moveinleft
                    $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                    with vpunch
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    hide h_wrestle_spank
                    show squatform3_2spank2 
                    with dissolve
                    bo"Is you going up! Atta girl!" with vpunch
                    scene black with vpunch
                    hin"*Gasp* [bo_name_stutter]!" with vpunch
                    call changeRespect("Hinata",-5) from _call_changeRespect_186
                    hin"W-what the hell are you doing! You can't be doing that!" with vpunch
                    bo"Relax [hin_rel], it was just some encouragement..."
                    hin"You are way over the line, [bo_name]! You can't just hit your [hin_rel_mother]'s behind and call it 'encouragement'!"
                    jump hinatasquatmad
            bo"You got that motion down!"
            bo"Now for the easy part..."
            bo"An explosive ascent to the top! Drive through your entire foot while keeping your core engaged!"
            bo"The less time you spent on the extension, the more energy you preserve!"
            hin"S-smart... I didn't know that!"
            bo"Aaand..."
            scene squatform1 with dissolve
            bo"...Up you go!" with vpunch
            hin"*Exhales* Phew!" with vpunch
            menu:
                hin"*Exhales* Phew!"
                "Excellent job!":
                    show hinata_squatbehindup with dissolve
                    bo"Excellent job [hin_rel]! That was impressive form control..."
                "{color=[obediencecolor]}Feel her up one last time...{/color}":
                    show squatform1_1 with dissolve
                    bo"Nice work [hin_rel]! Feeling the burn in your glutes yet?" with vpunch
                    call checkObedience(30, "hinatasquatmad","Hinata") from _call_checkObedience_22
                    hin"Y-yeah... I think so..."
                    scene squatform1 with dissolve
                    bo"A job well done then! That was impressive..."
                    show squatform1_1 with dissolve:
                        zoom 1.2 xalign 0.5 yalign 0.5
                    bo"...form control, [hin_rel]. I am proud of you!"
                    hin"T-thank you..."
                    call increaselust(10) from _call_increaselust_171
                    bot"She isn't even mentioning it! F-fuck... I am getting addicted to this feeling!"
            show hinata_squat_behindface with dissolve:
                yalign 0.5
            show hinata_squat_behindface:
                easein 3 yalign 0.0
            hin"Let's wrap up this session then... s-shall we?"
            bo"I was hoping we could do more, you know..."
            hin"M-maybe next time? I am getting pretty tired..."
            scene black with dissolve
            bo"Alright then..."
            hin"[bo_name_stutter]..."
            show hinata_bedroomtraining_idle with dissolve
            call changeRespect("Hinata",1) from _call_changeRespect_187
            hin"Thanks for the... h-help, and the advice!"
            hin"I enjoyed your company, but..."
            hin"Let's try to keep things, uhm... normal?"
            bo"Is something wrong [hin_rel]?"
            hin"Not particularly. I am just worried about you..."
            hin"I'll see you around, okay?"
            scene black with dissolve
            $ renpy.sound.play("/audio/soun_fx/doorclose.opus", channel="sfx3", loop=False, relative_volume = 1.0)
            bo"You sure will!"
            bot"I guess she isn't that oblivious to my... advances!"
            bot"I'll have to be careful..."
            scene black with dissolve
            $ renpy.end_replay()


                
                

            
            
                
        



    $ hinata_squat_1sttime = True

    $ hinata_squatcounter = 0
    jump action_taken

label hinatasquatmad:
    scene black with vpunch
    hin"O-okay! I've had enough of this!"
    call changeRespect("Hinata", -2) from _call_changeRespect_188
    show hinata_squat_behindface with dissolve:
        yalign 0.6
    show hinata_squat_behindface:
        easein 3 yalign 0.0
    hin"I am not s-sure this is what I thought it would be..."
    scene black with vpunch
    $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx2", loop=False, relative_volume = 0.7)
    "[hin_name] left the room in what seemed like pent-up frustration..."
    bot"S-shit... Did I blew it?"
    $ renpy.end_replay()
    jump action_taken


label hinatsquatmassagefail:
    hide screen parallaxcentered
    scene black with vpunch
    hin"U-uhm, I don't feel too comfortable with that!"
    show hinata_squat_behindface with dissolve:
        yalign 0.6
    show hinata_squat_behindface:
        easein 3 yalign 0.0
    hin"M-maybe some other time?"
    hin"I am not s-sure this is what I thought it would be..."
    scene black with vpunch
    $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx2", loop=False, relative_volume = 0.7)
    "[hin_name] left the room in what seemed like pent-up frustration..."
    bot"S-shit... Did I blew it?"
    $ renpy.end_replay()
    jump action_taken

label hinata_stretch_label:
    $ initialize_replay_defaults()
    if _in_replay:
        $ percentage = 0
    bo"I could probably show you a few stretching tips that could come in handy......"
    scene watch4 with dissolve:
        zoom 1.2 xalign 0.5 yalign 0.0
    hin"Hmmm...? You think there's something I could learn from you?"
    scene watch4 with dissolve
    bo"Considering that you lost to me... Maybe you could use a few of my 'secrets'!"
    scene black with dissolve
    hin"Oooh...? Secrets you say?"
    "[hin_name] lies on her training mat..."
    show hinata_exhausted with dissolve:
        yalign 1.0 xalign 0.5
    show hinata_exhausted:
        easein 5 yalign 0.0
    label youcouldusesomestretching:
    hin"To be fair, I am exhausted after facing you, and I was planning on wrapping up with some stretching, so..."
    hin"Let's see what those so called 'tips' of yours are all about..."
    scene black with dissolve
    show screen parallaxcentered("frontstretch_start",1,1.0,True,[0.7, 1.2]) with dissolve
    call showscrollingimage from _call_showscrollingimage_89
    default frontstretchmenu1_counter = 0
    menu frontstretchmenu1:
        hin"..."
        "Gotta make sure you give your legs a good stretch...": #legs
            default frontstretchmenu1 = False
            if frontstretchmenu1 == True:
                show screen parallaxcentered("hinata_stretch_frontstretch_legs",1,1.0,True,[0.7, 1.2])
                with dissolve
                $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                hin"A-ah... M-my legs again?" with vpunch
                bo"Don't be alarmed... Legs being the largest muscle group of our bodies, often require a little extra attention!"
                hin"I s-suppose you are right on that count..."
                bot"I just can't resist those sexy, athletic legs of hers..."
            else:    
                hide screen parallaxcentered
                show screen parallaxcentered("frontstretch1",1,1.0,True,[0.7, 1.2])
                with dissolve
                bo"First..."
                show screen parallaxcentered("hinata_stretch_frontstretch_legs",1,1.0,True,[0.7, 1.2])
                with dissolve
                $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                hin"A-ah..." with vpunch
                bo"Let's start with your legs - they must have knotted up with tension after all those squats..."
                hin"Y-yes, especially my quads..."
                bo"Leave it to me. Some light strokes right about here ought to release all that tension..."
                hin"Mhmm... S-sure!"
                bot"[hin_rel]'s thighs... They are so soft to my touch, but as soon as I press my palms down on her legs, all that muscle underneath quickly becomes apparent..."
                call increaselust(5) from _call_increaselust_177
                bot"F-fuck! She's so unbelievably hot! I wonder how it'd feel without these sexy yoga pants of hers covering her skin..."
                if percentage >= 95:
                    "Something was quickly growing under your pants..."
                    bot"T-this is the worst time to be getting a freaking massive boner! I hope she doesn't notic-"
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                    scene black
                    hide screen parallaxcentered
                    hin"[bo_name_stutter]!" with vpunch
                    bo"Uuh, w-what's wrong?"
                    call checkLust(200) from _call_checkLust_5
                    bot"F-fuck she definitely noticed!"
                    jump hinatasquatmad

            $ frontstretchmenu1 = True
            $ frontstretchmenu1_counter +=1
            jump frontstretchmenu1
        "Your abdominal muscles should be relaxed...": #legs2
            default frontstretchmenu2 = False
            if frontstretchmenu2 == False:
                hide screen parallaxcentered
                show screen parallaxcentered("frontstretch2",1,0.5,True,[0.7, 1.2])
                with dissolve
                hin"[bo_name_stutter]!?" with vpunch
                bo"Is something wrong? Your abdominal muscles are quite tense..."
                hin"Y-you think so?"
                show screen parallaxcentered("frontstretch2_1",1,0.5,True,[0.7, 1.2]) with dissolve
                bo"I even feel some knotting around here..." with vpunch
                hin"A-ah!"
                bo"Want me to take care of it for you?"
                hin"Uhm... I s-suppose there's no harm in that, but don't stray further from my abdomen, okay?"
                show screen parallaxcentered("hinata_stretch_frontstretch_stomach",1,1.0,True,[0.7, 1.2]) with dissolve
                $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                bo"Is that supposed to mean something, [hin_rel]?"
                hin"N-no... It's just that, I am not too c-comfortable, *Soft Groan* w-with how touchy assisted s-stretching can get..."
                hin"I get all t-tingly around my stomach, and your hands are warm! The sensation is quite foreign..."
                hin"A-although I do admit, your touch feels quite reserved, nice even... It really seems like you know your s-stuff..."
                bo"R-right?"
                bot"D-damn! She really has no problem letting me rub her beautifully toned tummy..."
                call increaselust(10) from _call_increaselust_178
                bot"I've no idea how she manages to sculpt such a perfectly tight, sexy stomach at her age, let alone after giving birth twice!"
                if percentage >= 95:
                    "Something was quickly growing under your pants..."
                    bot"T-this is the worst time to be getting a freaking massive boner! I hope she doesn't notic-"
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                    scene black
                    hide screen parallaxcentered
                    hin"[bo_name_stutter]!" with vpunch
                    bo"Uuh, w-what's wrong?"
                    call checkLust(200) from _call_checkLust_6
                    bot"F-fuck she definitely noticed!"
                    jump hinatasquatmad
            else:
                show screen parallaxcentered("hinata_stretch_frontstretch_stomach",1,1.0,True,[0.7, 1.2])
                with dissolve
                $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                hin"[bo_name_stutter]! M-my abdomen again?" with vpunch
                bo"I thought I felt some tightness around this place..."
                hin"Do you f-feel it too?"
                hin"N-no...? I don't think so at least. Just the usual m-mild soreness..."
                bot"Hope you don't mind my stupid excuse to feel your sexy stomach again, [hin_rel]..."
                hin"Can we move on to something else p-please? The t-tingling is quite irritating..."

            $ frontstretchmenu2 = True
            $ frontstretchmenu1_counter +=1
            jump frontstretchmenu1
        "Your core area seems to be tense..." if frontstretchmenu1_counter >= 2: #core
            hide screen parallaxcentered
            show screen parallaxcentered("frontstretch1_1",1,0.5,True,[0.7, 1.2])
            with dissolve
            bo"Your core area seems to easily tense up, [hin_rel]..."
            hin"It d-does...?"
            bo"I'll take care of it for you in one sweeping motion if you don't mind..."
            hin"U-uhm.. Sure!"
            show screen parallaxcentered("hinata_stretch_frontstretch_legsstomach",1,0.5,True,[0.7, 1.2]) with dissolve
            $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
            bo"I can tell how tense you are from just a few timid touches. But don't worry, this will certainly help you relax!"
            hint"Isn't he r-rubbing a little bit too hard?"
            bo"Your hips in particular..."
            call increaselust(10) from _call_increaselust_179
            $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
            if percentage >= 95:
                "Something was quickly growing under your pants..."
                bot"T-this is the worst time to be getting a freaking massive boner! I hope she doesn't notic-"
                $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                scene black
                hide screen parallaxcentered
                hin"[bo_name_stutter]!" with vpunch
                bo"Uuh, w-what's wrong?"
                call checkLust(200) from _call_checkLust_7
                bot"F-fuck she definitely noticed!"
                jump hinatasquatmad
            $ frontstretchmenu1_counter +=1
            hin"M-my hips? What's wrong with my hips..."
            bot"What else [hin_rel]! They are sexy as fuck and get me going..." with vpunch
            bo"T-they seem quite tense. As if they were carrying more load than what would be optimal. Perhaps due to your squatting form?"
            hin"I s-see... So I should work on my form, huh?"
            bo"Don't worry, a few more sessions with me and we'll set that straight in no time!"
            hin"R-right..."
            hint"T-then again, [bo_name] knows what he is doing, and it feels quite nice too..."
            hint"N-nothing wrong with some light stretching assistance..."
            jump frontstretchmenu1
        "Your chest area needs some attention too!": #breasts1
            hide screen parallaxcentered
            show screen parallaxcentered("frontstretch1_1",1,0.6,True,[0.7, 1.2]) with dissolve
            bo"[hin_rel], there's another area I think could use some attention if you don't mind..."
            hin"As long as it's n-nothing innapropriate..."
            bot"Titties..."
            call increaselust(10) from _call_increaselust_180
            bot"tiitties, tiddies, tits, TIDDIES!! I need to feel them! Just once... Just one squeeze!" with vpunch
            $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
            show screen parallaxcentered("frontstretch3",1,0.6,True,[0.7, 1.2]) with dissolve
            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx2", loop=False, relative_volume = 1.0)
            hide screen parallaxcentered
            show frontstretch3 with dissolve:
                zoom 1.4 xalign 0.5 yalign 0.1
            hin"Gasp!" with vpunch
            scene black
            $ renpy.sound.play("/audio/soun_fx/spank4.opus", channel="sfx2", loop=False, relative_volume = 1.0)
            call changeRespect("Hinata",-10) from _call_changeRespect_197
            "[hin_name] slapped you in the face!" with vpunch
            hin"[bo_name_stutter]! W-why would you do that!" with vpunch
            bo"[hin_rel_stutter] it was just... stretchin-"
            hin"Enough! I won't hear any more of it! I am your [hin_rel_mother], you idiot! You cannot t-touch me like that..." with vpunch
            jump hinatasquatmad
        "{color=[obediencecolor]}Let's move on...{/color}" if frontstretchmenu1_counter >= 3:
            pass
        "{color=[obediencecolor]}????{/color}" if frontstretchmenu1_counter < 3:
            "Help [hin_name] with her 'stretching' without scaring her..."
            jump frontstretchmenu1

    hide screen parallaxcentered
    show screen parallaxcentered("frontstretch1",1,0.0,True,[0.7, 1.2]) with dissolve
    bo"Let's move on..."
    hide screen parallaxcentered
    show screen parallaxcentered("frontstretch1_1",1,0.0,True,[0.7, 1.2])
    with dissolve
    hin"M-move on? Move on where exactly..."
    bo"Oh, I was thinking I'd show you some more advanced stretching techniques if you don't mind..."
    call checkObedience(34,"hinatsquatmassagefail","Hinata") from _call_checkObedience_26
    hin"A-advanced, eh? I am a bit curious I admit..."
    hin"Although I am wondering if it's right for us to be working out together, considering your..."
    bo"[hin_rel], this is just some mild stretching, isn't it?" with vpunch
    bo"How could my condition affect something like this, especially when it's with you no less!"
    hide screen parallaxcentered
    show screen parallaxcentered("frontstretch1_2",1,0.0,True,[0.7, 1.2])
    with dissolve
    hin"H-hey! That came off rude..." with vpunch
    hide screen parallaxcentered
    show screen parallaxcentered("frontstretch1_1",1,0.0,True,[0.7, 1.2])
    with dissolve
    bo"You know what I meant! With you being my [hin_rel] and all... Heh-eh *Nervous laughter*"
    hide screen parallaxcentered
    show screen parallaxcentered("frontstretch1_2",1,0.0,True,[0.7, 1.2])
    with dissolve
    hin"*Giggles* R-right? What kind of [hin_rel_to_bo] would think of his [hin_rel_mother] like that..."
    bot"If only you knew..."
    hide screen parallaxcentered
    show screen parallaxcentered("frontstretch1_1",1,0.0,True,[0.7, 1.2])
    with dissolve
    hin"I suppose there's no harm in seeing some of your advanced techniques then..."
    hide screen parallaxcentered
    show screen parallaxcentered("frontstretch1_2",1,0.0,True,[0.7, 1.2])
    with dissolve
    hin"Let's see it then, trainer [bo_name]! *Teasing giggle*"
    bo"We'll see if you'll still be laughing after this!"
    hide screen parallaxcentered
    show screen parallaxcentered("legstretch1",1,0.0,True,[0.7, 1.2])
    with dissolve
    hin"Oh!" with vpunch
    "You abruptly lift one of her legs and place it on your shoulder..."
    default frontstretchmenu2_counter = 0
    menu frontstretchmenu2:
        hin"..."
        "Massage her inner thighs...": #legs
            bo"Let's get those legs even more limber..."
            hide screen parallaxcentered
            show screen parallaxcentered("hinata_legstretchanim1",1,1.0,True,[0.7, 1.2]) #anim
            with dissolve
            $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
            hin"Ah! T-that's..."
            bo"Trust me [hin_rel], this will feel amazing after..."
            hin"It a-already does..."
            hint"Though he is a bit too close to spots he shouldn't be I think..."
            bo"Certain muscles are tougher to reach than others..."
            bo"With your leg raised like this, I can easily apply some pressure to your hamstrings to alleviate some of the deeper muscle knotting..."
            hin"H-huh... *Ahh..* Interesting..."
            bot"Her thighs are burning up!"
            call increaselust(10) from _call_increaselust_181
            bot"The sight of her, the feeling of her thighs, the exerted body heat... F-fuck! I am getting way too aroused! I am so close to her p-privates too..."
            if percentage >= 95:
                "Something was quickly growing under your pants..."
                bot"T-this is the worst time to be getting a freaking massive boner! I hope she doesn't notic-"
                $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                scene black
                hide screen parallaxcentered
                hin"[bo_name_stutter]!" with vpunch
                bo"Uuh, w-what's wrong?"
                call checkLust(200) from _call_checkLust_8
                bot"F-fuck she definitely noticed!"
                jump hinatasquatmad
            bot"One slip of my hand and I could catch a feel of her-"

            hin"S-should we try something else?" with vpunch
            hide screen parallaxcentered
            show screen parallaxcentered("legstretch1",1,1.0,True,[0.7, 1.2]) #anim
            with dissolve
            bo"If that's what you want..."
            $ frontstretchmenu2_counter += 1
            jump frontstretchmenu2
        "Press on her lower abdomen...": #stomach
            hide screen parallaxcentered
            show screen parallaxcentered("legstretch1",1,1.0,True,[0.7, 1.2])
            with dissolve
            bo"Don't be alarmed with this next one..."
            hide screen parallaxcentered
            show screen parallaxcentered("legstretch2_2",1,0.5,True,[0.7, 1.2])
            with dissolve
            hin"[bo_name_stutter]...? Y-you are pressing a little h-hard!"
            bo"Yes, but..."
            hide screen parallaxcentered
            show screen parallaxcentered("hinata_naveltretchanim1",1,0.5,True,[0.7, 1.2])
            with dissolve
            $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
            bo"Feel how your abdomen relaxes after a few circular motions of my fingers?"
            call increaselust(10) from _call_increaselust_182
            bot"I am spreading her stomach around... her navel is brushing against my fingers!"
            if percentage >= 95:
                "Something was quickly growing under your pants..."
                bot"T-this is the worst time to be getting a freaking massive boner! I hope she doesn't notic-"
                $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                scene black
                hide screen parallaxcentered
                hin"[bo_name_stutter]!" with vpunch
                bo"Uuh, w-what's wrong?"
                call checkLust(200) from _call_checkLust_9
                bot"F-fuck she definitely noticed!"
                jump hinatasquatmad
            hin"Ahh! It's a little bit p-painful *Groans* But somewhat s-satisfying too..."
            bo"R-right...?"
        
            $ frontstretchmenu2_counter += 1
            jump frontstretchmenu2

        "Do you mind if I shift your posture around?" if frontstretchmenu2_counter >=2 and hinata_stretchribs == False: #stomach
            hide screen parallaxcentered
            show screen parallaxcentered("legstretch1",1,1.0,True,[0.7, 1.2])
            with dissolve
            bo"Would you mind if I shift your posture around a bit?"
            hin"Uhm... For what purpose would that be?"
            bo"It'd be much easier to get a deeper stretch for your back and waist with what I have in mind..."
            hin"That does sound nice, I t-think..."
            hin"Let's see it!"
            hide screen parallaxcentered
            screen black
            with dissolve
            bo"Let's get this leg over the other, and..."
            hide screen parallaxcentered
            show screen parallaxcentered("pinch_anim1",1,0.5,True,[0.7, 1.2])
            with dissolve
            bo"Just like that. Are you feeling the deeper stretch in your back?"
            hin"Y-you are right! It d-does feel nice..."
            menu hinata_ribmassage:
                hin"Y-you are right! It d-does feel nice..."
                "Massage her ribs":
                    default hinata_stretchribs = False
                    $ hinata_stretchribs = True
                    bo"Now to add a little pressure..."
                    hide screen parallaxcentered
                    show screen parallaxcentered("hinata_stretchpinchanim1",1,0.5,True,[0.7, 1.2])
                    with dissolve
                    bo"...Right about here!"
                    hin"Aah! Don't p-pinch too hard..." with vpunch
                    bo"You sure? The deeper I reach for the muscle, the more relief you'll feel..."
                    hin"M-maybe a little bit more then..."
                    bot"I feel like she's opening up a little bit more than usual!"
                    jump hinata_ribmassage
                "{color=[obediencecolor]}Move higher!{/color}" if hinata_stretchribs == True:
                    bo"Next, I'll have to move a little bit higher..."
                    hin"H-higher?" with vpunch
                    if massageknowledge <1:
                        bot"Hehe! I wonder if I could pass this off as some sort of advanced massage technique!"
                        play sound("/audio/soun_fx/attributeslost.opus")
                        hide screen scrollingtext
                        show screen scrollingtext("Missing massage knowledge") onlayer screens
                        hide screen parallaxcentered
                        show screen parallaxcentered("pinch2",1,0.5,True,[0.7, 1.2])
                        with dissolve
                        $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                        hin"*Gasp!* [bo_name_stutter], s-stop! What do you think you are doing?"
                        bo"I was j-just massa-"
                        call changeRespect("Hinata",-3) from _call_changeRespect_198
                        hide screen parallaxcentered
                        show pinch2 with dissolve:
                            zoom 1.4 xalign 0.5 yalign 0.1
                        scene black
                        hin"Enough! I won't hear any more of it! I am your [hin_rel_mother], you idiot! You cannot t-touch me like that..." with vpunch
                        jump hinatasquatmad
                    else:
                        bot"With my newly acquired massage knowledge, maybe this will work!"
                        bo"Just a tiny bit higher, yes. Though you don't have to worry..."
                        bo"This is a very common massage technique. Deep tissue they call it! Specifically for your ribcage..."
                        hide screen scrollingtext
                        play sound("/audio/soun_fx/attributes.opus")
                        show screen scrollingtext("Massage knowledge opportunity!")
                        hin"Okay then... I'll trust you on this one!"
                        bo"Here goes..."
                        hide screen parallaxcentered
                        show screen parallaxcentered("pinch2",1,0.5,True,[0.7, 1.2])
                        with dissolve
                        $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp3.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                        hin"*Gasp* T-that's..." with vpunch
                        bot"I can't stop now!"
                        $ renpy.sound.play("/audio/soun_fx/grope1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                        hide screen parallaxcentered
                        show screen parallaxcentered("hinata_stretchpinctitsanim",1,0.5,True,[0.7, 1.2])
                        with dissolve
                        $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp4.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                        bo"Now if I pinch deeper into the tissue here..."
                        hin"[bo_name_stutter] you can't... *Ahh..*!" with vpunch
                        bo"It's nothing s-serious [hin_rel]... Don't you feel the tension dispersing like this?"
                        hin"B-but y-you are being a bit too... t-thorough, no?"
                        bo"You are losing focus [hin_rel]. You should be twisting your waist a little harder if you want this deep stretch to be felt in its entirety..."
                        call increaselust(10) from _call_increaselust_183
                        hin"M-maybe we should try s-something else...?"
                        bot"[hin_rel]'s underboob... What a sublime feeling! I get this uncontrollable urge to bury my fingers in her breast! It feels so soft, so squishy! inviting even..."
                        if percentage >= 95:
                            "Something was quickly growing under your pants..."
                            bot"T-this is the worst time to be getting a freaking massive boner! I hope she doesn't notic-"
                            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                            scene black
                            hide screen parallaxcentered
                            hin"[bo_name_stutter]!" with vpunch
                            bo"Uuh, w-what's wrong?"
                            call checkLust(200) from _call_checkLust_10
                            bot"F-fuck she definitely noticed!"
                            jump hinatasquatmad
                        hide screen parallaxcentered
                        show screen parallaxcentered("pinch2",1,0.5,True,[0.7, 1.2])
                        with dissolve
                        hin"[bo_name_stutter]!" with vpunch
                        hide screen parallaxcentered
                        show screen parallaxcentered("pinch_anim1",1,0.5,True,[0.7, 1.2])
                        with dissolve
                        bo"R-right, just making sure you get the full experience..."
                        bot"Damn it! Maybe a few more sessions and I'll get my chance..."
                        call changeObedience("Hinata",1) from _call_changeObedience_120
                        hin"N-not sure if this is the experience I was looking for..."
                        hin"Nonetheless, it was nice to try... once!"
                        hin"Let's do something else, please?"
                        hide screen parallaxcentered
                        show screen parallaxcentered("legstretch1",1,0.5,True,[0.7, 1.2])
                        with dissolve
                        bo"Right..."
                        jump frontstretchmenu2
                "Go back...":
                    bo"Let's try something else..."
                    hide screen parallaxcentered
                    show screen parallaxcentered("legstretch1",1,0.5,True,[0.7, 1.2])
                    with dissolve
                    bo"Okay..."
                    jump frontstretchmenu2
                


            $ frontstretchmenu2_counter += 1
            jump frontstretchmenu2

        "{color=[hatredcolor]}Slip a finger in her pussy!{/color}": 
            hide screen parallaxcentered
            show screen parallaxcentered("legstretch1_1",1,1.0,True,[0.7, 1.2])
            with dissolve
            hin"Oh, my legs a-again?"
            hide screen parallaxcentered
            show screen parallaxcentered("hinata_legstretchanim1",1,1.0,True,[0.7, 1.2])
            with dissolve
            $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
            bo"Y-your legs, yes. They need some extra attention!"
            hin"A-attention?"
            bot"I am so close to h-her pussy! I could just pretend my hand slipped, or something!"
            bot"Fuck it! I want to feel [hin_rel]'s pussy! Even if it's just this once time!" with vpunch
            show screen parallaxcentered("legstretch3",1,0.6,True,[0.7, 1.2]) with dissolve
            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx2", loop=False, relative_volume = 1.0)
            hide screen parallaxcentered
            show legstretch3 with dissolve:
                zoom 1.4 xalign 0.5 yalign 0.1
            pause 0.2
            show legstretch3 with dissolve:
                zoom 1.4 xalign 0.5 yalign 1.0
            hin"Gasp!" with vpunch
            bot"H-holy shit! I am s-stretching her vulva with my thumb!" with vpunch
            $ renpy.sound.play("/audio/soun_fx/spank4.opus", channel="sfx2", loop=False, relative_volume = 1.0)
            call changeRespect("Hinata",-10) from _call_changeRespect_199
            scene black
            "[hin_name] slapped you in the face!" with vpunch
            hin"[bo_name_stutter]! W-why would you do that!" with vpunch
            bo"M-my h-hand just slipped! It was an accid-"
            hin"Enough! I won't hear any more of it! I am your [hin_rel_mother], you idiot! You cannot t-touch me like that..." with vpunch
            call changeHatred(1) from _call_changeHatred_140
            if hatred >= 20:
                bot"Bitch! She'll pay for this..."
            else:
                bot"What did I expect..."
            jump hinatasquatmad

        "{color=[obediencecolor]}????{/color}" if frontstretchmenu1_counter < 2:
            "Help [hin_name] with her 'stretching' without scaring her..."

        "{color=[obediencecolor]}Let's move on to the final phase...{/color}" if frontstretchmenu1_counter >=2:
            pass

    hide screen parallaxcentered
    scene black 
    with dissolve
    bo"Are you ready to move on to the final phase?"
    hin"T-there's..."
    show screen parallaxcentered("hinata_exhausted",1,0.0,True,[0.7, 1.2])
    with dissolve
    hin"...More?"
    hin"I am already feeling a bit... too r-relaxed! Not to mention exhausted..."
    hin"I think we should stop here... don't you agree?"
    bo"Would that not be a waste [hin_rel]? All this trouble... just to leave your back unattended?"
    bot"Come on, come on...!"
    hin"[bo_name]..."
    call checkObedience(39,"hinatsquatmassagefail","Hinata") from _call_checkObedience_27
    hin"...you sure are a persistent t-trainer, aren't you?"
    hide screen parallaxcentered
    show screen parallaxcentered("frontstretch1_2",1,0.0,True,[0.7, 1.2])
    with dissolve
    bo"Only the best, for the best..."
    hin"Then just a little bit..."
    bot"Yes!" with vpunch
    bo"You won't regret this..."
    hide screen parallaxcentered
    scene black
    with dissolve
    hin"Give me a second then..."
    "[hin_name] rises to her knees and reluctantly starts turning around..."
    hide screen parallaxcentered
    show screen parallaxcentered("backstretch000",1,0.0,True,[0.7, 1.2])
    with dissolve
    "She turns to you with a look of hesitation, her shoulders visibly tense..."
    hide screen parallaxcentered
    show screen parallaxcentered("backstretch000_1",1,0.0,True,[0.7, 1.2])
    with dissolve
    call increaselust(10) from _call_increaselust_184
    bot"[hin_rel] on her knees, right beneath me... What a fucking view!"
    if percentage >= 95:
        "Something was quickly growing under your pants..."
        bot"T-this is the worst time to be getting a freaking massive boner! I hope she doesn't notic-"
        $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx2", loop=False, relative_volume = 1.0)
        scene black
        hide screen parallaxcentered
        hin"[bo_name_stutter]!" with vpunch
        bo"Uuh, w-what's wrong?"
        call checkLust(200) from _call_checkLust_11
        bot"F-fuck she definitely noticed!"
        jump hinatasquatmad
    hin"So... you want me to get on my stomach?"
    menu randomhinmenu4593:
        hin"So... you want me to get on my stomach?"
        "{color=[hatredcolor]}Spank that ass{/color}":
            call checkHatred(30,"randomhinmenu4593") from _call_checkHatred_21
            hide screen parallaxcentered
            show backstretch000_1 with dissolve:
                zoom 1.4 xalign 0.5 yalign 1.0
            show backstretch000_1 with dissolve:
                easein 4 yalign 0.0
            bot"How can I resist when she almost prostrates beneath me like that..." with vpunch
            hin"Uhm, [bo_name]? You are looking at me weird..."
            bot"I am sorry [hin_rel] but your ass is literally calling for it!"
            scene black
            show backstretch000_1:
                zoom 1.4 xalign 0.5 yalign 1.0
            with dissolve
            pause 0.2
            show h_wrestle_spank with moveinleft
            $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.7)
            with vpunch
            hide h_wrestle_spank
            scene black
            show backstretch000_3
            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx3", loop=False, relative_volume = 1.0) 
            with dissolve
            bo"Come on [hin_rel]! Get that ass on the floor!" with vpunch
            show backstretch000_3 with dissolve:
                xalign 0.5 yalign 0.0
            pause 0.3
            $ renpy.sound.play("/audio/soun_fx/spank4.opus", channel="sfx2", loop=False, relative_volume = 1.0)
            call changeRespect("Hinata",-10) from _call_changeRespect_200
            scene black
            "[hin_name] quickly rose to her feet and slapped you in the face!" with vpunch
            hin"[bo_name_stutter]! W-why would you do that!" with vpunch
            bo"It was just a joke! Will you rela-"
            hin"Enough! I won't hear any more of it! I am your [hin_rel_mother], you idiot! You cannot t-touch me like that! Let alone h-hit my behind!" with vpunch
            call changeHatred(1) from _call_changeHatred_141
            bot"Bitch! You think I'll let you slap me like that?"
            bot"Your time will come, [hin_rel]..."
            jump hinatasquatmad
        "If you don't mind...":
            bo"If you don't mind..."

        "{color=[dominancecolor]}Unless you would prefer to stay on all fours...{/color}":
            bo"That's exactly what you should do..."
            call changeDominance(1) from _call_changeDominance_89
            bo"Unless you would prefer to stay on all fours of course!" with vpunch
            hin"[bo_name_stutter]! Don't make crude remarks. You are better than that..."
            bo"Just a silly little comment [hin_rel], you know you shouldn't take me seriously..."
            call changeRespect("Hinata",-1) from _call_changeRespect_201
            hide screen parallaxcentered
            show screen parallaxcentered("backstretch000",1,0.0,True,[0.7, 1.2])
            with dissolve
            hin"*Sigh...*"


    hide screen parallaxcentered
    show screen parallaxcentered("backstretch000",1,0.0,True,[0.7, 1.2])
    with dissolve   
    hin"Alright then..."
    hide screen parallaxcentered
    show screen parallaxcentered("backstretch0",1,1.0,True,[0.7, 1.2])
    with dissolve
    call increaselust(10) from _call_increaselust_185
    bot"She's just... perfect! There's no other word to describe her!"
    if percentage >= 95:
        "Something was quickly growing under your pants..."
        bot"T-this is the worst time to be getting a freaking massive boner! I hope she doesn't notic-"
        hide screen parallaxcentered
        show screen parallaxcentered("backstretch00",1,0.0,True,[0.7, 1.2])
        with dissolve
        $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx2", loop=False, relative_volume = 1.0)
        scene black
        hide screen parallaxcentered
        hin"[bo_name_stutter]!" with vpunch
        bo"Uuh, w-what's wrong?"
        call checkLust(200) from _call_checkLust_12
        bot"F-fuck she definitely noticed!"
        jump hinatasquatmad
    hin"So...?"
    hin"You said something about leaving my back unattended?"
    bo"Let's get to it..."
    default backstretchmenu1_counter = 0
    menu backstretchmenu1:
        hin"..."
        "Massage her back": #
            hide screen parallaxcentered
            show screen parallaxcentered("backstretch0_5",1,1.0,True,[0.7, 1.2])
            with dissolve
            bo"You ready for this...?"
            hin"Yeah..."
            hide screen parallaxcentered
            show screen parallaxcentered("backstretch0_3",1,1.0,True,[0.7, 1.2])
            with dissolve
            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp3.opus", channel="sfx2", loop=False, relative_volume = 1.0)
            hin"*Gasp* N-not that low, [bo_name]!" with vpunch
            bo"Relax [hin_rel]... Take a deep breath. I know what I am doing, okay?"
            hin"..."
            hide screen parallaxcentered
            show screen parallaxcentered("hinata_stretchback_massage",1,1.0,True,[0.7, 1.2])
            with dissolve
            $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
            hin"Mpfff... That hits the s-spot!"
            bo"Of course it does. Our backs are extremely muscle-dense! Even more so when it comes to one as well trained as yours..."
            hin"Is that... a snide remark? *Ah..* Or a compliment?"
            bo"Could be either..."
            hin"Shut up and keep going, [bo_name]. But don't stray too far p-please..."
            bo"As you wish..."
            hin"*Ah...* *Soft Groan*..." with vpunch
            bot"Every time I slide down to her lower back, my forearms brush against her backside and she doesn't even bring it up!"
            call increaselust(5) from _call_increaselust_186
            hin"*Ah...* Yes... That's the spot..." with vpunch
            bot"Instead, she lets out this soft groans, she is enjoying it, isn't she?"
            bot"But not as much as I am! Her exposed back feels so nice to the touch. The sweat from her body still lingers, acting like a lubricant for my massaging..."
            hin"Mmmmmmhhh..."
            $ backstretchmenu1_counter += 1
            jump backstretchmenu1
        "Massage her legs": #back
            hide screen parallaxcentered
            show screen parallaxcentered("backstretch0_1b",1,1.0,True,[0.7, 1.2])
            with dissolve
            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp3.opus", channel="sfx2", loop=False, relative_volume = 1.0)
            bo"Now for your legs..." with vpunch
            hin"*Soft gasp* C-careful now..."
            bo"It's just your hamstrings [hin_rel]... I'll be careful!"
            bo"...Shall I begin?"
            hide screen parallaxcentered
            show screen parallaxcentered("hinata_stretchbacklegs_massage",1,1.0,True,[0.7, 1.2])
            with dissolve
            $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
            hin"O-okay. But don't stray too far..."
            call increaselust(10) from _call_increaselust_187
            bot"The amount of willpower it takes to not cop a feel..."
            hin"*Soft Groan* Aah..."
            bot"And then she keeps letting out this soft little moans..."
            call increaselust(5) from _call_increaselust_188
            bot"I am losing my fucking mind!" with vpunch
            hin"Mmmpff... *Soft groan* G-good..."
            bo"How's that, [hin_rel]..."
            hin"Mmhh... If I knew you could do this with your hands, maybe I'd ask for help more often!"
            bo"Well, now you can!"
            hin"Indeed I c-can... *Ahmmf*"
            bot"My lord... Will this be a common occurrence now!?" with vpunch
            
            $ backstretchmenu1_counter += 1
            jump backstretchmenu1
        "{color=[obediencecolor]}Full body massage...{/color}" if backstretchmenu1_counter>=2: #full body
            hide screen parallaxcentered
            show screen parallaxcentered("backstretch0_4",1,1.0,True,[0.7, 1.2])
            with dissolve
            bo"Now let's wrap this up with a full body massage, from top to bottom..."
            bo"...Are you ready?"
            hin"I am not too sure about that, [bo_name_stutter]..."
            hide screen parallaxcentered
            show screen parallaxcentered("hinata_stretchfullbody_massage",1,1.0,True,[0.7, 1.2])
            with dissolve
            $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
            bo"Don't you worry! I can circumvent the areas you don't like! Just like this..."
            bo"...See?"
            hin"Mmmhh... That was nice..."
            bo"Shall I keep going then?"
            hin"As long as you don't let your hands w-wander..."
            hide screen parallaxcentered
            show screen parallaxcentered("hinata_stretchfullbody_massagerepeat",1,1.0,True,[0.7, 1.2])
            with dissolve
            bo"Of course..."
            hin"T-thank you... *Mmmhh...*"
            hint"I had no idea [bo_name] was this skilled with his hands. Strong too..."
            hin"That f-feels nice... *Mmmmmaaaah* *Long groan"
            menu:
                hin"That f-feels nice..."
                "{color=[obediencecolor]}It's time to try something!{/color}":
                    hide screen parallaxcentered
                    show screen parallaxcentered("backstretch0_3",1,1.0,True,[0.7, 1.2])
                    with dissolve
                    bot"Fuck... I want to try something so bad!"
                    hin"You... s-stopped? Is it over...?"
                    bo"Doesn't have to be if you don't want it to be! I can go on for a little while longer..."
                    call changeObedience("Hinata",1) from _call_changeObedience_121
                    hin"Then... M-maybe one last pass?"
                    bo"Alright then. Here goes..."
                    bot"This is my last chance!"
                    hide screen parallaxcentered
                    show screen parallaxcentered("hinata_stretchfullbody_massageass",1,1.0,True,[0.7, 1.2])
                    with dissolve
                    $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                    pause 0.4
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp3.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                    bot"If I do... this! She won't suspect a thing..."
                    bot"That ass is to fucking die for!" with vpunch
                    hint"Did he just...!" with vpunch
                    bot"Fuck, now I want more... Just one last time, m-maybe?"
                    bo"Another pass, [hin_rel]?"
                    hin"Uhm..."
                    hint"Must have been an accident I suppose..."
                    menu:
                        hin"Uhm..."
                        "{color=[hatredcolor]}You seem undecided!{/color}":
                            bo"You seem..."
                            hide screen parallaxcentered
                            show screen parallaxcentered("hinata_stretchfullbody_massageass",1,1.0,True,[0.7, 1.2])
                            with dissolve
                            $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                            pause 0.4
                            call changeHatred(1) from _call_changeHatred_142
                            bo"...Undecided!" with vpunch
                            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                            hide screen parallaxcentered
                            hin"Gasp!" with vpunch
                            scene black
                            $ renpy.sound.play("/audio/soun_fx/spank4.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                            
                            call changeRespect("Hinata",-10) from _call_changeRespect_202
                            "[hin_name] turned around and slapped you in the face!" with vpunch
                            hin"[bo_name_stutter]! W-why would you do that!" with vpunch
                            bo"What do you mean [hin_rel_stutter], I was just m-massaging-"
                            hin"Enough! I won't hear any more of it! I am your [hin_rel_mother], you idiot! You cannot t-touch me like that..." with vpunch
                            jump hinatasquatmad
                        "{color=[obediencecolor]}Wait for her reply...{/color}":
                            bo"..."
                            hin"I think..."
                            hin"We should stop here for today. But..."
                            hin"I had fun, and you've been... respectful, for the most part..."
                            bo"For the most part?"
                            hin"Just now you..."
                            call changeObedience("Hinata",1) from _call_changeObedience_122
                            hin"...N-nevermind!" with vpunch
                            hin"We can pick up where we left off some other time, okay?"
                            bot"She must have realized I touched her down there, but she let it pass I think!"
                            bot"Maybe I can keep reaching bit by bit..."
                            bo"Alright then..."
                            jump endhinata_exercisessesion
                        





                "End the session...":
                    jump endhinata_exercisessesion
                


            $ backstretchmenu1_counter += 1
            jump backstretchmenu1
        "{color=[obediencecolor]}Move to her posterior{/color}" if backstretchmenu1_counter>=2: #posterior
            hide screen parallaxcentered
            show screen parallaxcentered("backstretch0_1b",1,1.0,True,[0.7, 1.2])
            with dissolve
            bo"There's one last spot we haven't covered [hin_rel]..."
            hin"[bo_name]... Some things shouldn't need to be said. You know that, right?"
            menu:
                hin"[bo_name]... Some things shouldn't need to be said. You know that, right?"
                "{color=[hatredcolor]}Grope her ass!{/color}":
                    bot"Fuck it! I don't care anymore..."
                    bot"I just have to feel that ass of hers, even if it's just this one time!" with vpunch
                    $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                    hide screen parallaxcentered
                    show screen parallaxcentered("hinata_stretcass_groperepeat",1,1.0,False)
                    with dissolve
                    
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                    bo"I think your ass could use a massage too [hin_rel]!"
                    hide screen parallaxcentered
                    scene black
                    hin"Gasp!" with vpunch
                    $ renpy.sound.play("/audio/soun_fx/spank4.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                    call changeRespect("Hinata",-10) from _call_changeRespect_203
                    "[hin_name] slapped you in the face!" with vpunch
                    hin"[bo_name_stutter]! W-why would you do that!" with vpunch
                    bo"[hin_rel_stutter] it was just... stretchin-"
                    hin"Enough! I won't hear any more of it! I am your [hin_rel_mother], you idiot! You cannot t-touch me like that..." with vpunch
                    jump hinatasquatmad

                    
                    
                "Are you sure...?":
                    hide screen parallaxcentered
                    show screen parallaxcentered("backstretch1",1,1.0,False)
                    with dissolve
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp3.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                    hin"*Gasp*"
                    bo"Are you sure...?"
                    hint"T-the nerve on this kid! Why does [bo_name] ever think I'd want something like this from him!"
                    hide screen parallaxcentered
                    show screen parallaxcentered("backstretch00",1,0.0,False)
                    with dissolve
                    "She looks back at you with a menacing look..."
                    call changeRespect("Hinata",-1) from _call_changeRespect_204
                    hin"Absolutely not [bo_name]!" with vpunch
                    bo"Okay! You don't have to be mad... I was only thinking about your own well-being!"
                    hin"Sure you were..."
                    hide screen parallaxcentered
                    jump hinatasquatmad

            jump hinatasquatmad
        "End the session" if backstretchmenu1_counter>=2:
            jump endhinata_exercisessesion
    #backstretch000_1
label endhinata_exercisessesion:
    hide screen parallaxcentered
    show screen parallaxcentered("backstretch00a",1,1.0,False)
    with dissolve
    bot"That should do it..."
    hin"What a relief..."
    hin"That was pretty g-good, I gotta give it you..."
    hin"Although I am not sure how we went from stretching tips, to a full massage..."
    bo"The two are correlated [hin_rel]..."
    hide screen parallaxcentered
    show screen parallaxcentered("hinata_exhausted",1,1.0,False)
    with dissolve
    call changeObedience("Hinata",1) from _call_changeObedience_123
    hin"I am not complaining! But it was certainly a lot..."
    hin"I feel better, m-more relaxed..."
    hin"T-thank you [bo_name]..."
    bo"Any time! Let me know if I can help some other time, okay?"
    hin"Will do..."
    hide screen parallaxcentered
    scene black
    with dissolve
    bot"..."
    call increaselust(10) from _call_increaselust_189
    bot"I've never got this close to [hin_rel]'s body before..."
    bot"That was fucking incredible!"
    bot"I get this feeling that this might have been the start of something more..."
    $ renpy.end_replay()
    hide screen parallaxcentered
    with dissolve


    $ hinata_stretch_1sttime = True


    jump action_taken