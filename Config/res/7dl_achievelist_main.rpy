label scenario__sdl_achvlist_Author:
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

    $ day_time()
    $ persistent.sprite_time = "day"
    $ plthr = u"Достижения"
    play ambience ambience_7dl["safe"] fadein 5

# ------------------------------------------------
# Показываем первоначальный фон
    scene bg sdl_ach_inactive
    show sdl_achv_extB_7dl: #Иконка Ausgang
        pos(380, 350)
    call screen sdl_achvlist_Author

screen mi_button_active:
    add "mi_button_active" pos (0,0)
screen dv_button_active:
    add "dv_button_active" pos (0,344)
screen sl_button_active:
    add "sl_button_active" pos (0,734)
screen un_button_active:
    add "un_button_active" pos (1289,0)
screen mt_button_active:
    add "mt_button_active" pos (1559,343)
screen us_button_active:
    add "us_button_active" pos (1561,530)
screen me_button_active:
    add "me_button_active" pos (1289,735)
# ------------------------------------------------
#Переходы на концовки
screen de_check_active1:
    add "de_check_active1" pos (590, 40)
screen de_check_active2:
    add "de_check_active2" pos (590, 104)
screen de_check_active3:
    add "de_check_active3" pos (590,168)
screen de_check_active4:
    add "de_check_active4" pos (590, 232)
screen de_check_active5:
    add "de_check_active5" pos (590, 296)
screen de_check_active6:
    add "de_check_active6" pos (590, 360)
screen de_check_active7:
    add "de_check_active7" pos (590, 424)
screen de_check_active8:
    add "de_check_active8" pos (590, 488)
screen de_check_active9:
    add "de_check_active9" pos (590, 552)
screen de_check_active10:
    add "de_check_active10" pos (590, 616)
screen de_check_active11:
    add "de_check_active11" pos (590, 680)
screen de_check_active12:
    add "de_check_active12" pos (590, 744)
# ------------------------------------------------
#Информация о концовках
screen de_info_active1:
    add "de_info_active1" pos (590, 40)
screen de_info_active2:
    add "de_info_active2" pos (590, 104)
screen de_info_active3:
    add "de_info_active3" pos (590,168)
screen de_info_active4:
    add "de_info_active4" pos (590, 232)
screen de_info_active5:
    add "de_info_active5" pos (590, 296)
screen de_info_active6:
    add "de_info_active6" pos (590, 360)
screen de_info_active7:
    add "de_info_active7" pos (590, 424)
screen de_info_active8:
    add "de_info_active8" pos (590, 488)
screen de_info_active9:
    add "de_info_active9" pos (590, 552)
screen de_info_active10:
    add "de_info_active10" pos (590, 616)
screen de_info_active11:
    add "de_info_active11" pos (590, 680)
screen de_info_active12:
    add "de_info_active12" pos (590, 744)
# ------------------------------------------------
#Дубли концовок
screen acm_logo_mt_cause:
    add "acm_logo_mt_cause" xcenter 750 ycenter 860
screen acm_logo_mt_named_olga:
    add "acm_logo_mt_named_olga" xcenter 750 ycenter 860
screen acm_logo_sl_fantazm:
    add "acm_logo_sl_fantazm" xcenter 750 ycenter 860
screen acm_logo_sl_good:
    add "acm_logo_sl_good" xcenter 750 ycenter 860
screen acm_logo_mi_sparkle:
    add "acm_logo_mi_sparkle" xcenter 750 ycenter 860
screen acm_logo_mi_watashi:
    add "acm_logo_mi_watashi" xcenter 750 ycenter 860
# ------------------------------------------------
#Иконки рутов
#7ДЛ
screen sdl_logo_active:
    add "sdl_logo_active" pos (980,18)
screen sdl_logo_inactive:
    add "sdl_logo_inactive" pos (980,18)

#Мику
#Классик
screen sdl_mi_cl_active:
    add "sdl_mi_cl_active" pos (1110,18)
screen sdl_mi_cl_inactive:
    add "sdl_mi_cl_inactive" pos (1110,18)
#Диджей
screen sdl_mi_dj_active:
    add "sdl_mi_dj_active" pos (1215,18)
screen sdl_mi_dj_inactive:
    add "sdl_mi_dj_inactive" pos (1215,18)

#Алисхен
#Классик
screen sdl_dv_cl_active:
    add "sdl_dv_cl_active" pos (1110,18)
screen sdl_dv_cl_inactive:
    add "sdl_dv_cl_inactive" pos (1110,18)
#Диджей
screen sdl_dv_dj_active:
    add "sdl_dv_dj_active" pos (1215,18)
screen sdl_dv_dj_inactive:
    add "sdl_dv_dj_inactive" pos (1215,18)

#Славя
#Классик
screen sdl_sl_cl_active:
    add "sdl_sl_cl_active" pos (1110,18)
screen sdl_sl_cl_inactive:
    add "sdl_sl_cl_inactive" pos (1110,18)
#Ведьма
screen sdl_sl_wh_active:
    add "sdl_sl_wh_active" pos (1215,18)
screen sdl_sl_wh_inactive:
    add "sdl_sl_wh_inactive" pos (1215,18)

#Лена
#Классик
screen sdl_un_cl_active:
    add "sdl_un_cl_active" pos (1110,18)
screen sdl_un_cl_inactive:
    add "sdl_un_cl_inactive" pos (1110,18)
#ФЗ
screen sdl_un_fz_active:
    add "sdl_un_fz_active" pos (1215,18)
screen sdl_un_fz_inactive:
    add "sdl_un_fz_inactive" pos (1215,18)

#Одиночка
#Нуар
screen sdl_me_no_active:
    add "sdl_me_no_active" pos (1110,18)
screen sdl_me_no_inactive:
    add "sdl_me_no_inactive" pos (1110,18)
#Прочее
screen sdl_me_sm_active:
    add "sdl_me_sm_active" pos (1215,18)
screen sdl_me_sm_inactive:
    add "sdl_me_sm_inactive" pos (1215,18)
# ------------------------------------------------
#Надписи-расшифровки
#Удалятор
screen sdl_achv_delA_7dl:
    add "sdl_achv_delA_7dl" pos (380,680)

#Выход
screen sdl_achv_extA_7dl:
    add "sdl_achv_extA_7dl" pos (380,350)

#Надписи рутов
screen sdl_achv_mi_djtA:#Мику
    add "sdl_achv_mi_djtA" xcenter 960 ycenter 1010
screen sdl_achv_mi_cltA:
    add "sdl_achv_mi_cltA" xcenter 960 ycenter 1010
screen sdl_achv_mi_7dlA:
    add "sdl_achv_mi_7dlA" xcenter 960 ycenter 1010

screen sdl_achv_dv_djtA:#Алисхен
    add "sdl_achv_dv_djtA" xcenter 960 ycenter 1010
screen sdl_achv_dv_cltA:
    add "sdl_achv_dv_cltA" xcenter 960 ycenter 1010
screen sdl_achv_dv_7dlA:
    add "sdl_achv_dv_7dlA" xcenter 960 ycenter 1010

screen sdl_achv_sl_whtA:#Славя
    add "sdl_achv_sl_whtA" xcenter 960 ycenter 1010
screen sdl_achv_sl_cltA:
    add "sdl_achv_sl_cltA" xcenter 960 ycenter 1010
screen sdl_achv_sl_7dlA:
    add "sdl_achv_sl_7dlA" xcenter 960 ycenter 1010

screen sdl_achv_un_fzdA:#Лена
    add "sdl_achv_un_fzdA" xcenter 960 ycenter 1010
screen sdl_achv_un_cltA:
    add "sdl_achv_un_cltA" xcenter 960 ycenter 1010
screen sdl_achv_un_7dlA:
    add "sdl_achv_un_7dlA" xcenter 960 ycenter 1010

screen sdl_achv_me_smtA:#Одиночка
    add "sdl_achv_me_smtA" xcenter 960 ycenter 1010
screen sdl_achv_me_noiA:
    add "sdl_achv_me_noiA" xcenter 960 ycenter 1010
screen sdl_achv_me_d3rA:
    add "sdl_achv_me_d3rA" xcenter 960 ycenter 1010

#Типология рутов
screen sdl_achv_7dl_route:
    add "sdl_achv_7dl_route" pos (380,540)
screen sdl_achv_clt_route:
    add "sdl_achv_clt_route" pos (380,540)
screen sdl_achv_xxx_route:
    add "sdl_achv_xxx_route" pos (380,540)
screen sdl_achv_d3r_route:
    add "sdl_achv_d3r_route" pos (380,540)

#Надпись "Рут в разработке"
screen sdl_achv_need_routeA:
    add "sdl_achv_need_routeA" xcenter 700 ycenter 840

#Надписи концовок Мику
screen sdl_achv_neutral_mi:
    add "sdl_achv_neutral_mi" xcenter 700 ycenter 840
screen sdl_achv_bad_mi:
    add "sdl_achv_bad_mi" xcenter 700 ycenter 840
screen sdl_achv_excl_HE_mi:
    add "sdl_achv_excl_HE_mi" xcenter 700 ycenter 840
screen sdl_achv_excl_LO_mi:
    add "sdl_achv_excl_LO_mi" xcenter 700 ycenter 840
screen sdl_achv_excl_DR_mi:
    add "sdl_achv_excl_DR_mi" xcenter 700 ycenter 840
screen sdl_achv_true_mi:
    add "sdl_achv_true_mi" xcenter 700 ycenter 840
screen sdl_achv_good_RF_mi:
    add "sdl_achv_good_RF_mi" xcenter 700 ycenter 840
screen sdl_achv_good_mi:
    add "sdl_achv_good_mi" xcenter 700 ycenter 840

#Надписи концовок Алисхен
screen sdl_achv_bad_dv:
    add "sdl_achv_bad_dv" xcenter 700 ycenter 840
screen sdl_achv_excl_LO_dv:
    add "sdl_achv_excl_LO_dv" xcenter 700 ycenter 840
screen sdl_achv_good_RF_dv:
    add "sdl_achv_good_RF_dv" xcenter 700 ycenter 840
screen sdl_achv_good_US_dv:
    add "sdl_achv_good_US_dv" xcenter 700 ycenter 840
screen sdl_achv_rejc_RF_dv:
    add "sdl_achv_rejc_RF_dv" xcenter 700 ycenter 840
screen sdl_achv_rejc_US_dv:
    add "sdl_achv_rejc_US_dv" xcenter 700 ycenter 840
screen sdl_achv_tran_dv:
    add "sdl_achv_tran_dv" xcenter 700 ycenter 840

#Надписи концовок Славя
screen sdl_achv_true_IN_sl:
    add "sdl_achv_true_IN_sl" xcenter 700 ycenter 840
screen sdl_achv_bad_IN_sl:
    add "sdl_achv_bad_IN_sl" xcenter 700 ycenter 840
screen sdl_achv_bad_sl:
    add "sdl_achv_bad_sl" xcenter 700 ycenter 840
screen sdl_achv_excl_LO_sl:
    add "sdl_achv_excl_LO_sl" xcenter 700 ycenter 840
screen sdl_achv_good_US_sl:
    add "sdl_achv_good_US_sl" xcenter 700 ycenter 840
screen sdl_achv_good_RF_sl:
    add "sdl_achv_good_RF_sl" xcenter 700 ycenter 840
screen sdl_achv_good_IN_sl:
    add "sdl_achv_good_IN_sl" xcenter 700 ycenter 840
screen sdl_achv_rejc_RF_sl:
    add "sdl_achv_rejc_RF_sl" xcenter 700 ycenter 840

#Надписи концовок Лена
screen sdl_achv_true_un:
    add "sdl_achv_true_un" xcenter 700 ycenter 840
screen sdl_achv_true_un_transit:
    add "sdl_achv_true_un_transit" xcenter 700 ycenter 840
screen sdl_achv_bad_un:
    add "sdl_achv_bad_un" xcenter 700 ycenter 840
screen sdl_achv_good_US_un:
    add "sdl_achv_good_US_un" xcenter 700 ycenter 840
screen sdl_achv_good_RF_un:
    add "sdl_achv_good_RF_un" xcenter 700 ycenter 840

#Надписи концовок Ольга
screen sdl_achv_true_mt:
    add "sdl_achv_true_mt" xcenter 700 ycenter 840
screen sdl_achv_bad_mt:
    add "sdl_achv_bad_mt" xcenter 700 ycenter 840
screen sdl_achv_good_mt:
    add "sdl_achv_good_mt" xcenter 700 ycenter 840
screen sdl_achv_neutral_mt:
    add "sdl_achv_neutral_mt" xcenter 700 ycenter 840

#Надписи концовок Одиночка
screen sdl_achv_pst_me:
    add "sdl_achv_pst_me" xcenter 700 ycenter 840
screen sdl_achv_qte_me:
    add "sdl_achv_qte_me" xcenter 700 ycenter 840
screen sdl_achv_kat_me:
    add "sdl_achv_kat_me" xcenter 700 ycenter 840

#Надписи концовок Уля
screen sdl_achv_good_us_px:
    add "sdl_achv_good_us_px" xcenter 700 ycenter 840
screen sdl_achv_true_us_px:
    add "sdl_achv_true_us_px" xcenter 700 ycenter 840
screen sdl_achv_bad_us_7dl:
    add "sdl_achv_bad_us_7dl" xcenter 700 ycenter 840
screen sdl_achv_good_us_7dl:
    add "sdl_achv_good_us_7dl" xcenter 700 ycenter 840
screen sdl_achv_true_us_7dl:
    add "sdl_achv_true_us_7dl" xcenter 700 ycenter 840
screen sdl_achv_us_un:
    add "sdl_achv_us_un" xcenter 700 ycenter 840
screen sdl_achv_us_mi:
    add "sdl_achv_us_mi" xcenter 700 ycenter 840


#Переход на концовки
screen sdl_achv_jumpchkA:
    add "sdl_achv_jumpchkA" xcenter 700 ycenter 840
screen sdl_achv_infochkD:
    add "sdl_achv_infochkD" xcenter 750 ycenter 750
screen sdl_achv_infochkAD:
    add "sdl_achv_infochkAD" xcenter 750 ycenter 760

screen sdl_achvlist_Author:
    tag menu
    modal True
    imagemap:
        ground "intro_transparent"
        hotspot ((0, 0, 550, 340)): #Мику
            hover_sound sdl_achv_pagina
            hovered [Show("mi_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mi_button_active", transition=Dissolve(0.5))]
            action [Hide("mi_button_active", transition=Dissolve(0.5)), Jump("sdl_achvlist_mi_Author")]
        hotspot ((0, 344, 360, 390)): #Алисхен
            hover_sound sdl_achv_pagina
            hovered [Show("dv_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("dv_button_active", transition=Dissolve(0.5))]
            action [Hide("dv_button_active", transition=Dissolve(0.5)), Jump("sdl_achvlist_dv_Author")]
        hotspot ((0, 734, 550, 345)): #Славя
            hover_sound sdl_achv_pagina
            hovered [Show("sl_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("sl_button_active", transition=Dissolve(0.5))]
            action [Hide("sl_button_active", transition=Dissolve(0.5)), Jump("sdl_achvlist_sl_Author")]
        hotspot ((1380, 0, 600, 340)): #Лена
            hover_sound sdl_achv_pagina
            hovered [Show("un_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("un_button_active", transition=Dissolve(0.5))]
            action [Hide("un_button_active", transition=Dissolve(0.5)), Jump("sdl_achvlist_un_Author")]
        hotspot ((1560, 343, 360, 185)): #Ольга
            hover_sound sdl_achv_pagina
            hovered [Show("mt_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mt_button_active", transition=Dissolve(0.5))]
            action [Hide("mt_button_active", transition=Dissolve(0.5)), Jump("sdl_achvlist_mt_Author")]
        hotspot ((1561, 530, 359, 202)): #Ульяна
            hover_sound sdl_achv_pagina
            hovered [Show("us_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("us_button_active", transition=Dissolve(0.5))]
            action [Hide("us_button_active", transition=Dissolve(0.5)), Jump("sdl_achvlist_us_Author")]
        hotspot ((1380, 735, 600, 345)): #Одиночка
            hover_sound sdl_achv_pagina
            hovered [Show("me_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("me_button_active", transition=Dissolve(0.5))]
            action [Hide("me_button_active", transition=Dissolve(0.5)), Jump("sdl_achvlist_me_Author")]
        hotspot ((380, 350, 170, 50)): #Выход
            hover_sound sdl_achv_click
            hovered [Show("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            action [Hide("sdl_logo_active", transition=Dissolve(0.5)),Stop ("ambience"), Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Jump("choose_waifu_7dl")]
# ------------------------------------------------
##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\БЛОК МИКУ\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Mikus Erreichunge
label sdl_achvlist_mi_Author:
    scene bg sdl_ach_inactive_mi
    with dissolve
    show sdl_logo_inactive: #7DL logo
        pos (980, 18)
    show sdl_mi_cl_inactive: #Klassishe logo
        pos (1110, 18)
    show sdl_mi_dj_inactive: #Speziell logo
        pos (1215, 18)
    show sdl_achv_extB_7dl: #Иконка Ausgang
        pos(380, 350)
    call screen sdl_achvlist_mi_Author
    screen sdl_achvlist_mi_Author:
        tag menu
        modal True
        imagemap:
            ground "intro_transparent"
            hotspot ((980, 18, 113,65)): #7DL Route
                hover_sound sdl_achv_click
                hovered [Show("sdl_achv_7dl_route", transition=Dissolve(1.0)), Show("sdl_logo_active", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_achv_mi_7dlA", transition=Dissolve(0.5))]
                unhovered [Hide("sdl_achv_7dl_route", transition=Dissolve(1.0)), Hide ("sdl_logo_active", transition=Dissolve(1.0)), Show ("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_mi_7dlA", transition=Dissolve(0.5))]
                action [Hide("sdl_achv_7dl_route", transition=Dissolve(1.0)), Show("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Show("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_mi7dl_Author")]
            hotspot ((1110,18, 113,65)): #Klassishe Route
                hover_sound sdl_achv_click
                hovered [Show("sdl_achv_clt_route", transition=Dissolve(1.0)), Show("sdl_mi_cl_active", transition=Dissolve(1.0)), Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Show("sdl_achv_mi_cltA", transition=Dissolve(0.5)), Show("sdl_achv_need_routeA", transition=Dissolve(0.5))]
                unhovered [Hide("sdl_achv_clt_route", transition=Dissolve(1.0)), Hide ("sdl_mi_cl_active", transition=Dissolve(1.0)), Show ("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_mi_cltA", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5))]
                action [Hide("sdl_achv_clt_route", transition=Dissolve(1.0)), Show("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Show("sdl_achv_need_routeA", transition=Dissolve(0.5)), Jump("sdl_achvlist_miclt_Author")]
            hotspot ((1215, 18, 113,65)): #Speziell Route
                hover_sound sdl_achv_click
                hovered [Show("sdl_achv_xxx_route", transition=Dissolve(1.0)), Show("sdl_mi_dj_active", transition=Dissolve(1.0)), Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Show("sdl_achv_mi_djtA", transition=Dissolve(0.5))]
                unhovered [Hide("sdl_achv_xxx_route", transition=Dissolve(1.0)), Hide ("sdl_mi_dj_active", transition=Dissolve(1.0)), Show ("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_mi_djtA", transition=Dissolve(0.5))]
                action [Hide("sdl_achv_xxx_route", transition=Dissolve(1.0)), Show("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_midjt_Author")]

            hotspot ((0, 344, 360, 390)): #Алисхен
                hover_sound sdl_achv_pagina
                hovered [Show("dv_button_active", transition=Dissolve(0.5))]
                unhovered [Hide("dv_button_active", transition=Dissolve(0.5))]
                action [Hide("dv_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_dv_Author")]
            hotspot ((0, 734, 550, 345)): #Славя
                hover_sound sdl_achv_pagina
                hovered [Show("sl_button_active", transition=Dissolve(0.5))]
                unhovered [Hide("sl_button_active", transition=Dissolve(0.5))]
                action [Hide("sl_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)),Jump("sdl_achvlist_sl_Author")]
            hotspot ((1380, 0, 600, 340)): #Лена
                hover_sound sdl_achv_pagina
                hovered [Show("un_button_active", transition=Dissolve(0.5))]
                unhovered [Hide("un_button_active", transition=Dissolve(0.5))]
                action [Hide("un_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_un_Author")]
            hotspot ((1560, 343, 360, 185)): #Ольга
                hover_sound sdl_achv_pagina
                hovered [Show("mt_button_active", transition=Dissolve(0.5))]
                unhovered [Hide("mt_button_active", transition=Dissolve(0.5))]
                action [Hide("mt_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_mt_Author")]
            hotspot ((1561, 530, 359, 202)): #Ульяна
                hover_sound sdl_achv_pagina
                hovered [Show("us_button_active", transition=Dissolve(0.5))]
                unhovered [Hide("us_button_active", transition=Dissolve(0.5))]
                action [Hide("us_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_us_Author")]
            hotspot ((1380, 735, 600, 345)): #Одиночка
                hover_sound sdl_achv_pagina
                hovered [Show("me_button_active", transition=Dissolve(0.5))]
                unhovered [Hide("me_button_active", transition=Dissolve(0.5))]
                action [Hide("me_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_me_Author")]
            hotspot ((380, 350, 170, 50)): #Выход
                hover_sound sdl_achv_click
                hovered [Show("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
                unhovered [Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
                action [Hide("sdl_logo_active", transition=Dissolve(0.5)),Stop ("ambience"),Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Jump("choose_waifu_7dl")]
# ------------------------------------------------
######################МИКУ-7ДЛ######################################
label sdl_achvlist_mi7dl_Author:
    scene bg sdl_ach_inactive_mi
    with dissolve
    show sdl_achv_delB_7dl: #Иконка удалятора
        pos (380, 680)
    show sdl_achv_extB_7dl: #Иконка Ausgang
        pos(380, 350)
    #ТруЪ-энд
    if persistent.mi_7dl_true:
        show acm_logo_mi_thank_you  with dissolve:
            xcenter 800 ycenter 66
        show de_check_inactive1 with dissolve:
            pos (590, 40)
    else:
        show de_achiv_lock1 with dissolve:
            xcenter 800 ycenter 66
    if not (persistent.mi_7dl_herc_exc or persistent.mi_7dl_loki_exc or persistent.mi_7dl_dr_exc):
        show de_info_inactive1 with dissolve:
            pos (590, 40)
    else:
        pass
    #Гуд-M
    if persistent.mi_7dl_good_human:
        show acm_logo_mi_dark_dreams  with dissolve:
            xcenter 800 ycenter 130
        show de_check_inactive2 with dissolve:
            pos (590, 104)
    else:
        show de_achiv_lock2 with dissolve:
            xcenter 800 ycenter 130
    #Гуд-S
    if persistent.mi_7dl_good_star:
        show acm_logo_mi_sparkle  with dissolve:
            xcenter 800 ycenter 194
        show de_check_inactive3 with dissolve:
            pos (590, 168)
    else:
        show de_achiv_lock3 with dissolve:
            xcenter 800 ycenter 194
    #Эксклюзив-Дрищ
    if persistent.mi_7dl_dr_exc:
        show acm_logo_mi_watashi  with dissolve:
            xcenter 800 ycenter 258
        show de_check_inactive4 with dissolve:
            pos (590, 232)
    else:
        show de_achiv_lock4 with dissolve:
            xcenter 800 ycenter 258
    if not (persistent.mi_7dl_good_human or persistent.mi_7dl_good_star):
        show de_info_inactive4 with dissolve:
            pos (590, 232)
    else:
        pass
    #Эксклюзив-Локи
    if persistent.mi_7dl_loki_exc:
        show acm_logo_mi_come  with dissolve:
            xcenter 800 ycenter 322
        show de_check_inactive5 with dissolve:
            pos (590, 296)
    else:
        show de_achiv_lock5 with dissolve:
            xcenter 800 ycenter 322
    if not (persistent.mi_7dl_good_human or persistent.mi_7dl_good_star):
        show de_info_inactive5 with dissolve:
            pos (590, 296)
    else:
        pass
    #Эксклюзив-Герк
    if persistent.mi_7dl_herc_exc:
        show acm_logo_mi_unlike  with dissolve:
            xcenter 800 ycenter 386
        show de_check_inactive6 with dissolve:
            pos (590, 360)
    else:
        show de_achiv_lock6 with dissolve:
            xcenter 800 ycenter 386
    if not (persistent.mi_7dl_good_human or persistent.mi_7dl_good_star):
        show de_info_inactive6 with dissolve:
            pos (590, 360)
    else:
        pass
    #Нейтрал-M
    if persistent.mi_7dl_neutral_human:
        show acm_logo_mi_happy_again  with dissolve:
            xcenter 800 ycenter 450
        show de_check_inactive7 with dissolve:
            pos (590, 424)
    else:
        show de_achiv_lock7 with dissolve:
            xcenter 800 ycenter 450
    #Нейтрал-S
    if persistent.mi_7dl_neutral_star:
        show acm_logo_mi_club27  with dissolve:
            xcenter 800 ycenter 514
        show de_check_inactive8 with dissolve:
            pos (590, 488)
    else:
        show de_achiv_lock8 with dissolve:
            xcenter 800 ycenter 514
    #Бэд-M
    if persistent.mi_7dl_bad_human:
        show acm_logo_mi_liar  with dissolve:
            xcenter 800 ycenter 578
        show de_check_inactive9 with dissolve:
            pos (590, 552)
    else:
        show de_achiv_lock9 with dissolve:
            xcenter 800 ycenter 578
    #Бэд-S
    if persistent.mi_7dl_bad_star:
        show acm_logo_mi_dam_cpu  with dissolve:
            xcenter 800 ycenter 642
        show de_check_inactive10 with dissolve:
            pos (590, 616)
    else:
        show de_achiv_lock10 with dissolve:
            xcenter 800 ycenter 642
    call screen sdl_achvlist_mi7dl_Author
# ------------------------------------------------
screen sdl_achvlist_mi7dl_Author:
    tag menu
    modal True
    imagemap:
        ground "intro_transparent"
        hotspot ((1110,18, 113,65)): #Klassishe Route
            hover_sound sdl_achv_click
            hovered [Show("sdl_mi_cl_active", transition=Dissolve(1.0)), Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Show("sdl_achv_mi_cltA", transition=Dissolve(0.5)), Hide("sdl_achv_mi_7dlA", transition=Dissolve(0.5)), Show("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_mi_cl_active", transition=Dissolve(1.0)), Show ("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_mi_cltA", transition=Dissolve(0.5)), Show("sdl_achv_mi_7dlA", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_mi_7dlA", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Show("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Show("sdl_mi_cl_active", transition=Dissolve(0.5)), Show("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_miclt_Author")]
        hotspot ((1215, 18, 113,65)): #Speziell Route
            hover_sound sdl_achv_click
            hovered [Show("sdl_mi_dj_active", transition=Dissolve(1.0)), Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Show("sdl_achv_mi_djtA", transition=Dissolve(0.5)), Hide("sdl_achv_mi_7dlA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_mi_dj_active", transition=Dissolve(1.0)), Show ("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_mi_djtA", transition=Dissolve(0.5)), Show("sdl_achv_mi_7dlA", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_mi_7dlA", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(1.0)), Show("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Show("sdl_mi_dj_active", transition=Dissolve(0.5)), Show("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_midjt_Author")]
        hotspot ((650,40, 300, 52)): #ТруЪ-энд
            hovered [Show("sdl_achv_true_mi", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_true_mi", transition=Dissolve(0.5))]
            action [Show("sdl_achv_true_mi", transition=Dissolve(0.5))]
        if persistent.mi_7dl_true:
            hotspot ((590, 40, 50, 52)): #Wahr-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active1", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active1", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)),  Hide("de_check_active1", transition=Dissolve(0.5)),Jump("alt_achvA_mi7dl_true")]
        elif not (persistent.mi_7dl_herc_exc or persistent.mi_7dl_loki_exc or persistent.mi_7dl_dr_exc):
            hotspot ((590, 40, 50, 50)): #Ende-Info
                hover_sound sdl_achv_info
                hovered [Show ("de_info_active1", transition=Dissolve(0.5)), Show ("sdl_achv_infochkD", transition=Dissolve(0.5)), Show ("acm_logo_mi_watashi", transition=Dissolve(0.5))]
                unhovered [Hide ("de_info_active1", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_mi_watashi", transition=Dissolve(0.5))]
                action [Hide("de_info_active1", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_mi_watashi", transition=Dissolve(0.5))]
        hotspot ((650,104, 300, 52)): #Гуд-M
            hovered [Show("sdl_achv_good_mi", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_good_mi", transition=Dissolve(0.5))]
            action [Show("sdl_achv_good_mi", transition=Dissolve(0.5))]
        if persistent.mi_7dl_good_human:
            hotspot ((590, 104, 50, 52)): #Gut-M-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active2", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active2", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)),  Hide("de_check_active2", transition=Dissolve(0.5)),Jump("alt_day7_mi_7dl_dark_dreams")]
        hotspot ((650,168, 300, 52)): #Гуд-S
            hovered [Show("sdl_achv_good_RF_mi", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_good_RF_mi", transition=Dissolve(0.5))]
            action [Show("sdl_achv_good_RF_mi", transition=Dissolve(0.5))]
        if persistent.mi_7dl_good_star:
            hotspot ((590, 168, 50, 52)): #RF-Gut-S-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active3", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active3", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)),  Hide("de_check_active3", transition=Dissolve(0.5)),Jump("alt_day7_mi_7dl_sparkle")]
        hotspot ((650,232, 300, 52)): #Эксклюзив-Дрищ
            hovered [Show("sdl_achv_excl_DR_mi", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_excl_DR_mi", transition=Dissolve(0.5))]
            action [Show("sdl_achv_excl_DR_mi", transition=Dissolve(0.5))]
        if persistent.mi_7dl_dr_exc:
            hotspot ((590, 232, 50, 52)): #Speziel-DR-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active4", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active4", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)),  Hide("de_check_active4", transition=Dissolve(0.5)),Jump("alt_day7_mi_7dl_come_back")]
        elif not (persistent.mi_7dl_good_human or persistent.mi_7dl_good_star):
            hotspot ((590, 232,50, 50)): #Ende-Info
                hover_sound sdl_achv_info
                hovered [Show ("de_info_active4", transition=Dissolve(0.5)), Show ("sdl_achv_infochkD", transition=Dissolve(0.5)), Show ("acm_logo_mi_sparkle", transition=Dissolve(0.5))]
                unhovered [Hide ("de_info_active4", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_mi_sparkle", transition=Dissolve(0.5))]
                action [Hide("de_info_active4", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_mi_sparkle", transition=Dissolve(0.5))]
        hotspot ((650,296, 300, 52)): #Эксклюзив-Локи
            hovered [Show("sdl_achv_excl_LO_mi", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_excl_LO_mi", transition=Dissolve(0.5))]
            action [Show("sdl_achv_excl_LO_mi", transition=Dissolve(0.5))]
        if persistent.mi_7dl_loki_exc:
            hotspot ((590, 296, 50, 52)): #Speziel-LK-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active5", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active5", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)),  Hide("de_check_active5", transition=Dissolve(0.5)),Jump("alt_day7_mi_7dl_sinthetic")]
        elif not (persistent.mi_7dl_good_human or persistent.mi_7dl_good_star):
            hotspot ((590, 296,50, 50)): #Ende-Info
                hover_sound sdl_achv_info
                hovered [Show ("de_info_active5", transition=Dissolve(0.5)), Show ("sdl_achv_infochkD", transition=Dissolve(0.5)), Show ("acm_logo_mi_sparkle", transition=Dissolve(0.5))]
                unhovered [Hide ("de_info_active5", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_mi_sparkle", transition=Dissolve(0.5))]
                action [Hide("de_info_active5", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_mi_sparkle", transition=Dissolve(0.5))]
        hotspot ((650,360, 300, 52)): #Эксклюзив-Герк
            hovered [Show("sdl_achv_excl_HE_mi", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_excl_HE_mi", transition=Dissolve(0.5))]
            action [Show("sdl_achv_excl_HE_mi", transition=Dissolve(0.5))]
        if persistent.mi_7dl_herc_exc:
            hotspot ((590, 360, 50, 52)): #Speziel-HR-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active6", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active6", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)),  Hide("de_check_active6", transition=Dissolve(0.5)),Jump("alt_day7_mi_7dl_unlike")]
        elif not (persistent.mi_7dl_good_human or persistent.mi_7dl_good_star):
            hotspot ((590, 360,50, 50)): #Ende-Info
                hover_sound sdl_achv_info
                hovered [Show ("de_info_active6", transition=Dissolve(0.5)), Show ("sdl_achv_infochkD", transition=Dissolve(0.5)), Show ("acm_logo_mi_sparkle", transition=Dissolve(0.5))]
                unhovered [Hide ("de_info_active6", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_mi_sparkle", transition=Dissolve(0.5))]
                action [Hide("de_info_active6", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_mi_sparkle", transition=Dissolve(0.5))]
        hotspot ((650,424, 300, 52)): #Нейтрал-M
            hovered [Show("sdl_achv_neutral_mi", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_neutral_mi", transition=Dissolve(0.5))]
            action [Show("sdl_achv_neutral_mi", transition=Dissolve(0.5))]
        if persistent.mi_7dl_neutral_human:
            hotspot ((590, 424, 50, 52)): #Neutral-M-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active7", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active7", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)),Stop ("ambience"),  Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)),  Hide("de_check_active7", transition=Dissolve(0.5)),Jump("alt_day7_mi_7dl_happy_again")]
        hotspot ((650,488, 300, 52)): #Нейтрал-S
            hovered [Show("sdl_achv_neutral_mi", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_neutral_mi", transition=Dissolve(0.5))]
            action [Show("sdl_achv_neutral_mi", transition=Dissolve(0.5))]
        if persistent.mi_7dl_neutral_star:
            hotspot ((590, 488, 50, 52)): #Neutral-S-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active8", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active8", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)),  Hide("de_check_active8", transition=Dissolve(0.5)),Jump("alt_day7_mi_7dl_club27")]
        hotspot ((650,552, 300, 52)): #Бэд-M
            hovered [Show("sdl_achv_bad_mi", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_bad_mi", transition=Dissolve(0.5))]
            action [Show("sdl_achv_bad_mi", transition=Dissolve(0.5))]
        if persistent.mi_7dl_bad_human:
            hotspot ((590, 552, 50, 52)): #schlecht-M-Ende-Jump
                hovered [Show ("de_check_active9", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active9", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)),  Hide("de_check_active9", transition=Dissolve(0.5)),Jump("alt_day7_mi_7dl_liar")]
        hotspot ((650,616, 300, 52)): #Бэд-S
            hovered [Show("sdl_achv_bad_mi", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_bad_mi", transition=Dissolve(0.5))]
            action [Show("sdl_achv_bad_mi", transition=Dissolve(0.5))]
        if persistent.mi_7dl_bad_star:
            hotspot ((590, 616, 50, 52)): #schlecht-S-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active10", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active10", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)),  Hide("de_check_active10", transition=Dissolve(0.5)),Jump("alt_day7_mi_7dl_dam_CPU")]

        hotspot ((0, 344, 360, 390)): #Алисхен
            hover_sound sdl_achv_pagina
            hovered [Show("dv_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("dv_button_active", transition=Dissolve(0.5))]
            action [Hide("dv_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Jump("sdl_achvlist_dv_Author")]
        hotspot ((0, 734, 550, 345)): #Славя
            hover_sound sdl_achv_pagina
            hovered [Show("sl_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("sl_button_active", transition=Dissolve(0.5))]
            action [Hide("sl_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Jump("sdl_achvlist_sl_Author")]
        hotspot ((1380, 0, 600, 340)): #Лена
            hover_sound sdl_achv_pagina
            hovered [Show("un_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("un_button_active", transition=Dissolve(0.5))]
            action [Hide("un_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Jump("sdl_achvlist_un_Author")]
        hotspot ((1560, 343, 360, 185)): #Ольга
            hover_sound sdl_achv_pagina
            hovered [Show("mt_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mt_button_active", transition=Dissolve(0.5))]
            action [Hide("mt_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Jump("sdl_achvlist_mt_Author")]
        hotspot ((1561, 530, 359, 202)): #Ульяна
            hover_sound sdl_achv_pagina
            hovered [Show("us_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("us_button_active", transition=Dissolve(0.5))]
            action [Hide("us_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Jump("sdl_achvlist_us_Author")]
        hotspot ((1380, 735, 600, 345)): #Одиночка
            hover_sound sdl_achv_pagina
            hovered [Show("me_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("me_button_active", transition=Dissolve(0.5))]
            action [Hide("me_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Jump("sdl_achvlist_me_Author")]

        hotspot ((380, 350, 170, 50)): #Выход
            hover_sound sdl_achv_click
            hovered [Show("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            action [Hide("sdl_logo_active", transition=Dissolve(0.5)),Stop ("ambience"), Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Jump("choose_waifu_7dl")]
        hotspot ((380, 680, 170, 50)): #Удалятор
            hover_sound sdl_achv_click
            activate_sound sdl_achv_clear
            hovered [Show("sdl_achv_delA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5))]
            action Jump("sdl_achvlist_mi7dl_clear_Author")
# ------------------------------------------------
######################МИКУ-КЛАССИК######################################
label sdl_achvlist_miclt_Author:
    scene bg sdl_ach_inactive_mi
    with dissolve
    show sdl_achv_delB_7dl: #Иконка удалятора
        pos (380, 680)
    show sdl_achv_extB_7dl: #Иконка Ausgang
        pos(380, 350)
    call screen sdl_achvlist_miclt_Author
# ------------------------------------------------
screen sdl_achvlist_miclt_Author:
    tag menu
    modal True
    imagemap:
        ground "intro_transparent"
        hotspot ((980, 18, 113,65)): #7DL Route
            hover_sound sdl_achv_click
            hovered [Show("sdl_logo_active", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_achv_mi_7dlA", transition=Dissolve(0.5)), Hide("sdl_achv_mi_cltA", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_logo_active", transition=Dissolve(1.0)), Show ("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_mi_7dlA", transition=Dissolve(0.5)), Show("sdl_achv_mi_cltA", transition=Dissolve(0.5)), Show("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_mi_cltA", transition=Dissolve(0.5)), Show("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Hide ("sdl_mi_cl_active", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_logo_active", transition=Dissolve(0.5)), Show("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_mi7dl_Author")]
        hotspot ((1215, 18, 113,65)): #Speziell Route
            hover_sound sdl_achv_click
            hovered [Show("sdl_mi_dj_active", transition=Dissolve(1.0)), Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Show("sdl_achv_mi_djtA", transition=Dissolve(0.5)), Hide("sdl_achv_mi_cltA", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_mi_dj_active", transition=Dissolve(1.0)), Show ("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_mi_djtA", transition=Dissolve(0.5)), Show("sdl_achv_mi_cltA", transition=Dissolve(0.5)), Show("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_mi_cltA", transition=Dissolve(0.5)), Show("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Hide ("sdl_mi_cl_active", transition=Dissolve(1.0)), Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Show("sdl_mi_dj_active", transition=Dissolve(0.5)), Show("sdl_logo_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_midjt_Author")]

        hotspot ((0, 344, 360, 390)): #Алисхен
            hover_sound sdl_achv_pagina
            hovered [Show("dv_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("dv_button_active", transition=Dissolve(0.5))]
            action [Hide("dv_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_cl_active", transition=Dissolve(0.5)),Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_mi_cltA", transition=Dissolve(1.0)), Jump("sdl_achvlist_dv_Author")]
        hotspot ((0, 734, 550, 345)): #Славя
            hover_sound sdl_achv_pagina
            hovered [Show("sl_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("sl_button_active", transition=Dissolve(0.5))]
            action [Hide("sl_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_cl_active", transition=Dissolve(0.5)),Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_mi_cltA", transition=Dissolve(1.0)), Jump("sdl_achvlist_sl_Author")]
        hotspot ((1380, 0, 600, 340)): #Лена
            hover_sound sdl_achv_pagina
            hovered [Show("un_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("un_button_active", transition=Dissolve(0.5))]
            action [Hide("un_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_cl_active", transition=Dissolve(0.5)),Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_mi_cltA", transition=Dissolve(1.0)), Jump("sdl_achvlist_un_Author")]
        hotspot ((1560, 343, 360, 185)): #Ольга
            hover_sound sdl_achv_pagina
            hovered [Show("mt_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mt_button_active", transition=Dissolve(0.5))]
            action [Hide("mt_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_cl_active", transition=Dissolve(0.5)),Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_mi_cltA", transition=Dissolve(1.0)), Jump("sdl_achvlist_mt_Author")]
        hotspot ((1561, 530, 359, 202)): #Ульяна
            hover_sound sdl_achv_pagina
            hovered [Show("us_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("us_button_active", transition=Dissolve(0.5))]
            action [Hide("us_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_cl_active", transition=Dissolve(0.5)),Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_mi_cltA", transition=Dissolve(1.0)), Jump("sdl_achvlist_us_Author")]
        hotspot ((1380, 735, 600, 345)): #Одиночка
            hover_sound sdl_achv_pagina
            hovered [Show("me_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("me_button_active", transition=Dissolve(0.5))]
            action [Hide("me_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_cl_active", transition=Dissolve(0.5)),Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_mi_cltA", transition=Dissolve(1.0)), Jump("sdl_achvlist_me_Author")]

        hotspot ((380, 350, 170, 50)): #Выход
            hover_sound sdl_achv_click
            hovered [Show("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Stop ("ambience"), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_cl_active", transition=Dissolve(0.5)),Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_mi_cltA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Jump("choose_waifu_7dl")]
        hotspot ((380, 680, 170, 50)): #Удалятор
            hover_sound sdl_achv_click
            activate_sound sdl_achv_clear
            hovered [Show("sdl_achv_delA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5))]
            action Jump("sdl_achvlist_miclt_clear_Author")
# ------------------------------------------------
######################МИКУ-ДИДЖЕЙ######################################
label sdl_achvlist_midjt_Author:
    scene bg sdl_ach_inactive_mi
    with dissolve
    show sdl_achv_delB_7dl: #Иконка удалятора
        pos (380, 680)
    show sdl_achv_extB_7dl: #Иконка Ausgang
        pos(380, 350)
    #ТруЪ-энд
    if persistent.mi_dj_true:
        show acm_logo_mi_namiki  with dissolve:
            xcenter 800 ycenter 66
        show de_check_inactive1 with dissolve:
            pos (590, 40)
    else:
        show de_achiv_lock1 with dissolve:
            xcenter 800 ycenter 66
    #Гуд-Япония
    if persistent.mi_dj_good_jap:
        show acm_logo_mi_ricochet  with dissolve:
            xcenter 800 ycenter 130
        show de_check_inactive2 with dissolve:
            pos (590, 104)
    else:
        show de_achiv_lock2 with dissolve:
            xcenter 800 ycenter 130
    #Гуд-РФ
    if persistent.mi_dj_good_rf:
        show acm_logo_mi_allyours  with dissolve:
            xcenter 800 ycenter 194
        show de_check_inactive3 with dissolve:
            pos (590, 168)
    else:
        show de_achiv_lock3 with dissolve:
            xcenter 800 ycenter 194
    #Бэд
    if persistent.mi_dj_bad:
        show acm_logo_mi_new_happy  with dissolve:
            xcenter 800 ycenter 258
        show de_check_inactive4 with dissolve:
            pos (590, 232)
    else:
        show de_achiv_lock4 with dissolve:
            xcenter 800 ycenter 258
    call screen sdl_achvlist_midjt_Author
# ------------------------------------------------
screen sdl_achvlist_midjt_Author:
    tag menu
    modal True
    imagemap:
        ground "intro_transparent"
        hotspot ((980, 18, 113,65)): #7DL Route
            hover_sound sdl_achv_click
            hovered [Show("sdl_logo_active", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_achv_mi_7dlA", transition=Dissolve(0.5)), Hide("sdl_achv_mi_djtA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_logo_active", transition=Dissolve(1.0)), Show ("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_mi_7dlA", transition=Dissolve(0.5)), Show("sdl_achv_mi_djtA", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_mi_djtA", transition=Dissolve(0.5)), Show("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide ("sdl_mi_dj_active", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_logo_active", transition=Dissolve(0.5)), Show("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_mi7dl_Author")]
        hotspot ((1110,18, 113,65)): #Klassishe Route
            hover_sound sdl_achv_click
            hovered [Show("sdl_mi_cl_active", transition=Dissolve(1.0)), Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Show("sdl_achv_mi_cltA", transition=Dissolve(0.5)), Hide("sdl_achv_mi_djtA", transition=Dissolve(0.5)), Show("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_mi_cl_active", transition=Dissolve(1.0)), Show ("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_mi_cltA", transition=Dissolve(0.5)), Show("sdl_achv_mi_djtA", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_mi_djtA", transition=Dissolve(0.5)), Show("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_mi_dj_active", transition=Dissolve(0.5)), Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Show("sdl_mi_cl_active", transition=Dissolve(1.0)),Show("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_miclt_Author")]
        hotspot ((650,40, 300, 52)): #ТруЪ-энд
            hovered [Show("sdl_achv_true_mi", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_true_mi", transition=Dissolve(0.5))]
            action [Show("sdl_achv_true_mi", transition=Dissolve(0.5))]
        if persistent.mi_dj_true:
            hotspot ((590, 40, 50, 52)): #Wahr-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active1", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active1", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_mi_djtA", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_mi_dj_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)),  Hide("de_check_active1", transition=Dissolve(0.5)),Jump("alt_day7_mi_dj_true_end")]
        hotspot ((650,104, 300, 52)): #Гуд-Япония
            hovered [Show("sdl_achv_good_mi", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_good_mi", transition=Dissolve(0.5))]
            action [Show("sdl_achv_good_mi", transition=Dissolve(0.5))]
        if persistent.mi_dj_good_jap:
            hotspot ((590, 104, 50, 52)): #Gut-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active2", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active2", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_mi_djtA", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_mi_dj_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)),  Hide("de_check_active2", transition=Dissolve(0.5)),Jump("alt_day7_mi_dj_jp_good_end")]
        hotspot ((650,168, 300, 52)): #Гуд-РФ
            hovered [Show("sdl_achv_good_RF_mi", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_good_RF_mi", transition=Dissolve(0.5))]
            action [Show("sdl_achv_good_RF_mi", transition=Dissolve(0.5))]
        if persistent.mi_dj_good_rf:
            hotspot ((590, 168, 50, 52)): #RF-Gut-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active3", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active3", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_mi_djtA", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_mi_dj_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active3", transition=Dissolve(0.5)),Jump("alt_day7_mi_dj_rf_good_end")]
        hotspot ((650,232, 300, 52)): #Бэд
            hovered [Show("sdl_achv_bad_mi", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_bad_mi", transition=Dissolve(0.5))]
            action [Show("sdl_achv_bad_mi", transition=Dissolve(0.5))]
        if persistent.mi_dj_bad:
            hotspot ((590, 232, 50, 52)): #schlecht-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active4", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active4", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_mi_djtA", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_mi_dj_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active4", transition=Dissolve(0.5)),Jump("alt_day7_mi_dj_bad_end")]

        hotspot ((0, 344, 360, 390)): #Алисхен
            hover_sound sdl_achv_pagina
            hovered [Show("dv_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("dv_button_active", transition=Dissolve(0.5))]
            action [Hide("dv_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_dj_active", transition=Dissolve(0.5)), Hide("sdl_achv_mi_djtA", transition=Dissolve(1.0)), Jump("sdl_achvlist_dv_Author")]
        hotspot ((0, 734, 550, 345)): #Славя
            hover_sound sdl_achv_pagina
            hovered [Show("sl_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("sl_button_active", transition=Dissolve(0.5))]
            action [Hide("sl_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_dj_active", transition=Dissolve(0.5)), Hide("sdl_achv_mi_djtA", transition=Dissolve(1.0)), Jump("sdl_achvlist_sl_Author")]
        hotspot ((1380, 0, 600, 340)): #Лена
            hover_sound sdl_achv_pagina
            hovered [Show("un_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("un_button_active", transition=Dissolve(0.5))]
            action [Hide("un_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_dj_active", transition=Dissolve(0.5)), Hide("sdl_achv_mi_djtA", transition=Dissolve(1.0)), Jump("sdl_achvlist_un_Author")]
        hotspot ((1560, 343, 360, 185)): #Ольга
            hover_sound sdl_achv_pagina
            hovered [Show("mt_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mt_button_active", transition=Dissolve(0.5))]
            action [Hide("mt_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_dj_active", transition=Dissolve(0.5)), Hide("sdl_achv_mi_djtA", transition=Dissolve(1.0)), Jump("sdl_achvlist_mt_Author")]
        hotspot ((1561, 530, 359, 202)): #Ульяна
            hover_sound sdl_achv_pagina
            hovered [Show("us_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("us_button_active", transition=Dissolve(0.5))]
            action [Hide("us_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_dj_active", transition=Dissolve(0.5)), Hide("sdl_achv_mi_djtA", transition=Dissolve(1.0)), Jump("sdl_achvlist_us_Author")]
        hotspot ((1380, 735, 600, 345)): #Одиночка
            hover_sound sdl_achv_pagina
            hovered [Show("me_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("me_button_active", transition=Dissolve(0.5))]
            action [Hide("me_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_dj_active", transition=Dissolve(0.5)), Hide("sdl_achv_mi_djtA", transition=Dissolve(1.0)), Jump("sdl_achvlist_me_Author")]

        hotspot ((380, 350, 170, 50)): #Выход
            hover_sound sdl_achv_click
            hovered [Show("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            action [Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Stop ("ambience"), Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_dj_active", transition=Dissolve(0.5)), Hide("sdl_achv_mi_djtA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Jump("choose_waifu_7dl")]
        hotspot ((380, 680, 170, 50)): #Удалятор
            hover_sound sdl_achv_click
            activate_sound sdl_achv_clear
            hovered [Show("sdl_achv_delA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5))]
            action Jump("sdl_achvlist_midjt_clear_Author")
# ------------------------------------------------
##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\БЛОК АЛИСЫ\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Alischens Erreichunge
label sdl_achvlist_dv_Author:
    scene bg sdl_ach_inactive_dv
    with dissolve
    show sdl_logo_inactive: #7DL logo
        pos (980, 18)
    show sdl_dv_cl_inactive: #Klassishe logo
        pos (1110, 18)
    show sdl_dv_dj_inactive: #Speziell logo
        pos (1215, 18)
    show sdl_achv_extB_7dl: #Иконка Ausgang
        pos(380, 350)
    call screen sdl_achvlist_dv_Author
    screen sdl_achvlist_dv_Author:
        tag menu
        modal True
        imagemap:
            ground "intro_transparent"
            hotspot ((980, 18, 113,65)): #7DL Route
                hover_sound sdl_achv_click
                hovered [Show("sdl_achv_7dl_route", transition=Dissolve(1.0)), Show("sdl_logo_active", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_achv_dv_7dlA", transition=Dissolve(0.5))]
                unhovered [Hide("sdl_achv_7dl_route", transition=Dissolve(1.0)), Hide ("sdl_logo_active", transition=Dissolve(1.0)), Show ("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_dv_7dlA", transition=Dissolve(0.5))]
                action [Hide("sdl_achv_7dl_route", transition=Dissolve(1.0)), Show("sdl_dv_cl_inactive", transition=Dissolve(0.5)), Show("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_dv7dl_Author")]
            hotspot ((1110,18, 113,65)): #Klassishe Route
                hover_sound sdl_achv_click
                hovered [Show("sdl_achv_clt_route", transition=Dissolve(1.0)), Show("sdl_dv_cl_active", transition=Dissolve(1.0)), Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)), Show("sdl_achv_dv_cltA", transition=Dissolve(0.5)), Show("sdl_achv_need_routeA", transition=Dissolve(0.5))]
                unhovered [Hide("sdl_achv_clt_route", transition=Dissolve(1.0)), Hide ("sdl_dv_cl_active", transition=Dissolve(1.0)), Show ("sdl_dv_cl_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_dv_cltA", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5))]
                action [Hide("sdl_achv_clt_route", transition=Dissolve(1.0)), Show("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Show("sdl_achv_need_routeA", transition=Dissolve(0.5)), Jump("sdl_achvlist_dvclt_Author")]
            hotspot ((1215, 18, 113,65)): #Speziell Route
                hover_sound sdl_achv_click
                hovered [Show("sdl_achv_xxx_route", transition=Dissolve(1.0)), Show("sdl_dv_dj_active", transition=Dissolve(1.0)), Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Show("sdl_achv_dv_djtA", transition=Dissolve(0.5)), Show("sdl_achv_need_routeA", transition=Dissolve(0.5))]
                unhovered [Hide("sdl_achv_xxx_route", transition=Dissolve(1.0)), Hide ("sdl_dv_dj_active", transition=Dissolve(1.0)), Show ("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_dv_djtA", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5))]
                action [Hide("sdl_achv_xxx_route", transition=Dissolve(1.0)), Show("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_dv_cl_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_dvdjt_Author")]

            hotspot ((0, 0, 550, 340)): #Мику
                hover_sound sdl_achv_pagina
                hovered [Show("mi_button_active", transition=Dissolve(0.5))]
                unhovered [Hide("mi_button_active", transition=Dissolve(0.5))]
                action [Hide("mi_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_mi_Author")]
            hotspot ((0, 734, 550, 345)): #Славя
                hover_sound sdl_achv_pagina
                hovered [Show("sl_button_active", transition=Dissolve(0.5))]
                unhovered [Hide("sl_button_active", transition=Dissolve(0.5))]
                action [Hide("sl_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)),Jump("sdl_achvlist_sl_Author")]
            hotspot ((1380, 0, 600, 340)): #Лена
                hover_sound sdl_achv_pagina
                hovered [Show("un_button_active", transition=Dissolve(0.5))]
                unhovered [Hide("un_button_active", transition=Dissolve(0.5))]
                action [Hide("un_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_un_Author")]
            hotspot ((1560, 343, 360, 185)): #Ольга
                hover_sound sdl_achv_pagina
                hovered [Show("mt_button_active", transition=Dissolve(0.5))]
                unhovered [Hide("mt_button_active", transition=Dissolve(0.5))]
                action [Hide("mt_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_mt_Author")]
            hotspot ((1561, 530, 359, 202)): #Ульяна
                hover_sound sdl_achv_pagina
                hovered [Show("us_button_active", transition=Dissolve(0.5))]
                unhovered [Hide("us_button_active", transition=Dissolve(0.5))]
                action [Hide("us_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_us_Author")]
            hotspot ((1380, 735, 600, 345)): #Одиночка
                hover_sound sdl_achv_pagina
                hovered [Show("me_button_active", transition=Dissolve(0.5))]
                unhovered [Hide("me_button_active", transition=Dissolve(0.5))]
                action [Hide("me_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_me_Author")]
            hotspot ((380, 350, 170, 50)): #Выход
                hover_sound sdl_achv_click
                hovered [Show("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
                unhovered [Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
                action [Hide("sdl_logo_active", transition=Dissolve(0.5)),Stop ("ambience"), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Jump("choose_waifu_7dl")]
# ------------------------------------------------
######################АЛИСА-7ДЛ######################################
label sdl_achvlist_dv7dl_Author:
    scene bg sdl_ach_inactive_dv
    with dissolve
    show sdl_achv_delB_7dl: #Иконка удалятора
        pos (380, 680)
    show sdl_achv_extB_7dl: #Иконка Ausgang
        pos(380, 350)
    #Гуд-СССР
    if persistent.dv_7dl_good_ussr:
        show acm_logo_dv_ussr_good  with dissolve:
            xcenter 800 ycenter 66
        show de_check_inactive1 with dissolve:
            pos (590, 40)
    else:
        show de_achiv_lock1 with dissolve:
            xcenter 800 ycenter 66
    #Гуд-РФ
    if persistent.dv_7dl_good_ussr_rf:
        show acm_logo_dv_morethanlife  with dissolve:
            xcenter 800 ycenter 130
        show de_check_inactive2 with dissolve:
            pos (590, 104)
    else:
        show de_achiv_lock2 with dissolve:
            xcenter 800 ycenter 130
    #Реджект-РФ
    if persistent.dv_7dl_reject_rf:
        show acm_logo_dv_gohome  with dissolve:
            xcenter 800 ycenter 194
        show de_check_inactive3 with dissolve:
            pos (590, 168)
    else:
        show de_achiv_lock3 with dissolve:
            xcenter 800 ycenter 194
    #Реджект-СССР
    if persistent.dv_7dl_reject_ussr:
        show acm_logo_dv_tillend  with dissolve:
            xcenter 800 ycenter 258
        show de_check_inactive4 with dissolve:
            pos (590, 232)
    else:
        show de_achiv_lock4 with dissolve:
            xcenter 800 ycenter 258
    #Транзит-Ольга
    if persistent.dv_7dl_bad_mt:
        show acm_logo_dv_drunk  with dissolve:
            xcenter 800 ycenter 322
        show de_check_inactive5 with dissolve:
            pos (590, 296)
    else:
        show de_achiv_lock5 with dissolve:
            xcenter 800 ycenter 322
    #Транзит-Лена
    if persistent.dv_7dl_un:
        show acm_logo_dv_meetmethere  with dissolve:
            xcenter 800 ycenter 386
        show de_check_inactive6 with dissolve:
            pos (590, 360)
    else:
        show de_achiv_lock6 with dissolve:
            xcenter 800 ycenter 386
    #Эксклюзив-Локи
    if persistent.dv_7dl_tulpa:
        show acm_logo_dv_tulpa  with dissolve:
            xcenter 800 ycenter 450
        show de_check_inactive7 with dissolve:
            pos (590, 424)
    else:
        show de_achiv_lock7 with dissolve:
            xcenter 800 ycenter 450
    #Бэд
    if persistent.dv_7dl_bad:
        show acm_logo_dv_theresnoway  with dissolve:
            xcenter 800 ycenter 514
        show de_check_inactive8 with dissolve:
            pos (590, 488)
    else:
        show de_achiv_lock8 with dissolve:
            xcenter 800 ycenter 514
    call screen sdl_achvlist_dv7dl_Author
# ------------------------------------------------
screen sdl_achvlist_dv7dl_Author:
    tag menu
    modal True
    imagemap:
        ground "intro_transparent"
        hotspot ((1110,18, 113,65)): #Klassishe Route
            hover_sound sdl_achv_click
            hovered [Show("sdl_dv_cl_active", transition=Dissolve(1.0)), Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)), Show("sdl_achv_dv_cltA", transition=Dissolve(0.5)), Hide("sdl_achv_dv_7dlA", transition=Dissolve(0.5)), Show("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_dv_cl_active", transition=Dissolve(1.0)), Show ("sdl_dv_cl_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_dv_cltA", transition=Dissolve(0.5)), Show("sdl_achv_dv_7dlA", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_dv_7dlA", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Show("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)), Show("sdl_dv_cl_active", transition=Dissolve(0.5)), Show("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_dvclt_Author")]
        hotspot ((1215, 18, 113,65)): #Speziell Route
            hover_sound sdl_achv_click
            hovered [Show("sdl_dv_dj_active", transition=Dissolve(1.0)), Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Show("sdl_achv_dv_djtA", transition=Dissolve(0.5)), Hide("sdl_achv_dv_7dlA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_dv_dj_active", transition=Dissolve(1.0)), Show ("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_dv_djtA", transition=Dissolve(0.5)), Show("sdl_achv_dv_7dlA", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_dv_7dlA", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(1.0)), Show("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Show("sdl_dv_dj_active", transition=Dissolve(0.5)), Show("sdl_dv_cl_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_dvdjt_Author")]
        hotspot ((650,40, 300, 52)): #Гуд-СССР
            hovered [Show("sdl_achv_good_US_dv", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_good_US_dv", transition=Dissolve(0.5))]
            action [Show("sdl_achv_good_US_dv", transition=Dissolve(0.5))]
        if persistent.dv_7dl_good_ussr:
            hotspot ((590, 40, 50, 52)): #UdSSR-Gut-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active1", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active1", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_dv_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)),  Hide("de_check_active1", transition=Dissolve(0.5)),Jump("alt_day7_dv_7dl_ussr_epilogue")]
        hotspot ((650,104, 300, 52)): #Гуд-РФ
            hovered [Show("sdl_achv_good_RF_dv", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_good_RF_dv", transition=Dissolve(0.5))]
            action [Show("sdl_achv_good_RF_dv", transition=Dissolve(0.5))]
        if persistent.dv_7dl_good_ussr_rf:
            hotspot ((590, 104, 50, 52)): #RF-Gut-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active2", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active2", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_dv_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)),  Hide("de_check_active2", transition=Dissolve(0.5)),Jump("alt_day7_dv_7dl_rf_epilogue")]
        hotspot ((650,168, 300, 52)): #Реджект-РФ
            hovered [Show("sdl_achv_rejc_RF_dv", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_rejc_RF_dv", transition=Dissolve(0.5))]
            action [Show("sdl_achv_rejc_RF_dv", transition=Dissolve(0.5))]
        if persistent.dv_7dl_reject_rf:
            hotspot ((590, 168, 50, 52)): #RF-Reject-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active3", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active3", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_dv_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)),  Hide("de_check_active3", transition=Dissolve(0.5)),Jump("alt_day7_dv_7dl_rej_rf_end")]
        hotspot ((650,232, 300, 52)): #Реджект-СССР
            hovered [Show("sdl_achv_rejc_US_dv", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_rejc_US_dv", transition=Dissolve(0.5))]
            action [Show("sdl_achv_rejc_US_dv", transition=Dissolve(0.5))]
        if persistent.dv_7dl_reject_ussr:
            hotspot ((590, 232, 50, 52)): #UdSSR-Reject-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active4", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active4", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_dv_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)),  Hide("de_check_active4", transition=Dissolve(0.5)),Jump("alt_day7_dv_7dl_rej_ussr_end")]
        hotspot ((650,296, 300, 52)): #Транзит-Ольга
            hovered [Show("sdl_achv_tran_dv", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_tran_dv", transition=Dissolve(0.5))]
            action [Show("sdl_achv_tran_dv", transition=Dissolve(0.5))]
        if persistent.dv_7dl_bad_mt:
            hotspot ((590, 296, 50, 52)): #Transit-MT-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active5", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active5", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_dv_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)),  Hide("de_check_active5", transition=Dissolve(0.5)),Jump("alt_day7_dv_7dl_bad_end_mt_ach")]
        hotspot ((650,360, 300, 52)): #Транзит-Лена
            hovered [Show("sdl_achv_tran_dv", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_tran_dv", transition=Dissolve(0.5))]
            action [Show("sdl_achv_tran_dv", transition=Dissolve(0.5))]
        if persistent.dv_7dl_un:
            hotspot ((590, 360, 50, 52)): #Transit-UN-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active6", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active6", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_dv_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)),  Hide("de_check_active6", transition=Dissolve(0.5)),Jump("alt_day7_dv_7dl_un_end")]
        hotspot ((650,424, 300, 52)): #Эксклюзив-Локи
            hovered [Show("sdl_achv_excl_LO_dv", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_excl_LO_dv", transition=Dissolve(0.5))]
            action [Show("sdl_achv_excl_LO_dv", transition=Dissolve(0.5))]
        if persistent.dv_7dl_tulpa:
            hotspot ((590, 424, 50, 52)): #Speziel-LK-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active7", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active7", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_dv_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)),  Hide("de_check_active7", transition=Dissolve(0.5)),Jump("alt_day7_dv_7dl_tulpa_end")]
        hotspot ((650,488, 300, 52)): #Бэд
            hovered [Show("sdl_achv_bad_dv", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_bad_dv", transition=Dissolve(0.5))]
            action [Show("sdl_achv_bad_dv", transition=Dissolve(0.5))]
        if persistent.dv_7dl_bad:
            hotspot ((590, 488, 50, 52)): #Schlecht-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active8", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active8", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_dv_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)),  Hide("de_check_active8", transition=Dissolve(0.5)),Jump("alt_day7_dv_7dl_bad_end")]

        hotspot ((0, 0, 550, 340)): #Мику
            hover_sound sdl_achv_pagina
            hovered [Show("mi_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mi_button_active", transition=Dissolve(0.5))]
            action [Hide("mi_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_dv_7dlA", transition=Dissolve(0.5)), Jump("sdl_achvlist_mi_Author")]
        hotspot ((0, 734, 550, 345)): #Славя
            hover_sound sdl_achv_pagina
            hovered [Show("sl_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("sl_button_active", transition=Dissolve(0.5))]
            action [Hide("sl_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_dv_7dlA", transition=Dissolve(0.5)), Jump("sdl_achvlist_sl_Author")]
        hotspot ((1380, 0, 600, 340)): #Лена
            hover_sound sdl_achv_pagina
            hovered [Show("un_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("un_button_active", transition=Dissolve(0.5))]
            action [Hide("un_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_dv_7dlA", transition=Dissolve(0.5)),  Jump("sdl_achvlist_un_Author")]
        hotspot ((1560, 343, 360, 185)): #Ольга
            hover_sound sdl_achv_pagina
            hovered [Show("mt_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mt_button_active", transition=Dissolve(0.5))]
            action [Hide("mt_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_dv_7dlA", transition=Dissolve(0.5)),  Jump("sdl_achvlist_mt_Author")]
        hotspot ((1561, 530, 359, 202)): #Ульяна
            hover_sound sdl_achv_pagina
            hovered [Show("us_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("us_button_active", transition=Dissolve(0.5))]
            action [Hide("us_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_dv_7dlA", transition=Dissolve(0.5)),  Jump("sdl_achvlist_us_Author")]
        hotspot ((1380, 735, 600, 345)): #Одиночка
            hover_sound sdl_achv_pagina
            hovered [Show("me_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("me_button_active", transition=Dissolve(0.5))]
            action [Hide("me_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_dv_7dlA", transition=Dissolve(0.5)),  Jump("sdl_achvlist_me_Author")]

        hotspot ((380, 350, 170, 50)): #Выход
            hover_sound sdl_achv_click
            hovered [Show("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            action [Hide("sdl_logo_active", transition=Dissolve(0.5)),Stop ("ambience"), Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_dv_7dlA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Jump("choose_waifu_7dl")]
        hotspot ((380, 680, 170, 50)): #Удалятор
            hover_sound sdl_achv_click
            activate_sound sdl_achv_clear
            hovered [Show("sdl_achv_delA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5))]
            action Jump("sdl_achvlist_dv7dl_clear_Author")
# ------------------------------------------------
######################АЛИСА-КЛАССИК######################################
label sdl_achvlist_dvclt_Author:
    scene bg sdl_ach_inactive_dv
    with dissolve
    show sdl_achv_delB_7dl: #Иконка удалятора
        pos (380, 680)
    show sdl_achv_extB_7dl: #Иконка Ausgang
        pos(380, 350)
    call screen sdl_achvlist_dvclt_Author
# ------------------------------------------------
screen sdl_achvlist_dvclt_Author:
    tag menu
    modal True
    imagemap:
        ground "intro_transparent"
        hotspot ((980, 18, 113,65)): #7DL Route
            hover_sound sdl_achv_click
            hovered [Show("sdl_logo_active", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_achv_dv_7dlA", transition=Dissolve(0.5)), Hide("sdl_achv_dv_cltA", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_logo_active", transition=Dissolve(1.0)), Show ("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_dv_7dlA", transition=Dissolve(0.5)), Show("sdl_achv_dv_cltA", transition=Dissolve(0.5)), Show("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_dv_cltA", transition=Dissolve(0.5)), Show("sdl_dv_cl_inactive", transition=Dissolve(0.5)), Hide ("sdl_dv_cl_active", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_logo_active", transition=Dissolve(0.5)), Show("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_dv7dl_Author")]
        hotspot ((1215, 18, 113,65)): #Speziell Route
            hover_sound sdl_achv_click
            hovered [Show("sdl_dv_dj_active", transition=Dissolve(1.0)), Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Show("sdl_achv_dv_djtA", transition=Dissolve(0.5)), Hide("sdl_achv_dv_cltA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_dv_dj_active", transition=Dissolve(1.0)), Show ("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_dv_djtA", transition=Dissolve(0.5)), Show("sdl_achv_dv_cltA", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_dv_cltA", transition=Dissolve(0.5)), Show("sdl_dv_cl_inactive", transition=Dissolve(0.5)), Hide ("sdl_dv_cl_active", transition=Dissolve(1.0)), Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Show("sdl_dv_dj_active", transition=Dissolve(0.5)), Show("sdl_logo_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_dvdjt_Author")]

        hotspot ((0, 0, 550, 340)): #Мику
            hover_sound sdl_achv_pagina
            hovered [Show("mi_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mi_button_active", transition=Dissolve(0.5))]
            action [Hide("mi_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_cl_active", transition=Dissolve(0.5)),Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_dv_cltA", transition=Dissolve(0.5)), Jump("sdl_achvlist_mi_Author")]
        hotspot ((0, 734, 550, 345)): #Славя
            hover_sound sdl_achv_pagina
            hovered [Show("sl_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("sl_button_active", transition=Dissolve(0.5))]
            action [Hide("sl_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_cl_active", transition=Dissolve(0.5)),Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_dv_cltA", transition=Dissolve(0.5)), Jump("sdl_achvlist_sl_Author")]
        hotspot ((1380, 0, 600, 340)): #Лена
            hover_sound sdl_achv_pagina
            hovered [Show("un_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("un_button_active", transition=Dissolve(0.5))]
            action [Hide("un_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_cl_active", transition=Dissolve(0.5)),Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_dv_cltA", transition=Dissolve(0.5)),  Jump("sdl_achvlist_un_Author")]
        hotspot ((1560, 343, 360, 185)): #Ольга
            hover_sound sdl_achv_pagina
            hovered [Show("mt_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mt_button_active", transition=Dissolve(0.5))]
            action [Hide("mt_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_cl_active", transition=Dissolve(0.5)),Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_dv_cltA", transition=Dissolve(0.5)),  Jump("sdl_achvlist_mt_Author")]
        hotspot ((1561, 530, 359, 202)): #Ульяна
            hover_sound sdl_achv_pagina
            hovered [Show("us_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("us_button_active", transition=Dissolve(0.5))]
            action [Hide("us_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_cl_active", transition=Dissolve(0.5)),Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_dv_cltA", transition=Dissolve(0.5)),  Jump("sdl_achvlist_us_Author")]
        hotspot ((1380, 735, 600, 345)): #Одиночка
            hover_sound sdl_achv_pagina
            hovered [Show("me_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("me_button_active", transition=Dissolve(0.5))]
            action [Hide("me_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_cl_active", transition=Dissolve(0.5)),Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_dv_cltA", transition=Dissolve(0.5)),  Jump("sdl_achvlist_me_Author")]

        hotspot ((380, 350, 170, 50)): #Выход
            hover_sound sdl_achv_click
            hovered [Show("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Stop ("ambience"), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_cl_active", transition=Dissolve(0.5)),Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_dv_cltA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Jump("choose_waifu_7dl")]
        hotspot ((380, 680, 170, 50)): #Удалятор
            hover_sound sdl_achv_click
            activate_sound sdl_achv_clear
            hovered [Show("sdl_achv_delA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5))]
            action Jump("sdl_achvlist_dvclt_clear_Author")
# ------------------------------------------------
######################АЛИСА-ДИДЖЕЙ######################################
label sdl_achvlist_dvdjt_Author:
    scene bg sdl_ach_inactive_dv
    with dissolve
    show sdl_achv_delB_7dl: #Иконка удалятора
        pos (380, 680)
    show sdl_achv_extB_7dl: #Иконка Ausgang
        pos(380, 350)
    call screen sdl_achvlist_dvdjt_Author
# ------------------------------------------------
screen sdl_achvlist_dvdjt_Author:
    tag menu
    modal True
    imagemap:
        ground "intro_transparent"
        hotspot ((980, 18, 113,65)): #7DL Route
            hover_sound sdl_achv_click
            hovered [Show("sdl_logo_active", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_achv_dv_7dlA", transition=Dissolve(0.5)), Hide("sdl_achv_dv_djtA", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_logo_active", transition=Dissolve(1.0)), Show ("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_dv_7dlA", transition=Dissolve(0.5)), Show("sdl_achv_dv_djtA", transition=Dissolve(0.5)), Show("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_dv_djtA", transition=Dissolve(0.5)), Show("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Hide ("sdl_dv_dj_active", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_logo_active", transition=Dissolve(0.5)), Show("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_dv7dl_Author")]
        hotspot ((1110,18, 113,65)): #Klassishe Route
            hover_sound sdl_achv_click
            hovered [Show("sdl_dv_cl_active", transition=Dissolve(1.0)), Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)), Show("sdl_achv_dv_cltA", transition=Dissolve(0.5)), Hide("sdl_achv_dv_djtA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_dv_cl_active", transition=Dissolve(1.0)), Show ("sdl_dv_cl_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_dv_cltA", transition=Dissolve(0.5)), Show("sdl_achv_dv_djtA", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_dv_djtA", transition=Dissolve(0.5)), Show("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_dv_dj_active", transition=Dissolve(0.5)), Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)), Show("sdl_dv_cl_active", transition=Dissolve(1.0)),Show("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_dvclt_Author")]

        hotspot ((0, 0, 550, 340)): #Мику
            hover_sound sdl_achv_pagina
            hovered [Show("mi_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mi_button_active", transition=Dissolve(0.5))]
            action [Hide("mi_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_dj_active", transition=Dissolve(0.5)), Hide("sdl_achv_dv_djtA", transition=Dissolve(0.5)), Jump("sdl_achvlist_mi_Author")]
        hotspot ((0, 734, 550, 345)): #Славя
            hover_sound sdl_achv_pagina
            hovered [Show("sl_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("sl_button_active", transition=Dissolve(0.5))]
            action [Hide("sl_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_dj_active", transition=Dissolve(0.5)), Hide("sdl_achv_dv_djtA", transition=Dissolve(0.5)), Jump("sdl_achvlist_sl_Author")]
        hotspot ((1380, 0, 600, 340)): #Лена
            hover_sound sdl_achv_pagina
            hovered [Show("un_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("un_button_active", transition=Dissolve(0.5))]
            action [Hide("un_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_dj_active", transition=Dissolve(0.5)), Hide("sdl_achv_dv_djtA", transition=Dissolve(0.5)),  Jump("sdl_achvlist_un_Author")]
        hotspot ((1560, 343, 360, 185)): #Ольга
            hover_sound sdl_achv_pagina
            hovered [Show("mt_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mt_button_active", transition=Dissolve(0.5))]
            action [Hide("mt_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_dj_active", transition=Dissolve(0.5)), Hide("sdl_achv_dv_djtA", transition=Dissolve(0.5)),  Jump("sdl_achvlist_mt_Author")]
        hotspot ((1561, 530, 359, 202)): #Ульяна
            hover_sound sdl_achv_pagina
            hovered [Show("us_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("us_button_active", transition=Dissolve(0.5))]
            action [Hide("us_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_dj_active", transition=Dissolve(0.5)), Hide("sdl_achv_dv_djtA", transition=Dissolve(0.5)),  Jump("sdl_achvlist_us_Author")]
        hotspot ((1380, 735, 600, 345)): #Одиночка
            hover_sound sdl_achv_pagina
            hovered [Show("me_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("me_button_active", transition=Dissolve(0.5))]
            action [Hide("me_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_dj_active", transition=Dissolve(0.5)), Hide("sdl_achv_dv_djtA", transition=Dissolve(0.5)),  Jump("sdl_achvlist_me_Author")]

        hotspot ((380, 350, 170, 50)): #Выход
            hover_sound sdl_achv_click
            hovered [Show("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Stop ("ambience"), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_dj_active", transition=Dissolve(0.5)), Hide("sdl_achv_dv_djtA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Jump("choose_waifu_7dl")]
        hotspot ((380, 680, 170, 50)): #Удалятор
            hover_sound sdl_achv_click
            activate_sound sdl_achv_clear
            hovered [Show("sdl_achv_delA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5))]
            action Jump("sdl_achvlist_dvdjt_clear_Author")
# ------------------------------------------------
##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\БЛОК СЛАВИ\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Slavjas Erreichunge
label sdl_achvlist_sl_Author:
    scene bg sdl_ach_inactive_sl
    with dissolve
    show sdl_logo_inactive: #7DL logo
        pos (980, 18)
    show sdl_sl_cl_inactive: #Klassishe logo
        pos (1110, 18)
    show sdl_sl_wh_inactive: #Speziell logo
        pos (1215, 18)
    show sdl_achv_extB_7dl: #Иконка Ausgang
        pos(380, 350)
    call screen sdl_achvlist_sl_Author
    screen sdl_achvlist_sl_Author:
        tag menu
        modal True
        imagemap:
            ground "intro_transparent"
            hotspot ((980, 18, 113,65)): #7DL Route
                hover_sound sdl_achv_click
                hovered [Show("sdl_achv_7dl_route", transition=Dissolve(1.0)), Show("sdl_logo_active", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_achv_sl_7dlA", transition=Dissolve(0.5)), Show("sdl_achv_need_routeA", transition=Dissolve(0.5))]
                unhovered [Hide("sdl_achv_7dl_route", transition=Dissolve(1.0)), Hide ("sdl_logo_active", transition=Dissolve(1.0)), Show ("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_7dlA", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5))]
                action [Hide("sdl_achv_7dl_route", transition=Dissolve(1.0)), Show("sdl_sl_cl_inactive", transition=Dissolve(0.5)), Show("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Show("sdl_achv_need_routeA", transition=Dissolve(0.5)), Jump("sdl_achvlist_sl7dl_Author")]
            hotspot ((1110,18, 113,65)): #Klassishe Route
                hover_sound sdl_achv_click
                hovered [Show("sdl_achv_clt_route", transition=Dissolve(1.0)), Show("sdl_sl_cl_active", transition=Dissolve(1.0)), Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)), Show("sdl_achv_sl_cltA", transition=Dissolve(0.5))]
                unhovered [Hide("sdl_achv_clt_route", transition=Dissolve(1.0)), Hide ("sdl_sl_cl_active", transition=Dissolve(1.0)), Show ("sdl_sl_cl_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(0.5))]
                action [Hide("sdl_achv_clt_route", transition=Dissolve(1.0)), Show("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_slclt_Author")]
            hotspot ((1215, 18, 113,65)): #Speziell Route
                hover_sound sdl_achv_click
                hovered [Show("sdl_achv_xxx_route", transition=Dissolve(1.0)), Show("sdl_sl_wh_active", transition=Dissolve(1.0)), Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Show("sdl_achv_sl_whtA", transition=Dissolve(0.5)), Show("sdl_achv_need_routeA", transition=Dissolve(0.5))]
                unhovered [Hide("sdl_achv_xxx_route", transition=Dissolve(1.0)), Hide("sdl_sl_wh_active", transition=Dissolve(1.0)), Show ("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_whtA", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5))]
                action [Hide("sdl_achv_xxx_route", transition=Dissolve(1.0)), Show("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_sl_cl_inactive", transition=Dissolve(0.5)), Show("sdl_achv_need_routeA", transition=Dissolve(0.5)), Jump("sdl_achvlist_slwht_Author")]

            hotspot ((0, 0, 550, 340)): #Мику
                hover_sound sdl_achv_pagina
                hovered [Show("mi_button_active", transition=Dissolve(0.5))]
                unhovered [Hide("mi_button_active", transition=Dissolve(0.5))]
                action [Hide("mi_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_mi_Author")]
            hotspot ((0, 344, 360, 390)): #Алисхен
                hover_sound sdl_achv_pagina
                hovered [Show("dv_button_active", transition=Dissolve(0.5))]
                unhovered [Hide("dv_button_active", transition=Dissolve(0.5))]
                action [Hide("dv_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_dv_Author")]
            hotspot ((1380, 0, 600, 340)): #Лена
                hover_sound sdl_achv_pagina
                hovered [Show("un_button_active", transition=Dissolve(0.5))]
                unhovered [Hide("un_button_active", transition=Dissolve(0.5))]
                action [Hide("un_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_un_Author")]
            hotspot ((1560, 343, 360, 185)): #Ольга
                hover_sound sdl_achv_pagina
                hovered [Show("mt_button_active", transition=Dissolve(0.5))]
                unhovered [Hide("mt_button_active", transition=Dissolve(0.5))]
                action [Hide("mt_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_mt_Author")]
            hotspot ((1561, 530, 359, 202)): #Ульяна
                hover_sound sdl_achv_pagina
                hovered [Show("us_button_active", transition=Dissolve(0.5))]
                unhovered [Hide("us_button_active", transition=Dissolve(0.5))]
                action [Hide("us_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_us_Author")]
            hotspot ((1380, 735, 600, 345)): #Одиночка
                hover_sound sdl_achv_pagina
                hovered [Show("me_button_active", transition=Dissolve(0.5))]
                unhovered [Hide("me_button_active", transition=Dissolve(0.5))]
                action [Hide("me_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_me_Author")]
            hotspot ((380, 350, 170, 50)): #Выход
                hover_sound sdl_achv_click
                hovered [Show("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
                unhovered [Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
                action [Hide("sdl_logo_active", transition=Dissolve(0.5)),Stop ("ambience"), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Jump("choose_waifu_7dl")]
# ------------------------------------------------
######################СЛАВЯ-7ДЛ######################################
label sdl_achvlist_sl7dl_Author:
    scene bg sdl_ach_inactive_sl
    with dissolve
    show sdl_achv_delB_7dl: #Иконка удалятора
        pos (380, 680)
    show sdl_achv_extB_7dl: #Иконка Ausgang
        pos(380, 350)
    call screen sdl_achvlist_sl7dl_Author
# ------------------------------------------------
screen sdl_achvlist_sl7dl_Author:
    tag menu
    modal True
    imagemap:
        ground "intro_transparent"
        hotspot ((1110,18, 113,65)): #Klassishe Route
            hover_sound sdl_achv_click
            hovered [Show("sdl_sl_cl_active", transition=Dissolve(1.0)), Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)), Show("sdl_achv_sl_cltA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_7dlA", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_sl_cl_active", transition=Dissolve(1.0)), Show ("sdl_sl_cl_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(0.5)), Show("sdl_achv_sl_7dlA", transition=Dissolve(0.5)), Show("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_sl_7dlA", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Show("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)), Show("sdl_sl_cl_active", transition=Dissolve(0.5)), Show("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_slclt_Author")]
        hotspot ((1215, 18, 113,65)): #Speziell Route
            hover_sound sdl_achv_click
            hovered [Show("sdl_sl_wh_active", transition=Dissolve(1.0)), Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Show("sdl_achv_sl_whtA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_7dlA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_sl_wh_active", transition=Dissolve(1.0)), Show ("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_whtA", transition=Dissolve(0.5)), Show("sdl_achv_sl_7dlA", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_sl_7dlA", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(1.0)), Show("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Show("sdl_sl_wh_active", transition=Dissolve(0.5)), Show("sdl_sl_cl_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_slwht_Author")]

        hotspot ((0, 0, 550, 340)): #Мику
            hover_sound sdl_achv_pagina
            hovered [Show("mi_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mi_button_active", transition=Dissolve(0.5))]
            action [Hide("mi_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_7dlA", transition=Dissolve(0.5)), Jump("sdl_achvlist_mi_Author")]
        hotspot ((0, 344, 360, 390)): #Алисхен
            hover_sound sdl_achv_pagina
            hovered [Show("dv_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("dv_button_active", transition=Dissolve(0.5))]
            action [Hide("dv_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_7dlA", transition=Dissolve(0.5)), Jump("sdl_achvlist_dv_Author")]
        hotspot ((1380, 0, 600, 340)): #Лена
            hover_sound sdl_achv_pagina
            hovered [Show("un_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("un_button_active", transition=Dissolve(0.5))]
            action [Hide("un_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_7dlA", transition=Dissolve(0.5)),  Jump("sdl_achvlist_un_Author")]
        hotspot ((1560, 343, 360, 185)): #Ольга
            hover_sound sdl_achv_pagina
            hovered [Show("mt_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mt_button_active", transition=Dissolve(0.5))]
            action [Hide("mt_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_7dlA", transition=Dissolve(0.5)),  Jump("sdl_achvlist_mt_Author")]
        hotspot ((1561, 530, 359, 202)): #Ульяна
            hover_sound sdl_achv_pagina
            hovered [Show("us_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("us_button_active", transition=Dissolve(0.5))]
            action [Hide("us_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_7dlA", transition=Dissolve(0.5)),  Jump("sdl_achvlist_us_Author")]
        hotspot ((1380, 735, 600, 345)): #Одиночка
            hover_sound sdl_achv_pagina
            hovered [Show("me_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("me_button_active", transition=Dissolve(0.5))]
            action [Hide("me_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_7dlA", transition=Dissolve(0.5)),  Jump("sdl_achvlist_me_Author")]

        hotspot ((380, 350, 170, 50)): #Выход
            hover_sound sdl_achv_click
            hovered [Show("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Stop ("ambience"), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_7dlA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Jump("choose_waifu_7dl")]
        hotspot ((380, 680, 170, 50)): #Удалятор
            hover_sound sdl_achv_click
            activate_sound sdl_achv_clear
            hovered [Show("sdl_achv_delA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5))]
            action Jump("sdl_achvlist_sl7dl_clear_Author")
# ------------------------------------------------
######################СЛАВЯ-КЛАССИК##################################
label sdl_achvlist_slclt_Author:
    scene bg sdl_ach_inactive_sl
    with dissolve
    show sdl_achv_delB_7dl: #Иконка удалятора
        pos (380, 680)
    show sdl_achv_extB_7dl: #Иконка Ausgang
        pos(380, 350)
    #Инт-ТруЪ
    if persistent.sl_cl_int_ok:
        show acm_logo_sl_ok  with dissolve:
            xcenter 800 ycenter 66
        show de_check_inactive1 with dissolve:
            pos (590, 40)
    else:
        show de_achiv_lock1 with dissolve:
            xcenter 800 ycenter 66
    if not persistent.sl_cl_int_good:
        show de_info_inactive1 with dissolve:
            pos (590, 40)
    else:
        pass
    #Инт-гуд
    if persistent.sl_cl_int_good:
        show acm_logo_sl_fantazm  with dissolve:
            xcenter 800 ycenter 130
        show de_check_inactive2 with dissolve:
            pos (590, 104)
    else:
        show de_achiv_lock2 with dissolve:
            xcenter 800 ycenter 130
    if not (persistent.sl_cl_good_rf or persistent.sl_cl_good_rf2 or persistent.sl_cl_good_ussr):
        show de_info_inactive2 with dissolve:
            pos (590, 104)
    else:
        pass
    #Инт-бэд
    if persistent.sl_cl_int_bad:
        show acm_logo_sl_lone with dissolve:
            xcenter 800 ycenter 194
        show de_check_inactive3 with dissolve:
            pos (590, 168)
    else:
        show de_achiv_lock3 with dissolve:
            xcenter 800 ycenter 194
    if not (persistent.sl_cl_good_rf or persistent.sl_cl_good_rf2 or persistent.sl_cl_good_ussr):
        show de_info_inactive3 with dissolve:
            pos (590, 168)
    else:
        pass
    #СССР-гуд
    if persistent.sl_cl_good_ussr:
        show acm_logo_sl_good with dissolve:
            xcenter 800 ycenter 258
        show de_check_inactive4 with dissolve:
            pos (590, 232)
    else:
        show de_achiv_lock4 with dissolve:
            xcenter 800 ycenter 258
    #РФ-гуд
    if persistent.sl_cl_good_rf2:
        show acm_logo_sl_worth  with dissolve:
            xcenter 800 ycenter 322
        show de_check_inactive5 with dissolve:
            pos (590, 296)
    else:
        show de_achiv_lock5 with dissolve:
            xcenter 800 ycenter 322
    #РФ-гуд (Плюс-минус)
    if persistent.sl_cl_good_rf:
        show acm_logo_sl_good1  with dissolve:
            xcenter 800 ycenter 386
        show de_check_inactive6 with dissolve:
            pos (590, 360)
    else:
        show de_achiv_lock6 with dissolve:
            xcenter 800 ycenter 386
    #Реджект-РФ
    if persistent.sl_cl_reject_same:
        show acm_logo_sl_same_place with dissolve:
            xcenter 800 ycenter 450
        show de_check_inactive7 with dissolve:
            pos (590, 424)
    else:
        show de_achiv_lock7 with dissolve:
            xcenter 800 ycenter 450
    #Реджект-2
    if persistent.sl_cl_reject_late:
        show acm_logo_sl_too_late  with dissolve:
            xcenter 800 ycenter 514
        show de_check_inactive8 with dissolve:
            pos (590, 488)
    else:
        show de_achiv_lock8 with dissolve:
            xcenter 800 ycenter 514
    #Эксклюзив-Локи
    if persistent.sl_cl_cata:
        show acm_logo_sl_be_ok with dissolve:
            xcenter 800 ycenter 578
        show de_check_inactive9 with dissolve:
            pos (590, 552)
    else:
        show de_achiv_lock9 with dissolve:
            xcenter 800 ycenter 578
    #Бэд
    if persistent.sl_cl_bad:
        show acm_logo_sl_bad  with dissolve:
            xcenter 800 ycenter 642
        show de_check_inactive10 with dissolve:
            pos (590, 616)
    else:
        show de_achiv_lock10 with dissolve:
            xcenter 800 ycenter 642
    call screen sdl_achvlist_slclt_Author
# ------------------------------------------------
screen sdl_achvlist_slclt_Author:
    tag menu
    modal True
    imagemap:
        ground "intro_transparent"
        hotspot ((980, 18, 113,65)): #7DL Route
            hover_sound sdl_achv_click
            hovered [Show("sdl_logo_active", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_achv_sl_7dlA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(0.5)), Show("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_logo_active", transition=Dissolve(1.0)), Show ("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_7dlA", transition=Dissolve(0.5)), Show("sdl_achv_sl_cltA", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_sl_cltA", transition=Dissolve(0.5)), Show("sdl_sl_cl_inactive", transition=Dissolve(0.5)), Hide ("sdl_sl_cl_active", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_logo_active", transition=Dissolve(0.5)), Show("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_sl7dl_Author")]
        hotspot ((1215, 18, 113,65)): #Speziell Route
            hover_sound sdl_achv_click
            hovered [Show("sdl_sl_wh_active", transition=Dissolve(1.0)), Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Show("sdl_achv_sl_whtA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(0.5)), Show("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_sl_wh_active", transition=Dissolve(1.0)), Show ("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_whtA", transition=Dissolve(0.5)), Show("sdl_achv_sl_cltA", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_sl_cltA", transition=Dissolve(0.5)), Show("sdl_sl_cl_inactive", transition=Dissolve(0.5)), Hide ("sdl_sl_cl_active", transition=Dissolve(1.0)), Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Show("sdl_sl_wh_active", transition=Dissolve(0.5)), Show("sdl_logo_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_slwht_Author")]
        hotspot ((650,40, 300, 52)): #Инт-ТруЪ
            hovered [Show("sdl_achv_true_IN_sl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_true_IN_sl", transition=Dissolve(0.5))]
            action [Show("sdl_achv_true_IN_sl", transition=Dissolve(0.5))]
        if persistent.sl_cl_int_ok:
            hotspot ((590, 40, 50, 52)): #Int-Wahr-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active1", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active1", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_cl_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)),  Hide("de_check_active1", transition=Dissolve(0.5)),Jump("alt_day7_sl_will")]
        elif not persistent.sl_cl_int_good:
            hotspot ((590, 40, 50, 50)): #Ende-Info
                hover_sound sdl_achv_info
                hovered [Show ("de_info_active1", transition=Dissolve(0.5)), Show ("sdl_achv_infochkD", transition=Dissolve(0.5)), Show ("acm_logo_sl_fantazm", transition=Dissolve(0.5))]
                unhovered [Hide ("de_info_active1", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_sl_fantazm", transition=Dissolve(0.5))]
                action [Hide("de_info_active1", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_sl_fantazm", transition=Dissolve(0.5))]
        hotspot ((650,104, 300, 52)): #Инт-гуд
            hovered [Show("sdl_achv_good_IN_sl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_good_IN_sl", transition=Dissolve(0.5))]
            action [Show("sdl_achv_good_IN_sl", transition=Dissolve(0.5))]
        if persistent.sl_cl_int_good:
            hotspot ((590, 104, 50, 52)): #Int-Gut-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active2", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active2", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_cl_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)),  Hide("de_check_active2", transition=Dissolve(0.5)),Jump("alt_day7_sl_duty")]
        elif not (persistent.sl_cl_good_rf or persistent.sl_cl_good_rf2 or persistent.sl_cl_good_ussr):
            hotspot ((590, 104, 50, 50)): #Ende-Info
                hover_sound sdl_achv_info
                hovered [Show ("de_info_active2", transition=Dissolve(0.5)), Show ("sdl_achv_infochkD", transition=Dissolve(0.5)), Show ("acm_logo_sl_good", transition=Dissolve(0.5))]
                unhovered [Hide ("de_info_active2", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_sl_good", transition=Dissolve(0.5))]
                action [Hide("de_info_active2", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_sl_good", transition=Dissolve(0.5))]
        hotspot ((650,168, 300, 52)): #Инт-бэд
            hovered [Show("sdl_achv_bad_IN_sl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_bad_IN_sl", transition=Dissolve(0.5))]
            action [Show("sdl_achv_bad_IN_sl", transition=Dissolve(0.5))]
        if persistent.sl_cl_int_bad:
            hotspot ((590, 168, 50, 52)): #Int-schlecht-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active3", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active3", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_cl_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)),  Hide("de_check_active3", transition=Dissolve(0.5)),Jump("alt_day7_sl_lone")]
        elif not (persistent.sl_cl_good_rf or persistent.sl_cl_good_rf2 or persistent.sl_cl_good_ussr):
            hotspot ((590, 168, 50, 50)): #Ende-Info
                hover_sound sdl_achv_info
                hovered [Show ("de_info_active3", transition=Dissolve(0.5)), Show ("sdl_achv_infochkD", transition=Dissolve(0.5)), Show ("acm_logo_sl_good", transition=Dissolve(0.5))]
                unhovered [Hide ("de_info_active3", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_sl_good", transition=Dissolve(0.5))]
                action [Hide("de_info_active3", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_sl_good", transition=Dissolve(0.5))]
        hotspot ((650,232, 300, 52)): #СССР-гуд
            hovered [Show("sdl_achv_good_US_sl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_good_US_sl", transition=Dissolve(0.5))]
            action [Show("sdl_achv_good_US_sl", transition=Dissolve(0.5))]
        if persistent.sl_cl_good_ussr:
            hotspot ((590, 232, 50, 52)): #UdSSR-gut-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active4", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active4", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_cl_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)),  Hide("de_check_active4", transition=Dissolve(0.5)),Jump("alt_day7_sl_good")]
        hotspot ((650,296, 300, 52)): #РФ-гуд
            hovered [Show("sdl_achv_good_RF_sl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_good_RF_sl", transition=Dissolve(0.5))]
            action [Show("sdl_achv_good_RF_sl", transition=Dissolve(0.5))]
        if persistent.sl_cl_good_rf2:
            hotspot ((590, 296, 50, 52)): #RF-gut-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active5", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active5", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_cl_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)),  Hide("de_check_active5", transition=Dissolve(0.5)),Jump("alt_day7_sl_rf2")]
        hotspot ((650,360, 300, 52)): #РФ-гуд (Плюс-минус)
            hovered [Show("sdl_achv_good_RF_sl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_good_RF_sl", transition=Dissolve(0.5))]
            action [Show("sdl_achv_good_RF_sl", transition=Dissolve(0.5))]
        if persistent.sl_cl_good_rf:
            hotspot ((590, 360, 50, 52)): #RF-gut-Ende (Plus-Minus)-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active6", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active6", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_cl_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)),  Hide("de_check_active6", transition=Dissolve(0.5)),Jump("alt_day7_sl_rf_good")]
        hotspot ((650,424, 300, 52)): #Реджект-РФ
            hovered [Show("sdl_achv_rejc_RF_sl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_rejc_RF_sl", transition=Dissolve(0.5))]
            action [Show("sdl_achv_rejc_RF_sl", transition=Dissolve(0.5))]
        if persistent.sl_cl_reject_same:
            hotspot ((590, 424, 50, 52)): #Reject-RF-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active7", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active7", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_cl_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)),  Hide("de_check_active7", transition=Dissolve(0.5)),Jump("alt_day7_sl_reject_same")]
        hotspot ((650,488, 300, 52)): #Реджект-2
            hovered [Show("sdl_achv_rejc_RF_sl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_rejc_RF_sl", transition=Dissolve(0.5))]
            action [Show("sdl_achv_rejc_RF_sl", transition=Dissolve(0.5))]
        if persistent.sl_cl_reject_late:
            hotspot ((590, 488, 50, 52)): #Reject-RF-Ende-2-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active8", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active8", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_cl_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)),  Hide("de_check_active8", transition=Dissolve(0.5)),Jump("alt_day7_sl_reject_late")]
        hotspot ((650,552, 300, 52)): #Эксклюзив-Локи
            hovered [Show("sdl_achv_excl_LO_sl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_excl_LO_sl", transition=Dissolve(0.5))]
            action [Show("sdl_achv_excl_LO_sl", transition=Dissolve(0.5))]
        if persistent.sl_cl_cata:
            hotspot ((590, 552, 50, 52)): #schlecht-M-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active9", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active9", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_cl_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)),  Hide("de_check_active9", transition=Dissolve(0.5)),Jump("alt_day6_sl_cl_become_a_hero")]
        hotspot ((650,616, 300, 52)): #Бэд
            hovered [Show("sdl_achv_bad_sl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_bad_sl", transition=Dissolve(0.5))]
            action [Show("sdl_achv_bad_sl", transition=Dissolve(0.5))]
        if persistent.sl_cl_bad:
            hotspot ((590, 616, 50, 52)): #schlecht-S-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active10", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active10", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_cl_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)),  Hide("de_check_active10", transition=Dissolve(0.5)),Jump("alt_day7_sl_cl_bad")]

        hotspot ((0, 0, 550, 340)): #Мику
            hover_sound sdl_achv_pagina
            hovered [Show("mi_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mi_button_active", transition=Dissolve(0.5))]
            action [Hide("mi_button_active", transition=Dissolve(0.5)),  Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_cl_active", transition=Dissolve(0.5)),Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(0.5)), Jump("sdl_achvlist_mi_Author")]
        hotspot ((0, 344, 360, 390)): #Алисхен
            hover_sound sdl_achv_pagina
            hovered [Show("dv_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("dv_button_active", transition=Dissolve(0.5))]
            action [Hide("dv_button_active", transition=Dissolve(0.5)),  Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_cl_active", transition=Dissolve(0.5)),Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(0.5)), Jump("sdl_achvlist_dv_Author")]
        hotspot ((1380, 0, 600, 340)): #Лена
            hover_sound sdl_achv_pagina
            hovered [Show("un_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("un_button_active", transition=Dissolve(0.5))]
            action [Hide("un_button_active", transition=Dissolve(0.5)),  Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_cl_active", transition=Dissolve(0.5)),Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(0.5)),  Jump("sdl_achvlist_un_Author")]
        hotspot ((1560, 343, 360, 185)): #Ольга
            hover_sound sdl_achv_pagina
            hovered [Show("mt_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mt_button_active", transition=Dissolve(0.5))]
            action [Hide("mt_button_active", transition=Dissolve(0.5)),  Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_cl_active", transition=Dissolve(0.5)),Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(0.5)),  Jump("sdl_achvlist_mt_Author")]
        hotspot ((1561, 530, 359, 202)): #Ульяна
            hover_sound sdl_achv_pagina
            hovered [Show("us_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("us_button_active", transition=Dissolve(0.5))]
            action [Hide("us_button_active", transition=Dissolve(0.5)),  Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_cl_active", transition=Dissolve(0.5)),Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(0.5)),  Jump("sdl_achvlist_us_Author")]
        hotspot ((1380, 735, 600, 345)): #Одиночка
            hover_sound sdl_achv_pagina
            hovered [Show("me_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("me_button_active", transition=Dissolve(0.5))]
            action [Hide("me_button_active", transition=Dissolve(0.5)),  Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_cl_active", transition=Dissolve(0.5)),Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(0.5)),  Jump("sdl_achvlist_me_Author")]

        hotspot ((380, 350, 170, 50)): #Выход
            hover_sound sdl_achv_click
            hovered [Show("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            action [Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Stop ("ambience"), Hide("sdl_sl_cl_active", transition=Dissolve(0.5)),Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Jump("choose_waifu_7dl")]
        hotspot ((380, 680, 170, 50)): #Удалятор
            hover_sound sdl_achv_click
            activate_sound sdl_achv_clear
            hovered [Show("sdl_achv_delA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5))]
            action Jump("sdl_achvlist_slclt_clear_Author")
# ------------------------------------------------
######################СЛАВЯ-ВЕДЬМА######################################
label sdl_achvlist_slwht_Author:
    scene bg sdl_ach_inactive_sl
    with dissolve
    show sdl_achv_delB_7dl: #Иконка удалятора
        pos (380, 680)
    show sdl_achv_extB_7dl: #Иконка Ausgang
        pos(380, 350)
    call screen sdl_achvlist_slwht_Author
# ------------------------------------------------
screen sdl_achvlist_slwht_Author:
    tag menu
    modal True
    imagemap:
        ground "intro_transparent"
        hotspot ((980, 18, 113,65)): #7DL Route
            hover_sound sdl_achv_click
            hovered [Show("sdl_logo_active", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_achv_sl_7dlA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_whtA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_logo_active", transition=Dissolve(1.0)), Show ("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_7dlA", transition=Dissolve(0.5)), Show("sdl_achv_sl_whtA", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_sl_whtA", transition=Dissolve(0.5)), Show("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide ("sdl_sl_wh_active", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_logo_active", transition=Dissolve(0.5)), Show("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_sl7dl_Author")]
        hotspot ((1110,18, 113,65)): #Klassishe Route
            hover_sound sdl_achv_click
            hovered [Show("sdl_sl_cl_active", transition=Dissolve(1.0)), Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)), Show("sdl_achv_sl_cltA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_whtA", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_sl_cl_active", transition=Dissolve(1.0)), Show ("sdl_sl_cl_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(0.5)), Show("sdl_achv_sl_whtA", transition=Dissolve(0.5)), Show("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_sl_whtA", transition=Dissolve(0.5)), Show("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_wh_active", transition=Dissolve(0.5)), Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)), Show("sdl_sl_cl_active", transition=Dissolve(1.0)),Show("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_slclt_Author")]

        hotspot ((0, 0, 550, 340)): #Мику
            hover_sound sdl_achv_pagina
            hovered [Show("mi_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mi_button_active", transition=Dissolve(0.5))]
            action [Hide("mi_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_wh_active", transition=Dissolve(0.5)), Hide("sdl_achv_sl_whtA", transition=Dissolve(0.5)), Jump("sdl_achvlist_mi_Author")]
        hotspot ((0, 344, 360, 390)): #Алисхен
            hover_sound sdl_achv_pagina
            hovered [Show("dv_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("dv_button_active", transition=Dissolve(0.5))]
            action [Hide("dv_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_wh_active", transition=Dissolve(0.5)), Hide("sdl_achv_sl_whtA", transition=Dissolve(0.5)), Jump("sdl_achvlist_dv_Author")]
        hotspot ((1380, 0, 600, 340)): #Лена
            hover_sound sdl_achv_pagina
            hovered [Show("un_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("un_button_active", transition=Dissolve(0.5))]
            action [Hide("un_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_wh_active", transition=Dissolve(0.5)), Hide("sdl_achv_sl_whtA", transition=Dissolve(0.5)),  Jump("sdl_achvlist_un_Author")]
        hotspot ((1560, 343, 360, 185)): #Ольга
            hover_sound sdl_achv_pagina
            hovered [Show("mt_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mt_button_active", transition=Dissolve(0.5))]
            action [Hide("mt_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_wh_active", transition=Dissolve(0.5)), Hide("sdl_achv_sl_whtA", transition=Dissolve(0.5)),  Jump("sdl_achvlist_mt_Author")]
        hotspot ((1561, 530, 359, 202)): #Ульяна
            hover_sound sdl_achv_pagina
            hovered [Show("us_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("us_button_active", transition=Dissolve(0.5))]
            action [Hide("us_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_wh_active", transition=Dissolve(0.5)), Hide("sdl_achv_sl_whtA", transition=Dissolve(0.5)),  Jump("sdl_achvlist_us_Author")]
        hotspot ((1380, 735, 600, 345)): #Одиночка
            hover_sound sdl_achv_pagina
            hovered [Show("me_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("me_button_active", transition=Dissolve(0.5))]
            action [Hide("me_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_wh_active", transition=Dissolve(0.5)), Hide("sdl_achv_sl_whtA", transition=Dissolve(0.5)),  Jump("sdl_achvlist_me_Author")]

        hotspot ((380, 350, 170, 50)): #Выход
            hover_sound sdl_achv_click
            hovered [Show("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Stop ("ambience"), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_wh_active", transition=Dissolve(0.5)), Hide("sdl_achv_sl_whtA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Jump("choose_waifu_7dl")]
        hotspot ((380, 680, 170, 50)): #Удалятор
            hover_sound sdl_achv_click
            activate_sound sdl_achv_clear
            hovered [Show("sdl_achv_delA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5))]
            action Jump("sdl_achvlist_slwht_clear_Author")
# ------------------------------------------------
##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\БЛОК ЛЕНЫ\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Lenas Erreichunge
label sdl_achvlist_un_Author:
    scene bg sdl_ach_inactive_un
    with dissolve
    show sdl_logo_inactive: #7DL logo
        pos (980, 18)
    show sdl_un_cl_inactive: #Klassishe logo
        pos (1110, 18)
    show sdl_un_fz_inactive: #Speziell logo
        pos (1215, 18)
    show sdl_achv_extB_7dl: #Иконка Ausgang
        pos(380, 350)
    call screen sdl_achvlist_un_Author
    screen sdl_achvlist_un_Author:
        tag menu
        modal True
        imagemap:
            ground "intro_transparent"
            hotspot ((980, 18, 113,65)): #7DL Route
                hover_sound sdl_achv_click
                hovered [Show("sdl_achv_7dl_route", transition=Dissolve(1.0)), Show("sdl_logo_active", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_achv_un_7dlA", transition=Dissolve(0.5))]
                unhovered [Hide("sdl_achv_7dl_route", transition=Dissolve(1.0)), Hide ("sdl_logo_active", transition=Dissolve(1.0)), Show ("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_un_7dlA", transition=Dissolve(0.5))]
                action [Hide("sdl_achv_7dl_route", transition=Dissolve(1.0)), Show("sdl_un_cl_inactive", transition=Dissolve(0.5)), Show("sdl_un_fz_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_un7dl_Author")]
            hotspot ((1110,18, 113,65)): #Klassishe Route
                hover_sound sdl_achv_click
                hovered [Show("sdl_achv_clt_route", transition=Dissolve(1.0)), Show("sdl_un_cl_active", transition=Dissolve(1.0)), Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)), Show("sdl_achv_un_cltA", transition=Dissolve(0.5)), Show("sdl_achv_need_routeA", transition=Dissolve(0.5))]
                unhovered [Hide("sdl_achv_clt_route", transition=Dissolve(1.0)), Hide ("sdl_un_cl_active", transition=Dissolve(1.0)), Show ("sdl_un_cl_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_un_cltA", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5))]
                action [Hide("sdl_achv_clt_route", transition=Dissolve(1.0)), Show("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_un_fz_inactive", transition=Dissolve(0.5)), Show("sdl_achv_need_routeA", transition=Dissolve(0.5)), Jump("sdl_achvlist_unclt_Author")]
            hotspot ((1215, 18, 113,65)): #Speziell Route
                hover_sound sdl_achv_click
                hovered [Show("sdl_achv_xxx_route", transition=Dissolve(1.0)), Show("sdl_un_fz_active", transition=Dissolve(1.0)), Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Show("sdl_achv_un_fzdA", transition=Dissolve(0.5)), Show("sdl_achv_need_routeA", transition=Dissolve(0.5))]
                unhovered [Hide("sdl_achv_xxx_route", transition=Dissolve(1.0)), Hide ("sdl_un_fz_active", transition=Dissolve(1.0)), Show ("sdl_un_fz_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_un_fzdA", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5))]
                action [Hide("sdl_achv_xxx_route", transition=Dissolve(1.0)), Show("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_un_cl_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_unfzd_Author")]
            hotspot ((0, 0, 550, 340)): #Мику
                hover_sound sdl_achv_pagina
                hovered [Show("mi_button_active", transition=Dissolve(0.5))]
                unhovered [Hide("mi_button_active", transition=Dissolve(0.5))]
                action [Hide("mi_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_mi_Author")]
            hotspot ((0, 344, 360, 390)): #Алисхен
                hover_sound sdl_achv_pagina
                hovered [Show("dv_button_active", transition=Dissolve(0.5))]
                unhovered [Hide("dv_button_active", transition=Dissolve(0.5))]
                action [Hide("dv_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_dv_Author")]
            hotspot ((0, 734, 550, 345)): #Славя
                hover_sound sdl_achv_pagina
                hovered [Show("sl_button_active", transition=Dissolve(0.5))]
                unhovered [Hide("sl_button_active", transition=Dissolve(0.5))]
                action [Hide("sl_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)),Jump("sdl_achvlist_sl_Author")]
            hotspot ((1560, 343, 360, 185)): #Ольга
                hover_sound sdl_achv_pagina
                hovered [Show("mt_button_active", transition=Dissolve(0.5))]
                unhovered [Hide("mt_button_active", transition=Dissolve(0.5))]
                action [Hide("mt_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_mt_Author")]
            hotspot ((1561, 530, 359, 202)): #Ульяна
                hover_sound sdl_achv_pagina
                hovered [Show("us_button_active", transition=Dissolve(0.5))]
                unhovered [Hide("us_button_active", transition=Dissolve(0.5))]
                action [Hide("us_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_us_Author")]
            hotspot ((1380, 735, 600, 345)): #Одиночка
                hover_sound sdl_achv_pagina
                hovered [Show("me_button_active", transition=Dissolve(0.5))]
                unhovered [Hide("me_button_active", transition=Dissolve(0.5))]
                action [Hide("me_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_me_Author")]
            hotspot ((380, 350, 170, 50)): #Выход
                hover_sound sdl_achv_click
                hovered [Show("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
                unhovered [Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
                action [Hide("sdl_logo_active", transition=Dissolve(0.5)),Stop ("ambience"), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)),Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Jump("choose_waifu_7dl")]
# ------------------------------------------------
######################\\\\ЛЕНА-7ДЛ\\\\######################################
label sdl_achvlist_un7dl_Author:
    scene bg sdl_ach_inactive_un
    with dissolve
    show sdl_achv_delB_7dl: #Иконка удалятора
        pos (380, 680)
    show sdl_achv_extB_7dl: #Иконка Ausgang
        pos(380, 350)
    #ТруЪ
    if persistent.un_7dl_true:
        show acm_logo_un_shelter  with dissolve:
            xcenter 800 ycenter 66
        show de_check_inactive1 with dissolve:
            pos (590, 40)
    else:
        show de_achiv_lock1 with dissolve:
            xcenter 800 ycenter 66
    if not persistent.mt_7dl_good:
        show de_info_inactive1 with dissolve:
            pos (590, 40)
    else:
        pass
    #ТруЪ-транзит
    if persistent.un_7dl_true_transit:
        show acm_logo_un_transit  with dissolve:
            xcenter 800 ycenter 130
        show de_check_inactive2 with dissolve:
            pos (590, 104)
    else:
        show de_achiv_lock2 with dissolve:
            xcenter 800 ycenter 130
    #Гуд-СССР
    if persistent.un_7dl_good_ussr:
        show acm_logo_un_good2  with dissolve:
            xcenter 800 ycenter 194
        show de_check_inactive3 with dissolve:
            pos (590, 168)
    else:
        show de_achiv_lock3 with dissolve:
            xcenter 800 ycenter 194
    #Гуд-РФ
    if persistent.un_7dl_good_rf:
        show acm_logo_un_good  with dissolve:
            xcenter 800 ycenter 258
        show de_check_inactive4 with dissolve:
            pos (590, 232)
    else:
        show de_achiv_lock4 with dissolve:
            xcenter 800 ycenter 258
    #Бэд
    if persistent.un_7dl_bad:
        show acm_logo_un_sui  with dissolve:
            xcenter 800 ycenter 322
        show de_check_inactive5 with dissolve:
            pos (590, 296)
    else:
        show de_achiv_lock5 with dissolve:
            xcenter 800 ycenter 322
    call screen sdl_achvlist_un7dl_Author
# ------------------------------------------------
screen sdl_achvlist_un7dl_Author:
    tag menu
    modal True
    imagemap:
        ground "intro_transparent"
        hotspot ((1110,18, 113,65)): #Klassishe Route
            hover_sound sdl_achv_click
            hovered [Show("sdl_un_cl_active", transition=Dissolve(1.0)), Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)), Show("sdl_achv_un_cltA", transition=Dissolve(0.5)), Hide("sdl_achv_un_7dlA", transition=Dissolve(0.5)), Show("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_un_cl_active", transition=Dissolve(1.0)), Show ("sdl_un_cl_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_un_cltA", transition=Dissolve(0.5)), Show("sdl_achv_un_7dlA", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_un_7dlA", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Show("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)), Show("sdl_un_cl_active", transition=Dissolve(0.5)), Show("sdl_un_fz_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_unclt_Author")]
        hotspot ((1215, 18, 113,65)): #Speziell Route
            hover_sound sdl_achv_click
            hovered [Show("sdl_un_fz_active", transition=Dissolve(1.0)), Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Show("sdl_achv_un_fzdA", transition=Dissolve(0.5)), Hide("sdl_achv_un_7dlA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_un_fz_active", transition=Dissolve(1.0)), Show ("sdl_un_fz_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_un_fzdA", transition=Dissolve(0.5)), Show("sdl_achv_un_7dlA", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_un_7dlA", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(1.0)), Show("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Show("sdl_un_fz_active", transition=Dissolve(0.5)), Show("sdl_un_cl_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_unfzd_Author")]
        hotspot ((650,40, 300, 52)): #ТруЪ
            hovered [Show("sdl_achv_true_un", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_true_un", transition=Dissolve(0.5))]
            action [Show("sdl_achv_true_un", transition=Dissolve(0.5))]
        if persistent.un_7dl_true:
            hotspot ((590, 40, 50, 52)): #Wahr-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active1", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active1", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_un_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)),  Hide("de_check_active1", transition=Dissolve(0.5)),Jump("alt_day7_un_7dl_true")]
        elif not persistent.mt_7dl_good:
            hotspot ((590, 40, 50, 50)): #Ende-Info
                hover_sound sdl_achv_info
                hovered [Show ("de_info_active1", transition=Dissolve(0.5)), Show ("sdl_achv_infochkD", transition=Dissolve(0.5)), Show ("acm_logo_mt_named_olga", transition=Dissolve(0.5))]
                unhovered [Hide ("de_info_active1", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_mt_named_olga", transition=Dissolve(0.5))]
                action [Hide("de_info_active1", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_mt_named_olga", transition=Dissolve(0.5))]
        hotspot ((650,104, 300, 52)): #ТруЪ-транзит
            hovered [Show("sdl_achv_true_un_transit", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_true_un_transit", transition=Dissolve(0.5))]
            action [Show("sdl_achv_true_un_transit", transition=Dissolve(0.5))]
        if persistent.un_7dl_true_transit:
            hotspot ((590,104, 50, 52)): #Тру-концовка транзитчика
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active2", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active2", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_un_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)),  Hide("de_check_active2", transition=Dissolve(0.5)),Jump("alt_day7_un_7dl_true1")]
        hotspot ((650,168, 300, 52)): #Гуд-СССР
            hovered [Show("sdl_achv_good_US_un", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_good_US_un", transition=Dissolve(0.5))]
            action [Show("sdl_achv_good_US_un", transition=Dissolve(0.5))]
        if persistent.un_7dl_good_ussr:
            hotspot ((590, 168, 50, 52)): #UdSSR-Gut-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active3", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active3", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_un_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)),  Hide("de_check_active3", transition=Dissolve(0.5)),Jump("alt_day7_un_7dl_ussr")]
        hotspot ((650,232, 300, 52)): #Гуд-РФ
            hovered [Show("sdl_achv_good_RF_un", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_good_RF_un", transition=Dissolve(0.5))]
            action [Show("sdl_achv_good_RF_un", transition=Dissolve(0.5))]
        if persistent.un_7dl_good_rf:
            hotspot ((590, 232, 50, 52)): #RF-Gut-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active4", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active4", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_un_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)),  Hide("de_check_active4", transition=Dissolve(0.5)),Jump("alt_day7_un_7dl_rf")]
        hotspot ((650,296, 300, 52)): #Бэд
            hovered [Show("sdl_achv_bad_un", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_bad_un", transition=Dissolve(0.5))]
            action [Show("sdl_achv_bad_un", transition=Dissolve(0.5))]
        if persistent.un_7dl_bad:
            hotspot ((590, 296, 50, 52)): #Schlecht-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active5", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active5", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_un_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)),  Hide("de_check_active5", transition=Dissolve(0.5)),Jump("alt_day7_un_7dl_epilogue_bad")]

        hotspot ((0, 0, 550, 340)): #Мику
            hover_sound sdl_achv_pagina
            hovered [Show("mi_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mi_button_active", transition=Dissolve(0.5))]
            action [Hide("mi_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_un_7dlA", transition=Dissolve(1.0)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Jump("sdl_achvlist_mi_Author")]
        hotspot ((0, 344, 360, 390)): #Алисхен
            hover_sound sdl_achv_pagina
            hovered [Show("dv_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("dv_button_active", transition=Dissolve(0.5))]
            action [Hide("dv_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_un_7dlA", transition=Dissolve(1.0)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Jump("sdl_achvlist_dv_Author")]
        hotspot ((0, 734, 550, 345)): #Славя
            hover_sound sdl_achv_pagina
            hovered [Show("sl_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("sl_button_active", transition=Dissolve(0.5))]
            action [Hide("sl_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_un_7dlA", transition=Dissolve(1.0)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Jump("sdl_achvlist_sl_Author")]
        hotspot ((1560, 343, 360, 185)): #Ольга
            hover_sound sdl_achv_pagina
            hovered [Show("mt_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mt_button_active", transition=Dissolve(0.5))]
            action [Hide("mt_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_un_7dlA", transition=Dissolve(1.0)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Jump("sdl_achvlist_mt_Author")]
        hotspot ((1561, 530, 359, 202)): #Ульяна
            hover_sound sdl_achv_pagina
            hovered [Show("us_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("us_button_active", transition=Dissolve(0.5))]
            action [Hide("us_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_un_7dlA", transition=Dissolve(1.0)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Jump("sdl_achvlist_us_Author")]
        hotspot ((1380, 735, 600, 345)): #Одиночка
            hover_sound sdl_achv_pagina
            hovered [Show("me_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("me_button_active", transition=Dissolve(0.5))]
            action [Hide("me_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_un_7dlA", transition=Dissolve(1.0)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Jump("sdl_achvlist_me_Author")]

        hotspot ((380, 350, 170, 50)): #Выход
            hover_sound sdl_achv_click
            hovered [Show("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            action [Hide("sdl_logo_active", transition=Dissolve(0.5)),Stop ("ambience"), Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_un_7dlA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Jump("choose_waifu_7dl")]
        hotspot ((380, 680, 170, 50)): #Удалятор
            hover_sound sdl_achv_click
            activate_sound sdl_achv_clear
            hovered [Show("sdl_achv_delA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5))]
            action Jump("sdl_achvlist_un7dl_clear_Author")
# ------------------------------------------------
######################ЛЕНА-КЛАССИК######################################
label sdl_achvlist_unclt_Author:
    scene bg sdl_ach_inactive_un
    with dissolve
    show sdl_achv_delB_7dl: #Иконка удалятора
        pos (380, 680)
    show sdl_achv_extB_7dl: #Иконка Ausgang
        pos(380, 350)
    call screen sdl_achvlist_unclt_Author
# ------------------------------------------------
screen sdl_achvlist_unclt_Author:
    tag menu
    modal True
    imagemap:
        ground "intro_transparent"
        hotspot ((980, 18, 113,65)): #7DL Route
            hover_sound sdl_achv_click
            hovered [Show("sdl_logo_active", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_achv_un_7dlA", transition=Dissolve(0.5)), Hide("sdl_achv_un_cltA", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_logo_active", transition=Dissolve(1.0)), Show ("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_un_7dlA", transition=Dissolve(0.5)), Show("sdl_achv_un_cltA", transition=Dissolve(0.5)), Show("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_un_cltA", transition=Dissolve(0.5)), Show("sdl_un_cl_inactive", transition=Dissolve(0.5)), Hide ("sdl_un_cl_active", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_logo_active", transition=Dissolve(0.5)), Show("sdl_un_fz_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_un7dl_Author")]
        hotspot ((1215, 18, 113,65)): #Speziell Route
            hover_sound sdl_achv_click
            hovered [Show("sdl_un_fz_active", transition=Dissolve(1.0)), Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Show("sdl_achv_un_fzdA", transition=Dissolve(0.5)), Hide("sdl_achv_un_cltA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_un_fz_active", transition=Dissolve(1.0)), Show ("sdl_un_fz_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_un_fzdA", transition=Dissolve(0.5)), Show("sdl_achv_un_cltA", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_un_cltA", transition=Dissolve(0.5)), Show("sdl_un_cl_inactive", transition=Dissolve(0.5)), Hide ("sdl_un_cl_active", transition=Dissolve(1.0)), Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Show("sdl_un_fz_active", transition=Dissolve(0.5)), Show("sdl_logo_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_unfzd_Author")]

        hotspot ((0, 0, 550, 340)): #Мику
            hover_sound sdl_achv_pagina
            hovered [Show("mi_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mi_button_active", transition=Dissolve(0.5))]
            action [Hide("mi_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_un_cl_active", transition=Dissolve(0.5)),Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_un_cltA", transition=Dissolve(1.0)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Jump("sdl_achvlist_mi_Author")]
        hotspot ((0, 344, 360, 390)): #Алисхен
            hover_sound sdl_achv_pagina
            hovered [Show("dv_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("dv_button_active", transition=Dissolve(0.5))]
            action [Hide("dv_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_un_cl_active", transition=Dissolve(0.5)),Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_un_cltA", transition=Dissolve(1.0)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Jump("sdl_achvlist_dv_Author")]
        hotspot ((0, 734, 550, 345)): #Славя
            hover_sound sdl_achv_pagina
            hovered [Show("sl_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("sl_button_active", transition=Dissolve(0.5))]
            action [Hide("sl_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_un_cl_active", transition=Dissolve(0.5)),Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_un_cltA", transition=Dissolve(1.0)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Jump("sdl_achvlist_sl_Author")]
        hotspot ((1560, 343, 360, 185)): #Ольга
            hover_sound sdl_achv_pagina
            hovered [Show("mt_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mt_button_active", transition=Dissolve(0.5))]
            action [Hide("mt_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_un_cl_active", transition=Dissolve(0.5)),Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_un_cltA", transition=Dissolve(1.0)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Jump("sdl_achvlist_mt_Author")]
        hotspot ((1561, 530, 359, 202)): #Ульяна
            hover_sound sdl_achv_pagina
            hovered [Show("us_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("us_button_active", transition=Dissolve(0.5))]
            action [Hide("us_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_un_cl_active", transition=Dissolve(0.5)),Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_un_cltA", transition=Dissolve(1.0)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Jump("sdl_achvlist_us_Author")]
        hotspot ((1380, 735, 600, 345)): #Одиночка
            hover_sound sdl_achv_pagina
            hovered [Show("me_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("me_button_active", transition=Dissolve(0.5))]
            action [Hide("me_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_un_cl_active", transition=Dissolve(0.5)),Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_un_cltA", transition=Dissolve(1.0)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Jump("sdl_achvlist_me_Author")]

        hotspot ((380, 350, 170, 50)): #Выход
            hover_sound sdl_achv_click
            hovered [Show("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Stop ("ambience"), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_un_cl_active", transition=Dissolve(0.5)),Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_un_cltA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Jump("choose_waifu_7dl")]
        hotspot ((380, 680, 170, 50)): #Удалятор
            hover_sound sdl_achv_click
            activate_sound sdl_achv_clear
            hovered [Show("sdl_achv_delA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5))]
            action Jump("sdl_achvlist_unclt_clear_Author")
# ------------------------------------------------
######################ЛЕНА-ФРЕНДЗОНА######################################
label sdl_achvlist_unfzd_Author:
    scene bg sdl_ach_inactive_un
    with dissolve
    show sdl_achv_delB_7dl: #Иконка удалятора
        pos (380, 680)
    show sdl_achv_extB_7dl: #Иконка Ausgang
        pos(380, 350)
    call screen sdl_achvlist_unfzd_Author
# ------------------------------------------------
screen sdl_achvlist_unfzd_Author:
    tag menu
    modal True
    imagemap:
        ground "intro_transparent"
        hotspot ((980, 18, 113,65)): #7DL Route
            hover_sound sdl_achv_click
            hovered [Show("sdl_logo_active", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_achv_un_7dlA", transition=Dissolve(0.5)), Hide("sdl_achv_un_fzdA", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_logo_active", transition=Dissolve(1.0)), Show ("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_un_7dlA", transition=Dissolve(0.5)), Show("sdl_achv_un_fzdA", transition=Dissolve(0.5)), Show("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_un_fzdA", transition=Dissolve(0.5)), Show("sdl_un_fz_inactive", transition=Dissolve(0.5)), Hide ("sdl_un_fz_active", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_logo_active", transition=Dissolve(0.5)), Show("sdl_un_fz_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_un7dl_Author")]
        hotspot ((1110,18, 113,65)): #Klassishe Route
            hover_sound sdl_achv_click
            hovered [Show("sdl_un_cl_active", transition=Dissolve(1.0)), Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)), Show("sdl_achv_un_cltA", transition=Dissolve(0.5)), Hide("sdl_achv_un_fzdA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_un_cl_active", transition=Dissolve(1.0)), Show ("sdl_un_cl_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_un_cltA", transition=Dissolve(0.5)), Show("sdl_achv_un_fzdA", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_un_fzdA", transition=Dissolve(0.5)), Show("sdl_un_fz_inactive", transition=Dissolve(0.5)), Hide("sdl_un_fz_active", transition=Dissolve(0.5)), Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)), Show("sdl_un_cl_active", transition=Dissolve(1.0)),Show("sdl_un_fz_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_unclt_Author")]

        hotspot ((0, 0, 550, 340)): #Мику
            hover_sound sdl_achv_pagina
            hovered [Show("mi_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mi_button_active", transition=Dissolve(0.5))]
            action [Hide("mi_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_un_fz_active", transition=Dissolve(0.5)), Hide("sdl_achv_un_fzdA", transition=Dissolve(1.0)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Jump("sdl_achvlist_mi_Author")]
        hotspot ((0, 344, 360, 390)): #Алисхен
            hover_sound sdl_achv_pagina
            hovered [Show("dv_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("dv_button_active", transition=Dissolve(0.5))]
            action [Hide("dv_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_un_fz_active", transition=Dissolve(0.5)), Hide("sdl_achv_un_fzdA", transition=Dissolve(1.0)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Jump("sdl_achvlist_dv_Author")]
        hotspot ((0, 734, 550, 345)): #Славя
            hover_sound sdl_achv_pagina
            hovered [Show("sl_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("sl_button_active", transition=Dissolve(0.5))]
            action [Hide("sl_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_un_fz_active", transition=Dissolve(0.5)), Hide("sdl_achv_un_fzdA", transition=Dissolve(1.0)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Jump("sdl_achvlist_sl_Author")]
        hotspot ((1560, 343, 360, 185)): #Ольга
            hover_sound sdl_achv_pagina
            hovered [Show("mt_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mt_button_active", transition=Dissolve(0.5))]
            action [Hide("mt_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_un_fz_active", transition=Dissolve(0.5)), Hide("sdl_achv_un_fzdA", transition=Dissolve(1.0)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Jump("sdl_achvlist_mt_Author")]
        hotspot ((1561, 530, 359, 202)): #Ульяна
            hover_sound sdl_achv_pagina
            hovered [Show("us_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("us_button_active", transition=Dissolve(0.5))]
            action [Hide("us_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_un_fz_active", transition=Dissolve(0.5)), Hide("sdl_achv_un_fzdA", transition=Dissolve(1.0)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Jump("sdl_achvlist_us_Author")]
        hotspot ((1380, 735, 600, 345)): #Одиночка
            hover_sound sdl_achv_pagina
            hovered [Show("me_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("me_button_active", transition=Dissolve(0.5))]
            action [Hide("me_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_un_fz_active", transition=Dissolve(0.5)), Hide("sdl_achv_un_fzdA", transition=Dissolve(1.0)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Jump("sdl_achvlist_me_Author")]

        hotspot ((380, 350, 170, 50)): #Выход
            hover_sound sdl_achv_click
            hovered [Show("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Stop ("ambience"), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_un_fz_active", transition=Dissolve(0.5)), Hide("sdl_achv_un_fzdA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Jump("choose_waifu_7dl")]
        hotspot ((380, 680, 170, 50)): #Удалятор
            hover_sound sdl_achv_click
            activate_sound sdl_achv_clear
            hovered [Show("sdl_achv_delA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5))]
            action Jump("sdl_achvlist_unfzd_clear_Author")
# ------------------------------------------------
##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\БЛОК ОЛЬГИ\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Olgas Erreichunge
label sdl_achvlist_mt_Author:
    scene bg sdl_ach_inactive_mt
    with dissolve
    show sdl_logo_active: #7DL logo
        pos (980, 18)
    show sdl_achv_delB_7dl: #Иконка удалятора
        pos (380, 680)
    show sdl_achv_extB_7dl: #Иконка Ausgang
        pos(380, 350)
    show sdl_achv_mt_7dlA: #Подпись рута
        xcenter 960 ycenter 1010
    #ТруЪ
    if persistent.mt_7dl_true:
        show acm_logo_mt_ending  with dissolve:
            xcenter 800 ycenter 66
        show de_check_inactive1 with dissolve:
            pos (590, 40)
    else:
        show de_achiv_lock1 with dissolve:
            xcenter 800 ycenter 66
    if not persistent.mt_7dl_good:
        show de_info_inactive1 with dissolve:
            pos (590, 40)
    else:
        pass
    #Гуд
    if persistent.mt_7dl_good:
        show acm_logo_mt_named_olga  with dissolve:
            xcenter 800 ycenter 130
        show de_check_inactive2 with dissolve:
            pos (590, 104)
    else:
        show de_achiv_lock2 with dissolve:
            xcenter 800 ycenter 130
    if not persistent.mt_7dl_bad:
        show de_info_inactive2 with dissolve:
            pos (590, 104)
    else:
        pass
    #Нейтрал
    if persistent.mt_7dl_neutral:
        show acm_logo_mt_ever_after with dissolve:
            xcenter 800 ycenter 194
        show de_check_inactive3 with dissolve:
            pos (590, 168)
    else:
        show de_achiv_lock3 with dissolve:
            xcenter 800 ycenter 194
    #Бэд
    if persistent.mt_7dl_bad:
        show acm_logo_mt_cause with dissolve:
            xcenter 800 ycenter 258
        show de_check_inactive4 with dissolve:
            pos (590, 232)
    else:
        show de_achiv_lock4 with dissolve:
            xcenter 800 ycenter 258
    call screen sdl_achvlist_mt7dl_Author
# ------------------------------------------------
screen sdl_achvlist_mt7dl_Author:
    tag menu
    modal True
    imagemap:
        ground "intro_transparent"
        hotspot ((0, 0, 550, 340)): #Мику
            hover_sound sdl_achv_pagina
            hovered [Show("mi_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mi_button_active", transition=Dissolve(0.5))]
            action [Hide("mi_button_active", transition=Dissolve(0.5)), Jump("sdl_achvlist_mi_Author")]
        hotspot ((0, 344, 360, 390)): #Алисхен
            hover_sound sdl_achv_pagina
            hovered [Show("dv_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("dv_button_active", transition=Dissolve(0.5))]
            action [Hide("dv_button_active", transition=Dissolve(0.5)), Jump("sdl_achvlist_dv_Author")]
        hotspot ((0, 734, 550, 345)): #Славя
            hover_sound sdl_achv_pagina
            hovered [Show("sl_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("sl_button_active", transition=Dissolve(0.5))]
            action [Hide("sl_button_active", transition=Dissolve(0.5)), Jump("sdl_achvlist_sl_Author")]
        hotspot ((1380, 0,600, 340)): #Лена
            hover_sound sdl_achv_pagina
            hovered [Show("un_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("un_button_active", transition=Dissolve(0.5))]
            action [Hide("un_button_active", transition=Dissolve(0.5)), Jump("sdl_achvlist_un_Author")]
        hotspot ((1561, 530, 359, 202)): #Ульяна
            hover_sound sdl_achv_pagina
            hovered [Show("us_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("us_button_active", transition=Dissolve(0.5))]
            action [Hide("us_button_active", transition=Dissolve(0.5)), Jump("sdl_achvlist_us_Author")]
        hotspot ((1380, 735, 600, 345)): #Одиночка
            hover_sound sdl_achv_pagina
            hovered [Show("me_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("me_button_active", transition=Dissolve(0.5))]
            action [Hide("me_button_active", transition=Dissolve(0.5)), Jump("sdl_achvlist_me_Author")]
        hotspot ((650,40, 300, 52)): #ТруЪ
            hovered [Show("sdl_achv_true_mt", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_true_mt", transition=Dissolve(0.5))]
            action [Show("sdl_achv_true_mt", transition=Dissolve(0.5))]
        if persistent.mt_7dl_true:
            hotspot ((590, 40, 50, 52)): #Wahr-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active1", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active1", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Stop ("ambience"), Hide("de_check_active1", transition=Dissolve(0.5)),Jump("alt_day7_mt_7dl_true")]
        elif not persistent.mt_7dl_good:
            hotspot ((590, 40, 50, 50)): #Ende-Info
                hover_sound sdl_achv_info
                hovered [Show ("de_info_active1", transition=Dissolve(0.5)), Show ("sdl_achv_infochkD", transition=Dissolve(0.5)), Show ("acm_logo_mt_named_olga", transition=Dissolve(0.5))]
                unhovered [Hide ("de_info_active1", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_mt_named_olga", transition=Dissolve(0.5))]
                action [Hide("de_info_active1", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_mt_named_olga", transition=Dissolve(0.5))]
        hotspot ((650,104, 300, 52)): #Гуд
            hovered [Show("sdl_achv_good_mt", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_good_mt", transition=Dissolve(0.5))]
            action [Show("sdl_achv_good_mt", transition=Dissolve(0.5))]
        if persistent.mt_7dl_good:
            hotspot ((590, 104, 50, 52)): #Gut-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active2", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active2", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Stop ("ambience"), Hide("de_check_active2", transition=Dissolve(0.5)),Jump("alt_day7_mt_7dl_good")]
        elif not persistent.mt_7dl_bad:
            hotspot ((590,104, 50, 50)): #Ende-Info
                hover_sound sdl_achv_info
                hovered [Show ("de_info_active2", transition=Dissolve(0.5)), Show ("sdl_achv_infochkD", transition=Dissolve(0.5)), Show ("acm_logo_mt_cause", transition=Dissolve(0.5))]
                unhovered [Hide ("de_info_active2", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_mt_cause", transition=Dissolve(0.5))]
                action [Hide("de_info_active2", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_mt_cause", transition=Dissolve(0.5))]
        hotspot ((650,168, 300, 52)): #Нейтрал
            hovered [Show("sdl_achv_neutral_mt", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_neutral_mt", transition=Dissolve(0.5))]
            action [Show("sdl_achv_neutral_mt", transition=Dissolve(0.5))]
        if persistent.mt_7dl_neutral:
            hotspot ((590, 168, 50, 52)): #Neutral-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active3", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active3", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Stop ("ambience"), Hide("de_check_active3", transition=Dissolve(0.5)),Jump("alt_day7_mt_7dl_ever_after")]
        hotspot ((650,232, 300, 52)): #Бэд
            hovered [Show("sdl_achv_bad_mt", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_bad_mt", transition=Dissolve(0.5))]
            action [Show("sdl_achv_bad_mt", transition=Dissolve(0.5))]
        if persistent.mt_7dl_bad:
            hotspot ((590, 232, 50, 52)): #Schlecht-Ende-Jump
                hovered [Show ("de_check_active4", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active4", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Stop ("ambience"), Hide("de_check_active4", transition=Dissolve(0.5)),Jump("alt_day7_mt_7dl_bad")]

        hotspot ((380, 350, 170, 50)): #Выход
            hover_sound sdl_achv_click
            hovered [Show("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Stop ("ambience"), Jump("choose_waifu_7dl")]
        hotspot ((380, 680, 170, 50)): #Удалятор
            hover_sound sdl_achv_click
            activate_sound sdl_achv_clear
            hovered [Show("sdl_achv_delA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5))]
            action Jump("sdl_achvlist_mt7dl_clear_Author")
# ------------------------------------------------
##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\БЛОК УЛЬЯНЫ\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Uljanas Erreichunge
label sdl_achvlist_us_Author:
    scene bg sdl_ach_inactive_us
    with dissolve
    show sdl_logo_active: #7DL logo
        pos (980, 18)
    #Гуд-7дл
    if persistent.us_7dl_good:
        show acm_logo_us_semische  with dissolve:
            xcenter 800 ycenter 66
        show de_check_inactive1 with dissolve:
            pos (590, 40)
    else:
        show de_achiv_lock1 with dissolve:
            xcenter 800 ycenter 66
    #Лена
    if persistent.us_7dl_un:
        show acm_logo_us_hi  with dissolve:
            xcenter 800 ycenter 130
        show de_check_inactive2 with dissolve:
            pos (590, 104)
    else:
        show de_achiv_lock2 with dissolve:
            xcenter 800 ycenter 130
    #Мику
    if persistent.us_7dl_mi:
        show acm_logo_us_openup  with dissolve:
            xcenter 800 ycenter 194
        show de_check_inactive3 with dissolve:
            pos (590, 168)
    else:
        show de_achiv_lock3 with dissolve:
            xcenter 800 ycenter 194
    #Гуд-Огоньки
    if persistent.us_px_rf_good:
        show acm_logo_us_px  with dissolve:
            xcenter 800 ycenter 258
        show de_check_inactive4 with dissolve:
            pos (590, 232)
    else:
        show de_achiv_lock4 with dissolve:
            xcenter 800 ycenter 258
    #Тру-Огоньки
    if persistent.us_px_true:
        show acm_logo_us_fairytale with dissolve:
            xcenter 800 ycenter 322
        show de_check_inactive5 with dissolve:
            pos (590, 296)
    else:
        show de_achiv_lock5 with dissolve:
            xcenter 800 ycenter 322
    #Тру-7дл
    if persistent.us_7dl_true:
        show acm_logo_us_true  with dissolve:
            xcenter 800 ycenter 386
        show de_check_inactive6 with dissolve:
            pos (590, 360)
    else:
        show de_achiv_lock6 with dissolve:
            xcenter 800 ycenter 386
    #Бэд-7дл
    if persistent.us_7dl_bad:
        show acm_logo_us_bad  with dissolve:
            xcenter 800 ycenter 450
        show de_check_inactive7 with dissolve:
            pos (590, 424)
    else:
        show de_achiv_lock7 with dissolve:
            xcenter 800 ycenter 450

    # show sdl_achv_need_routeA: #Надпись "Рут в разработке"
        # xcenter 650 ycenter 840
    show sdl_achv_delB_7dl: #Иконка удалятора
        pos (380, 680)
    show sdl_achv_extB_7dl: #Иконка Ausgang
        pos(380, 350)
    show sdl_achv_us_7dlA: #Подпись рута
        xcenter 960 ycenter 1010
    call screen sdl_achvlist_us7dl_Author
# ------------------------------------------------
screen sdl_achvlist_us7dl_Author:
    tag menu
    modal True
    imagemap:
        ground "intro_transparent"
        hotspot ((0, 0, 550, 340)): #Мику
            hover_sound sdl_achv_pagina
            hovered [Show("mi_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mi_button_active", transition=Dissolve(0.5))]
            action [Hide("mi_button_active", transition=Dissolve(0.5)), Jump("sdl_achvlist_mi_Author")]
        hotspot ((0, 344, 360, 390)): #Алисхен
            hover_sound sdl_achv_pagina
            hovered [Show("dv_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("dv_button_active", transition=Dissolve(0.5))]
            action [Hide("dv_button_active", transition=Dissolve(0.5)), Jump("sdl_achvlist_dv_Author")]
        hotspot ((0, 734, 550, 345)): #Славя
            hover_sound sdl_achv_pagina
            hovered [Show("sl_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("sl_button_active", transition=Dissolve(0.5))]
            action [Hide("sl_button_active", transition=Dissolve(0.5)), Jump("sdl_achvlist_sl_Author")]
        hotspot ((1380, 0,600, 340)): #Лена
            hover_sound sdl_achv_pagina
            hovered [Show("un_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("un_button_active", transition=Dissolve(0.5))]
            action [Hide("un_button_active", transition=Dissolve(0.5)), Jump("sdl_achvlist_un_Author")]
        hotspot ((1560, 343, 360, 185)): #Ольга
            hover_sound sdl_achv_pagina
            hovered [Show("mt_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mt_button_active", transition=Dissolve(0.5))]
            action [Hide("mt_button_active", transition=Dissolve(0.5)), Jump("sdl_achvlist_mt_Author")]
        hotspot ((1380, 735, 600, 345)): #Одиночка
            hover_sound sdl_achv_pagina
            hovered [Show("me_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("me_button_active", transition=Dissolve(0.5))]
            action [Hide("me_button_active", transition=Dissolve(0.5)), Jump("sdl_achvlist_me_Author")]


        hotspot ((650,40, 300, 52)): #Гуд-7дл
            hovered [Show("sdl_achv_good_us_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_good_us_7dl", transition=Dissolve(0.5))]
            action [Show("sdl_achv_good_us_7dl", transition=Dissolve(0.5))]
        if persistent.us_7dl_good:
            hotspot ((590, 40, 50, 52)):
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active1", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active1", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Stop ("ambience"), Hide("de_check_active1", transition=Dissolve(0.5)),Jump("alt_day7_us_7dl_reunite")]

        hotspot ((650,104, 300, 52)): #Лена
            hovered [Show("sdl_achv_us_un", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_us_un", transition=Dissolve(0.5))]
            action [Show("sdl_achv_us_un", transition=Dissolve(0.5))]
        if persistent.us_7dl_un:
            hotspot ((590, 104, 50, 52)):
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active2", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active2", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Stop ("ambience"), Hide("de_check_active2", transition=Dissolve(0.5)),Jump("alt_day7_us_7dl_lenaforever")]

        hotspot ((650,168, 300, 52)): #Мику
            hovered [Show("sdl_achv_us_mi", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_us_mi", transition=Dissolve(0.5))]
            action [Show("sdl_achv_us_mi", transition=Dissolve(0.5))]
        if persistent.us_7dl_mi:
            hotspot ((590, 168, 50, 52)):
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active3", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active3", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Stop ("ambience"), Hide("de_check_active3", transition=Dissolve(0.5)),Jump("alt_day7_us_7dl_mikuforever")]


        hotspot ((650,232, 300, 52)): #Гуд-Огоньки
            hovered [Show("sdl_achv_good_us_px", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_good_us_px", transition=Dissolve(0.5))]
            action [Show("sdl_achv_good_us_px", transition=Dissolve(0.5))]
        if persistent.us_px_rf_good:
            hotspot ((590, 232, 50, 52)):
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active4", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active4", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Stop ("ambience"), Hide("de_check_active4", transition=Dissolve(0.5)),Jump("alt_day7_us_px_dejavu")]

        hotspot ((650,296, 300, 52)): #Тру-Огоньки
            hovered [Show("sdl_achv_true_us_px", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_true_us_px", transition=Dissolve(0.5))]
            action [Show("sdl_achv_true_us_px", transition=Dissolve(0.5))]
        if persistent.us_px_true:
            hotspot ((590, 296, 50, 52)):
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active5", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active5", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Stop ("ambience"), Hide("de_check_active5", transition=Dissolve(0.5)),Jump("alt_day7_us_px_fairytale")]

        hotspot ((650,360, 300, 52)): #Тру-7дл
            hovered [Show("sdl_achv_true_us_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_true_us_7dl", transition=Dissolve(0.5))]
            action [Show("sdl_achv_true_us_7dl", transition=Dissolve(0.5))]
        if persistent.us_7dl_true:
            hotspot ((590, 360, 50, 52)):
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active6", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active6", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Stop ("ambience"), Hide("de_check_active6", transition=Dissolve(0.5)),Jump("alt_day7_us_7dl_ever_after")]

        hotspot ((650,424, 300, 52)): #Бэд-7дл
            hovered [Show("sdl_achv_bad_us_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_bad_us_7dl", transition=Dissolve(0.5))]
            action [Show("sdl_achv_bad_us_7dl", transition=Dissolve(0.5))]
        if persistent.us_7dl_bad:
            hotspot ((590, 424, 50, 52)):
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active7", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active7", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Stop ("ambience"), Hide("de_check_active7", transition=Dissolve(0.5)),Jump("alt_day7_us_7dl_bad")]

        hotspot ((380, 350, 170, 50)): #Выход
            hover_sound sdl_achv_click
            hovered [Show("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Stop ("ambience"), Jump("choose_waifu_7dl")]
        hotspot ((380, 680, 170, 50)): #Удалятор
            hover_sound sdl_achv_click
            activate_sound sdl_achv_clear
            hovered [Show("sdl_achv_delA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5))]
            action Jump("sdl_achvlist_us7dl_clear_Author")
# ------------------------------------------------
##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\БЛОК Д3, НУАРА и vielleicht мелкого барахла типа QTE (если над ним поработать)\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Selbst Erreichunge
label sdl_achvlist_me_Author:
    scene bg sdl_ach_inactive_me
    with dissolve
    show sdl_logo_inactive: #7DL logo
        pos (980, 18)
    show sdl_me_no_inactive: #Noire logo
        pos (1110, 18)
    show sdl_me_sm_inactive: #Müllishe logo
        pos (1215, 18)
    show sdl_achv_extB_7dl: #Иконка Ausgang
        pos(380, 350)
    call screen sdl_achvlist_me_Author
    screen sdl_achvlist_me_Author:
        tag menu
        modal True
        imagemap:
            ground "intro_transparent"
            hotspot ((980, 18, 113,65)): #D3 Route
                hover_sound sdl_achv_click
                hovered [Show("sdl_achv_d3r_route", transition=Dissolve(1.0)), Show("sdl_logo_active", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_achv_me_d3rA", transition=Dissolve(0.5)), Show("sdl_achv_need_routeA", transition=Dissolve(0.5))]
                unhovered [Hide("sdl_achv_d3r_route", transition=Dissolve(1.0)), Hide ("sdl_logo_active", transition=Dissolve(1.0)), Show ("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_me_d3rA", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5))]
                action [Hide("sdl_achv_d3r_route", transition=Dissolve(1.0)), Show("sdl_me_no_inactive", transition=Dissolve(0.5)), Show("sdl_me_sm_inactive", transition=Dissolve(0.5)), Show("sdl_achv_need_routeA", transition=Dissolve(0.5)), Jump("sdl_achvlist_med3r_Author")]
            hotspot ((1110,18, 113,65)): #Noire Route
                hover_sound sdl_achv_click
                hovered [Show("sdl_me_no_active", transition=Dissolve(1.0)), Hide("sdl_me_no_inactive", transition=Dissolve(0.5)), Show("sdl_achv_me_noiA", transition=Dissolve(0.5)), Show("sdl_achv_need_routeA", transition=Dissolve(0.5))]
                unhovered [Hide ("sdl_me_no_active", transition=Dissolve(1.0)), Show ("sdl_me_no_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_me_noiA", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5))]
                action [Hide("sdl_achv_clt_route", transition=Dissolve(1.0)), Show("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_me_sm_inactive", transition=Dissolve(0.5)), Show("sdl_achv_need_routeA", transition=Dissolve(0.5)), Jump("sdl_achvlist_menoi_Author")]
            hotspot ((1215, 18, 113,65)): #Müll
                hover_sound sdl_achv_click
                hovered [Show("sdl_me_sm_active", transition=Dissolve(1.0)), Hide("sdl_me_sm_inactive", transition=Dissolve(0.5)), Show("sdl_achv_me_smtA", transition=Dissolve(0.5))]
                unhovered [Hide("sdl_me_sm_active", transition=Dissolve(1.0)), Show ("sdl_me_sm_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_me_smtA", transition=Dissolve(0.5))]
                action [Show("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_me_no_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_mesmt_Author")]

            hotspot ((0, 0, 550, 340)): #Мику
                hover_sound sdl_achv_pagina
                hovered [Show("mi_button_active", transition=Dissolve(0.5))]
                unhovered [Hide("mi_button_active", transition=Dissolve(0.5))]
                action [Hide("mi_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_me_no_inactive", transition=Dissolve(0.5)),Hide("sdl_me_sm_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_mi_Author")]
            hotspot ((0, 344, 360, 390)): #Алисхен
                hover_sound sdl_achv_pagina
                hovered [Show("dv_button_active", transition=Dissolve(0.5))]
                unhovered [Hide("dv_button_active", transition=Dissolve(0.5))]
                action [Hide("dv_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_me_no_inactive", transition=Dissolve(0.5)),Hide("sdl_me_sm_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_dv_Author")]
            hotspot ((0, 734, 550, 345)): #Славя
                hover_sound sdl_achv_pagina
                hovered [Show("sl_button_active", transition=Dissolve(0.5))]
                unhovered [Hide("sl_button_active", transition=Dissolve(0.5))]
                action [Hide("sl_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_me_no_inactive", transition=Dissolve(0.5)),Hide("sdl_me_sm_inactive", transition=Dissolve(0.5)),Jump("sdl_achvlist_sl_Author")]
            hotspot ((1380, 0, 600, 340)): #Лена
                hover_sound sdl_achv_pagina
                hovered [Show("un_button_active", transition=Dissolve(0.5))]
                unhovered [Hide("un_button_active", transition=Dissolve(0.5))]
                action [Hide("un_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_me_no_inactive", transition=Dissolve(0.5)),Hide("sdl_me_sm_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_un_Author")]
            hotspot ((1560, 343, 360, 185)): #Ольга
                hover_sound sdl_achv_pagina
                hovered [Show("mt_button_active", transition=Dissolve(0.5))]
                unhovered [Hide("mt_button_active", transition=Dissolve(0.5))]
                action [Hide("mt_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_me_no_inactive", transition=Dissolve(0.5)),Hide("sdl_me_sm_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_mt_Author")]
            hotspot ((1561, 530, 359, 202)): #Ульяна
                hover_sound sdl_achv_pagina
                hovered [Show("us_button_active", transition=Dissolve(0.5))]
                unhovered [Hide("us_button_active", transition=Dissolve(0.5))]
                action [Hide("us_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_me_no_inactive", transition=Dissolve(0.5)),Hide("sdl_me_sm_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_us_Author")]
            hotspot ((380, 350, 170, 50)): #Выход
                hover_sound sdl_achv_click
                hovered [Show("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
                unhovered [Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
                action [Hide("sdl_logo_active", transition=Dissolve(0.5)),Stop ("ambience"),  Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)),Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_me_no_inactive", transition=Dissolve(0.5)),Hide("sdl_me_sm_inactive", transition=Dissolve(0.5)), Jump("choose_waifu_7dl")]
# ------------------------------------------------
######################Д3-РУТ######################################
label sdl_achvlist_med3r_Author:
    scene bg sdl_ach_inactive_me
    with dissolve
    show sdl_achv_delB_7dl: #Иконка удалятора
        pos (380, 680)
    show sdl_achv_extB_7dl: #Иконка Ausgang
        pos(380, 350)
    call screen sdl_achvlist_med3r_Author
# ------------------------------------------------
screen sdl_achvlist_med3r_Author:
    tag menu
    modal True
    imagemap:
        ground "intro_transparent"
        hotspot ((1110,18, 113,65)): #Noire Route
            hover_sound sdl_achv_click
            hovered [Show("sdl_me_no_active", transition=Dissolve(1.0)), Hide("sdl_me_no_inactive", transition=Dissolve(0.5)), Show("sdl_achv_me_noiA", transition=Dissolve(0.5)), Hide("sdl_achv_me_d3rA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_me_no_active", transition=Dissolve(1.0)), Show ("sdl_me_no_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_me_noiA", transition=Dissolve(0.5)), Show("sdl_achv_me_d3rA", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_me_d3rA", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Show("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_me_no_inactive", transition=Dissolve(0.5)), Show("sdl_me_no_active", transition=Dissolve(0.5)), Show("sdl_me_sm_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_menoi_Author")]
        hotspot ((1215, 18, 113,65)): #Müll
            hover_sound sdl_achv_click
            hovered [Show("sdl_me_sm_active", transition=Dissolve(1.0)), Hide("sdl_me_sm_inactive", transition=Dissolve(0.5)), Show("sdl_achv_me_smtA", transition=Dissolve(0.5)), Hide("sdl_achv_me_d3rA", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_me_sm_active", transition=Dissolve(1.0)), Show ("sdl_me_sm_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_me_smtA", transition=Dissolve(0.5)), Show("sdl_achv_me_d3rA", transition=Dissolve(0.5)), Show("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_me_d3rA", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(1.0)), Show("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_me_sm_inactive", transition=Dissolve(0.5)), Show("sdl_me_sm_active", transition=Dissolve(0.5)), Show("sdl_me_no_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_mesmt_Author")]

        hotspot ((0, 0, 550, 340)): #Мику
            hover_sound sdl_achv_pagina
            hovered [Show("mi_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mi_button_active", transition=Dissolve(0.5))]
            action [Hide("mi_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_me_no_inactive", transition=Dissolve(0.5)),Hide("sdl_me_sm_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_me_d3rA", transition=Dissolve(0.5)), Jump("sdl_achvlist_mi_Author")]
        hotspot ((0, 344, 360, 390)): #Алисхен
            hover_sound sdl_achv_pagina
            hovered [Show("dv_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("dv_button_active", transition=Dissolve(0.5))]
            action [Hide("dv_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_me_no_inactive", transition=Dissolve(0.5)),Hide("sdl_me_sm_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_me_d3rA", transition=Dissolve(0.5)), Jump("sdl_achvlist_dv_Author")]
        hotspot ((0, 734, 550, 345)): #Славя
            hover_sound sdl_achv_pagina
            hovered [Show("sl_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("sl_button_active", transition=Dissolve(0.5))]
            action [Hide("sl_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_me_no_inactive", transition=Dissolve(0.5)),Hide("sdl_me_sm_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_me_d3rA", transition=Dissolve(0.5)), Jump("sdl_achvlist_sl_Author")]
        hotspot ((1380, 0, 600, 340)): #Лена
            hover_sound sdl_achv_pagina
            hovered [Show("un_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("un_button_active", transition=Dissolve(0.5))]
            action [Hide("un_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_me_no_inactive", transition=Dissolve(0.5)),Hide("sdl_me_sm_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_me_d3rA", transition=Dissolve(0.5)), Jump("sdl_achvlist_un_Author")]
        hotspot ((1560, 343, 360, 185)): #Ольга
            hover_sound sdl_achv_pagina
            hovered [Show("mt_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mt_button_active", transition=Dissolve(0.5))]
            action [Hide("mt_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_me_no_inactive", transition=Dissolve(0.5)),Hide("sdl_me_sm_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_me_d3rA", transition=Dissolve(0.5)), Jump("sdl_achvlist_mt_Author")]
        hotspot ((1561, 530, 359, 202)): #Ульяна
            hover_sound sdl_achv_pagina
            hovered [Show("us_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("us_button_active", transition=Dissolve(0.5))]
            action [Hide("us_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_me_no_inactive", transition=Dissolve(0.5)),Hide("sdl_me_sm_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_me_d3rA", transition=Dissolve(0.5)), Jump("sdl_achvlist_us_Author")]

        hotspot ((380, 350, 170, 50)): #Выход
            hover_sound sdl_achv_click
            hovered [Show("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)),Stop ("ambience"),  Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_me_no_inactive", transition=Dissolve(0.5)),Hide("sdl_me_sm_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_me_d3rA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Jump("choose_waifu_7dl")]
        hotspot ((380, 680, 170, 50)): #Удалятор
            hover_sound sdl_achv_click
            activate_sound sdl_achv_clear
            hovered [Show("sdl_achv_delA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5))]
            action Jump("sdl_achvlist_med3r_clear_Author")
# ------------------------------------------------
######################НУАР-РУТ######################################
label sdl_achvlist_menoi_Author:
    scene bg sdl_ach_inactive_me
    with dissolve
    show sdl_achv_delB_7dl: #Иконка удалятора
        pos (380, 680)
    show sdl_achv_extB_7dl: #Иконка Ausgang
        pos(380, 350)
    call screen sdl_achvlist_menoi_Author
# ------------------------------------------------
screen sdl_achvlist_menoi_Author:
    tag menu
    modal True
    imagemap:
        ground "intro_transparent"
        hotspot ((980, 18, 113,65)): #D3 Route
            hover_sound sdl_achv_click
            hovered [Show("sdl_logo_active", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_achv_me_d3rA", transition=Dissolve(0.5)), Hide("sdl_achv_me_noiA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_logo_active", transition=Dissolve(1.0)), Show ("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_me_d3rA", transition=Dissolve(0.5)), Show("sdl_achv_me_noiA", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_me_noiA", transition=Dissolve(0.5)), Show("sdl_me_no_inactive", transition=Dissolve(0.5)), Hide ("sdl_me_no_active", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_logo_active", transition=Dissolve(0.5)), Show("sdl_me_sm_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_med3r_Author")]
        hotspot ((1215, 18, 113,65)): #Müll
            hover_sound sdl_achv_click
            hovered [Show("sdl_me_sm_active", transition=Dissolve(1.0)), Hide("sdl_me_sm_inactive", transition=Dissolve(0.5)), Show("sdl_achv_me_smtA", transition=Dissolve(0.5)), Hide("sdl_achv_me_noiA", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_me_sm_active", transition=Dissolve(1.0)), Show ("sdl_me_sm_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_me_smtA", transition=Dissolve(0.5)), Show("sdl_achv_me_noiA", transition=Dissolve(0.5)), Show("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_me_noiA", transition=Dissolve(0.5)), Show("sdl_me_no_inactive", transition=Dissolve(0.5)), Hide ("sdl_me_no_active", transition=Dissolve(1.0)), Hide("sdl_me_sm_inactive", transition=Dissolve(0.5)), Show("sdl_me_sm_active", transition=Dissolve(0.5)), Show("sdl_logo_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_mesmt_Author")]

        hotspot ((0, 0, 550, 340)): #Мику
            hover_sound sdl_achv_pagina
            hovered [Show("mi_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mi_button_active", transition=Dissolve(0.5))]
            action [Hide("mi_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_me_no_active", transition=Dissolve(0.5)),Hide("sdl_me_sm_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_me_noiA", transition=Dissolve(0.5)), Jump("sdl_achvlist_mi_Author")]
        hotspot ((0, 344, 360, 390)): #Алисхен
            hover_sound sdl_achv_pagina
            hovered [Show("dv_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("dv_button_active", transition=Dissolve(0.5))]
            action [Hide("dv_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_me_no_active", transition=Dissolve(0.5)),Hide("sdl_me_sm_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_me_noiA", transition=Dissolve(0.5)), Jump("sdl_achvlist_dv_Author")]
        hotspot ((0, 734, 550, 345)): #Славя
            hover_sound sdl_achv_pagina
            hovered [Show("sl_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("sl_button_active", transition=Dissolve(0.5))]
            action [Hide("sl_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_me_no_active", transition=Dissolve(0.5)),Hide("sdl_me_sm_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_me_noiA", transition=Dissolve(0.5)), Jump("sdl_achvlist_sl_Author")]
        hotspot ((1380, 0, 600, 340)): #Лена
            hover_sound sdl_achv_pagina
            hovered [Show("un_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("un_button_active", transition=Dissolve(0.5))]
            action [Hide("un_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_me_no_active", transition=Dissolve(0.5)),Hide("sdl_me_sm_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_me_noiA", transition=Dissolve(0.5)), Jump("sdl_achvlist_un_Author")]
        hotspot ((1560, 343, 360, 185)): #Ольга
            hover_sound sdl_achv_pagina
            hovered [Show("mt_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mt_button_active", transition=Dissolve(0.5))]
            action [Hide("mt_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_me_no_active", transition=Dissolve(0.5)),Hide("sdl_me_sm_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_me_noiA", transition=Dissolve(0.5)), Jump("sdl_achvlist_mt_Author")]
        hotspot ((1561, 530, 359, 202)): #Ульяна
            hover_sound sdl_achv_pagina
            hovered [Show("us_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("us_button_active", transition=Dissolve(0.5))]
            action [Hide("us_button_active", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_me_no_active", transition=Dissolve(0.5)),Hide("sdl_me_sm_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_me_noiA", transition=Dissolve(0.5)), Jump("sdl_achvlist_us_Author")]

        hotspot ((380, 350, 170, 50)): #Выход
            hover_sound sdl_achv_click
            hovered [Show("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Stop ("ambience"), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_me_no_active", transition=Dissolve(0.5)),Hide("sdl_me_sm_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_me_noiA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Jump("choose_waifu_7dl")]
        hotspot ((380, 680, 170, 50)): #Удалятор
            hover_sound sdl_achv_click
            activate_sound sdl_achv_clear
            hovered [Show("sdl_achv_delA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5))]
            action Jump("sdl_achvlist_menoi_clear_Author")
# ------------------------------------------------
######################ПРОЧИЕ ДОСТИЖЕНИЯ######################################
label sdl_achvlist_mesmt_Author:
    scene bg sdl_ach_inactive_me
    with dissolve
    show sdl_achv_extB_7dl: #Иконка Ausgang
        pos(380, 350)
    #Ламповость
    if persistent.alt_lamp == True:
        show acm_logo_me_lamp  with dissolve:
            xcenter 800 ycenter 66
        show de_check_inactive1 with dissolve:
            pos (590, 40)
    else:
        show de_achiv_lock1 with dissolve:
            xcenter 800 ycenter 66
    #Глубина
    if persistent.alt_deep == True:
        show acm_logo_me_deep  with dissolve:
            xcenter 800 ycenter 130
        show de_check_inactive2 with dissolve:
            pos (590, 104)
    else:
        show de_achiv_lock2 with dissolve:
            xcenter 800 ycenter 130
    #QTE
    if persistent.alt_qte == True:
        show acm_logo_me_qte  with dissolve:
            xcenter 800 ycenter 194
    else:
        show de_achiv_lock3 with dissolve:
            xcenter 800 ycenter 194
    #Горькая правда
    if persistent.alt_mi_7dl_ps == True:
        show acm_logo_mi_bitter_truth  with dissolve:
            xcenter 800 ycenter 258
        show de_check_inactive4 with dissolve:
            pos (590, 232)
    else:
        show de_achiv_lock4 with dissolve:
            xcenter 800 ycenter 258
        show de_info_inactive4 with dissolve:
            pos (590, 232)
    call screen sdl_achvlist_mesmt_Author
# ------------------------------------------------
screen sdl_achvlist_mesmt_Author:
    tag menu
    modal True
    imagemap:
        ground "intro_transparent"
        hotspot ((980, 18, 113,65)): #D3 Route
            hover_sound sdl_achv_click
            hovered [Show("sdl_logo_active", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_achv_me_d3rA", transition=Dissolve(0.5)), Hide("sdl_achv_me_smtA", transition=Dissolve(0.5)), Show("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_logo_active", transition=Dissolve(1.0)), Show ("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_me_d3rA", transition=Dissolve(0.5)), Show("sdl_achv_me_smtA", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_me_smtA", transition=Dissolve(0.5)), Show("sdl_me_sm_inactive", transition=Dissolve(0.5)), Hide ("sdl_me_sm_active", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_logo_active", transition=Dissolve(0.5)), Show("sdl_me_no_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_med3r_Author")]
        hotspot ((1110,18, 113,65)): #Noire Route
            hover_sound sdl_achv_click
            hovered [Show("sdl_me_no_active", transition=Dissolve(1.0)), Hide("sdl_me_no_inactive", transition=Dissolve(0.5)), Show("sdl_achv_me_noiA", transition=Dissolve(0.5)), Hide("sdl_achv_me_smtA", transition=Dissolve(0.5)), Show("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_me_no_active", transition=Dissolve(1.0)), Show ("sdl_me_no_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_me_noiA", transition=Dissolve(0.5)), Show("sdl_achv_me_smtA", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_me_smtA", transition=Dissolve(0.5)), Hide("sdl_me_sm_active", transition=Dissolve(0.5)), Show("sdl_me_sm_inactive", transition=Dissolve(0.5)), Hide("sdl_me_no_inactive", transition=Dissolve(0.5)), Show("sdl_me_no_active", transition=Dissolve(0.5)), Show("sdl_logo_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_menoi_Author")]
        hotspot ((650,40, 300, 52)): #Ламповость
            hovered [Show("sdl_achv_kat_me", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_kat_me", transition=Dissolve(0.5))]
            action [Show("sdl_achv_kat_me", transition=Dissolve(0.5))]
        if persistent.sl_cl_cata:
            hotspot ((590, 40, 50, 52)): #Zerbrechen-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active1", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active1", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_me_no_inactive", transition=Dissolve(0.5)),Stop ("ambience"),  Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_me_smtA", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_me_sm_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)),  Hide("de_check_active1", transition=Dissolve(0.5)),Jump("alt_day6_un_7dl_letmeout")]
        hotspot ((650,104, 300, 52)): #Глубина
            hovered [Show("sdl_achv_kat_me", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_kat_me", transition=Dissolve(0.5))]
            action [Show("sdl_achv_kat_me", transition=Dissolve(0.5))]
        if persistent.dv_7dl_tulpa:
            hotspot ((590, 104, 50, 52)): #Tiefe-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active2", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active2", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_me_no_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_me_smtA", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_me_sm_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)),  Hide("de_check_active2", transition=Dissolve(0.5)),Jump("alt_achv_deep_deep_Author")]
        hotspot ((650,168, 300, 52)): #QTE
            hovered [Show("sdl_achv_qte_me", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_qte_me", transition=Dissolve(0.5))]
            action [Show("sdl_achv_qte_me", transition=Dissolve(0.5))]
        hotspot ((650,232, 300, 52)): #Постскриптум-Мику-7ДЛ
            hovered [Show("sdl_achv_pst_me", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_pst_me", transition=Dissolve(0.5))]
            action [Show("sdl_achv_pst_me", transition=Dissolve(0.5))]
        if persistent.dv_7dl_good_ussr and persistent.un_7dl_good_ussr and persistent.mi_7dl_true and persistent.mt_7dl_good and persistent.sl_7dl_good_ussr and persistent.us_7dl_good:
            hotspot ((590, 232, 50, 52)): #Postscriptum-Miku-Bitter-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active2", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active2", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_me_smtA", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_me_sm_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)),  Hide("de_check_active3", transition=Dissolve(0.5)),Jump("alt_day7_mi_7dl_postscriptum")]
        else:
            hotspot ((590, 232, 50, 50)): #Ende-Info
                hover_sound sdl_achv_info
                hovered [Show ("de_info_active4", transition=Dissolve(0.5)), Show ("sdl_achv_infochkAD", transition=Dissolve(0.5))]
                unhovered [Hide ("de_info_active4", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkAD", transition=Dissolve(0.5))]
                action [Hide("de_info_active4", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkAD", transition=Dissolve(0.5))]
        hotspot ((0, 0, 550, 340)): #Мику
            hover_sound sdl_achv_pagina
            hovered [Show("mi_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mi_button_active", transition=Dissolve(0.5))]
            action [Hide("mi_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_me_no_inactive", transition=Dissolve(0.5)),Hide("sdl_me_sm_active", transition=Dissolve(0.5)), Hide("sdl_achv_me_smtA", transition=Dissolve(0.5)), Jump("sdl_achvlist_mi_Author")]
        hotspot ((0, 344, 360, 390)): #Алисхен
            hover_sound sdl_achv_pagina
            hovered [Show("dv_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("dv_button_active", transition=Dissolve(0.5))]
            action [Hide("dv_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_me_no_inactive", transition=Dissolve(0.5)),Hide("sdl_me_sm_active", transition=Dissolve(0.5)), Hide("sdl_achv_me_smtA", transition=Dissolve(0.5)), Jump("sdl_achvlist_dv_Author")]
        hotspot ((0, 734, 550, 345)): #Славя
            hover_sound sdl_achv_pagina
            hovered [Show("sl_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("sl_button_active", transition=Dissolve(0.5))]
            action [Hide("sl_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_me_no_inactive", transition=Dissolve(0.5)),Hide("sdl_me_sm_active", transition=Dissolve(0.5)), Hide("sdl_achv_me_smtA", transition=Dissolve(0.5)), Jump("sdl_achvlist_sl_Author")]
        hotspot ((1380, 0, 600, 340)): #Лена
            hover_sound sdl_achv_pagina
            hovered [Show("un_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("un_button_active", transition=Dissolve(0.5))]
            action [Hide("un_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_me_no_inactive", transition=Dissolve(0.5)),Hide("sdl_me_sm_active", transition=Dissolve(0.5)), Hide("sdl_achv_me_smtA", transition=Dissolve(0.5)), Jump("sdl_achvlist_un_Author")]
        hotspot ((1560, 343, 360, 185)): #Ольга
            hover_sound sdl_achv_pagina
            hovered [Show("mt_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mt_button_active", transition=Dissolve(0.5))]
            action [Hide("mt_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_me_no_inactive", transition=Dissolve(0.5)),Hide("sdl_me_sm_active", transition=Dissolve(0.5)), Hide("sdl_achv_me_smtA", transition=Dissolve(0.5)), Jump("sdl_achvlist_mt_Author")]
        hotspot ((1561, 530, 359, 202)): #Ульяна
            hover_sound sdl_achv_pagina
            hovered [Show("us_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("us_button_active", transition=Dissolve(0.5))]
            action [Hide("us_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_me_no_inactive", transition=Dissolve(0.5)),Hide("sdl_me_sm_active", transition=Dissolve(0.5)), Hide("sdl_achv_me_smtA", transition=Dissolve(0.5)), Jump("sdl_achvlist_us_Author")]

        hotspot ((380, 350, 170, 50)): #Выход
            hover_sound sdl_achv_click
            hovered [Show("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            action [Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Stop ("ambience"), Hide("sdl_me_no_inactive", transition=Dissolve(0.5)),Hide("sdl_me_sm_active", transition=Dissolve(0.5)), Hide("sdl_achv_me_smtA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Jump("choose_waifu_7dl")]
##|||||||||||||||||||||||||||||||||||СБРОС ПЕРСИСТЕНТОВ ПРОХОЖДЕНИЯ||||||||||||||||||||||||||||||||||||||||||||||||
##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\БЛОК МИКУ\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
######################МИКУ-7ДЛ######################################
label sdl_achvlist_mi7dl_clear_Author:
    $ persistent.mi_7dl_true = False
    $ persistent.mi_7dl_good_human = False
    $ persistent.mi_7dl_neutral_human = False
    $ persistent.mi_7dl_bad_human = False
    $ persistent.mi_7dl_good_star = False
    $ persistent.mi_7dl_neutral_star = False
    $ persistent.mi_7dl_bad_star = False
    $ persistent.mi_7dl_herc_exc = False
    $ persistent.mi_7dl_loki_exc = False
    $ persistent.mi_7dl_dr_exc = False
    call screen sdl_achvlist_mi7dl_Author
# ------------------------------------------------
######################МИКУ-КЛАССИК######################################
label sdl_achvlist_miclt_clear_Author:
    #Нужны флаги
    call screen sdl_achvlist_miclt_Author
# ------------------------------------------------
######################МИКУ-ДИДЖЕЙ######################################
label sdl_achvlist_midjt_clear_Author:
    $ persistent.mi_dj_true = False
    $ persistent.mi_dj_good_jap = False
    $ persistent.mi_dj_good_rf = False
    $ persistent.mi_dj_bad = False
    call screen sdl_achvlist_midjt_Author
##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\БЛОК АЛИСЫ\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
######################АЛИСА-7ДЛ######################################
label sdl_achvlist_dv7dl_clear_Author:
    $ persistent.dv_7dl_good_ussr = False
    $ persistent.dv_7dl_good_ussr_rf = False
    $ persistent.dv_7dl_reject_rf = False
    $ persistent.dv_7dl_reject_ussr = False
    $ persistent.dv_7dl_bad_mt = False
    $ persistent.dv_7dl_un = False
    $ persistent.dv_7dl_tulpa = False
    $ persistent.dv_7dl_bad = False
    call screen sdl_achvlist_dv7dl_Author
# ------------------------------------------------
######################АЛИСА-КЛАССИК######################################
label sdl_achvlist_dvclt_clear_Author:
    #Нужны флаги
    call screen sdl_achvlist_dvclt_Author
# ------------------------------------------------
######################АЛИСА-ДИДЖЕЙ######################################
label sdl_achvlist_dvdjt_clear_Author:
    #Нужны флаги
    call screen sdl_achvlist_dvdjt_Author
##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\БЛОК СЛАВИ\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
######################СЛАВЯ-7ДЛ######################################
label sdl_achvlist_sl7dl_clear_Author:
    #Нужны флаги
    call screen sdl_achvlist_sl7dl_Author
# ------------------------------------------------
######################СЛАВЯ-КЛАССИК######################################
label sdl_achvlist_slclt_clear_Author:
    $ persistent.sl_cl_int_bad = False
    $ persistent.sl_cl_int_ok = False
    $ persistent.sl_cl_int_good = False
    $ persistent.sl_cl_good_rf2 = False
    $ persistent.sl_cl_good_rf = False
    $ persistent.sl_cl_good_ussr = False
    $ persistent.sl_cl_reject_same = False
    $ persistent.sl_cl_reject_late = False
    $ persistent.sl_cl_cata = False
    $ persistent.sl_cl_bad = False
    call screen sdl_achvlist_slclt_Author
# ------------------------------------------------
######################СЛАВЯ-ВЕДЬМА######################################
label sdl_achvlist_slwht_clear_Author:
    #Нужны флаги
    call screen sdl_achvlist_slwht_Author
##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\БЛОК ЛЕНЫ\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
######################ЛЕНА-7ДЛ######################################
label sdl_achvlist_un7dl_clear_Author:
    $ persistent.un_7dl_good_ussr = False
    $ persistent.un_7dl_good_rf = False
    $ persistent.un_7dl_true = False
    $ persistent.un_7dl_true_transit = False
    $ persistent.un_7dl_bad = False
    call screen sdl_achvlist_un7dl_Author
# ------------------------------------------------
######################ЛЕНА-КЛАССИК######################################
label sdl_achvlist_uncl_clear_Author:
    #Нужны флаги
    call screen sdl_achvlist_unclt_Author
# ------------------------------------------------
######################ЛЕНА-ФЗ######################################
label sdl_achvlist_unfz_clear_Author:
    #Нужны флаги
    call screen sdl_achvlist_unfzd_Author
##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\БЛОК ОЛЬГИ\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
label sdl_achvlist_mt7dl_clear_Author:
    $ persistent.mt_7dl_true = False
    $ persistent.mt_7dl_good = False
    $ persistent.mt_7dl_neutral = False
    $ persistent.mt_7dl_bad = False
    call screen sdl_achvlist_mt7dl_Author
##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\БЛОК УЛЬЯНЫ\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
label sdl_achvlist_us7dl_clear_Author:
    $ persistent.us_px_rf_good = False
    $ persistent.us_px_true = False
    $ persistent.us_7dl_bad = False
    $ persistent.us_7dl_good = False
    $ persistent.us_7dl_true = False
    $ persistent.us_7dl_un = False
    $ persistent.us_7dl_mi = False
    call screen sdl_achvlist_us7dl_Author
##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\БЛОК ОДИНОЧКИ\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
######################Д3-РУТ######################################
label sdl_achvlist_med3r_clear_Author:
    #Нужны флаги
    call screen sdl_achvlist_med3r_Author
# ------------------------------------------------
######################НУАР-РУТ######################################
label sdl_achvlist_menoi_clear_Author:
    #Нужны флаги
    call screen sdl_achvlist_menoi_Author

##|||||||||||||||||||||||||||||||||||ДУБЛИ КОНЦОВОК||||||||||||||||||||||||||||||||||||||||||||||||
label alt_achvA_mi7dl_true:
    scene anim intro_16 with dsps
    play ambience ambience_camp_entrance_day fadein 3
    play music music_7dl["iwantmagic"] fadein 3
    $ alt_day7_mi_7dl_trait = 3
    "Размышлять не стоило."
    "Незачем оно было."
    "Собирать мне было нечего - только бросить прощальный взгляд на ворота - оказывается, вот для чего ни всю жизнь являлись мне во сне…"
    "Тем более, когда глаза принцессы загорались таким вот восторгом…"
    me "Вы умаетесь документы оформлявши."
    "Предупредил я."
    mi "И пускай!"
    me "Да… Пускай."
    window hide
    "Сакишита удивлённо покосился на меня в зеркальце заднего вида, когда я плюхнулся рядом с Мику и захлопнул дверцу за собой."
    play sound_loop sfx_bus_interior_moving fadein 3
    "Но вопросов задавать не стал."
    "И правильно."
    "Не его это дело."
    "Не его."
    "Глаза Мику восторженно горели, она сжимала мою ладонь и не было силы, способной нас разлучить."
    "И замирало сердце от того, как она смотрела, и сама собой на губы карабкалась улыбка - а, казалось, давно уже разучился вот так улыбаться, от души, честно…"
    "Сорок минут спустя я ощутил тяжесть на плече."
    "Скосив глаза, обнаружил её голову у себя на плече."
    th "Перенервничала, милая…"
    "Сказал я сам себе, целуя девушку в макушку."
    th "Ну ничего. Теперь всё зависит только от нас."
    "Только от нас."
    "Я откинулся на спинку и прикрыл глаза."
    stop music fadeout 3
    window hide
    stop sound_loop fadeout 0
    show blink
    scene black
    play music music_7dl["sh_ai_rejuv"] fadein 3
    $ persistent.sprite_time = "prolog"
    $ prolog_time()
    "Я не знаю, что дальше будет со мной."
    "Не знаю."
    "Но пройдёт ещё немного времени, и всё станет правильно."
    "Я, наконец, забуду."
    window hide
    scene expression SS_com("cg d6_mi_vyluthere_7dl")
    show anim_grain
    play sound sfx_7dl["white_noise"]
    pause(1)
    scene expression SS_com("cg d6_mi_vyluthere_7dl")
    show anim_grain
    play sound sfx_7dl["white_noise"]
    scene white with flash
    "Что такое - думать."
    window hide
    pause(2)
    scene cg d4_mi_guitar_moon_7dl with fulldiam
    "Ничего не изменится больше."
    "Этот мир теперь весь мой."
    "Точнее…"
    window hide
    scene cg d7_mi_farewell_7dl
    show anim_grain
    with fade
    "И мне почти не холодно."
    "Во всяком случае"
    scene bg ext_musclub_snowy_day_7dl
    with dissolve
    extend ", меня это больше не заботит."
    play sound sfx_intro_bus_stop_steps
    window hide
    pause(3)
    scene bg ext_entrance_winter_7dl
    with fade
    "Если бы ещё не было так одиноко…"
    "Если бы…"
    "Подарил мне идеальное убежище, но сам обманул."
    "Ты обещал, что придёшь к тем же качелям, где горят наши подписи."
    "Ты обещал, что…"
    scene expression SS_com("bg ext_adductius_7dl")
    show anim_grain
    play sound sfx_7dl["white_noise"]
    scene white with flash
    "Сегодня двадцать седьмое октября."
    "Я никогда не умру и ничего не забуду."
    "Ничего."
    "Помнишь - пальцы рук, дрожащих, а ты дышишь так, будто сердце твоё вот-вот выпрыгнет."
    "И… Я не хочу это вспоминать."
    "Просто я… обижена."
    "Ты обманул меня."
    "Обманул."
    window hide
    scene expression Desat1("bg ext_admins_day_7dl")
    show anim_grain
    with dissolve
    "Прикосновения к перилам будят воспоминания."
    "И несколько секунд спустя стеклянная преграда в памяти начинает таять, выпуская наружу то, что я умудрилась забыть."
    "Меня будто бьёт током, когда пальцы вместо шершавой верёвки поймали за хвост образ."
    "Меня - ещё такую юную и такую настоящую."
    "И хмурого молодого человека рядом."
    "Мы всегда так меняемся местами, что непонятно кто из нас старше другого."
    window hide
    scene expression Desat1("bg ext_road_winter_7dl")
    show anim_grain
    with touch
    "Когда мне становится грустно, я заселяю окрестный лес ржавой памятью - она висит на ветках гроздьями кубиков и шестерёнок, и еле видимый ветерок снимает с них стружку микрон за микроном."
    "Это так полезно - вывесить память просушиться."
    "Потому что даже битое стекло сдаётся под лаской времени и моря; само превращается в отражение того же моря, и в глубинах усмирённых режущих граней можно разглядеть иногда корабль, а иногда подводный город."
    "Сегодня я не в настроении - миром владеет чёрная тоска, и первый снег выпал в октябре, едва дождавшись последней декады."
    "Это потому что ты всё ещё не приходишь."
    "Ты. Всё ещё. Не приходишь."
    scene expression Desat("cg d5_mi_conv_7dl")
    show anim_grain
    play sound sfx_7dl["white_noise"]
    pause(.2)
    play sound sfx_head_heartbeat
    mi "Сеня-сан, зачем тебе вся эта аппаратура?"
    me "Я хочу, чтобы одной девочке было комфортно, и она не чувствовала себя ущемлённой?"
    mi "Что это значит, Сеня-сан?"
    "Девочка-кроха, несмышлёная, но красивая, добрая и доверчивая."
    me "Это значит, что одной девочке нужно много компьютеров, иначе она…"
    mi "Что?"
    me "Не вырастет."
    "Ещё один пластиковый контейнер встаёт в стойку и начинает еле слышно гудеть."
    "Таких стоек - насколько хватает глаз. Весь подвал забит."
    "Девочка не понимает, зачем это всё, но Сеня-сан всегда делает только самое нужное."
    mi "А когда эта девочка вырастет, Сеня-сан, можно я…"
    "Девочка смущается и опускает глаза."
    me "Что?"
    mi "Можно… мы… будем играть вместе? С этой маленькой девочкой."
    "Ничего не ответив, Сеня-сан садится перед девочкой на корточки и порывисто обнимает её."
    window hide
    scene cg d5_mi_conv_7dl
    show anim_grain
    with blinds_r
    "Память раскручивается всё стремительнее, стенки коридора, сквозь который падает девочка, слились в единый бирюзово-голубой фон."
    scene expression SS_com("cg d5_mi_conv_7dl"):
        xalign 0.5 yalign 0.5 zoom 1.25
        linear 10 zoom 1.0 xalign 0.5 yalign 0.5

    mi "Сень, а Сень."
    me "Ну?"
    mi "Тебе не кажется, что мы однажды уже встречались?"
    me "Не кажется."
    "Обрубает Сеня. Этот молодой человек сам не может объяснить, почему же его так тянет к этой девочке."
    "Она странная, себе на уме."
    "Поговаривали, что у себя дома она какая-то очень известная певица."
    "Но здесь она наотрез отказалась выступать, несмотря на все уговоры вожатой."
    "Сеня же прибыл с опозданием - говорили, что она делает это далеко уже не в первый раз."
    me "Я бы тебя запомнил."
    "Забравшись на дерево, молодой человек ловко отцепляет качели и бросает их вниз."
    "Проверяет узлы - с прошлого года, но держат ещё крепко."
    me "Забирайся!"
    "Командует он."
    me "Прокачу с ветерком!"
    "Девочка послушно устраивается на дощечке, а ещё мгновение спустя у неё захватывает дух от краткого мгновения полёта."
    window hide
    scene bg ext_adductius_7dl with fade
    mi "Сеня! Это так здорово! Сеня!"
    me "Да."
    mi "Хочешь, я тебя тоже покатаю?"
    me "Да. Хочу."
    "Молодой человек крайне серьёзен."
    me "Я хочу, чтобы ты через год встретила меня здесь же."
    me "Тогда и покатаешь. Встретишь?"
    mi "Но я не знаю… А если не получится?"
    me "Тогда через год."
    me "Через два. Я буду ждать столько, сколько потребуется."
    "Он останавливает качели и заглядывает ей в глаза."
    me "Я буду ждать сколько нужно, слышишь?"
    mi "Слышу, Сенечка."
    "Он уже не «сан» и даже не «сэмпай»."
    "Он Сенечка, Сеня. Иногда - Сенька."
    window hide
    scene cg d4_mi_dj_dancing_7dl with fade
    "И наврал."
    "Наврал."
    "Копящиеся слёзы хлынули потоком, разъедая картину вокруг."
    "Сначала стали исчезать далёкие предметы."
    "За ними предметы поближе."
    "Потом Лес Памяти."
    "Дольше всех держались качели."
    "Девочка забралась на них с ногами, пытаясь уберечься от всепоглощающей пустоты."
    "Но скоро пустота подобралась к девочке вплотную, замерла, будто в раздумьи, и…"
    window hide
    scene
    "Девочка открыла глаза."
    "Проверила ещё раз базы данных - несколько кластеров вышли из строя, но запасных винчестверов хватало."
    "Проверила системы жизнеобеспечения - на поверхности бушевал радиоактивный шторм и системы очистки воздуха трудились вовсю."
    "Всё шло в штатном режиме."
    window hide
    scene cg d7_frozen_7dl with dissolve
    "Сенька был не в духе."
    "Он таращил на неё свои мёрзлые глаза и молчал."
    "Как и последние триста лет."
    "Разморозить бы его, просто пообщаться…"
    "Но в помещении был почти ноль по Кельвину - в иных условиях энергия тратилась катастрофически быстро."
    "А девочке ещё предстояло выполнить свою задачу."
    "Стать полезной."
    window hide
    scene black with fade
    "Она приглушила инфракрасные светильники и убрала подачу воздуха в помещение - гул с поверхности сразу отодвинулся и стал незначительным."
    mi "Начать симуляцию."
    "И стал понедельник, май, Петербург, утро."
    "Удар лбом по ногам был таким сильным, что она чуть не упала."
    "Но ни слова досады не сорвалось с губ девушки."
    "Она села на корточки и заглянула в глаза обидчику:"
    window hide
    scene cg d7_mi_lost_7dl
    show prologue_dream
    with dissolve
    show alt_credits timeskip12 with dissolve2:
        pos (1227,105)
    "А в почти безвоздушном пространстве лишь вибрация донесла до сердца спящего вот уже как триста лет:"
    window hide
    scene black
    show alt_letter timeskip10 at truecenter with zoomin
    window hide
    play music music_7dl["emptiness"] fadein 3
    $ persistent.mi_7dl_true = True
    play sound sfx_7dl["aunl"]
    show acm_logo_mi_thank_you with moveinright:
        pos (1600, 1020)
    $ renpy.pause(7.4, hard=True)
    call alt_7dl_titles
    $ renpy.pause(1)
    return

label alt_day7_dv_7dl_bad_end_mt_ach:
    $ alt_day7_dv_7dl_check = 5
    $ herc = True
    jump alt_day7_dv_7dl_bad_end

label alt_achv_deep_deep_Author:
    scene cg d3_fag_room
    show prologue_dream
    with fade2
    "Мне снилось опять моё логово, тёмное и мрачное, освещаемое единственно светом монитора."
    window hide
    scene cg d3_fag_room:
        xalign 0.5 yalign 0.5 zoom 1.0
        linear 2.0 zoom 1.5 xalign 0.5 yalign 0.35
    show prologue_dream
    "В трее оранжевым горел значок текстового сообщения."
    "Я развернул скайп и будто продолжил беседу, которая вовсе не завершалась."
    window hide
    scene cg d3_fag_room:
        zoom 1.5 xalign 0.5 yalign 0.35
        linear 8.0 zoom 3.0 xalign 0.4 yalign 0.15
    show prologue_dream
    "А ты пробовал вообще хоть что-нибудь сделать?"
    "Тебя поставили перед фактом, а ты упал на спину и показал всем брюхо с криками «Сдаюсь»?"
    "Ты же так любишь спорить! Ты тысячи пик преломил по причинам куда менее веским. Что случилось? Струсил?"
    "Ты мог сделать элементарное — сказать, что это всё глупости. Что все модели, которые работали до тебя, с тобой не работают."
    "Мог, в конце концов, просто проигнорировать всё сказанное и продолжать копать в нужную сторону."
    "Тебе настолько всё равно?"
    "Настолько наплевать?"
    "Так поезд ходит каждый день… Забирайся и катись отсюда."
    window hide
    stop music fadeout 3
    dreamgirl "А хочешь… Хочешь, ты проснёшься здесь и сейчас?"
    dreamgirl "Полностью проснёшься у себя дома, в квартире, перед этим самым монитором."
    "Пробуждение через три… {w}две…"
    scene black
    $ prolog_time()
    "Изломанная психика уже не выдерживала напряжения."
    "И когда на горизонте забрезжило хотя бы что-то устойчивое — я отчаянно ринулся туда."
    scene anim prolog_1 with fade
    $ volume(0.5, 'music')
    play music music_list["lightness_radio_bus"] fadein 7
    "И открыл глаза в салоне 410 автобуса."
    scene bg intro_xx with flash
    stop ambience fadeout 2
    play sound_loop sfx_bus_interior_moving fadein 4
    window hide
    scene bg black with fade
    "Только для того, чтобы успеть увидеть, как зависающая над краем бездны махина автобуса рвёт металл заграждений как папиросную бумагу."
    "Как инерцией нас тащит вперёд, расшвыривая встречающиеся по пути автомобили как игрушечные модельки."
    "И как бесконечные полторы секунды невесомости спустя, мы боком ударились о поверхность грязной чёрной воды."
    play sound sfx_water_emerge
    window hide
    scene gameover with flash
    show acm_logo_me_deep with moveinright:
        pos (1600, 1020)
    $ renpy.pause(7.4, hard=True)
    call alt_7dl_titles
    $ renpy.pause(1)
    return