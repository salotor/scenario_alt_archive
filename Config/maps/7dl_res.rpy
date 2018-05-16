# Описываем 1-ю дополнительную карту ("малая" карта мода 7ДЛ)
# Ко всем идентификаторам добавляем суффикс "_alt1" ; этот же суффикс используем в описаниях дней

# отключение чибиков
init -1001 python:
    def disable_all_chibi_alt1():
        global global_zones_alt1
        for name,data in global_zones_alt1.iteritems():
            data["map_chibi"] = None


# Определяем источник изображений для картоосновы:
#    bgpic = "подложка"; avaliable = "доступно для выбора"; selected = "наведен курсор"

init -997 python:
    store.map_pics_alt1 = {
        "bgpic_alt1": get_image_7dl("gui/maps/map_bg.jpg"), 
        "avaliable_alt1": get_image_7dl("gui/maps/map_avaliable.jpg"), 
        "selected_alt1": get_image_7dl("gui/maps/map_selected.jpg")
    }

# Определяем ключи и координаты локаций данной карты:
#     ключи и координаты взяты из файла классики media.rpy
#     дополнительно добавлены из файла мода alt_script.rpy

init -996 python:
    store.map_zones_alt1 = {
# зоны, определенные в классике
            "me_mt_house_alt1":   {"position":[960,178,992,227],"default_bg":bg_tmp_image(u"Мой домик")},
            "estrade_alt1":       {"position":[1062,54,1154,135],"default_bg":bg_tmp_image(u"Эстрада")},
            "music_club_alt1":    {"position":[627,255,692,337],"default_bg":bg_tmp_image(u"Музклуб")},
            "square_alt1":        {"position":[887,360,998,545],"default_bg":bg_tmp_image(u"Площадь")},
            "dining_hall_alt1":   {"position":[1010,458,1137,581],"default_bg":bg_tmp_image(u"Столовая")},
            "sport_area_alt1":    {"position":[1220,481,1574,658],"default_bg":bg_tmp_image(u"Спорткомплекс")},
            "beach_alt1":         {"position":[1198,674,1488,831],"default_bg":bg_tmp_image(u"Пляж")},
            "boat_station_alt1":  {"position":[832,801,957,855],"default_bg":bg_tmp_image(u"Лодочный причал")},
            "clubs_alt1":         {"position":[437,437,647,597],"default_bg":bg_tmp_image(u"Клубы")},
            "library_alt1":       {"position":[1158,271,1285,357],"default_bg":bg_tmp_image(u"Библиотека")},
            "medic_house_alt1":   {"position":[1042,357,1138,444],"default_bg":bg_tmp_image(u"Медпункт")},
            "camp_entrance_alt1": {"position":[284,440,412,554],"default_bg":bg_tmp_image(u"Ворота в лагерь")},
            "forest_alt1":        {"position":[562,50,690,188],"default_bg":bg_tmp_image(u"о. Лес")},
# зоны, определенные в моде
            "un_mi_house_alt1":  {"position":[811,154,848,195],"default_bg":bg_tmp_image(u"Лена и Мику")},
            "sl_mz_house_alt1":  {"position":[1027,257,1058,300],"default_bg":bg_tmp_image(u"Славя и Женя")},
            "el_sh_house_alt1":  {"position":[854,292,884,331],"default_bg":bg_tmp_image(u"Эл и Шурик")},
            "dv_us_house_alt1":  {"position":[717,624,758,670],"default_bg":bg_tmp_image(u"Алиса и Ульяна")},
            "shed_alt1":         {"position":[1144,488,1211,584],"default_bg":bg_tmp_image(u"Склад")},
            "admin_house_alt1":  {"position":[790,350,860,447],"default_bg":bg_tmp_image(u"Администрация")},
            "old_house_alt1":    {"position":[238,1005,340,1071],"default_bg":bg_tmp_image(u"Старый корпус")}

    }

# Определяем новый класс нашей карты (сборка кода из mapclass.rpy и pyclasses.rpy оригинала)

init -51 python:
    global_map_result_alt1="error"

    def init_map_zones_realization_alt1(zones_alt1,default):
        global global_zones_alt1
        global_zones_alt1=zones_alt1
        for i,data in global_zones_alt1.iteritems():
            data["chibi"] = None
            data["label"] = default
            data["avaliable"] = True
            data["been_here"] = 0

    class Map_alt1(renpy.Displayable): 
        def __init__(self,pics,chibi,default):
            renpy.Displayable.__init__(self)
            self.pics=pics
            self.chibi=chibi
            self.default=default
            config.overlay_functions.append(self.overlay)

        def disable_all_zones(self):
            global global_zones_alt1
            for name,data in global_zones_alt1.iteritems():
                data["label"] = self.default
                data["avaliable"] = False
                data["been_here"] = 0
        def enable_all_zones(self):
            global global_zones_alt1
            for name,data in global_zones_alt1.iteritems():
                data["label"] = self.default
                data["avaliable"] = True
                data["been_here"] = 0
        def set_zone(self,name,label):
            global global_zones_alt1
            global_zones_alt1[name]["label"] = label
            global_zones_alt1[name]["avaliable"] = True
        def reset_zone(self,name):
            global global_zones_alt1
            global_zones_alt1[name]["label"] = self.default
            global_zones_alt1[name]["avaliable"] = False
            global_zones_alt1[name]["been_here"] = 0
        def enable_empty_zone(self,name):
            global global_zones_alt1
            self.set_zone(name,self.default)
            global_zones_alt1[name]["avaliable"] = True
        def reset_current_zone(self):
            self.enable_empty_zone(global_map_result_alt1)
        def disable_current_zone(self):
            global global_zones_alt1
            global_zones_alt1[global_map_result_alt1]["avaliable"] = False
        def been_there(self):
            global global_zones_alt1
            return global_zones_alt1[global_map_result_alt1]["been_here"]
        def set_chibi(self,name,ch):
            global global_zones_alt1
            if  ch in self.chibi:
                global_zones_alt1[name]["chibi"] = self.chibi[ch]
            else:
                global_zones_alt1[name]["chibi"] = None
        def reset_chibi(self,name):
            self.set_chibi(name,"")
        def event(self, ev, x, y, st):
            return
        def render(self, width, height, st, at):
            return renpy.Render(1, 1)
        def zoneclick(self,name):
            global global_zones_alt1
            global global_map_result_alt1
            store.map_enabled_alt1=False
            renpy.scene('mapoverlay')
            global_zones_alt1[name]["been_here"] += 1
            global_map_result_alt1 = name
            renpy.scene()
            if config.version == "1.0":
                if not not_in_rollback_or_fast_forward():
                    renpy.log("renpy.roll_forward_info()")
                    renpy.config.skipping = False
                    renpy.game.after_rollback = False
            ui.jumps(global_zones_alt1[name]["label"])()
        def overlay(self):
            if  store.map_enabled_alt1:
                global global_zones_alt1
                renpy.scene('mapoverlay')
                ui.layer('mapoverlay')
                for name,data in global_zones_alt1.iteritems():
                    if data["avaliable"]:
                        pos = data["position"]
                        ui.imagebutton(
                            im.Crop(self.pics["avaliable_alt1"],pos[0],pos[1],pos[2]-pos[0],pos[3]-pos[1]),
                            im.Crop(self.pics["selected_alt1"], pos[0],pos[1],pos[2]-pos[0],pos[3]-pos[1]), # добавляем сюда суффикс, и в альт_сторе тоже
                            clicked = renpy.curry(self.zoneclick)(name),
                            xpos = pos[0],
                            ypos = pos[1]
                        )
                        if  data["chibi"] != None:
                            ui.imagebutton(
                                anim.Blink(data["chibi"]),
                                anim.Blink(data["chibi"]),
                                clicked = renpy.curry(self.zoneclick)(name),
                                xpos = pos[0],
                                ypos = pos[1]
                            )
                ui.close()

# … и создаем новый объект класса
    store.map_alt1 = Map_alt1(store.map_pics_alt1, store.map_chibi, default) 

# Ниже кусок из pyclasses.rpy; возможно, есть и лишние строки - но без этого карта работать отказывалась
    import pygame
    import os
    import os.path
    from renpy.store import *
    from renpy.display.im import ImageBase, image, cache, Composite

    store.map_enabled_alt1 = False
    store.map_enabled_alt1_tmp = False
    def disable_stuff():
        store.map_enabled_alt1_tmp = store.map_enabled_alt1_tmp or store.map_enabled_alt1
        store.map_enabled_alt1 = False
    def enable_stuff():
        store.map_enabled_alt1 = store.map_enabled_alt1_tmp
        store.map_enabled_alt1_tmp = False

# инициализируем функции по методам вновь созданного класса

init 5 python:
    import renpy.store as store 
    if  not config_session:

        def disable_all_zones_alt1():
            store.map_alt1.disable_all_zones()
        def enable_all_zones_alt1():
            store.map_alt1.enable_all_zones()
        def set_zone_alt1(name,label):
            store.map_alt1.set_zone(name,label)
        def reset_zone_alt1(name):
            store.map_alt1.reset_zone(name)
        def enable_empty_zone_alt1(name):
            store.map_alt1.enable_empty_zone(name)
        def reset_current_zone_alt1():
            store.map_alt1.reset_current_zone()
        def disable_current_zone_alt1():
            store.map_alt1.disable_current_zone()
        def been_there_alt1():
            return store.map_alt1.been_there()
        def set_chibi_alt1(name,ch):
            store.map_alt1.set_chibi(name,ch)
        def reset_chibi_alt1(name):
            store.map_alt1.reset_chibi(name)
        def show_map_alt1():
            ui.jumps("_show_map_alt1")()
        def init_map_zones_alt1():
            init_map_zones_realization_alt1(store.map_zones_alt1,"nothing_here")

# определяем подосновы нашей карты (widget и bg) - собственно, подоснова карты:

init 5:
    if not config_session:
        image widget map_alt1 = get_image_7dl("gui/maps/map_bg.jpg")
        image bg map_alt1 = get_image_7dl("gui/maps/map_bg.jpg")

init 52 python:
    def disable_all_chibi_alt1():
        global global_zones_alt1
        for name,data in global_zones_alt1.iteritems():
            data["chibi"] = None

# инициализация зон карты должна проводиться один раз, при старте

# ну и собственно - выводим нашу карту на экран, любуемся ею и ждем-с нажатия мыша.

label _show_map_alt1:
    scene widget map_alt1
    $ store.map_enabled_alt1 = True #
    $ ui.interact()
    jump _show_map_alt1

# Описываем 2-ю дополнительную карту ("большая" карта мода 7ДЛ)
# Ко всем идентификаторам добавляем суффикс "_alt2" ; этот же суффикс используем в описаниях дней

# отключение чибиков - непонятно, зачем в этом месте - слишком рано.
init -1001 python:
    def disable_all_chibi_alt2():
        global global_zones_alt2
        for name,data in global_zones_alt2.iteritems():
            data["map_chibi"] = None


# Определяем источник изображений для картоосновы:
#    bgpic = "подложка"; avaliable = "доступно для выбора"; selected = "наведен курсор"

init -997 python:
    store.map_pics_alt2 = {
        "bgpic_alt2": get_image_7dl("gui/maps/7dl/7dl_bg.png"), 
        "avaliable_alt2": get_image_7dl("gui/maps/7dl/7dl_avaliable.png"), 
        "selected_alt2": get_image_7dl("gui/maps/7dl/7dl_selected.png") 
    }

# Определяем ключи и координаты локаций данной карты:
#     дополнительно добавлены РАЗДЕЛЬНЫЕ локации спорткомплекса и клубов.
#     (можно разделить еще спортзал и футбол, но надо перекрасить душевые на _avaliable и _selected картинках)

init -996 python:
    store.map_zones_alt2 = {
            "un_mi_house_alt2":   {"position":[659,312,692,352],"default_bg":bg_tmp_image(u"Лена и Мику")},
            "me_mt_house_alt2":   {"position":[785,334,819,374],"default_bg":bg_tmp_image(u"Мой домик")},
            "sl_mz_house_alt2":   {"position":[837,396,870,438],"default_bg":bg_tmp_image(u"Славя и Женя")},
            "estrade_alt2":       {"position":[870,234,939,306],"default_bg":bg_tmp_image(u"Эстрада")},
            "el_sh_house_alt2":   {"position":[693,425,721,465],"default_bg":bg_tmp_image(u"Эл и Шурик")},
            "music_club_alt2":    {"position":[509,400,568,468],"default_bg":bg_tmp_image(u"Музклуб")},
            "admin_house_alt2":   {"position":[632,479,715,560],"default_bg":bg_tmp_image(u"Админкорпус")},
            "wash_house_alt2":    {"position":[1061,292,1118,324],"default_bg":bg_tmp_image(u"Баня")},
            "square_alt2":        {"position":[723,490,818,646],"default_bg":bg_tmp_image(u"Площадь")},
            "dining_hall_alt2":   {"position":[825,565,934,671],"default_bg":bg_tmp_image(u"Столовая")},
            "dv_us_house_alt2":   {"position":[582,698,622,740],"default_bg":bg_tmp_image(u"Алиса и Ульяна")},
            "store_house_alt2":   {"position":[939,591,992,671],"default_bg":bg_tmp_image(u"Склад")},
            "cape_alt2":          {"position":[1211,948,1328,1070],"default_bg":bg_tmp_image(u"Мыс")},
            "sport_area_alt2":    {"position":[1000,508,1293,732],"default_bg":bg_tmp_image(u"Спорткомплекс")},
            "beach_alt2":         {"position":[976,746,1222,871],"default_bg":bg_tmp_image(u"Пляж")},
            "boat_station_alt2":  {"position":[679,849,781,892],"default_bg":bg_tmp_image(u"Лодочный причал")},
            "old_house_alt2":     {"position":[8,1019,88,1071],"default_bg":bg_tmp_image(u"Старый корпус")},
            "clubs_alt2":         {"position":[354,554,531,688],"default_bg":bg_tmp_image(u"Клубы")},
            "library_alt2":       {"position":[953,416,1052,485],"default_bg":bg_tmp_image(u"Библиотека")},
            "sandpit_alt2":       {"position":[1728,463,1918,721],"default_bg":bg_tmp_image(u"Карьер")},
            "medic_house_alt2":   {"position":[853,486,931,557],"default_bg":bg_tmp_image(u"Медпункт")},
            "camp_entrance_alt2": {"position":[229,554,333,645],"default_bg":bg_tmp_image(u"Остановка автобуса")},
            "forest_alt2":        {"position":[454,275,538,324],"default_bg":bg_tmp_image(u"Умывальники")},
            "islaone_alt2":       {"position":[453,960,706,1076],"default_bg":bg_tmp_image(u"о. Ближний")},
            "islatwo_alt2":       {"position":[711,992,1084,1077],"default_bg":bg_tmp_image(u"о. Длинный")},
            "lake_alt2":          {"position":[74,27,223,148],"default_bg":bg_tmp_image(u"Озеро")},
            "meadow_alt2":        {"position":[297,991,405,1079],"default_bg":bg_tmp_image(u"Луг")},
            "campfire_alt2":      {"position":[1501,970,1673,1072],"default_bg":bg_tmp_image(u"Костровая поляна")},
# раздельные локации спорткомплекса и клубов
            "sports_hall_alt2":   {"position":[1082,584,1290,732],"default_bg":bg_tmp_image(u"Спортзал и футбольное поле")},
            "volleyball_alt2":    {"position":[999,593,1079,685],"default_bg":bg_tmp_image(u"Воллейбольная площадка")},
            "court_alt2":         {"position":[1107,509,1176,576],"default_bg":bg_tmp_image(u"Теннисный корт")},
            "kyber_club_alt2":    {"position":[354,608,461,687],"default_bg":bg_tmp_image(u"Клуб кибернетиков")},
# секретнные зоны
            "secret_up_alt2":     {"position":[855,20,953,148],"default_bg":bg_tmp_image(u"Секретная зона вверху")},
            "secret_down_alt2":   {"position":[1758,849,1886,1007],"default_bg":bg_tmp_image(u"Секретная зона внизу")}

    }

# Определяем новый класс нашей карты (сборка кода из mapclass.rpy и pyclasses.rpy оригинала )

init -51 python:
    global_map_result_alt2="error"

    def init_map_zones_realization_alt2(zones_alt2,default):
        global global_zones_alt2
        global_zones_alt2=zones_alt2
        for i,data in global_zones_alt2.iteritems():
            data["chibi"] = None
            data["label"] = default
            data["avaliable"] = True
            data["been_here"] = 0

    class Map_alt2(renpy.Displayable): 
        def __init__(self,pics,chibi,default):
            renpy.Displayable.__init__(self)
            self.pics=pics
            self.chibi=chibi
            self.default=default
            config.overlay_functions.append(self.overlay)

        def disable_all_zones(self):
            global global_zones_alt2
            for name,data in global_zones_alt2.iteritems():
                data["label"] = self.default
                data["avaliable"] = False
                data["been_here"] = 0
        def enable_all_zones(self):
            global global_zones_alt2
            for name,data in global_zones_alt2.iteritems():
                data["label"] = self.default
                data["avaliable"] = True
                data["been_here"] = 0
        def set_zone(self,name,label):
            global global_zones_alt2
            global_zones_alt2[name]["label"] = label
            global_zones_alt2[name]["avaliable"] = True
        def reset_zone(self,name):
            global global_zones_alt2
            global_zones_alt2[name]["label"] = self.default
            global_zones_alt2[name]["avaliable"] = False
            global_zones_alt2[name]["been_here"] = 0
        def enable_empty_zone(self,name):
            global global_zones_alt2
            self.set_zone(name,self.default)
            global_zones_alt2[name]["avaliable"] = True
        def reset_current_zone(self):
            self.enable_empty_zone(global_map_result_alt2)
        def disable_current_zone(self):
            global global_zones_alt2
            global_zones_alt2[global_map_result_alt2]["avaliable"] = False
        def been_there(self):
            global global_zones_alt2
            return global_zones_alt2[global_map_result_alt2]["been_here"]
        def set_chibi(self,name,ch):
            global global_zones_alt2
            if  ch in self.chibi:
                global_zones_alt2[name]["chibi"] = self.chibi[ch]
            else:
                global_zones_alt2[name]["chibi"] = None
        def reset_chibi(self,name):
            self.set_chibi(name,"")
        def event(self, ev, x, y, st):
            return
        def render(self, width, height, st, at):
            return renpy.Render(1, 1)
        def zoneclick(self,name):
            global global_zones_alt2
            global global_map_result_alt2
            store.map_enabled_alt2=False
            renpy.scene('mapoverlay')
            global_zones_alt2[name]["been_here"] += 1
            global_map_result_alt2 = name
            renpy.scene()
            if config.version == "1.0":
                if not not_in_rollback_or_fast_forward():
                    renpy.log("renpy.roll_forward_info()")
                    renpy.config.skipping = False
                    renpy.game.after_rollback = False
            ui.jumps(global_zones_alt2[name]["label"])()
        def overlay(self):
            if  store.map_enabled_alt2:
                global global_zones_alt2
                renpy.scene('mapoverlay')
                ui.layer('mapoverlay')
                for name,data in global_zones_alt2.iteritems():
                    if data["avaliable"]:
                        pos = data["position"]
                        ui.imagebutton(
                            im.Crop(self.pics["avaliable_alt2"],pos[0],pos[1],pos[2]-pos[0],pos[3]-pos[1]),
                            im.Crop(self.pics["selected_alt2"], pos[0],pos[1],pos[2]-pos[0],pos[3]-pos[1]), # добавляем сюда суффикс, и в альт_сторе тоже
                            clicked = renpy.curry(self.zoneclick)(name),
                            xpos = pos[0],
                            ypos = pos[1]
                        )
                        if  data["chibi"] != None:
                            chibi_scale = im.Scale(data["chibi"],40,40) # масштабируем картинку чибика до нужного размера (напр. 40х40 пикс)
                            ui.imagebutton(
                                anim.Blink(chibi_scale), #показываем с измененным размером
                                anim.Blink(chibi_scale),
                                clicked = renpy.curry(self.zoneclick)(name),
                                xpos = pos[0],
                                ypos = pos[1]
                            )
                ui.close()

# … и создаем новый объект класса
    store.map_alt2 = Map_alt2(store.map_pics_alt2, store.map_chibi, default) 

# Ниже кусок из pyclasses.rpy; возможно, есть и лишние строки - но без этого карта работать отказывалась
    import pygame
    import os
    import os.path
    from renpy.store import *
    from renpy.display.im import ImageBase, image, cache, Composite

    store.map_enabled_alt2 = False
    store.map_enabled_alt2_tmp = False
    def disable_stuff():
        store.map_enabled_alt2_tmp = store.map_enabled_alt2_tmp or store.map_enabled_alt2
        store.map_enabled_alt2 = False
    def enable_stuff():
        store.map_enabled_alt2 = store.map_enabled_alt2_tmp
        store.map_enabled_alt2_tmp = False

# инициализируем функции по методам вновь созданного класса

init 5 python:
    import renpy.store as store 
    if not config_session:

        def disable_all_zones_alt2():
            store.map_alt2.disable_all_zones()
        def enable_all_zones_alt2():
            store.map_alt2.enable_all_zones()
        def set_zone_alt2(name,label):
            store.map_alt2.set_zone(name,label)
        def reset_zone_alt2(name):
            store.map_alt2.reset_zone(name)
        def enable_empty_zone_alt2(name):
            store.map_alt2.enable_empty_zone(name)
        def reset_current_zone_alt2():
            store.map_alt2.reset_current_zone()
        def disable_current_zone_alt2():
            store.map_alt2.disable_current_zone()
        def been_there_alt2():
            return store.map_alt2.been_there()
        def set_chibi_alt2(name,ch):
            store.map_alt2.set_chibi(name,ch)
        def reset_chibi_alt2(name):
            store.map_alt2.reset_chibi(name)
        def show_map_alt2():
            ui.jumps("_show_map_alt2")()
        def init_map_zones_alt2():
            init_map_zones_realization_alt2(store.map_zones_alt2,"nothing_here")

# определяем подосновы нашей карты (widget и bg) - собственно, подоснова карты:

init 5:
    if not config_session:
        image widget map_alt2 = get_image_7dl("gui/maps/7dl/7dl_bg.png")
        image bg map_alt2 = get_image_7dl("gui/maps/7dl/7dl_bg.png")

# еще раз отключаем чибиков 

init 52 python:
    def disable_all_chibi_alt2():
        global global_zones_alt2
        for name,data in global_zones_alt2.iteritems():
            data["chibi"] = None

# инициализация зон карты должна проводиться один раз, при старте

# ну и собственно - выводим нашу карту на экран, любуемся ею и ждем-с нажатия мыша.

label _show_map_alt2:
    scene widget map_alt2
    $ store.map_enabled_alt2 = True #
    $ ui.interact()
    jump _show_map_alt2

#    ЗАМЕЧАНИЯ ПО РЕАЛИЗАЦИИ
#-------------------------------
#    Чукча не писатель, чукча читатель.
#    Чукча не погромист (точнее, таки да, но совсем в другой области и на других языках).
#    Чукча две недели назад не умел ни в Питон, ни в Ренпай, от слова "совсем", да и сейчас не умеет.
#
#    Но вышенаписанное вроде бы как работает.
#    Скорее всего - в этом коде можно выкинуть что-то без потери функционала.