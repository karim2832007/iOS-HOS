default onsen_stared = False
default onsen_stared_long = False
default borutocaptured_d14 = False
default poolservice_d14 = False
default madamemassage_success = False
default madamemassage_fail = False
default madamereward_denied = False
default madamemassage_domreward = False
default onsen_blocked = False
default servchoice = "Older Servant"
default pool_complete = False
default hatred_nod = False
default onsen_information_attempt_done = False

init python:
    # Corrected version of the function
    def play_music_if_not_playing(track, fadein_time=1.0, volume=1.0):
        """
        Plays a music track if it's not already playing.
        Can also specify fade-in time and relative volume.
        """
        # The check remains the same
        if renpy.music.get_playing() != track:
            # Step 1: Play the track. The 'volume' argument is removed from here.
            renpy.music.play(track, fadein=fadein_time)
            # Step 2: Immediately set the volume for the 'music' channel.
            renpy.music.set_volume(volume)

label ch1_d14_onsen: # For repeatable version jump to ch1_d14_onsen_repeatable instead

    if onsen_blocked == True:
        bo "I can't enter! I don't think I am welcome in there anymore..."
        jump jumpbackdaimyoquarters
    label ch1_d14_onsen_replay:
    $ initialize_replay_defaults()
    show palace3_night with dissolve:
        zoom 1.1
    $ play_music_if_not_playing("audio/ost/Senya.opus", volume=0.5)
    show palace3_night:
        subpixel True 
        easein 5 zoom 1.3 xalign 0.5 yalign 1.0
    "You hear what sounds like a woman's voice resonating from the area as you begin to enter."
    show boruto surprised at center, with dissolve
    bot "Fuck, there's someone over there too!" with vpunch
    show boruto worried with dissolve
    bot "Too late to turn back now, the guards are on my tail!"
    if borutoknockedoutlove == True or borutoknockedouthatred == True:
        show boruto embarassed with dissolve
        bot "I don't want to get knocked out again like the last time, those bastards really are tough!"
    show boruto suspicious with dissolve
    bot "It doesn't sound like a guard at least, I have no choice now but to take my chances with this..."
    
    menu:
        "Rush inside":
            play sound "audio/soun_fx/footsteps.opus" volume 1.2
            scene blackscreen with fade
            "You burst into the onsen in a hurry, glancing back one last time to ensure you weren't spotted."
            show bg onsen1_night with dissolve
            show boruto surprised2 at left with dissolve
            bot"An onsen area...?"
            "The voice has now become clearer and decipherable, allowing you to faintly make out the tail end of the conversation..."
            scene bg onsen1_night with fade
            show madame normal with dissolve: 
                xalign -0.52
            show boruto suspicious:
                xalign 2.0 
                easein 1 xalign 1.0

            "Woman" "...- remember to toy with them and utilize the art of seduction."
            bot "Huh? Who is that? T-the art of... seduction?!"
           
            "Woman" "Let their hunger for your touch swell and overflow, before you allow your bodies to be joined with the techniques I have demonstrated."
            "Woman" "Instant gratification is never an effective strategy! The thrill of the chase will amplify their lust and desires to greater heights."
            show boruto surprised at right with vpunch
            bot "Lust and desire? Art of seduction? What the fuck is going on here?!"
            scene black
            "Servant" "Madame, I apologize for interrupting, but... we are not alone." with vpunch

            scene onsen_intro 1 with fade
            mada "Oh?"
            show onsen_intro 1:
                subpixel True
                easein 5 yalign 0
            bot "Shit, this could be bad..." with vpunch
            mada "What is the meaning of this?"
            mada "State your business here immediately before I summon the guards!"
            bot "She seems to be in charge here..."
            bot "How do I possibly get out of this situation now without being caught?!" with vpunch
            
            scene onsen_intro 1_1 with dissolve:
                yalign 0
            "Whispers" "{size=*0.8}Who is that? Have they sent someone for us to practice on?{/size}"
            show onsen_intro 1_1 with dissolve:
                xalign 1.0 yalign 0.35 zoom 1.6
            "Blonde woman" "{size=*0.8}I sure hope so, I was starting to get bored...{/size}"
            "Blonde woman" "{size=*0.8}I think he looks rather cute, can I go first?{/size}"
            show onsen_intro 1_1 with dissolve:
                xalign 1.0 yalign 0.2 zoom 2
            "Brunette woman" "{size=*0.8}That's no surprise, you think EVERYONE is cute!{/size}" with vpunch
            "Brunette woman" "{size=*0.8}You would really open up your legs for someone with hair like THAT? \nHe looks ridiculous!{/size}"

            scene onsen_intro 1_1 with dissolve:
                yalign 0
            bot "They've all got their eyes on me... \nWhat are they whispering to each other?!"
            bot "I should be careful with how I approach this..."

            menu onsen_approach_1:
                "Stare at her":
                    show onsen_intro 1_1:
                        subpixel True
                        easein 10 zoom 1.68 xalign 0.5 yalign 0.0
                    $ onsen_stared = True
                    "You stare at her without uttering a word, unable to come up with an appropriate response."
                    show onsen_intro 1_1 with dissolve:
                        zoom 1.0 xalign 0.5 yalign 0.0
                    "Panic starts to settle in as you claw your brain for a course of action."
                    bot "Think, damn it! What's wrong with me?!" with vpunch
                    bot "I can't just stand here and do nothing, I have to say something!"
                    show screen parallax1280("onsen_intro 1_1",) with dissolve 
                    call showscrollingimage from _call_showscrollingimage_195
                    "Your eyes wander and visually explore the woman's stunning figure before you." 
                    call increaselust(5) from _call_increaselust_269
                    bot "I don't know who this 'Madame' is, but damn is she fine!"
                    bot "She's definitely working for the Daimyo though, right?"
                    bot "Why else would she be here...?"
                    bot "Seems to be a figure of authority too... \nShe effortlessly commands the whole room with her presence alone."
                    bot "She hasn't done anything yet though... \nMaybe there's still a way out of this!"
                    call hidescrollingimage from _call_hidescrollingimage_150
                    hide screen parallax1280 with dissolve
                    scene onsen_intro 1_1 with dissolve:
                        yalign 0
                    mada "Well? I'm waiting..."

                    menu onsen_approach_2:
                        "Check her out again":
                            show screen parallax1280("onsen_intro 1_1") with dissolve
                            call showscrollingimage from _call_showscrollingimage_196
                            bot "Just look at the size of that ass!"
                            call increaselust(10) from _call_increaselust_270
                            bot "I'd love to have my way with that juicy thing."
                            bot "I would lick the sweat running down her smooth thighs and bury my face in those cheeks!"
                            bot "Her figure rivals even that of [hin_rel]'s..."
                            if hinata_captured == True:
                                bot "[hin_rel_stutter]!" with vpunch
                                bot "WHAT AM I DOING?!" with vpunch
                                bot"I need to focus on saving her instead of wasting time!"
                            else:
                                bot "WHAT AM I DOING?!" with vpunch
                                bot"I need to focus on the task at hand, I'm wasting time!"

                            hide screen parallax1280
                            show screen parallax1280("onsen_intro 1_1annoyed", menuenabled=True)
                            with dissolve
                            mada "I asked you a simple question!" with vpunch
                            mada "Are you capable of coherent speech? Or are you just here to foolishly drool all over my floor!"
                            bot "Fuck, seems like she is losing her patience... \nI'm running out of time!"

                            menu onsen_approach_3:
                                bot "Fuck, seems like she is losing her patience... \nI'm running out of time!"
                                "Keep staring at her":
                                    $ onsen_stared_long = True
                                    "You helplessly continue to stare at her with a blank expression on your face, no words escaping your mouth."
                                    "The silence in the room would be deafening, if not for the faint whispers and giggles of the servants circulating the room."
                                    "The contrasting combination of urgent self-preservation and lustful thoughts clash in your head, rendering you helpless and lost."
                                    "You're immobilized in front of your newly-found audience like a deer caught in headlights."
                                    bot "It's pointless, there's no getting out of this..."
                                    bot "What could I possibly say to make this situation any better?"
                                    bot "Those assholes have probably tracked me here by now anyway..."
                                    bot "How did I manage to end up like this? \nStuck between those fucking guards and a room full of half-naked women..."
                                    show onsen_intro 1_1annoyed:
                                        xalign 0.9 yalign 0.5 zoom 1.8
                                    hide screen parallax1280
                                    with dissolve
                                    bot "I guess it could be worse... I might as well enjoy the view while it lasts!"
                                    if hinata_captured == True:
                                        bot "I tried my best [hin_rel]... \nI'm so sorry..."
                                    else:
                                        bot "I'm so hopeless... I don't know what I expected..."
                                    
                                    show screen parallax1280("onsen_intro 1_1annoyed", initial_ypos=0.0) with dissolve

                                    mada "I have had enough of this foolishness, you have overstayed your welcome!"
                                    mada "Pick your jaw up from the floor and remove yourself from my presence at once!"
                                    scene black with dissolve
                                    call hidescrollingimage from _call_hidescrollingimage_151
                                    hide screen parallax1280 with dissolve
                                    stop music fadeout 2
                                    mada "GUARDS!!" with vpunch
                                    jump guards_onsen_thrown_out_ending

                                "{color=[hatredcolor]}I'll give you something to drool over, you bitch!{/color}":
                                    play sound "audio/soun_fx/error.opus" volume 1.0
                                    call changeHatred(1) from _call_changeHatred_195
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
                                    call hidescrollingimage from _call_hidescrollingimage_152
                                    
                                    scene black with dissolve
                                    stop music fadeout 2
                                    mada "GUARDS!!" with vpunch
                                    jump guards_onsen_thrown_out_ending

                                "Beg for help":
                                    jump onsen_beg_for_help

                        "Beg for help": 
                            jump onsen_beg_for_help

                "Beg for help":
                    label onsen_beg_for_help:
                        call hidescrollingimage2("Click twice to beg.") from _call_hidescrollingimage2_124
                        scene onsen_intro 1_1 with dissolve:
                            yalign 0.0
                        bot "Fuck it, they're not guards so maybe it's worth a shot..."
                        bo "Please, you have to help me! \nThere are guards outside searching for me and I need to stay hidden!"
                        if hinata_captured == True:
                            bo "I mean you ladies no harm and haven't done anything wrong, I'm just here to save someone dear to me!"
                        else:
                            bo "I mean you ladies no harm and haven't done anything wrong, I'm just trying to stay safe from them!"
                        bo "I give you my word! Please believe me!" with vpunch
                        jump examined_closer


label examined_closer:
    scene black with dissolve
    "The Madame raises her hand as if to signify a pause in the current state of affairs. She fixes her clothing and turns to address you..."
    scene onsen_intro 1_2 with dissolve:  
        yalign 1.0 
    show onsen_intro 1_2: 
        easein 4.0 yalign 0.1
 
    mada "Is that so...?"
    mada "I'll have you know that nothing on the palace grounds ever happens without my knowledge, or my approval."
    mada "And yet... "
    mada "Here you stand before me. A truly unexpected mystery emerging from the dark shadows of the night."
    mada "I must admit... \nI look forward to unwrapping and unravelling you to your very core... "
    mada "How very intriguing..."
    "She continues to gaze at you, seemingly scanning every inch of your appearance with as her eyes slowly move up and down your body."
    mada "Hmm... That face though... That hair..."
    mada "Could it be...?"
    
    if hinata_captured == True:
        mada "Yes, I see your true intentions now..."
        mada "You seek the Lady of the Leaf!" with vpunch
    else:
        mada "Yes, I recognize those features now..."
        mada "Does the Lady of the Leaf know you're here?"

    hide screen parallax1280
    
    bo "H-how did yo-...?!"

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
    mada "[bo_name], is it not?"
    bo "You know my n-name too!?"
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
    bot "How the FUCK does she know who I am?!" with vpunch
    show boruto suspicious at right with dissolve
    bot "Does this mean that she is actually helping me? \nOr am I going to regret trusting her?"
    bot "I'm running out of options here..."

    menu:
        "Don't trust her":
            bot "This doesn't feel right..."
            bot "If she knows who I am then it surely must be a trap!"
            show boruto:
                easeout 2 xpos 2000
            bot "I can't let this curse take control and make me chase every woman I see without caution!"
            scene black with dissolve
            bot "There has to be some other way..."
            
            scene onsen_intro 2_1 with dissolve:
                yalign 1.0
            show onsen_intro:
                easein 2 yalign 0.0
            "As you frantically look around, searching for any other options, you hear some commotion at the entrance as guards attempt to enter the area."
            "You notice the girls murmuring and glancing at you with a strange look..."
            bot"Shit! I am running out of options..."
            menu lkjashdfl23984:
                bot"Shit! I am running out of options..."
                "Jump in the onsen pools!"(supporter_scene = True):
                    $ call_label_action("madame_pool_replay")
                    call supp_rew from _call_supp_rew_12
                    jump lkjashdfl23984        
                    label madame_pool_replay:
                    $ initialize_replay_defaults()
                    bot "Fuck it! When life gives you lemons..."
                    scene onsen_intro 2_1 with fade:
                        yalign 0.0
                    $ renpy.sound.play("audio/soun_fx/clothes_drop.opus", channel="sfx3", loop=False, relative_volume = 1)
                    show boruto naked1 with dissolve:
                        zoom 0.38 xalign 0.4
                    "Servants" "*Gasping in unison*"
                    hide boruto with dissolve
                    bot "... You make lemonade!"
                    scene black with vpunch
                    play sound "audio/soun_fx/splash2.opus" volume 1.1
                    bo "Yahoo!" with vpunch
                    "You discard your clothes and jump into the onsen pool!"
                    scene black with vpunch
                    "You look around you, suddenly finding yourself surrounded by naked women!"
                    jump jumpingpoint_jumppool
                    
                "Make a run for it!":
                    pass
            jump guards_onsen_thrown_out_ending

        "Follow her":
            bot "I don't know what her intentions are, but I have no choice but to trust her for now."
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
            mada"Now, sit down and follow my lead..."

            scene onsen_intro 3 with dissolve:
                yalign 0.5
            show screen parallax1280("onsen_intro 3", initial_ypos=0.5)
            call showscrollingimage from _call_showscrollingimage_197
            "The Madame quickly covers your manhood with a towel, wraps your head in another, and gets down on her knees..."
            mada "Now is the time for you to sit still and not utter a word until I say it is safe."
            if onsen_stared == True:
                mada "Fortunately you have already proven that you are capable of remaining uselessly silent, so I trust that it will come naturally to you now as well."
            "She slowly moves her body up and down, rubbing her chest across your groin..."
            mada "Do we have an understanding?"
            call hidescrollingimage from _call_hidescrollingimage_153
            hide screen parallax1280

            menu:
                "Nod your head":
                    jump onsen_nod_head

                "{color=[hatredcolor]}Deviously nod your head{/color}": 
                    call changeHatred(1) from _call_changeHatred_196
                    bot "The arrogance on this fucking whore to tell me what to do..."
                    bot "I'll play along for now bitch... But my patience is wearing thin with you!"
                    bot "At the first possible opportunity, I intend to make you pay!"
                    $ hatred_nod = True
                    jump onsen_nod_head
            
label onsen_nod_head:
    "You nod your head in agreement..."
    "You tense up momentarily as her skin comes into contact with yours... But the rubbing sensation offers a sense of comfort, as you slowly let your guard down and relax."
    play sound "audio/soun_fx/footsteps.opus" volume 0.8
    mada"{size=*0.7}Here they come. Hush now...{/size}"
    show onsen_intro 3_1 with dissolve:
        zoom 1.1 yalign 0.0 xalign 1.0
    "Guard" "M-my lady! Excuse the intrusion but... have you perchance spotted a-"
    mada"You imbeciles! You dare barge into MY private chambers?" with vpunch
    "Guard" "This is an emergency, my lady! There's been an intrusion!"
    mada"Can't you see I am in the middle of servicing a welcomed guest?"
    mada"Out, NOW!" with vpunch
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
    mada "I will be blunt with you [bo_name], you should have never come here..."
    mada "Did you really think that you could take on the great Daimyo and his men single-handedly and live to tell the tale?"
    mada "While I can respect the courageous effort and good intentions... \nCourage can only get you so far!"
    mada "I have met your [hin_rel_mother] and sympathize with her, she is a graceful and kind soul..."
    mada "We had the opportunity to share a few moments together and get more acquainted with each other."
    mada "She truly is as amazing as my sources made her out to be! \nWe bonded instantly and effortlessly..."    
    mada "I guided her to the best of my ability in her endeavours here with the Daimyo..."
    mada "I tried to adequately prepare her for navigating through His Lordship's temperament and peculiarities..."
    
    if daimyomeeting_counter >= 3:
        mada "Unfortunately, she was unable to emerge from the meeting without upsetting him... \nAnd I fear it is something that he won't soon forget... Nor forgive..."
    else:
        mada "You must have inherited your obedience and wit from your [hin_rel_mother]! Both of you have proven to be quite capable in following my instructions well! *winks*"
        bot "Is she toying with me...?! What game is she playing at here?"
        
    mada "His Highness is a cruel man that does not tolerate being undermined... He goes along through his affairs by treating his subjects as simple cattle to be herded."
    mada "While normally I am against such sentiments... \nYou must understand that being here has indeed turned you into a sacrificial lamb, ready to be slaughtered yourself!"


    

    show screen parallax1280("onsen_intro 2", menuenabled=True) with dissolve
    call showscrollingimage from _call_showscrollingimage_198
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
            call increaselust(10) from _call_increaselust_271


            if onsen_stared == True: 
                bot "I just can't help myself, can I? At every opportunity..."
            
            bot "Look at those beautiful breasts... \nWho could possibly blame me for looking?"
            show screen parallax1280("onsen_intro 2") with fade
            bot "No wonder the Daimyo considers everyone cattle... \nHe apparently has concubines with massive milkers just prancing around the palace!"
            bot "I would probably feel the same way if I could watch them bouncing up and down all day!"
            bot "Damn, they're so nice to admire that I even forgot to blink for a second there...!"
            hide screen parallax1280 with fade

            show screen parallax1280("onsen_intro 2",menuenabled=True) with fade

            mada "Is something distracting you, little lamb?"
            bo "O-oh U-uhhm... No...!"
            bot "Shit, I mustn't get carried away like that..."

            menu:
                "Why did you help me?":
                    jump onsen_why_help_me

        "Why did you help me?":
            jump onsen_why_help_me
            
label onsen_why_help_me:

    bo "Why did you help me, Madame?"
    bo "You claimed to have aided my [hin_rel_mother] too...?"
    bo "What the hell is going on in this palace? \nAnd what is your part in all of this?!"
    
    mada "All will be revealed in time, do not get ahead of yourself [bo_name]."
    mada "As for why I am helping you escape..."
    mada "Let us just say that I do not want the Lady of the Leaf to be devastated by anything happening to you..."
    mada "The reasons of my allegiance and sympathy to her are none of your concern for now, and it is getting quite late..."
    mada "I will retire to my private chambers for the night to relieve the stress of tonight's adventure."
    mada "I suggest you lay low here momentarily, before making your way back home."
    if hinata_captured == True:
        bo "Back home?? I have to help my [hin_rel_mother], I can't just leave her here!" with vpunch
    else:
        bo "Back home?? I didn't come all this way to just simply give up now!" with vpunch
    mada "My servants will tend to you here, you are welcome to bathe and relax in their company."
    mada "Tend to him if he so wishes ladies, but do not delay his departure for long. I will not be here to prevent the guards from capturing him a second time..."
    "Servants" "Yes Madame, we will take care of him as per all your teachings."
    mada "Excellent, I entrust him now onto you then... \nEnsure his swift departure is safe and in good spirits."
    mada "I bid you farewell then, for now..."
    scene black
    call hidescrollingimage from _call_hidescrollingimage_154
    hide screen parallax1280 with fade

    "Madame heads off to retreat to her private quarters, leaving you alone by the pools."
    
    scene onsen_intro 2_1 with fade:
        yalign 0.0
    show boruto towelmad with dissolve:
        xalign 0.4
    
    if hinata_captured == True:
        bo "Wait! What about [hin_rel]?? \nI can't just leave her here, you have to help me!" with vpunch
    else:
        bo "Wait! You can't just leave me here like that, you have to help me!" with vpunch
    show boruto at smallshake
    bot "Crap! She completely ignored me..."
    bot "Surely she is capable of helping with more, right?"
    bot "She told me to keep a low profile here... "
    bot "But I can't just sit around and do nothing!" with vpunch

    menu yolomenuhehe1:
        "Relax in the pool with the servants"(supporter_scene = True):
            $ call_label_action("pool_service_d14")
            call supp_rew from _call_supp_rew_13
            jump yolomenuhehe1
            label pool_service_d14:
            show boruto towelsmirk with dissolve:
                xalign 0.4
            bot "Fuck it, I deserve some relaxation after all that mess!"
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
            label jumpingpoint_jumppool:
            "Servant" "{size=*0.8}Did you see that? The boy's hung!{/size}"
            "The girls quietly whisper to each other while stealing glances at you..."
            "Not before long, some of them quickly approach you!"
            show jumponsen_intro1 with dissolve:
                yalign 0.0
            show jumponsen_intro1:
                easein 2 yalign 1.0
            $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
            bo"L-ladies...?" 
            "Older Servant" "We don't often get younglings to keep us company... *Giggles*"
            "Younger Servant" "And a stud no less! You reckon you could be my first?"
            bo"Your f-first, huh?"

            show jumponsen_intro1_1 with dissolve:
                yalign 0.0
            show jumponsen_intro1_1:
                easein 2 yalign 1.0
            $ renpy.sound.play("/audio/soun_fx/water_move_2.opus", channel="sfx1", loop=False, relative_volume = 0.5)
            "Older Servant" "Don't tease our guest, you lousy fox! \nWe all know you've slept with hundreds of men..."
            "Younger Servant" "And all of them were unkempt, fat, and old! \nHe will be my first that I {i}enjoy!{/i} *giggles*"
            "Older Servant" "You are such a brat, you know that? \nWhy don't we let the handsome young man decide who he prefers?"

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
            call showscrollingimage from _call_showscrollingimage_199
            servchoice "Just sit back and relax for me..."
            servchoice "Is the water to your liking? \nAre you enjoying yourself here between the naked bodies of two gorgeous women?"
            bo "Y-yes... Everything is amazing!"
            servchoice "Let the steamy waters wash away all your stress and troubles, while we wash this young cock of yours..."
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
            bot "No way, this is going WAY better than I thought it would!"
            $ renpy.sound.play("/audio/soun_fx/handjob3.opus", channel="sfx2", loop=True, relative_volume = 0.6)

            servchoice "You heard me! Don't pretend you don't want to... \nI can feel your cock pulsing and twitching in anticipation..."
            servchoice "It's making me tingle all over just feeling it!"
            servchoice "So hard and thick in my hands too... You're ready for me, I sense it..."            
            servchoice "F-fuck, I need it NOW!" with vpunch
            scene black with dissolve

            call hidescrollingimage from _call_hidescrollingimage_155
            
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
            show jumponsen_intro 2_2 with dissolve
            $ renpy.sound.play("/audio/soun_fx/kiss1.opus", channel="sfx2", loop=True, relative_volume = 1)
            bot "I've never felt a tongue do that before!"
            "You allow her to pour all her affection and desire into you, her lips dancing on yours with a fiery passion as she let's out soft, quiet moans with every kiss!"
            "Your body is on the verge of complete relaxation as your eyes close shut, and you begin to lose yourself in the moment..."
            "The world and your surroundings dissolve as darkness closes in around you, the serene sound of flowing waters sending you into a trance as the servant unrelentingly offers herself to you."
            $ renpy.sound.play("/audio/soun_fx/kiss2.opus", channel="sfx2", loop=True, relative_volume = 1)
            "The heat of her body and the sweet taste of her saliva on your tongue overload your senses, as she mounts you and wraps her legs around your waist."
            menu randommenu_onsenpool:
                bot "This must be what heaven feels like..."
                "Grab her ass and pull her in!" if pool_complete == False:
                    show jumponsen_intro 2_3 with dissolve
                    $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                    "You let your hand explore the servant's body as your lips remain interlocked..."
                    "It finds its final resting spot upon her ass cheek, as you start to squeeze instinctively..."
                    show jumponsen_intro with dissolve:
                        zoom 1.1 xalign 0.5 yalign 0.9
                    "You grip it tight and pull her towards you, inviting her closer!"
                    servchoice "*moans* ♡ Yesss, I know... More... You want more!"
                    show jumponsen_intro 3 with dissolve
                    stop sfx2 fadeout 1
                    $ renpy.sound.play("/audio/soun_fx/water_move_2.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                    "She lifts herself towards you as she leans forwards... \nEffortlessly gliding through the water with the pull of your hands on her body."
                    "You feel her soft breasts pressed against your own chest as you grope her, her wet body creating ripples in the pool as she repositions herself."
                    "Your clenched fingers spread her ass cheeks wide open to expose her dripping wet pussy, as she moans softly under her breath..."
                    servchoice "A-ah yess!♡! Those strong hands feel so good on my body..." with vpunch
                    $ renpy.sound.play("/audio/soun_fx/water_move_4.opus", channel="sfx1", loop=False, relative_volume = 0.5)

                    servchoice "I want you... I need you all over me!♡"
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
                    call showscrollingimage from _call_showscrollingimage_200
                    servchoice "A-ahh, y-yess!♡... Exactly what I was craving!"
                    servchoice "You've had sex before, have you not?"
                    call hidescrollingimage("Click twice to start pounding her!") from _call_hidescrollingimage_156
                    scene black with dissolve
                    $ renpy.sound.play("/audio/soun_fx/splash1.opus", channel="sfx3", loop=False, relative_volume = 1)
                    $ renpy.sound.play("/audio/soun_fx/femalemoan1.opus", channel="sfx1", loop=True, relative_volume = 2)  
                    $ renpy.sound.play("/audio/soun_fx/pushitin1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                  
                    show screen parallax1280("jumponsen_intro 3_3", initial_ypos=1.0) with vpunch
                    call showscrollingimage from _call_showscrollingimage_201
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
                    call hidescrollingimage("Click twice to fuck her harder!") from _call_hidescrollingimage_157
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
                    call showscrollingimage from _call_showscrollingimage_202
                    bo "AGHHHH! ♡! *Loud Moans* ♡♡" with vpunch
                    call hidescrollingimage from _call_hidescrollingimage_158

                    show jumponsen_intro 3_after with dissolve
                    $ renpy.sound.play("/audio/soun_fx/water_move_1.opus", channel="sfx1", loop=False, relative_volume = 0.5)

                    servchoice "Fuck yeah, that's so hot♡! I can feel it dripping out of me..."
                    servchoice "Thank you for indulging me. I don't often get to have this much fun, let alone getting stretched by a young stud!"
                    "She playfully kisses you on the forehead while you catch your breath and regain post-nut clarity."

                    show screen parallax1280("jumponsen_intro 3_4", initial_ypos=0.5) with fade
                    call showscrollingimage from _call_showscrollingimage_203
                    $ renpy.sound.play("/audio/soun_fx/water_move_2.opus", channel="sfx1", loop=False, relative_volume = 0.5)

                    bo "I-I'm so sorry, I lost control, I should have pulled out..."
                    servchoice "Don't be silly cutie... That was exactly what I wanted!♡"
                    servchoice "I haven't had this much fun in a while!"
                    servchoice "Besides... Bathing in the heated pools prior to all our fun makes it perfectly safe."
                    servchoice "Think of it as a natural contraception, you won't be impregnating me here... Not unless we REALLY want it to happen! *wink*"
                    bot "Phew, I guess I got lucky there... \nBut I shouldn't make a habit of doing that!"
                    bot "I don't think it's quite the time to think about being a father right now, especially not with random women!"
                    servchoice "Did I leave you speechless? Come now, let's get you cleaned up!" with vpunch
                    scene black with dissolve
                    call hidescrollingimage from _call_hidescrollingimage_159
                    jump pool_ending


        "Follow Madame to her private quarters":
            if hinata_captured == True:
                bot "She's delusional if she thinks I'm just going to abandon [hin_rel] like this!"
            else :
                bot "She's delusional if she thinks I'm just going to pack up now and leave, I need to figure out what's going on!"
            bot "Now where did I leave my clothes again...?"
            
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
                    if hinata_captured == True:
                        bo "I came here to find my [hin_rel_mother], and I will not leave until I do!"
                        bo "If what you said is true and you share a bond with her, then you have to help me!"
                    else:
                        bo "I came here to the palace to figure out what's going on, and I will not leave until I do!"
                        bo "If what you said is true and you share a bond with my [hin_rel_mother], then you have to help me!"
                    bo "If not for me... "
                    bo "Then do it for her!" with vpunch

                    mada "Foolish boy, you have no idea with what you're meddling with!"
                    mada "Your overwhelming arrogance and blind confidence will be the end of you..."
                    if hinata_captured == True:
                        mada "You will end up in a cell right opposite your beloved [hin_rel_mother], except... You will be the only one to remain there, beaten and bruised, left to rot and degrade into dust!"
                    else:
                        mada "You will end up in a cell, beaten and bruised, left to rot and degrade into dust!"

                    menu:
                        "{color=[hatredcolor]}You fucking bitch!{/color}":
                            call changeHatred(2) from _call_changeHatred_197
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
                            bo "Just point me in the right direction, and whatever happens after that will be my burden to bear."
                            bo "If I am caught then so be it, it will be the consequences of my own actions..."
                            if hinata_captured == True:
                                bo "But I at least owe it to her to try!"
                            
                            "Madame draws a long breath and hesitates for a second before replying, clearly contemplating her next words with caution..."
                            "Her gaze softens and she regains her composure, a wave of what appears to be genuine sympathy washes over her features."
                            "While visibly annoyed with your stubbornness, she can't help but be slightly impressed with your heroic perseverance..."
                            
                            mada "Very well... If that is your wish..."
                            
                            "You let out a sigh of relief..."
                            bot "Finally..."
                            
                            mada "I will offer some of my guidance to aid you in finding what you seek..."
                            mada "However..."
                            mada "Seeing as how I have already gone out of my way to help you tonight as it stands..."
                            mada "I think a little... Repayment... Is in order first.... \nDon't you agree, little lamb?"
                            
                            bot "Why the fuck does she keep calling me that? \nI don't like that smirk on her face either..."
                            bo "Yes, of course... I suppose that sounds reasonable to me..."
                            bo "What exactly did you have in mind?"
                            
                            mada "Ladies, you are dismissed for tonight, you will not be needed anymore!"
                            "Servants" "Yes, Madame!"
                            
                            scene black with dissolve
                            play sound "audio/soun_fx/footsteps.opus" volume 0.6
                            "You watch as the servants scurry out of the room, leaving the two of you alone for the first time tonight."
                            
                            show screen parallax1280("onsen_intro 4_0", 1.25, menuenabled=True) with dissolve
                            call showscrollingimage from _call_showscrollingimage_204
                            "Madame lays down on the bed, resting her head on the soft pillows as she gazes at you with a sultry look in her eyes."
                            mada "Now, little lamb... I have a simple proposition for you."
                            mada "I seem to recall [hin_name] mentioning how her [hin_rel_to_bo] was quite the masseur..."
                            mada"How he often helps her relieve stress..."
                            mada "My terms are simple..."
                            mada "You are to prove her claims to me, by servicing me to the best of your capability."
                            bot "HUH?! She wants me to SERVICE her?" with vpunch
                            bot  "Is this really happening...?!"
                            mada "If I am satisfied, then I will in turn satisfy whatever needs you may have of me... regarding your [hin_rel_mother] of course!"
                            "The Madame's gaze drift downwards towards your crotch where it lingers for some time..."
                            mada "It's such a pity that I do not have any oil lying about here to aid you, you will sadly have to take your time and do without..."
                            mada "Show me, little lamb... Are you really as good as the rumors claim?"
                            mada "Do you think that you are up to the task?"

                            menu randommenu21384923984:
                                mada "Do you think that you are up to the task?"
                                "I will do my best" if massageknowledge ==0:
                                    default madame_massage_certainfail = False
                                    $ madame_massage_certainfail = True 
                                    bo "I will do my best to meet your standards Madame, I'm confident that you won't be disappointed!"
                                    bo "I do happen to have a small request though..."
                                    mada "Yes? Go on..."
                                    bo "Once you're satisfied, you stop calling me little lamb!"
                                    call hidescrollingimage from _call_hidescrollingimage_160
                                    hide screen parallax1280
                                    jump massage_minigame_start

                                "{color=[obediencecolor]}I am indeed, a master masseur!{/color}" if massageknowledge >= 1:
                                    $ madame_massage_certainfail = False 
                                    bo "You're in luck, I happen to be a master masseur!"
                                    bo "I make miracles happen with these fingers that leave women screaming for more, so you're in for a treat!"
                                    mada "Is that so? Let us see then if you can meet the high expectations that you set..."
                                    bo "I'll have you moaning my actual name instead of 'little lamb' to me in no time!"
                                    call changeDominance(1) from _call_changeDominance_121
                                    call hidescrollingimage from _call_hidescrollingimage_161
                                    hide screen parallax1280
                                    jump massage_minigame_start
                                
                                "{color=[obediencecolor]}???{/color}" if massageknowledge == 0:
                                    "Find a way to increase your massage knowledge to unlock this option!"
                                    jump randommenu21384923984

label pool_ending:

    show screen parallax1280("jumponsen_intro 4", initial_ypos=0.5) with fade
    $ renpy.sound.play("/audio/soun_fx/water_move_3.opus", channel="sfx1", loop=False, relative_volume = 0.5)
    $ renpy.sound.play("/audio/soun_fx/handjob3.opus", channel="sfx3", loop=True, relative_volume = 0.6)

    call showscrollingimage from _call_showscrollingimage_205
    "Two servants return to your side, wiping off any excess cum still left dripping on your cock."
    "Older Servant" "Still oozing after that, huh? Maybe you should visit more often..."
    "Older Servant" "We'll take care of your urges, and you'll take care of ours, won't you...?"
    bot"Is this paradise? Maybe I should live here instead-"
    show screen parallax1280("blackscreen") with vpunch
    "Guard from afar" "A sighting of the intruder was reported around this area. Step aside!" with vpunch
    show screen parallax1280("jumponsen_intro 4_1", initial_ypos=0.5) with dissolve
    "You hear some commotion from outside the onsen..."
    bot"S-shit! They are onto me."
    bo"I uuh, I best be making my exit, g-girls!"
    "Older Servant" "What a shame! But it's too risky to hold you here for much longer!"
    "Younger Servant" "Don't forget about us though! We would love to have you come visit again some time soon..."
    call hidescrollingimage from _call_hidescrollingimage_162
    "Older Servant" "That's enough. Quickly! Get dressed and I'll show you a quiet way out, away from prying eyes..."
    $ renpy.sound.play("/audio/soun_fx/water_move_2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
    scene black with fade
    hide screen parallax1280

    play sound "audio/soun_fx/clothes_dress.opus" volume 0.8
    "You stumble around getting yourself dressed before being quietly escorted outside by one of Madame's servants..."
    label jumpfrommassage_fail:
    show palace_night bg
    show boruto surprised2 at center
    with dissolve
    if hinata_captured==True:
        bot"Shit! [hin_rel]..."
        bot"I totally lost track of my objective, but it's too risky to get back in there with the guards on high alert."
        scene black with dissolve
        bot"I'll have to try again soon! Hang in there [hin_rel]..."
        "You make your way back home..."
    else:
        bot"Phew! Made it out alive, if nothing else..."
        scene black with dissolve
        "You make your way back home, exhausted but satisfied with the events of the night you head straight to bed..."
    $ poolservice_d14 = True
    $ pool_complete = True
    jump action_taken



label madame_reward_scene:
    $ initialize_replay_defaults()
    scene black with dissolve
    show screen parallax1280("onsen_intro 4_1") with dissolve
    $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 0.7)
    call showscrollingimage from _call_showscrollingimage_206
    mada "My my... What do we have here?"
    mada "Is it always this big, or have I had this much of an effect on you..."
    show screen parallax1280("onsen_intro 4_2") with dissolve
    mada "I must say, I am rather impressed with your... Endowment, little lamb."
    mada "Clearly you have had immoral thoughts about me tonight while you handled my body, you cannot deny it!"
    mada "However, you do know that I am one of the Daimyo's concubines, do you not?"
    mada "Have you any idea what he'd do to me if he ever found out about this?"
    mada "Or worse yet, what he would do... to you?"
    show screen parallax1280("onsen_intro 4_3") with dissolve
    mada "You can keep a secret though, can't you?"
    bo "Y-yes... M-Ma'am!"
    mada "Excellent, precisely what I wanted to hear!"
    mada "Then allow me to help..." 
    show screen parallax1280("v020_madame_hj1anim", menuenabled=True) with dissolve
    "Madame starts rubbing the length of your shaft, sending ripples of excitement through your body with every stroke"
    "Your eyes slowly drift from the deliberate movement of her hands towards her eyes..."
    "Fixated onto you, she gazes back as if staring into your soul, while masterfully navigating the length of your cock..."
    "But even so, she would occasionally briefly pause..."
    "Biting her bottom lip seductively and stealing a quick glance at your manhood, before resuming her motions."
    bo "Aghh, fuck yes! That feels good Madame..."

    mada "You have done well tonight, [bo_name]. In exchange, I too, shall service you..."
    label madame_reward_scene_first_choice:
        menu:
            "{color=[dominancecolor]}I need more than just your hands at my service!{/color}": 
                call checkDominance(15,"madame_reward_scene_first_choice") from _call_checkDominance_50
                bo "I need more than just your hands at my service!"
                show screen parallax1280("blackscreen") with dissolve
                mada"Ooh..? A bold one, aren't you? But everything has it's time, and it's pla-"
                show screen parallax1280("onsen_intro 5") with dissolve 
                "Before she could finish making her point, you stand above her, and push your erect cock between her soft and welcoming breasts!" with vpunch
                mada "Oh m-my! Your lust for my body can not easily be satiated, I see... I am quite flattered!"
                mada "I will allow it, this one time... Take what you have earned [bo_name]!"
                show screen parallax1280("blackscreen") with dissolve
                bo "They feel fucking amazing!"
                show screen parallax1280("onsen_intro 6") with dissolve 
                "Madame leans back, arching her back forward and pulling you in, allowing your hands to rest on her breasts."
                call hidescrollingimage("Click twice to start thrusting!") from _call_hidescrollingimage_163
                hide screen parallax1280
                show v020_madame_titjob1_anim:
                    yalign 1.0
                show v020_madame_titjob1_anim:
                    easein 10 yalign 0.1
                with dissolve
                "Maintaining eye contact, she gives you ample space to encourage you to thrust into her."
                "Her chest is conveniently lubricated with the sweat of your labours and the precum that was dripping out of your hard cock."
                mada "Yes that's it, watch how easily your manhood glides between them."
                mada "How does it feel to have your meat be surrounded by the breasts of a royal concubine?"
                show v020_madame_titjob1_anim with dissolve:
                    easein 10 yalign 0.5
                bo "Aghh...I-it feels so fucking good...!" with vpunch
                bo "So soft, yet so firm and full..."
                bo "It's as if they were made perfectly just for this!"
                mada "Take what you need from them, they are yours to use as you see fit..."
                show v020_madame_titjob1fast_anim with dissolve:
                    yalign 0.5
                bo "F-fuck yes, with pleasure!" with vpunch
                bo "F-feels even fucking better when I go faster... F-FUUUCK!"
                show screen parallax1280("blackscreen") with dissolve
                "You start losing control of your body as the pleasure builds up..."
                show screen parallax1280("v020_madame_titjob2_anim", menuenabled=True) with dissolve  
                call showscrollingimage from _call_showscrollingimage_207
                $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.5)
                "In a fit of uncontrollable lust, you grab Madame by the breasts and push her down onto the nearby bed." with vpunch
                "She offers little to no resistance, allowing you to take charge and dominate her as you wish!"
                mada "Oh, you are starting to get a bit rough now, aren't you?"
                mada "Does it excite you to be in control of my body?"
                bo "How could I not be excited?! I've been wanting enjoy your hot body since the moment I laid my eyes on you!"
                bo "These boobs are so perfect, I can't fucking keep my hands off them!"
                bo "The way they feel under my fingers after every squeeze... The way they bounce and jiggle with every thrust..."
                bo "Fuck, it just feels so... Right!"
                mada "*giggle* Your words of lust flatter me, and your very apparent arousal has you almost drooling all over me..."
                mada "You are granted full access to my breasts to do as you please, no more and no less..."
                mada "Show me how much you want this, and how much you want me!" with vpunch
                menu madamerna1293:
                    "{color=[hatredcolor]}This isn't enough, I need more!{/color}":
                        call checkHatred(30,"madamerna1293") from _call_checkHatred_35
                        bo "This isn't enough, I need more!" with vpunch
                        show screen parallax1280("onsen_intro hatred2", menuenabled=True) with dissolve
                        "You grab Madame by the hair and pull her head forward, staring menacingly at her as you growl at her and pin her arm down."
                        bo "You've fucking teased me all night you dumb skank, you think I will settle for only your tits?!"
                        bo "I've had enough with your games, now we play by MY rules!"
                        mada "You are pushing your luck, child! Cease this immediately!"
                        bo "We both know that's not going to happen, you're mine now bitch..."
                        label onsen_reward_hatred:
                            menu:
                                "{color=[hatredcolor]}Your whore mouth looks like a good start!{/color}":
                                    bo "Your whore mouth looks like a good start!"
                                    bo "Bring it over here so I can stuff it full with the taste of this hard cock!"
                                    show screen parallax1280("onsen_intro hatred3") with dissolve
                                    "You dash around the bed to angle yourself closer to her face, the primal hunger in you taking over as you grab her by the face!"
                                    "Your sweaty, erect cock now dangling before her, grazing her cheek every time it throbs and twitches in front of her."
                                    mada "What do you think you are doing?!" with vpunch
                                    bo "What does it look like, you dumb slut? I'm making you my bitch!"
                                    bo "We both know you want to be used like one of your worthless servants, so stop resisting and give me what I fucking want!"
                                    bo "I'm going to make you choke on this big cock and blast my cum all over your pretty little face..."
                                    bo "I will enjoy watching you take it all, you cum-hungry whore..."
                                    bo "We'll both get to watch as it drips from your violated lips, down your chin, and drip on those huge fucking tits!"
                                    bo "You're just another fucking useless hole to shove my cock in!"
                                    bo "So stop wasting my time, and start sucking on this fat cock, bitch!"
                                    scene black
                                    call hidescrollingimage from _call_hidescrollingimage_164
                                    mada "THAT IS ENOUGH!" with vpunch
                                    mada "I WILL NOT STAND FOR THIS DISRESPECT ANY LONGER!"
                                    "She shoves you hard to create some distance between the two of you, as she scrambles to her feet."
                                    bo "You BITCH!"
                                    show bg onsen1_night with dissolve
                                    show madame undress2 at center with dissolve
                                    "She regains her composure, and does what she should have done some time ago..."
                                    mada "GET OUT!" with vpunch
                                    show madame angry at center with dissolve
                                    mada "Don't ever let me see your face around here again, you disgusting swine!"
                                    $ onsen_blocked = True
                                    scene black with dissolve
                                    stop music fadeout 2
                                    mada "GUARDS!!" with vpunch
                                    jump guards_onsen_thrown_out_ending

                                "{color=[hatredcolor]}Your pussy must be soaking wet!{/color}":
                                    bo "Your pussy must be soaking wet!"
                                    bo "Time for a little hole inspection before I stuff it full and make you scream like the whore you are!"
                                    show screen parallax1280("onsen_intro hatred4") with dissolve
                                    "Without letting go of her by the hair, you drag her around as she flails her arms around in protest."
                                    "You manage to maneuver her and angle yourself above her groin, spreading her legs wide."
                                    "Your fully erect cock now rests on her crotch, as you slowly rub the head and shaft over her pussy."
                                    bo "Ah yes, I can feel the juicy lips around your tight hole!"
                                    bo "They are quivering from excitement and clearly feel moist, even through these clothes..."
                                    bo "It's like a fucking waterfall down here between your legs, don't even try to pretend that you're not enjoying it!"
                                    mada "What the fuck are you doing?!" with vpunch
                                    bo "What does it look like, you dumb slut? I'm making you my bitch!"
                                    bo "Finally I get to take what I've fucking earned, I've been wanting to fuck you all night since I first saw that hot ass on you..."
                                    bo "I'm done waiting though! So be a good little whore and stop fucking resisting!"
                                    mada "Ughh! Get off of me!"
                                    bo "I'm going to love the sound of that dripping wet pussy getting pounded, as I impale you with this huge cock!"
                                    bo "You will take all of it, again... and again... and again!"
                                    bo "Till I decide I'm done with you with your filthy hole today!"
                                    bo "You'll be walking around the palace with my cum leaking out of you, like the little fucking cum-dumpster you are..."
                                    bo "Everyone will finally see just how worthless you truly are, born to be passed around and discarded like trash!"
                                    mada "THAT IS ENOUGH!" with vpunch
                                    mada "I WILL NOT STAND FOR THIS DISRESPECT ANY LONGER!"
                                    scene black with dissolve
                                    call hidescrollingimage from _call_hidescrollingimage_165
                                    hide screen parallax1280 with fade
                                    "She shoves you hard to create some distance between the two of you as she scrambles to her feet and regains her composure and dignity."
                                    scene bg onsen1_night with dissolve
                                    show madame undress2 at center with dissolve
                                    mada "I don't know what has gotten into you, and why you thought this was appropriate in the slightest!"
                                    mada "I hope for your sake that this is your condition taking control, because I will not tolerate this for even one more second!"
                                    mada "Your night ends here [bo_name], I suggest you leave at once and never return!"
                                    $ onsen_blocked = True
                                    scene black with dissolve
                                    stop music fadeout 2
                                    mada "GUARDS!!" with vpunch
                                    jump guards_onsen_thrown_out_ending


                    "I love how they feel!":
                        bo "I love how they feel!"
                        bo "I could spend all night just playing with them, they feel so soft and warm!"
                        show screen parallax1280("onsen_intro 7") with dissolve

                        "You mount Madame's breasts and start thrusting your cock between them, enjoying the sensation of her soft skin rubbing against your shaft."
                        show screen parallax1280("v020_madame_titjob3_anim") with dissolve
                        "Madame passively allows you to do as you please, and just stares back up at you with a hint of intrigue in her eyes."
                        bo "F-fuck! I've never felt anything like this before, they are incredible..."
                        mada "That's it, you're doing great..."
                        mada "My body is yours to enjoy, take comfort in the warm touch of my breasts as they rub against every inch you have to offer!"
                        show screen parallax1280("v020_madame_titjob3fast_anim") with dissolve
                        bo "F-fuuuck, you're so hot!" with vpunch
                        "You pick up the pace, awkwardly thrusting in and out of her succulent curves, while squeezing her breasts together."
                        mada "Your movements are clumsy, inexperienced, and yet..."
                        mada "You are exciting me! This youthful energy of yours..."
                        show screen parallax1280("blackscreen") with dissolve
                        mada "Lie back and allow me to indulge you, little lamb!" with vpunch
                        show screen parallax1280("v020_madame_titjob4_anim") with dissolve
                        "She pushes you on your back as she hungrily gets on top of you, letting the weight of her breasts engulf your cock..."
                        mada "Is this what you lusted for all night?"
                        bo "Fuck yeah, it is! Ughh... and it's as good as I imagined it to be..."
                        mada "*Giggles* I'm glad you're enjoying yourself, because I'm loving the feeling of this hard cock between me!"
                        mada "I'm not stopping till I'm done milking it dry of ALL the cum you have to offer me!"
                        mada "I don't want want my breasts to only have sweat dripping off them..."
                        mada "I want them covered in your cum!" with vpunch
                        bo "Aghh f-fuck, I want that too!"
                        bo "I'm so c-close... Keep bouncing those tits on my cock!" 
                        bo "AGHHHH!" with flash
                        mada "Getting close, are you? Show me how much you love using them!"
                        mada "Cum all over me, I want it all!"
                        show screen parallax1280("blackscreen") with dissolve
                        bo "F-FUCK, LET ME GET UP...!"
                        bo "I'M CUMMING!" with flash
                        $ renpy.sound.play("/audio/soun_fx/cum8.opus", channel="sfx2", loop=False, relative_volume = 0.3) 
                        show screen parallax1280("onsen_intro 8") with flash
                        bo "Y-YES, FUCK... TAKE MY CUM!" 
                        $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.3) 
                        show screen parallax1280("onsen_intro 8_2") with flash
                        mada "Good boy, watch all that hot cum drip off my body..."
                        call decreaselust(100) from _call_decreaselust_135
                        mada "We'll make a man out of you yet, little lamb..." 
                        bot "*Heavy breathing* F-fuu-...That felt amazing..."
                        scene black
                        call hidescrollingimage from _call_hidescrollingimage_166
                        hide screen parallax1280

                        bot "Fuck, she's never going to drop that is she?"
                        bot "It's ok I guess, she can call me whatever she wants as long as we get to do this again some other time!"
                        mada "As arousing as that was, that's enough entertainment for now... \nCome now, allow me to wipe us both clean..."
                        "Madame takes a nearby towel and wipes up the mess that the two of you have created, to the best of her ability at least..."
                        $ madamemassage_domreward = True

                        scene bg onsen1_night with dissolve
                        show madame undress2 at left 
                        show boruto naked2 at right:
                            zoom 0.37
                        with dissolve
                        mada "[bo_name], what an excellent choice of company you were tonight..."
                        mada "I hope you enjoyed our little escapade here as much as I have."
                        mada "I'm starting to like your family more and more with every encounter! *smirk*"
                        mada "Speaking about family..." 

                        label madame_massage_minigame_success_initialendingfork:

                        if hinata_captured == True:
                            mada "I think the time has come for you to tend to your [hin_rel_mother], is it not?"
                            show boruto naked1_surprised at right:
                                zoom 0.37
                            bot "[hin_rel]! I completely forgot about her!" with vpunch
                            bo "Yes, please Madame! I must see her at once!"
                            show madame normal2 at left with dissolve
                            mada "Get dressed and follow me then... And do not make a sound! \nI know of a passage that will lead you safely into the dungeons."
                            $ onsen_information_attempt_done = True 
                            scene black with dissolve
                            play sound "audio/soun_fx/clothes_dress.opus" volume 0.8
                            jump dungeon_secretpassge
                        
                        elif hinata_captured == False and onsen_information_attempt_done == False:
                            mada "I think it is time to have you returned safely back to your [hin_rel_mother], is it not?"
                            show boruto naked1_surprised at right:
                                zoom 0.37
                            bot "I almost completely forgot about what I even came here for!" with vpunch
                            bo "Yes, Madame, I must slowly get going... But please, I need your help first in figuring everything out before I go!"
                            bo "What is the Daimyo planning? \nAnd why is he so interested in my family?"
                            bo "Something just doesn't feel right about any of this..."
                            show madame normal2 at left with dissolve
                            mada "I wish I could tell you more, but I am not at liberty to fully disclose the Daimyo's plans and intentions to you."
                            mada "Even {i}I{/i} am not privy to all of his secrets, despite my position as a concubine in his court."
                            mada "However, I can tell you that I believe he is planning something big, and that it {i}will{/i} involve your family in some way..."
                            bot "That doesn't sound very good at all..."
                            mada "I cannot say more, but I urge you to be cautious when dealing in anything revolving around him."
                            mada "For now though, we must focus on getting you out of here safely..."
                            mada "Get dressed and follow me... And do not make a sound! \nI will lead you safely out of the palace grounds."
                            scene black with dissolve
                            play sound "audio/soun_fx/clothes_dress.opus" volume 0.8
                            "You stumble about, getting dressed quickly to keep up with her while still trying to catch your breath."
                            play sound "audio/soun_fx/footsteps.opus" volume 0.8
                            "Following Madame through the winding corridors, she safely navigates you through the premises safely and undetected."
                            "You exchange a few glances and bid your farewells, before making your way back home exhausted, yet satisfied, with the events of the night..."
                            $ onsen_information_attempt_done = True
                            jump action_taken

                        else:  
                            mada "I think it is time to have you returned safely back to your [hin_rel_mother], is it not?"
                            mada "I have a feeling that you will be back again for more... I look forward to our next encounter!"
                            mada "For now though, I will escort you back outside the palace grounds safely."
                            show madame normal2 at left with dissolve
                            mada "Come little lamb, get dressed and follow me... I shall lead the way..."
                            scene black with dissolve
                            play sound "audio/soun_fx/clothes_dress.opus" volume 0.8
                            "You stumble about, getting dressed quickly to keep up with her while still trying to catch your breath."
                            play sound "audio/soun_fx/footsteps.opus" volume 0.8
                            "Following Madame through the winding corridors, she safely navigates you through the premises safely and undetected."
                            "You exchange a few glances and bid your farewells, before making your way back home exhausted, yet satisfied, with the events of the night..."
                            jump action_taken 


                            


            "Your hands feel amazing!":
                bo "Your hands feel amazing, Madame!"
                bo "Your fingers feel perfect wrapped around me! I could relax and enjoy this all night..."
                show screen parallax1280("blackscreen") with dissolve
                mada "Here, stand up and allow me to continue..."
                show screen parallax1280("onsen_intro 9") with dissolve
                mada"There's something to you, little lamb. A peculiar smell, a temptation..."
                show screen parallax1280("onsen_intro 9_2") with dissolve
                mada "It evokes something in me, and I can't help but wonder what it would be like to go further..." with vpunch
                show screen parallax1280("onsen_intro 9_3") with dissolve
                "Your breath hitches, as she leans forward, bringing her puckered lips a breath's distance away from you..." with vpunch
                bo "*Gulp*" with vpunch
                bot "Is she about to suck me off!? She's so close to the tip, I feel her breath on it!"
                show screen parallax1280("onsen_intro 9_1") with dissolve
                mada"*Giggles*" with vpunch
                mada "You didn't think I was about to... did you? Naughty boy..."
                show screen parallax1280("v020_madame_titjob5_anim", menuenabled= True) with dissolve
                mada"But this much, I can offer to you..."
                "She starts working your shaft with fiery intent."
                "Occasionally leaning in, entertaining intrusive thoughts to tease you for a brief moment, before resuming her 'service' to you..."

                mada "You want to know how it would feel, don't you...?"
                mada"Sleeping with a royal concubine, reveling in the pleasure my body has to offer..."
                bo "I-I do, Madame! I want you so f-fucking bad right now!"
                mada "I can feel your heart racing, your body trembling with anticipation..."
                mada "I see the lust in your eyes, your desire to claim more of me. But..."
                mada "I am already betrothed, you know. To a man of great stature no less..."
                mada "Perhaps one day you'll be a man of stature yourself, earning the right to indulge your desires with me as you please, rescuing me from my fate..."
                bo"*Moans* R-rescuing... y-you?" with vpunch
                mada "But that day is not today, little lamb..." 
                
                menu randommenu2384932453245:
                    "{color=[hatredcolor]}Or so you think!{/color}":
                        call checkHatred(30,"randommenu2384932453245") from _call_checkHatred_36
                        bo "What the fuck do you mean 'not today'?!" 
                        bo "You fucking whore!" with vpunch
                        bo "I'm done letting you play your games..."
                        show screen parallax1280("onsen_intro hatred1") with dissolve
                        call changeHatred(2) from _call_changeHatred_198
                        "You grab Madame by the hair and pull her head forward, a look of shock and disbelief flashing on her face as you stare menacingly at her and growl"
                        bo "You've fucking teased me all night you dumb skank, you think I will settle for only your hand?!"
                        bo "You deluded fucking slut! You'll play by MY rules now!"
                        mada "What the hell has gotten into you! Cease this behaviour immediately!"
                        bo "We both know that's not going to happen, you're mine now bitch..."
                        jump onsen_reward_hatred

                    "{color=[dominancecolor]}Plaster her face{/color}":
                        call checkDominance(15,"randommenu2384932453245") from _call_checkDominance_51
                        bo "F-fuck... You look so perfect down there...!"
                        bo "I can see you thinking about it! You want more too!"
                        mada "Perhaps, but sometimes we must suppress what we crave..."
                        mada "What I want is irrelevant at this point in time, my focus is on giving you release right now."
                        bot "Ahhh f-fuck, it's too much!"
                        bot "She can pretend all she wants, I know she wants it..."
                        bot "I'll give her a small taste of what she craves!" with vpunch
                        bo "F-fuuuck I'm getting close! Your breath on the tip is making me go crazy!"
                        show screen parallax1280("onsen_intro 9_3") with dissolve
                        mada "Oh? Does the proximity of my lips fuel your lust?"
                        mada "Does the thought of them surrounding your head push you over the edge?"
                        bo "It d-does! I want to feel them!"
                        bo "I want to F-FUCK them!" with vpunch
                        bo "F-FUUUCK I'M COMING!" with flash
                        $ renpy.sound.play("/audio/soun_fx/cum8.opus", channel="sfx2", loop=False, relative_volume = 0.3) 
                        show screen parallax1280("onsen_intro 9_4") with flash
                        mada "W-wai-...!"
                        bo "AHHHH!" with vpunch
                        $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.3) 
                        show screen parallax1280("onsen_intro 9_5") with flash
                        mada "No-...!"
                        bo "Y-YESSS!" with vpunch
                        bo "Fuck yes... That felt good!"
                        show screen parallax1280("onsen_intro 9_6") with dissolve
                        mada "Hmmph...!"
                        mada "You did NOT have permission to unload upon me in this fashion, [bo_name]!"
                        bo "O-oh... Forgive me Madame, but you were way too hot to resist..."
                        bo "That beautiful face was basically begging for it by being that close!"
                        mada "Don't be ridiculous, I am way above such sentiments..."
                        show screen parallax1280("onsen_intro 9_5") with dissolve
                        mada "I had no idea you had so much in store for me though!"
                        mada "It is quite remarkable how much you have managed to cover me with."
                        show screen parallax1280("onsen_intro 9_6") with dissolve
                        mada "I suppose I am also to blame, I should have expected as much from an inexperienced boy..."
                        mada "But I must say that I am {i}not{/i} particularly pleased with this outcome!"
                        mada "Let us not make a habit out of this, shall we?"
                        bo "Y-yes Madame, I apologize... \nI was enjoying myself a bit too much to even think of stopping..."
                        mada "Save your breath... Next time just be sure to give ample warning."
                        bot "N-next time?? Fuck, she's already thinking about having more..."
                        bo "O-of course! It won't happen again!"
                        scene black with dissolve
                        mada "Ensure that it doesn't... We'll make a man out of you yet, little lamb..." 
                        call hidescrollingimage from _call_hidescrollingimage_167
                        hide screen parallax1280
                        bot "Fuck, she's never going to drop that is she?"
                        bot "It's ok I guess, she can call me whatever she wants as long as we get to do this again some other time!"
                        mada "Enough entertainment for now... Allow me to wipe us both clean..."
                        "Madame takes a nearby towel and wipes up the mess that the two of you have created, to the best of her ability at least..."
                        scene bg onsen1_night with dissolve
                        show madame undress2 at left 
                        show boruto naked2 at right:
                            zoom 0.37
                        with dissolve
                        mada "[bo_name], what an excellent choice of company you were tonight..."
                        mada "I hope you enjoyed our little escapade here as much as I have."
                        mada "I'm starting to like your family more and more with every encounter! *smirk*"
                        mada "Speaking about family..." 
                        jump madame_massage_minigame_success_initialendingfork
                        
                    "Let her finish you off":
                        bo "I look forward to it, Madame!"
                        bo "I will do whatever it takes to earn that right, and claim you for my own!"
                        show screen parallax1280("onsen_intro 9") with dissolve
                        mada "Oooh? Will you now..."
                        "She pauses for a moment, and looks straight into your eyes as if to measure you..."
                        show v020_madame_titjob6_anim with dissolve
                        show v020_madame_titjob6_anim:
                            easein 9 yalign 0.17
                        mada"Many men say that in the heat of the moment, but not many follow through with their words in the aftermath..."
                        mada"But you... I sense something in you... Something different..."
                        mada "You are not quite like the rest, are you?"
                        mada "I feel the fire of desire burning inside you, a strange heat radiating from your body..."
                        mada "You want me, I know you do... I feel your lust consuming your every thought!"
                        bo "O-of course I do, Madame! I want you so badly right now!"
                        mada "Can you handle me though? As I push you beyond your limits and explore the depths of your desires."
                        bo "I-I can handle everything! I will prove it to you!"
                        mada "Then show me what you are capable of, little lamb..."
                        mada "Show me how much you want this, how much you want me!"
                        mada "Cum for me!"
                        bo "F-FUCK, I WANT Y-YOU!" with flash
                        scene black
                        bo "I'M CUMMING!" with flash
                        $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.3) 
                        show screen parallax1280("onsen_intro 10") with flash 
                        bo "Arrgh! T-take it!*" with flash 
                        $ renpy.sound.play("/audio/soun_fx/cum2.opus", channel="sfx2", loop=False, relative_volume = 0.3) 
                        show screen parallax1280("onsen_intro 10_1") with flash
                        mada "Good boy, watch all that hot cum drip off my hands and body..." 
                        $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.3) 
                        show screen parallax1280("onsen_intro 10_2") with longerflash
                        mada "We'll make a man of you yet, little lamb..." 
                        scene black
                        call hidescrollingimage from _call_hidescrollingimage_168
                        hide screen parallax1280
                        bot "Fuck, she's never going to drop that is she?"
                        bot "It's ok I guess, she can call me whatever she wants as long as we get to do this again some other time!"
                        mada "Enough entertainment for now... Allow me to wipe us both clean..."
                        "Madame takes a nearby towel and wipes up the mess that the two of you have created, to the best of her ability at least..."
                        scene bg onsen1_night with dissolve
                        show madame undress2 at left 
                        show boruto naked2 at right:
                            zoom 0.37
                        with dissolve
                        mada "[bo_name], what an excellent choice of company you were tonight..."
                        mada "I hope you enjoyed our little escapade here as much as I have."
                        mada "I'm starting to like your family more and more with every encounter! *smirk*"
                        mada "Speaking about family..." 
                        jump madame_massage_minigame_success_initialendingfork
                        




label dungeon_secretpassge:
    scene blackscreen with dissolve
    "You follow Madame through a tight pathway connecting the onsen with the palace's catacombs."
    show rangi_secret_pathway with dissolve:
        yalign 1.0
    show rangi_secret_pathway:
        easein 8 yalign 0.0
    mada"These catacombs have been long abandoned. The Daimyo isn't very keen on spending anything less than the bare minimum..."
    mada"Lucky for you, there should be a sewer grate somewhere around here that should lead you to the underground dungeons."
    mada"I wager that is where [hin_name] is held."
    bot "This place gives me the creeps..."
    scene black with dissolve
    show secret_dungeon_grate with dissolve:
        yalign 1.0
    show secret_dungeon_grate:
        easein 5 yalign 0.4
    mada "This is as far as I can go. I can not be seen with you any further... \nDropping through this grate will get you into the furthest depths of the dungeon cells."
    mada "Needless to say, I am taking a massive risk in assisting you with this. \nSo please, let no one ever hear of this..."
    bo "Thank you, Madame... I will never forget your kindness, or your help."
    mada"Your [hin_rel_mother] is worth as much, give her my regards!"
    mada "Good luck, [bo_name]..."
    show secret_dungeon_grate with fade:
        zoom 1.44 xalign 0.6 yalign 0.5
    "You say your goodbyes and carefully remove the iron grate, dropping into the darkness beyond..."
    scene black with dissolve
    stop music fadeout 2
    "..."    
    jump sneak_in_dungeon

label guards_onsen_thrown_out_ending:
    $ playmusic("audio/ost/kokuten.opus",0.3)
    scene black with dissolve
    bot "Fuck, I gotta get outta here!" with vpunch
    play sound "audio/soun_fx/footsteps.opus" volume 0.8
    "You gather yourself and make a dash towards the door."
    "You have no choice now but to abandon your rescue attempt, as you attempt to retrace your steps and circle back to the palace's exit."
    play sound "audio/soun_fx/swordsheathe2.opus" volume 0.8
    show daimyopalace_captured with dissolve:
        yalign 1.0
    show daimyopalace_captured:
        easein 5 yalign 0.3
    "You don't make it very far before the Daimyo's guard surround you."
    "Guards" "There's the little rat!" with vpunch
    "Guard leader" "Don't let him run away this time, capture him!"
    "With nowhere else to go, you are forced to try and maneuver your way past them in order to escape!"
    scene black with dissolve
    play sound "audio/soun_fx/heartbeatlongfast.opus" volume 2
    "Your heart races as you attempt to utilize your nimble agility and whatever stamina you have left remaining."
    "You desperately try to duck, dodge and evade your captors..."
    play sound "audio/soun_fx/fast_blink.opus" volume 0.8
    "But it's no use!" with vpunch
    bot "I knew I shouldn't have skipped leg day..."
    "Guard leader" "Beat his fucking ass!" with vpunch
    play sound "audio/soun_fx/beatdown.opus" volume 0.8
    "Guard" "Can I rail his ass instead?" with vpunch
    "Guard leader" "Wha-...? No, you fucking idiot! Can't you see? It's just a snot-faced kid."
    play sound "audio/soun_fx/bodythud.opus" volume 0.8
    show sneak_dungeon_fail with dissolve:
        yalign 1.0
    show sneak_dungeon_fail:
        easein 5 yalign 0.1
    "Guard leader" "This ought to be a lesson to you kid! Don't sneak in where you don't belong..."
    "The guards beat you to a pulp, before discarding your unconscious body outside the Daimyo's plot."
    "You lay unconscious, darkness enveloping you..."
    stop music fadeout 2

    $ borutocaptured_d14 = True
    scene sneak_dungeon_fail with fade:
        yalign 1.0
    "After almost a day, you wake up with a pounding headache."
    bo"God damn it..."
    jump action_taken