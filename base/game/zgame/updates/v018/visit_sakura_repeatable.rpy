default quest_1h2L_2h2H_inprogress = False

label visit_sakura_repeatable:
    show bg lr uchiha with dissolve
    show sakura normal at right
    show boruto normal at left
    with dissolve
    saku"Glad to see you around our place again!"
    if v21_hinatadate_progression == 2:
        saku "Did you enjoy your time here the other night?"
        show sakura teasing with dissolve
        saku "You seemed a little... distracted *Wink*"
        show boruto embarassed at left with dissolve
        bo "Yeah I wonder why..."
        show boruto normal with dissolve
        bot "Aunt Sakura is such a tease, but [hin_rel] could have caught us at dinner. We should be more careful."
        $ v21_hinatadate_progression = 1
        show sakura normal with dissolve
    saku"Remember our deal? You help your Auntie out, and I'll in turn, help you out!"
    saku"Ready to get some work done?"
    show boruto surprised2 with dissolve
    bo"Am I just picking up your laundry again?"
    show sakura teasing with dissolve
    saku"That you are! Chop, chop! Off you go... *Giggles*"
    saku"And remember, don't snoop around in girl's rooms!"
    if sakura_dildo_found == True:
        show boruto snob with dissolve
        bot"I already found your sex toys laying around, Auntie!"
    show boruto embarassed with dissolve
    bo"R-right..."

    # Quest variable for menu options
    if quest_hin.exists("2_hin2L") or quest_hin.exists("3_hin2H"):
        if quest_hin.is_state("1_hin2L", "in progress") or quest_hin.is_state("2_hin2H", "in progress"):
            $ quest_1h2L_2h2H_inprogress = True 

    menu sakura_menu_repeatable:
        saku"Ready to get some work done?"
        "Help Sakura with chores...":
            bot"Right, I suppose I'll start with the master bedroom..."
            scene black with dissolve
            jump sakura_chores_label
        "{color=[obediencecolor]}Sakura wants something from you{/color}" if sarada_key_to_heart == True:
            default sakura_asked_for_wine = False
            $ sakura_asked_for_wine = True
            saku"[bo_name], I've been thinking about something..."
            saku"But I am afraid I can only share it with you during night-time. Perhaps with a glass of wine in hand too!"
            saku"See if you can fetch your Auntie some alcohol and pay me a visit during nights..."
            saku"And I mean NIGHT! As in... midnight! Ideally while Sarada is asleep! You got it?"
            bo"I'll see what I can do!"
            bot"What is Auntie thinking!?"
            bot"Guess there's only one way to find out..." with vpunch
            bot"I'll check the shop for some wine and visit her during midnight!"
            jump sakura_menu_repeatable

        "Ask about helping [hin_name]" (advancement_event=True) if quest_1h2L_2h2H_inprogress:
            if wine_counter >=1:
                jump v21_hinatadate_quest_start_sakura
            else:
                call randomCheck(False, "Requirements not met") from _call_randomCheck_19
                "Advance Sakura's storyline further to be able to ask for her help!"
                jump sakura_menu_repeatable

        "Information":
            show screen sakuramenuinfo
            jump sakura_menu_repeatable
        "Leave":
            show boruto at smallshake
            bo"Oh, I just remembered! There's something I have to do Auntie, sorry!"
            scene black with dissolve
            bot"I'll come by some other time..."
            jump action_taken



label chores_finished_repeatable_label:
    $ uchihas_visited = True
    show bg lr uchiha with dissolve
    show boruto normal at left with dissolve
    bot"Must be in the kitchen still..."
    show boruto normal:
        easeout 1.5 xpos 1200
    pause 0.2
    scene black with dissolve
    "You make your way to the kitchen..."
    show chores_done sakura0 with dissolve
    show chores_done:
        easein 3 yalign 0.0
    "You catch Sakura in what seems to be a moment of contemplation..."
    show screen parallax1280("chores_done sakura0",1,0.0) with dissolve
    call showscrollingimage from _call_showscrollingimage_94
    menu chores_done_menu_repeatable:
        "You catch Sakura in what seems to be a moment of contemplation..."
        "Wait silently...":
            $ sakura_visit += 1
            if sakura_visit == 1:
                bot"I wonder what she's thinking about..."
                saku"Tsk!" with vpunch
                saku"How much longer must I endure this..."
                saku"At least I've got Sarada. One good thing came from that idiot!" with vpunch
                bot"She really is frustrated with my mentor, huh..."
                hide screen parallax1280
                show screen parallax1280("chores_done sakura1",1,0.0)
                with dissolve
                saku"[bo_name_stutter]! How long have you been standing there for? You caught me in my moment of sulking..."
                bo"I didn't mean to pry Auntie. I just got done with the chores and wanted to check up on you..."
                show screen parallax1280("chores_done sakura0",1,0.0) with dissolve
                saku"*Sigh* Don't get me wrong, I miss Sasuke, but I am also bored out of my mind left alone like this, you know?"
                show screen parallax1280("chores_done sakura1",1,0.0) with dissolve
                saku"But now I have my little handyman here to keep me busy, don't I?"
                saku"Come on, let's go to the living room. I want to talk to you about the idea I've mentioned before!"
                bo"Sure thing."
            elif sakura_visit >= 2:
                saku"Hmm, how far should I go with this idea of mine anyway..."
                saku"Is it even helpful to him? What if he gets the wrong idea..."
                bot"Uuh, I better pretend I've heard none of that."
                show screen parallax1280("chores_done sakura1",1,0.0) with dissolve
                saku"Oh, [bo_name]! My little handyman! *Giggles*"
                saku"Come on, let's go to the living room, spend some time together!"
                bo"Sure thing!"
            elif sakura_visit >= 4:
                saku"Is this the right thing to do...?"
                bot"Is she thinking of what I am thinking?"
                show screen parallax1280("chores_done sakura1",1,0.0) with dissolve
                saku"Oh, [bo_name]! My little handyman! *Giggles*"
                saku"Come on, let's go to the living room, spend some time together!"
                bo"Sure thing."
            scene black with dissolve
        "I am done with the chores!":
            bo"Hey Auntie, I am done with the chores!"
            show screen parallax1280("chores_done sakura1",1,0.0) with dissolve
            saku"Oh, [bo_name]! My little handyman! *Giggles*"
            if sakura_visit == 0:
                saku"Come on, let's go to the living room. I want to talk to you about the idea I've mentioned before!"
            else:
                saku"Come on, let's go to the living room, spend some time together!"
            bo"Sure thing..."
            scene black with dissolve
        "???" if sakura_relationship <48:
            "Perhaps if your relationship was improved first..."
            jump chores_done_menu_repeatable
        "Surprise her!" if sakura_relationship >= 48:
            hide screen parallax1280
            show screen scrollable_scene(initial_ypos=0.0,imagetoadd="chores_done sakura0",facetoadd="sakura boruto_behind")
            with dissolve
            menu:
                bot"What should I do..."
                "{color=[obediencecolor]} Grope her ass!{/color}":
                    "You sneak up behind her..."
                    hide screen scrollable_scene
                    show screen parallax1280("chores_done sakura_ass1",1,1.0)
                    with dissolve
                    $ renpy.sound.play("/audio/soun_fx/grope1.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                    bo "Can't resist a reward for all that hard work, Auntie..."
                    saku "[bo_name_stutter]!?" with vpunch
                    hide screen parallax1280
                    show screen parallax1280("chores_done sakura1_1",1,0.0)
                    with dissolve
                    "She gasps, turning to face you, her cheeks flushing as she swats your hand away."
                    call changesakura(1) from _call_changesakura
                    hide screen parallax1280
                    show screen parallax1280("chores_done sakura1",1,0.0)
                    with dissolve
                    saku "You little devil! That's one way to say 'chores done,' I suppose..."
                    call increaselust(10) from _call_increaselust_202
                    bot"Oh? She seems... unbothered!"
                    scene black with dissolve
                    saku"Come on, let's head on to the living room, but no more over-stepping boundaries, you got it?"
                    bo"Sure thing..."
                    bot"You little tease..."
                "{color=[obediencecolor]} Grope her tits!{/color}":
                    "You sneak up behind her..."
                    bot"I wonder how she'd react to this..."
                    hide screen scrollable_scene
                    show screen parallax1280("chores_done sakura_tits1",1,0.4)
                    with dissolve
                    $ renpy.sound.play("/audio/soun_fx/grope1.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                    bo "Don't mind me! Just checking if you're as tense as you sound, Auntie..."
                    saku "W-what!? Were you here all this time?" with vpunch
                    hide screen parallax1280
                    show screen parallax1280("chores_done sakura1_1",1,0.0)
                    with dissolve
                    "She yelps, stumbling back and pushing your hand away..."
                    saku "Oh, you're bold today! Hands off, unless I say otherwise!" with vpunch
                    call increaselust(10) from _call_increaselust_203
                    scene black with dissolve
                    call changesakura(-1) from _call_changesakura_1
                    saku"You understand why I hesitate, don't you...?"
                    bo"You are just teaching me stuff Auntie, it's not a big deal!"
                    saku"*Sigh...*"
                    hide screen parallax1280
                    show screen parallax1280("chores_done sakura1",1,0.0)
                    with dissolve
                    saku"Come on, let's head on to the living room, but no more over-stepping of boundaries, you got it?"
                    bo"Sure thing..."
                    bot"You little tease..."
                "{color=[hatredcolor]}Spank her ass{/color}":
                    
                    hide screen scrollable_scene
                    scene chores_done sakura0:
                        yalign 1.0
                    with dissolve
                    show chores_done_spankhand with moveinleft
                    $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                    with vpunch
                    hide screen parallax1280
                    show screen parallax1280("chores_done sakura_spanked1",1,0.5)
                    with dissolve
                    call changeHatred(1) from _call_changeHatred_149
                    
                    "You step up and deliver a firm smack, the sound echoing through the kitchen..."
                    bo "Thought you needed a wake-up call, Auntie!"
                    saku "[bo_name_stutter]!? Y-you..." with vpunch
                    hide screen parallax1280
                    show screen parallax1280("chores_done sakura1_1",1,0.0)
                    with dissolve
                    "She jumps, spinning around with a mix of shock and surprise..."
                    call changesakura(-1) from _call_changesakura_2
                    saku "You're asking for trouble now... keep that up, and I might just slap you back!"
                    call increaselust(10) from _call_increaselust_204
                    bot"Don't test me Auntie..."
                    scene black with dissolve
                    hide screen parallax1280
                    show screen parallax1280("chores_done sakura1",1,0.0)
                    with dissolve
                    saku"I see the stupid grin on your face! Don't go thinking for a second I will allow this to be a common occurrence. You get a pass only this one time..."
                    saku"Come on, let's head on to the living room, but no more over-stepping of boundaries, you got it?"
                    bo"Sure thing..."
                    bot"You little tease..."

                
            jump sakura_living_room_label
        
    label sakura_living_room_label:
    call hidescrollingimage from _call_hidescrollingimage_84
    scene black with dissolve


    call changesakura(3) from _call_changesakura_3
    "You spend some time talking about everyday stuff with Sakura, strengthening the bond between the two of you..."
    show sakura_lr 1 with dissolve
    saku"It's always nice to spend time with people you enjoy being around, isn't it?"
    saku"Do you have something else on your mind?"
    default sakura_talk = 0
    menu sakura_menu_repeatable2:
        saku"Do you have something else on your mind?"
        "Talk":
            menu sakura_talkmenu:
                "..."
                "About Sarada..." (greyed_out = (sakura_talk>=1)):
                    if sakura_talk == 0:
                        $ sakura_talk += 1
                    jump sakura_talk1
                "About your Husband..." (greyed_out = (sakura_talk>=2)) if sakura_relationship >= 10:
                    if sakura_talk == 1:
                        $ sakura_talk += 1
                    jump sakura_talk2
                "I stumbled upon something in your bedroom..." if sakura_relationship >= 30 and sakura_dildo_found == True:
                    jump sakura_talk3
                "???" if sakura_relationship < 10:
                    "Perhaps if your relationship was improved first..."
                    jump sakura_talkmenu
                "???" if sakura_relationship < 30:
                    "Perhaps if you stumbled upon a particular item first, along with improving your relationship first..."
                    jump sakura_talkmenu
                "{color=[obediencecolor]}About the wine you asked for...{/color}" if sakura_asked_for_wine == True:
                    saku"Did you find some?" with vpunch
                    $ wine_in_inventory = inventory.find_item_by_name("Wine")
                    if wine_in_inventory!= None:
                        bo"I got some!"
                        saku"Yaaay!" with vpunch
                        saku"Come by during midnight and we shall drink our sorrows away. Together of course!"
                        bo"O-okay..."
                        bot"Interesting proposition!"
                        jump sakura_talkmenu
                    else:
                        bo"N-not yet. I was just wandering what it is for..."
                        saku"Why to drink it of course! What else..."
                        saku"Come on then, get to it! Chop chop..."
                        jump sakura_talkmenu

                    jump sakura_talkmenu
                "Return":
                    jump sakura_menu_repeatable2


              
        "Interact":
            menu:
                "..."
                "{color=[obediencecolor]}A lesson in intimacy...{/color}":
                    jump sakura_lesson1
                "{color=[obediencecolor]}The secret to a woman's heart...{/color}" if sakura_relationship >= 35:
                    default sarada_key_to_heart = False
                    $ sarada_key_to_heart = True
                    saku"[bo_name], I've been thinking..."

                    jump sakura_lesson2

                "The key to HER heart..." if sakura_relationship >= 35 and sarada_key_to_heart == True and sarada_reintro_complete == False:
                    saku"I think it's about time you make a move, don't you think?"
                    bo"You want me to... w-with you!?" with vpunch
                    saku"Not with me you idiot! *Giggles*"
                    saku"With Sarada obviously... Why do you think I've taken it on me to show you a few things?"
                    saku"Because I want to see the two of you blossom of course..."
                    bo "I don't know, Auntie... I mean, I do like Sarada, but she is so... \nDifficult to deal with at times!"
                    bo "She always gives me the cold shoulder and avoids me like the plague!"
                    saku "That's just her way of showing she cares, [bo_name]..."
                    bo "You say that Auntie, but I'm still convinced that she hates me!"
                    saku "Remember this [bo_name]... \nThe opposite of love is not hate, it is indifference!"
                    saku "If she didn't care, she wouldn't act the way she does. She would just ignore you and not go out of her way to antagonize you!"
                    saku "But she doesn't, does she? \nShe gets angry, she lashes out, she avoids you..."
                    saku "Your presence and actions affect her! Deep down they matter to her!"
                    bo "It's quite a weird way to show someone you care, Auntie... \nDon't you think?"
                    saku "Perhaps... But that's just how Sarada is wired. She's an Uchiha, after all!"
                    saku "Lucky for you though, you have me to help! *wink*"
                    bo "How exactly though? I mean, I'm not even sure what to do, or how to approach her..."
                    saku "That's where I come in! Remember how I said that your actions affect her?"
                    bo "Yeah? Everything I seem to do just pisses her off!"
                    saku "That's because you don't know how to read her, [bo_name]! You don't understand what she wants, or what she {i}needs{/i}!"
                    saku "Let's change that!"
                    saku "You know what they say... \nThe way to a person's heart is through their stomach!"
                    bo "Huh? Now you're just making me hungry..."
                    saku "Come on, you silly goose!"
                    saku "Don't you remember? Every time you used to train together I had this little bento box prepared for you..."
                    saku "You'd train for hours at times, and then sit under a tree and share the moment!"
                    saku "I still remember how giddy Sarada was after spending that time with you."
                    bo "A bento box, hmm? Are you suggesting we try that again?"
                    saku "Exactly!"
                    saku "It will be a great way to show her that you care, and that you're willing to put in the effort!"
                    saku "Not only is it a kind and romantic gesture, but it will also remind her of all the good times you two had together when you were younger!"
                    saku "And who knows, maybe it will even rekindle some old feelings! Bring her back to her old self!"
                    bo "It's certainly worth a shot!"
                    bot "Although I doubt Sarada will ever come around. She's always been quite stubborn..."
                    saku"So...? Down for some cooking?" with vpunch
                    bo "Uuuhm, yes! But I could probably use your help on that one..."
                    bo "I don't know the first thing about cooking!" with vpunch
                    saku "*giggle* Men and their cooking skills, am I right?"
                    saku "It's a good thing you've grown up to be such a handsome young man, otherwise you'd be doomed to a life of solitude with instant ramen and takeout!"
                    bo "Hey! I'm not sure whether to be flattered or insulted by that!"
                    scene black with dissolve
                    saku "Come on, quickly! Let's focus on the task at hand before Sarada returns from the academy."
                    # saku "Come with me! I have everything we need in the kitchen!"
                    jump sarada_bento_intro

                "{color=[obediencecolor]}???{/color}" if sakura_relationship < 35:
                    "Perhaps if your relationship with Sakura was improved first..."
                    jump sakura_menu_repeatable2

                
                "{color=[obediencecolor]}???{/color}" if sakura_relationship < 35 and sarada_key_to_heart == False:
                    "Perhaps if you learned something from Sakura first..."
                    jump sakura_menu_repeatable2
                "Return":
                    jump sakura_menu_repeatable2
        "Information":
                show screen sakuramenuinfo
                jump sakura_menu_repeatable2
        "Leave":
            scene black with dissolve
            bot"I have to get going now Auntie!"
            scene black with dissolve
            call changesakura(1) from _call_changesakura_4
            "You leave the household after spending some time with Sakura..."
            jump action_taken
        

    label sakura_talk1:
        # Sakura talks to Boruto bout sarada's feelings
        saku"Actually, there's something I wanted to talk to you about!"
        saku"Sarada..."
        saku"Surely you know by now why she acts the way she does towards you, don't you?"
        bo"Uuuh, I can venture a guess, but with the way she acts I can only assume she hates my guts!"
        saku"*Sigh...* Sarada could never hate you, [bo_name]. Quite the opposite in fact..."
        saku"The way she acts stems from how oblivious you are to the fact that she harbors... feelings for you!"
        bo"F-feelings?" with vpunch
        saku"Why yes, feelings! Of course I can't be certain if those are feelings of hate, or perhaps love? *Giggles* Or mayhaps something in between!"
        bo"Then why the hell would she constantly cuss me out and avoid me..."
        saku"You see, women can be a mystery, more so to a man. At times, we'll act emotionally, perhaps even irrationally because of how intense and volatile those emotions are..."
        saku"When someone like you does something to stir those feelings up, whether by accident or not, it can get... complicated!"
        saku "I won't spell out why things are so tense between you two, that's for you to figure out. But I will say this:"
        saku "Find the answer, and you'll hold the key to her heart. Maybe more!"
        saku "Until then, I'll do what I can to guide you along the way. A little auntie wisdom never hurt, right?"
        bo "Uh... yeah, Thanks!"
        bot"Sarada's... got feelings, for me?"
        jump sakura_menu_repeatable2


    
    label sakura_talk2:
        # Sakura talks to Boruto about her frustrations with her husband
        bo "Auntie... about Uncle Sasuke..."
        bo "How long's he been gone this time?"
        saku "That damned husband of mine—ugh! I love him, N-no I hate him, I really do, but I'm so over his tragic hero routine."
        saku "Always off on some 'vital mission,' leaving me here to rot. Does he even realize I have needs too?"
        saku "When he's gone for months on end, what's a woman supposed to do? Knit? Stare at the walls? A woman has... needs, you know!"
        "The word hangs there, heavy and suggestive..."
        bo "Uh... I-I get it, Auntie. That's gotta be rough."
        saku "*Sigh* Sorry, [bo_name]. I shouldn't unload all this on you. It's just... lonely, you know?"
        "She softens, brushing a strand of hair behind her ear, her vulnerability tugging at you—and the curse."
        saku "Anyway, enough about my mess. How about you? How's that... condition of yours treating you?"
        "Was her shift in tone  deliberate? You wondered, as her eyes flickered to yours with a hint of curiosity..."
        call increaselust(10) from _call_increaselust_205
        jump sakura_menu_repeatable2

    label sakura_talk3:
        bo "Auntie, I swear I wasn't snooping or anything—it was just... there, out in the open in your bedroom..."
        saku "[bo_name]...? What are you going on about?"
        bo "Uh, you know... I found this weird-looking toy. Kinda shaped like a, uh... p-penis..."
  
        saku "W-what!?"
        "Her eyes widen, she was caught off guard."
        saku "Oh gods, you mean—oh, that's... um..."
        saku "T-that's just... a personal item, okay? Let's not make a big deal out of it!"
        bo "A personal item, huh? Didn't know you were into that kinda thing, Auntie."
        saku "[bo_name]! You little... don't you dare tease me about this!"
        saku "A woman's got to manage somehow when her husband's never around, alright? Let's leave it at that."
        bo "Fair enough. Your secret's safe with me."
        saku "*sigh* You're trouble, you know that? Just... don't go poking around my room again, got it?"

    label sakura_lesson1:
        $ initialize_replay_defaults()
        bo"What about our agreement, Auntie?"
        scene black with dissolve
        saku"Oh, you don't think I've forgotten, did you?"
        show bg lr uchiha with dissolve
        show sakura teasing at right:
            zoom 1.0
        show boruto surprised at left
        with dissolve
        show sakura:
            easein 3 xpos 870
        saku"I was just waiting for you to take some initiative. I like a man with initiative, a man that knows what he wants! *Giggles*"

        show sakura at smallshake
        saku"So... I've been thinking!"
        show boruto surprised at left with dissolve
        bo"..."
        saku"The way I see it..."

        "Sakura steps closer, her hand brushing your shoulder in a warm, reassuring gesture."
        saku"You could probably use a mentor to teach you a few things regarding girls, don't you think?"
        show boruto surprised3 with dissolve
        show boruto at smallshake
        "Her fingers linger, tracing a slow circle around your shoulder..."
        bo"That'd be n-nice..." with vpunch
        scene black with dissolve
        saku "I mean, if someone were to date my Sarada, hypothetically speaking of course, I'd rather they weren't a total klutz around women!"
        show bg lr uchiha
        show sakura_hug 1
        with dissolve
        saku "Take your [na_rel] for example, [na_name]'s always off somewhere, just like my idiot husband, and clueless about women to boot. I doubt he's taught you much, right?" with vpunch
        saku "And [hin_name]? Sweet as she is, and as much as I respect her, she's just too damn shy to give you the real talk, I am sure!"
        saku"Lucky for you, this is my specialty!"
        scene black with dissolve
        saku"So tell me, [bo_name]..."
        scene sakura_hug 3 with dissolve
        show sakura_hug:
            easein 3 yalign 0.1
        "Her voice drops, teasing and low, her eyes locking onto yours as she leans in closer, grasping you into her arms..."
        saku"Do you know your way around a girl's advances?"
        menu sakura_hug_menu_repeatable:
            saku"Do you know your way around a girl's advances?"
            "Pull her closer":
                saku"Do you know what a girl is looking for when she opens herself up to you?"
                bo"I think so..."
                scene bg lr uchiha
                show sakura_hug 2
                with dissolve
                "You slide your hands around her waist, pulling her gently closer. Her warmth presses against you..."
                saku "Not too passive, not too forward—nice! A solid move to test the waters."
                saku "What comes next isn't up to you, it's all about how she reacts."
                show sakura_hug 1_1shy with dissolve
                saku "Every woman's different, you know. Some like it slow, some crave boldness. Do you think you can guess your Auntie's type?"
                "Her shy smile dares you to answer, her breath catching slightly as she waits..."
                menu:
                    "Her shy smile dares you to answer, her breath catching slightly as she waits..."
                    "{color=[lovecolor]}Lean in for a kiss..{/color}":
                        show sakura_hug 4 with dissolve:
                            zoom 1.5 xalign 0.45 yalign 0.3
                        bot"She is so close, I can even feel her breath..."
                        jump leaninforakiss
                    "Make a bold move!":
                        bot"It's almost as if she is... daring me to do something!"
                        bot"In that case..."
                        bo"Auntie..."
                        show sakura_hug bold1 with dissolve
                        $ renpy.sound.play("/audio/soun_fx/grope1.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                        call checkSakura(30) from _call_checkSakura
                        if sakura_relationship >= 30:
                            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp1.opus", channel="sfx1", loop=False, relative_volume = 1.5)
                            saku"*Gasps* Oh m-my, [bo_name]" with vpunch
                            bo"I would have never guessed you were that type of a woman!"
                            show sakura_hug:
                                easein 1 yalign 0.0
                            saku"You are one eager boy, aren't you..." with vpunch
                            show sakura_hug:
                                easein 1 yalign 1.0

                            menu sakuramenu_pickup:
                                saku"You are one eager boy, aren't you..."
                                "{color=[dominancecolor]}Pick her up!{/color}":
                                    call checkDominance(25,"sakuramenu_pickup") from _call_checkDominance_26
                                    bo"Only as eager as you are, Auntie!"
                                    bo"...Ready?" with vpunch
                                    if is_opportunity_unlocked("l1_opportunity3", strength):
                                        pass
                                    else:
                                        saku"R-ready for what exactl-?"
                                        show bg lr uchiha:
                                            blur 20
                                        show sakura_hug bold2t:
                                            xalign 1.0
                                        with dissolve
                                        saku"[bo_name_stutter]!" with vpunch
                                        bo"Hnn--hgg!" with vpunch
                                        bot"O-oh shit! S-she is heavier than I expected..."
                                        scene black with vpunch
                                        $ renpy.sound.play("/audio/soun_fx/intro/bodythud.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                                        saku"Ouch-ch-ch-ch!" with vpunch
                                        call changesakura(-2) from _call_changesakura_5
                                        saku"W-what the hell was that for, [bo_name]..."
                                        show bg lr uchiha with dissolve
                                        show sakura angry at right:
                                            zoom 1.0
                                        show boruto surprised3 at left with dissolve
                                        with dissolve
                                        bo"I am sorry, you were j-just a little heavier than I expected..."
                                        saku"Oh I am heavy now, am I? You little..."
                                        show boruto embarassed with dissolve
                                        bo"I didn't mean it like that! Eh-eh..."
                                        call changesakura(-2) from _call_changesakura_6
                                        show sakura serious with dissolve
                                        saku"Maybe you are just a LITTLE too weak, huh? Thought of that?"
                                        saku"*Sigh*... Picking up your Auntie like that, what were you thinking?"
                                        show boruto worried with dissolve
                                        bo"S-sorry..."
                                        show sakura normal with dissolve
                                        show sakura at smallshake
                                        saku"Lost the wind from your sails now, have you? *Giggles*..."
                                        saku"Don't go pulling off moves way outside of your comfort zone, otherwise you risk awkward moments, just like this one!"
                                        saku"But don't worry, I understand..."
                                        show sakura teasing with dissolve
                                        saku"You wanted to prove to your Auntie how strong and mighty you were, huh?"
                                        scene black with dissolve
                                        show sakura walking_away with dissolve
                                        saku"Too bad you fumbled that real good! *Giggles*"
                                        saku"I am getting tired now, so..."
                                        "You couldn't help but stare at her alluring hips being swayed from one side to another with every tender step she made..."
                                        call increaselust(10) from _call_increaselust_206
                                        bot"Auntie... you can't just keep teasing me with that ass and expect me not to reach for it!"
                                        hide sakura walking_away with dissolve
                                        jump sakura_repeatable_ending_good
                                    saku"R-ready for what exactl-?"
                                    show bg lr uchiha:
                                            blur 20
                                    show sakura_hug bold2t:
                                        xalign 1.0
                                    with dissolve
                                    saku"[bo_name_stutter]!" with vpunch
                                    bo"Only as eager as my favourite Auntie is!" with vpunch
                                    saku"*Gasp!* [bo_name]! Put your Auntie down at once! *Giggles*" with vpunch
                                    bo"Only if you say please..."
                                    "You picked her up with ease, your hands firmly planned on her buttocks..."
                                    saku"W-why you! *Playful Giggles* Alright, will you please put me down?"
                                    call increaselust(10) from _call_increaselust_207
                                    if percentage >=90:
                                        call checkLust(200) from _call_checkLust_13
                                        "Feeling her body's warmth, her breasts rubbing against your torso, with your hands so close to where they shouldn't be..."
                                        show sakura_hug bold2_1t with dissolve
                                        bot"O-oh shit! My..." with vpunch
                                        saku"H-hey! W'what's that poking me down there..."
                                        $ renpy.sound.play("/audio/soun_fx/intro/bodythud.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                                        scene black with vpunch
                                        "Her sudden intrigue threw you off balance, causing you to accidentally drop her on the floor.."
                                        saku"Ouch-ch-ch-ch!" with vpunch
                                        call changesakura(-2) from _call_changesakura_7
                                        saku"W-what the hell was that for, [bo_name]..."
                                        "You tried to hide the evidence before Sakura could realize..."
                                        show bg lr uchiha with dissolve
                                        show sakura angry at right:
                                            zoom 1.0
                                        show boruto bonersurprised at left with dissolve
                                        with dissolve
                                        saku"You should be more carefu-"
                                        show sakura shy with dissolve
                                        show sakura at smallshake
                                        saku"Oh my! Is that..."
                                        sakut"Is it my f-fault? Have I let him get... too close?"
                                        bo"A-auntie, I am sorry, it's just that-"
                                        call changesakura(-2) from _call_changesakura_8
                                        saku"[bo_name], It's okay. It's my fault. I should have never let things get out of control in the first place..."
                                        saku"Uhm, I think it's best you head home now, okay?"
                                        saku"I know you are dealing with your... p-problem as best as you can, [hin_name] told me as much..."
                                        saku"You can come back when things get better, alright?"
                                        bo"S-sure..."
                                        scene black with dissolve
                                        "Sakura gently let you know that you should go, but not without an invitation for when things get better..."
                                        
                                        jump action_taken

                                        

                                    else:
                                        call checkLust(0) from _call_checkLust_14
                                        bo"If that is my Auntie's wish..."
                                        show sakura_hug:
                                            easeout 3 xpos 2600
                                        saku"My oh my, when did you grow so strong anyway. Carrying your Auntie like it's nothing..."
                                        saku"I am probably heavier than you are! *Giggles*"
                                        scene black with dissolve
                                        bo"Oh please, Auntie! You are as light as a feather..."
                                        bo"Brace!"
                                        $ renpy.sound.play("/audio/soun_fx/intro/bodythud.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                                        saku"Ah!" with vpunch
                                        show sakura_lr 1 with dissolve
                                        call changesakura(2) from _call_changesakura_9
                                        saku"*Giggles* Huhu! Strong and bold, aren't you..."
                                        "You gently dropped her on one of the living room couches..."
                                        saku"You keep surprising me in interesting ways, [bo_name]!"
                                        bo"Hehe! You ever need a piggy back ride, let me know!"
                                        saku"Ooh... I might take you up on that at some point, sounds like a fun ride!"
                                        call increaselust(20) from _call_increaselust_208
                                        bot"A fun ride, huh? Auntie..."
                                        saku"But your Auntie is getting tired by now..."
                                        jump sakura_repeatable_ending_good


                                        


                                "{color=[obediencecolor]}Turn the tables on her...{/color}":
                                    bo"Only as eager as you are..."
                                    show sakura_hug bold1_1 with dissolve
                                    "You raise your hand in preparation of your next move..."
                                    scene black with dissolve
                                    saku"What's that supposed to mean [bo_name]..." with vpunch
                                    show bg lr uchiha:
                                        blur 20
                                    show sakura_kiss 1
                                    with dissolve
                                    saku"You are not getting the wrong idea here, are you?"
                                    bo"I don't know Auntie..."
                                    show sakura_hug bold1_1 with dissolve
                                    show sakura_hug bold1_2 with dissolve
                                    $ renpy.sound.play("/audio/soun_fx/intro/spank4.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                    bo"...Am I?" with vpunch
                                    "You tired to match her playful energy, but a light tap of her bottom might have been too much..."
                                    scene black with vpunch
                                    saku"H-hey! Stop it..."
                                    show bg lr uchiha:
                                        blur 10
                                    show sakura_hug 1_1shy
                                    with dissolve
                                    saku"I think you did get the wrong idea after all..."
                                    saku"Remember why we are doing this...?"
                                    scene bg lr uchiha with dissolve
                                    show sakura shy at right:
                                        zoom 1.0
                                    show boruto surprised at left
                                    with dissolve
                                    saku"First, for your sake and then..."
                                    show sakura normal with dissolve
                                    saku"For somebody else's! *Giggles*"
                                    show sakura serious with dissolve
                                    saku"And that's not me!" with vpunch
                                    saku"So you better not be thinking of getting too handsy with me, alright?"
                                    show boruto surprised3 with dissolve
                                    bo"R-right..."
                                    show sakura normal with dissolve
                                    saku"*Giggles* Relax, I am not mad at you. It was just... an interesting choice of motions from you!"
                                    saku"You should save that for the one, you know? You can't just do something like that with your Auntie..."
                                    scene black with dissolve
                                    show sakura walking_away with dissolve
                                    saku"I'll drop it here, but I do hope you understand..."
                                    "You couldn't help but stare at her alluring hips being swayed from one side to another with every tender step she made..."
                                    call increaselust(10) from _call_increaselust_209
                                    bot"Auntie... you can't just keep teasing me with that ass and expect me not to reach for it!"
                                    hide sakura walking_away with dissolve
                                    jump sakura_repeatable_ending_good


                                


                            show bg lr uchiha
                            show sakura_hug 1_1shy
                            with dissolve
                            "Sakura snatches at your hands, placing them back to her waist instead..."
                            saku "T-there's such a thing as too direct, you know! *Awkward chuckle*"
                            saku"You can't just touch a woman like that you know..."
                            saku"You'll have to follow her lead, or at the very least, look for signs..."
                            scene black with dissolve
                            bo"R-right..."
                            "Sakura was slightly flustered, she gave you a playful shove to break the tension, ending her 'lesson' for now..."
                            call changesakura(-1) from _call_changesakura_10
                            scene bg lr uchiha with dissolve
                            show sakura shy at right:
                                zoom 1.0
                            show boruto surprised at left
                            with dissolve
                            saku"Today you may have failed the test, but you will surely get another chance soon..."
                            show sakura angry with dissolve
                            saku"Remember, be too direct and you'll scare off most sane woman away! Be too clueless and you risk never getting to shoot your shot entirely!"
                            show boruto embarassed with dissolve
                            bo"Got it, I think..."
                            hide sarada with dissolve
                            saku"*Sigh...*"
                            scene black with dissolve
                            saku"That'll be all for today. Auntie's tired, and you're getting a little too eager, [bo_name]..."
                            "Sakura turns away from you and walks down the living room..."
                            show sakura walking_away with dissolve
                            "You couldn't help but stare at her alluring hips being swayed from one side to another with every tender step she made..."
                            call increaselust(10) from _call_increaselust_210
                            bot"Auntie... you can't just keep teasing me with that ass and expect me not to reach for it!"
                            hide sakura walking_away with dissolve
                            jump sakura_repeatable_ending_good


                        else:
                            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp1.opus", channel="sfx1", loop=False, relative_volume = 1.5)
                            saku"*Gasps* [bo_name_stutter]..." with vpunch
                            bo"I would have never guessed you were that type of a woman!"
                            show sakura_hug:
                                easein 1 yalign 0.0
                            saku"N-no, [bo_name_stutter]..." with vpunch
                            show bg lr uchiha
                            show sakura_hug 1_1shy
                            with dissolve
                            "Sakura snatches at your hands, placing them back to her waist instead..."
                            saku "T-there's such a thing as too direct, you know! *Awkward chuckle*"
                            saku"You can't just touch a woman like that you know..."
                            saku"You'll have to follow her lead, or at the very least, look for signs..."
                            scene black with dissolve
                            bo"R-right..."
                            "Sakura was slightly flustered, she gave you a playful shove to break the tension, ending her 'lesson' for now..."
                            call changesakura(-1) from _call_changesakura_11
                            scene bg lr uchiha with dissolve
                            show sakura shy at right:
                                zoom 1.0
                            show boruto surprised at left
                            with dissolve
                            saku"Today you may have failed the test, but you will surely get another chance soon..."
                            show sakura angry with dissolve
                            saku"Remember, be too direct and you'll scare off most sane woman away! Be too clueless and you risk never getting to shoot your shot entirely!"
                            show boruto embarassed with dissolve
                            bo"Got it, I think..."
                            hide sarada with dissolve
                            saku"*Sigh...*"
                            scene black with dissolve
                            saku"That'll be all for today. Auntie's tired, and you're getting a little too eager, [bo_name]..."
                            "Sakura turns away from you and walks down the living room..."
                            show sakura walking_away with dissolve
                            "You couldn't help but stare at her alluring hips being swayed from one side to another with every tender step she made..."
                            call increaselust(10) from _call_increaselust_211
                            bot"Auntie... you can't just keep teasing me with that ass and expect me not to reach for it!"
                            hide sakura walking_away with dissolve
                            jump sakura_repeatable_ending_good
                        


                    
            "{color=[dominancecolor]}Reach for her chest!{/color}":
                call checkDominance(20,"sakura_hug_menu_repeatable") from _call_checkDominance_27
                show sakura_hug with dissolve:
                    easein 1 yalign 0.5
                bo"I am not too sure about a girl's advances..."
                scene bg lr uchiha
                show sakura_hug 1
                with dissolve
                bo"But..."
                sakut"Is he staring at my-"
                scene sakura_hug gropetits with dissolve
                call changeDominance(1,"sakuragropetits") from _call_changeDominance_90
                bo"I am pretty good at making the first move myself!" with vpunch
                show sakura_hug:
                    easein 0.5 yalign 0.1
                bo"Even more so with pretty girls like you, Auntie!" with vpunch
                scene black with dissolve
                saku"[bo_name_stutter]!" with vpunch
                show bg lr uchiha
                show sakura_hug 1_1shy
                with dissolve
                "Sakura snatches your wrist, guiding it firmly to her waist instead. Her cheeks flush, but her eyes flicker with an unreadable mix of emotion..."
                saku "T-there's such a thing as too direct, you know! *awkward chuckle*"
                saku "You can't just go for the prize without a little buildup, you know? It's a game you cannot rush through!"
                saku "B-besides, this is supposed to be educational. I set the pace, you follow. Got it?"
               
                show sakura_hug 1 with dissolve
                bot"Auntie looks relatively relaxed! Maybe I could push her further...?"
                saku "I see those wandering eyes! I asked you a question, young man—focus!" with vpunch
                scene black with dissolve
                bo"R-right..."
                "Sakura smirks, giving you a playful shove to break the tension, ending her 'lesson' for now..."
                call changesakura(1) from _call_changesakura_12
                scene bg lr uchiha with dissolve
                show sakura teasing at right:
                    zoom 1.0
                show boruto surprised at left
                with dissolve
                saku"Today you may have failed the test, but you will surely get another chance soon..."
                show sakura angry with dissolve
                saku"Remember, be too direct and you'll scare off most sane woman away! Be too clueless and you risk never getting to shoot your shot entirely!"
                show boruto embarassed with dissolve
                bo"Got it, I think..."
                hide sarada with dissolve
                saku"*Sigh...*"
                scene black with dissolve
                saku"That'll be all for today. Auntie's tired, and you're getting a little too eager, [bo_name]..."
                jump sakura_repeatable_ending_good
            "Pull off a romantic move...":
                scene bg lr uchiha
                show sakura_hug 1_1 with dissolve
                bot"I better show Auntie I am not a complete idiot if I want this to go somewhere..."
                bot"But what the hell do I even do!" with vpunch
                show sakura_hug at smallshake
                saku"...So?"
                scene sakura_hug 3 with dissolve:
                    yalign 0.0
                show sakura_hug:
                    linear 4 yalign 0.3
                saku"...So?"
                "You raise your hand and trace hers, brushing your fingers against her soft skin, until your palms meet..."
                scene sakura_hug 4 with dissolve
                "Your hands interlock, a quiet intimacy settles between the two of you..."
                show sakura_hug:
                    easein 6 yalign 0.3
                saku"Aww, so sweet, so sentimental!"
                saku"Plenty of girls will enjoy romantic gestures like this, but some will expect you to make a bolder move..."
                saku"You'll have to make the call based on the woman's body language, so..."
                menu:
                    saku"You'll have to make the call based on the woman's body language, so..."
                    "{color=[obediencecolor]}I bet I know which kind you are, auntie!{/color}":
                        bo "I bet I can guess your type, Auntie..."
                        scene sakura_hug_behind with dissolve:
                            yalign 1.0
                        show sakura_hug_behind:
                            easein 6 yalign 0.0
                        "You tug her arm gently, pulling her close, your arm wrapping around her stomach as her back presses against you."
                        bo"...You're the romantic kind, aren't you?"
                        call checkSakura(15) from _call_checkSakura_1 
                        if sakura_relationship >= 15:
                            pass
                        else:
                            scene bg lr uchiha:
                                blur 5
                            show sakura_hug_behind t:
                                zoom 0.7 xalign 0.5
                            saku"Oh m-my, [bo_name]..."
                            call changesakura(1) from _call_changesakura_13
                            saku"Making moves now, aren't you? But..."
                            show blackscreen with vpunch
                            hide sakura_hug_behind t
                            "Sakura gently pushes you off, rejecting your advance..."
                            hide blackscreen
                            show boruto surprised2 at left
                            show sakura normal at right
                            with dissolve
                            saku"You might be moving a little bit too fast..."
                            saku"But don't be hesitant to make a romantic move if a situation calls for it."
                            show sakura teasing with dissolve
                            saku"A girl will let you know how to proceed, or she'll put you down gently... *Giggles*"
                            saku"All you have to do is look for the signs she puts out. Understood?"
                            show boruto embarassed with dissolve
                            bo"I... t-think so?"
                            show sakura at smallshake
                            saku"Then that'll be all for today!"
                            scene black with dissolve
                            saku"You still have ways to go I am afraid... *Giggles*"
                            jump sakura_repeatable_ending_good
                        saku "*Giggles* Oh, you think so? Maybe I am..."
                        "Sakura doesn't resist but instead, her hand slides up to your neck, drawing you nearer, her breath warm against your skin..."
                        scene bg lr uchiha:
                                blur 5
                        show sakura_hug_behind t:
                            zoom 0.7 xalign 0.5
                        saku"Or maybe I'd prefer a guy who can surprise me..." with vpunch
                        menu sakura_move1:
                            saku"Or maybe I'd prefer a guy who can surprise me..."
                            "Move your hand to her waist":
                                show sakura_hug_behind 2t with dissolve
                                bo "How's this for a surprise, Auntie?"
                                saku "Mmm, smooth... a little spark to stir the romance."

                            "Move your hand to her ass":
                                show sakura_hug_behind 2asst with dissolve
                                "Your hand dips lower, cupping her ass with a teasing squeeze."
                                bo "Thought I'd spice things up a bit, Auntie."
                                call changesakura(-1) from _call_changesakura_14
                                show sakura_hug_behind 2asst at smallshake
                                saku "Oh! Naughty boy, you're pushing it already!" with vpunch
                                show sakura_hug_behind t with dissolve
                                "She swats your hand away, giggling, but her eyes flash with mischief."
                                saku"You can't just jump steps you know! You may think it's romantic..."
                                jump sakura_ending_mild
                            "Slide your hand under her top":
                                show sakura_hug_behind 2tits_1t with dissolve
                                saku"O-oh!?" with vpunch
                                "Your fingers slip under her shirt, grazing her bare skin."
                                bo "Just warming you up, Auntie..."
                                call changesakura(-3) from _call_changesakura_15
                                show sakura_hug_behind t with dissolve
                                saku "[bo_name_stutter]! Too bold, too soon!" with vpunch
                                "She squirms, pulling back with a flustered laugh."
                                jump sakura_ending_bad
                        
                        call checkSakura(25) from _call_checkSakura_2 
                        if sakura_relationship >= 25:
                            pass
                        else:
                            label sakura_ending_mild:
                            scene bg lr uchiha:
                                blur 5
                            show sakura_hug_behind t:
                                zoom 0.7 xalign 0.5
                            saku"But romance first, needs to simmer!"
                            
                            saku"You cannot rush into it, understood?"
                            show blackscreen with vpunch
                            hide sakura_hug_behind t
                            "Sakura gently pushes you off, rejecting your advance..."
                            hide blackscreen
                            show boruto surprised2 at left
                            show sakura normal at right
                            with dissolve
                            call changesakura(1) from _call_changesakura_16
                            saku"Although I have to admit, that wasn't bad!"
                            saku"Keep your eyes peeled for cues, and a girl will let you know how to proceed..."
                            show sakura teasing with dissolve
                            saku"But you can't exactly do that with your Auntie now, can you? *Giggles*"
                            show sakura at smallshake
                            saku"Then that'll be all for today!"
                            scene black with dissolve
                            saku"Don't worry though, you are slowly getting there!"
                            "Sakura turns away from you and walks down the living room..."
                            show sakura walking_away with dissolve
                            "You couldn't help but stare at her alluring hips being swayed from one side to another with every tender step she made..."
                            call increaselust(10) from _call_increaselust_212
                            hide sakura walking_away with dissolve
                            jump sakura_repeatable_ending_good
                            

                        saku "But now intimacy is brewing, and we are both feeling some heat! *Giggles* It's on you to handle that..."
                        "Sakura seemed to enjoy your subtle advances. Her calm expression tempted you to go further..."
                        saku"So... What next, young man?"
                        menu sakura_move2:
                            saku"So... What next, young man?"
                            "Move your hand lower":
                                show sakura_hug_behind 2asst with dissolve
                                "Your hand drifts down her waist, resting just above her hips, teasing the boundary."
                                bo "How's this feel, Auntie?"
                                pass
                            "Slide your hand under her pants":
                                show sakura_hug_behind 2pantst with dissolve
                                "Your fingers slip beneath her waistband, brushing her skin with intent."
                                bo "Thought I'd heat things up even more, Auntie!"
                                saku "Oh my—slow down, hotshot!" with vpunch
                                call changesakura(-2) from _call_changesakura_17
                                show sakura_hug_behind t with dissolve
                                "She grabs your wrist, nervously laughing as she pulls away."
                                jump sakura_ending_bad
                            "Slide your hand under her top":
                                show sakura_hug_behind 2tits_1t with dissolve
                                "Your hand sneaks under her shirt, grazing her chest."
                                bo "I Can't help myself around you, Auntie..."
                                call changesakura(-2) from _call_changesakura_18
                                saku "Hey! Handsy already?" with vpunch
                                show sakura_hug_behind t with dissolve
                                "She twists free, her tone scolding but playful."
                                
                                jump sakura_ending_bad
                        call checkSakura(30) from _call_checkSakura_3 
                        if sakura_relationship >= 30:
                            pass
                        else:
                            label sakura_ending_bad:
                            scene bg lr uchiha:
                                blur 5
                            show sakura_hug_behind t:
                                zoom 0.7 xalign 0.5
                            saku"You are doing good, really! But..."
                            
                            show blackscreen with vpunch
                            hide sakura_hug_behind t
                            "Sakura gently pushes you off, rejecting your advance..."
                            hide blackscreen
                            show boruto surprised2 at left
                            show sakura shy at right
                            with dissolve
                            call changesakura(1) from _call_changesakura_19
                            saku"Sometimes a girl might push you off, even when there's seemingly no reason for it..."
                            bo"W-what do I do then..."
                            show sakura normal with dissolve
                            saku"Well in that case, you are just going to have to give her time *Giggles*"
                            show sakura teasing with dissolve
                            saku"Remember, women can be complex creatures. You don't always have to understand. What's most important is to let us process our emotions as needed..."
                            saku"Do not forcibly try and storm through a boundary, instead, let her bring down her walls when she feels comfortable, and she'll love you for it!"
                            show boruto normal with dissolve
                            bo"I s-see..."
                            show sakura at smallshake

                            saku"Then that'll be all for today!"
                            scene black with dissolve
                            saku"Don't worry though, you are slowly getting there!"
                            "Sakura turns away from you and walks down the living room..."
                            show sakura walking_away with dissolve
                            "You couldn't help but stare at her alluring hips being swayed from one side to another with every tender step she made..."
                            call increaselust(10) from _call_increaselust_213
                            bot"What about your walls, Auntie! Will you ever bring them down?"
                            hide sakura walking_away with dissolve
                            jump sakura_repeatable_ending_good
                        saku "My oh my! Reaching somewhere you should't? Or maybe..."
                        menu sakura_move3:
                            saku "My oh my! Reaching somewhere you should't? Or maybe..."
                            "{color=[obediencecolor]}Test her limits!{/color}":
                                show sakura_hug_behind 2tits_1t with dissolve
                                "Your fingers glide up her shirt, tracing her curves..."
                                bo "You're too tempting, Auntie..."
                                call changesakura(1) from _call_changesakura_20
                                saku "Mmm—cheeky!" with vpunch
                                bot"I can feel her b-bra! And she doesn't even seem to m-mind!?"
                                bot"Then m-maybe..."
                                show sakura_hug_behind 2titst with dissolve
                                "Your other hand ventures lower, slipping beneath her pants..."
                                bo "What about t-this, Auntie..."
                                saku "*Gasps!* O-oh, you're in trouble now!" with vpunch
                                show sakura_hug_behind 2tits_1t with dissolve
                                call changesakura(1) from _call_changesakura_21
                                "She gasps, her body tensing before she stops you from going any lower on her..."
                                "She leaves your other hand to freely explore her upper body."
                                saku "Too much, too fast [bo_name_stutter]! Lesson's over, for now..."
                                scene black with dissolve

                           
                        "Sakura put a stop to your advances..."
                        show bg lr uchiha
                        show boruto surprised2 at left
                        show sakura shy at right
                        with dissolve
                        saku"Phew, things are getting heated up! But this is just a lesson, r-remember?"

                        "Her shaky voice, along with her flushed cheeks betrayed her composure..."
                        show sakura normal with dissolve
                        saku "You're learning fast, maybe too fast. It's best we cool off for now..."
                        scene black with dissolve
                        "Sakura turns away from you and walks down the living room..."
                        show sakura walking_away with dissolve
                        "You couldn't help but stare at her alluring hips being swayed from one side to another with every tender step she made..."
                        call increaselust(10) from _call_increaselust_214
                        saku"You are one good pupil, [bo_name]! But let's both remember that this isn't anything more than a little lesson, okay?"
                        bo"R-right..."
                        bot"You say that, but... With the way you act around me, I wonder if you really mean that, Auntie!"
                        hide sakura walking_away with dissolve
                        jump sakura_repeatable_ending_good
                        
                            
                    "{color=[lovecolor]}Lean in for a kiss...{/color}":
                        bot"The way she speaks, the way she acts..."
                        show sakura_hug:
                            easein 5 zoom 1.4 yalign 0.45 xalign 0.5
                        label leaninforakiss:
                        "Your heart pounds as you lean in..."

                        bot"Is t-this what she wants from me?"
                        "Your lips hover near hers, close enough to feel her breath hitch..."
                        scene black with dissolve
                        saku "[bo_name]...?"
                        scene bg lr uchiha:
                            blur 40
                        show sakura_kiss 1
                        with dissolve
                        "She doesn't pull away, instead, she pulls strands of her hair behind her ear, exposing her full face to you, her eyes wide but curious, waiting to see if you'll commit..."
                        call checkSakura(20) from _call_checkSakura_4 
                        if sakura_relationship >= 20:
                            show sakura_kiss:
                                easein 1 zoom 1.2 xalign 0.0 yalign 1.0
                            "You nudge your head forward..." with vpunch
                            scene black with dissolve
                            show sakura_kiss 2_1 with Dissolve(1):
                                xalign 0.0 yalign 0.45
                            $ renpy.sound.play("/audio/soun_fx/kiss1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                            "And you feel her once restrictive hand on your chin, now guiding you towards her lips..."
                            "Your lips touched, but only for a moment..."
                            scene bg lr uchiha:
                                blur 40
                            show sakura_kiss 1
                            with dissolve
                            call increaselust(10) from _call_increaselust_215
                            "Sakura held you back with her hand, making sure to give you only but a brief, small taste of hers..."
                            default sakura_firstkiss = False
                            if sakura_firstkiss == False:
                                saku"...Your first kiss?"
                            else:
                                saku"We shouldn't let ourselves indulge each other too much..."
                            menu sakura_kiss_menu:
                                saku"..."

                                "{color=[obediencecolor]}I see no problem with that...{/color}" if sakura_firstkiss == True:
                                    call checkSakura(30) from _call_checkSakura_5 
                                    if sakura_relationship >= 30:
                                        pass
                                    else:
                                        bo"I could use the extra p-practice..."
                                        show sakura_kiss at smallshake
                                        saku"Not so s-soon... *Giggles*!"
                                        saku"We can't just jump right in to it again, and there's, uhm, other things to consider first..."
                                        sakut"Sarada..."
                                        saku"You've got to play the 'game' first, remember? Look for another sign, then you'll know it's time..."
                                        scene black with vpunch
                                        saku"But that wasn't bad, [bo_name]! I am impressed..."
                                        show bg lr uchiha with dissolve
                                        show sakura teasing at center:
                                            zoom 1.0
                                        show boruto surprised3 at left
                                        with dissolve
                                        show sakura:
                                            easein 3 xalign 1.0
                                        call changesakura(1) from _call_changesakura_22
                                        saku "Not bad for a beginner. A little bold, but... effective."
                                        
                                        bo "R-right..."
                                        saku"That'll be all for today! But you should come by again some time soon. You still have a lot to learn after all... *Giggles*"
                                        jump sakura_repeatable_ending_good

                                    bo"I see no problem with that. It's only training after all..."
                                    saku"Hmm..."
                                    saku"I suppose so, but let's not overdo it, okay?" with vpunch
                                    scene black with dissolve
                                    show sakura_kiss 2_1 with Dissolve(1):
                                        xalign 0.0 yalign 0.45
                                    $ renpy.sound.play("/audio/soun_fx/kiss1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                                    "Once again, Sakura drops her guard and indulges your wish..."
                                    scene bg lr uchiha:
                                        blur 40
                                    show sakura_kiss 2
                                    with fade
                                    $ renpy.sound.play("/audio/soun_fx/kiss2.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                                    saku"Just... t-training..."
                                    bo"That's right... A-auntie!" with vpunch
                                    "In between the wet suckling noises of your kiss, you re-assured each other in short breaths, that this was just a simple act of 'training'..."
                                    scene black with dissolve
                                    show sakura_kiss 2_1 with Dissolve(1):
                                        xalign 0.0 yalign 0.45
                                    $ renpy.sound.play("/audio/soun_fx/kiss1.opus", channel="sfx3", loop=False, relative_volume = 1.0)
                                    "*Wet kissing sounds*..."
                                    sakut"Am I going t-too far?"
                                    hide sakura_kiss with dissolve
                                    show sakura_kiss_2_2 with dissolve:
                                        zoom 1.2 xalign 1.0 yalign 0.0
                                    "Sakura realized the kiss was dragging on for a while, and quickly put a stop to it."
                                    "Her slightly messy hair, the wetness of her lips, it was evident she found enjoyment in it herself..."
                                    scene black with dissolve
                                    "She quickly gathered her self, fixed her hair behind her ear, and broke the awkward silence..."
                                    scene bg lr uchiha:
                                        blur 40
                                    show sakura_kiss 1
                                    with dissolve
                                    saku"T-there you have it, a proper kissing lesson!"
                                    scene black with vpunch
                                    "She pushed you back, breaking the heat of the intimate moment in a playful manner..."
                                    saku"Not bad at all, [bo_name]! I am impressed..."
                                    show bg lr uchiha with dissolve
                                    show sakura teasing at center:
                                        zoom 1.0
                                    show boruto snob at left
                                    with dissolve
                                    show sakura:
                                        easein 3 xalign 1.0
                                    call changesakura(3) from _call_changesakura_23
                                    saku "You keep this up and I might just fall for you! Teeheehe!" with vpunch
                                    show sakura shy with dissolve 
                                    saku"On a more serious note, remember why we are doing this..."
                                    saku"While you are dealing with your problems, your Auntie here is simply helping you along the way, nothing more, okay?"
                                    bo "R-right..."
                                    bot"We'll see where that'll take us, Auntie!"
                                    show sakura normal with dissolve
                                    saku"Then that'll be all for today! But you should come by again some time soon. You still have a lot to learn after all... *Giggles*"
                                    scene black with dissolve
                                    "Sakura turns away from you and walks down the living room..."
                                    show sakura walking_away with dissolve
                                    "You couldn't help but stare at her alluring hips being swayed from one side to another with every tender step she made..."
                                    call increaselust(10) from _call_increaselust_216
                                    bot"Don't know how much longer I can take Auntie's teasing..."
                                    hide sakura walking_away with dissolve
                                    jump sakura_repeatable_ending_good
                                    


                                "W-what! Of course not..." if sakura_firstkiss == False:
                                    bo"W-what! N-no, of course not..."
                                    saku"Oh [bo_name]... One thing you should know about girls, is that they are much better at reading emotions than men are..."
                                    saku"In any case, since you've had plenty of kisses before, this will have to suffice! *Giggles*"
                                    scene black with vpunch
                                    "She pushed you back, breaking the heat of the intimate moment in a playful manner..."
                                    saku"But that wasn't bad, [bo_name]! I am impressed..."
                                    show bg lr uchiha with dissolve
                                    show sakura teasing at center:
                                        zoom 1.0
                                    show boruto surprised3 at left
                                    with dissolve
                                    show sakura:
                                        easein 3 xalign 1.0
                                    saku"But that wasn't bad, [bo_name]! I am impressed..."
                                    call changesakura(1) from _call_changesakura_24
                                    saku "Not bad for a beginner. A little bold, but... effective."
                                    
                                    bo "R-right..."
                                    saku"That'll be all for today! But you should come by again some time soon. You still have a lot to learn after all... *Giggles*"
                                    scene black with dissolve
                                    "Sakura turns away from you and walks down the living room..."
                                    show sakura walking_away with dissolve
                                    "You couldn't help but stare at her alluring hips being swayed from one side to another with every tender step she made..."
                                    call increaselust(10) from _call_increaselust_217
                                    bot"Don't know how much longer I can take Auntie's teasing..."
                                    hide sakura walking_away with dissolve
                                    $ sakura_firstkiss = True
                                    jump sakura_repeatable_ending_good
                                "Y-yeah..." if sakura_firstkiss == False:
                                    bo"Y-yeah..."
                                    saku"Then we better make it count!"
                                    scene bg lr uchiha:
                                        blur 40
                                    show sakura_kiss 2
                                    with fade
                                    bo"Aunt-" with vpunch
                                    $ renpy.sound.play("/audio/soun_fx/kiss1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                                    "She takes the lead, this time making sure you get a proper taste of her..."
                                    scene black with dissolve
                                    show sakura_kiss 2_1 with Dissolve(1):
                                        xalign 0.0 yalign 0.45
                                        
                                    "You felt her tongue exploring yours, and in turn, you made sure to follow her lead, and let her taste you..."
                                    scene bg lr uchiha:
                                        blur 40
                                    show sakura_kiss 2
                                    with fade
                                    $ renpy.sound.play("/audio/soun_fx/kiss2.opus", channel="sfx3", loop=False, relative_volume = 1.0)
                                    "The kiss kept going for a few seconds, seconds that felt like an eternity as the taste of her grew sweeter and sweeter with each exchange of fluids between you..."
                                    scene black with dissolve
                                    show sakura_kiss 2_1 with Dissolve(1):
                                        xalign 0.0 yalign 0.45
                                    "*Wet kissing sounds*..."
                                    hide sakura_kiss with dissolve
                                    show sakura_kiss_2_2 with dissolve:
                                        zoom 1.2 xalign 1.0 yalign 0.0
                                    "When Sakura decided to end the kiss, you couldn't help but notice how she looked slightly different..."
                                    "Her slightly messy hair, the wetness of her lips, was this just a lesson, or did she find some enjoyment in your moment of intimacy..."
                                    scene black with dissolve
                                    "She quickly gathered her self, fixed her hair behind her ear, and broke the awkward silence..."
                                    scene bg lr uchiha:
                                        blur 40
                                    show sakura_kiss 1
                                    with dissolve
                                    saku"T-there you have it, a proper first kiss..."
                                    scene black with vpunch
                                    "She pushed you back, breaking the heat of the intimate moment in a playful manner..."
                                    saku"Not bad at all, [bo_name]! I am impressed..."
                                    show bg lr uchiha with dissolve
                                    show sakura teasing at center:
                                        zoom 1.0
                                    show boruto surprised3 at left
                                    with dissolve
                                    show sakura:
                                        easein 3 xalign 1.0
                                    call changesakura(3) from _call_changesakura_25
                                    saku "You keep this up and I might just fall for you! Teeheehe!" with vpunch
                                    show sakura serious with dissolve 
                                    saku"On a more serious note though, don't let yourself catch feelings now, okay?"
                                    saku"While you are dealing with your problems, your Auntie here is simply helping you along the way, nothing more, okay?"
                                    bo "R-right..."
                                    saku"Then that'll be all for today! But you should come by again some time soon. You still have a lot to learn after all... *Giggles*"
                                    scene black with dissolve
                                    "Sakura turns away from you and walks down the living room..."
                                    show sakura walking_away with dissolve
                                    "You couldn't help but stare at her alluring hips being swayed from one side to another with every tender step she made..."
                                    call increaselust(10) from _call_increaselust_218
                                    bot"Don't know how much longer I can take Auntie's teasing..."
                                    hide sakura walking_away with dissolve
                                    $ sakura_firstkiss = True
                                    jump sakura_repeatable_ending_good
                                "{color=[dominancecolor]}The first of many!{/color}" if sakura_firstkiss == False:
                                    call checkDominance(20,"sakura_kiss_menu") from _call_checkDominance_28
                                    bo"The first of many!"
                                    scene bg lr uchiha:
                                        blur 40
                                    show sakura_kiss 2
                                    with fade
                                    $ renpy.sound.play("/audio/soun_fx/kiss2.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                                    saku"Oh my-" with vpunch
                                    call changeDominance(1) from _call_changeDominance_91
                                    "You catch her by surprise by leaning in for another kiss, but this time you make sure a proper exchange of fluids takes place..."
                                    scene black with dissolve
                                    show sakura_kiss 2_1 with Dissolve(1):
                                        xalign 0.0 yalign 0.45
                                    $ renpy.sound.play("/audio/soun_fx/kiss2.opus", channel="sfx3", loop=False, relative_volume = 1.0)
                                    "The kiss kept going for a few seconds, seconds that felt like an eternity as the taste of her grew sweeter and sweeter with each exchange of fluids between you..."
                                    "*Wet kissing sounds*..."
                                    hide sakura_kiss with dissolve
                                    show sakura_kiss_2_2 with dissolve:
                                        zoom 1.2 xalign 1.0 yalign 0.0
                                    "When Sakura decided to end the kiss, you couldn't help but notice how she looked slightly different..."
                                    "Her slightly messy hair, the wetness of her lips, was this just a lesson, or did she find some enjoyment in your moment of intimacy..."
                                    scene black with dissolve
                                    "She quickly gathered her self, fixed her hair behind her ear, and broke the awkward silence..."
                                    scene bg lr uchiha:
                                        blur 40
                                    show sakura_kiss 1
                                    with dissolve
                                    saku"That was... v-very forward. You should be careful with that!"
                                    call changesakura(1) from _call_changesakura_26
                                    saku"Not all girls are as receptive as your Auntie when it comes to that... *Giggles*" with vpunch
                                    scene black with vpunch
                                    "She pushed you back, breaking the heat of the intimate moment in a playful manner..."
                                    saku"Not bad at all, [bo_name]! I am impressed..."
                                    show bg lr uchiha with dissolve
                                    show sakura teasing at center:
                                        zoom 1.0
                                    show boruto surprised3 at left
                                    with dissolve
                                    show sakura:
                                        easein 3 xalign 1.0
                                    call changesakura(3) from _call_changesakura_27
                                    saku "You keep this up and I might just fall for you! Teeheehe!" with vpunch
                                    show sakura serious with dissolve 
                                    saku"On a more serious note though, don't let yourself catch feelings now, okay?"
                                    saku"While you are dealing with your problems, your Auntie here is simply helping you along the way. Nothing more than that, you understand right?"
                                    bo "R-right..."
                                    saku"Then that'll be all for today! But you should come by again some time soon. You still have a lot to learn after all... *Giggles*"
                                    scene black with dissolve
                                    "Sakura turns away from you and walks down the living room..."
                                    show sakura walking_away with dissolve
                                    "You couldn't help but stare at her alluring hips being swayed from one side to another with every tender step she made..."
                                    call increaselust(10) from _call_increaselust_219
                                    bot"Don't know how much longer I can take Auntie's teasing..."
                                    bot"She even knows about my condition, is she trying to-"
                                    hide sakura walking_away with dissolve
                                    $ sakura_firstkiss = True
                                    jump sakura_repeatable_ending_good
                                        

                        "But before you could reach for her lips, she raised her hand and pressed it against your mouth..."
                        show sakura_kiss at smallshake
                        saku"Not so soon... *Giggles*!"
                        saku"Remember? You've got to play the 'game' first, and once a girl gives you a sign, then you'll know it's time..."
                        scene black with vpunch
                        saku"But that wasn't bad, [bo_name]! I am impressed..."
                        show bg lr uchiha with dissolve
                        show sakura teasing at center:
                            zoom 1.0
                        show boruto surprised3 at left
                        with dissolve
                        show sakura:
                            easein 3 xalign 1.0
                        call changesakura(1) from _call_changesakura_28
                        saku "Not bad for a beginner. A little bold, but... effective."
                        
                        bo "R-right..."
                        saku"That'll be all for today! But you should come by again some time soon. You still have a lot to learn after all... *Giggles*"
                        jump sakura_repeatable_ending_good
                    


    scene black with dissolve

    label sakura_lesson2:
        $ initialize_replay_defaults()
        bo"Thinking about what, Auntie..."
        saku"I think you might be ready for my final lesson!"
        bo"O-oh really?"
        scene black with dissolve
        "Sakura gets off the couch and starts walking towards you, her movements slow but deliberate. A devious grin takes shape on her face as she is approaching..."
        scene bg lr uchiha:
            blur 10
        show sakura_walking 1:
            zoom 0.7 xalign 0.5
        with dissolve

        saku"You've shown some real promise, young man..."
        show sakura_walking 1 with dissolve:
            zoom 0.85 xalign 0.5
        "Her grin widens as she closes the distance..."
        show sakura_walking 1 with dissolve:
            zoom 1 xalign 0.5
        bo"A-auntie...?"
        saku"But..."
        show sakura_walking 2 with dissolve:
            zoom 1.05 xalign 0.5
        saku"It's time to find out if you can handle one final teaching of mine!" with vpunch
        scene black with vpunch
        "With a calculated, careful push, she sends you tumbling backwards onto the couch, landing flat on your back."
        scene sakura_lr 2_1 with dissolve
        "She follows, settling herself gracefully onto your lap, her head resting there as her body presses close..."
        show sakura_lr 2_1_2 with dissolve
        saku"[bo_name]... What do you think the key to a woman's heart is?"
        bo"N-no idea..."
        saku "Well, as lovely as gentle kisses and romantic gestures are, even the heat of passion..."
        saku "Nothing compares to building a true partnership, one that holds strong through every part of life."


        saku"You know, when I was younger, I dreamt of mastering medical Ninjutsu."
        saku"Back then, everyone kept calling me useless, can you even believe that!? But you know who never did?"
        bo"Uncle Sasuke...?"
        saku"Mhm... He used to come back from dangerous missions, battered and bleeding from head to toe..."
        scene sakura_lr 2_1 with dissolve
        saku"He'd rest his head on my lap, just like I lay now on yours, and he'd give me all the time in the world to try and tend to his wounds to the best of my abilities..."
        saku"Even as I trembled, fearing that my care wouldn't suffice, he laid there in silence while he was the one hurt, enduring all the pain of his injuries for my sake, just so I could try one more time..."
        scene sakura_lr 2_1_2 with dissolve:
            zoom 1.2 yalign 1.0 xalign 0.1
        saku"He'd look up into my eyes and say the most calming, soothing words I've ever heard in my entire life, like nothing could ever break him, or me..."
        saku "That's the kind of man we need, [bo_name]. One who shines bright on his own but lifts her light too, without dimming it."
        saku "Someone who chases his dreams but can also carry hers, as if they were his own. Strong, dependable, caring..."
        saku"...Are you following?"
        scene sakura_lr 2_1_2 with dissolve
        bo"Y-yeah..."
        saku "Feel her ambitions as if they were yours! That's what'll make a woman melt for you."
        saku"I am sure you know what Sarada's greatest ambition is, don't you?"
        bo"I think so..."
        saku"If she's going to become Hokage, she is going to need someone to stand by her side, to support that dream of hers."
        saku"As much as I'd like to see the two of you hit it off, It's not my place to meddle, at least not too much! *Giggles*"
        saku"Whether you want to be that someone for her, is your choice to make."
        saku"But [bo_name]..."
        saku"I've seen you being a great friend to Sarada for many years. You were even the first person she entrusted with her ambitions of being Hokage..."
        saku"You've spent so much time together, helped her train all these years, until one day..."
        saku"Life, I imagine, got in the way. You've lost touch with one another, and you haven't sought her out for two years now..."
        saku"I am not saying this to criticize you here, but surely you are able to see why she's so prickly with you now..."
        show sakura_lr 2_5 with dissolve:
            zoom 1.2 yalign 1.0 xalign 0.1
        call increaselust(10) from _call_increaselust_220
        "Sakura's voice softens, her words lingering as she shifts slightly on your lap and placing her hand close to your pelvis, her warmth seeping into you."
        scene sakura_lr 2_5
        show sakura_borutoface 1
        with dissolve
        bot"S-shit, my-" with vpunch
        saku "She misses you, you know. Beneath all that attitude, she's hurt you drifted away."
        bo "I... I didn't realize."
        call increaselust(10) from _call_increaselust_221
        bot"Her h-hand, it's so close! Does she not realize?"
        call checkLust(80) from _call_checkLust_15
        if percentage >= 80:
            scene sakura_lr 2_5 with dissolve:
                zoom 1.2 yalign 1.0 xalign 0.1
            bot"F-fuck it's growing l-larger, I am losing control!"
            saku"Now you know, the secret to a woman's heart!"
            bo"Uh, Y-yeah. T-thanks, Auntie..."
            saku"There is one last thing of course, but now is not the time to discuss it..."
            "Her eyes dart down towards your erection. Sakura seemed unfazed, perhaps intrigued, but you had no way of knowing..."
            sakut"My oh my! I wager his condition is to blame for this, unless he thinks of me... like that?"
            sakut"In any case, not too unnatural for a boy his age. I should definitely not bring it up though..."
            scene sakura_lr 2_5
            show sakura_borutoface 1
            with dissolve
            bot"She m-must be feeling it, her f-face is so close..."
            saku "*yawn* Oh, I'm getting so sleepy... all this talking's worn me out real good."
            scene sakura_lr 2_2
            show sakura_borutoface 1
            with dissolve
            "She nestles deeper into your lap, her head turned away and her eyes closing as if drifting off..."
            call increaselust(10) from _call_increaselust_222
            "A few minutes go by..."
            bot"F-fuck, her head's so close to me, I can even feel her warm breath on my cock even..."
            bot"This is not getting any better, what the hell do I even do!"
            bo"Uh... A-auntie?"
            "."
            scene sakura_lr 2_5_2
            show sakura_borutoface 1
            with dissolve
            ".."
            scene sakura_lr 2_2
            show sakura_borutoface 1
            with dissolve
            "..."
            "No response. Sakura's breathing remained steady, too steady..."
            show sakura_lr 2_5 with dissolve
            bo"A-auntie...!?" with vpunch
            bot"S-shit. I am dead, aren't I?"
            sakut"Maybe a l-little test, just to see how he reacts..."
            show sakura_lr 2_5_2 with dissolve
            saku"*Yawn*... *Exhales*... Mhmmm... *Sleeping Sounds*..."
            "Sakura was wide awake, pretending to be asleep, and you had no way of knowing..."
            bot"M-maybe I am saved, she seems to be knocked out good..."
            bo"A-auntie... you there?"
            saku"..."
            show sakura_lr 2_2 with dissolve
            sakut"What are you thinking... [bo_name]?"
            menu sakura_ending_menu_final:
                sakut"What are you thinking... [bo_name]?"
                "{color=[obediencecolor]}Take care of your needs!{/color}": #(supporter_scene = True)
                    jump sakura_takecareofyourneeds
                    $ call_label_action("sakura_takecareofyourneeds")
                    call supp_rew from _call_supp_rew_3
                    jump sakura_ending_menu_final
                "Make a run for it...":
                    bot"Maybe I can make a run for it! If I am fast enough..."
                    scene black with vpunch
                    bot"Then she'll never know!" with vpunch
                    saku"[bo_name_stutter]!? What's wrong?"
                    bo"S-sorry Auntie, I've got to be somewhere!" with vpunch
                    "..."
                    scene bg lr uchiha:
                        blur 10
                    show sakura_walking 1:
                        zoom 0.7 xalign 0.5
                    with dissolve
                    sakut"*Giggles*..."
                    sakut"Good boy that one. Sarada will be lucky to have him to herself..."
                    scene black with dissolve
                    $ renpy.end_replay()
                    jump action_taken
                
                


        else:
            pass
        saku"Now you do!"
        saku "*yawn* Oh, I'm getting sleepy... all this mentoring has me worn out..."
        saku"You wouldn't mind your Auntie taking a quick nap on your lap, would you?"
        menu:
            saku"You wouldn't mind your Auntie taking a quick nap on your lap, would you?"
            "Of course not...":
                show sakura_lr 2_3 with dissolve
                bo"Of course not..."
                call changesakura(3) from _call_changesakura_29
                saku"Aww, so sweet! Bring me back to the days I used to nanny you to sleep and stroke your hair just like this..."
                scene black with dissolve
                saku"Only now, the roles are reversed... *Yawn*"
                "She nestles deeper into your lap..."
                $ renpy.end_replay()
                jump action_taken
            "I have to go...":
                bo"Sorry Auntie, I have to get going..."
                show sakura_lr 2_1_2 with dissolve
                saku"Shame... But I understand!"
                scene black with dissolve
                saku"I hope to see you again some time soon!"
                $ renpy.end_replay()
                jump action_taken
            




















    label sakura_repeatable_ending_good:
    show sakura_lr 1 with dissolve
    saku"I'll be taking a nap before Sarada gets home, but I hope I'll be seeing you some time soon again!"
    menu:
        saku"I'll be taking a nap before Sarada gets home, but I hope I'll be seeing you some time soon again!"
        "You will!":
            bo"I'll be visiting once in a while! Thanks for offering your help too, Auntie!"
            saku"Of course! Be seeing you..."
        "{color=[hatredcolor]}(Oh you will, you immoral woman...){/color}":
            bo"Oh you will be seeing a lot more of me, auntie!"
            saku"Glad to hear that, Ciao!"
            bot"What a cock-tease you are, Auntie Sakura..."
            call changeHatred(1) from _call_changeHatred_150
            bot"Something's telling me you might just turn into an infidel slut!"
            bot"I don't care about you being betrothed to your husband. I am jumping right in to your panties the first chance I get!"
    scene black with dissolve
    call changesakura(1) from _call_changesakura_30
    "You leave the household after spending some time with Sakura..."
    $ renpy.end_replay()

    jump action_taken