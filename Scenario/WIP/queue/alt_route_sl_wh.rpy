label alt_day5_sl_wh_start:
    pause(1)
    call alt_day5_sl_wh_vars
    pause(1)
    $ persistent.sprite_time = "sunset"
    $ sunset_time()
    $ alt_chapter(5, u"Ведьма. Утро.")
    scene cg d5_rainy_idle_7dl with dissolve
    play music ambience_safe_7dl fadein 3
    play sound_loop ambience_rain_7dl_7dl
    "Я проснулся от холода и сырости, залезающей, казалось, за шиворот."
    th "Где я?"
    "Я рывком сел и огляделся."
    "Если память мне не изменяет, я был на костровой поляне."
    "Я и сейчас тут лежал, используя одно из бревен в качестве подушки."
    "Начавшийся дождь разбудил меня, а пока я тут головой мотал, успел промокнуть до нитки."
    window hide
    with fade

    "Вчера произошло что-то очень плохое."
    "Очень неправильное."
    "Не просто же так мне пусто на душе?"
    th "Почему мне…"
    th "Ты там?"
    "Молчание."
    th "Эй, моё похотливое альтер-эго, пора вставать, все встали, и ты тоже."
    "Молчание."
    th "Ау?"
    th "Ты… Ты здесь?.."
    "В том месте внутри меня, где последние несколько дней обитал мой язвительный и циничный собеседник, зияла сосущая пустота."
    th "…"
    "Воспоминания хлынули чередой."
    window hide
    scene expression Noir("bg ext_clubs_night")
    show prologue_dream
    with fade

    "Попытки наладить вещание."
    if alt_day4_sl_tut_iz:
        window hide
        scene expression Noir("bg int_attic2_day_7dl")
        show prologue_dream
        with fade
    
        "Звуковая завеса."
    window hide
    scene expression Noir("bg ext_old_building_night")
    show prologue_dream
    with fade

    "Попытки найти Шурика."
    window hide
    scene expression Noir("bg ext_polyana_night")
    show sl happy pioneer at center
    show prologue_dream
    with fade

    "И вчерашнее непонятное, страшное, {i}чёрное{/i}"
    scene bg ext_polyana_night
    show prologue_dream
    "Но миг я снова почувствовал вчерашнюю безумную похоть, это всесокрушающее чувство желания."
    "Но сегодня я уже мог справиться с этим сам."
    "Тем более, что мой внутренний собеседник всё-таки как-то смог помочь, чему-то научить меня."
    "Пусть и ценой собственного существования."
    scene bg ext_polyana_sunset
    show wet1
    with fade
    "Я с кряхтеньем поднялся на ноги."
    "И, прикинув направление, зашагал в сторону лагеря."
    "У меня было несколько неприятных вопросов к одной ведьмочке."
    window hide
    scene cg d5_rainy_idle_7dl with dissolve
    show spill_red with dspr
    $ renpy.pause(2, hard=True)
    show spill_gray with dspr
    $ renpy.pause(2, hard=True)
    show alt_credits timeskip_dev at truecenter with dissolve2
    $ renpy.pause(4, hard=True)
    with dissolve2
    window hide
    return