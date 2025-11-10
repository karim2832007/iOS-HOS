# game/zgame/updates/v020/massage_minigame.rpy

default consecutive_mild_choices = 0
default massage_stage = 1

label massage_minigame_start:
    # This is the entry point from madame_continuation.rpy

    # Initial setup
    $ satisfactionpercentage = 15
    $ consecutive_mild_choices = 0
    $ massage_stage = 1

    # Show the satisfaction bar throughout the minigame

    mada "Ha! I will make no guarantees regarding that..."
    mada "Come [bo_name], let us begin! Show me what you can do."
    scene black with dissolve
    "Madame shifts to lie on her stomach on a nearby massage table, her clothes still on. She seems tense, her shoulders high."

    # Jump to the first stage
    jump massage_stage_1_menu

#-------------------------------------------------------------------------------
# Stage 1: On her stomach, clothed, tense
#-------------------------------------------------------------------------------

label massage_stage_1_menu:
    show screen massage_stage_display
    show screen massagebar
    call check_satisfaction from _call_check_satisfaction
    show screen parallax1280("rang_massage_start 2_1tense", menuenabled=True) with dissolve #Add menuenabled=True to prevent clicks from selecting random menu options/breaking game (Only when menu choices are present)

    menu:
        "Massage her shoulders" if satisfactionpercentage<100:
            $ consecutive_mild_choices += 1
            $ renpy.sound.play("audio/soun_fx/groperepeat1.opus", channel="sfx3", loop=False, relative_volume = 1)
            show screen parallax1280("v20_madame_stage1_shoulders_massage")
            with dissolve
            if massageknowledge >= 1:
                bot"She's incredibly tense. Best to start with some gentle Effleurage to warm the muscles."
            bo "Let's start by loosening these up..."
            "You place your hands on her shoulders, applying gentle but firm pressure. You can feel the knots of tension under her skin."
            mada "Mmm... A competent start. But competence is the bare minimum I expect."

            call increasesatisfaction(15) from _call_increasesatisfaction
            call post_action_pause("massage_stage_1_menu") from _call_post_action_pause

        "Massage her waist" if satisfactionpercentage<100:
            $ consecutive_mild_choices += 1
            $ renpy.sound.play("audio/soun_fx/groperepeat1.opus", channel="sfx3", loop=False, relative_volume = 1)
            show screen parallax1280("v20_madame_stage1_waist_massage")
            with dissolve

            "You move your hands down to her waist, rubbing in slow, circular motions."
            mada "Keep your hands right there, boy. Your boundaries are being tested as much as your skill."
            "She's watching you, but doesn't stop you."

            call increasesatisfaction(15) from _call_increasesatisfaction_1
            call post_action_pause("massage_stage_1_menu") from _call_post_action_pause_1

        "{color=[obediencecolor]}Massage her thighs{/color}" if (consecutive_mild_choices >= 2 or massageknowledge >= 1) and satisfactionpercentage<100:
            $ renpy.sound.play("audio/soun_fx/groperepeat1.opus", channel="sfx3", loop=False, relative_volume = 1)
            show screen parallax1280("v20_madame_stage1_thighs_massage") with dissolve
            if massageknowledge == 1:
                bo"The tension often runs down into the legs. It's important to address the entire muscle group."
                mada "Oh? You understand the body's connections, it seems. Or you're simply getting bold. Either way... I'll allow it."
            else:
                "Feeling brave, you move your hands down to her firm thighs."
                mada "I can sense your hesitation, but this one time, I'll allow it."
            "She shifts slightly, giving you better access. A small victory."
            call increasesatisfaction(30) from _call_increasesatisfaction_2
            call post_action_pause("massage_stage_1_menu") from _call_post_action_pause_2

        "Massage her thighs" if not (consecutive_mild_choices >= 2 or massageknowledge >= 1) and satisfactionpercentage<100:
            $ renpy.sound.play("audio/soun_fx/groperepeat1.opus", channel="sfx3", loop=False, relative_volume = 1)
            show screen parallax1280("v20_madame_stage1_thighs_massage") with dissolve
            "You move your hands down to her thighs, perhaps a bit too soon."
            mada "Hey! A little eager, aren't we? Her majesty's back is your canvas for now. Do not stray from it."
            "She tenses up again, clearly displeased."
            call decreasesatisfaction(10) from _call_decreasesatisfaction
            call post_action_pause("massage_stage_1_menu") from _call_post_action_pause_3

        "{color=[hatredcolor]}Spank her ass!{/color}" if satisfactionpercentage<70:
            $ consecutive_mild_choices = 0
            scene black
            hide screen parallax1280
            with dissolve
            "You decide to succumb to your urges and just go for it."
            $ renpy.sound.play("audio/soun_fx/spank5.opus", channel="sfx3", loop=False, relative_volume = 1)
            show screen parallax1280("rang_massage_stage1_spank") with flash
            mada "What do you think you're doing?! Do you take me for a common harlot?!"
            call decreasesatisfaction(100) from _call_decreasesatisfaction_1
            hide screen parallax1280
            scene black
            with dissolve
            "She jolts up, her eyes flashing with fury. The test is over."
            mada "You lack subtlety and grace. You've crossed a line. Get out."
            jump massage_minigame_fail

        "{color=[obediencecolor]}Massage her ass{/color}" if satisfactionpercentage>70 and satisfactionpercentage<100:
            $ renpy.sound.play("audio/soun_fx/grabsound.opus", channel="sfx3", loop=False, relative_volume = 1.5)
            show screen parallax1280("v20_madame_stage1_ass_massage") with dissolve
            "You go for the ultimate prize, placing your hands directly on her clothed buttocks."
            mada "A bit... bold, don't you think?"
            hide screen parallax1280
            with dissolve
            "She complains, but only timidly as she lets out a relaxed moan..."
            call increasesatisfaction(30) from _call_increasesatisfaction_3
            call post_action_pause("massage_stage_1_menu") from _call_post_action_pause_4

        "Massage her feet" if satisfactionpercentage<100:
            $ consecutive_mild_choices = 0
            $ renpy.sound.play("/audio/soun_fx/groperepeat1.opus", channel="sfx1", loop=False, relative_volume = 1.1)
            show screen parallax1280("v20_madame_stage1_feet_massage") with dissolve
            "You move to the end of the table and start working on her feet."
            mada "My feet? They are perfectly fine. What an odd thing to do."
            "Her tone is icy. You've clearly made a tactical error."
            mada "Are you one of those peculiar men with a foot fixation? How utterly disappointing. We're done here."
            hide screen parallax1280
            scene black
            with dissolve
            jump massage_minigame_fail

        "Ask her to relax" if satisfactionpercentage>=100:
            $ consecutive_mild_choices = 0
            if satisfactionpercentage >= 100:
                mada "You've done well. I feel the tension melting away..."
                bo "Just relax. Let go completely."
                mada "Hmph. Very well. I suppose I can trust you that much."
                hide screen parallax1280
                hide screen massagebar
                scene black
                with dissolve
                "She takes a deep breath and her whole body seems to soften."
                jump massage_stage_2_start
            else:
                bo "You seem tense. Can you try to relax for me?"
                mada "I'm trying. Perhaps if your massage was more convincing, I would be."
                "Her words are sharp, a clear sign you haven't earned this yet."
                call decreasesatisfaction(20) from _call_decreasesatisfaction_2
                call post_action_pause("massage_stage_1_menu") from _call_post_action_pause_5

#-------------------------------------------------------------------------------
# Stage 2: On her stomach, clothed, relaxed
#-------------------------------------------------------------------------------

label massage_stage_2_start:
    $ satisfactionpercentage = 15
    $ consecutive_mild_choices = 0
    $ massage_stage = 2

    "With the initial tension gone, Madame's body is more receptive. She lies placidly on the table, her breathing even. The real test begins now."

    jump massage_stage_2_menu

label massage_stage_2_menu:
    show screen massage_stage_display
    show screen massagebar
    call check_satisfaction from _call_check_satisfaction_1

    show screen parallax1280("rang_massage_start 2", menuenabled=True) with dissolve

    menu massage_start_2_menu:
        "Massage her shoulders" if satisfactionpercentage<100:
            $ consecutive_mild_choices += 1
            $ renpy.sound.play("audio/soun_fx/groperepeat1.opus", channel="sfx3", loop=False, relative_volume = 1)
            show screen parallax1280("v20_madame_stage2_shoulders_massage") with dissolve
            "You return to her shoulders, finding them much more pliable now."
            mada "*sigh*... That's much better."
            "She murmurs, her voice thick with relaxation."
            call increasesatisfaction(15) from _call_increasesatisfaction_4
            call post_action_pause("massage_stage_2_menu") from _call_post_action_pause_6

        "Massage her waist" if satisfactionpercentage<100:
            $ consecutive_mild_choices += 1
            $ renpy.sound.play("audio/soun_fx/groperepeat1.opus", channel="sfx3", loop=False, relative_volume = 1)
            show screen parallax1280("v20_madame_stage2_waist_massage") with dissolve
            "Your hands glide over her waist, the fabric of her clothes the only barrier."
            mada "Mmm, you have a good rhythm."
            call increasesatisfaction(15) from _call_increasesatisfaction_5
            call post_action_pause("massage_stage_2_menu") from _call_post_action_pause_7

        "{color=[obediencecolor]}Massage her thighs{/color}" if (consecutive_mild_choices >= 2 or massageknowledge >= 1) and satisfactionpercentage<100:
            $ renpy.sound.play("audio/soun_fx/groperepeat1.opus", channel="sfx3", loop=False, relative_volume = 1)
            show screen parallax1280("v20_madame_stage2_thighs_massage") with dissolve
            "You massage her thighs again. This time, she doesn't protest."
            mada "Yes... right there. You're learning."
            "Her voice is a low purr."
            call increasesatisfaction(30) from _call_increasesatisfaction_6
            call post_action_pause("massage_stage_2_menu") from _call_post_action_pause_8

        "Massage her thighs" if not (consecutive_mild_choices >= 2 or massageknowledge >= 1) and satisfactionpercentage<100:
            $ renpy.sound.play("audio/soun_fx/groperepeat1.opus", channel="sfx3", loop=False, relative_volume = 1)
            show screen parallax1280("v20_madame_stage2_thighs_massage") with dissolve
            "You try for her thighs, but she subtly shifts away."
            mada "Patience. Earn it."
            "A gentle rebuke, but a rebuke nonetheless."
            call decreasesatisfaction(10) from _call_decreasesatisfaction_3
            call post_action_pause("massage_stage_2_menu") from _call_post_action_pause_9

        "{color=[dominancecolor]}Use a special technique on her toes{/color}" if satisfactionpercentage<100 and massageknowledge>=1:
            $ consecutive_mild_choices = 0
            $ renpy.sound.play("audio/soun_fx/groperepeat1.opus", channel="sfx3", loop=False, relative_volume = 1)
            call checkDominance(20, "massage_start_2_menu") from _call_checkDominance_52
            show screen parallax1280("v20_madame_stage2_feet_massage") with dissolve
            bot"The surface is relaxed. Time for some Petrissage to work the deeper knots."
            bo "Now that you're relaxed, I can address the deeper tension."
            bo "A full body massage includes the feet, Madame. One of our most stressed extremities."
            "You say it with a confidence you hope you possess. You take her feet in your hands."
            mada "Oh? Is that so? ...Very well. Don't disappoint me."
            "She seems intrigued by your confidence."
            call increasesatisfaction(40) from _call_increasesatisfaction_7

            call post_action_pause("massage_stage_2_menu") from _call_post_action_pause_10

        "Ask her to turn around" if satisfactionpercentage>=100:
            $ consecutive_mild_choices = 0
            if satisfactionpercentage >= 100:
                bo "To properly continue, I need you to turn over for me."
                mada "...Turn around?"
                "She considers it for a moment, then lets out a soft laugh."
                mada "Alright, 'master masseur'. Let's see what you have planned."
                jump massage_stage_3_start
            else:
                bo "I need you to turn around now."
                mada "I'm quite comfortable. You haven't convinced me to move just yet."
                call decreasesatisfaction(20) from _call_decreasesatisfaction_4
                call post_action_pause("massage_stage_2_menu") from _call_post_action_pause_11

#-------------------------------------------------------------------------------
# Stage 3: On her back, clothed
#-------------------------------------------------------------------------------

label massage_stage_3_start:
    $ satisfactionpercentage = 15
    $ consecutive_mild_choices = 0
    $ massage_stage = 3

    "She gracefully flips onto her back. As she settles, her eyes lock with yours. The dynamic has shifted, becoming far more intimate."
    jump massage_stage_3_menu

label massage_stage_3_menu:
    show screen massage_stage_display
    show screen massagebar
    call check_satisfaction from _call_check_satisfaction_2

    show screen parallax1280("rang_massage_start 1", menuenabled=True) with dissolve

    menu:
        "Massage her shoulders" if satisfactionpercentage<100:
            $ consecutive_mild_choices += 1
            $ renpy.sound.play("audio/soun_fx/groperepeat1.opus", channel="sfx3", loop=False, relative_volume = 1)
            show screen parallax1280("v20_madame_stage3_shoulders_massage") with dissolve
            "You gently massage her shoulders and collarbone area."
            mada "Mmm... You certainly know the way to a woman's muscles."
            "Her eyes are half-lidded with pleasure."
            call increasesatisfaction(15) from _call_increasesatisfaction_8
            call post_action_pause("massage_stage_3_menu") from _call_post_action_pause_12

        "Massage her waist" if satisfactionpercentage<100:
            $ consecutive_mild_choices += 1
            $ renpy.sound.play("audio/soun_fx/groperepeat1.opus", channel="sfx3", loop=False, relative_volume = 1)
            show screen parallax1280("v20_madame_stage3_waist_massage") with dissolve
            "Your hands rest on her waist, thumbs drawing circles on her stomach."
            mada "Careful... your hands are straying."
            "She says it, but makes no move to stop you."
            call increasesatisfaction(15) from _call_increasesatisfaction_9
            call post_action_pause("massage_stage_3_menu") from _call_post_action_pause_13

        "{color=[obediencecolor]}Massage her thighs{/color}" if (consecutive_mild_choices >= 2 or massageknowledge == 1) and satisfactionpercentage<100:
            $ renpy.sound.play("audio/soun_fx/groperepeat1.opus", channel="sfx3", loop=False, relative_volume = 1)
            show screen parallax1280("v20_madame_stage3_thighs_massage") with dissolve
            if massageknowledge == 1:
                bo "Relaxing the adductor muscles is key to relieving hip tension."
            mada "*gasp*... So bold. Just like your [hin_rel_mother] when she was pushed. I like it."
            "Her breath hitches, a clear sign of approval."
            call increasesatisfaction(30) from _call_increasesatisfaction_10
            call post_action_pause("massage_stage_3_menu") from _call_post_action_pause_14

        "Massage her thighs" if not (consecutive_mild_choices >= 2 or massageknowledge == 1) and satisfactionpercentage<100:
            $ renpy.sound.play("audio/soun_fx/groperepeat1.opus", channel="sfx3", loop=False, relative_volume = 1)
            show screen parallax1280("v20_madame_stage3_thighs_massage") with dissolve
            "You reach for her thighs prematurely."
            mada "Not so fast. You're losing your finesse. You may have her spirit, but you lack her patience."
            "She pushes your hands away gently."
            call decreasesatisfaction(10) from _call_decreasesatisfaction_5
            call post_action_pause("massage_stage_3_menu") from _call_post_action_pause_15

        "{color=[obediencecolor]}Massage her feet{/color}" if (consecutive_mild_choices >= 2 or massageknowledge >= 1) and satisfactionpercentage<100:
            $ renpy.sound.play("audio/soun_fx/groperepeat1.opus", channel="sfx3", loop=False, relative_volume = 1)
            hide screen parallax1280
            show screen parallax1280("v20_madame_stage3_feet_massage",initial_ypos=1.0)
            with dissolve
            "You take one of her feet, rubbing the sole with your thumb."
            mada "My feet again... you have a fixation, don't you? It... does feel good, I admit."
            call increasesatisfaction(30) from _call_increasesatisfaction_11
            call post_action_pause("massage_stage_3_menu") from _call_post_action_pause_16

        "Massage her feet" if not (consecutive_mild_choices >= 2 or massageknowledge >= 1) and satisfactionpercentage<100:
            $ renpy.sound.play("audio/soun_fx/groperepeat1.opus", channel="sfx3", loop=False, relative_volume = 1)
            show screen parallax1280("v20_madame_stage3_feet_massage") with dissolve
            "You reach for her feet."
            mada "No, not right now. Focus."
            call decreasesatisfaction(10) from _call_decreasesatisfaction_6
            call post_action_pause("massage_stage_3_menu") from _call_post_action_pause_17

        "{color=[hatredcolor]}Grab her by the pussy{/color}" if satisfactionpercentage<100:
            $ consecutive_mild_choices = 0
            $ renpy.sound.play("audio/soun_fx/groperepeat1.opus", channel="sfx3", loop=False, relative_volume = 1)
            show screen parallax1280("v20_madame_stage3_pussy_massage") with dissolve
            $ renpy.sound.play("audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx2", loop=False, relative_volume = 1)
            "Thinking you have her complete trust, your hand strays between her legs, over her clothes."
            mada "THAT IS ENOUGH!"
            hide screen parallax1280
            scene black
            with dissolve
            "She shoves you away with surprising strength."
            mada "You've ruined everything! Get out of my sight!"
            jump massage_minigame_fail

        "Ask her to take off her clothes" if satisfactionpercentage>=100:
            $ consecutive_mild_choices = 0
            if massageknowledge >= 1:
                # Player has knowledge, proceed with satisfaction check
                if satisfactionpercentage >= 100:
                    bo "These clothes are getting in the way."
                    mada "Are they now? Hmph. You've certainly earned a better view."
                    "She smirks, sitting up."
                    mada "Fine. But you had better make this worth my while."
                    "She removes her outer garments and lies back down on her stomach."
                    jump massage_stage_4_start
                else:
                    bo "Take off your clothes for me."
                    mada "You wish. A privilege like that must be earned, and you're not there yet."
                    call decreasesatisfaction(20) from _call_decreasesatisfaction_7
                    call post_action_pause("massage_stage_3_menu") from _call_post_action_pause_18
            else:
                mada "A bit too eager, aren't we little lamb?"
                mada "You did relatively well, but..."
                jump massage_knowledge_too_low

#-------------------------------------------------------------------------------
# Stage 4: On her stomach, unclothed
#-------------------------------------------------------------------------------

label massage_stage_4_start:
    $ satisfactionpercentage = 15
    $ consecutive_mild_choices = 0
    $ massage_stage = 4

    "The sight of her bare back is breathtaking. The air is thick with sensual energy. This is no longer just a massage."

    jump massage_stage_4_menu

label massage_stage_4_menu:
    show screen massage_stage_display
    show screen massagebar
    call check_satisfaction from _call_check_satisfaction_3

    show screen parallax1280("rang_massage_start 4", menuenabled=True) with dissolve

    menu:
        "Massage her shoulders" if satisfactionpercentage<100:
            $ consecutive_mild_choices += 1
            $ renpy.sound.play("audio/soun_fx/groperepeat1.opus", channel="sfx3", loop=False, relative_volume = 1)
            show screen parallax1280("v20_madame_stage4_shoulders_massage") with dissolve
            "Your hands on her bare skin feel electric. You work her shoulders, feeling her melt under your touch."
            mada "*moan*... Yes... right there..."
            call increasesatisfaction(15) from _call_increasesatisfaction_12
            call post_action_pause("massage_stage_4_menu") from _call_post_action_pause_19

        "Massage her waist" if satisfactionpercentage<100:
            $ consecutive_mild_choices += 1
            $ renpy.sound.play("audio/soun_fx/groperepeat1.opus", channel="sfx3", loop=False, relative_volume = 1)
            show screen parallax1280("v20_madame_stage4_waist_massage") with dissolve
            "You trace the elegant curve of her waist and back."
            mada "Much better without the fabric, isn't it?"
            "Her voice is a breathy whisper."
            call increasesatisfaction(15) from _call_increasesatisfaction_13
            call post_action_pause("massage_stage_4_menu") from _call_post_action_pause_20

        "{color=[obediencecolor]}Massage her thighs{/color}" if (consecutive_mild_choices >= 2 or massageknowledge >= 1) and satisfactionpercentage<100:
            $ renpy.sound.play("audio/soun_fx/groperepeat1.opus", channel="sfx3", loop=False, relative_volume = 1)
            show screen parallax1280("v20_madame_stage4_thighs_massage") with dissolve
            "You knead the soft flesh of her bare thighs."
            mada "Oooh, don't stop... that feels incredible."
            call increasesatisfaction(30) from _call_increasesatisfaction_14
            call post_action_pause("massage_stage_4_menu") from _call_post_action_pause_21
        
        "Massage her thighs" if not (consecutive_mild_choices >= 2 or massageknowledge >= 1) and satisfactionpercentage<100:
            $ renpy.sound.play("audio/soun_fx/groperepeat1.opus", channel="sfx3", loop=False, relative_volume = 1)
            show screen parallax1280("v20_madame_stage4_thighs_massage") with dissolve
            "You move to her thighs, but she tenses slightly."
            mada "Slowly. Savor the moment."
            call decreasesatisfaction(10) from _call_decreasesatisfaction_8
            call post_action_pause("massage_stage_4_menu") from _call_post_action_pause_22

        "{color=[obediencecolor]}Massage her ass{/color}" if (consecutive_mild_choices >= 2 or massageknowledge >= 1) and satisfactionpercentage<100 and massageknowledge >= 1:
            $ renpy.sound.play("audio/soun_fx/grabsound.opus", channel="sfx3", loop=False, relative_volume = 1.5)
            show screen parallax1280("v20_madame_stage4_ass_massage") with dissolve
            if massageknowledge == 1:
                bo"The gluteus maximus holds incredible tension. It needs to be worked directly."
                mada "So clinical... and yet so effective. Mmmhmm..."
            else:
                "Now, you cup the soft, full curve of her ass cheek. She moans deeply in response."
                mada "Mmmhmm... You're learning exactly what I want, little lamb."
            call increasesatisfaction(35) from _call_increasesatisfaction_15
            call post_action_pause("massage_stage_4_menu") from _call_post_action_pause_23

        "Massage her ass" if not (consecutive_mild_choices >= 2 or massageknowledge >= 1) and satisfactionpercentage<100 and massageknowledge >= 1:
            $ renpy.sound.play("audio/soun_fx/grabsound.opus", channel="sfx3", loop=False, relative_volume = 1.5)
            show screen parallax1280("v20_madame_stage4_ass_massage") with dissolve
            "You touch her ass, but she shifts away."
            mada "Not yet. You haven't earned that privilege."
            call decreasesatisfaction(10) from _call_decreasesatisfaction_9
            call post_action_pause("massage_stage_4_menu") from _call_post_action_pause_24

        "{color=[obediencecolor]}Massage her feet{/color}" if (consecutive_mild_choices >= 2 or massageknowledge >= 1) and satisfactionpercentage<100:
            $ renpy.sound.play("audio/soun_fx/groperepeat1.opus", channel="sfx3", loop=False, relative_volume = 1)
            show screen parallax1280("v20_madame_stage4_feet_massage") with dissolve
            "You return to her feet, now bare. The skin is soft and smooth under your hands."
            mada "Still so attentive to every detail... You are full of surprises, aren't you?"
            "Her voice is a low, appreciative hum."
            call increasesatisfaction(30) from _call_increasesatisfaction_16
            call post_action_pause("massage_stage_4_menu") from _call_post_action_pause_25

        "Massage her feet" if not (consecutive_mild_choices >= 2 or massageknowledge >= 1) and satisfactionpercentage<100:
            $ renpy.sound.play("audio/soun_fx/groperepeat1.opus", channel="sfx3", loop=False, relative_volume = 1)
            show screen parallax1280("v20_madame_stage4_feet_massage") with dissolve
            "You move to massage her feet."
            mada "My feet again? You were just working on more... central areas. Don't lose your focus now."
            "She sounds a little disappointed that you moved away from her back and waist."
            call decreasesatisfaction(10) from _call_decreasesatisfaction_10
            call post_action_pause("massage_stage_4_menu") from _call_post_action_pause_26

        "Ask her to turn around" if satisfactionpercentage>=100:
            $ consecutive_mild_choices = 0
            if satisfactionpercentage >= 100:
                bo "Let me see the front of you again."
                mada "...Again? Alright, fine."
                "She rolls over slowly, revealing her stunning front to you."
                mada "Let's see the grand finale."
                jump massage_stage_5_start
            else:
                bo "Turn around."
                mada "I'm not finished enjoying this side yet."
                call decreasesatisfaction(20) from _call_decreasesatisfaction_11
                call post_action_pause("massage_stage_4_menu") from _call_post_action_pause_27

#-------------------------------------------------------------------------------
# Stage 5: On her back, unclothed
#-------------------------------------------------------------------------------

label massage_stage_5_start:
    $ satisfactionpercentage = 15
    $ consecutive_mild_choices = 0
    $ massage_stage = 5

    "She lies before you, completely bare, her body flushed with pleasure. The air is thick with anticipation. Your final test."

    jump massage_stage_5_menu

label massage_stage_5_menu:
    show screen massage_stage_display
    show screen massagebar
    call check_satisfaction from _call_check_satisfaction_4

    show screen parallax1280("rang_massage_start 3", menuenabled=True) with dissolve

    menu:
        "Massage her shoulders" if satisfactionpercentage<100:
            $ consecutive_mild_choices += 1
            $ renpy.sound.play("audio/soun_fx/groperepeat1.opus", channel="sfx3", loop=False, relative_volume = 1)
            show screen parallax1280("v20_madame_stage5_shoulders_massage") with dissolve # Close up shot to imply shoulders
            "You focus on her shoulders and neck, kissing them lightly as you work."
            mada "*She sighs contentedly, melting completely.* Perfect..."
            call increasesatisfaction(15) from _call_increasesatisfaction_17
            call post_action_pause("massage_stage_5_menu") from _call_post_action_pause_28

        "Massage her waist" if satisfactionpercentage<100:
            $ consecutive_mild_choices += 1
            $ renpy.sound.play("audio/soun_fx/groperepeat1.opus", channel="sfx3", loop=False, relative_volume = 1)
            show screen parallax1280("v20_madame_stage5_waist_massage") with dissolve
            "Your hands roam her stomach, dangerously close to her breasts and groin."
            mada "You're teasing me, aren't you? Seeing how far you can go..."
            call increasesatisfaction(15) from _call_increasesatisfaction_18
            call post_action_pause("massage_stage_5_menu") from _call_post_action_pause_29

        "{color=[obediencecolor]}Massage her thighs{/color}" if (consecutive_mild_choices >= 2 or massageknowledge >= 1) and satisfactionpercentage<100:
            $ renpy.sound.play("audio/soun_fx/groperepeat1.opus", channel="sfx3", loop=False, relative_volume = 1)
            show screen parallax1280("v20_madame_stage5_thighs_massage") with dissolve
            "You massage her inner thighs, and she parts them for you willingly."
            mada "*moan*... Don't stop... please..."
            call increasesatisfaction(30) from _call_increasesatisfaction_19
            call post_action_pause("massage_stage_5_menu") from _call_post_action_pause_30

        "Massage her thighs" if not (consecutive_mild_choices >= 2 or massageknowledge >= 1) and satisfactionpercentage<100:
            $ renpy.sound.play("audio/soun_fx/groperepeat1.opus", channel="sfx3", loop=False, relative_volume = 1)
            show screen parallax1280("v20_madame_stage5_thighs_massage") with dissolve
            "You move to her thighs."
            mada "Gently... don't rush the best part."
            call decreasesatisfaction(10) from _call_decreasesatisfaction_12
            call post_action_pause("massage_stage_5_menu") from _call_post_action_pause_31

        "{color=[obediencecolor]}Massage her boobs{/color}" if (consecutive_mild_choices >= 2 or massageknowledge >= 1) and satisfactionpercentage<100 and massageknowledge>=1:
            $ renpy.sound.play("audio/soun_fx/grabsound.opus", channel="sfx3", loop=False, relative_volume = 1.5)
            show screen parallax1280("v20_madame_stage5_boobs_massage") with dissolve
            "Finally, you cup her bare breasts, massaging them gently."
            mada "YES! OH, GODS, YES!"
            "She arches her back, moaning loudly. Her facade of control is completely gone."
            call increasesatisfaction(30) from _call_increasesatisfaction_20
            call post_action_pause("massage_stage_5_menu") from _call_post_action_pause_32

        "Massage her boobs" if not (consecutive_mild_choices >= 2 or massageknowledge >= 1) and satisfactionpercentage<100:
            $ renpy.sound.play("audio/soun_fx/grabsound.opus", channel="sfx3", loop=False, relative_volume = 1.5)
            show screen parallax1280("v20_madame_stage5_boobs_massage") with dissolve
            mada "Not so rough! Be gentle! You're not just grabbing fruit at the market!"
            call decreasesatisfaction(10) from _call_decreasesatisfaction_13
            call post_action_pause("massage_stage_5_menu") from _call_post_action_pause_33

        # TODO - Either needs a new CG (cause the existing -pulldickout- bad choice CGs have her dressed - or i move this choice to first 3 stages which are dressed)
        "{color=[hatredcolor]}Pull your dick out{/color}" if satisfactionpercentage<100:
            $ consecutive_mild_choices = 0
            $ renpy.sound.play("audio/soun_fx/groperepeat1.opus", channel="sfx3", loop=False, relative_volume = 1)
            "You've brought her to the brink. Thinking this is the moment, you undo your pants."
            mada "...What are you doing?"
            "The pleasure drains from her face, replaced by ice-cold fury."
            hide screen parallax1280
            scene black
            with dissolve
            mada "Did you think this was just a prelude to you fucking me? This was about MY pleasure. You've just made it all about your disgusting lust."
            mada "The deal is off. GET OUT."
            jump massage_minigame_fail

        "I think this massage has served its purpose." if satisfactionpercentage>=100:
            $ consecutive_mild_choices = 0
            if satisfactionpercentage >= 100:
                bo "I think this massage has served its purpose. I've shown you what my hands can do."
                jump massage_final_choice
            else:
                bo "Let's try something different."
                mada "Mmm, no. I'm not finished with this 'something' just yet. Keep going."
                call decreasesatisfaction(20) from _call_decreasesatisfaction_14
                call post_action_pause("massage_stage_5_menu") from _call_post_action_pause_34

#-------------------------------------------------------------------------------
# Endings and Helper Labels
#-------------------------------------------------------------------------------

label massage_final_choice:
    hide screen massage_stage_display
    hide screen massagebar
    scene black
    with dissolve
    "She looks up at you, her body completely pliant, her eyes full of raw desire. She has been conquered, not by force, but by skill."
    mada "Impressive! You have exceeded even my expectations little la- ...[bo_name]."
    mada "A deal is a deal, I am a woman of my word and will uphold my side of the bargain... "
    mada "But first..."
    mada "Allow me to offer a... Different kind of assistance to you..."
    mada "One that I think you desperately need."
    bot "I like the sound of that!"
    call hidescrollingimage from _call_hidescrollingimage_218
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx3", loop=False, relative_volume = 0.7) 
    mada "Grab a towel and make yourself comfortable while I dress..."

    
    $ madamemassage_success = True
    scene rang_massage_successending:
        xalign 0.0 yalign 0.25 zoom 1.25
    with dissolve
    mada "I know more about your predicament than you think, [bo_name]."
    mada "I am aware of the curse that has befallen you, and how potent the urges that compel you are."
    bot "Wait, she knows about the curse? How?!" with vpunch
    mada "Having said that, perhaps it would be wise to address these urges that plague you..."
    mada "Let us take a moment to unwind together, shall we?"
    menu:
        "Accept her offer":
            bo "You don't have to ask me twice, Madame!"
            show rang_massage_successending_smiling with dissolve:
                xalign 0.0 yalign 0.15 zoom 1.25
            mada "Excellent..."
            mada"If we are to help your [hin_rel_mother], you are going to need to prepare for what's to come..."
            mada"I would hope that this..."
            hide screen massagebar
            scene black
            with dissolve
            mada"...Would help with clearing up your mind!"
            "You have successfully satisfied Madame's desires and passed her test. A true reward awaits..."
            jump madame_reward_scene

        "There's no time, [hin_rel] needs me!" if hinata_captured == True:
            bo "There's no time, [hin_rel] needs me!"
            bo "Everything I have gone through tonight has been for her, and I am still nowhere near rescuing her..."
            bo "I... I'm sorry but I don't think I can accept your offer Madame."
            show rang_massage_successending_smiling with dissolve:
                xalign 0.0 yalign 0.15 zoom 1.25
            mada "Straight to business. Just like her..."
            mada "I understand your concern, although I must admit that I am surprised by your self-restraint."
            mada "Many men have died wanting to be in your position right now, and yet you choose to turn it down."
            mada "I would be insulted if I didn't know better, but I can see how important this is to you."
            hide rang_massage_successending_smiling
            show rang_massage_successending:
                xalign 0.0 yalign 0.15 zoom 1.25
            with dissolve
            mada "Very well, I will accept your decision [bo_name]."
            bot "Phew, she doesn't seem to be upset with me."
            bot "...not visibly at least."
            mada "Follow me then, and do not make a sound... I know of a passage that will lead you safely into the dungeons."
            $ madamereward_denied = True
            jump dungeon_secretpassge

        "Ask for a blowjob.":
            bo "I would love to unwind with a sloppy blowjob from you!"
            mada "A... blowjob?"
            show rang_massage_successending_annoyed with dissolve:
                xalign 0.0 yalign 0.15 zoom 1.25
            "Her expression hardens instantly."
            mada "After all this intimacy, all this care..." 
            mada "You would selfishly demand for your own gratification in such a way?"
            mada "Your arrogance is astounding!" with vpunch
            mada "You have sorely misjudged this situation..."
            mada "The deal is off. Leave immediately!" 
            jump massage_minigame_fail

label check_satisfaction:
    if satisfactionpercentage <= 0:
        hide screen massagebar
        $ satisfactionpercentage = 0
        mada "This isn't working. I'm getting more tense, not less."
        hide screen parallax1280
        scene black
        with dissolve
        "She sits up, her expression one of deep disappointment."
        mada "This was a waste of time."
        jump massage_minigame_fail
    return

label post_action_pause(current_menu_label):
    pause 0.5
    call check_satisfaction from _call_check_satisfaction_5
    jump expression current_menu_label

# --- ENDING LABELS ---

label massage_knowledge_too_low:
    hide screen massage_stage_display
    hide screen massagebar
    hide screen parallax1280
    scene black
    with dissolve
    "Your massage knowledge is too low."
    scene bg onsen1_night
    show madame normal2 at left
    show boruto surprised2 at right
    with dissolve
    if hinata_captured == True:
        mada "I am afraid I won't be able to help you any further. The risk is just too high..."
        bo"W-what!? Why!"
        mada "I'll admit you have... potential. But right now, you'd be more likely to wound up dead if I let you continue any further on your own."
        show boruto angry with dissolve
        bo "But I thought if I satisfied you, you'd help me find my [hin_rel]!"
    else:
        mada "I am afraid our night ends here tonight..."
        bo"W-what!? Why!"
        mada "I'll admit you have... potential. But I find you lacking in many regards still and I do not wish to proceed."
        bo "But I thought if I satisfied you, you'd help me!"
    mada"Enough, child! There's too much for me to lose, and not much to gain. Do you even realize the amount of risk you are asking me to take?"
    mada"Perhaps if you had succeeded in convincing me, then I would have considered it..."
    bo"But-"
    mada"No buts! You should be grateful you are still alive..."


    hide madame with dissolve
    mada"Sarah! Escort out guest safely outside the Daimyo's premises..."
    scene black with dissolve
    "Servant" "At once, Madame!"
    "The Madame ordered one of her servants to escort you outside after you failed to meet her expectations."
    jump jumpfrommassage_fail


label massage_minigame_fail:
    hide screen massage_stage_display
    hide screen massagebar
    with dissolve
    # if fail was reached through hitting 0 on bar and some dismissal dialogue was already spoken, don't repeat dismissal
    if satisfactionpercentage != 0:
        mada "That's enough. Your technique is sloppy and you lack the proper focus for this."
        mada "I expected more from the Hokage's [na_rel_to_bo]. You have disappointed me."
        mada "Leave my sight before I call the guards to remove you forcibly."
    "With a final, dismissive wave of her hand, she orders you out. You have failed."
    bo "Wait, but you promised to help me!" with vpunch
    mada "I promised to help if I was {i}satisfied{/i}. I clearly am not. Now get out!"
    jump guards_onsen_thrown_out_ending