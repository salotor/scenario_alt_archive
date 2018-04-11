#init -1 python: # done  
    #def check_time_7dl(time_7dl):
        #from time import localtime, strftime
        #t = strftime("%H:%M:%S", localtime())
        #hour, min, sec = t.split(":")
        #hour = int(hour)
        #if hour in (6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18):
            #time_7dl = "day"
            #return time_7dl
        #elif hour in (19, 20, 21, 22, 23, 0, 1, 2, 3, 4, 5):
            #time_7dl = "night"
            #return time_7dl
            
init 1: # done
    $ list_waifu_7dl = []
    $ persistent.waifu_7dl = 0
    $ time_7dl = ""
    image bg mi_bg_7dl = get_image_7dl("gui/menu_main/mi_bg.png")
    image bg sl_bg_7dl = get_image_7dl("gui/menu_main/sl_bg.png")
    image bg un_bg_day_7dl = get_image_7dl("gui/menu_main/un_bg_day.png")
    image bg un_bg_night_7dl = get_image_7dl("gui/menu_main/un_bg_night.png")
    image bg us_bg_7dl = get_image_7dl("gui/menu_main/us_bg.png")
    python:
        style.log_button = Style(style.button)
        style.log_button.child = None
        style.log_button.focus_mask = None
        style.log_button.background  = None
        style.log_button_text = Style(style.normal_day)
        style.log_button_text.selected_color = "#115bc0"
        style.log_button_text.hover_color = "#115bc0"
        style.log_button_text.selected_color = "#b6ff00"
        style.log_button_text.hover_color = "#b6ff00"
    
init 9001 python: # done
    def add_lp_widget_7dl():
        for i in persistent.filters:
            if i['id'] == "widget__7dl_widget": i['is_active'] = True
            
    def del_lp_widget_7dl():  
        for i in persistent.filters:
            if i['id'] == "widget__7dl_widget": i['is_active'] = False
     
    def add_music_widget_7dl():
        for i in persistent.filters:
            if i['id'] == "music_widget_7dl": i['is_active'] = True
        
    def del_music_widget_7dl():
        for i in persistent.filters:
            if i['id'] == "music_widget_7dl": i['is_active'] = False

transform left_menu_7dl(xal, yal): # done
    xalign -0.1
    alpha 0.0
    easein 1 xalign xal alpha 1.0

screen alt_wip1:
    modal True
    add get_image("gui/o_rly/base.png")
    text "РАЗДЕЛ «МУЗЫКА» НАХОДИТСЯ В РАЗРАБОТКЕ":
        text_align 0.5
        yalign 0.46
        xalign 0.5
        color "#64483c"
        size 30
    textbutton _("OK"):
        text_size 60
        style "log_button"
        yalign 0.65
        xalign 0.5
        action Hide("alt_wip1")

screen alt_wip2:
    modal True
    add get_image("gui/o_rly/base.png")
    text "РАЗДЕЛ «ГАЛЕРЕЯ» НАХОДИТСЯ В РАЗРАБОТКЕ":
        text_align 0.5
        yalign 0.46
        xalign 0.5
        color "#64483c"
        size 30
    textbutton _("OK"):
        text_size 60
        style "log_button"
        yalign 0.65
        xalign 0.5
        action Hide("alt_wip2")
    
screen settings_widget_lp_on_7dl(): # done
    add get_image_7dl("gui/menu_elem/settings/settings_wdglp_on.png")
    
screen settings_widget_lp_off_7dl(): # done
    add get_image_7dl("gui/menu_elem/settings/settings_wdglp_off.png")
    
screen settings_widget_music_on_7dl(): # done
    add get_image_7dl("gui/menu_elem/settings/settings_wdgmus_on.png")
    
screen settings_widget_music_off_7dl(): # done
    add get_image_7dl("gui/menu_elem/settings/settings_wdgmus_off.png")
    
screen settings_dlc_on_7dl(): # done
    add get_image_7dl("gui/menu_elem/settings/settings_dlc_on.png")

screen settings_dlc_off_7dl(): # done
    add get_image_7dl("gui/menu_elem/settings/settings_dlc_off.png")

screen settings_hentai_un_new_7dl(): # done
    add get_image_7dl("gui/menu_elem/settings/settings_hent_new.png")
 
screen settings_hentai_un_old_7dl(): # done
    add get_image_7dl("gui/menu_elem/settings/settings_hent_old.png")
 
screen settings_reboot_7dl():
    add get_image_7dl("gui/menu_elem/settings/settings_reboot.png")
 
screen menu_7dl(): # need changes on settings pics
    if persistent.waifu_7dl == 1:
        #if time_7dl == "day":
            #imagemap at left_menu_7dl(0.1, 0.7):
                #auto get_image_7dl("gui/menu_main/mi_menu_%s.png")
                #hotspot (170, 511, 300, 38):
                    #action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=3), Jump("start_7dl")]
                #hotspot (170, 563, 300, 36):
                    #action [Show("settings_7dl", transition=Dissolve(0.2))]
                #hotspot (162, 615, 307, 40):
                    #action [Show("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=3), Jump("scenario__sdl_achvlist_Author")]
                #hotspot (165, 665, 233, 43):
                    #action [Show("contacts_7dl", transition=Dissolve(0.2))]
                #hotspot (164, 718, 153, 41):
                    #action [Show("media_7dl", transition=Dissolve(0.2))]
                #hotspot (164, 772, 146, 38):
                    #action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), MainMenu(confirm=False)]   
        #elif time_7dl == "night":
        imagemap at left_menu_7dl(0.1, 0.7):
            auto get_image_7dl("gui/menu_main/un_night_menu_%s.png")
            hotspot (170, 511, 300, 38):
                action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=3), Jump("start_7dl")]
            hotspot (170, 563, 300, 36):
                action [Show("settings_7dl", transition=Dissolve(0.2))]
            hotspot (162, 615, 307, 40):
                action [Show("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=3), Jump("scenario__sdl_achvlist_Author")]
            hotspot (165, 665, 233, 43):
                action [Show("contacts_7dl", transition=Dissolve(0.2))]
            hotspot (164, 718, 153, 41):
                action [Show("media_7dl", transition=Dissolve(0.2))]
            hotspot (164, 772, 146, 38):
                action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), MainMenu(confirm=False)]   
    elif persistent.waifu_7dl == 2:
        imagemap at left_menu_7dl(0.1, 0.7):
            auto get_image_7dl("gui/menu_main/sl_menu_%s.png")
            hotspot (170, 511, 300, 38):
                action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=3), Jump("start_7dl")]
            hotspot (170, 563, 300, 36):
                action [Show("settings_7dl", transition=Dissolve(0.2))]
            hotspot (162, 615, 307, 40):
                action [Show("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=3), Jump("scenario__sdl_achvlist_Author")]
            hotspot (165, 665, 233, 43):
                action [Show("contacts_7dl", transition=Dissolve(0.2))]
            hotspot (164, 718, 153, 41):
                action [Show("media_7dl", transition=Dissolve(0.2))]
            hotspot (164, 772, 146, 38):
                action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), MainMenu(confirm=False)]
    #elif persistent.waifu_7dl == 3:
        #imagemap at left_menu_7dl(0.1, 0.7):
            #auto "mods/test1/img/menu_main/mi_menu_%s.png"
            #hotspot (170, 511, 300, 38):
                #action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=3), Jump("start_7dl")]
            #hotspot (170, 563, 300, 36):
                #action [Show("settings_7dl", transition=Dissolve(0.2))]
            #hotspot (162, 615, 307, 40):
                #action [Show("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=3), Jump("scenario__sdl_achvlist_Author")]
            #hotspot (165, 665, 233, 43):
                #action [Show("contacts_7dl", transition=Dissolve(0.2))]
            #hotspot (164, 718, 153, 41):
                #action [Show("media_7dl", transition=Dissolve(0.2))]
            #hotspot (164, 772, 146, 38):
                #action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), MainMenu(confirm=False)]
    elif persistent.waifu_7dl == 4:
        imagemap at left_menu_7dl(0.1, 0.7):
            auto get_image_7dl("gui/menu_main/mi_menu_%s.png")
            hotspot (170, 511, 300, 38):
                action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=3), Jump("start_7dl")]
            hotspot (170, 563, 300, 36):
                action [Show("settings_7dl", transition=Dissolve(0.2))]
            hotspot (162, 615, 307, 40):
                action [Show("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=3), Jump("scenario__sdl_achvlist_Author")]
            hotspot (165, 665, 233, 43):
                action [Show("contacts_7dl", transition=Dissolve(0.2))]
            hotspot (164, 718, 153, 41):
                action [Show("media_7dl", transition=Dissolve(0.2))]
            hotspot (164, 772, 146, 38):
                action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), MainMenu(confirm=False)]     
    elif persistent.waifu_7dl == 5:
        imagemap at left_menu_7dl(0.1, 0.7):
            auto get_image_7dl("gui/menu_main/us_menu_%s.png")
            hotspot (170, 511, 300, 38):
                action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=3), Jump("start_7dl")]
            hotspot (170, 563, 300, 36):
                action [Show("settings_7dl", transition=Dissolve(0.2))]
            hotspot (162, 615, 307, 40):
                action [Show("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=3), Jump("scenario__sdl_achvlist_Author")]
            hotspot (165, 665, 233, 43):
                action [Show("contacts_7dl", transition=Dissolve(0.2))]
            hotspot (164, 718, 153, 41):
                action [Show("media_7dl", transition=Dissolve(0.2))]
            hotspot (164, 772, 146, 38):
                action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), MainMenu(confirm=False)]
    #elif persistent.waifu_7dl == 6:
        #imagemap at left_menu_7dl(0.1, 0.7):
            #auto "mods/test1/img/menu_main/mi_menu_%s.png"
            #hotspot (170, 511, 300, 38):
                #action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=3), Jump("start_7dl")]
            #hotspot (170, 563, 300, 36):
                #action [Show("settings_7dl", transition=Dissolve(0.2))]
            #hotspot (162, 615, 307, 40):
                #action [Show("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=3), Jump("scenario__sdl_achvlist_Author")]
            #hotspot (165, 665, 233, 43):
                #action [Show("contacts_7dl", transition=Dissolve(0.2))]
            #hotspot (164, 718, 153, 41):
                #action [Show("media_7dl", transition=Dissolve(0.2))]
            #hotspot (164, 772, 146, 38):
                #action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), MainMenu(confirm=False)]
            
screen settings_7dl(): # done
    tag menu
    add get_image_7dl("gui/menu_elem/settings/settings_bg.png") xalign 0.9 yalign 0.7
    if not persistent.lp_widget_7dl:
        imagebutton xalign 0.82 yalign 0.315:
            auto get_image_7dl("gui/menu_elem/settings/settings_wdgmlp_off_%s.png")
            hovered Show("settings_widget_lp_on_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_widget_lp_off_7dl", transition=Dissolve(0.2)), Hide("settings_widget_lp_on_7dl", transition=Dissolve(0.2))]
            action SetField(persistent,'lp_widget_7dl',True)
    else:
        imagebutton xalign 0.82 yalign 0.315:
            auto get_image_7dl("gui/menu_elem/settings/settings_wdgmlp_on_%s.png")
            hovered Show("settings_widget_lp_off_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_widget_lp_on_7dl", transition=Dissolve(0.2)), Hide("settings_widget_lp_off_7dl", transition=Dissolve(0.2))]
            action SetField(persistent,'lp_widget_7dl',False)
    if not persistent.music_widget_7dl:
        imagebutton xalign 0.82 yalign 0.365:
            auto get_image_7dl("gui/menu_elem/settings/settings_wdgmus_off_%s.png")
            hovered Show("settings_widget_music_on_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_widget_music_off_7dl", transition=Dissolve(0.2)), Hide("settings_widget_music_on_7dl", transition=Dissolve(0.2))]
            action SetField(persistent,'music_widget_7dl',True)
    else:
        imagebutton xalign 0.82 yalign 0.365:
            auto get_image_7dl("gui/menu_elem/settings/settings_wdgmus_on_%s.png")
            hovered Show("settings_widget_music_off_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_widget_music_on_7dl", transition=Dissolve(0.2)), Hide("settings_widget_music_off_7dl", transition=Dissolve(0.2))]
            action SetField(persistent,'music_widget_7dl',False)
    if not persistent.uv_dlc_on_7dl:
        imagebutton xalign 0.82 yalign 0.41:
            auto get_image_7dl("gui/menu_elem/settings/settings_dlc_off_%s.png")
            hovered Show("settings_dlc_on_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_dlc_off_7dl", transition=Dissolve(0.2)), Hide("settings_dlc_on_7dl", transition=Dissolve(0.2))]
            action SetField(persistent,'uv_dlc_on_7dl',True)
    else:
        imagebutton xalign 0.82 yalign 0.41:
            auto get_image_7dl("gui/menu_elem/settings/settings_dlc_on_%s.png")
            hovered Show("settings_dlc_off_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_dlc_on_7dl", transition=Dissolve(0.2)), Hide("settings_dlc_off_7dl", transition=Dissolve(0.2))]
            action SetField(persistent,'uv_dlc_on_7dl',False)
    if not persistent.hentai_un_old_7dl:
        imagebutton xalign 0.82 yalign 0.46:
            auto get_image_7dl("gui/menu_elem/settings/settings_hent_off_%s.png")
            hovered Show("settings_hentai_un_old_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_hentai_un_old_7dl", transition=Dissolve(0.2)), Hide("settings_hentai_un_new_7dl", transition=Dissolve(0.2))]
            action SetField(persistent,'hentai_un_old_7dl',True)
    else:
        imagebutton xalign 0.82 yalign 0.46:
            auto get_image_7dl("gui/menu_elem/settings/settings_hent_on_%s.png")
            hovered Show("settings_hentai_un_new_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_hentai_un_old_7dl", transition=Dissolve(0.2)), Hide("settings_hentai_un_new_7dl", transition=Dissolve(0.2))]
            action SetField(persistent,'hentai_un_old_7dl',False)
    if renpy.get_screen("settings_widget_lp_on_7dl") or renpy.get_screen("settings_widget_lp_off_7dl"):
        python:
            pass
    elif renpy.get_screen("settings_widget_music_on_7dl") or renpy.get_screen("settings_widget_music_off_7dl"):
        python:
            pass
    elif renpy.get_screen("settings_dlc_on_7dl") or renpy.get_screen("settings_dlc_off_7dl"):
        python:
            pass
    elif renpy.get_screen("settings_hentai_un_old_7dl") or renpy.get_screen("settings_hentai_un_new_7dl"):
        python:
            pass
    else:
        if persistent.lp_widget_7dl or persistent.music_widget_7dl:
            imagebutton xalign 0.81 yalign 0.8:
                auto get_image_7dl("gui/menu_elem/settings/settings_reboot_%s.png")
                hovered Show("settings_reboot_7dl", transition=Dissolve(0.2))
                unhovered Hide("settings_reboot_7dl", transition=Dissolve(0.2))
                action Jump("widgets_on_off_7dl")
        elif persistent.lp_widget_7dl and persistent.music_widget_7dl and not persistent.lock_apply_button_7dl:
            imagebutton xalign 0.81 yalign 0.8:
                auto get_image_7dl("gui/menu_elem/settings/settings_reboot_%s.png")
                hovered Show("settings_reboot_7dl", transition=Dissolve(0.2))
                unhovered Hide("settings_reboot_7dl", transition=Dissolve(0.2))
                action Jump("widgets_on_off_7dl")
        elif persistent.lp_widget_7dl and persistent.music_widget_7dl and persistent.lock_apply_button_7dl:
            imagebutton xalign 0.81 yalign 0.8:
                auto get_image_7dl("gui/menu_elem/settings/settings_reboot_%s.png")
                hovered Show("settings_reboot_7dl", transition=Dissolve(0.2))
                unhovered Hide("settings_reboot_7dl", transition=Dissolve(0.2))
                action NullAction()
        elif not persistent.lp_widget_7dl or not persistent.music_widget_7dl:
            imagebutton xalign 0.81 yalign 0.8:
                auto get_image_7dl("gui/menu_elem/settings/settings_reboot_%s.png")
                hovered Show("settings_reboot_7dl", transition=Dissolve(0.2))
                unhovered Hide("settings_reboot_7dl", transition=Dissolve(0.2))
                action Jump("widgets_on_off_7dl")
        elif not persistent.lp_widget_7dl and not persistent.music_widget_7dl:
            imagebutton xalign 0.81 yalign 0.8:
                auto get_image_7dl("gui/menu_elem/settings/settings_reboot_%s.png")
                hovered Show("settings_reboot_7dl", transition=Dissolve(0.2))
                unhovered Hide("settings_reboot_7dl", transition=Dissolve(0.2))
                action Jump("widgets_on_off_7dl")
                
screen contacts_7dl(): # done
    tag menu
    imagemap xalign 0.9 yalign 0.7:
        auto get_image_7dl("gui/menu_elem/contacts/contacts_%s.png")
        hotspot(1265, 330, 329, 59):
            action OpenURL("www.7dneyleta.ru") 
        hotspot(1265, 389, 329, 59):
            action OpenURL("https://vk.com/bl_7dl") 
        hotspot(1265, 449, 329, 59):
            action OpenURL("https://steamcommunity.com/sharedfiles/filedetails/?id=441054187") 
        hotspot(1265, 508, 329, 59):
            action OpenURL("https://vk.com/page-128046483_52530462") 
            
screen media_7dl(): # done, TODO gallery and music room
    tag menu
    imagemap:   
        auto get_image_7dl("gui/menu_elem/media/media_%s.png")
        hotspot(1333, 224, 540, 160):
            clicked [Show("alt_wip1", transition=Dissolve(0.2))]
        hotspot(1218, 394, 700, 700):
            clicked [Show("alt_wip2", transition=Dissolve(0.2))]
        
label choose_waifu_7dl: # done
    stop music
    stop sound
    stop sound_loop
    #if len(list_waifu_7dl) == 6:
    if len(list_waifu_7dl) == 4:
        $ list_waifu_7dl = []
    if persistent.waifu_7dl == 0:
        $ persistent.waifu_7dl = renpy.random.choice([1, 2, 4, 5])
        jump start_menu_7dl
    elif persistent.waifu_7dl == 1:
        $ persistent.waifu_7dl = renpy.random.choice([2, 4, 5])
        jump start_menu_7dl
    elif persistent.waifu_7dl == 2:
        $ persistent.waifu_7dl = renpy.random.choice([1, 4, 5])
        jump start_menu_7dl
    #elif persistent.waifu_7dl == 3:
        #$ persistent.waifu_7dl = renpy.random.choice([1, 2, 4, 5, 6])
        #jump start_menu_7dl
    elif persistent.waifu_7dl == 4:
        $ persistent.waifu_7dl = renpy.random.choice([1, 2, 5])
        jump start_menu_7dl
    elif persistent.waifu_7dl == 5:
        $ persistent.waifu_7dl = renpy.random.choice([1, 2, 4])
        jump start_menu_7dl
    #elif persistent.waifu_7dl == 6:
        #$ persistent.waifu_7dl = renpy.random.choice([1, 2, 3, 4, 5])
        #jump start_menu_7dl
        
label widgets_on_off_7dl:
    if persistent.lp_widget_7dl or persistent.music_widget_7dl:
        python:
            if persistent.lp_widget_7dl:
                add_lp_widget_7dl()
            if persistent.music_widget_7dl:
                add_music_widget_7dl()
            renpy.utter_restart()
    elif persistent.lp_widget_7dl and persistent.music_widget_7dl:
        python:
            add_lp_widget_7dl()
            add_music_widget_7dl()
            persistent.lock_apply_button_7dl = True
            renpy.utter_restart()
    elif not persistent.lp_widget_7dl or not persistent.music_widget_7dl:
        python:
            if not persistent.lp_widget_7dl:
                del_lp_widget_7dl()
            if not persistent.music_widget_7dl:
                del_music_widget_7dl()
            persistent.lock_apply_button_7dl = False
            renpy.utter_restart()
    elif not persistent.lp_widget_7dl and not persistent.music_widget_7dl:
        python:
            del_lp_widget_7dl()
            del_music_widget_7dl()
            persistent.lock_apply_button_7dl = False
            renpy.utter_restart()

label start_7dl:
    call alt_day0_vars
    call alt_day0_prologue
    jump choose_waifu_7dl
 
label start_menu_7dl: # need dopil on girls walls
    if persistent.waifu_7dl == 1 and 'un' not in list_waifu_7dl:
        play music music_7dl["take_my_hand"] fadein 3
        #$ time_7dl = check_time_7dl(time_7dl)
        #if time_7dl == "day":
            #$ list_waifu_7dl.append('un')
            #scene bg un_bg_day_7dl with fade
            #call screen menu_7dl
        #elif time_7dl == "night":
        $ list_waifu_7dl.append('un')
        scene bg un_bg_night_7dl with fade
        call screen menu_7dl
    if persistent.waifu_7dl == 2 and 'sl' not in list_waifu_7dl:
        $ list_waifu_7dl.append('sl')
        scene bg sl_bg_7dl with fade
        play music music_7dl["slavyas_fantazm"] fadein 3
        call screen menu_7dl
    #if persistent.waifu_7dl == 3 and 'dv' not in list_waifu_7dl:
        #$ list_waifu_7dl.append('dv')
        #scene bg black 
        #play music music_7dl["uncertainity"] fadein 3
        #call screen menu_7dl
    if persistent.waifu_7dl == 4 and 'mi' not in list_waifu_7dl:
        $ list_waifu_7dl.append('mi')
        scene bg mi_bg_7dl with fade
        play music music_7dl["tellyourworld"] fadein 3
        call screen menu_7dl
    if persistent.waifu_7dl == 5 and 'us' not in list_waifu_7dl:
        $ list_waifu_7dl.append('us')
        scene bg us_bg_7dl with fade
        play music music_7dl["thousand_of_pixies"] fadein 3
        call screen menu_7dl
    #if persistent.waifu_7dl == 6 and 'mt' not in list_waifu_7dl:
        #$ list_waifu_7dl.append('mt')
        #scene bg black 
        #play music music_7dl["wheres_wonderland"] fadein 3
        #call screen menu_7dl
    else:
        jump choose_waifu_7dl