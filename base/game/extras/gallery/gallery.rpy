## gallery.rpy
## Membership‑aware CG Gallery

default current_category = "Everything"
default gallery_page = 0
default closeup_page = 0

# -------------------------------------------------------------------------
# Locked Gallery (default for non-members)
# -------------------------------------------------------------------------
screen gallery_locked():
    tag menu
    add "black"

    $ filtered_items = get_filtered_items(current_category, persistent.show_only_unlocked)
    $ start = gallery_page * maxperpage
    $ end = min(start + maxperpage - 1, len(filtered_items) - 1)

    grid maxnumx maxnumy:
        xfill True
        yfill True

        for i in range(start, end + 1):
            $ item = filtered_items[i]
            $ item.refresh_lock()

            if item.is_locked:
                imagebutton:
                    idle Transform(
                        Composite(
                            (379, 180),
                            (0, 0), Transform(item.full_path, blur=50.0, matrixcolor=BrightnessMatrix(-0.2), size=(379, 180)),
                            (139, 40), Transform("images/locktransparent.png", size=(100, 100))
                        ),
                        size=(379, 180)
                    )
                    action NullAction()
                    xalign 0.5
                    yalign 0.0
                    style "gallery_button"
                    hovered Show("displayTextScreen", displayText=item.tooltip)
                    unhovered Hide("displayTextScreen")
            else:
                imagebutton:
                    idle Transform(item.full_path, size=(379, 180))
                    action Show("gallery_closeup", dissolve, [item.full_path])
                    xalign 0.5
                    yalign 0.0
                    style "gallery_button"
                    hovered Show("displayTextScreen", displayText=item.tooltip)
                    unhovered Hide("displayTextScreen")

        for i in range(end - start + 1, maxperpage):
            null

    use gallery_footer(filtered_items)

    # Full‑screen membership message for non‑members
    frame:
        xalign 0.5
        yalign 0.5
        background "#0008"
        padding (30, 30)
        text "❌ If you wish for unlocked CGs, verify your membership by clicking on Unlock Cheats and adding your Discord ID.":
            size 28
            color "#FFF"
            xalign 0.5
            text_align 0.5

# -------------------------------------------------------------------------
# Unlocked Gallery (exclusive for members)
# -------------------------------------------------------------------------
screen gallery_unlocked():
    tag menu
    add "black"

    $ filtered_items = get_filtered_items(current_category, persistent.show_only_unlocked)
    $ start = gallery_page * maxperpage
    $ end = min(start + maxperpage - 1, len(filtered_items) - 1)

    grid maxnumx maxnumy:
        xfill True
        yfill True

        for i in range(start, end + 1):
            $ item = filtered_items[i]

            imagebutton:
                idle Transform(item.full_path, size=(379, 180))
                action Show("gallery_closeup", dissolve, [item.full_path])
                xalign 0.5
                yalign 0.0
                style "gallery_button"
                hovered Show("displayTextScreen", displayText=item.tooltip)
                unhovered Hide("displayTextScreen")

        for i in range(end - start + 1, maxperpage):
            null

    use gallery_footer(filtered_items)

    # Full‑screen membership message for verified members
    frame:
        xalign 0.5
        yalign 0.5
        background "#0008"
        padding (30, 30)
        text "✅ Membership Verified — Have fun with the unlocked CGs!":
            size 28
            color "#FFD700"
            xalign 0.5
            text_align 0.5

# -------------------------------------------------------------------------
# Shared footer (pagination + navigation)
# -------------------------------------------------------------------------
screen gallery_footer(filtered_items):
    hbox:
        spacing 10
        xalign 0.53
        yalign 0.98

        $ total_pages = max(1, (len(filtered_items) + maxperpage - 1) // maxperpage)
        $ start_page = max(0, gallery_page - 5)
        $ end_page = min(total_pages - 1, gallery_page + 5)

        if start_page > 0:
            text "..." style "gallery_page_number" color "#000"

        for p in range(start_page, end_page + 1):
            $ is_current = p == gallery_page
            if is_current:
                button:
                    xpadding 10
                    ypadding 5
                    background "#ff7f00"
                    hover_background "#ff9f40"
                    text "{color=#000}[p+1]{/color}" style "gallery_page_number"
                    action SetVariable("gallery_page", p)
            else:
                button:
                    xpadding 10
                    ypadding 5
                    background "#fff8"
                    hover_background "#fffa"
                    text "{color=#000}[p+1]{/color}" style "gallery_page_number"
                    action SetVariable("gallery_page", p)

        if end_page < total_pages - 1:
            text "..." style "gallery_page_number" color "#000"

    if gallery_page > 0:
        textbutton "← Previous" style "powerup_button":
            action SetVariable("gallery_page", gallery_page - 1)
            xalign 0.15
            yalign 0.98

    if (gallery_page + 1) * maxperpage < len(filtered_items):
        textbutton "Next →" style "powerup_button":
            action SetVariable("gallery_page", gallery_page + 1)
            xalign 0.85
            yalign 0.98

    textbutton "{color=#000}Return{/color}" style "powerup_button":
        action [Hide("gallery"), ShowMenu("gallery_category_select")]
        xalign 0.018
        yalign 0.98
        background "#fff8"
        hover_background "#fffa"
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"

# -------------------------------------------------------------------------
# Closeup screen (shared)
# -------------------------------------------------------------------------
screen gallery_closeup(images):
    zorder 10
    $ height = config.screen_height
    imagebutton:
        idle Transform(images[closeup_page], ysize=height, fit="contain")
        action [SetVariable("closeup_page", 0), Hide("gallery_closeup", dissolve)]
        xalign 0.5
        yalign 0.5

# -------------------------------------------------------------------------
# Wrapper: choose locked or unlocked based on membership
# -------------------------------------------------------------------------
label show_gallery:
    if membership_active():
        show screen gallery_unlocked
    else:
        show screen gallery_locked
    return

# -------------------------------------------------------------------------
# Alias screen for compatibility
# -------------------------------------------------------------------------
screen gallery():
    use expression ("gallery_unlocked" if membership_active() else "gallery_locked")

# -------------------------------------------------------------------------
# Style definition for pagination numbers
# -------------------------------------------------------------------------
style gallery_page_number is default:
    size 20
    color "#000"
    xalign 0.5
    yalign 0.5

init python:
    def get_category_counts(category):
        """
        Returns (unlocked, total) counts for a CG gallery category.
        - If membership_active() is True → everything counts as unlocked.
        - Otherwise → only items that are not locked count as unlocked.
        """
        # Refresh lock status for all items first
        for item in gallery_items:
            item.refresh_lock()

        if membership_active():
            # Membership active → everything unlocked
            if category == "Everything":
                total = len(gallery_items)
                unlocked = total
            else:
                total = sum(1 for item in gallery_items if category in item.categories)
                unlocked = total
        else:
            # Normal logic → only unlocked items count
            if category == "Everything":
                total = len(gallery_items)
                unlocked = sum(1 for item in gallery_items if not item.is_locked)
            else:
                total = sum(1 for item in gallery_items if category in item.categories)
                unlocked = sum(
                    1 for item in gallery_items
                    if category in item.categories and not item.is_locked
                )

        return unlocked, total