label alt_day3_slots:
    stop music
    stop ambience
    stop sound_loop
    window hide
    scene black
    with dissolve
    
label alt_day3_router_dv:
    if alt_day3_dv_evening:
        "Поворочавшись, я улыбнулся посетившей мои сны Алисе."
        if lp_dv >= 11:
        "Мне снилась Алиса…"
        window hide
        if alt_day3_dv_evening:
            $ routetag = "dv7dl"
            jump alt_day4_dv_7dl_start
        else:
            jump alt_day3_router_un
            
label alt_day3_router_un:
    if lp_un >= 12 or (lp_un >= 11 and alt_day1_sl_conv):
        "Мне снилась Лена…"
        window hide
    if (alt_day3_un_med_help == 1) and (lp_un >= 12):
        $ routetag = "un7dl"
        jump alt_day4_un_7dl_start
    elif (alt_day2_date == 132) and (alt_day3_dancing == 132):
        $ routetag = "un7dl"
        jump alt_day4_un_fz_start
    else:
        jump alt_day3_router_mi

label alt_day3_router_mi:
    if lp_mi >= 13:
        if alt_day3_mi_dj:
            "Мне снилась Мику…"
            "Правда, не очень долго."
            window hide
            $ routetag = "mi7dl"
            jump alt_day4_mi_dj_start
    else:
        jump alt_day3_router_sl

label alt_day3_router_sl:
    if alt_day3_sl_day_event2 and lp_sl >= 13:
        "Мне снилась Славя…"
        window hide
        if alt_day3_technoquest_st3 == 2:
            $ routetag = "sl"
            jump alt_day4_sl_start
        else:
            $ routetag = "sl7dl"
            jump alt_day4_sl_7dl_start
    else:
        jump alt_day3_router_neutral
    
label alt_day3_router_neutral:
    if alt_dlc_active and alt_day3_uvao_spotted:
        $ routetag = "uv"
        "Сон был тревожным…"
        window hide
        jump alt_day4_start_uvao #Начало ЮВАО-рута
    else:
         jump alt_day4_neu_begin
         
         
label alt_day4_neu_begin:
    if alt_day3_dv_evening:
        call alt_day4_neu_dv #Эксклюзивный вход для Алисы
    elif alt_day3_technoquest_st3 == 2:
        call alt_day4_neu_aid #Точка входа для медпункта, описание.
        if alt_day3_un_med_help != 0:
            call alt_day4_neu_aid_un
            pause(1)
            if alt_day4_neu_transit == 11:
                jump alt_day4_un_cl_dinner
        pause(1)
        call alt_day4_neu_aid_sl
        if alt_day4_neu_transit == 2:
            jump alt_day4_sl_cl_shurik
        pause(1)
        call alt_day4_neu_aid_generic
        pause(1)
        if alt_day4_neu_transit == 6:
            call alt_day4_neu_mt
        else:
            call alt_day4_neu_us
    else:
        call alt_day4_neu_home #Домик ведёт к Ульянке, Ольге, Лене и Мику. 
        pause(1)
        if alt_day3_un_med_help != 0:
            call alt_day4_neu_un
            pause(1)
            if alt_day4_neu_transit == 1:
                jump alt_day4_un_7dl_dinner
            else:
                call alt_day4_neu_mt
        elif alt_day3_mi_date:
            call alt_day4_neu_mi
            pause(1)
        else:
            call alt_day4_neu_sl
            pause(1)
            if alt_day4_neu_transit == 6:
                call alt_day4_neu_mt
            else:
                call alt_day4_neu_us
    pause(1)        
    call alt_day4_neu_dinner #На обеде подводим итоги
    pause(1)
    call alt_day4_neu_curl
    pause(1)
    call alt_day4_neu_lunch 
    pause(1)
    call alt_day4_neu_supper
    pause(1)
    if alt_day4_neu_transit == 6:
        call alt_day4_neu_map_me_mt_house
        pause(1)
        #if alt_day4_neu_mt_diary #Флаг для просмотра дневника
    elif alt_day4_neu_transit == 5:   
        call alt_day4_neu_map_hideout
        pause(1)
        if not alt_day4_neu_mt:
            call alt_day4_neu_map_meadow
    else:
        call alt_day4_neu_map_dining_hall
    pause(1)
    call alt_day4_neu_sleeptime
    pause(1)
    jump alt_day5_neu_begin
    
label alt_day5_neu_begin:
    #День 5: утро??? В обед неудачник отправляется следить за Славей, Огонёк идёт на Карьер рядом с лесом памяти, там встречает Лену и запускает новую стадию огоньков и длится это до ужина. В полдник неудачник отправляется по картошку, следит за ругающейся Алисой. Ужин, неудачник отправляется на костёр, там делится с Ульянкой картохой(или нет, как сам захочет), "Огонёк" рассказывает од, что прознал, куда сбежала Лена, и почему её никто не нашёл, на костре наблюдает за вспышкой агрессии Алисы и шутит на эту тему - мол, ревнует Ульянку. Далее "неудачник" просыпается дома, далее идёт описание нескольких месяцев прозябания, но однажды в квартире разносится новый звонок, приглашающий на очередную встречу, и в зависимости от выбора  можно либо встретить мелочь на обратном пути, либо вернуться домой, пр хватив по пути пару бутылок удивительно дешёвого джина. Глоток, ещё глоток, слепота, метил, "ты пойдёшь со мной?" Огонёк же уходит на д6.    
    jump alt_day6_neu_begin
    
label alt_day6_neu_begin:
    jump alt_day7_neu_begin

label alt_day7_neu_begin:
    call alt_day7_neu_departure
    pause(1)
    If alt_day6_neu_var1:
        call alt_day7_neu_ending_good
    elIf alt_day6_neu_var2:
        call alt_day7_neu_ending_bad
    elIf alt_day6_neu_var3:
        call alt_day7_neu_ending_mi
    else alt_day6_neu_var4:
        call alt_day7_neu_ending_d3
return
