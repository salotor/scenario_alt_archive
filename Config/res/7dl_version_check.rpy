init:
    # Номер релиза сохранения, пустой по инициализации, в начале игры - присваивается номер релиза мода,
    # при загрузке:
    #  - если было сохранение с присвоением номера, при загрузке переменная будет взята из сохранения;
    #  - если загружается "старое" сохранение (до ввода процедуры контроля загрузок) - останется None 
    $ alt_save_release_no = None 

    $ alt_aicr_string = " "

    # определяем показываемый экран
screen alt_incompatible_release:
    tag menu
    modal True
    python: # почти цельностянуто из "menu:" в игре, цвета меняются со временем дня игры

        aicr_colors_hover = {'day': '#9dcd55', 'night': '#3ccfa2', 'sunset': '#dcd168', 'prologue': '#98d8da'}
        aicr_colors = {'day': '#466123', 'night': '#145644', 'sunset': '#69652f', 'prologue': '#496463'}
         
    window:
        text alt_aicr_string align (0.5, 0.05) color "#FF2500" font 'fonts/corbel.ttf' size 60 bold True text_align 0.5 line_spacing 20
        text u"РАБОТОСПОСОБНОСТЬ НЕ ГАРАНТИРУЕТСЯ. ВЫЛЕТ ИГРЫ ВОЗМОЖЕН В ЛЮБОЙ МОМЕНТ" align(0.5, 0.25) color "#FF2500" font 'fonts/corbel.ttf' size 60 bold True text_align 0.5 line_spacing 20
        text u"РЕКОМЕНДУЕТСЯ НАЧАТЬ ИГРУ ЗАНОВО"  align(0.5, 0.45) color aicr_colors_hover[persistent.timeofday] font 'fonts/corbel.ttf' size 60 bold True text_align 0.5 line_spacing 20
        text u"Ваши действия:"  align(0.5, 0.55) color aicr_colors_hover[persistent.timeofday] font 'fonts/corbel.ttf' size 55 bold True text_align 0.5 line_spacing 20

        right_padding 75
        bottom_padding 50
        yalign 0.5
        top_padding 50
        xfill True
        background (Frame(get_image((('gui/choice/' + persistent.timeofday) + '/choice_box.png')), 50, 50))
        left_padding 75
# кнопки выборов
        button: # начинаем заново
            xalign 0.5
            yalign 0.65
            action MainMenu(confirm=False)
            background None
            text u"Начать игру заново":
                hover_size 50
                color aicr_colors[persistent.timeofday]
                xcenter 0.5
                hover_color aicr_colors_hover[persistent.timeofday]
                font 'fonts/corbel.ttf'
                size 50
        button: # сначала удаляем (без предварительного запроса), потом начинаем заново. РАБОТАЕТ НЕ НА ВСЕХ СОХРАНЕНИЯХ. Будем выяснять.
            xalign 0.5
            yalign 0.75
            action [FileDelete(selected_slot, confirm=False), MainMenu(confirm=False)]
            background None
            text u"Удалить это сохранение и начать игру заново":
                hover_size 50
                color aicr_colors[persistent.timeofday]
                xcenter 0.5
                hover_color aicr_colors_hover[persistent.timeofday]
                font 'fonts/corbel.ttf'
                size 50
        button: # выходим в меню загрузки, ищем что-то другое
            xalign 0.5
            yalign 0.85
            action ShowMenu('load')
            background None
            text u"Выйти в меню загрузки":
                hover_size 50
                color aicr_colors[persistent.timeofday]
                xcenter 0.5
                hover_color aicr_colors_hover[persistent.timeofday]
                font 'fonts/corbel.ttf'
                size 50

# Для особо упёртых\упорных\…. Пробуем продолжить, авось получится. 
# Продолжение игры номер сохранения не перепишет; так что окно проверки будет вываливаться каждый раз
        button:  
            xalign 0.5
            yalign 0.95
            action Jump("alt_continue_game")
            background None
            text u"Загрузить это сохранение. На свой страх и риск, о возможных последствиях предупрежден.":
                hover_size 40
                color aicr_colors[persistent.timeofday]
                xcenter 0.5
                hover_color aicr_colors_hover[persistent.timeofday]
                font 'fonts/corbel.ttf'
                size 40


# После загрузки файла переходим именно в это место. Определено механикой Ренпая - 
# если есть метка 'after_load' - переходить на нее. В классике и других модах такая метка не обнаружена
# Не путать со служебной меткой '_after_load'

label after_load:

    # читаем 'save_name' и ищем в строке "7ДЛ" - думаю, этого дл идентификации мода достаточно
    if save_name.find(u'7ДЛ') != -1: #Если нашли вхождение '7ДЛ' в имени сохранения игры
        $ meet('ba',alt_meet['ba']) # повторный meet() с именами из собственного списка каналов спикеров после загрузки сохранения
        $ meet('ase',alt_meet['ase'])
        $ meet('we',alt_meet['we'])
        $ meet('ml',alt_meet['ml'])
        $ meet('ml2',alt_meet['ml2'])
        $ meet('ml3',alt_meet['ml3'])
        $ meet('voice1',alt_meet['voice1'])
        $ meet('kids',alt_meet['kids'])
        $ meet('dy',alt_meet['dy'])
        $ meet('icq',alt_meet['icq'])
        $ meet('el',alt_meet['el'])
        $ meet('un',alt_meet['un'])
        $ meet('dv',alt_meet['dv'])
        $ meet('sl',alt_meet['sl'])
        $ meet('us',alt_meet['us'])
        $ meet('mt',alt_meet['mt'])
        $ meet('cs',alt_meet['cs'])
        $ meet('mz',alt_meet['mz'])
        $ meet('mi',alt_meet['mi'])
        $ meet('uv',alt_meet['uv'])
        $ meet('bb',alt_meet['bb'])
        $ meet('sh',alt_meet['sh'])
        $ meet('ai',alt_meet['ai'])
        $ meet('sak',alt_meet['sak'])
        $ meet('me',alt_meet['me'])
        $ meet('pi',alt_meet['pi'])
        $ meet('dreamgirl',alt_meet['dreamgirl'])
        $ meet('voice',alt_meet['voice'])
        $ meet('voices',alt_meet['voices'])
        # Проверяем, совпадают ли версии сохранения и мода и есть ли версия сохранения в списке совместимых
        if (alt_release_no != alt_save_release_no) and (alt_save_release_no not in alt_compatible_release_no): # и если сохранение несовместимо

            python: # генерируем строку с номерами версий
                alt_aicr_string = (u"ЗАГРУЖАЕМАЯ ВЕРСИЯ СОХРАНЕНИЯ (%s) НЕСОВМЕСТИМА С ЭТОЙ ВЕРСИЕЙ МОДА (%s)") % (alt_save_release_no, alt_release_no)
            call screen alt_incompatible_release # и показываем экран предупреждения с выбором вариантов
        else:
            pass # версии совпали, играем дальше
    else: 
        pass # это не 7ДЛ, играем дальше

label alt_continue_game:
    return # .. и если все нормально - возвращаемся в игру