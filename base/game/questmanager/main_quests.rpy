define boruto1 = ( #Add quests here

    #Job intro quest
    Quest("bojob_1", ("Get a Job"), ("General"), "unlocked"),

    #Money problems intro quest
    Quest("bojob_2", ("[hin_name]'s debts"), ("General"), "unlocked"),

    #shower Quest in events_bathroom
    Quest("bo_shower_1", ("Just a peek!"), ("General"), "pending"),

    #hima Quest search in her bedroom
    Quest("bohim_1", ("[him_name]'s garments"), ("General"), "pending"),

    #Hima quest talk in her bedroom
    Quest("bohim_2", ("A plan for [him_name]"), ("General"), "pending"),

    #Hima quest talk in her bedroom (part 2 - swimsuit modeling etc)
    Quest("bohim_3", ("A plan for [him_name] (continued)"), ("General"), "pending"),
    Quest("1_bohim_3", ("Purchase a bikini and convince [him_name] to wear it"), ("A plan for [him_name] (continued)"), "pending"),
    Quest("2_bohim_3", ("Take some sexy shots of [him_name] in a bikini"), ("A plan for [him_name] (continued)"), "pending"),
    Quest("3_bohim_3", ("Not yet in game 1"), ("A plan for [him_name] (continued)"), "pending", wip=True),
    Quest("4_bohim_3", ("Not yet in game 2"), ("A plan for [him_name] (continued)"), "pending", wip=True),

    #Hina wake up quest + laundry
    Quest("bohin_1", ("[hin_name]'s hospitality"), ("General"), "pending"),

    #Shopkeeper market quest
    Quest("boshop_1", ("Shopkeeper's burden"), ("General"), "pending"),



    

    #work quest
    Quest("job_1", ("Look for a job using the map"), ("Get a Job"), "in progress"),
    Quest("job_2", ("Show up to work a few times"), ("Get a Job")),
    Quest("job_3", ("Investigate workplace during nights"), ("Get a Job")),
    Quest("job_4", ("Find out more about what's going on"), ("Get a Job")),
    Quest("job_5", ("Find a way to help or corrupt Yoru"), ("Get a Job"), wip=True),

    #hinata debt quest
    Quest("job2_1", ("Save 200$ until Day 7"), ("[hin_name]'s debts"), "in progress"),
    Quest("job2_2", ("Save 300$ until Day 14"), ("[hin_name]'s debts"), wip=False),
    Quest("job2_3", ("Convince [hin_name] to work with you"), ("[hin_name]'s debts")),

    

    )

#Hinata's quests
define hinata1 = ( # Add your quests below, don't forget the commas !
    Quest("hinata1love", ("[hin_name]'s Love path"), ("General"), "unlocked"),
    Quest("hinata1hatred", ("[hin_name]'s Hatred path"), ("General"), "unlocked"), 

    Quest("hin1L_1", ("Carry [hin_name] to her bedroom after she slips"), ("[hin_name]'s Love path"), "pending"), # Available
    Quest("hin1L_2", ("Massage [hin_name]'s entire body in the living room"), ("[hin_name]'s Love path"), "pending"), # Available
    # Quest("hin1L_3", ("Help [hin_name] with her financial struggles."), ("[hin_name]'s Love path"), "pending", wip=True),
    Quest("hin1L_4", ("Jerk off while [hin_name] 'helps' when waking up"), ("[hin_name]'s Love path"), "pending"), # Available
    Quest("hin1L_5", ("Have [hin_name] 'help' you in the shower"), ("[hin_name]'s Love path"), "pending"), # Available
    # Quest("hin1L_6", ("Find the 'Love' advancement event!"), ("[hin_name]'s Love path"), "pending"),

    Quest("hin1H_1", ("Use [hin_name]'s body after she slips"), ("[hin_name]'s Hatred path"), "pending"), # Available
    Quest("hin1H_2", ("Take advantage of [hin_name]'s body in the living room"), ("[hin_name]'s Hatred path"), "pending"), # Available
    # Quest("hin1H_3", ("Don't help [hin_name] with her financial struggles"), ("[hin_name]'s Hatred path"), "pending", wip=True),
    Quest("hin1H_4", ("Expose yourself to [hin_name] in the laundry room"), ("[hin_name]'s Hatred path"), "pending"), # Available
    Quest("hin1H_5", ("Defile [hin_name] while she is asleep "), ("[hin_name]'s Hatred path"), "pending"), # Available
    # Quest("hin1H_6", ("Find the 'hatred' advancement event!"), ("[hin_name]'s Hatred path"), "pending"),

    )

define hinata2 = ( # Level 2 quests
    Quest("hinata2love", ("[hin_name]'s Love path"), ("General"), "unlocked", questlevel=2),
    Quest("hinata2hatred", ("[hin_name]'s Hatred path"), ("General"), "unlocked", questlevel=2), 

    Quest("hin2L_1", ("Help [hin_name] unwind"), ("[hin_name]'s Love path"), "pending", questlevel=2),
    Quest("1_hin2L", ("Talk with Sakura about helping [hin_name]"), ("[hin_name]'s Love path"), "pending", questlevel=2),
    Quest("2_hin2L", ("Surprise [hin_name] in the Living Room at night with Wine and a Black Dress"), ("[hin_name]'s Love path"), "pending", questlevel=2),
    Quest("3_hin2L", ("Have a romantic night with only [hin_name]"), ("[hin_name]'s Love path"), "pending", wip=True, questlevel=2), #WIP
    Quest("hin2L_2", ("Convince [hin_name] to offer a 'helping hand'"), ("[hin_name]'s Love path"), "pending", questlevel=2),
    Quest("4_hin2L", ("Cuddle with [hin_name] as she provides stress relief"), ("[hin_name]'s Love path"), "pending", questlevel=2),
    Quest("5_hin2L", ("Pretend to be asleep while [hin_name] is 'assisting' you"), ("[hin_name]'s Love path"), "pending", questlevel=2),

    Quest("hin2H_1", ("Pressure [hin_name] to jerk you off"), ("[hin_name]'s Hatred path"), "pending", questlevel=2),
    Quest("1_hin2H", ("Manipulate [hin_name] in creative ways to use her hands for your pleasure"), ("[hin_name]'s Hatred path"), "pending", questlevel=2),
    Quest("hin2H_2", ("Help [hin_name] unwind"), ("[hin_name]'s Hatred path"), "pending", questlevel=2),
    Quest("2_hin2H", ("Talk with Sakura about helping [hin_name]"), ("[hin_name]'s Hatred path"), "pending", questlevel=2),
    Quest("3_hin2H", ("Tempt [hin_name] in the Living Room at night with Wine and a Black Dress"), ("[hin_name]'s Hatred path"), "pending", questlevel=2),
    Quest("4_hin2H", ("Find another way to convince [hin_name] to have fun together"), ("[hin_name]'s Hatred path"), "pending", wip=True, questlevel=2), #WIP

    )
    
#Himawari's quests
define himawari1 = ( # Add your quests below, don't forget the commas !
    Quest("himawari1love", ("[him_name]'s Love path"), ("General"), "unlocked"),
    Quest("himawari1hatred", ("[him_name]'s Hatred path"), ("General"), "unlocked"), 

    Quest("him1L_1", ("Wrestle with [him_name] and have her admit 'defeat'"), ("[him_name]'s Love path"), "pending"), #Updated: wrestling - Available
    Quest("him1L_2", ("'Convince' [him_name] to taste your 'syrup'"), ("[him_name]'s Love path"), "pending"), #Updated: blindfold - Available
    # Quest("him1L_3", ("[him_name]'s Love path"), ("[him_name]'s Love path"), "pending", wip=True), #todo
    Quest("him1L_4", ("Help [him_name] during the fly incident"), ("[him_name]'s Love path"), "pending"), # Available
    # Quest("him1L_5", ("Find the 'Love' advancement event!"), ("[him_name]'s Love path"), "pending", wip=True),

    Quest("him1H_1", ("Wrestle with [him_name] and serve her a 'punishment'"), ("[him_name]'s Hatred path"), "pending"), #Updated: wrestling - Available
    Quest("him1H_2", ("Trick [him_name] into tasting your 'syrup'"), ("[him_name]'s Hatred path"), "pending"), #Updated: blindfold - Available
    Quest("him1H_3", ("Soil her panties while fantasizing"), ("[him_name]'s Hatred path"), "pending"), # Available
    Quest("him1H_4", ("Take advantage of [him_name] during the fly incident"), ("[him_name]'s Hatred path"), "pending"), # Available
    # Quest("him1H_5", ("Find the 'hatred' advancement event!"), ("[him_name]'s Hatred path"), "pending", wip=True),

    )

define himawari2 = ( # Level 2 quests
    Quest("himawari2love", ("[him_name]'s Love path"), ("General"), "unlocked", questlevel=2),
    Quest("himawari2hatred", ("[him_name]'s Hatred path"), ("General"), "unlocked", questlevel=2), 

    Quest("him2L_1", ("Help [him_name] progress further in her modelling career"), ("[him_name]'s Love path"), "pending", questlevel=2),
    Quest("him2L_2", ("???"), ("[him_name]'s Love path"), "pending", wip=True, questlevel=2),
    Quest("him2L_3", ("???"), ("[him_name]'s Love path"), "pending", wip=True, questlevel=2),
    Quest("him2L_4", ("???"), ("[him_name]'s Love path"), "pending", wip=True, questlevel=2),
    Quest("him2L_5", ("???"), ("[him_name]'s Love path"), "pending", wip=True, questlevel=2),

    Quest("him2H_1", ("Force [him_name] to model for you in a bikini"), ("[him_name]'s Hatred path"), "pending", questlevel=2),
    Quest("him2H_2", ("???"), ("[him_name]'s Hatred path"), "pending", wip=True, questlevel=2),
    Quest("him2H_3", ("???"), ("[him_name]'s Hatred path"), "pending", wip=True, questlevel=2),
    Quest("him2H_4", ("???"), ("[him_name]'s Hatred path"), "pending", wip=True, questlevel=2),
    Quest("him2H_5", ("???"), ("[him_name]'s Hatred path"), "pending", wip=True, questlevel=2),

    )