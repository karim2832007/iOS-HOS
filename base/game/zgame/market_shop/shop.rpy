
default totalspent = 0
screen itemdescriptionshop(info,name,price):
    dismiss action [Hide("itemdescriptionshop"), Hide("displayTextScreen")]
    key "mouseup_3" action [Hide("itemdescriptionshop"), Hide("displayTextScreen")]  #close inventoryScreen and enable rollback
    zorder 300
    modal True
    frame:
        
        background "#000000"
        maximum(800, 311)
        xalign 0.5 yalign 0.55
        vbox:
            frame: #10% height line that shows item name
                background None
                ymaximum 0.1
                xfill True
                yfill True
                grid 2 1:
                    xfill True
                    yfill True
                    frame:
                        xfill True
                        yfill True
                        background None
                        text "[name]" xalign 0.5 size 30
                    frame:
                        xfill True
                        yfill True
                        background None
                        text "Info:" xalign 0.5 size 30
            grid 2 1: #split the rest of the area in 2 equal vertical parts
                xfill True
                yfill True

                frame: #left panel
                    xfill True
                    yfill True
                    background None
                    add "images/inventory/[name].png" xalign 0.5 yalign 0.5 at customzoomitem

                frame: #right panel
                    background None
                    text "Price:{color=#A9A9A9}{color=#3e9c35} $[price]{/color}{/color}" xalign 0.0 yalign 0.1 size 20 
                    text "Description: {color=#A9A9A9}[info]{/color}" xalign 0.0 yalign 0.3 size 20 
                    xfill True
                    yfill True
                    imagebutton: #buy button
                        xalign 0.5 yalign 0.9
                        auto "ui/buy_button_%s.png"
                        action [Hide("itemdescriptionshop"), Call("buyItem", name = name, cost = price)]
                        hover_sound "audio/soun_fx/select2.opus"
                        activate_sound "audio/soun_fx/select4.opus"
                        hovered Show("displayTextScreen", displayText = "Buy Item")
                        unhovered Hide("displayTextScreen")
        imagebutton:
            xpos 0.95
            idle "close_hover"
            hover "close"
            action [Hide("itemdescriptionshop"), Hide("displayTextScreen")]
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            hovered Show("displayTextScreen", displayText = "Close")
            unhovered Hide("displayTextScreen")
screen shopScreen():
    key "mouseup_3" action [Function(enable_rollback), Hide("shopScreen"), Hide("displayTextScreen")]  #close inventoryScreen and enable rollback
    modal True
    
    #shopkeeper interactions
    imagebutton:
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            # background("#f95150") #backgroudn to test clickable area
            maximum(700, 1000)   #clickable area for shopkeeper
            xpos -60
            ypos 0.01
            hover "characters/headshots/npcs/tenten/npc_shopkeep[shopkeep_annoyance]_hover.webp"
            idle "characters/headshots/npcs/tenten/npc_shopkeep[shopkeep_annoyance]_idle.webp"
            at customzoom
            # auto "characters/headshots/npcs/npc_shopkeep[shopkeep_annoyance]_%s.png" at customzoom
            hovered Show("displayTextScreen", displayText = "Interact with shopkeeper")
            unhovered Hide("displayTextScreen")
            action [Show("shopScreen"), Call("shoptocall")]


    frame style "inventory_frame_shop":
    
        text "Shop" xalign 0.5 ypos -5
        text "You have: {color=#3e9c35}$[money]{/color}" xalign 0.0 ypos -20
        text "Total spent: {color=#3e9c35}$[totalspent]{/color}" xalign 0.0 ypos 5
        imagebutton style "close_btn":
            xalign 0.99
            idle "close_hover"
            hover "close"
            action [Function(enable_rollback), Hide("shopScreen"), Hide("displayTextScreen")]
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            hovered Show("displayTextScreen", displayText = "Close Shop")
            unhovered Hide("displayTextScreen")
        vbox:
            ypos 30
            # Calculate the maximum number of slots based on the maximum items per slot
            $ max_items_per_slot = inventory.max_items_per_slot
            $ num_slots = max(20, int(sum(item.quantity for item in inventoryShop.items) / max_items_per_slot) + 1) # increase the slot here

            # Use vpgrid for flexible grid layout with scrollbars
            if num_slots > 20:
                vpgrid cols 5 spacing 5 draggable True mousewheel True scrollbars "vertical":
                    xpos 5 ypos 5
                    for slot in range(num_slots):  
                        fixed:
                            maximum(155, 155)
                            # background Image("images/inventory/inventory_gui/slot_bg.png") xalign 0.5 yalign 0.5
                            imagebutton:
                                idle "images/inventory/inventory_gui/slot_bg_idle.png" 
                                hover "images/inventory/inventory_gui/slot_bg_hover.png"
                                xalign 0.5 yalign 0.5
                                action NullAction()

                            # Check if the slot should display an item
                            if slot < len(inventoryShop.items):
                                $ item = inventoryShop.items[slot]
                                add Image("images/inventory/" + item.name + ".png", xalign=0.5, yalign=0.5)

                                # Get the item name
                                $ item_name = item.name.replace('_', ' ')
                                $ item_info = item.info
                                $ item_price = item.price
                                #hover show name
                                imagebutton:
                                    idle "images/inventory/inventory_gui/slot_bg5.png" 
                                    hover "images/inventory/inventory_gui/slot_bg_hover.png"
                                    action Show("itemdescriptionshop", info=item_info, name=item_name, price=item_price)
                                    hover_sound "audio/soun_fx/select2.opus"
                                    hovered Show("displayTextScreen", displayText = item_name)
                                    unhovered Hide("displayTextScreen")
                                    activate_sound "audio/soun_fx/select4.opus"

                                # Get the item quantity
                                $ item_quantity = item.quantity

                                # Display the item name
                                #text item_name style style["inv_item"]

                                # Display the item quantity
                                text str(item_quantity) style "item_quantity"
                                text str(item_price) style "item_price"
            else:
                vpgrid cols 5 spacing 5 draggable False mousewheel False:
                    xpos 5 ypos 5
                    for slot in range(num_slots):  
                        fixed:
                            maximum(155, 155)
                            # background Image("images/inventory/inventory_gui/slot_bg.png") xalign 0.5 yalign 0.5
                            imagebutton:
                                idle "images/inventory/inventory_gui/slot_bg_idle.png" 
                                hover "images/inventory/inventory_gui/slot_bg_hover.png" 
                                xalign 0.5 yalign 0.5
                                action NullAction()

                            # Check if the slot should display an item
                            if slot < len(inventoryShop.items):
                                $ item = inventoryShop.items[slot]
                                add Image("images/inventory/" + item.name + ".png", xalign=0.5, yalign=0.5)
                                # Get the item name info price
                                $ item_name = item.name.replace('_', ' ')
                                $ item_info = item.info
                                $ item_price = item.price
                                imagebutton:
                                    idle "images/inventory/inventory_gui/slot_bg5.png" 
                                    hover "images/inventory/inventory_gui/slot_bg_hover.png"
                                    action Show("itemdescriptionshop", info=item_info, name=item_name, price=item_price)
                                    hover_sound "audio/soun_fx/select2.opus"
                                    hovered Show("displayTextScreen", displayText = item_name)
                                    unhovered Hide("displayTextScreen")
                                    activate_sound "audio/soun_fx/select4.opus"

                                # Get the item quantity
                                $ item_quantity = item.quantity

                                # Display the item name
                                # text item_name style style["inv_item"]

                                # Display the item quantity
                                text str(item_quantity) style "item_quantity"
                                text str("$[item_price]") style "item_price"