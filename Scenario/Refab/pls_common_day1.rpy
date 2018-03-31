label alt_day0_prologue:
    $ renpy.pause(3)
    scene black
    play music music_list["drown"] fadein 3
    $ plthr = u"Выбор"
    $ alt_chapter0()
    with fade
    show spill_red with dspr
    $ renpy.pause(2, hard=True)
    show spill_gray with dspr
    $ renpy.pause(2, hard=True)
    $ timeskip0 = "Я с трудом вспоминаю, \n с чего всё началось…"
    if persistent.dv_7dl_good_ussr:
        show acm_a
    if persistent.un_7dl_good_rf or persistent.un_7dl_good_ussr:
        show acm_l
    if persistent.mi_7dl_good_human or persistent.mi_7dl_good_star:
        show acm_m
    if persistent.mt_7dl_good:
        show acm_o
    if persistent.sl_7dl_good_ussr:
        show acm_s
    if persistent.us_7dl_good:
        show acm_u
    with dissolve2
    pause(3)
    if alt_day_binder == 1:
        show cg d7_trio_7dl with flash
        $ renpy.pause(.4)
        scene black with fade2
        show alt_credits timeskip_come with dissolve2:
            pos (200,540)
    else:
        scene black with fade2
        show alt_credits timeskip0 with dissolve2:
            pos (200,540)
    with dissolve2
    window hide
    
label Ravsii__role_menu:
    call screen role_menu_7dl
    
screen intro_loki_screen:
    add "intro_loki" xalign 0.0 yalign 0.0
    
screen intro_herc_screen:
    add "intro_herc" xalign 0.0 yalign 0.0
    
screen intro_dr_screen:
    add "intro_dr" xalign 0.0 yalign 0.0
    
screen role_menu_7dl:
    tag menu
    modal False
    imagemap:
        ground "intro_transparent"
        hotspot ((0, 0, 635, 1080)):
            hovered [Show("intro_loki_screen", transition=Dissolve(0.5))]
            unhovered [Hide("intro_loki_screen", transition=Dissolve(1.0))]
            action [Hide("intro_loki_screen", transition=Dissolve(0.5)), Jump("alt_day0_start_loki")]
        hotspot ((635, 0, 652, 1080)):
            hovered [Show("intro_herc_screen", transition=Dissolve(0.5))]
            unhovered [Hide("intro_herc_screen", transition=Dissolve(1.0))]
            action [Hide("intro_herc_screen", transition=Dissolve(0.5)), Jump("alt_day0_start_herc")]
        hotspot ((1287, 0, 634, 1080)):
            hovered [Show("intro_dr_screen", transition=Dissolve(0.5))]
            unhovered [Hide("intro_dr_screen", transition=Dissolve(1.0))]
            action [Hide("intro_dr_screen", transition=Dissolve(0.5)), Jump("alt_day0_start")]

label alt_day0_start:
    play sound sfx_wind_gust
    scene intro_dr with dissolve
    pause(1)
    menu:
        "Так всё и начиналось.":
            $ plthr = u"Дрищ"
            $ alt_chapter0()
            play sound role_drisch
            $ renpy.pause(4, hard=True)
            with fade2
            $ routetag = 'prologue'
            $ prolog_time()
        "Но я не уверен точно.":
            jump alt_day0_prologue
        "На самом деле всё было совсем иначе!" if alt_day_binder == 3:
            $ plthr = u"Септим"
    jump alt_day0_start1

label alt_day0_start_herc:
    play sound mpbt fadein 0
    scene intro_herc with dissolve
    pause(1)
    menu:
        "Так всё и начиналось.":
            $ plthr = u"Герк"
            $ alt_chapter0()
            play sound role_herc
            $ renpy.pause(4, hard=True)
            with fade2
            $ routetag = 'prologue'
            $ prolog_time()
            $ herc = True
        "Но я не уверен точно.":
            jump alt_day0_prologue
        "На самом деле всё было совсем иначе!" if alt_day_binder == 3:
            $ plthr = u"Септим"
    jump alt_day0_start1

label alt_day0_start_loki:
    play sound sfx_punch_medium
    scene intro_loki with dissolve
    pause(1)
    menu:
        "Так всё и начиналось.":
            $ plthr = u"Локи"
            $ alt_chapter0()
            play sound role_loki
            $ renpy.pause(4, hard=True)
            with dissolve2
            $ routetag = 'prologue'
            scene black with fade
            show alt_credits timeskip6 with dissolve2:
                pos (200,540)
            $ renpy.pause(4, hard=True)
            scene bg ext_winterpark_sunset_7dl with dissolve
            $ prolog_time()
            $ loki = True
        "Но я не уверен точно…":
            jump alt_day0_prologue
        "На самом деле всё было совсем иначе!" if alt_day_binder == 3:
            $ plthr = u"Септим"
    jump alt_day0_start1

label alt_day0_start1:
    if loki:
        call alt_day0_start_l
    elif herc:
        call alt_day0_start_h
    else:
        call alt_day0_start_d
    if alt_day_catapult == 1:
        call alt_day0_epic_fail
        return
    jump alt_day0_opening

label alt_day0_opening:
    $ renpy.pause(2, hard=True)
    if alt_day_binder != 1:
        play music intro2 fadein 5
    else:
        play music seven_summer_days fadein 5
    scene black 
    $ renpy.pause(3, hard=True)
    scene op_back 
    with dissolve2
    $ renpy.pause(2, hard=True)
    show op_mi 
    with dissolve2
    $ renpy.pause(2, hard=True)
    show op_dv 
    with dissolve2
    $ renpy.pause(2, hard=True)
    show op_sl 
    with dissolve2
    $ renpy.pause(2, hard=True)
    show op_un 
    with dissolve2
    $ renpy.pause(2, hard=True)
    show mt_bus 
    with dissolve2
    $ renpy.pause(2, hard=True)
    show op_us
    show uv_bus behind op_dv
    with dissolve2
    $ renpy.pause(2, hard=True)
    show logo_day :
        pos (400,150)
    with dissolve2
    show acm_logo with zoomin:
        pos (1200,350)
    with vpunch 
    $ renpy.pause(2, hard=True)
    scene black 
    with dissolve2
    stop music fadeout 5
    $ renpy.pause(5, hard=True)
    jump alt_day1_start
    
    
label alt_day1_start:
    call alt_day1_vars
    pause(1)
    $ persistent.sprite_time = "day"
    $ night_time()
    call alt_day1_begin
    pause(1)
    if alt_day_binder == 1: # альтдень
        $ persistent.sprite_time = "day"
        $ day_time()
        $ alt_chapter(1, u"Лагерь.")
        call alt_day1_alt_M
        pause(1)
        $ persistent.sprite_time = "day"
        $ day_time()
        $ alt_chapter(1, u"Первые трудности.")
        call alt_day1_alt_A
        pause(1)
        $ persistent.sprite_time = "day"
        $ day_time()
        $ alt_chapter(1, u"Новая форма!")
        call alt_day1_alt_S
        pause(1)
        $ persistent.sprite_time = "day"
        $ day_time()
        $ alt_chapter(1, u"Немного о…")
        call alt_day1_alt_L
        pause(1)
        $ persistent.sprite_time = "day"
        $ day_time()
        $ alt_chapter(1, u"Пионэр.")
        call alt_day1_alt_O
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(1, u"Ужин.")
        call alt_day1_alt_supper
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(1, u"Теория гадостроения.")
        call alt_day1_alt_U
        if not alt_day1_alt_us_robbed:
            call alt_day1_alt_U_reject
            pause(1)
        $ persistent.sprite_time = "night"
        $ night_time()
        $ alt_chapter(1, u"Вечер.")                
        call alt_day1_alt_ev_A_S
    else: # обычный
        $ persistent.sprite_time = "day"
        $ day_time()
        $ alt_chapter(1, u"Пробуждение")
        call alt_day1_bus_start
        pause(1)
        $ persistent.sprite_time = "day"
        $ day_time()
        $ alt_chapter(1, u"Прибытие")
        call alt_day1_arrival
        pause(1)
        if alt_day1_sl_conv:
            pass
        else:
            if herc or loki:
                $ persistent.sprite_time = "day"
                call alt_day1_chase1
                $ persistent.sprite_time = "day"
                $ day_time()
                $ alt_chapter(1, u"Пристань")
                call alt_day1_dock
                pause(1)
        $ persistent.sprite_time = "day"
        $ day_time()
        $ alt_chapter(1, u"Вожатая")
        call alt_day1_mod_tan
        pause(1)
        $ persistent.sprite_time = "day"
        $ day_time()
        $ alt_chapter(1, u"Электроник")
        call alt_day1_elektron
        pause(1)
        $ persistent.sprite_time = "day"
        $ day_time()
        $ alt_chapter(1, u"Экскурсия")
        call alt_day1_meeting
        pause(1)
        $ persistent.sprite_time = "day"    
        call alt_day1_soccer_d1
        pause(1)
        $ sunset_time()
        $ persistent.sprite_time = "sunset"
        $ alt_chapter(1, u"Ужин")
        call alt_day1_supper
        pause(1)
        call alt_day1_dining_room
        pause(1)
        $ persistent.sprite_time = "sunset"
        $ sunset_time()
        $ alt_chapter(1, u"Погоня")
        call alt_day1_chase
        pause(1)
        if alt_day1_us_shotted:
            call alt_day1_headshot
        else:
            $ sunset_time()
            $ persistent.sprite_time = "sunset"
            call alt_day1_nocatch
        pause(1)
        $ persistent.sprite_time = "night"
        $ night_time()
        $ alt_chapter(1, u"Спасительница")
        call alt_day1_slavya_saviour
    pause(1)
    $ night_time()
    $ persistent.sprite_time = "night"
    $ alt_chapter(1, u"Вечер")
    call alt_day1_lena
    pause(1)
    if alt_day1_un_stopped:
        call alt_day1_un_stay
        pause(1)
    call alt_day1_sleep
    pause(1)
    jump alt_day2_start