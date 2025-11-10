image vfx_lightning_web = Movie(play="images/effects/attack.webm", mask="images/effects/attack_mask.webm", loop=False)
image speedlines = Movie(play="images/effects/anime_speedlines.webm", mask="images/effects/anime_speedlines_mask.webm", loop=True)
image blue_point = Movie(play="images/effects/blue_point.webm", mask="images/effects/blue_point_mask.webm", loop=False,size=(1280,720))
image charge_lightning = Movie(play="images/effects/charge_lightning.webm", mask="images/effects/charge_lightning_mask.webm", loop=False,size=(1280,720))
image impact = Movie(play="images/effects/impact.webm", mask="images/effects/impact_mask.webm", loop=False,size=(1280,720))
image lightning_transition1 = Movie(play="images/effects/lightning_transition1.webm", mask="images/effects/lightning_transition1_mask.webm", loop=False,size=(1280,720))
image lightning1 = Movie(play="images/effects/lightning1.webm", mask="images/effects/lightning1_mask.webm", loop=False,size=(1280,720))
image notesure2 = Movie(play="images/effects/notesure2.webm", mask="images/effects/notesure2_mask.webm", loop=False,size=(1280,720))
image notsure = Movie(play="images/effects/notsure.webm", mask="images/effects/notsure_mask.webm", loop=False,size=(1280,720))
image powerup1 = Movie(play="images/effects/powerup1.webm", mask="images/effects/powerup1_mask.webm", loop=False,size=(1280,720))
image powerup2 = Movie(play="images/effects/powerup2.webm", mask="images/effects/powerup2_mask.webm", loop=True,size=(1280,720))
image punch1 = Movie(play="images/effects/punch1.webm", mask="images/effects/punch1_mask.webm", loop=False,size=(1280,720))
image punch2 = Movie(play="images/effects/punch2.webm", mask="images/effects/punch2_mask.webm", loop=False,size=(1280,720))
image punch3 = Movie(play="images/effects/punch3.webm", mask="images/effects/punch3_mask.webm", loop=False,size=(1280,720))
image red_point = Movie(play="images/effects/red_point.webm", mask="images/effects/red_point_mask.webm", loop=False,size=(1280,720))
image smoke = Movie(play="images/effects/smoke.webm", mask="images/effects/smoke_mask.webm", loop=False,size=(1280,720))
image red_shockwave = Movie(play="images/effects/red_shockwave.webm",loop=False,size=(1280,720))


label vfx_tests:
    show vfx_lightning_web
    "vfx_lightning_web"
    show speedlines with dissolve
    "speedlines"
    hide speedlines
    show blue_point
    "blue_point"
    show charge_lightning
    "charge_lightning"
    show impact
    "impact"
    show lightning_transition1
    "lightning_transition1"
    show lightning1
    "lightning1"
    show notesure2
    "notesure2"
    show notsure
    "notsure"
    show powerup1
    "powerup1"
    show powerup2
    "powerup2"
    show punch1
    "punch1"
    show punch2
    "punch2"
    show punch3
    "punch3"
    show red_point
    "red_point"
    show smoke
    "smoke"
    show red_shockwave
    "red_shockwave"
    