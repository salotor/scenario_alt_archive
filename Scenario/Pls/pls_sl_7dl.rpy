label alt_day4_sl_7dl_start:
    if herc or loki:
        $ routetag = "sl7dl_sport" #Спортивная форма для бегающих со Славей Герка и Локи
    else:
        $ routetag = "sl7dl" #Базис

    call alt_day4_sl_7dl_vars
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(4, u"Славя. 7ДЛ. Утро")
    pause(1)
    call alt_day4_sl_7dl_begin
    pause(1)
    call alt_day4_sl_7dl_breakfast
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    if loki:
        $ routetag = "sl7dl_loki"
        call alt_day4_sl_7dl_loki_morning
        pause(1)
        $ alt_chapter(4, u"Славя. 7ДЛ. День")
        call alt_day4_sl_7dl_loki_day
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(4, u"Славя. 7ДЛ. Вечер")
        call alt_day4_sl_7dl_loki_evening
    elif herc:
        $ routetag = "sl7dl_herc"
        call alt_day4_sl_7dl_herc_morning
        pause(1)
        $ alt_chapter(4, u"Славя. 7ДЛ. День")
        call alt_day4_sl_7dl_herc_day
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(4, u"Славя. 7ДЛ. Вечер")
        call alt_day4_sl_7dl_herc_evening
    else:
        call alt_day4_sl_7dl_morning
        pause(1)
        $ alt_chapter(4, u"Славя. 7ДЛ. День")
        call alt_day4_sl_7dl_day
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(4, u"Славя. 7ДЛ. Вечер")
        call alt_day4_sl_7dl_evening
    pause(1)
    call alt_day4_sl_7dl_sundown
    $ persistent.sprite_time = "night"
    $ night_time()
    call alt_day4_sl_7dl_sleeptime
    pause(1)
    jump alt_day5_sl_7dl

label alt_day5_sl_7dl_start:
    if herc or loki:
        $ routetag = "sl7dl_sport" #Спортивная форма для бегающих со Славей Герка и Локи
    call alt_day5_sl_7dl_vars
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(4, u"Славя. 7ДЛ. Утро")
    pause(1)
    call alt_day5_sl_7dl_begin
    pause(1)
    call alt_day5_sl_7dl_breakfast
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    if loki:
        $ routetag = "sl7dl_loki"
        call alt_day5_sl_7dl_loki_morning
        pause(1)
        $ alt_chapter(5, u"Славя. 7ДЛ. День")
        call alt_day5_sl_7dl_loki_day
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(5, u"Славя. 7ДЛ. Вечер")
        call alt_day5_sl_7dl_loki_evening
    elif herc:
        $ routetag = "sl7dl_herc"
        call alt_day5_sl_7dl_herc_morning
        pause(1)
        $ alt_chapter(5, u"Славя. 7ДЛ. День")
        call alt_day5_sl_7dl_herc_day
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(5, u"Славя. 7ДЛ. Вечер")
        call alt_day5_sl_7dl_herc_evening
        pause(1)
    else:
        call alt_day5_sl_7dl_morning
        pause(1)
        $ alt_chapter(5, u"Славя. 7ДЛ. День")
        call alt_day5_sl_7dl_day
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(5, u"Славя. 7ДЛ. Вечер")
        call alt_day5_sl_7dl_evening
    pause(1)
    call alt_day5_sl_7dl_campfire
    pause(1)
    if (herc or loki) and (lp_sl > 18) and (persistent.sl_7dl_good_loki or persistent.sl_7dl_good_herc or persistent.sl_7dl_good):
        call alt_day5_sl_7dl_hentai
        $ alt_day5_sl_7dl_hentai_done = True
    pause(1)
    $ persistent.sprite_time = "night"
    $ night_time()
    call alt_day5_sl_7dl_sleeptime
    pause(1)
    jump alt_day6_sl_7dl

label alt_day6_sl_7dl_start:
    if (herc or loki) and (lp_sl > 15):
        $ routetag = "sl7dl_sport" #Спортивная форма для бегающих со Славей Герка и Локи
    call alt_day6_sl_7dl_vars
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(6, u"Славя. 7ДЛ. Утро")
    pause(1)
    call alt_day6_sl_7dl_begin
    pause(1)
    call alt_day6_sl_7dl_breakfast
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    if loki:
        $ routetag = "sl7dl_loki"
        call alt_day6_sl_7dl_loki_morning
        pause(1)
        $ alt_chapter(6, u"Славя. 7ДЛ. День")
        call alt_day6_sl_7dl_loki_day
    elif herc:
        $ routetag = "sl7dl_herc"
        call alt_day6_sl_7dl_herc_morning
        pause(1)
        $ alt_chapter(6, u"Славя. 7ДЛ. День")
        call alt_day6_sl_7dl_herc_day
    else:
        call alt_day6_sl_7dl_morning
        pause(1)
        $ alt_chapter(6, u"Славя. 7ДЛ. День")
        call alt_day6_sl_7dl_day
        pause(1)
    $ routetag = "sl7dl_dress"
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(6, u"Славя. 7ДЛ. Дискотека")
    call alt_day6_sl_7dl_evening
    pause(1)
    $ persistent.sprite_time = "night"
    $ night_time()
    if persistent.sl_7dl_good_loki and persistent.sl_7dl_good_herc and persistent.sl_7dl_good:
        $ routetag = "sl7dltrue"
    elif (lp_sl > 20) and (karma > 120):
        $ routetag = "sl7dlgood"
        pause(1)
        if persistent.sl_7dl_good_loki or persistent.sl_7dl_good_herc or persistent.sl_7dl_good:
            call alt_day6_sl_7dl_hentai
            $ alt_day6_sl_7dl_hentai_done = True
    elif lp_sl > 20:
        $ routetag = "sl7dlneu"
    else:
        $ routetag = "sl7dlbad"
    call alt_day6_sl_7dl_sleeptime
    pause(1)
    jump alt_day7_sl_7dl

label alt_day7_sl_7dl_start:
    call alt_day7_sl_7dl_vars
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(7, u"Славя. 7ДЛ. Утро")
    pause(1)
    call alt_day7_sl_7dl_begin
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    call alt_day7_sl_7dl_packing
    pause(1)
    $ alt_chapter(7, u"Славя. 7ДЛ. Отъезд")
    call alt_day7_sl_7dl_leaving
    pause(1)
    if routetag == "sl7dltrue":
        $ persistent.sprite_time = "prolog"
        $ prolog_time()
        $ alt_chapter(6, u"Славя. 7ДЛ. Тру")
        call alt_day7_sl_7dl_true
        pause(1)
        return
    $ alt_chapter(7, u"Славя. 7ДЛ. Эпилог")
    if loki:
        call alt_day7_sl_7dl_loki_epilogue
    elif herc:
        call alt_day7_sl_7dl_herc_epilogue
    else:
        call alt_day7_sl_7dl_epilogue
    pause(1)
    $ persistent.sprite_time = "prolog"
    $ prolog_time()
    if routetag == "sl7dlgood":
        if loki:
            $ alt_chapter(7, u"Славя. 7ДЛ. Гуд")
            call alt_day7_sl_7dl_loki_good
        elif herc:
            $ alt_chapter(7, u"Славя. 7ДЛ. Гуд")
            call alt_day7_sl_7dl_herc_good
        else:
            $ alt_chapter(7, u"Славя. 7ДЛ. Гуд")
            call alt_day7_sl_7dl_good
    elif routetag == "sl7dlneu":
        if loki:
            $ alt_chapter(7, u"Славя. 7ДЛ. Сволочь")
            call alt_day7_sl_7dl_loki_excl
        elif herc:
            $ alt_chapter(7, u"Славя. 7ДЛ. Реджект")
            call alt_day7_sl_7dl_herc_excl
        else:
            $ alt_chapter(7, u"Славя. 7ДЛ. Борец")
            call alt_day7_sl_7dl_excl
    elif routetag == "sl7dlbad":
        call alt_day7_sl_7dl_bad
    pause(1)
    return
=======
    if herc:
        call alt_day4_sl_7dl_herc_karma
    elif loki:
        call alt_day4_sl_7dl_loki_lp
    else:
        call alt_day4_sl_7dl_sam_sp
    pause(1)
    call alt_day4_sl_7dl_dinner
    pause(1)
    if herc:
        call alt_day4_sl_7dl_herc_lp
    elif loki:
        call alt_day4_sl_7dl_loki_sp
    else:
        call alt_day4_sl_7dl_sam_karma
    pause(1)
    call alt_day4_sl_7dl_lunch
    pause(1)
    if herc:
        call alt_day4_sl_7dl_herc_karma
    elif loki:
       call alt_day4_sl_7dl_loki_lp
    else:
        call alt_day4_sl_7dl_sam_sp
    pause(1)
    call alt_day4_sl_7dl_supper
    pause(1)
    if herc:
        call alt_day4_sl_7dl_herc_lp
    elif loki:
       call alt_day4_sl_7dl_loki_sp
    else:
        call alt_day4_sl_7dl_sam_karma
    pause(1)
    call alt_day4_sl_7dl_sleeptime
    jump alt_day5_sl_7dl_start
    
>>>>>>> master
