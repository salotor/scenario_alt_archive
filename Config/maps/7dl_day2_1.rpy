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
    if counter_sl_cl == 0:
        $ set_zone_alt1('square_alt1', 'alt_day2_event_square')
    $ set_zone_alt1('boat_station_alt1', 'alt_day2_event_boat_station')

    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(2, u"Знакомство с лагерем")
    
label alt_day2_map:
    $ persistent.sprite_time = "day"
    $ day_time
    play music music_7dl["everyday"] fadein 3
    
    if len(list_voyage_7dl) < 4: 
        play sound sfx_paper_bag
        $ show_map_alt1()
    else:
        return

label alt_day2_event_music_club:
    scene bg ext_musclub_day with fade
    if ('dv_prep' in list_d2_convoy_7dl):
        call alt_day2_event_music_club1
    else:
        call alt_day2_event_music_club1
        pause(1)
        call alt_day2_inmusic
        $ list_voyage_7dl.append('music_club')
        $ disable_current_zone_alt1()
    jump alt_day2_map


label alt_day2_event_clubs:
    call alt_day2_event_clubs1
    if been_there_alt1()>1:
        $ disable_current_zone_alt1()
        jump alt_day2_map
    window hide
    $ list_voyage_7dl.append('men_clubs')
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
    $ list_voyage_7dl.append('sport_area')
    $ disable_current_zone_alt1()
    jump alt_day2_map

label alt_day2_event_beach:
    $ list_voyage_7dl.append('beach')
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
    $ list_voyage_7dl.append('library')
    $ disable_current_zone_alt1()
    jump alt_day2_map

label alt_day2_event_medic_house:
    call alt_day2_event_medic_house1
    if been_there_alt1()>1:
        $ disable_current_zone_alt1()
        jump alt_day2_map
    $ list_voyage_7dl.append('medic')
    jump alt_day2_map
    
label alt_day2_event_square:
    $ persistent.sprite_time = "day"
    $ day_time()
    if ('sl' in list_d2_convoy_7dl): # второе посещение со Славей
        $ disable_current_zone_alt1()
        if alt_day1_sl_keys_took == 1:
            call alt_day2_sl_hyst
        else:
            call alt_day2_event_square_dunno
    else:
        if 'cleaning_sl' in list_voyage_7dl:# пришёл после уборки
            $ disable_current_zone_alt1()
        else:
            if ('sl_prep' in list_d2_convoy_7dl) and (len(list_voyage_7dl) < 2): # первое посещение со Славей
                $ set_chibi_alt1('square_alt1', 'sl')
                window hide
            else:
                $ disable_current_zone_alt1()
        call alt_day2_event_square_1
    jump alt_day2_map

label alt_day2_event_boat_station:
    call alt_day2_event_boat_station1
    if been_there_alt1()>1 :
        $ disable_current_zone_alt1()
    jump alt_day2_map
