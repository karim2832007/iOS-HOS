# v0.19 Tenten Quest Continuation - Pendant Return Logic
# Handles the "Hand it over" path from map_shop.rpy

# ATL Transform for slow scene zoom
transform slow_scene_zoom_right:
    # Over 20 seconds, zoom to 1.5 and shift slightly right
    linear 20.0 zoom 1.5 xpos -0.5 # Adjust 0.55 as needed

transform camera_reset:
    zoom 1 pos (0.0, 0.0)

label tenten_pendant_return_start:
    # Assuming we are already in the shop scene context from map_shop.rpy
    # Need appropriate Tenten sprites showing surprise/relief

    # Hide the shopkeeper headshot if it's showing
    hide screen shopkeeper

    # Show Tenten's character sprite - adjust expression as needed
    show ten normal # Happy
    show boruto laughing
    with dissolve

    show ten normal with vpunch:
        easein 0.5 xpos 0.6
    ten "You... You found it! Give it here!"
    # (Implied action: Boruto hands it over)
    # Add action: Tenten snatches it, clutches it tightly, inspects it
    scene black with dissolve # maybe show the pendant (but tricky cause its also referenced in other scenes)
    "She clutches the pendant tightly, carefully running her thumb over its surface."
    scene shop day with dissolve:
        zoom 0.5

    show ten normal at left with dissolve # Change sprite back to relieved/happy but maybe slightly guarded
    ten "It's really it... I never thought I'd see it again."
    show boruto laughing at right with dissolve
    bo "Yeah, had a run-in with some weird old merchant in the alley at night. He just... gave it to me."
    show boruto worried2 with dissolve
    $ renpy.sound.play("/audio/soun_fx/oldman_laugh3.opus",channel="sfx2",loop=False,relative_volume=1)
    show merchant 2 at center with dissolve:
        alpha 0.5
        easein 5 zoom 1.2 alpha 0.0
    bot "I totally didn't have to trade in a bunch of lewd pictures of my uh, subjects..."
    hide merchant 2
    # Add Boruto's observation about the pendant
    show boruto suspicious with dissolve
    bo "Thing felt... weird, though. Almost warm sometimes. Is there someth-"
    show boruto worried
    show ten angry
    with dissolve
    ten "A hooded, old looking guy wearing sunglasses?" with vpunch
    show ten at smallshake
    ten "I knew that creep looked off! To think he was a thief, off course he'd have his hands on something like this!"
    bo "I was just saying it felt kinda-"
    show ten normal with dissolve
    ten "Warm? It's... just old metal. Probably reacting to your body heat." # Nervous dismissal
    show ten sad2 with dissolve
    ten "But thank goodness you got it back. I thought it was lost forever."
    show boruto laughing with dissolve
    bo "Not on my watch! Certainly looks to be more than just a pendant for you, right?"
    # Change explanation of importance
    ten "It is... It's a family heirloom. Very old, very... significant."
    menu tenten_return_heirloom_react:
        ten "It is... It's a family heirloom. Very old, very... significant."
        "Significant how?":
            # Player shows curiosity
            show ten angry with dissolve
            ten "It's... complicated." # Evades
            show boruto suspicious with dissolve 

        "Glad I could help then.":

            show boruto laughing with dissolve 
            ten "Yes... thank you."



    # Dialogue continues after the menu choice
    # Reset Boruto's expression if needed, or keep based on choice? Let's keep suspicious for now.
    # Removed sprite zoom. Camera handles the scene zoom now.
    show boruto suspicious
    show halfblack
    with dissolve
    camera at slow_scene_zoom_right

    # Zoom effect lasts during this line until player click
    bot "Can't shake the feeling that there's something she's not telling me but..."

    # Explicitly reset the camera after the interaction
    camera at camera_reset
    hide halfblack
    with dissolve
    ten "Thank you, [bo_name]. Really. I don't know how to repay you."

    # --- Node P: Set flags, complete quest ---
    $ tenten_pendant_returned = True
    if quest.exists("shop1_3"):
        if quest.is_state("shop1_3", "in progress"):
            $ quest.check("shop1_3", "completed")
            $ notification("Objective Completed: Find the shopkeeper's keepsake")

    # --- Node Q: Misunderstanding, Offer Night Visit ---
    # Add sprite change: Tenten thoughtful/slightly embarrassed
    show ten angry with dissolve # thoughtful
    ten "You know... I might have misjudged you."
    ten "You went out of your way to bring this back..."
    show boruto embarassed with dissolve
    bo "Just doing the right thing, I guess."
    show ten normal with dissolve:
        easein 2 xpos 0.2
    ten "Still... I'd like to thank you properly."
    show ten normal with dissolve # Excited expression
    ten "Maybe... if you're free later tonight... we could meet up outside my shop? There's a place I'd like to show you..."
    show boruto surprised3 with vpunch
    # Add sprite change: Tenten hopeful/nervous
    bot "Is this..."
    bot "Is this what I think it is?!"
    show boruto snob with dissolve
    #     subpixel True
    #     easein 5 xpos 0.90
    bot "BEING A NICE GUY IS FINALLY PAYING OFF!"        
    show ten normal with dissolve # hopeful
    # --- Node n5: Accept Date? ---
    menu tenten_accept_date_offer:
        ten "What do you say. Will you come by tonight?"

        "Count me in!": # Love - Positive choice
            show boruto normal with dissolve
            # --- Node R: Accept Date ---
            bo "Sure, sounds nice."
            # Add sprite change: Tenten happy/excited
            show ten normal with dissolve # Excited expression
            ten "Really? Great! Come by my shop when the sun sets! I'll take you to my favorite spot. You're gonna love it!"
            $ tenten_date_agreed = True
            $ tenten_days_since_agreed = 0 # Start the counter
            bo "I'll hold you to it. See you then!"
            # Hide Tenten sprite, return to map
            hide ten
            hide boruto
            with dissolve
            scene black with dissolve
            jump market

        "Sorry, can't tonight.": # Neutral choice
            # --- Node n6: Decline Date ---
            # Add sprite change: Tenten disappointed but understanding
            show boruto laughing2 with dissolve
            bo "Sorry, I can't tonight. I got uhhh... some stuff I need to attend to... Yep."
            hide ten
            show ten sad2 at left
            with dissolve
            $ tenten_date_decline_counter += 1
            ten "Oh... okay. Maybe some other time then."
            bo "Yeah, maybe."
            bot "...totally"
            # Hide Tenten sprite, return to shop menu context (or leave?)
            # Flowchart says return to E_Standard (Standard Shop Menu/Dialogue)
            # Need to decide if we jump back to tenten_shopmenu or a new post-quest label
            # For now, let's jump back to the main shop menu label in map_shop.
            # We'll handle the post-quest dialogue variations via the hook we added earlier.
            jump action_taken

        "You want me to... At night? What for? ;)":
            
            $ tenten_date_decline_counter += 1 # Still counts as a decline for now
            hide ten
            show ten angry at left
            with dissolve
            ten "H-hey! It's not like that! I just... thought it would be nice gesture of my goodwill!"
            show ten at smallshake
            ten "Forget it then!" with vpunch
            show boruto angry with dissolve
            bo"*Tsk*!" with vpunch
            bot "Well, fuck! Better peace out..."
            show boruto normal with dissolve
            bo "Suit yourself."
            hide boruto with dissolve
            # Same return logic as standard decline
            jump action_taken