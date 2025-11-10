



        


#quest bohim_1------------------------------------------------------------------------------------------------------------------
screen bohim_1_screen():
    imagebutton:
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus" 
        xpos 0.22
        ypos 0.24
        auto "/ui/icons/itemflash_%s.png" at customzoom3
        action [Hide("displayTextScreen"), Jump("bohim_1_itemfound"), Hide("bohim_1_screen")]
        hovered Show("displayTextScreen", displayText = "Drawer")
        unhovered Hide("displayTextScreen")
        

default him_quest_initiated = False
default him_item1 = False

label bohim_1:
    if him_item1 == True:
        return
    else:

        if him_quest_initiated == True:
            jump skipquestintro
        $ him_quest_initiated = True
        $ clickinfobutton = "Maybe I can find something useful in here..."
        bot"[him_name] is away at school on weekdays..."
        bot"A chance to snoop around her room! Maybe I will find something useful, or something to use against her!"
        
        $ notification("Quest discovered!")
        $ quest.check("bohim_1", "unlocked")
        $ quest.add([
            Quest("bohim1_1", ("Look for a hidden item in [him_name]'s room while she is away"), ("[him_name]'s garments"), ("in progress")),
            Quest("bohim1_2", ("Perhaps her garments could enhance your nightly fantasies..."), ("[him_name]'s garments"), ("pending")),
        ])
        dev"At times, you will be able to find hidden items in some rooms."
        dev"Search around the room to find a quest item."
        label skipquestintro:
            $ infobutton = "active"
            show screen bohim_1_screen
            
            call showUIhouse from _call_showUIhouse_1
            $ ui.interact()
        label bohim_1_itemfound:
            $ him_item1 = True
            hide screen bohim_1_screen
            call hideUI from _call_hideUI_1
            bo"[him_name]'s drawer... Maybe I can find something to use against her!"
            
            show himaquest_p with dissolve
            show screen bohim_1_screen2
            call screen scrollingtext("Find a useful item...")
            
            $ ui.interact()
            label bohim_1_itemfoundjump:
            hide screen bohim_1_screen2
            bo"Those panties of hers..."
            bo"I have an idea of how to put them at use..."
            menu:
                bo"I have an idea of how to put them at use..."
                "Steal":
      
                    call getItem(himawaripanties, 1) from _call_getItem_1
                    
                    $ infobutton = "inactive"
                    hide screen bohim_1_screen2
                    $ quest.check("bohim1_1", "completed")
                    $ quest.check("bohim1_2", "in progress")
                    bo"I will be taking those!"
                    $ notification("Quest Updated")
                    scene himawari_bedroom_1 with dissolve
                    
                    return
               
                
    
screen bohim_1_screen2:
    imagebutton:
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"
        idle "himaquest_p"  #image in ui / needs to be seperate for correct images to be displayed when hovering
        hover "himaquest_p_hover"
        focus_mask "himaquest_p_mask"
        mouse "handsmall"
        hovered [Show("displayTextScreen", displayText = "[him_name]'s underwear")]
        unhovered [Hide("displayTextScreen")]
        action [Hide("displayTextScreen"), Jump("bohim_1_itemfoundjump")]



screen bohim_1_screen():
    imagebutton:
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus" 
        xpos 0.22
        ypos 0.24
        auto "/ui/icons/itemflash_%s.png" at customzoom3
        action [Hide("displayTextScreen"), Hide("bohim_1_screen2"), Jump("bohim_1_itemfound"), Hide("bohim_1_screen")]
        hovered Show("displayTextScreen", displayText = "Drawer")
        unhovered Hide("displayTextScreen")