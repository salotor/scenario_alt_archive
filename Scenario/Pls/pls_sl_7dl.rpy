label alt_day4_sl_7dl_start:
    call alt_day4_sl_7dl_vars
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(4, u"Славя. 7ДЛ. Утро")
    pause(1)
    call alt_day4_sl_7dl_begin
    pause(1)
    call alt_day4_sl_7dl_morgen
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(4, u"Славя. 7ДЛ. Призрак")
    call alt_day4_sl_7dl_old_camp
    pause(1)
    call alt_day4_sl_7dl_naiad
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(4, u"Славя. 7ДЛ. Обед")
    call alt_day4_sl_7dl_dinner
    pause(1)
    if alt_day4_sl_7dl_phone:
        $ alt_chapter(4, u"Славя. 7ДЛ. Секрет")
        call alt_day4_sl_7dl_secret
        pause(1)
            if loki:
                call alt_day4_sl_7dl_sneak
            elif herc:
                call alt_day4_sl_7dl_returning
            else:
                call alt_day4_sl_7dl_runaway
    else:
        $ alt_chapter(4, u"Славя. 7ДЛ. Мечта.")
            call alt_day4_sl_7dl_sleephour
            pause(1)
            if alt_day4_sl_7dl_rendezvous:
                call alt_day4_sl_7dl_cccombo
            else:
                call alt_day4_sl_7dl_concert
            pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(4, u"Славя. 7ДЛ. Вечер")
    call alt_day4_sl_7dl_supper
    pause(1)
    if lp_sl > 13:
        call alt_day4_sl_7dl_declaration
    else:
        call alt_day4_sl_7dl_span
    pause(1)
    call alt_day4_sl_7dl_sleeptime
    pause(1)
    jump alt_day5_sl_7dl_start

label alt_day5_sl_7dl_start:
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(5, u"Славя. 7ДЛ. Утро")
    pause(1)
    $ alt_chapter(5, u"Славя. 7ДЛ. День")
    $ alt_chapter(5, u"Славя. 7ДЛ. Вечер")
    $ alt_chapter(5, u"Славя. 7ДЛ. Костёр")
    $ alt_chapter(5, u"Славя. 7ДЛ. Ночь")
    jump alt_day6_sl_7dl_start
 
label alt_day6_sl_7dl_start:
    jump alt_day7_sl_7dl_start
    
label alt_day7_sl_7dl_start:
    #Cон
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    $ alt_chapter(6, u"Славя. 7ДЛ. Утро")
    $ alt_chapter(7, u"Славя. 7ДЛ. Отъезд")
    $ alt_chapter(7, u"Славя. 7ДЛ. ЭПИЛОГ")
    #Две подветки
    #Гуд, бэд, гуд-рф, бэд-рф, нейтрал, тру
    return