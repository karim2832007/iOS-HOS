label saradasakuraintroduction:
    $ initialize_replay_defaults()
    $ opportunity_sakurasarada_introduction = True
    # show boruto shirtless at center with dissolve
    # bedroom_gymend
    scene black with dissolve
    "Some time earlier..."
    $ change_music_volume(0.3, 1.0)
    show bg day:
        zoom 0.67
    show shina concerned at center
    with dissolve
    hin"Can't he keep his music a bit lower?"
    hin"*Sigh...* This kid is driving me insane..."
    hide shina with dissolve
    $ renpy.sound.play("/audio/soun_fx/dooropen.opus", channel="sfx3", loop=False, relative_volume = 0.6)
    $ change_music_volume(0.8, 1.0)
    hin"I have to let him know his auntie is here..."
    scene bg bb day with dissolve
    show shina surprised with dissolve
    show shina at smallshake
    pause 1
    show pushup_animation with dissolve
    bo"Fifteen!"
    hint"He takes his training seriously lately, doesn't he?"
    bo"Twenty!"
    hint"I wonder what's gotten into him lately..."
    bot"Is that [hin_rel] I just heard...?"
    bo"Two h-hundred!" with vpunch
    scene bg bb day with dissolve
    show shina concerned with dissolve
    hint"...? Looks like he's just about done..."

    scene bedroom_gymend with dissolve
    bot"I think I am starting to put on some real muscle! I wonder if [hin_rel] would notice a difference..."
    show shina shy2:
        xpos 1800
    show shina shy2:
        easein 1 xpos 700
    hin"[bo_name_stutter] Sorry to interrupt, but..."
    bot"Speak of the devil..."
    bo"What's up [hin_rel]?"
    hin"I need you to come downstairs for a moment, and put on a shirt please!"
    bo"Huh? Is this about [him_name]'s complaints? Am I about to get scolded...?"
    show shina angry with dissolve
    hin"You should get scolded! But no, this isn't about that..." with vpunch
    
    hin"Your [him_rel] has the right to request for some peace of mind you know! Your music is way too loud..."
    if not _in_replay:
        if quest_him.is_state("him1H_1", "completed"):
            hin"She was on the verge of tears the other day [bo_name]!"
            show shina concerned with dissolve
            hin"She told me you you two were wrestling and that you almost... h-hurt her!"
            call changeRespect("Hinata",-2) from _call_changeRespect_189
            hin"You can't be doing that with your [him_rel], [bo_name]! Please..."
        elif quest_him.is_state("him1L_1", "completed"):
            hin"She came to me all flustered the other day saying how she asked you nicely to turn the music down..."
            hin"Instead, 'He tickled me to death!' she said! *Sigh...* Can't you two just get along like normal any [him_rel_to_bo] and [him_rel] should?"
        $ lr1opportunitymenu = []
        menu lr1opportunityoncetime:
            set lr1opportunitymenu
            bot"..."
            "{color=[hatredcolor]}She got what she deserved...{/color}" if quest_him.is_state("him1H_1", "completed"):
                bo"That little brat got exactly what she deserved, [hin_rel]..."
                call changeHatred(1) from _call_changeHatred_136
                bo"What am I supposed to do when she barges in here riding her high horse and making demands... obey her every word?"
                show shina at smallshake
                hin"Good lord, [bo_name]..."
                hin"Just... try to be nicer with each other, will you please?"
                bo"Meh..."
            "I am sorry, I might have acted out a little bit...":
                bo"I am sorry, Okay? I might have acted out a little bit..."
                call changeRespect("Hinata", 1) from _call_changeRespect_190
                hin"*Sigh...*[bo_name], I know how [him_name] can be at times, but know that it comes from a place of love, okay?"
                bo"I don't think I've ever seen love look as ugly as hers, heh!"
            "{color=[dominancecolor]}Enough about her! How do I look [hin_rel]?{/color}":
                bo"I get it! Enough about [him_name]..."
                bo"How do you think I look [hin_rel]... Notice any difference?"
                hin"[bo_name_stutter]! D-don't just change the subject like that..." with vpunch
                call checkDominance(15, "lr1opportunityoncetime") from _call_checkDominance_25
                bo"I know, I know, just curious what you think..."
                hin"W-well, I suppose you do look like you've put on some muscle..."
                show shina shy2 with dissolve
                hin"You are starting to look a lot like your [na_rel]!"
                call changeDominance(1) from _call_changeDominance_83
                bo"Not sure if that's a compliment, or a snide remark..."
                show shina angry with dissolve
                hin"It's a c-compliment of course, you doofus!" with vpunch
                call checkObedience(20, "lr1opportunityoncetime", "Hinata") from _call_checkObedience_23
                show shina shy with dissolve
                hin"Your [na_rel] is a great man, you know! It would do you good to look up to him a little bit more..."
                show shina shy2 with dissolve
                hin"You are lucky to have inherited his good looks too!"
                call changeObedience("Hinata",1) from _call_changeObedience_117
                bo"I'd be luckier if I inherited yours instead..."
                hin"E-enough about this..."
    show shina normal with dissolve
    hin"Good grief..."
    hin"Listen, I am not here to scold you, that'll have to wait!"
    hin"Wrap up your exercising and make your way downstairs, alright?"
    hin"There's someone waiting to see you, wouldn't want to keep them waiting, would you?"
    hide shina with dissolve
    hin"And don't forget to put on a shirt!" with vpunch
    scene black with dissolve
    bot"I wonder who that is..."
    scene bg bb day with dissolve
    show boruto shirtless at center with dissolve
    bot"Should I put on a shirt before I go downstairs?"
    menu:
        bot"Should I put on a shirt before I go downstairs?"
        "{color=[dominancecolor]}I am digging this shirtless look...{/color}":
            bot"I am kinda digging this shirtless look..."
            default saradaintro_shirtless = False
            $ saradaintro_shirtless = True
            bot"What's wrong with a shirtless man anyway! It's not like I have massive badonkers like [hin_rel]'s to show off..."
        "I probably should...":
            $ saradaintro_shirtless = False
            bot"I probably should..."
            show boruto snob with fade
    bot"Right! Let's find out who this 'someone' is..."
    hide boruto with dissolve
    scene black with dissolve

    scene bg lr_day with dissolve:
        zoom 0.68
    if saradaintro_shirtless == True:
        show boruto shirtless with dissolve
    else:
        show boruto snob with dissolve
    $ change_music_volume(0.3, 1.0)
    bot"I can hear people conversing outside..."
    show boruto:
        easein 2 xpos 1600
    bot"Is that... auntie's voice?"
    $ renpy.sound.play("/audio/soun_fx/dooropen.opus", channel="sfx3", loop=False, relative_volume = 0.6)
    scene black with dissolve
    "You make your way to the porch..."
    # define sara = Character("Sarada", color="#8B0000", callback=name_callback, cb_name="sarada")
        
    



    #----
    scene bg porch with dissolve
    if saradaintro_shirtless == True:
        show boruto shirtless at left
        show shina smiling:
            xpos 1000
        with dissolve
        "You find [hin_name] conversing with two familiar faces..."
        scene black with dissolve
        show sakuraintro1 with dissolve:
            yalign 1.0
        show sakuraintro1:
            easein 3 yalign 0.0
        bot"Auntie Sakura... It's been a while since I last saw her..."
        show screen parallax1280("sakuraintro1",1,0.5) with dissolve
        call showscrollingimage from _call_showscrollingimage_90
        call increaselust(10) from _call_increaselust_176
        bot"Was she always this...pleasing to the eye?"
        hide screen parallax1280
        show screen parallax1280("sakuraintro1",1,0.0)
        with dissolve
        hide shina
        show screen parallax1280("sakuraintro1_1",1.1,0.0) with dissolve
        saku"There he is! The man of the hour..."
        hide screen parallax1280
        hide screen camera1280
        hide screen camera_ui
        hide scrollingimage onlayer screens
        scene bg porch
        show boruto shirtless at left
        show sakura porch:
            zoom 0.55 xalign 1.3
        with dissolve
        pause 0.2
        hide sakura
        show sakura normal at right
        with dissolve
        saku"My, my, shirtless too in all his glory..."
        show saradaintro1 with dissolve:
            yalign 1.0
        show saradaintro1:
            easein 2 yalign 0.0
        saku"[bo_name] certainly grew  up into a fine young man..."
        saku"Hasn't he... Sarada?" with vpunch
        sara"He has not...!"
        saku"Come on, Sarada! Scooch a little closer! Don't you want to see your friend up close... and personal?"
        show saradaintro1_1 with dissolve:
            yalign 0.0 zoom 1.05 xalign 0.5
        sara "*Cough!* M-mom!" with vpunch
        hide saradaintro1_1 with dissolve
        saku"*Giggles* Oops! My bad, I forgot about the thing you have..."
        sara"I don't have a thing! And [bo_name] needs to put a shirt on!" with vpunch
        hide saradaintro1 with dissolve
        call changeDominance(1) from _call_changeDominance_84
        bo"You two, I am right here you know..."
        show sakura teasing with dissolve
        saku"Indeed you are, looking mighty fine too, [bo_name]!"
        bo"Thanks, Auntie Saku-"
        show shina angry:
            xpos 1500
        show shina:
            easein 1 xpos 0
        show boruto:
            easeout 1.5 xpos -1000
        hin"You idiot! I told you to put on a shirt, didn't I?" with vpunch
        show shina serious with dissolve
        hin"You got poor Sarada all flustered..."
        sara"I am not f-flustered, Aunt [hin_name]!" with vpunch
        bo"Fine, sheesh!"
        show shina concerned with dissolve
        hin"Heh-eh... Sorry about that!"
        show shina shy with dissolve
        hin"[bo_name] may act strangely at times, given the thing we talked about..."
        saku"I sure didn't mind... unlike someone else!" with vpunch
        sara"Enough mom! Please..."
        show blackscreen with dissolve
        hide shina
        $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx3", loop=False, relative_volume = 0.7) 
        "You put on a shirt and rejoin the conversation..."
        show sakura greet
        show boruto snob at left
        hide blackscreen
        with dissolve



    else:
        show boruto surprised2 at left
    saku"There he is! We were just talking about you..."
    bo"Nice to see you again, Aunt Sakura!"
    show sakuraintro1_2 with dissolve:
        yalign 1.0
    show sakuraintro1_2:
        easein 5 yalign 0.0
    saku "Well, look who's all grown up! Nice to see you too, [bo_name]!"
    saku "Growing up to be such a handsome young man, despite having [na_name] as your father! *Giggles*"
    saku "I was worried you'd inherit his...bad looks and stupidity! Thank goodness you took after your mother instead!"
    bo"Right?"
    hin"H-hey you two! [na_name] isn't..." with vpunch
    saku"Oh you! You know I am joking! Mostly... *Giggles* I suppose even that knucklehead managed to clean up decently over the years!"
    show screen parallax1280("sakuraintro1_2",1,0.0) with dissolve
    call showscrollingimage from _call_showscrollingimage_91
    bot "Aunt Sakura... Though we don't share blood, that word 'aunt' has always felt natural for her. She and her husband might as well be [na_name]'s siblings, given how their bond runs deeper than mere friendship."
    bot "It's funny how life works sometimes. [hin_rel] and Sakura are like day and night, like two pieces of a puzzle that should never match. And yet..."
    bot"[hin_rel] with her gentle whispers and reserved mannerisms, Sakura blazing through life with infectious laughter and bold gestures. The two of them have been best buds since forever - They are inseparable!"
    bot"Aunt Sakura used to nanny me and [him_name] all the time when we were younger. In fact, I am pretty sure she even has a soft spot for me - The familial kind of course..."
    bot"At least I think so!"
    bot "The memories flood back easily... Her watching over me and [him_name] when we were little, treating us snacks behind [hin_name]'s back, scolding us with a voice that barely contained her laughter..."
    bot"She always had a special smile for me - the kind that made me feel like I was her own."
    bot "Where [hin_rel] would comfort with soft words, Sakura would sweep me into a bear hug that squeezed the sadness right out. They're proof that opposites don't just attract, they complete each other."
    bot "All these years, I've seen her as family, nothing more. She was just... Aunt Sakura. The mischievous auntie who'd sneak me extra dessert when [him_name] wasn't looking! Heh!"
    bot"But now that we see each other again..."
    menu:
        bot"But now that we see each other again..."
        "Something feels different...":
            bot"There's something different about her... I get this tingling feeling whenever she smiles at me the way she does..."
            bot"Was it always like this?"
        "{color=[dominancecolor]}She could be more than just an 'aunt'...{/color}":
            bot "I can't help but notice how her eyes sparkle when she laughs, when we spend time together..."
            bot"Maybe..."
            bot"Maybe she'd somehow be interested in us... getting closer?"
            call changeDominance(1) from _call_changeDominance_85
            bot"I'll have to test these waters carefully..."
        "{color=[hatredcolor]}She is hot as fuck! And in need of a man...{/color}":
            bot"Despite her old age, she's got a sexy body that puts younger women to shame!" with vpunch
            bot"And with her husband always out of town, just like [hin_rel]'s..."
            call changeHatred(1) from _call_changeHatred_137
            bot"Maybe this old hag needs someone to remind her what attention feels like!" with vpunch
    hide screen parallax1280
    hide screen camera1280
    hide screen camera_ui
    hide scrollingimage onlayer screens
    hide sakuraintro1_2
    with dissolve
    saku"There's someone more important than me to say hello to, [bo_name]..."
    show sakura teasing with dissolve
    saku"Hidden in her own little dark corner... I wonder why!" with vpunch
    saku"She's been... DYYYIIING, to see you after all! Isn't that right, Sarada?"
    show saradaintro1_1 with dissolve:
        yalign 0.0
    sara"M-mom! You are embarassing everyone! S-stop it already..." with vpunch
    show saradaintro1 with dissolve:
        yalign 1.0
    show saradaintro1:
        easein 4 yalign 0.0
    bo"How's it been, Sarada..."
    sara"H-hey..."
    bot "Sarada... Just seeing her brings back memories from days old..."
    bot "She's always been the perfect blend of her parents - her father's cool composure mixed with Sakura's fire, though right now that composure seems to be elluding her... I am pretty sure I know why!"
    show screen parallax1280("saradaintro1",1,0.0) with dissolve
    call showscrollingimage from _call_showscrollingimage_92
    bot "We used to be pretty close friends, me and her! We trained together almost daily. We were always pushing each other to be better, stronger..."
    bot "She even has aspirations of becoming the Hokage, eventually taking the village's reigns from [na_name]."
    bot"I am almost certain she used to have a massive crush on me. But I never reciprocated any similar feelings to her..."
    bot "The way she's avoiding direct eye contact, fidgeting with her glasses... Some things never change. She still has those same nervous habits when she is around me..."
    bot "But there's something different about her now. The way she carries herself, the way she dresses..."
    bot"There's hints of a woman with a strong purpose beneath that cold exterior of hers..."
    bot"Seeing her again after all this time... She's grown into herself in ways I didn't expect!"
    menu:
        bot"Seeing her again after all this time... She's grown into herself in ways I didn't expect!"
        "We have a lot of catching up to do":
            bot "Maybe we can rebuild the friendship we once had... Even if things are different now."
            
        "{color=[dominancecolor]}She's still cute when she's flustered!{/color}":
            bot "That blush of hers... I wonder in what other ways I could bring it out!"
            bot"If I am right about her having a crush on me, then..."
            call changeDominance(1) from _call_changeDominance_86
            bot"Perhaps me and her can have some fun together after all!"
            
        "{color=[hatredcolor]}I think I may have found the one!{/color}":
            bot "Sarada..."
            bot"She might actually be the one to help with this condition of mine!"
            bot"She's always been desperate for my attention, hasn't she?"
            call changeHatred(1) from _call_changeHatred_138
            bot"Perhaps she'll turn out to be the perfect little cock-sleeve if I 'reciprocate' those feelings she has for me..."
    
    hide screen parallax1280
    hide screen camera1280
    hide screen camera_ui
    hide saradaintro1
    hide saradaintro1_1
    hide scrollingimage onlayer screens
    hide sarada
    with dissolve
    saku"Come on Sarada, get in here!"
    show saradaending1 with dissolve:
        yalign 1.0
    show saradaending1:
        easein 3 yalign 0.1
    sara"Will you stop pestering me if I do?"
    show screen parallax1280("saradaending1",1,0.0) with dissolve
    call showscrollingimage from _call_showscrollingimage_93
    saku"Oh come on, you are being too harsh!"
    bot"I am liking this new look of hers! The choker is an interesting choice..."
    call hidescrollingimage from _call_hidescrollingimage_85
    hide screen parallax1280
    hide saradaending1
    with dissolve
    show sakura:
        easein 1 xalign 0.5
    
    show sarada shy at right with dissolve

    sara"F-fine..."
    saku"Aww, look at you two! Like two peas in a pod!"
    saku "My, my... [bo_name] certainly grew into quite the man! Right, Sarada?"
    show sarada angry with vpunch
    sara "Mom! Can you not..."
    show sarada:
        easein 1 xpos 1.14
    show sakura:
        easein 1 xpos 0.66
    show boruto :
        easein 1 xpos 0.21
    show shina smiling with dissolve:
        xpos -0.05

    hin "*Giggles* Some things never change, do they?"

    bo "It's been what... two years?"
    show sarada happy with dissolve
    sara "Two years, two months..."
    show sarada flustered with dissolve
    sara "N-not that I was counting or anything!" with vpunch
    show sakura normal with dissolve
    saku "Oh? Someone's been keeping track..."

    show sakura shy with dissolve
    saku "Though I wish we'd visited sooner! [hin_name] was just telling us about... your condition..."
    show shina concerned with dissolve
    hin "Sakura..."
    show boruto normal with dissolve
    bo "It's okay, [hin_rel]. I don't mind them knowing..."

    saku "How are you holding up, dear?"
    menu:
        "I'm managing...":
            bo "Taking it day by day. It's not easy but I am doing my best...."
            show sarada shy with dissolve
            sara "Is it... very difficult?"
            bo "Extremely. But having people who understand helps..."
            menu:
                bo "Extremely. But having people who understand helps..."

                "...":
                    show boruto worried with dissolve
                    bot"If only [hin_rel] could be of more... help."
                    saku"I am sure it does!"

                "{color=[lovecolor]}Hug [hin_name]{/color}" if hinata_love >= 3:
                    call checkLove(3,None,"Hinata") from _call_checkLove_5
                    show boruto normal:
                        easein 1 xalign 0.2
                    bo"If it weren't for [hin_rel]..."
                    show shinapretend1:
                        zoom 0.45 xalign 0.0 yalign 1.0       
                    with dissolve
                    show shina at smallshake
                    bo"I am pretty sure I would lose my mind..."
                    call changeLove("Hinata",1) from _call_changeLove_46
                    hin"[bo_name_stutter]..."
                    hin"I told you haven't I? I'll do my best to help you through this..."
                    menu:
                        hin"I told you haven't I? I'll do my best to help you through this..."
                        "{color=[obediencecolor]}Y-you will...?{/color}":
                            bo"Y-you will...?"
                            show shinapretend1_1 with dissolve:
                                zoom 0.45 xalign 0.0 yalign 1.0
                            bo"T-thanks [hin_rel]..."
                            "You dropped your hand lower behind her back..."
                            call checkObedience(20,"failiammanaging","Hinata") from _call_checkObedience_24
                            hin"Of c-course..."
                            hint"W-what is he..."
                            menu:
                                hint"W-what is he..."
                                "{color=[dominancecolor]}Grab it!{/color}" if dominance >= 20:
                                    show boruto snob with dissolve
                                    bo"What would I do without..."
                                    $ renpy.sound.play("/audio/soun_fx/groperepeat1.opus", channel="sfx3", loop=False, relative_volume = 0.4)
                                    show hinagropemoneyproblems2 with dissolve:
                                        zoom 0.45 xalign 0.0 yalign 1.0
                                    show shina surprised3 with dissolve
                                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp3.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                    call changeDominance(1) from _call_changeDominance_87
                                    bo"Your support, [hin_rel]..." with vpunch
                                    hin"*Gasp!*" with vpunch
                                    show boruto snob with dissolve
                                    bot"And your sweet ass!"
                                    hin"[bo_name_stutter]!"
                                    saku"Everything alright, you two?"
                                    call changeRespect("Hinata",-1) from _call_changeRespect_191
                                    show shinapretend4 with dissolve:
                                        zoom 0.45 xalign 0.0 yalign 1.0
                                    show shina at smallshake
                                    hint"W-what is he doing! What would Sakura and Sarada think if they k-knew!" with vpunch
                                    hide shinapretend4
                                    hide shinapretend1
                                    hide shinapretend1_1
                                    hide hinagropemoneyproblems2
                                    show boruto snob:
                                        easein 0.4 xalign 0.25
                                    with vpunch
                                    hin"Y-yeah! Things just got... a little e-emotional all of a sudden!"
                                    show shina concerned with dissolve
                                    hin"But we are f-fine now, right [bo_name]?"
                                    bo"We sure are..."
                                    show boruto normal with dissolve
                                    default hinata_groped_duringsaradaintro = False
                                    $ hinata_groped_duringsaradaintro = True

                                "You are the best!":
                                    hide shinapretend1_1 with dissolve
                                    bo"You are the best! Thanks [hin_rel]!"
                                    call changeRespect("Hinata",1) from _call_changeRespect_192
                                    hin"A-any time..."
                                    hide shinapretend4
                                    hide shinapretend1
                                    hide shinapretend1_1
                                    with dissolve
                                    show boruto normal:
                                        easein 0.5 xalign 0.25
                                    show shina shy with dissolve
                                    hint"Phew... I guess that was an accident!"
                                

                        "Thank you, [hin_rel]...":
                            hide shinapretend1 with dissolve
                            show boruto normal:
                                easein 1 xalign 0.25
                            bo"Thank you, [hin_rel]..."
                            hin"Of course..."
                        "Test (Don't click!)" if hatred>=100000:
                            label failiammanaging:
                            show shinapretend4:
                                zoom 0.45 xalign 0.0 yalign 1.0
                            show shina surprised2
                            with dissolve
                            call changeRespect("Hinata",-2) from _call_changeRespect_193
                            hint"W-what is he doing!"
                            hide shinapretend4
                            hide shinapretend1
                            hide shinapretend1_1
                            show boruto surprised2:
                                easein 0.4 xalign 0.25
                            with vpunch
                            hin"D-don't worry about it..."
                            bot"S-shit! I thought I could pass that off as an accident..."
                            show boruto normal with dissolve
                        
                    
                
                
        
        "{color=[hatredcolor]}I am losing my mind, but at least I have [hin_rel]!{/color}":
            show boruto sceeming with dissolve
            show boruto:
                easein 1 xalign 0.2
            show shinapretend1:
                zoom 0.45 xalign 0.0 yalign 1.0       
            with dissolve
            bo "I am slowly losing my mind, but..."
            show shina at smallshake
            show shinapretend1_1 with dissolve:
                zoom 0.45 xalign 0.0 yalign 1.0
            show shina surprised2 with dissolve
            bo"At least I have [hin_rel] to support me!"
            "You dropped your hand lower behind her back..."
            hin"[bo_name_stutter]?"

            saku"To have someone like [hin_name] in times like this is a blessing..."
            call checkObedience(20,"failiammanaging","Hinata") from _call_checkObedience_25
            saku"Do not forget that [bo_name]. I hope you appreciate your [hin_rel]'s efforts!"
            $ renpy.sound.play("/audio/soun_fx/groperepeat1.opus", channel="sfx3", loop=False, relative_volume = 0.4)
            show hinagropemoneyproblems2 with dissolve:
                zoom 0.45 xalign 0.0 yalign 1.0
            show shina surprised4 with dissolve
            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp3.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            hin"*Gasp!*" with vpunch
            call changeHatred(1) from _call_changeHatred_139
            bo"Oh I certainly appreciate her efforts, auntie!"
            call changeObedience("Hinata",1) from _call_changeObedience_118
            hin"*Gasp!*" with vpunch
            show boruto snob with dissolve
            bot"And her sweet ass!"
            bo"Thank you [hin_rel]! You are the best..."
            hin"[bo_name_stutter]!" with vpunch
            show sakura serious with dissolve
            saku"Everything alright? [hin_name] you seemed concerned... Is something wrong?"
            call changeRespect("Hinata",-1) from _call_changeRespect_194
            show shinapretend4 with dissolve:
                zoom 0.45 xalign 0.0 yalign 1.0
            show shina at smallshake
            show shina concerned with dissolve
            hin"E-everything's fine, it's just..."
            saku"Emotions running high, huh?"
            hint"W-what is he doing! What would Sakura and Sarada think if they saw him!" with vpunch
            hide shinapretend4
            hide shinapretend1
            hide shinapretend1_1
            hide hinagropemoneyproblems2
            show boruto snob:
                easein 0.4 xalign 0.25
            with vpunch
            hin"Y-yeah! Things just got... a little e-emotional!"
            show shina concerned with dissolve
            hin"But we are f-fine now, right [bo_name]?"
            bo"We sure are!"
            show boruto normal with dissolve
            $ hinata_groped_duringsaradaintro = True
            show sakura normal with dissolve
            saku "Same old [bo_name]... Always putting on a brave face."

    show sakura serious with dissolve
    show shina shy with dissolve
    saku "You know what? We should start having our weekend gatherings again!"
    show sakura teasing with dissolve
    saku "Remember how you two used to spend hours training together?"
    show sarada angry2 with dissolve
    sara "Mom...!"
    show shina smiling with dissolve
    hin "That's a wonderful idea! [bo_name] could use the company..."

    menu:
        hin "That's a wonderful idea! [bo_name] could use the company..."
        "That could be nice...":
            bo "Yeah, I'd like that. If Sarada's up for it?"
            show sarada shy with dissolve
            sara "I... I'll think about it..."
            call changeRespect("Hinata", 1) from _call_changeRespect_195
            hin"It would do both of you good, I reckon!"
            saku"Right?"
            
        "{color=[dominancecolor]}Only if Sarada can keep up{/color}":
            call changeDominance(1) from _call_changeDominance_88
            show boruto snob with dissolve
            bo "Think you can still match my pace, Sarada?"
            show sarada snob with dissolve
            sara "Ha! Don't get cocky, [bo_name]."
            show sakura teasing with dissolve
            saku "Oh my... Is that a challenge I hear?"

    show sakura normal with dissolve
    saku "Well, we should get going. But we'll be seeing more of each other, I hope!"
    show sarada shy with dissolve
    sara "M-maybe so... Take care, [bo_name]."

    bo"See you around, Sarada! You too auntie!"
    show sakuraending1 with dissolve:
        yalign 1.0
    show sakuraending1:
        easein 5 yalign 0.0
    saku"I would hope so, [bo_name]! Sarada's face is already brimming with anticipation! Isn't that right, Sarada?"
    sara"Damn it m-mom! Enough!" with vpunch
    hide sakuraending1 with dissolve
    hide sakura
    hide sarada
    with dissolve
    saku"*Giggles* O-ouch! Don't just punch your mom like that..." with vpunch
    sara"It wasn't a punch! And you deserved it..." with vpunch

    # Scene exit
    hide sakura
    hide sarada
    with dissolve
    show shina concerned with dissolve
    hin "Those two haven't changed a bit..."
    bo "Yeah..."

    if hinata_groped_duringsaradaintro == True:
        hin"[bo_name_stutter]... Why did you do that?"
        show boruto surprised2 with dissolve
        bo"You mean... the hug?"
        show shina serious with dissolve
        hin"It was more than a hug, [bo_name]!"
        hin"I told you before you cannot be doing that!" with vpunch
        hin"The nerve to even try that when Sakura and Sarada were right there..."
        hin"You cannot be touching your [hin_rel_mother] like that!" with vpunch
        hin"What would they think of you! Of me...?" with vpunch
        show boruto snob with dissolve
        bo"That we are... close?" with vpunch
        hide shina with dissolve
        call changeRespect("Hinata", -1) from _call_changeRespect_196
        hin"Ugh! I can't deal with this right now. Get a grip, [bo_name]!"
    scene black with dissolve
    "The reunion stirred something in your chest... was it nostalgia, or something more?"
    bot"I better take a shower! I am still sweaty from working out..."
    $ notification("Uchiha household unlocked")
    "You can now visit the Uchiha household during weekends..."
    default uchihahousehold_unlocked = False
    $ uchihahousehold_unlocked = True
    $ renpy.end_replay()
    jump action_taken