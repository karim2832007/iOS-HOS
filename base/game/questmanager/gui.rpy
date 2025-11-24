## Here is the place where you can customize the skin of your diary. 
## You can safety modify this file.


init -1: ## <-- Don't touch this one /!\

    ## The position of the diary screen in game
    ## If 0, the screen is under the textbox, if 2, the screen is over the textbox
    define diary_zorder = 0

    ## If true, the game is freezed when the player open the diary screen.
    define diary_modal = False

    ## Add between the {} all the category you want to display on the left page. 
    ## The others will be displayed on the right page.
    ## Be sure to add a comma between the categories
    define left_page = {_("General"),}

    ## --- NEW: Quest Filter State ---
    ## This dictionary holds the filter settings for the journal.
    ## True means quests with that state are SHOWN, False means they are HIDDEN.
    ## "in progress" is always True as requested.
    default quest_filter_states = {
        "pending": True,
        "unlocked": True,
        "in progress": True, # This state is always shown, but the variable is needed.
        "WIP": True,
        "completed": True,
        "done": True,
        "failed": True,
        "canceled": True,
        }
    default show_wip_quests = True

#_______________Image costumization___________________

## You can change the path of all the images to your own images.
image open_book = "questmanager/assets/open_book.png"
image book_close_idle = "questmanager/assets/book_close_idle.png"
image book_close_hover = "questmanager/assets/book_close_hover.png"
image completed = "questmanager/assets/completed.png"
image in_progress = "questmanager/assets/in_progress.png"
image journal_divider = "questmanager/assets/journal_divider.png"



#___________________Texts and styles_______________________


## The style that is used for the categories
style category_style is text:
    xalign 0.5 #if 0.0 text is at left, if 0.5 text is centered, if 1.0 text is at right 
    color "#63050e"
    # font "questmanager/assets/Pacifico-Regular.ttf"
    size 30
    bold False
    italic False
    strikethrough False



## MODIFIED: The style that is used for the pending (? ? ?) events
## The pending events are displayed with "???"
style quest_pending_style is text:
    color "#FFD700"
    # font "questmanager/assets/Pacifico-Regular.ttf"
    size 20
    bold False
    italic False
    strikethrough False

## The style that is used for the unlocked events
style quest_unlocked_style is text:
    color "#172993"
    # font "questmanager/assets/Pacifico-Regular.ttf"
    size 20
    bold False
    italic False
    strikethrough False

## The style that is used for the in progress events
style quest_in_progress_style is text:
    color "#172993"
    # font "questmanager/assets/Pacifico-Regular.ttf"
    size 25
    bold False
    italic False
    strikethrough False

## NEW: The style that is used for the WIP events
style quest_wip_style is text:
    color "#808080" # Grey
    size 20
    bold False
    italic False
    strikethrough False

## MODIFIED: The style that is used for the completed events
style quest_completed_style is text:
    yalign .5
    color "#008000" # Green
    size 20
    bold False
    italic True
    strikethrough False

## MODIFIED: The style that is used for the done events
style quest_done_style is text:
    color "#008000" # Green
    size 20
    bold False
    italic False
    strikethrough True

## The style that is used for the failed events
style quest_failed_style is text:
    color "#e12345"
    # font "questmanager/assets/Pacifico-Regular.ttf"
    size 20
    bold False
    italic False
    strikethrough True


#___________Buttons____________

## --- NEW: Style for the legend filter buttons ---
style legend_filter_button is button:
    # background None
    # hover_background None
    # xfill True # Ensures the hbox inside fills the space

    background Frame("gui/button/idle_background.png", 10, 10)  # optional image frame
    idle_background None             # dark semi-transparent
    hover_background "#444c"             # lighter semi-transparent
    selected_background "#55aa5588"      # light green with transparency
    insensitive_background "#2221" 

    # xpadding 15
    # ypadding 8
    # xmargin 5
    # ymargin 5
    # minimum (140, 40)



style open_diary_screen_btn is button:
    #background "" xalign .5 yalign .5
    #hover_background ""
    xysize(120,55)

style open_diary_screen_btn is text:
    size 35
    xalign .5

## --- NEW: Styles for the Journal Level Selector ---
## Following the existing pattern in this file.

# --- Style for a standard, unlocked level button ---
style level_selector_button is button:
    background None
    hover_background None

style level_selector_button is text:
    color "#6d5b43"
    hover_color "#a48965"
    size 22


# --- Style for the active/selected level button ---
style level_selector_button_active is button:
    background None
    hover_background None

style level_selector_button_active is text:
    color "#b43434"
    hover_color "#d45454"
    size 24
    bold True


# --- Style for a locked level button ---
style level_selector_button_locked is button:
    background None
    hover_background None

style level_selector_button_locked is text:
    color "#888888"
    hover_color "#888888" # No color change on hover
    size 22
    italic True