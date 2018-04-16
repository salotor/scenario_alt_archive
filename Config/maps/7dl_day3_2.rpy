label alt_day3_mapAf_prepare:
    $ disable_all_zones_alt1()
    $ disable_all_chibi_alt1()
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(3, u"Вообще-то, тихий час!")
    $ set_zone_alt1("music_club_alt1",   "alt_day3_eventAf_music_club")
    if alt_day3_dv_invite or alt_day3_dv_event:
        $ set_chibi_alt1("music_club_alt1",   "dv")
    else:
        $ set_chibi_alt1("music_club_alt1", "mi")
    if not (alt_day3_mi_invite or alt_day3_sl_day_event):
            $ set_zone_alt1("clubs_alt1",        "alt_day3_eventAf_clubs")
            $ set_chibi_alt1("clubs_alt1",        "el")
    $ set_zone_alt1("dining_hall_alt1",  "alt_day3_eventAf_dining_hall")
    $ set_chibi_alt1("dining_hall_alt1",  "us")
    if alt_day3_sl_day_event:
        $ set_zone_alt1("admin_house_alt1", "alt_day3_eventAf_admins")
        $ set_chibi_alt1("admin_house_alt1",        "sl")
    $ set_zone_alt1("me_mt_house_alt1",  "alt_day3_eventAf_me_mt_house")
    $ set_zone_alt1("un_mi_house_alt1", "alt_day3_eventAf_un_mi_house")
    $ set_zone_alt1("library_alt1",      "alt_day3_eventAf_library")
    if alt_day3_un_invite == 1:
        $ set_chibi_alt1("library_alt1",      "un")
    if not alt_day3_sl_day_event:
        $ set_zone_alt1("estrade_alt1",      "alt_day3_eventAf_estrade")
        if alt_day3_mi_invite:
            $ set_chibi_alt1("estrade_alt1",      "?")
    jump alt_day3_mapAf

label alt_day3_mapAf:
    window hide
    stop ambience
    stop sound_loop
    stop music
    scene black with fade
    play music music_list["smooth_machine"] fadein 3
    $ show_map_alt1()

label alt_day3_eventAf_clubs:
    scene bg ext_clubs_day with fade
    play ambience ambience_camp_center_day
    play music music_list["i_want_to_play"] fadein 3
    if been_there_alt1()>1:
        call alt_day3_eventAf_clubs_ladder
        $ disable_current_zone_alt1()
        jump alt_day3_mapAf
    else:
        call alt_day3_eventAf_clubs_technoquest
        pause(1)
        jump alt_day3_mapAf

label alt_day3_eventAf_music_club:
    call alt_day3_eventAf_music_club1
    if alt_day3_dv_invite or alt_day3_dv_event:
        return
    else:
        $ disable_current_zone_alt1()
        window hide
        jump alt_day3_mapAf

label alt_day3_eventAf_un_mi_house:
    call alt_day3_eventAf_un_mi_house1
    if not alt_day3_mi_invite:
        $ disable_current_zone_alt1()
        window hide
        jump alt_day3_mapAf
    else:
        window hide
        return

label alt_day3_eventAf_dining_hall:
    $ persistent.sprite_time = "day"
    call alt_day3_eventAf_dining_hall1
    if alt_day3_us_bugs == 1:
        window hide
        return
    else:
        window hide
        $ disable_current_zone_alt1()
        jump alt_day3_mapAf

label alt_day3_eventAf_admins:
    call alt_day3_eventAf_admins1
    call alt_day3_sl_postlunch
    window hide
    return

label alt_day3_eventAf_me_mt_house:
    call alt_day3_eventAf_me_mt_house1
    window hide
    return

label alt_day3_eventAf_library:
    call alt_day3_eventAf_library1
    scene bg ext_library_day with fade
    play ambience ambience_camp_center_day fadein 1
    if alt_day3_un_invite == 1:
        window hide
        return
    else:
        $ disable_current_zone_alt1()
        jump alt_day3_mapAf

label alt_day3_eventAf_estrade:
    call alt_day3_eventAf_estrade1
    if alt_day3_dv_dj:
        $ alt_day3_dv2_event = False
        $ disable_current_zone_alt1()
        jump alt_day3_mapAf
    else:
        call alt_day3_music
        window hide
        return
