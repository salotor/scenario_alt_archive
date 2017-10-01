label alt_day4_sl_7dl_start:
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(4, u"Славя. 7ДЛ. Утро")
    scene black
    play music music_list["drown"] fadein 3
    window hide
    show spill_red with dspr
    $ renpy.pause(2, hard=True)
    show spill_gray with dspr
    $ renpy.pause(2, hard=True)
    show alt_credits timeskip_dev at truecenter with dissolve2
    $ renpy.pause(4, hard=True)
    with dissolve2
    window hide
    return
    

label alt_day5_sl_7dl_start: # "Так как c Микой всё ещё в разлае, можем выбрать на сл. день - сычевать или мириться со Славей."
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(5, u"Славя. 7ДЛ. Утро")
    scene bg int_house_of_mt_sunset
    play music music_list["my_daily_life"] fadein 5
    "И снова здравствуйте! Пятый день пребывания в лучшем месте обозримой вселенной, пионерлагере «Совёнок», готов к вашему появлению!"
    window hide
    show spill_red with dspr
    $ renpy.pause(2, hard=True)
    show spill_gray with dspr
    $ renpy.pause(2, hard=True)
    show alt_credits timeskip_dev at truecenter with dissolve2
    $ renpy.pause(4, hard=True)
    with dissolve2
    window hide
    return