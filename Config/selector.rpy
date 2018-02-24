<<<<<<< HEAD
﻿# Здесь была прыгалка.
=======
﻿init :
    $ mods["scenario__sdl_selector"] = u"7ДЛ концовки"
    $ mod_tags["scenario__sdl_selector"] = ["length:days","gameplay:vn","protagonist:male"]
    
    image scenery:
        "images/1080/anim/prolog_2.jpg" with Dissolve(.5) 
        pause 2.6
        "images/1080/anim/prolog_1.jpg" with Dissolve(.5) 
        pause 0.6
        repeat
        
    image scenery2:
        "images/1080/anim/prolog_2.jpg" with Dissolve(.4) 
        pause 2.0
        "images/1080/anim/prolog_1.jpg" with Dissolve(.4) 
        pause 0.4
        repeat    
        
    image scenery3:
        "images/1080/anim/prolog_2.jpg" with Dissolve(.25) 
        pause 1.4
        "images/1080/anim/prolog_1.jpg" with Dissolve(.25) 
        pause 0.25
        repeat
        
label scenario__sdl_selector:

    $ init_map_zones_alt1()
    $ init_map_zones_alt2()
    $ alt_save_release_no = "00.x.0"
    $ bak_release_no = alt_release_no
    $ alt_release_no = "00.x.0"
    $ make_names_unknown()
    $ th_prefix = "«"
    $ th_suffix = "»"
    $ alt_day0_prologue = True
    $ plthr = u"Тест"
    $ day_time()
    $ persistent.sprite_time = "day"
    $ make_names_unknown_7dl()

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
    
    play ambience ambience_safe fadein 5
    
label sdl_menu:
    scene scenery with dissolve
    menu:
        "Руты.":
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
                            jump alt_day1_alt_M
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
                    $ alt_day3_event2 = 22
                    $ alt_day3_sl_day_event2 = True
                    $ lp_sl += 14
                    menu:
                        "7дл":
                            $ routetag = "sl7dl"
                            "Рут находится в разработке."
                            $ renpy.pause(1)
                            stop ambience fadeout 2
                            jump sdl_menu
                        "Классик":
                            $ alt_day3_technoquest_st3 = 2
                            $ routetag = "sl"
                            stop ambience fadeout 2
                            jump alt_day4_sl_start
                "Лена":
                    $ lp_un += 14
                    $ routetag = "un7dl"
                    menu:
                        "Френдзона":
                            $ alt_day2_date = 132
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
                                "Ключи"
                                "Есть":
                                    $ alt_day1_sl_keys_took = 1
                                "Нет":
                                    pass
                            menu:
                                "Газета"
                                "Записан":
                                    $ alt_day2_club_join_nwsppr = True
                                "Нет":
                                    pass 
                            menu:
                                "Транзит?"
                                "Да":
                                    $ alt_day4_neu_transit = 1
                                "Нет":
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
                "Ульяна":
                    "Рут находится в разработке."
                    $ renpy.pause(1)
                    stop ambience fadeout 2
                    jump sdl_menu
                "Одиночка":
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
                                jump alt_day6_mi_7dl_miku_farewell_finale
                            "{color=#8a59dd}Так честнее":
                                stop ambience fadeout 2
                                jump alt_day7_mi_7dl_liar
                    "Алиса":
                        menu:
                            "{color=#ff0000}Тульпа (эксклюзив){/color}":
                                stop ambience fadeout 2
                                jump alt_day7_dv_7dl_loki
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
                                                $ alt_day2_date = 6
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
                                                $ alt_day2_date = 6
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
                        "Рут находится в разработке."
                        $ renpy.pause(1)
                        stop ambience fadeout 2
                        jump alt_endings
                    "Одиночка":
                        "Рут находится в разработке."
                        $ renpy.pause(1)
                        stop ambience fadeout 2
                        jump alt_endings
>>>>>>> dev
