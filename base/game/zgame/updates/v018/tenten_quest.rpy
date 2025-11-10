#----------------------------------------------------------------------------------------------------------------------------------
label tenten_quest_start:
    $ renpy.sound.play("/audio/soun_fx/moving_sounds.opus", channel="sfx2", loop=False, relative_volume = 1)
    show boruto normal at left with dissolve
    show boruto surprised2 with dissolve
    "The shopkeeper is nowhere to be seen, but you hear some feint sounds coming from the backroom..."
    menu tenten_qauest_menu_start:
        "The shopkeeper's vanished from sight, but faint, frantic rustlings echo from the backroom, testing your curiosity..."
        "'Hello?'":
            show boruto normal with dissolve
            bo"Hello? Anybody here?"
            "Shopkeeper" "Where is it... Where is it!"
            "She seemed ignorant of your presence..."
            jump tenten_qauest_menu_start
        "Search the backroom":
            show blackscreen with dissolve
            "Shopkeeper" "Unbelievable! It had to be buried in this mess somewhere..."
            show tenten search1 with dissolve
            show tenten:
                easein 3 yalign 0.0
            "Shopkeeper" "If it's not here, then maybe—ugh, where else could it be?!"
            hide tenten search1
            hide blackscreen
            with dissolve
            show boruto suspicious with dissolve
            bot"Time to poke my nose where it doesn't belong! Let's see what's going on back there!"
            show boruto:
                easeout 2 xpos 2000
            label tenten_qauest_menu_start_replay:
            $ initialize_replay_defaults()
            scene black with dissolve
            "Shopkeeper" "It must be in here somewhere, surely!" with vpunch
            bot"O-oh, what's this!?" with vpunch
            show tenten stuck0 with dissolve
            call increaselust(20) from _call_increaselust_196
            "Stepping into the backroom, you catch the shopkeeper bent over and prostrated, wedged tight in a wooden contraption, her hips swaying as she rummages for something precious..."

            "Shopkeeper" "Not here either? Oh, come on! My most prized possession, gone? I'm not that careless, am I?!"
            "Shopkeeper" "No way I'm this much of a fool..."
            "Shopkeeper" "."
            "Shopkeeper" "..ugh, damn it!" with hpunch
            "Shopkeeper" "...Aghh! Ngh—get me out of this blasted thing!" with vpunch
            bot"Is she... actually trapped in there?"
            "Shopkeeper" "*Nervous chuckle* Heh... well, isn't this grand? Stuck like a pig in a trap! *Grunting Struggles*"
            "Shopkeeper" "...Aghh! Ugh... C-come on!" with vpunch
            menu tenten_stuck:
                "Shopkeeper" "...Aghh! Ugh... C-come on!"
                "*Cough cough*":
                    show tenten_bo_behind with dissolve
                    show tenten_bo_behind:
                        easein 1 alpha 0.1
                    bo"*Cough cough* A-ahem!" with vpunch
                    "Shopkeeper" "*Sharp gasp!* Oh, thank the stars! Someone's here? Please, kind stranger, could you spare a hand for a damsel in distress...?" with vpunch
                    menu:
                        "Shopkeeper" "*Sharp gasp!* Oh, thank the stars! Someone's here? Please, kind stranger, could you spare a hand for a damsel in distress...?"
                        "Grab that ass!":
                            bot"If she really is stuck in there then..."
                            hide tenten_bo_behind with dissolve
                            show tenten touch1 with dissolve
                            show tenten_stuck exp1 with dissolve:
                                zoom 0.5 xalign 1.0 yalign 1.0
                            "Shopkeeper" "H-hey! Who's back there? Are you helping or just groping me!?" with vpunch
                            bot"Heh! She really is stuck, if I keep my voice down, then she has no way of knowing who's behind her..."
                            menu:
                                "Shopkeeper" "H-hey! Who's back there? Are you helping or just groping me!?"
                                "Raise her dress!":
                                    bot"Why stop at a tease when I can feast my eyes on the whole prize?"
                                    show tenten touch2 with dissolve
                                    show tenten:
                                        easein 1 alpha 0.3
                                    show tenten_stuck at shake
                                    "Shopkeeper" "H-hey! What in the hell do you think you're pulling back there?!"
                                    $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                    scene tenten_lift 1 with fade
                                    show tenten_stuck exp2 with vpunch:
                                        zoom 0.5 xalign 1.0 yalign 1.0
                                    call increaselust(20) from _call_increaselust_197
                                    bot"N-no panties!? Clean shaven too, Shameless little minx..." with vpunch
                                    show tenten_stuck at shake
                                    "Shopkeeper" "*Shocked gasp!* Stop this instant, you fiend! I'll have you reported to the guards for this!" with vpunch
                                    bot"Report me? With what, your imagination? Hehe! You're not exactly in a position to tattle, sweetheart!"
                                    bot"Never seen a woman’s goods this close. It's dripping with temptation!"
                                    call increaselust(10) from _call_increaselust_198
                                    bot"It's practically calling for me, that sweet, musky aroma pulling me in..."

                                    default tenten_used = False
                                    default tenten_fucked = False
                                    menu tenten_freeuse:
                                        bot"It's practically calling for me, that sweet, musky aroma pulling me in..."
                                        "Spank that ass!" if tenten_godown_spank == 0:
                                            default tenten_godown_spank = 0
                                            $ tenten_godown_spank += 1
                                            $ tenten_used = True
                                            bot"How’s a man supposed to resist that plump, jiggling ass?"
                                            show tenten_hand spank with moveinright
                                            $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                            with vpunch
                                            scene tenten spank with dissolve 
                                            bot"A little love tap to set the mood!" with vpunch
                                            scene tenten_lift 1
                                            show tenten_spank1_1 zorder 100
                                            with dissolve
                                            show tenten_stuck exp2 with vpunch:
                                                zoom 0.5 xalign 1.0 yalign 1.0
                                            show tenten_stuck exp1 with dissolve
                                            show tenten_stuck at shake
                                            "Shopkeeper" "*Gasp!* Eek! You bastard! I'll strangle you once I get out of here!" with vpunch
                                            jump tenten_freeuse
                                        "{color=[hatredcolor]}Spank her again!{/color}" if tenten_godown_spank >=1:
                                            if tenten_godown_spank == 1:
                                                $ tenten_godown_spank += 1
                                                bot"That felt good, left a nice rosy imprint too!"
                                                show tenten_hand spank zorder 101 with moveinright
                                                $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                                with vpunch
                                                scene tenten spank with dissolve 
                                                call changeHatred(1) from _call_changeHatred_145
                                                bot"But that juicy backside’s practically screaming for another round!" with vpunch
                                                scene tenten_lift 1
                                                show tenten_spank1_2 zorder 100
                                                with dissolve
                                                show tenten_stuck exp2 with vpunch:
                                                    zoom 0.5 xalign 1.0 yalign 1.0
                                                show tenten_stuck at shake
                                                "Shopkeeper" "Ow! W-who's the coward back there?! I'll slice your grubby paws off when I get you!" with vpunch

                                                jump tenten_freeuse
                                            elif tenten_godown_spank >=2:
                                                
                                                if tenten_godown_spank == 2:
                                                    bot"Her ass is blooming with bruises! Gorgeous..."
                                                else:
                                                    bot"I am about to carve a permanent signature on your ass!"
                                                $ tenten_godown_spank += 1
                                                show tenten_hand spank zorder 102 with moveinright
                                                $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                                with vpunch
                                                scene tenten spank with dissolve 
                                                call changeHatred(1,"tentenspank1",2) from _call_changeHatred_146
                                                
                                                scene tenten_lift 1
                                                show tenten_spank1_3 zorder 100
                                                with dissolve
                                                show tenten_stuck exp4 with vpunch:
                                                    zoom 0.5 xalign 1.0 yalign 1.0
                                                show tenten_stuck at shake
                                                "Shopkeeper" "Aww!! Y-you b-bastard! *Sniffles* You'll pay for that!" with vpunch
                                                bot"Poor thing... Too bad I am addicted to the feeling of spanking it and watching the ripples run through your body!" with vpunch
                                                show tenten_stuck exp3 with dissolve
                                                jump tenten_freeuse


                                            $ tenten_godown_spank += 1
                                            jump tenten_freeuse
                                        "Go down on her":
                                            $ tenten_used = True
                                            hide tenten_stuck with dissolve
                                            bot"I can't help but wonder, does it taste as good as it looks too?"
                                            bot"This is a once-in-a-lifetime buffet, and I'm starving!"
                                            default tenten_godown = False
                                            $ tenten_godown = True
                                            bot"I..."
                                            show tenten_lift cunnilingus1 with dissolve
                                            bot"I have to know what it tastes like!"
                                            $ renpy.sound.play("/audio/soun_fx/lickpenis1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                                            show tenten_cunnilingus_anim1 with dissolve
                                            show tenten_stuck exp2 with vpunch:
                                                    zoom 0.5 xalign 1.0 yalign 1.0
                                            "Shopkeeper" "*Gasp!* Is t-that!?"
                                            show tenten_stuck at shake
                                            "Shopkeeper" "H-hey! Who s-said you can do that!" with vpunch
                                            $ renpy.sound.play("/audio/soun_fx/lickpenis1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                                            "Shopkeeper" "Get your slimy tongue off me, you degenerate!" with vpunch
                                            bot"T-tastes salty... Slightly musky but, not unpleasant!"
                                            show tenten_stuck exp1 with dissolve
                                            "Shopkeeper" "Don't t-touch me there, you creep!" with vpunch
                                            show tenten_lift 1
                                            hide tenten_cunnilingus_anim1
                                            hide tenten_stuck
                                            with dissolve
                                            jump tenten_freeuse
                                        "???" if tenten_godown == False:
                                            "Use the other options first..."
                                            jump tenten_freeuse
                                        "Taste her other hole too!" if tenten_godown == True:
                                            
                                            default tenten_godown_anal = False
                                            $ tenten_godown_anal = True
                                            $ tenten_used = True
                                            bot"And what about that tight little backdoor..."
                                            bot"If I'm going full deviant, then I need to taste that asshole too!"
                                            show tenten_lift anilingus1 with dissolve
                                            bot"I have to know what it tastes like!"
                                            show tenten_stuck exp1 with vpunch:
                                                    zoom 0.5 xalign 1.0 yalign 1.0
                                            show tenten_stuck at shake
                                            "Shopkeeper" "*Choked gasp!*"
                                            "Your hot breath grazes her puckered anus, and her cheeks clench tight, puckering her holes in a desperate reflex."
                                            "Shopkeeper" "Don't you even dream of violating me there, you twisted freak!"
                                            menu:
                                                "Shopkeeper" "Don't you even dream of violating me there, you twisted freak!"
                                                "Push your tongue inside!":
                                                    pass
                                                "(What am I thinking...)":
                                                    show tenten_lift 1
                                                    hide tenten_stuck
                                                    with dissolve
                                                    bot"What's wrong with me—licking an asshole?!"
                                                    bot"Maybe I'm too far gone... or maybe this curse is just warming up!"
                                                    jump tenten_freeuse
                                                
                                            $ renpy.sound.play("/audio/soun_fx/lickpenis1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                                            show tenten_anilingus_anim1 with dissolve
                                            show tenten_stuck exp2 with vpunch:
                                                    zoom 0.5 xalign 1.0 yalign 1.0
                                            "Shopkeeper" "*Gasp!* You f-freak! W-what are you, a d-dog?"
                                            show tenten_stuck at shake
                                            bot"Tastes w-weird! But what did I expect..."
                                            call increaselust(10) from _call_increaselust_199
                                            bot"The depravity of it though, I am enjoying this feeling!"
                                            "Shopkeeper" "Eeek! Y-you f-freaking weirdo!" with vpunch
                                            show tenten_lift 1
                                            hide tenten_anilingus_anim1
                                            hide tenten_stuck
                                            with dissolve
                                            jump tenten_freeuse

                                        "{color=[hatredcolor]}!?{/color}" if hatred >= 20 and percentage >= 100:
                                            if persistent.current_activation == "Free":
                                                call supp_rew from _call_supp_rew_4
                                                jump tenten_freeuse
                                            else:
                                                jump tenten_quest_rape
                                        "{color=[hatredcolor]}????{/color}" if hatred <20 and tenten_godown_spank >= 1:
                                            bot"Could I... No-no-no! What am I even thinking!"
                                            jump tenten_freeuse
                                        "Leave her be":
                                            bot"Better get going before she realizes!"
                                            scene black with dissolve
                                            "You left the establishment before you raised any suspicion, leaving the shopkeeper alone with her troubles..."
                                            jump action_taken
                                        

                                "Leave her be":
                                    bot"Better get going before she realizes!"
                                    scene black with dissolve
                                    jump action_taken
                                
                            
                            "test"

                        "'Uhm... Need some help?'":
                            jump tenten_needsomehelp
                        

                "'Uhm... Need some help?'":
                    show tenten_bo_behind with dissolve
                    show tenten_bo_behind:
                        easein 1 alpha 0.1
                    label tenten_needsomehelp:
                    bo"Uhm... Need some help?"
                    "Shopkeeper" "{size=-8}*Gasps*! I think I recognize that voice...{/size}"
                    "Shopkeeper" "*Gasps*! My luck! W-why yes, I could use some help! Perhaps you could lend me a h-hand good sir...?" with vpunch
                    bo"I could try! What would you prefer for me to do?"
                    "Shopkeeper" "Just... grab my waist and tug gently, maybe? I'm wedged in here like a cork!"
                    bo"Piece of cake! Here we go..."
                    hide tenten_bo_behind with dissolve
                    show tenten stuck1 with dissolve
                    show tenten_stuck exp1 with dissolve:
                        zoom 0.5 xalign 1.0 yalign 1.0
                    "Shopkeeper" "Eek! Easy, easy! Don't rip me in half!" with vpunch
                    call increaselust(10) from _call_increaselust_200
                    bo"S-shall I stop?"
                    "Shopkeeper" "W-what? No! Just try p-pulling a little harder!" with vpunch
                    menu:
                        "Shopkeeper" "W-what? No! Just try p-pulling a little harder!"
                        "Take advantage of the situation...":
                            bot"This girl certainly has an ass on her..."
                            bot"She's clueless... I bet I could cop a feel and she'd never know!"
                            show tenten:
                                easein 1 alpha 0.3
                            show tenten_stuck at shake
                            "Shopkeeper" "What's the hold-up? Put some muscle into it, can't you?!"
                            show tenten:
                                easein 1 alpha 1
                            bo"Oh I certainly can! Ready?"
                            scene tenten stuck anim2 with dissolve
                            bo"And..."
                            show tenten_stuck exp2 with dissolve:
                                zoom 0.5 xalign 1.0 yalign 1.0
                            "Shopkeeper" "*Gasp!* Hey, I said careful, not cop a feel!" with vpunch
                            "Your hands slide low, thumbs digging into the soft curve near her womanhood, brushing the silk hem of her dress and grazing the warmth hidden beneath..."
                            bo"Just getting a better grip, don’t panic! Here we go..." with vpunch

                            scene tenten_stuck_grope1 with dissolve
                            "You pretended to be of help, but in reality, you were helping yourself, taking the opportunity to feel whatever you could justify under this silly pretense..."
                            show tenten_stuck exp2 with vpunch:
                                zoom 0.5 xalign 1.0 yalign 1.0
                            "Shopkeeper" "A-are you sure this is helping? Just..."
                            bot"I should play it safe, now's the time to pull hard!"
                            show tenten_stuck exp1 with dissolve
                            "Shopkeeper" "...Aghh! Ugh..." with vpunch
                            bo"I think it's w-working!" with vpunch
                            default tenten_mild_grope = False
                            $ tenten_mild_grope = True
                            jump tenten_quest_end_good
                            


                            

                        "Pull harder!":
                            bo"Ready? And..."
                            scene tenten stuck1 with dissolve:
                                zoom 1.1 xalign 0.5
                            "You firmly grabbed her waist once more, and pulled as hard as you could!"
                            "Shopkeeper""Hnnh!! It h-hurts!" with vpunch
                            jump tenten_quest_end_good

                        

                "{color=[hatredcolor]}Stay silent...{/color}": # (supporter_scene = True)
                    jump shopkeeper_staysilent_l
                    # $ call_label_action("shopkeeper_staysilent_l")
                    call supp_rew from _call_supp_rew_2
                    jump tenten_stuck
                    
                        
                
        "Leave":
            scene black with dissolve
            jump market
        
#---------------------------------------------


label tenten_quest_end_good:
    $ renpy.sound.play("/audio/soun_fx/wakeup.opus", channel="sfx3", loop=False, relative_volume = 0.6)
    with Shake((0, 0, 0, 0), 1, dist=20, peak_time=0.8, smoothness=50)
    $ renpy.sound.play("/audio/soun_fx/pop.mp3", channel="sfx2", loop=False, relative_volume = 1.2)
    scene black with flash
    "..."
    $ renpy.sound.play("/audio/soun_fx/woman_crying1.opus", channel="sfx3", loop=False, relative_volume = 0.8)
    "Shopkeeper" "*Sniffles* I..."
    "You pulled and pulled, until..."
    show tenten quest_end1 with dissolve
    "The shopkeeper shot out of the contraption with enough force to throw you on your back, and her on top of you..."
    "She placed her arms around your shoulders and looked at you straight into the eyes. He puppy eyes made it seem like she was expecting something from you, while her tears kept crashing down on your chest..."
    if tenten_mild_grope == True:
        bot"Is she m-mad at me?"
    else:
        bo"Is everything o-okay?"
    "Shopkeeper" "I lost it! *Sniffles*" with vpunch
    show tenten quest_end2 with dissolve
    if tenten_mild_grope == True:
        bot"Phew! It seems I got away with this time! Not only that..."
        call increaselust(10) from _call_increaselust_201
        bot"But now she is sitting on top of my cock too!"
        bo"Uuh, lost what exactly?"
    else:
        bo"You lost... it? Lost what exactly?"
    $ renpy.sound.play("/audio/soun_fx/woman_crying2.opus", channel="sfx3", loop=False, relative_volume = 0.8)
    "Shopkeeper" "My most valuable possession. My pendant... *Sniffles*"
    "Shopkeeper" "My family's only keepsake! *Sniffles* I can't believe it. It's gone!" with vpunch
    menu:
        "Shopkeeper" "My family's only keepsake! *Sniffles* I can't believe it's gone!"
        "Reassure her...":
            bo"It must be somewhere around here, right?"
            show tenten quest_end2_2 with dissolve
            bo"Maybe I could help, but shouldn't we get off the floor first?"
        "{color=[hatredcolor]}Take advantage of the situation...{/color}":
            bot"Oh? I like were this is going! Perhaps I could do something about that..."
            show tenten quest_end2_1 with dissolve
            call changeHatred(1) from _call_changeHatred_147
            bo"You lost... your pendant, huh?"
            "Shopkeeper" "Y-yes... *Sniffles*"
            show tenten with dissolve:
                zoom 1.2 xalign 1.0 yalign 1.0
            "You kept brushing your hand against her thigh in a seemingly re-assuring fashion..."
            bo"Perhaps I could help you with that..."
            show tenten with dissolve:
                zoom 1.3 xalign 0.4 yalign 0.0
            "Shopkeeper" "Y-you would do that? *Sniffles*"
            bo"Of course I would!"
            bot"With the right incentive... Hehe!"
            bo"Let's discuss the terms after you get off my-"
    scene black with vpunch
    "Shopkeeper" "O-oh, Sorry! *Sniffles* My mind went blank for a second..."
    "The shopkeeper pats herself clean, hold back her tears, and turns to address you..."
    scene shop day with dissolve:
        zoom 0.5
    show ten sad1 at right with dissolve
    show boruto normal at left with dissolve
    "She leans back against a wooden counter, and takes a deep breath..."
    "Shopkeeper" "I suppose I owe you an apology, for bursting out in tears on you..."
    bo "It wasn't a problem..."
    "Shopkeeper" "Who knows how long I'd be stuck in there for if you didn't show up when you did..."
    "Shopkeeper" "Introductions are due, don't you think so?"
    ten "My name's Tenten..."
    bo"I am-"
    ten"And you are [bo_name], right?" with vpunch
    show boruto surprised2 with dissolve
    bo"Y-you know my name? Have we met before?" with vpunch
    ten"Not directly, but I used to hang out with your [na_rel] and [hin_rel] back in the day..."
    ten"A lot has happened since then, and we've mostly lost touch by now, but you and your [na_rel] are like two peas in a pod."
    ten"Your [na_rel] was just as weird as you are, both poking girls around when it's none of your business..."
    show boruto embarassed with dissolve
    bo"...H-huh?"
    show boruto normal with dissolve
    ten"So yeah, I know who you are..."
    ten "In any case, t-thank you, for helping me out. *Sniffles*"
    bo"So, you lost something important to you?"
    ten"My family's keepsake..."
    ten"I lost both my parents during the last Shinobi War. The one thing I had to remind me of them *Sniffles* was a pendant with an engraving of us."
    ten"It doesn't make any sense! I always kept it at the same place, safe in the backroom. How could it have disappeared!?"
    show boruto surprised2 with dissolve
    bo"A thief perhaps?"
    ten"Improbable, I always make sure to keep this place secured..."
    ten"Damn it! I have to find it! That pendant means the world to me! *Sniffles*"
    menu:
        ten"Damn it! I have to find it! That pendant means the world to me! *Sniffles*"
        "I can try to help!":
            show boruto worried with dissolve
            bo"Sound like it means a lot to you..."
            bo"I could try helping you find it."
            ten"You would do that for me?"
            bo"Of course..."
            show ten sad2 with dissolve
            ten"I would be forever in your debt! Please, if you find or hear anything that could be of help, please let me know!"

        "{color=[hatredcolor]}(I sense an opportunity!){/color}":
            show boruto sceeming with dissolve
            bot"If that pendant means so much for her then..."
            call changeHatred(1) from _call_changeHatred_148
            show boruto sceeming2 with dissolve
            bot"I sense an opportunity ahead!"
            show boruto snob with dissolve
            bo"Perhaps I could find it for you..."
            ten"You would do that for me?"
            bo"Well, maybe... for the right price!" with vpunch
            ten"P-please, I'd do anything to have my pendant back. I barely scrap by as is, so I am afraid money isn't really an option..."
            ten"But perhaps we could work something else out?"
            bot"Work something out we will, Tenten! Just you wait..."
            bo"Hmm, I'll think on it then!"
            ten"I would be forever in your debt! Please, if you find or hear anything that could be of help, please let me know!"
            bot"I better find that pendant of hers before she does then!"
            bot"I wonder what I could ask in exchange for it... Hehe!"
    show boruto normal with dissolve
    bo"Right! I'll stay vigilant then. I'll let you know if I come across anything useful!"
    hide boruto with dissolve
    show ten sad2 with dissolve
    ten"T-thank you! Please do... *Sniffles*"
    scene black with dissolve
    $ renpy.end_replay()
    $ tenten_quest_activated = True
    jump action_taken
        