label alt_day4_un_fz_start:
    pause(1)
    call alt_day4_un_fz_vars
    call alt_day4_neu_us_vars
    call alt_day4_sl_cl_vars
    pause(1)
    $ persistent.sprite_time = "prolog"
    $ prolog_time()
    $ alt_chapter(4, u"Лена. ФЗ. Утро")
    call alt_day4_un_fz_begin
    if alt_day2_rendezvous == 2:
        call alt_day4_un_fz_sl
        call alt_day4_fz_play
        call alt_day4_fz_postcard
    if alt_day2_rendezvous == 3:
        call alt_day4_un_fz_dv
        call alt_day4_fz_postcard
        $ persistent.sprite_time = "day"
        $ day_time()
        call alt_day4_fz_dv_dinner
    call alt_day4_fz_lost_coun

    call alt_day5_fz_supper
 
    call alt_day4_fz_sh_choose

    call alt_day4_fz_sh_menu
       
    call alt_day4_fz_old_camp

    call alt_day4_fz_xroad
    
    call alt_day4_fz_exit

    call alt_day4_fz_herbs
    
    if alt_day4_fz_sh == 1 or alt_day4_fz_sh == 4:
        jump alt_day5_fz_start
    elif alt_day4_fz_sh == 2:
        $ routetag = "sl"
        jump alt_day5_sl_start
    elif alt_day4_fz_sh == 3:
        $ routetag = "dv"
        jump alt_day5_dv_start

label alt_day5_fz_start:
    call alt_day5_fz_begin
    if routetag == "mt7dl":
        jump alt_day5_neu_begin
    else:
        return









