python early:
    if renpy.version(tuple=False) == "Ren'Py 6.16.3.502":
        mods = {}
        filters = {}
        mod_tags = {}

init 9000 python:
    if renpy.version(tuple=False) == "Ren'Py 6.16.3.502":
        if  not persistent.filters:
            persistent.filters = []
        for i in sorted(filters.keys()):
            if  not i in [item["id"] for item in persistent.filters]:
                persistent.filters += [{"id":i,"is_active":False}]
        for item in persistent.filters:
            if  item["id"] in filters and item["id"] in renpy.store.__dict__:
                if  item["is_active"]:
                    renpy.store.__dict__[item["id"]]()
            else:
                persistent.filters.remove(item)

init 9000 python:
    if renpy.version(tuple=False) == "Ren'Py 6.16.3.502":
        for m in mods:
            if  not m in mod_tags:
                mod_tags[m] = ["special:tag_me"]
    # uncomment to auto-add authors as tags
    #        mod_tags[m] += ["author:"+m.split("__")[0] if m.find("__")!=-1 else "author:unknown"]
        for m in mod_tags:
            if  not m in mods:
                del mod_tags[m]
        tag_mods = {t:[m for m in mods if t in mod_tags[m]] for t in set(sum(mod_tags.values(),[]))}

init python:
    if renpy.version(tuple=False) == "Ren'Py 6.16.3.502":
        rgsn = renpy.game.script.namemap
        rgsn["_start_original_7dl"],rgsn["start"] = rgsn["start"],rgsn["_start_original_7dl"]

label _start_original_7dl:
    scene backdrop_back
    show backdrop_new
    python:
        ui.button(background=None, clicked=ui.returns("original"), xpos=870, xanchor=0.5, ypos=300)
        ui.text(u"Начать игру", style="button_text", size=40, hover_color="0f0")
        if len(mods) > 0:
            ui.button(background=None, clicked=ui.returns("mods"), xpos=870, xanchor=0.5, ypos=500)
            ui.text(u"Моды и пользовательские сценарии", style="button_text", size=30, hover_color="0f0")
        if len(filters) > 0:
            ui.button(background=None, clicked=ui.returns("filters"), xpos=870, xanchor=0.5, ypos=550)
            ui.text(u"Управление фильтрами", style="button_text", size=30, hover_color="0f0")
        res = ui.interact()
    if  res == "original":
        jump _start_original_7dl
    elif res == "filters":
        jump filters_selection_7dl
    else:
        jump prepare_env_7dl

label prepare_env_7dl:
    $ renpy.music.stop()
    $ set_mode_adv()
    $ init_map_zones()
    $ make_names_known()
    $ skip_text_blocks = False
    $ font_size="small"
    $ day_time()
    scene bg black
    jump mods_selection_7dl

label mods_selection_7dl:
    $ mods_filter = {}
    $ mods_filter["+"] = []
    $ mods_filter["-"] = []
    jump mods_selection_7dl_loop

init python:
    if renpy.version(tuple=False) == "Ren'Py 6.16.3.502":
        def filter_mods_list(lst):
            res = []
            for i in lst:
                ok = True
                for p in mods_filter["+"]:
                    if  i not in tag_mods[p]:
                        ok = False
                for p in mods_filter["-"]:
                    if  i in tag_mods[p]:
                        ok = False
                if ok:
                    res += [i]
            return res

        def img_bar(name, color, x=None, y=None):
            rv = theme.OneOrTwoColor("_roundrect/rr" + name + ".png", color)
            return rv if x is None else Frame(rv, x, y, tile=True)
        style.futaba_button = Style(style.button)
        style.futaba_button.color = "#8E0000"
        style.futaba_button.background = Solid("#edaa88")
        style.futaba_button.hover_background = Solid("#ffd591")
        style.futaba_button.insensitive_background = Solid("#b5b5b5")
        style.futaba_vscrollbar = Style(style.vscrollbar)
        style.futaba_vscrollbar.bottom_bar       = img_bar("vscrollbar",       "#EEAA88", 0, 12)
        style.futaba_vscrollbar.top_bar          = img_bar("vscrollbar",       "#EEAA88", 0, 12)
        style.futaba_vscrollbar.thumb            = img_bar("vscrollbar_thumb", "#EEAA88")
        style.futaba_vscrollbar.hover_bottom_bar = img_bar("vscrollbar",       "#FFD591", 0, 12)
        style.futaba_vscrollbar.hover_top_bar    = img_bar("vscrollbar",       "#FFD591", 0, 12)
        style.futaba_vscrollbar.hover_thumb      = img_bar("vscrollbar_thumb", "#FFD591")

label mods_selection_7dl_loop:
    python:
        ui.window(yalign=0,xpos=700,xanchor=1.0,xfill=True,yfill=True,background="#F0E0D6")
        ui.null()
        ui.window(yalign=0,xpos=700,xanchor=0.0,xfill=True,yfill=True,background="#FFFFEE")
        ui.null()

        what_filters = [(k,len(filter_mods_list(v))) for k,v in tag_mods.iteritems() if k not in mods_filter["+"] and len(filter_mods_list(v))]
        what_mods = [(k, "{color=#117743}[%s]{/color} %s" %( "{{?}" if k.find("__") == -1 else k.split("__")[0], mods[k] )) for k in filter_mods_list(mods.keys())]

        what_filter_groups = sorted(list(set([i.split(":")[0] for i,n in what_filters if i.find(":")!=-1])))

        vp_tags = ui.viewport(mousewheel=True,xpos=35,ypos=0,xmaximum=700)
        ui.vbox(xmaximum=600)
        ui.text("Применено фильтров: %d"%len(sum(mods_filter.values(),[])),color="#8E0000")
        for t in mods_filter:
            for name in sorted(mods_filter[t]):
                ui.hbox(xpos=35)
                ui.button(clicked=ui.returns(("X",t,name)),style="futaba_button")
                ui.text("X",style="futaba_button")
                ui.button(xfill=True,right_margin=100-35,style="futaba_button")
                ui.text("%s %s"%(t,name),style="futaba_button")
                ui.close()
        ui.text("Найдено плагинов: %d"%len(what_mods),color="#8E0000")
        for g in what_filter_groups:
            ui.text(g+":",color="#8E0000",xpos=35)
            for name,n in sorted(what_filters):
                if  name.startswith(g+":"):
                    ui.hbox(xpos=70)
                    ui.button(clicked=ui.returns(("-",name)),style="futaba_button")
                    ui.text("-",style="futaba_button")
                    ui.button(clicked=ui.returns(("+",name)),style="futaba_button")
                    ui.text("+",style="futaba_button")
                    ui.button(xfill=True,right_margin=100,style="futaba_button")
                    ui.text("%s [%d]"%(name.split(":")[-1],n),style="futaba_button")
                    ui.close()
        ui.close()
        if  len(what_filters)+len(what_filter_groups) > 36:
            ui.bar(adjustment=vp_tags.yadjustment, xpos=20, style='futaba_vscrollbar')

        vp_mods = ui.viewport(mousewheel=True, xpos=820,ypos=0 if len(what_mods)>37 else (3+540*(37-len(what_mods))/37),xmaximum=1000)
        ui.vbox(xmaximum=1200)
        for lbl,name in sorted(what_mods,key=lambda (i,j):(j,i)):
            ui.button(xfill=True,clicked=ui.jumps(lbl),style="futaba_button")
            ui.text("%s"%(name),style="futaba_button")
        ui.close()
        if  len(what_mods) > 37:
            ui.bar(adjustment=vp_mods.yadjustment, xpos=800, style='futaba_vscrollbar')

        res = ui.interact()
        if  isinstance(res,tuple) and res[0] in ["+","-"]:
            mods_filter[res[0]] += [res[1]]
        if  isinstance(res,tuple) and res[0] in ["X"]:
            mods_filter[res[1]].remove(res[2])
    jump mods_selection_7dl_loop

label filters_selection_7dl:
    scene black
    python:
        def ui_button(text,clicked):
            ui.button(clicked=ui.returns(clicked) if clicked is not None else None, xpos=0, xanchor=0.0, ypos=0, xpadding=6, xminimum=30)
            ui.text(text, style="button_text", size=20)
            
        ui.vbox()
        for i,(item) in enumerate(persistent.filters):
            ui.hbox()
            ui_button("↑",("move_up",i) if i>0 else None)
            ui_button("[x]" if item["is_active"] else "[ ]", ("toggle",i))
            ui_button("↓",("move_down",i) if i<len(filters.keys())-1 else None)
            ui_button("[%s] %s"%(item["id"].split("__")[0],filters[item["id"]]),None)
            ui.close()
        ui_button("Save & restart","done")
        ui_button("Save & apply on next start","exit")
        ui.close()
        result = ui.interact()
    if  isinstance(result,tuple) and result[0] == "toggle":
        $ persistent.filters[result[1]]["is_active"] = not persistent.filters[result[1]]["is_active"]
    if  isinstance(result,tuple) and result[0] == "move_up":
        $ persistent.filters[result[1]-1], persistent.filters[result[1]] = persistent.filters[result[1]], persistent.filters[result[1]-1]
    if  isinstance(result,tuple) and result[0] == "move_down":
        $ persistent.filters[result[1]+1], persistent.filters[result[1]] = persistent.filters[result[1]], persistent.filters[result[1]+1]
    if  result == "done":
        $ renpy.utter_restart()
    if  result == "exit":
        return
    jump filters_selection_7dl
