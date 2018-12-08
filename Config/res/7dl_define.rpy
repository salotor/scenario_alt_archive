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

screen alt_timer:
    add "timer_anim" xalign 0.5 yalign 0.5
    key "7" action [Hide("alt_timer"), Jump("alt_day3_dv_stayhere")]
    text "ВЕРНУТЬСЯ В ЛАГЕРЬ! (--->7<---)" align (0.5, 0.8) color "#FF0000"
    timer 2.0 action Jump("alt_day3_leave")

screen alert_text: #пишем предупреждение игроку
    modal True
    add get_image_7dl("screens/wet1.png")
    add get_image("gui/o_rly/base.png")
    text "Строка 1.":
        text_align 0.5
        yalign 0.44
        xalign 0.5
        color "#64483c"
        font header_font
        size 30
    text "Строка 2.":
        text_align 0.5
        yalign 0.49
        xalign 0.5
        color "#64483c"
        font header_font
        size 30
    textbutton _("OK"):
        text_size 60
        style "log_button"
        text_style "settings_link"
        yalign 0.65
        xalign 0.5
        action [Hide("alert_text"), Return(value=None)]
        
init:
    transform fleft:
        xalign 0.16
        xanchor 0.5

    transform left:
        xalign 0.28
        xanchor 0.5

    transform cleft:
        xalign 0.355
        xanchor 0.5

    transform center:
        xalign 0.5

    transform cright:
        xalign 0.645
        xanchor 0.5

    transform right:
        xalign 0.72
        xanchor 0.5

    transform fright:
        xalign 0.84
        xanchor 0.5

    transform voy_left:
        xalign 0.0
        xanchor 0.5

    transform voy_right:
        xalign 1.0
        xanchor 0.5
        
    transform zenterright:
        xalign 0.5 zoom 1.0
        linear 0.4 zoom 1.02 xalign 0.7
        
    transform enterright:
        xalign 0.5 zoom 1.02
        linear 0.6 zoom 1.05 xalign 0.9
        
    transform zenterleft:
        xalign 0.5 zoom 1.0
        linear 0.4 zoom 1.02 xalign 0.3
        
    transform enterleft: #по левую
        xalign 0.5 zoom 1.02
        linear 0.6 zoom 1.05 xalign 0.1
        
    transform zentercenter: #для открывающихся дверей
        xalign 0.5 zoom 1.0
        linear 0.8 zoom 1.05 xalign 0.5
        
    transform zentercenter2: #для открывающихся дверей
        xalign 0.5 zoom 1.0 subpixel True
        linear 20.0 zoom 1.5 xalign 0.5
        
    transform zexitcenter: #отдаляющий эффект от центра
        xalign 0.5 zoom 1.05 subpixel True
        linear 0.8 zoom 1.0 xalign 0.5
        
    transform zexitcenter2: #отдаляющий эффект от центра
        xalign 0.5 zoom 1.5
        linear 20 zoom 1.0 xalign 0.5
        
    transform zexitright: #отдалаюящий эффект от левого края к центру
        xalign 0.7 zoom 1.05
        linear 0.8 zoom 1.0 xalign 0.5
        
    transform zexitleft: #отдаляющий эффект от правого края к центру 
        xalign 0.3 zoom 1.05
        linear 0.8 zoom 1.0 xalign 0.5
        
    transform bottotop:
        pos (0,-1261)
        linear 10.0 pos (0,0)
        linear 2.0 pos (0, -200)
    
    transform salute_main_black(salute):
        "sal_black"
        choice 15:
            0.2
        choice:
            "sal_splash" with dspq
            0.2
            salute with dspr
            "sal_black" with dsps
            6.0
        repeat
        
    transform salute_main(salute):
        "sal_black"
        choice 15:
            0.2
        choice:
            "sal_splash" with dspq
            0.2
            choice:
                salute with dspr
                "sal_black" with dsps
                6.0
            choice:
                salute with dspr
                "sal_black" with dissolve
                6.0
        repeat
        
    transform running:
        block:
            zoom 1.1 xcenter 0.5 ycenter 0.5
        block:
            ease 0.2 xoffset 0 yoffset 0
            ease 0.2 xoffset 25 yoffset 50
            ease 0.2 xoffset 0 yoffset 0
            ease 0.2 xoffset -25 yoffset 50
        repeat

    transform fast_running:
        pos (0,0) 
        linear 0.1 pos (-5,-5) 
        linear 0.1 pos (5,5) 
        pos (0,0) 
        linear 0.1 pos (0,-5) 
        linear 0.1 pos (0,5) 
        repeat

    transform fast_running2:
        block:
            zoom 1.1 xcenter 0.5 ycenter 0.5
        block:
            ease 0.1 xoffset 0 yoffset 0
            ease 0.1 xoffset 12 yoffset 25
            ease 0.1 xoffset 0 yoffset 0
            ease 0.1 xoffset -12 yoffset 25
        repeat
        
#Наши транзиты, с блекджеком и разными цветами.
    $ flash_cyan = Fade(1, 0, 1, color="#1fa")
    $ fade_red = Fade(2, 2, 2, color="#f11")
    $ flash2_red = Fade(0.5, 0, 0.5, color="#f11")
    $ flash_pink = Fade(1, 0, 1, color="#e25")
    
    $ diam = ImageDissolve(im.Tile(get_image_7dl("gui/transit/pattern.jpg")), 1.1, 1)
    $ fdiam = ImageDissolve(im.Tile(get_image_7dl("gui/transit/pattern.jpg")), 0.4, 1)
    $ fulldiam = MultipleTransition([False,fdiam,get_image_7dl("screens/digi1.jpg"),fdiam,True])
    
    $ gopr = ImageDissolve(im.Tile(get_image_7dl("gui/transit/blackout_go.png")), 0.95, 1)
    $ swradar = ImageDissolve(im.Tile(get_image_7dl("gui/transit/blackout3.jpg")), 0.95, 1)
    $ joff = MultipleTransition([False,swradar,Solid("#000"),swradar,True])
    $ swradarr = ImageDissolve(im.Tile(get_image_7dl("gui/transit/blackout32.jpg")), 0.95, 1)
    $ joffr = MultipleTransition([False,swradarr,Solid("#000"),swradarr,True])
    
    $ blind_d = ImageDissolve(im.Tile(get_image_7dl("gui/transit/roof_ks.jpg")), 1.3)
    $ blinds_l = ImageDissolve(im.Tile(get_image_7dl("gui/transit/roof_ks2.jpg")), 0.6)
    $ blinds_r = ImageDissolve(im.Tile(get_image_7dl("gui/transit/roof_ks3.jpg")), 0.7)
    
    $ blind_l = MultipleTransition([False,blinds_l,Solid("#011"),blinds_r,True])
    $ blind_r = MultipleTransition([False,blinds_r,Solid("#011"),blinds_l,True])
    $ touch = ImageDissolve(im.Tile(get_image_7dl("gui/transit/pattern2.jpg")), 0.9, 1)
    $ dspq = Dissolve(0.04, alpha=True)
    $ dsps = Dissolve(3.0, alpha=True)
    $ guess_on = ImageDissolve(get_image_7dl("screens/blackpalm.png"), 0.25, ramplen=256, reverse=True)
    $ guess_off = ImageDissolve(get_image_7dl("screens/blackpalm.png"), 0.3, ramplen=256)
#Анимы
    image anim_digi:
        get_image_7dl("screens/digi1.jpg")  with Dissolve(1.5) 
        pause 1.5
        get_image_7dl("screens/digi2.jpg")  with Dissolve(1.5) 
        pause 1.5
        repeat
    
    image anim_grain: #Смэртельный номер: тянем картинку, делаем прозрачной и запускаем в секвенцию - и всё в коде!
        filmetile(get_image_7dl("screens/alt_noise1.png"))
        pause 0.1
        filmetile(get_image_7dl("screens/alt_noise2.png"))
        pause 0.1
        filmetile(get_image_7dl("screens/alt_noise3.png"))
        pause 0.1
        repeat
        
    image anim_intro_recall:
        get_image("bg/semen_room.jpg")
        pause 0.1
        get_image("bg/semen_room_window.jpg")
        pause 0.1
        get_image("anim/intro_1.jpg")
        pause 0.1
        get_image("anim/intro_2.jpg")
        pause 0.1
        get_image("anim/intro_3.jpg")
        pause 0.1
        get_image("anim/intro_4.jpg")
        pause 0.1
        get_image("anim/intro_5.jpg")
        pause 0.1
        get_image("anim/intro_6.jpg")
        pause 0.1
        get_image("anim/intro_8.jpg")
        pause 0.1
        get_image("anim/prolog_2.jpg")
        pause 0.1
        get_image("anim/prolog_1.jpg")
        pause 0.1
        get_image("anim/intro_9.jpg")
        pause 0.1
        get_image("anim/intro_10.jpg")
        pause 0.1
        get_image("anim/intro_11.jpg")
        pause 0.1
        get_image("anim/intro_13.jpg")
        pause 0.1
        get_image("bg/intro_xx.jpg")
        pause 0.1
        repeat
        
    image anim_square_party:
        get_image("bg/ext_square_night_party.jpg") with Dissolve(.5) 
        pause 0.6
        get_image("bg/ext_square_night_party2.jpg") with Dissolve(.5) 
        pause 0.6
        repeat
        
    image anim_square_preparty:
        get_image_7dl("bg/ext_square_sunset3_7dl.jpg") with Dissolve(1.5) 
        pause 1.6
        get_image_7dl("bg/ext_square_sunset2_7dl.jpg") with Dissolve(1.5) 
        pause 1.4
        repeat
    
    image uv_bus:
        get_sprite_7dl("custom/uv_alt1_7dl.png")
        pause 0.5
        get_sprite_7dl("custom/uv_alt2_7dl.png") 
        pause 0.5
        get_sprite_7dl("custom/uv_alt3_7dl.png")
        pause 0.5
        get_sprite_7dl("custom/uv_alt2_7dl.png")
        pause 0.5
        get_sprite_7dl("custom/uv_alt1_7dl.png")
        pause 0.5
    
    image anim_underwater:
        get_image_7dl("bg/ext_underwater_7dl.jpg")  with Dissolve(2.0) 
        pause 2.0
        get_image_7dl("bg/ext_underwater2_7dl.jpg")  with Dissolve(2.0) 
        pause 2.0
        get_image_7dl("bg/ext_underwater3_7dl.jpg")  with Dissolve(2.0) 
        pause 2.0
        get_image_7dl("bg/ext_underwater2_7dl.jpg")  with Dissolve(2.0) 
        pause 2.0
        get_image_7dl("bg/ext_underwater_7dl.jpg")  with Dissolve(2.0) 
        pause 2.0
        repeat
    
    image salute = LiveComposite((1920,1080),
                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh1.png")),
                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh11.png")),
                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh2.png")),
                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh21.png")),
                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh3.png")),

                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh4.png")),
                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh41.png")),
                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh5.png")),
                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh51.png")),
                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh6.png")),
                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh61.png")),
                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh7.png")),
                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh71.png")),

                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh91.png")),
                                  (0,0), salute_main(get_image_7dl("screens/salute/spoloh9.png")))

    
    image timer_anim: 
        get_sprite_7dl("custom/win_7dl.png") 
        0.1 #Задержка
        get_sprite_7dl("custom/win2_7dl.png")
        0.1
        get_sprite_7dl("custom/win3_7dl.png")
        0.1
        repeat # Не убирать
        
    image ftl_anim: 
        get_image_7dl("screens/ftl1.png") 
        0.1 #Задержка
        get_image_7dl("screens/ftl2.png")
        0.1
        get_image_7dl("screens/ftl3.png")
        0.1
        repeat # Не убирать
        
    image un serious dress anim: 
        get_sprite_7dl("custom/un_3_dress_serious_1_7dl.png") 
        8.0 #Задержка
        get_sprite_7dl("custom/un_3_dress_serious_2_7dl.png")
        0.1
        get_sprite_7dl("custom/un_3_dress_serious_1_7dl.png") 
        4.0 #Задержка
        get_sprite_7dl("custom/un_3_dress_serious_2_7dl.png")
        0.15
        get_sprite_7dl("custom/un_3_dress_serious_1_7dl.png") 
        7.0 #Задержка
        get_sprite_7dl("custom/un_3_dress_serious_2_7dl.png")
        0.1
        repeat # Не убирать
        
    image scenery:
        get_image("anim/prolog_2.jpg") with Dissolve(.5) 
        pause 2.6
        get_image("anim/prolog_1.jpg") with Dissolve(.5) 
        pause 0.6
        repeat
        
    image scenery2:
        get_image("anim/prolog_2.jpg") with Dissolve(.4) 
        pause 2.0
        get_image("anim/prolog_1.jpg") with Dissolve(.4) 
        pause 0.4
        repeat    
        
    image scenery3:
        get_image("anim/prolog_2.jpg") with Dissolve(.25) 
        pause 1.4
        get_image("anim/prolog_1.jpg") with Dissolve(.25) 
        pause 0.25
        repeat
        
#Заставки
    image bg ext_stand3_night_7dl = im.MatrixColor(get_image_7dl("bg/ext_stand3_7dl.jpg"), im.matrix.tint(0.63, 0.78, 0.82))
    image bg ext_stand3_sunset_7dl = im.MatrixColor(get_image_7dl("bg/ext_stand3_7dl.jpg"), im.matrix.tint(0.94, 0.82, 1.0))
    image bg ext_stand3_prolog_7dl = im.MatrixColor(get_image_7dl("bg/ext_stand_pr_7dl.jpg"), im.matrix.tint(0.82, 0.84, 1.0))
    
#Задники
    image bg ext_adductius_7dl = get_image_7dl("bg/ext_adductius_7dl.png")
    image bg ext_admins_day_7dl = get_image_7dl("bg/ext_admins_day_7dl.jpg")
    image bg ext_admins_night_7dl = get_image_7dl("bg/ext_admins_night_7dl.jpg")
    image bg ext_admins_rain_7dl = get_image_7dl("bg/ext_admins_rain_7dl.jpg")
    image bg ext_aidpost_rain_7dl = get_image_7dl("bg/ext_aidpost_rain_7dl.jpg")
    image bg ext_aidpost_sunset_7dl = get_image_7dl("bg/ext_aidpost_sunset_7dl.jpg")
    image bg ext_backdoor_day_7dl = get_image_7dl("bg/ext_backdoor_day_7dl.png")
    image bg ext_backdoor_night_7dl = get_image_7dl("bg/ext_backdoor_night_7dl.png")
    image bg ext_bathhouse_day_7dl = get_image_7dl("bg/ext_bathhouse_day_7dl.jpg")
    image bg ext_backroad_day_7dl = get_image_7dl("bg/ext_backroad_day_7dl.png")
    image bg ext_beach2_day_7dl = get_image_7dl("bg/ext_beach2_day_7dl.jpg")
    image bg ext_boathouse_rain_7dl = get_image_7dl("bg/ext_boathouse_rain_7dl.jpg")
    image bg ext_boathouse_sunset_7dl = get_image_7dl("bg/ext_boathouse_sunset_7dl.jpg")
    image bg ext_boathouse_alt_day_7dl = get_image_7dl("bg/ext_boathouse_alt_day_7dl.png")
    image bg ext_bus1_7dl = get_image_7dl("bg/ext_bus1_7dl.jpg")
    image bg ext_busstop_dust_7dl = get_image_7dl("bg/ext_busstop_dust_7dl.png")
    image bg ext_busstop_sun_7dl = get_image_7dl("bg/ext_busstop_sun_7dl.png")
    image bg ext_clubs_rain_7dl = get_image_7dl("bg/ext_clubs_rain_7dl.jpg")
    image bg ext_dining_hall_away_rain_7dl = get_image_7dl("bg/ext_dining_hall_away_rain_7dl.jpg")
    
    image bg ext_dv_hideout_day_7dl = get_image_7dl("bg/ext_dv_hideout_day_7dl.jpg")
    image bg ext_dining_hall_backroad_day_7dl = get_image_7dl("bg/ext_dining_hall_backroad_day_7dl.jpg")
    
    image bg ext_dining_hall_near_rain_7dl = get_image_7dl("bg/ext_dining_hall_near_rain_7dl.jpg")
    image bg ext_entrance_night_clear_7dl = get_image_7dl("bg/ext_entrance_night_clear_7dl.png")
    image bg ext_entrance_night_clear_closed_7dl = get_image_7dl("bg/ext_entrance_night_clear_closed_7dl.png")
    image bg ext_hospital2_away_day_7dl = get_image_7dl("bg/ext_hospital2_away_day_7dl.jpg")
    image bg ext_hospital2_away_night_7dl = get_image_7dl("bg/ext_hospital2_away_night_7dl.jpg")
    image bg ext_house_of_mt_rain_7dl = get_image_7dl("bg/ext_house_of_mt_rain_7dl.jpg")
    image bg ext_house_of_un_night_7dl = get_image_7dl("bg/ext_house_of_un_night_7dl.jpg")
    image bg ext_houses_night_7dl = get_image_7dl("bg/ext_houses_night_7dl.jpg")
    image bg ext_houses_rainy_day_7dl = get_image_7dl("bg/ext_houses_rainy_day_7dl.jpg")
    image bg ext_lake_day_7dl = get_image_7dl("bg/ext_lake_day_7dl.png")
    image bg ext_lake_night_7dl = get_image_7dl("bg/ext_lake_night_7dl.png")
    image bg ext_lake_sunset_7dl = get_image_7dl("bg/ext_lake_sunset_7dl.png")
    image bg ext_lib_sunset_7dl = get_image_7dl("bg/ext_lib_sunset_7dl.jpg")
    image bg ext_musclub_night_7dl = get_image_7dl("bg/ext_musclub_night_7dl.jpg")
    image bg ext_night_sky_7dl = get_image_7dl("bg/ext_night_sky_7dl.jpg")
    image bg ext_old_building_day_7dl = get_image_7dl("bg/ext_old_building_day_7dl.jpg")
    image bg ext_playground2_7dl = get_image_7dl("bg/ext_playground2_7dl.jpg")
    image bg ext_road_sunset_7dl = get_image_7dl("bg/ext_road_sunset_7dl.jpg")
    image bg ext_sandpit_day_7dl = get_image_7dl("bg/ext_sandpit_day_7dl.png")
    image bg ext_seashore_7dl = get_image_7dl("bg/ext_seashore_7dl.jpg")
    image bg ext_shower_day_7dl = get_image_7dl("bg/ext_shower_day_7dl.jpg")
    image bg ext_shower_night_7dl = get_image_7dl("bg/ext_shower_night_7dl.jpg")
    image bg ext_sky2_7dl = get_image_7dl("bg/ext_sky2_7dl.jpg")
    image bg ext_sky_7dl = get_image_7dl("bg/ext_sky_7dl.jpg")
    image bg ext_square_rain_genda_7dl = get_image_7dl("bg/ext_square_rain_genda_7dl.png")
    image bg ext_square_rain_day_7dl = get_image_7dl("bg/ext_square_rain_day_7dl.jpg")
    image bg ext_square_sunset2_7dl = get_image_7dl("bg/ext_square_sunset2_7dl.jpg")
    image bg ext_square_sunset3_7dl = get_image_7dl("bg/ext_square_sunset3_7dl.jpg")
    image bg ext_stage_big_clear_day_7dl = get_image_7dl("bg/ext_stage_big_clear_day_7dl.jpg")
    image bg ext_stage_big_sunset_7dl = get_image_7dl("bg/ext_stage_big_sunset_7dl.jpg")
    image bg ext_stage_near_clear_7dl = get_image_7dl("bg/ext_stage_near_clear_7dl.jpg")
    image bg ext_stairs_day_7dl = get_image_7dl("bg/ext_stairs_day_7dl.jpg")
    image bg ext_stairs_night_7dl = get_image_7dl("bg/ext_stairs_night_7dl.jpg")
    image bg ext_stairs_sunset_7dl = get_image_7dl("bg/ext_stairs_sunset_7dl.jpg")
    image bg ext_stand3_7dl = get_image_7dl("bg/ext_stand3_7dl.jpg")
    image bg ext_stand_pr_7dl = get_image_7dl("bg/ext_stand_pr_7dl.jpg")
    image bg ext_tennis_court_7dl = get_image_7dl("bg/ext_tennis_court_7dl.jpg")
    image bg ext_townscape_ph_day_7dl = get_image_7dl("bg/ext_townscape_ph_day_7dl.png")
    image bg ext_un_hideout_day_7dl = get_image_7dl("bg/ext_un_hideout_day_7dl.png")
    image bg ext_un_hideout_night_7dl = get_image_7dl("bg/ext_un_hideout_night_7dl.png")
    image bg ext_un_house_with_un_7dl = get_image_7dl("bg/ext_un_house_with_un_7dl.jpg")
    image bg ext_underwater_7dl = get_image_7dl("bg/ext_underwater_7dl.jpg")
    image bg ext_volley_court_7dl = get_image_7dl("bg/ext_volley_court_7dl.png")
    image bg ext_warehouse2_day_7dl = get_image_7dl("bg/ext_warehouse2_day_7dl.png")
    image bg ext_warehouse_blurry_7dl = get_image_7dl("bg/ext_warehouse_blurry_7dl.jpg")
    image bg ext_warehouse_day_7dl = get_image_7dl("bg/ext_warehouse_day_7dl.png") 
    image bg ext_warehouse_night_7dl = get_image_7dl("bg/ext_warehouse_night_7dl.png")
    image bg ext_warehouse_rain_day_7dl = get_image_7dl("bg/ext_warehouse_rain_day_7dl.jpg")
    image bg ext_warehouse_sunset_7dl = get_image_7dl("bg/ext_warehouse_sunset_7dl.jpg")
    image bg ext_washstand_night_7dl = get_image_7dl("bg/ext_washstand_night_7dl.jpg")
    
    image bg int_access2_day_7dl = get_image_7dl("bg/int_access2_day_7dl.png")
    image bg int_admins_window_7dl = get_image_7dl("bg/int_admins_window_7dl.jpg")
    image bg int_attic_7dl = get_image_7dl("bg/int_attic_7dl.jpg")
    image bg int_attic2_day_7dl = get_image_7dl("bg/int_attic2_day_7dl.jpg")
    image bg int_attic2_night_7dl = get_image_7dl("bg/int_attic2_night_7dl.jpg")
    image bg int_attic_ladder_7dl = get_image_7dl("bg/int_attic_ladder_7dl.jpg")
    
    image bg int_bus_warp_7dl = get_image_7dl("bg/int_bus_warp_7dl.jpg")
    
    image bg int_caffee_day_7dl = get_image_7dl("bg/int_caffee_day_7dl.png")
    image bg int_catacomb_door_fullbright_7dl = get_image_7dl("bg/int_catacomb_door_fullbright_7dl.jpg")
    image bg int_catacombs_door_light2_7dl = get_image_7dl("bg/int_catacombs_door_light2_7dl.jpg")
    image bg int_chief_office_day_7dl = get_image_7dl("bg/int_chief_office_day_7dl.png")
    image bg int_chief_office_rain_7dl = get_image_7dl("bg/int_chief_office_rain_7dl.png")
    image bg int_clubs_dj_7dl = get_image_7dl("bg/int_clubs_dj_7dl.jpg")
    image bg int_clubs_dj_night_7dl = get_image_7dl("bg/int_clubs_dj_night_7dl.jpg")
    image bg int_clubs_dj_night_nolight_7dl = get_image_7dl("bg/int_clubs_dj_night_nolight_7dl.jpg")
    image bg int_clubs_male_rain_7dl = get_image_7dl("bg/int_clubs_male_rain_7dl.jpg")
    image bg int_clubs_male_rain_clean_table_7dl = get_image_7dl("bg/int_clubs_male_rain_clean_table_7dl.jpg")
    image bg int_concert_room_7dl = get_image_7dl("bg/int_concert_room_7dl.jpg")
    image bg int_coupe_day_7dl = get_image_7dl("bg/int_coupe_day_7dl.png")
    image bg int_coupe_night_7dl = get_image_7dl("bg/int_coupe_night_7dl.png")
    
    image bg int_d3_hideout_7dl = get_image_7dl("bg/int_d3_hideout_7dl.png")
    image bg int_dining_hall_people_rain_7dl = get_image_7dl("bg/int_dinning_hall_people_rain_7dl.jpg")
    image bg int_dining_hall_rain_7dl = get_image_7dl("bg/int_dinning_hall_rain_7dl.jpg")
    image bg int_editorial_day_7dl = get_image_7dl("bg/int_editorial_day_7dl.jpg")
    image bg int_extra_house_7dl = get_image_7dl("bg/int_extra_house_7dl.jpg")
    image bg int_extra_house_day_7dl = get_image_7dl("bg/int_extra_house_day_7dl.jpg")
    image bg int_hence_day_7dl = get_image_7dl("bg/int_hence_day_7dl.jpg") # дублирует int_mine_exit_day_7dl
    image bg int_hence_night_7dl = get_image_7dl("bg/int_hence_night_7dl.jpg")
    image bg int_hospital_hall_day_7dl = get_image_7dl("bg/int_hospital_hall_day_7dl.png")
    image bg int_looney_bin_7dl = get_image_7dl("bg/int_looney_bin_7dl.jpg")
    image bg int_looney_bin_nightmare_7dl = get_image_7dl("bg/int_looney_bin_nightmare_7dl.jpg")
    image bg int_mine_exit_day_7dl = get_image_7dl("bg/int_mine_exit_day_7dl.jpg")
    image bg int_mine_heart_7dl = get_image_7dl("bg/int_mine_heart_7dl.jpg")
    image bg int_mine_halt_left_7dl = get_image_7dl("bg/int_mine_halt_left_7dl.jpg")
    image bg int_mine_room2_7dl = get_image_7dl("bg/int_mine_room2_7dl.jpg")
    image bg int_mine_water_7dl = get_image_7dl("bg/int_mine_water_7dl.jpg")
    image bg int_mt_sam_room_close_7dl = get_image_7dl("bg/int_mt_sam_room_close_7dl.jpg")
    image bg int_mt_sam_room_7dl = get_image_7dl("bg/int_mt_sam_room_7dl.jpg")
    image bg int_mt_sam_room_night_7dl = get_image_7dl("bg/int_mt_sam_room_night_7dl.jpg")
    image bg int_mt_sam_room_away_7dl = get_image_7dl("bg/int_mt_sam_room_away_7dl.jpg")
    image bg int_old_building_day_7dl = get_image_7dl("bg/int_old_building_day_7dl.jpg")
    image bg int_potato_storage_7dl = get_image_7dl("bg/int_potato_storage_7dl.png")
    image bg int_refinery_day_7dl = get_image_7dl("bg/int_refinery_day_7dl.png")
    image bg int_warehouse_day_7dl = get_image_7dl("bg/int_warehouse_day_7dl.png")
    image bg int_warehouse_night_7dl = get_image_7dl("bg/int_warehouse_night_7dl.png")
    image bg int_sporthall_day_7dl = get_image_7dl("bg/int_sporthall_day_7dl.png")
    image bg int_sporthall_night_7dl = get_image_7dl("bg/int_sporthall_night_7dl.png")
    image bg int_toilet_day_7dl = get_image_7dl("bg/int_toilet_day_7dl.png")
    image bg int_toilet_night_7dl = get_image_7dl("bg/int_toilet_night_7dl.png")
    image bg int_train_7dl = get_image_7dl("bg/int_train_7dl.png")
    image bg int_wagon_day_7dl = get_image_7dl("bg/int_wagon_day_7dl.png")
    image bg int_wagon_sunset_7dl = get_image_7dl("bg/int_wagon_sunset_7dl.png")
    image bg int_wardrobe_7dl = get_image_7dl("bg/int_wardrobe_7dl.jpg")
    image bg int_wardrobe2_7dl = get_image_7dl("bg/int_wardrobe2_7dl.jpg")
    
#Outro
    image bg ext_busstop_summer_7dl = get_image_7dl("bg/outro/ext_busstop_summer_7dl.png")
    image bg ext_city_night_7dl = get_image_7dl("bg/outro/ext_city_night_7dl.png")
    image bg ext_countryside_day_7dl = get_image_7dl("bg/outro/ext_countryside_day_7dl.png")
    image bg ext_dining_hall_near_snowy_day_7dl = get_image_7dl("bg/outro/ext_dining_hall_near_snowy_day_7dl.jpg")
    image bg ext_earth_7dl = get_image_7dl("bg/outro/ext_earth_7dl.jpg")
    image bg ext_emptiness_7dl = get_image_7dl("bg/outro/ext_emptiness_7dl.png")
    image bg ext_entrance_winter_7dl = get_image_7dl("bg/outro/ext_entrance_winter_7dl.jpg")
    image bg ext_graveyard_rain_7dl = get_image_7dl("bg/outro/ext_graveyard_rain_7dl.png")
    image bg ext_houses_snowy_day_7dl = get_image_7dl("bg/outro/ext_houses_snowy_day_7dl.jpg")
    image bg ext_house_of_mt_snowy_day_7dl = get_image_7dl("bg/outro/ext_house_of_mt_snowy_day_7dl.jpg")
    image bg ext_khruschevka_day_7dl = get_image_7dl("bg/outro/ext_khruschevka_day_7dl.png")
    image bg ext_khruschevka_night_7dl = get_image_7dl("bg/outro/ext_khruschevka_night_7dl.png")
    image bg ext_khruschevka_sunset_7dl = get_image_7dl("bg/outro/ext_khruschevka_sunset_7dl.png")
    image bg ext_khruschevka_rain_7dl = get_image_7dl("bg/outro/ext_khruschevka_rain_7dl.png")
    image bg ext_musclub_snowy_day_7dl = get_image_7dl("bg/outro/ext_musclub_snowy_day_7dl.jpg")
    image bg ext_mv2_7dl = get_image_7dl("bg/outro/ext_mv2_7dl.jpg")
    image bg ext_railbridge_sunset_7dl = get_image_7dl("bg/outro/ext_railbridge_sunset_7dl.png")
    image bg ext_railstation_7dl = get_image_7dl("bg/outro/ext_railstation_7dl.png")
    image bg ext_road_winter_7dl = get_image_7dl("bg/outro/ext_road_winter_7dl.jpg")
    image bg ext_winter_night_7dl = get_image_7dl("bg/outro/ext_winter_night_7dl.png")
    image bg ext_winter_night_rotate_7dl = get_image_7dl("bg/outro/ext_winter_night_rotate_7dl.png")
    image bg ext_winterpark_7dl = get_image_7dl("bg/outro/ext_winterpark_7dl.png")
    
    image bg int_access_day_7dl = get_image_7dl("bg/outro/int_access_day_7dl.jpg")
    image bg int_church_7dl = get_image_7dl("bg/outro/int_church_7dl.png")
    image bg int_epilogue_bg_7dl = get_image_7dl("bg/outro/int_epilogue_bg_7dl.jpg")
    image bg int_excalator_7dl = get_image_7dl("bg/outro/int_excalator_7dl.png")
    image bg int_excalator2_7dl = get_image_7dl("bg/outro/int_excalator2_7dl.png")
    image bg int_home_lift_7dl = get_image_7dl("bg/outro/int_home_lift_7dl.png")
    image bg int_hospital_corridor_7dl = get_image_7dl("bg/outro/int_hospital_corridor_7dl.jpg")
    image bg int_intro_liaz_7dl = get_image_7dl("bg/outro/int_intro_liaz_7dl.jpg")
    image bg int_opened_door_7dl = get_image_7dl("bg/outro/int_opened_door_7dl.jpg")
    image bg int_sam_house_clean_7dl = get_image_7dl("bg/outro/int_sam_house_clean_7dl.jpg")
    image bg int_sam_room_7dl = get_image_7dl("bg/outro/int_sam_room_7dl.png")
    image bg int_store_7dl = get_image_7dl("bg/outro/int_store_7dl.png")
    image bg int_ward_day_7dl = get_image_7dl("bg/outro/int_ward_day_7dl.png")
    image bg int_ward_night_7dl = get_image_7dl("bg/outro/int_ward_night_7dl.png")
    image bg int_ward_sunset_7dl = get_image_7dl("bg/outro/int_ward_sunset_7dl.png")
    
#extra
    image bg ext_boathouse_sunset = get_image_extra7dl("bg/ext_boathouse_sunset.jpg")
    image bg ext_camp_entrance_sunset = get_image_extra7dl("bg/ext_camp_entrance_sunset.jpg")
    image bg ext_clubs_sunset = get_image_extra7dl("bg/ext_clubs_sunset.jpg")
    image bg ext_house_of_el_day = get_image_extra7dl("bg/ext_house_of_el_day.jpg")
    image bg ext_house_of_el_night = get_image_extra7dl("bg/ext_house_of_el_night.jpg")
    image bg ext_playground_sunset = get_image_extra7dl("bg/ext_playground_sunset.jpg")
    image bg ext_stage_big_day = get_image_extra7dl("bg/ext_stage_big_day.jpg")
    
    image bg int_dining_hall_people_sunset = get_image_extra7dl("bg/int_dining_hall_people_sunset.jpg")
    image bg int_house_of_mt_noitem_day = get_image_extra7dl("bg/int_house_of_mt_noitem_day.jpg")
    
#Сценки ака CG
    image cg d1_me_dahell_7dl = get_image_7dl("cg/d1_me_dahell_7dl.jpg")
    image cg d1_mi_bus_7dl = get_image_7dl("cg/d1_mi_bus_7dl.jpg")
    image cg d1_mi_dv_bus_7dl = get_image_7dl("cg/d1_mi_dv_bus_7dl.jpg")
    image cg d1_sl_dinner_0_day_7dl = get_image_7dl("cg/d1_sl_dinner_0_day_7dl.jpg")
    image cg d1_sl_dinner_day_7dl = get_image_7dl("cg/d1_sl_dinner_day_7dl.jpg")
    image cg d1_un_book_7dl = get_image_7dl("cg/d1_un_book_7dl.png")
    image cg d1_un_book0_7dl = get_image_7dl("cg/d1_un_book0_7dl.jpg")
    image cg d1_uv_bus_7dl = get_image_7dl("cg/d1_uv_bus_7dl.jpg")
    
    image cg d2_dv_boat_day_7dl = get_image_7dl("cg/d2_dv_boat_day_7dl.jpg")
    image cg d2_mi_me_polaroid_7dl = get_image_7dl("cg/d2_mi_me_polaroid_7dl.png")
    image cg d2_mt_me_resort_afar_7dl = get_image_7dl("cg/d2_mt_me_resort_afar_7dl.jpg")
    image cg d2_mt_me_resort_close_7dl = get_image_7dl("cg/d2_mt_me_resort_close_7dl.jpg")
    image cg d2_un_kissing_7dl = get_image_7dl("cg/d2_un_kissing_7dl.jpg")
    image cg d2_un_knees_7dl = get_image_7dl("cg/d2_un_knees_7dl.jpg")
    image cg d2_us_boat_escape_7dl = get_image_7dl("cg/d2_us_boat_escape_7dl.jpg")
    image cg d2_us_trainhop_7dl = get_image_7dl("cg/d2_us_trainhop_7dl.png")
    image cg d2_un_owlet_pioneer_7dl = get_image_7dl("cg/d2_un_owlet_pioneer_7dl.jpg")
    image cg d2_us_soccer_sunset_7dl = get_image_7dl("cg/d2_us_soccer_sunset_7dl.jpg")
    
    image cg d3_dv_alice_dj80_7dl = get_image_7dl("cg/d3_dv_alice_dj80_7dl.jpg")
    image cg d3_disco_no_un_7dl = get_image_7dl("cg/d3_disco_no_un_7dl.jpg")
    image cg d3_mi_dance_afar_bordo_7dl = get_image_7dl("cg/d3_mi_dance_afar_bordo_7dl.jpg")
    image cg d3_mi_dance_afar_7dl = get_image_7dl("cg/d3_mi_dance_afar_7dl.jpg")
    image cg d3_mi_dance_close_7dl = get_image_7dl("cg/d3_mi_dance_close_7dl.jpg")
    image cg d3_mi_dance_close_bordo_7dl = get_image_7dl("cg/d3_mi_dance_close_bordo_7dl.jpg")
    image cg d3_me_mirror_white_7dl = get_image_7dl("cg/d3_me_mirror_white_7dl.jpg")
    image cg d3_me_mirror_bordo_7dl = get_image_7dl("cg/d3_me_mirror_bordo_7dl.jpg")
    image cg d3_sl_bath_unplaited_7dl = get_image_7dl("cg/d3_sl_bath_unplaited_7dl.jpg")
    image cg d3_sl_tease_7dl = get_image_7dl("cg/d3_sl_tease_7dl.jpg")
    image cg d3_sl_tease2_7dl = get_image_7dl("cg/d3_sl_tease2_7dl.jpg")
    image cg d3_sl_dance_bordo_7dl = get_image_7dl("cg/d3_sl_dance_bordo_7dl.jpg")
    image cg d3_un_dance_bordo_7dl = get_image_7dl("cg/d3_un_dance_bordo_7dl.jpg")
    
    image cg d4_cs_car_day_7dl = get_image_7dl("cg/d4_cs_car_day_7dl.png")
    image cg d4_cs_car_day_ba_7dl = get_image_7dl("cg/d4_cs_car_day_ba_7dl.png")
    image cg d4_cs_car_day_ba_gl_7dl = get_image_7dl("cg/d4_cs_car_day_ba_gl_7dl.png")
    image cg d4_cs_car_day_cs_7dl = get_image_7dl("cg/d4_cs_car_day_cs_7dl.png")
    image cg d4_cs_car_day_cs_coat_7dl = get_image_7dl("cg/d4_cs_car_day_cs_coat_7dl.png")
    image cg d4_cs_car_night_ba_7dl = get_image_7dl("cg/d4_cs_car_night_ba_7dl.png")
    image cg d4_cs_car_night_ba_gl_7dl = get_image_7dl("cg/d4_cs_car_night_ba_gl_7dl.png")
    image cg d4_cs_car_night_cs_7dl = get_image_7dl("cg/d4_cs_car_night_cs_7dl.png")
    image cg d4_cs_car_night_cs_coat_7dl = get_image_7dl("cg/d4_cs_car_night_cs_coat_7dl.png")
    
    
    image cg d4_cs_car_dark_7dl = get_image_7dl("cg/d4_cs_car_dark_7dl.png")
    image cg d4_cs_car_light_7dl = get_image_7dl("cg/d4_cs_car_light_7dl.png")
    image cg d4_cs_car_open_7dl = get_image_7dl("cg/d4_cs_car_open_7dl.png")
    image cg d4_cs_car_rim_7dl = get_image_7dl("cg/d4_cs_car_rim_7dl.png")

    image cg d4_fz_catac_un_7dl = get_image_7dl("cg/d4_fz_catac_un_7dl.jpg")
    image cg d4_fz_catac_sl_7dl = get_image_7dl("cg/d4_fz_catac_sl_7dl.jpg")
    image cg d4_fz_catac_dv_7dl = get_image_7dl("cg/d4_fz_catac_dv_7dl.jpg")
    image cg d4_fz_catac_el_7dl = get_image_7dl("cg/d4_fz_catac_el_7dl.jpg")
    image cg d4_fz_camping_7dl = get_image_7dl("cg/d4_fz_camping_7dl.jpg")
    image cg d4_fz_un_reject_7dl = get_image_7dl("cg/d4_fz_un_reject_7dl.jpg")
    image cg d4_fz_un_sleep_7dl = get_image_7dl("cg/d4_fz_un_sleep_7dl.jpg")
    image cg d4_hatch_night_7dl = get_image_7dl("cg/d4_hatch_night_7dl.jpg")
    image cg d4_hatch_night_open_7dl = get_image_7dl("cg/d4_hatch_night_open_7dl.jpg")
    image cg d4_lineup_no_un_7dl = get_image_7dl("cg/d4_lineup_no_un_7dl.jpg")
    image cg d4_lineup_no_un_us_7dl = get_image_7dl("cg/d4_lineup_no_un_us_7dl.jpg")
    
    image cg d4_mi_dj_dancing_7dl = get_image_7dl("cg/d4_mi_dj_dancing_7dl.jpg")
    image cg d4_mi_dj_lib0_7dl = get_image_7dl("cg/d4_mi_dj_lib0_7dl.jpg")
    image cg d4_mi_dj_lib_7dl = get_image_7dl("cg/d4_mi_dj_lib_7dl.jpg")
    image cg d4_mi_guitar_club_7dl = get_image_7dl("cg/d4_mi_guitar_club_7dl.jpg")
    image cg d4_mi_guitar_moon_7dl = get_image_7dl("cg/d4_mi_guitar_moon_7dl.jpg")
    image cg d4_mi_kandji_7dl = get_image_7dl("cg/d4_mi_kandji_7dl.jpg")
    image cg d4_mi_lineup_7dl = get_image_7dl("cg/d4_mi_lineup_7dl.jpg")
    image cg d4_mi_hedgehod_7dl = get_image_7dl("cg/d4_mi_hedgehod_7dl.png")
    image cg d4_mi_hedgehod_day_7dl = get_image_7dl("cg/d4_mi_hedgehod_day_7dl.png")
    image cg d4_mi_sup_7dl = get_image_7dl("cg/d4_mi_sup_7dl.jpg")
    
    image cg d4_sh_met_7dl = get_image_7dl("cg/d4_sh_met_7dl.jpg")
    
    image cg d4_sl_phone_ring_7dl = get_image_7dl("cg/d4_sl_phone_ring_7dl.png")
    image cg d4_sl_phone_up_7dl = get_image_7dl("cg/d4_sl_phone_up_7dl.png")
    image cg d4_sl_lookup_7dl = get_image_7dl("cg/d4_sl_lookup_7dl.png")
    image cg d4_sl_dnd_7dl = get_image_7dl("cg/d4_sl_dnd_7dl.jpg")
    
    image cg d4_un_7dl = get_image_7dl("cg/d4_un_7dl.jpg")
    
    image cg d4_us_stardust_7dl = get_image_7dl("cg/d4_us_stardust_7dl.png")
    
    image cg d4_volley_rage_7dl = get_image_7dl("cg/d4_volley_rage_7dl.jpg")
    
    image cg d5_me_Alisa_7dl = get_image_7dl("cg/d5_me_Alisa_7dl.jpg")
    image cg d5_mi_conv_7dl = get_image_7dl("cg/d5_mi_conv_7dl.jpg")
    image cg d5_mt_redress_7dl = get_image_7dl("cg/d5_mt_redress_7dl.jpg")
    image cg d5_boat_night_solo_7dl = get_image_7dl("cg/d5_boat_night_solo_7dl.jpg")
    image cg d5_rainy_idle_7dl = get_image_7dl("cg/d5_rainy_idle_7dl.jpg")
    
    image cg d5_sl_bed_7dl = get_image_7dl("cg/d5_sl_bed_7dl.jpg")
    
    image cg d5_sl_bench_day_7dl = get_image_7dl("cg/d5_sl_bench_day_7dl.png")
    image cg d5_sl_bench_neutral_7dl = get_image_7dl("cg/d5_sl_bench_neutral_7dl.png")
    image cg d5_sl_bench_night_7dl = get_image_7dl("cg/d5_sl_bench_night_7dl.png")
    image cg d5_sl_bench_sunset_7dl = get_image_7dl("cg/d5_sl_bench_sunset_7dl.png")
    
    
    image cg d5_sl_hugs_7dl = get_image_7dl("cg/d5_sl_hugs_7dl.jpg")
    image cg d5_sl_kissing_7dl = get_image_7dl("cg/d5_sl_kissing_7dl.png")
    image cg d5_sl_moon_7dl = get_image_7dl("cg/d5_sl_moon_7dl.jpg")
    image cg d5_sl_snark_7dl = get_image_7dl("cg/d5_sl_snark_7dl.png")
    
    image cg d5_sl_square_me_lead_7dl = get_image_7dl("cg/d5_sl_square_me_lead_7dl.png")
    image cg d5_sl_square_sl_lead_7dl = get_image_7dl("cg/d5_sl_square_sl_lead_7dl.png")
    image cg d5_sl_square_us_lead_7dl = get_image_7dl("cg/d5_sl_square_us_lead_7dl.png")
    
    image cg d5_sl_swimming_7dl = get_image_7dl("cg/d5_sl_swimming_7dl.jpg")
    
    image cg d5_un_carrier_7dl = get_image_7dl("cg/d5_un_carrier_7dl.png")
    image cg d5_un_film_7dl = get_image_7dl("cg/d5_un_film_7dl.jpg")
    image cg d5_un_boat_7dl = get_image_7dl("cg/d5_un_boat_7dl.jpg")
    image cg d5_un_bed_7dl = get_image_7dl("cg/d5_un_bed_7dl.jpg")
    image cg d5_us_rendezvous_7dl = get_image_7dl("cg/d5_us_rendezvous_7dl.png")
    image cg d5_us_sneakpeak_7dl = get_image_7dl("cg/d5_us_sneakpeak_7dl.png")
    
    
    #image cg d5_us_baseball_7dl = get_image_7dl("cg/d5_us_baseball_7dl.png")
    
    image cg d6_dance_alt_7dl = get_image_7dl("cg/d6_dance_alt_7dl.jpg")
    image cg d6_dv_dance_7dl = get_image_7dl("cg/d6_dv_dance_7dl.jpg")
    image cg d6_dv_dance_normal_7dl = get_image_7dl("cg/d6_dv_dance_normal_7dl.jpg")
    image cg d6_dv_hentai_7dl = get_image_7dl("cg/d6_dv_hentai_7dl.png")
    image cg d6_dv_hentai2_7dl = get_image_7dl("cg/d6_dv_hentai2_7dl.jpg")
    
    image cg d6_mi_boat_7dl = get_image_7dl("cg/d6_mi_boat_7dl.jpg")
    image cg d6_mi_cya_7dl = get_image_7dl("cg/d6_mi_cya_7dl.jpg")
    
    image cg d6_mi_departure_7dl = get_image_7dl("cg/d6_mi_departure_7dl.png")
    image cg d6_mi_farewell_7dl = get_image_7dl("cg/d6_mi_farewell_7dl.jpg")
    image cg d6_mi_hugs_7dl = get_image_7dl("cg/d6_mi_hugs_7dl.png")
    image cg d6_mi_leaving_7dl = get_image_7dl("cg/d6_mi_leaving_7dl.jpg")
    image cg d6_mi_morning_7dl = get_image_7dl("cg/d6_mi_morning_7dl.jpg")
    image cg d6_mi_swimming_7dl = get_image_7dl("cg/d6_mi_swimming_7dl.jpg")
    image cg d6_mi_vyluthere_7dl = get_image_7dl("cg/d6_mi_vyluthere_7dl.jpg")
    
    image cg d6_mt_salute_7dl = get_image_7dl("cg/d6_mt_salute_7dl.jpg")
    
    image cg d6_sl_bag_7dl = get_image_7dl("cg/d6_sl_bag_7dl.png")
    image cg d6_sl_clean_7dl = get_image_7dl("cg/d6_sl_clean_7dl.jpg")
    image cg d6_sl_clean_dress_7dl = get_image_7dl("cg/d6_sl_clean_dress_7dl.jpg")
    image cg d6_sl_puppy_7dl = get_image_7dl("cg/d6_sl_puppy_7dl.png")
    image cg d6_sl_zettai_7dl = get_image_7dl("cg/d6_sl_zettai_7dl.jpg")
    
    image cg d6_un_dissolve_7dl = get_image_7dl("cg/d6_un_dissolve_7dl.jpg")
    
    image cg d6_un_evening_0_7dl = get_image_7dl("cg/d6_un_evening_0_7dl.jpg")
    image cg d6_un_evening_3_7dl = get_image_7dl("cg/d6_un_evening_3_7dl.jpg")
    image cg d6_un_evening_0_1_7dl = get_image_7dl("cg/d6_un_evening_0_1_7dl.jpg")
    image cg d6_un_evening_0_2_7dl = get_image_7dl("cg/d6_un_evening_0_2_7dl.jpg")
    
    image cg d6_us_dance_7dl = get_image_7dl("cg/d6_us_dance_7dl.png")
    
    image cg d7_dv_alice_dj_7dl = get_image_7dl("cg/d7_dv_alice_dj_7dl.jpg")
    image cg d7_dv_looney_7dl = get_image_7dl("cg/d7_dv_looney_7dl.png")
    image cg d7_dv_addic_happy_7dl = get_image_7dl("cg/d7_dv_addic_happy_7dl.jpg")
    image cg d7_dv_bed_7dl = get_image_7dl("cg/d7_dv_bed_7dl.jpg")
    image cg d7_dv_ep_red_7dl = get_image_7dl("cg/d7_dv_ep_red_7dl.jpg")
    image cg d7_dv_noir_7dl = get_image_7dl("cg/d7_dv_noir_7dl.jpg")
    image cg d7_dv_epilogue_kissing_7dl = get_image_7dl("cg/d7_dv_epilogue_kissing_7dl.jpg")
    image cg d7_dv_epilogue_bus_7dl = get_image_7dl("cg/d7_dv_epilogue_bus_7dl.png")
    image cg d7_mi_epilogue_bus_7dl = get_image_7dl("cg/d7_mi_epilogue_bus_7dl.png")
    image cg d7_sl_epilogue_bus_7dl = get_image_7dl("cg/d7_sl_epilogue_bus_7dl.png")
    image cg d7_un_epilogue_bus_7dl = get_image_7dl("cg/d7_un_epilogue_bus_7dl.png")
    
    
    #image cg d7_ka_epilogue_bus_7dl = get_image_7dl("cg/d7_ka_epilogue_bus_7dl.png")
    
    image cg d7_dv_rf_reject_7dl = get_image_7dl("cg/d7_dv_rf_reject_7dl.jpg")
    
    image cg d7_frozen_7dl = get_image_7dl("cg/d7_frozen_7dl.jpg")
    
    image cg d7_leaving_no_sh_7dl = get_image_7dl("cg/d7_leaving_no_sh_7dl.jpg")
    image cg d7_leaving_no_sl_7dl = get_image_7dl("cg/d7_leaving_no_sl_7dl.jpg")
    image cg d7_leaving_no_sl_sam_7dl = get_image_7dl("cg/d7_leaving_no_sl_sam_7dl.jpg")
    
    image cg d7_me_epilogue_bus_7dl = get_image_7dl("cg/d7_me_epilogue_bus_7dl.png")
    image cg d7_me_looney_7dl = get_image_7dl("cg/d7_me_looney_7dl.png")
    
    image cg d7_mi_club27_7dl = get_image_7dl("cg/d7_mi_club27_7dl.png")
    image cg d7_mi_epilogue_7dl = get_image_7dl("cg/d7_mi_epilogue_7dl.jpg")
    image cg d7_mi_farewell_7dl = get_image_7dl("cg/d7_mi_farewell_7dl.jpg")
    image cg d7_mi_ghost_7dl = get_image_7dl("cg/d7_mi_ghost_7dl.png")
    image cg d7_mi_hugs_7dl = get_image_7dl("cg/d7_mi_hugs_7dl.jpg")
    image cg d7_mi_kaito_7dl = get_image_7dl("cg/d7_mi_kaito_7dl.jpg")
    image cg d7_mi_letter_7dl = get_image_7dl("cg/d7_mi_letter_7dl.jpg")
    image cg d7_mi_lost_7dl = get_image_7dl("cg/d7_mi_lost_7dl.png")
    image cg d7_mi_letter_rain_7dl = get_image_7dl("cg/d7_mi_letter_rain_7dl.jpg")
    image cg d7_mi_letter_rain_tears_7dl = get_image_7dl("cg/d7_mi_letter_rain_tears_7dl.jpg")
    image cg d7_mi_meeting_7dl = get_image_7dl("cg/d7_mi_meeting_7dl.jpg")
    image cg d7_mi_ramen_7dl = get_image_7dl("cg/d7_mi_ramen_7dl.jpg")
    image cg d7_mi_reenter_7dl = get_image_7dl("cg/d7_mi_reenter_7dl.png")
    image cg d7_mi_sparkle_7dl = get_image_7dl("cg/d7_mi_sparkle_7dl.jpg")
    image cg d7_mi_sunk_7dl = get_image_7dl("cg/d7_mi_sunk_7dl.jpg")
    
    image cg d7_mt_epilogue_bus_7dl = get_image_7dl("cg/d7_mt_epilogue_bus_7dl.png")
    image cg d7_mt_n2gether_7dl = get_image_7dl("cg/d7_mt_n2gether_7dl.jpg")
    image cg d7_sl_gonna_be_ok_7dl = get_image_7dl("cg/d7_sl_gonna_be_ok_7dl.jpg")
    image cg d7_sh_ai_4eva_7dl = get_image_7dl("cg/d7_sh_ai_4eva_7dl.jpg")
    image cg d7_trio_7dl = get_image_7dl("cg/d7_trio_7dl.jpg")
    
    image cg d7_un_epilogue_7dl = get_image_7dl("cg/d7_un_epilogue_7dl.jpg")
    image cg d7_un_epilogue_bad_7dl = get_image_7dl("cg/d7_un_epilogue_bad_7dl.jpg")
    image cg d7_un_epilogue_bad2_7dl = get_image_7dl("cg/d7_un_epilogue_bad2_7dl.jpg")
    image cg d7_un_met_7dl = get_image_7dl("cg/d7_un_met_7dl.jpg")
    image cg d7_un_epilogue_d1_7dl = get_image_7dl("cg/d7_un_epilogue_d1_7dl.jpg")
    image cg d7_un_epilogue_d2_7dl = get_image_7dl("cg/d7_un_epilogue_d2_7dl.jpg")
    image cg d7_un_reanimation_7dl = get_image_7dl("cg/d7_un_reanimation_7dl.jpg")
    
    image cg d7_us_epilogue_bus_7dl = get_image_7dl("cg/d7_us_epilogue_bus_7dl.png")
    image cg d7_us_pixie_7dl = get_image_7dl("cg/d7_us_pixie_7dl.png")
    image cg d7_us_tai_tai_7dl = get_image_7dl("cg/d7_us_tai_tai_7dl.jpg")

    image cg d7_bus_night_7dl = get_image_7dl("cg/d7_bus_night_7dl.jpg")
    
    #extra
    image cg d2_water_dan_night = get_image_extra7dl("cg/d2_water_dan_night.jpg")
    image cg d3_fag_room = get_image_extra7dl("cg/d3_fag_room.jpg")
    image cg d3_potato_1 = get_image_extra7dl("cg/d3_potato_1.jpg")
    image cg d3_potato_2 = get_image_extra7dl("cg/d3_potato_2.jpg")
    image cg wtf_end_of_day = get_image_extra7dl("cg/wtf_end_of_day.jpg")
    
#Турнир
    image alt_tournament_bg = get_image_7dl("gui/tournament/alt_tournament_bg.png")
    image sal_black = Solid("#00000000")
    image sal_splash = Solid("#FFFFFF66")
    image alt_KS_censor = get_image_7dl("screens/alt_KS_censor.png")
    image alt_KS_censor2 = get_image_7dl("screens/alt_KS_censor2.png")
    
    
    image dv_playon = get_image_7dl("gui/tournament/dv_playon.png")
    image me_playon = get_image_7dl("gui/tournament/me_playon.png")
    image mi_playon = get_image_7dl("gui/tournament/mi_playon.png")
    image mz_playon = get_image_7dl("gui/tournament/mz_playon.png")
    image sh_playon = get_image_7dl("gui/tournament/sh_playon.png")
    image sl_playon = get_image_7dl("gui/tournament/sl_playon.png")
    image un_playon = get_image_7dl("gui/tournament/un_playon.png")
    image us_playon = get_image_7dl("gui/tournament/us_playon.png")
    
#Заглушки для wannabe-комикса
    image comix3 = get_image_7dl("gui/intro/comix3.png")
    image comix4 = get_image_7dl("gui/intro/comix4.png")
    image comix4 = get_image_7dl("gui/intro/comix4.png")

    image blind1_1 = get_image_7dl("gui/intro/blind1_1.png")
    image blind1_2 = get_image_7dl("gui/intro/blind1_2.png")
    image blind2_1 = get_image_7dl("gui/intro/blind2_1.png")
    image blind2_2 = get_image_7dl("gui/intro/blind2_2.png")
    image blind3_1 = get_image_7dl("gui/intro/blind3_1.png")
    image blind3_2 = get_image_7dl("gui/intro/blind3_2.png")
    image blind4_1 = get_image_7dl("gui/intro/blind4_1.png")
    image blind4_2 = get_image_7dl("gui/intro/blind4_2.png")
    image blind4_3 = get_image_7dl("gui/intro/blind4_3.png")
    image blind4_4 = get_image_7dl("gui/intro/blind4_4.png")
    image ldb_blind = get_image_7dl("sprites/custom/ldb_blind_7dl.png")
#Интро
    image believe_in_pain = get_image_7dl("gui/intro/believe_in_pain.jpg")
    image gameover = get_image_7dl("gui/intro/gameover.jpg")
    image intro_dr = get_image_7dl("gui/intro/intro_dr.png")
    image intro_herc = get_image_7dl("gui/intro/intro_herc.png")
    image intro_loki = get_image_7dl("gui/intro/intro_loki.png")
    image spill_gray = get_image_7dl("gui/intro/spill_gray.png")
    image spill_red = get_image_7dl("gui/intro/spill_red.png")
    image acm_a = get_image_7dl("gui/intro/acm_a.png")
    image acm_l = get_image_7dl("gui/intro/acm_l.png")
    image acm_m = get_image_7dl("gui/intro/acm_m.png")
    image acm_o = get_image_7dl("gui/intro/acm_o.png")
    image acm_s = get_image_7dl("gui/intro/acm_s.png")
    image acm_u = get_image_7dl("gui/intro/acm_u.png")
    image name_dv = get_image_7dl("gui/intro/name_dv.png")
    image name_un = get_image_7dl("gui/intro/name_un.png")
    image name_mi = get_image_7dl("gui/intro/name_mi.png")
    image name_mt = get_image_7dl("gui/intro/name_mt.png")
    image name_sl = get_image_7dl("gui/intro/name_sl.png")
    image name_us = get_image_7dl("gui/intro/name_us.png")
    image rain_overlay = get_image_7dl("screens/rain_overlay.png")
    image intro_transparent = get_image_7dl("gui/intro/intro_transparent.png")

#Элементы интерфейса
    image blackout = get_image_7dl("gui/transit/blackout.png")
    image blackout2 = get_image_7dl("gui/transit/blackout2.png")
    image blackout_exh = get_image_7dl("gui/transit/blackout_exh.png")
    image blackout_exh2 = get_image_7dl("gui/transit/blackout_exh2.png")
    image blackout_exh3 = get_image_7dl("gui/transit/blackout_exh3.png")
    image genda_portrait = get_image_7dl("sprites/custom/genda_portrait_7dl.png")
    image gfx bokeh = get_image_7dl("screens/splatter.png")
    
    image anim_exhausted: 
        get_image_7dl("gui/blackout_exh2.png")
        0.03 #Задержка
        get_image_7dl("gui/blackout_exh3.png")
        0.03 #Задержка
        get_image_7dl("gui/blackout_exh2.png")
        0.03 #Задержка
        get_image_7dl("gui/blackout_exh3.png")
        0.03 #Задержка
        get_image_7dl("gui/blackout_exh2.png")
        0.03 #Задержка
        repeat # Не убирать
    
#Карта
#    image bg map = store.map_pics["bg map"]
#    image widget map = store.map_pics["widget map"]

#Скачки по карте
    image bg map_explain = get_image_7dl("gui/maps/map_explain.jpg")
    image dvsem_el = get_image_7dl("gui/maps/dvsem_el.png")
    image eye_s = get_image_7dl("sprites/custom/eye_s_7dl.png")
#Сотик
    image frame = get_image_7dl("gui/phone/frame.png")
    image frame_sl = get_image_7dl("gui/phone/frame_sl.png")
    image cam_ui = get_image_7dl("gui/phone/cam_ui.png")
#Пека
    image laptop = get_image_7dl("gui/laptop/laptop.png")
    image laptop_dv_bad = get_image_7dl("gui/laptop/laptop_dv_bad.png")
    image laptop_dv_bad_dr = get_image_7dl("gui/laptop/laptop_dv_bad_dr.png")
    image laptop_dv_bad_loki = get_image_7dl("gui/laptop/laptop_dv_bad_loki.png")
    image laptop_dv_bad_herc = get_image_7dl("gui/laptop/laptop_dv_bad_herc.png")
    image laptop_mi_anyone = get_image_7dl("gui/laptop/laptop_mi_anyone.png")
    image laptop_prologue = get_image_7dl("gui/laptop/laptop_prologue.png")
    image laptop_un_epilogue = get_image_7dl("gui/laptop/laptop_un_epilogue.png")
    image laptop_un_epilogue_dr = get_image_7dl("gui/laptop/laptop_un_epilogue_dr.png")
    image laptop_un_epilogue_loki = get_image_7dl("gui/laptop/laptop_un_epilogue_loki.png")
    image laptop_un_epilogue_herc = get_image_7dl("gui/laptop/laptop_un_epilogue_herc.png")
    
    image anim_laptop: 
        get_image_7dl("gui/laptop/laptop_prologue.png") 
        0.3 #Задержка
        get_image_7dl("gui/laptop/laptop_prologue_weak.png")
        0.25
        get_image_7dl("gui/laptop/laptop_prologue_mid.png")
        0.25
        get_image_7dl("gui/laptop/laptop_prologue_strong.png")
        0.2
        get_image_7dl("gui/laptop/laptop_prologue_mid.png")
        0.25
        get_image_7dl("gui/laptop/laptop_prologue_weak.png")
        0.3
        repeat # Не убирать
    
#Камень-ножницы-бумага    
    image miku_paper = get_image_7dl("gui/rps/miku_paper.png")
    image miku_rock = get_image_7dl("gui/rps/miku_rock.png")
    image miku_scissor = get_image_7dl("gui/rps/miku_scissor.png")
    image sam_paper = get_image_7dl("gui/rps/sam_paper.png")
    image sam_rock = get_image_7dl("gui/rps/sam_rock.png")
    image sam_scissor = get_image_7dl("gui/rps/sam_scissor.png")
    
#Ачивы+лого 
    image acm_logo_dv_drunk = get_image_7dl("gui/acm/acm_logo_dv_drunk_7dl.png")
    image acm_logo_dv_gohome = get_image_7dl("gui/acm/acm_logo_dv_gohome_7dl.png")
    image acm_logo_dv_meetmethere = get_image_7dl("gui/acm/acm_logo_dv_meetmethere_7dl.png")
    image acm_logo_dv_morethanlife = get_image_7dl("gui/acm/acm_logo_dv_morethanlife_7dl.png")
    image acm_logo_dv_theresnoway = get_image_7dl("gui/acm/acm_logo_dv_theresnoway_7dl.png")
    image acm_logo_dv_tillend = get_image_7dl("gui/acm/acm_logo_dv_tillend_7dl.png")
    image acm_logo_dv_tulpa = get_image_7dl("gui/acm/acm_logo_dv_tulpa_7dl.png")
    image acm_logo_dv_true = get_image_7dl("gui/acm/acm_logo_dv_true_7dl.png") 
    image acm_logo_me_lamp = get_image_7dl("gui/acm/acm_logo_me_lamp_7dl.png") 
    image acm_logo_dv_ussr_good = get_image_7dl("gui/acm/acm_logo_dv_ussr_good_7dl.png")
    
    image acm_logo_me_deep = get_image_7dl("gui/acm/acm_logo_me_deep_7dl.png")
    image acm_logo_me_lamp = get_image_7dl("gui/acm/acm_logo_me_lamp_7dl.png")
    image acm_logo_me_qte = get_image_7dl("gui/acm/acm_logo_me_qte_7dl.png")
    
    image acm_logo_mi_allyours = get_image_7dl("gui/acm/acm_logo_mi_allyours_7dl.png")
    image acm_logo_mi_namiki = get_image_7dl("gui/acm/acm_logo_mi_namiki_7dl.png")
    image acm_logo_mi_new_happy = get_image_7dl("gui/acm/acm_logo_mi_new_happy_7dl.png")
    image acm_logo_mi_ricochet = get_image_7dl("gui/acm/acm_logo_mi_ricochet_7dl.png")
    image acm_logo_mi_ungood = get_image_7dl("gui/acm/acm_logo_mi_ungood_7dl.png")
    
    image acm_logo_mi_happy_again = get_image_7dl("gui/acm/acm_logo_mi_happy_again_7dl.png")
    image acm_logo_mi_liar = get_image_7dl("gui/acm/acm_logo_mi_liar_7dl.png")
    image acm_logo_mi_dark_dreams = get_image_7dl("gui/acm/acm_logo_mi_dark_dreams_7dl.png")
    image acm_logo_mi_club27 = get_image_7dl("gui/acm/acm_logo_mi_club27_7dl.png")
    image acm_logo_mi_sparkle = get_image_7dl("gui/acm/acm_logo_mi_sparkle_7dl.png")
    image acm_logo_mi_bitter_truth = get_image_7dl("gui/acm/acm_logo_mi_bitter_truth_7dl.png")
    image acm_logo_mi_dam_cpu = get_image_7dl("gui/acm/acm_logo_mi_dam_cpu_7dl.png")
    image acm_logo_mi_unlike = get_image_7dl("gui/acm/acm_logo_mi_unlike_7dl.png")
    image acm_logo_mi_come = get_image_7dl("gui/acm/acm_logo_mi_come_7dl.png")
    image acm_logo_mi_watashi = get_image_7dl("gui/acm/acm_logo_mi_watashi_7dl.png")
    image acm_logo_mi_thank_you = get_image_7dl("gui/acm/acm_logo_mi_thank_you_7dl.png")
    
    image acm_logo_mt_cause = get_image_7dl("gui/acm/acm_logo_mt_cause_7dl.png")
    image acm_logo_mt_ending = get_image_7dl("gui/acm/acm_logo_mt_ending_7dl.png")
    image acm_logo_mt_ever_after = get_image_7dl("gui/acm/acm_logo_mt_ever_after_7dl.png")
    image acm_logo_mt_named_olga = get_image_7dl("gui/acm/acm_logo_mt_named_olga_7dl.png")
    
    image acm_logo_sl_bad = get_image_7dl("gui/acm/acm_logo_sl_bad_7dl.png")
    image acm_logo_sl_be_ok = get_image_7dl("gui/acm/acm_logo_sl_be_ok_7dl.png")
    image acm_logo_sl_fantazm = get_image_7dl("gui/acm/acm_logo_sl_fantazm_7dl.png")
    image acm_logo_sl_good = get_image_7dl("gui/acm/acm_logo_sl_good_7dl.png")
    image acm_logo_sl_lone = get_image_7dl("gui/acm/acm_logo_sl_lone_7dl.png")
    image acm_logo_sl_ok = get_image_7dl("gui/acm/acm_logo_sl_ok_7dl.png")
    image acm_logo_sl_same_place = get_image_7dl("gui/acm/acm_logo_sl_same_place_7dl.png")
    image acm_logo_sl_too_late = get_image_7dl("gui/acm/acm_logo_sl_too_late_7dl.png")
    image acm_logo_sl_worth = get_image_7dl("gui/acm/acm_logo_sl_worth_7dl.png")
    
    image acm_logo_sl_am_home = get_image_7dl("gui/acm/acm_logo_sl_am_home_7dl.png")
    image acm_logo_sl_neon = get_image_7dl("gui/acm/acm_logo_sl_neon_7dl.png")
    image acm_logo_sl_missed = get_image_7dl("gui/acm/acm_logo_sl_missed_7dl.png")
    image acm_logo_sl_no_wonder = get_image_7dl("gui/acm/acm_logo_sl_no_wonder_7dl.png")
    image acm_logo_sl_pan = get_image_7dl("gui/acm/acm_logo_sl_pan_7dl.png")
    image acm_logo_sl_radio = get_image_7dl("gui/acm/acm_logo_sl_radio_7dl.png")
    image acm_logo_sl_right_road = get_image_7dl("gui/acm/acm_logo_sl_right_road_7dl.png")
    image acm_logo_sl_till_sunrise = get_image_7dl("gui/acm/acm_logo_sl_till_sunrise_7dl.png")
    image acm_logo_sl_dr_un = get_image_7dl("gui/acm/acm_logo_sl_dr_un_7dl.png")
    image acm_logo_sl_wasted = get_image_7dl("gui/acm/acm_logo_sl_wasted_7dl.png")
    
    image acm_logo_un_good = get_image_7dl("gui/acm/acm_logo_un_good_7dl.png")
    image acm_logo_un_good2 = get_image_7dl("gui/acm/acm_logo_un_good2_7dl.png")
    image acm_logo_un_shelter = get_image_7dl("gui/acm/acm_logo_un_shelter_7dl.png")
    image acm_logo_un_sui = get_image_7dl("gui/acm/acm_logo_un_sui_7dl.png")
    image acm_logo_un_transit = get_image_7dl("gui/acm/acm_logo_un_transit_7dl.png")
    image acm_logo_un_true = get_image_7dl("gui/acm/acm_logo_un_true_7dl.png")
    
    image acm_logo_us_bad = get_image_7dl("gui/acm/acm_logo_us_bad_7dl.png")
    image acm_logo_us_fairytale = get_image_7dl("gui/acm/acm_logo_us_fairytale_7dl.png")
    image acm_logo_us_hi = get_image_7dl("gui/acm/acm_logo_us_hi_7dl.png")
    image acm_logo_us_openup = get_image_7dl("gui/acm/acm_logo_us_openup_7dl.png")
    image acm_logo_us_px = get_image_7dl("gui/acm/acm_logo_us_px_7dl.png")
    image acm_logo_us_semische = get_image_7dl("gui/acm/acm_logo_us_semische_7dl.png")
    image acm_logo_us_true = get_image_7dl("gui/acm/acm_logo_us_true_7dl.png")
    
    image achieve_beagod = get_image_7dl("gui/acm/achieve_beagod_7dl.png")
    image acm_logo = get_image_7dl("gui/acm/acm_logo1_7dl.png") #Логотип сюжета

    image dreamgirl_overlay = get_image_7dl("screens/dreamgirl_overlay.png")
    image wet1 = get_image_7dl("screens/wet1.png")
    image volley_fight = get_sprite_7dl("custom/volley_fight_7dl.png")
    
#Картинки с использованием прозрачности и прочая спрайтовость
    image dv normal flipped = Transform("dv normal pioneer", xzoom=-1.0)
    image dv normal flipped far = Transform("dv normal pioneer far", xzoom=-1.0)
    image sl normal flipped = Transform("sl normal pioneer", xzoom=-1.0)
    image sl serious flipped = Transform("sl serious pioneer", xzoom=-1.0)
    #image d3_miku_dance_blush flipped = Transform("d3_miku_dance_blush", xzoom=-1.0)
    image uv shade3 sized = Transform("uv shade3", zoom=.4)
    image uv shade4 sized = Transform("uv shade4", zoom=.4)
    image digi_pad = get_sprite_7dl("custom/digi_pad_7dl.png")
    image sl_trench = get_sprite_7dl("custom/sl_trench_7dl.png")
    image sl_trench2 = get_sprite_7dl("custom/sl_trench2_7dl.png")
    image cotocomb_lighter = get_sprite_7dl("custom/cotocomb_lighter_7dl.png")
    image d4_cat_door_frame = get_sprite_7dl("custom/d4_cat_door_frame_7dl.png")
    image d6_miku_cries = get_sprite_7dl("custom/d6_miku_cries_7dl.png")
    image mouth_dull = get_sprite_7dl("custom/mouth_dull_7dl.png")
    image mi_ru = get_sprite_7dl("custom/mi_ru_7dl.png")
    image mt_bus = get_sprite_7dl("custom/mt_bus_7dl.png")
    image myst_mh = get_sprite_7dl("custom/myst_mh_7dl.png")
    image uvao_d1 = get_sprite_7dl("custom/uvao_d1_7dl.png")
    image dv_mt = get_sprite_7dl("custom/dv_mt_7dl.png")
    image backpack = get_sprite_7dl("custom/backpack_7dl.png")
    image backpack_tiny = get_sprite_7dl("custom/backpack_tiny_7dl.png")
    image dv_us_volley = get_sprite_7dl("custom/dv_us_volley_7dl.png")
    
#Dnd
    image alt_cat_map_wireframe = get_image_7dl("gui/dnd/alt_cat_map_wireframe.png")
    image alt_cat_map = get_image_7dl("gui/dnd/alt_cat_map.png")
    image alt_cat_map_pathfinding = get_image_7dl("gui/dnd/alt_cat_map_pathfinding.png")
    image PolaroidFrame_7dl = get_sprite_7dl("custom/PolaroidFrame_7dl.png")
    
    
#Звучок
#ambience
    $ ambience_7dl = {}

    $ ambience_7dl["blackout"] = get_ambience_7dl("ambience_blackout_7dl.ogg")
    $ ambience_7dl["disco"] = get_ambience_7dl("ambience_disco_7dl.ogg")
    $ ambience_7dl["concert"] = get_ambience_7dl("ambience_tellyourworld_concert_7dl.ogg")
    $ ambience_7dl["elevator"] = get_ambience_7dl("ambience_elevator_7dl.ogg")
    $ ambience_7dl["explosive_post"] = get_ambience_7dl("ambience_explosive_post_7dl.ogg")
    $ ambience_7dl["night_city"] = get_ambience_7dl("ambience_night_city_7dl.ogg")
    $ ambience_7dl["railroad"] = get_ambience_7dl("ambience_railroad_7dl.ogg")
    $ ambience_7dl["rain"] = get_ambience_7dl("ambience_rain_loop_7dl.ogg")
    $ ambience_7dl["safe"] = get_ambience_7dl("ambience_safe_7dl.ogg")
    $ ambience_7dl["salute"] = get_ambience_7dl("ambience_salute_7dl.ogg")
    $ ambience_7dl["int_silence"] = get_ambience_7dl("ambience_int_silence_7dl.ogg")
    $ ambience_7dl["showers"] = get_ambience_7dl("ambience_showers_7dl.ogg")
    $ ambience_7dl["town_day"] = get_ambience_7dl("ambience_town_day_7dl.ogg")
    $ ambience_7dl["train"] = get_ambience_7dl("ambience_train_7dl.ogg")
    $ ambience_7dl["tv"] = get_ambience_7dl("ambience_tv_7dl.ogg")
    $ ambience_7dl["underwater"] = get_ambience_7dl("ambience_underwater_7dl.ogg")
    $ ambience_7dl["volley"] = get_ambience_7dl("ambience_volley_7dl.ogg")
    
#music
    $ music_7dl = {}

    $ music_7dl["abyss_call"] = get_music_7dl("abyss_call_7dl.ogg")
    $ music_7dl["aftermath"] = get_music_7dl("aftermath_7dl.ogg")
    $ music_7dl["alice_theme"] = get_music_7dl("alice_theme_7dl.ogg")
    $ music_7dl["alone"] = get_music_7dl("alone_7dl.ogg")
    $ music_7dl["afraid_of_destiny"] = get_music_7dl("afraid_of_destiny_7dl.ogg")
    $ music_7dl["anglegrinder"] = get_music_7dl("anglegrinder_7dl.ogg")
    $ music_7dl["areyouabully"] = get_music_7dl("areyouabully_7dl.ogg")
    $ music_7dl["are_you_there"] = get_music_7dl("are_you_there_7dl.ogg")
    $ music_7dl["ask_you_out"] = get_music_7dl("ask_you_out_7dl.ogg")
    
    $ music_7dl["bad_apple"] = get_music_7dl("bad_apple_7dl.ogg")
    $ music_7dl["beasteye"] = get_music_7dl("beasteye_7dl.ogg")
    $ music_7dl["beat_symphonic"] = get_music_7dl("beat_symphonic_7dl.ogg")
    $ music_7dl["beth"] = get_music_7dl("beth_7dl.ogg")
    $ music_7dl["but_why"] = get_music_7dl("but_why_7dl.ogg")
    $ music_7dl["breath_again"] = get_music_7dl("breath_again_7dl.ogg")
    $ music_7dl["breath_again_slow"] = get_music_7dl("breath_again_slow_7dl.ogg")
    $ music_7dl["breath_me"] = get_music_7dl("breath_me_7dl.ogg")
    $ music_7dl["brigh_you"] = get_music_7dl("brigh_you_7dl.ogg")
    $ music_7dl["brim"] = get_music_7dl("brim_7dl.ogg")
    $ music_7dl["bureaucracy"] = get_music_7dl("bureaucracy_7dl.ogg")
    
    $ music_7dl["canon_d_flamenco"] = get_music_7dl("canon_d_flamenco_7dl.ogg")
    $ music_7dl["carefree"] = get_music_7dl("carefree_7dl.ogg")
    $ music_7dl["catch_the_hedge"] = get_music_7dl("catch_the_hedge_7dl.ogg")
    $ music_7dl["christmas_met"] = get_music_7dl("christmas_met_7dl.ogg")
    $ music_7dl["closetoyou"] = get_music_7dl("closetoyou_7dl.ogg")
    $ music_7dl["clueless_hope"] = get_music_7dl("clueless_hope_7dl.ogg")
    
    $ music_7dl["dawn"] = get_music_7dl("dawn_7dl.ogg")
    $ music_7dl["danceagain"] = get_music_7dl("danceagain_7dl.ogg")
    $ music_7dl["dance_with_me"] = get_music_7dl("dance_with_me_7dl.ogg")
    $ music_7dl["dance_with_me_piano"] = get_music_7dl("dance_with_me_piano_7dl.ogg")
    $ music_7dl["deadman"] = get_music_7dl("deadman_7dl.ogg")
    $ music_7dl["dead_silence"] = get_music_7dl("dead_silence_7dl.ogg")
    $ music_7dl["deep_inside"] = get_music_7dl("deep_inside_7dl.ogg")
    $ music_7dl["devastated"] = get_music_7dl("devastated_7dl.ogg")
    $ music_7dl["dropit"] = get_music_7dl("dropit_7dl.ogg")
    $ music_7dl["dv_guitar"] = get_music_7dl("dv_guitar_7dl.ogg")

    $ music_7dl["escape_2"] = get_music_7dl("escape_2_7dl.ogg")
    $ music_7dl["exodus"] = get_music_7dl("exodus_7dl.ogg")
    $ music_7dl["emptiness"] = get_music_7dl("emptiness_7dl.ogg")
    $ music_7dl["es_downmix"] = get_music_7dl("es_downmix_7dl.ogg")
    $ music_7dl["everlasting_summer_alice"] = get_music_7dl("everlasting_summer_alice_7dl.ogg")
    $ music_7dl["everyday"] = get_music_7dl("everyday_7dl.ogg")
    $ music_7dl["explore"] = get_music_7dl("explore_7dl.ogg")

    $ music_7dl["faraway"] = get_music_7dl("faraway_7dl.ogg")
    $ music_7dl["feel_you_inside"] = get_music_7dl("feel_you_inside_7dl.ogg")
    $ music_7dl["finale_farewell"] = get_music_7dl("finale_farewell_7dl.ogg")
    $ music_7dl["forgive_or_what"] = get_music_7dl("forgive_or_what_7dl.ogg")
    $ music_7dl["frostwithoutyou"] = get_music_7dl("frostwithoutyou_7dl.ogg")
    $ music_7dl["fsl_tn"] = get_music_7dl("fsl_tn_7dl.ogg")
    $ music_7dl["fyrsta"] = get_music_7dl("fyrsta_7dl.ogg")
    
    $ music_7dl["game_of_shadows"] = get_music_7dl("game_of_shadows_7dl.ogg")
    $ music_7dl["genki"] = get_music_7dl("genki_7dl.ogg")
    $ music_7dl["gimme_hand"] = get_music_7dl("gimme_hand_7dl.ogg")
    $ music_7dl["guitar_under_the_window"] = get_music_7dl("guitar_under_the_window_7dl.ogg")
    $ music_7dl["groovie"] = get_music_7dl("groovie_7dl.ogg")
    $ music_7dl["gonna_be_ok"] = get_music_7dl("gonna_be_ok_7dl.ogg")
    
    $ music_7dl["happy_ending"] = get_music_7dl("happy_ending_7dl.ogg")
    $ music_7dl["hdance_5"] = get_music_7dl("hdance_5_7dl.ogg")
    $ music_7dl["hear_a_love"] = get_music_7dl("hear_a_love_7dl.ogg")
    $ music_7dl["hell"] = get_music_7dl("hell_7dl.ogg")
    $ music_7dl["herc_death"] = get_music_7dl("herc_death_7dl.ogg")
    $ music_7dl["hug_me_already"] = get_music_7dl("hug_me_already_7dl.ogg")

    $ music_7dl["iamagod2"] = get_music_7dl("iamagod2_7dl.ogg")
    $ music_7dl["iamsadiamsorry3"] = get_music_7dl("iamsadiamsorry3_7dl.ogg")
    $ music_7dl["iamsadiamsorry2"] = get_music_7dl("iamsadiamsorry2_7dl.ogg")
    $ music_7dl["iamsadiamsorry"] = get_music_7dl("iamsadiamsorry_7dl.ogg")
    $ music_7dl["imfine"] = get_music_7dl("imfine_7dl.ogg")
    $ music_7dl["intro1"] = get_music_7dl("intro1_7dl.ogg")
    $ music_7dl["intro2"] = get_music_7dl("intro2_7dl.ogg")
    $ music_7dl["iwantmagic"] = get_music_7dl("iwantmagic_7dl.ogg")
    $ music_7dl["i_will_find_you"] = get_music_7dl("i_will_find_you_7dl.ogg")
    
    $ music_7dl["keep_looking"] = get_music_7dl("keep_looking_7dl.ogg")
    $ music_7dl["kiss_you"] = get_music_7dl("kiss_you_7dl.ogg")
    $ music_7dl["knock"] = get_music_7dl("knock_7dl.ogg")
    $ music_7dl["krwling"] = get_music_7dl("krwling_7dl.ogg")
    
    $ music_7dl["lastlight_guitar"] = get_music_7dl("lastlight_guitar_7dl.ogg")
    $ music_7dl["lastlight_piano"] = get_music_7dl("lastlight_piano_7dl.ogg")
    $ music_7dl["last_summer"] = get_music_7dl("last_summer_7dl.ogg")
    $ music_7dl["last_hope"] = get_music_7dl("last_hope_7dl.ogg")
    $ music_7dl["laugh_throught_the_universe"] = get_music_7dl("laugh_throught_the_universe_7dl.ogg")
    $ music_7dl["lazy_olga"] = get_music_7dl("lazy_olga_7dl.ogg")
    $ music_7dl["last_pixie"] = get_music_7dl("last_pixie_7dl.ogg")
    $ music_7dl["let_me_down"] = get_music_7dl("let_me_down_7dl.ogg")
    $ music_7dl["liliac_ball"] = get_music_7dl("liliac_ball_7dl.ogg")
    $ music_7dl["lonesome_shepherd"] = get_music_7dl("lonesome_shepherd_7dl.ogg")
    $ music_7dl["loki_on_3"] = get_music_7dl("loki_on_3_7dl.ogg")
    $ music_7dl["lullaby2"] = get_music_7dl("lullaby2_7dl.ogg")
    $ music_7dl["lost_without_you"] = get_music_7dl("lost_without_you_7dl.ogg")
    $ music_7dl["longing"] = get_music_7dl("longing_7dl.ogg")
    $ music_7dl["ltyh"] = get_music_7dl("ltyh_7dl.ogg")
    $ music_7dl["lth"] = get_music_7dl("lth_7dl.ogg")
    $ music_7dl["lunar_anguish"] = get_music_7dl("lunar_anguish_7dl.ogg")
    $ music_7dl["lyrica_sg"] = get_music_7dl("lyrica_sg_7dl.ogg")
    $ music_7dl["lynn"] = get_music_7dl("lynn_7dl.ogg")

    $ music_7dl["mammal"] = get_music_7dl("mammal_7dl.ogg")
    $ music_7dl["magic_is_gone"] = get_music_7dl("magic_is_gone_7dl.ogg")
    $ music_7dl["meetmethere_tts"] = get_music_7dl("meetmethere_tts_7dl.ogg")
    $ music_7dl["me2ost"] = get_music_7dl("me2ost_7dl.ogg")
    $ music_7dl["melancholy_sun"] = get_music_7dl("melancholy_sun_7dl.ogg")
    $ music_7dl["midday_reverie"] = get_music_7dl("midday_reverie_7dl.ogg")
    $ music_7dl["misery"] = get_music_7dl("misery_2_7dl.ogg")
    $ music_7dl["moment"] = get_music_7dl("moment_7dl.ogg")
    $ music_7dl["more_than_alive"] = get_music_7dl("more_than_alive_7dl.ogg")
    $ music_7dl["morning_dew"] = get_music_7dl("morning_dew_7dl.ogg") # звук дождя в начале трека сбивает с толку
    $ music_7dl["my_only_hope"] = get_music_7dl("my_only_hope_7dl.ogg")
    
    $ music_7dl["nap_one"] = get_music_7dl("nap_one_7dl.ogg")
    $ music_7dl["no_hope_left"] = get_music_7dl("no_hope_left_7dl.ogg")
    $ music_7dl["nookie"] = get_music_7dl("nookie_7dl.ogg")
    $ music_7dl["not_alone"] = get_music_7dl("not_alone_7dl.ogg")
    $ music_7dl["nowyouseeme"] = get_music_7dl("nowyouseeme_7dl.ogg")
    
    $ music_7dl["ofrust"] = get_music_7dl("ofrust.ogg")
    $ music_7dl["old_kiss"] = get_music_7dl("old_kiss_7dl.ogg")
    $ music_7dl["one_little_lone_cloud"] = get_music_7dl("one_little_lone_cloud_7dl.ogg")
    $ music_7dl["ourfirstmet"] = get_music_7dl("ourfirstmet_7dl.ogg") 
    $ music_7dl["outer"] = get_music_7dl("outer_science_7dl.ogg") 
    $ music_7dl["out_of_your_tier"] = get_music_7dl("out_of_your_tier_7dl.ogg") 
    $ music_7dl["out_of_painkillers"] = get_music_7dl("out_of_painkillers_7dl.ogg") 
    
    $ music_7dl["pathways"] = get_music_7dl("pathways_7dl.ogg")
    $ music_7dl["pixies_playing"] = get_music_7dl("pixies_playing_7dl.ogg")
    $ music_7dl["please_reprise"] = get_music_7dl("please_reprise_7dl.ogg")
    $ music_7dl["please_stop_it_mastered"] = get_music_7dl("please_stop_it_mastered_7dl.ogg")
    $ music_7dl["polyhymnia_intro"] = get_music_7dl("polyhymnia_intro_7dl.ogg")
    $ music_7dl["polyhymnia_main"] = get_music_7dl("polyhymnia_main_7dl.ogg")
    $ music_7dl["ppk"] = get_music_7dl("ppk_7dl.ogg")
    $ music_7dl["prologue_2"] = get_music_7dl("prologue_2_7dl.ogg")
    $ music_7dl["promise_to_meet_you"] = get_music_7dl("promise_to_meet_you_7dl.ogg")
    $ music_7dl["pure_energy"] = get_music_7dl("pure_energy_7dl.ogg")

    $ music_7dl["radio_void"] = get_music_7dl("radio_void_7dl.ogg")
    $ music_7dl["raindrops"] = get_music_7dl("raindrops_7dl.ogg")
    $ music_7dl["redemption"] = get_music_7dl("redemption_7dl.ogg")
    $ music_7dl["red_lights"] = get_music_7dl("red_lights_7dl.ogg")
    $ music_7dl["refuse_to_believe"] = get_music_7dl("refuse_to_believe_7dl.ogg")
    $ music_7dl["refuse_to_replay"] = get_music_7dl("refuse_to_replay_7dl.ogg")
    $ music_7dl["regret"] = get_music_7dl("regret_7dl.ogg")
    $ music_7dl["rewind"] = get_music_7dl("rewind_7dl.ogg")
    $ music_7dl["rightroad"] = get_music_7dl("rightroad_7dl.ogg")
    $ music_7dl["ritual2"] = get_music_7dl("ritual2_7dl.ogg")
    $ music_7dl["runaway"] = get_music_7dl("runaway_7dl.ogg")
    
    $ music_7dl["sad_piano"] = get_music_7dl("sad_piano_7dl.ogg")
    $ music_7dl["sam_lullaby"] = get_music_7dl("sam_lullaby_7dl.ogg")
    $ music_7dl["sammy"] = get_music_7dl("sammy_7dl.ogg")
    $ music_7dl["saveme"] = get_music_7dl("saveme_7dl.ogg")
    $ music_7dl["scorpions"] = get_music_7dl("scorpions_7dl.ogg")
    $ music_7dl["semische"] = get_music_7dl("semische_7dl.ogg")
    $ music_7dl["see_one_day"] = get_music_7dl("see_one_day_7dl.ogg")
    $ music_7dl["seven_summer_days"] = get_music_7dl("seven_summer_days_7dl.ogg")
    $ music_7dl["sign_of_blood"] = get_music_7dl("sign_of_blood_7dl.ogg")
    $ music_7dl["silent_angel"] = get_music_7dl("silent_angel_7dl.ogg")
    $ music_7dl["sh_ai_rejuv"] = get_music_7dl("sh_ai_rejuv_7dl.ogg")
    $ music_7dl["shape_of_my_heart"] = get_music_7dl("shape_of_my_heart_7dl.ogg")
    $ music_7dl["shappihn"] = get_music_7dl("shappihn_7dl.ogg")
    $ music_7dl["sheiscool"] = get_music_7dl("sheiscool_7dl.ogg")
    $ music_7dl["shehasgone"] = get_music_7dl("shehasgone_7dl.ogg")
    $ music_7dl["shestheone"] = get_music_7dl("shestheone_7dl.ogg")
    $ music_7dl["shib_mono"] = get_music_7dl("shib_mono_7dl.ogg")
    $ music_7dl["shib_stereo"] = get_music_7dl("shib_stereo_7dl.ogg")
    $ music_7dl["slavyas_fantazm"] = get_music_7dl("slavyas_fantazm_7dl.ogg")
    $ music_7dl["sky_feather"] = get_music_7dl("sky_feather_7dl.ogg")
    $ music_7dl["sammy"] = get_music_7dl("sammy_7dl.ogg")
    $ music_7dl["smlg"] = get_music_7dl("smlg_7dl.ogg")
    $ music_7dl["snatch"] = get_music_7dl("snatch_7dl.ogg")
    $ music_7dl["sneakupon"] = get_music_7dl("sneakupon_7dl.ogg")
    $ music_7dl["so_be_it"] = get_music_7dl("so_be_it_7dl.ogg")
    $ music_7dl["so_cold"] = get_music_7dl("so_cold_7dl.ogg")
    $ music_7dl["so_lonely"] = get_music_7dl("so_lonely_7dl.ogg")
    $ music_7dl["someone_like_you_guitar"] = get_music_7dl("someone_like_you_guitar_7dl.ogg")
    $ music_7dl["sorrow"] = get_music_7dl("sorrow_7dl.ogg")
    $ music_7dl["splin"] = get_music_7dl("splin1_7dl.ogg")
    $ music_7dl["stilllovingyou"] = get_music_7dl("stilllovingyou_7dl.ogg")
    $ music_7dl["summer_ends_soon"] = get_music_7dl("summer_ends_soon_7dl.ogg")
    $ music_7dl["summer_ends_soon2"] = get_music_7dl("summer_ends_soon2_7dl.ogg")
    $ music_7dl["surf"] = get_music_7dl("surf_7dl.ogg")

    $ music_7dl["take_my_hand"] = get_music_7dl("take_my_hand_7dl.ogg")
    $ music_7dl["tearing_sobs"] = get_music_7dl("tearing_sobs_7dl.ogg")
    $ music_7dl["tears_of"] = get_music_7dl("tears_of_7dl.ogg")
    $ music_7dl["tellyourworld"] = get_music_7dl("tellyourworld_7dl.ogg")
    $ music_7dl["temptation"] = get_music_7dl("temptation_7dl.ogg")
    $ music_7dl["tender_song"] = get_music_7dl("tender_song_7dl.ogg")
    $ music_7dl["there_you_are"] = get_music_7dl("loop_there_you_are!_7dl.ogg")
    $ music_7dl["the_way"] = get_music_7dl("the_way_7dl.ogg")
    $ music_7dl["think_again"] = get_music_7dl("think_again_7dl.ogg")
    $ music_7dl["thousand_little_things"] = get_music_7dl("thousand_little_things_7dl.ogg")
    $ music_7dl["thousand_of_pixies"] = get_music_7dl("thousand_of_pixies_7dl.ogg")
    $ music_7dl["tilltheend"] = get_music_7dl("tilltheend_7dl.ogg")
    $ music_7dl["timetowakeup"] = get_music_7dl("timetowakeup_7dl.ogg")
    $ music_7dl["to_the_sunrise"] = get_music_7dl("to_the_sunrise_7dl.ogg")
    $ music_7dl["too_serious"] = get_music_7dl("too_serious_7dl.ogg")
    $ music_7dl["too_quiet"] = get_music_7dl("too_quiet_7dl.ogg")
    
    $ music_7dl["uncertainity"] = get_music_7dl("uncertainity_7dl.ogg")
    $ music_7dl["unfulfilled"] = get_music_7dl("unfulfilled_7dl.ogg")
    $ music_7dl["uneven_me"] = get_music_7dl("uneven_me_7dl.ogg")
    $ music_7dl["unfinished_life"] = get_music_7dl("unfinished_life_7dl.ogg")
    $ music_7dl["unforgotten"] = get_music_7dl("unforgotten_7dl.ogg")
    $ music_7dl["unholy_you"] = get_music_7dl("unholy_you_7dl.ogg")
    
    $ music_7dl["vale"] = get_music_7dl("vale_7dl.ogg")
    $ music_7dl["vampire"] = get_music_7dl("vampire_7dl.ogg")
    $ music_7dl["vibe"] = get_music_7dl("vibe_7dl.ogg")
    $ music_7dl["viola"] = get_music_7dl("viola_7dl.ogg")
    
    $ music_7dl["war_to_fight"] = get_music_7dl("war_to_fight_7dl.ogg")
    $ music_7dl["what_am_i_doing_here"] = get_music_7dl("what_am_i_doing_here_7dl.ogg")
    $ music_7dl["what_cost"] = get_music_7dl("what_cost_7dl.ogg")
    $ music_7dl["whatnow"] = get_music_7dl("whatnow_7dl.ogg")
    $ music_7dl["what_if"] = get_music_7dl("what_if_7dl.ogg")
    $ music_7dl["wheres_wonderland"] = get_music_7dl("wheres_wonderland_7dl.ogg")
    $ music_7dl["will_you"] = get_music_7dl("will_you_7dl.ogg")
    $ music_7dl["wonderful_faraway"] = get_music_7dl("wonderful_faraway_7dl.ogg")
    
    $ music_7dl["you_were_late"] = get_music_7dl("you_were_late_7dl.ogg")
    $ music_7dl["you_are_human"] = get_music_7dl("you_are_human_7dl.ogg")
    $ music_7dl["you_are_soul"] = get_music_7dl("you_are_soul_7dl.ogg")
    $ music_7dl["you_are_star"] = get_music_7dl("you_are_star_7dl.ogg")
    $ music_7dl["you_re_dam_funny"] = get_music_7dl("you_re_dam_funny_7dl.ogg")
    $ music_7dl["youareours"] = get_music_7dl("youareours_7dl.ogg")
    $ music_7dl["youre_not_real"] = get_music_7dl("youre_not_real_7dl.ogg")
    $ music_7dl["your_life"] = get_music_7dl("your_life_7dl.ogg")
    $ music_7dl["yume_akari"] = get_music_7dl("yume_akari_7dl.ogg")
    
# sfx
    $ sfx_7dl = {}

    $ sfx_7dl["apple_bite"] = get_sfx_7dl("apple_bite_7dl.ogg")
    $ sfx_7dl["aunl"] = get_sfx_7dl("aunl_7dl.ogg")
    $ sfx_7dl["bed_squeak"] = get_sfx_7dl("bed_squeak_7dl.ogg")
    $ sfx_7dl["brake"] = get_sfx_7dl("brake_7dl.ogg")
    $ sfx_7dl["breath"] = get_sfx_7dl("breath_7dl.ogg")
    $ sfx_7dl["blanket"] = get_sfx_7dl("blanket_7dl.ogg")
    $ sfx_7dl["car_passing"] = get_sfx_7dl("car_passing_7dl.ogg")
    $ sfx_7dl["deagle_shot"] = get_sfx_7dl("deagle_shot_7dl.ogg")
    $ sfx_7dl["eat_horn"] = get_sfx_7dl("eat_horn_7dl.ogg")
    $ sfx_7dl["footsteps_grass"] = get_sfx_7dl("footsteps_grass_7dl.ogg")
    $ sfx_7dl["gate_open"] = get_sfx_7dl("gate_open_7dl.ogg")
    $ sfx_7dl["ghmm"] = get_sfx_7dl("ghm_7dl.ogg")
    $ sfx_7dl["hedgehog"] = get_sfx_7dl("hedgehog_7dl.ogg")
    $ sfx_7dl["highfive"] = get_sfx_7dl("highfive_7dl.ogg")
    $ sfx_7dl["intro_dr"] = get_sfx_7dl("intro_dr_7dl.ogg")
    $ sfx_7dl["KBtyping"] = get_sfx_7dl("KBtyping_7dl.ogg")
    $ sfx_7dl["kissing_sound"] = get_sfx_7dl("kissing_sound_7dl.ogg")
    $ sfx_7dl["makarych"] = get_sfx_7dl("makarych_7dl.ogg")
    $ sfx_7dl["miku_stomping"] = get_sfx_7dl("miku_stomping_7dl.ogg")
    $ sfx_7dl["metal_hit_on_metal"] = get_sfx_7dl("metal_hit_on_metal_7dl.ogg")
    $ sfx_7dl["mpbt"] = get_sfx_7dl("mpbt_7dl.ogg")
    $ sfx_7dl["old_phone"] = get_sfx_7dl("old_phone_7dl.ogg")
    $ sfx_7dl["plates_broken"] = get_sfx_7dl("plates_broken_7dl.ogg")
    $ sfx_7dl["phone_feedback"] = get_sfx_7dl("phone_feedback_7dl.ogg")
    $ sfx_7dl["pouring"] = get_sfx_7dl("pouring_7dl.ogg")
    $ sfx_7dl["pup_bark"] = get_sfx_7dl("pup_bark_7dl.ogg")
    $ sfx_7dl["push_the_button"] = get_sfx_7dl("push_the_button_7dl.ogg")
    $ sfx_7dl["raindrops_radio"] = get_sfx_7dl("raindrops_radio_7dl.ogg")
    $ sfx_7dl["reverse_bell"] = get_sfx_7dl("reverse_bell_7dl.ogg")
    $ sfx_7dl["ringtone"] = get_sfx_7dl("ringtone_7dl.ogg")
    #Озвучка заголовка роли by Noir Сычёв
    $ sfx_7dl["role_drisch"] = get_sfx_7dl("role_drisch_7dl.ogg")
    $ sfx_7dl["role_herc"] = get_sfx_7dl("role_herc_7dl.ogg")
    $ sfx_7dl["role_loki"] = get_sfx_7dl("role_loki_7dl.ogg")
    $ sfx_7dl["sigh_out"] = get_sfx_7dl("sigh_out_7dl.ogg")
    $ sfx_7dl["snap"] = get_sfx_7dl("snap_7dl.ogg")
    $ sfx_7dl["stahp"] = get_sfx_7dl("stahp_7dl.ogg")
    $ sfx_7dl["tearing"] = get_sfx_7dl("tearing_7dl.ogg")
    $ sfx_7dl["tousche"] = get_sfx_7dl("tousche_7dl.ogg")
    $ sfx_7dl["train_depart"] = get_sfx_7dl("train_depart_7dl.ogg")
    $ sfx_7dl["train_income"] = get_sfx_7dl("train_income_7dl.ogg")
    $ sfx_7dl["nesmogla"] = get_sfx_7dl("nesmogla_7dl.ogg")
    $ sfx_7dl["volley_hit"] = get_sfx_7dl("volley_hit_7dl.ogg")
    $ sfx_7dl["wakeup_horn"] = get_sfx_7dl("wakeup_horn_7dl.ogg")
    $ sfx_7dl["wakeup"] = get_sfx_7dl("wakeup_7dl.ogg")
    $ sfx_7dl["white_noise"] = get_sfx_7dl("white_noise_7dl.ogg")
    $ sfx_7dl["window_glass_break"] = get_sfx_7dl("window_glass_break_7dl.ogg")