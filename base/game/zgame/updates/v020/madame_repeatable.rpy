

label ch1_d14_onsen_repeatable: 

    if onsen_blocked == True:
        bo "I can't enter! I don't think I am welcome in there anymore..."
        jump jumpbackdaimyoquarters
    

    $ onsen_stared = False

    scene palace3_night with dissolve
    play music "audio/ost/Senya.opus" volume 0.4
    show palace3_night:
        subpixel True 
        easein 5 zoom 1.3 xalign 0.5 yalign 1.0
    "You hear what sounds like a woman's voice resonating from the area as you begin to enter."
    show boruto surprised at center, with dissolve
    bot "Fuck, there's someone over there!" with vpunch
    show boruto worried with dissolve
    bot "I hope it's Madame again, and not somebody else..."
    if borutoknockedoutlove == True or borutoknockedouthatred == True:
        show boruto embarassed with dissolve
        bot "I don't want to get knocked out again by any guards, those bastards really are tough!"
    show boruto suspicious with dissolve
    bot "It doesn't sound like a guard at least, I'll just have to take my chances with them..."
    
    menu:
        "Rush inside":
            play sound "audio/soun_fx/footsteps.opus" volume 1.2
            scene blackscreen with fade
            "You burst into the onsen in a hurry, glancing back one last time to ensure you weren't spotted."
            show bg onsen1_night with dissolve
            show boruto suspicious at left with dissolve
            bot "Back in the onsen again..."
            "The voice has now become clearer and decipherable, allowing you to faintly make out the tail end of the conversation..."
            scene bg onsen1_night with fade
            show madame normal with dissolve: 
                xalign -0.5 
            show boruto suspicious:
                xalign 2.0 
                easein 1 xalign 1.0

            "Woman" "...- remember to toy with them and utilize the art of seduction."
            bot "That voice... It sounds like Madame!"
            show boruto suspicious:
                easein 3 xalign 0.9
            show madame normal:
                xalign -0.5
                easein 3 xalign 0.0
            "Woman" "Let their hunger for your touch swell and overflow, before you allow your bodies to be joined with the techniques I have demonstrated."
            "Woman" "Instant gratification is never an effective strategy! The thrill of the chase will amplify their lust and desires to greater heights."
            show boruto surprised at right with vpunch
            bot "Lust and desire? Art of seduction? Is she teaching them again?!"
            "Servant" "Madame, I apologize for interrupting, but... we are not alone."

            scene onsen_intro 1 with fade
            mada "Oh?"
            show onsen_intro 1:
                easein 5 yalign 0
            mada "Well well, it seems like we have a guest tonight!"
            mada "Welcome back [bo_name], I see you have returned to us once more."
            mada "I trust you have been keeping yourself out of trouble since our last encounter?"

            if hinata_captured == True:
                bo "I'm afraid not... I need your help again Madame!"
            else:
                bo "Of course Madame, I've only come to visit this time... \nI hope you don't mind me dropping by unannounced?"
                mada "Not at all... As long as you behave, are always welcome here little lamb."

            mada "Truth be told... Your return is not an unexpected one, and I am glad to see you again."   

            scene onsen_intro 1_1 with dissolve:
                yalign 0
            "Whispers" "{size=*0.8}Who is that? Have they sent someone for us to practice on?{/size}"
            show onsen_intro 1_1 with dissolve:
                xalign 1.0 yalign 0.35 zoom 1.6
            "Blonde woman" "{size=*0.8}I sure hope so, I was starting to get bored...{/size}"
            "Blonde woman" "{size=*0.8}I think he looks rather cute, can I go first?{/size}"
            show onsen_intro 1_1 with dissolve:
                xalign 1.0 yalign 0.2 zoom 2
            "Brunette woman" "{size=*0.8}That's no surprise, you think EVERYONE is cute!{/size}"
            "Brunette woman" "{size=*0.8}You would really open up your legs for someone with hair like THAT? \nHe looks ridiculous!{/size}"

            scene onsen_intro 1_1 with dissolve:
                yalign 0
            bot "They've all got their eyes on me... \nWhat are they whispering to each other?!"
            bot "I should still be careful with how I approach this, just in case..."

            menu onsen_approach_1_repeatable:
                "Stare at her":
                    $ onsen_stared = True
                    show onsen_intro 1_1:
                        subpixel True
                        easein 10 zoom 1.68 xalign 0.5 yalign 0.0
                    bot "It's always so easy to lose my train of thought when Madame is around..."
                    show screen parallax1280("onsen_intro 1_1",) with dissolve 
                    call showscrollingimage from _call_showscrollingimage_208
                    "Your eyes wander and visually explore the woman's stunning figure before you." 
                    call increaselust(5) from _call_increaselust_272
                    bot "What an incredible woman she is... Damn she is fine!"
                    bot "She's a royal concubine for the Daimyo though, I shouldn't completely let my guard down around her!"
                    bot "She has total authority within this area and it shows! \nShe effortlessly commands the whole room with her presence alone."
                    bot "Madame hasn't done any wrong to me yet though... \nMaybe she deserves the benefit of the doubt?"
                    call hidescrollingimage from _call_hidescrollingimage_169
                    hide screen parallax1280 with dissolve

                    scene onsen_intro 1_1 with dissolve:
                        yalign 0 zoom 1.0 xalign 0.5
                    mada "Lost in your own head again, are we?"

                    menu onsen_approach_2_repeatable:
                        "Check her out again":
                            show screen parallax1280("onsen_intro 1_1") with dissolve
                            call showscrollingimage from _call_showscrollingimage_209
                            bot "Just look at the size of that ass!"
                            call increaselust(10) from _call_increaselust_273
                            bot "I'd love to have my way with that juicy thing."
                            bot "I would lick the sweat running down her smooth thighs and bury my face in those cheeks!"
                            bot "Her figure rivals even that of [hin_rel]'s..."
                            if hinata_captured == True:
                                bot "[hin_rel_stutter]!" with vpunch
                                bot "WHAT AM I DOING?!" with vpunch
                                bot"I need to focus on saving her instead of wasting time!"
                            hide screen parallax1280
                            show screen parallax1280("onsen_intro 1_1annoyed", menuenabled=True)
                            with dissolve
                            mada "[bo_name] I don't have time to just watch you stare at me!" with vpunch
                            mada "Are you capable of coherent speech today? Or are you just here to foolishly drool all over my floor!"
                            bot "Fuck, seems like she is losing her patience... \nI shouldn't anger her!"

                            menu onsen_approach_3_repeatable:
                                bot "Fuck, seems like she is losing her patience... \nI shouldn't anger her!"
                                "Keep staring at her":
                                    $ onsen_stared_long = True
                                    "You helplessly continue to stare at her with a blank expression on your face, no words escaping your mouth."
                                    "The silence in the room would be deafening, if not for the faint whispers and giggles of the servants circulating the room."
                                    "The contrasting combination of normal social cues and lustful thoughts clash in your head, rendering you helpless and lost."
                                    "You're immobilized in front of your audience like a deer caught in headlights."
                                    bot "It's pointless, all I can think about is how much I want to bury my face in her curves..."
                                    bot "What could I possibly say to make this situation any better?"
                                    bot "She probably thinks I'm just another perverted creep that thinks with my cock instead of my head..."
                                    bot "How did I manage to end up like this? \nWhy does my brain just simply turn off in a room full of half-naked women...?"
                                    show onsen_intro 1_1annoyed:
                                        xalign 0.9 yalign 0.5 zoom 1.8
                                    hide screen parallax1280
                                    with dissolve
                                    bot "I guess it could be worse... I might as well enjoy the view while it lasts!"
                                    if hinata_captured == True:
                                        bot "I tried my best [hin_rel]... \nI'm sorry..."
                                    
                                    show screen parallax1280("onsen_intro 1_1annoyed", initial_ypos=0.0) with dissolve

                                    mada "I have had enough of this foolishness, you have overstayed your welcome!"
                                    mada "Pick your jaw up from the floor and remove yourself from my presence at once!"
                                    scene black with dissolve
                                    call hidescrollingimage from _call_hidescrollingimage_170
                                    hide screen parallax1280 with dissolve
                                    stop music fadeout 2
                                    mada "GUARDS!!" with vpunch
                                    jump guards_onsen_thrown_out_ending

                                "{color=[hatredcolor]}I'll give you something to drool over, you bitch!{/color}":
                                    play sound "audio/soun_fx/error.opus" volume 1.0
                                    call changeHatred(1) from _call_changeHatred_199
                                    bo "I'll give you something to drool over, you bitch!"
                                    show onsen_intro 1_1annoyed with dissolve:
                                        xalign 0.5 yalign 0.0 zoom 1.4
                                    bo "Let's see if that whore mouth of yours feels better than it sounds!"
                                    mada "You insolent little worm!" with vpunch
                                    scene onsen_intro 1_1annoyed with dissolve:
                                        yalign 0.0
                                    mada "You obviously have no idea who you are addressing..."
                                    bot "*gulp* Maybe I shouldn't have said that out loud..."
                                    mada "You finally managed to find your tongue, only to utilize it so poorly and antagonize a royal concubine?"
                                    mada "Perhaps I should have it cut out and fed to the dogs..."
                                    bot "A royal concubine? Oh fuck, that doesn't sound good..."
                                    bot "Why did I think that was a good thing to say...?!" with vpunch
                                    mada "I have had enough of this foolishness, you have overstayed your welcome!"
                                    mada "Pick your jaw up from the floor and remove yourself from my presence at once!"
                                    call hidescrollingimage from _call_hidescrollingimage_171
                                    
                                    scene black with dissolve
                                    stop music fadeout 2
                                    mada "GUARDS!!" with vpunch
                                    jump guards_onsen_thrown_out_ending

                                "Beg for help" if hinata_captured ==True:
                                    jump onsen_beg_for_help_repeatable

                                "I need help relaxing tonight!" if hinata_captured == False:
                                    jump onsen_relax_repeatable

                        "Beg for help" if hinata_captured == True: 
                            jump onsen_beg_for_help_repeatable
                        
                        "I need help relaxing tonight!" if hinata_captured == False:
                            jump onsen_relax_repeatable

                "Beg for help" if hinata_captured == True:
                    label onsen_beg_for_help_repeatable:
                        call hidescrollingimage2("Click twice to beg.") from _call_hidescrollingimage2_125
                        scene onsen_intro 1_1 with dissolve:
                            yalign 0.0
                        bo "Please, you have to help me! \nThere are guards outside searching for me and I need to stay hidden!"
                        bo "As much as I always enjoy the sight of you, I'm here tonight to save [hin_rel]!"
                        bo "Will you lend me your aid Madame?"
                        jump examined_closer_repeatable

                "I need help relaxing tonight!" if hinata_captured == False:
                    label onsen_relax_repeatable:
                    bo "I need help relaxing tonight"
                    bo "The stress has been getting to me lately, and I could really use some good company to unwind and let go a little..."
                    bo "I couldn't think of a better place for that to happen, but here with you and your lovely servants!"
                    jump examined_closer_repeatable



label examined_closer_repeatable:
    scene black with dissolve
    "The Madame raises her hand as if to signify a pause in the current state of affairs. She fixes her clothing and turns to address you..."
    scene onsen_intro 1_2 with dissolve:  
        yalign 1.0 
    show onsen_intro 1_2: 
        easein 4.0 yalign 0.1
 
    mada "Is that so...?"
    mada "How is it that you always find yourself in these predicaments, little lamb..."
    if hinata_captured==True:
        mada "The circumstances surrounding [hin_name] are quite unfortunate, I must admit..."
    mada "I will be honest though... \nI'm not entirely sorry that it has led you back here before me."
    mada "How very exciting..."


    "She continues to gaze at you, seemingly scanning every inch of your appearance with as her eyes slowly move up and down your body."
    mada "A young man like you is very easy on the eyes, [bo_name]."
    mada "You really should come and visit more often..."
    "She gives you a slightly flirtatious smile, her eyes sparkling with mischief and intrigue."
    mada "I will grant you the aid that you seek, if that is what you wish..."
    mada "However, you must prove yourself worthy of it first, of course!"

    hide screen parallax1280
    
    bo "How exactly would you like me to prove myse-..."

    scene black with fade
    play sound "audio/soun_fx/footsteps.opus" volume 1.3
    "Your reply is cut short as you hear the faint thud of heavy footsteps in the outside corridor."
    "Guards" "Search every corner of every room in the vicinity, find the intruder immediately!"
    "Guards" "Do NOT let him get away!" with vpunch

    scene onsen_intro 1_2 with dissolve:
        yalign 0.1 
    mada "It seems as if we are about to have more unwanted company..."
    mada "Ladies, you are to stay put and distract any prying guards. \nMake no mention of our guest!" 
    "Servants" "Yes of course, Madame!"
    mada "[bo_name], let us continue after we have dealt with them."
    bo "Y-yes Madame..."
    mada "Make haste! Follow my lead if you know what is good for you..."
    mada "I don't like to be kept waiting!"
    
    scene bg onsen1_night with fade
    show boruto suspicious at right with dissolve
    show madame normal with dissolve:
                xalign 1.0 
                easein 3 xalign -2.0
    "She turns and swiftly walks away, disappearing out of sight behind the corner as she slips into an adjacent room."
    "You are left confused and bewildered at the unfolding of the events before you."
    show boruto surprised2 at right with dissolve
    bot "These guards just refuse to give up!" with vpunch
    show boruto suspicious at right with dissolve
    bot "Is she really going to help me? \nOr am I going to regret trusting her?"
    bot "I'm running out of options here..."

    menu:
        "Don't trust her":
            bot "This doesn't feel right..."
            bot "Maybe it was a mistake to come back here again..."
            show boruto:
                easeout 2 xpos 2000
            bot "I can't let this curse take control and make me chase every woman I see without caution!"
            scene black with dissolve
            bot "There has to be some other way without her..."
            
            scene onsen_intro 2_1 with dissolve:
                yalign 1.0
            show onsen_intro:
                easein 2 yalign 0.0
            "As you frantically look around, searching for any other options, you hear some commotion at the entrance as guards attempt to enter the area."
            "You notice the girls murmuring and glancing at you with a strange look..."
            bot "Shit! I am running out of options..."
            menu randomshitthatkeeposongivbing_menu:
                bot"Shit! I am running out of options..."
                "Jump in the onsen pools!" (supporter_scene = True):
                    $ call_label_action("randomshitthatkeeposongivbing")
                    call supp_rew from _call_supp_rew_14
                    jump randomshitthatkeeposongivbing_menu
                    label randomshitthatkeeposongivbing:
                    bot "Fuck it! When life gives you lemons..."
                    scene onsen_intro 2_1 with fade:
                        yalign 0.0
                    $ renpy.sound.play("audio/soun_fx/clothes_drop.opus", channel="sfx3", loop=False, relative_volume = 1)
                    show boruto naked1 with dissolve:
                        zoom 0.38 xalign 0.4
                    "You discard your clothes and fling them across the room!"
                    "Servants" "*Gasping in unison*"
                    bot "... You make lemonade!"    
                    scene black with dissolve
                    bot "Time to blend in and socialize a bit!"
                    "You set your eyes on a suitably free area and proceed to jump into the onsen pool!"
                    play sound "audio/soun_fx/splash1.opus" volume 1.1
                    bo "Yahoo!"
                    "You look around you, suddenly finding yourself surrounded by naked women!"
                    jump jumpingpoint_jumppool_repeatable
                    
                "Make a run for it!":
                    pass
            jump guards_onsen_thrown_out_ending

        "Follow her":
            bot "I can never know what her true intentions are, but I have no choice but to trust her for now."
            show boruto suspicious:
                easein 3 xalign -2.0
            scene black with fade
            play sound "audio/soun_fx/footsteps.opus" volume 0.8
            "You quickly follow in the footsteps of Madame deeper into her chambers."
            scene onsen_intro 2_2 with dissolve:
                yalign 1.0
            show onsen_intro:
                easein 2 yalign 0.0
            "As you round the corner she had gone past, she approaches you again with a towel in hand." 
            mada "Quickly, do as I say, and you may yet make it out alive!"
            mada "Undress immediately and discard your clothes! NOW!" with vpunch
            bo "What!?" with vpunch
            mada "You heard me..."
            mada "I said to undress, not to ask pointless questions!"
            scene black with dissolve
            play sound "audio/soun_fx/clothes_drop.opus" volume 0.8
            "You hesitate before swiftly removing all your garments and throwing them off to the side out of sight."
            mada "Now, sit down and follow my lead..."

            scene onsen_intro 3 with dissolve:
                yalign 0.5
            show screen parallax1280("onsen_intro 3", initial_ypos=0.5)
            call showscrollingimage from _call_showscrollingimage_210
            "The Madame quickly covers your manhood with a towel, wraps your head in another, and gets down on her knees..."
            mada "Now is the time for you to sit still and not utter a word until I say it is safe."
            if onsen_stared == True:
                mada "Fortunately you have already proven that you are capable of remaining uselessly silent, so I trust that it will come naturally to you now as well."
            "She slowly moves her body up and down, rubbing her chest across your groin..."
            mada "Do we have an understanding?"
            call hidescrollingimage from _call_hidescrollingimage_172
            hide screen parallax1280

            menu:
                "Nod your head":
                    jump onsen_nod_head_repeatable

                "{color=[hatredcolor]}Deviously nod your head{/color}": 
                    call changeHatred(1) from _call_changeHatred_200
                    bot "The arrogance on this fucking whore to tell me what to do..."
                    bot "I'll play along for now bitch... But my patience is wearing thin with you!"
                    bot "At the first possible opportunity, I intend to make you pay!"
                    $ hatred_nod = True
                    jump onsen_nod_head_repeatable
            
label onsen_nod_head_repeatable:
    "You nod your head in agreement..."
    "You tense up momentarily as her skin comes into contact with yours... But the rubbing sensation offers a sense of comfort, as you slowly let your guard down and relax."
    play sound "audio/soun_fx/footsteps.opus" volume 0.8
    mada"{size=*0.7}Here they come. Hush now...{/size}"
    show onsen_intro 3_1 with dissolve:
        zoom 1.1 yalign 0.0 xalign 1.0
    "Guard" "M-my lady! Excuse the intrusion but... have you perchance spotted a-"
    mada "You imbeciles! You dare barge into MY private chambers?" with vpunch
    "Guard" "This is an emergency, my lady! There's been an intrusion!"
    mada "Can't you see I am in the middle of servicing a welcomed guest?"
    mada "Out, NOW!" with vpunch
    mada "We shall continue this conversation outside privately you fools..."
    
    scene black with fade
    "You remain seated while the guards are forcefully shooed out of the room, bewildered by the sudden outburst of the concubine..."
    scene bg onsen1_night with dissolve
    show madame normal2 at left
    show demandingmen badguys1:
        xpos 0.5
    with dissolve
    "Guard" "M-madame, there must be some mistake..."
    "Guard" "We have only come to enforce your safety and that of the palace!"
    "Guard" "Allow us to handle the intruder and remove him from the grounds immediately!"
    show madame angry at left with dissolve
    mada "You will do no such thing!" with vpunch
    mada "How dare you threaten and insult an esteemed guest of the Daimyo!"
    "Guards" "W-wha-...? Madame..."
    
    mada "All you babbling baboons are the same..."
    mada "You all share the single collective brain cell that was given to only ONE of you at birth!"
    mada "I will not tolerate you unkempt brutes sullying this enclave with your filthy and unwarranted presence!"
    mada "Be gone immediately!" with vpunch
    show demandingmen badguys1:
        easein 2 xpos 0.55
    "The guards are taken aback by the unexpected pushback that the concubine is administering, and look to each other confused on how to respond to the onslaught of insults being hurled their way."
    
    "Guard" "M-my lady, I beg of you..."

    mada "Are you arguing with me?" with vpunch
    "Guard" "N-no my lady, of course not...!"
    mada "Did I stutter then? Or perhaps you are hard of hearing?"
    mada "Disobey my order to leave again, and I will have the Daimyo ornament the courtyard with your heads on pikes!" 
    mada "Be gone I said!" with vpunch
    show demandingmen badguys1:
        easein 1 xpos 0.6
    "Guards" "Y-yes my lady, at once my lady... F-forgive us..."
    
    show demandingmen badguys1:
        easeout 2 xpos 3.0
    play sound "audio/soun_fx/footsteps.opus" volume 0.8
    "Defeated and bewildered, the guards rush to take their leave from the onsen."
    "They are not completely convinced, but have no choice but to comply with the concubine's orders... For now..."

    


    show madame normal2 with dissolve:
        easein 1.0 xalign 0.5
    mada "Now, where were we..."
    scene black with dissolve

    if hatred_nod == True:
        "Madame returns to you and attempts to regain her composure, taking a deep breath before makking an attempt to continue addressing you."
        "You watch as she hesitates, and a slow smirk emerges on the corner of your lips..."
        bot "Tick tock... Your time is up now, bitch!"
        "Sensing an opportune moment with the guards having left, you decide to take advantage of her momentary lapse in focus and grab her by the hair!"
        mada "W-what in the world do you think you're doing?!" with vpunch
        bo "You just never know when to shut the fuck up, do you?!"
        show onsen_intro hatred1 with dissolve:
            yalign 0.0
        show onsen_intro hatred1:
            easein 3 yalign 0.5
        $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 0.7)
        "You discard your towel and drag her across the room to the nearest bed, yanking her head forcefully towards your now fully erect cock!"
        bo "Get your fucking ass on this bed...!" with vpunch
        bo "I've had enough of your attitude and your games! \nYou will learn to respect me the hard way now..."
        bo "Starting with something VERY hard in that fucking mouth of yours!"
        scene black with dissolve
        mada "THAT'S ENOUGH!" with vpunch
        "Madame finally comes back to her senses and puts up a real struggle against your unprovoked aggression."
        "She frees herself from your grasp with a final heavy shove to your chest!"
        show bg onsen1_night
        show madame angry at center
        mada "I have never been so humiliated in my life!"
        mada "I don't know what has suddenly come over you, or why you considered this appropriate... But I will not tolerate it!"
        mada "You are to leave immediately, never to return!"
        $ onsen_blocked = True
        stop music fadeout 2
        hide madame with dissolve
        mada "GUARDS!!" with vpunch
        jump guards_onsen_thrown_out_ending

    "Madame having dealt swiftly with the guards, regains her composure and returns her attention to you."
    scene onsen_intro 2 with fade
    show onsen_intro 2:
        easein 4.0 yalign 0.0
    "She leans back against the wooden guard rail, locking eyes with you..."
    "A faint smile apparent on her lips, hinting towards being pleased with the outcome of her performance."
    bo "T-thank you, for covering for me Madame..."
    bo "Who knows what would have happened to me without your help..."    
    mada "I know exactly what would have happened, which is why I decided to get involved."
    mada "The guards will still be roaming the premises for some time..."
    mada "It would be in your best interest if you remained here in silence, and in secret, for the time being..."
    bo "U-understood."
    mada "I will be blunt with you [bo_name], it is not entirely safe for you in the palace grounds..."
    mada "You put yourself at great risk if you think you can take on the great Daimyo and his men all by yourself!"
    mada "While I can respect the courageous effort and good intentions... \nCourage can only get you so far!"
    if hinata_captured == True:
        mada "Your [hin_rel_mother] truly is a remarkable woman, a graceful and kind soul..."
        mada "I share quite a unique bond with her, and would never wish any harm upon her."
        mada "She truly is as amazing as my sources have always made her out to be! \nWe get along effortlessly..."    
        mada "I always try to guide her to the best of my ability in her endeavours here with the Daimyo..."
        mada "Sometimes I am successful, other times... Not so much..."
        mada "His Highness is a cruel man that does not tolerate being undermined... He goes along through his affairs by treating his subjects as simple cattle to be herded."
        mada "While normally I am against such sentiments... \nYou must understand that being here has indeed turned you into a sacrificial lamb, ready to be slaughtered yourself!"
    else:
        mada "You must truly be drawn to me and my onsen to risk such danger without a second thought!"
        mada "I am not sure what it is exactly that you seek here tonight, but know that you are always welcome here in my sanctuary."
        mada "Me and my servants will be at your disposable to help alleviate any burden that you may be carrying."


    

    show screen parallax1280("onsen_intro 2", menuenabled=True) with dissolve
    call showscrollingimage from _call_showscrollingimage_211
    "The adrenaline is still pumping through your veins... but as tension and tempers have subsided, you look around you and start to take in your surroundings."
    "You notice the sparkling moonlight reflecting off the surface of the water, giving Madame's outline an almost angelic glow and accentuating the pale complexion of her skin..."
    "Steam from the heated pools, while not bothering your half-naked self, has made her skin glisten with beads of sweat... Dripping from her chin and streaming down her breasts, into the folds of her garments."
    
    bot "Fuck me, I only had time to admire her ass before... \nBut from the front she is just as stunning!"
    
    menu:
        "Stare at her tits":
            hide screen parallax1280 
            show onsen_intro 2:
                zoom 1.5 yalign 0.4
            with fade
            call increaselust(10) from _call_increaselust_274


            if onsen_stared == True: 
                bot "I just can't help myself, can I? At every opportunity..."
            
            bot "Look at those beautiful breasts... \nWho could possibly blame me for looking?"
            show screen parallax1280("onsen_intro 2") with fade
            bot "No wonder the Daimyo considers everyone cattle... \nHe has gorgeous concubines with massive milkers just prancing around the palace!"
            bot "I would probably feel the same way if I could watch them bouncing up and down all day!"
            bot "Damn, they're so nice to admire that I even forgot to blink for a second there...!"
            hide screen parallax1280 with fade

            show screen parallax1280("onsen_intro 2",menuenabled=True) with fade

            mada "Is something distracting you, little lamb?"
            bo "O-oh U-uhhm... No...!"
            bot "Shit, I mustn't get carried away like that..."

            menu:
                "Why do you help me?":
                    jump onsen_why_help_me_repeatable

        "Why do you help me?":
            jump onsen_why_help_me_repeatable
            
label onsen_why_help_me_repeatable:

    bo "Why exactly do you help me, Madame?"
    bo "You claim to have aided my [hin_rel_mother] too..."
    bo "What the hell is going on in this palace? \nAnd what is your part in all of this?!"
    
    mada "All will be revealed in time, do not get ahead of yourself [bo_name]."
    mada "As for why I am helping you escape the guards..."
    mada "Let us just say that I do not want the Lady of the Leaf to be devastated by anything happening to you..."
    mada "The exact reasons of my allegiance and sympathy to her are none of your concern for now, and it is getting quite late..."
    mada "I will retire to my private chambers for the night to relieve the stress of tonight's adventure."
    mada "I suggest you lay low here momentarily, before making your way back home."
    if hinata_captured==True:
        bo "Back home?? I have to help my [hin_rel_mother], I can't just leave her here!" with vpunch
    mada "My servants will tend to you here, you are welcome to bathe and relax in their company."
    mada "Tend to him if he so wishes ladies, but do not delay his departure for long. I will not be here to prevent the guards from capturing him a second time..."
    "Servants" "Yes Madame, we will take care of him as per all your teachings."
    mada "Excellent, I entrust him now onto you then... \nEnsure his swift departure is safe and in good spirits."
    mada "I bid you farewell then, for now..."
    scene black
    call hidescrollingimage from _call_hidescrollingimage_173
    hide screen parallax1280 with fade

    "Madame heads off to retreat to her private quarters, leaving you alone by the pools."

    if hinata_captured == True:
        scene onsen_intro 2_1 with fade:
            yalign 0.0
        show boruto towelmad with dissolve:
            xalign 0.4
    
        bo "Wait! What about [hin_rel]?? \nI can't just leave her here, you have to help me!" with vpunch
        show boruto at smallshake
        bot "Crap! She completely ignored me..."
        bot "Surely she is capable of helping with more, right?"
        bot "She told me to keep a low profile here... "
        bot "But I can't just sit around and do nothing!" with vpunch

    else:
        scene onsen_intro 2_1 with fade:
            yalign 0.0
        show boruto towelmad with dissolve:
            xalign 0.4
        bot "It was rather rude of her to leave me alone here, I was expecting better hospitality from her..."
        show boruto at smallshake
        bot "Does she not care about my company at all?"
        bot "She told me to keep a low profile here..."
        bot "But maybe I should follow her and demand some more attention from her!"

    menu lkjashdfl23984_3:
        "Relax in the pool with the servants"(supporter_scene = True):
            $ call_label_action("pool_service_repeatable")
            call supp_rew from _call_supp_rew_15
            jump lkjashdfl23984_3        
            label pool_service_repeatable:
            show boruto towelsmirk with dissolve:
                xalign 0.4
            if hinata_captured== True:
                bot "Fuck it, I deserve some relaxation after all that mess!"
            else:
                "Fuck it, I deserve some relaxation with or without her!"
            scene onsen_intro 2_1 with fade:
                yalign 0.0
            show boruto naked1 with dissolve:
                zoom 0.38 xalign 0.4
            "You discard the towel from your waist and ready yourself to jump in the onsen surrounded with naked women!"
            "Servants" "*Gasping in unison*"

            bot "A dip in a hot pool with hot servants sounds like just what I need right now..."
            
            scene black with dissolve
            play sound "audio/soun_fx/splash1.opus" volume 0.8
            bo "Yahoo!"
            label jumpingpoint_jumppool_repeatable:
            "Servant" "{size=*0.8}Did you see that? The boy's hung!{/size}"
            "The girls quietly whisper to each other while stealing glances at you..."
            "Not before long, some of them quickly approach you!"
            show jumponsen_intro1 with dissolve:
                yalign 0.0
            show jumponsen_intro1:
                easein 2 yalign 1.0
            $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
            bo"L-ladies...?" 

            if pool_complete == False:
                "Older Servant" "We don't often get younglings to keep us company... *Giggles*"
                "Younger Servant" "And a stud no less! You reckon you could be my first?"
                bo"Your f-first, huh?"

                show jumponsen_intro1_1 with dissolve:
                    yalign 0.0
                show jumponsen_intro1_1:
                    easein 2 yalign 1.0
                $ renpy.sound.play("/audio/soun_fx/water_move_2.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                "Older Servant" "Don't tease our guest, you lousy fox! \nWe all know you've slept with hundreds of men..."
                "Younger Servant" "And all of them were unkempt, fat, and old! \nHe will be my first that I enjoy {i}tonight{/i}! *giggles*"
                "Older Servant" "You are such a brat, you know that? \nWhy don't we let the handsome young man decide who he prefers?"

            else:
                "Older Servant" "Welcome back, handsome..."
                "Younger Servant" "*giggle* Did you miss us?"
                bo "Of course, you ladies are the whole reason I'm here!"
                "Older Servant" "Oh my... I was hoping you'd say that..."
                show jumponsen_intro1_1 with dissolve:
                    yalign 0.0
                show jumponsen_intro1_1:
                    easein 2 yalign 1.0
                $ renpy.sound.play("/audio/soun_fx/water_move_2.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                "Older Servant" "We've been craving more of you since the moment you last left!"
                "Younger Servant" "I can't wait to have you all to myself tonight!"
                "Older Servant" "Hush, you lousy fox! Who said you could have him all to yourself?"
                "Older Servant" "Why don't we let him decide for himself who he prefers to be serviced by tonight?"


            menu:
                bot "Who do I prefer to be entertained by?"
                "Have some fun with the younger and enthusiastic servant!":
                    $ servchoice = "Younger Servant"
                    bo "I think I would enjoy some energetic company right now!"
                "Have some fun with the older and experienced servant!":
                    $ servchoice = "Older Servant"
                    bo "I think I would enjoy a more experienced touch right now!"
            servchoice "Oh, naughty boy! I knew you would pick me!"
            servchoice "But first..."
            show jumponsen_intro 1_3 with fade: 
                yalign 0.0
            $ renpy.sound.play("/audio/soun_fx/water_move_3.opus", channel="sfx1", loop=False, relative_volume = 0.5)
            servchoice "We need to prepare you together..."
            show jumponsen_intro 1_3:
                easein 2 yalign 1.0
            $ renpy.sound.play("/audio/soun_fx/handjob3.opus", channel="sfx2", loop=True, relative_volume = 0.6)
            bo "What exactly do you mean by t-togeth... O-oh..."
            bot "Fuck, that grip feels good!" with vpunch
            show screen parallax1280("jumponsen_intro 1_3", initial_ypos=1.0)
            call showscrollingimage from _call_showscrollingimage_212
            servchoice "Just sit back and relax for me..."
            servchoice "Is the water to your liking? \nAre you enjoying yourself here between the naked bodies of two gorgeous women?"
            bo "Y-yes... Everything is amazing!"
            servchoice "Let the steamy waters wash away all your stress and troubles, while we wash this perfect cock of yours..."
            "Younger Servant" "I've never seen anything quite like it before!"
            "Older Servant" "It is quite impressive... And I bet it feels just as amazing as it looks..."
            servchoice "I'm getting so wet thinking about what's coming next...!"
            bo "N-next? W-what happens n-next?!"
            $ renpy.sound.play("/audio/soun_fx/water_move_4.opus", channel="sfx1", loop=False, relative_volume = 0.5)
            show screen parallax1280("jumponsen_intro 1_4", initial_ypos=1.0) with dissolve 
            $ renpy.sound.play("/audio/soun_fx/handjob4.opus", channel="sfx2", loop=True, relative_volume = 0.6)

            servchoice "*giggles* What do you think, silly?"
            servchoice "I thought it was very clear that we are here to tend to your needs..."
            servchoice "Which basically means..."
            servchoice "You're obviously going to fuck me!"
            bo "F-fuck you!?" with vpunch
            bot "Ah yes, this is going exactly the way I was hoping it would...!"
            $ renpy.sound.play("/audio/soun_fx/handjob3.opus", channel="sfx2", loop=True, relative_volume = 0.6)

            servchoice "You heard me! Don't pretend you don't want to... \nI can feel your cock pulsing and twitching in anticipation..."
            servchoice "It's making me tingle all over just feeling it!"
            servchoice "So hard and thick in my hands too... You're ready for me, I sense it..."            
            servchoice "F-fuck, I need it NOW!" with vpunch
            scene black with dissolve

            call hidescrollingimage from _call_hidescrollingimage_174
            
            show jumponsen_intro 2 with vpunch
            $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
            $ renpy.sound.play("/audio/soun_fx/kiss1.opus", channel="sfx2", loop=True, relative_volume = 1)
            "Before you can react or even say a word, she pushes you back and lunges at your face with her lips!"
            bo "... M-mmmm?!"
            if servchoice == "Older Servant":
                bot "Woah! This hungry cougar is on the prowl!"
                bot "She seems to know what she wants and how to get it, I definitely made the right decision with her...!"
            elif servchoice == "Younger Servant":
                bot "Woah! She's a feisty little thing!"
                bot "She seems very eager to attend to me and please me, I definitely made the right decision with her...!"
            show jumponsen_intro 2_1 with dissolve
            $ renpy.sound.play("/audio/soun_fx/kiss2.opus", channel="sfx2", loop=False, relative_volume = 1)
            servchoice "Mmhmm... ♡♡"
            bot "Fuck she's such a good kisser too..."
            bot "That tongue of her is incredible!"
            show jumponsen_intro 2_2 with dissolve
            $ renpy.sound.play("/audio/soun_fx/kiss1.opus", channel="sfx2", loop=True, relative_volume = 1)
            "You allow her to pour all her affection and desire into you, her lips dancing on yours with a fiery passion as she moans with every kiss!"
            "Your body is on the verge of complete relaxation as your eyes close shut, and you begin to lose yourself in the moment..."
            "The world and your surroundings dissolve as darkness closes in around you, the serene sound of flowing waters sending you into a trance as the servant unrelentingly offers herself to you."
            $ renpy.sound.play("/audio/soun_fx/kiss2.opus", channel="sfx2", loop=True, relative_volume = 1)
            "The heat of her body and the sweet taste of her saliva on your tongue overload your senses, as she mounts you and wraps her legs around your waist."
            menu randommenu_onsenpool_repeatable:
                bot "This must be what heaven feels like..."
                "Grab her ass and pull her in!":
                    show jumponsen_intro 2_3 with dissolve
                    $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                    "You let your hand explore the servant's body as your lips remain interlocked..."
                    "It finds its final resting spot upon her ass cheek, as you start to squeeze instinctively... You grip it tight and pull her towards you, inviting her closer..."
                    servchoice "*moans* ♡ Yesss, I know... More... You want more! ♡"
                    show jumponsen_intro 3 with dissolve
                    $ renpy.sound.play("/audio/soun_fx/water_move_2.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                    "She lifts herself towards you as she leans forwards... \nEffortlessly gliding through the water with the pull of your hands on her body."
                    "You feel her soft breasts pressed against your own chest as you grope her, her wet body creating ripples in the pool as she repositions herself."
                    "Your clenched fingers spread her ass cheeks wide open to expose her dripping wet pussy, as she moans softly under her breath..."
                    servchoice "A-ah yess ♡... Those strong hands feel so good on my body..."
                    $ renpy.sound.play("/audio/soun_fx/water_move_4.opus", channel="sfx1", loop=False, relative_volume = 0.5)

                    servchoice "I want them... I want you... All over me... ♡"
                    $ renpy.sound.play("/audio/soun_fx/water_move_3.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    show jumponsen_intro 3_1 with dissolve:
                        yalign 0.0
                        easein 3 yalign 1.0 
                    servchoice "But more importantly..."
                    show jumponsen_intro 3_2 with fade:
                        yalign 1.0
                    $ renpy.sound.play("/audio/soun_fx/pushitin1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                    servchoice "I want you INSIDE me!" with vpunch
                    show screen parallax1280("jumponsen_intro 3_2", initial_ypos=1.0) with dissolve
                    call showscrollingimage from _call_showscrollingimage_213
                    servchoice "A-ahhh, y-yeees... Exactly what I was craving..."
                    call hidescrollingimage("Click twice to start pounding her!") from _call_hidescrollingimage_175
                    scene black with dissolve
                    $ renpy.sound.play("/audio/soun_fx/splash1.opus", channel="sfx3", loop=False, relative_volume = 1)
                    $ renpy.sound.play("/audio/soun_fx/femalemoan1.opus", channel="sfx1", loop=True, relative_volume = 3)  
                    $ renpy.sound.play("/audio/soun_fx/pushitin1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                  
                    show screen parallax1280("jumponsen_intro 3_3", initial_ypos=1.0) with vpunch
                    call showscrollingimage from _call_showscrollingimage_214
                    $ renpy.sound.play("/audio/soun_fx/sexslaps2.opus", channel="sfxstat", loop=True, relative_volume = 1.0)
                    bo "F-F-FUCKKK!" with vpunch
                    servchoice "That's it... Keep fucking me you stud...!" with vpunch
                    $ renpy.sound.play("/audio/soun_fx/pushitin1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                    servchoice "Give me all of it... " with vpunch
                    $ renpy.sound.play("/audio/soun_fx/femalemoan2.opus", channel="sfx1", loop=True, relative_volume = 2)
                    servchoice "Y-YES!!" with vpunch
                    servchoice "Let that big hard cock deep into my tight pussy!♡" with vpunch
                    bo "A-ahhh... F-fuuuck..." with flash
                    $ renpy.sound.play("/audio/soun_fx/pushitin1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                    bo "It's gripping me so t-tightly..." with vpunch
                    bo "F-feels so fucking g-good..." with vpunch
                    show screen parallax1280("jumponsen_intro 3_5", initial_ypos=0.5) with dissolve
                    $ renpy.sound.play("/audio/soun_fx/femalemoan1.opus", channel="sfx1", loop=True, relative_volume = 3)
                    servchoice "Your e-every thrust..." with vpunch
                    $ renpy.sound.play("/audio/soun_fx/pushitin1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                    show screen parallax1280("jumponsen_intro 3_5_1", initial_ypos=0.5) with dissolve
                    servchoice "S-so DEEP inside of me..." with vpunch
                    show screen parallax1280("v020_servant_sex_anim", initial_ypos=0.5) with dissolve
                    servchoice "Hitting all the right spots...♡" with vpunch
                    servchoice "AGHHH F-FUUUCK M-ME! ♡" with vpunch
                    "You keep hammering away from beneath her, thrusting your hips upwards while she guides your cock deeper inside her."
                    $ renpy.sound.play("/audio/soun_fx/pushitin1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                    servchoice "*pant* F-FUCK YES, ALL THE WAY! ♡" with vpunch
                    call hidescrollingimage("Click twice to fuck her harder!") from _call_hidescrollingimage_176
                    show v020_servant_sex_animfast with dissolve:
                        yalign 1.0
                    "You heed her call, and do your best to satisfy her demands. Your rapid piston movements create ripples throughout the onsen!"
                    "The sound of her moans echo across the pools as she gets her hole stuffed, drawing looks of envy and lust from all the nearby spectators."
                    bo "I-I... I am c-close!" with flash
                    $ renpy.sound.play("/audio/soun_fx/pushitin2.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                    servchoice "Don't hold it in! Cum for me baby! I want it all inside of me!"
                    $ renpy.sound.play("/audio/soun_fx/pushitin1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                    $ renpy.sound.play("/audio/soun_fx/femaleorgasm.opus", channel="sfx1", loop=False, relative_volume = 1)
                    scene black
                    bo "F-FUCK I'M CUMMING!" with flash
                    $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                    stop sfxstat fadeout 1
                    show screen parallax1280("jumponsen_intro 3_5_2", initial_ypos=1.0) with longerflash
                    call showscrollingimage from _call_showscrollingimage_251 
                    bo "AGHHHH! ♡! *Loud Moans* ♡♡" with vpunch
                    call hidescrollingimage from _call_hidescrollingimage_177  

                    show jumponsen_intro 3_after with dissolve
                    $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)

                    servchoice "Fuck yeah, that's so hot♡! I can feel it dripping out of me..."
                    servchoice "Thank you for indulging me. I don't often get to have this much fun, let alone getting stretched by a young stud!"
                    "She playfully kisses you on the forehead while you catch your breath and regain post-nut clarity."

                    show screen parallax1280("jumponsen_intro 3_4", initial_ypos=0.5) with fade 
                    call showscrollingimage from _call_showscrollingimage_215
                    $ renpy.sound.play("/audio/soun_fx/water_move_2.opus", channel="sfx1", loop=False, relative_volume = 0.5)

                    bo "I-I'm so sorry, I lost control, I should have pulled out..."
                    servchoice "Don't be silly cutie... It's exactly what I wanted...♡"
                    servchoice "Besides... Bathing in the heated pools prior to all our fun makes it perfectly safe."
                    servchoice "Think of it as a natural contraception, you won't be impregnating me here... Not unless we REALLY want it to happen! *wink*"
                    if pool_complete==False:
                        bo "O-oh, wow ok... I had no idea, but that's definitely good to know!"
                    else:
                        bo "O-oh yeah... I completely forgot about that, but it's still good to know!"
                    bot "Phew, I guess I got lucky there... \nBut I shouldn't make a habit of doing that!"
                    bot "I don't think it's quite the time to think about being a father right now, especially not with random women!"
                    servchoice "Did I leave you speechless? Come now, let's get you cleaned up!" with vpunch
                    scene black with dissolve
                    call hidescrollingimage from _call_hidescrollingimage_178
                    jump pool_ending

                    

                
                # "???" if pool_complete == False: # Options for repeated returns
                #     "This option is unavailable to you right now, work in progress!"
                #     jump randommenu_onsenpool_repeatable

                # "???" if pool_complete == False: # Options for repeated returns
                #     "This option is unavailable to you right now, work in progress!"
                #     jump randommenu_onsenpool_repeatable

                # Extra options not implemented yet

                # "Use her feet!" if pool_complete == True: # Jumps to repeated version where it is available
                #     jump pool_feet

                # "Bend her over!" if pool_complete == True: # Jumps to repeated version where it is available
                #     jump pool_bendover


        "Follow Madame to her private quarters":
            if hinata_captured==True:
                bot "She's delusional if she thinks I'm just going to abandon [hin_rel] like this!"
                bot "Now where did I leave my clothes again...?"
            else:
                bot "I should follow her and see what she has to say..."
                bot "Maybe I can get her to help me herself!"
            
            scene black with dissolve
            play sound "audio/soun_fx/clothes_dress.opus" volume 0.8
            "You quickly dress and rush after Madame in the direction she left from, following in her footsteps to locate the private quarters she mentioned."
            play sound "audio/soun_fx/doorclose.opus" volume 0.8
            "You hear a door click closed off to the side and determine that it must have been her..."
            play sound "audio/soun_fx/dooropen.opus" volume 0.8
            "Without skipping a beat, you slip into the room yourself and close the door behind you... \nYou're greeted by the welcomed sight of Madame yet again before you."

            scene onsen_intro 4 with dissolve
            show onsen_intro 4:
                easein 4.0 yalign 0.0

            "Servant" "Hey! You can't be in here!"
            mada "Do you not know the definition of the word private, little lamb?"
            mada "It seems as if your explorations have led you straight into the lion's den... And I happened to have built up quite the appetite tonight."
            mada "Tell me... \nWere my faithful servants not to your liking?"
            mada "I suggest you head back to the pools before my patience with you dwindles too thin..."

            menu:
                "I'm not leaving!":
                    bo "I'm not leaving Madame!" with vpunch
                    if hinata_captured:
                        bo "I came here to find [hin_name], and I will not leave until I do!"
                        bo "If what you said is true and you share a bond with her, then you have to help me!"
                        bo "If not for me... "
                        bo "Then do it for her!" with vpunch
                        mada "Foolish boy, you have no idea with what you're meddling with!"
                        mada "Your overwhelming arrogance and blind confidence will be the end of you..."
                        mada "You will end up in a cell right opposite your beloved [hin_rel_mother], except... You will be the only one to remain there, beaten and bruised, left to rot and degrade into dust!"
                    else:
                        bo "You claim to want to help me, but you abandoned me by the pools!"
                        bo "I came here specifically for your company, Madame..."
                        bo "Don't just turn me away!"
                        mada "You arrogant little boy, do you really think that the world revolves around you and your desires?"


                    menu:
                        "{color=[hatredcolor]}You fucking bitch!{/color}":
                            call changeHatred(2) from _call_changeHatred_201
                            bo "You fucking bitch!" with vpunch
                            bo "You talk to me about arrogance while you walk around with your nose pointed to the sky and a stick up your whore ass!"
                            bo "You're nothing but a fucking hypocrite, only capable of worthless criticism and being bred like the royal slut you are!"
                            
                            show black with fade
                            "Servants" "*gasp*"
                            show bg onsen1_night with dissolve
                            show madame angry with dissolve
                            mada "You dare raise your voice and address me in that manner?!" with vpunch
                            mada "There is no room here for insolent little worms such as yourself."
                            mada "Clearly, I was mistaken for aiding such a brat..."
                            mada "A mistake that I will immediately correct!"
                            mada "Leave this area and never return!"
                            $ onsen_blocked = True
                            
                            scene black with dissolve
                            stop music fadeout 2
                            mada "GUARDS!!" with vpunch
                            jump guards_onsen_thrown_out_ending

                        "Please!":
                            bo "Please! I beg of you Madame..."
                            if hinata_captured==True:
                                bo "Just point me in the right direction, and whatever happens after that will be my burden to bear."
                                bo "If I am caught then so be it, it will be the consequences of my own actions... But I owe it to her to at least try!"
                            else:
                                bo "I crave your attention like nothing else in this world..."
                                bo "You promised to help if I deemed myself worthy..."
                                bo "So here I am before you, to prove to you that your company is not wasted on me!"
                            "Madame draws a long breath and hesitates for a second before replying, clearly contemplating her next words with caution..."
                            "Her gaze softens and she regains her composure, a wave of what appears to be genuine sympathy washes over her features."
                            "While visibly annoyed with your stubbornness, she can't help but be slightly impressed with your perseverance..."
                            
                            mada "Very well... If that is your wish..."
                            
                            "You let out a sigh of relief..."
                            bot "Finally..."
                            
                            mada "I will offer my aid to you this evening."
                            mada "However..."
                            mada "Seeing as how I have already gone out of my way to help you tonight as it stands..."
                            mada "I think a little... Repayment... Is in order first.... \nDon't you agree, little lamb?"
                            
                            bot "Why the fuck does she keep calling me that?"
                            bo "Yes, of course... I suppose that sounds reasonable to me..."
                            bo "What exactly did you have in mind?"
                            
                            mada "Ladies, you are dismissed for tonight, you will not be needed anymore."
                            "Servants" "Yes, Madame!"
                            
                            scene black with dissolve
                            play sound "audio/soun_fx/footsteps.opus" volume 0.6
                            "You watch as the servants scurry out of the room, leaving the two of you alone for the first time tonight."
                            
                            show screen parallax1280("onsen_intro 4_0", 1.25, menuenabled=True) with dissolve
                            call showscrollingimage from _call_showscrollingimage_216
                            "Madame lays down on the bed, resting her head on the soft pillows as she gazes at you with a sultry look in her eyes."
                            mada "Now, little lamb... I have a simple proposition for you."
                            if madamemassage_success == True or madamemassage_fail == True:
                                mada "I seem to recall your affinity for being quite the masseur..."
                            else:
                                mada "I seem to recall [hin_name] mentioning how her [hin_rel_to_bo] was quite the masseur..."
                                mada "How he often helps her relieve stress..."
                            mada "My terms are simple..."
                            mada "You are to prove these claims to me, by servicing me to the best of your capability."
                            if madamemassage_success == True or madamemassage_fail == True:
                                bot "She's looking forward to another massage!"
                                bot "I like where this is heading..."
                            else:
                                bot "HUH?! She wants me to SERVICE her?" with vpunch
                                bot  "Is this really happening...?!"
                            mada "If I am satisfied, then I will in turn satisfy whatever needs you may have of me..."
                            if hinata_captured==True:
                                mada "Regarding your [hin_rel_mother] of course, or perhaps even others...!"
                            "The Madame's gaze drift downwards towards your crotch where it lingers for some time..."
                            mada "It's such a pity that I do not have any oil lying about here to aid you, you will sadly have to take your time and do without..."
                            mada "Show me, little lamb... Are you really as worthy as you think you are?"
                            mada "Do you think that you are up to the task?"

                            menu randommenu21384923984_repeatable:
                                mada "Do you think that you are up to the task?"
                                "I will do my best" if massageknowledge ==0:
                                    $ madame_massage_certainfail = True #Block completion of mini-game
                                    bo "I will do my best to meet your standards Madame, I'm confident that you won't be disappointed!"
                                    bo "I do happen to have a small request though..."
                                    mada "Yes? Go on..."
                                    bo "Once you're satisfied, you stop calling me little lamb!"
                                    call hidescrollingimage from _call_hidescrollingimage_179
                                    hide screen parallax1280
                                    jump massage_minigame_start

                                "{color=[obediencecolor]}I am indeed, a master masseur!{/color}" if massageknowledge >= 1:
                                    $ madame_massage_certainfail = False #Allow completion of mini-game
                                    bo "You're in luck, I happen to be a master masseur!"
                                    bo "I make miracles happen with these fingers that leave women screaming for more, so you're in for a treat!"
                                    mada "Is that so? Let us see then if you can meet the high expectations that you set..."
                                    bo "I'll have you moaning my actual name instead of 'little lamb' to me in no time!"
                                    call changeDominance(1) from _call_changeDominance_122
                                    call hidescrollingimage from _call_hidescrollingimage_180
                                    hide screen parallax1280
                                    jump massage_minigame_start
                                
                                "{color=[obediencecolor]}???{/color}" if massageknowledge == 0:
                                    "Find a way to increase your massage knowledge to unlock this option!"
                                    jump randommenu21384923984_repeatable


