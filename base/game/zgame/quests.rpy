label journaltutorial:
    $ notification("Journal and map functionallity unlocked.")
    dev"You have unlocked the Journal, Map and Inventory systems."
    show questjournal1 with dissolve:
        zoom 0.8 xalign 0.5 yalign 0.0
    dev"[bo_name]'s journal will keep track of your active quests as well as provide general guidance if you are unsure of how to proceed."
    dev"The left page contains the titles of all your currently active quest, while the right page tracks each quest's objectives."
    dev"The current objective of each quest is marked with a blue arrow while completed objectives are marked with a green checkmark."
    show questjournal2 with dissolve:
        zoom 0.8 xalign 0.5 yalign 0.0
    dev"[him_name] and [hin_name]'s journals work a little bit differently..."
    dev"You'll have to explore to find and complete objectives that are initially hidden. When you complete one of those, it'll be marked as such on the right page as seen in the image above."
    dev"Completing multiple Love or Hatred objectives will unlock an 'Advancement' quest that will move the corresponding girl's Hatred/Love path to the next level when completed."
    dev"Completing an 'Advancement' quest will reset the girl's journal with new objectives and the whole process will repeat again."
    dev"Don't go crazy looking for hidden objectives just yet. This version will not have enough Love/Hatred objectives to advance either path to Level-2"
    hide questjournal1
    hide questjournal2
    with dissolve
 
    show screen actionbuttonshouse
    show halfblack
    show redarrow
    with dissolve
    dev"When available, use the buttons located at the left side of the screen to perform various actions."
    hide halfblack
    hide redarrow
    with dissolve
    dev"You are now in freeroam mode."
    dev"Please note that this section of the game is currently in an expiremental state and very much so, in development!"
    dev"The primary focus of the next few updates is to enhance the content, flow and feel of freeroam to make it as painless (And as saucy) as possible!"
    dev"Please look forward to that and perhaps reserve judgement until then!"




    
    call showUIhouse from _call_showUIhouse_67
    $ ui.interact()