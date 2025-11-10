
label infirmary:
    $ playmusic("/audio/ost/house1.opus", volume=0.7)
    call hidemarketUI from _call_hidemarketUI_1
    call hideUI from _call_hideUI_47
    if (day_part == 1 or day_part == 2) and tsunadeintroduction == True:
        scene black
        scene bg infirmaryday with dissolve
        menu:
            bot"..."
            "Visit Tsunade":
                if tsunadeintroductionseen == False:
                    jump visitclinic
                else:
                    jump visitclinicrepeatable
            "Leave":
                show screen topleftbuttons
                $ ui.interact()
            


    elif day_part == 1 or day_part == 2:
        scene black
        scene bg infirmaryday with dissolve
    else:
        scene black
        scene bg infirmary with dissolve


    hide screen housemap
    bot"There is nothing to do here at this time..."
    show screen topleftbuttons
    $ ui.interact()



label visitclinic:

    # bg infirmary room #bg room
    # tsunade intro #tsunade sitting
    # bg clinic #bg out of room

    scene black with dissolve
    bo"Alright then..."

    default tsunade_infirmaryintroduction = False
    if tsunade_infirmaryintroduction == True:
        dev"You should not be here :( Something went wrong."
        jump visitclinic
    
    else:
        $ tsunade_infirmaryintroduction = True
    label replay_visittsunade2:
    $ initialize_replay_defaults()
    scene bg infirmaryinside with dissolve
    show boruto worried at center with dissolve
    bot"Uh! I hate the smell of hospitals..."
    bot"Makes me feel like I am diseased..."
    show boruto laughing with dissolve
    $ renpy.sound.play("/audio/soun_fx/heels1.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    bot"But that's maybe because I am.. Heh!"
    scene black with dissolve
    "The rhythmic sound of high heels tapping against the marble floor captivated your ears..."
    scene ts_intro1 with dissolve:
        zoom 1.25 xalign 0.5 yalign 1.0
    show ts_intro1:
        easein 2 yalign 0.15
    pause 2
    show screen parallax1280("ts_intro1", 1.25) with dissolve
    call showscrollingimage from _call_showscrollingimage_11
    ts"Ah, [bo_name]. I was expecting you... Follow me!"
    bo"R-right..."
    bot"...Damn"
    bot"Tsunade certainly has an ass on her..."
    call increaselust(10) from _call_increaselust_82
    ts"Move it!" with vpunch
    call hidescrollingimage from _call_hidescrollingimage_16
    show ts_intro2 with fade:
        zoom 1.25 xalign 0.5 yalign 1.0
    $ renpy.sound.play("/audio/soun_fx/heels1.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    ts"Your [hin_rel_mother] has informed me of your progress..."
    menu:
        ts"Your [hin_rel_mother] has informed me of your progress..."
        "Stare at her ass":
            bot"I haven't had the chance to check Tsunade's ass last time..."
            call increaselust(10) from _call_increaselust_83
            bot"The she sways her hips while walking in her heels is almost mesmerizing..."
            show ts_intro2:
                easein 0.5 yalign 0.15
            pause 0.5
            ts"Hey! Focus up..." with vpunch
            ts"Did you hear what I said?"
            show screen parallax1280("ts_intro2", 1.25) with dissolve
            call showscrollingimage from _call_showscrollingimage_12
            bo"Uuuh, yeah! Sure..."
            ts"*Sighs*"
            call hidescrollingimage from _call_hidescrollingimage_17
        "I can assume as much...":
            show ts_intro2:
                easein 1.5 yalign 0.15
            pause 1
            bo"I can assume as much. Things aren't going as well as she'd have hoped I think..."
            show screen parallax1280("ts_intro2", 1.25) with dissolve
            call showscrollingimage from _call_showscrollingimage_13
            bo"That's why I am here, right?"
            ts"We'll talk about that in my office..."
            call hidescrollingimage from _call_hidescrollingimage_18
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/heels2.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    ts"We have to make a small detour before we go to my office..."
    scene ts_intro_tap with dissolve:
        zoom 1.25 xalign 0.5 yalign 1.0
    show ts_intro_tap:
        easein 2 yalign 0.15
    pause 1
    ts"Follow me down this hallway..."
    bo"S-sure..."
    show screen parallax1280("ts_intro_tap", 1.25) with dissolve
    call showscrollingimage from _call_showscrollingimage_14
    call increaselust(10) from _call_increaselust_84
    bot"Was this old hag always this sexy...?"
    bot"The way she crosses her legs with every step she takes, It is kinda... seductive."
    bot"Is she doing it on purpose?"
    call hidescrollingimage from _call_hidescrollingimage_19
    show ts_intro3 with fade:
        zoom 1.25 xalign 0.5 yalign 1.0
    show ts_intro3:
        easein 2 yalign 0.15
    ts"I have to pick up something before we head to my office..."
    ts"Wait for me here, Okay?"
    menu:
        ts"Wait for me here, Okay?"
        "Sure thing":
            bo"Sure thing..."
            ts"I will be back in a second."
        "Keep staring at her ass...":
            show screen parallax1280("ts_intro3", 1.25) with dissolve
            call showscrollingimage from _call_showscrollingimage_15
            bot"Not sure what she's even on about at this point..."
            bot"I am just mesmerized by her movements..."
            call increaselust(10) from _call_increaselust_85
            bot"Not to mention that ass beneath her pantyhose..."
            bot"The way her pencil skirt wraps around it..."
            ts"Ugh!"
            ts"I'll be back in a moment..."
            call hidescrollingimage from _call_hidescrollingimage_20
    scene ts_1p with dissolve
    show ts_1p:
        easein 2 yalign 0.15
    bot"Considering what happened last time..."
    bot"I wonder if we'll pick up where we left off..."
    scene ts_2p with dissolve:
        yalign 0.5
    bot"W-what the!" with vpunch
    call increaselust(10) from _call_increaselust_86
    bot"She must know people are watching when she bends over like that..."
    bot"Her panties are out on display for everyone to see!"
    "Tsunade picks up the small red container from the bed on her left..."
    scene ts_3p with dissolve:
        yalign 0.2
    ts"Hmm..."
    bot"W-why is she looking at me like that!"
    bot"Is she really doing this on purpose!?"
    scene black with dissolve
    ts"Get a grip, we are almost there..."
    $ renpy.sound.play("/audio/soun_fx/heels1.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    scene ts_intro4 with dissolve
    call increaselust(10) from _call_increaselust_87
    show ts_intro4:
        easein 2 yalign 0.15
    ts"Down this hall..."
    show screen parallax1280("ts_intro4", 1.0) with dissolve
    call showscrollingimage from _call_showscrollingimage_16
    bot"Fuck... I am losing control"
    call hidescrollingimage from _call_hidescrollingimage_21
    scene ts_intro5 with fade:
        xalign 0.5 yalign 1.0
    show ts_intro5:
        easein 2.5 yalign 0.15
    ts"Aaaand take a left in here..."
    show screen parallax1280("ts_intro5", 1.00) with dissolve
    call showscrollingimage from _call_showscrollingimage_17
    bo"S-sure..."
    bot"I am entranced by her figure..."
    bot"I am going to need a release soon..."
    call hidescrollingimage from _call_hidescrollingimage_22
    scene black with dissolve
    ts"Take a seat, I just need to..."
    scene ts_introfinal with dissolve:
        zoom 0.625 xalign 0.5 yalign 1.0
    show ts_introfinal:
        easein 2 yalign 0.2
    ts"...Move some stuff around"
    call increaselust(10) from _call_increaselust_88
    ts"And find my notes..."
    show screen parallax1280("ts_introfinal", 0.625) with dissolve
    call showscrollingimage from _call_showscrollingimage_18
    bot"F-fuck me!"

    bot"I am s-sure of it... She has to be doing this on purpose..."
    bot"The way she bends forward with her ass hanging out..."
    call increaselust(10) from _call_increaselust_89
    bot"I can't take all this teasing anymore!"
    menu:
        bot"I can't take all this teasing anymore!"
        "{color=[dominancecolor]}I see what you are doing!{/color}":
            bo"Tsunade..."
            ts"...Huh?"
            "Click twice to make a move!"
            $ ui.interact()
            show screen parallax1280("ts_introfinal_1", 0.625) with dissolve
            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp4.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            bo"I see what you are doing, you harlot!" with vpunch
            ts"*Gasps* H-hey! Take your hands off me!"
            "Click twice to grope her ass!"
            $ ui.interact()
            $ renpy.sound.play("/audio/soun_fx/grope2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            call changeDominance(1) from _call_changeDominance_53
            show screen parallax1280("tsunade_infirmaryintroassgrab1", 0.625) with dissolve
            with vpunch
            "You started squeezing Tsunade's ass..."
            bo"You want for this, don't you!"
            ts"What the hell are you talking about, [bo_name]!"
            ts"Stop this at once!" with vpunch
            menu menustopthisatonce:
                ts"Stop this at once!"
                "{color=[hatredcolor]}Your words say one thing...{/color}":
                    call checkHatred(15, "menustopthisatonce") from _call_checkHatred_10
                    bo"Your words say one thing..."
                    show screen parallax1280("ts_introfinal_3", 0.625) with dissolve
                    call changeHatred(1) from _call_changeHatred_94
                    bo"But your body says another!" with vpunch
                    ts"W-what the fuck are you doing you little shit!" with vpunch
                    bo"You practically had your ass hanging in front of me..."
                    bo"You expect me to believe you weren't asking for this?"
                    "Click twice to raise her skirt!"
                    $ ui.interact()
                    show screen parallax1280("ts_introfinal_4", 0.625) with dissolve
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                    ts"*Gasp*"
                    bo"You even know about my condition and yet..."
                    ts"You got the wrong idea, idiot!" with vpunch
                    bo"You shake your ass around and keep teasing me!"
                    menu menushakeyourassaround:
                        bo"You shake your ass around and keep teasing me!"
                        "{color=[hatredcolor]}Bad girl!{/color}":
                            call checkHatred(20, "menushakeyourassaround") from _call_checkHatred_11
                            bo"I know what you are..."
                            "Click twice to...!"
                            hide screen parallax1280
                            hide scrollingimage onlayer screens
                            
                            scene ts_introfinal_4:
                                zoom 0.7 xalign 1.0 yalign 0.5
                            with dissolve
                            call changeHatred(1) from _call_changeHatred_95
                            bo"You nymphomaniac whore-"
                            #ts_introfinal_spankhand
                            show ts_introfinal_spankhand with moveinright:
                                zoom 1.5 xalign 0.8 yalign 0.5
                            
                            with vpunch
                            $ renpy.sound.play("/audio/soun_fx/intro/spank5.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                            $ renpy.sound.play("/audio/soun_fx/intro/gruntwoman1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                            show ts_introfinal_6:
                                zoom 0.7 xalign 1.0 yalign 0.0
                            hide ts_introfinal_spankhand
                            with dissolve
                            ts"U-ah!" with vpunch
                            show screen parallax1280("ts_introfinal_6", 0.625) with dissolve
                            call showscrollingimage from _call_showscrollingimage_19
                            ts"Y-you...-"
                            call changeDominance(1) from _call_changeDominance_54
                            bo"I've heard the things you were whispering to yourself last time..."
                            bo"You depraved hag!"
                            "You left a small imprint through Tsunade's pantyhose as you slapped her ass with as much force as you could muster..."
                            call hidescrollingimage from _call_hidescrollingimage_23
                            scene black
                            ts"Get off m-me, little shit!" with vpunch
                            "Tsunade shoved you away and in an unexpected move..."
                            show tsunade intro with dissolve:
                                zoom 1.5 xalign 0.0 yalign 0.5
                            scene black with flash
                            "She jabbed you with a syringe. Presumably some sort of medicine to control your sudden impulses..."
                            scene bg infirmary room day
                            show boruto bonerevil4 at left 
                            show tsuna annoyed:
                                xalign 0.3
                            with dissolve
                            show tsuna:
                                easein 2 xalign 0.8
                            bo"W-what... did you do to me!"
                            show boruto bonersurprisedred at shake with dissolve:
                                subpixel True 
                                matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
                                linear 0.30 matrixcolor InvertMatrix(0.95)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.51)*HueMatrix(0.0) 
                                linear 0.55 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.05)*HueMatrix(0.0) 
                                linear 0.67 matrixcolor InvertMatrix(1.36)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.33)*HueMatrix(0.0) 
                                linear 1.00 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.00)*HueMatrix(0.0)
                            pause 1
                            show boruto bonersurprised with dissolve
                            show boruto bonersurprisedred with dissolve
                            show boruto bonersurprised with dissolve
                            show boruto bonersurprisedred with dissolve
                            show boruto bonersurprised with dissolve
                        
                            show tsuna annoyed at right with dissolve
                            ts"A tranquilizer... for your condition!"
                            ts"Have you finally calmed down?" with vpunch
                            bo"I... I am O-okay, I think..."
                            show boruto bonerevil2 with dissolve
                            bo"Although I am still hard as diamonds after all your teasing!"
                            show tsuna angry with dissolve
                            ts"I wasn't teasing you, you god-damned brat!" with vpunch
                            ts"I was testing you!" with vpunch
                            ts"And you failed... miserably!"
                            bo"W-what the hell are you on about you hag..."
                            scene black with dissolve
                            ts"*Sigh...*"
                            ts"Control your impulses, sit down, and I'll explain..."
                            jump tsunadeexplains

                        "{color=[dominancecolor]}Huh? Guess I got the wrong idea then...{/color}":
                            bo"Heh! Guess I got the wrong idea then..."
                            show screen parallax1280("ts_introfinal_1", 0.625) with dissolve
                            $ renpy.sound.play("/audio/soun_fx/grope2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                            call changeDominance(1) from _call_changeDominance_55
                            "You squeeze Tsunade's ass one last time before letting go..."
                            show screen parallax1280("ts_introfinal", 0.625) with dissolve
                            bo"Considering what happened last time, I thought you were teasing me..."
                            call hidescrollingimage from _call_hidescrollingimage_24
                            scene black with vpunch
                            ts"I wasn't teasing you, you god-damned idiot!" with vpunch
                            scene bg infirmary room day with dissolve
                            show boruto bonerevil at left with dissolve
                            show tsuna annoyed at right with dissolve
                            ts"I was testing you!" with vpunch
                            ts"And you failed... miserably!"
                            bo"W-what the hell are you on about you hag..."
                            scene black with dissolve
                            ts"*Sigh...*"
                            ts"Control your impulses, sit down, and I'll explain..."
                            jump tsunadeexplains
                            

                            

                    


                            
                        
                    
                "...Huh?":
                    bo"...Huh?"
                    bot"Did I misunderstood her intentions?"
                    call hidescrollingimage from _call_hidescrollingimage_25
                    scene black
                    ts"Enough!" with vpunch
                    "Tsunade pushes you away..."
                    scene bg infirmary room day with dissolve
                    show boruto bonersurprised at left with dissolve
                    show tsuna angry at right with dissolve 
                    ts"What were you thinking! You little runt!" with vpunch
                    bo"I mean, you kept swaying your booty around and scantily leaning forward..."
                    show boruto bonerevil with dissolve
                    bo"Excuse me if I thought that was you, teasing me!"
                    bot"Freaking hag!"
                    show tsuna annoyed with dissolve
                    ts"I wasn't teasing you, you god-damned idiot!" with vpunch
                    ts"I was testing you!" with vpunch
                    ts"And you failed... miserably!"
                    bo"W-what the hell are you on about..."
                    scene black with dissolve
                    ts"*Sigh...*"
                    ts"Control your impulses, sit down, and I'll explain..."
                    jump tsunadeexplains
                    
         
                



        "A-are you...":
            bo"T-tsunade... A-are you..."
            call hidescrollingimage from _call_hidescrollingimage_26
            scene ts_introfinal_1 with dissolve:
                yalign 0.0 xalign 0.4
            ts"...Huh? Am i what, [bo_name]?"
            scene ts_introfinal_2 with dissolve:
                yalign 0.0 xalign 0.4
            tst"There it is!" with vpunch
            scene bg infirmary room day with dissolve
            show boruto bonersurprised at left with dissolve
            show tsuna smug at right with dissolve 
            bo"The way you walk, the way you move, a-are you...-"
            "She cuts you off and pick the words right out of your mouth..."
            ts"...'Teasing me'?"
            show tsuna normal2 at right with dissolve
            ts"Of course not. I was merely... testing you."
            bo"T-testing me?"
            ts"Oh yes! And clearly evident by your... posture, you failed!"
            scene black
            bo"O-oh... My condition... I didn't mean to!" with vpunch
            ts"I know, I know..."
            ts"Control your impulses, sit down, and I'll explain..."
            
            jump tsunadeexplains
        
    

    



label tsunadeexplains:
    show bg tsunadeexplanation with dissolve
    "Tsunade takes a seat, holding the red package she picked up from earlier close to her."
    "She stares you down with an intimidating look..."
    ts"...Where do I even start!"
    ts"*Sigh*..."
    ts"Your [hin_rel_mother] has informed me of your progress. You should know, she sounded very concerned..."
    ts"I don't need to know the details as to why, but given your behavior just now, It easy to see why..."
    ts"It would seem your condition might prove more troublesome than initially thought, in more ways than one..."
    bo"What does that mean?"
    show bg tsunadeexplanation with dissolve:
        zoom 1.2 xalign 0.3 yalign 1.0
    ts"I am not even  sure if me telling you this is the right approach but..."
    ts"What I am holding here..."
    
    scene black with dissolve

    $ renpy.sound.play("/audio/soun_fx/heels1.opus", channel="sfx3", loop=False, relative_volume = 0.8)
    "Tsunade stands up and starts pacing around the office. You could sense some concern in her mannerisms..."
    "She takes some time to gather her thoughts before she starts addressing you..."
    ts"What if I told you that I am on the brink of the greatest scientific discovery of our lifetimes..."
    bo"I don't know a thing about science..."
    ts"What if I told you that, if I am correct, the world could experience a sudden, inequitable shift in power dynamics. One that would usher a new era for Konoha..."
    bo"...Huh?"
    ts"What if I told you that you and me, will be the ones responsible for forever altering the course of history!"
    bo"You sound like a damned looney, Tsunade. What's going on..."
    "Tsunade stops pacing and turns her attention to you..."
    scene ts_intro5 with fade:
        xalign 0.5 yalign 1.0
    show ts_intro5:
        easein 2.5 yalign 0.15
    "You understood from the look in her eyes, she meant her every word..."
    ts"I'll simplify, so that even you can understand..."

    show screen parallax1280("ts_intro5", 1.00) with dissolve
    call showscrollingimage from _call_showscrollingimage_20
    ts"We are on the precipice of greatness. The key that will let us peek beyond that precipice, lies in this little bag..."
    bo"You say that, but I still have no idea what it is that you are talking about..."
    bo"What's in the bag anyway...?"
    ts"[bo_name]..."
    ts"I am trusting you with this information because I know that deep inside, you are a good person, and you'll do what's right..."
    ts"Just like your Father and your [hin_rel_mother] did before you..."
    ts"I will let you in on my secrets, but you have to promise that this information will forever stay between the two of us..."
    bo"R-right..."
    ts"The two of us alone!" with vpunch
    ts"If any of this information falls in the wrong hands, your life, mine and even Konoha's existence, would be in grave danger..."
    ts"Danger that goes way beyond what you can comprehend!"
    ts"Do you understand the severity of our situation!?" with vpunch
    menu:
        ts"Do you understand the severity of our situation!?"
        "Yes Ma-am...":
            bo"I can tell this is important for you, you can trust me..."
            ts"Not just for me, [bo_name]. For everyone..."
        "Sure... (Meh... who cares!)":
            bo"Eeeh, sure..."
            bot"What could possibly matter this much..."
            ts"I need you take this seriously, [bo_name]. This goes much further than me, or you..."
    
    call hidescrollingimage from _call_hidescrollingimage_27
    scene black with dissolve
    ts"Are you ready to see what's inside?"
    scene bg infirmary room day
    show boruto surprised2 at left 
    show tsuna normal behind boruto:
        xalign 0.3
    with dissolve
    bo"...S-sure!"
    show tsuna:
        easein 2 xalign 1.0
    ts"Go on, open it..."
    $ renpy.sound.play("/audio/soun_fx/ominous_sound.opus", channel="sfx3", loop=False, relative_volume = 1.5)
    show cumcontainer:
        subpixel True
        xalign 0.5 ypos 50
        blur 20
        alpha 0.5
        zoom 0.2
        easein 4 blur 0 zoom 0.4 alpha 0.9
    bo"...Huh?"
    bo"It's just a glass container..."
    bo"With some gooey looking liquid..."
    show tsuna serious with dissolve
    ts"Not just any liquid, [bo_name]..."
    ts"Through my experiments I've discovered that this liquid has incomprehensibly powerful properties..."
    ts"If I can just conclude my hypothesis and prove that it's usage can be safely tested-"
    bo"Hold on! H-how does any of this have anything to do with me..."
    ts"Last time we met... you had a little incident, remember?"
    bo"You don't mean to tell me..."
    bo"This is m-my...?"
    ts"Mhm..."
    show cumcontainer:
        easeout 0.4 ypos 1000
    $ renpy.sound.play("/audio/soun_fx/glasssmash.opus", channel="sfx3", loop=False, relative_volume = 0.4)
    show boruto surprised3
    pause 0.2
    show tsuna angry with dissolve
    bo"C-CUM?" with vpunch
    ts"Y-you...!"
    show tsuna angry2 with dissolve
    ts"*Sigh*... F-freaking idiot..."
    ts"I just told you how important that was!"
    menu:
        ts"I just told you how important that was!"
        "Apologize":
            bo"I a-am s-sorry, I j-just..."
            call changetsunadedominance(3) from _call_changetsunadedominance_23
        "{color=[dominancecolor]}You can always get more!{/color}":
            show boruto sceeming2 with dissolve
            call changeDominance(1) from _call_changeDominance_56
            bo"You could always extract more, you know..."
            bot"Heh!"
            call changetsunadedominance(-3) from _call_changetsunadedominance_24
            show tsuna at smallshake
            ts"What happened last time is never occuring again!"
        
    show tsuna annoyed with dissolve
    show tsuna at smallshake
    ts"Whatever, I suppose you owe me another sample..."
    show tsuna:
        easein 1 xalign 0.5
    ts"Here, take this container..."
    show halfblack with dissolve
    "Tsunade needs your semen to conduct further experimentation and prove her hypothesis."
    "Providing substantial amounts to her can lead to breakthrough scientific discoveries that can have strong implications for your future!"
    "And perhaps, even the future of those around you..."
    $ notification ("Infirmary menu unlocked")
    show screen infirmarymenutopright with dissolve
    show expression FocusEffect("idle1", 1160, 50, 125, 0.7) as focus_effect onlayer screens with dissolve
    "Use the infirmary menu located at the top right of the screen to track your progress!"
    hide focus_effect  onlayer screens with dissolve
    "Tsunade is quite authoritative in nature, but given her over-reliance to you and your valuable commodity..."
    "Perhaps that is something you can change..."
    "Tsunade's demeanor will change based on your actions during your encounters!"
    hide halfblack with dissolve
    "Tsunade hands you an empty container..."
    show boruto normal with dissolve
    bo"What am I supposed to do with this..."
    show tsuna normal at right with dissolve
    ts"You know very well what I expect you to do..."
    $ renpy.end_replay()
    default tsunadeintroductionseen = False
    $ tsunadeintroductionseen = True
    jump infirmary_tsunademenu
    
        



    
init python:
 
    def close_infirmarymenu():
        renpy.hide_screen("infirmarymenu")
        renpy.hide_screen("test_tsunade")
        renpy.hide_screen("displayTextScreen")




screen infirmarymenutopright():
    imagebutton:
        xalign 0.98 yalign 0.02
        auto "images/ui/workmenu2_%s.webp"
        hovered Show("displayTextScreen", displayText = "Open Infirmary Menu")
        unhovered [Hide("displayTextScreen")]
        action [SetVariable("selected_infirmarymenu", "Tsunade"),Show("infirmarymenu")]
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"

default selected_infirmarymenu = "Tsunade"
screen infirmarymenu():
    
    
    default dropdown_open = False
    zorder 100

    

    key "mouseup_3" action [Hide("infirmarymenu"),Hide("test_tsunade"), Hide("displayTextScreen")] #close with rightclick
    
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
            action [Function(close_infirmarymenu)]

        #left selection menu
        vbox:
            xalign 0.05 yalign 0.2
            text "Menu" xalign 0.5 size (50 if renpy.variant("pc") else 40)
        vbox:
            
            xalign (0.05 if renpy.variant("pc") else 0.02) yalign (0.5 if renpy.variant("pc") else 0.55)
            spacing 30
            #Tsunade
            textbutton "Tsunade":
                xalign 0.5
                hover_sound "audio/soun_fx/select2.opus"
                activate_sound "audio/soun_fx/select4.opus"
                hovered Show("displayTextScreen", displayText = "Open Tsunade's panel")
                unhovered Hide("displayTextScreen")
                action SetVariable("selected_infirmarymenu", "Tsunade")
            #skill tree
            textbutton "Discoveries":
                xalign 0.5
                hover_sound "audio/soun_fx/select2.opus"
                activate_sound "audio/soun_fx/select4.opus"
                hovered Show("displayTextScreen", displayText = "Open Discoveries panel")
                unhovered Hide("displayTextScreen")
                action SetVariable("selected_infirmarymenu", "Discoveries")
            # #unlockabkles
            # textbutton "Rewards":
            #     xalign 0.5
            #     hover_sound "audio/soun_fx/select2.opus"
            #     activate_sound "audio/soun_fx/select4.opus"
            #     hovered Show("displayTextScreen", displayText = "Open Rewards panel")
            #     unhovered Hide("displayTextScreen")
            #     action SetVariable("selected_infirmarymenu", "rewards")
            # #tutorial
            # textbutton "Tutorial":
            #     xalign 0.5
            #     hover_sound "audio/soun_fx/select2.opus"
            #     activate_sound "audio/soun_fx/select4.opus"
            #     hovered Show("displayTextScreen", displayText = "Open Tutorial panel")
            #     unhovered Hide("displayTextScreen")
            #     action SetVariable("selected_infirmarymenu", "tutorial")

        #images of characters + outfits
        vbox:
            #Yoru
            xalign 1.0 yalign 0.5
            if selected_infirmarymenu ==  "Tsunade":
                add "/images/v2/tsunade_revisit/headshots/tsunade full.webp" at dissolvehack:
                    zoom 0.7



        if selected_infirmarymenu == "Tsunade":
            vbox:
                xalign 0.4 yalign 0.4
                text "Name: Tsunade" xalign 0.5
                text "Affiliation: Doctor" xalign 0.5
                text "Age: Unknown" xalign 0.5
                text "Relationship: Complicated" xalign 0.5
                null height 40 #add space
                frame:
                    xalign 0.65 yalign 0.53
                    background "#d3d3d320"
                    vbox:
                               
                        text "Your relationship with Tsunade" xalign 0.5
                        text "Will be dictated by what actions" xalign 0.5
                        text "you take during your encounters." xalign 0.5
                        null height 20 #add space
                        use center_balance_bar

                        if renpy.has_screen("test_tsunade"):
                            hbox:
                                xalign 0.5
                                textbutton "-":
                                    action SetVariable("tsunadedominance", tsunadedominance - 10)
                                    hover_sound "audio/soun_fx/select2.opus"
                                    style "small_button"
                                    hovered Show("displayTextScreen", displayText = "Decrease Tsunade's demeanor by 10")
                                    unhovered Hide("displayTextScreen")
                                textbutton "+":
                                    action SetVariable("tsunadedominance", tsunadedominance + 10)
                                    hover_sound "audio/soun_fx/select2.opus"
                                    style "small_button"
                                    hovered Show("displayTextScreen", displayText = "Increase Tsunade's demeanor by 10")
                                    unhovered Hide("displayTextScreen")
                
            
   
        #right screen descriptions
        elif selected_infirmarymenu == "Discoveries":
            vbox:
                xalign (0.5 if renpy.variant("pc") else 0.7)
                yalign (0.4 if renpy.variant("pc") else 0.4)
                text "Tsunade is conducting experiments with your semen."
                text "Providing her with enough quantities can help"
                text "her uncover new scientific discoveries."
                text "Semen extracted: [semenquantity:.2f] mL" color "#00FF00"
                null height 50 #add space
                text "Discoveries:"
                if tsunade_discovery_seen == True:
                    frame:
                        background "#d3d3d320"
                        vbox:
                            text "(30) Biological alteration capabilities." color "#00FF00" # Yellow color for discovery title
                            text "??? (WIP)"
                            text "??? (WIP)"
                else:
                    text "No significant discoveries made yet." color "#FFA500" # Orange color for no discovery
                    text "Maybe if more semen is extracted..." color "#FF0000"
                    frame:
                        background "#d3d3d320"
                        vbox:
                            text "???"
                            text "??? (WIP)"
                            text "??? (WIP)"

                      