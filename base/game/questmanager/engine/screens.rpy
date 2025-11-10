default journal_left_page_adjustment = ui.adjustment()
default journal_right_page_adjustment = ui.adjustment()

# Function to disable rollback
init python:
    def disable_rollback():
        config.rollback_enabled = False

# Function to enable rollback
    def enable_rollback():
        config.rollback_enabled = True

## --- MODIFIED: Legend implemented exactly as requested ---
screen quest_legend():
    vbox:
        xoffset -10
        yoffset 30
        text _("") style "category_style" size 24 xalign 0.0
        null height 5

        # --- REORDERED AND MODIFIED LEGEND ---

        # 1. In Progress (Static - NOT a filter)
        # MODIFIED: Action now hides the screen before showing it, allowing it to repeat.
        button style "legend_filter_button":
            action [Hide("cannot_toggle_message"), Show("cannot_toggle_message")]
            hover_sound "audio/soun_fx/select2.opus"
            hovered Show("displayTextScreen_QuestLegend", displayText="'In Progress' are the current active objectives. This is always shown.")
            unhovered Hide("displayTextScreen_QuestLegend")
            hbox:
                spacing 10
                text "■" color "#172993"
                text _("In Progress") size 20 color "#172993"

        # 2. Completed / Done (Toggleable)
        button style "legend_filter_button":
            action [ToggleDict(quest_filter_states, 'completed'), ToggleDict(quest_filter_states, 'done')]
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            hovered Show("displayTextScreen_QuestLegend", displayText="Quests that have been completed successfully. Click to toggle visibility.")
            unhovered Hide("displayTextScreen_QuestLegend")
            hbox:
                spacing 10
                # Icon color is solid green if ON, more faded green if OFF
                text "■" color ("#008000" if quest_filter_states['completed'] else "#00800040")
                # Text color is always solid green
                text _("Completed") size 20 color "#008000"

        # 3. Not Discovered Yet (Toggleable)
        button style "legend_filter_button":
            action ToggleDict(quest_filter_states, 'pending')
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            hovered Show("displayTextScreen_QuestLegend", displayText="Keep playing to unlock undiscovered objectives! Click to toggle visibility.")
            unhovered Hide("displayTextScreen_QuestLegend")
            hbox:
                spacing 10
                # Icon color is solid gold if ON, more faded gold if OFF
                text "■" color ("#FFD700" if quest_filter_states['pending'] else "#FFD70040")
                # Text color is always solid gold
                text _("Not Discovered Yet") size 20 color "#FFD700"
        
        # 4. Work In Progress (WIP) (Toggleable)
        # --- MODIFIED: Action now toggles our new variable, not the dictionary. ---
        button style "legend_filter_button":
            action ToggleVariable("show_wip_quests") # CHANGED ACTION
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            hovered Show("displayTextScreen_QuestLegend", displayText="A quest that will be available at a future game version. Click to toggle visibility.")
            unhovered Hide("displayTextScreen_QuestLegend")
            hbox:
                spacing 10
                # Icon color now checks our new variable
                text "■" color ("#808080" if show_wip_quests else "#80808040") # CHANGED CONDITION
                # Text color is always solid grey
                text _("Work In Progress (WIP)") size 20 color "#808080"

        # 5. Failed (Toggleable)
        button style "legend_filter_button":
            action ToggleDict(quest_filter_states, 'failed')
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            hovered Show("displayTextScreen_QuestLegend", displayText="A quest that can no longer be completed successfully. Click to toggle visibility.")
            unhovered Hide("displayTextScreen_QuestLegend")
            hbox:
                spacing 10
                # Icon color is solid red if ON, more faded red if OFF
                text "■" color ("#e12345" if quest_filter_states['failed'] else "#e1234540")
                # Text color is always solid red
                text _("Failed") size 20 color "#e12345"


## --- ORIGINAL CODE RESTORED ---
screen diary():
    key "mouseup_3" action [Function(enable_rollback), Hide("diary")]  #close diary and enable rollback

    #full screen
    frame:
        xysize (1280,720)
        background Frame("gui/overlay/game_menu_2.png")
        button: #screen sized button to prevent lcicks from behind screen
            xysize (config.screen_width, config.screen_height)
            background None
            action NullAction() # No action to perform on click

    zorder 1001
    modal diary_modal
    #portraits on left
    vbox:
        #boruto
        xalign 0.01 yalign 0.5
        text ""
        text "[bo_name]" color bo_color xalign 0.5
        imagebutton:
            at customzoom3
            xalign 0.5
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            hovered Show("displayTextScreen", displayText = "[bo_name]'s Quests")
            unhovered Hide("displayTextScreen")
            auto "ui/icons/boru1_%s.png"
            action [Hide("diary_hin"), Hide("diary_him"), Show("diary")]
        #hinata
        text ""
        text "[hin_name]" color hin_color xalign 0.5
        imagebutton:
            at customzoom3
            xalign 0.1
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            hovered Show("displayTextScreen", displayText = "[hin_name] Path Quests")
            unhovered Hide("displayTextScreen")
            auto "ui/icons/hina_%s.png"
            action [Hide("diary_him"), Hide("diary"), Show("diary_hin")]
        #himawari
        text ""
        text "[him_name]" color him_color xalign 0.5
        imagebutton:
            at customzoom3
            xalign 0.1
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            hovered Show("displayTextScreen", displayText = "[him_name] Path Quests")
            unhovered Hide("displayTextScreen")
            auto "ui/icons/hima_%s.png"
            action [Hide("diary_hin"), Hide("diary"), Show("diary_him")]

    default left_categories = collections.OrderedDict()
    default right_categories = collections.OrderedDict()
    window:
        xysize(1200,700)
        xalign 0.4
        yalign 0.2
        background "open_book" at customzoom
        for k, v in quest.quests_dict.items():
            for lpage in left_page:
                if k == lpage:
                    $ left_categories[k] = v
                else:
                    $ right_categories[k] = v

        fixed: # left page
            pos (80, 70)
            xysize (565, 690)
            # Use a vbox that stacks from the bottom-up to create a footer effect
            vbox:
                box_reverse True # This is the key change

                ## The legend is now the FIRST item, so it appears at the BOTTOM.
                use quest_legend()

                ## Add a spacer between the legend and the quest list.
                null height 0

                ## The quest list container now fills the remaining space ABOVE the legend.
                fixed:
                    yfill True
                    use events_page(quest, journal_left_page_adjustment, left_categories, 1) # Left page always shows level 1 quests
                    vbar:
                        xanchor 1.
                        yfill True
                        style "vscrollbar"
                        unscrollable "hide"
                        adjustment journal_left_page_adjustment

        fixed: # right page
            pos (750, 70)
            xysize (565, 680)
            # add Solid("#0f03")
            use events_page(quest, journal_right_page_adjustment, right_categories, 1) # Right page always shows level 1 quests
            vbar:
                xpos 1.
                style "vscrollbar"
                unscrollable "hide"
                adjustment journal_right_page_adjustment

        imagebutton: # cross to close the screen
            pos (1400, 360)
            idle "book_close_idle"
            hover "book_close_hover"
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            action [Function(enable_rollback), Hide("diary")]

screen diary_hin():
    # This action runs every time the screen is shown, resetting the view to the max level.
    on "show" action SetVariable("hin_current_view_level", hin_journal_level)
    key "mouseup_3" action [Function(enable_rollback), Hide("diary_hin")]  #close diary and enable rollback

    #full screen
    frame:
        xysize (1280,720)
        background Frame("gui/overlay/game_menu_2.png")
        button: #screen sized button to prevent lcicks from behind screen
            xysize (config.screen_width, config.screen_height)
            background None
            action NullAction() # No action to perform on click
    zorder 100
    modal diary_modal
    #portraits on left
    vbox:
        #boruto
        xalign 0.01 yalign 0.5
        text ""
        text "[bo_name]" color bo_color xalign 0.5
        imagebutton:
            at customzoom3
            xalign 0.5
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            hovered Show("displayTextScreen", displayText = "[bo_name]'s Quests")
            unhovered Hide("displayTextScreen")
            auto "ui/icons/boru1_%s.png"
            action [Hide("diary_hin"), Hide("diary_him"), Show("diary")]
        #hinata
        text ""
        text "[hin_name]" color hin_color xalign 0.5
        imagebutton:
            at customzoom3
            xalign 0.1
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            hovered Show("displayTextScreen", displayText = "[hin_name] Path Quests")
            unhovered Hide("displayTextScreen")
            auto "ui/icons/hina_%s.png"
            action [Hide("diary_him"), Hide("diary"), Show("diary_hin")]
        #himawari
        text ""
        text "[him_name]" color him_color xalign 0.5
        imagebutton:
            at customzoom3
            xalign 0.1
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            hovered Show("displayTextScreen", displayText = "[him_name] Path Quests")
            unhovered Hide("displayTextScreen")
            auto "ui/icons/hima_%s.png"
            action [Hide("diary_hin"), Hide("diary"), Show("diary_him")]


    default left_categories = collections.OrderedDict()
    default right_categories = collections.OrderedDict()
    window:
        xysize(1200,700)
        xalign 0.4
        yalign 0.2
        background "open_book" at customzoom
        for k, v in quest_hin.quests_dict.items():
            for lpage in left_page:
                if k == lpage:
                    $ left_categories[k] = v
                else:
                    $ right_categories[k] = v


        fixed: # left page
            pos (80, 70)
            xysize (565, 680)
            # Use a vbox that stacks from the bottom-up to create a footer effect
            vbox:
                box_reverse True # This is the key change

                ## The legend is now the FIRST item, so it appears at the BOTTOM.
                use quest_legend()

                ## Add a spacer between the legend and the quest list.
                null height 30

                ## The quest list container now fills the remaining space ABOVE the legend.
                fixed:
                    yfill True
                    # Left page always shows level 1 quests (General, etc)
                    use events_page(quest_hin, journal_left_page_adjustment, left_categories, 1)
                    vbar:
                        xanchor 1.
                        yfill True
                        style "vscrollbar"
                        unscrollable "hide"
                        adjustment journal_left_page_adjustment

        fixed: # right page
            pos (750, 70)
            xysize (565, 680)
            use events_page(quest_hin, journal_right_page_adjustment, right_categories, hin_current_view_level) 
            vbar:
                xpos 1.
                style "vscrollbar"
                unscrollable "hide"
                adjustment journal_right_page_adjustment


        imagebutton: # cross to close the screen
            pos (1400, 360)
            idle "book_close_idle"
            hover "book_close_hover"
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            action [Function(enable_rollback), Hide("diary_hin")]

        # The button is now a direct child of the 'window', drawn on top of everything.
        # Its coordinates are now relative to the window's top-left corner.
        if hin_journal_level > 1:
            # The text shows the current view out of the max unlocked level.
            textbutton "{color=#55ff55}▲{/color} Level [hin_current_view_level]/[hin_journal_level] {color=#55ff55}▼{/color}" at Position(xpos=930, ypos=27):
            # textbutton "Level [hin_current_view_level]/[hin_journal_level]" at Position(xpos=720, ypos=35):
                style "legend_filter_button"
                text_style "quest_unlocked_style"
                text_size 30
                # This action cycles the NEW 'view' variable up to the max unlocked level.
                action SetVariable("hin_current_view_level", (hin_current_view_level % hin_journal_level) + 1)
                hover_sound "audio/soun_fx/select2.opus"
                activate_sound "audio/soun_fx/select4.opus"

screen diary_him():
    on "show" action SetVariable("him_current_view_level", him_journal_level)
    key "mouseup_3" action [Function(enable_rollback), Hide("diary_him")]  #close diary and enable rollback

    #full screen
    frame:
        xysize (1280,720)
        background Frame("gui/overlay/game_menu_2.png")
        button: #screen sized button to prevent lcicks from behind screen
            xysize (config.screen_width, config.screen_height)
            background None
            action NullAction() # No action to perform on click
    zorder 100
    modal diary_modal
    #portraits on left
    vbox:
        #boruto
        xalign 0.01 yalign 0.5
        text ""
        text "[bo_name]" color bo_color xalign 0.5
        imagebutton:
            at customzoom3
            xalign 0.5
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            hovered Show("displayTextScreen", displayText = "[bo_name]'s quests")
            unhovered Hide("displayTextScreen")
            auto "ui/icons/boru1_%s.png"
            action [Hide("diary_hin"), Hide("diary_him"), Show("diary")]
        #hinata
        text ""
        text "[hin_name]" color hin_color xalign 0.5
        imagebutton:
            at customzoom3
            xalign 0.1
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            hovered Show("displayTextScreen", displayText = "[hin_name] Path Quests")
            unhovered Hide("displayTextScreen")
            auto "ui/icons/hina_%s.png"
            action [Hide("diary_him"), Hide("diary"), Show("diary_hin")]
        #himawari
        text ""
        text "[him_name]" color him_color xalign 0.5
        imagebutton:
            at customzoom3
            xalign 0.1
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            hovered Show("displayTextScreen", displayText = "[him_name] Path Quests")
            unhovered Hide("displayTextScreen")
            auto "ui/icons/hima_%s.png"
            action [Hide("diary_hin"), Hide("diary"), Show("diary_him")]


    default left_categories = collections.OrderedDict()
    default right_categories = collections.OrderedDict()
    window:
        xysize(1200,700)
        xalign 0.4
        yalign 0.2
        background "open_book" at customzoom
        for k, v in quest_him.quests_dict.items():
            for lpage in left_page:
                if k == lpage:
                    $ left_categories[k] = v
                else:
                    $ right_categories[k] = v


        fixed: # left page
            pos (80, 70)
            xysize (565, 680)
            # Use a vbox that stacks from the bottom-up to create a footer effect
            vbox:
                box_reverse True # This is the key change

                ## The legend is now the FIRST item, so it appears at the BOTTOM.
                use quest_legend()

                ## Add a spacer between the legend and the quest list.
                null height 30

                ## The quest list container now fills the remaining space ABOVE the legend.
                fixed:
                    yfill True
                    # Left page always shows level 1 quests (General, etc)
                    use events_page(quest_him, journal_left_page_adjustment, left_categories, 1)
                    vbar:
                        xanchor 1.
                        yfill True
                        style "vscrollbar"
                        unscrollable "hide"
                        adjustment journal_left_page_adjustment

        # --- RIGHT PAGE (UNCHANGED CONTENT, BUT NO BUTTON INSIDE) ---
        fixed: # right page
            pos (750, 70)
            xysize (565, 680)
            use events_page(quest_him, journal_right_page_adjustment, right_categories, him_current_view_level)
            vbar:
                xpos 1.
                style "vscrollbar"
                unscrollable "hide"
                adjustment journal_right_page_adjustment

        imagebutton: # cross to close the screen
            pos (1400, 360)
            idle "book_close_idle"
            hover "book_close_hover"
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            action [Function(enable_rollback), Hide("diary_him")]
        
        # The button is now a direct child of the 'window', drawn on top of everything.
        # Its coordinates are now relative to the window's top-left corner.
        if him_journal_level > 1:
            textbutton "{color=#55ff55}▲{/color} Level [him_current_view_level]/[him_journal_level] {color=#55ff55}▼{/color}" at Position(xpos=930, ypos=27):
                style "legend_filter_button"
                text_style "quest_unlocked_style"
                text_size 30
                # The action cycles the 'view' variable.
                action SetVariable("him_current_view_level", (him_current_view_level % him_journal_level) + 1)
                hover_sound "audio/soun_fx/select2.opus"
                activate_sound "audio/soun_fx/select4.opus"


# --- MODIFIED: Screen now takes 'level_to_show' as its last argument ---
screen events_page(manager, adjustment, categories, level_to_show):
    viewport:
        draggable True
        mousewheel "change"
        yadjustment adjustment
        has vbox
        add Solid("#f00", ysize=0)
        for k, v in categories.items():
            # --- MODIFIED: Use our helper function with the correct manager and level ---
            if any(is_quest_visible(manager, q, level_to_show) for q in v.values()):
                if k:
                    null height 25
                    add "journal_divider" xalign .5
                    null height 15
                # --- MODIFIED: Pass the manager and level down to evs_block ---
                use evs_block(manager, k, v, level_to_show)


# --- MODIFIED: Screen now takes 'level_to_show' ---
screen evs_block(manager, cat, evlist, level_to_show, prefix=" {b}-{/b} ", completed_suffix="{image=completed}", progress_suffix="{image=in_progress}", unknown=_("? ? ?")):
    text "~ "+__(cat)+" ~":
        style "category_style"

    null height 20
    for k,v in evlist.items():
        if is_quest_visible(manager, v, level_to_show):

            # --- REVISED LOGIC FOR NUANCED WIP DISPLAY ---

            # First, determine if the quest is a Work-In-Progress.
            if not manager.is_implemented(v.id):
                # --- This is a WIP quest. Now handle its specific states. ---

                # CASE 1: The WIP quest is failed. Hide the title, show failed style.
                # This directly solves the spoiler issue you asked about.
                if v.state == "failed":
                    text prefix + __(unknown):
                        size 20 and 30
                        style "quest_failed_style"

                # CASE 2: The WIP quest is pending. Hide the title, show default WIP style.
                elif v.state == "pending":
                    text prefix + __(unknown):
                        size 20 and 30
                        style "quest_wip_style"
                
                # CASE 3: The WIP quest is "in progress", "unlocked", etc.
                # This is the SNEAK PEEK. Reveal the title but style it as a grey WIP.
                else:
                    text prefix + __(v.title):
                        size 20 and 30
                        style "quest_wip_style"

            else:
                # --- This is a standard, fully implemented quest. ---
                # This block uses the original logic which works correctly for non-WIP quests.
                text prefix+(__(v.title) if v.state != "pending" else __(unknown))+(completed_suffix if v.state == "completed" else (progress_suffix if v.state == "in progress" else "")):
                    size 20 and 30

                    # Apply styling based on state for this implemented quest.
                    if v.state == "pending":
                        style "quest_pending_style"
                    elif v.state == "unlocked":
                        style "quest_unlocked_style"
                    elif v.state == "in progress":
                        style "quest_in_progress_style"
                    elif v.state == "WIP":
                        style "quest_wip_style"
                    elif v.state == "completed":
                        style "quest_completed_style"
                    elif v.state == "done":
                        style "quest_done_style"
                    elif v.state == "failed":
                        style "quest_failed_style"


# text when hovering any button / tooltip
screen displayTextScreen_QuestLegend:
    zorder 1100
    default displayText = "bedrooms"
    frame:
        background "#000000CC"  # Semi-transparent background
        padding (10, 10)
        align (0.5, 0.85)  # Adjust the alignment as needed

        text displayText:
            size 20
            color "#fff"

## --- NEW: Transient message for the non-toggleable filter ---
screen cannot_toggle_message():

    zorder 1002 # Ensure it's on top of the diary
    modal False # Doesn't block other inputs

    frame at a_notify:
        style "frame"
        background "#282828cc"
        padding (10, 5)
        text "This filter cannot be toggled."

transform a_notify:
    # A standard "toast" notification transform
    align (0.5, 0.95) # Appear at the bottom center of the screen
    on show:
        alpha 0.0
        linear 0.2 alpha 1.0 # Fade in
        pause 0.5             # Hold
        linear 0.5 alpha 0.0 # Fade out

init python:
    # --- NEW: Helper function to find the highest quest level in a manager ---
    def get_max_quest_level(manager):
        """
        Iterates through all quests in a manager and returns the highest 'questlevel'.
        Defaults to 1 if no quests or levels are found.
        """
        max_level = 1
        if not manager.quests_dict:
            return max_level
        
        all_levels = [getattr(q, 'questlevel', 1) for cat in manager.quests_dict.values() for q in cat.values()]
        if all_levels:
            return max(all_levels)
        return max_level

    # --- MODIFIED: Function now takes 'level_to_show' argument ---
    def is_quest_visible(manager, q, level_to_show):
        # --- NEW: HIDE SUB-QUESTS IF MASTER QUEST IS PENDING ---
        # This is the new hard rule that overrides all other filters.
        category_name = getattr(q, 'category', None)
        if category_name and category_name != _("General"): # We assume "General" never has a master quest
            master_quest = manager._find_master_quest_for_category(category_name)
            
            # If a master quest for this category exists AND it is still pending...
            if master_quest and master_quest.state == 'pending':
                # ...then this sub-quest is not visible. Period.
                return False
        # --- END NEW LOGIC ---


        # STEP 0: The quest must match the level we want to display.
        # (The rest of the function remains completely unchanged)
        quest_level = getattr(q, 'questlevel', 1)
        if quest_level != level_to_show:
            return False

        # STEP 1: All quests must pass the state filter first.
        # A quest is considered to have a visible state if it is 'in progress' or 'unlocked' (which are always on),
        # OR if its specific state is toggled to True in the filter dictionary.
        state_is_visible = (q.state in ("in progress", "unlocked")) or quest_filter_states.get(q.state, False)

        # If the quest's state is filtered out (e.g., 'failed' is toggled off),
        # then the quest is invisible. We can stop right here.
        if not state_is_visible:
            return False

        # STEP 2: If the state is visible, we now check the quest's TYPE.
        is_wip_quest = not manager.is_implemented(q.id)

        if is_wip_quest:
            # The quest is WIP and its state is visible. Its final visibility
            # now depends ONLY on the master WIP toggle.
            return show_wip_quests
        else:
            # The quest is not WIP and its state is visible. It has passed all
            # checks and should be shown.
            return True