init:
    $ mods["replays_7dl"] = u"Реплеи 7дл"
    $ mod_tags["replays_7dl"] = ["length:days","gameplay:vn","protagonist:male"]
    
label replays_7dl:

    $ init_map_zones_alt1()
    $ init_map_zones_alt2()
    $ day_time()
    $ persistent.sprite_time = "day"
    call screen replay_buttons_7dl

init 2:
    call alt_day0_vars
    call alt_day1_vars
    call alt_day2_vars
    call alt_day3_vars
    call alt_day5_sl_wh_vars
    call alt_day5_us_7dl_vars
    call alt_day4_mi_7dl_vars
    call alt_day5_mi_7dl_vars
    call alt_day6_mi_7dl_vars
    call alt_day5_mt_7dl_vars
    call alt_day6_mt_7dl_vars
    call alt_day4_neu_us_vars
    call alt_day5_neu_us_vars
    call alt_day4_sl_cl_vars
    call alt_day5_sl_cl_vars
    call alt_day6_sl_cl_vars
    call alt_day7_sl_cl_vars
    call alt_day4_mi_dj_vars
    call alt_day5_mi_dj_vars
    call alt_day6_mi_dj_vars
    call alt_day4_un_7dl_vars
    call alt_day5_un_7dl_vars
    call alt_day6_un_7dl_vars
    call alt_day4_un_fz_vars
    call alt_day4_mi_cl_vars
    call alt_day4_dv_7dl_vars
    call alt_day6_dv_7dl_vars
    call alt_day6_us_px_vars
    call alt_day6_us_7dl_vars
    call alt_day7_us_px_vars
    $ make_names_known_7dl()
    
screen replay_buttons_7dl:
    if renpy.seen_label("alt_day7_mt_7dl_loopback"):
        textbutton "Ольга, утро":
            style "log_button"
            text_style "settings_link"
            yalign 0.65
            xalign 0.5
            action Replay("alt_day7_mt_7dl_loopback", scope={"alt_day5_mt_7dl_hentai":True}, locked=None)
    else:
        text "Фок ю":
            color "#64483c"
            font header_font
            size 30
            yalign 0.65
            xalign 0.5
