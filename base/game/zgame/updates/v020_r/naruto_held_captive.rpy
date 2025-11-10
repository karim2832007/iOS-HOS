label naruto_held_captive:
    $ initialize_replay_defaults()
    default naruto_captive_seen = False
    $ naruto_captive_seen = True
    $ playmusic("audio/ost/kumogakure.opus",0.6)
    scene black with dissolve

    "Meanwhile, in a far away place..."
    scene v20_raikage1 with dissolve:
        yalign 1.0
    show v20_raikage1:
        easein 6 yalign 0.1
    "Raikage" "Time to pay a visit to that sorry bastard..."
    "Raikage" "He can't possibly keep his ruse up for much longer!"
    scene black with dissolve
    "Raikage" "..."
    show rai_naru 1_0 with dissolve
    "Raikage" "There he is!"
    $ renpy.sound.play("/audio/soun_fx/dropweapon.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    show nintroflash with flash:
        alpha 1.0
    show nintroflash:
        easein 4 alpha 0.0
    "Raikage" "The man who... almost, held back against hundreds of my men!"
    "Raikage" "Yet as it turns out..."
    show rai_naru 1_1_smirk with dissolve:
        yalign 1.0
    show rai_naru 1_1_smirk:
        easein 4 yalign 0.4
    "Raikage" "The renowned Hokage is just another measly man."
    na"You know you won't get away with this."
    show rai_naru 1_1_serious with dissolve:
        yalign 0.4
    "Raikage" "Bold words for a man in chains."
    "Raikage" "Do you take me for a fool, [na_name]!" with vpunch
    "Raikage" "Do you think me a man without a plan, a man without cause?"
    na"What about... a man without honor?"
    scene rai_naru 1_2 with dissolve:
        yalign 1.0
    show rai_naru 1_2:
        easein 5 yalign 0.0
    "Raikage" "You blasted FOOL!" with vpunch
    "Raikage" "Tell me, then [na_name]! Where's the honor in a world as unjust as ours?" with vpunch
    "Raikage" "A world where your birthright determines your ambition, not your merit." with vpunch
    "Raikage" "It's easy to throw around accusations of dishonor, when you have been fortunate enough to rule over a nation with opulence the likes of which we can only dream about." with vpunch
    scene rai_naru 1_1_serious with dissolve:
        yalign 0.4
    "Raikage" "While our nation's children starve to death, yours revel in prosperity given to them by birthright, not claimed."

    "Raikage" "Our women lay old and infertile, yours bloom with youth and bear children in abundance, all flourishing in the lap of luxury and peace."
    "Raikage" "Our fields wither under relentless storms, our rivers run dry, and our people cling to scraps of hope. Your lands? They overflow with rice paddies that never fail, markets brimming with goods we can never produce ourselves." with hpunch
    "Raikage" "Do you know what happens to a nation that cannot feed its people, [na_name]?" with vpunch
    "Raikage" "Do you know what becomes of a nation where children cannot be raised?"
    "Raikage" "In two generations, maybe three, the Hidden Cloud will be nothing but a memory carved into empty mountainsides."
    "Raikage" "While your precious nation continues to flourish, growing stronger with each passing year."
    "Raikage" "So tell me again about honor, Hokage. Is it honorable to watch an entire nation's people fade into extinction?"
    "Raikage" "Is it honorable to hoard resources while neighboring nations wither away?"
    na "Conquest will not solve your problems, it will only create new ones."
    na "The prosperity you speak of wasn't built in a day, nor was it built on the bones of other nations."
    scene rai_naru 1_0 with dissolve
    na "Our ancestors planted seeds of cooperation, not domination. They built alliances, not graveyards."
    na "If you truly care for your people's future, then cooperate with us to find a solution that doesn't demand blood."
    show rai_naru 1_2 with dissolve:
        yalign 0.4
    "Raikage" "Oh you bet your ASS, I'll be cooperating with your people..." with vpunch
    "Raikage" "More specifically, I'd gladly cooperate with your nation's women to bolster our own numbers..." with vpunch
    na"The other nations would condemn your actions. Your nation would be forever ostracised you fool!"
    scene rai_naru 1_1_serious with dissolve:
        yalign 0.4
    "Raikage" "See... that's where we differ!"
    "Raikage" "Your blind trust in the rest of this forsaken world is exactly what makes you weak!" with vpunch
    "Raikage" "I'd bet you the other nations would gladly join my initiative to see Konoha burn to the ground. In fact..." with vpunch
    show rai_naru 1_2 with dissolve:
        yalign 0.4
    "Raikage" "Your very own lord Daimyo is deeply involved in my plans!"
    na"Explain yourself..."
    "Raikage" "Baaa-ha-ha!" with vpunch
    "Raikage" "What kind of strategist would share their secrets with the enemy you fool!"
    scene rai_naru 1_1_serious with dissolve:
        yalign 0.4
    "Raikage" "Although now that I think about it, there is something of yours I'd like for you to share with me." with vpunch
    "Raikage" "Do that, and I'll share my secrets in return."
    na"..."
    scene rai_naru 1_1_smirk with dissolve:
        yalign 0.4
    "Raikage" "She's been alone for quite some time now, hasn't she?" with vpunch
    na"She...?"
    scene v20_rai_naru 1_0 hina with dissolve:
        yalign 1.0
    show v20_rai_naru 1_0 hina:
        easein 6 yalign 0.1
    "Raikage" "She was always quite the looker that one." with vpunch
    "Raikage" "I wonder if she kept growing in all the right places since the last time I've laid eyes on her."
    "Raikage" "Those curves... that soft skin... I bet she still blushes when a man looks at her the right way."
    scene rai_naru 1_1_smirk with dissolve:
        yalign 0.4
    "Raikage" "You'll share your wife with me, and I'll share my secrets about Konoha's imminent annihilation!!" with vpunch
    scene rai_naru 1_1_angry with dissolve:
            xalign 0.0 yalign 0.2
    $ renpy.sound.play("/audio/soun_fx/eye4s.opus", channel="sfx1", loop=False, relative_volume = 0.3)
    na "Touch my wife, or my family, and I'll rip you to pieces myself you bastard!" with Shake((0, 0, 0, 0), 2, dist=20, peak_time=0.8, smoothness=50)
    scene rai_naru 1_2 with dissolve:
        yalign 0.4
    "Raikage" "Bwaaa-ha-ahha! Relax, big man... Can't even take a little banter nowadays?" with vpunch
    "Raikage" "Despite my uuuh, reputation... I am quite the faithful man if I do say so myself!"
    "Raikage" "Although I'll admit. Your wife does have an effect on me, if you catch my drift!" with vpunch
    scene black
    $ renpy.sound.play("/audio/soun_fx/chain_rattle3.opus", channel="sfx1", loop=False, relative_volume = 1.0)
    "Raikage" "Bwaaa-ha-ha!" with vpunch
    $ renpy.sound.play("/audio/soun_fx/chain_rattle1.opus", channel="sfx1", loop=False, relative_volume = 1.0)
    na"Bastard..."
    "Raikage" "Samui! Suni! Show yourselves..."
    scene v20_samui2 with dissolve:
        yalign 1.0
    show v20_samui2:
        easein 5 yalign 0.0
    "Samui" "Hai!" with vpunch
    "Raikage" "Our 'guest' here is growing impatient. Please recite your mission in a concise manner." with vpunch
    
    "Samui" "Yes, my lord! Our mission as it stands is to infiltrate Konoha under the guise of a diplomatic cultural exchange program."
    "Samui" "Young Suni and I are to be housed within the Hokage's household as part of the 'Strengthening Inter-Nation Relations' initiative."
    scene rai_naru 1_1_angry with dissolve:
        yalign 0.4
    "Raikage" "And the best part? Your own council approved this 'cultural exchange' unanimously!" with vpunch
    "Raikage" "They were so eager to appear progressive and cooperative that they didn't even question the details."
    na "You won't get away with this!"
    scene v20_samui2 with dissolve:
        yalign 0.0
    "Suni" "We will be the perfect house guests, Lord Hokage. Polite, helpful, eager to learn about your 'ways'."
    scene v20_samui2_1 with dissolve:
        yalign 0.0
    $ renpy.sound.play("/audio/soun_fx/groperepeat1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    show screen image_with_border("v20_v20_samui_boxgrope",0.3,0.0,0.0) with dissolve
    "Suni" "Your wife, your daughter, they will grow quite fond of us, I'm sure. Women like them are so nurturing, so trusting..." with vpunch
    "Suni" "Isn't that right, Samui-san?" with vpunch
    "Raikage" "Suni! Do not lose focus..."
    hide screen image_with_border with dissolve
    "Suni" "Yes, of course. Father..."
    "Raikage" "That'll be all then."
    "Raikage" "Samui! Protect my son with your life if you must. Suni, remember your true mission..."
    "Samui" "Hai!"
    "Raikage" "You are dismissed. Your mission is now underway!"
    play sound "audio/soun_fx/fast_blink.opus" volume 0.8
    scene black with flash
    show rai_naru 1_2 with dissolve:
        yalign 1.0
    show rai_naru 1_2:
        easein 4 yalign 0.1
    na"Whatever shitty machinations you've come up with, there's two of my own back home to put a stop to them..."
    "Raikage" "My son, against your offspring! Things are getting interesting, aren't they Hokage!"
    $ renpy.sound.play("/audio/soun_fx/intro/evilmenlaugh.opus", channel="sfx2", loop=False, relative_volume = 0.3)
    scene black with dissolve
    scene v20_samui1 with dissolve:
        yalign 1.0
    show v20_samui1:
        easein 4 yalign 0.2
    "Suni" "'Mama... mama, can I put it in yet'? Hee-hee! Aren't we practically like mother and child now?"
    "Samui" "That's enough!" with vpunch
    scene v20_samui2_2 with dissolve:
        yalign 1.0
    show v20_samui2_2:
        easein 5 yalign 0.0
    "Samui" "Do not mistake me for a harlot for you to do as you please with."
    "Samui" "As the Raikage's heir, I owe you my life, not my body. Understood?"
    "Suni" "Haaaai, mama! *Devious giggle* Hehehe!"
    scene black with dissolve
    show v20_samui3_0 with dissolve:
        yalign 1.0
    show v20_samui3_0:
        easein 6 yalign 0.0
    "Suni" "Save some of that horn-dog energy of yours for the task at hand."
    "Suni" "Now get moving! The trip to Konoha will take us weeks..."
    scene black
    show v20_samui3_1 with flash:
        fit "contain" xalign 0.5
    "Suni" "Follow me! Don't fall behind..."
    scene black with dissolve
    return