label afterclinic:
    show hina concerned at left with dissolve:
        zoom 0.70
    hin"..."
    show boruto sad2 at right with dissolve
    bo"..."
    "[hin_name] opened her mouth to speak, but the words clumped in her throat. Similarly, your gaze dropped to the floor. An uneasy silence stretched between the two of you..."
    hide hina with dissolve
    hide boruto with dissolve
    "The rhythmic tapping of your footsteps against the ground was the only sound that accompanied your journey home..."
    scene black with fade
    "But you both knew that once you got there, you would have to have an honest conversation..."
    play sound("/audio/soun_fx/rain.opus") loop fadein 1.0 volume 2
    "Minutes ticked by like hours as the weight of unspoken words hung between the two of you."
    show introvideo with fade
    pause(3.5)
    $ renpy.pause(1, hard=True)
    scene bg intro2n with dissolve
    show hina talking at left with dissolve:
        zoom 0.70
    hin"Let's hurry inside, we are already soaking wet!"
    show boruto sad at right with dissolve
    bo"..."
    hide hina with dissolve
    hide boruto with dissolve
    scene black with fade
    $ renpy.music.stop(channel="sfx1")
    stop sound fadeout 2
    stop music fadeout 2
    pause(1)
    play sound "audio/soun_fx/dooropen.opus" volume 0.7
    pause (0.5)
    show bg lr night with dissolve:
        zoom 0.68
    "..."
    play music"/audio/ost/house2.opus" volume 0.6
    show blackscreen with dissolve
    show hima running0 with dissolve:
        zoom 0.7
    play sound "audio/soun_fx/footsteps.opus" volume 0.8
    "[him_name] hearing the door open, swiftly made her way to the living room."
    "Each of her frantic footsteps audible through the thudding of her bare feet stomping the wooden floor."
    hide blackscreen with dissolve
    show hima running1 with dissolve
    "It appears she was worried about your and her [hin_rel]'s long absence..."
    him"Mom!"
    "[him_name] took one look at your ashen expressions before flinging herself into Hinata's arms, burying her face against her mother's chest"
    $ renpy.sound.play("/audio/soun_fx/himawari/himascared1.opus", channel="sfx3", loop=False, relative_volume = 0.3)
    him"I was worried sick! Why are you so late?"
    "[him_name] often appears cold-hearted and nonchalant towards you, but in truth she is extremely emotional, fragile even..."
    "But only when it comes to your [hin_rel], whom she looks up to immensely."
    hide hima running1 with dissolve
    #side eye cg
    show bg lr night with dissolve
    show hima mad3 at right with dissolve:
        zoom 0.33
    "[him_name] glanced at you menacingly, her small fists clenched at her sides..."
    him"Was it, this idiot's fault?"
    show hina talking at left with dissolve:
        zoom 0.75 yalign 0.5
    hin"[him_name], what did we say about name-calling..."
    show hima mad3 at right with dissolve:
        zoom 0.33
    show boruto angry at mid with dissolve
    menu aftrerclinichimhatred:
        bot"There she goes again"
        "{color=[hatredcolor]}Reply aggressively{/color}":
            call checkHatred(5, "aftrerclinichimhatred") from _call_checkHatred_4
            show boruto angry2 with dissolve
            bo"Don't test me you god-damned brat! I've got enough on my plate as is."
            call changeRespect("Himawari", -1, "none") from _call_changeRespect_31
            show hima mad with dissolve
            $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            him"Hmph! If you've done anything to upset [hin_rel], I'll beat you to a pulp!"
            call borutoevil2 from _call_borutoevil2_1
            bo"Not before I have my way with you!"
            call changeHatred(1, "none") from _call_changeHatred_14
            "A sinister smirk formed on your face as you spoke those words..."
            "Could your crude comment allure to something much more vile than simple violence?"
            show hina assertive with dissolve:
                zoom 0.7
            show boruto surprised2 
            call changeRespect("Hinata", -1, "none") from _call_changeRespect_32
            hin"Enough! Both of you, drop it!" with vpunch
            hide hima
            show hima smug1 at right with dissolve:
                zoom 0.33
            $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            him"Hmph!"
            "Of course, your [hin_rel_mother] and [him_rel] dismissed it as just another of your all too common altercations."
        "Reply calmly":
            show boruto sad with dissolve
            bo"[him_name]... There is a lot going on you don't know about. Please just... drop it for now, will you?"
            show hima mad with dissolve:
                zoom 0.33
            $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            him"Hmph! If you've done anything to upset [hin_rel], I'll make you regret it!"
            show boruto normal with dissolve
            bo"*Sigh*"
            show hina assertive with dissolve:
                zoom 0.7
            call changeRespect("Hinata", 2, "none") from _call_changeRespect_33
            hin"Enough! [him_name], drop it..."

    hin"There is a lot to go through so let us all take a seat, please."
    show blackscreen with dissolve
    hide hina
    hide boruto
    hide hima
    "All three of you sit around in the living room. The tension is almost palpable..."
    hide blackscreen with dissolve
    show hima normal at right with dissolve:
        zoom 0.33
    show boruto normal at mid with dissolve
    show hina talking at left with dissolve:
        zoom 0.72
    hin"[him_name], the reason we were late is because... your [him_rel_to_bo] and I were at the infirmary."
    show hima worried2 with dissolve:
        zoom 0.33
    him"The infirmary? Why?"
    him"Is anyone hurt?"
    show hina surprised with dissolve
    hin"N-no. Not exactly..."
    show hima normal with dissolve
    "[hin_name] was careful with her wording. She did not want [him_name] to know of what she truly saw as she knew that she would hold it against [bo_name]"
    show hina concerned with dissolve
    hin"I was wrapping up my afternoon jog when I found [bo_name]... unconscious in a neighborhood street"
    hin"I rushed him to the infirmary. There, [bo_name] was diagnosed with a... condition."
    hide hima
    show hima smug2 at right with dissolve:
        zoom 0.33
    $ renpy.sound.play("/audio/soun_fx/himawari/loserlaugh.opus", channel="sfx3", loop=False, relative_volume = 0.5)
    him"[hin_rel]... we already knew he is brain damaged."
    show boruto angry with dissolve
    bo"You b-"
    show hina assertive with dissolve
    hin"[him_name]! This is important, take it seriously!" with vpunch
    hin"..."
    hin"Do you remember the stories about your [na_rel]?"
    show blackscreen with dissolve
    show hima normal with dissolve:
        zoom 0.33
    show boruto normal
    "[hin_name] explained much of the situation to [him_name], but again made sure to conceal some of the more explicit details, in an attempt to protect her daughter's innocence."
    hide blackscreen with dissolve
    show hina concerned with dissolve
    hin"And that is the gist of it..."
    show hima concerned with dissolve:
        zoom 0.33
    him"Hmmm. So if there is no tailed beast inside of him, there is nothing to worry about, right?"


    show hina talking with dissolve
    hin"*Sigh...*"
    show hima thinking at right with dissolve:
                zoom 0.33
    hin"We might not have to worry about the violent part of it, yes. Even so, your [him_rel_to_bo] could experience some... emotional disruption."
    hin"If he gets irritable or... agitated, know that he is dealing with his condition as best as he can."
    hin"[bo_name] promised me that he will control his condition by staying vigilant with the treatment the doctor prescribed..."
    hin"Right, [bo_name]?"
    show boruto worried with dissolve
    "Your [hin_rel]'s piercing gaze fixated on you, awaiting your reply..."
    menu:
        bo"Uuuhhh..."
        "Yes, I will do my best":
            show boruto worried with dissolve
            bo"Right, I will do my best so that you both don't have to be scared of  my... condition"
            call changeRespect("Hinata", 1, "none") from _call_changeRespect_34
            show boruto worried2 with dissolve
            bo"I promise."
            show hima smug1 with dissolve:
                zoom 0.33
            $ renpy.sound.play("/audio/soun_fx/himawari/himascoff1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
            him"You better!"
            him"I would much prefer not associating with you any more than I already am!"
            show boruto angry with dissolve
            bo"[him_name], you..."
            show hina assertive with dissolve
            hin"[him_name]!" with vpunch
            hin"Your [him_rel_to_bo] has a lot going against him at the moment. I would appreciate if you tried being more... sympathetic."
            show hima smug with dissolve:
                zoom 0.33
            him"If you say so, [hin_rel]."
            himt"The only thing against that idiot is his stupid brain!"
        "I can't guarantee [him_name]'s safety":
            bo"I will [hin_rel] but if [him_name] keeps provoking me, I might just snap."
            show hima smug1 with dissolve:
                zoom 0.33
            him"You...? Snap...?"
            show hima smug with dissolve
            him"What are you going to do, bad-mouth me to submission?"
            show boruto angry with dissolve
            menu:
                him"What are you going to do, bad-mouth me to submission?"
                "{color=[hatredcolor]}I will do much worse than that!{/color}":
                    show boruto pissy with dissolve
                    call changeHatred(1, "none") from _call_changeHatred_15
                    bo"Who knows, I might do just that... or worse!"
                    bot"You have no idea you dumb bitch..."
                    call changeRespect("Himawari", -1, "none") from _call_changeRespect_35
                    him"Hahaha! You have a future in comedy!"
                    menu:
                        him"Hahaha! You have a future in comedy!"
                        "{color=[hatredcolor]}And you have a future gagging on my cock!{/color}":
                            call changeHatred(1,"none") from _call_changeHatred_16
                            show boruto sceeming3 with dissolve
                            bo"And you have a future ga-"
                        "{color=[hatredcolor]}Piss off, you stupid bitch...{/color}":
                            bo"Piss off, you stupid bitch!"
                            call changeRespect("Hinata", -1, "none") from _call_changeRespect_36
                            show hina assertive with dissolve
                            show boruto surprised2
                            hin"[bo_name_stutter]!" with vpunch
                            call changeRespect("Himawari", -1, "none") from _call_changeRespect_37
                            $ renpy.sound.play("/audio/soun_fx/himawari/himascoff2.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                            him"Hmph!"
                        
                "{color=[dominancecolor]}If that's what it takes...{/color}":
                    bo"Who knows [him_name], if that's what it takes for you to behave..."
                    bo"Would you prefer I turn physical?"
                    show hima smug2 with dissolve
                    him"Ha! I can take you on anytime little man!"
                    call changeDominance(1,"none") from _call_changeDominance_10
                    bo"You sure you wanna put that to test?"
                

            show hina assertive with dissolve
            show boruto surprised2
            hin"Enough! Both of you, behave!" with vpunch
  
    show blackscreen with dissolve
    show hina concerned
    show hima thinking
    show boruto worried
    hide blackscreen with dissolve
    hin"We still don't exactly know the full implications of dealing with this, so let's all take it seriously."
    hin"With that [him_name], let's do our best as well to be supportive of [bo_name] as much as we can, okay?"
    him"So there is nothing to worry about at all..."
    show hima smug1 with dissolve
    him"You know..."
    show boruto surprised2 with dissolve
    him"This doesn't even sound that serious. Not sure what the big fuss is all about."
    show hima smug2 with dissolve
    $ renpy.sound.play("/audio/soun_fx/himawari/loserlaugh.opus", channel="sfx3", loop=False, relative_volume = 0.5)
    him"So [bo_name] has some sort of autism and we have to be careful not to hurt his feelings?"
    show boruto angry2 with dissolve
    show hima turnaway1 at right with dissolve:
        zoom 0.45
    $ renpy.sound.play("/audio/soun_fx/himawari/himascoff1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
    him"HA!" with vpunch
    him"No promises!"
    show boruto angry with dissolve
    bo"You little..."
    show hina assertive with dissolve
    "[him_name] jokingly dismissed the severity of your condition, turning around to go back to what she was doing..."
    hin"[him_name]! We will have a private talk about your attitude on the matter!"
    hide hina with dissolve
    show boruto at left with dissolve:
        easein 1 xpos -0.10
    him"Sure, sure! I am off."
    window hide #hide chat window
    show bg lr night with dissolve:
        subpixel True alpha 0.3
    show hima turn1 at right with dissolve:
        zoom 0.8 xalign 0.99 yalign 0.9
    show boruto surprised2 with dissolve
    call increaselust pass (10) from _call_increaselust_22 
    pause 1
    window show
    "You notice your [him_rel]'s ass peeking out of her skimpy shorts, revealing more than she intended..."
    "She must have not noticed them slipping up while she was erratically running beforehand..."
    show boruto angry with dissolve
    bot"This little rascal..."
    menu:
        bot"..."
        "Shame her":

            show hima turn1 at right with dissolve:
                zoom 0.45
            show boruto sceeming at left:
                easein 1 xpos 100
            bo"Hey [him_name]! Why is your saggy ass hanging out around your family... have you no shame?"
            window hide #hide chat window
            # hide boruto with dissolve
            show bg lr night with dissolve:
                subpixel True alpha 0.3
            show hima comment0 with dissolve:
                zoom 0.7 yalign 0.9
            $ renpy.sound.play("/audio/soun_fx/himawari/himagasp.opus", channel="sfx3", loop=False, relative_volume = 1.0)
            pause 1
            window show
            him"Eek!" with vpunch
            himt"When did this happen!?"
            himt"And why is that idiot..."
            show boruto sceeming2 with dissolve
            bo"Maybe it is you who has brain damage! HA!"
            call changeRespect("Himawari", -1, "none") from _call_changeRespect_38
            # hide boruto with dissolve
            show hima comment1 with dissolve:
                zoom 0.5 yalign 0.9
            show boruto surprised2 with dissolve
            "[him_name] was embarrassed but mostly annoyed at you."
        
            "She reached down to her shorts in shame, trying to pull them down as she was walking away..."
            window hide
            call increaselust pass (5) from _call_increaselust_23 
            pause 1
            window show
            show hima comment1 at right with dissolve:
                zoom 0.45
            show boruto smirk at left with dissolve
            him"And why are you the one to notice that, you freaking circus clown!"
            call changeRespect("Himawari", -1, "none") from _call_changeRespect_39
            him"Stop staring at my butt!"
            show boruto sceeming with dissolve
            bo"Then cover it up, bozo!"
            window hide
            # hide boruto with dissolve
            show hima comment2 with dissolve:
                zoom 0.5 yalign 0.9
            pause 1
            window show
            him"That is what I am doing, you dingus!"
            show hima comment2 at right with dissolve:
                zoom 0.45
            show boruto sceeming2 at left with dissolve
            bo"Good riddance, dimwit!"
            him"...!"
            call changeObedience("Himawari", 1, "none") from _call_changeObedience_30
            bot"Hehe! Stupid brat..."
            bot"She might be a major bitch, but her ass is anything but saggy..."
            hide hima with dissolve
            bot"I only said that to get on her nerves."
            default stareass = False
            
        "Drop the argument":
            bo"*Sigh...*"
            show hima turnaway2 with dissolve
            show boruto surprised2 with dissolve
            "You couldn't help but look at her ass as she was walking away..."
            show hima with dissolve:
                zoom 0.9
            bot"Did my [him_rel] always had an ass like that on her?"
            menu:
                bot"..."
                "Say something":
                    $ stareass = False
                    show boruto smirk with dissolve
                    bo"You might want to check your shorts, [him_name]."
                    show hima with dissolve:
                        zoom 0.8
                    him"Why? What's wrong with them..."
                    show hima turnaway3 with dissolve:
                        zoom 0.75
                    $ renpy.sound.play("/audio/soun_fx/himawari/himagasp.opus", channel="sfx3", loop=False, relative_volume = 1.0)
                    him"O-oh! Oops!"
                    "She shamefully dragged them back down as she was walking away..."
                    show hima comment2 with dissolve:
                        zoom 0.5 yalign 0.1
                    him"Why are you even looking there to begin with you perv!"
                    menu:
                        "..."
                        "Reply playfully":
                            show hima with dissolve:
                                zoom 0.5
                            show boruto snob with dissolve
                            bo"Hard not to when your entire bum is hanging out you demonspawn!"
                            call changeObedience("Himawari", 1, "none") from _call_changeObedience_31
                            him"I-it was an a-accident!"
                            call changeRespect("Himawari", -1, "none") from _call_changeRespect_40
                            show hima:
                                zoom 0.6
                            himt"Freaking perv!"
                            show hima:
                                zoom 0.5
                            $ renpy.sound.play("/audio/soun_fx/himawari/himascoff1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                            "[him_name] retreats to her bedroom..."
                            show hima:
                                easein 1 xpos 1.50
                        "Reply respectfully":
                            show boruto smirk2 with dissolve
                            bo"Relax, I am just looking out for you..."
                            call changeObedience("Himawari", 1, "none") from _call_changeObedience_32
                            show hima:
                                zoom 0.8

                            him"Y-yeah right! Sure you are..."
                            show hima:
                                zoom 0.6
                            
                            himt"Stupid perv!"
                            show hima:
                                zoom 0.5
                            $ renpy.sound.play("/audio/soun_fx/himawari/himascoff1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                            "[him_name] retreats to her bedroom..."
                            show hima:
                                easein 1 xpos 1.50

                "Keep staring":
                    $ stareass = True
                    show hima with dissolve:
                        zoom 1.4
                    bot"Fuck me..."
                    call increaselust pass (10) from _call_increaselust_24
                    bot"Is it my condition affecting me or was I always this pervy..."
                    show hima comment1 with vpunch:
                        zoom 1
                    show hima with dissolve:
                        zoom 0.5
                    call changeRespect("Himawari", -1, "none") from _call_changeRespect_41
                    "She notices the awkward silence while she was walking away, perhaps expecting you to fire-back at her attempt to ridicule your condition..."
                    "She quickly covers herself up and retreats to her bedroom..."
                    hide hima with dissolve
                    bot"Shit! Did she notice me staring?"
                
        
    hide hima with dissolve
    
    show boruto surprised at right with dissolve
    show hina assertive at left with dissolve:
        zoom 0.7
    with vpunch
    bot"oops..."
    bot"[hin_rel] has a scary look on her face..."
    if stareass == True:
        bot"Did she notice me staring at my [him_rel]'s ass too!?"
        hint"Was he...?"
        call changeRespect("Hinata", -1, "none") from _call_changeRespect_42
        if boruto_clinic_gropemom == True:
            hint"He also did... that, back in the clinic!"
            call changeRespect("Hinata", -1, "none") from _call_changeRespect_43
        hint"It can't be... He knows we are a family after all!"
        hint"Must be my imagination..."
    hin"[bo_name]! This petty fighting between you two must stop"
    menu:
        hin"[bo_name]! This petty fighting between you two must stop"
        "She is the one who started it":
            show boruto angry with dissolve
            bo"But [hin_rel], she is always the one who starts it."
            call changeRespect("Hinata",-1, "none") from _call_changeRespect_44
            show boruto angry2 with dissolve
            bo"What am I supposed to do, sit there and take it?"
        "I know, I will be better":
            show boruto worried with dissolve
            bo"You are right [hin_rel]. I know she is my little [him_rel] and I should start acting as I would want her to."
            show boruto worried2 with dissolve
            bo"Otherwise the more I antagonize her, the worse she will get."
            call changeRespect("Hinata",2, "none") from _call_changeRespect_45    
            hin"You got the right idea."
        "You are right, she will learn to respect me":
            show boruto sceeming with dissolve
            bo"I agree, which is why I will change the way I am dealing with her..."
            call changeDominance(1, "none") from _call_changeDominance_11
            show boruto sceeming2 with dissolve
            bo"From now on, she will learn to respect me!"
            hint"Uuuh, what does he mean by that..."
            hin"Just... try to be better."
    $ renpy.sound.play("/audio/soun_fx/hinata/hinatasigh1.opus", channel="sfx3", loop=False, relative_volume = 0.4)
    hin"*Sigh*"
    show hina talking with dissolve:
        zoom 0.72
    show boruto normal with dissolve
    hin"[bo_name] Listen, I know your [him_rel] can be abrasive at times but you can always try to be the bigger person when it comes to your arguments."
    hin"Be an example to her, be stronger! And yes, take a hit or two if that is what it takes."
    hin"That is what a man is, [bo_name]. A sturdy rock, a pillar of emotional support. One which his family can rely on when they need it most!"
    hin"Do you understand, my [hin_rel_to_bo]? Can you do that for your [him_rel]?... For me?"
    bo"[hin_rel]..."
    show boruto worried with dissolve
    bot"Damn me, [hin_rel] has a way with words..."
    bot"If only I wasn't the way I am..."
    menu ifonly:
        bot"If only I wasn't the way I am..."
        "I will try, [hin_rel]":
            show boruto normal with dissolve
            bo"I know, [hin_rel]. I will be better."
            show boruto worried with dissolve
            bo"With [na_rel] being away... I know, now more than ever that you and [him_name] need someone to rely on."
            bo"I will work towards becoming someone you can rely on..."
            show boruto worried2 with dissolve
            bo"Your sturdy rock."
            show hina talkinghappy with dissolve
            show hina:
                linear 0.5 xpos 0.4
            pause(0.5)
            hide hina with dissolve
            hide boruto with dissolve
            show hug normal with dissolve:
                zoom 0.8
                xalign 0.5 yalign 0.99
            "[hin_name] moved closer to you and gave you an unexpected hug."
            call changeLove("Hinata",1, "none") from _call_changeLove_11
            hin"That is what I want to hear, my [hin_rel_to_bo]..."
            show hug normal with dissolve:
                zoom 1.4
                xalign 0.5 yalign 1.0
            bot"Although there is another sturdy rock growing down there..."
            call increaselust pass (5) from _call_increaselust_25
            show halfblack with dissolve
            
            bot"Even the slightest touch is making me aroused..."
            bot"Must be the effect of my condition..."
            hide boruto boner0 with dissolve
            hide halfblack with dissolve
            show hug normal with dissolve:
                zoom 0.9
                xalign 0.5 yalign 0.99
            window hide
            pause 1
            window show
            bot"But then again, [hin_rel] is just so..."
            menu:
                bot"But then again, [hin_rel] is just so..."
                "Affectionate":
                    bot"She is so affectionate lately..."
                    bot"Not that I am complaining. It has been so long since she has last been like this..."
                    bot"Perhaps this condition of mine isn't so bad if it serves as the catalyst that brings us closer."
                "Sexy":
                    bot"Fuck me! Can you even blame me?"
                    bot"She is just so fucking hot..."
                    bot"I am slowly losing any sign of inhibition I've had..."
                    bot"I don't care if she is my [hin_rel], I just want to... feel her. More and more, until..."

                
            hide boruto boner0 with dissolve
            hin"My sweet boy..."
            bot"If I am not careful she might notice my boner..."
            menu:
                "..."
                "Hug her tightly":
                    show hug home11t with dissolve
                    hin"O-Oh!..."
                    call increaselust pass (5) from _call_increaselust_26
                    "You wrapped your hands around her waist, pulling her pelvis closer to yours..."
                    call changeDominance(1, "none") from _call_changeDominance_12
                    hin"E-easy d-does it... Are you o-okay [bo_name_stutter]?"
                    hint"He must be emotional after today's events..."
                    bo"It's just... everything that happened today, It is a lot to deal with..."
                    bo"Thank you, [hin_rel]... For being supportive."
                    hin"Y-yes... don't worry about it, I will always be there for you."
                    hint"This hug is lasting a bit too long..."
                    menu:
                        "..."
                        "Pull her closer":
                            show hug home2t with dissolve:
                                zoom 1.1
                            show hug at smallshake
                            bot"Being skin to skin with [hin_rel], feeling her body's warmth..."
                            bot"It is such a warm and fuzzy feeling. I kinda want to..."
                            window hide
                            show hug home2t with vpunch:
                                zoom 1.3
                            pause 1
                            window show
                            call changeDominance(1, "none") from _call_changeDominance_13
                            show hug at smallshake
                            hin"[bo_name_stutter]? Y-you are h-holding me a bit too tight, don't you think?"
                            bot"I just need to say some soapy stuff to not spook her too much..."
                            bo"[hin_rel], It's just... you are so important to me; I fear of what would become of me if you weren't as supportive as you are."
                            show hug home2t with vpunch:
                                zoom 1.35
                            show hug at smallshake
                            bo"Thank you..."
                            show hug home2t with vpunch:
                                easein 5 yalign 0.85
                            "Your waist was rubbing against hers while your erection slowly grew and pushed against your [hin_rel_mother]'s legs..."
                            bot"[hin_rel]'s tits... They are pressing against my chest!"
                            call increaselust pass (5) from _call_increaselust_27
                            "[hin_name] could feel your slight movements against her waist but in her mind, she dismissed it as affection after a traumatic event..."
                            "She could not possibly suspect that her [hin_rel_to_bo] was intentionally rubbing his boner against her pelvis..."
                            show hug home2t with dissolve:
                                zoom 0.8
                            hin"You are my [hin_rel_to_bo]... [bo_name]!"
                            hin"I will always be there for you no matter what, but..."
                            hin"Can you let go of me please? My waist is starting to ache..."
                            
                            hide hug with Dissolve(0.3)
                            bo"O-oh! I am sorry..." with vpunch

                        "Don't":
                            bot"I better not. [hin_rel] would be weirded out."
                            hide hug with dissolve
                        
                    
                "Don't":
                    bot"I better not. What if she gets scared of being affectionate because of my stupid erections..."
                    hide hug with dissolve
                

        "I will try, but only for you":
            bo"I will do what I can, [hin_rel]..."
            show boruto suspicious with dissolve
            bo"But no promises when it comes to [him_name]. That girl is just... too much lately."
            show hina assertive with dissolve
            hin"You have to try, for [him_name] too!"
            hin"She is your [him_rel], [bo_name]!"
            bo"Yeah, yeah I get it [hin_rel]..."
    
        "{color=#9c0303}Lie nefariously{/color}": 
            show boruto sceeming with dissolve
            bo"You are both important to me, [hin_rel]. I will be your support..."
            $ renpy.sound.play("/audio/soun_fx/horror.opus", channel="sfx2", loop=False, relative_volume = 0.5) 
            call borutoevil2 from _call_borutoevil2_2
            call changeHatred(1, "none") from _call_changeHatred_17
            bot"...And you'll both be mine! Wrapped around my finger to do with as I please."
            bot"Little by little, I will break [him_name]'s feeble mind, until she is begging for my forgiveness."
            bot"And when I am done with her, maybe you will be next!"
            show boruto sceeming with dissolve
            show hina surprised with dissolve
            hin"Hmmm..."
            call changeRespect("Hinata",-1, "none") from _call_changeRespect_46
            hint"That did not sound very sincere..."
            show hina assertive with dissolve
            hint"But it could be my imagination."
            show boruto surprised2 with dissolve
            bot"What's with [hin_rel]'s look... is she a mind-reader or something!?"


    hide halfblack2 with dissolve
    hide halfblack with dissolve
    show hina concerned at left with dissolve:
        zoom 0.7
    show boruto normal at right with dissolve
    hin"*Sigh*"
    show hina talking with dissolve:
        zoom 0.72
    hin"Now listen, there are a few things we need to discuss between us, [him_name] does not need to hear about any of this..."
    hin"Do you understand what I am implying, [bo_name]?"
    bot"Here comes the grilling..."
    bo"I know [hin_rel], it is probably for the better."
    hin"Right..."
    hin"Let us start from the beginning..."
    if lie_about_ino == True:
        hin"I know that back in the clinic, you said you don't remember much of what happened..."
        hin"But that does not revoke your acountability in what has transpired."
        menu:
            bo"..."
            "Keep up the facade":
                bo"[hin_rel], my memory is still blurry. What even happened?"
                bo"You are making it sound like I killed someone..."
                hin"[bo_name], your condition, what lady Tsunade said, Ino... "
                hin"I don't think I can spell it out for you but I am sure you can put the dots together..."
                call changeRespect("Hinata", -1, "none") from _call_changeRespect_47
                hin"Can't you?"
                bo"O-oh... Oh!"
                bo"I- I am sorry, [hin_rel]. I must have been possesed, spaced-out or s-something..."
                bo"I don't remember any of... that."
                hin"Hmm..."
                bot"She seems skeptical... I hope she bought the facade i put up."
            "Concede the truth":
                bo"[hin_rel], I..."
                show boruto worried with dissolve
                bo"I have been slowly regaining my memories, I remember now."
                call changeHatred(-1, "none") from _call_changeHatred_18
                show boruto worried2 with dissolve
                bo"What I have done to Ino is... unforgivable."
                bo"I am sorry, [hin_rel]. I wasn't in control of my actions."
                bo"And even that does not excuse what I did..."
                call changeRespect("Hinata", 1, "none") from _call_changeRespect_48
                hin"You are right, it does not. But..."
    show boruto worried with dissolve   
    show hina concerned with dissolve
    hin"When I found you with Ino in the street, I knew the moment I saw your eyes, that something was off"
    hin"The only reason I can cope with all this, is knowing that the curse was in control of your actions."
    hin"And while I am willing to see past what you did given the circumstances, along with what we have heard from lady Tsunade..."
    hin"I don't think Ino will be able to forgive you as easily, if at all, ever."
    if ino_fainted == True:
        hin"The things I have seen, [bo_name]... I can't even put them into words."
        window hide
        show ino_hinata 0 with flash:
            zoom 1.05 xalign 0.5 yalign 0.5
        pause 0.3
        hide ino_hinata 0 with dissolve
        window show
        hin"Ino might be forever traumatized and to be honest with you..."
        window hide
        show ino_hinata 2 with flash:
            zoom 1.05 xalign 0.5 yalign 0.5
        pause 0.3
        hide ino_hinata 2 with dissolve
        window show
        hin"I will need some time as well to process what I... experienced"
        hin"I know that in the moment, you were not yourself. I know that whatever is inside you compelled you towards that... evil."
        hin"I have seen what this curse is capable of in the past with your [na_rel]..."
        hin"But to see my own [hin_rel_to_bo], in that... scene, with my dear friend..."
        hin"Even if it was in your puppet-like state, you can see how this is... difficult for me too, right?"
        menu hatred2:
            bot"..."
            "Take your time, [hin_rel]...":
                bo"I understand [hin_rel]. Take as much time as you need."
                call changeRespect("Hinata", 1, "none") from _call_changeRespect_49
                bo"I promise you, I am not a monster..."
                bo"What happened with Ino was... unfortunate. I will make it up to her, somehow."
            "But [hin_rel], It wasn't me!":
                bo"But [hin_rel], It wasn't me!"
                bo"How can you blame me for th-"
                show hina assertive with dissolve
                hin"ENOUGH!" with vpunch
                
                call changeRespect("Hinata", -2, "none") from _call_changeRespect_50
                hin"[bo_name], you can't keep using your condition as an excuse!"
                hin"Think of Ino for a second! Do you think you can just tell her that?"
                hin"Would that make it up for everything that happened to her!?"
                hin"You need to be better than that!"
                hin"You have to take responsibility of your actions; now, and in the future!"
                bo"Y-you are right... I am sorry."
                
            
    show blackscreen with dissolve
    show hina assertive
    show boruto worried
    hide blackscreen with dissolve
    bo"What do I even say to her, [hin_rel]?"
    hin"Well..."
    show hina talking with dissolve
    hin"Listen [bo_name]..."
    hin"As hard as this is to deal with for us, it is certainly much harder for Ino herself."
    hin"I will talk with her and explain what we heard from Lady Tsunade."
    hin"Don't rush things, give her time to recover and be sincere when it is time to ask for forgiveness."
    hin"Until then, it is best you avoid contact with her, Understood?"
    menu untilthenino:
        "..."
        "Okay...":
            bo"I know, I'll stay away for now...."
            call changeRespect("Hinata", 1, "none") from _call_changeRespect_51
            hin"Good."
        "{color=#9c0303}Hide the truth{/color}" if hatred > 5:
            bot"I can't tell her how I really feel yet, she would probably kill me herself. But when the time is right... hehehe!"
            bo"I know [hin_rel]. Seeing your friend like that, I am sure it was hard on you..."
            $ renpy.sound.play("/audio/soun_fx/horror.opus", channel="sfx2", loop=False, relative_volume = 0.5) 
            call borutoevil from _call_borutoevil
            call changeHatred(1, "none") from _call_changeHatred_19
            bo"As it was hard for me..."
            bot"Yes, so hard..."
            bot"If only you knew, [hin_rel]... how 'hard' I was as I was about to penetrate Ino"
            bot"I enjoyed every second of breaking your dear friend's character."
            bot"And if you weren't there, I would enjoy ravaging her holes too."
            bot"For denying me that pleasure..."
            bot"Maybe I will enjoy breaking you in her stead!"
            show boruto normal with dissolve
            bot"..."
            bo"I understand how Ino must be feeling too..."
            hin"Good..."
            show boruto sceeming2 with dissolve
            bot"And I really don't care!"
            show boruto normal with dissolve

        "{color=#bdbdbd}(Missing hatred){/color}" if hatred <=5:
            "Your 'hatred' stat has to be at least '6'"
            jump untilthenino
    hin"There is something else we need to discuss..."
    bo"What's that, [hin_rel]?"
    show hina thinking with dissolve
    hin"Uuuh..."
    show blackscreen with dissolve
    hide hina
    show hina pthinking2 at mid with dissolve
    hint"Darn it... I am really not good at talking about these things."
    show hina pthinking at mid with dissolve
    hint"If only his [na_rel] was here. It would make things much simpler..."
    hide hina with dissolve
    hide blackscreen with dissolve
    show hina surprised at left with dissolve:
        zoom 0.7
    hin"Uuuh..."
    hin"You know... the t-things Lady Tsunade mentioned..."
    show boruto snob with dissolve
    bot"This will be an interesting talk if it's about what I am thinking..."
    default hinagirltalk = False
    default jokeaboutgirls = False

    menu:
        bot"This will be an interesting talk if it's about what I am thinking..."
        "Pretend you don't understand":
            show boruto suspicious with dissolve
            bo"What things [hin_rel], I don't understand..."
            show hina thinking with dissolve
            hin"Y-you know... the treatment methods Lady Tsunade mentioned?"
            hin"D-did your [na_rel] ever talk to you about... t-that?"
            menu:
                hin"D-did your [na_rel] ever talk to you about... t-that?"
                "Keep pretending":
                    show boruto surprised2 with dissolve
                    bo"...That? And how does [na_rel] fit in this anyway, he is away [hin_rel]."
                    show boruto worried with dissolve
                    bo"I have no idea what you are talking about. Can we speak in plain terms?"
                    show hina concerned with dissolve
                    hin"Come on, [bo_name]."
                    hint"...Are you really this dense?"
                    call changeObedience("Hinata",1, "none") from _call_changeObedience_33
                    hint"I suppose there is no way out of this for me..."
                    hin"Mmmmh! *exhales*"
                    "[hin_name] puffs herself up, readying up for what she considered an awkward speech."
                    hin"Okay! Listen..."
                    hin"Lady Tsunade said that with your condition, you will often feel..."
                    hin"A... c-certain way... down there."
                    show boruto worried2 with dissolve
                    bo"A certain way... down there?"
                    show boruto sceeming with dissolve
                    bot"If only you knew, [hin_rel]!"
                    show blackscreen with dissolve
                    hide boruto
                    show boruto boner0 with dissolve:
                        zoom 1.3 xalign 0.1 yalign 0.3
                    call increaselust pass (5) from _call_increaselust_28
                    bot"That this is exactly how I am feeling right now"
                    hide boruto boner0 with dissolve
                    hide blackscreen with dissolve
                    show boruto sceeming at right with dissolve
                    hin"You know... the way boys get when they get... excited?"
                    hin"It will feel... maybe a little bit painful and your...-"
                    menu:
                        hin"It will feel... maybe a little bit painful and your...-"
                        "I was just kidding, [hin_rel]":
                            show boruto laughing with dissolve
                            bo"I know [hin_rel], I was just playing around.. *Giggles"
                            hin"[bo_name]! Y-you..."
                            show boruto laughing2 with dissolve
                            bo"It was funny seeing you flustered"
                            show hina assertive with dissolve
                            show boruto surprised
                            call changeRespect("Hinata", -1, "none") from _call_changeRespect_52
                            hin"It was absolutely not!" with vpunch
                            menu :
                                hin"It was absolutely not!"
                                "Be respectful":
                                    show boruto smirk with dissolve
                                    bo"Yyyeah, that might have been a little bit stupid. Sorry [hin_rel]."
                                    show boruto normal with dissolve
                                    bo"You don't have to worry though, I think I will be alright."
                                    call changeRespect("Hinata", 2, "none") from _call_changeRespect_53
                                    show hina concerned with dissolve
                                    "[hin_name] lets out a soft moan of annoyance but also of relief..."
                                    hin"Mmmmmh!"
                                    hin"You silly goose!"
                                    hin"Don't put me in on the spot like that..."
                                    show boruto smirk2 with dissolve
                                    bo"Hehe..."
                                    show boruto worried with dissolve
                                    bo"The thing is..."
                                    jump ohthat

                                "Be vulgar":
                                    show boruto snob with dissolve
                                    bo"Oh come on! It was funny."
                                    show boruto smirk2 with dissolve
                                    bo"You tried to describe penile function as if it were a foreign satanic concept! *Giggles*"
                                    show boruto sceeming2 with dissolve
                                    bo"It is just a dick [hin_rel], I can stroke it myself if it reaches that point."
                                    show hina concerned with dissolve
                                    call changeRespect("Hinata", -1, "none") from _call_changeRespect_54
                                    hin"[bo_name_stutter]!" with vpunch
                                    show boruto snob with dissolve
                                    call changeObedience("Hinata", 1, "none") from _call_changeObedience_34
                                    hin"You don-t h-have to be so... vulgar!"
                                    show boruto worried with dissolve
                                    bo"The problem is..."
                                    jump ohthat
                                
                        "Oh, that. It is really painful [hin_rel]":
                            show boruto surprised2 with dissolve
                            bo"Oh, that!"
                            label ohthat:
                                show boruto sad with dissolve
                                bo"It really does hurt when it happens, [hin_rel]. It also makes me... think strange."
                                bo"It felt like that with Ino... when I-"
                                show hina surprised with dissolve
                                hin"I know... [bo_name]" with vpunch
                                "[hin_name] interrupted you before you could recount an event she imagined could be traumatic to you, but also to her."
                                hin"It is the effect your condition has on you. Just like Lady Tsunade mentioned..."
                                hin"Which is why it is important you don't let yourself stay like that for too long."
                                hin"You have to take care of yourself, do you understand?"
                                menu:
                                    hin"You have to take care of yourself, do you understand?"
                                    "I will do what I can, [hin_rel]":
                                        bo"I know, [hin_rel]. I'll do my best but..."
                                        show boruto sad2 with dissolve
                                        bo"Some times I just can't seem to take care of... myself. What do I do then?"
                                        show hina concerned with dissolve
                                        hin"Well, we will have to talk with Tsunade and see if there's anything we can do."
                                        hin"Until then, you are about that age now [bo_name]..."
                                        hin"You need to start talking with girls and forming relationships..."
                                        show boruto surprised2 with dissolve
                                        hin"Ever thought about getting a girlfriend?"
                                        jump getagirlfriend
                                    "What if I can't do it... alone?":
                                        show boruto worried2 with dissolve
                                        bo"But... What if I can't do it by myself [hin_rel]?"
                                        hin"W-well..."
                                        show hina concerned with dissolve
                                        
                                        hin"You are just going to have to find someone to h-help, I suppose."
                                        show boruto surprised2 with dissolve
                                        hin"Ever thought about getting a girlfriend?"
                                        menu getagirlfriend:
                                            hin"Ever thought about getting a girlfriend?"
                                            "Don't need one when I have you two!" if jokeaboutgirls == False:
                                                show boruto snob with dissolve
                                                bo"I have two of those right here at home..."
                                                show hina concerned with dissolve
                                                hin"W-What!?" with vpunch
                                                show hina assertive with dissolve
                                                call changeRespect("Hinata", -1, "none") from _call_changeRespect_55
                                                hin"Is this another one of your stupid jokes?"
                                                hin"[bo_name]! You can't be thinking of me and your [him_rel] like that!"
                                                hin"We are family for god's sake!"
                                                menu:
                                                    hin"We are family for god's sake!"
                                                    "Play it off as a joke":
                                                        show boruto laughing2 with dissolve
                                                        bo"Relax [hin_rel], I was just joking. *Giggles*"
                                                        call changeRespect("Hinata", -1, "none") from _call_changeRespect_56
                                                        hin"Then that was the stupidest joke I have ever heard!"
                                                        show boruto suspicious with dissolve
                                                        hin"Please [bo_name]! Take this seriously."
                                                        $ jokeaboutgirls = True
                                                        jump getagirlfriend
                                                    "I know, but you are just, so...":
                                                        show boruto suspicious with dissolve
                                                        bo"I know [hin_rel], I was just playing around. It's just that... sometimes my mind strays."
                                                        bo"You are both just... so alluring and beau-"
                                                        call changeRespect("Hinata", -1, "none") from _call_changeRespect_57
                                                        show boruto surprised
                                                        hin"[bo_name]! Enough!" with vpunch
                                                        show boruto worried2 with dissolve
                                                        bot"What the hell am I saying!"
                                                        show hina concerned with dissolve
                                                        hin"I truly hope your condition is to blame for whatever strange thoughts you are having."
                                                        call changeObedience("Hinata", 1, "none") from _call_changeObedience_35
                                                        hint"That must have been a bad attempt at humour..."
                                                        hint"Otherwise this will be more troublesome than I thought."
                                                        show hina assertive with dissolve
                                                        hin"Can we go back to being serious now?"
                                                        $ jokeaboutgirls = True
                                                        jump getagirlfriend

                                                    
                                            "I am not that good with girls... [hin_rel]":
                                                bo"Uuh... I don't know about that, [hin_rel]. I am not that good with girls, yet."
                                                bot"To be honest I am still a virgin, but I would rather not say that to [hin_rel]."
                                                bot"Tsunade's handjob was actually the closest I got to losing my virginity..."
                                                show hina concerned with dissolve
                                                hin"You still have to try, right?"
                                                show hina thinking with dissolve
                                                hin"Hmm..."
                                                hin"Maybe I can even teach you a thing or two about how to approach girls."
                                                show boruto surprised with dissolve
                                                "Your mind started racing with possible implications..."
                                                menu:
                                                    hin"Maybe I can even teach you a thing or two about how to apporach girls."
                                                    "You mean we could 'practice' together?":
                                                        show boruto surprised2 with dissolve
                                                        bo"You mean I could practice with you, [hin_rel]?"
                                                        show hina concerned with dissolve
                                                        hin"P-practice?" with vpunch
                                                        "The way you worded yourself caught her by surprise..."
                                                        call changeObedience("Hinata", 1, "none") from _call_changeObedience_36
                                                        hin"M-maybe practice is not the right word..."
                                                        hin"I meant m-more like... answering questions you might have."
                                                        show boruto worried2 with dissolve
                                                        bo"But what if I need the practice, [hin_rel]?"
                                                        show hina assertive
                                                        hin"Then you do that with girls you meet, you doofus!"
                                                        call changeRespect("Hinata", -1, "none") from _call_changeRespect_58
                                                        show hina at smallshake
                                                        hin"Not with your [hin_rel]!"
                                                        hin"*Sigh...*"
                                                    "That would be great!":
                                                        show boruto surprised2 with dissolve
                                                        bo"That would be great, [hin_rel]!"
                                                        show hina talking with dissolve
                                                        bo"I..."
                                                        menu:
                                                            bo"I..."
                                                            "Concede that you are a virgin":
                                                                show boruto worried with dissolve
                                                                bo"I could use all the help I could get..."
                                                                show boruto worried2 with dissolve
                                                                bo"I..."
                                                                bo"I am actually s-still a virgin, [hin_rel]"
                                                                show hina concerned with dissolve
                                                                hin"That's alright, [bo_name]. You are still young..."
                                                                show hina talkinghappy with dissolve
                                                                
                                                                hin"Besides, I could already tell. *Giggles*"
                                                                show boruto surprised with dissolve
                                                                hin"I have never seen you with a girl after all..."
                                                                show boruto sad with dissolve
                                                                bo"[hin_rel]..."
                                                                show hina talking with dissolve
                                                                hin"Don't be embarassed, there is no shame in that."
                                                                call changeRespect("Hinata", 1, "none") from _call_changeRespect_59
                                                                hin"Quite the opposite actually, it takes guts to admit!"
                                                                show boruto smirk with dissolve
                                                                bo"Eheh..."
                                                                jump endingconv

                                                            "Compliment her":
                                                                show boruto smirk with dissolve
                                                                bo"I would be learning from the best..."
                                                                bo"And most beautiful girl in the world."
                                                                show hina talkinghappy with dissolve
                                                                hin"*Giggles* [bo_name], stop!"
                                                                hin"Since when are you one to throw compliments like that..."
                                                                call changeLove("Hinata", 2, "none") from _call_changeLove_12
                                                                hin"Reminds me a bit of your [na_rel] and his soapy one-liners!"
                                                                hin"See? You are not as bad as you think you are. Girls typically like things like that."
                                                                hin"But not when they are your [hin_rel]! *Giggles*"
                                                                jump endingconv
                                                            
                                                    
                                            "With the way I am?":
                                                show boruto worried2 with dissolve
                                                bo"With my condition? I am afraid I will just be a burden to whoever is stuck with me."
                                                hint"He is... not wrong. It could be problematic..."
                                                show hina concerned with dissolve
                                                hin"Maybe you are right, but you still have to try, right!?"
                                                hin"We have seen what happens when the curse is left to fester. Lady Tsunade mentioned that it could even get worse if we are not careful!"
                                                menu:
                                                    hin"We have seen what happens when the curse is left to fester. Lady Tsunade mentioned that it could even get worse if we are not careful!"
                                                    "Maybe... you can help then?":
                                                        bo"Then... If we reach that point..."
                                                        show boruto embarassed with dissolve
                                                        bo"M-maybe you could help?"
                                                        show boruto surprised2
                                                        hin"Wha-" with vpunch
                                                        show hina assertive with dissolve
                                                        hin"[bo_name_stutter]!" with vpunch
                                                        hin"I am y-your [hin_rel]! Why would you even suggest that!?"
                                                        show boruto worried2 with dissolve
                                                        bo"It won't be... sexual, [hin_rel]."
                                                        bo"It would be more like a... medical need. To prevent worse from happening!"
                                                        call changeObedience("Hinata", 2, "none") from _call_changeObedience_37
                                                        show hina concerned with dissolve
                                                        hin"Still! You are my [hin_rel_to_bo]. We can't be doing things like that together..."
                                                        show hina talking with dissolve
                                                        hin"*Sigh...*"
                                                        hin"We will approach the situation one step at a time, okay?"
                                                        hin"For now, promise me you will do your best to take care of yourself!"
                                                        bo"I know. I will [hin_rel]..."
                                                        show blackscreen with dissolve
                                                        hide boruto
                                                        show boruto blue 1 with dissolve:
                                                            zoom 1.1 xalign 0.5 yalign 0.01
                                                        "Well, [hin_rel] didn't totally freak out at my suggestion..."
                                                        menu:
                                                            "Well, [hin_rel] didn't totally freak out at my suggestion..."
                                                            "{color=[hatredcolor]}I can coerse her into it!{/color}":
                                                                bot"I can pretend that the pain is unbearable so that she feels compelled to help. Or..."
                                                                show boruto blue 2 with dissolve
                                                                bot"I can even scare her into it or even blackmail her by using [him_name]!."
                                                                call changeHatred(2, "none") from _call_changeHatred_20
                                                                bot"I am going fucking crazy with this shit."
                                                                bot"So many ways to go about it... This will be fun!"
                                                                hide boruto
                                                                hide hina
                                                                hide blackscreen with dissolve
                                                                show hina concerned at left:
                                                                    zoom 0.7
                                                                show boruto sceeming at right
                                                                with dissolve
                                                                
                                                                "Your mind strayed for a while with wicked thoughts..."
                                                                "[hin_name] noticed..."
                                                                hin"You seem lost in thought..."
                                                                show boruto surprised at right with dissolve and vpunch
                                                                bot"Eh!"
                                                                hin"Everything okay?"
                                                                show boruto suspicious with dissolve
                                                                bo"Y-yeah! Don't worry about me [hin_rel]..."
                                                                show hina talking with dissolve
                                                                hint"Hmm..."
                                                                jump endingconv

                                                            "I might be able to convince her":
                                                                bot"Maybe she would be willing to 'help' in some ways if I play out the effects of my condition just a little bit more."
                                                                bot"It would be an opportunity to get closer than ever."
                                                                bot"Pulling on her motherly heart-strings of sorts..."
                                                                call changeHatred(-1, "none") from _call_changeHatred_21
                                                                bot"But I need to be careful otherwise I might spook her off."
                                                                hide boruto with dissolve
                                                                hide blackscreen with dissolve
                                                                show hina concerned with dissolve
                                                                show boruto suspicious at right
                                                                with dissolve
                                                                "Your mind strayed for a while..."
                                                                "[hin_name] noticed..."
                                                                hin"You seem lost in thought..."
                                                                show boruto surprised at right with dissolve and vpunch
                                                                bot"Eh!"
                                                                hin"Everything okay?"
                                                                show boruto suspicious with dissolve
                                                                bo"Y-yeah! Don't worry about me [hin_rel]..."
                                                                show hina talking with dissolve
                                                                hint"Hmm..."
                                                                jump endingconv
                                                       
                                                            

                                                    "You are right":
                                                        bo"You are right..."
                                                        bo"I would hate to burden you, or anyone else for that matter with my problem..."
                                                        bo"I'll do what I can to care for myself, hopefully no one else needs to be involved until I get better..."
                                                        hin"Everything will turn out okay [bo_name]..."
                                                        call changeLove("Hinata", 1, "none") from _call_changeLove_13
                                                        hin"Remember, we are in this together!"
                                                        hin"Just know that you can always talk to me, no matter the situation. We'll find a way through this!"
                                                        jump endingconv
                                            
                    


                "Oh you mean, the sex stuff?":
                    show boruto smirk with dissolve
                    bo"[hin_rel]... are you talking about sex and stuff?"
                    show hina concerned with dissolve
                    label introaware:
                        show boruto suspicious with dissolve
                        bo"Of course I am aware."
                        menu:
                            bo"Of course I am aware."
                            "Pretend you are an expert":
                                show boruto snob with dissolve
                                bo"In fact, I know all there is to know about the sex!"
                                show hina talkinghappy with dissolve
                                hint"The sex?"
                                show hina at smallshake
                                hin"*Giggles*"
                                show boruto surprised2 with dissolve
                                call changeDominance(-1, "none") from _call_changeDominance_14
                                bo"W-why are you laughing [hin_rel]? I am serious!"
                                hin"D-don't mind me, *Giggles*! I just thought of something funny."
                                show hina talking with dissolve
                                hin"Well, since you are an expert on the matter, that saves me the trouble of an uncomfortable discussion..."
                                show boruto angry with dissolve
                                bot"Is she making fun of me?"
                                hin"In any case..."
                            "[na_name] told me a few things":
                                show boruto embarassed with dissolve
                                bo"I spoke with [na_rel] before about it. I am an adult you know, you don't have to be so reserved..."
                                show boruto suspicious with dissolve
                                bo"Besides, sex isn't taboo or anything, right?"
                                call changeObedience("Hinata",1, "none") from _call_changeObedience_38
                                hin"Y-yes, I suppose..."
                                hin"In any case, since you talked with your [na_rel], we can skip the details..."
                        

                    hin"Lady Tsunade said that with your condition, you will often feel..."
                    show hina concerned with dissolve
                    hin"Some excitement... down there."
                    show boruto suspicious with dissolve
                    bot"Oh believe me [hin_rel], I know!"
                    show blackscreen with dissolve
                    hide boruto
                    show boruto boner0 with dissolve:
                        zoom 1.3 xalign 0.1 yalign 0.3
                    bot"In fact..."
                    call increaselust pass (5) from _call_increaselust_29
                    bot"That is exactly how I am feeling right now"
                    hide boruto boner0 with dissolve
                    hide blackscreen with dissolve
                    show boruto normal at right with dissolve
                    hin"Normally that wouldn't be an issue but..."
                    hin"In your case with your condition, It could be... painful. M-maybe stressful even..."
                    jump ohthat
                   
                
        "You know I am not a child, right?":
            show boruto embarassed with dissolve
            bo"Come on [hin_rel], you know I am not a child anymore..."
            show boruto suspicious with dissolve
            bo"We can speak openly about sex or whatever..."
            call changeObedience("Hinata", 1, "none") from _call_changeObedience_39
            hin"I... I don't know about o-openly, but I suppose this occasion demands it..."
            hin"So... you are aware of how these things work?"
            jump introaware
    
    label endingconv:
        scene black with dissolve
        hide boruto
        hide hina
        hin"In any case. To summarize..."
        show bg lr night with dissolve:
            zoom 0.68
        show halfblack with dissolve
        show hina talking at left with dissolve:
            zoom 0.72
        show boruto normal at right with dissolve
        hin"Given the circumstances, I know that you will need some..."
        hin"Alone time... to manage your condition."
        show hina concerned with dissolve
        hin"You can use the b-bathroom for as long as you need."
        show boruto worried with dissolve
        hin"O-okay?"
        hint"Now would be a good time to set some boundaries, as Lady Tsunade suggested..."
        if boruto_clinic_gropemom == True:
            hint"Especially so considering the way he has been acting..."
        bo"O-okay [hin_rel]..."
        show hina surprised with dissolve
        hin"More importantly [bo_name]..."
        hin"I understand you will be experiencing strange... f-feelings or sensations..."
        show hina assertive with dissolve:
            zoom 0.72
        hin"But it is absolutely pivotal that you do not associate these thoughts with those close to you..."
        dev"You have reached a selection menu that contains hidden scenes."
        dev"Hidden scenes are distinct selectable options that are hidden by default unless you meet multiple requirements."
        dev"For just this instance, you will be able to see the options even if you don't meet the requirements so you can familiarize yourself with the secret scene feature."
        dev"Feel free to experiment to discover more secret scenes."
        default introhatredplan = False
        default secretscenelovehandjob = False
        default introsecrethatredcummed = False

        
        menu hiddenscenes:
            hin"But it is absolutely pivotal that you do not associate these thoughts with those close to you..."
            "Why would I...":
                show boruto surprised with dissolve
                bo"You mean you and [him_name]?"
                show boruto surprised2 with dissolve
                bo"We are family, [hin_rel]! I am not a pervert!"
                show hina concerned with dissolve
                hin"Y-you say that but..."
                hin"The way you are acting today is... strange."
                if boruto_clinic_gropemom == True:
                    hint"He did touch me down there back in the clinic..."
                    if stareass == True:
                        hint"Not to mention the way he seemed to be staring at [him_name] just a few moments earlier..."
                    show hina assertive with dissolve
                    bot"Shit! She did notice after all..."
                    call changeRespect("Hinata", -1, "none") from _call_changeRespect_60
                    show boruto worried with dissolve
                    hin"You cannot be doing that [bo_name]! Not with me..."
                    hin"And especially not with your [him_rel]!"
                else:
                    hin"I am worried that with your condition, you might be having weird thoughts about... those around you."
                    hin"Although I hope that you won't..."
                show hina assertive with dissolve
                menu check1:
                    hin"And especially not with your [him_rel]!"

                    "I (probably) won't":
                        bo"I know, [hin_rel], I won't."
                        show boruto worried2 with dissolve
                        bo"At least I will try, but with the way my condition messes with me..."
                        bo"It might not be as simple as that..."
                        show hina concerned with dissolve
                        hin"As long as we all try to deal with this as best we can..."
                        hin"I am sure everything will turn out okay."
                        jump ending_afterclinic

                    "{color=[dominancecolor]}Can you really blame me?{/color}":  #dominance check
                        #call checkDominance(4,"check1")
                        show boruto suspicious with dissolve
                        bo"When you factor in my condition..."
                        show boruto snob behind hina with dissolve:
                            easein 1.2 xalign 0.25
                        
                        bo"Along with beautiful women like you around me..."
                        show boruto snob behind hina:
                            easein 0.3 xalign 0.21
                        $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp1.opus", channel="sfx2", loop=False, relative_volume = 0.5) 
                        show hina concerned with dissolve
               
                        show hinawaist:
                            zoom 0.5 xalign 0.9 yalign 0.1
                        
                        show cutoutborder_white:
                            zoom 0.75 pos (559, -109)
                        with dissolve


                        "You confidently grab [hin_name]'s waist..."
                        bo"Can you really blame me, [hin_rel]?"
                        show hina concerned with dissolve
                        hin"[bo_name_stutter]!"
                        bo"Don't worry too much [hin_rel]. How I feel I might not be able to control due to my condition..."
                        bo"But my actions..."
                        menu check2:
                            bo"But my actions..."
                            "{color=[obediencecolor]}Lower hand{/color}":    #obedience check
                                call checkObedience(4, "check2", "Hinata") from _call_checkObedience_8
                                show boruto sceeming with dissolve                         
                                bo"Those I think..."
                                show hinaass1 at shake with dissolve:
                                    zoom 0.5 xalign 0.9 yalign 0.1
                                $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx2", loop=False, relative_volume = 0.5) 
                                hide hinawaist
                                show hina at shake
                                show boruto sceeming2
                                bo"I can manage!" with vpunch
                                call changeObedience("Hinata", 2, "none") from _call_changeObedience_40
                                hin"H-hey! You can't be doing t-that! I thought I just told you!"
                                menu:
                                    hin"H-hey! You can't be doing t-that! I thought I just told you"
                                    "{color=[hatredcolor]}Grope her!{/color}":
                                        show boruto sceeming with dissolve
                                        bot"I just want to sink my hands in her ass!"
                                        bo"Relax [hin_rel], it's just a little..." 
                                        call changeHatred(1, "none") from _call_changeHatred_22
                                        show boruto sceeming2 with dissolve

                                        $ renpy.sound.play("/audio/soun_fx/groperepeat1.opus", channel="sfx2", loop=False, relative_volume = 0.5) 
                                        show hinacutoutgrope1 with dissolve:
                                            zoom 0.5 xalign 0.9 yalign 0.1
                                        $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx3", loop=False, relative_volume = 0.5) 
                                        show hina at shake
                                        bo"Just a little joke..." with vpunch
                                        hide hinawaist
                                        hide hinaass1
                                        hide hinaass2
                                        bo"It's not a big deal is it?"
                                        hide cutoutborder_white
                                        hide hinacutoutgrope1
                                        call changeLove("Hinata", -2, "none") from _call_changeLove_14
                                        $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp2.opus", channel="sfx2", loop=False, relative_volume = 0.6) 
                                        show boruto surprised at right with dissolve:
                                            easein 0.5 xalign 0.9
                                        hin"N-no!" with vpunch
                                        show hina assertive with dissolve
                                        "She pushes you away..."
                                        hin"[bo_name]! I've had it with your 'jokes'!" with vpunch
                                        call changeRespect("Hinata", -1 ,"none") from _call_changeRespect_61
                                        hin"You have to stop this or I'll have to beat some sense into you!"
                                        hide hina with dissolve
                                        "[hin_name] storms off..."
                                        show boruto sceeming with dissolve
                                        bot"Oops, I scared her off."
                                        bot"I was getting tired of her blabbering anyway, hehe."
                                        jump housetutorial2

                                    "Play it off as a joke":
                                        show hinawaist with dissolve:
                                            zoom 0.5 xalign 0.9 yalign 0.1
                                        show boruto snob with dissolve
                                        bo"Relax [hin_rel], it's just a little joke..."
                                        hide hinaass1
                                        hide hinawaist with dissolve
                                        hide cutoutborder_white
                                        call changeRespect("Hinata", -1, "none") from _call_changeRespect_62
                                        "She moves your hand away"
                                        show hina assertive with dissolve
                                        show boruto snob with dissolve:
                                            easein 0.5 xalign 0.5
                                        hin"Then I'd appreciate it if you stopped fooling around, especially now that we know how your condition affects you..."
                                        show boruto normal with dissolve
                                        call changeLove("Hinata", -1, "none") from _call_changeLove_15
                                        hide hina with dissolve
                                        "[hin_name] storms off..."
                                        bot"Oops, I scared her off."
                                        show boruto smirk with dissolve
                                        bot"I was getting tired of her blabbering anyway, hehe."
                                        jump housetutorial2
                                    
                            "Don't":
                                bo"Those I think I can manage..."
                                bot"She would probably kick my ass if I tried anything stupid, better not risk it..."
                                show hina concerned at left with dissolve
                                show boruto smirk at right:
                                    easein 1 xalign 0.9
                                hide hinawaist with dissolve
                                hide cutoutborder_white
                                hin"T-think!?" with vpunch
                                call changeObedience("Hinata", 1, "none") from _call_changeObedience_41
                                bo"I am kidding [hin_rel]. You can relax!"
                                bot"If only she knew..."
                                jump ending_afterclinic
                        
                        
                    
            "{color=[hatredcolor]}Get angry and 'blame' her{/color}" (secrethatred = True):
                dev"To unlock this hidden scene, max out your 'Hatred' along with your 'Lust' meter"
                call checkHatred(12,"hiddenscenes") from _call_checkHatred_5
                jump secretscenehate 


            "{color=[lovecolor]}I won't [hin_rel]. I promise you that.{/color}" (secretlove = True):
                #go in for hug, reassure, notice boner, bathroom hj
                dev"To unlock this hidden scene, max out [hin_name]'s Love along with your 'Lust' meter"
                call checkLove(4,"hiddenscenes","Hinata") from _call_checkLove_2
                jump secretscenelove 

    label secretscenelove:
        $ initialize_replay_defaults()
        $ secretscenelovehandjob = True
        show boruto worried2 with dissolve
        bo"[hin_rel]... I know that, better than anyone else does."
        show hina talking with dissolve
        bo"I know I might have been acting weird recently but I promise you... I would never willingly do something that would hurt you, or [him_name] for that matter."
        show hina concerned with dissolve:
            easein 1 xalign 0.2
        hin"[bo_name]..."
        show boruto sad2 with dissolve
        bo"But you in turn, have to promise me something as well..."
        hin"...W-what's that?"
        show boruto surprised2 with dissolve
        bo"W-well... You see..."
        show boruto suspicious with dissolve
        bo"My actions I can control, but s-sometimes... With the way my condition messes with my head, I just..."
        show boruto worried2 with dissolve
        bo"I have thoughts or p-physical reactions that are outside of my control."
        bo"If that ever happens  w-with you... can you please promise me you won't hold it against me?"
        bo"That would at least put my mind at ease..."
        show hina concerned with dissolve
        hin"[bo_name_stutter]..."
        hin"I told you before, didn't I?"
        show hina concerned with dissolve:
            easein 1 xalign 0.7
        show blackscreen with Fade(1,0.2,0.2)
        hide boruto
        hide hina
        show secrethug 1:
            zoom 0.4 xalign 0.5 yalign 0.5
        hide blackscreen
        with dissolve
        call changeLove("Hinata",1,"none") from _call_changeLove_16
        hin"We'll get through this together, I promise."
        bo"[hin_rel]..."
        bot"She smells so nice... Her skin is so soft too..."
        show secrethug 2 with dissolve:
            zoom 0.3 xalign 0.5 yalign 1.0
        bot"More importantly, does she not realize how her breasts are-"
        window hide
        show secrethug 2 with dissolve:
            zoom 0.5 xalign 0.5 yalign 1.0
        call increaselust(10) from _call_increaselust_30
        show secrethug 2 with dissolve:
            zoom 0.3 xalign 0.5 yalign 1.0
        bot"Shit! I am having a little bit of a reaction..."
        bo"Uuh... [hin_rel]?"
        show secrethug 2_1 with dissolve:
            zoom 0.35 xalign 0.5 yalign 0.0
        hin"Y-yes?"
        bo"Those physical reactions I was talking about before..."
        show secrethug 3 with dissolve:
            zoom 0.5 xalign 0.5 yalign 1.0
        call increaselust(10) from _call_increaselust_31
        bo"I might be having one of those right now."
        hin"W-what do you mean?"
        $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx3", loop=False, relative_volume = 0.5)
        show secrethug 3 with vpunch:
            zoom 0.3 xalign 0.5 yalign 1.0
        window hide
        pause 1
        hin"O-oh!" with vpunch
        hin"[bo_name_stutter]! W-what the heck is t-that!" with vpunch
        show blackscreen with dissolve
        hide secrethug 1
        hide secrethug 2
        hide secrethug 2_1
        hide secrethug 3
        show boruto bonersurprised at right
        show hina concerned at right behind boruto:
            zoom 0.7 xalign 0.7
        hide blackscreen with dissolve
        show hina concerned:
            easein 0.3 xalign 0.05
        pause 1
        "[hin_name] quickly backed off in embarassment after seeing your 'small reaction'"
        hin"H-how, w-when did that even happen!"
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
       
        bo"I don't know [hin_rel], but it h-hurts..."
        hint"N-no... It's just like when I found him with Ino!"
        hin"Remember what Tsunade said, [bo_name_stutter]!"
        show hina concerned:
            easein 0.5 xalign 0.35
        show boruto bonersurprised2 with dissolve
        hin"Quickly! You have to take care of that before your condition worsens..."


        show hina pushing with fade:
            zoom 0.4
        show hina pushing with dissolve:
            easein 0.4 xalign 0.69   
        show boruto bonersurprisedred with dissolve
        hin"Come on! Don't stare at me! Off to the bathroom you go!"
        show hina:
            easein 0.4 xpos 1.3
        show boruto:
            easein 0.4 xpos 1.5
        bo"Ooo-Okay...! Don't push that hard!" 
        scene black with dissolve
        $ renpy.sound.play("/audio/soun_fx/doorclose.opus", channel="sfx2", loop=False, relative_volume = 2.0) 
        "She pushes you into the bathroom and hastily shuts the door in embarassment."
        scene bg day with dissolve:
            zoom 0.70
        show bg day:
            easein 0.5 blur 40
        show halfblack with dissolve
        show hinadoor 1 with dissolve:
            zoom 0.3 xalign 0.5 yalign 1.0
        "[hin_name] leaned against the door in concern and waited outside to make sure you would be okay..."
        hin"[bo_name]..."
        hint"Just a moment ago, he looked..."
        hint"Darn it! Will he be okay by himself?"
        hint"I truly hope so! My poor boy..."
        scene black with dissolve
        "Meanwhile on the other side of the door..."
        scene otheerside1 with dissolve:
            zoom 0.5
        hide blackscreen with dissolve
        bo"[hin_rel]... Are you there?"
        hin"Y-yes [bo_name]! Is everything okay!?"
        bo"I... I-i am trying, but..."
        bo"Aaaarh!" with vpunch
        show otheerside2 with dissolve:
            zoom 0.5
        hide otherside2 with dissolve
        camera:
            subpixel True 
            matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
            linear 0.30 matrixcolor InvertMatrix(0.95)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.51)*HueMatrix(0.0) 
            linear 0.55 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.05)*HueMatrix(0.0) 
            linear 0.67 matrixcolor InvertMatrix(1.36)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.33)*HueMatrix(0.0) 
            linear 1.00 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.00)*HueMatrix(0.0)
        bo"AAARH!" with vpunch
        hin"[bo_name_stutter]!?"
        bo"It's not... working. It h-hurts so much!"
        scene black with dissolve
        bo"AAARGH!" with vpunch
        show bg day with dissolve:
            zoom 0.70
        show bg day:
            easein 0.5 blur 40
        show halfblack with dissolve
        show hinadoor 4 with dissolve:
            zoom 0.3 xalign 0.5 yalign 1.0
        hide black with dissolve
        hin"[bo_name]... It'll turn out fine t-trust me! Just keep t-trying your best..."
        hide hinadoor 4 with dissolve
        show bg day:
            easein 0.5 blur 0
        show hina concerned at right with dissolve:
            zoom 0.70
        $ renpy.sound.play("/audio/soun_fx/dooropen.opus", channel="sfx2", loop=False, relative_volume = 1.0)
        "[him_name] annoyed by your loud screams, came out of her bedroom to find out what's going on..."
        show hima mad with easeinleft:
            zoom 0.34
        him"[hin_rel]! What the heck is going on! Can you tell [bo_name] to shut it? I am trying to study!"
        hin"[him_name]..."
        hin"Your [him_rel_to_bo] is dealing with his condition... remember? He is doing his best trying to apply his prescribed medication..."
        bo"AAARGH!!" with vpunch
        show hima smug1 with dissolve
        him"It doesn't sound like that idiot is doing that too well then! I and the entire rest of the world can hear his wailing!"
        show hima thinking  with dissolve
        him"Can't you help him apply his medication [hin_rel]?"
        show hina at smallshake
        $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp1.opus", channel="sfx3", loop=False, relative_volume = 0.8)
        hin"N-no!"
        hin"I am a-afraid it's not that s-simple, [him_name]. Please just bear with him for a little while longer, okay? He is in great pain right now... Let's not make things worse."
        show hima at smallshake
        $ renpy.sound.play("/audio/soun_fx/himawari/himascoff1.opus", channel="sfx3", loop=False, relative_volume = 0.5)
        him"Hmmph!"
        show hima snobturn with dissolve:
            zoom 1.0 xalign -0.1
        him"At least tell him to keep it quiet, I am trying to study next door..."
        show hima snobturn:
            easein 0.4 xalign -0.8
        hin"..."
        hide hina with dissolve
        show bg day:
            easein 0.5 blur 40
        show halfblack with dissolve
        show hinadoor 2 with dissolve:
            zoom 0.3 xalign 0.5 yalign 0.0
        hide black with dissolve
        hin"[bo_name]... are yo-"
        show hinadoor 4 with dissolve:
            zoom 0.35 xalign 0.5 yalign 0.0
        bo"Arrh! F-fuck!" with vpunch
        bo"N-nothing's happening [hin_rel]!"
        show hinadoor 2 with dissolve:
            zoom 0.4 xalign 0.5 yalign 0.2
        hint"W-what do I do... Shall I rush to the infirmary!?"
        hint"But I can't leave him alone like this, can I? It's dangerous..."
        show otheerside2 with dissolve:
            zoom 0.5
        bo"Goddamn it it hurts so much!"
        menu:
            bo"Goddamn it it hurts so much!"
            "[hin_rel], what do I do!?":
                show otheerside2 with dissolve:
                    zoom 0.6 xalign 1.0 yalign 1.0
                bo"What do I do, [hin_rel]!?"
                bo"I am n-not feel-"
            "[hin_rel] please! Can you do something?":
                show otheerside2 with dissolve:
                    zoom 0.6 xalign 1.0 yalign 0.0
                bo"[hin_rel] please! Is there anything you can do?"
                bo"I can't take this anym-"
        hide otheerside2 with dissolve
        bo"AAAAAARGHHH!" with vpunch
        show hinadoor 3:
            zoom 0.3 xalign 0.5 yalign 0.2
        him"[hin_rel]!! Tell [bo_name] to shut up already!" with vpunch
        show hinadoor 2 with dissolve
        hint"Darn it! I..."
        bo"Aaaaarrg!" with vpunch
        hint"Am I really t-thinking about it? But I am left with no other option..."
        show hinadoor 1 with dissolve:
            zoom 0.5 xalign 0.5 yalign 0.2
        hin"[bo_name_stutter]... L-listen to me and listen carefully!"
        hin"I w-want you to turn a-around and face away f-from the door... okay?"
        scene black with dissolve
        $ renpy.sound.play("/audio/soun_fx/dooropen.opus", channel="sfx2", loop=False, relative_volume = 1.0) 
        hin"I am c-coming in... don't panic!"
        pause 0.5
        scene otheersidebg:
            zoom 0.5
        show boruto looking at left:
            xzoom -1 zoom 0.36
        show hina concerned at right:
            xzoom -1 zoom 0.75
        with dissolve
        bo"[hin_rel]!?"
        $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx3", loop=False, relative_volume = 0.6)
        show hina at smallshake
        hint"W-why is he nude!"
        hin"[bo_name_stutter]..."
        show hina assertive with dissolve:
            easein 1 xalign 0.8
        hin"Y-you are to say nothing. You need only listen to my voice. You got that?"
        show boruto blue 2_1 with Dissolve(2):
            xzoom -1 zoom 0.36
        bo"O-okay..."
        hin"That was the last word you spoke up until I leave this room..."
        hin"I need you to keep quiet and get in the shower... What I am about to do I will only do this one time because I am left with no other option." 
        scene black with dissolve
        call hideUI from _call_hideUI_48
        hin"Under no cicrumstances are you to turn around and look at me whilst I am..."
        show secretbath1 with dissolve:
            zoom 0.55 xalign 0.5 yalign 1.0
        show secretbath1:
            linear 2 yalign 0.0
        hin"...helping."
        show screen parallaxsecretlovescene("introsecretlovesceneanim") with dissolve
        $ renpy.sound.play("/audio/soun_fx/handjob1.opus", channel="sfx3", loop=False, relative_volume = 0.6)
        "You can control the scene with your cursor."
        speech_bubble_hin "That is all this is, I am just helping you deal with your medical n-needs..." (950, 200, "lefttop")
        speech_bubble_hin "Needless to say, this stays between us. Forever and until the end of time." (950, 200, "lefttop")
        hide screen parallaxsecretlovescene
        show secretbath2 with dissolve:
            zoom 0.55 yalign 0.0
        bot"H-holy... fuck!"
        show screen parallaxsecretlovescene("introsecretlovesceneanim") with dissolve
        $ renpy.sound.play("/audio/soun_fx/handjob4.opus", channel="sfx3", loop=False, relative_volume = 0.6)
        bot"[hin_rel]'s hand... [hin_rel]'s stroking my cock!"
        "Click twice to continue..." 
        window hide
        $ ui.interact()
        bot"I can't believe what's happening... the sensation is unreal."
        speech_bubble_bo "*Moans*" (200, 300, "righttop")
        speech_bubble_hin"..." (950, 200, "lefttop")
        bot"What the hell is up with her technique... It is as if she has done this a thousand times..."
        bot"The way she softens her grip when her hand moves up to the head and lets her fingers massage the tip, oh my fucking lord..."
        bot"It takes everything I have to not explode right as her delicate fingers move up and around my glans..."
        bot"And right as she gets back down to the base of the shaft... she tightens her grip, as if she is commanding for me to cum."
        speech_bubble_bo"*Moans loudly*" (300, 300, "righttop")
        speech_bubble_hin"..." (950, 200, "lefttop")
        bot"I can't take this much longer..."
        "Click twice to continue..." 
        window hide
        $ ui.interact()
        speech_bubble_hin"Did you hear that? I am only helping... Nothing more, nothing less. This one time and one time only." (950, 200, "lefttop")
        menu:
            hin"Did you hear that? I am only helping... Nothing more, nothing less. This one time and one time only."
            "...":
                $ renpy.sound.play("/audio/soun_fx/handjob1.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                speech_bubble_bo"..." (300, 300, "righttop")
            "Keep going [hin_rel]!":
                $ renpy.sound.play("/audio/soun_fx/handjob1.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                speech_bubble_bo"Y-yes... keep going [hin_rel]!" (300, 300, "righttop")
                speech_bubble_hin"Shush. No talking I said..." (950, 200, "lefttop")
        speech_bubble_hin"I am only doing this because I can't stand seeing you in pain [bo_name_stutter], but..." (950, 200, "lefttop")
        speech_bubble_hin"Y-you have to understand... what we are doing now is wrong. You need to be able to take care of your condition by yourself." (950, 200, "lefttop")
        speech_bubble_hin"..." (950, 200, "lefttop")
        speech_bubble_hin"You will only speak to let me k-know when you are c-close... so that you can f-finish by yourself." (950, 200, "lefttop")
        menu:
            hin"You will only speak to let me k-know when you are c-close... so that you can f-finish by yourself."
            "[hin_rel]... Can you go f-faster?":
                speech_bubble_bo "[hin_rel]... I n-need m-more! Go f-faster please~!" (300, 300, "righttop")
                speech_bubble_hin "Shhhhh! Y-you idiot!" (950, 200, "lefttop")
                hint"Even with everything I h-have... It's taking him so much longer than I expected..."
                show screen parallaxsecretlovescene("introsecretlovesceneanim2")
                hint"I s-suppose I have to try even harder..."
                $ renpy.sound.play("/audio/soun_fx/handjob2.opus", channel="sfx3", loop=False, relative_volume = 0.7)
                call changeObedience("Hinata",1, "none") from _call_changeObedience_42
                bot"S-she is actually doing it! She s-sped up!"
                "Click twice to continue..." 
                window hide
                $ ui.interact()
                bot"The s-sensation... it's overwhelming!"



                jump secretsceneloveend
            "...":
                bot"[hin_rel]... No one would last more than a few minutes in your s-service..."
                bot"B-but you expect me to finish by myself? A-after introducing me to pleasure I've never felt before?"
                bot"I don't know If I can do that..."

                jump secretsceneloveend
            
        label secretsceneloveend:
            default introscenecumonhands = False
            speech_bubble_bo"[hin_rel], I am..." (300, 300, "righttop")
            menu:
                bo"[hin_rel], I am..."
                "Warn her...":
                    $ renpy.sound.play("/audio/soun_fx/handjob3.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                    speech_bubble_bo"I am c-cumming [hin_rel]!" (300, 300, "righttop") with flash
                    speech_bubble_hin "O-oka-" (950, 200, "lefttop")
                    hide screen parallaxsecretlovescene
                "Stay quiet...":
                    $ renpy.sound.play("/audio/soun_fx/handjob3.opus", channel="sfx3", loop=False, relative_volume = 0.6)
                    bot"This is it, I can't hold on any longer..."
                    bot"I am sorry [hin_rel] but..."
                    $ introscenecumonhands = True
                    hide screen parallaxsecretlovescene
                    show secretcumnowarning1 with dissolve:
                        zoom 0.55 yalign 1.0
                    $ renpy.sound.play("/audio/soun_fx/cum1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    bot"I'll have to cover your hands with my cum!" with flash

            $ renpy.sound.play("/audio/soun_fx/cum2.opus", channel="sfx2", loop=False, relative_volume = 0.3)
            speech_bubble_bo"Hnggg... A-Ah!" (300, 140, "rightbase") with flash
            if introscenecumonhands == True:
                $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                show secretcumnowarning2 with flash:
                        zoom 0.55 yalign 1.0
                $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                call decreaselust(25) from _call_decreaselust_14
                "[hin_name] could not even react in time as you shot an enormous load of cum right as she was massaging your glans with her unique technique..."
                speech_bubble_hin "[bo_name_stutter]!" (950, 200, "lefttop")
                call changeObedience("Hinata",1,"none") from _call_changeObedience_43
                hint"My h-hand is covered in my [hin_rel_to_bo]'s f-fluids. W-what have I done..."
                speech_bubble_hin "A-are you d-done?" (950, 200, "lefttop")
                speech_bubble_bo"*Panting* Hnghh! N-no ~ Ah!" (300, 140, "rightbase") with flash
                $ renpy.sound.play("/audio/soun_fx/cum6.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                show secretcumnowarning3 with flash:
                        zoom 0.55 yalign 1.0
                speech_bubble_hin "T-there's more!?" (950, 200, "lefttop") with flash
                call decreaselust(25) from _call_decreaselust_15
                speech_bubble_hin "C-careful w-with that!" (950, 200, "lefttop")
                hint"It-s too late to let go now. I can't let him make a mess."
                $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                speech_bubble_bo"*Heavy breathing*" (300, 140, "rightbase") with flash
                "[hin_name] moved her hand back in shock, but the sudden explosion of cum drenched everything around you with your goo..."
                hint"W-what is all t-this!?"
                speech_bubble_hin "[bo_name]... do you feel bett-" (950, 200, "lefttop")
                speech_bubble_bo"*Loud Moaning* Arhh! T-there's more c-coming [hin_rel]!" (300, 140, "rightbase") with flash
                $ renpy.sound.play("/audio/soun_fx/cum11.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                show secretcumnowarning4 with flash:
                        zoom 0.55 yalign 1.0
                speech_bubble_hin "H-how!?" (950, 200, "lefttop") with flash
                speech_bubble_bo"Hnggg... A-Ah!" (300, 140, "rightbase") with flash
                $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                show secretcumnowarning5 with flash:
                        zoom 0.55 yalign 1.0
                call decreaselust(50) from _call_decreaselust_16
                $ renpy.sound.play("/audio/soun_fx/panting.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                speech_bubble_bo"*Heavy breathing*" (300, 140, "rightbase")
                speech_bubble_hin "..." (950, 200, "lefttop")
                hint"I have never s-seen anything l-like this before."
                    



            else:
                $ renpy.sound.play("/audio/soun_fx/cum2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                show secretcumwarn1 with flash:
                        zoom 0.55 yalign 1.0
                pause 0.5
                $ renpy.sound.play("/audio/soun_fx/cum3.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                show secretcumwarn2 with flash:
                        zoom 0.55 yalign 1.0
                call decreaselust(50) from _call_decreaselust_17
                $ renpy.sound.play("/audio/soun_fx/panting2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                speech_bubble_bo"*Panting*" (300, 50, "righttop")
                "[hin_name] managed to move her hand back to the base of your cock before you shot an enormous load of cum right as she gripped your shaft..."
                speech_bubble_hin "A-are you d-done?" (950, 200, "lefttop")
                speech_bubble_bo"*Panting* Hnghh! N-no ~ Ah!" (300, 50, "righttop") with flash
                $ renpy.sound.play("/audio/soun_fx/cum5.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                show secretcumwarn3 with flash:
                        zoom 0.55 yalign 1.0
                speech_bubble_hin "T-there's more!?" (950, 200, "lefttop") with flash
                speech_bubble_hin "C-careful w-with that!" (950, 200, "lefttop")
                speech_bubble_bo"Hnggg... A-Ah!" (300, 140, "rightbase") with flash
                $ renpy.sound.play("/audio/soun_fx/cum11.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                show secretcumwarn4 with flash:
                        zoom 0.55 yalign 1.0
                speech_bubble_hin "H-how!?" (950, 200, "lefttop") with flash
                call decreaselust(50) from _call_decreaselust_18
                hint"How is this possible. W-what is all t-this!?"
                $ renpy.sound.play("/audio/soun_fx/panting.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                speech_bubble_bo"*Heavy breathing*" (300, 140, "rightbase")
                hint"I have never seen a-anything like this before."
            
            hint"I can see how he is in so much pain if this is what's pent up inside of him..."
            hint"Not to mention the... s-size of it, that cannot be normal for a boy his age."
            hint"It's almost double the size of his [na_rel]'s for crying out loud!"
            speech_bubble_bo"*Heavy breathing*" (300, 140, "rightbase")
            hide screen parallaxsecretlovescene
            scene secretbath2 with dissolve:
                zoom 0.55 yalign 0.0
            hin "[bo_name_stutter]... A-are you feeling better?"
            show secretbath1 with dissolve:
                zoom 0.6 yalign 0.0 xalign 0.0
            bo"I... t-think so? T-thank you [hin_rel], but..."
            if introscenecumonhands == True:
                scene secretcumnowarning5 with dissolve:
                    zoom 0.55 yalign 1.0
            else:
                scene secretcumwarn4 with dissolve:
                    zoom 0.55 yalign 1.0

            call increaselust(10) from _call_increaselust_32
            bo"Y-your hand... it's still on m-"
            scene black with vpunch
            
            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx2", loop=False, relative_volume = 0.4)
            hin"*Gasps* I-I was lost in t-thought!"
            call changeObedience("Hinata",2, "none") from _call_changeObedience_44
            hin"..."
            hin"I w-will be g-going now. You stay and clean up after yourself. Tomorrow, we both act as if nothing ever happened..."
            hin"And while you are showering t-think about everything I said... Remember, this was the first and last time you u-used my help."
            $ renpy.sound.play("/audio/soun_fx/doorclose.opus", channel="sfx2", loop=False, relative_volume = 2.0)
            show boruto blue 2_1 with dissolve:
                zoom 1.0 xalign 0.5 yalign 0.0
            bot"Think about everything you said...?"
            show boruto blue 2 with dissolve:
                zoom 1.0 xalign 0.5 yalign 0.0
            bot"I have not heard a single fucking thing, [hin_rel]."
            bot"How was I supposed to when I was lost in an abyss of pleasure at your hands..."
            bot"And after experiencing that... I am supposed to never seek that high again? That would be hell on earth..."
            show boruto blue 2_1 with dissolve:
                zoom 1.0 xalign 0.5 yalign 0.0
            bot"But still, I can't believe [hin_rel] jacked me off."
            if introscenecumonhands == True:
                bot"I even plastered her hand with my cum..." 
            hide boruto with dissolve
            bot"And now I am addicted to that feeling..."
            bot"I want more... I need more."
            $ renpy.end_replay()
            $ boruto_location = "hallway"
            window hide
            $ hin_location = 'borutobedroom'
            $ him_location = 'himawaribedroom'
            $ notification (f"{hin_name} Love objective completed")
            $ quest_hin.check("hin1L_5", "done")
            scene bg day with dissolve:
                zoom 0.70 
            # show screen stats
            call hideButtons from _call_hideButtons_2
            call screen housemap





            
            



        
            





    
    label secretscenehate:
        $ introhatredplan = True
        show boruto furious at smallshake with dissolve
        bo"[hin_rel]!"
        show hina concerned with dissolve
        hin"W-what's wrong [bo_name_stutter]?"
        show boruto angry2 at smallshake with dissolve:
            easein 0.8 xalign 0.7
        bo"Do you think I asked for this?"
        hin"N-no..."
        show boruto angry at smallshake behind hina with dissolve:
            easein 0.8 xalign 0.4
        bo"Do you think I want to be like this!?"
        show boruto angry at smallshake behind hina with dissolve:
            easein 0.8 xalign 0.25
        show introsecrethatred 1:
            zoom 0.5 xalign 0.9 yalign 0.1
        show cutoutborder_white:
            zoom 0.75 pos (559, -109)
        with dissolve
        "You bring yourself shoulder to shoulder with your [hin_rel]..."
        "And you press your body against hers, looking down at her from behind..."
        call increaselust(10) from _call_increaselust_33
        show boruto sceeming2 with dissolve
        call changeHatred(1,"none") from _call_changeHatred_23
        bot"I kinda do want to be like this!"
        hin"T-that's not what I meant [bo_name_stutter]... Why are you getting so worked up?"
        bo"Why am I getting so worked up you say?"
        hide introsecrethatred 1
        hide cutoutborder_white
        with dissolve
        show boruto sceeming3 with dissolve
        show introsecrethatred 1b:
            zoom 0.5 xalign 0.9 yalign 0.1
        show cutoutborder_white:
            zoom 0.75 pos (559, -109)
        with dissolve
        
        call increaselust(10) from _call_increaselust_34
        bo"Because my own [hin_rel_mother] keeps trying to blame me for something outside of my control!"
        bo"Because while I suffer... you sit there and criticize my every action!"
        hin"You k-know that's not true..."
        hide introsecrethatred with dissolve
        show introsecrethatred 2b with dissolve:
            zoom 0.5 xalign 0.9 yalign 0.1
        show boruto sceeming3 with dissolve
        show boruto bonerevil2 with dissolve:
            easein 0.5 xalign 0.22
        call increaselust(10) from _call_increaselust_35
        bo"You also know that some things I can't control and yet you keep on nagging me about it."
        bot"I want to fucking grab that dumptruck of hers and take it to pound town..."
        "[hin_name] hasn't realized yet what you were truly thinking about behind her back, let alone what was happening in your pants..."
        hin"B-but you can still try to control your e-emotions... r-right?"
        hide introsecrethatred with dissolve
        show introsecrethatred 3b with dissolve:
            zoom 0.5 xalign 0.9 yalign 0.1
        call increaselust(10) from _call_increaselust_36   
        bo"C-control... my emotions...?"
        menu:
            bo"C-control... my emotions...?"
            "Exercise restraint":
                show boruto sceeming2 with dissolve
                call changeHatred(-1,"none") from _call_changeHatred_24
                bot"As much as I want to... I really shouldn't. She will hate me for it..."
                bo"That... maybe I can do [hin_rel]."
                show boruto worried2 with dissolve
                bo"But..."
                jump exerrestrain
            "{color=[hatredcolor]}Raise your hand behind her back{/color}":
                bo"You see..."
                hide introsecrethatred with dissolve
                show introsecrethatred 4b with dissolve:
                    zoom 0.5 xalign 0.9 yalign 0.1
                bo"This is exactly what I mean... You keep going on and on about control..."
                show boruto bonerevil3 with dissolve
                bo"But can't you understand..."
                menu:
                    bo"But can't you understand..."
                    "{color=[hatredcolor]}I have none!{/color}":
                        call changeHatred(1,"none") from _call_changeHatred_25
                        bo"I have no control!" with vpunch
                        $ renpy.sound.play("/audio/soun_fx/spank5instant.opus", channel="sfx3", loop=False, relative_volume = 0.5)
                        show introsecrethatredspank 1 at shake with vpunch:
                            zoom 0.5 xalign 0.9 yalign 0.1
                        $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx3", loop=False, relative_volume = 0.3)
                        show hina at shake
                        bo"That's the whole fucking issue!" with vpunch
                        hin"*Gasps*!" with vpunch
                        menu:
                            hin"*Gasps*!"
                            "Squeeze her ass before she escapes":
                                $ renpy.sound.play("/audio/soun_fx/grope1.opus", channel="sfx3", loop=False, relative_volume = 0.8)
                                show introsecrethatredspank 1_1 at shake with vpunch:
                                    zoom 0.5 xalign 0.9 yalign 0.1
                                "You grab a handful of her ass and squeeze as hard as you could!"
                                call changeObedience("Hinata",1,"none") from _call_changeObedience_45
                                hin"D-don't touch me like t-that you idiot!" with vpunch
                                hide cutoutborder_white
                                hide introsecrethatredspank
                                hide introsecrethatred
                                with dissolve
                                show boruto bonerevil2 with dissolve:
                                    easein 0.4 xalign 0.8
                                call changeRespect("Hinata",-2,"none") from _call_changeRespect_63
                                "[hin_name] pushes you away." with vpunch
                                $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp5.opus", channel="sfx3", loop=False, relative_volume = 0.4)
                                show hina at shake
                                hin"W-what the heck is that!?  [bo_name_stutter]!" with vpunch
                                bo"I though I just told you. Control [hin_rel]... I have none!"
                                show hina:
                                    easein 3 xpos -1.5
                                hin"Then you better  find some or else next time you try something stupid I'll cut your hands off myself!" with vpunch
                                hin"A-and take care of your c-condition... please!" with vpunch
                                "[hin_name] runs off in embarassment at the sight of your massive boner..."
                                show boruto bonerevil4 with dissolve
                                bot"Don't you worry about that [hin_rel]..."
                                bot"Tonight... I have a plan just for you!"
                                jump housetutorial2

                            "Don't":
                                hide introsecrethatred
                                hide cutoutborder_white
                                hide introsecrethatredspank
                                with dissolve
                                show boruto bonersurprisedred with dissolve:
                                    easein 1 xalign 0.8
                                
                                hin"W-why did you do that you idi-"
                                $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx3", loop=False, relative_volume = 0.3)
                                hin"Eeeeh!?" with vpunch
                                hin"[bo_name_stutter]! W-what the heck is t-that! When did that happ-" with vpunch
                                bo"A-and you think this is e-easy  on me?"
                                bo"I a-am sorry [hin_rel]... my c-condition got the b-better of me."
                                show hina:
                                    easein 0.8 xpos -1.5
                                hin"D-do something about that, please!"
                                "[hin_name] runs off in embarassment at the sight of your massive boner..."
                                hin"And don't you ever try anything like t-that again!" with vpunch
                                show boruto bonerevil4 with dissolve
                                bot"Don't you worry about that [hin_rel]..."
                                bot"Tonight... I have a plan just for you!"
                                jump housetutorial2



                                show boruto bonerevil4 with dissolve
                                bot"Don't you worry about that [hin_rel]..."
                                bot"Tonight... I have a plan just for you!"
                                jump housetutorial2
                            
                    "Exercise restraint":
                        label exerrestrain:
                            hide introsecrethatred
                            hide cutoutborder_white
                            with dissolve
                            show boruto bonersurprisedred with dissolve:
                                easein 1 xalign 0.8
                            bo"I... I have no control. Just l-look at me..."
                            $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx3", loop=False, relative_volume = 0.3)
                            hin"[bo_name_stutter]! W-what the heck is t-that! W-when did that happ-" with vpunch
                            bo"A-and you think this is e-easy... on me?"
                            show hina:
                                easein 0.8 xpos -1.5
                            hin"D-do something about that, please!"
                            "[hin_name] runs off in embarassment at the sight of your massive boner..."
                            show boruto bonerevil4 with dissolve
                            bot"Don't you worry about that [hin_rel]..."
                            bot"Tonight... I have a plan just for you!"
                            jump housetutorial2















          
    label ending_afterclinic:
        show blackscreen with dissolve
        show hina concerned
        show boruto normal
        hide blackscreen with dissolve
        hin"In any case..."
        hin"It is getting late and it has been a long day for all of us."
        hin"I will be upstairs with your [him_rel] to try and convey the severity of the situation to her."
        hin"You should try to get some rest, okay?"
        bo"Yeah..."
        hide boruto with dissolve
        hide hina with dissolve
        jump housetutorial2





    
        
        
            

    


        


        

        
    





