#Мод пилится на базе нетленки от АБЦБ - его сюжет и подача мне куда симпатичнее оригинальной стори.
#За что ему огромный респектище и, по возможности, оставлены отсылки на оригинальные правки.
init -1:
    $ alt_release_no = "0.36.a"
    $ alt_compatible_release_no = ["0.34.a", "0.34.b", "0.35.a", "0.36.a"]
    $ alt_hotfix_no = "hf0"
    $ plthr = u"none"

init 2:
    $ mods["scenario__alt_sevendl"] = u"7 Дней Лета"
    $ mod_tags["scenario__alt_sevendl"] = ["length:days","gameplay:vn","protagonist:male"]
    $ timeskip_come = "Ты пойдёшь со мной?"
    $ timeskip_dev = "Рут находится в разработке…\nВ активной разработке: Славя-7дл. День 6."
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
    $ timeskip13 = "ПРИДИ В СЕБЯ!"
    $ alt_credits_text ="{image=acm_logo}\n\nАвтор сценария, режиссёр и постановщик:\n\n{color=#99ff00}{b}7дл-кун aka Inakrin{/b}{/color}\n\nГрафика:\n\n\nGoodbyeNona - фоны и спрайты\n\nMannych - спрайт физрука\n\nМакс Смолев(sorasora) - cg-сценки\n\nАлексей - фоны и модели\n\nАлексей «kef34» Никифоров - а я помогал!\◐__◑/ ໒( • ͜ʖ • ) \n\n☆ FairyApple ☆ - cg-сценки\n\n\n\nМУЗЫКА\n\nApril Rain\n\nTym Nyman\n\nDeadPunk\n\nППВК\n\n\nКОД И АДАПТАЦИЯ\n\nNuttyprof, openplace - новая карта лагеря и новый карточный турнир.\n\nSalotor - галерея, порт сценария в {u}Steam{/u}\n\nEldhenn - порт сценария в {u}Steam{/u}\n\nЛенофаг Простой, Ravsii - стартовые меню\n\nАльфа-, бета- и гамма-тестеры:\n\nМакс Ветров, Drago23, Arlien, Peregarrett, Demiurge-kun, Дельта, KirillZ89, Ленофаг Простой, Ленивый Бегун, Занудный, Serge Domingo, Ravsii, Dantiras, salotor, Gr0m, Sitzileon, shers.\n\nТоварищи, помогавшие финансово:\nDarkness Inc\nAlex Traven\n\nСпасибо всем, кого не упомянул, но не забыл - за то, что помогали и поддерживали!\n\n\n\nКОНЕЦ."

    #Day - базис
    #Sunset - 94%, 82%, 100%
    #Night - 58%, 67%, 67%
    #Prologue - 84%, 72%, 100% 

    $ colors['ai'] = {'night': (41, 164, 1, 255), 'sunset': (67, 201, 2, 255), 'day': (72, 246, 2, 255), 'prolog': (60, 177, 2, 255)}
    $ store.names_list.append('ai')#Собеседник, ИИ

    $ colors['al'] = {'night': (122, 121, 102, 255), 'sunset': (198, 148, 153, 255), 'day': (211, 181, 153, 255), 'prolog': (177, 130, 153, 255)}
    $ store.names_list.append('al')#Алька

    $ colors['am'] = {'night': (94, 143, 100, 255), 'sunset': (152, 175, 149, 255), 'day': (162, 214, 149, 255), 'prolog': (136, 154, 149, 255)}
    $ store.names_list.append('am') #Альтернативный протагонист

    $ colors['ase'] = {'night': (137, 44, 44, 255), 'sunset': (222, 54, 56, 255), 'day': (236, 66, 66, 255), 'prolog': (198, 48, 66, 255)}
    $ store.names_list.append('ase')#Камео мисс Селезнёвой

    $ colors['ba'] = {'night': (137, 153, 135, 255), 'sunset': (223, 188, 201, 255), 'day': (237, 229, 201, 255), 'prolog': (199, 165, 201, 255)}
    $ store.names_list.append('ba') #Саныч

    $ colors['bb'] = {'night': (133, 116, 90, 255), 'sunset': (215, 142, 135, 255), 'day': (229, 173, 135, 255), 'prolog': (192, 125, 135, 255)}
    $ store.names_list.append('bb')#Биг босс (начальник)

    $ colors['dn'] = {'night': (119, 68, 45, 255), 'sunset': (193, 84, 67, 255), 'day': (205, 102, 67, 255), 'prolog': (172, 73, 67, 255)}
    $ store.names_list.append('dn')#Данечка

    $ colors['ka'] = {'night': (137, 82, 85, 255), 'sunset': (222, 101, 127, 255), 'day': (236, 123, 127, 255), 'prolog': (198, 89, 127, 255)}
    $ store.names_list.append('ka') #Катюшка

    $ colors['ln'] = {'night': (137, 82, 85, 255), 'sunset': (222, 101, 127, 255), 'day': (236, 123, 127, 255), 'prolog': (198, 89, 127, 255)}
    $ store.names_list.append('ln') #Понятно кто

    $ colors['ml'] = {'night': (43, 134, 98, 255), 'sunset': (70, 164, 147, 255), 'day': (74, 200, 147, 255), 'prolog': (62, 144, 147, 255)}
    $ store.names_list.append('ml')#Малец1
    
    $ colors['ml2'] = {'night': (43, 53, 134, 255), 'sunset': (70, 65, 200, 255), 'day': (74, 79, 200, 255), 'prolog': (62, 57, 200, 255)}
    $ store.names_list.append('ml2')#Малец2
    
    $ colors['ml3'] = {'night': (62, 114, 98, 255), 'sunset': (101, 139, 147, 255), 'day': (107, 170, 147, 255), 'prolog': (90, 122, 147, 255)}
    $ store.names_list.append('ml3')#Малец3
    
    $ colors['sak'] = {'night': (89, 115, 146, 255), 'sunset': (144, 140, 218, 255), 'day': (153, 171, 218, 255), 'prolog': (129, 123, 218, 255)}
    $ store.names_list.append('sak')#Сакишита

    $ colors['tn'] = {'night': (125, 111, 62, 255), 'sunset': (203, 136, 93, 255), 'day': (216, 166, 93, 255), 'prolog': (181, 120, 93, 255)}
    $ store.names_list.append('tn')#Тоник
    
    $ colors['voice1'] = {'night': (159, 8, 73, 255), 'sunset': (196, 7, 92, 255), 'day': (255, 136, 192, 255), 'prolog': (196, 7, 124, 255)}
    $ store.names_list.append('voice1')

    $ colors['we'] = {'night': (67, 23, 111, 255), 'sunset': (132, 27, 100, 255), 'day': (252, 15, 192, 255), 'prolog': (150, 50, 100, 255)}
    $ store.names_list.append('we')#Толпа
    
    if not renpy.version(tuple=False) == "Ren'Py 6.16.3.502":
        $ colors['voices'] = {'night': (192, 192, 192, 255), 'sunset': (192, 192, 192, 255), 'day': (192, 192, 192, 255), 'prolog': (192, 192, 192, 255)}
        $ store.names_list.append('voices')
        
        $ colors['kids'] = {'night': (235, 120, 131, 255), 'sunset': (235, 120, 131, 255), 'day': (235, 120, 131, 255), 'prolog': (235, 120, 131, 255)}
        $ store.names_list.append('kids')
        
        $ colors['dy'] = {'night': (192, 192, 192, 255), 'sunset': (192, 192, 192, 255), 'day': (56, 90, 107, 255), 'prolog': (192, 192, 192, 255)}
        $ store.names_list.append('dy')
        
        $ names['ai'] = u'Собеседник'
        $ names['al'] = u'Сердитый мальчик'
        $ names['am'] = u'Я'
        $ names['ase'] = u'Девочка'
        $ names['ba'] = u'Физрук'
        $ names['bb'] = u'Начальник лагеря'
        $ names['dn'] = u'Кудрявый'
        $ names['dy'] = u'Динамики'
        $ names['ka'] = u'Вожатая 2-го отряда'
        $ names['kids'] = u'Дети'
        $ names['ln'] = u'Странная девочка'
        $ names['ml'] = u'Мальчик'
        $ names['ml2'] = u'Мальчик'
        $ names['ml3'] = u'Мальчик'
        $ names['sak'] = u'Пожилой японец'
        $ names['tn'] = u'Странный мальчик'
        $ names['voice1'] = u'Продавщица'
        $ names['voices'] = u'Голоса'
        $ names['we'] = u'Хором'
        
label scenario__alt_sevendl:
# только если игру начали заново - принимаем номер релиза сохранения по номеру релиза мода
    $ alt_save_release_no = alt_release_no
# инициализация карт. Должна выполняться ТОЛЬКО один раз - иначе не работают сохранения
    $ init_map_zones_alt1()
    $ init_map_zones_alt2()
# пишем версию 7дл в трейсбеках
    $ config.version = config.version+" + 7DL v.%s.%s" % (alt_release_no, alt_hotfix_no)
# ------------------------------------------------
    jump start_menu_7dl

init 4: # вызываем все переменные в init (необходимо для работы повторов)
    call alt_day0_vars
    call alt_day1_vars
    call alt_day2_vars
    call alt_day3_vars
    call alt_day4_un_fz_vars
    call alt_day4_mi_cl_vars
    call alt_day5_sl_wh_vars
    call alt_day4_un_7dl_vars
    call alt_day5_un_7dl_vars
    call alt_day6_un_7dl_vars
    call alt_day4_mi_dj_vars
    call alt_day5_mi_dj_vars
    call alt_day6_mi_dj_vars
    call alt_day4_dv_7dl_vars
    call alt_day6_dv_7dl_vars
    call alt_day4_sl_cl_vars
    call alt_day5_sl_cl_vars
    call alt_day6_sl_cl_vars
    call alt_day7_sl_cl_vars
    call alt_day5_mt_7dl_vars
    call alt_day6_mt_7dl_vars
    call alt_day4_mi_7dl_vars
    call alt_day5_mi_7dl_vars
    call alt_day6_mi_7dl_vars
    call alt_day4_neu_us_vars
    call alt_day5_neu_us_vars
    call alt_day5_us_7dl_vars
    call alt_day6_us_7dl_vars
    call alt_day6_us_px_vars
    call alt_day7_us_px_vars
    call alt_day4_sl_7dl_vars
    call alt_day5_sl_7dl_vars
    call alt_day6_sl_7dl_vars
    call alt_day7_sl_7dl_vars

label alt_day0_vars: #Переменные нулевого дня
    $ make_names_unknown_7dl()
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
    $ th_prefix = "«"
    $ th_suffix = "»"
    $ alt_day_catapult = 0
    $ alt_replay_on = False
    $ alt_dlc_active = False
    $ herc = False
    $ loki = False
    $ d3 = False
    $ routetag = "prologue"
    $ role_bg = "intro_ground"
    if persistent.dv_7dl_good_ussr and persistent.un_7dl_good_ussr and persistent.mi_7dl_good_human and persistent.mt_7dl_good and persistent.sl_7dl_good_ussr and persistent.us_7dl_good: # условия не соответствуют появлению кусочков паззла
        $ alt_day_binder = 1
    else:
        $ alt_day_binder = 0
    return
    
label alt_day1_vars: #Переменные первого дня
    $ counter_sl_cl = 0 #Счётчик рута (Славя-классик in progress)
    $ counter_sl_7dl = 0 #Счётчик рута (Славя-7дл)
    #TODO - same shit для прочих девочек
    $ list_slavya_7dl = []
    $ list_slavya_7dl = []
    $ alt_route_flag = 1
    $ alt_day1_loop = False
    $ alt_day1_alt_chase = False
    $ alt_day1_alt_us_robbed = False
    $ alt_day1_alt_robbery = False
    $ alt_day1_dv_feed = False
    $ alt_day1_el_followed = False
    $ alt_day1_sam_paniqued = False
    $ alt_day1_sl_met = False
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
    $ list_clubs_7dl = []
    $ list_voyage_7dl = []
    $ list_d2_date_7dl = []
    $ list_d2_convoy_7dl = []
    $ alt_day2_bf_dv_us = False
    $ alt_day2_bf_un = False
    $ alt_day2_dv_bet_approve = False
    $ alt_day2_dv_bet_won = 0
    $ alt_day2_dv_chased = False
    $ alt_day2_dv_harass = False
    $ alt_day2_dv_tears = False
    $ alt_day2_dv_us_house_visited = False
    $ alt_day2_loki_minijack = False
    $ alt_day2_mi_kumuhimo = 0
    $ alt_day2_mi_rejected = False
    $ alt_day2_mi_hyst = False
    $ alt_day2_mt_help = False
    $ alt_day2_mi_met = False
    $ alt_day2_mi_snap = False
    $ alt_day2_sl_bf = False
    $ alt_day2_un_secret_spot = 0
    $ alt_day2_us_dubstep = False
    $ alt_day2_us_escape = False
    $ alt_day2_walk = 0
    $ alt_day2_fail = 0
    $ alt_day2_sup = 0
    $ alt_day2_cardgame_block_rollback = False
    $ alt_day2_olga_help = False
    $ alt_day2_slot_us_cake = False
    $ alt_day2_cake = False
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
    $ alt_day2_sl_chased = False
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
    $ alt_day3_mi_date = False
    $ alt_day3_mi_dj = False 
    $ alt_day3_mi_event = False
    $ alt_day3_mi_rejected = False
    $ alt_day3_mi_invite = False
    $ alt_day3_mi_invite2 = False
    $ alt_day3_mi_donor = False
    $ alt_day3_sl_bath_voy = False
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
    $ alt_day3_ladder_phys = 0
    $ alt_day3_ladder_mt = 0
    $ alt_day3_technoquest_st3_help = False
    $ alt_day3_un_fz_evening = False
    $ alt_day3_dv_rep = False
    $ alt_day3_un_fz_dinner = False
    return