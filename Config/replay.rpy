init:
    $ mods["alt_gallery_start"] = u"Галерея 7дл"
    $ mod_tags["alt_gallery_start"] = ["length:days","gameplay:vn","protagonist:male"]

init 9999 python:
    cursive_font = default_7dl_path + "Pics/fonts/olgactt.ttf"

    style.replays_textbutton = Style(style.base_font)
    style.replays_textbutton.font  = cursive_font
    style.replays_textbutton.size = 42
    #style.replays_textbutton.kerning = 3
    style.replays_textbutton.color = "#7847f3"
    style.replays_textbutton.hover_color = "#2f059a"
    style.replays_textbutton.selected_color = "#7847f3"
    style.replays_textbutton.selected_idle_color = "#7847f3"
    style.replays_textbutton.selected_hover_color = "#2f059a"
    style.replays_textbutton.insensitive_color = "#7847f3"

    style.replays_text_locked = Style(style.base_font)
    style.replays_text_locked.font  = cursive_font
    style.replays_text_locked.size = 42
    #style.replays_text_locked.kerning = 3
    style.replays_text_locked.color = "#808080"

    style.replays_text = Style(style.base_font)
    style.replays_text.font  = cursive_font
    style.replays_text.size = 42
    #style.replays_text.kerning = 3
    style.replays_text.color = "#7847f3"
    
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
    tag menu
    textbutton "Основной рут":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.235 #xpos 0.235
        ypos 0.187 #ypos 0.187
        action [Hide("replays_common_choice_7dl", transition=Dissolve(0.2)), Hide("replays_un_choice_7dl", transition=Dissolve(0.2)), Hide("replays_sl_choice_7dl", transition=Dissolve(0.2)), Hide("replays_dv_choice_7dl", transition=Dissolve(0.2)), Hide("replays_mi_choice_7dl", transition=Dissolve(0.2)), Show("replays_common_choice_7dl", transition=Dissolve(0.2))]
    textbutton "Одиночка":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.235 #xpos 0.235
        ypos 0.236 #ypos 0.236
        action [Hide("replays_common_choice_7dl", transition=Dissolve(0.2)), Hide("replays_un_choice_7dl", transition=Dissolve(0.2)), Hide("replays_sl_choice_7dl", transition=Dissolve(0.2)), Hide("replays_dv_choice_7dl", transition=Dissolve(0.2)), Hide("replays_mi_choice_7dl", transition=Dissolve(0.2)), Hide("replays_route_choice_7dl", transition=Dissolve(0.2)), Show("replays_neutral_7dl", transition=Dissolve(0.2))]
    textbutton "Лена":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.235
        ypos 0.285
        action [Hide("replays_common_choice_7dl", transition=Dissolve(0.2)), Hide("replays_un_choice_7dl", transition=Dissolve(0.2)), Hide("replays_sl_choice_7dl", transition=Dissolve(0.2)), Hide("replays_dv_choice_7dl", transition=Dissolve(0.2)), Hide("replays_mi_choice_7dl", transition=Dissolve(0.2)), Show("replays_un_choice_7dl", transition=Dissolve(0.2))]
    textbutton "Славя":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.235
        ypos 0.333
        action [Hide("replays_common_choice_7dl", transition=Dissolve(0.2)), Hide("replays_un_choice_7dl", transition=Dissolve(0.2)), Hide("replays_sl_choice_7dl", transition=Dissolve(0.2)), Hide("replays_dv_choice_7dl", transition=Dissolve(0.2)), Hide("replays_mi_choice_7dl", transition=Dissolve(0.2)), Show("replays_sl_choice_7dl", transition=Dissolve(0.2))]
    textbutton "Алиса":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.235
        ypos 0.382
        action [Hide("replays_common_choice_7dl", transition=Dissolve(0.2)), Hide("replays_un_choice_7dl", transition=Dissolve(0.2)), Hide("replays_sl_choice_7dl", transition=Dissolve(0.2)), Hide("replays_dv_choice_7dl", transition=Dissolve(0.2)), Hide("replays_mi_choice_7dl", transition=Dissolve(0.2)), Show("replays_dv_choice_7dl", transition=Dissolve(0.2))]
    textbutton "Мику":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.235
        ypos 0.431
        action [Hide("replays_common_choice_7dl", transition=Dissolve(0.2)), Hide("replays_un_choice_7dl", transition=Dissolve(0.2)), Hide("replays_sl_choice_7dl", transition=Dissolve(0.2)), Hide("replays_dv_choice_7dl", transition=Dissolve(0.2)), Hide("replays_mi_choice_7dl", transition=Dissolve(0.2)), Show("replays_mi_choice_7dl", transition=Dissolve(0.2))]
    textbutton "Ульяна":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.235
        ypos 0.479
        action [Hide("replays_common_choice_7dl", transition=Dissolve(0.2)), Hide("replays_un_choice_7dl", transition=Dissolve(0.2)), Hide("replays_sl_choice_7dl", transition=Dissolve(0.2)), Hide("replays_dv_choice_7dl", transition=Dissolve(0.2)), Hide("replays_mi_choice_7dl", transition=Dissolve(0.2)), Hide("replays_route_choice_7dl", transition=Dissolve(0.2)), Show("replays_us_7dl", transition=Dissolve(0.2))]
    textbutton "Ольга":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.235
        ypos 0.528
        action [Hide("replays_common_choice_7dl", transition=Dissolve(0.2)), Hide("replays_un_choice_7dl", transition=Dissolve(0.2)), Hide("replays_sl_choice_7dl", transition=Dissolve(0.2)), Hide("replays_dv_choice_7dl", transition=Dissolve(0.2)), Hide("replays_mi_choice_7dl", transition=Dissolve(0.2)), Hide("replays_route_choice_7dl", transition=Dissolve(0.2)), Show("replays_mt_7dl", transition=Dissolve(0.2))]

screen replays_common_choice_7dl:
    textbutton "Пролог":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.544
        ypos 0.187
        action [Hide("replays_route_choice_7dl", transition=Dissolve(0.2)), Hide("replays_common_choice_7dl", transition=Dissolve(0.2)), Show("replays_common_d0_7dl", transition=Dissolve(0.2))]
    textbutton "День 1":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.544
        ypos 0.236
        action [Hide("replays_route_choice_7dl", transition=Dissolve(0.2)), Hide("replays_common_choice_7dl", transition=Dissolve(0.2)), Show("replays_common_d1_7dl", transition=Dissolve(0.2))]
    textbutton "День 1 альтернативный":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.544
        ypos 0.285
        action [Hide("replays_route_choice_7dl", transition=Dissolve(0.2)), Hide("replays_common_choice_7dl", transition=Dissolve(0.2)), Show("replays_common_d1alt_7dl", transition=Dissolve(0.2))]
    textbutton "День 2":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.544
        ypos 0.333
        action [Hide("replays_route_choice_7dl", transition=Dissolve(0.2)), Hide("replays_common_choice_7dl", transition=Dissolve(0.2)), Show("replays_common_d2_1_7dl", transition=Dissolve(0.2))]
    textbutton "День 3":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.544
        ypos 0.382
        action [Hide("replays_route_choice_7dl", transition=Dissolve(0.2)), Hide("replays_common_choice_7dl", transition=Dissolve(0.2)), Show("replays_common_d3_1_7dl", transition=Dissolve(0.2))]

screen replays_common_d0_7dl:
    tag menu
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.235
        ypos 0.187
        action [Hide("replays_common_d0_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]
    if renpy.seen_label("alt_day0_start_l"):
        textbutton "Локи":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day0_start_l", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day0_start_h"):
        textbutton "Герк":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day0_start_h", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day0_start_d"):
        textbutton "Дрищ":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day0_start_d", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333

screen replays_common_d1_7dl:
    tag menu
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.235
        ypos 0.187
        action [Hide("replays_common_d1_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]
    if renpy.seen_label("alt_day1_begin"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day1_begin", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day1_bus_start"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day1_bus_start", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day1_firts_met"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day1_firts_met", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
    if renpy.seen_label("alt_day1_arrival"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.382
            action Replay("alt_day1_arrival", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.382
    if renpy.seen_label("alt_day1_chase1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.431
            action Replay("alt_day1_chase1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.431
    if renpy.seen_label("alt_day1_dock"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.479
            action Replay("alt_day1_dock", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.479
    if renpy.seen_label("alt_day1_mod_tan"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.528
            action Replay("alt_day1_mod_tan", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.528
    if renpy.seen_label("alt_day1_elektron"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.577
            action Replay("alt_day1_elektron", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.577
    if renpy.seen_label("alt_day1_meeting"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.625
            action Replay("alt_day1_meeting", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.625
    if renpy.seen_label("alt_day1_soccer_d1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.674
            action Replay("alt_day1_soccer_d1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.674
    if renpy.seen_label("alt_day1_supper"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.723
            action Replay("alt_day1_supper", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.723
    if renpy.seen_label("alt_day1_dining_room"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.771
            action Replay("alt_day1_dining_room", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.771
    if renpy.seen_label("alt_day1_chase"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.187
            action Replay("alt_day1_chase", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.187
    if renpy.seen_label("alt_day1_headshot"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.236
            action Replay("alt_day1_headshot", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.236
    if renpy.seen_label("alt_day1_nocatch"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.285
            action Replay("alt_day1_nocatch", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.285
    if renpy.seen_label("alt_day1_slavya_saviour"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.333
            action Replay("alt_day1_slavya_saviour", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.333
    if renpy.seen_label("alt_day1_lena"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.382
            action Replay("alt_day1_lena", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.382
    if renpy.seen_label("alt_day1_un_stay"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.431
            action Replay("alt_day1_un_stay", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.431
    if renpy.seen_label("alt_day1_sleep"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.479
            action Replay("alt_day1_sleep", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.479

screen replays_common_d1alt_7dl:
    tag menu
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.235
        ypos 0.187
        action [Hide("replays_common_d1alt_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]
    if renpy.seen_label("alt_day1_begin"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day1_begin", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day1_alt_M"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day1_alt_M", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day1_alt_A"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day1_alt_A", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
    if renpy.seen_label("alt_day1_alt_S"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.382
            action Replay("alt_day1_alt_S", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.382
    if renpy.seen_label("alt_day1_alt_L"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.431
            action Replay("alt_day1_alt_L", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.431
    if renpy.seen_label("alt_day1_alt_O"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.479
            action Replay("alt_day1_alt_O", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.479
    if renpy.seen_label("alt_day1_alt_supper"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.528
            action Replay("alt_day1_alt_supper", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.528
    if renpy.seen_label("alt_day1_alt_U"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.577
            action Replay("alt_day1_alt_U", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.577
    if renpy.seen_label("alt_day1_alt_U_reject"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.625
            action Replay("alt_day1_alt_U_reject", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.625
    if renpy.seen_label("alt_day1_alt_ev_A_S"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.674
            action Replay("alt_day1_alt_ev_A_S", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.674
    if renpy.seen_label("alt_day1_lena"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.723
            action Replay("alt_day1_lena", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.723
    if renpy.seen_label("alt_day1_un_stay"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.771
            action Replay("alt_day1_un_stay", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.771
    if renpy.seen_label("alt_day1_sleep"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.187
            action Replay("alt_day1_sleep", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.187

screen replays_common_d2_1_7dl:
    tag menu
    text "Часть 1":
        style "replays_text"
        xcenter 0.432
        ycenter 0.885
    text "Часть 2":
        style "replays_text"
        xcenter 0.741
        ycenter 0.883
    imagebutton:
        auto get_image_7dl("gui/gallery/gallery_right_arrow_%s.png") xcenter 0.749 ycenter 0.923 
        action Show("replays_common_d2_2_7dl", transition=Dissolve(0.2))
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.235
        ypos 0.187
        action [Hide("replays_common_d2_1_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]
    if renpy.seen_label("alt_day2_begin"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day2_begin", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day2_lineup"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day2_lineup", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day2_bf"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day2_bf", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
    if renpy.seen_label("alt_day2_guide"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.382
            action Replay("alt_day2_guide", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.382
    if renpy.seen_label("alt_day2_sl_guide"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.431
            action Replay("alt_day2_sl_guide", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.431
    if renpy.seen_label("alt_day2_sl_hyst"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.479
            action Replay("alt_day2_sl_hyst", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.479
    if renpy.seen_label("alt_day2_event_music_club1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.528
            action Replay("alt_day2_event_music_club1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.528
    if renpy.seen_label("alt_day2_inmusic"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.577
            action Replay("alt_day2_inmusic", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.577
    if renpy.seen_label("alt_day2_event_clubs1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.625
            action Replay("alt_day2_event_clubs1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.625
    if renpy.seen_label("alt_day2_event_camp_entrance1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.674
            action Replay("alt_day2_event_camp_entrance1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.674
    if renpy.seen_label("alt_day2_event_dv_us_house1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.723
            action Replay("alt_day2_event_dv_us_house1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.723
    if renpy.seen_label("alt_day2_event_dining_hall1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.771
            action Replay("alt_day2_event_dining_hall1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.771
    if renpy.seen_label("alt_day2_event_sport_area1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.187
            action Replay("alt_day2_event_sport_area1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.187
    if renpy.seen_label("alt_day2_event_beach1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.236
            action Replay("alt_day2_event_beach1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.236
    if renpy.seen_label("alt_day2_event_me_mt_house1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.285
            action Replay("alt_day2_event_me_mt_house1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.285
    if renpy.seen_label("alt_day2_event_library1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.333
            action Replay("alt_day2_event_library1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.333
    if renpy.seen_label("alt_day2_mz"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.382
            action Replay("alt_day2_mz", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.382
    if renpy.seen_label("alt_day2_event_medic_house1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.431
            action Replay("alt_day2_event_medic_house1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.431
    if renpy.seen_label("alt_day2_event_square_dunno"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.479
            action Replay("alt_day2_event_square_dunno", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.479
    if renpy.seen_label("alt_day2_event_square_1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.528
            action Replay("alt_day2_event_square_1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.528
    if renpy.seen_label("alt_day2_event_boat_station1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.577
            action Replay("alt_day2_event_boat_station1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.577
    if renpy.seen_label("alt_day2_convoy"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.625
            action Replay("alt_day2_convoy", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.625

screen replays_common_d2_2_7dl:
    tag menu
    text "Часть 3":
        style "replays_text"
        xcenter 0.432
        ycenter 0.885
    text "Часть 4":
        style "replays_text"
        xcenter 0.741
        ycenter 0.883
    imagebutton:
        auto get_image_7dl("gui/gallery/gallery_left_arrow_%s.png") xcenter 0.256 ycenter 0.923 
        action Show("replays_common_d2_1_7dl", transition=Dissolve(0.2))
    imagebutton:
        auto get_image_7dl("gui/gallery/gallery_right_arrow_%s.png") xcenter 0.749 ycenter 0.923 
        action Show("replays_common_d2_3_7dl", transition=Dissolve(0.2))
    if renpy.seen_label("alt_day2_event_estrade"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.187
            action Replay("alt_day2_event_estrade", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.187
    if renpy.seen_label("alt_day2_phone"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day2_phone", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day2_dubstep"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day2_dubstep", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day2_dubstep2"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day2_dubstep2", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
    if renpy.seen_label("alt_day2_dinner"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.382
            action Replay("alt_day2_dinner", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.382
    if renpy.seen_label("alt_day2_grand_escape"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.431
            action Replay("alt_day2_grand_escape", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.431
    if renpy.seen_label("alt_day2_siesta"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.479
            action Replay("alt_day2_siesta", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.479
    if renpy.seen_label("alt_day2_tournament"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.528
            action Replay("alt_day2_tournament", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.528
    if renpy.seen_label("alt_day2_walk_sl"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.577
            action Replay("alt_day2_walk_sl", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.577
    if renpy.seen_label("alt_day2_walk_alone"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.625
            action Replay("alt_day2_walk_alone", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.625
    if renpy.seen_label("alt_day2_ultim"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.674
            action Replay("alt_day2_ultim", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.674
    if renpy.seen_label("alt_day2_cards"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.723
            action Replay("alt_day2_cards", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.723
    if renpy.seen_label("alt_day2_tournament_prep"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.771
            action Replay("alt_day2_tournament_prep", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.771
    if renpy.seen_label("alt_day2_supper"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.187
            action Replay("alt_day2_supper", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.187
    if renpy.seen_label("alt_day2_slot_us_try"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.236
            action Replay("alt_day2_slot_us_try", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.236
    if renpy.seen_label("alt_day2_slot_us"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.285
            action Replay("alt_day2_slot_us", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.285
    if renpy.seen_label("alt_day2_sup2"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.333
            action Replay("alt_day2_sup2", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.333
    if renpy.seen_label("alt_day2_slot_sl"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.382
            action Replay("alt_day2_slot_sl", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.382
    if renpy.seen_label("alt_day2_eventEv_beach1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.431
            action Replay("alt_day2_eventEv_beach1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.431
    if renpy.seen_label("alt_day2_slot_dv"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.479
            action Replay("alt_day2_slot_dv", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.479

screen replays_common_d2_3_7dl:
    tag menu
    if renpy.seen_label("alt_day2_eventEv_music_club1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.187
            action Replay("alt_day2_eventEv_music_club1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.187
    if renpy.seen_label("alt_day2_slot_mi"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day2_slot_mi", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day2_eventEv_clubs1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day2_eventEv_clubs1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day2_eventEv_camp_entrance1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day2_eventEv_camp_entrance1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
    if renpy.seen_label("alt_day2_eventEv_un_mi_house1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.382
            action Replay("alt_day2_eventEv_un_mi_house1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.382
    if renpy.seen_label("alt_day2_un_loki_date"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.431
            action Replay("alt_day2_un_loki_date", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.431
    if renpy.seen_label("alt_day2_un_herc_date"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.479
            action Replay("alt_day2_un_herc_date", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.479
    if renpy.seen_label("alt_day2_eventEv_dv_us_house1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.528
            action Replay("alt_day2_eventEv_dv_us_house1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.528
    if renpy.seen_label("alt_day2_eventEv_dining_hall1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.577
            action Replay("alt_day2_eventEv_dining_hall1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.577
    if renpy.seen_label("alt_day2_eventEv_sport_area1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.625
            action Replay("alt_day2_eventEv_sport_area1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.625
    if renpy.seen_label("alt_day2_slot_un"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.674
            action Replay("alt_day2_slot_un", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.674
    if renpy.seen_label("alt_day2_eventEv_me_mt_house1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.723
            action Replay("alt_day2_eventEv_me_mt_house1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.723
    if renpy.seen_label("alt_day2_eventEv_library1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.771
            action Replay("alt_day2_eventEv_library1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.771
    if renpy.seen_label("alt_day2_eventEv_medic_house1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.187
            action Replay("alt_day2_eventEv_medic_house1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.187
    if renpy.seen_label("alt_day2_eventEv_estrade1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.236
            action Replay("alt_day2_eventEv_estrade1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.236
    if renpy.seen_label("alt_day2_eventEv_square1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.285
            action Replay("alt_day2_eventEv_square1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.285
    if renpy.seen_label("alt_day2_eventEv_boat_station1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.333
            action Replay("alt_day2_eventEv_boat_station1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.333
    if renpy.seen_label("alt_day2_dream"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.382
            action Replay("alt_day2_dream", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.382

screen replays_common_d3_1_7dl:
    tag menu
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.235
        ypos 0.187
        action [Hide("replays_common_d3_1_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]
    if renpy.seen_label("alt_day3_begin"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day3_begin", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day3_bf"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day3_bf", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day3_event_library1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day3_event_library1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
    if renpy.seen_label("alt_day3_event_estrade"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.382
            action Replay("alt_day3_event_estrade", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.382
    if renpy.seen_label("alt_day3_event_music_club"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.431
            action Replay("alt_day3_event_music_club", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.431
    if renpy.seen_label("alt_day3_bf_duty"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.479
            action Replay("alt_day3_bf_duty", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.479
    if renpy.seen_label("alt_day3_event_camp_entrance"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.528
            action Replay("alt_day3_event_camp_entrance", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.528
    if renpy.seen_label("alt_day3_event_music_club1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.577
            action Replay("alt_day3_event_music_club1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.577
    if renpy.seen_label("alt_day3_event_clubs1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.625
            action Replay("alt_day3_event_clubs1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.625
    if renpy.seen_label("alt_day3_event_camp_entrance1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.674
            action Replay("alt_day3_event_camp_entrance1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.674
    if renpy.seen_label("alt_day3_event_dining_hall1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.723
            action Replay("alt_day3_event_dining_hall1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.723
    if renpy.seen_label("alt_day3_event_sport_area1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.771
            action Replay("alt_day3_event_sport_area1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.771
    if renpy.seen_label("alt_day3_event_beach1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.187
            action Replay("alt_day3_event_beach1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.187
    if renpy.seen_label("alt_day3_event_medic_house1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.236
            action Replay("alt_day3_event_medic_house1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.236
    if renpy.seen_label("alt_day3_event_estrade1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.285
            action Replay("alt_day3_event_estrade1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.285
    if renpy.seen_label("alt_day3_event_square1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.333
            action Replay("alt_day3_event_square1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.333
    if renpy.seen_label("alt_day3_event_boat_station1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.382
            action Replay("alt_day3_event_boat_station1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.382
    if renpy.seen_label("alt_day3_dinner"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.431
            action Replay("alt_day3_dinner", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.431
    if renpy.seen_label("alt_day3_dinner_menu"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.479
            action Replay("alt_day3_dinner_menu", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.479

screen replays_common_d3_2_7dl:
    tag menu
    if renpy.seen_label("alt_day3_eventAf_music_club1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.187
            action Replay("alt_day3_eventAf_music_club1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.187
    if renpy.seen_label("alt_day3_eventAf_library1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day3_eventAf_library1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day3_eventAf_clubs_ladder"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day3_eventAf_clubs_ladder", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day3_eventAf_clubs_technoquest"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day3_eventAf_clubs_technoquest", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
    if renpy.seen_label("alt_day3_eventAf_un_mi_house1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.382
            action Replay("alt_day3_eventAf_un_mi_house1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.382
    if renpy.seen_label("alt_day3_eventAf_dining_hall1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.431
            action Replay("alt_day3_eventAf_dining_hall1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.431
    if renpy.seen_label("alt_day3_eventAf_admins1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.479
            action Replay("alt_day3_eventAf_admins1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.479
    if renpy.seen_label("alt_day3_sl_postlunch"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.528
            action Replay("alt_day3_sl_postlunch", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.528
    if renpy.seen_label("alt_day3_eventAf_me_mt_house1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.577
            action Replay("alt_day3_eventAf_me_mt_house1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.577
    if renpy.seen_label("alt_day3_eventAf_estrade1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.625
            action Replay("alt_day3_eventAf_estrade1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.625
    if renpy.seen_label("alt_day3_music"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.674
            action Replay("alt_day3_music", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.674
    if renpy.seen_label("alt_day3_aftermath"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.723
            action Replay("alt_day3_aftermath", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.723
    if renpy.seen_label("alt_day3_nightmare"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.771
            action Replay("alt_day3_nightmare", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.771
    if renpy.seen_label("alt_day3_supper1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.187
            action Replay("alt_day3_supper1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.187
    if renpy.seen_label("alt_day3_supper"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.236
            action Replay("alt_day3_supper", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.236
    if renpy.seen_label("alt_day3_supper2"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.285
            action Replay("alt_day3_supper2", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.285

screen replays_common_d3_3_7dl:
    tag menu
    if renpy.seen_label("alt_day3_dance_dance"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.187
            action Replay("alt_day3_dance_dance", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.187
    if renpy.seen_label("alt_day3_makeup"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day3_makeup", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day3_dv_lf"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day3_dv_lf", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day3_rockstar"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day3_rockstar", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
    if renpy.seen_label("alt_day3_dv_reunion"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.382
            action Replay("alt_day3_dv_reunion", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.382
    if renpy.seen_label("alt_day3_dv_stayhere1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.431
            action Replay("alt_day3_dv_stayhere1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.431
    if renpy.seen_label("alt_day3_bath_voyeur"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.479
            action Replay("alt_day3_bath_voyeur", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.479
    if renpy.seen_label("alt_day3_leave1"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.528
            action Replay("alt_day3_leave1", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.528
    if renpy.seen_label("alt_day3_choose"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.577
            action Replay("alt_day3_choose", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.577
    if renpy.seen_label("alt_day3_dance_dance2"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.625
            action Replay("alt_day3_dance_dance2", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.625
    if renpy.seen_label("alt_day3_med_un"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.674
            action Replay("alt_day3_med_un", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.674
    if renpy.seen_label("alt_day3_un_cards"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.723
            action Replay("alt_day3_un_cards", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.723
    if renpy.seen_label("alt_day3_un_strip_play"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.771
            action Replay("alt_day3_un_strip_play", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.771
    if renpy.seen_label("alt_day3_card_lose"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.187
            action Replay("alt_day3_card_lose", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.187
    if renpy.seen_label("alt_day3_card_won"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.236
            action Replay("alt_day3_card_won", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.236
    if renpy.seen_label("alt_day3_post_strip"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.285
            action Replay("alt_day3_post_strip", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.285
    if renpy.seen_label("alt_day3_mt_scare"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.333
            action Replay("alt_day3_mt_scare", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.333
    if renpy.seen_label("alt_day3_dance_dance2_menu"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.382
            action Replay("alt_day3_dance_dance2_menu", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.382
    if renpy.seen_label("alt_day3_technoquest3"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.431
            action Replay("alt_day3_technoquest3", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.431
    if renpy.seen_label("alt_day3_choose3"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.479
            action Replay("alt_day3_choose3", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.479
    if renpy.seen_label("alt_day3_mi_7dl_init"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.528
            action Replay("alt_day3_mi_7dl_init", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.528
    if renpy.seen_label("alt_day3_disco_past_d2"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.577
            action Replay("alt_day3_disco_past_d2", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.577
    if renpy.seen_label("alt_day3_sleeptime"):
        textbutton "Название":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.625
            action Replay("alt_day3_sleeptime", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.625

screen replays_neutral_7dl:
    tag menu
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.235
        ypos 0.187
        action [Hide("replays_neutral_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]
    if renpy.seen_label("alt_day4_neu_home"):
        textbutton "Начало":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day4_neu_home", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236

screen replays_un_choice_7dl:
    textbutton "7дл":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.544
        ypos 0.187
        action [Hide("replays_route_choice_7dl", transition=Dissolve(0.2)), Hide("replays_un_choice_7dl", transition=Dissolve(0.2)), Show("replays_un_7dl_7dl", transition=Dissolve(0.2))]

    text "Классик":
        style "replays_text_locked"
        xpos 0.544
        ypos 0.236
    textbutton "Френдзона":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.544
        ypos 0.285
        action [Hide("replays_route_choice_7dl", transition=Dissolve(0.2)), Hide("replays_un_choice_7dl", transition=Dissolve(0.2)), Show("replays_un_fz_7dl", transition=Dissolve(0.2))]

screen replays_un_7dl_7dl:
    tag menu
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.235
        ypos 0.187
        action [Hide("replays_un_7dl_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]
    if renpy.seen_label("alt_day4_un_7dl_begin"):
        textbutton "Начало":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day4_un_7dl_begin", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236

screen replays_un_fz_7dl:
    tag menu
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.235
        ypos 0.187
        action [Hide("replays_un_fz_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]
    if renpy.seen_label("alt_day4_un_fz_begin"):
        textbutton "Начало":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day4_un_fz_begin", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236

screen replays_sl_choice_7dl:
    textbutton "7дл":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.544
        ypos 0.187
        action [Hide("replays_route_choice_7dl", transition=Dissolve(0.2)), Hide("replays_sl_choice_7dl", transition=Dissolve(0.2)), Show("replays_sl_7dl_7dl", transition=Dissolve(0.2))]
    textbutton "Классик":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.544
        ypos 0.285
        action [Hide("replays_route_choice_7dl", transition=Dissolve(0.2)), Hide("replays_sl_choice_7dl", transition=Dissolve(0.2)), Show("replays_sl_cl_7dl", transition=Dissolve(0.2))]

    text "Ведьма":
        style "replays_text_locked"
        xpos 0.544
        ypos 0.236

screen replays_sl_7dl_7dl:
    tag menu
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.235
        ypos 0.187
        action [Hide("replays_sl_7dl_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]
    if renpy.seen_label("alt_day4_sl_7dl_begin"):
        textbutton "Начало":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day4_sl_7dl_begin", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236

screen replays_sl_cl_7dl:
    tag menu
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.235
        ypos 0.187
        action [Hide("replays_sl_cl_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]
    if renpy.seen_label("alt_day4_sl_cl_begin"):
        textbutton "Начало":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day4_sl_cl_begin", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236

screen replays_dv_choice_7dl:
    textbutton "7дл":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.544
        ypos 0.187
        action [Hide("replays_route_choice_7dl", transition=Dissolve(0.2)), Hide("replays_dv_choice_7dl", transition=Dissolve(0.2)), Show("replays_dv_7dl_7dl", transition=Dissolve(0.2))]

    text "Классик":
        style "replays_text_locked"
        xpos 0.544
        ypos 0.236

    text "Диджей":
        style "replays_text_locked"
        xpos 0.544
        ypos 0.285

screen replays_dv_7dl_7dl:
    tag menu
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.235
        ypos 0.187
        action [Hide("replays_dv_7dl_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]
    if renpy.seen_label("alt_day4_dv_7dl_begin"):
        textbutton "Начало":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day4_dv_7dl_begin", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236

screen replays_mi_choice_7dl:
    textbutton "7дл":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.544
        ypos 0.187
        action [Hide("replays_route_choice_7dl", transition=Dissolve(0.2)), Hide("replays_mi_choice_7dl", transition=Dissolve(0.2)), Show("replays_mi_7dl_7dl", transition=Dissolve(0.2))]

    text "Классик":
        style "replays_text_locked"
        xpos 0.544
        ypos 0.236
    textbutton "Диджей":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.544
        ypos 0.285
        action [Hide("replays_route_choice_7dl", transition=Dissolve(0.2)), Hide("replays_mi_choice_7dl", transition=Dissolve(0.2)), Show("replays_mi_dj_7dl", transition=Dissolve(0.2))]

screen replays_mi_7dl_7dl:
    tag menu
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.235
        ypos 0.187
        action [Hide("replays_mi_7dl_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]
    if renpy.seen_label("alt_day4_mi_7dl_begin"):
        textbutton "Начало":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day4_mi_7dl_begin", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236

screen replays_mi_dj_7dl:
    tag menu
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.235
        ypos 0.187
        action [Hide("replays_mi_dj_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]
    if renpy.seen_label("alt_day4_mi_dj_begin"):
        textbutton "Начало":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day4_mi_dj_begin", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236

screen replays_us_7dl:
    tag menu
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.235
        ypos 0.187
        action [Hide("replays_us_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]
    if renpy.seen_label("alt_day6_us_px_begin"):
        textbutton "Начало":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day6_us_px_begin", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236

screen replays_mt_7dl:
    tag menu
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.235
        ypos 0.187
        action [Hide("replays_mt_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]
    if renpy.seen_label("alt_day6_mt_7dl_begin"):
        textbutton "Начало":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day6_mt_7dl_begin", scope={}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
