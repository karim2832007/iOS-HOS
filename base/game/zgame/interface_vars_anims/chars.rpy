init python:
    import random

    renpy.music.register_channel("sfx1", "sfx")
    renpy.music.register_channel("sfx2", "sfx")
    renpy.music.register_channel("sfx3", "sfx")
    renpy.music.register_channel("sfx4", "sfx")
    renpy.music.register_channel("sfx5", "sfx")
    renpy.music.register_channel("sfxnotify", "sfx")
    renpy.music.register_channel("sfxstat", "sfx")
    renpy.music.register_channel("ambience", "sfx")
    renpy.music.register_channel("ambience2", "sfx")

    flash = Fade(.1, 0.01, .33, color="#ccc9c9ff") #flash effect

    longdissolve = Dissolve(3.0)  #long dissolve effect

    config.mouse = {
        'hand': [ ( "ui/hand_cursor_f2.png", 100, 140) ],
        'handsmall': [ ( "ui/hand_cursor_f2_small.png", 0, 50) ]
    }
    
default hashbase = 12
default show_buttons = False

#current event to handle jumps
default current_event =""

#shopkeep interaction
default shopkeep_interactions = 0

#room buttons visibility
default talkbutton = False
default actionbutton = False
default strengthbutton = False
default infobutton = "inactive"

transform mid:   #place sprites in mid with at mid
    xalign 0.5


define gui.text_outlines = [ (1, "#242526", 0, 0) ] #text outline 1 pixel

#darken bg
image halfblack = "#00000088"
image halfblack2 = "#00000088"
image halfblacklust = "#00000088"

#text colors
default lovecolor = "#ff6efa"
default obediencecolor = "#a16cc4"
default hatredcolor = "#a31d1d"
default dominancecolor = "#FF6666"
default moneycolor = "#3e9c35"
default impulsecolor = "#A85858"


#show disabled menu options / set to true if u want menu options to always show
define config.menu_include_disabled = False 
#shit way to hide menu opt when missing points

#Character Locations
default hin_location = ""
default him_location = ""
default  rooms = ["kitchen", "bathroom", "borutobedroom", "laundryroom", "livingroom", "himawaribedroom" , "hinatabedroom"]
default boruto_location = ""

#handles tutorials
default completed_intro = 1

default clickinfobutton = ""

#chapter1
default inohair = True
default inospank = False
default inospit = False
default inoslap = False
#Character variables

#boruto vars (stat levels defined in statcheck functions)
default strength = 0
default dominance = 0 
default money = 0
default hatred = 0
default has_key = False  #key, unlocks doors if conditional button = true
default has_sunscreen = False
default has_clothes1 = False
default has_clothes2 = False
default has_clothes3 = False
define boruto_clinic_gropemom = False
define lie_about_ino = False

#extra char vars
default ino_fainted = False

#hinata vars (stat levels defined in statcheck functions)
default grope_hinata = 0
default spank_hinata = 0
default clothes_hinata = ""
default hinata_obedience = 0
default hinata_love = 0
default hinata_respect = 0

#himawari vars (stat levels defined in statcheck functions)
default hima_shop = False
default hima_shop_bought = False

default grope_himawari = 0
default spank_himawari = 0
default clothes_himawari = ""
default himawari_obedience = 0
default himawari_love = 0
default himawari_respect = 0



#Characters + relations
default bo_name = "Boruto"
default bo_age = "18"


default na_rel_default = "Dad"
default na_name = "Naruto"
default na_rel = "[na_rel_default]"
default na_rel_to_bo_default = "son"
default na_rel_to_bo = "[na_rel_to_bo_default]"

default hin_rel_default = "Mom"

default hin_name = "Hinata"
default hin_rel = "[hin_rel_default]"
default hin_rel_to_bo_default = "son"
default hin_rel_to_bo = "[hin_rel_to_bo_default]"
default hin_age = "36"


default him_name = "Himawari"
default him_rel_default = "sister"
default him_rel = "[him_rel_default]"
default him_rel_to_bo_default = "brother"
default him_rel_to_bo = "[him_rel_to_bo_default]"
default him_age = "18"

#misc chars
define beast = Character("Beast", color="#a31d1d", what_color="#a31d1d", ctc="ctc_arrowblink")
define dm = Character("Demanding Men", image = "demandingmen", callback=name_callback, cb_name="demandingmen", ctc="ctc_arrowblink")
define dev = Character("Dev", color="#4d6e52", what_color="#71ad7a", ctc="ctc_arrowblink")
define ku = Character("Kushina", color="#8e2e41", ctc="ctc_arrowblink")
define to = Character("Toji", color="#7a3715", ctc="ctc_arrowblink")
define ko = Character("Koji", color="#bf490d", ctc="ctc_arrowblink")
define kot = Character(ko, what_italic=True, what_color="#7f7f7f", color="#bf490d", callback=name_callback, cb_name="koji", ctc="ctc_arrowblink")

define mada = Character("Madame", color="#FF7F50", callback=name_callback, cb_name="madame", ctc="ctc_arrowblink")
define da = Character("Daimyo", color="#E2DFD2", callback=name_callback, cb_name="daimyo", ctc="ctc_arrowblink")
define ten = Character("Tenten", color="#675348", callback=name_callback, cb_name="tenten", ctc="ctc_arrowblink")


#main chars
define bo = Character("[bo_name]", color="#FF3333", image = "boruto", callback=name_callback, cb_name="boruto", ctc="ctc_arrowblink")
define narrator = Character(name=None, ctc="ctc_arrowblink")
default bo_color = "#FF3333"
define boe = Character("[bo_name]", color="#800000", image = "boruto", callback=name_callback, cb_name="boruto", ctc="ctc_arrowblink")
default boe_color = "#800000"

define hin = Character("[hin_name]", color="#A533FF", image = "hinata", callback=name_callback, cb_name="hinata", ctc="ctc_arrowblink")
define hin_color = "#A533FF"

define him = Character("[him_name]", color="#3358FF", image = "himawari", callback=name_callback, cb_name="himawari", ctc="ctc_arrowblink")
define him_color = "#3358FF"

define bot = Character(bo, what_italic=True, what_color="#7f7f7f",what_outlines=[(2, "#000000", 0, 0)], color="#FF3333", image = "boruto", callback=name_callback, cb_name="boruto", ctc="ctc_arrowblink")
define hint = Character(hin, what_italic=True, what_color="#7f7f7f",what_outlines=[(2, "#000000", 0, 0)], color="#A533FF", image = "hinata", callback=name_callback, cb_name="hinata", ctc="ctc_arrowblink")
define himt = Character(him, what_italic=True, what_color="#7f7f7f",what_outlines=[(2, "#000000", 0, 0)], color="#3358FF", image = "himawari", callback=name_callback, cb_name="himawari", ctc="ctc_arrowblink")


#speech bubbles
define speech_bubble_bo = Character(
    "bo", 
    screen="bubble_say",
    what_style="bubble_speech_bo")
define speech_bubble_hin = Character(
    "[hin_name]", 
    screen="bubble_say",
    what_style="bubble_speech_hin")
define speech_bubble_him = Character(
    "[him_name]", 
    screen="bubble_say",
    what_style="bubble_speech_him")
define speech_bubble_yo = Character(
    "yo", 
    screen="bubble_say",
    what_style="bubble_speech_yo")


#side chars
default ts_name = "Tsunade"
default ino_name = "Ino"
default obo_name = "Obo"
default yo_name = "Yoruichi"
define ts = Character("[ts_name]", color="#FFBB33",callback=name_callback, cb_name="tsunade")
define tst = Character(ts, what_italic=True, what_color="#7f7f7f", color="#FFBB33")

define ino = Character("[ino_name]", color="#F3FF33", ctc="ctc_arrowblink")
define na = Character("[na_name]", color="#dd6300", ctc="ctc_arrowblink")
define obo = Character("[obo_name]", color="#8B4513", callback=name_callback, cb_name="obo", ctc="ctc_arrowblink")
define yo = Character("[yo_name]", color="#673147", callback=name_callback, cb_name="yoruichi", ctc="ctc_arrowblink")
define sara = Character("Sarada", color="#8B0000", callback=name_callback, cb_name="sarada", ctc="ctc_arrowblink")
define sarat = Character(sara, what_italic=True, what_color="#7f7f7f", color="#8B0000", ctc="ctc_arrowblink")
define saku = Character("Sakura", color="#ffb7c5", callback=name_callback, cb_name="sakura", ctc="ctc_arrowblink")
define sakut = Character(saku, what_italic=True, what_color="#7f7f7f", color="#ffb7c5")
define dio = Character("Dio 'The Man' Sartorio", color="#C0C0C0", callback=name_callback, cb_name="dio", ctc="ctc_arrowblink")


#--------------------------------------------------------------------------------------------------------

#Daimyo
image daimyo normal = At(Transform("daimyo_s normalt", zoom=0.7), sprite_highlight("daimyo")) 
image daimyo pervert = At(Transform("daimyo_s pervertt", zoom=0.7), sprite_highlight("daimyo")) 




#boruto normal
image boruto shirtless = At(Transform("boruto normal shirtless", zoom=0.34), sprite_highlight("boruto"))
image boruto cat = At(Transform("boruto normal cat", zoom=0.36), sprite_highlight("boruto"))
image boruto surprised = At(Transform("boruto normal surprised", zoom=0.36), sprite_highlight("boruto"))
image boruto surprised2 = At(Transform("boruto normal surprised2", zoom=0.36), sprite_highlight("boruto"))
image boruto surprised3 = At(Transform("boruto normal surprised3", zoom=0.36), sprite_highlight("boruto"))
image boruto suspicious = At(Transform("boruto normal suspicious", zoom=0.36), sprite_highlight("boruto"))
image boruto angry = At(Transform("boruto normal angry", zoom=0.36), sprite_highlight("boruto"))
image boruto angry2 = At(Transform("boruto normal angry2", zoom=0.36), sprite_highlight("boruto"))
image boruto embarassed = At(Transform("boruto normal embarassed", zoom=0.36), sprite_highlight("boruto"))
image boruto furious = At(Transform("boruto normal furious", zoom=0.36), sprite_highlight("boruto"))
image boruto pain = At(Transform("boruto normal pain", zoom=0.36), sprite_highlight("boruto"))
image boruto pain2 = At(Transform("boruto normal pain2", zoom=0.36), sprite_highlight("boruto"))
image boruto pissy = At(Transform("boruto normal pissy", zoom=0.36), sprite_highlight("boruto"))          #pissy hs
image boruto sad = At(Transform("boruto normal sad", zoom=0.36), sprite_highlight("boruto"))
image boruto sad2 = At(Transform("boruto normal sad2", zoom=0.36), sprite_highlight("boruto"))
image boruto sceeming = At(Transform("boruto normal sceeming", zoom=0.36), sprite_highlight("boruto"))
image boruto sceeming2 = At(Transform("boruto normal sceeming2", zoom=0.36), sprite_highlight("boruto"))
image boruto sceeming3 = At(Transform("boruto normal sceeming3", zoom=0.36), sprite_highlight("boruto"))
image boruto redsceeming = At(Transform("boruto red sceeming", zoom=0.36), sprite_highlight("boruto"))
image boruto sceeming4 = At(Transform("boruto normal sceeming4", zoom=0.36), sprite_highlight("boruto"))
image boruto smirk = At(Transform("boruto normal smirk", zoom=0.36), sprite_highlight("boruto"))
image boruto smirk2 = At(Transform("boruto normal smirk2", zoom=0.36), sprite_highlight("boruto"))
image boruto snob = At(Transform("boruto normal snob", zoom=0.36), sprite_highlight("boruto"))
image boruto worried = At(Transform("boruto normal worried", zoom=0.36), sprite_highlight("boruto"))
image boruto worried2 = At(Transform("boruto normal worried2", zoom=0.36), sprite_highlight("boruto"))
image boruto normal = At(Transform("boruto normal normal", zoom=0.36), sprite_highlight("boruto"))        #normal hs
image boruto redpain = At(Transform("boruto red pain", zoom=0.36), sprite_highlight("boruto"))            #redpain hs
image boruto laughing = At(Transform("boruto normal laughing", zoom=0.36), sprite_highlight("boruto"))
image boruto laughing2 = At(Transform("boruto normal laughing2", zoom=0.36), sprite_highlight("boruto"))
image boruto rednormal = At(Transform("boruto red normal", zoom=0.36), sprite_highlight("boruto"))            #red normal

#boruto boner clothed
image boruto bonersurprised = At(Transform("boruto boner surprised", zoom=0.36), sprite_highlight("boruto"))
image boruto bonersurprised2 = At(Transform("boruto boner surprised2", zoom=0.36), sprite_highlight("boruto"))
image boruto bonersurprisedred = At(Transform("boruto boner surprisedred", zoom=0.36), sprite_highlight("boruto"))
image boruto bonerevil = At(Transform("boruto boner evil", zoom=0.36), sprite_highlight("boruto"))
image boruto bonerevil2 = At(Transform("boruto boner evil2", zoom=0.36), sprite_highlight("boruto"))
image boruto bonerevil3 = At(Transform("boruto boner evil3", zoom=0.36), sprite_highlight("boruto"))
image boruto bonerevil4 = At(Transform("boruto boner evil4", zoom=0.36), sprite_highlight("boruto"))
image boruto bonerevil5 = At(Transform("boruto boner evil5", zoom=0.36), sprite_highlight("boruto"))

#boruto boxers no boner
image boruto box1surprised = At(Transform("boruto boxers1", zoom=0.36), sprite_highlight("boruto"))
image boruto box1smirk = At(Transform("boruto boxers1_smirk", zoom=0.36), sprite_highlight("boruto"))
#boruto boxers b2
image boruto box2surprised = At(Transform("boruto boxers2", zoom=0.36), sprite_highlight("boruto"))
image boruto box2smirk = At(Transform("boruto boxers2_smirk", zoom=0.36), sprite_highlight("boruto"))
image boruto box2smirk2 = At(Transform("boruto boxers2_smirk2", zoom=0.36), sprite_highlight("boruto"))
#boruto boxers b3
image boruto box3surprised = At(Transform("boruto boxers3_surprised", zoom=0.36), sprite_highlight("boruto"))
image boruto box3smirk = At(Transform("boruto boxers3", zoom=0.36), sprite_highlight("boruto"))
image boruto box3smirk2 = At(Transform("boruto boxers3_2", zoom=0.36), sprite_highlight("boruto"))


#boruto towel b3
image boruto towelmad = At(Transform("boruto nakedtowel", zoom=0.71), sprite_highlight("boruto"))
image boruto towelsmirk = At(Transform("boruto nakedtowel smirk", zoom=0.71), sprite_highlight("boruto"))



#yoga hinata
image hina assertive = At("hinata hs assertive", sprite_highlight("hinata"))      #assertive hs
image hina concerned = At("hinata hs concerned", sprite_highlight("hinata"))      #concerned hs
image hina surprised = At("hinata hs surprised", sprite_highlight("hinata"))      #surprised hs
image hina pthinkingangry = At("hinata thinking2 angry", sprite_highlight("hinata"))  #angry thinking portrait
image hina thinking = At("hinata hs thinking", sprite_highlight("hinata"))        #thinking
image hina pthinking = At("hinata p thinking", sprite_highlight("hinata"))        #thinking portrait
image hina pthinking2 = At("hinata p thinking2", sprite_highlight("hinata"))      #thinking portrait2
image hina talking = At("hinata talking", sprite_highlight("hinata"))            #talking
image hina talkinghappy = At("hinata talkinghappy", sprite_highlight("hinata"))        #thinking
image hina pushing = At("hinata pushing", sprite_highlight("hinata"))        #thinking


#sweater hinata

image shina restrained = At(Transform("sweaterhina restrained", zoom=0.7), sprite_highlight("hinata")) 

image shina angry = At(Transform("sweaterhina angry", zoom=0.37), sprite_highlight("hinata"))              
image shina angry2 = At(Transform("sweaterhina angry2", zoom=0.37), sprite_highlight("hinata"))              
image shina angry3 = At(Transform("sweaterhina angry3", zoom=0.37), sprite_highlight("hinata"))              
image shina normal = At(Transform("sweaterhina normal", zoom=0.37), sprite_highlight("hinata"))              
image shina serious = At(Transform("sweaterhina serious", zoom=0.37), sprite_highlight("hinata"))              
image shina concerned = At(Transform("sweaterhina concerned", zoom=0.37), sprite_highlight("hinata"))              
image shina surprised = At(Transform("sweaterhina surprised", zoom=0.37), sprite_highlight("hinata"))              
image shina surprised2 = At(Transform("sweaterhina surprised2", zoom=0.37), sprite_highlight("hinata"))              
image shina surprised3 = At(Transform("sweaterhina surprised3", zoom=0.37), sprite_highlight("hinata"))              
image shina surprised4 = At(Transform("sweaterhina surprised4", zoom=0.37), sprite_highlight("hinata"))              
image shina surprised5 = At(Transform("sweaterhina surprised5", zoom=0.37), sprite_highlight("hinata"))              
image shina assertive = At(Transform("sweaterhina assertive", zoom=0.37), sprite_highlight("hinata"))              
image shina smiling = At(Transform("sweaterhina smiling", zoom=0.37), sprite_highlight("hinata"))              
image shina shy = At(Transform("sweaterhina shy", zoom=0.37), sprite_highlight("hinata"))              
image shina shy2 = At(Transform("sweaterhina shy2", zoom=0.37), sprite_highlight("hinata"))              
image shina smiling = At(Transform("sweaterhina smiling", zoom=0.37), sprite_highlight("hinata"))              
image shina worried = At(Transform("sweaterhina worried", zoom=0.37), sprite_highlight("hinata"))              




#towel hina
image thina b1 = At(Transform("hinata btowel1", zoom=0.7), sprite_highlight("hinata")) 
image thina b1_1 = At(Transform("hinata btowel1_1", zoom=0.7), sprite_highlight("hinata")) 
image thina b2 = At(Transform("hinata btowel2", zoom=0.7), sprite_highlight("hinata"))

image thina bow1 = At(Transform("hinata towel bow1", zoom=0.7), sprite_highlight("hinata")) 
image thina bow2 = At(Transform("hinata towel bow2", zoom=0.7), sprite_highlight("hinata")) 
image thina bow3 = At(Transform("hinata towel bow2_2", zoom=0.7), sprite_highlight("hinata"))
image thina bowtowelfall = At(Transform("hinata towel bow towelfall", zoom=0.7), sprite_highlight("hinata")) 


image thina angry = At(Transform("hinata towel angry", zoom=0.7), sprite_highlight("hinata")) 
image thina annoyed = At(Transform("hinata towel annoyed", zoom=0.7), sprite_highlight("hinata")) 
image thina remove = At(Transform("hinata towel remove", zoom=0.7), sprite_highlight("hinata")) 
image thina shy = At(Transform("hinata towel shy", zoom=0.7), sprite_highlight("hinata")) 
image thina shy2 = At(Transform("hinata towel shy2", zoom=0.7), sprite_highlight("hinata")) 
image thina thinking = At(Transform("hinata towel thinking", zoom=0.7), sprite_highlight("hinata")) 

#maid hinata (ramen / restaurant)
image rhina angry1 = At(Transform("ramenhinata angry1", zoom=0.7), sprite_highlight("hinata")) 
image rhina angry2 = At(Transform("ramenhinata angry2", zoom=0.7), sprite_highlight("hinata")) 
image rhina angry3 = At(Transform("ramenhinata angry3", zoom=0.7), sprite_highlight("hinata")) 
image rhina concerned1 = At(Transform("ramenhinata concerned1", zoom=0.7), sprite_highlight("hinata")) 
image rhina normal1 = At(Transform("ramenhinata normal1", zoom=0.7), sprite_highlight("hinata")) 
image rhina normal2 = At(Transform("ramenhinata normal2", zoom=0.7), sprite_highlight("hinata")) 
image rhina serious1 = At(Transform("ramenhinata serious1", zoom=0.7), sprite_highlight("hinata")) 
image rhina shy1 = At(Transform("ramenhinata shy1", zoom=0.7), sprite_highlight("hinata")) 
image rhina shy2 = At(Transform("ramenhinata shy2", zoom=0.7), sprite_highlight("hinata")) 
image rhina shy3 = At(Transform("ramenhinata shy3", zoom=0.7), sprite_highlight("hinata")) 
image rhina smiling1 = At(Transform("ramenhinata smiling1", zoom=0.7), sprite_highlight("hinata")) 
image rhina thinking1 = At(Transform("ramenhinata thinking1", zoom=0.7), sprite_highlight("hinata")) 
image rhina working_normal1 = At(Transform("ramenhinata working_normal", zoom=0.70), sprite_highlight("hinata")) 
image rhina working_pensive1 = At(Transform("ramenhinata working_pensive", zoom=0.7), sprite_highlight("hinata")) 
image rhina working_sad1 = At(Transform("ramenhinata working_sad", zoom=0.7), sprite_highlight("hinata")) 
image rhina working_smiling1 = At(Transform("ramenhinata working_smiling", zoom=0.7), sprite_highlight("hinata"))

#maid hinata groped
image rhina ass1 = At(Transform("ramenhinata ass1", zoom=0.7), sprite_highlight("hinata")) 
image rhina ass2 = At(Transform("ramenhinata ass2", zoom=0.7), sprite_highlight("hinata")) 
image rhina ass3 = At(Transform("ramenhinata ass3", zoom=0.7), sprite_highlight("hinata")) 

#dress hinata
image dhina normal1 = At(Transform("hinatadress normal", zoom=0.7), sprite_highlight("hinata")) 
image dhina shy1 = At(Transform("hinatadress shy", zoom=0.7), sprite_highlight("hinata")) 
image dhina shy2 = At(Transform("hinatadress shy2", zoom=0.7), sprite_highlight("hinata")) 


#himawarihome
image hima happy = At("himawari happy", sprite_highlight("himawari"))
image hima embarassed = At("himawari embarassed", sprite_highlight("himawari"))
image hima fearful = At("himawari fearful", sprite_highlight("himawari"))
image hima concerned = At("himawari concerned", sprite_highlight("himawari"))       
image hima surprised = At("himawari surprised", sprite_highlight("himawari"))        
image hima thinking = At("himawari thinking", sprite_highlight("himawari"))         
image hima lookingdown = At("himawari lookingdown", sprite_highlight("himawari")) # Doesn't exist 
image hima teasing = At("himawari teasing", sprite_highlight("himawari")) # Doesn't exist           
image hima normal = At("himawari normal normal", sprite_highlight("himawari"))             
image hima turn1 = At("himawari turnaway1", sprite_highlight("himawari"))           
image hima grope1 = At("himawari grope1", sprite_highlight("himawari")) # Doesn't exist           
image hima grope2 = At("himawari grope2", sprite_highlight("himawari")) # Doesn't exist          
image hima grope3 = At("himawari grope3", sprite_highlight("himawari")) # Doesn't exist         
image hima grope4 = At("himawari grope4", sprite_highlight("himawari")) # Doesn't exist
image hima laughing = At("himawari laughing", sprite_highlight("himawari")) # Doesn't exist
image hima mad = At("himawari mad", sprite_highlight("himawari"))
image hima mad3 = At("himawari mad3", sprite_highlight("himawari"))
image hima normal = At("himawari normal normal", sprite_highlight("himawari"))
image hima scared = At("himawari scared", sprite_highlight("himawari")) # Doesn't exist
image hima shy = At("himawari shy", sprite_highlight("himawari"))
image hima shy2 = At("himawari shy2", sprite_highlight("himawari")) # Doesn't exist
image hima shy3 = At("himawari shy3", sprite_highlight("himawari")) # Doesn't exist
image hima smug = At("himawari smug", sprite_highlight("himawari"))
image hima smug1 = At("himawari smug1", sprite_highlight("himawari"))
transform scale_matrix_transform:
    matrixtransform ScaleMatrix(0.94, 1.0, 1.0)
image hima smug2 = At("himawari smug2", sprite_highlight("himawari"), scale_matrix_transform)
image hima smug3 = At("himawari smug3", sprite_highlight("himawari"))
image hima smugshy = At(Transform("himawari smugshy", zoom=1.07), sprite_highlight("himawari"))
image hima snobturn = At("himawari snobturn", sprite_highlight("himawari"))
image hima spank1 = At("himawari spank1", sprite_highlight("himawari")) # Doesn't exist
image hima spank2 = At("himawari spank2", sprite_highlight("himawari")) # Doesn't exist
image hima walkaway = At("himawari walkaway", sprite_highlight("himawari"))
image hima worried1 = At("himawari worried1", sprite_highlight("himawari"))
image hima worried2 = At("himawari worried2", sprite_highlight("himawari"))


image hima comment0 = At("himawari comment0", sprite_highlight("himawari"))
image hima comment1 = At("himawari comment1", sprite_highlight("himawari"))
image hima comment2 = At("himawari comment2", sprite_highlight("himawari"))
image hima running0 = At("himawari running0", sprite_highlight("himawari"))
image hima running1 = At("himawari running1", sprite_highlight("himawari"))
image hima turnaway1 = At("himawari turnaway1", sprite_highlight("himawari"))
image hima turnaway2 = At("himawari turnaway2", sprite_highlight("himawari"))
image hima turnaway3 = At("himawari turnaway3", sprite_highlight("himawari"))


#buruma Himawari
image gymhima shy = At(Transform("opinion1_himt", zoom=0.7), sprite_highlight("himawari")) 
image gymhima shy2 = At(Transform("opinion2_himt beh", zoom=0.65), sprite_highlight("himawari"))
image gymhima smug = At(Transform("gymhima_smug_src", zoom=0.7), sprite_highlight("himawari"))
image gymhima concerned = At(Transform("opinion1_himt ass3", zoom=0.7), sprite_highlight("himawari")) 
image gymhima concerned2 = At(Transform("opinion1_himt ass1", zoom=0.7), sprite_highlight("himawari")) 



#bikini himawari
image bhima shy = At(Transform("hima_ss_shy", zoom=0.7), sprite_highlight("himawari")) 
image bhima normal = At(Transform("hima_ss_normal", zoom=0.7), sprite_highlight("himawari")) 
image bhima embarrassed = At(Transform("hima_ss_embarrassed", zoom=0.7), sprite_highlight("himawari"))
image bhima disgusted = At(Transform("hima_ss_disgusted", zoom=0.7), sprite_highlight("himawari"))
image bhima angry = At(Transform("hima_ss_angry", zoom=0.7), sprite_highlight("himawari"))



#sidechars
image demandingmen badguys1  = At("demandingmen normal badguys1", sprite_highlight("demandingmen"))
image demandingmen badguys2 = At("demandingmen normal badguys2", sprite_highlight("demandingmen"))


#Tsunade
image tsuna angry = At(Transform("tsunade angry", zoom=0.75, ypos=-30), sprite_highlight("tsunade"))
image tsuna angry2 = At(Transform("tsunade angry2", zoom=0.75, ypos=-30), sprite_highlight("tsunade"))
image tsuna annoyed = At(Transform("tsunade annoyed", zoom=0.75, ypos=-30), sprite_highlight("tsunade"))
image tsuna full = At(Transform("tsunade full", zoom=0.75, ypos=-30), sprite_highlight("tsunade"))
image tsuna normal = At(Transform("tsunade normal", zoom=0.75, ypos=-30), sprite_highlight("tsunade"))
image tsuna normal2 = At(Transform("tsunade normal2", zoom=0.75, ypos=-30), sprite_highlight("tsunade"))
image tsuna serious = At(Transform("tsunade serious", zoom=0.75, ypos=-30), sprite_highlight("tsunade"))
image tsuna shy = At(Transform("tsunade shy", zoom=0.75, ypos=-30), sprite_highlight("tsunade"))
image tsuna smug = At(Transform("tsunade smug", zoom=0.75, ypos=-30), sprite_highlight("tsunade"))


#Boss
image boss angry = At(Transform("obo angry", zoom=0.36), sprite_highlight("obo"))
image boss angry2 = At(Transform("obo angry2", zoom=0.35), sprite_highlight("obo"))
image boss angry3 = At(Transform("obo angry3", zoom=0.36), sprite_highlight("obo"))
image boss concerned = At(Transform("obo concerned", zoom=0.36), sprite_highlight("obo"))
image boss laugh = At(Transform("obo laugh", zoom=0.36), sprite_highlight("obo"))
image boss laugh2 = At(Transform("obo laugh2", zoom=0.36), sprite_highlight("obo"))
image boss normal = At(Transform("obo normal", zoom=0.36), sprite_highlight("obo"))
image boss scared = At(Transform("obo scared", zoom=0.36), sprite_highlight("obo"))

#Yoruichi
image yoru normal = At(Transform("yoruichi normal", zoom=0.36), sprite_highlight("yoruichi"))
image yoru normal2 = At(Transform("yoruichi normal2", zoom=0.36), sprite_highlight("yoruichi"))
image yoru shy = At(Transform("yoruichi shy", zoom=0.36), sprite_highlight("yoruichi"))
image yoru shy2 = At(Transform("yoruichi shy2", zoom=0.36), sprite_highlight("yoruichi"))
image yoru shy3 = At(Transform("yoruichi shy3", zoom=0.36), sprite_highlight("yoruichi"))
image yoru lookingbackt = At(Transform("yoruichi lookingbackt"), sprite_highlight("yoruichi"))

image yoru angry = At(Transform("yoruichi angry", zoom=0.36), sprite_highlight("yoruichi"))
image yoru angry2 = At(Transform("yoruichi angry2", zoom=0.36), sprite_highlight("yoruichi"))
image yoru angry3 = At(Transform("yoruichi angry3", zoom=0.36), sprite_highlight("yoruichi"))

image yoru disgust = At(Transform("yoruichi disgust", zoom=0.36), sprite_highlight("yoruichi"))
image yoru disgust2 = At(Transform("yoruichi disgust2", zoom=0.36), sprite_highlight("yoruichi"))

image yoru scared = At(Transform("yoruichi scared", zoom=0.36), sprite_highlight("yoruichi"))
image yoru scared2 = At(Transform("yoruichi scared2", zoom=0.36), sprite_highlight("yoruichi"))

image yoru obedient = At(Transform("yoruichi obedient", zoom=0.36), sprite_highlight("yoruichi"))
image yoru surprised = At(Transform("yoruichi surprised", zoom=0.36), sprite_highlight("yoruichi"))


#Yoruichicombat combat
image yoruc normal = At(Transform("yorucombat normal", zoom=0.8, ypos=-45), sprite_highlight("yoruichi"))
image yoruc snob = At(Transform("yorucombat snob", zoom=0.8, ypos=-45), sprite_highlight("yoruichi"))
image yoruc annoyed = At(Transform("yorucombat annoyed", zoom=0.75, ypos=-30), sprite_highlight("yoruichi"))


#sakura
image sakura 1 = At(Transform("sakura1t", zoom=0.58), sprite_highlight("sakura"))              
image sakura 2 = At(Transform("sakura2t", zoom=0.58), sprite_highlight("sakura"))

image sakura normal = At(Transform("sakura normalt", zoom=0.57), sprite_highlight("sakura")) 
image sakura angry = At(Transform("sakura angryt", zoom=0.57), sprite_highlight("sakura"))              
image sakura greet = At(Transform("sakura greett", zoom=0.57), sprite_highlight("sakura"))              
image sakura serious = At(Transform("sakura serioust", zoom=0.57), sprite_highlight("sakura"))              
image sakura shy = At(Transform("sakura shyt", zoom=0.59), sprite_highlight("sakura"))              
image sakura teasing = At(Transform("sakura teasingt", zoom=0.59), sprite_highlight("sakura"))              

#sakura red dress
image sakurad normal1 = At(Transform("sakuradress normal", zoom=0.7), sprite_highlight("sakura"))
image sakurad normal2 = At(Transform("sakuradress normal2", zoom=0.7), sprite_highlight("sakura"))
image sakurad teasing1 = At(Transform("sakuradress teasing", zoom=0.7), sprite_highlight("sakura"))


#sarada underwear
image sarada underwear_angry = At(Transform("sarada_underwear_angry1", zoom=0.56), sprite_highlight("sarada"))              
image sarada underwear_angry2 = At(Transform("sarada_underwear_angry2", zoom=0.56), sprite_highlight("sarada"))              
image sarada underwear_flustered = At(Transform("sarada_underwear_flustered1", zoom=0.56), sprite_highlight("sarada"))              
image sarada underwear_normal = At(Transform("sarada_underwear_normal1", zoom=0.56), sprite_highlight("sarada"))              
image sarada underwear_normal2 = At(Transform("sarada_underwear_normal2", zoom=0.56), sprite_highlight("sarada"))              
image sarada underwear_serious = At(Transform("sarada_underwear_serious1", zoom=0.56), sprite_highlight("sarada"))              

#sarada
image sarada 1 = At(Transform("sarada1t", zoom=0.55), sprite_highlight("sarada"))              
image sarada 2 = At(Transform("sarada2t", zoom=0.55), sprite_highlight("sarada"))

image sarada angry = At(Transform("sarada angryt", zoom=0.55), sprite_highlight("sarada"))              
image sarada angry2 = At(Transform("sarada angry2t", zoom=0.55), sprite_highlight("sarada"))              
image sarada angry3 = At(Transform("sarada angry3t", zoom=0.57), sprite_highlight("sarada"))              
image sarada annoyed = At(Transform("sarada annoyedt", zoom=0.52), sprite_highlight("sarada"))              
image sarada flustered = At(Transform("sarada flusteredt", zoom=0.55), sprite_highlight("sarada"))              
image sarada sad = At(Transform("sarada sadt", zoom=0.55), sprite_highlight("sarada"))              
image sarada shy = At(Transform("sarada shyt", zoom=0.55), sprite_highlight("sarada"))              
image sarada snob = At(Transform("sarada snobt", zoom=0.55), sprite_highlight("sarada"))
image sarada happy = At(Transform("sarada happyt", zoom=0.55), sprite_highlight("sarada"))              
image sarada fighting = At(Transform("sarada_fightingstance"), sprite_highlight("sarada"))              
      

#night merchant
image merchant 1 = At(Transform("night merchant1t", zoom=0.7), sprite_highlight("dio"))              
image merchant 2 = At(Transform("night merchant2t", zoom=0.7), sprite_highlight("dio"))


#tenten
image ten normal = At(Transform("tenten normal", zoom=0.7), sprite_highlight("tenten"))              
image ten sad1 = At(Transform("tenten sad1", zoom=0.7), sprite_highlight("tenten"))              
image ten sad2 = At(Transform("tenten sad2", zoom=0.7), sprite_highlight("tenten"))
image ten angry = At(Transform("npc_shopkeep2_idle", zoom=0.7), sprite_highlight("tenten"))               


#madame
image madame normal = At(Transform("rangi normal", zoom=0.56), sprite_highlight("madame"))
image madame normal2 = At(Transform("rangi normal2", zoom=0.56), sprite_highlight("madame"))
image madame normal3 = At(Transform("rangibu", zoom=0.56), sprite_highlight("madame"))
image madame angry = At(Transform("rangi angry", zoom=0.56), sprite_highlight("madame"))

image madame undress = At(Transform("bh rangi 1t", zoom=0.56), sprite_highlight("madame"))
image madame undress2 = At(Transform("bh rangi 2t", zoom=0.56), sprite_highlight("madame"))
image madame undress3 = At(Transform("bh rangi 3t", zoom=0.56), sprite_highlight("madame"))
image madame naked = At(Transform("bh rangi 4t", zoom=0.56), sprite_highlight("madame"))

#ramencharmer ramen / restaurant
image rcharmer normal1 = At(Transform("ramencharmer normal", zoom=0.7))
image rcharmer sceeming1 = At(Transform("ramencharmer sceeming", zoom=0.7))
image rcharmer perv1 = At(Transform("ramencharmer perv1", zoom=0.7))
image rcharmer perv2 = At(Transform("ramencharmer perv2", zoom=0.7))

#ramenoldpervert ramen / restaurant
image rold normal1 = At(Transform("ramenold normal", zoom=0.7))
image rold pervert1 = At(Transform("ramenold pervert", zoom=0.7))
image rold caught1 = At(Transform("ramenold caught", zoom=0.7))

#ramenboy ramen / restaurant
image rboy normal1 = At(Transform("ramenboy normal", zoom=0.7))
image rboy angry1 = At(Transform("ramenboy angry", zoom=0.7))
image rboy smirk1 = At(Transform("ramenboy smirk", zoom=0.7))
image rboy crying1 = At(Transform("ramenboy crying", zoom=0.7))



#yoruichi ass
# image yoru ass = At(Transform("yoruichi ass", zoom=0.36), sprite_highlight("yoruichi"))
# image yoru ass2 = At(Transform("yoruichi ass2", zoom=0.36), sprite_highlight("yoruichi"))
# image yoru ass3 = At(Transform("yoruichi ass3", zoom=0.36), sprite_highlight("yoruichi"))




#--------------------------------------------------------------------------------------





        



