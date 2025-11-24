label himawari_modelling_session:
    default himamodel_firsttime = True
    $ hima_talked_modelling = True #Just incase Yoruichi's sexual favors appears twice
    bot"Now that she's seen Yoruichi the other day, I bet she'd be much more receptive to the idea..."
    if quest.exists("bohim_2"):
        if quest.is_state("3_bohim_2", "pending") or quest.is_state("2_bohim_2", "in progress") or quest.is_state("2_bohim_2", "pending") :
            $ quest.change_quest_title("2_bohim_2",f"Convince {him_name} to work with you")
            $ quest.change_quest_title("3_bohim_2",f"Purchase a camera and convince Yoru to help you")
            $ quest.change_quest_title("4_bohim_2",f"Have your first session with {him_name}")
            $ notification (f"Quest objective completed")
            $ quest.check("2_bohim_2", "completed")
            $ quest.check("3_bohim_2", "completed")
            $ inventoryShop.update_item(f"Bikini", price=100, quantity=1)

    $ himamodel_firsttime = False
    bo"You've asked me before to introduce you to one of my models, and now I have!"
    show boruto snob with dissolve
    bo"It's about time we start working together, don't you think?"
    if day_part == 3:
        show hima mad with dissolve
        him"It's freakin' night time you imbecile!"
        show hima at smallshake
        him"How about you be normal for once and ask me at a reasonable time..."
        show blackscreen with dissolve
        him"Hmph!" with vpunch
        "[him_name] will only consider modelling for you during daytime..."
        menu:
            "[him_name] will only consider modelling for you during daytime..."
            "Skip to daytime...":
                show himawari_bedroom_1 behind hima
                hide blackscreen
                with dissolve
                pass
            "Return":
                show hima smugshy
                hide blackscreen with dissolve
                jump repeatable_earnhertrust_menu
    show hima worried2 with dissolve
    show hima at smallshake
    him"O-oh, about that! You are really adamant about it, aren't you...?"
    show boruto normal with dissolve
    bo"I will assume you haven't forgotten why I- we are doing this, right...?"
    show hima at smallshake
    him"Mama..."
    show hima worried1 with dissolve
    himt"He's right. I can't be the one not helping Mom..."
    himt"As much as I despise him, he is at least t-trying something, I guess..."
    show hima worried2 with dissolve
    him"But... still, modelling? R-really?"
    show boruto snob with dissolve
    bo"Come on, you've met Yoru, right? If she's willing to work for me, then why not you too?"
    show hima shy with dissolve
    him"Y-yoru... She was so pretty!"
    bo"Right?"
    show hima smugshy with dissolve
    him"Come to think of it, why the hell does she work for a loser like you anyway!"
    show hima smug2 with dissolve
    him"You must be paying her off, right? There's no other way!"
    if yoruichi_relationship == "Obedient":
        menu:
            him"You must be paying her off, right? There's no other way!"
            "{color=[obediencecolor]}Actually, She pays me, in a way...{/color}":
                show boruto normal with dissolve
                bo"Actually, she pays me in a way..."
                show hima smugshy with dissolve
                show hima at smallshake
                him"W-what... What does that e-even mean!"
                bo"Me and her, we are more than... friends, you know?"
                show hima surprised with dissolve
                him"N-no way!" with vpunch
                show hima embarassed with dissolve
                call changeObedience("Himawari",1) from _call_changeObedience_127
                him"You and h-her... are like that!?" with vpunch
                show boruto normal with dissolve
                bo"We got pretty close lately, yeah."
                bo"I help her out with a few things, and in turn-"
                show hima mad with dissolve
                him"I don't want to hear any more of that! Let's move on..."
                show boruto snob with dissolve
                bo"Oh? As you wish then, little tigress..."
                him"Hmph!"
            "Actually, She works for me for free":
                show boruto normal with dissolve
                bo"Actually, she works for me for free..."
                show hima smugshy with dissolve
                show hima at smallshake
                him"W-what? Why would anyone do that!"
                bo"Me and her, we are more than friends you know..."
                show hima worried2 with dissolve
                him"H-huh...?"
                bo"I help her out with a few things, and in turn..."
                show boruto snob with dissolve
                bo"She helps me out with my own needs..."
                him"W-what does that mean..."
                bo"You are too young, you wouldn't get it."
                show hima mad with dissolve
                him"We are almost the same age, you retard! *Grrr*" with vpunch
                show boruto normal with dissolve
                bo"Right, right. Settle down little Tigress..."
                bo"Are we doing this or what...?"
                him"Hmph!" with vpunch

    else:
        menu:
            him"You must be paying her off, right? There's no other way!"
            "{color=[hatredcolor]}Lie{/color}":
                show boruto sceeming with dissolve
                bo"Not really, she works for me for free!"
                bo"That's what girlfriends are for anyway..."
                show hima smug1 with dissolve
                show hima at smallshake
                him"Bwahahaha! Don't make me laugh!"
                him"She? Your girlfriend? Probably in your dreams..."
                show hima smug2 with dissolve
                him"You are lying aren't you? I am going to ask her if that's true the next time we meet..."
                show boruto angry with dissolve
                bo"I am not lying, you..."
                call changeHatred(1) from _call_changeHatred_143
                bot"Stupid bitch... She is right though. I better play this safe for now..."
                him"Why are you getting flustered, hm?"
                show boruto snob with dissolve
                bo"Me...? Flustered? It's you who's about to go back on your word..."
                bo"Are you going to back down from a little modelling shoot even after your promise...?"
                show hima smugshy with dissolve
                him"Eh-eh..."

            "You are so stupid...":
                show boruto normal with dissolve
                bo"I am paying her... for her services. What are you, stupid?"
                show boruto snob with dissolve
                bo"That's how business works..."
                show hima smugshy with dissolve
                him"Right... So you are going to be paying me too then?"
                bo"Maybe, if your work is worth anything at all..."
                show hima mad with dissolve
                him"W-why you... And don't call me s-stupid!"
                bo"You were asking for it..."
                show hima at smallshake
                him"Hmph!" with vpunch
            

    show hima thinking with dissolve
    "[him_name] appeared lost in her thoughts for a moment..."
    show hima worried2 with dissolve
    him"F-fine!" with vpunch
    show boruto surprised2 with dissolve
    bot"Yes!"
    him"I g-guess we can try out your dumb idea..."
    him"So... when do we start?"
    show boruto snob with dissolve
    bo"Right about now is as good a time as any..."
    show hima embarassed with dissolve
    show hima at smallshake
    him"R-right now...?"
    bo"We don't exactly have the luxury of time, you know..."
    show hima worried2 with dissolve
    him"I s-suppose you are right..."
    him"So? What do I do..."
    bo"You silly goose, we are not shooting in here, neither in those rags you are wearing..."
    him"W-what! Why? What's wrong with my room, and my clothes!"
    bo"For one, your room has shitty lighting. Besides, I haven't prepared a studio in my room for nothing..."
    bo"If we are going to be professionals, then you have to trust me with some things, alright?"
    him"A... s-studio?"
    bo"Remember the sporty outfit I bought for you the other day for your birthday?"
    bo"It's time we make some use of it!"
    show boruto:
        easeout 2 xpos -1000
    bo"Wear that and meet me at my bedroom when you are ready..."
    show hima embarassed with dissolve
    him"W-wait! I haven't even agreed to wearing that..."
    bo"See you soon!" with vpunch
    show hima mad3 with dissolve
    him"F-freaking bozo..."
    show hima at smallshake
    him"Hmph!"
    scene black with dissolve
    him"I am not backing down now!"
    "..."
    show bg modelling with dissolve
    show boruto snob at left with dissolve
    bot"Hehe! I sure hope this works..."
    bot"I can't believe I convinced my [him_rel] to model for me!"
    bot"If everything goes as planned then..."
    call increaselust(5) from _call_increaselust_192
    bot"Just thinking of the possibilities gets my excited!"
    show boruto normal with dissolve
    bot"I should probably take it slow on her first photoshoot. Ease her in..."
    bot"Hopefully she won't get spooked off immedi-"
    show opinion1_him with dissolve:
        yalign 1.0
    show opinion1_him:
        easein 4 yalign 0.0
    him"A-are we doing this, or what...?"
    bot"My little [him_rel]..."
    call increaselust(5) from _call_increaselust_193
    bot"She is sexy as ever! Even more so when she bends to my will for once!" with vpunch
    show boruto surprised2 at left
    hide opinion1_him with dissolve
    show boruto snob with dissolve
    bo"Right away. Come on, move in the spot light..."
    show opinion2_himt beh at right:
        zoom 0.7 xpos 2000
    show opinion2_himt beh:
        easein 1 xpos 800
    him"This... r-really isn't my forte, you know."
    bo"You won't know until you try, right?"
    show opinion2_himt with dissolve
    him"I suppose..."
    hide boruto with dissolve
    bo"Let me just..."
    bo"Get my equipment ready. You sit there looking pretty, okay?"
    hide opinion2_himt
    show opinion1_himt ass1:
        zoom 0.7 xpos 800
    with dissolve
    him"I could do without your stupid comments..."
    himt"Is this thing even appropriate to wear?"
    show opinion1_himt ass3 with dissolve
    himt"*Sigh...* I guess we've been through this already. It's just something that athletes have to get used to..."
    himt"Maybe this will help in that regard..."
    hide opinion1_himt with dissolve
    himt"I should prepare myself..."
    scene black with dissolve
    bot"My trusty camera, today I'll put you to good use! Hehe..."

    show screen camera1280("bg modelling",1,1.0) with dissolve
    bot"Right where were we..."
    bo"Ready, [him_name]?"
    show screen camera_ui("Himawari",False) with dissolve
    "You turn around towards her..."
    show screen camera1280("hima_model_normal") with dissolve
    him"I..." with vpunch
    bot"N-nice..."
    hide screen camera1280
    hide screen camera_ui
    show screen camera1280("hima_model_normal",1,0.0)
    show screen camera_ui("Himawari",False)
    with dissolve
    him"I don't know! Do I just... s-stand here?"
    bo"Not exactly, but don't worry, okay?"
    bo"All you have to do is follow my lead and I'll ease you into it..."
    him"R-right..."
    bo"I know the lens can be scary, so I'll take a couple of steps back, and take what is supposed to be a full shot..."
    show screen camera1280("hima_model_start",1,0.0) with dissolve
    "Pan the camera to capture [him_name]'s face... or other features of hers!"
    him"F-from behind...?"
    call increaselust(5) from _call_increaselust_194
    bot"She certainly built some cake on her with all that exercising of hers..."
    bo"Front, behind, side... It makes no difference, [him_name]. A good model brings out her best on any profile. Confidence is key!"
    him"W-whatever you say..."
    bo"Ready... and..."
    show expression FocusEffect("idle1", 180, 350, 100, 0.7) as focus_effect onlayer screens with dissolve
    show screen camera_ui("Himawari")
    hide expression FocusEffect as focus_effect onlayer screens
    with dissolve
    $ ui.interact()
    show screen camera_ui("Himawari",False) with dissolve
    him"That flash... does that mean it's over? We are done?"
    bo"Done? Far from it..."
    bo"That was a single photograph. A session is supposed to last for multiple, you know..."
    him"Hmm... Can I see it?"
    hide screen camera_ui
    hide screen camera1280
    scene black
    with dissolve
    bo"S-sure..."
    scene bg modelling
    show opinion2_himt beh:
        xalign 0.5 zoom 0.7
    with dissolve
    show opinion2_himt beh at smallshake
    him"*Gasp!* T-that's...me?"
    show screen photo_album with dissolve
    hide opinion2_himt
    show opinion1_himt:
        zoom 0.8 xalign 0.5
    with dissolve
    bot"..."
    him"Isn't that angle, kinda weird...?"
    bo"Leave the f-framing to the expert, alright?"
    show opinion1_himt at smallshake
    him"Expert m-my ass! How did you even afford all this equipment anyway..."
    scene black with dissolve
    bo"Too many questions, too little posing! Let's get back to business"
    show screen camera1280("hima_model_normal back",1,0.0)
    show screen camera_ui("Himawari",False)
    with dissolve
    him"Hmph!" with vpunch
    him"Just as long as you don't try anything w-weird..."
    bo"Your expressions could really use some work you know!"
    bo"You look like you are about to kill someone!"
    him"Oh yeah? Maybe it's because I wanna kill you!"
    bo"Shuuut up, you harmless vixen... Come on, look a little alive!"
    hide screen camera_ui
    hide screen camera1280
    show screen camera1280("hima_model_normal back_close",1,0.7) with dissolve
    bo"I am closing in for a medium shot, alright? Try to look relaxed, for once!"
    him"I don't even know what that means..."
    bot"I can't help but stare at her ass through the lens..."
    call increaselust(5) from _call_increaselust_195
    bot"The things I'd do to lick the sweat straight from her-"
    bot"W-what am I even thinking! Come on, focus up. I can't fuck this up..." with vpunch
    him"So...? How am I doing?"
    bo"Don't worry too much about it. You are already doing better than what you were two minutes ago!"
    bot"Might as well gas her up a little bit!"
    bo"Ready... and..."
    show screen camera_ui("Himawari")
    with dissolve
    $ ui.interact()
    bo"Great shot! You are a natural..."
    him"You are just saying that to make me feel better."
    bo"I am serious [him_name]. You ain't half bad at this!"
    bo"Here, I'll prove it to you..."
    bo"Remember how when we started a while ago you were spooked by the lens?"
    bo"I'll close in on you now for a close-up, and I want you to pull off your best move! Something that comes naturally at you, alright?"
    him"I can try..."
    hide screen camera_ui
    hide screen camera1280
    scene black with dissolve
    bo"Then here I come..."
    "As you closed in on her, [him_name] pulled off something you weren't expecting..."
    show hima_model_normal bestshot with dissolve:
        yalign 1.0
    show hima_model_normal bestshot:
        easein 3 yalign 0.0
    "With a quick twise of her torso, she arched her back spectacularly, dropping her hands behind her and letting her head hang, leaving her hair flowing gently..."
    show hima_model_normal bestshot:
        easein 3 yalign 1.0
    bot"W-what the hell was that. She looks..."
    bot"B-beautiful, majestic even!"
    bot"D-damn it, since when did [him_name] get so... s-sexy!"
    bot"Her skimpy shorts are barely hanging on too!"
    scene black with vpunch
    him"H-hey! What's going on, was that bad?"
    bo"[him_name]... I missed the shot!"
    show hima_model_normal with dissolve:
        yalign 0.0
    him"And here I thought you were the expert here..."
    bo"You don't understand... That move you pulled off. It was... beautiful."
    him"...You are s-serious?"
    bo"I think you might truly have a natural inclination for this, [him_name]..."
    bo"Can you try doing that again? This time I won't be caught off-guard..."
    scene black with dissolve
    him"0-okay, I guess..."
    show screen camera1280("hima_model_normal bestshot",1,0.0)
    show screen camera_ui("Himawari",False)
    with dissolve
    bo"And..."
    show screen camera_ui("Himawari")
    with dissolve
    $ ui.interact()
    bo"Snap!"
    show screen camera1280("hima_model_start",1,0.0)
    show screen camera_ui("Himawari",False)
    with dissolve
    bo"Excellent job, [him_name]! I think we got ourselves a winner..."
    bo"You should probably see this one, you look spectacular..."
    him"Yeah w-well, coming from you, that means absolutely nothing..."
    hide screen camera1280
    hide screen camera_ui
    scene black with dissolve
    bo"I am serious! You should come check this one out..."
    scene bg modelling
    show opinion2_himt beh with dissolve:
        zoom 0.8 xalign 0.5
    him"F-fine..."
    hide opinion2_himt with dissolve
    "You sit alongside each other on the mattress and you go through the photos you've taken up until now..."
    scene black
    show hima_photoshoot end0
    with dissolve
    bo"This one's decent..."
    bo"Don't mind this one, the c-camera malfunctioned!"
    "You cycle through the photographs, until you reach the one that you thought would leave an impression on her..."
    show hima_photoshoot end000 with dissolve:
        zoom 1.1
    him"*Gasp*... T-thats me!?"
    bo"...Right?"
    show hima_photoshoot end000 with dissolve:
        zoom 1.0
    him"I look... b-beautiful! How'd you even do that?"
    scene black with dissolve
    bo"Well... y-you know! I am an expert after all!"
    bot"That was all her if I were to be honest..."
    scene black
    show hima_photoshoot end00
    with dissolve
    him"So you do know a thing or two after all..."
    him"Y-you know..."
    call changeObedience("Himawari",1) from _call_changeObedience_128
    him"This wasn't all that bad in the end. M-maybe I was wrong to distrust you..."
    bo"And we are only getting started! Imagine how much money we'd be making once you get the hang of it..."
    him"I... I'll believe it when I see it."
    him"You better be paying me my fair share by the way, or else..."
    "The more you prove yourself to [him_name] the more options it'll open up for future photoshoots!"
    bo"Of course! To commemorate our long lasting partnership, let's celebrate with one last shot to mark this day!"
    him"What do you have in mind?"
    menu tutorial_hima_photoshoot_menu:
        him"What do you have in mind?"
        "{color=[obediencecolor]}Lay on the bed for me...{/color}":
            pass
        "{color=[obediencecolor]}???{/color}":
            "You'll unlock more options as you prove yourself to [him_name]..."
            jump tutorial_hima_photoshoot_menu
        "{color=[obediencecolor]}???{/color}":
            "You'll unlock more options as you prove yourself to [him_name]..."
            jump tutorial_hima_photoshoot_menu
        "{color=[obediencecolor]}???{/color}":
            "You'll unlock more options as you prove yourself to [him_name]..."
            jump tutorial_hima_photoshoot_menu
    scene black with dissolve
    bo"I'll just sit up real quick, while you lay where you are, okay?"
    him"You want me to lay... on your stinky bed?"
    bo"Come on... Just one final click! Remember, this is cause for celebration!"
    him"...F-fine!" with vpunch
    show himamodel intermission with dissolve
    call changeObedience("Himawari", 1) from _call_changeObedience_129
    him"But make it quick!" with flash
    bo"*Click* *Click* *Click* *Click*" with flash
    him"What kind of shot is this anyway..."
    bo"*Click* *Click* You... *Click* *Click* wouldn't get it!" with flash
    him"S-stop saying that!" with vpunch
    him"And you only said one click!"
    bo"I've yet to capture the perfect shot. It takes time, you know..."
    with Shake((0, 0, 0, 0), 1, dist=20, peak_time=0.8, smoothness=50)
    scene black with vpunch
    him"I've had enough of this!" with vpunch
    "[him_name] storms off, putting an end to your first photoshoot with her."
    scene bg modelling
    show boruto snob
    with dissolve
    if quest.is_state("4_bohim_2", "in progress"):
        $ quest.check("4_bohim_2", "completed")
        $ quest.check("bohim_2", "completed")
        $ quest.check("bohim_3", "unlocked")
        $ quest.check("1_bohim_3", "in progress")
        $ inventoryShop.update_item(f"Bikini", price=100, quantity=1)
        $ notification (f"Objective Completed: Have your first session with {him_name}")
    bo"What a great success!"
    menu:
        bo"What a great success!"
        "{color=[hatredcolor]}This is how I break her walls down!{/color}":
            show boruto sceeming with dissolve
            bo"I've done such a great job of gassing her dumb ass up!"
            bo"I'll keep this up as long as it takes, and when the time is right.."
            show boruto sceeming2 with dissolve
            call changeHatred(1) from _call_changeHatred_144
            bo"Hehehe! That stupid bitch has no idea what I have in store for her..."
        "{color=[lovecolor]}This may be how I'll remedy our relationship{/color}":
            show boruto surprised2 with dissolve
            bo"This may just be the way to remedy our broken relationship..."
            bo"But there's still ways until that's reality."
            bo"For now, I just have to keep trying my best..."
    $ notification("Quest updated")
    scene black with dissolve
    jump action_taken
        
    


    
         









