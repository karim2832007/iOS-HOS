transform polaroid_spin:
    subpixel True
    xalign 0.5 yalign 0.5  # Center the image
    zoom 0.1               # Start very small
    alpha 0.0              # Start invisible
    rotate 0               # Initial rotation angle
    
    parallel:
        # Fade in while growing
        easein 0.5 alpha 1.0
        easein 2.0 zoom 0.6
    
    parallel:
        # Fast spin that gradually slows down
        linear 0.1 rotate 45
        linear 0.2 rotate 90
        linear 0.3 rotate 135
        linear 0.4 rotate 180
        linear 0.5 rotate 225
        linear 0.6 rotate 270
        linear 0.7 rotate 315
        easein 0.9 rotate 340
    
    # Small bounce effect at the end
    easein 0.4 zoom 0.8
    easeout 0.6 zoom 0.6

label nightmerchantintro:
show bg allerynight merchant with dissolve
if diointroduction_complete == True:
    show boruto normal at right with dissolve
    jump diomenu_label
else:
    pass
$ renpy.sound.play("/audio/soun_fx/oldman_laugh2.opus", channel="sfx2", loop=False, relative_volume = 0.8)
"Mysterious Man" "*Snickering*"
bo"Hey y-"
"Mysterious Man" "I sense someone with potential nearby..." with vpunch
bot"Is he talking about me?"
menu:
    bot"Is he talking about me?"   
    "Try to approach him!":
        show boruto suspicious at right with dissolve
        if nightmerchant_seen == False:
            jump findmerchantonetime
        else:
            pass
        bo"Hold on for a second..."
        $ renpy.sound.play("/audio/soun_fx/oldman_laugh3.opus", channel="sfx2", loop=False, relative_volume = 0.5)
        $ renpy.sound.play("/audio/soun_fx/wind1.opus", channel="sfx1", loop=False, relative_volume = 1.0)
        scene bg alleynight
        show boruto surprised2 at right
        with flash
        "Mysterious Man" "Hehehe!"
        show boruto angry with dissolve
        bo"Not again..."
        $ renpy.sound.play("/audio/soun_fx/oldman_laugh5.opus", channel="sfx2", loop=False, relative_volume = 0.5)
        show merchant 1:
            xpos -1400
        "Mysterious Man" "Referring to you..."
        show merchant 1:
            easein 0.5 xpos 200
        show boruto surprised2 with Dissolve(0.2)
        show boruto at smallshake
        "Mysterious Man" "I was indeed!" with vpunch
        
        bo"W-what the!"
        "In an instant, the hooded man appeared by your side!"
        "Blending in the shadows of night, and with movement as light as the wind, it would appear the man before you possessed discreet abilities of stealth way beyond those of your comprehension."
        "Mysterious Man" "Don't be alarmed, young prodigious son! If I wanted you harmed, you'd be long gone into the dark of night!"
        $ renpy.sound.play("/audio/soun_fx/oldman_laugh4.opus", channel="sfx2", loop=False, relative_volume = 0.5)
        "Mysterious Man" "Hehehe!"
        show boruto suspicious with dissolve
        bo"Who the hell are you, old man..."
        label diointroduction:
        "Mysterious Man" "Glad you asked! You are talking to the greatest visionary of our times, the one and only..."
        "Mysterious Man" "Dio Sartorio Pantaloni della Coutura the 3rd, Sovereign Sentinel of Fashion, His Eminence of Eternal Grace and Elegance!"
        dio "But you can just call me Dio 'The Man' Sartorio!"
        menu:
            dio "But you can just call me Dio 'The Man' Sartorio!"
            "Impressive...":
                show boruto surprised2 with dissolve
                bo"Impressive..."
                show merchant 2 with dissolve
                dio"But not as impressive as this..."
            "You look like a bum!":
                show boruto sceeming with dissolve
                bo"All those honorifics, just to look like a bum!"
                dio "Hah! Beauty is in the eye of the beholder, kid!"
                show merchant 2 with dissolve
                dio "For example..."
        "Dio puts his hand in one of his many pockets and pulls out a..."
        $ renpy.sound.play("/audio/soun_fx/ominous_sound.opus", channel="sfx3", loop=False, relative_volume = 1.5)
        show mei_voyeur at polaroid_spin
        show boruto surprised2 with dissolve
        "A candid polaroid of the famous Mei Terumi, the running Kage of one of the five great Shinobi nations!"
        dio"Can you believe it? One of the most prominent Kunoichi of our times, captured in such a primitive moment!"
        dio"The juxtaposition between the Mizukage's elegance and prominence, and being caught in the animalistic act of relieving herself in public..."
        hide mei_voyeur with dissolve
        show merchant 1 with dissolve
        dio"The beauty of it brings a tear to my eye!"
        show boruto sceeming with dissolve
        bo"So... you are just a creep then?"
        show merchant at smallshake
        dio"A c-creep!? What!? No! Of course not..."
        $ renpy.sound.play("/audio/soun_fx/oldman_laugh4.opus", channel="sfx2", loop=False, relative_volume = 0.5)
        show merchant at smallshake
        dio"More like a connoisseur and appreciator of a woman's charm!"
        show merchant 2 with dissolve
        show mei_voyeur at parchment:
            zoom 0.6 yalign 0.1
        dio"You've yet to realize whose presence you are in, have you?"
        "Dio pulls out the Mizukage's candid photo once more and boastfully points at her clothes..."
        show boruto surprised2 with dissolve
        bo"Uuuh, am I supposed to be looking at something else besides the Mizukage's giant rack?"
        dio"Don't you see? The signature on her belt..."
        bo"H-her belt?"
        "Dio keeps incessantly tapping his finger at the Mizukage's clothing..."
        dio"It's there on the collar of her dress too, see!?"
        dio"Her panties even! Her entire outfit, kid..."
        bo"W-what about her outfit?"
        hide mei_voyeur with dissolve
        show merchant 1 with dissolve
        dio"Can't you see? It bears the mark of the most prestigious, most expensive, most fashionable brand known across all the great Shinobi nations!"
        show boruto at smallshake
        bo"It does...?"
        dio"Her entire fit was custom made and specifically ordered for and tailored by, the one and only..."
        $ renpy.sound.play("/audio/soun_fx/oldman_laugh10.opus", channel="sfx2", loop=False, relative_volume = 0.5)
        show merchant at smallshake
        dio"Dio Sartorio Pantaloni della Coutura!" with vpunch
        show merchant 1 with dissolve
        $ renpy.sound.play("/audio/soun_fx/oldman_laugh5.opus", channel="sfx2", loop=False, relative_volume = 0.5)
        dio"Hehe! Wanna hear the best part of it all, kid?"
        $ renpy.sound.play("/audio/soun_fx/oldman_laugh6.opus", channel="sfx2", loop=False, relative_volume = 0.5)
        dio"In her moment of indecency, I was there to snap that exquisite polaroid myself! *Perverted Giggles*"
        dio"A renowned designer by day, and a cultured appreciator of beauty by night! The candid polaroids of my subjects help me funnel inspiration into my future work!"
        menu:
            dio"A renowned designer by day, and a cultured appreciator of beauty by night! The candid polaroids of my subjects help me funnel inspiration into my future work!"
            "Impressive...":
                bo"Impressive..."
                $ renpy.sound.play("/audio/soun_fx/oldman_laugh7.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                dio"Right!? But not everyone is as much of a visionary as me and you are, kid!"
                show boruto normal with dissolve
            "Just a creep then, got it!":
                show boruto sceeming2 with dissolve
                bo"So you are just a creep after all, just as I thought!"
                $ renpy.sound.play("/audio/soun_fx/oldman_laugh8.opus", channel="sfx2", loop=False, relative_volume = 0.5)
                dio"Takes one to know one! *Perverted giggles*"
                dio"Why do you reckon I am telling you all this, kid..."
        dio"You see, the Mizukage isn't someone to be messed with..."
        dio"You should have seen how her face turned into that of a demon as soon as she spotted me hiding in the bushes!"
        dio"So I had to do only what Dio 'The Man' Sartorio could do..."
        $ renpy.sound.play("/audio/soun_fx/fast_blink.opus", channel="sfx2", loop=False, relative_volume = 0.5)
        scene bg alleynight
        show boruto surprised2 at right
        with flash
        dio"Run like the wind!"
        show merchant 1:
            xpos -1000
        show merchant:
            easein 0.3 xpos 100
        dio"I ran and ran, for days on end, until I wound up in this place!" with vpunch
        dio"Of course I, Dio 'The Man' Sartorio, in my endless foresight, have come up with an impenetrable plan of stealth and clandestine to avoid raising suspicion even to someone as perceptive as the Mizukage herself!"
        show boruto suspicious with dissolve
        bo"A p-plan, huh? That plan being..."
        $ renpy.sound.play("/audio/soun_fx/oldman_laugh1.opus", channel="sfx2", loop=False, relative_volume = 0.5)
        dio"A rugged cloak and a pair of cheap sunglasses of course!" with vpunch
        dio"No one in their right minds would ever recognize me in this fit! Dio Sartorio hiding in bushes? wearing some cheap rugs? Inconceivable!"
        $ renpy.sound.play("/audio/soun_fx/oldman_laugh2.opus", channel="sfx2", loop=False, relative_volume = 0.5)
        dio"Do you see now, the brilliance of the greatest visionary of our times? The one and only Dio Sartorio Pantaloni della Coutura the 3rd, Sovereign Sentinel of Fashion, His Eminence of Eternal Grace and Elegance!"
        show boruto normal with dissolve
        bo"*Sigh*..."
        bot"What a looney..."
        dio"You must be wondering... 'Why would someone as great as Dio 'The Man' Sartorio even trust a commoner like me with all this information'?"
        bo"Not re-"
        dio"Because I see the glint in your eyes, kid!" with vpunch
        dio"The same glint I see in mine when I stare at myself in the mirror! The glint of a true visionary..."
        dio"The glint of someone who goes against the grain of normalcy!"
        dio"And so, I Dio 'The Man' Sartorio, will cut you a deal of a lifetime..."
        dio"Seeing how I wound up in your place all of a sudden, I am going to need the help of a local to expedite the acquaintance of myself with your Nation..."
        dio"You bring me some interesting  material involving the beautiful subjects of Konoha to stir my creativity and imagination, and in return..."
        dio"I'll pay you handsomely for your work! Perhaps even let you in on some of my designs, or some of the expensive trinkets I've come across in my days..."
        dio"What say you! Do we have a partnership at our hands?"
        default diointroduction_complete = False
        $ diointroduction_complete = True
        jump diomenu
        
            

    "Leave":
        bot"Better not meddle..."


default diotrust = 0
default tenten_pendant_found = False
label diomenu_label:
scene bg alleynight
show boruto surprised2 at right
$ renpy.sound.play("/audio/soun_fx/fast_blink.opus", channel="sfx2", loop=False, relative_volume = 0.5)
with flash
show merchant 1:
    xpos -1000
show merchant:
    easein 0.3 xpos 100
show boruto normal with dissolve
menu diomenu:
    dio"Howdy, partner!"
    "Do you have something for me?":
        if diotrust < 20:
            dio"Not before you earn your keep, kid!"
            jump diomenu

        else:
            dio"You've been providing some high quality material kid..."
            menu dio_rewards:
                dio"You've been providing some high quality material kid..."
                "Expensive Pendant" if diotrust >=20 and tenten_pendant_found == False:
                    dio"I've come across this expensive trinket a few days back..."
                    dio"I am imparting it to you, free of charge!"
                    $ tenten_pendant_found = True
                    $ notification("Tenten's pendant found!")
                    dio"A token of my gratitude if you will..."
                    bo"Thanks, I suppose..."
                    jump diomenu
                "???":
                    dio"Keep providing more material and I might let you in on this one!"
                    jump dio_rewards
                    
                "???":
                    dio"I'll only impart this one to a partner that I could trust with my life!"
                    jump dio_rewards
                "Return":
                    jump diomenu
                
            
    "Sell photos":
        bo"I might have something for you, Dio!"
        dio"Oh? Let me see, let me see!"
        $ yoruichi_photos = get_model_photo_count("Yoruichi") 
        $ himawari_photos = get_model_photo_count("Himawari")
        $ himawari_photos_swimsuit = get_model_photo_count("Himawari_swimsuit")
        if yoruichi_photos == 0 and himawari_photos == 0 and himawari_photos_swimsuit == 0:
            show boruto embarassed with dissolve
            bo"Uuuh, N-nevermind! I don't have any on me right now..." with vpunch
            dio"Damn it, kid! I am relying on you..."
            show boruto normal with dissolve
            jump diomenu
        menu:
            dio"Oh? Let me see, let me see!"
            "Sell [yoruichi_photos] photos of Yoruichi" if yoruichi_photos > 0:
                bo"What do you think about these..."
                dio"Oh? A dark-skinned Kunoichi! Not from these places is she?"
                bo"Long story..."
                dio"Beautiful nonetheless, I could do with these! I'll pay you $5 for each!"
                $ diotrust+= yoruichi_photos
                call changeMoney(yoruichi_photos*5) from _call_changeMoney_17
                $ delete_all_model_photos("Yoruichi")
                bo"Pleasure doing business with you!"
                jump diomenu
            "Sell [himawari_photos] photos of [him_name]" if himawari_photos > 0:
                bo"What do you think about these..."
                dio"A young one... Not my type, but her fair skin more than makes up for it!"
                dio"She looks familiar too..."
                dio"Intriguing! I'll pay you $10 for each one of hers."
                bo"Sounds like a deal!"
                $ diotrust+= himawari_photos
                call changeMoney(himawari_photos*10) from _call_changeMoney_18
                bo"Pleasure doing business with you!"
                $ delete_all_model_photos("Himawari")
                jump diomenu
            "Sell [himawari_photos_swimsuit] sexy photos of [him_name]" if himawari_photos_swimsuit > 0:
                bo"I also have these... they're a bit more special."
                dio"Hoho! Now this is premium material, kid! The innocence of youth combined with a tantalizing outfit!"
                dio"This is exactly the kind of inspiration I need! I'll pay you..."
                dio"Mmmm... let me do the math..."
                dio"..."
                dio"$20 for each of these masterpieces!"
                bo"Deal!"
                bot"Did this old geezer forget how to do math? Anyway, works for me!"
                # Give more trust and money for the premium photos
                $ diotrust += himawari_photos_swimsuit * 2 
                call changeMoney(himawari_photos_swimsuit * 20) from _call_changeMoney_Himawari_swimsuit
                bo"Pleasure doing business with you!"
                # Make sure to delete photos from the correct album
                $ delete_all_model_photos("Himawari_swimsuit")
                jump diomenu
                
    "Talk":
        bo"I wanted to ask you something..."
        dio"Hm...?"
        menu:
            dio"Hm...?"
            "Can you tell me your backstory?":
                bo"Can you tell me your backstory?"
                jump diointroduction
            "Return":
                bo"Nevermind..."
                jump diomenu
            
    "Information":
        $ selected_diomenuinfo = "Dio"
        show screen diomenuinfo
        jump diomenu

    "Leave":
        show boruto surprised2 with dissolve
        bo"I have to go!"
        hide boruto with dissolve
        scene black with dissolve
        jump market 
        

























init python:
    def close_diomenuinfo():
        renpy.hide_screen("diomenuinfo")
        renpy.hide_screen("test_tsunade")
        renpy.hide_screen("displayTextScreen")

    class PartnershipBar(renpy.Displayable):
        def __init__(self, width, height, value, min_value=0, max_value=200, **kwargs):
            super(PartnershipBar, self).__init__(**kwargs)
            self.width = width
            self.height = height
            self.value = value
            self.min_value = min_value
            self.max_value = max_value
            
        def render(self, width, height, st, at):
            render = renpy.Render(self.width, self.height)
            
            # Create the background first
            bg = renpy.Render(self.width, self.height)
            bg.fill("#444444")  # Dark gray background
            render.blit(bg, (0, 0))  # Blit background first
            
            # Calculate how much of the bar should be filled (percentage)
            fill_percentage = self.value / float(self.max_value)
            bar_width = int(fill_percentage * self.width)
            
            # Ensure bar width stays within bounds
            bar_width = max(0, min(bar_width, self.width))
            
            if bar_width > 0:  # Only create bar if there's a positive width
                bar = renpy.Render(bar_width, self.height)
                
                # Gradient color based on value (light blue to dark blue)
                if self.value <= 50:
                    bar.fill("#a3d9ff")  # Light blue for lower levels
                elif self.value <= 100:
                    bar.fill("#5cb7f5")  # Medium light blue
                elif self.value <= 150:
                    bar.fill("#1896ef")  # Medium blue
                else:
                    bar.fill("#0066b8")  # Dark blue for highest levels
                    
                render.blit(bar, (0, 0))  # Start from left side now
            
            # Add markers for progress visualization
            # Add tick marks at 25% intervals
            for i in range(1, 4):
                tick_pos = int(self.width * (i / 4.0))
                tick = renpy.Render(1, self.height // 3)
                tick.fill("#ffffff")  # White tick marks
                render.blit(tick, (tick_pos, self.height // 3))
                
            return render





default selected_diomenuinfo = "Dio"
screen diomenuinfo():
    
    
    default dropdown_open = False
    zorder 100

    

    key "mouseup_3" action [Hide("diomenuinfo"),Hide("test_tsunade"), Hide("displayTextScreen")] #close with rightclick
    
    #full screen
    frame:
        xysize (1280,720)
        background Frame("gui/overlay/game_menu_2.png")
        button: #screen sized button to prevent lcicks from behind screen
            xysize (config.screen_width, config.screen_height)
            background None
            action NullAction() # No action to perform on click

        #close button
        imagebutton:    
            at customzoom3
            xalign 0.95
            yalign 0.05
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            auto "map/ui_close_%s.png"
            hovered Show("displayTextScreen", displayText = "Close Menu")
            unhovered Hide("displayTextScreen")
            action [Function(close_diomenuinfo)]

        #left selection menu
        vbox:
            xalign 0.05 yalign 0.2
            text "Menu" xalign 0.5 size (50 if renpy.variant("pc") else 40)
        vbox:
            
            xalign (0.05 if renpy.variant("pc") else 0.02) yalign (0.5 if renpy.variant("pc") else 0.55)
            spacing 30
            #Tsunade
            textbutton "Dio":
                xalign 0.5
                hover_sound "audio/soun_fx/select2.opus"
                activate_sound "audio/soun_fx/select4.opus"
                hovered Show("displayTextScreen", displayText = "Open Dio's panel")
                unhovered Hide("displayTextScreen")
                action SetVariable("selected_diomenuinfo", "Dio")
            #skill tree
            textbutton "Partnership":
                xalign 0.5
                hover_sound "audio/soun_fx/select2.opus"
                activate_sound "audio/soun_fx/select4.opus"
                hovered Show("displayTextScreen", displayText = "Open Partnership panel")
                unhovered Hide("displayTextScreen")
                action SetVariable("selected_diomenuinfo", "Partnership")


        #images of characters + outfits
        vbox:
            xalign 1.0 yalign 0.5
            if selected_diomenuinfo ==  "Dio":
                add "merchant 1" at dissolvehack:
                    zoom 1.0



        if selected_diomenuinfo == "Dio":
            vbox:
                xalign 0.4 yalign 0.4
                text "Name: Dio Sartorio" xalign 0.5
                text "Affiliation: Business Partner " xalign 0.5
                text "Age: Unknown" xalign 0.5
                null height 40 #add space
                frame:
                    xalign 0.65 yalign 0.53
                    background "#d3d3d320"
                    vbox:
                               
                        text "A famous designer by day" xalign 0.5
                        text "and a pervert by night." xalign 0.5
                        text "Capable of appraising your work" xalign 0.5
                        text "In exchange of various goods!" xalign 0.5
                        null height 20 #add space
                        use dio_partnership_bar

                
            
   
        #right screen descriptions
        elif selected_diomenuinfo == "Partnership":
            vbox:
                xalign (0.5 if renpy.variant("pc") else 0.7)
                yalign (0.4 if renpy.variant("pc") else 0.4)
                text "Dio is willing to share useful items to you."
                text "Improve your partnership with him by providing"
                text "photoshoot material to earn his trust!"
                text "Trust: [diotrust]" color "#00FF00"
                null height 50 #add space
                text "Rewards:"
                text "More rewards will be added in future versions" color "#FF0000"
                frame:
                    background "#d3d3d320"
                    vbox:
                        text "20 - Someone's valuable Pendant"
                        text "???" #todo  40 - A forbidden jutsu scroll"
                        text "???"






screen dio_partnership_bar:
    frame:
        xalign 0.5
        yalign 0.5
        background None  # Removes the background
        padding (0,0)    # Removes the padding
        vbox:
            spacing 10
            text "Partnership Level: [diotrust]" xalign 0.5
            $ partnership_text = ""
            $ text_color = "#ffffff"  # default white
            if diotrust <= 25:
                $ partnership_text = "Initial Contact"
                $ text_color = "#a3d9ff"
            elif diotrust <= 50:
                $ partnership_text = "Acquaintance"
                $ text_color = "#7fc8f8"
            elif diotrust <= 75:
                $ partnership_text = "Business Contact"
                $ text_color = "#5cb7f5"
            elif diotrust <= 100:
                $ partnership_text = "Associate"
                $ text_color = "#3aa6f2"
            elif diotrust <= 125:
                $ partnership_text = "Colleague"
                $ text_color = "#1896ef"
            elif diotrust <= 150:
                $ partnership_text = "Business Partner"
                $ text_color = "#0085ec"
            elif diotrust <= 175:
                $ partnership_text = "Strategic Partner"
                $ text_color = "#0075d2"
            else:
                $ partnership_text = "Aibou"
                $ text_color = "#0066b8"
            text "[partnership_text]" xalign 0.5 color text_color
            fixed:
                xsize 400
                ysize 30
                add PartnershipBar(400, 30, diotrust, 0, 200)