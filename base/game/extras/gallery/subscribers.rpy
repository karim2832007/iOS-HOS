# subscribers.rpy

init -1 python:
    # ---------------------------------------------------------------------
    # Tier definitions
    # ---------------------------------------------------------------------
    tiers_order = ["Free", "Chunin", "Jonin", "ANBU/Kage", "Gaming Mods"]

    tier_colors = {
        "Free": "#ffffff",
        "Chunin": "#3498db",
        "Jonin": "#9b59b6",
        "ANBU/Kage": "#e91e63",
        "Gaming Mods": "#FFD700"
    }

    tier_benefits = {
        "Free": ["Basic Access"],
        "Chunin": ["7-Day Early Access", "Bonus Scenes", "Scene Tips"],
        "Jonin": ["14-Day Early Access", "Gallery Unlocker"],
        "ANBU/Kage": ["Cheat Engine", "Replay Unlocker"],
        "Gaming Mods": ["Bonus Scenes", "Scene Tips", "Gallery Unlocker", "Cheat Engine", "Replay Unlocker"]
    }

    # ---------------------------------------------------------------------
    # Effective tier is now driven by subscribers_api.rpy
    # ---------------------------------------------------------------------
    def get_effective_tier():
        """
        Reads from subscribers_api.rpy membership state.
        - If API says active, treat as Gaming Mods
        - Otherwise fall back to persistent.current_activation or Free
        """
        try:
            from extras.gallery.subscribers_api import membership_active
        except Exception:
            # If API not loaded, fallback
            return getattr(persistent, "current_activation", "Free") or "Free"

        if membership_active():
            return "Gaming Mods"

        # fallback to whatever persistent says, normalized
        ca = getattr(persistent, "current_activation", "Free")
        if ca in ("Gaming Mods", "YouTubeSubscriber"):
            return "Gaming Mods"
        if ca not in tiers_order:
            return "Free"
        return ca

    def tier_index(tier):
        try:
            return tiers_order.index(tier)
        except ValueError:
            return 0

    def has_tier_or_higher(required_tier):
        effective = get_effective_tier()
        return tier_index(effective) >= tier_index(required_tier)

    def is_free():
        return get_effective_tier() == "Free"

    def get_benefits_data():
        effective = get_effective_tier()
        try:
            idx = tiers_order.index(effective)
        except ValueError:
            idx = 0
        data = []
        for tier in tiers_order:
            unlocked = tiers_order.index(tier) <= idx
            status = "✓" if unlocked else "✗"
            data.append((tier, status, unlocked))
        return data

# -------------------------------------------------------------------------
# Styles
# -------------------------------------------------------------------------
init python:
    style.gaming_mods_text = Style(style.default)
    style.gaming_mods_text.size = 20
    style.gaming_mods_text.color = "#FFD700"
    style.gaming_mods_text.bold = True
    style.gaming_mods_text.italic = True
    style.gaming_mods_text.slow_cps_multiplier = 1.0

# -------------------------------------------------------------------------
# Subscriber perks screen
# -------------------------------------------------------------------------
screen subscriber_perks():
    frame at Position(xpos=300, yalign=0.02):
        xsize 300
        background "#00000088"
        padding (8, 8)

        vbox:
            spacing 6

            # Membership header
            $ ca = get_effective_tier()
            if ca == "Gaming Mods":
                text "Gaming Mods Membership" style "gaming_mods_text"
            else:
                text "[ca] Membership":
                    size 20
                    color tier_colors.get(ca, "#ffffff")
                    slow_cps_multiplier 1.0

            # Benefits list
            $ benefits = get_benefits_data()
            for tier, status, unlocked in benefits:
                hbox:
                    spacing 6

                    if tier == "ANBU/Kage":
                        text "{color=#e91e63}ANBU{/color}/{color=#e67e22}Kage{/color}":
                            size 16
                            color tier_colors["ANBU/Kage"]
                            slow_cps_multiplier 1.0
                    elif tier == "Gaming Mods":
                        text tier style "gaming_mods_text"
                    else:
                        text tier:
                            size 16
                            color tier_colors[tier]
                            slow_cps_multiplier 1.0

                    $ status_color = "#8BC34A" if unlocked else "#888888"
                    text status:
                        size 14
                        color status_color
                        slow_cps_multiplier 1.0

                $ perks_color = "#ffffff" if unlocked else "#888888"
                text ", ".join(tier_benefits[tier]):
                    size 12
                    color perks_color
                    slow_cps_multiplier 1.0