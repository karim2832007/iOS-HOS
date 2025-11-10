# v0.19 Tsunade Discovery Defaults
default tsunade_discovery_seen = False
default tsunade_discovery_sub_repeats = 0
default tsunade_discovery_dom_repeats = 0

label tsunade_discovery:
    # Event triggered when semenquantity >= 30 and tsunade_discovery_seen == False.
    # Tsunade explains her findings about the semen properties.

    # Set flag to prevent re-triggering
    $ tsunade_discovery_seen = True

    # Standard repeatable visit
    scene bg infirmaryinside with dissolve
    show boruto worried at center with dissolve
    bot"I should make my way to her office..."
    hide boruto with dissolve
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/doorknock.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    ts"Come in..."
    scene bg infirmary room day
    show boruto sceeming at left 
    show tsuna normal at right
    with dissolve
    show screen infirmarymenutopright with dissolve
    ts"I was expecting you..."
    show tsuna serious with dissolve
    show boruto surprised2 with dissolve

    ts "[bo_name], we need to talk. My research..."
    ts "It's yielded some significant results regarding your condition."
    bo "Results? What kind of results?"
    show boruto worried with dissolve
    ts "The samples you've provided... your semen..."
    ts "It possesses properties far beyond what I initially anticipated. Properties that are frankly..."
    ts "Alarming." with vpunch

    bo "Alarming? What do you mean?"
    ts "Firstly, the rate at which it seems to influence cellular regeneration suggests... accelerated conception." 
    ts "Pregnancies initiated through contact could progress at an unnatural speed."
    show boruto surprised3 with dissolve 
    bo "A-accelerated pregnancy? You mean...?"
    ts "It is exactly what you think it is."
    
    menu tsunadediscovery_childsupport:
        ts "It is exactly what you think it is."

        "We could test how that plays out with you!":
            call changeDominance(1) from _call_changeDominance_112 
            show boruto snob with dissolve
            bo "Surely you'd like to find out how that plays out!"
            bo "Me and you, we could, you know..."
            show tsuna angry with dissolve
            call changetsunadedominance(-1) from _call_changetsunadedominance_25
            ts "Watch your tone, brat. This is serious! Drop the pointless insinuations and pay attention.."


        "Am I going to be a father!?":
            show boruto worried2 with dissolve
            bo "Wait, are you saying... someone could actually get pregnant that fast? And I'd be responsible?"
            ts "The potential is there, yes. Which is why it's so critical for you to-"
            bo "B-but... I'm already busting my ass off day in day out at the ramen shop as it is! There's no way I'd be able to father children too!" with vpunch
            #bot "I... I knew it... Nice guys do finish last after all..." #?
            ts"Then pay attention to what I am saying, and don't interrupt me! *Sigh...*" with vpunch 


    show tsuna annoyed with dissolve
    ts "Secondly, and perhaps more concerning, are the potential psychoactive effects."
    ts "Not just on you, but on anyone who... interacts with it."
    show tsuna serious with dissolve 
    bo "Psychoactive? Like... drugs?"
    ts "The preliminary analysis shows similarities." 
    ts "It seems to induce a state resembling dependency or addiction in those exposed, potentially influencing their thoughts and actions towards seeking further exposure."
    ts "This includes you, [bo_name]. Your own urges might be amplified or altered by this property."
    show boruto worried2 with dissolve 
    bo "So... it's dangerous? To me and... others?"

    # Add Tenten-related thoughts based on relationship status
    if tenten_date_counter > 0 and tenten_extorted == False:
        bot "Addiction...? Shit... Is that why Tenten nags me about it every time I visit the damn shop?" 
    elif tenten_extorted == True:
        bot "Addictive, huh? Maybe that's why she was so easy to push around after I... persuaded her. Interesting." #She? Who? The player doesn't know what you are alluding to.

    ts "The full extent is still unknown, but the potential for misuse, and unintended consequences is immense."
    ts "We must exercise extreme caution moving forward."
    ts "Which brings me to my next point..."
    show boruto surprised2 with dissolve
    bot "Here we go..."
    show tsuna angry with dissolve 
    ts "From now on, any 'treatment' sessions, whether with me or... anyone else, absolutely require protection."
    if tenten_extorted == True:
        bot "Well... Maybe you could've told me so before I had Tenten suck me dry..."
    elif tenten_date_counter> 0:
        bot "Luckily, I haven't gone all the way through with Tenten yet, or anyone for that matter. Phew!"
    label repeat_tsunadediscovery: #jump here
    ts "Given my findings, condoms are no longer optional, they are mandatory. Understand?"

    menu tsunade_condom_optional_menu:
        ts "Condoms are no longer optional, they are mandatory. Understand?"

        "Y-yes, I understand.":
            show boruto worried with dissolve 
            bo "Okay... Okay, I get it. Condoms. Always."
            ts "Good. This is not something to be taken lightly."
        "Are you serious? That ruins the fun...":
            bo "Seriously? Condoms? Doesn't that kinda... kill the mood?"
            show tsuna angry2 with dissolve 
            ts "This isn't about 'mood', you idiot! This is about preventing potentially catastrophic consequences!" with vpunch
            call changetsunadedominance(1) from _call_changetsunadedominance_26
            ts "Addiction, accelerated pregnancies you can't handle... Get that through your thick skull!"
            bo "Alright, alright! Fine. Condoms. I get it."
        "{color=[dominancecolor]}Are you going to provide them then?{/color}":
            call checkDominance(15,"tsunade_condom_optional_menu") from _call_checkDominance_40
            show boruto snob with dissolve 
            call changeDominance(1, "tsunade_discovery_condom_demand") from _call_changeDominance_113
            bo "Mandatory, huh? Does that mean the esteemed Lady Tsunade will be providing the equipment for these 'treatments'?"
            show tsuna annoyed with dissolve 
            call changetsunadedominance(-2) from _call_changetsunadedominance_27
            ts "Don't get smart with me, brat. Yes, I will ensure protection is available here..."
            show boruto normal with dissolve
            ts "What you do outside this office is your responsibility, but I strongly advise you take precautions."
            
    show tsuna normal with dissolve 
    ts "Now... despite my discoveries, the need for managing your condition remains." 
    ts "And my research still requires samples, albeit collected safely."
    ts "I assume you came here for a reason, correct?"
    ts"Today, things will be slightly different given the circumstances..."

    # Check tsunadedominance to determine the treatment path
    if tsunadedominance >= 0: 
        jump tsunade_discovery_treatment_sub
    else: 
        jump tsunade_discovery_treatment_dom

# --- Submissive Path Treatment ---
label tsunade_discovery_treatment_sub:
    $ semendtoadd = 0
    if tsunade_discovery_sub_repeats == 0:
        show boruto worried with dissolve:
            xalign 0.0
        bo"So... this is the new norm? Always... protected?"
        show tsuna annoyed with dissolve
        ts"The data is unambiguous, [bo_name]. The risks are severe. Will I have to keep repeating myself?"
        ts"Your condition now mandates stringent safety protocols."
        bo"But what about the sensatio-"
        ts"This is non-negotiable!" with vpunch
        show tsuna serious with dissolve
        ts"I will oversee this procedure. You will comply. No questions asked..."
        show boruto angry with dissolve
        bot"Fantastic. Just what I needed. A cursed cock and now mandatory rubber training sessions."

        menu tsunade_discovery_sub_intro_menu:
            ts"Do you comprehend the absolute necessity of these precautions?"

            "Yes, Lady Tsunade. Safety first.":
                show boruto worried with dissolve
                bo"Y-yes, Ma'am. I understand. No risks."
                show tsuna normal2 with dissolve
                call changetsunadedominance(1) from _call_changetsunadedominance_28
                ts"Memorize that principle. Strict adherence is crucial."

            "It just feels... weird.":
                bo"But... condoms every time? It feels so... weird, like I'm some kind of guinea pig."
                show tsuna angry with dissolve
                call changetsunadedominance(2) from _call_changetsunadedominance_29
                ts"How you feel, is a luxury we cannot afford! Preventing catastrophe is the priority!" with vpunch
                show boruto surprised with dissolve
                ts"Would you prefer accidental, hyper-speed fatherhood? Or potentially enslaving someone to your biological cursed conditions? Focus!"
                show boruto worried with dissolve
                bot "I guess she's right..."
                show boruto angry with dissolve
                bot "Unless all this stuff is an elaborate ruse for her to use me as a toy!"
                show boruto worried with dissolve
                bot "No, Lady Tsunade isn't like that... r-right?"

            "{color=[dominancecolor]}Enough lectures...{/color}":
                call changeDominance(1, "tsunade_discovery_sub_equip") from _call_changeDominance_114
                show boruto snob with dissolve
                bo"Okay, okay. Less lecturing, more procedure...ing! Tell me what you need me to do, Lady Tsunade."
                show tsuna annoyed with dissolve
                ts"Don't get sassy with me little runt, or you won't like what comes next."
                show boruto sceeming2 with dissolve
                bo"Oh so you're saying you'll let me have a good time if I comply huh?"
                ts"You're pushing your luck, [bo_name]."
                call changetsunadedominance(-2) from _call_changetsunadedominance_30
                ts"Your impatience is noted, yet largely irrelevant."
                show boruto angry with dissolve

    label tsunade_discovery_treatment_sub_repeat:
    $ initialize_replay_defaults()
    ts"Strip. Bed. Move, NOW!" with vpunch
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.8)
    "Her tone leaves no room for arguing. You comply quickly, removing your clothes and settling onto the examination bed. Despite the unwelcoming atmosphere and warnings, your body reacts in arousal."
    "Tsunade approaches with a condom packet in hand, clinical focus etched onto her face."
    "She sits on the bed's edge, positioning herself between your legs."
    show screen parallax1280("tsunadiscsub_1",1.25,0.3) with dissolve
    call showscrollingimage from _call_showscrollingimage_158
    "She teared open the packet, revealing a pink condom. With surgical precision, her fingers grasp your erection and unroll the condom over it." 
    "Her touch sends an involuntary tremor through you."
    ts"Absolute stillness is required. Any erratic movement could compromise the integrity of the barrier."
    # tst"Maintain procedural detachment. Focus on sterile application. Emotional factors are secondary."
    bo"I am t-trying..."
    ts"Control yourself, [bo_name]. This demands meticulousness."
    "Almost unconsciously, your hands drift upwards, instinctively seeking to grab on to something..."
    ts"And remember, I am in control, you maintain your distance! This is a controlled medical extraction, not foreplay!" with vpunch
    ts"Your full compliance is expected!" with vpunch
    menu tsunade_discovery_sub_menu_1_condom:
        ts"Your full compliance is expected!"

        "Yes Ma'am!":
            bo"Yes Ma'am! I am in your c-care..."
            "She gives a short nod, accepting your quick submission."
            bo"It's just... strange. Like I'm nothing more than a sample source."
            ts"In this specific context, you {b}are{/b} the source of a highly volatile biological agent. Subjective feelings are secondary to risk mitigation."
            ts"Concentrate on the necessity of this procedure."

        "{color=[dominancecolor]}Reach for what must be grabbed!{/color}":
            call checkDominance(20, "tsunade_discovery_sub_menu_1_condom") from _call_checkDominance_41
            bo"Maintain distance... 'Lady' Tsunade? You know about my condition better than anyone..."
            call changeDominance(1) from _call_changeDominance_115
            show screen parallax1280("tsunadiscsub_1_1",1.25,0.3) with dissolve
            bo"And likewise, I know about your depravity too! Be honest, this is what you enjoy, right?" with vpunch 
            call changetsunadedominance(-3) from _call_changetsunadedominance_31
            ts"W-what?! Don't be absurd! Maintain protocol! This isn't a game..."
            bo"Your squishy badonkers certainly say otherwise!" with vpunch
            show screen parallax1280("tsunadiscsub_1",1.25,0.3) with dissolve
            ts"That's enough! Hands off or I swear, your dismembered prick will be easier to examine..."
            bo"R-right. S-scary."
            bot"I'd rather save my cock for now! Crazy bitch..."
            ts"Your lack of discipline is... problematic! Stop trying to blame your condition to excuse your disobedience!"

    scene black with dissolve
    call hidescrollingimage2 from _call_hidescrollingimage2_115
    "Maintaining control, Tsunade adjusts her position. She lets her weight fall over you, and makes herself comfortable onto your stomach with complete disregard."
    hide screen parallax1280
    show screen parallax1280("tsunadiscsub_2",1.25,1.0) with dissolve
    call showscrollingimage from _call_showscrollingimage_159
    ts"Knowing your tendencies, this revised orientation enhances the amount of control I have over you during the procedure, which given the risks we discussed, is necessary."
    bo"E-enhanced... *Struggles to breathe* control?"
    show screen parallax1280("tsunade_disc1_thighsanim_1",1.25,1.0) with dissolve
    ts"Precision is vital! I must observe the barrier's reaction dynamics throughout the stimulation phase." with vpunch
    "Tsunade started shifting her lower body's weight around ever so slightly, occasionally squeezing the tip of your cock between her thighs."
    bo"R-right... *Wheezing*"
    bot"'Reaction dynamics'. Sure thing... Her sitting almost square on my cock and rubbing her ass on it has nothing to do with anything else." 
    bot"T-though the heat from her thighs... even through this stupid rubber. I am r-rock fucking hard!"
    call increaselust(20) from _call_increaselust_238
    "Even muted by layers of clothing and latex, the direct pressure, friction and heat omitting from her heavy body, dominating yours, was enough to send you."
    ts"Proximity is a procedural requirement. Give yourself to me, and through simple friction, along with the thermic energy I am emanating, we can achieve the desired result."
    ts "It's important to test the rubber's endurance to your semen's peculiar properties. If the barrier doesn't hold, then we'll have to revise."

    scene black with dissolve
    call hidescrollingimage2 from _call_hidescrollingimage2_116
    ts"This is more troublesome than I thought..."
    ts"On your feet, [bo_name]!" with vpunch
    "Time seems to stretch and compress. Tsunade orders you to stand on your feet, and decides to change her approach..."
    hide screen parallax1280
    show screen parallax1280("tsunadiscsub_4",1.25,0.15) with dissolve
    call showscrollingimage from _call_showscrollingimage_160
    ts"It appears you keep producing semen throughout the process, the barrier still holds. Good..."
    ts"But you aren't yet there..."
    show screen parallax1280("tsunade_disc1_hjanim_1",1.25,0.15) with dissolve
    ts"Are you?" with vpunch
    bo "N-not... y-yet!"
    bot "Her hand.. Will this condom hold? I can already imagine myself exploding through the latex."
    ts"Your physiological arousal response remains remarkably potent, [bo_name], even when significantly dampened by the mandated barriers."
    bot"Barriers..."
    bo"By the way, I think it's called a cond-"
    show screen parallax1280("tsunade_disc1_hjanim_2",1.25,0.15) with dissolve
    ts"Shut it!" with vpunch
    "Tsunade picks up the pace and squeezes your cock harder than before..."
    ts"Fascinating. The inherent biological drive appears exceptionally resilient."
    bo"*Moans* I-it's... a bit p-painful w-when you..."
    call changetsunadedominance(1) from _call_changetsunadedominance_32
    ts"Irrelevant. Pain may be part of the process. You'll learn to enjoy that part too in due time."
    bot"E-enjoy... the pain? She's a lunatic..."
    bot"Feels like getting wanked with a dish glove. F-fuck this curse..."
    ts"Detachment must be maintained. The objective is controlled seminal expulsion entirely contained within an intact barrier."

    menu tsunade_discovery_sub_menu_2_condom:
        ts"Detachment must be maintained. The objective is controlled seminal expulsion entirely contained within an intact barrier."

        "Okay... Objective. Control. Barrier intact.":
            bo"Right... Barrier. Safe sample. Understood."
            ts"Precisely. Prepare for the manual stimulation phase."
            bo"M-manual stimulation? You mean like, I rub one out?"
            ts"No! The risk is too high for someone like you to handle it by themselves"
            ts"That is precisely why a medical professional such as myself has to take control and guide the process."
            bot"So she says, but at this point who's to say she's not just using me to satisfy her weird perverted kinks..."

        "{color=[dominancecolor]}(Fantasize) What if we swapped places...{/color}":
            call checkDominance(20, "tsunade_discovery_sub_menu_2_condom") from _call_checkDominance_disc_sub_2
            bo"W-what if, we swapped places. It c-could help the process be much f-faster..."
            ts"Explain yourself." with vpunch
            bo"Is there really a need for such excessive blue-balling, Lady Tsunade?"
            bo"How about I sit on the bed, and you instead..."
            show screen parallax1280("tsunadiscsub_4_3",1.25) with flash
            call changeDominance(1) from _call_changeDominance_116
            bo"You get down on your knees and use more than just your hands! You know what I mean?"
            bot"Hehe! Just thinking about it gets me going..."
            show screen parallax1280("tsunade_disc1_hjanim_2",1.25) with flash
            ts"Snap out of your fabled delusions. That will never happen..." with vpunch
            ts"I, am in command. This requires precise calibration, not recklessness!"
            ts"Your opinions on procedural technique are neither solicited, nor required."
            call changetsunadedominance(-2) from _call_changetsunadedominance_33
            ts"And if you truly care about the condition of your m-measly genitals, you'll stop questioning me, or my methods..."

    scene black with dissolve
    call hidescrollingimage2 from _call_hidescrollingimage2_117
    ts "Now it's nigh time we wrap this up."
    $ renpy.sound.play("/audio/soun_fx/intro/jerkoff2.opus", channel="sfx2", loop=False, relative_volume = 0.4)
    show screen parallax1280("tsunadiscsub_6",1,1.0) with dissolve
    call showscrollingimage from _call_showscrollingimage_161
    "Tsunade yanks on your cock, forcing you onto the bed, closer to her..." with vpunch
    show screen parallax1280("tsunade_disc1_hjanim_3") with dissolve
    ts"Commencing enhanced stimulation. Report any perceived barrier weakness, tearing, or slippage immediately."
    "Her hand begins a fast, unrelenting, agonizingly methodical twisting motion. The sensation is frustratingly indirect, muted significantly by the layer of latex." 
    #"Yet, watching her focused expression, her brow slightly furrowed in concentration, stirs the potent beast within you." #wtf
    bo"I am c-close...!" with vpunch
    ts"Anticipated. Barrier still holds. Endure the process..."
    bo"I... c-cant!" with flash
    #move after act if nescessary
    # bo"L-lady Tsunade... this might sound crazy, but..."
    # bo"Are you *sure* these things are helping?"
    # bo"It's like... the thing afflicting me *knows* we're trying to box it in, control it."
    # bo"And it doesn't like it. Not one bit."
    # bo"What if... what if trying to suppress it like this just makes it... angrier? More depraved?"
    # bo"Like it's fighting back against the restraint? Making things worse for... well, for anyone who has to deal with it?"
    # ts"That's... a disturbing thought, [bo_name]. But purely speculative."
    # ts"We operate based on the tangible risks we've identified - accelerated conception, psychoactive influence."
    # ts"Containment is the only logical course until we understand more. Attributing intent or rebellion to it... that's a dangerous path."

    scene black with dissolve
    call hidescrollingimage2 from _call_hidescrollingimage2_118
    "She shifted her position once more, kneeling on the mattress..."
    hide screen parallax1280
    show screen parallax1280("tsunadiscsub_7_1", 1, 0.15) with dissolve
    call showscrollingimage from _call_showscrollingimage_162
    $ renpy.sound.play("/audio/soun_fx/intro/jerkoff2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    "The kneeling posture allowed for full control, and clear observation. It felt strangely submissive."
    "Her gaze was fixed intently on the condom, assessing its safety under the increasing pressure."
    # bot"Is she indicating that it's my chance to take control?"
    # bo"L-lady Tsunade? Am I f-finally allowed to... T-touch?"
    # ts"Be quiet! The shift in posture is necessary to ensure the barrier will hold!" with vpunch
    # ts"Don't get any ambitious ideas!"
    # tst"Subject's arousal escalating. Barrier demonstrating expected tensile strength. Pace can be moderately increased without compromising integrity."
    show screen parallax1280("tsunade_disc1_hjanim_4", 1, 0.15, menuenabled=True) with dissolve
    $ renpy.sound.play("/audio/soun_fx/intro/jerkoff2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    "Her hand moves fractionally faster, the friction building steadily, evoking a powerful groan from deep within your chest." with flash

    ts"Remarkable erection strength, [bo_name]. The drive persists despite significant sensory dampening."
    bo"It's y-you... It's always you, L-lady Tsunade, that m-makes it..."
    ts"Silence!" with vpunch
    $ renpy.sound.play("/audio/soun_fx/intro/jerkoff2.opus", channel="sfx2", loop=False, relative_volume = 0.6)
    ts"Prepare for culmination! Expel without hesitation!"

    menu tsunade_discovery_sub_menu_3_condom:
        ts"Prepare for culmination! Expel without hesitation!"

        "Fill the condom!":
            bo"Please, Tsunade! Just... *Moans*... End this p-procedure!"
            ts"Barrier integrity is paramount! Do not compromise the protocol!"
            show screen parallax1280("tsunade_disc1_hjanim_4_1", 1, 0.15) with dissolve
            "She increases the pace marginally, balancing safety against your building desperation."
            call changetsunadedominance(2) from _call_changetsunadedominance_disc_sub_8
            $ renpy.sound.play("/audio/soun_fx/intro/jerkoff2.opus", channel="sfx2", loop=False, relative_volume = 0.7)
            ts"Release authorized! Now, [bo_name]!"
            bo"I... Can't h-hold it any longer! I am c-cumming!" with flash
            scene black with dissolve
            call hidescrollingimage2("Click twice to erupt!") from _call_hidescrollingimage2_119            
            $ renpy.sound.play("/audio/soun_fx/cum7.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            show tsunadiscsub_7_cum with flash:
                yalign 0.3
            "A powerful, shuddering climax rips through your body, intensely focused yet strangely muffled, contained entirely within the strained confines of the latex barrier."
            "The condom instantly clouds white, visibly filled with your potent release. The peak sensation slams into you, but the usual messy aftermath is absent, trapped within the rubber."
            ts"Is that... all of it?"
            ts"Dissapoin-"
            $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            show tsunadiscsub_7_cum2 with longerflash:
                yalign 0.3
            call decreaselust(50) from _call_decreaselust_disc_sub_2
            $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx2", loop=False, relative_volume = 0.4)
            bo"D-damn it... *Panting*" with vpunch
            tst"My days! What's with this obscene smell, the amount of it too..."
            scene black with dissolve
            ts"Satisfactory..."
            "Tsunade observes the contained result with a detached, almost clinical satisfaction. A slight nod."
            ts"Culmination achieved successfully. Barrier integrity maintained throughout expulsion. Optimal outcome."
            "With practiced, precise dexterity, she carefully removes the filled condom, efficiently knotting the end to prevent any leakage."            
            
   

    $ semendtoadd = 10
    call addSemen(semendtoadd) from _call_addSemen_4
    scene bg infirmary room day
    show boruto naked1_surprised at left:
        zoom 0.35
    show tsuna serious at right
    with dissolve
    "She places the knotted, filled condom into a sterile plastic specimen container, snapping the lid shut securely."
    ts"Lucky for you, it seems a condom can adequately protect those who engage in sexual activity with you. But..."
    ts"I do hope I've made the non-negotiable requirement for these precautions clear!"
    ts"Any deviation, any lapse in control or protocol adherence, invites potentially catastrophic consequences."

    menu tsunade_discovery_sub_menu_4_condom:
        ts"Do you finally, fully comprehend the gravity?"

        "That... was profoundly unsatisfying.":
            bo"Wow. All that buildup for... that. It felt... hollow. Empty."
            ts"Safety protocols seldom replicate the visceral thrill of uncontrolled release, [bo_name]. This is mandated by necessity, not designed for satisfaction."
            # ts"Dispose of the discarded barrier wrappers in the biohazard receptacle and dress yourself."
            call changetsunadedominance(2) from _call_changetsunadedominance_34

        "T-thank you... for ensuring it was safe.":
            bo"Uh... Thanks, Lady Tsunade. For... being so careful. I think I finally understand why now."
            show tsuna normal2 with dissolve
            ts"Comprehension is the foundation. Consistent adherence is paramount. Failure carries unacceptable risks."
            ts"Apply this same diligence should you engage in activities outside this clinic."
            call changetsunadedominance(1) from _call_changetsunadedominance_35

        "Is there truly no alternative? No cure coming?":
            bo"So this is my life now? Condoms every single time? Isn't there {b}ANYTHING{/b} else? A cure? Something to neutralize this damn stuff?"
            show tsuna annoyed with dissolve
            ts"Research into countermeasures is ongoing, but presently, meticulous containment is the only viable mitigation strategy."
            ts"Until a reliable neutralizing agent or cure is developed, this is your reality. Accept it and adapt."
            bot"So this is what it's like to have ebola... And to have a dick that shoots out ebola. And I just gotta 'deal with it'."
            bot"Great."

    ts"The procedure is concluded. Your physiological urges appear temporarily mitigated."
    ts"Clean the immediate area, dispose of the materials as directed, dress, and then vacate my office."
    ts"Report to me immediately should you experience any sudden resurgence of overwhelming urges." 
    ts"Or even if you observe any unusual behavioral changes, in yourself or others that could potentially be linked to accidental exposure."
    bo"R-right... Behavioral changes. Exposure. Got it."
    scene black with dissolve
    $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    "You dress up, before cleaning up Tsunade's office as instructed."
    "You contemplate the unsatisfying reality of the 'safe' procedure, and ponder..."
    bot"This curse... it just keeps getting more complicated the more I learn about it."
    $ renpy.end_replay()
    $ tsunade_discovery_sub_repeats += 1
    jump action_taken

# --- Dominant Path Treatment (Boruto demands, Tsunade complies with conditions) --- Not done yet
label tsunade_discovery_treatment_dom:
    if tsunade_discovery_dom_repeats == 0:


        show boruto snob at left with dissolve
        bo "So, despite all that scary talk..."
        bo "'Accelerated pregnancies', 'addiction'..." with vpunch
        bo "You still need my... 'resource', don't you, Tsunade?"
        show tsuna angry2 with dissolve
        ts "Managing your condition and continuing my research remain paramount, yes."
        ts "But the risks cannot be ignored."
        show boruto sceeming2 at left:
            easein 0.5 xalign 0.2
        bo "Risks {b}you'll{/b} have to manage while you service me."
        bo "Remember our little arrangement? My semen... your service!"
        call changetsunadedominance(-2) from _call_changetsunadedominance_discovery_dom_1
        show tsuna shy at right:
            easein 0.3 xalign 0.73
        ts "I... I remember. B-but the precautions are necessary."
        bo "Fine, fine. Condoms it is."
        bo "Now, are you going to just stand there gawking, or are you going to get on with it?" with vpunch

    label tsunade_discovery_treatment_dom_repeat:
    $ initialize_replay_defaults()
    $ semendtoadd = 0
    ts "R-right... Just... lay down on the bed."
    scene black with vpunch
    $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    "You lay back on the examination bed and undress yourself with a smirk across your face."
    show screen parallax1280("tsunadiscdom start1") with dissolve
    call showscrollingimage from _call_showscrollingimage_163
    "The familiar surge of dominance washes over you as Tsunade hesitantly approaches."
    $ renpy.sound.play("/audio/soun_fx/heels1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    "She retrieves a condom from a nearby drawer and makes her way to you..."
    ts "This... This is non-negotiable. It will be mandatory, understand?"
    show screen parallax1280("tsunadiscdom start1_1") with dissolve
    bo "Oh, I understand. But {b}you're{/b} the one putting it on me!"
    ts "W-what? Why should I-" with vpunch
    show boruto snob at right:
        easein 0.5 xalign 0.8
    bo "Because I need you to!" with vpunch
    bo "...Unless you'd prefer the alternative option of course. Hehe!"
    show tsuna annoyed at center:
        easein 0.3
    if tsunade_discovery_dom_repeats == 0:
        ts "*Tsk!* Just this once. To make sure you know how to properly apply it yourself." with vpunch
        tst "Thinking he can boss me around... Damned brat!"
    else:
        ts "*Tsk!* Again?! How hard is it to learn to do it by yourself?!" with vpunch
        tst "This damned brat... I bet he's playing stupid on purpose!"
    scene black
    call hidescrollingimage2 from _call_hidescrollingimage2_120
    $ renpy.sound.play("audio/soun_fx/condom_open.opus", channel="sfx3", loop=False, relative_volume = 0.7)
    "Tsunade kneels beside the bed, her fingers fumbling slightly as she tears open the condom packet."
    show screen parallax1280("tsunadiscdom start1_2") with dissolve
    call showscrollingimage from _call_showscrollingimage_164
    call increaselust(15) from _call_increaselust_discovery_dom_1
    "The sight of her, the legendary Sannin, forced into such a subservient act... it fuels your arousal!"
    ts"Pay attention now. It's important you observe how to properly apply protection..."
    show screen parallax1280("tsunadiscdom start1_3") with dissolve
    "She carefully takes the latex sheath and begins rolling it onto your already hardened cock."
    "Her fingers brush against your skin, sending electric shivers down your spine despite her reluctance."
    ts"See how it's rolled down all the way to the base?"
    ts"Now simply drain the air from the tip and then drag it to make sure it's not going to come off-"
    bo "See? Not so hard, was it?" with vpunch
    ts"Don't interrupt me!" with vpunch
    bo"Sorry Lady Tsunade, none of that registered. All I was paying attention to were your tits!"
    show screen parallax1280("tsunadiscdom start1_4") with dissolve
    $ renpy.sound.play("/audio/soun_fx/spank4.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    bo"O-ouch!" with vpunch
    "Annoyed by your carelessness, Tsunade let the stretched latex snap back to your tip!"
    ts"Y-you little runt... Start taking this seriously or I'll find another method to extract your damned semen!"
    bo"Or I have one of your more cooperative nurses handle this, you crazy hag!"
    ts"N-need I remind you how dangerous of a situation we find ourselves in? Stop being childish, start cooperating!"
    bo "Cooperate, Right..."
    scene black
    call hidescrollingimage2("Click twice to start 'cooperating'") from _call_hidescrollingimage2_121
    bo "In that case, now that we're all 'safe'... I think you know what comes next!"
    show tsunadiscdom_1 with flash:
        yalign 0.5 xalign 0.5 zoom 0.6
    ts "You... you still expect me to...?"
    bo "Of course." with vpunch
    bo "Your mouth worked wonders last time, even if you pretended otherwise."
    "You place your hand lightly on top of her head, guiding her gaze towards your covered erection."
    bo "Look at it, Tsunade. Right there."
    pause 0.4
    bo "Even with this stupid latex barrier... you still want it, don't you?"
    ts "D-don't be absurd..."
    bo "Your body doesn't lie. You're trembling."
    "She flinches slightly under your touch, her breath hitching."
    pause 0.6
    show tsunadiscdom_1:
        subpixel True
        easein 1 yalign 0.5 xalign 0.1 zoom 0.6 alpha 0.3
    pause 0.5
    show tsunadiscdom_2:
        yalign 0.5 xalign 0.9 zoom 0.6
    with dissolve
    pause 0.5
    bo "Enough staring. I'm getting impatient."
    "You grip her head a little firmer, rubbing her cheek against the smooth latex."
    ts"Don't just push it on my face, you i-idiot! What if the barrier slides off?"
    bo "Come on, move. Start working it!" with vpunch
    ts "Not until you shut it!"
    tst "The warmth of it, the scent alone... It's frightening how drawn I am to it."
    tst"My previous exposure to it... could it be that its effects already worked their way into my bloodstream?"
    bo"...So?"
    menu tsunade_discovery_dom_action_menu:
        ts "I... I need a moment..."

        "{color=[hatredcolor]}Don't test my patience, bitch!{/color}":
            call checkHatred(20, "tsunade_discovery_dom_action_menu") from _call_checkHatred_28
            scene black
            show tsunadiscdom_2_3:
                yalign 0.5 xalign 0.1 zoom 0.6
            with dissolve
            bo "A moment?" with vpunch
            bo "You think this thing inside me cares about 'moments'?"
            bo "You know, I noticed... with this stupid condom... it feels different."
            bo "Like that depraved thing inside me {b}knows{/b} we're trying to control it."
            bo "And it doesn't like it. Not one bit."
            bo "It gets even more... agitated. Like a form of protest, resistance."
            call changeHatred(1) from _call_changeHatred_discovery_dom_1
            show tsunadiscdom_2_3:
                alpha 0.2
            show tsunadiscdom_2_4:
                yalign 0.5 xalign 0.9 zoom 0.6
            with dissolve
            "You push your cock harder against her face, making her wince." with dissolve
            ts"H-hey. Cut it out!"
            bo "Are you sure these condoms are actually helping, Tsunade?"
            bo "Or are they just making things worse for whoever has to service me?"
            bo "Making the urges wilder? More... vicious?"
            call changetsunadedominance(-2) from _call_changetsunadedominance_discovery_dom_2
            ts "T-that's... I haven't observed-"
            bo "Now YOU shut up, and start doing something about it before I make you regret stalling." with vpunch
            jump tsunade_discovery_dom_continue_bj

        "{color=[dominancecolor]}Rub it on her face{/color}":
            call checkDominance(20, "tsunade_discovery_dom_action_menu") from _call_checkDominance_42
            call changeDominance(1) from _call_changeDominance_discovery_dom_1
            scene black
            show tsunadiscdom_3bc:
                yalign 0.5 xalign 0.1 zoom 0.6
            with dissolve
            bo "Need a moment? For what, To steel yourself? Come on Tsunade... we've been here before!"
            show tsunade_discovery_dom_rub_anim1:
                yalign 0.5 xalign 0.9 zoom 0.6
            show tsunadiscdom_3bc:
                alpha 0.2
            with dissolve
            "You begin rubbing it against her face..."
            bo"It's starting to really hurt you know..."
            ts"S-stop that, you imbecile!"
            bo"If you are not going to help, then I'll help myself..."
            ts"I thought I told you, it's dangerous! We have to proceed with caution!"
            bo "It doesn't matter how dangerous you claim this is."
            bo "You're still here, on your knees, ready to service my cock..."
            call changetsunadedominance(-2) from _call_changetsunadedominance_36
            ts"A m-medical service. That's all this is to me, and what it should be to you too."
            bo "Just accept it, Tsunade. It would make everything so much simpler."
            bo "Now, will you please... at last, open your mouth?"
            jump tsunade_discovery_dom_continue_bj

        "Just do it, Tsunade.":
            show tsunadiscdom_3bc with dissolve:
                yalign 0.5 xalign 0.1 zoom 0.6
            ts"H-hey, cut that out!"
            bo "It's s-starting to really hurt, you know..."
            bo"If you are not going to help, then I'll help myself..."
            jump tsunade_discovery_dom_continue_bj

label tsunade_discovery_dom_continue_bj:
    scene black with vpunch
    ts "S-stop that at once! I can do it myself..."
    show tsunadiscdom_4 with dissolve:
        yalign 0.5 xalign 0.0 zoom 0.6
    "She shrugs your hands away, and leans forward herself, a flicker of surprise in her eyes."
    ts"Now if we are going to do this, it has to be meticulous, calculated..."
    ts"No s-sudden movements, you got it?"
    ts"Just..."
    show tsunadiscdom_4_1:
        xalign 1.0 fit "contain"
    show tsunadiscdom_4 with dissolve:
        alpha 0.2
    with dissolve
    $ renpy.sound.play("/audio/soun_fx/sucking.mp3", channel="sfx2", loop=False, relative_volume = 1.0)
    bo"O-oh yes! Finally found your confidence, huh?"
    bo"Not sure if it's your massive tits that are more satiating, or that incredible, fat ass you try to hide!"
    tst"This d-damn smell, it's so strong, so... enticing!"
    bo"As nice as this is, the damn condom is complicating things quite a bit..."
    bo"The sensation is all but gone, Lady Tsunade..."
    scene black with dissolve
    stop sfx2 fadeout 1
    bo"I think you may have to put some more effort into it this time!" with vpunch
    "You grab her head again, much firmer this time, pulling her face off your dick and right up to your crotch."
    ts"H-hey!" with vpunch
    $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp2.opus", channel="sfx2", loop=False, relative_volume = 1.0)
    scene black
    show tsunadiscdom_5 with flash: 
        yalign 0.5 xalign 0.1 zoom 0.6
    pause 0.4
    bo "Do you mind if we make this process easier for both of us?"
    ts"W-what does that mean, [bo_name]. I told you, we have to be careful..."
    show tsunadiscdom_5: 
        alpha 0.2
    show tsunadiscdom_3a with flash: 
        yalign 0.5 xalign 0.9 zoom 0.6
    bo"Oh I'll be careful enough, Lady Tsunade..."
    bo"It's just that, at this rate your efforts may not lead us anywhere..."
    bo"No release for me, no scientific progress for you..."
    ts "So...? What is it that you are suggesting?"
    bo"Only that we pick up the pace a little. Would you mind kneeling on the floor for me...?"
    scene black with dissolve
    ts"I swear, if this is another of your stupid ideas..."
    show tsunadiscdom_6 with dissolve:
        yalign 0.5  xalign 0.1 zoom 0.71
    bo "Good." with vpunch
    "Without further warning, you shove her head down hard onto your erection."
    $ renpy.sound.play("/audio/soun_fx/gags/SDTGag11.opus", channel="sfx3", loop=False, relative_volume = 0.8)
    ts "*Gag!* Mmph!"
    "She gags as you force yourself partially into her mouth, the condom sliding against her lips."
    bot "Fuck yes... Even through the latex, this feels incredible. Maybe even better, knowing she has to work for it."
    bo "Now make sure you keep up that pace, or else my hands are here to help."
    show tsunadiscdom_7:
        yalign 0.5  xalign 0.9 zoom 0.71
    show tsunadiscdom_6:
        alpha 0.2
    with dissolve
    "Surprisingly, as you laid back she followed, leaning forward and bringing her head down on your crotch."
    $ renpy.sound.play("/audio/soun_fx/gluck1.opus", channel="sfx3", loop=False, relative_volume = 1.2)
    show tsunade_discovery_dom_bj_anim1:
        yalign 0.5  xalign 0.9 zoom 0.71
    bo "Good work Tsunade, keep that going! I always knew you had it in you..."
    ts"*Gluck gluck*" with vpunch
    bo"Those are the sounds I like to hear! The warmth of your mouth, the back of your throat getting pounded..."
    bo"if we are to be using condoms from now on... This will be exactly how you get what you want!"
    bo "Now make sure you keep up that pace, or else I'll have to to intervene..."
    $ renpy.sound.play("/audio/soun_fx/gluck2.opus", channel="sfx3", loop=False, relative_volume = 1.2)
    ts "Grrglg!" with vpunch
    bo "*Moans* Y-yes! "
    show blackscreen with dissolve
    "Tsunade keeps at it for a few minutes..."
    bo"*Groans* Keep that g-going..."
    hide blackscreen with dissolve
    $ renpy.sound.play("/audio/soun_fx/gluck1.opus", channel="sfx3", loop=False, relative_volume = 1.3)
    tst"His e-endurance is unbelievable! How much longer do I have to keep at it... My throat is getting sore!"
    menu tsunade_discovery_dom_bj_grip_menu:
        tst"His e-endurance is unbelievable! How much longer do I have to keep at it... My throat is getting sore!"
        "{color=[hatredcolor]}User her hair like handles{/color}":
            scene black with vpunch
            bo "You know what, get up here on this bed, I'll show you how it's done!"
            ts"Don't pull on my hair, you imbecile!" with vpunch
            show tsunadiscdom_3a with dissolve:
                yalign 0.5  xalign 0.1 zoom 0.71
            bo "Settle down, woman! Now hold still..."
            show tsunadiscdom_7a:
                yalign 0.5 xalign 0.9 zoom 0.6
            show tsunadiscdom_3a:
                alpha 0.2
            with dissolve
            $ renpy.sound.play("/audio/soun_fx/gags/longgag.opus", channel="sfx2", loop=False, relative_volume = 0.5)
            call changeHatred(1, "tsunade_discovery_dom_hairgrab") from _call_changeHatred_discovery_dom_2
            bo"...While I violate your throat!" with vpunch
            show tsunade_discovery_dom_bj_anim2 with dissolve:
                yalign 0.5 xalign 0.9 zoom 0.6
            $ renpy.sound.play("/audio/soun_fx/gluck1.opus", channel="sfx3", loop=False, relative_volume = 1.2)
            "You tangle your fingers tightly in her blonde hair, and start yanking forcibly to establish control!"
            ts "Mmph! *Muffled speech*"
            "Tsunade mutters some mumbled phonetics and pushes against your thighs, as if it to put a stop to your mindless aggression..."
            bo "Not a chance! Now work that mouth, or I'll pull harder." with vpunch
            hide tsunadiscdom_3a
            show tsunade_discovery_dom_bj_anim2_1:
                yalign 0.5  xalign 0.1 zoom 0.71
            show tsunade_discovery_dom_bj_anim2:
                alpha 0.1
            hide tsunadiscdom_7a
            with dissolve
            "Tsunade conceded. She dropped her hands down to the bed to brace herself, and reluctantly begun to suck. Her movements initially hesitant and clumsy, hampered by the latex."
            $ renpy.sound.play("/audio/soun_fx/bjsfx.opus", channel="sfx2", loop=True, relative_volume = 0.9)
            $ renpy.sound.play("/audio/soun_fx/gluck2.opus", channel="sfx3", loop=False, relative_volume = 1.3)
            "Under your forceful guidance, however, she starts to find a rhythm, the slickness of the condom combining with her saliva."
            call changeHatred(1) from _call_changeHatred_discovery_dom_3
            bot "Pulling her hair like this... seeing that look of resentment... Fuck! It makes me even harder for some deranged reason!"
            "You thrust your hips, deliberately forcing more of your length into her throat." with vpunch
            $ renpy.sound.play("/audio/soun_fx/gags/SDTGag4.opus", channel="sfx1", loop=False, relative_volume = 0.9)
            ts "*Gag! Cough!*" with vpunch
            bo "That's it, you depraved w-whore! Take it all, suck me dry!" with flash
            "Your rude remark was unsettling to her..."
            scene black with dissolve
            show tsunadiscdom_7b with dissolve:
                xalign 0.1 fit "contain"
            stop sfx2 fadeout 2
            "With her mouth stuffed with your cock, she managed a small proclamation of resistance, looking up to you and saying..."
            ts"S-stop this at once! We'll continue with my metho-"
            menu:
                ts"S-stop this at once! We'll continue with my metho-"
                "{color=[hatredcolor]}Pull the handlebars!{/color}":
                    pass
            bo"I don't think so, you whore! Here it c-comes..." with flash
            $ renpy.sound.play("/audio/soun_fx/cum4.opus", channel="sfx2", loop=False, relative_volume = 0.7)
            show tsunadiscdom_7a_5 with flash:
                xalign 0.9 fit "contain"
            bo"*Moans* Y-yes! S-stay right there, there's more coming!"
            $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.7)
            show tsunadiscdom_7a_5cum:
                xalign 0.9 fit "contain"
            show tsunadiscdom_7b:
                alpha 0.2
            with longerflash
            bo"Arrraagh! *Groans*..."
            call decreaselust(100) from _call_decreaselust_122
            "You held Tsunade in place by her twin tails until your balls were emptied. Her eyes started tearing up..."
            menu:
                "You held Tsunade in place by her twin tails until your balls were emptied. Her eyes started tearing up..."
                "{color=[hatredcolor]}Put her in a leg lock!{/color}":
                    bo"Goddamn Lady Tsunade! Did you feel me pulsating in your throat?"
                    $ renpy.sound.play("/audio/soun_fx/gags/SDTGag5.opus", channel="sfx1", loop=False, relative_volume = 0.9)
                    ts"Mhh...Guck!" with vpunch
                    bo"You didn't?"
                    scene black with vpunch
                    bo"Here, I think there's some left!"
                    show tsunadiscdom_8 with flash:
                        xalign 0.5 fit "contain"
                    $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                    $ renpy.sound.play("/audio/soun_fx/gags/SDTGag6.opus", channel="sfx1", loop=False, relative_volume = 0.9)
                    bo"O-oh fuck yeah!"
                    bo"Can you feel that? I think I keep leaking! Must be because of the warmth and tightness of your t-throat!"
                    $ renpy.sound.play("/audio/soun_fx/gags/SDTGag4.opus", channel="sfx1", loop=False, relative_volume = 0.9)
                    scene black
                    $ renpy.sound.play("/audio/soun_fx/gaspforair3.opus", channel="sfx3", loop=False, relative_volume = 0.8)
                    $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx4", loop=False, relative_volume = 0.5)
                    ts"*Gasps for air*"
                    "You finally break your chokehold. Tsunade stunned by your antics, lies momentarily motionless and speechless. Her still, burning hot exhales are brushing against your cock..."
                    show tsunadiscdom_9 with dissolve:
                        fit "contain" xalign 0.5
                    "You take the chance to show her the fruits of her labors!"
                    bo"See that, Lady Tsunade? That's all because of your work..."
                    ts"Y-you... *Heavy breathing*"
                    bo"It's almost leaking outside the condom too! Maybe you'd like a taste?"


                "Let her breathe...":
                    bo"F-fuck... *Groans*!"
                    scene black
                    show tsunadiscdom_10:
                        fit "contain" xalign 0.5
                    with flash
                    $ renpy.sound.play("/audio/soun_fx/gaspforair3.opus", channel="sfx3", loop=False, relative_volume = 0.8)
                    $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx4", loop=False, relative_volume = 0.5)
                    ts"*Gasps for air*"
                    "You finally let go of her  twin-tails. Tsunade stunned by your antics, lies momentarily motionless and speechless..."
                    bo"Look at that, Lady Tsunade! It's filled to the brim, all thanks to your service..."
                    ts"Y-you... *Heavy breathing*"
                    bo"M-maybe you'd like a taste of it too?"
            
                
            scene black
            ts "...E-enough!" with vpunch
            "She shoves you away backwards with a light push to your stomach..."
            show screen parallax1280("tsunadiscdom_11") with dissolve
            call showscrollingimage from _call_showscrollingimage_165
            ts"You... Y-you little SHITSTAIN!" with vpunch
            ts"I will not allow m-more of your antics, you hear me?"
            bo"Oh come on, after the great result we've had?"
            bo"Just look at the amounts you've managed to extract!"
            "You sway your waist side to side, the filled condom dangling in front of her face..." with vpunch
            ts"There's other ways to extract your semen if you keep behaving like this!"
            ts"Perhaps you'd prefer me to have you sedated next time...?"
            bo"Careful what you wish for, Lady Tsunade..."
            scene black with vpunch
            ts"*Tsk!*"
            show screen parallax1280("blackscreen") with dissolve
            jump tsunadedom_end123

        "{color=[dominancecolor]}Grab her head{/color}":
            scene black with dissolve
            bo "You are not too bad, Lady Tsunade, But perhaps you could use some of my help...?"
            bo"Can you get up here, please?"
            ts"Careful now, [bo_name]! R-remember the importance of maintaining safety protocols..."
            show tsunadiscdom_7b with dissolve:
                xalign 0.1 fit "contain"
            $ renpy.sound.play("/audio/soun_fx/gags/SDTGag4.opus", channel="sfx3", loop=False, relative_volume = 0.9)
            call changeDominance(1, "tsunade_discovery_dom_headgrab") from _call_changeDominance_discovery_dom_2
            "You cup the back of her head firmly, and firmly guide her towards you!"
            bo"R-right, right, safety protocols..."
            bo"Don't look at me like that, Lady Tsunade! Focus at the task at hand!"
            $ renpy.sound.play("/audio/soun_fx/gags/SDTGag5.opus", channel="sfx3", loop=False, relative_volume = 0.9)
            show tsunadiscdom_7b_1 with dissolve:
                xalign 0.1 fit "contain"
            "You make a small thrusting motion forward, and lightly push her head down on you. Surprisingly, Tsunade stays compliant, focused at her task..."
            call changeDominance(1) from _call_changeDominance_117 
            bot "Feeling her head under my palms... Knowing I'm completely dominating the former Hokage... What an intoxicating feeling!"

            show tsunadiscdom_7b_4:
                xalign 0.9 fit "contain"
            show tsunadiscdom_7b_1:
                alpha 0.2
            hide tsunadiscdom_7b
            with dissolve
            "Tsunade makes a small voluntary movement, taking most of your shaft in her mouth."
            bo "F-fuck, that feels nice..."
            bo"Would be even nicer if you put some effort into it though!"
            show tsunade_discovery_dom_bjdom_anim1 with dissolve:
                xalign 0.9 fit "contain"
            $ renpy.sound.play("/audio/soun_fx/gluck1.opus", channel="sfx3", loop=False, relative_volume = 1.2)
            bo"O-oh? Attentive aren't you? D-damn... Now you are really turning me on, Lady Tsunade!" with vpunch
            bo"T-that's some impressive mouth-work. K-keep that going..."
            $ renpy.sound.play("/audio/soun_fx/gluck2.opus", channel="sfx3", loop=False, relative_volume = 1.2)
            "You tangle your fingers around her hair, and carefully move her to all the right places..."
            bo "F-fuck, you are good! I am n-not far now!" with flash
            show tsunade_discovery_dom_bjdom_anim1_1:
                xalign 0.9 fit "contain"
            $ renpy.sound.play("/audio/soun_fx/bjsfx.opus", channel="sfx2", loop=True, relative_volume = 0.9)
            $ renpy.sound.play("/audio/soun_fx/gluck1.opus", channel="sfx3", loop=False, relative_volume = 1.3)
            "Knowing you are close, Tsunade picked up the pace..."
            bo"Oh f-fuck yes! Is t-that your tongue I am feeling wrapping around my cock?" with flash
            bo"Y-you really are, s-something else, L-lady Tsunade!" with flash
            bo"...H-here it comes!"
            scene black
            stop sfx2 fadeout 2 
            show tsunadiscdom_7b_1:
                xalign 0.1 fit "contain"
            with dissolve
            "Hearing you announce your imminent release, Tsunade started pulling away"
            menu:
                "Hearing you announce your imminent release, Tsunade started pulling away..."
                "{color=[dominancecolor]}I need you, Lady Tsunade!{/color}":
                    bo"N-no, stay r-right there, Lady Tsunade..."
                    $ renpy.sound.play("/audio/soun_fx/cum4.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                    show tsunadiscdom_7a_5 with flash:
                        xalign 0.9 fit "contain"
                    $ renpy.sound.play("/audio/soun_fx/gags/SDTGag7.opus", channel="sfx3", loop=False, relative_volume = 0.9)
                    bo"*Moans* I n-need you!" with flash
                    "You grabbed her twin-tails, and pulled her deeper onto your cock!"
                    $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                    show tsunadiscdom_7a_5cum:
                        xalign 0.9 fit "contain"
                    show tsunadiscdom_7b_1:
                        alpha 0.2
                    with longerflash
                    $ renpy.sound.play("/audio/soun_fx/gags/SDTGag8.opus", channel="sfx3", loop=False, relative_volume = 0.9)
                    bo"Arrraagh! *Groans*..."
                    call decreaselust(100) from _call_decreaselust_123
                    $ renpy.sound.play("/audio/soun_fx/gags/SDTGag9.opus", channel="sfx3", loop=False, relative_volume = 0.9)
                    "You held Tsunade in place by her twin tails until your balls were drained. Her eyes started tearing up..."
                    bo"F-fuck... *Groans*!"
                    scene black
                    show tsunadiscdom_10:
                        fit "contain" xalign 0.5
                    with flash
                    $ renpy.sound.play("/audio/soun_fx/gaspforair3.opus", channel="sfx3", loop=False, relative_volume = 0.8)
                    $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx4", loop=False, relative_volume = 0.5)
                    ts"*Gasps for air*"
                    "You finally let go of her  twin-tails. Tsunade stunned by your antics, lies momentarily motionless and speechless..."
                    bo"Look at that, Lady Tsunade! It's filled to the brim, all thanks to your service..."
                    ts"Y-you... *Heavy breathing*"
                    ts"You went... too f-far... *Heavy breathing*"
                    
                "{color=[hatredcolor]}Stay right there! (Leglock){/color}":
                    $ renpy.sound.play("/audio/soun_fx/gags/SDTGag5.opus", channel="sfx1", loop=False, relative_volume = 0.9)
                    ts"Mhh...Guck!" with vpunch
                    bo"Oh, no-no-no! Don't pull away now, Lady Tsunade!" with flash
                    scene black with vpunch
                    bo"Not when I am about too..."
                    show tsunadiscdom_8:
                        xalign 0.9 fit "contain"
                    show tsunadiscdom_7b_1:
                        alpha 0.2
                    with flash
                    $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.7)
                    $ renpy.sound.play("/audio/soun_fx/gags/SDTGag6.opus", channel="sfx1", loop=False, relative_volume = 0.9)
                    bo"...Explode in your t-throat!"
                    call decreaselust(100) from _call_decreaselust_124
                    "As she instinctively tries to pull back slightly for air, you swiftly lock your legs around the back of her head, trapping her completely."
                    "Her muffled protests and the vibrations against your thighs only heighten the sensation, pushing your release to greater heights!"
                    bo"Can you feel that? My pulsating cock in your mouth? I think I keep leaking! Must be because of the warmth and tightness of your t-throat!"
                    $ renpy.sound.play("/audio/soun_fx/gags/SDTGag4.opus", channel="sfx1", loop=False, relative_volume = 0.9)
                    scene black
                    $ renpy.sound.play("/audio/soun_fx/gaspforair3.opus", channel="sfx3", loop=False, relative_volume = 0.8)
                    $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx4", loop=False, relative_volume = 0.5)
                    ts"*Gasps for air*"
                    "You finally break your chokehold. Tsunade stunned by your antics, lies momentarily motionless and speechless..."
                    show tsunadiscdom_9 with dissolve:
                        fit "contain" xalign 0.5
                    "You take the chance to show her the fruits of her labors!"
                    bo"See that, Lady Tsunade? That's all because of your work..."
                    ts"Y-you... *Heavy breathing*"
                    bo"It's almost leaking outside the condom too! Maybe you'd like a taste?"
                


    scene black
    ts "...E-enough!" with vpunch
    "She shoves you away backwards with a light push to your stomach..."
    show screen parallax1280("tsunadiscdom_11") with dissolve
    call showscrollingimage from _call_showscrollingimage_166
    ts"You... Y-you little SHITSTAIN!" with vpunch
    ts"I will not allow m-more of your antics, you hear me?"
    bo"Oh come on, after the great result we've had?"
    bo"Just look at the amounts you've managed to extract!"
    "You sway your waist side to side, the filled condom dangling in front of her face..." with vpunch
    ts"There's other ways to extract your semen if you keep behaving like this!"
    ts"Perhaps you'd prefer me to have you sedated next time...?"
    bo"Careful what you wish for, Lady Tsunade..."
    scene black with vpunch
    ts"*Tsk!*"
    show screen parallax1280("blackscreen") with dissolve
    label tsunadedom_end123:
    "Ignoring your comment, Tsunade cautiously leans forward, her eyes narrowed and fixed on the filled condom still covering your cock."
    "She reaches out, grabbing your thighs nervously, steadying herself as she frantically inspects the latex membrane."
    ts "Let's... let's just make sure..."
    "Her voice is shaky, betraying her attempt at professionalism."
    pause 0.8
    "She meticulously examines the condom from different angles, looking for any sign of failure."
    bo "Worried it broke, Granny? Wouldn't want any... 'accidents', right?" with vpunch
    ts "Shut your trap, brat. This is serious."
    "After a tense moment that stretches too long, she seems satisfied, letting out a quiet sigh."
    ts "It held... No breaches."
    bo "See? All that fuss for nothing."
    bo "Now you have your precious sample, all wrapped up and safe."
    $ semendtoadd = 8
    ts "Just... hand it over."
    menu:
        ts "Just... hand it over."
        "{color=[dominancecolor]}You should take it off...{/color}":
            call changeDominance(1) from _call_changeDominance_discovery_dom_4
            bo"You take it off! Wouldn't want me to mess that up right?"
            ts"*Scoffs*..."
            call changetsunadedominance(-1) from _call_changetsunadedominance_37
            "She carefully pinches the base of the condom and slides it off, holding it up almost gingerly, like a biohazard."
            $ semendtoadd = 9
        "Hand it over carefully.":
            bo "Here you go."
            "You carefully hand the condom to her."
            ts "Good..."
            $ semendtoadd = 9
    show screen parallax1280("tsunadiscdom_12") with dissolve
    call showscrollingimage from _call_showscrollingimage_167
    ts "Sample acquired. You are feeling better, yes? Now get dressed, and get out!" with vpunch
    $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
    bo "Always a pleasure, Lady Tsunade!"
    "You leisurely swing your legs off the bed and get dressed. A smug, triumphant grin is plastered on your face."
    call addSemen(semendtoadd) from _call_addSemen_discovery_dom_1
    bo "Let me know when you are in need of another... 'safe' sample!"
    ts "Out of my office. Now!"
    "Tsunade turns away sharply, clutching the filled condom, her shoulders slumped in defeat..."
    tst "Damn him... Damn this curse! But the samples... they are vital..."
    tst "For the betterment of the village, I shall endure..."
    call hidescrollingimage2 from _call_hidescrollingimage2_122
    $ renpy.end_replay()
    $ tsunade_discovery_dom_repeats += 1
    jump action_taken