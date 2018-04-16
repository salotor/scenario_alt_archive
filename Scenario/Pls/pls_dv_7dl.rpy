label alt_day4_dv_7dl_start:
    call alt_day4_dv_7dl_vars
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(4, u"Алиса. 7ДЛ. Утро")
    call alt_day4_dv_7dl_begin
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(4, u"Алиса. 7ДЛ. Поход")
    call alt_day4_dv_7dl_forest
    pause(1)
    $ alt_chapter(4, u"Алиса. 7ДЛ. Тихий час")
    call alt_day4_dv_7dl_silent_hour
    if alt_day4_dv_7dl_walkman_presented:
        jump alt_day4_dv_7dl2dj_transit
    pause(1)
    if alt_day4_dv_7dl_help_cs:
        $ alt_chapter(4, u"Алиса. 7ДЛ. Поездка")
        call alt_day4_dv_7dl_roadtrip
        pause(1)
        call alt_day4_dv_7dl_alco
        pause(1)
        call alt_day4_dv_7dl_back_to_camp
    else: # отказался, остался с рыжей
        call alt_day4_dv_7dl_append
        pause(1)
        if alt_day4_dv_7dl_aidpost: # новая переменная
            call alt_day4_dv_7dl_aidpost
            pause(1)
            if not alt_day4_dv_7dl_drank_vodka:
                $ persistent.sprite_time = "sunset"
                $ sunset_time()
                $ alt_chapter(4, u"Алиса. 7ДЛ. Ужин")
                call alt_day4_dv_7dl_supper
                pause(1)
                call alt_day4_dv_7dl_sleeptime
                pause(1)
        else:
            call alt_day4_dv_7dl_mt_aid
            pause(1)
            call alt_day4_dv_7dl_supper
            pause(1)
            call alt_day4_dv_7dl_sleeptime
            pause(1)
    jump alt_day5_dv_7dl_start

label alt_day5_dv_7dl_start:
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    if alt_day4_dv_7dl_drank_vodka:
        $ alt_chapter(5, u"Алиса. 7ДЛ. Похмелье")
        call alt_day5_dv_7dl_alco_morning
        pause(1)
        call alt_day5_dv_7dl_begin
        pause(1)
    elif alt_day4_dv_7dl_help_cs:
        $ alt_chapter(5, u"Алиса. 7ДЛ. Возвращение.")
        call alt_day5_dv_7dl_roadtrip
        pause(1)
    else:
        $ alt_chapter(5, u"Алиса. 7ДЛ. Утро.")
        call alt_day5_dv_7dl_begin
        pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(5, u"Алиса. 7ДЛ. Свечка.")
    call alt_day5_dv_7dl_candle
    pause(1)
    $ alt_chapter(5, u"Алиса. 7ДЛ. День")
    call alt_day5_dv_7dl_dinner
    pause(1)
    call alt_day5_dv_7dl_lunch
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(5, u"Алиса. 7ДЛ. Вечер")
    call alt_day5_dv_7dl_supper
    pause(1)
    $ alt_chapter(5, u"Алиса. 7ДЛ. Костёр")
    call alt_day5_dv_7dl_evening
    pause(1)
    $ alt_chapter(5, u"Алиса. 7ДЛ. Ночь")
    call alt_day5_dv_7dl_night
    pause(1)
    jump alt_day6_dv_7dl_start

label alt_day6_dv_7dl_start:
    call alt_day6_dv_7dl_vars
    pause(1)
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    $ alt_chapter(6, u"Алиса. 7ДЛ. Утро")
    call alt_day6_dv_7dl_begin
    pause(1)
    call alt_day6_dv_7dl_breakfast
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(6, u"Алиса. 7ДЛ. День")
    call alt_day6_dv_7dl_dinner
    pause(1)
    if alt_day6_dv_7dl_sl_route:
        call alt_day6_dv_7dl_sl
        pause(1)
        if alt_day6_dv_7dl_sl_help_agree or not alt_day1_cofront_sl_dv == 3:#новая переменная согласился помочь
            call alt_day6_dv_7dl_sl_help
            pause(1)
        call alt_day6_dv_7dl_sl_help2
        pause(1)
    elif alt_day6_dv_7dl_mi_route:
        call alt_day6_dv_7dl_un
        pause(1)
        if lp_dv < 14 or ((herc or loki) and lp_dv < 18 and lp_un >= 5) or (lp_un >= 4 and not (herc or loki)):
           call alt_day6_dv_7dl_hl_failer2
           pause(1)
    call alt_day6_dv_7dl_concert
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(6, u"Алиса. 7ДЛ. Танцы")
    call alt_day6_dv_7dl_dance
    pause(1)
    if alt_day_catapult == 1:
        call alt_day6_dv_7dl_escape_convince
        return
    if alt_day6_dv_7dl_transit:
        if alt_day6_dv_7dl_sl_route:
            call alt_day6_dv_7dl_sl_dancing
            pause(1)
        elif alt_day6_dv_7dl_mi_route:
            if lp_un >= 4:
                call alt_day6_dv_7dl_un_dancing
                pause(1)
            else:
                call alt_day6_dv_7dl_mt_dancing
                pause(1)
    else:
        call alt_day6_dv_7dl_dv_dancing
        pause(1)
    if alt_day6_dv_7dl_transit:
        call alt_day6_dv_7dl_sleeptime
        pause(1)
    else:
        if alt_day1_sl_keys_took == 1 or alt_day1_sl_keys_took == 3 or alt_day4_dv_7dl_extra_key:
            if alt_day6_dv_7dl_sl_route:
                if alt_day4_dv_7dl_extra_key:
                    $ alt_day6_dv_7dl_key_hentai = 100
                else:
                    $ alt_day6_dv_7dl_key_hentai = 0
            else:
                $ alt_day6_dv_7dl_key_hentai = 100

        if alt_day4_dv_7dl_vodka or alt_day4_dv_7dl_portwine:
            $ alt_day6_dv_7dl_alco_hentai = 10

        if alt_day4_dv_7dl_ba_conv:
            $ alt_day6_dv_7dl_ba_hentai = 1

        $ alt_day6_dv_7dl_hentai = alt_day6_dv_7dl_key_hentai + alt_day6_dv_7dl_alco_hentai + alt_day6_dv_7dl_ba_hentai
        if alt_day6_dv_7dl_hentai == 111:
            if not (herc or loki):
                $ lp_dv += 4
            else:
                $ lp_dv += 2
            call alt_day6_dv_7dl_love_scene
            pause(1)
        else:
            call alt_day6_dv_7dl_non_love
            pause(1)
        call alt_day6_dv_7dl_sleeptime
        pause(1)
    jump alt_day7_dv_7dl_start

label alt_day7_dv_7dl_start:
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(7, u"Алиса. 7ДЛ. Утро")
    call alt_day7_dv_7dl_begin
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(7, u"Алиса. 7ДЛ. Отъезд")
    call alt_day7_dv_7dl_router
    pause(1)
    if alt_day6_dv_7dl_transit:
        if alt_day6_dv_7dl_dance == 1:
            call alt_day7_dv_7dl_un
            pause(1)
        if alt_day6_dv_7dl_dance == 22 or alt_day6_dv_7dl_dance == 21: # проверить 21 и 22
            call alt_day7_dv_7dl_sl
            pause(1)
    else:
        if alt_day7_dv_7dl_check == 5:
            call alt_day7_dv_7dl_mt
            pause(1)
        else:
            call alt_day7_dv_7dl_dv
            pause(1)
            if alt_day7_dv_7dl_loki_catapult: # новая переменная
                call alt_day7_dv_7dl_loki
                pause(1)
                call alt_day7_dv_7dl_tulpa_end
                pause(1)
                return
    call alt_day7_dv_7dl_bus
    pause(1)
    $ alt_chapter(7, u"Алиса. 7ДЛ. Эпилог")
    call alt_day7_dv_7dl_ending_router
    pause(1)
    $ persistent.sprite_time = "prolog"
    $ prolog_time()
    if alt_day7_dv_7dl_check == 1:
        if karma > 75:
            menu:
                "Сесть на место.":
                    call alt_day7_dv_7dl_rf_epilogue
                    pause(1)
                "Прочь из автобуса!":
                    call alt_day7_dv_7dl_ussr_epilogue
                    pause(1)
        else:
            call alt_day7_dv_7dl_rf_epilogue
            pause(1)
    elif alt_day7_dv_7dl_check == 2:
        if karma > 75:
            call alt_day7_dv_7dl_rej_ussr_end
            pause(1)
        else:
            call alt_day7_dv_7dl_rej_rf_end
            pause(1)
    elif alt_day7_dv_7dl_check == 4:
        call alt_day7_dv_7dl_un_end
        pause(1)
    else:
        call alt_day7_dv_7dl_bad_end
        pause(1)
    return

