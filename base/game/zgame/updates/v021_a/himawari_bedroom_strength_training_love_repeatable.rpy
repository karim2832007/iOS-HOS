# Love variant repeatable labels

label hima_training_proper_start_love_repeatable:
    $ initialize_replay_defaults()
    scene gymhima_buruma_sweaty_cg with dissolve:
        xalign 0.5 yalign 1
    show gymhima_buruma_sweaty_cg:
        subpixel True
        easein 3 yalign 0.7

    $ playmusic("audio/ost/house2.opus",0.6)
    # This is the repeatable variation. The first_exercise_hima flag would be false.
    him "Alright, let's get this over with. Just... try not to be as weird about it as last time."
    bo "Hey, I'm just trying to help. We've been over this, sometimes physical contact is necessary to make sure your form is right."
    bo "You know by now that I know what I'm doing, right?"
    him "I-I guess... Just keep the touching to a minimum! Let's just start."
    bo "Alright, alright. I'll only do what's necessary to help you."

    menu hima_training_menu_love_repeatable:
        # The first training section is available until its milestone flag is set.
        "Hamstring stretches.":
            $ hima_hamstring_repeat_counter = 0
            jump hima_training_hamstrings_love_repeatable

        # ??? for glute activation (requires hamstring stretch full completion first)
        "{color=[obediencecolor]}???{/color}" if not hima_hamstring_groped:
            bot "We need to make sure she gets the hamstring stretches right before we move on. Repetition is key."
            jump hima_training_menu_love_repeatable

        # Unlock if hamstring stretches full completion
        "{color=[obediencecolor]}Glute activation{/color}" if hima_hamstring_groped:
            call checkObedience(statvalue=2, statlevel=2, jumpvalue="none", character="Himawari") from _call_checkObedience_45
            # Fail state if obedience is too low
            if himawari_obedience.level<2 or (himawari_obedience.level == 2 and himawari_obedience.value < 2): 
                bot "She's still not quite comfortable enough with my help for this one. I need to build more trust..."
                jump hima_training_menu_love_repeatable
            else:
                jump hima_training_glutes_love_repeatable

        # ??? for posture correction (requires glute activation full completion first which leads to unavoidable failure)
        "{color=[lovecolor]}???{/color}" (advancement_event=True) if not hima_glute_spanked:
            bot "I should make sure she gets the other exercises right before we move on to more advanced things."
            jump hima_training_menu_love_repeatable

        # In the Love variant, this is not an aggressive act, but an accidental slip-up that creates an intimate moment.
        "{color=[lovecolor]}Advanced posture correction{/color}" if hima_glute_spanked and dominance.level >= 2:
            call checkLove(character="Himawari", statvalue=11, statlevel=1, jumpvalue="hima_training_menu_love_repeatable") from _call_checkLove_14
            jump hima_training_posture_love_repeatable

        "{color=[lovecolor]}Advanced posture correction{/color}" (advancement_event=True) if hima_glute_spanked and dominance.level == 1:
            call checkLove(character="Himawari", statvalue=11, statlevel=1, jumpvalue="hima_training_menu_love_repeatable") from _call_checkLove_15
            jump hima_training_posture_love_repeatable

        "That's enough for today.":
            scene black with dissolve
            bo "We're done for now. You did great today. Keep this up and you'll be unstoppable."
            him "Whatever... just get out."
            bot "She's definitely getting more used to this. Progress is slow, but it's there."
            jump action_taken

# ==============================================================================
# STRETCH 1: HAMSTRINGS (Repeatable Version)
# ==============================================================================

label hima_training_hamstrings_love_repeatable:
    bo "Alright, let's start with the hamstring stretches again."
    him "I know, I know. Sit on the floor, legs straight, touch my toes. I remember."
    scene black with dissolve
    "She moves into the position, already anticipating your critique."
    scene hima_hamstring_notstraight_cg with dissolve: 
        xalign 0.5 yalign 1
    show hima_hamstring_notstraight_cg:
        subpixel True
        easein 3 yalign 0.5
    bo "I know this is repetitive, but proper form is built on getting the basics perfect. I don't want you getting injured."
    show hima_hamstring_notstraight_cg_surprised with dissolve:
        yalign 0.5
    himt "Ugh, he's giving me that look again... The 'I'm so concerned about your safety' one. It's still... kind of flustering."
    scene black with dissolve
    "A bit flustered, she attempts the stretch, and just like before, her back immediately rounds."
    scene hima_hamstring_cg with dissolve:
        xalign 0.5 yalign 0.95
    show hima_hamstring_cg:
        subpixel True
        easein 3 yalign 0.7
    bot "Same mistake as last time. She's so focused on touching her toes she's forgetting everything else. I need to be patient."
    bo "Easy there..."
    bot "Still a terrible try, honestly."
    bo "Your back is still rounding. We talked about this. You're going to strain it."
    him "I'M TRYING! YOU DON'T HAVE TO SAY IT EVERY SINGLE TIME!" with vpunch
    bot "She's embarrassed that she hasn't improved. Gentle but firm is the way to go."
    bo "Hey, I have to say it every time you do it. A good coach corrects bad form until it's good form. We're going to fix this."
    himt "He's not wrong... but having him watch so closely is making me nervous."

    menu hima_hamstring_menu_love_repeatable:
        bot "She wants to prove she can do it. I can use that."

        "Let's see it again." if hima_hamstring_repeat_counter<3:
            if hima_hamstring_repeat_counter == 0:
                bo "Okay, let's see it again. Remember, back straight. Hinge from the hips."
                him "It IS straight! Or I'm trying to make it!"
                bo "Just focus. Try again."
                scene himawari_bedroom_strength_training_line_347 with dissolve:
                    xalign 0.5 yalign 1
                show himawari_bedroom_strength_training_line_347:
                    subpixel True
                    easein 3 yalign 0.7
                "She huffs and attempts the stretch again, with the same result."

            elif hima_hamstring_repeat_counter == 1:
                bo "Still the same mistake. You're just collapsing your torso. Are you even thinking about what I said?"
                him "Just shut up and let me concentrate! You're making it worse!"
                himt "Why is this so hard!? And why is he still watching me so closely!?"
                bo "Try it again."
                scene himawari_bedroom_strength_training_line_354 with dissolve: 
                    xalign 0.5 yalign 1.0
                show himawari_bedroom_strength_training_line_354:
                    subpixel True
                    easein 3 yalign 0.7
                "She tries again, her frustration clearly visible."
            elif hima_hamstring_repeat_counter == 2:
                bo "We're not getting anywhere like this. One more try."
                him "[bo_name]! Are you just trying to piss me off!?" with vpunch
                scene himawari_bedroom_strength_training_line_362 with dissolve:
                    xalign 0.5 yalign 1
                show himawari_bedroom_strength_training_line_362:
                    subpixel True
                    easein 3 yalign 0.7
                bo "I'm trying to teach you. If you'd just listen instead of fighting me, we could move on."
                bot "She has to be frustrated enough now to accept my help. She knows what's coming next."

            $ hima_hamstring_repeat_counter += 1
            if hima_hamstring_repeat_counter >= 2:
                $ hima_guide_physically = True
            jump hima_hamstring_menu_love_repeatable

        "{color=[dominancecolor]}???{/color}" if not hima_guide_physically:
            bot "She's still too proud. A few more failed attempts should convince her she needs my help."
            jump hima_hamstring_menu_love_repeatable

        # Unlocked permanently after "show me again" 2 times.
        "{color=[lovecolor]} Looks like I'll have to guide you. Again.{/color}" if hima_guide_physically:
            call checkLove(character="Himawari", statvalue=10, statlevel=1, jumpvalue="hima_hamstring_menu_love_repeatable") from _call_checkLove_16
            $ hima_guide_physically = True
            bo "Okay, looks like telling you still isn't enough. Your pride is getting in the way." 
            bo "Time for the hands-on approach again."
            him "Don't you dare use that as an excuse to t-"
            scene black with dissolve
            "Before she can finish, you move to sit behind her, just as you did last time."
            scene hima_hamstring_lookingback_cg with dissolve: 
                xalign 0.5 yalign 1
            show hima_hamstring_lookingback_cg:
                subpixel True
                easein 3 yalign 0.5
            him "Y-You're not going to... You know."
            bo "I'm your coach. My job is to fix your form. I need you to trust me on this. Stay still."
            jump hima_hamstring_correct_form_love_repeatable

        # ??? for different approach (unlocked when one of the two hamstring kinds of touches is done)
        "{color=[obediencecolor]}???{/color}" if not hima_hamstring_touch_unlocked:
            bot "I should try helping her directly first..."
            jump hima_hamstring_menu_love_repeatable

        "{color=[obediencecolor]}Let's try a different approach.{/color}" if hima_hamstring_touch_unlocked:
            $ hima_different_approach = True
            bo "Since that's not working, let's try to figure out the root of the problem."
            bot "Framing this as a diagnosis might make her more receptive and less self-conscious."
            him "Assess...? What are you talking about?"
            jump hima_hamstring_assess_flexibility_love_repeatable

        "Not too bad, let's move on.":
            bo "We'll come back to this. Flexibility is important, and we need to work on it if you want to avoid injury."
            bot "A tactical retreat. I've planted the seed that her form needs work. She'll be thinking about it."
            jump hima_training_menu_love_repeatable

    # First major branch, focusing on 'correcting' her form.
    label hima_hamstring_correct_form_love_repeatable:
        bo "You know the drill. I'm going to place my hands on your back to guide you into the proper alignment."
        scene black with dissolve
        "You gently place your hands on her lower back. She flinches slightly, but doesn't pull away."
        scene himawari_bedroom_strength_training_line_227_love with dissolve:
            xalign 0.5 yalign 1
        show himawari_bedroom_strength_training_line_227_love:
            subpixel True
            easein 3 yalign 0.5
        him "I-I'm not tense!"
        bo "You are. Even more than last time. Just relax."
        himt "Why does this keep happening? I know he's just trying to help, but having him this close... It makes me so flustered."
        call changeObedience("Himawari", 1, "hima_train_hamstring1", max_times=1, statlevel=2) from _call_changeObedience_156
        $ hima_hamstring_touch_unlocked = True

        menu hima_hamstring_correction_options_love_repeatable:
            bo "Now... let's fix this. Again."

            "Apply firm, steady pressure." if not hima_applied_pressure:
                $ hima_applied_pressure = True
                bo "I'm going to apply some pressure. Try to breathe into the stretch, don't fight it."
                scene black with dissolve
                "You push down firmly but gently, helping her back to straighten. She gasps, the feeling familiar now."
                scene himawari_bedroom_strength_training_line_227_v2_love with dissolve:
                    xalign 0.5 yalign 1.0
                show himawari_bedroom_strength_training_line_227_v2_love:
                    subpixel True
                    easein 3 yalign 0.7
                him "*gasp* O-okay... I remember this feeling."
                himt "It still hurts... but it's that good kind of hurt. It feels right. Why does it only feel right when he does this?"
                bo "That's a proper stretch. Your body needs to learn this. We'll keep doing it until it's second nature."
                bot "She's associating my touch with progress. Excellent."
                jump hima_hamstring_correction_options_love_repeatable

            "{color=[lovecolor]}Let's give you a real stretch.{/color}" if not hima_forced_down:
                $ hima_forced_down = True
                call checkLove(character="himawari", statvalue=10, jumpvalue="hima_hamstring_correction_options_love_repeatable") from _call_checkLove_17
                bo "You're still holding back. I know you can go deeper. Let's not waste time."
                scene black with dissolve
                "With a quick 'Ready?', you push her back down again, guiding her much deeper into the stretch, just like before."
                scene himawari_bedroom_strength_training_line_227_v3 with dissolve:
                    xalign 0.5 yalign 1
                show himawari_bedroom_strength_training_line_227_v3:
                    subpixel True
                    easein 3 yalign 0.5
                him "H-hey, still no warning, huh!?"
                bo "See? You can do it. You just needed a push. Are you starting to trust me yet?"
                himt "He was right... again. It's so frustrating!"
                him "I-I..."
                call changeLove(1, max_times=1, fromwhere="hima_hamstring_correction_options_forceherdown") from _call_changeLove_59
                bo "Good. Glad we're on the same page."
                jump hima_hamstring_correction_options_love_repeatable

            "Slide your hands down her back." if not hima_slide_hands:
                $ hima_slide_hands = True
                bo "Let me check your alignment again. Your whole spine seems out of whack."
                scene black with dissolve
                "You slowly slide your hands from her shoulders down her back, the motion familiar to both of you."
                scene himawari_bedroom_strength_training_line_227_v4 with dissolve:
                    xalign 0.5 yalign 1
                show himawari_bedroom_strength_training_line_227_v4:
                    subpixel True
                    easein 3 yalign 0.5
                him "A-are you doing that 'tension knot' check again!?"
                bo "And I'm still finding them. Chronic poor posture. We really need to fix this."
                bot "I can't believe her posture is still this bad. She really could hurt herself if she's not careful."
                him "O-okay... fine. Just... be quick about it."
                jump hima_hamstring_correction_options_love_repeatable

            "Nevermind." if not hima_slide_hands and not hima_forced_down and not hima_applied_pressure:
                bo "You're not focusing. Are you taking this seriously?"
                jump hima_hamstring_menu_love_repeatable
            
            "Still not quite right." if hima_slide_hands and hima_forced_down and hima_applied_pressure:
                bo "Better, but still not quite right."
                bo "Looks like we need a different approach."
                jump hima_hamstring_menu_love_repeatable

    # Second major branch, a more direct assessment.
    label hima_hamstring_assess_flexibility_love_repeatable:
        bo "I still think the problem isn't your back, but your hamstrings. They're probably so tight they're pulling your pelvis out of alignment."
        him "You said that last time..."
        bo "And it's still true. I need to check the muscle tension directly. Hold still."
        scene black with dissolve
        "Knowing she'll protest, you act quickly, placing a hand on her right calf before she can pull away."
        scene hima_hamstring_flexibility_grab_cg with dissolve:
            xalign 0.5 yalign 0.8
        show hima_hamstring_flexibility_grab_cg:
            subpixel True
            easein 3 yalign 0.5
        him "Is this really necessary to do again?"
        bo "It's diagnostic. We need to track your progress. Trust the process."
        show hima_hamstring_flexibility_grab_cg:
            subpixel True
            easein 0.5 yalign 0.7 zoom 1.2
        "You gently squeeze her calf muscle."
        bo "Hmm. Still tense. As I suspected."
        scene black with dissolve
        "You reposition yourself, sliding your hand up slowly, just as you did before."
        scene hima_hamstring_flexibility_grab_cg_v2_love with dissolve:
            xalign 0.5 yalign 1.0
        show hima_hamstring_flexibility_grab_cg_v2_love:
            subpixel True
            easein 3 yalign 0.5
        himt "His hand... It's just an 'assessment', I know, but my heart is beating so fast again. Why am I not used to this yet?"
        bo "Okay, I'm getting a feel for it. I think I know what we need to work on."

        menu hima_hamstring_grope_menu_love_repeatable:
            "Your hand rests on her lower thigh. This is just as awkward as last time."

            "{color=[obediencecolor]}Gently squeeze her thigh to 'test' the muscle.{/color}" if himawari_obedience_level >= 2:
                call checkObedience(statvalue=2, statlevel=2, jumpvalue="_hima_hamstring_grope_fail_love_repeatable", character="Himawari") from _call_checkObedience_46
                scene black with dissolve
                bo "Yep, this is still the source of the problem. Right here."
                "Your hand gently but firmly squeezes her mid-thigh, just like before."
                scene hima_hamstring_flexibility_grab_cg_v3 with dissolve:
                    xalign 0.5 yalign 1.0
                show hima_hamstring_flexibility_grab_cg_v3:
                    subpixel True
                    easein 3 yalign 0.6
                $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                him "H-Hey! Still feels weird!"
                bo "Tight as a drum. We have a lot of work to do if you want to be ready for the exams."
                show screen parallax1280("hima_hamstring_flexibility_grab_cg_v3", initial_ypos=0.6) with dissolve
                call showscrollingimage from _call_showscrollingimage_262
                bo "This is necessary. We don't want you tearing a muscle."
                bot "Her skin is so smooth... Okay, focus! Just help her."
                call changeObedience("Himawari", 1, "hima_train_hamstring2", statlevel=2, max_times=1) from _call_changeObedience_157
                scene black
                # Mark exercise as completed to unlock the next
                $ hima_hamstring_groped = True
                him"...[bo_name_stutter]!"
                bo "S-sorry! Zoned out for a second."
                bo "Okay, I know what the issue is. We can work on it. Let's move on for now."
                call hidescrollingimage2("Click twice to continue.") from _call_hidescrollingimage2_136
                "She pulls her leg away quickly, her face flushed."
                $ first_exercise_hima = False
                jump hima_training_proper_start_love_repeatable

            "{color=[lovecolor]}You 'slip' again, and your hand lands on her inner thigh.{/color}":
                call checkLove(character="Himawari", statvalue=11, jumpvalue="hima_hamstring_grope_menu_love_repeatable") from _call_checkLove_18
                bo "The tightness seems to be radiating. Let me check the adductors again."
                him "My... adductors? You said that last time right before you..."
                scene black with dissolve
                "As you shift to get a better angle, your hand 'slips' on the floor, sliding up and brushing against the soft skin of her inner thigh. She jumps, pulling her leg away instantly."
                scene hima_hamstring_flexibility_grab_cg_v4_love with dissolve:
                    xalign 0.5 yalign 1
                show hima_hamstring_flexibility_grab_cg_v4_love:
                    subpixel True
                    easein 3 yalign 0.5      
                him "HEY! Did you just 'slip' on purpose this time!?"
                bo "N-No! Of course not! The floor is just... really slippery right here! I swear!"
                bot "Oh god, she's on to me. She totally thinks I'm a creep now. But she's not yelling... much."
                call changeRespect("Himawari", -1) from _call_changeRespect_255
                "She stares at you, her face bright red, a mix of anger and embarrassment."
                him "...Just be more careful! If you're going to keep doing this, at least don't be so clumsy. Let's... let's just move on."
                bot "She said 'keep doing this'? Phew. That was way too close."
                jump hima_training_menu_love_repeatable

            "Stop the assessment.":
                bo "Alright. I've felt enough. Your hamstrings are definitely still the issue."
                "You pull your hand back, leaving her to process the interaction."
                bot "Okay, that's enough awkwardness for one day. But I've reinforced the idea that I need to physically check things to help her."
                jump hima_hamstring_menu_love_repeatable

label _hima_hamstring_grope_fail_love_repeatable:
    #Fail state
    "You reach to touch her thigh, but she recoils instantly."
    scene hima_hamstring_flexibility_grab_cg_v5 with dissolve:
        xalign 0.5 yalign 1
    show hima_hamstring_flexibility_grab_cg_v5:
        subpixel True
        easein 3 yalign 0.5
    him "Don't touch me there! I knew you were just being a pervert!"
    "You pushed too far. She's not comfortable enough for that yet."
    call changeRespect("Himawari", -2) from _call_changeRespect_256
    jump himawari_training_kicked_out_love_repeatable

label hima_training_glutes_love_repeatable:
    bo "Time for glute bridges. Let's see if you've been practicing your form."
    him "Ugh, this exercise again? Fine. Just... try not to stare this time."
    scene black with dissolve
    "She lies down, a look of weary resignation on her face."
    scene himawari_glutes_lie_cg with dissolve:
        xalign 0.5 yalign 1
    show himawari_glutes_lie_cg:
        subpixel True
        easein 3 yalign 0.5
    bot "Okay... she's in position. It's just as distracting as I remember. Be professional. Focus."
    show screen parallax1280("himawari_glutes_lie_cg", initial_ypos=0.5) with dissolve
    call showscrollingimage from _call_showscrollingimage_263
    bot "Just focus on her form. Don't get lost."
    him "...Well? Are you just going to stare all day, coach?"
    bo "R-right! Sorry! Checking your alignment."
    bo "Okay, lift your hips. Squeeze at the top. You know the drill."
    scene black
    call hidescrollingimage2("Click twice to continue.") from _call_hidescrollingimage2_137
    scene black with dissolve
    "She thrusts her hips upward, her form slightly better than last time, but still flawed."
    scene himawari_glutes_up_cg with dissolve:
        xalign 0.5 yalign 1.0
    show himawari_glutes_up_cg:
        subpixel True
        easein 3 yalign 0.8
    bot "She's definitely strong, but the bad habits are still there. I have to correct them."
    bo "Better than last time, but your hips are still a little tilted. Remember what I said about stability?"
    him "I am! J-just tell me what I'm doing wrong... again!"
    him "You keep telling me I'm athletic and then listing all my flaws!"
    bot "She's getting frustrated with the slow progress. I need to keep her motivated."
    bo "It's about doing it *right* to build good habits. We need to pinpoint the issue."
    bo "I might have to give you some... tactile feedback again. So you can feel which muscles to engage."
    scene black with dissolve
    "You move to kneel beside her, and she looks up at you with a familiar, concerned expression."
    scene himawari_glutes_up_concerned_cg with dissolve:
        xalign 0.5 yalign 1.0
    show himawari_glutes_up_concerned_cg:
        subpixel True
        easein 3 yalign 0.5
    him "Tactile... feedback? Oh no, not again."

    menu hima_glute_bridge_menu_love_repeatable:

        "Let's work on your explosive power.":
            bo "Your lift-off is still a little weak. It looks like you're still using your back. Remember: drive with the heels. Thrust."
            scene black with dissolve
            "She tries again, concentrating hard."
            scene himawari_glutes_up_concerned_cg_v2 with dissolve:
                xalign 0.5 yalign 1
            show himawari_glutes_up_concerned_cg_v2:
                subpixel True
                easein 3 yalign 0.5
            him "Hnngh! Like that?"
            himt "I'm trying, but it still feels awkward. Is he ever going to say I did it right?"
            bo "Almost! Still too much lower back. Think about pushing the floor away with your feet."
            him "If you're such an expert, explain it better!"
            bot "She's trying so hard. I need to find a new way to get through to her."
            $ hima_diagnosis_lift = True
            jump hima_glute_bridge_menu_love_repeatable

        "Let's check your stability.":
            bo "Do it again. And do it right this time. Don't rush it."
            him "Ughhh..!"
            scene black with dissolve
            "She gets into position, trying to hold perfectly still, but a slight wobble gives her away."
            scene himawari_glutes_up_concerned_cg_v3 with dissolve:
                xalign 0.5 yalign 1.0
            show himawari_glutes_up_concerned_cg_v3:
                subpixel True
                easein 3 yalign 0.8
            bo "See? There it is again. Your right hip dipped. That's the instability we talked about."
            him "It did not! I was perfectly still this time!"
            bo "I saw it. It's a common issue, don't get defensive. It just means we need to correct it."
            himt "He's watching so closely... Was I really shaking? This is so embarrassing."
            bot "Okay, need to be careful not to discourage her. Just focus on being helpful."
            $ hima_diagnosis_stability = True
            jump hima_glute_bridge_menu_love_repeatable

        "Let's test your muscle activation.":
            bo "Let's forget the other stuff for a second. The root problem might still be that you're not firing your glutes properly."
            him "Of course I am! I can feel it!"
            bo "Are you sure? Lift up, and consciously squeeze just your glutes. Isolate the muscle."
            scene black with dissolve
            "She lifts and squeezes, concentrating on your words."
            scene himawari_glutes_up_concerned_cg_v4 with dissolve:
                xalign 0.5 yalign 1.0
            show himawari_glutes_up_concerned_cg_v4:
                subpixel True
                easein 3 yalign 0.5
            him "What about n-"
            bo "Nope. I can still see your hamstrings and lower back engaging. You're compensating."
            him "I'M NOT COMPENSATING!" with vpunch
            bo "O-okay!"
            $ hima_diagnosis_activation = True
            jump hima_glute_bridge_menu_love_repeatable

        "{color=[obediencecolor]}Your core is still unstable.{/color}" if hima_diagnosis_stability and hima_diagnosis_lift:
            # UNLOCKED BY THE STABILITY 'FAILURE'.
            bo "That instability is still the biggest issue. We have to correct it. I'm going to hold you in place again so your body can re-learn what a stable position feels like."
            scene black with dissolve
            "You kneel beside her, and she eyes you warily."
            scene boruto_holding_her_hips_cg with dissolve:
                xalign 0.5 yalign 1
            show boruto_holding_her_hips_cg:
                subpixel True
                easein 3 yalign 0.5
            him "Hold me in place... You mean by putting your hands on my..."
            bot "Okay, here we go. Be respectful, be helpful."
            bo "This is where your hips need to be, [him_name]. Feel that?"
            him "O-okay, I feel it, now get your h-hands off."
            jump hima_glute_guide_hips_love_repeatable

        "{color=[obediencecolor]}????{/color}" if not hima_diagnosis_stability or not hima_diagnosis_lift:
            "If I keep explaining what she's doing wrong, maybe she'll be more open to me helping physically..."
            jump hima_glute_bridge_menu_love_repeatable

        "{color=[lovecolor]}You're still not creating the necessary mind-muscle connection.{/color}" if hima_diagnosis_activation and hima_diagnosis_lift:
            # UNLOCKED BY THE ACTIVATION 'FAILURE'.
            bo "Your brain still isn't connecting with the right muscle. We need to use tactile prompting again to build that neural pathway."
            him "Tactile... prompting? Are you sure that's a real thing and not just an excuse?"
            bo "It's basic kinesiology. We've been over this. Do you want to fix the problem or not?"
            him "F-fine! But don't you dare 'slip' this time!"
            bot "She agreed! Okay, just make it quick and clinical. No accidents."
            jump hima_glute_tactile_feedback_love_repeatable

        "{color=[lovecolor]}????{/color}" if not hima_diagnosis_activation or not hima_diagnosis_lift:
            "If I keep explaining what she's doing wrong, maybe she'll be more open to me helping physically..."
            jump hima_glute_bridge_menu_love_repeatable

        "Not too bad, let's move on.":
            bo "We'll come back to this. Your entire posterior chain could use some work, but we'll get there."
            jump hima_training_menu_love_repeatable

    # BRANCH 1: Manual Stabilization (The "Safer" Control Path)
    label hima_glute_guide_hips_love_repeatable:
        scene black with dissolve
        bo "You're still not quite getting it."
        "You kneel and place your hands firmly on her hip bones, supporting her."
        scene boruto_holding_her_cg with dissolve:
            xalign 0.5 yalign 1
        show boruto_holding_her_cg:
            subpixel True
            easein 3 yalign 0.5
        him "Y-your hands are so warm..."
        bo "Focus. Now push up. Feel how I'm keeping you level? This is the stability we're aiming for. Memorize this feeling."
        himt "He's so close... My hips do feel more stable, but it's so hard to concentrate on that when he's touching me."
        bot "Her form is much better like this. This is working."
        call changeObedience("Himawari", 1, "hima_train_glute1", statlevel = 2, max_times=1) from _call_changeObedience_158
        
        menu hima_glute_hip_guidance_menu_love_repeatable:
            bo "Don't break form. Keep the tension in your glutes."

            "{color=[lovecolor]}Good. Hold it there.{/color}":
                call checkLove(11, "hima_glute_hip_guidance_menu_love_repeatable", "Himawari") from _call_checkLove_19
                bo "Perfect. Hold that position. Feel the burn?"
                him "I-I can't hold it much longer, [bo_name], it's really hard!"
                "As she says that, her hips start to wobble again."
                scene black with dissolve
                bot "She's losing it! I have to stabilize her!"
                scene boruto_holding_her_cg_v2 with dissolve:
                    xalign 0.5 yalign 1
                show boruto_holding_her_cg_v2:
                    subpixel True
                    easein 3 yalign 0.5
                "To stop her from falling, your hands slip from her hips to brace her, ending up squarely on her glutes, just like last time."
                bo "Whoa there, [him_rel]! I've got you! Don't you give up on me now!"
                him "Y-you're touching my b-butt! Again!"
                bo "Just stabilizing you! Don't drop until I say so. You got this!"
                bot "Oh god my hands are on her butt again okay just pretend this is normal pretend this is normal!"
                call changeLove(character="himawari",amount=1, fromwhere="hima_glute_hip_guidance_menu_dialogue", max_times=1) from _call_changeLove_60
                "She holds the position, red with embarrassment, but doesn't try to push you away this time."
                show screen parallax1280("boruto_holding_her_cg_v3", initial_ypos=0.5) with dissolve
                call showscrollingimage from _call_showscrollingimage_264
                him "[bo_name_stutter], your hands..."
                bo "What's wrong? You're losing tension. Focus! I'm just making sure you're balanced."
                "She freezes, her eyes wide with embarrassment. But she holds the pose."
                himt "Is he doing this on purpose...? No... he's just helping. It's just training. So why is my whole body on fire?"
                bot "She's so flustered. I should probably move my hands... but her form is absolutely perfect right now!"
                call hidescrollingimage2("Click twice to continue.") from _call_hidescrollingimage2_138
                jump hima_glute_hip_guidance_menu_love_repeatable

            "Alright, that's enough stabilization.":
                bo "Better. You're starting to understand the movement. Let's move on."
                jump hima_glute_bridge_menu_love_repeatable


    # BRANCH 2: Tactile Feedback (The Accidental "Technical" Path)
    label hima_glute_tactile_feedback_love_repeatable:
        menu hima_glute_feedback_options_love_repeatable:
            "Use your fingers to 'prompt' the muscle.":
                bo "Okay, I'm going to reposition to give you more support. Don't freak out."
                scene black with dissolve
                him "O-okay... Just be careful this time."
                "You try to find a better grip, but in the process..."
                scene boruto_grope_her_cg_love with dissolve:
                    xalign 0.5 yalign 1
                show boruto_grope_her_cg_love:
                    subpixel True
                    easein 3 yalign 0.5
                $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.1)
                bot "Oh damn it not again! How does this keep happening!?"
                him "[bo_name_stutter]! SERIOUSLY!?" with vpunch
                show screen parallax1280("boruto_grope_her_cg_love", initial_ypos=0.5) with dissolve
                call showscrollingimage from _call_showscrollingimage_265
                scene black
                bo "I'M SO SORRY! MY HAND SLIPPED! AGAIN! I SWEAR!"
                him "Your hands are on my butt! AGAIN! Are you doing this on purpose, you perv!?"
                bo "N-No! I saw you start to wobble and I tried to catch you and my hands just-"
                him "J-just let go! Fine! It was... another accident, right?"
                bo "O-of course!! I would never do that to my own [him_rel]!"
                call hidescrollingimage2 from _call_hidescrollingimage2_139
                $ hima_glute_poked_for_real = True
                $ hima_glute_spanked = True
                #Fail state
                scene gymhima_buruma_sweaty_cg_love with dissolve:
                    xalign 0.5 yalign 1
                show gymhima_buruma_sweaty_cg_love:
                    subpixel True
                    easein 3 yalign 0.5
                him "I think that's enough coaching for today. I'm feeling a little... awkward."
                bo "I'm so s-"
                him "Just... try to be less clumsy next time, okay? If there is a next time."
                bo "O-okay!"
                scene black with dissolve
                bot "She said 'if there is a next time'... That's better than 'never again'! I still have a chance!"
                jump action_taken

label hima_training_posture_love_repeatable:
    bo "Alright, time for the advanced one. Posture correction. Ready to try the quadrupedal articulation again?"
    him "You mean the one where I have to get on all fours? Ugh, fine. Let's just get it over with."
    bo "It's not about strength, it's about control. You know the position. Hands under shoulders, knees under hips."
    him "Yeah, yeah, the plank position. I remember. Just... try not to fall on me this time." with vpunch
    
    menu hima_posture_initial_sell_love_repeatable:
        him "On... all fours!? What kind of exercise is that!?"

        "It's a foundational athletic stance.":
            bo "Y-you're taking this the wrong way!"
            bo "It's a foundational athletic stance, [him_name], we've been over this!! It's used in everything from yoga to physical therapy. If it's too 'advanced' for you, we can stop and try again in a few months when you're more confident."
            bo "What do you say?"
            him "F-fine! I can do it once more..! It's not a big deal."
            scene black with dissolve
            call changeObedience("Himawari", 1, "hima_posture_comply_kinesiology", statlevel=2, max_times=1) from _call_changeObedience_159

        "Big [him_rel_to_bo] knows best, trust me.":
            bo "Y-you're taking this the wrong way!"
            bo "It's the position for the exercise, we've discussed this already. Are you going to trust your coach, or are you going to waste more of our time?"
            him "Tch... You don't have to be such a jerk about it."
            "Grudgingly, she gets into position once again just to get it over with."
            scene black with dissolve
            call changeDominance(1, max_times=1, fromwhere="hima_posture_initial_sell_love_repeatable") from _call_changeDominance_127

    scene himawari_plank_cg with dissolve:
        xalign 0.5 yalign 1.0
    show himawari_plank_cg:
        subpixel True
        easein 3 yalign 0.7
    bot "Wow. Okay. It's still... quite a view. Be a good coach. Don't be a creep."
    bot "I need to get closer to check her form properly."
    bo "Your butt is still a bit too high. It's not engaging your core properly."
    him "Are you looking at my ass again?!"
    bo "I'm looking at your FORM. And your neck is too high."
    him "Well, show me what's right instead of just telling me what's wrong!"
    bo "Sure, but it's easier to show you than describe it. Is that okay?"
    him "F-fine..."
    scene black with dissolve
    "You move behind her, kneeling down to inspect her form, and she tenses up."
    $ renpy.sound.play("/audio/soun_fx/fast_blink.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    scene himawari_plank_surprised_cg with flash:
        xalign 0.5 yalign 1.0
    show himawari_plank_surprised_cg:
        subpixel True
        easein 3 yalign 0.5
    pause(1.0)
    him "You're... really close! Again!"
    himt "I can feel his breath on my legs. It's just as awkward as I remember."
    bo "Like I said, I'm a professional. A professional needs to examine the form from all angles."
    bo "From back here, it's even more obvious what the problem is."
    bo "Just hold still. I'm placing my hand on your lower back to guide you."
    scene black with dissolve
    bo "Take this seriously. You can do this."
    scene himawari_plank_helped_cg with dissolve:
        xalign 0.5 yalign 0.0
    show himawari_plank_helped_cg:
        subpixel True
        easein 3 yalign 0.5
    "You gently place one hand on her back. She's struggling to hold the pose."
    show screen parallax1280("himawari_plank_helped_cg", initial_ypos=0.5) with dissolve
    call showscrollingimage from _call_showscrollingimage_266
    bo "See? Your muscles are still fighting the position because your core isn't properly engaged."
    him "I-I'm trying my best! It's hard!"
    him "It's really hard to hold this for more than a few seconds, you know!"
    bo "I know. But I think you can hold it a few seconds longer than last time. Show me your progress."
    him "I'm gonna fall any second now!!" 
    scene black
    call hidescrollingimage2("Click twice to offer more assistance.") from _call_hidescrollingimage2_140
    scene black with dissolve
    bo "It's okay, I've got you."
    scene himawari_plank_helped_cgv2 with dissolve:
        xalign 0.5 yalign 0.0
    show himawari_plank_helped_cgv2:
        subpixel True
        easein 3 yalign 0.5      
    bo "I'm just taking a little of the weight. Now you can focus on form without worrying about collapsing."
    bot "Damn it, my knees are cramping up again..."
    bot "What if I just shift my weight a little to th-"
    scene black with vpunch
    bo "W-WOOAH NOT AGAIN!" with vpunch
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
    him "ARE YOU SERIOUS!? AGAIN!?" with hpunch
    him "GET YOUR FACE OFF MY ASS, YOU CLUMSY IDIOT!" with vpunch
    show screen parallax1280("himawari_plan_fall_angry") with dissolve
    call showscrollingimage from _call_showscrollingimage_267
    bo "MMVMFMFMVMVMV!!!!" with vpunch
    show screen parallax1280("himawari_plan_fall_angry_2") with dissolve
    scene black
    bo "*Gasping for air*"
    bo "I-"
    bo "MY KNEE GAVE OUT! I'M SO SORRY, IT HAPPENED AGAIN!"
    bot "God damn it she'll never believe me! How does this keep happening!?"
    him "You are the clumsiest person I have ever met! Are you doing this on purpose!?"
    bo "I'm really sorry, it's just that my legs were getting tired and-"
    him "And is that the reason why your head is STILL RIGHT ABOVE MY ASS?!" with vpunch
    bot "O-oops."
    him "MOVE!!!" with hpunch
    bo "I'll move right away!"
    call hidescrollingimage2 from _call_hidescrollingimage2_141
    scene black with dissolve
    "You scramble off the ground as she sits up, exhausted and utterly exasperated."
    jump posture_ending_love_repeatable

label posture_ending_love_repeatable:
    scene gymhima_buruma_sweaty_cg_love_annoyed with dissolve:
        xalign 0.5 yalign 1
    show gymhima_buruma_sweaty_cg_love_annoyed:
        subpixel True
        easein 3 yalign 0.5
    bo "Okay, so besides my apparent inability to stay upright during that last exercise, you're making real progress."
    him "...That's a very big 'besides'!"
    bot "She's annoyed, but not furious. That's a definite improvement. Phew!"
    him "You keep saying you care about my safety, and then you keep falling on me! You're unbelievable." with vpunch
    bo "It's not acting, [him_name]! I do care about you. A bad coach would just let you use bad form. I'm trying to look out for you."
    show gymhima_buruma_sweaty_cg_love with dissolve:
        xalign 0.5 yalign 0.5
    show gymhima_buruma_sweaty_cg_love:
        subpixel True
        easein 0.5 yalign 0.3
    bo "You've got amazing potential. With me supporting you, you'll be more than ready for your chunin exams in no time!"
    himt "D-does he really care that much? Even after all this... It seems... genuine!"
    hide gymhima_buruma_sweaty_cg_love
    show gymhima_buruma_sweaty_cg_love_annoyed
    with dissolve
    him "Hmph! I'd be ready with or without your clumsy 'coaching'!" with vpunch
    bot "Of course, she's still too proud to admit I'm helping, but I know I'm getting through to her."
    bo "Remember this feeling [him_name]. This is the feeling of improvement. We'll continue your training soon."
    him "Yeah... whatever. Get out so I can shower."
    scene black with vpunch
    "She shoos you out of the room, clearly exhausted but also a little proud of her progress."
    $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx2", loop=False, relative_volume = 0.9)
    "The door clicks shut behind you."
    jump action_taken

label himawari_training_kicked_out_love_repeatable:
    
    scene himawari_angry_cg with Dissolve(0.2):
        xalign 0.5 yalign 1
    show himawari_angry_cg:
        subpixel True
        easein 0.2 yalign 0.5

    him "I can't believe I was stupid enough to trust you, AGAIN! Get out of my room! NOW!"
    bo "I promise I can expl-"
    him "GET OUT!" with vpunch

    scene black with vpunch
    $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx2", loop=False, relative_volume = 0.9)
    "The door slams shut so hard the frame rattles."
    bot "Good job [bo_name]... Again?! How stupid could I be..."

    jump action_taken