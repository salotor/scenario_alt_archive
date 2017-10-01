label alt_day4_mi_7dl_start:
    call alt_day4_mi_7dl_vars
    call alt_day4_mi_7dl_ch1
    pause(1)
    call alt_day4_mi_7dl_ch2
    if alt_day4_mi_7dl_donor:
        call alt_day4_mi_7dl_ch3
        pause(1)
        call alt_day4_mi_7dl_ch4
    else:
        call alt_day4_mi_7dl_ch4
    pause(1)
    if not alt_day3_mi_donor:
        call alt_day4_mi_7dl_ch5a
        pause(1)
    else:
        call alt_day4_mi_7dl_ch5b
        pause(1)
        call alt_day4_mi_7dl_ch52
    pause(1)
    call alt_day4_mi_7dl_ch6
    pause(1)
    call alt_day4_mi_7dl_ch7
    pause(1)
    if alt_day3_mi_donor:
        call alt_day4_mi_7dl_ch8a
        pause(1)
        if alt_day4_mi_7dl_ev_savior and herc:
            call alt_day4_mi_7dl_ch81
        elif alt_day4_mi_7dl_ev_savior and loki:
            call alt_day4_mi_7dl_ch82
        else:
            call alt_day4_mi_7dl_ch83
    else:
        call alt_day4_mi_7dl_ch8b
    pause(1)
    jump alt_day5_mi_7dl_start

label alt_day5_mi_7dl_start:
    call alt_day5_mi_7dl_vars
    if alt_day4_mi_7dl_ev_savior and loki:
        call alt_day5_mi_7dl_rain_2gether
    else:
        call alt_day5_mi_7dl_morning
    pause(2)
    call alt_day5_mi_7dl_dinner
    pause(1)
    call alt_day5_mi_7dl_router
    pause(1)
    if persistent.mi_7dl_good_human or persistent.mi_good_star:
        call alt_day5_mi_7dl_lost
        pause(1)
        if alt_day5_mi_7dl_voyeur:
            call alt_day5_mi_7dl_hn
        else:
            call alt_day5_mi_7dl_branch
    else:
        call alt_day5_mi_7dl_branch
    pause(2)
    call alt_day5_mi_7dl_potato
    pause(1)
    if not alt_day5_mi_7dl_voyeur:
        call alt_day5_mi_7dl_camp_cleance
        pause(2)
    call alt_day5_mi_7dl_firecamp
    pause(3)
    call alt_day5_mi_7dl_goodnight
    pause(2)
    jump alt_day6_mi_7dl_start
    
label alt_day6_mi_7dl_start:
    call alt_day6_mi_7dl_vars
    call alt_day6_mi_7dl_wakeup
    pause(1)
    if alt_day5_mi_7dl_voyeur:
        call alt_day6_mi_7dl_soul
        pause(1)
        call alt_day6_mi_7dl_dinner
        pause(1)
        call alt_day6_mi_7dl_soul_day
        pause(1)
        call alt_day6_mi_7dl_miku_sakishita
        pause(1)
        $ alt_day6_mi_7dl_left = True
        call alt_day6_mi_7dl_miku_farewell_finale
        pause(1)
        if alt_day7_mi_7dl_trait == 3:
            return
        call alt_day6_mi_7dl_miku_farewell_soul
    elif alt_hpt < alt_spt:
        call alt_day6_mi_7dl_star
        pause(1)
        call alt_day6_mi_7dl_dinner
        pause(1)
        call alt_day6_mi_7dl_star_day
        pause(1)
        call alt_day6_mi_7dl_miku_sakishita
        $ alt_day6_mi_7dl_left = True
        call alt_day6_mi_7dl_miku_farewell_finale
        pause(1)
        call alt_day6_mi_7dl_miku_farewell_star
    else:
        call alt_day6_mi_7dl_human
        pause(1)
        call alt_day6_mi_7dl_human_day
    pause(1)
    call alt_day6_mi_7dl_discoteque
    pause(1)
    if alt_day7_mi_7dl_trait == 1:
        pause(1)
        return
    jump alt_day7_mi_7dl_start
    
label alt_day7_mi_7dl_start:
    #Роутер концовок
    if alt_day6_mi_7dl_left:
        if alt_day5_mi_7dl_voyeur:
            if and herc:
                $ routetag = "mi7dlcas"
            elif loki:
                $ routetag = "mi7dlcas"
            else:
                $ routetag = "mi7dlcas"
        else:
            if alt_spt >= 8:
                $ routetag = "mi7dlvoca"
            elif alt_spt > 6 and alt_day5_mi_7dl_kiss:
                $ routetag = "mi7dlcas1"
            else:
                $ routetag = "mi7dlvoca1"
    else:
        if lp_mi > 16:
            if alt_hpt >= 9:
                $ routetag = "mi7dldress"
            else:
                $ routetag = "mi7rej"
        else:
            $ routetag = "mi7dlcas2"
    call alt_day7_mi_7dl_wakeup
    pause(1)
    call alt_day7_mi_7dl_packing
    pause(1)
    if alt_day6_mi_7dl_left:
        call alt_day7_mi_7dl_departure_lone
        pause(1)
        if alt_day5_mi_7dl_voyeur:
            if herc:
                call alt_day7_mi_7dl_unlike
            elif loki:
                call alt_day7_mi_7dl_sinthetic
            else:
                call alt_day7_mi_7dl_come_back
        else:
            if alt_spt >= 8:
                call alt_day7_mi_7dl_sparkle
                if alt_day_binder == 1:
                     call alt_day7_mi_7dl_postscriptum
            elif alt_spt > 6 and alt_day5_mi_7dl_kiss:
                call alt_day7_mi_7dl_club27
            else:
                call alt_day7_mi_7dl_dam_CPU
        pause(1)
        return
    else:
        call alt_day7_mi_7dl_departure_a2th
        pause(1)
        if lp_mi > 16:
            if alt_hpt >= 9:
                call alt_day7_mi_7dl_dark_dreams
            else:
                call alt_day7_mi_7dl_happy_again
        else:
            call alt_day7_mi_7dl_liar
    pause(1)
    return