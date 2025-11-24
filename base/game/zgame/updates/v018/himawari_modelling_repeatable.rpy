default hima_model_repeat_count = 0

label himawari_modelling_session_repeatable:
    $ hima_model_repeat_count += 1
    show boruto snob with dissolve
    bo"Ready for another modelling session?"
    show hima thinking with dissolve
    "[him_name] appeared lost in her thoughts for a moment..."
    show hima smugshy with dissolve
    if quest.exists("bohim_2"):
        if quest.is_state("3_bohim_2", "pending") or quest.is_state("2_bohim_2", "in progress") or quest.is_state("2_bohim_2", "pending") :
            $ quest.change_quest_title("2_bohim_2",f"Convince {him_name} to work with you")
            $ quest.change_quest_title("3_bohim_2",f"Purchase a camera and convince Yoru to help you")
            $ quest.change_quest_title("4_bohim_2",f"Have your first session with {him_name}")
            $ notification (f"Quest objective completed")
            $ quest.check("2_bohim_2", "completed")
            $ quest.check("3_bohim_2", "completed")
    him"Uhm, why not, I suppose..." with vpunch
    show boruto surprised2 with dissolve
    bot"Oh, Not even a little protest?"
    him"I g-guess we can play your silly game once more..."
    show boruto snob with dissolve
    bo"So, meet you at my studio?"
    show hima worried2 with dissolve
    show hima at smallshake
    him"I'll be there soon. Just h-have to get changed first..."
    show boruto:
        easeout 2 xpos -1000
    bo"Didn't even have to ask you to put on your sporty outfit! Good girl, you are learning quick!"
    show hima embarassed with dissolve
    him"S-shut up!"
    bo"See you soon!"
    show hima mad3 with dissolve
    him"F-freaking idiot..."
    show hima at smallshake
    him"Hmph!"
    scene black with dissolve
    him"I am not backing down now!"
    "..."
    show bg modelling with dissolve
    show boruto snob at left with dissolve
    bot"I wonder if I'll be able to push her to do anything frisky today!"
    show opinion2_himt beh at right:
        zoom 0.7 xpos 2000
    show opinion2_himt beh:
        easein 1 xpos 800
    him"I am still... n-not used to this, you know."
    bo"Don't worry! You'll get there with time..."
    show opinion2_himt with dissolve
    him"I suppose..."
    hide boruto with dissolve
    bo"Let me just..."
    scene black with dissolve
    bo"Get my equipment ready. You sit there looking pretty, okay?"
    bot"My trusty camera, today I'll put you to good use! Hehe..."
    $ himawari_photoshoot_totalshots = 0
    label himawari_repeatable_menu_photo:
    $ initialize_replay_defaults()
    default himawari_photoshoot_totalshots = 0
    

    if himawari_photoshoot_totalshots >=3:
        hide screen camera_ui
        hide screen camera1280
        scene black
        with dissolve
        jump himawari_photoshoot_ending_repeatable
    else:
        pass
    hide screen camera_ui
    hide screen camera1280
    scene hima_model_normal:
        yalign 1.0
    with dissolve

    show hima_model_normal:
        easein 2 yalign 0.1
    him"S-so? What next..."
    menu himawari_repeatable_photo_menu:
        him "S-so? What next..."
        "Simple shots":
            $ himawari_photoshoot_totalshots += 1
            jump himawari_simple_shots_label
            
                
        "{color=[obediencecolor]}Atheletic Shots{/color}" if himawari_obedience >= 25:
            $ himawari_photoshoot_totalshots += 1
            default himawari_atheltic_shots_firsttime = False
            if himawari_atheltic_shots_firsttime == False:
                $ himawari_atheltic_shots_firsttime = True
                bo"I was thinking, we could do some athletic shots next..."
                him"A-athletic shots?"
                bo"Don't worry. It'll be fun!"
                bo"Besides, this is your forte, isn't it?"
                him"Alright then..."
                jump himawari_athletic_shots_label
            else:
                jump himawari_athletic_shots_label

        "{color=[obediencecolor]}Sexy Shots!{/color}" if himawari_obedience >= 35: # (supporter_scene = True)
            default himawari_sexy_shots_firsttime = False
            if himawari_sexy_shots_firsttime == False:
                $ himawari_sexy_shots_firsttime = True
                bot"I want to see her doing... s-sexy stuff!"
                bot"But I can't just say that so..."
                bo"I think you are ready for some truly aesthetic photos..."
                him"What does that even mean..."
                bo"It's when one is in trance with their body... When you can elicit some sort of emotion, by just posing!"
                him"S-sounds... interesting!"
                bo"Let's give it a try then, shall we?"
                him"Okay..."
                jump himawari_sexy_shots_label
                # $ call_label_action("himawari_sexy_shots_label")
                call supp_rew from _call_supp_rew
                jump himawari_repeatable_photo_menu
                
            else:
                $ himawari_photoshoot_totalshots += 1
                jump himawari_sexy_shots_label
                # $ call_label_action("himawari_sexy_shots_label")
                call supp_rew from _call_supp_rew_1
                jump himawari_repeatable_photo_menu

        "{color=[obediencecolor]}Think you can take off your socks?{/color}" if himawari_obedience >= 27 and himawari_photoshoot_socks_on == True:
            default himawari_photoshoot_socks_on = True
            $ himawari_photoshoot_socks_on = False
            default himawati_takesocks_off_firsttime = False
            if himawati_takesocks_off_firsttime == False:
                him"W-what? Do I really have to take my socks off?" with vpunch
                bo"Mhm..."
                him"Why!?" with vpunch
                bo"Because I said so? And because it'll make for some great shots..."
                bo"Come on, trust me on this one..."
                scene black with dissolve
                him"..."
                show himamodel socks_off with dissolve:
                    xalign 0.5 yalign 1.0 
                show himamodel:
                    easein 5 yalign 0.0
                call changeObedience("Himawari",1,"socksoff") from _call_changeObedience_124
                him"This is w-weird. You don't have to stare at me like that!"
                bo"I am just observing my subject, will you relax?"
                show himamodel:
                    easein 3 yalign 1.0
                him"W-whatever..."
                jump himawari_repeatable_menu_photo
            else:
                him"T-this again...?"
                bo"Come on, it'll make for some great shots! Trust me on this one..."
                show himamodel socks_off with dissolve:
                    xalign 0.5 yalign 1.0
                show himamodel:
                    easein 5 yalign 0.0
                him"Don't s-stare!"
                bo"I am not..."
                show himamodel:
                    easein 3 yalign 1.0
                bot"I totally am!"
                jump himawari_repeatable_menu_photo
        "{color=[obediencecolor]}Put your socks back on...{/color}" if himawari_obedience >= 27 and himawari_photoshoot_socks_on == False:
            $ himawari_photoshoot_socks_on = True
            bo"Can you put your socks back on?"
            scene black with dissolve
            him"Gladly..."
            show himamodel socks_on with dissolve:
                xalign 0.5 yalign 1.0
            show himamodel:
                easein 5 yalign 0.0
            him"That felt a bit w-weird anyway..."
            jump himawari_repeatable_menu_photo





            

        "{color=[obediencecolor]}???{/color}" if himawari_obedience < 25:
            "Increase [him_name]'s obedience to unlock..."
            jump himawari_repeatable_photo_menu
        "{color=[obediencecolor]}???{/color}" if himawari_obedience < 35:
            "Increase [him_name]'s obedience to unlock..."
            jump himawari_repeatable_photo_menu
        


label himawari_simple_shots_label:
    bo"Let's start with something simple..."
    menu himawari_simple_shots:
        bo"Let's start with something simple..."
        "A rear full shot":
            bo"Let's try something you are familiar with..."
            show screen camera1280("hima_model_normal",1,0.0) 
            show screen camera_ui("Himawari",False) 
            with dissolve 
            bo"I'll just take a couple steps back, and you sit there looking pretty..."
            bo"Think you can do that?"
            him"Easy enough..."
            show screen camera1280("hima_model_start",1,0.0) with dissolve
            bot"She certainly built some cake on her with all that exercising of hers..."
            bo"Ready... and..."
            show screen camera_ui("Himawari")
            with dissolve
            $ ui.interact()
            show screen camera_ui("Himawari",False) with dissolve
            bo"Not bad!"
            him"Right..."
            jump himawari_repeatable_menu_photo
        "That beautiful pose of yours...":
            bo"Remember that beautiful pose you pulled off the other day?"
            him"I do..."
            bo"Wanna try that once more? You looked sublime last time..."
            him"T-thanks, I guess..."
            call changeRespect("Himawari",1) from _call_changeRespect_205
            him"Here goes..."
            show screen camera1280("hima_model_normal bestshot",1,0.0) #Nescessary line for all shots (Replace variable with placeholder)
            show screen camera_ui("Himawari",False) #Nescessary line for all shots
            with dissolve #Nescessary line for all shots
            bo"And..."
            show screen camera_ui("Himawari") #Nescessary line for all shots
            with dissolve #Nescessary line for all shots
            $ ui.interact() #Nescessary line for all shots
            him"Did you get it this time? *Giggles*"
            bo"I think you might truly have a natural inclination for this, [him_name]..."
            him"M-moving on..."
            jump himawari_repeatable_menu_photo #Always jump to this label after the shot is done
        
        "Stay as you are...":
            bo"You look great as is, [him_name]..."
            bo"Stand still and try to look natural!"
            show screen camera1280("hima_model_normal",1,0.0)
            show screen camera_ui("Himawari",False)
            with dissolve
            bo"And..."
            show screen camera_ui("Himawari")
            with dissolve
            $ ui.interact()
            him"I feel like that one sucked..."
            bo"Don't say that. You'll do better on this next one!"
            jump himawari_repeatable_menu_photo


label himawari_athletic_shots_label:
    bo"How about you try a..."
    menu himawari_athletic_shots:
        bo"How about you try a..."
        "Hamstring stretch":
            bo "Let's see that hamstring stretch you like to boast about! Show off those years of leg training..."
            him "Fine, but don't get weird about it..."
            show screen camera1280("hima_model_athlestretch2_1", 1, 1.0)
            show screen camera_ui("Himawari", False)
            with dissolve
            bo "Stretch those legs out, nice and slow..."
            him"S-shut up, dummy..."
            bot"F-fuck me..."
            "Her thighs flex, you can't help but stare a little..."
            bo "And..."
            show screen camera_ui("Himawari")
            with dissolve
            $ ui.interact()
            bo "Damn, those workouts are paying off—tight in all the right places."
            him "Ugh, just take the shot already!"
            bo"Way ahead of you!"
            jump himawari_repeatable_menu_photo
        "Knock-down Pose":
            bo "How about you try pretending that you've just been knocked down, but..."
            him"W-what kind of sick scenario is that..."
            bo"Hold on! You aren't going down with out a fight! You rise to your knees and look back at me with a fierce look..."
            bo"Think you can do that?"
            him "This better be quick..."
            show screen camera1280("hima_model_athletic knocked", 1, 0.0)
            show screen camera_ui("Himawari", False)
            with dissolve
            bo "Perfect—spread those legs a little more..."
            "She glares but complies, her shorts riding up slightly."
            "She tries to hide her backside with her hand, but there's not much hidden anyway..."
            bo "And..."
            show screen camera_ui("Himawari")
            with dissolve
            $ ui.interact()
            bo "Hot damn, that's a knockout shot."
            him "Can you just... n-not talk? Like, at all...?"
            jump himawari_repeatable_menu_photo

        "Hamstring stretch on floor (Socks on)" if himawari_photoshoot_socks_on == True:
            bo "Lie down for a hamstring stretch, let's see how flexible you really are."
            him"Do w-what now?"
            bo"Just lay on your back for a moment, you can use the wall behind you for support..."
            him "This is for Mom's s-sake..."
            show screen camera1280("hima_model_athletic stretch1", 1, 0.0)
            show screen camera_ui("Himawari", False)
            with dissolve
            bo "Pull that leg up high,nice and tight..."
            "Her shorts strain as she stretches, and you zoom in shamelessly."
            bo "And..."
            show screen camera_ui("Himawari")
            with dissolve
            $ ui.interact()
            bot "Fuck! Now that's a view—those legs of her could crush me..."
            him "A-are you done? This ain't easy you know..."
            bo"Y-yeah..."
            jump himawari_repeatable_menu_photo

        "{color=[hatredcolor]}Try to take creepshots...{/color}":
            bo"Can you come over here for a second...?"
            him"H-huh? What for..."
            hide screen camera1280
            hide screen camera_ui
            scene black with dissolve
            bot"Hope this works..."
            show screen camera1280("hima_model_athletic creepshot", 1, 0.0)
            show screen camera_ui("Himawari", False)
            with dissolve
            him "What are you s-staring at..." with vpunch
            show screen camera_ui("Himawari")
            with dissolve
            $ ui.interact()
            "You hold the camera low, snapping sneaky shots of her stomach and chest."
            bot "Hehe! She'll never know anyway..."
            show screen camera_ui("Himawari")
            with dissolve
            $ ui.interact()
            bo"N-nevermind, I think I changed my mind, you can turn around..."
            call changeRespect("Himawari",-1) from _call_changeRespect_206
            him"W-why you... What the hell is this for!"
            hide screen camera1280
            hide screen camera_ui
            scene black with dissolve
            "As she angrily turns around, you trail slightly with the camera..."
            show screen camera1280("hima_model_athletic creepshot2", 1, 0.0)
            show screen camera_ui("Himawari", False)
            with dissolve
            bot"This is for snapping some pictures of your juice ass, bitch!"
            hide screen camera_ui
            show screen camera_ui("Himawari")
            with dissolve
            $ ui.interact()

            bot "Gotcha! Those curves of yours look even better up close."
            show screen camera1280("hima_model_normal back", 1, 0.0) with vpunch
            him "A-are we done here?"
            jump himawari_repeatable_menu_photo


        "Stretching pose (Barefoot)" if himawari_photoshoot_socks_on == False:
            bo "Now that you are barefoot, let's do something fun..."
            him "Fun for w-who exactly..."
            bo"It's no big deal, trust me!"
            bo"Just lay on your back for a moment and raise one of your legs... Easy, right?"
            show screen camera1280("hima_model_athlefeet", 1, 0.0)
            show screen camera_ui("Himawari", False)
            with dissolve
            bo "Higher, show off your well toned legs..."
            "Her bare soles flex, and you linger on the shot."
            him"T-this is weird..."
            bo "And..."
            show screen camera_ui("Himawari")
            with dissolve
            $ ui.interact()
            bot "Sexy as hell!"
            him "Gross... Next!"
            jump himawari_repeatable_menu_photo
        "Stretching pose (Socks on)" if himawari_photoshoot_socks_on == True:
            bo "With your nice little socks on, I want you to..."
            
            bo"Just lay on your back for a moment... Easy, right?"
            show screen camera1280("hima_model_athlesockstretch1", 1, 0.0)
            with dissolve
            him"Sure is..."
            menu:
                him"Sure is..."
                "Now raise one of your legs up...":
                    bo"And now, try raising one of your legs up..."
                    him"Can't just be simple, right?"
                    show screen camera1280("hima_model_athlesockstretch2", 1, 0.0) with dissolve
                    bo "Push it—let those socks hug your feet nice and tight..."
                    him"J-just.... shut up already!"

                    show screen camera_ui("Himawari")
                    with dissolve
                    $ ui.interact()
                    bo "Perfect! Those socks make your legs pop!"
                    him "I hope I never have to do that again!"
                    jump himawari_repeatable_menu_photo
                    
                "Stay as you are...":
                    pass
                
            bo "You look great as your are, a bit candid even..."
            show screen camera_ui("Himawari", False) with dissolve
            him"J-just.... shut up already!"
            bo "Ready, And..."
            show screen camera_ui("Himawari")
            with dissolve
            $ ui.interact()
            bo "Perfect—those socks make your legs pop!"
            him "I hope I never have to do that again!"
            jump himawari_repeatable_menu_photo








label himawari_photoshoot_ending_repeatable:
    him"I think I am done..."
    bo"Come on, right about when it started to get fun..."
    show hima_photoshoot end1 with dissolve
    him"Fun? Only for you..."
    $ renpy.end_replay()
    if quest.is_state("4_bohim_2", "in progress"):
        $ quest.check("4_bohim_2", "completed")
        $ quest.check("bohim_2", "completed")
        $ notification (f"Objective Completed: Have your first session with {him_name}")
    call increaselust(5) from _call_increaselust_190
    bot"S-she doesn't seem to mind my hand on her waist..."
    him"Have you even made any money from my photos yet...?"
    menu:
        him"Have you even made any money from my photos yet...?"
        "Not yet...":
            bo"Not yet, but I am working on it..."
            call changeRespect("Himawari", -1) from _call_changeRespect_207
            him"So what, I've been doing this with you for nothing?"
            bo"As I said, I am working on it [him_name]..."
            scene black with vpunch
            him"Then you better start working faster!" with vpunch
            "[him_name] storms off, annoyed at the fact that you have yet to show her the fruits of her labors..."
            jump action_taken

        "Give her $20" if money >=20:
            call changeMoney(-20) from _call_changeMoney_15
            bo"Here, this is for your hard work..."
            scene black with vpunch
            him"N-nice... Thank you!"
            show hima_photoshoot end0_5 with dissolve
            call changeObedience("Himawari", 1) from _call_changeObedience_125
            him"This wasn't such a  bad idea after all..."
            scene black with dissolve
            him"Maybe we can work together again soon? I like this getting paid part! Teehee!" with vpunch
            "[him_name] storms off with her hard earned $20..."
            jump action_taken
        "Give her $50" if money >=50:
            call changeMoney(-50) from _call_changeMoney_16
            bo"Here, this is for your hard work..."
            scene black with vpunch
            him"F-fifty!? That's insane... Thank you!" with vpunch
            show hima_photoshoot end0_5 with dissolve
            call changeObedience("Himawari", 3) from _call_changeObedience_126
            him"If this is what this job pays then maybe..."
            call increaselust(5) from _call_increaselust_191
            bot"She is leaning all over me..."
            scene black with vpunch
            him"Maybe we can work together again soon? I like this getting paid part! A lot! Teehee!" with vpunch
            "[him_name] storms off with her hard earned $50..."
            jump action_taken

        
