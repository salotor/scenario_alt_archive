label alt_day7_sl_bl_tt_map:
    $ persistent.sprite_time = "day"
    $ day_time()
    $ disable_all_zones_alt2()
    $ disable_all_chibi_alt2()
    $ set_zone_alt2('admin_house_alt2', 'alt_day7_sl_admins')
    $ set_zone_alt2('kyber_club_alt2', 'alt_day7_sl_clubs')
    $ set_zone_alt2('dining_hall_alt2', 'alt_day7_sl_dining_hall')
    $ set_zone_alt2('volleyball_alt2', 'alt_day7_sl_volleyball_alt')
    $ set_zone_alt2('estrade_alt2', 'alt_day7_sl_estrade')
    $ alt_day7_sl_map_progress = 0
    jump alt_day7_sl_map

label alt_day7_sl_map:
    play music music_list["smooth_machine"] fadein 2
    if alt_day7_sl_map_progress > 4:
        $ set_zone_alt2('square_alt2', 'alt_day7_sl_square')
        if alt_day6_sl_arc != 1:
            $ set_zone_alt2('boat_station_alt2', 'alt_day7_sl_boat_station')
        else:
            $ set_zone_alt2('beach_alt2', 'alt_day7_sl_beach')
    scene black with fade
    $ show_map_alt2()

label alt_day7_sl_admins:
    $ alt_day7_sl_code = True
    call alt_day7_sl_admins1
    $  alt_day7_sl_map_progress += 1
    $ disable_current_zone_alt2()
    jump alt_day7_sl_map

label alt_day7_sl_square:
    call alt_day7_sl_square1
    if alt_day7_sl_code or persistent.d3_code:
        if alt_day7_sl_code:
            if (persistent.mi_7dl_good_human or persistent.mi_7dl_good_star) and persistent.dv_7dl_good_ussr and persistent.sl_7dl_good_ussr and persistent.un_7dl_good_ussr and persistent.mt_7dl_good and persistent.us_7dl_good:
                jump alt_day7_d3_rejuv
        else:
           jump alt_day7_d3_rejuv
    $  alt_day7_sl_map_progress += 1
    $ disable_current_zone_alt2()
    call alt_day7_sl_beach
    return
    
label alt_day7_sl_clubs:
    call alt_day7_sl_clubs1
    $  alt_day7_sl_map_progress += 1
    $ disable_current_zone_alt2()
    jump alt_day7_sl_map
    
label alt_day7_sl_dining_hall:
    call alt_day7_sl_dining_hall1
    $  alt_day7_sl_map_progress += 1
    $ disable_current_zone_alt2()
    jump alt_day7_sl_map
    
label alt_day7_sl_sport_area:
    call alt_day7_sl_sport_area1
    $  alt_day7_sl_map_progress += 1
    $ disable_current_zone_alt2()
    jump alt_day7_sl_map
    
label alt_day7_sl_volleyball_alt:
    call alt_day7_sl_volleyball_alt1
    $  alt_day7_sl_map_progress += 1
    $ disable_current_zone_alt2()
    jump alt_day7_sl_map
    
label alt_day7_sl_estrade:
    call alt_day7_sl_estrade1
    $  alt_day7_sl_map_progress += 1
    $ disable_current_zone_alt2()
    jump alt_day7_sl_map
    
label alt_day7_sl_boat_station:
    call alt_day7_sl_boat_station1
    call alt_day7_sl_beach
    return