
#QTE-----------------------------------------------------------------

default arrow_colors = {"up": "#ffffff", "down": "#ffffff", "left": "#ffffff", "right": "#ffffff"}
default yoruichi_clothes = "Normal"
default yoruichi_bribed = 0
default yoruichi_relationship = "Passive"
define relationship_colors  = {
    "Passive": "#6f0000",
    "Formal": "#B3D5AE", #talking
    "Apprehensive": "#BE0000", #fearful
    "Unwillingly Obedient": "#542869",    #Listens
    "Obedient": "#8B00CC",    #Listens
    "Close": "#F996DD",  #minor sexual acts
    "Intimate": "#FF29C3", #full sexual acts
    "Submissive": "#8B00CC",    #Submits
    "Slave": "#450065",       #plaything
    "Sex-Slave": "#550000",   #submissive sex-slave
    "Apprehensive Sex-Slave": "#360023",   #hateful sex-slave
}
default yoruichi_objectives_passive = [
    {"description": "High score > 2000", "completed": False},
    {"description": "Unlock Yoruichi's Story 1", "completed": False},
    {"description": "Advance the relationship", "completed": False},
]
default yoruichi_objectives_formal = [
    {"description": "High score > 3800", "completed": False},
    {"description": "Complete 3 shifts with her", "completed": False},
    {"description": "Unlock Yoruichi's Story 2", "completed": False},
    {"description": "Uncover Yoruichi's secret", "completed": False},
    {"description": "Advance the relationship", "completed": False},
]
default yoruichi_objectives_apprehensive= [
    {"description": "Earn back her willingness by bribing her", "completed": False},
    {"description": "Complete 3 shifts with her", "completed": False},
    {"description": "Advance the relationship", "completed": False},
]
default yoruichi_objectives_obedient = [
    {"description": "High score > 4500", "completed": False},
    {"description": "Complete 6 shifts with her", "completed": False},
    {"description": "Unlock Obo's Story 2", "completed": False},
    {"description": "(WIP) Advance Relationship (WIP)", "completed": False},
]

default yoruichi_objectives_obedient_unwilling = [
    {"description": "High score > 4500", "completed": False},
    {"description": "Complete 6 shifts with her", "completed": False},
    {"description": "Unlock Obo's Story 2", "completed": False},
    {"description": "(WIP) Advance Relationship (WIP)", "completed": False},
]




# Add this screen for color picking:
screen color_picker(direction):
    zorder 1000000
    modal True
    frame:
        style_prefix "color_picker"
        vbox:
            text "Choose color for [direction] arrow:"
            hbox:
                for color in ["#ff0000", "#0000ff", "#ffff00", "#ff00ff", "#00ffff", "#ffffff"]:
                    textbutton "":
                        style "color_button"
                        background color
                        action [SetDict(arrow_colors, direction, color), Hide("color_picker")]
            textbutton "Cancel" action Hide("color_picker")

style color_picker_frame:
    xalign 0.5
    yalign 0.5
    padding (20, 20)

style color_button:
    xminimum 50
    yminimum 50


init python:
    import random
    import time

    def close_workmenu():
        renpy.hide_screen("workmenu")
        renpy.hide_screen("test_workmenu")
        renpy.hide_screen("displayTextScreen")

    def hide_displayTextScreen():
        renpy.hide_screen("displayTextScreen")
        
    def update_yoruichi_objectives():
        global yoruichi_objectives_passive
        global yoruichi_objectives_formal
        global yoruichi_objectives_apprehensive
        global yoruichi_objectives_obedient
        global yoruichi_objectives_obedient_unwilling
        if yoruichi_relationship == "Passive":
            if high_score > 2000:
                yoruichi_objectives_passive[0]["completed"] = True
            
            
            if score_2_claimed == True:
                yoruichi_objectives_passive[1]["completed"] = True

        elif yoruichi_relationship == "Formal":
            if high_score > 3800:
                yoruichi_objectives_formal[0]["completed"] = True
            
            if shifts_completed >= 3:
                yoruichi_objectives_formal[1]["completed"] = True
            
            if score_3_claimed == True:
                yoruichi_objectives_formal[2]["completed"] = True

            if yoruichi_talk_progress_formal == 4:
                yoruichi_objectives_formal[3]["completed"] = True

        elif yoruichi_relationship == "Apprehensive":
            if sharemoneywithyorucounter > 2:
                yoruichi_objectives_apprehensive[0]["completed"] = True
            
            if shifts_completed > 2:
                yoruichi_objectives_apprehensive[1]["completed"] = True
            
 
        elif yoruichi_relationship == "Obedient":
            if high_score > 4500:
                yoruichi_objectives_obedient[0]["completed"] = True
            
            if shifts_completed >= 6:
                yoruichi_objectives_obedient[1]["completed"] = True
            
            if score_4_claimed == True:
                yoruichi_objectives_obedient[2]["completed"] = True

        elif yoruichi_relationship == "Unwillingly Obedient":
            if high_score > 4500:
                yoruichi_objectives_obedient_unwilling[0]["completed"] = True
            
            if shifts_completed >= 6:
                yoruichi_objectives_obedient_unwilling[1]["completed"] = True
            
            if score_5_claimed == True:
                yoruichi_objectives_obedient_unwilling[2]["completed"] = True



    def get_reward_hover_text(claimed, high_score, required_score, previous_claimed, dailyhighscoreunlock):
        if claimed:
            return "Claimed"
        elif dailyhighscoreunlock:
            return "You already unlocked a reward for this shift, try again next shift"
        elif not previous_claimed:
            return "Unlock all previous rewards first"
        elif high_score >= required_score:
            return "Click to Claim"
        else:
            return f"Reach {required_score}+ score to unlock"

init:
    # All ramen-game variables
    $ normal_color = "#ffffff"
    $ correct_color = "#00ff00"
    $ high_score = 0 #tracks all time high score of player
    $ ramencurrency = 0 #each tries score added to currency, used to unlock powerups
    $ availablemoneytobepaid = 1000 #money that can be earned from mini-game for purposes of game balance. When expired defaults to paying 5$
    default ramenlevel1 = 0 # tracks game completions of level 1 game
    default unlockedramenlevel2 = False #Variable to unlock level 2 of game when ramenlevel1 reaches = 3
    default dailyhighscoreunlock = False #limits unlocking highscore stories to one per shift
    default shifts_completed = 0
    #Rewards screen unlockables
    default bonus_1_purchased = False
    default bonus_2_purchased = False
    default bonus_3_purchased = False
    default bonus_4_purchased = False
    default bonus_5_purchased = False
    default bonus_6_purchased = False
    default bonus_7_purchased = False
    default bonus_8_purchased = False
    default bonus_9_purchased = False
    #highscore
    default score_1_claimed = False
    default score_2_claimed = False
    default score_3_claimed = False
    default score_4_claimed = False
    default score_5_claimed = False
    default score_6_claimed = False
    default score_7_claimed = False
    default score_8_claimed = False

    #powerups
    default multiplier1_purchased = False
    default multiplier2_purchased = False
    default multiplier3_purchased = False
    default shifttimer1_purchased = False
    default shifttimer2_purchased = False
    default shifttimer3_purchased = False
    default sequencetimer1_purchased = False
    default sequencetimer2_purchased = False
    default sequencetimer3_purchased = False
    default addtosequencetimer = 0.0
    default addtooveralltimer = 0.0

    #acecssibility checkbox to prevent video from playing
    default use_video_background = True
    
    
screen qte_display(sequence, correct_inputs, progress):
    zorder 100
    frame:
        xalign 0.5
        yalign 0.25
        padding (20, 20)
        vbox:
            spacing 10
            text "Input this sequence:" align (0.5, 0.5)
            hbox:
                spacing 10
                align (0.5, 0.5)
                for i, arrow in enumerate(sequence):
                    $ direction = {'↑': 'up', '↓': 'down', '←': 'left', '→': 'right'}[arrow]
                    $ color = arrow_colors[direction]
                    text arrow size 50 color (color if i >= correct_inputs else correct_color)
            text "Time left: {:.1f}".format(timer) align (0.5, 0.5)
            # text "Progress: {:.0%}".format(progress) align (0.5, 0.5)
     
    timer 0.1 repeat True action If(timer > 0, SetVariable("timer", timer - 0.1), Jump("mistakemade"))

screen qte_display_overall(lives):
    zorder 100
    frame:
        xalign 0.5
        yalign 0.0
        padding (10, 10)
        vbox:
            spacing 10
            text "Shift ends in: {:.1f}".format(overall_timer) align (0.5, 0.5)
            hbox:
                xalign 0.5
                spacing 5
                for i in range(3):
                    if i < lives:
                        image "images/UI/Heart_full.png" zoom 3.5
                    else:
                        image "images/UI/Heart_empty.png" zoom 3.5

     
    timer 0.1 repeat True action If(overall_timer > 0, SetVariable("overall_timer", overall_timer - 0.1), Jump("end_sequence_overall"))

    


#score display
screen score_display(finalscore, high_score):
    zorder 110  # Ensures it stays on top
    frame:
        background None
        xalign 0.0
        yalign 0.0
        padding (20, 20)
        vbox:
            text "High Score: [high_score:.2f]" color "#00ff00" size 20
            text "Current Score: [finalscore:.2f]" color "#00ff00" size 20

screen qte_input(expected_input):
    modal True
    
    key "K_UP" action Return("↑")
    key "K_DOWN" action Return("↓")
    key "K_LEFT" action Return("←")
    key "K_RIGHT" action Return("→")

    key "K_KP8" action Return("↑")
    key "K_KP2" action Return("↓")
    key "K_KP4" action Return("←")
    key "K_KP6" action Return("→")

    #mobile
    if renpy.variant("touch"):
        vbox:
            xalign 0.5
            yalign 0.8

            # Up button
            button:
                action Return("↑")
                xalign 0.5
                ypos 40
                text "↑" size 150

            hbox:
                xalign 0.5
                ypos -30

                # Left button
                button:
                    action Return("←")
                    xalign 0.2
                    yalign 0.1
                    text "←" size 150

                # Down button
                button:
                    action Return("↓")
                    xalign 0.5
                    ypos 75
                    text "↓" size 150

                # Right button
                button:
                    action Return("→")
                    xalign 0.8
                    yalign 0.1
                    text "→" size 150


    timer 0.1 action NullAction()


image ramenwork = Movie(channel="movie_dp", play="images/video/ramenwork.webm", stop_music=False, size=(1280,720))
label start_qte:
    $ playmusic("/audio/ost/Hesitant Ramen.opus", 0.7)
    $ sequence_length = 2
    $ max_length = 7
    $ score = 120 #initial value to be 
    $ finalscore = 0
    $ game_active = True
    $ fail_counter = 0
    $ completioncounter = 0
    $ penaltytime = 0.0
    $ finalscore = 0
    $ lives = 3  # Initialize lives
    $ moneytobepaid = 0

    #sequence timer powerups
    $ addtosequencetimer = 0.5
    if sequencetimer1_purchased:
        $ addtosequencetimer += 0.5
    if sequencetimer2_purchased:
        $ addtosequencetimer += 1.5
    if sequencetimer3_purchased:
        $ addtosequencetimer += 3

    #score multiplier powerups
    $ scoremultiplier = 1
    if multiplier1_purchased:
        $ scoremultiplier += 0.1
    if multiplier2_purchased:
        $ scoremultiplier += 0.15
    if multiplier3_purchased:
        $ scoremultiplier += 0.25

    #overall timer powerups
    $ addtooveralltimer = 0
    if shifttimer1_purchased:
        $ addtooveralltimer += 5
    if shifttimer2_purchased:
        $ addtooveralltimer += 10
    if shifttimer3_purchased:
        $ addtooveralltimer += 15
    
    menu workmenu:
        "Are you ready to start?"
        "Level 1":
            hide screen workmenutopright
            hide screen scrollingtext
            $ renpy.sound.play("/audio/soun_fx/countdown.opus", channel="sfx2", loop=False, relative_volume = 0.9)
            show screen scrollingtext("Get ready to input the displayed sequence using your arrow-keys or numpad!")
            
            show halfblack with Dissolve(3.5)

            #video or still image based on accessibility
            if use_video_background:
                show ramenwork
            else:
                show ramenvideostill

            show halfblack2
            with dissolve

        "Level 2 (Locked)" if unlockedramenlevel2 == False: #todo mini-game start
            "In development"
            jump workmenu
        "Stage 2" if unlockedramenlevel2 == True:
            "In development"
            jump workmenu
            
        "Level 3 (Locked)":
            "In development"
            jump workmenu
        
        "Return" if mapintrotutorial == True:
            jump ramenkitchenmenu
        
        "Information":
            $ update_yoruichi_objectives()  #run function to check yoruichi objectives
            $ selected_workmenu = "tutorial"
            show screen workmenu
            jump workmenu
            
 

 


    $ overall_timer = 60  # 58 seconds overall game time
    $ overall_start_time = time.time()
    show screen score_display(finalscore, high_score)

    while game_active and sequence_length <= max_length and overall_timer >0: #exits while loop if overal timer is 0
        $ current_sequence = generate_sequence(sequence_length)
        $ correct_inputs = 0
        $ timer = 6.5 #initiate timer so that game doesnt end instantly. Actual timer is set under while loop

        $ progress = 0.0

        show screen score_display(finalscore, high_score)  # Refresh the score display
        show screen qte_display(current_sequence, correct_inputs, overall_timer) 
        show screen qte_display_overall(lives)
        
        $ start_time = time.time()
        $ overall_timer = max(0, 60 - (time.time() - overall_start_time) + addtooveralltimer)

        while correct_inputs < len(current_sequence) and timer > 0:
            $ timer = max(0, (6.5 - (time.time() - start_time)) - penaltytime + addtosequencetimer) #penaltytime removes 0.5 seconds everytime player completes full lsequence
            $ progress = correct_inputs / len(current_sequence)
            
            if auto_shift_mode:
                # Automatically play through the sequence with a delay
                while correct_inputs < len(current_sequence):
                    $ player_input = current_sequence[correct_inputs]
                    $ correct_inputs += 1
                    play sound "audio/soun_fx/select2.opus"

                    # Update the display so you can see progress
                    show screen qte_display(current_sequence, correct_inputs, progress)
                    $ renpy.restart_interaction()

                    # Small delay between each "auto press"
                    $ renpy.pause(0.01)   # adjust 0.1–0.4 seconds to control speed
            else:
                call screen qte_input(current_sequence[correct_inputs]) with None
                $ player_input = _return

                if player_input is not None:  # Only process actual inputs, not timer updates
                    if player_input == current_sequence[correct_inputs]:
                        $ correct_inputs += 1
                        play sound "audio/soun_fx/select2.opus"
                    else:
                        label mistakemade:
                            $ lives -= 1
                            show screen qte_display_overall(lives)
                            $ fail_counter += 1
                            hide screen scrollingtext
                            if fail_counter == 1:
                                play sound "audio/soun_fx/error.opus" volume 2.0
                                $ texttosend = "{color=#FF0000}Focus up!{/color} "
                                show screen scrollingtext(texttosend)
                            elif fail_counter == 2:
                                play sound "audio/soun_fx/error.opus" volume 2.0
                                $ texttosend = "{color=#FF0000}No more mistakes allowed!{/color} "
                                show screen scrollingtext(texttosend)
                            elif fail_counter >= 3:
                                play sound "/audio/soun_fx/attributeslost.opus"
                                $ texttosend = "{color=#FF0000}That's enough...{/color} "
                                show screen scrollingtext(texttosend)
                                $ game_active = False
                                jump end_sequence_mistakes            
            show screen qte_display(current_sequence, correct_inputs, progress)
            $ renpy.restart_interaction()

        hide screen qte_display
        hide screen qte_input

        if correct_inputs == len(current_sequence):
            $ scoretoadd = (score+timer)*scoremultiplier #score increases for every full completion by 10% / remaining timer added to score
            if finalscore > high_score:
                $ high_score = finalscore #update high score if current session's score is higher
            $ finalscore = finalscore + scoretoadd
 
            hide screen scrollingtextfast
            play sound "/audio/soun_fx/select3.opus"
            $ texttosend = f"{{color=#00ff00}}+{round(scoretoadd, 2)} score{{/color}}"
            show screen score_display(finalscore, high_score) #update score screen
            show screen scrollingtextfast(texttosend)
            $ sequence_length += 1
            if sequence_length > max_length:
                $ completioncounter += 1
                $ sequence_length = 2 + completioncounter
                $ max_length = 7 + completioncounter
                $ penaltytime += 0.5 # remove 0.5 seconds everytime the player completes a full sequence
                $ scoremultiplier = scoremultiplier + 0.1
                $ renpy.sound.play("/audio/soun_fx/multiplier2.opus", channel="sfx3", loop=False, relative_volume = 0.9)
                $ texttosend = f"{{color=#00ff00}}x{round(scoremultiplier, 2)} multiplier!{{/color}}"
                show screen scrollingtextfast(texttosend)
        else:
            jump end_sequence



    return

label end_sequence:
    $ playmusic("/audio/ost/market.opus", 0.9)
    hide screen qte_display
    hide screen qte_input
    hide screen qte_display_overall
    hide halfblack
    hide halfblack2
    hide ramenwork
    hide ramenvideostill
    hide screen score_display
    with dissolve
    if overall_timer <= 0:
        play sound "/audio/soun_fx/attributeslost.opus"
        "Time's up! You were too slow kid..."
        "Pick up the pace next time!"
        jump endconvergence
    else:
        jump endconvergence

label end_sequence_mistakes:
    $ playmusic("/audio/ost/market.opus", 0.9)
    hide ramenwork
    hide ramenvideostill
    hide halfblack
    hide halfblack2
    hide screen qte_display
    hide screen qte_input
    hide screen qte_display_overall
    hide screen score_display
    with dissolve
    obo"You are making too many mistakes kid! Remember, quality over quantity!"
    obo"Next time slow down a little bit..."
    jump endconvergence

label end_sequence_overall:
    $ playmusic("/audio/ost/market.opus", 0.9)
    $ renpy.sound.play("/audio/soun_fx/multiplier.opus", channel="sfx3", loop=False, relative_volume = 0.5)
    hide ramenwork
    hide ramenvideostill
    hide screen qte_display
    hide screen qte_input
    hide screen qte_display_overall
    hide halfblack
    hide halfblack2
    hide screen score_display
    with dissolve
    scene ramen workend with dissolve
    "You completed the work shift succesfully!"
    
    label endconvergence:
        if mapintrotutorial == False: #tutorial handling
            $ mapintrotutorial = True
            jump endofworktutorial
        
        $ shifts_completed += 1
        $ update_yoruichi_objectives()  #run function to check yoruichi objectives
        "Your final score is [finalscore:.2f]!"
        $ ramencurrency += finalscore #add score to currency
        $ int_number = int(finalscore) #convert score to integer
        if int_number >=1000:
            $ first_two_digits = int_number // 10**(len(str(int_number)) - 2) #extract first 2 digit s of integer to be used as payment if score is higher than 1000
        else:
            $ first_two_digits = int_number // 10**(len(str(int_number)) - 1) #extract first  digit of integer to be used as payment if score is higher than 1000
        $ availablemoneytobepaid -= first_two_digits #deallocate the paid amount from the initial 1000$ payable

        
        if availablemoneytobepaid >= 0: #payment handling

            if sharemoneywithyoru == True:
                call changeMoney(first_two_digits/2) from _call_changeMoney_4
                $ sharemoneywithyoru = False
                "You share some of your payment with Yoruichi as per your agreement..."
            else:
                call changeMoney(first_two_digits) from _call_changeMoney_5
        else:
            default allmoneypaid = False
            if allmoneypaid == False:
                obo"Kid... I am afraid I've got bad news for you."
                obo"Your performances have run me dry for now. You can keep working here whenever you want but I'll only be able to pay you 15$ flat for each shift until further notice."
            $ allmoneypaid = True
            if sharemoneywithyoru == True:
                $ sharemoneywithyoru = False
                "You share some of your payment with Yoruichi as per your agreement..."
            call changeMoney(15) from _call_changeMoney_6
        pause 0.5

        #score handling
        if finalscore > high_score:
            $ high_score = finalscore
            if finalscore > 5500:
                
                $ ramenlevel1 += 1
                if ramenlevel1 == 1:
                    obo"Kid... I want to pin you on the wall and make sweet love to your little white ass!"
                    obo"You are the best I've ever seen! Probably the best in the known lands even!"
                    obo"But that's only when it comes to prepping ramen! Don't mount your high horse just yet... There's more to this line of work for you to discover!"
                    obo"I'll tell you what though, You manage to hit any more performances like this and you'll earn yourself a promotion in no time!"
                    obo"Maybe you'll even be running this place in my stead soon! Hahaha!"
                else:
                    obo"Kid... you are setting unbeatable records. That's another all-time best performance!"

            elif finalscore > 5200:
                obo"Kid... I am picking my jaw from the floor... gimme a second."
                obo"..."
                obo"How the hell did you do that kid! You beat my own fucking performance. 40 years of experience... just to be bested by a kid!" with vpunch
                obo"HAHAHAHAHA!" with vpunch
                obo"You are my golden goose kid! I want to make sweet love to you so that you lay your little goose eggs."
                obo"Imagine 10 of you in my kitchen. I'd be serving entire nations!"
                obo"HahahahahahahahahaHahahahahahahahahaHahahahahahahahaha"
                "The old man has lost all sense..."
            
            elif finalscore > 4800:
                obo"You are getting dangerously close to my own performance kid..."
                obo"40 years of experience, forged in blood and sweat! Surely you can't match my skill... right? RIGHT!?"

            elif finalscore > 4500:
                obo"Rumors had it that there was someone around that would pull performances like this one. I always thought it a fairy-tale..."
                obo"But now I've witnessed it with my own eyes. You are a goddamn machine, son!"
                obo"But surely you can't beat my own performance... right? RIGHT!?"

            elif finalscore > 4200:
                obo"I can't believe it... You beat my head chef's performance. You are unreal kid!"
                obo"How much better can a little twerp be though. Surely you've reached your peak, right?"
   
            elif finalscore > 3800:
                obo"You beat my wife's performance! You are something special kid... I reckon that warrants a reward too! Talk to me some other time about that."
                obo"But you can't possibly beat my head chef's performance. Surely not..."

            elif finalscore > 3000:
                obo"Impressive kid, among the best I've seen from new recruits..."
                obo"But surely you can't match Yoru's performance... right?"
            elif finalscore >2500:
                obo"You are getting better kid! That was your best performance to date!"
            elif finalscore >2000:
                obo"Not too shabby kid! One of the better performances I've seen in a while."
            elif finalscore >1500:
                obo"Not bad... for a newbie. That was your best performance to date!"
            elif finalscore >1000:
                obo"That was your best performance yet! nothing impressive mind you, I've seen much better!"
            elif finalscore >500:
                obo"What a terrible showing..."
            else:
                obo"Kid... that was depressing."
                obo"I don't think I've ever seen a worse performance in my days..."

        if ramenlevel1 >= 3:
            obo"Kid, you are ready to move on to more challenging prep work!"
            $ notification("Ramen level 2 unlocked")
            $ unlockedramenlevel2 = True
        $ game_active = False

        if ramenkitchenintrotalk == True:
            $ yoruichiinteractiontaken = False
            jump shiftend #todo uncomment when done with tests or if starting tests
            
            # jump ramenkitchenmenu #todo uncomment when done with tests or if starting tests
        else:
            jump shiftendtutorial
        return






















style powerup_button:
    padding(10, 5)
    background "#404040"

style powerup_button_text:
    size 18

style powerup_text:
    size 20

#confirm power up purchase screen
screen confirm_purchase(powerup_name, cost):
    modal True
    style_prefix "confirm"
    zorder 10000

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 30

        vbox:
            spacing 20
            label _("Confirm Purchase")
            text _("Are you sure you want to purchase [powerup_name] for [cost] points?")
            
            hbox:
                spacing 100
                textbutton _("Yes") action Return(True)
                textbutton _("No") action Return(False)


 

# Powerup purchases
label confirm_powerup_purchase(powerup_id, powerup_text, cost):
    $ confirmed = renpy.call_screen("confirm_purchase", powerup_name=powerup_text, cost=cost)
    if confirmed:
        $ renpy.sound.play("/audio/soun_fx/attributes.opus", channel="sfxstat", loop=False, relative_volume = 1)
        $ setattr(store, f"{powerup_id}_purchased", True)
        $ ramencurrency -= cost
    else:
        pass
    return


# Point reward claims
label confirm_point_reward(reward_id, reward_text, cost, reward):
    $ confirmed = renpy.call_screen("confirm_purchase", powerup_name=reward_text, cost=cost)
    if confirmed:
        $ renpy.sound.play("/audio/soun_fx/attributes.opus", channel="sfxstat", loop=False, relative_volume = 1)
        $ setattr(store, f"{reward_id}_purchased", True)
        $ ramencurrency -= cost
        if reward != "none":
            call changeMoney(reward) from _call_changeMoney_7 
        
    else:
        pass
    return
#High score claims
label confirm_score_reward(reward_id, reward_text, required_score, reward):
    $ renpy.sound.play("/audio/soun_fx/attributes.opus", channel="sfxstat", loop=False, relative_volume = 1)
    hide screen displayTextScreen
    hide screen scrollingtextfast
    $ dailyhighscoreunlock = True
    $ setattr(store, f"{reward_id}_claimed", True)
    if reward != "none":
        call changeMoney(reward) from _call_changeMoney_8 
    hide screen workmenu
    jump expression reward_id
    return


style confirm_frame:
    background "#333333"
    xalign 0.5
    yalign 0.5

style confirm_label_text:
    size 24
    color "#FFFFFF"

style confirm_text:
    size 18
    color "#FFFFFF"

style confirm_button is button:
    padding(20, 10)
    background "#404040"
    hover_background "#606060"
    hover_sound "audio/soun_fx/select2.opus"  # Optional: add hover sound

style confirm_button_hover:
    background "#606060"  # Lighter color for hover effect

style confirm_button_text is button_text:
    size 18
    color "#FFFFFF"
    hover_color "#00FF00"

style confirm_button_text_hover:
    color "#00FF00"  # Change text color on hover (optional)




default selected_workmenu = "tutorial"
screen workmenu():

    
    default dropdown_open = False
    zorder 100

    

    key "mouseup_3" action [Hide("workmenu"), Hide("displayTextScreen")] #close with rightclick
    
    #full screen
    frame:
        xysize (1280,720)
        background Frame("gui/overlay/game_menu_2.png")
        button: #screen sized button to prevent lcicks from behind screen
            xysize (config.screen_width, config.screen_height)
            background None
            action NullAction() # No action to perform on click

        #close button
        imagebutton:    
            at customzoom3
            xalign 0.95
            yalign 0.05
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            auto "map/ui_close_%s.png"
            hovered Show("displayTextScreen", displayText = "Close Menu")
            unhovered Hide("displayTextScreen")
            action [Function(close_workmenu)]

        #left selection menu
        vbox:
            xalign 0.05 yalign 0.2
            text "Menu" xalign 0.5 size (50 if renpy.variant("pc") else 40)
        vbox:
            
            xalign (0.05 if renpy.variant("pc") else 0.02) yalign (0.5 if renpy.variant("pc") else 0.55)
            spacing 30
            #Yoruichu
            textbutton "Yoruichi":
                xalign 0.5
                hover_sound "audio/soun_fx/select2.opus"
                activate_sound "audio/soun_fx/select4.opus"
                hovered Show("displayTextScreen", displayText = "Open Yoruichi's panel")
                unhovered Hide("displayTextScreen")
                action SetVariable("selected_workmenu", "yoruichi")
            #skill tree
            textbutton "Power-ups":
                xalign 0.5
                hover_sound "audio/soun_fx/select2.opus"
                activate_sound "audio/soun_fx/select4.opus"
                hovered Show("displayTextScreen", displayText = "Open power-ups panel")
                unhovered Hide("displayTextScreen")
                action SetVariable("selected_workmenu", "powerups")
            #unlockabkles
            textbutton "Rewards":
                xalign 0.5
                hover_sound "audio/soun_fx/select2.opus"
                activate_sound "audio/soun_fx/select4.opus"
                hovered Show("displayTextScreen", displayText = "Open rewards panel")
                unhovered Hide("displayTextScreen")
                action SetVariable("selected_workmenu", "rewards")
            #tutorial
            textbutton "Tutorial":
                xalign 0.5
                hover_sound "audio/soun_fx/select2.opus"
                activate_sound "audio/soun_fx/select4.opus"
                hovered Show("displayTextScreen", displayText = "Open tutorial panel")
                unhovered Hide("displayTextScreen")
                action SetVariable("selected_workmenu", "tutorial")

            textbutton "Accessibility":
                xalign 0.5
                hover_sound "audio/soun_fx/select2.opus"
                activate_sound "audio/soun_fx/select4.opus"
                hovered Show("displayTextScreen", displayText = "Open accessibility panel")
                unhovered Hide("displayTextScreen")
                action SetVariable("selected_workmenu", "accessibility")

        #images of characters + outfits
        vbox:
            #Yoru
            xalign 1.0 yalign 0.5
            if selected_workmenu ==  "yoruichi":
                add "characters/headshots/npcs/yoruichi/yoruichi shy.webp" at dissolvehack:
                    zoom 0.36





            
   
        #right screen descriptions
        

        #skilltree
        if selected_workmenu == "powerups":
            vbox:
                xalign (0.5 if renpy.variant("pc") else 0.79) yalign 0.75
                text "Your score from each session is added to your total points!"
                text "Spend your accumulated points to purchase power ups!"
                text "Hover over each power to see a description of its effects!"
                text "Available Points: [ramencurrency:.2f]" color "#00FF00"
                if renpy.has_screen("test_rewards"):
                    hbox:
                        xalign 0.0
                        textbutton "-":
                            action SetVariable("ramencurrency", ramencurrency - 1000)
                            hover_sound "audio/soun_fx/select2.opus"
                            style "small_button"
                            hovered Show("displayTextScreen", displayText = "Decrease currency by 1000")
                            unhovered Hide("displayTextScreen")
                        textbutton "+":
                            action SetVariable("ramencurrency", ramencurrency + 1000)
                            hover_sound "audio/soun_fx/select2.opus"
                            style "small_button"
                            hovered Show("displayTextScreen", displayText = "Increase currency by 1000")
                            unhovered Hide("displayTextScreen")
                else:
                    pass
                null height 30 #add space
                text "All power ups are stackable!"
                frame:
                    background "#d3d3d320"
                    vbox:
                        $ powerups = [
                            ("multiplier1", "+10% points", 15000, "Start shifts with x0.1 added to multiplier effect"),
                            ("multiplier2", "+15% points", 20000, "Start shifts with x0.15 added to multiplier effect"),
                            ("multiplier3", "+25% points", 25000, "Start shifts with x0.25 added to multiplier effect"),
                            ("shifttimer1", "Shift Timer +5sec", 10000, "Add 5 seconds to the overall shift timer"),
                            ("shifttimer2", "Shift Timer +10sec", 15000, "Add 10 seconds to the overall shift timer"),
                            ("shifttimer3", "Shift Timer +15sec", 25000, "Add 15 seconds to the overall shift timer"),
                            ("sequencetimer1", "Sequence Timer +0.5sec", 5000, "Add 0.5 seconds to the sequence timer"),
                            ("sequencetimer2", "Sequence Timer +1.5sec", 10000, "Add 1.5 seconds to the sequence timer"),
                            ("sequencetimer3", "Sequence Timer +3sec", 15000, "Add 3 seconds to the sequence timer"),
                        ]

                        for powerup_id, powerup_text, cost, description in powerups: #for loop to create buttons for each line in the powerups array
                            $ purchased = getattr(store, f"{powerup_id}_purchased", False)
                            button:
                                xalign 0.5
                                # text f"(Cost: {cost}) {powerup_text}" color ("#00FF00" if purchased else "#808080")
                                text (powerup_text if purchased else f"(Cost: {cost}) {powerup_text}") color ("#00FF00" if purchased else "#FFFFFF" if purchased or ramencurrency >= cost else "#808080")
                                action If(purchased,
                                        NullAction(),
                                        If(ramencurrency >= cost,
                                            Call("confirm_powerup_purchase", powerup_id, powerup_text, cost), #sends name of power up to change purchase variable to True
                                            [Hide("scrollingtext"), Show("scrollingtext", text="Not enough points to purchase this powerup!")]))
                                sensitive (not purchased)
                                hover_sound "audio/soun_fx/select2.opus"
                                hovered Show("displayTextScreen", displayText = description)
                                unhovered Hide("displayTextScreen")

         




        #Rewards
        elif selected_workmenu == "rewards":
            hbox:
                if renpy.variant("mobile"):
                    xalign 0.9 yalign 0.2
                    text "Earn rewards by reaching new high-scores, or by spending your accumulated points!" size 20
                else:
                    xalign 0.9 yalign 0.2
                    text "Earn rewards by reaching new high-scores, or by spending your accumulated points!"

            # Points rewards
            frame:
                background "#d3d3d320"
                xalign 0.31 ypos (200 if renpy.variant("pc") else 200)
                vbox:
                    if renpy.variant("mobile"):
                        text "Spend points to claim!" xalign 0.5 size 20
                        text "Available Points: [ramencurrency:.2f]" color "#00FF00" xalign 0.5 size 18
                    else:
                        text "Spend points to claim!" xalign 0.5
                        text "Available Points: [ramencurrency:.2f]" color "#00FF00" xalign 0.5
                    null height 30 # add space

                    $ point_rewards = [
                        ("bonus_1", "Bonus payment 20$", 5000, 20),
                        ("bonus_2", "Bonus payment 50$", 10000, 50),
                        ("bonus_3", "Bonus payment 100$", 20000, 100),
                        ("bonus_4", "Bonus payment 50$", 30000, 50),
                        ("bonus_5", "Bonus payment 50$", 30000, 50),
                        ("bonus_6", "Bonus payment 50$", 30000, 50),
                        ("bonus_7", "Bonus payment 50$", 30000, 50),
                        ("bonus_8", "Bonus payment 50$", 30000, 50),
                        ("bonus_9", "Bonus payment 50$", 30000, 50),
                    ]

                    for reward_id, reward_text, cost, reward in point_rewards:
                        $ purchased = getattr(store, f"{reward_id}_purchased", False)
                        button:
                            xalign 0.5
                            if renpy.variant("mobile"):
                                text f"({cost}){reward_text}" color ("#808080" if purchased else "#FFFFFF") size 23
                            else:
                                text f"({cost}){reward_text}" color ("#808080" if purchased else "#FFFFFF")
                            action If(purchased,
                                    NullAction(),
                                    If(ramencurrency >= cost,
                                    Call("confirm_point_reward", reward_id, reward_text, cost, reward),
                                    [Hide("scrollingtext"), Show("scrollingtext", text="Not enough points to purchase this reward!")]))
                            # sensitive (not purchased)
                            hover_sound "audio/soun_fx/select2.opus"
                            hovered Show("displayTextScreen", displayText = "Claimed" if purchased else "Click to Unlock")
                            unhovered Hide("displayTextScreen")

            # High-score rewards
            frame:
                background "#d3d3d320"
                xalign (0.90 if renpy.variant("pc") else 1.0) ypos 200
                vbox:
                    if renpy.variant("mobile"):
                        text "Reach high-score to claim!" xalign 0.5 size 20
                        text "Current High-score: [high_score:.2f]" color "#00FF00" xalign 0.5 size 18
                        text"Can only redeem in order and once per shift." xalign 0.5 size 15
                    else:

                        text "Reach high-score to claim!" xalign 0.5
                        text "Current High-score: [high_score:.2f]" color "#00FF00" xalign 0.5
                        text"Can only redeem in order and once per shift." xalign 0.5 size 15
                    if renpy.has_screen("test_highscore"):
                        hbox:
                            xalign 0.5
                            textbutton "-":
                                action SetVariable("high_score", high_score - 1000)
                                hover_sound "audio/soun_fx/select2.opus"
                                style "small_button"
                                hovered Show("displayTextScreen", displayText = "Decrease high-score by 1000")
                                unhovered Hide("displayTextScreen")
                            textbutton "+":
                                action SetVariable("high_score", high_score + 1000)
                                hover_sound "audio/soun_fx/select2.opus"
                                style "small_button"
                                hovered Show("displayTextScreen", displayText = "Increase high-score by 1000")
                                unhovered Hide("displayTextScreen")
                    null height 20 # add space
                    $ score_rewards = [
                        ("score_1", "Obo has a gift for you", 1000, "none", None),
                        ("score_2", "Yoruichi's Story 1", 2000, "none", "score_1"),
                        ("score_3", "Yoruichi's Story 2 (Yoruichi's score)", 3800, "none", "score_2"),
                        ("score_4", "Obo's Story 1 (Head Chef's score)", 4200, "none", "score_3"), #4200
                        ("score_5", "WIP - Obo's Story 2 (Developer's score)", 999999, "none", "score_4"), #4500
                        ("score_6", "WIP - Yoruichi's Story 3", 999999, "none", "score_5"), #4800
                        ("score_7", "WIP - Obo's Story 3 (Obo's score)", 999999, "none", "score_6"), #5200
                        ("score_8", "WIP - An important choice awaits you", 999999, "none", "score_7"), #5500
                    ]

                    for reward_id, reward_text, required_score, reward, previous_reward in score_rewards:
                        $ claimed = getattr(store, f"{reward_id}_claimed", False)
                        $ previous_claimed = True if previous_reward is None else getattr(store, f"{previous_reward}_claimed", False)
                        button:
                            xalign 0.5
                            if renpy.variant("mobile"):
                                text f"{required_score} - {reward_text}" color ("#808080" if claimed else "#FFFFFF") size 25
                            else:
                                text f"{required_score} - {reward_text}" color ("#808080" if claimed else "#FFFFFF")

                            action If(claimed,
                                    NullAction(),
                                    If(high_score >= required_score and previous_claimed and not dailyhighscoreunlock,
                                    [Hide("displayTextScreen"), Call("confirm_score_reward", reward_id, reward_text, required_score, reward)],
                                    NullAction()))
                            sensitive (not claimed and high_score >= required_score and not dailyhighscoreunlock)
                            hover_sound "audio/soun_fx/select2.opus"
                            hovered Show("displayTextScreen", displayText = get_reward_hover_text(claimed, high_score, required_score, previous_claimed, dailyhighscoreunlock))
                            unhovered Hide("displayTextScreen")

        elif selected_workmenu == "tutorial":
            hbox:
                xalign 0.6 yalign 0.2
                add "ramentutorial.png" zoom 0.45
            frame:
                xalign (0.6 if renpy.variant("pc") else 0.6) yalign (0.53 if renpy.variant("pc") else 0.53)
                background "#00000080"
                vbox:
                    if renpy.variant("mobile"):
                        text "1. Displays all-time highscore and current session's score" xalign 0.0 size 25
                        text "2. Overall timer and remaining mistakes allowed" xalign 0.0 size 25
                        text "3. Current sequence to input and time left to do so" xalign 0.0 size 25
                        text "4. Notifications (Score gained, multipliers, fails, etc.) " xalign 0.0 size 25
                    else:
                        text "1. Displays all-time highscore and current session's score" xalign 0.5
                        text "2. Overall timer and remaining mistakes allowed" xalign 0.5
                        text "3. Current sequence to input and time left to do so" xalign 0.5
                        text "4. Notifications (Score gained, multipliers, fails, etc.) " xalign 0.5
            vbox:
                xalign 0.65 yalign (0.96 if renpy.variant("pc") else 0.99)
                text"Game Rules:" xalign 0.5
                text"-The session counts as 'completed' if you correctly input all sequences up until the overall timer hits 0.0" size 15 xalign 0.5
                text"-The session counts as 'lost' when you make 3 mistakes OR if the sequence timer runs out" size 15 xalign 0.5
                text"-Earn points by completing sequences with progressive difficulty" size 15 xalign 0.5
                text"-Completing a series of 5 sequences grants you an increasing score multiplier" size 15 xalign 0.5
                text"and increases the difficulty of the next series of sequences by adding one additional input" size 15 xalign 0.5
                null height 20 # add space
                text"Seek balance between speed and accuracy in order to achieve the best result" size 15 xalign 0.5 color correct_color
                text"Every 100 points you score will net you 1$ in payment!" size 15 xalign 0.5 color correct_color
                null height 10 # add space
                text"Score calculation for each completed sequence follows this formula:" size 12 xalign 0.5
                text"(100 + remaining sequence time) * multiplier" size 12 xalign 0.5
                text"EG(Time left = 4, Multiplier = x1.2): (100 + 4) *1.2 = 124.8 " size 12 xalign 0.5



        elif selected_workmenu == "yoruichi":
            vbox:
                xalign 0.4 yalign 0.4
                text "Name: Yoruichi" xalign 0.5
                text "Affiliation: Co-worker" xalign 0.5
                text "Age: 40" xalign 0.5
                textbutton "Relationship: {color=[relationship_colors.get(yoruichi_relationship, '#FFFFFF')]}[yoruichi_relationship]{/color}":
                    xalign 0.5
                    action NullAction()
                    hover_sound "audio/soun_fx/select2.opus"
                    hovered Show("displayTextScreen", displayText = 
                    "Yoruichi disregards your presence. She is distant and aloof" if yoruichi_relationship == "Passive" else
                    "Yoruichi tolerates your presence and tries to maintain a professional approach" if yoruichi_relationship == "Formal" else
                    "Yoruichi is fearful of what you've become. She hates who you are {p}but reluctantly listens to you out of need." if yoruichi_relationship == "Apprehensive" else
                    "Yoruichi obeys your wishes to a certain extend." if yoruichi_relationship == "Obedient" else
                    "Yoruichi involuntarily obeys your wishes to a certain extend." if yoruichi_relationship == "Unwillingly Obedient" else
                    "Unknown relationship status")
                    unhovered Hide("displayTextScreen")
                #outfits
                textbutton "Outfit: [yoruichi_clothes]":
                    xalign 0.5
                    action ToggleScreenVariable("dropdown_open")
                    hover_sound "audio/soun_fx/select2.opus"
                    hovered Show("displayTextScreen", displayText = "Check Yoruichi's available outfits")
                    unhovered Hide("displayTextScreen")
                
                showif dropdown_open:
                    frame:
                        xalign 0.5
                        style "dropdown_frame"
                        vbox:
                            textbutton "Casual":
                                action [SetVariable("yoruichi_clothes", "Normal"), SetScreenVariable("dropdown_open", False)]
                            textbutton "Cut-Short (Locked)":
                                sensitive False
                                action [SetVariable("yoruichi_clothes", "Cut-short"), SetScreenVariable("dropdown_open", False)]
                            textbutton "Slutty (Locked)":
                                sensitive False
                                action [SetVariable("yoruichi_clothes", "Slutty (Locked)"), SetScreenVariable("dropdown_open", False)]
                            textbutton "Slutty Lv2 (Locked)":
                                sensitive False
                                action [SetVariable("yoruichi_clothes", "Slutty (Locked)"), SetScreenVariable("dropdown_open", False)]
                            textbutton "Naked (Locked)":
                                sensitive False
                                action [SetVariable("yoruichi_clothes", "Slutty (Locked)"), SetScreenVariable("dropdown_open", False)]
                null height 30 #add space
                frame:
                    xalign 0.65 yalign 0.53
                    background "#d3d3d320"
                    vbox:
                               
                        text "Complete objectives to" xalign 0.5
                        text "advance relationship:" xalign 0.5
                        null height 10 #add space

                        #Objectives defined at start of minigames.rpy
                        if yoruichi_relationship == "Passive":
                            for objective in yoruichi_objectives_passive:
                                $ completed = "{color=#00FF00}✓{/color} " if objective["completed"] else ""
                                button:
                                    text "[completed][objective['description']]"
                                    action NullAction()
                                    hover_sound "audio/soun_fx/select2.opus"
                                    hovered Show("displayTextScreen", displayText = objective["description"])
                                    unhovered Hide("displayTextScreen")

                        elif yoruichi_relationship == "Formal":
                            for objective in yoruichi_objectives_formal:
                                $ completed = "{color=#00FF00}✓{/color} " if objective["completed"] else ""
                                button:
                                    text "[completed][objective['description']]"
                                    action NullAction()
                                    hover_sound "audio/soun_fx/select2.opus"
                                    hovered Show("displayTextScreen", displayText = objective["description"])
                                    unhovered Hide("displayTextScreen")

                        elif yoruichi_relationship == "Apprehensive":
                            for objective in yoruichi_objectives_apprehensive:
                                $ completed = "{color=#00FF00}✓{/color} " if objective["completed"] else ""
                                button:
                                    text "[completed][objective['description']]"
                                    action NullAction()
                                    hover_sound "audio/soun_fx/select2.opus"
                                    hovered Show("displayTextScreen", displayText = objective["description"])
                                    unhovered Hide("displayTextScreen")

                        elif yoruichi_relationship == "Obedient":
                            for objective in yoruichi_objectives_obedient:
                                $ completed = "{color=#00FF00}✓{/color} " if objective["completed"] else ""
                                button:
                                    text "[completed][objective['description']]"
                                    action NullAction()
                                    hover_sound "audio/soun_fx/select2.opus"
                                    hovered Show("displayTextScreen", displayText = objective["description"])
                                    unhovered Hide("displayTextScreen")

                        elif yoruichi_relationship == "Unwillingly Obedient":
                            for objective in yoruichi_objectives_obedient_unwilling:
                                $ completed = "{color=#00FF00}✓{/color} " if objective["completed"] else ""
                                button:
                                    text "[completed][objective['description']]"
                                    action NullAction()
                                    hover_sound "audio/soun_fx/select2.opus"
                                    hovered Show("displayTextScreen", displayText = objective["description"])
                                    unhovered Hide("displayTextScreen")


        if selected_workmenu == "accessibility":
            vbox:
                xalign (0.5 if renpy.variant("pc") else 0.6) yalign 0.3
                text "Customize your settings to suit your preference"
                text "Check the Power-ups panel as well!"
                text "Some Power-ups are designed for accessibility!"
                null height 50 #add space
                frame:
                    background "#d3d3d320"
                    vbox:
                        spacing 20
                        # Arrow color settings
                        text "Arrow Colors:" style "powerup_text"
                        hbox:
                            spacing 20
                            for direction in ["Up", "Down", "Left", "Right"]:
                                vbox:
                                    text direction style "powerup_text"
                                    textbutton "Change Color":
                                        style "powerup_button"
                                        text_color arrow_colors[direction.lower()]
                                        action Show("color_picker", direction=direction.lower())

                        # Video/Image toggle
                        text "Video Settings:" style "powerup_text"
                        textbutton ("Show Video" if use_video_background else "Show Still Image"):
                            style "powerup_button"
                            action ToggleVariable("use_video_background")
                text "Setting one of LEFT/RIGHT arrows to a different color is generally helpful for readability" size 14.5



