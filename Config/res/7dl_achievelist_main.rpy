##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ФУНКЦИИ И КЛАССЫ\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
init 2:
    $ sdl_achv_hovered_route = None
    $ sdl_achv_hovered_achv = None
    $ sdl_achv_hovered_jump = False
    $ sdl_achv_hovered_info = None
    $ sdl_achv_selected_route = None

label sdl_achv_reset_vars:
    $ sdl_achv_hovered_route = None
    $ sdl_achv_hovered_achv = None
    $ sdl_achv_hovered_jump = False
    $ sdl_achv_hovered_info = None
    $ sdl_achv_selected_route = None
    return

init python:
    # Сброс перзистентов
    def sdl_achv_clear_persistents_ask(achv_list):
        layout.yesno_screen(
            "Сбросить полученные концовки текущего рута?",
            yes = [Function(sdl_achv_clear_persistents, achv_list), Play("sound", sdl_achv_clear)],
            no  = NullAction()
            )
    
    def sdl_achv_clear_persistents(achv_list):
        for achv in achv_list:
            setattr(persistent, achv.get_persistent(), False)
        
        return
    
    
    
    # Das ist OOP!
    # Рут
    class sdl_achv_Route:
        def __init__(self, title, typology, icon_active, icon_inactive, achv_list, completed=True):
            self.title = title
            self.typology = typology
            self.icon_active = icon_active
            self.icon_inactive = icon_inactive
            self.achv_list = achv_list
            self.completed = completed
        
        def get_title(self):
            return self.title
        
        def get_typology(self):
            return self.typology
        
        def get_icon_active(self):
            return self.icon_active
        
        def get_icon_inactive(self):
            return self.icon_inactive
        
        def get_achv_list(self):
            return self.achv_list
        
        def is_completed(self):
            return self.completed
    
    # Ачивка
    class sdl_achv_Achievement:
        def __init__(self, icon, persistent, text, prerequisites, replay):
            self.icon = icon
            self.persistent = persistent
            self.text = text
            self.prerequisites = prerequisites
            self.replay = replay
        
        def get_icon(self):
            return self.icon
        
        def get_persistent(self):
            return self.persistent
        
        def get_text(self):
            return self.text
        
        def get_prerequisites(self):
            return self.prerequisites
        
        def get_replay(self):
            return self.replay
    
    # Требование к ачивке
    class sdl_achv_Prerequisite:
        def __init__(self, text, achievements):
            self.text = text
            self.achievements = achievements
        
        def check_conditions(self):
            if self.achievements == None:
                return False
            for achv in self.achievements:
                if getattr(persistent, achv.get_persistent()):
                    return True
            return False
        
        def get_text(self):
            return self.text
        
        def get_achievements(self):
            return self.achievements
    
    # Повтор
    class sdl_achv_Replay:
        def __init__(self, label, scope):
            self.label = label
            self.scope = scope
        
        def get_label(self):
            return self.label
        
        def get_scope(self):
            return self.scope



##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\МЕЛКИЕ ЭКРАНЫ\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# Кнопки персонажей
screen sdl_achv_main_buttons(parent_screen, character):
    tag main_buttons
    modal True
    
    # Мику
    if character == "mi":
        add "sdl_achv_mi_button_active" pos (0, 0)
    else:
        imagebutton pos (0, 0):
            hover_sound sdl_achv_pagina
            idle ("sdl_achv_mi_button_inactive")
            hover ("sdl_achv_mi_button_active")
            action [Hide(parent_screen, transition=Dissolve(0.5)), Call("sdl_achvlist_character", "mi", sdl_achv_mi_routes)]
    # Алисхен
    if character == "dv":
        add "sdl_achv_dv_button_active" pos (0, 343)
    else:
        imagebutton pos (0, 343):
            hover_sound sdl_achv_pagina
            idle ("sdl_achv_dv_button_inactive")
            hover ("sdl_achv_dv_button_active")
            action [Hide(parent_screen, transition=Dissolve(0.5)), Call("sdl_achvlist_character", "dv", sdl_achv_dv_routes)]
    # Славя
    if character == "sl":
        add "sdl_achv_sl_button_active" pos (0, 734)
    else:
        imagebutton pos (0, 734):
            hover_sound sdl_achv_pagina
            idle ("sdl_achv_sl_button_inactive")
            hover ("sdl_achv_sl_button_active")
            action [Hide(parent_screen, transition=Dissolve(0.5)), Call("sdl_achvlist_character", "sl", sdl_achv_sl_routes)]
    # Лена
    if character == "un":
        add "sdl_achv_un_button_active" pos (1289, 0)
    else:
        imagebutton pos (1289, 0):
            hover_sound sdl_achv_pagina
            idle ("sdl_achv_un_button_inactive")
            hover ("sdl_achv_un_button_active")
            action [Hide(parent_screen, transition=Dissolve(0.5)), Call("sdl_achvlist_character", "un", sdl_achv_un_routes)]
    # Ольга
    if character == "mt":
        add "sdl_achv_mt_button_active" pos (1560, 343)
    else:
        imagebutton pos (1560, 343):
            hover_sound sdl_achv_pagina
            idle ("sdl_achv_mt_button_inactive")
            hover ("sdl_achv_mt_button_active")
            action [Hide(parent_screen, transition=Dissolve(0.5)), Call("sdl_achvlist_character", "mt", sdl_achv_mt_routes)]
    # Ульяна
    if character == "us":
        add "sdl_achv_us_button_active" pos (1562, 530)
    else:
        imagebutton pos (1562, 530):
            hover_sound sdl_achv_pagina
            idle ("sdl_achv_us_button_inactive")
            hover ("sdl_achv_us_button_active")
            action [Hide(parent_screen, transition=Dissolve(0.5)), Call("sdl_achvlist_character", "us", sdl_achv_us_routes)]
    # Одиночка
    if character == "me":
        add "sdl_achv_me_button_active" pos (1289, 735)
    else:
        imagebutton pos (1289, 735):
            hover_sound sdl_achv_pagina
            idle ("sdl_achv_me_button_inactive")
            hover ("sdl_achv_me_button_active")
            action [Hide(parent_screen, transition=Dissolve(0.5)), Call("sdl_achvlist_character", "me", sdl_achv_me_routes)]
    
    # Выход
    imagebutton pos (380, 350):
        hover_sound sdl_achv_pagina
        idle ("sdl_achv_ext_inactive")
        hover ("sdl_achv_ext_active")
        action [Stop("ambience"), Hide(parent_screen, transition=Dissolve(0.5)), Jump("main_menu_7dl")]
# ------------------------------------------------------------------------------------------------
# Экран рута
screen sdl_achv_route(parent_screen, achv_list):
    tag route
    modal True
    
    # Удалятор
    imagebutton pos (380, 680):
        hover_sound sdl_achv_click
        idle ("sdl_achv_del_inactive")
        hover ("sdl_achv_del_active")
        action [Function(sdl_achv_clear_persistents_ask, achv_list)]
    
    # Ачивки
    $ sdl_achv_count = 0
    for achv in achv_list:
        if getattr(persistent, achv.get_persistent()):
            # Значок ачивки
            imagebutton xcenter 800 ycenter (66 + 64 * sdl_achv_count):
                idle (achv.get_icon())
                hovered [SetVariable("sdl_achv_hovered_achv", achv)]
                unhovered [SetVariable("sdl_achv_hovered_achv", None)]
                action [SetVariable("sdl_achv_hovered_achv", achv)]
            
            if achv.get_replay() != None:
                # Кнопка перехода к концовке
                imagebutton pos (590, 40 + 64 * sdl_achv_count):
                    hover_sound sdl_achv_click
                    idle ("sdl_achv_check_inactive")
                    hover ("sdl_achv_check_active")
                    hovered [SetVariable("sdl_achv_hovered_jump", True)]
                    unhovered [SetVariable("sdl_achv_hovered_jump", False)]
                    action [Stop("ambience"), SetVariable("sdl_achv_hovered_jump", False), Replay(achv.get_replay().get_label(), scope=achv.get_replay().get_scope(), locked=False), Play('ambience', default_7dl_path+"Sound/ambience/ambience_safe_7dl.ogg", fadein=5.0)]
        else:
            # Заблокированная ачивка
            imagebutton xcenter 800 ycenter (66 + 64 * sdl_achv_count):
                idle ("sdl_achv_lock")
                hovered [SetVariable("sdl_achv_hovered_achv", achv)]
                unhovered [SetVariable("sdl_achv_hovered_achv", None)]
                action [SetVariable("sdl_achv_hovered_achv", achv)]
            
            # Иконка пререквизитов
            $ sdl_achv_prerequisites = achv.get_prerequisites()
            for prerequisite in sdl_achv_prerequisites:
                if not prerequisite.check_conditions():
                    imagebutton pos (590, 40 + 64 * sdl_achv_count):
                        hover_sound sdl_achv_info
                        idle ("sdl_achv_info_inactive")
                        hover ("sdl_achv_info_active")
                        hovered [SetVariable("sdl_achv_hovered_info", achv.get_prerequisites())]
                        unhovered [SetVariable("sdl_achv_hovered_info", None)]
                        action [SetVariable("sdl_achv_hovered_info", achv.get_prerequisites())]
                    $ sdl_achv_prerequisites = {}
        $ sdl_achv_count += 1
    
    # Всплывающая инфа
    if sdl_achv_hovered_achv != None:
        add sdl_achv_hovered_achv.get_text() xcenter 700 ycenter 840
    
    if sdl_achv_hovered_jump == True:
        add "sdl_achv_jump" xcenter 700 ycenter 840
    
    if sdl_achv_hovered_info != None:
        use sdl_achv_prerequisites(sdl_achv_hovered_info)

# Экран пререквизитов
screen sdl_achv_prerequisites(prerequisites):
    frame xalign 0.5 yalign 0.5:
        background Frame("sdl_achv_frame", 0, 0)
        
        vbox:
            spacing 25
            null height 25
            for prerequisite in prerequisites:
                if not prerequisite.check_conditions():
                    hbox xalign 0.5:
                        spacing 25
                        null width 25
                        add prerequisite.get_text() xalign 0.5
                        null width 25
                    if prerequisite.get_achievements() != None:
                        hbox xalign 0.5:
                            spacing 25
                            null width 25
                            $ sdl_not_first_image = False
                            for prereq_achv in prerequisite.get_achievements():
                                if sdl_not_first_image:
                                    add "sdl_achv_info_or"
                                vbox:
                                    spacing 10
                                    add prereq_achv.get_icon()
                                    add prereq_achv.get_text() zoom 0.5 xalign 0.5
                                $ sdl_not_first_image = True
                            null width 25
            null height 25



##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\НАЧАЛЬНЫЙ ЭКРАН\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
label sdl_achvlist_main:
    if (renpy.version(tuple=False) == "Ren'Py 6.16.3.502") or (renpy.version(tuple=False) == "Ren'Py 6.18.3.761"):
### кусок из старой версии ачивлиста
        $ day_time()
        $ persistent.sprite_time = "day"
        $ plthr = u"Достижения"
        play ambience ambience_7dl["safe"] fadein 5
        scene bg sdl_old_ach_inactive
        show sdl_old_achv_extB_7dl:
            pos(380, 350)
        $ renpy.block_rollback()
        call screen sdl_old_achvlist_Author
###
    else:
        $ day_time()
        $ persistent.sprite_time = "day"
        $ plthr = u"Достижения"
        play ambience ambience_7dl["safe"] fadein 5
        
        $ renpy.block_rollback()
        call screen sdl_achvlist_main
        
screen sdl_achvlist_main:
    tag menu
    modal True
    
    add "sdl_achv_screen_main"
    
    # Кнопки персонажей
    use sdl_achv_main_buttons("sdl_achvlist_main", None)

##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ЭКРАН ПЕРСОНАЖА\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
label sdl_achvlist_character(character, route_list):
    call sdl_achv_reset_vars
    
    call screen sdl_achvlist_character(character, route_list)

screen sdl_achvlist_character(character, route_list):
    tag menu
    modal True
    
    add ("sdl_achv_screen_" + character)
    
    # Руты
    $ sdl_route_count = 0
    for route in route_list:
        if sdl_achv_selected_route == route:
            add route.get_icon_active() pos (980 + 117 * sdl_route_count, 18)
        else:
            imagebutton pos (980 + 117 * sdl_route_count, 18):
                hover_sound sdl_achv_click
                idle (route.get_icon_inactive())
                hover (route.get_icon_active())
                hovered [SetVariable("sdl_achv_hovered_route", route)]
                unhovered [SetVariable("sdl_achv_hovered_route", None)]
                action [SetVariable("sdl_achv_selected_route", route)]
        $ sdl_route_count += 1
    
    # Кнопки персонажей
    use sdl_achv_main_buttons("sdl_achvlist_character", character)
    
    # Всплывающая инфа
    if sdl_achv_hovered_route != None:
        add sdl_achv_hovered_route.get_typology() pos (380, 540)
        add sdl_achv_hovered_route.get_title() xcenter 960 ycenter 1010
        if not sdl_achv_hovered_route.is_completed():
            add "sdl_achv_need_route" xcenter 700 ycenter 840
    elif sdl_achv_selected_route != None:
        add sdl_achv_selected_route.get_typology() pos (380, 540)
        add sdl_achv_selected_route.get_title() xcenter 960 ycenter 1010
        if not sdl_achv_selected_route.is_completed():
            add "sdl_achv_need_route" xcenter 700 ycenter 840
    
    # Выбранный рут
    if sdl_achv_selected_route != None:
        use sdl_achv_route("sdl_achvlist_character", sdl_achv_selected_route.get_achv_list())
