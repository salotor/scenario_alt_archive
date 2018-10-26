label alt_day4_dv_cl_start:
    # call alt_day4_dv_cl_vars
    pause(1)
    $ renpy.save_persistent()
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(4, u"Алиска. Утро")
    call alt_day4_dv_begin
    pause(1)
    $ renpy.save_persistent()
    jump alt_day5_dv_cl_start

label alt_day5_dv_cl_start:
    # call alt_day5_dv_cl_vars
    pause(1)
    $ renpy.save_persistent()
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(5, u"Алиска. Утро")
    call alt_day5_dv_begin
    pause(1)
    $ renpy.save_persistent()
    return