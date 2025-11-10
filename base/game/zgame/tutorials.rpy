label bedroom_hallway:
    if boruto_location == "hallway":
        scene bg day:
            zoom 0.67
    else:
        $ boruto_location = "hallway"
        scene bg day with dissolve:
            zoom 0.67
    # show screen stats
    call hideButtons from _call_hideButtons_9
    call screen housemap  

label freeroam:
    dev"The game will soon allow you to freely roam your house and other areas"
    dev"Use the white buttons at the bottom left of your screen to navigate"
    dev"For now click on the living room icon to find your [hin_rel]"
    jump housetutorial


label housetutorial:
    $ hin_location = 'livingroom'
    $ him_location = 'livingroom'
    # show screen stats
    call screen housemap


label housetutorial2:
    window hide
    $ hin_location = 'borutobedroom'
    $ him_location = 'himawaribedroom'

    # show screen stats
    call screen housemap


label bedroomtutorial:
    hide screen actionbuttonshouse
    call hideUI from _call_hideUI_59
    $ boruto_location = "borutobedroom"
    $ strengthbutton = False
    $ day_part = 3
    $ day_number = 0
    $ actionbutton = True
    $ infobutton = False 
    scene bg bb night with dissolve
    if introhatredplan == True:
        show boruto bonerevil4 with dissolve
    else:
        show boruto normal at center with dissolve
    bo"..."
    bo"What a day..."
    dev"Days will be split in 4 parts from now on. 'Morning', 'Evening', 'Night' and 'Midnight'."
    dev"Each part of the day will present different options. You will have the freedom to explore and act as you see fit."
    dev"For now, just sleep to advance the story..."
    menu tutorialbedroom:
        
        bot"I am tired..."
        "Sleep" if introhatredplan == False:
            call hideButtons from _call_hideButtons_10
            $ completed_intro += 1
            if completed_intro == 4:
                $ completed_intro += 1
                bot"At last, my favourite past-time activity..."
                scene black with dissolve
                $ day_part +=1
                jump action_taken  #hacky way to fix time/day text disp;lay
        
        "{color=[hatredcolor]}Execute your plan!{/color}" if introhatredplan == True:

            $ introsecrethatredcummed = True

            $ boruto_location = "nightspy" #handles the quesiton amrk button at left of screen
            $ infobutton ="active"
            bot"But I have to endure a little while longer..."
            label replay_secretscenehate:
            $ initialize_replay_defaults()
            scene black with dissolve
            "."
            ".."
            "..."
            "Some time passes..."
            scene bg bb night with dissolve
            show boruto bonerevil4 with dissolve
            bot"It's time to pay [hin_rel] a little visit..."
            scene black with dissolve
            play sound "audio/soun_fx/dooropen.opus" volume 0.7
            "You wait until midnight and sneak into [hin_name]'s bedroom..."
            scene introhatredintro with dissolve:
                zoom 0.5
            bot"There you are!"
            scene introhatredintro with dissolve:
                zoom 0.6 xalign 0.0 yalign 1.0
            bot"You are looking so serene [hin_rel] while you sleep in your sexy night gown. Your little light on, even at your age..."
            show introhatredintro with dissolve:
                zoom 0.7 xalign 1.0 yalign 0.5
            show introhatredintro with dissolve:
                easein 3 zoom 0.7 xalign 0.0
            bot"But you see [hin_rel]..."
            bot"As serene as you are, you still have to pay for trying to guilt-trip me earlier today. And after I am done with you, you are going to be looking anything but serene!"
            scene introhatredintro with dissolve:
                zoom 0.5
            bot"Still, I better be careful... [hin_rel] is a heavy sleeper because of all the work she does around the house. But If she wakes up, I am as good as dead."
            menu:
                bot"I better be careful... If she wakes up I am as good as dead."
                "Approach from behind":
                    bot"If only I could get a peek of that big fat ass of yours..."
                    
                    bot"Maybe if I..."
                    scene iha0 with dissolve:
                        zoom 0.5
                    "You sneaklily try position yourself closer to her..."
                    show iha1 with dissolve:
                        zoom 0.5

                    bot"Oh shit, she moved! I don't think she realized yet though..."
                    bot"Just looking at how her ass protrudes through the bed sheets... it's making me want to dive bomb in there face first."
                    bot"You wouldn't mind if I moved your blanket a little bit, would you [hin_rel]?"
                    "Explore the scene to find 'hotspot' zones. Green hotspots will advance the scene."
                    show screen sleep_iha1
                    $ ui.interact()

                    label sleep_iha1_head:
                        default sleep_iha1_head_counter = 0
                        show iha1 with dissolve:
                            zoom 0.7 xalign 0.0 yalign 1.0
                        if sleep_iha1_head_counter > 0:
                            bot"Just you wait [hin_rel]... Perhaps I'll have a little something for your face as well tonight..."
                            jump sleep_iha1_headend
                        bot"You thought I'd let you step all over me and try to guilt-trip me [hin_rel]?"
                        bot"Your pretty little innocent face won't stop me from punishing you..."
                        label sleep_iha1_headend:
                            $ sleep_iha1_head_counter+= 1
                            show iha1 with dissolve:
                                zoom 0.5
                            show screen sleep_iha1
                            $ ui.interact()

                    label sleep_iha1_tits:
                        default sleep_iha1_tits_counter = 0
                        show iha1 with dissolve:
                            zoom 0.7 xalign 0.5 yalign 1.0
                        if sleep_iha1_tits_counter > 0:
                            bot"I can't believe you carry those around everyday and expect me to not salivate over them..."
                            jump sleep_iha1_titsend
                        bot"The badoonkers you carry on you [hin_rel]... I swear, one day I'll have my cock buried in between them!"
                        label sleep_iha1_titsend:
                            $ sleep_iha1_tits_counter+= 1
                            show iha1 with dissolve:
                                zoom 0.5
                            show screen sleep_iha1
                            $ ui.interact()

                    menu jumpfromsleep_iha1:
                        bot"You wouldn't mind if I moved your blanket a little bit, would you [hin_rel]?"
                        "Attempt to remove blanket":
                            pass
                    show iha2 with dissolve:
                        zoom 0.5
                    bot"Damn! Just a little bit more [hin_rel]... Don't you go ruining my fun now!"
                    "You managed to pull the blanket just a little bit before she shifted her posture once again..."
                    bot"...This time in one fell swoop!"
                    menu:
                        bot"...This time in one fell swoop!"
                        "Attempt to remove blanket again!":
                            show iha2 with dissolve:
                                zoom 0.56 xalign 1.0 yalign 0.5
                            bot"Just a little bit m-"
                            #cg a3
                            show iha3 with dissolve:
                                zoom 0.5
                            hin"Mmmm... *Snorts*" with vpunch
                            bot"Fuck! That scared the shit out of me... Can't you sit still for a second [hin_rel]?"
                            bot"Although this worked in my favor! Her little gown slid up..."
                            bot"Which means that whatever you are hiding behind this blanket is fully exposed under it!"
                            "Explore the scene to find 'hotspot' zones. Green hotspots will advance the scene."
                            show screen sleep_iha3 with dissolve
                            $ ui.interact()

                            label sleep_iha3_head:
                                default sleep_iha3_head_counter = 0
                                show iha3 with dissolve:
                                    zoom 0.7 xalign 0.0 yalign 0.5
                                if sleep_iha3_head_counter > 0:
                                    bot"If only you knew what your own [hin_rel_to_bo] is planning for you! I bet you wouldn't be sleeping so peacefully... "
                                    jump sleep_iha3_headend
                                bot"All you had to do was show some compassion [hin_rel]. Instead, you put the blame on me... Now in turn, I will put something on you!"
                                label sleep_iha3_headend:
                                    $ sleep_iha3_head_counter+= 1
                                    show iha3 with dissolve:
                                        zoom 0.5
                                    show screen sleep_iha3
                                    $ ui.interact()

                            label sleep_iha3_tits:
                                default sleep_iha3_tits_counter = 0
                                show iha3 with dissolve:
                                    zoom 0.7 xalign 0.5 yalign 0.8
                                if sleep_iha3_tits_counter > 0:
                                    bot"I am almost tempted to rip off your little gown and set those tits of yours free from their oppresion!"
                                    jump sleep_iha3_titsend
                                bot"That sexy black laced gown of yours is struggling to contain your massive tits. Even your perky nipples are poking against the soft fabric of it, almost asking to break free..."
                                label sleep_iha3_titsend:
                                    $ sleep_iha3_tits_counter+= 1
                                    show iha3 with dissolve:
                                        zoom 0.5
                                    show screen sleep_iha3
                                    $ ui.interact()


                            
                            menu jumpfromsleep_iha3:
                                bot"Which means that whatever you are hiding behind this blanket is fully exposed under it!"
                                "Remove blanket":
                                    show iha3 with dissolve:
                                        zoom 0.65 xalign 0.6 yalign 0.5
                                    bot"Now show me what you are hiding down there [hin_rel]!"
                                    show ihafinal with dissolve:
                                        zoom 0.5
                                    bot"H-" with vpunch
                                    call increaselust(30) from _call_increaselust_59
                                    bot"Holy shit..."
                                    bot"I mean... I knew you were carying [hin_rel], but this is the first time I catch a glimpse of you like this..."
                                    bot"I would never guess you slept in those slutty black laced panties..."
                                    bot"Is this what [na_rel] woke up to every day? To think he'd leave you alone like this... what an idiot!"
                                    bot"No matter... I'll be taking care of you now, [hin_rel]!"
                                    show ihafinal with dissolve:
                                        zoom 0.7 xalign 0.5 yalign 0.5
                                    bot"Your thick fucking ass is just so... juicy."
                                    show ihafinal with dissolve:
                                        zoom 0.7 xalign 1.0 yalign 1.0
                                    bot"Even your little perfectly-shaped feet are arousing."
                                    show ihafinal with dissolve:
                                        zoom 0.5
                                    bot"I can't believe I am rock hard creeping on you [hin_rel]. But..."
                                    bot"Who the fuck can blame me when your body was sculpted in an image of a freaking sex goddess..."
                                    bot"It's like every part of you was made to be worshipped. And I will do just that!"
                                    "Explore the scene to find 'hotspot' zones. Green hotspots will advance the scene."
                                    show screen sleep_ihafinal with dissolve
                                    $ ui.interact()


                            label ihafinal_head:
                                default sleep_ihafinal_counter = 0
                                show ihafinal with dissolve:
                                    zoom 0.7 xalign 0.0 yalign 0.1
                                if sleep_ihafinal_counter > 0:
                                    bot"It's time I have my revenge on you!"
                                    jump ihafinal_headEND
                                bot"I've endured enough [hin_rel]. Tonight, you are mine to do with as I please!"
                                label ihafinal_headEND:
                                    $ sleep_ihafinal_counter+= 1
                                    show ihafinal with dissolve:
                                        zoom 0.5
                                    show screen sleep_ihafinal
                                    $ ui.interact()
                            
                            label ihafinal_feet:
                                show ihafinal with dissolve:
                                    zoom 0.6 xalign 1.0 yalign 1.0
                                bot"Of course I would pay tribute to your feet..."
                                show acrotchpov_bg with dissolve:
                                    zoom 0.8 yalign 1.0 xpos 273
                                "You placed your kness on the edges of the mattress, getting as close to [hin_name]'s ass as you could without disrupting her sleep and..."
                                bot"Of course I would pay tribute to your pretty little feet..."
                                $ renpy.sound.play("/audio/soun_fx/jerkoff1.opus", channel="sfx2", loop=False, relative_volume = 0.2) 
                                show acrotchpov_bg at pov_jerkoff(0.2,5):
                                    subpixel True zoom 0.8 yalign 1.0
                                bot"I will c-cover your feet in my semen [hin_rel]!"
                                show acrotchpov_bg at pov_jerkoff(0.2,2):
                                    subpixel True zoom 0.8 yalign 1.0
                                bot"Take..."
                                show acrotchpov_bg at pov_jerkoffpullback(0.2):
                                    subpixel True zoom 0.8 yalign 1.0
                                bot"My..."
                                show acrotchpov_bg at pov_jerkoffthrust():
                                    subpixel True zoom 0.8 yalign 1.0
                                $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.3) 
                                show afinal feet1 behind acrotchpov_bg with flash:
                                    zoom 0.6 xalign 1.0 yalign 1.0
                                show acrotchpov_bg:
                                    easein 0.4 yoffset 40
                                bot"Seed!"
                                call decreaselust(20) from _call_decreaselust_50
                                bot"Now that's a pretty sight [hin_rel]... Your sexy soles covered in my spunk!"
                                $ renpy.sound.play("/audio/soun_fx/jerkoff2.opus", channel="sfx2", loop=False, relative_volume = 0.2) 
                                show acrotchpov_bg at pov_jerkoff(0.2,5):
                                    subpixel True zoom 0.8 yalign 1.0
                                bot"But I am nowhere near satisfied yet!"
                                show acrotchpov_bg at pov_jerkoffpullback(0.2):
                                    subpixel True zoom 0.8 yalign 1.0
                                bot"I have more in store f-for you!"
                                show acrotchpov_bg at pov_jerkoffthrust():
                                    subpixel True zoom 0.8 yalign 1.0
                                $ renpy.sound.play("/audio/soun_fx/cum2.opus", channel="sfx2", loop=False, relative_volume = 0.3) 
                                show afinal feet2 behind acrotchpov_bg with flash:
                                    zoom 0.6 xalign 1.0 yalign 1.0
                                show acrotchpov_bg:
                                    easein 0.4 yoffset 40
                                bot"Take this!"
                                show acrotchpov_bg at pov_jerkoffpullback(0.2):
                                    easein 0.3 subpixel True zoom 0.8 yalign 1.0 xoffset -130
                                bot"And..."
                                $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                                show acrotchpov_bg at pov_jerkoffthrust():
                                    subpixel True zoom 0.8 yalign 1.0
                                show afinal feet3 behind acrotchpov_bg with flash:
                                    zoom 0.6 xalign 1.0 yalign 1.0
                                bot"This!"
                                show acrotchpov_bg:
                                    easein 0.3 yoffset 60
                                call decreaselust(40) from _call_decreaselust_51
                                $ renpy.sound.play("/audio/soun_fx/panting.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                                bo"*Panting*"
                                bot"Fuck! W-what have I done... [hin_rel]'s feet are drenched in my cum"
                                bot"Could all this semen even dry off by the morning?"
                                scene afinal feet3 with fade:
                                    zoom 0.5
                                bot"Look at you [hin_rel]..."
                                scene afinal feet3 with dissolve:
                                    zoom 0.9 xalign 0.7 yalign 1.0
                                show afinal feet3 with dissolve:
                                    easein 5 zoom 1 xalign 1.0 yalign 1.0
                                bot"Still so blissfuly unaware of the fact that you are covered in your [hin_rel_to_bo]'s cum. Looking at you like this..."
                                call increaselust(10) from _call_increaselust_60
                                bot"It excites me even more!"
                                scene afinal feet3 with fade:
                                    zoom 0.5
                                bot"Now I realize. All this time I've been mistaking the strong feelings I was having for you for something they were not [hin_rel]..."
                                bot"Those weren't feelings of love, at least not entirely..."
                                bot"What I truly felt was lust! Lust over you and your whore-like body!"
                                menu:
                                    bot"What I truly felt was lust! Lust over you and your whore-like body!"
                                    "{color=[hatredcolor]}Pay a final tribute!{/color}":
                                        show afinal feet3 with dissolve:
                                            zoom 0.6 xalign 1.0 yalign 1.0
                                        show acrotchpov_bg with dissolve:
                                            zoom 0.8 yalign 1.0 xpos 273
                                        bot"And my lust for you knows no bounds!"
                                        $ renpy.sound.play("/audio/soun_fx/jerkoff2.opus", channel="sfx2", loop=False, relative_volume = 0.2) 
                                        show acrotchpov_bg at pov_jerkoff(0.2,5):
                                            subpixel True zoom 0.8 yalign 1.0
                                        bot"Now that I discovered this intoxicating feeling of lust..."
                                        show acrotchpov_bg at pov_jerkoff(0.2,2):
                                            subpixel True zoom 0.8 yalign 1.0
                                        bot"Now that I realize how I trully am..."
                                        show acrotchpov_bg at pov_jerkoffpullback(0.2):
                                            subpixel True zoom 0.8 yalign 1.0
                                        bot"I will do everything in my power to make... you..."
                                        show acrotchpov_bg at pov_jerkoffthrust():
                                            subpixel True zoom 0.8 yalign 1.0
                                        $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.3) 
                                        show afinal feet4 behind acrotchpov_bg with flash:
                                            zoom 0.6 xalign 1.0 yalign 1.0
                                        show acrotchpov_bg:
                                            easein 0.4 yoffset 70
                                        call changeHatred(1,"none") from _call_changeHatred_67
                                        bot"Mine!!"
                                        hide acrotchpov_bg with dissolve
                                        call decreaselust(50) from _call_decreaselust_52
                                        show halfblack with dissolve
                                        show boruto masturbating with dissolve:
                                            zoom 1.0 xalign 0.5 yalign 0.0
                                        show boruto blue 2 with Dissolve(1.5):
                                            zoom 1.0 xalign 0.5 yalign 0.0
                                    
                                        bot"Holy s-shit! I've let my self go entirely..."
                                        show boruto blue 1 with dissolve:
                                            zoom 1.0 xalign 0.5 yalign 0.0
                                        bot"I can't believe I plastered [hin_rel]'s feet with my spunk."
                                        call changeHatred(1,"none") from _call_changeHatred_68
                                        bot"But she deserved that and more, after what she's done!"
                                        bot"This strange feeling of satisfcation... I am not sure if it's because of climaxing all over [hin_rel], or if it's some deranged sense of accomplishment from violating her like this..."
                                        hide boruto blue 1
                                        hide halfblack
                                        with dissolve
                                        show afinal feet4 with dissolve:
                                            zoom 0.75 xalign 1.0 yalign 1.0 
                                        bot"[hin_rel]'s feet are practically bathing in a pool of my semen. This shit ain't drying off in a year... let alone by tomorrow."
                                        show afinal feet4 with dissolve:
                                            zoom 0.5
                                        bot"Fuck... Well, no point stressing about it now that the deed is done. I either wake up tomorrow a lucky man, or..."
                                        show afinal feet4 with dissolve:
                                            zoom 0.7 xalign 0.0 yalign 0.2
                                        bot"[hin_rel] kills me in my sleep, in which case I at least die a satisfied man!"
                                        jump secretsceneintroending


                                    "Don't":
                                        bot"Now that I discovered this intoxicating feeling of lust..."
                                        bot"Now that I realize how I truly am..."
                                        bot"I vow upon myself, to do everything in my power to make you mine."
                                        bot"But tonight, is not that night yet... I'd be risking too much."
                                        show halfblack with dissolve
                                        show boruto masturbating with dissolve:
                                            zoom 1.0 xalign 0.5 yalign 0.0
                                        show boruto blue 2 with Dissolve(1.5):
                                            zoom 1.0 xalign 0.5 yalign 0.0
                                        bot"I've let myself go..."
                                        bot"I can't believe I covered [hin_rel]'s feet with my... fluids."
                                        bot"But she had it coming... didn't she?"
                                        bot"She knows that I am suffering... and still she tried to shame me..."
                                        hide boruto blue 1
                                        hide halfblack
                                        with dissolve
                                        show afinal feet3 with dissolve:
                                            zoom 0.75 xalign 1.0 yalign 1.0 
                                        bot"[hin_rel]'s feet are covered in my semen. Will all that even dry off by tomorrow?"
                                        show afinal feet3 with dissolve:
                                            zoom 0.5
                                        bot"Fuck... Well, the deed is done. No point stressing about it after the fact. I either wake up tomorrow a lucky man, or..."
                                        show afinal feet3 with dissolve:
                                            zoom 0.7 xalign 0.0 yalign 0.2
                                        bot"[hin_rel] kills me in my sleep, in which case I at least die a satisfied man!"
                                        jump secretsceneintroending
                                    

                            label ihafinal_ass:
                                $ clickinfobutton = f"I'll have some fun with you {hin_rel}!" # text displayed when clicking info button

                                bot"How can I resist paying tribute to your ass..."
                                show acrotchpov_bg with dissolve:
                                    zoom 0.8 yalign 1.0
                                "You placed your kness on the edges of the mattress getting as close to [hin_name]'s ass as you could without disrupting her sleep and..."
                                
                                $ renpy.sound.play("/audio/soun_fx/jerkoff1.opus", channel="sfx2", loop=False, relative_volume = 0.2) 
                                show acrotchpov_bg at pov_jerkoff(0.2,5):
                                    subpixel True zoom 0.8 yalign 1.0
                                bot"I will c-cover your fat ass with my semen [hin_rel]!"
                                show acrotchpov_bg at pov_jerkoff(0.2,2):
                                    subpixel True zoom 0.8 yalign 1.0
                                bot"Take..."
                                show acrotchpov_bg at pov_jerkoffpullback(0.2):
                                    subpixel True zoom 0.8 yalign 1.0
                                bot"My..."
                                show acrotchpov_bg at pov_jerkoffthrust():
                                    subpixel True zoom 0.8 yalign 1.0
                                $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.3) 
                                show afinal ass1 behind acrotchpov_bg with flash:
                                    zoom 0.5 xalign 1.0 yalign 1.0
                                show acrotchpov_bg:
                                    easein 0.4 yoffset 40
                                bot"Seed!"
                                call decreaselust(20) from _call_decreaselust_53
                                bot"Your ass deserves much more than that!"
                                $ renpy.sound.play("/audio/soun_fx/jerkoff2.opus", channel="sfx2", loop=False, relative_volume = 0.2) 
                                show acrotchpov_bg at pov_jerkoff(0.2,5):
                                    subpixel True zoom 0.8 yalign 1.0
                                bot"I am nowhere near satisfied yet!"
                                show acrotchpov_bg at pov_jerkoffpullback(0.2):
                                    subpixel True zoom 0.8 yalign 1.0
                                bot"I have more in store f-for you!"
                                show acrotchpov_bg at pov_jerkoffthrust():
                                    subpixel True zoom 0.8 yalign 1.0
                                $ renpy.sound.play("/audio/soun_fx/cum2.opus", channel="sfx2", loop=False, relative_volume = 0.3) 
                                show afinal ass2 behind acrotchpov_bg with flash
                                show acrotchpov_bg:
                                    easein 0.4 yoffset 40
                                bot"Take this!"
                                show acrotchpov_bg at pov_jerkoffpullback(0.2):
                                    easein 0.3 subpixel True zoom 0.8 yalign 1.0
                                bot"And..."
                                $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                                show acrotchpov_bg at pov_jerkoffthrust():
                                    subpixel True zoom 0.8 yalign 1.0
                                show afinal ass3 behind acrotchpov_bg with flash
                                bot"This!"
                                show acrotchpov_bg:
                                    easein 0.3 yoffset 60
                                call decreaselust(40) from _call_decreaselust_54
                                $ renpy.sound.play("/audio/soun_fx/panting.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                                bo"*Panting*"
                                scene afinal ass3 with dissolve:
                                    zoom 0.6 xalign 0.5 yalign 0.5
                                bot"Fuck! W-what have I done... [hin_rel]'s ass is drenched in my cum. I even soiled her panties and legs..."
                                bot"Could all this semen even dry off by the morning?"
                                scene afinal ass3 with fade:
                                    zoom 0.5
                                bot"Look at you [hin_rel]..."
                                scene afinal ass3 with dissolve:
                                    zoom 0.8 xalign 0.6 yalign 0.5
                                show afinal ass3 with dissolve:
                                    easein 5 zoom 1 xalign 0.4 yalign 0.5
                                bot"Still so blissfuly unaware of the fact that you are covered in your [hin_rel_to_bo]'s cum. Looking at you like this..."
                                call increaselust(10) from _call_increaselust_61
                                bot"It excites me even more!"
                                scene afinal ass3 with fade:
                                    zoom 0.5
                                bot"Now I realize. All this time I've been mistaking the strong feelings I was having for you for something they were not [hin_rel]..."
                                bot"Those weren't feelings of love, at least not entirely..."
                                bot"What I truly felt was lust! Lust over you and your whore-like body!"
                                menu:
                                    bot"What I truly felt was lust! Lust over you and your whore-like body!"
                                    "{color=[hatredcolor]}Pay a final tribute!{/color}":
                                        show afinal ass3 with dissolve
                                        show acrotchpov_bg with dissolve:
                                            zoom 0.8 yalign 1.0
                                        bot"And my lust for you knows no bounds!"
                                        $ renpy.sound.play("/audio/soun_fx/jerkoff2.opus", channel="sfx2", loop=False, relative_volume = 0.2) 
                                        show acrotchpov_bg at pov_jerkoff(0.2,5):
                                            subpixel True zoom 0.8 yalign 1.0
                                        bot"Now that I discovered this intoxicating feeling of lust..."
                                        show acrotchpov_bg at pov_jerkoff(0.2,2):
                                            subpixel True zoom 0.8 yalign 1.0
                                        bot"Now that I realize how I trully am..."
                                        show acrotchpov_bg at pov_jerkoffpullback(0.2):
                                            subpixel True zoom 0.8 yalign 1.0
                                        bot"I will do everything in my power to make... you..."
                                        show acrotchpov_bg at pov_jerkoffthrust():
                                            subpixel True zoom 0.8 yalign 1.0
                                        $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.3) 
                                        show afinal ass4 behind acrotchpov_bg with flash
                                        show acrotchpov_bg:
                                            easein 0.4 yoffset 70
                                        bot"Mine!!"
                                        $ renpy.sound.play("/audio/soun_fx/jerkoff1.opus", channel="sfx2", loop=False, relative_volume = 0.2) 
                                        show acrotchpov_bg at pov_jerkoff(0.2,5):
                                            subpixel True zoom 0.8 yalign 1.0
                                        bot"*Moans*"
                                        show acrotchpov_bg at pov_jerkoff(0.2,2):
                                            subpixel True zoom 0.8 yalign 1.0
                                        bot"And goddamn it! I swear one day..."
                                        show acrotchpov_bg at pov_jerkoffpullback(0.2):
                                            subpixel True zoom 0.8 yalign 1.0
                                        call changeHatred(1,"none") from _call_changeHatred_69
                                        bot"My dick will be buried deep inside your holes, and all this semen won't be covering you..."
                                        show acrotchpov_bg at pov_jerkoffthrust():
                                            subpixel True zoom 0.8 yalign 1.0
                                        $ renpy.sound.play("/audio/soun_fx/cum11.opus", channel="sfx2", loop=False, relative_volume = 0.2) 
                                        show afinal ass5 behind acrotchpov_bg with flash
                                        show acrotchpov_bg:
                                            easein 0.4 yoffset 70
                                        bot"It will be deep inside your womb and your ass instead!"
                                        hide acrotchpov_bg with dissolve
                                        call decreaselust(50) from _call_decreaselust_55
                                        $ renpy.sound.play("/audio/soun_fx/panting.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                                        bot"*Panting*"
                                        show halfblack with dissolve
                                        show boruto masturbating with dissolve:
                                            zoom 1.0 xalign 0.5 yalign 0.0
                                        show boruto blue 2 with Dissolve(1.5):
                                            zoom 1.0 xalign 0.5 yalign 0.0
                                    
                                        bot"Holy s-shit! I've let my self go entirely..."
                                        show boruto blue 1 with dissolve:
                                            zoom 1.0 xalign 0.5 yalign 0.0
                                        bot"I can't believe I plastered [hin_rel]'s ass with my spunk."
                                        show boruto blue 2
                                        with dissolve
                                        call changeHatred(1,"none") from _call_changeHatred_70
                                        bot"But she deserved that and more, after what she's done!"
                                        bot"This strange feeling of satisfaction... I am not sure if it's because of climaxing all over [hin_rel], or if it's some deranged sense of accomplishment from violating her like this..."
                                        hide boruto blue 1
                                        hide halfblack
                                        with dissolve
                                        show afinal ass5 with dissolve:
                                            zoom 0.65 xalign 0.5 yalign 0.5
                                        bot"[hin_rel]'s ass is covered with my semen. It even dripped down to her thighs and  into the bed sheets... Fuck! This shit ain't drying off in a year... let alone by tomorrow."
                                        show afinal ass5 with dissolve:
                                            zoom 0.5
                                        bot"Well... no point stressing about it now that the the deed is done. I either wake up tomorrow a lucky man, or..."
                                        show afinal ass5 with dissolve:
                                            zoom 0.7 xalign 0.0 yalign 0.2
                                        bot"[hin_rel] kills me in my sleep, in which case I at least die a satisfied man!"
                                        jump secretsceneintroending


                                    "Don't":
                                        bot"Now that I discovered this intoxicating feeling of lust..."
                                        bot"Now that I realize how I truly am..."
                                        bot"I vow upon myself, to do everything in my power to make you mine."
                                        bot"But tonight, is not that night yet... I'd be risking too much."
                                        show halfblack with dissolve
                                        show boruto masturbating with dissolve:
                                            zoom 1.0 xalign 0.5 yalign 0.0
                                        show boruto blue 2 with Dissolve(1.5):
                                            zoom 1.0 xalign 0.5 yalign 0.0
                                        bot"I've let myself go..."
                                        bot"I can't believe I covered [hin_rel]'s ass with my... fluids."
                                        bot"But she had it coming... didn't she?"
                                        bot"She knows that I am suffering... and still she tried to shame me..."
                                        hide boruto blue 1
                                        hide halfblack
                                        with dissolve
                                        show afinal ass3 with dissolve:
                                            zoom 0.6 xalign 0.5 yalign 0.5
                                        bot"[hin_rel]'s ass is covered with my semen. Will all that even dry off by tomorrow?"
                                        show afinal ass3 with dissolve:
                                            zoom 0.5
                                        bot"Fuck... Well, the deed is done. No point stressing about it after the fact. I either wake up tomorrow a lucky man, or..."
                                        show afinal ass3 with dissolve:
                                            zoom 0.7 xalign 0.0 yalign 0.2
                                        bot"[hin_rel] kills me in my sleep, in which case I at least die a satisfied man!"
                                        jump secretsceneintroending

                      
                              
                                

                        
                "Approach from the front": 
                    $ clickinfobutton = f"I'll have some fun with you {hin_rel}!" # text displayed when clicking info button
                    show introhatredintro with dissolve:
                        zoom 0.6 xalign 0.0 yalign 0.5
                    bot"Easy does it..." 
                    scene black with vpunch
                    bo"O-oh..!" 
                    scene ihb0 with dissolve:
                        zoom 0.5
                    "[hin_name] shifted her posture as you approached..."
                    bot"[hin_rel]... you've got some of the greatest pair of tits I have ever laid my eyes on..."
                    bot"Would be a shame if I didn't take a better look..."
                    menu:
                        bot"Would be a shame if I didn't take a better look..."
                        "Try removing blanket":
                            pass
                    scene ihb1 with dissolve:
                        zoom 0.5
                    
                    bot"S-shit!" with vpunch
                    "[hin_name] shifted her posture yet again..."
                    bot"That spooked me off! Stay still for a second [hin_rel]... will you?"
                    "Explore the scene to find 'hotspot' zones. Green hotspots will advance the scene."
                    show screen sleep_ihb1
                    $ ui.interact()

                    label sleep_ihb1_head:
                        default sleep_ihb1_head_counter = 0
                        show ihb1 with dissolve:
                            zoom 0.7 xalign 0.0 yalign 1.0
                        if sleep_ihb1_head_counter > 0:
                            bot"Just you wait [hin_rel]... Perhaps I'll have a little something for your face as well tonight..."
                            jump sleep_ihb1_headend
                        bot"You thought I'd let you step all over me and try to guilt-trip me [hin_rel]?"
                        bot"Your pretty little innocent face won't stop me from punishing you..."
                        label sleep_ihb1_headend:
                            $ sleep_ihb1_head_counter+= 1
                            show ihb1 with dissolve:
                                zoom 0.5
                            show screen sleep_ihb1
                            $ ui.interact()

                    label sleep_ihb1_tits:
                        default sleep_ihb1_tits_counter = 0
                        show ihb1 with dissolve:
                            zoom 0.7 xalign 0.5 yalign 0.5
                        if sleep_ihb1_tits_counter > 0:
                            bot"I swear... one day I'll have my cock buried in between them!"
                            jump sleep_ihb1_titsend
                        bot"Those perfectly shaped tits of yours [hin_rel]... Your perky nipples are almost visible through your gown! It's as if your tits are screaming to be set free."
                        bot"Perhaps I should do just that..."
                        label sleep_ihb1_titsend:
                            $ sleep_ihb1_tits_counter+= 1
                            show ihb1 with dissolve:
                                zoom 0.5
                            show screen sleep_ihb1
                            $ ui.interact()

                    menu jumpfromsleep_ihb1:
                        bot"You wouldn't mind if I moved your blanket a little bit, would you [hin_rel]?"
                        "Attempt to remove blanket":
                            pass
                    show ihb2 with Dissolve(1.5):
                        zoom 0.5
                    bot"D-damn!" with vpunch
                    call increaselust(10) from _call_increaselust_62
                    bot"So... fucking... beautiful!"
                    bot"You stay right there looking pretty like that [hin_rel]..."
                    show screen sleep_ihb2
                    $ ui.interact()
                    

                    label sleep_ihb2_head:
                        default sleep_ihb2_head_counter = 0
                        show ihb2 with dissolve:
                            zoom 0.7 xalign 0.0 yalign 0.5
                        if sleep_ihb2_head_counter > 0:
                            bot"If only you knew what your own [hin_rel_to_bo] is planning for you! I bet you wouldn't be sleeping so peacefully... "
                            jump sleep_ihb2_headend
                        bot"All you had to do was show some compassion [hin_rel]. Instead, you put the blame on me... Now in turn, I will put something on you!"
                        label sleep_ihb2_headend:
                            $ sleep_ihb2_head_counter+= 1
                            show ihb2 with dissolve:
                                zoom 0.5
                            show screen sleep_ihb2
                            $ ui.interact()

                    label sleep_ihb2_tits:
                        default sleep_ihb2_tits_counter = 0
                        show ihb2 with dissolve:
                            zoom 0.7 xalign 0.5 yalign 0.5
                        if sleep_ihb2_tits_counter == 1:
                            bot"I am one step away from burying my face in there and licking the sweat straight from your tits... all the way down to your toned tummy [hin_rel]."
                        elif sleep_ihb2_tits_counter > 1:
                            bot"Fuck! It's too risky to try anything right now..."
                            jump sleep_ihb2_titsend
                        else:
                            bot"Your slutty little nipples are making me so horny [hin_rel]... It takes everything I have to hold myself back from ripping off your gown and fucking you on the spot"
                        label sleep_ihb2_titsend:
                            $ sleep_ihb2_tits_counter+= 1
                            show ihb2 with dissolve:
                                zoom 0.5
                            show screen sleep_ihb2
                            $ ui.interact()

                    label sleep_ihb2_fit:
                        default sleep_ihb2_fit_counter = 0
                        show ihb2 with dissolve:
                            zoom 0.7 xalign 0.8 yalign 0.8
                        if sleep_ihb2_fit_counter == 1:
                            bot"I cannnot fathom how a woman of your age can look so fucking hot. And I can't believe THAT woman happens to be my [hin_rel]... right in front of my very eyes!"
                            bot"The things I would do to you [hin_rel]... Soon enough, I'll have my chance!"
                        elif sleep_ihb2_fit_counter > 1:
                            bot"Tonight I have other plans for you..."
                            jump sleep_ihb2_fitend
                        else:
                            bot"Your toned stomach... your thick muscular thighs. Every part of you is making me salivate over your body [hin_rel]..."
                        label sleep_ihb2_fitend:
                            $ sleep_ihb2_fit_counter+= 1
                            show ihb2 with dissolve:
                                zoom 0.5
                            show screen sleep_ihb2
                            $ ui.interact()


                    
                    menu jumpfromsleep_ihb2:
                        bot"I need to see all of you, in all  your beautiful glory!"
                        "Remove blanket":
                            show ihb2 with dissolve:
                                zoom 0.65 xalign 1.0 yalign 0.5
                            bot"Now show me what you are hiding down there [hin_rel]!"
                            show ihbfinal with dissolve:
                                zoom 0.5
                            call increaselust(30) from _call_increaselust_63
                            bot"Fucking hell...."
                            bot"How am I supposed to do anything but fantasize about you when you look like that [hin_rel]..."
                            bot"Is this what [na_rel] woke up to every day? To think he'd leave you alone like this... what an idiot!"
                            bot"No matter... I'll be taking care of you now, [hin_rel]!"
                            show ihbfinal with dissolve:
                                zoom 0.7 xalign 0.0 yalign 0.5
                            bot"Your perfectly shaped tits along with your fit protruding navel..."
                            show ihbfinal with dissolve:
                                zoom 0.7 xalign 1.0 yalign 1.0
                            bot"...or, your sexy long legs and your cute little feet."
                            bot"I can't decide which part of you is more worthy of my 'attention'"
                            show ihbfinal with dissolve:
                                zoom 0.5
                            bot"Just looking at you has me rock hard [hin_rel]. But..."
                            bot"Who the fuck can blame me when your body was sculpted in an image of a freaking sex goddess..."
                            bot"It's like every part of you was made to be worshipped. And I will do just that!"
                            "Explore the scene to find 'hotspot' zones. Green hotspots will advance the scene."
                            show screen sleep_ihbfinal with dissolve
                            $ ui.interact()


                            label ihbfinal_head:
                                default sleep_ihbfinal_counter = 0
                                show ihbfinal with dissolve:
                                    zoom 0.7 xalign 0.0 yalign 0.1
                                if sleep_ihbfinal_counter > 0:
                                    bot"It's time I have my revenge on you!"
                                    jump ihbfinal_headEND
                                bot"I've endured enough [hin_rel]. Tonight, you are mine to do with as I please!"
                                label ihbfinal_headEND:
                                    $ sleep_ihbfinal_counter+= 1
                                    show ihbfinal with dissolve:
                                        zoom 0.5
                                    show screen sleep_ihbfinal
                                    $ ui.interact()
                            
                            label ihbfinal_upper:
                                show ihbfinal with dissolve:
                                    zoom 0.7 xalign 0.0 yalign 0.5
                                bot"There's no way I could ever resist those tits of yours!"
                                show ihbfinal with dissolve:
                                    zoom 0.5
                                show bcrotchpov with dissolve:
                                    zoom 0.8 yalign 1.0 xpos -0.26
                                "You placed your kness on the edges of the mattress, getting as close to [hin_name]'s body as you could without disrupting her sleep and..."
                                bot"Of course I would pay tribute to your tits..."
                                $ renpy.sound.play("/audio/soun_fx/jerkoff1.opus", channel="sfx2", loop=False, relative_volume = 0.2) 
                                show bcrotchpov at pov_jerkoff(0.2,5):
                                    subpixel True zoom 0.8 yalign 1.0
                                bot"I will c-cover your body in my semen [hin_rel]!"
                                show bcrotchpov at pov_jerkoff(0.2,2):
                                    subpixel True zoom 0.8 yalign 1.0
                                bot"Take..."
                                show bcrotchpov at pov_jerkoffpullback(0.2):
                                    subpixel True zoom 0.8 yalign 1.0
                                bot"My..."
                                show bcrotchpov at pov_jerkoffthrust():
                                    subpixel True zoom 0.8 yalign 1.0
                                $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.3) 
                                show bfinal upper1 behind bcrotchpov with flash:
                                    zoom 0.5
                                show bcrotchpov:
                                    easein 0.4 yoffset 40
                                bot"Seed!"
                                $ renpy.sound.play("/audio/soun_fx/jerkoff1.opus", channel="sfx2", loop=False, relative_volume = 0.2) 
                                show bcrotchpov at pov_jerkoffpullback(0.2):
                                    easein 0.5 subpixel True zoom 0.8 yalign 1.0  xpos -0.30
                                bo"*Moans*"
                                show bcrotchpov at pov_jerkoffthrust():
                                    easein 0.3 yoffset 0
                                $ renpy.sound.play("/audio/soun_fx/cum2.opus", channel="sfx2", loop=False, relative_volume = 0.3) 
                                show bfinal upper2 behind bcrotchpov with flash:
                                    zoom 0.5
                            
                                call decreaselust(20) from _call_decreaselust_56
                                scene bfinal upper2 with dissolve:
                                    zoom 0.7 xalign 0.0 yalign 0.5
                                bot"Now that's a pretty sight [hin_rel]... Your sexy stomach and tits covered in my spunk!"
                                show bfinal upper2:
                                    zoom 0.5
                                show bcrotchpov:
                                    zoom 0.8 yalign 1.0 xpos -0.26
                                with dissolve
                                $ renpy.sound.play("/audio/soun_fx/jerkoff2.opus", channel="sfx2", loop=False, relative_volume = 0.2) 
                                show bcrotchpov at pov_jerkoff(0.2,5):
                                    subpixel True zoom 0.8 yalign 1.0
                                bot"But I am nowhere near satisfied yet!"
                                show bcrotchpov at pov_jerkoffpullback(0.2):
                                    subpixel True zoom 0.8 yalign 1.0
                                bot"I have more in store f-for you!"
                                show bcrotchpov at pov_jerkoffthrust():
                                    subpixel True zoom 0.8 yalign 1.0
                                $ renpy.sound.play("/audio/soun_fx/cum2.opus", channel="sfx2", loop=False, relative_volume = 0.3) 
                                show bfinal upper3 behind bcrotchpov with flash:
                                    zoom 0.5
                                show bcrotchpov:
                                    easein 0.4 yoffset 40
                                bot"Take this...!"
                                show bcrotchpov at pov_jerkoffpullback(0.2):
                                    easein 0.3 subpixel True zoom 0.8 yalign 1.0 xoffset -130
                                bot"And..."
                                show bcrotchpov at pov_jerkoffthrust():
                                    easein 0.2 subpixel True zoom 0.8 ypos 0.95
                                pause 0.5
                                $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                                show bfinal upper3 behind bcrotchpov with flash:
                                    zoom 0.5 xalign 1.0 yalign 1.0
                                
                                bot"And t-this!"
                                
                                call decreaselust(40) from _call_decreaselust_57
                                $ renpy.sound.play("/audio/soun_fx/panting.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                                bo"*Panting*"
                                bot"Fuck! W-what have I done... [hin_rel]'s body is drenched in my cum. There is an entire pool of my semen lying between her breasts!"
                                bot"Could all this semen even dry off by the morning?"
                                scene bfinal upper3 with fade:
                                    zoom 0.5
                                bot"Look at you [hin_rel]..."
                                scene bfinal upper3 with dissolve:
                                    zoom 0.7 xalign 0.7 yalign 0.7
                                show bfinal upper3 with dissolve:
                                    easein 5 zoom 0.8 xalign 0.0 yalign 0.4
                                bot"Still so blissfuly unaware of the fact that you are covered in your [hin_rel_to_bo]'s cum. Looking at you like this..."
                                call increaselust(10) from _call_increaselust_64
                                bot"It excites me even more!"
                                scene bfinal upper3 with fade:
                                    zoom 0.5
                                bot"Now I realize. All this time I've been mistaking the strong feelings I was having for you for something they were not [hin_rel]..."
                                bot"Those weren't feelings of love, at least not entirely..."
                                bot"What I truly felt was lust! Lust over you and your whore-like body!"
                                menu:
                                    bot"What I truly felt was lust! Lust over you and your whore-like body!"
                                    "{color=[hatredcolor]}Pay a final tribute!{/color}":
                                        show bfinal upper3 with dissolve:
                                            zoom 0.5 xalign 1.0 yalign 1.0
                                        show bcrotchpov with dissolve:
                                            zoom 0.8 yalign 1.0 xpos -0.26
                                        bot"And my lust for you knows no bounds!"
                                        $ renpy.sound.play("/audio/soun_fx/jerkoff2.opus", channel="sfx2", loop=False, relative_volume = 0.2) 
                                        show bcrotchpov at pov_jerkoff(0.2,5):
                                            subpixel True zoom 0.8 yalign 1.0
                                        bot"Now that I discovered this intoxicating feeling of lust..."
                                        show bcrotchpov at pov_jerkoff(0.2,2):
                                            subpixel True zoom 0.8 yalign 1.0
                                        bot"Now that I realize how I trully am..."
                                        show bcrotchpov at pov_jerkoffpullback(0.2):
                                            subpixel True zoom 0.8 yalign 1.0
                                        bot"I will do everything in my power to make... you..."
                                        show bcrotchpov at pov_jerkoffthrust():
                                            subpixel True zoom 0.8 yalign 1.0
                                        $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.3) 
                                        show bfinal upper4 behind bcrotchpov with flash:
                                            zoom 0.5 xalign 1.0 yalign 1.0
                                        show bcrotchpov:
                                            easein 0.4 yoffset 70
                                        call changeHatred(1,"none") from _call_changeHatred_71
                                        bot"Mine!!"
                                        show bcrotchpov at pov_jerkoffpullback(0.2):
                                            easein 0.6 subpixel True zoom 0.8 yalign 1.0 xoffset -260
                                        bot"I can't resist it anymore... Y-your face deserves a little s-something too!"
                                        show bcrotchpov at pov_jerkoffthrust():
                                            easein 0.3 subpixel True zoom 0.8 ypos 0.91
                                        pause 0.5
                                        $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                                        show bfinal upper5 behind bcrotchpov with longerflash:
                                            zoom 0.5 xalign 1.0 yalign 1.0
                                        
                                        bo"*Moans*!"
                                        call decreaselust(50) from _call_decreaselust_58
                                        show bfinal upper5 with dissolve:
                                            zoom 0.5
                                        bot"Holy shit, my semen is on her fucking face!"
                                        show bfinal upper6:
                                            zoom 0.7 xalign 0.0 yalign 0.2
                                        show bcrotchpov:
                                            zoom 0.85 ypos 1.05
                                        with dissolve
                                        hin"[na_name]..."
                                        hide bcrotchpov with dissolve
                                        scene bfinal upper6 with dissolve:
                                            zoom 0.5
                                        bot"Oh fuck oh fuck oh fuck!" with vpunch
                                        
                                        "Hearing [hin_name]'s voice, you quickly got off her bed looking to make your escape but..."
                                        bot"Please don't wake up! Not now [hin_rel]!"
                                        scene bfinal upper6 with dissolve:
                                            zoom 0.9 xalign 0.1 yalign 0.3
                                        hin"*Snores*... don't be s-so ~Shh-hhsh~ *Snores* S-so rough... [na_name]..."
                                        bot"F-fuck... She is just dreaming from the looks of it... Phew!"
                                        call changeHatred(1,"none") from _call_changeHatred_72
                                        scene bfinal upper6 with dissolve:
                                            zoom 0.5
                                        bot"Kinda funny to see her yearning to be fucked by [na_rel] when she is covered in my spunk!"
                                        bot"You know [hin_rel]... I could fuck you senseless in his stead. All you have to do is ask... Until then, I'll find more ways to violate you!"

                                        show halfblack with dissolve
                                        show boruto masturbating with dissolve:
                                            zoom 1.0 xalign 0.5 yalign 0.0
                                        show boruto blue 2 with Dissolve(1.5):
                                            zoom 1.0 xalign 0.5 yalign 0.0
                                    
                                        bot"But fuck me... I've let my self go entirely!"
                                        show boruto blue 1 with dissolve:
                                            zoom 1.0 xalign 0.5 yalign 0.0
                                        bot"I can't believe I plastered [hin_rel]'s body and face with my spunk."
                                        call changeHatred(1,"none") from _call_changeHatred_73
                                        show boruto blue 2 with dissolve
                                        bot"But she deserved that and more, after what she's done!"
                                        bot"This strange feeling of satisfcation... I am not sure if it's because of climaxing all over [hin_rel], or if it's some deranged sense of accomplishment from violating her like this..."
                                        hide boruto blue 1
                                        hide halfblack
                                        with dissolve
                                        show bfinal upper6 with dissolve:
                                            zoom 0.7 xalign 0.8 yalign 0.5
                                        show bfinal upper6:
                                            easein 3 xalign 0.2 yalign 0.5
                                        bot"[hin_rel]'s upper body is practically bathing in a pool of my semen. This shit ain't drying off in a year... let alone by tomorrow."
                                        show bfinal upper6 with dissolve:
                                            zoom 0.5
                                        bot"Fuck... Well, no point stressing about it now that the deed is done. I either wake up tomorrow a lucky man, or..."
                                        show bfinal upper6 with dissolve:
                                            zoom 0.7 xalign 0.0 yalign 0.2
                                        bot"[hin_rel] kills me in my sleep, in which case I at least die a satisfied man!"
                                        jump secretsceneintroending


                                    "Don't":
                                        bot"Now that I discovered this intoxicating feeling of lust..."
                                        bot"Now that I realize how I truly am..."
                                        bot"I vow upon myself, to do everything in my power to make you mine."
                                        bot"But tonight, is not that night yet... I'd be risking too much."
                                        show halfblack with dissolve
                                        show boruto masturbating with dissolve:
                                            zoom 1.0 xalign 0.5 yalign 0.0
                                        show boruto blue 2 with Dissolve(1.5):
                                            zoom 1.0 xalign 0.5 yalign 0.0
                                        bot"I've let myself go..."
                                        bot"I can't believe I covered [hin_rel]'s tits with my... fluids."
                                        bot"But she had it coming... didn't she?"
                                        bot"She knows that I am suffering... and still she tried to shame me..."
                                        hide boruto blue 1
                                        hide halfblack
                                        with dissolve
                                        show bfinal upper3 with dissolve:
                                            zoom 0.7 xalign 0.2 yalign 0.5 
                                        bot"[hin_rel]'s body is covered in my semen. Will all that even dry off by tomorrow?"
                                        show bfinal upper3 with dissolve:
                                            zoom 0.5
                                        bot"Fuck... Well, the deed is done. No point stressing about it after the fact. I either wake up tomorrow a lucky man, or..."
                                        show bfinal upper3 with dissolve:
                                            zoom 0.7 xalign 0.0 yalign 0.2
                                        bot"[hin_rel] kills me in my sleep, in which case I at least die a satisfied man!"
                                        jump secretsceneintroending
                                    

                            label ihbfinal_lower:
                                show ihbfinal with dissolve:
                                    zoom 0.65 xalign 1.0 yalign 0.95
                                bot"There's no way I could ever resist your sexy legs and feet..."
                                show ihbfinal with dissolve:
                                    zoom 0.5
                                show bcrotchpov with dissolve:
                                    zoom 0.8 yalign 1.0 xpos 0.05
                                "You placed your kness on the edges of the mattress, getting as close to [hin_name]'s body as you could without disrupting her sleep and..."
                                
                                $ renpy.sound.play("/audio/soun_fx/jerkoff1.opus", channel="sfx2", loop=False, relative_volume = 0.2) 
                                show bcrotchpov at pov_jerkoff(0.2,5):
                                    subpixel True zoom 0.8 yalign 1.0
                                bot"Your well trained legs are probably bigger than mine and yet... they are just so damn perfect."
                                show bcrotchpov at pov_jerkoff(0.2,2):
                                    subpixel True zoom 0.8 yalign 1.0
                                bot"I will c-cover them in my semen [hin_rel]!"
                                show bcrotchpov at pov_jerkoff(0.2,2):
                                    subpixel True zoom 0.8 yalign 1.0
                                bot"Take..."
                                show bcrotchpov at pov_jerkoffpullback(0.2):
                                    subpixel True zoom 0.8 yalign 1.0
                                bot"My..."
                                show bcrotchpov at pov_jerkoffthrust():
                                    subpixel True zoom 0.8 yalign 1.0
                                $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.3) 
                                show bfinal lower1 behind bcrotchpov with flash:
                                    zoom 0.5
                                show bcrotchpov:
                                    easein 0.4 yoffset 40
                                bot"Seed!"
                                $ renpy.sound.play("/audio/soun_fx/jerkoff1.opus", channel="sfx2", loop=False, relative_volume = 0.2) 
                                show bcrotchpov at pov_jerkoffpullback(0.2):
                                    easein 0.5 subpixel True zoom 0.8 yalign 1.0
                                bo"*Moans*"
                                show bcrotchpov at pov_jerkoffthrust():
                                    easein 0.3 yoffset 0
                                $ renpy.sound.play("/audio/soun_fx/cum2.opus", channel="sfx2", loop=False, relative_volume = 0.3) 
                                show bfinal lower2 behind bcrotchpov with flash:
                                    zoom 0.5
                            
                                call decreaselust(20) from _call_decreaselust_59
                                bot"Now that's a pretty sight [hin_rel]... Your sexy thighs covered in my spunk..."
                                $ renpy.sound.play("/audio/soun_fx/jerkoff2.opus", channel="sfx2", loop=False, relative_volume = 0.2) 
                                show bcrotchpov at pov_jerkoff(0.2,5):
                                    linear 1 subpixel True zoom 0.8 yalign 0.8 xpos +0.15 
                                bot"But I am nowhere near satisfied yet!"
                                show bcrotchpov at pov_jerkoffpullback(0.2):
                                    subpixel True zoom 0.8
                                bot"I have more in store f-for you!"
                                show bcrotchpov at pov_jerkoffthrust():
                                    subpixel True zoom 0.8
                                $ renpy.sound.play("/audio/soun_fx/cum2.opus", channel="sfx2", loop=False, relative_volume = 0.3) 
                                show bfinal lower3 behind bcrotchpov with flash:
                                    zoom 0.5
                                show bcrotchpov:
                                    easein 0.4 yoffset 40
                                bot"Take this...!"
                                show bcrotchpov at pov_jerkoffpullback(0.2):
                                    easein 0.3 subpixel True zoom 0.8 yalign 1.0 xoffset -130
                                bot"And..."
                                show bcrotchpov at pov_jerkoffthrust():
                                    easein 0.2 subpixel True zoom 0.8 ypos 0.95
                                pause 0.5
                                $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                                show bfinal lower4 behind bcrotchpov with flash:
                                    zoom 0.5 xalign 1.0 yalign 1.0 
                                bot"And t-this!"
                                show bcrotchpov at pov_jerkoffpullback(0.2):
                                    easein 0.8 subpixel True zoom 0.8 yalign 0.6 xoffset 170
                                bot"Let's not forget your feet!"
                                show bcrotchpov at pov_jerkoffthrust():
                                    easein 0.5 subpixel True zoom 0.8 yalign 0.7
                                
                                pause 0.5
                                
                                $ renpy.sound.play("/audio/soun_fx/cum5.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                                with longerflash
                                show bcrotchpov:
                                    easein 5 subpixel True zoom 0.8 ypos 1.0
                                call decreaselust(40) from _call_decreaselust_60
                                $ renpy.sound.play("/audio/soun_fx/panting.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                                
                                bo"*Panting*"
                                bot"Fuck! W-what have I done... [hin_rel]'s legs are drenched in my cum!"
                                bot"Can all this... fluid even dry off by the morning?"
                                scene bfinal lower4 with dissolve:
                                    zoom 0.7 xalign 1.0 yalign 1.0
                                bot"Look at you [hin_rel]..."
                                scene bfinal lower4 with dissolve:
                                    zoom 0.8 xalign 1.0 yalign 1.0
                                show bfinal lower4 with dissolve:
                                    easein 5 zoom 0.7 xalign 0.0 yalign 0.2
                                bot"Still so blissfuly unaware of the fact that you are covered in your [hin_rel_to_bo]'s cum. Looking at you like this..."
                                call increaselust(10) from _call_increaselust_65
                                bot"It excites me even more!"
                                scene bfinal lower4 with fade:
                                    zoom 0.5
                                bot"Now I realize. All this time I've been mistaking the strong feelings I was having for you for something they were not [hin_rel]..."
                                bot"Those weren't feelings of love, at least not entirely..."
                                bot"What I truly felt was lust! Lust over you and your whore-like body!"
                                menu:
                                    bot"What I truly felt was lust! Lust over you and your whore-like body!"
                                    "{color=[hatredcolor]}Pay a final tribute!{/color}":
                                        show bfinal lower4 with dissolve:
                                            zoom 0.5 xalign 1.0 yalign 1.0
                                        show bcrotchpov with dissolve:
                                            zoom 0.8 yalign 1.0 xpos 0.05
                                        bot"And my lust for you knows no bounds!"
                                        $ renpy.sound.play("/audio/soun_fx/jerkoff2.opus", channel="sfx2", loop=False, relative_volume = 0.2) 
                                        show bcrotchpov at pov_jerkoff(0.2,5):
                                            subpixel True zoom 0.8 yalign 1.0
                                        bot"Now that I discovered this intoxicating feeling of lust..."
                                        show bcrotchpov at pov_jerkoff(0.2,2):
                                            subpixel True zoom 0.8 yalign 1.0
                                        bot"Now that I realize how I trully am..."
                                        show bcrotchpov at pov_jerkoffpullback(0.2):
                                            subpixel True zoom 0.8 yalign 1.0
                                        bot"I will do everything in my power to make... you..."
                                        show bcrotchpov at pov_jerkoffthrust():
                                            subpixel True zoom 0.8 yalign 1.0
                                        $ renpy.sound.play("/audio/soun_fx/cum4.opus", channel="sfx2", loop=False, relative_volume = 0.3) 
                                        show bfinal lower5 behind bcrotchpov with flash:
                                            zoom 0.5 xalign 1.0 yalign 1.0
                                        show bcrotchpov:
                                            easein 0.4 yoffset 70
                                        call changeHatred(1,"none") from _call_changeHatred_74
                                        bot"Mine!!"
                                        show bcrotchpov at pov_jerkoffpullback(0.2):
                                            easein 0.6 subpixel True zoom 0.8 yalign 1.0 xoffset 180
                                        bo"*Moans*"
                                        show bcrotchpov at pov_jerkoffthrust():
                                            easein 0.3 subpixel True zoom 0.8 ypos 0.91
                                        pause 0.5
                                        $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                                        show bfinal lower6 behind bcrotchpov with longerflash:
                                            zoom 0.5 xalign 1.0 yalign 1.0
                                        show bcrotchpov:
                                            easein 5 subpixel True zoom 0.8 ypos 1.30
                                        call decreaselust(50) from _call_decreaselust_61
                                        show bfinal lower6 with dissolve:
                                            zoom 0.5
                                        $ renpy.sound.play("/audio/soun_fx/panting.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                                        bot"*Panting*"
                                        show bfinal lower6:
                                            zoom 0.7 xalign 1.0 yalign 1.0
                                        hide bcrotchpov
                                        with dissolve
                                        bot"Unreal... [hin_rel]'s feet are absolutely soaked in my spunk!"
                                        scene bfinal lower6 with dissolve:
                                            zoom 0.5
                                       

                                        show halfblack with dissolve
                                        show boruto masturbating with dissolve:
                                            zoom 1.0 xalign 0.5 yalign 0.0
                                        show boruto blue 2 with Dissolve(1.5):
                                            zoom 1.0 xalign 0.5 yalign 0.0
                                    
                                        bot"But fuck me... I've let my self go entirely!"
                                        show boruto blue 1 with dissolve:
                                            zoom 1.0 xalign 0.5 yalign 0.0
                                        bot"I can't believe I plastered [hin_rel]'s legs with my spunk."
                                        call changeHatred(1,"none") from _call_changeHatred_75
                                        show boruto blue 2 with dissolve
                                        bot"But she deserved that and more, after what she's done!"
                                        bot"This strange feeling of satisfcation... I am not sure if it's because of climaxing all over [hin_rel], or if it's some deranged sense of accomplishment from violating her like this..."
                                        hide boruto blue 1
                                        hide halfblack
                                        with dissolve
                                        show bfinal lower6 with dissolve:
                                            zoom 0.7 xalign 0.0 yalign 00
                                        show bfinal lower6:
                                            easein 4 xalign 1.0 yalign 1.0
                                        bot"[hin_rel]'s legs are soaked to the brim... This shit ain't drying off in a year... let alone by tomorrow."
                                        show bfinal lower6 with dissolve:
                                            zoom 0.5
                                        bot"Fuck... Well, no point stressing about it now that the deed is done. I either wake up tomorrow a lucky man, or..."
                                        show bfinal lower6 with dissolve:
                                            zoom 0.7 xalign 0.0 yalign 0.2
                                        bot"[hin_rel] kills me in my sleep, in which case I at least die a satisfied man!"
                                        jump secretsceneintroending


                                    "Don't":
                                        bot"Now that I discovered this intoxicating feeling of lust..."
                                        bot"Now that I realize how I truly am..."
                                        bot"I vow upon myself, to do everything in my power to make you mine."
                                        bot"But tonight, is not that night yet... I'd be risking too much."
                                        show halfblack with dissolve
                                        show boruto masturbating with dissolve:
                                            zoom 1.0 xalign 0.5 yalign 0.0
                                        show boruto blue 2 with Dissolve(1.5):
                                            zoom 1.0 xalign 0.5 yalign 0.0
                                        bot"I've let myself go..."
                                        bot"I can't believe I covered [hin_rel]'s legs with my... fluids."
                                        bot"But she had it coming... didn't she?"
                                        bot"She knows that I am suffering... and still she tried to shame me..."
                                        hide boruto blue 1
                                        hide halfblack
                                        with dissolve
                                        show bfinal lower4 with dissolve:
                                            zoom 0.7 xalign 1.0 yalign 1.0
                                        bot"[hin_rel]'s lower body is covered in my semen. Will all that even dry off by tomorrow?"
                                        show bfinal lower4 with dissolve:
                                            zoom 0.5
                                        bot"Fuck... Well, the deed is done. No point stressing about it after the fact. I either wake up tomorrow a lucky man, or..."
                                        show bfinal lower4 with dissolve:
                                            zoom 0.7 xalign 0.0 yalign 0.2
                                        bot"[hin_rel] kills me in my sleep, in which case I at least die a satisfied man!"
                                        jump secretsceneintroending
                        
                         
                    
                        
                
            














            label secretsceneintroending:
                scene black with dissolve
                $ renpy.end_replay()
                $ notification (f"{hin_name} Hatred objective completed")
                $ quest_hin.check("hin1H_5", "done")
                $ renpy.sound.play("/audio/soun_fx/doorclose.opus", channel="sfx2", loop=False, relative_volume = 0.6) 
                bot"I should try to get some sleep..."
                $ completed_intro += 1
                if completed_intro == 4:
                    $ completed_intro += 1
                    scene black with dissolve
                    $ day_part +=1
                    jump action_taken  #hacky way to fix time/day text disp;lay

           








            
                
    