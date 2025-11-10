screen image_with_border(img, zoomlevel=1,xalignpos=0.0,yalignpos=0.0, border_size=10):
    
    frame:
        xalign xalignpos
        yalign yalignpos
        background "#000000"
        padding (border_size, border_size)
        add img:
            zoom zoomlevel
            

# Triggered after Tenten agrees to a date out of gratitude for returning the pendant.

default tenten_date_success = False # Flag for successful date outcome
default tenten_lake_swim = False    # Flag if they decide to swim
default tenten_lake_shared_story = False # Flag if backstories were shared
default tenten_helped_release = False # Flag if Tenten helped Boruto
default tenten_lake_date_fail_retry = 0 # Flag of failed dates with retry possibility
default tenten_lake_date_fail_permanent = False # Flag of permanent date failure. In the future certain options might unlock it again (re-set to false)
default tenten_date_seen = False # Flag for repeatable-specific logic
default expert_option = False # Flag for different branch that should not call hidescrollingimage2
default tenten_date_peeked = False # Used for dialogue flavor in repeatable
default tenten_date_handjob = False # Used for dialogue flavor in repeatable
default tenten_date_titsuck = False # Used for dialogue flavor in repeatable
default tenten_date_thighfuck = False # Used for dialogue flavor in repeatable
default tenten_assgrab_fail = False # Used for dialogue flavor in repeatable
default tenten_assgrab_normal = False # Used for dialogue flavor in repeatable
default tenten_pussy_fail = False # Used for dialogue flavor in repeatable

label tenten_meet_at_shop:
    $ initialize_replay_defaults()
    $ tenten_lake_swim = False
    $ tenten_lake_shared_story = False
    $ tenten_helped_release = False
    $ tenten_date_asked_today = False
    hide tenten_date_market_out
    call hideUI from _call_hideUI_63

    if tenten_lake_date_fail_retry>0:
        show ten angry at center with dissolve
        ten "Promise to be... Less awkward this time?"
        show boruto embarassed at right with dissolve
        bo "D-definitely..!"
        show ten normal with dissolve
        ten "Hmph. Well, let's go then!"
        jump tenten_lake_date_start_repeatable
        
    if tenten_days_since_agreed > 1:
        show ten angry at center with dissolve
        ten "There you are! I was starting to think you stood me up... again."
        show boruto embarassed at right with dissolve
        bo "Sorry, got held up."
        ten "Hmph. Well, you're here now."
        if tenten_date_seen == True:
            jump tenten_lake_date_start_repeatable

    elif tenten_date_decline_counter > 0:
        show ten sad2 at center with dissolve 
        ten "Oh, hi. You actually made it. Despite rejecting me earlier..."
        show boruto smirk at right with dissolve
        bo "Wouldn't miss it."
        ten "Right..."
        if tenten_date_seen == True:
            jump tenten_lake_date_start_repeatable

    elif tenten_date_counter == 0 and tenten_days_since_agreed == 0:
        show ten sad2 at center with dissolve 
        ten "You came!"
        show boruto laughing at right with dissolve
        bo "Of course! You said there's a place you wanted to do show me, right?"
        ten "Mhm!"
        bo"Let's get going then!"

    elif tenten_date_counter >= 1: # Already had at least one date (counter increments *after* the date)
        show ten normal at center with dissolve
        ten "Back again, huh? Starting to like these little meetings."
        show boruto embarassed at right with dissolve
        bo "Something like that."
        ten "Ready when you are."
        if tenten_date_seen == True:
            jump tenten_lake_date_start_repeatable

    else: # Default fallback, likely first time or reset state
        show ten normal at center with dissolve
        ten "You ready to go?"
        show boruto laughing at right with dissolve
        bo "Yeah, let's head out."
        if tenten_date_seen == True:
            jump tenten_lake_date_start_repeatable

label tenten_lake_date_start:
    $ tenten_date_seen = True

    $ playmusic("audio/ost/lakedate.opus",0.3)
    show boruto:
        easein 2 xalign -3
    show ten:
        easein 2 xalign -3
    with moveoutleft
    hide ten
    hide boruto
    scene black
    with dissolve
    pause(1)
    scene bg_night_forest1 with Dissolve(0.5):
        xalign 0.5 yalign 1.0 subpixel True
    show bg_night_forest1:
        easein 10 zoom 1.15 yalign 0.0 xalign 1.0 subpixel True
    pause(2)
    $ renpy.sound.play("/audio/soun_fx/crickets.opus",channel="sfx1",loop=True,relative_volume=0.05)
    "The path winds through the darkening woods, while crickets chirp the silence of the night away."
    show tenten_walk1 with dissolve
    "Tenten kept walking slightly ahead of you, carving a path through the moonlit forest for the both of you..."
    bot "She seems at ease out here, away from the village. I wonder..."
    scene bg_night_forest2 with Dissolve(1)
    bo"Hey, Tenten..."
    scene bg_night_forest2 with dissolve
    show ten sad2 at center with dissolve
    camera:
        subpixel True
        pos (0.5, 0.5) zoom 1.0 anchor (0.5, 0.5)
        easein 10.0 zoom 1.2
    ten"Hmm? Is something wrong?"
    bo "No. It's just, you haven't told me yet..."
    camera:
        pos (0.5, 0.5) zoom 1.0 anchor (0.5, 0.5)
    with dissolve
    menu:
        bo "You haven't told me yet..."
        "Where are we going?":
            bo"Where are we even going?"
            ten"We are not far off now..."
            hide ten with dissolve
            ten"Keep following me, alright? I promise it's worth the short trail!"
        "Make a silly joke":
            bo"We've been walking for a while now. You aren't... secretly abducting me or anything, are you?"
            ten"*Giggles* Maybe I am..."
            hide ten with dissolve
            ten"Come on, you dumdum, we are almost there..."
    

    hide ten
    hide boruto
    scene black
    with dissolve
    show tenten_walk1 with dissolve
    ten"All I can say is that the place where we are going, it's magical! I kept it all for myself for some time now, but..."
    ten" I thought this time, I'd share it with you! A token of my gratitude for your... friendship!"
    bo"M-magical, huh?"
    ten"Indeed! Fairies flying across the sky, Genies in lamps, anything you could dream of, really!"
    bo"F-fairies?" with vpunch
    ten"*Giggles* I jest of course! Come on, it's right across this passage!"
    scene bg_night_forest3 with Dissolve(1)
    "As the path narrows slightly, your hand brushes against hers. A small spark, a moment of hesitation."
    scene black with dissolve
    bot "Should I...?"
    scene replace_handhold_overlay
    with Dissolve(1)
    scene replace_handhold_overlay:
        subpixel True
        align (0.5, 0.5)
        easein 10 zoom 1.15
    "Taking a quiet breath, you gently let your fingers intertwine with hers."
    "She doesn't pull away. Instead, her fingers tighten slightly around yours."
    ten "..."
    bo "..."
    "You continue walking, hand in hand, the silence now filled with a quiet warmth."
    scene black with dissolve
    pause (1)
    show bg_lake_1 with dissolve:
        zoom 1.3 xalign 0.5 yalign 1.0 subpixel True
    show bg_lake_1:
        easein 10 zoom 1.0 yalign 0.0 subpixel True
    
    $ renpy.sound.play("/audio/soun_fx/lake_owl_ambience.opus",channel="sfx2",loop=True,relative_volume=0.4)
    "Soon you arrive at a lake, hidden between the thick forest woods."
    "Its serenity is a stark contrast to the usual bustle of the village."
    show ten sad2 at center with dissolve
    ten"Here we are!"
    ten"The only place in the world I can let myself loose. Away from all my troubles..."
    hide ten
    scene black
    with dissolve
    "Tenten lets go of your hand as she walks towards the water's edge..."

    show tenten_lookaway_1:
        zoom 1.0 xalign 0.5 yalign 1.0 subpixel True
    show tenten_lookaway_1:
        easein 3 yalign 0.1
    with dissolve
    "She looks back at you as you approach, offering a small, hesitant smile."
    ten "Thank you for accompanying me, [bo_name]..."
    show screen parallax1280("tenten_lookaway_1",1,0.4) with dissolve
    call showscrollingimage from _call_showscrollingimage_98
    hide tenten_lookaway_1
    bo "No problem. It's nice, getting away from it all..."
    hide boruto with dissolve
    menu tenten_lake_date_opening_kind:
        "You scratch your head, wondering what's your next best move."

        "It really is beautiful out here.":
            bo "It really is beautiful out here. Peaceful."
            ten "Yeah... it is. A good place to clear your head."
            bot "Ugh... Smooth, [bo_name]. Real smooth. 'The lake is nice.' Why do I get the feeling that I suck at small talk?"
            ten "Is that what you think we came here to do?"
            ten "Talking about the lake and the weather? *Giggles*"
            bo "Of course!"
            bo "W-wait, I m-mean, of course not!"
            bo "Sorry, I'm not very good at this."
            "She laughs at your nervousness, but in good spirit."
            ten "Don't worry, I'll lead the way!"
            "She winks, leaving you wondering what she could possibly mean."
            jump tenten_lake_date_walk

        "{color=[dominancecolor]}(Make a move){/color}":

            bo "I..."
            show screen parallax1280("lookaway1_1") with dissolve
            call changeDominance(1) from _call_changeDominance_95
            bo"I needed this too, you know..."
            ten "U-umm..."
            bo"Time away from everything, with someone like you..."
            bo"Someone who understands..."
            ten "U-umm... I am not sure I am following, but I am glad you are enjoying this!"
            bo "M-maybe I'll let you in on my own troubles soon enough. Until then, thank you for showing me your secret resort! It's as beautiful as you said..."
            ten"*Giggles* Right?"
            bot "Heh, easy there. Don't want to scare her off."
            bot "It's the first time I get the chance to get a bit closer to her."
            bot "I still don't know how she would react to my usual... urges..."
            bot "Best try not to ruin it."
            scene black
            call hidescrollingimage2 from _call_hidescrollingimage2
            show bg_lake_1
            with dissolve
            jump tenten_lake_date_walk

        "Admit you're nervous":
            bo "You know, I've never really done this sort of thing before..."
            ten "So you're saying... you're nervous? *Giggles*"
            bo "Y-you could say that? But I'm not, c-clueless or anything!"
            ten "I guess we'll see about that."
            bo "Wh-what do you mean?"
            jump tenten_lake_date_walk

label tenten_lake_date_walk:
    ten "Let's walk along the shore for a bit?"
    bo "Sure!"
    call hidescrollingimage2 from _call_hidescrollingimage2_1
    with Dissolve(1)
    scene bg_lake_1 with Dissolve(1)
    "You walk side-by-side along the water's edge. The initial awkwardness begins to fade as you fall into easy conversation."
    show boruto laughing at left with dissolve
    bo "So, besides losing priceless heirlooms, how's the shop been?"
    show ten sad2 at right with dissolve
    ten "Busy, actually. Maybe *too* busy for just one person."
    ten "It gets lonely sometimes, you know? Since my parents..."
    "Her voice starts to tremble."
    show boruto sad with dissolve
    ten "Well, the shop is all I really have left of them, besides the pendant."
    bot "She's opening up... What do I say?"

    menu tenten_lake_date_talk1:
        bot "She's opening up... What do I say?"
        "It must be hard doing it all alone.":
            bo "That sounds tough, Tenten. Running a business, especially with those memories..."
            ten "It is... but it's mine. It keeps me grounded."
            ten "Better than sulking over what could have been."
            ten "I already spent years loathing myself for not being strong enough to protect them..."
            ten "Or bright enough to be a doctor like Ts-"
            show boruto laughing:
                easein 1 xalign 0.7
            bo "Shhhh..."
            bo "You're doing your best and that's what matters."
            jump tenten_lake_date_share_story

        "You should hire some help.":
            bo "If it's too much, maybe you should hire some help?"
            ten "Maybe... but finding someone trustworthy isn't easy. And money's tight."
            ten "It's just... easier to rely on myself, I guess."
            show boruto laughing:
                easein 1 xalign 0.73
            bo "I'm pretty trustworthy!"
            if tenten_mild_grope==True:
                bot "Totally... I didn't just grope her while she was stuck or anything"
                show tenten_stuck_grope1 with flash
                if tenten_used==True:
                    bot "Or used her..."
                    show tenten_hand spank with flash
                    if tenten_godown_anal==True:
                        bot "Or..."
                        show  tenten_lift anilingus1 with flash
            jump tenten_lake_date_share_story

        "Maybe I could help out sometime?":
            show boruto laughing with dissolve
            bo "Hey, if you ever need an extra pair of hands, even just for organizing or something... let me know."
            show boruto laughing:
                easein 1 xalign 0.7
            bo "Consider it part of the... ongoing 'thank you' service."
            ten "R-really? You'd do that? You're not just saying it?"
            if tenten_used==True:
                show boruto sceeming3 with dissolve
                bot "Just like I 'helped' you when you were stuck..."
            bo "Of course I would. What are friends for-"
            bot "Fuck, did I just friendzone myself?"
            ten "I... I might take you up on that. Thanks, [bo_name]."
            jump tenten_lake_date_share_story

label tenten_lake_date_share_story:
    show boruto normal
    show ten angry
    with dissolve
    ten "It still bothers me, though... How did that old creep even get his hands on it?"
    bo"It's okay. We dealt with that, didn't we? It's in the past..."
    show screen image_with_border("tenten_cutout1",0.5) with dissolve
    "You place your arm around her waist and re-assure her..."
    call increaselust(10) from _call_increaselust_225
    bot"That ass though..."
    if percentage>=50:
        call checkLust(50) from _call_checkLust_16
        show boruto bonersurprised with dissolve
        bot"Might have solved one problem, but another arises!"

        menu tenten_lake_date_ass_thoughts:
            bot"Not sure who's going to deal with my problem..."
            "Snap out of it":
                bot "Must. Resist. The urge! Keep it professional... mostly."

            "{color=[dominancecolor]}Grab her ass{/color}":                
                bo"He did seem capable of moving fast, when I met him..."
                show boruto snob with dissolve
                call changeDominance(1) from _call_changeDominance_96
                show screen image_with_border("tenten_cutout1_2",0.5) with dissolve
                $ renpy.sound.play("/audio/soun_fx/grope1.opus", channel="sfx3", loop=False)
                show ten angry with dissolve
                show ten at smallshake
                bo"Somewhat like this..."
                bot "(Heh, couldn't resist.)"
                hide screen image_with_border
                call checkDominance(15,"tenten_lake_date_fail_permanent_label") from _call_checkDominance_30
                show boruto surprised2:
                    easein 0.3 xalign 0.3
                show ten at smallshake
                ten "Hey! What was that for?!" with vpunch
                bo "Sorry, I got carried away!"
                ten "I-idiot! Consider that your last warning..."
                show ten normal with dissolve
                ten"A lady deserves proper treatment, you know?"
                ten "Like I was saying..."

            "Cop a feel":
                show boruto sceeming2 with dissolve:
                    zoom 1.0 xpos 0.8
                show screen image_with_border("tenten_cutout1_1",0.5) with fade
                $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx3", loop=False)
                "You lean in closer and wrap your other arm around her bottom..."
                bot "Just a little squeeze!"
                show boruto surprised
                hide screen image_with_border
                show boruto surprised2:
                    easein 0.3 xalign 0.3
                show ten at smallshake
                ten "[bo_name]! W-what is that for!" with vpunch
         
                show boruto embarassed
                with dissolve
                bo "S-sorry, just trying to offer a comforting touch..."
                ten "Idiot... consider that your last warning."
                ten "Like I was saying,"


    show boruto normal
    hide screen image_with_border
    with dissolve

    ten "Can't believe I was careless enough to lose it in the backroom, while I was... indisposed. Did he somehow sneak in? Pick the lock?"
    show ten sad1 with dissolve
    ten "With everything going on... the Hokage being away, the Daimyo imposing harsher taxes on small establishments like mine, it feels like bad things just keep happening one after another..."
    ten "Then, an old weirdo steals my family's keepsake. I just can't catch a break, you know?"
    show boruto worried with dissolve
    bo "Yeah, sounds like a lot to deal with..."
    ten "It's just... after the war, everything changed. People left, priorities shifted."
    show boruto sad with dissolve
    ten "Sometimes it feels like everyone moved on, found new connections... and I'm still just the shop gal."
    show boruto sad with dissolve:
        easein 1 xalign 0.0
    bot "Loneliness... I know something about that, even surrounded by family."
    bo "I get that. Feeling... disconnected, even when you're not technically alone."
    ten "You do?"

    menu tenten_lake_date_boruto_share:
        bot "Should I tell her? Even just a little bit about the curse? She seems trustworthy now..."

        "Be vague.":
            show boruto sad:
                easein 1 
            bo "Yeah. Sometimes it feels like... there's something isolating me. Something nobody else really understands."
            bot "Best not to mention the curse directly. Don't want to freak her out."
            ten "I think I know what you mean. Like carrying a weight others can't see."
            jump tenten_lake_date_connection

        "Change the subject":
            bo "Anyway! Enough heavy stuff. Look how clear the water is today."
            ten "Oh... yeah. It is."
            bot "Maybe not the right time to share."
            jump tenten_lake_date_activity_suggest


label tenten_lake_date_connection:
    "A comfortable silence falls between you."
    "Tenten seems to be processing what you shared..."
    show ten sad2 with dissolve
    ten "Thanks for... telling me that, [bo_name]. Even if it was... vague."
    ten "It helps to know you're not alone in feeling... weird, sometimes."
    ten "Makes you seem a little less like the annoying brat your father used to be, and more... human."
    show boruto embarassed with dissolve
    bo "Hey! I am creative, not annoying."
    "You both share a light laugh, breaking the tension."

    show ten normal with dissolve
    ten "It's getting kind of hot though, isn't it?"
    ten "The water looks really inviting..."
    show boruto surprised with dissolve
    bot "Is she suggesting...?" with vpunch

    jump tenten_lake_date_activity_suggest


label tenten_lake_date_activity_suggest:
    menu tenten_lake_date_swim_choice:
        bot "She seems relaxed now. Maybe..."

        "Thinking of going for a swim?":
            show boruto embarassed with dissolve
            bo "Thinking of going for a swim, Tenten?"
            "She glances at you hesitantly."
            ten "Maybe... If you are? Don't want to swim alone."
            show boruto surprised2 with dissolve
            bot "She's actually considering it." with vpunch
            jump tenten_lake_date_swim_confirm

        "{color=[hatredcolor]}Too shy to admit you just wanna hookup?{/color}":
            call changeHatred(1) from _call_changeHatred_152
            show boruto sceeming2 with dissolve
            bo "Tenten..."
            bo "If you want a taste of me you can just say it plainly."
            show boruto sceeming3 with dissolve:
                easein 2 xalign 0.75
            #? Add something more, you already have the assets.
            pause 0.4
            show ten angry with dissolve
            show screen image_with_border("tenten_cutout1_2",0.5) with dissolve
            show ten at smallshake
            $ renpy.sound.play("/audio/soun_fx/grope1.opus", channel="sfx3", loop=False)
            bo "You wouldn't be the first!"
            hide screen image_with_border
            scene black
            with vpunch
            ten"E-enough!"
            ten"To think I ever gave you a chance..."

            jump tenten_lake_date_fail_permanent_label

label tenten_lake_date_swim_confirm:
    menu tenten_lake_date_swim_decision:
        "Yeah, let's do it!":
            show boruto embarassed with dissolve
            bo "Last one in is cleaning shuriken for a week!"
            ten "You're on!"
            $ tenten_lake_swim = True
            hide boruto
            hide ten
            hide bg_lake_1
            scene black
            with Dissolve(1)
            jump tenten_lake_date_undress

        "I'm sorry Tenten, but my heart belongs to someone else":
            show boruto 
            bo "I'm sorry Tenten, but my heart belongs to someone else."
            show ten angry with dissolve
            ten "What? It's not like that!"
            ten "Are you seriously implying I was trying to..."
            ten "You're only a kid!"
            jump tenten_lake_date_fail_retry
        
        "{color=[dominancecolor]}We could do more than just swimming!{/color}":
            call changeDominance(1) from _call_changeDominance_97
            show boruto sceeming2 with dissolve:
                easein 2 xalign 0.73
            bo "Oh I'm thinking about a few more things besides swimming..."
            show screen image_with_border("tenten_cutout1",0.5) with dissolve
            call checkDominance(20,"tenten_lake_date_fail_permanent_label") from _call_checkDominance_31
            ten "I am not s-sure I follow ..."
            bo "Come on, you'll find out once we dip in!"
            ten "Right..."
            scene black
            hide screen image_with_border
            with Dissolve(1)
            jump tenten_lake_date_undress

label tenten_lake_date_fail_permanent_label:
    hide screen image_with_border
    $ tenten_lake_date_fail_permanent = True
    $ tenten_date_agreed = False
    $ tenten_date_success = False
    stop sound channel "sfx1"
    stop sound channel "sfx2"
    stop sound channel "sfx3"
    $ playmusic("audio/ost/lakedate_fail.opus",0.5)
    $ renpy.sound.play("/audio/soun_fx/crickets.opus",channel="sfx1",loop=True,relative_volume=0.05)
    $ renpy.sound.play("/audio/soun_fx/lake_owl_ambience.opus",channel="sfx2",loop=True,relative_volume=0.4)
    scene black with vpunch
    scene bg_lake_1
    show ten angry at right
    show boruto surprised at left
    with dissolve
    ten "I'm disappointed in you."
    ten "So all this was just to... take advantage of me?"
    ten "I was stupid to think you were ever really listening to me."
    ten "You can find your own way back to the village."
    ten "I'm leaving."
    show ten angry with dissolve:
        easein 1 xpos 2500
    bot "W-whatever! She's way too sensitive, sheesh!"
    show boruto angry with dissolve
    bot "Her loss!" with vpunch
    jump action_taken

label tenten_lake_date_fail_retry:
    $ tenten_lake_date_fail_retry += 1
    $ tenten_date_agreed = False
    $ tenten_date_success = False
    $ tenten_date_counter += 1
    $ tenten_date_shop_dialogueflavor_mentioned = False
    stop sound channel "sfx1"
    stop sound channel "sfx2"
    stop sound channel "sfx3"
    $ playmusic("audio/ost/lakedate_fail.opus",0.5)
    $ renpy.sound.play("/audio/soun_fx/crickets.opus",channel="sfx1",loop=True,relative_volume=0.05)
    $ renpy.sound.play("/audio/soun_fx/lake_owl_ambience.opus",channel="sfx2",loop=True,relative_volume=0.4)
    scene black with dissolve
    pause(1.0)
    scene bg_lake_1
    show ten angry at right
    with dissolve
    ten "I think we got off on the wrong foot here."
    show boruto surprised at left with dissolve
    ten "You should take some time alone to figure out what you want."
    bo "B-but... Tenten I-"
    ten "You can find your own way back home!" with vpunch
    show ten angry with dissolve:
        easein 1 xpos 2500
    bo "Well that went... Well, I guess?"
    show boruto sad with dissolve
    bot "...fuck."
    bot "Maybe I should change my approach slightly next time..."
    bot "...if there is a next time."
    jump action_taken

label tenten_lake_date_undress:
    ten "Okay, um... maybe turn around? Give a girl some privacy?"
    show screen parallax1280("tenten_lookaway_2") with flash
    call showscrollingimage from _call_showscrollingimage_99
    bo "O-okay..."
    call hidescrollingimage2(text="Click twice to turn around without peeking.") from _call_hidescrollingimage2_2
    "You turn your back."
    bot "Okay [bo_name], be cool... No peeking now that she started trusting you..."
    menu:
        "I'm gonna peek anyway.":
            $ tenten_date_peeked = True
            show tenten_lake_back_undress with flash:
                zoom 1.25 xalign 0.5 yalign 1.0
            show tenten_lake_back_undress with dissolve:
                zoom 1.25 xalign 0.5 yalign 0.0
            show tenten_lake_back_undress_full with flash:
                zoom 1.25 xalign 0.5 yalign 1.0
            show tenten_lake_back_undress_full with dissolve:
                zoom 1.25 xalign 0.5 yalign 0.0
            scene black
            with dissolve
            bot "Whoa... Definitely worth it!"
            call increaselust(10) from _call_increaselust_226
        "Don't":
            bot "Nope. Not gonna do it. Earn that trust."

    $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus",channel="sfx1",loop=False,relative_volume=0.5)
    "You hear the rustle of clothing behind you."
    $ renpy.sound.play("/audio/soun_fx/waterjump.opus",channel="sfx1",loop=False,relative_volume=0.5)
    "And then a splash of water..."
    ten "Okay... you can turn around now!"
    show screen parallax1280("pov2_talk", 1.25, 0.5, False) with flash
    call showscrollingimage from _call_showscrollingimage_100
    bot "Did she get... fully naked!?"
    bot"I thought she'd come prepared in a swimsuit or s-something..."
    hide screen parallax1280
    show screen parallax1280("pov2_1talk", 1.25, 0.3, False)
    with dissolve
    ten"Are you coming in or are you going to sit there and stare? Come on, time to get undressed! *Giggles*"
    bo"R-right here? Y-you don't mind if I...?"
    ten"Go on, you klutz! Did you think a woman of my age would be fazed by something as mild as a boy's body?"
    call hidescrollingimage2("Click twice to undress...") from _call_hidescrollingimage2_3
    scene bg_lake_1 with dissolve
    show boruto surprised2 with dissolve
    bo"If you say so..."
    $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus",channel="sfx1",loop=False,relative_volume=0.5)
    show boruto naked1_surprised with fade:
        zoom 0.4
    pause 0.8
    show pov2_1talk with dissolve:
        zoom 1.25 xalign 0.5 yalign 0.3
    ten "{size=-4}*Mutters Silently* Oh m-my! Not what I expected... at all!{/size}"
    bo "R-right. Make way, I'm going in!"
    jump tenten_lake_date_swimming

label tenten_lake_date_swimming:
    scene black with vpunch
    $ renpy.sound.play("/audio/soun_fx/waterjump2.opus",channel="sfx1",loop=False,relative_volume=0.5)
    pause(0.5)
    show screen parallax1280("both_in_lake_submerged", 1.25) with flash
    call showscrollingimage from _call_showscrollingimage_101
    bot "She looks incredible like this. relaxed, carefree. It's hard not to stare, especially at her..."
    bot "Hopefully she doesn't notice that my eyes are fixated on her tits!"
    ten "A-are you okay..?"
    call hidescrollingimage2 from _call_hidescrollingimage2_4
    jump tenten_lake_date_release_check


label tenten_lake_date_release_check:
    # Condition flares up
    # $ renpy.sound.play("/audio/soun_fx/boruto_pain_groan.opus", channel="sfx2", loop=False, relative_volume = 0.8) # Pain sound
    stop music fadeout 1
    $ renpy.sound.play("/audio/soun_fx/bassstart.opus",channel="sfx1",loop=False,relative_volume=0.5)
    $ renpy.sound.play("/audio/soun_fx/introbass3.opus",channel="sfx2",loop=True,relative_volume=0.7)
    show screen parallax1280("both_in_lake_slightly_submerged", 1.25, 0.5, False) with flash
    call increaselust(50) from _call_increaselust_227
    bo "I'm f-"
    call showscrollingimage from _call_showscrollingimage_102
    show screen parallax1280("both_in_lake_slightly_submerged2", 1.25, 0.5, False) with dissolve
    bo "*Groans softly*" with vpunch
    ten "[bo_name]? What's wrong! You look like you are in pain..."
    $ renpy.sound.play("/audio/soun_fx/heartbeatlong.opus",channel="sfx1",loop=True,relative_volume=0.5)
    bo "I... It's nothing."
    if tenten_lake_shared_story == True: 
        bo "Just... It's the... condition I mentioned."
        ten "The pain? Is it bad? Can I... Can I do anything?"
    else:
        ten "Are you sure? You look like you're really hurting. Can I do anything to help?"

    menu tenten_lake_date_ask_help:
        ten "Is there... anything I can do?"

        "Explain your condition":
            bo"Let me just..."
            show screen parallax1280("blackscreen", 1.25, 0.5, False) with dissolve
            bo"...Take a b-breather!"
            call decreaselust(10) from _call_decreaselust_101
            show screen parallax1280("both_in_lake_slightly_submerged", 1.25, 0.5, False) with dissolve
            bo "It's... it's really hard to talk about, Tenten. But you asked... and you deserve the truth."
            bo "Remember how you told me you lost your parents? How the shop is all you have left?"
            ten "Yeah...?"
            bo "Well, my [na_rel]... he left something behind for me too. Not as nice as your inheritance, but... a heavy burden instead."
            bo"A curse..."
            show screen parallax1280("both_in_lake_slightly_submerged3", 1.25, 0.5, False) with dissolve
            ten "A curse? You don't mean... *Gasps*" with vpunch
            ten"The Kyuubi's curse? I've seen what it did to [na_name]..."
            show screen parallax1280("both_in_lake_slightly_submerged", 1.25, 0.5, False) with dissolve
            bo "Not exactly that. Tsunade studied it. It's tied to what happened to him... the Jinchūriki stuff, but it's different."
            bo "It's called PGAD, or s-something. Something about being in a constant state of a-arousal..."
            bo "Sounds almost funny, right? But it really isn't. It's dangerous. I, am dangerous... Tenten."
            ten "D-dangerous..? How?"
            bo "It... it messes with everything. My emotions are all over the place, I get irritable for no reason..."
            bo "Tsunade said it even affects my body, makes me stronger, but also causes..." 
            bo "Problems... down there."
            bo "The worst part is the arousal. It's constant. And the urges... they get overwhelming. Depraved even."
            bo "It's not just wanting... it's needing. And it spreads, gets worse, if I stay aroused for too long without..."
            bo "Without climaxing. Regularly."
            ten "[bo_name]... That's..."
            bo "If I don't manage it... if I let it fester... Tsunade said I could become a danger. To myself, to people I care about."
            bo "How can you trust someone who needs... *that*... just to stay sane? To not become a monster?"
            ten "[bo_name]..."
            ten "Wow... I had no idea. To carry that burden... the constant need, the fear... That's... horrible."
            ten "You're not a monster, [bo_name]! You're fighting something immense. And you're alone n-now..."
            ten "I'm here for you, and I'm not gonna judge y-"
            show screen parallax1280("both_in_lake_slightly_submerged2", 1.25, 0.5, False) with dissolve
            call increaselust(20) from _call_increaselust_228
            "Your breathing is shaky, you feel it fester in your stomach..."
            bo "But right now... the pain, the urge, it's..." with vpunch
            bo "It's getting really bad again. I... I need..."

            menu ask_sex_scene:
                bo "It's getting really bad again. I... I need..."

                "Ask for a handjob":
                    bo "Yeah... Could you... help me? Just... with your hand?"
                    ten "[bo_name], this is... I know your mom and dad, this is just... What would they think?"
                    bo "You're probably right, I shouldn't h-..."
                    ten "No... wait. Okay, Okay! If it really helps you with your pain... then I'll do it."
                    
                    jump tenten_lake_date_handjob_scene

                "Grab her ass":
                    call hidescrollingimage2 from _call_hidescrollingimage2_5
                    jump tenten_lake_date_assgrab_fail

                "Ask if you can grab her ass":
                    jump tenten_lake_date_assgrab

                "Ask if you can suck on her breasts":
                    jump tenten_lake_date_titsuck

                "{color=[obediencecolor]}???{/color}":
                    "Complete a date with Tenten successfully to unlock!"
                    jump ask_sex_scene
            
        "No, I'll be fine. (Refuse help)":
            bo "No, no! I'll... manage."
            ten "Are you sure? You look like you're in a lot of pain."
            show screen parallax1280("blackscreen", 1.25, 0.5, False) with dissolve
            bo "I'm fine I just... need a minute."
            call decreaselust(20) from _call_decreaselust_102
            show screen parallax1280("both_in_lake_slightly_submerged", 1.25, 0.5, False) with dissolve
            bot "I'd rather not drag her into this right now..."
            $ renpy.sound.stop(channel="sfx1")
            $ renpy.sound.stop(channel="sfx2")
            $ renpy.sound.stop(channel="sfx3")
            $ playmusic("audio/ost/lakedate.opus",0.3)
            call hidescrollingimage2 from _call_hidescrollingimage2_6
            scene black with dissolve
            "Eventually, you get your urges under control, and you fall back into easy conversation"
            "Time passes faster than you both realize, until you eventually decide to make your way back to the village..."
            jump tenten_lake_date_ending_kind

label tenten_lake_date_handjob_scene:
    $ tenten_date_handjob = True
    $ tenten_helped_release = True
    ten "O-okay... um... where...?"
    show screen parallax1280("blackscreen", 1.25, 0.5, False) with dissolve
    bo "We are a-alone, are we not?"
    "Tenten looks around nervously..."
    $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
    "She gestures vaguely for you to follow her."
    bot "She... she actually agreed. Out of kindness..."
    bot"Maybe she is into m-me?"
    bot "No... I can't fall into that trap of wishful thinking and risk ruining things, best not make any assumptions yet..."
    scene black
    call hidescrollingimage2 from _call_hidescrollingimage2_7
    $ renpy.sound.play("/audio/soun_fx/water_move_4.opus", channel="sfx1", loop=False, relative_volume = 0.5)
    "You walk to a slightly more shallow part of the lake."
    $ renpy.sound.play("/audio/soun_fx/water_move_3.opus", channel="sfx1", loop=False, relative_volume = 0.5)
    $ playmusic("audio/ost/lakedate.opus",0.3)
    $ renpy.sound.play("/audio/soun_fx/crickets.opus",channel="sfx2",loop=True,relative_volume=0.05)
    $ renpy.sound.play("/audio/soun_fx/lake_owl_ambience.opus",channel="sfx3",loop=True,relative_volume=0.4)
    show hj2 with dissolve:
        zoom 1.25 xalign 0.5 yalign 1.0
    show hj2:
        easein 3 yalign 0.0
    ten"It's growing so f-fast... Is it painful?"
    bo "Y-yeah..."
    show screen parallax1280("hj2", 1.25, 1.0) with dissolve
    call showscrollingimage from _call_showscrollingimage_103
    ten "*Gasps softly* D-don't let it just poke me..." with vpunch
    bo"I can't quite c-control it you know..."
    ten"The heat it emanates, I can feel it..."
    ten"I can almost sense your p-pain through it. It's so ...hardened too."
    bo "Part of the curse, I t-think..."
    "She takes a deep breath."
    ten "Then..."
    scene black with dissolve
    call hidescrollingimage2 from _call_hidescrollingimage2_8
    "Hesitantly, she reaches out. Her touch is surprisingly gentle."
    ten"Leave it to my capable hands..."
    $ renpy.sound.play("/audio/soun_fx/water_move_2.opus", channel="sfx1", loop=False, relative_volume = 0.5)
    scene hj4 with dissolve
    "Her hand closes around you, still slightly trembling..."
    show screen parallax1280("tenten_handjob_1", 1.25, 0.8) with dissolve
    $ renpy.sound.play("/audio/soun_fx/handjob1.opus", channel="sfx1", loop=True, relative_volume = 1.0)
    "She starts a slow, uncertain rhythm..."
    bo "Tenten..."
    "She starts a slow, uncertain rhythm..."
    ten "Is this... h-helping?"
    menu hj_option_1:
        ten "Is this... h-helping?"
        "Enjoy the process...":
            bo "Just like that..."
            pass
        "Come on, f-faster!":
            bo "Y-yeah... faster... maybe?"
            label date0gofaster:
            $ renpy.sound.play("/audio/soun_fx/water_move_2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            $ renpy.sound.play("/audio/soun_fx/handjob2.opus", channel="sfx1", loop=True, relative_volume = 1.0)
            show screen parallax1280("tenten_handjob_1_fast", 1.25, 0.8) with dissolve
            "She nods, blushing furiously but increasing the pace. Her movements become more erratic."
            ten "I... I can't believe I'm doing this..."
            bo "Ah... y-yes! Faster, Tenten! Please!"
            ten "You are getting really a-anxious, are you not?"
            bo "Ngh... Don't stop..."
            ten "Just... tell me when..."
            bo "A-almost... there!"
            ten"It's best if I end this quickly then..."
            call hidescrollingimage2 from _call_hidescrollingimage2_9
            $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            label date0gofaster_2:
            scene hj3 with dissolve:
                xzoom -1
            "She brings herself closer to you, her stomach brushing against the tip of your manhood while she keeps delicately working the shaft..."
            show tenten_handjob_2 with dissolve
            bo"T-tenten..."
            ten"Don't worry. I'll take care of it for you..."
            show tenten_handjob_2_fast with dissolve
            ten"This ought to get the job done!"
            bot"F-fuck! She is kinda good at t-this..."
            bot"I can't hold on any longer!" with flash
            ten"It's pulsating... t-throbbing!"
            scene hj3 with dissolve:
                xzoom -1
            ten"You are about to... aren't you?"
            $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            show hj3_cum1 with flash:
                xzoom -1
            bo"S-sorry... I am c-cumming!" with flash
            ten"It's okay... Let it all out..."
            bo"Aaahh! *Moans*" with vpunch
            $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            show hj3_cum1_1 with longerflash:
                xzoom -1
            $ renpy.sound.stop(channel="sfx1")
            $ renpy.sound.stop(channel="sfx2")
            $ renpy.sound.stop(channel="sfx3")
            call decreaselust(100) from _call_decreaselust_103
            ten"..."
            bo"*Heavy breathing*..."
            ten"...F-feeling better?"
            bo"M-much better. Thank you, Tenten..."
            ten"*Sigh*"
            ten"Look at this mess you made..."
            scene black with dissolve
            bo"My a-apologies..."
            ten"Come on, let's wash ourselves..."
            $ renpy.sound.play("/audio/soun_fx/water_move_2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            show screen parallax1280("both_in_lake_submerged2",1.25) with dissolve
            call showscrollingimage from _call_showscrollingimage_104
            jump date0endingjump
    ten"Just... r-relax, okay?"
    bot "She's... actually good at this. And she's doing it... for me."
    menu dialogue_option_hj:
        "I'm glad you got your pendant back":
            bo "The pendant..."
            bo "I'm glad-"
            scene black with dissolve
            hide hj3
            "You didn't even manage to finish your sentence when..."
            $ renpy.sound.play("/audio/soun_fx/water_move_3.opus", channel="sfx1", loop=False, relative_volume = 0.5)
            show screen parallax1280("hj", 1.25) with dissolve
            call showscrollingimage from _call_showscrollingimage_105
            $ renpy.sound.play("/audio/soun_fx/kiss1.opus", channel="sfx3", loop=False, relative_volume = 1.0)
            "...She leans in and unexpectedly interrupts you with a kiss."
            bot "!" with vpunch
            bot"M-my first real kiss..."
            
        "{color=[dominancecolor]}You're an expert at this!{/color}":
            call changeDominance(1) from _call_changeDominance_98
            bo "You're an expert at this!"
            ten "Sh-shut up idiot..."
            ten "I don't do stuff like this often..."
            ten "I'm just trying to help with your.. p-problem, just like you helped with mine..."
            $ expert_option = True
                
    menu hj_option_2:
        bo "..."
        "{color=[dominancecolor]}Reach for a kiss{/color}" if expert_option == True:
            if dominance >= 15:
                
                bo"Tenten, I am sorry but..."
                call checkDominance(15,"none") from _call_checkDominance_32
                show screen parallax1280("hj7_grabtit", 1.25) with dissolve
                bo"You are too pretty for me not to make a move..."
                "You reach in for a kiss, and a little something more..."
                show screen parallax1280("blackscreen", 1.25) with vpunch
                "Tenten pushes you slightly back by gently pressing her palm against your chest..."
                ten"That was... a bit s-sudden!"
                ten"A heads up would be nice! Like..."
                $ renpy.sound.play("/audio/soun_fx/kiss1.opus", channel="sfx3", loop=False, relative_volume = 1.0)
                show screen parallax1280("hj", 1.25) with dissolve
                ten"...This!"
                bot"O-oh...? She went in for it herself!" with vpunch
                bot"And she keeps s-stroking my cock! I think I am about to..." with flash
                show screen parallax1280("hj2", 1.25) with dissolve
                "She pulled back momentarily..."
                ten"Bet you enjoyed that one..."
                call changeDominance(1) from _call_changeDominance_99
                bo"Almost as much as you did!"
                ten"Oh you..."
                show screen parallax1280("blackscreen", 1.25) with vpunch
                ten"Job's not finished, is it...? *Giggles*"
                call hidescrollingimage2 from _call_hidescrollingimage2_10
                jump date0gofaster_2
            else:
                show screen parallax1280("hj7_grabtit", 1.25) with dissolve
                ten"*Gasps*" with vpunch
                call checkDominance(15,"none") from _call_checkDominance_33
                "You reach in for a kiss, but you reached for more than what Tenten was comfortable with..."
                show screen parallax1280("hj2", 1.25) with dissolve
                ten"H-hey, careful!"
                bo"S-sorry..."
                ten"Just, follow my lead, okay...?"
                call hidescrollingimage2 from _call_hidescrollingimage2_11
                jump date0gofaster


            "You instinctively reached for her breasts!"
            $ renpy.sound.play("/audio/soun_fx/water_move_5.opus", channel="sfx1", loop=False, relative_volume = 0.5)
            show screen parallax1280("hj7_grabtit", 1.25) with flash
            call showscrollingimage from _call_showscrollingimage_106
            ten "[bo_name_stutter]!"
            bo "Just... keep going..."
        

        "Enjoy the kiss..." if expert_option == False:
            $ renpy.sound.play("/audio/soun_fx/kiss1.opus", channel="sfx3", loop=False, relative_volume = 1.0)
            "You kept exploring each other's lips, while Tenten kept gently stroking your manhood..."
            bot"She..."
            bot"She has a nice t-taste to her. I think I am about to..." with flash
            show screen parallax1280("hj2", 1.25) with dissolve
            "She pulled back momentarily..."
            ten"Bet you enjoyed that one..."
            bo"Tenten, I-"
            show screen parallax1280("blackscreen", 1.25) with vpunch
            ten"Job's not finished, is it...? *Giggles*"
            call hidescrollingimage2 from _call_hidescrollingimage2_12
            jump date0gofaster_2

    label date0endingjump:
    ten "Oh dear..."
    bo "T-thank you, Tenten. I... I feel much better. The pain's gone."
    "You both avoid each other's gaze, feeling somewhat flustered by what transpired..."
    ten "G-good... Just don't mention this. To anyone. Ever."
    bo "R-right. This will be our secret..."
    call hidescrollingimage2 from _call_hidescrollingimage2_13
    scene black with dissolve

    jump tenten_lake_date_ending_kind

label tenten_lake_date_assgrab_fail:
    $ tenten_assgrab_fail = True
    call changeDominance(1) from _call_changeDominance_100
    $ renpy.sound.play("/audio/soun_fx/spank7.opus", channel="sfx3", loop=False)
    show screen parallax1280("2h_assgrab",1.25,1.0)
    call showscrollingimage from _call_showscrollingimage_107
    with vpunch
    ten "Hey! [bo_name], what do you think you're doing?!"
    call hidescrollingimage2 from _call_hidescrollingimage2_14
    $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
    scene black with dissolve
    show screen parallax1280("pov2_angry",1.25,0.3) with dissolve
    ten "I offered to help you because you said you were in pain, not so you could just... grope me!"
    ten "I thought maybe you were different, but you're just like everyone else!"
    call hidescrollingimage2 from _call_hidescrollingimage2_15

    "Tenten stepped out of the water to dry herself..."
    show tenten_lake_back_undress with dissolve:
        zoom 1.25 xalign 0.5 yalign 0.0
    show tenten_lake_back_undress:
        easein 6 yalign 1.0
    bot"Fuck! Can't believe I blew my chances with her..."
    scene black with dissolve
    jump tenten_lake_date_fail_retry

label tenten_lake_date_assgrab:
    $ tenten_assgrab_normal = True 
    bo "Can I just... feel your ass for a few seconds?"
    bo "It... it helps ground me sometimes. When the curse flares up... Physical contact..."
    ten "Grab... my ass? Seriously? Is that... part of the 'treatment' Tsunade mentioned?"
    ten "I... I don't know, [bo_name]... This feels..."
    bo "Please, Tenten? Just for a moment? If it doesn't help, I'll stop."
    ten "...Okay. Fine. Just... be quick about it."
    call hidescrollingimage2 from _call_hidescrollingimage2_16
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
    $ playmusic("audio/ost/lakedate.opus",0.3)
    $ renpy.sound.play("/audio/soun_fx/lake_owl_ambience.opus",channel="sfx2",loop=True,relative_volume=0.4)
    show screen parallax1280("1h_assgrab",1.25) with dissolve
    call showscrollingimage from _call_showscrollingimage_108
    call increaselust(10) from _call_increaselust_229
    ten "*Gasps softly* O-okay...?"

    menu lakedate_assgrab_choice1:

        "Pull her close and wholly grab her ass":
            call hidescrollingimage2 from _call_hidescrollingimage2_17
            scene black with dissolve
            pause(0.5)
            $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
            show screen parallax1280("2h_assgrab_v2",1.25) with dissolve
            ten "[bo_name_stutter]!"
            menu lakedate_assgrab_choice2:
                "{color=[hatredcolor]}Finger her ass{/color}":
                    call changeHatred(1) from _call_changeHatred_153
                    bo "Tenten... Bent over a bit more... just for a second."
                    ten "Wh-what? Why?"
                    call hidescrollingimage2 from _call_hidescrollingimage2_18
                    scene black with dissolve
                    "Before she can fully react, you move your hand right between her asscheeks, your fingers probing gently at first."
                    show screen parallax1280("finger",1.25,1.0) with flash
                    $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                    call showscrollingimage from _call_showscrollingimage_109
                    ten "Eek! [bo_name]! Stop it! What are you doing?!" with vpunch
                    call hidescrollingimage2 from _call_hidescrollingimage2_19
                    scene black with dissolve
                    $ renpy.sound.play("/audio/soun_fx/water_move_2.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                    "She pushes you away forcefully, eyes wide with betrayal and disgust."
                    show screen parallax1280("pov2_angry",1.25,0.3) with dissolve
                    ten "I offered to help you because you said you were in pain, not so you could just... do that to me!"
                    ten "I thought maybe you were different, but you're just like everyone else!"
                    call hidescrollingimage2 from _call_hidescrollingimage2_20
                    "Tenten stepped out of the water to dry herself..."
                    show tenten_lake_back_undress with dissolve:
                        zoom 1.25 xalign 0.5 yalign 0.0
                    show tenten_lake_back_undress:
                        easein 6 yalign 1.0
                    bot"Fuck! Can't believe I blew my chances with her..."
                    scene black with dissolve                    
                    call hidescrollingimage2 from _call_hidescrollingimage2_21
                    jump tenten_lake_date_fail_permanent_label

                "{color=[dominancecolor]}Touch her pussy{/color}":
                    $ tenten_pussy_fail = True
                    bo "Just... let me..."
                    call hidescrollingimage2 from _call_hidescrollingimage2_22
                    scene black with dissolve
                    "You shift your grip slightly, letting your fingers slip inside her pussy."
                    $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                    call changeDominance(1) from _call_changeDominance_101
                    show screen parallax1280("finger_front",1.25) with flash
                    call showscrollingimage from _call_showscrollingimage_110
                    ten "N-no! [bo_name], don't!" with vpunch
                    call hidescrollingimage2 from _call_hidescrollingimage2_23
                    scene black with dissolve
                    $ renpy.sound.play("/audio/soun_fx/water_move_2.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                    "She shoves your hand away, looking horrified."
                    show screen parallax1280("pov2_angry",1.25,0.3) with dissolve
                    ten "I said I'd help, but... not like that! What's wrong with you?!"
                    bo"S-sorry! I thought we had something going here..."
                    ten"Ugh! Men..."
                    scene black
                    call hidescrollingimage2 from _call_hidescrollingimage2_24
                    ten"Boys, rather!" with vpunch
                    ten"Immature little boys..."
                    "Tenten stepped out of the water to dry herself..."
                    show tenten_lake_back_undress with dissolve:
                        zoom 1.25 xalign 0.5 yalign 0.0
                    show tenten_lake_back_undress:
                        easein 6 yalign 1.0
                    bot"Fuck! Can't believe I blew my chances with her..."
                    scene black with dissolve                    
                    call hidescrollingimage2 from _call_hidescrollingimage2_25
                    jump tenten_lake_date_fail_retry

                "{color=[dominancecolor]}Fuck her thighs{/color}":
                    call checkDominance(20,"lakedate_assgrab_choice2") from _call_checkDominance_34
                    $ tenten_date_thighfuck = True
                    bo "Just like this... hold still..."
                    call hidescrollingimage2 from _call_hidescrollingimage2_26
                    scene black with dissolve
                    "You reposition yourself slightly, pressing your hardening erection against the inside of her upper thighs, trapping it between them."
                    $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                    show screen parallax1280("tenten_ts_anim1",1.25, 0.8) with flash
                    call showscrollingimage from _call_showscrollingimage_111
                    
                    ten "Wh-what are you...? [bo_name]! This is...!"
                    "She tenses up, her breathing becoming shallow..."
                    bo"Is it o-okay if I..."
                    call hidescrollingimage2("Click twice to thrust deeper!") from _call_hidescrollingimage2_27
                    call changeDominance(1) from _call_changeDominance_102
                    hide screen parallax1280
                    show screen parallax1280("tenten_ts_anim1_1",1.25, 0.8) with vpunch
                    ten"I d-don't know, you tell me. Is it... okay?"
                    ten"Is this what you need to f-feel better?"
                    ten"Not exactly w-what I had in mind you know..."
                    call hidescrollingimage2("Click twice to use her thighs!") from _call_hidescrollingimage2_28
                    $ renpy.sound.play("/audio/soun_fx/handjob3.opus", channel="sfx1", loop=True, relative_volume = 0.8)
                    hide screen parallax1280
                    show screen parallax1280("tenten_thighsex_1",1.25, 0.8)
                    with dissolve
                    bo"Me n-neither, but s-sometimes..."
                    ten"Good l-lord, [bo_name_stutter]!?"
                    bo "Ngh... Tenten... your thighs... so soft... so warm..."
                    ten "[bo_name]! Wh-what are you doing?! That's not...!"
                    bo "Can't... help it... Feels too good... Need this... The curse..."
                    ten "Is.. is it really helping?"
                    bo "Just... hold still... please..."
                    "She bites her lip, looking torn between pulling away and letting you continue, her hands gripping your shoulders tightly."
                    call hidescrollingimage2("Click twice to thrust harder!") from _call_hidescrollingimage2_29
                    hide screen parallax1280
                    show screen parallax1280("tenten_thighsex_1_fast",1.25, 0.8)
                    with dissolve
                    bo "Ngh... Almost... Tenten, just a bit more..."
                    ten "You're... you're going so fast...!"
                    bo "It feels... so good... Hnngh!"
                    ten "*Small gasp* Be careful...!"
                    scene black with dissolve
                    $ renpy.sound.play("/audio/soun_fx/water_move_3.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                    show screen parallax1280("tenten_ts_anim2",1.25) with flash
                    bo "*Hhh... Ngh...*"
                    ten "..."
                    jump lakedate_thighjob_choice

                    menu lakedate_thighjob_choice:
                        ten "..."
                        "Keep going...":
                            bo "Almost there, Tenten... just... hold on..."
                            show screen parallax1280("tenten_thighsex_2",1.25, 0.8) with dissolve
                            ten"H-hold on a moment! W-where do you plan to..."
                            show screen parallax1280("tenten_thighsex_2_fast",1.25, 0.8) with dissolve
                            "You increase the pace, rubbing yourself raw against her soft inner thighs."
                            bo"W-where else, Tenten..."
                            ten"You are c-close to somewhere you shouldn't be. C-careful!" with vpunch
                            bo"I... I a-am!" with flash
                            $ renpy.sound.play("/audio/soun_fx/cum5.opus", channel="sfx3", loop=False, relative_volume = 0.3)
                            show screen parallax1280("tenten_ts_cum1",1.25, 0.8) with flash
                            $ renpy.sound.stop(channel="sfx1") # Stop thighjob loop
                            bo"I am c-cumming!"
                            ten"!" with vpunch
                            $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx3", loop=False, relative_volume = 0.3) 
                            show screen parallax1280("tenten_ts_cum2",1.25, 0.8) with longerflash
                            call decreaselust(100) from _call_decreaselust_104
                            "You shudder, releasing onto her legs and into the water."
                            call hidescrollingimage2 from _call_hidescrollingimage2_30
                            scene black with dissolve
                            $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                            show screen parallax1280("both_in_lake_submerged2",1.25) with dissolve
                            call showscrollingimage from _call_showscrollingimage_112
                            "Tenten stares down at the mess with wide, unblinking eyes, trembling slightly."
                            ten "You... you finished..."
                            bo "I... yeah. Thank you, Tenten. The... the pain is easing now."
                            ten "..." 
                            $ tenten_helped_release = True
                            call hidescrollingimage2 from _call_hidescrollingimage2_31
                            scene black with dissolve
                            jump tenten_lake_date_ending_kind

                        "Pull back and ask for a handjob":
                            $ renpy.sound.stop(channel="sfx1") 
                            call hidescrollingimage2 from _call_hidescrollingimage2_32
                            scene black with dissolve
                            $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                            "You stop moving, pulling back slightly and hiding back into the water out of embarrassment, still not quite believing what's happening."
                            $ renpy.sound.play("/audio/soun_fx/water_move_2.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                            show screen parallax1280("both_in_lake_slightly_submerged",1.25) with dissolve
                            call showscrollingimage from _call_showscrollingimage_113
                            bo "Tenten... This is... maybe making it worse... The friction..."
                            bo "I think... what Tsunade said... about direct... 'manual stimulation'..."
                            ten "You mean...?"
                            "She looks hesitant but relieved it's not some of the worse ideas she had in mind."
                            bo "Could you... just... use your hand? Like we talked about?"
                            jump tenten_lake_date_handjob_scene

                        "Stop and apologize":
                            call hidescrollingimage2 from _call_hidescrollingimage2_33
                            $ renpy.sound.stop(channel="sfx1") 
                            scene black with dissolve
                            "You suddenly stop, pulling away."
                            $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                            show screen parallax1280("both_in_lake_slightly_submerged",1.25) with dissolve
                            call showscrollingimage from _call_showscrollingimage_114
                            bo "I... I'm sorry, Tenten. This isn't right. I shouldn't have..."
                            "She looks surprised by your apology, her tension easing slightly."
                            ten "[bo_name]... It's okay. You said it was the curse..."
                            bo "Still... I took advantage. Let's just... forget it."
                            bot "Managed to pull back before things got worse. Good."
                            call hidescrollingimage2 from _call_hidescrollingimage2_34
                            scene black with dissolve
                            jump tenten_lake_date_ending_kind

                "Ask for more":
                    "You hold her close for another moment, then release your grip."
                    $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                    show screen parallax1280("both_in_lake_slightly_submerged",1.25) with dissolve
                    call showscrollingimage from _call_showscrollingimage_115
                    bo "Tenten.. I think... just holding you isn't quite enough... The pain..."
                    bo "It feels like... I need that 'release' Tsunade mentioned."
                    ten "Release...? You mean..."
                    "She looks nervous, understanding dawning."
                    bo "Yeah... If you could... just... with your hand? Please?"
                    ten "...Okay, [bo_name]. If it's really for the pain... I'll help."
                    jump tenten_lake_date_handjob_scene

        "{color=[hatredcolor]}Finger her ass{/color}":
            call changeHatred(1) from _call_changeHatred_154
            bo "Tenten... Bent over a bit more... just for a second."
            ten "Wh-what? Why?"
            call hidescrollingimage2 from _call_hidescrollingimage2_35
            scene black with dissolve
            "Before she can fully react, you move your hand right between her asscheeks, your fingers probing gently at first."
            show screen parallax1280("finger",1.25,1.0) with flash
            $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
            call showscrollingimage from _call_showscrollingimage_116
            ten "Eek! [bo_name]! Stop it! What are you doing?!" with vpunch
            call hidescrollingimage2 from _call_hidescrollingimage2_36
            scene black with dissolve
            $ renpy.sound.play("/audio/soun_fx/water_move_2.opus", channel="sfx1", loop=False, relative_volume = 0.5)
            "She pushes you away forcefully, eyes wide with betrayal and disgust."
            ten "That's NOT okay! Get away from me!"
            show screen parallax1280("pov2_angry",1.25,0.3) with dissolve
            ten "I offered to help you because you said you were in pain, not so you could just... do that to me!"
            ten "I thought maybe you were different, but you're just like everyone else!"
            call hidescrollingimage2 from _call_hidescrollingimage2_37
            "Tenten stepped out of the water to dry herself..."
            show tenten_lake_back_undress with dissolve:
                zoom 1.25 xalign 0.5 yalign 0.0
            show tenten_lake_back_undress:
                easein 6 yalign 1.0
            bot"Fuck! Can't believe I blew my chances with her..."
            scene black with dissolve                    
            call hidescrollingimage2 from _call_hidescrollingimage2_38
            jump tenten_lake_date_fail_permanent_label

        "{color=[dominancecolor]}Touch her pussy{/color}":
            $ tenten_pussy_fail = True
            bo "Just... let me..."
            call hidescrollingimage2 from _call_hidescrollingimage2_39
            scene black with dissolve
            "You shift your grip slightly, letting your fingers slip inside her pussy."
            $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
            show screen parallax1280("finger_front",1.25) with flash
            call showscrollingimage from _call_showscrollingimage_117
            call changeDominance(1) from _call_changeDominance_103
            ten "N-no! [bo_name], don't!" with vpunch
            call hidescrollingimage2 from _call_hidescrollingimage2_40
            scene black with dissolve
            $ renpy.sound.play("/audio/soun_fx/water_move_2.opus", channel="sfx1", loop=False, relative_volume = 0.5)
            "She shoves your hand away, looking horrified."
            show screen parallax1280("pov2_angry",1.25,0.3) with dissolve
            ten "I said I'd help, but... not like that! What's wrong with you?!"
            bo"S-sorry! I thought we had something going here..."
            ten"Ugh! Men..."
            scene black
            call hidescrollingimage2 from _call_hidescrollingimage2_41
            ten"Boys, rather!" with vpunch
            ten"Immature little boys..."
            "Tenten stepped out of the water to dry herself..."
            show tenten_lake_back_undress with dissolve:
                zoom 1.25 xalign 0.5 yalign 0.0
            show tenten_lake_back_undress:
                easein 6 yalign 1.0
            bot"Fuck! Can't believe I blew my chances with her..."
            scene black with dissolve                    
            call hidescrollingimage2 from _call_hidescrollingimage2_42
            jump tenten_lake_date_fail_retry

        "Ask for more":
            "You hesitantly release your grip."
            $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
            show screen parallax1280("both_in_lake_slightly_submerged",1.25) with dissolve
            call showscrollingimage from _call_showscrollingimage_118
            bo "Tenten.. I think... just that isn't quite enough... The pain..."
            bo "It feels like... I need that 'release' Tsunade mentioned."
            ten "Release...? You mean..."
            bo "Yeah... If you could... just... with your hand? Please?"
            jump tenten_lake_date_handjob_scene

label tenten_lake_date_titsuck:
    $ tenten_date_titsuck = True
    bo "Maybe... Could I... suck on your... ?"
    ten "Suck... suck my 'what'?! [bo_name], are you serious? How is 'that' supposed to help with your... 'condition'?"
    bo "I... I don't know! It's... maybe the closeness? The... comfort? Tsunade said... unconventional things might help manage the... urges... the pain..."
    ten "Unconventional is one thing, [bo_name], but this is..." 

    menu tenten_lake_date_titsuck_choice:
        bot "Okay, maybe that was a weird ask. How do I play this?"

        "{color=[hatredcolor]}Don't question it, just let me.{/color}":
            call hidescrollingimage2 from _call_hidescrollingimage2_43
            bo "Less talking, more helping."
            scene black with dissolve
            "Ignoring her hesitation, you reach out quickly, cupping her breast through her wet top."
            $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
            show screen parallax1280("titgrab",1.25, 1.0) with flash
            call showscrollingimage from _call_showscrollingimage_119
            call changeHatred(1) from _call_changeHatred_155
            bo"That's a nice pair you have on you, Tenten!"
            ten "H-hey! W-what are you doing all of a sudden!" with vpunch
            call hidescrollingimage2 from _call_hidescrollingimage2_44
            scene black with dissolve
            $ renpy.sound.play("/audio/soun_fx/water_move_2.opus", channel="sfx1", loop=False, relative_volume = 0.5)
            "She slaps your hand away hard and scrambles back, looking furious and betrayed."
            $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
            scene black with dissolve
            show screen parallax1280("pov2_angry",1.25,0.3) with dissolve
            ten "I offered to help you because you said you were in pain, not so you could just... grope me!"
            ten "I thought maybe you were different, but you're just like everyone else!"
            call hidescrollingimage2 from _call_hidescrollingimage2_45

            "Tenten stepped out of the water to dry herself..."
            show tenten_lake_back_undress with dissolve:
                zoom 1.25 xalign 0.5 yalign 0.0
            show tenten_lake_back_undress:
                easein 6 yalign 1.0
            ten "I try to be understanding because you're supposedly in pain, and you pull this?! You're disgusting!"
            bot"Fuck! Can't believe I blew my chances with her..."
            scene black with dissolve
            jump tenten_lake_date_fail_permanent_label

        "Please, Tenten? Just for a little bit?":
            bo "Please? I know it sounds crazy... but the pain is really bad right now. Maybe... maybe the warmth... or... something... might just... calm it down? If it doesn't work, I'll stop immediately. Promise."
            ten "..."
            ten "This is... really weird, [bo_name]. Are you *sure* this isn't just... you being...?" 
            bo "No! It's the curse, I swear! Please?"
            ten "*Sighs deeply*... Fine. Fine! But just for a *minute*. And if this is some kind of trick..."

            menu tenten_lake_date_titsuck_agreed:
                "Suck on her breasts.":
                    call hidescrollingimage2 from _call_hidescrollingimage2_46
                    scene black with dissolve
                    "She looks away, face burning red, standing rigidly..."
                    show screen parallax1280("titgrab",1.25,1.0) with dissolve        
                    "You lean in, your heart pounding..."
                    $ renpy.sound.play("/audio/soun_fx/water_move_2.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                    ten"Gently... O-okay?"
                    bo"Y-yeah..."
                    show screen parallax1280("use1",1.25) with dissolve
                    call showscrollingimage from _call_showscrollingimage_120
                    $ renpy.sound.play("/audio/soun_fx/sucking.mp3", channel="sfx3", loop=True, relative_volume = 0.9)
                    ten "*Gasp!* Ah..." 
                    "She trembles slightly..."
                    show screen parallax1280("tenten_breastsuck_anim1",1.25) with dissolve
                    "You continue to suckle gently, the warmth and softness surprisingly calming for both of you..."
                    bot "She... she's letting me suck on her tiddies!"
                    bot"It's somewhat... comforting..."

                    menu tenten_lake_date_titsuck_ongoing:
                        "Keep going gently":
                            "You continue your ministrations, occasionally swirling your tongue."
                            ten "*Ngh...*"
                            jump tenten_lake_date_titsuck_relief_check

                        "Suck harder":
                            show screen parallax1280("tenten_breastsuck_anim1_1",1.25) with dissolve
                            $ renpy.sound.play("/audio/soun_fx/sucking.mp3", channel="sfx1", loop=True, relative_volume = 1.0)
                            ten "Ngh! [bo_name]... We s-said gently! R-remember?" with vpunch
                            "Her breath hitches as she instinctively grabs your shoulder."
                            jump tenten_lake_date_titsuck_relief_check

                        "Stop now":
                            $ renpy.sound.stop(channel="sfx3")
                            call hidescrollingimage2 from _call_hidescrollingimage2_47
                            scene black with dissolve
                            $ renpy.sound.play("/audio/soun_fx/water_move_2.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                            "You pull back gently."
                            bo "Okay... Okay, that's... thank you, Tenten."
                            $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                            show screen parallax1280("both_in_lake_slightly_submerged",1.25) with dissolve
                            call showscrollingimage from _call_showscrollingimage_121
                            "She avoids your gaze, still breathing a little heavily, looking incredibly flustered."
                            ten "Did... did it help? At all?"
                            bo "Yeah... a little. Thanks."
                            bot "Better stop before I push it too far."
                            call hidescrollingimage2 from _call_hidescrollingimage2_48
                            scene black with dissolve
                            jump tenten_lake_date_ending_kind

        "Back down and apologize.":
            bo "You know what? You're right. That was... a really weird and stupid thing to ask. I'm sorry, Tenten. Pain's making me say dumb things."
            "Tenten seems relieved, though still a bit wary."
            ten "B-but.. The pain, are you just gonna suffer through it?"
            bo "It's still.. hurting really bad but, it's not the f-first time I've had to endure it."
            bo "I can't be using it as an excuse to use you."
            ten "It... It's okay. Just... maybe stick to more normal requests if you need help?"
            bo "I w-will. Thank you for being so understanding, Tenten"
            bot "Managed to salvage that. Asking to suck her tits... what was I thinking?"
            call hidescrollingimage2 from _call_hidescrollingimage2_49
            scene black with dissolve
            "You do your best to cope with the pain without making things more awkward."
            "Time passes, the layer of awkwardness slowly going away."
            ten "Shall we get going?"
            $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
            bo "Last one out is cleaning shuriken for another week!"
            ten "H-hey you started moving before you said that!"
            $ renpy.sound.play("/audio/soun_fx/water_move_2.opus", channel="sfx1", loop=False, relative_volume = 0.5)
            jump tenten_lake_date_ending_kind


label tenten_lake_date_titsuck_relief_check:
    bo "Ngh... Tenten... I think... it's actually helping..." 
    call hidescrollingimage2 from _call_hidescrollingimage2_50
    scene black with dissolve
    $ renpy.sound.stop(channel="sfx1") 
    $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx3", loop=False, relative_volume = 0.8)
    call decreaselust(100) from _call_decreaselust_105 
    $ tenten_helped_release = True 

    "You pull away, breathing heavily but looking more relaxed."
    $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
    show screen parallax1280("both_in_lake_slightly_submerged",1.25) with dissolve
    call showscrollingimage from _call_showscrollingimage_122
    bo "Wow... I... I think the pain's gone. Thank you, Tenten. Really."
    "Tenten stares at you, her expression a mixture of shock, embarrassment, and confusion."
    ten "It... it actually worked?"
    bo "Yeah... Yeah, it did."
    ten "That's... good. I guess."
    ten "Something like breastfeeding an infant... Eh-eh! *Nervous chuckle*"
    "She's still processing the strangeness of it all."
    ten "Just... let's not... talk about this method. Ever."
    bo "Agreed. Sealed lips..."
    call hidescrollingimage2 from _call_hidescrollingimage2_51
    scene black with dissolve

    jump tenten_lake_date_ending_kind

label tenten_lake_date_ending_kind:
    $ tenten_date_success = True
    $ tenten_date_counter += 1
    $ tenten_last_date_day = day_number
    $ tenten_date_decline_counter = 0
    $ tenten_days_since_agreed = 0 # Reset waiting counter
    $ tenten_date_agreed = False # Date is done, agreement fulfilled
    $ tenten_lake_date_fail_retry = 0 # Reset fail retry to 0 in case there were previous failed tries that now led to success
    $ tenten_date_shop_dialogueflavor_mentioned = False

    scene black with dissolve
    pause(1)
    $ playmusic("audio/ost/lakedate.opus",0.3)

    if tenten_helped_release:
        "You both take some time to dress back up, facing away from each other."
        "You catch yourselves occasionally looking at one another, sharing awkward chuckles..."
        scene bg_night_forest3 with dissolve
        "The walk back starts in a thick, charged silence. Tenten keeps glancing at you, then quickly away, her cheeks still pink." #1
        show ten sad2 at right with dissolve
        ten "That was-"
        show boruto embarassed at left with dissolve
        bo "Amazing! I m-mean..." with vpunch
        show boruto normal with dissolve
        bo "It was very kind... and caring of you."
        show boruto worried with dissolve
        pause(0.2)
        bo "Thanks again, Tenten. For... everything. You really helped."
        ten "Just... take care of yourself, okay? With that condition..."
        bo "Believe me, I am trying my best."
        ten "Right... Well..."
        ten "We should probably get going by now? It's getting late."
        bo "Oh! Y-yeah, right. Good idea."

        hide ten
        hide boruto
        scene black
        with dissolve
        bot "That was... unexpected. But she helped. Maybe she cares more than she lets on?"
    else:        
        scene bg_night_forest3 with dissolve
        "You start making your way back."
        show boruto laughing at left:
            xalign 0.3
        show ten sad2 at right:
            xalign 0.7
        with dissolve
        ten "I... I actually had a really nice time, [bo_name]. Despite the... awkward bits."
        bo "Me too actually!"
        bo "We should do this again sometime."
        ten "I'd... I'd like that."
        bo "Great! Then it's settled."
        ten "It is getting a bit chilly out here though, maybe we should head back?"
        bo "Yeah, probably for the best. Don't want you catching a cold."
        ten "*Giggles softly* Right."
        "You both retrieve your clothes from the shore."
        show boruto:
            easein 2 xalign -3
        show ten:
            easein 2 xalign -3
        with moveoutleft
        hide ten
        hide boruto
        scene black
        with dissolve
        bot "That went... surprisingly well. Maybe there's something here after all."

    "You walk back towards the village together, a comfortable silence settling between you."
    scene bg ramenshop night with dissolve
    show ten sad2 at center with dissolve
    ten"Thank you for accompanying me, [bo_name]..."
    ten"I'll see you again sometime soon, right?"
    hide ten with dissolve
    bo"I'll see you around."
    scene black with dissolve
    jump tenten_date_end_cleanup

label tenten_date_end_cleanup:
    $ tenten_date_agreed = False

    $ renpy.sound.stop(channel="music") 
    $ renpy.end_replay() 
    stop sound channel "sfx1"
    jump action_taken