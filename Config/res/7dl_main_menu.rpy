init 1 python:
    if (renpy.version(tuple=False) == "Ren'Py 6.16.3.502") or (renpy.version(tuple=False) == "Ren'Py 6.18.3.761"):
        header_font = "fonts/corbel.ttf"
        style.settings_link = Style(style.base_font)
        style.settings_link.font  = header_font
        style.settings_link.size = 60
        style.settings_link.kerning = 3
        style.settings_link.color = "#909ca3"
        style.settings_link.hover_color = "#ffffff"
        style.settings_link.selected_color = "#909ca3"
        style.settings_link.selected_idle_color = "#909ca3"
        style.settings_link.selected_hover_color = "#ffffff"
        style.settings_link.insensitive_color = "#909ca3"
        
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
            
init 1:
    $ list_waifu_7dl = []
    $ persistent.waifu_7dl = 0
    $ time_7dl = ""
    image bg un_bg_7dl = get_image_7dl("gui/menu_main/un_bg.png")
    image bg sl_bg_7dl = get_image_7dl("gui/menu_main/sl_bg.png")
    #image bg dv_bg_7dl = get_image_7dl("gui/menu_main/dv_bg.png")
    image bg mi_bg_7dl = get_image_7dl("gui/menu_main/mi_bg.png")
    image bg us_bg_7dl = get_image_7dl("gui/menu_main/us_bg.png")
    #image bg mt_bg_7dl = get_image_7dl("gui/menu_main/mt_bg.png")
    
init 9001 python:
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
            
    def chk_lp_widget_7dl():
        for i in persistent.filters:
            if i['id'] == "widget__7dl_widget":
                if i['is_active']:
                    persistent.lp_widget_7dl = True
                else:
                    persistent.lp_widget_7dl = False
                    
    def chk_music_widget_7dl():
        for i in persistent.filters:
            if i['id'] == "music_widget_7dl":
                if i['is_active']:
                    persistent.music_widget_7dl = True
                else:
                    persistent.music_widget_7dl = False
            
transform left_menu_7dl(xal, yal):
    xalign -0.1
    alpha 0.0
    easein 1 xalign xal alpha 1.0

screen alt_wip:
    modal True
    add get_image("gui/o_rly/base.png")
    text "РАЗДЕЛ НАХОДИТСЯ В РАЗРАБОТКЕ":
        text_align 0.5
        yalign 0.46
        xalign 0.5
        color "#64483c"
        font header_font
        size 40
    textbutton _("OK"):
        text_size 60
        style "log_button"
        text_style "settings_link"
        yalign 0.6
        xalign 0.5
        action Hide("alt_wip")

screen help_7dl:
    modal True
    add get_image("gui/o_rly/base.png")
    text "Уважаемый читатель,":
        text_align 0.5
        yalign 0.44
        xalign 0.5
        color "#64483c"
        font header_font
        size 40
    text "проекту требуется ваша помощь!":
        text_align 0.5
        yalign 0.49
        xalign 0.5
        color "#64483c"
        font header_font
        size 40
    textbutton _("Подробнее"):
        text_size 40
        style "log_button"
        text_style "settings_link"
        yalign 0.6
        xalign 0.23
        action [Hide("help_7dl", transition=Dissolve(0.2)), OpenURL("https://vk.com/wall-128046483_29533"), Stop('music', fadeout=2), Jump("random_bg_7dl")]
    textbutton _("Закрыть"):
        text_size 40
        style "log_button"
        text_style "settings_link"
        yalign 0.6
        xalign 0.5
        action [Hide("help_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=2), Jump("random_bg_7dl")]
    textbutton _("Больше не показывать"):
        text_size 40
        style "log_button"
        text_style "settings_link"
        yalign 0.6
        xalign 0.83
        action [Hide("help_7dl", transition=Dissolve(0.2)), SetField(persistent,'dont_disturb', True), Stop('music', fadeout=2), Jump("random_bg_7dl")]
        
screen settings_widget_lp_on_7dl():
    add get_image_7dl("gui/menu_elem/settings/settings_wdglp_descr_on.png")
    
screen settings_widget_lp_off_7dl():
    add get_image_7dl("gui/menu_elem/settings/settings_wdglp_descr_off.png")
    
screen settings_widget_music_on_7dl():
    add get_image_7dl("gui/menu_elem/settings/settings_wdgmus_descr_on.png")
    
screen settings_widget_music_off_7dl():
    add get_image_7dl("gui/menu_elem/settings/settings_wdgmus_descr_off.png")
    
screen settings_dlc_on_7dl():
    add get_image_7dl("gui/menu_elem/settings/settings_dlc_descr_on.png")

screen settings_dlc_off_7dl():
    add get_image_7dl("gui/menu_elem/settings/settings_dlc_descr_off.png")

screen settings_hentai_un_new_7dl():
    add get_image_7dl("gui/menu_elem/settings/settings_hent_descr_new.png")
 
screen settings_hentai_un_old_7dl():
    add get_image_7dl("gui/menu_elem/settings/settings_hent_descr_old.png")

screen settings_reboot_7dl():
    add get_image_7dl("gui/menu_elem/settings/settings_reboot_descr.png")

screen settings_chapter_on_7dl():
    add get_image_7dl("gui/menu_elem/settings/settings_chapter_descr_on.png")

screen settings_chapter_off_7dl():
    add get_image_7dl("gui/menu_elem/settings/settings_chapter_descr_off.png")

screen menu_7dl():
    if persistent.waifu_7dl == 1:
        imagemap at left_menu_7dl(0.1, 0.7):
            auto get_image_7dl("gui/menu_main/un_menu_%s.png")
            hotspot (170, 511, 300, 38):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=2), Jump("start_7dl")]
            hotspot (170, 563, 300, 36):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Show("settings_7dl", transition=Dissolve(0.2))]
            hotspot (162, 615, 307, 40):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Show("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=2), Jump("scenario__sdl_achvlist_Author")]
            hotspot (165, 665, 233, 43):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Show("contacts_7dl", transition=Dissolve(0.2))]
            hotspot (164, 718, 153, 41):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Show("media_7dl", transition=Dissolve(0.2))]
            hotspot (164, 772, 146, 38):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), MainMenu(confirm=False)]   
    elif persistent.waifu_7dl == 2:
        imagemap at left_menu_7dl(0.1, 0.7):
            auto get_image_7dl("gui/menu_main/sl_menu_%s.png")
            hotspot (170, 511, 300, 38):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=2), Jump("start_7dl")]
            hotspot (170, 563, 300, 36):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Show("settings_7dl", transition=Dissolve(0.2))]
            hotspot (162, 615, 307, 40):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Show("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=2), Jump("scenario__sdl_achvlist_Author")]
            hotspot (165, 665, 233, 43):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Show("contacts_7dl", transition=Dissolve(0.2))]
            hotspot (164, 718, 153, 41):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Show("media_7dl", transition=Dissolve(0.2))]
            hotspot (164, 772, 146, 38):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), MainMenu(confirm=False)]
    # elif persistent.waifu_7dl == 3:
        # imagemap at left_menu_7dl(0.1, 0.7):
            # auto get_image_7dl("gui/menu_main/dv_menu_%s.png"
            # hotspot (170, 511, 300, 38):
                # hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                # action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=2), Jump("start_7dl")]
            # hotspot (170, 563, 300, 36):
                # hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                # action [Show("settings_7dl", transition=Dissolve(0.2))]
            # hotspot (162, 615, 307, 40):
                # hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                # action [Show("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=2), Jump("scenario__sdl_achvlist_Author")]
            # hotspot (165, 665, 233, 43):
                # hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                # action [Show("contacts_7dl", transition=Dissolve(0.2))]
            # hotspot (164, 718, 153, 41):
                # hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                # action [Show("media_7dl", transition=Dissolve(0.2))]
            # hotspot (164, 772, 146, 38):
                # hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                # action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), MainMenu(confirm=False)]
    elif persistent.waifu_7dl == 4:
        imagemap at left_menu_7dl(0.1, 0.7):
            auto get_image_7dl("gui/menu_main/mi_menu_%s.png")
            hotspot (170, 511, 300, 38):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=2), Jump("start_7dl")]
            hotspot (170, 563, 300, 36):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Show("settings_7dl", transition=Dissolve(0.2))]
            hotspot (162, 615, 307, 40):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Show("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=2), Jump("scenario__sdl_achvlist_Author")]
            hotspot (165, 665, 233, 43):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Show("contacts_7dl", transition=Dissolve(0.2))]
            hotspot (164, 718, 153, 41):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Show("media_7dl", transition=Dissolve(0.2))]
            hotspot (164, 772, 146, 38):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), MainMenu(confirm=False)]     
    elif persistent.waifu_7dl == 5:
        imagemap at left_menu_7dl(0.1, 0.7):
            auto get_image_7dl("gui/menu_main/us_menu_%s.png")
            hotspot (170, 511, 300, 38):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=2), Jump("start_7dl")]
            hotspot (170, 563, 300, 36):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Show("settings_7dl", transition=Dissolve(0.2))]
            hotspot (162, 615, 307, 40):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Show("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=2), Jump("scenario__sdl_achvlist_Author")]
            hotspot (165, 665, 233, 43):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Show("contacts_7dl", transition=Dissolve(0.2))]
            hotspot (164, 718, 153, 41):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Show("media_7dl", transition=Dissolve(0.2))]
            hotspot (164, 772, 146, 38):
                hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), MainMenu(confirm=False)]
    # elif persistent.waifu_7dl == 6:
        # imagemap at left_menu_7dl(0.1, 0.7):
            # auto get_image_7dl("gui/menu_main/mt_menu_%s.png"
            # hotspot (170, 511, 300, 38):
                # hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                # action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=2), Jump("start_7dl")]
            # hotspot (170, 563, 300, 36):
                # hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                # action [Show("settings_7dl", transition=Dissolve(0.2))]
            # hotspot (162, 615, 307, 40):
                # hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                # action [Show("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=2), Jump("scenario__sdl_achvlist_Author")]
            # hotspot (165, 665, 233, 43):
                # hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                # action [Show("contacts_7dl", transition=Dissolve(0.2))]
            # hotspot (164, 718, 153, 41):
                # hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                # action [Show("media_7dl", transition=Dissolve(0.2))]
            # hotspot (164, 772, 146, 38):
                # hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
                # action [Hide("menu_7dl", transition=Dissolve(0.2)), Hide("settings_7dl", transition=Dissolve(0.2)), Hide("contacts_7dl", transition=Dissolve(0.2)), Hide("media_7dl", transition=Dissolve(0.2)), MainMenu(confirm=False)]
            
screen settings_7dl():
    tag menu
    add get_image_7dl("gui/menu_elem/settings/settings_bg.png") xalign 0.9 yalign 0.7
    if not persistent.lp_widget_7dl:
        imagebutton xalign 0.82 yalign 0.315:
            auto get_image_7dl("gui/menu_elem/settings/settings_wdgmlp_off_%s.png")
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_widget_lp_on_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_widget_lp_off_7dl", transition=Dissolve(0.2)), Hide("settings_widget_lp_on_7dl", transition=Dissolve(0.2))]
            action SetField(persistent,'lp_widget_7dl', True)
    else:
        imagebutton xalign 0.82 yalign 0.315:
            auto get_image_7dl("gui/menu_elem/settings/settings_wdgmlp_on_%s.png")
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_widget_lp_off_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_widget_lp_on_7dl", transition=Dissolve(0.2)), Hide("settings_widget_lp_off_7dl", transition=Dissolve(0.2))]
            action SetField(persistent,'lp_widget_7dl', False)
    if not persistent.music_widget_7dl:
        imagebutton xalign 0.82 yalign 0.365:
            auto get_image_7dl("gui/menu_elem/settings/settings_wdgmus_off_%s.png")
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_widget_music_on_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_widget_music_off_7dl", transition=Dissolve(0.2)), Hide("settings_widget_music_on_7dl", transition=Dissolve(0.2))]
            action SetField(persistent,'music_widget_7dl', True)
    else:
        imagebutton xalign 0.82 yalign 0.365:
            auto get_image_7dl("gui/menu_elem/settings/settings_wdgmus_on_%s.png")
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_widget_music_off_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_widget_music_on_7dl", transition=Dissolve(0.2)), Hide("settings_widget_music_off_7dl", transition=Dissolve(0.2))]
            action SetField(persistent,'music_widget_7dl', False)
    if not persistent.uv_dlc_on_7dl:
        imagebutton xalign 0.82 yalign 0.41:
            auto get_image_7dl("gui/menu_elem/settings/settings_dlc_off_%s.png")
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_dlc_on_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_dlc_off_7dl", transition=Dissolve(0.2)), Hide("settings_dlc_on_7dl", transition=Dissolve(0.2))]
            action SetField(persistent,'uv_dlc_on_7dl',True)
    else:
        imagebutton xalign 0.82 yalign 0.41:
            auto get_image_7dl("gui/menu_elem/settings/settings_dlc_on_%s.png")
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_dlc_off_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_dlc_on_7dl", transition=Dissolve(0.2)), Hide("settings_dlc_off_7dl", transition=Dissolve(0.2))]
            action SetField(persistent,'uv_dlc_on_7dl',False)
    if not persistent.hentai_un_old_7dl:
        imagebutton xalign 0.82 yalign 0.46:
            auto get_image_7dl("gui/menu_elem/settings/settings_hent_off_%s.png")
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_hentai_un_old_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_hentai_un_old_7dl", transition=Dissolve(0.2)), Hide("settings_hentai_un_new_7dl", transition=Dissolve(0.2))]
            action SetField(persistent,'hentai_un_old_7dl',True)
    else:
        imagebutton xalign 0.82 yalign 0.46:
            auto get_image_7dl("gui/menu_elem/settings/settings_hent_on_%s.png")
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_hentai_un_new_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_hentai_un_old_7dl", transition=Dissolve(0.2)), Hide("settings_hentai_un_new_7dl", transition=Dissolve(0.2))]
            action SetField(persistent,'hentai_un_old_7dl',False)
    if not persistent.chapter_off_7dl:
        imagebutton xpos 0.662 ypos 0.49:
            auto get_image_7dl("gui/menu_elem/settings/settings_chapter_on_%s.png")
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_chapter_off_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_chapter_off_7dl", transition=Dissolve(0.2)), Hide("settings_chapter_on_7dl", transition=Dissolve(0.2))]
            action SetField(persistent,'chapter_off_7dl',True)
    else:
        imagebutton xpos 0.662 ypos 0.49:
            auto get_image_7dl("gui/menu_elem/settings/settings_chapter_off_%s.png")
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_chapter_on_7dl", transition=Dissolve(0.2))
            unhovered [Hide("settings_chapter_on_7dl", transition=Dissolve(0.2)), Hide("settings_chapter_off_7dl", transition=Dissolve(0.2))]
            action SetField(persistent,'chapter_off_7dl',False)
    if (compare_music_widget_7dl != persistent.music_widget_7dl) or (compare_lp_widget_7dl != persistent.lp_widget_7dl):
        imagebutton xalign 0.81 yalign 0.8:
            auto get_image_7dl("gui/menu_elem/settings/settings_reboot_%s.png")
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            hovered Show("settings_reboot_7dl", transition=Dissolve(0.2))
            unhovered Hide("settings_reboot_7dl", transition=Dissolve(0.2))
            action Jump("widgets_on_off_7dl")
                
screen contacts_7dl():
    tag menu
    imagemap xalign 0.9 yalign 0.7:
        auto get_image_7dl("gui/menu_elem/contacts/contacts_%s.png")
        hotspot(1265, 330, 329, 59):
            action OpenURL("http://7dneyleta.ru") 
        hotspot(1265, 389, 329, 59):
            action OpenURL("https://vk.com/bl_7dl") 
        hotspot(1265, 449, 329, 59):
            action OpenURL("https://steamcommunity.com/sharedfiles/filedetails/?id=441054187") 
        hotspot(1265, 508, 329, 59):
            action OpenURL("https://vk.com/page-128046483_52530462") 
            
screen media_7dl():
    tag menu
    imagemap:   
        auto get_image_7dl("gui/menu_elem/media/media_%s.png")
        hotspot(1333, 224, 540, 160):
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            clicked [Show("alt_wip", transition=Dissolve(0.2))]
        hotspot(1218, 394, 700, 700):
            hover_sound get_sfx_7dl("ach_list/achv_click_7dl.ogg")
            clicked [Hide("media_7dl", transition=Dissolve(0.2)), Hide("menu_7dl", transition=Dissolve(0.2)), Stop('music', fadeout=2), Jump("alt_gallery_start")]
        
label main_menu_7dl:
    stop music
    stop sound
    stop sound_loop
    window hide
    call alt_day0_vars
    $ renpy.block_rollback()
    
    $ chk_music_widget_7dl()
    $ chk_lp_widget_7dl()
    $ compare_music_widget_7dl = persistent.music_widget_7dl
    $ compare_lp_widget_7dl = persistent.lp_widget_7dl
    
    if not persistent.dont_disturb:
        if persistent.mi_7dl_true or persistent.mi_7dl_good_human or persistent.mi_7dl_neutral_human or persistent.mi_7dl_bad_human or persistent.mi_7dl_good_star or persistent.mi_7dl_neutral_star or persistent.mi_7dl_bad_star or persistent.mi_7dl_herc_exc or persistent.mi_7dl_loki_exc or persistent.mi_7dl_dr_exc or persistent.mi_dj_true or persistent.mi_dj_good_jap or persistent.mi_dj_good_rf or persistent.mi_dj_bad or persistent.dv_7dl_good_ussr or persistent.dv_7dl_good_ussr_rf or persistent.dv_7dl_reject_rf or persistent.dv_7dl_reject_ussr or persistent.dv_7dl_bad_mt or persistent.dv_7dl_un or persistent.dv_7dl_tulpa or persistent.dv_7dl_bad or persistent.sl_cl_int_bad or persistent.sl_cl_int_ok or persistent.sl_cl_int_good or persistent.sl_cl_good_rf2 or persistent.sl_cl_good_rf or persistent.sl_cl_good_ussr or persistent.sl_cl_reject_same or persistent.sl_cl_reject_late or persistent.sl_cl_cata or persistent.sl_cl_bad or persistent.un_7dl_good_ussr or persistent.un_7dl_good_rf or persistent.un_7dl_true or persistent.un_7dl_true_transit or persistent.un_7dl_bad or persistent.mt_7dl_true or persistent.mt_7dl_good or persistent.mt_7dl_neutral or persistent.mt_7dl_bad or persistent.us_px_rf_good or persistent.us_px_true or persistent.us_7dl_bad or persistent.us_7dl_good or persistent.us_7dl_true or persistent.us_7dl_un or persistent.us_7dl_mi:
            scene bg ext_city_night_7dl with fade
            play music music_7dl["seven_summer_days"] fadein 3
            $ renpy.transition(dissolve)
            call screen help_7dl
    
label random_bg_7dl:
    if len(list_waifu_7dl) == 4: #max 6
        $ list_waifu_7dl = []
    if persistent.waifu_7dl == 0:
        $ persistent.waifu_7dl = renpy.random.choice([1, 2, 4, 5])
    elif persistent.waifu_7dl == 1:
        $ persistent.waifu_7dl = renpy.random.choice([2, 4, 5])
    elif persistent.waifu_7dl == 2:
        $ persistent.waifu_7dl = renpy.random.choice([1, 4, 5])
    #elif persistent.waifu_7dl == 3:
        #$ persistent.waifu_7dl = renpy.random.choice([1, 2, 4, 5, 6])
    elif persistent.waifu_7dl == 4:
        $ persistent.waifu_7dl = renpy.random.choice([1, 2, 5])
    elif persistent.waifu_7dl == 5:
        $ persistent.waifu_7dl = renpy.random.choice([1, 2, 4])
    #elif persistent.waifu_7dl == 6:
        #$ persistent.waifu_7dl = renpy.random.choice([1, 2, 3, 4, 5])
    if persistent.waifu_7dl == 1 and 'un' not in list_waifu_7dl:
        play music music_7dl["take_my_hand"] fadein 3
        $ list_waifu_7dl.append('un')
        scene bg un_bg_7dl with fade
        call screen menu_7dl
    if persistent.waifu_7dl == 2 and 'sl' not in list_waifu_7dl:
        $ list_waifu_7dl.append('sl')
        scene bg sl_bg_7dl with fade
        play music music_7dl["slavyas_fantazm"] fadein 3
        call screen menu_7dl
    #if persistent.waifu_7dl == 3 and 'dv' not in list_waifu_7dl:
        #$ list_waifu_7dl.append('dv')
        #scene bg dv_bg_7dl with fade
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
        #scene bg mt_bg_7dl with fade
        #play music music_7dl["wheres_wonderland"] fadein 3
        #call screen menu_7dl
    else:
        jump main_menu_7dl
        
label widgets_on_off_7dl:
    python:
        if persistent.lp_widget_7dl:
            add_lp_widget_7dl()
        else:
            del_lp_widget_7dl()
        if persistent.music_widget_7dl:
            add_music_widget_7dl()
        else:
            del_music_widget_7dl()
        renpy.utter_restart()

label start_7dl:
    call alt_day0_vars
    call alt_day0_prologue
    jump main_menu_7dl