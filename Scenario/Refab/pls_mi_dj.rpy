label alt_day4_mi_dj_start:
    pause(1)
    call alt_day4_mi_dj_vars
    pause(1)
    call alt_day4_mi_dj_begin
    pause(1)
    if alt_day4_mi_dj_hedg:
        call alt_day4_mi_dj_hedg_hunt
    pause(1)
    call alt_day4_mi_dj_morning
    pause(1)
    call alt_day4_mi_dj_day
    pause(1)
    if alt_day3_technoquest_st1 or alt_day3_technoquest_st2:
        call alt_day4_mi_dj_radio
        pause(1)
        call alt_day4_mi_dj_dinner
        pause(1)
    else:
        call alt_day4_mi_dj_cleaning
        pause(1)
        if not alt_day4_mi_dj_hedg:
            call alt_day4_mi_dj_dinner
            pause(1)
        else:
            call alt_day4_mi_dj_dinner2
            pause(1)
    call alt_day4_mi_dj_repetition # добавить разбивку?
    pause(1)
    call alt_day4_mi_dj_supper
    pause(1)
    call alt_day4_mi_dj_evening
    pause(1)
    call alt_day4_mi_dj_night
    pause(1)
    call alt_day4_mi_dj_sleeptime
    pause(1)
    jump alt_day5_start_mi_dj
    
label alt_day5_start_mi_dj:
    pause(1)
    call alt_day5_mi_dj_vars
    pause(1)
    call alt_day5_begin_mi_dj
    pause(1)
    call alt_day5_mi_dj_cinema
    pause(1)
    call alt_day5_mi_dj_dinner
    pause(1)
    call alt_day5_mi_dj_mapprepare
    pause(1)
    call alt_day5_mi_dj_supper
    pause(1)
    if alt_day5_mi_dj_voyeur == 2:
        call alt_day5_mi_dj_voyeur_2
    elif alt_day5_mi_dj_voyeur == 3:
        call alt_day5_mi_dj_voyeur_3
    else:
        call alt_day5_mi_dj_voyeur_4
    pause(1)
    if alt_day5_mi_dj_voyeur == 4 or (alt_day5_mi_dj_voyeur == 2 and alt_day5_mi_dj_dv_blade):
        call alt_day5_mi_dj_late_evening
        pause(1)
        if alt_day5_mi_dj_favorite_song:
            call alt_day5_mi_dj_evening_club1
            pause(1)
            if alt_day5_mi_dj_forgive:
                call alt_day5_mi_dj_sleeptime
                pause(1)
            else:
                call alt_day5_mi_dj_evening_club2
                pause(1)
                if not alt_day5_mi_dj_hentai:
                    call alt_day5_mi_dj_sleeptime
                    pause(1)
        else:
            call alt_day5_mi_dj_sleeptime
            pause(1)
    else:
        call alt_day5_mi_dj_sleeptime
        pause(1)
    jump alt_day6_start_mi_dj
    
label alt_day6_start_mi_dj:
    pause(1)
    call alt_day6_mi_dj_vars
    pause(1)
    if alt_day5_mi_dj_hentai:
        call alt_day6_mi_dj_good
        pause(1)
    else: 
        call alt_day6_mi_dj_neutral
        pause(1)
    call alt_day6_mi_dj_radio
    pause(1)
    call alt_day6_mi_dj_dinner # возможно разбить на 3 лейбла: общий и по проверке alt_day5_mi_dj_hentai
    pause(1)
    call alt_day6_mi_dj_concert
    pause(1)
    if alt_day5_mi_dj_voyeur != 4:
        if alt_day6_mi_dj_dv_evil or alt_day6_mi_dj_sl_evil:
            call alt_day6_mi_dj_reject
            pause(1)
            if alt_day6_mi_dj_un_evil:
                call alt_day6_mi_dj_supper
                pause(1)
            else:
                call alt_day6_mi_dj_newswall
                pause(1)
                call alt_day6_mi_dj_late_supper
                pause(1)
        else:
            if alt_day6_mi_dj_sonic_agreed: # новая переменная
                if alt_day5_mi_dj_cut:
                    call alt_day6_mi_dj_newswall
                    pause(1)
                else:
                    call alt_day6_mi_dj_sonic
                    pause(1)
                call alt_day6_mi_dj_late_supper
                pause(1)
            else:
                call alt_day6_mi_dj_reject
                pause(1)
                if alt_day6_mi_dj_un_evil:
                    call alt_day6_mi_dj_supper
                    pause(1)
                else:
                    call alt_day6_mi_dj_newswall
                    pause(1)
                    call alt_day6_mi_dj_late_supper
                    pause(1)
    else:
        call alt_day6_mi_dj_sonic
        pause(1)
        call alt_day6_mi_dj_late_supper
        pause(1)
    call alt_day6_mi_dj_discotheque
    pause(1)
    call alt_day6_mi_dj_first_dance
    pause(1)
    call alt_day6_mi_dj_second_dance 
    pause(1)
    if lp_mi >= 19 and not alt_day6_mi_dj_me_evil:
        call alt_day6_mi_dj_dance2_success
        pause(1)
    else:
        call alt_day6_mi_dj_dance2_fail
        pause(1)
        if alt_day6_mi_dj_rejected and alt_day6_mi_dj_letmeout:
            return
    jump alt_day7_mi_dj_start
    
label alt_day7_mi_dj_start:
    if alt_day6_mi_dj_hentai2:
        call alt_day7_mi_dj_together
        pause(1)
    else:
        call alt_day7_mi_dj_alone
        pause(1)
    if alt_day6_mi_dj_hentai1:
        call alt_day7_mi_dj_badfeel
        pause(1)
    call alt_day7_mi_dj_preparations
    pause(1)
    if alt_day6_mi_dj_letmeout or alt_day6_mi_dj_letmestay:
        call alt_day7_mi_dj_epilogue_frost
        pause(1)
        if alt_day6_mi_dj_letmeout:
            call alt_day7_mi_dj_bad_end
            pause(1)
        else:
            call alt_day7_mi_dj_true_end
            pause(1)
    elif alt_day6_mi_dj_hentai2 or alt_day6_mi_dj_no_hentai:
        call alt_day7_mi_dj_good
        pause(1)
        if alt_day6_mi_dj_hentai2:
            call alt_day7_mi_dj_jp_good_end
            pause(1)
        elif alt_day6_mi_dj_no_hentai:
            call alt_day7_mi_dj_rf_good_end
            pause(1)
               
    return