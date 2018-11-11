init 1:
    $ page_7dl = 1
    $ max_bgs_page_7dl = 9
    $ max_arts_page_7dl = 10
    $ max_un_page_7dl = 2
    $ max_sl_page_7dl = 2
    $ max_dv_page_7dl = 2
    $ max_mi_page_7dl = 3
    $ max_us_page_7dl = 2
    $ max_mt_page_7dl = 1
    
    $ show_image_7dl = ""
    $ show_image2_7dl = ""
    $ show_image3_7dl = ""
    $ show_image4_7dl = ""
    $ gallery_mode_7dl = ""
    
    $ style.page_7dl_text = Style(style.default)
    $ style.page_7dl_text.font  = get_image_7dl("fonts/a_AvanteLtNr.ttf")
    $ style.page_7dl_text.color = "#ffffff"
    $ style.page_7dl_text.size = 60
    
    image bg gallery_7dl = get_image_7dl("gui/gallery/gallery_bg.png")
    image bg gallery_moments_7dl = get_image_7dl("gui/gallery/gallery_moments_bg.png")
    $ locked_img_7dl = ["gallery_stub_1.png", "gallery_stub_2.png", "gallery_stub_3.png"]
        
screen gallery_main_7dl:
    add get_image_7dl("gui/gallery/gallery_bg.png")
    if not gallery_mode_7dl == "bgs":
        imagebutton: 
            auto get_image_7dl("gui/gallery/gallery_navig_bgs_%s.png") xcenter 0.167 ycenter 0.046 
            action [Show("bgs_7dl_1", transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", "bgs"), SetVariable("page_7dl", 1)]
    else:
        imagebutton: 
            auto get_image_7dl("gui/gallery/gallery_navig_bgs_%s.png") xcenter 0.167 ycenter 0.046 
            action NullAction()
    if not (gallery_mode_7dl == "arts" or gallery_mode_7dl == "start"):
        imagebutton: 
            auto get_image_7dl("gui/gallery/gallery_navig_arts_%s.png") xcenter 0.5 ycenter 0.046
            action [Show("arts_7dl_1", transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", "arts"), SetVariable("page_7dl", 1)]
    else:
        imagebutton: 
            auto get_image_7dl("gui/gallery/gallery_navig_arts_%s.png") xcenter 0.5 ycenter 0.046
            action NullAction()
    if not (gallery_mode_7dl == "bgs" or gallery_mode_7dl == "moments"):
        imagebutton: 
            auto get_image_7dl("gui/gallery/gallery_navig_filter_%s.png") xcenter 0.917 ycenter 0.148
            action [Show("filter_settings_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", "filter"), SetVariable("page_7dl", 1)]
    if not gallery_mode_7dl == "moments":
        imagebutton: 
            auto get_image_7dl("gui/gallery/gallery_navig_moments_%s.png") xcenter 0.833 ycenter 0.046
            action Show("alt_wip", transition=Dissolve(0.2))
            # action [Show("replays_route_choice_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", "moments")]
    else:
        imagebutton: 
            auto get_image_7dl("gui/gallery/gallery_navig_moments_%s.png") xcenter 0.833 ycenter 0.046
            action NullAction()
    if gallery_mode_7dl == "start":
        timer 0.01 action [Show("arts_7dl_1", transition=Dissolve(1.0)), Show("gallery_bw_7dl", transition=Dissolve(1.0)), Show("gallery_fw_7dl", transition=Dissolve(1.0)), Show("gallery_exit_7dl", transition=Dissolve(1.0))]
    elif gallery_mode_7dl == "arts":
        timer 0.01 action [Show("arts_7dl_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2)), Show("gallery_exit_7dl", transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "bgs":
        timer 0.01 action [Show("bgs_7dl_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2)), Show("gallery_exit_7dl", transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "moments":
        add "bg gallery_moments_7dl" xcenter 0.503 ycenter 0.532
    elif gallery_mode_7dl == "filter":
        timer 0.01 action [Show("filter_settings_7dl", transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2)), Show("gallery_exit_7dl", transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "un":
        timer 0.01 action [Show("arts_7dl_un_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2)), Show("gallery_exit_7dl", transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "sl":
        timer 0.01 action [Show("arts_7dl_sl_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2)), Show("gallery_exit_7dl", transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "dv":
        timer 0.01 action [Show("arts_7dl_dv_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2)), Show("gallery_exit_7dl", transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "mi":
        timer 0.01 action [Show("arts_7dl_mi_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2)), Show("gallery_exit_7dl", transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "us":
        timer 0.01 action [Show("arts_7dl_us_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2)), Show("gallery_exit_7dl", transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "mt":
        timer 0.01 action [Show("arts_7dl_mt_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2)), Show("gallery_exit_7dl", transition=Dissolve(0.2))]

screen gallery_exit_7dl:
    if gallery_mode_7dl == "bgs":
        imagebutton: 
            auto get_image_7dl("gui/gallery/gallery_navig_exit_%s.png") xalign 0.029 yalign 0.971 
            action [Hide("bgs_7dl_%s" % str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", ""), SetVariable("page_7dl", 1), Jump("main_menu_7dl")]
    elif gallery_mode_7dl == "arts" or gallery_mode_7dl == "start":
        imagebutton: 
            auto get_image_7dl("gui/gallery/gallery_navig_exit_%s.png") xalign 0.029 yalign 0.971 
            action [Hide("arts_7dl_%s" % str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", ""), SetVariable("page_7dl", 1), Jump("main_menu_7dl")]
    elif gallery_mode_7dl == "moments":
        imagebutton: 
            auto get_image_7dl("gui/gallery/gallery_navig_exit_%s.png") xalign 0.029 yalign 0.971 
            action [Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", ""), SetVariable("page_7dl", 1), Hide("replays_common_choice_7dl", transition=Dissolve(0.2)), Hide("replays_un_choice_7dl", transition=Dissolve(0.2)), Hide("replays_sl_choice_7dl", transition=Dissolve(0.2)), Hide("replays_dv_choice_7dl", transition=Dissolve(0.2)), Hide("replays_mi_choice_7dl", transition=Dissolve(0.2)), Show("arts_7dl_1"), Hide("arts_7dl_1"), Jump("main_menu_7dl")]
    elif gallery_mode_7dl == "filter":
        imagebutton: 
            auto get_image_7dl("gui/gallery/gallery_navig_exit_%s.png") xalign 0.029 yalign 0.971 
            action [Hide("filter_settings_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", ""), SetVariable("page_7dl", 1), Jump("main_menu_7dl")]
    elif gallery_mode_7dl == "un":
        imagebutton: 
            auto get_image_7dl("gui/gallery/gallery_navig_exit_%s.png") xalign 0.029 yalign 0.971 
            action [Hide("arts_7dl_un_%s" % str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", ""), SetVariable("page_7dl", 1), Jump("main_menu_7dl")]
    elif gallery_mode_7dl == "sl":
        imagebutton: 
            auto get_image_7dl("gui/gallery/gallery_navig_exit_%s.png") xalign 0.029 yalign 0.971 
            action [Hide("arts_7dl_sl_%s" % str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", ""), SetVariable("page_7dl", 1), Jump("main_menu_7dl")]
    elif gallery_mode_7dl == "dv":
        imagebutton: 
            auto get_image_7dl("gui/gallery/gallery_navig_exit_%s.png") xalign 0.029 yalign 0.971 
            action [Hide("arts_7dl_dv_%s" % str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", ""), SetVariable("page_7dl", 1), Jump("main_menu_7dl")]
    elif gallery_mode_7dl == "mi":
        imagebutton: 
            auto get_image_7dl("gui/gallery/gallery_navig_exit_%s.png") xalign 0.029 yalign 0.971 
            action [Hide("arts_7dl_mi_%s" % str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", ""), SetVariable("page_7dl", 1), Jump("main_menu_7dl")]
    elif gallery_mode_7dl == "us":
        imagebutton: 
            auto get_image_7dl("gui/gallery/gallery_navig_exit_%s.png") xalign 0.029 yalign 0.971 
            action [Hide("arts_7dl_us_%s" % str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", ""), SetVariable("page_7dl", 1), Jump("main_menu_7dl")]
    elif gallery_mode_7dl == "mt":
        imagebutton: 
            auto get_image_7dl("gui/gallery/gallery_navig_exit_%s.png") xalign 0.029 yalign 0.971 
            action [Hide("arts_7dl_mt_%s" % str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", ""), SetVariable("page_7dl", 1), Jump("main_menu_7dl")]
        
screen gallery_bw_7dl:
    if gallery_mode_7dl == "bgs":
        if not renpy.get_screen("bgs_7dl_1"):
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_backward_%s.png") xalign 0.045 yalign 0.5 
                action [SetVariable("page_7dl", page_7dl-1), Hide("bgs_7dl_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("bgs_7dl_%s" % str(page_7dl-1), transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "arts":
        if not renpy.get_screen("arts_7dl_1"):
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_backward_%s.png") xalign 0.045 yalign 0.5 
                action [SetVariable("page_7dl", page_7dl-1), Hide("arts_7dl_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("arts_7dl_%s" % str(page_7dl-1), transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "un":
        if not renpy.get_screen("arts_7dl_un_1"):
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_backward_%s.png") xalign 0.045 yalign 0.5 
                action [SetVariable("page_7dl", page_7dl-1), Hide("arts_7dl_un_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("arts_7dl_un_%s" % str(page_7dl-1), transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "sl":
        if not renpy.get_screen("arts_7dl_sl_1"):
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_backward_%s.png") xalign 0.045 yalign 0.5 
                action [SetVariable("page_7dl", page_7dl-1), Hide("arts_7dl_sl_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("arts_7dl_sl_%s" % str(page_7dl-1), transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "dv":
        if not renpy.get_screen("arts_7dl_dv_1"):
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_backward_%s.png") xalign 0.045 yalign 0.5 
                action [SetVariable("page_7dl", page_7dl-1), Hide("arts_7dl_dv_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("arts_7dl_dv_%s" % str(page_7dl-1), transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "mi":
        if not renpy.get_screen("arts_7dl_mi_1"):
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_backward_%s.png") xalign 0.045 yalign 0.5 
                action [SetVariable("page_7dl", page_7dl-1), Hide("arts_7dl_mi_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("arts_7dl_mi_%s" % str(page_7dl-1), transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "us":
        if not renpy.get_screen("arts_7dl_us_1"):
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_backward_%s.png") xalign 0.045 yalign 0.5 
                action [SetVariable("page_7dl", page_7dl-1), Hide("arts_7dl_us_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("arts_7dl_us_%s" % str(page_7dl-1), transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "mt":
        if not renpy.get_screen("arts_7dl_mt_1"):
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_backward_%s.png") xalign 0.045 yalign 0.5 
                action [SetVariable("page_7dl", page_7dl-1), Hide("arts_7dl_mt_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("arts_7dl_mt_%s" % str(page_7dl-1), transition=Dissolve(0.2))]
     
screen gallery_fw_7dl:
    if gallery_mode_7dl == "start":
        imagebutton:
            auto get_image_7dl("gui/gallery/gallery_navig_forward_%s.png") xalign 0.957 yalign 0.5
            action [SetVariable("page_7dl", 2), SetVariable("gallery_mode_7dl", "arts"), Hide("arts_7dl_1", transition=Dissolve(0.2)), Show("arts_7dl_2", transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "bgs":
        if not renpy.get_screen("bgs_7dl_%s" % str(max_bgs_page_7dl)):
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_forward_%s.png") xalign 0.957 yalign 0.5 
                action [SetVariable("page_7dl", page_7dl+1), Hide("bgs_7dl_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("bgs_7dl_%s" % str(page_7dl+1), transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "arts":
        if not renpy.get_screen("arts_7dl_%s" % str(max_arts_page_7dl)):
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_forward_%s.png") xalign 0.957 yalign 0.5 
                action [SetVariable("page_7dl", page_7dl+1), Hide("arts_7dl_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("arts_7dl_%s" % str(page_7dl+1), transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "un":
        if not renpy.get_screen("arts_7dl_un_%s" % str(max_un_page_7dl)):
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_forward_%s.png") xalign 0.957 yalign 0.5 
                action [SetVariable("page_7dl", page_7dl+1), Hide("arts_7dl_un_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("arts_7dl_un_%s" % str(page_7dl+1), transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "sl":
        if not renpy.get_screen("arts_7dl_sl_%s" % str(max_sl_page_7dl)):
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_forward_%s.png") xalign 0.957 yalign 0.5 
                action [SetVariable("page_7dl", page_7dl+1), Hide("arts_7dl_sl_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("arts_7dl_sl_%s" % str(page_7dl+1), transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "dv":
        if not renpy.get_screen("arts_7dl_dv_%s" % str(max_dv_page_7dl)):
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_forward_%s.png") xalign 0.957 yalign 0.5 
                action [SetVariable("page_7dl", page_7dl+1), Hide("arts_7dl_dv_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("arts_7dl_dv_%s" % str(page_7dl+1), transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "mi":
        if not renpy.get_screen("arts_7dl_mi_%s" % str(max_mi_page_7dl)):
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_forward_%s.png") xalign 0.957 yalign 0.5 
                action [SetVariable("page_7dl", page_7dl+1), Hide("arts_7dl_mi_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("arts_7dl_mi_%s" % str(page_7dl+1), transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "us":
        if not renpy.get_screen("arts_7dl_us_%s" % str(max_us_page_7dl)):
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_forward_%s.png") xalign 0.957 yalign 0.5 
                action [SetVariable("page_7dl", page_7dl+1), Hide("arts_7dl_us_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("arts_7dl_us_%s" % str(page_7dl+1), transition=Dissolve(0.2))]
    elif gallery_mode_7dl == "mt":
        if not renpy.get_screen("arts_7dl_mt_%s" % str(max_mt_page_7dl)):
            imagebutton:
                auto get_image_7dl("gui/gallery/gallery_navig_forward_%s.png") xalign 0.957 yalign 0.5 
                action [SetVariable("page_7dl", page_7dl+1), Hide("arts_7dl_mt_%s" % str(page_7dl), transition=Dissolve(0.2)), Show("arts_7dl_mt_%s" % str(page_7dl+1), transition=Dissolve(0.2))]

screen filter_settings_7dl:
    tag menu
    imagebutton: 
        auto get_image_7dl("gui/gallery/filter/gallery_filter_un_%s.png") xalign 0.19 yalign 0.15
        action [Hide("filter_settings_7dl", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", "un"), SetVariable("page_7dl", 1), Show("arts_7dl_un_1", transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2))]
    imagebutton:
        auto get_image_7dl("gui/gallery/filter/gallery_filter_sl_%s.png") xalign 0.5 yalign 0.15 
        action [Hide("filter_settings_7dl", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", "sl"), SetVariable("page_7dl", 1), Show("arts_7dl_sl_1", transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2))] 
    imagebutton:
        auto get_image_7dl("gui/gallery/filter/gallery_filter_dv_%s.png") xalign 0.8 yalign 0.15 
        action [Hide("filter_settings_7dl", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", "dv"), SetVariable("page_7dl", 1), Show("arts_7dl_dv_1", transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2))] 
    imagebutton:
        auto get_image_7dl("gui/gallery/filter/gallery_filter_mi_%s.png") xalign 0.2 yalign 0.93
        action [Hide("filter_settings_7dl", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", "mi"), SetVariable("page_7dl", 1), Show("arts_7dl_mi_1", transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2))] 
    imagebutton:
        auto get_image_7dl("gui/gallery/filter/gallery_filter_us_%s.png") xalign 0.5 yalign 0.93 
        action [Hide("filter_settings_7dl", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", "us"), SetVariable("page_7dl", 1), Show("arts_7dl_us_1", transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2))] 
    imagebutton:
        auto get_image_7dl("gui/gallery/filter/gallery_filter_mt_%s.png") xalign 0.8 yalign 0.93 
        action [Hide("filter_settings_7dl", transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", "mt"), SetVariable("page_7dl", 1), Show("arts_7dl_mt_1", transition=Dissolve(0.2)), Show("gallery_bw_7dl", transition=Dissolve(0.2)), Show("gallery_fw_7dl", transition=Dissolve(0.2))] 
                    
screen bgs_7dl_1:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_bgs_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg ext_adductius_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_adductius_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_adductius_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg ext_backdoor_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_backdoor_day_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_backdoor_day_7dl"), SetVariable("show_image2_7dl", "bg ext_backdoor_night_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("bg ext_backroad_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_backroad_day_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_backroad_day_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg ext_boathouse_alt_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_boathouse_alt_day_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_boathouse_alt_day_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg ext_busstop_dust_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_busstop_dust_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_busstop_dust_7dl"), SetVariable("show_image2_7dl", "bg ext_busstop_sun_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg ext_city_night_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_city_night_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_city_night_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

screen bgs_7dl_2:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_bgs_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg ext_entrance_night_clear_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_entrance_night_clear_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_entrance_night_clear_7dl"), SetVariable("show_image2_7dl", "bg ext_entrance_night_clear_closed_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg ext_lake_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_lake_day_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_lake_day_7dl"), SetVariable("show_image2_7dl", "bg ext_lake_night_7dl"), SetVariable("show_image3_7dl", "bg ext_lake_sunset_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("bg ext_mv2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_mv2_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_mv2_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg ext_railbridge_sunset_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_railbridge_sunset_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_railbridge_sunset_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg ext_sandpit_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_sandpit_day_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_sandpit_day_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg ext_shower_night_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_shower_night_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_shower_night_7dl"), SetVariable("show_image2_7dl", "bg ext_shower_day_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
       
screen bgs_7dl_3:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_bgs_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg ext_tennis_court_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_tennis_court_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_tennis_court_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg ext_townscape_ph_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_townscape_ph_day_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_townscape_ph_day_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("bg ext_un_hideout_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_un_hideout_day_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_un_hideout_day_7dl"), SetVariable("show_image2_7dl", "bg ext_un_hideout_night_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg ext_volley_court_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_volley_court_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_volley_court_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg int_access2_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_access2_day_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_access2_day_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg int_attic_ladder_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_attic_ladder_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_attic_ladder_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
        
screen bgs_7dl_4:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_bgs_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg int_chief_office_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_chief_office_day_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_chief_office_day_7dl"), SetVariable("show_image2_7dl", "bg int_chief_office_rain_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg int_editorial_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_editorial_day_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_editorial_day_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("bg int_home_lift_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_home_lift_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_home_lift_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg int_mt_sam_room_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_mt_sam_room_7dl_%s.png")xalign 0.2 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_mt_sam_room_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg int_mt_sam_room_away_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_mt_sam_room_away_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_mt_sam_room_away_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg int_mt_sam_room_close_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_mt_sam_room_close_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_mt_sam_room_close_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
       
screen bgs_7dl_5:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_bgs_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg int_hospital_hall_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_hospital_hall_day_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_hospital_hall_day_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg int_potato_storage_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_potato_storage_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_potato_storage_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("bg int_sporthall_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_sporthall_day_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_sporthall_day_7dl"), SetVariable("show_image2_7dl", "bg int_sporthall_night_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg int_store_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_store_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_store_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg int_train_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_train_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_train_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg int_wardrobe_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_wardrobe_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_wardrobe_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
        
screen bgs_7dl_6:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_bgs_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg int_wardrobe2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_wardrobe2_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_wardrobe2_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg int_warehouse_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_warehouse_day_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_warehouse_day_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("bg int_warehouse_night_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_warehouse_night_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_warehouse_night_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg ext_graveyard_rain_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_graveyard_rain_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_graveyard_rain_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg ext_khruschevka_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_khruschevka_day_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_khruschevka_day_7dl"), SetVariable("show_image2_7dl", "bg ext_khruschevka_night_7dl"), SetVariable("show_image3_7dl", "bg ext_khruschevka_rain_7dl"), SetVariable("show_image4_7dl", "bg ext_khruschevka_sunset_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg ext_winter_night_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_winter_night_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_winter_night_7dl"), SetVariable("show_image2_7dl", "bg ext_winter_night_rotate_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
        
screen bgs_7dl_7:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_bgs_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg ext_winterpark_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_winterpark_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_winterpark_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg int_excalator_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_excalator_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_excalator_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("bg int_excalator2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_excalator2_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_excalator2_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg int_refinery_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_refinery_day_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_refinery_day_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg int_toilet_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_toilet_day_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_toilet_day_7dl"), SetVariable("show_image2_7dl", "bg int_toilet_night_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg ext_countryside_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_countryside_day_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_countryside_day_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
        
screen bgs_7dl_8:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_bgs_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg ext_dining_hall_backroad_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_dining_hall_backroad_day_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_dining_hall_backroad_day_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg ext_dv_hideout_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_dv_hideout_day_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_dv_hideout_day_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("bg ext_square_rain_genda_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_square_rain_genda_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_square_rain_genda_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("bg ext_warehouse_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_warehouse_day_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_warehouse_day_7dl"), SetVariable("show_image2_7dl", "bg ext_warehouse_night_7dl"), SetVariable("show_image3_7dl", "bg ext_warehouse_sunset_7dl"), SetVariable("show_image4_7dl", "bg ext_warehouse_rain_day_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("bg ext_warehouse2_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/ext_warehouse2_day_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ext_warehouse2_day_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("bg int_coupe_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_coupe_day_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_coupe_day_7dl"), SetVariable("show_image2_7dl", "bg int_coupe_night_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
        
screen bgs_7dl_9:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_bgs_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("bg int_d3_hideout_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_d3_hideout_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_d3_hideout_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("bg int_wagon_day_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/bgs/int_wagon_day_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg int_wagon_day_7dl"), SetVariable("show_image2_7dl", "bg int_wagon_sunset_7dl"), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15

screen arts_7dl_1:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_arts_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d1_un_book_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d1_un_book_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", "arts"), SetVariable("show_image_7dl", "cg d1_un_book_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15 
    if renpy.seen_image("cg d2_mi_me_polaroid_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d2_mi_me_polaroid_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", "arts"), SetVariable("show_image_7dl", "cg d2_mi_me_polaroid_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15 
    if renpy.seen_image("cg d2_mt_me_resort_afar_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d2_mt_me_resort_afar_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", "arts"), SetVariable("show_image_7dl", "cg d2_mt_me_resort_afar_7dl"), SetVariable("show_image2_7dl", "cg d2_mt_me_resort_close_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15 
    if renpy.seen_image("cg d2_un_kissing_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d2_un_kissing_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", "arts"), SetVariable("show_image_7dl", "cg d2_un_kissing_7dl"), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93 
    if renpy.seen_image("cg d2_un_knees_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d2_un_knees_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", "arts"), SetVariable("show_image_7dl", "cg d2_un_knees_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93 
    if renpy.seen_image("cg d2_us_soccer_sunset_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d2_us_soccer_sunset_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("gallery_mode_7dl", "arts"), SetVariable("show_image_7dl", "cg d2_us_soccer_sunset_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93 
        
screen arts_7dl_2:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_arts_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d2_us_trainhop_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d2_us_trainhop_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d2_us_trainhop_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15 
    if renpy.seen_image("cg d3_mi_dance_afar_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d3_mi_dance_afar_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d3_mi_dance_afar_7dl"), SetVariable("show_image2_7dl", "cg d3_mi_dance_afar_bordo_7dl"), SetVariable("show_image3_7dl", "cg d3_mi_dance_close_7dl"), SetVariable("show_image4_7dl", "cg d3_mi_dance_close_bordo_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15 
    if persistent.hentai_graphics_7dl and renpy.seen_image("cg d3_sl_bath_unplaited_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d3_sl_bath_unplaited_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d3_sl_bath_unplaited_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15 
    if renpy.seen_image("cg d4_mi_dj_lib_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d4_mi_dj_lib_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d4_mi_dj_lib_7dl"), SetVariable("show_image2_7dl", "cg d4_mi_dj_lib0_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93 
    if renpy.seen_image("cg d4_mi_hedgehod_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d4_mi_hedgehod_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d4_mi_hedgehod_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93 
    if renpy.seen_image("cg d4_us_stardust_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d4_us_stardust_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d4_us_stardust_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93 
       
screen arts_7dl_3:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_arts_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d5_un_carrier_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d5_un_carrier_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d5_un_carrier_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15 
    if renpy.seen_image("cg d5_us_rendezvous_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d5_us_rendezvous_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d5_us_rendezvous_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15 
    if renpy.seen_image("cg d5_us_sneakpeak_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d5_us_sneakpeak_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d5_us_sneakpeak_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15 
    if renpy.seen_image("cg d6_dance_alt_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_dance_alt_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_dance_alt_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93 
    if renpy.seen_image("cg d6_mi_departure_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_mi_departure_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_mi_departure_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93 
    if renpy.seen_image("cg d6_mi_farewell_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_mi_farewell_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_mi_farewell_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93 
        
screen arts_7dl_4:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_arts_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d6_mi_hugs_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_mi_hugs_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_mi_hugs_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15 
    if renpy.seen_image("cg d6_sl_clean_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_sl_clean_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_sl_clean_7dl"), SetVariable("show_image2_7dl", "cg d6_sl_clean_dress_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15 
    if renpy.seen_image("cg d6_sl_zettai_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_sl_zettai_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_sl_zettai_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15 
    if renpy.seen_image("cg d6_un_evening_0_1_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_un_evening_0_1_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_un_evening_0_1_7dl"), SetVariable("show_image2_7dl", "cg d6_un_evening_0_2_7dl"), SetVariable("show_image3_7dl", "cg d6_un_evening_0_7dl"), SetVariable("show_image4_7dl", "cg d6_un_evening_3_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93 
    if renpy.seen_image("cg d7_dv_addic_happy_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_dv_addic_happy_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_dv_addic_happy_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93 
    if renpy.seen_image("cg d7_dv_alice_dj_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_dv_alice_dj_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_dv_alice_dj_7dl"), SetVariable("show_image2_7dl", "cg d3_dv_alice_dj80_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
       
screen arts_7dl_5:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_arts_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d7_dv_looney_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_dv_looney_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_dv_looney_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15 
    if renpy.seen_image("cg d7_dv_rf_reject_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_dv_rf_reject_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_dv_rf_reject_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15 
    if renpy.seen_image("cg d7_frozen_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_frozen_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_frozen_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15 
    if renpy.seen_image("cg d7_mi_ghost_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_ghost_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_ghost_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93 
    if renpy.seen_image("cg d7_mi_hugs_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_hugs_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_hugs_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93 
    if renpy.seen_image("cg d7_mi_lost_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_lost_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_lost_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93 
     
screen arts_7dl_6:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_arts_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d7_mi_ramen_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_ramen_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_ramen_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15 
    if renpy.seen_image("cg d7_mi_reenter_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_reenter_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_reenter_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15 
    if renpy.seen_image("cg d7_sh_ai_4eva_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_sh_ai_4eva_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_sh_ai_4eva_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15 
    if renpy.seen_image("cg d7_sl_gonna_be_ok_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_sl_gonna_be_ok_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_sl_gonna_be_ok_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93 
    if renpy.seen_image("cg d7_un_epilogue_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_un_epilogue_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_un_epilogue_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93 
    if renpy.seen_image("cg d7_un_epilogue_d1_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_un_epilogue_d1_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_un_epilogue_d1_7dl"), SetVariable("show_image2_7dl", "cg d7_un_epilogue_d2_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93 
     
screen arts_7dl_7:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_arts_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d7_un_reanimation_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_un_reanimation_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_un_reanimation_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15 
    if renpy.seen_image("cg d7_us_pixie_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_us_pixie_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_us_pixie_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15 
    if renpy.seen_image("cg d4_cs_car_day_ba_gl_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d4_cs_car_day_ba_gl_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d4_cs_car_day_ba_gl_7dl"), SetVariable("show_image2_7dl", "cg d4_cs_car_day_cs_7dl"), SetVariable("show_image3_7dl", "cg d4_cs_car_day_7dl"), SetVariable("show_image4_7dl", "cg d4_cs_car_open_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15 
    if renpy.seen_image("cg d4_sl_lookup_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d4_sl_lookup_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d4_sl_lookup_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93 
    if renpy.seen_image("cg d4_sl_phone_ring_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d4_sl_phone_ring_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d4_sl_phone_ring_7dl"), SetVariable("show_image2_7dl", "cg d4_sl_phone_up_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93 
    if renpy.seen_image("cg d5_sl_hugs_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d5_sl_hugs_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d5_sl_hugs_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93 
        
screen arts_7dl_8:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_arts_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d5_sl_snark_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d5_sl_snark_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d5_sl_snark_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15 
    if persistent.hentai_graphics_7dl and renpy.seen_image("cg d6_dv_hentai_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_dv_hentai_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_dv_hentai_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15 
    if persistent.hentai_graphics_7dl and renpy.seen_image("cg d6_dv_hentai2_7dl"):    # renpy не засчитывает это cg увиденным
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_dv_hentai2_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_dv_hentai2_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15 
    if renpy.seen_image("cg d6_sl_bag_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_sl_bag_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_sl_bag_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93 
    if renpy.seen_image("cg d6_us_dance_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_us_dance_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_us_dance_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93 
    if renpy.seen_image("cg d5_sl_square_us_lead_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d5_sl_square_us_lead_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d5_sl_square_us_lead_7dl"), SetVariable("show_image2_7dl", "cg d5_sl_square_sl_lead_7dl"), SetVariable("show_image3_7dl", "cg d5_sl_square_me_lead_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93 
        
screen arts_7dl_9:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_arts_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d1_mi_bus_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d1_mi_bus_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d1_mi_bus_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15 
    if renpy.seen_image("cg d1_mi_dv_bus_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d1_mi_dv_bus_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d1_mi_dv_bus_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15 
    if renpy.seen_image("cg d7_dv_epilogue_bus_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_dv_epilogue_bus_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_dv_epilogue_bus_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15 
    if renpy.seen_image("cg d7_me_epilogue_bus_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_me_epilogue_bus_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_me_epilogue_bus_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93 
    if renpy.seen_image("cg d7_mi_club27_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_club27_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_club27_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93 
    if renpy.seen_image("cg d7_mi_epilogue_bus_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_epilogue_bus_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_epilogue_bus_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93 

screen arts_7dl_10:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_arts_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d7_mt_epilogue_bus_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mt_epilogue_bus_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mt_epilogue_bus_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15 
    if renpy.seen_image("cg d7_sl_epilogue_bus_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_sl_epilogue_bus_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_sl_epilogue_bus_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15 
    if renpy.seen_image("cg d7_un_epilogue_bus_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_un_epilogue_bus_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_un_epilogue_bus_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15 
    if renpy.seen_image("cg d7_us_epilogue_bus_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_us_epilogue_bus_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_us_epilogue_bus_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93        
        
screen arts_7dl_un_1:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_un_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d1_un_book_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d1_un_book_7dl_%s.png") xalign 0.19 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d1_un_book_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d2_un_kissing_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d2_un_kissing_7dl_%s.png") xalign 0.5 yalign 0.15
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d2_un_kissing_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("cg d2_un_knees_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d2_un_knees_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d2_un_knees_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d5_un_carrier_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d5_un_carrier_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d5_un_carrier_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d6_un_evening_0_1_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_un_evening_0_1_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_un_evening_0_1_7dl"), SetVariable("show_image2_7dl", "cg d6_un_evening_0_2_7dl"), SetVariable("show_image3_7dl", "cg d6_un_evening_0_7dl"), SetVariable("show_image4_7dl", "cg d6_un_evening_3_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("cg d7_un_epilogue_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_un_epilogue_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_un_epilogue_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
     
screen arts_7dl_un_2:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_un_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d7_un_reanimation_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_un_reanimation_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_un_reanimation_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d7_un_epilogue_bus_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_un_epilogue_bus_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_un_epilogue_bus_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15        
        
screen arts_7dl_sl_1:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_sl_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if persistent.hentai_graphics_7dl and renpy.seen_image("cg d3_sl_bath_unplaited_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d3_sl_bath_unplaited_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d3_sl_bath_unplaited_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d6_sl_clean_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_sl_clean_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_sl_clean_7dl"), SetVariable("show_image2_7dl", "cg d6_sl_clean_dress_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("cg d6_sl_zettai_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_sl_zettai_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_sl_zettai_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d4_sl_lookup_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d4_sl_lookup_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d4_sl_lookup_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d5_sl_hugs_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d5_sl_hugs_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d5_sl_hugs_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("cg d6_sl_bag_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_sl_bag_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_sl_bag_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
        
screen arts_7dl_sl_2:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_sl_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d7_sl_epilogue_bus_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_sl_epilogue_bus_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_sl_epilogue_bus_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15        
        
screen arts_7dl_dv_1:
    tag menu
    $ next_page_7dl = str(page_7dl) + "/" + str(max_dv_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d7_dv_addic_happy_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_dv_addic_happy_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_dv_addic_happy_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d7_dv_alice_dj_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_dv_alice_dj_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_dv_alice_dj_7dl"), SetVariable("show_image2_7dl", "cg d3_dv_alice_dj80_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("cg d7_dv_looney_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_dv_looney_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_dv_looney_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d7_dv_rf_reject_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_dv_rf_reject_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_dv_rf_reject_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if persistent.hentai_graphics_7dl and renpy.seen_image("cg d6_dv_hentai_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_dv_hentai_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_dv_hentai_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if persistent.hentai_graphics_7dl and renpy.seen_image("cg d6_dv_hentai2_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_dv_hentai2_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_dv_hentai2_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
        
screen arts_7dl_dv_2:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_dv_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d1_mi_dv_bus_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d1_mi_dv_bus_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d1_mi_dv_bus_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d7_dv_epilogue_bus_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_dv_epilogue_bus_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_dv_epilogue_bus_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
        
screen arts_7dl_mi_1:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_mi_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d2_mi_me_polaroid_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d2_mi_me_polaroid_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d2_mi_me_polaroid_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d3_mi_dance_afar_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d3_mi_dance_afar_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d3_mi_dance_afar_7dl"), SetVariable("show_image_7dl", "cg d3_mi_dance_afar_bordo_7dl"), SetVariable("show_image_7dl", "cg d3_mi_dance_close_7dl"), SetVariable("show_image4_7dl", "cg d3_mi_dance_close_bordo_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("cg d4_mi_dj_lib_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d4_mi_dj_lib_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d4_mi_dj_lib_7dl"), SetVariable("show_image2_7dl", "cg d4_mi_dj_lib0_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d4_mi_hedgehod_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d4_mi_hedgehod_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d4_mi_hedgehod_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d6_mi_departure_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_mi_departure_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_mi_departure_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("cg d6_mi_farewell_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_mi_farewell_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_mi_farewell_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
        
screen arts_7dl_mi_2:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_mi_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d6_mi_hugs_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_mi_hugs_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_mi_hugs_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d7_mi_ghost_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_ghost_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_ghost_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("cg d7_mi_hugs_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_hugs_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_hugs_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d7_mi_lost_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_lost_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_lost_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d7_mi_ramen_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_ramen_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_ramen_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("cg d7_mi_reenter_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_reenter_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_reenter_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
        
screen arts_7dl_mi_3:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_mi_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d1_mi_bus_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d1_mi_bus_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d1_mi_bus_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d1_mi_dv_bus_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d1_mi_dv_bus_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d1_mi_dv_bus_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("cg d7_mi_club27_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_club27_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_club27_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d7_mi_epilogue_bus_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mi_epilogue_bus_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mi_epilogue_bus_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
        
screen arts_7dl_us_1:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_us_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d2_us_soccer_sunset_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d2_us_soccer_sunset_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d2_us_soccer_sunset_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d2_us_trainhop_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d2_us_trainhop_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d2_us_trainhop_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    if renpy.seen_image("cg d4_us_stardust_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d4_us_stardust_7dl_%s.png") xalign 0.8 yalign 0.15 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d4_us_stardust_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    if renpy.seen_image("cg d5_us_sneakpeak_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d5_us_sneakpeak_7dl_%s.png") xalign 0.2 yalign 0.93 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d5_us_sneakpeak_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    if renpy.seen_image("cg d7_us_pixie_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_us_pixie_7dl_%s.png") xalign 0.5 yalign 0.93 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_us_pixie_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    if renpy.seen_image("cg d6_us_dance_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d6_us_dance_7dl_%s.png") xalign 0.8 yalign 0.93 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d6_us_dance_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
        
screen arts_7dl_us_2:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_us_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d5_us_rendezvous_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d5_us_rendezvous_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d5_us_rendezvous_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    if renpy.seen_image("cg d7_us_epilogue_bus_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_us_epilogue_bus_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_us_epilogue_bus_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
        
screen arts_7dl_mt_1:
    tag menu
    $ next_page_7dl = str(page_7dl)  + "/" + str(max_mt_page_7dl)
    textbutton next_page_7dl:
        text_style "page_7dl_text"
        style "page_7dl_text"
        xalign 0.95
        yalign 0.95
    if renpy.seen_image("cg d2_mt_me_resort_afar_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d2_mt_me_resort_afar_7dl_%s.png") xalign 0.19 yalign 0.15 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d2_mt_me_resort_afar_7dl"), SetVariable("show_image2_7dl", "cg d2_mt_me_resort_close_7dl"), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
        
    if renpy.seen_image("cg d7_mt_epilogue_bus_7dl"):
        imagebutton:
            auto get_image_7dl("gui/gallery/arts/d7_mt_epilogue_bus_7dl_%s.png") xalign 0.5 yalign 0.15 
            action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg d7_mt_epilogue_bus_7dl"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")] 
    else:
        add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15        
        
label alt_gallery_start:
    play music music_7dl["more_than_alive"] fadein 3
    scene bg gallery_7dl with fade
    $ gallery_mode_7dl = "start"
    $ renpy.block_rollback()
    call screen gallery_main_7dl       
    
label alt_gallery:
    $ renpy.block_rollback()
    call screen gallery_main_7dl       

label show_img_7dl:
    $ renpy.scene()
    if show_image_7dl == "cg d7_dv_rf_reject_7dl":
        $ renpy.show(show_image_7dl, at_list=[bottotop])
    elif show_image_7dl == "cg d7_mi_ghost_7dl":
        $ renpy.show(show_image_7dl, at_list=[bottotop])
    elif show_image_7dl == "cg d7_mi_hugs_7dl":
        $ renpy.show(show_image_7dl, at_list=[bottotop])
    else:
        $ renpy.show(show_image_7dl)
    $ renpy.with_statement(fade)
    $ renpy.pause()
    $ show_image_7dl = ""
    if show_image2_7dl:
        $ renpy.scene()
        $ renpy.show(show_image2_7dl)
        $ renpy.with_statement(fade)
        $ renpy.pause()
        $ show_image2_7dl = ""
    if show_image3_7dl:
        $ renpy.scene()
        $ renpy.show(show_image3_7dl)
        $ renpy.with_statement(fade)
        $ renpy.pause()
        $ show_image3_7dl = ""
    if show_image4_7dl:
        $ renpy.scene()
        $ renpy.show(show_image4_7dl)
        $ renpy.with_statement(fade)
        $ renpy.pause()
        $ show_image4_7dl = ""
    $ renpy.show("bg black")
    jump alt_gallery
    
# screen bgs_7dl_x: # x - pagenum
    # tag menu
    # $ next_page_7dl = str(page_7dl)  + "/" + str(max_bgs_page_7dl)
    # textbutton next_page_7dl:
        # text_style "page_7dl_text"
        # style "page_7dl_text"
        # xalign 0.95
        # yalign 0.95
    # if renpy.seen_image("bg ctrlv1"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/bgs/ctrlv1_%s.png") xalign 0.19 yalign 0.15 
            # action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ctrlv1"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")] 
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    # if renpy.seen_image("bg ctrlv2"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/bgs/ctrlv2_%s.png") xalign 0.5 yalign 0.15 
            # action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ctrlv2"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")] 
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    # if renpy.seen_image("bg ctrlv3"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/bgs/ctrlv3_%s.png") xalign 0.8 yalign 0.15 
            # action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ctrlv3"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")] 
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    # if renpy.seen_image("bg ctrlv4"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/bgs/ctrlv4_%s.png") xalign 0.2 yalign 0.93 
            # action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ctrlv4"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")] 
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    # if renpy.seen_image("bg ctrlv5"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/bgs/ctrlv5_%s.png") xalign 0.5 yalign 0.93 
            # action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ctrlv5"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")] 
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    # if renpy.seen_image("bg ctrlv6"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/bgs/ctrlv6_%s.png") xalign 0.8 yalign 0.93 
            # action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "bg ctrlv6"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")] 
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93

# screen arts_7dl_x: # x - pagenum
    # tag menu
    # $ next_page_7dl = str(page_7dl)  + "/" + str(max_arts_page_7dl)
    # textbutton next_page_7dl:
        # text_style "page_7dl_text"
        # style "page_7dl_text"
        # xalign 0.95
        # yalign 0.95
    # if renpy.seen_image("cg ctrlv1"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/arts/ctrlv1_%s.png") xalign 0.19 yalign 0.15 
            # action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg ctrlv1"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")] 
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15 
    # if renpy.seen_image("cg ctrlv2"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/arts/ctrlv2_%s.png") xalign 0.5 yalign 0.15 
            # action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg ctrlv2"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")] 
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15 
    # if renpy.seen_image("cg ctrlv3"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/arts/ctrlv3_%s.png") xalign 0.8 yalign 0.15 
            # action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg ctrlv3"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")] 
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15 
    # if renpy.seen_image("cg ctrlv4"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/arts/ctrlv4_%s.png") xalign 0.2 yalign 0.93 
            # action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg ctrlv4"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")]
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93 
    # if renpy.seen_image("cg ctrlv5"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/arts/ctrlv5_%s.png") xalign 0.5 yalign 0.93 
            # action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg ctrlv5"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")] 
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93 
    # if renpy.seen_image("cg ctrlv6"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/arts/ctrlv6_%s.png") xalign 0.8 yalign 0.93 
            # action [Hide(gallery_mode_7dl + "_7dl_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg ctrlv6"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")] 
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93 

# screen arts_7dl_xx_x: #xx - girlname, x - pagenum
    # tag menu
    # $ next_page_7dl = str(page_7dl)  + "/" + str(max_xx_page_7dl)
    # textbutton next_page_7dl:
        # text_style "page_7dl_text"
        # style "page_7dl_text"
        # xalign 0.95
        # yalign 0.95
    # if renpy.seen_image("cg ctrlv1"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/arts/ctrlv1_%s.png") xalign 0.19 yalign 0.15 
            # action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg ctrlv1"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")] 
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.19 yalign 0.15
    # if renpy.seen_image("cg ctrlv2"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/arts/ctrlv2_%s.png") xalign 0.5 yalign 0.15 
            # action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg ctrlv2"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")] 
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.15
    # if renpy.seen_image("cg ctrlv3"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/arts/ctrlv3_%s.png") xalign 0.8 yalign 0.15 
            # action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg ctrlv3"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")] 
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.15
    # if renpy.seen_image("cg ctrlv4"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/arts/ctrlv4_%s.png") xalign 0.2 yalign 0.93 
            # action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg ctrlv4"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")] 
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.2 yalign 0.93
    # if renpy.seen_image("cg ctrlv5"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/arts/ctrlv5_%s.png") xalign 0.5 yalign 0.93 
            # action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg ctrlv5"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")] 
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.5 yalign 0.93
    # if renpy.seen_image("cg ctrlv6"):
        # imagebutton:
            # auto get_image_7dl("gui/gallery/arts/ctrlv6_%s.png") xalign 0.8 yalign 0.93 
            # action [Hide("arts_7dl_" + gallery_mode_7dl + "_" + str(page_7dl), transition=Dissolve(0.2)), Hide("gallery_bw_7dl", transition=Dissolve(0.2)), Hide("gallery_fw_7dl", transition=Dissolve(0.2)), Hide("gallery_exit_7dl", transition=Dissolve(0.2)), SetVariable("show_image_7dl", "cg ctrlv6"), SetVariable("show_image2_7dl", ""), SetVariable("show_image3_7dl", ""), SetVariable("show_image4_7dl", ""), Jump("show_img_7dl")] 
    # else:
        # add get_image_7dl("gui/gallery/locked_img/" + renpy.random.choice(locked_img_7dl)) xalign 0.8 yalign 0.93
        