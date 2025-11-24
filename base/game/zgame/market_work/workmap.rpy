screen workmap_staircase():
    
    imagebutton:
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"
        idle "idle1"  #image in ui / needs to be seperate for correct images to be displayed when hovering
        hover "ramenshop stairs leftdoor"
        focus_mask "ramenshop stairs leftdoor"
        hovered [Show("displayTextScreen", displayText = "Suspicious Door")]
        unhovered [Hide("displayTextScreen")]
        action [Hide("workmap_staircase"),Hide("displayTextScreen"), Jump("stairs_leftdoor")]

    imagebutton:
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"
        idle "idle2"
        hover "ramenshop stairs updoor"
        focus_mask "ramenshop stairs updoor"
        hovered [Show("displayTextScreen", displayText = "Second Floor Hallway")]
        unhovered [Hide("displayTextScreen")]
        action [Hide("workmap_staircase"),Hide("displayTextScreen"), Jump("stairs_updoor")]


label stairs_leftdoor:
    bot"This door is locked."
    if spyworkmapcounter > 1:
        bot"I was joking last time about this place being a sex dungeon, but this door..."
        bot"It won't even budge even as I put my entire weight onto it. It must be barricaded from the other side... But why?"
    else:
        bot"The whole place gives off creepy vibes. Could easily pass for a sex dungeon in a horror movie..."
    show screen workmap_staircase
    $ ui.interact()

label stairs_updoor:
    default stairs_updoor_explored = False
    if stairs_updoor_explored == False:
        show ramenshop upstairs with dissolve
        $ renpy.sound.play("/audio/soun_fx/intro/introwoman2.opus", channel="sfx3", loop=False, relative_volume = 1.0)
        pause 1
        bot"The room straight ahead..."
        bot"That's where Yoru's voice is coming from..."
        bot"But shall I use the opportunity to look around first? Maybe I can find something useful..."
        bot"What even is all this junk..."
        bot"Is that a freaking greatsword against that wall!?" with vpunch
        bot"What the fuck is going on in here..."
        "Search around to find points of interest"
        $ stairs_updoor_explored = True
    show ramenshop upstairs with dissolve
    if spyworkmapcounter > 1:
        $ renpy.sound.play("/audio/soun_fx/intro/introwoman3.opus", channel="sfx3", loop=False, relative_volume = 1.3)
        bot"Oh shit!" with vpunch
        bot"That came from the room to the left! The one with the photography gear..."
        bot"Maybe I can sneak into the room at the end of the hallway. Could be that something important is in there..."
        show screen workmap_upstairs(spyworkmapcounter)
        $ ui.interact()
    else:
        show screen workmap_upstairs(spyworkmapcounter)
        $ ui.interact()



    "Search around to find points of interest"
    

screen workmap_upstairs(spyworkmapcounter):
    
    imagebutton:
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"
        idle "idle1"  #image in ui / needs to be seperate for correct images to be displayed when hovering
        hover "ramenshop upstairs sword"
        focus_mask "ramenshop upstairs sword"
        hovered [Show("displayTextScreen", displayText = "Greatsword")]
        unhovered [Hide("displayTextScreen")]
        action [Hide("workmap_upstairs"),Hide("displayTextScreen"), Jump("upstairs_greatsword")]

    imagebutton:
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"
        idle "idle2"
        hover "ramenshop upstairs bookshelf"
        focus_mask "ramenshop upstairs bookshelf"
        hovered [Show("displayTextScreen", displayText = "Bookshelf")]
        unhovered [Hide("displayTextScreen")]
        action [Hide("workmap_upstairs"),Hide("displayTextScreen"), Jump("upstairs_bookshelf")]

    if spyworkmapcounter <2: #rooms before visiting the 2nd time

        imagebutton:
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            idle "idle3"
            hover "ramenshop upstairs photoroom"
            focus_mask "ramenshop upstairs photoroom"
            hovered [Show("displayTextScreen", displayText = "Strange Room")]
            unhovered [Hide("displayTextScreen")]
            action [Hide("workmap_upstairs"), Hide("displayTextScreen"), Jump("upstairs_photoroom")]

        imagebutton:
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            idle "idle4"
            hover "ramenshop upstairs secretroom"
            focus_mask "ramenshop upstairs secretroom"
            hovered [Show("displayTextScreen", displayText = "Dimly Lit Room")]
            unhovered [Hide("displayTextScreen")]
            action [Hide("workmap_upstairs"), Hide("displayTextScreen"), Jump("upstairs_secretroom")]

    if spyworkmapcounter >=2: #rooms after 2nd visit

        imagebutton:
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            idle "idle3"
            hover "ramenshop upstairs photoroom"
            focus_mask "ramenshop upstairs photoroom"
            hovered [Show("displayTextScreen", displayText = "Strange Room")]
            unhovered [Hide("displayTextScreen")]
            action [Hide("workmap_upstairs"), Hide("displayTextScreen"), Jump("upstairs_secretroom2")]

        imagebutton:
            hover_sound "audio/soun_fx/select2.opus"
            activate_sound "audio/soun_fx/select4.opus"
            idle "idle4"
            hover "ramenshop upstairs secretroom"
            focus_mask "ramenshop upstairs secretroom"
            hovered [Show("displayTextScreen", displayText = "Dimly Lit Room")]
            unhovered [Hide("displayTextScreen")]
            action [Hide("workmap_upstairs"), Hide("displayTextScreen"), Jump("upstairs_enter_secretroom")] #upstairs_enter_secretroom


    #return
    imagebutton:
        xalign 0.05 yalign 0.05
        auto "images/ui/return_button_%s.png"
        hovered Show("displayTextScreen", displayText = "Return to Staircase")
        unhovered [Hide("displayTextScreen")]
        action [Hide("workmap_upstairs"), Hide("displayTextScreen"), Jump("return_staircase")]
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"

label upstairs_greatsword:
    bot"Why the hell would a ramen-shop owner have a greatsword lying around..."
    bot"Unless it's supposed to be cosmetic?"
    show screen workmap_upstairs(spyworkmapcounter)
    $ ui.interact()
label upstairs_bookshelf:
    bot"The framed pictures on this wall... They remind me of a familiar landscape."
    bot"I can't quite place it though..."
    bot"There's a bunch of books laying around too..."
    menu upstairs_bookmenu:
        bot"There's a bunch of books laying around too..."
        "Kamasutra - The Gift of Pleasure":
            bot"Some hentai-like looking book..."
            bot"It depicts a bunch of strange sexual positions..."
            bot"Obo's a dirty old man, isn't he..."
            jump upstairs_bookmenu
        "The Art of War":
            bot"Something about wars and military strategy..."
            bot"Why would Obo be interested in war strategy?"
            bot"Unless he is a part-time war general or something, ha!"
            bot"There's no way an old fat fuck like him would know anything about war..."
            jump upstairs_bookmenu
        "Daimyo's Manifesto":
            bot"This is a strange one, It looks to be written in a cryptic manner. A bunch of euphemisms and hidden meanings are making it impossible to decipher its true message..."
            bot"'Be thy blessed mother, thou art the one whose womb shalt bear the seed of the cursed one and so shalt thee give birth to the child of hatred...'"
            bot"'Thy son, shalt paint the leaf red with his own blood.'"
            bot"'Thy child shalt break down the gates.'"
            bot"'And so shalt the coming storm, swoop up the lifeless leaves.'"
            bot"What is this shit even supposed to mean..."
            jump upstairs_bookmenu
        "Return":
            pass
        
    show screen workmap_upstairs(spyworkmapcounter)
    $ ui.interact()

label upstairs_photoroom:
    scene ramenshop photoroom with dissolve
    show screen workmap_photoroom
    "Search around to find points of interest"
    $ ui.interact()

label upstairs_secretroom: #1st time visiting
    show ramenshop upstairs with dissolve:
        zoom 1.7 xalign 0.5 yalign 0.5
    bot"This is where the voices are coming from..."
    bot"Shall I take a look?"
    menu:
        bot"Shall I take a look?"
        "Take a look":
            #ramen nightscenes
            jump ramennightscenes
        "Keep exploring":
            show ramenshop upstairs with dissolve:
                zoom 1.0
            bot"I need to find out everything I can first..."
            show screen workmap_upstairs(spyworkmapcounter)
            $ ui.interact()

label upstairs_secretroom2: #2nd time visiting
    show ramenshop upstairs with dissolve:
        zoom 1.7 xalign 0.0 yalign 0.5
    bot"The voices are coming from the photo-room..."
    bot"Shall I take a look?"
    menu:
        bot"Shall I take a look?"
        "Take a look":
            #ramen nightscenes
            jump ramennightscenes
        "Keep exploring":
            show ramenshop upstairs with dissolve:
                zoom 1.0
            bot"Maybe there's something I can find first..."
            show screen workmap_upstairs(spyworkmapcounter)
            $ ui.interact()



        

screen workmap_photoroom():
    
    imagebutton:
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"
        idle "idle1"  #image in ui / needs to be seperate for correct images to be displayed when hovering
        hover "ramenshop photoroom bed"
        focus_mask "ramenshop photoroom bed"
        hovered [Show("displayTextScreen", displayText = "Rugged Bed")]
        unhovered [Hide("displayTextScreen")]
        action [Hide("workmap_photoroom"),Hide("displayTextScreen"), Jump("photoroom_bed")]


    imagebutton:
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"
        idle "idle2"
        hover "ramenshop photoroom camera"
        focus_mask "ramenshop photoroom camera"
        hovered [Show("displayTextScreen", displayText = "Camera Gear")]
        unhovered [Hide("displayTextScreen")]
        action [Hide("workmap_photoroom"), Hide("displayTextScreen"), Jump("photoroom_camera")]

    imagebutton:
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"
        idle "idle3"
        hover "ramenshop photoroom return"
        focus_mask "ramenshop photoroom return"
        hovered [Show("displayTextScreen", displayText = "Return to hallway")]
        unhovered [Hide("displayTextScreen")]
        action [Hide("workmap_photoroom"), Hide("displayTextScreen"), Jump("return_upstairs")]

    imagebutton:
        xalign 0.05 yalign 0.05
        auto "images/ui/return_button_%s.png"
        hovered Show("displayTextScreen", displayText = "Return to Hallway")
        unhovered [Hide("displayTextScreen")]
        action [Hide("workmap_photoroom"), Hide("displayTextScreen"), Jump("return_upstairs")]
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"

label return_upstairs:
    show ramenshop upstairs with dissolve
    show screen workmap_upstairs(spyworkmapcounter)
    $ ui.interact()

label return_staircase:
    show ramenshop stairs with dissolve
    show screen workmap_staircase
    $ ui.interact()

label photoroom_bed:
    bot"A messy mattress is lying on the floor. A bunch of photography gear is stored on the counter next to it..."
    bot"Doesn't look like gear a hobbyist would use."
    show screen workmap_photoroom
    $ ui.interact() 


label photoroom_camera:
    bot"A professional grade camera mounted on a tripod..."
    bot"What possible use could the old man have of something like this?"
    bot"He must be running some part-time gig of sorts..."
    bot"Unless he is a spying on someone... or something?"
    show screen workmap_photoroom
    $ ui.interact()



screen workmap_secretroom():
    
    imagebutton:
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"
        idle "idle1"  #image in ui / needs to be seperate for correct images to be displayed when hovering
        hover "ramenshop secretroom wall"
        focus_mask "ramenshop secretroom wall"
        hovered [Show("displayTextScreen", displayText = "Damaged Wall")]
        unhovered [Hide("displayTextScreen")]
        action [Hide("workmap_secretroom"),Hide("displayTextScreen"), Jump("secretroom_wall")]


    imagebutton:
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"
        idle "idle2"
        hover "ramenshop secretroom books"
        focus_mask "ramenshop secretroom books"
        hovered [Show("displayTextScreen", displayText = "Drawer with Books")]
        unhovered [Hide("displayTextScreen")]
        action [Hide("workmap_secretroom"), Hide("displayTextScreen"), Jump("secretroom_books")]

    imagebutton:
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"
        idle "idle3"
        hover "ramenshop secretroom table"
        focus_mask "ramenshop secretroom table"
        hovered [Show("displayTextScreen", displayText = "Table")]
        unhovered [Hide("displayTextScreen")]
        action [Hide("workmap_secretroom"), Hide("displayTextScreen"), Jump("secretroom_table")]

    imagebutton:
        xalign 0.05 yalign 0.05
        auto "images/ui/return_button_%s.png"
        hovered Show("displayTextScreen", displayText = "Return to Hallway")
        unhovered [Hide("displayTextScreen")]
        action [Hide("workmap_secretroom"), Hide("displayTextScreen"), Jump("return_upstairs")]
        hover_sound "audio/soun_fx/select2.opus"
        activate_sound "audio/soun_fx/select4.opus"

label upstairs_enter_secretroom:
    show ramenshop secretroom with dissolve
    "Search around to find points of interest"
    show screen workmap_secretroom
    $ ui.interact()

label secretroom_wall:
    bot"This wall looks strangely suspicious..."
    $ renpy.sound.play("/audio/soun_fx/ominous_sound.opus", channel="sfx3", loop=False, relative_volume = 1.5)
    bot"It appears to be connected to another room... but there's no door to open. Huh..."
    bot"The wooden structure is blocking access to whatever is behind..."
    bot"The wall to the right of it is also showing signs of tampering..."
    $ renpy.sound.play("/audio/soun_fx/doorknock.opus", channel="sfx2", loop=False, relative_volume = 1.5)
    bot"It even feels empty to the touch..."
    bot"Is the old man hiding dead bodies behind it or something...?"
    show screen workmap_secretroom
    $ ui.interact()

transform parchment:
    subpixel True
    xalign 0.5 ypos -0.15
    blur 20
    alpha 0.5
    zoom 0.3
    easein 4 blur 0 zoom 0.7 alpha 0.85
label secretroom_books:
    bot"More books laying around..."
    "You search the drawers..."
    $ renpy.sound.play("/audio/soun_fx/ominous_sound.opus", channel="sfx3", loop=False, relative_volume = 1.5)
    show parchment at parchment
    bot"Oh...? What's this"
    bot"Looks like an important parchment of sorts, sealed with a strange ribbon. Feels like if I touch it it'll crumble to pieces."
    bot"The receiver and sender of it are ciphered in cryptic code..."
    bot"The code reads:{p}{p}'Nkswiy'c mywwkxnwoxdc' , 'Pyb dro voknob yp Kukdceus'."
    menu:
        bot"The code reads:{p}{p}'Nkswiy'c mywwkxnwoxdc' , 'Pyb dro voknob yp Kukdceus'."
        "Try to decode the message":
            bot"The code reads: 'Nkswiy'c mywwkxnwoxdc' , 'Pyb dro voknob yp Kukdceus'. {p} Hmm... The characters are at least familiar, but they don't seem to correspond to some known language."
            bot"The code reads: 'Nkswiy'c mywwkxnwoxdc' , 'Pyb dro voknob yp Kukdceus'. {p}{p} Could it be some sort of cipher? I am way too stupid for this shit..."
        "Don't":
            bot"Maybe if I actually attended school I could do something about this..."
        
    bot"Looks like goddamn gibberish."
    bot"The small section that I can see reads..."
    bot"'...the three stages ~ Infiltrate, Assimilate, Ext-(unreadable).'"
    hide parchment with dissolve
    bot"I-infiltrate...?"
    bot"S-shit! Yoru said it herself... Obo might not be what he looks like!"
    bot"Can that old bastard really be a spy for the enemy? This letter... the sword, this whole place exudes a sinister aura..."
    bot"Could this all be in my head? And even if Obo's not who he says he is..."
    bot"I have almost no evidence for a concrete accusation. I'll have to keep looking for the truth..."

    show screen workmap_secretroom
    $ ui.interact()
label secretroom_table:
    bot"The table the old bastard threw Yoru on the other night..."
    bot"It seems she prepared a bunch of food and beverages for Obo again..."
    bot"The frame above the table... It depicts the same landscape as the other frames in the hallway do. I've seen this summit before... but where?"
    show screen workmap_secretroom
    $ ui.interact()