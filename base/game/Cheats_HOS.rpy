
# =========================
# Defaults & Variables
# =========================
default sequence_timer_hack = False
default score_multiplier_hack = False
default arrow_cheat_mode = False  # False = random arrows, True = all ↑
default auto_shift_mode = False

default cheat_error    = ""
define detail_inputs  = {}

# Extra colors for other stats
default dominancecolor = "#FF0000"  # or whatever color you want
default respectcolor        = "#1e90ff"  # Respect = blue
default lovelevelcolor      = "#ff85d4"  # Love Level = lighter pink
default obediencelevelcolor = "#c29fff"  # Obedience Level = lighter purple
default hatredlevelcolor    = "#ff4d4d"  # Hatred Level = brighter red
default strengthpointscolor = "#ffa500"  # Strength Points = orange
default strengthlevelcolor  = "#ffcc66"  # Strength Level = gold
default lustcolor           = "#ff1493"  # Lust = deep pink
default relationshipcolor   = "#00ced1"  # Relationship = teal
default trustcolor          = "#87cefa"  # Trust = light blue

# Ramen shop & navigation
default shiftshackcolor   = "#FFD700"  # Gold for work/money
default backmenucolor     = "#87cefa"  # Light blue for navigation
default toggleoncolor  = "#32CD32"  # Lime green for ON
default toggleoffcolor = "#B22222"  # Firebrick red for OFF

init python:
    # Text inside the button
    style.cheat_button_text.bold = True
    style.cheat_button_text.italic = True

    # Make all navigation button text bold + italic
    style.navigation_button_text.bold = True
    style.navigation_button_text.italic = True

    # YouTube button style
    style.Karim_youtube = Style(style.navigation_button)
    style.Karim_youtube_text = Style(style.navigation_button_text)
    style.Karim_youtube_text.color = "#FF0000"       # YouTube red
    style.Karim_youtube_text.hover_color = "#ff6666" # lighter red glow

    # Patreon button style
    style.Karim_patreon = Style(style.navigation_button)
    style.Karim_patreon_text = Style(style.navigation_button_text)
    style.Karim_patreon_text.color = "#FF424D"       # Patreon pink/red
    style.Karim_patreon_text.hover_color = "#ff7a85" # lighter glow

    # Discord button style
    style.Karim_discord = Style(style.navigation_button)
    style.Karim_discord_text = Style(style.navigation_button_text)
    style.Karim_discord_text.color = "#5865F2"       # Discord blurple
    style.Karim_discord_text.hover_color = "#8892ff" # lighter glow

    # Telegram button style
    style.Karim_telegram = Style(style.navigation_button)
    style.Karim_telegram_text = Style(style.navigation_button_text)
    style.Karim_telegram_text.color = "#229ED9"      # Telegram blue
    style.Karim_telegram_text.hover_color = "#66cfff" # lighter glow
  
    # Style for the Unlock button container (same as other nav buttons)
    style.Karim_unlock = Style(style.navigation_button)

    # Style for the Unlock button text (matches Gaming Mods membership style)
    style.Karim_unlock_text = Style(style.navigation_button_text)
    style.Karim_unlock_text.color = "#FFD700"       # Gold like Gaming Mods
    style.Karim_unlock_text.hover_color = "#ffea8a" # lighter gold on hover
    style.Karim_unlock_text.bold = True
    style.Karim_unlock_text.italic = True


init -999 python:
    # Define hashbase to prevent crash in version_updates.rpy
    if 'hashbase' not in globals():
        hashbase = "Gaming Mods"  # Or whatever version string you want to use
        renpy.log("✅ hashbase defined by Karim")

# 🛠 Enable developer console
init -2 python:
    config.console   = True


screen cheats_overlay():
    zorder 200  # Always on top

    frame:
        background None
        padding (20, 20)
        xpos 1.0
        ypos 1.0
        xanchor 1.0
        yanchor 1.0

        textbutton "CHEATS":
            style "cheat_button"
            text_color "#e67e22"
            action Show("cheat_menu")



##  Helpers

init python:
    def safe_int(s):
        """
        Safely parse an integer from any input.
        Returns None if parsing fails.
        """
        try:
            return int(str(s).strip())
        except Exception:
            return None


##  Python logic

init python:
    def apply_var_change(varname, amount_raw):
        amt = safe_int(amount_raw)
        if amt is None:
            store.cheat_error = "Enter an integer."
            return

        cur = getattr(store, varname, 0)

        # Numbers: handle directly
        if isinstance(cur, (int, float)):
            setattr(store, varname, cur + amt)
            return

        # Stat-like objects
        if hasattr(cur, "value"):
            cur.value += amt
            return

        # DynamicStatLevel-like objects
        if hasattr(cur, "level"):
            cur.level += amt
            return

        # Fallback: try += if the object supports it
        try:
            cur += amt
        except Exception as e:
            store.cheat_error = f"Cannot edit {varname}: {type(cur)} → {e}"


##  Error Popup

screen cheat_error_popup():
    zorder 300
    if cheat_error:
        frame:
            style_prefix "say"
            xalign 0.5 yalign 0.1
            text "[cheat_error]" color "#ff4444" size 28
        timer 2.5 action SetVariable("cheat_error", "")


# At the top of your script (before any use of diotrust), set the default:

########################################################################
# Quick Menu → Cheat Menu
########################################################################

screen cheat_menu():
    tag cheat
    modal True
    zorder 201

    frame:
        xalign 1.0 yalign 0.0
        xsize 300 yfill True
        background "#0008"
        padding (20, 20)

        vbox:
            spacing 16

            text "Cheat Menu" size 28 color "#fff" xalign 0.5

            textbutton "Boruto":
                style "cheat_button"
                text_color "#1E90FF"
                action [Hide("cheat_menu"), Show("character_stats", character="Boruto")]

            textbutton "Hinata":
                style "cheat_button"
                text_color hin_color
                action [Hide("cheat_menu"), Show("character_stats", character="Hinata")]

            textbutton "Himawari":
                style "cheat_button"
                text_color him_color
                action [Hide("cheat_menu"), Show("character_stats", character="Himawari")]

            textbutton "Tsunade":
                style "cheat_button"
                text_color "#FFBB33"
                action [Hide("cheat_menu"), Show("character_stats", character="Tsunade")]

            textbutton "Sakura":
                style "cheat_button"
                text_color "#ffb7c5"
                action [Hide("cheat_menu"), Show("character_stats", character="Sakura")]

            textbutton "Sarada":
                style "cheat_button"
                text_color "#8B0000"
                action [Hide("cheat_menu"), Show("character_stats", character="Sarada")]

            textbutton "Dio":
                style "cheat_button"
                text_color "#C0C0C0"
                action [Hide("cheat_menu"), Show("character_stats", character="Dio")]

            textbutton "Ramen Shop":
                style "cheat_button"
                text_color "#FF8C00"
                action [Hide("cheat_menu"), Show("ramen_shop_screen")]

            null height 12

            textbutton "Close":
                style "cheat_button"
                action Hide("cheat_menu")
                xalign 0.5


########################################################################
# Character → Stats List (with Dio + colors)
########################################################################

screen character_stats(character):
    tag cheat
    modal True
    zorder 200
    use cheat_error_popup

    frame:
        xalign 1.0 yalign 0.0
        xsize 300 yfill True
        background "#000a"
        padding (20, 20)

        vbox:
            spacing 12

            text "[character] Cheats" size 32 color "#fff" xalign 0.5

            if character in ["Hinata", "Himawari"]:
                $ name = character.lower()
                $ stats = [
                    (f"{name}_respect",     "Respect", respectcolor),
                    (f"{name}_love",        "Love", lovecolor),
                    (f"{name}_obedience",   "Obedience", obediencecolor),
                    (f"{name}_love_level",     "Love Level", lovelevelcolor),
                    (f"{name}_obedience_level","Obedience Level", obediencelevelcolor),
                ]
            elif character == "Boruto":
                $ stats = [
                    ("money",     "Money", moneycolor),
                    ("hatred",    "Hatred", hatredcolor),
                    ("hatred_level", "Hatred Level", hatredlevelcolor),
                    ("strengthlevel","Strength Points", strengthpointscolor),
                    ("strength",  "Strength Level", strengthlevelcolor),
                    ("dominance", "Dominance", dominancecolor),
                    ("dominance_level", "Dominance Level", dominancecolor),
                    ("percentage",    "Lust", lustcolor),
                ]
            elif character == "Sakura":
                $ stats = [
                    ("sakura_relationship", "Relationship", relationshipcolor),
                ]
            elif character == "Sarada":
                $ stats = [
                    ("sarada_relationship", "Relationship", relationshipcolor),
                ]
            elif character == "Dio":
                $ stats = [
                    ("diotrust", "Trust", trustcolor),
                ]
            else:
                $ stats = [("tsunadedominance", "Dominance", dominancecolor)]

            for varname, label, col in stats:
                textbutton label:
                    style "cheat_button"
                    text_color col
                    action [
                        Hide("character_stats"),
                        Show("stat_detail", varname=varname, label=label, character=character)
                    ]

            null height 20

            textbutton "Back to Menu" style "cheat_button" action [
                Hide("character_stats"),
                Show("cheat_menu")
            ] xalign 0.5


########################################################################
# Stat Detail (+ / – plus free‐form input)
########################################################################


screen stat_detail(varname, label, character):
    tag cheat
    modal True
    zorder 200

    use cheat_error_popup

    $ detail_inputs.setdefault(varname, "")

    frame:
        xalign 0.5
        yalign 0.10
        xsize 350
        background "#0010"
        padding (20, 20)

        vbox:
            spacing 16

            # Show current value (handles Stat, DynamicStatLevel, or number)
            $ cur_val = getattr(renpy.store, varname, 0)
            if hasattr(cur_val, "value"):
                $ display_val = cur_val.value
            elif hasattr(cur_val, "level"):
                $ display_val = cur_val.level
            elif isinstance(cur_val, (int, float)):
                $ display_val = cur_val
            else:
                $ display_val = "❌ Unsupported"

            text f"{label} (Current: {display_val})" size 24 color "#fff" xalign 0.5

            # Free‐form input + Apply
            hbox:
                spacing 8

                input:
                    id "input_" + varname
                    value DictInputValue(detail_inputs, varname)
                    length 6
                    allow "-0123456789"
                    xsize 100

                textbutton "Apply" style "cheat_button" action Function(
                    apply_var_change_safe, varname, detail_inputs.get(varname, ""), label
                )

            # + / – / Back row
            hbox:
                spacing 12
                textbutton "+" style "cheat_button" action Function(apply_var_change_safe, varname, "1", label)
                textbutton "–" style "cheat_button" action Function(apply_var_change_safe, varname, "-1", label)
                textbutton f"Back to {character}" style "cheat_button" action [
                    Hide("stat_detail"),
                    Show("character_stats", character=character)
                ]


########################################################################
# Safe stat change function (handles Stat, DynamicStatLevel, and numbers)
########################################################################

init python:
    def apply_var_change_safe(varname, amount_str, label=None):
        amt = safe_int(amount_str)
        if amt is None:
            renpy.notify("❌ Invalid input: must be a number.")
            return

        cur = getattr(renpy.store, varname, 0)

        # Case 1: Plain number
        if isinstance(cur, (int, float)):
            new_val = cur + amt
            setattr(renpy.store, varname, new_val)
            renpy.notify(f"{label or varname} → {new_val}")
            return

        # Case 2: Stat-like object with a .value property
        if hasattr(cur, "value"):
            cur.value += amt
            # Optional clamp to avoid negatives on value fields
            if cur.value < 0:
                cur.value = 0
            renpy.notify(f"{label or varname} → {cur.value}")
            return

        # Case 3: DynamicStatLevel-like object with a .level property
        if hasattr(cur, "level"):
            try:
                cur.level += amt
                renpy.notify(f"{label or varname} → {cur.level}")
            except Exception as e:
                renpy.notify(f"⚠️ Cannot edit {varname}: {type(cur)} → {e}")
            return

        # Case 4: Fallback — try += if supported
        try:
            cur += amt
            renpy.notify(f"{label or varname} → {cur}")
        except Exception as e:
            renpy.notify(f"⚠️ Cannot edit {varname}: {type(cur)} → {e}")



# =========================
# Calculation & Sequence Functions
# =========================
init python:
    import random

    def generate_sequence(length):
        if arrow_cheat_mode:
            return ['↑'] * length
        else:
            directions = ['↑', '↓', '←', '→']
            return [random.choice(directions) for _ in range(length)]


# =========================
# Main Ramen Shop Screen
# =========================
screen ramen_shop_screen():
    tag cheat
    modal True
    zorder 200
    use cheat_error_popup

    frame:
        xalign 1.0 yalign 0.0
        xsize 300 yfill True
        background "#000a"
        padding (20, 20)

        vbox:
            spacing 12

            text "Ramen Shop Cheats" size 32 color "#fff" xalign 0.5

            textbutton "Shifts Hack":
                style "cheat_button"
                text_color shiftshackcolor
                action [Hide("ramen_shop_screen"), Show("shifts_hack_screen")]

            textbutton "Yoruichi Relationship":
                style "cheat_button"
                text_color relationshipcolor
                action [Hide("ramen_shop_screen"), Show("yoruichi_relationship_screen")]

            null height 20

            textbutton "Back to Menu":
                style "cheat_button"
                text_color backmenucolor
                action [Hide("ramen_shop_screen"), Show("cheat_menu")]
                xalign 0.5
# =========================
# Shifts Hack Screen
# =========================
screen shifts_hack_screen():
    tag cheat
    modal True
    zorder 200
    use cheat_error_popup

    frame:
        xalign 1.0 yalign 0.0
        xsize 300 yfill True
        background "#000a"
        padding (20, 20)

        vbox:
            spacing 12

            text "Shifts Hack" size 32 color "#fff" xalign 0.5

            viewport:
                draggable True
                mousewheel True
                ymaximum 400

                vbox:
                    spacing 8

                    # Arrow Cheat Mode
                    textbutton ("Arrow Cheat Mode: [arrow_cheat_mode and 'ON' or 'OFF']"):
                        style "cheat_button"
                        text_color (toggleoncolor if arrow_cheat_mode else toggleoffcolor)
                        action ToggleVariable("arrow_cheat_mode")

                    # Auto Shift Mode
                    textbutton ("Auto Shift: [auto_shift_mode and 'ON' or 'OFF']"):
                        style "cheat_button"
                        text_color (toggleoncolor if auto_shift_mode else toggleoffcolor)
                        action ToggleVariable("auto_shift_mode")

            null height 20

            textbutton "Back to Ramen Shop":
                style "cheat_button"
                action [Hide("shifts_hack_screen"), Show("ramen_shop_screen")]
                xalign 0.5
# =========================
# Yoruichi Relationship Screen
# =========================
screen yoruichi_relationship_screen():
    tag cheat
    modal True
    zorder 200
    use cheat_error_popup

    frame:
        xalign 1.0 yalign 0.0
        xsize 300 yfill True
        background "#000a"
        padding (20, 20)

        vbox:
            spacing 12

            text "Current: [yoruichi_relationship]" size 24 color relationship_colors[yoruichi_relationship] xalign 0.5

            viewport:
                draggable True
                mousewheel True
                ymaximum 400

                vbox:
                    spacing 8

                    for rel, col in relationship_colors.items():
                        textbutton rel:
                            style "cheat_button"
                            text_color col
                            action SetVariable("yoruichi_relationship", rel)

                    if yoruichi_relationship == "Passive":
                        $ current_objectives = yoruichi_objectives_passive
                    elif yoruichi_relationship == "Formal":
                        $ current_objectives = yoruichi_objectives_formal
                    elif yoruichi_relationship == "Apprehensive":
                        $ current_objectives = yoruichi_objectives_apprehensive
                    else:
                        $ current_objectives = []

                    if current_objectives:
                        text "Objectives:" size 18 color "#fff"
                        for obj in current_objectives:
                            text ("✓ " if obj["completed"] else "✗ ") + obj["description"] size 16 color "#ccc"

            null height 20
            textbutton "Back to Ramen Shop" style "cheat_button" action [Hide("yoruichi_relationship_screen"), Show("ramen_shop_screen")] xalign 0.5



##  Styles

style cheat_button:
    background "#444"
    hover_background "#666"
    padding (6, 4)
    size 20
    color "#fff"
    bold True


define gm = Character(
    "Gaming Mods",
    color="#FFD700",            # golden name
    what_color="#FFF8DC",       # softer golden for dialogue text
    ctc="ctc_arrowblink",       # same click-to-continue indicator as Dev
    who_style="gm_name"         # custom style for the name
)

init python:
    style.gm_name = Style(style.say_label)   # base it on the default name style
    style.gm_name.color = "#FFD700"          # bright gold
    style.gm_name.outlines = [
        (2, "#B8860B", 0, 0)                 # darker golden glow outline
    ]
default paypal_url = "https://paypal.me/KarimMoubarak0"

init python:
    style.gm_flair_big = Style(style.default)
    style.gm_flair_big.color = "#FFD700"
    style.gm_flair_big.outlines = [(3, "#B8860B", 0, 0)]
    style.gm_flair_big.bold = True
    style.gm_flair_big.italic = True
    style.gm_flair_big.size = 42

    style.gm_flair_mid = Style(style.default)
    style.gm_flair_mid.color = "#FFD700"
    style.gm_flair_mid.outlines = [(2, "#B8860B", 0, 0)]
    style.gm_flair_big.italic = True
    style.gm_flair_mid.bold = True
    style.gm_flair_mid.size = 28

    style.gm_flair_soft = Style(style.default)
    style.gm_flair_soft.color = "#FFD700"
    style.gm_flair_soft.outlines = [(1, "#B8860B", 0, 0)]
    style.gm_flair_soft.bold = True
    style.gm_flair_soft.italic = True
    style.gm_flair_soft.size = 24

transform activate_glow:
    on idle:
        linear 0.3 alpha 0.8
    on hover:
        linear 0.2 alpha 1.0
    on selected_idle:
        linear 0.3 alpha 0.9
    on selected_hover:
        linear 0.2 alpha 1.0
    # You can also add effects like zoom or color tint here
screen displayTextScreen2(displayText=""):
    frame:
        background "#0008"
        padding (10, 10)
        text displayText color "#FFF" size 20
screen displayTextScreen3(displayText=""):
    frame:
        background "#0008"
        padding (10, 10)
        text displayText color "#FFF" size 20
define config.developer = False


define config.name = "House Of Shinobi"        # Display name shown on device
define build.name = "HoS"                      # Internal short name (no spaces)
define build.package = "com.gamingmods.hos"    # Unique bundle ID for iOS
