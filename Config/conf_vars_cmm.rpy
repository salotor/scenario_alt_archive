﻿#Мод пилится на базе нетленки от АБЦБ - его сюжет и подача мне куда симпатичнее оригинальной стори.
#За что ему огромный респектище и, по возможности, оставлены отсылки на оригинальные правки.
init -1:
    $ alt_release_no = "0.32.a"
    $ alt_compatible_release_no = ["0.00.x", "0.32.a"] 

init 2:
    $ mods["scenario__alt_sevendl"] = u"7 Дней Лета"
    $ mod_tags["scenario__alt_sevendl"] = ["length:days","gameplay:vn","protagonist:male"]
    $ timeskip_come = "Ты пойдёшь со мной?"
    $ timeskip_dev = "Рут находится в разработке…\nВ активной разработке: Ульяна-7дл. Побег."
    $ timeskip33 = "ВЕЛИКОЕ ОГРАБЛЕНИЕ!"
    $ timeskip3 = "Я скучаю…"
    $ timeskip4 = "Я хочу к тебе…"
    $ timeskip5 = "ПОШЛА ВОООООН!"
    $ timeskip6 = "ПРЕДУПРЕЖДЕНИЕ\nВсе совпадения персонажей и характеров\nс реально существующими людьми\nсчитать злой волей автора"
    $ timeskip7 = "Твоя Мику"
    $ timeskip8 = "ПРОСНИСЬ"
    $ timeskip9 = "Я буду ждать."
    $ timeskip10 = "Спасибо…"
    $ timeskip11 = "Прощай."
    $ timeskip12 = "Ты потерялся, малыш?"
    $ alt_credits_text = "Команда Soviet Games (IIchan Eroge Team) благодарит вас за время, уделённое игре!\n\nБлагодарности:\n\nPyTom'у за движок Ren'Py.\n\nСайту freesounds.org за бесплатные звуки.\n\nСайтам iichan.hk и 2ch.hk.\n\nВсем, кто помогал работать над игрой.\n\nВсем, кто нас поддерживал все эти годы, ждал и верил!\n\n7ДЛ\n\nBeta-test:\n\nМакс Ветров, Drago23, Arlien, Peregarrett, Demiurge-kun, Дельта, KirillZ89, Ленофаг Простой, Ленивый Бегун, Занудный, Serge Domingo, Ravsii, Dantiras, salotor.\n\nОСОБЫЕ БЛАГОДАРНОСТИ:\n\nMannych - за колоритного физрука!\n\nEldhenn - за адаптацию игры в Steam.\n\nPeregarrett, Chess - за кошко-рут.\n\nЛенофаг Простой, Ravsii - за идеи и помощь их реализации.\n\nNuttyprof, openplace - за новую карту лагеря.\n\nМакс Смолев(sorasora) - за новые cg-сценки и стиль БЛ.\n\nАлексей - за фоны и модели.\n\nRINA-SAN, ☆ FairyApple ☆ - за вдохновение и неконтролируемые приступы позитива!\n\nВсем, кого не упомянул, но не забыл - за то, что помогали и поддерживали!\n\n\n\nКОНЕЦ.\n"
    
    $ colors['ba'] = {'night': (88, 18, 67, 255), 'sunset': (132, 27, 100, 255), 'day': (252, 15, 192, 255), 'prolog': (150, 50, 100, 255)}
    $ store.names_list.append('ba')
    
    $ colors['sak'] = {'night': (44, 12, 67, 255), 'sunset': (66, 18, 100, 255), 'day': (176, 10, 192, 255), 'prolog': (75, 34, 100, 255)}
    $ store.names_list.append('sak')
    
    $ colors['ai'] = {'night': (44, 12, 67, 255), 'sunset': (66, 18, 100, 255), 'day': (176, 10, 192, 255), 'prolog': (34, 150, 100, 255)}
    $ store.names_list.append('ai')
    
    #Камео мисс Селезнёвой
    $ colors['ase'] = {'night': (97, 10, 10, 255), 'sunset': (137, 14, 14, 255), 'day': (236, 66, 66, 255), 'prolog': (137, 14, 14, 255)}
    $ store.names_list.append('ase')
    
    $ colors['we'] = {'night': (67, 23, 111, 255), 'sunset': (132, 27, 100, 255), 'day': (252, 15, 192, 255), 'prolog': (150, 50, 100, 255)}
    $ store.names_list.append('we')
    
    $ colors['ml'] = {'night': (20, 69, 68, 255), 'sunset': (32, 106, 104, 255), 'day': (74, 200, 147, 255), 'prolog': (50, 20, 80, 255)}
    $ store.names_list.append('ml')
    
    $ colors['ml2'] = {'night': (20, 46, 68, 255), 'sunset': (32, 73, 104, 255), 'day': (74, 170, 147, 255), 'prolog': (32, 75, 106, 255)}
    $ store.names_list.append('ml2')
    
    $ colors['voice1'] = {'night': (159, 8, 73, 255), 'sunset': (196, 7, 92, 255), 'day': (255, 136, 192, 255), 'prolog': (196, 7, 124, 255)}
    $ store.names_list.append('voice1')
    
    $ colors['bb'] = {'night': (159, 8, 73, 255), 'sunset': (196, 7, 92, 255), 'day': (255, 136, 192, 255), 'prolog': (196, 7, 124, 255)}
    $ store.names_list.append('bb')
    
    $ colors['icq'] = {'night': (6, 62, 14, 255), 'sunset': (10, 91, 20, 255), 'day': (10, 204, 10, 255), 'prolog': (10, 91, 30, 255)}
    $ store.names_list.append('icq')
    #Резерв
    #$ colors['ann'] = {'night': (15, 159, 14, 255), 'sunset': (10, 217, 16, 255), 'day': (170, 254, 160, 255), 'prolog': (10, 215, 30, 255)}
    #$ store.names_list.append('ann')
    
    $ lp_mi = 0
    $ lp_sl = 0
    $ lp_un = 0
    $ lp_us = 0
    $ lp_dv = 0
    $ karma = 0
    $ plthr = u"none"
    $ alt_sp = 0
    $ alt_spt = 0
    $ alt_hpt = 0
    $ mt_pt = 0
    $ d3_pt = 0
    $ us_pt = 0
label scenario__alt_sevendl:
# инициализация карт. Должна выполняться ТОЛЬКО один раз - иначе не работают сохранения
# ------------------------------------------------
    $ init_map_zones_alt1()
    $ init_map_zones_alt2()

# ------------------------------------------------
# только если игру начали заново - принимаем номер релиза сохранения по номеру релиза мода
    $ alt_save_release_no = alt_release_no
# ------------------------------------------------

    call alt_day0_vars
jump choose_waifu_7dl

label alt_day0_vars: #Переменные нулевого дня
    $ lp_mi = 0
    $ lp_sl = 0
    $ lp_un = 0
    $ lp_us = 0
    $ lp_dv = 0
    $ karma = 0
    $ plthr = u"none"
    $ alt_sp = 0
    $ alt_spt = 0
    $ alt_hpt = 0
    $ mt_pt = 0
    $ d3_pt = 0
    $ us_pt = 0
    $ alt_day_binder = 0
    $ semen_str = 10
    $ alt_dlc_active = False
    $ herc = False
    $ loki = False
    $ d3 = False
    $ routetag = "prologue"
    $ role_bg = "intro_ground"
    if persistent.dv_7dl_good_ussr and persistent.un_7dl_good_ussr and persistent.mi_good_human and persistent.mt_7dl_good and persistent.sl_7dl_good_ussr and persistent.us_7dl_good:
        $ alt_day_binder = 1
    return
    
label alt_day1_vars: #Переменные первого дня
    $ alt_route_flag = 1
    $ alt_day1_alt_chase = False
    $ alt_day1_alt_us_robbed = False
    $ alt_day1_alt_robbery = False
    $ alt_day1_alt_sl_conv = False
    $ alt_day1_dv_feed = False
    $ alt_day1_el_followed = False
    $ alt_day1_sam_paniqued = False
    $ alt_day1_sl_met = False
    $ alt_day1_sl_conv = False
    $ alt_day1_sl_keys_took = 0
    $ alt_day1_un_dated = False
    $ alt_day1_un_ignored = False
    $ alt_day1_un_nicebook = False
    $ alt_day1_un_stopped = False
    $ alt_day1_us_shotted = False
    $ alt_day1_chase = False
    $ alt_day1_chase_uvao = False
    $ alt_day1_genda_investigation = False
    $ alt_day1_cofront_sl_dv = 0
    $ alt_day1_headshot = False
    return
    
label alt_day2_vars: #Переменные второго дня
    $ alt_route_flag = 2
    $ alt_day2_bf_dv_us = False
    $ alt_day2_bf_un = False
    $ alt_day2_club_join_badmin = False
    $ alt_day2_club_join_cyb = False
    $ alt_day2_club_join_footbal = False
    $ alt_day2_club_join_nwsppr = False
    $ alt_day2_club_join_musc = False
    $ alt_day2_club_join_volley = False
    $ alt_day2_dv_bet_approve = False
    $ alt_day2_dv_bet_won = 0
    $ alt_day2_dv_bumped = False
    $ alt_day2_dv_chased = False
    $ alt_day2_dv_harass = False
    $ alt_day2_dv_tears = False
    $ alt_day2_dv_us_house_visited = False
    $ alt_day2_loki_minijack = False
    $ alt_day2_mi_kumuhimo = 0
    $ alt_day2_mi_met = False
    $ alt_day2_mi_met2 = False
    $ alt_day2_mi_rejected = False
    $ alt_day2_mi_hyst = False
    $ alt_day2_mt_help = False
    $ alt_day2_mi_snap = False
    $ alt_day2_rendezvous = 0
    $ alt_day2_rendezvous_dinner = 0
    $ alt_day2_sl_bf = False
    $ alt_day2_sl_guilty = 0 #0 не был свидетелем, 1 был, 2 вступился
    $ alt_day2_date = 0 #un 1, sl 2, dv 3, mi 4, us 5, mt 6
    $ alt_day2_un_secret_spot = 0
    $ alt_day2_us_dubstep = False
    $ alt_day2_us_escape = False
    $ alt_day2_muz_done = False #Если только ходил в музклуб, но не записывался
    $ alt_day2_lib_done = False
    $ alt_day2_med_done = False
    $ alt_day2_club_done = False
    $ alt_day2_phys_done = False
    $ alt_day2_beach_done = False
    $ alt_day2_necessary_done = 0
    $ alt_day2_walk = 0
    $ alt_day2_fail = 0
    $ alt_day2_sup = 0
    $ alt_day2_cardgame_block_rollback = False
    $ alt_day2_olga_help = False
    #Переменные для турнира
    $ alt_day2_round1 = 0 #0 не участвовал, 1 проиграл, если победил то -V-
    $ alt_day2_round2 = 0 #0 не участвовал, 1 проиграл, если победил, то -V-
    $ alt_day2_round3 = 0 #0 не участвовал 1 для проигрыша 2 для победы
    $ alt_day2_desk1 = 0
    $ alt_day2_hf1 = 0
    $ alt_day2_desk2 = 0
    $ alt_day2_hf2 = 0
    $ alt_day2_f1 = 0
    $ alt_day2_desk3 = 0
    $ alt_day2_hf3 = 0
    $ alt_day2_desk4 = 0
    $ alt_day2_hf4 = 0
    $ alt_day2_f2 = 0
    $ alt_day2_revanche = False
    $ alt_day3_us_shenan = False
    $ alt_day3_duty = False
    return
    
label alt_day3_vars: #Переменные третьего дня
    $ alt_route_flag = 3
    $ alt_day3_dancing = 0
    $ alt_day3_event1 = 0
    $ alt_day3_event2 = 0
    $ alt_day3_event3 = 0
    $ alt_day3_event4 = 0
    $ alt_day3_dv_date = False
    $ alt_day3_dv_dj = False 
    $ alt_day3_dv_evening = False
    $ alt_day3_dv_event = False
    $ alt_day3_dv2_event = False
    $ alt_day3_dv_guitar_lesson = False
    $ alt_day3_dv_invite = False
    $ alt_day3_dv_rejected = False
    $ alt_day3_ladder_phys = 0
    $ alt_day3_ladder_ph_loser = False
    $ alt_day3_ladder_mt = 0
    $ alt_day3_ladder_mt_loser = False
    $ alt_day3_ladder_us = 0
    $ alt_day3_mi_date = False
    $ alt_day3_mi_dj = False 
    $ alt_day3_mi_event = False
    $ alt_day3_mi_rejected = False
    $ alt_day3_mi_invite = False
    $ alt_day3_mi_invite2 = False
    $ alt_day3_mi_donor = False
    $ alt_day3_sl_bath_voy = False
    $ alt_day3_sl_day_event2 = False
    $ alt_day3_sl_day_event = False
    $ alt_day3_sl_event = False
    $ alt_day3_sl_invite = False
    $ alt_day3_technoquest_st1 = False
    $ alt_day3_technoquest_st2 = False
    $ alt_day3_technoquest_st3 = 0
    $ alt_timer = 10
    $ alt_day3_timer_range = 0
    $ alt_day3_timer_jump = 0
    $ alt_day3_lp_route = 0
    $ alt_day3_un_cheated = False
    $ alt_day3_un_date = False 
    $ alt_day3_un_event = False
    $ alt_day3_un_med_help = False
    $ alt_day3_un_strip_pool_sp = 5
    $ alt_day3_un_strip_pool_un = 5
    $ alt_day3_un_invite = 0
    $ alt_day3_us_bugs = 0
    $ alt_day3_us_invite = False
    $ alt_day3_uvao_spotted = False
    return