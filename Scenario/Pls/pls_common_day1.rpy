label alt_day1_start:
    call alt_day1_vars
    pause(1)
    $ persistent.sprite_time = "day"
    $ night_time()
    call alt_day1_begin
    pause(1)
   $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(1, u"Пробуждение")
    call alt_day1_bus_start
    pause(1)
    $ alt_chapter(1, u"Прибытие")
    call alt_day1_arrival
    pause(1)
    $ alt_chapter(1, u"Первое знакомство")
    call alt_day1_firts_met
    if not alt_day1_sl_conv:
        if herc or loki:
        call alt_day1_chase1
        $ alt_chapter(1, u"Пристань")
        call alt_day1_dock
        pause(1)
    $ alt_chapter(1, u"Вожатая")
    call alt_day1_mod_tan
    pause(1)
    $ alt_chapter(1, u"Электроник")
    call alt_day1_elektron
    pause(1)
    $ alt_chapter(1, u"Экскурсия")
    call alt_day1_meeting
    pause(1)
    call alt_day1_soccer_d1
    pause(1)
    $ sunset_time()
    $ persistent.sprite_time = "sunset"
    $ alt_chapter(1, u"Ужин")
    call alt_day1_supper
    pause(1)
    call alt_day1_dining_room
    pause(1)
    $ alt_chapter(1, u"Погоня")
    call alt_day1_chase
    pause(1)
    if alt_day1_us_shotted:
        call alt_day1_headshot
    else:
        call alt_day1_nocatch
    pause(1)
    $ persistent.sprite_time = "night"
    $ night_time()
    $ alt_chapter(1, u"Спасительница")
    call alt_day1_slavya_saviour
    pause(1)
    $ alt_chapter(1, u"Вечер")
    call alt_day1_lena
    pause(1)
    if alt_day1_un_stopped:
        call alt_day1_un_stay
        pause(1)
    call alt_day1_sleep
    pause(1)
    jump alt_day2_start