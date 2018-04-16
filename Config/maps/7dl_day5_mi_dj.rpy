label alt_day5_mi_dj_mapprepare:
    window hide
    $ day_time()
    $ persistent.sprite_time = "day"
    $ alt_chapter(5, u"Мику. DJ. В поисках Мику!")
    $ disable_all_zones_alt1()
    $ disable_all_chibi_alt1()
    $ set_zone_alt1('music_club_alt1', 'alt_day5_mi_dj_music_club')
    $ set_chibi_alt1 ('music_club_alt1', '?')
    $ set_zone_alt1('clubs_alt1', 'alt_day5_mi_dj_clubs')
    $ set_chibi_alt1 ('clubs_alt1', '?')
    $ set_zone_alt1('camp_entrance_alt1', 'alt_day5_mi_dj_camp_entrance')
    $ set_chibi_alt1 ('camp_entrance_alt1', '?')
    $ set_zone_alt1('un_mi_house_alt1', 'alt_day5_mi_dj_un_mi_house')
    $ set_chibi_alt1 ('un_mi_house_alt1', '?')
    $ set_zone_alt1('estrade_alt1', 'alt_day5_mi_dj_estrade')
    $ set_chibi_alt1 ('estrade_alt1', '?')
    play music music_list["two_glasses_of_melancholy"] fadein 2
    jump alt_day5_mi_dj_map

label alt_day5_mi_dj_map:
    scene black with fade
    if alt_day5_mi_dj_necessary_done >= 4:
        window hide
        "Я устал и запыхался, я обежал этот чёртов лагерь уже сто раз…"
        "И нигде, ни в одном из мест, где только могла быть девушка, её либо не видели, либо она вот-вот ушла."
        "Я прикинул, куда можно было бы пойти ещё."
        play sound sfx_7dl["eat_horn"] fadein 5
        th "Уже пора ужинать. Время-то как летит."
        dreamgirl "Пойдёшь набивать утробу?"
        th "Да нет. Но там будет вожатая. И Славя. Кажется, пришла пора попросить помощи."
        window hide
        return
    else:
        $ show_map_alt1()

label alt_day5_mi_dj_music_club:
    call alt_day5_mi_dj_music_club1
    $ disable_current_zone_alt1()
    $ alt_day5_mi_dj_necessary_done += 1
    $ alt_day5_mi_dj_musclub_visited = True
    jump alt_day5_mi_dj_map

label alt_day5_mi_dj_clubs:
    call alt_day5_mi_dj_clubs1
    $ disable_current_zone_alt1()
    $ alt_day5_mi_dj_necessary_done += 1
    jump alt_day5_mi_dj_map

label alt_day5_mi_dj_camp_entrance:
    call alt_day5_mi_dj_camp_entrance1
    $ disable_current_zone_alt1()
    $ alt_day5_mi_dj_entrance_visited = True
    $ alt_day5_mi_dj_necessary_done += 1
    jump alt_day5_mi_dj_map

label alt_day5_mi_dj_un_mi_house:
    call alt_day5_mi_dj_un_mi_house1
    $ disable_current_zone_alt1()
    $ alt_day5_mi_dj_home_visited = True
    $ alt_day5_mi_dj_necessary_done += 1
    jump alt_day5_mi_dj_map

label alt_day5_mi_dj_estrade:
    call alt_day5_mi_dj_estrade1
    $ disable_current_zone_alt1()
    $ alt_day5_mi_dj_estrade_visited = True
    $ alt_day5_mi_dj_necessary_done += 1
    if alt_day5_mi_dj_necessary_done < 1: # как и нахрена оно тут?
        play music music_list["two_glasses_of_melancholy"] fadein 2
    else:
        stop music fadeout 6
    jump alt_day5_mi_dj_map