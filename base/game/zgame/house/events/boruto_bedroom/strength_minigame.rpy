label strengthmenu:
    call hideUI from _call_hideUI_12
    default strengthtutorial = False
    if strengthtutorial == False:
        show boruto normal with dissolve
        bo"Tsunade did say on that day that this curse of mine might not be all doom and gloom..."
        bo"She said that it could even affect my physicality in unforseen ways..."
        show boruto embarassed with dissolve
        bo"She went on about, uuh... Somatic cells multiplying... or something?"
        show boruto worried2 with dissolve
        bo"No matter..."
        bo"Those debt collecting men the other day... they pushed me away like I was nothing to them!"
        bo"If I want to protect myself and those I care for, I better get stronger, and fast..."
        bo"I wonder what might happen if I put some effort into this..."
        show boruto snob with dissolve
        bo"Can I get stronger than my mentor, uncle Sasuke?"
        show boruto worried with dissolve
        bo"Stronger than even... [na_rel]?"
        bo"Only one way to find out..."
        $ renpy.sound.play("/audio/soun_fx/clothes_dress.opus", channel="sfx2", loop=False, relative_volume = 0.5)
        scene black with dissolve
        "You take off your shirt..."
        show bedroom_gymstart with dissolve
        bo"I've always had a small frame, but quite a lean physique. Would be fun to find out if I can get as muscular as [na_rel]!"
        bo"But before that..."
        bo"There's nothing better than some exciting music to get you pumped during training! What should I put on..."
        menu:
            bot"There's nothing better than some exciting music to get you pumped during training! What should I put on..."
            "[na_rel]'s favorite":
            #reversesituaiton
                $ radiostation = 1                 
                $ playmusic("audio/ost/reversesituation.opus",0.6)
                bo"[na_rel]'s favorite... Not my style, but it will have to do!"
            "[na_rel]'s CD":
                #lightnign
                $ radiostation = 2        
                $ playmusic("audio/ost/lightningspeed.opus",0.7)
                bo"[na_rel] let me have this a while ago. Said he is way past those days..."
            "Mysterious CD":
                $ radiostation = 3 
                $ playmusic("audio/ost/gym_Junkyousha.opus",0.8)
                bo"I don't even know where this one came from, but it bangs!"
            "Root CD":
                $ radiostation = 4 
                $ playmusic("audio/ost/nightattack.opus",0.7)
                bo"[na_rel] said he doesn't even remember where he got this from. Sounds like old men's music, but it gets me going!"
            "Mentor's CD":
                $ radiostation = 5 
                $ playmusic("audio/ost/kokuten.opus",0.6)
                bo"My mentor's CD. Much better than what [na_rel] listens to!"
            "[bo_name]'s CD":
                $ radiostation = 6  
                $ playmusic("audio/ost/borutotheme.opus",0.5)
                bo"The new shit! This is my jam!"

        "You can now train to increase your 'Strength'!"
        "Increasing your strength might present new opportunities and events!"
        "It might even prove useful in defending yourself from adversaries that would see you, or those around you harmed."
        $ notification ("Strength training unlocked")
        show screen gymmenutopright with dissolve
        show expression FocusEffect("idle1", 1160, 50, 125, 0.7) as focus_effect onlayer screens with dissolve
        "Use the Training menu on the top right to track your progress."
        hide focus_effect  onlayer screens with dissolve
        $ strengthtutorial = True
        jump bedroom_training_menu
    
    else:
        if radiostation == 1:
            $ playmusic("audio/ost/reversesituation.opus",0.6)
        elif radiostation == 2:    
            $ playmusic("audio/ost/lightningspeed.opus",0.7)
        elif radiostation == 3:
            $ playmusic("audio/ost/gym_Junkyousha.opus",0.8)
        elif radiostation == 4:
            $ playmusic("audio/ost/nightattack.opus",0.7)
        elif radiostation == 5:
            $ playmusic("audio/ost/kokuten.opus",0.6)
        elif radiostation == 6: 
            $ playmusic("audio/ost/borutotheme.opus",0.5)
        scene black with dissolve
        "You take off your shirt..."
        show bedroom_gymstart with dissolve
        menu bedroom_training_menu:
            "..."
            "Begin Training":
                jump start_strength_minigame
                
            "Change Radio":
                default radiostation = 0
                menu:
                    bot"What should I put on..."
                    "[na_rel]'s favorite":
                    #reversesituaiton
                        $ radiostation = 1                 
                        $ playmusic("audio/ost/reversesituation.opus",0.75)
                        $ change_music_volume(0.8, 1.0)
                        bo"[na_rel]'s favorite... Not my style, but it will have to do!"
                    "[na_rel]'s CD":
                        #lightnign
                        $ radiostation = 2        
                        $ playmusic("audio/ost/lightningspeed.opus",0.85)
                        $ change_music_volume(0.8, 1.0)
                        bo"[na_rel] let me have this a while ago. Said he is way past those days..."
                    "Mysterious CD":
                        $ radiostation = 3 
                        $ playmusic("audio/ost/gym_Junkyousha.opus",0.99)
                        $ change_music_volume(0.8, 1.0)
                        bo"I don't even know where this one came from, but it bangs!"
                    "Root CD":
                        $ radiostation = 4 
                        $ playmusic("audio/ost/nightattack.opus",0.85)
                        $ change_music_volume(0.8, 1.0)
                        bo"[na_rel] said he doesn't even remember where he got this from. Sounds like old men's music, but it gets me going!"
                    "Mentor's CD":
                        $ radiostation = 5 
                        $ playmusic("audio/ost/kokuten.opus",0.75)
                        $ change_music_volume(0.8, 1.0)
                        bo"My mentor's CD. Much better than what [na_rel] listens to!"
                    "[bo_name]'s CD":
                        $ radiostation = 6
                        $ playmusic("audio/ost/borutotheme.opus",0.6)
                        $ change_music_volume(0.5, 1.0)
                        bo"The new shit! This is my jam!"
                jump bedroom_training_menu

            "Information":
                $ selected_level = strength
                show screen gymmenu
                jump bedroom_training_menu
            "Return":
                bo"Meh, not feeling like it."
                call hideUI from _call_hideUI_61
                if day_part == 1:
                    jump bedroom_boruto_morning
                elif day_part == 2:
                    jump bedroom_boruto_evening
                elif day_part == 3 or day_part ==4:
                    jump bedroom_boruto_night
                




init python:
 
    def close_gymmenu():
        renpy.hide_screen("gymmenu")
        renpy.hide_screen("displayTextScreen")




screen gymmenutopright():
    imagebutton:
        xalign 0.98 yalign 0.02
        auto "images/ui/workmenu2_%s.webp"
        hovered Show("displayTextScreen", displayText = "Open Strength Menu")
        unhovered [Hide("displayTextScreen")]
        action [SetVariable("selected_level", strength),SetVariable("selected_gymmenu", "Boruto"),Show("gymmenu")]
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"

default selected_gymmenu = "Boruto"

screen gymmenu():
    
    default dropdown_open = False
    zorder 1011
    
    

    key "mouseup_3" action [Hide("gymmenu"), Hide("displayTextScreen")] #close with rightclick
    
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
            action [Function(close_gymmenu)]

        #left selection menu
        vbox:
            xalign 0.05 yalign 0.2
            text "Menu" xalign 0.5 size (50 if renpy.variant("pc") else 40)
        vbox:
            
            xalign (0.05 if renpy.variant("pc") else 0.02) yalign (0.5 if renpy.variant("pc") else 0.55)
            spacing 30
            #Boruto
            textbutton "[bo_name]":
                xalign 0.5
                hover_sound "audio/soun_fx/select2.opus"
                activate_sound "audio/soun_fx/select4.opus"
                hovered Show("displayTextScreen", displayText = "Open [bo_name]'s panel")
                unhovered Hide("displayTextScreen")
                action [SetVariable("selected_gymmenu", "Boruto")]
            #Opoortunities
            textbutton "Opportunities":
                xalign 0.5
                hover_sound "audio/soun_fx/select2.opus"
                activate_sound "audio/soun_fx/select4.opus"
                hovered Show("displayTextScreen", displayText = "Open Opportunities panel")
                unhovered Hide("displayTextScreen")
                action [SetVariable("selected_gymmenu", "Opportunities")]

            #Tutorial
            textbutton "Tutorial":
                xalign 0.5
                hover_sound "audio/soun_fx/select2.opus"
                activate_sound "audio/soun_fx/select4.opus"
                hovered Show("displayTextScreen", displayText = "Open Tutorial panel")
                unhovered Hide("displayTextScreen")
                action [SetVariable("selected_gymmenu", "Tutorial")]

        vbox:
            #
            xalign 1.0 yalign 0.5
            if selected_gymmenu ==  "Boruto":
                add "boruto boxers1_smirk" at dissolvehack:
                    zoom 0.4 ypos 50



        if selected_gymmenu == "Boruto":
            vbox:
                xalign 0.4 yalign 0.4
                text "[bo_name]" xalign 0.5
                text "Strength: Level [strength]" xalign 0.5
                null height 40 #add space
                frame:
                    xalign 0.65 yalign 0.53
                    background "#d3d3d320"
                    vbox:
                               
                        text "Fill the bar to unlock your potential" xalign 0.5
                        text "and uncover new opportunities!" xalign 0.5
                        null height 20 #add space
                        use strength_balance_bar
                        
                
            
   
        #right screen descriptions
        elif selected_gymmenu == "Opportunities":
            vbox:
                xalign (0.5 if renpy.variant("pc") else 0.79) yalign 0.45
                text "Increasing your strength to certain levels"
                text "will present you with new opportunities."
                text "You can keep track of them below!"
                null height 50 #add space
                text "Current Strength: Level [strength]"
                if selected_level == strength:
                    text "Current Strength Points: [strengthlevel]" color "#00FF00"
                elif selected_level < strength:
                    text"Already unlocked" color "#00FF00"
                else:
                    text"Current Strength level too low!" color "#FF0000"
                null height 30 #add space

                textbutton "Displayed Level: [selected_level]":
                    action ToggleScreenVariable("dropdown_open")
                    hover_sound "audio/soun_fx/select2.opus"
                    hovered Show("displayTextScreen", displayText = "Show opportunities for selected level")
                    unhovered Hide("displayTextScreen")

                showif dropdown_open:
                    frame:
                        style "dropdown_frame"
                        vbox:
                            textbutton "Level 0":
                                action [SetVariable("selected_level", 0), SetScreenVariable("dropdown_open", False)]
                            textbutton "Level 1":
                                action [SetVariable("selected_level", 1), SetScreenVariable("dropdown_open", False)]
                            textbutton "Level 2":
                                action [SetVariable("selected_level", 2), SetScreenVariable("dropdown_open", False)]
                

                

                frame:
                    background "#d3d3d320"
                    vbox:
                        if selected_level >= 3: #todo change when new strength levels are introduced in the future
                            $ opportunities  = [
                                ("op_error1", "???", 0, "???"),
                                ("op_error2", "???", 0, "???"),
                                ("op_error3", "???", 0, "???"),

                            ]
                        else:

                            if selected_level == 0:
                                $ opportunities  = [
                                    ("l0_opportunity1", "1.", 20, "-Someone may interrupt your workouts..."),
                                    ("l0_opportunity2", "2.", 50, "-Perhaps you could stop them!"),
                                    ("l0_opportunity3", "3.", 100, "-You can now overpower [him_name]!"),

                                ]
                            elif selected_level == 1:
                                $ opportunities  = [
                                    ("l1_opportunity1", "1.", 20, "-Someone may take notice of your efforts!"),
                                    ("l1_opportunity2", "2.", 50, "-You can now train with [hin_name]!"),
                                    ("l1_opportunity3", "3.", 80, "-You may be able to overpower even a Shinigami!"),
                                    ("l1_opportunity3", "4.", 100, "You can now 'help' [hin_name] during her workouts!"),

                                ]
                            elif selected_level == 2:
                                $ opportunities  = [
                                    ("l2_opportunity1", "1.", 20, "-You may be able to overpower a strong adversary!"),
                                    ("l2_opportunity2", "2.", 50, "-(WIP)"),
                                    ("l2_opportunity3", "3.", 100, "-(WIP)"),

                                ]

                        for opportunity_id, opportunity_text, cost, description in opportunities:
                            $ unlocked = strengthlevel >= cost
                            if selected_level < strength:
                                text (description)color ("#00FF00")

                            else:
                                text (description if unlocked else f"({cost}) {description}") color ("#00FF00" if unlocked else "#808080")

        elif selected_gymmenu == "Tutorial":
            hbox:
                xalign 0.6 yalign 0.1
                add "strengthtutorial" zoom 0.45
            frame:
                xalign (0.6 if renpy.variant("pc") else 0.6) yalign (0.53 if renpy.variant("pc") else 0.53)
                background "#00000080"
                vbox:
                    if renpy.variant("mobile"):
                        text "1. Displays your stamina gauge. Letting it deplete ends the game" xalign 0.0 size 25
                        text "2. Info panel: Timer left, Completed pushups, STAM depletion rate" xalign 0.0 size 25
                        text "3. Boost zones. Tapping them grants the player benefits" xalign 0.0 size 25
                    else:
                        text "1. Displays your stamina gauge. Letting it deplete ends the game" xalign 0.5
                        text "2. Info panel: Timer left, Completed pushups, STAM depletion rate" xalign 0.5
                        text "3. Boost zones. Tapping them grants the player benefits" xalign 0.5
            vbox:
                xalign 0.6 yalign (0.96 if renpy.variant("pc") else 0.99)
                text"Game Rules:" xalign 0.5
                text"-The session ends when either the timer, or the stamina gauge runs out." size 15 xalign 0.5
                text"-Click as fast as you can to keep the stamina gauge full!" size 15 xalign 0.5
                text"-[bo_name] tires out the longer the session is active causing the gauge to deplete faster!" size 15 xalign 0.5
                text"-Tapping the yellow boost zones will grant [bo_name] a temporary boost to his stamina" size 15 xalign 0.5
                text"-Every 10 clicks count as one pushup" size 15 xalign 0.5
                null height 20 # add space
                text"Pace yourself and opportunistically pick up boost zones to complete as many pushups as possible!" size 15 xalign 0.5 color correct_color
                text"1 pushup = 1 strength point acquired" size 15 xalign 0.5 color correct_color
                null height 10 # add space
                text"Acquiring 100 total strength points" size 12 xalign 0.5
                text"Will increase your Strength Level" size 12 xalign 0.5

init python:
    strengthlevel = 0
    selected_level = 0

    class StrengthBar(renpy.Displayable):
        def __init__(self, width, height, value, **kwargs):
            super(StrengthBar, self).__init__(**kwargs)
            self.width = width
            self.height = height
            self.value = value
            
        def render(self, width, height, st, at):
            render = renpy.Render(self.width, self.height)
            
            # Create the background first
            bg = renpy.Render(self.width, self.height)
            bg.fill("#444444")  # Dark gray background
            render.blit(bg, (0, 0))  # Blit background first
            
            # Calculate the center position
            center = self.width // 2
            
            # Create the foreground bar
            bar_width = int((self.value / 100.0) * self.width)
            if bar_width > 0:  # Only create bar if there's a positive width
                bar = renpy.Render(bar_width, self.height)
                bar.fill("#FF6666")  # Red for the bar
                render.blit(bar, (0, 0))  # Blit bar starting from the left
            
            return render
        
        def event(self, ev, x, y, st):
            return None
        
        def visit(self):
            return []

screen strength_balance_bar:
    frame:
        xalign 0.5
        yalign 0.5
        background None  # Removes the background
        padding (0,0)    # Removes the padding
        vbox:
            spacing 10
            text "Strength Points: [strengthlevel]/100" xalign 0.5
            fixed:
                xsize 400
                ysize 30
                add StrengthBar(400, 30, strengthlevel)
                
    







init python:
    import math
    import random

    class StrengthMinigame2():
        def __init__(self, win_label, lose_label, impossible=False, strength_level=0):
            self.strength_level = strength_level
            self.impossible = impossible
            
            # Adjust timer based on conditions
            base_time = 5.0 if impossible else 10.0
            self.time_remaining = base_time * (1 + strength_level/100.0)
            
            self.progress = 0.0
            self.clicks = 0
            # Adjust drain rate based on conditions
            base_drain = 2.0 * (20.0 if impossible else 1.0)  # 20x drain if impossible
            self.drain_multiplier = base_drain * (1 - strength_level/100.0)  # Reduce by strength level %
            
            self.shake_intensity = 0.0
            self.start_time = None
            self.game_ended = False
            self.win_label = win_label
            self.lose_label = lose_label
            self.strength_gained = 0  # Track strength points gained

        def update(self):
            if self.start_time is None:
                self.start_time = renpy.time.time()
                
            current_time = renpy.time.time()
            elapsed = current_time - self.start_time
            self.time_remaining = max(0, self.time_remaining - (current_time - self.start_time))
            self.start_time = current_time
            
            base_intensity = 10.0
            max_intensity = 30.0
            progress_factor = self.progress / 100.0
            self.shake_intensity = base_intensity + (max_intensity - base_intensity) * progress_factor
            
            if self.time_remaining <= 0:
                self.game_ended = True
                renpy.jump(self.lose_label)
                
            if not self.game_ended:
                self.progress = max(0.0, self.progress - (2.0 * 0.0167 * self.drain_multiplier))

        def handle_click(self):
            if self.game_ended:
                return
                
            self.progress = min(100.0, self.progress + 5.0)
            self.clicks += 1
            # Check for every 10th click
            if self.clicks % 10 == 0:
                if store.strengthlevel < 100:
                    store.strengthlevel += 1
                    self.strength_gained += 1
                    renpy.sound.play("/audio/soun_fx/multiplier2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                    renpy.hide_screen("scrollingtextfast")
                    store.texttosend = f"You gained {{color=#00ff00}}+1{{/color}} STR points"
                    renpy.show_screen("scrollingtextfast", store.texttosend)
            # Only check for win if not in impossible mode
            if not self.impossible and self.progress >= 100.0:
                self.game_ended = True                
                renpy.jump(self.win_label)
                

transform game_shake2(intensity):
    xoffset 0 yoffset 0
    block:
        parallel:
            linear 0.05 xoffset intensity * random.uniform(-1, 1)
            linear 0.05 xoffset intensity * random.uniform(-1, 1)
            repeat
        parallel:
            linear 0.05 yoffset intensity * random.uniform(-1, 1)
            linear 0.05 yoffset intensity * random.uniform(-1, 1)
            repeat


screen strength_minigame2(win_label, lose_label, imageadd, setyaling =0.5, impossible=False, strength_level=0):
    modal True
    
    default game2 = StrengthMinigame2(win_label, lose_label, impossible, strength_level)
    
    timer 0.0167 repeat True action Function(game2.update)
    
    frame:
        background None
        xfill True
        yfill True
        at game_shake2(game2.shake_intensity)

        add imageadd xalign 0.5 yalign setyaling at transform:
                alpha 1.0
                on show:
                    alpha 0.0
                    linear 0.1 alpha 1.0
        
        frame:
            background "#2a2a2a"
            xsize 80
            ysize 400
            xpos 50
            yalign 0.5
            padding (10, 10)
            
            vbox:
                spacing 10
                text "PROG" size 20 color "#aaa" xalign 0.5
                
                bar:
                    value AnimatedValue(game2.progress, 100.0)
                    range 100 
                    ysize 350
                    xsize 40
                    xalign 0.5
                    left_bar "#444"
                    right_bar "#0f0"
                    bar_vertical True
        
        frame:
            xalign 0.5
            ypos 50
            background "#2a2a2a"
            padding (20, 20)
            
            vbox:
                spacing 10
                text "Time left: {:.1f}".format(max(0, game2.time_remaining)) color "#fff" size 30
                text "STR gained: [game2.strength_gained]" color "#fff" size 30
        
        button:
            background None
            xfill True
            yfill True
            action Function(game2.handle_click)






    #
    #
    #
    #
    #
    #
    #
    #
    #
init python:
    class StrengthMinigame():
        def __init__(self):
            self.time_remaining = 30.0
            self.stamina = 100.0
            self.clicks = 0  # Track raw clicks
            self.pushups = 0  # Track pushups (clicks / 10)
            self.base_stamina_drain = 30
            self.drain_multiplier = 1.0    
            self.base_click_recovery = 10.0
            self.recovery_multiplier = 1.0  
            self.shake_intensity = 0.0
            self.boost_zones = []          
            self.next_boost_time = 25.0    
            self.start_time = None
            self.game_ended = False
            self.ended_by_stamina = False
            self.drain_reduction = 1.0

        def update(self):
            if self.start_time is None:
                self.start_time = renpy.time.time()
                
            current_time = renpy.time.time()
            elapsed = current_time - self.start_time
            self.time_remaining = max(0, 30.0 - elapsed)
            
            # Calculate increasing difficulty (increases to 3.2)
            self.drain_multiplier = (1.0 + (3.0 * elapsed / 30.0)) * self.drain_reduction
            
            # Calculate decreasing recovery (decreases to 20% of original)
            self.recovery_multiplier = 1.0 - (0.80 * elapsed / 30.0)
            
            # Update pushups count
            self.pushups = self.clicks // 10
            
            # Check both time and stamina for game end
            if self.stamina <= 0:
                self.game_ended = True
                self.ended_by_stamina = True
                self.shake_intensity = 0.0
                return
            elif self.time_remaining <= 0:
                self.game_ended = True
                self.ended_by_stamina = False
                self.shake_intensity = 0.0
                return
                
            # Update shake intensity based on stamina
            base_intensity = 10.0
            max_intensity = 30.0
            stamina_factor = (1.0 - self.stamina / 100.0)
            self.shake_intensity = base_intensity + (max_intensity - base_intensity) * stamina_factor
            
            # Drain stamina with increasing difficulty
            self.stamina = max(0.0, self.stamina - (self.base_stamina_drain * 0.0167 * self.drain_multiplier))
            
            # Handle boost zones
            if self.time_remaining <= self.next_boost_time and self.time_remaining > 5.0:
                self.spawn_boost_zone()
                self.next_boost_time -= 5.0

        def handle_click(self):
            if self.game_ended:
                return
                
            recovery_amount = self.base_click_recovery * self.recovery_multiplier
            self.stamina = min(100.0, self.stamina + recovery_amount)
            self.clicks += 1

        def activate_boost(self):
            if self.game_ended:
                return
                
            boost_amount = 50.0 * (self.recovery_multiplier * 0.5 + 0.5)
            self.stamina = min(100.0, self.stamina + boost_amount)
            self.drain_reduction *= 0.85
            renpy.sound.play("/audio/soun_fx/multiplier2.opus", channel="sfx2", loop=False, relative_volume = 0.9)
            self.boost_zones = []
                    
        def spawn_boost_zone(self):
            x = random.randint(100, config.screen_width - 100)
            y = random.randint(100, config.screen_height - 100)
            self.boost_zones.append((x, y))


    class StrengthMinigameHinata():
        def __init__(self):
            self.time_remaining = 30.0
            self.stamina = 100.0
            self.clicks = 0
            self.pushups = 0
            self.base_stamina_drain = 30
            self.drain_multiplier = 1.0    
            self.base_click_recovery = 10.0
            self.recovery_multiplier = 1.0  
            self.shake_intensity = 0.0
            self.boost_zones = []          
            self.next_boost_time = 25.0    
            self.start_time = None
            self.game_ended = False
            self.ended_by_stamina = False
            self.drain_reduction = 1.0
            self.competitor_cap = None  # Will be set from screen
            
            # Calculate difficulty reduction based on strength and strengthlevel
            if strength >= 2:
                self.difficulty_reduction = 0.75  # 75% reduction
            elif strength == 1:
                self.difficulty_reduction = strengthlevel / 65.0  # 0-65% reduction
            else:
                self.difficulty_reduction = 0.0  # No reduction

            # Adjust click requirement based on difficulty reduction
            self.clicks_per_squat = max(5, int(10 * (1.0 - self.difficulty_reduction)))

        def set_competitor_cap(self, cap):
            self.competitor_cap = cap

        def update(self):
            if self.start_time is None:
                self.start_time = renpy.time.time()
                
            current_time = renpy.time.time()
            elapsed = current_time - self.start_time
            self.time_remaining = max(0, 30.0 - elapsed)
            
            # Modified drain multiplier calculation with difficulty reduction
            base_drain = 1.0 + (3.0 * elapsed / 30.0)
            self.drain_multiplier = (base_drain * (1.0 - self.difficulty_reduction)) * self.drain_reduction
            
            # Calculate decreasing recovery (decreases to 20% of original)
            self.recovery_multiplier = 1.0 - (0.80 * elapsed / 30.0)
            
            # Handle pushup counting and capping
            potential_pushups = self.clicks // self.clicks_per_squat
            
            # Apply cap if strength < 1 and we have a competitor cap
            if strength < 1 and self.competitor_cap is not None:
                self.pushups = min(potential_pushups, max(0, int(self.competitor_cap) - 1))
            else:
                self.pushups = potential_pushups
            
            # Check both time and stamina for game end
            if self.stamina <= 0:
                self.game_ended = True
                self.ended_by_stamina = True
                self.shake_intensity = 0.0
                return
            elif self.time_remaining <= 0:
                self.game_ended = True
                self.ended_by_stamina = False
                self.shake_intensity = 0.0
                return
                
            # Update shake intensity based on stamina
            base_intensity = 10.0
            max_intensity = 30.0
            stamina_factor = (1.0 - self.stamina / 100.0)
            self.shake_intensity = base_intensity + (max_intensity - base_intensity) * stamina_factor
            
            # Modified stamina drain with difficulty reduction
            effective_drain = self.base_stamina_drain * (1.0 - self.difficulty_reduction)
            self.stamina = max(0.0, self.stamina - (effective_drain * 0.0167 * self.drain_multiplier))
            
            # Handle boost zones
            if self.time_remaining <= self.next_boost_time and self.time_remaining > 5.0:
                self.spawn_boost_zone()
                self.next_boost_time -= 5.0

        def handle_click(self):
            if self.game_ended:
                return
                
            # Check if we should allow more clicks based on cap
            if strength < 1 and self.competitor_cap is not None:
                potential_pushups = (self.clicks + 1) // self.clicks_per_squat
                if potential_pushups >= int(self.competitor_cap):
                    return
                
            recovery_amount = self.base_click_recovery * self.recovery_multiplier
            self.stamina = min(100.0, self.stamina + recovery_amount)
            self.clicks += 1

        def activate_boost(self):
            if self.game_ended:
                return
                
            boost_amount = 50.0 * (self.recovery_multiplier * 0.5 + 0.5)
            self.stamina = min(100.0, self.stamina + boost_amount)
            self.drain_reduction *= 0.85
            renpy.sound.play("/audio/soun_fx/multiplier2.opus", channel="sfx2", loop=False, relative_volume = 0.9)
            self.boost_zones = []
                    
        def spawn_boost_zone(self):
            x = random.randint(100, config.screen_width - 100)
            y = random.randint(100, config.screen_height - 100)
            self.boost_zones.append((x, y))

transform game_shake(intensity):
    xoffset 0 yoffset 0
    block:
        parallel:
            linear 0.05 xoffset intensity * random.uniform(-1, 1)
            linear 0.05 xoffset intensity * random.uniform(-1, 1)
            repeat
        parallel:
            linear 0.05 yoffset intensity * random.uniform(-1, 1)
            linear 0.05 yoffset intensity * random.uniform(-1, 1)
            repeat

transform no_shake:
    xoffset 0
    yoffset 0

screen strength_minigame():
    modal True
    
    default game = StrengthMinigame()
    
    timer 0.0167 repeat True action Function(game.update)
    
    frame:
        background "#222"
        xfill True
        yfill True
        at (game_shake(game.shake_intensity) if not game.game_ended else no_shake)
        
        # Character image (alternates every 5 clicks)
        if game.clicks % 10 < 5:
            add "pushup_up" xalign 0.5 yalign 0.5 at transform:
                alpha 1.0
                on show:
                    alpha 0.0
                    linear 0.1 alpha 1.0
        else:
            add "pushup_down" xalign 0.5 yalign 0.5 at transform:
                alpha 1.0
                on show:
                    alpha 0.0
                    linear 0.1 alpha 1.0
        
        # Stamina bar with modern styling
        frame:
            background "#2a2a2a"
            xsize 80
            ysize 400
            xpos 50
            yalign 0.5
            padding (10, 10)
            
            vbox:
                spacing 10
                text "STAM" size 20 color "#aaa" xalign 0.5
                
                bar:
                    value AnimatedValue(game.stamina, 100.0)
                    range 100 
                    ysize 350
                    xsize 40
                    xalign 0.5
                    left_bar "#444"
                    right_bar "#0f0"
                    bar_vertical True
                    bar_invert False
        
        # Timer and score
        frame:
            xalign 0.5
            ypos 50
            background "#2a2a2a"
            padding (20, 20)
            
            vbox:
                spacing 10
                text "Time: {:.1f}".format(max(0, game.time_remaining)) color "#fff" size 30
                text "Pushups: [game.pushups]" color "#fff" size 30
                text "Progress: {}/10".format(game.clicks % 10) color "#aaa" size 20
                text "Drain Rate: {:.1f}x".format(game.drain_multiplier) color ("#ff4444" if game.drain_multiplier > 3 else "#ffaa44" if game.drain_multiplier > 2 else "#44ff44") size 30
        
        # Click handling for the main game area
        button:
            background None
            xfill True
            yfill True
            action Function(game.handle_click)
        
        # Boost zones
        for x, y in game.boost_zones:
            frame:
                xpos x-37
                ypos y-37
                
                button:
                    xysize (75, 75)
                    background "#ffdd00"
                    hover_background "#ffee55"
                    action Function(game.activate_boost)
                    
                    text "+" size 60 color "#000" xalign 0.5 yalign 0.5
            
        # Game over screen
        if game.game_ended:
            frame:
                xalign 0.5
                yalign 0.7
                background "#000c"
                padding (20, 20)
                
                vbox:
                    spacing 20
                    text "Session Over!" size 60 xalign 0.5 color "#fff"
                    
                    if game.ended_by_stamina:
                        text "You ran out of stamina!" size 40 xalign 0.5 color "#ff4444"
                    else:
                        text "Time's up!" size 40 xalign 0.5 color "#ffaa44"
                        
                    text "Final Score: [game.pushups] pushups" size 40 xalign 0.5 color "#fff"
                    textbutton "Continue":
                        text_size 30
                        xalign 0.5
                        background "#444"
                        hover_background "#666"
                        padding (40, 20)
                        action Return([game.pushups, game.ended_by_stamina])





#hinata minigame
screen strength_minigame_hinata(character_image="hinata_squats_front"):
    modal True
    
    default game = StrengthMinigameHinata()
    default competitor_squats = 0.0
    default max_competitor_squats = renpy.random.randint(22, 29)
    
    timer 0.0167 repeat True action Function(game.update)
    # Competitor squats increase timer
    timer 0.1 repeat True action [
    SetScreenVariable('competitor_squats', min(max_competitor_squats, competitor_squats + (max_competitor_squats - competitor_squats) * 0.01)),
    Function(game.set_competitor_cap, competitor_squats)
]
    
    frame:
        background "#222"
        xfill True
        yfill True
        at (game_shake(game.shake_intensity) if not game.game_ended else no_shake)
        
        add character_image
        if game.clicks % 10 < 5:
            pass
        else:
            pass
        
        # Stamina bar
        frame:
            background "#2a2a2a"
            xsize 80
            ysize 400
            xpos 50
            yalign 0.5
            padding (10, 10)
            
            vbox:
                spacing 10
                text "STAM" size 20 color "#aaa" xalign 0.5
                
                bar:
                    value AnimatedValue(game.stamina, 100.0)
                    range 100 
                    ysize 350
                    xsize 40
                    xalign 0.5
                    left_bar "#444"
                    right_bar "#0f0"
                    bar_vertical True
                    bar_invert False
        
        # Timer, score and competitor score
        frame:
            xalign 0.5
            ypos 50
            background "#2a2a2a"
            padding (20, 20)
            
            vbox:
                spacing 10
                text "Time: {:.1f}".format(max(0, game.time_remaining)) color "#fff" size 30
                text "Your Squats: [game.pushups]" color "#fff" size 30
                text "[hin_name]: {:.0f}".format(competitor_squats) color "#A533FF" size 30
                text "Progress: {}/{}".format(game.clicks % game.clicks_per_squat, game.clicks_per_squat) color "#aaa" size 20
                text "Drain Rate: {:.1f}x".format(game.drain_multiplier) color ("#ff4444" if game.drain_multiplier > 3 else "#ffaa44" if game.drain_multiplier > 2 else "#44ff44") size 30
        
        # Click handling for the main game area
        button:
            background None
            xfill True
            yfill True
            action Function(game.handle_click)
        
        # Boost zones
        for x, y in game.boost_zones:
            frame:
                xpos x-37
                ypos y-37
                
                button:
                    xysize (75, 75)
                    background "#ffdd00"
                    hover_background "#ffee55"
                    action Function(game.activate_boost)
                    
                    text "+" size 60 color "#000" xalign 0.5 yalign 0.5
            
        # Game over screen
        if game.game_ended:
            frame:
                xalign 0.5
                yalign 0.7
                background "#000c"
                padding (20, 20)
                
                vbox:
                    spacing 20
                    text "Session Over!" size 60 xalign 0.5 color "#fff"
                    
                    if game.ended_by_stamina:
                        text "You ran out of stamina!" size 40 xalign 0.5 color "#ff4444"
                    else:
                        text "Time's up!" size 40 xalign 0.5 color "#ffaa44"
                    
                    text "Your Score: [game.pushups] squats" size 40 xalign 0.5 color "#fff"
                    text "[hin_name]'s score: {:.0f} squats".format(competitor_squats) size 40 xalign 0.5 color "#A533FF"
                    
                    if game.pushups > competitor_squats:
                        text "You won!" size 40 xalign 0.5 color "#44ff44"
                    else:
                        text "You lost!" size 40 xalign 0.5 color "#ff4444"
                        
                    textbutton "Continue":
                        text_size 30
                        xalign 0.5
                        background "#444"
                        hover_background "#666"
                        padding (40, 20)
                        action Return([game.pushups, game.ended_by_stamina, game.pushups > competitor_squats])