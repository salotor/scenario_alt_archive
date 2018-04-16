label alt_day4_sl_7dl_start:
    call alt_day4_sl_7dl_vars
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(4, u"Славя. 7ДЛ. Утро")
    $ alt_chapter(4, u"Славя. 7ДЛ. День")
    $ alt_chapter(4, u"Славя. 7ДЛ. Вечер")
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