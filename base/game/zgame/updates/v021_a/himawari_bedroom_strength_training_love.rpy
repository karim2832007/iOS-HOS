# Love variant
default first_time_hima_peek = True # Flag used to display one-time warning about impulse choices

label hima_strength_training_check_love:
    if (himawari_obedience < 20 and himawari_obedience_level==1):
        "Her pride is still a little too high. She's not ready to accept your help with training just yet."
        "Increase her obedience to 20 before suggesting this."
        jump himastretchingmenu
    
    elif himawari_respect < 0:
        show hima mad3 with vpunch
        him "Get out. I'm not in the mood for you."
        call checkRespect(0, "Himawari") from _call_checkRespect_12
        bot "She's still upset. I should give her some space."
        "She's too angry to even consider training with you right now."
        jump action_taken
    
    # This whole block will only play out once. All future repeats, you go straight into the competition intro.
    elif not hima_agreed_squat_competition:
        bo "Hey, I saw you training earlier. Your form's a little... stiff."
        show hima mad
        show boruto surprised
        with dissolve
        him "What are you talking about? My form is perfect! I'm getting ready for the Chunin Exams."
        bo "I know, but you're too rigid. I'm worried you're going to pull something training like that."
        show hima smug2 with dissolve
        him "And I suppose you're the grand master of taijutsu now?"
        show boruto embarassed with dissolve
        bo "I just... I've been training a lot. I might know a thing or two. I want to help you."
        him "Help me? You? That's hilarious."
        show boruto normal with dissolve
        bo "I want to see you succeed, [him_name]. For real. Let me help you, as your [him_rel_to_bo]."
        show hima smug3 with dissolve
        him "Why should I listen to a slacker like you?"
        show boruto laughing with dissolve
        bo "Because I can prove I know what I'm talking about. How about I show you?"
        him "I'm sure this will be good..."
        bo "A simple competition. Me versus you. Good old healthy sibling rivalry."
        him "Hahaha! Yeah right. Why would I waste my time competing against you?"
        him "You don't know the first thing about fitness! Look at you!"
        show boruto sad with dissolve
        bo "I'm serious about this! I've been working hard."
        show hima smug with dissolve
        him "Even if you have, I'd still wipe the floor with you. At any competition."
        show boruto smirk with dissolve
        bo "Are you so sure? How about we make it interesting?"
        show hima surprised with dissolve
        him "Interesting how?"
        bot "Okay, I've got her attention. Time to reel her in."
        bo "You beat me in a squat competition, you get $100. My treat."
        show hima smug3 with dissolve
        him "Ha! Easiest money I'll ever make! You're on!"
        bo "But there's a condition."
        him "I knew it..."
        bo "If I win..."
        him "Yeah, yeah, what do you want? Not that it's going to happen."
        bot "We'll see about that."
        bo "If I win... you have to take my training advice seriously."
        him "Your 'coaching'? Seriously?"
        bo "I just want you to be safe and do your best. That's all."
        him "Fine. But we do this my way. In my room. Starting tomorrow."
        him "And if you get weird about it, I'll kick you so hard you'll be tasting your own tonsils."
        bo "Deal. Be ready."
        him "I will be! I can't wait to take your money!"
        bot "She's so fired up. This is going to be fun. I just hope I can actually win..."
        $ hima_agreed_squat_competition = True
        "You've challenged [him_name] to a friendly competition. Return to her room later to begin."
        jump action_taken
    else:
        label hima_agreed_squat_competition_love:
        # --- Convincing her to change. This first variation will only be asked once. Otherwise it goes to the "reasking" variation. ---

        if not hima_in_buruma:
            if not hima_buruma_already_asked:
                show boruto smirk with dissolve
                bo "So, ready for our little competition?"
                show hima smug with dissolve
                him "Ready to take your money, you mean? Let's get this over with."
                bo "Hold on. You're not seriously going to train in that, are you?"
                show hima mad with dissolve
                him "What's wrong with what I'm wearing? Are you trying to find an excuse to back out?"
                show boruto sad with dissolve
                bot "I can't let her train like this. She could get hurt, or overheat. I need to convince her."
                bo "You'll rip something. Or get heatstroke. If you're going to take this seriously, you need to dress for it. Proper workout clothes."
                him "Ugh, you're so annoying! Always such a worrywart!"
                show hima smugshy with dissolve
                himt "Maybe he really does care about my safety..."
                show boruto normal with dissolve
                if tsunade_discovery_seen == True:
                    bot "She's complaining, but she's actually listening to me. Is this what Tsunade meant about my semen's qualities? This weird connection between us... if it helps her stay safe, maybe it's a good thing."
                else:
                    bot "She's complaining, but her anger is fading. She's actually considering it. Progress!"
                $ hima_buruma_already_asked = True
            # Second time player attempts to ask her to change into buruma, slight variation.
            else:
                bo "So, are you ready to start squatting or...?"
                him "Are you going to bring up my clothes again? I get it, you're worried."
                bo "I just want you to be careful. I already explained why it's important."
                show boruto angry with dissolve
                bot "Come on, please just listen to me on this one..."
                
        menu hima_ask_burama_love:
            # For those who get here before collecting the necessary lvl 2 obedience points from other advancement events (fail-retry state if statcheck fails).
            "{color=[obediencecolor]}Insist she wears the proper gear.{/color}":
                call checkObedience(statvalue=2, statlevel=2, jumpvalue="hima_change_failure_love", character="Himawari") from _call_checkObedience_42
                show hima shy with dissolve
                himt "Why do I always end up listening to him? Ugh..."
                him "F-fine! I'll change! But don't you dare peek, you perv! I'm still going to crush you!"
                him "I'll let you know when I'm ready."
                bo "Okay, okay! Sheesh, why would I peek on my own [him_rel]? I'll wait out here."
                hide hima with easeoutright
                scene black with dissolve
                $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx2", loop=False, relative_volume = 0.9)
                "She ushers you out and proceeds to change."
                $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 0.9)
                menu:
                    "You decide to:"
                    "Wait outside.":
                        call changeRespect("Himawari", amount=3) from _call_changeRespect_249
                        bot "I should respect her privacy. Besides, winning this fairly will feel much better."
                        bot".."
                        bot"..."
                        bo "[him_name], are you done yet?"
                        him "Come in."
                    "{color=[impulsecolor]}Peek!{/color}":
                        if first_time_hima_peek:
                            "Although you've learned to control it, your curse still lingers."
                            "At times, you may succumb to your {color=[impulsecolor]}Impulse{/color}, but be careful..."
                            "Letting the curse uncontrollably feast upon your impulses may lead to catastrophic outcomes."
                            "If your impulses grow too strong, visit Kushina in your dreams. She will know how to assist you."
                            $ first_time_hima_peek = False
                        call changeHatred(amount=1) from _call_changeHatred_210
                        bot "I shouldn't... but... just a quick look couldn't hurt, right?"
                        bot "Juuuust a tiny peek... maybe I'll get lucky and..."
                        show screen peeking12801024("hima_changing_buruma") with flash
                        bot "...wow. She's... really beautiful."
                        bot "Okay, that was a mistake. Now I can't think straight."
                        bot "Her figure is... perfect." with vpunch
                        bot "Focus, [bo_name]! Focus on the competition!"
                        scene black with dissolve
                        hide screen peeking12801024 with dissolve
                        scene black with dissolve
                        him "Come in."
                        bo "C-coming!"

                $ hima_in_buruma = True
                jump hima_squat_minigame_start_love

label hima_change_failure_love:
    # Fail condition
    show hima mad3 with vpunch
    him "I'm not changing! I'll beat you in my pajamas if I have to! Now let's do this or get out!"
    call changeRespect("Himawari", -2) from _call_changeRespect_250
    show boruto sad with dissolve
    bot "Tch. She's so stubborn."
    bot "She refuses to change. I'll just have to hope she doesn't hurt herself. Maybe if she trusted me a bit more..."
    jump action_taken


# --- The Squat Minigame ---
label hima_squat_minigame_start_love:
    $ first_exercise_hima = True

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
    else:
        $ playmusic("audio/ost/reversesituation.opus",0.6)

    if hima_competition_full_clear:
        menu competition_full_clear_love:
            "Skip the squatting competition?"
            "Yes, and bring me my Doritos.":
                dev"Doritos are not available for delivery yet."
                dev"Visit www.houseofshinobi.com to see our store."
                jump hima_training_proper_start_love_repeatable
            "I don't skip leg day.":
                pass
    # First time entry
    if hima_first_time_competition:
        if day_part == 3: 
            scene himawari_bedroom_2
        else:
            scene himawari_bedroom_1
        show gymhima shy at center with easeinleft
        him "Happy now? I feel ridiculous."
        show boruto laughing at left with dissolve
        bot "Wow. She looks amazing. Okay, don't get distracted."
        bo "You look like you're taking this seriously now. Good."
        bot "She looks determined... Maybe I've underestimated her."
        show gymhima smug with dissolve
        him "Alright, let's do this. First one to quit or fail loses. And you owe me $100."
        bo "And if I win, you have to accept my coaching, no arguments."
        him "Hah! In your dreams."
        show boruto normal with dissolve
        bot "I hope I can pull this off."
        $ hima_first_time_competition = False

    # Lost last time
    elif not hima_first_time_competition and hima_competition_last_win == False:
        if day_part == 3: 
            scene himawari_bedroom_2
        else:
            scene himawari_bedroom_1
        show gymhima smug at right with dissolve
        him "Came back for a rematch? I didn't know you liked losing so much."
        show boruto smirk at left with dissolve
        bot "She's so cocky... And here I thought letting her win was a good idea."
        bo "Don't get ahead of yourself just because I went easy on you, [him_name]."
        bo "This time, I'm not holding back."
        him "You talk a good game, but we both know I'm the more athletic one!"
        bot "We'll see about that..."
        bo "Less talking, more squatting."

    # Won last time
    elif not hima_first_time_competition and hima_competition_last_win:
        if day_part == 3: 
            scene himawari_bedroom_2
        else:
            scene himawari_bedroom_1
        show gymhima smug at right with easeinleft        
        him "You really wanna give me another shot at your money, huh?"
        show boruto smirk at left with dissolve
        bo "Uhh... Are you forgetting who won last time?"
        show gymhima smug at right with dissolve
        him "Luck. Pure luck."
        bot "She'll never admit I'm stronger. That's kinda cute."
        bo "You call that luck? I call it skill."
        him "Ha! You got lucky, that's all! Slacker!"
        bo "Yeah, okay, enough trash talk. Let's do this."
        him "Don't order me around!"
        bot "Heh. She's so competitive."
        bo "Ready?"

    menu:
        "Move behind her.":
            $ himawari_squat_minigame_frombehind = True
            show boruto normal with dissolve
            bot "If I stand behind her, I can catch her if her knees give out mid-exercise."
            bot "She does tend to push herself too hard..."
        "Stay in front.":
            $ himawari_squat_minigame_frombehind = False
            pass

    $ renpy.sound.play("/audio/soun_fx/countdown.opus", channel="sfx2", loop=False, relative_volume = 0.9)
    scene black
    if himawari_squat_minigame_frombehind == True:
        show himawari_squatbehindup:
            xysize (1280, 720)
            fit "contain"
            xalign 0.5
            yalign 0.5
        show halfblack
        with dissolve
        show screen scrollingtext("Get ready to tap as fast as you can!")
        hide halfblack with Dissolve(3)
        $ pushups, ended_by_stamina, wonsquats = renpy.call_screen("strength_minigame_himawari", "himawari_squats_behind")
    else:
        show himawari_squatup:
            xysize (1280, 720)
            fit "contain"
            xalign 0.5
            yalign 0.5
        show halfblack
        with dissolve
        show screen scrollingtext("Get ready to tap as fast as you can!")
        hide halfblack with Dissolve(3)
        $ pushups, ended_by_stamina, wonsquats = renpy.call_screen("strength_minigame_himawari", "himawari_squats_front")

    if wonsquats:
        # Player wins
        $ neverwonhima = False
        $ hima_competition_last_win = True
        scene black with dissolve
        bo "Whew! That was a good... warmup!"
        scene hima_squat_win_cg with dissolve:
            xalign 0.5 yalign 1
        show hima_squat_win_cg:
            subpixel True
            easein 3 yalign 0.5
        him "*Pant... pant...* H-How...? No way..."
        "You completed [pushups] squats and won the competition!"
        bot "She really gave it her all. I'm impressed."
        bo "What's wrong, [him_name]? Out of breath? I told you I've been training."
        bo "A deal's a deal. Now you have to let me help you. Properly. It's my responsibility as your [him_rel_to_bo]."
        him "I... *pant*... I can't believe it..."
        bo "Hey, you did great. Don't be too hard on yourself. Now we can work together to get you even stronger. Let's start with your first real lesson."
        himt "How could I lose... to him! He's actually gotten so much stronger..." with vpunch
        scene black with dissolve
        "She is visibly shaken, but also a little impressed, as she realizes you might actually know what you're doing."
        if hima_competition_full_clear:
            jump hima_training_proper_start_love_repeatable
        else:
            jump hima_training_proper_start_love
    else:
        # Player loses
        $ hima_competition_last_win = False
        scene black with dissolve
        scene hima_squat_lose_cg with dissolve:
            xalign 0.5 yalign 0.0
        show hima_squat_lose_cg:
            subpixel True
            easein 3 yalign 0.5
        him "Ha! See? All talk! I knew you couldn't keep up."
        menu hima_squat_competition_fail_love:
            "You failed to beat her. She looks pretty proud of herself."
            "Pay her $100 as promised." if money >= 100:
                call changeMoney(-100) from _call_changeMoney_24
                bo "Alright, alright, you win. Here."
                "You hand over the $100."
                call changeRespect("Himawari", 2) from _call_changeRespect_251
                him "Heh. Pleasure doing business with you. Now if you'll excuse me, I have some real training to do."
                bot "She's so happy she won. It was worth it just to see her smile... even if she's gloating."
                jump action_taken
            "Admit you're broke and promise to make it up to her.":
                bo "[him_name], I know you'll think I'm making excuses, but I promise, as soon as I get paid from my next shift at Obo's I'll repay you."
                call changeRespect("Himawari", -3) from _call_changeRespect_252
                scene hima_squat_lose_cg_mad with dissolve:
                    xalign 0.5 yalign 0.5
                show hima_squat_lose_cg_mad:
                    subpixel True
                    easein 0.3 zoom 1.2 yalign 0.2
                him "ARE YOU SERIOUS!? You made a bet with me and you don't even have the money!?" with vpunch
                him "You're unbelievable! A liar and a sore loser! Get out of my sight!"
                bot "Damn it... I should have known better than to make a bet I couldn't pay."
                call changeHatred(1, max_times=1, fromwhere="hima_squat_competition_fail_dontpay") from _call_changeHatred_211
                scene black with dissolve
                "She's furious. You lost the bet and couldn't even pay up. You've lost all her respect."
                jump action_taken


label hima_training_proper_start_love:
    $ initialize_replay_defaults()
    scene gymhima_buruma_sweaty_cg with dissolve:
        xalign 0.5 yalign 1
    show gymhima_buruma_sweaty_cg:
        subpixel True
        easein 3 yalign 0.7

    $ playmusic("audio/ost/house2.opus",0.6)
    if first_exercise_hima:
        him "So? What's this 'coaching' all about? Let's get it over with."
        himt "I can't believe I lost... He's so much stronger than before. It's... frustrating. And kind of..."
        bot "I need to be a good coach now and prove I was serious about helping her."
        bo "Alright [him_name], let's see... I think we should start with..."
    else:
        him "Just... don't be weird about it this time."
        bo "Hey, I'm just trying to help. I'm sorry, but sometimes there may need to be some physical contact just to ensure you're okay."
        bo "Haven't I proven I know what I'm doing?"
        him "I-I guess... Just keep the touching to a minimum!"
        bo "I'll only do what's necessary to help you with your form."

    menu hima_training_menu_love:
        # The first training section is available until its milestone flag is set.
        "Hamstring stretches.":
            $ hima_hamstring_repeat_counter = 0
            jump hima_training_hamstrings_love

        # ??? for glute activation (requires hamstring stretch full completion first)
        "{color=[obediencecolor]}???{/color}" if not hima_hamstring_groped:
            bot "I should make sure she gets the hamstring stretches right before we move on to something else."
            jump hima_training_menu_love

        # Unlock if hamstring stretches full completion
        "{color=[obediencecolor]}Glute activation{/color}" if hima_hamstring_groped:
            call checkObedience(statvalue=2, statlevel=2, jumpvalue="none", character="Himawari") from _call_checkObedience_43
            # Fail state if obedience is too low
            if himawari_obedience.level<2 or (himawari_obedience.level == 2 and himawari_obedience.value < 2): 
                bot "She's still not quite comfortable with my help. I need to build more trust..."
                jump hima_training_menu_love
            else:
                jump hima_training_glutes_love

        # ??? for posture correction (requires glute activation full completion first which leads to unavoidable failure)
        "{color=[lovecolor]}???{/color}" (advancement_event=True) if not hima_glute_spanked:
            bot "I should make sure she gets the other exercises right before we move on to more advanced things."
            jump hima_training_menu_love

        # In the Love variant, this is not an aggressive act, but an accidental slip-up that creates an intimate moment.
        "{color=[lovecolor]}Advanced posture correction{/color}" if hima_glute_spanked and dominance.level >= 2:
            call checkLove(character="Himawari", statvalue=11, statlevel=1, jumpvalue="hima_training_menu_love") from _call_checkLove_8
            jump hima_training_posture_love

        "{color=[lovecolor]}Advanced posture correction{/color}" (advancement_event=True) if hima_glute_spanked and dominance.level == 1:
            call checkLove(character="Himawari", statvalue=11, statlevel=1, jumpvalue="hima_training_menu_love") from _call_checkLove_9
            jump hima_training_posture_love

        "That's enough for today.":
            scene black with dissolve
            bo "We're done for now. You did great today. Your training has just begun."
            him "Whatever... just get out."
            bot "I think I'm starting to get through to her. Next time, maybe she'll be even more receptive."
            jump action_taken

# ==============================================================================
# STRETCH 1: HAMSTRINGS
# ==============================================================================

label hima_training_hamstrings_love:
    bo "Hamstring stretches!"
    bo "Let's start simple."
    bo "Sit on the floor. Legs straight. Touch your toes."
    him "Hmph! I know how to do a basic stretch."
    scene black with dissolve
    "She seems a little frustrated by the simple instruction, but she moves to follow your guidance."
    scene hima_hamstring_notstraight_cg with dissolve: 
        xalign 0.5 yalign 1
    show hima_hamstring_notstraight_cg:
        subpixel True
        easein 3 yalign 0.5
    bo "I know it may seem like I'm treating you like a total beginner, but trust me, I'm not."
    bo "I just need to make sure your form is right because the last thing I want is for you to get injured because of me."
    show hima_hamstring_notstraight_cg_surprised with dissolve:
        yalign 0.5
    himt "*gasp* Is he r-really that... concerned about me?"
    scene black with dissolve
    "Flustered by her realization, she attempts the stretch again, her form sloppy and strained, her back rounding immediately."
    scene hima_hamstring_cg with dissolve:
        xalign 0.5 yalign 0.95
    show hima_hamstring_cg:
        subpixel True
        easein 3 yalign 0.7
    bot "Not the best form... But if I'm too harsh, she'll just get defensive."
    bo "Not a bad try..."
    bot "Terrible try actually." 
    bo "But notice how your back is rounded? That's a good way to hurt your back."
    him "I SAID I KNOW WHAT I'M DOING!!" with vpunch
    bot "She's embarrassed I called her out. I need to be gentle but firm."
    bo "Hey, I'm just trying to help. A good coach doesn't let his student use bad form. We're going to fix this, right now."
    himt "Look at him being all overprotective... But he's not wrong about my back."

    menu hima_hamstring_menu_love:
        bot "She wants to prove me wrong, and I can use that to help her improve."

        "Show me again. Slowly." if hima_hamstring_repeat_counter<3:
            if hima_hamstring_repeat_counter == 0:
                bo "Okay, fine. Show me again. But this time, try to keep your back straight."
                him "It IS straight!"
                bo "It's not. Look, just try again. Focus on hinging at your hips."
                scene himawari_bedroom_strength_training_line_347 with dissolve:
                    xalign 0.5 yalign 1
                show himawari_bedroom_strength_training_line_347:
                    subpixel True
                    easein 3 yalign 0.7
                "She attempts the stretch again, with the same flawed result, her frustration mounting."

            elif hima_hamstring_repeat_counter == 1:
                bo "Still rounding. Your pelvis isn't tilting. You're just collapsing your torso. Are you listening?"
                him "Just shut up and let me concentrate!"
                himt "Why can't I do it right!? Why is he watching me so closely!?"
                bo "Try it again."
                scene himawari_bedroom_strength_training_line_354 with dissolve: 
                    xalign 0.5 yalign 1.0
                show himawari_bedroom_strength_training_line_354:
                    subpixel True
                    easein 3 yalign 0.7
                "She attempts the stretch again, with the same flawed result, her frustration mounting."
            elif hima_hamstring_repeat_counter == 2:
                bo "Still not quite right. Again. Maybe it'll be easier if you focus on just one foot first."
                him "[bo_name]! Are you just trying to annoy me!?" with vpunch
                scene himawari_bedroom_strength_training_line_362 with dissolve:
                    xalign 0.5 yalign 1
                show himawari_bedroom_strength_training_line_362:
                    subpixel True
                    easein 3 yalign 0.7
                bo "I'm trying to *teach* you. You're the one fighting me on it. Do it right, and we can move on."
                bot "Pushing her a little. Forcing her to choose between her pride and her desire to learn... This should work."

            $ hima_hamstring_repeat_counter += 1
            if hima_hamstring_repeat_counter >= 2:
                $ hima_guide_physically = True
            jump hima_hamstring_menu_love

        "{color=[dominancecolor]}???{/color}" if not hima_guide_physically:
            bot "She's not frustrated enough to accept my help yet. A few more tries should do it."
            jump hima_hamstring_menu_love

        # Unlocked permanently after "show me again" 2 times.
        "{color=[lovecolor]} Looks like I'll have to guide you.{/color}" if hima_guide_physically:
            call checkLove(character="Himawari", statvalue=10, statlevel=1, jumpvalue="hima_hamstring_menu_love") from _call_checkLove_10
            $ hima_guide_physically = True
            bo "Okay, clearly just telling you isn't working. Your pride is getting in the way." 
            bo "Sometimes a coach has to get hands-on to help a student understand the movement."
            him "Don't you dare use that as an excuse to t-"
            scene black with dissolve
            "Before she can finish her sentence, you move to sit behind her, giving her some space."
            scene hima_hamstring_lookingback_cg with dissolve: 
                xalign 0.5 yalign 1
            show hima_hamstring_lookingback_cg:
                subpixel True
                easein 3 yalign 0.5
            him "W-What are you doing? D-don't get too close."
            bo "I'm your coach. My job is to make sure you have good form, even if it feels a bit weird. But trust me, I want what's best for you. Stay still."
            jump hima_hamstring_correct_form_love

        # ??? for different approach (unlocked when one of the two hamstring kinds of touches is done)
        "{color=[obediencecolor]}???{/color}" if not hima_hamstring_touch_unlocked:
            bot "I should try helping her directly first..."
            jump hima_hamstring_menu_love

        "{color=[obediencecolor]}Let's try a different approach.{/color}" if hima_hamstring_touch_unlocked:
            $ hima_different_approach = True
            bo "Since that's not working, let's try to figure out the root of the problem."
            bot "Framing this as a diagnosis might make her more receptive and less self-conscious."
            him "Assess...? What are you talking about?"
            jump hima_hamstring_assess_flexibility_love

        "Not too bad, let's move on.":
            bo "We'll come back to this. Flexibility is important, and we need to work on it if you want to avoid injury."
            bot "A tactical retreat. I've planted the seed that her form needs work. She'll be thinking about it."
            jump hima_training_menu_love

    # First major branch, focusing on 'correcting' her form.
    label hima_hamstring_correct_form_love:
        bo "I'm going to place my hands on your back to give you a feel for what proper alignment is, okay?"
        scene black with dissolve
        "You gently place your hands on her lower back, thumbs tracing the muscles along her spine."
        scene himawari_bedroom_strength_training_line_227_love with dissolve:
            xalign 0.5 yalign 1
        show himawari_bedroom_strength_training_line_227_love:
            subpixel True
            easein 3 yalign 0.5
        him "I-I'm not tense!"
        bo "You are. Relax."
        himt "Ughh this whole caring [him_rel_to_bo] attitude is just... making me more flustered... Get it together [him_name]!"
        call changeObedience("Himawari", 1, "hima_train_hamstring1", max_times=1, statlevel=2) from _call_changeObedience_152
        $ hima_hamstring_touch_unlocked = True

        menu hima_hamstring_correction_options_love:
            bo "Now... let's fix this."

            "Apply firm, steady pressure." if not hima_applied_pressure:
                $ hima_applied_pressure = True
                bo "I'm going to apply some pressure now. Don't fight it. Let your body sink into the stretch."
                scene black with dissolve
                "You push down firmly but gently, helping her back to straighten. A small gasp escapes her lips as she's pushed deeper than she could go on her own."
                scene himawari_bedroom_strength_training_line_227_v2_love with dissolve:
                    xalign 0.5 yalign 1.0
                show himawari_bedroom_strength_training_line_227_v2_love:
                    subpixel True
                    easein 3 yalign 0.7
                him "*gasp* O-okay... I feel that."
                himt "It hurts... but it's a good hurt. It feels... right. Why does it feel right when he's helping me?"
                bo "That's the feeling of a proper stretch. Remember it. That's what we're aiming for."
                bot "She's associating my touch with a positive result. This is a good step."
                jump hima_hamstring_correction_options_love

            "{color=[lovecolor]}Let's give you a real stretch.{/color}" if not hima_forced_down:
                $ hima_forced_down = True
                call checkLove(character="himawari", statvalue=10, jumpvalue="hima_hamstring_correction_options_love") from _call_checkLove_11
                bo "You're still holding back. I know you're capable of more. Let's give this another try."
                scene black with dissolve
                "With a quick 'Ready?', you push her back down, firmly and smoothly, guiding her much deeper into the stretch than she's prepared for."
                scene himawari_bedroom_strength_training_line_227_v3 with dissolve:
                    xalign 0.5 yalign 1
                show himawari_bedroom_strength_training_line_227_v3:
                    subpixel True
                    easein 3 yalign 0.5
                him "H-hey, warn a girl first!"
                bo "See? You can touch your toes. Your flexibility is better than you think. Now, are you going to trust me, or do we need another demonstration?"
                himt "He... He was right after all!"
                him "I-I..."
                call changeLove(1, max_times=1, fromwhere="hima_hamstring_correction_options_forceherdown") from _call_changeLove_57
                bo "Good. I'm glad we understand each other."
                jump hima_hamstring_correction_options_love

            "Slide your hands down her back." if not hima_slide_hands:
                $ hima_slide_hands = True
                bo "Your entire spine is out of alignment. Let me check."
                scene black with dissolve
                "You slowly slide your hands from her shoulders down the length of her back, feeling the curve of her spine, your fingers brushing against the fabric of her shirt."
                scene himawari_bedroom_strength_training_line_227_v4 with dissolve:
                    xalign 0.5 yalign 1
                show himawari_bedroom_strength_training_line_227_v4:
                    subpixel True
                    easein 3 yalign 0.5
                him "Wh-what are you doing!?"
                bo "Checking for tension knots. You're riddled with them. A sign of chronic poor posture."
                bot "I should've started teaching her about proper form earlier! She could've ended up hurting herself judging by all this."
                him "O-okay... fine. Just... be quick about it."
                jump hima_hamstring_correction_options_love

            "Nevermind." if not hima_slide_hands and not hima_forced_down and not hima_applied_pressure:
                bo "You're not focusing. Are you taking this seriously?"
                jump hima_hamstring_menu_love
            
            "Still not quite right." if hima_slide_hands and hima_forced_down and hima_applied_pressure:
                bo "Better, but still not quite right."
                bo "Looks like we need a different approach."
                jump hima_hamstring_menu_love

    # Second major branch, a more direct assessment.
    label hima_hamstring_assess_flexibility_love:
        bo "The problem might not be your back, but your hamstrings themselves. They might be so tight that they're pulling your pelvis out of alignment, forcing your back to compensate."
        him "You think...?"
        bo "I need to check the muscle tension directly. Hold still."
        scene black with dissolve
        "Knowing she'll keep protesting out of embarrassment if you don't act quickly, you reach out and place a hand on her right calf."
        scene hima_hamstring_flexibility_grab_cg with dissolve:
            xalign 0.5 yalign 0.8
        show hima_hamstring_flexibility_grab_cg:
            subpixel True
            easein 3 yalign 0.5
        him "And what is this supposed to do?"
        bo "This is just diagnostic. I'll show you how much I learned about optimal practice from all the hours I spent training. Trust the process."
        show hima_hamstring_flexibility_grab_cg:
            subpixel True
            easein 0.5 yalign 0.7 zoom 1.2
        "You gently squeeze her calf muscle."
        bo "Hmm. Tense. As I suspected."
        scene black with dissolve
        "You reposition yourself, sliding your hand up slowly, from her calf, over the back of her knee, to the base of her hamstring."
        scene hima_hamstring_flexibility_grab_cg_v2_love with dissolve:
            xalign 0.5 yalign 1.0
        show hima_hamstring_flexibility_grab_cg_v2_love:
            subpixel True
            easein 3 yalign 0.5
        himt "His hand... It's just an 'assessment', right? So why is my heart beating so fast?"
        bo "I think I know what's going on now that I'm getting a better feel for it."

        menu hima_hamstring_grope_menu_love:
            "Your hand rests on her lower thigh. This is a bit awkward."

            "{color=[obediencecolor]}Gently squeeze her thigh to 'test' the muscle.{/color}" if himawari_obedience_level >= 2:
                call checkObedience(statvalue=2, statlevel=2, jumpvalue="_hima_hamstring_grope_fail_love", character="Himawari") from _call_checkObedience_44
                scene black with dissolve
                bo "This is the source of the problem. Right here."
                "Your hand gently but firmly squeezes her mid-thigh, testing the toned muscle."
                scene hima_hamstring_flexibility_grab_cg_v3 with dissolve:
                    xalign 0.5 yalign 1.0
                show hima_hamstring_flexibility_grab_cg_v3:
                    subpixel True
                    easein 3 yalign 0.6
                $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                him "H-Hey!"
                bo "Just as I thought. Tight as a drum. We have a lot of work to do."
                show screen parallax1280("hima_hamstring_flexibility_grab_cg_v3", initial_ypos=0.6) with dissolve
                call showscrollingimage from _call_showscrollingimage_256
                bo "This is necessary to make sure we don't accidentally tear one of your muscles."
                bot "Her skin is so smooth... Okay, focus! I need to help her."
                call changeObedience("Himawari", 1, "hima_train_hamstring2", statlevel=2, max_times=1) from _call_changeObedience_153
                scene black
                # Mark exercise as completed to unlock the next
                $ hima_hamstring_groped = True
                him"...[bo_name_stutter]!"
                bo "S-sorry! I got stuck in a train of thought for a second."
                bo "I think I know what the issue is now. We'll work on it. For now, let's move on."
                call hidescrollingimage2("Click twice to continue.") from _call_hidescrollingimage2_130
                "She pulls her leg away quickly, clearly embarrassed."
                $ first_exercise_hima = False
                jump hima_training_proper_start_love

            "{color=[lovecolor]}You slip, and your hand lands on her inner thigh.{/color}":
                call checkLove(character="Himawari", statvalue=11, jumpvalue="hima_hamstring_grope_menu_love") from _call_checkLove_12
                bo "The tightness seems to be radiating. Let me check the adductors as well."
                him "My... adductors?"
                scene black with dissolve
                "As you shift to get a better angle, your hand slips on the floor, sliding up and brushing against the soft skin of her inner thigh. She jumps, pulling her leg away instinctively."
                scene hima_hamstring_flexibility_grab_cg_v4_love with dissolve:
                    xalign 0.5 yalign 1
                show hima_hamstring_flexibility_grab_cg_v4_love:
                    subpixel True
                    easein 3 yalign 0.5      
                him "WHOA! What was that!?"
                bo "S-Sorry! I slipped! I didn't mean to... to touch you there!"
                bot "Oh god, that was so embarrassing. Smooth move, idiot. Now she thinks I'm a total creep."
                call changeRespect("Himawari", -1) from _call_changeRespect_253
                "She stares at you for a moment, her face bright red, before breaking the silence."
                him "...Just be more careful. Let's... let's just move on."
                bot "She's not kicking me out? Phew. That was close."
                jump hima_training_menu_love

            "Stop the assessment.":
                bo "Alright. I've felt enough. Your hamstrings are definitely the issue."
                "You pull your hand back, leaving her to process the interaction."
                bot "Okay, that was super awkward. But I think I got the info I needed. I've established that I need to physically check things to help her."
                jump hima_hamstring_menu_love

label _hima_hamstring_grope_fail_love:
    #Fail state
    "You reach to touch her thigh, but she recoils instantly."
    scene hima_hamstring_flexibility_grab_cg_v5 with dissolve:
        xalign 0.5 yalign 1
    show hima_hamstring_flexibility_grab_cg_v5:
        subpixel True
        easein 3 yalign 0.5
    him "Don't touch me there! I knew you were just being a pervert!"
    "You pushed too far. She's not comfortable enough for that yet."
    call changeRespect("Himawari", -2) from _call_changeRespect_254
    jump himawari_training_kicked_out_love

label hima_training_glutes_love:
    bo "Glute bridges. Your glutes are one of your biggest muscle groups, but you're not fully using them. Lie on your back."
    him "My... glutes? Okay, Mr. Kinesiology."
    scene black with dissolve
    "She reluctantly lies down, her gaze fixed on the ceiling, trying to look bored."
    scene himawari_glutes_lie_cg with dissolve:
        xalign 0.5 yalign 1
    show himawari_glutes_lie_cg:
        subpixel True
        easein 3 yalign 0.5
    bot "Whoa... okay, deep breaths. Be professional. Focus on the exercise. Don't be weird."
    show screen parallax1280("himawari_glutes_lie_cg", initial_ypos=0.5) with dissolve
    call showscrollingimage from _call_showscrollingimage_257
    bot "Just focus on her form."
    him "...Well? What are you staring at, coach?"
    bo "R-right! Sorry! I was just checking your alignment before we start."
    bo "Now, lift your hips. Squeeze your glutes at the top."
    scene black
    call hidescrollingimage2("Click twice to continue.") from _call_hidescrollingimage2_131
    scene black with dissolve
    "She thrusts her hips upward, her body forming a mostly straight line from her shoulders to her knees."
    scene himawari_glutes_up_cg with dissolve:
        xalign 0.5 yalign 1.0
    show himawari_glutes_up_cg:
        subpixel True
        easein 3 yalign 0.8
    bot "She's so athletic. It's really impressive."
    bot "Her form is a little off, though. I have to correct it."
    bo "Not bad, but your hips are tilted and you could get them a little higher. I thought you were supposed to be the athletic one in the family?"
    him "I am! J-just tell me what I'm doing wrong!"
    him "You keep saying I'm athletic just to tell me I'm doing it wrong!"
    bot "She's getting frustrated. I need to explain it better. Maybe showing her is the only way."
    bo "This isn't about just 'doing' it, it's about doing it *right* to avoid injury. We need to figure out the issue."
    bo "I might have to give you some... tactile feedback. So you can feel which muscles to engage."
    scene black with dissolve
    "You move to kneel beside her to get a better view."
    scene himawari_glutes_up_concerned_cg with dissolve:
        xalign 0.5 yalign 1.0
    show himawari_glutes_up_concerned_cg:
        subpixel True
        easein 3 yalign 0.5
    him "Tactile... feedback? A-again?!"


    menu hima_glute_bridge_menu_love:

        "Let's work on your explosive power.":
            bo "The first thing is your lift-off. It's a little weak. It looks like you're using your back, not your glutes. Drive your heels into the floor and thrust."
            scene black with dissolve
            "She tries again, seemingly focusing, a bead of sweat on her temple."
            scene himawari_glutes_up_concerned_cg_v2 with dissolve:
                xalign 0.5 yalign 1
            show himawari_glutes_up_concerned_cg_v2:
                subpixel True
                easein 3 yalign 0.5
            him "Hnngh! Like that?"
            himt "I'm trying, but it feels so awkward. I hope he doesn't think I'm weak."
            bo "Almost! You're still starting the movement with your lower back. Try to think about pushing the floor away with your feet."
            him "You're the expert, give better instructions if something's wrong!"
            bot "She's trying so hard. I need to find a better way to explain it."
            $ hima_diagnosis_lift = True
            jump hima_glute_bridge_menu_love

        "Let's check your stability.":
            bo "Do it again. And do it right this time. Don't rush it."
            him "Ughhh..!"
            scene black with dissolve
            "She shifts her body around to get into position, her expression one of intense concentration. A slight wobble betrays her."
            scene himawari_glutes_up_concerned_cg_v3 with dissolve:
                xalign 0.5 yalign 1.0
            show himawari_glutes_up_concerned_cg_v3:
                subpixel True
                easein 3 yalign 0.8
            bo "See? There. Your right hip dipped a little. That means you're a bit unstable."
            him "It did not! I was perfectly still!"
            bo "I have a better view than you do. It's a common thing, don't worry. It's just something we need to correct."
            himt "He's watching so closely... Was I shaking? I don't know! This is so embarrassing."
            bot "Okay, I need to be careful not to make her feel self-conscious. Just focus on being helpful."
            $ hima_diagnosis_stability = True
            jump hima_glute_bridge_menu_love

        "Let's test your muscle activation.":
            bo "Let's forget power and stability for a second. The root problem might be simpler: you might not be firing your glutes properly."
            him "Of course I am! I can feel it!"
            bo "Are you sure? Lift up, and while you're at the top, consciously squeeze just your glutes. Nothing else."
            scene black with dissolve
            "She lifts and squeezes, trying it once more with your advice in mind."
            scene himawari_glutes_up_concerned_cg_v4 with dissolve:
                xalign 0.5 yalign 1.0
            show himawari_glutes_up_concerned_cg_v4:
                subpixel True
                easein 3 yalign 0.5
            him "What about n-"
            bo "Nope. I can see your hamstrings and lower back engaging. You're compensating."
            him "I'm NOT COMPENSATING!" with vpunch
            bo "O-okay!"
            $ hima_diagnosis_activation = True
            jump hima_glute_bridge_menu_love

        "{color=[obediencecolor]}Your core is unstable.{/color}" if hima_diagnosis_stability and hima_diagnosis_lift:
            # UNLOCKED BY THE STABILITY 'FAILURE'.
            bo "Your instability is the biggest thing we need to fix. It has to be corrected. I'll have to hold you in place to help your body learn what a stable position feels like."
            scene black with dissolve
            "You kneel beside her, your shadow falling over her."
            scene boruto_holding_her_hips_cg with dissolve:
                xalign 0.5 yalign 1
            show boruto_holding_her_hips_cg:
                subpixel True
                easein 3 yalign 0.5
            him "Hold me in place? What does that-"
            bot "Okay, this is it. Just be respectful and make sure it's helpful."
            bo "You feel that, [him_name]? That's where your hips need to be."
            him "O-okay, I get it, now move your h-hands."
            jump hima_glute_guide_hips_love

        "{color=[obediencecolor]}????{/color}" if not hima_diagnosis_stability or not hima_diagnosis_lift:
            "If I keep explaining what she's doing wrong, maybe she'll be more open to me helping physically..."
            jump hima_glute_bridge_menu_love

        "{color=[lovecolor]}You're not creating the necessary mind-muscle connection.{/color}" if hima_diagnosis_activation and hima_diagnosis_lift:
            # UNLOCKED BY THE ACTIVATION 'FAILURE'.
            bo "Your brain isn't connecting with the right muscle. It's a common problem for beginners. We can use tactile prompting to create that neural pathway."
            him "Tactile... prompting? That sounds like something you just made up."
            bo "It's basic kinesiology. I'm sorry, but sometimes there may need to be some physical contact just to ensure you're okay."
            him "F-fine! Whatever, you nerd!"
            bot "She agreed! Okay, just make it quick and clinical. Don't be a creep."
            jump hima_glute_tactile_feedback_love

        "{color=[lovecolor]}????{/color}" if not hima_diagnosis_activation or not hima_diagnosis_lift:
            "If I keep explaining what she's doing wrong, maybe she'll be more open to me helping physically..."
            jump hima_glute_bridge_menu_love

        "Not too bad, let's move on.":
            bo "We'll come back to this. Your entire posterior chain could use some work, but we'll get there."
            jump hima_training_menu_love

    # BRANCH 1: Manual Stabilization (The "Safer" Control Path)
    label hima_glute_guide_hips_love:
        scene black with dissolve
        bo "I don't think you quite get it yet."
        "You kneel and place your hands firmly but gently on her hip bones, supporting her."
        scene boruto_holding_her_cg with dissolve:
            xalign 0.5 yalign 1
        show boruto_holding_her_cg:
            subpixel True
            easein 3 yalign 0.5
        him "Y-your hands are..."
        bo "Focus. Now push up. Feel how I'm keeping you level? This is the stability you're lacking. Your body needs to memorize this feeling."
        himt "He's so close... But my hips... they do feel more stable. Is this really how it works?"
        bot "Okay, this seems to be helping. Her form is much better now."
        call changeObedience("Himawari", 1, "hima_train_glute1", statlevel = 2, max_times=1) from _call_changeObedience_154
        
        menu hima_glute_hip_guidance_menu_love:
            bo "Don't break form. Feel the pressure building in your muscles."

            "{color=[lovecolor]}Good. Hold it there.{/color}":
                call checkLove(11, "hima_glute_hip_guidance_menu_love", "Himawari") from _call_checkLove_13
                bo "Perfect. Hold that position. Can you feel the tension in your glutes?"
                him "I-I can't hold it here much longer, [bo_name], this is really hard!"
                "As she says that, her hips start to wobble and dip."
                scene black with dissolve
                bot "She's losing it! I have to stabilize her!"
                scene boruto_holding_her_cg_v2 with dissolve:
                    xalign 0.5 yalign 1
                show boruto_holding_her_cg_v2:
                    subpixel True
                    easein 3 yalign 0.5
                "To stop her from falling, your hands slip from her hips to brace her, ending up squarely on her glutes."
                bo "Whoa there, [him_rel]! I've got you! Come on, be tough, you can do it."
                him "W-where are you t-touching m-"
                bo "Just stabilizing you! Don't you dare drop until I say so. You got this!"
                bot "Oh god my hands are almost on her butt okay just pretend this is normal!"
                call changeLove(character="himawari",amount=1, fromwhere="hima_glute_hip_guidance_menu_dialogue", max_times=1) from _call_changeLove_58
                "As she holds the position, red with embarrassment, she tries to push your hands away."
                show screen parallax1280("boruto_holding_her_cg_v3", initial_ypos=0.5) with dissolve
                call showscrollingimage from _call_showscrollingimage_258
                him "[bo_name_stutter], your hands are t-"
                bo "What's wrong? You lost tension. Focus! I'm just making sure you're not imbalanced."
                "She freezes, her eyes filled with embarrassment. She doesn't drop."
                himt "Is he doing this on purpose...? No. He's just... helping me. It's part of the training. So why does my skin feel like it's on fire?"
                bot "She's so flustered she can't even focus on the exercise. I should probably move my hands... but her form is perfect right now!"
                call hidescrollingimage2("Click twice to continue.") from _call_hidescrollingimage2_132
                jump hima_glute_hip_guidance_menu_love

            "Alright, that's enough stabilization.":
                bo "Better. You're starting to understand the movement. Let's move on."
                jump hima_glute_bridge_menu_love


    # BRANCH 2: Tactile Feedback (The Accidental "Technical" Path)
    label hima_glute_tactile_feedback_love:
        menu hima_glute_feedback_options_love:
            "Use your fingers to 'prompt' the muscle.":
                bo "I'm just gonna need to reposition myself to give you more support, okay?"
                scene black with dissolve
                him "O-okay..."
                "You try to find the right grip to take off more weight from her body but..."
                scene boruto_grope_her_cg_love with dissolve:
                    xalign 0.5 yalign 1
                show boruto_grope_her_cg_love:
                    subpixel True
                    easein 3 yalign 0.5
                $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                bot "Oh fuck oh fuck oh fuck I'm straight up groping her why did my hands go there!!"
                him "[bo_name_stutter]?!" with vpunch
                show screen parallax1280("boruto_grope_her_cg_love", initial_ypos=0.5) with dissolve
                call showscrollingimage from _call_showscrollingimage_259
                scene black
                bo "I-I'M SO SORRY! MY HAND SLIPPED! I DIDN'T MEAN TO, I SWEAR!!"
                him "Y-your hands are on my butt, idiot! Are you insane?!"
                bo "I j-just saw your body giving out and didn't want you to fall on the floor and in my attempt to lift more weight off you my hands-"
                him "J-just let it go, it's okay... it was an accident, right?"
                bo "O-of course!! I would never do that to my own [him_rel]!"
                call hidescrollingimage2 from _call_hidescrollingimage2_133
                $ hima_glute_poked_for_real = True
                $ hima_glute_spanked = True
                #Fail state
                scene gymhima_buruma_sweaty_cg_love with dissolve:
                    xalign 0.5 yalign 1
                show gymhima_buruma_sweaty_cg_love:
                    subpixel True
                    easein 3 yalign 0.5
                him "However, I started feeling a bit awkward now, so I think that's enough coaching for today."
                bo "I'm so s-"
                him "Maybe next time try to be less clumsy, okay?"
                bo "O-okay!"
                scene black with dissolve
                bot "She said 'next time'... Phew... At least that means I still got a chance!"
                jump action_taken

label hima_training_posture_love:
    bo "Posture. This one is advanced, for total core and back stabilization. Are you sure you're ready for it?"
    him "Ready? I can do anything you can do!"
    bo "It's not about strength. It's about control and precision. It's a controlled quadrupedal spinal articulation."
    him "A what-a-pedal what? Just tell me what to do, smartass!"
    him "And quit making words up to sound smart!" 
    bo "Get on all fours. It's called the plank position. Hands under your shoulders, knees under your hips."
    him "On... all fours!? What kind of exercise is that!?" with vpunch
    
    menu hima_posture_initial_sell_love:
        him "On... all fours!? What kind of exercise is that!?"

        "It's a foundational athletic stance.":
            bo "Y-you're taking this the wrong way!"
            bo "It's a foundational athletic stance, [him_name]! It's used in everything from yoga to physical therapy. If it's too 'advanced' for you, we can stop and try again in a few months when you're more confident."
            bo "What do you say?"
            him "F-fine! I can do it! It's not a big deal."
            scene black with dissolve
            call changeObedience("Himawari", 1, "hima_posture_comply_kinesiology", statlevel=2, max_times=1) from _call_changeObedience_155

        "Big [him_rel_to_bo] knows best, trust me.":
            bo "Y-you're taking this the wrong way!"
            bo "It's the position for the exercise. Are you going to trust your coach, or are you going to waste more of our time?"
            him "Tch... You don't have to be such a jerk about it."
            "Grudgingly, she gets into position just to get it over with."
            scene black with dissolve
            call changeDominance(1, max_times=1, fromwhere="hima_posture_initial_sell_love") from _call_changeDominance_126

    scene himawari_plank_cg with dissolve:
        xalign 0.5 yalign 1.0
    show himawari_plank_cg:
        subpixel True
        easein 3 yalign 0.7
    bot "Wow. Okay. Just... be a good coach. Don't be a creep."
    bot "But I need to get closer to check her form."
    bo "Your butt is a bit too high for it to really engage your core properly."
    him "Are you looking at my ass again?!"
    bo "And your neck is too high."
    him "Maybe instead of constantly telling me what I'm doing wrong you should show me what the right way is!"
    bo "Sure, but it's easier to just show you than try to describe it. Is that okay?"
    him "F-fine..."
    scene black with dissolve
    "You move behind her, kneeling down to inspect her form better."
    $ renpy.sound.play("/audio/soun_fx/fast_blink.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    scene himawari_plank_surprised_cg with flash:
        xalign 0.5 yalign 1.0
    show himawari_plank_surprised_cg:
        subpixel True
        easein 3 yalign 0.5
    pause(1.0)
    him "You're... you're really close!"
    himt "I can feel his breath on my legs. This is so... awkward."
    bo "Like I said, I'm a professional! And a professional knows you can't examine every issue with your form by just lazily standing in 1 place all day."
    bo "From over here it's even more obvious what the problem is."
    bo "Just hold still. First, I'm placing one hand on your lower back to guide the movement."
    scene black with dissolve
    bo "Take this seriously, I know you can do it."
    scene himawari_plank_helped_cg with dissolve:
        xalign 0.5 yalign 0.0
    show himawari_plank_helped_cg:
        subpixel True
        easein 3 yalign 0.5
    "You gently place one hand on her back. She is clearly struggling."
    show screen parallax1280("himawari_plank_helped_cg", initial_ypos=0.5) with dissolve
    call showscrollingimage from _call_showscrollingimage_260
    bo "You see how even one simple touch is enough to get your muscles into overdrive?"
    bo "It's because your core isn't properly engaged."
    him "I-I'm trying my best!"
    him "It's really hard to hold this position for more than a few seconds, you know!"
    bo "I know it is, don't worry. But I think you can easily hold it a few seconds longer."
    him "I'm gonna fall any second now!!" 
    scene black
    call hidescrollingimage2("Click twice to offer more assistance.") from _call_hidescrollingimage2_134
    scene black with dissolve
    bo "It's okay, I've got you."
    scene himawari_plank_helped_cgv2 with dissolve:
        xalign 0.5 yalign 0.0
    show himawari_plank_helped_cgv2:
        subpixel True
        easein 3 yalign 0.5      
    bo "I'm lifting a small bit of weight off you without you realizing. Now you can give it your all without worrying about failure."
    bot "Damn it, it's hard to keep my knees bent like this though..."
    bot "What if I tried to move a little bit more to th-"
    scene black with vpunch
    bo "W-WOOAH FFUCKK!" with vpunch
    him "H-Hey are y-" with vpunch
    $ renpy.sound.play("/audio/soun_fx/himawari/himagasp2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    scene himawari_plan_fall at smallshake with flash
    bo "..."
    show himawari_plan_fall:
        subpixel True
        easein 0.1 zoom 1.3 xalign 0.3 yalign 0.4
    bo "vmfmfm!! FMMFMV!!" with vpunch
    show himawari_plan_fall_angry:
        subpixel True
        easein 0.1 zoom 1.3 xalign 0.7 yalign 0.4
    him "W-what the hell are you doing?!" with hpunch
    him "GET YOUR FACE OFF MY ASS BEFORE TRYING TO SPEAK, IDIOT!" with vpunch
    show screen parallax1280("himawari_plan_fall_angry") with dissolve
    call showscrollingimage from _call_showscrollingimage_261
    bo "MMVMFMFMVMVMV!!!!" with vpunch
    show screen parallax1280("himawari_plan_fall_angry_2") with dissolve
    scene black
    bo "*Gasping for air*"
    bo "I-"
    bo "I FUCKING SLIPPED!! I'M SO SORRY!"
    bot "God damn it she'll never believe me!"
    him "Gosh, how clumsy can you be, damn idiot!"
    bo "I'm really sorry it's just that my legs were getting tired and-"
    him "And is that the reason why your head is STILL RIGHT ABOVE MY ASS?!" with vpunch
    bot "O-oops."
    him "MOVE!!!" with hpunch
    bo "I'll move right away!"
    call hidescrollingimage2 from _call_hidescrollingimage2_135
    scene black with dissolve
    "You get off the ground and as she sits down collect herself, exhausted and embarassed."
    jump posture_ending_love

label posture_ending_love:
    scene gymhima_buruma_sweaty_cg_love_annoyed with dissolve:
        xalign 0.5 yalign 1
    show gymhima_buruma_sweaty_cg_love_annoyed:
        subpixel True
        easein 3 yalign 0.5
    bo "Well, if we exclude the awkward bits, I think I'm a pretty good coach after all, eh?"
    him "...That's a big 'if' right there!"
    bot "She's slightly less resistant than I would've expected her to be, given everything... Phew!"
    him "How could you be so careless and then act like you're all about my safety?" with vpunch
    bo "It's not acting, [him_name]! I care about you. A bad coach would just push you non stop. But I need to look out for you as well."
    show gymhima_buruma_sweaty_cg_love with dissolve:
        xalign 0.5 yalign 0.5
    show gymhima_buruma_sweaty_cg_love:
        subpixel True
        easein 0.5 yalign 0.3
    bo "You've got potential. Really great potential. With me supporting you like this, I'm sure you'll be strong enough for your chunin exams in no time!"
    himt "D-does he really care as much as he's saying? It seems... genuine!"
    hide gymhima_buruma_sweaty_cg_love
    show gymhima_buruma_sweaty_cg_love_annoyed
    with dissolve
    him "Hmph! That goes without saying! I would've been able to achieve that with or without your 'coaching'!" with vpunch
    bot "Of course, she's still too proud to give credit where it's due, but it's okay."
    if dominance.level == 1:
        $ dominance.level += 1
        $ dominance.value = 0
        $ hima_dominance_adv1_hatred_complete = True # Can use same variable as the hatred one
        $ notification("Your dominance level has reached level 2! The stat has been reset to 0.")
    bo "Remember this feeling [him_name]. This is the feeling of improvement. We'll continue your training soon."
    him "Yeah... whatever. Get out so I can shower."
    scene black with vpunch
    "She shoos you out of the room, clearly exhausted but also a little proud of herself."
    $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx2", loop=False, relative_volume = 0.9)
    "The door clicks shut behind you."
    $ hima_competition_full_clear = True
    jump action_taken

label himawari_training_kicked_out_love:
    
    scene himawari_angry_cg with Dissolve(0.2):
        xalign 0.5 yalign 1
    show himawari_angry_cg:
        subpixel True
        easein 0.2 yalign 0.5

    him "I can't believe I was stupid enough to trust you! Get out of my room! NOW!"
    bo "I-I'm so sorry I thought-"
    him "GET OUT!" with vpunch

    scene black with vpunch
    $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx2", loop=False, relative_volume = 0.9)
    "The door slams shut so hard the frame rattles."
    bot "Damn it, I betrayed her trust with that stupid move..."

    jump action_taken