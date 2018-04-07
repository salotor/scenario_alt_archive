label alt_day1_start:
    call alt_day1_vars
    $ persistent.sprite_time = "day"
    $ night_time()
    call alt_day1_begin
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(1, u"Лагерь.")
    call alt_day1_alt_M
    pause(1)
    $ alt_chapter(1, u"Первые трудности.")
    call alt_day1_alt_A
    pause(1)
    $ alt_chapter(1, u"Новая форма!")
    call alt_day1_alt_S
    pause(1)
    $ alt_chapter(1, u"Немного о…")
    call alt_day1_alt_L
    pause(1)
    $ alt_chapter(1, u"Пионэр.")
    call alt_day1_alt_O
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(1, u"Ужин.")
    call alt_day1_alt_supper
    pause(1)
    $ alt_chapter(1, u"Теория гадостроения.")
    call alt_day1_alt_U
    if not alt_day1_alt_us_robbed:
        call alt_day1_alt_U_reject
        pause(1)
    $ persistent.sprite_time = "night"
    $ night_time()
    $ alt_chapter(1, u"Вечер.")                
    call alt_day1_alt_ev_A_S
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