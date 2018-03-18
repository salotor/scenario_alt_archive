label alt_day3_map_prepare:
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(3, u"День")
    $ disable_all_zones_alt1()
    $ disable_all_chibi_alt1()
    
    play music music_list["everyday_theme"]

    $ set_zone_alt1("music_club_alt1",   "alt_day3_event_music_club")
    if alt_day3_mi_event:
        $ set_chibi_alt1("music_club_alt1",   "mi")
    $ set_zone_alt1("clubs_alt1",        "alt_day3_event_clubs")
    $ set_zone_alt1("camp_entrance_alt1","alt_day3_event_camp_entrance")
    if alt_day2_date == 132:
        $ set_chibi_alt1("camp_entrance_alt1","me")
    $ set_zone_alt1("dining_hall_alt1",  "alt_day3_event_dining_hall")
    $ set_zone_alt1("sport_area_alt1",   "alt_day3_event_sport_area")
    $ set_zone_alt1("beach_alt1",        "alt_day3_event_beach")
    if alt_day3_sl_event:
        $ set_chibi_alt1("beach_alt1",        "sl")
    if alt_day2_date != 132:
        $ set_zone_alt1("library_alt1",      "alt_day3_event_library")
        if alt_day3_un_event:
            $ set_chibi_alt1("library_alt1",      "un")
    $ set_zone_alt1("medic_house_alt1",  "alt_day3_event_medic_house")
    $ set_zone_alt1("estrade_alt1",      "alt_day3_event_estrade")
    if alt_day3_dv_event:
        $ set_chibi_alt1("estrade_alt1",      "dv")
    $ set_zone_alt1("square_alt1",       "alt_day3_event_square")
    $ set_zone_alt1("boat_station_alt1", "alt_day3_event_boat_station")

    jump alt_day3_map

label alt_day3_map:
    $ show_map_alt1()

label alt_day3_event_music_club:
    call alt_day3_event_music_club1
    if alt_day3_mi_event:
        return
    else:
        $ disable_current_zone_alt1()
        jump alt_day3_map


label alt_day3_event_clubs:
    call alt_day3_event_clubs1
    $ disable_current_zone_alt1()
    jump alt_day3_map

label alt_day3_event_camp_entrance:
    call alt_day3_event_camp_entrance1
    if alt_day2_date == 132:
       return
    else:
        $ disable_current_zone_alt1()
        jump alt_day3_map

label alt_day3_event_dining_hall:
    call alt_day3_event_dining_hall1
    $ disable_current_zone_alt1()
    jump alt_day3_map
    
label alt_day3_event_sport_area:
    call alt_day3_event_sport_area1
    $ disable_current_zone_alt1()
    jump alt_day3_map

label alt_day3_event_beach:
    call alt_day3_event_beach1
    if alt_day3_sl_event:
        return
    else:
        $ disable_current_zone_alt1()
        jump alt_day3_map

label alt_day3_event_library:
    $ persistent.sprite_time = "day"
    call alt_day3_event_library1
    if alt_day3_un_event:
        return
    else:
        $ disable_current_zone_alt1()
        jump alt_day3_map

label alt_day3_event_medic_house:
    call alt_day3_event_medic_house1
    $ disable_current_zone_alt1()
    jump alt_day3_map

label alt_day3_event_estrade:
    call alt_day3_event_estrade1
    return

label alt_day3_event_square:
    call alt_day3_event_square1
    $ disable_current_zone_alt1()
    jump alt_day3_map

label alt_day3_event_boat_station:
    call alt_day3_event_boat_station1
    $ disable_current_zone_alt1()
    jump alt_day3_map
