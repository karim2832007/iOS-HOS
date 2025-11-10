label fantasize:
    menu hinata_fantasize:
        bot"I can't stop thinking about [hin_rel]..."
        "A night out...":
            label replay_anightout:
            $ initialize_replay_defaults()
            scene black with dissolve
            bot"I don't know if this is because of my condition but..."
            show hinafantasize 0 with dissolve:
                yalign 1.0 xalign 0.5 zoom 0.7
            show hinafantasize 0:
                easein 2 yalign 0.0
            bot"You are stuck on my fucking mind [hin_rel]..."
            bot"One of those days, I'll have you put one of your nice pink dresses on..."
            scene hinafantasize 0 with dissolve:
                zoom 0.66 xalign 0.5 yalign 0.6
            pause 0.3
            scene black with vpunch
            bot"No, wait!"
            scene hinafantasize 3 at halfzoom with dissolve
            bot"A black dress would be much more fitting given your elegance..."
            show hinafantasize 3 at halfzoom with dissolve:
                zoom 1.3 xalign 1.0 yalign 0.0
            show hinafantasize 3 at halfzoom:
                easein 2 xalign 0.0 yalign 1.0
            bot"A dress that would leave your long sexy legs exposed..."
            scene hinafantasize 2 at halfzoom with dissolve
            with flash
            bot"We'd go out on dates together and..."
            scene hinafantasize 2 at halfzoom with dissolve:
                zoom 1.34 xalign 0.0 yalign 1.0
            bot"And t-then I w-would..." with flash
            $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.4)
            bot"I w-would... H-hngh!" with longerflash
            call decreaselust(50) from _call_decreaselust_10
            bot"F-fuck... I can't believe I creamed my pants thinking about [hin_rel] like that."
            scene black with dissolve
            $ renpy.end_replay()
            jump action_taken



        "{color=[hatredcolor]}(Locked){/color}":
            dev"WIP"
            call checkHatred(30, "hinata_fantasize") from _call_checkHatred_1
            jump hinata_fantasize
        "{color=[lovecolor]}(Locked){/color}":
            dev"WIP"
            call checkLove(10, "hinata_fantasize", "Hinata") from _call_checkLove
            jump hinata_fantasize
        "Return":
            jump fantasizemenu
        

    menu himawari_fantasize:
        
        bot"To think that even [him_name] occupies my thoughts... How far have I fallen?"
        "Little cock-tease...":
            label replay_littlecocktease:
            $ initialize_replay_defaults()
            scene black with dissolve
            bot"You are just such a fucking cock-tease [him_name]...."
            show hinafantasize_schl 2 with dissolve
            bot"To think that even a bitch like you is occupying my thoughts..."
            show hinafantasize_schl 7 with dissolve
            bot"One of those days I'll have to teach you a lesson in how you should behave around your older [him_rel_to_bo]..."
            scene hinafantasize_schl 6 with dissolve:
                xalign 0.5 yalign 1.0
            show hinafantasize_schl:
                easein 2 yalign 0.0
            bot"You damned b-brat..." with flash
            show screen parallax1280("hinafantasize_schl 6") with dissolve
            "You can move the screen with your cursor or by dragging."
            "Click twice to continue"
            $ ui.interact()
            $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.4)
            bot"Y-you are such a... H-hngh!" with longerflash
            call decreaselust(50) from _call_decreaselust_11
            bot"Goddamn cock-tease..."
            hide screen parallax1280
            show hinafantasize_schl 2
            with dissolve
            bot"F-fuck... to think that I creamed my pants thinking about [him_name] of all people..."
            scene black with dissolve
            bot"I am going insane..."
            $ renpy.end_replay()
            jump action_taken
        
        "(Locked)" if himawaripanties.quantity == 0 and himawaripantiescum.quantity == 0:
            "Find something to help you fantasize first..."
            jump himawari_fantasize
        "Use [him_name]'s panties" (secrethatred = True) if himpantiesinv!= None or himpantiscumininv!= None:
            label replay_himasecretpanties:
            $ initialize_replay_defaults()
            scene black with dissolve
            bot"What if I..."
            $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.4)
            show himafantasize_panties1 with dissolve
            bot"I can put those panties of hers to good use now that I think about it..."
            show himafantasize_panties2 with dissolve
            pause 0.3
            scene black with dissolve
            bot"The soft silken fabric along with the aroma of her scent rubbing off on my cock will make it easier for me to picture..."
            show himafantasize_b1 with dissolve:
                zoom 0.82
            bot"...this fucking brat!"
            show himafantasize_b1 with dissolve:
                zoom 0.95 xalign 0.9 yalign 0.3
            bot"I don't know how, or when she grew into that body of hers..."
            $ renpy.sound.play("/audio/soun_fx/jerkoffclothes.opus", channel="sfx2", loop=False, relative_volume = 0.4)
            if not _in_replay:
                call useItem(himawaripanties,1) from _call_useItem
            bot"B-but I am not c-complaining! [him_name]'s one sexy girl..."
            show himafantasize_b2 with dissolve:
                zoom 0.82
            bot"If only she didn't grew up to be such a bitch along with it..."
            show himafantasize_b3 with dissolve:
                zoom 0.82
            bot"It was only a few years ago since we'd go visit the secluded beach near our home together..."
            show himafantasize_b3 with dissolve:
                zoom 0.95 xalign 0.0 yalign 0.3
            bot"She wasn't as abrasive back then..."
            show himafantasize_b3 with dissolve:
                zoom 1.05 xalign 1.0 yalign 1.0
            show himafantasize_b3:
                easein 6 xalign 0.0 yalign 0.3
            bot"In fact, I remember how she would even have me help apply some of her lotion at times..."
            bot"We both didn't think much of it then, but now all I can think about is..."
            $ renpy.sound.play("/audio/soun_fx/jerkoffclothes.opus", channel="sfx2", loop=False, relative_volume = 0.4)
            show himafantasize_b3 with dissolve:
                zoom 0.82
            bot"F-fuck! What a wasted opportunity..."
            show p_him1 with dissolve:
                zoom 0.5
            bot"Back then, I am almost certain that [him_name] was oblivious to how well she grew into her curvy body..."
            bot"Why else would she have kept wearing those slutty skin-tight bikinis of hers around me..."
            show himafantasize_f1 with dissolve:
                zoom 0.8
            bot"Unless of course... she was a slut all along!"
            bot"No matter. Even if she didn't, I certainly did..."
            show himafantasize_f1 with dissolve:
                zoom 0.95 yalign 1.0
            bot"At some point, I couldn't resist sneaking in a few peeks whenever I had the chance to..."
            bot"How could I not when her wet, sweaty bottoms would slide into her ass-cheeks and almost reveal her tight little holes to me."
            bot"I think it was one of those days when..."
            $ renpy.sound.play("/audio/soun_fx/jerkoffclothes.opus", channel="sfx2", loop=False, relative_volume = 0.4)
            show himafantasize_f2 with dissolve:
                zoom 1.0 xalign 0.0 yalign 1.0
            show himafantasize_f2:
                easeout 2 xalign 1.0 yalign 0.5
            pause 1.95
            scene himafantasize_f2 with dissolve:
                zoom 0.8
            show himafantasize_f2_1 with Dissolve(1):
                zoom 0.8
            pause 1.5
            show himafantasize_f2_2 with Dissolve(1):
                zoom 0.85 xalign 1.0
            him"H-hey!" with vpunch
            bot"She caught me staring..."
            show himafantasize_f2_2 with vpunch:
                zoom 0.95 xalign 1.0
            him"Are you s-staring at my...!?" with vpunch
            scene himafantasize_f2_2 with dissolve:
                zoom 0.82
            menu:
                him"Are you s-staring at my...!?" with vpunch
                "{color=[hatredcolor]}???{/color}":
                    bot"But now, I want to do much more than stare at your ass [him_name]!"
                    bot"I w-want to..."
                    $ renpy.sound.play("/audio/soun_fx/cum6.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                    show himafantasize_f12_3 with flash:
                        zoom 0.8
                    bot"G-get in there and..."
                    $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                    show himafantasize_f2_4 with longerflash:
                        zoom 0.8
                    bot"S-stretch your little holes!"
                    call changeHatred(1) from _call_changeHatred_2
                    show himafantasize_f2_4 with dissolve:
                        zoom 1.0 xalign 0.0 yalign 1.0
                    show himafantasize_f2_4:
                        easein 5 xalign 1.0 yalign 0.3
                    bot"I'll make you understand, that you aren't worth nearly as much as you think you are!"

                    call decreaselust(100) from _call_decreaselust_12
                    scene himafantasize_f2_4 with dissolve:
                        zoom 0.8
                    scene black with dissolve
                    bot"You'll have your lesson in humility soon enough, [him_name]..."


                "Introspect...":
                    bot"I suppose that's when she started acting like she does towards me..."
                    bot"B-but am I really to b-blame...?"
                    bot"She is j-just so..."
                    $ renpy.sound.play("/audio/soun_fx/cum10.opus", channel="sfx2", loop=False, relative_volume = 0.4)
                    with flash
                    call decreaselust(100) from _call_decreaselust_13
                    scene black with dissolve
                    bot"I am just a man after all..."
            $ renpy.end_replay()
            show himafantasize_panties2_1 with dissolve:
                zoom 1.2 xalign 0.5 yalign 0.6
            
            if not quest.is_state("bohim_1", "done"):
                $ notification("Quest Completed")
                $ quest.check("bohim_1", "done") #marks left quest as complete (make sure any references now check if quest is completed to avoid errors)
                $ quest.remove("[him_name]'s garments") # removes the quest from the right page (use when completed)
                $ renpy.block_rollback()
            if himpantiscumininv!= None:
                bot"[him_name]'s panties are getting really crusty now... Yuck!"
            else:
                bot"Your panties are now soaked in my cum [him_name]..."
                call getItem(himawaripantiescum,1) from _call_getItem
            if not quest_him.is_state("him1H_3", "done"):
                $ quest_him.check("him1H_3", "done") #mark fantasize hatred in hima's log complete
                $ notification (f"{him_name} Hatred objective completed")
            
            bot"I wonder if her cum-stained panties have any use..."
            scene black with dissolve
            
                
            

            


            








            jump action_taken
        "{color=[hatredcolor]}(Locked){/color}":
            dev"WIP"
            call checkHatred(30, "himawari_fantasize") from _call_checkHatred_2
            jump himawari_fantasize
        "{color=[lovecolor]}(Locked){/color}":
            dev"WIP"
            call checkLove(10, "himawari_fantasize", "Himawari") from _call_checkLove_1
            jump himawari_fantasize
        "Return":
            jump fantasizemenu
        