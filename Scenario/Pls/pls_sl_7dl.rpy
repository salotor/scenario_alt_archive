label alt_day4_sl_7dl_start:
    if herc or loki:
        $ routetag = "sl7dl_sport"
    else:
        $ routetag = "sl7dl"
    call alt_day4_sl_7dl_vars
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(4, u"Славя. 7ДЛ. Утро")
    pause(1)
    $ renpy.save_persistent()
    call alt_day4_sl_7dl_begin
    pause(1)
    $ renpy.save_persistent()
    call alt_day4_sl_7dl_breakfast
    pause(1)
    $ renpy.save_persistent()
    $ persistent.sprite_time = "sunset"
    $ day_time()
    if loki:
        $ routetag = "sl7dl_loki"
        call alt_day4_sl_7dl_loki_morning
        pause(1)
        $ renpy.save_persistent()
        $ alt_chapter(4, u"Славя. 7ДЛ. День")
        call alt_day4_sl_7dl_loki_day
        pause(1)
        $ renpy.save_persistent()
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(4, u"Славя. 7ДЛ. Вечер")
        call alt_day4_sl_7dl_loki_evening
    elif herc:
        $ routetag = "sl7dl_herc"
        call alt_day4_sl_7dl_herc_morning
        pause(1)
        $ renpy.save_persistent()
        $ alt_chapter(4, u"Славя. 7ДЛ. День")
        call alt_day4_sl_7dl_herc_day
        pause(1)
        $ renpy.save_persistent()
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(4, u"Славя. 7ДЛ. Вечер")
        call alt_day4_sl_7dl_herc_evening
    else:
        call alt_day4_sl_7dl_morning
        pause(1)
        $ renpy.save_persistent()
        $ alt_chapter(4, u"Славя. 7ДЛ. День")
        call alt_day4_sl_7dl_day
        pause(1)
        $ renpy.save_persistent()
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(4, u"Славя. 7ДЛ. Вечер")
        call alt_day4_sl_7dl_evening
    pause(1)
    $ renpy.save_persistent()
    call alt_day4_sl_7dl_sundown
    $ persistent.sprite_time = "night"
    $ night_time()
    call alt_day4_sl_7dl_sleeptime
    pause(1)
    $ renpy.save_persistent()
    jump alt_day5_sl_7dl_start

label alt_day5_sl_7dl_start:
    if herc and alt_day4_sl_7dl_workout :
        $ routetag = "sl7dl_sport"
    call alt_day5_sl_7dl_vars
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(5, u"Славя. 7ДЛ. Утро")
    pause(1)
    $ renpy.save_persistent()
    call alt_day5_sl_7dl_begin
    pause(1)
    $ renpy.save_persistent()
    call alt_day5_sl_7dl_breakfast
    pause(1)
    $ renpy.save_persistent()
    $ persistent.sprite_time = "sunset"
    $ day_time()
    if loki:
        $ routetag = "sl7dl_loki"
    elif herc:
        $ routetag = "sl7dl_herc"
    call alt_day5_sl_7dl_candle
    pause(1)
    $ renpy.save_persistent()
    if loki:
        $ alt_chapter(5, u"Славя. 7ДЛ. День")
        call alt_day5_sl_7dl_loki_day
        pause(1)
        $ renpy.save_persistent()
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(5, u"Славя. 7ДЛ. Вечер")
        call alt_day5_sl_7dl_loki_evening
    elif herc:
        $ alt_chapter(5, u"Славя. 7ДЛ. День")
        call alt_day5_sl_7dl_herc_day
        pause(1)
        $ renpy.save_persistent()
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(5, u"Славя. 7ДЛ. Вечер")
        call alt_day5_sl_7dl_herc_evening
        pause(1)
        $ renpy.save_persistent()
    else:
        $ alt_chapter(5, u"Славя. 7ДЛ. День")
        call alt_day5_sl_7dl_day
        pause(1)
        $ renpy.save_persistent()
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(5, u"Славя. 7ДЛ. Вечер")
        call alt_day5_sl_7dl_evening
    pause(1)
    $ renpy.save_persistent()
    $ alt_chapter(5, u"Славя. 7ДЛ. Костёр")
    call alt_day5_sl_7dl_campfire
    pause(1)
    $ renpy.save_persistent()
    if herc and (lp_sl > 16) and (persistent.sl_7dl_good_loki and persistent.sl_7dl_good):
        call alt_day5_sl_7dl_hentai
        $ alt_day5_sl_7dl_hentai_done = True
    pause(1)
    $ renpy.save_persistent()
    $ persistent.sprite_time = "night"
    $ night_time()
    call alt_day5_sl_7dl_sleeptime
    pause(1)
    $ renpy.save_persistent()
    window hide
    with fade
    jump alt_day6_sl_7dl_start

label alt_day6_sl_7dl_start:
    if herc:
        call alt_day6_sl_7dl_camping
        pause(1)
        $ renpy.save_persistent()
        call alt_day6_sl_7dl_revenge
    if not alt_day5_sl_7dl_herc_sick:
        $ routetag = "sl7dl_sport"
    call alt_day6_sl_7dl_vars
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(6, u"Славя. 7ДЛ. Утро")
    pause(1)
    $ renpy.save_persistent()
    call alt_day6_sl_7dl_begin
    pause(1)
    $ renpy.save_persistent()
    if not alt_day5_sl_7dl_herc_sick:
        call alt_day6_sl_7dl_breakfast
    pause(1)
    $ renpy.save_persistent()
    $ persistent.sprite_time = "day"
    $ day_time()
    if loki:
        $ routetag = "sl7dl_loki"
        call alt_day6_sl_7dl_loki_morning
        pause(1)
        $ renpy.save_persistent()
        $ alt_chapter(6, u"Славя. 7ДЛ. День")
        call alt_day6_sl_7dl_loki_day
    elif herc:
        $ routetag = "sl7dl_herc"
        call alt_day6_sl_7dl_herc_morning
        pause(1)
        $ renpy.save_persistent()
        $ alt_chapter(6, u"Славя. 7ДЛ. День")
        call alt_day6_sl_7dl_herc_day
    else:
        $ routetag = "sl7dl"
        call alt_day6_sl_7dl_morning
        pause(1)
        $ renpy.save_persistent()
        $ alt_chapter(6, u"Славя. 7ДЛ. День")
        call alt_day6_sl_7dl_day
        pause(1)
        $ renpy.save_persistent()
    call alt_day6_sl_7dl_evening
    pause(1)
    $ renpy.save_persistent()
    call alt_day6_sl_7dl_catapult
    if (karma < 50) and not herc:
        pause(1)
        $ renpy.save_persistent()
        return
    pause(1)
    $ renpy.save_persistent()
    if (herc or loki) or alt_day5_sl_7dl_olroad:
        $ routetag = "sl7dl_dress"
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(6, u"Славя. 7ДЛ. Дискотека")
    call alt_day6_sl_7dl_disco
    pause(1)
    $ renpy.save_persistent()
    $ persistent.sprite_time = "night"
    $ night_time()
    if persistent.sl_7dl_good_loki and persistent.sl_7dl_good_herc and persistent.sl_7dl_good:
        $ routetag = "sl7dltrue"
    elif (lp_sl >= 19) and (karma > 120):    # надо ещё не простившего Локи тут проверять, он же на гуд не выходит
        $ routetag = "sl7dlgood"
        pause(1)
        $ renpy.save_persistent()
    elif lp_sl >= 19:
        $ routetag = "sl7dlneu"
    else:
        $ routetag = "sl7dlbad"
    if lp_sl >= 19:
        if alt_day6_sl_7dl_forgive or not loki:
            call alt_day6_sl_7dl_hentai
            $ alt_day6_sl_7dl_hentai_done = True
    pause(1)
    $ renpy.save_persistent()
    if not alt_day6_sl_7dl_hentai_done or not (herc or loki):
        call alt_day6_sl_7dl_sleeptime
    pause(1)
    $ renpy.save_persistent()
    jump alt_day7_sl_7dl_start

label alt_day7_sl_7dl_start:
    call alt_day7_sl_7dl_vars
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(7, u"Славя. 7ДЛ. Утро")
    pause(1)
    if alt_day6_sl_7dl_hentai_done:
        if herc:
            call alt_day7_sl_7dl_begin_herc
        elif loki:
            call alt_day7_sl_7dl_begin_loki
        else:
            call alt_day7_sl_7dl_begin
    else:
        call alt_day7_sl_7dl_begin
    pause(1)
    $ renpy.save_persistent()
    $ persistent.sprite_time = "day"
    $ day_time()
    if herc:
        call alt_day7_sl_7dl_packing_herc
    elif loki:
        call alt_day7_sl_7dl_packing_loki
    else:
        call alt_day7_sl_7dl_packing
    pause(1)
    $ renpy.save_persistent()
    $ alt_chapter(7, u"Славя. 7ДЛ. Отъезд")
    call alt_day7_sl_7dl_leaving
    pause(1)
    if routetag == "sl7dltrue" and not alt_day7_sl_7dl_freewill:
    $ renpy.save_persistent()
        $ persistent.sprite_time = "sunset"
        $ prolog_time()
        $ alt_chapter(6, u"Славя. 7ДЛ. Тру")
        call alt_day7_sl_7dl_true
        pause(1)
        $ renpy.save_persistent()
        return
    $ persistent.sprite_time = "sunset"
    $ prolog_time()
    $ alt_chapter(7, u"Славя. 7ДЛ. Эпилог")
    if lp_sl > 20:
        if karma < 120: # не простивший Локи разве должен сюда попадать? and (alt_day6_sl_7dl_forgive or not loki) нужно
            call alt_day7_sl_7dl_rf_good
            pause(1)
            if alt_day_binder == 1:
                call alt_day7_sl_7dl_postscriptum
        else:
            if herc:
                call alt_day7_sl_7dl_herc
                pause(1)
                if alt_day4_sl_7dl_phone:
                    call alt_day7_sl_7dl_herc_neon
                else:
                    call alt_day7_sl_7dl_herc_right_road
            elif loki:
                call alt_day7_sl_7dl_loki
                pause(1)
                if alt_day6_sl_7dl_forgive:
                    call alt_day7_sl_7dl_loki_radio
                else:
                    call alt_day7_sl_7dl_loki_rewind
                pause(1)
                if alt_day7_sl_7dl_loki_park:
                    call alt_day7_sl_7dl_loki_am_home
                else:
                    call alt_day7_sl_7dl_loki_oafa
            else:
                call alt_day7_sl_7dl_epi
                pause(1)
                if alt_day5_sl_7dl_olroad:
                    call alt_day7_sl_7dl_loopback
                    if alt_day_binder == 1:
                        call alt_day7_sl_7dl_loop_ps
                else:
                    call alt_day7_sl_7dl_wasted
    else:
        call alt_day7_sl_7dl_missed
    pause(1)
    $ renpy.save_persistent()
    return