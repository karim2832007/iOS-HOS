default qte_round_count = 0
default qte_difficulty_level = 1
default qte_indefinite_mode = False
default qte_combat_active = False
# Combat sequences that increase in difficulty
define qte_attack_sequences = ["LLRR", "RRLL", "RLRLRL", "LRLRLR", "LLRRLL"]
define qte_defend_sequences = ["RLLL", "LRRR", "RRLLL", "LLRRR", "LLLLLL"]
default qte_defend_hp_depletion_rate = 0.0
default qte_defend_hp_restoration = 0.0
default qte_initial_player_hp = 100

label end_combat:
    hide screen qte_background
    hide screen qte_background_boruto
    hide screen qte_vfx_controller 
    hide screen qte_hp_bars
    hide screen qte_scrolling_feedback
    $ qte_vfx_list = []
    $ qte_combat_active = False
    $ qte_indefinite_mode = False
    $ qte_round_count = 0
    $ qte_difficulty_level = 1
    $ player_hp = 100
    $ enemy_hp = 100
    $ enemy_sprite_state = "smug"
    return

screen qte_hp_bars():
    zorder 50
    
    # Player HP Bar (Left side)
    frame:
        style_prefix "qte_hp"
        xpos 20
        yalign 0.08
        padding (15, 20)

        vbox:
            spacing 10
            text "PLAYER" size 20 color "#00ff41" xalign 0.5 bold True

            frame:
                padding (2, 2)
                background "#000000"
                xalign 0.5
                bar value player_hp range 100 xsize 24 ysize 400 xalign 0.5:
                    left_bar "#1a1a1a"
                    right_bar "#00ff41"
                    bar_vertical True
                    bar_invert False

            $ hp_color = "#00ff41" if player_hp > 60 else "#ffaa00" if player_hp > 30 else "#ff4444"
            text "[to_int(player_hp)]/100" size 16 xalign 0.5 color hp_color bold True

    # Enemy HP Bar (Right side)
    frame:
        style_prefix "qte_hp"
        xpos config.screen_width - 130
        yalign 0.08
        padding (15, 20)

        vbox:
            spacing 10
            text "ENEMY" size 20 color "#ff4444" xalign 0.5 bold True

            frame:
                padding (2, 2)
                background "#000000"
                xalign 0.5
                bar value enemy_hp range 100 xsize 24 ysize 400 xalign 0.5:
                    left_bar "#1a1a1a"
                    right_bar "#ff4444"
                    bar_vertical True
                    bar_invert False

            $ enemy_hp_color = "#ff4444" if enemy_hp > 60 else "#ffaa00" if enemy_hp > 30 else "#666666"
            text "[enemy_hp]/100" size 16 xalign 0.5 color enemy_hp_color bold True

default combat_outcome = ""

label qte_combat_controller(win_label="combat_victory", lose_label="combat_defeat"):
    $ qte_combat_active = True
    $ qte_indefinite_mode = True
    $ qte_vfx_counter = 0
    $ qte_round_count = 0
    $ qte_difficulty_level = 1
    $ combat_outcome = "" 
    # Show persistent HP bars and background
    show screen qte_hp_bars
    show screen qte_background
    show screen qte_vfx_controller
    
    # Combat loop
    while qte_combat_active:
        $ qte_round_count += 1
        
        # Determine mode (alternate between attack and defend)
        if qte_round_count % 2 == 1:
            $ current_mode = "attack"
        else:
            $ current_mode = "defend"
        
        # Calculate difficulty
        $ qte_difficulty_level = min((qte_round_count - 1) // 3 + 1, 5)
        
        # Set damage based on difficulty
        $ damage = 5 + (qte_difficulty_level * 4)
        
        # Set time based on difficulty (decreases as difficulty increases)
        $ time_limit = 4.0 - (qte_difficulty_level * 0.4)
        $ time_limit = max(time_limit, 1.5)  # Minimum 1.5 seconds
        
        # Choose sequence based on mode and difficulty
        if current_mode == "attack":
            $ sequence_index = min(qte_difficulty_level - 1, len(qte_attack_sequences) - 1)
            $ current_sequence = qte_attack_sequences[sequence_index]
        else:
            $ damage = damage * 1.5
            $ sequence_index = min(qte_difficulty_level - 1, len(qte_defend_sequences) - 1)
            $ current_sequence = qte_defend_sequences[sequence_index]
        
        # Special rapid fire rounds every 3th round
        if qte_round_count % 3 == 0 and current_mode == "attack":
            $ current_sequence = "spamclick"
            $ time_limit = 2.0
        
        # ADDED: Special defend spamclick rounds every 4th round
        if qte_round_count % 4 == 0 and current_mode == "defend":
            $ current_sequence = "spamclick"
            $ time_limit = 1.5  # Longer time for defense
        
        # Call QTE screen
        call screen qte_combat_indefinite(mode=current_mode, damage_taken=damage, 
                                        input_duration=time_limit, input_sequence=current_sequence)
        
        # Check for victory/defeat
        if player_hp <= 0:
            $ qte_combat_active = False
            $ combat_outcome = "defeat"
            hide screen qte_scrolling_feedback
            show screen qte_scrolling_feedback(text="DEFEAT!", color="#ff0000", with_shake=True)
            $ renpy.sound.play("audio/soun_fx/error.opus", relative_volume=3)
            pause 2.0
        elif enemy_hp <= 0:
            $ qte_combat_active = False
            $ combat_outcome = "victory"
            hide screen qte_scrolling_feedback
            show screen qte_scrolling_feedback(text="VICTORY!", color="#00ff00", with_shake=True)
            $ renpy.sound.play("audio/soun_fx/multiplier2.opus")
            pause 2.0
    
    # End combat
    call end_combat from _call_end_combat
    return combat_outcome

# QTE Combat System Variables
default player_hp = 100
default enemy_hp = 100

# QTE State Variables
default qte_active = False
default qte_time_left = 0.0
default qte_max_time = 3.0
default qte_input_sequence = ""
default qte_current_input = ""
default qte_click_count = 0
default qte_mode = "attack"
default qte_damage = 0
default qte_success = False
default qte_feedback_text = ""
default qte_feedback_color = "#ffffff"
default qte_dodge_direction = None
default qte_vfx_counter = 0
default qte_bg_shake = False
default qte_vfx_list = []
default qte_bg_xalign = 0.5
default enemy_sprite_state = "smug"

init python:
    vfx_punch_cycle = ['punch1', 'punch2', 'punch3']
    def to_int(x):
        try:
            return int(x)
        except:
            return 0
        
    def remove_vfx_from_list(vfx_data):
        global qte_vfx_list
        try:
            qte_vfx_list.remove(vfx_data)
        except ValueError:
            pass
    
    def cleanup_old_vfx():
        import time
        current_time = time.time()
        new_list = []
        for vfx in qte_vfx_list:
            created = vfx.get('time',     0)
            life    = vfx.get('lifetime', 0.4)
            if current_time - created < life:
                new_list.append(vfx)
        qte_vfx_list[:] = new_list

# Main QTE Screen
screen qte_combat(mode="attack", damage_taken=10, input_duration=3.0, input_sequence="RLR"):
    on "show" action [
        # Initialize defend spamclick variables if needed
        If(mode == "defend" and input_sequence == "spamclick",
            [
                SetVariable("qte_initial_player_hp", player_hp),
                SetVariable("qte_defend_hp_depletion_rate", damage_taken / input_duration),
                SetVariable("qte_defend_hp_restoration", 2)  # Each click restores 15% of depletion rate
            ]
        ),
        SetVariable("qte_active", True),
        SetVariable("qte_time_left", input_duration),
        SetVariable("qte_max_time", input_duration),
        SetVariable("qte_input_sequence", input_sequence),
        SetVariable("qte_current_input", ""),
        SetVariable("qte_click_count", 0),
        SetVariable("qte_mode", mode),
        SetVariable("qte_damage", damage_taken),
        SetVariable("qte_success", False),
        SetVariable("qte_feedback_text", ""),
        SetVariable("qte_feedback_color", "#ffffff"),
        SetVariable("qte_bg_shake", False),
    ]
    modal True
    
    # Player HP Bar (Left side)
    frame:
        style_prefix "qte_hp"
        xpos 20
        yalign 0.08
        padding (15, 20)

        vbox:
            spacing 10
            text "PLAYER" size 20 color "#00ff41" xalign 0.5 bold True

            frame:
                padding (2, 2)
                background "#000000"
                xalign 0.5
                bar value player_hp range 100 xsize 24 ysize 400 xalign 0.5:
                    left_bar "#1a1a1a"
                    right_bar "#00ff41"
                    bar_vertical True
                    bar_invert False

            $ hp_color = "#00ff41" if player_hp > 60 else "#ffaa00" if player_hp > 30 else "#ff4444"
            text "[to_int(player_hp)]/100" size 16 xalign 0.5 color hp_color bold True

    # Enemy HP Bar (Right side)
    frame:
        style_prefix "qte_hp"
        xpos config.screen_width - 130
        yalign 0.08
        padding (15, 20)

        vbox:
            spacing 10
            text "ENEMY" size 20 color "#ff4444" xalign 0.5 bold True

            frame:
                padding (2, 2)
                background "#000000"
                xalign 0.5
                bar value enemy_hp range 100 xsize 24 ysize 400 xalign 0.5:
                    left_bar "#1a1a1a"
                    right_bar "#ff4444"
                    bar_vertical True
                    bar_invert False

            $ enemy_hp_color = "#ff4444" if enemy_hp > 60 else "#ffaa00" if enemy_hp > 30 else "#666666"
            text "[enemy_hp]/100" size 16 xalign 0.5 color enemy_hp_color bold True

    # Main QTE UI (Bottom center)
    frame:
        style_prefix "qte"
        xalign 0.5
        ypos config.screen_height - 320
        padding (30, 20)

        vbox:
            spacing 15

            # Mode Display - Modified for defend spamclick
            if mode == "defend" and input_sequence == "spamclick":
                $ mode_text = "PARRY"
                $ mode_color = "#00aaff"
            else:
                $ mode_text = "ATTACK" if mode == "attack" else "DEFEND" if mode == "defend" else "RAPID FIRE"
                $ mode_color = "#ff6600" if mode == "attack" else "#0099ff" if mode == "defend" else "#ffaa00"

            text mode_text size 32 color mode_color xalign 0.5 bold True:
                outlines [(3, "#000000", 0, 0)]

            # Timer Bar
            $ timer_ratio = qte_time_left / qte_max_time if qte_max_time > 0 else 0
            $ timer_color = "#00ff00" if timer_ratio > 0.6 else "#ffff00" if timer_ratio > 0.3 else "#ff4444"

            frame:
                padding (2, 2)
                background "#000000"

                bar value qte_time_left range qte_max_time xsize 404 ysize 20:
                    left_bar timer_color
                    right_bar "#333333"

            text "Time: [qte_time_left:.1f]s" size 20 xalign 0.5 color "#ffffff" bold True

            # Input Display
            if input_sequence != "spamclick":
                # [Your existing L/R input display code...]
                hbox:
                    spacing 15
                    xalign 0.5

                    for i, char in enumerate(input_sequence):
                        $ input_correct = i < len(qte_current_input) and qte_current_input[i] == char
                        $ input_wrong = i < len(qte_current_input) and qte_current_input[i] != char
                        $ input_pending = i >= len(qte_current_input)

                        # Different colors for left (green) and right (red) arrows
                        if char == "L":
                            $ input_color = "#00ff00" if input_correct else ("#ff0000" if input_wrong else "#00aa00")
                            $ bg_color = "#00ff0040" if input_correct else ("#ff000060" if input_wrong else "#00000080")
                            $ border_color = "#00ff00" if input_correct else ("#ff0000" if input_wrong else "#00aa00")
                        else:  # "R"
                            $ input_color = "#00ff00" if input_correct else ("#ff0000" if input_wrong else "#ff4444")
                            $ bg_color = "#00ff0040" if input_correct else ("#ff000060" if input_wrong else "#00000080")
                            $ border_color = "#00ff00" if input_correct else ("#ff0000" if input_wrong else "#ff4444")

                        $ display_char = "←" if char == "L" else "→" if char == "R" else char

                        frame:
                            background bg_color
                            padding (15, 10)

                            frame:
                                background None
                                padding (0, 0)
                                text display_char size 30 color input_color bold True:
                                    outlines [(1, border_color, 0, 0)]

                text "Input:" size 18 xalign 0.5 color "#cccccc"
            else:
                # Spam click mode display - Modified for defend mode
                if mode == "defend":
                    frame:
                        background "#00aaff40"
                        padding (20, 15)
                        xalign 0.5
                        text "Tap to Block!" size 28 xalign 0.5 color "#00aaff" bold True:
                            outlines [(2, "#000000", 0, 0)]
                else:
                    frame:
                        background "#ffaa0040"
                        padding (20, 15)
                        xalign 0.5
                        text "Tap to Attack!" size 28 xalign 0.5 color "#ffaa00" bold True:
                            outlines [(2, "#000000", 0, 0)]

            # Feedback Text
            if qte_feedback_text and qte_active:
                text qte_feedback_text size 22 color qte_feedback_color xalign 0.5 bold True:
                    outlines [(3, "#000000", 0, 0)]

    # Mobile Touch Areas
    if renpy.variant("touch"):
        if input_sequence != "spamclick":
            # Left half of screen
            button:
                xpos 0
                ypos 0
                xsize config.screen_width // 2
                ysize config.screen_height
                background None
                action Function(qte_input_handler, "L")
                hover_background "#ffffff10"

            # Right half of screen
            button:
                xpos config.screen_width // 2
                ypos 0
                xsize config.screen_width // 2
                ysize config.screen_height
                background None
                action Function(qte_input_handler, "R")
                hover_background "#ffffff10"

            # Touch area indicators (green left, red right)
            text "←" size 100 color "#00aa0066" xpos 150 yalign 0.5:
                outlines [(2, "#00000066", 0, 0)]
            text "→" size 100 color "#ff444466" xpos config.screen_width - 250 yalign 0.5:
                outlines [(2, "#00000066", 0, 0)]

        # Full screen tap for spamclick mode
        if input_sequence == "spamclick":
            button:
                xpos 0
                ypos 0
                xsize config.screen_width
                ysize config.screen_height
                background None
                action Function(qte_input_handler, "CLICK")
                hover_background "#ffaa0010"

    # PC Controls
    if not renpy.variant("touch"):
        key "K_LEFT" action Function(qte_input_handler, "L")
        key "K_RIGHT" action Function(qte_input_handler, "R")
        key "K_a" action Function(qte_input_handler, "L")
        key "K_d" action Function(qte_input_handler, "R")

        if input_sequence == "spamclick":
            key "K_SPACE" action Function(qte_input_handler, "CLICK")
            key "mouseup_1" action Function(qte_input_handler, "CLICK")
            button:
                xpos 0
                ypos 0
                xsize config.screen_width
                ysize config.screen_height
                background None
                action Function(qte_input_handler, "CLICK")

        if input_sequence != "spamclick" and qte_active:
            text "Use ← → OR 'A' and 'D'" size 16 color "#ffffff66" xalign 0.5 ypos config.screen_height - 60:
                outlines [(1, "#00000066", 0, 0)]
        if renpy.variant("touch"):
            text "Tap Left/Right part of screen" size 16 color "#ffffff66" xalign 0.5 ypos config.screen_height - 60:
                outlines [(1, "#00000066", 0, 0)]

    # Timer updates
    if qte_active:
        timer 0.016667 repeat True action Function(qte_timer_update)

    # Auto-return timer
    if not qte_active and qte_feedback_text:
        timer 0.5 action Return()

    if enemy_sprite_state == "hitt":
        timer 0.2 action SetVariable("enemy_sprite_state", "afraid")

screen qte_enemy_reset_timer():
    timer 0.8 action SetVariable("enemy_sprite_state", "smug")

screen qte_scrolling_feedback(text, color="#ffffff", with_shake=False):
    zorder 100000
    frame:
        background None
        xalign 0.5
        yalign 0.4
        if with_shake:
            at qte_feedback_shake
        text "[text]" size 32 color color bold True at qte_scroll_text:
            outlines [(3, "#000000", 0, 0)]

define enemy_sprite = ConditionSwitch(
    "enemy_sprite_state == 'hitt'", "dm_fight1 hitt",
    "enemy_sprite_state == 'afraid'", "dm_fight1 afraidt",
    "enemy_sprite_state == 'attack'", "dm_fight1 attackt",
    "True", "dm_fight1 smugt"
)

screen qte_background():
    fixed at Position(xalign=qte_bg_xalign):
        if qte_bg_shake:
            add enemy_sprite at qte_bg_shake_transform
            timer 0.12 action SetVariable("qte_bg_shake", False)
        else:
            add enemy_sprite

screen qte_background_boruto(dodge_image):
    zorder 200
    if qte_dodge_direction:
        if qte_dodge_direction == "left":
            add dodge_image at qte_dodge_left_transform
        elif qte_dodge_direction == "right":
            add dodge_image at qte_dodge_right_transform
        timer 1.0 action SetVariable("qte_dodge_direction", None)

init python:
    sfx_channel_cycle = ["sfx1", "sfx2", "sfx3"]
    
    def qte_input_handler(input_type):
        global qte_current_input, qte_click_count, qte_feedback_text, qte_feedback_color, qte_vfx_list, enemy_sprite_state, qte_vfx_counter
        global player_hp, qte_defend_hp_restoration
        if not qte_active: return

        if qte_input_sequence == "spamclick":
            if input_type == "CLICK":
                qte_click_count += 1
                
                # Handle defend spamclick mode
                if qte_mode == "defend":
                    # Restore HP on each click
                    player_hp = min(qte_initial_player_hp, player_hp + qte_defend_hp_restoration)
                    qte_feedback_text = f"Blocked hits: {qte_click_count}"
                    qte_feedback_color = "#00aaff"
                    
                    # Play defensive sound
                    channel_index = (qte_click_count - 1) % len(sfx_channel_cycle)
                    channel_name = sfx_channel_cycle[channel_index]
                    renpy.sound.play("audio/soun_fx/select2.opus", channel="sfx3")
                    
                    # Add defensive VFX
                    vfx_index = qte_click_count % 2  # Alternate between two defensive effects
                    vfx_name = "punch1" if vfx_index == 0 else "punch2"  # You might want to use different VFX for defense
                    x_pos = renpy.random.randint(int(config.screen_width * 0.3), int(config.screen_width * 0.7))
                    y_pos = renpy.random.randint(int(config.screen_height * 0.35), int(config.screen_height * 0.65))
                    qte_vfx_counter += 1
                    import time
                    qte_vfx_list.append({
                        'name': vfx_name, 
                        'x': x_pos, 
                        'y': y_pos, 
                        'id': qte_vfx_counter,
                        'time': time.time()
                    })
                
                else:
                    # Original attack spamclick behavior
                    qte_feedback_text = f"Hits: ({qte_click_count})"
                    qte_feedback_color = "#ffff00"
                    
                    channel_index = (qte_click_count - 1) % len(sfx_channel_cycle)
                    channel_name = sfx_channel_cycle[channel_index]
                    renpy.sound.play("audio/soun_fx/punch2.opus", channel="sfx3")
                    
                    enemy_sprite_state = "hitt"
                    
                    vfx_index = (qte_click_count - 1) % len(vfx_punch_cycle)
                    vfx_name = vfx_punch_cycle[vfx_index]
                    x_pos = renpy.random.randint(int(config.screen_width * 0.3), int(config.screen_width * 0.7))
                    y_pos = renpy.random.randint(int(config.screen_height * 0.35), int(config.screen_height * 0.65))
                    qte_vfx_counter += 1
                    import time
                    qte_vfx_list.append({
                        'name': vfx_name, 
                        'x': x_pos, 
                        'y': y_pos, 
                        'id': qte_vfx_counter,
                        'time': time.time()
                    })

        else:
            # Original input handling for L/R sequences
            if input_type in ["L", "R"]:
                qte_current_input += input_type
                if len(qte_current_input) <= len(qte_input_sequence):
                    if qte_input_sequence.startswith(qte_current_input):
                        if qte_mode == "defend":
                            renpy.sound.play("audio/soun_fx/select2.opus")
                        elif qte_mode == "attack":
                            renpy.sound.play("audio/soun_fx/hand_signs.opus", relative_volume=0.6)
                        
                        qte_feedback_text = "Good!"
                        qte_feedback_color = "#00ff00"
                        
                        if qte_current_input == qte_input_sequence:
                            qte_complete_success()
                    else:
                        renpy.sound.play("audio/soun_fx/error.opus", relative_volume = 3)
                        qte_feedback_text = "Wrong input!"
                        qte_feedback_color = "#ff0000"
                        qte_complete_failure()

    # Modify the existing qte_timer_update function
    def qte_timer_update():
        global qte_time_left, qte_active, player_hp, qte_defend_hp_depletion_rate
        if not qte_active: return
        qte_time_left -= 0.016667
        
        # Handle HP depletion for defend+spamclick mode
        if qte_mode == "defend" and qte_input_sequence == "spamclick":
            player_hp -= qte_defend_hp_depletion_rate * 0.016667
            if player_hp <= 0:
                player_hp = 0
                qte_complete_defend_spamclick_failure()
                return
        
        if qte_time_left <= 0:
            qte_time_left = 0
            if qte_input_sequence == "spamclick":
                if qte_mode == "defend":
                    qte_complete_defend_spamclick_success()
                else:
                    qte_complete_spamclick()
            else:
                qte_complete_timeout()

    # Add new completion functions for defend spamclick mode
    def qte_complete_defend_spamclick_success():
        global qte_active, qte_success, qte_feedback_text, qte_feedback_color
        if not qte_active: return
        qte_active = False
        qte_success = True
        
        renpy.sound.play("audio/soun_fx/multiplier2.opus")
        renpy.sound.play("audio/soun_fx/woosh4.opus")
        
        feedback_msg = f"PERFECT DEFENSE! Survived with {int(player_hp)} HP! ({qte_click_count} blocks)"
        feedback_color = "#00aaff"
        
        renpy.hide_screen("qte_scrolling_feedback")
        renpy.show_screen("qte_scrolling_feedback", text=feedback_msg, color=feedback_color)
        qte_feedback_text = feedback_msg
        qte_feedback_color = feedback_color

    def qte_complete_defend_spamclick_failure():
        global qte_active, qte_success, qte_feedback_text, qte_feedback_color, qte_bg_shake, enemy_sprite_state, player_hp
        if not qte_active: return
        qte_active = False
        qte_success = False
        
        renpy.sound.play("audio/soun_fx/error.opus", relative_volume=3)
        renpy.sound.play("audio/soun_fx/punch.opus", relative_volume=0.6)
        
        # Apply the original damage since defense failed
        player_hp = max(0, player_hp - qte_damage)
        
        feedback_msg = f"DEFENSE FAILED! HP depleted! You take {qte_damage} damage!"
        feedback_color = "#ff0000"
        qte_bg_shake = True
        enemy_sprite_state = "attack"
        
        renpy.hide_screen("qte_scrolling_feedback")
        renpy.show_screen("qte_scrolling_feedback", text=feedback_msg, color=feedback_color)
        qte_feedback_text = feedback_msg
        qte_feedback_color = feedback_color
        
        # Show screen to reset enemy sprite
        renpy.show_screen("qte_enemy_reset_timer")

    def qte_complete_success():
        global qte_active, qte_success, enemy_hp, qte_bg_shake, qte_dodge_direction, qte_vfx_list, enemy_sprite_state, qte_vfx_counter
        if not qte_active: return
        qte_active = False
        qte_success = True

        if qte_mode == "attack":
            if qte_input_sequence != "spamclick":
                renpy.sound.play("audio/soun_fx/jutsu.opus", relative_volume=10)
                renpy.sound.play("audio/soun_fx/lightning_jutsu.opus", relative_volume=0.6, channel="sfx3")
                qte_vfx_counter += 1
                import time
                qte_vfx_list.append({
                    'name': 'lightning1', 
                    'x': int(config.screen_width / 2), 
                    'y': int(config.screen_height * 0.4),
                    'id': qte_vfx_counter,
                    'time': time.time(),
                    'lifetime':  1.4,
                })
            else:
                renpy.sound.play("audio/soun_fx/punch3.opus")
            
                qte_vfx_counter += 1
                import time
                qte_vfx_list.append({
                    'name': 'impact', 
                    'x': int(config.screen_width / 2), 
                    'y': int(config.screen_height * 0.4),
                    'id': qte_vfx_counter,
                    'time': time.time(),
                    'lifetime':  1.0,
                })
            
            enemy_hp = max(0, enemy_hp - qte_damage)
            feedback_msg = f"SUCCESS! Enemy takes {qte_damage} damage!"
            feedback_color = "#00ff00"
            qte_bg_shake = True
            enemy_sprite_state = "hitt"

        else:
            renpy.sound.play("audio/soun_fx/multiplier2.opus")
            renpy.sound.play("audio/soun_fx/woosh4.opus")
            feedback_msg = "PERFECT DEFENSE!"
            feedback_color = "#0088ff"
            enemy_sprite_state = "attack"
            last_input = qte_input_sequence[-1]
            if last_input == 'L': qte_dodge_direction = "left"
            elif last_input == 'R': qte_dodge_direction = "right"

        renpy.hide_screen("qte_scrolling_feedback")
        renpy.show_screen("qte_scrolling_feedback", text=feedback_msg, color=feedback_color)

    def qte_complete_failure():
        global qte_active, qte_success, player_hp, qte_bg_shake, enemy_sprite_state
        if not qte_active: return
        qte_active = False
        qte_success = False
        
        if qte_mode == "defend":
            renpy.sound.play("audio/soun_fx/punch.opus", relative_volume = 0.6)
            player_hp = max(0, player_hp - qte_damage)
            feedback_msg = f"FAILED! You take {qte_damage} damage!"
            feedback_color = "#ff0000"
            qte_bg_shake = True
            enemy_sprite_state = "attack"
            # Show screen to reset enemy sprite
            renpy.show_screen("qte_enemy_reset_timer")
        else:
            renpy.sound.play("audio/soun_fx/error.opus", relative_volume = 3)
            feedback_msg = "Attack missed!"
            feedback_color = "#ff8800"
        
        renpy.hide_screen("qte_scrolling_feedback")
        renpy.show_screen("qte_scrolling_feedback", text=feedback_msg, color=feedback_color)
    
    def qte_complete_timeout():
        global qte_active, qte_success, player_hp, qte_feedback_text, qte_feedback_color, qte_bg_shake, enemy_sprite_state
        if not qte_active: return
        qte_active = False
        qte_success = False
        renpy.sound.play("audio/soun_fx/error.opus", relative_volume = 3)
        
        if qte_mode == "defend":
            renpy.sound.play("audio/soun_fx/punch.opus", relative_volume = 0.6)
            player_hp = max(0, player_hp - qte_damage)
            feedback_msg = f"TOO SLOW! You take {qte_damage} damage!"
            feedback_color = "#ff0000"
            qte_bg_shake = True
            enemy_sprite_state = "attack"
            # Show screen to reset enemy sprite
            renpy.show_screen("qte_enemy_reset_timer")
        else:
            feedback_msg = "TOO SLOW! Attack missed!"
            feedback_color = "#ff8800"
        
        renpy.hide_screen("qte_scrolling_feedback")
        renpy.show_screen("qte_scrolling_feedback", text=feedback_msg, color=feedback_color)
        qte_feedback_text = feedback_msg
        qte_feedback_color = feedback_color

    def qte_complete_spamclick():
        global qte_active, qte_success, enemy_hp, qte_feedback_text, qte_feedback_color, qte_bg_shake
        if not qte_active: return
        qte_active = False
        qte_success = True
        renpy.sound.play("audio/soun_fx/punch3.opus")

        damage_dealt = qte_click_count * 2
        enemy_hp = max(0, enemy_hp - damage_dealt)
        feedback_msg = f"DEALT {damage_dealt} DAMAGE! (x{qte_click_count} hits)"
        feedback_color = "#ffaa00"
        qte_bg_shake = True
        renpy.hide_screen("qte_scrolling_feedback")
        renpy.show_screen("qte_scrolling_feedback", text=feedback_msg, color=feedback_color)
        qte_feedback_text = feedback_msg
        qte_feedback_color = feedback_color

screen qte_vfx_controller():
    zorder 300
    
    # Single repeating timer to clean up old VFX
    timer 0.05 repeat True action Function(cleanup_old_vfx)

    $ vfx_list_copy = list(qte_vfx_list)

    for vfx_data in vfx_list_copy:
        $ image_to_show = vfx_data['name']
        $ image_alias = "vfx_{}_{}".format(vfx_data['name'], vfx_data['id'])

        add image_to_show as image_alias at qte_vfx_popup_and_fade, Position(
            xpos=vfx_data['x'], 
            ypos=vfx_data['y'], 
            xanchor=0.5, 
            yanchor=0.5
        )


screen qte_combat_indefinite(mode="attack", damage_taken=10, input_duration=3.0, input_sequence="RLR"):
    on "show" action [
        # Initialize defend spamclick variables if needed
        If(mode == "defend" and input_sequence == "spamclick",
            [
                SetVariable("qte_initial_player_hp", player_hp),
                SetVariable("qte_defend_hp_depletion_rate", damage_taken / input_duration),
                SetVariable("qte_defend_hp_restoration", damage_taken * 0.05)  # Each click restores 15% of depletion rate
            ]
        ),
        SetVariable("qte_active", True),
        SetVariable("qte_time_left", input_duration),
        SetVariable("qte_max_time", input_duration),
        SetVariable("qte_input_sequence", input_sequence),
        SetVariable("qte_current_input", ""),
        SetVariable("qte_click_count", 0),
        SetVariable("qte_mode", mode),
        SetVariable("qte_damage", damage_taken),
        SetVariable("qte_success", False),
        SetVariable("qte_feedback_text", ""),
        SetVariable("qte_feedback_color", "#ffffff"),
        SetVariable("qte_bg_shake", False),
    ]
    modal True
    
    # Main QTE UI (Bottom center)
    frame:
        style_prefix "qte"
        xalign 0.5
        ypos config.screen_height - 320
        padding (30, 20)

        vbox:
            spacing 15

            # Mode Display - Modified for defend spamclick
            if mode == "defend" and input_sequence == "spamclick":
                $ mode_text = "PARRY"
                $ mode_color = "#00aaff"
            else:
                $ mode_text = "ATTACK" if mode == "attack" else "DEFEND" if mode == "defend" else "RAPID FIRE"
                $ mode_color = "#ff6600" if mode == "attack" else "#0099ff" if mode == "defend" else "#ffaa00"

            text mode_text size 32 color mode_color xalign 0.5 bold True:
                outlines [(3, "#000000", 0, 0)]

            # Timer Bar
            $ timer_ratio = qte_time_left / qte_max_time if qte_max_time > 0 else 0
            $ timer_color = "#00ff00" if timer_ratio > 0.6 else "#ffff00" if timer_ratio > 0.3 else "#ff4444"

            frame:
                padding (2, 2)
                background "#000000"

                bar value qte_time_left range qte_max_time xsize 404 ysize 20:
                    left_bar timer_color
                    right_bar "#333333"

            text "Time: [qte_time_left:.1f]s" size 20 xalign 0.5 color "#ffffff" bold True

            # Input Display
            if input_sequence != "spamclick":
                hbox:
                    spacing 15
                    xalign 0.5

                    for i, char in enumerate(input_sequence):
                        $ input_correct = i < len(qte_current_input) and qte_current_input[i] == char
                        $ input_wrong = i < len(qte_current_input) and qte_current_input[i] != char
                        $ input_pending = i >= len(qte_current_input)

                        # Different colors for left (green) and right (red) arrows
                        if char == "L":
                            $ input_color = "#00ff00" if input_correct else ("#ff0000" if input_wrong else "#00aa00")
                            $ bg_color = "#00ff0040" if input_correct else ("#ff000060" if input_wrong else "#00000080")
                            $ border_color = "#00ff00" if input_correct else ("#ff0000" if input_wrong else "#00aa00")
                        else:  # "R"
                            $ input_color = "#00ff00" if input_correct else ("#ff0000" if input_wrong else "#ff4444")
                            $ bg_color = "#00ff0040" if input_correct else ("#ff000060" if input_wrong else "#00000080")
                            $ border_color = "#00ff00" if input_correct else ("#ff0000" if input_wrong else "#ff4444")

                        $ display_char = "←" if char == "L" else "→" if char == "R" else char

                        frame:
                            background bg_color
                            padding (15, 10)

                            frame:
                                background None
                                padding (0, 0)
                                text display_char size 30 color input_color bold True:
                                    outlines [(1, border_color, 0, 0)]

                $ display_input = ""
                for c in qte_current_input:
                    $ display_input += "←" if c == "L" else "→" if c == "R" else c

                text "Input:" size 18 xalign 0.5 color "#cccccc"
            else:
                # Spam click mode display - Modified for defend mode
                if mode == "defend":
                    frame:
                        background "#00aaff40"
                        padding (20, 15)
                        xalign 0.5
                        text "Tap to Block!" size 28 xalign 0.5 color "#00aaff" bold True:
                            outlines [(2, "#000000", 0, 0)]
                else:
                    frame:
                        background "#ffaa0040"
                        padding (20, 15)
                        xalign 0.5
                        text "Tap to Attack!" size 28 xalign 0.5 color "#ffaa00" bold True:
                            outlines [(2, "#000000", 0, 0)]

            # Feedback Text
            if qte_feedback_text and qte_active:
                text qte_feedback_text size 22 color qte_feedback_color xalign 0.5 bold True:
                    outlines [(3, "#000000", 0, 0)]

    # Mobile Touch Areas
    if renpy.variant("touch"):
        if input_sequence != "spamclick":
            # Left half of screen
            button:
                xpos 0
                ypos 0
                xsize config.screen_width // 2
                ysize config.screen_height
                background None
                action Function(qte_input_handler, "L")
                hover_background "#ffffff10"

            # Right half of screen
            button:
                xpos config.screen_width // 2
                ypos 0
                xsize config.screen_width // 2
                ysize config.screen_height
                background None
                action Function(qte_input_handler, "R")
                hover_background "#ffffff10"

            # Touch area indicators (green left, red right)
            text "←" size 100 color "#00aa0066" xpos 150 yalign 0.5:
                outlines [(2, "#00000066", 0, 0)]
            text "→" size 100 color "#ff444466" xpos config.screen_width - 250 yalign 0.5:
                outlines [(2, "#00000066", 0, 0)]

        # Full screen tap for spamclick mode
        if input_sequence == "spamclick":
            button:
                xpos 0
                ypos 0
                xsize config.screen_width
                ysize config.screen_height
                background None
                action Function(qte_input_handler, "CLICK")
                hover_background "#ffaa0010"

    # PC Controls
    if not renpy.variant("touch"):
        key "K_LEFT" action Function(qte_input_handler, "L")
        key "K_RIGHT" action Function(qte_input_handler, "R")
        key "K_a" action Function(qte_input_handler, "L")
        key "K_d" action Function(qte_input_handler, "R")

        if input_sequence == "spamclick":
            key "K_SPACE" action Function(qte_input_handler, "CLICK")
            key "mouseup_1" action Function(qte_input_handler, "CLICK")
            button:
                xpos 0
                ypos 0
                xsize config.screen_width
                ysize config.screen_height
                background None
                action Function(qte_input_handler, "CLICK")

        if input_sequence != "spamclick" and qte_active:
            text "Use ← → OR 'A' and 'D'" size 16 color "#ffffff66" xalign 0.5 ypos config.screen_height - 60:
                outlines [(1, "#00000066", 0, 0)]
        if renpy.variant("touch"):
            text "Tap Left/Right part of screen" size 16 color "#ffffff66" xalign 0.5 ypos config.screen_height - 60:
                outlines [(1, "#00000066", 0, 0)]

    # Timer updates
    if qte_active:
        timer 0.016667 repeat True action Function(qte_timer_update)

    # Auto-return timer
    if not qte_active and qte_feedback_text:
        timer 0.5 action Return()

    if enemy_sprite_state == "hitt":
        timer 0.2 action SetVariable("enemy_sprite_state", "afraid")

transform qte_vfx_popup_and_fade:
    alpha 1.0
    zoom 1.0
    easein 0.3 zoom 1.1
    pause 0.1
    easeout 0.3 alpha 0.0

transform qte_scroll_text:
    yalign 0.4 xalign 0.5
    alpha 0
    parallel:
        ease 0.3 alpha 1
        pause 1.0
        ease 0.8 alpha 0
    parallel:
        subpixel True
        ease 0.1 ypos 0.35
        linear 1.8 ypos 0.0

transform qte_feedback_shake:
    parallel:
        xoffset 0
        linear 0.02 xoffset -6
        linear 0.02 xoffset 6
        linear 0.02 xoffset -4
        linear 0.02 xoffset 4
        linear 0.02 xoffset -2
        linear 0.02 xoffset 0
    parallel:
        yoffset 0
        linear 0.02 yoffset -3
        linear 0.02 yoffset 3
        linear 0.02 yoffset -2
        linear 0.02 yoffset 2
        linear 0.02 yoffset 0

transform qte_bg_shake_transform:
    xoffset 0 yoffset 0
    linear 0.02 xoffset -10 yoffset -4
    linear 0.02 xoffset 10 yoffset 4
    linear 0.02 xoffset -6 yoffset 3
    linear 0.02 xoffset 6 yoffset -3
    linear 0.02 xoffset -3 yoffset 1
    linear 0.02 xoffset 0 yoffset 0

transform qte_dodge_left_transform:
    xalign 0.5 yalign 0.5
    alpha 0.0
    parallel:
        ease 0.2 alpha 1.0
        pause 0.5
        ease 0.3 alpha 0.0
    parallel:
        subpixel True
        ease 0.4 xoffset -400

transform qte_dodge_right_transform:
    xzoom -1 xalign 0.5 yalign 0.5
    alpha 0.0
    parallel:
        ease 0.2 alpha 1.0
        pause 0.5
        ease 0.3 alpha 0.0
    parallel:
        subpixel True
        ease 0.4 xoffset 400

style qte_hp_frame:
    background "#222222ee"
style qte_frame:
    background "#222222ee"
style qte_vbox:
    spacing 15
style qte_text:
    color "#ffffff"
    outlines [(2, "#000000", 0, 0)]