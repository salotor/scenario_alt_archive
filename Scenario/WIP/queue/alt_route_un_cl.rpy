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