 #intro followup after waking up
label after_asleep:
    scene bg lr night with fade:
        zoom 0.67
    show boruto smirk at left with dissolve
    bo"I am sorry [hin_rel]. I overslept again..."
    show shina angry2 at right with dissolve:
        xzoom(-1)
    hin"Why you..."
    show boruto embarassed with dissolve
    bo"Hehe! *Nervous Laughter*"
    show shina assertive at right with dissolve
    hin"Come on [bo_name]..."
    hin"It's always the same story with you isn't it?"
    bo"What can I say... it just happens."
    show boruto surprised2 with dissolve
    bot"I can't bring up what I dreamt about of course, but..."
    menu:
        bot"I can't bring up what I dreamt about of course, but..."
        "[hin_rel], is everything okay?":
            show boruto suspicious with dissolve
            bo"This might be abrupt, but uhm... how are you feeling [hin_rel]? Is everything okay?"
            hin"Huh? Where is this coming from, [bo_name]?"
            menu:
                hin"Huh? Where is this coming from, [bo_name]?"
                "I am just worried about you...":
                    show boruto worried2 with dissolve
                    bo"I am just worried about you [hin_rel]..."
                    bo"With [na_rel] being away and us not talking much as of late..."
                    show boruto smirk2 with dissolve
                    bo"I thought I'd ask, you know? Make sure the best [hin_rel] in the world is holding herself up!"
                    show shina concerned with dissolve
                    show boruto worried2 with dissolve
                    call changeRespect("Hinata") from _call_changeRespect_70
                    hin"[bo_name]..."
                    show shina shy2 with dissolve
                    hin"Come on! You worry too much about me and too little about yourself!"
                    show shina smiling with dissolve
                    hin"Everything's fine, I promise! Now you better focus on taking care of yourself, alright?"

                "Nevermind...":
                    show boruto embarassed with dissolve
                    bo"Nevermind! I just thought I'd ask..."
                    show shina normal with dissolve
                    hin"Hmm...? I am okay [bo_name], don't spend your days worrying about me..."
                
        "I just had a bad lucid dream...":
            show boruto suspicious with dissolve
            bo"I just had a bad lucid dream. I wanted to wake up but..."
            show shina shy with dissolve
            hin"Another one of those. huh?"
            hin"You used to talk in your sleep all the time when you were younger..."
            show shina serious with dissolve
            hin"I though you grew out of it but..."
            show shina smiling with dissolve
            hin"It seems that'll be your curse to bear!"
            bo"My curse... huh?"
            hin"Don't worry too much about it, there's worse things in life than lucid dreams."
            show boruto worried2 with dissolve
            bot"I wonder [hin_rel], would you say the same thing if you knew what my dream was about?"

        
    show shina serious
    show boruto suspicious
    with dissolve
    $ renpy.sound.play("/audio/soun_fx/hinata/hinatasigh2.opus", channel="sfx2", loop=False, relative_volume = 0.3)
    hin"*Sigh*"
    show shina shy with dissolve
    hin"In any case, please hurry to the grocery store and pick up a few things for me, will you?"
    call changeMoney(15) from _call_changeMoney_1
    show shina normal with dissolve
    hin"You will need this..."
    hin"Now make haste! You don't have much time."
    show boruto normal with dissolve
    bo"Right on it, sorry again."
    show boruto normal:
        easeout 1 xpos -500
    bo"I'll see you soon!"
    show shina shy at center with dissolve:
        zoom 1.3 yalign 0.2
    hin"And [bo_name_stutter]..."
    bo"Y-yeah...?"
    show shina worried with dissolve
    hin"Stay safe out there... alright? You and your [him_rel] is all I have left."
    bo"Of course, [hin_rel]... Love ya!"
    show shina smiling with dissolve
    hin"Thanks for looking out for me!"
    hide shina with dissolve
    scene black with dissolve
    "You make your way to the door."
    "..."
    scene bg lr night with vpunch:
        zoom 0.67
    show hima smug at right with dissolve:
        zoom 0.335
    him"Hold it right there, you spiky haired twat."
    show boruto angry at left with dissolve
    him"Where are you off to this time?"
    hin"[him_name]! Language!"
    $ renpy.sound.play("/audio/soun_fx/himawari/himascoff1.opus", channel="sfx2", loop=False, relative_volume = 0.4)
    him"Hmph!"
    menu boruto_hima_reply1:
        bot"[him_name] is at it again. I should..."
        "Reply calmly":
            $ hima_shop = True
            show boruto worried with dissolve
            bo"[him_name] please, is the name-calling necessary you little rascal?"
            show hima smug1 with dissolve:
                zoom 0.335
            him"Absolutely it is."   
            show boruto normal with dissolve
            bo"I am just going to pick up a few things for [hin_rel]."
            bo"You need anything?"
            show hima surprised with dissolve:
                zoom 0.335
            $ renpy.sound.play("/audio/soun_fx/himawari/SWFBreath21.opus", channel="sfx2", loop=False, relative_volume = 1.4)
            him"O-oh, I..." with vpunch
            show hima shy with dissolve:
                zoom 0.335
            himt"Since when does this idiot think of anyone but himself..."
            him"Just get me a few of my favourite snackies..."
            show hima smug1 with dissolve:
                zoom 0.335
            call changeRespect("Himawari", 1, "none") from _call_changeRespect_71
            him"Your treat of course!"
            $ renpy.sound.play("/audio/soun_fx/himawari/loserlaugh.opus", channel="sfx2", loop=False, relative_volume = 0.4)
            him"Teehee!"
            show boruto smirk with dissolve
            bo"On it, you devil spawn"
            scene black with dissolve
        "Reply aggressively":
            $ hima_shop = False
            show boruto angry2 with dissolve
            call changeDominance(1, "none") from _call_changeDominance_16
            bo"It's none of your damn business you little bitch!"
            bo"You better stop with the name-calling or there will be consequences." with vpunch
            call changeRespect("Hinata", -1, "none") from _call_changeRespect_72
            hin"[bo_name_stutter]!" with vpunch
            scene black with vpunch
            $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx2", loop=False, relative_volume = 0.4)
            "You slam the door behind you and storm off before either girl can get a word out..."
            "Through the door you hear [him_name] say..."
            call changeRespect("Himawari", -1, "none") from _call_changeRespect_73
            $ renpy.sound.play("/audio/soun_fx/himawari/loserlaugh.opus", channel="sfx2", loop=False, relative_volume = 0.4)
            him"Hahahaha! Consequences he says, funny guy isn't he, [hin_rel]?"
            bot"Stupid bitch... her time will come."
            hin"[him_name] please, I know your [him_rel_to_bo] can be annoying at times, but have some poise yourself."
            show boruto surprised at left with dissolve
            show boruto at smallshake
            bot"And even [hin_rel] is taking her side..."
            menu:
                bot"And even [hin_rel] is taking her side..."
                "{color=[hatredcolor]}Hold it against her{/color}":
                    show boruto sad with dissolve
                    bot"If [hin_rel] is taking her side behind my back..."
                    show boruto angry2 with dissolve
                    call changeHatred(1, "none") from _call_changeHatred_27
                    call borutoevil from _call_borutoevil_1
                    bot"I will make sure both of them live to regret that."
                    show boruto worried2 with dissolve
                    bot"And here I thought [hin_rel] was in my corner... Did she really just call me annoying?"
                    

                    
                "Be considerate":
                    show boruto sad2 with dissolve
                    call changeHatred(-1,"none") from _call_changeHatred_28
                    bot"[hin_rel] is not entirely wrong I suppose. I can be better, I will be better, if not for my dumb [him_rel], then at least for her."
                
        "Be respectful":
            
            show boruto normal with dissolve
            bo"[him_name], can you stop with the names? Need I remind you I am your older [him_rel_to_bo]?"
            show hima smug1 with dissolve
            him"You are as much of an older [him_rel_to_bo] to me as a typewriter is older to a phone"
            him"Antiqued and inferior in every way!"
            show boruto sad with dissolve
            bo"*Sigh"
            show boruto suspicious with dissolve
            bo"I won't stoop that low [him_name]. In any case..."
            show boruto normal with dissolve
            bo"I am picking up a few things for [hin_rel]."
            show hima smug2 with dissolve
            him"Get me some snackies too and maybe I'll consider upgrading you from a typewriter to a printer or something..."
            menu:
                bot"*Sigh... This damn girl..."
                "I will consider it":
                    $ hima_shop = True
                    call changeRespect("Himawari", 1, "none") from _call_changeRespect_74
                    bo"I'll see to it if I have some spare money..."
                    
                    $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                    show hima smug3 with dissolve
                    him"Hmph! You cheapskate..."
                "Don't think I will":
                    $ hima_shop = False
                    show boruto angry with dissolve
                    bo"With the way you are acting? Not a chance in hell, you brat."
                    $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                    him"Hmph! Cheapskate..."
                    show hima turn1 with dissolve:
                        zoom 0.45
                    call changeRespect("Himawari", -1, "none") from _call_changeRespect_75
                    him"I expected nothing more from your sorry ass..."
                    him"I am out of here!"
                    show hima:
                        zoom 0.6
                    show halfblack behind hima
                    with dissolve
                    window hide
                    pause 1
                    window show
                    show boruto sceeming
                    hide halfblack
                    with dissolve
                    show hima with dissolve:
                        zoom 0.45
                    bot"This damned girl... all she has going for her is her freaking ass."
                    
                    show hima at center with easeinright
                    
                    
                    
                    menu:
                        bot"..."
                        "Fire back":
                            call changeDominance(1, "none") from _call_changeDominance_17
                            show boruto sceeming2 with dissolve
                            bo"You keep this atittude up and it is your ass that's going to be sorry, you damn brat!"
                            him"Ooooh... I am so scared!"
                            $ renpy.sound.play("/audio/soun_fx/himawari/loserlaugh.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                            him"I am shiverring I am telling you!"
                            show hima:
                                pause 0.5
                                linear 1.5 xpos -0.5
                            show boruto surprised2 with dissolve
                            him"I better run before I poop my panties! Teehee!"
                            call changeRespect("Himawari", -1, "none") from _call_changeRespect_76
                            show boruto angry with dissolve
                            bot"I will get back to her some day..."
                        "Stay silent":
                            $ renpy.sound.play("/audio/soun_fx/himawari/loserlaugh.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                            hide hima with easeoutleft
                            show boruto worried with dissolve 
                            bot"I would rather not make things worse..."

                        
                        
    

    scene black with dissolve
    play sound "audio/soun_fx/dooropen.opus" volume 0.7
    "[bo_name] heads out"
    show bg intro2n with dissolve:
        zoom 0.69
    stop music fadeout 5

    show boruto normal at center with dissolve
    bo"*Sigh...*"
    bo"I have gotten myself into a shitty situation. My [him_rel] has no respect for me and acts like a spoiled brat."
    show boruto sad2 with dissolve
    bo"And [hin_rel]... I can feel her pulling further away lately."
    show boruto sad with dissolve
    bo"To be fair, after the last Shinobi War, I haven't had the drive to either keep training or working. It just feels like there's no point in any of it."
    show boruto normal with dissolve
    bo"I will have to change my outlook if I care about maintaining a good relationship with them."

    scene black with dissolve
    "You made your way to the local convenience store..."

    #store cg
    scene bg conv store with dissolve
    bo"Now to pick up the things [hin_rel] asked me to..."
    menu:
        "..."
        "Buy groceries ({color=#85bb65}-$15{/color})":
            call changeMoney(-15) from _call_changeMoney_2
            bot"There goes most of my money..."
            bot"I am left with $[money] to my name. Heh!"
            bot"I should probably look for a job or something."
            
      
    if hima_shop == True:
        menu:
            bot"Come to think of it, [him_name] did ask for something too..."
            "Buy her favorite snacks ({color=#85bb65}-$5{/color})":
                call checkMoney(5, "himawaridontbuy") from _call_checkMoney
                $ hima_shop_bought = True
                call getItem(snacks, 1) from _call_getItem_2
                
                bot"Aaaaand now I am totally broke."
                bot"And for what... A spoiled little [him_rel]? Hopefully she at least appreciates the gesture."
            "Ignore her request":
                $ hima_shop_bought = False
                bot"But I don't think I care to be honest. Not with the way she acts at least."
                label himawaridontbuy:
                    $ hima_shop_bought = False
                    bot"Spoiled brat... why would I spend any money on her anyway?"
    scene black with dissolve
    bot"Better make my way back home..."
    bot"I already messed up with oversleeping. Wouldn't want to upset [hin_rel] any more..."

    scene bg intro with fade
    $ renpy.music.play("/audio/soun_fx/rain.opus", channel="sfx1", synchro_start=True, fadein=1)
    show boruto surprised2 with dissolve
    bo"The rain from before... It's back again."
    show boruto embarassed with dissolve
    bo"And the concept of an umbrella still elludes me..."
    scene black with dissolve
    "[bo_name] was approaching his home when..."

    play sound"/audio/soun_fx/heartbeat.opus" volume 1.4
    play music"/audio/ost/evilhymn.opus" volume 1.0
    "."
    play sound"/audio/soun_fx/heartbeat.opus" volume 1.8
    ".."
    play sound"/audio/soun_fx/heartbeat.opus" volume 2.2
    "...!"

    scene bg intro
    show boruto redpain with vpunch
    $ renpy.music.play("/audio/soun_fx/horror.opus", channel="sfx2", synchro_start=True, loop=False)
    show boruto pain with dissolve
    show boruto at smallshake
    bo"This... pain... It's the same as before!"
    show boruto redpain with dissolve
    play sound"/audio/soun_fx/heartbeat.opus" volume 2.5
    play sound("/audio/soun_fx/rain.opus") loop fadein 1.0

    show boruto pain2 with dissolve
    play sound"/audio/soun_fx/heartbeat2.opus" volume 2.8
    bo"Argh!" with vpunch
    show boruto at shake
    
    show boruto pain2 with dissolve:
        matrixcolor InvertMatrix(1.84)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0)
    play sound"/audio/soun_fx/heartbeat.opus" volume 2.8
    bo"What the fuck is going on! The p-pain, it's so intense!"
    show boruto redpain:
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 


    play sound"/audio/soun_fx/heartbeat.opus" volume 3.0
    show boruto at smallshake
    bo"Aaaaargh!!" with hpunch
    play sound"/audio/soun_fx/heartbeat.opus" volume 2.8
    show boruto aura at dizzyflash
    with flash
    
    "An abrupt pain rippled throughout [bo_name]'s body. A feeling similar to that of a sensory overload would put him into what seemed like a temporary state of paralysis."
    "In that moment, while his consciousness would stay intact..."
    call increaselust pass (10) from _call_increaselust_37
    
    "Something else would awaken inside of him..."




    
    show boruto aura angry with dissolve:
        zoom 1.1 xalign 0.5 yalign 0.5
    window auto hide
    camera at Shake((0, 0, 0, 0), 2, dist=20, peak_time=0.6, smoothness=40):
        subpixel True 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.30 matrixcolor InvertMatrix(0.95)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.51)*HueMatrix(0.0) 
        linear 0.55 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.05)*HueMatrix(0.0) 
        linear 0.67 matrixcolor InvertMatrix(1.36)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.33)*HueMatrix(0.0) 
        linear 1.00 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.00)*HueMatrix(0.0) 
    with Pause(2.62)
    camera:
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.00)*HueMatrix(0.0)
    window auto show
    bo"The p-pain... it's... growing s-stronger."
    scene boruto aura restrain with flash
    $ renpy.sound.play("/audio/soun_fx/bassstart.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    show boruto_intro_t at dizzy2 with dissolve:
        zoom 2.2 xalign 0.3 yalign 0.3
    with flash
    
    bo"Aaaaargh!!!" with vpunch
    bo"My f-fucking head...!" with vpunch
    bo"It's a-about to... f-fucking explode!" with vpunch
    window hide
    hide boruto_intro_t
    show boruto_intro_final:
        zoom 2.2 xalign 0.3 yalign 0.3
    $ renpy.transition(dissolve)
    $ renpy.sound.play("/audio/soun_fx/wakeup.opus", channel="sfx3", loop=False, relative_volume = 1.6)
    $ renpy.pause(.5, hard=True)
    with Shake((0, 0, 0, 0), 1.7, dist=40, peak_time=0.7, smoothness=50)
    hide boruto_intro_final
    scene boruto aura restrain2 with flash:
        zoom 2.4 xalign 0.3 yalign 0.3
    $ renpy.sound.play("/audio/soun_fx/eyesharingan2.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    show screen endof_prerelease with flash
    scene black with flash
    bo"!"
    play sound"/audio/soun_fx/heartbeat2.opus" volume 1.5
    "."
    play sound"/audio/soun_fx/heartbeat2.opus" volume 2.3
    ".."
    play sound"/audio/soun_fx/heartbeat2.opus" volume 3.0
    "..."



    #pre-release


    scene boruto boner with fade
    bo"I can't... control... my..."
    bo"Aargh! I need..."
    bo"I need someone... anyone!"
    scene boruto aura restrain2 at dizzy with dissolve
    "It was as if the entirety of [bo_name]'s senses where converging around his pelvic area. The accumulation of pain and oversensitivity sent [bo_name] into an almost feral like frenzy..."
    bo"I... I h-have to..."
    call increaselust pass (20) from _call_increaselust_38
    bo"I need to expel my urges! The desire is irresistible, it's... unbearable!"
    
    scene boruto aura restrain2 with dissolve
    $ renpy.sound.play("/audio/soun_fx/bassstart.opus", channel="sfx2", loop=False, relative_volume = 0.9, fadein = 0.05)
    scene boruto_intro_finalclean:
        zoom 2.2 xalign 0.3 yalign 0.3
    bo"Aaaaargh!!!" with vpunch
    show halfblack with dissolve
    dev"An important note from the developer:"
    dev"This is the very first scene I've worked on when I started developing HoS. Since then, my workflow and consistency has improved immensely."
    dev"Be warned that the following sequence might be lacking in quality until I eventually rework/scrap it."
    dev"As a side-note, 3rd person narration is used momentarily to detach the player from the actions the MC is 'involuntarily' about to make."
    dev"If you don't want [bo_name] to act like a piece of shit, choose the relevant options! Otherwise, indulge your depravity..."
    hide halfblack with dissolve
    scene black with dissolve
    "Almost entirely consumed by the pain of this inexplicable condition, [bo_name] maniacally looked around in beast-like fashion..."
    "Anything and everything around him could prove to be the remedy of his condition if it could be used as means of expelling his uncontainable desires..."
    "Hoping that in doing so, the immense pain he was experiencing would subdue."
    scene black with dissolve
    show boruto looking with dissolve:
        zoom 1.2 yalign 0.0 xalign 0.84
    "[bo_name]'s eyes locked on to someone he recognized..."
    label inointroscene:
    $ initialize_replay_defaults()
    scene ino sitting with fade
    "A neighboring woman, sitting idly under a small structure covering herself from the rain, utterly unaware of what was occurring within him."
    "[bo_name] erratically approached towards her direction..."
    bo"Ino... You..."
    bo"You will have to do!"
    call increaselust pass (30) from _call_increaselust_39
    "Yamanaka Ino, a retired Kunoichi and a close colleague and friend of [bo_name]'s [hin_rel]. She is about the same age as [hin_name] and have kept close ties with her throughout the years."
    "Blissfully unaware of what was occurring within [bo_name], Ino saw him approaching in a strange fashion, but had no reason to suspect his ill-nature, as he was a well known character to her, incapable of evil."
    "As [bo_name] got closer, Ino noticed his agitated demeanor. She assumed a more defensive stance..."
    scene ino sitting 2 with fade
    ino"[bo_name], you seem strange, everything okay?"
    "Hearing Ino's voice, [bo_name] hesitated for a second..."
    
    menu:
        "Hearing Ino's voice, [bo_name] hesitated for a second..."
        "{color=[hatredcolor]}Let your unreasonable temptations consume you.{/color}":
            scene black with fade
            $ renpy.sound.play("/audio/soun_fx/eye4s.opus", channel="sfx3", loop=False, relative_volume = 0.5)    
            show kurama1 with flash
            show kurama1:
                easein 2 alpha 0.0
            beast"Yes... Yes! Let me in, human!"
            $ renpy.sound.play("/audio/soun_fx/intro/gruntwoman2.opus", channel="sfx2", loop=False, relative_volume = 0.5)      
            "[bo_name] lunged at her..."
            scene ino sitting 3 with dissolve and vpunch
            call changeHatred(1) from _call_changeHatred_29
            call increaselust pass (60) from _call_increaselust_40
            "You grabbed one of her arms and violently pulled her off her seat..." with vpunch   
            "Ino, while a capable Kunoichi back in her active days, was utterly powerless in this moment. As much as she tried to pull away..."
            "It would quickly become apparent to her, that [bo_name]'s unusual strength, perhaps a side-effect of his current condition, would prohibit any attempts of escape."
            ino"[bo_name], what the hell are you doing. P-please... let me go! It hurts!"
            bo"Shut up, Ino."
            bo"You... you will relieve me from this pain."
            ino"[bo_name]... what the hell are you saying? Have you gone insane!? This isn't like you!"
            ino"P-please... *Whimpers*"
            menu:
                ino"P-please... *Whimpers*"
                "{color=[hatredcolor]}Abuse her{/color}":
                    scene bg ino with dissolve
                    show inograb 1 with vpunch:
                        zoom 0.6 xalign 0.5 yalign 0.5
                    "You take hold of both of her arms and firmly hold them behind her back..."
                    ino"Ouch, that hurts! [bo_name] I beg you, stop!"
                    bo"I can't, Ino!"
                    scene bg ino with dissolve
                    show boruto boner2t with dissolve
                    bo"Just... keep quiet and let me rid myself from this pain..."
                    ino"W-what are you d-doing!?"
                    bo"You better stay silent..."
                    show boruto boner3t with dissolve
                    bo"Or else..."
                    ino"[bo_name_stutter]! P-PLEASE!"
                    show boruto boner4t with dissolve
                    bo"This will get much worse!"
                    hide boruto with dissolve
                    "Yanking her arms, you pulled Ino closer to you..."
                    window hide
                    show inograb 2 with vpunch:
                        zoom 0.6 xalign 0.5 yalign 0.5
                    pause 1
                    window show
                    "And pushed your cock against her ass while forcibly grinding it on her wet skirt..."
                    ino"PLEASE!"
                    ino"S-SOMEONE! HEEEELP!!"
                    "In your somewhat conscious state of mind, you knew that if someone caught wind of what was happening, you could be in deep trouble."
                    
                    menu inoexclusivemenu:
                        "You tried to silence Ino's pleads by..."
                        "Giving her a commanding spank":
                            $ inospank = True
                            $ inohair = True
                            hide inograb 1 with dissolve
                            show inospank 2 with dissolve:
                                zoom 0.8
                                xalign 0.5 yalign 0.3
                            "You let go of her arm, instead taking hold of her ponytail and pulling on it harshly in a way that forced Ino to bend her kness, hoping to alievate some of the pressure you were putting on her."
                            ino"*Squeals"
                            ino"P-please... s-stop!"
                            "Consumed by your lust, you raised her skirt up and..."
                            
                            show inospank 3 with dissolve
                            $ renpy.sound.play("/audio/soun_fx/intro/spank5.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                            ino"Kyaaaa!" with vpunch
                            pause(0.5)
                            show inospank 4 with dissolve
                            bo"Take that!"
                            "Ino let out a loud squeel, as you slapped her ass with enough force, so that a visible bruise would form..."
                            bo"The more you scream, the worse it will get, understood?"
                            "Fear withholding her actions, Ino could not speak a word. All she could do was sob, letting out only occasional convulsing gasps"
                            ino"*Sobbing"
                            default inospankmenu1 = False
                            label punishino:
                                menu:
                                    
                                    "Did [bo_name] find some twisted pleasure in breaking Ino's character?"
                                    "Spank again" if inospankmenu1 == False:
                                        $ inospankmenu1 = True
                                        $ inospank = True
                                        bo"Another one, for good measure..."
                                        $ renpy.sound.play("/audio/soun_fx/intro/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                        show inospank 3 with vpunch
                                        pause(0.5)
                                        
                                        show inospank 4 with dissolve
                                        ino"*Sobbing"
                                        ino"N-no more... P-please!"
                                        jump punishino

                                    "Lower fishnets":
                                        bo"It's time I get a closer look Ino."
                                        bo"Don't panic, I will be quick..."
                                        show inospank 5 with dissolve:
                                            zoom 0.9
                                        ino"NOOOO, PLEASE!!"
                                        ino"LET ME GO!!"
                                        "Understanding that [bo_name] had nefarious intentions, Ino started panicking." 
                                        "She screamed and flailed her arms around trying to prevent what was about to happen."
                                        "But you had a firm grip on her ponytail. There was nothing she could do."
                                        "The more she tried to get away, the more painful it would get for her."
                                        menu :
                                            "..."
                                            "Shut her up":
                                                bo"Did I not tell you to..."
                                                scene bg ino with dissolve
                                                show ino_shutup 1 with dissolve:
                                                    zoom 0.6 xalign 0.5 yalign 0.5
                                                show ino_shutup_spank0 with moveinright:
                                                    zoom 0.6 xalign 0.5 yalign 0.5
                                                hide ino_shutup_spank0
                                                $ renpy.sound.play("/audio/soun_fx/intro/spank4.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                show ino_shutup_spank with vpunch:
                                                    zoom 0.6 xalign 0.5 yalign 0.8
                                                bo"SHUT!"
                                                pause(0.5)
                                                hide ino_shutup_spank with dissolve
                                                show ino_shutup 2 with dissolve:
                                                    zoom 1.4 xalign -0.3 yalign 0.2
                                                ino"AAAW!"
                                                show ino_shutup 2 with dissolve:
                                                    zoom 0.6 xalign 0.5 yalign 0.5
                                                $ renpy.sound.play("/audio/soun_fx/intro/spank7.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                show ino_shutup_spank with vpunch:
                                                     zoom 0.6 xalign 0.5 yalign 0.8
                                                bo"THE FUCK!."
                                                pause(0.5)
                                                hide ino_shutup_spank with dissolve
                                                show ino_shutup 3 with dissolve:
                                                    zoom 1.4 xalign -0.3 yalign 0.2
                                                ino"AWWW!! STOP!"
                                                show ino_shutup 4 with dissolve:
                                                    zoom 0.6 xalign 0.5 yalign 0.8
                                                $ renpy.sound.play("/audio/soun_fx/intro/spank5.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                show ino_shutup_spank with vpunch:
                                                     zoom 0.6 xalign 0.5 yalign 0.8
                                                bo"UP!!!"
                                                pause(0.5)
                                                hide ino_shutup_spank with dissolve
                                                show ino_shutup 4 with dissolve:
                                                    zoom 1.4 xalign -0.3 yalign 0.2
                                                ino"STOP! Y-YOU FUCKING MONSTER!!"
                                                show ino_shutup 4 with dissolve:
                                                    zoom 0.6 xalign 0.5 yalign 0.8
                                                "Ino's morbid screams kept echoing through the streets, was there really no one around?"
                                                "Her eyes started rolling up as she was on the brink of unconsciousness, the pain quickly becoming overwhelming."
                                                bo"Stupid bitch, I told you it would get worse the louder you get."
                                                bo"And yet... you keep on screeching!"
                                                menu :
                                                    bo"..."
                                                    "Slap her face":
                                                        $ inospank = True
                                                        bo"I have had enough of your squeeling!"
                                                        show ino_shutup 4 with dissolve:
                                                            zoom 1.4 xalign -0.3 yalign 0.2
                                                        bo"Maybe this will get you to shut the fuck up!"
                                                        show ino_faceslap with moveinleft:
                                                            zoom 2.5 xalign +15 yalign 0.2
                                                        $ renpy.sound.play("/audio/soun_fx/intro/spank4.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                        with vpunch
                                                        show ino_shutup slap1 with dissolve:
                                                            zoom 1.4 xalign -0.3 yalign 0.2
                                                        pause 0.1
                                                        hide ino_faceslap with dissolve
                                                        ino"Ugh..."                                                       
                                                        "Ino let out one last measly squeel..."
                                                        show ino_shutup slap2 with dissolve:
                                                            zoom 1.4 xalign -0.3 yalign 0.2
                                                        "Her eyes started rolling up..."
                                                        scene bg ino with dissolve
                                                        show ino_letgo 0 with dissolve:
                                                            zoom 0.6 xalign 0.5
                                                        pause (1)
                                                        "Moments before falling unconsciouss, she used what little strength she could muster to try and raise her stockings back up..."
                                                        # show ino_shutup slap2 with dissolve:
                                                        #     zoom 1.35
                                                        #cg
                                                        bo"Hahaha! She is about to lose it."
                                                        menu:
                                                            bo"..."
                                                            "Let go of her ponytail":
                                                                $ inospank = True
                                                                show ino_letgo 1 with dissolve
                                                                "You slowly loosened your grip on her hair, knowing full well the moment you released it..."
                                                                "Her weakened body would hit the ground."
                                                                $ ino_fainted = True
                                                                scene black with dissolve
                                                                $ renpy.sound.play("/audio/soun_fx/intro/bodythud.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                                                                "Thud!" with vpunch
                                                                "As you let go off her hair, Ino's body harshly hit the floor."
                                                                show inofloor 1 with dissolve
                                                                pause(1)
                                                                "It would appear the impact left her momentarily unconscious. Her battered body, now lying in a bunch of rain puddles, mixed with her tears, saliva and dirt
                                                                after enduring your brutal abuse."
                                                                
                                                                jump letgo
                                                            "Finish her off":
                                                                $ inospank = True
                                                                bo"Still trying so hard..."
                                                                bo"That's a no go, Ino!"
                                                                show ino_shutup_spank0 with moveinright:
                                                                    zoom 0.6 xalign 0.5 yalign +2
                                                                hide ino_shutup_spank0
                                                                $ renpy.sound.play("/audio/soun_fx/intro/spank5.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                                show ino_shutup_spank with vpunch:
                                                                    zoom 0.6 xalign 0.5 yalign +2
                                                                
                                                                pause(0.3)
                                                                hide ino_shutup_spank with dissolve
                                                                show ino_letgo 1 with dissolve
                                                                bo"Aww, she has gone and lost it..."
                                                                menu:
                                                                    bo"..."
                                                                    "Let go of her ponytail":
                                                                        $ ino_fainted = True
                                                                        scene black with dissolve
                                                                        $ renpy.sound.play("/audio/soun_fx/intro/bodythud.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                                                                        "Thud!" with vpunch
                                                                        "As you let go off her hair, Ino's body harshly hit the floor."
                                                                        show inofloor 1 with dissolve
                                                                        pause(1)
                                                                        "It would appear the impact left her momentarily unconscious. Her battered body, now lying in a bunch of rain puddles, mixed with her tears, saliva and dirt
                                                                        after enduring your brutal abuse."
                                                                        jump letgo
                                                        
                                                    "Penetrate her":
                                                        bo"Maybe this, will get you to finally shut up!"
                                                        jump inolast
                                                        #cock cg
                                                        
                                            "Grab her ass":
                                                bo"Will you fucking relax!?"
                                                show inospank 8 with dissolve
                                                "You sink your fingers into her ass, grabbing it with enough force to signify your intentions to Ino..."
                                                "Your gesture only served to make Ino panic even more..."
                                                ino"NO! TAKE YOUR HANDS OFF ME! Y-YOU BRUTE!"
                                                menu:
                                                    bo"..."
                                                    "Restrain her!":
                                                        bo"Stop flailing your damn arms around..."
                                                        bo"And shut the fuck up for a second!"
                                                        show inospank f1 with dissolve
                                                        "You took hold of her arms and pulled them towards you, restricting Ino's movements."
                                                        bo"Did I not say the louder you are, the worse it would get!?!"
                                                        "You pull roughly on both of her arms, so that her ass is forced to grind against your erect cock."
                                                        ino"AAAAH! L-LET ME GO!"
                                                        ino"P-PLEASE!!"
                                                        show inospank f2 with dissolve:
                                                            zoom 0.67 xalign 0.5 yalign 0.5
                                                        "You pressed your cock against her bare ass, the feeling excited you even more."
                                                        $ renpy.sound.play("/audio/soun_fx/inocrying3.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                                                        ino"*Sobbing"
                                                        ino"N-no..."
                                                        ino"A-anything b-but that... p-please."
                                                        "You could feel Ino weakening. She stopped trying to break free from your grip..."
                                                        "It would appear she was slowly losing consciousness, perhaps from the overwhelming stress of the situation she found herself in."
                                                        $ ino_fainted = True
                                                        menu:
                                                            bo"..."
                                                            "Penetrate her":
                                                                #block of code to run
                                                            
                                                                show inospank f3 with dissolve
                                                                ino"..."
                                                                "Ino was completely silent, as you pressed the tip of your cock against her ass..."
                                                                "It was clear to you now she lost consciousness, her body only held up by your firm grip on her hands."
                                                                bo"Aww... Was this too much for you Ino?"
                                                                bo"But we haven't even started yet..."
                                                                menu:
                                                                    "..."
                                                                    "Force her down":
                                                                        bo"At least we can get comfortable with you being still for once!"
                                                                        menu:
                                                                            bo"..."
                                                                            "Send her flying with a final spank":
                                                                                show inospankv2_1 with moveinleft:
                                                                                    zoom 0.6 xalign 0.5 yalign +2
                                                                                hide inospankv2_1
                                                                                $ renpy.sound.play("/audio/soun_fx/intro/spank5.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                                                show inospankv2_2 with vpunch:
                                                                                    zoom 0.6 xalign 0.5 yalign +2
                                                                                pause(0.1)
                                                                                scene black
                                                                                hide inospankv2_2
                                                                                "You dish out one last hard spank before letting go of her hands and pushing her down on the ground..."
                                                                            "Push her down":
                                                                                bo"Down you go, bitch!"
                                                                            
                                                                        
                                                                        scene black with dissolve
                                                                        $ renpy.sound.play("/audio/soun_fx/intro/bodythud.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                                                                        "*Thud" with vpunch
                                                                        show ino_hinata 0 with dissolve
                                                                        "Her lifeless body hits the floor..."
                                                                        jump letgo
                                                                    "Let go of her hands":
                                                                        "You knew that if you let go, Ino would hit the ground face first."
                                                                        scene black with dissolve
                                                                        $ renpy.sound.play("/audio/soun_fx/intro/bodythud.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                                                                        "*Thud" with vpunch
                                                                        "That did not stop you..."
                                                                        show ino_hinata 0 with dissolve
                                                                        jump letgo

                                                                    "Take her as she is":
                                                                        scene black with dissolve
                                                                        bo"Can't think of a better time to fuck your holes..."
                                                                        "You let go of her hands..."
                                                                        $ renpy.sound.play("/audio/soun_fx/intro/bodythud.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                                                                        "*Thud" with vpunch

                                                                        scene bginofinal1 with dissolve
                                                                        show ino vaginal4 with dissolve:
                                                                            zoom 1 xalign 0.5 yalign 0.1
                                                                        "Her lifeless body hit the floor..."
                                                                        bo"Look at you now..."
                                                                        bo"This could have been much easier you know..."
                                                                       
                                                                        scene bginofinal1 with dissolve
                                                                        hide ino
                                                                        show ino hairgrab3_2 with dissolve:
                                                                            pos (146, -622) 
                                                                        "You moved her little thong to the side, exposing both of her holes to yourself..."
                                                                        bo"To think that a mature lady such as you was hiding these goods..."
                                                                        bo"Not even my fantasies could match the real deal!"
                                                                        show ino vaginal4 with dissolve:
                                                                            zoom 1 xalign 0.5 yalign 0.1
                                                                        ino"Don't..."
                                                                        ino"T-touch me..."
                                                                        "She seemed to be falling in and out of consciousness..."
                                                                        "But she was utterly exhausted. There was nothing she could do."
                                                                        hide ino
                                                                        show ino hairgrab3_2 with dissolve:
                                                                            pos (146, -622) 
                                                                        "Ino was at your mercy.."
                                                                        bo"Are you still with me, Ino? The fun is just about to begin!"
                                                                        menu:
                                                                            "..."
                                                                            "Fuck her pussy":
                                                                                show ino vaginal4 with dissolve:
                                                                                    zoom 1 xalign 0.5 yalign 0.1
                                                                                ino"..."
                                                                                bo"Aww, she went and lost it again, what a shame."
                                                                                jump inopenetratepussy
                                                                            "Fuck her asshole":
                                                                                show ino vaginal4 with dissolve:
                                                                                    zoom 1 xalign 0.5 yalign 0.1
                                                                                ino"..."
                                                                                bo"Aww, she went and lost it again, what a shame."
                                                                                jump inopenetrateasshole
                                                                                                                                              
                                            
                            label letgo:
                                $ ino_fainted = True
                                bo"Must have been a little bit too rough..."
                                bo"Have I... gone too far?"
                                $ renpy.sound.play("/audio/soun_fx/ominous_sound.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                scene black with dissolve
                                show boruto looking with dissolve:
                                    zoom 1 xalign 0.5 yalign 0.1
                                menu :
                                    bot"Have I... gone too far?"
                                    
                                    "{color=[hatredcolor]}I am a monster{/color}":
                                        bo"Yes, I am a fucking monster. The worst part is..."
                                        call changeHatred(1, "none") from _call_changeHatred_30
                                        show boruto masturbating with dissolve:
                                            zoom 1.0 xalign 0.5 yalign 0.1
                                        bo"I find some deranged enjoyment in this."
                                    "It was her fault":
                                        show boruto masturbating with dissolve
                                        bo"No... If only she stopped resisting, this could be painless for both of us."
                                    "Blame your condition":
                                        bo"But... this fucking feeling inside of me... It is almost like I have no control, no sense!"
                                        show boruto masturbating with dissolve
                                        bo"This... this is not me, is it?"
                                        "[bo_name] tried to convince himself that this isn't what he wanted. but..."
                                        scene black with dissolve
                                bo"No matter, it is time I get rid of this fucking urge of mine."
                                scene black with dissolve
                                if inospank == True:
                                    show ino_letgofinal 0 with dissolve
                                else:
                                    show ino_letgofinal_nospank 0 with dissolve
                                
                                bo"Besides, look at this bitch. Wearing such a slutty thong, her little puckered asshole peeking through it."
                                bo"At least she won't be able to make a sound now!"
                                menu:
                                    "..."
                                    "Ravage her asshole":
                                        bo"It looks so tight, I just can't resist it, can I?"
                                        if inospank == True:
                                            show ino_letgofinal 2 with dissolve
                                        else:
                                            show ino_letgofinal_nospank 2 with dissolve
                                        bo"Not going to stay tight for long though!"
                                        jump hinatainterferes
                                    "Ravage her pussy":
                                        bo"That clean shaven pussy of hers looks so inviting."
                                        if inospank == True:
                                            show ino_letgofinal 2 with dissolve
                                        else:
                                            show ino_letgofinal_nospank 2 with dissolve
                                        "I just have to ravage it!"
                                        jump hinatainterferes
                                    
                                    
                            
                        "{color=[hatredcolor]}Gagging her with your hands{/color}":
                            
                            $ ino_fainted = True
                            # scene bg ino with dissolve
                            show inograb at shake
                            "You turn her around and keep her restrained with one of your hands..."
                            scene bg ino
                            show inogag start:
                                zoom 0.6 xalign 0.5
                            with dissolve
                            "Your other hand, taking hold of her jaw with your thumb pushed inside of her mouth..."
                            bo"I don't think you understand, Ino"
                            bo"You keep this pretty mouth of yours closed or..."
                            scene black with dissolve
                            ino"AAH! NOOO!" with vpunch
                            ino"What are you doing, you brute!"
                            "You violently push Ino down and reach for her mouth from behind her..."
                            scene inogag 1 with dissolve:
                                zoom 0.69
                            "Ino lost her balance from your sudden push. She braced herself on all fours and started crawling in the rain covered ground."
                            "You held her jaw in place as you wrapped your left hand around her throat, while your cock kept pressing against her skirt."
                            "Tears started rolling down her face, as Ino slowly fathomed what was transpiring..."
                            bo"You are not in a position to scream!"
                            bo"Another word from your whore mouth and I swear this will turn into your worst nightmare!"
                            ino"Y-you monster! Take your filthy hands off of me!"
                            
                            menu:
                                "..."
                                "Force your fingers inside her mouth":
                                    scene inogag 1_5 with dissolve:
                                        zoom 0.7
                                    bo"You see... you keep on screaming like a mindless whore..."
                                    bo"If words are not your strongest suite..."
                                    bo"Then maybe this will make you understand!"
                                    menu:
                                        "..."
                                        "Gag her":
                                            scene black with dissolve
                                            "You place your body above her back in such a way that your weight would keep her in her crawling position..."
                                            show inogag 2 with dissolve:
                                                zoom 0.69
                                            "You shoved your thumb deep down her throat and pulled her head back towards you..."
                                            $ renpy.sound.play("/audio/soun_fx/inogag1.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                                            bo"Will you keep on screaming now!? You loud whore!?"
                                            "All Ino could mutter was muffled words and gargling sounds"
                                            ino"Mhmmm!! Sh--~tohhp! MMhhMh!!! *gargles*"
                                            bo"And if I stop...?"
                                            show inogag:
                                                zoom 0.72
                                            bo"Will you keep on resisting!?" with vpunch
                                            $ renpy.sound.play("/audio/soun_fx/inogag3.opus", channel="sfx2", loop=False, relative_volume = 1.5)
                                            "You pulled her head backwards so she could see into your eyes as you were violating her mouth with your hands..."
                                            "You were expecting some sort of affirmation..."
                                            scene black with dissolve
                                            "But Ino had other plans..."
                                            show inogag 3 with dissolve and vpunch:
                                                zoom 0.8 xalign 0.5
                                            $ renpy.sound.play("/audio/soun_fx/gruntwoman2.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                                            "Ino clenched her jaw as hard as she could and bit down on your fingers. Her bite strong enough to draw blood..."
                                            show inogag with dissolve:
                                                zoom 0.67
                                            bo"AAARH!" with vpunch
                                            bo"You fucking bitch!"
                                            scene black with dissolve
                                            $ renpy.sound.play("/audio/soun_fx/intro/bodythud.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                                            "You let go and push her on the ground."
                                            show ino_hinata 1 with dissolve
                                            $ renpy.sound.play("/audio/soun_fx/femalecough3.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                            ino"*Cough *Cough"
                                            ino"*Heavy breathing"
                                            ino"*Cough"
                                            bo"You will pay for this..."
                                            scene black with dissolve
                                            "Ino finds strength to rise to her knees..."
                                            show inogag 4 with dissolve
                                            "She looks up towards you with a defiant look on her face"
                                            ino"You f-fucking MONSTER!" with vpunch
                                            ino"Y-you thought you could do that to me and get away with it!?"
                                            ino"Fuck you, piece of shit!"
                                            $ inoslap = False
                                            $ inospit = False
                                            label chokemenu:
                                                if inospit == True and inoslap == False:
                                                    ino"FUCK YOU! DISGUSTING PIG!" with vpunch
                                                if inoslap == True and inospit == True:
                                                    show inogag 4_2 with dissolve
                                                    ino"AW!!"
                                                    ino"Y-YOU..."
                                                    ino"..."
                                                    "She looked back up to you, her previously defiant look now turned into a fearful one..."
                                                    ino"*Sobs"

                                            menu:
                                                
                                                bot"..." 
                                                "Choke her":
                                                    bo"I have had enough of your futile resistance!"
                                                    bo"Now..."
                                                    scene black with dissolve
                                                    "You stand over her, looking down into her teary eyes..."
                                                    $ renpy.sound.play("/audio/soun_fx/eye1s.opus", channel="sfx3", loop=False, relative_volume = 0.5)    
                                                    
                                                    show inochoke 1 with vpunch
                                                    show kurama2 with flash
                                                    show kurama2:
                                                        easein 1 alpha 0.0
                                                    bo"Now you suffer!"
                                                    $ renpy.sound.play("/audio/soun_fx/inogag2.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                                                    "In your rage, you wrap your hands around her neck..."
                                                    ino"Hnn-ng-! Hnn!"
                                                    bo"You bite me, I choke you!"
                                                    bo"Fair trade, don't you think? You bitch!"
                                                    show inochoke 2 with dissolve:
                                                        zoom 0.9 xalign 0.5 yalign 0.3
                                                    $ renpy.sound.play("/audio/soun_fx/inogag6.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                                                    "Ino's eyes started rolling up as you applied enough pressure to cause asphyxiation."
                                                    "She was a few seconds away from losing consciousness..."
                                                    bo"Look at you now... not so defiant, are you...?"
                                                    bo"..."
                                                    bo"But I am a merciful god..."
                                                    bo"I will give you one final chance. You speak a single word, and this gets even worse!"
                                                    scene black with dissolve
                                                    "You let go just before she fell unconsciouss..."
                                                    show ino_hinata 2 with dissolve
                                                    $ renpy.sound.play("/audio/soun_fx/cough4.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                    ino"*Cough *Cough"
                                                    "Ino struggled for a while. She took deep long breaths trying to recover from being at the brink of aspyxiation..."
                                                    scene black with dissolve
                                                    "She got up again, took one last long breath and..."
                                                    show inochoke 4 with dissolve
                                                    ino"HEEEEELP!!!!!" with vpunch
                                                    ino"SOMEONE PLEA..." with vpunch
                                                    "Before she could even finish her pleading, you..."
                                                    menu:
                                                        "..."
                                                        "Slap her":
                                                            $ inospank = False
                                                            show dream_hinaslap 1 zorder 10:
                                                                xpos -1000 xzoom(-1)
                                                            show dream_hinaslap 1 zorder 10:
                                                                easeout 0.3 xpos 0
                                                            
                                                            pause 0.3
                                                            
                                                            $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                                            with vpunch
                                                            show inoslapped 11 
                                                            hide dream_hinaslap
                                                            with dissolve
                                                            bo"Shut the fuck up already!"
                                                            "You hit her with enough force to daze her..."
                                                            show inoslapped 222 with dissolve
                                                            "Combined with the stress and abuse she endured, it was enough for her to fall unconsciouss..."
                                                            scene black with dissolve
                                                            show ino_hinata 0_nospank with dissolve
                                                            $ renpy.sound.play("/audio/soun_fx/intro/bodythud.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                                                            "*Thud" with vpunch
                                                            "Her body fell into the ground face first..." 
                                                            bo"Oops..."
                                                            scene black with dissolve
                                                            jump letgo


                                                        "{color=[hatredcolor]}Put her to sleep{/color}":
                                                            $ inospank = False
                                                            scene black with dissolve
                                                            "You pushed her on the ground..."
                                                            show inochokefinal 0 with dissolve:
                                                                zoom 0.85 xalign 0.5 yalign 0.9
                                                            bo"You have had your chance bitch, you fucking blew it!"
                                                            ino"EEEK! NO!"
                                                            ino"HEL-"
                                                            show inochokefinal 1 with dissolve and vpunch:
                                                                zoom 0.7 xalign 0.5
                                                            $ renpy.sound.play("/audio/soun_fx/inogag1.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                                                            "You jump on top of her and firmly grasp her throat..."
                                                            bo"Now you pay the price!"
                                                            ino"Hngggn!! N-no-hnn!"
                                                            ino"*Gargles"
                                                            "You were unrelenting this time. You pushed your entire body weight on to her, fully intending to shut her up for good."
                                                            "She started frothing..."
                                                            "But the sight of her struggling did not disuade you..."
                                                            menu:
                                                                "..."
                                                                "Choke her harder":
                                                                    show frothing 1 with dissolve and vpunch:
                                                                        zoom 0.65 xalign 0.5
                                                            $ renpy.sound.play("/audio/soun_fx/inogag3.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                                                            "Ino's suffering under your hands only emboldened you as you pushed your entire weight onto her thighs, your legs pressing against hers..."
                                                            "In fact, it might have aroused you... evident by your cock now resting between her legs"
                                                            ino"Hh-hhnn!!"
                                                            bo"*Grunts"
                                                            menu:
                                                                "..."
                                                                "Choke her harder":
                                                                    show frothing 1 with dissolve:
                                                                        zoom 0.70 xalign 0.5 yalign 0.1
                                                            $ renpy.sound.play("/audio/soun_fx/inogag4.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                                                            bo"It could have been so simple for you, Ino!"
                                                            bo"This is..."
                                                            menu:
                                                                "..."
                                                                "Choke her harder":
                                                                    show frothing 1_2 with dissolve:
                                                                        zoom 0.75
                                                            $ renpy.sound.play("/audio/soun_fx/inogag2.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                                                            bo"YOUR FAULT!" with vpunch
                                                            ino"Hnng..."
                                                            "You could see the life slowly drained from her eyes..."
                                                            menu:
                                                                "..."
                                                                "Choke her harder":
                                                                    show frothing 1_3 with dissolve:
                                                                        zoom 0.8
                                                            $ renpy.sound.play("/audio/soun_fx/inogag1.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                                                            ino"..."
                                                            "Ino was almost completely silent, her only sign of life being the occasional convulsion or gargle..."
                                                            bo"What's wrong now Ino, can't talk?"
                                                            menu:
                                                                "..."
                                                                "Choke her harder":
                                                                    show frothing 2 with dissolve:
                                                                        zoom 0.85
                                                            ino"..."
                                                            bo"Stupid whore!"
                                                            bo"Hey! Can you hear me!?"
                                                            "Her almost lifeless eyes stared into the distance. It would appear she lost her senses...."
                                                            bo"Don't go sleeping on me, I have plans for you..."
                                                            menu:
                                                                "..."
                                                                "Toss her to the side":
                                                                    scene black with dissolve
                                                                    show frothingface 2 with dissolve:
                                                                        zoom 0.7 xalign 0.5 yalign 0.5
                                                                    "You take one last look at her pretty face just to make sure she is unconscious..."
                                                                    scene black with dissolve
                                                                    "Before tossing her lifeless body to the side..."
                                                                    $ renpy.sound.play("/audio/soun_fx/intro/bodythud.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                                                                    "*Thud" with vpunch
                                                                    show ino_hinata 0_nospank with dissolve
                                                                    bo"..."
                                                                    jump letgo
                                                                "Facefuck her":
                                                                    label facefuckino:
                                                                        default spitcounterintro = 0
                                                                        scene black with dissolve
                                                                        show frothingface 1 with dissolve:
                                                                            zoom 0.7 xalign 0.5 yalign 0.5
                                                                        bo"On second thought, I think I like that look on your face..."                                                                   
                                                                        show frothingface 2 with dissolve:
                                                                            zoom 0.75 xalign 0.5 yalign 0.5
                                                                        bo"Aww, you look so serene like this..."
                                                                
                                                                        show inohead 1 with dissolve:
                                                                            zoom 0.75 xalign 0.5 yalign 0.5
                                                                        hide spitmark1 with dissolve
                                                                        bo"Would be a crying shame if something were to happen to it..."
                                                                        menu :
                                                                            bot"..."
                                                                            "Spit on her":
                                                                                $ spitcounterintro += 1
                                                                                
                                                                                show inohead 1 with dissolve:
                                                                                    zoom 0.80 xalign 0.5 yalign 0.5
                                                                                $ renpy.sound.play("/audio/soun_fx/spit1.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                                                                                show spitfx1:
                                                                                    zoom 0.8 xalign 0.5
                                                                                show spitmark1:
                                                                                    xalign 0.50 yalign 0.22 zoom 0.2
                                                                                with dissolve and flash
                                                                                show inohead 1 with dissolve:
                                                                                    zoom 0.75 xalign 0.5 yalign 0.5
                                                                                show spitmark1 with dissolve:
                                                                                    xalign 0.50 yalign 0.22 zoom 0.2
                                                                                hide spitfx1 with dissolve
                                                                                call changeHatred(1,"none") from _call_changeHatred_31
                                                                                bo"That suits you better!"
                                                                            "Don't":
                                                                                pause 0.1
                                                                        hide spitmark1 with dissolve
                                                                        show inohead 1_1 with dissolve:
                                                                            zoom 0.75 xalign 0.5 yalign 0.5
                                                                        bo"And to think all you used this pretty mouth of yours for was just to fucking scream..."
                                                        
                                                                        show inohead 1_2 with dissolve:
                                                                            zoom 0.75 xalign 0.5 yalign 0.5
                                                                        bo"But I have another use for it..."
                                                                        menu :
                                                                            bot"..."
                                                                            "Spit on her":
                                                                                $ spitcounterintro += 1
                                                                                show inohead 1_2 with dissolve:
                                                                                    zoom 0.80 xalign 0.5 yalign 0.5
                                                                                $ renpy.sound.play("/audio/soun_fx/spit2.opus", channel="sfx2", loop=False, relative_volume = 0.9)
                                                                                pause 0.4
                                                                                show spitfx1:
                                                                                    zoom 0.85 xalign 0.5
                                                                                show inohead 1_2:
                                                                                    zoom 0.75 xalign 0.5 yalign 0.5
                                                                                show spitmark1:
                                                                                    xalign 0.50 yalign 0.22 zoom 0.2
                                                                                with dissolve and flash
                                                                            
                                                                                hide spitfx1 with dissolve
                                                                                
                                                                                bo"Fucking whore!"
                                                                            "Don't":
                                                                                pause 0.1
                                                                        hide spitmark1 with dissolve
                                                                        show inohead 1_3 with dissolve:
                                                                            zoom 0.75 xalign 0.5 yalign 0.5
                                                                        bo"I am thinking that I will..."
                                           
                                                                        show inohead 1_4 with dissolve:
                                                                            zoom 0.75 xalign 0.5 yalign 0.5
                                                                        bo"Stretch it just a little bit..."
                                                                        menu :
                                                                            bot"..."
                                                                            "Spit on her":
                                                                                $ spitcounterintro += 1
                                                                                show inohead 1_4 with dissolve:
                                                                                    zoom 0.80 xalign 0.5 yalign 0.5
                                                                                $ renpy.sound.play("/audio/soun_fx/spit3.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                                                                                show spitfx1:
                                                                                    zoom 0.85 xalign 0.5
                                                                                show inohead 1_4:
                                                                                    zoom 0.75 xalign 0.5 yalign 0.5
                                                                                show spitmark1:
                                                                                    xalign 0.50 yalign 0.22 zoom 0.2
                                                                                with dissolve and flash
                                                                                hide spitfx1 with dissolve
                                                                                
                                                                                bo"That's more like it.."
                                                                            "Don't":
                                                                                pause 0.1
                                                                        hide spitmark1 with dissolve
                                                                        show inousehead 2 with dissolve:
                                                                            zoom 0.75 xalign 0.5 yalign 0.5
                                                                        bo"So that maybe, I can fit my entire cock in it!"
                                                                        menu :
                                                                            bot"..."
                                                                            "Spit on her":
                                                                                $ spitcounterintro += 1
                                                                                show inousehead 2 with dissolve:
                                                                                    zoom 0.80 xalign 0.5 yalign 0.5
                                                                                $ renpy.sound.play("/audio/soun_fx/spit4.opus", channel="sfx2", loop=False, relative_volume = 1.4)
                                                                                pause 0.5
                                                                                show spitfx1:
                                                                                    zoom 0.85 xalign 0.5
                                                                                show inousehead 2:
                                                                                    zoom 0.75 xalign 0.5 yalign 0.5
                                                                                show spitmark1:
                                                                                    xalign 0.50 yalign 0.22 zoom 0.2
                                                                                with dissolve and flash
                                                                                hide spitfx1 with dissolve
                                                                                
                                                                                bo"Gotta make sure you are lubricated!"
                                                                            "Don't":
                                                                                pause 0.1

                                                                        hide spitmark1 with dissolve
                                                                        show inofacefinal 1 with dissolve:
                                                                            zoom 0.75 xalign 0.5 yalign 0.5
                                                                        bo"It is time I get rid of this fucking pain!"
                                                                        menu :
                                                                            bot"..."
                                                                            "Get closer":
                                                                                show inofacefinal 2 with dissolve
                                                                                bo"Come on, open up..."
                                                                                bo"Oh my bad, I forgot!"
                                                                                bo"You might need some help with that..."
                                                                                menu:
                                                                                    bo"..."
                                                                                    "'Help' her":
                                                                                        show inofacefinal 3 with dissolve
                                                                                        bo"It ain't gonna fit..."
                                                                                        bo"Just a little bit more Ino..."
                                                                                        menu:
                                                                                            bo"..."
                                                                                            "Force her mouth open":
                                                                                                show inofacefinal 4 with dissolve
                                                                                                bo"That's more like it!"
                                                                                                menu inofacefinal:
                                                                                                    bo"..."
                                                                                                    "'Lubricate' her one final time":
                                                                                                        $ spitcounterintro += 1
                                                                                                        if spitcounterintro == 6:
                                                                                                            bo"One more for good measure"
                                                                                                        elif spitcounterintro == 7:
                                                                                                            bo"I just can't help it!"
                                                                                                        elif spitcounterintro == 8:
                                                                                                            bo"Bitch!"
                                                                                                        elif spitcounterintro == 9:
                                                                                                            bo"Fuck you!"
                                                                                                        elif spitcounterintro >9:
                                                                                                            bo"..."
                                                                                                        else:
                                                                                                            bo"And just to be sure..."
                                                                                                        $ renpy.sound.play("/audio/soun_fx/spit4.opus", channel="sfx2", loop=False, relative_volume = 1.6)
                                                                                                        pause 0.5
                                                                                                        show spitfx1:
                                                                                                            zoom 0.85 xalign 0.5 
                                                                                                        
                                                                                                        show spitmark1:
                                                                                                            zoom 0.2 pos (0.35, 0.02)
                                                                                                        with dissolve and flash
                                                                                                        hide spitfx1 with dissolve
                                                                                                        show inofacefinal 4:
                                                                                                            zoom 0.75 xalign 0.5 yalign 0.5
                                                                                                        show spitmark1:
                                                                                                            zoom 0.2 pos (0.35, 0.02)
                                                                                                        with dissolve
                                                                                                        if spitcounterintro == 6:
                                                                                                            bo"Looking better and better!"
                                                                                                        elif spitcounterintro == 7:
                                                                                                            bo"Take that bitch!"
                                                                                                        elif spitcounterintro == 8:
                                                                                                            bo"Just like your daddy envisioned you'd be when you grew up eh?"
                                                                                                        elif spitcounterintro == 9:
                                                                                                            bo"That's right you god-damned whore!"
                                                                                                        elif spitcounterintro >9:
                                                                                                            bo"..."
                                                                                                        else:
                                                                                                            bo"Dirty whore!"
                                                                                                        if spitcounterintro == 7:
                                                                                                            bo"Your pretty face is drenched in my spit, just like a whore like you deserves to be!"
                                                                                                            call changeHatred(2,"none") from _call_changeHatred_32
                                                                                                        elif spitcounterintro == 8:
                                                                                                            dev"I am not judging but uuuuh...."
                                                                                                        elif spitcounterintro >= 9:
                                                                                                            bot"I am running out of saliva..."
                                                                                                        jump inofacefinal
                                                                                                    "Facefuck her!":
                                                                                                        hide spitmark1 with dissolve
                                                                                                        show inofacefinal 4 with dissolve:
                                                                                                            zoom 1.05 xalign 0.5 yalign 0.5
                                                                                                        bo"Now say 'Aaa'!"
                                                                                                        bo"I am going to shove my cock so deep down your throat you are going to be thankful you were unconscious!"
                                                                                                        jump hinatainterferes
                                                                    

                                                        
                                                    
                                                        
                                                "Spit on her" if inospit == False:

                                                    $ inospit = True
                                                    bo"Have I not said, you were going to pay for this!?"
                                                    $ renpy.sound.play("/audio/soun_fx/spit4.opus", channel="sfx2", loop=False, relative_volume = 1.8)
                                                    pause 0.6
                                                    show spitmark1:
                                                        zoom 0.3 xalign 0.5 yalign 0.01
                                                        pos (0.57, -252)
                                                        ypos -53
                                                    show spitfx1:
                                                        xalign 0.65
                                                   
                                                    with dissolve and flash
                                                    hide spitfx1 with dissolve
                                                    call changeHatred(1,"none") from _call_changeHatred_33
                                                    bo"Take this you dumb bitch!"
                                                    jump chokemenu


                                                "Slap her" if inoslap == False and inospit == True:
                                                    $ inoslap = True
                                                    bo"Hey! No talking back allowed!"
                                                    show ino_faceslap with moveinleft:
                                                        zoom 2.5 yalign 0.2 xpos +130
                                                    $ renpy.sound.play("/audio/soun_fx/intro/spank4.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                    with vpunch
                                                    show inogag 4_1 with dissolve
                                                    hide spitmark1 with dissolve
                                                    hide ino_faceslap with dissolve
                                                    ino"Ugh!"
                                                    bo"Slut!"
                                                    bo"That was for biting me!"
                                                    jump chokemenu

                    
                                
                        
                "{color=[dominancecolor]}Use her{/color}":
                    #naked rage cg exposed cock
                    bo"You.. belong to me now!"
                    scene black with dissolve
                    ino"W-what a-are you doing?! P-please..."
                    "You forcibly dragged her closer to you and held her in place..."
                    show inoravage 1 with dissolve:
                        zoom 0.5 xalign 0.5
                    ino"EEEK!" with vpunch
                    "Ino let out a scream as she felt you carelessly place your hands all over her..."
                    call changeDominance(1) from _call_changeDominance_38
                    "Your left hand grabbing her exposed belly and your right hand groping her breasts..."
                    ino"W-why are you t-touching me like that!?"
                    ino"[bo_name]! Please! Stop this at once!"
                    "Ino tried to escape the firm grasp you had of her, but you wouldn't bulge..."
                    show inoravage 2 with dissolve
                    "In fact, you went even further, sliding your hand under her garment..."
                    ino"[bo_name]! Y-you can't do that! What would your [hin_rel] think of this!?"
                    default inoplayass = False
                    default inoplaytits = False
                    menu:
                        bot"..."
                        "Grope her tits":
                            bo"I don't think you understand, Ino..."
                            show inogropetits 1 with vpunch:
                                zoom 0.85 xalign 0.5 yalign 0.7
                            ino"EEEK!"
                            bo"You are mine to do with as I please!"
                            ino"NO! W-WHY!?"
                            ino"T-this isn't like you [bo_name]! P-please!"
                            $ inoplaytits = True
                            $ inoplayass = False
                            menu inorepeatingstart:
                                bo"Not like... me?"
                                "Deceive her...":
                                    label deceive:
                                        bo"Not like me?"
                                        scene black with dissolve
                                        "You let go of her... for now."
                                        show bg ino with dissolve
                                        show inotransparent at left with dissolve:
                                            zoom 0.47
                                        "Ino in her short moment of reprive, frantically pulled down her skirt and instinctively covered her chest..."
                                        ino"Thank the lords, there is still some sense left in you!"
                                        "Her back was turned towards you, It would seem she did not yet realize your nefarious intentions..."
                                        hide inotransparent with dissolve
                                        show boruto boner2t with dissolve
                                        bo"You are right, Ino. This isn't... me."
                                        show boruto boner3t with dissolve
                                        ino"Why would you do that, [bo_name]!?"
                                        ino"I am practically like an aunt to you! I was there when you were growing up! Have you no shame!?"
                                        ino"How could you do that to me!"
                                        bo"Do that... to you?"
                                        show boruto boner4t with dissolve
                                        bo"It was just some touching, Ino"
                                        bo"You see..."
                                        scene bg ino with dissolve
                                        show inotransparent at left with dissolve:
                                            zoom 0.47
                                        show boruto looking at right with dissolve:
                                            zoom 0.4 xzoom -1
                                        bo"You were right, that wasn't me. Because I am much worse than that!"
                                        show inotransparent at left with dissolve:
                                            zoom 0.47
                                        ino"W-what are you saying, [bo_name]!?"
                                        
                                        show inotransparent at left with dissolve:
                                            xzoom (-1)
                                            zoom 0.47
                                        "Ino turns around, only to see you completely naked and stroking your cock." 
                                        show inotransparent at left:
                                            easein 0.3 zoom 0.47 xpos-0.08
                                        $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                                        ino"AAH!" with vpunch
                                        
                                        ino"...W-why are you naked!?"
                                        ino"Y-you are not t-thinking of doing something bad, are you?"
                                        show boruto masturbating at right:
                                            easein 0.3 xpos 0.94
                                        bo"Ino, or should I say... auntie! All I am thinking about is bad!"
                                        ino"N-no... s-stay away from me!"
                                        show boruto masturbating at right:
                                            easein 0.3 xpos 0.85
                                        scene ino dragback with vpunch:
                                                zoom 1.1 xalign 0.1
                                        $ renpy.sound.play("/audio/soun_fx/intro/gruntwoman2.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                                        "You reach for her before she could react"
                                        bo"Did I not say you are mine to do with as I please!?"
                                    menu inorepeatingmenu:
                                        bo"..."
                                        "Play with her tits":
                                            $ inoplaytits = True
                                            $ inoplayass = False
                                            bo"Oh you poor girl..."
                                            
                                            scene black with dissolve
                                            show bg ino:
                                                blur 20
                                            show inogropetits 4:
                                                zoom 0.5 xalign 0.5
                                            with dissolve
                                            
                                            "You pull her towards you, restraining her arms behind her back and shoving your cock between her thighs."
                                            ino"AH! NO!" with vpunch
                                            ino"[bo_name], w-what are you doing!?"
                                            ino"Y-you are just a kid, you can't do this to me!"
                                            ino"What would your [hin_rel] think of you!?"
                                            image anim1 = Movie(channel="movie_dp", play="images/video/inotits.webm", stop_music=False)

                                            menu:
                                                bo"..."
                                                "Who the fuck cares!":
                                                    show anim1:
                                                        zoom 0.5 xalign 0.5
                                                    bo"I don't give a fuck about that right now..."
                                                    bo"In fact, whenever you visited my [hin_rel], I would always be just a few feet away..."
                                                    bo"Hidden in the bathroom, fantasizing about fucking your sexy ass beneath those tempting fishnets of yours..."
                                                    bo"To think that now, I could do just that!"
                                                    ino"What the hell are you talking about, [bo_name]! This isn't you! The [bo_name] I know would never do or say such wicked things!"
                                                    ino"Let me go right this moment!"
                                                    menu:
                                                        "..."
                                                        "I thought we've been through this already...":
                                                            bo"I thought we've been through this already, Ino. This isn't me..."
                                                            bo"Which is exactly why I will ravage your holes and have zero remorse about it!"
                                                            ino"Y-you m-monster..."
                                                            label inoescapes:
                                                                ino"LET..."
                                                                ino"ME..."
                                                                scene black
                                                                $ renpy.sound.play("/audio/soun_fx/gruntwoman2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                                ino"GO!!" with vpunch
                                                                "Ino's struggles paid off, she managed to escape your grip..."
                                                                ino"SOMEONE, PLEASE HELP!"
                                                                "But only for a second..."
                                                                menu:
                                                                    bo"Where do you think you are going..."
                                                                    "Stop her":
                                                                        show bg ino:
                                                                            blur 20
                                                                        show inoescape 1 with vpunch:
                                                                            zoom 0.7 xalign 0.5
                                                                        $ renpy.sound.play("/audio/soun_fx/gruntwoman1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                                        bo"You slippery whore!"
                                                                        "You grab her by her waist and easily pull her back..."
                                                                        bo"The more you resist, the worse it gets!"
                                                                        menu:
                                                                            bo"..."
                                                                            "Expose her tits":
                                                                                $ inoplaytits = True
                                                                                $ inoplayass = False
                                                                                
                                                                                scene black with dissolve
                                                                                show bg ino with dissolve:
                                                                                    blur 20
                                                                                show inoanim1 with vpunch:
                                                                                    zoom 0.5 xalign 0.5
                                                                                $ renpy.sound.play("/audio/soun_fx/kyaa.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                                                ino"EEEK! DON'T TOUCH ME THERE!"
                                                                                bo"I will do with you as I damn please."
                                                                                "You sunk your hands under her tight vest and moved your hands up through her stomach and to her bare breasts..."
                                                                                bo"Oh? What's with your muscular physique Ino! For an old bitch you certainly have some muscle on you. The feeling of moving my hands all over your toned stomach is intoxicating..."
                                                                                bo"I am thinking I want more!"
                                                                                show inogropetitsanim with vpunch:
                                                                                    zoom 0.5 xalign 0.5
                                                                                $ renpy.sound.play("/audio/soun_fx/inocryingshort.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                                                ino"No! *sobbing*"
                                                                                "Powerless as she was, Ino started sobbing while you carelessly played around with her breasts, she kept begging and pleading for you to stop..."
                                                                                ino"S-stop t-touching me! P-pleaseeee! *sobbing*"
                                                                                bo"Aww, don't start crying now Ino..."
                                                                                bo"We still have ways to go you know."
                                                                                bo"Playing with your firm titties, it is getting me real excited!"
                                                                                bo"Perhaps it is time I take what I need, what I... want!"
                                                                                
                                                                                menu finalinomenu:
                                                                                    
                                                                                    bo"..."
                                                                                    "Force her on all fours":
                                                                                        ino"*Sobbing*"
                                                                                        scene black with dissolve
                                                                                        $ renpy.sound.play("/audio/soun_fx/bodythud.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                                                        "You violently shoved Ino on the ground" with vpunch
                                                                                        show inoall4 start with dissolve
                                                                                        $ renpy.sound.play("/audio/soun_fx/inocryingshort.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                                                        ino"uh.. ah!"
                                                                                        ino"S-someone, anyone p-please, save me from this nightmare..."
                                                                                        bo"No-one is around, Ino. Can't you see!?"
                                                                                        scene black with dissolve
                                                                                        "Ino got up on her knees..."
                                                                                        show ino crawlingbu with dissolve
                                                                                        "She tried to crawl away, but she was exhausted..."
                                                                                        bo"Don't you start trying crawling away now..."
                                                                                        show inocrawlinganim with dissolve:
                                                                                            zoom 1.1 xalign 0.5
                                                                                        $ renpy.sound.play("/audio/soun_fx/inocrying3.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                                                        ino"N-no! S-stay away, y-you m-monster!"
                                                                                        "She slowly made small strides crawling away from you..."
                                                                                        "But it was apparent she was exhausted from all her previous struggling..."
                                                                                        ino"*Panting"
                                                                                        ino"S-stay..."
                                                                                        ino"B-back..."
                                                                                        menu:
                                                                                            "..."
                                                                                            "Stop her":
                                                                                                bo"Stupid whore!"
                                                                                                hide inocrawlinganim
                                                                                                show inoall4 start2 with dissolve
                                                                                                
                                                                                                "She turned around as she heard you approaching..."
                                                                                                ino"N-no..."
                                                                                                show inoall4 start2_2 with dissolve:
                                                                                                    zoom 1.1 xalign 0.7 yalign 0.1
                                                                                                bo"You think you will crawl your way out of this?"
                                                                                                ino"Stay away from me..."
                                                                                                "She kept making small strides... but to no avail"
                                                                                                show inoall4 start2_3 with dissolve:
                                                                                                    zoom 1.2 xalign 0.7
                                                                                                ino"Don't touch me..."
                                                                                                bo"You are mine to do with as I please!"
                                                                                                show inoall4 start2_4 with dissolve:
                                                                                                    zoom 1.3 xalign 0.7
                                                                                                ino"N-never..."
                                                                                                show inoall4 start2_5 with dissolve:
                                                                                                    zoom 1.4 xalign 0.7
                                                                                                bo"There is no escape..."
                                                                                                show inoall4 start2_6 with dissolve:
                                                                                                    zoom 1.5 xalign 0.7
                                                                                                ino"You m-monster!"

                                                                                            
                                                                                        show inoall4 1 with vpunch:
                                                                                            zoom 1 xalign 0.5 yalign 0.5
                                                                                        bo"Gotcha, dumb whore!"
                                                                                        show inogag 1_5 with dissolve:
                                                                                            zoom 0.7 xalign 0.5
                                                                                        "You hunch over her back reaching for her mouth... your entire weight pressed against her..."
                                                                                        "Ino was exhausted, she could barely move..."
                                                                                        bo"You belong to me now!"
                                                                                        $ renpy.sound.play("/audio/soun_fx/inocryingshort.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                                                        ino"*Sobbing"
                                                                                        ino"P-please..."
                                                                                        ino"L-let me go..."
                                                                                        menu:
                                                                                            ino"L-let me go..."
                                                                                            "Restrain her hands":
                                                                                                scene black with dissolve
                                                                                                bo"That is not happening you whore!"
                                                                                                show inohands 1 with vpunch
                                                                                                $ renpy.sound.play("/audio/soun_fx/gruntwoman2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                                                                bo"Not before I have my way with you!"
                                                                                                "You kneel over her legs as she was crawling away, grabbing and pulling on both of her arms."
                                                                                                "Ino left out a soft moan of disgruntlement, she was too tired to attempt an escape."
                                                                                                ino"...Ugh..."
                                                                                                ino"T-that h-hurts, you b-bastard..."
                                                                                                menu:
                                                                                                    ino"T-that h-hurts, you b-bastard..."
                                                                                                    "Raise her skirt":
                                                                                                        show inohands 2 with dissolve
                                                                                                        bo"And it's about to hurt a lot more if you keep this charade up!"
                                                                                                ino"Y-you can't do that..."
                                                                                                ino"L-let me go!"
                                                                                                menu:
                                                                                                    "Lower her fishnets":
                                                                                                        bo"Wishful thinking, Ino..."
                                                                                                        show inohands 3 with dissolve
                                                                                                        bo"The fun is about to begin!"
                                                                                                ino"W-what are you d-doing!? You c-can't touch me there!"
                                                                                                bo"Ino, you poor girl..."
                                                                                                scene black
                                                                                                bo"Make no mistake, I will do more than just touch you 'down there'..."
                                                                                                $ renpy.sound.play("/audio/soun_fx/spank4.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                                                                pause 0.1                                                                                          
                                                                                                show inohands 4 with vpunch
                                                                                                "You let go of her arms and instead grabbed a handful of her ass."
                                                                                                "You sunk your fingers deep into her ass, causing Ino to jitter. She placed her hands on your thighs amd pushed as hard she could, but your entire weight laying on her was holding her in place."
                                                                                                ino"Y-you piece of shit! Touch me again and I s-swear you will live to regret it!"
                                                                                                bo"Is that a threat?"
                                                                                                menu:
                                                                                                    bo"Oh Ino... You are in no position to threaten me!"
                                                                                                    "Spank her":
                                                                                                        bo"The audacity to even speak those words out loud..."
                                                                                                        window hide
                                                                                                        show inohair_doubletap1 with moveinleft:
                                                                                                            zoom 1.1 xpos -100
                                                                                                        $ renpy.sound.play("/audio/soun_fx/intro/spank5.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                                                                        with vpunch
                                                                                                        pause 0.15                                                                      
                                                                                                        show inohands 4_s1 with dissolve
                                                                                                        hide inohair_doubletap1 with dissolve
                                                                                                        window show
                                                                                                        ino"Hnnaaa!!"
                                                                                                        bo"Makes the process of breaking you even more satisfying!"
                                                                                                        $ renpy.sound.play("/audio/soun_fx/inocryingshort.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                                                                        ino"*Sobbing"
                                                                                                        ino"You b-bastard!"
                                                                                                        "Ino was exhausted, her eyes started rolling up. It would seem she was close to unconsciousness."
                                                                                                        "A few more hits would surely make her lose her senses..."
                                                                                                        ino"P-please *crying* d-don't hurt me!"
                                                                                                        bo"You see... that's dependant on you, Ino..."
                                                                                                        menu:
                                                                                                            bo"Will you be a good girl?"
                                                                                                            "Spank again!":
                                                                                                                bo"Because I am thinking..."
                                                                                                                window hide
                                                                                                                show inohair_doubletap1 with moveinleft:
                                                                                                                    zoom 1.1 xpos -100
                                                                                                                $ renpy.sound.play("/audio/soun_fx/intro/spank8.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                                                                                with vpunch
                                                                                                                hide inohair_doubletap1 with dissolve
                                                                                                                show inohair_doubletap2 with moveinright:
                                                                                                                    zoom 1.1 xpos -100
                                                                                                                $ renpy.sound.play("/audio/soun_fx/intro/spank4.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                                                                                with vpunch
                                                                                                                pause 0.15                                                                      
                                                                                                                show inohands 4_s2 with dissolve
                                                                                                                hide inohair_doubletap2 with dissolve
                                                                                                                window show
                                                                                                                ino"...Uhhgh..!!"
                                                                                                                bo"You haven't been that good of a girl up until now!"
                                                                                                                jump inolast

                                                                                                            "Expose her holes":
                                                                                                                bo"As long as you let me have my way..."
                                                                                                                scene black with dissolve
                                                                                                                jump inolast

                                                                                                    "Expose her holes":
                                                                                                        bo"Especially when your little holes are in such close viscinity!"
                                                                                                        jump inolast
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                            "Pull her hair":
                                                                                                scene black with dissolve
                                                                                                bo"You are not going anywhere!"
                                                                                                $ renpy.sound.play("/audio/soun_fx/intro/gruntwoman1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                                                                show ino hairgrab1 with vpunch
                                                                                                bo"Not before I have my way with you!"
                                                                                                "You took hold of her ponytail and held her in place by dragging on to it..."
                                                                                                ino"T-that h-hurts..."
                                                                                                default inohairpull_spank = False
                                                                                                menu hairgrabrepeating:
                                                                                                    "..."
                                                                                                    "Lower her fishnets":
                                                                                                        bo"Those have to go..."
                                                                                                    "Spank her" if inohairpull_spank == False:
                                                                                                        $ inohairpull_spank = True
                                                                                                        bo"And it is about to hurt a lot more!"
                                                                                                        ino"N-no... P-please!"
                                                                                                        #block of code to run
                                                                                                        show ino_hairgrabspank with moveinright
                                                                                                        hide ino_hairgrabspank
                                                                                                        $ renpy.sound.play("/audio/soun_fx/intro/spank5.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                                                                        show ino_hairgrabspank2 with vpunch
                                                                                                        show ino hairgrab1_spanked with dissolve
                                                                                                        $ renpy.sound.play("/audio/soun_fx/intro/gruntwoman2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                                                                        ino"Aww!" with vpunch
                                                                                                        hide ino_hairgrabspank2 with dissolve
                                                                                                        ino"D-don't do that! Y-you monster!"
                                                                                                        jump hairgrabrepeating
                                                                                                scene black with dissolve
                                                                                                "You lower her fishnets..."
                                                                                                if inohairpull_spank == True:
                                                                                                    show ino hairgrab2_2spanked with dissolve
                                                                                                else:
                                                                                                    show ino hairgrab2 with dissolve
                                                                                                
                                                                                                ino"W-what are y-you doing..."
                                                                                                bo"You know very well what is coming, Ino!"
                                                                                                ino"Y-you can't do that! You are just a kid!"
                                                                                                menu inorepeating2:
                                                                                                    "..."
                                                                                                    "Shut her up":
                                                                                                        bo"Just a kid you say...? Ever seen a kid do this!?"
                                                                                                        show inohair_doubletap1 with moveinleft
                                                                                                        $ renpy.sound.play("/audio/soun_fx/intro/spank6.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                                                                        show inohair_doubletap1 with vpunch
                                                                                                        hide inohair_doubletap1 with dissolve
                                                                                                        show inohair_doubletap2 with moveinright:
                                                                                                                    zoom 1.1 xpos -100 ypos -40
                                                                                                        show ino hairgrab2_2spankedx2 with vpunch
                                                                                                        $ renpy.sound.play("/audio/soun_fx/intro/spank5.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                                                                        show inohair_doubletap2 with dissolve
                                                                                                        hide  inohair_doubletap2 with dissolve
                                                                                                        show ino hairgrab2_2spankedx2 with dissolve:
                                                                                                            zoom 1.05 xalign 0.9
                                                                                                        $ renpy.sound.play("/audio/soun_fx/intro/gruntwoman3.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                                                                                                        ino"Aaaaargh!!!"
                                                                                                        "You roughly yank her hair, as if Ino was a horse to be tamed..." with vpunch
                                                                                                        ino"...."
                                                                                                        bo"Will you shut the fuck up now Ino!?"
                                                                                                        show inohair_doubletap1 with moveinleft
                                                                                                        $ renpy.sound.play("/audio/soun_fx/intro/spank5.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                                                                        show inohair_doubletap1 with vpunch
                                                                                                        hide inohair_doubletap1 with dissolve
                                                                                                        show inohair_doubletap2 with moveinright
                                                                                                        $ renpy.sound.play("/audio/soun_fx/intro/spank7.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                                                                        show inohair_doubletap2 with vpunch
                                                                                                        show ino hairgrab2_4 with dissolve
                                                                                                        hide inohair_doubletap2 with dissolve
                                                                                                        
                                                                                                    

                                                                                                    "Spank again":
                                                                                                        default spankcounterinto = 0
                                                                                                        $ spankcounterinto += 1
                                                                                                        if spankcounterinto == 0:
                                                                                                            bo"I will do as I please you damn whore!"
                                                                                                        elif spankcounterinto == 1:
                                                                                                            bo"Take that you stupid whore!"
                                                                                                        elif spankcounterinto == 2:
                                                                                                            bo"All you had to do was shut up and let me have my way"
                                                                                                        elif spankcounterinto == 3:
                                            
                                                                                                            bo"Just a kid you said, eh!?" with vpunch
                                                                                                        else:
                                                                                                            scene ino hairgrab2_2spankedx2 with dissolve:
                                                                                                                zoom 1.5 xalign 0.5 yalign 1.0
                                                                                                            bo"Or maybe I won't!"
                                                                                                            bo"That same kid will now ruin you, bitch!"
                                                                                                            
                                                                                                            show inohair_doubletap1 with moveinleft
                                                                                                            $ renpy.sound.play("/audio/soun_fx/intro/spank5.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                                                                            show inohair_doubletap1 with vpunch
                                                                                                            scene black with vpunch
                                                                                                            $ renpy.sound.play("/audio/soun_fx/intro/bodythud.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                                                                                            "*Thud*"
                                                                                                            bo"Oops! There she goes..."
                                                                                                            
                                                                                                            jump letgo

                                                                                                        show inohair_doubletap1 with moveinleft
                                                                                                        $ renpy.sound.play("/audio/soun_fx/intro/spank5.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                                                                        show inohair_doubletap1 with vpunch
                                                                                                        show ino hairgrab2_2spankedx2 with dissolve
                                                                                                        hide inohair_doubletap1 with dissolve
                                                                                                        if spankcounterinto == 0:
                                                                                                            ino"No m-more... P-please..."
                                                                                                        elif spankcounterinto == 1:
                                                                                                            ino"W-why are you d-doing this!?"
                                                                                                        elif spankcounterinto == 2:
                                                                                                            $ renpy.sound.play("/audio/soun_fx/inocrying3.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                                                                            ino"*Sobbing*"
                                                                                                        elif spankcounterinto == 3:
                                                                                                            $ renpy.sound.play("/audio/soun_fx/intro/screamwoman.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                                                                                                            ino"Aaaaaaaaaaaaargh!!!"
                                                                                                            bo"Okay, Okay. I get it, you are in pain. Maybe I'll stop... You don't have to wail about it!"
                                                                                                        else:
                                                                                                            $ renpy.sound.play("/audio/soun_fx/intro/bodythud.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                                                                            scene black with vpunch

                                                                                                            jump letgo

                                                                                                        jump inorepeating2
                                                                                                "Ino was battered by your abuse... Exhausted, she braced herself on all fours."
                                                                                                bo"Now this is a more appropriate stance, Ino..."
                                                                                                bo"Do me a favor and stay like that, will you?"
                                                                                                "You could hear her breathing slow down. A few more hits would probably make her lose her senses..."
                                                                                                ino"Fuck you, you piece of shit!"
                                                                                                menu:
                                                                                                    "..."
                                                                                                    "Give her a little push":
                                                                                                        bo"Still resiliant I see,"
                                                                                                        scene black with dissolve
                                                                                                        "You give her a little 'push'"
                                                                                                        $ renpy.sound.play("/audio/soun_fx/intro/bodythud.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                                                                        ino"Augh!" with vpunch

                                                                                                    "Spank her again!":
                                                                                                        bo"You never learn..."
                                                                                                        show ino_hairgrabspank with moveinright
                                                                                                        $ renpy.sound.play("/audio/soun_fx/intro/spank6.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                                                                        show ino_hairgrabspank with vpunch
                                                                                                        hide ino_hairgrabspank with dissolve
                                                                                                        show inohair_doubletap2 with moveinright
                                                                                                        $ renpy.sound.play("/audio/soun_fx/intro/spank8.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                                                                        show inohair_doubletap2 with vpunch
                                                                                                        show ino hairgrab2_5_9 with dissolve
                                                                                                        hide inohair_doubletap2 with dissolve
                                                                                                        bo"Do you... you stupid bitch!"

                                                                                                "Ino could no longer support herself on her hands..."
                                                                                                label inolast:
                                                                                                    scene bginofinal1 with dissolve
                                                                                                    show ino vaginal4 with dissolve:
                                                                                                        zoom 1 xalign 0.5 yalign 0.1
                                                                                                    ino"Ugh... N-no more..."
                                                                                                    scene black with dissolve
                                                                                                    "She was on the brink of unsconsciousnes"
                                                                                                    "But that didn't stop you..."
                                                                                                    hide ino
                                                                                                    scene bginofinal1 with dissolve
                                                                                                    show ino hairgrab3_1 with dissolve:
                                                                                                        zoom 1 xpos 105
                                                                                                    "You pulled on her hair, forcing her gaze towards you..."
                                                                                                    bo"Look at you now..."
                                                                                                    bo"This could have been much easier you know..."
                                                                                                    show ino hairgrab3_2 with dissolve:
                                                                                                        zoom 1.3
                                                                                                    ino"Not there... p-please!"
                                                                                                    scene black with dissolve
                                                                                                    "You let go of her hair and instead..."
                                                                                                    scene bginofinal1 with dissolve
                                                                                                    hide ino
                                                                                                    show ino hairgrab3_2 with dissolve:
                                                                                                        pos (146, -622) 
                                                                                                    "You moved her little thong to the side, exposing both of her holes to yourself..."
                                                                                                    bo"To think that a mature lady such as you was hiding these goods..."
                                                                                                    bo"Not even my fantasies could match the real deal!"
                                                                                                    show ino vaginal4 with dissolve:
                                                                                                        zoom 1 xalign 0.5 yalign 0.1
                                                                                                    ino"Don't..."
                                                                                                    ino"T-touch me..."
                                                                                                    "But Ino was utterly exhausted. There was nothing she could do."
                                                                                                    hide ino
                                                                                                    show ino hairgrab3_2 with dissolve:
                                                                                                        pos (146, -622) 
                                                                                                    "She was at your mercy.."
                                                                                                    menu ravagefinalinomenu:
                                                                                                        "..."
                                                                                                        "Put her to sleep":
                                                                                                            "One last spank would surely make her lose her senses..."
                                                                                                            menu:
                                                                                                                "..."
                                                                                                                "Do it!":
                                                                                                                    bo"You know, this would be much easier..."
                                                                                                                    show ino_hairgrabspank with moveinleft:
                                                                                                                        zoom 1.5 yalign 0.9 xzoom(-1) xpos 0.05
                                                                                                                    hide ino_hairgrabspank
                                                                                                                    $ renpy.sound.play("/audio/soun_fx/intro/spank5.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                                                                                    show ino_hairgrabspank2 with vpunch:
                                                                                                                        zoom 1.5 yalign 0.9 xzoom(-1) xpos 0.05
                                                                                                                    pause 0.5
                                                                                                                    hide ino_hairgrabspank2 with dissolve
                                                                                                                    bo"If you sat still!"
                                                                                                                    ino"Uhh..."
                                                                                                                    ino"..."
                                                                                                                    scene black with dissolve
                                                                                                                    $ renpy.sound.play("/audio/soun_fx/intro/bodythud.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                                                                                                                    "*Thud" with vpunch
                                                                                                                    scene ino faintedravage with dissolve:
                                                                                                                        zoom 1.025 xalign 0.5 yalign 0.95
                                                                                                                    pause 1
                                                                                                                    "Ino could not handle your abuse anymore..."
                                                                                                                    "She fell face first onto the ground..."
                                                                                                                    jump letgo
                                                                                                                "Reconsider":
                                                                                                                    bot"I want her to feel me as I penetrate her little holes!"
                                                                                                                    jump ravagefinalinomenu
                                                                                                                
                                                                                                        "Penetrate her pussy":
                                                                                                            label inopenetratepussy:
                                                                                                                bo"But we got this far, Ino..."
                                                                                                                hide ino
                                                                                                                show inovaginal with dissolve:
                                                                                                                    pos (159, -590) 
                                                                                                                show spankbruises with dissolve:
                                                                                                                    zoom 1 pos (131, -581) alpha 0.7

                                                                                                                
                                                                                                                bo"Would be a shame to stop here..."
                                                                                                                $ renpy.sound.play("/audio/soun_fx/genericsexsound2.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                                                                                                                "You started rubbing your cock around her vulva..."
                                                                                                                ino"..."
                                                                                                                ino"...Ugh... N-n.......... N-no..."
                                                                                                                ino"..."
                                                                                                                "Ino let out a few silent moans, but it was clear she was almost entirely unconsciouss..."
                                                                                                                bo"You wouldn't mind..."
                                                                                                                bo"If I pushed it in! Would you!?"
                                                                                                                menu:
                                                                                                                    "..."
                                                                                                                    "Push it in":
                                                                                                                        hide spankbruises
                                                                                                                        hide inovaginal
                                                                                                                        hide ino
                                                                                                                        $ renpy.sound.play("/audio/soun_fx/pushitin2.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                                                                                                                        show ino vaginal4 with vpunch:
                                                                                                                            pos (159, -590)
                                                                                                                        
                                                                                                                        "You pushed the tip in... It would prove difficult to fully penetrate her."
                                                                                                                        bo"Y-you are... so tight!"
                                                                                                                        ino"..."
                                                                                                                        bo"But we can't stop here!"
                                                                                                                        menu:
                                                                                                                            "..."
                                                                                                                            "Push harder!":
                                                                                                                                $ renpy.sound.play("/audio/soun_fx/pushitin1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                                                                                                                                pause 0.1
                                                                                                                                show ino vaginal5 with vpunch
                                                                                                                                bo"Aaarh!"
                                                                                                                                bo"Your pussy is so fucking tight, Ino!"
                                                                                                                                show ino with dissolve:
                                                                                                                                    zoom 1 pos (55, -40)
                                                                                                                                "Ino seemed to have passed out. The overwhelming stress and abuse she endured at your hands proved to be too much for her..."
                                                                                                                                hide ino
                                                                                                                                show ino vaginal5 with dissolve:
                                                                                                                                    pos (159, -590)
                                                                                                                                bo"But I want to feel all of you!"
                                                                                                                                hide ino with dissolve
                                                                                                                                show ino vaginal4 with dissolve:
                                                                                                                                    zoom 0.6 xpos 576
                                                                                                                                bo"It's time I take what I want, what I need! "
                                                                                                                                menu:
                                                                                                                                    "..."
                                                                                                                                    "Fuck her":
                                                                                                                                        $ ino_fainted = True
                                                                                                                                        jump hinatainterferes
                                                                                                                                
                                                                                                                                
                                                                                                                        
                                                                                                                        

                                                                                                                
                                                                                                                
                                                                                                        "Penetrate her asshole":
                                                                                                            label inopenetrateasshole:
                                                                                                                bo"But we got this far, Ino..."
                                                                                                                hide ino
                                                                                                                show inoanal with dissolve:
                                                                                                                    pos (159, -590) 
                                                                                                                show spankbruises with dissolve:
                                                                                                                    zoom 1 pos (131, -581) alpha 0.7


                                                                                                                bo"Would be a shame to stop here..."
                                                                                                                $ renpy.sound.play("/audio/soun_fx/genericsexsound2.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                                                                                                                "You started rubbing your dick around her asshole..."
                                                                                                                "Occasionally poking it with the tip of your cock."
                                                                                                                ino"..."
                                                                                                                ino"...Ugh... N-n.......... N-no..."
                                                                                                                ino"..."
                                                                                                                "Ino let out a few silent moans, but it was clear she was almost entirely unconsciouss..."
                                                                                                                bo"You wouldn't mind..."
                                                                                                                bo"If I pushed it in! Would you!?"
                                                                                                                menu:
                                                                                                                    "..."
                                                                                                                    "Push it in":
                                                                                                                        hide spankbruises
                                                                                                                        hide inoanal
                                                                                                                        hide ino
                                                                                                                        $ renpy.sound.play("/audio/soun_fx/pushitin2.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                                                                                                                        show ino anal1 with vpunch:
                                                                                                                            pos (159, -590)
                                                                                                                        "You tried to push the tip in... But It would prove difficult to fully penetrate her."
                                                                                                                        bo"Your little asshole is so tight, Ino..."
                                                                                                                        ino"..."
                                                                                                                        bo"But we can't stop here!"
                                                                                                                        menu:
                                                                                                                            "..."
                                                                                                                            
                                                                                                                            "Push harder!":
                                                                                                                                $ renpy.sound.play("/audio/soun_fx/pushitin1.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                                                                                                                                pause 0.1
                                                                                                                                show ino anal1_2 with vpunch
                                                                                                                                bo"Aaarh!"
                                                                                                                                "You only manage to get part of the tip in..."
                                                                                                                                bo"I can't believe how hard your asshole is gripping me..."
                                                                                                                                bo"I am about to explode and I am not even halfway inside of you yet!"
                                                                                                                                show ino with dissolve:
                                                                                                                                    zoom 1 pos (55, -40)
                                                                                                                                "Ino seemed to have passed out. The overwhelming stress and abuse she endured at your hands proved to be too much for her..."
                                                                                                                                hide ino
                                                                                                                                $ renpy.sound.play("/audio/soun_fx/pushitin1.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                                                                                                                                show ino anal3 with dissolve:
                                                                                                                                    pos (159, -590)
                                                                                                                                "You take out the tip trying to loosen her anus..."
                                                                                                                                bo"But I want to feel all of you!"
                                                                                                                                bo"I want to fuck the shit out of you!"
                                                                                                                                hide ino with dissolve
                                                                                                                                $ renpy.sound.play("/audio/soun_fx/pushitin2.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                                                                                                                                show ino anal1_2 with dissolve and vpunch:
                                                                                                                                    zoom 0.6 xpos 576
                                                                                                                                bo"I can't resist this gaping little asshole of yours"
                                                                                                                                bo"It's time I take what I want, what I need! "
                                                                                                                                menu:
                                                                                                                                    "..."
                                                                                                                                    "Fuck her asshole":
                                                                                                                                        $ ino_fainted = True
                                                                                                                                        jump hinatainterferes
                                                                                                    
     

                                                                                    "Force her on her knees":
                                                                                        ino"*Sobbing*"
                                                                                        ino"S-someone, a-anyone p-please, save me from this nightmare..."
                                                                                        scene black with dissolve
                                                                                        bo"No-one is around, Ino. Can't you see!?"
                                                                                        "You violently shoved Ino on the ground" with vpunch
                                                                                        show inoforcebj 0 with dissolve
                                                                                        "She fell on her knees and looked up to you with a defiant look..."
                                                                                        ino"Y-you monster!"
                                                                                        ino"S-stay away from me!!"
                                                                                        bo"Ooh, such a defiant look Ino."
                                                                                        bo"Don't you cry on me now, you know what's coming..."
                                                                                        ino"Screw you!!"
                                                                                        menu:
                                                                                            "..."
                                                                                            "Slap her":
                                                                                                show ino_faceslap with moveinright:
                                                                                                    zoom 2.5 yalign 0.2 xzoom(-1) 
                                                                                                    pos (-868, 0.26)
                                                                                                $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                                                                with vpunch
                                                                                                show inoforcebj 1_1 with dissolve:
                                                                                                    xzoom (-1)
                                                                                                pause 0.1
                                                                                                hide ino_faceslap with dissolve
                                                                                                ino"Ah!"
                                                                                                bo"Bitch!"
                                                                                                bo"That will teach you to talk back!"
                                                                                                show inoforcebj 1_2 with dissolve
                                                                                                ino"Y-you..."
                                                                                                bo"Come on! Open up!"
                                                                                                "She looks up to you with a scared look on her face. Her previous defiant look almost faded."
                                                                                                ino"Y-you fucking m-monster..."
                                                                                                bo"Hah! Can't blame you for that one I suppose."
                                                                                                bo"No matter. You will suck my dick whether you like it or not!"
                                                                                                menu:
                                                                                                    "..."
                                                                                                    "Put it on her face":
                                                                                                        show inoforcebj 1_3 with dissolve
                                                                                                        bo"Come on now, open up..."
                                                                                                        bo"Or I will have to do it myself!"
                                                                                                        ino"I..."
                                                                                                        ino"I c-can't... Please."
                                                                                                        bo"So you need a little help I see..."
                                                                                                        menu:
                                                                                                            "..."
                                                                                                            "Cock slap her":
                                                                                                                "You move your hips sideways and..."
                                                                                                                $ renpy.sound.play("/audio/soun_fx/spank4.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                                                                                show cockslap with vpunch
                                                                                                                pause 0.5
                                                                                                                show cockslap2 with dissolve
                                                                                                                bo"Open. Up!"
                                                                                                                ino"Ewwh.."
                                                                                                                scene cockslap with dissolve
                                                                                                                "Your cock was repeatedly tapping and rubbing her cheek..."
                                                                                                                ino"N-no, p-please..."
                                                                                                                jump helpher
                                                                                                            "''Help' her'":
                                                                                                                label helpher:
                                                                                                                    bo"*Sigh"
                                                                                                                    show inoforcebj 3_2 with dissolve:
                                                                                                                        xzoom (1)
                                                                                                                    "You stand right above her with your knees slightly bent so that your cock would rest on her face while grabbing the back of her head and pushing her towards you"
                                                                                                                    bo"Do I have to do everything myself?"
                                                                                                                    ino"Y-you can't do this to me, p-please!"
                                                                                                                    menu:
                                                                                                                        "..."
                                                                                                                        "Rub it against her":
                                                                                                                            show inoforcebj 3_4 with vpunch
                                                                                                                            bo"I can do whatever I damn please!"
                                                                                                                            show inoforcebj1anim with dissolve
                                                                                                                            $ renpy.sound.play("/audio/soun_fx/genericsexsound2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                                                                                            "You grab the back of her head and start rubbing your cock against the side of her face."
                                                                                                                            bo"To think that only some years ago..."
                                                                                                                            bo"You used to babysit me..."
                                                                                                                            bo"Now my dick is rubbing against your smeared face"
                                                                                                                            bo"I can't hold on much longer, Ino..."
                                                                                                                            hide inoforcebj1anim
                                                                                                                            show inoforcebj 3_9 with vpunch
                                                                                                                            bo"It's time you service my cock!"
                                                                                                                            menu:
                                                                                                                                "..."
                                                                                                                                "Force it in":
                                                                                                                                    show inoforcebj 4_1 with dissolve
                                                                                                                                    bo"Come on, Ino! Open up!"
                                                                                                                                    $ renpy.sound.play("/audio/soun_fx/inocrying3.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                                                                                                    ino"*Sobbing"
                                                                                                                                    ino"N-no!"
                                                                                                                                    $ renpy.sound.play("/audio/soun_fx/pushitin1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                                                                                                                    show inoforcebj 4 with vpunch
                                                                                                                                    bo"Then I'll do it myself!"
                                                                                                                                    "You pressed the tip of your cock against her lips but Ino kept clenching her mouth as hard as she could..."
                                                                                                                                    
                                                                                                                                    jump hinatainterferes
                                                                                                            
                                                                                                    
                                                                                                    





                                                                                                
                                                                                            "Approach her":
                                                                                                show inoforcebj 2 with dissolve
                                                                                                bo"Your defiance only emboldens me Ino..."
                                                                                                bo"This would be much easier for both of us if you were... compliant."
                                                                                                menu:
                                                                                                    "..."
                                                                                                    "Put your cock in front of her":
                                                                                                        show inoforcebj 2_1 with dissolve
                                                                                                        bo"You will suck on this..."
                                                                                                        bo"Whether you like it or not!"
                                                                                                        ino"Don't come any closer your fucking creep!"
                                                                                                        menu:
                                                                                                            "..."
                                                                                                            "Get closer":
                                                                                                                show inoforcebj 2_1_2 with dissolve
                                                                                                                "You stood right above her, your cock hanging above her face"
                                                                                                                bo"Come on, open up... Or I will have to force it in!"
                                                                                                                bo"Which way will it be, Ino!?"
                                                                                                                ino"F-fuck y-you! You piece of shit!"
                                                                                                                menu:
                                                                                                                    "..."
                                                                                                                    "Slap her":
                                                                                                                        show ino_faceslap with moveinleft:
                                                                                                                            zoom 2.5
                                                                                                                            pos (140, -0.3) 
                                                                                                                        $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.5)

                                                                                                                        with vpunch
                                                                                                                        pause 0.1
                                                                                                                        show inoforcebj 2_1_3_1 with dissolve
                                                                                                                        hide ino_faceslap with dissolve
                                                                                                                        bo"Don't talk back to me, whore!"
                                                                                                                        bo"You keep disobeying me and this gets worse!"
                                                                                                                        show inoforcebj 2_1_3_2 with dissolve
                                                                                                                        ino"P-please, don't hit me..."
                                                                                                                        jump areyousure
                                                                                                                    "Are you sure about this, Ino?":
                                                                                                                        label areyousure:
                                                                                                                            bo"Are you sure you want me to do it myself, Ino?"
                                                                                                                            
                                                                                                                            show inoforcebj 2_1_3 with dissolve
                                                                                                                            "You could see it in her eyes,her defiance was overshadowed by her fear of what was to come "
                                                                                                                            bo"I don't think you thought things through..."
                                                                                                                            ino"..."
                                                                                                                            scene black with dissolve
                                                                                                                            ino"W-what do you... m-mean..."
                                                                                                                            "You circle around her a few times..."
                                                                                                                            "Ino could not dare to move or turn around to watch you..."
                                                                                                                            "You suddenly stop behind her..."
                                                                                                                            $ renpy.sound.play("/audio/soun_fx/inogag3.opus", channel="sfx2", loop=False, relative_volume = 0.9)
                                                                                                                            ino"Agh!!" with vpunch
                                                                                                                            show inoforcebj 2_1_4 with vpunch
                                                                                                                            bo"You keep this fucking mouth of yours wide open or I swear, I will put you to sleep and have my way with you bitch!"
                                                                                                                            scene black with dissolve
                                                                                                                            scene inoforcebj 2_2 with dissolve:
                                                                                                                                zoom 1.02
                                                                                                                            "You stand above her once more, this time her mouth slightly open. It would seem you broke her resistance..."
                                                                                                                            menu:
                                                                                                                                "..."
                                                                                                                                "Good girl...":
                                                                                                                                   bo"Now that is a face I like..."
                                                                                                                                   bo"Wasn't too hard was it, Ino?"
                                                                                                                                   bo"Now be a good girl and open up!"
                                                                                                                                   $ renpy.sound.play("/audio/soun_fx/inocrying3.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                                                                                                   show inoforcebj 2_3 with dissolve
                                                                                                                                   ino"It is... n-not going t-to fit..."
                                                                                                                                   ino"P-please d-don't do this..."
                                                                                                                                   show inoforcebj 2_4 with dissolve
                                                                                                                                   "You press your cock right against her lips. One little push and you would bury it inside her mouth."
                                                                                                                                   bo"There is no turning back now, Ino!"
                                                                                                                                   bo"It is time I get rid of this fucking pain!"
                                                                                                                                   menu:
                                                                                                                                    "..."
                                                                                                                                    "Force it in":
                                                                                                                                        bo"Don't be shy now..."
                                                                                                                                        show inoforcebj 2_5 with dissolve
                                                                                                                                        ino"N-no... hnnng..."
                                                                                                                                        "The tip sunk under her upper lip, but fitting the entire thing in would be a tall task..."
                                                                                                                                        bo"Just a little bit more..."
                                                                                                                                        menu :
                                                                                                                                            "..."
                                                                                                                                            "Force it in!":
                                                                                                                                                jump hinatainterferes
                                                                                                                                                
                                                                                                                                            
                                                                                                                                            
                                                                                                                                   
                                                                                                                                    
                                                                                                                                   
                                                                                                                                   
                                                                                                                                "Slap her!":
                                                                                                                                    bo"Do I spot some defiance in your look, Ino!?"
                                                                                                                                    ino"N-no!"
                                                                                                                    
                                                                                                                                    show dream_hinaslap 1 zorder 10:
                                                                                                                                        xpos 1000
                                                                                                                                    show dream_hinaslap 1 zorder 10:
                                                                                                                                        easeout 0.3 xpos 90
                                                                                                                                    
                                                                                                                                    pause 0.3
                                                                                                                                    show dream_hinaslap 2
                                                                                                                                    $ renpy.sound.play("/audio/soun_fx/spank8.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                                                                                                                    pause 0.1
                                                                                                                                    $ renpy.sound.play("/audio/soun_fx/femalegrunt1.opus", channel="sfx3", loop=False, relative_volume = 0.3)
                                                                                                                                    with vpunch
                                                                                                                                    
                                                                                                                                    pause 0.1
                                                                                                                                    hide dream_hinaslap 1
                                                                                                                                    hide dream_hinaslap 2
                                                                                                                                    show inoforcebj 2_2slap
                                                                                                                                    with dissolve
                                                                                                                                    bo"You just don't get it, do you!?"
                                                                                                                                    show inoforcebj 2_2slap2 with dissolve
                                                                                                                                    ino"U.....uh..."
                                                                                                                                    "Your slaps combined with Ino's overwhleming stress seemed to be pushing her towards unconsiousness..."
                                                                                                                                    bo"Ohhh, poor girl..."
                                                                                                                                    bo"Have you gone and lost it?"
                                                                                                                                    show inoforcebj 2_2slap3 with dissolve
                                                                                                                                    ino"..."
                                                                                                                                    bo"Not what I was planning... but I can work with that!"
                                                                                                                                    menu :
                                                                                                                                        "..."
                                                                                                                                        "Facefuck her":
                                                                                                                                            scene black with dissolve
                                                                                                                                            "You give her a little push so that she falls on her back..."
                                                                                                                                            $ renpy.sound.play("/audio/soun_fx/intro/bodythud.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                                                                                                                                            "*Thud" with vpunch
                                                                                                                                            jump facefuckino
                                                                                                                                        "Let her fall face first":
                                                                                                                                            scene black with dissolve
                                                                                                                                            "You take a step back so that her lifeless body falls face first into the ground..."
                                                                                                                                            $ renpy.sound.play("/audio/soun_fx/intro/bodythud.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                                                                                                                                            "*Thud" with vpunch
                                                                                                                                            show ino faintedafterslap with dissolve
                                                                                                                                            bo"Oops..."
                                                                                                                                            jump letgo

                                                                                                
                                                                            "Expose her ass":
                                                                                $ inoplaytits = False
                                                                                $ inoplayass = True
                                                                                
                                                                               
                                                                                scene black with dissolve
                                                                                "You easily drag her back in..."
                                                                                show bg ino with dissolve:
                                                                                    blur 20
                                                                                show inogropeass 3a with vpunch:
                                                                                            zoom 0.7 xalign 0.5
                                                                                menu:
                                                                                    bo"You get that ass over here..."
                                                                                    "Fuck her thighs":
                                                                                        show inogropeass 3a with vpunch:
                                                                                            zoom 0.7 xalign 0.5
                                                                                        bo"You get that ass over here..."  
                                                                                        bo"And you stay on top of my dick as long as I want you to!"
                                                                                        "You drag her back in and shove your cock in between her thighs while making sure to grab a handful of her ass, raising it up towards you."
                                                                                        "Ino put her hands between  yours trying to push you away, but you would not budge."
                                                                                        $ renpy.sound.play("/audio/soun_fx/intro/gruntwoman2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                                                        ino"EEK!"
                                                                                        ino"Y-YOU CAN'T TOUCH ME DOWN THERE! S-STOP IT!"
                                                                                        bo"Oh I can..."
                                                                                        show inogropeass 3b:
                                                                                            zoom 0.7 xalign 0.5
                                                                                        bo"And I will!" with vpunch
                                                                                        "You squeezed her ass tightly..."
                                                                                        "And started playing with it"
                                                                                        show inogropeassnaked1 with dissolve:
                                                                                            zoom 0.7 xalign 0.5
                                                                                        bo"How does it feel Ino... or should I say, auntie!?"
                                                                                        bo"The little boy you used to nanny is now playing with your ass and shoving his cock between your legs!"
                                                                                        bo"For an old hag though I have to say, you do have a sweet ass on you..."
                                                                                        ino"You are disgusting!"
                                                                                        ino"Y-you won't get away with this!"
                                                                                        bo"Oh yeah?"
                                                                                        hide inogropeassnaked1
                                                                                        show inogropeass 3_1 with vpunch
                                                                                        bo"And what are you going to do about it!"
                                                                                        "You spread her ass apart and shoved your cock deeper between the gap you created between her thighs."
                                                                                        "Your sudden thrust caused Ino to lose balance. She used the railing behind you to stabilize herself but in the process, she unwillingly gave you free reign of her ass."
                                                                                        ino"EEEEEK! N-NO!"
                                                                                        bo"That's right, Nothing!"
                                                                                        show inogropeass 3_2 with vpunch
                                                                                        bo"*Grunts"
                                                                                        "You pushed as deep as you could..."
                                                                                        show inogropeassnaked2 with dissolve:
                                                                                            zoom 0.7 xalign 0.5
                                                                                        $ renpy.sound.play("/audio/soun_fx/jerkoff1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                                                        "And started fucking her thighs while playing with her ass"
                                                                                        ino"Y-YOU BRUTE!"
                                                                                        ino"S-stop this at once!"
                                                                                        "Powerless as she was, Ino started sobbing while you carelessly played around with her ass, she kept begging and pleading for you to stop..."
                                                                                        menu:
                                                                                            "..."
                                                                                            "Spread her pussy":
                                                                                                bo"Stop...?"
                                                                                                hide inogropeassnaked2
                                                                                                show inogropeass 3_6
                                                                                                bo"But I am only getting started!" with vpunch
                                                                                                "You dragged her panties and previously ripped fishnets aside, your cock now brushing against the entrance to her pussy!"
                                                                                                "One little push and you would penetrate whichever hole you pleased."
                                                                                            "Spread her anus":
                                                                                                bo"Stop...?"
                                                                                                hide inogropeassnaked2
                                                                                                show inogropeass 3_4
                                                                                                bo"But I am only getting started!" with vpunch
                                                                                                "You dragged her panties and previously ripped fishnets aside, your cock now brushing against the entrance to both of her holes!"
                                                                                                "One little push and you would penetrate whichever hole you pleased."
                                                                                        $ renpy.sound.play("/audio/soun_fx/inocrying3.opus", channel="sfx2", loop=False, relative_volume = 0.5)    
                                                                                        ino"N-no! NOT THERE! P-pleaseeee! *sobbing*"
                                                                                        bo"Aww, don't you start crying now Ino..."
                                                                                        bo"We still have ways to go, you know."
                                                                                        bo"Playing with your firm ass, it is getting me real excited!"
                                                                                        ino"No..."
                                                                                        bo"Perhaps it is time I take what I need, what I... want!"
                                                                                        ino"Y-you can't!"
                                                                                        jump finalinomenu
                                                                        
                                                                                                                        
                                                                
                                                        "Tell her how you really feel":
                                                            bo"You don't know me, Ino!"
                                                            bo"I have always lusted over you! Only now..."
                                                            bo"Something compels me to take you on the spot!" with vpunch
                                                            show inogropetitsanim with dissolve:
                                                                zoom 0.5 xalign 0.5
                                                            $ renpy.sound.play("/audio/soun_fx/kyaa.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                            ino"Kyaaa!"
                                                            ino"W-what are you doing!?"
                                                            ino"Have you no m-morals, y-you m-monster?"
                                                            jump inoescapes
                                                    
                                                        
                                        "Play with her ass":
                                            $ inoplaytits = False
                                            $ inoplayass = True
                                            bo"Oh you poor girl..."
                                            
                                            scene black with dissolve
                                            show bg ino:
                                                blur 20
                                            show inogropeass 3a:
                                                zoom 0.7 xalign 0.5
                                            with dissolve
                                            "You pull her towards you, restraining her moves with your overwhelming strength and pressing your cock between her thighs."
                                            ino"A-ah! NO!" with vpunch
                                            ino"[bo_name], w-what are you doing!?"
                                            ino"Y-you are just a kid, you can't do this to me!"
                                            ino"What would your [hin_rel] think of you!?"
                                            

                                            menu:
                                                bo"..."
                                                "Grope her ass!":
                                                    show inogropeassnaked1 with dissolve:
                                                        zoom 0.7 xalign 0.5
                                                    bo"I don't give a fuck about that right now..."
                                                    bo"In fact, whenever you visited my [hin_rel], I would always be just a few feet away..."
                                                    bo"Hidden in the bathroom, fantasizing about fucking your sexy ass beneath those tempting fishnets of yours..."
                                                    bo"To think that now, I could do just that!"
                                                    ino"What the hell are you talking about, [bo_name]! This isn't you! The [bo_name] I know would never do or say such wicked things!"
                                                    ino"Let me go right this moment!"
                                                    menu:
                                                        "..."
                                                        "I thought we've been through this already...":
                                                            bo"I though we've been through this already, Ino! This isn't me..."
                                                            hide inogropeassnaked1
                                                            show inogropeass 3_1 with dissolve
                                                            bo"Which is exactly why I will ravage your holes and have zero remorse about it!" with vpunch
                                                            ino"Y-you m-monster..."
                                                        "Tell her how you really feel":
                                                            bo"You don't know me, Ino!"
                                                            bo"I have always lusted over you! Only know..."
                                                            hide inogropeassnaked1
                                                            show inogropeass 3_1 with dissolve
                                                            bo"Something compels me to take you on the spot!" with vpunch
                                                            ino"Have you no m-morals, y-you m-monster!?"
                                            jump inoescapes

                                "Go further!":  
                                    
   
                                    bo"You know nothing of me, Ino!"
                                    if inoplaytits == True:
                                        show inogropetits 2 with dissolve:
                                            zoom 0.5
                                        bo"If only you knew..."
                                        "You sunk your hands deep into her breasts and rubbed them together, up and down, left and right!"
                                        bo"This is all I ever wanted!  I fantasized about fucking your tits countless times."
                                        ino"What the hell are you saying!? This cannot be you, [bo_name]"
                                        show inogropetits 3 with dissolve
                                        "Ino struggled to break free, eventually falling back and grabbing a nearby railing..."
                                        ino"Let me go, y-you demon!"
                                        "This was your opportunity to push it further!"
                                        menu :
                                            "..."
                                            "Expose her tits":
                                                show inogropetits 3_1 with dissolve
                                                ino"Eek!"
                                                bo"Not before I savour those sagging tits of yours!"
                                                ino"No!"
                                                ino"You are just a kid..."
                                                ino"You can't touch me there!"
                                                show inogropetits 3_2 with vpunch:
                                                    zoom 0.8 xalign 0.5 yalign 0.3
                                                bo"Oh I can, and I will!"
                                                jump getnaked

                                    if inoplayass == True:
                                        bo"If only you knew..."
                                        show inogropeass 1_2 with dissolve
                                        "You raised her skirt and pushed her ass cheecks up and towards you..."
                                        "Ino's hands were pressing against your shoulders trying to break free, but your strength was overwhelming, you did not even budge."
                                        bo"This is all I ever wanted!  I fantasized about fucking you sensless countless times."
                                        ino"No! P-please [bo_name], you can't touch me there!"
                                        menu:
                                            "..."
                                            "Play with her ass":
                                                bo"Oh I can and I will!"
                                                show inoplayassanim with dissolve:
                                                    zoom 0.7 xalign 0.5
                                                "You kept sinking your hands deep into her meaty ass, grabbing, spreading and moving it around as you pleased."
                                                "At times, you spread her ass cheeks far apart enough, that her little puckered asshole would peek through her panties."
                                                ino"You f-freak! Get off of me!"
                                                bo"But your ass feels so nice and firm Ino!"
                                                bo"Would be a crying shame to let it go... I am thinking I want more of it!"
                                                menu :
                                                    "..."
                                                    "Spread her asshole":
                                                        hide inoplayassanim
                                                        show inogropeass 1_4 with vpunch
                                                        ino"EEEK!"
                                                        bo"I can't wait to bury my dick deep inside there!"
                                                        ino"NOOO!" with vpunch
                                                            
                                                        ino"What the hell are you saying!? This cannot be you, [bo_name]"
                                                        show inogropeass 1_2
                                                        "Ino was struggling to break free..." with hpunch
                                                        ino"Let me go, you demon!"
                                                        ino"This isn't you! I know you better than that!"
                                                        menu:
                                                            "..."
                                                            "Get rough with her":
                                                                label inoassplay:
                                                                    bo"No, Ino..."
                                                                    scene black with dissolve
                                                                    bo"This is me. The same sweet boy you used to nanny..."
                                                                    show inogropeass 2 with vpunch:
                                                                        zoom 0.7 xalign 0.5
                                                                    bo"That boy is now spreading your ass apart!"
                                                                    ino"NOOOOO! YOU FUCKING FREAK. LET ME GO!"
                                                                    "Ino lost her balance trying to fight you off. She fell onto the nearest railing and grabbed on to it to stabilize herself."
                                                                    "Only now, you had a much better grip on her waist as you were supported by the railing behind your back."
                                                                    bo"I did warn you that making a fuss will only make this worse, did I not, Ino?"
                                                                    menu:
                                                                        "..."
                                                                        "Rip her fishnets":
                                                                            show inogropeass 2_2 with dissolve
                                                                            "You rip a small hole in her fishnets. You could feel the softened skin around her pussy at the edge of your fingers."
                                                                            ino"EEEEK!"
                                                                            bo"You scream again and I destroy you down there, understood?"
                                                                            ino"Y-you fucking psycho! Don't touch me!"
                                                                        
                                                                    
                                                                    menu:
                                                                        "..."
                                                                        "Spread her pussy":
                                                                            show inogropeass 2_1 with vpunch
                                                                            bo"Do I feel some... wetness down there?"
                                                                            ino"D-don't touch me!"
                                                                            ino"We are under the rain you fucking idiot!"
                                                                            show inospreadpussy:
                                                                                zoom 0.7 xalign 0.5
                                                                            bo"Just making sure!"
                                                                            "You move your fingers around her labia, spreading her pussy and occasionaly gliding your fingers around her pussy's lips"
                                                                            ino"EEEEK!" with vpunch
                                                                            jump getnaked
                                                                                
                                                                                

                                                                        "Spread her ass":
                                                                            bo"Do I feel some... wetness down there?"
                                                                            ino"D-don't touch me!"
                                                                            ino"We are under the rain you fucking idiot!"
                                                                            show inogropeass anus with vpunch
                                                                            bo"Don't mind me, just an excuse to feel your little asshole!"
                                                                            show inospreadanus:
                                                                                zoom 0.7 xalign 0.5
                                                                            bo"Don't mind me, just an excuse to feel your little asshole!"
                                                                            "You move your fingers around her asshole, spreading her ass and pussy, occasionaly gliding your fingers around her asshole's creased skin."
                                                                            ino"EEEEK!" with vpunch
                                                                            jump getnaked
                                                                label getnaked:
                                                                    ino"Nononono!"
                                                                    ino"YOU CAN'T TOUCH ME LIKE THAT! SOMEONE HELP ME!!"
                                                                    bo"Stop fucking screeching you banshee bitch!"
                                                                    "You needed a way to silence her..."
                                                                    menu:
                                                                        "..."
                                                                        "Slip a finger inside" if inoplayass == True:
                                                                            jump inofree
                                                                        "Pinch her nipples" if inoplaytits == True:
                                                                            jump inofree
                                                                    label inofree:
                                                                        bo"If you don't shut the fuck up, I swear this will turn into your worst nightmare!"
                                                                        scene black with vpunch
                                                                        ino"N-never!"
                                                                        "As soon as your grip weakened, Ino used the opportunity to momentarily break free"
                                                                        
                                                                        show bg ino with dissolve
                                                                        show inotransparent at left with dissolve:
                                                                            zoom 0.47
                                                                        ino"*Panting"
                                                                        "Ino in her short moment of reprive, frantically pulled down her clothes and instinctively covered her erogenous zones..."
                                                                        "She was afraid to make a move, fearing what your reaction would be..."
                                                                        ino"Y-you monster... Stay away from me!"
                                                                        "Her back was turned towards you, It would seem she did not yet realize your sinister intentions..."
                                                                        hide inotransparent with dissolve
                                                                        show boruto boner2t with dissolve
                                                                        bo"Ino, you poor girl..."
                                                                        bo"You must be so afraid of what I have become..."
                                                                        bo"Not even able to look me in the eyes..."
                                                                        show boruto boner3t with dissolve
                                                                        bo"My sweet auntie, forgive me..."
                                                                        ino"Why would you do that, [bo_name]?"
                                                                        ino"How could you do that to me!?"
                                                                        show boruto boner4t with dissolve
                                                                        bo"Forgive me, auntie..."
                                                                        
                                                                        scene bg ino with dissolve
                                                                        show boruto masturbating at right with dissolve:
                                                                            zoom 0.4 xzoom -1
                                                                        show inotransparent at left with dissolve:
                                                                            zoom 0.47
                                                                        ino"..."
                                                                        bo"For this is about to get much worse!"
                                                                        ino"W-what are you saying [bo_name]... Snap out of it! Please!"
                                                                        bo"Still hanging on blind hope..."
                                                                        show boruto masturbating at right:
                                                                            easein 0.4 xpos 0.93
                                                                        bo"This IS me you whore! There is nothing to snap out of!"
                                                                        bo"Turn around and marvel at me!"
                                                                        
                                                                        show inotransparent at left with dissolve:
                                                                            xzoom (-1)
                                                                            zoom 0.47
                                                                        "Ino turns around, only to see you completely naked and stroking your cock."
                                                                        show inotransparent at left:
                                                                            easein 0.3 xpos -0.10
                                                                        $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                                                                        ino"*Gasps" with vpunch
                                                                        ino"...W-why are you naked!?"
                                                                        ino"Y-you are not thinking of doing... that!?"
                                                                        bo"The things I will do to you... you have no idea!"
                                                                        ino"NO-no-no-no-no! STAY AWAY!"
                                                                        "Ino panicked, she tried to run away but..."
                                                                        show boruto masturbating at right:
                                                                            easein 0.2 xpos 0.80
                                                                        scene ino dragback with vpunch:
                                                                            zoom 1.1 xalign 0.1
                                                                        $ renpy.sound.play("/audio/soun_fx/intro/gruntwoman2.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                                                                        "You snap at her before she could react"
                                                                        bo"Did I not say you are mine to do with as I please!?"
                                                                        jump inorepeatingmenu
                                                                    
                                                            "Deceive her":
                                                                jump deceive

                                                        
                                                    
                                                    
                                    #she tries to escape

                                    

                                

                        "Grope her ass":
                            $ inoplaytits = False
                            $ inoplayass = True
                            bo"I don't think you understand, Ino..."
                            scene black
                            show bg ino:
                                blur 20
                            with dissolve
                            "You turned her around and..."
                            show inogropeass 1 with dissolve:
                                zoom 0.7 xalign 0.5
                            ino"EEEK!"
                            bo"You are mine to do with as I please!"
                            show inogropeass 1_1 with vpunch
                            "You sunk your hands deep into her skin, spreading her ass around."
                            ino"AHHH! NO! W-WHY!?"
                            ino"T-this isn't like you [bo_name]! P-please!"
                            #she tries to escape
                            jump inorepeatingstart    

                    menu:
                        "[bo_name] in his blind rage chose to:"
                        "Pin her down":                            
                            #cg on the floor doggy
                            bo"Shut up!"
                            bo"You are taking my cock whether you like it ir not!"
                            #cg2 dog




                            jump hinatainterferes
                        "Force her on her knees":
                            bo"Enough squeeling."
                            "[bo_name] forcibly pushed Ino down on her knees."
                            #cg2 ino on knees, crying
                            ino"Please! W-why!?"
                            ino"[bo_name], it is me, can't you recognize me?"
                            ino"Is it really you?"
                            bo"Silence!"
                            bo"It's time you put that loud mouth of yours to use for something more useful."
                            menu:
                                "..."
                                "Facefuck her":
                                    #cg2 ino on knees, crying, cock on face
                                    bo"Open up. Or I will force my way through."
                                    ino"Noooo! P-please!"
                                    jump hinatainterferes
                                
                                
                                          
                
        "Try to warn her":
            bo"Ino, I.. I can't control myself"
            bo"I... Something is... taking over me..."
            bo"Consuming me..."
            bo"I need you to... I have to...!"
            $ renpy.sound.play("/audio/soun_fx/eye1s.opus", channel="sfx3", loop=False, relative_volume = 0.5)    
            show kurama2 with flash
            show kurama2:
                easein 1 alpha 0.0
            beast"DO NOT DARE TO RESIST ME, PUNY HUMAN!"
            bo"Aaaaargh!" with vpunch
            scene black
            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            "[bo_name] lunged at her!" 
            scene ino sitting 3 with fade
            call increaselust pass (80) from _call_increaselust_41 
            "You grasped Ino's left arm, applying firm pressure, so as to keep her within reach."
            "Ino, while a capable Kunoichi back in her active days, was utterly powerless in this moment. As much as she tried to pull away..."
            "It would quickly become apparent to her, that [bo_name]'s unusual strength, perhaps a side-effect of his current condition, would prohibit any attrempts of escape."
            "Such being the case, Ino resorted to her only available option..."
            ino"[bo_name], what... w-what are you doing? P-please... let go of me. This isn't like yourself."
            ino"*Whimpers*"
            bo"N-not like m-my self?"
            bo"Ino, y-you don't understand..."
            bo"For fuck's sake! I don't understand!" with vpunch
            menu:
                bo"For fuck's sake! I don't understand!"
                "{color=[hatredcolor]}Surrender to your urges{/color}":
                    $ renpy.sound.play("/audio/soun_fx/eye4s.opus", channel="sfx3", loop=False, relative_volume = 0.5)    
                    show kurama1 with flash
                    show kurama1:
                        easein 2 alpha 0.0
                    beast"Yes... YES! LET ME IN!"
                    "[bo_name] succumbed to his unholy urges. His inhibitions no longer present."
                    bo"T-this is not what I want..."
                    bo"But it is what I need!" with vpunch
                    scene black
                    "[bo_name] harshly pushed Ino on the ledge where she was sitting."
                    scene ino grinding1 with dissolve
                    "He took the chance to feel her up, sinking his hands into her bottom."
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                    ino"Aaah! Don't touch me!" with vpunch
                    ino"[bo_name]! Have you gone fucking insane!?"
                    ino"Stop this at once!"
                    bo"Don't panic Ino. It will be quick, I promise."
                    menu:
                        "..."
                        "Take out your cock":
                            "[bo_name] lusting for Ino, quickly undressed..."
                            show ino grinding2 with dissolve
                            "He took out his erect cock and started forcibly grinding it against Ino's ass"
                            $ renpy.sound.play("/audio/soun_fx/kyaa.opus", channel="sfx3", loop=False, relative_volume = 0.2)
                            ino"Eeek!" with vpunch
                            ino"W-what the fuck are you doing!?"
                            bo"I just need a release, just stay right there!"
                         
                    ino"You can't do this to me [bo_name]! What would your [hin_rel] think of you!?"
                    "Ino, realizing the grim nature of the situation, tried to reason with you. Her voice was shaky, her eyes watery. She was on the verge of breaking down..."
                    "She could not fathom that the [hin_rel_to_bo] of her best friend would ever be doing this to her."
                    ino"P-please..." 
                    ino"Let go of me!"
                    menu:
                        "..."
                        "Raise her skirt":
                            bo"That's not happening, you are mine now."
                            show ino grinding3 with dissolve
                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                    ino"*GASP!" with vpunch
                    ino"No, no, no!"
                    ino"SOMEONE, PLEASE! HELP!" with vpunch
                    $ ino_spanked = False
                    menu:
                        "..."
                        "Spank her":
                            $ ino_spanked = True
                            bo"Enough squeeling!"
                            pause(0.6)
                            $ renpy.sound.play("/audio/soun_fx/intro/spank5.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                            show ino grinding3_s with vpunch
                            $ renpy.sound.play("/audio/soun_fx/gruntwoman2.opus", channel="sfx3", loop=False, relative_volume = 0.4)
                            pause(0.6)
                            show ino grinding3 spanked with dissolve:
                                zoom 1.5 xalign 0.1 yalign 0.1
                            ino"AAAH!"
                            "Ino let out another loud squeel, tears now flowing down her delicate face"
                            show ino grinding3 spanked with dissolve:
                                zoom 1
                            call changeDominance(1, "none") from _call_changeDominance_18
                            bo"Stay quiet! Disobedient girls get punished."
                            bo"You don't want to be punished... do you?"
                            ino"W-why... [bo_name], why!?"
                            menu:
                                "..."
                                "Lower her fishnets":
                                    
                                    jump testscene

                        "Lower her fishnets":
                            label testscene:
                                bo"Those have to go..."
                                if ino_spanked == True:
                                    show ino grinding4 spanked with dissolve
                                    $ renpy.sound.play("/audio/soun_fx/inocrying1.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                                    "You lowered her stockings. Revealing Ino's black thong. The last line of fabric seperating your throbbing cock, from her sensitive regions..."
                                    "A visible bruise was imprinted on her ass from your previous rough spanking."
                                else:
                                    show ino grinding4 with dissolve
                                    $ renpy.sound.play("/audio/soun_fx/inocrying1.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                                    "You lowered her stockings. Revealing Ino's black thong. The last line of fabric seperating your throbbing cock, from her sensitive regions..."
                                    $ ino_spanked = False
                                ino"Stop!...You m-monster."
                                ino"P-please!"
                                ino"*Sobbing"
                                "Ino was mortified. She was uncontrollably sobbing knowing her best friend's [hin_rel_to_bo] was about to penetrate her."
                                bo"You wouldn't understand..."
                                bo"Now sit there like a good girl..."
                                menu:
                                    bo"And allow me to rid myself of this pain!"
                                    "Spank her bare ass":
                                        bo"This is your fault!"
                                        $ ino_spanked = True
                                        $ renpy.sound.play("/audio/soun_fx/intro/spank7.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                        show ino grinding4 spanked2_b with vpunch
                                        pause(0.5)
                                        show ino grinding4 spanked2 with dissolve
                                        ino"AAAAAAH!!!!" with vpunch
                                        bo"You are such a fucking tease, Ino..."
                                        bo"You have made me like this... Now you will remedy your mistake! "
                                        "All Ino could do was let out defeated squeels..."
                                        "[bo_name] seemed to take some pleasure in breaking Ino's character."
                                        "Was it the effect of his condition?"
                                        menu:
                                            "Or did something sinister awaken inside him."
                                            "{color=[hatredcolor]}Spank her again{/color}":
                                                bo"Take this! You whore!"
                                                $ renpy.sound.play("/audio/soun_fx/intro/spank8.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                                scene ino grinding4 spankedfinal_b with vpunch
                                                pause(0.2)
                                                
                                                show ino grinding4 spankedfinal with dissolve
                                                ino"Hnnnnng!!"
                                                "As [bo_name] kept mercilessly spanking Ino's ass, she grinned her teeth in an attempt to deal with the pain."
                                                call changeHatred(1, "none") from _call_changeHatred_34
                                                bo"Now shut the fuck up!" with vpunch
                                                bo"It is time I put an end to the suffering... of both of us!"
                                                menu:
                                                    "..."
                                                    "{color=[hatredcolor]}Destroy her{/color}":
                                                        $ inospank = True
                                                        show ino grinding endings with dissolve
                                                        "You moved her panties to the side, exposing her clean shaven vulva..."
                                                        ino"Y-you can't touch me there. P-please!"
                                                        $ renpy.sound.play("/audio/soun_fx/growl1.opus", channel="sfx3", loop=False, relative_volume = 0.5)    
                                                        show kurama1 with flash
                                                        show kurama1:
                                                            easein 2 alpha 0.0
                                                        beast"..."
                                                        bo"I can..."
                                                        show inotestspank:
                                                            xpos 1000
                                                        show inotestspank:
                                                            easeout 0.2 xpos 0
                                                        pause 0.2
                                                        $ renpy.sound.play("/audio/soun_fx/intro/spank5.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                                        with vpunch
                                                        # hide inotestspank with dissolve 
                                                        bo"AND I WILL!"
                                                        scene black with dissolve
                                                        ino"..."
                                                        bo"Now loosen up!"
                                                        "Ino was completely silent..."
                                                        $ renpy.sound.play("/audio/soun_fx/intro/bodythud.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                                                        "*Thud..." with vpunch
                                                        "But not by choice..."
                                                        show ino_hinata 0 with dissolve
                                                        call changeHatred(1, "none") from _call_changeHatred_35
                                                        bo"Uuh, oops!"
                                                        "It appears she lost her consciousness after enduring your unrelenting abuse. The stress combined with the pain proved to be too much for her to bare."
                                                        "Her unresponsive body hit the floor..."
                                                        jump letgo

                                                    "Penetrate her":
                                                        jump penetrateher
                                                    
                                            "Penetrate her":
                                                jump penetrateher

                                    "Penetrate her":
                                        label penetrateher:
                                            if ino_spanked == True:
                                                show ino grinding4 spanked with dissolve:
                                                    zoom 1.1 xalign 0.7 yalign 0.5
                                                bo"You have made me like this... Now you will remedy your mistake!"
                                                window hide
                                                show ino grinding endings with dissolve
                                                pause 1
                                                window show
                                                "You moved her panties to the side, exposing her clean-shaven vulva..."
                                                ino"No! Y-you can't touch me there. P-please!"
                                                bo"Oh I'll do much more than touch you!"

                                                
                                            else:
                                                show ino grinding4 with dissolve:
                                                    zoom 1.1 xalign 0.7 yalign 0.5
                                                bo"You have made me like this... Now you will remedy your mistake!"
                                                window hide
                                                show ino grinding ending2 with dissolve
                                                pause 1
                                                window show
                                                "You moved her panties to the side, exposing her clean-shaven vulva..."
                                                ino"No! Y-you can't touch me there. P-please!"
                                                bo"Oh I'll do much more than touch you!"
                                            jump hinatainterferes
                

                "Find another way":
                    bo"I.. I-i don't know what to do!"
                    "[bo_name], with what little sense had yet to elude him, knew that what he was about to do, was unforgivable and strictly against his morals."
                    "Consumed as he was by his unreasonable urges, the only solution he could think of was..."
                    scene black with dissolve
                    bo"Ino, p-please just... Stay right there for a minute."
                    show inouse1 with dissolve
                    "[bo_name] pushed down on Ino's shoulder, compelling her to fall down on her knees."
                    "Ino looked up to him with tears in her eyes, her mind racing trying to figure a way out of this situation."
                    ino"[bo_name], w-what are you doing!?"
                    scene bg ino with dissolve
                    show boruto boner2t with dissolve
                    "Ino caught glimpse of [bo_name] fiddling with something under his pants"
                    "It was at that moment, Ino realized what he was referring to when he kept repeating that 'he needed this'."
                    show inouse2 with dissolve
                    ino"What the...!?"
                    ino"[bo_name], what are you planning to do! Think things through, be rational, please!"
                    hide inouse2 with dissolve
                    show boruto boner3t with dissolve
                    bo"It won't take long, I p-promise..."
                    show boruto boner4t with dissolve
                    bo"A-all you have to do is-"
                    scene black with dissolve
                    ino"N-n-no.. stay away from me!" with vpunch

                    scene inouse with dissolve
                    show boruto masturbating at left with dissolve:
                        zoom 0.4 xalign -0.4 yalign 0.8
                    "Ino could only watch with fear in her eyes as [bo_name] stood in front of her, maniacally gripping his erect cock with both hands."
                    "He seemed utterly lost in his troubles..."
                    bo"Ino, I..."
                    bo"I know, I shouldn't be doing this but..."
                    menu:
                        bo"I know, I shouldn't be doing this but..."
                        "Keep your distance":
                            bo"Y-you have to understand..."
                            bo"I n-need this... It hurts!"
                            ino"Stay away from me you weirdo!"
                            show halfblack with dissolve
                            dev"Congratulations! Allow me to break the 4th wall just this once in honor your monumental achievement!"
                            dev"You are literally the second coming of Jesus Christ himself (Or whatever god you believe in)."
                            dev"You have reached the end of this scene in the most humane way available to you"
                            dev"Since I expected that absolutely no one would be here, I must bestow upon you..."
                            call changeMoney(100) from _call_changeMoney_3
                            dev"Your reward!"
                            dev"Enjoy your 100 buckaroos for not being a depraved fuck!"
                            dev"Now back to the game!"
                            hide halfblack with dissolve
                            ino"Y-you..."
                            ino"You depraved FUCK!" with vpunch
                            ino"I hope a pigeon swoops down and bites your dick off!"
                            $ renpy.sound.play("/audio/soun_fx/intro/jerkoff2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                            bo"*Furiously masturbating*"
                            "You paid no attention to her remarks. All you could think about was getting rid of whatever was affecting you..."
                            bo"I... I am c-close!"
                            scene black with dissolve
                            jump hinatainterferes
                        "{color=[hatredcolor]}Surrender to your urges{/color}":
                            show boruto looking at left with dissolve:
                                easein 0.5 zoom 0.4 xalign -0.2
                    $ renpy.sound.play("/audio/soun_fx/growl2.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                    show kurama1 with flash
                    show kurama1:
                        easein 1 alpha 0.0
                    beast"He..he...he...heee... You cannot resist me!"
                    bo"Something is taking over me, and y-you are just so beautiful. Your sexy fishnets, your skimpy clothes."
                    bo"Whenever you visited my [hin_rel], I always used to fantasize about you."
                    show boruto masturbating with dissolve
                    $ renpy.sound.play("/audio/soun_fx/intro/jerkoff2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    "You started furiously masturbating in front of her..."
                    bo"I would go to the bathroom and think about all the ways I would have you while you were just outside!"
                    bo"I have blown so many loads thinking about you..."
                    bo"Only this time..."
                    menu:
                        bo"I get to blow one..."
                        "On your face":
                            show boruto masturbating at left with dissolve:
                                easein 0.3 zoom 0.4 xalign 0.0
                            bo"I get to blow one right on your face!"
                            ino"N-no! S-stay away you m-monster!" with vpunch
                            scene black with dissolve
                            "You approached her right as you were about to explode."
                            scene inouse4_1 with dissolve:
                                zoom 1.3 xalign 0.5 yalign 0.5
                            call changeDominance(1, "none") from _call_changeDominance_19
                            $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                            "Standing right over her thighs, you lowered your knees so that your cock would sit only a few inches above her face"
                            scene inouse4_1 with dissolve
                            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                            "Ino horrified at the sight of what was transpiring, took a glance at your towering cock, and quickly turned her attention to you..."
                            scene inouse4_2 with dissolve
                            ino"No, no no no! You promised not to touch me!"
                            ino"Stay away! You animal!!"
                            "Tears mixed with the rain, caused her mascara to start dripping down her face, as she kept trying to plead to you."
                            menu:
                                "..."
                                "Lose control":
                                    bo"I.. I can't, control, myself!"
                                    show inoforcebj 2_4 with dissolve
                                    $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                    "You lowered your cock closer to her mouth..."
                                    ino"W-what are you doing!?"
                                    ino"Y-you are too close!"
                                    ino"Don't even think a-abou-!"
                                    menu:
                                        ino"Don't even think a-abou-!"
                                        "Force it in":
                                            show inoforcebj 2_5 with vpunch
                                            $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                            $ renpy.sound.play("/audio/soun_fx/inogarggle1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                            ino"mmmhm! mm-No!!" with vpunch
                                            bo"I just can't resist the urge Ino!"
                                            call changeDominance(1, "none") from _call_changeDominance_20
                                            "You pressed the tip against her upper lip, one more push and you would violate her mouth."
                                            bo"I want to fill your throat with my seed!"
                                            $ renpy.sound.play("/audio/soun_fx/inogarggle1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                            ino"Mnnhmmmmm!!" with vpunch
                                            jump hinatainterferes
                                        "Cum in her mouth":
                                            show inoforcebj 2_5 with vpunch:
                                                zoom 1.2
                                            $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                            $ renpy.sound.play("/audio/soun_fx/gaspforair1.opus", channel="sfx3", loop=False, relative_volume = 0.3)
                                            ino"mmmhm! mm-No!!" with vpunch
                                            "You gently pressed the tip against her upper lip..."
                                            call changeDominance(1, "none") from _call_changeDominance_21
                                            bo"Open up, Ino! I want to fill your mouth with my seed!"
                                            ino"..."
                                            jump hinatainterferes
                                        
                                "Cum on her face":
                                    $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                    bo"Shut up, Ino. I am only going to plaster your face with my cum, not touch you."
                                    show inoforcebj 2_2slap3 with dissolve
                                    "Ino mortified by what else you were capable of doing, reluctantly sat motionless with closed eyes, awaiting the inevitable."

                                    jump hinatainterferes
                                
                               
                        "All over you":
                            show boruto masturbating at left with dissolve:
                                easein 0.3 zoom 0.4 xalign 0.0
                            $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                            bo"I get to blow one right all over you!"
                            ino"N-no! S-stay away you m-monster!" with vpunch
                            scene black with dissolve
                            "You approached her right as you were about to explode."
                            scene inouse4_1 with dissolve:
                                zoom 1.5
                            $ renpy.sound.play("/audio/soun_fx/intro/jerkoff2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                            "Standing right over her thighs, you lowered your knees so that your cock would sit only a few inches above her body"
                            call changeDominance(1, "none") from _call_changeDominance_22
                            "Ino horrified at the sight of what was transpiring, took a glance at your towering cock, and quickly turned her attention to you..."
                            scene inouse4_2 with dissolve
                            ino"No, no no no! You promised not to touch me!"
                            ino"Stay away! You animal!!"
                            "Tears mixed with the rain, caused her mascara to start dripping down her face, as she kept trying to plead to you."
                            $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                            bo"Shut up, Ino. I am only going to plaster you with my cum, not touch you."
                            "Ino mortified by what else you were capable of doing, reluctantly sat motionless with a defeated look on her face, awaiting the inevitable."
                            jump hinatainterferes
                    
                            
                        
                    

    label borutoturnstonormal:
        "Tsunade took a moment to change out of her cum-ridden clothes..."
        show halfblack2 with dissolve
        show boruto looking with dissolve:
            zoom 1 xalign 0.5 yalign 0.1
        show boruto blue 2 with longdissolve
        "As soon as you 'relieved' yourself on Tsunade... Whatever was affecting you seemed to subside for now."
        bot"Wait what!?"
        show boruto blue 1 with dissolve
        bot"NEXT TIME!?" with vpunch
        bot"Am I hearing things or did she really just say that..."
        bot"Have I been reincarnated as Giacomo Casanova!?" with vpunch
        bot"Come to think of it, what the fuck is going on anyway?"
        bot"I can't believe I just plastered lady Tsunade with my cum."
        bot"Not to mention that the pain from before is gone. Is this paradise? Have I finally perished?"
        hide boruto with dissolve
        "A few minutes pass as you contemplate everything that happened."
        hide halfblack2 with dissolve
        jump tsunadeending2



    label hinatainterferes:
        "[bo_name] was seconds away of doing something unforgivable."
        show blackscreen with dissolve
        "Before he could reach the point of no return, someone, alarmed by Ino's loud pleads for help, intervened..."
        show blackscreen with dissolve
        "A few moments earlier..."
        show hinata running with dissolve:
            subpixel True
            xalign 0.5 yalign 0.9
            zoom 1.25
            linear 4.0 yalign 0.1
        hide blackscreen with dissolve
        hin"Is that... Ino's voice!?"
        hin"She sounded..."
        hin"Disturbed."
        hin"I should see what's going on!"
        show blackscreen with dissolve
        "."
        ".."
        hide blackscreen with dissolve
        "[hin_name] approached the scene from afar"
        show hinata running2 with dissolve:
            subpixel True
            xalign 0.5 yalign 1.0
            zoom 1.25
            easein 5.0 yalign 0.3

        "She was in range to make out the silhouettes of whoever was involved, but not close enough to realize yet, what was occuring."
        hin"This...!"
        hide hinata running2 with flash
        hide blackscreen with vpunch
        hin"This looks like... assault?!"
        show blackscreen with dissolve
        hin"I should approach carefully and incapacitate whoever that is before they notice me!"
        show hinata running2 with dissolve:
           zoom 1.25
           xalign 0.5 yalign 0.3 
        "As [hin_name] got closer, the grim reality of what was transpiring quickly became apparent to her..."
        hide hinata
        show bg ino with dissolve
        show boruto masturbating with dissolve:
            subpixel True
            xalign 0.5 yalign 0.1
            zoom 0.42 xpos 1.00
        $ renpy.music.play("/audio/soun_fx/horror.opus", channel="sfx2", synchro_start=True, loop=False)
        hin"Is that..!?"
        hin"No... no, no, no!"
        hin"It... it can't be!"
        hide boruto
        hide bg ino
        hide blackscreen with dissolve
        "Her very own [hin_rel_to_bo], was about to violate her dear friend and former colleague."
        show bg ino with dissolve
        show hinata angryt with dissolve:
            zoom 0.5
            xalign 0.5
            yalign 0.5
        "[hin_name] being as cunning as she is, quickly realized that [bo_name] was likely affected by something."
        hint"There is a slight red glint in his eyes!"
        hint"Perhaps [bo_name] is under some sort of... influence?"
        hint"At least... I hope so"
        hint"Please let this be a fever nightmare, a genjutsu, anything but reality!"
        hint"My [hin_rel_to_bo] would never do this!"
        hide hinata
        show boruto masturbating with dissolve:
            subpixel True
            xalign 0.5 yalign 0.1
            zoom 1
        "[bo_name]'s senses tingled, he felt that someone else was nearby"
        show boruto looking with dissolve:
            subpixel True
            xalign 0.5 yalign 0.1
            zoom 1
        "He turned around only for his eyes to lock with his own [hin_rel_mother]..."
        bo"!"
        #eyes meet cg
        menu:
            bo"M-[hin_rel]!?"
            "Stay back or you will be next":
                show boruto masturbating with dissolve:
                    subpixel True
                    xalign 0.5 yalign 0.1
                    zoom 1
                $ renpy.sound.play("/audio/soun_fx/intro/jerkoff2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                bo"Stay back! Or I will have you next!"
                hide boruto with dissolve
                hide bg ino with dissolve
                hin"*Gasps"
                "[bo_name] still absorbed by his unsubduing lust, kept going at it with complete disregard of his own [hin_rel_mother]'s presence."

            "Ignore her and keep at it":
                show boruto masturbating with dissolve:
                    subpixel True
                    xalign 0.5 yalign 0.1
                    zoom 1
                $ renpy.sound.play("/audio/soun_fx/intro/jerkoff2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                bo"Enjoy the show, I suppose."
                hide boruto with dissolve
                hide bg ino with dissolve
                "[bo_name] kept going, as if his own [hin_rel] wasn't just a few feet away from him, watching him violate her friend."
                hin"*Gasps"

            "Take her too":
                show boruto masturbating with dissolve:
                    subpixel True
                    xalign 0.5 yalign 0.1
                    zoom 1
                hide boruto with dissolve
                hide bg ino with dissolve
                
                bo"If you want to join your friend... I will happily oblige!"
                hin"*Gasps"
            "I can explain":
                "The shock of realizing his [hin_rel] was there, brought back some sense back to [bo_name], but..."
                show boruto looking with dissolve:
                    subpixel True
                    xalign 0.5 yalign 0.1
                    zoom 1.1
                bo"M-[hin_rel]... I- I can explain!"
                hint"He is... conscious!?"
                hint"It can't be! There must be an explanation to this."
        hide boruto
        scene bg ino with dissolve
        show hinata angry2t with dissolve:
            zoom 0.4
            xalign 0.1

        show boruto masturbating with dissolve:
            zoom 0.4
            xalign 1.55
            pos (1.67, -59) 


        "[hin_name] knew this was not the time to lose composure."
        "She assumed a combat stance, readying the use of her bloodline's technique. One capable of putting anyone to sleep."
        stop music fadeout 3
        hin"Enough of this!"
        show hinata:
            linear 0.2 xpos 0.5

        show boruto:
            linear 0.4 ypos 1.3 xpos 2500
        play sound"/audio/soun_fx/suspense.opus" volume 0.4
        hide hinata with dissolve
        "[hin_name] quickly struck [bo_name]'s vital chakra points and put him into a temporary state of unconsiousness." with vpunch
        scene black with dissolve
        show boruto uncons with dissolve:
            zoom 1
            xalign 0.5 ypos 100
        "[bo_name] fell to the ground, still half-naked and exposed in front of his [hin_rel]."
        hint"My [hin_rel_to_bo]... Why!?"
        hide boruto with dissolve
        play music"/audio/ost/disaster.opus" volume 0.7 fadein 3
        hint"But Ino comes first..."
        # if ino unconscious
        if ino_fainted == True:
            scene black with dissolve
            hin"My good god, Ino!"
            show ino_hinata 0 with vpunch
            hin"Ino!"
            hin"Ino please, can you hear me? Wake up!"
            hint"Ino looks battered!"
            hint"This... wasn't [bo_name], was it?... He could never do this."
            hint"It can't be... Ino could easily fend for herself..."
            hint"What the hell is going on. There must be an explanation to this!"
            $ renpy.sound.play("/audio/soun_fx/femalecough2.opus", channel="sfx2", loop=False, relative_volume = 0.3)
            ino"*Cough *Cough*"
            show blackscreen with dissolve
            hide blackscreen with dissolve
            "Ino was falling in and out of consciousness."
            show ino_hinata 1 at dizzyflashshort with dissolve:
                pos (0.6, 1.04) xzoom 1.0 zoom 1.24


            hin"Ino!"
            hin"Can you hear me Ino!"
            show blackscreen with dissolve
            hide blackscreen with dissolve
            $ renpy.sound.play("/audio/soun_fx/femalecough1.opus", channel="sfx2", loop=False, relative_volume = 0.3)
            "She was hyperventilating for a while, coughing and gasping for air..."
            hin"Are you okay!?"
            show blackscreen with dissolve
            hide blackscreen with dissolve
            hin"Ino, please!"
            "Until she was able to speak a singular word..."
            $ renpy.sound.play("/audio/soun_fx/femalecough3.opus", channel="sfx2", loop=False, relative_volume = 0.3)
            ino "*Cough* *Cough*"
            ino"..."
            ino"...H-[hin_name]?"
            show black with dissolve
            hin"Yes, it's me Ino!"
            hide ino_hinata
            show ino_hinata 2
            with dissolve
            hin"Are you hurt!? Talk to me, Ino"
            ino"I..."
            $ renpy.sound.play("/audio/soun_fx/femalecough2.opus", channel="sfx2", loop=False, relative_volume = 0.3)
            ino"*Cough *Cough"
            "[hin_name] picked a tissue from her purse, and wiped Ino's dirty face as best as she could..."
            show ino_hinata 2_5 with dissolve
            hin"It's ok Ino..."
            hin"I am here with you."
            show ino_hinata 3 with dissolve
            "Ino was slowly regaining her consciousness, memories of what transpired only moments ago, quickly flooding her thoughts."
            ino"[hin_name]..."
            hin"You will be ok Ino, take your time."
            hin"I am right here with you."
            show ino_hinata final with dissolve
            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            ino"*Gasp" with vpunch
            ino"Is he still here?" with vpunch
            show ino_hinata 3 with dissolve
            $ renpy.sound.play("/audio/soun_fx/inocrying1.opus", channel="sfx2", loop=False, relative_volume = 0.3)
            "Ino started hyperventilating again, memories of abuse flooding her brain."
            "[hin_name] carresed her face, trying to reassure her friend that she will be okay."
            hin"It's okay, Ino..."
            hin"I... I put him to sleep."
            ino"*Heavy breathing"
            scene black with dissolve
            "Ino took a few seconds to calm down..."
            show ino_hinata final with dissolve
            ino"*Heavy breathing*"
            ino"[hin_name]..."
            ino"[hin_name]! W-why!?"
            ino"What... just happened!"
            ino"WHY!?" with vpunch
            hint"She must be so scared... traumatized even."
            hin"Ino..."
            "As much as [hin_name] tried to help... In that moment, Ino was emotionally broken. She seeked answers for which [hin_name] had none..."
            scene black with dissolve
            "She found enough strength to get on her knees..."
            show inoknees1 with dissolve
            ino"W-why..."
            $ renpy.sound.play("/audio/soun_fx/inocrying2.opus", channel="sfx2", loop=False, relative_volume = 0.3)
            "Ino helpleslly kneeled under the rain and burst into tears as she recounted her traumatizing experience."
            ino"WHY!?" with vpunch
            ino"Your own [hin_rel_to_bo], [hin_name]!"
            hin"Ino! I am so sorry..."
            ino"He tried to..."
            ino"He...!"
            ino"HE!..."
            scene black with dissolve
            $ renpy.sound.play("/audio/soun_fx/inocrying3.opus", channel="sfx2", loop=False, relative_volume = 0.4)
            "Ino could not get the words out... her emotions got the better of her. She fell into [hin_name]'s arms as she kept violently bawling."
            hin"It's okay... you are going to be okay."
            ino"*Crying"
            ino"H-he did... unspeakable things to m-me... [hin_name]."
            ino"I... I don-t understand."
            hin"I don't either, Ino."
            hin"I am sorry..."
            hin"We will figure this out together, okay?"
            "[hin_name] gave some time to Ino..."
        show ino ending with dissolve
        hint"Poor girl... she must be so scared"
        if ino_fainted == False:
            hin"Ino..."
            $ renpy.sound.play("/audio/soun_fx/inocrying1.opus", channel="sfx2", loop=False, relative_volume = 0.3)
            ino"[hin_name]! W-what's going on."
            ino"W-why.. would [bo_name_stutter] do this to me?"
            hin"Ino! I am so sorry..."
            hin"I.. I don't know exactly but..."
            #ino rage crying
            show ino ending rage with vpunch:
                zoom 1.5
                xalign 0.5
                yalign 1
            ino"Your [hin_rel_to_bo], [hin_name]! He tried to..."
            ino"He tried to..."
            ino"H-he-"
            hin"I... I know Ino. List-"
            ino"Why!?" with vpunch
            hin"..."
        scene ino ending with dissolve
        $ renpy.end_replay()
        hin"Ino... Listen please..."
        hin"I am not sure what is going on, but if there's one thing I know is that [bo_name] would never do something like that of his own accord."
        hin"I saw something... In his eyes, a strange glint of some sort..."
        hin"I don't know exactly what it was but perhaps something was affecting him."
        hin"I will rush [bo_name] to the infirmary and find out what is going on."
        hin"In the meantime, please try to compose yourself and rest assured..."
        hin"When [bo_name] is back to his senses I will have him personally apologize and explain himself to you."
        ino"..."
        
        ino"I... I don't understand."
        ino"This is all.. too much."
        ino"But... T-thank you... [hin_name]."
        if ino_fainted == True:
            hin"Will you be okay alone? Can you make it to the infirmatory yourself?"
            ino"[hin_name] please..."
            scene ino ending rage with dissolve
            ino"Just go. But know this..."
            ino"If there is no explanation for what your [hin_rel_to_bo] did to me..."
            ino"I swear on my family's name, he will die by my hands!"
            hin"..."
            hin"Ino, [bo_name] would never do that himself, I would stake my life of it!"
            hin"And even if he did, make no mistake, I will be right there with you when you do."
        ino"..."
        hin"..."
        hin"Be well... Ino."
        scene black with fade
        pause(1)
        show boruto uncons with dissolve:
            zoom 0.75
            xalign 0.5 yalign 0.5
        "[hin_name] turned to her unconscious [hin_rel_to_bo]..."
        "She carefully covered him up..."
        show boruto uncons with dissolve:
            zoom 1.5
            yalign 0.5
        "But unavoidably caught glimpse of his still erect cock"
        hint"..."
        scene black with fade
        "[hin_name] rushed to the infirmary to find out what was going on with [bo_name]"
        
        hint"[bo_name]... "
        show hinata running with dissolve:
            zoom 1.75
            xalign 0.5 yalign 0.05
        hint"You would never do something like that of your own accord, right?"
        hint"I hope that this has some logical explanation to it."
        hint"I have not raised you to be capable of... that."
        hint"And why would... Darn it!"
        hint"I need to hurry up, Lady Tsunade would surely have some answers about this... I hope"
        scene bg infirmary with fade
        "[hin_name] made it to the infirmary."
        "There resided a renowned medical practitioner known around the world for her immense medicinal knowledge..."
        stop music fadeout 1
        hin"I need to find her..."
        $ renpy.music.stop(channel="sfx1", fadeout=1)
        play sound "audio/soun_fx/dooropen.opus" volume 0.7
        play music"/audio/ost/house1.opus" volume 0.6
        "[hin_name] barged through the door" with hpunch
        show tsunade intro with dissolve:
            zoom 0.9
            subpixel True
            xalign 0.5 yalign 0.99
            linear 5.0 yalign 0.1
        "It was none other than lady Tsunade"
        "A former Hokage, powerful Kunoichi, and close comrade to [bo_name]'s [na_rel]."
        "If anyone knew what was troubling [bo_name], it would be her."
        hin"Lady Tsunade! This is an emergency!" with vpunch
        scene black with fade
        "[hin_name] explains the situation to Tsunade..."
        "Tsunade paces for a while, but eventually sits down on her desk"
        show tsunade intro2 with dissolve
        pause 1
        ts"Hmmm, I understand."
        ts"[hin_name]..."
        ts"I have a suspicion of what might be the case. I fear this might be connected to what his [na_rel] dealt with in the past..."
        ts"I will explain more once I confirm my hypothesis..."
        show tsunade intro2 with dissolve:
            zoom 1.4 xalign 1.0 yalign 0.0
        ts"Care to give me a few minutes alone with [bo_name]?"
        hin"Of course..."
        scene black with dissolve
        show bg clinic with dissolve
        show hina pthinking2 with dissolve
        hint"..."
        hint"It can't be...[na_name]'s past? Is [bo_name]... affected by that?"
        show hina pthinking with dissolve
        hint"I pray not. For his sake, and for everyone elses."
        label replaytsunadenaruto:
        $ initialize_replay_defaults()
        scene black with fade
        "Inside the doctor's office..."
        show exam1 with dissolve:
            zoom 0.80
            xalign 0.5
            yalign 0.5
        #tsunade boruto cg
        ts"This looks somewhat similar to what [na_name] dealt with in the past"
        ts"The Jinchūriki's curse must have been inherited, at least residually to [bo_name]."
        ts"The only problem is..."
        scene black with dissolve
        "Tsunade approached you..."
        show b1 with dissolve:
            zoom 1.2
            xalign 0.5
            yalign 0.5
        #boner cg
        ts"What's left of the curse seems to have manifested into sexual aggression, depravity and lust."
        scene black with dissolve
        "Tsunade removed your pants to examine your genital area."
        show b3 with dissolve:
            zoom 1
            xalign 0.5
            yalign 0.99
        
        ts"Oh my..."
        ts"If the curse is powerful enough to sustain... that—even while he is unconscious, I fear of what would transpire when he wakes up."
        hide b2 with dissolve
        show exam1 with dissolve:
            zoom 1.3
            xalign 0.1
            yalign 0.04
        ts"What [hin_name] described was horrific. I need to find a way to prevent potentially similar future occurrences."
        ts"And that thing needs to be taken care of somehow,  or everyone around him would be in grave danger."
        scene black with fade
        "Tsunade took a moment to ponder upon potential solutions..."
        show tsunade thinking with fade
        show tsunade thinking:
            easein 10 zoom 1.3 xalign 1.0 yalign 0.0
        "Her brow furrowed in deep thought. She replayed the details in her mind, searching for a viable plan."
        ts"Hmm..."
        ts"[bo_name]'s symptoms are quite different than those that troubled his [na_rel]."
        ts"I still remember those years..."
        #scene white with dissolve
        scene black with dissolve and flash
        "Years ago, [bo_name]'s [na_rel] was infamous for his bearing of the Jinchūriki's curse, the same curse that now appears to be troubling his [na_rel_to_bo]."
        show n0 with dissolve:
            zoom 0.75
            yalign 0.5 xalign 0.5
        "In his case, the curse manifested as violent aggression, often resulting in harm, or even death to those around him."
        "Shunned by society, [na_name] then an outcast, seeked acceptance from anyone that would embrace him as he was."
        show n1 with dissolve:
            zoom 0.75
            yalign 0.5 xalign 0.5
        "Tsunade was among the first people to embrace [na_name], serving as his teacher in combat but more importantly, in life."
        "She played a pivotal role in guiding him towards becoming an upstanding person, despite his flaws."
        show n2 with dissolve:
            zoom 0.75
            yalign 0.5 xalign 0.5
        "[na_name], having lacked a mother figure in his life, quickly grew fond of Tsunade and would look for every opportunity to get 'closer' to her."
        "At first she was annoyed at his clinginess but she tried her best to put up with him, knowing that he had a troubled upbringing, perhaps looking for compassion."
        "But [na_name] was getting attached, and as time passed, he grew more curious..."
        show n2_2 with dissolve:
            zoom 0.75
            yalign 0.5 xalign 0.5
        
        "And daring..."
        "Seeing Tsunade put up with his perversion, only fueled his curiosity..."
        show n3 with dissolve:
            zoom 0.75
            yalign 0.5 xalign 0.5
        "One thing led to another..."
        "And as time would pass, the two grew much closer..."
        scene black with fade
        $ renpy.sound.play("/audio/soun_fx/sexslaps1.opus", channel="sfx2", loop=False, relative_volume = 0.4)
        "Years went by and eventually, Tsunade decided it was time to impart to [na_name] one final lesson..."
        show n4 with dissolve:
            zoom 0.75
            yalign 0.5 xalign 0.5
        "That of becoming a man..."
        show n5 with dissolve:
            zoom 0.75
            yalign 0.5 xalign 0.5
        "Tsunade found in [na_name], that which she was lacking since she was widowed..."
        $ renpy.sound.play("/audio/soun_fx/genericsexsound.opus", channel="sfx3", loop=False, relative_volume = 0.4)
        show tsunadenaruto with dissolve:
            zoom 0.75
            yalign 0.5 xalign 0.5
        "A relationship of intimacy and indulgence. By now she would happily accept his advances, no matter how depraved."
        show n6_3 with dissolve:
            zoom 0.75
            yalign 0.5 xalign 0.5
        "She even started enjoying their 'closer' relationship and let herself plunge into pleasure."
        "The more she indulged his sexual advances..."
        show n7 with dissolve:
            zoom 0.75
            yalign 0.5 xalign 0.5
        $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx2", loop=False, relative_volume = 0.2)
        "The more she would come to enjoy her sexual deviance as well." with flash
        "For years they secretly kept up their debauchery, until [na_name] would eventually marry [hin_name]."
        scene black with dissolve
        scene tsunade thinking with dissolve
        "They might have put a pause to their intimate relationship, but their friendship lasts to this day."
        "And as history would have it, Tsunade was now in a similar predicament. This time with [na_name]'s [na_rel_to_bo]."
        $ renpy.end_replay()
        ts"If my suspicions are correct, the only way for [bo_name]'s urges to settle..."
        ts"Is for him to have..."
        ts"Some sort of... release."
        ts"..."
        ts"These poor people... First his [na_rel], now him. What terrible luck."
        ts"And how do I even begin to explain this situation to [hin_name]..."
        ts"*Sigh...*"
        label replaytsunadeboruto1:
        $ initialize_replay_defaults()
        ts"For now, someone has to deal with..."
        scene tsunade surprised with dissolve and vpunch:
            zoom 1.05
        ts"That..."
        scene black with dissolve
        show b3 with dissolve:
            zoom 1.24
            xalign 0.5 yalign 0.8
        show b3:
            easein 3 yalign 0.40
        ts"My lord! Is it growing bigger by the minute!?"
        ts"Could that mean he is close to waking up?"
        scene tsunade surprised with dissolve
        ts"Damn me! I spaced out."
        ts"I should hurry up..."
        scene tsunade thinking with dissolve:
            zoom 1.05
        ts"Otherwise, as soon as [bo_name] wakes up, everyone around him would be in grave danger."
        ts"I could call a nurse, but this situation is much more dangerous than it appears..."
        scene black with dissolve
        show b3 with dissolve:
            zoom 1.24
            xalign 0.5 yalign 0.4
        ts"I don't want to do this, but it must be done."
        scene black with dissolve
        ts"It is for... medical purposes after all."
        "Tsunade pulls a stool close to your bed..."
        scene tsunade jo1 with dissolve
        "And starts carefully stroking your erect cock in a reserved manner."
        ts"Oh my...It almost reaches up to his chest."
        ts"Can I even do this? I hope my hands will suffice..."
        scene tsunade jo2 with dissolve:
            zoom 1.15 xalign 0.99 yalign 0.99
        "As evident by the size of it, she had to use both hands to even have a chance at making you climax"
        scene tsunadeclinichj2 with dissolve
        "She expertly moved her hands up and down your shaft. Trying to make the process as quick as possible."
        scene tsunadeclinichj2 with dissolve:
            zoom 1.15 yalign 1.0
        "Her only indication of whether you were close or not was the precum that would slowly drip down your cock and onto her hands"
        scene tsunadeclinichj2 with dissolve:
            zoom 1.5 xalign 1.0 yalign 0.0
        ts"All this... slime. I should have probably used medical gloves."
        ts"This is taking longer than I expected, [hin_name] must be growing anxious..."
        ts"Seems like I will have to use my skills to their full extent."
        scene tsunade jo3cum1 with dissolve:
            subpixel True
            xalign 0.5 yalign 0.0
            zoom 1.15
            linear 2.0 yalign 1.0

        pause(2)
        "Tsunade put one hand under your scrotum, simultaneously massaging your testicles and using her fingers to apply pressure to your prostate gland."
        scene tsunadeclinichj2 with flash:
            xalign 0.5 yalign 0.3
            zoom 1.05
        ts"I think that did it!"
        scene tsunadeclinichj2 with dissolve
        $ renpy.sound.play("/audio/soun_fx/handjob4.opus", channel="sfx2", loop=False, relative_volume = 0.5)
        ts"I can tell he is close..."
        ts"My hand is covered with his excessive precum. Yuck.."
        scene black with dissolve
        show boruto waking1 with dissolve:
            zoom 1.7
            xalign 0.00
        "At that point, [bo_name] seemed to be regaining his consciousness."
        #boruto consciousness cg
        "Tsunade being solely focused on her task, had yet to realize that."
        show boruto waking2 with dissolve:
            zoom 1.6
            xalign 0.01
        bot"Ahh..."
        show boruto waking3 with dissolve:
            zoom 1.6
            xalign 0.01
        bot"Why am I feeling like I am about to bust..."
        bot"W-where... am I?"
        show tsunadeclinichj2 with dissolve:
            zoom 1.7
            xalign 0.5 yalign 0.01
        bot"I recognize her... That's Tsunade, a friend of my [na_rel]"
        window hide
        show tsunadeclinichj2:
            subpixel True
            xalign 0.5 yalign 0.01
            zoom 1.7
            linear 3.0 yalign 0.99
        $ renpy.pause(3.5, hard=True)
        #cg realize
        bot"...!" with vpunch
        hide tsunade
        hide tsunadeclinichj2
        show boruto waking4 with dissolve:
            zoom 1.7
            xalign 0.00
        bot"Is she... giving me a handy!? Is this a dream or something? Was I dropped on my head?"
        $ renpy.end_replay()
        default tsunaderough = False
        menu :
            bot"...!"
            "Pretend you are still unconscious":
                label replaytsunade_pretendasleep:
                $ initialize_replay_defaults()
                bot"Her hands around my cock... It feels way too good!"
                bot"I've no idea what the fuck is going on but if I pretend I am still asleep, there's a good chance she keeps this up..."
                show boruto waking2 with dissolve:
                    zoom 1.68
                    xalign 0.01
                bot"Hehe! You are so smart, [bo_name]!"
                scene tsunadeclinichj2 with dissolve
                ts"This is taking way too long... But I am also getting way too... *Sigh*"
                ts"It might be time to try a different approach..."
                bot"What does that mean!?" with vpunch
                show boruto waking2 with dissolve:
                    zoom 1.6
                    xalign 0.01
                bot"Please don't stop... please don't stop!"
                show boruto waking2 with dissolve:
                    zoom 1.8
                    xalign 0.01 yalign 0.1
                bot"!?" with vpunch
                bot"Is she...!?"
                show pretend0 with dissolve
                "Tsunade took of her heels and got on the clinic bed..."
                ts"Am I really about to do this...?"
                ts"But it should make things faster..."
                show pretend1 with dissolve:
                    zoom 1.1 xalign 0.99
                ts"Besides, it's not like I am not... intrigued, to say the least."
                show pretend1 with dissolve:
                    zoom 1.0
                bot"Holy shit!" with vpunch
                bot"This is defnitely not a dream!"
                bot"I can feel the matress sinking in..."
                show pretend1 with dissolve:
                    zoom 1.3 xalign 0.01 yalign 0.99
                bot"Her nylon-covered thighs pressing against mine..."
                show pretend1 with dissolve:
                    zoom 1.4 xalign 0.6 yalign 0.99
                bot"Her delicate hands wrapped around my cock!"
                bot"Holy s-shit I can't take this for much longer!"
                scene boruto waking2 with dissolve:
                    zoom 1.6
                    xalign 0.01
                "[bo_name] wanted to see Tsunade servicing his cock with his own eyes..."
                scene black with dissolve
                "But opening them would be risking the entire ordeal off. He could only feel or imagine what was transpiring..."
                show pretend2eyesanim1_t with dissolve
                "The sensations alone would still be enough to overwhelm him..."
                "His mind started racing with all the possibilities..."
                hide pretend2eyesanim1_t
                show pretendanim
                $ renpy.sound.play("/audio/soun_fx/handjob1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                bot"I can feel her heated breath on the tip of my prick!"
                bot"I she about to!?"
                "Her hands kept moving around your shaft, every twist and twirl bringing you closer to an explosion of pleasure."
                ts"It's just so... enticing!"
                ts"Certainly more potent than his [na_rel]'s..."
                bot"Huh!? [na_rel]??" with vpunch
                bot"Whatever, just... keep stroking me you deranged woman!"
                scene black with dissolve
                "You took note of her remark, but had no time to think about that right now."
                show pretend3 with dissolve
                ts"I just can't help but caress it..."
                ts"I am getting excited too... This brings back memories of old."
                ts"It's time to take it up a notch, see if I still got it!"
                scene black with dissolve
                bot"Fuck! I really wish I could see what's happening!"
                bot"Oh! Is she...?" with vpunch
                show pretend4eyes_t with dissolve
                bot"Is she climbing on top of me!?"
                bot"I can't handle any more of this fucking teasing, just suck me dry already!"
                show pretend5 with dissolve
                ts"My... Is it growing even bigger?"
                scene black with dissolve
                "Meanwhile, outside the room..."
                show bg clinic with dissolve
                show hina pthinking with dissolve
                hint"What could be taking so long..."
                show hina pthinking2 with dissolve
                hint"Shall I ask what's going on?"
                show pretend5 with dissolve
                ts"The sensation looks to be arousing to him even while he is unconscious."
                bot"Unconscious? If only you knew..."
                menu:
                    bot"I can't take this anymore!"
                    "{color=[hatredcolor]}Wake up and facefuck her{/color}":
                        bot"Bitch, I am awake! I am tired of this charade!"
                        call changeHatred(1, "none") from _call_changeHatred_36
                        bot"I am so temped to wake up and shove my cock deep inside your mouth till you beg for me to stop."
                        bot"In fact why don't I do just that! There's nothing to stop m-"
                    "Persevere...":
                        bot"If only I could wake up and-"
                    
                show pretend5_2:
                    zoom 1.2 xalign 0.9 yalign 0.01
                hin"L-lady Tsunade..." with vpunch
                $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                show pretend5_2:
                    zoom 1.3 xalign 0.9 yalign 0.01
                ts"{size=*0.8}Oh, shit!{/size}"
                bot"[hin_rel]!?"
                bot"'Oh shit' is right!"
                scene black with dissolve
                show bg clinic with dissolve
                show hina surprised at center with dissolve:
                    zoom 0.7
                hin"Is evertyhing okay? You seem to be taking a while..."
                show pretend5_2 with dissolve
                bot"Damn it, [hin_rel]! The timing could not be worse!"
                show pretend5_1 with dissolve:
                    zoom 1.05 xalign 0.99
                ts"E-everything is going as planned, [hin_name]."
                show pretend5_3 with dissolve
                ts"I am just a-administrating a unique treatment protocol to [bo_name_stutter]."
                bot"Good save, Tsunade!"
                ts"Just a few more minutes and we will be done, [hin_name]. Please bear with us!"
                hin"O-okay..."
                show pretend5_4 with dissolve:
                    zoom 1.2 xalign 0.99
                ts"{size=*0.8}Close call!{/size}"
                bot"Now keep on for fuck's sake, I am about to explode!"
                show pretend5_4 with dissolve:
                    zoom 1
                ts"I... I have to finish this up."
                ts"Perhaps it's time I use my..."
                bot"Oh god yes! Suck me dry please!"
                show pretend5 with dissolve:
                    zoom 1.2 xalign 0.99
                ts"I can't resist it..."
                ts"Just a little kiss, no one would ever know anyway..."
                $ renpy.sound.play("/audio/soun_fx/Suck Air 2.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                show pretend7 with dissolve
                "Tsunade was enthralled by your manhood..."
                show pretendani2 with dissolve
                $ renpy.sound.play("/audio/soun_fx/bjsfx.opus", channel="sfx2", loop=False, relative_volume = 1.4)
                "She gripped it with both hands and started violently stroking it, her rough movements making an audible 'flap' sound whenever she reached the base of your cock."
                "At the same time, she moved her lips back and forth around the glans, occasionaly giving it gentle kisses..."
                bot"H-holy s-shit!"
                bot"My lord, just one hip thrust and I'd explode deep inside her throat!"
                bo"*Moans*"
                ts"..."
                "Your audible moan did not stop her, she was fully invested in bringing you to climax."
                bo"A-a...ahh!"
                bo"*Loud moans*"
                bot"That's it! I am about to fucking explode!"
                bot"What if..."
                menu:
                    bot"What if..."
                    "{color=[hatredcolor]}Move your hips and thrust!{/color}":
                        bot"I can't take it anymore!"
                        call changeHatred(1, "none") from _call_changeHatred_37
                        bot"I want this bitch to choke on it!"
                        bot"Take..."
                        "Just as you were about to cum..."
                        scene black with dissolve
                        $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                        "You shifted your pelvis forward and..." with flash
                        $ renpy.sound.play("/audio/soun_fx/inogag4.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                        show force1 with vpunch:
                            zoom 1.2 xalign 0.99 yalign 0.01
                        $ renpy.sound.play("/audio/soun_fx/gags/SDTGag7.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                        "You forced your cock in her mouth." with vpunch
                        $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                        bo"Take this!" with flash
                        menu :
                            bo"Take this!"
                            "Cum down her throat":
                                $ renpy.sound.play("/audio/soun_fx/throatcum.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                with flash
                            
                            
                        show force1_3 with dissolve and flash:
                            zoom 1.1 xalign 0.99 yalign 0.01
                        "Before Tsunade could even react, your load excerted with such force, that it quickly filled her mouth and shot out of her nose..."
                        $ renpy.sound.play("/audio/soun_fx/gags/SDTGag23.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                        ts"Mmmh!"
                        call decreaselust(25) from _call_decreaselust_19
                        show force2 with vpunch and flash:
                            zoom 1.2 xalign 0.99 yalign 0.01
                        $ renpy.sound.play("/audio/soun_fx/cum11.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                        bo"A-aaahhh!!" with flash
                        bo"*Moans*"
                        call decreaselust(25) from _call_decreaselust_20
                        show force2 with vpunch and flash:
                            zoom 1.1 xalign 0.99 yalign 0.01
                        bo"There's more coming you whore!"
                        "Before you shot another load, Tsunade managed to back away just enough..."
                        $ renpy.sound.play("/audio/soun_fx/gags/SDTGag1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                        show force1_1 with dissolve:
                            zoom 1.05 xalign 0.99 yalign 0.01
                        "To avoid choking on your endless stream of cumshots..." 
                        $ renpy.sound.play("/audio/soun_fx/gags/SDTGag2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                        show force1_4 with flash
                        $ renpy.sound.play("/audio/soun_fx/cum4.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                        $ renpy.sound.play("/audio/soun_fx/chokecum1.opus", channel="sfx1", loop=False, relative_volume = 0.4)
                        "As soon as she managed to detach, a pool of drool and cum poured from her mouth, covering her chest and your shaft."
                        "She struggled to speak as her throat and sinuses were flooded with your comical amount of cum."
                        ts"*Cough Cough*... Eehww- *Cough*"
                        bo"*Moans*"
                        call decreaselust(25) from _call_decreaselust_21
                        $ renpy.sound.play("/audio/soun_fx/cough1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
                        ts"*Cough*... Y-you... *Cough*"
                        bo"One last..."
                        menu:
                            bo"One last..."
                            "Plaster her face":
                                $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                with flash
                              
                        show force1_5 with flash:
                            zoom 1.1 xalign 0.99 yalign 0.01
                        $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                        bo"F-final load straight to your face!" with flash
                        call decreaselust(25) from _call_decreaselust_22
                        scene black with dissolve
                        show forcedending1 with dissolve:
                            zoom 1.3 xalign 0.8 yalign 0.0
                        "Tsunade, drenched in your cum and in total awe of what transpired, removed one of her hands from your cock and braced herself on the bed."
                        show forcedending2 with dissolve:
                            zoom 1.2 xalign 0.8 yalign 0.0
                        "She kept watching, almost in fascination as the seemingly endless stream of sperm kept leaking from both your cock and her face."
                        $ renpy.sound.play("/audio/soun_fx/cough4.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                        scene forcedending1 with dissolve:
                            zoom 1.2 xalign 0.99 yalign 0.01
                        ts"*Cough* W-what the fu- *Cough*"
                        bo"Aww, is the doctor in trouble. Did you choke on your patient's cum!? Perhaps you need some further medical aid"
                        show forcedending3 with dissolve:
                            zoom 1.2 xalign 1.0 yalign 0.0
                        ts"Y-you little bastard... Were you awake all this time!?"
                        menu:
                            ts"Y-you little bastard... Were you awake all this time!?"
                            "'Apologize'":
                                bo"I've heard everything you were whispering to yourself, you are a perverse woman, aren't you Tsunade?"
                                ts"..."
                                bo"In any case, I got carried away. I am sorry for not saying anything."
                                ts"Y-you should be!"
                                ts"You treat me like that next time and I will make sure you regret it!"
                                scene black with dissolve
                                jump tsunadeending

                            "{color=[dominancecolor]}Own it{/color}":
                                bo"Don't act all high and mighty now, you immoral woman. I have heard how you spoke..."
                                call changeDominance(1, "none") from _call_changeDominance_23
                                bo"You enjoyed this... didn't you?"
                                
                                ts"T-that doesn't mean you can do with me as you like, *cough* y-you little shit!"
                                ts"*Cough* Damn y-you..."
                                ts"You treat me like a whore next time and it will be your last day on earth!"
                                scene black with dissolve
                                jump tsunadeending
                        
                    "{color=[dominancecolor]}Wake up and explode all over her!{/color}":
                        bot"I've had enough of this shit!"
                        scene black with dissolve
                        show grab hand
                        bo"Come here you crazy nympho!"
                        ts"W-what!?" with vpunch
                        show tsunade angry1_2 with dissolve:
                            zoom 0.5
                            xalign 0.5 yalign 0.5
                        bo"Don't act surprised! You started this!"
                        jump tsunadeexplode
                    "{color=[lovecolor]}Let it happen{/color}":
                        bot"I have no time to think! I-... I am about to..."
                        bot"If she doesn't move I'll cover her face!"
                        ts"It's coming... I can feel it."
                        $ renpy.sound.play("/audio/soun_fx/bj/Suck Air 19.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                        ts"Maybe... just a small t-taste..."
                        ts"F-for diagnostic purposes...y-yes."
                        menu:
                            bot"I can't hold it.."
                            "Cum":
                                $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                scene letit1 with flash:
                                    zoom 1.05 xalign 0.99 yalign 0.01
                        $ renpy.sound.play("/audio/soun_fx/gags/SDTGag11.opus", channel="sfx2", loop=False, relative_volume = 0.5)           
                        bo"A-ahh..."
                        call decreaselust(25) from _call_decreaselust_23
                        bo"*Moans*"
                        $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                        show letit1_1 with flash:
                            zoom 1.1 xalign 0.99 yalign 0.01
                        $ renpy.sound.play("/audio/soun_fx/cum2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                        bo"mm...mmm!" with flash
                        $ renpy.sound.play("/audio/soun_fx/throatpie.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                        "To your surprise, Tsunade did not budge. She took your load straight from the source."
                        "She kept slurping as much as she could manage by sucking on the tip but..."
                        menu:
                            bot"I'll fucking explode!"
                            "{color=[dominancecolor]}Explode in her mouth{/color}":
                                bot"This bitch is s-slurping it up..."
                                bot"Then you will enjoy this too!"
                                $ renpy.sound.play("/audio/soun_fx/cum6.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                show letit1_2 with vpunch:
                                    zoom 1.15 xalign 0.99 yalign 0.01
                                $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                bo"Hnng!" with flash
                                $ renpy.sound.play("/audio/soun_fx/gags/SDTGag13.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                ts"M-mmm!!"
                                $ renpy.sound.play("/audio/soun_fx/cum2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                bo"Ahh!!" with flash
                                #show cg
                                $ renpy.sound.play("/audio/soun_fx/cum7.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                show letit1_3 with flash:
                                    zoom 1.05 xalign 0.99 yalign 0.01
                                call decreaselust(25) from _call_decreaselust_24
                                "The overwhelming sensations you felt cumulated into an explosion of pleasure right into Tsunade's mouth."
                                $ renpy.sound.play("/audio/soun_fx/cum4.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                $ renpy.sound.play("/audio/soun_fx/gags/SDTGag19.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                ts"*Slurps*" with flash
                                $ renpy.sound.play("/audio/soun_fx/gags/SDTgag7.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                ts"Gl-urp..! Hn--hng"
                                $ renpy.sound.play("/audio/soun_fx/gags/SDTgag20.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                "She was caught by surprise, as you shot with enough force for the cum to reach her nostrils. Her throat and sinuses were flooded with your semen"
                                
                                scene black with dissolve
                                show letit2_3 with dissolve
                                $ renpy.sound.play("/audio/soun_fx/gaspforair2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                "Tsunade took a moment to recover while you kept ejaculating comical amounts of semen."
                                $ renpy.sound.play("/audio/soun_fx/gaspforair4.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                ts"*Cough Cough*"
                                $ renpy.sound.play("/audio/soun_fx/cum11.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                show letit2_4 with flash:
                                    zoom 1.07 xalign 0.99 yalign 0.01
                                $ renpy.sound.play("/audio/soun_fx/gaspforair1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                ts"Oh... m-my... *cough*"
                                call decreaselust(25) from _call_decreaselust_25
                                ts"That... I did not expect. B-but the taste of it..."
                                ts"It's intoxicating..."
                                $ renpy.sound.play("/audio/soun_fx/cum12.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                show coughing2 with flash 
                                bo"*Panting*" with flash
                                ts"D-does it never end!? It's like a hose..." with vpunch
                                ts"I.. I-have to s-stop it or the whole office will be a mess!"
                                scene black with dissolve
                                bot"Yes! Keep on sucking on it you nymphomaniac whore!"
                                call changeDominance(1,"none") from _call_changeDominance_24
                                $ renpy.sound.play("/audio/soun_fx/cum8.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                show letit3_2 with vpunch
                                $ renpy.sound.play("/audio/soun_fx/gags/SDTgag12.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                ts"Hn-mhm!" with flash
                                $ renpy.sound.play("/audio/soun_fx/gags/SDTgag19.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                ts"*Choking sounds*" with flash
                                $ renpy.sound.play("/audio/soun_fx/cum9.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                $ renpy.sound.play("/audio/soun_fx/gags/SDTgag15.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                ts"Glr-slurp..Hn-gnn!" with flash
                                menu:
                                    bo"!"
                                    "Fill her up!":
                                        $ renpy.sound.play("/audio/soun_fx/throatcum.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                                        show letit3_1 with flash:
                                            zoom 1.15 xalign 0.99 yalign 0.01
                                call decreaselust(50) from _call_decreaselust_26
                                "You shoot one last massive load down Tsunade's throat..."
                                $ renpy.sound.play("/audio/soun_fx/gags/SDTgag12.opus", channel="sfx3", loop=False, relative_volume = 1.0)
                                ts"Mmm..."
                                bot"Holy shit! She took it like a champ! I can still feel her lips around my cock!"
                                scene black with dissolve
                                bot"I can't believe she swallowed all of that while sucking me dry..."
                                bot"I never knew Tsunade was such a depraved woman..."
                                scene black with dissolve
                                bot"Well, there's no point keeping up the illusion anymore, is there?"
                                bot"It's time I open my eyes..."
                                show letit3_3:
                                    blur 15
                                call blink("...","Still a bit dizzy...","Oh m-") from _call_blink_1
                                show letit3_3 with dissolve:
                                    blur 0
                                hin"[bo_name_stutter]?"
                                show letit3_3 with dissolve:
                                    zoom 1.3 xalign 0.9
                                $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp1.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                                ts"!" with vpunch
                                scene bg clinic with dissolve
                                show hina pthinking2 with dissolve
                                "[hin_name] not knowing what was occuring, could faintly hear some grunting sounds she conceived as pain."
                                hin"Are you okay, [bo_name]?!"
                                show hina concerned at mid with dissolve:
                                    zoom 0.7
                                hin"It sounds like you are in pain..."
                                hin"Lady Tsunade, what's going on!?"
                                scene letit3_3 with dissolve
                                $ renpy.sound.play("/audio/soun_fx/femalegrunt1.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                                $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                                ts"*Panting* Huuuh.... Huuuuh..."
                                bot"Heh, this will be fun!"
                                show letit3_3 with dissolve:
                                    zoom 1.3 xalign 0.9 yalign 0.1
                                ts"It's a-alright [hin_name] *cough*, we are just about to wrap u-"
                                show letit3_4 with dissolve:
                                    zoom 1.0
                                "You interrupted her mid sentence..." with vpunch
                                bo"I am okay, [hin_rel]."
                                show letit3_4 with dissolve:
                                    zoom 1.2 xalign 0.99 yalign 0.01
                                $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp3.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                                ts"!? *Gasps*" with vpunch
                                "In that moment, Tsunade realized you have been awake for some time now..."
                                bo"Tsunade is just tending to my... treatment."
                                $ renpy.sound.play("/audio/soun_fx/cough1.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                                ts"{size=*0.8}Y-you... *cough* little shit!{/size}"
                                bo"I will be right there with you in just a moment. Don't be scared... okay?"
                                scene black with dissolve
                                show bg clinic with dissolve
                                show hina concerned at mid with dissolve:
                                    zoom 0.7
                                call changeLove("Hinata", 1, "none") from _call_changeLove_20
                                hin"Oh thank the lords, I am so relieved!"
                                hin"We will catch up soon then."
                                bo"Yes, we will..."
                                scene letit3_3 with dissolve
                                bot"I... I did that? She is drenched in my cum, what an absolute whore!"
                                menu:
                                    bot"I... I did that? She is drenched in my cum, what an absolute whore!"
                                    "{color=[hatredcolor]}Nice work, you nympho whore{/color}":
                                        call changeHatred(1,"none") from _call_changeHatred_38
                                        bo"Nice work, you nymphomaniac whore! I thoroughly enjoyed that"
                                        show letit3_4 with dissolve:
                                            zoom 1.1 xalign 0.99 yalign 0.01
                                        "Hearing you say that, Tsunade turned to you with an angry... but embarassed look."
                                        show letit3_4 with dissolve:
                                            zoom 1.0 xalign 0.99 yalign 0.01
                                        bo"Don't go looking at me like that now you crazy nympho... this was your idea!"
                                        "She wanted to protest but her throat was full of your semen"
                                        scene black with dissolve
                                        $ renpy.sound.play("/audio/soun_fx/cough4.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                        ts"*Cough* *Cough*"
                                        show forcedending2 with dissolve
                                        ts"*Cough* Y-you..."
                                        "She cleared some of the cum from her pipes by coughing it out and turned her attention to you..."
                                        show forcedending3 with dissolve:
                                            zoom 1.05 xalign 0.99
                                        ts"How long have you been awake for!?"
                                        bo"No reason to make a fuss now. Wouldn't want my [hin_rel] to find out about this, would you?"
                                        bo"Besides, I've heard every word you spoke, I know you enjoyed this..."
                                        bo"You wouldn't slurp all that cum up otherwise! Heh!"
                                        show forcedending3 with dissolve:
                                            zoom 1.1 xalign 0.99 yalign 0.01
                                        ts"T-that doesn't mean you can talk to me like that, *cough* y-you little shit!"
                                        scene forcedending2 with dissolve
                                        $ renpy.sound.play("/audio/soun_fx/cough1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                        ts"*Cough* Damn y-you..."
                                        show forcedending3 with dissolve:
                                            zoom 1.05 xalign 0.99
                                        ts"You treat me like a whore next time and it will be your last day on earth!"
                                        scene black with dissolve
                                        jump tsunadeending
                                    "That was amazing, Tsunade":
                                        bo"T-tsunade... that was amazing."
                                        ts"{size=*0.8}Are you p-proud of your *cough* l-little theatrics, you asshole?{/size}"
                                        scene black with vpunch
                                        $ renpy.sound.play("/audio/soun_fx/cough4.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                        ts"*Cough Cough*"
                                        show forcedending3 with dissolve:
                                            zoom 1.05 xalign 0.99
                                        "She cleared some of the cum from her pipes by coughing it out and turned her attention to you..."
                                        ts"{size=*0.9}How long have you been awake for?{/size}"
                                        bo"All along... but keep it quiet. We wouldn't want my [hin_rel] to find out about this..."
                                        ts"Y-you... I only did what I had to! Don't get any weird ideas."
                                        bo"Relax Tsunade, I heard everything you were whispering to yourself. I know you enjoyed it..."
                                        bo"Just as much as I did."
                                        ts"You little..."
                                        ts"You... you deceived me! You pull something like this next time and I'll make you regret it!"
                                        scene black with dissolve
                                        jump tsunadeending
                                  
                            "Warn her":
                                bo"T-tsunade...!"
                                show letit1_1 with dissolve:
                                    zoom 1.05 xalign 0.99 yalign 0.01
                                "Hearing your voice, Tsunade recoiled backwards..."
                                $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                show letit1_11 with flash:
                                    zoom 1 xalign 0.99 yalign 0.01
                                bo"C-careful, I am about to explode!" with flash
                                $ renpy.sound.play("/audio/soun_fx/cum5.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                show letit2_2 with flash
                                call decreaselust(25) from _call_decreaselust_27
                                ts"Y-you a-are awake!?" with vpunch
                                "She managed to back off just in time to avoid the stream of semen you excerted with violent force..."
                                show letit2_3 with flash
                                $ renpy.sound.play("/audio/soun_fx/cum6.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                bo"T-there's m-more..." with flash
                                bo"coming!" with flash
                                call decreaselust(25) from _call_decreaselust_28
                                ts"T-this is highly ab-bnormal..."
                                ts"H-how pent up were you!?"
                                bo"Hnn-gn!"
                                $ renpy.sound.play("/audio/soun_fx/cum7.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                show letit2_4 with flash
                                call decreaselust(15) from _call_decreaselust_29
                                ts"U-un...Unreal!"
                                bo"I... I am not d-done yet!"
                                $ renpy.sound.play("/audio/soun_fx/cum8.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                show coughing2 with flash
                                call decreaselust(10) from _call_decreaselust_30
                                "Tsunade was infatuated by the phenomenon. Her face now covered from colateral 'damage'"
                                ts"I've never seen anything like this... I w-want to..."
                                show force1_4 with dissolve
                                ts"E-examine it... c-closer."
                                $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                bo"*Heavy breathing*"
                                "Tsunade almost hypnotized by the vision and taste of your release, was within an inch of letting herself go entirely..."
                                bo"T-tsunade...?"
                                bot"W-what is she doing!?"
                                scene black with dissolve
                                ts"O...O-oh!"
                                "She stopped herself before she went too far..."
                                show letit2_1 with dissolve
                                ts"I got c-caught up in my th-thoughts..."
                                ts"This w-was a highly unusual procedure after all."
                                ts"L-listen [bo_name], it's a good thing you woke up when you did."
                                ts"But don't get the wrong idea, this was an one time thing."
                                ts"To... p-protect you... and us from your condition. It won't happen again next time I... examine you."
                                bo"Huh!?"
                                ts"I know you are confused... Let's clean up first. There's a lot to go through."
                                scene black with dissolve
                                jump tsunadeending
                            
            "Pull her towards your bed":
                label tsunadereplay_pullher:
                $ initialize_replay_defaults()
                scene boruto evil with dissolve:
                    zoom 1.6
                    xalign 0.01
                bot"I don't know what's going on. But I want more!"
                scene black
                show grab hand with vpunch
                bo"Come here, you crazy nympho!"
                scene black with vpunch
                $ renpy.sound.play("/audio/soun_fx/intro/gruntwoman1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                ts"Aghhh!" with vpunch
                "You forcibly pulled Tsunade's arm..."
                show tsunade ending choice with dissolve:
                    zoom 0.5
                    xalign 0.5 yalign 0.5
                call changeDominance(1, "none") from _call_changeDominance_25
                with vpunch
                "Tsunade lost her balance and fell on to your bed. A silent, sharp exhale left her parted lips as she tried to keep her composure."
                show tsunade ending choice with dissolve:
                    zoom 0.8
                    xalign 0.0 yalign 0.9
                "Her hand reached for her skirt as soon as she realized that her bottom was now almost fully exposed to you."
                show tsunade ending choice1 with dissolve:
                    zoom 0.9
                    xalign 1.0 yalign 0.2
                ts"Hey! You little shit, watch your mouth!"
                ts"And... keep it quiet! There are people outs-"
                menu:
                    "[bo_name] interrupted her before she could finish her little protest..."
                    "{color=[hatredcolor]}Finish what you started, bitch{/color}":
                        $ tsunaderough = True
                        show tsunade angry1_2 with vpunch:
                            zoom 0.8 xalign 0.3 yalign 0.2
                        ts"H-hey!"
                        "You grabbed her arm and forcibly placed it back where it belonged, your rough movements exposing one of her breasts."
                        show tsunade angry1_1 with vpunch:
                            zoom 0.6 xalign 0.5
                        bo"Finish me off, bitch."
                        show tsunade angry1_1 with vpunch:
                            zoom 0.7 xalign 0.5
                        ts"Y-you will not talk to me like that!"
                        menu:
                            ts"Y-you will not talk to me like that!"
                            "{color=[hatredcolor]}Shut the fuck up already{/color}":
                                call changeHatred(1, "none") from _call_changeHatred_39
                                bo"Shut the fuck up and keep stroking, you nympho whore!" with vpunch
                                show tsunade angry1_1 with dissolve:
                                    zoom 0.85 xalign 0.1 yalign 0.2
                                ts"..."
                            "{color=[dominancecolor]}I know what you are...{/color}":
                                bo"Don't put on a righteous act now... You are the one who started this!"
                                call changeDominance(1, "none") from _call_changeDominance_26
                                bo"You are enjoying this aren't you?"
                                show tsunade angry1_1 with dissolve:
                                    zoom 0.85 xalign 0.5 yalign 0.1
                                ts"Absolutely not! I... I am doing what I have to!"
                        $ renpy.sound.play("/audio/soun_fx/handjob2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                        "Tsunade was irritated, but she didn't stop... In fact, she kept biting her lower lip throughout the entire ordeal..."
                        show tsunade with dissolve:
                            zoom 0.75
                            xalign 0.5
                            yalign 0.6
                        "Coincidentally, her pussy juices started overflowing and dripping down her thighs..."
                        show tsunade with dissolve:
                            zoom 0.5
                        bo"Now, stay right there and take..."
                        bo"my..." with flash
                        bo"load!" with flash
                        label tsunadecum:
                            menu :
                                "...!"
                                "Plaster her face" if tsunaderough == True:
                                    show tsunade with dissolve:
                                        zoom 1.1 xalign 0.99 yalign 0.1
                                    $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                    show tsunade f1 with flash:
                                        zoom 1.15 xalign 0.99 yalign 0.1
                                    bo"A-ah!" with vpunch
                                    
                                    $ renpy.sound.play("/audio/soun_fx/cum2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                    show tsunade f2 with flash:
                                        zoom 1.25 xalign 0.99 yalign 0.1
                                    bo"There's m-more coming!" with flash
                                    ts"Not on my f-face! You asshol-"
                                    $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                    show tsunade f3 with flash:
                                        zoom 0.9
                                    call decreaselust pass (200) from _call_decreaselust_31
                                    $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                    bo"*Panting*"
                                    menu tsunadefinalmenu:
                                        bo"*Panting*"
                                        "Apologize":
                                            bo"I am sorry, lady Tsunade. It all just happened so quick... I had no time to think."
                                            show tsunade angry1c with dissolve:
                                                zoom 0.7 xalign 0.7 yalign 0.0
                                            bo"I feel... better now. "
                                            call changeHatred(-1, "none") from _call_changeHatred_40
                                            show tsunade angry1c with dissolve:
                                                zoom 0.85 xalign 0.8 yalign 0.2
                                            ts"*Sigh...*"
                                            scene black with dissolve
                                            ts"It's alright. Just... warn me, next time."
                                            jump tsunadeending
                                        "{color=[dominancecolor]}Own it{/color}":
                                            call changeDominance(1,"none") from _call_changeDominance_27
                                            bo"Don't act like you didn't enjoy it yourself. I took notice of how wet you got down there..."
                                            show tsunade angry2c with dissolve:
                                                zoom 1.0 xalign 0.7 yalign 0.0
                                            ts"That doesn't mean you can use me as you like you idiot!"
                                            show tsunade angry1c with dissolve:
                                                zoom 1.0 xalign 0.7 yalign 0.0
                                            ts"*Sigh...*"
                                            
                                            ts"Just... warn me, next time."
                                            scene black with dissolve
                                            jump tsunadeending
                                        
                                    

                                "Plaster her tits" if tsunaderough == True:
                                    show tsunade cumtits1 with dissolve and flash:
                                        zoom 1.2 xalign 0.9 yalign 0.4
                                    # play sound("/audio/soun_fx/male_grunt2.opus")
                                    bo"*Moans"
                                    ts"Eck.."
                                    show tsunade cumtits2 with dissolve and flash:
                                        zoom 1.15
                                    bo"Ugh!~Aaah!"
                                    ts"My lord..."
                                    ts"So much of it pent up..."
                                    ts"Are yo-"
                                    "Before she could finish her sentence, you blow one last load, covering her tits with your cum..."
                                    show tsunade cumtits3 with dissolve and flash:
                                        zoom 1.10 xalign 0.99
                                    # play sound("/audio/soun_fx/male_grunt.opus")
                                    bo"*Grunts" 
                                    #todo fix cg cum only face
                                    show tsunade cumtits3 with dissolve:
                                        zoom 0.55 xalign 0.5 yalign 0.5
                                    call decreaselust pass (200) from _call_decreaselust_32
                                    ts"S-so much of it..."
                                    bo"*Panting"
                                    jump tsunadefinalmenu

                                "Cover her legs" if tsunaderough == False:
                                    $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                    show tsunade cumlegs1only with dissolve and flash:
                                        zoom 0.8 xalign 0.3 yalign 0.8
                                    # play sound("/audio/soun_fx/male_grunt2.opus")
                                    bo"*Moans"
                                    ts"Eck.."
                                    $ renpy.sound.play("/audio/soun_fx/cum2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                    show tsunade cumlegs2only with dissolve and flash
                                    bo"Ugh!~Aaah!"
                                    ts"My lord..."
                                    # play sound("/audio/soun_fx/male_grunt.opus")
                                    bo"*Grunts" with flash
                                    ts"So much of it pent up..."
                                    ts"Are yo-"
                                    "Before she could finish her sentence, you blow one last enormous load..."
                                    $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                    show tsunade cumlegs3only with dissolve and flash
                                    "Emptying your balls on her legs..."
                                    ts"Oh... my... lord..."
                                    ts"This is just... unnatural!"
                                    ts"Have you been pent up your entire life?"
                                    $ renpy.sound.play("/audio/soun_fx/cum4.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                    show tsunade cumlegs4only with dissolve and flash:
                                        zoom 0.55 xalign 0.5 yalign 0.5
                                    "Tsunade was covered in your cum which was still dripping from your cock down to Tsunade's skirt..."
                                    call decreaselust pass (200) from _call_decreaselust_33
                                    $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                    bo"*Panting"
                                    menu:
                                        bo"*Panting"
                                        "Apologize":
                                            bo"I am sorry, lady Tsunade. It all just happened so quick... I had no time to think,"
                                            show tsunade cumlegs4only with dissolve:
                                                zoom 0.7 xalign 0.7 yalign 0.0
                                            bo"I feel... better now. "
                                            call changeHatred(-1, "none") from _call_changeHatred_41
                                            show tsunade angry1_2 with dissolve:
                                                zoom 1.0 xalign 1.0 yalign 0.0
                                            ts"*Sigh...*"
                                            scene black with dissolve
                                            bo"I a-apologize..."
                                            ts"It's... alright. Just warn me, next time."
                                            jump tsunadeending
                                        "{color=[dominancecolor]}Own it{/color}":
                                            call changeDominance(1,"none") from _call_changeDominance_28
                                            bo"Don't act like you didn't enjoy it yourself. I took notice of how wet you got down there..."
                                            show tsunade cumlegs4only with dissolve:
                                                zoom 1.0 xalign 0.7 yalign 0.0
                                            ts"That doesn't mean you can use me as you like you idiot!"
                                            show tsunade cumlegs4only with dissolve:
                                                zoom 1.0 xalign 0.7 yalign 0.0
                                            ts"*Sigh...*"
                                            show tsunade cumlegs4only with dissolve:
                                                zoom 1.1 xalign 1.0 yalign 0.0
                                            ts"Just... warn me next time."
                                            scene black with dissolve
                                            jump tsunadeending
                                
                                "Cover her face" if tsunaderough == False:
                                    bo"Stroke me h-harder! Tsunade!!"
                                   
                                    $ renpy.sound.play("/audio/soun_fx/cum5.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                    show tsunade cumface1 with dissolve and flash:
                                        zoom 1.2 xalign 0.9 yalign 0.1
                                    bo"Hnnnnngh!!"
                                    ts"Keep it quiet you doofus! Your [hin_rel] is outs-"
                                    $ renpy.sound.play("/audio/soun_fx/cum6.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                    show tsunade cumface2 with dissolve and flash:
                                        zoom 1.4 xalign 0.8 yalign 0.1
                                    "Before she could finish her sentence, you blow one last load, covering her face with your cum..."
                                    show tsunade cumface2 with dissolve:
                                        zoom 0.55 xalign 0.5 yalign 0.5
                                    call decreaselust pass (200) from _call_decreaselust_34
                                    bo"*Panting"
                                    ts"Did you have to aim for my face you little devil?"
                                    jump tsunadefinalmenu
                            
                    "Explode all over her":
                        label tsunadeexplode:
                        #cum covereed cg
                        bo"I can't hold it anymore!" with flash
                        bo"L-lady Tsunade ~ T-take it!" with flash
                        show tsunade ending choice with dissolve:
                            zoom 0.8 xalign 0.9
                        ts"Y-you...!"
                        menu:
                            ts"Hold on a sec-"
                            "Cover her tits":
                                $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                                play sound("/audio/soun_fx/male_grunt2.opus")
                                show tsunade cumtits1 with dissolve and flash:
                                    zoom 1.2 xalign 0.9 yalign 0.4

                                bo"*Moans"
                                ts"Eck.."
                                $ renpy.sound.play("/audio/soun_fx/cum2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                show tsunade cumtits2 with dissolve and flash:
                                    zoom 1.15
                                bo"Ugh!~Aaah!"
                                ts"My lord..."
                                $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                show tsunade cumtits3 with dissolve and flash:
                                    zoom 1.10 xalign 0.99
                                bo"*Grunts"
                                ts"So much of it pent up..."
                                ts"Are yo-"
                                "Before she could finish her sentence, you grabbed her hand and..."
                                show tsunade angry1 with dissolve and flash:
                                    zoom 1.2 xalign 0.01 yalign 0.1
                                bo"Come on... k-keep stroking me!"
                                show tsunade angry1 with flash:
                                    zoom 0.55 xalign 0.5 yalign 0.5
                                call decreaselust pass (25) from _call_decreaselust_35
                                bo"I am not done yet!"
                                ts"Th...T-theres m-more!?"
                                menu:
                                    ts"Th...T-theres m-more!?"
                                    "Cover her face":
                                        bo"Stroke me h-harder! Tsunade!!"
                                   
                                        $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                        
                                        show tsunade cumface1 with dissolve and flash:
                                            zoom 1.2 xalign 0.9 yalign 0.1
                                        play sound("/audio/soun_fx/male_grunt2.opus")
                                        bo"Hnnnnngh!!"
                                        ts"Keep it quiet you doofus! Your [hin_rel] is outs-"
                                        $ renpy.sound.play("/audio/soun_fx/cum5.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                        $ renpy.sound.play("/audio/soun_fx/femalegrunt1.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                                        show tsunade cumface2 with dissolve and flash:
                                            zoom 1.4 xalign 0.8 yalign 0.1
                                        "You shot a second load directly on her face, completely covering it with your cum..."
                                        call decreaselust pass (25) from _call_decreaselust_36
                                        bo"*Moans"
                                        "You let out a few loud uncontrollable moans..."
                                        scene black with dissolve
                                        "To an unsuspecting someone, it would sound more like painful grunts."
                                        show bg clinic with dissolve
                                        show hina pthinking2 with dissolve
                                        hint"Was that...!"
                                        show hina pthinking with dissolve
                                        hint"It's [bo_name]'s voice! is he in pain!?"
                                        show hina surprised at center with dissolve:
                                            zoom 0.7
                                        hin"Lady Tsunade! Can I come in yet? Is [bo_name] okay!?"
                                        scene black with dissolve
                                        show tsunade angry2c with dissolve:
                                            zoom 0.85 xalign 0.9 yalign 0.2
                                        bo"[hin_rel]!?"
                                        show tsunade angry2c with dissolve:
                                            zoom 0.95 xalign 0.9 yalign 0.2
                                        ts"{size=*0.8}You idiot! Keep it quiet!{/size}"
                                        show tsunade cumface2 with dissolve:
                                            zoom 0.6 xalign 0.5 yalign 0.5
                                        ts"A few more minutes [hin_name]!"
                                        ts"I am just injecting [bo_name] with some medic-"
                                        menu:
                                            ts"I am just injecting [bo_name] with some medic-"
                                            "Plaster her!":
                                                $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                                show tsunade cumlegs1 with dissolve and flash:
                                                    zoom 0.9  yalign 0.7 xalign 0.0
                                                "You keep cumming over and over, this time covering her thighs..."
                                                bo"*Grunts"
                                                call changeDominance(1, "none") from _call_changeDominance_29
                                                show tsunade angry1c with dissolve:
                                                    zoom 0.97 xalign 0.9 yalign 0.2
                                                ts"With s-some medicine..."
                                                ts"[bo_name] is anesthesized, y-you don't have to worry, [hin_name]."
                                                show tsunade angry2c with dissolve:
                                                    zoom 0.99 xalign 0.9 yalign 0.2
                                                ts"{size=*0.8}You idiot! What the fuck is wrong with your cock!{/size}"
                                                hin"Oh..."
                                                call changeObedience("Hinata", 1, "none") from _call_changeObedience_48
                                                hin"O-okay..."
                                                show tsunade angry2c with dissolve:
                                                    zoom 1.01 xalign 0.9 yalign 0.2
                                                ts"{size=*0.8}Control your hose for a freaking second!{/size}"
                                                $ renpy.sound.play("/audio/soun_fx/cum6.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                                show tsunade cumlegs2 with dissolve and flash:
                                                    zoom 0.9  yalign 0.7 xalign 0.0
                                                play sound("/audio/soun_fx/male_grunt2.opus")
                                                bo"Aaaa-ah!!~Hngg!"
                                                hint"..."
                                                ts"{size=*0.8}Oh... my... lord!{/size}"
                                                $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                                                show tsunade cumlegs3 with dissolve and flash:
                                                    xalign 0.5
                                                ts"{size=*0.8}Does it ever end!?{/size}"
                                                "From top to bottom, Tsunade was absolutely drenched in your cum. You have not let a spot unmarked."
                                                window hide
                                                
                                                show tsunade cumlegs3 with dissolve and flash:
                                                    zoom 0.7
                                                call decreaselust pass (50) from _call_decreaselust_37
                                                pause 2
                                                window show
                                                show tsunade cumlegs3 with dissolve:
                                                    zoom 0.5 xalign 0.5
                                                $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                                                bo"*Panting*"
                                                ts"Such... potency."
                                                bo"Medicine... eh? You sure took some of mine as well!"
                                                show tsunade cumlegs3 with dissolve:
                                                    zoom 0.9 xalign 0.8 yalign 0.0
                                                ts"You little devil!"
                                                scene black with dissolve
                                                ts"At least... warn me next time."
                                                jump tsunadeending

                                            
                        
                        

                    "{color=[dominancecolor]}Don't be shy, Tsunade{/color}":
                        $ tsunaderough = False
                        show tsunade angry1_1 with dissolve:
                            zoom 1 xalign 0.0 yalign 0.38
                        show tsunade:
                            easein 3 xalign 0.5 yalign 0.2
                        call changeDominance(1, "none") from _call_changeDominance_30
                        "You grabbed her hand and placed it back on your cock..."
                        bo"Come on, don't be shy now. You are the one who started this..."
                        show tsunade angry1_1 with dissolve:
                            zoom 0.5 xalign 0.5 yalign 0.5
                        
                        ts"You sly little devil... I never knew you had it in you."
                        "Tsunade willingly grabbed your shaft, and started quickly stroking, knowing you were close to climaxing."
                        bo"I- I am close..."
                        bo"Don't stop... T-tsunade!"
                        "Tsunade was not opposed to your ideas. She induldged your advances..."
                        show tsunade with dissolve:
                            zoom 0.75
                            xalign 0.5
                            yalign 0.6
                        "In fact, she might have enjoyed it, as evident by her pussy juices overflowing down her thighs"
                        show tsunade with dissolve:
                            zoom 0.5
                        bo"Now, stay right there and take..."
                        bo"my..." with flash
                        bo"load!" with flash
                        jump tsunadecum
        label tsunadeending:
            $ renpy.end_replay()
            jump borutoturnstonormal
        label tsunadeending2:
            $ renpy.end_replay()
            show bg infirmary room with dissolve
            show tsunade leaning angry with dissolve:
                        zoom 0.8
                        xalign 0.5 yalign 0.5
            ts"Hey! Snap out of it!" with vpunch
            show tsunade leaning with fade
            ts"Your [hin_rel_mother] is waiting outside..."
            ts"I will explain the situation to both of you once we clean ourselves up."
            hide tsunade with dissolve
            bot"Ah, right."
            bot"My memory is... cloudy."
            show ino sitting with flash
            hide ino with dissolve
            bot"But I do remember, Ino."
            bot"I tried to..."
            show ino sitting 3 with flash
            hide ino with dissolve
            bot"I was in pain. but... what I did was..."
            menu:
                "What I did..."
                "{color=[hatredcolor]}Was satisfying{/color}":
                    bot"It had to be done... My entire being was calling for it. I even enjoyed the feeling."
                    bot"But now thinking about it, it was so wrong."
                    bot"So... why?"
                    bot"Why did I enjoy it."
                    call changeHatred(1, "none") from _call_changeHatred_42
                    bot"Is that who I am?"
                "Was evil":
                    bot"What I did was unforgivable..."
                    call changeHatred(-1, "none") from _call_changeHatred_43
                    bot"I will have to apologize to Ino later, but she would probably kill me if she ever saw me again."
                    bot"What even compelled me to do that to her..."
                    bot"Is that who I am?"
            bot"*Sigh...*"
            show tsunade leaning with dissolve:
                zoom 1.5 yalign 0.90
            ts"Hey!! Stop dozing off." with vpunch
            call increaselust pass (5) from _call_increaselust_42
            menu :
                "..."
                "Let intrusive thoughts take control":
                    bot"Those milkers of hers, I swear to god one day..."
                    bot"I will have my dick buried so deep between them, even Columbus will have trouble finding it."
                    show tsunade leaning angry with dissolve:
                        zoom 0.8
                        xalign 0.5 yalign 0.5
                    bo"Will you stop showing off your mammaries? I know I just came on you, but I am not sure I can resist much longer..."
                    ts"Don't get any ideas [bo_name]. What happened earlier was an one time thing... For medical purposes."
                    bot"Heh! She says that but she did slip up 'next time', earlier..."
                    bot"I would have never guessed Lady Tsunade is such a... deviant!"
                    bot"I imagine this won't be the last time we see each other..."
                "Be respectful":
                    bo"Uuuhh..."
                    show tsunade leaning angry with dissolve:
                        zoom 0.8
                        xalign 0.5 yalign 0.5
                    ts"And stop staring at my breasts. What happened earlier was an one time thing... for medical purposes."
                    bo"Sure..."
                    bot"She says that but she did slip up 'next time', earlier..."
                    bot"If I play my cards right I could have another chance with her in the future."
            show blackscreen with dissolve
            show tsunade leaning 
            "..."
            hide blackscreen with dissolve
            ts"I am calling your [hin_rel] in now..."
            show tsunade leaning angry with dissolve
            ts"Needless to say, she doesn't have to know about the treatment I administered to you..."
            ts"Do you understand?"
            bo"What's with the angry face... I am pretty sure we both enjoyed that! I wouldn't rat you out..."
            show tsunade at smallshake
            ts"...*Scoffs*"
            scene black with dissolve
            "Tsunade, after cleaning up the mess, calls in [hin_name] to brief both her, and you..."
            show bg clinic with dissolve
            show hina pthinking with dissolve
            hint"Why is this taking so long..."
            ts"[hin_name], we are ready now... You should come in."
            show hina pthinking2 with dissolve
            hint"Oh!"
            hide hina with dissolve
            hin"Ah, yes. Right away!"
            scene black with dissolve
            show bg infirmary room with dissolve
            show hina surprised at left with dissolve:
                zoom 0.70
            hin"[bo_name]! You are awake! Are you feeling well?"
            show boruto worried at right with dissolve
            bo"[hin_rel]..."
            show hina thinking with dissolve
            hin"Are you okay!? ...Feeling any pain? Do you... remember what happened?"
            show boruto normal with dissolve
            bo"I am okay, [hin_rel]. You can relax..."
            bot"I remember some details... but considering what I did to Ino, it's probably not a good idea to let [hin_rel] know..."
            menu:
                bo"[hin_rel], I..."
                "Lie":
                    $ lie_about_ino = True
                    show boruto suspicious with dissolve
                    bo"Not quite, [hin_rel]. All I remember was coming back from the grocery store to pick up the things you wanted me to..."
                    bo"Then I saw Ino, your friend. But after that..."
                    show boruto worried with dissolve
                    bo"It's all a blur."
                    show hina thinking at left with dissolve:
                        zoom 0.70
                    hint"Is he being truthful?"
                    hide hina thinking with dissolve
                    show hina concerned at left with dissolve:
                        zoom 0.70
                    hin"I see, we should hear what lady Tsunade has to say first then..."
                    hin"We will discuss what happened with Ino when we are alone..."
                    show boruto surprised2
                    bot"Is she on to me!?"
                    show boruto normal with dissolve
                "Be honest":
                    $ lie_about_ino = False
                    show boruto sad with dissolve
                    bo"I..."
                    bo"It's all a bit blurry, but I remember walking back from the grocery store to pick up the things you wanted me to..."
                    bo"But when I saw Ino, next to our house..."
                    menu:
                        bot"Shall I just blame it on my... condition?"
                        "Be brutally honest":
                            show boruto worried2 with dissolve
                            bo"It was as if something took hold of my senses. I wasn't myself. I was in pain, looking for some sort of release and I... snapped."
                            bo"I did something unforgivable to her."
                            show hina assertive with dissolve
                            show boruto surprised2
                            hin"Unforgivable is right! We will hear what lady Tsunade has to say first, but nothing will excuse what you did to Ino."
                            hin"You will apologize to her as soon as the situation clears up."
                            hin"Do you understand?"
                            show boruto sad2 with dissolve
                            bo"I do... I will, [hin_rel]."
                        "Blame your 'condition'":
                            show boruto suspicious with dissolve
                            bo"I felt like I wasn't myself. I was in pain, looking for some sort of release and I... snapped."
                            show boruto pain with dissolve
                            bo"[hin_rel], I swear. I wasn't in control of my actions. It's just..."
                            bo"The way I felt, I was in pa.."
                            show boruto surprised3 
                            show hina assertive
                            call changeRespect("Hinata", -1) from _call_changeRespect_77
                            hin"Enough!" with vpunch
                            show boruto sad2 with dissolve
                            hin"[bo_name], there is nothing you can say that makes what you did excusable!"
                            hin"We will hear what lady Tsunade has to say first, but as soon as the situation clears up, you will apologize to Ino."
                            hin"Do you understand?"
                            show boruto sad with dissolve
                            bo"I... I do, [hin_rel]"
                        
            
            scene tsunade thinking with dissolve
            ts"*Sigh...*"
            show tsunade intro2 with dissolve:
                zoom 1.05
            ts"Listen up you two."
            ts"Most of what happened can be explained with what I am about to tell you..."
            ts"[hin_name], remember when I said this might be connected to your husband's curse?"
            ts"I am afraid I have all but confirmed my hypothesis..."
            show halfblack with dissolve
            show hina surprised at left with dissolve:
                zoom 0.70

            hin"*Gasps"
            hin"No! Not that..."
            hide hina with dissolve
            show boruto worried at right with dissolve
            bot"My [na_rel]'s curse? I have heard stories..."
            bot"Stories that would make anyone tremble in fear..."
            show boruto worried2 with dissolve
            bot"Will I be like he was then?"
            hide boruto with dissolve
            hide halfblack with dissolve
            ts"Not something you wanted to hear, I know..."
            ts"Although there are some... good news to [bo_name]'s case"
            ts"Would you rather I lead with the good, or bad news first."
            show halfblack with dissolve 
            show boruto worried at right with vpunch
            show hina concerned at left with vpunch:
                zoom 0.70
            hin"Good news."
            bo"Bad news."
            show hina assertive with dissolve
            hin"[bo_name], let me do the talking, okay?"
            show boruto surprised2 with dissolve
            menu:
                bot"But it's my condition..."
                "Be assertive":
                    show boruto pissy with dissolve
                    bo"But [hin_rel], it's my problem!"
                    show boruto pissy:
                        linear 0.5 xpos 0.55
                    bo"I need to know what am I in for."
                    scene black with dissolve
                    show grab hand
                    "You moved to her side, and assertively grabbed her hand, as if to say this was your decision to make."
                    scene tsunade thinking with dissolve
                    show boruto angry at right:
                        xpos 0.55
                    show hina concerned at left:
                        zoom 0.70
                    show hina at smallshake
                    hin"Okay, okay! Have it your way then..."
                    call changeDominance() from _call_changeDominance_31
                    show boruto angry at right with dissolve
                    hint"What has gotten into him..."
                    hint"He is not one to be stubborn about menial things"
                    show boruto normal with dissolve
                    bo"Let us hear the whole of it then, Lady Tsunade."
                    hin"..."
                    hide halfblack with dissolve
                    ts"Alright then, brace yourselves."
                    hide boruto with dissolve
                    hide hina with dissolve
                    jump badnews

                "Let her have her way":
                    show boruto surprised
                    bo"I..."
                    show boruto sad with dissolve
                    bo"Fine, have it your way."
                    call changeRespect("Hinata",1, "none") from _call_changeRespect_78
                    show hina concerned with dissolve
                    hin"Then let us hear the good news first, Lady Tsunade..."
                    hide boruto with dissolve
                    hide hina with dissolve
                    ts"You see..."
                    ts"Since there is no beast sealed inside of him, I don't suspect transfiguration as a potential side effect."
                    ts"There also seems to be no reason to worry when it comes to the violent, or even murderous nature of the curse, such as was the case with his [na_rel]."                   
                    ts"Whatever changes shall occur, should primarily be constrained to either the psychological or emotional sphere of [bo_name]."
                    ts"That being said..."
                    jump badnews
                    
            label badnews:
                scene tsunade thinking with dissolve
                ts"It is my undestanding that you, [bo_name], have partially inherited the Jinchūriki's curse from your [na_rel]"
                ts"It might have took a while to manifest in you, but manifest it did, as we are all aware now."
                ts"Your condition is medically known as Persistent Genital Arousal Disorder or PGAD for short."
                ts"PGAD by itself would be controllable, but combined with your curse... Until we find a way to either expel, or at worst contain it, you will be troubled with the effect it has on you."
                ts"From what I have observed, you can expect; heightened emotional sensitivity, abnormal irritability and certain... physiological irregularities."
                ts"Namely, you might notice an effect on your strength, as your muscle fibers seem to have rapidly multiplied, which would explain some of the pain you were feeling."
                ts"As for the pain near your penile area, it also appears to be a by-product of the multiplication of somatic cells around your genital area."
                ts"This could explain the abnormal size your penis can take when you are feeling..."
                ts"Aroused..."
                ts"A state which will be all too common for you from now on..."
                ts"While your cognition does not seem to be affected, there is an apparent shift in your sexual psyche."
                ts"Excessive lust, constant arousal and the need to reach climax, are only some of the effects you can expect in that regard."
                show tsunade with dissolve:
                    zoom 1.1 yalign 0.0
                ts"Pay attention now, as this is the most important part."
                hin"..."
                bo"..."
                ts"The curse is unfortunately, metastatic."
                ts"Meaning that the longer it is left to fester, the more it spreads within you... eventually consuming your entire self."
                ts"Allowing it to so, would mean putting yourself and those around you in grave danger as your emotions, your actions, your body and your thinking all run rampant."
                show halfblack with dissolve
                show hina concerned at left with dissolve:
                    zoom 0.70
                $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                hin"*Gasps*"
                hin"No..."
                show boruto surprised at right with dissolve
                bot"..."
                hide hina with dissolve
                hide boruto with dissolve
                hide halfblack with dissolve
                ts"The silver lining here is that the metastasis can be contained..."
                hin"Praise be!"
                ts"All you have to do is..."
                scene tsunade intro2 with dissolve
                ts"Avoid staying in a state of 'arousal' for extended periods of time..."
                ts"That is to say, you are going to have to find ways to climax. Regularly."
                scene tsunade intro2 with dissolve:
                    zoom 1.2 xalign 1.0 yalign 0.0
                ts"And just so we are perfectly clear, I am referring to sexual climax..."
                scene tsunade thinking with dissolve
                ts"[hin_name], [bo_name] is still young, inexperienced... The easiest way for him to deal with this would be self-masturbation."
                ts"Although please understand that if he runs into... difficulties. The burden of education falls on you."
                show hina surprised at left:
                    zoom 0.70
                hin"W-What!? Lady Tsunade, what are you insinuating?" with vpunch
                hide hina with dissolve
                ts"Relax [hin_name]. I am of course NOT suggesting that you be the one to take care of his... needs."
                ts"That would be despicable."
                ts"I am only suggesting that you don't shy away from at least, verbally educating him."
                ts"[bo_name]'s father being away, and his tendency to isolate himself, are not factors that contribute to a promising start to [bo_name]'s treatment."
                ts"An ideal scenario would be for [bo_name] to find an outside partner to help with his... needs."
                scene tsunade intro2 with dissolve:
                    zoom 1.2 xalign 1.0 yalign 0.0
                ts"You hear that, [bo_name]?"
                show halfblack with dissolve
                default clinichug = False
                show boruto sad at right with dissolve
                menu:
                    bo"Sounds... manageable"
                    "Be 'humorous'":
                        $ clinichug = False
                        $ boruto_clinic_gropemom = False
                        show boruto smirk with dissolve
                        bo"I basically have terminal sex cancer and the only way to prevent its spread is to literally, 'fuck around'"
                        show boruto laughing2 with dissolve
                        bo"Simple enough. I don't think there is a way I can possible 'fuck it up'!"
                        bo"Heh, get it?"
                        show hina assertive at left with dissolve:
                            zoom 0.70
                        hin"[bo_name_stutter]!" with vpunch
                        show boruto surprised2 with dissolve
                        call changeRespect("Hinata",-1, "none") from _call_changeRespect_79
                        hin"Take this seriously! And watch your language."
                        hide boruto with dissolve
                        hide hina with dissolve
                        scene tsunade thinking with dissolve
                        ts"Your [hin_rel_mother] is right, [bo_name]..."
                        ts"You might not remember what happened before you got here, But [hin_name] does, and from what she described to me, it was horrific."
                        
                    "Be reasonable":
                        $ clinichug = True
                        show boruto sad with dissolve
                        bo"I... see."
                        bo"So long as I put effort into controlling my condition, I should be able to keep those around me safe."
                        show boruto worried2 with dissolve
                        bo"[hin_rel]... I don't want you to be worried about me."
                        bo"I will do everything I can to deal with my problem, so you and [him_name] don't have to be scared."
                        call hughinata from _call_hughinata #hug hinata scene
                        jump clinicfinal
                
                label clinicfinal:            
                    hide halfblack2 with dissolve
                    hide halfblack with dissolve
                    ts"Listen, you two..."
                    ts"I know that you need to have a serious discussion about what happened with Ino, as well as how you will proceed now that we have an understanding of [bo_name]'s state."
                    ts"But before that, let me pass on to you the... lesser bad side of your condition."
                    ts"While [bo_name] did inherit [na_name]'s curse, it appears to be only residually."
                    ts"From what I gathered the curse is heavily fragmented..."
                    ts"Meaning, there is no tailed beast residing within you. Nor will we have to worry about excessive violence, or murderous intent, as was the case with your [na_rel]."
                    ts"But be warned... We have no way of knowing what the future could look like if the curse is left to fester freely."
                    ts"Be vigilant with the preventative measures I administered and if all goes as planned, you should be able to lead a normal life."
                    show tsunade intro2 with dissolve:
                        zoom 1.5
                        xalign 0.5 yalign 0.1
                    ts"And [bo_name]..."
                    ts"If complications arise, don't hesitate to visit me again."
                    show tsunade thinking with dissolve:
                        zoom 1
                    ts"Now give us a few minutes alone with your [hin_rel], would you?"
                    bo"Of course..."
                    scene black with dissolve
                    show bg clinic with dissolve
                    show boruto worried with dissolve
                    bot"That explains a lot..."
                    bot"Now that I am aware of my condition, I should be more thoughtful of how I proceed."
                    bot"Despite what I told [hin_rel] and lady Tsunade, The truth is that I do remember what I did to Ino..."
                    show boruto surprised2 with dissolve
                    bot"Could my [hin_rel] and [him_rel] be potential triggers too?"
                    bot"Do I really see them like that?"
                    if boruto_clinic_gropemom == True:
                        bot"Even back in there, I willingy reached for [hin_rel]'s ass."
                    else:
                        bot"Come to think about it, sometimes I do catch myself perving on them."
                    show boruto sad with dissolve
                    bo"*Sigh...*"
                    menu:
                        bot"Thinking about it, I probably want to..."
                        "Harness it":
                            show boruto suspicious with dissolve
                            bot"Harness it."
                            bot"Lady Tsunade did mention something about increased strength and whatnot. Not sure about the sexual psyche stuff, but..."
                            bot"If I play my cards right, perhaps I could put some of its side-effects to good use..."
                        "Resist it":
                            show boruto worried2 with dissolve
                            bot"Resist it as much as I can." 
                            bot"If I leave it to freely fester..."
                            bot"It will likely negatively affect my relationship with both my [hin_rel] and [him_rel]"
                            call changeHatred(-1, "none") from _call_changeHatred_44
                            bot"And those are bad enough as they are."
                            show boruto worried with dissolve
                            bot"I should be careful with how I proceed."
                        "{color=[hatredcolor]}Abuse it{/color}":
                            show boruto sceeming  with dissolve
                            bot"Abuse it."
                            bot"I can think of so many ways to use its effects to my benefit."
                            show boruto sceeming2 with dissolve
                            bot"I will need to be careful, but if I tread methodically, I am certain I can get both my [hin_rel] and [him_rel] 'closer' to me."
                            call changeHatred(1, "none") from _call_changeHatred_45
                            bot"One way or another."
                
                show boruto normal with dissolve
                bot"I should wait for [hin_rel]..."
                if lie_about_ino == True:
                    bot"Hopefully she bought my lie about what happened with Ino, otherwise I am in for a big scolding."
                else:
                    bot"She is probably going to scold me for what I did to Ino..."
                scene black with dissolve
                "Inside Tsunade's office..."
                show tsunade intro2 with dissolve
                ts"[hin_name], I don't want to sugarcoat things for you."
                ts"Your lives are about to take a sudden turn. Living under the same roof with [bo_name]'s condition, It will not be easy to navigate..."
                ts"But if you care for each other, I am certain you will find ways to work through it."
                ts"if there is anything you would like to discuss, now would be the time."
                if boruto_clinic_gropemom == True:
                    show hina concerned at left with dissolve:
                        zoom 0.7
                    hin"Lady Tsunade, This is embarrassing but..."
                    hin"While I was hugging [bo_name] just a little while ago, I think he intentionally touched my..."
                    hin"*Sigh...*"
                    show hina surprised with dissolve
                    hin"Will I have to worry about that? Does my own [hin_rel_to_bo] really see me like... that?"
                    hide hina with dissolve
                    ts"I can't know that for certain, [hin_name]."
                    ts"What I do know is that if for some weird reason, your [hin_rel_to_bo] was attracted to you before..."
                    ts"His condition would surely amplify his... attraction."
                    ts"Nevertheless, so long as you are stern and set proper boundaries, I see no reason to be concerned."
                else:
                    show hina concerned at left with dissolve:
                        zoom 0.7
                    hin"Lady Tsunade... This is all a bit too much. How do we even proceed?"
                    hide hina with dissolve
                ts"It all boils down to what I mentioned before, [hin_name]."
                ts"As long as you are there for each other and [bo_name] stays vigilant with his... treatments, I am certain you can work through this."
                show hina thinking at left with dissolve:
                        zoom 0.7
                hin"I... I see. Thank you, doctor. We appreciate your help."
                hide hina with dissolve
                ts"[hin_name], one last thing..."
                show tsunade thinking with dissolve:
                    zoom 1.1 yalign 0.0
                ts"Things can, and will very likely get complicated, but no matter how difficult it gets..."
                ts"Please..."
                scene tsunade intro2 with dissolve
                ts"Do not cut ties with your [hin_rel_to_bo]. Be his emotional support, be someone he can lean on. He relies a lot on you, especially so through these difficult times."
                ts"I fear of how his curse might develop, if he loses those closest to him."
                show hina assertive at left with dissolve:
                        zoom 0.7
                "[hin_name] seemed slightly bothered by Tsunade's remark"
                hin"I would never abandon him... Tsunade, he is my [hin_rel_to_bo]!"
                show hina at smallshake
                hin"Have a good day!"
                hide hina with dissolve
                $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                show tsunade thinking with dissolve:
                    zoom 1.1 yalign 0.0
                tst"You say that [hin_name], but I wonder..." 
                tst"If my suspicions are correct, this won't be easy on you."
                "[hin_name] visibly agitated, hastily said her goodbyes and left the room..."
                scene black with dissolve
                show hina pthinking2 with dissolve
                hint"Cut ties with my [hin_rel_to_bo]? Why would she even bring that up!"
                hin"Good grief..."
                hide hina with dissolve
                show bg clinic with dissolve
                show boruto worried at right with dissolve
                bo"Everything ok, [hin_rel]?"
                if clinichug == False:
                    show hina concerned at left with dissolve:
                        zoom 0.7
                    hin"[bo_name]..."
                    hint"[bo_name] is good at hiding his true feelings."
                    hint"But this must have hit him hard."
                    hint"When he joked around back in there... I am sure it was a way for him to cope with his diagnosis..."
                    hint"My poor boy..."
                    call hughinata from _call_hughinata_1
                show hina assertive at left with dissolve:
                    zoom 0.7
                show boruto worried2 at right with dissolve
                hin"You are not off the hook yet, [bo_name]. There is so much we need to discuss as soon as we get home."
                hin"It is getting late too, [him_name] must be wondering what is going on."
                hin"We will have an important discussion once we get home, understand?"
                
                bo"I know, [hin_rel]."
                bot"She seems unusually pissy."
                if boruto_clinic_gropemom == True:
                    bot"Is it because she realized I touched her ass? I hope not."
                bot"Maybe she knows I am hiding some of the truth regarding Ino."
                bot"Fuck. I am in deep trouble aren't I."
                
                scene black with dissolve
                play sound("/audio/soun_fx/rain.opus") loop fadein 1.0
                show bg infirmary with dissolve
                menu:
                    "..."
                    "Make your way home":
                        jump afterclinic



                
                    
                
                


                
            
            
                

            
                



                
            

                    
            
        

        

    
            
    