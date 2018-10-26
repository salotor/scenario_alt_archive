label alt_day4_mi_cl_start:
    call alt_day4_mi_cl_vars
    pause(1)
    $ renpy.save_persistent()
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(4, u"Мику. Утро. Медпункт")
    call alt_day4_mi_start
    pause(1)
    $ renpy.save_persistent()
    call alt_day4_mi_cs_med_play
    pause(1)
    $ renpy.save_persistent()
    if not alt_day4_mi_rival_won:
        $ persistent.sprite_time = "day"
        $ day_time()
        $ alt_chapter(4, u"Мику. Медпункт. Дежурство")
        call alt_day4_mi_duty
        pause(1)
        $ renpy.save_persistent()
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(4, u"Мику. Попытка ужина.")
        call alt_day4_mi_supper_sick
        pause(1)
        $ renpy.save_persistent()
    else:
        if alt_day4_mi_mi2midj_transit:
            $ persistent.sprite_time = "day"
            $ day_time()
            $ alt_chapter(4, u"Мику. DJ. Свидание.")
            call alt_day4_mi_visit_sick
            pause(1)
            $ renpy.save_persistent()
            call alt_day4_mi_rps3
            pause(1)
            $ renpy.save_persistent()
            call alt_day4_mi_movealong
            pause(1)
            $ renpy.save_persistent()
            call alt_day4_mi_med_EV
            pause(1)
            $ renpy.save_persistent()
            call alt_day4_mi_back2radio
            pause(1)
            $ renpy.save_persistent()
            if alt_day4_mi_comfort:
                $ persistent.sprite_time = "sunset"
                $ sunset_time()
                $ alt_chapter(4, u"Мику. DJ. Вечер")
                call alt_day4_mi_date
                pause(1)
                $ renpy.save_persistent()
                jump alt_day5_start_mi_dj
            else:
                $ persistent.sprite_time = "sunset"
                $ sunset_time()
                $ alt_chapter(4, u"Мику. Вечер.")
                call alt_day4_mi_date_sick
                pause(1)
                $ renpy.save_persistent()
                call alt_day4_mi_xroad
                pause(1)
                $ renpy.save_persistent()
                $ night_time()
                $ persistent.sprite_time = "night"
                call alt_day4_mi_herbs
                pause(1)
                $ renpy.save_persistent()
                jump alt_day5_mi_cl_start
        else:
            $ persistent.sprite_time = "day"
            $ day_time()
            $ alt_chapter(4, u"Мику. Клуб.")
            call alt_day4_mi_club_sick
            pause(1)
            $ renpy.save_persistent()
            call alt_day4_mi_med_EV
            pause(1)
            $ renpy.save_persistent()
    call alt_day4_mi2sl_mi
    pause(1)
    $ renpy.save_persistent()
    if not alt_day4_mi_dance:
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(4, u"Мику. Вечер.")
        call alt_day4_mi_date_sick
        pause(1)
        $ renpy.save_persistent()
        call alt_day4_mi_xroad
        pause(1)
        $ renpy.save_persistent()
        $ night_time()
        $ persistent.sprite_time = "night"
        call alt_day4_mi_herbs
        pause(1)
        $ renpy.save_persistent()
    jump alt_day5_mi_cl_start

label alt_day5_mi_cl_start:
    # call alt_day5_mi_cl_vars
    pause(1)
    $ renpy.save_persistent()
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(5, u"Мику. Утро.")
    call alt_day5_mi_begin
    pause(1)
    $ renpy.save_persistent()
    return