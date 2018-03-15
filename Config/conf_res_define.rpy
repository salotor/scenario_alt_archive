init:
    transform fleft:
        xalign 0.16
        xanchor 0.5
        yalign 0.0

    transform left:
        xalign 0.28
        xanchor 0.5
        yalign 0.0

    transform cleft:
        xalign 0.355
        xanchor 0.5
        yalign 0.0

    transform center:
        xalign 0.5
        yalign 0.0

    transform cright:
        xalign 0.645
        xanchor 0.5
        yalign 0.0

    transform right:
        xalign 0.72
        xanchor 0.5
        yalign 0.0

    transform fright:
        xalign 0.84
        xanchor 0.5
        yalign 0.0

    transform voy_left:
        xalign 0.0
        xanchor 0.5
        yanchor 0.0

    transform voy_right:
        xalign 1.0
        xanchor 0.5
        yanchor 0.0
        
    transform zenterright:
        xalign 0.5 yalign 0.5 zoom 1.0
        linear 0.4 zoom 1.02 xalign 0.7 yalign 0.5
        
    transform enterright:
        xalign 0.5 yalign 0.5 zoom 1.02
        linear 0.6 zoom 1.05 xalign 0.9 yalign 0.5
        
    transform zenterleft:
        xalign 0.5 yalign 0.5 zoom 1.0
        linear 0.4 zoom 1.02 xalign 0.3 yalign 0.5
        
    transform enterleft: #по левую
        xalign 0.5 yalign 0.5 zoom 1.02
        linear 0.6 zoom 1.05 xalign 0.1 yalign 0.5
        
    transform zentercenter: #для открывающихся дверей
        xalign 0.5 yalign 0.5 zoom 1.0
        linear 0.8 zoom 1.05 xalign 0.5 yalign 0.5
        
    transform zentercenter2: #для открывающихся дверей
        xalign 0.5 yalign 0.5 zoom 1.0 subpixel True
        linear 20.0 zoom 1.5 xalign 0.5 yalign 0.5
        
    transform zexitcenter: #отдаляющий эффект от центра
        xalign 0.5 yalign 0.5 zoom 1.05 subpixel True
        linear 0.8 zoom 1.0 xalign 0.5 yalign 0.5
        
    transform zexitcenter2: #отдаляющий эффект от центра
        xalign 0.5 yalign 0.5 zoom 1.5
        linear 20 zoom 1.0 xalign 0.5 yalign 0.5
        
    transform zexitright: #отдалаюящий эффект от левого края к центру
        xalign 0.7 yalign 0.5 zoom 1.05
        linear 0.8 zoom 1.0 xalign 0.5 yalign 0.5
        
    transform zexitleft: #отдаляющий эффект от правого края к центру 
        xalign 0.3 yalign 0.5 zoom 1.05
        linear 0.8 zoom 1.0 xalign 0.5 yalign 0.5
        
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
#Наши транзиты, с блекджеком и разными цветами.
    $ flash_cyan = Fade(1, 0, 1, color="#1fa")
    $ fade_red = Fade(2, 2, 2, color="#f11")
    $ flash2_red = Fade(0.5, 0, 0.5, color="#f11")
    $ flash_pink = Fade(1, 0, 1, color="#e25")
    
    $ diam = ImageDissolve(im.Tile(get_image_7dl("gui/pattern.jpg")), 1.1, 1)
    $ fdiam = ImageDissolve(im.Tile(get_image_7dl("gui/pattern.jpg")), 0.4, 1)
    $ fulldiam = MultipleTransition([False,fdiam,get_image_7dl("gui/digi1.jpg"),fdiam,True])
    
    $ gopr = ImageDissolve(im.Tile(get_image_7dl("gui/blackout_go.png")), 0.95, 1)
    $ swradar = ImageDissolve(im.Tile(get_image_7dl("gui/blackout3.jpg")), 0.95, 1)
    $ joff = MultipleTransition([False,swradar,Solid("#000"),swradar,True])
    $ swradarr = ImageDissolve(im.Tile(get_image_7dl("gui/blackout32.jpg")), 0.95, 1)
    $ joffr = MultipleTransition([False,swradarr,Solid("#000"),swradarr,True])
    
    $ blind_d = ImageDissolve(im.Tile(get_image_7dl("gui/roof_ks.jpg")), 1.3)
    $ blinds_l = ImageDissolve(im.Tile(get_image_7dl("gui/roof_ks2.jpg")), 0.6)
    $ blinds_r = ImageDissolve(im.Tile(get_image_7dl("gui/roof_ks3.jpg")), 0.7)
    
    $ blind_l = MultipleTransition([False,blinds_l,Solid("#011"),blinds_r,True])
    $ blind_r = MultipleTransition([False,blinds_r,Solid("#011"),blinds_l,True])
    $ touch = ImageDissolve(im.Tile(get_image_7dl("gui/pattern2.jpg")), 0.9, 1)
    $ dspq = Dissolve(0.04, alpha=True)
    $ dsps = Dissolve(3.0, alpha=True)
    $ guess_on = ImageDissolve(get_image_7dl("blackpalm.png"), 0.25, ramplen=256, reverse=True)
    $ guess_off = ImageDissolve(get_image_7dl("blackpalm.png"), 0.3, ramplen=256)
#Анимы
    image anim_digi:
        get_image_7dl("gui/digi1.jpg")  with Dissolve(1.5) 
        pause 1.5
        get_image_7dl("gui/digi2.jpg")  with Dissolve(1.5) 
        pause 1.5
        repeat
    
    image anim_grain: #Смэртельный номер: тянем картинку, делаем прозрачной и запускаем в секвенцию - и всё в коде!
        filmetile(get_image_7dl("gui/alt_noise1.png"))
        pause 0.1
        filmetile(get_image_7dl("gui/alt_noise2.png"))
        pause 0.1
        filmetile(get_image_7dl("gui/alt_noise3.png"))
        pause 0.1
        repeat
        
    image anim_intro_recall:
        "images/1080/bg/semen_room.jpg"
        pause 0.1
        "images/1080/bg/semen_room_window.jpg"
        pause 0.1
        "images/1080/anim/intro_1.jpg"
        pause 0.1
        "images/1080/anim/intro_2.jpg"
        pause 0.1
        "images/1080/anim/intro_3.jpg"
        pause 0.1
        "images/1080/anim/intro_4.jpg"
        pause 0.1
        "images/1080/anim/intro_5.jpg"
        pause 0.1
        "images/1080/anim/intro_6.jpg"
        pause 0.1
        "images/1080/anim/intro_8.jpg"
        pause 0.1
        "images/1080/anim/prolog_2.jpg"
        pause 0.1
        "images/1080/anim/prolog_1.jpg"
        pause 0.1
        "images/1080/anim/intro_9.jpg"
        pause 0.1
        "images/1080/anim/intro_10.jpg"
        pause 0.1
        "images/1080/anim/intro_11.jpg"
        pause 0.1
        "images/1080/anim/intro_13.jpg"
        pause 0.1
        "images/1080/bg/intro_xx.jpg"
        pause 0.1
        repeat
        
    image anim_square_party:
        "images/1080/bg/ext_square_night_party.jpg" with Dissolve(.5) 
        pause 0.6
        "images/1080/bg/ext_square_night_party2.jpg" with Dissolve(.5) 
        pause 0.6
        repeat
        
    image anim_square_preparty:
        get_image_7dl("bg/ext_square_sunset3_7dl.jpg") with Dissolve(1.5) 
        pause 1.6
        get_image_7dl("bg/ext_square_sunset2_7dl.jpg") with Dissolve(1.5) 
        pause 1.4
        repeat
    
    image uv_bus:
        get_sprite_7dl("misc/uv_alt1.png")
        pause 0.5
        get_sprite_7dl("misc/uv_alt2.png") 
        pause 0.5
        get_sprite_7dl("misc/uv_alt3.png")
        pause 0.5
        get_sprite_7dl("misc/uv_alt2.png")
        pause 0.5
        get_sprite_7dl("misc/uv_alt1.png")
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
                                  (0,0), salute_main(get_image_7dl("spoloh1.png")),
                                  (0,0), salute_main(get_image_7dl("spoloh11.png")),
                                  (0,0), salute_main(get_image_7dl("spoloh2.png")),
                                  (0,0), salute_main(get_image_7dl("spoloh21.png")),
                                  (0,0), salute_main(get_image_7dl("spoloh3.png")),

                                  (0,0), salute_main(get_image_7dl("spoloh4.png")),
                                  (0,0), salute_main(get_image_7dl("spoloh41.png")),
                                  (0,0), salute_main(get_image_7dl("spoloh5.png")),
                                  (0,0), salute_main(get_image_7dl("spoloh51.png")),
                                  (0,0), salute_main(get_image_7dl("spoloh6.png")),
                                  (0,0), salute_main(get_image_7dl("spoloh61.png")),
                                  (0,0), salute_main(get_image_7dl("spoloh7.png")),
                                  (0,0), salute_main(get_image_7dl("spoloh71.png")),

                                  (0,0), salute_main(get_image_7dl("spoloh91.png")),
                                  (0,0), salute_main(get_image_7dl("spoloh9.png")))

    
    image timer_anim: 
        get_image_7dl("gui/win.png") 
        0.1 #Задержка
        get_image_7dl("gui/win2.png")
        0.1
        get_image_7dl("gui/win3.png")
        0.1
        repeat # Не убирать
        
    image ftl_anim: 
        get_image_7dl("gui/ftl1.png") 
        0.1 #Задержка
        get_image_7dl("gui/ftl2.png")
        0.1
        get_image_7dl("gui/ftl3.png")
        0.1
        repeat # Не убирать
        
    image un serious dress anim: 
        get_sprite_7dl("misc/un_3_dress_serious_1.png") 
        8.0 #Задержка
        get_sprite_7dl("misc/un_3_dress_serious_2.png")
        0.1
        get_sprite_7dl("misc/un_3_dress_serious_1.png") 
        4.0 #Задержка
        get_sprite_7dl("misc/un_3_dress_serious_2.png")
        0.15
        get_sprite_7dl("misc/un_3_dress_serious_1.png") 
        7.0 #Задержка
        get_sprite_7dl("misc/un_3_dress_serious_2.png")
        0.1
        repeat # Не убирать
#Заставки
    image bg ext_stand3_night_7dl = im.MatrixColor(get_image_7dl("bg/ext_stand3_7dl.jpg"), im.matrix.tint(0.63, 0.78, 0.82))
    image bg ext_stand3_sunset_7dl = im.MatrixColor(get_image_7dl("bg/ext_stand3_7dl.jpg"), im.matrix.tint(0.94, 0.82, 1.0))
    image bg ext_stand3_prolog_7dl = im.MatrixColor(get_image_7dl("bg/ext_stand_pr_7dl.jpg"), im.matrix.tint(0.82, 0.84, 1.0))
    
#Задники
    image bg ext_adductius_7dl = get_image_7dl("bg/ext_adductius_7dl.png")
    image bg ext_admins_day_7dl = get_image_7dl("bg/ext_admins_day_7dl.jpg")
    image bg ext_admins_night_7dl = get_image_7dl("bg/ext_admins_night_7dl.jpg")
    image bg ext_admins_rain_7dl = get_image_7dl("bg/ext_admins_rain_7dl.jpg")
    image bg ext_aidpost_sunset_7dl = get_image_7dl("bg/ext_med_sunset_7dl.jpg")
    image bg ext_aidpost2_sunset_7dl = get_image_7dl("bg/ext_med2_sunset_7dl.jpg")
    
    image bg ext_backdoor_day_7dl = get_image_7dl("bg/ext_backdoor_day_7dl.png")
    image bg ext_backdoor_night_7dl = get_image_7dl("bg/ext_backdoor_night_7dl.png")
    image bg ext_bathhouse_day_7dl = get_image_7dl("bg/ext_bathhouse_day_7dl.jpg")
    image bg ext_backroad_day_7dl = get_image_7dl("bg/ext_backroad_day_7dl.png")
    image bg ext_beach2_day_7dl = get_image_7dl("bg/ext_beach2_day_7dl.jpg")
    image bg ext_boathouse_sunset_7dl = get_image_7dl("bg/ext_boathouse_sunset_7dl.jpg")
    image bg ext_boathouse_alt_day_7dl = get_image_7dl("bg/ext_boathouse_alt_day_7dl.png")
    image bg ext_bus1_7dl = get_image_7dl("bg/ext_bus1_7dl.jpg")
    image bg ext_busstop_dust_7dl = get_image_7dl("bg/ext_busstop_dust_7dl.png")
    image bg ext_busstop_sun_7dl = get_image_7dl("bg/ext_busstop_sun_7dl.png")
    
    image bg ext_city_night_7dl = get_image_7dl("bg/outro/ext_city_night_7dl.png")
    image bg ext_clubs_sunset_rain_7dl = get_image_7dl("bg/ext_clubs_sunset_rain_7dl.jpg")
    image bg ext_countryside_day_7dl = get_image_7dl("bg/outro/ext_countryside_day_7dl.jpg")
    
    image bg ext_dining_hall_near_snowy_day_7dl = get_image_7dl("bg/outro/ext_dining_hall_near_snowy_day_7dl.jpg")
    
    image bg ext_earth_7dl = get_image_7dl("bg/outro/ext_earth_7dl.jpg")
    
    image bg ext_entrance_night_clear_7dl = get_image_7dl("bg/ext_entrance_night_clear_7dl.png")
    image bg ext_entrance_night_clear_closed_7dl = get_image_7dl("bg/ext_entrance_night_clear_closed_7dl.png")
    image bg ext_entrance_winter_7dl = get_image_7dl("bg/outro/ext_entrance_winter_7dl.jpg")
    
    image bg ext_graveyard_rain_7dl = get_image_7dl("bg/outro/ext_graveyard_rain_7dl.jpg")
    
    image bg ext_hospital2_away_day_7dl = get_image_7dl("bg/ext_hospital2_away_day_7dl.jpg")
    image bg ext_hospital2_away_night_7dl = get_image_7dl("bg/ext_hospital2_away_night_7dl.jpg")
    image bg ext_houses_night_7dl = get_image_7dl("bg/ext_houses_night_7dl.jpg")
    image bg ext_houses_rainy_day_7dl = get_image_7dl("bg/ext_houses_rainy_day_7dl.jpg")
    image bg ext_houses_snowy_day_7dl = get_image_7dl("bg/outro/ext_houses_snowy_day_7dl.jpg")
    image bg ext_house_of_mt_snowy_day_7dl = get_image_7dl("bg/outro/ext_house_of_mt_snowy_day_7dl.jpg")
    image bg ext_house_of_un_night_7dl = get_image_7dl("bg/ext_house_of_un_night_7dl.jpg")
    
    image bg ext_khruschevka_day_7dl = get_image_7dl("bg/outro/ext_khruschevka_day_7dl.jpg")
    
    image bg ext_lib_sunset_7dl = get_image_7dl("bg/ext_lib_sunset_7dl.jpg")
    image bg ext_lake_day_7dl = get_image_7dl("bg/ext_lake_day_7dl.png")
    image bg ext_lake_night_7dl = get_image_7dl("bg/ext_lake_night_7dl.png")
    image bg ext_lake_sunset_7dl = get_image_7dl("bg/ext_lake_sunset_7dl.png")
    
    image bg ext_musclub_night_7dl = get_image_7dl("bg/ext_musclub_night_7dl.jpg")
    image bg ext_musclub_snowy_day_7dl = get_image_7dl("bg/outro/ext_musclub_snowy_day_7dl.jpg")
    image bg ext_mv2_7dl = get_image_7dl("bg/outro/ext_mv2_7dl.jpg")
    
    image bg ext_night_sky_7dl = get_image_7dl("bg/ext_night_sky_7dl.jpg")
    
    image bg ext_old_building_day_7dl = get_image_7dl("bg/ext_old_building_day_7dl.jpg")
    
    image bg ext_playground2_7dl = get_image_7dl("bg/ext_playground2_7dl.jpg")
    
    image bg ext_road_sunset_7dl = get_image_7dl("bg/ext_road_sunset_7dl.jpg")
    image bg ext_road_winter_7dl = get_image_7dl("bg/outro/ext_road_winter_7dl.jpg")
    image bg ext_railbridge_sunset_7dl = get_image_7dl("bg/outro/ext_railbridge_sunset_7dl.png")
    
    image bg ext_sandpit_day_7dl = get_image_7dl("bg/ext_sandpit_day_7dl.png")
    image bg ext_stairs_day_7dl = get_image_7dl("bg/ext_stairs_day_7dl.jpg")
    image bg ext_stairs_night_7dl = get_image_7dl("bg/ext_stairs_night_7dl.jpg")
    image bg ext_stairs_sunset_7dl = get_image_7dl("bg/ext_stairs_sunset_7dl.jpg")
    image bg ext_seashore_7dl = get_image_7dl("bg/ext_seashore_7dl.jpg")
    image bg ext_shower_day_7dl = get_image_7dl("bg/ext_shower_day_7dl.jpg")
    image bg ext_shower_night_7dl = get_image_7dl("bg/ext_shower_night_7dl.jpg")
    image bg ext_sky_7dl = get_image_7dl("bg/ext_sky_7dl.jpg")
    image bg ext_sky2_7dl = get_image_7dl("bg/ext_sky2_7dl.jpg")
    image bg ext_stage_big_sunset_7dl = get_image_7dl("bg/ext_stage_big_sunset_7dl.jpg")
    image bg ext_stage_big_clear_day_7dl = get_image_7dl("bg/ext_stage_big_clear_day_7dl.jpg")
    image bg ext_stage_near_clear_7dl = get_image_7dl("bg/ext_stage_near_clear_7dl.jpg")
    image bg ext_stand3_7dl = get_image_7dl("bg/ext_stand3_7dl.jpg")
    image bg ext_stand_pr_7dl = get_image_7dl("bg/ext_stand_pr_7dl.jpg")
    image bg ext_square_rain_day_7dl = get_image_7dl("bg/ext_square_rain_day_7dl.jpg")
    image bg ext_square_sunset2_7dl = get_image_7dl("bg/ext_square_sunset2_7dl.jpg")
    image bg ext_square_sunset3_7dl = get_image_7dl("bg/ext_square_sunset3_7dl.jpg")
    
    image bg ext_townscape_ph_day_7dl = get_image_7dl("bg/ext_townscape_ph_day_7dl.png")
    image bg ext_tennis_court_7dl = get_image_7dl("bg/ext_tennis_court_7dl.jpg")
    image bg ext_underwater_7dl = get_image_7dl("bg/ext_underwater_7dl.jpg")
    
    image bg ext_un_hideout_day_7dl = get_image_7dl("bg/ext_un_hideout_day_7dl.png")
    image bg ext_un_hideout_night_7dl = get_image_7dl("bg/ext_un_hideout_night_7dl.png")
    image bg ext_un_hideout_sunset_7dl = get_image_7dl("bg/ext_un_hideout_sunset_7dl.png")
    image bg ext_un_house_with_un_7dl = get_image_7dl("bg/ext_un_house_with_un_7dl.jpg")
    
    image bg ext_volley_court_7dl = get_image_7dl("bg/ext_volley_court_7dl.png")
    
    image bg ext_warehouse_day_7dl = get_image_7dl("bg/ext_warehouse_day_7dl.jpg")
    image bg ext_warehouse2_day_7dl = get_image_7dl("bg/ext_warehouse2_day_7dl.jpg")
    image bg ext_warehouse_blurry_7dl = get_image_7dl("bg/ext_warehouse_blurry_7dl.jpg")
    image bg ext_warehouse_night_7dl = get_image_7dl("bg/ext_warehouse_night_7dl.jpg")
    image bg ext_washstand_night_7dl = get_image_7dl("bg/ext_washstand_night_7dl.jpg")
    image bg ext_winter_night_7dl = get_image_7dl("bg/outro/ext_winter_night_7dl.jpg")
    image bg ext_winterpark_7dl = get_image_7dl("bg/outro/ext_winterpark_7dl.jpg")
    image bg ext_winterpark_sunset_7dl = get_image_7dl("bg/outro/ext_winterpark_sunset_7dl.jpg")
    
    image bg int_access_day_7dl = get_image_7dl("bg/int_access_day_7dl.jpg")
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
    image bg int_concert_room_7dl = get_image_7dl("bg/int_concert_room_7dl.jpg")
    
    image bg int_d3_hideout_7dl = get_image_7dl("bg/int_d3_hideout_7dl.jpg")
    
    image bg int_dining_hall_people_rain_7dl = get_image_7dl("bg/int_dinning_hall_people_rain_7dl.jpg")
    image bg int_dining_hall_rain_7dl = get_image_7dl("bg/int_dinning_hall_rain_7dl.jpg")
    
    image bg int_editorial_day_7dl = get_image_7dl("bg/int_editorial_day_7dl.jpg")
    image bg int_epilogue_bg_7dl = get_image_7dl("bg/outro/int_epilogue_bg_7dl.jpg")
    image bg int_extra_house_7dl = get_image_7dl("bg/int_extra_house_7dl.jpg")
    image bg int_extra_house_day_7dl = get_image_7dl("bg/int_extra_house_day_7dl.jpg")
    
    image bg int_hence_day_7dl = get_image_7dl("bg/int_hence_day_7dl.jpg")
    image bg int_hence_night_7dl = get_image_7dl("bg/int_hence_night_7dl.jpg")
    image bg int_home_lift_7dl = get_image_7dl("bg/int_home_lift_7dl.png")
    image bg int_hospital_hall_day_7dl = get_image_7dl("bg/int_hospital_hall_day_7dl.jpg")
    
    image bg int_intro_liaz_7dl = get_image_7dl("bg/int_intro_liaz_7dl.jpg")
    
    image bg int_looney_bin_7dl = get_image_7dl("bg/int_looney_bin_7dl.jpg")
    image bg int_looney_bin_nightmare_7dl = get_image_7dl("bg/int_looney_bin_nightmare_7dl.jpg")
    
    image bg int_mine_heart_7dl = get_image_7dl("bg/int_mine_heart_7dl.jpg")
    image bg int_mine_halt_left_7dl = get_image_7dl("bg/int_mine_halt_left_7dl.jpg")
    image bg int_mine_room2_7dl = get_image_7dl("bg/int_mine_room2_7dl.jpg")
    image bg int_mine_water_7dl = get_image_7dl("bg/int_mine_water_7dl.jpg")
    image bg int_mt_sam_room_close_7dl = get_image_7dl("bg/int_mt_sam_room_close_7dl.jpg")
    image bg int_mt_sam_room_7dl = get_image_7dl("bg/int_mt_sam_room_7dl.jpg")
    image bg int_mt_sam_room_away_7dl = get_image_7dl("bg/int_mt_sam_room_away_7dl.jpg")
    
    image bg int_old_building_day_7dl = get_image_7dl("bg/int_old_building_day_7dl.jpg")
    image bg int_opened_door_7dl = get_image_7dl("bg/outro/int_opened_door_7dl.jpg")
    
    image bg int_plats_7dl = get_image_7dl("bg/outro/int_plats_7dl.jpg")
    image bg int_potato_storage_7dl = get_image_7dl("bg/int_potato_storage_7dl.png")
    image bg int_refinery_7dl = get_image_7dl("bg/int_refinery_7dl.png")
    
    image bg int_sam_house_clean_7dl = get_image_7dl("bg/int_sam_house_clean_7dl.jpg")
    image bg int_sam_room_7dl = get_image_7dl("bg/int_sam_room_7dl.png")
    image bg int_warehouse_day_7dl = get_image_7dl("bg/int_warehouse_day_7dl.png")
    image bg int_warehouse_night_7dl = get_image_7dl("bg/int_warehouse_night_7dl.png")
    image bg int_sporthall_day_7dl = get_image_7dl("bg/int_sporthall_day_7dl.png")
    image bg int_sporthall_night_7dl = get_image_7dl("bg/int_sporthall_night_7dl.png")
    image bg int_store_7dl = get_image_7dl("bg/int_store_7dl.png")
    
    image bg int_toilet_7dl = get_image_7dl("bg/outro/int_toilet_7dl.jpg")
    image bg int_train_7dl = get_image_7dl("bg/int_train_7dl.png")
    
    image bg int_wardrobe_7dl = get_image_7dl("bg/int_wardrobe_7dl.jpg")
    image bg int_wardrobe2_7dl = get_image_7dl("bg/int_wardrobe2_7dl.jpg")
    
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
    image cg d3_mi_dance_afar_7dl = get_image_7dl("cg/d3_mi_dance_afar_7dl.jpg")
    image cg d3_mi_dance_close_7dl = get_image_7dl("cg/d3_mi_dance_close_7dl.jpg")
    image cg d3_me_mirror_white_7dl = get_image_7dl("cg/d3_me_mirror_white_7dl.jpg")
    image cg d3_me_mirror_bordo_7dl = get_image_7dl("cg/d3_me_mirror_bordo_7dl.jpg")
    image cg d3_sl_bath_unplaited_7dl = get_image_7dl("cg/d3_sl_bath_unplaited_7dl.jpg")
    image cg d3_sl_tease_7dl = get_image_7dl("cg/d3_sl_tease_7dl.jpg")
    image cg d3_sl_tease2_7dl = get_image_7dl("cg/d3_sl_tease2_7dl.jpg")
    image cg d3_sl_dance_bordo_7dl = get_image_7dl("cg/d3_sl_dance_bordo_7dl.jpg")
    image cg d3_un_dance_bordo_7dl = get_image_7dl("cg/d3_un_dance_bordo_7dl.jpg")
    
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
    
    image cg d4_sl_sleeping_7dl = get_image_7dl("cg/d4_sl_sleeping_7dl.jpg")
    image cg d4_sl_sleep_7dl = get_image_7dl("cg/d4_sl_sleep_7dl.jpg")
    image cg d4_sl_dnd_7dl = get_image_7dl("cg/d4_sl_dnd_7dl.jpg")
    
    image cg d4_un_7dl = get_image_7dl("cg/d4_un_7dl.jpg")
    
    image cg d4_us_stardust_7dl = get_image_7dl("cg/d4_us_stardust_7dl.png") #Тысяча огоньков
    
    image cg d4_volley_rage_7dl = get_image_7dl("cg/d4_volley_rage_7dl.jpg")
    
    image cg d5_me_Alisa_7dl = get_image_7dl("cg/d5_me_Alisa_7dl.jpg")
    image cg d5_mi_conv_7dl = get_image_7dl("cg/d5_mi_conv_7dl.jpg")
    image cg d5_mt_redress_7dl = get_image_7dl("cg/d5_mt_redress_7dl.jpg")
    image cg d5_boat_night_solo_7dl = get_image_7dl("cg/d5_boat_night_solo_7dl.jpg")
    image cg d5_rainy_idle_7dl = get_image_7dl("cg/d5_rainy_idle_7dl.jpg")
    image cg d5_sl_bed_7dl = get_image_7dl("cg/d5_sl_bed_7dl.jpg")
    image cg d5_sl_bench_7dl = get_image_7dl("cg/d5_sl_bench_7dl.jpg")
    image cg d5_sl_kissing_7dl = get_image_7dl("cg/d5_sl_kissing_7dl.png")
    image cg d5_sl_moon_7dl = get_image_7dl("cg/d5_sl_moon_7dl.jpg")
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
    
    image cg d6_mi_boat_7dl = get_image_7dl("cg/d6_mi_boat_7dl.jpg")
    image cg d6_mi_cya_7dl = get_image_7dl("cg/d6_mi_cya_7dl.jpg")
    
    image cg d6_mi_departure_7dl = get_image_7dl("cg/d6_mi_departure_7dl.png")
    image cg d6_mi_farewell_7dl = get_image_7dl("cg/d6_mi_farewell_7dl.jpg")
    image cg d6_mi_hugs_7dl = get_image_7dl("cg/d6_mi_hugs_7dl.png")
    image cg d6_mi_leaving_7dl = get_image_7dl("cg/d6_mi_leaving_7dl.jpg")
    image cg d6_mi_morning_7dl = get_image_7dl("cg/d6_mi_morning_7dl.jpg")
    image cg d6_mi_swimming_7dl = get_image_7dl("cg/d6_mi_swimming_7dl.jpg")
    
    image cg d6_mi_vyluthere_7dl = get_image_7dl("cg/d6_mi_vyluthere_7dl.jpg")
    image cg d6_sl_clean_7dl = get_image_7dl("cg/d6_sl_clean_7dl.jpg")
    image cg d6_sl_zettai_7dl = get_image_7dl("cg/d6_sl_zettai_7dl.jpg")
    image cg d6_un_evening_0_7dl = get_image_7dl("cg/d6_un_evening_0_7dl.jpg")
    image cg d6_un_evening_3_7dl = get_image_7dl("cg/d6_un_evening_3_7dl.jpg")
    image cg d6_un_evening_0_1_7dl = get_image_7dl("cg/d6_un_evening_0_1_7dl.jpg")
    image cg d6_un_evening_0_2_7dl = get_image_7dl("cg/d6_un_evening_0_2_7dl.jpg")
    
    #image cg d6_us_lost_road_7dl = get_image_7dl("cg/d6_us_lost_road_7dl.png")
    
    image cg d7_dv_alice_dj_7dl = get_image_7dl("cg/d7_dv_alice_dj_7dl.jpg")
    image cg d7_dv_looney_7dl = get_image_7dl("cg/d7_dv_looney_7dl.png")
    image cg d7_dv_addic_happy_7dl = get_image_7dl("cg/d7_dv_addic_happy_7dl.jpg")
    image cg d7_dv_bed_7dl = get_image_7dl("cg/d7_dv_bed_7dl.jpg")
    image cg d7_dv_ep_red_7dl = get_image_7dl("cg/d7_dv_ep_red_7dl.jpg")
    image cg d7_dv_noir_7dl = get_image_7dl("cg/d7_dv_noir_7dl.jpg")
    image cg d7_dv_epilogue_kissing_7dl = get_image_7dl("cg/d7_dv_epilogue_kissing_7dl.jpg")
    image cg d7_dv_epilogue_bus_7dl = get_image_7dl("cg/d7_dv_epilogue_bus_7dl.jpg")
    image cg d7_dv_rf_reject_7dl = get_image_7dl("cg/d7_dv_rf_reject_7dl.jpg")
    
    image cg d7_frozen_7dl = get_image_7dl("cg/d7_frozen_7dl.jpg")
    image cg d7_leaving_no_sh_7dl = get_image_7dl("cg/d7_leaving_no_sh_7dl.jpg")
    image cg d7_leaving_no_sl_7dl = get_image_7dl("cg/d7_leaving_no_sl_7dl.jpg")
    image cg d7_leaving_no_sl_sam_7dl = get_image_7dl("cg/d7_leaving_no_sl_sam_7dl.jpg")
    
    image cg d6_mi_cry_sleeping_7dl = get_image_7dl("cg/d6_mi_cry_sleeping_7dl.png")

    image cg d7_mi_club27_7dl = get_image_7dl("cg/d7_mi_club27_7dl.jpg")
    image cg d7_mi_epilogue_7dl = get_image_7dl("cg/d7_mi_epilogue_7dl.jpg")
    image cg d7_mi_farewell_7dl = get_image_7dl("cg/d7_mi_farewell_7dl.jpg")
    image cg d7_mi_hugs_7dl = get_image_7dl("cg/d7_mi_hugs_7dl.jpg")
    
    image cg d7_mi_hands_tight_7dl = get_image_7dl("cg/d7_mi_hands_tight_7dl.jpg")
    image cg d7_mi_hands_split_7dl = get_image_7dl("cg/d7_mi_hands_split_7dl.jpg")
    image cg d7_mi_hands_2gether_7dl = get_image_7dl("cg/d7_mi_hands_2gether_7dl.jpg")
    
    image cg d7_mi_kaito_7dl = get_image_7dl("cg/d7_mi_kaito_7dl.jpg")
    image cg d7_mi_letter_7dl = get_image_7dl("cg/d7_mi_letter_7dl.jpg")
    image cg d7_mi_lost_7dl = get_image_7dl("cg/d7_mi_lost_7dl.png")
    image cg d7_mi_letter_rain_7dl = get_image_7dl("cg/d7_mi_letter_rain_7dl.jpg")
    image cg d7_mi_letter_rain_tears_7dl = get_image_7dl("cg/d7_mi_letter_rain_tears_7dl.jpg")
    image cg d7_mi_meeting_7dl = get_image_7dl("cg/d7_mi_meeting_7dl.jpg")
    image cg d7_mi_ramen_7dl = get_image_7dl("cg/d7_mi_ramen_7dl.jpg")
    image cg d7_mi_reenter_7dl = get_image_7dl("cg/d7_mi_reenter_7dl.png")
    image cg d7_mi_shesgone_7dl = get_image_7dl("cg/d7_mi_shesgone_7dl.jpg") #Свежачок от Макса
    image cg d7_mi_sparkle_7dl = get_image_7dl("cg/d7_mi_sparkle_7dl.jpg")
    image cg d7_mi_sunk_7dl = get_image_7dl("cg/d7_mi_sunk_7dl.jpg")
    
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
    
    #image cg d7_us_bus_stop_7dl = get_image_7dl("cg/d7_us_bus_stop_7dl.png")
    image cg d7_us_pixie_7dl = get_image_7dl("cg/d7_us_pixie_7dl.png")
    #image cg d7_us_no_mans_land_7dl = get_image_7dl("cg/d7_us_no_mans_land_7dl.png")
    
    #image cg d7_walkman_7dl = get_image_7dl("cg/d7_walkman_7dl.jpg")
    #image cg d7_walkman_7dl = get_image_7dl("cg/d7_walkman_7dl.png")
    image cg d7_bus_night_7dl = get_image_7dl("cg/d7_bus_night_7dl.jpg")
    
#Турнир
    image alt_tournament_bg = get_image_7dl("gui/tournament/alt_tournament_bg.png")
    image sal_black = Solid("#00000000")
    image sal_splash = Solid("#FFFFFF66")
    image alt_KS_censor = get_image_7dl("alt_KS_censor.png")
    image alt_KS_censor2 = get_image_7dl("alt_KS_censor2.png")
    
    
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
    image ldb_blind = get_image_7dl("gui/ldb_blind.png")
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
    image rain_overlay = get_image_7dl("gui/rain_overlay.png")
    image intro_transparent = get_image_7dl("gui/intro/intro_transparent.png")

#Элементы интерфейса
    image blackout = get_image_7dl("gui/blackout.png")
    image blackout2 = get_image_7dl("gui/blackout2.png")
    image blackout_exh = get_image_7dl("gui/blackout_exh.png")
    image blackout_exh2 = get_image_7dl("gui/blackout_exh2.png")
    image blackout_exh3 = get_image_7dl("gui/blackout_exh3.png")
    image genda_portrait = get_image_7dl("gui/genda_portrait.png")
    image gfx bokeh = get_image_7dl("gui/splatter.png")
    
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
    image dvsem_el = get_image_7dl("gui/maps/dvsem_el.png")
    image eye_s = get_image_7dl("gui/eye_s.png")
#Сотик
    image frame = get_image_7dl("gui/phone/frame.png")
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
    image acm_logo_dv_drunk = get_image_7dl("gui/acm_logo_dv_drunk.png")
    image acm_logo_dv_gohome = get_image_7dl("gui/acm_logo_dv_gohome.png")
    image acm_logo_dv_meetmethere = get_image_7dl("gui/acm_logo_dv_meetmethere.png")
    image acm_logo_dv_morethanlife = get_image_7dl("gui/acm_logo_dv_morethanlife.png")
    image acm_logo_dv_theresnoway = get_image_7dl("gui/acm_logo_dv_theresnoway.png")
    image acm_logo_dv_tillend = get_image_7dl("gui/acm_logo_dv_tillend.png")
    image acm_logo_dv_tulpa = get_image_7dl("gui/acm_logo_dv_tulpa.png")
    image acm_logo_me_lamp = get_image_7dl("gui/acm_logo_me_lamp.png") 
    image acm_logo_dv_ussr_good = get_image_7dl("gui/acm_logo_dv_ussr_good.png")
    
    image acm_logo_me_deep = get_image_7dl("gui/acm_logo_me_deep.png")
    image acm_logo_me_lamp = get_image_7dl("gui/acm_logo_me_lamp.png")
    image acm_logo_me_qte = get_image_7dl("gui/acm_logo_me_qte.png")
    
    image acm_logo_mi_allyours = get_image_7dl("gui/acm_logo_mi_allyours.png")
    image acm_logo_mi_namiki = get_image_7dl("gui/acm_logo_mi_namiki.png")
    image acm_logo_mi_new_happy = get_image_7dl("gui/acm_logo_mi_new_happy.png")
    image acm_logo_mi_ricochet = get_image_7dl("gui/acm_logo_mi_ricochet.png")
    image acm_logo_mi_ungood = get_image_7dl("gui/acm_logo_mi_ungood.png")
    
    image acm_logo_mi_happy_again = get_image_7dl("gui/acm_logo_mi_happy_again.png")
    image acm_logo_mi_liar = get_image_7dl("gui/acm_logo_mi_liar.png")
    image acm_logo_mi_dark_dreams = get_image_7dl("gui/acm_logo_mi_dark_dreams.png")
    image acm_logo_mi_club27 = get_image_7dl("gui/acm_logo_mi_club27.png")
    image acm_logo_mi_sparkle = get_image_7dl("gui/acm_logo_mi_sparkle.png")
    image acm_logo_mi_bitter_truth = get_image_7dl("gui/acm_logo_mi_bitter_truth.png")
    image acm_logo_mi_dam_cpu = get_image_7dl("gui/acm_logo_mi_dam_cpu.png")
    image acm_logo_mi_unlike = get_image_7dl("gui/acm_logo_mi_unlike.png")
    image acm_logo_mi_come = get_image_7dl("gui/acm_logo_mi_come.png")
    image acm_logo_mi_watashi = get_image_7dl("gui/acm_logo_mi_watashi.png")
    image acm_logo_mi_thank_you = get_image_7dl("gui/acm_logo_mi_thank_you.png")
    
    image acm_logo_mt_cause = get_image_7dl("gui/acm_logo_mt_cause.png")
    image acm_logo_mt_ending = get_image_7dl("gui/acm_logo_mt_ending.png")
    image acm_logo_mt_ever_after = get_image_7dl("gui/acm_logo_mt_ever_after.png")
    image acm_logo_mt_named_olga = get_image_7dl("gui/acm_logo_mt_named_olga.png")
    
    image acm_logo_sl_bad = get_image_7dl("gui/acm_logo_sl_bad.png")
    image acm_logo_sl_be_ok = get_image_7dl("gui/acm_logo_sl_be_ok.png")
    image acm_logo_sl_fantazm = get_image_7dl("gui/acm_logo_sl_fantazm.png")
    image acm_logo_sl_good = get_image_7dl("gui/acm_logo_sl_good.png")
    image acm_logo_sl_lone = get_image_7dl("gui/acm_logo_sl_lone.png")
    image acm_logo_sl_ok = get_image_7dl("gui/acm_logo_sl_ok.png")
    image acm_logo_sl_same_place = get_image_7dl("gui/acm_logo_sl_same_place.png")
    image acm_logo_sl_too_late = get_image_7dl("gui/acm_logo_sl_too_late.png")
    image acm_logo_sl_worth = get_image_7dl("gui/acm_logo_sl_worth.png")
    
    image acm_logo_un_good = get_image_7dl("gui/acm_logo_un_good.png")
    image acm_logo_un_good2 = get_image_7dl("gui/acm_logo_un_good2.png")
    image acm_logo_un_shelter = get_image_7dl("gui/acm_logo_un_shelter.png")
    image acm_logo_un_sui = get_image_7dl("gui/acm_logo_un_sui.png")
    image acm_logo_un_transit = get_image_7dl("gui/acm_logo_un_transit.png")
    
    image acm_logo_us_bad = get_image_7dl("gui/acm_logo_us_bad.png")
    image acm_logo_us_fairytale = get_image_7dl("gui/acm_logo_us_fairytale.png")
    image acm_logo_us_hi = get_image_7dl("gui/acm_logo_us_hi.png")
    image acm_logo_us_openup = get_image_7dl("gui/acm_logo_us_openup.png")
    image acm_logo_us_semische = get_image_7dl("gui/acm_logo_us_semische.png")
    
    image achieve_beagod = get_image_7dl("gui/achieve_beagod.png")
    image acm_logo = get_image_7dl("gui/acm_logo1.png") #Логотип сюжета
    
    image myst_mh = get_image_7dl("gui/myst_mh.png")
    
    image dreamgirl_overlay = get_image_7dl("gui/dreamgirl_overlay.png")
    image wet1 = get_image_7dl("gui/wet1.png")
    image volley_fight = get_image_7dl("gui/volley_fight.png")
    
#Картинки с использованием прозрачности и прочая спрайтовость
    image dv normal flipped = Transform("dv normal pioneer", xzoom=-1.0)
    image dv normal flipped far = Transform("dv normal pioneer far", xzoom=-1.0)
    image sl normal flipped = Transform("sl normal pioneer", xzoom=-1.0)
    image sl serious flipped = Transform("sl serious pioneer", xzoom=-1.0)
    #image d3_miku_dance_blush flipped = Transform("d3_miku_dance_blush", xzoom=-1.0)
    image uv shade3 sized = Transform("uv shade3", zoom=.4)
    image uv shade4 sized = Transform("uv shade4", zoom=.4)
    image digi_pad = get_sprite_7dl("misc/digi_pad.png")
    image hands_together = get_sprite_7dl("misc/hands_together.png")
    image hands_together_tight = get_sprite_7dl("misc/hands_together_tight.png")
    image sl_trench = get_sprite_7dl("misc/sl_trench.png")
    image sl_trench2 = get_sprite_7dl("misc/sl_trench2.png")
    image cotocomb_lighter = get_sprite_7dl("misc/cotocomb_lighter.png")
    image d4_cat_door_frame = get_sprite_7dl("misc/d4_cat_door_frame.png")
    image d6_miku_cries = get_sprite_7dl("misc/d6_miku_cries.png")
    image mouth_dull = get_sprite_7dl("misc/mouth_dull.png")
    image mi_ru = get_sprite_7dl("misc/mi_ru.png")
    image mt_bus = get_sprite_7dl("misc/mt_bus.png")
    image uvao_d1 = get_sprite_7dl("misc/uvao_d1.png")
    image dv_mt = get_sprite_7dl("misc/dv_mt.png")
    image backpack = get_sprite_7dl("misc/backpack.png")
    image backpack_tiny = get_sprite_7dl("misc/backpack_tiny.png")
    image dv_us_volley = get_sprite_7dl("misc/dv_us_volley.png")
    
#Dnd
    image alt_cat_map_wireframe = get_image_7dl("gui/dnd/alt_cat_map_wireframe.png")
    image alt_cat_map = get_image_7dl("gui/dnd/alt_cat_map.png")
    image alt_cat_map_pathfinding = get_image_7dl("gui/dnd/alt_cat_map_pathfinding.png")
    image PolariodFrame = get_image_7dl("gui/PolariodFrame.png")
    
    
#Звучок
#ambience
    $ ambience_concert = get_ambience_7dl("tellyourworld_concert.ogg")
    $ ambience_elevator = get_ambience_7dl("ambience_elevator.ogg")
    $ ambience_explosive_post = get_ambience_7dl("ambience_explosive_post.ogg")
    $ ambience_night_city = get_ambience_7dl("ambience_night_city.ogg")
    $ ambience_railroad = get_ambience_7dl("railroad_ambience.ogg")
    $ ambience_rain = get_ambience_7dl("ambience_rain_loop.ogg")
    $ ambience_safe = get_ambience_7dl("ambience_safe.ogg")
    $ ambience_salute = get_ambience_7dl("ambience_salute.ogg")
    $ ambience_town_day = get_ambience_7dl("ambience_town_day.ogg")
    $ ambience_underwater = get_ambience_7dl("ambience_underwater.ogg")
    $ ambience_volley = get_ambience_7dl("ambience_volley.ogg")
    
    
#music
    $ alice_theme = get_music_7dl("alice_theme.ogg")
    $ afraid_of_destiny = get_music_7dl("afraid_of_destiny.ogg")
    $ anglegrinder = get_music_7dl("anglegrinder.ogg")
    $ areyouabully = get_music_7dl("areyouabully.ogg")
    $ are_you_there = get_music_7dl("are_you_there.ogg")
    $ ask_you_out = get_music_7dl("ask_you_out.ogg")
    
    $ bad_apple = get_music_7dl("bad_apple.ogg")
    $ beat_symphonic = get_music_7dl("beat_symphonic.ogg")
    $ beth = get_music_7dl("beth.ogg")
    $ betray_vol1 = get_music_7dl("betray_vol1.ogg")
    $ but_why = get_music_7dl("but_why.ogg")
    $ breath_again = get_music_7dl("breath_again.ogg")
    $ breath_me = get_music_7dl("breath_me.ogg")
    $ beasteye = get_music_7dl("beasteye.ogg")
    
    $ catch_the_hedge = get_music_7dl("catch_the_hedge.ogg")
    $ christmas_met = get_music_7dl("christmas_met.ogg")
    $ closetoyou = get_music_7dl("closetoyou.ogg")
    $ clueless_hope = get_music_7dl("clueless_hope.ogg")
    
    $ danceagain = get_music_7dl("danceagain.ogg")
    $ dance_with_me = get_music_7dl("dance_with_me.ogg")
    $ dance_with_me_piano = get_music_7dl("dance_with_me_piano.ogg")
    $ deadman = get_music_7dl("deadman.ogg")
    $ dead_silence = get_music_7dl("dead_silence.ogg")
    $ dedicated = get_music_7dl("dedicated.ogg")
    $ deep_inside = get_music_7dl("deep_inside.ogg")
    $ dropit = get_music_7dl("dropit.ogg")
    $ dv_guitar = get_music_7dl("dv_guitar.ogg")
    $ escape_2 = get_music_7dl("escape_2.ogg")
    $ exodus = get_music_7dl("Exodus.ogg")
    
    $ emptiness = get_music_7dl("emptiness.ogg")
    $ es_downmix = get_music_7dl("es_downmix.ogg")
    $ Everlasting_Summer_Alice = get_music_7dl("Everlasting_Summer_Alice.ogg")
    $ expose_the_hero = get_music_7dl("expose_the_hero.ogg")
    
    $ feel_you_inside = get_music_7dl("feel_you_inside.ogg")
    $ finale_farewell = get_music_7dl("finale_farewell.ogg")
    $ forgive_or_what = get_music_7dl("forgive_or_what.ogg")
    $ frostwithoutyou = get_music_7dl("frostwithoutyou.ogg")
    
    $ genki = get_music_7dl("genki.ogg")
    $ guitar_under_the_window = get_music_7dl("guitar_under_the_window.ogg")
    $ groovie = get_music_7dl("groovie.ogg")
    $ gonna_be_ok = get_music_7dl("gonna_be_ok.ogg")
    
    $ happy_ending = get_music_7dl("happy_ending.ogg")
    $ herc_death = get_music_7dl("herc_death.ogg")
        
    $ iamagod2 = get_music_7dl("iamagod2.ogg")
    $ iamsadiamsorry3 = get_music_7dl("iamsadiamsorry3.ogg")
    $ iamsadiamsorry2 = get_music_7dl("iamsadiamsorry2.ogg")
    $ iamsadiamsorry = get_music_7dl("iamsadiamsorry.ogg")
    $ intro1 = get_music_7dl("intro1.ogg")
    $ intro2 = get_music_7dl("intro2.ogg")
    $ iwantmagic = get_music_7dl("iwantmagic.ogg")
    
    $ knock = get_music_7dl("knock.ogg")
    $ kiss_you = get_music_7dl("kiss_you.ogg")
    
    $ lastlight_guitar = get_music_7dl("lastlight_guitar.ogg")
    $ lastlight_piano = get_music_7dl("lastlight_piano.ogg")
    $ laugh_throught_the_universe = get_music_7dl("laugh_throught_the_universe.ogg")
    $ lazy_olga = get_music_7dl("lazy_olga.ogg")
    $ last_pixie = get_music_7dl("last_pixie.ogg")
    $ lonesome_shepherd = get_music_7dl("lonesome_shepherd.ogg")
    $ liliac_ball = get_music_7dl("liliac_ball.ogg")
    $ loki_on_3 = get_music_7dl("loki_on_3.ogg")
    $ lullaby2 = get_music_7dl("lullaby2.ogg")
    
    $ lost_without_you = get_music_7dl("lost_without_you.ogg")
    $ longing = get_music_7dl("longing.ogg")
    $ ltyh = get_music_7dl("ltyh.ogg")
    $ lunar_anguish = get_music_7dl("lunar_anguish.ogg")
    $ lyrica_sg = get_music_7dl("lyrica_sg.ogg")
    $ lynn = get_music_7dl("lynn.ogg")

    $ mammal = get_music_7dl("mammal.ogg")
    $ meetmethere_tts = get_music_7dl("meetmethere_tts.ogg")
    $ me2ost = get_music_7dl("me2ost.ogg")
    $ melancholy_sun = get_music_7dl("melancholy_sun.ogg")
    $ misery = get_music_7dl("misery.ogg")
    $ moment = get_music_7dl("moment.ogg")
    $ more_than_alive = get_music_7dl("more_than_alive.ogg")
    $ my_only_hope= get_music_7dl("my_only_hope.ogg")
    
    $ nookie = get_music_7dl("nookie.ogg")
    $ no_hope_left = get_music_7dl("no_hope_left.ogg")
    $ nowyouseeme = get_music_7dl("nowyouseeme.ogg")
    
    $ old_kiss = get_music_7dl("old_kiss.ogg")
    $ ourfirstmet = get_music_7dl("ourfirstmet.ogg") 
    $ outer = get_music_7dl("Outer_Science.ogg") 
    $ out_of_your_tier = get_music_7dl("out_of_your_tier.ogg") 
    $ out_of_painkillers = get_music_7dl("out_of_painkillers.ogg") 
    
    $ pathways = get_music_7dl("pathways.ogg")
    $ Please_Reprise = get_music_7dl("Please_Reprise.ogg")
    $ pixies_playing = get_music_7dl("pixies_playing.ogg")
    $ polyhymnia_intro = get_music_7dl("polyhymnia_intro.ogg")
    $ polyhymnia_main = get_music_7dl("polyhymnia_main.ogg")
    $ ppk = get_music_7dl("ppk.ogg")
    $ prologue_1 = get_music_7dl("prologue_1.ogg")
    $ promise_to_meet_you = get_music_7dl("promise_to_meet_you.ogg")

    $ Redemption = get_music_7dl("Redemption.ogg")
    $ red_lights = get_music_7dl("red_lights.ogg")
    $ refuse_to_believe = get_music_7dl("refuse_to_believe.ogg")
    $ refuse_to_replay = get_music_7dl("refuse_to_replay.ogg")
    $ rewind = get_music_7dl("rewind.ogg")
    $ rightroad = get_music_7dl("rightroad.ogg")
    $ ritual2 = get_music_7dl("ritual2.ogg")
    $ runaway = get_music_7dl("runaway.ogg")
    
    $ Sad_Piano = get_music_7dl("Sad_Piano.ogg")
    $ sam_lullaby = get_music_7dl("sam_lullaby.ogg")
    $ scorpions = get_music_7dl("scorpions.ogg")
    $ Semische = get_music_7dl("Semische.ogg")
    $ seven_summer_days = get_music_7dl("seven_summer_days.ogg")
    $ sign_of_blood = get_music_7dl("sign_of_blood.ogg")
    $ silent_angel = get_music_7dl("silent_angel.ogg")
    $ sh_ai_rejuv = get_music_7dl("sh_ai_rejuv.ogg")
    $ shape_of_my_heart = get_music_7dl("shape_of_my_heart.ogg")
    $ sheiscool = get_music_7dl("sheiscool.ogg")
    $ shehasgone = get_music_7dl("shehasgone.ogg")
    $ shib_mono = get_music_7dl("shib_mono.ogg")
    $ shib_stereo = get_music_7dl("shib_stereo.ogg")
    $ shivers = get_music_7dl("shivers.ogg")
    $ slavyas_fantazm = get_music_7dl("slavyas_fantazm.ogg")
    $ sky_feather = get_music_7dl("sky_feather.ogg")
    $ sneakupon = get_music_7dl("sneakupon.ogg")
    $ so_cold = get_music_7dl("so_cold.ogg")
    $ so_lonely = get_music_7dl("so_lonely.ogg")
    $ someone_like_you_guitar = get_music_7dl("someone_like_you_guitar.ogg")
    $ splin = get_music_7dl("splin1.ogg")
    $ stilllovingyou = get_music_7dl("stilllovingyou.ogg")
    $ summer_ends_soon2 = get_music_7dl("summer_ends_soon2.ogg")

    $ take_my_hand = get_music_7dl("take_my_hand.ogg")
    $ tears_of = get_music_7dl("tears_of.ogg")
    $ tellyourworld = get_music_7dl("tellyourworld.ogg")
    $ temptation = get_music_7dl("temptation.ogg")
    $ tender_song = get_music_7dl("tender_song.ogg")
    $ there_you_are = get_music_7dl("loop_there_you_are!.ogg")
    $ the_way = get_music_7dl("the_way.ogg")
    $ thousand_little_things = get_music_7dl("thousand_little_things.ogg")
    $ thousand_of_pixies = get_music_7dl("thousand_of_pixies.ogg")
    $ tilltheend = get_music_7dl("tilltheend.ogg")
    $ timetowakeup = get_music_7dl("timetowakeup.ogg")
    $ to_the_sunrise = get_music_7dl("to_the_sunrise.ogg")
    $ too_quiet = get_music_7dl("too_quiet.ogg")
    
    $ uncertainity = get_music_7dl("uncertainity.ogg")
    $ unfulfilled = get_music_7dl("unfulfilled.ogg")
    $ uneven_me = get_music_7dl("uneven_me.ogg")
    $ unfinished_life = get_music_7dl("unfinished_life.ogg")
    $ unforgotten = get_music_7dl("unforgotten.ogg")#регистр
    $ unholy_you = get_music_7dl("unholy_you.ogg")
    
    $ vale = get_music_7dl("vale.ogg")
    $ vampire = get_music_7dl("vampire.ogg")
    
    $ walkingaway = get_music_7dl("walkingaway.ogg")
    $ what_am_i_doing_here = get_music_7dl("what_am_i_doing_here.ogg")
    $ what_cost = get_music_7dl("what_cost.ogg")
    $ whatnow = get_music_7dl("whatnow.ogg")
    $ wheres_wonderland = get_music_7dl("wheres_wonderland.ogg")
    $ will_you = get_music_7dl("will_you.ogg")
    $ wonderful_faraway = get_music_7dl("wonderful_faraway.ogg")
    
    $ you_were_late = get_music_7dl("you_were_late.ogg")
    $ you_are_human = get_music_7dl("you_are_human.ogg")
    $ you_are_soul = get_music_7dl("you_are_soul.ogg")
    $ you_are_star = get_music_7dl("you_are_star.ogg")
    $ youareours = get_music_7dl("youareours.ogg")
    $ youre_not_real = get_music_7dl("youre_not_real.ogg")
    
# sfx
    $ apple_bite = get_sfx_7dl("apple_bite.ogg")
    $ aunl = get_sfx_7dl("aunl.ogg")
    $ bed_squeak = get_sfx_7dl("bed_squeak.ogg")
    $ brake = get_sfx_7dl("brake.ogg")
    $ breath = get_sfx_7dl("breath.ogg")
    $ blanket = get_sfx_7dl("blanket.ogg")
    $ car_passing = get_sfx_7dl("car_passing.ogg")
    $ deagle_shot = get_sfx_7dl("deagle_shot.ogg")
    $ eat_horn = get_sfx_7dl("eat_horn.ogg")
    $ footsteps_grass = get_sfx_7dl("footsteps_grass.ogg")
    $ ghmm = get_sfx_7dl("ghm.ogg")
    $ hedgehog = get_sfx_7dl("hedgehog.ogg")
    $ highfive = get_sfx_7dl("highfive.ogg")
    $ intro_dr = get_sfx_7dl("intro_dr.ogg")
    $ KBtyping = get_sfx_7dl("KBtyping.ogg")
    $ kissing_sound = get_sfx_7dl("kissing_sound.ogg")
    $ makarych = get_sfx_7dl("makarych.ogg")
    $ miku_stomping = get_sfx_7dl("miku_stomping.ogg")
    $ metal_hit_on_metal = get_sfx_7dl("metal_hit_on_metal.ogg")
    $ mpbt = get_sfx_7dl("mpbt.ogg")
    $ phone_feedback = get_sfx_7dl("phone_feedback.ogg")
    $ pouring = get_sfx_7dl("pouring.ogg")
    $ pup_bark = get_sfx_7dl("pup_bark.ogg")
    $ push_the_button = get_sfx_7dl("push_the_button.ogg")
    $ raindrops_radio = get_sfx_7dl("raindrops_radio.ogg")
    $ reverse_bell = get_sfx_7dl("reverse_bell.ogg")
    $ ringtone = get_sfx_7dl("ringtone.ogg")
    #Озвучка заголовка роли by Noir Сычёв
    $ role_drisch = get_sfx_7dl("role_drisch.ogg")
    $ role_herc = get_sfx_7dl("role_herc.ogg")
    $ role_loki = get_sfx_7dl("role_loki.ogg")
    $ sigh_out = get_sfx_7dl("sigh_out.ogg")
    $ snap = get_sfx_7dl("snap.ogg")
    $ stahp = get_sfx_7dl("stahp.ogg")
    $ tearing = get_sfx_7dl("tearing.ogg")
    $ tousche = get_sfx_7dl("tousche.ogg")
    $ train_depart = get_sfx_7dl("train_depart.ogg")
    $ train_income = get_sfx_7dl("train_income.ogg")
    $ nesmogla = get_sfx_7dl("nesmogla.ogg")
    $ volley_hit = get_sfx_7dl("volley_hit.ogg")
    $ wakeup_horn = get_sfx_7dl("wakeup_horn.ogg")
    $ wakeup = get_sfx_7dl("wakeup.ogg")
    $ white_noise = get_sfx_7dl("white_noise.ogg")
    $ window_glass_break = get_sfx_7dl("window_glass_break.ogg")