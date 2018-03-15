label alt_day2_start:
    call alt_day2_vars
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    $ alt_chapter(2, u"Пробуждение")
    call alt_day2_begin
    pause(1)
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    $ alt_chapter(2, u"Линейка")
    call alt_day2_lineup
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(2, u"Завтрак")
    call alt_day2_bf
    pause(1)
    call alt_day2_guide
    pause(1)
    if alt_day1_un_dated != 1:
        call alt_day2_convoy
        pause(1)
    call alt_day2_map_prepare
    pause(1)
    call alt_day2_event_estrade
    pause(1)
    if alt_day2_rendezvous == 3:
        if alt_day2_loki_minijack:
            $ persistent.sprite_time = "day"
            call alt_day2_dubstep2
        else:
            call alt_day2_phone
    else:
        call alt_day2_dubstep
        pause(1)
        if alt_day2_loki_minijack:
            call alt_day2_dubstep2
    pause(1)
    call alt_day2_dinner
    pause(1)
    if alt_day2_us_escape:
        $ persistent.sprite_time = "day"
        $ day_time()
        $ alt_chapter(2, u"Великий побег.")
        call alt_day2_grand_escape
    else:
        $ persistent.sprite_time = "day"
        $ day_time()
        $ alt_chapter(2, u"Тихий час.")
        call alt_day2_siesta
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(2, u"Турнир")
    call alt_day2_tournament
    pause(1)
    if alt_day2_walk == 2:
        call alt_day2_walk_sl
    else:
        call alt_day2_walk_alone
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(2, u"Ультиматум")
    call alt_day2_ultim
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(2, u"Турнир")
    call alt_day2_cards
    pause(1)
    call alt_day2_tournament_prep # добавить в турнир return вместо jump alt_day2_supper
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(2, u"Ужин")
    call alt_day2_supper
    pause(1)
    if alt_day2_slot_us_cake: # новая переменная
        call alt_day2_slot_us_try
        pause(1)
        if lp_us > 1:
            call alt_day2_slot_us
        else:
            call alt_day2_sup2
            pause(1)
            if alt_day2_dv_chased:
                call alt_day2_eventEv_beach1
                pause(1)
                if lp_dv > 3 and alt_day2_dv_bet_approve:
                    $ alt_day2_date = 3
                    call alt_day2_slot_dv
                else:
                    pass
            else:
                call alt_day2_mapEv_prepare
    else:
        call alt_day2_sup2
        pause(1)
        if alt_day2_dv_chased:
            call alt_day2_eventEv_beach1
            pause(1)
            if lp_dv > 3 and alt_day2_dv_bet_approve:
                $ alt_day2_date = 3
                call alt_day2_slot_dv
            else:
                pass
        else:
            call alt_day2_mapEv_prepare
    pause(1)
    $ night_time ()
    $ persistent.sprite_time = "night"
    call alt_day2_dream
    pause(1)
    jump alt_day3_start
