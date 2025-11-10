init python:
    def close_map():
        renpy.hide_screen("mapui")
        renpy.hide_screen("displayTextScreen")
        #renpy.show_screen("housemap")

  

screen mapui():
    zorder 1020
    key "mouseup_3" action Hide("mapui") #close with rightclick
    frame:
        xysize (1280,720)
        if day_part == 1 or day_part == 2:
            background Frame("map/newmap.jpg")
        else:
            background Frame("map/newmap_night.jpg")
        button: #screen sized button to prevent lcicks from behind screen
            xysize (config.screen_width, config.screen_height)
            background None
            action NullAction() # No action to perform on click
            

            #close map button
            imagebutton:
                hover_sound "audio/soun_fx/select2.opus"
                activate_sound "audio/soun_fx/select4.opus"
                auto "map/ui_close_%s.png"
                hovered Show("displayTextScreen", displayText = "Close Map")
                unhovered Hide("displayTextScreen")
                action [Function(close_map)]
               

            #home button
            imagebutton:
                hover_sound "audio/soun_fx/select2.opus"
                activate_sound "audio/soun_fx/select4.opus"
                idle Transform("map/map_home.webp", alpha=0.8)
                hover "map/map_home.webp"
                focus_mask True
                yalign 1.0
                hovered Show("displayTextScreen", displayText = "Home")
                unhovered Hide("displayTextScreen")
                action [Function(close_map), SetVariable("boruto_location", "home"), Function(move_to_room, "house")]

            #Inohouse button
            imagebutton:
                hover_sound "audio/soun_fx/select2.opus"
                activate_sound "audio/soun_fx/select4.opus"
                idle Transform("map/map_inohouse.webp", alpha=0.8)
                hover "map/map_inohouse.webp"
                focus_mask True
                hovered Show("displayTextScreen", displayText = "Ino's House")
                unhovered Hide("displayTextScreen")
                action [Function(close_map), SetVariable("boruto_location", "inohouse"), Function(move_to_room, "inohouse")]

            #Uchihahousehold button
            if uchihahousehold_unlocked == True:
                imagebutton:
                    hover_sound "audio/soun_fx/select2.opus"
                    activate_sound "audio/soun_fx/select4.opus"
                    idle Transform("map/map_uchihahouse.webp", alpha=0.8)
                    hover "map/map_uchihahouse.webp"
                    focus_mask True
                    hovered Show("displayTextScreen", displayText = "Uchiha Household")
                    unhovered Hide("displayTextScreen")
                    action [Function(close_map), SetVariable("boruto_location", "uchihahousehold"), Function(move_to_room, "uchihahousehold")]

            #market button
            imagebutton:
                hover_sound "audio/soun_fx/select2.opus"
                activate_sound "audio/soun_fx/select4.opus"
                idle Transform("map/map_market.webp", alpha=0.8)
                hover "map/map_market.webp"
                focus_mask True
                hovered Show("displayTextScreen", displayText = "Market Area")
                unhovered Hide("displayTextScreen")
                action [Function(close_map), SetVariable("boruto_location", "market"), Function(move_to_room, "shop")]

            #Infirmary button
            imagebutton:
                hover_sound "audio/soun_fx/select2.opus"
                activate_sound "audio/soun_fx/select4.opus"
                idle Transform("map/map_infirmary.webp", alpha=0.8)
                hover "map/map_infirmary.webp"
                focus_mask True
                hovered Show("displayTextScreen", displayText = "Infirmary")
                unhovered Hide("displayTextScreen")
                action [Function(close_map), SetVariable("boruto_location", "infirmary"), Function(move_to_room, "infirmary")]
            

            #Daimyo button
            if daimyo_unlocked == True:
                imagebutton:
                    hover_sound "audio/soun_fx/select2.opus"
                    activate_sound "audio/soun_fx/select4.opus"
                    idle Transform("map/map_daimyo.webp", alpha=0.8)
                    hover "map/map_daimyo.webp"
                    focus_mask True
                    hovered Show("displayTextScreen", displayText = "Daimyo's Plot")
                    unhovered Hide("displayTextScreen")
                    action [Function(close_map), SetVariable("boruto_location", "daimyopalace"), Function(move_to_room, "daimyopalace")]
            
            
