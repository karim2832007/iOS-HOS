# Total points to earn:
# himawari_obedience
# Level 1 - 3 points
# Level 2 - 3 points
# hatred
# Level 1 - 1 point
# Flags to track pose usage and session progress.
default hima_swimsuit_pose_simple = False
default hima_swimsuit_pose_sitting = False
default hima_swimsuit_pose_sexy = False
default hima_swimsuit_first_time = True
default hima_swimsuit_shots_taken = 0
default hima_model_swimsuit_repeat_count = 0
default player_owns_vixens_lure = False # Item "Bikini" from shop - price has been adjusted to 100.
default hima_swimsuit_not_paid = False
default hima_swimsuit_groped = False
default hima_chose_simple_1 = False
default hima_chose_simple_2 = False
default hima_chose_simple_3 = False
default hima_chose_simple_4 = False
default hima_swimsuit_pose_simple_rear_1 = False
default hima_swimsuit_pose_simple_rear_2 = False
default hima_chose_sitting_1 = False
default hima_chose_sitting_2 = False
default hima_chose_sitting_3 = False
default hima_chose_sitting_4 = False
default hima_chose_sexy_1 = False
default hima_chose_sexy_2 = False
default hima_chose_sexy_3 = False
default hima_chose_sexy_4 = False
default hima_chose_sexy_5 = False
default hima_chose_sexy_6 = False
default hima_chose_sexy_7 = False
# Initialize defaults for new session
label initialize_swimsuit_defaults:
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

label hima_swimsuit_modelling_check:
    # Check prerequisites other than love/hate choice (handled in room)
    # Check outfit first
    $ vixenslureinv = inventory.find_item_by_name("Bikini")
    if vixenslureinv == None:
        bo"You know, about our modelling sessions, I was thinking we could try it with a different outfit, something like-"
        show hima shy with dissolve
        him"Different outfit? You're really pushing it with this 'director' thing, aren't you?"
        bot"Wait a second... I didn't even buy it yet!"
        bo "Just... think about it, for next time. Models have to try different things to progress!"
        bot"I should go check the shop and look for the most revealing outfit I can find! Next time I'll be ready."
        jump himastretchingsetupsprites
    elif vixenslureinv!= None:
        $ player_owns_vixens_lure = True
    # Outfit check passed. Owns outfit but not enough obedience
    if (himawari_obedience.value < 20 and himawari_obedience.level==1):
        show hima shy with dissolve
        him"Another shoot? You're really milking this 'director' thing, aren't you?"
        bo"You're damn right. You're getting good, [him_name]. Real good."
        show hima smug2 with dissolve
        him"Obviously. I'm the star here. You're just the guy with the camera."
        bo"True, but stars need to shine brighter to get noticed. The photos we've got are solid, but we need something... bold. Something that screams 'pay up.'"
        show hima worried2 with dissolve
        him"Bold? What are you scheming now?"
        bo"I invested in a new outfit. High-end, designed to show off every curve, every angle."
        scene black with dissolve
        "You pull out the bikini, waving it in her face as an invitation."
        scene v021_hima_swimsuit_give_outfit with dissolve:
            xalign 0.5 yalign 1.0
        show v021_hima_swimsuit_give_outfit:
            subpixel True
            easein 3 yalign 0.9
        bo"Tada!!"
        him"ARE YOU KIDDING ME!? This is basically underwear! You expect me to wear THIS?" with vpunch
        call checkObedience(20,"none","Himawari") from _call_checkObedience_49
        him"No way, you perv! I'm not parading around like some... some slut!" with vpunch
        scene black with dissolve
        $ renpy.sound.play("/audio/soun_fx/spank5.opus",channel="sfx4",loop=False,relative_volume=0.5)
        "[him_name] slaps the bikini out of your hands and storms out."
        bot"What a whiny bitch!"
        "Increase her obedience to 35 first before suggesting this."
        jump action_taken
    # Owns outfit, has enough obedience, but didn't complete regular photoshoot twice
    elif hima_model_repeat_count < 2:
        bo"You know, about our modelling sessions, I was thinking we could try it with a different outfit, something like-"
        show hima shy with dissolve
        him"Different outfit? You're really pushing it with this 'director' thing, aren't you?"
        bot"Wait a second... I didn't even buy it yet!"
        bo "Just... think about it, for next time. Models have to try different things to progress!"
        him"In your dreams, loser. Like I would ever wear that and pose for you."
        bot"To wear something like this... I guess she needs to get a little bit more confidence from our regular photoshoots."
        jump himastretchingsetupsprites
    
    # All conditions passed
    elif ((himawari_obedience.value>=20 and himawari_obedience.level==1) or himawari_obedience.level>1) and player_owns_vixens_lure and hima_model_repeat_count >= 2 and (chosen_hate_path == True or chosen_love_path == True):
        jump hima_swimsuit_modelling_start
    else: # Fallback fail scenario in case of different conditions combination
        "Increase her obedience to 35, have a couple of photoshoots with her and acquire a new special outfit for her before suggesting this."
        jump himastretchingsetupsprites

label hima_swimsuit_modelling_start:

    # First-Time Persuasion Dialogue
    if hima_swimsuit_first_time:
        if hima_model_swimsuit_repeat_count == 0:
            $ hima_model_swimsuit_repeat_count +=1
        him"Another shoot? You're really pushing it with this 'director' thing, aren't you?"
        call checkObedience(20,"none","Himawari") from _call_checkObedience_50
        him"But hey! As long as it makes me more money!"
        show boruto snob with dissolve
        $ notification ("Quest updated")
        $ quest.check("1_bohim_3","completed")
        $ quest.check("2_bohim_3","in progress")
        bot"The little bitch thinks she's got this all figured out. A few easy photoshoots and she acts like a star. Little does she know..."
        if tsunade_discovery_seen == True: 
            bot"I've got other plans for you, [him_name]! A little more exposure to my 'poison' and I'll have you wrapped around my finger... or my cock! Hehe..."
        bo"Well, you're getting good at it. So good in fact, that the I think you may be ready to take this to the next level! A level similar to Yoruichi's work. More professional. More... lucrative."
        show hima worried2 with dissolve
        him"Yoru? The beautiful purple haired lady! I still don't believe she works for you..."
        show hima smugshy with dissolve
        show hima at smallshake
        him"*Hmph!* What do you mean m-more lucrative?"
        bot"I knew that'd hit a soft spot! She's looking up to Yoruichi..."
        show hima at smallshake
        him"You aren't scheming anything stupid, are you? You creep..."
        show boruto snob with dissolve
        bo"I believe you are capable of matching Yoruichi's talents, but to confirm my hypothesis, you are going to have to prove yourself first."
        bo"And so, I've prepared a gift, and an investment... in you!"
        show hima shy with dissolve
        him"A gift!? What's this supposed to be?"
        scene black with dissolve
        "You pull out the bikini, waving it in her face as an invitation."
        scene v021_hima_swimsuit_give_outfit with dissolve:
            xalign 0.5 yalign 1.0
        show v021_hima_swimsuit_give_outfit:
            subpixel True
            easein 3 yalign 0.9
        him"ARE YOU KIDDING ME!? This is basically underwear! You expect me to wear THIS?" with vpunch
        him"No way, you perv! I'm not parading around for you like some... some s-slut!"
        show v021_hima_swimsuit_give_outfit at smallshake:
            subpixel True
            yalign 0.5
        bot"But that's exactly what the goal is my dear [him_rel]... And after you were so kind to help taste my 'recipe', sooner or later you'll be exactly that, my slut!"
        bo"What did you think modeling entailed, hm? The entire premise is to make items more desirable with your youthful, athletic looks. This is what professional models do, what Yoru does!"
        him"It's... it's practically nothing! How is this even professional?"
        himt"Ugh, my head is starting to throb again. Why do I always feel so agitated when I argue with him lately? It's like... a weird itch under my skin."
        bo"It's about form, confidence, and market appeal. You have the body of an athlete, [him_name]. You may not be as fit as Yoru, but you are certainly younger, and that sells!." 
        bo"It's a waste not to capitalize on it. You want to help [hin_rel], right? Or are you going to let your pride stand in our way?"
        scene black with dissolve
        "She bites her lip, glancing at the bikini, then at you. Her fists clench, torn between her fury and the cold, hard truth of your words."
        if day_part == 3: 
            scene himawari_bedroom_2
        else:
            scene himawari_bedroom_1
        show hima smugshy at right:
            zoom 0.34
        show boruto sceeming at left
        with dissolve
        him"F-fine! But ONE weird comment, one look that's not 'professional', and I swear to god I'll..."
        show boruto angry with dissolve
        bo"You'll do as you're told, don't think that just because I'm your [him_rel_to_bo] you can argue. This is a professional set. Now go change. Don't waste my time."
        show hima mad with dissolve
        him"Ughh... Careful with that tone, idiot!"
        show boruto sceeming with dissolve
        bo"I'll take that as a 'yes sir'."
        show boruto sceeming3
        show hima mad
        with dissolve
        show hima:
            easeout 1 xpos 2000
        $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.8)
        him"Hmph!" with vpunch
        scene black with dissolve
        him"Don't just stand there, idiot! Give me some space if I am to change into this thing!" with vpunch

        bot"That's a good girl... You better start obeying my word, you little brat!"
        if hima_swimsuit_first_time == True:
            $ notification(f"{him_name}'s Bikini outfit unlocked!")
        $ hima_swimsuit_first_time = False

    # Repeatable Entry (Non-First Time)
    else:
        if hima_swimsuit_groped:
            show boruto sceeming with dissolve
            bo"About that swimsuit photoshoot..."
            show hima mad3 at right with easeinright
            him"After what you did to me last time?"
            him"Not a chance, creep. At least not without knowing it's worth my time for sure this time."
            bo"You already know it's worth it. We're making money!"
            him"We? You gave me chump change. You're using me!"
            him"I'm not doing anything unless you give me $50 right off the bat."
            show boruto angry with dissolve
            bot"God damn it, she's getting overconfident..."
            menu payupfront_photoshoot:
                bot"God damn it, she's getting overconfident..."
                "Give her the $50.":
                    if money >= 50:
                        bo"Fine. Here you go. Now you better do as I say and not complain every second."
                        call changeMoney(-50) from _call_changeMoney_25
                        him"Hmmph! I'll do as I please."
                        # reset grope flag so they don't get stuck in -$50 permanently to do photoshoot
                        $ hima_swimsuit_groped = False
                        show hima:
                            easeout 1 xpos 2000
                        scene black with dissolve
                        "She heads off to change, her grumbling noticeably less intense than the last time."
                        jump hima_swimsuit_modelling_hatred_begin
                    else:
                        bot"I don't have enough money, damn it!"
                        jump himastretchingmenu
                "You wish, golddigger.":
                    show boruto sceeming with dissolve
                    bo"You wish, golddigger."
                    him"In that case get lost loser!"
                    jump himastretchingmenu

        show hima smugshy at right with easeinright
        him"Back for another round, 'Director'? Hope you've got my money ready."
        bo"Money comes after the work. You know the drill. Get into the outfit I got you."
        if hima_swimsuit_not_paid == True:
            him"That's what you said last time and you never paid me, you creep!"
            show boruto angry with dissolve
            bo"Either you're gonna do as I say, or you're gonna stay poor forever. What other choice do you have? Your body is the only thing you got going for you."
            him"Just so you know, working with you is hell on earth! I am only doing this for [hin_rel]'s sake."
            show boruto sceeming with dissolve
            bot"You keep telling yourself that! In due time, you'll be doing much more than posing for me!"
            show hima:
                easeout 1 xpos 2000
            scene black with dissolve
            "She heads off to change, her grumbling noticeably less intense than the last time."
        else:
            show hima worried2 with dissolve
            him"Ugh, that goddamn thing again? Fine, but you better make this quick. I hate wearing it."
            himt"But... there's a part of me that's almost... relieved? No, that's stupid. I hate this. I hate him."
            bot"She hates it, but she's complying much faster. The association is forming: obedience equals relief from the withdrawal she can't even identify. Perfect."
            show hima:
                easeout 1 xpos 2000
            scene black with dissolve
            "She heads off to change, her grumbling noticeably less intense than the last time."

    # Photoshoot Begins
    label hima_swimsuit_modelling_hatred_begin:
    $ initialize_replay_defaults()
    call initialize_swimsuit_defaults from _call_initialize_swimsuit_defaults
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/dooropen.opus", channel="sfx1", loop=False, relative_volume = 0.5)
    "[him_name] calls you in, after changing into the bikini..."
    scene bg modelling with dissolve
    show bhima shy at center with dissolve
    "She looks uncomfortable, like a cornered animal. Her arms trying to cover her body, as she avoids your gaze."
    bo"Looking good, little [him_rel]!"
    show bhima at smallshake
    him"S-shut up! Can we just... get this over with?"
    bo"Relax. You're on the clock. Let's start simple."
    bot"She's putting on a good show. The blushing, the shame... it's all part of the act. I bet she's eating this up inside. She just needs me to give her the excuse to enjoy it."

    label hima_swimsuit_repeatable_menu:
        if hima_swimsuit_shots_taken >= 3:
            jump hima_swimsuit_ending

        hide screen camera_ui
        hide screen camera1280
        scene bg modelling
        show bhima embarrassed at center
        with dissolve
        him"So? What's next? My patience is wearing thin."
        if hima_swimsuit_shots_taken == 0:
            bo"We haven't even started yet..."
            him"Yeah well, you better make this worth my time!"
        menu hima_swimsuit_repeatable_menu_menu:
            bot"I wonder what I should ask of her next..."
            "Simple Shots" if not hima_swimsuit_pose_simple: 
                $ hima_swimsuit_shots_taken += 1
                if hima_chose_simple_1 == True and hima_chose_simple_2 == True and hima_chose_simple_3 == True:
                    $ hima_swimsuit_pose_simple = True # Hide entire menu if all simple shots already taken in this session
                jump hima_swimsuit_simple_shots
            "{color=[obediencecolor]}Sitting Poses{/color}" if (himawari_obedience.level >= 2 and not hima_swimsuit_pose_sitting) or (himawari_obedience.value == 23 and himawari_obedience.level == 1 and not hima_swimsuit_pose_sitting):
                $ hima_swimsuit_shots_taken += 1
                call checkObedience(statvalue=23, jumpvalue="none", character="Himawari", statlevel=1) from _call_checkObedience_51
                if hima_chose_sitting_1 == True and hima_chose_sitting_2 == True and hima_chose_sitting_3 == True:
                    $ hima_swimsuit_pose_sitting = True # Hide entire menu if all simple shots already taken in this session
                jump hima_swimsuit_sitting_shots
            "{color=[obediencecolor]}Sexy Shots{/color}" if ((himawari_obedience.value >= 3 and himawari_obedience.level == 2) or himawari_obedience.level>2) and not hima_swimsuit_pose_sexy:
                $ hima_swimsuit_shots_taken += 1
                call checkObedience(statvalue=3, jumpvalue="none", character="Himawari", statlevel=2) from _call_checkObedience_52
                if hima_chose_sexy_1 == True and hima_chose_sexy_2 == True and hima_chose_sexy_3 == True:
                    $ hima_swimsuit_pose_sexy = True # Hide entire menu if all simple shots already taken in this session
                $ call_label_action("hima_swimsuit_sexy_shots")
                call supp_rew from _call_supp_rew_18
                jump hima_swimsuit_repeatable_menu_menu
            # Sitting poses locked
            "{color=[obediencecolor]}???{/color}" if himawari_obedience.value < 23 and himawari_obedience.level == 1:
                call checkObedience(statvalue=23, jumpvalue="hima_swimsuit_repeatable_menu_menu", character="Himawari") from _call_checkObedience_53
                jump hima_swimsuit_repeatable_menu
            # Sexy poses locked
            "{color=[obediencecolor]}???{/color}" if himawari_obedience.level < 2 or (himawari_obedience.level == 2 and himawari_obedience.value < 3):
                call checkObedience(statvalue=3, jumpvalue="hima_swimsuit_repeatable_menu_menu", character="Himawari", statlevel=2) from _call_checkObedience_54
                jump hima_swimsuit_repeatable_menu
            "Wrap it up for today.":
                jump hima_swimsuit_ending


# --- SIMPLE SHOTS ---
label hima_swimsuit_simple_shots:
    if hima_swimsuit_shots_taken == 1:
        bo"Let's ease you into it. Just some basic poses to warm up!"
        him"Like w-what exactly..."
    elif hima_swimsuit_shots_taken == 2:
        bo"Stop complaining and do as I say or we'll be here forever."
        $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.8)
        him"Hmph!" with vpunch
    else:
        pass
    menu:
        "Frontal shots." if not (hima_chose_simple_1 and hima_chose_simple_2 and hima_chose_simple_3 and hima_chose_simple_4):
            menu:
                "Stand tall, try to look natural!" if not hima_chose_simple_1:
                    $ hima_chose_simple_1 = True
                    bo"Stand against the wall, contrapposto. Hold a natural pose, project some confidence!"

                    bo"You look so stiff! You can at least try to look at the lens..."
                    call changeObedience(character="Himawari", amount=1, fromwhere="v21_swimsuit_simple_1", max_times=1) from _call_changeObedience_165
                    scene v21_hima_modelstart1 with dissolve:
                        xalign 0.5 yalign 0.95
                    show v21_hima_modelstart1:
                        subpixel True
                        easein 3 yalign 0.2
                    him"You can't compare me with h-her..."
                    him"She's an expert, isn't she? I am just getting s-started..."
                    bo"Not too bad!"
                    him"S-shut up..." with vpunch
                    bot"And what a fine body it is. An asset. Better than Yoruichi's, even."
                    himt"He's right though, I have to try my best!"
                    bo"The agency is paying for that natural athleticism of yours. Now hold that pose and stop complaining..."
                    show screen camera1280("v21_hima_modelstart1_1", 1, 0.0)
                    show screen camera_ui("Himawari_swimsuit", False)
                    with dissolve
                    show screen camera_ui("Himawari_swimsuit")
                    $ ui.interact()
                    bo"Acceptable. Let's move on."
                    him"`Acceptable`? What are you, some kind of photo guru?"
                    bo"For all intents and purposes, yes, exactly."
                    him"Ughh... I'm gonna murder you!"
                    jump hima_swimsuit_repeatable_menu
                "Side profile, hand on hip." if not hima_chose_simple_2:
                    $ hima_chose_simple_2 = True
                    bo"Turn to the side. Hand on your hip. Chin up. Give me a strong profile."
                    him"Ugh..."
                    scene side normal 3_a with dissolve: # variations not used so far: side normal 2_a, side normal 3_b, side normal_a
                        xalign 0.5 yalign 0.95
                    show side normal 3_a:
                        subpixel True
                        easein 3 yalign 0.2
                    call changeObedience(character="Himawari", amount=1, fromwhere="v21_swimsuit_simple_2", max_times=1) from _call_changeObedience_166
                    him"I feel like an idiot."
                    bot"Every command she follows erodes her defiance just a little bit more. It's like taming a wild animal."
                    bo"You look like a model. There's a difference. Hold it."
                    show screen camera1280("side normal 3_a", 1, 0.0)
                    show screen camera_ui("Himawari_swimsuit", False)
                    with dissolve
                    show screen camera_ui("Himawari_swimsuit")
                    $ ui.interact()
                    bo"Solid. Next."
                    him"Solid is the pain you'll feel when my fist is up your ass!"
                    him"Stop ordering me around and let's get this over with!"
                    bo"Whew, feisty!"
                    jump hima_swimsuit_repeatable_menu
                "Try to look more innocent." if not hima_chose_simple_3:
                    $ hima_chose_simple_3 = True
                    bo"Drop the glare. Give me something softer. A little vulnerability. Make them want to 'protect' you."
                    him"That's absurd..."
                    scene frontal pose 4_a with dissolve: # variations not used so far: frontal pose 2_a, frontal pose 2_a_closeup, frontal pose 3_a, frontal pose 3_b, frontal pose 3_b_closeup, frontal pose_a
                        xalign 0.5 yalign 0.95
                    show frontal pose 4_a:
                        subpixel True
                        easein 3 yalign 0.2
                    him"What the hell is this supposed to achieve?"
                    bo"Innocence sells, you know. Especially when it's combined with youthful cuteness!"
                    call changeObedience(character="Himawari", amount=1, fromwhere="v21_swimsuit_simple_3", max_times=1) from _call_changeObedience_167
                    him"Spare me your shitty attempts at flattery! This is wholly uncomfortable..."
                    bo"It's marketing. It's what makes the photos appealing. Now hold still and quit chirping."
                    show screen camera1280("frontal pose 4_a", 1, 0.0)
                    show screen camera_ui("Himawari_swimsuit", False)
                    with dissolve
                    show screen camera_ui("Himawari_swimsuit")
                    $ ui.interact()
                    bo"That's a keeper. Not bad."
                    him"Not bad? What's that supposed to mean?"
                    bo"Just makes me wonder what's underneath that whole 'innocence' act..."
                    him"W-what?! You're the one who told me to look innocent!"
                    bo"Exactly, you had to *try* to look innocent!"
                    him"H-huh?! What are you implying, loser?!"
                    bo"Nevermind."
                    jump hima_swimsuit_repeatable_menu
                "Think of a pose you would like!" if not hima_chose_simple_4:
                    $ hima_chose_simple_4 = True
                    bo"Hopefully you learned something from our other sessions. Use that knowledge and come up with a pose that would attract eyes."
                    him"I.. I'm not sure what you have in mind but I'll t-try..."
                    bo"Let's see it then!"
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
                    bo"Not bad, [him_name], not bad at all!"
                    himt"H-he likes it!"
                    bo"Looks like all the time I spent coaching you on posing is finally paying off!"
                    him"Don't try to take credit for my hard work, idiot!"
                    bo"But..."
                    him"...but?"
                    bo"We're not quite there yet. I need to check your posture from a little bit closer to perfect it."
                    hide screen camera_ui
                    hide screen camera1280
                    scene black with dissolve
                    him"Don't you dare be using that shit again as an excuse to creep on me, you pervert!"
                    scene frontal pose 3_b with dissolve:
                        xalign 0.5 yalign 0.95
                    show frontal pose 3_b:
                        subpixel True
                        easein 3 yalign 0.2
                    bo"Be quiet and let me do my job if you want that payment."
                    bot"Oh yes... Indeed, she's got the whole package. Now I just gotta keep making her more... willing, to offer it all to me!"
                    him"I see what you're staring at, you creep! You got anything to say? Otherwise back off and let's get this over with!"
                    bo"No, my dear [him_rel], you were right actually. Everything looks... Perfect."
                    him"Hmph! Of course!"
                    bot"Especially those titties of yours!"
                    show screen camera1280("frontal pose 3_b", 1, 0.0)
                    show screen camera_ui("Himawari_swimsuit", False)
                    with dissolve
                    bot"Look at her... The frustration makes her even sexier!"
                    show screen camera_ui("Himawari_swimsuit")
                    $ ui.interact()
                    bo"Amazing!"
                    him"Now back the hell off, pervert!"
                    bo"Relax, [him_name]."
                    jump hima_swimsuit_repeatable_menu
                    # Added frontal pose 3_a and 3_b
        "Rear shots." if not (hima_swimsuit_pose_simple_rear_1 and hima_swimsuit_pose_simple_rear_2):
            menu:
                "Turn around, let's see a rear shot." if not hima_swimsuit_pose_simple_rear_1:
                    $ hima_swimsuit_pose_simple_rear_1 = True
                    bo"Turn around, let's see a rear shot."
                    him"You're not trying to find more excuses to stare at my ass, are you?!"
                    bo"Stop complaining, every professional model can do a variety of shots. This is one of them."
                    him"Hmph, fine, but don't think I can't see where you're looking!"
                    scene rear shot 3_a with dissolve:
                        xalign 0.5 yalign 0.95
                    show rear shot 3_a:
                        subpixel True
                        easein 3 yalign 0.2
                    him"Ummm..."
                    bo"Perfection, just like that, hold it right there."
                    show screen camera1280("rear shot 3_a", 1, 0.0)
                    show screen camera_ui("Himawari_swimsuit", False)
                    with dissolve
                    show screen camera_ui("Himawari_swimsuit")
                    $ ui.interact()
                    bo"That's it! Perfect!"
                    bo"The only thing I would change is, add a little bit of your attitude in it, you know?"
                    hide screen camera_ui
                    hide screen camera1280
                    him"A-attitude? I'll show you attitude if you keep pushing it!"
                    bo"Come on, [him_name], I'm sure you know what I'm talking about."
                    bo"Give it a try, just be yourself."
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
                    bo"That you're a natural! Why are you always trying to find something bad in what I'm saying?"
                    him"Because I know you're a creep!"
                    bo"I'm trying to help you build your career as a model. Stop complaining."
                    jump hima_swimsuit_repeatable_menu
                    #Added rear shot 3_a, rear shot 2_b (follow up from same choice)

                    
                "Turn around and stand on your tiptoes" if not hima_swimsuit_pose_simple_rear_2:
                    $ hima_swimsuit_pose_simple_rear_2 = True
                    bo"Now, a true model knows how to show off their best assets."
                    him"W-what do you mean?"
                    bo"I need you to turn around, and try balancing on your tiptoes."
                    him"What's my feet got to do with the pose, idiot!"
                    bo"Trust me, you'll see. Just do it."
                    him"Something like this...?"
                    scene rear shot_a with dissolve:
                        xalign 0.5 yalign 0.95
                    show rear shot_a:
                        subpixel True
                        easein 3 yalign 0.2
                    bot"Wow, I didn't even tell her to spread her legs, and she just instinctively does it..!"
                    bo"See what I'm talking about? See how that makes your ass and glutes really stand out?"
                    him"STOP STARING AT MY ASS AND TAKE THE PICTURE ALREADY!" with vpunch
                    show screen camera1280("rear shot_a", 1, 0.0)
                    show screen camera_ui("Himawari_swimsuit", False)
                    with dissolve
                    bo"Calm down, I'm trying to get the best angle."
                    bot"What a crybaby, sheesh."
                    show screen camera_ui("Himawari_swimsuit")
                    $ ui.interact()
                    bo"There we go!"
                    bo"The more quiet you stay the faster we get this over with."
                    him"You're the one who should be quiet, you're getting on my nerves and my patience is running thin!"
                    bo"Do you want to make money or not?"
                    him"I g-guess."
                    bo"Then be quiet."
                    jump hima_swimsuit_repeatable_menu
                    # Added rear shot_a
            


# --- SITTING POSES ---
label hima_swimsuit_sitting_shots:
    if hima_swimsuit_shots_taken == 1:
        bo"Alright, let's try some sitting poses."
        him"Great. More ways to feel exposed."
        bot"Her futile resistance is already wavering. Beautiful."
        bo"More angles for the client. More money for [hin_rel]. Get to it."
    elif hima_swimsuit_shots_taken == 2:
        bo"I see you're finally getting eager! Are you perhaps, even if just a little bit, enjoying this?"
        him"I said shut up and tell me what's next!"
        bo"Good girl, always so willing!"
        him"UGHH!"
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
            him"This feels so... open."
            bot"Yes. Open for business. My business."
            call changeObedience(character="Himawari", amount=1, fromwhere="v21_swimsuit_sitting_1", max_times=1, statlevel=2) from _call_changeObedience_168 # Sitting poses only become accessible after first run, meaning obedience is now at statlevel = 2 already
            bo"That's the point. It shows off the design. Hold it."
            show screen camera1280("sitting pose 3_a", 1, 0.0)
            show screen camera_ui("Himawari_swimsuit", False)
            with dissolve
            show screen camera_ui("Himawari_swimsuit")
            $ ui.interact()
            bo"Perfect. That pose screams confidence."
            himt"He likes m-my... confidence?"
            him"S-shut up! Or I'll make you scream in pain instead!"
            bo"I give you praise and this is your response?"
            bo"Anyway..."
            jump hima_swimsuit_repeatable_menu
        "Knees up, legs together." if not hima_chose_sitting_2:
            $ hima_chose_sitting_2 = True
            bo"Now bring your knees together, and maintain eye contact with the camera."
            scene sitting pose 4_a with dissolve: # variations not used so far: sitting pose 4_b, sitting pose 4_c
                xalign 0.5 yalign 0.95
            show sitting pose 4_a:
                subpixel True
                easein 3 yalign 0.2
            him"You're not staring somewhere else, are you?"
            himt"Why am I so dizzy? Just focus... focus on the camera..."
            bot"I'll stare wherever I want, bitch. You're mine now. The dumber you get from the withdrawal, the easier this is."
            call changeObedience(character="Himawari", amount=1, fromwhere="v21_swimsuit_sitting_2", max_times=1, statlevel=2) from _call_changeObedience_169
            bo"My focus is on the shot. Just hold the pose."
            show screen camera1280("sitting pose 4_a", 1, 0.0)
            show screen camera_ui("Himawari_swimsuit", False)
            with dissolve
            show screen camera_ui("Himawari_swimsuit")
            $ ui.interact()
            bo"That's a killer shot."
            him"You'll see a killer soon if I catch you staring again, creep."
            bo"I'm just doing my job."
            bo"Anyway..."
            jump hima_swimsuit_repeatable_menu
        "Face away from me, sit on your butt." if not hima_chose_sitting_3:
            $ hima_chose_sitting_3 = True
            bo"Now turn away from me, sit down, and look back over your shoulder."
            scene sitting pose 5_a with dissolve: # variations not used so far: sitting pose 5_b, sitting pose 5_closeup, sitting pose 5_front, sitting pose 5_relax, sitting pose 5_shy
                xalign 0.5 yalign 0.95
            show sitting pose 5_a:
                subpixel True
                easein 3 yalign 0.2
            him"This is so embarrassing... My back is completely bare."
            bot"Her embarrassment is my aphrodisiac. I could get drunk on it."
            call changeObedience(character="Himawari", amount=1, fromwhere="v21_swimsuit_sitting_3", max_times=1, statlevel=2) from _call_changeObedience_170
            bo"It's a classic pose for a reason. It highlights the form. Own it."
            show screen camera1280("sitting pose 5_a", 1, 0.0)
            show screen camera_ui("Himawari_swimsuit", False)
            with dissolve
            show screen camera_ui("Himawari_swimsuit")
            $ ui.interact()
            bo"Fantastic. You're more photogenic when you're not scowling."
            him"Can you just give a non qualified compliment for once?"
            bo"Oh now you care about my compliments, huh?"
            him"W-what, NO! Idiot, that's not what I meant."
            bo"Sure..."
            jump hima_swimsuit_repeatable_menu
        "Face towards me, sit on your butt." if not hima_chose_sitting_4:
            $ hima_chose_sitting_4 = True
            bo"Now sit down on your ass while facing me."
            him"Sounds easy!"
            bo"Let's see it then."
            scene sitting pose 5_front with dissolve:
                xalign 0.5 yalign 0.95
            show sitting pose 5_front:
                subpixel True
                easein 3 yalign 0.2
            him"This feels... More exposed than I thought it would."
            him"And it's because you're staring at me like a creep! Get behind the camera and take the picture already!"
            bo"I was just checking first to see if you got the pose correctly. I'm the director here, and you're the one taking orders."
            him"J-just get it done!"
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
            bo"Actually, there's one little thing."
            him"You just said it was perfect!"
            bo"It was close to perfect, but the angle could be even better."
            him"So move then."
            scene black with dissolve
            "You start walking towards her."
            him"W-what are you doing? Stay away!"
            bo"Calm down, this is the proper angle I was telling you about."
            scene sitting pose 5_closeup with dissolve:
                xalign 0.5 yalign 0.95
            show sitting pose 5_closeup:
                subpixel True
                easein 3 yalign 0.2
            him"The p-proper angle? You mean an excuse to stare at my cleavage?! H-how is this any better?"
            bo"It's not about your cleavage, dear [him_rel]."
            bot"Well, it is, but..."
            bo"It's about the vulnerability. It sells! Stay right there."
            show screen camera1280("sitting pose 5_closeup", 1, 0.0)
            show screen camera_ui("Himawari_swimsuit", False)
            with dissolve
            him"Be quick!!"
            show screen camera_ui("Himawari_swimsuit")
            $ ui.interact()
            bo"There we go."
            him"N-now get away from me!"
            bo"You did great, this one is definitely going to sell!"
            jump hima_swimsuit_repeatable_menu
            #Added sitting pose 5_front, sitting pose 5_closeup"





# --- SEXY SHOTS ---



# --- ENDING ---
label hima_swimsuit_ending:
    if himawari_obedience.level == 1 and hima_swimsuit_shots_taken == 0:
        "You must take at least some pictures with [him_name] to successfully complete the advancement event!"
    elif himawari_obedience.level == 1 and hima_swimsuit_shots_taken > 0:
        $ himawari_obedience.level += 1
        $ himawari_obedience.value = 0
        $ notification(f"{him_name}'s obedience level has reached level 2! The stat has been reset to 0.")
    bo"See? Wasn't so hard, was it?"
    hide screen camera_ui
    hide screen camera1280
    scene black
    with dissolve
    $ renpy.sound.play("/audio/soun_fx/footsteps.opus", channel="sfx1", loop=False, relative_volume = 1.5)
    "As you call 'wrap', [him_name] runs up to you, ready to snatch the money out of your pockets."
    scene bg modelling
    show bhima angry at center
    show boruto surprised at left
    with dissolve
    him"GIVE ME MY MONEY, ASSHOLE!"
    show boruto sceeming with dissolve
    bo"Calm down! And here I thought you were doing so well..."
    if quest_him.is_state("him2H_1", "pending") or quest_him.is_state("him2H_1", "in progress"):
        $ notification (f"{him_name} Hatred Level 2 objective completed")
        $ quest_him.check("him2H_1", "completed")
    him"I did do well. So pay me. We're done."
    bo"As promised. Your payment for a professional session."
    $ renpy.end_replay()
    menu swimsuitpayment:
        "How do you handle payment?"

        # Will go to love variant
        "{color=[lovecolor]}Give her $50{/color}" if money >= 50: # Convert this to a love only option where she'll get a little bit 'emotional' after you encourage her and thank her for her contribution or some shit. It'll result in an extra hugging cg where the MC may decide to cop a fell or not.
            label lovetestswimsuit:
            call changeMoney(-50) from _call_changeMoney_26
            show boruto normal with dissolve
            bot"Despite pushing her out of her comfort zone, she did her best and she delivered."
            bo"As promised, [him_name]. Here's your payment. You deserve it."
            show bhima normal with vpunch
            him"F-fifty dollars? [bo_name], are you sure about this? Where do you even find this kind of money?"
            call changeRespect("Himawari", 3) from _call_changeRespect_259
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
            call showscrollingimage from _call_showscrollingimage_272
            him"You are the best [him_rel_to_bo] ever!"
            bo"Heh.. I try...!"
            bo"But remember, we're not done yet, you can achieve so much more in this industry!"
            bo"I believe in you!"
            call hidescrollingimage() from _call_hidescrollingimage_219
            bot"She's my [him_rel] but..."
            bot"Damn it, she's so close to me... And with that bikini..."
            "In a vulnerable moment of hesitation, your mind begins to wander..."
            menu:
                "What do you do?"
                "Cop a feel.":
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
                    call hidescrollingimage2() from _call_hidescrollingimage2_146                    
                "Don't.":
                    call changeRespect("Himawari", 3) from _call_changeRespect_260
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
            bot"The standard rate. Enough to keep the dog fed and coming back for more, but not so much that she gets ideas above her station. Just a steady drip of reinforcement."
            bo"Here's your pay. Good work today."
            call changeMoney(-20) from _call_changeMoney_27
            show bhima shy with dissolve
            him"Thanks... I guess."
            call changeRespect("Himawari", 1) from _call_changeRespect_261
            bo"Maybe next time don't be so argumentative, do as I say and MAYBE, just maybe... you'll make more."
            show boruto sceeming with dissolve
            bot"That's right, all I gotta do is tie her sense of value to money and sooner or later she'll be doing exactly as I say with zero resistance!"
            scene black with dissolve
            "[him_name] takes the money and leaves, still processing the session."
            $ hima_swimsuit_not_paid = False
            jump action_taken
        "{color=[hatredcolor]}Short-change her ($20){/color}" if money >= 20: # hatred exclusive option. MC will tease her with the money, 'beckoning' for her to reach for it.
            if chosen_hate_path:
                call checkHatred(30,"swimsuitpayment") from _call_checkHatred_48
            bot"This is the best option. The ultimate mindfuck. Degrade her completely, then spit in her face with this insulting payment."
            bot"Lock her into a cycle of desperate rage. She'll have to come back to 'earn' what she's 'owed'. She'll be my perfect, angry little puppet."
            bo"Market's tough. I don't think there's much money left to give you. What do you think about something like 20 bucks?"
            call changeRespect("Himawari", -5) from _call_changeRespect_262
            show bhima angry with dissolve
            him"Twenty bucks? TWENTY!? After what you just made me do!?"
            show boruto sceeming2 with dissolve
            bo"That was a test, [him_name]. To see if you had what it takes. The real payment comes when we deliver the full set. I promise."
            bot"Oh, you'll get what you deserve. You'll get exactly what you deserve."
            call changeHatred(2, max_times=1, fromwhere="shortchange") from _call_changeHatred_214
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
            call showscrollingimage from _call_showscrollingimage_273
            him"You..promised!!"
            call hidescrollingimage2("Click twice to overpower her!") from _call_hidescrollingimage2_147
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
            call showscrollingimage from _call_showscrollingimage_274
            bo"In fact, I would even go as far as to say that... the feeling is mutual, my dear [him_rel]."
            call hidescrollingimage("Click twice to go a little bit easier on her.") from _call_hidescrollingimage_220
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
                    call showscrollingimage from _call_showscrollingimage_275
                    him"GET YOUR HANDS OFF ME, CREEP!"
                    him"YOU THINK I'LL FALL FOR THAT?!"
                    call hidescrollingimage2("Press twice to let her go.") from _call_hidescrollingimage2_148
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
            call changeMoney(-20) from _call_changeMoney_28
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
            bo"On a second thought... Looking at these pictures..."
            bo"They're kinda trash. I doubt they'll sell for anything."
            show bhima angry with dissolve
            him"What? How dare you?!"
            show bhima at smallshake
            him"You made me do THAT for nothing!?"
            bo"It's an investment, [him_name]!"
            him"You're full of it! I knew I shouldn't have trusted you!"
            call changeRespect("Himawari", -5) from _call_changeRespect_263
            bot"What did she expect? Not even stripping naked and getting money on top of it? What a dumb bitch."
            scene black with dissolve
            $ renpy.sound.play("/audio/soun_fx/footsteps.opus", channel="sfx1", loop=False, relative_volume = 1.5)
            "[him_name] storms out, furious."
            bo"At least put your clothes on first, dummy!"
            him"SHUT UP!!!" with hpunch
            $ hima_swimsuit_not_paid = True
            jump action_taken