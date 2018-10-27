label scenario__sdl_achvlist_Author:
    $ day_time()
    $ persistent.sprite_time = "day"
    $ plthr = u"Достижения"
    play ambience ambience_7dl["safe"] fadein 5
        
# ------------------------------------------------
# Показываем первоначальный фон
    scene bg sdl_ach_inactive
    show sdl_achv_extB_7dl: #Иконка Ausgang  
        pos(380, 350)
    $ renpy.block_rollback()
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
    add "de_info_active3" pos (590, 168)
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
screen acm_logo_sl_radio:
    add "acm_logo_sl_radio" xcenter 750 ycenter 860
screen acm_logo_sl_am_home:
    add "acm_logo_sl_am_home" xcenter 750 ycenter 860
screen acm_logo_sl_neon:
    add "acm_logo_sl_neon" xcenter 750 ycenter 860
screen acm_logo_sl_right_road:
    add "acm_logo_sl_right_road" xcenter 750 ycenter 860
screen acm_logo_sl_dr_un:
    add "acm_logo_sl_dr_un" xcenter 750 ycenter 860
screen acm_logo_sl_wasted:
    add "acm_logo_sl_wasted" xcenter 750 ycenter 860
screen acm_logo_sl_fantazm:
    add "acm_logo_sl_fantazm" xcenter 750 ycenter 860
screen acm_logo_sl_good:
    add "acm_logo_sl_good" xcenter 750 ycenter 860
screen acm_logo_mi_sparkle:
    add "acm_logo_mi_sparkle" xcenter 750 ycenter 860
screen acm_logo_mi_watashi:
    add "acm_logo_mi_watashi" xcenter 750 ycenter 860
screen acm_logo_us_px:
    add "acm_logo_us_px" xcenter 750 ycenter 860
screen acm_logo_us_hi:
    add "acm_logo_us_hi" xcenter 750 ycenter 860
screen acm_logo_us_semische:
    add "acm_logo_us_semische" xcenter 750 ycenter 860
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
    
#Ульяна
#Огоньки
screen sdl_us_px_active:
    add "sdl_us_px_active" pos (1110,18)
screen sdl_us_px_inactive:
    add "sdl_us_px_inactive" pos (1110,18)
    
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

screen sdl_achv_us_pxsA:#Ульяна
    add "sdl_achv_us_pxsA" xcenter 960 ycenter 1010
screen sdl_achv_us_7dlA:
    add "sdl_achv_us_7dlA" xcenter 960 ycenter 1010

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
screen sdl_achv_tran_HE_dv:
    add "sdl_achv_tran_HE_dv" xcenter 700 ycenter 840
    
#Надписи концовок Славя
screen sdl_achv_true_sl:
    add "sdl_achv_true_sl" xcenter 700 ycenter 840
screen sdl_achv_true_IN_sl:
    add "sdl_achv_true_IN_sl" xcenter 700 ycenter 840
screen sdl_achv_bad_IN_sl:
    add "sdl_achv_bad_IN_sl" xcenter 700 ycenter 840
screen sdl_achv_bad_sl:
    add "sdl_achv_bad_sl" xcenter 700 ycenter 840
screen sdl_achv_excl_LO_sl:
    add "sdl_achv_excl_LO_sl" xcenter 700 ycenter 840
screen sdl_achv_good_LO_sl:
    add "sdl_achv_good_LO_sl" xcenter 700 ycenter 840
screen sdl_achv_neutral_LO_sl:
    add "sdl_achv_neutral_LO_sl" xcenter 700 ycenter 840
screen sdl_achv_rejc_LO_sl:
    add "sdl_achv_rejc_LO_sl" xcenter 700 ycenter 840
screen sdl_achv_good_HE_sl:
    add "sdl_achv_good_HE_sl" xcenter 700 ycenter 840
screen sdl_achv_good_DR_sl:
    add "sdl_achv_good_DR_sl" xcenter 700 ycenter 840
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
screen sdl_achv_true_us:
    add "sdl_achv_true_us" xcenter 700 ycenter 840
screen sdl_achv_good_us:
    add "sdl_achv_good_us" xcenter 700 ycenter 840
screen sdl_achv_bad_us:
    add "sdl_achv_bad_us" xcenter 700 ycenter 840
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
            action [Hide("sdl_logo_active", transition=Dissolve(0.5)),Stop ("ambience"), Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Jump("main_menu_7dl")]
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
                action [Hide("sl_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_sl_Author")]
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
                action [Hide("sdl_logo_active", transition=Dissolve(0.5)),Stop ("ambience"),Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Jump("main_menu_7dl")]
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
            action [Hide("sdl_achv_mi_7dlA", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Show("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Show("sdl_mi_cl_active", transition=Dissolve(0.5)), Jump("sdl_achvlist_miclt_Author")]
        hotspot ((1215, 18, 113,65)): #Speziell Route
            hover_sound sdl_achv_click
            hovered [Show("sdl_mi_dj_active", transition=Dissolve(1.0)), Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Show("sdl_achv_mi_djtA", transition=Dissolve(0.5)), Hide("sdl_achv_mi_7dlA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_mi_dj_active", transition=Dissolve(1.0)), Show ("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_mi_djtA", transition=Dissolve(0.5)), Show("sdl_achv_mi_7dlA", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_mi_7dlA", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(1.0)), Show("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Show("sdl_mi_dj_active", transition=Dissolve(0.5)), Jump("sdl_achvlist_midjt_Author")]
        hotspot ((650,40, 300, 52)): #ТруЪ-энд
            hovered [Show("sdl_achv_true_mi", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_true_mi", transition=Dissolve(0.5))]
            action [Show("sdl_achv_true_mi", transition=Dissolve(0.5))]
        if persistent.mi_7dl_true:
            hotspot ((590, 40, 50, 52)): #Wahr-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active1", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active1", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active1", transition=Dissolve(0.5)), Replay("alt_day7_mi_7dl_thank_you", scope={"alt_replay_on" : "True"}, locked=False)]
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
                action [Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active2", transition=Dissolve(0.5)), Replay("alt_day7_mi_7dl_dark_dreams", scope={"alt_replay_on" : "True"}, locked=False)]
        hotspot ((650,168, 300, 52)): #Гуд-S      
            hovered [Show("sdl_achv_good_RF_mi", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_good_RF_mi", transition=Dissolve(0.5))]
            action [Show("sdl_achv_good_RF_mi", transition=Dissolve(0.5))] 
        if persistent.mi_7dl_good_star:
            hotspot ((590, 168, 50, 52)): #RF-Gut-S-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active3", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active3", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active3", transition=Dissolve(0.5)), Replay("alt_day7_mi_7dl_sparkle", scope={"alt_replay_on" : "True"}, locked=False)]
        hotspot ((650,232, 300, 52)): #Эксклюзив-Дрищ
            hovered [Show("sdl_achv_excl_DR_mi", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_excl_DR_mi", transition=Dissolve(0.5))]
            action [Show("sdl_achv_excl_DR_mi", transition=Dissolve(0.5))] 
        if persistent.mi_7dl_dr_exc:
            hotspot ((590, 232, 50, 52)): #Speziel-DR-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active4", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active4", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active4", transition=Dissolve(0.5)), Replay("alt_day7_mi_7dl_come_back", scope={"alt_replay_on" : "True"}, locked=False)]
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
                action [Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active5", transition=Dissolve(0.5)), Replay("alt_day7_mi_7dl_sinthetic", scope={"alt_replay_on" : "True"}, locked=False)]
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
                action [Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active6", transition=Dissolve(0.5)), Replay("alt_day7_mi_7dl_unlike", scope={"alt_replay_on" : "True"}, locked=False)]
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
                action [Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)),Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active7", transition=Dissolve(0.5)), Replay("alt_day7_mi_7dl_happy_again", scope={"alt_replay_on" : "True"}, locked=False)]
        hotspot ((650,488, 300, 52)): #Нейтрал-S
            hovered [Show("sdl_achv_neutral_mi", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_neutral_mi", transition=Dissolve(0.5))]
            action [Show("sdl_achv_neutral_mi", transition=Dissolve(0.5))]  
        if persistent.mi_7dl_neutral_star:
            hotspot ((590, 488, 50, 52)): #Neutral-S-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active8", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active8", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active8", transition=Dissolve(0.5)), Replay("alt_day7_mi_7dl_club27", scope={"alt_replay_on" : "True"}, locked=False)]
        hotspot ((650,552, 300, 52)): #Бэд-M       
            hovered [Show("sdl_achv_bad_mi", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_bad_mi", transition=Dissolve(0.5))]
            action [Show("sdl_achv_bad_mi", transition=Dissolve(0.5))]  
        if persistent.mi_7dl_bad_human:
            hotspot ((590, 552, 50, 52)): #schlecht-M-Ende-Jump
                hovered [Show ("de_check_active9", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active9", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active9", transition=Dissolve(0.5)), Replay("alt_day7_mi_7dl_liar", scope={"alt_replay_on" : "True"}, locked=False)]
        hotspot ((650,616, 300, 52)): #Бэд-S      
            hovered [Show("sdl_achv_bad_mi", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_bad_mi", transition=Dissolve(0.5))]
            action [Show("sdl_achv_bad_mi", transition=Dissolve(0.5))]  
        if persistent.mi_7dl_bad_star:
            hotspot ((590, 616, 50, 52)): #schlecht-S-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active10", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active10", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active10", transition=Dissolve(0.5)), Replay("alt_day7_mi_7dl_dam_CPU", scope={"alt_replay_on" : "True"}, locked=False)]
        
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
            action [Hide("sdl_logo_active", transition=Dissolve(0.5)),Stop ("ambience"), Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Jump("main_menu_7dl")]
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
            action [Hide("sdl_achv_mi_cltA", transition=Dissolve(0.5)), Show("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Hide ("sdl_mi_cl_active", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_logo_active", transition=Dissolve(0.5)), Jump("sdl_achvlist_mi7dl_Author")]
        hotspot ((1215, 18, 113,65)): #Speziell Route
            hover_sound sdl_achv_click
            hovered [Show("sdl_mi_dj_active", transition=Dissolve(1.0)), Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Show("sdl_achv_mi_djtA", transition=Dissolve(0.5)), Hide("sdl_achv_mi_cltA", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_mi_dj_active", transition=Dissolve(1.0)), Show ("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_mi_djtA", transition=Dissolve(0.5)), Show("sdl_achv_mi_cltA", transition=Dissolve(0.5)), Show("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_mi_cltA", transition=Dissolve(0.5)), Show("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Hide ("sdl_mi_cl_active", transition=Dissolve(1.0)), Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Show("sdl_mi_dj_active", transition=Dissolve(0.5)), Jump("sdl_achvlist_midjt_Author")]
        
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
            action [Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Stop ("ambience"), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_cl_active", transition=Dissolve(0.5)),Hide("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_mi_cltA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Jump("main_menu_7dl")]
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
            action [Hide("sdl_achv_mi_djtA", transition=Dissolve(0.5)), Show("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide ("sdl_mi_dj_active", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_logo_active", transition=Dissolve(0.5)), Jump("sdl_achvlist_mi7dl_Author")]
        hotspot ((1110,18, 113,65)): #Klassishe Route
            hover_sound sdl_achv_click
            hovered [Show("sdl_mi_cl_active", transition=Dissolve(1.0)), Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Show("sdl_achv_mi_cltA", transition=Dissolve(0.5)), Hide("sdl_achv_mi_djtA", transition=Dissolve(0.5)), Show("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_mi_cl_active", transition=Dissolve(1.0)), Show ("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_mi_cltA", transition=Dissolve(0.5)), Show("sdl_achv_mi_djtA", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_mi_djtA", transition=Dissolve(0.5)), Show("sdl_mi_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_mi_dj_active", transition=Dissolve(0.5)), Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Show("sdl_mi_cl_active", transition=Dissolve(1.0)), Jump("sdl_achvlist_miclt_Author")]
        hotspot ((650,40, 300, 52)): #ТруЪ-энд
            hovered [Show("sdl_achv_true_mi", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_true_mi", transition=Dissolve(0.5))]
            action [Show("sdl_achv_true_mi", transition=Dissolve(0.5))]
        if persistent.mi_dj_true:
            hotspot ((590, 40, 50, 52)): #Wahr-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active1", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active1", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_mi_djtA", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_mi_dj_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active1", transition=Dissolve(0.5)), Replay("alt_day7_mi_dj_true_end", scope={"alt_replay_on" : "True"}, locked=False)]
        hotspot ((650,104, 300, 52)): #Гуд-Япония
            hovered [Show("sdl_achv_good_mi", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_good_mi", transition=Dissolve(0.5))]
            action [Show("sdl_achv_good_mi", transition=Dissolve(0.5))] 
        if persistent.mi_dj_good_jap:
            hotspot ((590, 104, 50, 52)): #Gut-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active2", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active2", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_mi_djtA", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_mi_dj_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active2", transition=Dissolve(0.5)), Replay("alt_day7_mi_dj_jp_good_end", scope={"alt_replay_on" : "True"}, locked=False)]
        hotspot ((650,168, 300, 52)): #Гуд-РФ      
            hovered [Show("sdl_achv_good_RF_mi", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_good_RF_mi", transition=Dissolve(0.5))]
            action [Show("sdl_achv_good_RF_mi", transition=Dissolve(0.5))] 
        if persistent.mi_dj_good_rf:
            hotspot ((590, 168, 50, 52)): #RF-Gut-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active3", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active3", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_mi_djtA", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_mi_dj_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active3", transition=Dissolve(0.5)), Replay("alt_day7_mi_dj_rf_good_end", scope={"alt_replay_on" : "True"}, locked=False)]
        hotspot ((650,232, 300, 52)): #Бэд
            hovered [Show("sdl_achv_bad_mi", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_bad_mi", transition=Dissolve(0.5))]
            action [Show("sdl_achv_bad_mi", transition=Dissolve(0.5))] 
        if persistent.mi_dj_bad:
            hotspot ((590, 232, 50, 52)): #schlecht-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active4", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active4", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_mi_djtA", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_mi_dj_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active4", transition=Dissolve(0.5)), Replay("alt_day7_mi_dj_bad_end", scope={"alt_replay_on" : "True"}, locked=False)]
        
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
            action [Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Stop ("ambience"), Hide("sdl_mi_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_mi_dj_active", transition=Dissolve(0.5)), Hide("sdl_achv_mi_djtA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Jump("main_menu_7dl")]
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
                action [Hide("sl_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_sl_Author")]
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
                action [Hide("sdl_logo_active", transition=Dissolve(0.5)),Stop ("ambience"), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Jump("main_menu_7dl")]
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
                action [Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_dv_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active1", transition=Dissolve(0.5)), Replay("alt_day7_dv_7dl_ussr_epilogue", scope={"alt_replay_on" : "True"}, locked=False)]
        hotspot ((650,104, 300, 52)): #Гуд-РФ
            hovered [Show("sdl_achv_good_RF_dv", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_good_RF_dv", transition=Dissolve(0.5))]
            action [Show("sdl_achv_good_RF_dv", transition=Dissolve(0.5))] 
        if persistent.dv_7dl_good_ussr_rf:
            hotspot ((590, 104, 50, 52)): #RF-Gut-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active2", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active2", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_dv_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active2", transition=Dissolve(0.5)), Replay("alt_day7_dv_7dl_rf_epilogue", scope={"alt_replay_on" : "True"}, locked=False)]
        hotspot ((650,168, 300, 52)): #Реджект-РФ     
            hovered [Show("sdl_achv_rejc_RF_dv", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_rejc_RF_dv", transition=Dissolve(0.5))]
            action [Show("sdl_achv_rejc_RF_dv", transition=Dissolve(0.5))] 
        if persistent.dv_7dl_reject_rf:
            hotspot ((590, 168, 50, 52)): #RF-Reject-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active3", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active3", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_dv_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active3", transition=Dissolve(0.5)), Replay("alt_day7_dv_7dl_rej_rf_end", scope={"alt_replay_on" : "True"}, locked=False)]
        hotspot ((650,232, 300, 52)): #Реджект-СССР
            hovered [Show("sdl_achv_rejc_US_dv", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_rejc_US_dv", transition=Dissolve(0.5))]
            action [Show("sdl_achv_rejc_US_dv", transition=Dissolve(0.5))] 
        if persistent.dv_7dl_reject_ussr:
            hotspot ((590, 232, 50, 52)): #UdSSR-Reject-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active4", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active4", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_dv_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active4", transition=Dissolve(0.5)), Replay("alt_day7_dv_7dl_rej_ussr_end", scope={"alt_replay_on" : "True"}, locked=False)]
        hotspot ((650,296, 300, 52)): #Транзит-Ольга
            hovered [Show("sdl_achv_tran_HE_dv", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_tran_HE_dv", transition=Dissolve(0.5))]
            action [Show("sdl_achv_tran_HE_dv", transition=Dissolve(0.5))]
        if persistent.dv_7dl_bad_mt:
            hotspot ((590, 296, 50, 52)): #Transit-MT-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active5", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active5", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_dv_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active5", transition=Dissolve(0.5)), SetVariable("alt_day7_dv_7dl_check", 5), SetVariable("herc", "True"), Replay("alt_day7_dv_7dl_bad_end", scope={"alt_replay_on" : "True"}, locked=False)]
        hotspot ((650,360, 300, 52)): #Транзит-Лена       
            hovered [Show("sdl_achv_tran_dv", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_tran_dv", transition=Dissolve(0.5))]
            action [Show("sdl_achv_tran_dv", transition=Dissolve(0.5))] 
        if persistent.dv_7dl_un:
            hotspot ((590, 360, 50, 52)): #Transit-UN-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active6", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active6", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_dv_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active6", transition=Dissolve(0.5)), Replay("alt_day7_dv_7dl_un_end", scope={"alt_replay_on" : "True"}, locked=False)]
        hotspot ((650,424, 300, 52)): #Эксклюзив-Локи
            hovered [Show("sdl_achv_excl_LO_dv", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_excl_LO_dv", transition=Dissolve(0.5))]
            action [Show("sdl_achv_excl_LO_dv", transition=Dissolve(0.5))]
        if persistent.dv_7dl_tulpa:
            hotspot ((590, 424, 50, 52)): #Speziel-LK-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active7", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active7", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_dv_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active7", transition=Dissolve(0.5)), Replay("alt_day7_dv_7dl_tulpa_end", scope={"alt_replay_on" : "True"}, locked=False)]
        hotspot ((650,488, 300, 52)): #Бэд
            hovered [Show("sdl_achv_bad_dv", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_bad_dv", transition=Dissolve(0.5))]
            action [Show("sdl_achv_bad_dv", transition=Dissolve(0.5))]  
        if persistent.dv_7dl_bad:
            hotspot ((590, 488, 50, 52)): #Schlecht-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active8", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active8", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_dv_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active8", transition=Dissolve(0.5)), Replay("alt_day7_dv_7dl_bad_end", scope={"alt_replay_on" : "True"}, locked=False)]
        
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
            action [Hide("sdl_logo_active", transition=Dissolve(0.5)),Stop ("ambience"), Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_dv_7dlA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Jump("main_menu_7dl")]
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
            action [Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Stop ("ambience"), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_cl_active", transition=Dissolve(0.5)),Hide("sdl_dv_dj_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_dv_cltA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Jump("main_menu_7dl")]
# ------------------------------------------------   
######################АЛИСА-ДИДЖЕЙ######################################
label sdl_achvlist_dvdjt_Author:
    scene bg sdl_ach_inactive_dv
    with dissolve
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
            action [Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Stop ("ambience"), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_dv_dj_active", transition=Dissolve(0.5)), Hide("sdl_achv_dv_djtA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Jump("main_menu_7dl")]
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
                hovered [Show("sdl_achv_7dl_route", transition=Dissolve(1.0)), Show("sdl_logo_active", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_achv_sl_7dlA", transition=Dissolve(0.5))]
                unhovered [Hide("sdl_achv_7dl_route", transition=Dissolve(1.0)), Hide ("sdl_logo_active", transition=Dissolve(1.0)), Show ("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_7dlA", transition=Dissolve(0.5))]
                action [Hide("sdl_achv_7dl_route", transition=Dissolve(1.0)), Show("sdl_sl_cl_inactive", transition=Dissolve(0.5)), Show("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_sl7dl_Author")]
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
                action [Hide("sdl_logo_active", transition=Dissolve(0.5)),Stop ("ambience"), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Jump("main_menu_7dl")]
# ------------------------------------------------   
######################СЛАВЯ-7ДЛ######################################
label sdl_achvlist_sl7dl_Author:
    scene bg sdl_ach_inactive_sl
    with dissolve
    show sdl_achv_delB_7dl: #Иконка удалятора
        pos (380, 680)
    show sdl_achv_extB_7dl: #Иконка Ausgang
        pos(380, 350)
    
    # Тру
    if persistent.sl_7dl_true:
        show acm_logo_sl_no_wonder with dissolve:
            xcenter 800 ycenter 66
        show de_check_inactive1 with dissolve:
            pos (590, 40)
    else:
        show de_achiv_lock1 with dissolve:
            xcenter 800 ycenter 66
        if not (persistent.sl_7dl_loki_good and persistent.sl_7dl_herc_good2 and persistent.sl_7dl_good2):
            show de_info_inactive1 with dissolve:
                pos (590, 40)
        else:
            pass
    # РФ-гуд
    if persistent.sl_7dl_good_rf:
        show acm_logo_sl_till_sunrise with dissolve:
            xcenter 800 ycenter 130
        show de_check_inactive2 with dissolve:
            pos (590, 104)
    else:
        show de_achiv_lock2 with dissolve:
            xcenter 800 ycenter 130
    # Локи-Гуд
    if persistent.sl_7dl_loki_good:
        show acm_logo_sl_radio with dissolve:
            xcenter 800 ycenter 194
        show de_check_inactive3 with dissolve:
            pos (590, 168)
    else:
        show de_achiv_lock3 with dissolve:
            xcenter 800 ycenter 194
        if not (persistent.sl_7dl_loki_neu or persistent.sl_7dl_loki_rej):
            show de_info_inactive3 with dissolve:
                pos (590, 168)
        else:
            pass
    # Локи-Нейтрал
    if persistent.sl_7dl_loki_neu:
        show acm_logo_sl_am_home with dissolve:
            xcenter 800 ycenter 258
        show de_check_inactive4 with dissolve:
            pos (590, 232)
    else:
        show de_achiv_lock4 with dissolve:
            xcenter 800 ycenter 258
    # Локи-Реджект
    if persistent.sl_7dl_loki_rej:
        show acm_logo_sl_pan with dissolve:
            xcenter 800 ycenter 322
        show de_check_inactive5 with dissolve:
            pos (590, 296)
    else:
        show de_achiv_lock5 with dissolve:
            xcenter 800 ycenter 322
    # Герк-Гуд
    if persistent.sl_7dl_herc_good:
        show acm_logo_sl_right_road_7dl with dissolve:
            xcenter 800 ycenter 386
        show de_check_inactive6 with dissolve:
            pos (590, 360)
    else:
        show de_achiv_lock6 with dissolve:
            xcenter 800 ycenter 386
    # Герк-Гуд 2
    if persistent.sl_7dl_herc_good2:
        show acm_logo_sl_neon with dissolve:
            xcenter 800 ycenter 450
        show de_check_inactive7 with dissolve:
            pos (590, 424)
    else:
        show de_achiv_lock7 with dissolve:
            xcenter 800 ycenter 450
        if not persistent.sl_7dl_herc_good:
            show de_info_inactive7 with dissolve:
                pos (590, 424)
        else:
            pass
    # Дрищ-Гуд
    if persistent.sl_7dl_good:
        show acm_logo_sl_wasted with dissolve:
            xcenter 800 ycenter 514
        show de_check_inactive8 with dissolve:
            pos (590, 488)
    else:
        show de_achiv_lock8 with dissolve:
            xcenter 800 ycenter 514
    # Дрищ-Гуд 2
    if persistent.sl_7dl_good2:
        show acm_logo_sl_dr_un with dissolve:
            xcenter 800 ycenter 578
        show de_check_inactive9 with dissolve:
            pos (590, 552)
    else:
        show de_achiv_lock9 with dissolve:
            xcenter 800 ycenter 578
        if not persistent.sl_7dl_good:
            show de_info_inactive9 with dissolve:
                pos (590, 552)
        else:
            pass
    # Бэд
    if persistent.sl_7dl_bad:
        show acm_logo_sl_missed with dissolve:
            xcenter 800 ycenter 642
        show de_check_inactive10 with dissolve:
            pos (590, 616)
    else:
        show de_achiv_lock10 with dissolve:
            xcenter 800 ycenter 642
    
    call screen sdl_achvlist_sl7dl_Author
# ------------------------------------------------ 
screen sdl_achvlist_sl7dl_Author:
    tag menu
    modal True
    imagemap:
        ground "intro_transparent"
        hotspot ((1110,18, 113,65)): #Klassishe Route
            hover_sound sdl_achv_click
            hovered [Show("sdl_sl_cl_active", transition=Dissolve(1.0)), Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)), Show("sdl_achv_sl_cltA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_7dlA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_sl_cl_active", transition=Dissolve(1.0)), Show ("sdl_sl_cl_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(0.5)), Show("sdl_achv_sl_7dlA", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_sl_7dlA", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Show("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)), Show("sdl_sl_cl_active", transition=Dissolve(0.5)), Show("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_slclt_Author")]
        hotspot ((1215, 18, 113,65)): #Speziell Route
            hover_sound sdl_achv_click
            hovered [Show("sdl_sl_wh_active", transition=Dissolve(1.0)), Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Show("sdl_achv_sl_whtA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_7dlA", transition=Dissolve(0.5)), Show("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_sl_wh_active", transition=Dissolve(1.0)), Show ("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_whtA", transition=Dissolve(0.5)), Show("sdl_achv_sl_7dlA", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_sl_7dlA", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(1.0)), Show("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Show("sdl_sl_wh_active", transition=Dissolve(0.5)), Show("sdl_sl_cl_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_slwht_Author")]
        
        hotspot ((650, 40, 300, 52)): # Тру
            hovered [Show("sdl_achv_true_sl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_true_sl", transition=Dissolve(0.5))]
            action [Show("sdl_achv_true_sl", transition=Dissolve(0.5))]
        if persistent.sl_7dl_true:
            hotspot ((590, 40, 50, 52)): #Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active1", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active1", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_7dlA", transition=Dissolve(1.0)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active1", transition=Dissolve(0.5)), Replay("alt_day7_sl_7dl_true", scope={"alt_replay_on" : "True"}, locked=False)]
        elif not persistent.sl_7dl_loki_good:
            hotspot ((590, 40, 50, 50)): #Ende-Info
                hover_sound sdl_achv_info
                hovered [Show ("de_info_active1", transition=Dissolve(0.5)), Show ("sdl_achv_infochkD", transition=Dissolve(0.5)), Show ("acm_logo_sl_radio", transition=Dissolve(0.5))]
                unhovered [Hide ("de_info_active1", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_sl_radio", transition=Dissolve(0.5))]
                action [Hide("de_info_active1", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_sl_radio", transition=Dissolve(0.5))]
        elif not persistent.sl_7dl_herc_good2:
            hotspot ((590, 40, 50, 50)): #Ende-Info
                hover_sound sdl_achv_info
                hovered [Show ("de_info_active1", transition=Dissolve(0.5)), Show ("sdl_achv_infochkD", transition=Dissolve(0.5)), Show ("acm_logo_sl_neon", transition=Dissolve(0.5))]
                unhovered [Hide ("de_info_active1", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_sl_neon", transition=Dissolve(0.5))]
                action [Hide("de_info_active1", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_sl_neon", transition=Dissolve(0.5))]
        elif not persistent.sl_7dl_good2:
            hotspot ((590, 40, 50, 50)): #Ende-Info
                hover_sound sdl_achv_info
                hovered [Show ("de_info_active1", transition=Dissolve(0.5)), Show ("sdl_achv_infochkD", transition=Dissolve(0.5)), Show ("acm_logo_sl_dr_un", transition=Dissolve(0.5))]
                unhovered [Hide ("de_info_active1", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_sl_dr_un", transition=Dissolve(0.5))]
                action [Hide("de_info_active1", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_sl_dr_un", transition=Dissolve(0.5))]
        hotspot ((650, 104, 300, 52)): # РФ-гуд
            hovered [Show("sdl_achv_good_RF_sl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_good_RF_sl", transition=Dissolve(0.5))]
            action [Show("sdl_achv_good_RF_sl", transition=Dissolve(0.5))]
        if persistent.sl_7dl_good_rf:
            hotspot ((590, 104, 50, 52)): #RF-gut-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active2", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active2", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_7dlA", transition=Dissolve(1.0)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active2", transition=Dissolve(0.5)), Replay("alt_day7_sl_7dl_rf_good", scope={"alt_replay_on" : "True"}, locked=False)]
        hotspot ((650, 168, 300, 52)): # Локи-Гуд
            hovered [Show("sdl_achv_good_LO_sl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_good_LO_sl", transition=Dissolve(0.5))]
            action [Show("sdl_achv_good_LO_sl", transition=Dissolve(0.5))]
        if persistent.sl_7dl_loki_good:
            hotspot ((590, 168, 50, 52)): #Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active3", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active3", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_7dlA", transition=Dissolve(1.0)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active3", transition=Dissolve(0.5)), Replay("alt_day7_sl_7dl_loki_radio", scope={"alt_replay_on" : "True"}, locked=False)]
        elif not (persistent.sl_7dl_loki_neu or persistent.sl_7dl_loki_rej):
            hotspot ((590, 168, 50, 50)): #Ende-Info
                hover_sound sdl_achv_info
                hovered [Show ("de_info_active3", transition=Dissolve(0.5)), Show ("sdl_achv_infochkD", transition=Dissolve(0.5)), Show ("acm_logo_sl_am_home", transition=Dissolve(0.5))]
                unhovered [Hide ("de_info_active3", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_sl_am_home", transition=Dissolve(0.5))]
                action [Hide("de_info_active3", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_sl_am_home", transition=Dissolve(0.5))]
        hotspot ((650, 232, 300, 52)): # Локи-Нейтрал
            hovered [Show("sdl_achv_neutral_LO_sl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_neutral_LO_sl", transition=Dissolve(0.5))]
            action [Show("sdl_achv_neutral_LO_sl", transition=Dissolve(0.5))]
        if persistent.sl_7dl_loki_neu:
            hotspot ((590, 232, 50, 52)): #Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active4", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active4", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_7dlA", transition=Dissolve(1.0)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active4", transition=Dissolve(0.5)), Replay("alt_day7_sl_7dl_loki_am_home", scope={"alt_replay_on" : "True"}, locked=False)]
        hotspot ((650, 296, 300, 52)): # Локи-Реджект
            hovered [Show("sdl_achv_rejc_LO_sl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_rejc_LO_sl", transition=Dissolve(0.5))]
            action [Show("sdl_achv_rejc_LO_sl", transition=Dissolve(0.5))]
        if persistent.sl_7dl_loki_rej:
            hotspot ((590, 296, 50, 52)): #Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active5", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active5", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_7dlA", transition=Dissolve(1.0)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active5", transition=Dissolve(0.5)), Replay("alt_day7_sl_7dl_loki_oafa", scope={"alt_replay_on" : "True"}, locked=False)]
        hotspot ((650, 360, 300, 52)): # Герк-Гуд
            hovered [Show("sdl_achv_good_HE_sl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_good_HE_sl", transition=Dissolve(0.5))]
            action [Show("sdl_achv_good_HE_sl", transition=Dissolve(0.5))]
        if persistent.sl_7dl_herc_good:
            hotspot ((590, 360, 50, 52)): #Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active6", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active6", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_7dlA", transition=Dissolve(1.0)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active6", transition=Dissolve(0.5)), Replay("alt_day7_sl_7dl_herc_right_road", scope={"alt_replay_on" : "True"}, locked=False)]
        hotspot ((650, 424, 300, 52)): # Герк-Гуд 2
            hovered [Show("sdl_achv_good_HE_sl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_good_HE_sl", transition=Dissolve(0.5))]
            action [Show("sdl_achv_good_HE_sl", transition=Dissolve(0.5))]
        if persistent.sl_7dl_herc_good2:
            hotspot ((590, 424, 50, 52)): #Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active7", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active7", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_7dlA", transition=Dissolve(1.0)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active7", transition=Dissolve(0.5)), Replay("alt_day7_sl_7dl_herc_neon", scope={"alt_replay_on" : "True"}, locked=False)]
        elif not persistent.sl_7dl_herc_good:
            hotspot ((590, 424, 50, 50)): #Ende-Info
                hover_sound sdl_achv_info
                hovered [Show ("de_info_active7", transition=Dissolve(0.5)), Show ("sdl_achv_infochkD", transition=Dissolve(0.5)), Show ("acm_logo_sl_right_road", transition=Dissolve(0.5))]
                unhovered [Hide ("de_info_active7", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_sl_right_road", transition=Dissolve(0.5))]
                action [Hide("de_info_active7", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_sl_right_road", transition=Dissolve(0.5))]
        hotspot ((650, 488, 300, 52)): # Дрищ-Гуд
            hovered [Show("sdl_achv_good_DR_sl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_good_DR_sl", transition=Dissolve(0.5))]
            action [Show("sdl_achv_good_DR_sl", transition=Dissolve(0.5))]
        if persistent.sl_7dl_good:
            hotspot ((590, 488, 50, 52)): #Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active8", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active8", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_7dlA", transition=Dissolve(1.0)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active8", transition=Dissolve(0.5)), Replay("alt_day7_sl_7dl_wasted", scope={"alt_replay_on" : "True"}, locked=False)]
        hotspot ((650, 552, 300, 52)): # Дрищ-Гуд 2
            hovered [Show("sdl_achv_good_DR_sl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_good_DR_sl", transition=Dissolve(0.5))]
            action [Show("sdl_achv_good_DR_sl", transition=Dissolve(0.5))]
        if persistent.sl_7dl_good2:
            hotspot ((590, 552, 50, 52)): #Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active9", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active9", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_7dlA", transition=Dissolve(1.0)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active9", transition=Dissolve(0.5)), Replay("alt_day7_sl_7dl_loopback", scope={"alt_replay_on" : "True"}, locked=False)]
        elif not persistent.sl_7dl_good:
            hotspot ((590, 552, 50, 50)): #Ende-Info
                hover_sound sdl_achv_info
                hovered [Show ("de_info_active9", transition=Dissolve(0.5)), Show ("sdl_achv_infochkD", transition=Dissolve(0.5)), Show ("acm_logo_sl_wasted", transition=Dissolve(0.5))]
                unhovered [Hide ("de_info_active9", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_sl_wasted", transition=Dissolve(0.5))]
                action [Hide("de_info_active9", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_sl_wasted", transition=Dissolve(0.5))]
        hotspot ((650, 616, 300, 52)): # Бэд
            hovered [Show("sdl_achv_bad_sl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_bad_sl", transition=Dissolve(0.5))]
            action [Show("sdl_achv_bad_sl", transition=Dissolve(0.5))]
        if persistent.sl_7dl_bad:
            hotspot ((590, 616, 50, 52)): #Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active10", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active10", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_7dlA", transition=Dissolve(1.0)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active10", transition=Dissolve(0.5)), Replay("alt_day7_sl_7dl_missed", scope={"alt_replay_on" : "True"}, locked=False)]
        
        
        hotspot ((0, 0, 550, 340)): #Мику
            hover_sound sdl_achv_pagina
            hovered [Show("mi_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mi_button_active", transition=Dissolve(0.5))]
            action [Hide("mi_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_7dlA", transition=Dissolve(0.5)), Jump("sdl_achvlist_mi_Author")]
        hotspot ((0, 344, 360, 390)): #Алисхен
            hover_sound sdl_achv_pagina
            hovered [Show("dv_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("dv_button_active", transition=Dissolve(0.5))]
            action [Hide("dv_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_7dlA", transition=Dissolve(0.5)), Jump("sdl_achvlist_dv_Author")]
        hotspot ((1380, 0, 600, 340)): #Лена
            hover_sound sdl_achv_pagina
            hovered [Show("un_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("un_button_active", transition=Dissolve(0.5))]
            action [Hide("un_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_7dlA", transition=Dissolve(0.5)),  Jump("sdl_achvlist_un_Author")]
        hotspot ((1560, 343, 360, 185)): #Ольга
            hover_sound sdl_achv_pagina
            hovered [Show("mt_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mt_button_active", transition=Dissolve(0.5))]
            action [Hide("mt_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_7dlA", transition=Dissolve(0.5)),  Jump("sdl_achvlist_mt_Author")]
        hotspot ((1561, 530, 359, 202)): #Ульяна
            hover_sound sdl_achv_pagina
            hovered [Show("us_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("us_button_active", transition=Dissolve(0.5))]
            action [Hide("us_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_7dlA", transition=Dissolve(0.5)),  Jump("sdl_achvlist_us_Author")]
        hotspot ((1380, 735, 600, 345)): #Одиночка
            hover_sound sdl_achv_pagina
            hovered [Show("me_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("me_button_active", transition=Dissolve(0.5))]
            action [Hide("me_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_7dlA", transition=Dissolve(0.5)),  Jump("sdl_achvlist_me_Author")]
        
        hotspot ((380, 350, 170, 50)): #Выход
            hover_sound sdl_achv_click
            hovered [Show("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            action [Stop ("ambience"), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_7dlA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Jump("main_menu_7dl")]
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
            hovered [Show("sdl_logo_active", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_achv_sl_7dlA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_logo_active", transition=Dissolve(1.0)), Show ("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_7dlA", transition=Dissolve(0.5)), Show("sdl_achv_sl_cltA", transition=Dissolve(0.5))]
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
                action [Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_cl_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active1", transition=Dissolve(0.5)), Replay("alt_day7_sl_will", scope={"alt_replay_on" : "True"}, locked=False)]
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
                action [Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_cl_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active2", transition=Dissolve(0.5)), Replay("alt_day7_sl_duty", scope={"alt_replay_on" : "True"}, locked=False)]
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
                action [Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_cl_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active3", transition=Dissolve(0.5)), Replay("alt_day7_sl_lone", scope={"alt_replay_on" : "True"}, locked=False)]
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
                action [Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_cl_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active4", transition=Dissolve(0.5)), Replay("alt_day7_sl_good", scope={"alt_replay_on" : "True"}, locked=False)]
        hotspot ((650,296, 300, 52)): #РФ-гуд
            hovered [Show("sdl_achv_good_RF_sl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_good_RF_sl", transition=Dissolve(0.5))]
            action [Show("sdl_achv_good_RF_sl", transition=Dissolve(0.5))]
        if persistent.sl_cl_good_rf2:
            hotspot ((590, 296, 50, 52)): #RF-gut-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active5", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active5", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_cl_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active5", transition=Dissolve(0.5)), Replay("alt_day7_sl_rf2", scope={"alt_replay_on" : "True"}, locked=False)]
        hotspot ((650,360, 300, 52)): #РФ-гуд (Плюс-минус)      
            hovered [Show("sdl_achv_good_RF_sl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_good_RF_sl", transition=Dissolve(0.5))]
            action [Show("sdl_achv_good_RF_sl", transition=Dissolve(0.5))] 
        if persistent.sl_cl_good_rf:
            hotspot ((590, 360, 50, 52)): #RF-gut-Ende (Plus-Minus)-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active6", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active6", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_cl_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active6", transition=Dissolve(0.5)), Replay("alt_day7_sl_rf_good", scope={"alt_replay_on" : "True"}, locked=False)]   
        hotspot ((650,424, 300, 52)): #Реджект-РФ
            hovered [Show("sdl_achv_rejc_RF_sl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_rejc_RF_sl", transition=Dissolve(0.5))]
            action [Show("sdl_achv_rejc_RF_sl", transition=Dissolve(0.5))]
        if persistent.sl_cl_reject_same:
            hotspot ((590, 424, 50, 52)): #Reject-RF-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active7", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active7", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_cl_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active7", transition=Dissolve(0.5)), Replay("alt_day7_sl_reject_same", scope={"alt_replay_on" : "True"}, locked=False)]   
        hotspot ((650,488, 300, 52)): #Реджект-2 
            hovered [Show("sdl_achv_rejc_RF_sl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_rejc_RF_sl", transition=Dissolve(0.5))]
            action [Show("sdl_achv_rejc_RF_sl", transition=Dissolve(0.5))]  
        if persistent.sl_cl_reject_late:
            hotspot ((590, 488, 50, 52)): #Reject-RF-Ende-2-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active8", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active8", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_cl_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active8", transition=Dissolve(0.5)), Replay("alt_day7_sl_reject_late_ach", scope={"alt_replay_on" : "True"}, locked=False)]   
        hotspot ((650,552, 300, 52)): #Эксклюзив-Локи   
            hovered [Show("sdl_achv_excl_LO_sl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_excl_LO_sl", transition=Dissolve(0.5))]
            action [Show("sdl_achv_excl_LO_sl", transition=Dissolve(0.5))]  
        if persistent.sl_cl_cata:
            hotspot ((590, 552, 50, 52)): #schlecht-M-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active9", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active9", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_cl_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active9", transition=Dissolve(0.5)), Replay("alt_day6_sl_cl_become_a_hero", scope={"alt_replay_on" : "True"}, locked=False)]   
        hotspot ((650,616, 300, 52)): #Бэд   
            hovered [Show("sdl_achv_bad_sl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_bad_sl", transition=Dissolve(0.5))]
            action [Show("sdl_achv_bad_sl", transition=Dissolve(0.5))]  
        if persistent.sl_cl_bad:
            hotspot ((590, 616, 50, 52)): #schlecht-S-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active10", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active10", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_sl_cl_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active10", transition=Dissolve(0.5)), Replay("alt_day7_sl_cl_bad", scope={"alt_replay_on" : "True"}, locked=False)]   
        
        hotspot ((0, 0, 550, 340)): #Мику
            hover_sound sdl_achv_pagina
            hovered [Show("mi_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mi_button_active", transition=Dissolve(0.5))]
            action [Hide("mi_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_cl_active", transition=Dissolve(0.5)),Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(0.5)), Jump("sdl_achvlist_mi_Author")]
        hotspot ((0, 344, 360, 390)): #Алисхен
            hover_sound sdl_achv_pagina
            hovered [Show("dv_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("dv_button_active", transition=Dissolve(0.5))]
            action [Hide("dv_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_cl_active", transition=Dissolve(0.5)),Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(0.5)), Jump("sdl_achvlist_dv_Author")]
        hotspot ((1380, 0, 600, 340)): #Лена
            hover_sound sdl_achv_pagina
            hovered [Show("un_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("un_button_active", transition=Dissolve(0.5))]
            action [Hide("un_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_cl_active", transition=Dissolve(0.5)),Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(0.5)),  Jump("sdl_achvlist_un_Author")]
        hotspot ((1560, 343, 360, 185)): #Ольга
            hover_sound sdl_achv_pagina
            hovered [Show("mt_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mt_button_active", transition=Dissolve(0.5))]
            action [Hide("mt_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_cl_active", transition=Dissolve(0.5)),Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(0.5)),  Jump("sdl_achvlist_mt_Author")]
        hotspot ((1561, 530, 359, 202)): #Ульяна
            hover_sound sdl_achv_pagina
            hovered [Show("us_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("us_button_active", transition=Dissolve(0.5))]
            action [Hide("us_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_cl_active", transition=Dissolve(0.5)),Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(0.5)),  Jump("sdl_achvlist_us_Author")]
        hotspot ((1380, 735, 600, 345)): #Одиночка
            hover_sound sdl_achv_pagina
            hovered [Show("me_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("me_button_active", transition=Dissolve(0.5))]
            action [Hide("me_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_cl_active", transition=Dissolve(0.5)),Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(0.5)),  Jump("sdl_achvlist_me_Author")]
        
        hotspot ((380, 350, 170, 50)): #Выход
            hover_sound sdl_achv_click
            hovered [Show("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            action [Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Stop ("ambience"), Hide("sdl_sl_cl_active", transition=Dissolve(0.5)),Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_cltA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Jump("main_menu_7dl")]
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
            hovered [Show("sdl_logo_active", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_achv_sl_7dlA", transition=Dissolve(0.5)), Hide("sdl_achv_sl_whtA", transition=Dissolve(0.5)), Hide("sdl_achv_need_routeA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_logo_active", transition=Dissolve(1.0)), Show ("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_sl_7dlA", transition=Dissolve(0.5)), Show("sdl_achv_sl_whtA", transition=Dissolve(0.5)), Show("sdl_achv_need_routeA", transition=Dissolve(0.5))]
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
            action [Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Stop ("ambience"), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_sl_wh_active", transition=Dissolve(0.5)), Hide("sdl_achv_sl_whtA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Jump("main_menu_7dl")]
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
                action [Hide("sl_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_sl_Author")]
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
                action [Hide("sdl_logo_active", transition=Dissolve(0.5)),Stop ("ambience"), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)),Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Jump("main_menu_7dl")]
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
                action [Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_un_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active1", transition=Dissolve(0.5)), Replay("alt_day7_un_7dl_true", scope={"alt_replay_on" : "True"}, locked=False)]
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
                action [Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_un_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active2", transition=Dissolve(0.5)), Replay("alt_day7_un_7dl_true1", scope={"alt_replay_on" : "True"}, locked=False)]
        hotspot ((650,168, 300, 52)): #Гуд-СССР
            hovered [Show("sdl_achv_good_US_un", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_good_US_un", transition=Dissolve(0.5))]
            action [Show("sdl_achv_good_US_un", transition=Dissolve(0.5))] 
        if persistent.un_7dl_good_ussr:
            hotspot ((590, 168, 50, 52)): #UdSSR-Gut-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active3", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active3", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_un_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active3", transition=Dissolve(0.5)), Replay("alt_day7_un_7dl_ussr", scope={"alt_replay_on" : "True"}, locked=False)]
        hotspot ((650,232, 300, 52)): #Гуд-РФ     
            hovered [Show("sdl_achv_good_RF_un", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_good_RF_un", transition=Dissolve(0.5))]
            action [Show("sdl_achv_good_RF_un", transition=Dissolve(0.5))] 
        if persistent.un_7dl_good_rf:
            hotspot ((590, 232, 50, 52)): #RF-Gut-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active4", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active4", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_un_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active4", transition=Dissolve(0.5)), Replay("alt_day7_un_7dl_rf", scope={"alt_replay_on" : "True"}, locked=False)]
        hotspot ((650,296, 300, 52)): #Бэд
            hovered [Show("sdl_achv_bad_un", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_bad_un", transition=Dissolve(0.5))]
            action [Show("sdl_achv_bad_un", transition=Dissolve(0.5))] 
        if persistent.un_7dl_bad:
            hotspot ((590, 296, 50, 52)): #Schlecht-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active5", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active5", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_un_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active5", transition=Dissolve(0.5)), Replay("alt_day7_un_7dl_epilogue_bad", scope={"alt_replay_on" : "True"}, locked=False)]
        
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
            action [Hide("sdl_logo_active", transition=Dissolve(0.5)),Stop ("ambience"), Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_un_7dlA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Jump("main_menu_7dl")]
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
            action [Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Stop ("ambience"), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_un_cl_active", transition=Dissolve(0.5)),Hide("sdl_un_fz_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_un_cltA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Jump("main_menu_7dl")]
# ------------------------------------------------   
######################ЛЕНА-ФРЕНДЗОНА######################################
label sdl_achvlist_unfzd_Author:
    scene bg sdl_ach_inactive_un
    with dissolve
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
            action [Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Stop ("ambience"), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_un_cl_inactive", transition=Dissolve(0.5)),Hide("sdl_un_fz_active", transition=Dissolve(0.5)), Hide("sdl_achv_un_fzdA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Jump("main_menu_7dl")]
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
        if not persistent.mt_7dl_good:
            show de_info_inactive3 with dissolve:
                pos (590, 168)
        else:
            pass
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
                action [Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Stop ("ambience"), Hide("de_check_active1", transition=Dissolve(0.5)), Replay("alt_day7_mt_7dl_true", scope={"alt_replay_on" : "True"}, locked=False)]
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
                action [Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Stop ("ambience"), Hide("de_check_active2", transition=Dissolve(0.5)), Replay("alt_day7_mt_7dl_good", scope={"alt_replay_on" : "True"}, locked=False)]
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
                action [Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Stop ("ambience"), Hide("de_check_active3", transition=Dissolve(0.5)), Replay("alt_day7_mt_7dl_ever_after", scope={"alt_replay_on" : "True"}, locked=False)]
        elif not persistent.mt_7dl_good:
            hotspot ((590, 168, 50, 50)): #Ende-Info
                hover_sound sdl_achv_info
                hovered [Show ("de_info_active3", transition=Dissolve(0.5)), Show ("sdl_achv_infochkD", transition=Dissolve(0.5)), Show ("acm_logo_mt_named_olga", transition=Dissolve(0.5))]
                unhovered [Hide ("de_info_active3", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_mt_named_olga", transition=Dissolve(0.5))]
                action [Hide("de_info_active3", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_mt_named_olga", transition=Dissolve(0.5))]   
        hotspot ((650,232, 300, 52)): #Бэд
            hovered [Show("sdl_achv_bad_mt", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_bad_mt", transition=Dissolve(0.5))]
            action [Show("sdl_achv_bad_mt", transition=Dissolve(0.5))] 
        if persistent.mt_7dl_bad:
            hotspot ((590, 232, 50, 52)): #Schlecht-Ende-Jump
                hovered [Show ("de_check_active4", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active4", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Stop ("ambience"), Hide("de_check_active4", transition=Dissolve(0.5)), Replay("alt_day7_mt_7dl_bad", scope={"alt_replay_on" : "True"}, locked=False)]    
            
        hotspot ((380, 350, 170, 50)): #Выход
            hover_sound sdl_achv_click
            hovered [Show("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Stop ("ambience"), Jump("main_menu_7dl")]
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
    show sdl_logo_inactive: #7DL logo
        pos (980, 18)
    show sdl_us_px_inactive: #Speziell logo
        pos (1110, 18)
    show sdl_achv_extB_7dl: #Иконка Ausgang
        pos(380, 350)
    call screen sdl_achvlist_us_Author
    screen sdl_achvlist_us_Author:
        tag menu
        modal True
        imagemap:
            ground "intro_transparent"
            hotspot ((980, 18, 113,65)): #7DL Route
                hover_sound sdl_achv_click
                hovered [Show("sdl_achv_7dl_route", transition=Dissolve(1.0)), Show("sdl_logo_active", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_achv_us_7dlA", transition=Dissolve(0.5))]
                unhovered [Hide("sdl_achv_7dl_route", transition=Dissolve(1.0)), Hide ("sdl_logo_active", transition=Dissolve(1.0)), Show ("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_us_7dlA", transition=Dissolve(0.5))]
                action [Hide("sdl_achv_7dl_route", transition=Dissolve(1.0)), Show("sdl_us_px_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_us7dl_Author")]
            hotspot ((1110,18, 113,65)): #Speziell Route
                hover_sound sdl_achv_click
                hovered [Show("sdl_achv_xxx_route", transition=Dissolve(1.0)), Show("sdl_us_px_active", transition=Dissolve(1.0)), Hide("sdl_us_px_inactive", transition=Dissolve(0.5)), Show("sdl_achv_us_pxsA", transition=Dissolve(0.5))]
                unhovered [Hide("sdl_achv_xxx_route", transition=Dissolve(1.0)), Hide ("sdl_us_px_active", transition=Dissolve(1.0)), Show ("sdl_us_px_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_us_pxsA", transition=Dissolve(0.5))]
                action [Hide("sdl_achv_xxx_route", transition=Dissolve(1.0)), Show("sdl_logo_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_uspxs_Author")]
            
            hotspot ((0, 0, 550, 340)): #Мику
                hover_sound sdl_achv_pagina
                hovered [Show("mi_button_active", transition=Dissolve(0.5))]
                unhovered [Hide("mi_button_active", transition=Dissolve(0.5))]
                action [Hide("mi_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_us_px_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_mi_Author")]
            hotspot ((0, 344, 360, 390)): #Алисхен
                hover_sound sdl_achv_pagina
                hovered [Show("dv_button_active", transition=Dissolve(0.5))]
                unhovered [Hide("dv_button_active", transition=Dissolve(0.5))]
                action [Hide("dv_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_us_px_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_dv_Author")]
            hotspot ((0, 734, 550, 345)): #Славя
                hover_sound sdl_achv_pagina
                hovered [Show("sl_button_active", transition=Dissolve(0.5))]
                unhovered [Hide("sl_button_active", transition=Dissolve(0.5))]
                action [Hide("sl_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_us_px_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_sl_Author")]
            hotspot ((1380, 0, 600, 340)): #Лена
                hover_sound sdl_achv_pagina
                hovered [Show("un_button_active", transition=Dissolve(0.5))]
                unhovered [Hide("un_button_active", transition=Dissolve(0.5))]
                action [Hide("un_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_us_px_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_un_Author")]
            hotspot ((1560, 343, 360, 185)): #Ольга
                hover_sound sdl_achv_pagina
                hovered [Show("mt_button_active", transition=Dissolve(0.5))]
                unhovered [Hide("mt_button_active", transition=Dissolve(0.5))]
                action [Hide("mt_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_us_px_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_mt_Author")]
            hotspot ((1380, 735, 600, 345)): #Одиночка
                hover_sound sdl_achv_pagina
                hovered [Show("me_button_active", transition=Dissolve(0.5))]
                unhovered [Hide("me_button_active", transition=Dissolve(0.5))]
                action [Hide("me_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_us_px_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_me_Author")]
            hotspot ((380, 350, 170, 50)): #Выход
                hover_sound sdl_achv_click
                hovered [Show("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
                unhovered [Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
                action [Hide("sdl_logo_active", transition=Dissolve(0.5)),Stop ("ambience"),Hide("sdl_us_px_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_us_7dlA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Jump("main_menu_7dl")]
# ------------------------------------------------   
######################УЛЬЯНА-7ДЛ######################################
label sdl_achvlist_us7dl_Author:
    scene bg sdl_ach_inactive_us
    with dissolve
    show sdl_achv_delB_7dl: #Иконка удалятора
        pos (380, 680)
    show sdl_achv_extB_7dl: #Иконка Ausgang
        pos(380, 350)

    #Тру-7дл
    if persistent.us_7dl_true:
        show acm_logo_us_true  with dissolve:
            xcenter 800 ycenter 66
        show de_check_inactive6 with dissolve:
            pos (590, 40)
    else:
        show de_achiv_lock6 with dissolve:
            xcenter 800 ycenter 66
        if not (persistent.us_px_rf_good and (persistent.us_7dl_un or persistent.us_7dl_mi)):
            show de_info_inactive1 with dissolve:
                pos (590, 40)
        else:
            pass
    #Гуд-7дл
    if persistent.us_7dl_good:
        show acm_logo_us_semische  with dissolve:
            xcenter 800 ycenter 130
        show de_check_inactive1 with dissolve:
            pos (590, 104)
    else:
        show de_achiv_lock1 with dissolve:
            xcenter 800 ycenter 130
    #Лена
    if persistent.us_7dl_un:
        show acm_logo_us_hi  with dissolve:
            xcenter 800 ycenter 194
        show de_check_inactive2 with dissolve:
            pos (590, 168)
    else:
        show de_achiv_lock2 with dissolve:
            xcenter 800 ycenter 194
    #Мику
    if persistent.us_7dl_mi:
        show acm_logo_us_openup  with dissolve:
            xcenter 800 ycenter 258
        show de_check_inactive3 with dissolve:
            pos (590, 232)
    else:
        show de_achiv_lock3 with dissolve:
            xcenter 800 ycenter 258
    #Бэд-7дл
    if persistent.us_7dl_bad:
        show acm_logo_us_bad  with dissolve:
            xcenter 800 ycenter 322
        show de_check_inactive7 with dissolve:
            pos (590, 296)
    else:
        show de_achiv_lock7 with dissolve:
            xcenter 800 ycenter 322

    call screen sdl_achvlist_us7dl_Author
# ------------------------------------------------ 
screen sdl_achvlist_us7dl_Author:
    tag menu
    modal True
    imagemap:
        ground "intro_transparent"
        hotspot ((1110,18, 113, 65)): #Speziell Route
            hover_sound sdl_achv_click
            hovered [Show("sdl_us_px_active", transition=Dissolve(1.0)), Hide("sdl_us_px_inactive", transition=Dissolve(0.5)), Show("sdl_achv_us_pxsA", transition=Dissolve(0.5)), Hide("sdl_achv_us_7dlA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_us_px_active", transition=Dissolve(1.0)), Show ("sdl_us_px_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_us_pxsA", transition=Dissolve(0.5)), Show("sdl_achv_us_7dlA", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_us_7dlA", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(1.0)), Show("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_us_px_inactive", transition=Dissolve(0.5)), Show("sdl_us_px_active", transition=Dissolve(0.5)), Jump("sdl_achvlist_uspxs_Author")]

        hotspot ((650, 40, 300, 52)): #Тру-7дл
            hovered [Show("sdl_achv_true_us", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_true_us", transition=Dissolve(0.5))]
            action [Show("sdl_achv_true_us", transition=Dissolve(0.5))] 
        if persistent.us_7dl_true:
            hotspot ((590, 40, 50, 52)):
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active1", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active1", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_us_px_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_us_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active1", transition=Dissolve(0.5)), Replay("alt_day7_us_7dl_ever_after", scope={"alt_replay_on" : "True"}, locked=False)]
        elif not persistent.us_px_rf_good:
            hotspot ((590, 40, 50, 50)): #Ende-Info
                hover_sound sdl_achv_info
                hovered [Show ("de_info_active1", transition=Dissolve(0.5)), Show ("sdl_achv_infochkD", transition=Dissolve(0.5)), Show ("acm_logo_us_px", transition=Dissolve(0.5))]
                unhovered [Hide ("de_info_active1", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_us_px", transition=Dissolve(0.5))]
                action [Hide("de_info_active1", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_us_px", transition=Dissolve(0.5))]
        elif not (persistent.us_7dl_un or persistent.us_7dl_mi):
            hotspot ((590, 40, 50, 50)): #Ende-Info
                hover_sound sdl_achv_info
                hovered [Show ("de_info_active1", transition=Dissolve(0.5)), Show ("sdl_achv_infochkD", transition=Dissolve(0.5)), Show ("acm_logo_us_hi", transition=Dissolve(0.5))]
                unhovered [Hide ("de_info_active1", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_us_hi", transition=Dissolve(0.5))]
                action [Hide("de_info_active1", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_us_hi", transition=Dissolve(0.5))]
        hotspot ((650, 104, 300, 52)): #Гуд-7дл
            hovered [Show("sdl_achv_good_us", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_good_us", transition=Dissolve(0.5))]
            action [Show("sdl_achv_good_us", transition=Dissolve(0.5))]
        if persistent.us_7dl_good:
            hotspot ((590, 104, 50, 52)):
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active2", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active2", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_us_px_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_us_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active2", transition=Dissolve(0.5)), Replay("alt_day7_us_7dl_reunite", scope={"alt_replay_on" : "True"}, locked=False)]
        hotspot ((650, 168, 300, 52)): #Лена
            hovered [Show("sdl_achv_us_un", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_us_un", transition=Dissolve(0.5))]
            action [Show("sdl_achv_us_un", transition=Dissolve(0.5))]
        if persistent.us_7dl_un:
            hotspot ((590, 168, 50, 52)):
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active3", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active3", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_us_px_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_us_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active3", transition=Dissolve(0.5)), Replay("alt_day7_us_7dl_lenaforever", scope={"alt_replay_on" : "True"}, locked=False)]
        hotspot ((650, 232, 300, 52)): #Мику
            hovered [Show("sdl_achv_us_mi", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_us_mi", transition=Dissolve(0.5))]
            action [Show("sdl_achv_us_mi", transition=Dissolve(0.5))]  
        if persistent.us_7dl_mi:
            hotspot ((590, 232, 50, 52)):
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active4", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active4", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_us_px_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_us_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active4", transition=Dissolve(0.5)), Replay("alt_day7_us_7dl_mikuforever", scope={"alt_replay_on" : "True"}, locked=False)]
        hotspot ((650, 296, 300, 52)): #Бэд-7дл
            hovered [Show("sdl_achv_bad_us", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_bad_us", transition=Dissolve(0.5))]
            action [Show("sdl_achv_bad_us", transition=Dissolve(0.5))]
        if persistent.us_7dl_bad:
            hotspot ((590, 296, 50, 52)):
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active5", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active5", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_us_px_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_us_7dlA", transition=Dissolve(1.0)), Hide("sdl_logo_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active5", transition=Dissolve(0.5)), Replay("alt_day7_us_7dl_bad", scope={"alt_replay_on" : "True"}, locked=False)]

        hotspot ((0, 0, 550, 340)): #Мику
            hover_sound sdl_achv_pagina
            hovered [Show("mi_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mi_button_active", transition=Dissolve(0.5))]
            action [Hide("mi_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_us_px_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_us_7dlA", transition=Dissolve(1.0)), Jump("sdl_achvlist_mi_Author")]
        hotspot ((0, 344, 360, 390)): #Алисхен
            hover_sound sdl_achv_pagina
            hovered [Show("dv_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("dv_button_active", transition=Dissolve(0.5))]
            action [Hide("dv_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_us_px_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_us_7dlA", transition=Dissolve(1.0)), Jump("sdl_achvlist_dv_Author")]
        hotspot ((0, 734, 550, 345)): #Славя
            hover_sound sdl_achv_pagina
            hovered [Show("sl_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("sl_button_active", transition=Dissolve(0.5))]
            action [Hide("sl_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_us_px_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_us_7dlA", transition=Dissolve(1.0)), Jump("sdl_achvlist_sl_Author")]
        hotspot ((1380, 0, 600, 340)): #Лена
            hover_sound sdl_achv_pagina
            hovered [Show("un_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("un_button_active", transition=Dissolve(0.5))]
            action [Hide("un_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_us_px_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_us_7dlA", transition=Dissolve(1.0)), Jump("sdl_achvlist_un_Author")]
        hotspot ((1560, 343, 360, 185)): #Ольга
            hover_sound sdl_achv_pagina
            hovered [Show("mt_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mt_button_active", transition=Dissolve(0.5))]
            action [Hide("mt_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_us_px_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_us_7dlA", transition=Dissolve(1.0)), Jump("sdl_achvlist_mt_Author")]
        hotspot ((1380, 735, 600, 345)): #Одиночка
            hover_sound sdl_achv_pagina
            hovered [Show("me_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("me_button_active", transition=Dissolve(0.5))]
            action [Hide("me_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_us_px_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_us_7dlA", transition=Dissolve(1.0)), Jump("sdl_achvlist_me_Author")]

        hotspot ((380, 350, 170, 50)): #Выход
            hover_sound sdl_achv_click
            hovered [Show("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            action [Hide("sdl_logo_active", transition=Dissolve(0.5)),Stop ("ambience"), Hide("sdl_us_px_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_us_7dlA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Jump("main_menu_7dl")]
        hotspot ((380, 680, 170, 50)): #Удалятор
            hover_sound sdl_achv_click
            activate_sound sdl_achv_clear
            hovered [Show("sdl_achv_delA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5))]
            action Jump("sdl_achvlist_us7dl_clear_Author")
# ------------------------------------------------   
######################УЛЬЯНА-ОГОНЬКИ######################################
label sdl_achvlist_uspxs_Author:
    scene bg sdl_ach_inactive_us
    with dissolve    
    show sdl_achv_delB_7dl: #Иконка удалятора
        pos (380, 680)
    show sdl_achv_extB_7dl: #Иконка Ausgang
        pos(380, 350)

    #Тру-Огоньки
    if persistent.us_px_true:
        show acm_logo_us_fairytale with dissolve:
            xcenter 800 ycenter 66
        show de_check_inactive5 with dissolve:
            pos (590, 40)
    else:
        show de_achiv_lock5 with dissolve:
            xcenter 800 ycenter 66
        if not persistent.us_7dl_good:
            show de_info_inactive1 with dissolve:
                pos (590, 40)
        else:
            pass
    #Гуд-Огоньки
    if persistent.us_px_rf_good:
        show acm_logo_us_px  with dissolve:
            xcenter 800 ycenter 130
        show de_check_inactive4 with dissolve:
            pos (590, 104)
    else:
        show de_achiv_lock4 with dissolve:
            xcenter 800 ycenter 130

    call screen sdl_achvlist_uspxs_Author
# ------------------------------------------------
screen sdl_achvlist_uspxs_Author:
    tag menu
    modal True
    imagemap:
        ground "intro_transparent"
        hotspot ((980, 18, 113, 65)): #7DL Route
            hover_sound sdl_achv_click
            hovered [Show("sdl_logo_active", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_achv_us_7dlA", transition=Dissolve(0.5)), Hide("sdl_achv_us_pxsA", transition=Dissolve(0.5))]
            unhovered [Hide ("sdl_logo_active", transition=Dissolve(1.0)), Show ("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_us_7dlA", transition=Dissolve(0.5)), Show("sdl_achv_us_pxsA", transition=Dissolve(0.5))]
            action [Hide("sdl_achv_us_pxsA", transition=Dissolve(0.5)), Show("sdl_us_px_inactive", transition=Dissolve(0.5)), Hide ("sdl_us_px_active", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Show("sdl_logo_active", transition=Dissolve(0.5)), Jump("sdl_achvlist_us7dl_Author")]

        hotspot ((650, 40, 300, 52)): #Тру-Огоньки
            hovered [Show("sdl_achv_true_us", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_true_us", transition=Dissolve(0.5))]
            action [Show("sdl_achv_true_us", transition=Dissolve(0.5))] 
        if persistent.us_px_true:
            hotspot ((590, 40, 50, 52)):
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active1", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active1", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Stop ("ambience"), Hide("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_us_pxsA", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_us_px_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active1", transition=Dissolve(0.5)), Replay("alt_day7_us_px_fairytale", scope={"alt_replay_on" : "True"}, locked=False)]
        elif not persistent.us_7dl_good:
            hotspot ((590, 40, 50, 50)): #Ende-Info
                hover_sound sdl_achv_info
                hovered [Show ("de_info_active1", transition=Dissolve(0.5)), Show ("sdl_achv_infochkD", transition=Dissolve(0.5)), Show ("acm_logo_us_semische", transition=Dissolve(0.5))]
                unhovered [Hide ("de_info_active1", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_us_semische", transition=Dissolve(0.5))]
                action [Hide("de_info_active1", transition=Dissolve(0.5)), Hide ("sdl_achv_infochkD", transition=Dissolve(0.5)), Hide ("acm_logo_us_semische", transition=Dissolve(0.5))]
        hotspot ((650, 104, 300, 52)): #Гуд-Огоньки
            hovered [Show("sdl_achv_good_us", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_good_us", transition=Dissolve(0.5))]
            action [Show("sdl_achv_good_us", transition=Dissolve(0.5))]
        if persistent.us_px_rf_good:
            hotspot ((590, 104, 50, 52)):
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active2", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active2", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Stop ("ambience"), Hide("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_us_pxsA", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_us_px_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active2", transition=Dissolve(0.5)), Replay("alt_day7_us_px_dejavu", scope={"alt_replay_on" : "True"}, locked=False)]

        hotspot ((0, 0, 550, 340)): #Мику
            hover_sound sdl_achv_pagina
            hovered [Show("mi_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mi_button_active", transition=Dissolve(0.5))]
            action [Hide("mi_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_us_px_active", transition=Dissolve(0.5)), Hide("sdl_achv_us_pxsA", transition=Dissolve(1.0)), Jump("sdl_achvlist_mi_Author")]
        hotspot ((0, 344, 360, 390)): #Алисхен
            hover_sound sdl_achv_pagina
            hovered [Show("dv_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("dv_button_active", transition=Dissolve(0.5))]
            action [Hide("dv_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_us_px_active", transition=Dissolve(0.5)), Hide("sdl_achv_us_pxsA", transition=Dissolve(1.0)), Jump("sdl_achvlist_dv_Author")]
        hotspot ((0, 734, 550, 345)): #Славя
            hover_sound sdl_achv_pagina
            hovered [Show("sl_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("sl_button_active", transition=Dissolve(0.5))]
            action [Hide("sl_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_us_px_active", transition=Dissolve(0.5)), Hide("sdl_achv_us_pxsA", transition=Dissolve(1.0)), Jump("sdl_achvlist_sl_Author")]
        hotspot ((1380, 0, 600, 340)): #Лена
            hover_sound sdl_achv_pagina
            hovered [Show("un_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("un_button_active", transition=Dissolve(0.5))]
            action [Hide("un_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_us_px_active", transition=Dissolve(0.5)), Hide("sdl_achv_us_pxsA", transition=Dissolve(1.0)), Jump("sdl_achvlist_un_Author")]
        hotspot ((1560, 343, 360, 185)): #Ольга
            hover_sound sdl_achv_pagina
            hovered [Show("mt_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("mt_button_active", transition=Dissolve(0.5))]
            action [Hide("mt_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_us_px_active", transition=Dissolve(0.5)), Hide("sdl_achv_us_pxsA", transition=Dissolve(1.0)), Jump("sdl_achvlist_mt_Author")]
        hotspot ((1380, 735, 600, 345)): #Одиночка
            hover_sound sdl_achv_pagina
            hovered [Show("me_button_active", transition=Dissolve(0.5))]
            unhovered [Hide("me_button_active", transition=Dissolve(0.5))]
            action [Hide("me_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_us_px_active", transition=Dissolve(0.5)), Hide("sdl_achv_us_pxsA", transition=Dissolve(1.0)), Jump("sdl_achvlist_me_Author")]

        hotspot ((380, 350, 170, 50)): #Выход
            hover_sound sdl_achv_click
            hovered [Show("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5))]
            action [Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Stop ("ambience"), Hide("sdl_us_px_active", transition=Dissolve(0.5)), Hide("sdl_achv_us_pxsA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Jump("main_menu_7dl")]
        hotspot ((380, 680, 170, 50)): #Удалятор
            hover_sound sdl_achv_click
            activate_sound sdl_achv_clear
            hovered [Show("sdl_achv_delA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5))]
            action Jump("sdl_achvlist_uspxs_clear_Author")
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
                action [Hide("sl_button_active", transition=Dissolve(0.5)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_me_no_inactive", transition=Dissolve(0.5)),Hide("sdl_me_sm_inactive", transition=Dissolve(0.5)), Jump("sdl_achvlist_sl_Author")]
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
                action [Hide("sdl_logo_active", transition=Dissolve(0.5)),Stop ("ambience"), Hide("sdl_achv_mi_7dlA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)),Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_me_no_inactive", transition=Dissolve(0.5)),Hide("sdl_me_sm_inactive", transition=Dissolve(0.5)), Jump("main_menu_7dl")]
# ------------------------------------------------
######################Д3-РУТ######################################
label sdl_achvlist_med3r_Author:
    scene bg sdl_ach_inactive_me
    with dissolve
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
            action [Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)),Stop ("ambience"), Hide("sdl_logo_active", transition=Dissolve(0.5)),Hide("sdl_me_no_inactive", transition=Dissolve(0.5)),Hide("sdl_me_sm_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_me_d3rA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Jump("main_menu_7dl")]
# ------------------------------------------------
######################НУАР-РУТ######################################
label sdl_achvlist_menoi_Author:
    scene bg sdl_ach_inactive_me
    with dissolve
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
            action [Hide("sdl_achv_need_routeA", transition=Dissolve(0.5)), Stop ("ambience"), Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Hide("sdl_me_no_active", transition=Dissolve(0.5)),Hide("sdl_me_sm_inactive", transition=Dissolve(0.5)), Hide("sdl_achv_me_noiA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Jump("main_menu_7dl")]
# ------------------------------------------------
######################ПРОЧИЕ ДОСТИЖЕНИЯ######################################
label sdl_achvlist_mesmt_Author:
    scene bg sdl_ach_inactive_me
    with dissolve
    show sdl_achv_delB_7dl: #Иконка удалятора
        pos (380, 680)
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
        show de_check_active4 with dissolve:
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
        if persistent.alt_lamp:
            hotspot ((590, 40, 50, 52)): #Zerbrechen-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active1", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active1", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                action [Hide("sdl_me_no_inactive", transition=Dissolve(0.5)),Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_me_smtA", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_me_sm_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active1", transition=Dissolve(0.5)), Replay("alt_day6_un_7dl_letmeout", scope={"alt_replay_on" : "True"}, locked=False)]
        hotspot ((650,104, 300, 52)): #Глубина
            hovered [Show("sdl_achv_kat_me", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_kat_me", transition=Dissolve(0.5))]
            action [Show("sdl_achv_kat_me", transition=Dissolve(0.5))] 
        if persistent.alt_deep:
            hotspot ((590, 104, 50, 52)): #Tiefe-Ende-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active2", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active2", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))] 
                action [Hide("sdl_me_no_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_me_smtA", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_me_sm_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active2", transition=Dissolve(0.5)), Replay("alt_achv_deep_deep_Author", scope={"alt_replay_on" : "True"}, locked=False)]
        hotspot ((650,168, 300, 52)): #QTE       
            hovered [Show("sdl_achv_qte_me", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_qte_me", transition=Dissolve(0.5))]
            action [Show("sdl_achv_qte_me", transition=Dissolve(0.5))] 
        hotspot ((650,232, 300, 52)): #Постскриптум-Мику-7ДЛ
            hovered [Show("sdl_achv_pst_me", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_pst_me", transition=Dissolve(0.5))]
            action [Show("sdl_achv_pst_me", transition=Dissolve(0.5))] 
        if persistent.alt_mi_7dl_ps:
            hotspot ((590, 232, 50, 52)): #Postscriptum-Miku-Bitter-Jump
                hover_sound sdl_achv_click
                hovered [Show ("de_check_active4", transition=Dissolve(0.5)), Show ("sdl_achv_jumpchkA", transition=Dissolve(0.5))]
                unhovered [Hide ("de_check_active4", transition=Dissolve(0.5)), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5))] 
                action [Hide("sdl_sl_wh_inactive", transition=Dissolve(0.5)), Stop ("ambience"), Hide ("sdl_achv_jumpchkA", transition=Dissolve(0.5)), Hide("sdl_achv_me_smtA", transition=Dissolve(1.0)), Hide("sdl_logo_inactive", transition=Dissolve(0.5)), Hide("sdl_me_sm_active", transition=Dissolve(0.5)), Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5)), Hide("de_check_active3", transition=Dissolve(0.5)), Replay("alt_day7_mi_7dl_postscriptum", scope={"alt_replay_on" : "True"}, locked=False)]
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
            action [Hide("sdl_logo_inactive", transition=Dissolve(0.5)),Stop ("ambience"), Hide("sdl_me_no_inactive", transition=Dissolve(0.5)),Hide("sdl_me_sm_active", transition=Dissolve(0.5)), Hide("sdl_achv_me_smtA", transition=Dissolve(1.0)), Hide("sdl_achv_extA_7dl", transition=Dissolve(0.5)), Jump("main_menu_7dl")]
        hotspot ((380, 680, 170, 50)): #Удалятор
            hover_sound sdl_achv_click
            activate_sound sdl_achv_clear
            hovered [Show("sdl_achv_delA_7dl", transition=Dissolve(0.5))]
            unhovered [Hide("sdl_achv_delA_7dl", transition=Dissolve(0.5))]
            action Jump("sdl_achvlist_mesmt_clear_Author")
            
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
    $ persistent.sl_7dl_true = False
    $ persistent.sl_7dl_good_rf = False
    $ persistent.sl_7dl_loki_good = False
    $ persistent.sl_7dl_loki_neu = False
    $ persistent.sl_7dl_loki_rej = False
    $ persistent.sl_7dl_herc_good = False
    $ persistent.sl_7dl_herc_good2 = False
    $ persistent.sl_7dl_good = False
    $ persistent.sl_7dl_good2 = False
    $ persistent.sl_7dl_bad = False
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
######################УЛЬЯНА-7ДЛ######################################
label sdl_achvlist_us7dl_clear_Author:
    $ persistent.us_7dl_bad = False
    $ persistent.us_7dl_good = False
    $ persistent.us_7dl_true = False
    $ persistent.us_7dl_un = False
    $ persistent.us_7dl_mi = False
    call screen sdl_achvlist_us7dl_Author
# ------------------------------------------------ 
######################УЛЬЯНА-ОГОНЬКИ######################################
label sdl_achvlist_uspxs_clear_Author:
    $ persistent.us_px_rf_good = False
    $ persistent.us_px_true = False
    call screen sdl_achvlist_uspxs_Author
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
# ------------------------------------------------ 
######################ПРОЧИЕ ДОСТИЖЕНИЯ######################################
label sdl_achvlist_mesmt_clear_Author:
    $ persistent.alt_lamp = False
    $ persistent.alt_deep = False
    $ persistent.alt_qte = False
    $ persistent.alt_mi_7dl_ps = False
    call screen sdl_achvlist_mesmt_Author
    
##|||||||||||||||||||||||||||||||||||ДУБЛИ КОНЦОВОК||||||||||||||||||||||||||||||||||||||||||||||||      
    
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
    $ persistent.alt_deep = True
    show acm_logo_me_deep with moveinright:
    pause(3)
    scene black
    show gameover
    with gopr
    return

label alt_day7_sl_reject_late_ach:
    call alt_day7_sl_reject_late
    call alt_day7_sl_rej_mi
    call alt_day7_sl_rej_end