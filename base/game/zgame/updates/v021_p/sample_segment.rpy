# label ntrwarning_skip:
#     $ notification("Skipped due to optional preferences")
#     return

# label ramen_segment_scene:
#     #todo scene wiuth obo where she tries the outfit and blabla happens
#     $ renpy.sound.play("/audio/soun_fx/backgroundchatting.opus", channel="ambience", loop=True, fadein = 1, relative_volume = 0.3)
#     scene black with dissolve
#     "After Obo interaction, trying out outfit, blabla..."
#     show rename2 with dissolve:
#         fit "contain" xalign 0.05
#     "The moment [hin_name] stepped out of the backroom, the murmurs grew louder and louder..."
#     "Customer Whispering" "H-hey! Isn't that..."
#     "Customer talking" "Her... at a place like this? Impossible..."
#     show rename2_1:
#         zoom 0.58 xalign 0.95
#     show rename2:
#         alpha 0.3
#     with dissolve
#     "Handsy Customer" "I wouldn't mistake those curves for anyone else's..."
#     "Handsy Customer" "It really is her!"
#     "Drunken Customer" "It's true! Lady [hin_name] is our barmaid! *Hic!*"
#     scene black with vpunch
#     "Drunken Customer" "A cause for celebration, another round on me!" with vpunch
#     show bg ramenwork with dissolve:
#         zoom 0.96
#     show bg:
#         blur 5
#     show rhina working_normal1 at left
#     with dissolve
#     hint"So m-many people! And there murmurs..."
#     show rhina at smallshake
#     hint"It feels like everyone is staring at me!"
#     show rboy angry1 at right behind rhina with dissolve:
#         xpos 2000
#     show rboy:
#         easein 2 xpos 1300
#     "???" "Lady [hin_name]... Is it not?"
#     hint"H-huh? A young boy...?"
#     show rhina working_smiling1 with dissolve
#     hin"Y-yes... And you are?"
#     "???" "I have no name..."
#     hin"H-huh?"
#     show rhina working_sad1 with dissolve
#     "???" "My moma is dead, my father has disowned me..."
#     hint"Poor boy! To be left alone orphaned in this world..."
#     show rboy at smallshake
#     "???" "If that were not enough, your [hin_rel_to_bo]..."
#     hin"[bo_name]? Are you two... f-friends?"
#     show rboy crying1 with dissolve
#     "???" "Friends? No... *Sniffles*"
#     hint"Is he... c-crying?"
#     "???" "Your [hin_rel_to_bo] is..."
#     show rboy:
#         easein 2 xpos 600
#     pause 1
#     scene black with dissolve
#     "???" "He is a big meanie and a bully! *Sniffles*"
#     hin"Are you s-sure? [bo_name] would never-" with vpunch
#     if persistent.netorareoptional == True: #if NTR disabled: #todo check how you should handle NTR. In most cases just black screen it + minimal dialogue to justify alternative action will be enough. Only skip actual touching/sexual stuff. Emotional stuff should be shown as normal
#         call ntrwarning_skip
#         "The boy leans in for a comforting hug..."
#         hin"There, there..."
#     else:
#         show ramenboy_intro 1 with dissolve:
#             yalign 0.0
#         show ramenboy_intro 1:
#             easein 5 yalign 1.0
#         hin"H-hey, wait a second! I am working right now..."
#         if persistent.netorareoptional == True: #if NTR disabled:
#             hin""
#         "???" "*Sniffles* He is a bully! He made my life a living hell... But you are nice, aren't you?"
#         hint "This boy... His hand is on my- what is he trying to do..."
#         hin"It's okay, you don't have to cry. I'll talk to him about it, you two will be friends in no time!"
#         "???" "T-thank you, nice lady. *sniffles* But it's not fair that he has a moma as pretty as you!"
#         hin"H-huh...?"
#         show ramenboy_intro 1_1 with dissolve
#         $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp6.opus", channel="sfx2", loop=False, relative_volume = 0.6)
#         "???" "Can you be my moma too!?" with vpunch
#         scene black with vpunch
#         $ renpy.sound.play("/audio/soun_fx//glasssmash.opus", channel="sfx3", loop=False, relative_volume = 0.3)
#         "The sceeming young man slid his fingers where they didn't belong, startling [hin_name] and causing her to lose her balance!"
#     show bg ramenwork with dissolve:
#         zoom 0.96
#     show bg:
#         blur 5
#     show rboy smirk1 at center
#     show rboy:
#         easein 3 xpos -1000
#     with dissolve
#     "???" "Hihihi! I am outie!"
#     scene black with dissolve
#     #todo
#     "Scene where Hinata is on floor cleaning, someone tries to pull some shit off, Obo steps in and diffuses the situation/reassures Hinata"
#     #blabla

#     #todo after above scene
#     scene bg ramentoilet
#     show rboy smirk1 at center
#     with dissolve
#     "???" "Turns out this little mission may end up being fun after all!"
#     "???" "I had no idea the target's [hin_rel] was so fucking hot!"
#     scene black with dissolve
#     "???" "Hihihi..."

#     #todo 2nd mini-game + shiftend scene
#     #blabla





#     #todo toilet scene (I will probably handle this part)
#     scene bg ramentoilet
#     show rhina shy2 at center
#     with dissolve
#     hint"Unisex bathrooms, eh? Lucky no one is here..."
#     scene black with dissolve
#     hint"I better make this quick..."
#     scene p0 with dissolve:
#         yalign 0.0
#     show p0:
#         easein 5 yalign 1.0
#     hint"Y-yuck! Cracked walls, and... what is up with the holes?"
#     call showscrollingimage
#     show screen parallax1280("p0",1,0.5) with dissolve
#     hint"At least the toilet seems clean..."
#     $ renpy.sound.play("/audio/soun_fx/clothes_drop.opus", channel="sfx2", loop=False, relative_volume = 0.7)
#     hide screen parallax1280
#     show screen parallax1280("p0_1",1,0.0)
#     with dissolve
#     hint"..."
#     call hidescrollingimage
#     "blabla"

#     #some random examples of hwo to work with cutouts:
#     show bg ramenwork with dissolve:
#         zoom 0.96
#     show bg:
#         blur 5
#     show rhina shy1 at left with dissolve
#     hint"Sure is busy today..."
#     show rcharmer normal1 at right behind rhina
#     show rcharmer:
#         easein 1 xalign 0.9
#     "'Charming' Man" "Hey, pretty lady..."
#     hin"How can I help you, Sir?"
#     show rcharmer:
#         easein 3 xalign 0.3
#     "'Charming' Man" "I was thinking more along the lines of..."
#     if persistent.netorareoptional == True: #if NTR disabled: #todo check how you should handle NTR. In most cases just black screen it + minimal dialogue to justify alternative action will be enough. Only skip actual touching/sexual stuff. Emotional stuff should be shown as normal
#         call ntrwarning_skip
#         $ renpy.sound.play("/audio/soun_fx/slap.opus", channel="sfx2", loop=False, relative_volume = 0.8)
#         show rcharmer at right
#         show rhina angry1
#         with flash
#         hin"Don't even think about it!"
#         "'Charming' Man" "R-right, right..."
#         show rcharmer perv1 with dissolve
#         show rcharmer:
#             easein 1 xpos 2000
#         "'Charming' Man" "Maybe next time then!"
#         hide rcharmer with dissolve

#     else:
#         "'Charming' Man" "How could I help YOU..."
#         show rhina shy2 with dissolve
#         $ renpy.sound.play("/audio/soun_fx/hinata/hinatagasp1.opus", channel="sfx2", loop=False, relative_volume = 0.7)
#         show rhina at smallshake
#         hin"*Sharp gasp*!" with vpunch
#         #todo check how image_with_border is used. Besides sprite dialogue,, you cna also use it during full screen cg to show detials while hiding/skirting around consistency. (EG: full cg shows Hinata serving a table, imaga_with_border shows zoomed-in groping of her tits/ass)
#         show screen image_with_border("ramenshop_test1",0.5,1.0,0.0) with dissolve
#         "'Charming' Man" "...If you know what I mean!"
#         show rhina at smallshake
#         hin"You can't do t-that, sir!"
#         hide screen image_with_border
#         show rcharmer perv2
#         with dissolve
#         show rcharmer:
#             easein 1 xalign 0.7
#         show rhina ass2 with dissolve
#         "'Charming' Man" "Maybe next time then!"
#         hide rcharmer with dissolve


    
#     scene black with dissolve
#     "end example 1"


