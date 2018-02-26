label alt_day6_us_7dl_start:
    if routetag == "us7dl_good":
        call alt_day6_us_px_begin:
    else:
        call alt_day6_us_7dl_begin:
    pause(1)
    call alt_day6_us_px_begin
    pause(1)
    call alt_day6_us_px_exercises
    pause(1)
    call alt_day6_us_px_breakfast
    pause(1)
    if routetag == "us7dl_bad":
        jump alt_day6_us_7dl_revelations
    call alt_day6_us_px_carrier
    pause(1)
    if loki:
        call alt_day6_us_px_loki
    else:
        call alt_day6_us_px_hyst
    pause(1)
    call alt_day6_us_px_dinner
    pause(1)
    call alt_day6_us_px_ostr
    pause(1)
    if loki:
        call alt_day6_us_px_preparings
        pause(1)
    else:
        call alt_day6_us_px_party
        pause(1)
        call alt_day6_us_px_party_mi
        pause(1)
        call alt_day6_us_px_party_mt
        pause(1)
        call alt_day6_us_px_party_un
        pause(1)
        call alt_day6_us_px_party_dv
        pause(1)
        if persistent.us_px_good or persistent.us_7dl_good:
            call alt_day6_us_px_party_sl
            $ alt_day6_us_px_sl_join = True
        pause(1)
        call alt_day6_us_px_far_gate
        if alt_day6_us_px_sl_join:
            call alt_day6_us_px_concert_sl
        else:
            call alt_day6_us_px_concert_ba
    pause(1)
    call alt_day6_us_px_concert
    pause(1)
    call alt_day6_us_px_supper
    pause(1)
    call alt_day6_us_px_discoteque
    pause(1)
    if alt_day6_us_px_sl_join:
        if loki:
            call alt_day6_us_px_sl_slowdance
        else:
            call alt_day6_us_px_afterwords
        pause(1)
        call alt_day6_us_px_returning
    else:
        call alt_day6_us_px_dancedance
    pause(1)
    call alt_day6_us_px_sleeptime
    pause(1)
    jump alt_day6_us_px_start
    
label alt_day7_us_px_start:
    call alt_day7_us_px_begin
    pause(1)
    call alt_day7_us_px_breakfast
    pause(1)
    if alt_day6_us_px_sl_join:
        call alt_day7_us_px_escape
        pause(1)
        call alt_day7_us_px_cleaning
        pause(1)
        call alt_day7_us_px_bus
        pause(1)
        if alt_day7_us_px_escaped:
            call alt_day7_us_px_wastelands
            if loki:
                call alt_day7_us_px_loki
            else:
                call alt_day7_us_px_heathrow
            return
        else:
        call alt_day7_us_px_mourning
        pause(1)
    else:
        call alt_day7_us_px_wastelands
    pause(1)
    call alt_day7_us_px_packing
    pause(1)
    call alt_day7_us_px_leaving
    pause(1)
    call alt_day7_us_px_dejavu
    pause(1)
    if loki:
        call alt_day7_us_px_fairytale
    else:
        call alt_day7_us_px_realvu
    return

label alt_day6_us_7dl_revelations:
    call alt_day6_us_7dl_helping
    pause(1)
    if alt_day6_us_7dl_mi_friends == 2:
        call alt_day_us_7dl_repetition
    elif alt_day6_us_7dl_sl_friends == 2:
        call alt_day7_us_7dl_helping
    else:
        call alt_day7_us_7dl_un_met
    pause(1)
    call alt_day6_us_7dl_dinner
    pause(1)
    if (alt_day6_us_7dl_mi_friends == 2) or (alt_day6_us_7dl_sl_friends == 2):
        call alt_day6_us_7dl_soundcheck
        pause(1)
        call alt_day6_us_7dl_concert
    else:
        call alt_day6_us_7dl_snake
        pause(1)
        call alt_day6_us_7dl_rendezvous
    pause(1)
    call alt_day6_us_7dl_supper
    pause(1)
    call alt_day6_us_7dl_disco
    pause(1)
    if alt_day6_us_7dl_sl_friends == 2:
        call alt_day6_us_7dl_beauty
    elif alt_day6_us_7dl_mi_friends == 2:
        call alt_day6_us_7dl_foreign #Выбор на флаг3, для концовки
    elif alt_day6_us_7dl_un_friends == 2:
        call alt_day6_us_7dl_danceagain #Выбор на флаг3, для концовки
    elif alt_day4_neu_us_pixies == 2:
        call alt_day6_us_7dl_tea
    else:
        call alt_day6_us_7dl_getlostdance
    pause(1)
    call alt_day6_us_7dl_sleeptime
    pause(1)
    jump alt_day7_us_7dl_start
    
label alt_day7_us_7dl_start:
    call alt_day7_us_7dl_begin
    pause(1)
    call alt_day7_us_7dl_breakfast
    pause(1)
    call alt_day7_us_7dl_packing
    pause(1)
    call alt_day7_us_7dl_leaving
    pause(1)
    call alt_day7_us_7dl_wakeup
    pause(1)
    if us_pt > 7:
        call alt_day7_us_7dl_wastelands
    elif alt_day6_us_7dl_mi_friends == 3:
        call alt_day7_us_7dl_mikuforever
    elif alt_day6_us_7dl_un_friends == 3:
        call alt_day7_us_7dl_lenaforever
    else:
        call alt_day7_us_7dl_verses
    pause(1)
    return
    