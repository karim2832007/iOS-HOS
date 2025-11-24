label visituchihas_label:
$ renpy.sound.play("/audio/soun_fx/doorknock.opus", channel="sfx2", loop=False, relative_volume = 0.8)
show boruto normal at left with dissolve
"*Knock Knock*"
"..."
default wine_counter_mentioned = False
if day_part == 1:
    $ renpy.sound.play("/audio/soun_fx/dooropen.opus", channel="sfx3", loop=False, relative_volume = 0.6)
    saku"Ah!" with vpunch
    show sakura greet at right with dissolve
    saku"[bo_name]! I am so glad you showed up!"
    show sakura normal with dissolve
    saku"Sarada isn't home right now, but I could use some company myself if you want to come in!"
    menu:
        saku"Sarada isn't home right now, but I could use some company myself if you want to come in!"
        "I came to see you anyway, Auntie!":
            show boruto normal with dissolve
            bo"I came to spend some time with you anyway, Auntie Sakura!"
            show sakura teasing with dissolve
            call changesakura(2) from _call_changesakura_31
            saku"Aww, what a gentleman! Wanna come inside then?"
            hide skaura with dissolve
            bo"For sure!"
            hide boruto with dissolve
            scene black with dissolve
            jump visitsakura_tutorial
        "I'll come back when Sarada is around...":
            show boruto embarassed with dissolve
            bo"Oh, I'll come back when Sarada is around then..."
            show sakura shy with dissolve
            call changesakura(-2) from _call_changesakura_32
            saku"Aww, bummer! Your Auntie would like to spend some time with you too, you know..."
            bo"Maybe next time!"
            hide boruto with dissolve
            show sakura at smallshake
            saku"..."
            jump action_taken
        

elif day_part == 2 or day_part == 3:
    $ renpy.sound.play("/audio/soun_fx/dooropen.opus", channel="sfx3", loop=False, relative_volume = 0.6)
    saku"Ah!" with vpunch
    show sakura greet at right with dissolve
    if wine_counter >= 1 and wine_counter_mentioned == False:
        $ wine_counter_mentioned = True
        show sakura shy with dissolve
        saku"Eh-eh... About the other night..."
        show boruto surprised at left with dissolve
        bo"Did Sarada f-find out!?" with vpunch
        show sakura normal with dissolve
        saku"Of course not, but still..."
        show boruto snob with dissolve
        saku"I don't have to tell you to keep it between us, right?"
        bo"Of course!"
        show sakura serious with dissolve
        saku"Your best kept secret, [bo_name]! From everyone..."
        bo"Right, right!"
        show sakura normal with dissolve
        saku"In any case... I am glad you showed up again!"
    else:
        saku"[bo_name]! I am so glad you showed up!"
    

    show sakura normal with dissolve
    saku"Are you here to see Sarada?"
    menu:
        saku"Are you here to see Sarada?"
        "I came to see you, Auntie!":
            show boruto normal with dissolve
            bo"I came to spend some time with you instead, Auntie Sakura!"
            show sakura teasing with dissolve
            call changesakura(2) from _call_changesakura_33
            saku"Aww, what a sweetie! But you should make some time for your friend at some point, okay?"
            saku"Wanna come inside then?"
            hide skaura with dissolve
            bo"For sure!"
            hide boruto with dissolve
            scene black with dissolve
            jump visitsakura_tutorial
        "Yeah, can I see her?":
            show boruto embarassed with dissolve
            bo"Yeah, can I see her?"
            show sakura teasing with dissolve
            saku"Of course!"
            if sarada_reintro_complete == True:
                show boruto normal with dissolve
                saku"She was all giddy last time after you left."
                saku"I think our little ploy worked perfectly *Giggles*!" with vpunch
                show boruto surprised2 with dissolve
                bo"It did!?" with vpunch
                saku"Come on, come inside!"
            else:

                saku"Although things may not be so simple..."
                show boruto at smallshake
                bo"H-huh...?"
                saku"You'll find out soon enough, young man..."
            hide boruto with dissolve
            hide sakura with dissolve
            jump visit_sarada

elif day_part == 4:
    if sakura_asked_for_wine == True:
        $ wine_in_inventory = inventory.find_item_by_name("Wine")
        if wine_in_inventory!= None:
            bot"I got the wine Auntie Sakura asked for. Shall I try knocking on the door at this time?"
            menu:
                bot"I got the wine Auntie Sakura asked for. Shall I try knocking on the door at this time?"
                "Knock on the door":
                    jump sakura_wine_date
                "M-maybe later...":
                    show screen topleftbuttons
                    $ ui.interact()

        else:
            bot"Auntie Sakura asked me to bring some wine and visit her during midnight, but I forgot the wine!" with vpunch
            show screen topleftbuttons
            $ ui.interact()


    else:
        pass

    bot"There's nothing to do here at this time... I think?"
    show screen topleftbuttons
    $ ui.interact()


label visit_sarada:
    $ initialize_replay_defaults()
    $ uchihas_visited = True
    default sarada_visited = 0
    $ sarada_visited += 1
    
    show bg lr uchiha with dissolve
    show sakura normal at right with dissolve
    saku"Sarada is probably in her bedroom, but do tread carefully, [bo_name]..."

    if sarada_reintro_complete == True:
        show boruto surprised2 at left with dissolve
        bo "Yeah, I know Auntie... She's always a handful!"
        show bg uchiha_bedroom 
        show sakura normal at right 
        with dissolve
        saku"There, there... but don't go barging in a girl's room, okay?"
        hide sakura with dissolve
        saku"I'll leave you two alone..."
        show boruto suspicious at left with dissolve
        bo"Right..."
        jump sarada_reintro_door

    if sarada_visited >= 2:
        bo"Yeah, that much I already got to learn last time..."
        show bg uchiha_bedroom with dissolve
        show sakura normal at right with dissolve
        show boruto surprised2 at left with dissolve
        saku"There, there... but don't go barging in a girl's room, okay?"
        hide sakura with dissolve
        saku"I'll leave you two alone..."
        bo"Right..."
        hide boruto with dissolve
        show bg with dissolve:
            zoom 1.2 xalign 0.5 yalign 0.2
        $ sarada_visited += 1
        jump sarada_revisit_menu
    else:
        pass
    show boruto normal at left with dissolve
    bo "Is something wrong?"
    show sakura teasing with dissolve
    saku"You are a smart young man, I'll let you figure that one out! *Giggles*"
    show boruto embarassed with dissolve
    bo"R-right..."
    saku"Come on then, off you go!"
    show sakura:
        easein 1 xalign 0.4
    scene black with dissolve
    "Sakura playfully pushes on your shoulders, encouraging you to visit her daughter..."
    show bg uchiha_bedroom with dissolve
    show sakura normal at right with dissolve
    show boruto surprised2 at left with dissolve
    saku"There, there... but don't go barging in a girl's room, okay?"
    hide sakura with dissolve
    saku"I'll leave you two alone..."
    bo"Right..."
    hide boruto with dissolve
    show bg with dissolve:
        zoom 1.2 xalign 0.5 yalign 0.2
    menu sarada_revisit_menu:
        bot"..."

        "Knock on the door" if sarada_visited >= 2:
            $ renpy.sound.play("/audio/soun_fx/doorknock.opus", channel="sfx2", loop=False, relative_volume = 0.6)
            "*Knock knock*"
            bo"H-hey, it's me..."
            "..."
            bo"...Sarada?"
            bot"But... Auntie said she is inside. Is she ignoring me?"
            menu:
                bot"But... Auntie said she is inside. Is she ignoring me?"
                "Take a peek!":
                    show bg with dissolve:
                        zoom 1.4
                    bot"My curiosity demands a peek!"
                    scene black with dissolve
                    sara"Uh... ♡ Ahh...! ♡"
                    show screen peeking1024("sarada_masturbating")
                    show screen peaking_overlay("bgp peak_updown")
                    with Dissolve(1)
                    bot"...!" with vpunch
                    bot"Is she m-masturbating?"
                    show screen peeking1024("sarada_masturbating1") with dissolve
                    $ renpy.sound.play("/audio/soun_fx/eyesharingan1.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                    sara"W-who's there!"
                    scene black with dissolve
                    bot"S-shit! My cue to get the fuck out of here..."
                    $ renpy.end_replay()
                    jump action_taken

        "Knock on the door" if sarada_visited == 1:
            $ renpy.sound.play("/audio/soun_fx/doorknock.opus", channel="sfx2", loop=False, relative_volume = 0.6)
            "*Knock knock*"
            bo"H-hey, it's me..."
            sara"[bo_name_stutter]!?" with vpunch
            bo"Can I come in?"
            sara"Absolutely not! I don't want to see you right now..."
            bo"Uuh, can I ask why?"
            sara"You go and figure it out yourself! I-idiot..." with vpunch
            bot"What the hell is wrong with her..."
            menu:
                bot"What the hell is wrong with her..."
                "Take a peek!":
                    show bg with dissolve:
                        zoom 1.4
                    bot"Maybe I'll find out with a quick peek! Hehe..."
                    scene black with dissolve

                    show screen peeking1024("sarada_peek 1")
                    show screen peaking_overlay("bgp peak_updown")
                    with Dissolve(1)
                    bot"D-damn..."
                    bot"I wasn't particularly attracted to Sarada before this t-thing took hold of me, but..."
                    bot"She's been growing into her panties quite well! Just look at that ass on her..."
                    bot"Maybe I should give her the attention she craved over all those years!"
                    sara"Hashirama Senju -- What an interesting person!"
                    bot"She was always enamored with the idea of being Hokage..."
                    bot"It seems she is reading books regarding the subject to prepare herself..."
                    $ renpy.sound.play("/audio/soun_fx/eyesharingan1.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                    hide screen peeking1024
                    hide screen peaking_overlay
                    show screen peeking1024("sarada_peek 1_1")
                    show screen peaking_overlay("bgp peak_updown")
                    with flash
                    sara"Totally unlike someone I know!" with vpunch
                    hide screen peeking1024
                    hide screen peaking_overlay

                    show bg uchiha_bedroom with dissolve
                    show boruto surprised3 at left with dissolve
                    bot"W-what the hell! Can she s-see things through walls!?" with vpunch
                    show boruto surprised2 with dissolve
                    bot"Better get out of here before I raise any more suspicion!"
                    hide boruto with dissolve
                    scene black with dissolve
                    bot"I guess I'll try my luck with her some other time. Maybe Auntie Sakura could help?"
                    $ renpy.end_replay()
                    jump action_taken


                    

                "Consult Sakura...":
                    bot"Maybe Auntie could help..."
                    scene black with dissolve
                    show bg lr uchiha with dissolve
                    show sakura normal at right with dissolve
                    saku"[bo_name]! How did it go with Sarada?"
                    show boruto worried at left with dissolve
                    bo"I think... she is avoiding me?"
                    show sakura shy with dissolve
                    saku"Aww, you poor thing! I did say it may not be so simple, didn't I?"
                    show sakura teasing with dissolve
                    saku"But worry not! Your Auntie is here to help! *Giggles*"
                    show boruto surprised2 with dissolve
                    bo"You can do that?"
                    saku"Of course! Girls know girls you know, let alone my own daughter!"
                    saku"I am pretty sure I know exactly what's going on, but it's best we discuss it while we are alone..."
                    saku"Wouldn't want to worsen things for Sarada, would you?"
                    bo"I suppose not..."
                    show sakura greet with dissolve
                    saku"In that case you best make your escape for now!"
                    saku"Come by during mornings when Sarada is busy with school and I'll make sure you learn a thing or two, alright?"
                    show boruto snob with dissolve
                    bo"Sounds good! See you then, Auntie!"
                    hide boruto with dissolve
                    saku"Be seeing you!"
                    scene black with dissolve
                    $ renpy.end_replay()
                    jump action_taken

                
        "Barge in!" if sarada_visited == 1:
            bot"Time for a hero's entrance!"
            play sound "audio/soun_fx/dooropen.opus" volume 0.7
            scene black with dissolve
            bo"Sarada, guess who decided to show up!"
            scene sarada_barge 1 with dissolve:
                zoom 1.2 xalign 0.0 yalign 1.0
            show sarada_barge:
                easein 4 zoom 1.0 xalign 0.5 yalign 0.7
            "Sarada being utterly lost in her reading, took a second before realizing your unannounced intrusion..."
            bot"N-nice panties.... They shape well around her bottom!"
            show sarada_barge 1_1 with dissolve:
                zoom 1.1
            sara"[bo_name_stutter]!?" with vpunch
            "Sarada turned to you with a look you knew all too well from days old..."
            "The fiercest look you've ever seen a woman with, you knew what was about to come..."
            bot"Oh s-shit! Bad timing? Maybe I can still s-save face..."
            call changeDominance(1, "sareadabarge") from _call_changeDominance_92
            bo"It's b-been a while, hasn't it? Heh-eh..."
            show sarada_barge 1_1 with dissolve:
                zoom 1.2 xalign 0.0
            sara"Y-you..."
            with Shake((0, 0, 0, 0), 2, dist=10, peak_time=2, smoothness=50)
            scene black with vpunch
            sara"GET THE HELL OUT OF HERE YOU BLASTED HALF-WIT!" with vpunch
            $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx2", loop=False, relative_volume = 0.7)
            "Sarada flinged the book she was reading aiming square at your face!"
            show bg uchiha_bedroom with dissolve
            show boruto surprised3 at left with dissolve
            bot"Good lord! That could have killed me if I didn't react in time..."
            show boruto embarassed with dissolve
            bot"W-who throws a book full power straight at people's faces"
            show sakura angry at right with dissolve
            saku"[bo_name]...? Did you do something stupid even after my warning?"
            show boruto at smallshake
            bo"I don't think Sarada wants to see me after all... Heh-eh!"
            show boruto surprised2 with dissolve
            sara"I can hear you, you low-life half-wit!" with vpunch
            sara"MOOOM! GET HIM THE HELL OUT OF HERE!"
            show sakura serious with dissolve
            show sakura:
                easein 0.7 xalign 0.5
            saku"{size=*0.8}Pst... Quick! To the living room before this gets any worse...{/size}"
            scene black with dissolve
            show bg lr uchiha with dissolve
            show sakura serious at right with dissolve
            call changesarada(-1) from _call_changesarada
            saku"*Sigh* I thought I warned you..."
            show boruto worried at left with dissolve
            bo"S-sorry, I suppose?"
            saku"Why do you think Sarada reacted like that, hm?"
            show boruto embarassed with dissolve
            bo"Maybe uuh, she's gone and lost it?"
            show sakura shy with dissolve
            saku"*Sigh...*"
            show blackscreen with dissolve
            "Meanwhile..."
            sara"Where's that damned book..."
            sara"I can't believe I had to throw my precious 'How to be Hokage Vol. 389'"
            show sarada_barge ending with Dissolve(1):
                yalign 1.0 xalign 0.5
            show sarada_barge:
                easein 5 yalign 0.0
            sara"But that idiot totally deserved it!"
            sara"What makes him think he can barge in on me after two whole years of avoiding me..."
            show sarada_barge with dissolve:
                zoom 0.6 xalign 0.5
            sara"While I was in my underwear too!" with vpunch
            sara"Tsk!" with vpunch
            hide sarada_barge with dissolve
            sara"And now I can't even focus on reading this! Argh!" with vpunch
            show sarada_barge 1_2 with dissolve
            show sarada_barge:
                easein 6 yalign 0.6
            call changesarada(1) from _call_changesarada_1
            sara"At least he is still... t-thinking about me? M-maybe...?"
            sara"Hmph! Not that I care..." with vpunch
            hide sarada_barge 1_2 with dissolve
            "..."
            hide blackscreen with dissolve
            show sakura shy with dissolve
            saku"Ara ara... Young boys truly are clueless, huh?"
            show sakura teasing with dissolve
            bo"H-huh?"
            saku"But worry not! Your Auntie is here to help! *Giggles*"
            show boruto surprised2 with dissolve
            bo"W-what does that mean..."
            saku"I suppose I'll have to open your eyes myself, but it's best we discuss that while we are alone..."
            saku"Wouldn't want to worsen things for Sarada, would you?"
            bo"I suppose not..."
            show sakura greet with dissolve
            saku"In that case you best make your escape for now!"
            saku"Come by during mornings when Sarada is busy with school and I'll make sure you learn a thing or two, alright?"
            show boruto snob with dissolve
            bo"Sounds good! See you then, Auntie!"
            hide boruto with dissolve
            saku"Be seeing you!"
            scene black with dissolve
            $ renpy.end_replay()
            jump action_taken



        
    

label visitsakura_tutorial:
    default visitsakura_1sttime = False
    if uchiha_tutorial == True:
        jump visit_sakura_repeatable
    else:
        
        show bg lr uchiha with dissolve
        show sakura normal at right with dissolve
        saku"It's been a while since you've last been around here..."
        show boruto worried at left with dissolve
        bo "Yeah... life's been keeping me busy."
        saku "Oh, I bet, especially with your recent diagnosis. But you're here now, and—well, take a look around! Your Uncle Sasuke decided to take some... creative liberties with the living room."
        saku "I hope you don't mind the dark, gloomy, no-window vibe. It's like living in a hermit's cave sometimes!"
        saku "I swear, Sarada and I aren't as demented as your mentor! *giggles*"
        show boruto laughing with dissolve
        bo"Heh, I don't mind it. He was always more inclined to the shadows, which begs the question, how did you two ever hit it off..."
        show sakura teasing with dissolve
        saku"Hehe! Opposites attract, right? Your [hin_rel_mother] can attest to that! She's got her own quirky match, right?"
        show sakura normal with dissolve
        saku"Besides, for all his brooding, Sasuke does have a few redeeming qualities..."
        show sakura shy with dissolve
        show sakura at smallshake
        saku"But only a few! I would appreciate if that idiot spent a little more time with his wife..."
        show sakura angry with dissolve
        show sakura at smallshake
        saku"Nowadays he is absent all the damn time! *Grr* Just thinking about him makes my blood boil..."

        saku"If not for me, then at least his daughter! Garh..."
        saku"Imbeciles! He and your [na_rel] both. They have no idea how lucky they are they found me and [hin_name]..."
        saku"'Village's safety' this and that, 'Important covert missions'... All he ever does is doomsay and brood around like some sort of tragic hero..."
        show sakura normal with dissolve
        saku "*sigh* S-sorry, sorry... enough of me ranting about my woes. At least I've got you here to brighten my day now, don't I?"
        show boruto surprised2 with dissolve
        menu:
            saku "*sigh* S-sorry, sorry... enough of me ranting about my woes. At least I've got you here to brighten my day now, don't I?"
            "{color=[dominancecolor]}Sounds like you could use someone else...{/color}":
                show boruto snob with dissolve
                call changeDominance(1) from _call_changeDominance_93
                bo "Sounds like you could use someone else around here, huh? Someone who doesn't vanish into the shadows."
                show sakura teasing with dissolve
                saku "Oh? And who might that be, Boruto? Are you offering to step up?"
                "Her tone's playful, but her eyes flicker with something sharper..."
            "{color=[lovecolor]}I'd love to keep you company...{/color}":
                show boruto normal with dissolve
                bo "I'd love to keep you company, Auntie Sakura. Can't let you deal with all this alone."
                show sakura shy
                call changesakura(2) from _call_changesakura_34
                saku "That's sweet of you, Boruto..."
            "You sure do!":
                bo "You sure do! I'm here now, so no more gloomy days, right?"
                show sakura normal
                saku "Heh, you're a lifesaver, Boruto. I'll hold you to that!"

        show boruto normal with dissolve
        saku"I could certainly do with some company! Especially yours..."
        show sakura normal with dissolve
        saku "Tell you what, I was just about to finish up breakfast prep. Give me a sec to wrap things up, and then I've got an idea I'd like to run by you."
        saku "Actually, why don't you follow me to the kitchen? I'd love to hear more about that... diagnosis of yours, if you're up for sharing."
        bo "Sure thing, Auntie."
        scene black with dissolve
        "You trail after her, keeping the small talk flowing as she moves around the kitchen with ease..."

        show sakurakitchen 1 with dissolve:
            yalign 1.0
        show sakurakitchen:
            easein 4 yalign 0.0
        "You open up about the beast's curse and how it's been gnawing at you, twisting your thoughts into something primal, leaving you restless and... frustrated."
        saku "That must be tough... especially for a young man like you, full of energy with nowhere to put it."
        call increaselust(10) from _call_increaselust_223
        show screen parallax1280("sakurakitchen 1",1,0.0) with dissolve
        call showscrollingimage from _call_showscrollingimage_95
        "Your eyes stray, catching the way Sakura glides across the kitchen, her hips swaying as she bends to grab a pan, her shirt tugging tight against her exposed stomach"
        saku"You know, about that idea of mine I mentioned earlier..."
        saku"I bet me and you, we could help each other with our... frustrations!"
        call increaselust(5) from _call_increaselust_224
        bo"A-auntie...!?" with vpunch
        "Your face heats up fast, and she notices, a mischievous glint in her eye."
        saku "*giggles* Oops, my wording was a little vague, wasn't it? Don't get too flustered!"

        saku "What I mean is... these mornings get so lonely with Sarada at school and Sasuke off playing shadow ninja."
        saku "I'm stuck here, drowning in chores and misery. But if you swung by now and then,helped me out a bit, I'd be happy to help you too."
        bo "H-help me how, Auntie Sakura?" with vpunch
        saku "Oh, I've got a gift in mind for you. Something special."
        bo "A g-gift?"
        saku "Mhm! One that could do wonders for you, and maybe even Sarada too! That is, if you play your cards right...."
        bo "S-Sarada? What's she got to do with this...?"

        saku "Now, now, I'm not spilling all my secrets just yet! First, you've got to help your poor old auntie with some chores. *giggles*"
        saku "So, what do you say? Deal?"
        bo "Chores, huh? What do you need me to do?"
        saku "Well, every morning Sarada tears through here like a tornado on her way to school, and I'm not much better, honestly."
        saku "How about you tidy up the house while I finish breakfast? I'll meet you back in the living room when you're done."

        call hidescrollingimage("Click twice to start the chores.") from _call_hidescrollingimage_86 
        scene black with dissolve
        bo"You got it!"
        saku"And careful when tidying up girl's rooms, don't snoop around!" with vpunch
        show bg lr uchiha with dissolve
        show boruto surprised2 with dissolve

        bo "Wonder what she means by 'imparting a gift'..."
        bo "She can't seriously be thinking... nah, no way."
        "Visiting the Uchiha household in the mornings will let you help Sakura with chores and keep her company during her lonely days."
        "Build your bond with Sakura to uncover what gifts, and secrets she has in store for you!"

        menu sakura_menu1:
            bot"..."
            "Help Sakura with chores...":
                bot"Right, I suppose I'll start with the master bedroom..."
                scene black with dissolve
                jump sakura_chores_label
            "Information":
                show screen sakuramenuinfo
                jump sakura_menu1
            "Leave":
                scene black with dissolve
                bot"I'll come by some other time..."
                jump action_taken
            




label chores_finished_label:
    if uchiha_tutorial == True:
        jump chores_finished_repeatable_label
    else:
        pass
    show bg lr uchiha with dissolve
    show boruto normal at left with dissolve
    bot"She must be in the kitchen..."
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
    call showscrollingimage from _call_showscrollingimage_96
    default sakura_visit = 0
    menu chores_done_menu:
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
                bot"Is she talking about me? Uuh, I better pretend I've heard none of that."
                hide screen parallax1280
                show screen parallax1280("chores_done sakura1",1,0.0)
                with dissolve
                saku"Oh, [bo_name]! My little handyman! *Giggles*"
                saku"Come on, let's go to the living room, spend some time together!"
                bo"Sure thing!"
            elif sakura_visit >= 4:
                saku"Maybe today I could..."
                saku"Hmm, Is this the right thing to do...?"
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
        "???" if sakura_relationship <20:
            "Perhaps if your relationship was improved first..."
            jump chores_done_menu
   
        
     
    call hidescrollingimage from _call_hidescrollingimage_87
    scene black with dissolve
    show bg lr uchiha with dissolve
    show sakura teasing at right with dissolve:
        zoom 1.02
    saku"So... I've been thinking!"
    show boruto surprised2 at left with dissolve
    bo"..."
    saku"From what I understand of your condition and the circumstances around it..."
    show sakura:
        easein 3 xpos 850
    saku"I bet you could use some help managing all that life's throwing at ya, no?"
    "Sakura rubs your shoulder in a reassuring manner..."
    show boruto surprised3 with dissolve
    show boruto at smallshake
    bo"A-auntie!?" with vpunch
    saku"Don't get all flustered! You are not thinking of anything weird, are you?"
    saku"I am betrothed, you know! *Giggles*" with vpunch
    scene black with dissolve
    saku"But, that doesn't mean..." with vpunch
    show bg lr uchiha
    show sakura_hug 1
    with dissolve
    saku"...That we can't help each other out with our woes!"
    saku"In exchange for your occasional company, I am willing to impart upon you something that every man craves!"
    menu sakura_hug_menu1:
        saku"In exchange for your occasional company, I am willing to impart upon you something that every man craves!"
        "Y-yourself?":
            show sakura_hug 1_1 with dissolve
            bo"Y-yourself?"
            show sakura_hug at smallshake
            saku"*Giggles* Oh you silly goose! Don't be joking with your Auntie like that!"
            call changesakura(2) from _call_changesakura_35
            saku"Flattery will get you nowhere!"
        "{color=[dominancecolor]}What if I crave you, auntie...{/color}":
            call checkDominance(15,"sakura_hug_menu1") from _call_checkDominance_29
            show sakura_hug 2 with dissolve
            bo"What if I crave you, auntie? Will you impart even yourself to me?"
            saku"H-hey! *Nervous giggles* You know I am betrothed!"
            saku"Don't be joking around like that with your Auntie! What if others were to hear you say that!"
            call changeDominance(1,"sakurahug") from _call_changeDominance_94
            show sakura_hug at smallshake
            bo"Then I wouldn't mind!"
            show sakura_hug 1_1 with fade
            call changesakura(2) from _call_changesakura_36
            "She gently moved your hand away from her waist..."
            saku"R-right, right! You flatter me but, enough joking around!"
        "(I like where this is going...)":
            show sakura_hug 1_1 with dissolve
            bot"I like where this is going..."
            bo"I am... intrigued."
            saku"I bet you are!"

    scene black with dissolve
    saku"You see... Every man wants to know what lies in a woman's mind..."
    saku"Or rather, what the key to a woman's heart is!"
    show sakura_hug 3 with dissolve
    show sakura_hug:
        easein 1 yalign 0.0
    with vpunch
    "Sakura tightens her grip and pulls you ever so closer to her gentle smile. She looks straight into your eyes and asks..."
    show screen parallax1280("sakura_hug 3",1,0.0) with dissolve
    call showscrollingimage from _call_showscrollingimage_97
    saku"You want to know too, don't you? The key to a woman's heart..."
    bo"*Gulp*..."
    saku"Then you are in luck, your Auntie here will help you figure it out!"
    call hidescrollingimage from _call_hidescrollingimage_88
    saku"But, let's not get ahead of ourselves..."
    show bg lr uchiha
    show boruto surprised3 at left
    show sakura teasing at center
    show sakura:
        easein 3 xalign 0.8
    with fade
    saku"Your Auntie here is getting tired and you know how the old adage goes, right?"
    scene black with dissolve
    "Sakura lays down on one of the living room couches..."
    show sakura_lr 1 with dissolve
    saku"Konoha wasn't built in a day, and as with all great things, learning the ways to a woman's heart will take some time!"
    saku"I'll be taking a nap before Sarada gets home, but I hope I'll be seeing you some time soon again!"
    menu:
        saku"I'll be taking a nap before Sarada gets home, but I hope I'll be seeing you some time soon again!"
        "You will!":
            bo"I'll be visiting once in a while! Thanks for offering your help too, auntie!"
            saku"Of course! Be seeing you..."
        "{color=[hatredcolor]}(Oh you will, you immoral woman...){/color}":
            bo"Oh you will be seeing a lot more of me, auntie!"
            saku"Glad to hear that..."
            bot"What a cock-tease you are, Auntie Sakura..."
            call changeHatred(1) from _call_changeHatred_151
            bot"Something's telling me you might just turn into an infidel slut!"
            show sakura_lr with dissolve:
                zoom 1.2 xalign 0.0 yalign 0.2
            show sakura_lr:
                easein 3 xalign 0.75 yalign 1.0
            bot"I don't care about you being betrothed to your husband. I am jumping right in to your panties the first chance I get!"
            scene black with dissolve
            saku"Ciao!"
    scene black with dissolve
    call changesakura(1) from _call_changesakura_37
    "You leave the household after spending some time with Sakura..."
    default uchihas_visited = False
    $ uchihas_visited = True
    default uchiha_tutorial = False
    $ uchiha_tutorial = True
    jump action_taken
        
        








label sakura_chores_label:
    $ chores_completed = 0
    $ sakura_bra_done = False
    $ sakura_dildo_done = False
    $ sakura_pants_done = False
    $ sakura_sheets_done = False
    show bg sakurabedroom
    show sakura_bra_chores
    show sakura_dildo_chores
    show sakura_panties_chores
    show sakura_sheets_chores
    with dissolve

    show screen sakura_chores
    $ ui.interact()



label sakura_chore_bra_text:
    hide screen sakura_chores
    bot"Auntie's bra casually laying around..."
    hide sakura_bra_chores
    with dissolve
    if chores_completed >= 3:
        hide screen sakura_chores with dissolve
        jump sakura_chores_finished
    else:
        show screen sakura_chores
        $ ui.interact()

label sakura_chore_dildo_text:
    if sakura_dildo_found == True:
        hide screen sakura_chores
        show sakura_dildo at parchment:
            zoom 0.6 yalign 0.01 rotate 30
        bot"I should probably not mess with that right now..."
        hide sakura_dildo with dissolve
        show screen sakura_chores
        $ ui.interact()

    default sakura_dildo_found = False
    $ sakura_dildo_found = True
    hide screen sakura_chores
    bot"What's that... purple thing hidden under the wardrobe?"
    hide sakura_dildo_chores with dissolve
    $ renpy.sound.play("/audio/soun_fx/ominous_sound.opus", channel="sfx3", loop=False, relative_volume = 1.5)
    show sakura_dildo at parchment:
        zoom 0.6 yalign 0.01 rotate 30
    bot"...!" with vpunch
    bot"A s-sex toy!?" with dissolve
    bot"Is Auntie Sakura using something like this to pleasure herself!?" with vpunch
    hide sakura_dildo with dissolve
    bot"Hmm, I wonder if I can use this somehow!"
    show sakura_dildo_chores with dissolve
    bot"But I should leave it where it was for now. Auntie did say to not snoop around. Hehe!"

    show screen sakura_chores
    $ ui.interact()

label sakura_chore_panties_text:
    hide screen sakura_chores
    bot"Those are some skimpy panties Auntie..." 
    hide sakura_panties_chores
    with dissolve
    if chores_completed >= 3:
        hide screen sakura_chores with dissolve
        jump sakura_chores_finished
    else:
        show screen sakura_chores
        $ ui.interact()

label sakura_chore_sheets_text:
    hide screen sakura_chores
    bot"Her sheets smell nice..." # 
    hide sakura_sheets_chores
    with dissolve
    if chores_completed >= 3:
        hide screen sakura_chores with dissolve
        jump sakura_chores_finished
    else:
        show screen sakura_chores
        $ ui.interact()

# --- Label to jump to after completion ---
label sakura_chores_finished:
    hide screen sakura_chores
    bot"Looks alright to me!"
    scene black with dissolve
    bot"On to Sarada's..."
    jump sarada_chores_label



    






default chores_completed = 0
default sakura_bra_done = False
default sakura_dildo_done = False
default sakura_pants_done = False
default sakura_sheets_done = False




screen sakura_chores():


    tag menu
    modal True

 
    frame:

        background "#222a"  # Dark background with some transparency
        
        # Position
        xalign 0.5
        yalign 0.1
        
        # Proper padding for content
        padding (15, 12, 15, 12)
        

        # Container for better organization
        hbox:
            spacing 10
            yalign 0.5
            

            
            text "Chores [chores_completed]/3":
                color "#fff"  # White text
                outlines [(2, "#000c", absolute(0), absolute(0))]  
                size 28  #
                hover_underline True  
                
                at transform:
                    on hover:
                        ease 0.2 size 30
                    on idle:
                        ease 0.2 size 28

    fixed:

        # --- Bra ---
        # Only show the button if this chore is NOT done yet
        if not sakura_bra_done:
            imagebutton:


                idle "sakura_bra_chores"    
                hover "sakura_bra_chores"   
                hover_sound "audio/soun_fx/select2.opus"
                activate_sound "audio/soun_fx/select4.opus"
                hovered [Show("displayTextScreen", displayText = "Pick up the bra")]
                unhovered [Hide("displayTextScreen")]
                focus_mask True             

                # Action(s) to perform when clicked
                action [
                    SetVariable("sakura_bra_done", True),
                    SetVariable("chores_completed", chores_completed + 1),
                    Hide("displayTextScreen"),
                    Jump("sakura_chore_bra_text")
                    ]

        if not sakura_dildo_done:
            imagebutton:


                idle "sakura_dildo_chores"
                hover "sakura_dildo_chores"
                hover_sound "audio/soun_fx/select2.opus"
                activate_sound "audio/soun_fx/select4.opus"
                hovered [Show("displayTextScreen", displayText = "???")]
                unhovered [Hide("displayTextScreen")]
                focus_mask True
                action [
                    SetVariable("sakura_dildo_done", True),
                    Hide("displayTextScreen"),
                    Jump("sakura_chore_dildo_text")
                    ]

        # --- Pants ---
        if not sakura_pants_done:
            imagebutton:


                idle "sakura_panties_chores"
                hover "sakura_panties_chores"
                hover_sound "audio/soun_fx/select2.opus"
                activate_sound "audio/soun_fx/select4.opus"
                hovered [Show("displayTextScreen", displayText = "Pick up the panties")]
                unhovered [Hide("displayTextScreen")]
                focus_mask True
                action [
                    SetVariable("sakura_pants_done", True),
                    SetVariable("chores_completed", chores_completed + 1),
                    Hide("displayTextScreen"),
                    Jump("sakura_chore_panties_text")
                    ]

        # --- Sheets ---
        if not sakura_sheets_done:
            imagebutton:


                idle "sakura_sheets_chores"
                hover "sakura_sheets_chores"
                hover_sound "audio/soun_fx/select2.opus"
                activate_sound "audio/soun_fx/select4.opus"
                hovered [Show("displayTextScreen", displayText = "Make the bed")]
                unhovered [Hide("displayTextScreen")]
                focus_mask True
                action [
                    SetVariable("sakura_sheets_done", True),
                    SetVariable("chores_completed", chores_completed + 1),
                    Hide("displayTextScreen"),
                    Jump("sakura_chore_sheets_text")
                    ]






init python:
    def close_sakuramenuinfo():
        renpy.hide_screen("sakuramenuinfo")
        renpy.hide_screen("displayTextScreen")
        renpy.hide_screen("test_sakuramenuinfo")


default selected_sakuramenuinfo = "Sakura"
screen sakuramenuinfo():
    

    on "show" action If(
        renpy.has_screen("test_sakuramenuinfo"),
        [Hide("sakuramenuinfo"), Show("test_sakuramenuinfo")],
        None
    )
    
    default dropdown_open = False
    zorder 100

    

    key "mouseup_3" action [Hide("sakuramenuinfo"),Hide("test_tsunade"),Hide("test_sakuramenuinfo"), Hide("displayTextScreen")] #close with rightclick
    
    #full screen
    frame:
        xysize (1280,720)
        background Frame("gui/overlay/game_menu_2.png")
        button: #screen sized button to prevent lcicks from behind screen
            xysize (config.screen_width, config.screen_height)
            background None
            action NullAction() # No action to perform on click

        #close button
        imagebutton:    
            at customzoom3
            xalign 0.95
            yalign 0.05
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            auto "map/ui_close_%s.png"
            hovered Show("displayTextScreen", displayText = "Close Menu")
            unhovered Hide("displayTextScreen")
            action [Function(close_sakuramenuinfo)]

        #left selection menu
        vbox:
            xalign 0.05 yalign 0.2
            text "Menu" xalign 0.5 size (50 if renpy.variant("pc") else 40)
        vbox:
            
            xalign (0.05 if renpy.variant("pc") else 0.02) yalign (0.5 if renpy.variant("pc") else 0.55)
            spacing 30
            #Tsunade
            textbutton "Sakura":
                xalign 0.5
                hover_sound "audio/soun_fx/select2.opus"
                activate_sound "audio/soun_fx/select4.opus"
                hovered Show("displayTextScreen", displayText = "Open Sakura's panel")
                unhovered Hide("displayTextScreen")
                action SetVariable("selected_sakuramenuinfo", "Sakura")

        vbox:
            xalign 1.2 yalign 0.5
            if selected_sakuramenuinfo ==  "Sakura":
                add "sakura normal" at dissolvehack:
                    zoom 1.0



        if selected_sakuramenuinfo == "Sakura":
            vbox:
                xalign 0.4 yalign 0.4
                text "Name: Sakura Haruno" xalign 0.5
                text "Age: 37" xalign 0.5
                null height 40 #add space
                frame:
                    xalign 0.65 yalign 0.53
                    background "#d3d3d320"
                    vbox:
                               
                        text "A lonely housewife with" xalign 0.5
                        text "a hot temper. Mother of your" xalign 0.5
                        text "childhood friend Sarada" xalign 0.5
                        text "and a close family friend" xalign 0.5
                        null height 20 #add space
                        use sakura_relationship_bar








screen sakura_relationship_bar:
    frame:
        xalign 0.5
        yalign 0.5
        background None  # Removes the background
        padding (0,0)    # Removes the padding
        vbox:
            spacing 10
            text "Relationship: [sakura_relationship]" xalign 0.5
            $ relationship_text = ""
            $ text_color = "#ffffff"  # default white
            if sakura_relationship <= 25:
                $ relationship_text = "Friends"
                $ text_color = "#a3d9ff"
            elif sakura_relationship <= 50:
                $ relationship_text = "Close-Friends"
                $ text_color = "#7fc8f8"
            elif sakura_relationship <= 75:
                $ relationship_text = "'Friends' with Benefits"
                $ text_color = "#5cb7f5"
  
            text "[relationship_text]" xalign 0.5 color text_color
            fixed:
                xsize 400
                ysize 30
                add PartnershipBar(400, 30, sakura_relationship, 0, 100)
















#Sarada


label sarada_chores_label:
    $ chores_completed_sarada = 0
    $ sarada_bra_done = False
    $ sarada_dildo_done = False
    $ sarada_pants_done = False
    $ sarada_sheets_done = False
    show bg saradabedroom
    show sarada_bra_chores
    show sarada_dildo_chores
    show sarada_panties_chores
    show sarada_sheets_chores
    with dissolve
    bot"So simplistic. I suppose she grew out of her girly phase..."
    bot"Do these two just fling their clothing all over the place? *Sigh*..."
    show screen sarada_chores
    $ ui.interact()



label sarada_chore_bra_text:
    hide screen sarada_chores
    bot"About ten sizes smaller than Auntie's..."
    hide sarada_bra_chores
    with dissolve
    if chores_completed_sarada >= 3:
        hide screen sarada_chores with dissolve
        jump sarada_chores_finished
    else:
        show screen sarada_chores
        $ ui.interact()

label sarada_chore_dildo_text:


    default sarada_dildo_found = False
    $ sarada_dildo_found = True
    hide screen sarada_chores
    bot"A family picture frame..."
    hide sarada_dildo_chores with dissolve
    $ renpy.sound.play("/audio/soun_fx/ominous_sound.opus", channel="sfx3", loop=False, relative_volume = 1.5)
    show sarada_frame at parchment:
        zoom 0.45 yalign 0.1 rotate 10
    bot"Looks cute..." with vpunch
    bot"There's a message left from my mentor Sasuke at the bottom, I presume for Sarada..." with dissolve
    bot "'I may often be gone, but my thoughts are always with you. Your strength and determination makes me prouder than you'll ever know. Continue to forge your own path, and remember that no matter how far apart we are, the bond we share can never be broken. Until I return home... -Your father'"
    hide sarada_frame with dissolve
    bot"Reminds me of [na_rel]... I don't know what to make of this when both are so often absent!"

    show screen sarada_chores
    $ ui.interact()

label sarada_chore_panties_text:
    hide screen sarada_chores
    bot"Much more modest than Auntie's..." # Replace text
    hide sarada_panties_chores
    with dissolve
    if chores_completed_sarada >= 3:
        hide screen sarada_chores with dissolve
        jump sarada_chores_finished
    else:
        show screen sarada_chores
        $ ui.interact()

label sarada_chore_sheets_text:
    hide screen sarada_chores
    bot"Has a nice scent..." # Replace text
    hide sarada_sheets_chores
    with dissolve
    if chores_completed_sarada >= 3:
        hide screen sarada_chores with dissolve
        jump sarada_chores_finished
    else:
        show screen sarada_chores
        $ ui.interact()

# --- Label to jump to after completion ---
label sarada_chores_finished:
    hide screen sarada_chores
    bot"Seems like I am done!"
    scene black with dissolve
    bot"I should check on Auntie Sakura..."
    jump chores_finished_label



default chores_completed_sarada = 0
default sarada_bra_done = False
default sarada_dildo_done = False
default sarada_pants_done = False
default sarada_sheets_done = False

screen sarada_chores():

    # Tag makes sure only one instance of this screen is shown.
    # Modal prevents clicking anything underneath until the screen is hidden.
    tag menu
    modal True

 
    frame:

        background "#222a"  # Dark background with some transparency
        
        # Position
        xalign 0.5
        yalign 0.1
        
        # Proper padding for content
        padding (15, 12, 15, 12)
        

        # Container for better organization
        hbox:
            spacing 10
            yalign 0.5
            

            
            # Styled text with better formatting
            text "Chores [chores_completed_sarada]/3":
                color "#fff"  # White text
                outlines [(2, "#000c", absolute(0), absolute(0))]  # Subtle outline
                size 28  # Larger text size
                hover_underline True  # Optional: underline on hover
                
                # Add a subtle glow effect when the number changes
                at transform:
                    on hover:
                        ease 0.2 size 30
                    on idle:
                        ease 0.2 size 28

    fixed:

        # --- Bra ---
        # Only show the button if this chore is NOT done yet
        if not sarada_bra_done:
            imagebutton:


                idle "sarada_bra_chores"    
                hover "sarada_bra_chores"   
                hover_sound "audio/soun_fx/select2.opus"
                activate_sound "audio/soun_fx/select4.opus"
                hovered [Show("displayTextScreen", displayText = "Pick up the bra")]
                unhovered [Hide("displayTextScreen")]
                focus_mask True             

                # Action(s) to perform when clicked
                action [
                    SetVariable("sarada_bra_done", True),
                    SetVariable("chores_completed_sarada", chores_completed_sarada + 1),
                    Hide("displayTextScreen"),
                    Jump("sarada_chore_bra_text")
                    ]

        if not sarada_dildo_done:
            imagebutton:


                idle "sarada_dildo_chores"
                hover "sarada_dildo_chores"
                hover_sound "audio/soun_fx/select2.opus"
                activate_sound "audio/soun_fx/select4.opus"
                hovered [Show("displayTextScreen", displayText = "???")]
                unhovered [Hide("displayTextScreen")]
                focus_mask True
                action [
                    SetVariable("sarada_dildo_done", True),
                    Hide("displayTextScreen"),
                    Jump("sarada_chore_dildo_text")
                    ]

        # --- Pants ---
        if not sarada_pants_done:
            imagebutton:


                idle "sarada_panties_chores"
                hover "sarada_panties_chores"
                hover_sound "audio/soun_fx/select2.opus"
                activate_sound "audio/soun_fx/select4.opus"
                hovered [Show("displayTextScreen", displayText = "Pick up the panties")]
                unhovered [Hide("displayTextScreen")]
                focus_mask True
                action [
                    SetVariable("sarada_pants_done", True),
                    SetVariable("chores_completed_sarada", chores_completed_sarada + 1),
                    Hide("displayTextScreen"),
                    Jump("sarada_chore_panties_text")
                    ]

        # --- Sheets ---
        if not sarada_sheets_done:
            imagebutton:


                idle "sarada_sheets_chores"
                hover "sarada_sheets_chores"
                hover_sound "audio/soun_fx/select2.opus"
                activate_sound "audio/soun_fx/select4.opus"
                hovered [Show("displayTextScreen", displayText = "Make the bed")]
                unhovered [Hide("displayTextScreen")]
                focus_mask True
                action [
                    SetVariable("sarada_sheets_done", True),
                    SetVariable("chores_completed_sarada", chores_completed_sarada + 1),
                    Hide("displayTextScreen"),
                    Jump("sarada_chore_sheets_text")
                    ]






init python:
    def close_saradamenuinfo():
        renpy.hide_screen("saradamenuinfo")
        renpy.hide_screen("displayTextScreen")
        renpy.hide_screen("test_saradamenuinfo")


default selected_saradamenuinfo = "Sarada"
screen saradamenuinfo():
    on "show" action If(
        renpy.has_screen("test_saradamenuinfo"),
        [Hide("saradamenuinfo"), Show("test_saradamenuinfo"), SetVariable("selected_saradamenuinfo", "Sarada")],
        None
    )
    
    default dropdown_open = False
    zorder 100

    

    key "mouseup_3" action [Hide("saradamenuinfo"),Hide("test_tsunade"), Hide("displayTextScreen")] #close with rightclick
    
    #full screen
    frame:
        xysize (1280,720)
        background Frame("gui/overlay/game_menu_2.png")
        button: #screen sized button to prevent lcicks from behind screen
            xysize (config.screen_width, config.screen_height)
            background None
            action NullAction() # No action to perform on click

        #close button
        imagebutton:    
            at customzoom3
            xalign 0.95
            yalign 0.05
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            auto "map/ui_close_%s.png"
            hovered Show("displayTextScreen", displayText = "Close Menu")
            unhovered Hide("displayTextScreen")
            action [Function(close_saradamenuinfo)]

        #left selection menu
        vbox:
            xalign 0.05 yalign 0.2
            text "Menu" xalign 0.5 size (50 if renpy.variant("pc") else 40)
        vbox:
            
            xalign (0.05 if renpy.variant("pc") else 0.02) yalign (0.5 if renpy.variant("pc") else 0.55)
            spacing 30
            #Tsunade
            textbutton "Sarada":
                xalign 0.5
                hover_sound "audio/soun_fx/select2.opus"
                activate_sound "audio/soun_fx/select4.opus"
                hovered Show("displayTextScreen", displayText = "Open Sarada's panel")
                unhovered Hide("displayTextScreen")
                action SetVariable("selected_saradamenuinfo", "Sarada")

        vbox:
            xalign 1.2 yalign 0.5
            if selected_saradamenuinfo ==  "Sarada":
                add "sarada happy" at dissolvehack:
                    zoom 1.0



        if selected_saradamenuinfo == "Sarada":
            vbox:
                xalign 0.4 yalign 0.4
                text "Name: Sarada Uchiha" xalign 0.5
                text "Age: 18" xalign 0.5
                null height 40 #add space
                frame:
                    xalign 0.65 yalign 0.53
                    background "#d3d3d320"
                    vbox:
                               
                        text "A determined kunoichi and" xalign 0.5
                        text "aspiring Hokage. Daughter of" xalign 0.5
                        text "Sakura and Sasuke, and your" xalign 0.5
                        text "close childhood friend." xalign 0.5
                        null height 20 #add space
                        use sarada_relationship_bar







screen sarada_relationship_bar:
    frame:
        xalign 0.5
        yalign 0.5
        background None  # Removes the background
        padding (0,0)    # Removes the padding
        vbox:
            spacing 10
            text "Relationship: [sarada_relationship]" xalign 0.5
            $ relationship_text = ""
            $ text_color = "#ffffff"  # default white
            if sarada_relationship <= 25:
                $ relationship_text = "Childhood Friends"
                $ text_color = "#a3d9ff"
            elif sarada_relationship <= 50:
                $ relationship_text = "Confused Friends"
                $ text_color = "#7fc8f8"
            elif sarada_relationship <= 75:
                $ relationship_text = "Girlfriend" # Friends with Benefits?
                $ text_color = "#5cb7f5"
  
            text "[relationship_text]" xalign 0.5 color text_color
            fixed:
                xsize 400
                ysize 30
                add PartnershipBar(400, 30, sarada_relationship, 0, 100)




