# v0.19 Tenten Quest Continuation - Post-Quest Shop Dialogue

label tenten_daytime_dialogue_entry:
    # Main entry point for Tenten's shop dialogue after the pendant quest.
    # Dispatches to different logic blocks based on player actions and relationship status.

    hide screen shopkeeper
    if tenten_brain_damage == True:
        jump tenten_postquest_brain_damage
    elif tenten_extorted or tenten_lake_date_fail_permanent:
        jump tenten_postquest_extorted

    else:
        jump tenten_postquest_normal_entry

label tenten_postquest_extorted:
    # Handles dialogue if Tenten was extorted or the date failed permanently.
    $ shopkeep_annoyance = 2
    if tenten_date_shop_dialogueflavor_mentioned == False:
        show ten angry at left with dissolve
        ten "You again... What do you want now?"
        ten "Just buy something or get out. And keep your hands to yourself."
        if tenten_extorted:
            ten "Pig!" with vpunch
        if tsunade_discovery_seen==True:
            show boruto angry at right with dissolve
            $ bot(renpy.random.choice([
                "Bitch... Wait till my radioactive cum turns you into a fucking goblin, that'll teach you.",
                "Ungrateful bitch... Just wait until my special 'load' makes you sprout an extra limb or two.",
                "Keep talking, bitch. Soon enough, you'll be glowing in the dark thanks to my 'special delivery'.",
                "You think you're tough? Wait until my radioactive jizz melts that pretty face of yours.",
                "Mark my words, bitch. One shot from me and you'll be begging for a cure you won't get.",
                "Enjoy that attitude while it lasts. My 'gift' is going to rearrange more than just your features.",
                "Can't wait to see the look on your face when my radioactive seed turns you into an orc."
            ]))
            hide boruto
        $ tenten_date_shop_dialogueflavor_mentioned = True
    else:
        show shopkeeperimage with dissolve:
            zoom 0.7 xpos -60 ypos 0.01
        $ ten(renpy.random.choice([
            "You again... What do you want now?",
            "Oh, it's you. Spit it out.",
            "What is it this time? Don't waste my time.",
            "Back for more, huh? Make it quick.",
            "Ugh, not you again. What now?"
        ]))
    jump tenten_postquest_shop_exit

label tenten_postquest_brain_damage:
    $ shopkeep_annoyance = 2
    default braindamage_mentioned = False
    if braindamage_mentioned == False:
        $ braindamage_mentioned = True
        show ten angry at left with dissolve
        ten "You... I remember you!" with vpunch
        bot"O-oh shit!"
        ten"We were together at my favorite place, weren't we? And then... A-and then... You... Y-you-"
        show ten at smallshake
        ten"Aaarh! W-why can't I remember anything from that night!" with vpunch
        ten "D-did you... You did something horrible to me, didn't you?!" with vpunch
        show boruto angry at right with dissolve
        bo "W-what are you talking about? Don't throw around such serious baseless accusations on people! I'm here to shop!"
        ten "You tread carefully, young man..."
        ten "I am watching your every move!" with vpunch
        call changeHatred(1) from _call_changeHatred_164
        bot "Lucky me! She should consider herself lucky she doesn't remember."
        dev"You really lucked out on this one, eh?"
        dev"Tenten cannot be romanced anymore, but perhaps there's more in store for her in the future..."
        $ tenten_date_shop_dialogueflavor_mentioned = True
    else:
        show shopkeeperimage with dissolve:
            zoom 0.7 xpos -60 ypos 0.01
        $ ten(renpy.random.choice([
            "You again... What do you want now?",
            "Oh, it's you. Spit it out.",
            "What is it this time? Don't waste my time.",
            "Back for more, huh? Make it quick.",
            "Ugh, not you again. What now?"
        ]))
    jump tenten_postquest_shop_exit

label tenten_postquest_normal_entry:
    # Handles the normal dialogue path (pendant returned, no permanent failure).
    # Starts with greeting logic.

    # --- Determine Greeting --- Make it so it shows this only if date was within last 24h, not all dates in general (show only once after a date)
    if tenten_date_agreed:
        # Reminder greeting if a date is already agreed upon - will keep being repeated on all visits until date is attempted.
        show ten normal at left with dissolve
        if tenten_days_since_agreed == 0:
            ten "Hey! Don't forget, we're meeting outside the shop tonight! I'll take you to my favorite spot."
        elif tenten_days_since_agreed == 1:
            ten "You... didn't forget about tonight, did you? Like you forgot yesterday?"
        else:
            ten "So... are you actually coming tonight? You've kept me waiting for [tenten_days_since_agreed] days..."
        show boruto embarassed at right with dissolve
        bo "Right, right. Outside shop, tonight."
        ten "You'd better not forget..."
        jump tenten_postquest_shop_exit
    
    elif tenten_date_counter > 0 and tenten_lake_date_fail_retry == 0:
        # Post-date greeting (successful date) - only once until new date happens
        if not tenten_date_shop_dialogueflavor_mentioned:
            show ten normal at left with dissolve
            if tenten_date_counter == 1:
                ten "Oh, hey! Good to see you again after our little outing! Let me know if you need anything..."
            else:
                ten "Back again? It's always nice seeing you stop by.."
            $ tenten_date_shop_dialogueflavor_mentioned = True
        else:
            show shopkeeperimage with dissolve:
                zoom 0.7 xpos -60 ypos 0.01
            ten "How may I be of service, [bo_name]?"
        jump tenten_postquest_check_player_ask  # After greeting, check if player can ask for another date

    elif tenten_lake_date_fail_retry > 0:
        # Greeting after a failed date (retry possible) - only once until new date happens
        if not tenten_date_shop_dialogueflavor_mentioned:
            show ten angry at left with dissolve
            ten "So, all that weirdness on that night..."
            ten "Just this once, I'll pretend it never happened."
            $ tenten_date_shop_dialogueflavor_mentioned = True
        else:
            show shopkeeperimage with dissolve:
                zoom 0.7 xpos -60 ypos 0.01
            ten "How may I be of service, [bo_name]?"
        jump tenten_postquest_check_player_ask

    else:
        # Pre-first date greeting (no dates happened, none agreed) - only once until new date happens. Then check if tenten must ask
        if tenten_date_decline_counter == 0 and tenten_date_counter == 0 and not tenten_date_shop_dialogueflavor_mentioned:
            show ten normal at left with dissolve
            ten "Hey... thanks again for bringing my pendant back."
            jump tenten_postquest_check_tenten_ask
        show shopkeeperimage with dissolve:
            zoom 0.7 xpos -60 ypos 0.01
        ten "How may I be of service, [bo_name]?"
        jump tenten_postquest_check_tenten_ask

label tenten_postquest_check_player_ask:
    # Checks if the player should be prompted to ask Tenten out again.
    # This happens if they've dated before (counter > 0) and no date is currently agreed and player was not prompted yet today.

    if tenten_date_counter > 0 and not tenten_date_agreed and not tenten_date_asked_today:
        # Check if the last date failed but is retryable
        if tenten_lake_date_fail_retry > 0:
            $ tenten_date_asked_today = True
            jump tenten_postquest_player_ask_retry_menu
        else:
            $ tenten_date_asked_today = True
            # Last date was successful (or this is just a normal subsequent ask)
            jump tenten_postquest_player_ask_menu
    else:
        # Conditions not met for player to ask, check if Tenten should ask
        jump tenten_postquest_check_tenten_ask

label tenten_postquest_player_ask_menu:
    # Menu for the player to ask Tenten out again after a successful date.
    menu tenten_player_ask_date_prompt:

        "I just wanna buy some stuff.":
            jump tenten_postquest_shop_exit

        "Ask her out again":
            if tsunade_discovery_seen == True:
                bot "Asking her out again... Right, Tsunade's warning. If things get heated, gotta remember the condoms. No exceptions."
            menu tenten_ask_another_date_player_init:
                ten "So... thinking about visiting the lake again sometime soon?"

                "Definitely! How about tonight?":
                    ten "Yes! That sounds perfect. I'll meet you outside my shop around night time then!"
                    $ tenten_date_agreed = True
                    $ tenten_days_since_agreed = 0
                    $ tenten_date_asked_today = True # Mark as asked today since a date was agreed
                    jump tenten_postquest_shop_exit

                "Maybe another time.":
                    hide shopkeeperimage
                    show ten sad2 at left
                    with dissolve
                    $ tenten_date_decline_counter += 1 # Track declines even post-first date
                    $ tenten_date_asked_today = True # Mark as asked today even if declined
                    ten "Oh... alright. Let me know when you're free."
                    if tsunade_discovery_seen == True:
                        $ bot(renpy.random.choice([
                            "Sorry Tenten. I can't risk my radioactive load turning you into a goblin if the condom breaks.",
                            "Can't do it, Tenten. Too risky with this whole radioactive jizz situation. Don't want you growing scales.",
                            "Declining for your safety, Tenten. Wouldn't want you ending up looking like one of Orochimaru's experiments."
                        ]))
                        $ bot(renpy.random.choice([
                            "I'm doing this for you.",
                            "Trust me, you'll thank me later when you're not sprouting horns.",
                            "Consider this a favor. A radioactive makeover isn't a good look.",
                            "Better safe than sorry..."
                        ]))
                    jump tenten_postquest_shop_exit

                "Actually, just browsing today.":
                    hide shopkeeperimage
                    show ten sad1 at left
                    with dissolve
                    $ tenten_date_asked_today = True
                    ten "Okay, okay. Let me know if you need anything!"
                    jump tenten_postquest_shop_exit

label tenten_postquest_player_ask_retry_menu:
    # Menu for the player to ask Tenten out again after a failed date (retry possible). Will prompt again every day as long as last date is on retry state.
    if tenten_date_shop_dialogueflavor_mentioned == False:
        show boruto embarassed at right with dissolve
        bo "Tenten, about our last date I'm sorry, I can expl-"
        ten "Like I said, it never happened!"
        $ tenten_date_shop_dialogueflavor_mentioned = True
    "You carefully consider whether asking her out again and trying once more is worth it."

    menu tenten_player_ask_date_retry_prompt:
        "You carefully consider whether asking her out again and trying once more is worth it."

        "I just wanna buy some stuff.":
            jump tenten_postquest_shop_exit

        "Ask her out again.":
            # --- Ask about another date (Triggered by Player - Retry) ---
            if tsunade_discovery_seen == True:
                bot "Maybe I should at least warn her about Tsunade's discovery this time?"
                bot "If I screw up again... there may not be another one."
            "I was wondering if you'd give me another chance?"
            menu tenten_ask_another_date_player_retry_init:
                ten "I don't know... After last time..."

                "It'll be different this time.": 
                    show boruto worried at right
                    with dissolve
                    bo "I'm sorry, this time will be different, I promise."
                    hide shopkeeperimage
                    show ten angry at left
                    with dissolve
                    ten "..."
                    "She gives it some consideration."
                    "You can clearly tell she's both confused and hurt."
                    ten "Hmph. I guess we'll find out. Meet me at the usual spot."
                    call changeHatred(-1, "agreed_tenten_date_shop") from _call_changeHatred_165 
                    $ tenten_date_agreed = True
                    $ tenten_days_since_agreed = 0
                    $ tenten_date_asked_today = True
                    jump tenten_postquest_shop_exit

                "Nevermind.":
                    # (Decline - Retry) ---
                    show boruto normal at right with dissolve 
                    bo "You're right, let's keep some distance for now."
                    hide shopkeeperimage
                    show ten sad1 at left 
                    with dissolve
                    $ tenten_date_decline_counter += 1
                    $ tenten_date_asked_today = True 
                    ten "Oh... alright then..."
                    $ shopkeep_annoyance = 2
                    if tsunade_discovery_seen == True:
                        $ bot(renpy.random.choice([
                            "Sorry Tenten. I can't risk my radioactive load turning you into a goblin if the condom breaks.",
                            "Can't do it, Tenten. Too risky with this whole radioactive jizz situation. Don't want you growing scales.",
                            "Declining for your safety, Tenten. Wouldn't want you ending up looking like one of Orochimaru's experiments."
                        ]))
                        $ bot(renpy.random.choice([
                            "I'm doing this for you.",
                            "Trust me, you'll thank me later when you're not sprouting horns.",
                            "Consider this a favor. A radioactive makeover isn't a good look.",
                            "Better safe than sorry..."
                        ]))
                    jump tenten_postquest_shop_exit

label tenten_postquest_check_tenten_ask:
    # Checks if Tenten should initiate asking the player out.
    # Conditions: Not asked today, no date agreed, not in retry state.
    $ should_ask_date = False
    if not tenten_date_asked_today and not tenten_date_agreed and tenten_lake_date_fail_retry == 0:
        # Condition 1: First date ever
        $ condition1 = (tenten_date_counter == 0)
        # Condition 2: After first date, Tenten asks if 7 days passed
        $ condition2 = (tenten_date_counter > 0 and 'day_number' in globals() and day_number > 0 and tenten_last_date_day > 0 and (day_number - tenten_last_date_day > 7))

        if condition1 or condition2:
            $ should_ask_date = True
            $ tenten_date_asked_today = True

    if should_ask_date:
        jump tenten_postquest_tenten_ask_menu
    else:
        # No one is asking for a date, go to neutral exit
        jump tenten_postquest_neutral_exit

label tenten_postquest_tenten_ask_menu:
    # Menu for when Tenten initiates asking the player out.
    if tenten_date_counter > 0:
        # Ask about another date (Triggered by Tenten after 7 days) ---
        ten "Actually, first of all... I was wondering, were you thinking about visiting the lake again sometime soon?"
        if tsunade_discovery_seen == True:
            bot "She's asking... Right, Tsunade's warning. Gotta be careful. Condoms."

        menu tenten_ask_another_date_tenten_init:
            bot "She's asking... Right, Tsunade's warning. Gotta be careful. Condoms."

            "Definitely! How about tonight?":
                ten "Yes! That sounds perfect. I'll meet you outside my shop around night time then!"
                if tsunade_discovery_seen == True and money < 300:
                    show boruto normal at right with dissolve
                    bo "Oh, and... this is kinda embarrassing, but..."
                    bo "Could you maybe... bring a condom this time? I'm kinda broke right now and, umm..."
                    bo "I just found out that my..-"
                    ten "Oh don't worry I got plenty of those!"
                    hide boruto
                $ tenten_date_agreed = True
                $ tenten_days_since_agreed = 0
                jump tenten_postquest_shop_exit

            "Maybe another time.":
                hide shopkeeperimage
                show ten sad2 at left
                with dissolve
                $ tenten_date_decline_counter += 1
                ten "Oh... alright. Let me know when you're free."
                if tsunade_discovery_seen == True:
                    show boruto normal at right with dissolve
                    bot "Sorry Tenten. I'm not nearly rich enough to be paying for child support on top of everything else right now."
                    bot "Especially considering your shop is expensive as fuck."
                    show boruto surprised3 with vpunch
                    bot "Wait, what if I get dad discounts?"
                    hide boruto
                jump tenten_postquest_shop_exit

            "Just browsing today.":
                hide shopkeeperimage
                show ten sad1 at left
                with dissolve
                ten "Okay, okay. Let me know if you need anything!"
                jump tenten_postquest_shop_exit
    else: # No dates happened yet (tenten_date_counter == 0)
        # Ask about the first date (adjust intro based on declines)
        if tenten_date_decline_counter == 0:
            ten "Still thinking about that lake visit, if you're interested..."
        elif tenten_date_decline_counter == 1:
            ten "Changed your mind about meeting up, maybe?"
        else:
            ten "Still busy, I suppose?"

        # Ask about scheduling first date ---
        menu tenten_ask_first_date:
            "You're carefully considering whether dating Tenten is your primary concern right now."

            "I just wanna buy some stuff.":
                ten "Fiiine, fine!"
                jump tenten_postquest_shop_exit

            "Yes, let's do it.":
                ten "Great! I'll see you there!"
                if tsunade_discovery_seen == True:
                    show boruto normal at right with dissolve 
                    bot "I just hope Tsunade is full of shit and my cum doesn't turn her into a goblin or something..."
                    hide boruto
                $ tenten_date_agreed = True
                $ tenten_days_since_agreed = 0
                jump tenten_postquest_shop_exit

            "Still can't tonight, sorry.":
                hide shopkeeperimage
                show ten sad2 at left
                with dissolve
                $ tenten_date_decline_counter += 1
                ten "Oh... okay. Well, the offer stands if you change your mind."
                if tsunade_discovery_seen == True:
                    show boruto normal at right with dissolve
                    bot "Maybe if you at least promised me some kind of dad discount on condoms I'd consider it."
                    hide boruto
                jump tenten_postquest_shop_exit

label tenten_postquest_neutral_exit:
    # Handles the case where no date ask happens (e.g., already asked today, conditions not met).
    # Provides a neutral closing line before going to the shop menu.
    jump tenten_postquest_shop_exit

label tenten_postquest_shop_exit:
    # Common exit point. Hides characters involved in the dialogue and shows the shopkeeper screen.
    hide ten
    hide boruto # Hide Boruto too, just in case he was shown
    show screen shopkeeper
    show screen marketreturn
    with dissolve
    jump tenten_shopmenu # Return to standard shop menu

# Fallback in case something goes wrong, though all branches should jump to tenten_postquest_shop_exit.
label tenten_postquest_fallback_exit:
    show screen shopkeeper with dissolve
    jump tenten_shopmenu