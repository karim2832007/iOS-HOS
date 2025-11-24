label kuramachoice_dream:
    $ initialize_replay_defaults()
    default kushina_plan_unlocked = False
    $ kushina_plan_unlocked = True
    $ renpy.sound.play("/audio/ost/sleep.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    scene black with fade
    pause(1)
    "You fall into a deep slumber..."
    show dreamvignette zorder 100 with dissolve
    "A strange dream captivates your senses..."
    play music"/audio/ost/dreaming.opus" volume 0.5
    $ renpy.sound.play("/audio/soun_fx/wind3.opus", channel="sfx3", loop=False, relative_volume = 0.8)
    show kushina_dream intro1 at brightreveal
    with flash
    ku"You made it back!"
    ku"Took you long enough!"
    ku"Hey, [bo_name]..."
    show kushina_dream intro1_0 with dissolve
    ku"Think you can try to speak this time?"
    ku"Don't worry if you still can't! It may take a while to build an affinity to this realm!"
    menu:
        ku"Don't worry if you still can't! It may take a while to build an affinity to this realm!"
        "...":
            pass
        "...":
            pass
        "Stare at her boobs...":
            show kushina_dream intro1_0 with dissolve:
                zoom 1.2 xalign 0.5 yalign 0.4
            call increaselust(10) from _call_increaselust_281
            default kushina_stareboobs = False
            $ kushina_stareboobs = True
            bot"..."
            ku"Uuuh... Heh-he! *nervous chuckle*"
            ku"It seems like you are still not quite there yet!"
    show screen parallax1280("kushina_dream intro1",1,0.5) with dissolve
    call showscrollingimage from _call_showscrollingimage_242
    bot"."
    bot".."
    bot"..."
    show screen parallax1280("kushina_dream intro1_0",1,0.5) with dissolve
    ku"Don't even worry about it!"
    show screen parallax1280("kushina_dream intro1",1,0.5) with dissolve
    ku"It took your [na_rel] years to speak too. I am sure you'll get there in no time!"
    ku"Not to worry though, we can still convene, even via your subconscious alone."
    ku"The Kyuubi's chakra forever binds us after all. A blessing, and a curse both..."
    show screen parallax1280("kushina_dream intro1_0",1,0.5) with dissolve
    ku"I am just hoping that it'll turn out to be more of a blessing for you than it was for me! Hehe *Nervous chuckle*"
    bot"A... d-dream?"
    show screen parallax1280("kushina_dream intro1",1,0.5) with dissolve
    ku"Ah! S-silly me! I forgot to tell you..."
    ku"I can faintly read your thoughts, or at least I think I can..."
    ku"Just now, you thought this was a dream, right?"
    bot"It... isn't?"
    show screen parallax1280("kushina_dream intro1_0",1,0.5) with dissolve
    ku"Well... Not exactly a dream."
    ku"More like..."
    show screen parallax1280("kushina_dream intro1",1,0.5) with dissolve
    ku"A construct of your mind. Like a fever hallucination, but also as real as you make it out to be..."
    ku"Both me and [na_name] had our own constructs. Your [na_rel]'s was a sky, and mine was a prison..."
    ku"I know, I know, hard to wrap your mind around, right?"
    ku"You see this beach? What if I told you it resembles something about you..."
    ku"It's hard to say exactly, but if I were to wager a guess..."
    ku "Look at that horizon, how it stretches endlessly before us, azure sky melting into deeper cerulean waters." 
    ku "Like your potential, it appears infinite yet remains seemingly unreachable."  
    ku "Each day you walk closer to that distant line, yet it retreats with equal measure..." 
    ku "Not in mockery, but in invitation. Your ambition lives in that space where sea meets sky."
    $ renpy.sound.play("/audio/soun_fx/wind2.opus", channel="sfx3", loop=False, relative_volume = 1.2)
    show screen parallax1280("kushina_dream int0",1,0.5) with dissolve
    ku "Listen to those waves. That eternal rhythm... Crash, retreat, crash, retreat, and on it goes forever more."  
    ku "Some waves retreat gently, while others surge forward with magnificent force, reshaping the very coastline."   
    ku "Like your emotions, they cannot be stopped, only experienced and allowed to pass."
    ku "And this sand beneath our feet... each grain has traveled impossible distances."
    ku "From mountain peaks to river beds, only to arrive at this very moment under your step."
    ku "Your own journey is bound to be equally uncertain, but equally purposeful!"
    ku "What you see here, is what you are [bo_name]... Remember this!"
    ku "As for me, I am not sure why I am in a bikini of all things, although I am sure your mind has a valid reason to conjure me like this..."
    if kushina_stareboobs == True:
        show screen parallax1280("kushina_dream int0_1",1,0.5) with dissolve
        ku"Although I did sense a strange thought from you a moment ago."
        ku"There's no way you see your granny like that, r-right? Heh-eh... *Nervous chuckle*"
    else:
        show screen parallax1280("kushina_dream int0_1",1,0.5) with dissolve
        ku"At least I hope so! Heh-eh... *Nervous chuckle*"
    scene black with dissolve
    call hidescrollingimage from _call_hidescrollingimage_209
    scene kushina_dream intro1_0 with dissolve:
        yalign 1.0
    show kushina_dream intro1_0:
        easein 4 yalign 0.2
    stop music fadeout 3
    $ renpy.sound.play("/audio/soun_fx/wind4.opus", channel="sfx3", loop=False, relative_volume = 0.8)
    ku"Now come! There's something I wanted to show you..."
    $ renpy.sound.play("/audio/ost/Dramatic-OST.opus",channel="music",loop=True,relative_volume=1)
    $ renpy.sound.play("/audio/soun_fx/bassstart.opus",channel="sfx1",loop=False,relative_volume=0.5)
    $ renpy.sound.play("/audio/soun_fx/growl1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
    show kurama1
    show kurama1:
        easein 2 alpha 0.0
    with flash
    pause 1
    show red_shockwave with dissolve
    show red_shockwave:
        easein 2 alpha 0.0
    show kushina_dream intro1_1 with dissolve
    ku"D-damn it!" with vpunch
    show screen parallax1280("kushina_dream intro1_2",1,0.5) with dissolve
    call showscrollingimage from _call_showscrollingimage_243
    ku"I knew he was lurking around, but I hoped we'd have a little bit more time to ourselves..."
    ku"No matter... I'll handle this!"
    scene black
    call hidescrollingimage from _call_hidescrollingimage_210
    ku"Stay back [bo_name]!"
    $ renpy.sound.play("/audio/soun_fx/growl2.opus", channel="sfx2", loop=False, relative_volume = 0.7)
    $ renpy.sound.play("/audio/soun_fx/thunderstrike.opus", channel="sfx3", loop=False, relative_volume = 0.5)
    show red_shockwave with dissolve
    show red_shockwave:
        easein 2 alpha 0.0
    pause 0.2
    show kushina_dream_bg with dissolve
    show kushina_dream kurama 0 with flashred:
        alpha 0.0 yalign 1.0
    show kushina_dream:
        easein 3 alpha 1.0 yalign 0.4
    beast"Did you really think I'd let you to your devious machinations, woman..."
    $ renpy.sound.play("/audio/soun_fx/growl1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    beast"Where you exist, I will prey. You know that much... *Low growl*"
    show kushina_dream kurama 1_1 with dissolve:
        easein 2 yalign 1.0
    ku"And where you prey, I shall always be there to stop you!"
    show kushina_dream:
        easein 3 yalign 0.6
    ku"You will not claim what you desire. Not now, nor ever!" with vpunch
    $ renpy.sound.play("/audio/soun_fx/growl2.opus", channel="sfx2", loop=False, relative_volume = 0.7)
    show kushina_dream kurama 1 with dissolve
    beast"*GROWLS*" with Shake((0, 0, 0, 0), 2, dist=10, peak_time=0.7, smoothness=50)
    beast "You think a mere fragment like YOU... has the power to stop me?"
    "The two constructs of your mind engage in a heated exchange. You can only observe from a distance, unable to speak yourself..."
    "Yet you feel the weight of the world crushing down on your shoulders, realizing a critical decision looms before you. One that will determine the fate of your very soul."
    jump v20_show_split_choice


label temporary_v20_choice:
    default nochoice_made_yet = False
    $ nochoice_made_yet = True

    # dev"The choice you make will not be final in this version."
    # dev"Neither choice will currently affect your gameplay outside of this dream. As such, you can freely choose either option to see the introductory events."
    # dev"Full implementation of the events, as well as the surrounding systems, are planned for v0.21."
    "You aren't yet ready to make a choice..."
    ku"[bo_name]! Leave while it's still safe..."
    ku"I'll handle things and keep this beast at bay!"
    ku"Return to me once you are ready!"
    $ renpy.sound.play("/audio/soun_fx/wakeup.opus", channel="sfx3", loop=False, relative_volume = 0.6)
    $ renpy.sound.play("/audio/soun_fx/growl1.opus", channel="sfx2", loop=False, relative_volume = 0.7)
    show kushina_dream wakeup at brightreveal:
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 
    with longerflash
    with Shake((0, 0, 0, 0), 1.5, dist=20, peak_time=0.8, smoothness=50)
    pause 0.3
    scene kushina_dream wakeup with dissolve
    bo"*Snoring*..." with vpunch
    scene black with dissolve
    "Visit Kushina once you've completed enough objectives in the respective path you want to choose."
    $ nochoice_made_yet = True
    jump action_taken
    # menu:
    #     dev"The choice you make will not be final in this version.\nFull implementation of the events, as well as the surrounding systems is planned for v0.21."
    #     "Test Love Path (Not final)":
    #         jump v20_testlovepath_temp
    #     "Test Hatred Path (Not final)":
    #         jump v20_testhatepath_temp
        


label v20_testlovepath_temp:
    stop sfx1 fadeout 1
    stop sfx2 fadeout 1
    stop music fadeout 1
    scene black with dissolve
    bot"I..."
    $ playmusic("audio/ost/dreaming.opus",0.5)
    $ renpy.sound.play("/audio/soun_fx/growl3.opus", channel="sfx2", loop=False, relative_volume = 0.7)
    show kushina_dream kurama_chained with flash:
        yalign 1.0
    show kushina_dream:
        easein 3 yalign 0.4
    beast"*Snarls with rage!* REEEEeEee!" with Shake((0, 0, 0, 0), 2, dist=10, peak_time=0.7, smoothness=50)
    bo"I won't lose myself to you!"
    show kushina_dream with dissolve:
        yalign 1.0 zoom 1.2 xalign 0.5
    ku"[bo_name]!?" with vpunch
    ku"You... did that? You can speak too!"
    bo"I t-think so...?"
    show kushina_dream kurama_chained1 with dissolve
    show kushina_dream:
        easein 3 yalign 0.5
    ku"Quickly then!"

    "Kushina makes her way back to you, holding a small fragment of light in her palm..."
    show love_choice_split_screen with dissolve:
        yalign 1.0 subpixel True
    show love_choice_split_screen:
        easein 4 yalign 0.4
    ku"Take this, squeeze it in your hand, or rather... brain! Imagine you are shattering a fragment of his soul!"
    ku"Do that, and it'll weaken his hold over you and break this dark illusion of his..."
    bo "R-right!"
    scene kushina_dream kurama_chained1 with dissolve:
        yalign 1.0
    show kushina_dream kurama_chained1:
        easein 3 yalign 0.4
    $ renpy.sound.play("/audio/soun_fx/growl2.opus", channel="sfx2", loop=False, relative_volume = 0.7)
    beast"Do NOT listen to her. Do so and you shall live to forever regret it!"
    beast"Without me you are NOTHING!"
    "You heed Kushina's advice, and attempt to break a fragment of the beast's soul..."
    $ renpy.sound.play("/audio/soun_fx/wakeup.opus", channel="sfx3", loop=False, relative_volume = 0.6)
    label repeat_kushina_love_introscene:
    show kushina_dream kurama_chained1 at brightreveal:
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 
    with longerflash
    with Shake((0, 0, 0, 0), 1.5, dist=20, peak_time=0.8, smoothness=50)
    $ renpy.sound.play("/audio/soun_fx/thunderstrike.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    pause 0.3
    show kushina_dream_bg:
        alpha 0.0
    show kushina_dream_bg:
        easein 3 alpha 1.0 yalign 1.0
    beast"You think this does anything to alter the course of your destiny?"
    $ renpy.sound.play("/audio/soun_fx/growl2.opus", channel="sfx1", loop=False, relative_volume = 0.7)
    beast"I will be back... *Low growl*"
    ku"[bo_name]!"
    scene black
    # show kushina_dream intro1_1
    # with dissolve
    # show kushina_dream intro1_0:
    #     alpha 0.0 yalign 1.0
    # show kushina_dream intro1_0:
    #     easein 3 alpha 1.0 yalign 0.4
    scene kushina_dream intro1_1 with dissolve:
        yalign 1.0
    show kushina_dream intro1_1:
        easein 4 yalign 0.2
    $ renpy.sound.play("/audio/soun_fx/wind4.opus", channel="sfx3", loop=False, relative_volume = 0.8)
    show kurama1
    show kurama1:
        easein 2 alpha 0.0
    with flash
    pause 1
    show red_shockwave with dissolve
    show red_shockwave:
        easein 2 alpha 0.0
    show kushina_dream intro1_0 with dissolve
    ku"You did it! You broke his reign over you! This time at least..."
    bo"I... did?"
    ku"See what I mean when I say everything in here is a construct of your mind?"
    show kushina_dream intro1 with dissolve:
        zoom 1.1 xalign 0.5
    ku"You are getting the hang of it quick! *Giggles*"
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/wind3.opus", channel="sfx3", loop=False, relative_volume = 0.8)
    show kushina_dream love1:
        yalign 1.0
    show kushina_dream at brightreveal:
        easein 4 yalign 0.5
    ku"M-maybe... too q-quick!"
    bo"Am I... real? Is this re-real!?"
    show kushina_dream love1_1 with dissolve:
        xalign 0.0 yalign 0.4 zoom 1.1
    ku"I can't believe it..."
    ku"You look..."
    scene black with vpunch
    $ renpy.sound.play("/audio/soun_fx/intro/bodythud.opus", channel="sfx3", loop=False, relative_volume = 0.5)
    ku"Just like my son!"
    show screen parallax1280("kushina_dream love1_2",1,0.5) with dissolve
    call showscrollingimage from _call_showscrollingimage_244
    ku"A spitting image of him! Only maybe a little bit cuter!"
    ku"How'd you even do that!?"
    bo"You said this place is what I make it to be, so... I just thought myself living in it right alongside you, and then..."
    bo"...here I am!"
    ku"You truly are gifted, you know that? To be able to take a physical form in your own plane is no small feat!"
    bo"A-auntie..."
    ku"O-oh oops! *Giggle* S-sorry, it's just that..."
    ku"This is the first time I've ever seen how you look! You'll have to excuse my excitement this one time!"
    ku"Need I remind you I am not exactly a-alive..."
    ku"I simply exist in your mind, just like the beast does..."
    call increaselust(10) from _call_increaselust_282
    bo"Y-you certainly feel alive."
    ku"H-hey... I am not that fat, am I!? *Giggles*" with vpunch
    bot"If this is a dream, then..."
    menu:
        bo"Y-you certainly feel alive."
        "Grope her boobs!":
            bo"If this is a dream, and you are not real, then..."
            $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.2)
            show screen parallax1280("kushina_dream love1_2tits",1,0.5) with dissolve
            ku"U-uhm... [bo_name]?"
            scene kushina_dream love1_2tits:
                yalign 1.0

        "Grab her ass!":
            bo"If this is a dream, and you are not real, then..."
            $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 1.2)
            show screen parallax1280("kushina_dream love1_2ass",1,0.5) with dissolve
            ku"U-uhm... [bo_name]?"
            scene kushina_dream love1_2ass:
                yalign 1.0
    scene black
    call hidescrollingimage from _call_hidescrollingimage_211
    bo"Definitely feels real!" with vpunch
    ku"Uhm, *nervous giggle* I am still... myself, ya know!?"
    $ renpy.sound.play("/audio/soun_fx/wakeup.opus", channel="sfx3", loop=False, relative_volume = 0.6)

    show kushina_dream wakeup at brightreveal:
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 
    with longerflash
    with Shake((0, 0, 0, 0), 1.5, dist=20, peak_time=0.8, smoothness=50)
    pause 0.3
    scene kushina_dream wakeup with dissolve
    bo"*Snoring*..." with vpunch
    scene black with dissolve
    "You can now visit Kushina and Kurama in your dreams."
    # $ chosen_love_path = True
    jump action_taken


label v20_testhatepath_temp:
    stop sfx1 fadeout 1
    stop sfx2 fadeout 1
    $ renpy.sound.play("/audio/soun_fx/horror.opus",channel="sfx1",loop=False,relative_volume=1)
    scene black with dissolve
    $ renpy.pause(1, hard=True)
    $ playmusic("/audio/ost/evilhymn.opus", 1.2)
    $ renpy.sound.play("/audio/soun_fx/howlingwind.opus",channel="sfx2",loop=True,relative_volume=0.3)
    "You chose evil, and evil chose you. A terrible and yet beautiful power answers your call."
    show kushina_dream kurama 1_1 with dissolve
    show kushina_dream kurama 1_1:
        easein 3 yalign 0.5
    beast"We shall find out soon enough, red-haired fox..."
    show kushina_dream:
        easein 3 yalign 0.0
    ku"I told you already. You lay as much as a hand on him..."
    show kushina_dream kurama 0 with dissolve
    ku"And I'll kill you myself!" with vpunch
    $ renpy.sound.play("/audio/soun_fx/growl1.opus", channel="sfx2", loop=False, relative_volume = 0.7)
    beast"Riiiight, right..."

    show kushina_dream:
        easein 1 yalign 0.3
    boe"Oi..." with vpunch
    boe"Oi kid, can you hear me..." with vpunch
    bot"Ku... Kurama...?"
    boe"She is about to hand you over a fragment of my soul. Keep it intact..."
    boe"In exchange, I'll show you a world you never knew existed."
    $ renpy.sound.play("/audio/soun_fx/wakeup.opus", channel="sfx3", loop=False, relative_volume = 0.6)
    show kushina_dream at brightreveal:
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 
    with longerflash
    with Shake((0, 0, 0, 0), 1.5, dist=20, peak_time=0.8, smoothness=50)
    $ renpy.sound.play("/audio/soun_fx/thunderstrike.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    pause 0.3
    show kushina_dream_bg:
        alpha 0.0
    show kushina_dream_bg:
        easein 3 alpha 1.0 yalign 1.0
    beast"Hee-hee-hee..."
    $ renpy.sound.play("/audio/soun_fx/growl2.opus", channel="sfx1", loop=False, relative_volume = 0.7)
    beast"Remember our pact..."
    show love_choice_split_screen with dissolve:
        yalign 1.0 subpixel True
    show love_choice_split_screen:
        easein 4 yalign 0.4
    "Kushina makes her way back to you, holding a small fragment of light in her palm..."
    ku"Quickly [bo_name]! You have to try and break this fragment of his soul."
    ku"Every broken fragment, weakens his hold over you..."
    bot"..."
    ku"Come on! Trust me on this one!" with vpunch
    show kurama1 with flashred
    show kurama1:
        easein 1 alpha 0.0
    show red_shockwave with dissolve
    show red_shockwave:
        easein 2 alpha 0.0
    $ renpy.sound.play("/audio/soun_fx/growl2.opus", channel="sfx2", loop=False, relative_volume = 0.7)
    $ renpy.sound.play("/audio/soun_fx/eye4s.opus", channel="sfx1", loop=False, relative_volume = 0.7)
    show screen parallax1280("kushina_dream hate1",1,0.2) with dissolve
    call showscrollingimage from _call_showscrollingimage_245
    bot"I don't think I will..."
    ku"W-what? I think I am having trouble reading your thoughts..."
    ku"You are still with me, right?"
    bot"Naaah! You heard me right!"
    ku"[bo_name_stutter]...?"
    $ renpy.sound.play("/audio/soun_fx/thunderstrike.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    hide screen parallax1280
    show screen parallax1280("kushina_dream hate1_1",1,0.2)
    with flash
    ku"W-what is the meaning of this! How did you-"
    ku"Did you do this!?" with vpunch
    ku"No, it can't be... It's the beast's doing!"
    ku"It must have took hold of you, but there's still time."
    ku"Listen carefully..."
    ku"When you feel like you are losing yourself, look towards those you love most."
    ku"All you have to do is think of who you were before the curse took manifest. That's how you repel it, with the help of others."
    ku"So please..."
    hide screen parallax1280
    show screen parallax1280("kushina_dream hate1_2",1,0.2)
    with dissolve
    ku"Listen to me!"
    bot"Making demands now, aren't you?"
    ku"N-no! I am just trying to help. You can't let the Kyuubi do to you what it did to me."
    ku"You HAVE to fight it!"
    bot"I don't think you understand..."
    bot"The beast has nothing to do with this."
    ku"H-huh...?"
    bot"Now let's put your teachings to the test!"
    bot"You said this realm is my conjuring, right?"
    bot"Does that mean you are bound to my will too?"
    ku"What are you planning to do..."
    bot"In that case..."
    $ renpy.sound.play("/audio/soun_fx/thunderstrike.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    hide screen parallax1280
    show screen parallax1280("kushina_dream hate1_3",1,0.2)
    with flash
    bot"Raise your hands up!" with vpunch
    ku"S-stop it! It's not wise to use your powers against your own people! It'll only serve to empower him..."
    bot"Interesting..."
    bot"Although, I thought I already told you..."
    $ renpy.sound.play("/audio/soun_fx/thunderstrike.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    hide screen parallax1280
    show screen parallax1280("kushina_dream hate2_1",1,0.2)
    with flash
    bo"This is my doing!" with vpunch
    ku"[bo_name_stutter]!? How did you..."
    ku"To take physical form in your own conjuring is a skill that takes years!"
    ku"You look exactly like your [na_rel]! More importantly..."
    ku"W-what the hell are you thinking, touching your granny like that!" with vpunch
    bo"I think you are my type of girl, granny!"
    ku"What the hell are you saying you imbecile."
    ku"The Kyuubi is going to have a field day with your stupid-ass if you don't take this seriously!"
    hide screen parallax1280
    show screen parallax1280("kushina_dream hate2",1,0.2)
    with dissolve
    ku"H-hey!" with vpunch
    bo"Oh I am taking this extremely seriously.\nThanks to you, I think I might have discovered a newfound self of mine!"
    bo"I should probably repay you in some way!"
    ku"You have to snap out of it!"
    bo"Say granny, since you are bound to my will, does that mean that..."
    hide screen parallax1280
    show screen parallax1280("kushina_dream hate2_2",1,0.2)
    with dissolve
    ku"W-what the!" with vpunch
    bo"If I wanted to FUCK you... would you oblige me?" with vpunch
    scene black
    call hidescrollingimage from _call_hidescrollingimage_212
    $ renpy.sound.play("/audio/soun_fx/wakeup.opus", channel="sfx3", loop=False, relative_volume = 0.6)

    show kushina_dream wakeup at brightreveal:
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 
    with longerflash
    with Shake((0, 0, 0, 0), 1.5, dist=20, peak_time=0.8, smoothness=50)
    pause 0.3
    scene kushina_dream wakeup with dissolve
    call changeHatred(5) from _call_changeHatred_202
    bo"*Snoring... angrily!*" with vpunch
    scene black with dissolve
    "You can now visit Kushina and Kurama in your dreams."
    # $ chosen_hate_path = True
    jump action_taken

label kuramachoice_dream_repeat:
    $ renpy.sound.play("/audio/ost/sleep.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    scene black with fade
    "You fall into a deep slumber..."
    $ renpy.sound.play("/audio/ost/Dramatic-OST.opus",channel="music",loop=True,relative_volume=1)
    $ renpy.sound.play("/audio/soun_fx/bassstart.opus",channel="sfx1",loop=False,relative_volume=0.5)
    $ renpy.sound.play("/audio/soun_fx/growl1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
    show kurama1
    show kurama1:
        easein 2 alpha 0.0
    with flash
    pause 1
    show red_shockwave with dissolve
    show red_shockwave:
        easein 2 alpha 0.0
    show kushina_dream intro1_1 with dissolve
    show kushina_dream:
        easein 2 yalign 0.0
    ku"D-damn it!" with vpunch
    show screen parallax1280("kushina_dream intro1_2",1,0.5) with dissolve
    call showscrollingimage from _call_showscrollingimage_246
    ku"I knew he was coming, but I hoped we'd have a little bit more time to ourselves..."
    ku"No matter... I'll handle this!"
    scene black
    call hidescrollingimage from _call_hidescrollingimage_213
    ku"Stay back [bo_name]!"
    $ renpy.sound.play("/audio/soun_fx/growl2.opus", channel="sfx2", loop=False, relative_volume = 0.7)
    $ renpy.sound.play("/audio/soun_fx/thunderstrike.opus", channel="sfx3", loop=False, relative_volume = 0.5)
    show red_shockwave with dissolve
    show red_shockwave:
        easein 2 alpha 0.0
    pause 0.2
    show kushina_dream kurama 0 with flashred:
        alpha 0.0 yalign 1.0
    show kushina_dream:
        easein 3 alpha 1.0 yalign 0.4
    beast"Did you really think I'd let you to your devious machinations, woman..."
    $ renpy.sound.play("/audio/soun_fx/growl1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    beast"Where you exist, I will prey. You know that much... *Low growl*"
    show kushina_dream kurama 1_1 with dissolve:
        easein 2 yalign 1.0
    ku"And where you prey, I shall always be there to stop you!"
    show kushina_dream:
        easein 3 yalign 0.6
    ku"You are not getting what you want. Not now, nor ever!" with vpunch
    $ renpy.sound.play("/audio/soun_fx/growl2.opus", channel="sfx2", loop=False, relative_volume = 0.7)
    show kushina_dream kurama 1 with dissolve
    beast"*GROWLS*" with Shake((0, 0, 0, 0), 2, dist=10, peak_time=0.7, smoothness=50)
    beast"You think YOU... will stop me?"
    "The two ethereal beings engage in a heated exchange. You can only observe from a distance, unable to speak yourself..."
    "Yet you feel the weight of the world on your shoulders, an important choice must be made."
    jump v20_show_split_choice