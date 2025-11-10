#==============================================================================
# Triggered by visiting Himawari's room after winning the the wrestling event
# hima_wrestling_won == True
# himawari_obedience >= 35 (lvl1) or himawari_obedience_level >= 2.

# Available points
# Hatred -> 4 level one points
# Obedience -> 5 level two points
# Dominance -> 3 level one points
#==============================================================================

# Hatred variant
default himawari_squat_minigame_frombehind = False
default hima_agreed_squat_competition = False
default hima_in_buruma = False
default hima_hamstring_groped = False
default hima_glute_spanked = False
default hima_buruma_already_asked = False
default hima_first_time_competition = True
default hima_competition_last_win = False
default hima_competition_full_clear = False
# Progression Flags for Training Section
default neverwonhima = True
default first_exercise_hima = True
default hima_hamstring_touch_unlocked = False
default hima_hamstring_grope_unlocked = False
default hima_glute_spank_unlocked = False
default hima_glute_poked_for_real = False
# Quest Flag.
default hima_dominance_adv1_hatred_complete = False

label hima_strength_training_check:
    if (himawari_obedience < 20 and himawari_obedience_level==1):
        "Her will is still too strong. She dismisses your offer to train with someone she considers a loser."
        "Increase her obedience to 20 before suggesting this."
        jump himastretchingmenu
    
    elif himawari_respect < 0:
        show hima mad3 with vpunch
        him "Get out. I'm not in the mood for you."
        call checkRespect(0, "Himawari") from _call_checkRespect_11
        bot "The bitch is still feisty. I'll have to be more... persuasive."
        "She's too angry to even consider training with you right now."
        jump action_taken
    
    # This whole block will only play out once. All future repeats, you go straight into the competition intro.
    elif not hima_agreed_squat_competition:
        show boruto sceeming with dissolve
        bo "Still sore from getting your ass kicked in wrestling?"
        show hima mad with dissolve
        him "Shut up! That was a fluke! I'm just... trying to get my form right for the Chunin Exams."
        bo "Your form is terrible. You're too rigid. You're going to pull something training like that."
        show hima smug2 with dissolve
        him "And I suppose you're the grand master of taijutsu now?"
        bo "I'm the one who pinned you in under a minute. So, yes. You need a real coach if you're serious."
        him "And let me guess, you're volunteering? How generous."
        bo "I want to see you succeed, [him_name]. For real. Who else is going to help you?"
        show hima smug3 with dissolve
        him "What exactly do you know about success, loser?"
        bo "Well let's just say that actions speak louder than words. How about I show you?"
        him "I can't wait to hear where this is going..."
        bo "A simple competition. Me versus you. Less talk, more work."
        him "Hahaha! Yeah right. Why would I waste my time on you?"
        him "You don't know the first thing about fitness! Look at yourself!"
        show boruto angry with dissolve
        bo "Keep talking. All words, no action. Proves my point."
        show hima smug with dissolve
        him "I don't need 'actions' when we both know I'd destroy you at any competition, even one you picked."
        show boruto sceeming2 with dissolve
        bo "Talk is cheap. How about money? Would that sweeten the deal for you?"
        show hima surprised with dissolve
        him "M-Money?"
        bot "Of course she changes her tune now..."
        bo "You beat me in a squat competition, you get $100. On the spot."
        show hima smug3 with dissolve
        him "Ha! Easy money! You're on, idiot!"
        show boruto sceeming3 with dissolve
        bo "But there's a catch."
        him "Here we go..."
        bo "If I win..."
        him "Yeah, yeah, whatever you want! That's about as likely as pigs flying."
        bot "Careful what you wish for."
        bo "Whatever I want, huh? Don't make promises you can't keep."
        him "I am confident. I'm confident I'll destroy you."
        bo "Then we have a deal. My win means you accept my 'coaching', no questions asked."
        him "Fine. But we do this my way. In my room. Starting tomorrow."
        him "And if you try any 'funny business' like last time, I'll kick you so hard you'll be tasting your own tonsils."
        bo "Deal. Be ready."
        him "I will be! As if I could ever lose a bet to you!"
        show boruto angry with dissolve
        bot "Keep talking, bitch. Soon enough, you won't be able to talk back at all."
        $ hima_agreed_squat_competition = True
        "You've challenged [him_name] to a competition. Return to her room later to begin."
        jump action_taken
    else:
        label hima_agreed_squat_competition:
        # --- Convincing her to change. This first variation will only be asked once. Otherwise it goes to the "reasking" variation. ---

        if not hima_in_buruma:
            if not hima_buruma_already_asked:
                bo "So, are you ready to start squatting?"
                show hima smug with dissolve
                him "Am I ready? The question is are you ready to lose your money? Let's get this over with."
                bo "Hold on. You're not seriously going to train in that, are you?"
                show hima mad with dissolve
                him "What's wrong with what I'm wearing? Are you trying to weasel out of this already?"
                show boruto sceeming with dissolve
                bot "Her normal clothes are hot, but that gym outfit... it'll show off every curve. I need her in that."
                bo "You'll rip something. Or get heatstroke. If you're going to take this seriously, you need to dress for it. Proper workout clothes."
                him "Ugh, you're so annoying! Always making up excuses!"
                show hima smugshy with dissolve
                himt "Maybe he really cares about me after all..."
                if tsunade_discovery_seen == True:
                    bot "She's complaining, but the fight is already draining out of her. This must be what Tsunade meant when she said 'psychoactive effects' about those exposed to my semen... Perfect!"
                else:
                    bot "She's complaining, but the fight is already draining out of her. Perfect!"
                $ hima_buruma_already_asked = True
            # Second time player attempts to ask her to change into buruma, slight variation.
            else:
                bo "So, are you ready to start squatting or...?"
                him "Let me guess, you're gonna start telling me how 'strong' you are and how you're gonna prove it with actions, only to use my outfit as an excuse to run away again?"
                bo "I'm only trying to look out for you. I already explained why it's necessary."
                show boruto angry with dissolve
                bot "Just let me see you in that hot damn outfit already you bitch..."
                
        menu hima_ask_burama:
            # For those who get here before collecting the necessary lvl 2 obedience points from other advancement events (fail-retry state if statcheck fails).
            "{color=[obediencecolor]}Insist she wears the proper gear.{/color}":
                call checkObedience(statvalue=2, statlevel=2, jumpvalue="hima_change_failure", character="Himawari") from _call_checkObedience_39
                show hima shy with dissolve
                himt "Why am I even listening to him? Ugh..."
                him "F-fine! I'll change! But don't you dare peek, you perv! And I'm still going to crush you!"
                him "I'll say when I'm ready."
                bo "Fine, sheesh, why on earth would I peek on my own [him_rel] changing, are you out of your mind?"
                hide hima with easeoutright
                scene black with dissolve
                $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx2", loop=False, relative_volume = 0.9)
                "She kicks you out and proceeds to change."
                $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 0.9)
                menu:
                    "You decide to:"
                    "Wait outside.":
                        call changeRespect("Himawari", amount=3) from _call_changeRespect_243
                        bot"I have no need for peeking... Considering what's to come after I beat her in this competition!"
                        bot".."
                        bot"..."
                        bo"[him_name], are you done yet?"
                        him"Come in."
                    "Peek!":
                        bot"She'll never know... Why wouldn't I peek?!"
                        bot"Juuuust a quick short look and if my timing is right then maybe..."
                        show screen peeking12801024("hima_changing_buruma") with flash
                        bot"...talk about good timing!"
                        bot"Oh, dear [him_rel], I'd love to get my hands on those titties of yours!"
                        bot"And that isn't all..."
                        bot"Look at that ass!" with vpunch
                        bot"I'd love t-"
                        scene black with dissolve
                        hide screen peeking12801024
                        scene black with dissolve
                        him"Come in."
                        bo"O-okay!"

                $ hima_in_buruma = True
                jump hima_squat_minigame_start

label hima_change_failure:
    # Fail condition
    show hima mad3 with vpunch
    him "I'm not changing! I'll beat you in my pajamas if I have to! Now put your money where your mouth is or get out!"
    call changeRespect("Himawari", -2) from _call_changeRespect_244
    show boruto angry with dissolve
    bot "Tch. Stubborn bitch."
    bot "She refuses to change. Maybe if I could somehow make her more receptive to my suggestions by making her more obedient..."
    jump action_taken


# --- The Squat Minigame ---
label hima_squat_minigame_start:
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
        menu competition_full_clear:
            "Skip the squatting competition?"
            "Yes, and bring me my Doritos.":
                dev"Doritos are not available for delivery yet."
                dev"Visit www.houseofshinobi.com to see our store."
                jump hima_training_proper_start_repeatable
            "I don't skip leg day bitch.":
                pass
    # First time entry
    if hima_first_time_competition:
        if day_part == 3: 
            scene himawari_bedroom_2
        else:
            scene himawari_bedroom_1
        show gymhima shy at center with easeinleft
        him "Happy now? I look ridiculous."
        show boruto sceeming at left with dissolve
        bot "You look like a piece of meat, and I'm starving."
        bo "You look like you're serious about this for once. Good."
        bot "It seems she intends to actually try hard to prove me wrong... Perhaps I've underestimated her."
        show gymhima smug with dissolve
        him "Alright, loser. You, me, squats. First one to quit or fail loses. And you owe me $100."
        bo "And if I win, you do whatever I say. You'll accept my 'coaching', no questions asked."
        him "Hah! In your dreams."
        bot "Soon to be your reality."
        $ hima_first_time_competition = False

    # Lost last time
    elif not hima_first_time_competition and hima_competition_last_win == False:
        if day_part == 3: 
            scene himawari_bedroom_2
        else:
            scene himawari_bedroom_1
        show gymhima smug at right with dissolve
        him "Came back to get your ass kicked again? I didn't know you were a masochist."
        show boruto angry at left with dissolve
        bot "You little bitch..."
        bo "Don't get cocky just because I tried to be a good [him_rel_to_bo] and let you win, [him_name]."
        bo "Otherwise I'll be forced to take it seriously."
        him "You're good with words, but this is a physical competition, and we already saw who's more fit!"
        show boruto sceeming2 with dissolve
        bot "Oh I'll show you physical alright if you don't drop that bitchy attitude..."
        bo "You asked for it. Let's get started."

    # Won last time
    elif not hima_first_time_competition and hima_competition_last_win:
        if day_part == 3: 
            scene himawari_bedroom_2
        else:
            scene himawari_bedroom_1
        show gymhima smug at right with easeinleft        
        him "You really wanna give me your money huh?"
        show boruto sceeming at left with dissolve
        bo "Uhh... Are you forgetting who won last time?"
        show gymhima smug at right with dissolve
        him "No but you must clearly forgetting *why* you won."
        show boruto sceeming3 with dissolve
        bot "Because you're my bitch and I own you."
        bo "Because I'm stronger than you?"
        him "Ha! Because I let you, of course! Loser!"
        show boruto angry with dissolve
        bot "This little bitch..."
        bo "Yeah, okay, cut the trashtalking and start squatting."
        him "Don't order me around!"
        bot "That's exactly what I'll be doing. Soon, you'll beg for my orders."
        bo "Squat."

    menu:
        "Move behind her.":
            $ himawari_squat_minigame_frombehind = True
            show boruto sceeming3 with dissolve
            bot "Let me sneakily adjust my position and get that first row experience of that ass...!"
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
        "You completed [pushups] squats and crushed her in the competition!"
        bot "Look at her, gasping for air, and this is just the beginning."
        bo "What's wrong, [him_name]? Out of breath? I told you I've been training."
        bo "A deal's a deal. Now you're my student. And you'll do exactly as I say."
        him "I... *pant*... I hate you..."
        bo "Good. Hate is a powerful motivator. Now, let's begin your first lesson."
        himt "How could I lose... to someone like him! UGHH!" with vpunch
        scene black with dissolve
        "She is visibly shaken as she realizes she will have to deal with your ego while you coach her."
        if hima_competition_full_clear:
            jump hima_training_proper_start_repeatable
        else:
            jump hima_training_proper_start
            
    else:
        # Player loses
        $ hima_competition_last_win = False
        scene black with dissolve
        scene hima_squat_lose_cg with dissolve:
            xalign 0.5 yalign 0.0
        show hima_squat_lose_cg:
            subpixel True
            easein 3 yalign 0.5
        him "Ha! See? All talk, loser! I knew you couldn't keep up."
        menu hima_squat_competition_fail:
            "You failed to beat her. Pathetic."
            "Pay her $100 as promised." if money >= 100:
                call changeMoney(-100) from _call_changeMoney_23
                bo "Tch... fine. Here."
                "You hand over the $100."
                call changeRespect("Himawari", 2) from _call_changeRespect_245
                him "Heh. Pleasure doing business with you, bozo. Now get out, I have real training to do."
                bot "Enjoy that money, bitch. Next time, I won't be so merciful."
                jump action_taken
            "Don't give her shit.":
                bo "Uh... I, uh, seem to have left my wallet in my other pants."
                call changeRespect("Himawari", -5) from _call_changeRespect_246
                scene hima_squat_lose_cg_mad with dissolve:
                    xalign 0.5 yalign 0.5
                show hima_squat_lose_cg_mad:
                    subpixel True
                    easein 0.3 zoom 1.2 yalign 0.2
                him "ARE YOU SERIOUS!? You made a bet with me and you don't even have the money!?" with vpunch
                him "You're pathetic! A liar and a weakling! Get out of my sight!"
                bot "Fucking bitch... I'll make you pay for that disrespect."
                call changeHatred(1, max_times=1, fromwhere="hima_squat_competition_fail_dontpay") from _call_changeHatred_207
                scene black with dissolve
                "She's furious. You lost the bet and couldn't even pay up. You've lost all her respect."
                jump action_taken


label hima_training_proper_start:
    $ initialize_replay_defaults()
    scene gymhima_buruma_sweaty_cg with dissolve:
        xalign 0.5 yalign 1
    show gymhima_buruma_sweaty_cg:
        subpixel True
        easein 3 yalign 0.7

    $ playmusic("audio/ost/house2.opus",0.6)
    if first_exercise_hima:
        him "So? What's this 'coaching' all about? Just get it over with."
        himt "I can't believe I lost... He's so much stronger than before. It's... infuriating. And kind of..."
        bot "She's trying to process it. The cognitive dissonance is delicious. The strong [him_rel_to_bo] she resents is now her 'teacher'. Time to show her who's in charge."
        bo "Alright [him_name], let's see... I think we should start with..."
    else:
        him "Try anything like that again and..."
        bo "And what? Do you want to get stronger or not?"
        bo "Have I not already proven to you I know what I'm doing?"
        him "I-I guess... Just tone down the touching!"
        bo "We'll do whatever's necessary to make you stronger."

    menu hima_training_menu:
        # The first training section is available until its milestone flag is set.
        "Hamstring stretches.":
            $ hima_hamstring_repeat_counter = 0
            jump hima_training_hamstrings

        # ??? for glute activation (requires hamstring stretch full completion first)
        "{color=[obediencecolor]}???{/color}" if not hima_hamstring_groped:
            bot"I'll probably need to assert more control during the hamstring stretches before she'll be receptive to other kinds of 'help'..."
            jump hima_training_menu

        # Unlock if hamstring stretches full completion
        "{color=[obediencecolor]}Glute activation{/color}" if hima_hamstring_groped:
            call checkObedience(statvalue=2, statlevel=2, jumpvalue="none", character="Himawari") from _call_checkObedience_40
            # Fail state if obedience is too low
            if himawari_obedience.level<2 or (himawari_obedience.level == 2 and himawari_obedience.value < 2): 
                bot"She's still too defiant. I need to somehow make her more obedient..."
                jump hima_training_menu
            else:
                jump hima_training_glutes

        # ??? for posture correction (requires glute activation full completion first which leads to unavoidable failure)
        "{color=[hatredcolor]}???{/color}" (advancement_event=True) if not hima_glute_spanked:
            bot"I'll probably need to assert more control during other exercises before she'll be receptive to other kinds of 'help'..."
            jump hima_training_menu

        # Unlock if glute activation full completion achieved
        "{color=[hatredcolor]}Advanced posture correction{/color}" if hima_glute_spanked and dominance.level >= 2:
            call checkHatred(statvalue=35, statlevel=1, jumpvalue="hima_training_menu") from _call_checkHatred_40
            # Fail state if obedience is too low
            jump hima_training_posture

        "{color=[hatredcolor]}Advanced posture correction{/color}" (advancement_event=True) if hima_glute_spanked and dominance.level == 1:
            call checkHatred(statvalue=35, statlevel=1, jumpvalue="hima_training_menu") from _call_checkHatred_41
            # Fail state if obedience is too low
            jump hima_training_posture

        "That's enough for today.":
            scene black with dissolve
            bo "We're done for now. Don't think this is over. Your training has just begun."
            him "Whatever... just get out."
            bot "I've planted the seed. Next time, we'll go further."
            jump action_taken

# ==============================================================================
# STRETCH 1: HAMSTRINGS
# ==============================================================================

label hima_training_hamstrings:
    bo "Hamstring stretches!"
    bo "Here's what we're gonna do."
    bo "Sit on the floor. Legs straight. Touch your toes."
    him "Hmph! I know how to do a basic stretch, idiot."
    scene black with dissolve
    "She shakes off her frustration, giving you the benefit of the doubt as she begins to follow your guidance."
    scene hima_hamstring_notstraight_cg with dissolve: 
        xalign 0.5 yalign 1
    show hima_hamstring_notstraight_cg:
        subpixel True
        easein 3 yalign 0.5
    bo "That's what you call straight? This isn't a god damn photoshoot session. This is exercise. Who are you posing for?"
    show hima_hamstring_notstraight_cg_surprised with dissolve:
        yalign 0.5
    himt "*gasp* What am I doing? Why is my body automatically going into posing mode when I'm supposed to be stretching?!"
    scene black with dissolve
    "Flustered by her realization, she attempts the stretch again, her form sloppy and strained, her back rounding immediately."
    scene hima_hamstring_cg with dissolve:
        xalign 0.5 yalign 0.95
    show hima_hamstring_cg:
        subpixel True
        easein 3 yalign 0.7
    bot "Terrible. She's all about showing off while completely disregarding technique. That pride will be the first thing to break."
    bo "Do you? Because that's not a stretch, that's a spinal injury waiting to happen. Your back is completely rounded."
    him "I SAID I KNOW WHAT I'M DOING!!" with vpunch
    bot "She's trying to process the humiliation of losing so easily and now being lectured... Little by little she'll get used to it though!"
    bo "Clearly you don't. A teacher doesn't let his student perform a technique incorrectly. We're going to fix this, right now."
    himt "Damn loser, treating me like a child... But he's not wrong about my ba- No! I won't give him the satisfaction."

    menu hima_hamstring_menu:
        bot "Her pride is on the line. She's desperate to prove me wrong, and that desperation is the key."

        "Show me again. Slowly." if hima_hamstring_repeat_counter<3:
            default hima_hamstring_repeat_counter = 0
            if hima_hamstring_repeat_counter == 0:
                bo "Fine. Show me again. But this time, try to actually touch your feet."
                him "I AM touching them!"
                bo "Barely, you're not even touching your toes. Again."
                scene himawari_bedroom_strength_training_line_347 with dissolve:
                    xalign 0.5 yalign 1
                show himawari_bedroom_strength_training_line_347:
                    subpixel True
                    easein 3 yalign 0.7
                "She attempts the stretch again, with the same flawed result, her frustration mounting."

            elif hima_hamstring_repeat_counter == 1:
                bo "Still wrong. Your pelvis isn't tilting. You're just collapsing your torso. Are you even listening to my instructions?"
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
                bo "Pathetic. Again. Maybe it'll be easier if you focus on just 1 foot first."
                him "[bo_name]! Are you just trying to humiliate me!?" with vpunch
                scene himawari_bedroom_strength_training_line_362 with dissolve:
                    xalign 0.5 yalign 1
                show himawari_bedroom_strength_training_line_362:
                    subpixel True
                    easein 3 yalign 0.7
                bo "I'm trying to *teach* you. You're the one humiliating yourself with this stubborn defiance. Do it right, or we'll be here all day."
                bot "Pushing her buttons, forcing her to choose between her pride and her desire for this to end... All aprt of the plan!"

            $ hima_hamstring_repeat_counter += 1
            if hima_hamstring_repeat_counter >= 2:
                $ hima_guide_physically = True
            jump hima_hamstring_menu

        "{color=[dominancecolor]}???{/color}" if not hima_guide_physically:
            bot"She's not frustrated enough yet. She needs to believe she's incapable of succeeding on her own."
            jump hima_hamstring_menu

        # Unlocked permanently after "show me again" 2 times.
        "{color=[dominancecolor]} I'll have to guide you physically.{/color}" if hima_guide_physically:
            default hima_guide_physically = False
            call checkDominance(statvalue=30, statlevel=1, jumpvalue="hima_hamstring_menu") from _call_checkDominance_62
            $ hima_guide_physically = True
            bo "One thing I noticed is that your pride seems to be an obstacle to your progress." 
            bo "And as you know by now, a good coach has to get hands-on when the student is this resistant."
            him "Don't you dare start using these cheap excuses to g-"
            scene black with dissolve
            "Before she can finish her sentence, you move to sit behind her, your presence looming."
            scene hima_hamstring_lookingback_cg with dissolve: 
                xalign 0.5 yalign 1
            show hima_hamstring_lookingback_cg:
                subpixel True
                easein 3 yalign 0.5
            him "W-What are you doing? D-don't get close to me."
            bo "I'm your teacher. My job is to ensure you learn, even if you're too stubborn to listen. Stay still."
            jump hima_hamstring_correct_form

        # ??? for different approach (unlocked when one of the two hamstring kinds of touches is done)
        "{color=[obediencecolor]}???{/color}" if not hima_hamstring_touch_unlocked:
            bot"I guess I have to make her less resistant first..."
            jump hima_hamstring_menu

        "{color=[obediencecolor]}Let's try a different approach.{/color}" if hima_hamstring_touch_unlocked:
            default hima_different_approach = False
            $ hima_different_approach = True
            bo "Since plan A isn't working with that stubborn head of yours, I'll need to assess the root of the problem."
            bot "It's not about her failure anymore, it's about my 'diagnosis'. A personal trainer can touch his student, can't he?"
            him "Assess...? What are you talking about?"
            jump hima_hamstring_assess_flexibility

        "This is pointless. Let's move on.":
            bo "We'll come back to this. Hamstring stretches aren't your strong suit. But this flexibility issue is going to sabotage all your other training."
            bot "A tactical retreat. I've planted the seed of doubt in her mind about her own body."
            jump hima_training_menu

    # First major branch, focusing on 'correcting' her form.
    label hima_hamstring_correct_form:
        bo "I'm going to place my hands on your back to provide tactile feedback on your spinal alignment. Do not tense up."
        scene black with dissolve
        "Ignoring her complaints, you place your hands on her lower back, thumbs pressing into the tense muscles of her upper back."
        scene himawari_bedroom_strength_training_line_227 with dissolve:
            xalign 0.5 yalign 1
        show himawari_bedroom_strength_training_line_227:
            subpixel True
            easein 3 yalign 0.5
        him "I-I'm not tense!"
        bo "You are. Relax."
        bot "So easy. The lie of 'helping' is a powerful key. She's already letting me control her."
        call changeObedience("Himawari", 1, "hima_train_hamstring1", max_times=1, statlevel=2) from _call_changeObedience_147
        $ hima_hamstring_touch_unlocked = True

        menu hima_hamstring_correction_options:
            bo "Now... let's fix this mess."

            "Apply firm, steady pressure." if not hima_applied_pressure:
                default hima_applied_pressure = False
                $ hima_applied_pressure = True
                bo "I'm going to apply pressure now. Don't fight it. Let your body sink into the stretch."
                scene black with dissolve
                "You push down firmly but gently, forcing her back to straighten. A small gasp escapes her lips as she's pushed deeper than she could go on her own."
                scene himawari_bedroom_strength_training_line_227_v2 with dissolve:
                    xalign 0.5 yalign 1.0
                show himawari_bedroom_strength_training_line_227_v2:
                    subpixel True
                    easein 3 yalign 0.7
                him "*gasp* O-okay... I feel that."
                himt "It hurts... but it's a good hurt. It feels... right. Why does it feel right when he's forcing me?"
                bo "That's the feeling of a proper stretch. Remember it. It's the feeling of my guidance."
                bot "She's associating my physical control with positive results and relief. A crucial step!"
                jump hima_hamstring_correction_options

            "{color=[dominancecolor]}Force her down. Hard.{/color}" if not hima_forced_down:
                default hima_forced_down = False
                $ hima_forced_down = True
                call checkDominance(30, "hima_hamstring_correction_options") from _call_checkDominance_63
                bo "You're still fighting me. It seems a gentle approach is wasted on you."
                scene black with dissolve
                "Without warning, you shove her back down, hard and fast, forcing her much deeper into the stretch than she's prepared for."
                scene himawari_bedroom_strength_training_line_227_v3 with dissolve:
                    xalign 0.5 yalign 1
                show himawari_bedroom_strength_training_line_227_v3:
                    subpixel True
                    easein 3 yalign 0.5
                show himawari_bedroom_strength_training_line_227_v3_angry with dissolve:
                    yalign 0.5
                him "AH! That hurts, you bastard!"
                bo "Pain is an excellent teacher. You see how you managed to actually touch your toes? Now, are you going to listen to me, or do we need another lesson?"
                himt "He's enjoying this... humiliating me! And the worst part is the advice worked. My back is completely straight."
                him "I-I..."
                call changeDominance(1, max_times=1, fromwhere="hima_hamstring_correction_options_forceherdown") from _call_changeDominance_123
                bo "Good. I'm glad we understand each other."
                jump hima_hamstring_correction_options

            "Slide your hands down her back." if not hima_slide_hands:
                default hima_slide_hands = False
                $ hima_slide_hands = True
                bo "Your entire spine is out of alignment. Let me see."
                scene black with dissolve
                "You slowly slide your hands from her shoulders down the length of her back, feeling the curve of her spine, your fingers brushing against the fabric of her shirt."
                scene himawari_bedroom_strength_training_line_227_v4 with dissolve:
                    xalign 0.5 yalign 1
                show himawari_bedroom_strength_training_line_227_v4:
                    subpixel True
                    easein 3 yalign 0.5
                him "Wh-what are you doing!?"
                bo "Checking for tension knots. You're riddled with them. A sign of chronic poor posture."
                bot "The excuse is perfect. I can touch her anywhere on her back, and it's all part of the 'assessment'!"
                him "O-okay... fine. Just... be quick about it."
                bot "She's capitulated. The initial touch has been accepted and now the boundaries are being expanded."
                jump hima_hamstring_correction_options

            "Nevermind." if not hima_slide_hands and not hima_forced_down and not hima_applied_pressure:
                bo "You're learning slower than I thought you would."
                bo "Are you gonna take this seriously or what?"
                jump hima_hamstring_menu
            
            "Still not quite right." if hima_slide_hands and hima_forced_down and hima_applied_pressure:
                bo "Still not quite right, after all."
                bo "Looks like we need a different approach."
                jump hima_hamstring_menu

    # Second major branch, a more direct transgression under the guise of 'assessment'.
    label hima_hamstring_assess_flexibility:
        bo "The problem might not be your back, but your hamstrings themselves. They might be so tight that they're pulling your pelvis out of alignment, forcing your back to compensate."
        him "You think...?"
        bot "She's buying it. The pseudo-scientific language makes it sound legitimate. Now for the physical exam!"
        bo "I need to check the muscle tension directly. Hold still."
        scene black with dissolve
        "Before she can agree or protest, you reach out and place a hand on her right calf."
        scene hima_hamstring_flexibility_grab_cg with dissolve:
            xalign 0.5 yalign 0.8
        show hima_hamstring_flexibility_grab_cg:
            subpixel True
            easein 3 yalign 0.5
        him "And this is supposed to achieve, what exactly?"
        bo "This is just diagnostic. Trust my process."
        show hima_hamstring_flexibility_grab_cg:
            subpixel True
            easein 0.5 yalign 0.7 zoom 1.2
        "You gently squeeze her calf muscle."
        bo "Hmm. Tense. As I suspected."
        scene black with dissolve
        "You reposition yourself, sliding your hand up slowly, from her calf, over the back of her knee, to the base of her hamstring."
        scene hima_hamstring_flexibility_grab_cg_v2 with dissolve:
            xalign 0.5 yalign 1.0
        show hima_hamstring_flexibility_grab_cg_v2:
            subpixel True
            easein 3 yalign 0.5
        himt "His hand... It's just an 'assessment', right? So why is my heart beating so fast?"
        bo "I think I know what's going on now that I got a little bit closer."
        bot "The slow, deliberate movement. It's not aggressive, it's calculated... That's why she's not stopping me!"

        menu hima_hamstring_grope_menu:
            "Your hand rests on her lower thigh. The real test begins now."

            "{color=[obediencecolor]}Grab her thigh firmly to 'test' the muscle.{/color}" if himawari_obedience_level >= 2:
                call checkObedience(statvalue=2, statlevel=2, jumpvalue="_hima_hamstring_grope_fail", character="Himawari") from _call_checkObedience_41
                scene black with dissolve
                bo "This is the source of the problem. Right here."
                "Your hand clamps down firmly on her mid-thigh, your fingers pressing into the toned muscle."
                scene hima_hamstring_flexibility_grab_cg_v3 with dissolve:
                    xalign 0.5 yalign 1.0
                show hima_hamstring_flexibility_grab_cg_v3:
                    subpixel True
                    easein 3 yalign 0.6
                $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                him "H-Hey!"
                bo "Just as I thought. Tight as a drum. We have a lot of work to do."
                show screen parallax1280("hima_hamstring_flexibility_grab_cg_v3", initial_ypos=0.6) with dissolve
                call showscrollingimage from _call_showscrollingimage_252
                bo "I just need to have a better look to know exactly where to start..."
                bot "Her skin is so smooth. I can feel the muscle twitching under my palm. She's trying to decide if she should fight. But she won't. She can't."
                call changeObedience("Himawari", 1, "hima_train_hamstring2", statlevel=2, max_times=1) from _call_changeObedience_148
                scene black
                # Mark exercise as completed to unlock the next
                $ hima_hamstring_groped = True
                him"G-get your hands off me you creep!"
                bo "Will you let me do my job for once? I'm trying to help."
                "You hold the grip for a moment longer than necessary, your thumb stroking her skin. She's flustered and avoids your gaze."
                bo "I think I know where the issue lies already but we'll address that later. For now, let's move on."
                call hidescrollingimage2("Click twice to continue.") from _call_hidescrollingimage2_126
                "She pushes you off quickly, clearly embarrassed."
                $ first_exercise_hima = False
                jump hima_training_proper_start

            "{color=[hatredcolor]}Let your hand wander to her inner thigh.{/color}":
                call checkHatred(30, "hima_hamstring_grope_menu") from _call_checkHatred_42
                bo "The tightness seems to be radiating. I need to check the adductors as well."
                him "My... adductors?"
                scene black with dissolve
                "You rotate your hand, letting your fingers brush against the soft skin of her inner thigh. She jumps, pulling her leg away instinctively."
                scene hima_hamstring_flexibility_grab_cg_v4 with dissolve:
                    xalign 0.5 yalign 1
                show hima_hamstring_flexibility_grab_cg_v4:
                    subpixel True
                    easein 3 yalign 0.5      
                him "STOP IT! What the hell do you think you're doing!?"
                bo "I'm trying to help you! Your muscles are a mess! But if you're going to be hysterical, then fine. We're done here."
                bot "Pushed too far, too soon. But twisting it, making it her fault for reacting... that plants a different kind of seed."
                call changeRespect("Himawari", -2) from _call_changeRespect_247
                jump himawari_training_kicked_out # Fail condition

            "Stop the assessment.":
                bo "Alright. I've seen enough. Your hamstrings are definitely the issue."
                "You pull your hand back, leaving her to process the interaction."
                bot "A tactical retreat. I've established that her legs are fair game for my 'assessment'. I'll use that opening later."
                jump hima_hamstring_menu

        label _hima_hamstring_grope_fail:
            #Fail state
            "You reach to grip her thigh, but she recoils instantly."
            scene hima_hamstring_flexibility_grab_cg_v5 with dissolve:
                xalign 0.5 yalign 1
            show hima_hamstring_flexibility_grab_cg_v5:
                subpixel True
                easein 3 yalign 0.5
            him "Don't touch me there! I knew you were a pervert!"
            "You pushed too far. She's not compliant enough for that yet."
            call changeRespect("Himawari", -2) from _call_changeRespect_248
            jump himawari_training_kicked_out

label hima_training_glutes:
    bo "Glute bridges. Your ass is your biggest muscle group, but you're not using it. Lie on your back."
    him "My... Just say glutes, you perv!"
    scene black with dissolve
    "She reluctantly lies down, her gaze fixed on the ceiling, avoiding you."
    scene himawari_glutes_lie_cg with dissolve:
        xalign 0.5 yalign 1
    show himawari_glutes_lie_cg:
        subpixel True
        easein 3 yalign 0.5
    bot "D-damn it, in that position, laying down, she looks just about ready for me to..."
    show screen parallax1280("himawari_glutes_lie_cg", initial_ypos=0.5) with dissolve
    call showscrollingimage from _call_showscrollingimage_253
    bot "No, I can't take it that far with her yet."
    him "...Well? Come on, expert."
    bo "R-right! I was checking out to see if there's any tension left in your body before we proceed with the exercise."
    bo "Now, lift your hips. Squeeze your glutes at the top."
    scene black
    call hidescrollingimage2("Click twice to continue.") from _call_hidescrollingimage2_127
    scene black with dissolve
    "She thrusts her hips upward, her body forming a straight line from her shoulders to her knees."
    scene himawari_glutes_up_cg with dissolve:
        xalign 0.5 yalign 1.0
    show himawari_glutes_up_cg:
        subpixel True
        easein 3 yalign 0.8
    bot "Presenting it to me on a silver platter. What a good girl."
    bot "Almost as if her body involuntarily responded to my command..."
    bo "Sloppy. Your hips are tilted and you're barely getting any height. I thought you were supposed to be the athletic one in the family?"
    him "I am! J-just tell me what to do next!"
    him "Always bringing up how 'athletic' I am just to tell me I'm doing it wrong!"
    bot "She's practically begging for me to 'correct' her. It would be rude not to oblige."
    bo "This isn't about just 'doing' it, it's about doing it *right*. We need to diagnose the issue."
    bo "I'm going to have to give you some... tactile feedback. So you understand which muscles to engage."
    scene black with dissolve
    "You reposition yourself in preparation for your excuse."
    scene himawari_glutes_up_concerned_cg with dissolve:
        xalign 0.5 yalign 1.0
    show himawari_glutes_up_concerned_cg:
        subpixel True
        easein 3 yalign 0.5
    him "Tactile... feedback? A-again?!"


    default hima_diagnosis_lift = False
    default hima_diagnosis_stability = False
    default hima_diagnosis_activation = False
    menu hima_glute_bridge_menu:

        "Let's test your explosive power.":
            bo "The first problem is your lift-off. It's weak. There's no power. It looks like you're using your back, not your glutes. Drive your heels into the floor and thrust."
            scene black with dissolve
            "She tries again, seemingly focusing, a bead of sweat on her temple."
            scene himawari_glutes_up_concerned_cg_v2 with dissolve:
                xalign 0.5 yalign 1
            show himawari_glutes_up_concerned_cg_v2:
                subpixel True
                easein 3 yalign 0.5
            him "Hnngh! Like that?"
            himt "If he's gonna keep pissing me off then I might as well enjoy it by pretending to be dumb. Hmph!"
            bo "Are you trying to piss me off? Your ass is still on the floor."
            him "You're the expert, give better instructions if something's wrong!"
            bot "God damn bitch, she's trying to make fun of me, I'll teach her."
            $ hima_diagnosis_lift = True
            jump hima_glute_bridge_menu

        "Let's test your stability.":
            bo "Do it again. And do it right this time. Don't play dumb if you wanna get stronger."
            him "Ughhh..!"
            scene black with dissolve
            "She shifts her body around to get into the plank position, her expression one of intense concentration. A slight wobble betrays her."
            scene himawari_glutes_up_concerned_cg_v3 with dissolve:
                xalign 0.5 yalign 1.0
            show himawari_glutes_up_concerned_cg_v3:
                subpixel True
                easein 3 yalign 0.8
            bo "See? There. Your right hip dipped, same as earlier. Total instability."
            him "It did not! I was perfectly still!"
            bo "I have a better view than you do. Your proprioception is off. Another flaw to correct."
            himt "He's making things up... I think. Was I shaking? I don't know! He's messing with my head."
            bot "Gaslighting 101. Make her doubt her own senses."
            $ hima_diagnosis_stability = True
            jump hima_glute_bridge_menu

        "Let's test your muscle activation.":
            bo "Let's forget power and stability. The root problem might be simpler: you literally don't know which muscle to use. You're not firing your glutes at all."
            him "Of course I am! I can feel it!"
            bo "Can you? Lift up, and while you're at the top, consciously squeeze just your glutes. Nothing else."
            scene black with dissolve
            "She lifts and squeezes, trying it once more with your advice in mind."
            scene himawari_glutes_up_concerned_cg_v4 with dissolve:
                xalign 0.5 yalign 1.0
            show himawari_glutes_up_concerned_cg_v4:
                subpixel True
                easein 3 yalign 0.5
            him "What about n-"
            bo "Nope. I can see your hamstrings and lower back compensating. You're cheating."
            him "I'm NOT CHEATING!" with vpunch
            bot "Checkmate. She's now completely on the defensive, desperate to prove herself on a test I invented and which she can never pass."
            $ hima_diagnosis_activation = True
            jump hima_glute_bridge_menu

        "{color=[obediencecolor]}Your core is unstable.{/color}" if hima_diagnosis_stability and hima_diagnosis_lift:
            # UNLOCKED BY THE STABILITY 'FAILURE'.
            bo "Your instability is the most dangerous flaw. It has to be corrected. I'll have to hold you in place to force your body to learn what a stable position feels like."
            scene black with dissolve
            "You kneel beside her, your shadow falling over her."
            scene boruto_holding_her_hips_cg with dissolve:
                xalign 0.5 yalign 1
            show boruto_holding_her_hips_cg:
                subpixel True
                easein 3 yalign 0.5
            him "Hold me in place? What does that-"
            bot "The pretext is established. Her diagnosed 'instability' requires my hands on her."
            bo "You feel that [hin_rel]? That's where your hips need to be."
            him "O-okay, I get it, now get your hands off me!"
            jump hima_glute_guide_hips

        "{color=[obediencecolor]}????{/color}" if not hima_diagnosis_stability or not hima_diagnosis_lift:
            "If I keep telling her what she's doing wrong she'll probably be less resistant to my other plans..."
            jump hima_glute_bridge_menu

        "{color=[dominancecolor]}You're not creating the necessary mind-muscle connection.{/color}" if hima_diagnosis_activation and hima_diagnosis_lift:
            # UNLOCKED BY THE ACTIVATION 'FAILURE'.
            bo "Your brain isn't connecting with the right muscle. It's a common problem for amateurs. We need to use tactile prompting to create that neural pathway."
            him "Tactile... prompting? That sounds fake."
            bo "It's basic kinesiology. Do you want to fix the problem or not?"
            him "F-fine! Whatever, you nerd!"
            bot "Wrapped the transgression in jargon she can't dispute. She's agreed to be touched because she's too proud to admit she doesn't understand."
            jump hima_glute_tactile_feedback

        "{color=[dominancecolor]}????{/color}" if not hima_diagnosis_activation or not hima_diagnosis_lift:
            "If I keep telling her what she's doing wrong she'll probably be less resistant to my other plans..."
            jump hima_glute_bridge_menu

        "This is pointless. Let's move on.":
            bo "We'll come back to this. Your entire posterior chain is a mess. It needs a lot of work."
            jump hima_training_menu

    # BRANCH 1: Manual Stabilization (The "Safer" Control Path)
    label hima_glute_guide_hips:
        scene black with dissolve
        bo "I don't think you quite get it yet."
        "You kneel and place your hands firmly on her hip bones, caging her in."
        scene boruto_holding_her_cg with dissolve:
            xalign 0.5 yalign 1
        show boruto_holding_her_cg:
            subpixel True
            easein 3 yalign 0.5
        him "Y-your hands are..."
        bo "Focus. Now push up. Feel how I'm keeping you level? This is the stability you're lacking. Your body needs to memorize this."
        himt "He's so close... But my hips... they do feel more stable. Is this really how it works?"
        bot "Controlling her every move. My touch equals 'correctness'. Her body is learning to move to my rhythm."
        call changeObedience("Himawari", 1, "hima_train_glute1", statlevel = 2, max_times=1) from _call_changeObedience_149
        
        menu hima_glute_hip_guidance_menu:
            bo "Don't break form. Feel the pressure building in your muscles."

            "{color=[dominancecolor]}Good. Hold it there.{/color}":
                call checkDominance(30, "hima_glute_hip_guidance_menu") from _call_checkDominance_64
                bo "Perfect. Hold that position. Feel the tension in your glutes?"
                him "I-I can't hold it here much longer, [bo_name], this is too m-"
                scene black with dissolve
                bot "There it is, my excuse to get a better grip!"
                scene boruto_holding_her_cg_v2 with dissolve:
                    xalign 0.5 yalign 1
                show boruto_holding_her_cg_v2:
                    subpixel True
                    easein 3 yalign 0.5
                bo "Dear [him_rel], you think I'll let you fail? I'm here for you! Come on, be tough."
                him "W-where are you t-touching m-"
                bo "That's the feeling of weakness leaving your body. Don't you dare drop until I say so."
                bot "Pure control. Her muscles are screaming, but as long as I can keep feeling her perfect body for just a second longer..."
                call changeDominance(1, "hima_glute_hip_guidance_menu_dialogue", max_times=1) from _call_changeDominance_124
                "As she holds the position in embarrassment, she reluctantly tries to move your hands away from her ass."
                show screen parallax1280("boruto_holding_her_cg_v3", initial_ypos=0.5) with dissolve
                call showscrollingimage from _call_showscrollingimage_254
                him "[bo_name_stutter], your hands are t-"
                bo "What's wrong? You lost tension. Focus. I'm just making sure you're not imbalanced."
                "She freezes, her eyes wide. She doesn't drop, but her breathing is irregular."
                himt "Is he trying to...? No. He's... checking my alignment. It's part of the training. So why does my skin feel like it's on fire?"
                bot "She's too flustered to protest. The boundary has been moved without a single shot fired!"
                call hidescrollingimage2("Click twice to continue.") from _call_hidescrollingimage2_128
                jump hima_glute_hip_guidance_menu

            "Alright, that's enough stabilization.":
                bo "Better. You're starting to understand the movement. Let's move on."
                jump hima_glute_bridge_menu


    # BRANCH 2: Tactile Feedback (The Transgressive "Technical" Path)
    label hima_glute_tactile_feedback:
        menu hima_glute_feedback_options:
            "Time to create that 'neural pathway'."

            "Use your fingers to 'prompt' the muscle.":
                bo "Assume the proper glute bridge position like I showed you earlier."
                scene black with dissolve
                him "O-okay..."
                bo "The target is the gluteus maximus. Right... here."
                $ renpy.sound.play("/audio/soun_fx/grope2.opus",channel="sfx4",loop=False,relative_volume=0.5)
                scene boruto_grope_her_cg with dissolve:
                    xalign 0.5 yalign 1
                show boruto_grope_her_cg:
                    subpixel True
                    easein 3 yalign 0.5
                "Not wasting a second, you get a good hold of her right buttock. She yelps and complains."
                him "Hey! I told you not to do that!"
                bo "I'm not 'doing' anything. I'm prompting the muscle. That's the one I want you to squeeze. If you had done it right the first time, this wouldn't be necessary. Now, squeeze!"
                him "Y-you're grabbing my ass, idiot! You're just straight up grabbing my ass and calling it... 'prompting'!? Are you insane?!"
                bo "Quit whining, I'm trying to help you here. Do it right and I won't have to get physical."
                bot "Yeah... right!"
                $ hima_glute_poked_for_real = True
                jump hima_glute_feedback_options

            "{color=[hatredcolor]}A 'prompt' isn't enough. Use a 'motivational slap'.{/color}" if hima_glute_poked_for_real == True:
                call checkHatred(35, "hima_glute_feedback_options") from _call_checkHatred_43
                bo "The finger prompt was too subtle for you. The neural signal is weak. You need a larger surface area to register the command. A stronger stimulus."
                him "A stronger... stimulus?"
                scene black with dissolve
                "As she lifts her hips again, hesitantly this time, your open palm connects with her strained posterior with a sharp, stinging smack that echoes in the room."
                $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.9)
                scene boruto_grope_her_cg_v2 with dissolve:
                    xalign 0.5 yalign 1.0
                show boruto_grope_her_cg_v2:
                    subpixel True
                    easein 3 yalign 0.5
                him "KYA—!"
                "A bright red handprint blooms on the fabric of her shorts."
                bot "The sound it made... the way her perfect ass jiggled from the impact. Fucking intoxicating."
                bo "THAT is the muscle. Feel it now? That's the one I want you to squeeze. Now do it again."
                himt "WHAT ON EARTH ARE YOU D-" with vpunch
                bo "I said, AGAIN." with vpunch
                $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.9)
                show boruto_grope_her_cg with vpunch    
                "Her body is trembling, a tear of frustration in her eye, but she pushes her hips up again, higher this time."
                "Or was it just the force of your spank?"
                scene black with dissolve
                call changeHatred(1, fromwhere="hima_train_glute_spank", max_times=1) from _call_changeHatred_208
                him "That's IT!! I've had ENOUGH! HOW DARE YOU TOUCH ME LIKE THAT, YOU CREEP!" with vpunch
                # Mark exercise as completed, fail this attempt but unlock next option for next time
                $ hima_glute_spanked = True
                jump himawari_training_kicked_out

            "Let's move on before you hurt yourself.":
                bo "Let's move on. Try to remember that feeling of activation."
                jump hima_training_menu

label hima_training_posture:
    # Phase 1: The Sell. Manipulating her into the position.
    bo "Posture. This one is advanced, for total core and back stabilization. I'm not even sure you're ready for it."
    him "Not ready? I can do anything you can do, loser."
    bot "Predictable. Her pride is a string I can pull any time I want."
    bo "It's not about strength. It's about control and precision. It's called a controlled quadrupedal spinal articulation."
    him "A what-a-pedal what? Just tell me what to do, smartass!"
    him "And quit making words up to sound smart!" 
    himt "But... 'advanced'... I have to prove I can do it."
    bo "Get on all fours. Hands under your shoulders, knees under your hips."
    him "On... all fours!? What do you think I am, some kind of pet!?" with vpunch
    
    menu hima_posture_initial_sell:
        him "On... all fours!? What do you think I am, some kind of pet!?"

        "It's a foundational athletic stance.":
            bo "It's a foundational athletic stance, [him_name]. Or do they not teach you basic kinesiology at your school? If it's too 'advanced' for you, we can stop."
            him "F-fine! I can do it! It's not a big deal."
            scene black with dissolve
            call changeObedience("Himawari", 1, "hima_posture_comply_kinesiology", statlevel=2, max_times=1) from _call_changeObedience_150

        "It's what I told you to do.":
            bo "It's the position your teacher commanded. Are you going to obey, or are you going to waste more of my time?" with vpunch
            him "Tch... You don't have to be such a jerk about it."
            "As her resistance slowly weakens, she gets in position just to get it over with."
            scene black with dissolve
            call changeDominance(1, max_times=1, fromwhere="hima_posture_initial_sell") from _call_changeDominance_125
            
        "Is it too demeaning for you?":
            bo "What's the matter? Is getting on your hands and knees a little too demeaning for the great [him_name]?"
            him "W-what!? Of course not! It's just a dumb stretch!" with vpunch
            bot "Her pride is so easy to weaponize. She just submitted to my request just to spite me..."
            scene black with dissolve
            "Flustered and angry, she immediately gets into position to prove you wrong."
            call changeHatred(1, fromwhere="hima_posture_demean_response", max_times=1) from _call_changeHatred_209

    scene himawari_plank_cg with dissolve:
        xalign 0.5 yalign 1.0
    show himawari_plank_cg:
        subpixel True
        easein 3 yalign 0.7
    bot "Oh yes. On all fours. Like a good little pet."
    bot "But I need to get more... physical."
    bo "Your hands are wrong. Spread your fingers wide to distribute the weight. Your index fingers should be pointing straight ahead."
    him "They *are* straight!"
    bo "And your neck is too high."
    him "Maybe instead of constantly telling me what I'm doing wrong you should specify what the right way is, idiot!"
    bot "Heh. Exactly what I need."
    bo "Sure, but it's easier to just show you than try to describe it."
    him "R-right..."
    scene black with dissolve
    "In the blink of an eye, you move behind her, kneeling down to inspect her form better."
    $ renpy.sound.play("/audio/soun_fx/fast_blink.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    scene himawari_plank_surprised_cg with flash:
        xalign 0.5 yalign 1.0
    show himawari_plank_surprised_cg:
        subpixel True
        easein 3 yalign 0.5
    pause(1.0)
    him "You're... you're too close!"
    himt "I can feel his breath on my legs. I feel so... exposed."
    bot "She can complain all she wants but her body has already been conditioned by my dominance... She won't move!"
    bo "Shut up and hold still. First, I'm placing one hand on your lower back to guide the movement."
    scene black with dissolve
    bo "Take this seriously, I don't wanna hear more whining."
    scene himawari_plank_grope_re_cg with dissolve:
        xalign 0.5 yalign 0.0
    show himawari_plank_grope_re_cg:
        subpixel True
        easein 3 yalign 0.5
    "You place one hand on her back and another on her thigh. She flinches violently but doesn't pull away."
    him "Don't-"
    bo "This is part of the exercise. You need to build strength in your core."
    show screen parallax1280("himawari_plank_grope_re_cg", initial_ypos=0.5, menuenabled=True) with dissolve
    call showscrollingimage from _call_showscrollingimage_255
    him "And your hand helps me do that how exactly?"
    bo "You asked for more specific instructions. This is it. Stop flopping around and hold the position."
    bot "The first point of contact is made. Now time for some good old reverse psychology..."

    menu hima_posture_correction_submenu:
        bot "The first point of contact is made. Now time for some good old reverse psychology..."

        "You've lost your chance to learn.":
            bo "You know what? Forget it. You're unteachable. You flinch, you resist, you're too proud to learn."
            him "W-wait!"
            him "I... I'll be still. J-just... show me."
            himt "Why did I say that!? Why do I care what he thinks!? It's that stupid throbbing in my head again..."
            bot "And there it is. The poison works its magic. She craves the relief of submission."
            bo "Fine. But this is your last chance. Do not move."
            show screen parallax1280("blackscreen",1.0,1.0,menuenabled=False) with dissolve
            scene black
            call hidescrollingimage2("Click twice to continue.") from _call_hidescrollingimage2_129
            jump hima_posture_place_second_hand

label hima_posture_place_second_hand:
    scene black with dissolve
    "You take advantage of the moment to place your other hand squarely on her ass."
    scene himawari_plank_grope_re_cg_v2 with dissolve:
        xalign 0.5 yalign 1
    show himawari_plank_grope_re_cg_v2:
        subpixel True
        easein 3 yalign 0.5
    $ renpy.sound.play("/audio/soun_fx/himawari/himagasp2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    him "*Gasp*!"
    himt "His hand! It's right on my... H-He can't... This isn't training! But... my hips aren't moving anymore. Was he r-right?!"
    bot "The pretext of 'stabilization' is the ultimate shield. She can't argue with results, even if the method is a violation."
    call changeObedience("Himawari", 1, "hima_train_posture_stabilize", statlevel=2, max_times=1) from _call_changeObedience_151
    him "Okay, I get it now, get your hands off me!" with vpunch
    bo "Are you sure?"
    him "Let me do it alone!"
    scene black with dissolve
    bo "Let's see it then."
    scene himawari_plank_guide_cg with dissolve:
        xalign 0.5 yalign 0.5
    show himawari_plank_guide_cg:
        subpixel True
        easein 3 yalign 1.0
    bo "Better than before, now do the movement."
    him "M-movement?"
    bo "What, you thought all you have to do is plank on the floor for a few seconds?"
    bo "Anyone can do that!"
    him "I can b-barely just hold this position, I don't think I can move."
    bot "She's subconsciously begging for my help again..."
    bo "Maybe you could use a little bit of help then, I guess you are a slow learner unless guided."
    scene himawari_plank_guide_bor_cg with dissolve
    bo "Now, from this position, you have to get your butt a little bit lower to fully engage your abs."
    him "H-how much lower?"
    bot "Wow, she didn't even complain about my hand on her thigh. That's a first!"
    show himawari_plank_guide_bor_cg_v2 with dissolve
    $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
    bo "Right down to about here..."
    him "H-hey, stop, what are you d-"
    bo "Now keep repeating this motion."
    show v21_himawari_plank_updown
    bo "Slowly arch up... and now, slowly sag down..."
    bo "Feel the rhythm? This is what perfect form feels like."
    him "Stop making it harder! Why are you pushing against my thighs?"
    bo "You have to resist my pressure. This is how you build strength through the entire range of motion."
    bot "Yes... push back into me. That's a good girl."
    bo "Don't get lazy, keep going!"
    him "[bo_name], I said stop. Seriously."

    menu posture_ending_menu:
        "Threaten to spank her for poor performance.":
            bo "This is pathetic, your form is weak and you wanna quit already? Keep going or I'll give you some real 'tactile feedback' to remember."
            him "Wh-what...?"
            bo "You heard me. Arch your back perfectly, or I'll spank you so hard you won't sit for a week. Your choice."
            scene black with dissolve
            him "I SAID STOP!!!" with hpunch
            "Not wanting to permanently damage your relationship with her, you spare her, standing up and leaving her on the map."
            scene himawari_scared_cg with dissolve:
                xalign 0.5 yalign 1.0
            "She stays on all fours for a moment, trembling."
            himt"Is this really what I have to go through to get... 'stronger'?"
            bo "I said get up. Or have you grown comfortable in that position?"
            bot "There it is. Submission born not from grudging respect, but from pure terror."
            if dominance.level == 1:
                $ dominance.level += 1
                $ dominance.value = 0
                $ hima_dominance_adv1_hatred_complete = True
                $ notification("Your dominance level has reached level 2! The stat has been reset to 0.")
            bo "Remember this feeling [him_name]. This is the feeling of improvement. We'll continue your training soon."
            him "Get. Out."
            scene black with vpunch
            "She gathers herself, and quickly kicks you out, clearly shaken by what just happened."
            $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx2", loop=False, relative_volume = 0.9)
            "The door slams shut so hard the frame rattles."
            bot "She'll remember, alright. She'll remember who's in charge from now on."
            $ hima_competition_full_clear = True
            jump action_taken

#==============================================================================
# Generic failure label
#==============================================================================

label himawari_training_kicked_out:
    
    scene himawari_angry_cg with Dissolve(0.2):
        xalign 0.5 yalign 1
    show himawari_angry_cg:
        subpixel True
        easein 0.2 yalign 0.5

    him "I can't believe I was stupid enough to trust you! Get out of my room! NOW!"
    bo "It was just a joke, calm down!"
    him "GET OUT!" with vpunch

    scene black with vpunch
    $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx2", loop=False, relative_volume = 0.9)
    "The door slams shut so hard the frame rattles."
    bot "Well... that could have gone better."

    jump action_taken




screen peeking12801024(baseImage):
    on "show" action Function(mark_screen_image_gallery, baseImage)
    key "K_SPACE" action Return()

    # The viewport will automatically size its scrollable area
    # to fit the content inside it.
    viewport:
        # Allows you to drag the image around.
        draggable True
        # Optional: Defines scroll speed when the mouse is at the edge.
        edgescroll (300, 300)
        # Start the view slightly off-center for a better initial effect.
        xinitial 0.1
        yinitial 0.1

        # This frame holds the wobbling and zoomed image.
        # It ensures everything is centered properly.
        frame:
            background None
            xalign 0.5
            yalign 0.5

            # Add the image and apply the zoom directly.
            # The viewport will see the new, larger size of the zoomed image
            # and create the peeking/panning area automatically.
            add baseImage:
                at smooth_peek_wobble
                zoom 1.3 # Adjust this zoom factor to your liking
                subpixel True

    # This button makes the whole screen clickable to exit.
    button:
        action Return()
        style "empty"