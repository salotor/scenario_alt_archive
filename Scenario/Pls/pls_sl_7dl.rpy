#Герк: помощь-личное-изменения-помощь
#Локи: личное-изменения-помощь-личное
#Дрищ: изменения-помощь-личное-изменения
# Помощь - $karma
# Личное - $lp_sl
# Изменения - $ alt_sp 

label alt_day4_sl_7dl_start:
    call alt_day4_sl_7dl_vars
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(4, u"Славя. 7ДЛ. Утро")
    pause(1)
    call alt_day4_sl_7dl_begin
    pause(1)
    call alt_day4_sl_7dl_breakfast
    pause(1)
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
    