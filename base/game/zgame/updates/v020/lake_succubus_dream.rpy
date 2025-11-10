default succubus_seen = False
default succubus_bargain_accepted = False

label lake_succubus:
    $ initialize_replay_defaults()
    $ renpy.sound.play("/audio/soun_fx/wind3.opus", channel="sfx3", loop=False, relative_volume = 0.8)
    show bg_lake_1 at brightreveal
    show boruto normal at center,brightreveal
    with flash
    bot "..."
    bot "Where am I?"
    bot "It feels... wet. And cold."
    if tenten_date_seen == True:
        bot "Is this the lake where me and Tenten...?"

    show blackscreen with dissolve
    "In the distance, you notice a slender, dark figure, laying on the lake's surface."
    "As you try to get closer, your perspective shifts to a bird's eye view."
    
    scene p1 with dissolve:
        zoom 1.19 yalign 0.5 xalign 0.5 subpixel True
    show p1:
        easein 5 subpixel True yalign 0.2

    bot "W-what on earth is that? How is she staying afloat in that position?"

    "Rumor has it, under a full moon's glow, when the sky is stretched dark and starless, a Succubus is summoned bearing cross-shaped earrings."
    "Her skin, fair as an angel’s and soft as a feather’s touch, shined under the lunar light."
    "Slightly unkempt brown bangs hanged across her forehead, a teasing veil that concealed the wicked secret behind her innocuous appearance."

    bot "Is she NAKED?! I need to get a closer look..."

    scene black with dissolve

    "As soon as you start walking forward, you notice several figures emerging from the woods."

    bot "Why are they walking towards her like zombies? And why are they all naked?"

    "Suddenly, the men swarm all over her and start using her."

    show p1_1 with dissolve
    $ renpy.sound.play("/audio/soun_fx/bjair1.opus", channel="sfx1", loop=False, relative_volume = 1.2)
    "Through sheer subconscious will your feint vision shifts to a different perspective, as if to satisfy your rising arousal."

    "Random Men" "I can't believe it! The stories we've heard are true, she'll do anything we ask of her!"

    bot "W-woah, I can't actually tell if my condition is making stuff up or if all this is real!"
    bot "Look at how expertly and eagerly she handles multiple men at once... She can't be human!"
    bot "If this was just my condition reacting why would it create {b}this{/b}, of all things?"

    "Beneath her bangs, shined through a sinful gaze." 
    "Her brown, glowing eyes stared straight into the souls of her victims during each and every depraved act they frantically partook in."
    "Men lucky, or unlucky enough to stumble upon her would quickly discover that behind her carefully crafted seductive form, lied a sex-crazed woman." 
    "...and she would stop at nothing to drain the essence of her ignorant victims, straight from its source."
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/Succubus_Deranged_Reverb.opus", channel="sfx1", loop=False, relative_volume = 1.2)
    "Succubus of the Lake" "More... I need, MORE!"

    "You start getting creeped out."

    bot "There's no way I'm just making this up..."
    if tenten_date_seen == True: 
        bot "And why does she look like ...h-her?"

    "Once again your cloudy vision shifts to a different point in time."
    scene black
    show p2
    with dissolve
    $ renpy.sound.play("/audio/soun_fx/panting.opus", channel="sfx1", loop=False, relative_volume = 1.2)
    "You begin to wonder..."
    "Is this still just your imagination or is it a premonition?"
    if tenten_brain_damage == True:
        bot "This... Is this a reflection of when I almost drowned Tenten facefucking her at the lake?"
        bot "Am I being warned of some kind of punishment?"
        bot "There's no way this has anything to do with her, Tenten is a little bitch. But the resemblance is... uncanny."

    "Random Men" "The rumors were true! We have to tell the others!"
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/Succubus_Deranged_Laugh_Reverb.opus", channel="sfx1", loop=False, relative_volume = 1.2)
    "Stories of a sex-crazed Succubus spread like wildfire."
    "Soon enough, every man of the village had to see with their own lust-filled eyes if the rumors they'd heard were true..."

    show p3 with dissolve
    $ renpy.sound.play("/audio/soun_fx/handjob4.opus", channel="sfx1", loop=False, relative_volume = 1.2)
    "Random Man" "Hurry up, It's my turn next! She'll vanish when the sun rises!"

    "Lured in by the siren's song, men from across the lands would gather."
    "The Succubus's devilish smile taunted the crowd, inviting those brave enough to try and claim her, perhaps all at once!"
    "It didn't matter who, or how. Farmer, merchant, or wanderer..."
    "She would happily devote herself to every man's most depraved fantasies, indulging their every desire, while secretly absorbing their essence."

    bot "Are they using her or is she... using them?"
    scene black
    show p4
    with dissolve
    $ renpy.sound.play("/audio/soun_fx/panting.opus", channel="sfx1", loop=False, relative_volume = 1.2)
    "There she lay, hours into the morning, sprawled across the lake, her skin shining with the slick remnants of every man's essence."
    "Hundreds had taken her, but so did she, take something from them..."
    "With every kiss, every fevered caress, she drank the men in, their essence, secretly absorbed."
    $ renpy.sound.play("/audio/soun_fx/Succubus_Deranged_Giggle_Reverb.opus", channel="sfx1", loop=False, relative_volume = 1.2)
    "It flowed into her like rivers of molten gold, feeding her power, filling her with ecstasy."

    menu:
        "Do you need help?":
            bo"Do you need help?"
            bo"..."
            bo"Hello?"
            bot"She's not responding..."
            bot"Now that I think about it, none of the men reacted to my presence."
            bo"WHY IS EVERYONE IGNORING ME?!"

    scene black with dissolve
    "Just before the sun rose, a curious bunch stumbled upon the Succubus giggling to herself."

    show p5 with dissolve
    $ renpy.sound.play("/audio/soun_fx/Succubus_Soft_Laugh_Reverb.opus", channel="sfx1", loop=False, relative_volume = 1.2)
    "She lounged there, laughing softly, her glowing eyes still lit-up with mischief."

    bo "I better get out of here, I've got a bad feeling about this."

    $ renpy.sound.play("/audio/soun_fx/Succubus_Last_Dance.opus", channel="sfx1", loop=False, relative_volume = 1.2)
    "Succubus of the Lake" "One last dance?"
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/Succubus_Deranged_Laugh_ReverbDelay.opus", channel="sfx1", loop=False, relative_volume = 1.2)
    "Her giggles echoed throughout the lake."


    "The men hesitated, sensing the danger, but her allure was a chain they couldn’t break."
    "They fell upon her, lost in the heat of her embrace."
    "With each thrust, each ragged moan, she siphoned the last drops of their vitality."

    "After all, every drop of their essence grew her powers further, while leaving the men impotent for the rest of their lives..."

    scene p1 with dissolve:
        zoom 1.19 yalign 0.5 xalign 0.5 subpixel True
    show p1:
        easein 5 subpixel True yalign 0.2

    "Such was the curse of the Succubus of the Lake."

    scene black with dissolve
    
    bot "God damn it, my gut feeling was right after all, I better get out of here."

    "As you slip in and out of consciousness, she notices you, and through the veil of the dream she looks straight at you:"

    show p5 with dissolve
    "..."
    $ renpy.sound.play("/audio/soun_fx/eye2.opus", channel="sfx1", loop=False, relative_volume = 1.2)
    show p5_1 with flash:
        yalign 0.3, xalign 0.5
    bo "WHAT THE HELL!" with vpunch
    "Succubus of the Lake" "What about you, will you take my bargain?"

    menu:
        "Accept the bargain":
            $ succubus_bargain_accepted = True # Can affect future story/options
            bo"Fine, let's see what you got!"
            bo"..."
            bo"So... Are you gonna 'drain my essence' too now or what?"
            bo"I volunteer as tribute!"
            $ renpy.sound.play("/audio/soun_fx/Succubus_Deranged_Laugh4.opus", channel="sfx1", loop=False, relative_volume = 1.2)
        "Run away":
            $ renpy.sound.play("/audio/soun_fx/Succubus_Deranged_Laugh4.opus", channel="sfx1", loop=False, relative_volume = 1.2)
            bo"STAY AWAY FROM ME YOU SEX-CRAZED FREAK!" with vpunch
    $ renpy.sound.play("/audio/soun_fx/wakeup.opus", channel="sfx3", loop=False, relative_volume = 0.6)
    scene bo_wakeup_during_dream at brightreveal:
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.05)*HueMatrix(0.0) 
    with longerflash
    with Shake((0, 0, 0, 0), 1, dist=20, peak_time=0.8, smoothness=50)
    $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx2", loop=False, relative_volume = 0.4)
    $ renpy.end_replay()
    bot"*Rapid breathing* What the... f-fuck!?"
    call increaselust(50) from _call_increaselust_268
    "You woke up in the middle of the night naked, drenched in sweat, with a violent erection smearing your bedsheets..."
    scene black with vpunch
    bot"Damn it! This fucking curse is driving me crazy!"
    "You fetch some underwear and try to get back to sleep..."
    bot"Was that... Tenten? Why would I dream of something like that?"
    $ renpy.end_replay()
    jump action_taken
    $ succubus_seen = True