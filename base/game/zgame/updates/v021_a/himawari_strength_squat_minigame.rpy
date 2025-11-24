init python:
    class StrengthMinigameHimawari():
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

screen strength_minigame_himawari(character_image="himawari_squats_front"):
    modal True
    
    default game = StrengthMinigameHimawari()
    default competitor_squats = 0.0
    default max_competitor_squats = renpy.random.randint(22, 29)
    
    timer 0.0167 repeat True action Function(game.update)
    # Competitor squats increase timer
    timer 0.1 repeat True action [
    SetScreenVariable('competitor_squats', min(max_competitor_squats, competitor_squats + (max_competitor_squats - competitor_squats) * 0.01)),
    Function(game.set_competitor_cap, competitor_squats)
]
    
    # This main frame will serve as our black background and handle the screen shake
    frame:
        background "#000" # Changed to solid black for the letterbox effect
        xfill True
        yfill True
        at (game_shake(game.shake_intensity) if not game.game_ended else no_shake)
        
        # Add the character animation, scaled to fit the screen height
        add character_image:
            xysize (1280, 720)
            fit "contain"
            xalign 0.5
            yalign 0.5
        
        # The rest of the UI elements are layered on top of the background and character
        
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
            yalign 0.5
            xalign 0.99
            background "#2a2a2a"
            padding (20, 20)
            
            vbox:
                spacing 10
                text "Time: {:.1f}".format(max(0, game.time_remaining)) color "#fff" size 30
                text "Your Squats: [game.pushups]" color "#fff" size 30
                text "[him_name]: {:.0f}".format(competitor_squats) color "#A533FF" size 30
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
                    text "[him_name]'s score: {:.0f} squats".format(competitor_squats) size 40 xalign 0.5 color "#A533FF"
                    
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