# Initialize defaults for new session
label initialize_swimsuit_defaults_love:
    $ hima_swimsuit_pose_simple = False
    $ hima_chose_simple_1 = False
    $ hima_chose_simple_2 = False
    $ hima_chose_simple_3 = False
    $ hima_chose_simple_4 = False
    $ hima_swimsuit_pose_simple_rear_1 = False
    $ hima_swimsuit_pose_simple_rear_2 = False
    $ hima_swimsuit_pose_sitting = False
    $ hima_chose_sitting_1 = False
    $ hima_chose_sitting_2 = False
    $ hima_chose_sitting_3 = False
    $ hima_chose_sitting_4 = False
    $ hima_swimsuit_pose_sexy = False
    $ hima_chose_sexy_1 = False
    $ hima_chose_sexy_2 = False
    $ hima_chose_sexy_3 = False
    $ hima_chose_sexy_4 = False
    $ hima_chose_sexy_5 = False
    $ hima_chose_sexy_6 = False
    $ hima_chose_sexy_7 = False
    $ hima_swimsuit_shots_taken = 0
    return

label hima_swimsuit_modelling_check_love:
    # Check prerequisites other than love/hate choice (handled in room)
    # Check outfit first
    $ vixenslureinv = inventory.find_item_by_name("Bikini")
    if vixenslureinv == None:
        bo"You know, about our modelling sessions, I was thinking we could try something a little different, something more professional-"
        show hima shy with dissolve
        him"Different? What are you planning now, [bo_name]?"
        bot"Whoops... I need to actually buy it first."
        bo "Just... think about it, for next time. The best models are versatile, and I know you can be one of the best."
        bot"I should check the shop. I want to find something that will really show everyone how amazing she is."
        jump himastretchingsetupsprites
    elif vixenslureinv!= None:
        $ player_owns_vixens_lure = True
    # Outfit check passed. Owns outfit but not enough obedience
    if (himawari_obedience.value < 20 and himawari_obedience.level==1):
        show hima shy with dissolve
        him"Another shoot? You really seem to enjoy this 'director' thing, don't you?"
        bo"Only because you're such a great model, [him_name]. You're getting better every time."
        show hima smug2 with dissolve
        him"Well, obviously. I'm the star here."
        bo"You are. And stars deserve to shine their brightest. The photos we have are great, but I think we can create something... truly special. Something that will get you noticed."
        show hima worried2 with dissolve
        him"Special? What do you have in mind?"
        bo"I invested in a new outfit for you. It's high-fashion, designed to highlight your amazing physique."
        scene black with dissolve
        "You gently pull out the bikini, presenting it to her."
        scene v021_hima_swimsuit_give_outfit with dissolve:
            xalign 0.5 yalign 1.0
        show v021_hima_swimsuit_give_outfit:
            subpixel True
            easein 3 yalign 0.9
        bo"Ta-da!"
        him"ARE YOU KIDDING ME!? That's... it's so tiny! You want me to wear THAT?" with vpunch
        call checkObedience(20,"none","Himawari") from _call_checkObedience_55
        him"No way! I... I can't wear something so revealing!" with vpunch
        scene black with dissolve
        $ renpy.sound.play("/audio/soun_fx/spank5.opus",channel="sfx4",loop=False,relative_volume=0.5)
        "[him_name] pushes the bikini away, her face bright red, before running out of the room."
        bot"I pushed too hard, too soon. She's not ready for this yet."
        "Increase her obedience to 35 first before suggesting this."
        jump action_taken
    # Owns outfit, has enough obedience, but didn't complete regular photoshoot twice
    elif hima_model_repeat_count < 2:
        bo"You know, about our modelling sessions, I was thinking we could try something a little different, something more professional-"
        show hima shy with dissolve
        him"Different? What are you planning now, [bo_name]?"
        bot"Whoops... I need to actually buy it first."
        bo "Just... think about it, for next time. The best models are versatile, and I know you can be one of the best."
        him"I... I don't know, [bo_name]. That sounds... embarrassing."
        bot"Maybe if we do a few more of our regular photoshoots, she'll build up the confidence for it. I have to be patient."
        jump himastretchingsetupsprites
    
    # All conditions passed
    elif ((himawari_obedience.value>=20 and himawari_obedience.level==1) or himawari_obedience.level>1) and player_owns_vixens_lure and hima_model_repeat_count >= 2 and (chosen_hate_path == True or chosen_love_path == True):
        jump hima_swimsuit_modelling_start_love
    else: # Fallback fail scenario in case of different conditions combination
        "Increase her obedience to 35, have a couple of photoshoots with her and acquire a new special outfit for her before suggesting this."
        jump himastretchingsetupsprites

label hima_swimsuit_modelling_start_love:

    # First-Time Persuasion Dialogue
    if hima_swimsuit_first_time:
        if hima_model_swimsuit_repeat_count == 0:
            $ hima_model_swimsuit_repeat_count +=1
        him"Another shoot? You really seem to enjoy this 'director' thing, don't you?"
        call checkObedience(20,"none","Himawari") from _call_checkObedience_56
        him"But... I guess it's for a good cause."
        show boruto smirk with dissolve
        $ notification ("Quest updated")
        $ quest.check("1_bohim_3","completed")
        $ quest.check("2_bohim_3","in progress")
        bot"She's trying so hard to be brave about this. I'm proud of her..!"
        if tsunade_discovery_seen == True: 
            bot"But knowing what I know now about my... 'juice'... I have to be careful. I don't want to hurt her. I just want... to help her see her own potential."
        bo"You're a natural at it. So good, in fact, that I think you're ready to take the next step. To the kind of level Yoruichi works at. More professional... more artistic."
        show hima worried2 with dissolve
        himt"Yoru? She's so graceful and beautiful... I could never be like her."
        show hima smugshy with dissolve
        show hima at smallshake
        him"*Hmph!* What do you mean m-more artistic?"
        bot"Comparing her to Yoruichi was the right move. She looks up to her so much..."
        show hima at smallshake
        him"You aren't planning anything weird, are you...?"
        show boruto laughing with dissolve
        bo"I believe you have just as much potential as Yoruichi. To prove it, to everyone, and to yourself, we need to show them what you're capable of."
        bo"So, I got you a gift. Think of it as an investment... in your future."
        show hima shy with dissolve
        him"A gift? For me?"
        scene black with dissolve
        "You gently pull out the bikini, presenting it to her."
        scene v021_hima_swimsuit_give_outfit with dissolve:
            xalign 0.5 yalign 1.0
        show v021_hima_swimsuit_give_outfit:
            subpixel True
            easein 3 yalign 0.9
        him"ARE YOU KIDDING ME!? That's... it's so tiny! You want me to wear THAT?" with vpunch
        him"N-no way! I... I can't walk around in something so... r-revealing!"
        show v021_hima_swimsuit_give_outfit at smallshake:
            subpixel True
            yalign 0.5
        bot"I knew this would be hard for her. I have to show her this isn't about being lewd, it's about art... and helping our family."
        bo"This is what high-fashion modeling is, [him_name]. It's about showing the beauty of the human form. It's about confidence. It's what professionals like Yoruichi do."
        him"But... it's practically nothing! How is this professional?"
        bo"It's about art, confidence, and market appeal. You have the strong, beautiful body of an athlete, [him_name]. You have a youthful energy that Yoruichi doesn't. That's special."
        bo"It would be a shame not to celebrate that. You want to help [hin_rel], right? Is a little shyness going to stand in the way of that?"
        scene black with dissolve
        "She bites her lip, her gaze flickering between the bikini and your earnest face. Her fists clench, torn between her embarrassment and the sincerity in your words."
        if day_part == 3: 
            scene himawari_bedroom_2
        else:
            scene himawari_bedroom_1
        show hima smugshy at right:
            zoom 0.34
        show boruto smirk at left
        with dissolve
        him"F-fine! But if you say ONE weird thing, or look at me in any way that isn't 'professional', I swear I'll..."
        bo"I promise, this will be completely professional. You have my word. Now, go get changed. The light is perfect right now."
        show hima mad with dissolve
        him"Ughh... F-fine, don't rush me!"
        show boruto laughing with dissolve
        bo"Take all the time you need."
        show hima mad
        with dissolve
        show hima:
            easeout 1 xpos 2000
        $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.8)
        him"Hmph!" with vpunch
        scene black with dissolve
        him"Don't just stand there, dummy! Give me some privacy to change into this thing!" with vpunch
        if hima_swimsuit_first_time == True:
            $ notification(f"{him_name}'s Bikini outfit unlocked!")
        bot"She's so brave... She's really going to do it. I have to make sure I don't let her down."
        $ hima_swimsuit_first_time = False

    # Repeatable Entry (Non-First Time)
    else:
        if hima_swimsuit_groped: # This branch comes from the Hatred payment option, so the dialogue reflects a break in trust.
            show boruto sceeming with dissolve
            bo"Hey, about that swimsuit photoshoot..."
            show hima mad3 at right with easeinright
            him"After what you did to me last time?"
            him"I don't think so. Not unless you can prove you'll treat me with respect this time."
            bo"You're right, I messed up. I'm sorry. We can still do good work together."
            him"Words are cheap. You used me."
            him"I'm not doing anything unless you pay me $50 upfront, as a sign of good faith."
            show boruto angry with dissolve
            bot"Damn it, I broke her trust... I have to earn it back."
            menu payupfront_photoshoot_love:
                bot"Damn it, I broke her trust... I have to earn it back."
                "Give her the $50.":
                    if money >= 50:
                        bo"You're right. Here. I promise I'll be better this time. I'll be professional."
                        call changeMoney(-50) from _call_changeMoney_29
                        him"Hmph... This is your last chance."
                        # reset grope flag so they don't get stuck in -$50 permanently to do photoshoot
                        $ hima_swimsuit_groped = False
                        show hima:
                            easeout 1 xpos 2000
                        scene black with dissolve
                        "She heads off to change, her expression still wary, but willing to give you another chance."
                        jump hima_swimsuit_modelling_love_begin
                    else:
                        bot"I don't have enough money to prove I'm serious. I messed up."
                        jump himastretchingmenu
                "I can't afford that right now.":
                    show boruto sceeming with dissolve
                    bo"I can't afford that right now, [him_name]. I'm sorry."
                    him"Then I guess we're done here. Come back when you can treat me like a partner, not a tool."
                    jump himastretchingmenu

        show hima smugshy at right with easeinright
        him"Ready for another session, 'Director'? I hope you appreciate the trust I'm putting in you."
        bo"I do. More than you know. Are you ready? Let's go make some art."
        if hima_swimsuit_not_paid == True:
            him"That's what you said last time, but you didn't pay me. It hurt, [bo_name]."
            show boruto angry with dissolve
            bo"I know, and I'm sorry. Things were tight. I promise I'll make it right. The only way to do that is to take even better pictures that are guaranteed to sell."
            him"You're lucky I'm doing this for [hin_rel]'s sake... and because a small part of me still trusts you."
            show boruto sceeming with dissolve
            bot"I'll make it up to her. I swear it. We'll do such great work, she'll see this was all worth it."
            show hima:
                easeout 1 xpos 2000
            scene black with dissolve
            "She heads off to change, her movements filled with a hesitant hope."
        else:
            show hima worried2 with dissolve
            him"Ugh, that tiny thing again? Okay... but let's make it quick. It's still a little embarrassing."
            himt"But... there's a part of me that's almost... excited? No, that's silly. It's just... I like working with him."
            bot"She's getting more comfortable. She trusts me. That feeling... it's more valuable than any photo."
            show hima:
                easeout 1 xpos 2000
            scene black with dissolve
            "She heads off to change, a small, almost imperceptible smile on her face."

    # Photoshoot Begins
    label hima_swimsuit_modelling_love_begin:
    $ initialize_replay_defaults()
    call initialize_swimsuit_defaults_love from _call_initialize_swimsuit_defaults_love
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/dooropen.opus", channel="sfx1", loop=False, relative_volume = 0.5)
    "[him_name] calls you in, after changing into the bikini..."
    scene bg modelling with dissolve
    show bhima shy at center with dissolve
    "She looks shy but determined, trying to cover herself while also holding her head high. She meets your gaze for a moment before looking away, blushing."
    bo"You look... amazing, [him_rel]."
    show bhima at smallshake
    him"D-don't say that! Can we just... start?"
    bo"Of course. Take a deep breath. Let's start with something simple."
    bot"She's so beautiful. The way she's trying to be brave... it's captivating. I have to do right by her and capture this perfectly."

    label hima_swimsuit_repeatable_menu_love:
        if hima_swimsuit_shots_taken >= 3:
            jump hima_swimsuit_ending_love

        hide screen camera_ui
        hide screen camera1280
        scene bg modelling
        show bhima embarrassed at center
        with dissolve
        him"So? What's next, director?"
        if hima_swimsuit_shots_taken == 0:
            bo"Just warming up. Let's get started."
            him"Heh. Well, let's see what you've got in mind then."
        menu hima_swimsuit_repeatable_menu_menu_love:
            bot"What pose would best capture her spirit?"
            "Simple Shots" if not hima_swimsuit_pose_simple: 
                $ hima_swimsuit_shots_taken += 1
                if hima_chose_simple_1 == True and hima_chose_simple_2 == True and hima_chose_simple_3 == True:
                    $ hima_swimsuit_pose_simple = True # Hide entire menu if all simple shots already taken in this session
                jump hima_swimsuit_simple_shots_love
            "{color=[obediencecolor]}Sitting Poses{/color}" if (himawari_obedience.level >= 2 and not hima_swimsuit_pose_sitting) or (himawari_obedience.value == 23 and himawari_obedience.level == 1 and not hima_swimsuit_pose_sitting):
                $ hima_swimsuit_shots_taken += 1
                call checkObedience(statvalue=23, jumpvalue="none", character="Himawari", statlevel=1) from _call_checkObedience_57
                if hima_chose_sitting_1 == True and hima_chose_sitting_2 == True and hima_chose_sitting_3 == True:
                    $ hima_swimsuit_pose_sitting = True # Hide entire menu if all simple shots already taken in this session
                jump hima_swimsuit_sitting_shots_love
            "{color=[obediencecolor]}Sexy Shots{/color}" if ((himawari_obedience.value >= 3 and himawari_obedience.level == 2) or himawari_obedience.level>2) and not hima_swimsuit_pose_sexy:
                $ hima_swimsuit_shots_taken += 1
                call checkObedience(statvalue=3, jumpvalue="none", character="Himawari", statlevel=2) from _call_checkObedience_58
                if hima_chose_sexy_1 == True and hima_chose_sexy_2 == True and hima_chose_sexy_3 == True:
                    $ hima_swimsuit_pose_sexy = True # Hide entire menu if all simple shots already taken in this session
                $ call_label_action("hima_swimsuit_sexy_shots_love")
                call supp_rew from _call_supp_rew_19
                jump hima_swimsuit_repeatable_menu_menu_love
            # Sitting poses locked
            "{color=[obediencecolor]}???{/color}" if himawari_obedience.value < 23 and himawari_obedience.level == 1:
                call checkObedience(statvalue=23, jumpvalue="hima_swimsuit_repeatable_menu_menu_love", character="Himawari") from _call_checkObedience_59
                jump hima_swimsuit_repeatable_menu_love
            # Sexy poses locked
            "{color=[obediencecolor]}???{/color}" if himawari_obedience.level < 2 or (himawari_obedience.level == 2 and himawari_obedience.value < 3):
                call checkObedience(statvalue=3, jumpvalue="hima_swimsuit_repeatable_menu_menu_love", character="Himawari", statlevel=2) from _call_checkObedience_60
                jump hima_swimsuit_repeatable_menu_love
            "Wrap it up for today.":
                jump hima_swimsuit_ending_love


# --- SIMPLE SHOTS ---
label hima_swimsuit_simple_shots_love:
    if hima_swimsuit_shots_taken == 1:
        bo"Let's ease into it. Just some basic poses to warm up."
        him"O-okay... like what?"
    elif hima_swimsuit_shots_taken == 2:
        bo"Just follow my lead. You're doing perfectly."
        $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.8)
        him"Hmph! Well, of course I am." with vpunch
    else:
        pass
    menu:
        "Frontal shots." if not (hima_chose_simple_1 and hima_chose_simple_2 and hima_chose_simple_3 and hima_chose_simple_4):
            menu:
                "Stand tall, try to look natural!" if not hima_chose_simple_1:
                    $ hima_chose_simple_1 = True
                    bo"Let's start here. Stand against the wall, and just try to relax. Project that confidence I know you have."
                    call changeObedience(character="Himawari", amount=1, fromwhere="v21_swimsuit_simple_1_love", max_times=1) from _call_changeObedience_171
                    scene v21_hima_modelstart1 with dissolve:
                        xalign 0.5 yalign 0.95
                    show v21_hima_modelstart1:
                        subpixel True
                        easein 3 yalign 0.2
                    bo"You look a little nervous! It's okay. Just look at me through the lens."
                    him"I... I'm not a professional like Yoruichi..."
                    him"She's done this so many times. I'm just getting s-started..."
                    bo"And you're already amazing."
                    him"S-stop that..." with vpunch
                    bot"That blush... she's so stunning. I need to capture this."
                    himt"He really thinks I'm good at this... I have to try my best!"
                    bo"All that training has given you such a strong presence. Just hold that pose... perfect."
                    show screen camera1280("v21_hima_modelstart1_1", 1, 0.0)
                    show screen camera_ui("Himawari_swimsuit", False)
                    with dissolve
                    show screen camera_ui("Himawari_swimsuit")
                    $ ui.interact()
                    bo"Beautiful. Let's move on."
                    him"`Beautiful`? Y-you're not just saying that?"
                    bo"I wouldn't lie about something like this."
                    him"Oh... O-okay then! Let's do another!"
                    jump hima_swimsuit_repeatable_menu_love
                "Side profile, hand on hip." if not hima_chose_simple_2:
                    $ hima_chose_simple_2 = True
                    bo"Turn to the side. Hand on your hip. Chin up. Show me a strong profile."
                    him"Okay..."
                    scene side normal 3_a with dissolve: # variations not used so far: side normal 2_a, side normal 3_b, side normal_a
                        xalign 0.5 yalign 0.95
                    show side normal 3_a:
                        subpixel True
                        easein 3 yalign 0.2
                    call changeObedience(character="Himawari", amount=1, fromwhere="v21_swimsuit_simple_2_love", max_times=1) from _call_changeObedience_172
                    him"This feels a little silly."
                    bot"With every pose she agrees to, she seems to open up a little more. It's like watching a flower bloom."
                    bo"You look like a model. There's a difference. Hold it."
                    show screen camera1280("side normal 3_a", 1, 0.0)
                    show screen camera_ui("Himawari_swimsuit", False)
                    with dissolve
                    show screen camera_ui("Himawari_swimsuit")
                    $ ui.interact()
                    bo"Excellent. Next."
                    him"Y-you really think so? I'm not used to this kind of praise..."
                    him"L-let's just get this done!"
                    bo"Whatever you say, star."
                    jump hima_swimsuit_repeatable_menu_love
                "Try to look more innocent." if not hima_chose_simple_3:
                    $ hima_chose_simple_3 = True
                    bo"Okay, for this one, drop the serious look. Give me something softer. A little vulnerability. Let them see the gentle side of you."
                    him"That's not... really me."
                    scene frontal pose 4_a with dissolve: # variations not used so far: frontal pose 2_a, frontal pose 2_a_closeup, frontal pose 3_a, frontal pose 3_b, frontal pose 3_b_closeup, frontal pose_a
                        xalign 0.5 yalign 0.95
                    show frontal pose 4_a:
                        subpixel True
                        easein 3 yalign 0.2
                    him"What's the point of a pose like this?"
                    bo"Innocence has a beauty all its own. Your gentle side is just as powerful as your strong side."
                    call changeObedience(character="Himawari", amount=1, fromwhere="v21_swimsuit_simple_3_love", max_times=1) from _call_changeObedience_173
                    him"I... I guess that makes sense. But it's still embarrassing..."
                    bo"It's about telling a story with the photo. Now hold still, you look lovely."
                    show screen camera1280("frontal pose 4_a", 1, 0.0)
                    show screen camera_ui("Himawari_swimsuit", False)
                    with dissolve
                    show screen camera_ui("Himawari_swimsuit")
                    $ ui.interact()
                    bo"That's a keeper. Really sweet."
                    him"Sweet? What's that supposed to mean?"
                    bo"It means it's a side of you not many people get to see. I feel lucky to capture it."
                    him"W-what?! I-it's just a pose, dummy!"
                    bo"Right, just a pose."
                    him"S-stop smirking! What are you thinking?!"
                    bo"Nothing, nothing."
                    jump hima_swimsuit_repeatable_menu_love
                "Think of a pose you would like!" if not hima_chose_simple_4:
                    $ hima_chose_simple_4 = True
                    bo"Okay, I think you've learned a lot from our sessions. How about you show me a pose you think would look great?"
                    him"I.. I don't know if I can, but I'll t-try..."
                    bo"I know you can do it."
                    scene frontal pose 3_a with dissolve:
                        xalign 0.5 yalign 0.95
                    show frontal pose 3_a:
                        subpixel True
                        easein 3 yalign 0.2
                    him"How about t-this?"
                    show screen camera1280("frontal pose 3_a", 1, 0.0)
                    show screen camera_ui("Himawari_swimsuit", False)
                    with dissolve
                    show screen camera_ui("Himawari_swimsuit")
                    $ ui.interact()
                    bo"That's... perfect, [him_name]. Absolutely perfect."
                    himt"H-he likes it!"
                    bo"See? You're a natural! All that hard work you put into your training really shows."
                    him"Y-you really think so? It's not just... you being nice?"
                    bo"I'm serious."
                    him"...Thank you."
                    bo"But... I think we can make it even better. Let me just check the angle up close."
                    hide screen camera_ui
                    hide screen camera1280
                    scene black with dissolve
                    him"H-hey! Don't get too close, okay?"
                    scene frontal pose 3_b with dissolve:
                        xalign 0.5 yalign 0.95
                    show frontal pose 3_b:
                        subpixel True
                        easein 3 yalign 0.2
                    bo"Relax, I'm just doing my job. Making sure you look your best."
                    bot"Wow... up close, she's even more breathtaking. I need to keep my cool... be professional."
                    him"Well? What do you think? Are you just going to stare?"
                    bo"Sorry... I was just... you were right. This pose is perfect. Everything looks... perfect."
                    him"Hmph! Of course it is!"
                    bot"Especially that look of pride on her face."
                    show screen camera1280("frontal pose 3_b", 1, 0.0)
                    show screen camera_ui("Himawari_swimsuit", False)
                    with dissolve
                    bot"That shy confidence... it makes her even more beautiful."
                    show screen camera_ui("Himawari_swimsuit")
                    $ ui.interact()
                    bo"Amazing!"
                    him"O-okay, you can back up now, dummy!"
                    bo"Right, sorry."
                    jump hima_swimsuit_repeatable_menu_love
        "Rear shots." if not (hima_swimsuit_pose_simple_rear_1 and hima_swimsuit_pose_simple_rear_2):
            menu:
                "Turn around, let's see a rear shot." if not hima_swimsuit_pose_simple_rear_1:
                    $ hima_swimsuit_pose_simple_rear_1 = True
                    bo"Okay, let's try a rear shot. It's a very classic modelling pose."
                    him"Y-you're not just trying to stare at my butt, are you?"
                    bo"I'm trying to take a photo that highlights your athletic form. Every professional model does these."
                    him"Hmph, fine, but I'll know if you're looking anywhere other than the camera!"
                    scene rear shot 3_a with dissolve:
                        xalign 0.5 yalign 0.95
                    show rear shot 3_a:
                        subpixel True
                        easein 3 yalign 0.2
                    him"Ummm..."
                    bo"That's it, that's perfect. Just hold that."
                    show screen camera1280("rear shot 3_a", 1, 0.0)
                    show screen camera_ui("Himawari_swimsuit", False)
                    with dissolve
                    show screen camera_ui("Himawari_swimsuit")
                    $ ui.interact()
                    bo"That's it! Perfect!"
                    bo"Now, what if you added a little of your personality to it?"
                    hide screen camera_ui
                    hide screen camera1280
                    him"P-personality? What does that even mean?"
                    bo"Come on, [him_name], you know what I'm talking about."
                    bo"Just be yourself. Let that fiery spirit show."
                    scene rear shot 2_b with dissolve:
                        xalign 0.5 yalign 0.95
                    show rear shot 2_b:
                        subpixel True
                        easein 3 yalign 0.2
                    him"L-like this...?"
                    bo"Wow, hold it right there!"
                    show screen camera1280("rear shot 2_b", 1, 0.0)
                    show screen camera_ui("Himawari_swimsuit", False)
                    with dissolve
                    show screen camera_ui("Himawari_swimsuit")
                    bo"I knew you had it in you, [him_name]!"
                    him"What's that supposed to mean?"
                    bo"That you're a natural! You always know just how to make a pose your own."
                    him"W-well... I guess I am pretty cool."
                    bo"You are. I'm just here to help you show it to the world."
                    jump hima_swimsuit_repeatable_menu_love
                "Turn around and stand on your tiptoes" if not hima_swimsuit_pose_simple_rear_2:
                    $ hima_swimsuit_pose_simple_rear_2 = True
                    bo"Okay, a true model knows how to accentuate their best features."
                    him"W-what do you mean?"
                    bo"I need you to turn around, and try balancing on your tiptoes. It really defines the leg muscles."
                    him"My feet? What do they have to do with anything?"
                    bo"Trust me, it's a pro trick. Just try it."
                    him"Something like this...?"
                    scene rear shot_a with dissolve:
                        xalign 0.5 yalign 0.95
                    show rear shot_a:
                        subpixel True
                        easein 3 yalign 0.2
                    bot"Wow, that pose really does... everything. She looks incredible."
                    bo"See what I'm talking about? See how it makes your legs and glutes look so strong and defined?"
                    him"STOP TALKING ABOUT MY BUTT AND TAKE THE PICTURE ALREADY!" with vpunch
                    show screen camera1280("rear shot_a", 1, 0.0)
                    show screen camera_ui("Himawari_swimsuit", False)
                    with dissolve
                    bo"Okay, okay, I'm trying to get the best angle."
                    bot"Her flustered reactions are so cute."
                    show screen camera_ui("Himawari_swimsuit")
                    $ ui.interact()
                    bo"There we go!"
                    bo"The more we work together, the faster we can get these done."
                    him"You're the one who keeps distracting me by saying embarrassing things!"
                    bo"Do you want to create amazing art or not?"
                    him"I... I guess."
                    bo"Then trust your director."
                    jump hima_swimsuit_repeatable_menu_love
            
# --- SITTING POSES ---
label hima_swimsuit_sitting_shots_love:
    if hima_swimsuit_shots_taken == 1:
        bo"Alright, let's try some sitting poses."
        him"Okay. I trust you."
        bot"She's really starting to trust me. I can't betray that."
        bo"These will create a different mood. More thoughtful. You ready?"
    elif hima_swimsuit_shots_taken == 2:
        bo"You seem like you're getting into it! Are you, maybe, even having a little fun?"
        him"J-just tell me what's next, dummy!"
        bo"Alright, alright, my brilliant model."
        him"S-stop it!"
    menu:
        "Choose a pose:"
        "One leg extended." if not hima_chose_sitting_1:
            $ hima_chose_sitting_1 = True
            bo"Sit against the wall, one leg extending forward."
            scene sitting pose 3_a with dissolve: # variations not used so far: sitting pose 2_a, sitting pose 2_b, sitting pose 2_c
                xalign 0.5 yalign 0.95
            show sitting pose 3_a:
                subpixel True
                easein 3 yalign 0.2
            him"This feels so... elegant."
            bot"Elegant. That's the perfect word for her."
            call changeObedience(character="Himawari", amount=1, fromwhere="v21_swimsuit_sitting_1_love", max_times=1, statlevel=2) from _call_changeObedience_174
            bo"That's the point. It shows off the design and your long lines. Hold it."
            show screen camera1280("sitting pose 3_a", 1, 0.0)
            show screen camera_ui("Himawari_swimsuit", False)
            with dissolve
            show screen camera_ui("Himawari_swimsuit")
            $ ui.interact()
            bo"Perfect. That pose radiates confidence."
            himt"He thinks I look... confident?"
            him"W-well, I am a confident person! S-so there!"
            bo"I know you are. That's why these photos are so good."
            bo"Anyway..."
            jump hima_swimsuit_repeatable_menu_love
        "Knees up, legs together." if not hima_chose_sitting_2:
            $ hima_chose_sitting_2 = True
            bo"Now bring your knees together, and give me a soft look, right at the camera."
            scene sitting pose 4_a with dissolve: # variations not used so far: sitting pose 4_b, sitting pose 4_c
                xalign 0.5 yalign 0.95
            show sitting pose 4_a:
                subpixel True
                easein 3 yalign 0.2
            him"Are you looking right at the lens? Nowhere else?"
            himt"Why is my heart beating so fast? Just focus... focus on the camera..."
            bot"She's so focused on trusting me. I have to live up to it. I'll only look through the lens."
            call changeObedience(character="Himawari", amount=1, fromwhere="v21_swimsuit_sitting_2_love", max_times=1, statlevel=2) from _call_changeObedience_175
            bo"My focus is on the shot. Just hold the pose."
            show screen camera1280("sitting pose 4_a", 1, 0.0)
            show screen camera_ui("Himawari_swimsuit", False)
            with dissolve
            show screen camera_ui("Himawari_swimsuit")
            $ ui.interact()
            bo"That's a killer shot."
            him"Hmph. You better not be just saying that."
            bo"I'm just doing my job, which is making you look as amazing as you are."
            bo"Anyway..."
            jump hima_swimsuit_repeatable_menu_love
        "Face away from me, sit on your butt." if not hima_chose_sitting_3:
            $ hima_chose_sitting_3 = True
            bo"Now turn away from me, sit down, and look back over your shoulder."
            scene sitting pose 5_a with dissolve: # variations not used so far: sitting pose 5_b, sitting pose 5_closeup, sitting pose 5_front, sitting pose 5_relax, sitting pose 5_shy
                xalign 0.5 yalign 0.95
            show sitting pose 5_a:
                subpixel True
                easein 3 yalign 0.2
            him"This is a little embarrassing... my back is so exposed."
            bot"Her vulnerability is beautiful, not something to be exploited. It's a sign of her trust in me."
            call changeObedience(character="Himawari", amount=1, fromwhere="v21_swimsuit_sitting_3_love", max_times=1, statlevel=2) from _call_changeObedience_176
            bo"It's a classic pose for a reason. It highlights your strong back. Own it."
            show screen camera1280("sitting pose 5_a", 1, 0.0)
            show screen camera_ui("Himawari_swimsuit", False)
            with dissolve
            show screen camera_ui("Himawari_swimsuit")
            $ ui.interact()
            bo"Fantastic. You look so graceful when you're not scowling at me."
            him"Can you just give a normal compliment for once?"
            bo"Oh, so you want my compliments now, huh?"
            him"W-what, NO! Dummy, that's not what I meant."
            bo"Sure..."
            jump hima_swimsuit_repeatable_menu_love
        "Face towards me, sit on your butt." if not hima_chose_sitting_4:
            $ hima_chose_sitting_4 = True
            bo"Now sit down on the floor while facing me."
            him"Sounds easy enough!"
            bo"Let's see it then."
            scene sitting pose 5_front with dissolve:
                xalign 0.5 yalign 0.95
            show sitting pose 5_front:
                subpixel True
                easein 3 yalign 0.2
            him"This feels... more vulnerable than I thought it would."
            him"And it's because you're just standing there staring! Get behind the camera and take the picture."
            bo"Sorry, I was just checking to see if the pose felt natural. As the director, I need to make sure you're comfortable."
            him"J-just take the picture!"
            show screen camera1280("sitting pose 5_front", 1, 0.0)
            show screen camera_ui("Himawari_swimsuit", False)
            with dissolve
            bo"Here we go..!"
            show screen camera_ui("Himawari_swimsuit")
            $ ui.interact()
            bo"Perfect!"
            him"Great, so can I get up n-"
            hide screen camera_ui
            hide screen camera1280
            bo"Actually, there's one little adjustment."
            him"You just said it was perfect!"
            bo"The pose is perfect, but the angle could be even better."
            him"So move then."
            scene black with dissolve
            "You start walking towards her."
            him"W-what are you doing? Don't get too close!"
            bo"Relax, I just need a different perspective for the shot."
            scene sitting pose 5_closeup with dissolve:
                xalign 0.5 yalign 0.95
            show sitting pose 5_closeup:
                subpixel True
                easein 3 yalign 0.2
            him"A d-different perspective? It just looks like you're trying to look down my top! H-how is this better?"
            bo"It's not about that, dear [him_rel]."
            bot"Okay, maybe it is a little, but..."
            bo"It's about capturing your expression from a more intimate angle. It shows vulnerability. It's artistic! Stay right there."
            show screen camera1280("sitting pose 5_closeup", 1, 0.0)
            show screen camera_ui("Himawari_swimsuit", False)
            with dissolve
            him"Hurry up!!"
            show screen camera_ui("Himawari_swimsuit")
            $ ui.interact()
            bo"There we go."
            him"N-now back away!"
            bo"You did great, this one is going to be a masterpiece!"
            jump hima_swimsuit_repeatable_menu_love

# --- SEXY SHOTS ---


# --- ENDING ---
label hima_swimsuit_ending_love:
    if himawari_obedience.level == 1 and hima_swimsuit_shots_taken == 0:
        "We should probably take at least one picture with [him_name] to successfully complete the advancement event!"
    elif himawari_obedience.level == 1 and hima_swimsuit_shots_taken > 0:
        $ himawari_obedience.level += 1
        $ himawari_obedience.value = 0
        $ notification(f"{him_name}'s obedience level has reached level 2! The stat has been reset to 0.")
    bo"See? That was great, wasn't it?"
    hide screen camera_ui
    hide screen camera1280
    scene black
    with dissolve
    $ renpy.sound.play("/audio/soun_fx/footsteps.opus", channel="sfx1", loop=False, relative_volume = 1.5)
    "As you call 'wrap', [him_name] walks up to you, looking exhausted but proud."
    scene bg modelling
    show bhima angry at center
    show boruto surprised at left
    with dissolve
    him"SO, 'DIRECTOR', WHERE'S MY PAY?"
    show boruto laughing with dissolve
    bo"Right here! And I have to say, you were amazing today."
    if quest_him.is_state("him2L_1", "pending") or quest_him.is_state("him2L_1", "in progress"):
        $ notification (f"{him_name} Love hidden objective completed")
        $ quest_him.check("him2L_1", "completed")
    him"I was pretty good, wasn't I? So pay up. We're done."
    bo"As promised. Your payment for a truly professional session."
    $ renpy.end_replay()
    menu swimsuitpayment_love:
        "How do you handle payment?"

        "{color=[lovecolor]}Give her $50{/color}" if money >= 50: # Convert this to a love only option where she'll get a little bit 'emotional' after you encourage her and thank her for her contribution or some shit. It'll result in an extra hugging cg where the MC may decide to cop a fell or not.
            label lovetestswimsuit_love:
            call changeMoney(-50) from _call_changeMoney_30
            show boruto normal with dissolve
            bot"Despite pushing her out of her comfort zone, she did her best and she delivered."
            show boruto laughing with dissolve
            bo"As promised, [him_name]. Here's your payment. You deserve it."
            show bhima normal with vpunch
            him"F-fifty dollars? [bo_name], are you sure about this? Where do you even find this kind of money?"
            call changeLove("Himawari", 1) from _call_changeLove_79
            show boruto embarassed with dissolve
            bo"You know, some of this, some of that... W-well, most of it is just me working at the ramen shop really!"
            show bhima shy with dissolve
            him"How is that going by the way, do you like it?"
            menu:
                him"How is that going by the way, do you like it?"
                "It's a fucking nightmare.":
                    show boruto sad2 with dissolve
                    bo"It's a fucking nightmare."
                    bo"Grinding day in, day out, for a few bucks to help you and [hin_rel]..."
                    show boruto embarassed with dissolve
                    bo"But you know, that's also exactly why it's worth it!"
                    him"R-really? And you're giving me your hard earned money from it?"
                "I.. yeah, sure it's really fun!":
                    bo"I.. yeah, sure it's really fun!"
                    him"You don't sound very convincing."
                    bo"Why are you asking anyway, don't worry, I'm making money."
                    him"But you're working hard for it."
                    him"And then giving it to me just for a few pictures..."
            show boruto laughing2
            bo"You deserve it, [him_name]. I know what you did today wasn't as easy for you as you made it look."
            bo"I also know sometimes it can feel weird, even awkward, letting your [him_rel_to_bo] see you like th-"
            scene black with dissolve
            "Before managing to finish your sentence, she suddenly pounces you."
            $ renpy.sound.play("/audio/soun_fx/pin.opus",channel="sfx4",loop=False,relative_volume=0.5)
            scene v021_hima_swimsuit_hug with dissolve:
                yalign 0.0
            show v021_hima_swimsuit_hug:
                easein 3 yalign 0.5
            bo"[him_name]..."
            show screen parallax1280("v021_hima_swimsuit_hug", initial_ypos=0.5) with dissolve
            call showscrollingimage from _call_showscrollingimage_276
            him"[bo_name], you are the best [him_rel_to_bo] ever!"
            bo"Heh.. I try...!"
            bo"But remember, we're not done yet, you can achieve so much more in this industry!"
            bo"I believe in you!"
            call hidescrollingimage() from _call_hidescrollingimage_221
            bot"She's my [him_rel] but..."
            bot"Damn it, she's so close to me... And with that bikini..."
            "In a vulnerable moment of hesitation, your mind begins to wander..."
            menu:
                "What do you do?"
                "{color=[impulsecolor]}Cop a feel.{/color}":
                    if first_time_hima_peek:
                        "Although you've learned to control it, your curse still lingers."
                        "At times, you may succumb to your {color=[impulsecolor]}Impulse{/color}, but be careful..."
                        "Letting the curse uncontrollably feast upon your impulses may lead to catastrophic outcomes."
                        "If your impulses grow too strong, visit Kushina in your dreams. She will know how to assist you."
                        $ first_time_hima_peek = False
                    bot"Maybe... I could just..."
                    $ renpy.sound.play("/audio/soun_fx/grabsound.opus",channel="sfx4",loop=False,relative_volume=0.5)
                    scene v021_hima_swimsuit_hug_grope with dissolve:
                        yalign 0.0
                    show v021_hima_swimsuit_hug_grope:
                        subpixel True
                        easein 3 yalign 0.5
                    him"[bo_name_stutter]... What are you doing?"
                    bo"What am I-"
                    bo"O-oh! [him_name], I'm so sorry!"
                    show screen parallax1280("v021_hima_swimsuit_hug_grope", initial_ypos=0.5) with dissolve
                    scene black
                    bo"I don't know how my hand-"
                    him"Then... maybe move it, idiot!"
                    bo"It was just, I thought I saw something on your..!"
                    him"Ohh! Did you get it off?!"
                    bo"I t-think so."
                    bot"I'd better not keep pushing it, or she'll realize what's going on."
                    call hidescrollingimage2() from _call_hidescrollingimage2_149                    
                "Don't.":
                    call changeRespect("Himawari", 3) from _call_changeRespect_265
                    pass
            scene black with dissolve
            pause 1.0
            scene bg modelling
            show bhima normal at center
            show boruto normal at left
            with dissolve
            him"Thanks for your support, [bo_name]."
            him"I appreciate it, even if you act like an idiot sometimes."
            show boruto embarassed with dissolve
            bo"I'll do my best to be more... normal, next time, I guess!"
            show boruto normal with dissolve
            bo"But I also wanted to thank you, [him_name]. You went out of your comfort zone to help make more money and help [hin_rel]."
            bo"You're a great [him_rel]!"
            him"T-thank you, [bo_name]."
            $ hima_swimsuit_not_paid = False
            jump action_taken
        "Give her $30" if money >= 30:
            bot"The standard rate. It's fair, and it shows her that her hard work is valued. We're partners in this."
            show boruto smirk with dissolve
            bo"Here's your pay. You earned every bit of it today."
            call changeMoney(-20) from _call_changeMoney_31
            show bhima shy with dissolve
            him"Thanks, [bo_name]."
            call changeRespect("Himawari", 1) from _call_changeRespect_266
            bo"If we keep working together like this, I know we can make even more next time. You were a star."
            bot"This is good. Building a partnership based on trust and shared success. We can accomplish anything together."
            scene black with dissolve
            "[him_name] takes the money and leaves, a thoughtful smile on her face."
            $ hima_swimsuit_not_paid = False
            jump action_taken
        "{color=[hatredcolor]}Short-change her ($20){/color}" if money >= 20: # hatred exclusive option. MC will tease her with the money, 'beckoning' for her to reach for it.
            if chosen_hate_path:
                call checkHatred(30,"swimsuitpayment_love") from _call_checkHatred_49
            bot"This is the best option. The ultimate mindfuck. Degrade her completely, then spit in her face with this insulting payment."
            bot"Lock her into a cycle of desperate rage. She'll have to come back to 'earn' what she's 'owed'. She'll be my perfect, angry little puppet."
            bo"Market's tough. I don't think there's much money left to give you. What do you think about something like 20 bucks?"
            call changeRespect("Himawari", -5) from _call_changeRespect_267
            show bhima angry with dissolve
            him"Twenty bucks? TWENTY!? After what you just made me do!?"
            show boruto sceeming2 with dissolve
            bo"That was a test, [him_name]. To see if you had what it takes. The real payment comes when we deliver the full set. I promise."
            bot"Oh, you'll get what you deserve. You'll get exactly what you deserve."
            call changeHatred(2, max_times=1, fromwhere="shortchange_love") from _call_changeHatred_215
            him"You promised me payment and I'll get my payment, idiot!"
            bo"I did, but I never said how much, did I?"
            show boruto sceeming3 with dissolve
            bo"Besides, if you want your money that bad..."
            scene black with dissolve
            bo"Prove it."
            bo"Come and get it little [him_rel]!"
            stop music fadeout 1
            $ renpy.sound.play("/audio/soun_fx/bassstart.opus",channel="sfx1",loop=False,relative_volume=0.5)
            $ renpy.sound.play("/audio/soun_fx/introbass3.opus",channel="sfx2",loop=True,relative_volume=0.7)
            scene v021_hima_swimsuit_hold_money with dissolve:
                yalign 0
            show v021_hima_swimsuit_hold_money:
                subpixel True
                easein 3 yalign 0.3 zoom 1.1
            bo"You want it, don't you?"
            show v021_hima_swimsuit_hold_money:
                subpixel True
                easein 0.5 yalign 0.2 zoom 1.2
            bo"It's right here!"
            scene black with dissolve
            "Suddenly, before you manage to get in another word..."
            $ renpy.sound.play("/audio/soun_fx/scuffle.opus",channel="sfx3",loop=False,relative_volume=0.7)
            scene v021_hima_swimsuit_reach_money with dissolve:
                yalign 0
            show v021_hima_swimsuit_reach_money:
                subpixel True
                easein 3 yalign 0.3
            bo"Not so fast, [him_name]."
            him"Ughh, give it to me, you creep! I worked for it!"
            show screen parallax1280("v021_hima_swimsuit_reach_money", zoom=1.25, initial_ypos=0.3) with dissolve
            scene black
            call showscrollingimage from _call_showscrollingimage_277
            him"You..promised!!"
            call hidescrollingimage2("Click twice to overpower her!") from _call_hidescrollingimage2_150
            scene black with dissolve
            bo"[him_name]..."
            $ renpy.sound.play("/audio/soun_fx/pin.opus",channel="sfx4",loop=False,relative_volume=0.5)
            pause 1.0
            scene v021_hima_swimsuit_reach_money_2 with dissolve:
                yalign 0
            show v021_hima_swimsuit_reach_money_2:
                subpixel True
                easein 3 yalign 0.6
            bo"You forget I'm stronger than you, don't you?" with vpunch
            $ renpy.sound.play("/audio/soun_fx/grope2.opus",channel="sfx4",loop=False,relative_volume=0.5)
            him"L-let me go, creep!"
            bo"Let you go? You put your hands on me first! I didn't realize you wanted me that bad!"
            show screen parallax1280("v021_hima_swimsuit_reach_money_2", zoom=1.25, initial_ypos=0.6) with dissolve
            scene black
            call showscrollingimage from _call_showscrollingimage_278
            bo"In fact, I would even go as far as to say that... the feeling is mutual, my dear [him_rel]."
            call hidescrollingimage("Click twice to go a little bit easier on her.") from _call_hidescrollingimage_222
            scene black with dissolve
            "You release the pressure from one of her wrists just enough to let her regain her balance, as she desperately attempts to push you off."
            scene v021_hima_swimsuit_slide_hand with dissolve:
                yalign 1.0
            show v021_hima_swimsuit_slide_hand:
                subpixel True
                easein 3 yalign 0.8
            $ renpy.sound.play("/audio/soun_fx/grope1.opus",channel="sfx4",loop=False,relative_volume=0.3)
            him"W-what are you doing?! GET YOUR FILTHY HANDS OFF ME [bo_name]!"
            $ hima_swimsuit_groped = True
            bo"Maybe if you ask nicely."
            show v021_hima_swimsuit_slide_hand:
                subpixel True
                easein 0.5 yalign 0.4
            him"[bo_name], stop this, please!"
            menu:
                him"[bo_name], stop this, please!"
                "Squeeze her ass":
                    show v021_hima_swimsuit_slide_hand:
                        subpixel True
                        easein 0.5 yalign 0.9
                    bo"Stop what? I'm not doing anything."
                    bo"I was just thinkin-"
                    scene black with dissolve
                    bo"Oh my lord!!" with vpunch
                    him"W-what?" with vpunch
                    bo"There's a bug!!"
                    him"WHAT! WHERE?!" with vpunch
                    bo"Right..."
                    scene v021_hima_swimsuit_squeeze_ass with flash:
                        yalign 0.0
                    show v021_hima_swimsuit_squeeze_ass:
                        subpixel True
                        easein 3.0 yalign 0.7
                    $ renpy.sound.play("/audio/soun_fx/grabsound.opus",channel="sfx4",loop=False,relative_volume=0.5)
                    bo"HERE!" with vpunch
                    show screen parallax1280("v021_hima_swimsuit_squeeze_ass", zoom=1.25, initial_ypos=0.7) with dissolve
                    scene black
                    call showscrollingimage from _call_showscrollingimage_279
                    him"GET YOUR HANDS OFF ME, CREEP!"
                    him"YOU THINK I'LL FALL FOR THAT?!"
                    call hidescrollingimage2("Press twice to let her go.") from _call_hidescrollingimage2_151
                    bo"I swear there was a bug I just wasn't sure on which side of your a-"
                    scene black with dissolve
                    $ renpy.sound.play("/audio/soun_fx/spank5.opus",channel="sfx4",loop=False,relative_volume=0.5)
                    stop sfx1
                    stop sfx2
                    stop sfx3
                    him"LET GO!" with vpunch
                    bo"OWWW!" with vpunch
                "Let her go":
                    bo"Relax, I'm not doing anything."
                    "You slowly release the pressure and allow her to break off your hold."
                    scene black with dissolve
                    him"What on earth has gotten into you?!"
            scene v021_hima_swimsuit_end_angry with dissolve:
                yalign 1.0
            show v021_hima_swimsuit_end_angry:
                subpixel True
                easein 3 yalign 0.35
            him"I should have never agreed to this!" with vpunch
            bo"Before you say or do anything else you'll regret, here's your money. Twenty bucks, as we agreed."
            call changeMoney(-20) from _call_changeMoney_32
            stop sfx1
            stop sfx2
            stop sfx3
            stop sfx4
            $ playmusic("audio/ost/house2.opus",0.6)
            scene black with dissolve
            him"If you ever do anything like this again..."
            scene bg modelling
            show bhima embarrassed at right
            show boruto sceeming2 at left
            with dissolve
            bo"What? You don't wanna keep making money?"
            him"Hmph!"
            bo"That's what I thought. You'd better work a little bit on being more cooperative next time."
            him"Get out of my sight!"
            bot"I got what I wanted anyway..."
            bot"For now!"
            $ hima_swimsuit_not_paid = False
            jump action_taken
        "I am strapped for cash, sorry!":
            show boruto sad with dissolve
            bo"On second thought... I just checked my pockets and..."
            bo"There's nothing in them!" with vpunch
            show bhima angry with dissolve
            him"What? Then why did you promise me money?!"
            show bhima at smallshake
            him"You made me do all of that... for nothing!?"
            bo"It's not for nothing, [him_name]! It's practice!"
            bo"I'm sorry, I promise I'll make it up to you as soon as possible."
            call changeRespect("Himawari", -5) from _call_changeRespect_268
            him"You'd better! Or else forget about repeat sessions."
            scene black with dissolve
            $ renpy.sound.play("/audio/soun_fx/footsteps.opus", channel="sfx1", loop=False, relative_volume = 1.5)
            "[him_name] storms out, looking betrayed."
            bo"At least put your clothes on first, you'll catch a cold!"
            him"SHUT UP!!!" with hpunch
            $ hima_swimsuit_not_paid = True
            jump action_taken