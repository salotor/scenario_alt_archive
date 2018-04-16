label alt_day4_un_start:
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(4, u"Утро")
    if lp_un == 14 and alt_day3_technoquest_st3:
        scene bg int_aidpost_day with dissolve
        "Последний танец - вместо того, чтобы танцевать его с Леной, я, дурак, пошёл помогать этим олухам."
        "Вот и помог."
    window hide
    show spill_red with dspr
    $ renpy.pause(2, hard=True)
    show spill_gray with dspr
    $ renpy.pause(2, hard=True)
    show alt_credits timeskip_dev at truecenter with dissolve2
    $ renpy.pause(4, hard=True)
    with dissolve2
    window hide
    return

label alt_day4_un_cl_dinner:
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(4, u"Лена. Обед")
    play ambience ambience_dining_hall_full fadein 3
    scene bg int_dining_hall_people_sunset  with fade
    "В столовой была куча народа — и это несмотря на то, что большинство из них родители растащили погулять."
    "Странные люди, странные приоритеты."
    "К счастью, меня это не очень интересовало."
    "Куда интереснее мне были глаза напротив."
    show un smile pioneer with dissolve
    "Зел-лёные такие!"
    window hide
    show spill_red with dspr
    $ renpy.pause(2, hard=True)
    show spill_gray with dspr
    $ renpy.pause(2, hard=True)
    show alt_credits timeskip_dev at truecenter with dissolve2
    $ renpy.pause(4, hard=True)
    with dissolve2
    window hide
    return