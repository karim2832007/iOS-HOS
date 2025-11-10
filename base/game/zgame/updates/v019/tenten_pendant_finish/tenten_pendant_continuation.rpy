# v0.19 Tenten Pendant Finish Defaults
default tenten_pendant_returned = False
default tenten_extorted = False
default tenten_date_agreed = False
default tenten_days_since_agreed = 0
default tenten_date_asked_today = False # Tracks if Tenten asked about a date today
default tenten_last_date_day = 0 # Tracks the day number of the last successful date
default tenten_date_decline_counter = 0
default tenten_date_counter = 0
default tenten_path_is_dominance = False
default tenten_asked_money = False
default tenten_asked_info = False
default tenten_all_options_exhausted = False

label tenten_pendant_continuation:
    hide shopkeeperimage #hide shopkeeper image to use sprite and autohighlighting for quest dialogue
    show boruto normal at right
    show ten sad1 at left
    with dissolve
    bo"About your pendant..."
    show ten sad1:
        ease 0.3 xalign 0.5
    ten"H-have you found it!?" with vpunch
    $ tenten_magic_word_counter = 0 # Initialize counter for this interaction
    menu show_pendant_tease:
        "Of course I did, calm down.": # Neutral/Good option
            show boruto laughing2 with dissolve
            bo "Of course I did, calm down."
            show ten angry:
                ease 0.3 xpos 0.3
            show boruto surprised
            ten "Calm down? You know how important this is to me! Show me!" with vpunch
            # Proceed to the original options menu below

        "Perhaps, what's the magic word?":
            $ tenten_magic_word_counter = 1
            # Removed invalid call changeHatred(1)
            show boruto snob with dissolve
            bo "Perhaps, what's the magic word?"
            show ten angry:
                ease 0.3 xalign 0.3
            ten "*Scoffs* Just show it to me, smartass!" with vpunch
            show boruto angry # Show Boruto angry *before* the menu
            menu magic_word_repeat_menu_1:
                "Still waiting for the magic word...":
                    $ tenten_magic_word_counter = 2
                    $ shopkeep_annoyance = min(shopkeep_annoyance + 1, 2) # Increment annoyance, cap at 2
                    # Removed invalid call changeHatred(1)
                    show boruto sceeming with dissolve
                    bo "Still waiting for that magic word..."
                    show ten angry:
                        ease 0.3 xalign 0.5
                    ten "Are you serious?! Stop messing around and show me the damn pendant!" with vpunch
                    menu magic_word_repeat_menu_2:
                        "Come on, the magic word?":
                            $ tenten_magic_word_counter = 3
                            $ shopkeep_annoyance = min(shopkeep_annoyance + 1, 2) # Increment annoyance again, cap at 2
                            # Removed invalid call changeHatred(1)
                            show boruto sceeming2 with dissolve
                            bo "Come on, Tenten, the magic word?"
                            show ten angry with hpunch # 3rd Annoyance (Snapping)
                            ten "THAT'S IT! You want the magic word?! FINE! {size=+4}ABRACADABRA, YOU ASSHOLE!{/size} NOW SHOW ME THE PENDANT BEFORE I SHOVE MY FIST WHERE THE SUN DON'T SHINE!" with hpunch
                            # Check annoyance level after she snaps
                            if shopkeep_annoyance >= 2:
                                $ shopkeep_block = True
                                # Use the kick-out sequence
                                ten "Get out of here you idiot!" with vpunch
                                hide boruto
                                hide ten
                                scene black with vpunch
                                jump market # Kick player out
                            else:
                                # Annoyance not high enough, proceed normally
                                jump pendant_options_label 

                        "Alright, fine.":
                            show boruto normal with dissolve
                            bo "Alright, fine."
                            jump pendant_options_label 

                "Okay, okay.":
                    show boruto normal with dissolve
                    bo "Okay, okay."
                    show ten:
                        ease 0.3 xalign 0.3
                    jump pendant_options_label

        "Maybe... maybe not.":
            show boruto sceeming with dissolve
            bo "Maybe... maybe not."
            show ten sad1 with dissolve # Anxious/Demanding
            ten "Don't tease me! Is it the pendant or not?!" with vpunch
    # --- NEW MENU END ---

    # Original menu follows the new one
    label pendant_options_label: # Add label to jump to
    menu pendant_options:
        bot "It seems like it's quite valuable to her... Should I...?"
        "Hand it over":
            jump tenten_pendant_return_start

        "{color=[dominancecolor]}Ask for a different kind of repayment...{/color}":
            call checkDominance(15, "tenten_pendant_dominance_fail") from _call_checkDominance_39
            $ tenten_path_is_dominance = True
            jump tenten_pendant_dom

        "{color=[hatredcolor]}Extort her{/color}":
            call checkHatred(20, "pendant_options_label") from _call_checkHatred_23
            jump tenten_pendant_extort_start

label tenten_pendant_dominance_fail:
    $ tenten_path_is_dominance = False
    show boruto sceeming2
    bo "You know, if it's really that important, there's a lot of other ways you could repay me, if you know what I mean..."
    show ten angry with vpunch
    show boruto surprised2
    ten "I can't believe you would suggest something like that after I trusted you!"
    ten "Get out of my shop, now!" with hpunch
    hide boruto
    hide ten
    scene black with vpunch
    $ shopkeep_annoyance = 2
    jump market # Kick player out