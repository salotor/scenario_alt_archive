label alt_day5_sl_wh_start:
    call alt_day5_sl_wh_vars
    pause(1)
    $ renpy.save_persistent()
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(5, u"Ведьма. Утро.")
    call alt_day5_sl_wh_begin
    pause(1)
    $ renpy.save_persistent()
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