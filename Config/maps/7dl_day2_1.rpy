label alt_day2_map_prepare:
    $ disable_all_zones_alt1()
    $ disable_all_chibi_alt1()
    $ set_zone_alt1('music_club_alt1', 'alt_day2_event_music_club')
    $ set_zone_alt1('clubs_alt1', 'alt_day2_event_clubs')
    $ set_zone_alt1('camp_entrance_alt1', 'alt_day2_event_camp_entrance')
    $ set_zone_alt1('dv_us_house_alt1', 'alt_day2_event_dv_us_house')
    $ set_zone_alt1('dining_hall_alt1', 'alt_day2_event_dining_hall')
    $ set_zone_alt1('sport_area_alt1', 'alt_day2_event_sport_area')
    $ set_zone_alt1('beach_alt1', 'alt_day2_event_beach')
    $ set_zone_alt1('me_mt_house_alt1', 'alt_day2_event_me_mt_house')
    $ set_zone_alt1('library_alt1', 'alt_day2_event_library')
    $ set_zone_alt1('medic_house_alt1', 'alt_day2_event_medic_house')
    if alt_day2_sl_guilty == 0:
        $ set_zone_alt1('square_alt1', 'alt_day2_event_square')
    $ set_zone_alt1('boat_station_alt1', 'alt_day2_event_boat_station')

    $ alt_day2_necessary_done = 0
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(2, u"Знакомство с лагерем")
    
label alt_day2_map:
    $ persistent.sprite_time = "day"
    $ day_time
    stop sound_loop
    stop ambience
    stop music fadeout 6
    play music music_list["everyday_theme"] fadein 3
    if alt_day2_necessary_done != 4:
        play sound sfx_paper_bag
        $ show_map_alt1()
    else:
        return

label alt_day2_event_music_club:
    scene bg ext_musclub_day with fade
    if alt_day2_rendezvous == 4:
        call alt_day2_event_music_club1
    else:
        call alt_day2_event_music_club1
        pause(1)
        call alt_day2_inmusic
        $ alt_day2_necessary_done += 1
        $ disable_current_zone_alt1()
    jump alt_day2_map


label alt_day2_event_clubs:
    call alt_day2_event_clubs1
    if been_there_alt1()>1:
        $ disable_current_zone_alt1()
        jump alt_day2_map
    window hide
    $ alt_day2_necessary_done += 1
    jump alt_day2_map

label alt_day2_event_camp_entrance:
    call alt_day2_event_camp_entrance1
    if been_there_alt1()==2:
        $ disable_current_zone_alt1()
    jump alt_day2_map

label alt_day2_event_dv_us_house:
    call alt_day2_event_dv_us_house1
    if been_there_alt1()>1:
        $ disable_current_zone_alt1()
        jump alt_day2_map
    $ alt_day2_dv_us_house_visited = True
    jump alt_day2_map

label alt_day2_event_dining_hall:
    call alt_day2_event_dining_hall1
    $ disable_current_zone_alt1()
    jump alt_day2_map

label alt_day2_event_sport_area:
    call alt_day2_event_sport_area1
    $ alt_day2_necessary_done += 1
    $ disable_current_zone_alt1()
    jump alt_day2_map

label alt_day2_event_beach:
    call alt_day2_event_beach1
    $ disable_current_zone_alt1()
    jump alt_day2_map

label alt_day2_event_me_mt_house:
    call alt_day2_event_me_mt_house1
    if been_there_alt1()>1:
        $ disable_current_zone_alt1()
        jump alt_day2_map
    window hide
    jump alt_day2_map

label alt_day2_event_library:
    call alt_day2_event_library1
    pause(1)
    call alt_day2_mz
    $ alt_day2_necessary_done += 1
    $ disable_current_zone_alt1()
    jump alt_day2_map

label alt_day2_event_medic_house:
    call alt_day2_event_medic_house1
    if been_there_alt1()>1:
        $ disable_current_zone_alt1()
        jump alt_day2_map
    $ alt_day2_necessary_done += 1
    jump alt_day2_map
    
label alt_day2_event_square:
    $ persistent.sprite_time = "day"
    $ day_time()
    if alt_day2_rendezvous == 2: # второе посещение со Славей
        $ disable_current_zone_alt1()
    else:
        if alt_day2_necessary_done > 1: # пришёл после уборки
            $ disable_current_zone_alt1()
        else:
            if alt_day2_rendezvous == 22: # первое посещение со Славей
                $ alt_day2_necessary_done += 1
                $ set_chibi_alt1('square_alt1', 'sl')
                window hide
            else:
                if loki and alt_day2_rendezvous != 22: # отказ Локи
                    pass
                else: # припахали
                    $ alt_day2_necessary_done += 1
                $ disable_current_zone_alt1()
    $ persistent.sprite_time = "day"
    $ day_time()
    call alt_day2_event_square_1
    if (alt_day2_rendezvous == 2) and (alt_day1_sl_keys_took == 1) and (alt_day2_sl_guilty != 0):
        call alt_day2_sl_hyst
    else:
        call alt_day2_event_square_dunno
    jump alt_day2_map

label alt_day2_event_boat_station:
    call alt_day2_event_boat_station1
    if been_there_alt1()>1 :
        $ disable_current_zone_alt1()
    jump alt_day2_map
