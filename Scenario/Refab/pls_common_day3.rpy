label alt_day3_start:
    call alt_day3_vars
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ prolog_time() 
    $ alt_chapter(3, u"Утро")
    call alt_day3_begin
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(3, u"Завтрак")   
    call alt_day3_bf
    pause(1)
    if alt_day3_un_event and not alt_day3_duty:
        $ persistent.sprite_time = "day"
        call alt_day3_event_library1
    elif alt_day3_dv_event and not alt_day3_duty:
        call alt_day3_event_estrade
    elif alt_day3_mi_event and not alt_day3_duty:
        call alt_day3_event_music_club
    elif alt_day3_duty:
        call alt_day3_bf_duty
        pause(1)
        if alt_day2_date == 132:
            call alt_day3_event_camp_entrance
        else:
            call alt_day3_map_prepare
    elif alt_day2_date == 132:
        call alt_day3_event_camp_entrance
    else:
        call alt_day3_map_prepare
    pause(1)
# обед
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(3, u"Обед")
    call alt_day3_dinner
    pause(1)
    if alt_day3_duty:
        if alt_day2_date == 3 and alt_day3_dv_event:
            pass
        else:
            call alt_day3_dinner_menu
    else:
        call alt_day3_dinner_menu
    pause(1)
    if alt_day2_date == 3 and alt_day3_dv_event and alt_day3_duty:
        call alt_day3_eventAf_music_club1
    elif alt_day3_un_fz_dinner:
        pass
    elif alt_day3_un_invite == 1:
        call alt_day3_eventAf_library1
    else:
        call alt_day3_mapAf_prepare
    pause(1)
    if alt_day3_un_fz_dinner or alt_day3_dv_rep:
        call alt_day3_aftermath
        pause(1)
        call alt_day3_nightmare
        if alt_day_catapult == 1:
            return
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(3, u"Ужин")
        pause(1)
        call alt_day3_supper1
        pause(1)
        if not alt_day3_un_fz_dinner:
            $ sunset_time ()
            $ persistent.sprite_time = "sunset"
            call alt_day3_supper2
    else:
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(3, u"Ужин")
        call alt_day3_supper
        pause(1)
        if alt_day3_mi_invite2:
            pass
        else:
            $ sunset_time ()
            $ persistent.sprite_time = "sunset"
            call alt_day3_supper2
    pause(1)
# вечер
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(3, u"Танцы")
    call alt_day3_dance_dance
    pause(1)
    if not alt_day3_dv_dj:
        call alt_day3_makeup
        pause(1)
        if alt_day2_date == 132:
            if alt_day3_un_fz_evening:
                jump alt_day3_disco
            else:
                call alt_day3_dv_lf
                pause(1)
                call alt_day3_rockstar
                pause(1)
                if alt_day3_dv2_event or alt_day2_date == 132:
                    call alt_day3_sleeptime
                    pause(1)
                    jump alt_day3_slots
                else:
                    call alt_day3_dv_reunion
                    pause(1)
                    scene black
                    screen alt_timer:
                        add "timer_anim" xalign 0.5 yalign 0.5
                        key "7" action [Hide("alt_timer"), Call("alt_day3_dv_stayhere")]
                        text "ВЕРНУТЬСЯ В ЛАГЕРЬ! (--->7<---)" align (0.5, 0.8) color "#FF0000"
                        timer 2.0 action Call("alt_day3_leave")
                    call screen alt_timer
        if alt_day3_dv_date or (alt_day3_dv2_event and not alt_day3_dv_dj):
            call alt_day3_dv_lf
            pause(1)
            call alt_day3_rockstar
            pause(1)
            if alt_day3_dv2_event or alt_day2_date == 132:
                call alt_day3_sleeptime
                pause(1)
                jump alt_day3_slots
            else:
                call alt_day3_dv_reunion
                pause(1)
                scene black
                screen alt_timer:
                    add "timer_anim" xalign 0.5 yalign 0.5
                    key "7" action [Hide("alt_timer"), Jump("alt_day3_dv_stayhere")]
                    text "ВЕРНУТЬСЯ В ЛАГЕРЬ! (--->7<---)" align (0.5, 0.8) color "#FF0000"
                    timer 2.0 action Jump("alt_day3_leave")
                call screen alt_timer
        else:
            jump alt_day3_disco
    else:
        jump alt_day3_disco # первый танец

label alt_day3_dv_stayhere:
    call alt_day3_dv_stayhere1
    pause(1)
    $ persistent.sprite_time = "night"
    call alt_day3_bath_voyeur
    pause(1)
    call alt_day3_sleeptime
    pause(1)
    jump alt_day3_slots
    
label alt_day3_leave:
    call alt_day3_leave1
    pause(1)
    return

label alt_day3_disco:
    $ persistent.sprite_time = "night"
    $ night_time()
    call alt_day3_choose
    pause(1)
    if alt_day3_sl_day_event2 and alt_day3_dancing:
        call alt_day3_technoquest3
        pause(1)
        jump alt_day3_slots
    else:
        call alt_day3_dance_dance2
        pause(1)
        if alt_day3_un_med_help == 1:
            $ alt_chapter(3, u"Медпункт. Вечер.")
            call alt_day3_med_un
            pause(1)
            if persistent.un_7dl_good_ussr or persistent.un_7dl_good_rf:
                call alt_day3_un_cards
                pause(1)
                call alt_day3_un_strip_play
                pause(1)
                if alt_day3_un_strip_pool_sp == 0:
                    call alt_day3_card_lose
                elif alt_day3_un_strip_pool_un == 0:
                    call alt_day3_card_won
                pause(1)
            call alt_day3_post_strip
            pause(1)
            call alt_day3_sleeptime
            pause(1)
            jump alt_day3_slots
        elif alt_day3_us_bugs == 1 and alt_day2_date != 132:
            call alt_day3_mt_scare
            pause(1)
            call alt_day3_bath_voyeur
            pause(1)
            call alt_day3_sleeptime
            pause(1)
            jump alt_day3_slots
        elif alt_day3_technoquest_st3 == 1:
            if alt_day3_mi_dj or (lp_mi > 7):
                jump alt_day3_disco2
            else:
                call alt_day3_dance_dance2_menu
                pause(1)
                if alt_day3_technoquest_st3_help:
                    if alt_day3_dv_dj or alt_day3_mi_dj:
                        jump alt_day3_disco2
                    else:
                        call alt_day3_technoquest3
                        pause(1)
                        jump alt_day3_slots
                else:
                    if alt_day2_date == 132:
                        call alt_day3_technoquest3
                        pause(1)
                        jump alt_day3_slots
                    else:
                        $ girls_list = ('dv', 'un', 'mi', 'sl')
                        $ lp_max = max( [eval('lp_'+w) for w in girls_list] )
                        $ max_who = [w for w in girls_list if eval('lp_'+w) == lp_max]
                        $ max_who_id = max_who[0] if lp_max > 5 and len(max_who)==1 else 'nobody'
                        call expression 'alt_day3_max_lp_{}'.format(max_who_id)
                        if alt_day3_lp_route == 1 or alt_day3_lp_route == 2:
                            call alt_day3_technoquest3
                            pause(1)
                            jump alt_day3_slots
                        else:
                            jump alt_day3_disco2
        else:
            jump alt_day3_disco2

label alt_day3_disco2:
    $ persistent.sprite_time = "night"
    $ night_time()
    call alt_day3_choose3
    pause(1)
    if alt_day3_mi_date and (alt_day2_date == 4) and (alt_day3_dancing == 41 or alt_day3_dancing == 40):
        call alt_day3_mi_7dl_init
        pause(1)
        jump alt_day4_mi_7dl_start
    elif alt_day3_dancing == 5:
        call alt_day3_sleeptime
        pause(1)
        jump alt_day3_slots
    else:
        call alt_day3_disco_past_d2
        pause(1)
        call alt_day3_bath_voyeur
        pause(1)
        call alt_day3_sleeptime
        pause(1)
        jump alt_day3_slots
