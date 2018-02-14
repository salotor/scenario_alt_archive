init:
    $ filters["muzlo"] = u"Музыка в 7ДЛ"

python early:
    def muzlo():
        def check_muzlo(value):   
            for k, v in music_list.items():
                if v == value:
                    return k
        def check_muzlo_7dl(value):
            for k, v in music_list_7dl.items():
                if v == value:
                    return k
        def get_mus_7dl(ch):
            global m
            m = renpy.music.get_playing(channel=ch)
        def editoverlay():
            if plthr == u"none" or plthr == u"Выбор":
                return
            else:
                get_mus_7dl('music')
                ui.button(clicked=None, xpos=0.40, xanchor=0.0, ypos=2, xpadding=6, xminimum=200)
                if m in music_list.values():
                    ui.text(check_muzlo(m), style="button_text", size=13)
                elif m in music_list_7dl.values():
                    ui.text(check_muzlo_7dl(m), style="button_text", size=13)
                elif m not in music_list_7dl.values():
                    if (m == music_list_7dl[u"С. Ейбог feat. Liru - Everlasting Summer"][0] or 
                        m == music_list_7dl[u"С. Ейбог feat. Liru - Everlasting Summer"][1] or 
                            m == music_list_7dl[u"С. Ейбог feat. Liru - Everlasting Summer"][2]):
                                ui.text("%s" % "С. Ейбог feat. Liru - Everlasting Summer", style="button_text", size=13)
                    elif (m == music_list_7dl["KPM Music - Bass Renaissaince"][0] or 
                        m == music_list_7dl["KPM Music - Bass Renaissaince"][1]):
                            ui.text("%s" % "KPM Music - Bass Renaissaince", style="button_text", size=13)
                    elif (m == music_list_7dl["Scorpions - Still Loving you"][0] or 
                        m == music_list_7dl["Scorpions - Still Loving you"][1]):
                            ui.text("%s" % "Scorpions - Still Loving you", style="button_text", size=13)
                elif m == None:
                    get_mus_7dl('ambience')
                    if a == "scenario_alt/Sound/ambience/ambience_safe.ogg":
                        ui.text("%s" % "Mikko Tarmia - Back Hall (Amnesia OST)", style="button_text", size=13)
                    else: 
                        ui.text("%s" % "Нет музыки", style="button_text", size=13)
                else:
                    ui.text("%s" % "Неизвестный трек", style="button_text", size=13)
        config.overlay_functions.append(editoverlay)

