label alt_day4_dv_dj_start:
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(4, u"Alice DJ. Утро")
    scene bg int_house_of_mt_sunset
    play music music_list["my_daily_life"]
    #Спецсценарий для романсящих Алиску - диджея либо собирающихся сделать её таковой.
    #Саб-руты: медпункт - вербовка Алису на четвёртый день, медпункт (Алиса-диджей), базис (Алиса-диджей), базис с вербовкой.
    "Заглушка для Алисы-диджея."
    "Поздравляю, вы выбрали Элис диджей-рут! Рут находится в разработке."
    show spill_red with dspr
    $ renpy.pause(2, hard=True)
    show spill_gray with dspr
    $ renpy.pause(2, hard=True)
    show alt_credits timeskip_dev at truecenter with dissolve2
    $ renpy.pause(4, hard=True)
    with dissolve2
    window hide
    return
label alt_day4_dv_7dl2dj_transit:
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(4, u"Alice DJ. День.")
    if alt_day4_dv_7dl_walkman_presented:
        dv "Ты серьёзно? Просто так отдашь?"
        me "А что не так-то?"
        me "Я вижу, тебе нравится этим заниматься, так что если чем-то могу помочь…"
        dv "Удивлена. Честно."
        "Она подошла ко мне и, немного посомневавшись, поцеловала - просто клюнула — в щёку."
        "Не знаю, пыталась ли она за этим нехитрым действием спрятать собственное смущение, делая несвойственные ей решительные поступки, но только смутилась она ещё сильнее."
        "И всё равно, ни прятаться, ни мямлить она больше не собиралась."
        "Видимо, вкусила вчера внимания и поняла, что оно есть хорошо."
        me "Я могу тебе ещё как-нибудь помочь?"
        dv "Нет, я сейчас в радиорубку, буду пробовать собственные силы на поприще ведущего."
        "Она улыбнулась и убежала."
    return