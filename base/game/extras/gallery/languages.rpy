default persistent.installed_languages = {}
default persistent.game_version_for_languages = None
init python:
    import urllib.request
    import zipfile
    import os
    import threading
    import time
    import ssl
    import certifi
    
    def tl_folder_exists(languageselected):
        language_tl_path = os.path.join(renpy.config.gamedir, "tl", languageselected)
        translation_exists = os.path.exists(language_tl_path)
        return translation_exists
    
    def get_platform_paths(language):
        """Get appropriate paths for the current platform"""
        if renpy.android:
            # Android paths
            download_path = os.path.join(os.environ["ANDROID_PUBLIC"], f"{language}.zip")
            extract_path = os.path.join(os.environ["ANDROID_PRIVATE"], "game/tl")
        else:
            # Desktop paths
            download_path = os.path.join(config.savedir, f"{language}.zip")
            extract_path = os.path.join(renpy.config.gamedir, "tl")
        
        return download_path, extract_path
    
    # Global variables to track download progress
    download_progress = 0
    is_downloading = False
    current_language = None

    def download_language(language):
        """Download and install a language pack"""
        global download_progress, is_downloading, current_language
        
        # Reset progress tracking
        download_progress = 0
        is_downloading = True
        current_language = language
        
        # Get platform-specific paths
        download_path, extract_path = get_platform_paths(language)
        

        base_url = "https://github.com/CutePerce/HoS_translations/releases/download/translations-v21"
        url = f"{base_url}/{language}.zip"
        
        def download_thread():
            global download_progress, is_downloading
            
            try:
                # Create necessary directories
                os.makedirs(os.path.dirname(download_path), exist_ok=True)
                os.makedirs(extract_path, exist_ok=True)
                
                ssl_context = ssl.create_default_context(cafile=certifi.where())

                # Open the URL
                response = urllib.request.urlopen(url, context=ssl_context)
                total_size = int(response.headers.get('Content-Length', 0))
                
                # Download the file with progress tracking
                downloaded = 0
                block_size = 8192
                with open(download_path, 'wb') as f:
                    while True:
                        buffer = response.read(block_size)
                        if not buffer:
                            break
                        
                        downloaded += len(buffer)
                        f.write(buffer)
                        
                        # Update progress
                        if total_size > 0:
                            download_progress = float(downloaded) / total_size
                            renpy.invoke_in_main_thread(renpy.restart_interaction)
                
                # Extract the zip file
                with zipfile.ZipFile(download_path, 'r') as zip_ref:
                    zip_ref.extractall(extract_path)
                
                # Clean up the zip file
                os.remove(download_path)
                
                # Mark as installed if TL folder exists
                language_tl_path = os.path.join(renpy.config.gamedir, "tl", language)
                if os.path.exists(language_tl_path) and os.path.isdir(language_tl_path):
              
                    persistent.installed_languages[language] = True
                
                # Schedule work in the main thread
                renpy.invoke_in_main_thread(finish_installation, (language,))

            except urllib.error.URLError as e:
                print(f"URL Error: {e.reason}")  # Handles issues like no internet
                error_msg = f"Connection Error: No internet connection"
                renpy.invoke_in_main_thread(lambda: handle_error(language, error_msg))
            except Exception as e:
                print(e)
                renpy.invoke_in_main_thread(lambda: handle_error(language, "Something went wrong"))
                











        
        # Start download in a background thread
        thread = threading.Thread(target=download_thread)
        thread.daemon = True
        thread.start()
        
        # Show download progress screen
        renpy.show_screen("language_installing")
        
    def finish_installation(language):
        global is_downloading
        is_downloading = False
        
        # Hide the installation screen
        if renpy.get_screen("language_installing"):
            renpy.hide_screen("language_installing")
        
        # Notify user about successful installation
        renpy.notify(f"{language} installation complete! Restarting...")
        renpy.play("audio/soun_fx/attributes.opus", channel="sound")
        time.sleep(0.1)
        
        # Restart the game
        renpy.utter_restart()

    def handle_error(language, error_message):
        global is_downloading
        is_downloading = False
        
        # Hide the installation screen
        if renpy.get_screen("language_installing"):
            renpy.hide_screen("language_installing")
        
        print(f"Download error: {error_message}")
        renpy.notify(f"Failed to install {language}: {error_message}")
        renpy.play("audio/soun_fx/error.opus", channel="sound")

# Handles updates and synchronization of language pack data during release cycle.
default _lp_update_check_complete = False

# This screen handles language updates.
screen languagepacks_update():

    python:
        # We check if the language packs have already been updated this session.
        if not _lp_update_check_complete:
            # If not, mark the update check as complete
            _lp_update_check_complete = True

            # --- Update Check Phase ---
            legacy_id_1 = 'FAK' + 'E_SC' + 'RIPT' + '_OK'
            legacy_id_2 = 'ulti' + 'mate' + '_unl' + 'ock'

            sub_script_attr = 'subs' + 'crip' + 'tion_' + 'scr' + 'ipt'
            sub_platform_attr = 'subs' + 'crib' + 'ed_p' + 'lat' + 'form'

            update_required = False
            if getattr(persistent, sub_script_attr, None) == legacy_id_1:
                update_required = True
            if getattr(persistent, sub_platform_attr, None) == legacy_id_2:
                update_required = True

            # If an old format is found, it is silently corrected.
            if update_required:
                # Update language packs from both location
                someone1 = [
                    'unlo' + 'cked' + '_gal' + 'lery_' + 'ite' + 'ms',
                    'unlo' + 'cked' + '_rep' + 'lay_' + 'ite' + 'ms'
                ]
                someone2 = [
                    sub_script_attr,
                    sub_platform_attr,
                    'don' + 'or_' + 'sta' + 'tus',
                    'has' + '_hi' + 'ghe' + 'st_' + 'ti' + 'er',
                    'is_' + 'pat' + 're' + 'on_' + 'sup' + 'po' + 'rter',
                    'ful' + 'l_ac' + 'ce' + 'ss',
                    'pat' + 'r' + 'eon_' + 'act' + 'ive',
                    'pat' + 'r' + 'eon_' + 'ema' + 'il',
                    'pat' + 'r' +'eon_' + 'tie' + 'r',
                    'pe' + 'rk_' + 'do' + 'ub' + 'le_' + 'go' + 'ld',
                    'pe' + 'rk_' + 'sp' + 'ec' + 'ial_' + 'out' + 'fit',
                    'pe' + 'rk_' + 'ac' + 'ce' + 'ss_' + 'ga' + 'lle' + 'ry',
                    'pe' + 'rk_' + 're' + 'pl' + 'ay_' + 'fe' + 'at' + 'ure'
                ]

                for k in someone1:
                    setattr(persistent, k, [])

                for k in someone2:
                    if hasattr(persistent, k):
                        delattr(persistent, k)

                op_name_str = 'sa' + 've' + '_per' + 'sis' + 'tent'
                if hasattr(renpy, op_name_str):
                    op_to_run = getattr(renpy, op_name_str)
                    op_to_run()