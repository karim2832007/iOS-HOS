default ramennightscenescounter = 0
default yoru_replayscenes = False #variable to pass and reset on chosen scene to replay
default yoru_viewallscenes = False #used after viewing all scenes for replay funcitonality

label ramennightscenes:
    if ramennightscenescounter >=2:
        bot"Same shit as last time it seems..."
        bot"Do I really want to spy on them again?"
        menu:
            bot"Do I really want to spy on them again?"
            "Yes" if yoru_viewallscenes != True:
                bot"I am sick in the head..."
                "a"
                jump yoru_replay_nightscene2

            "Replay Scene 1" if yoru_viewallscenes == True:
                bot"I am sick in the head..."
                $ yoru_replayscenes = True
                jump yoru_replay_nightscene1

            "Replay Scene 2" if yoru_viewallscenes == True:
                bot"I am sick in the head..."
                $ yoru_replayscenes = True
                jump yoru_replay_nightscene2

            "Exit the building":
                bot"I am not watching that shit again..."
                scene black with dissolve
                "You exit the building and make your way home..."
                jump action_taken
            
    elif ramennightscenescounter == 1:
        $ ramennightscenescounter =2
        label yoru_replay_nightscene2:
        $ initialize_replay_defaults()
        $ yoru_viewallscenes = True
        "You lean against the wall and take a peek inside the studio-like room..."
        $ renpy.sound.play("/audio/soun_fx/sexslaps1.opus", channel="sfx2", loop=False, relative_volume = 1)
        $ renpy.sound.play("/audio/soun_fx/handjob4.opus", channel="sfx3", loop=False, relative_volume = 1)
        show screen ramen_peaking("ramen_nightscene2_1")
        show screen peaking_overlayramen
        with Dissolve(1)
        obo"How's this you whore!" with vpunch
        $ renpy.sound.play("/audio/soun_fx/gruntwoman1.opus", channel="sfx1", loop=False, relative_volume = 1)
        obo"Are you looking at the camera like I told you to?"
        bot"Crazy bastard. Is he really filming this shit... But what for?"
        hide screen ramen_peaking
        hide screen peaking_overlayramen
        scene black
        with dissolve
        yo"Y-yes O-obo, so p-please..."
        yo"Go easy on me..."
        obo"...E-Easy?"
        $ renpy.sound.play("/audio/soun_fx/sexslaps1.opus", channel="sfx2", loop=False, relative_volume = 1)
        $ renpy.sound.play("/audio/soun_fx/handjob4.opus", channel="sfx3", loop=False, relative_volume = 1)
        show screen ramen_peaking("ramen_nightscene2_anim1")
        show screen peaking_overlayramen with vpunch
        $ renpy.sound.play("/audio/soun_fx/gruntwoman3.opus", channel="sfx1", loop=False, relative_volume = 1)
        obo"The entire point of this film is for everyone to see the despair in your eyes as I fill your defiled pussy with my cum!" with vpunch
        obo"Don't you understand, Yoru? Everyone in this god-forsaken village hates you. For what you are..."
        obo"For how you look! So no, there's no going easy for you!"
        show screen ramen_peaking("ramen_nightscene2_3") with Dissolve(1)
        bot"Yoru told me before that people hated her for her resemblance to the people of Kumogakure... But, hated for what she is? What did Obo mean by that..."
        bot"What could Yoru be that warrants such treatment... I must be missing something here."
        obo"You will look straight into the lens while I break you down to what you really are."
        show screen ramen_peaking("ramen_nightscene2_2") with dissolve
        obo"My very own..."
        $ renpy.sound.play("/audio/soun_fx/pushitin1.opus", channel="sfx2", loop=False, relative_volume = 1)
        $ renpy.sound.play("/audio/soun_fx/gruntwoman2.opus", channel="sfx1", loop=False, relative_volume = 1)
        show screen ramen_peaking("ramen_nightscene2_3") with vpunch
        obo"Personal!"
        show screen ramen_peaking("ramen_nightscene2_2") with Dissolve(1)
        $ renpy.sound.play("/audio/soun_fx/pushitin1.opus", channel="sfx2", loop=False, relative_volume = 1)
        $ renpy.sound.play("/audio/soun_fx/mon_after_hit.opus", channel="sfx1", loop=False, relative_volume = 1)
        show screen ramen_peaking("ramen_nightscene2_4") with vpunch
        obo"Cum-dump!"
        show screen ramen_peaking("nightscene2_anim1") with dissolve
        $ renpy.sound.play("/audio/soun_fx/sexslaps1.opus", channel="sfx2", loop=False, relative_volume = 1)
        obo"People pay good money to see you get fucked to the brink of unconsciousness..."
        bot"... So that's why."
        obo"And that's exactly what we are doing tonight!" with vpunch
        obo"So sit there like the cum-slut that you are, and allow me to empty my balls inside of you!"
        $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx2", loop=False, relative_volume = 0.7)
        show screen ramen_peaking("ramen_nightscene2_4") with flash
        $ renpy.sound.play("/audio/soun_fx/cum2.opus", channel="sfx3", loop=False, relative_volume = 0.7)
        obo"F-fffuck!" with flash
        $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.7)
        show screen ramen_peaking("ramen_nightscene2_2") with longerflash
        obo"Your kind is truly special Yoru..."
        obo"For your pussies to be able to withstand the pounding of a thousand armies..."
        obo"And still be as tight as they are! Truly a gift to be savored..."
        hide screen ramen_peaking
        hide screen peaking_overlayramen
        with dissolve
        obo"Would be a shame to not abuse that, wouldn't it?"
        yo"N-no..."
        obo"You told me before that you are infertile..."
        yo"I... am..."
        obo"What if I told you..."
        $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.7)
        show screen ramen_peaking("ramen_nightscene2_5")
        show screen peaking_overlayramen with vpunch
        $ renpy.sound.play("/audio/soun_fx/gruntwoman2.opus", channel="sfx3", loop=False, relative_volume = 1)
        $ renpy.sound.play("/audio/soun_fx/pushitin2.opus", channel="sfx1", loop=False, relative_volume = 1)
        obo"I don't believe that for a second!"

        show screen ramen_peaking("nightscene2_anim2") with dissolve
        $ renpy.sound.play("/audio/soun_fx/sexslaps2.opus", channel="sfx2", loop=False, relative_volume = 1)
        $ renpy.sound.play("/audio/soun_fx/handjob4.opus", channel="sfx3", loop=False, relative_volume = 1)
        obo"Which is why I'll fill your womb up to the brim twice, no..."
        obo"Thrice!" with vpunch
        obo"Every single night I'll be filling you up until I see your belly balooning with my offspring..."
        obo"Imagine the child's power, fathered by me..."
        $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.7)
        $ renpy.sound.play("/audio/soun_fx/gruntwoman1.opus", channel="sfx3", loop=False, relative_volume = 1)
        show screen ramen_peaking("ramen_nightscene2_5")
        $ renpy.sound.play("/audio/soun_fx/ominous_sound.opus", channel="sfx1", loop=False, relative_volume = 1.5)
        obo"Mothered by a SHINIGAMI WHORE!" with vpunch
        bot"A... shinigami!?"
        show screen ramen_peaking("nightscene2_anim3")
        $ renpy.sound.play("/audio/soun_fx/sexslaps3.opus", channel="sfx2", loop=False, relative_volume = 1)
        $ renpy.sound.play("/audio/soun_fx/handjob4.opus", channel="sfx3", loop=False, relative_volume = 1)
        obo"Wouldn't that be a sight to behold!?" with vpunch
        obo"So open up your womb to me Yoru!"
        obo"Conceive for me!" with vpunch
        $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.7)
        obo"For that is your ultimate purpose you whore!" with flash
        $ renpy.sound.play("/audio/soun_fx/cum2.opus", channel="sfx2", loop=False, relative_volume = 0.7)
        obo"Carry!" with flash
        $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx2", loop=False, relative_volume = 0.7)
        obo"My!" with flash
        $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.7)
        show screen ramen_peaking("ramen_nightscene2_7") with longerflash
        obo"Offspring!"
        obo"Would you look at that..."
        obo"Your womb could not bear any more of my semen, it shot up your filthy ass..."
        $ renpy.sound.play("/audio/soun_fx/spank6.opus", channel="sfx2", loop=False, relative_volume = 1.2)
        hide screen ramen_peaking
        hide screen peaking_overlayramen
        scene black
        with flash
        obo"Shameful!"
        obo"But there's always another night for that..."
        show ramenshop upstairs with dissolve
        bot"What... the fuck?"
        bot"I need to get out of here first!"
        scene black with dissolve
        "You quietly but swiftly make your way outside the building..."
        $ renpy.end_replay()
        if yoru_replayscenes == True:
            $ yoru_replayscenes = False
            jump action_taken
        show bg ramenshop night with dissolve
        show boruto surprised3 with dissolve
        bot"Yoru... A shinigami!?" with vpunch
        show boruto suspicious with dissolve
        bot"I've heard of them before. Regarded as some sort of deity in tales of old..."
        bot"Convoys of Death, capable of possesing a person's soul and leading them to their demise. Supposedely at least..."
        bot"I thought shinigamis existed only in children's fairy tales."
        bot"...A machination of people's minds to serve as cautionary tales--But to think they actually exist!?"
        bot"And that Yoru might be one. How's that possible!?"
        $ notification ("Quest updated")
        $ quest.check("job_4", "completed")
        $ quest.check("job_5", "in progress")
        bot"Her? A god of death? She sure as shit doesn't seem like one to me..."
        bot"What the hell have I gotten myself involved in."
        scene black with dissolve
        bot"Fuck...! I'll sleep on it for now but I need to be careful! Lest I find myself dead in a fucking ditch somewhere around here..."
        bot"There might be more to Obo and Yoru than I realize."
        $ renpy.end_replay()
        jump action_taken


        
        





    elif ramennightscenescounter == 0:
        $ ramennightscenescounter =1
    label yoru_replay_nightscene1:
    $ initialize_replay_defaults()

    scene black with dissolve
    "You carefully approach the room and take a peek inside..."
    show screen ramen_peaking("ramen_nightscene1_1") 
    show screen peaking_overlayramen
    $ renpy.sound.play("/audio/soun_fx/bjsfx.opus", channel="sfx2", loop=False, relative_volume = 1)
    with Dissolve(1)
    $ renpy.sound.play("/audio/soun_fx/bj3.opus", channel="sfx3", loop=False, relative_volume = 1)
    obo"That's it bitch! Keep sucking on it..."
    call increaselust(10) from _call_increaselust_53
    "Move your cursor in any direction to get a better view."
    show expression FocusEffect("idle1", 640, 50, 125, 0.7) as focus_effect onlayer screens with dissolve
    "When present, you can use the button at the top of the screen to view CG without the peeking effect"
    hide focus_effect  onlayer screens with dissolve
    obo"Twirl that tongue of yours around my cock and clean it up!"
    $ renpy.sound.play("/audio/soun_fx/bjsfx.opus", channel="sfx2", loop=False, relative_volume = 1)
    $ renpy.sound.play("/audio/soun_fx/bj2.opus", channel="sfx3", loop=False, relative_volume = 1)
    yo"*Gluck* Slurp-mmgh *Gag*"
    bot"I've had a suspicion this is what Yoru meant when we talked..."
    $ renpy.sound.play("/audio/soun_fx/bjsfx.opus", channel="sfx2", loop=False, relative_volume = 1)
    bot"Obo's using Yoru for his pleasure, knowing full well her circumstances prohibit her from running away..."
    $ renpy.sound.play("/audio/soun_fx/bjsfx.opus", channel="sfx2", loop=False, relative_volume = 1)
    $ renpy.sound.play("/audio/soun_fx/bj1.opus", channel="sfx3", loop=False, relative_volume = 1)
    obo"Keep on sucking bitch! All the way to the base..." with vpunch
    bot"Dirty old man... He's so rough with her."
    bot"Does she really have to put up with... this?"
    "Click twice to continue..."
    $ ui.interact()
    hide screen ramen_peaking
    hide screen peaking_overlayramen
    scene black with vpunch
    $ renpy.sound.play("/audio/soun_fx/smashtable.opus", channel="sfx3", loop=False, relative_volume = 0.7)
    $ renpy.sound.play("/audio/soun_fx/gruntwoman2.opus", channel="sfx2", loop=False, relative_volume = 1.2)
    obo"Come over here you whore!"
    $ renpy.sound.play("/audio/soun_fx/gaspforair3.opus", channel="sfx3", loop=False, relative_volume = 1.5)
    show screen ramen_peaking("ramen_nightscene1_3") 
    show screen peaking_overlayramen
    with Dissolve(2)
    $ renpy.sound.play("/audio/soun_fx/cough1.opus", channel="sfx3", loop=False, relative_volume = 0.7)
    yo"*Cough cough*"
    bot"He is pulling her around by her hair..."
    $ renpy.sound.play("/audio/soun_fx/smashtable.opus", channel="sfx3", loop=False, relative_volume = 0.6)
    obo"Get on the fucking table!" with vpunch
    hide screen ramen_peaking
    hide screen peaking_overlayramen
    scene black
    with dissolve
    obo"I am just getting started fucking your throat..."
    show screen ramen_peaking("ramen_nightscene1_2") 
    show screen peaking_overlayramen
    with Dissolve(1)
    $ renpy.sound.play("/audio/soun_fx/bj2.opus", channel="sfx3", loop=False, relative_volume = 0.7)
    $ renpy.sound.play("/audio/soun_fx/inogag1.opus", channel="sfx2", loop=False, relative_volume = 0.7)
    obo"How's this you slut!" with vpunch
    obo"You will not breathe again until I empty my balls right down your esophagus!"
    obo"Now sit there like the little cock-sleeve you are and..."
    show screen ramen_peaking("ramen_nightscene1_anim2")
    $ renpy.sound.play("/audio/soun_fx/bj3.opus", channel="sfx3", loop=False, relative_volume = 0.99)
    $ renpy.sound.play("/audio/soun_fx/gags/SDTGag1.opus", channel="sfx2", loop=False, relative_volume = 1.2)
    obo"Allow me to expand your throat's crevices!" with vpunch
    bot"The old bastard is fucking crazy!"
    $ renpy.sound.play("/audio/soun_fx/bj2.opus", channel="sfx3", loop=False, relative_volume = 0.99)
    $ renpy.sound.play("/audio/soun_fx/gags/SDTGag23.opus", channel="sfx2", loop=False, relative_volume = 1.2)
    bot"He is pulling Yoru around by her throat..."
    menu:
        bot"He is pulling Yoru around by her throat..."
        "He is a monster":
            bot"He is a monster..."
        "I could learn a thing or two from him":
            bot"This is kinda fun! I could learn a thing or two from the old bastard."
    $ renpy.sound.play("/audio/soun_fx/gags/SDTGag16.opus", channel="sfx2", loop=False, relative_volume = 1.2)
    obo"Would you look at that... your throat is bulging from taking all of my cock inside of it!"
    obo"You are a deepthroat champion Yoru..."
    $ renpy.sound.play("/audio/soun_fx/bj2.opus", channel="sfx3", loop=False, relative_volume = 1.1)
    $ renpy.sound.play("/audio/soun_fx/chokegag1.opus", channel="sfx2", loop=False, relative_volume = 0.7)
    show screen ramen_peaking("nightscene1_anim1") 
    obo"But can you handle this!?"
    $ renpy.sound.play("/audio/soun_fx/bj1.opus", channel="sfx1", loop=False, relative_volume = 1.1)
    yo"*Gluck Gluck* mmh-gluck..."
    obo"Now that's a proper way to fuck a whore's throat... Don't you think?"
    $ renpy.sound.play("/audio/soun_fx/gaspforair2.opus", channel="sfx2", loop=False, relative_volume = 0.99)
    obo"Don't gasp for air just yet..."
    obo"I can go much faster than this!"
    with vpunch
    show screen ramen_peaking("nightscene1_anim2")
    $ renpy.sound.play("/audio/soun_fx/bj2.opus", channel="sfx3", loop=False, relative_volume = 1.1)
    $ renpy.sound.play("/audio/soun_fx/chokegag2.opus", channel="sfx2", loop=False, relative_volume = 0.7)
    obo"*Grunts*"
    obo"That's it Yoru... Take it!" with vpunch
    
    obo"Take it all down your throat!" with vpunch
    $ renpy.sound.play("/audio/soun_fx/bj3.opus", channel="sfx3", loop=False, relative_volume = 1.1)
    $ renpy.sound.play("/audio/soun_fx/chokegag3.opus", channel="sfx1", loop=False, relative_volume = 0.7)
    obo"I am about to fill you up with my semen!" with flash
    obo"Don't you go choking on it now bitch!"
    show screen ramen_peaking("ramen_nightscene1_afteranim1") with dissolve
    $ renpy.sound.play("/audio/soun_fx/throatcum.opus", channel="sfx2", loop=False, relative_volume = 1)
    $ renpy.sound.play("/audio/soun_fx/throatpie.opus", channel="sfx3", loop=False, relative_volume = 1)
    obo"Yessss...!" with flash
    $ renpy.sound.play("/audio/soun_fx/bj/swallowlong.opus", channel="sfx2", loop=False, relative_volume = 0.7)
    obo"That's it you whore... Gulp all of it down!" with flash
    $ renpy.sound.play("/audio/soun_fx/cum7.opus", channel="sfx1", loop=False, relative_volume = 1)
    obo"Every single last drop!" with flash
    $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx3", loop=False, relative_volume = 1)
    show screen ramen_peaking("ramen_nightscene1_afteranim2") with longerflash
    obo"Aaaaarrrgh!"
    obo"Let me hear you swallow it all Yoru..."
    obo"Cock stays inside until I hear you gulp every..."
    $ renpy.sound.play("/audio/soun_fx/bj/Swallow 1.opus", channel="sfx2", loop=False, relative_volume = 1.5)
    obo"Last..."
    $ renpy.sound.play("/audio/soun_fx/bj/Swallow 7.opus", channel="sfx2", loop=False, relative_volume = 0.7)
    yo"*Gulp*"
    obo"Drop!"
    $ renpy.sound.play("/audio/soun_fx/bj/Swallow 1.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    yo"*Gulp*"
    obo"Now that's a good girl!"
    $ renpy.sound.play("/audio/soun_fx/bj/Swallow 1.opus", channel="sfx2", loop=False, relative_volume = 0.6)
    hide screen ramen_peaking
    scene black
    with dissolve
    $ renpy.sound.play("/audio/soun_fx/chokecum2.opus", channel="sfx2", loop=False, relative_volume = 0.7)
    obo"I will allow you but a fleeting moment. To gather yourself..."
    show screen ramen_peaking("ramen_nightscene1_3") with dissolve
    obo"But you know you have one last job... right?"
    obo"It is tradition after all..."
    yo"P-please O-obo... Not t-this time. It s-smells so bad..."
    scene black
    hide screen ramen_peaking
    hide screen peaking_overlayramen
    with vpunch
    $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    $ renpy.sound.play("/audio/soun_fx/femalegrunt1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
    yo"Aarh!"
    $ renpy.sound.play("/audio/soun_fx/smashtable.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    $ renpy.sound.play("/audio/soun_fx/glasssmash.opus", channel="sfx3", loop=False, relative_volume = 0.5)
    obo"You dare speak up to me you bitch!?" with vpunch
    "Obo picked up the coffee mug he had Yoru prepare for him and threw it across the room in rage..."
    bot"Holy shit Obo is insane..."
    obo"Now crawl to me and make yourself useful or I swear you'll be out in the streets begging by tomorrow morning."
    show screen ramen_peaking("ramen_nightscene1_4")
    show screen peaking_overlayramen
    $ renpy.sound.play("/audio/soun_fx/bjsfx.opus", channel="sfx2", loop=False, relative_volume = 1.5)
    $ renpy.sound.play("/audio/soun_fx/bjair1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
    with Dissolve(2)
    yo"*Slurping*"
    obo"See now you are being useful..."
    obo"Smells bad you say..."
    obo"*Scoffs*"
    obo"How do you think a cock smells after a hard day of work in the kitchen you whore!" with vpunch
    obo"But that's exactly why you are here Yoru!"
    $ renpy.sound.play("/audio/soun_fx/bjsfx.opus", channel="sfx2", loop=False, relative_volume = 1.5)
    $ renpy.sound.play("/audio/soun_fx/bjair2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
    yo"*Slurping*"
    obo"To lick the sweat and grease right off from it!"
    obo"I am sure all this shit you cooked for me tastes worse than my cock..."
    obo"So tell me Yoru..."
    $ renpy.sound.play("/audio/soun_fx/bjsfx.opus", channel="sfx2", loop=False, relative_volume = 1.5)
    $ renpy.sound.play("/audio/soun_fx/bjair1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
    obo"If you are useless when it comes to cooking..."
    obo"Useless when working in my kitchen..."
    hide screen ramen_peaking
    hide screen peaking_overlayramen
    scene black with vpunch
    $ renpy.sound.play("/audio/soun_fx/gaspforair2.opus", channel="sfx3", loop=False, relative_volume = 1.0)
    obo"Then what are you good for!?" with vpunch
    $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    $ renpy.sound.play("/audio/soun_fx/gruntwoman2.opus", channel="sfx3", loop=False, relative_volume = 0.9)
    obo"Huh!?" with vpunch
    yo"D-don't hit me... P-please..."
    obo"Shut the fuck up and open your mouth... I have a gift for you!"
    show screen ramen_peaking("ramen_nightscene1_6")
    show screen peaking_overlayramen
    $ renpy.sound.play("/audio/soun_fx/cum4.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    obo"Hnnargh!" with flash
    show screen ramen_peaking("ramen_nightscene1_7")
    $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    obo"Y-yeeessss!!" with longerflash
    obo"Now that's a look that suits a whore like you!"
    obo"Open wide and show me your tongue! I have something else for you..."
    show screen ramen_peaking("ramen_nightscene1_8") with dissolve
    obo"That's a good girl..."
    obo"Before that... I'll ask once more since you neglected to answer before..."
    obo"What are you good for then... Yoru?"
    $ renpy.sound.play("/audio/soun_fx/gruntwoman2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    $ renpy.sound.play("/audio/soun_fx/inocrying3.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    show screen ramen_peaking("ramen_nightscenefinal1") with vpunch
    obo"HMM?" with vpunch
    yo"*Holding back tears*"
    yo"To b-be y-your..."
    obo"Look at me in the eyes while you say it, bitch!" with vpunch
    show screen ramen_peaking("ramen_nightscenefinal2") with dissolve
    yo"To b-be your... *sobbing* o-obedient cum-slut..."
    obo"That's right you whore!"
    obo"To be my obedient little cum-dump..."
    obo"You better remember that!"
    $ renpy.sound.play("/audio/soun_fx/spit4.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    pause 0.5
    hide screen ramen_peaking
    hide screen peaking_overlayramen
    scene black with flash
    show ramenshop upstairs with dissolve
    bot"Good lord, what the fuck am I watching!"
    $ renpy.end_replay()
    if yoru_replayscenes == True: #replay
        $ yoru_replayscenes = False
        jump action_taken
    bot"Obo is a fucking animal..."
    menu:
        bot"Obo is a fucking animal..."
        "Kindred spirits, me and him!":
            bot"Takes one to know one!"
            bot"Me and him, we could do... things together, I reckon!"
        "I have to do something for Yoru!":
            bot"I can't leave Yoru in his hands..."
            bot"I'll have to figure out a way to save her!"
    bot"But I better get the fuck out of here before the crazy bastard sniffs me out!"
    scene black with dissolve
    "You make your way home as you contemplate what you just experienced..."
    bot"How can the old fuck have such a hold over her..."
    
    $ notification ("Quest updated")
    $ quest.check("job_3", "completed")
    $ quest.check("job_4", "in progress")
    bot"I need to find out more! There must be something I am missing..."
    jump action_taken
        



screen ramen_peaking(baseImage):
    on "show" action Function(mark_screen_image_gallery, baseImage)

    key "K_SPACE" action Return()
    button:
        action Return()
    viewport id "ramenpeeking":
        child_size (1900, 0)
        edgescroll (300, 900)
        draggable True
        yinitial 0.5
        xinitial 0.5
    
        frame:
            background None
            # foreground "particleFog" at alpha1
            
            xalign 0.5
            
            viewport:
                yinitial 1.0
                xinitial 1.0
                area (150, 0, 1.0, 1.0)
                child_size (1600, 1328)
                edgescroll (350, 900)
                add baseImage subpixel True
    
    imagebutton:
        xalign 0.5 yalign 0.01
        auto "images/ui/viewunzoomed_%s.png"
        hovered Show("displayTextScreen", displayText = "View CG unzoomed")
        unhovered [Hide("displayTextScreen")]
        action [Show("unzoomed_image", baseImage = baseImage), Hide("displayTextScreen")]
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"

screen peaking_overlayramen():
    
    sensitive False
    add "bgp peak2" xalign 0.5

screen unzoomed_image(baseImage):
    modal True
    on "show" action Function(mark_screen_image_gallery, baseImage)

    add baseImage zoom 0.8 xalign 0.5 yalign 0.5
    for k in ['K_RETURN', 'K_SPACE', 'K_KP_ENTER', 'K_SELECT', 'mouseup_1']:
        key k action NullAction()
    
    #full screen button
    button:
        action NullAction()


    #return
    imagebutton:
        xalign 0.95 yalign 0.05
        auto "images/ui/return_button_%s.png"
        hovered Show("displayTextScreen", displayText = "Return to Event")
        unhovered [Hide("displayTextScreen")]
        action [Hide("unzoomed_image"), Hide("displayTextScreen")]
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"



































































