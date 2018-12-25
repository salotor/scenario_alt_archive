label alt_day4_neu_begin:
    call alt_day4_neu_us_vars
    call alt_day4_sl_cl_vars
    call alt_day4_un_7dl_vars
    call alt_day4_un_fz_vars
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(4, u"Одиночка. Утро")
    if alt_day3_dv_evening:
        call alt_day4_neu_dv
        pause(1)
    elif alt_day3_technoquest_st3 == 2:
        call alt_day4_neu_aid
        pause(1)
        if alt_day3_un_med_help != 0:
            call alt_day4_neu_aid_un
            pause(1)
            if alt_day4_neu_transit == 11:
                jump alt_day4_un_cl_dinner
        elif (counter_sl_cl == 7) or (lp_sl >= 13):
            call alt_day4_neu_aid_sl
            pause(1)
            if alt_day4_neu_transit == 2:
                $ mt_pt = 0
                $ d3_pt = 0
                $ us_pt = 0
                $ lp_us -= 3
                $ routetag = "sl"
                jump alt_day4_sl_start
        else:
            call alt_day4_neu_aid_generic
            pause(1)
        if alt_day4_neu_transit == 6:
            call alt_day4_neu_mt
            pause(1)
        elif alt_day4_neu_transit == 5:
            call alt_day4_neu_us
            pause(1)
    else:
        call alt_day4_neu_home
        pause(1)
        if alt_day3_us_bugs == 1:
            $ alt_day4_neu_transit = 5
            call alt_day4_neu_us
            pause(1)
        elif alt_day3_un_med_help != 0:
            call alt_day4_neu_un
            pause(1)
            if alt_day4_neu_transit == 1:
                $ mt_pt = 0
                $ d3_pt = 0
                $ us_pt = 0
                if persistent.hentai_un_old_7dl:
                    $ alt_un_old_hentai = True
                jump alt_day4_un_7dl_start
        elif alt_day3_mi_date:
            call alt_day4_neu_mi
            pause(1)
        else:
            call alt_day4_neu_sl
            pause(1)
            if alt_day4_neu_transit == 6:
                call alt_day4_neu_mt
                pause(1)
            elif alt_day4_neu_transit == 5:
                call alt_day4_neu_us
                pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(4, u"Одиночка. День")
    call alt_day4_neu_dinner
    pause(1)
    call alt_day4_neu_curl
    pause(1)
    if herc:
        return
        #jump alt_day4_noir_start
    call alt_day4_neu_lunch 
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(4, u"Одиночка. Вечер")
    call alt_day4_neu_supper
    pause(1)
    if alt_day4_neu_mt_fire or alt_day4_neu_us_snake:
        call alt_day4_neu_map_me_mt_house
        if alt_day4_neu_mt_diary:
            call alt_day4_neu_mt_diary_vol1
            pause(1)
        elif alt_day4_neu_us_snake:
            call alt_day4_neu_us_guards
            pause(1)
            if alt_day4_neu_us_pixies:
                call alt_day4_neu_us_launch
                pause(1)
        else:
            call alt_day4_neu_map_dining_hall
            pause(1)
    else:
        call alt_day4_neu_map_dining_hall
        pause(1)
    call alt_day4_neu_sleeptime
    pause(1)
    jump alt_day5_neu_begin
    
label alt_day5_neu_begin:
    call alt_day5_neu_us_vars
    call alt_day5_mt_7dl_vars
    call alt_day5_us_7dl_vars
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(5, u"Одиночка. Утро")
    if alt_day4_neu_us_pixies:
        call alt_day5_morningdream
        pause(1)
    call alt_day5_neu_start
    pause(1)
    call alt_day5_neu_breakfast
    pause(1)
    if alt_day5_neu_candle == 1:
        call alt_day5_neu_along
        pause(1)
        call alt_day5_neu_cndl
        pause(1)
    elif alt_day5_neu_candle == 2:
        call alt_day5_neu_cndl
        pause(1)
    elif alt_day5_neu_candle == 3:
        call alt_day5_neu_gaming
        pause(1)
    elif alt_day4_neu_us_pixies:
        call alt_day5_neu_arrest
        pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(5, u"Одиночка. Обед")
    call alt_day5_neu_dinner
    pause(1)
    if alt_day4_neu_us_pixies == 2:
        call alt_day5_neu_us_career
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(5, u"Одиночка. Вечер")
        call alt_day5_neu_us_punishment
        pause(1)
        if alt_day5_neu_us_stores:
            call alt_day5_neu_us_warm_evening
            pause(1)
        else:
            call alt_day5_neu_us_hungry
            pause(1)
        call alt_day5_neu_us_sleetptime
        pause(1)
        if alt_day4_neu_us_pixies == 3:
            $ routetag = "us7dl_good"
        else:
            $ routetag = "us7dl_bad"
        jump alt_day6_us_7dl_start
        pause(1)
        return
    else:
        call alt_day5_neu_mi_estrade
        pause(1)
        call alt_day5_neu_lunch
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(5, u"Одиночка. Вечер")
        call alt_day5_neu_supper
        pause(1)
        call alt_day5_neu_evening
        pause(1)
        $ alt_chapter(5, u"Одиночка. Костёр")
        call alt_day5_neu_campfire_doom
        pause(1)
        call alt_day5_neu_sleepnight
        pause(1)
        if mt_pt >= 7 and alt_day5_neu_mt_voyeur != 0:
            $ routetag = "mt7dl"
            call alt_day5_neu_mt_selector
            pause(1)
            if alt_day5_neu_mt_diary:
                call alt_day5_neu_mt_retrib
            elif alt_day5_mt_7dl_hentai:
                call alt_day5_neu_mt_tea_party
            jump alt_day6_mt_7dl_start
        elif us_pt >= 4:
            $ routetag = "us7dl_bad"
            jump alt_day6_us_7dl_start
            pause(1)
            return
    jump alt_day6_neu_begin
    
label alt_day6_neu_begin:
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(6, u"Одиночка. Утро")
    call alt_day6_neu_start
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    call alt_day6_neu_morning
    pause(1)
    if loki:
        $ alt_chapter(6, u"Одиночка. День")
        call alt_day6_neu_loki_day
        pause(1)
        call alt_day6_neu_loki_concert
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(6, u"Одиночка. Танцы")
        call alt_day6_neu_loki_disco
        pause(1)
    else:
        $ alt_chapter(6, u"Одиночка. День")
        call alt_day6_neu_day
        pause(1)
        call alt_day6_neu_concert
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(6, u"Одиночка. Танцы")
        call alt_day6_neu_disco
        pause(1)
    call alt_day6_neu_pirate
    pause(1)
    if loki:
        call alt_day6_neu_loki_disco2
        pause(1)
        $ persistent.sprite_time = "night"
        $ night_time()
        call alt_day6_neu_loki_evening
    else:
        call alt_day6_neu_disco2
        pause(1)
        $ persistent.sprite_time = "night"
        $ night_time()
        call alt_day6_neu_evening
    pause(1)
    call alt_day6_neu_sleeptime
    pause(1)
    jump alt_day7_neu_begin

label alt_day7_neu_begin:
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(7, u"Одиночка. Сон")
    call alt_day7_neu_sleep
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(7, u"Одиночка. Подъём")
    call alt_day7_neu_wakeup
    pause(1)
    call alt_day7_neu_explore
    pause(1)
    $ alt_chapter(7, u"Одиночка. Диалог")
    call alt_day7_neu_dialogue
    pause(1)
    $ prolog_time()
    if persistent.neu_loki_neu or persistent.neu_neu:
        menu:
            "Настоящее":
                $ alt_chapter(7, u"Одиночка. Настоящее")
                if loki:
                    call alt_day7_neu_neu_loki
                else:
                    call alt_day7_neu_neu
            "Будущее":
                $ alt_chapter(7, u"Одиночка. Будущее")
                call alt_day7_neu_true
    else:
        $ alt_chapter(7, u"Одиночка. Настоящее")
        if loki:
            call alt_day7_neu_neu_loki
        else:
            call alt_day7_neu_neu
    pause(1)
    return