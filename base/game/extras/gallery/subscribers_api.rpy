# subscribers_api.rpy
# Drop this into game/extras/gallery/
# Key-only verification with a client-side, clock-tamper resistant timer.
# Uses time.monotonic() (steady, not affected by manual clock changes).

init python:
    import time, ssl, json, certifi
    from urllib.request import Request, urlopen
    from urllib.error   import HTTPError, URLError
    from urllib.parse   import quote

    # 24h activation duration (no backend edit required)
    ACTIVATION_DURATION = 24 * 60 * 60

    # Backend endpoint (must match app.py routes)
    KEY_STATUS_URL_BASE = "https://verifier.gaming-mods.com/validate_key"

    # Persistent fields
    if not hasattr(persistent, "entered_key"):
        persistent.entered_key = ""
    if not hasattr(persistent, "current_activation"):
        persistent.current_activation = "Free"

    # Monotonic-based activation fields (new)
    # activation_monotonic_start: local monotonic timestamp when activation began
    # activation_duration: seconds of access granted (default 24h)
    if not hasattr(persistent, "activation_monotonic_start"):
        persistent.activation_monotonic_start = None
    if not hasattr(persistent, "activation_duration"):
        persistent.activation_duration = ACTIVATION_DURATION

    # API response buffer
    key_response = {"ok": False, "valid": False, "message": ""}

    # -------- Clock-tamper resistant membership check --------
    #
    # We measure elapsed time using time.monotonic(), which ignores changes
    # to the wall-clock (system date/time). This prevents simple clock rollback tricks.
    #
    def membership_active():
        mstart = persistent.activation_monotonic_start
        if mstart is None:
            return False
        elapsed = time.monotonic() - mstart
        return (
            elapsed < (persistent.activation_duration or ACTIVATION_DURATION)
            and persistent.current_activation == "YouTubeSubscriber"
        )

    def membership_remaining_seconds():
        mstart = persistent.activation_monotonic_start
        if mstart is None:
            return 0
        elapsed = time.monotonic() - mstart
        duration = persistent.activation_duration or ACTIVATION_DURATION
        remaining = int(duration - elapsed)
        return max(0, remaining)

    def inject_cheats_overlay():
        if membership_active():
            if "cheats_overlay" not in config.overlay_screens:
                config.overlay_screens.append("cheats_overlay")
        else:
            if "cheats_overlay" in config.overlay_screens:
                config.overlay_screens.remove("cheats_overlay")
                renpy.notify("⛔ Cheats expired. Re‑verify to unlock again.")

    # Initial overlay state at startup
    inject_cheats_overlay()

    # ---------- Key validation (24h activation) ----------

    def check_generated_key():
        global key_response
        entered_key = (persistent.entered_key or "").strip()

        if not entered_key:
            renpy.show_screen("subscription_confirmation_screen",
                              message="❌ Please paste your generated key.")
            return

        key_response = {"ok": False, "valid": False, "message": ""}
        renpy.show_screen("loading_indicator")
        renpy.invoke_in_thread(make_key_request)

    def make_key_request():
        global key_response
        try:
            ctx  = ssl.create_default_context(cafile=certifi.where())
            key  = quote((persistent.entered_key or "").strip(), safe="")
            url  = KEY_STATUS_URL_BASE + "/" + key
            req  = Request(url, headers={"User-Agent": "RenPy-Client", "Accept": "application/json"})
            resp = urlopen(req, timeout=15, context=ctx)
            data = json.loads(resp.read().decode())

            # Backend returns {"ok": true/false, "valid": true/false, "message": "..."}
            key_response["ok"]     = bool(data.get("ok"))
            key_response["valid"]  = bool(data.get("valid"))
            key_response["message"]= data.get("message", "") or ""

        except HTTPError as e:
            if e.code == 410:
                key_response = {"ok": False, "valid": False, "message": "Key expired. Request a new one."}
            elif e.code == 400:
                key_response = {"ok": False, "valid": False, "message": "Invalid or unknown key."}
            else:
                key_response = {"ok": False, "valid": False, "message": "HTTP {}".format(e.code)}
        except URLError:
            key_response = {"ok": False, "valid": False, "message": "No internet connection."}
        except Exception as e:
            key_response = {"ok": False, "valid": False, "message": "Key check error: {}".format(e)}

        renpy.invoke_in_main_thread(handle_key_response)

    def handle_key_response():
        renpy.hide_screen("loading_indicator")
        if key_response.get("ok") and key_response.get("valid"):
            # Start the 24h countdown anchored to monotonic time
            persistent.current_activation = "YouTubeSubscriber"
            persistent.activation_monotonic_start = time.monotonic()
            persistent.activation_duration = ACTIVATION_DURATION

            inject_cheats_overlay()

            # Show success with remaining time
            remaining = membership_remaining_seconds()
            hours   = remaining // 3600
            minutes = (remaining % 3600) // 60
            seconds = remaining % 60
            renpy.show_screen(
                "subscription_confirmation_screen",
                message=f"✅ Key accepted. Cheats unlocked for {hours:02d}:{minutes:02d}:{seconds:02d}!"
            )
        else:
            msg = key_response.get("message") or "❌ Invalid or expired key."
            renpy.show_screen("subscription_confirmation_screen", message=msg)


# ────────────────────────────────────────────
# Screens
# ────────────────────────────────────────────
transform loading_bounce:
    yoffset 0
    ease 0.8 yoffset -10
    ease 0.8 yoffset 0
    repeat

screen loading_indicator():
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        padding (30, 30)
        vbox:
            spacing 10
            text "Checking key status…" style "gui_text" xalign 0.5
            text "Please wait…" style "gui_text" xalign 0.5 at loading_bounce
            textbutton "Cancel" action Hide("loading_indicator") xalign 0.5

screen subscription_confirmation_screen(message=""):
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        padding (20, 20)
        vbox:
            spacing 20
            text "[message]" style "gui_text" xalign 0.5
            textbutton "OK" action Hide("subscription_confirmation_screen") xalign 0.5


# ────────────────────────────────────────────
# Prompt
# ────────────────────────────────────────────
label ask_generated_key:
    $ entered_key = renpy.input(
        "Paste your generated key:",
        default=(persistent.entered_key or ""),
        length=120
    )
    $ entered_key = (entered_key or "").strip()
    if entered_key:
        $ persistent.entered_key = entered_key
        $ check_generated_key()
    return


# ────────────────────────────────────────────
# Navigation screen (with monotonic countdown + unlock)
# ────────────────────────────────────────────
init 999:
    screen navigation():

        use languagepacks_update

        vbox:
            at nav_dissolve
            style_prefix "navigation"

            xpos gui.navigation_xpos
            yalign 0.5
            spacing gui.navigation_spacing

            if main_menu:
                textbutton _("Start") action Start()
            else:
                textbutton _("History") action ShowMenu("history")
                textbutton _("Save") action ShowMenu("save")

            textbutton _("Load") action ShowMenu("load")
            textbutton _("Gallery") action ShowMenu("gallery_category_select")

            if main_menu:
                textbutton _("Replay Scenes") action ShowMenu("replay_category_select")

            textbutton _("YouTube") action OpenURL("http://www.youtube.com/@GamingNewbie2007") style "Karim_youtube"
            textbutton _("Discord") action OpenURL("https://discord.com/invite/RM64pBbbpE") style "Karim_discord"

            # Membership countdown (monotonic-based)
            python:
                active = membership_active()
                if active:
                    remaining = membership_remaining_seconds()
                    hours   = remaining // 3600
                    minutes = (remaining % 3600) // 60
                    seconds = remaining % 60
                    timer_text = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

            if active:
                frame:
                    background None
                    has vbox
                    text timer_text style "Karim_unlock_text" xalign 0.5
                    # Update every second and enforce overlay state
                    timer 1.0 action [Function(inject_cheats_overlay), Function(renpy.restart_interaction)]
            else:
                vbox:
                    spacing 10
                    textbutton _("Unlock Cheats"):
                        style "Karim_unlock"
                        text_style "Karim_unlock_text"
                        action Function(lambda: renpy.call_in_new_context("ask_generated_key"))

            textbutton _("Preferences") action ShowMenu("preferences")

            if _in_replay:
                textbutton _("End Replay") action EndReplay(confirm=True)
            elif not main_menu:
                textbutton _("Main Menu") action MainMenu()

            textbutton _("About") action ShowMenu("about")

            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
                textbutton _("Help") action ShowMenu("help")

            if renpy.variant("pc"):
                textbutton _("Quit") action Quit(confirm=not main_menu)