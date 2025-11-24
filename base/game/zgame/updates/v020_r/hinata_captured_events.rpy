label hinata_captured_1:
    scene bg day:
        zoom 0.7
    show boruto worried
    with dissolve
    bot"I hope [hin_rel]'s doing alright..."
    bot"I should try sneaking in the Daimyo's plot as soon as possible!"
    hide boruto worried with dissolve
    scene black with dissolve
    "Some time earlier..."
    label hinata_captured_1_replay:
    $ initialize_replay_defaults()
    show daimyopalace bg
    show demandingmen normal badguys2:
        xzoom -1 xpos -1400
    show demandingmen:
        easein 3 xpos -700
    show shina restrained:
        xpos -1000
    show shina restrained:
        easein 3 xalign 0.2
    
    "???" "And what do we have here..."
    show daimyo normal at right:
        xalign 1.2
    with dissolve
    da "So nice of you to visit me again so soon, my lady..."
    hin"..."
    show daimyo pervert with dissolve
    da "I knew you took a liking to me the first time we saw each other! Hehehe..."
    hint"D-disgusting..."
    show daimyo normal with dissolve
    da "You see, I would very much like spending some time together, but I am quite preoccupied as you can see, so..."
    da "Three days!" with vpunch
    hin"T-three... days?"
    da "You have failed to comply with my rule, have you not?"
    hin"I-..."
    da "SILENCE!" with vpunch
    da "Three days and three nights you shall spend in my dungeons, ruminating upon your treasonous behavior!"
    da "That should give us ample time together, don't you think? For you to understand that actions have consequences, and for me to instill upon you that NO ONE, is above MY LAW!" with vpunch
    da "Toji! Dump her in the deepest cell of my dungeons! She is not to be fed, nor stained by anyone's touch other than mine!"
    to"At once, my lord!" with vpunch
    hide daimyo with dissolve
    show blackscreen with dissolve
    da"I shall discipline her personally later tonight..."
    scene daimyopalace bg
    show mp_v1_grab:
        xpos 0.30
    with dissolve
    to"Get a move on!"
    da "And remember Toji, no one is to touch the lady but me..."
    da "Lest they find their hands dismembered and fed to the dogs!" with vpunch
    hide mp_v1_grab
    show mp_v1_3:
        xpos 0.30
    with dissolve
    to"H-hai!" with vpunch
    hide mp_v1_3 with dissolve
    scene black with dissolve
    stop music fadeout 5
    $ renpy.sound.play("/audio/soun_fx/dungeon_ambient.opus", channel="ambience", loop=True, relative_volume = 1.0)
    "..."
    "Toji led [hin_name] to the Daimyo's underground dungeons, where she was to be held for the next three days."
    hint"What a foul smell..."
    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp4.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    hin"*Gasps!*" with vpunch
    $ renpy.sound.play("/audio/soun_fx/horror.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    $ renpy.sound.play("/audio/soun_fx/dungeon_ambient2.opus", channel="ambience2", loop=True, relative_volume = 1.0)
    show v20_walk_through_dungeon with dissolve:
        yalign 1.0
    pause 0.3
    show v20_walk_through_dungeon:
        subpixel True
        easein 5 yalign 0.5
    to"Keep walking!" with vpunch
    hin"B-but... There's a c-corpse!"
    to"And...?"
    scene black with vpunch
    to"I said keep walking, lest you want to join the corpses yourself..." with vpunch
    show captives 0 with dissolve:
        yalign 0.5
    show captives 0:
        subpixel True
        easein 5 yalign 1.0
    hint"..."
    "[hin_name] took hesitant glances while passing through cellars, a glimpse of what was soon to be her own experience..."
    "The Daimyo had a strange method of handling his captives..."
    "In his words...\n'There's no need to waste money on guards, or food. Toss the prisoners in a cellar, forget about them, and the problem will eventually solve itself...'"
    "'They will either die, or live long enough to conform to my rule!'"
    show captives 1_1 with dissolve:
        yalign 0.7
    show captives 1_1:
        subpixel True
        easein 5 yalign 1.0
    "Neither men, or women were exempt from his methods..."
    "And if captivity proved insufficient, the Daimyo would simply revert to other disciplinary methods of instilling his rule upon his subjects..."
    show dead_captives 1_2 with dissolve:
        yalign 0.0
    show dead_captives 1_2:
        subpixel True
        easein 7 yalign 1.0
    $ renpy.sound.play("/audio/soun_fx/dungeon_whipman2.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    "Men were mercilessly whipped and tortured, others were hanged upside down until enough blood pooled in their heads causing fatal intracranial pressure."
    "Women on the other hand..."
    $ renpy.sound.play("/audio/soun_fx/dungeon_womanscream.opus", channel="sfx1", loop=False, relative_volume = 1.6)
    scene captives 1_2 with dissolve:
        yalign 0.5
    show captives 1_2:
        subpixel True
        easein 7 yalign 1.0
    "Those deemed 'useful' would be isolated, to be used by the Daimyo's men for copulation."
    scene dead_captives 1 with dissolve:
        yalign 1.0
    show dead_captives 1:
        subpixel True
        easein 7 yalign 0.6
    "The rest would be left to rot..."
    "No one was above the Daimyo's rule."
    scene black with dissolve
    "Not even those who shared his blood..."
    "Young Girl" "You!" with vpunch
    scene captive daughter with dissolve:
        yalign 1.0
    show captive daughter:
        subpixel True
        easein 7 yalign 0.2
    "Young Girl" "Release me you bastard!" with vpunch
    to"Bwa-hahaha! You are the Daimyo's bastard offspring, are you not?" with vpunch
    hint"His own children!? What cruelty..."
    to"You aren't going anywhere little girl. You have your whore Mother to blame for your fate!"
    "Daimyo's Daughter" "RELEASE ME! I'll slit my father's throat, and then yours!" with vpunch
    to "Maybe I shall fill your womb with my offspring, just as your harlot of a mother had other men fill hers!"
    scene captive wife with dissolve:
        yalign 1.0
    show captive wife:
        subpixel True
        easein 5 yalign 0.2
    "Daimyo's Concubine" "You bastard! Touch my daughter and I shall curse you for all eternity!" with vpunch
    to "Bwa-hahaha! Shut your mouth you infidel whore! You'll both remain chained opposite of each other, watching one another rot until the day you perish!" with vpunch
    scene bg cell
    show mp_v1_3:
        xpos 0.30
    with dissolve
    to"Don't you worry, my 'lady'..."
    show mp_v1_3:
        easein 1 xpos 0.25
    pause 0.7
    to"Your stay here will be temporary, so long as you don't anger the Daimyo any further! Bwa-ahaha!"
    $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 2.0)
    hide mp_v1_3
    show hin_captured_groped_anim:
        xpos 0.25
    with dissolve
    hin"D-don't touch me! The Daimyo s-said-"
    to"Bwa-ahaha!"
    hide hin_captured_groped_anim with dissolve
    to"Shut it, bitch..."
    "I don't think you understand what the Daimyo meant..."
    scene black with vpunch
    $ renpy.sound.play("/audio/soun_fx/prison_cell.opus", channel="sfx1", loop=False, relative_volume = 1.0)
    "Toji shoved [hin_name] into her cell, chaining her to the iron clasps attached to the ceiling!"
    $ renpy.sound.play("/audio/soun_fx/chain_rattle3.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    hin"A-arh!" with vpunch
    scene v20_hin_captured 0 with dissolve:
        yalign 1.0
    show v20_hin_captured 0:
        subpixel True
        easein 5 yalign 0.1
    to"The Daimyo simply wants for you to remain... pure."
    show v20_hin_captured 0 with dissolve:
        yalign 0.6
    show v20_hin_captured:
        easein 3 yalign 1.0
    to"There's other ways to have fun with you..."
    show v20_hin_captured 0_1 with dissolve:
        easein 3 yalign 1.0
    to"Some caress here, some kissing there...\nAs long as I don't fuck your brains out!" with vpunch
    menu:
        to"Some caress here, some kissing there...\nAs long as I don't fuck your brains out!"
        "(Bite him)":
            default hinata_bite_toji = False
            $ hinata_bite_toji = True
            show v20_hin_captured 0_2 with dissolve:
                zoom 1.1 yalign 0.8
            with vpunch
            $ renpy.sound.play("/audio/soun_fx/male_groan2.opus", channel="sfx2", loop=False, relative_volume = 1.5)
            pause 0.5
            scene black with vpunch
            $ renpy.sound.play("/audio/soun_fx/clothe_tear2.opus", channel="sfx1", loop=False, relative_volume = 1.2)
            to"Arrh! You bitch!" with vpunch
            scene v20_hin_captured 1 glareblood with flash:
                yalign 0.05
            show v20_hin_captured 1 glareblood:
                easein 8 yalign 0.7
            "Still grasping [hin_name]'s clothing, Toji fell back tearing her sweater apart!"
            hin"Don't touch me! Asshole..." with vpunch
            to"You filthy WHORE!"
            to"If it weren't for his highness, I'd pin you on the wall and ravage your asshole till the sun rose up again..."
            hin"..."
            to"This won't be the last we see of each other. I swear it on my life..."




        "(Stay silent...)":
            hint "This b-bastard! Putting his dirty finger in my..."
            hint"So despicable! But I fear of what may happen if I revolt..."
            show v20_hin_captured 0_1f 1 with dissolve:
                zoom 1.05 yalign 0.6 xalign 0.5
            to"Oooh? Quite tame, aren't you? Although that glare of yours tells another story..."
            show v20_hin_captured mouthanim with dissolve
            to"I could put your pretty mouth to good use right about now..."
            hint"Stay calm..."
            to"Or maybe I should turn you around, pin you to the wall, and have my way with the rest of you!"
            hint"He must be bluffing! He knows he can't d-do that..."
            to "I could treat you nicer you know, if you were good to me. If you were..."
            to"My wife!" with vpunch
            hint"!" with vpunch
            to "Ever since the first time I saw you up close, I was struck by your beauty."
            to "Surely I could do better than your stupid husband..."

            show screen image_with_border("v20_hin_captured_pussy",0.8,0.5,0.0)
            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx2", loop=False, relative_volume = 0.8)
            # show v20_hin_captured with dissolve:
            #     xalign 1.0 yalign 1.0
            to "In every way imaginable!" with vpunch
            hide screen image_with_border
            scene black with vpunch
            hin"Don't t-touch me!"
            $ renpy.sound.play("/audio/soun_fx/clothe_tear2.opus", channel="sfx1", loop=False, relative_volume = 1.2)
            to"Bwa-ahaha! You look even better like this!" with vpunch
            scene v20_hin_captured 1 glare with flash:
                yalign 0.05
            show v20_hin_captured 1 glare:
                easein 8 yalign 1.0
            "Grasping [hin_name]'s clothing, Toji fell back tearing her sweater apart in the process!"
            to"To think you'd reject me so nonchalantly..."
            show v20_hin_captured with dissolve:
                yalign 0.3
            to "Stuck up bitch!" with vpunch
            to"If it weren't for his highness, I'd pin you on the wall and ravage your asshole till the sun rose up again..."
            hin"..."
            to"This won't be the last we see of each other. I swear it on my life..."
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/prison_cell.opus", channel="sfx1", loop=False, relative_volume = 1.0)
    "Toji shuts [hin_name]'s cell in frustration, leaving [hin_name] chained and stripped of her clothing in the Daimyo's cold underground dungeons..."
    scene v20_hin_captured 1 tired with dissolve:
        yalign 1.0
    show v20_hin_captured 1 tired:
        easein 8 yalign 0.4
    hint"Despicable bastard, him and the Daimyo both!"
    hint"This can't be right..."
    hint"I never knew that this is how the Daimyo treats his people behind closed doors. I have to do something..."
    hint"This injustice cannot continue!"
    hint"But first..."
    show v20_hin_captured 1 with dissolve
    hint"I must endure. Three days and three nights without food, without water..."
    hint"Stay calm, [hin_name]. Ignore the cold, ignore the screams..."
    scene black with dissolve
    stop ambience fadeout 3
    stop ambience2 fadeout 3
    hint"Think of your beautiful children, your loving husband, time will pass."
    $ renpy.end_replay()


    jump house

label hinata_captured_2:
    scene bg day:
        zoom 0.7
    show boruto worried
    with dissolve
    bot"It's been two days now, what the hell is going on!"
    bot"I should try sneaking in the Daimyo's estate as soon as possible!"
    hide boruto worried with dissolve
    stop music fadeout 2
    scene black with dissolve

    "Meanwhile..."
    label hinata_captured_2_replay:
    $ initialize_replay_defaults()
    $ renpy.sound.play("/audio/soun_fx/dungeon_ambient.opus", channel="ambience", loop=True, relative_volume = 1.0)
    # $ renpy.sound.play("/audio/soun_fx/horror.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    $ renpy.sound.play("/audio/soun_fx/dungeon_ambient2.opus", channel="ambience2", loop=True, relative_volume = 1.0)
    scene v20_hin_captured 2 with dissolve:
        yalign 1.0
    show v20_hin_captured 2:
        easein 8 yalign 0.1
    hint"..."
    hint"No light, no food or water... Time has lost all meaning in this darkness."
    scene black with dissolve
    show blackscreen
    show emptycell:
        yalign 1.0 alpha 0.0
    with dissolve
    show emptycell at dizzy:
        easein 5 yalign 0.0 alpha 1.0
    hint"My throat burns with thirst. I am feeling dizzier every second. What a grueling feeling..."
    "???" "My Lady..."
    hin"H-huh...?"
    hin"Who's there!?" with vpunch
    $ renpy.sound.play("/audio/soun_fx/horror.opus", channel="sfx1", loop=False, relative_volume = 0.5) 
    scene emptycell_toji1 with flash:
        yalign 1.0
    show emptycell_toji1 at brightreveal:
        easein 5 yalign 0.0
    ko "My lady, please, don't be scared..."
    hin"Y-you..."
    show v20_hin_captured 1var with dissolve:
        yalign 1.0
    show v20_hin_captured:
        easein 8 yalign 0.2
    hin "You are here to hurt me aren't you? Just like your immoral partner, or your cruel lord..."
    show v20_hin_captured 1 glare with dissolve:
        zoom 1.4 yalign 0.44 xalign 0.5
    hin "Do it, then! Get it over with!" with vpunch
    scene emptycell_toji1 with dissolve:
        yalign 0.1
    ko"I understand your mistrust my lady, but..."
    $ renpy.sound.play("/audio/soun_fx/ominous_sound.opus", channel="sfx2", loop=False, relative_volume = 0.6)
    show emptycell_toji1_1 with dissolve:
        easein 3 yalign 0.55
    ko"I don't seek to harm you. On the contrary, I'd like to help..."
    hint"W-water!?" with vpunch
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/prison_cell.opus", channel="sfx1", loop=False, relative_volume = 1.0)
    ko"Make no mistake, my allegiance still lies with the Daimyo. You have disobeyed his orders and scarred his ego and for that, you must remain his prisoner."
    ko"But beyond that, I take no pleasure in watching you suffer. Which is why..."
    show v20_hin_captured 1_5 with dissolve:
        zoom 3.5 yalign 1.0 xalign 0.4
    ko"I sneaked this in for you."
    scene v20_hin_captured 1_1 with dissolve:
        yalign 0.9
    show v20_hin_captured 1_1:
        subpixel True
        easein 5 yalign 0.4
    hin"How do I know... that I can trust you?"
    ko"I can't answer that for you my lady, but you should know that I am taking a monumental risk in doing this."
    ko"If the Daimyo ever finds out, I could very well be executed for treason."
    hint"He is not wrong..."
    ko"I shall leave you to ponder upon your thoughts, but I will be returning later tonight to remove the evidence."
    hin"..."
    ko"I trust that this will stay between us, my lady."
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/prison_cell.opus", channel="sfx1", loop=False, relative_volume = 1.0)
    ko"Farewell for now."
    hin"..."
    hin"W-wait!" with vpunch
    show emptycell_toji1 with dissolve:
        yalign 1.0
    show emptycell_toji1:
        easein 3 yalign 0.6
    ko"Is something wrong, my lady?"
    hin"The bowl... I can't r-reach it!"
    $ renpy.sound.play("/audio/soun_fx/horror.opus", channel="sfx1", loop=False, relative_volume = 0.5)
    show emptycell_toji1_2 with dissolve:
        yalign 0.5
    "[hin_name] missed Koji's devious smirk flickering through the darkness."
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/prison_cell.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    ko"How careless of me. Your chains are holding you upright after all..."
    show v20_hin_captured 1_2 with dissolve:
        yalign 0.8
    show v20_hin_captured 1_2 with dissolve:
        subpixel True
        easein 5 yalign 0.5
    ko"My apologies. Allow me to loosen your chains..."
    hin"T-thank you..."
    $ renpy.sound.play("/audio/soun_fx/chain_rattle2.opus", channel="sfx1", loop=False, relative_volume = 1.0)
    scene v20_hin_captured 1_3 with dissolve:
        yalign 1.0
    ko"There's no need for that. I am simply doing the right thing."
    $ renpy.sound.play("/audio/soun_fx/chain_rattle3.opus", channel="sfx1", loop=False, relative_volume = 1.0)
    scene v20_hin_captured 1_3waist with dissolve
    ko"Although these old chains are rusty. Just a bit higher..."
    hint"...Is he truly trying to help?" with vpunch
    $ renpy.sound.play("/audio/soun_fx/chain_rattle2.opus", channel="sfx1", loop=False, relative_volume = 1.0)
    scene v20_hin_captured 1_3ass with dissolve
    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp3.opus", channel="sfx2", loop=False, relative_volume = 0.9)
    ko"Almost got it!" with vpunch
    show screen image_with_border("v20_hin_captured 1_3_annoyed",0.4,0.0,0.0) with dissolve
    hin"W-what are you-" with vpunch
    scene v20_hin_captured 1_3waist with dissolve
    ko"That should do it!" with vpunch
    hide screen image_with_border
    scene black
    with dissolve
    $ renpy.sound.play("/audio/soun_fx/prison_cell.opus", channel="sfx1", loop=False, relative_volume = 1.0)
    ko"I shall leave you with that, my lady."
    "Koji took his leave, after leaving [hin_name] with the lingering stench of his touch, and the drugged bowl of water beckoning at her."
    $ renpy.sound.play("/audio/soun_fx/intro/bodythud.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    "*Body thud*!\n[hin_name] dropped to her knees as soon as her chains were loosened." with vpunch
    show v20_hin_captured 1_4bowl:
        yalign 1.0
    show v20_hin_captured at dizzyflashshort:
        subpixel True
        easein 5 yalign 0.3
    hint"D-damn it! My legs are giving out from beneath me. My head is spinning too..."
    call showscrollingimage from _call_showscrollingimage_221
    show screen parallax1280("v20_hin_captured 1_4bowl",1,1.0) with dissolve
    "After almost two days of being forced upright, [hin_name]'s exhausted body was giving out. Combined with dehydration, the bowl before her seemed like a cruel promise of relief..."
    "Yet her instincts whispered that something was wrong..."
    call hidescrollingimage from _call_hidescrollingimage_188
    show screen parallax1280("v20_hin_captured 1_5",1,1.0) with dissolve
    call showscrollingimage from _call_showscrollingimage_222
    "But in her drained, fragile state, she succumbed to the temptation..."
    hin"Just... a few sips. Enough to quench my thirst."
    scene black with dissolve
    call hidescrollingimage from _call_hidescrollingimage_189

    stop ambience fadeout 3
    stop ambience2 fadeout 3
    "Some time passes..."
    $ renpy.end_replay()
    jump house

label hinata_captured_3:
    scene bg day:
        zoom 0.7
    show boruto worried
    with dissolve
    bot"Fuck. I am getting a bad feeling about [hin_rel]..."
    bot"I should try sneaking in the Daimyo's estate as soon as possible!"
    hide boruto worried with dissolve
    stop music fadeout 2
    scene black with dissolve

    "Meanwhile..."
    label hinata_captured_3_replay:
    $ initialize_replay_defaults()
    $ renpy.sound.play("/audio/soun_fx/dungeon_ambient.opus", channel="ambience", loop=True, relative_volume = 1.0)
    # $ renpy.sound.play("/audio/soun_fx/horror.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    $ renpy.sound.play("/audio/soun_fx/dungeon_ambient2.opus", channel="ambience2", loop=True, relative_volume = 1.0)
    scene v20_daimyoend_0 with dissolve:
        yalign 1.0
    show v20_daimyoend_0:
        easein 8 yalign 0.35
    hin"I can't... t-take it a-anymore!"
    hin"P-please... s-someone..."
    $ renpy.sound.play("/audio/soun_fx/intro/evilmenlaugh.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    scene black with dissolve
    show blackscreen
    show emptycell:
        yalign 1.0 alpha 0.0
    with dissolve
    show emptycell at dizzy:
        easein 3 yalign 0.0 alpha 1.0
    hint"My throat burns with thirst. I am feeling dizzier every second. What a grueling feeling..."
    show emptycell_daimyo with dissolve:
        alpha 0.0
    show emptycell_daimyo at brightreveal:
        subpixel True
        easein 5 yalign 0.0 alpha 1.0
    "???" "*evil chuckle*"
    "???" "Good, good..."
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/prison_cell.opus", channel="sfx1", loop=False, relative_volume = 1.0)
    "..."
    show v20_daimyoend_00_0 with dissolve:
        yalign 0.3
    show v20_daimyoend_00_0:
        easein 44 yalign 0.7
    hin"D-don't... look!"
    show daimyo_whip2 with dissolve:
        yalign 1.0
    show daimyo_whip2:
        easein 4 yalign 0.5
    da"Like a docile dog..."
    show daimyo_whip2 with dissolve:
        zoom 1.1 xalign 0.0 yalign 1.0
    da"I suppose I won't be needing this then!"
    $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 1.6)
    scene daimyo_naked1 with fade:
        yalign 0.0
    show daimyo_naked1:
        easein 4 yalign 1.0
    hin"W-wait... you are..."
    call showscrollingimage from _call_showscrollingimage_223
    show screen parallax1280("v20_daimyoend_0",1,0.6) with dissolve
    hin"Y-you said... th-three days..."
    hin"Are you here... to free m-me?"
    show screen parallax1280("blackscreen",1,0.6) with dissolve
    da"Indeed! How perceptive of you..."
    $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 1.6)
    show screen parallax1280("v20_daimyoend_00_1",1,0.6) with dissolve
    da"First, let's free you of your clothes!"
    scene black
    call hidescrollingimage from _call_hidescrollingimage_190
    scene v20_daimyoend_0drug1 with dissolve:
        yalign 1.0
    show v20_daimyoend_0drug1:
        easein 5 yalign 0.0
    hin"Why am I..."
    hin"My pu-pussy... it's burning up!"
    show v20_daimyoend_0drug1 with dissolve:
        yalign 1.0
    da"It will feel better momentarily..."
    $ renpy.sound.play("/audio/soun_fx/phial_drop.opus", channel="sfx2", loop=False, relative_volume = 2.5)
    show v20_daimyoend_0drug1_1 with dissolve:
        yalign 1.0
    hin"H-huh...?" with vpunch
    da"Just a sip of my medicine... and you'll be be 'free' of all your pain and suffering!"
    call showscrollingimage from _call_showscrollingimage_224
    show screen parallax1280("v20_daimyoend_0drug1_1",1,0.6) with dissolve
    hin"Th...thank y-you..."
    show screen parallax1280("blackscreen",1,0.6) with dissolve
    da"Aaah you are too kind! Here, let me help..."
    show screen parallax1280("v20_daimyoend_0drug1_3",1,0.6) with dissolve
    da"It's time for you to transcend..."
    show screen parallax1280("blackscreen",1,0.6) with dissolve
    da"Say 'Aaaah'!"
    $ renpy.sound.play("/audio/soun_fx/longpiss.opus", channel="sfx3", relative_volume = 1.5)
    hide screen parallax1280
    show screen parallax1280("v20_daimyoend_0drug1_2",1,0.0)
    with dissolve
    stop sfx3 fadeout 4
    da"If I knew the drug was as effective as it is, then I would have moved my plans forward much faster."
    hide screen parallax1280
    show screen parallax1280("v20_daimyoend_0drug1_3",1,0.6)
    with dissolve
    $ renpy.sound.play("/audio/soun_fx/phial_drop.opus", channel="sfx2", loop=False, relative_volume = 2.5)
    hin"D...drug?"
    da"That little phial you just consumed..."
    hide screen parallax1280
    show screen parallax1280("v20_daimyoend_0drug1_3",1,0.0)
    with dissolve
    show screen parallax1280("v20_daimyoend_0drug1_4a",1,0.6) with dissolve
    da"It's the world's most powerful aphrodisiac!"
    da"Strong enough to bring down the inhibitions even of a bitch like yourself!" with vpunch
    da"Soon enough, all you Konoha women will grow dependent on it, to serve as cattle for my allies!"
    da"But you specifically..."
    scene black
    call hidescrollingimage from _call_hidescrollingimage_191
    scene v20_daimyoend_0drug1_4a with dissolve:
        zoom 1.1 xalign 0.5 yalign 0.0
    da"You I think I'll keep for myself!" with vpunch
    scene v20_daimyoend_0drug1_4 with dissolve:
        zoom 1.15 xalign 0.5 yalign 0.0
    da"Let me see your mouth! Did you drink it all?" with vpunch
    hin"Y..yeshh... Aaah..."
    scene black with vpunch
    da"BWA-HA-HAHAHAHA!"
    scene v20_daimyoend_0drug1 with dissolve:
        yalign 1.0
    show v20_daimyoend_0drug1:
        easein 5 yalign 0.1
    da"I'll cut you a deal then..." with vpunch
    da"I'll make sure that burning itch you are feeling is gone, but in exchange..."
    scene black with dissolve
    da"You'll have to take care of my own burning need..."
    da"Do we have an agreemen-"
    call showscrollingimage from _call_showscrollingimage_225
    show screen parallax1280("v20_daimyoend_0lick1",1,0.6) with dissolve
    hin"Pl... please!" with vpunch
    da"You Insatiable whore! Didn't even let me finish my proposal..."
    da"No matter. It pleases me to see your once defiant self now beneath my cock,  caressing my sack no less!"
    da"How about you taste my nuts instead!"
    show screen parallax1280("v20_daimyoend_0lick2",1,0.6) with dissolve
    $ renpy.sound.play("/audio/soun_fx/lickpenis1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    hin"*licking*"
    da"Now that's what I call servicing your lord!" with vpunch
    da"If only you were cooperative beforehand, then maybe you wouldn't have to..."
    show screen parallax1280("v20_daimyoend_0lick3",1,0.6) with dissolve
    $ renpy.sound.play("/audio/soun_fx/gags/SDTGag2.opus", channel="sfx2", loop=False, relative_volume = 1.2)
    da"...Choke on my cock!" with vpunch
    hin"*gag*!" with vpunch
    da"Ah... who am I kidding!"
    da"To tell you the truth..."
    show screen parallax1280("v20_daimyoend_0lick4",1,0.6) with dissolve
    $ renpy.sound.play("/audio/soun_fx/gags/SDTGag1.opus", channel="sfx2", loop=False, relative_volume = 1.2)
    hin"*gag*!" with vpunch
    da"I have always had my sights on you, and your family!" with vpunch
    $ renpy.sound.play("/audio/soun_fx/various_sex/deeptroat_forced1.opus",loop=True, channel="sfx2", relative_volume = 0.8)
    show screen parallax1280("v20_hin_captured daimyobj",1.0,0.6,transformeffect=custom_ypunch_repeat(timer=1.6)) with dissolve
    da"After all, there's nothing more satisfying than debasing entitled human trash like yourself!" with vpunch
    da"From now on, every time you open your whore mouth to oppose me, I'll make sure I'll be there to stuff it shut with my cock!"
    $ renpy.sound.play("/audio/soun_fx/various_sex/deepthroat_gluck.opus",loop=True, channel="sfx2", relative_volume = 1.0)
    show screen parallax1280("v20_hin_captured daimyobj_fast",1.0,0.6,transformeffect=custom_ypunch_repeat(timer=1)) with dissolve
    da"Come on, you desecrated bitch! Drain my fucking balls!" with vpunch
    da"Dr-draaain them!" with flash
    scene black
    call hidescrollingimage from _call_hidescrollingimage_192
    stop sfx2 fadeout 1
    $ renpy.sound.play("/audio/soun_fx/cum5.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    show v20_daimyoend_0lick4cum with flash:
        yalign 0.3
    da"Aar-agh! You aren't going anywhere!" with vpunch
    $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    show screen parallax1280("v20_daimyoend_0endstopmp1",1,0.6) with longerflash
    call showscrollingimage from _call_showscrollingimage_226
    da"Swallow it all, bitch!" with vpunch
    scene black
    call hidescrollingimage from _call_hidescrollingimage_193
    $ renpy.sound.play("/audio/soun_fx/intro/bodythud.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    da"*Groans* Ahhh..." with vpunch
    show screen parallax1280("v20_daimyoend_0end2_3",1,0.6) with longerflash
    call showscrollingimage from _call_showscrollingimage_227
    hin"*Heavy breathing*..."
    da"Oi... you still alive?"
    da"*Sigh...* If I am to keep you around, you are going to have to start being useful..."
    da"How about you lick my foot clean for starters!"
    show screen parallax1280("v20_daimyoend_0end2_1",1,0.6) with dissolve
    hin"A-ah..."
    da"I'll have to figure out what to do with your cursed offspring too..."
    show screen parallax1280("v20_daimyoend_0end2_2",1,0.6) with dissolve
    da"The little girl... [him_name], was it? I may have a plan for her..."
    da"The bastard boy on the other hand, I may just have to get rid of that one!"
    da"But not before I have him watch his [hin_rel_mother] getting used like the whore she is!"
    scene black
    show v20_daimyoend_0end2_2pee:
        yalign 0.0
    call hidescrollingimage from _call_hidescrollingimage_194
    $ renpy.sound.play("/audio/soun_fx/longpiss.opus", channel="sfx3", loop=True, relative_volume = 0.8)
    show v20_daimyoend_0end2_2pee:
        easein 7 yalign 1.0 alpha 0.0
    da"Ahhh... What a relief!"
    stop sfx3 fadeout 5
    da"I hope you are ready for what's to come. The night is still young..."
    da"Hee-he-hee..."
    default hin_captured_gameover = False
    $ hin_captured_gameover = True
    stop ambience fadeout 3
    stop ambience2 fadeout 3
    $ renpy.end_replay()
    jump house



label hinata_captured_midnight1:
    stop music fadeout 2
    "Meanwhile..."
    label hinata_captured_midnight1_replay:
    $ initialize_replay_defaults()
    $ renpy.sound.play("/audio/soun_fx/dungeon_ambient.opus", channel="ambience", loop=True, relative_volume = 1.0)
    # $ renpy.sound.play("/audio/soun_fx/horror.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    $ renpy.sound.play("/audio/soun_fx/dungeon_ambient2.opus", channel="ambience2", loop=True, relative_volume = 1.0)
    scene v20_hin_captured 2 with dissolve:
        yalign 1.0
    show v20_hin_captured 2:
        easein 8 yalign 0.1
    hint"It's impossible to rest..."
    $ renpy.sound.play("/audio/soun_fx/dungeon_womanscream.opus", channel="sfx2", loop=False, relative_volume = 2.0)
    "The wailing screams of women echoed through the dungeons, even during the darkest hours."
    hint"Those women... It cannot be!"
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/sexslaps1.opus", channel="sfx3", loop=True, relative_volume = 0.6,fadein=1)
    hint"Are they being..."
    $ renpy.sound.play("/audio/soun_fx/sexslaps1.opus", channel="sfx3", loop=True, relative_volume = 0.8,fadein=1)
    $ renpy.sound.play("/audio/soun_fx/spank5.opus", channel="sfx2", relative_volume = 0.8)
    scene dungeon_victim 2 with flash:
        yalign 1.0
    show dungeon_victim 2:
        easein 8 yalign 0.3
    "Guard" "Oi! Get up, bitch! We ain't done with you yet..." with vpunch
    "Violent Guard" "Move over! It's my turn next." with vpunch
    scene black with dissolve
    "A violent guard seized the captive girl's hair, yanking her head toward his groin..."
    $ renpy.sound.play("/audio/soun_fx/spank6.opus", channel="sfx2", relative_volume = 1.2)
    $ renpy.sound.play("/audio/soun_fx/various_sex/deeptroat_forced2.opus",loop=True, channel="sfx2", relative_volume = 0.8)

    scene dungeon_victim 2_1 with flash:
        yalign 1.0 xalign 0.5 zoom 1.02
    show dungeon_victim 2_1 at custom_ypunch_repeat:
        easein 8 yalign 0.5
    "Violent Guard" "Nothing like a young cock-sleeve to provide some relief after a hard day's work!" with vpunch
    "Violent Guard" "Come on, take all of it! Put that mouth to use..." with vpunch
    "Guard" "Don't go breaking her yet, fool!" with vpunch
    stop sfx2 fadeout 2
    stop sfx3 fadeout 2
    scene black with dissolve
    "The Daimyo's men would take turns defiling the captive women."
    $ renpy.sound.play("/audio/soun_fx/various_sex/spitroast_repeat.opus",loop=True, channel="sfx2", relative_volume = 0.8)
    "Even commoners that earned the Daimyo's favor would be allowed to copulate with the 'cheapest' items in captivity."
    scene dungeon_victim 1 with dissolve:
        yalign 1.0 zoom 1.0 xalign 0.5
    show dungeon_victim 1:
        easein 8 yalign 0.5
    "Old Commoner" "To think that commoners like us would be given the chance to taste young pussy..."
    "Old Commoner" "The Daimyo's generosity knows no bounds!"
    scene black with dissolve
    stop sfx3 fadeout 2
    stop sfx2 fadeout 2
    "The men closest to the Daimyo were given enjoyed unrestricted access the most valuable items in captivity..."
    "Guard" "I can't believe we are shagging the Daimyo's own daughter!" with vpunch
    $ renpy.sound.play("/audio/soun_fx/spank6.opus", channel="sfx2", relative_volume = 1.2)
    $ renpy.sound.play("/audio/soun_fx/various_sex/mature_sexslaps1.opus",loop=True, channel="sfx3", relative_volume = 0.8)
    scene daimyo_daughter 1_0 with flash:
        yalign 1.0 zoom 1.0 xalign 0.5 xzoom -1
    show daimyo_daughter 1_0:
        easein 8 yalign 0.1
    "Guard" "Thrusting into royalty feels like sweet revenge..."
    $ renpy.sound.play("/audio/soun_fx/various_sex/deeptroat_forced1.opus",loop=True, channel="sfx2", relative_volume = 0.9)
    scene daimyo_daughter 1_2 with flash:
        yalign 1.0 zoom 1.02 xalign 0.5
    show daimyo_daughter 1_2 at custom_ypunch_repeat:
        easein 8 yalign 0.4
    $ renpy.sound.play("/audio/soun_fx/spank6.opus", channel="sfx1", relative_volume = 1.2)
    "Guard" "...Or should I say, former royalty! Come on you little bitch, move your hips!" with flash
    "Daimyo's Daughter" "*Gargling, choking gasps*"
    "Guard" "Gag on it, you filthy wretch!" with vpunch
    "Guard" "I still see you sneering at me, just like how I remember you strutting past my post at your chambers, so high and mighty..."
    "Guard" "You probably thought that you would grow up being a princess, did you not...?"
    "Guard" "But look at you now. Just another whore to drain our balls!" with flash
    $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx1", loop=False, relative_volume = 0.5)
    stop sfx3 fadeout 2
    stop sfx2 fadeout 1
    scene daimyo_daughter 1_3 with longerflash:
        yalign 0.5 zoom 1.0 xalign 0.5
    show daimyo_daughter 1_3:
        easein 5 yalign 0.1
    $ renpy.sound.play("/audio/soun_fx/spank6.opus", channel="sfx1", relative_volume = 1.2)
    "Daimyo's former Concubine" "Let go of h-her, bastards!" with vpunch
    "Guard" "You look better drenched in filth, though your whore mother begs to differ..."
    scene black with dissolve
    "Guard" "No matter. You'll both serve us all the same!"
    $ renpy.sound.play("/audio/soun_fx/various_sex/angry_sex1.opus",loop=True, channel="sfx3", relative_volume = 0.8)
    scene daimyo_daughter 1_4 with dissolve:
        yalign 0.0 zoom 1.0 xalign 0.5
    show daimyo_daughter 1_4 at custom_vpunch_repeat:
        subpixel True
        easein 8 yalign 1.0
    "Guard" "Damn right they will!"
    "Daimyo's Former Concubine" "Argh! *Pained groans*... I'll slaughter you!" with vpunch
    "Guard" "You dumb whores never learn!"
    "Guard" "The moment you lost  the Daimyo's favor, is the moment you and your brat became ours to ruin. Your fates are sealed!"
    "Guard" "If only you thought twice before sucking on another man's cock. Maybe you wouldn't be sitting on mine then! Hahaha!"
    "Guard" "Now shut the fuck up while I carve your royal holes to the shape of my cock!" with vpunch
    $ renpy.sound.play("/audio/soun_fx/cum11.opus", channel="sfx1", loop=False, relative_volume = 0.5)
    scene black
    show daimyo_daughter 1_5 with flash:
        yalign 1.0 zoom 1.05 xalign 0.5
    show daimyo_daughter:
        easein 6 zoom 1.2 alpha 0.0
    stop sfx3 fadeout 3
    "..."
    scene v20_hin_captured 2 with dissolve:
        yalign 1.0
    show v20_hin_captured 2:
        easein 8 yalign 0.1
    $ renpy.sound.play("/audio/soun_fx/dungeon_womanscream.opus", channel="sfx1", loop=False, relative_volume = 1.6)
    hint"All those screams... W-what the hell is going on beyond these walls!"
    hint"Darn it! I can't even tell how much time has passed..."
    hint"And I am already feeling dehydrated..."
    scene black with dissolve
    show blackscreen
    show emptycell:
        yalign 1.0 alpha 0.0
    with dissolve
    show emptycell at dizzy:
        easein 5 yalign 0.0 alpha 1.0
    hint"I have to endure! Just a few more hours..."
    $ renpy.sound.play("/audio/soun_fx/intro/evilmenlaugh.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    "???" "*Sinister chuckle*"
    hint"...Who's that?"
    hin"Is... someone there!?"
    $ renpy.sound.play("/audio/soun_fx/horror.opus", channel="sfx1", loop=False, relative_volume = 0.5) 
    scene emptycell_daimyo with flash:
        yalign 1.0
    show emptycell_daimyo at brightreveal:
        easein 5 yalign 0.0
    "???" "There she is..."
    da "The 'Lady' of the leaf... Stripped bare in all her tarnished glory."
    show emptycell_daimyo with dissolve:
        yalign 1.0
    da "That makes two of us! Hehe... *Creepy laughter*"
    show v20_hin_captured 1 glare with dissolve:
        yalign 1.0
    show v20_hin_captured 1 glare:
        easein 4 yalign 0.4
    hin"Y-you... What do you want from me?"
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/prison_cell.opus", channel="sfx1", loop=False, relative_volume = 1.0)
    da"What I want from you, you ask..."
    show daimyo_whip1 with dissolve:
        yalign 1.0
    show daimyo_whip1:
        subpixel True
        easein 5 yalign 0.3
    da"That should be painfully clear, my lady..."
    "The Daimyo opened [hin_name]'s cell and slowly walked towards her, stretching the top end of a whip he carried with him."
    scene black
    show daimyo_whipping0 with dissolve
    show daimyo_whipping0:
        easein 3 yalign 0.0
    hint"N-no way..."
    hin"Y-you can't do that!" with vpunch
    da "There it is again... That wretched tone in your voice."
    da "Presuming to dictate what I can, or cannot do!"
    $ renpy.sound.play("/audio/soun_fx/whipping1.opus", channel="sfx1", loop=False, relative_volume = 1.0)
    show daimyo_whip2 with flash
    da "Such insolence!"
    scene black with dissolve
    "The Daimyo cracked his whip on the floor, before he started menacingly circling around [hin_name]..."
    show daimyo_whipping0 with dissolve
    show daimyo_whipping0:
        easein 3 yalign 0.0
    da"It seems to me, you cling onto this idea of yours, that somehow your marital status makes you exempt from obeying my rule."
    da "Tell me, my lady... Do you believe yourself above your ruler's command?"
    hint"B-bastard..."
    hin"..."
    $ renpy.sound.play("/audio/soun_fx/whipping2.opus", channel="sfx1", loop=False, relative_volume = 1.0)
    da"ANSWER ME!" with flash
    da "Do you think your self above my rule? Yes, or no..."
    hin"I..."
    hin"...do not."
    da"Excellent! Now before we proceed..."
    show daimyo_whipping1 with dissolve:
        zoom 0.7 xalign 0.5
    da"I gave very explicit orders for you to remain... untouched."
    show daimyo_whipping1 at smallshake
    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp3.opus", channel="sfx2", loop=False, relative_volume = 0.9)
    "The Daimyo run his fingers across [hin_name]'s bare back."
    da "Pray tell my lady, who's responsible for this shameful state of yours?"
    hin"Y-your men... the larger one, he tried to-"
    da "Toji! Strong as an ox, dumb as a rock that one.\nFear not, my lady..."
    da "Most men see the Hokage's wife as a prize to claim. But I..."
    show daimyo_whipping1_1 with dissolve:
        zoom 0.7 xalign 0.5
    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp1.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    da "I see you for what you really are!" with vpunch
    hin"*Gasp!*"
    $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 2.0)
    scene black
    show v20_hin_captured stomachanim:
        zoom 0.73 xalign 0.5 yalign 0.05
    with dissolve
    da "Old, used and spent! A faded hag past her prime, with a womb stretched by two births. I have no desire for such a creature..."
    $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 2.0)
    da "This sagging flab of flesh around your stomach fills me with disgust!"
    hin"S-stop it!" with vpunch
    da "I prefer my women young, fresh and vibrant..."
    scene black
    show daimyo_whipping2:
        zoom 0.7 xalign 0.5
    with dissolve
    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp4.opus", channel="sfx2", loop=False, relative_volume = 0.7)
    da "And lush where it matters most!" with vpunch
    show daimyo_whipping2_1 with dissolve:
        zoom 0.7 xalign 0.5
    hin"Y-you can't do that!" with vpunch
    da "I could do that and far worse, my lady..."
    show daimyo_whipping3_1 with dissolve:
        zoom 1.4 yalign 0.0 xalign 0.5
    show daimyo_whipping3_1:
        easein 2 yalign 0.7
    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx2", loop=False, relative_volume = 0.7)
    da"But...!"
    hin"*Gasps!"
    scene black with vpunch
    $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 1.6)
    da"It's not your body I am after..."
    "The Daimyo pulled [hin_name]'s pants down and shoved her against a cellar's wall."
    show daimyo_whipping start0 with dissolve:
        yalign 1.0
    show daimyo_whipping:
        subpixel True
        easein 5 yalign 0.0
    da"It's your dignity that I want to see stripped away from you!" with vpunch
    hin"Y-you-"
    da"SILENCE! You miserable wretch!" with vpunch
    da "Never in my life have I met one so brazenly disrespectful..."
    da"That despicable look on your face, that defiant glare, I know exactly what you are thinking..."
    da"'He can't touch me! I am the Hokage's wife...'"
    da"'He won't get away with this!'"
    da"When instead, you should have been down on your knees, groveling and begging for mercy!"
    da "Bah! You make my blood boil!" with vpunch
    da "Yet I am a man of honor, a benevolent and merciful lord..."
    da "Unable to meet or obey even the simplest of orders or demands, I should have had you and your family executed for your treasonous display of disrespect!"
    da "Instead, I'll let you decide your own fate..."
    scene black with vpunch
    da "Turn around!" with vpunch
    "[hin_name] knew what was coming. Knowing full well she was in no position to revolt, she reluctantly faced the wall..."
    show daimyo_whipping start1 with dissolve:
        yalign 1.0
    da "A simple trial, my lady!\nTen lashes you shall endure..." with vpunch
    show daimyo_whipping:
        subpixel True
        easein 5 yalign 0.0
    da "For every time you squeal, or speak, you shall pay a cardinal price!"
    da "Endure in silence, and I shall absolve you of any further punishment. A symbol of my respect for your strong will."
    da "Face away if you understand the terms!"
    hint"What a m-monster. To think this is the man responsible for our people..."
    show daimyo_whipping start1_1 with dissolve:
        yalign 0.0
    da"Splendid!" with vpunch
    show daimyo_whipping start2 with dissolve:
        yalign 0.0
    show daimyo_whipping:
        subpixel True
        easein 5 yalign 1.0
    hint"I won't let him break me down!"
    da"Now I wonder, do I lash your back..."
    show daimyo_whipping with dissolve:
        yalign 1.0
    da"...or your bare ass!" with vpunch
    $ renpy.sound.play("/audio/soun_fx/whipping1.opus", channel="sfx1", loop=False, relative_volume = 1.0)
    show whipping_hands with flash
    hide whipping_hands
    show daimyo_whipping start2 a
    with dissolve
    hin"...!" with vpunch
    hint"I must endure!"
    da"That's one!" with vpunch
    da"No squealing yet, eh? I expected as much..."
    show daimyo_whipping:
        easein 2 yalign 0.5
    da "The proud heiress of the Hyuuga bloodline won't succumb as easily..."
    da "Let alone the Hokage's wife! But can you withstand this!?" with vpunch
    $ renpy.sound.play("/audio/soun_fx/whipping_repeat.opus", channel="sfx1", loop=False, relative_volume = 1.0)
    show whipping_hands with flash
    hide whipping_hands
    show daimyo_whipping start2 b
    with flash
    da"YARGH!" with vpunch
    show daimyo_whipping:
        easein 3 yalign 1.0
    hint"S-stay... strong!" with vpunch
    da"Still holding on I see. Admirable..."
    da"In that case, I'll make sure I draw blood with this next one!" with vpunch
    $ renpy.sound.play("/audio/soun_fx/whipping2.opus", channel="sfx1", loop=False, relative_volume = 1.0)
    show whipping_hands with flash
    hide whipping_hands
    show daimyo_whipping start2 c
    $ renpy.sound.play("/audio/soun_fx/whipping3.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    with flash
    da"TAKE THAT! INSOLENT WORM!" with vpunch
    hin"Ugh! *Silent grunt*" with vpunch
    da"Did I hear a grunt escape you...?"
    show daimyo_whipping with dissolve:
        zoom 1.2 xalign 0.5 yalign 1.0
    da"Must have felt that one scorch your flesh!"
    hint"B-bastard! You'll never see me broken!"
    show daimyo_whipping with dissolve:
        easein 2 zoom 1.0 xalign 0.5 yalign 0.5
    da"No matter. I will make sure you let out a cry next..."
    $ renpy.sound.play("/audio/soun_fx/whipping4.opus", channel="sfx1", loop=False, relative_volume = 1.0)
    show whipping_hands with flash
    hide whipping_hands
    show daimyo_whipping start2 d
    $ renpy.sound.play("/audio/soun_fx/whipping1.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    with flash
    da"Take this, and that!" with vpunch
    hin"...!" with vpunch
    hint"It hurts so m-much but..."
    hint"Just one m-more left-"
    show daimyo_whipping:
        subpixel True
        easein 10 zoom 0.9 xalign 0.5 yalign 1.0
    $ renpy.sound.play("/audio/soun_fx/whipping_repeat.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    show whipping_hands with flash
    hide whipping_hands
    show daimyo_whipping start2 d
    with flash
    pause 0.2
    $ renpy.sound.play("/audio/soun_fx/whipping_repeat.opus", channel="sfx1", loop=False, relative_volume = 1.0)
    show whipping_hands with flash
    hide whipping_hands
    show daimyo_whipping start2 e
    with flash
    da"Damn you... SCREAM!" with vpunch
    $ renpy.sound.play("/audio/soun_fx/whipping1.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    show whipping_hands with flash
    hide whipping_hands
    show daimyo_whipping start2 e
    with dissolve
    hin"...!!!" with vpunch
    da"Let me hear your cries of anguish!"
    hint"N-never...!" with vpunch
    da"Wretched... bitch! *Tired Breathing*" with vpunch
    da"Coincidently... *Panting* It seems I have lost count of your lashings! Too bad the rules prohibit you speaking..." with vpunch
    hint"N-no... That's not fair!"
    da"To make absolutely certain my conditions are met..."
    $ renpy.sound.play("/audio/soun_fx/whipping_repeat.opus", channel="sfx1", loop=True, relative_volume = 1.0)
    scene black with flash
    da"I'll have to administer a few extra lashes!" with vpunch
    da"Hyaa!" with flash
    da"Come on, scream already!" with flash
    da"Hyaa, Yar!" with flash
    da"Cry out for me, you stubborn wretch!" with flash
    hint"Endure... I must endure!" with vpunch
    stop sfx1 fadeout 5
    "The Daimyo, reveling in his own cruelty, broke his rules and lashed [hin_name] for what felt like an eternity..."
    "."
    ".."
    "..."
    da"*Exhausted panting*..."
    da"...Not a single whimper! Damned woman..."
    show whipend 1 with dissolve:
        yalign 0.0
    show whipend 1:
        easein 3 yalign 1.0
    da"Do not think for a moment... *Panting*"
    da"...That this defiance spares you my wrath!"
    da"You'll still serve your three day sentence!" with vpunch
    show whipend 1_1 with dissolve:
        zoom 1.2 yalign 1.0 xalign 0.5
    $ renpy.sound.play("/audio/soun_fx/spank4.opus", channel="sfx2", loop=False, relative_volume = 0.6)
    da"All you earned is your flesh staying 'mostly' untouched. Consider it my mercy..." with vpunch
    hin"You..."
    "[hin_name] finally breaks her silence. Her voice trembling with her own wrath..."
    show whipend 1_1 with dissolve:
        easein 1 zoom 1.4 yalign 0.0
    $ renpy.sound.play("/audio/soun_fx/eye1.opus", channel="sfx2", loop=False, relative_volume = 0.6)
    hin"Can't even honor your own rules, yet you demand your people to?\nDo NOT forego of your promise, or you are no lord at all!" with flash
    scene black with vpunch
    da"You insolent woman! I am honor incarnate!"
    show daimyo_whip2 with dissolve:
        yalign 1.0
    show daimyo_whip2:
        subpixel True
        easein 4 yalign 0.5
    da"I shall keep my word, but be warned..."
    da"Do not insinuate, or dare insult me again, for it shall be your last..."
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/prison_cell.opus", channel="sfx1", loop=False, relative_volume = 1.0)
    da"Until next time, 'Lady' [hin_name]..."
    "The Daimyo slammed the cell gate shut, leaving [hin_name] untouched, her unyielding spirit stinging his pride."
    $ renpy.sound.play("/audio/soun_fx/intro/bodythud.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    "*Body thud*!" with vpunch
    show whipend 1_2 with dissolve:
        zoom 1.1 yalign 0.1 xalign 1.0
    show whipend 1_2:
        subpixel True
        easein 5 yalign 1.0
    hin"U-ugh!" with vpunch
    hint"That b-bastard..."
    hint"I will never let him see me break!"
    hint"He'll answer for this... I swear it!"
    show blackscreen:
        alpha 0.0
    show blackscreen:
        subpixel True
        easein 6 alpha 1.0
    stop ambience fadeout 5
    stop ambience2 fadeout 5
    "Some time later..."
    scene black with dissolve
    $ playmusic("audio/ost/Senya.opus",0.5)
    da"KOOOOJI!!" with vpunch
    show daimyo 3_1 with dissolve
    show demandingmen badguys1:
        xpos 1300 yalign 1.0 xzoom -1.0 yzoom 1.12 zoom 1.1
    show demandingmen:
        easein 1 xpos 700
    ko"Yes, my lord?" with vpunch
    da"Listen well, and don't waste my time..."
    da"You are to fetch and administer my concubine's recently developed concoction to a certain individual..."
    ko"May I ask for what occasion, my lord? As I understand, the drug's mixture is yet unstable. Its effects could even be lethal in its current form."
    da "I need results and I need them now, Koji! Besides, what better test than a living subject?"
    ko"Who is the target, my lord?"
    da"You are to secretly administer the drug to the Hokage's wife!"
    ko"L-lady [hin_name]!?" with vpunch
    da"Is that a problem, Koji...?"
    ko"Of c-course not, my lord! It's just..."
    ko"What if the Lady... perishes? The other nations would surely raise questions. The optics of the Hokage's wife perishing while he is held captive, it could spark unrest-"
    show daimyo 4_1 with fade
    da"I don't give a rat's ass if she dies! That defiant bitch mocks my rule with every breath."
    da"The order stands, Koji!"
    da"Mix the drug in a bowl of water, offer it as a 'secret kindness' to our 'prized' captive, and report back once she drinks."
    da"If she dies, she dies. We'll simply have to craft a calculated lie."
    show daimyo 2 with fade
    da"If she survives, then... *Perverted chuckles*"
    da "Get it done!" with vpunch
    ko"At once, my lord..."
    hide demandingmen with dissolve
    show blackscreen:
        alpha 0.0
    show blackscreen:
        easein 3 alpha 1.0
    da"Hehehe! Let's see you defy me now, wretched whore!"
    scene black with dissolve
    stop ambience fadeout 3
    stop ambience2 fadeout 3
    $ renpy.end_replay()
    jump action_taken



    


    

    



label hinata_captured_midnight2:
    stop music fadeout 2
    "Meanwhile..."
    label hinata_captured_midnight2_replay:
    $ initialize_replay_defaults()
    $ renpy.sound.play("/audio/soun_fx/dungeon_ambient.opus", channel="ambience", loop=True, relative_volume = 1.0)
    # $ renpy.sound.play("/audio/soun_fx/horror.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    $ renpy.sound.play("/audio/soun_fx/dungeon_ambient2.opus", channel="ambience2", loop=True, relative_volume = 1.0)
    scene v20z_1 at dizzyflashshort:
        yalign 0.0
    hint"*Heavy breathing*... Why is my heart racing so fast?"
    hint "This... strange warmth spreading through me... What is it?"
    show v20z_1:
        easein 1 yalign 1.0
    $ renpy.sound.play("/audio/soun_fx/horror.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    hint"My entire body is flaring up..."
    hint"Down there... it feels so hot. W-why?"
    hint"I can't... hold it in any longer!" with vpunch
    show emptycell with dissolve:
        yalign 1.0
    show emptycell_toji1:
        alpha 0.0
    show emptycell_toji1:
        easein 5 yalign 0.6 alpha 1.0
    $ renpy.sound.play("/audio/soun_fx/ominous_sound.opus", channel="sfx2", loop=False, relative_volume = 0.6)
    kot"Still alive I see, but did she consume the drink?"
    ko "My lady... are you alright?"
    show v20z_1_1 with dissolve:
        yalign 0.0
    $ renpy.sound.play("/audio/soun_fx/longpiss.opus", channel="sfx3", loop=True, relative_volume = 0.8)
    show v20z_1_2:
        yalign 0.0
    show v20z_1_2:
        easein 2 yalign 1.0    
    hin"P-please, don't look! I... I can't h-hold it in!" with vpunch
    stop sfx3 fadeout 1
    show v20z_1_3 with dissolve
    call showscrollingimage from _call_showscrollingimage_228
    show screen parallax1280("v20z_1_3",1,0.6) with dissolve
    hint"W-what is wrong with me..."
    kot"The bowl! It's empty!" with vpunch
    kot"Does that mean... the drug is in effect!?"
    show black
    call hidescrollingimage from _call_hidescrollingimage_195
    $ renpy.sound.play("/audio/soun_fx/prison_cell.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    kot"I should... c-confirm before I report back to the Daimyo!"
    scene v20z_1_3 with dissolve:
        yalign 1.0
    ko"Poor thing, you must be suffering. I didn't mean to shame you my l-lady, but I do have to dispose of the evidence, remember?"
    show v20z_1_3:
        easein 5 yalign 0.0
    hin"K-koji... *Heavy breathing* W-what is happening to me?"
    ko"I... am unsure, my lady. But I am here to ease your pain, I assure you!"
    ko"Being in this... state, it must be degrading. I am s-sorry my Lady."
    hin"..."
    ko"Let me help you to your feet. We should do something about this mess..."
    scene black with dissolve
    hin"T-thank you... for the water, and your kindness... Koji."
    call showscrollingimage from _call_showscrollingimage_229
    show screen parallax1280("v20z_1_3_2",1,0.6) with dissolve
    hin"Y-you... are not like the others."
    hin"Tell me, p-please... do you know... what's wrong with me?"
    ko "You feel it, don't you? A fire coursing through your veins, a heat you can't ignore?"
    hin"Y-yes... I am d-drenched in sweat, my body... it's like it's not mine anymore. And this hot flush-"
    ko "We need to cool you down, my lady. Let me help..."  
    scene black with dissolve
    call hidescrollingimage from _call_hidescrollingimage_196
    $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 1.6)
    call showscrollingimage from _call_showscrollingimage_230
    show screen parallax1280("v20z_1_3_1",1,0.6) with dissolve
    hin"W-wait, p-please!" with vpunch
    ko"I assure you my lady, this will be of great help..."
    hin"B-but... down there..."
    hin"I f-feel... strange!"
    ko"Naturally, your body must be itching for a comforting touch right about now. You must be craving for relief..."
    hin"A... c-comforting touch? R-relief?"
    show screen parallax1280("blackscreen",1,0.6) with dissolve
    $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 1.6)
    show screen parallax1280("v20z_1_3_1a",1,0.6) with dissolve
    hin"...!" with vpunch
    ko"Ah, I see now. My suspicions are confirmed..."
    hide screen parallax1280
    show screen parallax1280("v20z_1_3_1b",1,1.0)
    with dissolve
    ko"Your pussy... it's drenched, my lady! You're trembling with need!" with vpunch
    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp4.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    hin"*Gasps!* N-not there!" with vpunch
    scene black
    call hidescrollingimage from _call_hidescrollingimage_197
    hin "S-stop! This isn't... I can't!" with vpunch
    call showscrollingimage from _call_showscrollingimage_231
    show screen parallax1280("v20z_1_4a",1,0.6) with dissolve
    $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 2.0)
    hin"T-this is... adultery!" with vpunch
    ko"No-no-no! You misunderstood me m-my lady..."
    ko"I am simply trying to help alleviate you of your current state..."
    hin"Mmmh... But, my hu-husband... I am his!"
    ko"Oh don't worry about him..."
    ko"He would want this for you, wouldn't he? For you to feel... at peace, free of this torment. Right?"
    hin"...N-no!"
    show screen parallax1280("blackscreen",1,0.6) with dissolve
    $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 1.6)
    show screen parallax1280("v20z_1_4_2",1,0.6) with dissolve
    $ renpy.sound.play("/audio/soun_fx/hinata/hinatamoan1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    ko"Look at you... so sensitive! Your nipples are all perked up. Your body is begging for more, isn't it?"
    $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 2.0)
    show screen parallax1280("v20_hin_captured koji1_tits",1,0.6) with dissolve
    $ renpy.sound.play("/audio/soun_fx/hinata/hinatamoan2.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    ko"Just a gentle touch... Doesn't this feel nice, my lady?" with vpunch
    $ renpy.sound.play("/audio/soun_fx/hinata/hinatamoan3.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    hin"*Moans* B-but... [na_name]!"
    $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 2.0)
    ko"You'll be right with him after this, you'll see..."
    $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 2.0)
    ko"Once the drug's effects well and truly kick in, you won't know the difference!"
    $ renpy.sound.play("/audio/soun_fx/grabsound.opus", channel="sfx1", loop=False, relative_volume = 2.0)
    hin"D-drug...? What d-drug... W-why does your t-touch feel... so s-soothing?"
    show screen parallax1280("v20z_1_5",1,0.6) with dissolve
    $ renpy.sound.play("/audio/soun_fx/hinata/hinatamoan1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    ko"It'll feel even better down there!" with vpunch
    hin"My... p-pussy? It's burning up!"
    ko"Let's ease that heat, shall we?"
    show screen parallax1280("blackscreen",1,0.6) with dissolve
    $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 1.6)
    ko"But first, allow me to remove your damp clothes. Soiled underwear are no good..."
    show screen parallax1280("v20z_1_6",1,0.6) with dissolve
    $ renpy.sound.play("/audio/soun_fx/hinata/hinatamoan2.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    ko"See...? That feels good, doesn't it?"
    $ renpy.sound.play("/audio/soun_fx/hinata/hinatamoan3.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    hin"Mhm♡... S-stop, please!" with flash
    show screen parallax1280("v20z_1_6_1",1,0.6) with dissolve
    ko"But we are just getting started, my lady!"
    $ renpy.sound.play("/audio/soun_fx/hinata/hinatamoan4.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    hin"Y-you...A-ah! *soft moan* You can't touch me th-there!" with vpunch
    show screen parallax1280("v20_hin_captured koji1_pussy",1,0.6) with dissolve
    $ renpy.sound.play("/audio/soun_fx/handjob3.opus", channel="sfx1", loop=True, relative_volume = 0.8)
    ko"You say that, yet with every touch your pussy keeps oozing juice! You are enjoying this, aren't you?"
    $ renpy.sound.play("/audio/soun_fx/hinata/hinatamoan1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    hin"N-no! *moans* I am...♡ n-not!" with vpunch
    ko"Don't try to fight the pleasure, my lady..."
    hin"P-please! M-my husband... I l-love him!"
    ko"The aphrodisiac can overpower even your greatest inhibitions..."
    $ renpy.sound.play("/audio/soun_fx/hinata/hinatamoan2.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    hin"A-aphro...disiac? *moans*" with vpunch
    show screen parallax1280("v20_hin_captured koji1_pussyfast",1,0.6) with dissolve
    $ renpy.sound.play("/audio/soun_fx/handjob5.opus", channel="sfx1", loop=True, relative_volume = 0.8)
    ko"Don't worry! Some good orgasms later, you ain't gonna be remembering much of your husband anyway!" with vpunch
    "The aphrodisiac drug inhibited [hin_name]'s every sense, sending shivers down her spine with every movement of Koji's fingers. It didn't take long before [hin_name]'s futile resistances broke down."
    hin"N-no... *moans* No! I don't want to... f-forget about..." with flash
    $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 1.6)
    stop sfx1 fadeout 2
    show screen parallax1280("blackscreen",1,0.6) with longerflash
    hin"♡...[na_name]! Aaah-♡aah!♡ *orgasmic moans*!!"
    show screen parallax1280("v20z_1_7",1,0.6) with dissolve
    hin"*Heavy breathing*...♡ What's... going on..."
    hin"W-why... is my b-body... like this?"
    ko"I think you are primed, my lady..."
    hin"P...primed? W-where... am I?"
    ko"Just look at that pussy juice dripping down your thighs..."
    $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 1.6)
    show screen parallax1280("blackscreen",1,0.6) with dissolve
    ko"You are indeed primed!"
    show screen parallax1280("koji_l1",1,0.6) with dissolve
    ko"Primed for fornication!" with vpunch
    ko"I can sense the heat emanating from your womb, onto my cock. You might even be ovulating, my lady..."
    hin"O...ovulating? N-no... wait!"
    ko"The aphrodisiac can have that effect. You must be extremely vulnerable to conception right now..."
    show screen parallax1280("koji_l1_1",1,0.6) with dissolve
    $ renpy.sound.play("/audio/soun_fx/hinata/hinatamoan2.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    ko"And there's no way I am letting the Daimyo instill more bastards in you!"
    hin"The... D-daimyo? *moans* N-no, K-koji... W-we can't!"
    show screen parallax1280("v20_hin_captured koji1_stomachrub",1,0.6) with dissolve
    ko"Please, my lady... I'll make you a d-deal!"
    ko"The t-truth is, I've always loved you!"
    hin"L-loved... me? W-what is going on..."
    ko"Ever since the first time I saw you, I've longed for you, lusted for your forbidden body..."
    ko"I have never been more infatuated with a woman. Strong-willed, smart, and an amazing body, all wrapped in one solemnly cute package!"
    ko"Let's copulate, let's have children [hin_name]! I'll help you escape, and we'll raise a happy family far away from these lands!"
    hin"I don't... understand... what's happening!"
    show screen parallax1280("blackscreen",1,0.6) with dissolve
    ko"Argh! I can't take it any more, my lady!"
    $ renpy.sound.play("/audio/soun_fx/chain_rattle2.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    hin"K...Koji-san?" with vpunch
    $ renpy.sound.play("/audio/soun_fx/chain_rattle3.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    ko"Do not fret, my lady. I know you are tired! This will help keep you in a breeding position!"
    show screen parallax1280("koji_l2",1,0.6) with dissolve
    ko"The Daimyo be damned! Let's fornicate... Let's FUCK like animals!" with vpunch
    show screen parallax1280("koji_l2_0",1,0.6) with dissolve
    ko"I love you my lady! I'll make you mine!" with vpunch
    scene black
    call hidescrollingimage("Click twice to fornicate!") from _call_hidescrollingimage_198
    $ renpy.sound.play("/audio/soun_fx/pushitin1.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    $ renpy.sound.play("/audio/soun_fx/various_sex/mature_sexslaps1.opus",loop=True, channel="sfx3", relative_volume = 0.8)
    ko"Aw♡-uuaah!♡" with flash
    show koji_l2_1:
        alpha 0 yalign 0.0
    show koji_l2_1 at custom_vpunch_repeat:
        easein 8 yalign 0.8 alpha 1.0
    # $ start_continuous_plaps(interval=2)
    ko"I knew it! You truly are one of a kind! Y-your pussy's grip is just so tight..."
    ko"Yet it takes my cock all the way in with ease!"
    hin"*moans* A-ah...♡ uuh!"
    ko"Our compatibility is unmatched! We were meant for each other..."
    ko"But If i am to s-save you... this has to be kept a secret, or we'll both be dead not before long!"
    ko"Do you... *groan*... u-understand, my lady?"
    hin"*moans* M-my pussy... it f-feels... nice! A-ah...♡ uuh!"
    ko"I love you! I LOVE YOU! I want you to..."
    ko"...I want you to *groan*... have my kids, lady [hin_name]! I want you to... get pregnant!"
    show koji_l2_1:
        easein 3 alpha 0.0
    # $ stop_continuous_plaps()
    ko"Get pregnant♡! Get pregnant♡!♡ Get PREGNAAAANT!!" with vpunch
    $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx1", loop=False, relative_volume = 0.5)
    scene black with flash
    stop ambience fadeout 2
    stop ambience2 fadeout 2
    stop sfx2 fadeout 2
    stop sfx3 fadeout 2
    "..."
    show bo_wakeup_during_dream with dissolve
    call increaselust(10) from _call_increaselust_279
    bot"F-fuck! I can't even sleep these days..."
    bot"What am I even doing knowing [hin_rel] is held captive for three days now..."
    scene black with dissolve
    bot"I get this feeling something terrible is going on..."
    $ renpy.sound.play("/audio/soun_fx/dungeon_ambient.opus", channel="ambience", loop=True, relative_volume = 1.0)
    "..."
    show koji_l2_1 with dissolve:
        yalign 0.0
    
    ko"I love you... I LOVE YOU!" with vpunch
    $ renpy.sound.play("/audio/soun_fx/cum9.opus", channel="sfx1", loop=False, relative_volume = 0.5)
    show koji_l2_2 with flash:
        easein 3 yalign 0.6
    ko"O-ooaah! *orgasms*!♡! Y-you love me too... r-right!?" with vpunch
    "???" "Oooooooi-oi-oi!!" with Shake((0, 0, 0, 0), 2, dist=10, peak_time=0.7, smoothness=50)
    show koji_l2_2_1 with dissolve:
        zoom 1.2 xalign 0.0 yalign 0.7
    "???" "What in the FUCK is going on in here!? Koji, you sly motherfucker..."
    show emptycell_koji with dissolve:
        yalign 1.0
    $ renpy.sound.play("/audio/soun_fx/horror.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    show emptycell_koji:
        easein 4 yalign 0.0
    to"Did the Daimyo not say to leave her untouched, you sneaky rat!?"
    ko"Toji! It's... it's not what you think!"
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/prison_cell.opus", channel="sfx1", loop=False, relative_volume = 1.0)
    "Toji furious but intrigued, forced his way into the cell."
    "Koji quickly dismounted [hin_name] in a state of panic, knowing full well his life would be on the line if the Daimyo found out about his actions..."
    scene v20_day1_ending1 with dissolve:
        yalign 0.0
    show v20_day1_ending1:
        easein 6 yalign 1.0
    to "Do you know how many times I've dreamed of fucking this bitch?" with vpunch
    to"Instead, I find you mounting her like an animal, her cunt full of your filthy sperm!"
    to"Tell me exactly what is going on before I rat your ass out to the Daimyo!" with vpunch
    ko"Th-the Daimyo, he ordered for me to administer a powerful drug to her..."
    ko"I was just... co-confirming its effects!"
    call showscrollingimage from _call_showscrollingimage_232
    show screen parallax1280("v20_day1_ending1",1,0.6) with dissolve
    "The two men spend some time arguing while [hin_name] laid confused and defiled, entranced by the drug's effects."
    "Not before long, the men came at an agreement..."
    ko"He'll have us both killed if he finds out she is 'unpure'!"
    to"Yeah well, tough luck! You are the one who started it you stupid fuck!"
    to"Either I rat you out, or I get to have some fun too..."
    scene black
    call hidescrollingimage from _call_hidescrollingimage_199
    $ renpy.sound.play("/audio/soun_fx/prison_cell.opus", channel="sfx1", loop=False, relative_volume = 1.0)
    kot"*Tsk!* B-bastard... There goes my dreams." with vpunch
    show emptycell_toji1 with dissolve:
        yalign 1.0
    show emptycell_toji1:
        easein 4 yalign 0.2
    ko"F-fine, but..."
    kot"If I can't have her, then neither should you!"
    ko"Don't take too long. The Daimyo will be visiting her shortly..."
    to"Just... buy me a few minutes, or hours-"
    show emptycell:
        alpha 0.0
    show emptycell:
        easein 5 alpha 1.0
    ko "You better clean her up too, otherwise we'll both be dead shortly!" with vpunch
    to"Tsk! Fucking rat bastard..."
    scene black with dissolve
    to"On your knees, bitch!" with vpunch
    show v20_day1_ending1_1 with dissolve:
        yalign 0.0
    show v20_day1_ending1_1:
        easein 5 yalign 1.0
    to"No fun... You are drugged out of your fucking mind, aren't you?"
    hin"To...ji?"
    to"Ooh!? You remember my name!"
    scene black
    $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 1.6)
    to"Guess there's some life left in you yet!" with vpunch
    scene v20_day1_ending1_2 with dissolve:
        yalign 0.0
    show v20_day1_ending1_2:
        easein 5 yalign 1.0
    to"Do you remember the times you've denied me too?"
    to"Yet here you are, panting like a bitch in heat beneath my cock!"
    call showscrollingimage from _call_showscrollingimage_233
    show screen parallax1280("v20_day1_ending1_2",1,0.6) with dissolve
    hin"I... remember you. You are... a bad man!"
    hin"But this cock... It's pretty. The scent...it's...drawing me in!"
    to"Bwa-haaaha!"
    to"Don't you worry 'my lady'! You'll be getting a good taste of it soon!"
    to"It's a shame I don't have enough time to ravage your holes as much as I would like..."
    show screen parallax1280("blackscreen",1,0.6) with dissolve
    to"Instead..."
    show screen parallax1280("v20_toji1",1,0.6) with dissolve
    to"I'll make good use of this running mouth of yours!"
    hin"We can't... do that..."
    show screen parallax1280("v20_toji1_1",1,0.6) with dissolve  
    to"Sure we can! Especially since you seem so eager for it too, with your little tongue hanging out your whore mouth..." with vpunch
    to"I've been waiting for this moment ever since I first saw you..."
    to"Now open wide, bitch!" with vpunch
    show screen parallax1280("blackscreen",1,0.6) with dissolve
    hin"B-but...-" with vpunch 
    $ renpy.sound.play("/audio/soun_fx/gags/SDTGag2.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    show screen parallax1280("v20_toji1_2",1,0.6) with flash
    to"No buts! Now choke on it!" with vpunch
    $ renpy.sound.play("/audio/soun_fx/gags/SDTGag5.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    hin"*gags*!" with vpunch
    to"Come on, it's not even halfway through your throat. You could at least put some effort into it..." with vpunch
    $ renpy.sound.play("/audio/soun_fx/gags/SDTGag8.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    hin"*gags*"
    to"What was that...? 'I can do better' you say?"
    show screen parallax1280("blackscreen",1,0.6) with dissolve
    to"If you say so..."
    $ renpy.sound.play("/audio/soun_fx/gags/SDTGag2.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    show screen parallax1280("v20_toji1_3",1,0.6) with dissolve
    to"Now that's more like it!" with vpunch
    to"I am not letting go until I empty my balls down your throat..." with vpunch
    scene black
    $ renpy.sound.play("/audio/soun_fx/various_sex/deeptroat_forced1.opus",loop=True, channel="sfx2", relative_volume = 0.5)
    show screen parallax1280("v20_hin_captured toji_bj1",1.0,0.6,transformeffect=custom_ypunch_repeat(timer=1.6)) with dissolve
    to"Now that's more like lady of the leaf I've been dreaming about!"
    to"Consider this my revenge for every snide look, every demeaning word of yours..."
    to"All you Konoha cunts are the same! Always pretentious, riding your high horses of morality..." with vpunch
    stop sfx2 fadeout 0.5
    show screen parallax1280("v20_hin_captured toji_bj2",1.0,0.6,transformeffect=custom_ypunch_repeat(timer=0.8)) with dissolve
    $ renpy.sound.play("/audio/soun_fx/various_sex/deepthroat_gluck.opus",loop=True, channel="sfx2", relative_volume = 0.7)
    to"Aaargh! That empty look on your face makes my blood boil!" with vpunch
    to"It's no fun using your mouth pussy when you are drugged out of your fucking mind..."
    to"But that won't stop me from using it like a cock-sleeve!"
    to"I only wish you were present to bear witness to your sorry state..."
    to"You Konoha whores are lucky you were born on this side of the world..."
    to"Otherwise we'd make sure to make good use out of your bountiful cunts on our side of the world."
    to "We'd show you what real cock feels like. Your impotent men, your husband especially, they are all a sorry bunch of fucking twerps!"
    to "It's no fair when women as beautiful as you, end up with such useless men..."
    to"No matter. Once the Daimyo's plan succeeds, you'll all be riding our cocks instead!"
    to"Speaking of the Daimyo..." with flash
    show screen parallax1280("blackscreen",1.0,0.6) with flash
    $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
    $ renpy.sound.play("/audio/soun_fx/gaspforair3.opus", channel="sfx2", loop=False, relative_volume = 1.5)
    hin"*gasping for air*"
    to"It ain't gonna be much longer before he makes his way here."
    to"I'd rather be alive to see the day your shitty nation burns to the ground, so..."
    show screen parallax1280("v20_tojicum1_1_rub",1.0,0.6) with dissolve
    to"It's best we make this quick!"
    scene black
    show screen parallax1280("v20_tojicum1_1_rub",1.0,0.6,transformeffect=custom_vpunch_repeat(timer=1.8)) with dissolve
    "Toji started rubbing his still erect cock all over [hin_name]'s face, smearing it with his semen..."
    to"I have a special technique in mind..."
    to"One that allows for maximum depth penetration, and maximum degradation!"
    to"In fact, I have had a prisoner die on me while performing my special technique. But you..."
    to"You can take it, can't you? You are strong!"
    to"Strong willed, strong-minded, you are the Hokage's bitch! The Lady of the leaf..."
    hin"I... am... I am-"
    show screen parallax1280("blackscreen",1.0,0.6) with dissolve
    $ renpy.sound.play("/audio/soun_fx/gags/SDTGag2.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
    $ renpy.sound.play("/audio/soun_fx/various_sex/deepthroat_gluck.opus",loop=True, channel="sfx2", relative_volume = 0.7)
    to"Let's see if the Lady can handle this!" with flash
    "Toji stepped forward, towering above [hin_name], his legs firmly planted across her sides and his cock dangling above her smeared face..."
    show screen parallax1280("v20_tojicum0_1",1.0,0.6,transformeffect=custom_vpunch_repeat(timer=1.8)) with dissolve
    hin"*gagging noises* Gl-uck...guh!" with vpunch
    to"Now THIS... is how you fuck a throat!" with vpunch
    to"Y-yeaaah... That's it, you bitch! You sit there like a good girl while choking on my cock, with my balls slapping against your pretty face!"
    to"I'll empty an entire civilization of sperm so deep down your esophagus, you'll have no need for food for the rest of the week!"
    to"You'll swallow every last drop of cum, as if it were sugar-coated pearls of semen!"
    show screen parallax1280("v20_tojicum0_1a",1.0,0.6) with flash
    to"Don't... pass out on me now! *groan* Aaargh!" with flash
    show screen parallax1280("v20_tojicum0",1.0,0.6,transformeffect=custom_vpunch_repeat(timer=1.8)) with flash
    to"Open wide, bitch! H-here it comes! AAARGH!" with vpunch
    scene black
    call hidescrollingimage() from _call_hidescrollingimage_200
    show v20_tojicum0:
        yalign 1.0 alpha 0.0
    show v20_tojicum0 at custom_vpunch_repeat:
        easein 5 yalign 0.0 alpha 1.0
    "Toji kept mercilessly thrusting his hips, while dragging [hin_name] upwards by her hair. The size of his cock left her throat bulged."
    "It wasn't long before his legs started convulsing. The wet heat of [hin_name]'s insides sent him over the edge, and a few final thrusts after..."
    stop sfx2 fadeout 1 
    $ renpy.sound.play("/audio/soun_fx/throatcum.opus", channel="sfx1", loop=False, relative_volume = 0.6)
    show v20_tojicum00 with longerflash:
        yalign 0.0
    show v20_tojicum00:
        easein 3 alpha 0.0
    show v20_tojicum0:
        alpha 0.0
    show v20_tojicum0:
        easein 3 alpha 1.0
    to"AAAAAAARGH!!!" with flash
    $ renpy.sound.play("/audio/soun_fx/throatpie.opus", channel="sfx1", loop=False, relative_volume = 1.0)
    call showscrollingimage from _call_showscrollingimage_234
    show screen parallax1280("v20_tojicum0",1,0.6) with dissolve
    to"Now keep swallowing, bitch! *Heavy breathing*" with flash
    to"D-damn... look at you go!"
    to"From being the Hokage's wife, reduced to a semen vacuum for my cock!"
    call hidescrollingimage from _call_hidescrollingimage_201
    to"Bwa-ha-haha!" with vpunch
    $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx1", loop=False, relative_volume = 0.5)
    $ renpy.sound.play("/audio/soun_fx/gaspforair3.opus", channel="sfx2", loop=False, relative_volume = 1.5)
    show v20_tojicum1_1 with flash
    show v20_tojicum1_1:
        easein 3 yalign 0.4
    hin"*gasping for air*"
    to"You pulled through! Impressive..."
    to"Yet I do see some of my precious kids still lying on your tongue..."
    show v20_tojicum0_2 with dissolve:
        yalign 0.0
    show v20_tojicum0_2:
        easein 6 yalign 1.0
    to"And that look on your face, I am not sure I like it!" with vpunch
    to"Tell me, my lady... who's your master!?"
    hin"Na... [na_name]..."
    to"Wrong answer!"
    show v20_tojicum1_1_slap with dissolve:
        yalign 0.5
    pause 0.2
    $ renpy.sound.play("/audio/soun_fx/slapecho.opus", channel="sfx2", loop=False, relative_volume = 1.2)
    show v20_tojicum1_1_slap1 with flash:
        yalign 0.5
    to"Get out of my face, bitch!" with vpunch
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/intro/bodythud.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    call showscrollingimage from _call_showscrollingimage_235
    show screen parallax1280("v20_tojicum1_2",1,0.6) with dissolve
    hin"..."
    to"I can't believe Koji of all men got to fill your cunt first..."
    show screen parallax1280("blackscreen",1,0.6) with dissolve
    to"And now I have to clean this fucking mess of piss and cum myself..."
    $ renpy.sound.play("/audio/soun_fx/longpiss.opus", channel="sfx3", loop=True, relative_volume = 0.8)
    to"Oi..."
    show screen parallax1280("v20_day1_ending1_4",1,0.6) with dissolve
    to"Oi OI! What the fuck are you doing, you dumb cunt!" with vpunch
    stop sfx3 fadeout 2
    hin"Safe... sex..."
    to"You've lost your fucking mind, didn't you..."
    show screen parallax1280("blackscreen",1.0,0.6) with dissolve
    to"*Sigh...* Time to clean this shit up."
    scene black
    call hidescrollingimage from _call_hidescrollingimage_202
    stop ambience fadeout 3
    stop ambience2 fadeout 3
    "Meanwhile..."
    $ playmusic("audio/ost/Senya.opus",0.5)
    show daimyo 3_1 with dissolve
    show demandingmen badguys1:
        xpos 1300 yalign 1.0 xzoom -1.0 yzoom 1.12 zoom 1.1
    show demandingmen:
        easein 1 xpos 700
    ko"It is done, my lord..." with vpunch
    show daimyo 4_1 with fade
    da"Am I to understand that she is still alive then?"
    ko"Alive and w-well, my lord. Although the drug's effects might have been stronger than we initially expected..."
    show daimyo 2 with fade
    da"Hi-hee-he! I don't see the problem with that!"
    scene black with dissolve
    da"I shall check it out myself momentarily..."
    scene black
    da"You are dismissed!" with vpunch
    ko"H-hai!"
    "..."
    $ renpy.end_replay()
    jump action_taken
    



label hinata_captured_midnight3:
    stop music fadeout 2
    scene black with dissolve
    "Meanwhile..."
    label hinata_captured_midnight3_replay:
    $ initialize_replay_defaults()
    $ renpy.sound.play("/audio/soun_fx/dungeon_ambient.opus", channel="ambience", loop=True, relative_volume = 1.0)
    # $ renpy.sound.play("/audio/soun_fx/horror.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    $ renpy.sound.play("/audio/soun_fx/dungeon_ambient2.opus", channel="ambience2", loop=True, relative_volume = 1.0)
    $ renpy.sound.play("/audio/soun_fx/various_sex/mature_sexslaps2.opus",loop=True, channel="sfx3", relative_volume = 0.8,fadein=2)
    hin"Aaah-ah..ah!"
    show v20_daimyoend_0test1 with dissolve:
        alpha 0.0 yalign 1.0
    show v20_daimyoend_0test1 at custom_vpunch_repeat:
        easein 4 alpha 1.0 yalign 0.02
    da"I did tell you the night is still young..."
    hin"Aaah-ah-ah...♡ *moans* ah!♡ M-more... H-harder Aaah-ah-ah...♡!"
    call showscrollingimage from _call_showscrollingimage_236
    show screen parallax1280("v20_daimyoend_0test1",1,0.6) with dissolve
    da"You have no idea HOW much more awaits you, you slut!"
    $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    stop sfx3 fadeout 1
    show screen parallax1280("blackscreen",1,0.6) with longerflash
    da"Uuuuuhh-uhuuu! *orgasm*"
    show screen parallax1280("v20_daimyoend_0test0",1,0.6) with dissolve
    hin"My p-pussy...♡ It still burns♡!"
    da"Addiction must be kicking in..."
    da"You know, maybe I do have room for another concubine after all."
    show screen parallax1280("blackscreen",1,0.6) with dissolve
    da"But first, I have to confirm you are capable of fulfilling that role!"
    $ renpy.sound.play("/audio/soun_fx/various_sex/mature_sexslaps1.opus",loop=True, channel="sfx3", relative_volume = 0.8,fadein=2)
    show screen parallax1280("v20_daimyoend_0test2_1",1,0.6,transformeffect=custom_vpunch_repeat(timer=1.8)) with dissolve
    da"I am not going to leave you to rest until you beg for me to breed your stuck-up cunt!"
    hin"Aaah-ah-ah...♡ *moans* ah!♡ F-faster... H-harder!! Aaah-ah-ah...♡!"
    da"Y-yess! Beg for it, bitch!" with vpunch
    hin"Aaah-ah-ah...♡ F-fuck me! ah!♡ P-please!! Aaah-ah-ah...♡!"
    da"You are nothing but a sow!"
    $ renpy.sound.play("/audio/soun_fx/cum9.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    stop sfx3 fadeout 1
    show screen parallax1280("v20_daimyoend_01_2",1,0.6) with flash
    hin"♡♡ Aaaaaa-aahhh♡!♡ *orgasm*"
    da"Your cunt is worthy of it's title, 'Lady' of the leaf..."
    scene black
    call hidescrollingimage from _call_hidescrollingimage_203
    da"Bwaa-ahaha! You damn nympho!"
    scene v20_zend1 with dissolve:
            yalign 1.0
    show v20_zend1:
        easein 3 yalign 0.4
    da"I'd stay for more, but my cock is barely functional after carving your cunt out for three hours!"
    scene black with dissolve
    da"I'll be back for more of course at my earliest convenience... Hehehe!"
    "..."
    stop ambience fadeout 3
    stop ambience2 fadeout 3
    "A day goes by."
    scene palace
    show boruto angry
    with dissolve
    bot"*Tsk!* No luck yet..."
    show boruto worried with dissolve
    bot"I'll check again tonight."
    hide boruto with dissolve
    bot"I'll find you [hin_rel]..."
    scene black with dissolve
    "Later that day..."
    scene palace3_night
    show demandingmen badguys1
    with dissolve
    to"Oi! We have to do something!"
    ko"I know, I know!"
    ko"I have a plan. Meet me tonight by her cell..."
    scene black with dissolve
    "Later that night..."
    "Day 4..."
    $ renpy.sound.play("/audio/soun_fx/dungeon_ambient.opus", channel="ambience", loop=True, relative_volume = 1.0)
    # $ renpy.sound.play("/audio/soun_fx/horror.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    $ renpy.sound.play("/audio/soun_fx/dungeon_ambient2.opus", channel="ambience2", loop=True, relative_volume = 1.0)
    $ renpy.sound.play("/audio/soun_fx/various_sex/roughsex_repeat.opus",loop=True, channel="sfx3", relative_volume = 0.6,fadein=2)
    to"Oi..."
    show emptycell_koji with dissolve:
        yalign 1.0
    show emptycell_koji at custom_vpunch_repeat:
        easein 4 yalign 0.0
    to"OI! W-what kind of plan is this you sly horndog!"

    show v20_hin_captured day3toji with dissolve:
        zoom 1.0 xalign 0.0 yalign 1.0
    show v20_hin_captured at custom_ypunch_repeat:
        easein 5 yalign 0.4
    hin"Aaah-ahrrh! ♡ *groan* ah!♡ H-harder Aaah-ah-ah...♡!"
    ko"Shut the fuck up and keep watch, you dim-witted brute!" with vpunch
    ko"We'll... we'll take turns!"
    scene emptycell_koji with dissolve:
        yalign 1.0
    show emptycell_koji at custom_vpunch_repeat:
        easein 4 yalign 0.0
    to"Then hurry the fuck up! I am not going to sit here and watch you fuck her brains out!"
    scene v20_hin_captured day3toji with dissolve:
        zoom 1.0 xalign 0.0 yalign 1.0
    show v20_hin_captured at custom_ypunch_repeat:
        easein 5 yalign 0.4
    ko"You are just jealous you can't do this!"
    scene black
    show v20_hin_captured day3toji2 at custom_ypunch_repeat:
        yalign 0.7
    with dissolve
    ko"Piston mode, activated!" with vpunch
    hin"Aaah-ahrrh! ♡ *groan* ah!♡ Yes-yes-yes!♡ Aaah-ah-ah...♡!"
    scene emptycell_koji with dissolve:
        yalign 1.0
    show emptycell_koji at custom_vpunch_repeat:
        easein 4 yalign 0.0
    to"You goddamn fucking retard..."
    $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    stop sfx3 fadeout 2
    scene v20_day3_1_2 with longerflash
    show v20_day3_1_2:
        easein 4 yalign 0.1
    ko"*orgasms* UUuuh-uh-uuuh!"
    to"Oi..."
    to"...You done? Get the fuck outta there! It's my turn next"
    ko"W-what? Done!? Of c-course not..." with vpunch
    ko"Do you take me for an impotent three pump champion like yourself?"
    scene black with dissolve
    ko"I still got hours in me..."
    
    call showscrollingimage from _call_showscrollingimage_237
    $ renpy.sound.play("/audio/soun_fx/various_sex/deeptroat_forced1.opus",loop=True, channel="sfx3", relative_volume = 0.6,fadein=1)
    show screen parallax1280("v20_day3_bj1",1,0.6,transformeffect=custom_ypunch_repeat(timer=1.8)) with dissolve
    ko"I'll take her mouth next."
    to"L-leave something untainted from your filth for me, you freak!"
    ko"I was the one who came up with the plan. Finder's keepers!"
    to"I am losing my goddamn patience..."
    show screen parallax1280("blackscreen",1,0.6) with dissolve
    ko"Shut the fuck up and check this out..."
    $ renpy.sound.play("/audio/soun_fx/chain_rattle3.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    ko"Put this one there..." with vpunch
    $ renpy.sound.play("/audio/soun_fx/chain_rattle2.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    show screen parallax1280("v20_day3_bj1_1",1,0.6) with dissolve
    ko"And this one here..."
    ko"Can you believe I was in love with this bitch a few days ago?"
    ko "{size=*0.7}Legs up my lady, otherwise this may hurt...{/size}"
    ko"As soon as I stretched her pussy out the other day, I got over her real quick..."
    ko"Turns out she's just another hole, only prettier than most..."
    show screen parallax1280("emptycell_koji",1,0.6) with dissolve

    to"Fuck are you on about... More importantly, fuck are you even doing to her?"
    $ renpy.sound.play("/audio/soun_fx/spank5.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    show screen parallax1280("v20_day3_bj2",1,0.6) with flash
    ko"That's it! Now keep that ass up my lady. Three points of contact should be enough..." with vpunch
    show screen parallax1280("blackscreen",1,0.6) with flash
    $ renpy.sound.play("/audio/soun_fx/prison_cell.opus", channel="sfx1", loop=False, relative_volume = 1.0)
    to"I've had enough of your fucking circus clown show! I am coming in!"
    show screen parallax1280("v20_day3_bj3",1,0.6,transformeffect=custom_vpunch_repeat(timer=1.8)) with dissolve
    $ renpy.sound.play("/audio/soun_fx/various_sex/spitroast2_repeat.opus",loop=True, channel="sfx3", relative_volume = 0.6,fadein=2)
    ko"Yee-haa! Check this out! Suspended mid-air blowjobs are the best!"
    show screen parallax1280("blackscreen",1,0.6) with vpunch
    $ renpy.sound.play("/audio/soun_fx/sexslaps3.opus", channel="sfx1", loop=False, relative_volume = 1.0,fadein=1)
    to"Move over, I am taking the only place you've left untainted!"
    show screen parallax1280("v20_day3_bj4",1,0.6,transformeffect=custom_ypunch_repeat(timer=1.8)) with dissolve
    ko"*Tsk!* What if someone finds out you dimwit!" with vpunch
    to"Not my concern..."
    "The two men took turns violating the swinging [hin_name]..."
    "The chains attached to her limbs allowed for easy access to any of her holes."
    to"Won't she suffocate hanging like that?"
    ko"Three points of contact, distributed weight... You wouldn't get it!"
    scene black
    show v20_day3_bj4_1
    call hidescrollingimage from _call_hidescrollingimage_204
    stop sfx3 fadeout 2
    $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    show v20_day3_bj4_1 with flash:
        alpha 1.0 yalign 0.4
    show v20_day3_bj4_1:
        easein 5 alpha 0.0 yalign 0.3
    to"Turn her around, turn around! I wanna fuck her mouth too!"
    "."
    ".."
    "..."
    "Day 7"
    show v20_zend1 with dissolve:
        yalign 0.0
    show v20_zend1:
        easein 44 yalign 0.8
    hin"*Heavy breathing*...♡ Cock..."
    hin"I need... cocks♡!"
    $ renpy.sound.play("/audio/soun_fx/prison_cell.opus", channel="sfx1", loop=False, relative_volume = 1.0)
    scene daimyo_naked1 with dissolve:
        yalign 0.0
    scene daimyo_naked1 with dissolve:
        easein 4 yalign 1.0
    da"Ask and you shall receive!"
    scene black with vpunch
    da"Didn't think I'd forget about you, did you?"
    $ renpy.sound.play("/audio/soun_fx/various_sex/mature_sexslaps2.opus",loop=True, channel="sfx3", relative_volume = 0.8,fadein=2)
    show v20_zend1_vag1:
        alpha 0.0 yalign 1.0
    show v20_zend1_vag1 at custom_vpunch_repeat:
        easein 3 alpha 1.0 yalign 0.2
    hin"Aaah-ahrrh! ♡ *groan* ah!♡ Cock-cock-cooock! Ah-ah-harder! Aaah-ah-ah...♡!"
    show v20_zend1_vag1:
        easein 5 alpha 0 yalign 1.0
    stop sfx3 fadeout 3
    "Meanwhile..."
    show secret_dungeon_grate with dissolve:
        yalign 1.0
    show secret_dungeon_grate:
        easein 2 yalign 0.3
    bot"There's echoing screams coming down from down there!"
    bot"It must be were [hin_rel]'s held!"
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/intro/bodythud.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    bot"I am going in!" with vpunch
    scene v20_bo_dropin1_1 with dissolve:
        yalign 1.0
    show v20_bo_dropin1_1 with dissolve:
        easein 44 yalign 0.2
    bot"W-what the hell is this place..."
    bot"It reeks of... death and piss!"
    show captives 0 with dissolve:
        yalign 1.0
    show captives 0:
        easein 3 yalign 0.2
    bot"Is that guy d-dead? No wonder it smells like death!"
    hide captives with dissolve
    bot"Is this the kind of place [hin_rel] is held captive in for the measly crime of not paying debts?"
    bot"What bollocks! This place is hell. No proper ruler would ever do something like this..."
    scene black with dissolve
    bot"I'll have the Daimyo pay after I free [hin_rel]!"
    "Meanwhile..."
    label jumphere_capture_counter_3:
    call showscrollingimage from _call_showscrollingimage_238
    $ renpy.sound.play("/audio/soun_fx/various_sex/mature_sexslaps1.opus",loop=True, channel="sfx3", relative_volume = 0.9,fadein=1)
    show screen parallax1280("v20_zend1_vag1_1",1,0.6,transformeffect=custom_ypunch_repeat(timer=1.8)) with dissolve
    da"*Grunts*... Arh... T-take that! *Grunts*...Bitch!" with vpunch
    da"You can't stop moaning every time I rip through your cervix!"
    hin"Aaah-ahrrh! ♡ *groan* ah!♡ Aaah-ah-ah...♡!"
    stop sfx3 fadeout 1
    show screen parallax1280("blackscreen",1,0.6) with dissolve
    da "Oi, get up! Don't go collapsing on me yet..."
    da"I have more plans for you in mind..."
    show screen parallax1280("v20_zend1_vag1_2",1,0.6) with dissolve
    da"I've stretched your already used pussy way too often, but It appears I have neglected another hole of yours..."
    hin"A-♡aaaaah...♡"
    show screen parallax1280("blackscreen",1,0.6) with dissolve
    da"It's time we get that fixed! Come here you bitch!" with vpunch
    hide screen parallax1280
    show screen parallax1280("v20_daimyoend_0anal2_0",1,0.9)
    with dissolve
    hin"*Heavy breahting*...♡! Co...ck! More... cock!♡"
    da"Do not fret, for this cock will be stretching your asshole open!" with vpunch
    $ renpy.sound.play("/audio/soun_fx/pushitin1.opus", channel="sfx2", loop=False, relative_volume = 1.2)
    $ renpy.sound.play("/audio/soun_fx/various_sex/roughsex_repeat.opus",loop=True, channel="sfx3", relative_volume = 1.0)
    hide screen parallax1280
    show screen parallax1280("v20_daimyoend_0anal2_1",1,0.9)
    with flash
    stop sfx3 fadeout 1
    hin"*Painful moan* Aarh! M-my... ass!" with vpunch
    hide screen parallax1280
    show screen parallax1280("v20_hin_captured daimyoanal",1,0.9,transformeffect=custom_vpunch_repeat(timer=1.8))
    with flash
    $ renpy.sound.play("/audio/soun_fx/various_sex/roughsex_repeat.opus",loop=True, channel="sfx3", relative_volume = 1.0)
    $ renpy.sound.play("/audio/soun_fx/pushitin2.opus", channel="sfx2", loop=False, relative_volume = 1.2)
    hin"Arhh-aghhh!! *Painful moan*!" with vpunch
    da"That's it, all the way! I'll rip you a new one, you entitled Konoha bitch!" with vpunch
    scene black
    call hidescrollingimage from _call_hidescrollingimage_205
    stop sfx3 fadeout 2
    show v20_bo_dropin1 with dissolve:
        yalign 0.0
    show v20_bo_dropin1:
        easein 4 yalign 0.7
    bot"H-how much deeper does this place go..."
    bot"And what the hell is up with..."
    show captives 1_2 with dissolve:
        yalign 0.0
    show captives 1_2:
        easein 3 yalign 1.0
    $ renpy.sound.play("/audio/soun_fx/horror.opus", channel="sfx2", loop=False, relative_volume = 0.6)
    bot"...her!" with vpunch
    bot"She looks... d-defiled! M-maybe dead too..."
    hide captives with dissolve
    $ renpy.sound.play("/audio/soun_fx/various_sex/roughsex_repeat.opus",loop=True, channel="sfx3", relative_volume = 0.1)
    bot"F-fuck! I better find [hin_rel] fast..."
    scene black with dissolve
    "You head deeper into the dungeons..."
    $ renpy.sound.play("/audio/soun_fx/dream_ambient.opus", channel="sfxstat", loop=True, relative_volume = 0.5)
    "."
    ".."
    "..."
    $ renpy.sound.play("/audio/soun_fx/various_sex/roughsex_repeat.opus",loop=True, channel="sfx3", relative_volume = 0.3)
    show bg cell:
        alpha 0.0 yalign 1.0
    show bg cell:
        easein 8 alpha 1.0 yalign 0.5
    bot"Someone's there! I can hear faint grunts coming from beneath the darkness!"
    bot"..."
    $ renpy.sound.play("/audio/soun_fx/heartbeatlongfast.opus", channel="sfx2", loop=False, relative_volume = 1.2)
    bot"Whatever it is, it's behind this cell... I am sure of it!"
    menu:
        bot"Whatever it is, it's behind this cell... I am sure of it!"
        "...":
            pass
        "...":
            pass
        "...":
            pass
    play sound"/audio/soun_fx/heartbeat.opus" volume 2.5
    $ renpy.sound.play("/audio/soun_fx/various_sex/roughsex_repeat.opus",loop=True, channel="sfx3", relative_volume = 0.5)
    bot"."
    show bg cell with dissolve:
        zoom 1.1 xalign 1.0
    play sound"/audio/soun_fx/heartbeat.opus" volume 3.5
    bot".."
    show bg cell with dissolve:
        zoom 1.2 xalign 1.0
    play sound"/audio/soun_fx/heartbeat.opus" volume 4.5
    bot"..."
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/various_sex/roughsex_repeat.opus",loop=True, channel="sfx3", relative_volume = 0.7)
    scene emptycell with dissolve
    show emptycell_boruto_ntr1:
        alpha 0.0
    show emptycell_boruto_ntr1:
        easein 8 alpha 1.0
    bo"..."
    bo"M..."
    show emptycell_boruto_ntr1 at dizzy with dissolve
    $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx1", loop=False, relative_volume = 1.6)
    $ renpy.sound.play("/audio/soun_fx/earringing.opus", channel="sfx2", loop=False, relative_volume = 0.05)
    bo"[hin_rel_stutter]...?"
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/various_sex/roughsex_repeat.opus",loop=True, channel="sfx3", relative_volume = 0.9)
    call showscrollingimage from _call_showscrollingimage_239
    show screen parallax1280("v20_hin_captured daimyoanal",1,0.6,transformeffect=custom_vpunch_repeat(timer=1.8)) with dissolve
    da"It appears... *Grunts*... we have a spectator!" with vpunch
    show screen parallax1280("v20_hin_captured daimyoanalfast",1,0.6,transformeffect=custom_vpunch_repeat(timer=0.8)) with dissolve
    da"Let us put on a show then!" with vpunch
    hin"Aaah-ahrrh! ♡ *groan* ah!♡ YOU ARE S-STRETCHING...♡! MY ASS WIDE!" with vpunch
    scene black
    call hidescrollingimage from _call_hidescrollingimage_206
    show emptycell_boruto_ntr1 at dizzyflashshort
    $ renpy.sound.play("/audio/soun_fx/heartbeat.opus", channel="sfx1", loop=False, relative_volume = 1.6)
    $ renpy.sound.play("/audio/soun_fx/earringing.opus", channel="sfx2", loop=False, relative_volume = 0.05)
    menu gameover_daimyo_menu:
        hin"Aaah-ahrrh! ♡ *groan* ah!♡ YOU ARE S-STRETCHING...♡! M-MY..."
        "Give up...":
            scene emptycell_boruto_ntr1_1 with dissolve:
                yalign 0.3
            bo"[hin_rel_stutter]..."
            $ renpy.sound.play("/audio/soun_fx/eye4s.opus", channel="sfx1", loop=False, relative_volume = 0.3)
            show emptycell_boruto_ntr1_3 with flash:
                alpha 1.0 yalign 0.3
            show emptycell_boruto_ntr1_3:
                easein 1 alpha 0.0
            bo"[hin_rel.upper()]!"
            call showscrollingimage from _call_showscrollingimage_240
            show screen parallax1280("v20_hin_captured daimyoanal",1,0.6,transformeffect=custom_vpunch_repeat(timer=1.8)) with dissolve
            hin"Aaah-ahrrh! ♡ *groan* ah!♡ Give me m-more... MORE!" with flash
            da"Your asshole alone is tighter than all my concubines combined!"
            stop sfx3 fadeout 1
            $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx1", loop=False, relative_volume = 0.3)
            show screen parallax1280("v20_daimyoend_0anal2_3",1,0.9) with longerflash
            da"Uurr-yaaah! *Groans*" with vpunch
            scene black
            call hidescrollingimage from _call_hidescrollingimage_207
            bo"M...m-more?"
            bo"She wants... m-more!?"
            show v20_bo_dropin1_2 with dissolve:
                yalign 0.3
            bo"Y-you bastard... what did you do to her..."
            da"Ahh... I see now..."
            show v20_zend1_vag1_3 with dissolve:
                yalign 1.0
            show v20_zend1_vag1_3:
                easein 4 yalign 0.0
            hin"*Heavy breathing*...Ah...eh..."
            da"The resemblance is uncanny..."
            da"You look exactly like that Hokage cretin..." with vpunch
            da"You are... her [hin_rel_to_bo], aren't you?"
            show v20_zend1_vag1_3:
                easein 2 yalign 0.85
            da"You must be wandering why your whore of a [hin_rel_mother]'s asshole is left gaping by another man's cock..."
            scene black with dissolve
            da"How about you hear it straight from the source..."
            "The Daimyo carried [hin_name] to the edge of her cellar, mere inches away from you..."
            $ renpy.sound.play("/audio/soun_fx/longpiss.opus", channel="sfx1", relative_volume = 1.5)
            scene v20_defeat_1 with dissolve:
                yalign 1.0
            show v20_defeat_1:
                easein 3 yalign 0.3
            hin"Ah-aah! ♡ *orgasmic moans* ah!♡!" with vpunch
            da"Ah, there she goes pissing herself again!"
            da "Don't mind the shower kid... It's your [hin_rel_mother]'s after all! Hee-hee-he!"
            stop sfx1 fadeout 3
            hin"M-more♡... Please m-master♡! Give me more!♡"
            da"What was that... Did you hear her, kid?"
            hin"...Cock♡! I need.. COCKS♡! F-fuck me a-again... PLEASE!♡♡" with vpunch
            call increaselust(100) from _call_increaselust_280
            scene black with vpunch
            $ renpy.sound.play("/audio/soun_fx/intro/bodythud.opus", channel="sfx2", loop=False, relative_volume = 1.8)
            "*Thud!*"
            show v20_bo_dropin1_2 with dissolve
            da"You heard her. Your whore of a [hin_rel_mother] is a cock craving sow!"
            da"And I shall happily oblige her until the end of her days!"
            "At a loss for words, your legs gave out from beneath you..."
            "What once you remembered as a loving [hin_rel_mother] figure, was now reduced to nothing more than a sex-crazed animal right before your eyes."
            show v20_bo_dropin1_2_1 with dissolve
            bo"[hin_rel_stutter]..."
            bo"I thought you w-were..."
            show v20_bo_dropin1_2_2 with dissolve
            $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 1.1)
            bo"I T-THOUGHT YOU W-WERE MINE!" with flash
            scene black with dissolve
            da"BWAAA-HAA-HAA-HAA!" with vpunch
            da"Are you really jerking yourself to the sight of your [hin_rel_mother] being defiled?"
            $ renpy.sound.play("/audio/soun_fx/various_sex/roughsex_repeat.opus",loop=True, channel="sfx3", relative_volume = 1.6,fadein=2)
            call showscrollingimage from _call_showscrollingimage_241
            show screen parallax1280("v20_defeat_2",1,0.6,transformeffect=custom_ypunch_repeat(timer=1.8)) with dissolve
            da"Then let's give your bastard something to jerk off too, shall we?"
            hin"[bo_name_stutter]...?"
            $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 1.1)
            bo"[hin_rel_mother]! S-stop... P-please..." with vpunch
            hin"S-stop...? Aaah-ahrrh! ♡ *groan* B-but..."
            $ renpy.sound.play("/audio/soun_fx/jerkoffshort.opus", channel="sfx2", loop=False, relative_volume = 1.1)
            bo"Don't you see? H-he is evil! He is... using something against you! I know it!"
            hin"N-no... no! Aaah-ahrrh! ♡ *moans* M-MORE!"
            hin"S-sorry... [bo_name_stutter]... I just..."
            hin"I can't live... Aaah-ah-ah!♡ Without s-sex... Aaa-aaah! I can't live... without his cock!" with flash
            stop sfx3 fadeout 1
            stop sound fadeout 1
            stop music fadeout 1
            stop ambience fadeout 1
            stop ambience2 fadeout 1
            $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx1", loop=False, relative_volume = 0.3)
            show screen parallax1280("v20_defeat_2_1",1,0.6,transformeffect=custom_ypunch_repeat(timer=1.8)) with flash
            da"That's right! You'll forever be my personal sow!"
            scene black
            call hidescrollingimage from _call_hidescrollingimage_208
            $ renpy.sound.play("/audio/soun_fx/dream_ambient.opus", channel="sfxstat", loop=True, relative_volume = 0.5)
            scene v20_defeat_2_1 with dissolve:
                zoom 1.2 xalign 0.0 yalign 1.0
            "You lay frozen in disbelief, your world shattered in the blink of an eye. Your own guilt consuming you, agonizingly..."
            scene v20_defeat_2_1 with dissolve:
                zoom 1.4 xalign 0.0 yalign 1.0
            "You've lost your [hin_rel_mother] to another man..."
            "And your dignity by yourself."
            scene black with dissolve
            "You were eventually captured by the Daimyo's men, thrown in a cellar to rot until the end of your days."
            "Day 14...."
            $ renpy.sound.play("/audio/soun_fx/spank5.opus", channel="sfx1", loop=False, relative_volume = 0.3)
            scene v20_assdown0 with flash:
                yalign 0.0
            show v20_assdown0:
                easein 4 yalign 1.0
            ko"Shhh! S-stop fucking moaning..."
            "[hin_name] was kept in the dungeons for far longer than the promise of her three day tenure. The three men took turns copulating in secrecy, behind each other's backs..."
            scene black with dissolve
            "Day 30..."
            $ renpy.sound.play("/audio/soun_fx/growl3.opus", channel="sfx3", loop=False, relative_volume = 0.9)   
            $ renpy.sound.play("/audio/soun_fx/eye4s.opus", channel="sfx1", loop=False, relative_volume = 0.3) 
            show kurama1 onlayer screens with flashred
            show kurama1 onlayer screens:
                easein 2 alpha 0.0
            "Out of pure, unadulterated rage, you made one last attempt to free [hin_name] and escape..."
            show v20_borutokilled with dissolve:
                yalign 1.0
            show v20_borutokilled:
                easein 4 yalign 0.0
            "Your rage got you far, within a breath's distance of [hin_name]'s cellar..."
            "Before you could break her shackles, you were killed unceremoniously by one of the Daimyo's grunts, but not before killing two of his men yourself."
            scene black with dissolve
            "Day 90..."
            scene v20_pregnant1 with dissolve:
                yalign 0.0
            show v20_pregnant1:
                easein 5 yalign 1.0
            "[hin_name], a shadow of her former self, was found carrying a child within her womb..."
            scene black with dissolve
            "The Daimyo celebrated the occasion, thinking the child his own."
            "Day 180..."
            scene v20_hina_concubine with dissolve:
                yalign 1.0
            show v20_hina_concubine:
                easein 6 yalign 0.0
            "The drugs had stolen more than her freedom, they had stolen her very self. [hin_name] took her place among the Daimyo's concubines, another broken soul in his gilded harem."
            scene black with dissolve
            "Ten years later..."
            "Konoha unexpectedly fell, not to weakness, but to treachery. The village that had stood for generations crumbled as their own Daimyo opened the gates to foreign invaders."
            "Men were quickly killed, a mercy their women were not granted. A mysterious drug's influence spread among them, reshaping them into obedient cattle of their conquerors' will."
            "One woman survived..."
            scene v20_hima_revenge with dissolve:
                yalign 1.0
            show v20_hima_revenge:
                easein 5 yalign 0.0
            "[him_name] embarked on a lifelong mission of revenge, swearing vengeance upon those who wronged her family."
            scene black with dissolve
            $ renpy.sound.play("/audio/soun_fx/bassstart.opus", channel="sfx1", loop=False, relative_volume = 1, fadein = 0.05)
            queue sfx1 ("audio/soun_fx/introbass3.opus") volume 0.4 loop
            show disclameimerintro with Fade(0.5,0,3):
                zoom 2.0 xalign 0.6 yalign 0.3
            show disclameimerintro:
                easeout 30 subpixel True zoom 1.0 xalign 0.492 yalign 0.3
            "Years later, when the Shinobi world lay in ruins, survivors whispered of a woman with eyes like blood and the fury of a fox - a harbinger of their reckoning..."
            $ renpy.end_replay()
            menu:
                "Years later, when the Shinobi world lay in ruins, survivors whispered of a woman with eyes like blood and the fury of a fox - a harbinger of their reckoning..."
                "Game over":
                    dev"You dun fucked up with this one mate. There's no returning to reality now. You are living in it."
                    $ renpy.full_restart()

            
        "{color=[hatredcolor]}*The beast rages*{/color}" (supporter_scene = True):
            default hin_ending21_started = False
            default hin_ending21_faster = False
            default hin_ending21_spanked_counter = 0
            default hin_ending21_hairpulled_counter = 0
            default hin_ending21_counter = 0
            call checkHatred(30, "gameover_daimyo_menu") from _call_checkHatred_38
            label v21_rageending_hinata_replay:
            $ initialize_replay_defaults()
            $ call_label_action("v21_rageending_hinata")
            call supp_rew from _call_supp_rew_17
            jump gameover_daimyo_menu
            






