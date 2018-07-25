label alt_day4_un_7dl_start:
    pause(1)
    if (alt_day3_un_med_help == 1) and (lp_un >= 13):
        call alt_day4_neu_us_vars
        pause(1)
        call alt_day4_un_7dl_vars
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(4, u"Лена. 7ДЛ. Утро")
        call alt_day4_un_7dl_begin
        pause(1)
        if not alt_day4_un_7dl_morning_searching:
            call alt_day4_un_7dl_lineup
            pause(1)
        call alt_day4_un_7dl_breakfast # разбить?
        pause(1)
        call alt_day4_un_7dl_declaration
        pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(4, u"Лена. 7ДЛ. День")
    call alt_day4_un_7dl_dinner
    pause(1)
    call alt_day4_un_7dl_launch
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(4, u"Лена. 7ДЛ. Вечер")
    call alt_day4_un_7dl_supper
    pause(1)
    call alt_day4_un_7dl_sleeptime
    pause(1)
    jump alt_day5_un_7dl_start
    
label alt_day5_un_7dl_start:
    pause(1)
    call alt_day5_un_7dl_vars
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(5, u"Лена. 7ДЛ. Утро")
    call alt_day5_un_7dl_begin
    pause(1)
    call alt_day5_un_7dl_breakfast
    pause(1)
    if loki and (alt_day1_sl_keys_took == 1 or alt_day1_sl_keys_took == 3):
        call alt_day5_un_7dl_breakfast_l
        pause(1)
        call alt_day5_un_7dl_clubs
        pause(1)
    else:
        if loki:
            call alt_day5_un_7dl_breakfast_l
            pause(1)
        elif herc:
            call alt_day5_un_7dl_breakfast_h
            pause(1)
        if not (loki or herc):
            call alt_day5_un_7dl_games
            pause(1)
        else:
            call alt_day5_un_7dl_cleaning
            pause(1)
        $ persistent.sprite_time = "day"
        $ day_time()
        $ alt_chapter(5, u"Лена. 7ДЛ. Обед")
        call alt_day5_un_7dl_dinner
        pause(1)
        if not (herc or loki) and 'nwsppr' in list_clubs_7dl:
            call alt_day5_un_7dl_dinner_d
            pause(1)
            call alt_day5_un_7dl_unl
            pause(1)
        else:
            if not (herc or loki):
                call alt_day5_un_7dl_dinner_d
                pause(1)
            else:
                call alt_day5_un_7dl_dinner_hl
                pause(1)
            call alt_day5_un_7dl_np
            pause(1)
        call alt_day5_un_7dl_launch
        pause(1)
        if not (herc or loki) and 'nwsppr' in list_clubs_7dl:
            call alt_day5_un_7dl_library
            pause(1)
        else:
            call alt_day5_un_7dl_washing
            pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(5, u"Лена. 7ДЛ. Вечер")
    call alt_day5_un_7dl_supper
    pause(1)
    if 'nwsppr' in list_clubs_7dl and not alt_day5_un_7dl_club_day and not (herc or loki):
        call alt_day5_un_7dl_runaway
        pause(1)
    elif alt_day5_un_7dl_club_day:
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(5, u"Лена. 7ДЛ. Вечер")
        call alt_day5_un_7dl_video
        pause(1)
    elif alt_day5_un_7dl_solo_washing:
        call alt_day5_un_7dl_evening_un
        pause(1)
        $ persistent.sprite_time = "night"
        $ night_time()
        $ alt_chapter(5, u"Лена. 7ДЛ. Ночь")
        call alt_day5_un_7dl_runaway
        pause(1)
    elif alt_day5_un_7dl_sl_un_washing:
        call alt_day5_un_7dl_evening_dv
        pause(1)
    if not alt_day5_un_7dl_club_day:
        call alt_day5_un_7dl_island_hen
        pause(1)
    call alt_day5_un_7dl_sleeptime
    pause(1)
    jump alt_day6_un_7dl_start
    
label alt_day6_un_7dl_start:
    pause(1)
    call alt_day6_un_7dl_vars
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(6, u"Лена. 7ДЛ. Утро")
    call alt_day6_un_7dl_begin
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(6, u"Лена. 7ДЛ. День")
    call alt_day6_un_7dl_dinner
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(6, u"Лена. 7ДЛ. Вечер")
    call alt_day6_un_7dl_supper
    pause(1)
    if alt_day_catapult == 1:
        call alt_day6_un_7dl_letmeout
        pause(1)
        return
    $ persistent.sprite_time = "night"
    $ night_time()
    $ alt_chapter(6, u"Лена. 7ДЛ. Танцы")
    call alt_day6_un_7dl_dance
    pause(1)
    $ alt_chapter(6, u"Лена. 7ДЛ. Ночь")
    call alt_day6_un_7dl_sleeptime
    pause(1)
    $ alt_day7_un_7dl_rnm = lp_un * 4
    if alt_day5_un_7dl_sl_un_washing or alt_day4_un_7dl_dv_us_explosives:
        $ alt_day7_un_7dl_rnm = alt_day7_un_7dl_rnm*1.1
    if alt_day5_un_7dl_sl_un_washing and alt_day4_un_7dl_dv_us_explosives:
        $ alt_day7_un_7dl_rnm = alt_day7_un_7dl_rnm*1.2
    if persistent.mt_7dl_good:
        $ alt_day7_un_7dl_rnm = alt_day7_un_7dl_rnm*0.9

    if alt_day4_neu_transit == 1:
        $ routetag = "un"
    elif alt_day6_un_7dl_agreed or (alt_day7_un_7dl_rnm <= 75):
        $ routetag = "un7dlbad"
    else:
        $ routetag = "un7dlgood"
    jump alt_day7_un_7dl_start
    

label alt_day7_un_7dl_start:
    call alt_day7_un_7dl_vars
    pause(1)
    $ persistent.sprite_time = "prolog"
    $ prolog_time()
    $ alt_chapter(7, u"Лена. 7дл. Утро")
    call alt_day7_un_7dl_begin
    pause(1)
    call alt_day7_un_7dl_epilogue_all
    pause(1)
    $ alt_chapter(7, u"Лена. 7дл. Эпилог")
    if routetag == "un7dlgood":
        call alt_day7_un_7dl_epilogue
        pause(1)
        call alt_day7_un_7dl_epilogue_rt
        pause(1)
        if alt_day7_un_7dl_true_end:
            call alt_day7_un_7dl_true
            pause(1)
        elif karma >= 75:
            menu:
                "Ну уж чёрта с два!":
                    call alt_day7_un_7dl_rf
                    pause(1)
                "Прочь из автобуса!":
                    call alt_day7_un_7dl_ussr
                    pause(1)
        else:
            call alt_day7_un_7dl_rf
            pause(1)
    elif routetag == "un7dlbad":
        call alt_day7_un_7dl_epilogue_bad
        pause(1)
    elif routetag == "un":
        call alt_day7_un_7dl_true1
        pause(1)
    return