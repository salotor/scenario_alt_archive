﻿init:
    $ style.alt_days = Style(style.default)
    $ style.alt_days.color = "#390874"
    $ style.alt_days.italic = False
    $ style.alt_days.bold = True
    $ style.alt_days.size = 64
    $ style.alt_days.text_align = 0.5

    $ style.alt_chapters = Style(style.default)
    $ style.alt_chapters.color = "#2572ff"
    $ style.alt_chapters.italic = False
    $ style.alt_chapters.bold = True
    $ style.alt_chapters.size = 48
    $ style.alt_chapters.text_align = 0.5
    
    $ style.alt_credits = Style(style.default)
    $ style.alt_credits.color = "#EFF"
    $ style.alt_credits.drop_shadow = [ (1, 1), (1, 1), (1, 1), (1, 1) ]
    $ style.alt_credits.drop_shadow_color = "#111"
    $ style.alt_credits.italic = False
    $ style.alt_credits.bold = False
    $ style.alt_credits.text_align = 0.5
    image alt_credits = ParameterizedText(style = "alt_credits", size = 50)
    
    $ style.alt_letter = Style(style.default)
    $ style.alt_letter.color = "#00ffff"
    $ style.alt_letter.drop_shadow = [ (-1, 0), (0, 0), (-1, 1), (0, 1) ]
    $ style.alt_letter.drop_shadow_color = "#0ff"
    $ style.alt_letter.italic = True
    $ style.alt_letter.bold = False
    
    image alt_letter = ParameterizedText(style = "alt_letter", size = 70)
    
init:
    if not ((renpy.version(tuple=False) == "Ren'Py 6.16.3.502") or (renpy.version(tuple=False) == "Ren'Py 6.18.3.761")):
        if renpy.mobile:
            $ style.base_font = Style(style.default)
            $ style.base_font.font  = get_image_7dl("fonts/calibri.ttf")
            $ style.base_font.size = 28
            $ style.base_font.line_spacing = 2
            
            $ style.chapter = Style(style.base_font)
            $ style.chapter.font  = get_image_7dl("fonts/corbel.ttf")
            $ style.chapter.size = 120
            $ style.chapter.color = "#fff"
            $ style.chapter.outlines = [ (1, "#ffdd7d", 0, 0) ]
            
            $ style.daynum = Style(style.chapter)
            $ style.daynum.font  = get_image_7dl("fonts/corbel.ttf")
            $ style.daynum.size = 45

init -66 python:
    import random
    
    class alt_CardGameRival:
        
        def __init__(self,avatar,name):
            self.name = name
            self.mood = 0
            self.avatar = avatar
        
        def pick_my_card_last(self):
            for i in range(0,n_cards):
                if  cards_my[i].interesting:
                    x = i
            return x
        
        def allow_to_take(self):
            for i in range(0,n_cards):
                cards_rival[i].allow = True
        
        def allow_to_defend(self):
            return True
        
        def want_to_defend(self):
            return True
        
        def what_to_xchange(self):
            i = random.randrange(0,n_cards)
            j = random.randrange(0,n_cards)
            while i==j:
                j = random.randrange(0,n_cards)
            return (i,j)
        
        def give_away_card(self):
            return random.randrange(0,n_cards)
    
    class CardGameRivalSl(alt_CardGameRival):
        def pick_my_card(self):
            x = random.randrange(0,n_cards)
            while cards_my[x].name == name_of_none or cards_my[x].interesting:
                x = random.randrange(0,n_cards)
            return x
        
        def pick_my_card_last(self):
            return self.pick_my_card()
    
    class CardGameRivalSh(alt_CardGameRival):
        def pick_my_card(self):
            x = random.randrange(0,n_cards)
            while cards_my[x].name == name_of_none or cards_my[x].interesting:
                x = random.randrange(0,n_cards)
            return x
        
        def pick_my_card_last(self):
            return self.pick_my_card()
    
    class CardGameRivalMz(alt_CardGameRival):
        def pick_my_card(self):
            x = random.randrange(0,n_cards)
            while cards_my[x].name == name_of_none or cards_my[x].interesting:
                x = random.randrange(0,n_cards)
            return x
        
        def pick_my_card_last(self):
            return self.pick_my_card()
    
    class CardGameRivalMi(alt_CardGameRival):
        def pick_my_card(self):
            x = random.randrange(0,n_cards)
            while cards_my[x].name == name_of_none or cards_my[x].interesting:
                x = random.randrange(0,n_cards)
            return x
        
        def pick_my_card_last(self):
            return self.pick_my_card()
            
init -10 python:
    p = get_image_7dl("gui/avaset/sh/sh-")
    sh_avatar_set = {
                 'body':p+"body.png",
                 0     :p+"emo6.png",
            }
            
    p = get_image_7dl("gui/avaset/mi/mi-")
    mi_avatar_set = {
                 'body':p+"body.png",
                 0     :p+"emo5.png",
            }
            
    p = get_image_7dl("gui/avaset/mz/mz-")
    mz_avatar_set = {
                 'body':p+"body.png",
                 0     :p+"emo6.png",
            }
        
init 3 python:

    if not renpy.version(tuple=False) == "Ren'Py 6.16.3.502":
        def meet(who, name):
            global store
            gl = globals()
            gl[who + "_name"] = name
            store.names[who] = name

        def save_names_known():
            gl = globals()
            global store
            for x in store.names_list:
                if not (x == 'narrator' or x == 'th'):
                    store.names[x] = gl["%s_name"%x]

    def make_names_unknown_7dl():
        global store
        meet('ai',u"Собеседник")
        meet('al',u"Сердитый мальчик")
        meet('am',u"Я")
        meet('ase',u"Девочка")
        meet('ba',u"Физрук")
        meet('bb',u"Начальник лагеря")
        meet('cs',u"Медсестра")
        meet('dn',u"Кудрявый")
        meet('dreamgirl',u"…")
        meet('dv',u"Рыжая")
        meet('dy',u"Динамики")
        meet('el',u"Кудрявый")
        meet('ka',u"Вожатая 2-го отряда")
        meet('kids',u"Дети")
        meet('ln',u"Странная девочка")
        meet('me',u"Семён")
        meet('mi',u"Японка")
        meet('ml',u"Мальчик")
        meet('ml2',u"Мальчик")
        meet('ml3',u"Мальчик")
        meet('mt',u"Вожатая")
        meet('mz',u"Девушка в очках")
        meet('pi',u"Пионер")
        meet('sak',u"Пожилой японец")
        meet('sh',u"Очкарик")
        meet('sl',u"Блондинка")
        meet('tn',u"Странный мальчик")
        meet('un',u"Грустная девочка")
        meet('us',u"Мелкая")
        meet('uv',u"Кошкодевочка")
        meet('voice',u"Голос")
        meet('voice1',u"Продавщица")
        meet('voices',u"Голоса")
        meet('we',u"Хором")
        
    def make_names_known_7dl():
        global store
        meet('al',u"Алька")
        meet('ase',u"Алиса")
        meet('ba',u"Саныч")
        meet('bb',u"Алексей Максимыч")
        meet('cs',u"Виола")
        meet('dn',u"Даня")
        meet('dv',u"Алиса")
        meet('dy',u"Динамики")
        meet('el',u"Электроник")
        meet('ka',u"Катюшка")
        meet('ln',u"Алёна")
        meet('mi',u"Мику")
        meet('mt',u"Ольга Дмитриевна")
        meet('mz',u"Женя")
        meet('sak',u"Сакишита Тихиро")
        meet('sh',u"Шурик")
        meet('sl',u"Славя")
        meet('tn',u"Тоник")
        meet('un',u"Лена")
        meet('us',u"Ульянка")
        meet('uv',u"Юля")
        
    make_names_unknown_7dl()
    set_mode_adv()
    reload_names()

init -265 python: 
    #Пресеты с возможностью настройки
    def Noir(id, brightness = -0.4, tint_r = 0.2126, tint_g = 0.7152, tint_b = 0.0722, saturation = 0.5):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(brightness) * im.matrix.tint(tint_r, tint_g, tint_b) * im.matrix.saturation(saturation))
    def D3_intro(id, brightness = -0.2, opacity = 0.5):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(brightness) *  im.matrix.opacity(opacity))
    def Desat(id, brightness = -0.35, saturation = 0.5):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(brightness) *  im.matrix.saturation(saturation))
    def Desat1(id, brightness = -0.4, saturation = 0.35):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(brightness) *  im.matrix.saturation(saturation))
        
    #Пресеты без возможности настройки
    def SS_com(id):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(-0.2) * im.matrix.contrast(1.6) * im.matrix.saturation(0)* im.matrix.colorize("#0aa", "#000"))
        
    def SS_com_r(id):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(-0.2) * im.matrix.contrast(1.6) * im.matrix.saturation(0)* im.matrix.colorize("#a00", "#000"))
        
    def Sepia(id):
        return im.MatrixColor(ImageReference(id), im.matrix.saturation(0.15) * im.matrix.tint(1.0, .94, .76))
        
    #Тинты для разного времени суток    
    def Notch(id):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(-0.2) * im.matrix.saturation(0.6))
    def Dawn(id):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(-0.1) * im.matrix.tint(0.94, 0.82, 1.0))
    def Noon(id):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(0.2) * im.matrix.tint(1.0, 0.94, 0.82))
    def HomeCity(id):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(-0.1) * im.matrix.tint(0.82, 0.84, 1.0))
    def Rained(id):
        return im.MatrixColor(ImageReference(id), im.matrix.brightness(-0.4) * im.matrix.tint(0.68, 0.90, 0.8) * im.matrix.saturation(0.6))

    def filmetile(bitmap, opacity=0.1):
        return im.Tile(im.Alpha(bitmap,opacity))

init -6 python:
    def alt_chapter0():
        global save_name
        save_name = (u"7ДЛ v.%s.%s: пролог. %s") % (alt_release_no, alt_hotfix_no, plthr)

init -5 python:
    def alt_chapter(alt_day_number, alt_chapter_name):
        global save_name
        renpy.block_rollback()
# ----------------------------------------------------------------------
# в имя сохраняемого файла добавим номер релиза игры
        sdn = (u"7ДЛ v.%s.%s: День %d") % (alt_release_no, alt_hotfix_no, alt_day_number)
        save_name = ((sdn) + (u" - ")) + (alt_chapter_name)
# -----------------------------------------------------------------------
        if not persistent.chapter_off_7dl:
            renpy.scene()
            if persistent.sprite_time == "day":
                renpy.show('bg ext_stand3_7dl')
            elif persistent.sprite_time == "sunset":
                renpy.show('bg ext_stand3_sunset_7dl')
            elif persistent.sprite_time == "night":
                renpy.show('bg ext_stand3_night_7dl')
            elif persistent.sprite_time == "prolog":
                renpy.show('bg ext_stand3_prolog_7dl')
            renpy.pause(1.0)
            renpy.transition(dissolve)
            
            if routetag == "dv": #Классическая и диджей ветка гуд
                renpy.show("dv normal pioneer2", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
            elif routetag == "dvbad": #Классическая ветка, бэд, диджей ветка дисмисс
                renpy.show("dv sad pioneer2", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)    
               
            elif routetag == "dv7dl": #7дл-ветка, гуд
                renpy.show("dv normal pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "dv7dlbad": #7дл-ветка, реджект/дисмисс
                renpy.show("dv guilty pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "dv7dlgood": #7дл-ветка, гуд
                renpy.show("dv smile pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
                

            elif routetag == "mi7dl": #7дл-ветка, диджей гуд
                renpy.show("mi normal pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "mi7": #Мику-коммон
                renpy.show("mi sad pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "mi7dlbad": #7дл-ветка, реджект, диджей нейтрал
                renpy.show("mi cry pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "mi7dlgood": #7дл-ветка, реджект, диджей нейтрал
                renpy.show("mi happy pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "mi7dldress":
                renpy.show("mi normal dress", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "mi7rej": #7дл-ветка, реджект, диджей бэд
                renpy.show("mi serious pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "mi7true": #7дл-ветка, реджект, диджей бэд
                renpy.show("mi shy pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "mi7dlvoca":
                renpy.show("mi shy voca", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "mi7dlcas":
                renpy.show("mi happy casual", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "mi7dlcas1":
                renpy.show("mi sad casual", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "mi7dlcas1":
                renpy.show("mi cry casual", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "mi7dlvoca1":
                renpy.show("mi sad voca", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
                
            elif routetag == "sl": #Классическая ветка, нормал
                renpy.show("sl normal pioneer2", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "sltrue": #Классик, тру
                renpy.show("sl shy sport", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "slcas": #Классическая ветка гуд
                renpy.show("sl smile casual", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "slbad": #Классическая ветка, бэд
                renpy.show("sl sad pioneer2", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)    
            
            elif routetag == "sl7dl": #Ветка 7дл, базис
                renpy.show("sl normal pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "sl7dl_herc": #Ветка 7дл, Герк
                renpy.show("sl smile pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "sl7dl_loki": #Ветка 7дл, Локи
                renpy.show("sl smile2 pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
                
            elif routetag == "sl7dl_sport": #Ветка 7дл, спортивная
                renpy.show("sl smile sport", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "sl7dl_dress": #Ветка 7дл, платье
                renpy.show("sl smile2 dress", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            
            elif routetag == "sl7dltrue": #Ветка 7дл, тру
                renpy.show("sl_gr normal casual", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "sl7dlneu": #Ветка 7дл, тру
                renpy.show("sl serious casual", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "sl7dlgood": #Ветка 7дл, тру
                renpy.show("sl happy casual", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "sl7dluv": #Ветка 7дл, тру
                renpy.show("sl normal_uv dress", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "sl7dlbad": #Ветка 7дл, тру
                renpy.show("sl cry pioneer2", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            
            elif routetag == "un": #Классическая
                renpy.show("un normal pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
            elif routetag == "unbad": #Классическая ветка, бэд
                renpy.show("un sad pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)    
                
            elif routetag == "un7dl": #7дл-ветка, гуд
                renpy.show("un normal pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            #Флаг для плохого эпилога Лены
            elif routetag == "un7dlbad": #7дл-ветка, реджект/бэд
                renpy.show("un sorrow modern", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "un7dlgood": #7дл-ветка, реджект/бэд
                renpy.show("un smile modern", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)    
                
            elif routetag == "mt7dl": #Ольга - общая
                renpy.show("mt grin pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "mt7dl_bad": #Ольга - плохая концовка
                renpy.show("mt sad pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
                
            elif routetag == "us7dl_good":
                renpy.show("us smile sport", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
                
            elif routetag == "us7dl_good_surp":
                renpy.show("us surp1 sport", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
                
            elif routetag == "us7dl_bad":
                renpy.show("us normal pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
                
            elif routetag == "us7dl_bad_laugh":
                renpy.show("us laugh pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
                
            elif routetag == "us7dl_bad_sad":
                renpy.show("us sad pioneer", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
                
            elif routetag == "uv_unknown": #Кошочку еще не знаем
                renpy.show("uv black silhouette", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "uv": #Кошонка-распашонка
                renpy.show("uv normal", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "uv_true": #Кошочка поражена до самой глыбины своих глыбин
                renpy.show("uv surprise", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "uv_false": #Кошонка на позитиве
                renpy.show("uv grin", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
            elif routetag == "uv_bad": #Виноватая кошонка
                renpy.show("uv guilty", zorder=1, at_list=[left])
                renpy.transition(moveinleft)
                renpy.pause(2.0)
                
            else:
                renpy.show("owl")
                renpy.pause(0.3)
            
            dn = (u"7ДЛ: День %d") % (alt_day_number)
            if persistent.sprite_time == "prolog":
                renpy.show('day_num', what=Text(dn, style=style.alt_days,xcenter=0.5215,ycenter=0.25))
                renpy.show('day_text', what=Text(alt_chapter_name, style=style.alt_chapters,xcenter=0.5215,ycenter=0.35))
            else:
                renpy.show('day_num', what=Text(dn, style=style.alt_days,xcenter=0.5215,ycenter=0.35))
                renpy.show('day_text', what=Text(alt_chapter_name, style=style.alt_chapters,xcenter=0.5215,ycenter=0.45))
        
            renpy.pause(3)
            renpy.scene()
            renpy.show('bg black')
            renpy.transition(blind_r)
            set_mode_adv()

    if persistent.altCardsDemo == None:
        persistent.altCardsDemo = False

    if persistent.altCardsFail == None:
        persistent.altCardsFail = False

    if persistent.altCardsWon1 == None:
        persistent.altCardsWon1 = False

    if persistent.altCardsWon2 == None:
        persistent.altCardsWon2 = False

    if persistent.altCardsWon3 == None:
        persistent.altCardsWon3 = False
        
    if persistent.altCardsWon4 == None:
        persistent.altCardsWon4 = False
    
    
    # Функция для дрожания огонька спички в котокомбах
    def random_zoom(trans, st, at):
        if st < 1.0: # 1 sec random zooming each 0.1 sec
            trans.zoom = 1.0 + renpy.random.random() * 0.5 
            return 0.1
        trans.zoom = 1.0
        return None        

init 52 python:
    def disable_all_chibi():
        global global_zones
        for name,data in global_zones.iteritems():
            data["chibi"] = None
        
init -1001 python:
    def disable_all_chibi():
        global global_zones
        for name,data in global_zones.iteritems():
            data["map_chibi"] = None
            
init -1000 python:
    if renpy.version(tuple=False) == "Ren'Py 6.16.3.502":
        default_7dl_path = 'scenario_alt/'
    elif (renpy.version(tuple=False) == "Ren'Py 6.18.3.761") or (persistent.nonsteam_7dl == True):
        default_7dl_path = 'mods/scenario_alt/'
    else:
        if renpy.mobile:
            default_7dl_path = 'scenario_alt/'
        else:
            default_7dl_path = '../441054187/scenario_alt/'
    config_session = False

init -999 python:
    def get_image_7dl(file):
        return default_7dl_path+"Pics/%s" % (file)
    def get_image_extra7dl(file):
        return default_7dl_path+"Pics/extra/%s" % (file)
        
init -998 python:
    def get_sfx_7dl(file):
        return default_7dl_path+"Sound/sfx/%s" % (file)
    def get_ambience_7dl(file):
        return default_7dl_path+"Sound/ambience/%s" % (file)
    def get_music_7dl(file):
        return default_7dl_path+"Sound/music/%s" % (file)
        
init -997 python:
    def get_sprite_7dl(file):
        return default_7dl_path+"Pics/sprites/%s" % (file)
    def get_sprite_ori(file):
        return get_image("sprites/%s") % (file)
    
    store.map_chibi = {
            "?" : get_image_7dl("gui/maps/map_icon_n00.png"),
            "me": get_image_7dl("gui/maps/map_icon_n01.png"),
            "mi": get_image_7dl("gui/maps/map_icon_n02.png"),
            "sh": get_image_7dl("gui/maps/map_icon_n03.png"),
            "el": get_image_7dl("gui/maps/map_icon_n04.png"),
            "mz": get_image_7dl("gui/maps/map_icon_n05.png"),
            "mt": get_image_7dl("gui/maps/map_icon_n06.png"),
            "uv": get_image_7dl("gui/maps/map_icon_n07.png"),
            "un": get_image_7dl("gui/maps/map_icon_n08.png"),
            "us": get_image_7dl("gui/maps/map_icon_n09.png"),
            "dv": get_image_7dl("gui/maps/map_icon_n10.png"),
            "sl": get_image_7dl("gui/maps/map_icon_n11.png"),
            "cs": get_image_7dl("gui/maps/map_icon_n12.png"),
        }
        
init python:
    
    import math

    class Shaker(object):
    
        anchors = {
            'top' : 0.0,
            'center' : 0.5,
            'bottom' : 1.0,
            'left' : 0.0,
            'right' : 1.0,
            }
    
        def __init__(self, start, child, dist):
            if start is None:
                start = child.get_placement()
            #
            self.start = [ self.anchors.get(i, i) for i in start ]  # central position
            self.dist = dist    # maximum distance, in pixels, from the starting point
            self.child = child
            
        def __call__(self, t, sizes):
            # Float to integer… turns floating point numbers to
            # integers.                
            def fti(x, r):
                if x is None:
                    x = 0
                if isinstance(x, float):
                    return int(x * r)
                else:
                    return x

            xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

            xpos = xpos - xanchor
            ypos = ypos - yanchor
            
            nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

            return (int(nx), int(ny), 0, 0)
    
    def _Shake(start, time, child=None, dist=100.0, **properties):

        move = Shaker(start, child, dist=dist)
    
        return renpy.display.layout.Motion(move,
                      time,
                      child,
                      add_sizes=True,
                      **properties)

    Shake = renpy.curry(_Shake)
        
# ================================================================================================
#                                            альтернативный старт БЛ - WIP
init 2 python:
    if persistent.autostart_7dl:
        rgsn = renpy.game.script.namemap
        rgsn["splashscreen_7dl"],rgsn["splashscreen"] = rgsn["splashscreen"],rgsn["splashscreen_7dl"]
        
        rgsn = renpy.game.script.namemap
        rgsn["alt_start_7dl"],rgsn["start"] = rgsn["start"],rgsn["alt_start_7dl"]

label splashscreen_7dl:

    python:
        
        if not persistent.set_volumes:
            
            persistent.lan_chosen = True
            persistent.licensed = True
            
            persistent.timeofday='prologue'
            
            persistent.choices = []
            
            persistent.show_achievements = False
            
            persistent.show_hentai_ach = False
            
            _preferences.language = None
            
            persistent.set_volumes = True
            persistent.achievement = True
            persistent.collector = True
            
            persistent.font_size = "small"
            persistent.hentai = False
            
            _preferences.volumes['music'] = .65
            _preferences.volumes['sfx'] = 1.0
            _preferences.volumes['voice'] = .75

    $ prolog_time()
    return

label alt_start_7dl:
    $ renpy.music.stop()
    $ skip_text_blocks = True
    $ renpy.block_rollback()
    $ init_map_zones()

    jump scenario__alt_sevendl
# ================================================================================================