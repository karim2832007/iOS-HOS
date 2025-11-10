



# The script of the game goes in this file.
image introvideo = Movie(channel="movie_dp", play="images/video/rain.webm", stop_music=False, size=(1280,720))

#initiate quest log
default quest = Manager()
default quest_hin = Manager()
default quest_him = Manager()



# The game starts here.

label start:
    python:
        # We are now calling the Python function directly,
        # which is a silent operation that won't confuse the engine.
        reconcile_stats_on_start()
    $ inventory = Inventory()
    $ inventoryShop = Inventory()
    stop music fadeout 2
    scene black with dissolve
    pause 1
    $ v19g_1sttime_r = True #Prevent day reset from occuring for saves created after v19
    $ renpy.sound.play("/audio/soun_fx/bassstart.opus", channel="sfx1", loop=False, relative_volume = 1, fadein = 0.05)
 
    queue sfx1 ("audio/soun_fx/introbass3.opus") volume 0.4 loop
    show disclameimerintro with Fade(0.5,0,3):
        zoom 2.0 xalign 0.6 yalign 0.3
    show disclameimerintro:
        easeout 30 subpixel True zoom 1.0 xalign 0.492 yalign 0.3
    pause 2
    "Thank you for taking the time to try out House of Shinobi! if you enjoy what you see, {a=https://subscribestar.adult/cutepercentage}please consider supporting the creator's efforts.{/a}"
    "If not, I would still appreciate your feedback. Your contribution in either way, will be formative for the future of this game."
    "Sound is an integral part of this experience."
    menu:
        "Would you like to use the recommended sound settings?"
        "Yes":
            $ _preferences.set_volume("music", 1)
            $ _preferences.set_volume("sfx", 1)
        "No":
            pass
    $ renpy.sound.play("/audio/soun_fx/ominous_sound.opus", channel="sfx2", loop=False, relative_volume = 0.6)
    show sound_disclaimer with dissolve:
        zoom 0.5 subpixel True xalign 0.5 yalign 0.5 alpha 0.55
    show sound_disclaimer:
        linear 15 subpixel True zoom 0.9 xalign 0.5 yalign 0.5 alpha 0.0
    "Extra care was put into curating and mixing soundtrack and SFX at appropriate levels and intervals to enhance the game's storytelling."

    "Using headphones is highly suggested for the intended and complete experience!"
    "If you find the need to adjust SFX volume levels, please do so via your system's settings as opposed to in-game settings. That is done to maintain relative volume levels that are dependant on Ren'Py's engine settings."
    hide sound_disclaimer with dissolve
    "Before you proceed, please read the following important disclaimers:"
    show epilepsy with dissolve:
        alpha 0.9 xalign 0.5 ypos -0.49
    show epilepsy with dissolve:
        easeout 10 subpixel True alpha 0.0
    "This game contains flashing lights and rapidly changing images that may trigger seizures in individuals with photosensitive epilepsy. Player discretion is advised."
    "This game contains explicit adult content that is intended for mature audiences only. The material included may be offensive to some viewers."
    "If you are under the legal age or if its otherwise illegal in your corresponding jurisdiction to consume adult content, please exit the game now."
    "Be aware that the game includes depictions of the following elements:"
    "-Sexual content and nudity"
    "-Graphic depictions of violence, including mild gore and blood."
    "-Strong language and profanity"
    "All characters appearing in this game are above the legal age of consent."

    "Please note that for the purposes of story-telling and within the context of artistic expression, this game portrays fictitious dark themes and adult content which should only ever exist, in fiction."
    "The creator condemns any and all acts of non-consensual sexual behavior outside the realm of fiction."
    menu:
        "By continuing, you acknowledge that you are at least 18 years of age and understand the nature of the content you are about to experience."
        "Continue":
            hide epilepsy with dissolve
    
            pass
        "Exit":
            return
    $ renpy.sound.play("/audio/soun_fx/wakeup.opus", channel="sfx3", loop=False, relative_volume = 1.6)
    with Shake((0, 0, 0, 0), 2, dist=40, peak_time=0.9, smoothness=50)
    stop sfx1 fadeout 1.0
    scene black with flash
    play music"/audio/ost/Hurricane Suite Final2.opus" volume 0.9
    #initiate inventory

    






    $ renpy.sound.play("/audio/soun_fx/rain.opus", channel="sfx1", loop=True, relative_volume = 0.6, fadein = 1)
    # play music"/audio/ost/Hyouhaku.opus" volume 0.3
    window hide
    show introvideo with fade
    $ renpy.pause(6.8, hard=True)
    scene black with dissolve
    pause 0.5
    scene bg intro with dissolve
    show boruto worried2 at center with dissolve

    label introwartestt:


    "You" "Heavy rain, darkened clouds... Perhaps a premonition for something ominous?"
    show boruto normal with dissolve
    "You" "Although I am not one to believe in superstitions, today feels... perilously somber."
    show boruto embarassed with dissolve
    "You" "But more likely, just my blind hope for something exciting to break the monotony of my stale life..."
    label introwartest:
    $ initialize_replay_defaults()
    scene black with fade
    show bg ninja war:
        xalign 0.5 yalign 0.5
        zoom 1.1
    with fade
    "A few years have passed since the last Shinobi War ravaged Konoha village."
    show war1 at halfzoom with dissolve
    "A sizeable portion of its population perished, fighting to protect their birthplace, their families and their lives."
    "Endless bloodshed would flow down the streets and into the rivers, as the brave warriors of Konoha fought against imperialistic expansionists."
    show war2 at halfzoom with dissolve
    "It was their valor and courage that kept Konoha's lands intact and its enemies at bay——Lands that were highly coveted by neighboring nations due to their great opulence..."
    show war2 with dissolve:
        subpixel True
        xalign 0.5 yalign 0.0
        easein 10 zoom 0.9 xalign 0.55
    "But much more crucial than that, Konoha possessed another 'commodity' of extreme importance..."
    "A resource with such immense value, that it would almost condemn Konoha to a perpetual state of war with other power-hungry nations."
    show war2 with dissolve:
        zoom 0.5
    "In a world ruled by violence, there was one virtue that would be sought after the most and govern the world with an iron fist..."
    $ renpy.sound.play("/audio/soun_fx/swordsheathe3.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    window hide
    show warhinatafinal at brightrevealzoom:
        zoom 0.5
    with flash
    pause 3
    "That, of strength..."
    show warhinatafinal with dissolve:
        easein 20 zoom 0.6
    "A wicked thought would slowly form and inhibit the minds of many. An idea, that wanted strength to be cultivated in more ways than one..."
    "Konoha's female populace, renowned by many and perceived as the strongest and smartest across the known lands. It was them who became central to this dark ambition..."
    show war3 with dissolve:
        zoom 0.5
    "As many nations would envy and see them not only as objects of desire, but also an invaluable commodity to be enslaved or sold for profit..."
    show war3 with dissolve:
        easein 10 subpixel True zoom 0.95 xalign 0.7 yalign 0.15
    $ renpy.sound.play("/audio/soun_fx/intro/evilmenlaugh.opus", channel="sfx2", loop=False, relative_volume = 0.7)
    "But the fate of strong female shinobi, also referred to as 'Kunoichi', would be much worse than that of mere slavery..."
    "A rotten, cruel practice... employed by ambitious nationalistic overlords, hoping to bolster their armies and strengthen their Nation's gene pools..."
    window hide
    $ renpy.sound.play("/audio/soun_fx/intro/introwoman1.opus", channel="sfx2", loop=False, relative_volume = 1.3)
    show captured1 at atblur with Fade(0.5,0.5,3):
        easein 10 zoom 0.5
    "A sorrowful fate of being held captive and treated as if they were mere livestock, destined to be endlessly bred by entire Nations. From the edge of night... "
    window hide
    show captured1_1 at brightrevealzoom:
        zoom 0.5
    with flash
    pause 0.5
    $ renpy.sound.play("/audio/soun_fx/intro/introwoman2.opus", channel="sfx3", loop=False, relative_volume = 1.1)
    "Until the dawn of tomorrow... A selection of the nation's strongest men would take turns filling their Kunoichi captives' wombs, and not only, with their semen..."
    $ renpy.sound.play("/audio/soun_fx/intro/gruntwoman2.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    show captured2 with vpunch:
        zoom 0.8 xalign 1.0 yalign 0.7
    show captured2:
        easein 5 zoom 0.5 xalign 0.5 yalign 0.5
    pause 1   
    "Some would partake in more than just the process of breeding, as they sadistically derived pleasure from breaking their prisoners' once, indomitable wills..."
    $ renpy.sound.play("/audio/soun_fx/intro/gruntwoman3.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    "In their eyes, those were the same women that threatened their pursuit of power, the same Kunoichi responsible for the deaths of their friends, countrymen and sometimes even their families on the battlefield." with vpunch
    $ renpy.sound.play("/audio/soun_fx/intro/gruntwoman1.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    show captured2 with vpunch:
        zoom 0.8 xalign 1.0 yalign 0.7
    scene black with dissolve

    show captured4 with dissolve:
        zoom 0.5 xalign 0.95 yalign 0.99
    show captured4 with dissolve:
        easein 3 zoom 0.4 xalign 0.5 yalign 0.5
    pause 2
    "Those very women, were now under their feet, to be done with as they pleased..."
    call showscrollingimage from _call_showscrollingimage_304
    show screen genericparallax("captured4")
    $ renpy.sound.play("/audio/soun_fx/intro/introwoman4.opus", channel="sfx3", loop=False, relative_volume = 0.8)
    "Angry Soldier" "Y-you... you killed my son you fucking whore!" with vpunch
    "You can control the scene by hovering your cursor (Or dragging on mobile)"
    "Angry Soldier" "For that, you will pay..."
    hide screen genericparallax
    $ renpy.sound.play("/audio/soun_fx/intro/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    pause 0.2
    $ renpy.sound.play("/audio/soun_fx/intro/spank5.opus", channel="sfx3", loop=False, relative_volume = 0.8)
    show screen genericparallax("captured4_1") with flash
    $ renpy.sound.play("/audio/soun_fx/intro/gruntwoman2.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    $ renpy.sound.play("/audio/soun_fx/intro/introwoman1.opus", channel="sfx3", loop=False, relative_volume = 1.4)
    "Angry Soldier" "And when I am done with your ass, I will fill your womb up to the brim and you will bear me the son you owe me!"
    show screen genericparallax("captured4") with dissolve
    "Imprisoned Kunoichi" "Please... No m-more..."
    default introcounter = 0
    menu intromenu:
        "..."
        "Spank her":
            $ introcounter += 1
            if introcounter == 1:
                $ renpy.sound.play("/audio/soun_fx/intro/spank8.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                
                pause 0.1
                $ renpy.sound.play("/audio/soun_fx/intro/gruntwoman1.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                show screen genericparallax("captured4_1") with vpunch
                "Angry Soldier" "Shut up you filthy whore!"
                show screen genericparallax("captured4") with dissolve
                $ renpy.sound.play("/audio/soun_fx/intro/introwoman1.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                "Imprisoned Kunoichi" "*Sobbing*"
            elif introcounter == 2:
                $ renpy.sound.play("/audio/soun_fx/intro/spank7.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                pause 0.2
                $ renpy.sound.play("/audio/soun_fx/intro/gruntwoman3.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                show screen genericparallax("captured4_1") with vpunch
                $ renpy.sound.play("/audio/soun_fx/intro/introwoman1.opus", channel="sfx3", loop=False, relative_volume = 0.8)
                "Angry Soldier" "After all you've done!? Don't you cry now, bitch!"
                show screen genericparallax("captured4") with dissolve
                "Imprisoned Kunoichi" "P-please... H-have m-mercy..."
                "Imprisoned Kunoichi" "*Sobbing*"
            elif introcounter == 3:

                "Angry Soldier" "Mercy? What mercy did you show to my son you whore!"
                $ renpy.sound.play("/audio/soun_fx/intro/spank5.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                pause 0.1
                show screen genericparallax("captured4_1") with vpunch
                $ renpy.sound.play("/audio/soun_fx/intro/screamwoman.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                "Imprisoned Kunoichi" "*Cries of anguish*"
                "Angry Soldier" "Fuck you and your shithole of a country."
                show screen genericparallax("captured4_2") with dissolve
                "Angry Soldier" "You deserve this and worse!"
                
                "Imprisoned Kunoichi" "..."
                "She passed out..."
                jump afterintromneu
            
            jump intromenu 
        "Continue":
            jump afterintromneu
label afterintromneu:
    "Click twice to continue..."
    hide scrollingimage onlayer screens
    window hide
    $ renpy.pause(hard=True)
    show captured4_2 behind genericparallax:
        zoom 0.5 xalign 0.9 yalign 0.9
    hide screen genericparallax with dissolve
    scene black with dissolve
    scene captured3 with Fade(0,0.5,2):
        zoom 0.5
    "And thus, they would reciprocate the violence — If not on the battlefield, then in the dungeons. That was their way of extracting revenge."
    scene black with dissolve
    show rotate2 with dissolve:
        zoom 0.5
    "Having endured the wrath of those seeking revenge and being stripped of both their humanity and their autonomy..."
    show introanimwar with dissolve:
        zoom 0.5
    hide rotate2
    $ renpy.sound.play("/audio/soun_fx/intro/introwoman1.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    "The unfortunate Kunoichi would be made available for anyone to use..."
    "In the end, It didn't matter how, or whose offspring the women would carry, so long as they did."
    "Imprisoned and shackled in underground dungeons, their bodies were never to be found again. Their existence, diminished to that of a breeding mare up until the day their fertility would expire..."
    show introanimwar with dissolve:
        easein 20 alpha 0.05 zoom 0.9 xalign 0.2 yalign 0.1
    $ renpy.sound.play("/audio/soun_fx/intro/introwoman3.opus", channel="sfx3", loop=False, relative_volume = 0.8)
    "The more fortunate ones would perish at their captor's abuse before they would suffer bearing tens of their offspring."
    "But the Kunoichi that endured, hoping for a moment of reprieve, perchance even their liberation..."
    scene black with dissolve
    show captured3_1 with Fade(0.5,0.5,2):
        easein 7 xalign 0.4 zoom 0.5
    $ renpy.sound.play("/audio/soun_fx/intro/gruntwoman5.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    "Those women would inevitably conceive. 'Fed' and 'cared' for only as much as was needed for them to keep producing heirs..."
    $ renpy.sound.play("/audio/soun_fx/intro/evilmenlaugh.opus", channel="sfx3", loop=False, relative_volume = 0.8)
    "A twisted method of cultivating a stronger populace by way of selective breeding...?"
    show captured3_1:
        linear 10 alpha 0.0
    "Or perhaps, simply a deranged method of indulging upon their deepest, darkest desires."
    "Such was the way of a world build upon the premise of violence..."
    "Alas, not everyone would subscribe to a world like that..."
    $ renpy.end_replay()
    scene black with dissolve
    if disablentrwarning == False:
        $ disablentrwarning = True
        menu:
            "Would you like to disable optional NTR content?"
            "Disable optional NTR":
                $ persistent.netorareoptional = True
                "Optional NTR content is now disabled."
                "Given the circumstances of the Shinobi world, your actions may still lead to avoidable NTR!"
                "Act wisely..."
                pass
            "Enable optional NTR":
                $ persistent.netorareoptional = False
                pass
    show narutointro33 with dissolve:
        subpixel True

        xalign 0.5 yalign 1.0
        easeout 7 zoom 0.5
    "One man in particular, was to be largely credited for Konoha's survival, as well as its integrity..."
    
        
    $ na_name = renpy.input("What is his name?", default = na_name, length=15, allow="ABCDEFGHIJKLMNOPQRSTUVWXYZSabcdefghijklmnopqrstuvwxyz ").strip() or "Naruto"
    $ na_rel = renpy.input("He is your: (Leave empty for default) {p}Suggested roles: (Landlord, Guardian, etc.)", default = "", length=15, allow="ABCDEFGHIJKLMNOPQRSTUVWXYZSabcdefghijklmnopqrstuvwxyz ").strip() or "Dad"
    $ na_rel_to_bo = renpy.input("You are his: (Leave empty for default) {p}Suggested roles: (Tenant)", default = "", length=15, allow="ABCDEFGHIJKLMNOPQRSTUVWXYZSabcdefghijklmnopqrstuvwxyz ").strip() or "son"
    show narutointro11 at halfzoom with dissolve
    "[na_name], Konoha village's running chief."
    show negotiate1 at halfzoom with dissolve
    "After the war, [na_name] has been away from the village. Embroiled in constant political disputes with neighboring nations."
    show negotiate2 at halfzoom with dissolve
    "For years he fought and pleaded with other village chiefs trying to prevent another Shinobi War from breaking out."
    "And while his efforts would bring temporary peace, it was not without a cost..."
    show narutointro4 at halfzoom with dissolve
    "His continuous efforts would leave him stranded from his village, rarely allowing opportunities to visit."
    scene bg intro with fade
    show boruto normal with dissolve
    "Behind, he left you:"

    
    $ bo_name = renpy.input("What is your name?", default = bo_name, length=15, allow="ABCDEFGHIJKLMNOPQRSTUVWXYZSabcdefghijklmnopqrstuvwxyz ").strip() or "Boruto"
    $ bo_age = renpy.input("And your age:", default = "18", length=3, allow="1234567890").strip() or "18"
    default bo_name_stutter ="B-boruto"
    default hin_rel_stutter ="M-mom"
    $ bo_name_stutter = format_name_with_prefix(bo_name)
    show narutointro22 at halfzoom with dissolve
    "[na_name] was well respected both within his own nation but also those outside. His fighting prowess and reputation served as a detterant to any who thought of instigating against him."
    show narutointro4_1 at halfzoom with dissolve
    "But as the years passed by, [na_name] grew older and in the eyes of some, weaker."
    show ninjawar2 at halfzoom with dissolve
    "Tensions would slowly rise and so would those that were opposed to [na_name]'s idealistic views."
    scene ninjawar6 at halfzoom with dissolve
    "A world forged in violence is destined to be fought for in blood, not words or politcs..."
    play sound"/audio/soun_fx/swordslash2.opus" volume 0.6
    show warinblood at halfzoom with flash
    "A mantra that many would sympathize with, even within [na_name]'s village, Konoha."
    






    show negotiate2 at halfzoom with dissolve:
        easein 5 xalign 0.99 zoom 1.3
    "While [na_name] pursued peace fighting a hopeful battle of politics and appeasement..."
    $ playmusic("/audio/ost/Hurricane Suite ending.opus", 0.9)
    queue music ("audio/ost/Hyouhaku.opus") volume 0.4
    $ timer = 23.95
    $ timer2 = 25.6       # +1.8
    $ timer3 = 26.1         # +0.5
    $ timer4 = 27.5       # +1.5
    $ timer5 = 29.3       # +1.8
    $ timer6 = 29.8       # +0.5
    $ timer7 = 31.3       # +1.5
    $ timer8 = 33.1       # +1.8
    $ timer9 = 33.6       # +0.5
    $ timer10 = 35.1      # +1.5
    $ timer11 = 36.9      # +1.8
    $ timer12 = 37.4      # +0.5
    $ timer13 = 38.9      # +1.5
    $ timer14 = 40.7      # +1.8
    $ timer15 = 41.2      # +0.5
    $ timer16 = 42.7      # +1.5
    $ timer17 = 44.3      # +1.8
    $ timer18 = 44.8        # +0.5
    $ timer19 = 46.3      # +1.5
    $ timer20 = 46.4      # +1.5

    

    show screen timer_display
    show screen timer_display2
    show screen timer_display3
    show screen timer_display4
    show screen timer_display5
    show screen timer_display6
    show screen timer_display7
    show screen timer_display8
    show screen timer_display9
    show screen timer_display10
    show screen timer_display11
    show screen timer_display12
    show screen timer_display13
    show screen timer_display14
    show screen timer_display15
    show screen timer_display16
    show screen timer_display17
    show screen timer_display18
    show screen timer_display19
    show ninjawar4 with Fade(2,0.5,4):
        easein 6 zoom 0.5
    "Other nations would seize the opportunity to expand their territories."
    show ninjawar3 at halfzoom with dissolve
    "Conquest, being the singular greatest feat in their pursuit of dominance..."
    "And with them growing stronger, Konoha's passivity could prove to be its own demise."
    show narutofinal at halfzoom with dissolve
    show narutofinal:
        easeout 8 subpixel True zoom 1 xalign 0.9 yalign 0.2
    "Unrest would slowly fester within Konoha as [na_name]'s efforts were starting to be thought by many to be wishful thinking, a mirage, an unattainable dream..."
    "Some would even consider it an act of cowardice in the face of an adversarial period..."
    show warinblood2 at halfzoom with Fade(1,0.5,2):
        subpixel True
        xalign 0.5
        linear 10 zoom 1.2
    "But even worse than that..."
    "There are those who conspired against him. Scheming in the shadows, ready to capsize his valiant efforts of peace whenever the opportunity presented itself..."
    show warinblood1 at halfzoom with dissolve
    "All in pursuit of what was proven time and time again to be the remedy to all opposition..."
    show ninjawar5 at halfzoom with dissolve
    "An unyielding cycle of endless violence and war..."
    scene bg intro with fade 
    show boruto normal with dissolve
    
    call screen clicktwicescreen
    bo"."
    bo".."
    bo"..."
    bo "Sure is a long way home from school..." 
    show boruto embarassed with dissolve
    bo "Considering how bad that's going, I'm not even sure why I am still attending at this point."
    show boruto worried with dissolve
    bo "Putting in all that effort... for what? There is no prospect for a wondrous adventure, nor a potential romance brewing up."
    show boruto sad with dissolve
    bo "*Sigh...*"
    show boruto sad2 with dissolve
    bo "Is this all there is to life?"
    show boruto pain2 with dissolve
    $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx2", loop=False, relative_volume = 1.5)
    bo "Ugh...!" with vpunch
    "A sudden sharp pain jolts through your head"
    show boruto surprised2 with dissolve
    bo "Just a headache hopefully, I should pick up the pace and rest for a bit when I get home."
    default introponder = 0
    

    menu:
        bot "*Sigh...*"

        "Ponder idly in the rainfall":
            $ introponder +=1
            show boruto worried with dissolve
            bo "..."
            bo "Damn it, I must pick my self back up, before things get worse."
            bo "I can't keep wasting away like this..."
            call changeMoney(7) from _call_changeMoney
            show boruto laughing with dissolve
            "You found some coins in the street..."
            bo"Oh? My lucky day!"
            show boruto snob with dissolve
            bo"If this is a day of superstition, then let this happenstance signify the start of a radical change!"
            show boruto worried with dissolve
            menu:
            
                "Keep pondering":
                    $ introponder +=1
                    bo "*Sigh...*"
                    bo "For some reason, the rain droplets vaporizing on my face, it feels... nice..."
                    show boruto sad2 with dissolve
                    bo "Like a gentle caress from a loved one."
                
                "Go home":
                    jump go_home
            
            menu:
    
                "Keep... pondering?":
                    $ introponder +=1
                    show boruto normal with dissolve
                    bo "I really should get going... Wouldn't wanna get soaking wet..."
                    show boruto laughing2 with dissolve
                    bo "A certain someone would flip out of her tits if I did."
                    show boruto laughing with dissolve
                    bo "*Chuckles*"
                    show boruto smirk with dissolve
                
                "Go home":
                    jump go_home

            menu:
    
                "Why not... keep pondering after all?":
                    $ introponder +=1
                    show boruto normal with dissolve
                    bo "But seriously, who even cares about what they are teaching at school nowdays..."
                    bo "Pissagorean theorem? Hypotenuse this, square root that, yada yada bing bong, magic triangles out my ass!"
                    show boruto smirk with dissolve
                    bo "I really could not care less if I tried."
                    bo "And everyone's expecting me to expend my limited brain capacity on that bogus. Sheesh..."
                
                "Go home":
                    jump go_home

            menu:
    
                "Pond... of course you will":
                    $ introponder +=1
                    show boruto normal with dissolve
                    bo "Right, this is getting ridiculous now..."
                    bo "I can feel the extra weight of my clothes being soaked through!"
                    bo "I really should get going."
                    bo "Or maybe...."
                
                "Go home":
                    jump go_home


            menu:
    
                "Do I even have to ask?":
                    $ introponder +=1
                    show boruto laughing with dissolve
                    bo "You know, when people say I am stupid, I think they really mean that on a cellular level..."
                    bo "Perhaps I really am built alternatively than most."
                    show boruto smirk with dissolve
                    
                
                "Go home":
                    jump go_home

            menu:
    
                "!?":
                    stop music fadeout 1.0
                    play sound"/audio/soun_fx/heartbeat.opus" volume 1
                    #$renpy.music.play("/audio/soun_fx/suspense.opus", synchro_start=True, loop=False)
                    show boruto embarassed with dissolve
                    bo "Guess I really am retarded..."
                    play sound"/audio/soun_fx/heartbeat.opus"
                    bo "There's no denying it..."
                    play sound"/audio/soun_fx/heartbeat.opus" volume 1
                    show boruto normal with dissolve
                    ".."
                    play sound"/audio/soun_fx/heartbeat.opus" volume 1
                    show boruto worried2 with dissolve
                    "..."
                    play sound"/audio/soun_fx/heartbeat.opus" volume 1
                    $ renpy.sound.play("/audio/soun_fx/horror.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                    show boruto redpain with dissolve
                    show boruto pain with dissolve
                    "...!"
                    show boruto pain2 with dissolve
                    
                    bo "What was that!?"
                    show boruto surprised with dissolve
                    bo "I think I... sensed something, or someone. Almost as if something brushed my shoulder."
                    show boruto surprised2 with dissolve           
                    bo "But there's nobody there..."
                    show boruto suspicious with dissolve
                    bo "*Sigh*..."
                    show boruto worried2 with dissolve
                    bo"Must be the rainfall barraging down on my already null head..."
                    bo "I better hurry home now and get some much needed rest."
                    jump go_home


                    
                
                "Go home":
                    jump go_home



        "Hurry home before you are drenched":
            bo "...Better be quick before I am soaked wet"
            jump go_home

    label go_home:
    hide screen timer_display
    hide screen timer_display2
    hide screen timer_display3
    hide screen timer_display4
    hide screen timer_display5
    hide screen timer_display6
    hide screen timer_display7
    hide screen timer_display8
    hide screen timer_display9
    hide screen timer_display10
    hide screen timer_display11
    hide screen timer_display12
    hide screen timer_display13
    hide screen timer_display14
    hide screen timer_display15
    hide screen timer_display16
    hide screen timer_display17
    hide screen timer_display18
    hide screen timer_display19
    #pause(1)
    scene bg intro2 with fade
    show boruto smirk at left with dissolve
    bo "Took me a while..."
    show boruto normal with dissolve:
        easeout 1 xpos 1000

    stop music fadeout 1.0
    play sound "audio/soun_fx/dooropen.opus" volume 0.7
    $ renpy.sound.stop(channel="sfx1", fadeout = 2)
    hide boruto with dissolve
    "[bo_name] opens the door..."

    scene bg lr_day with dissolve:
        xalign 0.5 yalign 0.3
        zoom 0.68
    play music"/audio/ost/house2.opus" volume 0.6
    show boruto smirk with dissolve
    bo "I can hear someone in the living room, I better go say hello..."

    scene hina intro0 at halfzoom with dissolve
    "You caught her by surprise..."
    "Mature Lady" "Oh, [bo_name]!"
    $ hin_name = renpy.input("What is her name?", default = hin_name, length=15, allow="ABCDEFGHIJKLMNOPQRSTUVWXYZSabcdefghijklmnopqrstuvwxyz ").strip() or "Hinata"
    $ hin_rel = renpy.input("She is your: (Leave empty for default){p}Suggested roles: (Landlady, Guardian, etc.)", default = "", length=15, allow="ABCDEFGHIJKLMNOPQRSTUVWXYZSabcdefghijklmnopqrstuvwxyz ").strip() or "Mom"
    $ hin_rel_stutter = format_name_with_prefix(hin_rel)
    $ hin_rel_to_bo = renpy.input("You are her: (Leave empty for default) {p}Suggested roles: (Tenant)", default = "", length=15, allow="ABCDEFGHIJKLMNOPQRSTUVWXYZSabcdefghijklmnopqrstuvwxyz ").strip() or "son"
    $ hin_age = renpy.input("How old is she?:", default = hin_age, length=3, allow="1234567890 ").strip() or "36"
    default hin_rel_mother = hin_rel
    if hin_rel == "Mom" or hin_rel == "mom" or hin_rel == "Mother" or hin_rel == "mother" or hin_rel == "mommy" or hin_rel == "Mommy":
        $ hin_rel_mother = "Mother"
    else:
        $ hin_rel_mother = hin_rel
    label intro_hinataintroduction:
    scene hina intro00 at halfzoom with dissolve:
        xalign 0.9 yalign 0.3
        zoom 1.15
    $ initialize_replay_defaults()
    hin"I didn't realize you were home..."
    bo"Just arrived. How are you faring, [hin_rel]?"
    hin"I was just resting for a while after taking care of some house chores."
    scene hina intro00 at halfzoom with dissolve
    bot"This is my [hin_rel], Hinata, a retired chunin Kunoichi. Nowdays she spends most of her time keeping the house in order now that [na_rel] is away."
    bot"She is a woman of few words, loving and caring... But also quick to turn stern when an occasion calls for it."
    bot"While she rarely expresses her full thoughts or emotions, she is exceptionally cunning."
    scene black with dissolve
    bot"In fact she had somewhat of a reputation for being an unapologetically smart and observant shinobi in her active days."
    window hide 
    $ renpy.sound.play("/audio/soun_fx/wind2.opus", channel="sfx2", loop=False, relative_volume = 0.4)
    show warhinata2 at halfzoom, brightrevealzoom with dissolve
    bot"Characteristics perhaps derived from her more silent nature and introspective tendencies..."
    bot"Opposing shinobi would often mistake her silent traits for weakness. But of course, [hin_rel] would swiftly put their foolish ambitions to rest..." 
    show warhinaintro1 at halfzoom with dissolve
    bot"As she would prove time and time again fighting on the front lines, that she was one formidable Kunoichi."
    scene black with dissolve
    play sound "audio/soun_fx/swordsheathe1.opus" volume 0.4
    bot"Anyone who would underestimate her due to her femininity or introverted demeanor..."
    play sound "audio/soun_fx/swordslash1.opus" volume 0.7
    show warhinaintro2 at halfzoom with flash
    bot"Would quickly meet their demise at her hands."
    bot"[na_name] used to say that her reputation was getting too grand for her own good..."
    show warhinaintro3 at halfzoom with dissolve
    bot"And he was right, as [hin_name] started becoming a point of prime contention during battles."
    bot"Opposing nations would send entire fleets after her, perhaps due to her marital status with [na_name]..."
    show warhinaintro4 at halfzoom with dissolve:
        zoom 1.5 xalign 0.5
        linear 3 zoom 1
        subpixel True
    bot"Or maybe... other reasons I am not privy to."
    bot"While [hin_name] could fend for herself, the circumstances were far too dangerous for her to keep being out on the battlefield."
    show warhinatafinal at halfzoom with dissolve
    play sound "audio/soun_fx/swordsheathe2.opus" volume 0.7
    bot"[hin_name] would sheathe her sword one last time..."
    bot"As after the last war, [na_name] issued a mandate to officiate [hin_rel]'s absence from any and all future battles."
    bot"While most citizens understood the risks for both [hin_name] and Konoha as a whole..."
    bot"A small minority criticized my [na_rel]'s decision, as it seemed like preferential treatment. Not to mention the fact that Konoha would be losing one of its finest shinobi..."
    scene black with Dissolve(2)
    "[hin_name] takes a more modest posture as you unexpectadly enter the room"
    show hina intro11 at halfzoom:
        subpixel True
        xalign 0.5 yalign 0.99
        zoom 1.0
        linear 5 yalign 0.3
    with dissolve
    pause 2
    bot"Since then, [hin_rel] has been relegated to the role of a home caretaker... slowly left to wither into old age."
    bot"It doesn't sit too well with me to be honest, a woman of her stature... She deserves something better, something more."
    bot"Despite all that, she tries her best to be a caring mother-figure, but truth be told..."
    bot"I am feeling her growing distant lately. I think [na_rel]'s abscense combined with the surrounding circumstances has taken a toll on her..."
    bot"Perhaps the burden is too heavy for her to carry alone. Maybe she just needs someone to lean on..."
    bot"Or maybe seeing me devolve into the useless [hin_rel_to_bo] I have become has taken a toll on her..."
    bot"It's possible that if I picked up some responsibilities and did something with my life she would pick her self back up, and perhaps be more attentive of herself... and me."
    menu:
        bot "Until then, I will do what I can to make her"

        "Respect me":
            call changeRespect("Hinata", 1, "none") from _call_changeRespect_64
            bot"Respect me. I want our relationship to be of mutual respect so that we can both... thrive."
            bot"But right now I can understand why she is almost giving up on me. I am not bringing much to the table."
            bot"I should probably either start taking school seriously, or look into getting a job so I can provide some value to our house."
        "Love me":
            call changeLove("Hinata", 1, "none") from _call_changeLove_17
            bot"Love me... I just want to feel her tender embrace, her sweet affection. I miss the days when she'd put me between her arms and carelessly squeeze me to death, heh!"
            bot"I remember sitting there blushed, absorbing the warmth from her body while my sinuses were filled with her sweet aroma..."
            bot"If only we could go back to those days... I would do or give anything for that, to make her understand how much she means to me..."
        "Obey me":
            call changeObedience("Hinata", 1, "none") from _call_changeObedience_46
            bot"Obey... me."
            bot"Strong words, I know. But I just can't help and think of her as a woman."
            bot"After [na_name] left, she has been an empty shell of her former self, devoid of any ambition. Ironic coming from me, I know but..."
            bot"Such a beautiful lady, left to rot by my stupid [na_rel]. It is simply a waste..."
            bot"I want her to be more, she deserves to be more."
            bot"And if [na_rel] won't tend to that... then I will!"
    show hina intro22 at halfzoom with dissolve:
        xalign 0.5 yalign 0.2
        zoom 1.1
    hin"How about you [bo_name], are you doing okay? How was school?"
    bo"Uuuuh, you know... school was alright..."
    bo"Learned something about a... pissagoreum theorem or something?"
    show hina intro24 at halfzoom with dissolve:
        xalign 0.5 yalign 0.3
        zoom 1.0
    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx2", loop=False, relative_volume = 0.2)
    hin"[bo_name]!" with vpunch
    show hina intro23 at halfzoom with dissolve:
        xalign 0.5 yalign 0.2
        zoom 1.05
    hin"Mind your tongue!"
    show hina intro24 at halfzoom with dissolve:
        xalign 0.5 yalign 0.2
        zoom 1.0
    bot"[hin_rel] can be... overcaring at times."
    bot"She despises matters of vulglarity or indecency..."
    bot"But lucky for me, I know her better than that. She will probably scold me for a while..."
    bot"And two seconds after, she will go back to being the sweet, serene angel she always is."
    bot"She is just too nice for her own good. Probably the reason I turned into a good for nothing [hin_rel_to_bo]..."
    scene black with dissolve
    "[hin_name] stood up, as if getting ready to scold you..."
    bot"Here it comes..."
    scene bg lr_day:
        xalign 0.5 yalign 0.3
        zoom 0.68
    show shina angry at right:
        xzoom -1.0
    show boruto worried at left
    with dissolve
    hin"Pythagorean is what it's called and you better know how to apply it. It's basic geometry for crying out loud."
    show shina assertive with dissolve
    $ renpy.sound.play("/audio/soun_fx/hinata/hinatasigh3.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    hin"*Sigh*"
    show shina normal with dissolve

    hin"[bo_name], listen... A man sees in the world what he carries in knowledge."
    hin"To stop learning is to be complacent and complacency is worse than death!"
    show boruto surprised2
    show shina serious
    with dissolve
    hin"Do you understand?"
    menu:
        hin"Do you understand?"
        "I... think so":
            bo"Uuuuh... I.. t-think so?"
            show boruto smirk with dissolve
            bot"[hin_rel] sure is smart. But I am not. Hehe"
        "You are right":
            show boruto normal with dissolve
            bo"I never though about it like that, [hin_rel]..."
            show boruto laughing with dissolve
            bo"You sure are smarter than me and [na_rel]. *Giggles*"

    show boruto normal with dissolve
    show shina worried with dissolve
    $ renpy.sound.play("/audio/soun_fx/hinata/hinatasigh1.opus", channel="sfx2", loop=False, relative_volume = 0.3)
    hin"*Sigh*... You really are [na_name]'s [na_rel_to_bo]..."
    if introponder >= 3:
        show shina normal with dissolve
        hin"And why exactly are your clothes soaked in rain, [bo_name]! I just had them washed..."
        show boruto embarassed with dissolve
        bo"I might have stood under the rain a bit too long...Hehe! *Nervous laughter*"
    #show cg leaning forward boob
    scene bg hina scolding at halfzoom
    with fade
    hin"What am I going to do with you?"

    menu:
        hin"What am I going to do with you?"
        "(Let intrusive thoughts take control)":
            show bg hina scolding at halfzoom with dissolve:
                zoom 1.5 xalign 0.4 yalign 0.95
            bot"[hin_rel] is hiding it well with that oversized pink sweater she is wearing, but rest assured..."
            scene hina exercise at halfzoom with dissolve              
            bot"Her body is... well preserved."
            bot"Even after leaving her fighting days behind, she thinks it's mandatory to keep in combat shape..."
            scene hina exercise3 at halfzoom with dissolve
            bot"She wants to be able to defend herself and those she cares for when and if an occasion calls for it."
            scene hina exercise2 at halfzoom with dissolve
            bot"I know she is my [hin_rel] and all, but I... Just looking at her is pleasing to the eye, ya know?"
            scene hina exercise1 at halfzoom with dissolve
            bot"All that exercise is surely keeping her in shape, well past what a woman around her age has any hope of looking like..."
            
            bot"Sometimes I catch myself staring when she is doing some of her routine stretches"
            scene hina exercise4 at halfzoom with dissolve
            bot"It doesn't help my case when she practices her yoga posing in the living room..."
            bot"But then I remember, she is my [hin_rel], and I am no pervert... "
            bot"Or at least I try! *chuckles*"
            
            scene bg lr_day with dissolve:
                zoom 0.68
            show shina angry at left
            with vpunch
            hin"[bo_name_stutter]!"
            show boruto surprised at right with dissolve
            bot"Ah, shit! I zoned out."
            hin"Were you laughing at what I said?"
            menu:
                hin"Were you laughing at what I said?"
                "Come up with an excuse":
                    bo"U-uh... N-no! I just thought of something funny..."
                    show shina serious with dissolve
                    call changeRespect("Hinata", -1, "none") from _call_changeRespect_65
                    hin"Come on, [bo_name]. Don't zone out mid-conversation..."
                "'N-no! I got distracted by your...'":
                    bo"N-no! I got distracted by your b... uuh, you!"
                    show shina shy with dissolve
                    hin"...Huh?"
                    show shina angry2 with dissolve
                    call changeRespect("Hinata", -2, "none") from _call_changeRespect_66
                    hin"What kind of an excuse is that, [bo_name]!"
        
            show shina assertive with dissolve
            hin"Did you at least get what I said?"
            show boruto normal with dissolve
            bo"Yeah yeah, I am on it [hin_rel]..."
            show boruto smirk with dissolve
            bot"I have no idea what she said..."
            show boruto normal with dissolve
            bo"I will take a nap now, I am dead tired, talk to you later."
            show shina smiling with dissolve
            hin"Don't oversleep. I'll need your help later."








            scene black with fade
            bo"Sure thing."
       
            menu sneakmenu:
                "Go for a nap":
                    scene black with fade
                    "You make your way to your room..."
                    show bg bb intro
                    show boruto normal
                    with dissolve
                    bot"I Better get some sleep now."
                    stop music fadeout 2
                    hide boruto with dissolve
                    $ renpy.end_replay()
                    jump nap

                "Sneak one last peek":
                    scene black
                    show bg hina final:
                        subpixel True
                        xalign 0.5 yalign 0.5
                        zoom 0.7
                        easein 5.0 yalign 1.0
                    with dissolve
                        
                    bot"She is always so careless with that oversized sweater of hers..."
                    bot"Does she expect me not to take a look when it inadvertently slides down all the way to her b-breasts?"
                    bot"And as much as I try not to, my eyes are drawn down there too..."
                    "Press 'H' to hide the text box whenever you need to. (Use the Hide UI button at the bottom right if you are on mobile)"
                    bot"But..."
                    bot"I really have to stop perving on my [hin_rel]..."
                    scene black with fade
                    "You make your way to your room..."
                    show bg bb intro
                    show boruto normal
                    with dissolve
                    bot"I better get some sleep now."
                    stop music fadeout 2
                    hide boruto with dissolve
                    $ renpy.end_replay()
                    jump nap
                
                
        "You? You dont have to do anything":
            
            bo"It's not on you [hin_rel], it's on me. Trust me when I say, I will come around. I just need some... time."
            bo"Please don't worry too much about me."
            scene bg hina kiss at halfzoom with dissolve:
                xalign 0.5 yalign 0.3
                zoom 1.05
            
            call changeLove("Hinata", 1, "none") from _call_changeLove_18
            hin"Aww, my sweet boy..."
            hin"Time, we have in abundance. But waste too much of it and you will inevitably come to regret it, ok?"
            scene bg hina kiss2 with dissolve:
                subpixel True
                xalign 0.3 yalign 0.9
                zoom 0.7
                linear 4.0 yalign 0.2
                
            $ renpy.sound.play("/audio/soun_fx/hinata/kisscheek.opus", channel="sfx2", loop=False, relative_volume = 0.6)
            "[hin_name] leaned forward and kissed you on the cheek"
            scene bg lr_day with dissolve:
                zoom 0.68
            show boruto surprised at left with dissolve
            show shina smiling behind boruto with dissolve:
                xzoom(-1)
                xalign 0.3
                easein 1 xpos 0.5 ypos -34
            bot"That was... nice."
            show boruto surprised2 with dissolve
            bo"T-thanks [hin_rel],  I got it..."
            show boruto smirk with dissolve
            bo"I am off to take a nap now..."
            show boruto smirk2 with dissolve
            bo"See ya later!"
            show shina shy with dissolve
            hin"You and your excessive napping... Don't oversleep!"
            show shina shy with dissolve
            hin"I'll need your help later..."
            scene black with fade
            bo"Sure thing."
            $ renpy.end_replay()
            jump sneakmenu
    label nap:
        $ initialize_replay_defaults()
        $ renpy.sound.play("/audio/ost/sleep.opus", channel="sfx2", loop=False, relative_volume = 1.0)
        scene black with fade

        pause(1)
        "You fall into a deep slumber..."
        
        show dreamvignette zorder 100 with dissolve
        "A lucid dream captivates your senses..."
        play music"/audio/ost/dreaming.opus" volume 0.5
        $ renpy.sound.play("/audio/soun_fx/wind3.opus", channel="sfx3", loop=False, relative_volume = 0.8)
        show dream palace0 at brightreveal
        with longerflash
        bot"."
        bot".."
        bot"..."
        bot"W-what the hell is this place... It looks almost unearthly."
        bot"Come to think of it, Where... am I?"
        bot"Ahh, right..."
        bot"I was talking with my [hin_rel_mother] a moment ago and then I hit the bed. This must be a dream then..."
        bot"Although it feels so... vivid. Almost as if it were real."
        bot"I've never dreamt like this before..."
        $ renpy.sound.play("/audio/soun_fx/wind2.opus", channel="sfx2", loop=False, relative_volume = 0.8)
        bot"I feel like I am part of my surroundings. I can sense the air around me brushing against my skin, I can even smell it..."
        bot"But as I try to breathe it and speak, I realize... "
        bot"I am all but ethereal. I have no substance, no mass. I can't move or speak..."
        bot"I can only simply observe. And yet..."
        $ renpy.sound.play("/audio/soun_fx/wind1.opus", channel="sfx3", loop=False, relative_volume = 0.8)
        show dream palace1 at brightreveal
        with longerflash
        bot"This omnipotent feeling engulfs my every sense. I feel powerful, yet feeble. I am everything... but I am also nothing."
        "The pathway led you to an underground palace-like structure..."
        bot"It's as if I am an overarching deity, looking over my domain."
        bot"Even this place I am dreaming of looks like a place where a god would reside."
        bot"I have to find out what's going on, but how?"
        $ renpy.sound.play("/audio/soun_fx/wind4.opus", channel="sfx2", loop=False, relative_volume = 0.6)
        bot"A tall golden gate stands right below me as I float through the air. Surely it hides something important behind it..."
        bot"I wonder..."
        bot"...Will my dream lead me through it?"
        $ renpy.sound.play("/audio/soun_fx/gateopening.opus", channel="sfx3", loop=False, relative_volume = 0.6)
        show dream palace2 at brightreveal
        with longerflash
        
        pause 2
        $ renpy.sound.play("/audio/soun_fx/throneroom.opus", channel="sfx2", loop=False, relative_volume = 0.8)
        pause 1
        $ renpy.sound.play("/audio/soun_fx/whispers.opus", channel="sfx1", loop=False, relative_volume = 0.8)
        show dream palace2 at dizzy
        bot"Of course it would, but..."
        bot"I am getting... dizzy. I can hear... silent whispers..."
        bot"I think I can see someone at the end of this pathway. I can't quite make out who, but he looks like..."
        $ renpy.sound.play("/audio/soun_fx/godvoice.opus", channel="sfxstat", loop=False, relative_volume = 0.5)
        "Man sitting on throne" "You finally made it... my loyal servant!"
        bot"Huh...? Is he addressing me?"
        scene black
        show dreamvignette zorder 100
        with dissolve
        $ renpy.sound.play("/audio/soun_fx/wind4.opus", channel="sfxnotify", loop=False, relative_volume = 0.4)
        "Man sitting on throne" "I was expecting you for quite some time..."
        show dream bo1 with dissolve:
            zoom 1.3 xalign 0.5 yalign 1.0 subpixel True
        show dream bo1:
            easein 5 yalign 0.0
        "Man sitting on throne" "So much so... that my cock started yearning for your service!"
        bot"Huh!?" with vpunch
        bot"Who the fuck is this guy. Does he think I am... gay?"
        bot"And what's up with the leash and his massive-"
        "Man sitting on throne" "Care to explain your insolence!?" with vpunch
        show blackscreen with vpunch
        "The man on the throne forcibly yanks the leash he is holding..."
        scene dream hinaleash1 at brightrevealzoom,halfzoom
        show dreamvignette zorder 100
        with longerflash
        $ renpy.sound.play("/audio/soun_fx/intro/gruntwoman1.opus", channel="sfx2", loop=False, relative_volume = 0.4)
        "Forcing his subject that much closer to him..." with vpunch
        hin"Arh!"
        hin"...Forgive me my lord. I did not mean any disrespect."
        bot"[hin_rel_stutter]!?" with vpunch
        bot"Who is that bastard! Why is he ordering my [hin_rel_mother] around!?"
        bot"M-more importantly... w-why the h-hell is she n-naked?"
        show dream hinaleash1 with dissolve:
            zoom 0.55 yalign 1.0
        hin"After all, I exist to serve you, and my duties..."
        show dream hinaleash1_1 at brightreveal,halfzoom
        with longerflash
        hin"I intend to fulfil with pleasure!"
        bot"W-WHAT!?" with vpunch
        bot"It can't be... [hin_rel] would kill whoever that bastard is before he uttered another word!"
        bot"W-why is she doing this!?..."
        bot"She must have been forced into it! There's no way [hin_rel] would ever stoop so low!"
        "Man sitting on throne" "Well spoken, my loyal subject! For that is your purpose... isn't it?"
        "Man sitting on throne" "To attend to my every desire, to exist for my pleasure..."
        "Man sitting on throne" "Now crawl! Crawl to your master and come take what you crave, you whore!" with vpunch
        
        show dream hinaleash2 at brightrevealzoom,halfzoom
        with longerflash
        hin"At once, my lord!"
        bot"But of course, this is just a dream... That isn't really [hin_rel], is it?"
        bot"It's just an afterimage that happens to look like her..."
        bot"[hin_rel] would never let herself be called a w-whore... Let alone be humiliated like this!"
        bot"But even so, why would I ever dream of something like this..."
        menu:
            bot"But even so, why would I ever dream of something like this..."
            "Yank her leash!":
                bot"And why does it feel like I am..."
                "Man sitting on throne" "...That's my obedient little pet!"
                "Man sitting on throne" "But surely you can..."
                show dream hinayank1 at brightrevealzoom,halfzoom
                with vpunch
                $ renpy.sound.play("/audio/soun_fx/intro/gruntwoman1.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                hin"A-ah!" with vpunch
                "Man sitting on throne" "Crawl a little faster, can you not!?"
                show dream hinayank2 at halfzoom with dissolve
                hin"*Panting*"
                "Man sitting on throne" "Don't stop now, puppy! You have ways to go, don't you?"
                show dream hinayank3 at halfzoom with dissolve 
                hin"Y-yes master..."
                menu:
                    hin"Y-yes master..."
                    "Yank her leash again!":
                        "Man sitting on throne" "Then..."
                        scene black with vpunch
                        $ renpy.sound.play("/audio/soun_fx/gaspforair1.opus", channel="sfx2", loop=False, relative_volume = 0.2)
                        show dream hinayank4 at brightrevealzoom,halfzoom
                        "Man sitting on throne" "Crawl faster you whore! I am growing impatient..."
                        
                        hin"*Tired moaning*"
                        hin"A-as you c-command..."
                        "Man sitting on throne" "Only a few steps to go..."

                    "Spare her...":
                        "Man sitting on throne" "Only a few steps to go..."
                    


                
            "Bark for me dog!":
                bot"And why does it feel like I am..."
                "Man sitting on throne" "...That's my obedient little pet!"
                "Man sitting on throne" "Now bark for me like the dog you are!" with vpunch
                show dream hinabark1 at brightrevealzoom, halfzoom
                with flash
                hin"..."
                hin"*Wharf Wharf*"
                scene dream hinabark2 at halfzoom:
                    zoom 1.05 xalign 0.5 yalign 0.5
                show dreamvignette zorder 100
                with dissolve
                hin"...Master?"
     
                $ intro_dogmenu = []
                menu dogmenu:
                    set intro_dogmenu
                    hin"...Master?"
                    "Lick the floor!":
                        "Man sitting on throne" "Now lick the floor for me!"
                        show dream hinabark1 at halfzoom with dissolve:
                            zoom 1.0
                        hin"At once..."
                        show dream hinabark3 at brightrevealzoom,halfzoom
                        with flash
                        hin"*Licks floor*"
                        "Man sitting on throne" "That's it... clean my floors you nasty bitch!"
                        hide dream hinabark3
                        show dream hinabark3 at halfzoom:
                            zoom 1.1 xalign 0.5 yalign 1.0
                        with dissolve
                        hin"..."
                        jump dogmenu


                    "Crawl to me like a puppy!":
                        "Man sitting on throne" "Now crawl to me on all fours!"
                        show dream hinabark2 at halfzoom with dissolve:
                            zoom 1.0
                        hin"As you command..."
                        show dream hinabark4 at brightrevealzoom,halfzoom
                        with flash
                        hin"*Panting*"
                        "Man sitting on throne" "Good girl!"
                        "Man sitting on throne" "Don't you graze your knees now..."
                        show dream hinabark4 at halfzoom with dissolve:
                            zoom 1.1 xalign 0.5 yalign 1.0
                        "Man sitting on throne" "Only I get to break your delicate body!"
                        jump dogmenu
                    "That's enough!":
                        show dream hinabark2 at halfzoom with dissolve:
                            zoom 1.0
                        "Man sitting on throne" "That's enough, my loyal puppy!"
                        "Man sitting on throne" "Make your way to me, it's time for your reward..."
                        show dream hinabark1 at halfzoom with dissolve:
                            zoom 1.0
                        hin"Yes master!"
                        show dream hinabark4 at brightrevealzoom, halfzoom
                        with flash
                        "Man sitting on throne" "Come on, only a few steps to go..."
                        hin"*Exhausted moans*"
                        hin"Ughh... Argh..."
                        "Man sitting on throne" "You are not tired, are you?"
                        show dream hinaleash1_1 at brightrevealzoom, halfzoom
                        with flash
                        hin"N-no... master!"
                        "Man sitting on throne" "Good... We are only just getting started!"
                        scene black with vpunch
                        show dreamvignette zorder 100 with dissolve
                        "Man sitting on throne" "Come on then! Crawl faster you bitch..."


                        pass

        scene dream hinaleash3 at brightrevealzoom,halfzoom
        with flash
        show dreamvignette zorder 100 with dissolve
        hin"I am h-here... m-my lord!"
        "Man sitting on throne" "Look at you..."
        "Man sitting on throne" "Your wanting eyes..."
        "Man sitting on throne" "Your short, shallow breathing..."
        show dream bo3 with dissolve:
            zoom 1.3 xalign 0.5 yalign 1.0 subpixel True
        show dream bo3:
            easein 5 yalign 0.5
        "Man sitting on throne" "You yearn for this as much as I do — More, even... don't you?"
        hin"I do, m-master!"
        show dream bo3 with vpunch:
            zoom 1.4 xalign 1.0 yalign 0.3
        "Man sitting on throne" "Show me then!"
        show dream bo3 with vpunch:
            zoom 1.3 xalign 0.5 yalign 1.0
        "Man sitting on throne" "Look into my eyes and beg for your reward!"
        show lookup1 at brightrevealzoom
        with flash
        hin"P-please, master..."
        hin"Allow me to s-service you!"
        bot"This fucking bastard!"
        bot"How dare he disrespect my [hin_rel_mother] like that..."
        scene black with dissolve
        show dreamvignette zorder 100 with dissolve
        stop music fadeout 2
        bot"If only I knew who he was..."
        play music"/audio/ost/ramennight.opus" volume 0.7
        bot"I would kill him myself!"
        bot"Why am I stuck in this... n-nightmare!"
        bot"Come on..."
        
        show dream bo2:
            zoom 1.3 xalign 0.5 yalign 1.0 subpixel True
        with flash
        bot"Wake up!"
        show dream bo2 with dissolve:
            yalign 0.8
        bot"I am sick of this asshole parading my [hin_rel] around!"
        show dream bo2 with dissolve:
            yalign 0.7
        bot"Let..."
        show dream bo2 with dissolve:
            yalign 0.6
        bot"me..."
        show dream bo2 with dissolve:
            yalign 0.55
        bot"OUT!" with vpunch
        show dream bo2 at dizzyflash:
            easein 3 yalign 0.0
        with flash
        $ renpy.sound.play("/audio/soun_fx/horror.opus", channel="sfx2", loop=False, relative_volume = 0.9)
        $ renpy.sound.play("/audio/soun_fx/earringing.opus", channel="sfx3", loop=False, relative_volume = 0.1)
        with Shake((0, 0, 0, 0), 3, dist=10, peak_time=0.5, smoothness=40)
        
        bot"."
        bot".."
        show dream bo2 at dizzyflashshort
        bot"...!"
        boe"I am not convinced..."
        show dream bo2:
            zoom 1.25 xalign 0.5 yalign 1.0 subpixel True
        with flash
        boe"...[hin_rel_mother]!" with vpunch
        bot"W-what the... FUCK!?" with vpunch
        bot"It can't be..."
        show dream bo2 at dizzyflashshort:
            zoom 1.3 yalign 0.0
        with flash
        bot"T-that's... m-me?"
        bot"I am the one... holding [hin_rel]'s leash?"
        show dream bo3 at brightrevealzoom:
            zoom 1.5 yalign 0.0
        with flash
        bot"I am the one d-degrading h-her like that?"
        bot"W-why..."
        bot"HOW!?" with vpunch
        bot"I would n-never do something like this to her!"
        show dream bo3 with dissolve:
            zoom 1.6 yalign 0.0
        bot"W-whats with the grin on my face? Is he... enjoying this!?"
        bot"B-bastard! Why would you humiliate your [hin_rel_mother] like that!"
        $ renpy.sound.play("/audio/soun_fx/eye1s.opus", channel="sfx2", loop=False, relative_volume = 0.8)
        show dream bo3_1 at dizzyflashshort with dissolve:
            zoom 1.6 yalign 0.0
        boe"Beg for it! Yearn for my cock!"
        bot"S-stop it you asshole!"
        $ renpy.sound.play("/audio/soun_fx/eye2s.opus", channel="sfx2", loop=False, relative_volume = 0.9)
        show dream bo3_2 with flash:
            zoom 1.65 yalign 0.0
        boe"Show me how much of a whore you really are!"
        bot"No, [hin_rel]!"
        show dream bo3_2 with flash:
            zoom 1.7 yalign 0.0
        boe"Prove to me your desire to be defiled by your own [hin_rel_to_bo]!" with vpunch
        bot"She would n-never!"
        show dream hinafinal3 at brightrevealzoom
        with flash 
        boe"Isn't that what you long for... you despicable whore!?"
        bot"[hin_rel_stutter]... N-no..."
        hide dream hinafinal3
        show dream hinafinal3:
            zoom 1.1 xalign 0.0
        with dissolve
        boe"Huh!?" with vpunch
        scene lookup2 at brightrevealzoom
        show dreamvignette zorder 100
        with flash
        bot"Don't listen to him!"
        hin"Please [bo_name_stutter], I beg of you! L-let me have your seed!"
        hin"I need it... I want it!"
        $ config.menu_include_disabled = True
        menu introfinalmenu:
            hin"I need it... I want it!"
            "{color=[hatredcolor]}Abuse her{/color}":

                if introspit == 1:
                    boe"I've reconsidered..."
                    boe"What you did to me that fateful day... It is unforgivable [hin_rel]!"
                    boe"You will live the rest of your days repenting for it..."
                    boe"And you'll be mine to use as I see fit!"
                    jump introspit1
                elif introspit == 2:
                    boe"I've reconsidered..."
                    boe"You do deserve worse after all..."
                    boe"And so you shall have..."
                    jump introspit2
                elif introspit >=3:
                    boe"I simply cannot resist defiling your battered and abused face..."
                    jump introfinalspit

                default introspit = 0
                $ introspit += 1 #clean / introspit = 1
                boe"You want it that much... huh?"
                boe"I think you deserve something more than that..."
                hin"I... do?"
                boe"Oh yes you do! Say, something like..."
                $ renpy.sound.play("/audio/soun_fx/spit1.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                show spitfx1:
                    zoom 0.9 xalign 0.5 yalign 0.6
                show spitmark1:
                    xalign 0.52 yalign 0.22 zoom 0.15
                with dissolve and flash
                if intropissedon == True:
                    show dream spit1v
                else:
                    show dream spit1
                show spitmark1 zorder 1:
                    xalign 0.52 yalign 0.25 zoom 0.15 alpha 0.6
                with dissolve
                boe"Your [hin_rel_to_bo]'s spit on your face!"
                boe"Isn't that nice of me ...[hin_rel_mother]?"
                bot"Y-you bastard!"
                bot"Aaargh! W-why am I watching this! Why am I here!?"
                bot"[hin_rel] p-please..."
                if intropissedon == True:
                    show dream spit2v:
                        zoom 1.3 xalign 0.5 yalign 0.7
                else:
                    show dream spit2:
                        zoom 1.3 xalign 0.5 yalign 0.7
                
                show spitmark1 zorder 2:
                    xalign 0.52 yalign 0.28 zoom 0.14 alpha 0.4
                with dissolve
                hin"Y-yes, [bo_name_stutter]! T-thank you..."
                boe"You will not address me by my name again you whore!"
                show dream spit3:
                    zoom 1.4 xalign 0.5 yalign 0.7
                if intropissedon == True:
                    show dream spit3v:
                        zoom 1.4 xalign 0.5 yalign 0.7
                else:
                    show dream spit3:
                        zoom 1.4 xalign 0.5 yalign 0.7
                
                show spitmark1 zorder 3:
                    xalign 0.53 yalign 0.30 zoom 0.13 alpha 0.3
                with dissolve
                if intropissedon == True:
                    default introhinraged = False
                    $ introhinraged = True
                    boe"Oh you poor thing! Is that..."
                    boe"Do I spy rage within your eyes...[hin_rel_mother]!? Was getting pissed on and spat on by your own [hin_rel_to_bo] too much for you to bear?"
                    boe"Perhaps there is something you want to say...?"
                    hin"N-no... M-master. I would n-never!"
                    boe"Then get rid of that insolent look on your disgusting face right this very moment!" with vpunch
                hin"Of course, m-master!"
                boe"Look up to me then, you bitch!"
                if intropissedon == True:
                    scene dream spit4_1
                else:
                    scene dream spit4
                show dreamvignette zorder 10
                with dissolve
                boe"Good girl..."
                # show dream spit4 with dissolve:
                #     zoom 1.0 xalign 0.5 yalign 0.5
                boe"What you did to me that fateful day... It is unforgivable, [hin_rel_mother]!"
                bot"N-no... no no no! What the f-fuck is going on..."
                bot"I would never hurt [hin_rel]... P-please stop!"
                bot"Aaaaargh! Why can't I leave this nightmare!" with vpunch
                boe"You will live the rest of your days repenting for it..."
                boe"You will serve as my property to use as I see fit!"
                menu introspit1:
                    boe"You will serve as my property to use as I see fit!"
                    "{color=[hatredcolor]}Spit on her again!{/color}":
                        boe"If I please to see you covered in my spit..."
                        $ introspit += 1 #unclean / introspit = 2
                        $ renpy.sound.play("/audio/soun_fx/spit4.opus", channel="sfx2", loop=False, relative_volume = 1.2)
                        pause 0.5
                        show spitfx1:
                            zoom 0.9 xalign 0.5 yalign 0.6
                        show spitmark1:
                            xalign 0.52 yalign 0.26 zoom 0.15
                        with dissolve and flash
                        show dream spit2v zorder 1
                        show spitmark1 zorder 2:
                            xalign 0.52 yalign 0.35 zoom 0.15 alpha 0.5
                        with dissolve
                        boe"Then I shall do just that!"
                        hin"Y-yes... m-my lord!"
                        scene black with flash
                        show dreamvignette zorder 100 with dissolve
                        boe"Bah! Your face alone is enough to make my blood boil..." with vpunch
                        show dream bo3_1 at brightrevealzoom:
                            zoom 1.5 yalign 0.0 xalign 0.5
                        with flash
                        $ renpy.sound.play("/audio/soun_fx/eye2s.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                        "'You' take a seat once more..."
                        
                        boe"But I am getting carried away..."
                        boe"You are my [hin_rel_mother] after all..."
                        boe"I'd hate seeing you broken..."
                        $ renpy.sound.play("/audio/soun_fx/eyejougan.opus", channel="sfx2", loop=False, relative_volume = 0.8)
                        show dream bo3_2 with flash:
                            zoom 1.55 yalign 0.0 xalign 0.5
                        boe"At least not before I WANT you broken!"
                        show dream bo3_2 with dissolve:
                            zoom 1.58 yalign 0.0 xalign 0.5
                        boe"You insolent whore!" with vpunch
                        show dream bo3_2 with dissolve:
                            zoom 1.62 yalign 0.0 xalign 0.5
                        boe"To think you'd do something like that..."
                        show dream bo3_3 with dissolve:
                            zoom 1.65 yalign 0.0 xalign 0.5
                        boe"On second thought, maybe you do deserve worse!"
                        show dream bo3_2 at dizzyflashshort:
                            zoom 1.75 yalign 0.0 xalign 0.5
                        $ renpy.sound.play("/audio/soun_fx/eye1s.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                        with flash
                        boe"After all, why should I not break you! Your past actions warrant that much, if not more!"
                        show blackscreen with dissolve
                        "'You' rise again from your throne, but this time..."
                        hide blackscreen
                        show dream hinafinal3v at brightrevealzoom
                        with flash
                        boe"Have I been too tolerant of your insolence...?"
                        hide dream hinafinal3v
                        show dream hinafinal3v:
                            zoom 1.1 xalign 0.0
                        with dissolve
                        boe"Do you deserve to be battered and abused!?" with vpunch
                        show dream spit5v at brightrevealzoom
                        with flash
                        boe"ANSWER ME!" with vpunch
                        hin"I deserve... whatever it is you wish for me, m-master."
                        boe"You know your place well, impertinent pup!"
                        boe"And so you shall have..."
                        menu introspit2:
                            boe"And so you shall have..."
                            "{color=[hatredcolor]}Cover her in your spit!{/color}":
                                
                                label unlockedspit:
                                    $ notification("Previously exclusive scene")
                                    if introspit >= 3:
                                        boe"A little bit more of my spit on your face..."
                                        jump introfinalspit
                                    boe"My spit covering your filthy face!"
                                    show dream spit4_1 with dissolve:
                                        zoom 1.1 xalign 0.5 yalign 1.0
                                    boe"Take..."
                                    $ renpy.sound.play("/audio/soun_fx/spit3.opus", channel="sfx2", loop=False, relative_volume = 1.3)
                                    pause 0.2
                                    show spitfx1:
                                        zoom 0.9 xalign 0.5 yalign 0.6
                                    show spitmark2:
                                        xalign 0.52 yalign 0.22 zoom 0.15
                                    show spitmark1:
                                        xalign 0.52 yalign 0.22 zoom 0.15
                                    with dissolve and flash
                                    show dream spit2v zorder 1:
                                        zoom 1.15
                                    show spitmark2 zorder 2:
                                        xalign 0.52 yalign 0.25 zoom 0.15 alpha 0.6
                                    show spitmark1 zorder 2:
                                        xalign 0.52 yalign 0.25 zoom 0.15 alpha 0.6
                                    with dissolve
                                    boe"That! You disgusting whore..."
                                    boe"To think you'd do something like that to your own blood..."
                                    show dream spit3v zorder 1:
                                        zoom 1.2 xalign 0.5 yalign 1.0
                                    show spitmark2 zorder 2:
                                        xalign 0.53 yalign 0.23 zoom 0.15 alpha 0.4
                                    show spitmark1 zorder 2:
                                        xalign 0.53 yalign 0.23 zoom 0.15 alpha 0.4
                                    with dissolve
                                    boe"Have you no shame!?" with vpunch
                                    boe"Reprehensible... Unforgivable!"
                                    boe"Don't you look at me like that..."
                                    menu introunlockspitmenu:
                                        boe"Don't you look at me like that..."
                                        "Eyes up!" if introeyesup == False and intromouthopen == False:
                                            default introeyesup = False
                                            $ introeyesup = True
                                            boe"Eyes up!" with vpunch
                                            show dream spit1v
                                            show spitmark1:
                                                alpha 0.25 yalign -0.03
                                            show spitmark2:
                                                alpha 0.25 yalign -0.05
                                            with dissolve
                                            jump introunlockspitmenu

                                        "Mouth open!" if intromouthopen == False:
                                            default intromouthopen = False
                                            $ intromouthopen = True
                                            boe"Mouth open...!"
                                            show dream spit5v
                                            show spitmark1:
                                                alpha 0.25 yalign -0.03
                                            show spitmark2:
                                                alpha 0.25 yalign -0.05
                                            with dissolve
                                            jump introunlockspitmenu

                                        "Proceed..." if intromouthopen == True or introeyesup == True :
                                            boe"Good girl..."
                                            pass
                                            

                                    if intromouthopen == True and introeyesup == True:
                                        scene dream spit5v at brightrevealzoom
                                        show dreamvignette zorder 100
                                        with dissolve

                                    elif intromouthopen == True:
                                        scene dream spit5v at brightrevealzoom
                                        show dreamvignette zorder 100
                                        with dissolve

                                    else:
                                        scene dream spit1v at brightrevealzoom
                                        show dreamvignette zorder 100
                                        with dissolve

                                    $ intromouthopen = False
                                    $ introeyesup = False
                                    boe"We are not done yet..."
                                    boe"I have more in store for you!"
                                    $ introspit +=1 # 3
                                    menu introfinalspit:
                                        boe"I have more in store for you!"
                                        "{color=[hatredcolor]}Spit on her again!{/color}":
                                            if introspit == 3:
                                                boe"I will never forgive you..."
                                            elif introspit == 4:
                                                boe"And yet, that's not enough!"
                                                boe"Fuck you!" with vpunch
                                            else:
                                                boe"There's no forgiveness for the likes of you!"
                                                boe"Fuck you!" with vpunch
                                            pause 0.5
                                            show dream spit4_1 with dissolve:
                                                zoom 1.1 xalign 0.5 yalign 1.0
                                            $ renpy.sound.play("/audio/soun_fx/spit2.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                                            pause 0.5
                                            show spitfx1:
                                                zoom 0.9 xalign 0.5 yalign 0.6
                                            show spitmark2:
                                                xalign 0.52 yalign 0.22 zoom 0.15
                                            show spitmark1:
                                                xalign 0.52 yalign 0.22 zoom 0.15
                                            show spitmark3:
                                                xzoom (-1) xalign 0.49 yalign 0.16 zoom 0.15
                                            with dissolve and flash
                                            show dream spit2v zorder 1:
                                                zoom 1.15
                                            show spitmark2 zorder 2:
                                                xalign 0.52 yalign 0.25 zoom 0.15 alpha 0.6
                                            show spitmark1 zorder 2:
                                                xalign 0.52 yalign 0.25 zoom 0.15 alpha 0.6
                                            show spitmark3 zorder 2:
                                                xzoom (-1) xalign 0.49 yalign 0.19 zoom 0.15 alpha 0.6
                                            with dissolve
                                            boe"Take that! You disgusting whore..."
                                            boe"To think you'd do something like that to your own blood..."
                                            show dream spit3v zorder 1:
                                                zoom 1.2 xalign 0.5 yalign 1.0
                                            show spitmark2 zorder 2:
                                                xalign 0.53 yalign 0.23 zoom 0.15 alpha 0.4
                                            show spitmark1 zorder 2:
                                                xalign 0.53 yalign 0.23 zoom 0.15 alpha 0.4
                                            show spitmark3 zorder 2:
                                                xzoom (-1) xalign 0.48 yalign 0.17 zoom 0.15 alpha 0.6
                                            with dissolve
                                            if introspit == 3:
                                                boe"You filthy whore!" with vpunch
                                                boe"Say you are sorry!"
                                            elif introspit == 4:
                                                boe"Disgusting whore!"
                                            else:
                                                boe"Bitch!"
                                            
                                            if introspit == 3:
                                                hin"I... am s-sorry, m-master!"
                                            else:
                                                hin"P-please..."
                                            menu introunlockspitmenufinal:
                                                boe"Don't you look at me like that..."
                                                "Eyes up!" if introeyesup == False and intromouthopen == False:
                                                    $ introeyesup = True
                                                    boe"Eyes up!" with vpunch
                                                    show dream spit1v
                                                    show spitmark1:
                                                        alpha 0.25 yalign -0.03
                                                    show spitmark3:
                                                        alpha 0.25 yalign -0.05
                                                    show spitmark2:
                                                        alpha 0.25 yalign -0.05
                                                    with dissolve
                                                    jump introunlockspitmenufinal

                                                "Mouth open!" if intromouthopen == False:
                                                    $ intromouthopen = True
                                                    boe"Mouth open...!"
                                                    show dream spit5v
                                                    show spitmark1:
                                                        alpha 0.25 yalign -0.03
                                                    show spitmark3:
                                                        alpha 0.25 yalign -0.05
                                                    show spitmark2:
                                                        alpha 0.25 yalign -0.05
                                                    with dissolve
                                                    jump introunlockspitmenufinal

                                                "Proceed..." if intromouthopen == True or introeyesup == True :
                                                    boe"Good girl..."
                                                    pass
                                                    

                                            if intromouthopen == True and introeyesup == True:
                                                scene dream spit5v at brightrevealzoom
                                                show dreamvignette zorder 100
                                                with dissolve

                                            elif intromouthopen == True:
                                                scene dream spit5v at brightrevealzoom
                                                show dreamvignette zorder 100
                                                with dissolve

                                            else:
                                                scene dream spit1v at brightrevealzoom
                                                show dreamvignette zorder 100
                                                with dissolve

                                            $ intromouthopen = False
                                            $ introeyesup = False
                                            boe"We are not done yet..."
                                            boe"I have more in store for you!"
                                            $ introspit +=1 # 3
                                            jump introfinalspit
                                        "{color=[hatredcolor]}Slap her!{/color}":
                                            jump testslapjump
                                        "Spare her...":
                                            boe"...I've ruined your ugly face enough... haven't I, [hin_rel]!?"
                                            boe"But I think you can take more, can't you?"
                                            hin"M-master...?"
                                            jump introspit2
                                        

                                  
                            "{color=[hatredcolor]}Slap her!{/color}":
                                label testslapjump:
                                
                                $ notification("Previously exclusive scene")
                                label unlockedslap:
                                    if introslap == 0:
                                        # scene lookup2_2 with dissolve
                                        hin"M-master, p-please... Forgive me!"
                                        boe"Forgive... you?"
                                        label introhinrage:
                                        if introspit >=1 and introhinraged == False:
                                            $ introhinraged = True
                                            show dream spit2v with dissolve:
                                                zoom 1.5 yalign 0.6 xalign 0.5
                                            boe"You dare ask for... forgiveness?"
                                            show dream spit1v with dissolve:
                                                zoom 1.3 yalign 0.6 xalign 0.5
                                            boe"Look at me you whore!"
                                            show dream spit6_1 with dissolve:
                                                zoom 1
                                            show dream_hinaslap 1 with moveinright
                                            $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                            show dream_hinaslap 2
                                            $ renpy.sound.play("/audio/soun_fx/femalegrunt1.opus", channel="sfx3", loop=False, relative_volume = 0.3)
                                            with vpunch
                                            show dream spit7_1
                                            hide dream_hinaslap
                                            with dissolve
                                            boe"You ungrateful, useless bitch!" with vpunch
                                            show dream spit7_2 with Dissolve(1)
                                            boe"You deserve nothing but my wrath!" with vpunch
                                            # scene lookup2_2 with dissolve:
                                            #     zoom 1.2 xalign 0.5 yalign 0.5
                                            # hide dream spit2v
                                            scene dream spit4_1

                                            show dreamvignette zorder 10
                                            with dissolve

                                            show dream spit2v:
                                                zoom 1.3 xalign 0.5 yalign 0.7
                   
                                            with dissolve
                                            hin"Y-you are r-right, [bo_name_stutter]! P-please have m-mercy..."
                                            $ renpy.sound.play("/audio/soun_fx/spit2.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                                            pause 0.5
                                            show spitfx1:
                                                zoom 0.9 xalign 0.5 yalign 0.6
                                            # show spitmark1:
                                            #     xalign 0.52 yalign 0.22 zoom 0.15
                                            with dissolve and flash
                                            show spitmark1 zorder 2:
                                                xalign 0.52 yalign 0.25 zoom 0.15 alpha 0.6
                                            with dissolve

                                            scene dream spit4_1
                                            show dream spit3:
                                                zoom 1.4 xalign 0.5 yalign 0.7
                                            show dream spit3v:
                                                zoom 1.4 xalign 0.5 yalign 0.7
                                            show spitmark1 zorder 3:
                                                xalign 0.53 yalign 0.30 zoom 0.13 alpha 0.3
                                            with dissolve
                                            boe"You will not address me by my name again you whore!"
                                            hin"As y-you wish, m-master..."
                                            boe"Oh you poor thing! Is that..."
                                            if intropissedon == True:
                                                boe"Do I spy rage within your eyes...[hin_rel_mother]!? Was getting pissed on, spat on and slapped by your own [hin_rel_to_bo] too much for you to bear?"
                                            else:
                                                boe"Do I spy rage within your eyes...[hin_rel_mother]!? Was getting slapped and spat on by your own [hin_rel_to_bo] too much for you to bear?"
                                            boe"Perhaps there is something you want to say...?"
                                            hin"N-no... M-master. I would n-never!"
                                            boe"Then get rid of that insolent look on your disgusting face right this very moment!" with vpunch
                                            hin"Of course, m-master!"
                                            boe"Look up to me then, you bitch!"
                                            scene dream spit4_1
                                            show dreamvignette zorder 10
                                      
                                            with dissolve
                                            hin"I did not mean any disrespect, m-master..."
                                            hin"F-forgive me..."
                                            boe"Open your mouth you whore!" with vpunch
                                            scene lookup2_2 with dissolve:
                                                zoom 1 xalign 0.5 yalign 0.5
                                            show dreamvignette zorder 10
                                            with dissolve
                                            boe"Good girl..."
                                            boe"*Scoffs*... Forgive her she says..."

                                            menu:
                                                boe"*Scoffs*... Forgive her she says..."
                                                "{color=[hatredcolor]}Slap her again{/color}":
                                                    jump introslap1
                                                "Spare her...":
                                                    boe"...I've beaten your ugly face enough... haven't I, [hin_rel_mother]!?"
                                                    hin"M-master...?"
                                                    boe"Perhaps it's time we get back to your main course..."
                                                    jump introfinalmenu
                                        jump introslap1

                                    elif introslap == 1:
                                        scene lookup2_2 with dissolve
                                        hin"M-master, p-please... Forgive me!"
                                        boe"Forgive... you?"
                                        
                                        jump introslap1
                                    elif introslap == 2:
                                        boe"There's no forgiveness for what you've done... None!" with vpunch
                                        scene lookup2_2 with dissolve
                                        hin"Y-you are right m-master! I simply misspoke..."
                                        jump introslap2
                                    elif introslap >= 3:
                                        boe"Spewing shit... spreading lies!" with vpunch
                                        boe"That's what you are! A pathetic, ungrateful, useless lying [hin_rel_mother]!"
                                        
                                        scene lookup2_2 with flash
                                        boe"Look at me bitch!" with vpunch
                                        hin"..."
                                        jump introslapfinal
                                    else:
                                        pass
                                    boe"What you should have gotten long ago..."
                                    label unlockedslapfromspit:
                                    show dream_hinaslap 1 with moveinright
                                    $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                    show dream_hinaslap 2
                                    $ renpy.sound.play("/audio/soun_fx/femalegrunt1.opus", channel="sfx3", loop=False, relative_volume = 0.3)
                                    with vpunch
                                    show dream spit7_1
                                    hide dream_hinaslap
                                    with dissolve
                                    boe"A lesson in humility!"
                                    show dream spit7_2 with Dissolve(1)
                                    boe"Know your place! You impudent WHORE!" with vpunch
                                    if introspit >=1 and introhinraged == False:
                                        hin"F-forgive me... M-master!"
                                        jump introhinrage
                                    else:
                                        show dream spit7_2 with dissolve:
                                            zoom 1.1 xalign 0.5 yalign 1.0
                                        hin"M-master, p-please... Forgive me!"
                                        scene lookup2_2 with dissolve
                                        boe"Forgive... you?"
                                        default introslap = 0
                                        $ introslap += 1 #1

                                    menu introslapmenu:
                                        boe"Forgive... you?"
                                        "{color=[hatredcolor]}Slap her again!{/color}":
                                            if introslap == 1:
                                                show dream spit2v with dissolve:
                                                    zoom 1.5 yalign 0.6 xalign 0.5
                                                label introslap1:
                                                boe"You dare ask for... forgiveness?"
                                                show dream spit1v with dissolve:
                                                    zoom 1.3 yalign 0.6 xalign 0.5
                                                boe"Look at me you whore!"
                                                show dream spit6_1 with dissolve:
                                                    zoom 1
                                                show dream_hinaslap 1 with moveinright
                                                $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                                show dream_hinaslap 2
                                                $ renpy.sound.play("/audio/soun_fx/femalegrunt1.opus", channel="sfx3", loop=False, relative_volume = 0.3)
                                                with vpunch
                                                show dream spit7_1
                                                hide dream_hinaslap
                                                with dissolve
                                                boe"Impertinent animal!" with vpunch
                                                show dream spit7_2 with Dissolve(1)
                                                boe"There's no forgiveness for what you've done... None!" with vpunch
                                                scene lookup2_2 with dissolve:
                                                    zoom 1.2 xalign 0.5 yalign 0.5
                                                hide dream spit2v
                                                hin"Y-you are right m-master! I simply misspoke..."
                                                scene lookup2_2 with dissolve:
                                                    zoom 1 xalign 0.5 yalign 0.5
                                                $ introslap += 1 #2
                                                menu:
                                                    hin"Y-you are right m-master! I simply misspoke..."
                                                    "{color=[hatredcolor]}Slap her again{/color}":
                                                        jump introslap2
                                                    "Spare her...":
                                                        boe"...I've beaten your ugly face enough... haven't I, [hin_rel_mother]!?"
                                                        hin"M-master...?"
                                                        boe"Perhaps it's time we get back to your main course..."
                                                        jump introfinalmenu
                                                        
                                                    
                                                
                                            elif introslap == 2:
                                                
                                                scene dream spit2v:
                                                    zoom 1.5 yalign 0.6 xalign 0.5
                                                show dreamvignette zorder 100
                                                with dissolve
                                                label introslap2:
                                                scene dream spit2v:
                                                    zoom 1.5 yalign 0.6 xalign 0.5
                                                show dreamvignette zorder 100
                                                with dissolve
                                                boe"Misspoke... you say?"
                                                show dream spit1v with dissolve:
                                                    zoom 1.3
                                                hin"N-no... p-please! I didn't mean-"
                                                show dream spit6_1 with dissolve:
                                                    zoom 1
                                                show dream_hinaslap 1 with moveinright
                                                $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                                show dream_hinaslap 2
                                                $ renpy.sound.play("/audio/soun_fx/femalegrunt1.opus", channel="sfx3", loop=False, relative_volume = 0.3)
                                                with vpunch
                                                show dream spit7_1
                                                hide dream_hinaslap
                                                with dissolve
                                                boe"Isn't that all you do?" with vpunch
                                                show dream spit7_2 with Dissolve(1)
                                                boe"Spewing shit... spreading lies!" with vpunch
                                                boe"That's what you are! A pathetic, ungrateful, useless lying [hin_rel_mother]!"
                                                scene lookup2_2 with dissolve:
                                                    zoom 1.2 xalign 0.5 yalign 0.5
                                                hin"..."
                                                scene lookup2_2:
                                                    zoom 1 xalign 0.5 yalign 0.5
                                                show dreamvignette zorder 100
                                                with dissolve
                                                $ introslap += 1 #3
                                                menu:
                                                    hin"..."
                                                    "{color=[hatredcolor]}Slap her again{/color}":
                                                        jump introslapfinal
                                                    "Spare her...":
                                                        boe"...I've beaten your ugly face enough... haven't I, [hin_rel_mother]!?"
                                                        hin"M-master...?"
                                                        boe"Perhaps it's time we get back to your main course..."
                                                        jump introfinalmenu
                                            else:
                                                
                                                show dream spit2v with dissolve:
                                                    zoom 1.5 yalign 0.6 xalign 0.5
                                                label introslapfinal:
                                                boe"Once again... you brought the worst out of me [hin_rel]..."
                                                show dream spit1v with dissolve:
                                                    zoom 1.0 yalign 0.6 xalign 0.5
                                                show dream_hinaslap 1 with moveinright
                                                $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                                show dream_hinaslap 2
                                                $ renpy.sound.play("/audio/soun_fx/femalegrunt1.opus", channel="sfx3", loop=False, relative_volume = 0.3)
                                                with vpunch
                                                show dream spit7_1
                                                hide dream_hinaslap
                                                with dissolve
                                                boe"Gifted... aren't you?" with vpunch
                                                show dream spit7_2 with Dissolve(1)
                                                boe"You pitiful whore!" with vpunch
                                                scene lookup2_2 with dissolve:
                                                    zoom 1.2 xalign 0.5 yalign 0.5
                                                hin"..."
                                                scene lookup2_2:
                                                    zoom 1 xalign 0.5 yalign 0.5
                                                show dreamvignette zorder 100
                                                with dissolve
                                                $ introslap += 1 #4+
                                                menu:
                                                    hin"..."
                                                    "{color=[hatredcolor]}Slap her again{/color}":
                                                        jump introslapfinal
                                                    "I've had enough...":
                                                        boe"...I've had enough of beating your ugly face, [hin_rel_mother]!"
                                                        hin"M-master...?"
                                                        boe"Perhaps it's time we get back to your main course..."
                                                        jump introfinalmenu
                                                
                                                
                                                

                                        "Spare her...":
                                            boe"You shall have a moment of reprieve, for now..."
                                            boe"What do you say to that... [hin_rel]?"
                                            hin"T-thank you, m-master..."
                                            boe"Impudent whore..."
                                            if introslap >=1:
                                                scene lookup2_3
                                            else:
                                                scene lookup2_1
                                            show dreamvignette zorder 100
                                            with dissolve
                                            boe"Eyes on me!"
                                            jump introfinalmenu
                                        

                                    
                            "Spare her...":
                                boe"You shall have my benevolent kindness, for now..."
                                boe"What do you say to that... [hin_rel]?"
                                show lookup2_5 with dissolve:
                                    zoom 1.3 xalign 0.5 yalign 0.7
                                hin"T-thank you, m-master..."
                                boe"That's my whore..."
                                scene lookup2_1 at brightrevealzoom
                                show dreamvignette zorder 100
                                with flash
                                boe"Eyes on me!"
                                jump introfinalmenu
                                
                            
                        



                    "Spare her...":
                        show dream spit2 with dissolve:
                            zoom 1.3 xalign 0.5 yalign 0.7
                        hin"Of c-course... m-master."
                        bo"That's my whore..."
                        bo"Eyes on me!" with vpunch
                        scene lookup2
                        show dreamvignette zorder 100
                        with dissolve
                        jump introfinalmenu
                    
                            
                            
 
            "{color=[hatredcolor]}Piss on her{/color}":
                default intropiss = 0
                $ notification("Previously exclusive scene")
                label unlockedpissintro:
                    $ intropiss += 1 #1
                    show blackscreen with dissolve
                    boe"*Scoffs*" with vpunch                 
                    if introslap >= 1 or introspit>=2 or intropissedon == True:
                        scene dream hinafinal0v
                        show dreamvignette zorder 100
                        with dissolve
                    else:
                        scene dream hinafinal0 
                        show dreamvignette zorder 100
                        with dissolve
                    "'You' take a seat to contemplate your next action..."
                    boe"Considering what you've done to me..."
                    boe"...Do you really think you are deservant of my seed!?"
                    hin"M-master, If not for that..."
                    if introslap >= 1 or introspit>=2 or intropissedon == True:
                        show dream hinafinal0v with dissolve:
                            zoom 1.1 xalign 0.5 yalign 0.3
                    else:
                        show dream hinafinal0 with dissolve:
                            zoom 1.1 xalign 0.5 yalign 0.3
                    hin"T-then what would my p-purpose be?"
                    
                    show dream bo3_1 at dizzyflash with dissolve:
                        zoom 1.6 yalign 0.0
                    boe"Your... purpose?"
                    boe"I'll tell you what your purpose really is..."
                    show dream bo3_1 with dissolve:
                        zoom 1.65 yalign 0.0
                    boe"Your existance is utterly and completely futile..."
                    show dream bo3_1 with dissolve:
                        zoom 1.7 yalign 0.0
                    boe"You are only as useful as your holes allow you to be..."
                    show dream bo3_1 with dissolve:
                        zoom 1.75 yalign 0.0
                    boe"The moment I stop deriving pleasure from abusing you and your holes, is the moment you cease having any use!"
                    $ renpy.sound.play("/audio/soun_fx/eye1s.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                    show dream bo3_2 with flash:
                        zoom 1.8 yalign 0.0
                    boe"I will degrade, humiliate and punish you until the last of your days..."
                    boe"And when I am done extracting vengeance, then and only then..."
                    $ renpy.sound.play("/audio/soun_fx/eyesharingan2.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                    show dream bo3_3 at dizzyflashshort:
                        zoom 1.9 yalign 0.0
                    with flash
                    boe"Will I have you pay the ultimate price for what you've done!"
                    show dream bo3_3 with dissolve:
                        zoom 1.5 yalign 0.0
                    boe"When you are done doing that... perhaps you'll get to see the light of day once more!"
                    if introslap >= 1 or introspit>=2 or intropissedon == True:
                        show dream hinafinal0v with dissolve:
                            zoom 1.1 xalign 0.5 yalign 0.3 xzoom (-1)
                    else:
                        show dream hinafinal0 with dissolve:
                            zoom 1.1 xalign 0.5 yalign 0.3 xzoom (-1)
                    boe"Or perhaps not!" with vpunch
                    boe"Do you now realize... what your purpose is?"
                    hin"..."
                    if introslap >= 1 or introspit>=2 or intropissedon == True:
                        show dream hinafinal1v with dissolve:
                            zoom 1.1 xalign 0.5 yalign 0.3
                    else:
                        show dream hinafinal1 with dissolve:
                            zoom 1.1 xalign 0.5 yalign 0.3
                    boe"Do you understand, how little I think of you... [hin_rel_mother]!"
                    hin"Y-yes m-master..."
                    boe"And even so... you still crave for your [hin_rel_to_bo]'s cock... don't you?"
                    hin"I d-do..."
                    boe"Then you shall have it under one condition..."
                    scene black
                    show dreamvignette zorder 100
                    with dissolve
                    boe"Open your mouth you stupid whore!" with vpunch
                    $ renpy.sound.play("/audio/soun_fx/longpiss.opus", channel="sfx2", loop=True, relative_volume = 0.6)
                    if introslap >= 1 or introspit>=2 or intropissedon == True:
                        show dreamhinapiss1_v at brightrevealzoom:
                            zoom 1.0 xalign 0.5 yalign 0.5
                    else:
                        show dreamhinapiss1 at brightrevealzoom:
                            zoom 1.0 xalign 0.5 yalign 0.5
                    with flash
                    boe"You shall first serve as my personal urinal..."
                    boe"If you manage to swallow every last drop... maybe then and only then, will I consider stuffing my cock down your throat!"
                    if introslap >= 1 or introspit>=2 or intropissedon == True:
                        show dreamhinapiss2_v with dissolve:
                            zoom 1.0 xalign 0.5 yalign 0.5
                    else:
                        show dreamhinapiss2 with dissolve:
                            zoom 1.0 xalign 0.5 yalign 0.5
                    boe"Now crawl!"
                    if introslap >= 1 or introspit>=2 or intropissedon == True:
                        show introhina_pissv with dissolve:
                            zoom 1.0 xalign 0.5 yalign 0.5
                    else:
                        show introhina_piss with dissolve:
                            zoom 1.0 xalign 0.5 yalign 0.5
                    $ renpy.sound.play("/audio/soun_fx/whipping.opus", channel="sfx3", loop=True, relative_volume = 0.6)
                    "'You' walked backwards whilst whipping [hin_name]'s leash on the floor. The message was clear, follow or be punished..."
                    "The whipcracking sounds served to remind her of her place. Almost as if [hin_name] was your mare, to be instilled with fear..."
                    boe"Crawl you filthy whore!"
                    boe"Claim what you crave... Work for it, fight for it!"
                    boe"Don't stop following me until I am done pissing in your mouth!"
                    "Click twice to stop..."
                    show screen clicktwicescreen
                    $ ui.interact()
                    hide screen clicktwicescreen
                    hide introhina_piss
                    hide introhina_pissv
                    with dissolve
                    $ renpy.sound.stop(channel="sfx2", fadeout=1.0)
                    $ renpy.sound.stop(channel="sfx3", fadeout=1.0)
                    show dreamhinapiss1_v with dissolve
                    show dreamhinapiss4_1 with dissolve:
                        zoom 1.05 xalign 0.5 yalign 0.0
                    boe"Oh? [hin_rel_mother]... Are you crying?"
                    boe"Did I go and ruin your pretty face? Crying shame really..."
                    $ config.menu_include_disabled = True
                    menu intropissmenu:
                        boe"Did I go and ruin your pretty face? Crying shame really..."
                        "Gulp down my piss!" if introgulped == False:
                            default introgulped = False
                            boe"But you aren't done yet... are you?"
                            boe"Close your stinking mouth and swallow every... last... drop!"
                            show dreamhinapiss4_3 with Dissolve(1):
                                zoom 1.05 xalign 0.5 yalign 0.0
                            show dreamhinapiss4_2 with Dissolve(1):
                                zoom 1.05 xalign 0.5 yalign 0.0
                            hide dreamhinapiss4_3
                            $ renpy.sound.play("/audio/soun_fx/bj/Swallow 1.opus", channel="sfx3", loop=False, relative_volume = 1.5)
                            show dreamhinapiss4_3 with dissolve:
                                zoom 1.05 xalign 0.5 yalign 0.0
                            hide dreamhinapiss4_2
                            hin"*Gulp*"
                            boe"Show me..."
                            scene dreamhinapiss4_4:
                                zoom 1.05 xalign 0.5 yalign 0.0
                            show dreamvignette zorder 100
                            with dissolve
                            boe"Such a filthy skank!"
                            boe"Passable work, [hin_rel_mother]!"
                            $ introgulped = True
                            jump intropissmenu


                        "Degrade her further!":
                            $ introgulped = False
                            boe"Oh?"
                            show dreamhinapiss5 with dissolve:
                                zoom 1.05 xalign 0.5 yalign 0.0
                            $ renpy.sound.play("/audio/soun_fx/longpiss.opus", channel="sfx2", loop=True, relative_volume = 0.6)
                            boe"Would you look at that! A second wind..."
                            show dreamhinapiss5_1 with dissolve:
                                zoom 1.1 xalign 0.5 yalign 0.7
                            boe"Head down you whore!" with vpunch
                            boe"It would seem your job is not done yet!"
                            show introhina_pissv with dissolve:
                                zoom 1.0 xalign 0.5 yalign 0.5
                            $ renpy.sound.play("/audio/soun_fx/whipping.opus", channel="sfx3", loop=True, relative_volume = 0.6)
                            boe"Come on then!" with vpunch
                            boe"Keep crawling bitch!"
                            "Click twice to stop..."
                            show screen clicktwicescreen
                            $ ui.interact()
                            hide screen clicktwicescreen
                            hide introhina_piss
                            hide introhina_pissv
                            with dissolve
                            $ renpy.sound.stop(channel="sfx2", fadeout=1.0)
                            $ renpy.sound.stop(channel="sfx3", fadeout=1.0)
                            hide dreamhinapiss4_1
                            show dreamhinapiss1_v with dissolve
                            show dreamhinapiss4_1 with dissolve:
                                zoom 1.05 xalign 0.5 yalign 0.0
                            boe"You filthy whore..."
                            hide dreamhinapiss5
                            hide dreamhinapiss5_1
                            $ config.menu_include_disabled = True
                            jump intropissmenu
                        "Well done!" if introgulped == True:
                            $ config.menu_include_disabled = False
                            default intropissedon = False
                            $ intropissedon = True
                            $ introgulped = False
                            boe"Well done! An excellent display of your utilitarian use around here... don't you think so too, [hin_rel_mother]!"
                            hin"Y-yes! T-thank you, m-master..."
                            boe"But you see... I am not quite satisfied yet!"
                            jump introfinalmenu
                            
                        
                    
                    
                

                    jump introfinalmenu





            "Fuck her skull!" if introspit >= 1 or intropiss >= 1:
                $ call_label_action("fuckherskull_intro")
                call supp_rew from _call_supp_rew_16
                jump introfinalmenu
                label fuckherskull_intro:
                #introfinalmenu
                show dream bo3_1 at brightrevealzoom:
                    zoom 1.4 xalign 0.5 yalign 0.0
                with flash
                boe"Bravo [hin_rel_mother]!... Bravo!"
                boe"An entertaining performance..."
                boe"Despite your old age... you are still as eager as ever to serve your [hin_rel_to_bo]'s desires!"
                show dream bo3_2 at dizzyflashshort:
                    zoom 1.5 xalign 0.5 yalign 0.0
                $ renpy.sound.play("/audio/soun_fx/eye1.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                with flash
                boe"...You fucking hag!"
                show dream bo3_2 with dissolve:
                    zoom 1.55 xalign 0.5 yalign 0.0
                boe"I despise you so much..."
                show dream bo3_2 with dissolve:
                    zoom 1.6 xalign 0.5 yalign 0.0
                boe"You are deplorable, truly..."
                boe"But I reckon you do deserve a little something for all your efforts!"


                if introspit >= 2 or intropissedon == True or introslap >=1:
                    show dream hinafinal0v at brightrevealzoom
                    with flash
                else:
                    show dream hinafinal0 at brightrevealzoom
                    with flash
                boe"You've been a good slave, [hin_rel_mother]! The only thing you can excel at, really..."
                boe"You obeyed your [hin_rel_to_bo]'s every command. You attended to my every desire..."
                boe"You shall have your reward!"
                if introspit >= 2 or intropissedon == True or introslap >=1:
                    show dream hinafinal1v at brightrevealzoom
                    with flash
                else:
                    show dream hinafinal1 at brightrevealzoom
                    with flash
                boe"You can't wait for this... can't you?"
                hin"P-please master! Let me s-service your cock..."
                boe"Well then, you impatient whore...!"
                $ renpy.sound.play("/audio/soun_fx/intro/gruntwoman1.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                show dream hinafinal5 with flash
                "'You' harshly yank [hin_name]'s leash so that her face falls on your cock..."
                boe"Ask... and you shall receive!"

                scene black with flash
                show dreamvignette zorder 100
                if introspit >= 2 or intropissedon == True or introslap >=1:
                    show dreamending1 with dissolve:
                        xpos 68  yalign 0.0
                else:
                    show dreamending1_clean with dissolve:
                        xpos 68  yalign 0.0
                boe"Is this what you want? A young cock stuffed down your throat?"
                hin"Y-yes master. P-please! Can I t-touch it yet...?"
                if introspit >= 2 or intropissedon == True or introslap >=1:
                    show dreamending2 with dissolve:
                        xpos 468  yalign 0.0
                else:
                    show dreamending2_clean with dissolve:
                        xpos 468  yalign 0.0
                boe"Not yet you filthy whore..."
                boe"You've had me waiting all this time, now my cock is dripping with precum all over your smeared face..."
                show dreamending3 with dissolve:
                    xpos 868 yalign 1.0
                boe"All this slime leaking down on you... It needs to be cleaned up!"
                boe"Wouldn't want your ugly face to get any messier than it already is, would we?"
                hin"N-no master..."
                boe"Then it's time you do what you do best, [hin_rel_mother]!"
                menu dreamendingmenu:
                    boe"Then it's time you do what you do best, [hin_rel_mother]!"
                    "{color=[hatredcolor]}Extended scene{/color}":
                        $ notification("Previously exclusive scene")
                        label introfinalscenelocked:
                        
                        scene dreamending4_fs1 at brightrevealzoom
                        show dreamvignette zorder 100
                        with flash
                        boe"Your hands will stay on the ground while you lick my cock dry..."
                        boe"I want your mouth, your throat even, lubricated with my semen so that..."
                        boe"When I shove my cock deep inside your mouth, you'll be able to take it all the way to its base!"
                        show dreamending4_fs2 with dissolve:
                            zoom 1.1 xalign 0.0
                        hin"Y-your cock... d-down my t-throat..."
                        show dreamending4_fs1 zorder 50 with dissolve:
                            zoom 1.15 
                        scene black
                        show dreamvignette zorder 100
                        with flash
                        show dreamending5 with dissolve:
                            zoom 1.15 xalign 0.02 yalign 0.4
                        boe"I see your shit for brains has already left your mind broken..."
                        boe"Have you surrendered to lust... [hin_rel_mother]? I am not sure I like that..."
                        boe"No matter... I shall have at you as you are! Start licking you worthless piece of fuck-meat!"
                        show dreamending6_1 with dissolve:
                            zoom 1.15 xalign 0.98 yalign 0.4
                        hin"As you w-wish..."
                        show into_hina_final with dissolve:
                            zoom 1.15 xalign 0.98 yalign 0.4
                        $ renpy.sound.play("/audio/soun_fx/genericsexsound2.opus", channel="sfx3", loop=False, relative_volume = 1.0)
                        hin"*Lick* *Slurprs*"
                        boe"That's it you dirty whore! Twist and twirl your tongue around your [hin_rel_to_bo]'s cock..."
                        $ renpy.sound.play("/audio/soun_fx/genericsexsound2.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                        hin"*Continues Licking*"
                        boe"Although..."
                        show dreamending7 with dissolve:
                            zoom 1.15 xalign 0.02 yalign 0.4
                        boe"I don't think I like the fact that you seem to be enjoying this so much..."
                        show dreamending8 with dissolve:
                            zoom 1.15 xalign 0.98 yalign 0.4
                        boe"Back off you whore!" with vpunch
                        scene dream hinafinal1v at brightrevealzoom
                        show dreamvignette zorder 100
                        with flash
                        hin"M... M-master?"
                        boe"I... really, truly despise your face [hin_rel_mother]."
                        boe"It has come to the point where I can only get off when I see you in despair..."
                        menu introfinalmenu_locked:
                            boe"It has come to the point where I can only get off when I see you in despair..."
                            "{color=[hatredcolor]}Bring her to tears!{/color}":
                                default lockedscene_introfinal1 = True
                                $ lockedscene_introfinal1 = False
                                $ renpy.sound.play("/audio/soun_fx/intro/gruntwoman1.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                                show dream finalmenu1 with flash
                                boe"And so, I shall see you shedding tears of anquish to satisfy MY desires!"
                                show dream finalmenu1 with vpunch:
                                    zoom 1.1 xalign 0.5 yalign 0.0
                                "'You' held her leash high above her head, forcing [hin_name] to keep her posture high to avoid choking..."
                                show dream finalmenu1 with dissolve:
                                    zoom 1 xalign 0.5 yalign 0.0
                                boe"It's a shame I have to restrain from utterly and completely breaking your spirit before you fulfil your ultimate purpose..."
                                show dream finalmenu1_1 with dissolve:
                                    zoom 1.05
                                with vpunch
                                $ renpy.sound.play("/audio/soun_fx/inogag1.opus", channel="sfx3", loop=False, relative_volume = 1.0)
                                hin"*Gagging Noises*"
                                "[hin_name] started slowly frothing..."

                                boe"But I can still derive some pleasure from seeing you bawling at my hand!"
                                show dream finalmenu1_1 with dissolve:
                                    zoom 1.0
                                "[hin_name] might lose her senses if you push her too hard..."
                                default introabuse_firstaction = False
                                default introabuse_counter = 0
                                default introspitcounter = 0
                                menu introhina_abuse:
                                    boe"But I can still derive some pleasure from seeing you bawling at my hand!"
                                    "{color=[hatredcolor]}Spit in her mouth!{/color}":
                                        if introabuse_counter == 0 or introspitcounter == 0:
                                            show dream finalmenu_slap with dissolve
                                            if introabuse_firstaction == False:
                                                $ renpy.sound.play("/audio/soun_fx/gaspforair3.opus", channel="sfx2", loop=False, relative_volume = 1.3)
                                                $ introabuse_firstaction = True
                                                "'You' drop her leash and  grab her by her hair instead, allowing her a moment of reprieve to draw a much needed breath..."
                                            boe"Open your mouth bitch!"
                                            show dream finalmenu_spit with dissolve
                                            $ renpy.sound.play("/audio/soun_fx/spit2.opus", channel="sfx2", loop=False, relative_volume = 1.3)
                                            pause 0.5
                                            show spitfx1:
                                                zoom 0.9 xalign 0.5 yalign 0.6
                                            show spitmark2:
                                                xalign 0.45 yalign 0.45 zoom 0.15
                                            show spitmark1:
                                                xalign 0.45 yalign 0.45 zoom 0.15
                                            with dissolve and flash
                                            show dream finalmenu_spit_1 zorder 1:
                                                zoom 1
                                            show spitmark2 zorder 2:
                                                xalign 0.45 yalign 0.45 zoom 0.15 alpha 0.4
                                            show spitmark1 zorder 2:
                                                xalign 0.45 yalign 0.45 zoom 0.15 alpha 0.4
                                            with dissolve
                                            boe"I'll never tire of covering your ugly face in my spit..."
                                            boe"You disgusting whore..."
                                            scene dream finalmenu1_2
                                            show dreamvignette zorder 100
                                            with dissolve
                                            boe"Back to the leash bitch, Hold your head up high!"
                                            $ introspitcounter += 1
                                        else:
                                            show dream finalmenu_slap4 with dissolve
                                            if introabuse_firstaction == False:
                                                $ renpy.sound.play("/audio/soun_fx/gaspforair3.opus", channel="sfx2", loop=False, relative_volume = 1.3)
                                                $ introabuse_firstaction = True
                                                "'You' drop her leash and  grab her by her hair instead, allowing her a moment of reprieve to draw a much needed breath..."
                                            boe"That wasn't the last of it [hin_rel_mother]! Open up!"
                                            show dream finalmenu_spit_1 with dissolve
                                            $ renpy.sound.play("/audio/soun_fx/spit2.opus", channel="sfx2", loop=False, relative_volume = 1.3)
                                            pause 0.5
                                            show spitfx1:
                                                zoom 0.9 xalign 0.5 yalign 0.6
                                            show spitmark2:
                                                xalign 0.45 yalign 0.45 zoom 0.15
                                            show spitmark1:
                                                xalign 0.45 yalign 0.45 zoom 0.15
                                            with dissolve and flash
                                            show dream finalmenu_spit_2 zorder 1:
                                                zoom 1
                                            show spitmark2 zorder 2:
                                                xalign 0.45 yalign 0.45 zoom 0.15 alpha 0.4
                                            show spitmark1 zorder 2:
                                                xalign 0.45 yalign 0.45 zoom 0.15 alpha 0.4
                                            with dissolve
                                            boe"I won't stop until I hear you crying, bitch!"
                                            scene dream finalmenu1_3
                                            show dreamvignette zorder 100
                                            with dissolve
                                            boe"We are not done yet! Head held high you whore!"


                                        
                                        jump introhina_abuse




                                        
                                        
                                    "{color=[hatredcolor]}Smash her face!{/color}":
                                        if introabuse_counter == 0:
                                            show dream finalmenu_slap with dissolve
                                        elif introabuse_counter <=1:
                                            show dream finalmenu_slap4 with dissolve
                                        else:
                                            show dream finalmenu_slap5 with dissolve

                                        if introabuse_firstaction == False:
                                            $ renpy.sound.play("/audio/soun_fx/gaspforair3.opus", channel="sfx2", loop=False, relative_volume = 1.3)
                                            $ introabuse_firstaction = True
                                            "'You' drop her leash and  grab her by her hair instead, allowing her a moment of reprieve to draw a much needed breath..."
                                        boe"Come here you deplorable whore!"
                                        if introabuse_counter == 0:
                                            boe"Did you think you'd get what you wanted that easy?"
                                            boe"Do me a favor and hold your mouth wide open..."
                                            show dream finalmenu_slap1wider with dissolve
                                            $ renpy.sound.play("/audio/soun_fx/spit2.opus", channel="sfx2", loop=False, relative_volume = 1.3)
                                            pause 0.5
                                            show spitfx1:
                                                zoom 0.9 xalign 0.5 yalign 0.6
                                            show spitmark2:
                                                xalign 0.45 yalign 0.45 zoom 0.15
                                            show spitmark1:
                                                xalign 0.45 yalign 0.45 zoom 0.15
                                            with dissolve and flash
                                            show dream finalmenu_slap2spit zorder 1:
                                                zoom 1
                                            show spitmark2 zorder 2:
                                                xalign 0.45 yalign 0.45 zoom 0.15 alpha 0.4
                                            show spitmark1 zorder 2:
                                                xalign 0.45 yalign 0.45 zoom 0.15 alpha 0.4
                                            with dissolve
                                            boe"What did you think was going to happen you dumb hoe!" with vpunch
                                            #slap
                                            show dream_hinaslap 1 zorder 10:
                                                xpos 1000
                                            show dream_hinaslap 1 zorder 10:
                                                easeout 0.3 xpos 0
                                            
                                            pause 0.3
                                            show dream_hinaslap 2
                                            $ renpy.sound.play("/audio/soun_fx/spank8.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                            pause 0.1
                                            $ renpy.sound.play("/audio/soun_fx/femalegrunt1.opus", channel="sfx3", loop=False, relative_volume = 0.3)
                                            with vpunch
                                            hide dream_hinaslap
                                            show dream finalmenu_slap3
                                            with Dissolve(0.3)
                                            hin"Aar-ah!"
                                            show dream finalmenu_slap3_1 with dissolve
                                            boe"Must have felt that one [hin_rel_mother]!"
                                            show dream finalmenu_slap4 with dissolve:
                                                zoom 1.05
                                            boe"Holding back tears, are you now?"
                                            scene dream finalmenu1_3 with flash:
                                                zoom 1.0
                                            show dreamvignette zorder 100 with dissolve
                                            boe"No matter, you'll get there soon enough!"
                                        
                                        elif introabuse_counter == 1:
                                            boe"On with it then you bitch! You know what it is that I want to see!" with vpunch
                                            show dream finalmenu_slap4_1 with dissolve
                                            boe"Hah! You already know what's coming I see..."
                                            #slap
                                            show dream_hinaslap 1 zorder 10:
                                                xpos 1000
                                            show dream_hinaslap 1 zorder 10:
                                                easeout 0.3 xpos 0
                                            pause 0.3
                                            show dream_hinaslap 2
                                            
                                            $ renpy.sound.play("/audio/soun_fx/spank8.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                            pause 0.1
                                            $ renpy.sound.play("/audio/soun_fx/femalegrunt1.opus", channel="sfx3", loop=False, relative_volume = 0.3)
                                            with vpunch
                                            show dream finalmenu_slap5_1 at dizzyflashshort
                                            hide dream_hinaslap 2
                                            with dissolve

                                            
                                            boe"Oh oops... Did that leave you dazed, poor [hin_rel_mother]!?"
                                            $ renpy.sound.play("/audio/soun_fx/hinata/hinatacrying.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                                            show dream finalmenu_slap5 with dissolve:
                                                zoom 1.05
                                            boe"That's exactly what I was looking for! Cry for me you puny bitch!" with vpunch
                                            show dream finalmenu_slap5 with dissolve:
                                                zoom 1.1
                                            boe"Sob and beg for mercy..."
                                            scene dream finalmenu1_3 with flash:
                                                zoom 1.0
                                            hin"M-master... p-please!"
                                            show dreamvignette zorder 100 with dissolve
                                            boe"Is that all you can muster!?"
                                        
                                        elif introabuse_counter == 2:
                                            boe"What's with the stupid look on your face [hin_rel_mother]..."
                                            show dream finalmenu_slap5_1 with dissolve:
                                                zoom 1.05
                                            boe"Does your pride not allow you to beg for mercy?"
                                            show dream finalmenu_slap5_1 with dissolve:
                                                zoom 1.1
                                            boe"To think the famous [hin_name] of Konoha village only amounts to this sorry slob of meat..."
                                            show dream finalmenu_slap5_1 with dissolve:
                                                zoom 1.0
                                            boe"Is that it then... [hin_rel_mother]?"
                                            "You' knew from her demeanor that she could not take much more..."
                                            boe"What a shame, I expected more of a fight from you..."
                                            menu:
                                                boe"What a shame, I expected more of a fight from you..."
                                                "Deliver the finishing blow!":
                                                    boe"There's something to your face [hin_rel_mother]..."
                                                    show dream finalmenu_slap5 with dissolve:
                                                        zoom 1.1
                                                    boe"It just brings the worst out of me!"
                                                    hin"D-don't do it... [bo_name_stutter]! plea-"
                                                    show dream finalmenu_slap5 with dissolve:
                                                        zoom 1
                                                    #slap
                                                    show dream_hinaslap 1 zorder 10:
                                                        xpos 1000
                                                    show dream_hinaslap 1 zorder 10:
                                                        easeout 0.3 xpos 0
                                                    
                                                    pause 0.3
                                                    show dream_hinaslap 2
                                                    $ renpy.sound.play("/audio/soun_fx/spank8.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                                    pause 0.1
                                                    $ renpy.sound.play("/audio/soun_fx/femalegrunt1.opus", channel="sfx3", loop=False, relative_volume = 0.3)
                                                    with vpunch
                                                    hide dream_hinaslap
                                                    show dream finalmenu_slap5_3
                                                    with dissolve
                                                    $ renpy.sound.play("/audio/soun_fx/earringing.opus", channel="sfx2", loop=False, relative_volume = 0.2)
                                                    show dream finalmenu_slap5_3 at dizzy
                                                    with flash
                                                    boe"Hahahaha! So you can beg after all, [hin_rel_mother]!"
                                                    boe"But doing so by calling out my name? Tsk! No good..."
                                                    boe"What a shame... It would seem you've went and lost your fucking senses, bitch!"
                                                    boe"No matter... That didn't stop me before and it won't stop me now!"
                                                    jump introhina_faint

                                                "Play a sick joke on her":
                                                    show dream finalmenu_slap5 with dissolve:
                                                        zoom 1
                                                    boe"I shall put you out of your misery... shouldn't I [hin_rel_mother]!?"
                                                    show dream_hinaslap 1 zorder 10:
                                                        xpos 1000
                                                    show dream_hinaslap 1 zorder 10:
                                                        easein 0.3 xpos 100
                                                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp3.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                                                    pause 0.3
                                                    show dream_hinaslap 1 zorder 10:
                                                        easein 0.5 xpos 200 alpha 0
                                                    show dream finalmenu_slap4_1
                                                    with Dissolve(0.2)
                                                    pause 0.2
                                                    
                                                    hide dream_hinaslap
                                                    
                                                    show dream finalmenu_slap5_1 with dissolve
                                                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatacrying.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                                    boe"I jest, I jest! Don't you cry on me now! What kind of sick fuck would do that to his own [hin_rel_mother]..."
                                                    show dream finalmenu_slap5_1 with dissolve:
                                                        zoom 1
                                                    boe"I am not a monster you know!"
                                                    boe"Stay with me now, [hin_rel_mother]! You wouldn't be very useful if you passed out..."
                                                    scene dream finalmenu1_3 with flash:
                                                        zoom 1.0
                                                    show dreamvignette zorder 100 with dissolve
                                                    hin"..."
                                                    jump introhina_abuse

                                                "Spare her...":
                                                    show dream finalmenu_slap5_1 with dissolve:
                                                        zoom 1
                                                    boe"Stay with me now, [hin_rel_mother]! You wouldn't be very useful if you passed out..."
                                                    scene dream finalmenu1_3 with flash:
                                                        zoom 1.0
                                                    show dreamvignette zorder 100 with dissolve
                                                    hin"..."
                                                    jump introhina_abuse

                                                

                                        $ introabuse_counter += 1
                                        jump introhina_abuse
                                        
                                    "{color=[hatredcolor]}Keep strangling her!{/color}":
                                        $ introabuse_firstaction = False
                                        with vpunch
                                        if introabuse_counter == 0:   
                                            $ renpy.sound.play("/audio/soun_fx/inogag2.opus", channel="sfx2", loop=False, relative_volume = 1.3)
                                            boe"Are you feeling your airways grasping for air yet! Let me hear your choking sounds!"
                                            show dream finalmenu1_3 with dissolve:
                                                zoom 1.05
                                            boe"The more you struggle, the harder I get, [hin_rel_mother]!"
                                            show dream finalmenu1_3 with dissolve:
                                                zoom 1.0
                                            boe"But I need you to stay conscious for me..."
                                            
                                            show dream finalmenu1_2 with flash:
                                                zoom 1.1
                                            $ renpy.sound.play("/audio/soun_fx/gaspforair3.opus", channel="sfx1", loop=False, relative_volume = 1.5)
                                            pause 0.4
                                            $ renpy.sound.play("/audio/soun_fx/cough2.opus", channel="sfx3", loop=False, relative_volume = 0.4)
                                            boe"There, there... poor woman, take a breather..."
                                            hin"*Cough Cough* *Gasping for Air*"
                                            boe"Don't you black out on me now, [hin_rel_mother]... We have ways to go!"
                                            scene dream finalmenu1_3 with flash:
                                                zoom 1.0
                                            show dreamvignette zorder 100 with dissolve
                                            $ renpy.sound.play("/audio/soun_fx/inogag2.opus", channel="sfx2", loop=False, relative_volume = 1.3)
                                            boe"Let's get right back at it!" with vpunch
                                            with flash
                                        
                                        elif introabuse_counter == 1:
                                            $ renpy.sound.play("/audio/soun_fx/inogag2.opus", channel="sfx2", loop=False, relative_volume = 1.3)
                                            show dream finalmenu1_3 with dissolve:
                                                zoom 1.05
                                            boe"Must be close to suffocating now [hin_rel_mother]..."
                                            show dream finalmenu1_4 with dissolve:
                                                zoom 1.1
                                            boe"Perhaps if you begged for mercy one last time I'd change my mind"
                                            show dream finalmenu1_2 with flash:
                                                zoom 1.0
                                            $ renpy.sound.play("/audio/soun_fx/gaspforair3.opus", channel="sfx1", loop=False, relative_volume = 1.5)
                                            pause 0.4
                                            $ renpy.sound.play("/audio/soun_fx/cough2.opus", channel="sfx3", loop=False, relative_volume = 0.4)
                                            boe"Here, here... wanna try begging now?"
                                            hin"*Cough Cough* *Gasping for Air*"
                                            $ renpy.sound.play("/audio/soun_fx/hinata/hinatacrying.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                            show dream finalmenu1_3 with dissolve:
                                                zoom 1.1
                                            hin"*Restrained Crying*"
                                            boe"There it is, [hin_rel_mother]!" with vpunch
                                            show dream finalmenu1_3 with dissolve:
                                                zoom 1.0
                                            boe"What I've been waiting for! Cry you bitch!"
                                            boe"I want your tear-smeared face staring into the distance while I keep asphyxiating you!"
                                            
                                            scene dream finalmenu1_4 with flash:
                                                zoom 1.0
                                            show dreamvignette zorder 100 with dissolve
                                            $ renpy.sound.play("/audio/soun_fx/inogag2.opus", channel="sfx2", loop=False, relative_volume = 1.3)
                                            hin"[bo_name_stutter]... plea-!"
                                            boe"You dare call me by my name, [hin_rel_mother]!?" with vpunch
                                            boe"Insolent WHORE!"
                                            with flash

                                        elif introabuse_counter == 2:
                                            $ renpy.sound.play("/audio/soun_fx/inogag6.opus", channel="sfx2", loop=False, relative_volume = 1.3)
                                            show dream finalmenu1_4 with dissolve:
                                                zoom 1.05
                                            boe"You are fucking foaming [hin_rel_mother]!"
                                            boe"Don't tell me you are about to pass out..."
                                            "You' knew that she was close to pasing out..."
                                            boe"What a shame, I expected more of a fight from you..."
                                            menu:
                                                boe"What a shame, I expected more of a fight from you..."
                                                "Strangulate her!":
                                                    boe"But I told you already, didn't I [hin_rel_mother]!?" with vpunch
                                                    boe"Your struggles only serve to embolden me!"
                                                    show dream finalmenu1_4 with vpunch:
                                                        zoom 1.1
                                                    $ renpy.sound.play("/audio/soun_fx/inogag6.opus", channel="sfx2", loop=False, relative_volume = 1.3)
                                                    boe"Asphyxiate then you bitch!"
                                                    show dream finalmenu1_4 at dizzy:
                                                        zoom 1.2
                                                    with flash
                                                    boe"I want to see your life drained from your eyes..."
                                                    boe"I want to see you suffer for what you've done!" with vpunch
                                                    hin"..."
                                                    scene dream finalmenu_slap5_2 at brightrevealzoom
                                                    show dreamvignette zorder 100
                                                    with flash
                                                    boe"But you shouldn't perish just yet..."
                                                    "'You' let go just as [hin_name] lost her senses. Instead, 'you' held her unconscious body up by her hair..."
                                                    boe"No, no, no... Death would be an easy way out for you."
                                                    boe"I won't have you get off that easily, not after what you've done!"
                                                    $ renpy.sound.play("/audio/soun_fx/spit2.opus", channel="sfx2", loop=False, relative_volume = 1.5)
                                                    pause 0.5
                                                    scene black with flash
                                                    $ renpy.sound.play("/audio/soun_fx/bodythud.opus", channel="sfx2", loop=False, relative_volume = 1.3)
                                                    "*Body thuds*!"
                                                    jump introdreamend


                                                
                                     

                                                "Spare her...":
                                                    show dream finalmenu1_2 with flash:
                                                        zoom 1.0
                                                    $ renpy.sound.play("/audio/soun_fx/gaspforair3.opus", channel="sfx1", loop=False, relative_volume = 1.5)
                                                    pause 0.4
                                                    $ renpy.sound.play("/audio/soun_fx/cough2.opus", channel="sfx3", loop=False, relative_volume = 0.4)
                                                    hin"*Cough Cough* *Gasping for Air*"
                                                    $ renpy.sound.play("/audio/soun_fx/hinata/hinatacrying.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                                                    show dream finalmenu1_3 with dissolve:
                                                        zoom 1.1
                                                    hin"*Restrained Crying*"
                                                    boe"Don't you worry [hin_rel_mother]..." with vpunch
                                                    show dream finalmenu1_3 with dissolve:
                                                        zoom 1.0
                                                    boe"I want you to stay with me. After all..."
                                                    boe"What kind of monster would strangulate his own [hin_rel_mother]!"                                                    
                                                    scene dream finalmenu1_4 with flash:
                                                        zoom 1.0
                                                    show dreamvignette zorder 100 with dissolve
                                                    $ renpy.sound.play("/audio/soun_fx/inogag2.opus", channel="sfx2", loop=False, relative_volume = 1.3)
                                                    boe"But I still have to keep you in check" with vpunch
                                                    with flash
                                                    jump introhina_abuse

                                            
                                        $ introabuse_counter += 1
                                        jump introhina_abuse
                                        
                                    "Return":
                                        jump introfinalmenu_locked
                                        
                                    

                            "Finish what you started...":
                                boe"But I shall fuck your face regardless..."
                                show dream hinafinal5 with flash
                                boe"Get over here you whore!" with vpunch
                                show dream hinafinal6 with dissolve
                                boe"It's nigh time I expand your throat's crevices!"
                                show dream hinafinal7 with dissolve
                                boe"Open wide... [hin_rel_mother]!"
                                show dream hinafinal8 with dissolve
                                boe"Is that all you can do?"
                                boe"Wider you god-damned demon!" with vpunch
                                show dream hinafinal9 at brightrevealzoom
                                with flash
                                pause 0.5
                                boe"That's more like it! Now..."
                                boe"How would you prefer I bury my cock inside your throat..."
                                boe"Do I yank on your leash like the animal that you are, or do I simply violently thrust and bury my cock in your mouth-pussy..."
                                $ renpy.sound.play("/audio/soun_fx/inogarggle1.opus", channel="sfx2", loop=False, relative_volume = 0.6)
                                show dream hinafinal9 with dissolve:
                                    zoom 1.2 xalign 0.8 yalign 0.2
                                hin"mhhmmm *Muffled sounds*"
                                menu:
                                    hin"mhhmmm *Muffled sounds*"
                                    "Pull her leash!":
                                        show dream hinafinal10 at dizzy2:
                                            zoom 1.2
                                        $ renpy.sound.play("/audio/soun_fx/pushitin1.opus", channel="sfx1", loop=False, relative_volume = 0.6)
                                        $ renpy.sound.play("/audio/soun_fx/gags/SDTGag8.opus", channel="sfx3", loop=False, relative_volume = 1.6)
                                        with flash
                                        boe"Choke on your [hin_rel_to_bo]'s cock you stupid fucking bitch!" with vpunch
                                    "Thrust forward!":
                                        show dream hinafinal10 at dizzy2:
                                            zoom 1.4 xalign 0.7 yalign 0.3
                                        $ renpy.sound.play("/audio/soun_fx/pushitin1.opus", channel="sfx1", loop=False, relative_volume = 0.6)
                                        $ renpy.sound.play("/audio/soun_fx/gags/SDTGag1.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                                        with flash
                                        boe"Take your [hin_rel_to_bo]'s cock deep down your throat you stupid fucking bitch!" with vpunch
                                    
                                
                                boe"Fuck you!" with vpunch
                                show dream hinafinal10_1 with dissolve
                                jump introhina_nofaint
                            



                        bot"Get me out of this fucking nightmare!"
                        scene black with vpunch
                        with longerflash
                        
                        jump introdreamend

                        
                    "Escape the nightmare":
                        hide dreamending3 with dissolve
                        bot"No, fuck this shit!"
                        hide dreamending2_clean
                        hide dreamending2
                        with dissolve
                        bot"I am not about to watch my self fuck my own [hin_rel]!"
                        hide dreamending1_clean
                        hide dreamending1
                        with dissolve
                        bot"Get me out of this fucking nightmare!"
                        scene black with vpunch
                        with longerflash
                        
                        jump introdreamend
                    

            "Get me out of this nightmare!":
                show lookup2 at dizzyflash:
                    zoom 1.2 yalign 0.0 xalign 0.5
                bot"No! I am not about to watch my self fuck my own [hin_rel]!"
                show lookup2 at dizzyflash:
                    zoom 1.4 yalign 0.0 xalign 0.5


                bot"Get me out of this fucking nightmare!"
                scene black with vpunch
                with longerflash
                
                
                jump introdreamend
            

                label introhina_faint:
                scene dream finalmenu_slap5_3 at dizzyflashshort:
                    zoom 1.1 xalign 0.5 yalign 0.5
                show dreamvignette zorder 100
                with flash
                boe"I shall fuck your skull even as your senses are half gone you whore!" with vpunch
                $ renpy.sound.play("/audio/soun_fx/wakeup.opus", channel="sfx3", loop=False, relative_volume = 1.6)
                with Shake((0, 0, 0, 0), 1, dist=30, peak_time=0.9, smoothness=30)
                $ renpy.sound.play("/audio/soun_fx/inogag4.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                $ renpy.sound.play("/audio/soun_fx/cum12.opus", channel="sfx1", loop=False, relative_volume = 1.0)
                scene dream hinafinal10 with flash:
                    zoom 1.4 xalign 0.3 yalign 0.3
                
                show screen endof_introfaint with flash
                scene black with flash
                jump introdreamendfromfaint

                label introhina_nofaint:
                $ renpy.sound.play("/audio/soun_fx/wakeup.opus", channel="sfx3", loop=False, relative_volume = 1.6)
                with Shake((0, 0, 0, 0), 1, dist=30, peak_time=0.9, smoothness=30)
                $ renpy.sound.play("/audio/soun_fx/inogag4.opus", channel="sfx2", loop=False, relative_volume = 1.0)
                $ renpy.sound.play("/audio/soun_fx/cum12.opus", channel="sfx1", loop=False, relative_volume = 1.0)
                scene dream hinafinal10 with flash:
                    zoom 1.4 xalign 0.3 yalign 0.3
                
                show screen endof_introfaint with flash
                scene black with flash
                jump introdreamendfromfaint
                

                    

        
            





        label introdreamend:
        bot"Aaaaargh!!"
        $ renpy.sound.play("/audio/soun_fx/wakeup.opus", channel="sfx3", loop=False, relative_volume = 0.6)
        label introdreamendfromfaint:
        $ config.menu_include_disabled = False
        $ playmusic("/audio/ost/house2.opus", 0.5)
        scene bg bb intro at brightreveal:
            matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 
        with longerflash
        with Shake((0, 0, 0, 0), 1, dist=20, peak_time=0.8, smoothness=50)
        show boruto box2surprised with Dissolve(1):
            blur 30
        show boruto box2surprised with Dissolve(2):
            easein 2 blur 0
        $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx2", loop=False, relative_volume = 0.3)
        $ renpy.end_replay()
        bot"*Rapid breathing*"
        bot"..."
        bot"W-what the fuck just happened! ...A d-dream?"
        bot"...Thank fuck!"
        bot"But it was so vivid. I could have sworn I was there..."
        if lockedscene_introfinal1 == False:
            call changeHatred(1) from _call_changeHatred_26
            bot"I almost feel a sense of contempt for myself having experienced that shit..."
        "You realize something's poking under your boxers..."
        window hide
        
        pause 0.5
        scene black with vpunch
        bot"Why is my...!"
        bot"Am I finally losing it? ...*Sigh* Fuck me!"
        $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.4)
        bot"I better put on some clothes and go outside. I need to clear out this useless head of mine..."

        



            
        scene bg bb intro:
            matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 


        show boruto surprised2
        with dissolve
        bo"Shit! I overslept... again!" with vpunch
        show boruto worried with dissolve
        bo"Can't blame me after that shitty nightmare though!"
        show boruto normal with dissolve
        bo"[hin_rel] did say earlier that she needed me for something."
        show boruto worried2 with dissolve
        bo"I should tend to her, make sure she is okay too..."
        
        $ renpy.sound.play("/audio/soun_fx/footsteps.opus", channel="sfx2", loop=False, relative_volume = 0.4)
        scene bg day with dissolve:
            xalign 0.5 yalign 0.5
            zoom 1
        show boruto surprised2 at center with dissolve
        bot"Someone's making loud thudding noises in the room next to mine..."
        show boruto normal with dissolve
        bot"I should check what's going on!"
        screen peakingIntro(baseImage):
            on "show" action Function(mark_screen_image_gallery, baseImage)
            key "K_SPACE" action Return()
            button:
                action Return()
            viewport id "peaking":
                child_size (1600, 1328)
                edgescroll (340, 550)
                draggable True
                yinitial 0.1
                xinitial 0.1
            
                frame:
                    background None            
                    xalign 0.5
                    viewport:
                        area (320, 0, 1.0, 1.0)
                        child_size (1600, 1328)
                        edgescroll (340, 550)
                        add baseImage subpixel True at halfzoom
        menu himaintro:
            bot"I should check what's going on!"
            "Barge in":
                play sound "audio/soun_fx/dooropen.opus" volume 0.7
                scene barg1:
                    xalign 0.5 yalign 0.5 zoom 0.7
                with fade
                call changeDominance(1, "none") from _call_changeDominance_15
                bo"The hell is going on in here?"

                show barg2:
                    xalign 0.99 yalign 0.5
                    zoom 0.75

                "Girl" "[bo_name], what the fuck!" with vpunch
                bo"Uuuuuh! It's not what you think, I-i heard some loud t-thuds a-and.."
                show barg2:
                    xalign 0.99 yalign 0.5
                    zoom 0.8
                "Girl" "Knock on the freakin' door you goddamn idiot!" with vpunch
                scene black with fade
                "Girl" "Just.. Give me a second to wrap up."
                "."
                ".."
                "..."
                show himawari_bedroom_1:
                    blur 20
                show knock2_1 at halfzoom:
                    xalign 0.5 yalign 0.1
                    zoom 0.7
        
                with dissolve
                "Girl" "So...? What do you want you brute!"
                bo"I thought I should check up on you, heard some loud thuds from outside. Thought you... fainted... or something?"
                show knock2_1 at halfzoom with dissolve:
                    xalign 0.5 yalign 0.1
                    zoom 0.8
                "Girl" "Are you... stupid?" 
                show knock2_1 at halfzoom with dissolve:
                    xalign 0.5 yalign 0.1
                    zoom 0.7
                "Girl" "It was just me exercising you twat." with vpunch
                show knock2_1 at halfzoom with dissolve:
                    xalign 0.5 yalign 0.75
                    zoom 0.7
                    subpixel True
                    linear 2.0 yalign 0.99
                "Girl" "Wooden floors... working out..."
                show knock2_1 at halfzoom with dissolve:
                    xalign 0.5 yalign 0.5
                    zoom 0.5
                $ renpy.sound.play("/audio/soun_fx/himawari/himascoff1.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                "Girl" "*Scoffs* Use that brain of yours and connect the dots, will you?"
                show knock2 at halfzoom with dissolve:
                    xalign 0.5 yalign 0.1
                    zoom 0.75
                
                #show bg horizontal3
                $ renpy.sound.play("/audio/soun_fx/himawari/loserlaugh.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                "Girl" "Now get out before I beat your ass."
    
                

                jump himaintroduction

            "Knock on the door":
                $ renpy.sound.play("/audio/soun_fx/doorknock.opus", channel="sfx2", loop=False, relative_volume = 1)
                bo"Can I come in?"
                "Girl" "Give me a sec, [bo_name]"
                menu himadoorknock:
                    bot"..."
                    "Peek inside through the keyhole":
                        show boruto smirk with dissolve
                        bot"Curiosity killed the cat or something..."
                        show boruto sceeming2 with dissolve
                        bot"But I am not a cat, am I? hehe!"
                        scene black with dissolve
                        window hide
                        pause 1
                        show screen peakingIntro("introhimapeak")
                        show screen peaking_overlay
                        bot"O-oh?" with vpunch
                        "Move your cursor around for a better view."
                        bot"I can't see clearly, but it looks like she is just working out..."
                        bot"But, damn... She is looking kinda ho- s-sweaty..!"
                        bot"All that exercise is paying dividends on her body."
                        bot"I should stop peeking though before I get caught..."
                        "Click twice to stop peeking."
                        window hide
                        $ ui.interact()
                        hide screen peakingIntro
                        hide screen peaking_overlay
                        scene bg day with dissolve:
                            xalign 0.5 yalign 0.5
                            zoom 1
                        show boruto embarassed at mid with dissolve
                        bot"... If only she wasn't the way she is, heh!"
                        show boruto normal with dissolve
                        bot"I Better wait until she calls me in unless I want to deal with her attitude."
                        
                    "Wait":
                        bot"Better wait unless I am ready to deal with her attitude"
                bot"."
                bot".."
                bot"..."  
                show boruto surprised2 with dissolve
                "Girl" "You can come in now."
                scene black with dissolve
                pause 0.5
                play sound "audio/soun_fx/dooropen.opus" volume 0.7
                show himawari_bedroom_1:
                    blur 20
                show knock1 at halfzoom:
                    xalign 0.5 yalign 0.5
                    zoom 0.75
                    subpixel True
                    ease2 3.0 yalign 0.01
                with dissolve
                
                bo"I thought I should check up on you, heard some loud thuds from outside. Thought you... fainted... or something?"
                show knock1_1 at halfzoom with dissolve:
                    xalign 0.5 yalign 0.01
                    
                "Girl" "Thuds? F-fainted??" 
                scene black with dissolve
                show himawari_bedroom_1:
                    blur 20
                show knock2_1 at halfzoom:
                    xalign 0.5 yalign 0.1
                    zoom 0.7
                with dissolve
                "Girl" "It was just me exercising you twat." with vpunch
                show knock2_1 at halfzoom with dissolve:
                    xalign 0.5 yalign 0.75
                    zoom 0.7
                    subpixel True
                    linear 2.0 yalign 0.99
                "Girl" "Wooden floors... working out..."
                show knock2_1 at halfzoom with dissolve:
                    xalign 0.5 yalign 0.5
                    zoom 0.5
                $ renpy.sound.play("/audio/soun_fx/himawari/himascoff1.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                "Girl" "*Scoffs* Use that brain of yours and connect the dots, will you?"
                show knock2 at halfzoom with dissolve:
                    xalign 0.5 yalign 0.1
                    zoom 0.75
                
                #show bg horizontal3
                $ renpy.sound.play("/audio/soun_fx/himawari/loserlaugh.opus", channel="sfx2", loop=False, relative_volume = 0.3)
                "Girl" "Now get out before I beat your ass."
                show knock3 at halfzoom with dissolve:
                    xalign 0.5 yalign 0.01
                    zoom 0.9
                
                "Girl" "Teehee!"
                jump himaintroduction

    
    label himaintroduction:
        $ him_name = renpy.input("What is her name?", default = him_name, length=15, allow="ABCDEFGHIJKLMNOPQRSTUVWXYZSabcdefghijklmnopqrstuvwxyz ").strip() or "Himawari"
        $ him_rel = renpy.input("She is your: (Leave empty for default){p}Suggested roles: (Roommate)", default = "", length=15, allow="ABCDEFGHIJKLMNOPQRSTUVWXYZSabcdefghijklmnopqrstuvwxyz ").strip() or "Sister"
        $ him_rel_to_bo = renpy.input("You are her: (Leave empty for default) {p}Suggested roles: (Roommate)", default = "", length=15, allow="ABCDEFGHIJKLMNOPQRSTUVWXYZSabcdefghijklmnopqrstuvwxyz ").strip() or "brother"
        $ him_age = renpy.input("How old is she?:", default = 18, length=2, allow="1234567890 ").strip() or "18"
        label himaintroreplay:
        $ initialize_replay_defaults()
        scene hima intro at halfzoom:
            xalign 0.5 zoom 0.5 yalign 0.7
        show bg horizontal3
        show dreamvignette zorder 100:
            alpha 0.5
        with fade
        bot"This is my [him_rel], [him_name]. She is younger than me but not by much. It seems like I have interrupted one of her many workout routines..."
        scene hina exercise at halfzoom with dissolve 
        bot"She has inherited her mother's nature after all whom she very much looks up to."
        scene black with dissolve
        show knock2_1 at halfzoom:
            xalign 0.5 yalign 0.99
            zoom 0.7
            subpixel True
            easein 3.0 yalign 0.0
        show dreamvignette zorder 100:
            alpha 0.5
        with dissolve
        bot"...Albeit with some bonus bitchiness to go along."
        bot"Her every word towards me, a subtle proclamation of her superiority. At least in her own feeble mind."
        scene black with dissolve
        show hima intro at halfzoom:
            xalign 0.5 yalign 0.5
            zoom 0.8
            subpixel True
            easein 3.0 yalign 0.0
        show dreamvignette zorder 100:
            alpha 0.5
        with dissolve
        bot"She takes extreme pride in her image, often taking a moment to look at her own reflection, basking in her self-appointed grandeur."
        bot"I despise that about her, but I try to look past it."
        scene black with dissolve
        show hima intro3 at halfzoom:
            zoom 0.7 xalign 0.5 yalign 0.5
        show dreamvignette zorder 100:
            alpha 0.5
        with dissolve
        bot"Thankfully, she does have a few redeeming qualities..."
        show hinachunin at halfzoom with dissolve
        hide hima intro3
        bot"Recently, she has been taking her Kunoichi studies seriously looking to achieve the same rank as her [hin_rel_mother] used to hold."
        scene black with dissolve
        show hima intro3 at halfzoom:
            zoom 0.7 xalign 0.5 yalign 0.5
        show dreamvignette zorder 100:
            alpha 0.5
        with dissolve
        bot"Her determination to keep pushing her body to its limits day in and day out is..."
        show hima intro3_1 at halfzoom with dissolve:
            zoom 0.8 xalign 0.5 yalign 0.5
        bot"commendable..."
        bot"And along with her academic excellence, I have no doubt that she will eventually match [hin_rel]'s prowess, if not surpass it."
        scene black with dissolve
        show hima intro4 at halfzoom:
            zoom 0.65 xalign 0.5 yalign 1.0
            subpixel True
            easein 3 yalign 0.0
        show dreamvignette zorder 100:
            alpha 0.5
        with dissolve
        pause 1
        bot "Unlike [hin_rel] though, [him_name] will not hold back from expressing herself and can be a grade 'A' bitch at times..."
        show hima intro4_1 at halfzoom with dissolve:
            zoom 0.7 xalign 0.5 yalign 0.0
        show hima intro4_1 at halfzoom:
            subpixel True
            easein 3 zoom 0.72
        bot "She does not hesitate to remind me that she thinks of me as somewhat of a loser."
        bot "Me and her, we don't loathe each other... yet." 
        bot "We do our best to find common ground where we can."
        show hima intro2 at halfzoom with dissolve:
            zoom 0.55 xalign 0.5 yalign 1.0
            subpixel True
            easein 10.0 yalign 0.0
        bot "Regardless of her attitude, there's no denying that she has grown into a beautiful woman."
        bot "The extreme amount of work she puts in herself..."
        show hima intro2 at halfzoom with dissolve:
            zoom 0.6 xalign 0.5 yalign 0.45
        show bg horizontal3
        with dissolve
        bot "Can easily be... Observed. Especially so now that she has come of age."
        scene black with dissolve
        show hima peak2 at halfzoom:
            zoom 0.56 xalign 0.5 yalign 0.5
        show dreamvignette zorder 100:
            alpha 0.5
        with dissolve
        bot "Along with the fact that she tends to wear skimpy clothing around the house, it is making it difficult for me to not see her as a woman."
        bot "Regardless, No amount of beauty is going to counterweigh her shitty, bratty demeanor!"
        bot "I will have to find a way to improve her attitude towards me, and if I can..."
        menu hima_path:
            bot"I will make her"
            "Respect me":
                call changeRespect("Himawari", 1, "none") from _call_changeRespect_67
                bot"Respect me..."
                bot"I won't allow this brat to disrespect me at every chance she gets."
                bot"If there is no easy way, she will have to learn the hard way." 
            "Obey me":
                call changeObedience("Himawari", 1, "none") from _call_changeObedience_47
                bot"Obey me. I have had it with her shitty attitude lately. I will find a way to subjugate her, and make her do what I want!"
                bot"Perhaps I'll have her be my personal slave. Washing my clothes, making me food, or... heh! I can think of so many things!"

            "Love me":
                call changeLove("Himawari", 1, "none") from _call_changeLove_19
                bot"...L-love me. She is my [him_rel] after all and I care for her. We have our differences at the moment, but I am sure we can work those out."
                bot"I want to see her blossom into the woman I know she can be, not abrasive or hateful, but loving and caring, just like [hin_rel]."
                bot"Before we reach that level, I will have to work on earning back her good graces and trust."
        #cg
        scene black with dissolve
        show himawari_bedroom_1:
                    blur 20
        show knock2 at halfzoom:
            xalign 0.5 yalign 0.5
            zoom 0.50
        him"Pst! Stop dozing off in my room you klutz!" with vpunch
        show knock2 at halfzoom with dissolve:
            xalign 0.5 yalign 0.0
            zoom 0.6
        him"Have you confirmed my physical integrity yet, Oh my white knight in shining armor?"
        call changeRespect("Himawari", -1, "none") from _call_changeRespect_68
        him"Now kindly fuck off." with vpunch
        menu:
            him"Now kindly fuck off."
            "Alright you stuck up bitch!":
                bo"Alright you stuck up bitch!"
                show knock2_1 at halfzoom:
                    xalign 0.5 yalign 0.1
                    zoom 0.9
                $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                him"Piss off, loser!" with vpunch
                call changeRespect("Himawari", -1, "none") from _call_changeRespect_69
                scene black with vpunch
            "Okay, okay!":
                bo"Okay, okay... I am sorry!"

        scene black
        $ renpy.end_replay()



    label livingroom_aftersleep:
        scene bg day with vpunch:
            xalign 0.5 yalign 0.5
            zoom 0.69
        $ renpy.sound.play("/audio/soun_fx/doorslam.opus", channel="sfx2", loop=False, relative_volume = 0.5)
        "[him_name] slams the door after she kicks you out of her room..."
        show boruto angry with dissolve
        bot"This damn girl. She will be my demise..."
        show boruto sceeming2 with dissolve
        bot"Or I will be hers..."
        show halfblack with dissolve
        dev"You might have noticed how throughout the game, your choices might affect your relationships in different ways."
        dev"The story, dialogue and scenes available to you will vary based on your stats."
        dev"Naturally, you won't be able to experience everything in a singular playthrough."
        default showrelationships = True
        show screen topleftbuttons
        image arrowui = "gui/arrow.png"
        show arrowui:
            xalign 0.1
        dev"To check your current stats, click on the 'info' button at the top left of the screen."
        dev"Keep in mind that losing points in certain attributes is not always a bad thing."
        dev"As an example, keeping [bo_name]'s 'Hatred' stat high might unlock some options but it might also lock you out of 'Romance' options."
        dev"In that regard, if you want to experience a 'pure' playthrough with a focus on romance, you shouldn't mind losing 'Hatred' points."
        dev"You can hover over each stat to see more information about how it works."
        dev"Some interactions in repeatable events will be hidden until your corresponding stat is high enough."
        dev"Other interactions might initiate a stat check which can either be 'passed' or 'failed' depending on the corresponding stat's value at that given moment."
        dev"And finally some interactions will be hidden until multiple requirements are met. Those are known as secret scenes and will have a unique selection background when available"
        dev"Feel free to experiment and approach each situation as you see fit."
        hide arrowui
        hide halfblack with dissolve
        show boruto worried with dissolve
        bo"*Sigh*"
        show boruto normal with dissolve
        bot"[hin_rel] said she needed me for something, but I overslept..."
        bot"I better find her fast!"
        hide boruto with dissolve


        $ quest.load(boruto1)
        $ quest_hin.load(hinata1)
        $ quest_him.load(himawari1)


        $ himawaripanties = Item(name=f"Panties", info=f"A pair of already worn pink underwear belonging to {him_name}", price=0, quantity=1)
        $ himawaripantiescum = Item(name=f"Soiled Panties", info=f"A pair of cum-stained panties belonging to {him_name}", price=0, quantity=1)
        $ lockpicks = Item(name="Lockpicks", info="A pack of 3 lockpicks", price=9999, quantity=3)
        $ snacks = Item(name="Snacks", info=f"{him_name}'s favorite snacks. She would appreciate it as a gift", price=10, quantity=1)
        $ flowers = Item(name="Flowers", info="A bouquet of beautiful flowers. A nice gift for a mature lady", price=20, quantity=1)
        $ condoms = Item(name="Condoms", info="A monster condom suitable for someone's mangum dong", price=20, quantity=1)
        $ pills = Item(name="Pills", info="A bottle of prescription pills of unknown usage", price=50, quantity=99)
        $ camera = Item(name="Camera", info="A camera device used by professional photographers", price=75, quantity=1)
        $ wine = Item(name="Wine", info="A bottle of exquisite wine", price=50, quantity=40)
        $ blackdress = Item(name="Black Dress", info="An elegant black dress. Suitable for emphasizing a mature lady's curvature", price=9999, quantity=1)
        #cosplay himawari
        $ cosplayoutfitcammy = Item(name="Cammy Outfit", info="A skimpy cosplay-outfit. Suitable for someone with a smaller stature", price=9999, quantity=1)
        $ cosplayoutfitchunli = Item(name="Chunli Outfit", info="A skimpy cosplay-outfit. Suitable for someone with a smaller stature", price=9999, quantity=1)
        #cosplay hinata
        $ maidoutfit = Item(name="Maid Outfit", info="A revealing maid outfit", price=9999, quantity=1)
        $ cosplayoutfitslave = Item(name="Slave Outfit", info="A skimpy cosplay-outfit. Suitable for someone with a smaller stature", price=9999, quantity=1)

        $ swimsuit = Item(name="Swimsuit", info="A modest one-piece swimsuit. Suitable for a mature lady", price=9999, quantity=1)
        $ bikini = Item(name="Bikini", info="A skimpy bikini. Suitable for someone with a smaller stature", price=9999, quantity=1)
        $ pool = Item(name="Pool installation", info="Order a pool installation for your home", price=9999, quantity=1)


        $ inventoryShop.add_item(lockpicks, 99)
        $ inventoryShop.add_item(snacks, 99)
        $ inventoryShop.add_item(condoms, 99)
        $ inventoryShop.add_item(flowers, 99)
        $ inventoryShop.add_item(pills, 99)
        $ inventoryShop.add_item(camera, 1)
        $ inventoryShop.add_item(wine, 49)
        $ inventoryShop.add_item(blackdress, 1) 

        $ inventoryShop.add_item(cosplayoutfitcammy, 1) 
        $ inventoryShop.add_item(cosplayoutfitchunli, 1) 

        $ inventoryShop.add_item(maidoutfit, 1)
        $ inventoryShop.add_item(cosplayoutfitslave, 1)

        $ inventoryShop.add_item(swimsuit, 1) 
        $ inventoryShop.add_item(bikini, 1) 
        $ inventoryShop.add_item(pool, 1)







        jump freeroam

        

     
            


    # This ends the game.


    return



