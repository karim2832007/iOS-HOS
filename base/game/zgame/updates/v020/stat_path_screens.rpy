# ##############################################################################
#
#                               Split-Choice Screen
#
# A robust, two-option choice screen designed for major story decisions.
#
# Features:
# - Full-pane background animations on mouse hover.
# - Dynamic display of path requirements (e.g., quests completed).
# - A popup screen for detailing unmet requirements.
# - Flawless rollback behavior; the entire choice interaction is treated as
#   a single, undoable step, ensuring a clean user experience.
#
# ##############################################################################

# -- Section 0: Setup and Definitions --
# Defines colors, helper functions, and other initial configuration.

define lovecolor_splitchoice = "#ff69b4"
define hatredcolor_splitchoice = "#dc143c"
define reqs_met_color = "#32cd32"      # Lime green for met requirements.
define reqs_not_met_color = "#ff4500"  # Orangey-red for unmet requirements.
default chosen_love_path = False
default chosen_hate_path = False

init python:
    import re

    def analyze_quests_for_path(quest_definitions, manager, path_identifier):
        """Analyzes a list of quests to determine progress on a specific path."""
        total_in_path = 0
        completed_count = 0
        incomplete_quests = []
        for quest_item in quest_definitions:
            quest_id = quest_item.id
            if path_identifier in quest_id:
                
                # --- THIS IS THE FIX ---
                # Only consider quests that are actually implemented.
                if manager.is_implemented(quest_id):
                    
                    # 1. This quest is now counted towards the total number of requirements.
                    total_in_path += 1
                    
                    # 2. Now check if this implemented quest has been completed.
                    if manager.exists(quest_id) and \
                    (manager.is_state(quest_id, "done") or manager.is_state(quest_id, "completed")):
                        completed_count += 1
                    else:
                        # 3. If it's implemented but not complete, add it to the list for the popup.
                        incomplete_quests.append(quest_item)
                
                # If a quest is NOT implemented (is_implemented is False), we simply do nothing.
                # It's skipped entirely, solving both problems at once.

        return {"total": total_in_path, "completed": completed_count, "incomplete": incomplete_quests}

    def colorize_path_words(input_string):
        """Scans a string and wraps 'love' and 'hatred' with color tags."""
        if not isinstance(input_string, str):
            return input_string
        s = re.sub(r'love', lambda m: f"{{color={lovecolor}}}{m.group(0)}{{/color}}", input_string, flags=re.IGNORECASE)
        s = re.sub(r'hatred', lambda m: f"{{color={hatredcolor}}}{m.group(0)}{{/color}}", s, flags=re.IGNORECASE)
        return s
    renpy.pure(colorize_path_words)

    # MODIFIED: This function is renamed and no longer calls a new context.
    # It now prepares and returns the data needed for the requirements popup screen.
    def prepare_path_failure_data(path_id, all_quest_definitions, quest_hin, quest_him, hinata1, incomplete_quests):
        renpy.sound.play("audio/soun_fx/attributeslost.opus")

        all_quests_with_state = []

        # Check for completed quests first.
        for quest_template in all_quest_definitions:
            if path_id in quest_template.id:
                manager = quest_hin if quest_template in hinata1 else quest_him
                if manager.is_state(quest_template.id, "done") or manager.is_state(quest_template.id, "completed"):
                    all_quests_with_state.append((quest_template, "completed"))

        # Then, add the already-identified incomplete quests.
        for quest_template in incomplete_quests:
            manager = quest_hin if quest_template in hinata1 else quest_him
            state = "in progress" if manager.exists(quest_template.id) and not manager.is_state(quest_template.id, "pending") else "pending"
            all_quests_with_state.append((quest_template, state))

        all_quests_with_state.sort(key=lambda item: {"completed": 0, "in progress": 1, "pending": 2}[item[1]])
        
        # It now returns the data instead of calling a new context.
        return all_quests_with_state

# -- Section 1: Image and Video Definitions --
# Defines all static and animated visual assets used by the screen.

image split_choice_bg:
    # The static background image.
    "images/randomshit/kushina_dream_kurama_1.png"
    pos (0.491, 0.5)
    anchor (0.5, 0.5)
    zoom 1.02
    yalign 0.7

image hatred_eye:
    # Animated aura overlay for the 'hatred' path hover effect.
    Movie(play="images/video/split_screen/red_aura_transparent.webm", mask="images/video/split_screen/red_aura_transparent_mask.webm", loop=True, size=(400, 250))
    pos (690, 144)
    anchor (0.5, 0.5)
    xzoom 0.49
    yzoom 0.6
    rotate 45

image love_eye:
    # Animated aura overlay for the 'love' path hover effect.
    Movie(play="images/video/split_screen/violet_aura_transparent.webm", mask="images/video/split_screen/violet_aura_transparent_mask.webm", loop=True, size=(400, 250))
    pos (595, 144)
    anchor (0.5, 0.5)
    xzoom 0.49
    yzoom 0.6
    rotate -45

image falling_embers:
    # Looping particle effect shown over the background during hover.
    Movie(play="images/video/split_screen/falling_embers_960x540.webm", mask="images/video/split_screen/falling_embers_960x540_mask.webm", loop=True, size=(1280, 720))

image split_choice_hatred_hover:
    # Composite image combining the background and the hatred aura.
    contains:
        "split_choice_bg"
    contains:
        "hatred_eye"

image split_choice_love_hover:
    # Composite image combining the background and the love aura.
    contains:
        "split_choice_bg"
    contains:
        "love_eye"

image hover_glow:
    # A subtle glow effect for the hovered pane.
    "images/randomshit/hover_glow_effect.png"
    alpha 0.5


# -- Section 2: Animation Transforms --
# Defines ATL transforms for animations and transitions.

transform choice_bg_zoom_idle:
    # The default, non-hovered state for the background.
    pass

transform choice_bg_zoom_right:
    # Zooms and pans the background when the right pane is hovered.
    subpixel True
    pos (0.0, 0.5)
    anchor (0.0, 0.5)
    easeout 0.5 zoom 1.05

transform choice_bg_zoom_left:
    # Zooms and pans the background when the left pane is hovered.
    subpixel True
    pos (1.0, 0.5)
    anchor (1.0, 0.5)
    easeout 0.5 zoom 1.05

transform choice_glow_fade_in:
    # Fades in the hover glow effect.
    easein 0.4 alpha 0.5

transform glow_pulse:
    # A pulsing animation for the central divider.
    alpha 0.6
    linear 1.5 alpha 1.0
    linear 1.5 alpha 0.6
    repeat


# -- Section 3: Style Definitions --
# Defines all SL styles for screen elements.

style split_choice_info_text:
    xalign 0.5
    yalign 0.5
    text_align 0.5
    size 18
    color "#cccccc"
    outlines [ (2, "#00000099", 0, 0) ]
    xminimum 380

style split_choice_reqs_text is split_choice_info_text:
    # Style for the "X/Y requirements met" text.
    top_margin 10

style split_choice_reqs_details_text is split_choice_info_text:
    # A smaller, italicized style for the "Click to see details" hint.
    size 16
    italic True
    color "#dddddd"
    top_margin -10

style split_choice_inner_frame is button:
    # The main container frame for each choice's text content.
    pos (0.5, 0.5)
    anchor (0.5, 0.5)
    xsize 450
    padding (25, 25)
    background Solid("#000000aa")
    hover_background Solid("#000000aa")

style split_choice_caption_base:
    # Base style for the main choice captions ("Love", "Hatred").
    xalign 0.5
    xfill True
    top_padding 20
    bottom_padding 20
    size 28
    bold True
    text_align 0.5
    color "#ffffff"
    outlines [ (5, "#000000cc", 0, 0), (2, "#000000", 0, 0) ]

style love_caption_text is split_choice_caption_base:
    hover_color lovecolor_splitchoice

style hatred_caption_text is split_choice_caption_base:
    hover_color hatredcolor_splitchoice


# -- Section 4: Screen Definitions --

screen split_choice(left_caption, right_caption, left_completed, left_required, right_completed, right_required, crossfade_intro=False):

### The main split choice screen interface.
### Accepts path data and presents the two-option choice. Returns the chosen
### path identifier ("love" or "hatred") when a button is clicked.

    modal True

    # If coming from the intro, start with interaction disabled.
    default interaction_enabled = not crossfade_intro
    # This flag will be used to trigger the one-time timer.
    default timer_activated = False

    # If this is the first call after the intro, handle the crossfade
    # and set the flag to activate the timer statement.
    if crossfade_intro:
        on "show" action [
            Hide("split_choice_intro_overlay", transition=Dissolve(0.5)),
            SetScreenVariable("timer_activated", True)
        ]

    # This timer statement is now used instead of the Timer() action.
    # It only runs when timer_activated is True.
    if timer_activated:
        timer 0.3 action [
            # Enable interaction.
            SetScreenVariable("interaction_enabled", True),
            # Disable this timer so it doesn't run again.
            SetScreenVariable("timer_activated", False)
            ]

    default left_hovered = False
    default right_hovered = False
    # This flag tracks if the player has hovered over a choice yet.
    default has_interacted_with_choice = False

    # Dynamically adds the correct background based on hover state.
    if left_hovered:
        add "split_choice_love_hover" at choice_bg_zoom_left
        add "falling_embers"
    elif right_hovered:
        add "split_choice_hatred_hover" at choice_bg_zoom_right
        add "falling_embers"
    else:
        add "split_choice_bg" at choice_bg_zoom_idle
        add "falling_embers"

    fixed:
        # -- Left Choice Pane --
        frame:
            xsize 0.5
            yfill True
            background None
            padding (0, 0)
            margin (0, 0)

            if left_hovered:
                add "hover_glow" at choice_glow_fade_in

            # The action is None until interaction is enabled.
            button action (Return("love") if interaction_enabled else None) style "split_choice_inner_frame" hover_sound ("audio/soun_fx/select2.opus" if interaction_enabled else None):
                vbox:
                    xfill True
                    spacing 15
                    text left_caption style "love_caption_text"
                    text "Path of Empathy and Connection.\nForge bonds that transcend conflict." style "split_choice_info_text"
                    if left_completed >= left_required:
                        text ("{color=[reqs_met_color]}[left_completed]/[left_required]{/color} requirements met.") style "split_choice_reqs_text"
                    else:
                        text ("{color=[reqs_not_met_color]}[left_completed]/[left_required]{/color} requirements met.") style "split_choice_reqs_text"
                        text "Click to see details!" style "split_choice_reqs_details_text"

            # A full-pane mousearea allows the hover effect to trigger
            # anywhere on the left half of the screen.
            mousearea:
                xfill True
                yfill True
                # Hover actions are disabled until interaction is enabled.
                hovered ([SetScreenVariable("left_hovered", True), Play("sound", "audio/soun_fx/growl2.opus"), SetScreenVariable("has_interacted_with_choice", True)] if interaction_enabled else [])
                unhovered (SetScreenVariable("left_hovered", False) if interaction_enabled else None)

        # -- Right Choice Pane --
        frame:
            xpos 640 # Start of the right half (1280 / 2)
            xsize 0.5
            yfill True
            background None
            padding (0, 0)
            margin (0, 0)
            
            if right_hovered:
                add "hover_glow" at choice_glow_fade_in

            # The action is None until interaction is enabled.
            button action (Return("hatred") if interaction_enabled else None) style "split_choice_inner_frame" hover_sound ("audio/soun_fx/select2.opus" if interaction_enabled else None):
                vbox:
                    xfill True
                    spacing 15
                    text right_caption style "hatred_caption_text"
                    text "Path of Power and Domination.\nSeize control and shape destiny." style "split_choice_info_text"
                    if right_completed >= right_required:
                        text ("{color=[reqs_met_color]}[right_completed]/[right_required]{/color} requirements met.") style "split_choice_reqs_text"
                    else:
                        text ("{color=[reqs_not_met_color]}[right_completed]/[right_required]{/color} requirements met.") style "split_choice_reqs_text"
                        text "Click to see details!" style "split_choice_reqs_details_text"

            mousearea:
                xfill True
                yfill True
                # Hover actions are disabled until interaction is enabled.
                hovered ([SetScreenVariable("right_hovered", True), Play("sound", "audio/soun_fx/growl2.opus"), SetScreenVariable("has_interacted_with_choice", True)] if interaction_enabled else [])
                unhovered (SetScreenVariable("right_hovered", False) if interaction_enabled else None)

    # ### CHANGE: The vbar element for the central divider has been removed. ###
    #
    # The central, pulsing divider line.
    # vbar:
    #     xalign 0.5
    #     yfill True
    #     xsize 4
    #     base_bar Solid("#fff")
    #     at glow_pulse

    # This button only appears after the player has hovered over at least one choice.
    # if has_interacted_with_choice:
    imagebutton:
        xalign 0.95 yalign 0.05
        auto "images/ui/return_button_%s.png"
        hovered Show("displayTextScreen", displayText = "Return")
        unhovered [Hide("displayTextScreen")]
        # CORRECTED ACTION: Return a value that the new label loop can process.
        action [
            Hide("displayTextScreen"), 
            Return("cancel")
        ]
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"


# NEW SCREEN: A non-interactive overlay for the intro sequence.
screen split_choice_intro_overlay():
    zorder 1 # Ensure it draws on top of the background.

    # The ashes/embers effect, matching the main screen.
    add "falling_embers"

    fixed:
        # -- Left Pane (Static Visual Only) --
        frame:
            xsize 0.5
            yfill True
            background None
            frame style "split_choice_inner_frame":
                vbox:
                    xfill True
                    spacing 15
                    text "Love" style "love_caption_text"
                    text "Path of Empathy and Connection.\nForge bonds that transcend conflict." style "split_choice_info_text"
                    # Add empty text placeholders to perfectly match the main screen's layout.
                    text "" style "split_choice_reqs_text"
                    text "" style "split_choice_reqs_details_text"

        # -- Right Pane (Static Visual Only) --
        frame:
            xpos 640
            xsize 0.5
            yfill True
            background None
            frame style "split_choice_inner_frame":
                vbox:
                    xfill True
                    spacing 15
                    text "Hatred" style "hatred_caption_text"
                    text "Path of Power and Domination.\nSeize control and shape destiny." style "split_choice_info_text"
                    # Add empty text placeholders to perfectly match the main screen's layout.
                    text "" style "split_choice_reqs_text"
                    text "" style "split_choice_reqs_details_text"

    # ### CHANGE: The vbar element for the central divider has been removed. ###
    #
    # The central, pulsing divider line.
    # vbar:
    #     xalign 0.5
    #     yfill True
    #     xsize 4
    #     base_bar Solid("#fff")
    #     at glow_pulse

# -- Section 5: Script Logic --
# Contains the main game logic for presenting and handling the choice.

#TODO Remove test labels and call the screen's label properly from the correct entrypoint in the game
# A test label for quickly demonstrating the screen with unmet requirements.
label start_screen_test:
    $ quest_hin.load(hinata1)
    $ quest_him.load(himawari1)
    $ quest_hin.check("hin1L_1", "done")
    $ quest_hin.check("hin1L_2", "done")
    $ quest_him.check("him1L_1", "done")
    dev"Split screen test sequence initiated (some quests have been marked completed for testing)"
    jump v20_show_split_choice

# A test label for demonstrating the screen with all requirements met.
label start_screen_test_completed:
    $ quest_hin.load(hinata1)
    $ quest_him.load(himawari1)
    python:
        # Using a non-colliding variable name 'quest_item' to prevent
        # overwriting a global 'quest' variable, which is used elsewhere.
        for quest_item in hinata1: quest_hin.check(quest_item.id, "done")
        for quest_item in himawari1: quest_him.check(quest_item.id, "done")
    dev"Split screen test sequence initiated (all quests have been marked completed for testing)"
    jump v20_show_split_choice

# REMOVED: The wrapper label is no longer needed as renpy.call_in_new_context is gone.

#TODO Fix the dialogue leading up to the screen. Decide if the "intro" sequence will be shown only once or every time this label is called
label v20_show_split_choice:
    call hideUI from _call_hideUI_65
    
    # This flag will tell the python block whether the intro screen is showing.
    $ intro_was_shown = False

    # Step 1: Show the Kurama background and play the growl.
    show split_choice_bg with dissolve:
        yalign 0.0 subpixel True
    $ renpy.sound.play("/audio/soun_fx/growl3.opus", channel="sfx1", loop=False, relative_volume = 1.5)
    show split_choice_bg at shake:
        easein 3 yalign 0.7

    $ renpy.pause(3, hard=True)

    # Step 2: Show the divider, buttons, and ashes all at once.
    show screen split_choice_intro_overlay with Dissolve(0.75)

    $ renpy.pause(0.5, hard=True)

    # The intro is complete. Flag it as seen and re-enable input.
    $ love_hate_screen_seen = True
    $ intro_was_shown = True

    # Step 3: Pre-calculate all path requirements ONCE to be efficient.
    python:
        # Love Path Analysis
        love_hinata_data = analyze_quests_for_path(hinata1, quest_hin, "L")
        love_himawari_data = analyze_quests_for_path(himawari1, quest_him, "L")
        love_total_defined = love_hinata_data["total"] + love_himawari_data["total"]
        love_total_completed = love_hinata_data["completed"] + love_himawari_data["completed"]
        quests_leeway = 3
        love_quests_required = love_total_defined - quests_leeway
        love_incomplete_quests = love_hinata_data["incomplete"] + love_himawari_data["incomplete"]

        # Hatred Path Analysis
        hatred_hinata_data = analyze_quests_for_path(hinata1, quest_hin, "H")
        hatred_himawari_data = analyze_quests_for_path(himawari1, quest_him, "H")
        hatred_total_defined = hatred_hinata_data["total"] + hatred_himawari_data["total"]
        hatred_total_completed = hatred_hinata_data["completed"] + hatred_himawari_data["completed"]
        hatred_quests_required = hatred_total_defined - quests_leeway
        hatred_incomplete_quests = hatred_hinata_data["incomplete"] + hatred_himawari_data["incomplete"]
        
        all_quest_definitions = hinata1 + himawari1

    # -- NEW: Stable Ren'Py Label Loop --
    # This replaces the entire unstable python while-loop block.
label v20_choice_loop:
    # Call the choice screen. The first time, intro_was_shown is True.
    call screen split_choice(
        left_caption="Love",
        right_caption="Hatred",
        left_completed=love_total_completed, left_required=love_quests_required,
        right_completed=hatred_total_completed, right_required=hatred_quests_required,
        crossfade_intro=intro_was_shown
        )

    # After the first loop, the intro animation is finished, so we set this to False.
    $ intro_was_shown = False

    $ choice = _return

    if choice == "love":
        if love_total_completed >= love_quests_required:
            $ renpy.sound.play("audio/soun_fx/dramatic_choice_effect.opus")
            jump love_path_success_transition
        else:
            # Player fails requirements. Prepare data for the popup...
            $ quests_for_popup = prepare_path_failure_data("L", all_quest_definitions, quest_hin, quest_him, hinata1, love_incomplete_quests)
            # ...and call the popup screen normally.
            call screen path_requirements_screen(
                path_title="Love",
                path_description="...",
                completed_count=love_total_completed,
                required_count=love_quests_required,
                missing_count=love_quests_required - love_total_completed,
                all_quests_with_state=quests_for_popup
                )
            # After the popup is closed, loop back to the choice screen.
            jump v20_choice_loop

    elif choice == "hatred":
        if hatred_total_completed >= hatred_quests_required:
            $ renpy.sound.play("audio/soun_fx/dramatic_choice_effect.opus")
            jump hatred_path_success_transition
        else:
            # Player fails requirements. Prepare data for the popup...
            $ quests_for_popup = prepare_path_failure_data("H", all_quest_definitions, quest_hin, quest_him, hinata1, hatred_incomplete_quests)
            # ...and call the popup screen normally.
            call screen path_requirements_screen(
                path_title="Hatred",
                path_description="...",
                completed_count=hatred_total_completed,
                required_count=hatred_quests_required,
                missing_count=hatred_quests_required - hatred_total_completed,
                all_quests_with_state=quests_for_popup
                )
            # After the popup is closed, loop back to the choice screen.
            jump v20_choice_loop

    elif choice == "cancel":
        # The player clicked the return button.
        jump temporary_v20_choice