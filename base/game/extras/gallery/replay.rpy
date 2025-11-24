## replay_gallery.rpy
## Membership‑aware Replay Gallery

default replay_page = 0
default current_replay_category = "Everything"

# -------------------------------------------------------------------------
# Exit button during replays (optional)
# -------------------------------------------------------------------------
screen Replayexit():
    zorder 100
    imagebutton auto "images/replay/exit_%s.png" action EndReplay() yalign .99 xalign .99
    # Requires exit_idle.png and exit_hover.png in images/replay/

# -------------------------------------------------------------------------
# Locked Replay Gallery (non-members)
# -------------------------------------------------------------------------
screen replay_gallery_locked():
    tag menu
    add "black"

    $ filtered_items = [item for item in Replay_items if current_replay_category == "Everything" or current_replay_category in item.categories]
    $ start = replay_page * maxperpage
    $ end = min(start + maxperpage - 1, len(filtered_items) - 1)

    grid maxnumx maxnumy:
        xfill True
        yfill True

        for i in range(start, end + 1):
            $ item = filtered_items[i]
            $ thumb_path = item.thumbs[0] if hasattr(item, 'thumbs') and item.thumbs else "images/characters/kurama/kurama2.webp"

            if renpy.seen_label(item.replay) or (hasattr(persistent, 'unlocked_replay_items') and persistent.unlocked_replay_items and item.replay in persistent.unlocked_replay_items):
                imagebutton:
                    idle Transform(thumb_path, size=(379, 180))
                    action Replay(item.replay, locked=False)
                    xalign 0.5
                    yalign 0.0
                    style "gallery_button"
                    hovered Show("displayTextScreen", displayText=item.get_tooltip())
                    unhovered Hide("displayTextScreen")
            else:
                imagebutton:
                    idle Transform(
                        Composite(
                            (379, 180),
                            (0, 0), Transform(thumb_path, blur=50.0, matrixcolor=BrightnessMatrix(-0.5), size=(379, 180)),
                            (139, 40), Transform("images/locktransparent.png", size=(100, 100))
                        ),
                        size=(379, 180)
                    )
                    action NullAction()
                    xalign 0.5
                    yalign 0.0
                    style "gallery_button"
                    hovered Show("displayTextScreen", displayText=item.get_tooltip())
                    unhovered Hide("displayTextScreen")

        for i in range(end - start + 1, maxperpage):
            null

    use replay_gallery_footer(filtered_items)

    # Full‑screen membership message for non‑members
    frame:
        xalign 0.5
        yalign 0.5
        background "#0008"
        padding (30, 30)
        text "❌ If you wish for unlocked replays, verify your membership by clicking on Unlock Cheats and adding your Discord ID.":
            size 28
            color "#FFF"
            xalign 0.5
            text_align 0.5

# -------------------------------------------------------------------------
# Unlocked Replay Gallery (Gaming Mods / YouTube Subscriber)
# -------------------------------------------------------------------------
screen replay_gallery_unlocked():
    tag menu
    add "black"

    $ filtered_items = [item for item in Replay_items if current_replay_category == "Everything" or current_replay_category in item.categories]
    $ start = replay_page * maxperpage
    $ end = min(start + maxperpage - 1, len(filtered_items) - 1)

    grid maxnumx maxnumy:
        xfill True
        yfill True

        for i in range(start, end + 1):
            $ item = filtered_items[i]
            $ thumb_path = item.thumbs[0] if hasattr(item, 'thumbs') and item.thumbs else "images/characters/kurama/kurama2.webp"

            imagebutton:
                idle Transform(thumb_path, size=(379, 180))
                action Replay(item.replay, locked=False)
                xalign 0.5
                yalign 0.0
                style "gallery_button"
                hovered Show("displayTextScreen", displayText=item.get_tooltip())
                unhovered Hide("displayTextScreen")

        for i in range(end - start + 1, maxperpage):
            null

    use replay_gallery_footer(filtered_items)

    # Full‑screen membership message for verified members
    frame:
        xalign 0.5
        yalign 0.5
        background "#0008"
        padding (30, 30)
        text "✅ Membership Verified — Have fun with the unlocked replays!":
            size 28
            color "#FFD700"
            xalign 0.5
            text_align 0.5

# -------------------------------------------------------------------------
# Shared footer (pagination + navigation)
# -------------------------------------------------------------------------
screen replay_gallery_footer(filtered_items):
    $ start = replay_page * maxperpage
    $ end = min(start + maxperpage, len(filtered_items))
    $ shown = end - start

    # Info grid
    grid maxnumx maxnumy:
        xfill True
        yfill True
        for i in range(start, end):
            $ item = filtered_items[i]
            hbox:
                style_prefix "name"
                spacing maxthumbx - 20
                xalign 0.5
                yalign 0.1
                text item.name
        for i in range(shown, maxperpage):
            null

    # Pagination
    hbox:
        spacing 10
        xalign 0.5
        yalign 0.98

        $ total_pages = max(1, (len(filtered_items) + maxperpage - 1) // maxperpage)
        $ start_page = max(0, replay_page - 5)
        $ end_page = min(total_pages - 1, replay_page + 5)

        if start_page > 0:
            text "..." style "gallery_page_number" color "#000"

        for p in range(start_page, end_page + 1):
            $ is_current = p == replay_page
            if is_current:
                button:
                    xpadding 10
                    ypadding 5
                    background "#ff7f00"
                    hover_background "#ff9f40"
                    text "{color=#000}[p+1]{/color}" style "gallery_page_number"
                    action SetVariable("replay_page", p)
            else:
                button:
                    xpadding 10
                    ypadding 5
                    background "#fff8"
                    hover_background "#fffa"
                    text "{color=#000}[p+1]{/color}" style "gallery_page_number"
                    action SetVariable("replay_page", p)

        if end_page < total_pages - 1:
            text "..." style "gallery_page_number" color "#000"

    #previous, next, and return buttons
    if replay_page > 0:
        textbutton "{color=#000}← Previous{/color}" style "powerup_button":
            action SetVariable("replay_page", replay_page - 1)
            xalign 0.15
            yalign 0.98
            hover_background "#fffa"
            background "#fff8"
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"

    if (replay_page + 1) * maxperpage < len(filtered_items):
        textbutton "{color=#000}Next →{/color}" style "powerup_button":
            action SetVariable("replay_page", replay_page + 1)
            xalign 0.85
            yalign 0.98
            background "#fff8"
            hover_background "#fffa"
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"

    textbutton "{color=#000}Return{/color}" style "powerup_button":
        action [Hide("replay_gallery"), ShowMenu("replay_category_select")]
        xalign 0.018
        yalign 0.98
        background "#fff8"
        hover_background "#fffa"
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"

# -------------------------------------------------------------------------
# Wrapper: choose locked or unlocked based on membership
# -------------------------------------------------------------------------
label show_replay_gallery:
    if membership_active():
        show screen replay_gallery_unlocked
    else:
        show screen replay_gallery_locked
    return

init python:
    def get_replay_category_counts(category):
        """
        Returns (unlocked, total) counts for a replay category.
        - If membership_active() is True → everything counts as unlocked.
        - Otherwise → only labels actually seen count as unlocked.
        """
        if membership_active():
            if category == "Everything":
                total = len(Replay_items)
                unlocked = total
            else:
                total = sum(1 for item in Replay_items if category in item.categories)
                unlocked = total
        else:
            if category == "Everything":
                total = len(Replay_items)
                unlocked = sum(1 for item in Replay_items if renpy.seen_label(item.replay))
            else:
                total = sum(1 for item in Replay_items if category in item.categories)
                unlocked = sum(
                    1 for item in Replay_items
                    if category in item.categories and renpy.seen_label(item.replay)
                )
        return unlocked, total

# -------------------------------------------------------------------------
# Alias screen for compatibility
# -------------------------------------------------------------------------
screen replay_gallery():
    use expression ("replay_gallery_unlocked" if membership_active() else "replay_gallery_locked")

# -------------------------------------------------------------------------
# Style definition for pagination numbers
# -------------------------------------------------------------------------
style gallery_page_number is default:
    size 20
    color "#000"
    xalign 0.5
    yalign 0.5