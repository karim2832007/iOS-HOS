# stat_path_requirements_popup.rpy

define pending_quest_color = "#FFD700"
define completed_quest_color = "#008000"

style popup_title_text is gui_text:
    size 45
    color "#ffffff"
    outlines [ (2, "#000000cc", 0, 0) ]
    xalign 0.5

style popup_subtitle_text is gui_text:
    size 22
    color "#e0e0e0"
    outlines [ (1, "#000000", 0, 0) ]
    text_align 0

style popup_body_text is gui_text:
    size 22
    color "#e0e0e0"
    outlines [ (1, "#000000", 0, 0) ]
    xalign 0.5

style popup_quest_item is gui_text:
    size 20
    color "#ffffff"
    outlines [ (1, "#000000", 0, 0) ]
    xalign 0.5

screen path_requirements_screen(path_title, path_description, completed_count, required_count, missing_count, all_quests_with_state):
    modal True
    zorder 200

    frame:
        xysize (1280, 720)
        background Frame("gui/overlay/game_menu_nodivider.png")

        button:
            xysize (config.screen_width, config.screen_height)
            background None
            action NullAction()

        imagebutton:
            xalign 0.95 yalign 0.05
            auto "map/ui_close_%s.png"
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            action Jump("temporary_v20_choice")

        vbox:
            xalign 0.5
            yalign 0.5
            xsize 750
            spacing 15

            $ formatted_title = colorize_path_words(path_title)
            text "[formatted_title] Path" style "popup_title_text"

            null height 30

            text "You have completed [completed_count] of [required_count] required [formatted_title] objectives." style "popup_body_text"
            null height 10
            text "Complete [missing_count] more of the following to proceed:" style "popup_body_text"
            null height 20

            viewport:
                mousewheel True
                ymaximum 300
                ## MODIFIED: These are the two key changes to fix the scrollbars.
                scrollbars "vertical"
                vscrollbar_unscrollable "hide"

                vbox:
                    ## MODIFIED: This prevents the horizontal scrollbar from appearing.
                    xfill True
                    spacing 10
                    for quest, state in all_quests_with_state:

                        if state == "completed":
                            $ final_title = renpy.substitute(quest.title)
                            $ formatted_quest_title = colorize_path_words(final_title)
                            text "- {s}{color=[completed_quest_color]}[formatted_quest_title!t]{/color}{/s}" style "popup_quest_item"

                        elif state == "pending":
                            hbox:
                                style "popup_quest_item"
                                spacing 10

                                text "-"
                                textbutton "? ? ?":
                                    text_color pending_quest_color
                                    action NullAction()
                                    hover_sound "audio/soun_fx/select2.opus"
                                    activate_sound "audio/soun_fx/select4.opus"
                                    hovered Show("displayTextScreen_QuestLegend", displayText="Keep playing to unlock undiscovered objectives!")
                                    unhovered Hide("displayTextScreen_QuestLegend")

                        else:
                            $ final_title = renpy.substitute(quest.title)
                            $ formatted_quest_title = colorize_path_words(final_title)
                            text "- [formatted_quest_title!t]" style "popup_quest_item"