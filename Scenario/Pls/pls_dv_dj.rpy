label alt_day4_dv_dj_start:
    # call alt_day4_dv_dj_vars
    pause(1)
    if not alt_day4_dv_7dl_walkman_presented:
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(4, u"Alice DJ. Утро")
        call alt_day4_dv_dj_begin
        pause(1)
    else:
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(4, u"Alice DJ. День.")
        call alt_day4_dv_7dl2dj_transit
        pause(1)
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