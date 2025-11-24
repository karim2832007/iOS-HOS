# inventory.rpy — full file replacement (bullet-proof initialization + syntax-correct)

# -------------------------------------------------------------------------
# Transforms (ATL)
# -------------------------------------------------------------------------
transform customzoomitem:
    zoom 1.5

transform customitemalpha:
    alpha 0.9


# -------------------------------------------------------------------------
# Item description screen
# -------------------------------------------------------------------------
screen itemdescription(info, name, quantity):
    dismiss action [Hide("itemdescription"), Hide("displayTextScreen")]
    key "mouseup_3" action [Hide("itemdescription"), Hide("displayTextScreen")]
    zorder 300
    modal True

    frame:
        background "#000000"
        maximum (800, 311)
        xalign 0.5
        yalign 0.55

        vbox:
            frame:
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

            grid 2 1:
                xfill True
                yfill True

                frame:  # left panel
                    xfill True
                    yfill True
                    background None
                    add "images/inventory/[name].png" xalign 0.5 yalign 0.5 at customzoomitem

                frame:  # right panel
                    background None

                    text "Owned: {color=#A9A9A9}{color=#3e9c35}[quantity]{/color}{/color}" xalign 0.0 yalign 0.1 size 20
                    text "Description: {color=#A9A9A9}[info]{/color}" xalign 0.0 yalign 0.3 size 20

                    if name == "MassageTipsVolume1":
                        text "Tip: {color=#bfffbf}I should take some time to read this book when I am in my bedroom.{/color}" xalign 0.0 yalign 0.8 size 18
                        xfill True
                        yfill True

                    if name == "Camera":
                        imagebutton:
                            xalign 0.5
                            yalign 0.9
                            auto "ui/use_button_%s.png"
                            action [Hide("itemdescription"), Hide("displayTextScreen"), Show("photo_album")]
                            hover_sound "audio/soun_fx/select2.opus"
                            activate_sound "audio/soun_fx/select4.opus"
                            hovered Show("displayTextScreen", displayText="UseItem")
                            unhovered Hide("displayTextScreen")

                        imagebutton:
                            xpos 0.95
                            idle "close_hover"
                            hover "close"
                            action [Hide("itemdescription"), Hide("displayTextScreen")]
                            hover_sound "audio/soun_fx/select2.opus"
                            activate_sound "audio/soun_fx/select4.opus"
                            hovered Show("displayTextScreen", displayText="Close")
                            unhovered Hide("displayTextScreen")


# -------------------------------------------------------------------------
# Inventory screen
# -------------------------------------------------------------------------
screen inventoryScreen():
    zorder 200
    key "mouseup_3" action [Function(enable_rollback), Hide("inventoryScreen"), Hide("displayTextScreen")]
    modal True

    frame style "inventory_frame":
        text "Inventory" xalign 0.5 ypos -5
        text "You have: {color=#3e9c35}$[money]{/color}" xalign 0.0 ypos -5

        imagebutton style "close_btn":
            idle "close_hover"
            hover "close"
            action [Function(enable_rollback), Hide("inventoryScreen"), Hide("displayTextScreen")]
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            hovered Show("displayTextScreen", displayText="CloseInventory")
            unhovered Hide("displayTextScreen")

        vbox:
            ypos 30

            # Calculate the maximum number of slots based on the maximum items per slot
            $ max_items_per_slot = inventory.max_items_per_slot
            $ num_slots = max(21, int(sum(item.quantity for item in inventory.items) / max_items_per_slot) + 1)

            # Use vpgrid for flexible grid layout with scrollbars
            if num_slots > 21:
                vpgrid cols 7 spacing 5 draggable True mousewheel True scrollbars "vertical":
                    xpos 5
                    ypos 5

                    for slot in range(num_slots):
                        fixed:
                            maximum (155, 155)

                            imagebutton:
                                idle "images/inventory/inventory_gui/slot_bg_idle.png"
                                hover "images/inventory/inventory_gui/slot_bg_hover.png"
                                xalign 0.5
                                yalign 0.5
                                action NullAction()

                            if slot < len(inventory.items):
                                $ item = inventory.items[slot]
                                add "images/inventory/" + item.name + ".png" xalign 0.5 yalign 0.5

                                $ item_name = item.name.replace('_', '')
                                $ item_info = item.info
                                $ item_quantity = item.quantity

                                imagebutton:
                                    idle "images/inventory/inventory_gui/slot_bg5.png"
                                    hover "images/inventory/inventory_gui/slot_bg_hover.png"
                                    action Show("itemdescription")
                                    hover_sound "audio/soun_fx/select2.opus"
                                    hovered Show("displayTextScreen", info=item_info, name=item_name, quantity=item_quantity)
                                    unhovered Hide("displayTextScreen")
                                    activate_sound "audio/soun_fx/select4.opus"

                                text str(item_quantity) style "item_quantity"
            else:
                vpgrid cols 7 spacing 5 draggable False mousewheel False:
                    xpos 5
                    ypos 5

                    for slot in range(num_slots):
                        fixed:
                            maximum (155, 155)

                            imagebutton:
                                idle "images/inventory/inventory_gui/slot_bg_idle.png"
                                hover "images/inventory/inventory_gui/slot_bg_hover.png"
                                xalign 0.5
                                yalign 0.5
                                action NullAction()

                            if slot < len(inventory.items):
                                $ item = inventory.items[slot]
                                add "images/inventory/" + item.name + ".png" xalign 0.5 yalign 0.5

                                $ item_name = item.name.replace('_', '')
                                $ item_info = item.info
                                $ item_quantity = item.quantity

                                imagebutton:
                                    idle "images/inventory/inventory_gui/slot_bg5.png"
                                    hover "images/inventory/inventory_gui/slot_bg_hover.png"
                                    action Show("itemdescription", info=item_info, name=item_name, quantity=item_quantity)
                                    hover_sound "audio/soun_fx/select2.opus"
                                    hovered Show("displayTextScreen", displayText=item_name)
                                    unhovered Hide("displayTextScreen")
                                    activate_sound "audio/soun_fx/select4.opus"

                                text str(item_quantity) style "item_quantity"

                                if item_name in ["Camera", "Other_Usable_Item", "Another_Item"]:
                                    frame:
                                        xsize 10
                                        ysize 10
                                        xalign 0.8
                                        yalign 0.1
                                        background "#00FF00"
                                        at customitemalpha


# -------------------------------------------------------------------------
# Images
# -------------------------------------------------------------------------
image close:
    "images/inventory/inventory_gui/close.png"
    size (30, 30)

image close_hover:
    "images/inventory/inventory_gui/close_hover.png"
    size (30, 30)


# -------------------------------------------------------------------------
# Styles
# -------------------------------------------------------------------------
style inv_item is text:
    size 16
    bold True
    color Color((255, 0, 149, 255))
    pos (2, 0)

style item_quantity is text:
    size 16
    bold True
    color Color((255, 0, 149, 255))
    pos (115, 125)

style item_price is text:
    size 16
    bold True
    color Color((62, 156, 53, 255))
    pos (10, 5)

style inventory_frame is frame:
    padding (20, 20, 0, 30)
    xalign 0.5
    yalign 0.5
    xsize 1160
    ysize 550
    background Color((0, 0, 0, 161))

style inventory_frame_shop is frame:
    padding (20, 20, 0, 30)
    xalign 0.98
    yalign 0.5
    xsize 840
    ysize 720
    background Color((0, 0, 0, 161))

style close_btn:
    xpos 1100
    ypos 0

style hud_frame is frame:
    xpadding 10
    ypadding 10
    xalign 0.5
    yalign 0.0


# -------------------------------------------------------------------------
# Class definitions (must load first)
# -------------------------------------------------------------------------
init -2 python:
    class Item:
        def __init__(self, name, info, price, quantity=1):
            self.name = name
            self.info = info
            self.price = price
            self.quantity = quantity

    class Inventory:
        def __init__(self):
            self.items = []
            self.max_items_per_slot = 99

        def add_item(self, item, quantity=1):
            remaining_quantity = quantity
            while remaining_quantity > 0:
                for inv_item in self.items:
                    if inv_item.name == item.name and inv_item.quantity < self.max_items_per_slot:
                        available_quantity = min(remaining_quantity, self.max_items_per_slot - inv_item.quantity)
                        inv_item.quantity += available_quantity
                        remaining_quantity -= available_quantity
                        break
                else:
                    available_quantity = min(remaining_quantity, self.max_items_per_slot)
                    new_item = Item(name=item.name, info=item.info, price=item.price, quantity=available_quantity)
                    self.items.append(new_item)
                    remaining_quantity -= available_quantity

        def remove_item(self, item, quantity=1):
            remaining_quantity = quantity
            for inv_item in list(self.items):
                if inv_item.name == item.name:
                    if remaining_quantity >= inv_item.quantity:
                        remaining_quantity -= inv_item.quantity
                        self.items.remove(inv_item)
                    else:
                        inv_item.quantity -= remaining_quantity
                        remaining_quantity = 0
                    if remaining_quantity == 0:
                        break

        def find_item_by_name(self, name):
            for inv_item in self.items:
                if inv_item.name == name:
                    return inv_item
            return None

        def update_item(self, item_name, name=None, info=None, price=None, quantity=None):
            items_to_update = [it for it in self.items if it.name == item_name]
            if not items_to_update:
                renpy.log(f"No item found with name: {item_name}")
                return
            for it in items_to_update:
                if name is not None:
                    it.name = name
                if info is not None:
                    it.info = info
                if price is not None:
                    it.price = price
                if quantity is not None:
                    it.quantity = quantity

        @staticmethod
        def update_independent_item(item, name=None, info=None, price=None, quantity=None):
            if name is not None:
                item.name = name
            if info is not None:
                item.info = info
            if price is not None:
                item.price = price
            if quantity is not None:
                item.quantity = quantity
            renpy.log(f"Updated independent item: {item.name}")


# -------------------------------------------------------------------------
# Safe global instance creation and aliasing
# -------------------------------------------------------------------------
init -1 python:
    # Create a single global inventory instance early.
    if "inventoryShop" not in globals():
        inventoryShop = Inventory()

    # Alias `inventory` to `inventoryShop` for UI code that expects `inventory`.
    if "inventory" not in globals():
        inventory = inventoryShop
    else:
        inventoryShop = inventory