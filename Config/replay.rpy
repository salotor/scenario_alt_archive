init:
    $ mods["replays_7dl"] = u"Реплеи 7дл"
    $ mod_tags["replays_7dl"] = ["length:days","gameplay:vn","protagonist:male"]
    
label replays_7dl:

    $ init_map_zones_alt1()
    $ init_map_zones_alt2()
    $ day_time()
    $ persistent.sprite_time = "day"
    call screen replays_route_choice_7dl

init 9999 python:
    cursive_font = default_7dl_path + "Pics/fonts/olgactt.ttf"

    style.replays_textbutton = Style(style.base_font)
    style.replays_textbutton.font  = cursive_font
    style.replays_textbutton.size = 60
    style.replays_textbutton.kerning = 3
    style.replays_textbutton.color = "#7847f3"
    style.replays_textbutton.hover_color = "#2f059a"
    style.replays_textbutton.selected_color = "#7847f3"
    style.replays_textbutton.selected_idle_color = "#7847f3"
    style.replays_textbutton.selected_hover_color = "#2f059a"
    style.replays_textbutton.insensitive_color = "#7847f3"

    style.replays_text = Style(style.base_font)
    style.replays_text.font  = cursive_font
    style.replays_text.size = 60
    style.replays_text.kerning = 3
    style.replays_text.color = "#808080"
    
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
    
screen replays_route_choice_7dl:
    textbutton "Основной рут":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.2
        ypos 0.05
        action [Hide("replays_common_choice_7dl", transition=Dissolve(0.2)), Hide("replays_un_choice_7dl", transition=Dissolve(0.2)), Hide("replays_sl_choice_7dl", transition=Dissolve(0.2)), Hide("replays_dv_choice_7dl", transition=Dissolve(0.2)), Hide("replays_mi_choice_7dl", transition=Dissolve(0.2)), Show("replays_common_choice_7dl", transition=Dissolve(0.2))]
    
    textbutton "Одиночка":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.2
        ypos 0.1
        action [Hide("replays_common_choice_7dl", transition=Dissolve(0.2)), Hide("replays_un_choice_7dl", transition=Dissolve(0.2)), Hide("replays_sl_choice_7dl", transition=Dissolve(0.2)), Hide("replays_dv_choice_7dl", transition=Dissolve(0.2)), Hide("replays_mi_choice_7dl", transition=Dissolve(0.2)), Hide("replays_route_choice_7dl", transition=Dissolve(0.2)), Show("replays_neutral_7dl", transition=Dissolve(0.2))]
    
    textbutton "Лена":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.2
        ypos 0.15
        action [Hide("replays_common_choice_7dl", transition=Dissolve(0.2)), Hide("replays_un_choice_7dl", transition=Dissolve(0.2)), Hide("replays_sl_choice_7dl", transition=Dissolve(0.2)), Hide("replays_dv_choice_7dl", transition=Dissolve(0.2)), Hide("replays_mi_choice_7dl", transition=Dissolve(0.2)), Show("replays_un_choice_7dl", transition=Dissolve(0.2))]
    
    textbutton "Славя":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.2
        ypos 0.2
        action [Hide("replays_common_choice_7dl", transition=Dissolve(0.2)), Hide("replays_un_choice_7dl", transition=Dissolve(0.2)), Hide("replays_sl_choice_7dl", transition=Dissolve(0.2)), Hide("replays_dv_choice_7dl", transition=Dissolve(0.2)), Hide("replays_mi_choice_7dl", transition=Dissolve(0.2)), Show("replays_sl_choice_7dl", transition=Dissolve(0.2))]
    
    textbutton "Алиса":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.2
        ypos 0.25
        action [Hide("replays_common_choice_7dl", transition=Dissolve(0.2)), Hide("replays_un_choice_7dl", transition=Dissolve(0.2)), Hide("replays_sl_choice_7dl", transition=Dissolve(0.2)), Hide("replays_dv_choice_7dl", transition=Dissolve(0.2)), Hide("replays_mi_choice_7dl", transition=Dissolve(0.2)), Show("replays_dv_choice_7dl", transition=Dissolve(0.2))]
    
    textbutton "Мику":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.2
        ypos 0.3
        action [Hide("replays_common_choice_7dl", transition=Dissolve(0.2)), Hide("replays_un_choice_7dl", transition=Dissolve(0.2)), Hide("replays_sl_choice_7dl", transition=Dissolve(0.2)), Hide("replays_dv_choice_7dl", transition=Dissolve(0.2)), Hide("replays_mi_choice_7dl", transition=Dissolve(0.2)), Show("replays_mi_choice_7dl", transition=Dissolve(0.2))]
    
    textbutton "Ульяна":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.2
        ypos 0.35
        action [Hide("replays_common_choice_7dl", transition=Dissolve(0.2)), Hide("replays_un_choice_7dl", transition=Dissolve(0.2)), Hide("replays_sl_choice_7dl", transition=Dissolve(0.2)), Hide("replays_dv_choice_7dl", transition=Dissolve(0.2)), Hide("replays_mi_choice_7dl", transition=Dissolve(0.2)), Hide("replays_route_choice_7dl", transition=Dissolve(0.2)), Show("replays_us_7dl", transition=Dissolve(0.2))]
    
    textbutton "Ольга":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.2
        ypos 0.4
        action [Hide("replays_common_choice_7dl", transition=Dissolve(0.2)), Hide("replays_un_choice_7dl", transition=Dissolve(0.2)), Hide("replays_sl_choice_7dl", transition=Dissolve(0.2)), Hide("replays_dv_choice_7dl", transition=Dissolve(0.2)), Hide("replays_mi_choice_7dl", transition=Dissolve(0.2)), Hide("replays_route_choice_7dl", transition=Dissolve(0.2)), Show("replays_mt_7dl", transition=Dissolve(0.2))]
    
screen replays_common_choice_7dl:
    textbutton "Пролог":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.6
        ypos 0.05
        action [Hide("replays_route_choice_7dl", transition=Dissolve(0.2)), Hide("replays_common_choice_7dl", transition=Dissolve(0.2)), Show("replays_common_d0_7dl", transition=Dissolve(0.2))]

    textbutton "День 1":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.6
        ypos 0.1
        action [Hide("replays_route_choice_7dl", transition=Dissolve(0.2)), Hide("replays_common_choice_7dl", transition=Dissolve(0.2)), Show("replays_common_d1_7dl", transition=Dissolve(0.2))]

    textbutton "День 1 альтернативный":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.6
        ypos 0.15
        action [Hide("replays_route_choice_7dl", transition=Dissolve(0.2)), Hide("replays_common_choice_7dl", transition=Dissolve(0.2)), Show("replays_common_d1alt_7dl", transition=Dissolve(0.2))]

    textbutton "День 2":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.6
        ypos 0.2
        action [Hide("replays_route_choice_7dl", transition=Dissolve(0.2)), Hide("replays_common_choice_7dl", transition=Dissolve(0.2)), Show("replays_common_d2_7dl", transition=Dissolve(0.2))]

    textbutton "День 3":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.6
        ypos 0.25
        action [Hide("replays_route_choice_7dl", transition=Dissolve(0.2)), Hide("replays_common_choice_7dl", transition=Dissolve(0.2)), Show("replays_common_d3_7dl", transition=Dissolve(0.2))]

screen replays_common_d0_7dl:
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.2
        ypos 0.05
        action [Hide("replays_common_d0_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]

    if renpy.seen_label("alt_day0_start_l"):
        textbutton "Локи":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.2
            ypos 0.1
            action Replay("alt_day0_start_l", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text"
            xpos 0.2
            ypos 0.1
            
    if renpy.seen_label("alt_day0_start_h"):
        textbutton "Герк":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.2
            ypos 0.15
            action Replay("alt_day0_start_h", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text"
            xpos 0.2
            ypos 0.15
            
    if renpy.seen_label("alt_day0_start_d"):
        textbutton "Дрищ":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.2
            ypos 0.2
            action Replay("alt_day0_start_d", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text"
            xpos 0.2
            ypos 0.2
            
screen replays_common_d1_7dl:
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.2
        ypos 0.05
        action [Hide("replays_common_d1_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]
    if renpy.seen_label("alt_day1_begin"):
        textbutton "Начало":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.2
            ypos 0.1
            action Replay("alt_day1_begin", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text"
            xpos 0.2
            ypos 0.1

screen replays_common_d1alt_7dl:
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.2
        ypos 0.05
        action [Hide("replays_common_d1alt_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]

    if renpy.seen_label("alt_day1_alt_M"):
        textbutton "Начало":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.2
            ypos 0.1
            action Replay("alt_day1_alt_M", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text"
            xpos 0.2
            ypos 0.1
            
screen replays_common_d2_7dl:
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.2
        ypos 0.05
        action [Hide("replays_common_d2_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]

    if renpy.seen_label("alt_day2_begin"):
        textbutton "Начало":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.2
            ypos 0.1
            action Replay("alt_day2_begin", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text"
            xpos 0.2
            ypos 0.1

screen replays_common_d3_7dl:
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.2
        ypos 0.05
        action [Hide("replays_common_d3_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]

    if renpy.seen_label("alt_day3_begin"):
        textbutton "Начало":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.2
            ypos 0.1
            action Replay("alt_day3_begin", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text"
            xpos 0.2
            ypos 0.1

screen replays_neutral_7dl:
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.2
        ypos 0.05
        action [Hide("replays_neutral_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]

    if renpy.seen_label("alt_day4_neu_home"):
        textbutton "Начало":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.2
            ypos 0.1
            action Replay("alt_day4_neu_home", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text"
            xpos 0.2
            ypos 0.1
            
screen replays_un_choice_7dl:
    textbutton "7дл":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.6
        ypos 0.05
        action [Hide("replays_route_choice_7dl", transition=Dissolve(0.2)), Hide("replays_un_choice_7dl", transition=Dissolve(0.2)), Show("replays_un_7dl_7dl", transition=Dissolve(0.2))]

    text "Классик":
        style "replays_text"
        xpos 0.6
        ypos 0.1

    textbutton "Френдзона":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.6
        ypos 0.15
        action [Hide("replays_route_choice_7dl", transition=Dissolve(0.2)), Hide("replays_un_choice_7dl", transition=Dissolve(0.2)), Show("replays_un_fz_7dl", transition=Dissolve(0.2))]

screen replays_un_7dl_7dl:
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.2
        ypos 0.05
        action [Hide("replays_un_7dl_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]

    if renpy.seen_label("alt_day4_un_7dl_begin"):
        textbutton "Начало":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.2
            ypos 0.1
            action Replay("alt_day4_un_7dl_begin", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text"
            xpos 0.2
            ypos 0.1

screen replays_un_fz_7dl:
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.2
        ypos 0.05
        action [Hide("replays_un_fz_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]

    if renpy.seen_label("alt_day4_un_fz_begin"):
        textbutton "Начало":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.2
            ypos 0.1
            action Replay("alt_day4_un_fz_begin", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text"
            xpos 0.2
            ypos 0.1

screen replays_sl_choice_7dl:
    textbutton "7дл":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.6
        ypos 0.05
        action [Hide("replays_route_choice_7dl", transition=Dissolve(0.2)), Hide("replays_sl_choice_7dl", transition=Dissolve(0.2)), Show("replays_sl_7dl_7dl", transition=Dissolve(0.2))]

    textbutton "Классик":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.6
        ypos 0.15
        action [Hide("replays_route_choice_7dl", transition=Dissolve(0.2)), Hide("replays_sl_choice_7dl", transition=Dissolve(0.2)), Show("replays_sl_cl_7dl", transition=Dissolve(0.2))]
      
    text "Ведьма":
        style "replays_text"
        xpos 0.6
        ypos 0.1
      
screen replays_sl_7dl_7dl:
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.2
        ypos 0.05
        action [Hide("replays_sl_7dl_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]

    if renpy.seen_label("alt_day4_sl_7dl_begin"):
        textbutton "Начало":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.2
            ypos 0.1
            action Replay("alt_day4_sl_7dl_begin", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text"
            xpos 0.2
            ypos 0.1

screen replays_sl_cl_7dl:
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.2
        ypos 0.05
        action [Hide("replays_sl_cl_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]

    if renpy.seen_label("alt_day4_sl_cl_begin"):
        textbutton "Начало":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.2
            ypos 0.1
            action Replay("alt_day4_sl_cl_begin", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text"
            xpos 0.2
            ypos 0.1

screen replays_dv_choice_7dl:
    textbutton "7дл":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.6
        ypos 0.05
        action [Hide("replays_route_choice_7dl", transition=Dissolve(0.2)), Hide("replays_dv_choice_7dl", transition=Dissolve(0.2)), Show("replays_dv_7dl_7dl", transition=Dissolve(0.2))]

    text "Классик":
        style "replays_text"
        xpos 0.6
        ypos 0.1
      
    text "Диджей":
        style "replays_text"
        xpos 0.6
        ypos 0.15
      
screen replays_dv_7dl_7dl:
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.2
        ypos 0.05
        action [Hide("replays_dv_7dl_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]

    if renpy.seen_label("alt_day4_dv_7dl_begin"):
        textbutton "Начало":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.2
            ypos 0.1
            action Replay("alt_day4_dv_7dl_begin", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text"
            xpos 0.2
            ypos 0.1
            
screen replays_mi_choice_7dl:
    textbutton "7дл":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.6
        ypos 0.05
        action [Hide("replays_route_choice_7dl", transition=Dissolve(0.2)), Hide("replays_mi_choice_7dl", transition=Dissolve(0.2)), Show("replays_mi_7dl_7dl", transition=Dissolve(0.2))]

    text "Классик":
        style "replays_text"
        xpos 0.6
        ypos 0.1
  
    textbutton "Диджей":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.6
        ypos 0.15
        action [Hide("replays_route_choice_7dl", transition=Dissolve(0.2)), Hide("replays_mi_choice_7dl", transition=Dissolve(0.2)), Show("replays_mi_dj_7dl", transition=Dissolve(0.2))]
  
screen replays_mi_7dl_7dl:
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.2
        ypos 0.05
        action [Hide("replays_mi_7dl_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]

    if renpy.seen_label("alt_day4_mi_7dl_begin"):
        textbutton "Начало":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.2
            ypos 0.1
            action Replay("alt_day4_mi_7dl_begin", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text"
            xpos 0.2
            ypos 0.1

screen replays_mi_dj_7dl:
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.2
        ypos 0.05
        action [Hide("replays_mi_dj_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]

    if renpy.seen_label("alt_day4_mi_dj_begin"):
        textbutton "Начало":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.2
            ypos 0.1
            action Replay("alt_day4_mi_dj_begin", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text"
            xpos 0.2
            ypos 0.1
            
screen replays_us_7dl:
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.2
        ypos 0.05
        action [Hide("replays_us_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]

    if renpy.seen_label("alt_day6_us_px_begin"):
        textbutton "Начало":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.2
            ypos 0.1
            action Replay("alt_day6_us_px_begin", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text"
            xpos 0.2
            ypos 0.1
            
screen replays_mt_7dl:
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.2
        ypos 0.05
        action [Hide("replays_mt_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]

    if renpy.seen_label("alt_day6_mt_7dl_begin"):
        textbutton "Начало":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.2
            ypos 0.1
            action Replay("alt_day6_mt_7dl_begin", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text"
            xpos 0.2
            ypos 0.1
