label hima_training_proper_start_repeatable:
    $ initialize_replay_defaults()
    scene gymhima_buruma_sweaty_cg with dissolve:
        xalign 0.5 yalign 1
    show gymhima_buruma_sweaty_cg:
        subpixel True
        easein 3 yalign 0.7

    $ playmusic("audio/ost/house2.opus",0.6)
    if first_exercise_hima:
        him "So, what's on the training menu today? Let's just get this over with."
        himt "I still can't believe I have to do this... Being 'coached' by him is infuriating. And yet..."
        bot "She's still trying to process it. The resignation is delicious. Time to remind her who's in charge."
        bo "Alright [him_name], let's see... I think we should start with..."
    else:
        him "Try anything like that again and..."
        bo "And what? Do you want to get stronger or not?"
        bo "Have I not already proven to you I know what I'm doing?"
        him "I-I guess... Just tone down the touching!"
        bo "We'll do whatever's necessary to make you stronger."

    menu hima_training_menu_repeatable:
        # The first training section is available until its milestone flag is set.
        "Hamstring stretches.":
            $ hima_hamstring_repeat_counter = 0
            jump hima_training_hamstrings_repeatable

        # ??? for glute activation (requires hamstring stretch full completion first)
        "{color=[obediencecolor]}???{/color}" if not hima_hamstring_groped:
            bot"I'll probably need to assert more control during the hamstring stretches before she'll be receptive to other kinds of 'help'..."
            jump hima_training_menu_repeatable

        # Unlock if hamstring stretches full completion
        "{color=[obediencecolor]}Glute activation{/color}" if hima_hamstring_groped:
            call checkObedience(statvalue=2, statlevel=2, jumpvalue="none", character="Himawari") from _call_checkObedience_47
            # Fail state if obedience is too low
            if himawari_obedience.level<2 or (himawari_obedience.level == 2 and himawari_obedience.value < 2): 
                bot"She's still too defiant. I need to somehow make her more obedient..."
                jump hima_training_menu_repeatable
            else:
                jump hima_training_glutes_repeatable

        # ??? for posture correction (requires glute activation full completion first which leads to unavoidable failure)
        "{color=[hatredcolor]}???{/color}" (advancement_event=True) if not hima_glute_spanked:
            bot"I'll probably need to assert more control during other exercises before she'll be receptive to other kinds of 'help'..."
            jump hima_training_menu_repeatable

        # Unlock if glute activation full completion achieved
        "{color=[hatredcolor]}Advanced posture correction{/color}" if hima_glute_spanked and dominance.level >= 2:
            call checkHatred(statvalue=35, statlevel=1, jumpvalue="hima_training_menu_repeatable") from _call_checkHatred_44
            # Fail state if obedience is too low
            jump hima_training_posture_repeatable

        "{color=[hatredcolor]}Advanced posture correction{/color}" (advancement_event=True) if hima_glute_spanked and dominance.level == 1:
            call checkHatred(statvalue=35, statlevel=1, jumpvalue="hima_training_menu_repeatable") from _call_checkHatred_45
            # Fail state if obedience is too low
            jump hima_training_posture_repeatable

        "That's enough for today.":
            scene black with dissolve
            bo "We're done for now. Don't think this is over. Your training has just begun."
            him "Whatever... just get out."
            bot "I've planted the seed. Next time, we'll go further."
            jump action_taken

# ==============================================================================
# STRETCH 1: HAMSTRINGS
# ==============================================================================

label hima_training_hamstrings_repeatable:
    bo "Hamstring stretches!"
    bo "Here's what we're gonna do."
    bo "Sit on the floor. Legs straight. Touch your toes."
    him "Hmph! Are we really doing this one again? I know how it works."
    scene black with dissolve
    "She sighs, bracing herself for another round of your insufferable 'guidance'."
    scene hima_hamstring_notstraight_cg with dissolve: 
        xalign 0.5 yalign 1
    show hima_hamstring_notstraight_cg:
        subpixel True
        easein 3 yalign 0.5
    bo "That's what you call straight? This isn't a god damn photoshoot session. This is exercise. Who are you posing for?"
    show hima_hamstring_notstraight_cg_surprised with dissolve:
        yalign 0.5
    himt "*gasp* Why does my body keep doing that? Automatically going into posing mode when I'm supposed to be stretching?!"
    scene black with dissolve
    "Still flustered by the memory of her previous failures, she attempts the stretch again, her form still stubbornly flawed."
    scene hima_hamstring_cg with dissolve:
        xalign 0.5 yalign 0.95
    show hima_hamstring_cg:
        subpixel True
        easein 3 yalign 0.7
    bot "Terrible. She's all about showing off while completely disregarding technique. That pride will be the first thing to break."
    bo "Do you? Because that's not a stretch, that's a spinal injury waiting to happen. Your back is completely rounded."
    him "I HEARD YOU THE FIRST TIME!!" with vpunch
    bot "She's trying to process the humiliation of losing so easily and now being lectured... Little by little she'll get used to it though!"
    bo "Clearly you don't. A teacher doesn't let his student perform a technique incorrectly. We're going to fix this, right now."
    himt "Damn loser, treating me like a child... It's just as annoying as last time. He's still not wrong about my back, but I'll never admit it to the likes of him!"

    menu hima_hamstring_menu_repeatable:
        bot "Her pride is on the line. She's desperate to prove me wrong, and that desperation is the key."

        "Show me again. Slowly." if hima_hamstring_repeat_counter<3:
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
                him "[bo_name]! Is humiliating me the only reason we do this exercise you damn idiot!?" with vpunch
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
            jump hima_hamstring_menu_repeatable

        "{color=[dominancecolor]}???{/color}" if not hima_guide_physically:
            bot"She's not frustrated enough yet. She needs to believe she's incapable of succeeding on her own."
            jump hima_hamstring_menu_repeatable

        # Unlocked permanently after "show me again" 2 times.
        "{color=[dominancecolor]} I'll have to guide you physically.{/color}" if hima_guide_physically:
            call checkDominance(statvalue=30, statlevel=1, jumpvalue="hima_hamstring_menu_repeatable") from _call_checkDominance_65
            $ hima_guide_physically = True
            bo "One thing I noticed is that your pride seems to be an obstacle to your progress." 
            bo "And as you know by now, a good coach has to get hands-on when the student is this resistant."
            him "Don't you dare use that same cheap excuse to g-"
            scene black with dissolve
            "Before she can finish her sentence, you move to sit behind her, your presence looming."
            scene hima_hamstring_lookingback_cg with dissolve: 
                xalign 0.5 yalign 1
            show hima_hamstring_lookingback_cg:
                subpixel True
                easein 3 yalign 0.5
            him "W-What are you doing? D-don't get close to me."
            bo "I'm your teacher. My job is to ensure you learn, even if you're too stubborn to listen. Stay still."
            jump hima_hamstring_correct_form_repeatable

        # ??? for different approach (unlocked when one of the two hamstring kinds of touches is done)
        "{color=[obediencecolor]}???{/color}" if not hima_hamstring_touch_unlocked:
            bot"I guess I have to make her less resistant first..."
            jump hima_hamstring_menu_repeatable

        "{color=[obediencecolor]}Let's try a different approach.{/color}" if hima_hamstring_touch_unlocked:
            $ hima_different_approach = True
            bo "Since plan A isn't working with that stubborn head of yours, I'll need to assess the root of the problem."
            bot "It's not about her failure anymore, it's about my 'diagnosis'. A personal trainer can touch his student, can't he?"
            him "Assess...? What are you talking about?"
            jump hima_hamstring_assess_flexibility_repeatable

        "This is pointless. Let's move on.":
            bo "We'll come back to this. Hamstring stretches aren't your strong suit. But this flexibility issue is going to sabotage all your other training."
            bot "A tactical retreat. I've planted the seed of doubt in her mind about her own body."
            jump hima_training_menu_repeatable

    # First major branch, focusing on 'correcting' her form.
    label hima_hamstring_correct_form_repeatable:
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
        call changeObedience("Himawari", 1, "hima_train_hamstring1", max_times=1, statlevel=2) from _call_changeObedience_160
        $ hima_hamstring_touch_unlocked = True

        menu hima_hamstring_correction_options_repeatable:
            bo "Now... let's fix this mess."

            "Apply firm, steady pressure." if not hima_applied_pressure:
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
                jump hima_hamstring_correction_options_repeatable

            "{color=[dominancecolor]}Force her down. Hard.{/color}" if not hima_forced_down:
                $ hima_forced_down = True
                call checkDominance(30, "hima_hamstring_correction_options_repeatable") from _call_checkDominance_66
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
                call changeDominance(1, max_times=1, fromwhere="hima_hamstring_correction_options_forceherdown") from _call_changeDominance_128
                bo "Good. I'm glad we understand each other."
                jump hima_hamstring_correction_options_repeatable

            "Slide your hands down her back." if not hima_slide_hands:
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
                jump hima_hamstring_correction_options_repeatable

            "Nevermind." if not hima_slide_hands and not hima_forced_down and not hima_applied_pressure:
                bo "You're learning slower than I thought you would."
                bo "Are you gonna take this seriously or what?"
                jump hima_hamstring_menu_repeatable
            
            "Still not quite right." if hima_slide_hands and hima_forced_down and hima_applied_pressure:
                bo "Still not quite right, after all."
                bo "Looks like we need a different approach."
                jump hima_hamstring_menu_repeatable

    # Second major branch, a more direct transgression under the guise of 'assessment'.
    label hima_hamstring_assess_flexibility_repeatable:
        bo "Alright, let's reassess the problem. I still think it's your hamstrings themselves, pulling your pelvis out of alignment."
        him "That's what you said last time..."
        bot "She's buying it. The pseudo-scientific language makes it sound legitimate. Now for the physical exam!"
        bo "I need to check the muscle tension directly. Hold still."
        scene black with dissolve
        "Before she can agree or protest, you reach out and place a hand on her right calf."
        scene hima_hamstring_flexibility_grab_cg with dissolve:
            xalign 0.5 yalign 0.8
        show hima_hamstring_flexibility_grab_cg:
            subpixel True
            easein 3 yalign 0.5
        him "And remind me what this is supposed to achieve, exactly?"
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
        himt "His hand... It's just an 'assessment', he says. Why does my heart still beat so fast every time he does this?"
        bo "I think I know what's going on now that I got a little bit closer."
        bot "The slow, deliberate movement. It's not aggressive, it's calculated... That's why she's not stopping me!"

        menu hima_hamstring_grope_menu_repeatable:
            "Your hand rests on her lower thigh. The real test begins now."

            "{color=[obediencecolor]}Grab her thigh firmly to 'test' the muscle.{/color}" if himawari_obedience_level >= 2:
                call checkObedience(statvalue=2, statlevel=2, jumpvalue="_hima_hamstring_grope_fail_repeatable", character="Himawari") from _call_checkObedience_48
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
                call showscrollingimage from _call_showscrollingimage_268
                bo "I just need to have a better look to know exactly where to start..."
                bot "Her skin is so smooth. I can feel the muscle twitching under my palm. She's trying to decide if she should fight. But she won't. She can't."
                call changeObedience("Himawari", 1, "hima_train_hamstring2", statlevel=2, max_times=1) from _call_changeObedience_161
                scene black
                # Mark exercise as completed to unlock the next
                $ hima_hamstring_groped = True
                him"G-get your hands off me you creep!"
                bo "Will you let me do my job for once? I'm trying to help."
                "You hold the grip for a moment longer than necessary, your thumb stroking her skin. She's flustered and avoids your gaze."
                bo "I think I know where the issue lies already but we'll address that later. For now, let's move on."
                call hidescrollingimage2("Click twice to continue.") from _call_hidescrollingimage2_142
                "She pushes you off quickly, clearly embarrassed."
                $ first_exercise_hima = False
                jump hima_training_proper_start_repeatable

            "{color=[hatredcolor]}Let your hand wander to her inner thigh.{/color}":
                call checkHatred(30, "hima_hamstring_grope_menu_repeatable") from _call_checkHatred_46
                bo "The tightness seems to be radiating. I need to check the adductors as well."
                him "My adductors... again?"
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
                call changeRespect("Himawari", -2) from _call_changeRespect_257
                jump himawari_training_kicked_out_repeatable # Fail condition

            "Stop the assessment.":
                bo "Alright. I've seen enough. Your hamstrings are definitely the issue."
                "You pull your hand back, leaving her to process the interaction."
                bot "A tactical retreat. I've established that her legs are fair game for my 'assessment'. I'll use that opening later."
                jump hima_hamstring_menu_repeatable

        label _hima_hamstring_grope_fail_repeatable:
            #Fail state
            "You reach to grip her thigh, but she recoils instantly."
            scene hima_hamstring_flexibility_grab_cg_v5 with dissolve:
                xalign 0.5 yalign 1
            show hima_hamstring_flexibility_grab_cg_v5:
                subpixel True
                easein 3 yalign 0.5
            him "Don't touch me there! I knew you were a pervert!"
            "You pushed too far. She's not compliant enough for that yet."
            call changeRespect("Himawari", -2) from _call_changeRespect_258
            jump himawari_training_kicked_out_repeatable

label hima_training_glutes_repeatable:
    bo "Glute bridges. Your ass is your biggest muscle group, but you're not using it. Lie on your back."
    him "Ugh, not this one. Again?! You pervy idiot!"
    scene black with dissolve
    "She reluctantly lies down, her gaze fixed on the ceiling, avoiding you."
    scene himawari_glutes_lie_cg with dissolve:
        xalign 0.5 yalign 1
    show himawari_glutes_lie_cg:
        subpixel True
        easein 3 yalign 0.5
    bot "D-damn it, in that position, laying down, she looks just about ready for me to..."
    show screen parallax1280("himawari_glutes_lie_cg", initial_ypos=0.5) with dissolve
    call showscrollingimage from _call_showscrollingimage_269
    bot "No, I can't take it that far with her yet."
    him "...Well? Come on, expert."
    bo "R-right! Just... checking your starting form. Can't be too careful."
    bo "I just figured you would've learned the next steps by now."
    bo "Now, lift your hips. Squeeze your glutes at the top."
    scene black
    call hidescrollingimage2("Click twice to continue.") from _call_hidescrollingimage2_143
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
    him "There you go again! Building me up just to tear me down, I ALREADY AM doing that! J-just tell me what to do next!" with vpunch
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


    menu hima_glute_bridge_menu_repeatable:

        "Let's test your explosive power.":
            bo "Your lift-off is still weak. No power. It looks like you're using your back, not your glutes. Drive your heels into the floor and thrust."
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
            jump hima_glute_bridge_menu_repeatable

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
            himt "Is he making things up again? I still can't tell for sure when he's watching me like that. He's messing with my head."
            bot "Gaslighting 101. Make her doubt her own senses."
            $ hima_diagnosis_stability = True
            jump hima_glute_bridge_menu_repeatable

        "Let's test your muscle activation.":
            bo "Okay, let's get back to basics. I still think the root problem is muscle activation. You're not firing your glutes at all."
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
            jump hima_glute_bridge_menu_repeatable

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
            jump hima_glute_guide_hips_repeatable

        "{color=[obediencecolor]}????{/color}" if not hima_diagnosis_stability or not hima_diagnosis_lift:
            "If I keep telling her what she's doing wrong she'll probably be less resistant to my other plans..."
            jump hima_glute_bridge_menu_repeatable

        "{color=[dominancecolor]}You're not creating the necessary mind-muscle connection.{/color}" if hima_diagnosis_activation and hima_diagnosis_lift:
            # UNLOCKED BY THE ACTIVATION 'FAILURE'.
            bo "Your brain isn't connecting with the right muscle. It's a common problem for amateurs. We need to use tactile prompting to create that neural pathway."
            him "Tactile... prompting? Are you really using that bullshit terminology with me again?"
            bo "It's basic kinesiology. Do you want to fix the problem or not?"
            him "F-fine! Whatever, you nerd!"
            bot "Wrapped the transgression in jargon she can't dispute. She's agreed to be touched because she's too proud to admit she doesn't understand."
            jump hima_glute_tactile_feedback_repeatable

        "{color=[dominancecolor]}????{/color}" if not hima_diagnosis_activation or not hima_diagnosis_lift:
            "If I keep telling her what she's doing wrong she'll probably be less resistant to my other plans..."
            jump hima_glute_bridge_menu_repeatable

        "This is pointless. Let's move on.":
            bo "We'll come back to this. Your entire posterior chain is a mess. It needs a lot of work."
            jump hima_training_menu_repeatable

    # BRANCH 1: Manual Stabilization (The "Safer" Control Path)
    label hima_glute_guide_hips_repeatable:
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
        himt "He's so close... My hips feel more stable when he does this, as much as I hate it I can't deny it, UGH!"
        bot "Controlling her every move. My touch equals 'correctness'. Her body is learning to move to my rhythm."
        call changeObedience("Himawari", 1, "hima_train_glute1", statlevel = 2, max_times=1) from _call_changeObedience_162
        
        menu hima_glute_hip_guidance_menu_repeatable:
            bo "Don't break form. Feel the pressure building in your muscles."

            "{color=[dominancecolor]}Good. Hold it there.{/color}":
                call checkDominance(30, "hima_glute_hip_guidance_menu_repeatable") from _call_checkDominance_67
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
                call changeDominance(1, "hima_glute_hip_guidance_menu_dialogue", max_times=1) from _call_changeDominance_129
                "As she holds the position in embarrassment, she reluctantly tries to move your hands away from her ass."
                show screen parallax1280("boruto_holding_her_cg_v3", initial_ypos=0.5) with dissolve
                call showscrollingimage from _call_showscrollingimage_270
                him "[bo_name_stutter], your hands are t-"
                bo "What's wrong? You lost tension. Focus. I'm just making sure you're not imbalanced."
                "She freezes, her eyes wide. She doesn't drop, but her breathing is irregular."
                himt "Is he trying to...? No. He's... checking my alignment. It's part of the training. So why does my skin feel like it's on fire?"
                bot "She's too flustered to protest. The boundary has been moved without a single shot fired!"
                call hidescrollingimage2("Click twice to continue.") from _call_hidescrollingimage2_144
                jump hima_glute_hip_guidance_menu_repeatable

            "Alright, that's enough stabilization.":
                bo "Better. You're starting to understand the movement. Let's move on."
                jump hima_glute_bridge_menu_repeatable


    # BRANCH 2: Tactile Feedback (The Transgressive "Technical" Path)
    label hima_glute_tactile_feedback_repeatable:
        menu hima_glute_feedback_options_repeatable:
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
                him "YOU'RE GRABBING MY ASS AGAIN, IDIOT! Don't you dare call it 'prompting' this time! Are you insane?!" with vpunch
                bo "Quit whining, I'm trying to help you here. Do it right and I won't have to get physical."
                bot "Yeah... right!"
                $ hima_glute_poked_for_real = True
                jump hima_glute_feedback_options_repeatable

            "{color=[hatredcolor]}A 'prompt' isn't enough. Use a 'motivational slap'.{/color}" if hima_glute_poked_for_real == True:
                call checkHatred(35, "hima_glute_feedback_options_repeatable") from _call_checkHatred_47
                bo "The finger prompt was too subtle for you. The neural signal is weak. You need a larger surface area to register the command. A stronger stimulus."
                him "A stronger... stimulus? Don't you dare..."
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
                him "HOW DARE Y-" with vpunch
                bo "I said, AGAIN."
                $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.9)
                show boruto_grope_her_cg with vpunch    
                "Her body is trembling, a tear of frustration in her eye, but she pushes her hips up again, higher this time."
                "Or was it just the force of your spank?"
                scene black with dissolve
                call changeHatred(1, fromwhere="hima_train_glute_spank", max_times=1) from _call_changeHatred_212
                him "That's IT!! I've had ENOUGH! HOW DARE YOU TOUCH ME LIKE THAT, YOU CREEP!" with vpunch
                # Mark exercise as completed, fail this attempt but unlock next option for next time
                $ hima_glute_spanked = True
                jump himawari_training_kicked_out_repeatable

            "Let's move on before you hurt yourself.":
                bo "Let's move on. Try to remember that feeling of activation."
                jump hima_training_menu_repeatable

label hima_training_posture_repeatable:
    # Phase 1: The Sell. Manipulating her into the position.
    bo "Alright, let's work on that advanced posture correction again. Let's see if you've improved at all."
    him "Not ready? I can do anything you can do, loser."
    bot "Predictable. Her pride is a string I can pull any time I want."
    bo "It's not about strength. It's about control and precision. It's called a controlled quadrupedal spinal articulation."
    him "That 'quadrupedal' thing again? Just tell me what to do, smartass!"
    him "And quit making words up to sound smart!" 
    himt "But... 'advanced'... I have to prove I can do it."
    bo "Get on all fours. Hands under your shoulders, knees under your hips."
    him "On all fours... again!? Are you ever going to let this go? I'm not your pet!" with vpunch
    
    menu hima_posture_initial_sell_repeatable:
        him "On all fours... again!? Are you ever going to let this go? I'm not your pet!"

        "It's a foundational athletic stance.":
            bo "It's a foundational athletic stance, [him_name]. We've been over this. Or do they not teach you basic kinesiology at your school? If it's too 'advanced' for you, we can stop."
            him "F-fine! I can do it! It's not a big deal."
            scene black with dissolve
            call changeObedience("Himawari", 1, "hima_posture_comply_kinesiology", statlevel=2, max_times=1) from _call_changeObedience_163

        "It's what I told you to do.":
            bo "It's the position your teacher commanded. Don't make me repeat it over and over again. Are you going to obey, or are you going to waste more of my time?" with vpunch
            him "Tch... You don't have to be such a jerk about it."
            "As her resistance slowly weakens, she gets in position just to get it over with."
            scene black with dissolve
            call changeDominance(1, max_times=1, fromwhere="hima_posture_initial_sell_repeatable") from _call_changeDominance_130
            
        "Is it too demeaning for you?":
            bo "What's the matter? Is getting on your hands and knees still too demeaning for the great [him_name]?"
            him "W-what!? Of course not! It's just a dumb stretch!" with vpunch
            bot "Her pride is so easy to weaponize. Once again she just submits to my request just to spite me..."
            scene black with dissolve
            "Flustered and angry, she immediately gets into position."
            call changeHatred(1, fromwhere="hima_posture_demean_response", max_times=1) from _call_changeHatred_213

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
    bot "Heh. Exactly what I need, as always."
    bo "We went over this. It's easier if I show you. Now hold still."
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
    call showscrollingimage from _call_showscrollingimage_271
    him "And you're going to tell me that hand placement is 'necessary' again, aren't you?"
    bo "You asked for more specific instructions. This is it. Stop flopping around and hold the position."
    bot "The first point of contact is made. Now time for some good old reverse psychology..."

    menu hima_posture_correction_submenu_repeatable:
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
            call hidescrollingimage2("Click twice to continue.") from _call_hidescrollingimage2_145
            jump hima_posture_place_second_hand_repeatable

label hima_posture_place_second_hand_repeatable:
    scene black with dissolve
    "Once again, you take advantage of the moment to place your other hand squarely on her ass."
    scene himawari_plank_grope_re_cg_v2 with dissolve:
        xalign 0.5 yalign 1
    show himawari_plank_grope_re_cg_v2:
        subpixel True
        easein 3 yalign 0.5
    $ renpy.sound.play("/audio/soun_fx/himawari/himagasp2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    him "*Gasp*!"
    himt "His hand! Right on my... again! This can't be part of the training... but it works. My hips are stable. Was he... right about this being the only way?!"
    bot "The pretext of 'stabilization' is the ultimate shield. She can't argue with results, even if the method is a violation."
    call changeObedience("Himawari", 1, "hima_train_posture_stabilize", statlevel=2, max_times=1) from _call_changeObedience_164
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
    him "UGH!! Again?!" with vpunch
    bo "What, you thought all you have to do is plank on the floor for a few seconds?"
    bo "Anyone can do that!"
    him "I still can b-barely just hold this position, I don't think I can move."
    bot "She's subconsciously begging for my help again..."
    bo "Maybe you could use a little bit of help then, I guess you are a slow learner unless guided."
    scene himawari_plank_guide_bor_cg with dissolve
    bo "Now, from this position, you have to get your butt a little bit lower to fully engage your abs."
    him "H-how much lower?"
    bot "She's getting used to my hand on her thigh. Good."
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

    menu posture_ending_menu_repeatable:
        "Threaten to spank her for poor performance.":
            bo "This is pathetic, your form is weak and you wanna quit already? Keep going or I'll give you some real 'tactile feedback' to remember."
            him "Don't you dare threaten me again!"
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

label himawari_training_kicked_out_repeatable:
    
    scene himawari_angry_cg with Dissolve(0.2):
        xalign 0.5 yalign 1
    show himawari_angry_cg:
        subpixel True
        easein 0.2 yalign 0.5

    him "I can't believe I was stupid enough to trust you, AGAIN! Get out of my room! NOW!"
    bo "It was just a joke, calm down!"
    him "GET OUT!" with vpunch

    scene black with vpunch
    $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx2", loop=False, relative_volume = 0.9)
    "The door slams shut so hard the frame rattles."
    bot "Well... that could have gone better."

    jump action_taken