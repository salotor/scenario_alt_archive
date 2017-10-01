init:
    $ filters["widget__7dl_widget"] = u"Прогресс и информация по моду 7ДЛ"

python early:
    def widget__7dl_widget():
        def editoverlay():
            if plthr == u"none":
                ui.button(clicked=None, xpos=0.0, xanchor=0.0, ypos=2, xpadding=6, xminimum=600)
                ui.text("%s" % ("Несовместимые данные"), style="button_text", size=13)
            else:
                ui.button(clicked=None, xpos=0.16, xanchor=0.0, ypos=2, xpadding=6, xminimum=200)
                ui.text("%s" % (save_name), style="button_text", size=13)
                
                ui.button(clicked=None, xpos=0.07, xanchor=0.0, ypos=2, xpadding=6, xminimum=120)
                if alt_sp > 0:
                    if karma >= 75:
                        ui.text("%s: %d | %s: %d" % ("Карма", karma, "Воля", alt_sp), style="button_text", size=14, color="#7bacff")
                    else:
                        ui.text("%s: %d | %s: %d" % ("Карма", karma, "Воля", alt_sp), style="button_text", size=13)
                elif alt_spt > 0 or alt_hpt > 0:
                    if alt_spt >= 7:
                        ui.text("%s: %d | %s: %d" % ("Princess", alt_spt, "Human", alt_hpt), style="button_text", size=14, color="#ff7bac")
                    elif alt_hpt >= 7:
                        ui.text("%s: %d | %s: %d" % ("Human", alt_hpt, "Princess", alt_spt), style="button_text", size=14, color="#ac7bff")
                    else:
                        ui.text("%s: %d | %s: %d" % ("Human", alt_hpt, "Princess", alt_spt), style="button_text", size=13)
                else:
                    if karma >= 75:
                        ui.text("%s: %d" % ("Карма", karma), style="button_text", size=14, color="#7bacff")
                    else:
                        ui.text("%s: %d" % ("Карма", karma), style="button_text", size=13)
                        
                ui.button(clicked=None, xpos=0.0, xanchor=0.0, ypos=2, xpadding=6, xminimum=120)
                ui.text("%s: %s" % ("Роль", plthr), style="button_text", size=13)
                
            if (us_pt > 0) or (mt_pt > 0) or (d3_pt > 0):
                ui.button(clicked=None, xpos=1.0, xanchor=1.0, ypos=2, xpadding=6, xminimum=120)
                if us_pt < 8:
                    ui.text("%s: %d" % ("Ульяна", us_pt), style="button_text", size=13, color="#f65252")
                else:
                    ui.text("%s: %d" % ("Ульяна", us_pt), style="button_text", size=14, color="#ff3200")
                ui.button(clicked=None, xpos=0.93, xanchor=1.0, ypos=2, xpadding=6, xminimum=120)
                if us_pt < 8:
                    ui.text("%s: %d" % ("Ольга", mt_pt), style="button_text", size=13, color="#f65252")
                else:
                    ui.text("%s: %d" % ("Ольга", mt_pt), style="button_text", size=14, color="#00ea32")
                ui.button(clicked=None, xpos=0.86, xanchor=1.0, ypos=2, xpadding=6, xminimum=140)
                if us_pt < 8:
                    ui.text("%s: %d" % ("Одиночка", d3_pt), style="button_text", size=13, color="#f65252")
                else:
                    ui.text("%s: %d" % ("Одиночка", d3_pt), style="button_text", size=14, color="#e1dd7d")
            else:
                ui.button(clicked=None, xpos=1.0, xanchor=1.0, ypos=2, xpadding=6, xminimum=120)
                ui.text("%s: %d" % ("Ульяна", lp_us), style="button_text", size=13)
                
                ui.button(clicked=None, xpos=0.93, xanchor=1.0, ypos=2, xpadding=6, xminimum=120)
                if lp_mi >= 13:
                    if lp_mi < 20:
                        ui.text("%s: %d" % ("Мику", lp_mi), style="button_text", size=14, color="#00bbbb")
                    else:
                        ui.text("%s: %d" % ("Мику", lp_mi), style="button_text", size=15, color="#00ffff")
                else:
                    ui.text("%s: %d" % ("Мику", lp_mi), style="button_text", size=13)
                    
                ui.button(clicked=None, xpos=0.86, xanchor=1.0, ypos=2, xpadding=6, xminimum=120)
                if lp_dv >=11:
                    if lp_dv < 18:
                        ui.text("%s: %d" % ("Алиса", lp_dv), style="button_text", size=14, color="#bb8800")
                    else:
                        ui.text("%s: %d" % ("Алиса", lp_dv), style="button_text", size=15, color="#ffaa00")
                else:
                    ui.text("%s: %d" % ("Алиса", lp_dv), style="button_text", size=13)
                
                ui.button(clicked=None, xpos=0.79, xanchor=1.0, ypos=2, xpadding=6, xminimum=120)
                if lp_sl >= 14:
                    if lp_sl < 20:
                        ui.text("%s: %d" % ("Славя", lp_sl), style="button_text", size=14, color="#bbb200")
                    else:
                        ui.text("%s: %d" % ("Славя", lp_sl), style="button_text", size=15, color="#ffaa00")
                else:
                    ui.text("%s: %d" % ("Славя", lp_sl), style="button_text", size=13)
                
                ui.button(clicked=None, xpos=0.72, xanchor=1.0, ypos=2, xpadding=6, xminimum=120)
                if lp_un >= 12:
                    if lp_un < 20:
                        ui.text("%s: %d" % ("Лена", lp_un), style="button_text", size=14, color="#9f72be")
                    else:
                        ui.text("%s: %d" % ("Лена", lp_un), style="button_text", size=15, color="#d599ff")
                else:
                    ui.text("%s: %d" % ("Лена", lp_un), style="button_text", size=13)
                
        config.overlay_functions.append(editoverlay)

