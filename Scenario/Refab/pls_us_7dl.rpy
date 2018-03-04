label alt_day6_us_7dl_start:
    call alt_day6_us_7dl_vars
    pause(1)
    if routetag == "us7dl_good":
        call alt_day6_us_px_begin
    else:
        call alt_day6_us_7dl_begin
    pause(1)
    call alt_day6_us_7dl_exercises
    pause(1)
    call alt_day6_us_7dl_breakfast
    pause(1)
    if routetag == "us7dl_bad":
        call alt_day6_us_7dl_helping
        pause(1)
        if alt_day6_us_7dl_mi_friends == 2:
            call alt_day_us_7dl_preps
        elif alt_day6_us_7dl_sl_friends == 2:
            call alt_day6_us_7dl_warehouse
        else:
            call alt_day6_us_7dl_un_met
        pause(1)
        call alt_day6_us_7dl_dinner
        pause(1)
        if (alt_day6_us_7dl_mi_friends == 2) or (alt_day6_us_7dl_sl_friends == 2):
            call alt_day6_us_7dl_soundcheck
        else:
            call alt_day6_us_7dl_button
        pause(1)
        if us_pt <= 4:
            pass
        else:
            call alt_day6_us_7dl_rendezvous
        pause(1)
    else:
        call alt_day6_us_px_carrier
        pause(1)
        call alt_day6_us_px_dinner
        pause(1)
        call alt_day6_us_px_Lena
        pause(1)
        if persistent.us_7dl_good:
            call alt_day6_us_px_party_sl
            $ alt_day6_us_px_sl_join = True
            pause(1)
        else:
            call alt_day6_us_px_far_gate
    pause(1)
    call alt_day6_us_7dl_concert
    pause(1)
    call alt_day6_us_7dl_supper
    pause(1)
    call alt_day6_us_7dl_disco
    pause(1)
    if alt_day4_neu_us_pixies == 2:
        call alt_day6_us_7dl_tea
    elif alt_day4_neu_us_pixies == 3:
        call alt_day6_us_px_afterwords
    pause(1)
    call alt_day6_us_7dl_sleeptime
    pause(1)
    jump alt_day7_us_7dl_start
    
label alt_day7_us_7dl_start:
    call alt_day7_us_7dl_begin
    pause(1)
    call alt_day7_us_7dl_breakfast
    pause(1)
    if alt_day6_us_px_sl_join:
        call alt_day7_us_px_escape
        pause(1)
        call alt_day7_us_px_bus
        pause(1)
        if alt_day7_us_px_escaped:
            call alt_day7_us_px_wastelands
            pause(1)
            call alt_day7_us_px_fairytale
            return
        else:
            call alt_day7_us_px_mourning
    pause(1)
    call alt_day7_us_7dl_packing
    pause(1)
    call alt_day7_us_7dl_leaving
    if routetag == "us7dl_bad":
        call alt_day7_us_7dl_wakeup
        pause(1)
        if us_pt > 5:
            call alt_day7_us_7dl_reunite
        elif alt_day6_us_7dl_mi_friends == 3:
            call alt_day7_us_7dl_mikuforever
        elif alt_day6_us_7dl_un_friends == 3:
            call alt_day7_us_7dl_lenaforever
        else:
            call alt_day7_us_7dl_verses
        pause(1)
        return
    else:
        call alt_day7_us_px_dejavu
        pause(1)
        if loki:
            call alt_day7_us_px_runaway
        else:
            call alt_day7_us_px_realvu
        return