default v21_hinatadate_starskissed = False

# Stat acquisition:
# Level 2 hatred point acquisition here total: 1 - Impulse points: 2
# Level 2 Hinata Love point acquisition here total: 3

######################################################

# WIP commented out, needs CGs



# label v21_hinatadate_repeatable:
#     # Triggered from living room couch.
#     # Requirement: wine, 2 day cooldown (v21_hinatadate_daycounter >= 3)
#     $ v21_hinatadate_daycounter = 0 # Day counter used to track days, resets after each date and doesn't allow dates within 2 days

#     bo "You know [hin_rel], since it's the weekend... Why don't we have another fun night together?"
#     bo "Unless you have something better to do..?"
#     scene hina nightmassage3 with dissolve:
#         yalign 1.0 zoom 1.25
#     show hina nightmassage3:
#         easein 4 yalign 0.0
#     hin "Ooh a fun night out? That does sound quite enticing right now!"
#     hin "What have you organized this time, is Sakura hosting dinner again? I have such a nice time whenever we visit!"
#     if v21_hinatadate_progression == 3:
#         hin "A-although I must admit, stargazing with you was quite lovely."
#         hin "It gave me a sense of serenity that I haven't felt in quite some time..."
#         hin "I wouldn't mind sharing a moment like that again with you if that's what you have planned."
#         hin "Will we be doing something similar tonight?"
#     elif v21_hinatadate_progression == 4:
#         hin "Our last evening sipping wine here on the couch was pretty fun too."
#         hin "Although I think I m-might have gone a little overboard, I don't remember much of what happened."
#         hin "But I do remember waking up in a good mood the morning after, so I'm sure you took great care of me!"
#         hin "Are we doing something similar tonight?"
#     bo "Well don't make me ruin the surprise! You should know better than that!"
#     hin "You and your silly games [bo_name]!"
#     hin "How do I prepare for something I don't know about?"
#     bo "You're just going to have to trust me I guess."
#     hin "Now why in the world would I willingly make that mistake?"
#     if v21_hinatadate_progression > 2:
#         hin "You made me dress up last time even though we weren't even going out!"
#         bo "And you looked and felt amazing in your dress all night..."
#         bo "You were smiling the whole evening, don't try to deny it!"
#         hin "W-well... You're not wrong, it felt nice to dress up for a change."
#         bo "See? I know you better than you think!"
#         bo "The main reason why you have to trust me though is because, well..."
#         $ v21_hinatadate_progression = 1
#     bo "You don't really have a choice! Besides, would I ever lead you astray?"
#     hin "It wouldn't be the first time..."
#     if chosen_hate_path:
#         bo "Oh stop your nagging already [hin_rel] and go get changed!"
#         hin "How do I know what to wear if you're keeping everything so secretive?"
#         bot "The less you wear and the more revealing it is, the better."
#         bo "Remember the dress I bought you?"
#         hin "Oh, the black one? That one is really pretty."
#         bo "Exactly, hurry up and put that on again for me, I bought it for a reason! I'll wait here for you."
#         hin "For y-you? What do you mean by that..."
#         bo "Come on [hin_rel], let's not waste the whole evening here!"
#         hin "Okay, okay... Let me go get ready then."
#     else:
#         bo "Have a little faith in me [hin_rel]!"
#         bo "I promise you'll enjoy yourself regardless of what we do together."
#         bo "These nights are all about you, so relax and let me take care of everything."
#         hin "O-oh, okay... but what should I wear for it then?"
#         bo "Why don't you put on the black dress again, you look absolutely perfect in it."
#         hin "Y-you really think so? I suppose I could wear it again..."
#         hin "Let me go get changed then, I'll be right back."
#         bo "Sure, take your time!"
#     scene black with dissolve
#     "She disappears upstairs into her room for a while while you sit and wait for her on the couch."
#     "When you finally hear her coming back down, your heart races in anticipation and you get up to greet her."
#     scene 00173-2590298243 with dissolve:
#         yalign 1.0 zoom 1.25
#     show 00173-2590298243:
#         easein 7 subpixel True yalign 0.0
#     hin "S-so... How do I look?"
#     hin "I went for the heels again, even though they can be a bit of a pain to walk in."
#     hin "I don't really get many opportunities to wear them, but I think they compliment the dress so nicely!"
#     show screen parallax1280("00173-2590298243",1.25,0.5,True) with dissolve
#     bot "[hin_rel] looks incredible as always! A real certified MILF!"
#     call increaselust(10)
#     bot "I'll never get tired of looking at that body. And this dress leaves nothing for imagination!"
#     bot "I'd love to bury my face in those puppies and let my hands wander up those juicy thighs..."
#     bot "I wonder what color panties she has on right now, I bet I could catch a glimpse if she bends over!"
#     hin "...[bo_name_stutter]?"
#     bo "O-oh sorry [hin_rel], I was just thinking about how beautiful you look tonight in that dress again..."
#     bo "You're absolutely breathtaking!"
#     hin "Oh s-stop it you! You know I blush easily..."
#     bo "Well it's the truth, you always manage to put a smile on my face!"
#     bot "And a rock hard erection in my pants!" with vpunch
#     menu:
#         "{color=[obediencecolor]}Give me a twirl, let's see the whole outfit again!{/color}":
#             bo "Do a quick twirl for me, let's see the whole outfit!"
#             bot "Her juicy ass always looks so divine in it, her curves are accentuated perfectly!"
#             call checkObedience(20, "v21_twirlobediencefail_repeatable", "Hinata", 1)
#             hin "O-okay, sure!"
#             #reuse CG from behind showing off her ass nervously
#             call increaselust(10)
#             bot "There's that ass that I know and love!"
#             bot "I gotta stop myself from just drooling all over for it... \nBut fuck does it look good!"
#             hin "Does it look okay from the back too? It's always hard for me to tell from the mirror."
#             bo "It's stunning! That dress really shows off your figure perfectly."
#             hin "O-oh, that's sweet of you to say, thank you. I'm just glad that it fits!"
#             hin "I'm always a little worried about it being too tight..."
#             bot "Tight is just the way I like you [hin_rel]!"
#             show screen parallax1280("00173-2590298243",1.25,0.2) with dissolve
#             hin "Are you ready to go now? We shouldn't leave Sakura waiting too long if she's expecting us!"
#             pass

#         "Ready to start the evening?":
#             bo "You all done then [hin_rel]? Ready to start the evening?"
#             hin "I think so, yes! We shouldn't leave Sakura waiting too long if she's expecting us!"
#             pass

#     menu v21_hinatadate_optionsmenu:
#         bot "What should we do tonight?"
#         "Go visit Sakura for dinner (Replay)": #bug just a replay for now before it is revised, but could technically be kept like that too
#             bo "Yes, Auntie is waiting! We shouldn't delay much longer or the food might start getting cold!"
#             bo "Let's go!"
#             jump v21_hinatalovelevel2_date_walk

#         "Enjoy the night together alone":
#             bo "Actually [hin_rel], Sakura isn't expecting us..."
#             hin "S-she isn't? Was she not available tonight?"
#             bo "No, it's not that..."
#             bo "I just wanted to surprise you with a special evening together, just the two of us!"
#             bo "I love Auntie, don't get me wrong, but you deserve the full spotlight occasionally too."
#             bot "I'm going to miss out on Auntie being a tease, but I don't want any distractions tonight!"
#             hin "O-oh well, that's very f-flattering [bo_name]..."
#             hin "I-I'm not sure what to say..."
#             hin "But... I'm all dressed up for nothing then if we're not going out. I should probably go change back..."
#             bo "Absolutely not!"
#             bot "Don't you dare!" with vpunch
#             #bug CG hold her hand in front of you POV shot
#             bo "You deserve to look beautiful even when there's no one else around to see it."
#             bo "You should see the smile on your face and twinkle in your eyes every time you wear that dress."
#             bo "It would be a shame to hide that away again."
#             hin "[bo_name]..."
#             bo "You look great [hin_rel]. And this is still a special occasion, after all."
#             hin "I... I s-suppose. But what are we going to do?"
#             bo "I've got it all planned out. First, how about a glass of wine to start the evening?"
#             hin "You brought w-wine?"
#             bo "Of course! I'll go pour us some and let it help us wind down."
#             bot "Time to see if I can get her a little tipsy. Things always seem get more interesting then!"
#             scene black
#             call hidescrollingimage("Click twice to pour some wine!")
#             "You go to the kitchen and pour two glasses of wine, bringing them back to the living room."
#             #bug drink wine at dinner table
#             hin "Thank you, [bo_name]."
#             bo "Anything for you, [hin_rel]."
#             bot "She's only taking small sips. Always so elegant and reserved."
#             bot "I just need to distract her and keep her busy till it starts kicking in, the alcohol will do the rest."
#             bo "This wine is always so smooth and rich, it's no wonder it's Auntie's favorite."
#             hin "Y-yeah she does love her wine... She would be upset to know that we're drinking it without her you know."
#             bo "Don't worry, it'll be our little secret!"
#             "You both share a smirk with each other while imagining the hypothetical consequences if Sakura found out."
#             "Casual conversation flows between you, the atmosphere light and playful, as you slowly go through the evening."
#             "With just the two of you, there is more wine to enjoy, and you both find yourselves loosening up after a few glasses."
#             bot "Time for a slight change of scenery!"
#             bo "[hin_rel] I have an idea, come with me..."
#             scene black with fade
#             "You suddenly get up and place your hand in her palm, encouraging her to follow."
#             hin "S-sure, but... W-where are we going?"

#     menu:
#         "Go outside and watch the stars.":
#             jump v21_hinatadate_repeat_outside

#         "Relax together on the couch with more wine.":
#             jump v21_hinatadate_repeat_inside

# label v21_twirlobediencefail_repeatable:
#     hin "A t-twirl? Is that really necessary right now [bo_name]?"
#     bot "Damn, she's not comfortable enough to show off a little for me..."
#     bot "I'll have to try sneak a peek later when she's not looking instead!"
#     call changeRespect("Hinata", -1)
#     hin "W-why would you even ask that?"
#     hin "We should probably just get going..."
#     bo "Y-yeah, you're right [hin_rel]..."
#     hin "It would be rude to leave Sakura waiting too long if she's expecting us."
#     jump v21_hinatadate_optionsmenu


# label v21_hinatadate_repeat_outside:
#     $ v21_hinatadate_progression = 3
#     bo "Let's go for a little walk, it's such a nice night out that it would be a shame to miss it."
#     hin "Okay, but... you're going to have to make sure I don't fall with these heels on again."
#     bo "I can't make any promises, but I'll try my best!"
#     scene black
#     hin "You're the worst...!"
#     #bug CG holding hands walking in grassy field
#     "You both head outside, the cool night air a pleasant contrast to the warmth of the house."
#     "As you cross the nearby grassy field, you can see the constellations of stars towering above you as they illuminate your path."
#     hin "It's so peaceful out here."
#     bo "It really is. A good escape from the stress of reality."
#     hin "Is reality something you can ever {i}truly{/i} escape though?"
#     hin "Sometimes I j-just... I worry so much about what the future holds."
#     bo "You shouldn't think like that [hin_rel], we'll face it head on as it comes."
#     bo "No need to worry about the unpredictable."
#     #bug CG of her tripping dress could be hiked up a bit and panties flashed
#     "As you walk, [hin_name] stumbles on an uneven patch of ground, her unstable balance in heels finally catching up to her."
#     hin "Whoa!" with vpunch
#     "She starts to fall as she flails her hands frantically, trying to grasp onto you or anything else within reach."
#     scene black with dissolve
#     "You dive to catch her before she hits the ground, but end up only cushioning her fall as you land on the ground together."
#     #bug CG both on the ground her on top of boruto
#     bo "Oof!" with vpunch
#     hin "Clumsy me! S-sorry, [bo_name]."
#     bo "No need to apologize, I got you."
#     bot "Her body is pressed against mine. So soft... so warm from the wine. I can even feel her breasts against my chest."
#     #general comments on the description of whatever the image looks like, maybe have her hand on his crotch accidentally
#     "She pulls back a little flustered but giddy, and you both continue sitting on the ground looking up at the sky."
#     #bug CG stargazing
#     scene stargazingsitting with dissolve
#     bo "I must admit, this is actually the real reason I brought you out here. I know how much the stars call out to you."
#     hin "O-oh? You remembered..."
#     bo "Yeah, you said you love stargazing and looking out into the cosmos."
#     bo "I still find it quite intimidating to stare out into the abyss, but I want to share this with you."
#     call changeLove("Hinata", 1, v21_hinatalove_stargazing, 1, 2)
#     hin "It's very sweet of you to do this for me, thank you."
#     bo "Do you ever wonder if there is anything up there, maybe different planets or dimensions with alternate versions of us?"
#     hin "I would hope so, it would be a shame if it was all empty and meaningless..."
#     bo "Do you think our clones are looking up at the same night sky right now, enjoying life and smiling just as we are?"
#     bo "Or are they complete strangers and lead completely different lives, not tied together in any way?"
#     hin "I actually think the universe can only handle one of you [bo_name]! Any more and the universe would probably collapse in on itself."
#     hin "There's only room for so much chaos in one lifetime."
#     "You can't help but let out a chuckle, knowing full well that she's half-serious."
#     hin "But if there are copies of us somewhere I'm sure that fate would bring them together. Just as how it brought you to me here!"
#     #bug CG Falling star
#     scene stargazingpoint with dissolve
#     hin "Look, a falling star!" with vpunch
#     hin "You know what that means, right? Quick, make a wish!"
#     bo "I don't need to wish for anything. I have everything I could ever want right here [hin_rel]..."
#     bot "Cheesy, but smooth enough that it works every time!"
#     hin "Oh, [bo_name]..."
#     scene stargazingheadsclose
#     "She rests her head on you, as you put your arm around her, pulling her closer."
#     bot "Perfect. Now for the fun part."
#     "Your hand rests on her waist, your thumb stroking her side gently. As she relaxes, your hand starts to drift lower, towards her thigh."
#     bot "Just a little touch... she's had some wine, she might not even notice. Or maybe she'll like it."
#     "Your fingers brush against the soft skin of her upper thigh, just below the hem of her dress."
#     hin "*gasps softly*"
#     bot "Okay she did notice, but she's not moving away. Is this an invitation?"
#     "You grow bolder, your hand moving to gently squeeze her thigh."
#     hin "[bo_name_stutter]..."
#     bo "Yes [hin_rel]?"
#     bot "Her leg is so firm, yet so soft. I want to slide my hand all the way up..."
#     hin "Why do you like spending so much time with your old hag of a [hin_rel_mother]?"
#     bo "A smile on your lips is worth more to me than anything else in this galaxy. You'll always come first!"
#     bo "Besides, I never knew hags could look so beautiful."
#     hin "You're such a sweet boy."
#     #bug CG kiss cheek either black background or have stars
#     "She turns her head and kisses your cheek, her lips lingering for a moment."
#     bot "She's so close and her scent is intoxicating. I want to feel those lips of hers on mine so badly..."
#     menu:
#         "{color=[dominancecolor]}Kiss her on the lips{/color}":
#             if not v21_hinatadate_starskissed:
#                 call checkDominance(0,"v21_hinatadate_kissfail",2)
#                 bo "You can do better than that [hin_rel]."
#                 #bug CG kiss lips
#                 "You turn your head, capturing her lips with yours."
#                 hin "Mmmph!"
#                 bot "She's so soft... Her lips taste of sweet wine with an almost cherry-like aftertaste."
#                 bot "You don't know how long I've wanted this. How long I've waited for this."
#                 bot "And finally, it's happening. I'm starting to make you mine!"
#                 "She pushes weakly against you at first, then seems to melt into the kiss for a moment before pulling away."
#                 call changeLove("Hinata",1,"v21_hinatadate_starsdomkiss",1,2)
#                 "The shame is evident on her face as she guiltily realizes she lingered, even for a second..."
#                 hin "[bo_name]... why did you do that!"
#                 bo "I don't know, it just felt... right!"
#                 hin "It's absolutely not r-right... I'm your [hin_rel_mother]! Your condition must have blurred your mind."
#                 bot "It's always the curse. Such a convenient excuse for the both of us."
#                 bo "But I don't care about that, I only care about you."
#                 bo "It felt good, didn't it?"
#                 hin "N-no... S-stop it!"
#                 hin "The time we've spent together has been... great."
#                 hin "But you've completely lost your mind... Please, we can't be doing this!"
#                 hin "Let's just m-move past this, don't try anything like that again, o-okay?"
#                 bot "You keep pushing me away [hin_rel], but I won't let you go that easily."
#                 bot "I want you too much to let you slip away from me..."
#                 $ v21_hinatadate_starskissed = True
#             else:
#                 bo "I can't... not again..."
#                 bo "[hin_rel] said to not try to kiss her again, it would probably upset her!"
#                 menu:
#                     "{color=[impulsecolor]}Fuck that, those lips are mine!{/color}":
#                         bot "Who cares what she said, she wants it but just doesn't know it yet!" with vpunch
#                         bot "You can't keep those lips from me [hin_rel], not anymore!"
#                         call changeHatred(1)
#                         bot "You've given me a taste of them already and now... I want more!"
#                         "You lean in, throwing caution to the wind and press your lips against hers."
#                         hin "Mmmph!"
#                         bot "They're just as soft as I remember, and I can't get enough of them."
#                         "Caught off guard, she freezes for a moment as the kiss fuses the two of you together before pushing you back."
#                         hin "N-no... we can't..."
#                         bo "Why not? It felt good, didn't it? It felt... right."
#                         call changeRespect("Hinata", -2)
#                         hin "We talked about this [bo_name]! Why do you keep p-pushing me?"
#                         hin "It's inappropriate and crossing a line to be k-kissing my own [hin_rel_to_bo]!"
#                         hin "I don't want to ruin our relationship over a moment of weakness."
#                         bo "We're not ruining anything, if anything we are reinforcing it!"
#                         hin "J-just, stop it! Let's not ruin the evening like this..."
#                         bot "You keep pushing me away [hin_rel], but I won't let you go that easily."
#                         bot "I want you too much to let you slip away from me..."
#                         pass


#                     "I should respect her wishes":
#                         bot "I need to control my urges."
#                         bot "They will ruin everything if I can't keep myself in check."
#                         bot "[hin_rel] needs more time..."
#                         pass

#         "Just enjoy the moment":
#             bot "I shouldn't push it... [hin_rel] would be too upset."
#             bot "It's one thing to hold and caress her, but kissing might be too intimate right now."
#             bot "Let's just savor this moment together."
#             pass

#     label v21_hinatadate_kissfailjump:
#     "You both sit in silence for a while longer, deep in thought while gazing to the skies before deciding to head back home."
#     #reuse one of the CGs to walk home
#     scene 00051-3684313299 with dissolve:
#         yalign 0.2
#     "The events of the night weighing heavily on your foggy minds through the haze of wine, as you walk the path together."
#     hin "I r-really enjoyed tonight, thank you [bo_name]."
#     bo "Not nearly as much as I did!"
#     hin "These nights together really feel s-special... I haven't felt this way in a long time!"
#     hin "Let's do it again sometime soon!"
#     bo "Of course [hin_rel], I never planned on stopping..."
#     bot "Tonight was a complete success. She's slowly opening up to me."
#     bot "I just have to make sure I don't push her too fast. And then soon, she'll be all mine."
#     scene black
#     "You finally reach the front door of your house, entering with a now exhausted [hin_rel] by your side."
#     "You bid her goodnight while looking forward to your next planned night together."
#     if quest.is_state("3_hin2L", "in progress"):
#         $ notification (f"{hin_name} Love Level 2 objective completed")
#         $ quest_hin.check("3_hin2L", "completed")
#         $ quest_hin.check("hin2L_1", "completed")
#         #$ quest_hin.check("hin2L_2", "in progress") 
#     jump action_taken


# label v21_hinatadate_kissfail:
#     "Your body wants nothing more than to kiss her deeply, to claim her lips with your own."
#     "But you don't have it in you, and fear causes you to freeze up instead."
#     bot "I-... I want it so badly but I can't do this..."
#     bot "[hin_rel] would be too upset with me!"
#     bot "R-... right?"
#     jump v21_hinatadate_kissfailjump


# label v21_hinatadate_repeat_inside:
#     bo "Let's get a little more comfortable and move this party to the couch."
#     hin "S-sure..."
#     scene black
#     "You lead her to the couch, and pour the last glasses of wine left from the bottle."
#     scene winedrinkcouchpour with dissolve
#     bo "Another glass?"
#     hin "Maybe just a small one. I'm feeling a little lightheaded already."
#     bot "Excellent. Just as planned."
#     bo "I don't see the problem with that, you're allowed to let go and enjoy yourself tonight [hin_rel]!"
#     scene winedrinkcouch with dissolve
#     "You talk for a while about everything and nothing at the same time, the wine loosening both of your tongues."
#     #bug CG sleepy Hinata on couch
#     "[hin_name]'s demeanor shifts as the night progresses, her responses slowly reduced to soft murmurs and slurred grunts."
#     hin "Thish was r-really nice..."
#     call changeLove("Hinata",1,"v21_hinatadate_wineinside",1,2)
#     hin "Thaank you f-for tonight... It was so lovely..."
#     hin "I'm getting a little... shh-leepy."
#     bo "I should have known you'd bow out first, you are the wine lightweight here after all."
#     "She yawns, her head starting to droop as her eyes struggle to stay open."
#     bo "You can rest your head on my shoulder if you want, no need to force yourself."
#     hin "Mmm... Mhmm... Okay..."
#     scene fallasleepcouch with dissolve
#     #bug some version of her falling asleep
#     "She leans against you, her hair tickling your neck. Soon enough, her breathing evens out as she drifts off to a light state of sleep."
#     $ v21_hinatadate_progression = 4
#     bot "She's so beautiful when she's asleep."
#     bot "Such a peaceful aura to her and so vulnerable with her guard down. Sooner or later she'll be all mine for the taking."
#     #bug CG dress wardrobe malfunction, one breast exposed
#     "As she slightly shifts to get comfortable, her dress falls ever so slightly lower, practically revealing the full swell of her breast."
#     bot "Would you look at that. Someone's trying to pop out and say hello!"
#     menu:
#         bot "What should I do?"
#         "{color=[lovecolor]}Cover her up{/color}":
#             bot "It's not right to take advantage of her like this, I should cover her up."
#             bot "Besides, she'd probably wake up if I tried anything!"
#             bot "She needs her rest and deserves to have it in peace."
#             "You gently adjust her dress to cover her, your fingers brushing against her soft skin."
#             bot "But fuck, she feels amazing. I don't know how much more I can resist the temptation..."
#             bot "I'll just... carry her to bed."
#             hin "[bo_name]...?"
#             bo "Come on [hin_rel], let's get you up to your room."
#             hin "Mmm... Okay..."
#             scene black with dissolve
#             "You carefully lift her into your arms and carry her upstairs to her room, laying her gently on the bed."
#             bo "Goodnight, [hin_rel]."
#             bot "I hope you have the sweetest of dreams..."
#             hin "Th-thank you... Goodnight..."
#             "You lean down and kiss her forehead, lingering for a moment before taking your leave."
#             if quest.is_state("3_hin2L", "in progress"):
#                 $ notification (f"{hin_name} Love Level 2 objective completed")
#                 $ quest_hin.check("3_hin2L", "completed")
#                 $ quest_hin.check("hin2L_1", "completed")
#                 #$ quest_hin.check("hin2L_2", "in progress")
#             jump action_taken

#         "{color=[impulsecolor]}Fully expose her{/color}":
#             bot "She's not in any state to consent, but wasn't that the whole point of all of this?"
#             if hatred.level >=2:
#                 call changeHatred(1,"v21_hinatadate_sleepexposeherlvl2",2)
#             else:
#                 call changeHatred(1)
#             bot "What she doesn't know, can't hurt her..."
#             bot "Time to see some titties!"
#             "You carefully pull her dress lower, fully exposing her breasts as she continues to obliviously sleep."
#             #bug CG tits out
#             bot "Fuck they're incredible! So full... and so soft looking."
#             bot "Why do you hide these and keep them hidden from me under your clothes all day."
#             bot "You should proudly be parading around the house with them bouncing around for me to enjoy looking at!"
#             bot "Those nipples look so suckable... I can't help it, I just want a quick taste..."
#             "Before you manage to lean over and give them a lick, [hin_name] gives a short groan and shifts slightly."
#             hin "-Mmm..."
#             bot "I guess it's too risky for that, she must be feeling the air on her sensitive breasts and waking up."
#             bot "Let's not get caught, we have to play the long game..."
#             hin "... [bo_name_stutter]?"
#             hin "W-what time is it... Why does it feel so c-cold?"
#             scene black with dissolve
#             "[hin_name] glances down and realizes she's exposed, her dress no longer covering her properly."
#             $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
#             "She quickly covers herself up, panic setting in as she processes the situation."
#             #bug either a previous image that fits or one of her getting up
#             hint "H-how long has my dress been like this...?" with vpunch
#             hint "I-I can't believe this... I need to be more careful..."
#             hint "[bo_name]... I hope he didn't notice anything, how embarrassing!"
#             hin "Th-thank you for tonight, I had a really nice time..."
#             hin "W-we should get going now... I'm really t-tired."
#             bo "Of course [hin_rel], you should get some rest."
#             scene black with dissolve
#             "[hin_name] wishes you goodnight and makes her way up the stairs to retire to her room."
#             "You take a moment to admire her figure as she ascends the stairs, her ass bouncing in her dress at every step."
#             scene bg lr night
#             show boruto smirk2 at center
#             with dissolve
#             bot "She's so irresistible..."
#             bot "Too bad I didn't get to enjoy more of her tonight."
#             show boruto sceeming with dissolve
#             bot "There will be more opportunities though, you'll be mine soon [hin_rel]!"
#             show boruto:
#                 easeout 1 xpos -200
#             scene black with dissolve
#             bot "For now though, I should get some rest too..."
#             if quest.is_state("3_hin2L", "in progress"):
#                 $ notification (f"{hin_name} Love Level 2 objective completed")
#                 $ quest_hin.check("3_hin2L", "completed")
#                 $ quest_hin.check("hin2L_1", "completed")
#                 #$ quest_hin.check("hin2L_2", "in progress")
#             bot "Let's see what I can get up to tomorrow!"
#             jump action_taken


########################################################################

# Hatred cut

        # "{color=[hatredcolor]}Grope and fondle her!{/color}":
        #     bot "She won't even know... A little touch won't hurt."
        #     "Your hand moves to her exposed breast, your fingers brushing against her nipple as it hardens instantly at your touch."
        #     bot "Even in her sleep, her body wants me and is aching is to be touched."
        #     "You gently squeeze her breast, feeling its weight in your hand as the palm of your hand indents it."
        #     "Your free hand moves down, over her stomach, to the apex of her thighs."
        #     bot "I wonder if she's wet for me out of reaction to my touch..."
        #     bot "Fuck [hin_rel], show me just how much you enjoy this deep down!"
        #     "You explore her body and gently caress her through her panties, feeling the heat and moisture on your fingertips."
        #     hin "Mmm..."
        #     bot "Shit! Did she wake up?"
        #     "You freeze, but her breathing remains deep and even."
        #     bot "Fucking hell, that's hot. She's moaning in her sleep and probably dreaming about this..."
        #     bot "I'd love nothing more than to rip those panties off and shove my cock inside you [hin_rel]!"
        #     "You continue touching her a while longer before pulling your hands away, your heart pounding from the adrenaline and fear of getting caught."
        #     hin "-Mmm..."
        #     bot "I know, you want more and so do I... But I can't risk waking you up."
        #     bot "Let's not get caught, we have to play the long game..."
        #     "You gently adjust her dress to cover her, your fingers brushing against her soft skin."
        #     bot "But fuck, she feels amazing. I don't know how much more I can resist the temptation..."
        #     bot "I'll just... carry her to bed."
        #     hin "[bo_name]...?"
        #     bo "Come on [hin_rel], let's get you up to your room."
        #     hin "Mmm... Okay..."
        #     scene black with dissolve
        #     "You carefully lift her into your arms and carry her upstairs to her room, laying her gently on the bed."
        #     bo "Goodnight, [hin_rel]."
        #     bot "Dream of me fucking your brains out tonight, because I know I will hehe..."
        #     hin "Th-thank you... Goodnight..."
        #     "You take one last look , lingering for a moment before taking your leave."
        #     if quest.is_state("3_hin2L", "in progress"):
        #         $ notification (f"{hin_name} Love Level 2 objective completed")
        #         $ quest_hin.check("3_hin2L", "completed")
        #         $ quest_hin.check("hin2L_1", "completed")
        #     jump action_taken







