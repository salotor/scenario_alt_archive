init:
    $ mods["scenario__sdl_selector"] = u"Селектор 7дл"
    $ mod_tags["scenario__sdl_selector"] = ["length:days","gameplay:vn","protagonist:male"]
    
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
        
label scenario__sdl_selector:

    $ init_map_zones_alt1()
    $ init_map_zones_alt2()
    $ alt_save_release_no = alt_release_no
    $ day_time()
    $ persistent.sprite_time = "day"

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
    $ plthr = u"Дрищ"
    play ambience ambience_7dl["safe"] fadein 5
    
label sdl_menu:
    scene scenery with dissolve
    menu:
        "Выбранный лейбл":
            $ persistent.altCardsWon1 = True
            $ persistent.altCardsWon2 = True
            $ persistent.altCardsWon3 = True
            stop ambience fadeout 2
            jump alt_test
        "Руты":
            menu:
                "С самого начала?":
                    menu:
                        "День Первый":
                            menu:
                                "Герк":
                                    $ herc = True
                                    $ plthr = u"Герк"
                                "Локи":
                                    $ loki = True
                                    $ plthr = u"Локи"
                                "Дрищ":
                                    $ plthr = u"Дрищ"
                            stop ambience fadeout 2
                            jump alt_day1_start
                        "День Первый Альтернативный":
                            menu:
                                "Герк":
                                    $ herc = True
                                    $ plthr = u"Герк"
                                "Локи":
                                    $ loki = True
                                    $ plthr = u"Локи"
                                "Дрищ":
                                    $ plthr = u"Дрищ"
                            stop ambience fadeout 2
                            $ alt_day_binder = 1
                            jump alt_day1_start
                "Ульяна":
                    menu:
                        "Локи":
                            $ loki = True
                            $ plthr = u"Локи"
                            $ us_pt += 5
                        "Дрищ":
                            $ plthr = u"Дрищ"
                            $ us_pt += 5
                            pause(1)
                    menu:
                        "День 6":
                            menu:
                                "Начало дня":
                                    menu:
                                        "7дл":
                                            $ routetag = "us7dl_bad"
                                        "7дл после пряток":
                                            $ routetag = "us7dl_bad"
                                            $ alt_day4_neu_us_pixies == 2
                                        "Огоньки":
                                            $ routetag = "us7dl_good"
                                            $ alt_day4_neu_us_pixies == 3
                                    stop ambience fadeout 2
                                    jump alt_day6_us_7dl_start
                                "Отдельные сцены":
                                    menu:
                                        "Утро":
                                            menu:
                                                "Зарядка":
                                                    stop ambience fadeout 2
                                                    call alt_day6_us_7dl_exercises
                                                "Завтрак":
                                                    stop ambience fadeout 2
                                                    call alt_day6_us_7dl_breakfast
                                                "7дл - помощь по лагерю":
                                                    stop ambience fadeout 2
                                                    call alt_day6_us_7dl_helping
                                                "7дл - помощь Мику":
                                                    stop ambience fadeout 2
                                                    call alt_day6_us_7dl_preps
                                                "7дл - помощь Славе":
                                                    stop ambience fadeout 2
                                                    call alt_day6_us_7dl_warehouse
                                                "7дл - поиски Лены":
                                                    stop ambience fadeout 2
                                                    call alt_day6_us_7dl_un_met
                                        "День":
                                            menu:
                                                "Обед":
                                                    stop ambience fadeout 2
                                                    call alt_day6_us_7dl_dinner
                                                "7дл - саундчек":
                                                    stop ambience fadeout 2
                                                    call alt_day6_us_7dl_soundcheck
                                                "7дл - Ульяна - пуговица":
                                                    stop ambience fadeout 2
                                                    call alt_day6_us_7dl_button
                                                "7дл - Ульяна - рандеву":
                                                    stop ambience fadeout 2
                                                    call alt_day6_us_7dl_rendezvous
                                                "Огоньки - карьер":
                                                    stop ambience fadeout 2
                                                    call alt_day6_us_px_carrier
                                                "Огоньки - обед":
                                                    stop ambience fadeout 2
                                                    call alt_day6_us_px_dinner
                                                "Огоньки - Лена":
                                                    stop ambience fadeout 2
                                                    call alt_day6_us_px_Lena
                                                "Огьньки - Славя":
                                                    stop ambience fadeout 2
                                                    call alt_day6_us_px_party_sl
                                                "Огоньки - дальние ворота":
                                                    stop ambience fadeout 2
                                                    call alt_day6_us_px_far_gate
                                        "Вечер":
                                            menu:
                                                "7дл - концерт":
                                                    stop ambience fadeout 2
                                                    call alt_day6_us_7dl_concert
                                                "7дл - ужин":
                                                    stop ambience fadeout 2
                                                    call alt_day6_us_7dl_supper
                                                "7дл - танцы":
                                                    stop ambience fadeout 2
                                                    call alt_day6_us_7dl_disco
                                                "Огоньки - чаепитие":
                                                    stop ambience fadeout 2
                                                    call alt_day6_us_7dl_tea
                                                "Огоньки - вечер у пристани.":
                                                    stop ambience fadeout 2
                                                    call alt_day6_us_px_afterwords
                                                "Отбой":
                                                    stop ambience fadeout 2
                                                    call alt_day6_us_7dl_sleeptime
                        "День 7, ЭПИЛОГ":
                            stop ambience fadeout 2
                            call alt_day6_us_px_vars
                            stop ambience fadeout 2
                            call alt_day6_us_7dl_vars
                            stop ambience fadeout 2
                            call alt_day7_us_px_vars
                            menu:
                                "С самого начала, Огоньки":
                                    menu:
                                        "Со Славей":
                                            $ alt_day6_us_px_sl_join = True
                                        "Без Слави":
                                            $ alt_day6_us_px_sl_join = False
                                    $ alt_day4_neu_us_pixies = 3
                                    stop ambience fadeout 2
                                    jump alt_day7_us_7dl_start
                                "С самого начала, 7дл":
                                    menu:
                                        "Подветка Мику":
                                            $ alt_day6_us_7dl_mi_friends = 3
                                        "Подветка Лены":
                                            $ alt_day6_us_7dl_un_friends = 3
                                        "Главная подветка":
                                            $ alt_day6_us_7dl_tr = True
                                    jump alt_day7_us_7dl_start
                                "Выбор сцен":
                                    $ alt_day6_us_7dl_tr = True
                                    menu:
                                        "Утро(гл. ветка)":
                                            stop ambience fadeout 2
                                            call alt_day7_us_7dl_begin
                                        "Завтрак (гл. ветка)":
                                            stop ambience fadeout 2
                                            call alt_day7_us_7dl_begin
                                        "Побег (огоньки)":
                                            menu:
                                                "Со Славей.":
                                                    $ alt_day6_us_px_sl_join = True
                                                    stop ambience fadeout 2
                                                    call alt_day7_us_px_escape
                                                "Без Слави":
                                                    stop ambience fadeout 2
                                                    call alt_day7_us_px_escape
                                                "Автобус":
                                                    stop ambience fadeout 2
                                                    call alt_day7_us_px_bus
                                                "Пустоши":
                                                    stop ambience fadeout 2
                                                    call alt_day7_us_px_bus
                                                "История сказки (эпилог)":
                                                    stop ambience fadeout 2
                                                    call alt_day7_us_px_fairytale
                                                "Возвращение в лагерь со Славей":
                                                    $ alt_day6_us_px_sl_join = True
                                                    stop ambience fadeout 2
                                                    call alt_day7_us_px_mourning
                                                "Возвращение в лагерь без Слави":
                                                    stop ambience fadeout 2
                                                    call alt_day7_us_px_mourning
                                        "Утреннее рандеву":
                                            menu:
                                                "С Ульянкой":
                                                    $ alt_day6_us_7dl_tr
                                                    stop ambience fadeout 2
                                                    call alt_day7_us_7dl_rendezvous2
                                                "С Мику":
                                                    $ alt_day6_us_7dl_mi_friends = 3
                                                    stop ambience fadeout 2
                                                    call alt_day7_us_7dl_rendezvous2
                                                "С Леной":
                                                    $ alt_day6_us_7dl_un_friends = 3
                                                    stop ambience fadeout 2
                                                    call alt_day7_us_7dl_rendezvous2
                                                "С вещами":
                                                    stop ambience fadeout 2
                                                    call alt_day7_us_7dl_packing
                                        "Огоньки, отъезд":
                                            stop ambience fadeout 2
                                            call alt_day7_us_px_dejavu
                                        "7дл, отъезд":
                                            menu:
                                                "С Ульяной":
                                                    $ alt_day6_us_7dl_tr
                                                    stop ambience fadeout 2
                                                    call alt_day7_us_7dl_leaving
                                                "С Мику":
                                                    $ alt_day6_us_7dl_mi_friends = 3
                                                    stop ambience fadeout 2
                                                    call alt_day7_us_7dl_leaving
                                                "С Леной":
                                                    $ alt_day6_us_7dl_un_friends = 3
                                                    stop ambience fadeout 2
                                                    call alt_day7_us_7dl_leaving
                                        "7дл, эпилоги":
                                            menu:
                                                "Пробуждение":
                                                    $ alt_day6_us_7dl_tr
                                                    stop ambience fadeout 2
                                                    call alt_day7_us_7dl_wakeup
                                                "Ульяна, хорошая концовка":
                                                    $ alt_day6_us_7dl_tr
                                                    stop ambience fadeout 2
                                                    call alt_day7_us_7dl_reunite
                                                "Концовка Мику":
                                                    $ alt_day6_us_7dl_mi_friends = 3
                                                    stop ambience fadeout 2
                                                    call alt_day7_us_7dl_mikuforever
                                                "Концовка Лены":
                                                    $ alt_day6_us_7dl_un_friends = 3
                                                    stop ambience fadeout 2
                                                    call alt_day7_us_7dl_lenaforever
                                                "Плохая концовка":
                                                    stop ambience fadeout 2
                                                    call alt_day7_us_7dl_bad
                                            
                "Мику":
                    $ lp_mi += 14
                    $ routetag = "mi7dl"
                    menu:
                        "DJ":
                            $ alt_day3_mi_dj = True
                            
                            stop ambience fadeout 2
                            jump alt_day4_mi_dj_start
                        "7дл":
                            menu:
                                "День 4. Едем в город вместе?":
                                    $ alt_day3_mi_donor = True
                                    $ alt_hpt += 2
                                    stop ambience fadeout 2
                                    jump alt_day4_mi_7dl_start
                                "Едем в город в одиночестве?":
                                    $ alt_spt += 2
                                    stop ambience fadeout 2
                                    jump alt_day4_mi_7dl_start
                                "День 5.":
                                    stop ambience fadeout 2
                                    jump alt_day5_mi_7dl_start
                                "День 6.":
                                    menu:
                                        "Ветка Принцессы":
                                            $ alt_spt += 10
                                        "Ветка Человека":
                                            $ alt_hpt += 10
                                        "Бонусная ветка":
                                            $ alt_day5_mi_7dl_voyeur = True
                                    stop ambience fadeout 2
                                    jump alt_day6_mi_7dl_start
                                "Прощание общее":
                                    menu:
                                        "Звезда":
                                            pass
                                        "Душа":
                                            $ alt_day5_mi_7dl_voyeur = True
                                    stop ambience fadeout 2
                                    jump alt_day6_mi_7dl_miku_sakishita
                                "Прощание: Принцесса":
                                    stop ambience fadeout 2
                                    jump alt_day6_mi_7dl_miku_farewell_star
                                "Прощание: Душа":
                                    stop ambience fadeout 2
                                    jump alt_day6_mi_7dl_miku_farewell_soul
                            
                        "Классик":
                            "Рут находится в разработке."
                            $ renpy.pause(1)
                            stop ambience fadeout 2
                            jump sdl_menu
                "Алиса":
                    $ routetag = "dv7dl"
                    $ lp_dv = 14
                    menu:
                        "DJ":
                            "Рут находится в разработке."
                            $ renpy.pause(1)
                            stop ambience fadeout 2
                            jump sdl_menu
                        "7дл":
                            $ alt_day3_event3 = 33
                            stop ambience fadeout 2
                            jump alt_day4_dv_7dl_start
                        "Классик":
                            "Рут находится в разработке."
                            $ renpy.pause(1)
                            stop ambience fadeout 2
                            jump sdl_menu
                "Славя":
                    $ lp_sl += 13
                    menu:
                        "7дл":
                            $ counter_sl_cl = 5
                            $ routetag = "sl7dl"
                            menu:
                                "Герк":
                                    $ herc = True
                                "Локи":
                                    $ loki = True
                                "Дрищ":
                                    pass
                            menu:
                                "Записаться на волейбол":
                                    $ list_clubs_7dl.append('volley')
                                "Не записываться.":
                                    pass
                            menu:
                                "Записаться в музыкальный клуб":
                                    $ list_clubs_7dl.append('music_club')
                                "Не записываться":
                                    pass
                                jump alt_day4_sl_7dl_start
                            $ renpy.pause(1)
                            stop ambience fadeout 2
                            jump sdl_menu
                        "Классик":
                            $ counter_sl_cl = 5
                            $ alt_day3_technoquest_st3 = 2
                            $ routetag = "sl"
                            stop ambience fadeout 2
                            menu:
                                "Проверка инт-эпилога":
                                    call alt_day7_sl_loop2
                                "Проверка концовок - воля":
                                    $ alt_day6_sl_int = 4
                                    call alt_day7_sl_will
                                "Проверка концовок - долг":
                                    call alt_day7_sl_duty
                            $ alt_day3_technoquest_st3 = 2
                            $ routetag = "sl"
                            stop ambience fadeout 2
                            jump alt_day4_sl_start
                "Лена":
                    $ lp_un += 14
                    $ routetag = "un7dl"
                    menu:
                        "Френдзона":
                            $ list_d2_date_7dl('un_fz')
                            $ alt_day3_dancing = 132
                            stop ambience fadeout 2
                            jump alt_day4_un_fz_start
                        "7дл":
                            menu:
                                "Карма"
                                "10":
                                    $ karma = 10
                                "30":
                                    $ karma = 30
                                "100":
                                    $ karma = 100
                            menu:
                                "Герк":
                                    $ herc = True
                                "Дрищ":
                                    pass
                                "Локи":
                                    $ loki = True
                            menu:
                                "Ключи есть":
                                    $ alt_day1_sl_keys_took = 1
                                "Ключей нет":
                                    pass
                            menu:
                                "Записан в газету":
                                    $ list_clubs_7dl.append('nwsppr')
                                "Не записан":
                                    pass 
                            menu:
                                "Транзит":
                                    $ alt_day4_neu_transit = 1
                                "Регуляр":
                                    $ alt_day4_neu_transit = 0
                                    $ alt_day3_un_med_help = 1
                            stop ambience fadeout 2
                            jump alt_day4_un_7dl_start

                        "Классик":
                            "Рут находится в разработке."
                            $ renpy.pause(1)
                            stop ambience fadeout 2
                            jump sdl_menu
                    
                "Ольга":
                    $ mt_pt += 8
                    stop ambience fadeout 2
                    jump alt_day6_mt_7dl_start
                "Одиночка":
                    menu:
                        "Утро с Алисой":
                            $ alt_day3_dv_evening = True
                        "Утро в медпункте":
                            $ alt_day3_technoquest_st3 = 2
                        "Утро в домике":
                            pass
                    stop ambience fadeout 2
                    jump alt_day4_neu_begin
        "Концовки":
            label alt_endings:
                with fade
                menu:
                    "Мику-DJ":
                        menu:
                            "{color=#ed6b6b}С новым счастьем! (плохая){/color}":
                                stop ambience fadeout 2
                                jump alt_day7_mi_dj_bad_end
                            "{color=#6beded}Моя Мику! (истинная){/color}":
                                stop ambience fadeout 2
                                jump alt_day7_mi_dj_true_end
                            "{color=#aced6b}Обязательно дождись! (хорошая){/color}":
                                stop ambience fadeout 2
                                jump alt_day7_mi_dj_jp_good_end
                            "{color=#ed6b6b}И не мечтай! (хорошая-рф){/color}":
                                menu:
                                    "С послесловием":
                                        $ alt_day_binder = 1
                                    "Без послесловия":
                                        with fade
                                stop ambience fadeout 2
                                jump alt_day7_mi_dj_rf_good_end
                    "Мику-7дл":
                        menu:
                            "Эпилог.":
                                menu:
                                    "Мику уехала":
                                        $ alt_day6_mi_7dl_left = True
                                        menu:
                                            "Звезда":
                                                $ alt_spt += 10
                                                $ lp_mi += 20
                                            "Сомневающийся":
                                                $ alt_spt += 7
                                            "Безвольный":
                                                $ alt_spt += 1
                                        stop ambience fadeout 2
                                        jump alt_day7_mi_7dl_start
                                        
                                    "Мику осталась":
                                        menu:
                                            "Человек":
                                                $ alt_hpt += 10
                                                $ lp_mi += 20
                                            "Сомневающийся":
                                                $ alt_hpt += 7
                                            "Безвольный":
                                                $ alt_hpt += 1
                                        stop ambience fadeout 2
                                        jump alt_day7_mi_7dl_start
                            "{color=#ff7bac}Искорка{/color}":
                                stop ambience fadeout 2
                                jump alt_day7_mi_7dl_sparkle
                            "{color=#dddddd}Горькая правда{/color}":
                                stop ambience fadeout 2
                                jump alt_day7_mi_7dl_postscriptum
                            "{color=#ee6a9b}Чёртов процессор{/color}":
                                stop ambience fadeout 2
                                jump alt_day7_mi_7dl_dam_CPU
                            "{color=#dd598a}Клуб-27{/color}":
                                stop ambience fadeout 2
                                jump alt_day7_mi_7dl_club27
                            "{color=#dd6666}Не похожа{/color}":
                                stop ambience fadeout 2
                                jump alt_day7_mi_7dl_unlike
                            "{color=#66dd66}Синтетическое счастье{/color}":
                                stop ambience fadeout 2
                                jump alt_day7_mi_7dl_sinthetic
                            "{color=#6666dd}Возвращайся{/color}":
                                stop ambience fadeout 2
                                jump alt_day7_mi_7dl_come_back
                            "{color=#ac7bff}Странные сны{/color}":
                                stop ambience fadeout 2
                                jump alt_day7_mi_7dl_dark_dreams
                            "{color=#9b6aee}Развесели снова":
                                stop ambience fadeout 2
                                jump alt_day7_mi_7dl_happy_again
                            "{color=#dd598a}Спасибо тебе…{/color}":
                                $ alt_day5_mi_7dl_voyeur = True
                                stop ambience fadeout 2
                                $ alt_day5_mi_7dl_voyeur = True
                                $ persistent.mi_7dl_dr_exc = True
                                jump alt_day6_mi_7dl_miku_farewell_finale
                            "{color=#8a59dd}Так честнее":
                                stop ambience fadeout 2
                                jump alt_day7_mi_7dl_liar
                    "Алиса":
                        menu:
                            "{color=#ff0000}Тульпа (эксклюзив){/color}":
                                stop ambience fadeout 2
                                call alt_day7_dv_7dl_loki
                                pause(1)
                                stop ambience fadeout 2
                                call alt_day7_dv_7dl_tulpa_end
                                pause(1)
                                return
                            "{color=#d16bed}Meet me there (транзитная){/color}":
                                stop ambience fadeout 2
                                jump alt_day7_dv_7dl_un_end
                            "{color=#aaaaac}Нет пути (плохая){/color}":
                                menu:
                                    "Пьяная-помятая…":
                                        $ alt_day7_dv_7dl_check = 5
                                    "Плохая концовка.":
                                        with fade
                                stop ambience fadeout 2
                                jump alt_day7_dv_7dl_bad_end
                            "{color=#fca635}Больше, чем жизнь (хорошая-рф){/color}":
                                menu:
                                    "С послесловием":
                                        $ alt_day_binder = 1
                                    "Без послесловия":
                                        with fade
                                stop ambience fadeout 2
                                jump alt_day7_dv_7dl_rf_epilogue
                            "{color=#ffb68f}Светлое настоящее (хорошая){/color}":
                                stop ambience fadeout 2
                                jump alt_day7_dv_7dl_ussr_epilogue
                            "{color=#aaaaaa}До самого конца (нейтральная){/color}":
                                stop ambience fadeout 2
                                jump alt_day7_dv_7dl_rej_ussr_end
                            "{color=#e37944}Я отвезу тебя домой. (нейтральная-рф){/color}":
                                stop ambience fadeout 2
                                jump alt_day7_dv_7dl_rej_rf_end
                    "Славя":
                        menu:
                            "{color=#f7f723}Всё же хорошо? (истинная){/color}":
                                stop ambience fadeout 2
                                jump alt_day7_sl_will
                            "{color=#f7f723}Зови меня «дорогой» (инт){/color}":
                                stop ambience fadeout 2
                                jump alt_day7_sl_duty
                            "{color=#d6bf3c}Твоя. Подделка (плохая){/color}":
                                stop ambience fadeout 2
                                jump alt_day7_sl_cl_bad
                            "{color=#57a4fa}На том же самом месте (нейтральная-рф){/color}":
                                stop ambience fadeout 2
                                jump alt_day7_sl_reject_same
                            "{color=#57d7fa}Пора домой (нейтральная){/color}":
                                stop ambience fadeout 2
                                jump alt_day7_sl_reject_late
                            "{color=#f2fa57}Что-то правильное (хорошая2-рф){/color}":
                                stop ambience fadeout 2
                                jump alt_day7_sl_rf2
                            "{color=#f2fa57}Сомнения (хорошая-рф){/color}":
                                stop ambience fadeout 2
                                jump alt_day7_sl_rf_good
                            "{color=#ecf711}Плюс-минус полчаса (хорошая){/color}":
                                stop ambience fadeout 2
                                jump alt_day7_sl_good
                            "{color=#f7f723}Цена одиночества (плохая){/color}":
                                stop ambience fadeout 2
                                jump alt_day7_sl_lone
                            "{color=#9894e0}Всё будет хорошо (эксклюзив){/color}":
                                stop ambience fadeout 2
                                jump alt_day6_sl_cl_become_a_hero
                            "{color=#aaaaaa}Postscriptum {/color}":
                                stop ambience fadeout 2
                                jump alt_day8_sl_postscriptum
                    "Лена":
                        menu:
                            "Хорошие":
                                menu:
                                    "Эпилог.":
                                        stop ambience fadeout 2
                                        jump alt_day7_un_7dl_epilogue
                                    "{color=#9894e0}Вся жизнь впереди (хорошая){/color}":
                                        stop ambience fadeout 2
                                        jump alt_day7_un_7dl_ussr
                                    "{color=#a6a1ff}Вся жизнь впереди-2 (хорошая-рф){/color}":
                                        menu:
                                            "С послесловием":
                                                $ alt_day_binder = 1
                                            "Без послесловия":
                                                with fade
                                        stop ambience fadeout 2
                                        jump alt_day7_un_7dl_rf
                            "{color=#ff3098}Вдоль, а не поперёк (плохая){/color}":
                                stop ambience fadeout 2
                                jump alt_day7_un_7dl_epilogue_bad
                            "Дождь.":
                                stop ambience fadeout 2
                                jump alt_day7_un_7dl_true
                    "Ольга":
                        menu:
                            "Сброс флагов концовок":
                                $ persistent.mt_7dl_good = False
                                $ persistent.mt_7dl_bad = False
                                $ persistent.mt_7dl_ever_after = False
                                $ persistent.mt_7dl_true = False
                            "Эпилоги":
                                menu:
                                    "{color=#3350fb}Выбор: прошлое{/color}":
                                        menu:
                                            "Истинная концовка":
                                                $ mt_pt = 15
                                                $ list_d2_date_7dl('mt')
                                                $ alt_day5_neu_mt_diary = True 
                                                $ alt_day4_neu_mt_diary = True
                                            "Нейтральная концовка":
                                                pass
                                        stop ambience fadeout 2
                                        jump alt_day7_mt_7dl_loopthru
                                    "{color=#33fb50}Выбор: будущее{/color}":
                                        menu:
                                            "Хорошая концовка":
                                                $ mt_pt = 13
                                                $ list_d2_date_7dl('mt')
                                                $ alt_day3_dancing = 5
                                                $ alt_day4_neu_mt_fire = True
                                                $ alt_day_binder = 1
                                            "Плохая концовка":
                                                pass
                                        stop ambience fadeout 2
                                        jump alt_day7_mt_7dl_loopback
                            "{color=#3ff02b}Чудо по имени Ольга (хорошая){/color}":
                                menu:
                                    "С послесловием":
                                        $ alt_day_binder = 1
                                    "Без послесловия":
                                        with fade
                                stop ambience fadeout 2
                                jump alt_day7_mt_7dl_good
                            "{color=#ffffff}Лучше не просыпаться (плохая){/color}":
                                    stop ambience fadeout 2
                                    jump alt_day7_mt_7dl_bad
                            "{color=#f07a2b}Долго и счастливо? (нейтральная){/color}":
                                    stop ambience fadeout 2
                                    jump alt_day7_mt_7dl_ever_after
                            "{color=#bf2bf0}По праву памяти (истинная){/color}":
                                    stop ambience fadeout 2
                                    jump alt_day7_mt_7dl_true
                    "Ульяна":
                        menu:
                            "{color=#ff0000}Ульяна, хорошая концовка.{/color}":
                                $ alt_day6_us_7dl_tr
                                stop ambience fadeout 2
                                call alt_day7_us_7dl_reunite
                            "{color=#aced6b}Ульяна, Концовка Мику.{/color}":
                                $ alt_day6_us_7dl_mi_friends = 3
                                stop ambience fadeout 2
                                call alt_day7_us_7dl_mikuforever
                            "{color=#9894e0}Ульяна, Концовка Лены.{/color}":
                                $ alt_day6_us_7dl_un_friends = 3
                                stop ambience fadeout 2
                                call alt_day7_us_7dl_lenaforever
                            "{color=#ed6b6b}Ульяна, Плохая концовка.{/color}":
                                stop ambience fadeout 2
                                call alt_day7_us_7dl_bad
                            "{color=#ffff00}Огоньки, Истинная концовка.{/color}":
                                stop ambience fadeout 2
                                call alt_day7_us_px_fairytale
                            "{color=#ffff11}Огоньки, Хорошая концовка.{/color}":
                                stop ambience fadeout 2
                                call alt_day7_us_px_dejavu
                            "{color=#6beded}Ульяна, Истинная концовка.{/color}":
                                stop ambience fadeout 2
                                call alt_day7_us_7dl_ever_after
                        $ renpy.pause(1)
                        stop ambience fadeout 2
                        jump alt_endings
                    "Одиночка":
                        "Рут находится в разработке."
                        $ renpy.pause(1)
                        stop ambience fadeout 2
                        jump alt_endings