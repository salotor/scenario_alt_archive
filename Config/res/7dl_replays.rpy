init 999 python:
    olgactt_font = default_7dl_path + "Pics/fonts/olgactt.ttf"

    style.replays_textbutton = Style(style.base_font)
    style.replays_textbutton.font  = olgactt_font
    style.replays_textbutton.size = 42
    style.replays_textbutton.color = "#7847f3"
    style.replays_textbutton.hover_color = "#2f059a"
    style.replays_textbutton.selected_color = "#7847f3"
    style.replays_textbutton.selected_idle_color = "#7847f3"
    style.replays_textbutton.selected_hover_color = "#2f059a"
    style.replays_textbutton.insensitive_color = "#7847f3"

    style.replays_text = Style(style.base_font)
    style.replays_text.font  = olgactt_font
    style.replays_text.size = 42
    style.replays_text.color = "#7847f3"

    style.replays_text_locked = Style(style.base_font)
    style.replays_text_locked.font  = olgactt_font
    style.replays_text_locked.size = 42
    style.replays_text_locked.color = "#808080"
    
init 99:
    $ make_names_known_7dl()

screen replays_route_choice_7dl:
    tag menu
    textbutton "Основной рут":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.235
        ypos 0.187
        action [Hide("replays_common_choice_7dl", transition=Dissolve(0.2)), Hide("replays_un_choice_7dl", transition=Dissolve(0.2)), Hide("replays_sl_choice_7dl", transition=Dissolve(0.2)), Hide("replays_dv_choice_7dl", transition=Dissolve(0.2)), Hide("replays_mi_choice_7dl", transition=Dissolve(0.2)), Show("replays_common_choice_7dl", transition=Dissolve(0.2))]
    textbutton "Одиночка":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.235
        ypos 0.236
        action [Hide("replays_common_choice_7dl", transition=Dissolve(0.2)), Hide("replays_un_choice_7dl", transition=Dissolve(0.2)), Hide("replays_sl_choice_7dl", transition=Dissolve(0.2)), Hide("replays_dv_choice_7dl", transition=Dissolve(0.2)), Hide("replays_mi_choice_7dl", transition=Dissolve(0.2)), Hide("replays_route_choice_7dl", transition=Dissolve(0.2)), Show("replays_neutral_1_7dl", transition=Dissolve(0.2))]
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
        action [Hide("replays_common_choice_7dl", transition=Dissolve(0.2)), Hide("replays_un_choice_7dl", transition=Dissolve(0.2)), Hide("replays_sl_choice_7dl", transition=Dissolve(0.2)), Hide("replays_dv_choice_7dl", transition=Dissolve(0.2)), Hide("replays_mi_choice_7dl", transition=Dissolve(0.2)), Hide("replays_route_choice_7dl", transition=Dissolve(0.2)), Show("replays_us_1_7dl", transition=Dissolve(0.2))]
    textbutton "Ольга":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.235
        ypos 0.528
        action [Hide("replays_common_choice_7dl", transition=Dissolve(0.2)), Hide("replays_un_choice_7dl", transition=Dissolve(0.2)), Hide("replays_sl_choice_7dl", transition=Dissolve(0.2)), Hide("replays_dv_choice_7dl", transition=Dissolve(0.2)), Hide("replays_mi_choice_7dl", transition=Dissolve(0.2)), Hide("replays_route_choice_7dl", transition=Dissolve(0.2)), Show("replays_mt_1_7dl", transition=Dissolve(0.2))]

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
            action Replay("alt_day0_start_l", scope={"alt_replay_on" : "True"}, locked=None)
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
            action Replay("alt_day0_start_h", scope={"alt_replay_on" : "True"}, locked=None)
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
            action Replay("alt_day0_start_d", scope={"alt_replay_on" : "True"}, locked=None)
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
        textbutton "alt_day1_begin":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day1_begin", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day1_bus_start"):
        textbutton "alt_day1_bus_start":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day1_bus_start", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day1_firts_met"):
        textbutton "alt_day1_firts_met":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day1_firts_met", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
    if renpy.seen_label("alt_day1_arrival"):
        textbutton "alt_day1_arrival":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.382
            action Replay("alt_day1_arrival", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.382
    if renpy.seen_label("alt_day1_chase1"):
        textbutton "alt_day1_chase1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.431
            action Replay("alt_day1_chase1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.431
    if renpy.seen_label("alt_day1_dock"):
        textbutton "alt_day1_dock":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.479
            action Replay("alt_day1_dock", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.479
    if renpy.seen_label("alt_day1_mod_tan"):
        textbutton "alt_day1_mod_tan":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.528
            action Replay("alt_day1_mod_tan", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.528
    if renpy.seen_label("alt_day1_elektron"):
        textbutton "alt_day1_elektron":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.577
            action Replay("alt_day1_elektron", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.577
    if renpy.seen_label("alt_day1_meeting"):
        textbutton "alt_day1_meeting":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.625
            action Replay("alt_day1_meeting", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.625
    if renpy.seen_label("alt_day1_soccer_d1"):
        textbutton "alt_day1_soccer_d1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.674
            action Replay("alt_day1_soccer_d1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.674
    if renpy.seen_label("alt_day1_supper"):
        textbutton "alt_day1_supper":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.723
            action Replay("alt_day1_supper", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.723
    if renpy.seen_label("alt_day1_dining_room"):
        textbutton "alt_day1_dining_room":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.771
            action Replay("alt_day1_dining_room", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.771
    if renpy.seen_label("alt_day1_chase"):
        textbutton "alt_day1_chase":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.187
            action Replay("alt_day1_chase", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.187
    if renpy.seen_label("alt_day1_headshot"):
        textbutton "alt_day1_headshot":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.236
            action Replay("alt_day1_headshot", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.236
    if renpy.seen_label("alt_day1_nocatch"):
        textbutton "alt_day1_nocatch":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.285
            action Replay("alt_day1_nocatch", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.285
    if renpy.seen_label("alt_day1_slavya_saviour"):
        textbutton "alt_day1_slavya_saviour":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.333
            action Replay("alt_day1_slavya_saviour", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.333
    if renpy.seen_label("alt_day1_lena"):
        textbutton "alt_day1_lena":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.382
            action Replay("alt_day1_lena", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.382
    if renpy.seen_label("alt_day1_un_stay"):
        textbutton "alt_day1_un_stay":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.431
            action Replay("alt_day1_un_stay", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.431
    if renpy.seen_label("alt_day1_sleep"):
        textbutton "alt_day1_sleep":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.479
            action Replay("alt_day1_sleep", scope={"alt_replay_on" : "True"}, locked=None)
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
        textbutton "alt_day1_begin":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day1_begin", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day1_alt_M"):
        textbutton "alt_day1_alt_M":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day1_alt_M", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day1_alt_A"):
        textbutton "alt_day1_alt_A":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day1_alt_A", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
    if renpy.seen_label("alt_day1_alt_S"):
        textbutton "alt_day1_alt_S":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.382
            action Replay("alt_day1_alt_S", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.382
    if renpy.seen_label("alt_day1_alt_L"):
        textbutton "alt_day1_alt_L":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.431
            action Replay("alt_day1_alt_L", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.431
    if renpy.seen_label("alt_day1_alt_O"):
        textbutton "alt_day1_alt_O":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.479
            action Replay("alt_day1_alt_O", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.479
    if renpy.seen_label("alt_day1_alt_supper"):
        textbutton "alt_day1_alt_supper":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.528
            action Replay("alt_day1_alt_supper", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.528
    if renpy.seen_label("alt_day1_alt_U"):
        textbutton "alt_day1_alt_U":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.577
            action Replay("alt_day1_alt_U", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.577
    if renpy.seen_label("alt_day1_alt_U_reject"):
        textbutton "alt_day1_alt_U_reject":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.625
            action Replay("alt_day1_alt_U_reject", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.625
    if renpy.seen_label("alt_day1_alt_ev_A_S"):
        textbutton "alt_day1_alt_ev_A_S":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.674
            action Replay("alt_day1_alt_ev_A_S", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.674
    if renpy.seen_label("alt_day1_lena"):
        textbutton "alt_day1_lena":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.723
            action Replay("alt_day1_lena", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.723
    if renpy.seen_label("alt_day1_un_stay"):
        textbutton "alt_day1_un_stay":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.771
            action Replay("alt_day1_un_stay", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.771
    if renpy.seen_label("alt_day1_sleep"):
        textbutton "alt_day1_sleep":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.187
            action Replay("alt_day1_sleep", scope={"alt_replay_on" : "True"}, locked=None)
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
        textbutton "alt_day2_begin":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day2_begin", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day2_lineup"):
        textbutton "alt_day2_lineup":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day2_lineup", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day2_bf"):
        textbutton "alt_day2_bf":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day2_bf", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
    if renpy.seen_label("alt_day2_guide"):
        textbutton "alt_day2_guide":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.382
            action Replay("alt_day2_guide", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.382
    if renpy.seen_label("alt_day2_sl_guide"):
        textbutton "alt_day2_sl_guide":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.431
            action Replay("alt_day2_sl_guide", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.431
    if renpy.seen_label("alt_day2_sl_hyst"):
        textbutton "alt_day2_sl_hyst":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.479
            action Replay("alt_day2_sl_hyst", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.479
    if renpy.seen_label("alt_day2_event_music_club1"):
        textbutton "alt_day2_event_music_club1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.528
            action Replay("alt_day2_event_music_club1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.528
    if renpy.seen_label("alt_day2_inmusic"):
        textbutton "alt_day2_inmusic":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.577
            action Replay("alt_day2_inmusic", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.577
    if renpy.seen_label("alt_day2_event_clubs1"):
        textbutton "alt_day2_event_clubs1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.625
            action Replay("alt_day2_event_clubs1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.625
    if renpy.seen_label("alt_day2_event_camp_entrance1"):
        textbutton "alt_day2_event_camp_entrance1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.674
            action Replay("alt_day2_event_camp_entrance1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.674
    if renpy.seen_label("alt_day2_event_dv_us_house1"):
        textbutton "alt_day2_event_dv_us_house1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.723
            action Replay("alt_day2_event_dv_us_house1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.723
    if renpy.seen_label("alt_day2_event_dining_hall1"):
        textbutton "alt_day2_event_dining_hall1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.771
            action Replay("alt_day2_event_dining_hall1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.771
    if renpy.seen_label("alt_day2_event_sport_area1"):
        textbutton "alt_day2_event_sport_area1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.187
            action Replay("alt_day2_event_sport_area1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.187
    if renpy.seen_label("alt_day2_event_beach1"):
        textbutton "alt_day2_event_beach1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.236
            action Replay("alt_day2_event_beach1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.236
    if renpy.seen_label("alt_day2_event_me_mt_house1"):
        textbutton "alt_day2_event_me_mt_house1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.285
            action Replay("alt_day2_event_me_mt_house1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.285
    if renpy.seen_label("alt_day2_event_library1"):
        textbutton "alt_day2_event_library1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.333
            action Replay("alt_day2_event_library1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.333
    if renpy.seen_label("alt_day2_mz"):
        textbutton "alt_day2_mz":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.382
            action Replay("alt_day2_mz", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.382
    if renpy.seen_label("alt_day2_event_medic_house1"):
        textbutton "alt_day2_event_medic_house1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.431
            action Replay("alt_day2_event_medic_house1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.431
    if renpy.seen_label("alt_day2_event_square_dunno"):
        textbutton "alt_day2_event_square_dunno":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.479
            action Replay("alt_day2_event_square_dunno", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.479
    if renpy.seen_label("alt_day2_event_square_1"):
        textbutton "alt_day2_event_square_1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.528
            action Replay("alt_day2_event_square_1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.528
    if renpy.seen_label("alt_day2_event_boat_station1"):
        textbutton "alt_day2_event_boat_station1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.577
            action Replay("alt_day2_event_boat_station1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.577
    if renpy.seen_label("alt_day2_convoy"):
        textbutton "alt_day2_convoy":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.625
            action Replay("alt_day2_convoy", scope={"alt_replay_on" : "True"}, locked=None)
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
        textbutton "alt_day2_event_estrade":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.187
            action Replay("alt_day2_event_estrade", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.187
    if renpy.seen_label("alt_day2_phone"):
        textbutton "alt_day2_phone":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day2_phone", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day2_dubstep"):
        textbutton "alt_day2_dubstep":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day2_dubstep", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day2_dubstep2"):
        textbutton "alt_day2_dubstep2":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day2_dubstep2", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
    if renpy.seen_label("alt_day2_dinner"):
        textbutton "alt_day2_dinner":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.382
            action Replay("alt_day2_dinner", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.382
    if renpy.seen_label("alt_day2_grand_escape"):
        textbutton "alt_day2_grand_escape":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.431
            action Replay("alt_day2_grand_escape", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.431
    if renpy.seen_label("alt_day2_siesta"):
        textbutton "alt_day2_siesta":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.479
            action Replay("alt_day2_siesta", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.479
    if renpy.seen_label("alt_day2_tournament"):
        textbutton "alt_day2_tournament":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.528
            action Replay("alt_day2_tournament", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.528
    if renpy.seen_label("alt_day2_walk_sl"):
        textbutton "alt_day2_walk_sl":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.577
            action Replay("alt_day2_walk_sl", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.577
    if renpy.seen_label("alt_day2_walk_alone"):
        textbutton "alt_day2_walk_alone":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.625
            action Replay("alt_day2_walk_alone", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.625
    if renpy.seen_label("alt_day2_ultim"):
        textbutton "alt_day2_ultim":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.674
            action Replay("alt_day2_ultim", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.674
    if renpy.seen_label("alt_day2_cards"):
        textbutton "alt_day2_cards":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.723
            action Replay("alt_day2_cards", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.723
    if renpy.seen_label("alt_day2_tournament_prep"):
        textbutton "alt_day2_tournament_prep":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.771
            action Replay("alt_day2_tournament_prep", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.771
    if renpy.seen_label("alt_day2_supper"):
        textbutton "alt_day2_supper":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.187
            action Replay("alt_day2_supper", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.187
    if renpy.seen_label("alt_day2_slot_us_try"):
        textbutton "alt_day2_slot_us_try":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.236
            action Replay("alt_day2_slot_us_try", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.236
    if renpy.seen_label("alt_day2_slot_us"):
        textbutton "alt_day2_slot_us":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.285
            action Replay("alt_day2_slot_us", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.285
    if renpy.seen_label("alt_day2_sup2"):
        textbutton "alt_day2_sup2":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.333
            action Replay("alt_day2_sup2", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.333
    if renpy.seen_label("alt_day2_slot_sl"):
        textbutton "alt_day2_slot_sl":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.382
            action Replay("alt_day2_slot_sl", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.382
    if renpy.seen_label("alt_day2_eventEv_beach1"):
        textbutton "alt_day2_eventEv_beach1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.431
            action Replay("alt_day2_eventEv_beach1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.431
    if renpy.seen_label("alt_day2_slot_dv"):
        textbutton "alt_day2_slot_dv":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.479
            action Replay("alt_day2_slot_dv", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.479

screen replays_common_d2_3_7dl:
    tag menu
    text "Часть 5":
        style "replays_text"
        xcenter 0.432
        ycenter 0.885
    text "Часть 6":
        style "replays_text"
        xcenter 0.741
        ycenter 0.883
    imagebutton:
        auto get_image_7dl("gui/gallery/gallery_left_arrow_%s.png") xcenter 0.256 ycenter 0.923 
        action Show("replays_common_d2_2_7dl", transition=Dissolve(0.2))
    if renpy.seen_label("alt_day2_eventEv_music_club1"):
        textbutton "alt_day2_eventEv_music_club1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.187
            action Replay("alt_day2_eventEv_music_club1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.187
    if renpy.seen_label("alt_day2_slot_mi"):
        textbutton "alt_day2_slot_mi":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day2_slot_mi", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day2_eventEv_clubs1"):
        textbutton "alt_day2_eventEv_clubs1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day2_eventEv_clubs1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day2_eventEv_camp_entrance1"):
        textbutton "alt_day2_eventEv_camp_entrance1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day2_eventEv_camp_entrance1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
    if renpy.seen_label("alt_day2_eventEv_un_mi_house1"):
        textbutton "alt_day2_eventEv_un_mi_house1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.382
            action Replay("alt_day2_eventEv_un_mi_house1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.382
    if renpy.seen_label("alt_day2_un_loki_date"):
        textbutton "alt_day2_un_loki_date":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.431
            action Replay("alt_day2_un_loki_date", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.431
    if renpy.seen_label("alt_day2_un_herc_date"):
        textbutton "alt_day2_un_herc_date":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.479
            action Replay("alt_day2_un_herc_date", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.479
    if renpy.seen_label("alt_day2_eventEv_dv_us_house1"):
        textbutton "alt_day2_eventEv_dv_us_house1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.528
            action Replay("alt_day2_eventEv_dv_us_house1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.528
    if renpy.seen_label("alt_day2_eventEv_dining_hall1"):
        textbutton "alt_day2_eventEv_dining_hall1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.577
            action Replay("alt_day2_eventEv_dining_hall1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.577
    if renpy.seen_label("alt_day2_eventEv_sport_area1"):
        textbutton "alt_day2_eventEv_sport_area1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.625
            action Replay("alt_day2_eventEv_sport_area1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.625
    if renpy.seen_label("alt_day2_slot_un"):
        textbutton "alt_day2_slot_un":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.674
            action Replay("alt_day2_slot_un", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.674
    if renpy.seen_label("alt_day2_eventEv_me_mt_house1"):
        textbutton "alt_day2_eventEv_me_mt_house1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.723
            action Replay("alt_day2_eventEv_me_mt_house1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.723
    if renpy.seen_label("alt_day2_eventEv_library1"):
        textbutton "alt_day2_eventEv_library1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.771
            action Replay("alt_day2_eventEv_library1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.771
    if renpy.seen_label("alt_day2_eventEv_medic_house1"):
        textbutton "alt_day2_eventEv_medic_house1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.187
            action Replay("alt_day2_eventEv_medic_house1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.187
    if renpy.seen_label("alt_day2_eventEv_estrade1"):
        textbutton "alt_day2_eventEv_estrade1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.236
            action Replay("alt_day2_eventEv_estrade1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.236
    if renpy.seen_label("alt_day2_eventEv_square1"):
        textbutton "alt_day2_eventEv_square1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.285
            action Replay("alt_day2_eventEv_square1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.285
    if renpy.seen_label("alt_day2_eventEv_boat_station1"):
        textbutton "alt_day2_eventEv_boat_station1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.333
            action Replay("alt_day2_eventEv_boat_station1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.333
    if renpy.seen_label("alt_day2_dream"):
        textbutton "alt_day2_dream":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.382
            action Replay("alt_day2_dream", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.382

screen replays_common_d3_1_7dl:
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
        action Show("replays_common_d3_2_7dl", transition=Dissolve(0.2))
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.235
        ypos 0.187
        action [Hide("replays_common_d3_1_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]
    if renpy.seen_label("alt_day3_begin"):
        textbutton "alt_day3_begin":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day3_begin", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day3_bf"):
        textbutton "alt_day3_bf":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day3_bf", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day3_event_library1"):
        textbutton "alt_day3_event_library1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day3_event_library1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
    if renpy.seen_label("alt_day3_event_estrade"):
        textbutton "alt_day3_event_estrade":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.382
            action Replay("alt_day3_event_estrade", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.382
    if renpy.seen_label("alt_day3_event_music_club"):
        textbutton "alt_day3_event_music_club":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.431
            action Replay("alt_day3_event_music_club", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.431
    if renpy.seen_label("alt_day3_bf_duty"):
        textbutton "alt_day3_bf_duty":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.479
            action Replay("alt_day3_bf_duty", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.479
    if renpy.seen_label("alt_day3_event_camp_entrance"):
        textbutton "alt_day3_event_camp_entrance":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.528
            action Replay("alt_day3_event_camp_entrance", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.528
    if renpy.seen_label("alt_day3_event_music_club1"):
        textbutton "alt_day3_event_music_club1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.577
            action Replay("alt_day3_event_music_club1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.577
    if renpy.seen_label("alt_day3_event_clubs1"):
        textbutton "alt_day3_event_clubs1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.625
            action Replay("alt_day3_event_clubs1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.625
    if renpy.seen_label("alt_day3_event_camp_entrance1"):
        textbutton "alt_day3_event_camp_entrance1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.674
            action Replay("alt_day3_event_camp_entrance1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.674
    if renpy.seen_label("alt_day3_event_dining_hall1"):
        textbutton "alt_day3_event_dining_hall1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.723
            action Replay("alt_day3_event_dining_hall1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.723
    if renpy.seen_label("alt_day3_event_sport_area1"):
        textbutton "alt_day3_event_sport_area1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.771
            action Replay("alt_day3_event_sport_area1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.771
    if renpy.seen_label("alt_day3_event_beach1"):
        textbutton "alt_day3_event_beach1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.187
            action Replay("alt_day3_event_beach1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.187
    if renpy.seen_label("alt_day3_event_medic_house1"):
        textbutton "alt_day3_event_medic_house1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.236
            action Replay("alt_day3_event_medic_house1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.236
    if renpy.seen_label("alt_day3_event_estrade1"):
        textbutton "alt_day3_event_estrade1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.285
            action Replay("alt_day3_event_estrade1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.285
    if renpy.seen_label("alt_day3_event_square1"):
        textbutton "alt_day3_event_square1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.333
            action Replay("alt_day3_event_square1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.333
    if renpy.seen_label("alt_day3_event_boat_station1"):
        textbutton "alt_day3_event_boat_station1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.382
            action Replay("alt_day3_event_boat_station1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.382
    if renpy.seen_label("alt_day3_dinner"):
        textbutton "alt_day3_dinner":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.431
            action Replay("alt_day3_dinner", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.431
    if renpy.seen_label("alt_day3_dinner_menu"):
        textbutton "alt_day3_dinner_menu":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.479
            action Replay("alt_day3_dinner_menu", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.479

screen replays_common_d3_2_7dl:
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
        action Show("replays_common_d3_1_7dl", transition=Dissolve(0.2))
    imagebutton:
        auto get_image_7dl("gui/gallery/gallery_right_arrow_%s.png") xcenter 0.749 ycenter 0.923 
        action Show("replays_common_d3_3_7dl", transition=Dissolve(0.2))
    if renpy.seen_label("alt_day3_eventAf_music_club1"):
        textbutton "alt_day3_eventAf_music_club1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.187
            action Replay("alt_day3_eventAf_music_club1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.187
    if renpy.seen_label("alt_day3_eventAf_library1"):
        textbutton "alt_day3_eventAf_library1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day3_eventAf_library1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day3_eventAf_clubs_ladder"):
        textbutton "alt_day3_eventAf_clubs_ladder":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day3_eventAf_clubs_ladder", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day3_eventAf_clubs_technoquest"):
        textbutton "alt_day3_eventAf_clubs_technoquest":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day3_eventAf_clubs_technoquest", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
    if renpy.seen_label("alt_day3_eventAf_un_mi_house1"):
        textbutton "alt_day3_eventAf_un_mi_house1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.382
            action Replay("alt_day3_eventAf_un_mi_house1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.382
    if renpy.seen_label("alt_day3_eventAf_dining_hall1"):
        textbutton "alt_day3_eventAf_dining_hall1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.431
            action Replay("alt_day3_eventAf_dining_hall1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.431
    if renpy.seen_label("alt_day3_eventAf_admins1"):
        textbutton "alt_day3_eventAf_admins1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.479
            action Replay("alt_day3_eventAf_admins1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.479
    if renpy.seen_label("alt_day3_sl_postlunch"):
        textbutton "alt_day3_sl_postlunch":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.528
            action Replay("alt_day3_sl_postlunch", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.528
    if renpy.seen_label("alt_day3_eventAf_me_mt_house1"):
        textbutton "alt_day3_eventAf_me_mt_house1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.577
            action Replay("alt_day3_eventAf_me_mt_house1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.577
    if renpy.seen_label("alt_day3_eventAf_estrade1"):
        textbutton "alt_day3_eventAf_estrade1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.625
            action Replay("alt_day3_eventAf_estrade1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.625
    if renpy.seen_label("alt_day3_music"):
        textbutton "alt_day3_music":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.674
            action Replay("alt_day3_music", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.674
    if renpy.seen_label("alt_day3_aftermath"):
        textbutton "alt_day3_aftermath":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.723
            action Replay("alt_day3_aftermath", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.723
    if renpy.seen_label("alt_day3_nightmare"):
        textbutton "alt_day3_nightmare":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.771
            action Replay("alt_day3_nightmare", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.771
    if renpy.seen_label("alt_day3_supper1"):
        textbutton "alt_day3_supper1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.187
            action Replay("alt_day3_supper1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.187
    if renpy.seen_label("alt_day3_supper"):
        textbutton "alt_day3_supper":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.236
            action Replay("alt_day3_supper", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.236
    if renpy.seen_label("alt_day3_supper2"):
        textbutton "alt_day3_supper2":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.285
            action Replay("alt_day3_supper2", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.285

screen replays_common_d3_3_7dl:
    tag menu
    text "Часть 5":
        style "replays_text"
        xcenter 0.432
        ycenter 0.885
    text "Часть 6":
        style "replays_text"
        xcenter 0.741
        ycenter 0.883
    imagebutton:
        auto get_image_7dl("gui/gallery/gallery_left_arrow_%s.png") xcenter 0.256 ycenter 0.923 
        action Show("replays_common_d3_2_7dl", transition=Dissolve(0.2))
    if renpy.seen_label("alt_day3_dance_dance"):
        textbutton "alt_day3_dance_dance":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.187
            action Replay("alt_day3_dance_dance", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.187
    if renpy.seen_label("alt_day3_makeup"):
        textbutton "alt_day3_makeup":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day3_makeup", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day3_dv_lf"):
        textbutton "alt_day3_dv_lf":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day3_dv_lf", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day3_rockstar"):
        textbutton "alt_day3_rockstar":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day3_rockstar", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
    if renpy.seen_label("alt_day3_dv_reunion"):
        textbutton "alt_day3_dv_reunion":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.382
            action Replay("alt_day3_dv_reunion", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.382
    if renpy.seen_label("alt_day3_dv_stayhere1"):
        textbutton "alt_day3_dv_stayhere1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.431
            action Replay("alt_day3_dv_stayhere1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.431
    if renpy.seen_label("alt_day3_bath_voyeur"):
        textbutton "alt_day3_bath_voyeur":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.479
            action Replay("alt_day3_bath_voyeur", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.479
    if renpy.seen_label("alt_day3_leave1"):
        textbutton "alt_day3_leave1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.528
            action Replay("alt_day3_leave1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.528
    if renpy.seen_label("alt_day3_choose"):
        textbutton "alt_day3_choose":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.577
            action Replay("alt_day3_choose", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.577
    if renpy.seen_label("alt_day3_dance_dance2"):
        textbutton "alt_day3_dance_dance2":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.625
            action Replay("alt_day3_dance_dance2", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.625
    if renpy.seen_label("alt_day3_med_un"):
        textbutton "alt_day3_med_un":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.674
            action Replay("alt_day3_med_un", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.674
    if renpy.seen_label("alt_day3_un_cards"):
        textbutton "alt_day3_un_cards":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.723
            action Replay("alt_day3_un_cards", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.723
    if renpy.seen_label("alt_day3_un_strip_play"):
        textbutton "alt_day3_un_strip_play":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.771
            action Replay("alt_day3_un_strip_play", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.771
    if renpy.seen_label("alt_day3_card_lose"):
        textbutton "alt_day3_card_lose":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.187
            action Replay("alt_day3_card_lose", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.187
    if renpy.seen_label("alt_day3_card_won"):
        textbutton "alt_day3_card_won":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.236
            action Replay("alt_day3_card_won", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.236
    if renpy.seen_label("alt_day3_post_strip"):
        textbutton "alt_day3_post_strip":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.285
            action Replay("alt_day3_post_strip", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.285
    if renpy.seen_label("alt_day3_mt_scare"):
        textbutton "alt_day3_mt_scare":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.333
            action Replay("alt_day3_mt_scare", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.333
    if renpy.seen_label("alt_day3_dance_dance2_menu"):
        textbutton "alt_day3_dance_dance2_menu":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.382
            action Replay("alt_day3_dance_dance2_menu", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.382
    if renpy.seen_label("alt_day3_technoquest3"):
        textbutton "alt_day3_technoquest3":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.431
            action Replay("alt_day3_technoquest3", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.431
    if renpy.seen_label("alt_day3_choose3"):
        textbutton "alt_day3_choose3":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.479
            action Replay("alt_day3_choose3", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.479
    if renpy.seen_label("alt_day3_mi_7dl_init"):
        textbutton "alt_day3_mi_7dl_init":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.528
            action Replay("alt_day3_mi_7dl_init", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.528
    if renpy.seen_label("alt_day3_disco_past_d2"):
        textbutton "alt_day3_disco_past_d2":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.577
            action Replay("alt_day3_disco_past_d2", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.577
    if renpy.seen_label("alt_day3_sleeptime"):
        textbutton "alt_day3_sleeptime":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.625
            action Replay("alt_day3_sleeptime", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.625

screen replays_neutral_1_7dl:
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
        action Show("replays_neutral_2_7dl", transition=Dissolve(0.2))
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.235
        ypos 0.187
        action [Hide("replays_neutral_1_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]
    if renpy.seen_label("alt_day4_neu_dv"):
        textbutton "alt_day4_neu_dv":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day4_neu_dv", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day4_neu_aid"):
        textbutton "alt_day4_neu_aid":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day4_neu_aid", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day4_neu_aid_un"):
        textbutton "alt_day4_neu_aid_un":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day4_neu_aid_un", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
    if renpy.seen_label("alt_day4_neu_aid_sl"):
        textbutton "alt_day4_neu_aid_sl":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.382
            action Replay("alt_day4_neu_aid_sl", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.382
    if renpy.seen_label("alt_day4_neu_aid_generic"):
        textbutton "alt_day4_neu_aid_generic":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.431
            action Replay("alt_day4_neu_aid_generic", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.431
    if renpy.seen_label("alt_day4_neu_mt"):
        textbutton "alt_day4_neu_mt":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.479
            action Replay("alt_day4_neu_mt", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.479
    if renpy.seen_label("alt_day4_neu_us"):
        textbutton "alt_day4_neu_us":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.528
            action Replay("alt_day4_neu_us", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.528
    if renpy.seen_label("alt_day4_neu_home"):
        textbutton "alt_day4_neu_home":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.577
            action Replay("alt_day4_neu_home", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.577
    if renpy.seen_label("alt_day4_neu_un"):
        textbutton "alt_day4_neu_un":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.625
            action Replay("alt_day4_neu_un", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.625
    if renpy.seen_label("alt_day4_neu_mi"):
        textbutton "alt_day4_neu_mi":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.674
            action Replay("alt_day4_neu_mi", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.674
    if renpy.seen_label("alt_day4_neu_sl"):
        textbutton "alt_day4_neu_sl":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.723
            action Replay("alt_day4_neu_sl", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.723
    if renpy.seen_label("alt_day4_neu_dinner"):
        textbutton "alt_day4_neu_dinner":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.771
            action Replay("alt_day4_neu_dinner", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.771
    if renpy.seen_label("alt_day4_neu_curl"):
        textbutton "alt_day4_neu_curl":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.187
            action Replay("alt_day4_neu_curl", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.187
    if renpy.seen_label("alt_day4_neu_lunch"):
        textbutton "alt_day4_neu_lunch":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.236
            action Replay("alt_day4_neu_lunch", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.236
    if renpy.seen_label("alt_day4_neu_supper"):
        textbutton "alt_day4_neu_supper":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.285
            action Replay("alt_day4_neu_supper", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.285
    if renpy.seen_label("alt_day4_neu_map_me_mt_house"):
        textbutton "alt_day4_neu_map_me_mt_house":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.333
            action Replay("alt_day4_neu_map_me_mt_house", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.333
    if renpy.seen_label("alt_day4_neu_mt_diary_vol1"):
        textbutton "alt_day4_neu_mt_diary_vol1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.382
            action Replay("alt_day4_neu_mt_diary_vol1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.382
    if renpy.seen_label("alt_day4_neu_us_guards"):
        textbutton "alt_day4_neu_us_guards":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.431
            action Replay("alt_day4_neu_us_guards", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.431
    if renpy.seen_label("alt_day4_neu_us_launch"):
        textbutton "alt_day4_neu_us_launch":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.479
            action Replay("alt_day4_neu_us_launch", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.479
    if renpy.seen_label("alt_day4_neu_map_dining_hall"):
        textbutton "alt_day4_neu_map_dining_hall":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.528
            action Replay("alt_day4_neu_map_dining_hall", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.528
    if renpy.seen_label("alt_day4_neu_sleeptime"):
        textbutton "alt_day4_neu_sleeptime":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.577
            action Replay("alt_day4_neu_sleeptime", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.577
            
screen replays_neutral_2_7dl:
    tag menu
    text "День 5":
        style "replays_text"
        xcenter 0.432
        ycenter 0.885
    text "День 5":
        style "replays_text"
        xcenter 0.741
        ycenter 0.883
    imagebutton:
        auto get_image_7dl("gui/gallery/gallery_left_arrow_%s.png") xcenter 0.256 ycenter 0.923 
        action Show("replays_neutral_1_7dl", transition=Dissolve(0.2))
    if renpy.seen_label("alt_day5_morningdream"):
        textbutton "alt_day5_morningdream":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.187
            action Replay("alt_day5_morningdream", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.187
    if renpy.seen_label("alt_day5_neu_start"):
        textbutton "alt_day5_neu_start":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day5_neu_start", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day5_neu_breakfast"):
        textbutton "alt_day5_neu_breakfast":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day5_neu_breakfast", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day5_neu_along"):
        textbutton "alt_day5_neu_along":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day5_neu_along", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
    if renpy.seen_label("alt_day5_neu_cndl"):
        textbutton "alt_day5_neu_cndl":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.382
            action Replay("alt_day5_neu_cndl", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.382
    if renpy.seen_label("alt_day5_neu_gaming"):
        textbutton "alt_day5_neu_gaming":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.431
            action Replay("alt_day5_neu_gaming", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.431
    if renpy.seen_label("alt_day5_neu_arrest"):
        textbutton "alt_day5_neu_arrest":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.479
            action Replay("alt_day5_neu_arrest", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.479
    if renpy.seen_label("alt_day5_neu_dinner"):
        textbutton "alt_day5_neu_dinner":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.528
            action Replay("alt_day5_neu_dinner", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.528
    if renpy.seen_label("alt_day5_neu_us_career"):
        textbutton "alt_day5_neu_us_career":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.577
            action Replay("alt_day5_neu_us_career", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.577
    if renpy.seen_label("alt_day5_neu_us_punishment"):
        textbutton "alt_day5_neu_us_punishment":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.625
            action Replay("alt_day5_neu_us_punishment", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.625
    if renpy.seen_label("alt_day5_neu_us_warm_evening"):
        textbutton "alt_day5_neu_us_warm_evening":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.674
            action Replay("alt_day5_neu_us_warm_evening", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.674
    if renpy.seen_label("alt_day5_neu_us_hungry"):
        textbutton "alt_day5_neu_us_hungry":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.723
            action Replay("alt_day5_neu_us_hungry", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.723
    if renpy.seen_label("alt_day5_neu_us_sleetptime"):
        textbutton "alt_day5_neu_us_sleetptime":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.771
            action Replay("alt_day5_neu_us_sleetptime", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.771
    if renpy.seen_label("alt_day5_neu_mi_estrade"):
        textbutton "alt_day5_neu_mi_estrade":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.187
            action Replay("alt_day5_neu_mi_estrade", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.187
    if renpy.seen_label("alt_day5_neu_lunch"):
        textbutton "alt_day5_neu_lunch":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.236
            action Replay("alt_day5_neu_lunch", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.236
    if renpy.seen_label("alt_day5_neu_supper"):
        textbutton "alt_day5_neu_supper":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.285
            action Replay("alt_day5_neu_supper", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.285
    if renpy.seen_label("alt_day5_neu_evening"):
        textbutton "alt_day5_neu_evening":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.333
            action Replay("alt_day5_neu_evening", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.333
    if renpy.seen_label("alt_day5_neu_campfire_doom"):
        textbutton "alt_day5_neu_campfire_doom":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.382
            action Replay("alt_day5_neu_campfire_doom", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.382
    if renpy.seen_label("alt_day5_neu_sleepnight"):
        textbutton "alt_day5_neu_sleepnight":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.431
            action Replay("alt_day5_neu_sleepnight", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.431
    if renpy.seen_label("alt_day5_neu_mt_selector"):
        textbutton "alt_day5_neu_mt_selector":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.479
            action Replay("alt_day5_neu_mt_selector", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.479
    if renpy.seen_label("alt_day5_neu_mt_retrib"):
        textbutton "alt_day5_neu_mt_retrib":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.528
            action Replay("alt_day5_neu_mt_retrib", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.528
    if renpy.seen_label("alt_day5_neu_mt_tea_party"):
        textbutton "alt_day5_neu_mt_tea_party":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.577
            action Replay("alt_day5_neu_mt_tea_party", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544

screen replays_un_choice_7dl:
    textbutton "7дл":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.544
        ypos 0.187
        action [Hide("replays_route_choice_7dl", transition=Dissolve(0.2)), Hide("replays_un_choice_7dl", transition=Dissolve(0.2)), Show("replays_un_7dl_1_7dl", transition=Dissolve(0.2))]

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

screen replays_un_7dl_1_7dl:
    tag menu
    text "День 4":
        style "replays_text"
        xcenter 0.432
        ycenter 0.885
    text "День 5":
        style "replays_text"
        xcenter 0.741
        ycenter 0.883
    imagebutton:
        auto get_image_7dl("gui/gallery/gallery_right_arrow_%s.png") xcenter 0.749 ycenter 0.923 
        action Show("replays_un_7dl_2_7dl", transition=Dissolve(0.2))
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.235
        ypos 0.187
        action [Hide("replays_un_7dl_1_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]
    if renpy.seen_label("alt_day4_un_7dl_begin"):
        textbutton "alt_day4_un_7dl_begin":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day4_un_7dl_begin", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day4_un_7dl_lineup"):
        textbutton "alt_day4_un_7dl_lineup":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day4_un_7dl_lineup", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day4_un_7dl_breakfast"):
        textbutton "alt_day4_un_7dl_breakfast":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day4_un_7dl_breakfast", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
    if renpy.seen_label("alt_day4_un_7dl_declaration"):
        textbutton "alt_day4_un_7dl_declaration":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.382
            action Replay("alt_day4_un_7dl_declaration", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.382
    if renpy.seen_label("alt_day4_un_7dl_dinner"):
        textbutton "alt_day4_un_7dl_dinner":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.431
            action Replay("alt_day4_un_7dl_dinner", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.431
    if renpy.seen_label("alt_day4_un_7dl_launch"):
        textbutton "alt_day4_un_7dl_launch":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.479
            action Replay("alt_day4_un_7dl_launch", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.479
    if renpy.seen_label("alt_day4_un_7dl_supper"):
        textbutton "alt_day4_un_7dl_supper":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.528
            action Replay("alt_day4_un_7dl_supper", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.528
    if renpy.seen_label("alt_day4_un_7dl_sleeptime"):
        textbutton "alt_day4_un_7dl_sleeptime":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.577
            action Replay("alt_day4_un_7dl_sleeptime", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.577
    if renpy.seen_label("alt_day5_un_7dl_begin"):
        textbutton "alt_day5_un_7dl_begin":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.187
            action Replay("alt_day5_un_7dl_begin", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.187
    if renpy.seen_label("alt_day5_un_7dl_breakfast"):
        textbutton "alt_day5_un_7dl_breakfast":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.236
            action Replay("alt_day5_un_7dl_breakfast", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.236
    if renpy.seen_label("alt_day5_un_7dl_breakfast_l"):
        textbutton "alt_day5_un_7dl_breakfast_l":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.285
            action Replay("alt_day5_un_7dl_breakfast_l", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.285
    if renpy.seen_label("alt_day5_un_7dl_clubs"):
        textbutton "alt_day5_un_7dl_clubs":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.333
            action Replay("alt_day5_un_7dl_clubs", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.333
    if renpy.seen_label("alt_day5_un_7dl_breakfast_h"):
        textbutton "alt_day5_un_7dl_breakfast_h":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.382
            action Replay("alt_day5_un_7dl_breakfast_h", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.382
    if renpy.seen_label("alt_day5_un_7dl_games"):
        textbutton "alt_day5_un_7dl_games":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.431
            action Replay("alt_day5_un_7dl_games", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.431
    if renpy.seen_label("alt_day5_un_7dl_cleaning"):
        textbutton "alt_day5_un_7dl_cleaning":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.479
            action Replay("alt_day5_un_7dl_cleaning", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.479
    if renpy.seen_label("alt_day5_un_7dl_dinner"):
        textbutton "alt_day5_un_7dl_dinner":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.528
            action Replay("alt_day5_un_7dl_dinner", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.528
    if renpy.seen_label("alt_day5_un_7dl_dinner_d"):
        textbutton "alt_day5_un_7dl_dinner_d":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.577
            action Replay("alt_day5_un_7dl_dinner_d", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.577
    if renpy.seen_label("alt_day5_un_7dl_unl"):
        textbutton "alt_day5_un_7dl_unl":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.625
            action Replay("alt_day5_un_7dl_unl", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.625
    if renpy.seen_label("alt_day5_un_7dl_dinner_hl"):
        textbutton "alt_day5_un_7dl_dinner_hl":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.674
            action Replay("alt_day5_un_7dl_dinner_hl", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.674
    if renpy.seen_label("alt_day5_un_7dl_np"):
        textbutton "alt_day5_un_7dl_np":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.723
            action Replay("alt_day5_un_7dl_np", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.723
    if renpy.seen_label("alt_day5_un_7dl_launch"):
        textbutton "alt_day5_un_7dl_launch":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.771
            action Replay("alt_day5_un_7dl_launch", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.771

screen replays_un_7dl_2_7dl:
    tag menu
    text "День 5":
        style "replays_text"
        xcenter 0.432
        ycenter 0.885
    text "День 6":
        style "replays_text"
        xcenter 0.741
        ycenter 0.883
    imagebutton:
        auto get_image_7dl("gui/gallery/gallery_left_arrow_%s.png") xcenter 0.256 ycenter 0.923 
        action Show("replays_un_7dl_1_7dl", transition=Dissolve(0.2))
    imagebutton:
        auto get_image_7dl("gui/gallery/gallery_right_arrow_%s.png") xcenter 0.749 ycenter 0.923 
        action Show("replays_un_7dl_3_7dl", transition=Dissolve(0.2))
    if renpy.seen_label("alt_day5_un_7dl_library"):
        textbutton "alt_day5_un_7dl_library":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.187
            action Replay("alt_day5_un_7dl_library", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.187
    if renpy.seen_label("alt_day5_un_7dl_washing"):
        textbutton "alt_day5_un_7dl_washing":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day5_un_7dl_washing", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day5_un_7dl_supper"):
        textbutton "alt_day5_un_7dl_supper":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day5_un_7dl_supper", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day5_un_7dl_runaway"):
        textbutton "alt_day5_un_7dl_runaway":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day5_un_7dl_runaway", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
    if renpy.seen_label("alt_day5_un_7dl_video"):
        textbutton "alt_day5_un_7dl_video":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.382
            action Replay("alt_day5_un_7dl_video", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.382
    if renpy.seen_label("alt_day5_un_7dl_evening_un"):
        textbutton "alt_day5_un_7dl_evening_un":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.431
            action Replay("alt_day5_un_7dl_evening_un", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.431
    if renpy.seen_label("alt_day5_un_7dl_evening_dv"):
        textbutton "alt_day5_un_7dl_evening_dv":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.479
            action Replay("alt_day5_un_7dl_evening_dv", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.479
    if renpy.seen_label("alt_day5_un_7dl_island_hen"):
        textbutton "alt_day5_un_7dl_island_hen":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.528
            action Replay("alt_day5_un_7dl_island_hen", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.528
    if renpy.seen_label("alt_day5_un_7dl_sleeptime"):
        textbutton "alt_day5_un_7dl_sleeptime":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.577
            action Replay("alt_day5_un_7dl_sleeptime", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.577
    if renpy.seen_label("alt_day6_un_7dl_begin"):
        textbutton "alt_day6_un_7dl_begin":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.187
            action Replay("alt_day6_un_7dl_begin", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.187
    if renpy.seen_label("alt_day6_un_7dl_dinner"):
        textbutton "alt_day6_un_7dl_dinner":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.236
            action Replay("alt_day6_un_7dl_dinner", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.236
    if renpy.seen_label("alt_day6_un_7dl_supper"):
        textbutton "alt_day6_un_7dl_supper":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.285
            action Replay("alt_day6_un_7dl_supper", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.285
    if renpy.seen_label("alt_day6_un_7dl_letmeout"):
        textbutton "alt_day6_un_7dl_letmeout":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.333
            action Replay("alt_day6_un_7dl_letmeout", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.333
    if renpy.seen_label("alt_day6_un_7dl_dance"):
        textbutton "alt_day6_un_7dl_dance":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.382
            action Replay("alt_day6_un_7dl_dance", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.382
    if renpy.seen_label("alt_day6_un_7dl_sleeptime"):
        textbutton "alt_day6_un_7dl_sleeptime":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.431
            action Replay("alt_day6_un_7dl_sleeptime", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.431

screen replays_un_7dl_3_7dl:
    tag menu
    text "День 7":
        style "replays_text"
        xcenter 0.432
        ycenter 0.885
    imagebutton:
        auto get_image_7dl("gui/gallery/gallery_left_arrow_%s.png") xcenter 0.256 ycenter 0.923 
        action Show("replays_un_7dl_2_7dl", transition=Dissolve(0.2))
    if renpy.seen_label("alt_day7_un_7dl_begin"):
        textbutton "alt_day7_un_7dl_begin":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.187
            action Replay("alt_day7_un_7dl_begin", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.187
    if renpy.seen_label("alt_day7_un_7dl_epilogue_all"):
        textbutton "alt_day7_un_7dl_epilogue_all":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day7_un_7dl_epilogue_all", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day7_un_7dl_epilogue"):
        textbutton "alt_day7_un_7dl_epilogue":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day7_un_7dl_epilogue", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day7_un_7dl_epilogue_rt"):
        textbutton "alt_day7_un_7dl_epilogue_rt":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day7_un_7dl_epilogue_rt", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
            
screen replays_un_fz_7dl:
    tag menu
    text "День 4":
        style "replays_text"
        xcenter 0.432
        ycenter 0.885
    text "День 4":
        style "replays_text"
        xcenter 0.741
        ycenter 0.883
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.235
        ypos 0.187
        action [Hide("replays_un_fz_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]
    if renpy.seen_label("alt_day4_un_fz_begin"):
        textbutton "alt_day4_un_fz_begin":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day4_un_fz_begin", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day4_un_fz_sl"):
        textbutton "alt_day4_un_fz_sl":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day4_un_fz_sl", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day4_fz_play"):
        textbutton "alt_day4_fz_play":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day4_fz_play", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
    if renpy.seen_label("alt_day4_fz_postcard"):
        textbutton "alt_day4_fz_postcard":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.382
            action Replay("alt_day4_fz_postcard", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.382
    if renpy.seen_label("alt_day4_un_fz_dv"):
        textbutton "alt_day4_un_fz_dv":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.431
            action Replay("alt_day4_un_fz_dv", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.431
    if renpy.seen_label("alt_day4_fz_dv_dinner"):
        textbutton "alt_day4_fz_dv_dinner":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.479
            action Replay("alt_day4_fz_dv_dinner", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.479
    if renpy.seen_label("alt_day4_fz_lost_coun"):
        textbutton "alt_day4_fz_lost_coun":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.528
            action Replay("alt_day4_fz_lost_coun", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.528
    if renpy.seen_label("alt_day4_fz_supper"):
        textbutton "alt_day4_fz_supper":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.577
            action Replay("alt_day4_fz_supper", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.577
    if renpy.seen_label("alt_day4_fz_sh_choose"):
        textbutton "alt_day4_fz_sh_choose":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.625
            action Replay("alt_day4_fz_sh_choose", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.625
    if renpy.seen_label("alt_day4_fz_sh_menu"):
        textbutton "alt_day4_fz_sh_menu":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.674
            action Replay("alt_day4_fz_sh_menu", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.674
    if renpy.seen_label("alt_day4_fz_old_camp"):
        textbutton "alt_day4_fz_old_camp":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.723
            action Replay("alt_day4_fz_old_camp", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.723
    if renpy.seen_label("alt_day4_fz_xroad"):
        textbutton "alt_day4_fz_xroad":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.771
            action Replay("alt_day4_fz_xroad", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.771
    if renpy.seen_label("alt_day4_fz_exit"):
        textbutton "alt_day4_fz_exit":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.187
            action Replay("alt_day4_fz_exit", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.187
    if renpy.seen_label("alt_day4_fz_herbs"):
        textbutton "alt_day4_fz_herbs":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.236
            action Replay("alt_day4_fz_herbs", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.236
    if renpy.seen_label("alt_day5_fz_begin"):
        textbutton "alt_day5_fz_begin":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.285
            action Replay("alt_day5_fz_begin", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.285

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
        action [Hide("replays_route_choice_7dl", transition=Dissolve(0.2)), Hide("replays_sl_choice_7dl", transition=Dissolve(0.2)), Show("replays_sl_cl_1_7dl", transition=Dissolve(0.2))]

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
            action Replay("alt_day4_sl_7dl_begin", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236

screen replays_sl_cl_1_7dl:
    tag menu
    text "День 4":
        style "replays_text"
        xcenter 0.432
        ycenter 0.885
    text "День 5":
        style "replays_text"
        xcenter 0.741
        ycenter 0.883
    imagebutton:
        auto get_image_7dl("gui/gallery/gallery_right_arrow_%s.png") xcenter 0.749 ycenter 0.923 
        action Show("replays_sl_cl_2_7dl", transition=Dissolve(0.2))
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.235
        ypos 0.187
        action [Hide("replays_sl_cl_1_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]
    if renpy.seen_label("alt_day4_sl_begin"):
        textbutton "alt_day4_sl_begin":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day4_sl_begin", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day4_sl_cl_shurik"):
        textbutton "alt_day4_sl_cl_shurik":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day4_sl_cl_shurik", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day4_sl_laundry"):
        textbutton "alt_day4_sl_laundry":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day4_sl_laundry", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
    if renpy.seen_label("alt_day4_sl_supper"):
        textbutton "alt_day4_sl_supper":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.382
            action Replay("alt_day4_sl_supper", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.382
    if renpy.seen_label("alt_day4_sl_party_up"):
        textbutton "alt_day4_sl_party_up":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.431
            action Replay("alt_day4_sl_party_up", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.431
    if renpy.seen_label("alt_day4_sl_lf_coop"):
        textbutton "alt_day4_sl_lf_coop":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.479
            action Replay("alt_day4_sl_lf_coop", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.479
    if renpy.seen_label("alt_day4_sl_old_camp"):
        textbutton "alt_day4_sl_old_camp":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.528
            action Replay("alt_day4_sl_old_camp", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.528
    if renpy.seen_label("alt_day4_sl_wh_night"):
        textbutton "alt_day4_sl_wh_night":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.577
            action Replay("alt_day4_sl_wh_night", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.577
    if renpy.seen_label("alt_day4_sl_old_camp2"):
        textbutton "alt_day4_sl_old_camp2":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.625
            action Replay("alt_day4_sl_old_camp2", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.625
    if renpy.seen_label("alt_day4_sl_cs_night"):
        textbutton "alt_day4_sl_cs_night":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.674
            action Replay("alt_day4_sl_cs_night", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.674
    if renpy.seen_label("alt_day5_sl_begin"):
        textbutton "alt_day5_sl_begin":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.187
            action Replay("alt_day5_sl_begin", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.187
    if renpy.seen_label("alt_day5_sl_dinner"):
        textbutton "alt_day5_sl_dinner":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.236
            action Replay("alt_day5_sl_dinner", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.236
    if renpy.seen_label("alt_day5_sl_supper"):
        textbutton "alt_day5_sl_supper":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.285
            action Replay("alt_day5_sl_supper", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.285
    if renpy.seen_label("alt_day5_sl_fire"):
        textbutton "alt_day5_sl_fire":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.333
            action Replay("alt_day5_sl_fire", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.333
    if renpy.seen_label("alt_day5_sl_night"):
        textbutton "alt_day5_sl_night":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.382
            action Replay("alt_day5_sl_night", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.382

screen replays_sl_cl_2_7dl:
    tag menu
    text "День 6":
        style "replays_text"
        xcenter 0.432
        ycenter 0.885
    text "День 6":
        style "replays_text"
        xcenter 0.741
        ycenter 0.883
    imagebutton:
        auto get_image_7dl("gui/gallery/gallery_left_arrow_%s.png") xcenter 0.256 ycenter 0.923 
        action Show("replays_sl_cl_1_7dl", transition=Dissolve(0.2))
    imagebutton:
        auto get_image_7dl("gui/gallery/gallery_right_arrow_%s.png") xcenter 0.749 ycenter 0.923 
        action Show("replays_sl_cl_3_7dl", transition=Dissolve(0.2))
    if renpy.seen_label("alt_day6_sl_begin"):
        textbutton "alt_day6_sl_begin":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.187
            action Replay("alt_day6_sl_begin", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.187
    if renpy.seen_label("alt_day6_sl_morgen"):
        textbutton "alt_day6_sl_morgen":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day6_sl_morgen", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day6_sl_ba_quest1"):
        textbutton "alt_day6_sl_ba_quest1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day6_sl_ba_quest1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day6_sl_dinner"):
        textbutton "alt_day6_sl_dinner":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day6_sl_dinner", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
    if renpy.seen_label("alt_day6_sl_amp_list"):
        textbutton "alt_day6_sl_amp_list":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.382
            action Replay("alt_day6_sl_amp_list", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.382
    if renpy.seen_label("alt_day6_sl_amp_club"):
        textbutton "alt_day6_sl_amp_club":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.431
            action Replay("alt_day6_sl_amp_club", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.431
    if renpy.seen_label("alt_day6_sl_ambulance"):
        textbutton "alt_day6_sl_ambulance":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.479
            action Replay("alt_day6_sl_ambulance", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.479
    if renpy.seen_label("alt_day6_sl_concert"):
        textbutton "alt_day6_sl_concert":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.528
            action Replay("alt_day6_sl_concert", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.528
    if renpy.seen_label("alt_day6_sl_sh_tug"):
        textbutton "alt_day6_sl_sh_tug":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.577
            action Replay("alt_day6_sl_sh_tug", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.577
    if renpy.seen_label("alt_day6_sl_regular_arc"):
        textbutton "alt_day6_sl_regular_arc":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.625
            action Replay("alt_day6_sl_regular_arc", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.625
    if renpy.seen_label("alt_day6_sl_hala"):
        textbutton "alt_day6_sl_hala":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.674
            action Replay("alt_day6_sl_hala", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.674
    if renpy.seen_label("alt_day6_sl_dance"):
        textbutton "alt_day6_sl_dance":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.723
            action Replay("alt_day6_sl_dance", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.723
    if renpy.seen_label("alt_day6_sl_dancing"):
        textbutton "alt_day6_sl_dancing":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.771
            action Replay("alt_day6_sl_dancing", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.771
    if renpy.seen_label("alt_day6_sl_debarkader"):
        textbutton "alt_day6_sl_debarkader":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.187
            action Replay("alt_day6_sl_debarkader", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.187
    if renpy.seen_label("alt_day6_sl_true_route"):
        textbutton "alt_day6_sl_true_route":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.236
            action Replay("alt_day6_sl_true_route", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.236
    if renpy.seen_label("alt_day6_sl_cl_become_a_hero"):
        textbutton "alt_day6_sl_cl_become_a_hero":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.285
            action Replay("alt_day6_sl_cl_become_a_hero", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.285
    if renpy.seen_label("alt_day6_sl_intellectual"):
        textbutton "alt_day6_sl_intellectual":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.333
            action Replay("alt_day6_sl_intellectual", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.333

screen replays_sl_cl_3_7dl:
    tag menu
    text "День 7":
        style "replays_text"
        xcenter 0.432
        ycenter 0.885
    imagebutton:
        auto get_image_7dl("gui/gallery/gallery_left_arrow_%s.png") xcenter 0.256 ycenter 0.923 
        action Show("replays_sl_cl_2_7dl", transition=Dissolve(0.2))
    if renpy.seen_label("alt_day7_sl_fear"):
        textbutton "alt_day7_sl_fear":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.187
            action Replay("alt_day7_sl_fear", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.187
    if renpy.seen_label("alt_day7_sl_1996"):
        textbutton "alt_day7_sl_1996":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day7_sl_1996", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day7_sl_loop"):
        textbutton "alt_day7_sl_loop":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day7_sl_loop", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day7_sl_begin"):
        textbutton "alt_day7_sl_begin":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day7_sl_begin", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
    if renpy.seen_label("alt_day7_sl_breakfast"):
        textbutton "alt_day7_sl_breakfast":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.382
            action Replay("alt_day7_sl_breakfast", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.382
    if renpy.seen_label("alt_day7_sl_admins1"):
        textbutton "alt_day7_sl_admins1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.431
            action Replay("alt_day7_sl_admins1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.431
    if renpy.seen_label("alt_day7_sl_square1"):
        textbutton "alt_day7_sl_square1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.479
            action Replay("alt_day7_sl_square1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.479
    if renpy.seen_label("alt_day7_sl_beach"):
        textbutton "alt_day7_sl_beach":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.528
            action Replay("alt_day7_sl_beach", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.528
    if renpy.seen_label("alt_day7_sl_clubs1"):
        textbutton "alt_day7_sl_clubs1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.577
            action Replay("alt_day7_sl_clubs1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.577
    if renpy.seen_label("alt_day7_sl_dining_hall1"):
        textbutton "alt_day7_sl_dining_hall1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.625
            action Replay("alt_day7_sl_dining_hall1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.625
    if renpy.seen_label("alt_day7_sl_sport_area1"):
        textbutton "alt_day7_sl_sport_area1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.674
            action Replay("alt_day7_sl_sport_area1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.674
    if renpy.seen_label("alt_day7_sl_volleyball_alt1"):
        textbutton "alt_day7_sl_volleyball_alt1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.723
            action Replay("alt_day7_sl_volleyball_alt1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.723
    if renpy.seen_label("alt_day7_sl_estrade1"):
        textbutton "alt_day7_sl_estrade1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.771
            action Replay("alt_day7_sl_estrade1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.771
    if renpy.seen_label("alt_day7_sl_boat_station1"):
        textbutton "alt_day7_sl_boat_station1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.187
            action Replay("alt_day7_sl_boat_station1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.187
            
    if renpy.seen_label("alt_day7_sl_dinner"):
        textbutton "alt_day7_sl_dinner":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.236
            action Replay("alt_day7_sl_dinner", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.236
            
screen replays_dv_choice_7dl:
    textbutton "7дл":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.544
        ypos 0.187
        action [Hide("replays_route_choice_7dl", transition=Dissolve(0.2)), Hide("replays_dv_choice_7dl", transition=Dissolve(0.2)), Show("replays_dv_7dl_1_7dl", transition=Dissolve(0.2))]

    text "Классик":
        style "replays_text_locked"
        xpos 0.544
        ypos 0.236

    text "Диджей":
        style "replays_text_locked"
        xpos 0.544
        ypos 0.285

screen replays_dv_7dl_1_7dl:
    tag menu
    text "День 4":
        style "replays_text"
        xcenter 0.432
        ycenter 0.885
    text "День 5":
        style "replays_text"
        xcenter 0.741
        ycenter 0.883
    imagebutton:
        auto get_image_7dl("gui/gallery/gallery_right_arrow_%s.png") xcenter 0.749 ycenter 0.923 
        action Show("replays_dv_7dl_2_7dl", transition=Dissolve(0.2))
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.235
        ypos 0.187
        action [Hide("replays_dv_7dl_1_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]
    if renpy.seen_label("alt_day4_dv_7dl_begin"):
        textbutton "alt_day4_dv_7dl_begin":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day4_dv_7dl_begin", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day4_dv_7dl_forest"):
        textbutton "alt_day4_dv_7dl_forest":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day4_dv_7dl_forest", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day4_dv_7dl_silent_hour"):
        textbutton "alt_day4_dv_7dl_silent_hour":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day4_dv_7dl_silent_hour", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
    if renpy.seen_label("alt_day4_dv_7dl_roadtrip"):
        textbutton "alt_day4_dv_7dl_roadtrip":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.382
            action Replay("alt_day4_dv_7dl_roadtrip", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.382
    if renpy.seen_label("alt_day4_dv_7dl_alco"):
        textbutton "alt_day4_dv_7dl_alco":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.431
            action Replay("alt_day4_dv_7dl_alco", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.431
    if renpy.seen_label("alt_day4_dv_7dl_back_to_camp"):
        textbutton "alt_day4_dv_7dl_back_to_camp":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.479
            action Replay("alt_day4_dv_7dl_back_to_camp", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.479
    if renpy.seen_label("alt_day4_dv_7dl_append"):
        textbutton "alt_day4_dv_7dl_append":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.528
            action Replay("alt_day4_dv_7dl_append", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.528
    if renpy.seen_label("alt_day4_dv_7dl_aidpost"):
        textbutton "alt_day4_dv_7dl_aidpost":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.577
            action Replay("alt_day4_dv_7dl_aidpost", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.577
    if renpy.seen_label("alt_day4_dv_7dl_mt_aid"):
        textbutton "alt_day4_dv_7dl_mt_aid":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.625
            action Replay("alt_day4_dv_7dl_mt_aid", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.625
    if renpy.seen_label("alt_day4_dv_7dl_supper"):
        textbutton "alt_day4_dv_7dl_supper":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.674
            action Replay("alt_day4_dv_7dl_supper", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.674
    if renpy.seen_label("alt_day4_dv_7dl_sleeptime"):
        textbutton "alt_day4_dv_7dl_sleeptime":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.723
            action Replay("alt_day4_dv_7dl_sleeptime", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.723
    if renpy.seen_label("alt_day5_dv_7dl_alco_morning"):
        textbutton "alt_day5_dv_7dl_alco_morning":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.187
            action Replay("alt_day5_dv_7dl_alco_morning", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.187
    if renpy.seen_label("alt_day5_dv_7dl_begin"):
        textbutton "alt_day5_dv_7dl_begin":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.236
            action Replay("alt_day5_dv_7dl_begin", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.236
    if renpy.seen_label("alt_day5_dv_7dl_roadtrip"):
        textbutton "alt_day5_dv_7dl_roadtrip":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.285
            action Replay("alt_day5_dv_7dl_roadtrip", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.285
    if renpy.seen_label("alt_day5_dv_7dl_candle"):
        textbutton "alt_day5_dv_7dl_candle":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.333
            action Replay("alt_day5_dv_7dl_candle", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.333
    if renpy.seen_label("alt_day5_dv_7dl_dinner"):
        textbutton "alt_day5_dv_7dl_dinner":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.382
            action Replay("alt_day5_dv_7dl_dinner", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.382
    if renpy.seen_label("alt_day5_dv_7dl_lunch"):
        textbutton "alt_day5_dv_7dl_lunch":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.431
            action Replay("alt_day5_dv_7dl_lunch", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.431
    if renpy.seen_label("alt_day5_dv_7dl_supper"):
        textbutton "alt_day5_dv_7dl_supper":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.479
            action Replay("alt_day5_dv_7dl_supper", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.479
    if renpy.seen_label("alt_day5_dv_7dl_evening"):
        textbutton "alt_day5_dv_7dl_evening":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.528
            action Replay("alt_day5_dv_7dl_evening", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.528
    if renpy.seen_label("alt_day5_dv_7dl_night"):
        textbutton "alt_day5_dv_7dl_night":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.577
            action Replay("alt_day5_dv_7dl_night", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.577

screen replays_dv_7dl_2_7dl:
    tag menu
    text "День 6":
        style "replays_text"
        xcenter 0.432
        ycenter 0.885
    text "День 6":
        style "replays_text"
        xcenter 0.741
        ycenter 0.883
    imagebutton:
        auto get_image_7dl("gui/gallery/gallery_left_arrow_%s.png") xcenter 0.256 ycenter 0.923 
        action Show("replays_dv_7dl_1_7dl", transition=Dissolve(0.2))
    imagebutton:
        auto get_image_7dl("gui/gallery/gallery_right_arrow_%s.png") xcenter 0.749 ycenter 0.923 
        action Show("replays_dv_7dl_3_7dl", transition=Dissolve(0.2))
    if renpy.seen_label("alt_day6_dv_7dl_begin"):
        textbutton "alt_day6_dv_7dl_begin":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.187
            action Replay("alt_day6_dv_7dl_begin", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.187
    if renpy.seen_label("alt_day6_dv_7dl_breakfast"):
        textbutton "alt_day6_dv_7dl_breakfast":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day6_dv_7dl_breakfast", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day6_dv_7dl_dinner"):
        textbutton "alt_day6_dv_7dl_dinner":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day6_dv_7dl_dinner", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day6_dv_7dl_sl"):
        textbutton "alt_day6_dv_7dl_sl":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day6_dv_7dl_sl", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
    if renpy.seen_label("alt_day6_dv_7dl_sl_help"):
        textbutton "alt_day6_dv_7dl_sl_help":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.382
            action Replay("alt_day6_dv_7dl_sl_help", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.382
    if renpy.seen_label("alt_day6_dv_7dl_sl_help2"):
        textbutton "alt_day6_dv_7dl_sl_help2":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.431
            action Replay("alt_day6_dv_7dl_sl_help2", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.431
    if renpy.seen_label("alt_day6_dv_7dl_un"):
        textbutton "alt_day6_dv_7dl_un":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.479
            action Replay("alt_day6_dv_7dl_un", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.479
    if renpy.seen_label("alt_day6_dv_7dl_hl_failer2"):
        textbutton "alt_day6_dv_7dl_hl_failer2":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.528
            action Replay("alt_day6_dv_7dl_hl_failer2", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.528
    if renpy.seen_label("alt_day6_dv_7dl_concert"):
        textbutton "alt_day6_dv_7dl_concert":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.577
            action Replay("alt_day6_dv_7dl_concert", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.577
    if renpy.seen_label("alt_day6_dv_7dl_dance"):
        textbutton "alt_day6_dv_7dl_dance":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.625
            action Replay("alt_day6_dv_7dl_dance", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.625
    if renpy.seen_label("alt_day6_dv_7dl_escape_convince"):
        textbutton "alt_day6_dv_7dl_escape_convince":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.674
            action Replay("alt_day6_dv_7dl_escape_convince", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.674
    if renpy.seen_label("alt_day6_dv_7dl_sl_dancing"):
        textbutton "alt_day6_dv_7dl_sl_dancing":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.723
            action Replay("alt_day6_dv_7dl_sl_dancing", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.723
    if renpy.seen_label("alt_day6_dv_7dl_un_dancing"):
        textbutton "alt_day6_dv_7dl_un_dancing":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.771
            action Replay("alt_day6_dv_7dl_un_dancing", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.771
    if renpy.seen_label("alt_day6_dv_7dl_mt_dancing"):
        textbutton "alt_day6_dv_7dl_mt_dancing":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.187
            action Replay("alt_day6_dv_7dl_mt_dancing", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.187
    if renpy.seen_label("alt_day6_dv_7dl_dv_dancing"):
        textbutton "alt_day6_dv_7dl_dv_dancing":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.236
            action Replay("alt_day6_dv_7dl_dv_dancing", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.236
    if renpy.seen_label("alt_day6_dv_7dl_love_scene"):
        textbutton "alt_day6_dv_7dl_love_scene":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.285
            action Replay("alt_day6_dv_7dl_love_scene", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.285
    if renpy.seen_label("alt_day6_dv_7dl_non_love"):
        textbutton "alt_day6_dv_7dl_non_love":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.333
            action Replay("alt_day6_dv_7dl_non_love", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.333
    if renpy.seen_label("alt_day6_dv_7dl_sleeptime"):
        textbutton "alt_day6_dv_7dl_sleeptime":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.382
            action Replay("alt_day6_dv_7dl_sleeptime", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.382
    
screen replays_dv_7dl_3_7dl:
    tag menu
    text "День 7":
        style "replays_text"
        xcenter 0.432
        ycenter 0.885
    imagebutton:
        auto get_image_7dl("gui/gallery/gallery_left_arrow_%s.png") xcenter 0.256 ycenter 0.923 
        action Show("replays_dv_7dl_2_7dl", transition=Dissolve(0.2))
    if renpy.seen_label("alt_day7_dv_7dl_begin"):
        textbutton "alt_day7_dv_7dl_begin":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.187
            action Replay("alt_day7_dv_7dl_begin", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.187
    if renpy.seen_label("alt_day7_dv_7dl_router"):
        textbutton "alt_day7_dv_7dl_router":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day7_dv_7dl_router", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day7_dv_7dl_un"):
        textbutton "alt_day7_dv_7dl_un":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day7_dv_7dl_un", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day7_dv_7dl_sl"):
        textbutton "alt_day7_dv_7dl_sl":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day7_dv_7dl_sl", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
    if renpy.seen_label("alt_day7_dv_7dl_mt"):
        textbutton "alt_day7_dv_7dl_mt":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.382
            action Replay("alt_day7_dv_7dl_mt", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.382
    if renpy.seen_label("alt_day7_dv_7dl_dv"):
        textbutton "alt_day7_dv_7dl_dv":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.431
            action Replay("alt_day7_dv_7dl_dv", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.431
    if renpy.seen_label("alt_day7_dv_7dl_loki"):
        textbutton "alt_day7_dv_7dl_loki":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.479
            action Replay("alt_day7_dv_7dl_loki", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.479
    if renpy.seen_label("alt_day7_dv_7dl_bus"):
        textbutton "alt_day7_dv_7dl_bus":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.528
            action Replay("alt_day7_dv_7dl_bus", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.528
    if renpy.seen_label("alt_day7_dv_7dl_ending_router"):
        textbutton "alt_day7_dv_7dl_ending_router":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.577
            action Replay("alt_day7_dv_7dl_ending_router", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.577
    
screen replays_mi_choice_7dl:
    textbutton "7дл":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.544
        ypos 0.187
        action [Hide("replays_route_choice_7dl", transition=Dissolve(0.2)), Hide("replays_mi_choice_7dl", transition=Dissolve(0.2)), Show("replays_mi_7dl_1_7dl", transition=Dissolve(0.2))]

    text "Классик":
        style "replays_text_locked"
        xpos 0.544
        ypos 0.236
    textbutton "Диджей":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.544
        ypos 0.285
        action [Hide("replays_route_choice_7dl", transition=Dissolve(0.2)), Hide("replays_mi_choice_7dl", transition=Dissolve(0.2)), Show("replays_mi_dj_1_7dl", transition=Dissolve(0.2))]

screen replays_mi_7dl_1_7dl:
    tag menu
    text "День 4":
        style "replays_text"
        xcenter 0.432
        ycenter 0.885
    text "День 4":
        style "replays_text"
        xcenter 0.741
        ycenter 0.883
    imagebutton:
        auto get_image_7dl("gui/gallery/gallery_right_arrow_%s.png") xcenter 0.749 ycenter 0.923 
        action Show("replays_mi_7dl_2_7dl", transition=Dissolve(0.2))
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.235
        ypos 0.187
        action [Hide("replays_mi_7dl_1_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]
    if renpy.seen_label("alt_day4_mi_7dl_ch1"):
        textbutton "alt_day4_mi_7dl_ch1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day4_mi_7dl_ch1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day4_mi_7dl_ch2"):
        textbutton "alt_day4_mi_7dl_ch2":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day4_mi_7dl_ch2", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day4_mi_7dl_ch3"):
        textbutton "alt_day4_mi_7dl_ch3":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day4_mi_7dl_ch3", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
    if renpy.seen_label("alt_day4_mi_7dl_ch4"):
        textbutton "alt_day4_mi_7dl_ch4":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.382
            action Replay("alt_day4_mi_7dl_ch4", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.382
    if renpy.seen_label("alt_day4_mi_7dl_ch5a"):
        textbutton "alt_day4_mi_7dl_ch5a":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.431
            action Replay("alt_day4_mi_7dl_ch5a", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.431
    if renpy.seen_label("alt_day4_mi_7dl_ch5b"):
        textbutton "alt_day4_mi_7dl_ch5b":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.479
            action Replay("alt_day4_mi_7dl_ch5b", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.479
    if renpy.seen_label("alt_day4_mi_7dl_ch52"):
        textbutton "alt_day4_mi_7dl_ch52":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.528
            action Replay("alt_day4_mi_7dl_ch52", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.528
    if renpy.seen_label("alt_day4_mi_7dl_ch6"):
        textbutton "alt_day4_mi_7dl_ch6":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.577
            action Replay("alt_day4_mi_7dl_ch6", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.577
    if renpy.seen_label("alt_day4_mi_7dl_ch7"):
        textbutton "alt_day4_mi_7dl_ch7":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.625
            action Replay("alt_day4_mi_7dl_ch7", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.625
    if renpy.seen_label("alt_day4_mi_7dl_ch8a"):
        textbutton "alt_day4_mi_7dl_ch8a":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.674
            action Replay("alt_day4_mi_7dl_ch8a", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.674
    if renpy.seen_label("alt_day4_mi_7dl_ch81"):
        textbutton "alt_day4_mi_7dl_ch81":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.723
            action Replay("alt_day4_mi_7dl_ch81", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.723
    if renpy.seen_label("alt_day4_mi_7dl_ch82"):
        textbutton "alt_day4_mi_7dl_ch82":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.771
            action Replay("alt_day4_mi_7dl_ch82", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.771
    if renpy.seen_label("alt_day4_mi_7dl_ch83"):
        textbutton "alt_day4_mi_7dl_ch83":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.187
            action Replay("alt_day4_mi_7dl_ch83", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.187
    if renpy.seen_label("alt_day4_mi_7dl_ch8b"):
        textbutton "alt_day4_mi_7dl_ch8b":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.236
            action Replay("alt_day4_mi_7dl_ch8b", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.236

screen replays_mi_7dl_2_7dl:
    tag menu
    text "День 5":
        style "replays_text"
        xcenter 0.432
        ycenter 0.885
    text "День 6":
        style "replays_text"
        xcenter 0.741
        ycenter 0.883
    imagebutton:
        auto get_image_7dl("gui/gallery/gallery_left_arrow_%s.png") xcenter 0.256 ycenter 0.923 
        action Show("replays_mi_7dl_1_7dl", transition=Dissolve(0.2))
    imagebutton:
        auto get_image_7dl("gui/gallery/gallery_right_arrow_%s.png") xcenter 0.749 ycenter 0.923 
        action Show("replays_mi_7dl_3_7dl", transition=Dissolve(0.2))
    if renpy.seen_label("alt_day5_mi_7dl_rain_2gether"):
        textbutton "alt_day5_mi_7dl_rain_2gether":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.187
            action Replay("alt_day5_mi_7dl_rain_2gether", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.187
    if renpy.seen_label("alt_day5_mi_7dl_morning"):
        textbutton "alt_day5_mi_7dl_morning":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day5_mi_7dl_morning", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day5_mi_7dl_dinner"):
        textbutton "alt_day5_mi_7dl_dinner":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day5_mi_7dl_dinner", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day5_mi_7dl_router"):
        textbutton "alt_day5_mi_7dl_router":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day5_mi_7dl_router", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
    if renpy.seen_label("alt_day5_mi_7dl_lost"):
        textbutton "alt_day5_mi_7dl_lost":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.382
            action Replay("alt_day5_mi_7dl_lost", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.382
    if renpy.seen_label("alt_day5_mi_7dl_hn"):
        textbutton "alt_day5_mi_7dl_hn":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.431
            action Replay("alt_day5_mi_7dl_hn", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.431
    if renpy.seen_label("alt_day5_mi_7dl_branch"):
        textbutton "alt_day5_mi_7dl_branch":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.479
            action Replay("alt_day5_mi_7dl_branch", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.479
    if renpy.seen_label("alt_day5_mi_7dl_potato"):
        textbutton "alt_day5_mi_7dl_potato":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.528
            action Replay("alt_day5_mi_7dl_potato", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.528
    if renpy.seen_label("alt_day5_mi_7dl_camp_cleance"):
        textbutton "alt_day5_mi_7dl_camp_cleance":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.577
            action Replay("alt_day5_mi_7dl_camp_cleance", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.577
    if renpy.seen_label("alt_day5_mi_7dl_firecamp"):
        textbutton "alt_day5_mi_7dl_firecamp":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.625
            action Replay("alt_day5_mi_7dl_firecamp", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.625
    if renpy.seen_label("alt_day5_mi_7dl_goodnight"):
        textbutton "alt_day5_mi_7dl_goodnight":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.674
            action Replay("alt_day5_mi_7dl_goodnight", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.674
    if renpy.seen_label("alt_day6_mi_7dl_wakeup"):
        textbutton "alt_day6_mi_7dl_wakeup":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.187
            action Replay("alt_day6_mi_7dl_wakeup", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.187
    if renpy.seen_label("alt_day6_mi_7dl_soul"):
        textbutton "alt_day6_mi_7dl_soul":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.236
            action Replay("alt_day6_mi_7dl_soul", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.236
    if renpy.seen_label("alt_day6_mi_7dl_dinner"):
        textbutton "alt_day6_mi_7dl_dinner":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.285
            action Replay("alt_day6_mi_7dl_dinner", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.285
    if renpy.seen_label("alt_day6_mi_7dl_soul_day"):
        textbutton "alt_day6_mi_7dl_soul_day":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.333
            action Replay("alt_day6_mi_7dl_soul_day", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.333
    if renpy.seen_label("alt_day6_mi_7dl_miku_sakishita"):
        textbutton "alt_day6_mi_7dl_miku_sakishita":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.382
            action Replay("alt_day6_mi_7dl_miku_sakishita", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.382
    if renpy.seen_label("alt_day6_mi_7dl_miku_farewell_finale"):
        textbutton "alt_day6_mi_7dl_miku_farewell_finale":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.431
            action Replay("alt_day6_mi_7dl_miku_farewell_finale", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.431
    if renpy.seen_label("alt_day6_mi_7dl_miku_farewell_soul"):
        textbutton "alt_day6_mi_7dl_miku_farewell_soul":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.479
            action Replay("alt_day6_mi_7dl_miku_farewell_soul", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.479
    if renpy.seen_label("alt_day6_mi_7dl_star"):
        textbutton "alt_day6_mi_7dl_star":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.528
            action Replay("alt_day6_mi_7dl_star", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.528
    if renpy.seen_label("alt_day6_mi_7dl_star_day"):
        textbutton "alt_day6_mi_7dl_star_day":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.577
            action Replay("alt_day6_mi_7dl_star_day", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.577
    if renpy.seen_label("alt_day6_mi_7dl_miku_farewell_star"):
        textbutton "alt_day6_mi_7dl_miku_farewell_star":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.625
            action Replay("alt_day6_mi_7dl_miku_farewell_star", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.625
    if renpy.seen_label("alt_day6_mi_7dl_human"):
        textbutton "alt_day6_mi_7dl_human":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.674
            action Replay("alt_day6_mi_7dl_human", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.674
    if renpy.seen_label("alt_day6_mi_7dl_human_day"):
        textbutton "alt_day6_mi_7dl_human_day":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.723
            action Replay("alt_day6_mi_7dl_human_day", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.723
    if renpy.seen_label("alt_day6_mi_7dl_discoteque"):
        textbutton "alt_day6_mi_7dl_discoteque":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.771
            action Replay("alt_day6_mi_7dl_discoteque", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.771
    
screen replays_mi_7dl_3_7dl:
    tag menu
    text "День 7":
        style "replays_text"
        xcenter 0.432
        ycenter 0.885
    imagebutton:
        auto get_image_7dl("gui/gallery/gallery_left_arrow_%s.png") xcenter 0.256 ycenter 0.923 
        action Show("replays_mi_7dl_2_7dl", transition=Dissolve(0.2))
    if renpy.seen_label("alt_day7_mi_7dl_begin"):
        textbutton "alt_day7_mi_7dl_begin":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.187
            action Replay("alt_day7_mi_7dl_begin", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.187
    if renpy.seen_label("alt_day7_mi_7dl_wakeup"):
        textbutton "alt_day7_mi_7dl_wakeup":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day7_mi_7dl_wakeup", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day7_mi_7dl_packing"):
        textbutton "alt_day7_mi_7dl_packing":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day7_mi_7dl_packing", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day7_mi_7dl_departure_lone"):
        textbutton "alt_day7_mi_7dl_departure_lone":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day7_mi_7dl_departure_lone", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
    if renpy.seen_label("alt_day7_mi_7dl_departure_a2th"):
        textbutton "alt_day7_mi_7dl_departure_a2th":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.382
            action Replay("alt_day7_mi_7dl_departure_a2th", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.382
    
screen replays_mi_dj_1_7dl:
    tag menu
    text "День 4":
        style "replays_text"
        xcenter 0.432
        ycenter 0.885
    text "День 4":
        style "replays_text"
        xcenter 0.741
        ycenter 0.883
    imagebutton:
        auto get_image_7dl("gui/gallery/gallery_right_arrow_%s.png") xcenter 0.749 ycenter 0.923 
        action Show("replays_mi_dj_2_7dl", transition=Dissolve(0.2))
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.235
        ypos 0.187
        action [Hide("replays_mi_dj_1_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]
    if renpy.seen_label("alt_day4_mi_dj_begin"):
        textbutton "alt_day4_mi_dj_begin":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day4_mi_dj_begin", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day4_mi_dj_hedg_hunt"):
        textbutton "alt_day4_mi_dj_hedg_hunt":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day4_mi_dj_hedg_hunt", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day4_mi_dj_morning"):
        textbutton "alt_day4_mi_dj_morning":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day4_mi_dj_morning", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
    if renpy.seen_label("alt_day4_mi_dj_day"):
        textbutton "alt_day4_mi_dj_day":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.382
            action Replay("alt_day4_mi_dj_day", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.382
    if renpy.seen_label("alt_day4_mi_dj_radio"):
        textbutton "alt_day4_mi_dj_radio":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.431
            action Replay("alt_day4_mi_dj_radio", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.431
    if renpy.seen_label("alt_day4_mi_dj_cleaning"):
        textbutton "alt_day4_mi_dj_cleaning":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.479
            action Replay("alt_day4_mi_dj_cleaning", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.479
    if renpy.seen_label("alt_day4_mi_dj_dinner"):
        textbutton "alt_day4_mi_dj_dinner":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.528
            action Replay("alt_day4_mi_dj_dinner", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.528
    if renpy.seen_label("alt_day4_mi_dj_dinner2"):
        textbutton "alt_day4_mi_dj_dinner2":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.577
            action Replay("alt_day4_mi_dj_dinner2", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.577
    if renpy.seen_label("alt_day4_mi_dj_repetition"):
        textbutton "alt_day4_mi_dj_repetition":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.625
            action Replay("alt_day4_mi_dj_repetition", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.625
    if renpy.seen_label("alt_day4_mi_dj_supper"):
        textbutton "alt_day4_mi_dj_supper":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.674
            action Replay("alt_day4_mi_dj_supper", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.674
    if renpy.seen_label("alt_day4_mi_dj_evening"):
        textbutton "alt_day4_mi_dj_evening":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.723
            action Replay("alt_day4_mi_dj_evening", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.723
    if renpy.seen_label("alt_day4_mi_dj_night"):
        textbutton "alt_day4_mi_dj_night":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.771
            action Replay("alt_day4_mi_dj_night", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.771
    if renpy.seen_label("alt_day4_mi_dj_sleeptime"):
        textbutton "alt_day4_mi_dj_sleeptime":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.187
            action Replay("alt_day4_mi_dj_sleeptime", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.187

screen replays_mi_dj_2_7dl:
    tag menu
    text "День 5":
        style "replays_text"
        xcenter 0.432
        ycenter 0.885
    text "День 5":
        style "replays_text"
        xcenter 0.741
        ycenter 0.883
    imagebutton:
        auto get_image_7dl("gui/gallery/gallery_left_arrow_%s.png") xcenter 0.256 ycenter 0.923 
        action Show("replays_mi_dj_1_7dl", transition=Dissolve(0.2))
    imagebutton:
        auto get_image_7dl("gui/gallery/gallery_right_arrow_%s.png") xcenter 0.749 ycenter 0.923 
        action Show("replays_mi_dj_3_7dl", transition=Dissolve(0.2))
    if renpy.seen_label("alt_day5_mi_dj_begin"):
        textbutton "alt_day5_mi_dj_begin":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.187
            action Replay("alt_day5_mi_dj_begin", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.187
    if renpy.seen_label("alt_day5_mi_dj_cinema"):
        textbutton "alt_day5_mi_dj_cinema":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day5_mi_dj_cinema", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day5_mi_dj_dinner"):
        textbutton "alt_day5_mi_dj_dinner":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day5_mi_dj_dinner", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day5_mi_dj_music_club1"):
        textbutton "alt_day5_mi_dj_music_club1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day5_mi_dj_music_club1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
    if renpy.seen_label("alt_day5_mi_dj_clubs1"):
        textbutton "alt_day5_mi_dj_clubs1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.382
            action Replay("alt_day5_mi_dj_clubs1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.382
    if renpy.seen_label("alt_day5_mi_dj_camp_entrance1"):
        textbutton "alt_day5_mi_dj_camp_entrance1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.431
            action Replay("alt_day5_mi_dj_camp_entrance1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.431
    if renpy.seen_label("alt_day5_mi_dj_un_mi_house1"):
        textbutton "alt_day5_mi_dj_un_mi_house1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.479
            action Replay("alt_day5_mi_dj_un_mi_house1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.479
    if renpy.seen_label("alt_day5_mi_dj_estrade1"):
        textbutton "alt_day5_mi_dj_estrade1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.528
            action Replay("alt_day5_mi_dj_estrade1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.528
    if renpy.seen_label("alt_day5_mi_dj_supper"):
        textbutton "alt_day5_mi_dj_supper":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.577
            action Replay("alt_day5_mi_dj_supper", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.577
    if renpy.seen_label("alt_day5_mi_dj_voyeur_2"):
        textbutton "alt_day5_mi_dj_voyeur_2":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.625
            action Replay("alt_day5_mi_dj_voyeur_2", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.625
    if renpy.seen_label("alt_day5_mi_dj_voyeur_3"):
        textbutton "alt_day5_mi_dj_voyeur_3":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.674
            action Replay("alt_day5_mi_dj_voyeur_3", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.674
    if renpy.seen_label("alt_day5_mi_dj_voyeur_4"):
        textbutton "alt_day5_mi_dj_voyeur_4":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.723
            action Replay("alt_day5_mi_dj_voyeur_4", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.723
    if renpy.seen_label("alt_day5_mi_dj_late_evening"):
        textbutton "alt_day5_mi_dj_late_evening":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.771
            action Replay("alt_day5_mi_dj_late_evening", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.771
    if renpy.seen_label("alt_day5_mi_dj_evening_club1"):
        textbutton "alt_day5_mi_dj_evening_club1":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.187
            action Replay("alt_day5_mi_dj_evening_club1", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.187
    if renpy.seen_label("alt_day5_mi_dj_evening_club2"):
        textbutton "alt_day5_mi_dj_evening_club2":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.236
            action Replay("alt_day5_mi_dj_evening_club2", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.236
    if renpy.seen_label("alt_day5_mi_dj_sleeptime"):
        textbutton "alt_day5_mi_dj_sleeptime":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.285
            action Replay("alt_day5_mi_dj_sleeptime", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.285
    
screen replays_mi_dj_3_7dl:
    tag menu
    text "День 6":
        style "replays_text"
        xcenter 0.432
        ycenter 0.885
    text "День 6":
        style "replays_text"
        xcenter 0.741
        ycenter 0.883
    imagebutton:
        auto get_image_7dl("gui/gallery/gallery_left_arrow_%s.png") xcenter 0.256 ycenter 0.923 
        action Show("replays_mi_dj_2_7dl", transition=Dissolve(0.2))
    imagebutton:
        auto get_image_7dl("gui/gallery/gallery_right_arrow_%s.png") xcenter 0.749 ycenter 0.923 
        action Show("replays_mi_dj_4_7dl", transition=Dissolve(0.2))
    if renpy.seen_label("alt_day6_mi_dj_good"):
        textbutton "alt_day6_mi_dj_good":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.187
            action Replay("alt_day6_mi_dj_good", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.187
    if renpy.seen_label("alt_day6_mi_dj_neutral"):
        textbutton "alt_day6_mi_dj_neutral":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day6_mi_dj_neutral", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day6_mi_dj_radio"):
        textbutton "alt_day6_mi_dj_radio":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day6_mi_dj_radio", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day6_mi_dj_dinner"):
        textbutton "alt_day6_mi_dj_dinner":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day6_mi_dj_dinner", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
    if renpy.seen_label("alt_day6_mi_dj_rendezvous"):
        textbutton "alt_day6_mi_dj_rendezvous":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.382
            action Replay("alt_day6_mi_dj_rendezvous", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.382
    if renpy.seen_label("alt_day6_mi_dj_forgiveness"):
        textbutton "alt_day6_mi_dj_forgiveness":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.431
            action Replay("alt_day6_mi_dj_forgiveness", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.431
    if renpy.seen_label("alt_day6_mi_dj_tale"):
        textbutton "alt_day6_mi_dj_tale":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.479
            action Replay("alt_day6_mi_dj_tale", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.479
    if renpy.seen_label("alt_day6_mi_dj_plain"):
        textbutton "alt_day6_mi_dj_plain":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.528
            action Replay("alt_day6_mi_dj_plain", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.528
    if renpy.seen_label("alt_day6_mi_dj_concert"):
        textbutton "alt_day6_mi_dj_concert":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.577
            action Replay("alt_day6_mi_dj_concert", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.577
    if renpy.seen_label("alt_day6_mi_dj_reject"):
        textbutton "alt_day6_mi_dj_reject":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.625
            action Replay("alt_day6_mi_dj_reject", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.625
    if renpy.seen_label("alt_day6_mi_dj_newswall"):
        textbutton "alt_day6_mi_dj_newswall":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.674
            action Replay("alt_day6_mi_dj_newswall", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.674
    if renpy.seen_label("alt_day6_mi_dj_late_supper"):
        textbutton "alt_day6_mi_dj_late_supper":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.723
            action Replay("alt_day6_mi_dj_late_supper", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.723
    if renpy.seen_label("alt_day6_mi_dj_sonic"):
        textbutton "alt_day6_mi_dj_sonic":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.771
            action Replay("alt_day6_mi_dj_sonic", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.771
    if renpy.seen_label("alt_day6_mi_dj_supper"):
        textbutton "alt_day6_mi_dj_supper":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.187
            action Replay("alt_day6_mi_dj_supper", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.187
    if renpy.seen_label("alt_day6_mi_dj_discotheque"):
        textbutton "alt_day6_mi_dj_discotheque":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.236
            action Replay("alt_day6_mi_dj_discotheque", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.236
    if renpy.seen_label("alt_day6_mi_dj_first_dance"):
        textbutton "alt_day6_mi_dj_first_dance":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.285
            action Replay("alt_day6_mi_dj_first_dance", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.285
    if renpy.seen_label("alt_day6_mi_dj_second_dance"):
        textbutton "alt_day6_mi_dj_second_dance":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.333
            action Replay("alt_day6_mi_dj_second_dance", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.333
    if renpy.seen_label("alt_day6_mi_dj_dance2_success"):
        textbutton "alt_day6_mi_dj_dance2_success":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.382
            action Replay("alt_day6_mi_dj_dance2_success", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.382
    if renpy.seen_label("alt_day6_mi_dj_dance2_fail"):
        textbutton "alt_day6_mi_dj_dance2_fail":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.431
            action Replay("alt_day6_mi_dj_dance2_fail", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.431
    
screen replays_mi_dj_4_7dl:
    tag menu
    text "День 7":
        style "replays_text"
        xcenter 0.432
        ycenter 0.885
    imagebutton:
        auto get_image_7dl("gui/gallery/gallery_left_arrow_%s.png") xcenter 0.256 ycenter 0.923 
        action Show("replays_mi_dj_3_7dl", transition=Dissolve(0.2))
    if renpy.seen_label("alt_day7_mi_dj_together"):
        textbutton "alt_day7_mi_dj_together":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.187
            action Replay("alt_day7_mi_dj_together", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.187
    if renpy.seen_label("alt_day7_mi_dj_alone"):
        textbutton "alt_day7_mi_dj_alone":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day7_mi_dj_alone", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day7_mi_dj_badfeel"):
        textbutton "alt_day7_mi_dj_badfeel":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day7_mi_dj_badfeel", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day7_mi_dj_preparations"):
        textbutton "alt_day7_mi_dj_preparations":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day7_mi_dj_preparations", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
    if renpy.seen_label("alt_day7_mi_dj_epilogue_frost"):
        textbutton "alt_day7_mi_dj_epilogue_frost":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.382
            action Replay("alt_day7_mi_dj_epilogue_frost", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.382
    if renpy.seen_label("alt_day7_mi_dj_good"):
        textbutton "alt_day7_mi_dj_good":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.431
            action Replay("alt_day7_mi_dj_good", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.431
    
screen replays_us_1_7dl:
    tag menu
    text "День 6":
        style "replays_text"
        xcenter 0.432
        ycenter 0.885
    text "День 6":
        style "replays_text"
        xcenter 0.741
        ycenter 0.883
    imagebutton:
        auto get_image_7dl("gui/gallery/gallery_right_arrow_%s.png") xcenter 0.749 ycenter 0.923 
        action Show("replays_us_2_7dl", transition=Dissolve(0.2))
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.235
        ypos 0.187
        action [Hide("replays_us_1_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]
    if renpy.seen_label("alt_day6_us_px_begin"):
        textbutton "alt_day6_us_px_begin":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day6_us_px_begin", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day6_us_7dl_begin"):
        textbutton "alt_day6_us_7dl_begin":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day6_us_7dl_begin", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day6_us_7dl_exercises"):
        textbutton "alt_day6_us_7dl_exercises":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day6_us_7dl_exercises", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
    if renpy.seen_label("alt_day6_us_7dl_breakfast"):
        textbutton "alt_day6_us_7dl_breakfast":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.382
            action Replay("alt_day6_us_7dl_breakfast", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.382
    if renpy.seen_label("alt_day6_us_px_carrier"):
        textbutton "alt_day6_us_px_carrier":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.431
            action Replay("alt_day6_us_px_carrier", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.431
    if renpy.seen_label("alt_day6_us_px_dinner"):
        textbutton "alt_day6_us_px_dinner":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.479
            action Replay("alt_day6_us_px_dinner", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.479
    if renpy.seen_label("alt_day6_us_px_Lena"):
        textbutton "alt_day6_us_px_Lena":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.528
            action Replay("alt_day6_us_px_Lena", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.528
    if renpy.seen_label("alt_day6_us_px_party_sl"):
        textbutton "alt_day6_us_px_party_sl":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.577
            action Replay("alt_day6_us_px_party_sl", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.577
    if renpy.seen_label("alt_day6_us_px_far_gate"):
        textbutton "alt_day6_us_px_far_gate":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.625
            action Replay("alt_day6_us_px_far_gate", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.625
    if renpy.seen_label("alt_day6_us_7dl_concert"):
        textbutton "alt_day6_us_7dl_concert":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.674
            action Replay("alt_day6_us_7dl_concert", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.674
    if renpy.seen_label("alt_day6_us_7dl_helping"):
        textbutton "alt_day6_us_7dl_helping":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.723
            action Replay("alt_day6_us_7dl_helping", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.723
    if renpy.seen_label("alt_day6_us_7dl_preps"):
        textbutton "alt_day6_us_7dl_preps":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.771
            action Replay("alt_day6_us_7dl_preps", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.771
    if renpy.seen_label("alt_day6_us_7dl_warehouse"):
        textbutton "alt_day6_us_7dl_warehouse":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.187
            action Replay("alt_day6_us_7dl_warehouse", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.187
    if renpy.seen_label("alt_day6_us_7dl_un_met"):
        textbutton "alt_day6_us_7dl_un_met":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.236
            action Replay("alt_day6_us_7dl_un_met", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.236
    if renpy.seen_label("alt_day6_us_7dl_dinner"):
        textbutton "alt_day6_us_7dl_dinner":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.285
            action Replay("alt_day6_us_7dl_dinner", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.285
    if renpy.seen_label("alt_day6_us_7dl_soundcheck"):
        textbutton "alt_day6_us_7dl_soundcheck":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.333
            action Replay("alt_day6_us_7dl_soundcheck", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.333
    if renpy.seen_label("alt_day6_us_7dl_button"):
        textbutton "alt_day6_us_7dl_button":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.382
            action Replay("alt_day6_us_7dl_button", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.382
    if renpy.seen_label("alt_day6_us_7dl_rendezvous"):
        textbutton "alt_day6_us_7dl_rendezvous":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.431
            action Replay("alt_day6_us_7dl_rendezvous", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.431
    if renpy.seen_label("alt_day6_us_7dl_supper"):
        textbutton "alt_day6_us_7dl_supper":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.479
            action Replay("alt_day6_us_7dl_supper", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.479
    if renpy.seen_label("alt_day6_us_7dl_disco"):
        textbutton "alt_day6_us_7dl_disco":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.528
            action Replay("alt_day6_us_7dl_disco", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.528
    if renpy.seen_label("alt_day6_us_7dl_tea"):
        textbutton "alt_day6_us_7dl_tea":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.577
            action Replay("alt_day6_us_7dl_tea", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.577
    if renpy.seen_label("alt_day6_us_px_afterwords"):
        textbutton "alt_day6_us_px_afterwords":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.625
            action Replay("alt_day6_us_px_afterwords", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.625
    if renpy.seen_label("alt_day6_us_7dl_sleeptime"):
        textbutton "alt_day6_us_7dl_sleeptime":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.674
            action Replay("alt_day6_us_7dl_sleeptime", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.674

screen replays_us_2_7dl:
    tag menu
    text "День 7":
        style "replays_text"
        xcenter 0.432
        ycenter 0.885
    imagebutton:
        auto get_image_7dl("gui/gallery/gallery_left_arrow_%s.png") xcenter 0.256 ycenter 0.923 
        action Show("replays_us_1_7dl", transition=Dissolve(0.2))
    if renpy.seen_label("alt_day7_us_7dl_begin"):
        textbutton "alt_day7_us_7dl_begin":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.187
            action Replay("alt_day7_us_7dl_begin", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.187
    if renpy.seen_label("alt_day7_us_7dl_breakfast"):
        textbutton "alt_day7_us_7dl_breakfast":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day7_us_7dl_breakfast", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day7_us_px_escape"):
        textbutton "alt_day7_us_px_escape":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day7_us_px_escape", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day7_us_px_bus"):
        textbutton "alt_day7_us_px_bus":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day7_us_px_bus", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
    if renpy.seen_label("alt_day7_us_px_wastelands"):
        textbutton "alt_day7_us_px_wastelands":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.382
            action Replay("alt_day7_us_px_wastelands", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.382
    if renpy.seen_label("alt_day7_us_px_mourning"):
        textbutton "alt_day7_us_px_mourning":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.431
            action Replay("alt_day7_us_px_mourning", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.431
    if renpy.seen_label("alt_day7_us_7dl_rendezvous2"):
        textbutton "alt_day7_us_7dl_rendezvous2":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.479
            action Replay("alt_day7_us_7dl_rendezvous2", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.479
    if renpy.seen_label("alt_day7_us_7dl_packing"):
        textbutton "alt_day7_us_7dl_packing":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.528
            action Replay("alt_day7_us_7dl_packing", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.528
    if renpy.seen_label("alt_day7_us_7dl_leaving"):
        textbutton "alt_day7_us_7dl_leaving":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.577
            action Replay("alt_day7_us_7dl_leaving", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.577
    if renpy.seen_label("alt_day7_us_7dl_wakeup"):
        textbutton "alt_day7_us_7dl_wakeup":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.625
            action Replay("alt_day7_us_7dl_wakeup", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.625
    
screen replays_mt_1_7dl:
    tag menu
    text "День 6":
        style "replays_text"
        xcenter 0.432
        ycenter 0.885
    text "День 6":
        style "replays_text"
        xcenter 0.741
        ycenter 0.883
    imagebutton:
        auto get_image_7dl("gui/gallery/gallery_right_arrow_%s.png") xcenter 0.749 ycenter 0.923 
        action Show("replays_mt_2_7dl", transition=Dissolve(0.2))
    textbutton "...":
        style "log_button"
        text_style "replays_textbutton"
        xpos 0.235
        ypos 0.187
        action [Hide("replays_mt_1_7dl", transition=Dissolve(0.2)), Show("replays_route_choice_7dl", transition=Dissolve(0.2))]
    if renpy.seen_label("alt_day6_mt_7dl_begin"):
        textbutton "alt_day6_mt_7dl_begin":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day6_mt_7dl_begin", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day6_mt_7dl_morning"):
        textbutton "alt_day6_mt_7dl_morning":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day6_mt_7dl_morning", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day6_mt_7dl_dv_morning"):
        textbutton "alt_day6_mt_7dl_dv_morning":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day6_mt_7dl_dv_morning", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
    if renpy.seen_label("alt_day6_mt_7dl_un_morning"):
        textbutton "alt_day6_mt_7dl_un_morning":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.382
            action Replay("alt_day6_mt_7dl_un_morning", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.382
    if renpy.seen_label("alt_day6_mt_7dl_retail"):
        textbutton "alt_day6_mt_7dl_retail":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.431
            action Replay("alt_day6_mt_7dl_retail", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.431
    if renpy.seen_label("alt_day6_mt_7dl_retail_px"):
        textbutton "alt_day6_mt_7dl_retail_px":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.479
            action Replay("alt_day6_mt_7dl_retail_px", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.479
    if renpy.seen_label("alt_day6_mt_7dl_declaration0"):
        textbutton "alt_day6_mt_7dl_declaration0":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.528
            action Replay("alt_day6_mt_7dl_declaration0", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.528
    if renpy.seen_label("alt_day6_mt_7dl_memento"):
        textbutton "alt_day6_mt_7dl_memento":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.577
            action Replay("alt_day6_mt_7dl_memento", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.577
    if renpy.seen_label("alt_day6_mt_7dl_retail_vg"):
        textbutton "alt_day6_mt_7dl_retail_vg":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.625
            action Replay("alt_day6_mt_7dl_retail_vg", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.625
    if renpy.seen_label("alt_day6_mt_7dl_forgive"):
        textbutton "alt_day6_mt_7dl_forgive":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.674
            action Replay("alt_day6_mt_7dl_forgive", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.674
    if renpy.seen_label("alt_day6_mt_7dl_diary3"):
        textbutton "alt_day6_mt_7dl_diary3":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.723
            action Replay("alt_day6_mt_7dl_diary3", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.723
    if renpy.seen_label("alt_day6_mt_7dl_dinner"):
        textbutton "alt_day6_mt_7dl_dinner":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.771
            action Replay("alt_day6_mt_7dl_dinner", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.771
    if renpy.seen_label("alt_day6_mt_7dl_concert"):
        textbutton "alt_day6_mt_7dl_concert":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.187
            action Replay("alt_day6_mt_7dl_concert", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.187
    if renpy.seen_label("alt_day6_mt_7dl_supper"):
        textbutton "alt_day6_mt_7dl_supper":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.236
            action Replay("alt_day6_mt_7dl_supper", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.236
    if renpy.seen_label("alt_day6_mt_7dl_choice"):
        textbutton "alt_day6_mt_7dl_choice":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.285
            action Replay("alt_day6_mt_7dl_choice", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.285
    if renpy.seen_label("alt_day6_mt_7dl_catha"):
        textbutton "alt_day6_mt_7dl_catha":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.333
            action Replay("alt_day6_mt_7dl_catha", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.333
    if renpy.seen_label("alt_day6_mt_7dl_declare"):
        textbutton "alt_day6_mt_7dl_declare":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.382
            action Replay("alt_day6_mt_7dl_declare", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.382
    if renpy.seen_label("alt_day6_mt_7dl_nighttime"):
        textbutton "alt_day6_mt_7dl_nighttime":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.544
            ypos 0.431
            action Replay("alt_day6_mt_7dl_nighttime", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.544
            ypos 0.431

screen replays_mt_2_7dl:
    tag menu
    text "День 7":
        style "replays_text"
        xcenter 0.432
        ycenter 0.885
    imagebutton:
        auto get_image_7dl("gui/gallery/gallery_left_arrow_%s.png") xcenter 0.256 ycenter 0.923 
        action Show("replays_mt_1_7dl", transition=Dissolve(0.2))
    if renpy.seen_label("alt_day7_mt_7dl_begin"):
        textbutton "alt_day7_mt_7dl_begin":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.187
            action Replay("alt_day7_mt_7dl_begin", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.187
    if renpy.seen_label("alt_day7_mt_7dl_morning"):
        textbutton "alt_day7_mt_7dl_morning":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.236
            action Replay("alt_day7_mt_7dl_morning", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.236
    if renpy.seen_label("alt_day7_mt_7dl_conclude"):
        textbutton "alt_day7_mt_7dl_conclude":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.285
            action Replay("alt_day7_mt_7dl_conclude", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.285
    if renpy.seen_label("alt_day7_mt_7dl_byes"):
        textbutton "alt_day7_mt_7dl_byes":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.333
            action Replay("alt_day7_mt_7dl_byes", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.333
    if renpy.seen_label("alt_day7_mt_7dl_dv_bye"):
        textbutton "alt_day7_mt_7dl_dv_bye":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.382
            action Replay("alt_day7_mt_7dl_dv_bye", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.382
    if renpy.seen_label("alt_day7_mt_7dl_un_fz_bye"):
        textbutton "alt_day7_mt_7dl_un_fz_bye":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.431
            action Replay("alt_day7_mt_7dl_un_fz_bye", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.431
    if renpy.seen_label("alt_day7_mt_7dl_un_bye"):
        textbutton "alt_day7_mt_7dl_un_bye":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.479
            action Replay("alt_day7_mt_7dl_un_bye", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.479
    if renpy.seen_label("alt_day7_mt_7dl_departure"):
        textbutton "alt_day7_mt_7dl_departure":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.528
            action Replay("alt_day7_mt_7dl_departure", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.528
    if renpy.seen_label("alt_day7_mt_7dl_loopthru"):
        textbutton "alt_day7_mt_7dl_loopthru":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.577
            action Replay("alt_day7_mt_7dl_loopthru", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.577
    if renpy.seen_label("alt_day7_mt_7dl_loopback"):
        textbutton "alt_day7_mt_7dl_loopback":
            style "log_button"
            text_style "replays_textbutton"
            xpos 0.235
            ypos 0.625
            action Replay("alt_day7_mt_7dl_loopback", scope={"alt_replay_on" : "True"}, locked=None)
    else:
        text "?????":
            style "replays_text_locked"
            xpos 0.235
            ypos 0.625
            