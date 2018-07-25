label alt_day4_sl_start:
    if (alt_day3_sl_day_event2 != 0) and lp_sl >= 13: # прямой выход
        call alt_day4_sl_cl_vars
        call alt_day4_un_fz_vars
        call alt_day4_neu_us_vars
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(4, u"Славя. Утро.")
        call alt_day4_sl_begin
        pause(1)
    call alt_day4_sl_cl_shurik
    pause(1)
    if alt_day4_sl_tut_iz:
        call alt_day4_sl_laundry
        pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(4, u"Славя. Вечер.")
    call alt_day4_sl_supper
    pause(1)
    call alt_day4_sl_party_up
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(4, u"Славя. Поиски.")
    call alt_day4_sl_lf_coop
    pause(1)
    $ persistent.sprite_time = "night"
    $ night_time()
    call alt_day4_sl_old_camp
    pause(1)
    if alt_day4_sl_wh: # новая переменная
        $ persistent.sprite_time = "night"
        $ night_time()
        call alt_day4_sl_wh_night
        pause(1)
        if alt_day5_sl_wh_transit:  # новая переменная
            jump alt_day5_sl_wh_start
    else:
        $ persistent.sprite_time = "night"
        call alt_day4_sl_old_camp2
        pause(1)
    $ persistent.sprite_time = "day"
    call alt_day4_sl_cs_night
    pause(1)
    jump alt_day5_sl_start

label alt_day5_sl_start:
    pause(1)
    call alt_day5_sl_cl_vars
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(5, u"Славя. Утро.")
    call alt_day5_sl_begin # может разбить на несколько?
    pause(1)
    if alt_day_catapult == 1:
        return
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(5, u"Славя. День.")
    call alt_day5_sl_dinner
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(5, u"Славя. Вечер.")
    call alt_day5_sl_supper
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(5, u"Славя. Костёр.")
    call alt_day5_sl_fire
    pause(1)
    $ persistent.sprite_time = "night"
    $ night_time()
    $ alt_chapter(5, u"Славя. Ночь.")
    call alt_day5_sl_night
    pause(1)
    jump alt_day6_sl_start

label alt_day6_sl_start:
    pause(1)
    call alt_day6_sl_cl_vars
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(6, u"Славя. Утро.")
    call alt_day6_sl_begin # разбить?
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    call alt_day6_sl_morgen
    pause(1)
    call alt_day6_sl_ba_quest1
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(6, u"Славя. День.")
    call alt_day6_sl_dinner
    pause(1)
    call alt_day6_sl_amp_list
    pause(1)
    $ persistent.sprite_time = "day"
    $ day_time()
    call alt_day6_sl_amp_club
    pause(1)
    if alt_day6_sl_shirt or alt_sp < 4:
        call alt_day6_sl_ambulance
        pause(1)
        call alt_day6_sl_concert
        pause(1)
        $ persistent.sprite_time = "night"
        $ night_time()
        $ alt_chapter(6, u"Славя. Снова один.")
        call alt_day6_sl_sh_tug
        pause(1)
    else:
        call alt_day6_sl_true_route
        pause(1)
        if loki and lp_sl < 18:
            call alt_day6_sl_cl_become_a_hero
            pause(1)
            return
        if alt_day6_sl_int == 1:
            if alt_sp >= 6 and (persistent.sl_cl_good_rf or persistent.sl_cl_good_rf2 or persistent.sl_cl_good_ussr):
                $ persistent.sprite_time = "prolog"
                $ prolog_time()
                call alt_day6_sl_intellectual
                pause(1)
                if alt_day6_sl_int == 2:
                    $ routetag = "sltrue"
                    $ persistent.sprite_time = "prolog"
                    $ prolog_time()
                    $ alt_chapter(7, u"Славя. Фантазм.")
                    call alt_day7_sl_fear
                    pause(1)
                    $ persistent.sprite_time = "day"
                    $ day_time()
                    call alt_day7_sl_1996
                    pause(1)
                    if alt_day6_sl_int == 3:
                        call alt_day7_sl_loop
                        pause(1)
                        call alt_day7_sl_loop2
                        if alt_day6_sl_int == 4:
                            call alt_day7_sl_will
                            pause(1)
                            return
                        else:
                            call alt_day7_sl_duty
                            pause(1)
                            return
                call alt_day7_sl_lone
                pause(1)
                return
        call alt_day6_sl_regular_arc
        pause(1)
        $ alt_chapter(6, u"Славя. Концерт.")
        $ persistent.sprite_time = "day"
        call alt_day6_sl_hala
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(6, u"Славя. Танцы")
        call alt_day6_sl_dance
        pause(1)
        call alt_day6_sl_dancing
        pause(1)
        $ persistent.sprite_time = "night"
        $ night_time()
        $ alt_chapter(6, u"Славя. Ночь.")
        call alt_day6_sl_debarkader
        pause(1)
    jump alt_day7_sl_start

label alt_day7_sl_start:
    pause(1)
    call alt_day7_sl_cl_vars
    pause(1)
    call alt_day7_sl_begin
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    call alt_day7_sl_breakfast
    pause(1)
    call alt_day7_sl_bl_tt_map
    pause(1)
    call alt_day7_sl_dinner
    if (lp_sl >= 18) or (alt_sp >= 6):
        if alt_day6_sl_good == 1:
            if lp_sl >= 18:
                call alt_day7_sl_good
            elif alt_sp >= 6:
                call alt_day7_sl_rf_good
            pause(1)
            if alt_day6_sl_arc == 1:
                $ persistent.sprite_time = "prolog"
                $ prolog_time()
                call alt_day8_sl_postscriptum
        elif alt_day6_sl_good == 3:
            call alt_day7_sl_cl_bad
        else:
            if alt_day6_sl_arc == 1 and lp_sl > 20:
                if alt_day6_sl_good == 2:
                    call alt_day7_sl_rf_good
                else:
                    call alt_day7_sl_rf2
            else:
                if alt_sp >= 6:
                    call alt_day7_sl_reject_late
                    $ alt_day7_sl_gl = ('dv', 'un', 'mi', 'us')
                    $ alt_day7_sl_lp_counter = max( [eval('lp_'+w) for w in alt_day7_sl_gl] )
                    $ alt_day7_sl_lp_top = [w for w in alt_day7_sl_gl if eval('lp_'+w) == alt_day7_sl_lp_counter]
                    $ alt_day7_sl_lp_top_id = alt_day7_sl_lp_top[0] if alt_day7_sl_lp_counter >= 1 and len(alt_day7_sl_lp_top)==1 else 'mt'
                    call expression 'alt_day7_sl_rej_{}'.format(alt_day7_sl_lp_top_id)
                    pause(1)
                    call alt_day7_sl_rej_end
                elif lp_sl >= 18:
                    call alt_day7_sl_reject_same
        pause(1)
        return
    call alt_day7_sl_cl_bad
    pause(1)
    if alt_day6_sl_arc == 1:
        $ persistent.sprite_time = "prolog"
        $ prolog_time()
        call alt_day8_sl_postscriptum
        pause(1)
    return