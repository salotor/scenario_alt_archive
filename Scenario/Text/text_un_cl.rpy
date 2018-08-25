label alt_day4_un_begin:
    if lp_un == 14 and alt_day3_technoquest_st3:
        scene bg int_aidpost_day with dissolve
        "Последний танец - вместо того, чтобы танцевать его с Леной, я, дурак, пошёл помогать этим олухам."
        "Вот и помог."
    stop music fadeout 3
    stop ambience fadeout 6
    window hide
    with fade
    return
 
label alt_day4_un_dinner:
    play ambience ambience_dining_hall_full fadein 3
    scene bg int_dining_hall_people_sunset  with fade
    "В столовой была куча народа — и это несмотря на то, что большинство из них родители растащили погулять."
    "Странные люди, странные приоритеты."
    "К счастью, меня это не очень интересовало."
    "Куда интереснее мне были глаза напротив."
    show un smile pioneer with dissolve
    "Зел-лёные такие!"
    stop music fadeout 3
    stop ambience fadeout 6
    window hide
    with fade
    return