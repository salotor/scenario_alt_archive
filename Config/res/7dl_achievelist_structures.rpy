init 9999 python:
    ##### КАК ЭТО РАБОТАЕТ #####
    # Все концовки загоняются в массив концовок рута (в том порядке, в котором они и будут выводиться).
    # А руты - в списки рутов персонажа.
    #
    # Объект sdl_achv_Achievement (ачивка):
    ## icon          - иконка концовки
    ## persistent    - название перзистента
    ## text          - надпись (объявляется в ресурсах), описывающая характер концовки
    ## prerequisites - список объектов sdl_achv_Prerequisite, описывающих требования для выхода на концовку
    ## replay        - объект sdl_achv_Replay, использующийся для перехода к концовке
    #
    # Объект sdl_achv_Prerequisite (требование к концовке):
    ## text         - надпись (объявляется в ресурсах), описывающая тип требования
    ## achievements - список объектов sdl_achv_Achievement, удовлетворяющих условию (поля prerequisites и replay не обязательны)
    ###
    ### Пример: пусть для выхода на концовку стоит условие:
    ###     (persistent.us_7dl_un or persistent.us_7dl_mi) and persistent.us_px_rf_good
    ### Тогда нужно создать 2 объекта-требования
    ###     sdl_achv_Prerequisite(
    ###         "sdl_achv_info_end",
    ###         {
    ###             sdl_achv_Achievement("acm_logo_us_px", "us_px_rf_good", "sdl_achv_us_good", None, None)
    ###         }
    ###     ),
    ###     sdl_achv_Prerequisite(
    ###         "sdl_achv_info_end",
    ###         {
    ###             sdl_achv_Achievement("acm_logo_us_hi", "us_7dl_un", "sdl_achv_us_un", None, None),
    ###             sdl_achv_Achievement("acm_logo_us_openup", "us_7dl_mi", "sdl_achv_us_mi", None, None)
    ###         }
    ###     )
    #
    # Объект sdl_achv_Replay (повтор):
    ## label - метка, к которой надо перейти для просмотра концовки
    ## scope - scope-параметр ренпаевского Replay. Здесь следует инициализировать необходимые переменные
    ############################
    
    # Массивы концовок всех рутов
    
    ## Мику-7дл
    sdl_achv_array_mi_7dl = [
        sdl_achv_Achievement(    # ТруЪ
            "acm_logo_mi_thank_you",
            "mi_7dl_true",
            "sdl_achv_mi_true",
            {
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_mi_unlike", "mi_7dl_herc_exc", "sdl_achv_mi_HE_excl", None, None),
                        sdl_achv_Achievement("acm_logo_mi_come", "mi_7dl_loki_exc", "sdl_achv_mi_LO_excl", None, None),
                        sdl_achv_Achievement("acm_logo_mi_watashi", "mi_7dl_dr_exc", "sdl_achv_mi_DR_excl", None, None)
                    }
                )
            },
            sdl_achv_Replay("alt_day7_mi_7dl_thank_you", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Гуд-M
            "acm_logo_mi_dark_dreams",
            "mi_7dl_good_human",
            "sdl_achv_mi_good",
            {},
            sdl_achv_Replay("alt_day7_mi_7dl_dark_dreams", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Гуд-S
            "acm_logo_mi_sparkle",
            "mi_7dl_good_star",
            "sdl_achv_mi_good_RF",
            {},
            sdl_achv_Replay("alt_day7_mi_7dl_sparkle", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Эксклюзив-Локи
            "acm_logo_mi_come",
            "mi_7dl_loki_exc",
            "sdl_achv_mi_LO_excl",
            {
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_mi_dark_dreams", "mi_7dl_good_human", "sdl_achv_mi_good", None, None),
                        sdl_achv_Achievement("acm_logo_mi_sparkle", "mi_7dl_good_star", "sdl_achv_mi_good_RF", None, None)
                    }
                )
            },
            sdl_achv_Replay("alt_day7_mi_7dl_sinthetic", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Эксклюзив-Герк
            "acm_logo_mi_unlike",
            "mi_7dl_herc_exc",
            "sdl_achv_mi_HE_excl",
            {
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_mi_dark_dreams", "mi_7dl_good_human", "sdl_achv_mi_good", None, None),
                        sdl_achv_Achievement("acm_logo_mi_sparkle", "mi_7dl_good_star", "sdl_achv_mi_good_RF", None, None)
                    }
                )
            },
            sdl_achv_Replay("alt_day7_mi_7dl_unlike", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Эксклюзив-Дрищ
            "acm_logo_mi_watashi",
            "mi_7dl_dr_exc",
            "sdl_achv_mi_DR_excl",
            {
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_mi_dark_dreams", "mi_7dl_good_human", "sdl_achv_mi_good", None, None),
                        sdl_achv_Achievement("acm_logo_mi_sparkle", "mi_7dl_good_star", "sdl_achv_mi_good_RF", None, None)
                    }
                )
            },
            sdl_achv_Replay("alt_day7_mi_7dl_come_back", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Нейтрал-M
            "acm_logo_mi_happy_again",
            "mi_7dl_neutral_human",
            "sdl_achv_mi_neutral",
            {},
            sdl_achv_Replay("alt_day7_mi_7dl_happy_again", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Нейтрал-S
            "acm_logo_mi_club27",
            "mi_7dl_neutral_star",
            "sdl_achv_mi_neutral",
            {},
            sdl_achv_Replay("alt_day7_mi_7dl_club27", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Бэд-M
            "acm_logo_mi_liar",
            "mi_7dl_bad_human",
            "sdl_achv_mi_bad",
            {},
            sdl_achv_Replay("alt_day7_mi_7dl_liar", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Бэд-S
            "acm_logo_mi_dam_cpu",
            "mi_7dl_bad_star",
            "sdl_achv_mi_bad",
            {},
            sdl_achv_Replay("alt_day7_mi_7dl_dam_CPU", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Постскриптум
            "acm_logo_mi_bitter_truth",
            "mi_7dl_ps",
            "sdl_achv_mi_pst",
            {
                sdl_achv_Prerequisite(
                    "sdl_achv_info_pst",
                    None
                )
            },
            sdl_achv_Replay("alt_day7_mi_7dl_postscriptum", {"alt_replay_on" : "True"})
        )
    ]
    
    ## Мику-DJ
    sdl_achv_array_mi_djt = [
        sdl_achv_Achievement(    # ТруЪ
            "acm_logo_mi_namiki",
            "mi_dj_true",
            "sdl_achv_mi_true",
            {},
            sdl_achv_Replay("alt_day7_mi_dj_true_end", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Гуд-Япония
            "acm_logo_mi_ricochet",
            "mi_dj_good_jap",
            "sdl_achv_mi_good",
            {},
            sdl_achv_Replay("alt_day7_mi_dj_jp_good_end", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Гуд-РФ
            "acm_logo_mi_allyours",
            "mi_dj_good_rf",
            "sdl_achv_mi_good_RF",
            {},
            sdl_achv_Replay("alt_day7_mi_dj_rf_good_end", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Бэд
            "acm_logo_mi_new_happy",
            "mi_dj_bad",
            "sdl_achv_mi_bad",
            {},
            sdl_achv_Replay("alt_day7_mi_dj_bad_end", {"alt_replay_on" : "True"})
        )
    ]
    
    ## Алиса-7дл
    sdl_achv_array_dv_7dl = [
        sdl_achv_Achievement(    # ТруЪ
            "acm_logo_dv_true",
            "dv_7dl_true",
            "sdl_achv_dv_true",
            {
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_dv_ussr_good", "dv_7dl_good_ussr", "sdl_achv_dv_good_US", None, None)
                    }
                )
            },
            sdl_achv_Replay("alt_day7_dv_7dl_true", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Гуд-СССР
            "acm_logo_dv_ussr_good",
            "dv_7dl_good_ussr",
            "sdl_achv_dv_good_US",
            {},
            sdl_achv_Replay("alt_day7_dv_7dl_ussr_epilogue", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Гуд-РФ
            "acm_logo_dv_morethanlife",
            "dv_7dl_good_rf",
            "sdl_achv_dv_good_RF",
            {},
            sdl_achv_Replay("alt_day7_dv_7dl_rf_epilogue", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Реджект-СССР
            "acm_logo_dv_tillend",
            "dv_7dl_reject_ussr",
            "sdl_achv_dv_rejc_US",
            {},
            sdl_achv_Replay("alt_day7_dv_7dl_rej_ussr_end", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Реджект-РФ
            "acm_logo_dv_gohome",
            "dv_7dl_reject_rf",
            "sdl_achv_dv_rejc_RF",
            {},
            sdl_achv_Replay("alt_day7_dv_7dl_rej_rf_end", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Транзит-Ольга
            "acm_logo_dv_drunk",
            "dv_7dl_bad_mt",
            "sdl_achv_dv_HE_tran",
            {},
            sdl_achv_Replay("alt_day7_dv_7dl_bad_end", {"alt_replay_on" : "True", "herc" : "True", "alt_day7_dv_7dl_check" : 5})
        ),
        sdl_achv_Achievement(    # Транзит-Лена
            "acm_logo_dv_meetmethere",
            "dv_7dl_un",
            "sdl_achv_dv_tran",
            {},
            sdl_achv_Replay("alt_day7_dv_7dl_un_end", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Эксклюзив-Локи
            "acm_logo_dv_tulpa",
            "dv_7dl_tulpa",
            "sdl_achv_dv_LO_excl",
            {},
            sdl_achv_Replay("alt_day7_dv_7dl_tulpa_end", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Бэд
            "acm_logo_dv_theresnoway",
            "dv_7dl_bad",
            "sdl_achv_dv_bad",
            {},
            sdl_achv_Replay("alt_day7_dv_7dl_bad_end", {"alt_replay_on" : "True"})
        )
    ]
    
    ## Славя-7дл
    sdl_achv_array_sl_7dl = [
        sdl_achv_Achievement(    # ТруЪ
            "acm_logo_sl_no_wonder",
            "sl_7dl_true",
            "sdl_achv_sl_true",
            {
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_sl_radio", "sl_7dl_loki_good", "sdl_achv_sl_LO_good", None, None)
                    }
                ),
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_sl_neon", "sl_7dl_herc_good2", "sdl_achv_sl_HE_good", None, None)
                    }
                ),
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_sl_dr_un", "sl_7dl_good2", "sdl_achv_sl_DR_good", None, None)
                    }
                )
            },
            sdl_achv_Replay("alt_day7_sl_7dl_true", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # РФ-гуд
            "acm_logo_sl_till_sunrise",
            "sl_7dl_good_rf",
            "sdl_achv_sl_good_RF",
            {},
            sdl_achv_Replay("alt_day7_sl_7dl_rf_good", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Локи-Гуд
            "acm_logo_sl_radio",
            "sl_7dl_loki_good",
            "sdl_achv_sl_LO_good",
            {
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_sl_am_home", "sl_7dl_loki_neu", "sdl_achv_sl_LO_neutral", None, None),
                        sdl_achv_Achievement("acm_logo_sl_pan", "sl_7dl_loki_rej", "sdl_achv_sl_LO_rejc", None, None)
                    }
                )
            },
            sdl_achv_Replay("alt_day7_sl_7dl_loki_radio", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Локи-Нейтрал
            "acm_logo_sl_am_home",
            "sl_7dl_loki_neu",
            "sdl_achv_sl_LO_neutral",
            {},
            sdl_achv_Replay("alt_day7_sl_7dl_loki_am_home", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Локи-Реджект
            "acm_logo_sl_pan",
            "sl_7dl_loki_rej",
            "sdl_achv_sl_LO_rejc",
            {},
            sdl_achv_Replay("alt_day7_sl_7dl_loki_oafa", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Герк-Гуд
            "acm_logo_sl_neon",
            "sl_7dl_herc_good2",
            "sdl_achv_sl_HE_good",
            {
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_sl_right_road", "sl_7dl_herc_good", "sdl_achv_sl_HE_neutral", None, None)
                    }
                )
            },
            sdl_achv_Replay("alt_day7_sl_7dl_herc_neon", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Герк-Гуд
            "acm_logo_sl_right_road",
            "sl_7dl_herc_good",
            "sdl_achv_sl_HE_neutral",
            {},
            sdl_achv_Replay("alt_day7_sl_7dl_herc_right_road", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Дрищ-Гуд
            "acm_logo_sl_wasted",
            "sl_7dl_good",
            "sdl_achv_sl_DR_good",
            {},
            sdl_achv_Replay("alt_day7_sl_7dl_wasted", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Дрищ-Гуд 2
            "acm_logo_sl_dr_un",
            "sl_7dl_good2",
            "sdl_achv_sl_DR_good",
            {
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_sl_wasted", "sl_7dl_good", "sdl_achv_sl_DR_good", None, None)
                    }
                )
            },
            sdl_achv_Replay("alt_day7_sl_7dl_loopback", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Бэд
            "acm_logo_sl_missed",
            "sl_7dl_bad",
            "sdl_achv_sl_bad",
            {},
            sdl_achv_Replay("alt_day7_sl_7dl_missed", {"alt_replay_on" : "True"})
        )
    ]
    
    ## Славя-Классик
    sdl_achv_array_sl_clt = [
        sdl_achv_Achievement(    # Инт-ТруЪ
            "acm_logo_sl_ok",
            "sl_cl_int_ok",
            "sdl_achv_sl_true_IN",
            {
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_sl_fantazm", "sl_cl_int_good", "sdl_achv_sl_good_IN", None, None)
                    }
                )
            },
            sdl_achv_Replay("alt_day7_sl_will", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Инт-гуд
            "acm_logo_sl_fantazm",
            "sl_cl_int_good",
            "sdl_achv_sl_good_IN",
            {
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_sl_good", "sl_cl_good_rf", "sdl_achv_sl_good_RF", None, None),
                        sdl_achv_Achievement("acm_logo_sl_worth", "sl_cl_good_rf2", "sdl_achv_sl_good_RF", None, None),
                        sdl_achv_Achievement("acm_logo_sl_good", "sl_cl_good_ussr", "sdl_achv_sl_good_US", None, None)
                    }
                )
            },
            sdl_achv_Replay("alt_day7_sl_duty", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Инт-бэд
            "acm_logo_sl_lone",
            "sl_cl_int_bad",
            "sdl_achv_sl_bad_IN",
            {
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_sl_good", "sl_cl_good_rf", "sdl_achv_sl_good_RF", None, None),
                        sdl_achv_Achievement("acm_logo_sl_worth", "sl_cl_good_rf2", "sdl_achv_sl_good_RF", None, None),
                        sdl_achv_Achievement("acm_logo_sl_good", "sl_cl_good_ussr", "sdl_achv_sl_good_US", None, None)
                    }
                )
            },
            sdl_achv_Replay("alt_day7_sl_lone", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # СССР-гуд
            "acm_logo_sl_good",
            "sl_cl_good_ussr",
            "sdl_achv_sl_good_US",
            {},
            sdl_achv_Replay("alt_day7_sl_good", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # РФ-гуд
            "acm_logo_sl_worth",
            "sl_cl_good_rf2",
            "sdl_achv_sl_good_RF",
            {},
            sdl_achv_Replay("alt_day7_sl_rf2", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # РФ-гуд (Плюс-минус)
            "acm_logo_sl_good",
            "sl_cl_good_rf",
            "sdl_achv_sl_good_RF",
            {},
            sdl_achv_Replay("alt_day7_sl_rf_good", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Реджект-РФ
            "acm_logo_sl_same_place",
            "sl_cl_reject_same",
            "sdl_achv_sl_rejc_RF",
            {},
            sdl_achv_Replay("alt_day7_sl_reject_same", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Реджект-2
            "acm_logo_sl_too_late",
            "sl_cl_reject_late",
            "sdl_achv_sl_rejc_RF",
            {},
            sdl_achv_Replay("alt_achv_sl_reject_late", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Эксклюзив-Локи
            "acm_logo_sl_be_ok",
            "sl_cl_cata",
            "sdl_achv_sl_LO_excl",
            {},
            sdl_achv_Replay("alt_day6_sl_cl_become_a_hero", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Бэд
            "acm_logo_sl_bad",
            "sl_cl_bad",
            "sdl_achv_sl_bad",
            {},
            sdl_achv_Replay("alt_day7_sl_cl_bad", {"alt_replay_on" : "True"})
        )
    ]
    
    ## Лена-7дл
    sdl_achv_array_un_7dl = [
        sdl_achv_Achievement(    # ТруЪ
            "acm_logo_un_true",
            "un_7dl_true",
            "sdl_achv_un_true",
            {
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_un_good", "un_7dl_good_rf", "sdl_achv_un_good_RF", None, None)
                    }
                ),
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_un_good2", "un_7dl_good_ussr", "sdl_achv_un_good_US", None, None)
                    }
                )
            },
            sdl_achv_Replay("alt_day7_un_7dl_true", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # ТруЪ-транзит
            "acm_logo_un_transit",
            "un_7dl_true_transit",
            "sdl_achv_un_true_transit",
            {},
            sdl_achv_Replay("alt_day7_un_7dl_transit", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Гуд-СССР
            "acm_logo_un_good2",
            "un_7dl_good_ussr",
            "sdl_achv_un_good_US",
            {},
            sdl_achv_Replay("alt_day7_un_7dl_ussr", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Гуд-РФ
            "acm_logo_un_good",
            "un_7dl_good_rf",
            "sdl_achv_un_good_RF",
            {},
            sdl_achv_Replay("alt_day7_un_7dl_rf", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Реджект
            "acm_logo_un_shelter",
            "un_7dl_rej",
            "sdl_achv_un_rejc",
            {
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_mt_named_olga", "mt_7dl_good", "sdl_achv_mt_good", None, None)
                    }
                )
            },
            sdl_achv_Replay("alt_day7_un_7dl_rej", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Бэд
            "acm_logo_un_sui",
            "un_7dl_bad",
            "sdl_achv_un_bad",
            {},
            sdl_achv_Replay("alt_day7_un_7dl_epilogue_bad", {"alt_replay_on" : "True"})
        )
    ]
    
    ## Ольга-7дл
    sdl_achv_array_mt_7dl = [
        sdl_achv_Achievement(    # ТруЪ
            "acm_logo_mt_ending",
            "mt_7dl_true",
            "sdl_achv_mt_true",
            {
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_mt_named_olga", "mt_7dl_good", "sdl_achv_mt_good", None, None)
                    }
                )
            },
            sdl_achv_Replay("alt_day7_mt_7dl_true", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Гуд
            "acm_logo_mt_named_olga",
            "mt_7dl_good",
            "sdl_achv_mt_good",
            {
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_mt_cause", "mt_7dl_bad", "sdl_achv_mt_bad", None, None)
                    }
                )
            },
            sdl_achv_Replay("alt_day7_mt_7dl_good", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Нейтрал
            "acm_logo_mt_ever_after",
            "mt_7dl_neutral",
            "sdl_achv_mt_neutral",
            {
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_mt_named_olga", "mt_7dl_good", "sdl_achv_mt_good", None, None)
                    }
                )
            },
            sdl_achv_Replay("alt_day7_mt_7dl_ever_after", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Бэд
            "acm_logo_mt_cause",
            "mt_7dl_bad",
            "sdl_achv_mt_bad",
            {},
            sdl_achv_Replay("alt_day7_mt_7dl_bad", {"alt_replay_on" : "True"})
        )
    ]
    
    ## Ульяна-7дл
    sdl_achv_array_us_7dl = [
        sdl_achv_Achievement(    # ТруЪ
            "acm_logo_us_true",
            "us_7dl_true",
            "sdl_achv_us_true",
            {
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_us_px", "us_px_rf_good", "sdl_achv_us_good", None, None)
                    }
                ),
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_us_hi", "us_7dl_un", "sdl_achv_us_un", None, None),
                        sdl_achv_Achievement("acm_logo_us_openup", "us_7dl_mi", "sdl_achv_us_mi", None, None)
                    }
                )
            },
            sdl_achv_Replay("alt_day7_us_7dl_ever_after", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Гуд
            "acm_logo_us_semische",
            "us_7dl_good",
            "sdl_achv_us_good",
            {},
            sdl_achv_Replay("alt_day7_us_7dl_reunite", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Лена-энд
            "acm_logo_us_hi",
            "us_7dl_un",
            "sdl_achv_us_un",
            {},
            sdl_achv_Replay("alt_day7_us_7dl_lenaforever", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Мику-энд
            "acm_logo_us_openup",
            "us_7dl_mi",
            "sdl_achv_us_mi",
            {},
            sdl_achv_Replay("alt_day7_us_7dl_mikuforever", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Бэд
            "acm_logo_us_bad",
            "us_7dl_bad",
            "sdl_achv_us_bad",
            {},
            sdl_achv_Replay("alt_day7_us_7dl_bad", {"alt_replay_on" : "True"})
        )
    ]
    
    ## Ульяна-Огоньки
    sdl_achv_array_us_pxs = [
        sdl_achv_Achievement(    # ТруЪ
            "acm_logo_us_fairytale",
            "us_px_true",
            "sdl_achv_us_true",
            {
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_us_semische", "us_7dl_good", "sdl_achv_us_good", None, None)
                    }
                )
            },
            sdl_achv_Replay("alt_day7_us_px_fairytale", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Гуд
            "acm_logo_us_px",
            "us_px_rf_good",
            "sdl_achv_us_good",
            {},
            sdl_achv_Replay("alt_day7_us_px_dejavu", {"alt_replay_on" : "True"})
        )
    ]
    
    ## Одиночка-Сыч
    sdl_achv_array_me_owl = [
        sdl_achv_Achievement(    # ТруЪ
            "acm_logo_neu_true",
            "neu_true",
            "sdl_achv_me_true",
            {
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_neu_neu", "neu_loki_neu", "sdl_achv_me_LO_neutral", None, None),
                        sdl_achv_Achievement("acm_logo_neu_neu", "neu_neu", "sdl_achv_me_DR_neutral", None, None)
                    }
                ),
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_neu_bad", "neu_bad", "sdl_achv_me_bad", None, None)
                    }
                )
            },
            sdl_achv_Replay("alt_day7_neu_true", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Локи-Нейтрал
            "acm_logo_neu_neu",
            "neu_loki_neu",
            "sdl_achv_me_LO_neutral",
            {
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_neu_bad", "neu_bad", "sdl_achv_me_bad", None, None)
                    }
                )
            },
            sdl_achv_Replay("alt_day7_neu_neu_loki", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Дрищ-Нейтрал
            "acm_logo_neu_neu",
            "neu_neu",
            "sdl_achv_me_DR_neutral",
            {
                sdl_achv_Prerequisite(
                    "sdl_achv_info_end",
                    {
                        sdl_achv_Achievement("acm_logo_neu_bad", "neu_bad", "sdl_achv_me_bad", None, None)
                    }
                )
            },
            sdl_achv_Replay("alt_day7_neu_neu", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Бэд
            "acm_logo_neu_bad",
            "neu_bad",
            "sdl_achv_me_bad",
            {},
            sdl_achv_Replay("alt_day7_neu_bad", {"alt_replay_on" : "True"})
        )
    ]
    
    ## Одиночка-Прочее
    sdl_achv_array_me_smt = [
        sdl_achv_Achievement(    # Ламповость
            "acm_logo_me_lamp",
            "alt_lamp",
            "sdl_achv_me_kat",
            {},
            sdl_achv_Replay("alt_day6_un_7dl_letmeout", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # Глубина
            "acm_logo_me_deep",
            "alt_deep",
            "sdl_achv_me_kat",
            {},
            sdl_achv_Replay("alt_achv_deep_deep", {"alt_replay_on" : "True"})
        ),
        sdl_achv_Achievement(    # QTE
            "acm_logo_me_qte",
            "alt_qte",
            "sdl_achv_me_qte",
            {},
            None
        ),
        sdl_achv_Achievement(    # QTE victim
            "acm_logo_me_victim",
            "alt_victim",
            "acm_achv_me_victim",
            {},
            None
        )
    ]
    
    
    
    
    
    # Руты
    ## Мику
    sdl_achv_route_mi_7dl = sdl_achv_Route("sdl_achv_mi_7dl", "sdl_achv_7dl_route", "sdl_achv_mi_7dl_active", "sdl_achv_7dl_inactive",   sdl_achv_array_mi_7dl)
    sdl_achv_route_mi_clt = sdl_achv_Route("sdl_achv_mi_clt", "sdl_achv_clt_route", "sdl_achv_mi_cl_active",  "sdl_achv_mi_cl_inactive", [],                   completed=False)
    sdl_achv_route_mi_djt = sdl_achv_Route("sdl_achv_mi_djt", "sdl_achv_xxx_route", "sdl_achv_mi_dj_active",  "sdl_achv_mi_dj_inactive", sdl_achv_array_mi_djt)
    ## Алиса
    sdl_achv_route_dv_7dl = sdl_achv_Route("sdl_achv_dv_7dl", "sdl_achv_7dl_route", "sdl_achv_dv_7dl_active", "sdl_achv_7dl_inactive",   sdl_achv_array_dv_7dl)
    sdl_achv_route_dv_clt = sdl_achv_Route("sdl_achv_dv_clt", "sdl_achv_clt_route", "sdl_achv_dv_cl_active",  "sdl_achv_dv_cl_inactive", [],                   completed=False)
    sdl_achv_route_dv_djt = sdl_achv_Route("sdl_achv_dv_djt", "sdl_achv_xxx_route", "sdl_achv_dv_dj_active",  "sdl_achv_dv_dj_inactive", [],                   completed=False)
    ## Славя
    sdl_achv_route_sl_7dl = sdl_achv_Route("sdl_achv_sl_7dl", "sdl_achv_7dl_route", "sdl_achv_sl_7dl_active", "sdl_achv_7dl_inactive",   sdl_achv_array_sl_7dl)
    sdl_achv_route_sl_clt = sdl_achv_Route("sdl_achv_sl_clt", "sdl_achv_clt_route", "sdl_achv_sl_cl_active",  "sdl_achv_sl_cl_inactive", sdl_achv_array_sl_clt)
    sdl_achv_route_sl_wht = sdl_achv_Route("sdl_achv_sl_wht", "sdl_achv_xxx_route", "sdl_achv_sl_wh_active",  "sdl_achv_sl_wh_inactive", [],                   completed=False)
    ## Лена
    sdl_achv_route_un_7dl = sdl_achv_Route("sdl_achv_un_7dl", "sdl_achv_7dl_route", "sdl_achv_un_7dl_active", "sdl_achv_7dl_inactive",   sdl_achv_array_un_7dl)
    sdl_achv_route_un_clt = sdl_achv_Route("sdl_achv_un_clt", "sdl_achv_clt_route", "sdl_achv_un_cl_active",  "sdl_achv_un_cl_inactive", [],                   completed=False)
    sdl_achv_route_un_fzd = sdl_achv_Route("sdl_achv_un_fzd", "sdl_achv_xxx_route", "sdl_achv_un_fz_active",  "sdl_achv_un_fz_inactive", [],                   completed=False)
    ## Ольга
    sdl_achv_route_mt_7dl = sdl_achv_Route("sdl_achv_mt_7dl", "sdl_achv_7dl_route", "sdl_achv_mt_7dl_active", "sdl_achv_7dl_inactive",   sdl_achv_array_mt_7dl)
    ## Ульяна
    sdl_achv_route_us_7dl = sdl_achv_Route("sdl_achv_us_7dl", "sdl_achv_7dl_route", "sdl_achv_us_7dl_active", "sdl_achv_7dl_inactive",   sdl_achv_array_us_7dl)
    sdl_achv_route_us_pxs = sdl_achv_Route("sdl_achv_us_pxs", "sdl_achv_xxx_route", "sdl_achv_us_px_active",  "sdl_achv_us_px_inactive", sdl_achv_array_us_pxs)
    ## Одиночка
    sdl_achv_route_me_d3r = sdl_achv_Route("sdl_achv_me_d3r", "sdl_achv_d3r_route", "sdl_achv_me_7dl_active", "sdl_achv_7dl_inactive",   [],                   completed=False)
    sdl_achv_route_me_owl = sdl_achv_Route("sdl_achv_me_owl", "sdl_achv_7dl_route", "sdl_achv_me_ow_active",  "sdl_achv_me_ow_inactive", sdl_achv_array_me_owl)
    sdl_achv_route_me_noi = sdl_achv_Route("sdl_achv_me_noi", "sdl_achv_xxx_route", "sdl_achv_me_no_active",  "sdl_achv_me_no_inactive", [],                   completed=False)
    sdl_achv_route_me_smt = sdl_achv_Route("sdl_achv_me_smt", "sdl_achv_smt_route", "sdl_achv_me_sm_active",  "sdl_achv_me_sm_inactive", sdl_achv_array_me_smt)
    
    
    
    # Персонажи
    sdl_achv_mi_routes = [
        sdl_achv_route_mi_7dl,
        sdl_achv_route_mi_clt,
        sdl_achv_route_mi_djt
    ]
    sdl_achv_dv_routes = [
        sdl_achv_route_dv_7dl,
        sdl_achv_route_dv_clt,
        sdl_achv_route_dv_djt
    ]
    sdl_achv_sl_routes = [
        sdl_achv_route_sl_7dl,
        sdl_achv_route_sl_clt,
        sdl_achv_route_sl_wht
    ]
    sdl_achv_un_routes = [
        sdl_achv_route_un_7dl,
        sdl_achv_route_un_clt,
        sdl_achv_route_un_fzd
    ]
    sdl_achv_mt_routes = [
        sdl_achv_route_mt_7dl
    ]
    sdl_achv_us_routes = [
        sdl_achv_route_us_7dl,
        sdl_achv_route_us_pxs
    ]
    sdl_achv_me_routes = [
        sdl_achv_route_me_d3r,
        sdl_achv_route_me_owl,
        sdl_achv_route_me_noi,
        sdl_achv_route_me_smt
    ]
    