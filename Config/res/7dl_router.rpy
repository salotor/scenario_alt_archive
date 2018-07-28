label alt_day3_slots:
   scene scenery
   with dissolve
   $ alt_spt = 0
   $ alt_hpt = 0
    
label alt_day3_router_dv:
    if alt_day3_dv_evening:
        "Поворочавшись, я улыбнулся посетившей мои сны Алисе."
        if lp_dv >= 11:
            "Мне снилась Алиса…"
            window hide
            if alt_day3_dv_evening:
                $ routetag = "dv7dl"
                jump alt_day4_dv_7dl_start
            else:
                jump alt_day3_router_un
            
label alt_day3_router_un:
    if lp_un >= 12 or (lp_un >= 11 and (counter_sl_7dl == 1)):
        "Мне снилась Лена…"
        window hide
    if (alt_day3_un_med_help == 1) and (lp_un >= 13):
        $ routetag = "un7dl"
        jump alt_day4_un_7dl_start
    elif (('un_fz' in list_d2_date_7dl)) and (alt_day3_dancing == 132):
        $ routetag = "un7dl"
        jump alt_day4_un_fz_start
    else:
        jump alt_day3_router_mi

label alt_day3_router_mi:
    if lp_mi >= 13:
        if alt_day3_mi_dj:
            "Мне снилась Мику…"
            "Правда, не очень долго."
            window hide
            $ routetag = "mi7dl"
            jump alt_day4_mi_dj_start
    else:
        jump alt_day3_router_sl

label alt_day3_router_sl:
    if lp_sl >= 13:
        "Мне снилась Славя…"
        window hide
        if (counter_sl_7dl == 5):
            jump alt_day4_sl_7dl_start
        elif counter_sl_cl == 5:
            $ lp_us -= 3
            $ routetag = "sl"
            jump alt_day4_sl_start
    else:
        jump alt_day3_router_neutral
    
label alt_day3_router_neutral:
    if alt_dlc_active and alt_day3_uvao_spotted:
        $ routetag = "uv"
        "Сон был тревожным…"
        window hide
        jump alt_day4_start_uvao
    else:
         jump alt_day4_neu_begin