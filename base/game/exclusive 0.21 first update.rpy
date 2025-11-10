label hima_swimsuit_sexy_shots:
    if quest.is_state("2_bohim_3", "in progress"):
        $ notification ("Quest updated")
        $ quest.check("2_bohim_3","completed")
    if hima_swimsuit_shots_taken == 1:
        bo"Okay, you've been doing well so far, but for the shots that really pay the bills? Time to turn up the heat!"
        him"I knew it. Here comes the pervert shit."
        bot"She says that like it's a bad thing. It's the only reason she's here."
        bo"It's what the market dictates. Don't project your insecurities onto a business transaction."
        if quest.is_state("2_bohim_2", "in progress"):
            $ quest.check("2_bohim_2","completed")
            $ notification ("Quest updated")
    if hima_swimsuit_shots_taken == 2:
        bo"You didn't think that was all, right? We've barely just started! You've got so much more to show everyone."
        him"Sh-show everyone..? I thought that only special buyers-"
        bo"You know what I mean, come on, stop stalling and get in position."
        bot"She's barely even complaining at this point! What a good obedient bitch!"
    else:
        pass
    menu hima_swimsuit_sexy_shots_menu:
        "Choose a pose:"
        "On your knees, looking back at me." if not hima_chose_sexy_1:
            $ hima_chose_sexy_1 = True
            bo"Drop to your knees. Hands on the mattress. Look back at the camera."
            him"No. That's... that's a fucking whore's pose. I'm not doing it."
            himt"I feel sick... but my head... the ache is fading a little now that he's giving orders again. What is wrong with me?"
            bot"Dread it, run from it... Sooner or later you'll be doing exactly as I command. All according to plan!"
            bo"It's a pose that conveys a specific, high-value aesthetic. It will pay for [hin_rel]'s expenses for a month. Now, be a good girl and kneel."
            scene all fours_a with dissolve:
                xalign 0.5 yalign 0.95
            show all fours_a:
                subpixel True
                easein 3 yalign 0.2
            him"This... is weird..."
            bo"You're doing great, stop complaining."
            show screen camera1280("all fours_a", 1, 0.0)
            show screen camera_ui("Himawari_swimsuit", False)
            with dissolve
            show screen camera_ui("Himawari_swimsuit")
            $ ui.interact()
            call changeObedience("Himawari", 1, fromwhere="vixen_sexy_knees", max_times=1) from _call_changeObedience_182
            bo"That's the shot. Perfect."
            himt"I can feel his eyes scanning me..."
            him"I swear if I see you staring at me like a creep one more time..."
            bo"Then what?"
            him"You'll find out!"
            jump hima_swimsuit_repeatable_menu
        "Lie on the mattress, ass up." if not hima_chose_sexy_2:
            $ hima_chose_sexy_2 = True
            bo"Lie on the mattress, hips high. Relaxed but bold."
            scene all fours 2_a with dissolve: # variations not used so far: all fours 2_b
                xalign 0.5 yalign 0.95
            show all fours 2_a:
                subpixel True
                easein 3 yalign 0.2
            him"This feels so wrong in this outfit..."
            bot"But it feels so right to me. Show me that ass."
            bo"It's right for the shot. Trust me. You have a natural beauty that people will pay to see."
            show screen camera1280("all fours 2_a", 1, 0.0)
            show screen camera_ui("Himawari_swimsuit", False)
            with dissolve
            show screen camera_ui("Himawari_swimsuit")
            $ ui.interact()
            call increaselust(10) from _call_increaselust_298
            bo"Stunning. That's going to sell."
            him"You bet it will. And it's MY money!"
            bot"I don't know about that, but..."
            him"Did you say something?"
            bo"No, you're hearing voices."
            him"Another dumbass joke and I'm out of here!"
            jump hima_swimsuit_repeatable_menu
        "Lie on the mattress, on your back." if not hima_chose_sexy_3:
            $ hima_chose_sexy_3 = True
            bo"Lie on the mattress, on your back."
            him"And do what..?"
            bo"Just do as I say. Then follow your instinct."
            scene mattress pose 2_a with dissolve:
                xalign 0.5 yalign 0.95
            show mattress pose 2_a:
                subpixel True
                easein 3 yalign 0.2
            him"Something like t-this?"
            bot"Look at how she just instinctively sticks her tits up for me!"
            bot"She's already being subconsciously trained to try to impress me with her... assets!"
            him"[bo_name_stutter]?"
            bo"*clears throat* Sorry I was just trying to set up the shot."
            bo"That's an okay attempt."
            bot"Way more than okay but can't have her thinking that that's all just yet..."
            him"Just okay?! I'm doing my best here! Just get this over with, idiot!"
            show screen camera1280("mattress pose 2_a", 1, 0.0)
            show screen camera_ui("Himawari_swimsuit", False)
            with dissolve
            bo"I said I'm setting up the shot, be patient."
            show screen camera_ui("Himawari_swimsuit")
            $ ui.interact()
            bo"There we go. Not bad."
            bo"But that's not all."
            hide screen camera_ui
            hide screen camera1280
            bo"I forgot to zoom in to the appropriate area."
            him"Z-zoom? I know exactly what you're doing, creep, don't you dare!"
            menu:
                bo"Do you? I'm trying to make money for you. Now be quiet as I adjust my shot."
                "Focus on her feet.":
                    bo"Don't tell me how to do my job if you want to make money."
                    bo"I'm trying to concentrate."
                    bot"Yes... concentrating, on your feet!"
                    scene mattress pose 2_a_lower with dissolve:
                        xalign 0.5 yalign 0.95
                    show mattress pose 2_a_lower:
                        subpixel True
                        easein 3 yalign 0.2
                    bot"Check out those perfect feet..."
                    him"What are you looking at now, pervert?!"
                    bo"Quiet, I'm not done setting the shot up yet. Stay still."
                    show screen camera1280("mattress pose 2_a_lower", 1, 0.0)
                    show screen camera_ui("Himawari_swimsuit", False)
                    with dissolve
                    show screen camera_ui("Himawari_swimsuit")
                    $ ui.interact()
                    bo"See? Wasn't that hard."
                    him"It is when I have no idea what you're staring at!"
                    bo"I was just capturing your expressive pretty face, that's all!"
                    him"I can see where the camera is facing towards, idiot, and it was definitely not on my face."
                    bo"..."
                    jump hima_swimsuit_repeatable_menu
                "Focus on her boobs.":
                    bo"Don't tell me how to do my job if you want to make money."
                    bo"I'm trying to concentrate."
                    bot"Yes... concentrating, on those titties of yours!"
                    scene mattress pose 2_a_upper with dissolve:
                        xalign 0.5 yalign 0.95
                    show mattress pose 2_a_upper:
                        subpixel True
                        easein 3 yalign 0.2
                    bot"That whole bikini talk was a genius idea, she's practically naked... Money well spent!"
                    him"Are you gonna take the picture or not?!"
                    bo"I can see you are tense. Relax first."
                    him"How can I relax when you're zooming in on my private parts!"
                    bo"[him_name], trust the process."
                    show screen camera1280("mattress pose 2_a_upper", 1, 0.0)
                    show screen camera_ui("Himawari_swimsuit", False)
                    with dissolve
                    show screen camera_ui("Himawari_swimsuit")
                    $ ui.interact()
                    bo"See? Wasn't that hard."
                    him"It is when I have no idea what you're staring at!"
                    bo"I was just capturing your expressive pretty face, that's all!"
                    him"Sure you were... perv!"
                    jump hima_swimsuit_repeatable_menu
        # Added mattress pose 2_a, lower, upper

        "{color=[hatredcolor]}???{/color}" if (hatred.value < 30 and hatred.level ==1):
            call checkHatred(statvalue=30, jumpvalue="hima_swimsuit_sexy_shots") from _call_checkHatred_52
            bot"I probably need to ease her into it a bit more first before trying this... I'll keep pushing!"
            jump hima_swimsuit_sexy_shots_menu
        "{color=[hatredcolor]}Now lie on your back, spread wide open, lift one leg up.{/color}" if not hima_chose_sexy_4 and (hatred.value >= 30 or hatred.level>1):
            call checkHatred(30) from _call_checkHatred_53
            $ hima_chose_sexy_4 = True
            bo"Final shot. The one that pays for everything. Lie on your back. Open your legs for the camera. Wide."
            him"I... I can't. Please, [bo_name], don't make me do this."
            bot"Begging. Fucking beautiful. Her pleading is the sweetest sound. Her resistance is finally wavering... This is the moment where she really begins to obey!"
            bo"This isn't me making you do anything. This is you finally contributing to this household. Besides, what's the big deal? It's just a damn pose. Get on with it..."
            him"I hate you... I hate you so much..."
            call changeHatred(1, max_times=1, fromwhere="swimsuit_sexyshothatred") from _call_changeHatred_230
            scene mattress pose_a:
                xalign 0.5 yalign 0.95
            show mattress pose_a:
                subpixel True
                easein 3 yalign 0.2
            "Her voice is barely heard as she hesitantly complies, trembling with shame. Her eyes are filled with the anger and frustration of doing what you command her to do."
            bot"That tear... that's my trophy. The proof of my victory."
            bo"Look at the camera, [him_name]. Let them see your face."
            show screen camera1280("mattress pose_a", 1, 0.0)
            show screen camera_ui("Himawari_swimsuit", False)
            with dissolve
            show screen camera_ui("Himawari_swimsuit")
            $ ui.interact()
            bo"That's a wrap. You did well."
            him"Y-you... You disgusting pig!"
            him"I'm your [him_rel]!"
            bo"Calm down, all I said is you did a great job, as a model! You have a bright career ahead if you keep this up!"
            him"Keep this up? You made me pose like a whore! And for what?"
            bo"Soon, your payment will be due."
            jump hima_swimsuit_repeatable_menu
            # Other, not used so far: rear shot 2_a, rear shot 2_b, rear shot 3_a, rear shot 3_b, rear shot_a, rear shot_b, v21_hima_model_start1_1behind
        "Knees on the floor, hands on the bed." if not hima_chose_sexy_5:
            $ hima_chose_sexy_5 = True
            bo"Knees on the floor, hands on the bed. Look back towards me."
            him"Why do you keep picking poses that make me look like a whore?!"
            bot"Because you are one."
            bo"It's not how it looks, trust me. This will sell quite highly. Now get on your knees!"
            scene mattress pose 3_a with dissolve:
                xalign 0.5 yalign 0.95
            show mattress pose 3_a:
                subpixel True
                easein 3 yalign 0.2
            him"This feels so... Wrong! Do all models do stuff like that?"
            bo"You bet they do. And I spent a lot more time with them than you. Remember Yoru?"
            bo"She could easily pull this off, and better!"
            him"I-I'm trying my best!"
            him"If only you would stop creeping!"
            show screen camera1280("mattress pose 3_a", 1, 0.0)
            show screen camera_ui("Himawari_swimsuit", False)
            with dissolve
            bo"It's all in your head. I'm just setting up the shot, don't be so self-centered."
            show screen camera_ui("Himawari_swimsuit")
            $ ui.interact()
            bo"There we go, see?"
            bo"It came out perfect!"
            him"C-can I move now?"
            bo"Not so fast!"
            bo"Just when we get the perfect pose you want to move? Let me make more money for you!"
            hide screen camera_ui
            hide screen camera1280
            bo"I need to adjust my angle slightly, stay right there."
            scene mattress pose 3_b with dissolve:
                xalign 0.5 yalign 0.95
            show mattress pose 3_b:
                subpixel True
                easein 3 yalign 0.2
            bot"Here we are... What a perfect little ass, complimented by her amazing feet."
            him"W-where did you go?!"
            bo"Stay still, I'm trying to get a better angle of your ass-assets!"
            show screen camera1280("mattress pose 3_b", 1, 0.0)
            show screen camera_ui("Himawari_swimsuit", False)
            with dissolve
            bo"And..."
            show screen camera_ui("Himawari_swimsuit")
            $ ui.interact()
            bo"Done!"
            him"Finally... You weren't just staring at my ass, were you?!"
            bo"[him_name], come on. Please, let me do my job and quit your whining."
            jump hima_swimsuit_repeatable_menu

        "Lie on the mattress, on your side." if not hima_chose_sexy_6:
            $ hima_chose_sexy_6 = True
            bo"Lie on the mattress, on your side."
            him"Okay, but you shouldn't st-"
            bo"Do as you're told, or we'll be here all day."
            him"F-fine!"
            scene mattress pose 4_a with dissolve:
                xalign 0.5 yalign 0.95
            show mattress pose 4_a:
                subpixel True
                easein 3 yalign 0.2
            him"L-like this?"
            bo"Finally, you're getting the hang of it!"
            bot"I love how she just started posing for me with barely any extra direction..."
            bot"She's finally starting to be subconsciously trained, little by little!"
            bo"What a great ass you've got there, little [him_rel]!"
            bot"Oops, I shouldn't have said that out loud."
            him"SO ALL THIS JUST TO STARE AT MY ASS, JUST LIKE I THOUGHT!" with vpunch
            bo"Shhhh, let me concentrate, this is a good one."
            show screen camera1280("mattress pose 4_a", 1, 0.0)
            show screen camera_ui("Himawari_swimsuit", False)
            with dissolve
            show screen camera_ui("Himawari_swimsuit")
            $ ui.interact()
            bo"There we go. Not bad. But Yoruichi would still have done better."
            hide screen camera_ui
            hide screen camera1280
            "Out of embarrassment, she quickly tries to cover her ass with her hand."
            scene mattress pose 5_a with dissolve:
                xalign 0.5 yalign 0.95
            show mattress pose 5_a:
                subpixel True
                easein 3 yalign 0.2
            him"Creep! This was NOT what I agreed to!"
            bo"Shhh, stay right there! This one is even better!"
            bot"She looks so vulnerable... And she doesn't even realize that she kinda looks like she wants to masturbate!"
            him"Let's move to a different one already!"
            show screen camera1280("mattress pose 5_a", 1, 0.0)
            show screen camera_ui("Himawari_swimsuit", False)
            with dissolve
            bo"I'll say when we're moving on. Stay right there."
            show screen camera_ui("Himawari_swimsuit")
            $ ui.interact()
            bo"There we go. Amazing."
            him"Finally!"
            him"Let's do something else where you're not sticking that camera in my privates maybe?!"
            bo"It's what sells, [him_name]."
            bo"I told you. You want to get paid? Trust the process."
            him"Ughhh!"
            jump hima_swimsuit_repeatable_menu

        "Lie on your stomach with your feet up" if not hima_chose_sexy_7:
            $ hima_chose_sexy_7 = True
            bo"Lie on your stomach, feet up, like you are just relaxing after a long day."
            him"That should be easy, because I'm feeling like it's a long day already."
            bo"Do you ever stop complaining?"
            scene mattress pose 6_a with dissolve:
                xalign 0.5 yalign 0.95
            show mattress pose 6_a:
                subpixel True
                easein 3 yalign 0.2
            him"I'll stop complaining when you stop telling me what to do and give me my money."
            bo"You look like you are bored! You expect this to sell?"
            show screen camera1280("mattress pose 6_a", 1, 0.0)
            show screen camera_ui("Himawari_swimsuit", False)
            with dissolve
            bot"Well, that old fart Dio will still pay me for it anyway, so might as well snap one."
            show screen camera_ui("Himawari_swimsuit")
            $ ui.interact()
            bo"I suggest you try to at least look like you're enjoying it, if you want to make any money."
            hide screen camera_ui
            hide screen camera1280
            him"I'm trying, idiot, you're not very specific with your instructions!"
            show screen camera1280("mattress pose 6_c", 1, 0.0)
            show screen camera_ui("Himawari_swimsuit", False)
            with dissolve
            bo"Let's see..."
            show screen camera_ui("Himawari_swimsuit")
            $ ui.interact()
            bo"That's a bit better."
            bo"But I want you to actually try looking at the camera for once."
            bo"You know, that's what separates you from Yoruichi."
            bo"You do it for the money. She makes it... personal."
            him"Shut up, idiot! Of course I do it for the money. You're my [him_rel_to_bo]. What the hell are you implying with 'personal'?"
            bo"Just... try looking at the camera. Don't overthink it."
            show screen camera1280("mattress pose 6_b", 1, 0.0)
            show screen camera_ui("Himawari_swimsuit", False)
            with dissolve
            bo"That's it, stay there."
            show screen camera_ui("Himawari_swimsuit")
            $ ui.interact()
            bo"See? Now that looks much better."
            him"S-sure..."
            jump hima_swimsuit_repeatable_menu

label hima_swimsuit_sexy_shots_love:
    if quest.is_state("2_bohim_3", "in progress"):
        $ notification ("Quest updated")
        $ quest.check("2_bohim_3","completed")
    if hima_swimsuit_shots_taken == 1:
        bo"Okay, you've been doing so well. For the shots that really show your artistic range, we need to try something a little bolder."
        him"I knew it. Here comes the embarrassing stuff."
        bot"She says that, but she's blushing, not angry. I think she's ready to trust me with this."
        bo"It's about pushing boundaries, artistically. Trust me, it's a collaboration."
        if quest.is_state("2_bohim_2", "in progress"):
            $ quest.check("2_bohim_2","completed")
            $ notification ("Quest updated")
    if hima_swimsuit_shots_taken == 2:
        bo"Ready for the next one? We're creating something really special here. You're showing so much of your true self."
        him"M-my true self..? I thought we were just taking pictures for money-"
        bo"It's more than that. Now, let's get into position."
        bot"She's barely even protesting now. We're really in sync. This is amazing."
    else:
        pass
    menu hima_swimsuit_sexy_shots_menu_love:
        "Choose a pose:"
        "On your knees, looking back at me." if not hima_chose_sexy_1:
            $ hima_chose_sexy_1 = True
            bo"Let's try this. On your knees, hands on the mattress. Look back at the camera."
            him"No. That's... that's a really suggestive pose. I don't want to do that."
            himt"I feel nervous... but my head... the fuzziness is gone now that he's directing me again. What is happening to me?"
            bot"This is a big step for her. I have to be gentle, to show her it's about art, not exploitation."
            bo"It's a pose that conveys a powerful, alluring aesthetic. It will help [hin_rel] for a month. Please, be brave and trust me."
            scene all fours_a with dissolve:
                xalign 0.5 yalign 0.95
            show all fours_a:
                subpixel True
                easein 3 yalign 0.2
            him"This... is strange..."
            bo"You're doing great, you look incredible."
            show screen camera1280("all fours_a", 1, 0.0)
            show screen camera_ui("Himawari_swimsuit", False)
            with dissolve
            show screen camera_ui("Himawari_swimsuit")
            $ ui.interact()
            call changeObedience("Himawari", amount=1, fromwhere="vixen_sexy_knees_love", max_times=1) from _call_changeObedience_183
            bo"That's the shot. Perfect."
            himt"I can feel his eyes on me... but it doesn't feel... bad?"
            him"Just... take the picture and don't say anything embarrassing."
            bo"Wouldn't dream of it."
            him"You'd better not!"
            jump hima_swimsuit_repeatable_menu_love
        "Lie on the mattress, ass up." if not hima_chose_sexy_2:
            $ hima_chose_sexy_2 = True
            bo"Lie on the mattress, hips high. Relaxed but elegant."
            scene all fours 2_a with dissolve: # variations not used so far: all fours 2_b
                xalign 0.5 yalign 0.95
            show all fours 2_a:
                subpixel True
                easein 3 yalign 0.2
            him"This feels so vulnerable in this outfit..."
            bot"And yet she looks so powerful. Show me that confidence."
            bo"It's perfect for the shot. Trust me. You have a natural grace that people will admire."
            show screen camera1280("all fours 2_a", 1, 0.0)
            show screen camera_ui("Himawari_swimsuit", False)
            with dissolve
            show screen camera_ui("Himawari_swimsuit")
            $ ui.interact()
            call increaselust(10) from _call_increaselust_299
            bo"Stunning. That's going to be a favorite."
            him"You bet it will. And it's for our family!"
            bot"And I get to be the one to see it first..."
            him"Did you say something?"
            bo"No, just admiring your work."
            him"H-hmph! Well, keep admiring and taking pictures!"
            jump hima_swimsuit_repeatable_menu_love
        "Lie on the mattress, on your back." if not hima_chose_sexy_3:
            $ hima_chose_sexy_3 = True
            bo"Lie on the mattress, on your back."
            him"And do what..?"
            bo"Just relax. Find a pose that feels natural."
            scene mattress pose 2_a with dissolve:
                xalign 0.5 yalign 0.95
            show mattress pose 2_a:
                subpixel True
                easein 3 yalign 0.2
            him"Something like t-this?"
            bot"Wow, she instinctively arched her back... she's a complete natural at this."
            bot"She's learning subconsciously how to present herself in the most beautiful way. It's incredible."
            him"[bo_name_stutter]?"
            bo"*clears throat* Sorry, I was just framing the shot in my head."
            bo"That's a really good start."
            bot"It's way more than good but I don't want to make her more embarrassed than she already is."
            him"Just good?! I'm trying my best here! Just take the picture, dummy!"
            show screen camera1280("mattress pose 2_a", 1, 0.0)
            show screen camera_ui("Himawari_swimsuit", False)
            with dissolve
            bo"I'm setting up the shot, be patient."
            show screen camera_ui("Himawari_swimsuit")
            $ ui.interact()
            bo"There we go. Really nice."
            bo"But that's not all."
            hide screen camera_ui
            hide screen camera1280
            bo"I want to zoom in to capture the details."
            him"Z-zoom? I know what you're thinking, perv, don't you dare!"
            menu:
                bo"What am I thinking? I'm trying to make art here. Just trust me for a moment."
                "Focus on her feet.":
                    bo"You have to trust your director if you want to create the best art."
                    bo"I'm trying to concentrate."
                    bot"Yes... concentrating, on her elegant feet!"
                    scene mattress pose 2_a_lower with dissolve:
                        xalign 0.5 yalign 0.95
                    show mattress pose 2_a_lower:
                        subpixel True
                        easein 3 yalign 0.2
                    bot"They're surprisingly delicate..."
                    him"What are you looking at now, weirdo?!"
                    bo"Quiet, I'm setting up the shot. Stay still."
                    show screen camera1280("mattress pose 2_a_lower", 1, 0.0)
                    show screen camera_ui("Himawari_swimsuit", False)
                    with dissolve
                    show screen camera_ui("Himawari_swimsuit")
                    $ ui.interact()
                    bo"See? It wasn't so bad."
                    him"It is when I have no idea what part of me you're focusing on!"
                    bo"I was just capturing your expressive pretty face, that's all!"
                    him"The camera wasn't pointing at my face, dummy, I can see it!"
                    bo"..."
                    jump hima_swimsuit_repeatable_menu_love
                "Focus on her boobs.":
                    bo"You have to trust your director if you want to create the best art."
                    bo"I'm trying to concentrate."
                    bot"Yes... concentrating, on the beautiful curve of her chest."
                    scene mattress pose 2_a_upper with dissolve:
                        xalign 0.5 yalign 0.95
                    show mattress pose 2_a_upper:
                        subpixel True
                        easein 3 yalign 0.2
                    bot"This bikini was a good idea... it fits her so well. Money well spent."
                    him"Are you gonna take the picture or what?!"
                    bo"I can see you are tense. Relax first."
                    him"How can I relax when you're zooming in like that?!"
                    bo"[him_name], trust the process."
                    show screen camera1280("mattress pose 2_a_upper", 1, 0.0)
                    show screen camera_ui("Himawari_swimsuit", False)
                    with dissolve
                    show screen camera_ui("Himawari_swimsuit")
                    $ ui.interact()
                    bo"See? It wasn't so bad."
                    him"It is when I have no idea what part of me you're focusing on!"
                    bo"I was just capturing your expressive pretty face, that's all!"
                    him"Sure you were... perv!"
                    jump hima_swimsuit_repeatable_menu_love
        
        "{color=[hatredcolor]}???{/color}" if (hatred.value < 30 and hatred.level ==1):
            call checkHatred(statvalue=30, jumpvalue="hima_swimsuit_sexy_shots_love") from _call_checkHatred_54
            bot"I probably need to ease her into it a bit more first before trying this... I'll keep pushing!"
            jump hima_swimsuit_sexy_shots_menu_love
        "{color=[hatredcolor]}Now lie on your back, spread wide open, lift one leg up.{/color}" if not hima_chose_sexy_4 and (hatred.value >= 30 or hatred.level > 1):
            call checkHatred(30) from _call_checkHatred_55
            $ hima_chose_sexy_4 = True
            bo"Final shot. The one that pays for everything. Lie on your back. Open your legs for the camera. Wide."
            him"I... I can't. Please, [bo_name], don't make me do this."
            bot"Begging. Fucking beautiful. Her pleading is the sweetest sound. Her resistance is finally wavering... This is the moment where she really begins to obey!"
            bo"This isn't me making you do anything. This is you finally contributing to this household. Besides, what's the big deal? It's just a damn pose. Get on with it..."
            him"I hate you... I hate you so much..."
            call changeHatred(1, max_times=1, fromwhere="swimsuit_sexyshotimpulse_love") from _call_changeHatred_231
            scene mattress pose_a:
                xalign 0.5 yalign 0.95
            show mattress pose_a:
                subpixel True
                easein 3 yalign 0.2
            "Her voice is barely heard as she hesitantly complies, trembling with shame. Her eyes are filled with the anger and frustration of doing what you command her to do."
            bot"That tear... that's my trophy. The proof of my victory."
            bo"Look at the camera, [him_name]. Let them see your face."
            show screen camera1280("mattress pose_a", 1, 0.0)
            show screen camera_ui("Himawari_swimsuit", False)
            with dissolve
            show screen camera_ui("Himawari_swimsuit")
            $ ui.interact()
            bo"That's a wrap. You did well."
            him"Y-you... You disgusting pig!"
            him"I'm your [him_rel]!"
            bo"Calm down, all I said is you did a great job, as a model! You have a bright career ahead if you keep this up!"
            him"Keep this up? You made me pose like a whore! And for what?"
            bo"Soon, your payment will be due."
            jump hima_swimsuit_repeatable_menu_love
        "Knees on the floor, hands on the bed." if not hima_chose_sexy_5:
            $ hima_chose_sexy_5 = True
            bo"Knees on the floor, hands on the bed. Look back towards me."
            him"Why do all these poses feel so embarrassing?!"
            bot"Because she's not used to being so open. But she looks beautiful."
            bo"It's about creating dynamic lines. It's very high-fashion. You can do this!"
            scene mattress pose 3_a with dissolve:
                xalign 0.5 yalign 0.95
            show mattress pose 3_a:
                subpixel True
                easein 3 yalign 0.2
            him"This feels so... exposed! Do all models do stuff like this?"
            bo"The best ones do. And I've seen how hard you work. Remember Yoru?"
            bo"She could pull this off, and I know you can too."
            him"I-I'm trying my best!"
            him"If you'd just stop staring!"
            show screen camera1280("mattress pose 3_a", 1, 0.0)
            show screen camera_ui("Himawari_swimsuit", False)
            with dissolve
            bo"I'm looking through the lens. Just setting up the shot, don't worry."
            show screen camera_ui("Himawari_swimsuit")
            $ ui.interact()
            bo"There we go, see?"
            bo"It came out perfect!"
            him"C-can I move now?"
            bo"Not so fast!"
            bo"The light is perfect, and so is the pose. Let me get one more for you!"
            hide screen camera_ui
            hide screen camera1280
            bo"I need to adjust my angle slightly, stay right there."
            scene mattress pose 3_b with dissolve:
                xalign 0.5 yalign 0.95
            show mattress pose 3_b:
                subpixel True
                easein 3 yalign 0.2
            bot"From here... the curve of her back and her delicate feet... it's a perfect composition."
            him"W-where did you go?!"
            bo"Stay still, I'm trying to get a better angle on your... posture!"
            show screen camera1280("mattress pose 3_b", 1, 0.0)
            show screen camera_ui("Himawari_swimsuit", False)
            with dissolve
            bo"And..."
            show screen camera_ui("Himawari_swimsuit")
            $ ui.interact()
            bo"Done!"
            him"Finally... You weren't just staring at my butt, were you?!"
            bo"[him_name], come on. Please, trust me. We're a team."
            jump hima_swimsuit_repeatable_menu_love

        "Lie on the mattress, on your side." if not hima_chose_sexy_6:
            $ hima_chose_sexy_6 = True
            bo"Lie on the mattress, on your side."
            him"Okay, but don't say anything weird."
            bo"You have my word. Just get comfortable."
            him"F-fine!"
            scene mattress pose 4_a with dissolve:
                xalign 0.5 yalign 0.95
            show mattress pose 4_a:
                subpixel True
                easein 3 yalign 0.2
            him"L-like this?"
            bo"Finally, you're anticipating what I need!"
            bot"It's like we can read each other's minds... she knows what looks good."
            bot"She's finally starting to see herself as the beautiful person she is."
            bo"What a graceful pose, little [him_rel]!"
            bot"Oops, maybe that was a bit too much."
            him"HEY! I TOLD YOU NOT TO SAY ANYTHING WEIRD ABOUT MY BODY!" with vpunch
            bo"Shhh, you'll ruin the shot. I'm sorry, it just slipped out."
            show screen camera1280("mattress pose 4_a", 1, 0.0)
            show screen camera_ui("Himawari_swimsuit", False)
            with dissolve
            show screen camera_ui("Himawari_swimsuit")
            $ ui.interact()
            bo"There we go. Really good. Though, Yoruichi taught me a variation on this one."
            hide screen camera_ui
            hide screen camera1280
            "Blushing, she quickly tries to cover her rear with her hand."
            scene mattress pose 5_a with dissolve:
                xalign 0.5 yalign 0.95
            show mattress pose 5_a:
                subpixel True
                easein 3 yalign 0.2
            him"Dummy! This was NOT part of the deal!"
            bo"Shhh, stay right there! That pose is even better!"
            bot"She looks so shy... and she doesn't even realize how that pose creates a beautiful S-curve."
            him"Let's move to a different one already!"
            show screen camera1280("mattress pose 5_a", 1, 0.0)
            show screen camera_ui("Himawari_swimsuit", False)
            with dissolve
            bo"I'll say when we're moving on. Just hold that for a second longer."
            show screen camera_ui("Himawari_swimsuit")
            $ ui.interact()
            bo"There we go. Amazing."
            him"Finally!"
            him"Can we do something else where you're not focusing the camera on my private parts, maybe?!"
            bo"It's art, [him_name]."
            bo"I told you. You want to get paid? Trust the process."
            him"Ughhh!"
            jump hima_swimsuit_repeatable_menu_love

        "Lie on your stomach with your feet up" if not hima_chose_sexy_7:
            $ hima_chose_sexy_7 = True
            bo"Lie on your stomach, feet up, like you are just relaxing after a long day."
            him"That should be easy, because I am exhausted."
            bo"Does that mean you're ever going to admit you're having fun?"
            scene mattress pose 6_a with dissolve:
                xalign 0.5 yalign 0.95
            show mattress pose 6_a:
                subpixel True
                easein 3 yalign 0.2
            him"I'll admit I'm having fun when you admit you're an annoying director and give me my money."
            bo"You look a little tired! Do you expect that to sell?"
            show screen camera1280("mattress pose 6_a", 1, 0.0)
            show screen camera_ui("Himawari_swimsuit", False)
            with dissolve
            bot"Even her tired look is cute. I'll take one anyway."
            show screen camera_ui("Himawari_swimsuit")
            $ ui.interact()
            bo"I suggest you try to at least look like you're enjoying yourself, if you want this to be a success."
            hide screen camera_ui
            hide screen camera1280
            him"I'm trying, dummy, but you're a terrible director!"
            show screen camera1280("mattress pose 6_c", 1, 0.0)
            show screen camera_ui("Himawari_swimsuit", False)
            with dissolve
            bo"Let's see..."
            show screen camera_ui("Himawari_swimsuit")
            $ ui.interact()
            bo"That's a bit better."
            bo"But what if you tried looking at the camera?"
            bo"You know, that's what separates you from Yoruichi."
            bo"You do it for the money. She makes it... a performance."
            him"Shut up, idiot! Of course I do it for the money. You're my [him_rel_to_bo]. What the hell are you implying with 'performance'?"
            bo"Just... try looking at me. Through the camera. Don't overthink it."
            show screen camera1280("mattress pose 6_b", 1, 0.0)
            show screen camera_ui("Himawari_swimsuit", False)
            with dissolve
            bo"That's it, stay there."
            show screen camera_ui("Himawari_swimsuit")
            $ ui.interact()
            bo"See? Now that looks so much better."
            him"S-sure..."
            jump hima_swimsuit_repeatable_menu_love


label v21_rageending_hinata:
            scene emptycell_boruto_ntr1_1 with dissolve:
                yalign 0.3
            bo"[hin_rel_stutter]..."
            $ renpy.sound.play("/audio/soun_fx/eye4s.opus", channel="sfx1", loop=False, relative_volume = 0.3)
            show emptycell_boruto_ntr1_3 with flash:
                alpha 1.0 yalign 0.3
            show emptycell_boruto_ntr1_3:
                easein 1 alpha 0.0
            bo"S-stop... p-please!"
            call showscrollingimage from _call_showscrollingimage_306
            show screen parallax1280("v20_hin_captured daimyoanal",1,0.6,transformeffect=custom_vpunch_repeat(timer=1.8)) with dissolve
            da"The show has just begun, you little shit!{p}Now sit there and watch as your infidel whore of a [hin_rel_mother] has her perverted desires satisfied!"
            hin"Aaah-ahrrh! ♡ *groan* ah!♡ Give me m-more... MORE!" with flash
            da"Just listen to her! Begging for more even while I stretch her asshole! Bwahahahaha!!" with vpunch
            bo"M...more?"
            scene black
            call hidescrollingimage from _call_hidescrollingimage_250
            show emptycell_boruto_ntr1_1 with dissolve:
                alpha 1.0 yalign 0.3
            bo"She is..."
            $ renpy.sound.play("/audio/soun_fx/growl2.opus", channel="sfx3", loop=False, relative_volume = 1.3)
            show emptycell_boruto_ntr1_3 with flash:
                alpha 1.0 yalign 0.3
            show emptycell_boruto_ntr1_3 at dizzyflashshort:
                easein 3 alpha 0.0
            bo"...asking for m-more!?"
            $ renpy.sound.play("/audio/ost/Dramatic-OST.opus",channel="music",loop=True,relative_volume=1)
            bo"W-what have you done to her... you BASTARD!" with vpunch
            $ renpy.sound.play("/audio/soun_fx/eye4s.opus", channel="sfx1", loop=False, relative_volume = 0.3)
            show emptycell_boruto_ntr1_3 with flash:
                alpha 1.0 yalign 0.3
            show emptycell_boruto_ntr1_3:
                easein 1 alpha 0.0
            show emptycell_boruto_ntr1_2 with flash:
                zoom 1.1 xalign 0.5 alpha 0.0 yalign 0.3
            show emptycell_boruto_ntr1_2:
                easein 5 alpha 1.0
            bo"I'LL KILL YOU!" with Shake((0, 0, 0, 0), 0.7, dist=20, peak_time=0.7, smoothness=50)
            da"BWA-HAHAHAHA!{p}And how exactly do you plan on doing that?"
            da"You try anything and I'll have you imprisoned right across this whore's cell!{p}That way you can watch me ravage her each and every single day!"
            $ renpy.sound.play("/audio/soun_fx/growl1.opus", channel="sfx3", loop=False, relative_volume = 0.9)
            hide emptycell_boruto_ntr1_3
            show emptycell_boruto_ntr1_3:
                zoom 1.1 xalign 0.5 alpha 1.0 yalign 0.3
            show kurama1 with flash
            show kurama1:
                easein 2 alpha 0.0
            show emptycell_boruto_ntr1_3:
                easein 2 alpha 0.0
            bo "No... NO! S-STOP!" with Shake((0, 0, 0, 0), 0.7, dist=20, peak_time=0.7, smoothness=50)
            beast"And so you've come to me, in your time of need..."
            show emptycell_boruto_ntr1_3 with flashred:
                zoom 1.3 xalign 0.5 yalign 0.1
            pause 0.5
            $ renpy.sound.play("/audio/soun_fx/crate_break2.opus", channel="sfx3", loop=False, relative_volume = 1.5)
            scene black with flash
            da"W-what the-" with vpunch
            "For a brief moment, an inexplicable surge of chakra flowed through you, ripping your clothes apart and turning you into a fox-like demon!"
            "In one swift motion, you instinctively and effortlessly ripped through the iron bars as if they were made of paper..."
            scene daimyo_killed1 with dissolve:
                yalign 1.0
            show daimyo_killed1:
                easein 3 yalign 0.1
            da"W-w-wait! H-how did you-"
            $ renpy.sound.play("/audio/soun_fx/claw3.opus", channel="sfx1", loop=False, relative_volume = 0.6)
            show daimyo_killed1_1 with flash:
                yalign 0.1
            da"Wh-wh-what do you wan-" with vpunch
            $ renpy.sound.play("/audio/soun_fx/claw1.opus", channel="sfx1", loop=False, relative_volume = 0.6)
            $ renpy.sound.play("/audio/soun_fx/fleshpierce.opus", channel="sfxstat", loop=False, relative_volume = 0.5)
            show daimyo_killed1_3 with flashred:
                yalign 0.1
            da"...!" with vpunch
            $ renpy.sound.play("/audio/soun_fx/fleshpierce.opus", channel="sfxstat", loop=False, relative_volume = 1.0)
            $ renpy.sound.play("/audio/soun_fx/claw1.opus", channel="sfx1", loop=False, relative_volume = 0.6)
            show daimyo_killed1_3 with flashred:
                yalign 1.0
            pause 0.5
            scene black with vpunch
            $ renpy.sound.play("/audio/soun_fx/crate_break2.opus", channel="sfx3", loop=False, relative_volume = 1.5)
            $ renpy.sound.play("/audio/soun_fx/body_drop.opus", channel="sfx1", loop=False, relative_volume = 1)
            $ renpy.sound.play("/audio/soun_fx/woosh2.opus", channel="sfxstat", loop=False, relative_volume = 0.4)
            show daimyo_killed2:
                alpha 0.0 yalign 1.0
            
            show daimyo_killed2:
                easein 8 alpha 1.0 yalign 0.6
            "Before the Daimyo's maimed body could hit the floor, you swooped in with incredible speed and hurled his lifeless corpse outside the cell from where you broke in, leaving you and [hin_name] alone..."
            scene black with dissolve
            $ renpy.sound.play("/audio/soun_fx/growl3.opus", channel="sfx3", loop=False, relative_volume = 1.3)
            bo"[hin_rel_stutter]... *Panting*"
            "With your fox-like features having mostly dissipated, you leaned over above your kneeling [hin_rel_mother], still dazed and aloof from the drug's effects."
            scene supposed_to_be_mine_1 with dissolve:
                yalign 1.0
            show supposed_to_be_mine_1:
                easein 3 yalign 0.1
            "You turned her head towards you, staring intensely at her eyes, barely managing to hold back your unbound rage stirred by your utter disbelief of her infidelittty..." with flashred
            hin"[bo_name_stutter]... my [hin_rel_to_bo]... What's... going on?"
            menu:
                hin"[bo_name_stutter]... my [hin_rel_to_bo]... What's... going on?"
                "{color=[impulsecolor]}Take her!{/color}":
                    hin"[bo_name_stutter]... You can't look at me... when I am like this!{p}Me and you... we are-"
                    bo"Why did you do that, [hin_rel]! WHY!?{p}I wanted to be the one for you, and yet..." with vpunch
                    label jumptakeherend:
                    hin"That man... he made me feel... good!"
                    bo"Wh... what did you s-say!?" with vpunch
                    hin"Can you... bring him back?"
                    $ renpy.sound.play("/audio/soun_fx/eye4s.opus", channel="sfx3", loop=False, relative_volume = 0.9)
                    show kurama1 with flash
                    show kurama1:
                        easein 2 alpha 0.0
                    beast"GIVE ME WHAT I WANT!"
                    bo"I see now..."
                    scene supposed_to_be_mine_3 with dissolve:
                        yalign 0.1
                    bo "You are no longer m-my [hin_rel_mother], are you?" with vpunch
                    scene black with vpunch
                    bo"Then I'll give you what you want you whore!"
                    jump takeherending
                    
                "{color=[lovecolor]}Save her!{/color}":
                    bo"Why did you do that... [hin_rel_stutter], WHY!?" with vpunch
                    hin"Did you... kill that man? Why...?"
                    bo"W-why? He was... he forced himself on you! Why else!"
                    bo"Y-you were supposed to be faithful to [na_rel]... to me!"
                    bo"You w-were supposed to be..."
                    $ renpy.sound.play("/audio/soun_fx/kiss1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                    show supposed_to_be_mine_2 with dissolve:
                        yalign 0.1
                    bo"...mine!"
                    $ renpy.sound.play("/audio/soun_fx/growl1.opus", channel="sfx3", loop=False, relative_volume = 0.9)    
                    show kurama1 with flash
                    show kurama1:
                        easein 2 alpha 0.0
                    beast"My power is not to be borrowed without a price, stupid child..."
                    menu:
                        beast"My power is not to be borrowed without a price, stupid child..."
                        "{color=[impulsecolor]}Take her!{/color}":
                            jump jumptakeherend
                           
                        "{color=[lovecolor]}*a*e her!?{/color}":
                            hide supposed_to_be_mine_2 with dissolve
                            hin"[bo_name_stutter]... You can't do that!{p}Me and you... we are-"
                            bo"Aaa-argh! S-shut up!" with vpunch
                            bo"I love you, [hin_rel]! I wanted to be the one for you, and yet..." with vpunch
                            hin"That man... he made me feel... good!"
                            bo"Wh... what did you s-say!?" with vpunch
                            hin"Can you... bring him back?"
                            with flashred
                            menu:
                                hin"Can you... bring him back?"
                                "{color=[impulsecolor]}Take her!{/color}":
                                    $ renpy.sound.play("/audio/soun_fx/eye4s.opus", channel="sfx3", loop=False, relative_volume = 0.9)
                                    show kurama1 with flash
                                    show kurama1:
                                        easein 2 alpha 0.0
                                    beast"GIVE ME WHAT I WANT!"
                                    jump takeherending
                                "{color=[impulsecolor]}Rape her!{/color}":
                                    bo"W-what are you s-saying..."
                                    $ renpy.sound.play("/audio/soun_fx/growl1.opus", channel="sfx3", loop=False, relative_volume = 0.9)
                                    show kurama1 with flash
                                    show kurama1:
                                        easein 2 alpha 0.0
                                    beast"Do you see now, foolish child..."
                                    bo"[hin_rel_stutter]... what have they done to you!?"
                                    hin"Pl-please... I am h-heating up again... I need someone!"
                                    bo"You are no longer my [hin_rel_mother], are you?"
                                    $ renpy.sound.play("/audio/soun_fx/eye4s.opus", channel="sfx3", loop=False, relative_volume = 0.9)    
                                    show kurama1 with flash
                                    show kurama1:
                                        easein 2 alpha 0.0
                                    beast"GIVE ME WHAT I WANT!"
                                    scene supposed_to_be_mine_3 with dissolve:
                                        yalign 0.1
                                    bo "You are just another w-whore!" with vpunch
                                    scene black with vpunch
                                    bo"And I shall treat you like one!"
                                    jump takeherending
                                
                            

            label takeherending:
            scene v21_hin_end with dissolve:
                yalign 1.0
            show v21_hin_end:
                easein 4 yalign 0.0
            bo"Turn around, bitch!" with vpunch
            hin"N-no bad words... r-remember?"
            show v21_hin_end:
                easein 0.5 yalign 1.0
            pause 0.05
            $ renpy.sound.play("/audio/soun_fx/intro/spank4.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            bo"I said turn around! Or I'll make you..." with flash
            "You lightly slapped her breasts around to signify your intentions"
            hin"A-ah! You can't do that!"
            scene black with vpunch
            bo"Watch me!"
            scene v21_hin_hin_sex0 with dissolve:
                yalign 1.0
            show v21_hin_hin_sex0:
                easein 4 yalign 0.25
            "You turned her around and begun rubbing your erect cock on her exposed holes..."
            hin"N-not there! You can't touch that p-place... it's-" with vpunch
            scene black with dissolve
            "Meanwhile..."
            scene v21_hin_guards_alert with dissolve:
                yalign 1.0
            show v21_hin_guards_alert:
                easein 6 yalign 0.0
            pause 0.5
            "Guards" "Oi! Did you hear that?"
            "Guards" "I did. It came from deep within the dungeons, right?"
            "Guards" "The Daimyo had an arranged 'session' with the prized captive, didn't he?"
            "Guards" "Let's go check it out! Maybe he'll let us have a go too!"
            scene black with dissolve
            "..."
            hin "[bo_name_stutter], s-stop! We can't..."
            scene v21_hin_hin_sex0 with dissolve:
                yalign 1.0
            show v21_hin_hin_sex0:
                easein 4 yalign 0.25
            bo"If everyone's going to take turns on you, then why not me too!" with vpunch
            menu:
                bo"If everyone's going to take turns on you, then why not me too!"
                "Push it in!":
                    pass
            $ renpy.sound.play("/audio/soun_fx/pushitin1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
            show v21_hin_hin_sex0_1 with flash:
                yalign 0.25
            pause 0.7
            scene v21_hin_hin_sex0_1pov with dissolve:
                yalign 1.0
            show v21_hin_hin_sex0_1pov:
                easein 3 yalign 0.0
            hin"AHh! N-NO!♡ We can't! Y-you are... *moans*... my [hin_rel_to_bo]!♡"
            show v21_hin_hin_sex0_1pov with dissolve:
                yalign 1.0
            # default hin_ending21_spanked_counter = 0
            # default hin_ending21_hairpulled_counter = 0
            # default hin_ending21_counter = 0
            menu v21_hinata_endmenu1:
                hin"AHh! N-NO!♡ We can't! Y-you are... *moans*... my [hin_rel_to_bo]!♡"
                "Fuck her!" if hin_ending21_started == False:
                    $ hin_ending21_started = True
                    call showscrollingimage from _call_showscrollingimage_307
                    # show screen parallax1280("v21_hin_hin_sex0_1b",1,0.6,transformeffect=custom_ypunch_repeat(timer=1.8)) with dissolve
                    show screen parallax1280("v21_hin_hin_sex0_1b",1,0.6) with dissolve
                    bo"How can you say that in this sorry state of yours..."
                    $ renpy.sound.play("/audio/soun_fx/pushitin2.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                    show screen parallax1280("v21_hin_hin_sex0_1",1,0.6) with dissolve
                    with flash
                    hin"Aah!♡ *Moans* Don't push it deeper! S-stop... please!" with vpunch
                    bo"I am just getting started, [hin_rel]!"
                    $ renpy.sound.play("/audio/soun_fx/various_sex/mature_sexslaps2.opus",loop=True, channel="sfx3", relative_volume = 0.4,fadein=2)
                    show screen parallax1280("v21_hinataending_sex0",1,0.6,transformeffect=custom_ypunch_repeat(timer=2),menuenabled=True) with dissolve
                    bo"There's no going back now!" with vpunch
                    hin"N-no... Ah-ah!♡... NO!" with vpunch
                    jump v21_hinata_endmenu1
                "Keep going!" if hin_ending21_started == True and (hin_ending21_hairpulled_counter >= 1 or hin_ending21_spanked_counter >= 1): #after spank/pull
                    $ hin_ending21_counter += 1
                    bo"How's that, you depraved whore!" with vpunch
                    hin"A-ah-ah!♡ Don't... say such things!" with vpunch
                    bo"Still putting on your motherly act, even after what you did..."
                    bo"You betrayed us! You are nothing but a whore to me!" with vpunch
                    hin"I... Ah-ah-ah!♡... I still love you!♡!"
                    jump v21_hinata_endmenu1
                "Pull her hair!":
                    if hin_ending21_spanked_counter >= 1:
                        show screen parallax1280("v21_hin_hin_sex0_1b_spanked",1,0.6) with dissolve
                        bo"Come on [hin_rel]!"
                        show screen parallax1280("v21_hin_hin_sex0_1_hairspanked",1,0.6) with dissolve
                        $ renpy.sound.play("/audio/soun_fx/hinata/hinatamoan3.opus", channel="sfx1", loop=False, relative_volume = 3.2)
                        hin"A-ah!♡" with vpunch
                        bo"Stick that ass of yours out for me!" with vpunch
                        show screen parallax1280("v21_hinataending_sex1_spanked",1,0.6,transformeffect=custom_ypunch_repeat(timer=2),menuenabled=True) with dissolve
                        hin"You can't pull... on your [hin_rel_mother]'s hair! Ah-ah-aaah *moans*!♡"
                        bo"Then why are you swaying your hips on my cock, huh!?"
                        hin"Because I..."
                        hin"I... Ah-ah♡!"
                        $ renpy.sound.play("/audio/soun_fx/hinata/hinatamoan1.opus", channel="sfx1", loop=False, relative_volume = 2.2)
                        $ renpy.sound.play("/audio/soun_fx/pushitin2.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                        hin"I can't... s-stop myself!♡" with flash
                        bo"That's right [hin_rel]! Because you are a bitch in heat, hungry for cock!{p}Even if it's your own [hin_rel_to_bo]'s..."

                          
                    else:
                        show screen parallax1280("v21_hin_hin_sex0_1b",1,0.6) with dissolve
                        bo"Come on [hin_rel]!"
                        show screen parallax1280("v21_hin_hin_sex0_1_hair",1,0.6,menuenabled=True) with dissolve
                        $ renpy.sound.play("/audio/soun_fx/hinata/hinatamoan3.opus", channel="sfx1", loop=False, relative_volume = 3.2)
                        hin"A-ah!♡" with vpunch
                        bo"Stick that ass of yours out for me!" with vpunch
                        show screen parallax1280("v21_hinataending_sex1",1,0.6,transformeffect=custom_ypunch_repeat(timer=2),menuenabled=True) with dissolve
                        hin"You can't pull... on your [hin_rel_mother]'s hair! Ah-ah-aaah *moans*!♡"
                        bo"Then why are you swaying your hips on my cock, huh!?"
                        hin"Because I..."
                        hin"I..."
                        $ renpy.sound.play("/audio/soun_fx/pushitin2.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                        $ renpy.sound.play("/audio/soun_fx/hinata/hinatamoan1.opus", channel="sfx1", loop=False, relative_volume = 2.2)
                        hin"I can't... s-stop myself!" with flash
                        bo"That's right [hin_rel]! Because you are a bitch in heat, hungry for cock!{p}Even if it's your own [hin_rel_to_bo]'s..."

                    $ hin_ending21_started = True
                    $ hin_ending21_counter += 1
                    $ hin_ending21_hairpulled_counter += 1
                    $ hin_ending21_faster = False
                    jump v21_hinata_endmenu1
                "Spank her!":
                    if hin_ending21_spanked_counter >= 1:
                        show screen parallax1280("v21_hin_hin_sex0_1b_spanked",1,0.6) with dissolve
                        bo"Look at you, [hin_rel]!{p}Broken beyond recognition...{p}Bouncing on your [hin_rel_to_bo]'s cock..."
                        $ renpy.sound.play("/audio/soun_fx/spank5.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                        $ renpy.sound.play("/audio/soun_fx/hinata/hinatamoan3.opus", channel="sfx1", loop=False, relative_volume = 3.2)
                        show screen parallax1280("v21_hin_hin_sex1_1_spanking",1,0.6) with flash
                        pause 0.3
                        show screen parallax1280("v21_hinataending_sex1_spanked",1,0.6,transformeffect=custom_ypunch_repeat(timer=2)) with dissolve
                        $ renpy.sound.play("/audio/soun_fx/pushitin2.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                        bo"This is what you wanted, isn't it...?"
                        hin"A-ah!♡ N-no... stop... p-please!" with vpunch
                        bo"Stop? Then why are you bouncing your fat ass on my cock, huh!?" with vpunch
                        
                        $ renpy.sound.play("/audio/soun_fx/spank4.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                        $ renpy.sound.play("/audio/soun_fx/hinata/hinatamoan1.opus", channel="sfx1", loop=False, relative_volume = 1.0)
                        show screen parallax1280("v21_hin_hin_sex1_1_spanking",1,0.6) with flash
                        pause 0.3
                        show screen parallax1280("v21_hinataending_sex1_spanked",1,0.6,transformeffect=custom_ypunch_repeat(timer=2)) with dissolve
                        hin"A-ah!♡ *moans* Don't hit... your [hin_rel_mother]! Ah-ah-aaah *moans*!♡ "
                        bo"Shut up, bitch!"
                        hin"A-ah-ah-ah!♡"
                        $ renpy.sound.play("/audio/soun_fx/spank6.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                        $ renpy.sound.play("/audio/soun_fx/hinata/hinatamoan2.opus", channel="sfx1", loop=False, relative_volume = 2.2)
                        show screen parallax1280("v21_hin_hin_sex1_1_spanking",1,0.6) with flash
                        pause 0.3
                        show screen parallax1280("v21_hinataending_sex1_spanked",1,0.6,transformeffect=custom_ypunch_repeat(timer=2),menuenabled=True) with dissolve
                        bo"It seems you are getting tighter each time I do!"

                          
                    else:
                        show screen parallax1280("v21_hin_hin_sex0_1b",1,0.6) with dissolve
                        bo"Look at you, [hin_rel]!{p}Broken beyond recognition...{p}Bouncing on your [hin_rel_to_bo]'s cock..."
                        show screen parallax1280("v21_hin_hin_sex0_1",1,0.6) with dissolve
                        $ renpy.sound.play("/audio/soun_fx/pushitin2.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                        bo"This is what you wanted, isn't it...?"
                        
                        hin"A-ah!♡ N-no... stop... p-please!" with vpunch
                        bo"Stop? Then why are you bouncing your fat ass on my cock, huh!?" with vpunch
                        $ renpy.sound.play("/audio/soun_fx/spank4.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                        show screen parallax1280("v21_hin_hin_sex1_1_spanking",1,0.6) with flash
                        pause 0.3
                        show screen parallax1280("v21_hinataending_sex1_spanked",1,0.6,transformeffect=custom_ypunch_repeat(timer=2)) with dissolve
                        hin"A-ah!♡ *moans* Don't hit... your [hin_rel_mother]! Ah-ah-aaah *moans*!♡ "
                        bo"Shut up, bitch!"
                        hin"A-ah-ah-ah!♡"
                        $ renpy.sound.play("/audio/soun_fx/spank4.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                        show screen parallax1280("v21_hin_hin_sex1_1_spanking",1,0.6) with flash
                        pause 0.3
                        show screen parallax1280("v21_hinataending_sex1_spanked",1,0.6,transformeffect=custom_ypunch_repeat(timer=2),menuenabled=True) with dissolve
                        bo"It seems you are getting tighter each time I do!"
                    $ hin_ending21_started = True
                    $ hin_ending21_counter += 1
                    $ hin_ending21_spanked_counter += 1
                    $ hin_ending21_faster = False
                    jump v21_hinata_endmenu1
                "Thrust faster!" if hin_ending21_counter >= 3 and hin_ending21_faster == False:
                    $ hin_ending21_faster = True
                    $ hin_ending21_counter += 1
                    hin"Pl-please... Ah-ah!♡ No more... I am about to-!!♡" with flash
                    bo"I can't believe you've let other men do that to you..."
                    bo"After you've acted so distant from me for so long..."
                    hin"Ah-ah-ah!♡ N-no..."
                    $ renpy.sound.play("/audio/soun_fx/pushitin2.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                    show screen parallax1280("v21_hinataending_sex1_spanked_fast",1,0.6,transformeffect=custom_ypunch_repeat(timer=1),menuenabled=True) with dissolve
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatamoan3.opus", channel="sfx1", loop=False, relative_volume = 3.2)
                    bo"You dare put other men before me!? Your own [hin_rel_to_bo]!?"
                    bo"Have you no shame!?" with vpunch
                    hin"Ah-ah-ah!♡ F-fuck me... ha-harder!♡"
                    jump v21_hinata_endmenu1            

                "{color=[impulsecolor]}Fill her up!{/color}" if hin_ending21_faster == True:
                    show screen parallax1280("v21_hinataending_sex1_spanked_fast",1,0.6,transformeffect=custom_ypunch_repeat(timer=1),menuenabled=False) with dissolve
                    bo"All you ever do is tease me and tease me some more!"
                    bo"And then you go and do something like this with other men..."
                    bo"Have you... no dignity!?" with flash
                    $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    hin"Ah-ah-ah!♡ Yes-yes-yes!" with flash
                    $ renpy.sound.play("/audio/soun_fx/cum5.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    bo"You immoral WHORE!" with flash
                    scene black
                    call hidescrollingimage("Click twice to fill her up!") from _call_hidescrollingimage_251
                    $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    scene black
                    stop sfx3 fadeout 3
                    show v21_hin_hin_sex0_1povcum with longerflash:
                        yalign 1.0
                    show v21_hin_hin_sex0_1povcum:
                        easein 10 yalign 0.5
                    bo"Aaaarr-aaah!!" with vpunch
                    hin"No-no-no! Not inside!! Ah-ah-ah!♡" with flash
                    $ renpy.sound.play("/audio/soun_fx/bodythud.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                    scene black
                    "[hin_name]'s convulsing legs gave out from beneath her.{p}She laid on the floor, experiencing an ecstatic orgasm that left her shaking, paralyzed by the euphoric feeling elicited by her drugged state."
                    bo"*Panting*...{p}Look at you [hin_rel]... Laying on the floor, shaking like an animal!"
                    hin"*Uh-a-a-ah!♡ *Orgasmic moans*!"
                    scene v21_hin_beforeend1 with dissolve:
                        yalign 1.0
                    show v21_hin_beforeend1:
                        easein 8 yalign 0.4
                    bo"Have you no words... no apology?" with vpunch 
                    hin"B...[bo_name_stutter]... I am s-sorry..."
                    hin"But... I am not yet..."
                    scene v21_hin_beforeend1 with dissolve:
                        yalign 0.8 zoom 1.2 xalign 1.0
                    bo"Speak louder, you fucking bitch!" with vpunch
                    hin"I am not yet... satisfied... My pussy... is still burning up!" with vpunch
                    scene black with vpunch
                    bo"Not yet... satisfied?"
                    bo"So you did enjoy this after all..."
                    bo"You yearn for more of my cock, don't you!?" with vpunch
                    hin"N-no..."
                    bo"I always knew you were a masochistic nympho..."
                    scene v21_hin_nelson0 with dissolve:
                        yalign 1.0
                    show v21_hin_nelson0:
                        easein 8 yalign 0.0
                    "Emboldened by her insatiable remarks, you picked [hin_name] up with ease, placing her in the most shameful pose you could think of, the one you found her fucking other men with..."
                    bo"In that case, tell me... [hin_rel_mother]!"
                    show v21_hin_nelson0:
                        easein 1 yalign 1.0
                    bo"Have you ever had your asshole stretched? You probably haven't even let [na_rel] touch you down there, did you?"
                    hin"Awweeh!♡ ...sh-shtop!"
                    bo "No matter... You are mine now!"
                    menu:
                        bo "No matter... You are mine now!"
                        "{color=[impulsecolor]}Push it in her ass!{/color}":
                            pass
                        
                    $ renpy.sound.play("/audio/soun_fx/pushitin1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                    show v21_hin_nelson1 with flash:
                        yalign 1.0
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatamoan1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                    call showscrollingimage from _call_showscrollingimage_308
                    # show screen parallax1280("v21_hinataending_sex1_spanked_fast",1,0.6,transformeffect=custom_ypunch_repeat(timer=1)) with dissolve
                    show screen parallax1280("v21_hin_nelson1",1,0.6,menuenabled=True) with dissolve
                    hin"Mhh-aah!♡" with flash
                    bo"I'll make sure you are never left unsatisfied again!" with vpunch
                    menu:
                        bo"I'll make sure you are never left unsatisfied again!"
                        "{color=[impulsecolor]}Fuck her ass raw!{/color}":
                            pass
                    show screen parallax1280("v21_hinataending_nelson",1,0.6,transformeffect=custom_vpunch_repeat(timer=1.5),menuenabled=True) with dissolve
                    $ renpy.sound.play("/audio/soun_fx/sexslaps1.opus", channel="sfx3", loop=True, relative_volume = 0.6,fadein=0.8)
                    bo"How's this, you cheating WHORE!" with vpunch
                    hin"Ah-ah-♡ *Muffled words*... ah-ah-*moans*!♡" with vpunch
                    bo"What's that...? Can't even talk with your mouth stretched open, can you?"
                    bo"But it sure sounds like you are enjoying this!"
                    bo"I for one sure am! Your asshole is even tighter than your used up cunt!" with vpunch
                    bo"Though it won't stay like that after I have my way with your ass!"
                    menu:
                        bo"Though it won't stay like that after I have my way with your ass!"
                        "{color=[impulsecolor]}Ravage her asshole!{/color}":
                            pass
                    show screen parallax1280("v21_hinataending_nelson_fast",1,0.6,transformeffect=custom_vpunch_repeat(timer=0.8),menuenabled=True) with dissolve
                    bo"F-fuck yes!" with vpunch
                    hin"Awweeh!♡ ...sh-shtop! Ah-ah--AAAHH!♡"
                    bo"If only I knew how much of an insatiable whore you were..."
                    bo"I'd be fucking you every chance I could get back home!"
                    bo"Do you have any idea how many times I fantasized about fucking your brains out?"
                    bo"All these mornings you kept shaking your ass around in my room..."
                    bo"This is for teasing me for all those years with your whore-ish looks, bitch!" with vpunch
                    menu:
                        bo"This is for teasing me for all those years with your whore-ish looks, bitch!"
                        "{color=[impulsecolor]}Fill her up!{/color}":
                            pass
                    $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    hin"Ah-ah-ah!♡ Yesh-yesh!! *moans*" with flash
                    $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    stop sfx3 fadeout 2
                    show screen parallax1280("v21_hin_nelson2",1,0.6) with longerflash
                    bo"Here it comes, you fucking nympho bitch!" with vpunch
                    show screen parallax1280("v21_hin_nelson3",1,0.6,menuenabled=False) with longerflash
                    bo"*Panting* Do you... feel it, [hin_rel]?"
                    bo"My cock throbbing, flooding your insides with MY sperm..."
                    scene black
                    call hidescrollingimage() from _call_hidescrollingimage_252
                    bo"From now on... no other man shall have his way with you, not even [na_rel]!"
                    "You let go of [hin_name]'s mouth..."
                    $ renpy.sound.play("/audio/soun_fx/bodythud.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                    "Weakened by the constant orgasms, [hin_name] slowly tumbled down beneath you..." with vpunch
                    bo"I will be the only one responsible for fucking you senseless, you hear me?"
                    "Elated and unresponsive, she started slowly crawling away towards the cell's now broken iron bars..."
                    bo"Oi, [hin_rel]... Answer me!{p}I said..."
                    $ renpy.sound.play("/audio/soun_fx/spank4.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatamoan3.opus", channel="sfx1", loop=False, relative_volume = 3.2)
                    scene v21_hin_crawl1 with flash:
                        yalign 1.0
                    show v21_hin_crawl1:
                        easein 2 yalign 0.1
                    bo"Do you understand me!?" with vpunch
                    show v21_hin_crawl1:
                        easein 1 yalign 1.0
                    "You grabbed her hair and harshly smacked her ass, putting a stop to her feeble crawling..."
                    bo"I said..."
                    $ renpy.sound.play("/audio/soun_fx/spank5.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatamoan1.opus", channel="sfx1", loop=False, relative_volume = 2.2)
                    scene v21_hin_crawl1_1 at custom_ypunch_repeat(1) with flash:
                        zoom 1.1 xalign 0.5 yalign 0.2
                    bo"I will be the one fucking you senseless! Not [na_rel], neither these shitty assholes, you got that!?" with vpunch
                    hin"Ah-ah-aaah♡! Y-yes, [bo_name_stutter]! F-fuck me h-harderrr-Ah-ah!♡ Pl-please...."
                    scene v21_hin_crawl1 with dissolve:
                        yalign 0.1
                    $ renpy.sound.play("/audio/soun_fx/spank5.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatamoan2.opus", channel="sfx1", loop=False, relative_volume = 2.2)
                    scene v21_hin_crawl1_1 with flash:
                        yalign 0.2 
                    bo"SAY THAT LOUDER!" with vpunch
                    scene black
                    $ renpy.sound.play("/audio/soun_fx/spank6.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                    hin"Arh-aaah♡!" with flash
                    scene v21_hin_crawl1_2 with dissolve:
                        yalign 0.8
                    show v21_hin_crawl1_2:
                        easein 5 yalign 0.1
                    bo"Say it, [hin_rel]!"
                    hin"Ah-ah...♡! I need..."
                    show v21_hin_crawl1_2_yes with flash:
                        yalign 0.1 zoom 1.1 xalign 1.0
                    show v21_hin_crawl1_2_yes:
                        easein 8 yalign 0.5
                    $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                    hin"-Ah-ah-aaah♡! I need you [bo_name]! Ah-ah-aaah♡! I need my [hin_rel_to_bo]'s cock inside of me!"
                    scene black
                    "Meanwhile..."
                    show daimyo_killed2:
                        alpha 0.0 yalign 1.0
                    
                    show daimyo_killed2:
                        easein 8 alpha 1.0 yalign 0.6
                    "Scared Guard" "Oi... is th-th-th-that-"
                    "Skeptic Guard" "It can't be!"
                    scene black with dissolve
                    "..."
                    scene v21_hin_crawl1_3_afterblack with dissolve:
                        yalign 1.0
                    show v21_hin_crawl1_3_afterblack at custom_ypunch_repeat(1):
                        easein 5 yalign 0.0
                    bo "That's right, you are forever mine!"
                    bo "I'll make sure I plant my seed in you every single day!"
                    hin"Ah-ah-ah!♡ I don't care anymore...{p}F-fuck me [bo_name_stutter]... FUCK ME H-HARDER!♡"
                    scene black with dissolve
                    $ renpy.sound.play("/audio/soun_fx/growl3.opus", channel="sfx3", loop=False, relative_volume = 0.9)   
                    show kurama1 onlayer screens with flashred
                    show kurama1 onlayer screens:
                        easein 2 alpha 0.0
                    beast "He-he-he... It won't be long now.{p}Soon I shall be born again!"
                    $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                    call showscrollingimage from _call_showscrollingimage_309
                    show screen parallax1280("v21_hin_crawl1_4_afterblack",1,0.3) with flash
                    hin"I l-love you... my [hin_rel_to_bo]!"
                    bo "How could I ever love someone like you, [hin_rel_mother]..."
                    bo "Betrayed and forgotten, now I realize...{p}All I ever felt for you was never love..."
                    bo "It was lust all along!" with vpunch
                    $ renpy.sound.play("/audio/soun_fx/intro/bodythud.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                    show screen parallax1280("blackscreen",1,0.6) with vpunch
                    bo"Your defiled face disgusts me, your breath stinks of other men's odor..."
                    "You shove her wanting face away from you, causing her to lose her balance and fall to the ground."
                    $ renpy.sound.play("/audio/soun_fx/spank5.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatamoan3.opus", channel="sfx1", loop=False, relative_volume = 3.2)
                    hide screen parallax1280
                    show screen parallax1280("v21_hin_crawl1_5_afterblack",1,1.0)
                    with flash
                    bo"You don't deserve anyone's love, not anymore!{p}All you are good for is being my own personal fuckmeat to be bred!"
                    hin"Y-yes... Br-breed me! Give me more... MORE!" with vpunch
                    scene black with dissolve
                    call hidescrollingimage from _call_hidescrollingimage_253
                    $ renpy.sound.play("/audio/soun_fx/spank5.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatamoan2.opus", channel="sfx1", loop=False, relative_volume = 2.2)
                    with flash
                    show daimyo_killed2:
                        alpha 0.0 yalign 1.0
                    
                    show daimyo_killed2:
                        easein 8 alpha 1.0 yalign 0.6
                    "The two guards cautiously observed from afar, realizing the danger you posed clearly evident by their lord's maimed carcass..."
                    "Your violent assault, both physical and sexual, mortified even the likes of them."
                    scene black with dissolve
                    "..."
                    $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                    bo"F-fffuck! I'll never get tired of your cunt, [hin_rel_mother]!" with flash
                    scene v21_hin_end with dissolve:
                        yalign 1.0
                    show v21_hin_end:
                        easein 5 yalign 0.1
                    bo"You'll be forever mine...{p}My very own cocksleeve!"
                    "Your endless lust left you blind to the looming dangers around you..."
                    "The guards carefully bid their time, waiting for an opportunity to silently approach!"
                    $ renpy.sound.play("/audio/soun_fx/swordsheathe3.opus", channel="sfx1", loop=False, relative_volume = 1.0)
                    $ renpy.sound.play("/audio/soun_fx/ominous_sound.opus", channel="sfx2", loop=False, relative_volume = 1.5)
                    show v21_hin_end_dead with dissolve:
                        yalign 0.1
                    "As soon as you turned your back to the cell's entrance..."
                    
                    scene black with vpunch
                    with flashred
                    $ renpy.sound.play("/audio/soun_fx/fleshpierce.opus", channel="sfxstat", loop=False, relative_volume = 0.5)
                    pause 0.3
                    image youdiedmp4 = Movie(play="images/video/youdied.webm",loop=False)
                    show youdiedmp4 with dissolve:
                        yalign 0.3 xalign 0.5
                    "The tip of their spear ran through your chest, piercing your heart!"
                    $ renpy.sound.play("/audio/soun_fx/growl1.opus", channel="sfx2", loop=False, relative_volume = 0.9)   
                    show kurama1 onlayer screens with flashred
                    show kurama1 onlayer screens:
                        easein 2 alpha 0.0
                    "An outburst of rage gave you enough strength to fend against the two guards..."
                    show v20_borutokilled with dissolve:
                        yalign 1.0
                    show v20_borutokilled:
                        easein 4 yalign 0.0
                    $ renpy.sound.play("/audio/soun_fx/heartbeatdead.opus", channel="sfx2", loop=False, relative_volume = 2.2)
                    "Before you knew it, your heart gave up on you, but not before managing to kill the two guards.{p} Miraculously, [hin_name] was left unharmed by your unbound fury."
                    scene black with dissolve
                    "Day 30..."
                    scene v20_pregnant1 with dissolve:
                        yalign 0.0
                    show v20_pregnant1:
                        easein 5 yalign 1.0
                    "[hin_name], a shadow of her former self, was kept imprisoned and later found carrying a child within her womb, it's father still unknown."
                    scene black with dissolve
                    "Day 90..."

                    scene v21_burnedvillage with dissolve:
                        zoom 0.98 xalign 0.5 yalign 0.5
                    "The news of the Daimyo's death quickly spread."
                    show ninjawar3 with dissolve:
                        zoom 0.5
                    "Combined with the Hokage's absence, It didn't take long for opportunistic nations to swoop in and reap every valuable commodity Konoha possessed..."
                    scene v20_tojicum0_1a with dissolve:
                        yalign 1.0
                    show v20_tojicum0_1a:
                        easein 5 yalign 0.0
                    "The female populace would not be spared either..."
                    scene black with dissolve
                    "Ten years later..."
                    "Konoha was reduced to nothing more than rubble. The village that had stood for generations crumbled under their oppressors agenda."
                    "Men were quickly killed, a mercy their women were not granted. A mysterious drug's influence spread among them, reshaping them into obedient cattle of their conquerors' will."
                    "One woman survived..."
                    scene v20_hima_revenge with dissolve:
                        yalign 1.0
                    show v20_hima_revenge:
                        easein 5 yalign 0.0
                    "[him_name] embarked on a lifelong mission of revenge, swearing vengeance upon those who wronged her family."
                    scene black with dissolve
                    $ renpy.sound.play("/audio/soun_fx/bassstart.opus", channel="sfx1", loop=False, relative_volume = 1, fadein = 0.05)
                    queue sfx1 ("audio/soun_fx/introbass3.opus") volume 0.4 loop
                    show disclameimerintro with Fade(0.5,0,3):
                        zoom 2.0 xalign 0.6 yalign 0.3
                    show disclameimerintro:
                        easeout 30 subpixel True zoom 1.0 xalign 0.492 yalign 0.3
                    "Years later, when the Shinobi world lay in ruins, survivors whispered of a woman with eyes like blood and the fury of a fox - a harbinger of their reckoning..."
                    $ renpy.end_replay()
                    menu:
                        "Years later, when the Shinobi world lay in ruins, survivors whispered of a woman with eyes like blood and the fury of a fox - a harbinger of their reckoning..."
                        "Game over":
                            dev"You dun fucked up with this one mate. There's no returning to reality now. You are living in it."
                            $ renpy.full_restart()

label kushina_tierherup_shibari:
    bot"Hey Kurama!"
    bot"I think she is ready..."
    ku"Ready? Ready for what exactly..."
    scene black
    bot"Strip her of all her clothes!" with vpunch
    scene v21_kushina_hate_closeup_naked with dissolve:
        yalign 0.2
    ku"[bo_name_stutter]!?" with vpunch
    bot"And a little accessory for the upcoming display..."
    scene toy_start1 with flash
    bot"Pierce her nipples!" with vpunch
    show toy_start1:
        easein 0.7 yalign 0.0
    ku"Ou-ouch! What is the meaning of this..." with vpunch
    $ renpy.sound.play("/audio/soun_fx/growl1.opus", channel="sfx3", loop=False, relative_volume = 0.9)
    bot"It's time we show you who's in charge in here, you stuck up hag!"
    scene black with vpunch
    bot"Tie her up, Kurama!" with vpunch
    scene toy_start1_1 with dissolve:
        yalign 1.0
    show toy_start1_1:
        easein 3 yalign 0.1
    ku"A-aah! *Groans* More... r-ropes!?{p}This h-hurts! [bo_name_stutter], stop this at once!"
    bot"You claim you are here to help, right granny?"
    show toy_start1_1:
        easein 5 yalign 0.8
    ku"Of course, now untie me!{p}Pretty p...please?"
    scene toy_start1_2 with dissolve:
        yalign 1.0
    show toy_start1_2:
        easein 3 yalign 0.3
    ku"M-my legs?"
    bot"Then how comes all you've ever done is be a massive cock-tease!"
    bot"You keep flaunting your curves around knowing how it affects me..."
    bot"You are doing it on purpose, aren't you?"
    ku"Wh-what are you saying, [bo_name_stutter]!"
    bot"I understand now..."
    scene black with vpunch
    bot"Spread your legs open, you lying bitch!" with vpunch
    scene toy_spread with dissolve:
        yalign 1.0
    show toy_spread:
        easein 4 yalign 0.38
    bot"This is what you wanted all along, isn't it?"
    ku "What are you talking about!?"
    bot"To have your own perverted desires satisfied..."
    bot "Just like me, you are afflicted by the same curse, are you not?"
    bot "That means you feel what I feel, right!?"
    ku "I don't know what you are talking about!{p}You are losing your mind, [bo_name]!"
    bot"Then I'll prove it to you, by bringing you to orgasm!" with vpunch
    menu kushina_shibarimenu:
        bot"Then I'll prove it to you, by bringing you to orgasm!"
        "Degrade her!":
            bot"Losing my mind, am I now..."
            scene toy_pose1_1 with dissolve:
                yalign 1.0
            show toy_pose1_1:
                easein 5 yalign 0.3
            bot"I am not the one putting the 'goods' on display for all to see, am I?{p}Let alone for your grandson, you whore!"
            ku"Stop staring down there... And don't call me that again!"
            ku"You are forcing me to do this!" with vpunch
            scene toy_pose1 with dissolve:
                yalign 1.0
            show toy_pose1:
                easein 5 yalign 0.2
            bot"We'll see if you claim the same after I bring you to your knees!"
            "You forced her on an awkward position, with the ropes rubbing across her erogenous zones..."
            show toy_pose1:
                easein 1 yalign 0.9
            ku"AW-OUCH! That burns my...- you idiot! Put me down at once!" with vpunch
            scene toy_start1_2 with dissolve:
                yalign 1.0
            show toy_start1_2:
                easein 3 yalign 0.3
            ku"M-my legs?"
            bot"So you do prefer your legs spread apart after all..."
            ku"Stop flailing me around, you idiot! What if..."
            scene toy_start1_1 with dissolve:
                yalign 0.0
            show toy_start1_1:
                easein 5 yalign 0.9
            ku"I fall... or s-something!"
            bot"Don't go giving me ideas now..."
            bot"Maybe I shall have you fall straight on to my cock!"
            ku"Kurama... you BASTARD! Stop messing with his mind!" with vpunch
            scene toy_spread with dissolve:
                yalign 1.0
            show toy_spread:
                easein 4 yalign 0.4
            bot"Now shut up and spread your legs wide open!" with vpunch
            jump kushina_shibarimenu
        "Use a vibrator!":
            scene toy_spread:
                easein 0.4 yalign 1.0 zoom 1.1
            bot"Make her pussy scream, Kurama!" with vpunch
            scene black with vpunch
            ku"My... WHAT NOW!?" with vpunch
            ku"Have you lost your damn mind-"
            scene toy_vibrator1 with flash
            show toy_vibrator1:
                easein 5 yalign 0.15
            ku"Ahh! It... burns!" with vpunch
            ku"You can't do something like that to me!"
            ku"We sh-share a sacred bond, [bo_name_stutter]!"
            show toy_vibrator1:
                easein 2 yalign 0.4
            bot"We'll share an even stronger bond, once I stuff your pussy with my cock, bitch!"
            ku"Sh-shut up, you idiot! Untie me at once!" with vpunch
            show toy_vibrator1_1 with dissolve:
                easein 1 yalign 0.9
            bot"Come on, spread your legs wide open!"
            scene toy_vibrator1_1 with flash:
                yalign 0.0
            show toy_vibrator1_1:
                easein 0.6 yalign 1.0
            bot"Your body was made to be played with, Kushina!"
            ku"Ar-aah!! *Groans* Take it out, take it OUT!" with vpunch
            scene black
            bot"I told you, I am going to make you cum!"
            scene toy_vibrator1_2 with dissolve:
                yalign 0.0
            show toy_vibrator1_2:
                easein 6 yalign 0.75
            ku"No m-more... please!" with vpunch
            bot"For an old hag, you sure are holding up well, Kushina!"
            bot"Look at that flexibility of yours!"
            scene toy_vibrator1_3cum with flash:
                yalign 0.0
            ku"Aaahh-aah! I don't wanna hear it! Shut up... SHUT UP!" with flash
            bot"Oh I am going to have fun with you once you are broken down, granny!"
            bot"Up the intensity, Kurama!" with vpunch
            ku"I am n-not g-g-going to cum..." with flash
            $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            show toy_vibrator1_3cum:
                easein 1 yalign 1.0
            call changekushina(10) from _call_changekushina_10
            ku"...From something like th-th-this!"
            scene toy_vibrator1_3cum with flash:
                yalign 0.9
            $ renpy.sound.play("/audio/soun_fx/cum6.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            $ renpy.sound.play("/audio/soun_fx/wakeup.opus", channel="sfx2", loop=False, relative_volume = 0.6)

            show toy_vibrator1_3cum at brightreveal:
                matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 
            with longerflash
            with Shake((0, 0, 0, 0), 1.5, dist=20, peak_time=0.8, smoothness=50)
            pause 0.3
            scene kushina_dream wakeup with dissolve
            call changeHatred(1,statlevel=2) from _call_changeHatred_232
            bo"*Snoring... angrily!*" with vpunch
            scene black with dissolve
           
            jump action_taken
        "Use anal beads!":
            scene toy_spread:
                easein 0.4 yalign 1.0 zoom 1.1
            bot"Stuff her asshole, Kurama!" with vpunch
            scene black with vpunch
            ku"My... WHAT NOW!?" with vpunch
            ku"Have you lost your damn mind-"
            scene toy_analbeads0 with flash
            show toy_analbeads0:
                easein 5 yalign 0.3
            ku"Aww-arrh! It... hurts!" with vpunch
            ku"Why would you... think of that!?"
            bot"Your asshole can take some beating... Not bad, for an old hag!"
            ku"Sh-shut up, you idiot! Untie me at once!" with vpunch
            show toy_analbeads0:
                easein 1 yalign 0.9
            bot"But if you are going to fit my fully erect cock up your ass..."
            scene toy_analbeads1 with flash:
                yalign 0.0
            show toy_analbeads1:
                easein 0.6 yalign 1.0
            bot"You are going to have to do better than that!{p}Deeper, Kurama!"
            ku"Ar-aah!! *Groans* Take 'em out, take it OUT!" with vpunch
            scene black
            bot"Shut up and spread those legs open, bitch!"
            scene toy_analbeads1_1 with dissolve:
                yalign 0.0
            show toy_analbeads1_1:
                easein 6 yalign 1.0
            ku"No m-more... please!" with vpunch
            bot"But there's only a few left to fit in you, granny!"
            scene toy_analbeads1_2:
                yalign 0.0
            show toy_analbeads1_2:
                easein 6 yalign 1.0
            bot"Besides... you haven't even came yet!" with flash
            ku"I am n-not g-g-going to cum..." with flash
            $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            scene toy_analbeads1_3 with flash:
                yalign 0.0
            call changekushina(10) from _call_changekushina_11
            ku"...From something like th-th-this!"
            scene toy_analbeads1_3 with flash:
                yalign 0.9
            $ renpy.sound.play("/audio/soun_fx/cum6.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            $ renpy.sound.play("/audio/soun_fx/wakeup.opus", channel="sfx2", loop=False, relative_volume = 0.6)

            show toy_analbeads1_3 at brightreveal:
                matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 
            with longerflash
            with Shake((0, 0, 0, 0), 1.5, dist=20, peak_time=0.8, smoothness=50)
            pause 0.3
            scene kushina_dream wakeup with dissolve
            call changeHatred(1,statlevel=2) from _call_changeHatred_233
            bo"*Snoring... angrily!*" with vpunch
            scene black with dissolve
           
            jump action_taken



init python:

    def initialize_replay_defaults_2():

        if _in_replay:

            store.hinata_respect = 10
            store.hinata_obedience.level = 5
            store.hinata_obedience.value = 100
            store.hinata_love.level = 5
            store.hinata_love.value = 100

            store.himawari_respect = 10
            store.himawari_obedience.level = 5
            store.himawari_obedience.value = 100
            store.himawari_love.level=5
            store.himawari_love.value = 100

            store.hatred.level = 5
            store.hatred.value = 100
            store.dominance.level = 5
            store.dominance.value = 100
            store.percentage = 100
            store.strength = 10

