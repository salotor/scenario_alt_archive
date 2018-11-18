label alt_day6_us_7dl_start:
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    call alt_day6_us_px_vars
    call alt_day6_us_7dl_vars
    if alt_day4_neu_us_pixies == 3:
        $ alt_chapter(6, u"Огоньки. Утро")
        call alt_day6_us_px_begin
    else:
        $ alt_chapter(6, u"Ульяна. 7ДЛ. Утро")
        call alt_day6_us_7dl_begin
    pause(1)
    call alt_day6_us_7dl_exercises
    pause(1)
    call alt_day6_us_7dl_breakfast
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    if alt_day4_neu_us_pixies == 3:
        $ alt_chapter(6, u"Огоньки. Утро.")
        call alt_day6_us_px_carrier
        pause(1)
        $ alt_chapter(6, u"Огоньки. День")
        call alt_day6_us_px_dinner
        pause(1)
        call alt_day6_us_px_Lena
        pause(1)
        if persistent.us_7dl_good:
            call alt_day6_us_px_party_sl
            pause(1)
        else:
            call alt_day6_us_px_far_gate
        pause(1)
        $ alt_chapter(6, u"Огоньки. Концерт")
        call alt_day6_us_7dl_concert
    else:
        $ alt_chapter(6, u"Ульяна. 7ДЛ. Утро.")
        call alt_day6_us_7dl_helping
        pause(1)
        if alt_day6_us_7dl_mi_friends == 2:
            call alt_day6_us_7dl_preps
        elif alt_day6_us_7dl_sl_friends == 2:
            call alt_day6_us_7dl_warehouse
        else:
            call alt_day6_us_7dl_un_met
        pause(1)
        $ alt_chapter(6, u"Ульяна. 7ДЛ. День")
        call alt_day6_us_7dl_dinner
        pause(1)
        if (alt_day6_us_7dl_mi_friends == 2) or (alt_day6_us_7dl_sl_friends == 2):
            call alt_day6_us_7dl_soundcheck
            pause(1)
            call alt_day6_us_7dl_concert
        else:
            call alt_day6_us_7dl_button
            pause(1)
            if alt_day6_us_7dl_tr:
                $ alt_chapter(6, u"Ульяна. 7ДЛ. Ррромантика")
                call alt_day6_us_7dl_rendezvous
            else:
                $ alt_chapter(6, u"Ульяна. 7ДЛ. Концерт")
                call alt_day6_us_7dl_concert
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    if alt_day4_neu_us_pixies == 3:
        $ alt_chapter(6, u"Огоньки. Вечер")
    else:
        $ alt_chapter(6, u"Ульяна. 7ДЛ. Вечер")
    call alt_day6_us_7dl_supper
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    call alt_day6_us_7dl_disco
    pause(1)
    if alt_day4_neu_us_pixies == 2:
        call alt_day6_us_7dl_tea
    elif alt_day4_neu_us_pixies == 3:
        call alt_day6_us_px_afterwords
    pause(1)
    call alt_day6_us_7dl_sleeptime
    pause(1)
    jump alt_day7_us_7dl_start
    
label alt_day7_us_7dl_start:
    call alt_day7_us_px_vars
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    if alt_day4_neu_us_pixies == 3:
        call alt_day7_us_px_vars
        if alt_day6_us_px_sl_join:
            $ routetag = "us7dl_good_surp"
        else:
            $ routetag = "us7dl_good"
        $ alt_chapter(7, u"Огоньки. Утро")
    else:
        if alt_day6_us_7dl_tr:
            $ routetag = "us7dl_bad_laugh"
        elif (alt_day6_us_7dl_mi_friends == 3) or (alt_day6_us_7dl_un_friends == 3):
            $ routetag = "us7dl_bad"
        else:
            $ routetag = "us7dl_bad_sad"
        $ alt_chapter(7, u"Ульяна. 7ДЛ. Утро")
    call alt_day7_us_7dl_begin
    pause(1)
    call alt_day7_us_7dl_breakfast
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    if alt_day4_neu_us_pixies == 3:
        call alt_day7_us_px_escape
        if alt_day6_us_px_sl_join:
            pause(1)
            $ alt_chapter(7, u"Огоньки. Автобус")
            call alt_day7_us_px_bus
            pause(1)
            if alt_day7_us_px_escaped:
                call alt_day7_us_px_wastelands
                pause(1)
                $ persistent.sprite_time = "prolog"
                $ prolog_time()
                $ alt_chapter(7, u"Огоньки. Сказка")
                call alt_day7_us_px_fairytale
                return
            else:
                call alt_day7_us_px_mourning
        else:
            call alt_day7_us_px_mourning
        $ persistent.sprite_time = "prolog"
        $ prolog_time()
        $ alt_chapter(7, u"Огоньки. Эпилог")
        call alt_day7_us_px_dejavu
        pause(1)
        return
    elif alt_day6_us_7dl_tr or (alt_day6_us_7dl_mi_friends == 3) or (alt_day6_us_7dl_un_friends == 3):
        call alt_day7_us_7dl_rendezvous2
    else:
        call alt_day7_us_7dl_packing
    pause(1)
    $ alt_chapter(7, u"Ульяна. 7ДЛ. Отъезд")
    call alt_day7_us_7dl_leaving
    $ persistent.sprite_time = "prolog"
    $ prolog_time()
    if (persistent.us_7dl_un or persistent.us_7dl_mi) and persistent.us_px_rf_good and (alt_day4_neu_us_pixies != 0) and alt_day6_us_7dl_tr:
        $ alt_chapter(7, u"Ульяна. Спасибо.")
        call alt_day7_us_7dl_ever_after
        pause(1)
        return
    $ alt_chapter(7, u"Ульяна. 7ДЛ. Эпилог")
    call alt_day7_us_7dl_wakeup
    pause(1)
    if alt_day6_us_7dl_tr:
        call alt_day7_us_7dl_reunite
    else:
        if alt_day6_us_7dl_mi_friends == 3:
            call alt_day7_us_7dl_mikuforever
        elif alt_day6_us_7dl_un_friends == 3:
            call alt_day7_us_7dl_lenaforever
        else:
            call alt_day7_us_7dl_bad
    pause(1)
    return