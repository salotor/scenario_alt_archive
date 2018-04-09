init 1:
    
    $ page_7dl = 1
    $ show_image_7dl = ""
    $ gallery_mode_7dl = ""
    $ filter_7dl = ""
    
    $ style.page_7dl_text = Style(style.default)
    $ style.page_7dl_text.font  = get_image_7dl("gui/gallery/ofont_ru_a_AvanteLtNr.ttf")
    $ style.page_7dl_text.color = "#ffffff"
    $ style.page_7dl_text.size = 60
    
    image bg gallery_7dl = get_image_7dl("gui/gallery/gallery_bg.png")
    $ locked_img_7dl = ["gallery_stub_1.png", "gallery_stub_2.png", "gallery_stub_3.png", "gallery_stub_4.png", "gallery_stub_5.png", 
                        "gallery_stub_6.png", "gallery_stub_7.png", "gallery_stub_8.png", "gallery_stub_9.png"]
        
screen gallery_main_7dl:
    add get_image_7dl("gui/gallery/gallery_bg.png")
    if not gallery_mode_7dl == "bgs":
        imagebutton: 
            auto get_image_7dl("gui/gallery/gallery_navig_bgs_%s.png") xalign 0.31 yalign 0.029 
            action [Show("bgs_7dl_1", transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", "bgs"), SetVariable("page_7dl", 1)]
        imagebutton: 
            auto get_image_7dl("gui/gallery/gallery_navig_filter_%s.png") xalign 0.9764 yalign 0.124 
            action [Show("filter_settings_7dl", transition=Dissolve(0.2)), SetVariable("page_7dl", 1)]
    elif gallery_mode_7dl == "arts":
        imagebutton: 
            auto get_image_7dl("gui/gallery/gallery_navig_bgs_%s.png") xalign 0.31 yalign 0.029 
            action NullAction()
    else:
        imagebutton: 
            auto get_image_7dl("gui/gallery/gallery_navig_bgs_%s.png") xalign 0.31 yalign 0.029 
            action [Hide("bgs_7dl_%s" % str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", "none")]
    if not gallery_mode_7dl == "arts":
        imagebutton: 
            auto get_image_7dl("gui/gallery/gallery_navig_arts_%s.png") xalign 0.733 yalign 0.032 
            action [Show("art_7dl_1", transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", "arts"), SetVariable("page_7dl", 1)]
    elif gallery_mode_7dl == "bgs":
        imagebutton: 
            auto get_image_7dl("gui/gallery/gallery_navig_arts_%s.png") xalign 0.733 yalign 0.032 
            action NullAction()
    else:
        imagebutton:
            auto get_image_7dl("gui/gallery/gallery_navig_arts_%s.png") xalign 0.733 yalign 0.032 
            action [Hide("art_7dl_%s" % str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", "none")]
    if gallery_mode_7dl == "":
        timer 0.01 action [Show("art_7dl_%s" % str(page_7dl), transition=Dissolve(1.0)), Show("gallery_bw_7dl", transition=Dissolve(1.0)), Show("gallery_fw_7dl", transition=Dissolve(1.0)), SetVariable("gallery_mode_7dl", "arts")]
    elif gallery_mode_7dl == "bgs":
        timer 0.01 action [Show("bgs_7dl_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "arts":
        timer 0.01 action [Show("art_7dl_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2))]
    elif filter_7dl == "un":
        timer 0.01 action [Show("art_7dl_un_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2))]
    elif filter_7dl == "sl":
        timer 0.01 action [Show("art_7dl_sl_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2))]
    elif filter_7dl == "dv":
        timer 0.01 action [Show("art_7dl_dv_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2))]
    elif filter_7dl == "mi":
        timer 0.01 action [Show("art_7dl_mi_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2))]
    elif filter_7dl == "us":
        timer 0.01 action [Show("art_7dl_us_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2))]
    elif filter_7dl == "mt":
        timer 0.01 action [Show("art_7dl_mt_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2))]

screen gallery_exit_7dl:
    if gallery_mode_7dl == "bgs":
        imagebutton: 
            auto get_image_7dl("gui/gallery/gallery_navig_bgs_%s.png") xalign 0.31 yalign 0.029 
            action [Hide("bgs_7dl_%s" % str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", "none")]
        
screen gallery_bw_7dl:
    if gallery_mode_7dl == "bgs":
        if renpy.get_screen("bgs_7dl_1"):
            pass
        else:
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_backward_%s.png") xalign 0.045 yalign 0.5 
                if renpy.get_screen("bgs_7dl_2"):
                    action [SetVariable("page_7dl", 1), Hide("bgs_7dl_2", transition=Dissolve(0.2)), Show("bgs_7dl_1", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_3"):
                    action [SetVariable("page_7dl", 2), Hide("bgs_7dl_3", transition=Dissolve(0.2)), Show("bgs_7dl_2", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_4"):
                    action [SetVariable("page_7dl", 3), Hide("bgs_7dl_4", transition=Dissolve(0.2)), Show("bgs_7dl_3", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_5"):
                    action [SetVariable("page_7dl", 4), Hide("bgs_7dl_5", transition=Dissolve(0.2)), Show("bgs_7dl_4", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_6"):
                    action [SetVariable("page_7dl", 5), Hide("bgs_7dl_6", transition=Dissolve(0.2)), Show("bgs_7dl_5", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_7"):
                    action [SetVariable("page_7dl", 6), Hide("bgs_7dl_7", transition=Dissolve(0.2)), Show("bgs_7dl_6", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_8"):
                    action [SetVariable("page_7dl", 7), Hide("bgs_7dl_8", transition=Dissolve(0.2)), Show("bgs_7dl_7", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_9"):
                    action [SetVariable("page_7dl", 8), Hide("bgs_7dl_9", transition=Dissolve(0.2)), Show("bgs_7dl_8", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_10"):
                    action [SetVariable("page_7dl", 9), Hide("bgs_7dl_10", transition=Dissolve(0.2)), Show("bgs_7dl_9", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_11"):
                    action [SetVariable("page_7dl", 10), Hide("bgs_7dl_11", transition=Dissolve(0.2)), Show("bgs_7dl_10", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_12"):
                    action [SetVariable("page_7dl", 11), Hide("bgs_7dl_12", transition=Dissolve(0.2)), Show("bgs_7dl_11", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_13"):
                    action [SetVariable("page_7dl", 12), Hide("bgs_7dl_13", transition=Dissolve(0.2)), Show("bgs_7dl_12", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_14"):
                    action [SetVariable("page_7dl", 13), Hide("bgs_7dl_14", transition=Dissolve(0.2)), Show("bgs_7dl_13", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_15"):
                    action [SetVariable("page_7dl", 14), Hide("bgs_7dl_15", transition=Dissolve(0.2)), Show("bgs_7dl_14", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_16"):
                    action [SetVariable("page_7dl", 15), Hide("bgs_7dl_16", transition=Dissolve(0.2)), Show("bgs_7dl_15", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_17"):
                    action [SetVariable("page_7dl", 16), Hide("bgs_7dl_17", transition=Dissolve(0.2)), Show("bgs_7dl_16", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_18"):
                    action [SetVariable("page_7dl", 17), Hide("bgs_7dl_18", transition=Dissolve(0.2)), Show("bgs_7dl_17", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_19"):
                    action [SetVariable("page_7dl", 18), Hide("bgs_7dl_19", transition=Dissolve(0.2)), Show("bgs_7dl_18", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_20"):
                    action [SetVariable("page_7dl", 19), Hide("bgs_7dl_20", transition=Dissolve(0.2)), Show("bgs_7dl_19", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_21"):
                    action [SetVariable("page_7dl", 20), Hide("bgs_7dl_21", transition=Dissolve(0.2)), Show("bgs_7dl_20", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_22"):
                    action [SetVariable("page_7dl", 21), Hide("bgs_7dl_22", transition=Dissolve(0.2)), Show("bgs_7dl_21", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_23"):
                    action [SetVariable("page_7dl", 22), Hide("bgs_7dl_23", transition=Dissolve(0.2)), Show("bgs_7dl_22", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_24"):
                    action [SetVariable("page_7dl", 23), Hide("bgs_7dl_24", transition=Dissolve(0.2)), Show("bgs_7dl_23", transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "arts":
        if renpy.get_screen("art_7dl_1"):
            pass
        else:
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_backward_%s.png") xalign 0.045 yalign 0.5
                if renpy.get_screen("art_7dl_2"):
                    action [SetVariable("page_7dl", 1), Hide("art_7dl_2", transition=Dissolve(0.2)), Show("art_7dl_1", transition=Dissolve(0.2))]
                elif renpy.get_screen("art_7dl_3"):
                    action [SetVariable("page_7dl", 2), Hide("art_7dl_3", transition=Dissolve(0.2)), Show("art_7dl_2", transition=Dissolve(0.2))]
                elif renpy.get_screen("art_7dl_4"):
                    action [SetVariable("page_7dl", 3), Hide("art_7dl_4", transition=Dissolve(0.2)), Show("art_7dl_3", transition=Dissolve(0.2))]
                elif renpy.get_screen("art_7dl_5"):
                    action [SetVariable("page_7dl", 4), Hide("art_7dl_5", transition=Dissolve(0.2)), Show("art_7dl_4", transition=Dissolve(0.2))]
                elif renpy.get_screen("art_7dl_6"):
                    action [SetVariable("page_7dl", 5), Hide("art_7dl_6", transition=Dissolve(0.2)), Show("art_7dl_5", transition=Dissolve(0.2))]
                elif renpy.get_screen("art_7dl_7"):
                    action [SetVariable("page_7dl", 6), Hide("art_7dl_7", transition=Dissolve(0.2)), Show("art_7dl_6", transition=Dissolve(0.2))]
                elif renpy.get_screen("art_7dl_8"):
                    action [SetVariable("page_7dl", 7), Hide("art_7dl_8", transition=Dissolve(0.2)), Show("art_7dl_7", transition=Dissolve(0.2))]
    elif filter_7dl == "un":
        if renpy.get_screen("art_7dl_un_1"):
            pass
        else:
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_backward_%s.png") xalign 0.045 yalign 0.5
                action [SetVariable("page_7dl", 1), Hide("art_7dl_un_2", transition=Dissolve(0.2)), Show("art_7dl_un_1", transition=Dissolve(0.2))]
    elif filter_7dl == "sl":
        pass
    elif filter_7dl == "dv":
        pass
    elif filter_7dl == "mi":
        if renpy.get_screen("art_7dl_mi_1"):
            pass
        else:
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_backward_%s.png") xalign 0.045 yalign 0.5
                action [SetVariable("page_7dl", 1), Hide("art_7dl_mi_2", transition=Dissolve(0.2)), Show("art_7dl_mi_1", transition=Dissolve(0.2))]
    elif filter_7dl == "us":
        pass
    elif filter_7dl == "mt":
        pass
     
screen gallery_fw_7dl:
    if gallery_mode_7dl == "bgs":
        if renpy.get_screen("bgs_7dl_24"):
            pass
        else:
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_forward_%s.png") xalign 0.957 yalign 0.5
                if renpy.get_screen("bgs_7dl_1"):
                    action [SetVariable("page_7dl", 2), Hide("bgs_7dl_1", transition=Dissolve(0.2)), Show("bgs_7dl_2", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_2"):
                    action [SetVariable("page_7dl", 3), Hide("bgs_7dl_2", transition=Dissolve(0.2)), Show("bgs_7dl_3", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_3"):
                    action [SetVariable("page_7dl", 4), Hide("bgs_7dl_3", transition=Dissolve(0.2)), Show("bgs_7dl_4", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_4"):
                    action [SetVariable("page_7dl", 5), Hide("bgs_7dl_4", transition=Dissolve(0.2)), Show("bgs_7dl_5", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_5"):
                    action [SetVariable("page_7dl", 6), Hide("bgs_7dl_5", transition=Dissolve(0.2)), Show("bgs_7dl_6", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_6"):
                    action [SetVariable("page_7dl", 7), Hide("bgs_7dl_6", transition=Dissolve(0.2)), Show("bgs_7dl_7", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_7"):
                    action [SetVariable("page_7dl", 8), Hide("bgs_7dl_7", transition=Dissolve(0.2)), Show("bgs_7dl_8", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_8"):
                    action [SetVariable("page_7dl", 9), Hide("bgs_7dl_8", transition=Dissolve(0.2)), Show("bgs_7dl_9", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_9"):
                    action [SetVariable("page_7dl", 10), Hide("bgs_7dl_9", transition=Dissolve(0.2)), Show("bgs_7dl_10", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_10"):
                    action [SetVariable("page_7dl", 11), Hide("bgs_7dl_10", transition=Dissolve(0.2)), Show("bgs_7dl_11", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_11"):
                    action [SetVariable("page_7dl", 12), Hide("bgs_7dl_11", transition=Dissolve(0.2)), Show("bgs_7dl_12", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_12"):
                    action [SetVariable("page_7dl", 13), Hide("bgs_7dl_12", transition=Dissolve(0.2)), Show("bgs_7dl_13", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_13"):
                    action [SetVariable("page_7dl", 14), Hide("bgs_7dl_13", transition=Dissolve(0.2)), Show("bgs_7dl_14", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_14"):
                    action [SetVariable("page_7dl", 15), Hide("bgs_7dl_14", transition=Dissolve(0.2)), Show("bgs_7dl_15", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_15"):
                    action [SetVariable("page_7dl", 16), Hide("bgs_7dl_15", transition=Dissolve(0.2)), Show("bgs_7dl_16", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_16"):
                    action [SetVariable("page_7dl", 17), Hide("bgs_7dl_16", transition=Dissolve(0.2)), Show("bgs_7dl_17", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_17"):
                    action [SetVariable("page_7dl", 18), Hide("bgs_7dl_17", transition=Dissolve(0.2)), Show("bgs_7dl_18", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_18"):
                    action [SetVariable("page_7dl", 19), Hide("bgs_7dl_18", transition=Dissolve(0.2)), Show("bgs_7dl_19", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_19"):
                    action [SetVariable("page_7dl", 20), Hide("bgs_7dl_19", transition=Dissolve(0.2)), Show("bgs_7dl_20", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_20"):
                    action [SetVariable("page_7dl", 21), Hide("bgs_7dl_20", transition=Dissolve(0.2)), Show("bgs_7dl_21", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_21"):
                    action [SetVariable("page_7dl", 22), Hide("bgs_7dl_21", transition=Dissolve(0.2)), Show("bgs_7dl_22", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_22"):
                    action [SetVariable("page_7dl", 23), Hide("bgs_7dl_22", transition=Dissolve(0.2)), Show("bgs_7dl_23", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_23"):
                    action [SetVariable("page_7dl", 24), Hide("bgs_7dl_23", transition=Dissolve(0.2)), Show("bgs_7dl_24", transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "arts":
            if renpy.get_screen("art_7dl_8"):
                pass
            else:
                imagebutton:
                    auto get_image_7dl("gui/gallery/gallery_navig_forward_%s.png") xalign 0.957 yalign 0.5
                    if renpy.get_screen("art_7dl_1"):
                        action [SetVariable("page_7dl", 2), Hide("art_7dl_1", transition=Dissolve(0.2)), Show("art_7dl_2", transition=Dissolve(0.2))]
                    elif renpy.get_screen("art_7dl_2"):
                        action [SetVariable("page_7dl", 3), Hide("art_7dl_2", transition=Dissolve(0.2)), Show("art_7dl_3", transition=Dissolve(0.2))]
                    elif renpy.get_screen("art_7dl_3"):
                        action [SetVariable("page_7dl", 4), Hide("art_7dl_3", transition=Dissolve(0.2)), Show("art_7dl_4", transition=Dissolve(0.2))]
                    elif renpy.get_screen("art_7dl_4"):
                        action [SetVariable("page_7dl", 5), Hide("art_7dl_4", transition=Dissolve(0.2)), Show("art_7dl_5", transition=Dissolve(0.2))]
                    elif renpy.get_screen("art_7dl_5"):
                        action [SetVariable("page_7dl", 6), Hide("art_7dl_5", transition=Dissolve(0.2)), Show("art_7dl_6", transition=Dissolve(0.2))]
                    elif renpy.get_screen("art_7dl_6"):
                        action [SetVariable("page_7dl", 7), Hide("art_7dl_6", transition=Dissolve(0.2)), Show("art_7dl_7", transition=Dissolve(0.2))]
                    elif renpy.get_screen("art_7dl_7"):
                        action [SetVariable("page_7dl", 8), Hide("art_7dl_7", transition=Dissolve(0.2)), Show("art_7dl_8", transition=Dissolve(0.2))]
    elif filter_7dl == "un":
        if renpy.get_screen("art_7dl_un_2"):
            pass
        elif renpy.get_screen("art_7dl_un_1"):
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_forward_%s.png") xalign 0.957 yalign 0.5
                action [SetVariable("page_7dl", 2), Hide("art_7dl_un_1", transition=Dissolve(0.2)), Show("art_7dl_un_2", transition=Dissolve(0.2))]
    elif filter_7dl == "sl":
        pass
    elif filter_7dl == "dv":
        pass
    elif filter_7dl == "mi":
        if renpy.get_screen("art_7dl_mi_2"):
            pass
        else:
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_backward_%s.png") xalign 0.045 yalign 0.5
                action [SetVariable("page_7dl", 2), Hide("art_7dl_mi_1", transition=Dissolve(0.2)), Show("art_7dl_mi_2", transition=Dissolve(0.2))]
    elif filter_7dl == "us":
        pass
    elif filter_7dl == "mt":
        pass
                    
screen gallery_fw_7dl:
    if gallery_mode_7dl == "bgs":
        if renpy.get_screen("bgs_7dl_24"):
            pass
        else:
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_forward_%s.png") xalign 0.957 yalign 0.5
                if renpy.get_screen("bgs_7dl_1"):
                    action [SetVariable("page_7dl", 2), Hide("bgs_7dl_1", transition=Dissolve(0.2)), Show("bgs_7dl_2", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_2"):
                    action [SetVariable("page_7dl", 3), Hide("bgs_7dl_2", transition=Dissolve(0.2)), Show("bgs_7dl_3", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_3"):
                    action [SetVariable("page_7dl", 4), Hide("bgs_7dl_3", transition=Dissolve(0.2)), Show("bgs_7dl_4", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_4"):
                    action [SetVariable("page_7dl", 5), Hide("bgs_7dl_4", transition=Dissolve(0.2)), Show("bgs_7dl_5", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_5"):
                    action [SetVariable("page_7dl", 6), Hide("bgs_7dl_5", transition=Dissolve(0.2)), Show("bgs_7dl_6", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_6"):
                    action [SetVariable("page_7dl", 7), Hide("bgs_7dl_6", transition=Dissolve(0.2)), Show("bgs_7dl_7", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_7"):
                    action [SetVariable("page_7dl", 8), Hide("bgs_7dl_7", transition=Dissolve(0.2)), Show("bgs_7dl_8", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_8"):
                    action [SetVariable("page_7dl", 9), Hide("bgs_7dl_8", transition=Dissolve(0.2)), Show("bgs_7dl_9", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_9"):
                    action [SetVariable("page_7dl", 10), Hide("bgs_7dl_9", transition=Dissolve(0.2)), Show("bgs_7dl_10", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_10"):
                    action [SetVariable("page_7dl", 11), Hide("bgs_7dl_10", transition=Dissolve(0.2)), Show("bgs_7dl_11", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_11"):
                    action [SetVariable("page_7dl", 12), Hide("bgs_7dl_11", transition=Dissolve(0.2)), Show("bgs_7dl_12", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_12"):
                    action [SetVariable("page_7dl", 13), Hide("bgs_7dl_12", transition=Dissolve(0.2)), Show("bgs_7dl_13", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_13"):
                    action [SetVariable("page_7dl", 14), Hide("bgs_7dl_13", transition=Dissolve(0.2)), Show("bgs_7dl_14", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_14"):
                    action [SetVariable("page_7dl", 15), Hide("bgs_7dl_14", transition=Dissolve(0.2)), Show("bgs_7dl_15", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_15"):
                    action [SetVariable("page_7dl", 16), Hide("bgs_7dl_15", transition=Dissolve(0.2)), Show("bgs_7dl_16", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_16"):
                    action [SetVariable("page_7dl", 17), Hide("bgs_7dl_16", transition=Dissolve(0.2)), Show("bgs_7dl_17", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_17"):
                    action [SetVariable("page_7dl", 18), Hide("bgs_7dl_17", transition=Dissolve(0.2)), Show("bgs_7dl_18", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_18"):
                    action [SetVariable("page_7dl", 19), Hide("bgs_7dl_18", transition=Dissolve(0.2)), Show("bgs_7dl_19", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_19"):
                    action [SetVariable("page_7dl", 20), Hide("bgs_7dl_19", transition=Dissolve(0.2)), Show("bgs_7dl_20", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_20"):
                    action [SetVariable("page_7dl", 21), Hide("bgs_7dl_20", transition=Dissolve(0.2)), Show("bgs_7dl_21", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_21"):
                    action [SetVariable("page_7dl", 22), Hide("bgs_7dl_21", transition=Dissolve(0.2)), Show("bgs_7dl_22", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_22"):
                    action [SetVariable("page_7dl", 23), Hide("bgs_7dl_22", transition=Dissolve(0.2)), Show("bgs_7dl_23", transition=Dissolve(0.2))]
                elif renpy.get_screen("bgs_7dl_23"):
                    action [SetVariable("page_7dl", 24), Hide("bgs_7dl_23", transition=Dissolve(0.2)), Show("bgs_7dl_24", transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "arts":
            if renpy.get_screen("art_7dl_8"):
                pass
            else:
                imagebutton:
                    auto get_image_7dl("gui/gallery/gallery_navig_forward_%s.png") xalign 0.957 yalign 0.5
                    if renpy.get_screen("art_7dl_1"):
                        action [SetVariable("page_7dl", 2), Hide("art_7dl_1", transition=Dissolve(0.2)), Show("art_7dl_2", transition=Dissolve(0.2))]
                    elif renpy.get_screen("art_7dl_2"):
                        action [SetVariable("page_7dl", 3), Hide("art_7dl_2", transition=Dissolve(0.2)), Show("art_7dl_3", transition=Dissolve(0.2))]
                    elif renpy.get_screen("art_7dl_3"):
                        action [SetVariable("page_7dl", 4), Hide("art_7dl_3", transition=Dissolve(0.2)), Show("art_7dl_4", transition=Dissolve(0.2))]
                    elif renpy.get_screen("art_7dl_4"):
                        action [SetVariable("page_7dl", 5), Hide("art_7dl_4", transition=Dissolve(0.2)), Show("art_7dl_5", transition=Dissolve(0.2))]
                    elif renpy.get_screen("art_7dl_5"):
                        action [SetVariable("page_7dl", 6), Hide("art_7dl_5", transition=Dissolve(0.2)), Show("art_7dl_6", transition=Dissolve(0.2))]
                    elif renpy.get_screen("art_7dl_6"):
                        action [SetVariable("page_7dl", 7), Hide("art_7dl_6", transition=Dissolve(0.2)), Show("art_7dl_7", transition=Dissolve(0.2))]
                    elif renpy.get_screen("art_7dl_7"):
                        action [SetVariable("page_7dl", 8), Hide("art_7dl_7", transition=Dissolve(0.2)), Show("art_7dl_8", transition=Dissolve(0.2))]
    elif filter_7dl == "un":
        if renpy.get_screen("art_7dl_un_2"):
            pass
        elif renpy.get_screen("art_7dl_un_1"):
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_forward_%s.png") xalign 0.957 yalign 0.5
                action [SetVariable("page_7dl", 2), Hide("art_7dl_un_1", transition=Dissolve(0.2)), Show("art_7dl_un_2", transition=Dissolve(0.2))]
    elif filter_7dl == "sl":
        pass
    elif filter_7dl == "dv":
        pass
    elif filter_7dl == "mi":
        if renpy.get_screen("art_7dl_mi_2"):
            pass
        else:
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_backward_%s.png") xalign 0.045 yalign 0.5
                action [SetVariable("page_7dl", 2), Hide("art_7dl_mi_1", transition=Dissolve(0.2)), Show("art_7dl_mi_2", transition=Dissolve(0.2))]
    elif filter_7dl == "us":
        pass
    elif filter_7dl == "mt":
        pass

screen bgs_7dl_1:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/24"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg d4_hatch_night_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/d4_hatch_night_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("bgs_7dl_1", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg d4_hatch_night_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg d4_hatch_night_open_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/d4_hatch_night_open_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("bgs_7dl_1", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg d4_hatch_night_open_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.154
    if renpy.seen_image("bg d4_mi_kandji_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/d4_mi_kandji_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("bgs_7dl_1", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg d4_mi_kandji_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg d5_rainy_idle_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/d5_rainy_idle_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("bgs_7dl_1", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg d5_rainy_idle_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg d7_dv_noir_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/d7_dv_noir_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("bgs_7dl_1", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg d7_dv_noir_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg d7_un_epilogue_bad_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/d7_un_epilogue_bad_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide("bgs_7dl_1", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "d7_un_epilogue_bad_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen bgs_7dl_2:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/24"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg d7_un_epilogue_bad2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/d7_un_epilogue_bad2_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("bgs_7dl_2", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg d7_un_epilogue_bad2_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg ext_adductius_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_adductius_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("bgs_7dl_2", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_adductius_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.154
    if renpy.seen_image("bg ext_admins_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_admins_day_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("bgs_7dl_2", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_admins_day_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg ext_admins_night_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_admins_night_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("bgs_7dl_2", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_admins_night_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg ext_admins_rain_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_admins_rain_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("bgs_7dl_2", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_admins_rain_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg ext_bathhouse_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_bathhouse_day_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide("bgs_7dl_2", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "ext_bathhouse_day_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
       
screen bgs_7dl_3:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/24"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg ext_beach2_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_beach2_day_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("bgs_7dl_3", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_beach2_day_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg ext_boathouse_sunset_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_boathouse_sunset_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("bgs_7dl_3", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_boathouse_sunset_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.154
    if renpy.seen_image("bg ext_bus1_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_bus1_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("bgs_7dl_3", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_bus1_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg ext_city_night_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_city_night_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("bgs_7dl_3", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_city_night_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg ext_clubs_sunset_rain_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_clubs_sunset_rain_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("bgs_7dl_3", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_clubs_sunset_rain_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg ext_countryside_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_countryside_day_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide("bgs_7dl_3", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_countryside_day_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
        
screen bgs_7dl_4:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/24"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg ext_dining_hall_away_night_uvao1_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_dining_hall_away_night_uvao1_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("bgs_7dl_4", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_dining_hall_away_night_uvao1_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg ext_dining_hall_away_night_uvao2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_dining_hall_away_night_uvao2_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("bgs_7dl_4", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_dining_hall_away_night_uvao2_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.154
    if renpy.seen_image("bg ext_dining_hall_near_snowy_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_dining_hall_near_snowy_day_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("bgs_7dl_4", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "ext_dining_hall_near_snowy_day_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg ext_earth_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_earth_7dl_%s.png")xalign 0.2 yalign 0.93 
            action [Hide("bgs_7dl_4", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_earth_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg ext_entrance_night_clear_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_entrance_night_clear_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("bgs_7dl_4", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_entrance_night_clear_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg ext_entrance_night_clear_closed_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_entrance_night_clear_closed_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide("bgs_7dl_4", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "ext_entrance_night_clear_closed_7dl"), Jump("show_image_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
       
screen bgs_7dl_5:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/24"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg ext_entrance_winter_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_entrance_winter_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("bgs_7dl_5", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_entrance_winter_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg ext_graveyard_rain_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_graveyard_rain_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("bgs_7dl_5", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_graveyard_rain_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.154
    if renpy.seen_image("bg ext_hospital2_away_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_hospital2_away_day_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("bgs_7dl_5", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_hospital2_away_day_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg ext_hospital2_away_night_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_hospital2_away_night_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("bgs_7dl_5", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_hospital2_away_night_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg ext_house_of_mt_snowy_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_house_of_mt_snowy_day_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("bgs_7dl_5", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_house_of_mt_snowy_day_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg ext_house_of_un_night_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_house_of_un_night_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide("bgs_7dl_5", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_house_of_un_night_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
        
screen bgs_7dl_6:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/24"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg ext_houses_night_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_houses_night_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("bgs_7dl_6", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_houses_night_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg ext_houses_rainy_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_houses_rainy_day_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("bgs_7dl_6", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_houses_rainy_day_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.154
    if renpy.seen_image("bg ext_houses_snowy_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_houses_rainy_day_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("bgs_7dl_6", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_houses_snowy_day_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg ext_khruschevka_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_khruschevka_day_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("bgs_7dl_6", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_khruschevka_day_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg ext_lake_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_lake_day_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("bgs_7dl_6", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_lake_day_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg ext_lake_night_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_lake_night_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide("bgs_7dl_6", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_lake_night_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
        
screen bgs_7dl_7:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/24"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg ext_lake_sunset_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_lake_sunset_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("bgs_7dl_7", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_lake_sunset_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg ext_lib_sunset_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_lib_sunset_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("bgs_7dl_7", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_lib_sunset_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.154
    if renpy.seen_image("bg ext_med_sunset_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_med_sunset_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("bgs_7dl_7", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_med_sunset_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg ext_med2_sunset_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_med2_sunset_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("bgs_7dl_7", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "ext_med2_sunset_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg ext_musclub_night_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_musclub_night_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("bgs_7dl_7", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_musclub_night_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg ext_musclub_snowy_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_musclub_snowy_day_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide("bgs_7dl_7", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_musclub_snowy_day_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
        
screen bgs_7dl_8:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/24"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg ext_mv2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_mv2_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("bgs_7dl_8", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_mv2_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg ext_night_sky_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_night_sky_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("bgs_7dl_8", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_night_sky_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.154
    if renpy.seen_image("bg ext_old_building_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_old_building_day_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("bgs_7dl_8", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_old_building_day_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg ext_old_building_sunset_red_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_old_building_sunset_red_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("bgs_7dl_8", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_old_building_sunset_red_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg ext_playground2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_playground2_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("bgs_7dl_8", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_playground2_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg ext_road_sunset_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_road_sunset_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide("bgs_7dl_8", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_road_sunset_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
        
screen bgs_7dl_9:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/24"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg ext_road_winter_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_road_winter_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("bgs_7dl_9", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_road_winter_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15 
    if renpy.seen_image("bg ext_sandpit_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_sandpit_day_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("bgs_7dl_9", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_sandpit_day_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.154
    if renpy.seen_image("bg ext_seashore_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_seashore_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("bgs_7dl_9", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_seashore_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg ext_shower_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_shower_day_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("bgs_7dl_9", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_shower_day_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg ext_shower_night_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_shower_night_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("bgs_7dl_9", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_shower_night_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg ext_sky_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_sky_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide("bgs_7dl_9", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_sky_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
        
screen bgs_7dl_10:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/24"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg ext_sky2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_sky2_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("bgs_7dl_10", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_sky2_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg ext_square_rain_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_square_rain_day_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("bgs_7dl_10", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_square_rain_day_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.154
    if renpy.seen_image("bg ext_square_sunset2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_square_sunset2_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("bgs_7dl_10", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_square_sunset2_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg ext_square_sunset3_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_square_sunset3_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("bgs_7dl_10", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_square_sunset3_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg ext_stage_big_clear_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_stage_big_clear_day_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("bgs_7dl_10", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_stage_big_clear_day_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg ext_stage_big_sunset_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_stage_big_sunset_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide("bgs_7dl_10", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_stage_big_sunset_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
        
screen bgs_7dl_11:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/24"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg ext_stage_near_clear_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_stage_near_clear_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("bgs_7dl_11", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_stage_near_clear_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg ext_stairs_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_stairs_day_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("bgs_7dl_11", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_stairs_day_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.154
    if renpy.seen_image("bg ext_stairs_night_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_stairs_night_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("bgs_7dl_11", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_stairs_night_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg ext_stairs_sunset_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_stairs_sunset_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("bgs_7dl_11", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_stairs_sunset_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg ext_stand_pr_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_stand_pr_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("bgs_7dl_11", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_stand_pr_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg ext_stand3_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_stand3_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide("bgs_7dl_11", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_stand3_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
       
screen bgs_7dl_12:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/24"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg ext_tennis_court_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_tennis_court_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("bgs_7dl_12", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_tennis_court_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg ext_townscape_ph_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_townscape_ph_day_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("bgs_7dl_12", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_townscape_ph_day_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.154
    if renpy.seen_image("bg ext_un_hideout_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_un_hideout_day_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("bgs_7dl_12", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_un_hideout_day_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg ext_un_hideout_night_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_un_hideout_night_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("bgs_7dl_12", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_un_hideout_night_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg ext_un_hideout_sunset_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_un_hideout_sunset_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("bgs_7dl_12", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_un_hideout_sunset_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg ext_un_house_with_un_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_un_house_with_un_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide("bgs_7dl_12", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_un_house_with_un_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
        
screen bgs_7dl_13:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/24"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg ext_underwater_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_underwater_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("bgs_7dl_13", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_underwater_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg ext_underwater2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_underwater2_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("bgs_7dl_13", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_underwater2_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.154
    if renpy.seen_image("bg ext_underwater3_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_underwater3_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("bgs_7dl_13", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_underwater3_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg ext_volley_court_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_volley_court_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("bgs_7dl_13", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_volley_court_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg ext_warehouse_blurry_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_warehouse_blurry_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("bgs_7dl_13", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_warehouse_blurry_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg ext_warehouse_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_warehouse_day_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide("bgs_7dl_13", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_warehouse_day_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
        
screen bgs_7dl_14:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/24"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg ext_warehouse_night_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_warehouse_night_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("bgs_7dl_14", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_warehouse_night_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg ext_warehouse_rain_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_warehouse_rain_day_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("bgs_7dl_14", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_warehouse_rain_day_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.154
    if renpy.seen_image("bg ext_warehouse2_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_warehouse2_day_7dl_%s.png") xalign 0.8 yalign 0.15
            action [Hide("bgs_7dl_14", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_warehouse2_day_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg ext_washstand_night_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_washstand_night_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("bgs_7dl_14", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_washstand_night_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg ext_washstand_sunset_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_washstand_sunset_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("bgs_7dl_14", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_washstand_sunset_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg ext_winter_night_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_winter_night_7dl_%s.png")xalign 0.8 yalign 0.93 
            action [Hide("bgs_7dl_14", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_winter_night_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
        
screen bgs_7dl_15:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/24"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg ext_winterpark_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_winterpark_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("bgs_7dl_15", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_winterpark_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg ext_winterpark_sunset_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_winterpark_sunset_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("bgs_7dl_15", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_winterpark_sunset_7dl"), Jump("show_image_7dl")]  
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.154
    if renpy.seen_image("bg int_access_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_access_day_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("bgs_7dl_15", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_access_day_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg int_access2_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_access2_day_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("bgs_7dl_15", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_access2_day_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg int_admins_window_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_admins_window_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("bgs_7dl_15", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_admins_window_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg int_admins_window_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_admins_window_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide("bgs_7dl_15", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_admins_window_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
        
screen bgs_7dl_16:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/24"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg int_attic_ladder_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_attic_ladder_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("bgs_7dl_16", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_attic_ladder_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg int_attic2_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_attic2_day_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("bgs_7dl_16", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_attic2_day_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.154
    if renpy.seen_image("bg int_attic2_night_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_attic2_night_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("bgs_7dl_16", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_attic2_night_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg int_bus_warp_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_bus_warp_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("bgs_7dl_16", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_bus_warp_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg int_caffee_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_caffee_day_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("bgs_7dl_16", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_caffee_day_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg int_catacomb_door_fullbright_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_catacomb_door_fullbright_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide("bgs_7dl_16", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_catacomb_door_fullbright_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
        
screen bgs_7dl_17:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/24"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg int_catacombs_door_light2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_catacombs_door_light2_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("bgs_7dl_17", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_catacombs_door_light2_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg int_catacombs_entrance_light_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_catacombs_entrance_light_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("bgs_7dl_17", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_catacombs_entrance_light_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.154
    if renpy.seen_image("bg int_chief_office_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_chief_office_day_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("bgs_7dl_17", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_chief_office_day_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg int_chief_office_rain_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_chief_office_rain_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("bgs_7dl_17", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_chief_office_rain_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg int_clubs_dj_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_clubs_dj_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("bgs_7dl_17", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_clubs_dj_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg int_clubs_dj_night_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_clubs_dj_night_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide("bgs_7dl_17", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_clubs_dj_night_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
      
screen bgs_7dl_18:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/24"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg int_clubs_dj_night_nolight_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_clubs_dj_night_nolight_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("bgs_7dl_18", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_clubs_dj_night_nolight_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg int_concert_room_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_concert_room_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("bgs_7dl_18", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_concert_room_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.154
    if renpy.seen_image("bg int_d3_hideout_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_d3_hideout_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("bgs_7dl_18", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_d3_hideout_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg int_dinning_hall_people_rain_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_dinning_hall_people_rain_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("bgs_7dl_18", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_dinning_hall_people_rain_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg int_dinning_hall_rain_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_dinning_hall_rain_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("bgs_7dl_18", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_dinning_hall_rain_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg int_editorial_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_editorial_day_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide("bgs_7dl_18", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_editorial_day_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
        
screen bgs_7dl_19:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/24"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg int_epilogue_bg_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_epilogue_bg_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("bgs_7dl_19", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_epilogue_bg_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg int_extra_house_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_extra_house_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("bgs_7dl_19", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_extra_house_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.154
    if renpy.seen_image("bg int_extra_house_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_extra_house_day_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("bgs_7dl_19", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_extra_house_day_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg int_hence_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_hence_day_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("bgs_7dl_19", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_hence_day_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg int_hence_night_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_hence_night_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("bgs_7dl_19", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_hence_night_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg int_home_lift_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_home_lift_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide("bgs_7dl_19", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_home_lift_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
        
screen bgs_7dl_20:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/24"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg int_hospital_hall_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_hospital_hall_day_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("bgs_7dl_20", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_hospital_hall_day_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg int_intro_liaz_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_intro_liaz_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("bgs_7dl_20", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_intro_liaz_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.154
    if renpy.seen_image("bg int_looney_bin_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_looney_bin_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("bgs_7dl_20", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_looney_bin_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg int_looney_bin_nightmare_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_looney_bin_nightmare_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("bgs_7dl_20", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_looney_bin_nightmare_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg int_mine_exit_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_mine_exit_day_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("bgs_7dl_20", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_mine_exit_day_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg int_mine_halt_left_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_mine_halt_left_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide("bgs_7dl_20", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_mine_halt_left_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
        
screen bgs_7dl_21:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/24"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg int_mine_heart_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_mine_heart_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("bgs_7dl_21", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_mine_heart_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg int_mine_room2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_mine_room2_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("bgs_7dl_21", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_mine_room2_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.154
    if renpy.seen_image("bg int_mine_water_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_mine_water_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("bgs_7dl_21", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_mine_water_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg int_mines_halt_spotlight_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_mines_halt_spotlight_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("bgs_7dl_21", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_mines_halt_spotlight_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg int_mt_sam_room_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_mt_sam_room_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("bgs_7dl_21", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_mt_sam_room_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg int_mt_sam_room_away_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_mt_sam_room_away_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide("bgs_7dl_21", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_mt_sam_room_away_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
        
screen bgs_7dl_22:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/24"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg int_mt_sam_room_close_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_mt_sam_room_close_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("bgs_7dl_22", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_mt_sam_room_close_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg int_old_building_day_uvao_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_old_building_day_uvao_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("bgs_7dl_22", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_old_building_day_uvao_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.154
    if renpy.seen_image("bg int_opened_door_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_opened_door_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("bgs_7dl_22", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_opened_door_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg int_plats_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_plats_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("bgs_7dl_22", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_plats_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg int_refinery_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_refinery_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("bgs_7dl_22", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_refinery_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg int_sam_house_clean_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_sam_house_clean_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide("bgs_7dl_22", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_sam_house_clean_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
        
screen bgs_7dl_23:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/24"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg int_sam_room_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_sam_room_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("bgs_7dl_23", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_sam_room_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg int_sleep_hentai_office_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_sleep_hentai_office_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("bgs_7dl_23", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_sleep_hentai_office_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.154
    if renpy.seen_image("bg int_sleep_hentai_office2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_sleep_hentai_office2_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("bgs_7dl_23", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_sleep_hentai_office2_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg int_sporthall_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_sporthall_day_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("bgs_7dl_23", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_sporthall_day_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg int_sporthall_night_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_sporthall_night_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("bgs_7dl_23", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_sporthall_night_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg int_store_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_store_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide("bgs_7dl_23", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_store_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
        
screen bgs_7dl_24:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/24"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg int_toilet_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_toilet_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("bgs_7dl_24", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_toilet_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg int_wardrobe_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_wardrobe_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("bgs_7dl_24", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_wardrobe_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.154
    if renpy.seen_image("bg int_wardrobe2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_wardrobe2_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("bgs_7dl_24", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_wardrobe2_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg int_warehouse_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_warehouse_day_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("bgs_7dl_24", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_warehouse_day_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg int_warehouse_night_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_warehouse_night_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("bgs_7dl_24", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_warehouse_night_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
     
screen art_7dl_1:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/8"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d1_un_book_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d1_un_book_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("art_7dl_1", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d1_un_book_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d2_mi_me_polaroid_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d2_mi_me_polaroid_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("art_7dl_1", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d2_mi_me_polaroid_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.154
    if renpy.seen_image("cg d2_mt_me_resort_afar_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d2_mt_me_resort_afar_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("art_7dl_1", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d2_mt_me_resort_afar_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d2_mt_me_resort_close_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d2_mt_me_resort_close_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("art_7dl_1", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d2_mt_me_resort_close_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d2_un_kissing_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d2_un_kissing_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("art_7dl_1", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d2_un_kissing_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("cg d2_un_knees_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d2_un_knees_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide("art_7dl_1", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d2_un_knees_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
        
screen art_7dl_2:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/8"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d2_us_soccer_sunset_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d2_us_soccer_sunset_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("art_7dl_2", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d2_us_soccer_sunset_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d2_us_trainhop_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d2_us_trainhop_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("art_7dl_2", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d2_us_trainhop_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.154
    if renpy.seen_image("cg d3_dv_alice_dj80_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d3_dv_alice_dj80_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("art_7dl_2", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d3_dv_alice_dj80_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d3_mi_dance_afar_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d3_mi_dance_afar_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("art_7dl_2", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d3_mi_dance_afar_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d3_mi_dance_close_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d3_mi_dance_close_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("art_7dl_2", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d3_mi_dance_close_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("cg d3_sl_bath_unplaited_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d3_sl_bath_unplaited_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide("art_7dl_2", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d3_sl_bath_unplaited_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
       
screen art_7dl_3:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/8"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d4_mi_dj_lib_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d4_mi_dj_lib_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("art_7dl_3", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d4_mi_dj_lib_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d4_mi_dj_lib0_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d4_mi_dj_lib0_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("art_7dl_3", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d4_mi_dj_lib0_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.154
    if renpy.seen_image("cg d4_mi_hedgehod_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d4_mi_hedgehod_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("art_7dl_3", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d4_mi_hedgehod_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d4_us_stardust_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d4_us_stardust_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("art_7dl_3", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d4_us_stardust_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d5_un_carrier_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d5_un_carrier_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("art_7dl_3", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d5_un_carrier_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("cg d5_us_sneakpeak_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d5_us_sneakpeak_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide("art_7dl_3", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d5_us_sneakpeak_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
        
screen art_7dl_4:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/8"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d6_dance_alt_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_dance_alt_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("art_7dl_4", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_dance_alt_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d6_mi_departure_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_mi_departure_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("art_7dl_4", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_mi_departure_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.154
    if renpy.seen_image("cg d6_mi_farewell_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_mi_farewell_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("art_7dl_4", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_mi_farewell_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d6_mi_hugs_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_mi_hugs_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("art_7dl_4", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_mi_hugs_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d6_sl_clean_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_sl_clean_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("art_7dl_4", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_sl_clean_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("cg d6_sl_zettai_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_sl_zettai_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide("art_7dl_4", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_sl_zettai_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
       
screen art_7dl_5:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/8"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d6_un_evening_0_1_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_un_evening_0_1_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("art_7dl_5", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_un_evening_0_1_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d6_un_evening_0_2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_un_evening_0_2_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("art_7dl_5", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_un_evening_0_2_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.154
    if renpy.seen_image("cg d6_un_evening_0_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_un_evening_0_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("art_7dl_5", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_un_evening_0_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d6_un_evening_3_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_un_evening_3_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("art_7dl_5", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_un_evening_3_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d7_bus_night_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_bus_night_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("art_7dl_5", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_bus_night_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("cg d7_dv_addic_happy_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_dv_addic_happy_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide("art_7dl_5", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_dv_addic_happy_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
        
screen art_7dl_6:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/8"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d7_dv_alice_dj_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_dv_alice_dj_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("art_7dl_6", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_dv_alice_dj_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d7_dv_looney_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_dv_looney_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("art_7dl_6", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_dv_looney_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.154
    if renpy.seen_image("cg d7_dv_rf_reject_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_dv_rf_reject_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("art_7dl_6", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_dv_rf_reject_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d7_frozen_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_frozen_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("art_7dl_6", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_frozen_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d7_mi_hugs_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_hugs_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("art_7dl_6", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_hugs_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("cg d7_mi_lost_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_lost_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide("art_7dl_6", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_lost_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
     
screen art_7dl_7:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/8"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d7_mi_ramen_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_ramen_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("art_7dl_7", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_ramen_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d7_mi_reenter_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_reenter_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("art_7dl_7", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_reenter_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.154
    if renpy.seen_image("cg d7_sh_ai_4eva_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_sh_ai_4eva_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("art_7dl_7", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_sh_ai_4eva_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d7_sl_gonna_be_ok_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_sl_gonna_be_ok_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("art_7dl_7", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_sl_gonna_be_ok_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d7_un_epilogue_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_un_epilogue_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("art_7dl_7", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_un_epilogue_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("cg d7_un_epilogue_d1_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_un_epilogue_d1_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide("art_7dl_7", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_un_epilogue_d1_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
     
screen art_7dl_8:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/8"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d7_un_epilogue_d2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_un_epilogue_d2_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide("art_7dl_8", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_un_epilogue_d2_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d7_un_reanimation_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_un_reanimation_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("art_7dl_8", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_un_reanimation_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.154
    if renpy.seen_image("cg d7_us_pixie_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_us_pixie_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("art_7dl_8", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_us_pixie_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
     
screen art_7dl_un_1:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/2"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d1_un_book_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d1_un_book_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide("art_7dl_un_1", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d1_un_book_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d2_un_kissing_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/int_sleep_hentai_office_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide("art_7dl_un_1", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg int_sleep_hentai_office_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.154
    if renpy.seen_image("cg d2_un_knees_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/int_sleep_hentai_office2_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("art_7dl_un_1", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg int_sleep_hentai_office2_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d5_un_carrier_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/int_sporthall_day_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("art_7dl_un_1", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg int_sporthall_day_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d6_un_evening"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/int_sporthall_night_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("art_7dl_un_1", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg int_sporthall_night_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("cg d7_un_epilogue_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_un_epilogue_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide("art_7dl_un_1", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_un_epilogue_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
     
screen art_7dl_un_2:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/2"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d7_un_reanimation_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_un_reanimation_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("art_7dl_un_2", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_un_reanimation_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
        
screen art_7dl_sl_1:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/1"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d3_sl_bath_unplaited_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d3_sl_bath_unplaited_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("art_7dl_sl_1", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d3_sl_bath_unplaited_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d6_sl_clean_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_sl_clean_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("art_7dl_sl_1", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_sl_clean_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.154
    if renpy.seen_image("cg d6_sl_zettai_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_sl_zettai_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("art_7dl_sl_1", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_sl_zettai_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
        
screen art_7dl_dv_1:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/1"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d3_dv_alice_dj"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d3_dv_alice_dj_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("art_7dl_dv_1", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d3_dv_alice_dj"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d7_dv_addic_happy_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_dv_addic_happy_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("art_7dl_dv_1", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_dv_addic_happy_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.154
    if renpy.seen_image("cg d7_dv_looney_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_dv_looney_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("art_7dl_dv_1", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_dv_looney_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d7_dv_rf_reject_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_dv_rf_reject_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("art_7dl_dv_1", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_dv_rf_reject_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
        
screen art_7dl_mi_1:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/2"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d2_mi_me_polaroid_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d2_mi_me_polaroid_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("art_7dl_mi_1", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d2_mi_me_polaroid_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d3_mi_dance_close_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d3_mi_dance_close_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("art_7dl_mi_1", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d3_mi_dance_close_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.154
    if renpy.seen_image("cg d4_mi_dj_lib0_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d4_mi_dj_lib0_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("art_7dl_mi_1", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d4_mi_dj_lib0_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d4_mi_hedgehod_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d4_mi_hedgehod_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("art_7dl_mi_1", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d4_mi_hedgehod_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d6_mi_departure_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_mi_departure_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("art_7dl_mi_1", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_mi_departure_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("cg d6_mi_farewell_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_mi_farewell_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide("art_7dl_mi_1", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_mi_farewell_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
        
screen art_7dl_mi_2:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/2"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d6_mi_hugs_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_mi_hugs_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("art_7dl_mi_2", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_mi_hugs_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d7_mi_hugs_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_hugs_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("art_7dl_mi_2", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_hugs_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.154
    if renpy.seen_image("cg d7_mi_lost_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_lost_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("art_7dl_mi_2", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_lost_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d7_mi_ramen_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_ramen_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("art_7dl_mi_2", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_ramen_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d7_mi_reenter_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_reenter_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("art_7dl_mi_2", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_reenter_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
        
screen art_7dl_us_1:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/1"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d2_us_soccer_sunset_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d2_us_soccer_sunset_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("art_7dl_us_1", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d2_us_soccer_sunset_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d2_us_trainhop_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d2_us_trainhop_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("art_7dl_us_1", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d2_us_trainhop_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.154
    if renpy.seen_image("cg d4_us_stardust_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d4_us_stardust_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("art_7dl_us_1", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d4_us_stardust_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d5_us_sneakpeak_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d5_us_sneakpeak_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("art_7dl_us_1", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d5_us_sneakpeak_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d7_us_pixie_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_us_pixie_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("art_7dl_us_1", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_us_pixie_7dl"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
        
screen art_7dl_mt_1:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/1"
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d2_mt_me_resort"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d2_mt_me_resort_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("art_7dl_mt_1", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d2_mt_me_resort"), Jump("show_image_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
        
screen filter_settings_7dl:
    tag menu
    imagebutton: 
        auto get_image_7dl("gui/gallery/arts/d1_un_book_7dl_%s.png") xalign 0.19 yalign 0.15 
        action [Hide("filter_settings_7dl", transition=Dissolve(0.2)), SetVariable("filter_7dl", "un"), SetVariable("page_7dl", 1), Show("art_7dl_un_1", transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2))] 
    imagebutton:
        auto get_image_7dl("gui/gallery/arts/d3_sl_bath_unplaited_7dl_%s.png") xalign 0.5 yalign 0.15 
        action [Hide("filter_settings_7dl", transition=Dissolve(0.2)), SetVariable("filter_7dl", "sl"), SetVariable("page_7dl", 1), Show("art_7dl_sl_1", transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2))] 
    imagebutton:
        auto get_image_7dl("gui/gallery/arts/d7_dv_addic_happy_7dl_%s.png") xalign 0.8 yalign 0.15 
        action [Hide("filter_settings_7dl", transition=Dissolve(0.2)), SetVariable("filter_7dl", "dv"), SetVariable("page_7dl", 1), Show("art_7dl_dv_1", transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2))] 
    imagebutton:
        auto get_image_7dl("gui/gallery/arts/d6_mi_departure_7dl_%s.png") xalign 0.2 yalign 0.93 
        action [Hide("filter_settings_7dl", transition=Dissolve(0.2)), SetVariable("filter_7dl", "mi"), SetVariable("page_7dl", 1), Show("art_7dl_mi_1", transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2))] 
    imagebutton:
        auto get_image_7dl("gui/gallery/arts/d7_us_pixie_7dl_%s.png") xalign 0.5 yalign 0.93 
        action [Hide("filter_settings_7dl", transition=Dissolve(0.2)), SetVariable("filter_7dl", "us"), SetVariable("page_7dl", 1), Show("art_7dl_us_1", transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2))] 
    imagebutton:
        auto get_image_7dl("gui/gallery/arts/d2_mt_me_resort_afar_7dl_%s.png") xalign 0.8 yalign 0.93 
        action [Hide("filter_settings_7dl", transition=Dissolve(0.2)), SetVariable("filter_7dl", "mt"), SetVariable("page_7dl", 1), Show("art_7dl_mt_1", transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2))] 
    
label alt_gallery_start:
    scene bg gallery_7dl with fade
    play music tellyourworld fadein 3
    call screen gallery_main_7dl       
    
label alt_gallery:
    call screen gallery_main_7dl       

# хз что тут ниже происходит, но работает ¯\_(ツ)_/¯
label show_image_7dl(img_7dl = show_image_7dl):
    $ renpy.scene()
    $ renpy.show(img_7dl)
    $ renpy.with_statement(fade)
    $ renpy.pause()
    jump alt_gallery