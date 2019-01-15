# ***********************************************************************************************
#                                           НЕ ЗАБЫТЬ !!!!
# ***********************************************************************************************
#                          переменные турнира по другим дням (временное согласование — в конце)
# alt_route_common
# — строки 14532, 14537, 15024, 15175: 
#   alt_pe == 1                             >>   alt_my_rival_1_tour.take == 'un'                — Соперник в 1 туре — Лена
#
# — строка 15026:
#   alt_day2_hf2 == 1                       >>   alt_day2_gamblers_result['un'] in [2,11]        — Лена, как минимум, добралась до полуфинала 
#
# — строка 16530:
#   alt_day2_hf2 == 5 & alt_day2_round3 != 0 >>   alt_my_rival_semifinal.take == 'us'             — Ульяна — соперник в полуфинале + Сэм выиграл
#                                               + alt_day2_gamblers_result['me'] >= 21
# — строки 12461, 12475, 12499:
#   alt_day2_f1 == 5 & alt_day2_round3 == 1 >>   alt_day2_gamblers_result['us'] == 22            — Ульяна выиграла турнир
#
# — строка 12488:
#   alt_day2_f1 == 4                        >>   alt_day2_gamblers_result['mi'] >= 21            — Мику вышла в финал
#
# — строка 15029:
#   alt_day2_f1 == 1                        >>   alt_day2_gamblers_result['un'] >= 21            — Лена, как минимум, вышла в финал
#
# — строка 26152:
#   alt_day2_round3 != 0 & alt_day2_f1 == 1 >>   alt_day2_gamblers_result['un'] >= 21            — Лена, как минимум, вышла в финал
#   при изменённом турнире в этом выражении alt_day2_round3 != 0 — не нужно. Сэм турнир смотрит до конца.
#
# — строки 12558, 13464, 12980:
#   alt_day2_round3 == 2                    >>   alt_day2_gamblers_result['me'] == 22            — Семён выиграл турнир
#
# — строка 12578:
#   ((alt_day2_round1 == 1) or (alt_day2_round2 == 1)) >> alt_day2_gamblers_result['me'] < 12    — Семён проиграл в 1 или 2 туре
#
# — строка 14532:                                   (с учётом, что соперник — Лена)
#   alt_day2_round1 == 1                    >>  alt_day2_gamblers_result['me'] == 1              — Семён проиграл в 1 туре
#       
# — строка 14537:                                   (с учётом, что соперник — Лена)
#   alt_day2_round2 != 1                    >>  alt_day2_gamblers_result['me'] >= 2              — Семён как минимум, выиграл в 1 туре
#
# — строки 15024, 15175:                            (с учётом, что соперник — Лена)
#   alt_day2_fail == 1                      >>   alt_day2_gamblers_result['un'] > 2              — Семён проиграл в 1 туре Лене БЕЗ РЕВАНША
#       
# — строки 12980, 13461, 15388, 15396, 19998: 
#   alt_day2_dv_bet_won == 2 — нигде не присваивается, предположительно — она прошла дальше в турнире
#   alt_day2_dv_bet_won == 2               >>    alt_day2_gamblers_result['me'] < alt_day2_gamblers_result['dv'] 
#                                                or alt_day2_gamblers_result['me'] == 1             — Алиса с Семеном наравне или прошла дальше
#
# alt_route_sl_cl
# — строка 14315:
#   alt_day2_f1 == 4 & alt_day2_round3 == 1 >>   alt_my_rival_final.take == 'mi'                    — Мику — соперник в финале + Сэм выиграл
#                                              + alt_day2_gamblers_result['me'] == 22
#
# alt_route_mi_cl
# — строка 248:
#   alt_day2_fail != 1                      >>  alt_day2_gamblers_result['me'] > 1                  — по крайней мере, Семён не проиграл в 1 туре
#
# — строка 859:
#   alt_day2_round3 == 2                    >>  alt_day2_gamblers_result['me'] == 22                — Семён выиграл турнир
# 
#   
# alt_route_un_fz
# — строка 943:
#   alt_day2_fail == 1                      >>  alt_my_rival_1_tour.take == 'un'                    — Семён проиграл Лене в 1 туре.
#                                             + alt_day2_gamblers_result['me'] == 1
#                           При этом далее есть фраза — "хотя она далеко и не прошла" — это не факт, Лена может и выиграть турнир, вообще-то.
#       
#
# alt_route_me_zneutral
# — строка 799:
#   alt_day2_dv_bet_won != 1                >>  alt_day2_gamblers_result['me'] <= 21                — Семён не выиграл турнир
#       
# ***********************************************************************************************



# *************************************************************************************************************** УДАЛИТЬ
# Этот кусок кода удалить — он нужен для отдельного входа в турнир
init 2:
    $ mods["scenario__alt__test"] = u">== '7 Дней Лета'. Турнир. Проверка. ==<"
    $ mod_tags["scenario__alt__test"] = ["length:test","gameplay:test","protagonist:male","special:TEST","character:7ДЛ — ТЕСТ"]
    
label scenario__alt__test:
    $ alt_save_release_no = "00.x.0"
    $ bak_release_no = alt_release_no
    $ alt_release_no = "00.x.0"
    $ th_prefix = "«"
    $ th_suffix = "»"
    $ alt_day0_prologue = True
    stop ambience
    $ day_time()
    $ persistent.sprite_time = "day"
    $ make_names_unknown_7dl()
    $ meet('un',"Лена")
    $ meet('sl',"Славя")
    $ meet('dv',"Алиса")
    $ meet('mi',"Мику")
    $ meet('us',"Ульяна")
    $ meet('sh',"Шурик")
    $ meet('mz',"Женя")
    $ meet('el',"Электроник")
    $ meet('mt',"Ольга Дмитриевна")
    $ meet('ba',"Физрук")
    
    scene bg int_dining_hall_day with fade
    window show
    
    call alt_day0_vars
    call alt_day1_vars
    call alt_day2_vars
    $ plthr = u"Локи"                       # играем за Локи
    $ loki = True
    $ herc = False
    $ alt_day2_dv_bet_approve = True        # спорим с Алисой
    $ alt_day2_dv_harass = False
    $ alt_day2_walk = 0                     # метим карты
    $ lp_dv = 6                             # всем девчонкам по 6 ЛП
    $ lp_un = 6
    $ lp_mi = 6
    $ lp_sl = 6
    
    "Проверка турнира."
    "{b}Играем за Локи; метим карты; спорим с Алисой; всем девчонкам — по 6 ЛП.{/b}"
    window hide
    
# *************************************************************************************************************** /УДАЛИТЬ






# ================================================================================================
#                                            начало игры (именно на ЭТУ метку переходим из сценария)
# ================================================================================================
label alt_day2_cards_tournament:
    $ persistent.sprite_time = "day"
    $ day_time()
    $ alt_chapter(2, u"Турнир")
    stop ambience fadeout 1
    stop music fadeout 1
    play sound sfx_close_door_1
    scene bg int_dining_hall_day with fade
    play music music_7dl["bureaucracy"] fadein 1
    play ambience ambience_medium_crowd_indoors_1 fadein 1
    window show
    "А внутри уже всё было готово!"
    "Столы были сдвинуты плей-офф таблицей, победитель пересаживался за соседний стол, проигравший просто вставал с места."
    "Настроение у всех было приподнятое и праздничное."
    "Я пригляделся, смотря по соперникам и прикидывая шансы."

    show sh normal at right
    show us normal pioneer at left
    with dissolve
    "Шурик, как и я, не совсем понимающий, что он здесь забыл, сидел рядом с Ульяной."
    "Егоза нетерпеливо раскачивалась на стуле и пыталась вытянуть из Шурика какие-то сведения о предстоящей игре, на что тот только недовольно хмурился и делал вид, что он вообще не с ней."
    hide sh
    hide us
    with dissolve
    
    show sl normal pioneer at right
    show mz normal glasses pioneer at left
    with dissolve
    if ('library' in list_voyage_7dl):
        "Следующий стол оккупировала жужелица из библиотеки, ей противостояла Славя."
    else:
        "Следующий стол занимала та самая незнакомая девочка в очках, против неё играла Славя."
    "Я, поймав её взгляд, ободряюще улыбнулся:"
    me "Удачи."
    show sl smile pioneer at right
    sl "Спасибо."
    "Она улыбнулась в ответ."
    hide sl
    hide mz
    with dissolve

    show dv smile pioneer2 at left
    show mi normal pioneer at right
    with dissolve
    "Алисе в жертвы досталась Мику, и я на секунду пожалел несчастную японскую девочку."
    "То, каким азартом горели глаза Алисы, говорило лишь об одном — хищница настроена на победу, и ни на что иное!"
    if alt_day2_dv_bet_approve:
        show dv grin pioneer2 at left
        "Поймав мой взгляд, Алиса подмигнула, напоминая о пари, и я ответно кивнул."
    elif alt_day2_dv_harass:
        show dv sad pioneer2 with dissolve
        "Встретившись со мной глазами, она почему-то вздрогнула и мгновенно отвернулась."
        "Кажется, сценка у дверей произвела на неё неизгладимое впечатление!"
    else:
        "Меня она не удостоила даже взглядом."
    hide dv
    hide mi
    with dissolve

    show un normal pioneer with dissolve
    "Пустовало одно место — напротив Лены. Кажется, мне предстоит играть с ней."
    "Всё остальное пространство было занято болельщиками и зрителями."
    me "Привет ещё раз."
    "Я опустился на стул напротив."
    me "Кажется, нам предстоит выступить друг против друга."
    show un shy pioneer with dissolve
    un "Да…"
    "От внимания зрителей она явно чувствовала себя не в своей тарелке."
    me "Значит, удачи нам обоим."
    "На секундочку вдруг захотелось сдать партию, чтобы немного приободрить эту грустную девочку. Надо же иногда делать и добрые дела, не так ли?"
    hide un with dissolve

    window hide
    $ persistent.sprite_time = "day"
    $ day_time()
    with dissolve
# ------------------------------------------------------------- ADD загоняем БГ зала на нижний слой
    python:
        renpy.scene('underlay')
        renpy.show('bg int_dining_hall_day',layer='underlay')
        renpy.scene('master')
        renpy.transition(dissolve)
# ------------------------------------------------------------- /ADD
    window show
    "Закончив считать карты, Электроник повернулся в нашу сторону и с нездоровым даже для него оживлением обратился к нам:"
    show el normal pioneer at right
    el "Карты у нас есть, все на местах. Начинаем турнир!"
    me "Погоди, торопыга."
    "Проворчал я."
    me "Как насчёт правил? Или мы в техасский холдем поиграть присели?"
    el "Ой, правила. Точно."
    "Электроник взял маркер, которым чертил схемы игры, и погрузился в размышления, машинально покусывая колпачок."
    el "Так вот."
    "Он показал на схему."
# ------------------------------------------------------------- ADD Показываем схему турнира на фоне зала
    python:
        renpy.show('alt_tournament_bg',layer='underlay')
        renpy.transition(dissolve)
# ------------------------------------------------------------- /ADD
    el "Это схема турнира, и…"
    show dv angry pioneer2 at left
    show el normal pioneer at cright
    with dissolve
    dv "Да уж не тупые. Поняли, что проигравший выбывает."
    "Перебила его Алиса."
    dv "О правилах игры давай."
    hide dv
    show el normal pioneer at center
    with dissolve
# ------------------------------------------------------------- ADD Убираем схему турнира
    python:
        renpy.hide('alt_tournament_bg',layer='underlay')
        renpy.transition(dissolve)
# ------------------------------------------------------------- /ADD
    el "Ладно."
    "Смутившийся было Электроник мгновенно набрал привычный темп."
    el "Основное правило — проигравший выбывает. Поэтому никаких вторых шансов, переигровок, реваншей и прочего!"
    "Он отмахнулся от тянущей руку Ульянки, и продолжил."
    el "Каждый тур состоит из двух игр, если и после них у игроков будет ничья, исход решит третья партия. После этого проигравшие в туре выбывают, и начинается сле…"
    me "Я тебя умоляю."
    "Не выдержал я."
    me "Хватит уж о системе плей-офф! Мы все прекрасно знаем, как она работает! Давай о правилах игры!"
    el "Я уже почти перешёл к ним."
    "Выкрутился Электроник."
    el "Поскольку добровольцев…"
    "Он кинул взгляд в мою сторону и мгновенно поправился."
    el "Участников будет восемь, то туров, будет, соответственно, три."
    "Тут у него загорелась во лбу звезда, и он поднял указательный палец."
    el "Победитель последнего тура получит огромный приз!"
    show dv normal pioneer2 at left
    show el normal pioneer at cright
    me "К игре!"
    "Хором с Алисой рявкнули мы."
    el "Да я уже почти там. Чего вы, в самом деле!"
    "Он спрятал растерянность, делая вид, что прочищает горло."
    hide dv
    show el normal pioneer at center
    with dissolve
    el "Итак, все комбинации покерные, вы должны собрать у себя комбинацию сильнее, чем у противника. Двойку, тройку, четвёрку…"
    show us grin pioneer at cleft
    show el normal pioneer at cright
    with dissolve
    us "Пятёрку!"
    "Крикнула Ульяна, видимо, уставшая от того, что её игнорируют."
    el "Если кто-то не в курсе относительно ценности комбинаций."
    "Проигнорировал реплику Эл."
    hide us
    show el normal pioneer at center
    with dissolve
    el "Их можно посмотреть на таблице."
    "И он показал на другую половину бумажного листа."
    window hide
# ----------------------------------------------------------------------------------- ADD Показываем правила игры  
    if persistent.altRulesRead_new:                            # если правила игры уже прочитаны
        menu:
            "Показать комбинации":
                jump alt_day2_poker_rules_reading
            "Комбинации вроде бы помню, но нужна подсказка при игре":
                $ alt_hint_poker_contractual = True
                jump alt_day2_poker_rules_known
            "Я комбинации знаю, и подсказки не нужны":
                $ alt_hint_poker_contractual = False
                jump alt_day2_poker_rules_known
    else:                                                       # если ещё правил не читали — читаем.
        pass

label alt_day2_poker_rules_reading:
    $ alt_hint_poker_contractual = True
    $ set_mode_nvl()
    window show
    "{size=35}{u}Возможные комбинации карт в порядке убывания достоинства:{/u}{/size}{nw}"
    ""
    "- {b}Роял-флеш{/b} (англ. {i}royal flush{/i} — «королевская масть»): не является отдельной комбинацией,{nw}"
    "{space=15}а является частным случаем стрит-флеша, старшим из всех возможных, и состоит из 5 старших{nw}"
    if persistent.font_size == 'small':
        "{space=15}(туз, король, дама, валет, десять) карт одной масти, например: {b}{color=#FF6600}Т{image=suit_ussr_S} К{image=suit_ussr_S} Д{image=suit_ussr_S} В{image=suit_ussr_S} 10{image=suit_ussr_S}{/color}{/b}."
    elif persistent.font_size == 'large':
        "{space=15}(туз, король, дама, валет, десять) карт одной масти, например: {b}{color=#FF6600}Т{image=suit_ussr_L} К{image=suit_ussr_L} Д{image=suit_ussr_L} В{image=suit_ussr_L} 10{image=suit_ussr_L}{/color}{/b}."
    "{space=15}Если хотя бы одна из пяти карт не совпадает по масти с остальными, в таком случае получившаяся{nw}"
    "{space=15}комбинация будет расцениваться как стрит от туза."
    "{space=15}Эта комбинация выпадает достаточно редко; может быть, кому-то и повезёт...{nw}"
    ""
            
    "- {b}Стрит-флеш{/b} (англ. {i}straight flush{/i} — «масть по порядку»): любые пять карт одной масти по порядку,{nw}"
    if persistent.font_size == 'small':
        "{space=15}например: {b}{color=#009833}9{image=suit_utan_S} 8{image=suit_utan_S} 7{image=suit_utan_S} 6{image=suit_utan_S} 5{image=suit_utan_S}{/color}{/b}. Туз может как начинать порядок (роял-флеш),{nw}"
        "{space=15}так и заканчивать его: {b}{color=#009833}5{image=suit_uvao_S} 4{image=suit_uvao_S} 3{image=suit_uvao_S} 2{image=suit_uvao_S} Т{image=suit_uvao_S}{/color}{/b}."
        "{space=15}Комбинации карт {b}{color=#FF6600}2{image=suit_ussr_S} Т{image=suit_ussr_S} К{image=suit_ussr_S} Д{image=suit_ussr_S} В{image=suit_ussr_S}{/color}{/b} или {b}{color=#FF6600}4{image=suit_2ch_S} 3{image=suit_2ch_S} 2{image=suit_2ch_S} Т{image=suit_2ch_S} К{image=suit_2ch_S}{/color}{/b} — не являются стрит-флешами.{nw}"
    elif persistent.font_size == 'large':
        "{space=15}например: {b}{color=#009833}9{image=suit_utan_L} 8{image=suit_utan_L} 7{image=suit_utan_L} 6{image=suit_utan_L} 5{image=suit_utan_L}{/color}{/b}. Туз может как начинать порядок (роял-флеш),{nw}"
        "{space=15}так и заканчивать его: {b}{color=#009833}5{image=suit_uvao_L} 4{image=suit_uvao_L} 3{image=suit_uvao_L} 2{image=suit_uvao_L} Т{image=suit_uvao_L}{/color}{/b}."
        "{space=15}Комбинации карт {b}{color=#FF6600}2{image=suit_ussr_L} Т{image=suit_ussr_L} К{image=suit_ussr_L} Д{image=suit_ussr_L} В{image=suit_ussr_L}{/color}{/b} или {b}{color=#FF6600}4{image=suit_2ch_L} 3{image=suit_2ch_L} 2{image=suit_2ch_L} Т{image=suit_2ch_L} К{image=suit_2ch_L}{/color}{/b} — не являются стрит-флешами.{nw}"
    "{space=15}Если на руках у игрока оказывается {b}шесть{/b} карт по порядку, младшая карта игнорируется."
    "{space=15}Если у двух игроков одновременно на руках оказывается стрит-флеш, выигрывает тот,{nw}"
    "{space=15}у кого комбинация начинается с карты более высокого достоинства."
    "{space=15}Если у обоих игроков стрит-флеши идентичные, объявляется ничья.{nw}"
    ""
    
    $ renpy.pause (1)
    nvl clear
            
    "- {b}Покер{/b}/Каре/Четвёрка (англ. {i}four of a kind, quads{/i} — «четыре одинаковых»): четыре карты{nw}"
    if persistent.font_size == 'small':
        "{space=15}одинакового достоинства, например: {b}{color=#FF6600}8{image=suit_ussr_S} 8{image=suit_2ch_S} {color=#009833}8{image=suit_uvao_S} 8{image=suit_utan_S}{/color}{/b}{/b}, остальные карты не важны."
    elif persistent.font_size == 'large':
        "{space=15}одинакового достоинства, например: {b}{color=#FF6600}8{image=suit_ussr_L} 8{image=suit_2ch_L} {color=#009833}8{image=suit_uvao_L} 8{image=suit_utan_L}{/color}{/b}{/b}, остальные карты не важны."
    "{space=15}Если в дополнение к покеру на руках у игрока имеется ещё и пара, она не считается;{nw}"
    "{space=15}{i}комбинации «Четыре + два» в игре нет{/i}."
    "{space=15}Два покера принципиально не могут быть одинаковыми, так что когда у двух игроков в наличии{nw}"
    "{space=15}такие комбинации, побеждает тот, у кого покер состоит из карт более высокого достоинства.{nw}"
    ""
    
    "- {b}Фул-хаус{/b}/Полный дом/Три плюс два (англ. {i}full house, full boat{/i} — «полный дом», «полная лодка»):{nw}"
    if persistent.font_size == 'small':
        "{space=15}одна тройка и одна пара, например: {b}{color=#FF6600}10{image=suit_ussr_S} 10{image=suit_2ch_S} {color=#009833}10{image=suit_utan_S} 8{image=suit_uvao_S} {color=#FF6600}8{image=suit_ussr_S}{/color}{/color}{/b}{/b}."
    elif persistent.font_size == 'large':
        "{space=15}одна тройка и одна пара, например: {b}{color=#FF6600}10{image=suit_ussr_L} 10{image=suit_2ch_L} {color=#009833}10{image=suit_utan_L} 8{image=suit_uvao_L} {color=#FF6600}8{image=suit_ussr_L}{/color}{/color}{/b}{/b}."
    "{space=15}Если на руках две тройки, тройка карт младшего достоинства считается, как пара карт;{nw}"
    "{space=15}{i}комбинации «Две тройки» в игре нет{/i}."
    "{space=15}Если у соперников одновременно оказались на руках такие комбинации,{nw}"
    "{space=15}старшей считается та, в которой тройку составляют более высокие по достоинству карты,"
    if persistent.font_size == 'small':
        "{space=15}например: {b}{color=#009833}В{image=suit_uvao_S} {color=#FF6600}В{image=suit_2ch_S} В{image=suit_ussr_S} {color=#009833}9{image=suit_uvao_S} 9{image=suit_utan_S}{/color}{/color}{/b}{/b} старше, чем {b}{color=#FF6600}7{image=suit_2ch_S} 7{image=suit_ussr_S} {color=#009833}7{image=suit_utan_S} Т{image=suit_uvao_S} {color=#FF6600}Т{image=suit_2ch_S}{/color}{/color}{/b}."
    elif persistent.font_size == 'large':
        "{space=15}например: {b}{color=#009833}В{image=suit_uvao_L} {color=#FF6600}В{image=suit_2ch_L} В{image=suit_ussr_L} {color=#009833}9{image=suit_uvao_L} 9{image=suit_utan_L}{/color}{/color}{/b}{/b} старше, чем {b}{color=#FF6600}7{image=suit_2ch_L} 7{image=suit_ussr_L} {color=#009833}7{image=suit_utan_L} Т{image=suit_uvao_L} {color=#FF6600}Т{image=suit_2ch_L}{/color}{/color}{/b}."
    "{space=15}Два фулл-хауса, как и два покера, одинаковыми быть не могут (джокеров в колоде нет).{nw}"
    ""
    
    $ renpy.pause (1)
    nvl clear
    
    if persistent.font_size == 'small':
        "- {b}Флеш{/b} (англ. {i}flush{/i} — «масть»): пять карт одной масти, например: {b}{color=#009833}К{image=suit_utan_S} В{image=suit_utan_S} 8{image=suit_utan_S} 4{image=suit_utan_S} 3{image=suit_utan_S}{/b}.{nw}"
    elif persistent.font_size == 'large':
        "- {b}Флеш{/b} (англ. {i}flush{/i} — «масть»): пять карт одной масти, например: {b}{color=#009833}К{image=suit_utan_L} В{image=suit_utan_L} 8{image=suit_utan_L} 4{image=suit_utan_L} 3{image=suit_utan_L}{/b}.{nw}"
    "{space=15}Такую комбинацию для оценки называют «флеш от короля» — старшей карты комбинации."
    "{space=15}Самая старшая комбинация — с  тузом.{nw}"
    "{space=15}Если на руках оказывается {b}шесть{/b} карт одной масти, младшая карта комбинации игнорируется."
    "{space=15}Если у обоих соперников на руках будет такая комбинация, преимущество отдаётся тому,{nw}"
    "{space=15}у кого старшая карта в комбинации окажется более высокого достоинства."
    "{space=15}Если же получится так, что достоинство старших карт одинаково, объявляется ничья.{nw}"
    ""

    "- {b}Стрит{/b} (англ. {i}straight{/i} — «порядок»):  пять карт по порядку любых мастей,{nw}"
    if persistent.font_size == 'small':
        "{space=15}например: {b}{color=#FF6600}5{image=suit_2ch_S} 4{image=suit_ussr_S} {color=#009833}3{image=suit_utan_S} {color=#FF6600}2{image=suit_2ch_S} Т{image=suit_2ch_S}{/color}{/color}{/b}."
    elif persistent.font_size == 'large':
        "{space=15}например: {b}{color=#FF6600}5{image=suit_2ch_L} 4{image=suit_ussr_L} {color=#009833}3{image=suit_utan_L} {color=#FF6600}2{image=suit_2ch_L} Т{image=suit_2ch_L}{/color}{/color}{/b}."
    "{space=15}Если на руках оказывается {b}шесть{/b} карт по порядку, младшая карта в комбинации не участвует.{nw}"
    "{space=15}Туз может как начинать порядок, так и заканчивать его."
    if persistent.font_size == 'small':
        "{space=15}В приведённом выше примере {b}{color=#FF6600}Т{image=suit_2ch_S}{/color}{/b} заканчивает комбинацию и его достоинство{nw}"
        "{space=15}оценивается в единицу, а {b}{color=#FF6600}5{image=suit_2ch_S}{/color}{/b} считается старшей картой."
        "{space=15}Вышеприведённая комбинация является самым младшим стритом; самый старший стрит -{nw}"
        "{space=15}это стрит от туза: {b}{color=#FF6600}Т{image=suit_ussr_S} {color=#009833}К{image=suit_uvao_S} {color=#FF6600}Д{image=suit_2ch_S} В{image=suit_2ch_S} 10{image=suit_ussr_S}{/color}{/color}{/b}."
    elif persistent.font_size == 'large':
        "{space=15}В приведённом выше примере {b}{color=#FF6600}Т{image=suit_2ch_L}{/color}{/b} заканчивает комбинацию и его достоинство{nw}"
        "{space=15}оценивается в единицу, а {b}{color=#FF6600}5{image=suit_2ch_L}{/color}{/b} считается старшей картой."
        "{space=15}Вышеприведённая комбинация является самым младшим стритом; самый старший стрит -{nw}"
        "{space=15}это стрит от туза: {b}{color=#FF6600}Т{image=suit_ussr_L} {color=#009833}К{image=suit_uvao_L} {color=#FF6600}Д{image=suit_2ch_L} В{image=suit_2ch_L} 10{image=suit_ussr_L}{/color}{/color}{/b}."
    "{space=15}При одновременном наличии стритов у двух игроков победитель определяется по старшей{nw}"
    "{space=15}карте комбинации; если и старшие карты окажутся одинаковыми — объявляется ничья.{nw}"
    ""
    
    $ renpy.pause (1)
    nvl clear
            
    "- {b}Тройка{/b}/Сет/Триплет/Трипс (англ. {i}three of a kind, set{/i} — «три одинаковых», «набор»):{nw}"
    if persistent.font_size == 'small':
        "{space=15}три карты одного достоинства, например: {b}{color=#009833}7{image=suit_uvao_S} 7{image=suit_utan_S} {color=#FF6600}7{image=suit_2ch_S}{/color}{/b}."
    elif persistent.font_size == 'large':
        "{space=15}три карты одного достоинства, например: {b}{color=#009833}7{image=suit_uvao_L} 7{image=suit_utan_L} {color=#FF6600}7{image=suit_2ch_L}{/color}{/b}."
    "{space=15}Когда у двух соперников на руках одновременно окажутся тройки, победителем объявляется{nw}"
    "{space=15}тот игрок, у которго тройку составляют карты более высокого достоинства."
    "{space=15}Идентичных троек, как и покеров, и фулл-хаусов, в игре быть не может.{nw}"
    ""
    
    if persistent.font_size == 'small':
        "- {b}Две пары{/b}/Две двойки/Два плюс два (англ. {i}two pairs{/i}): две пары карт, например: {b}{color=#009833}8{image=suit_uvao_S} 8{image=suit_utan_S} {color=#FF6600}4{image=suit_ussr_S} 4{image=suit_2ch_S}{/color}{/b}."
    elif persistent.font_size == 'large':
        "- {b}Две пары{/b}/Две двойки/Два плюс два (англ. {i}two pairs{/i}): две пары карт, например: {b}{color=#009833}8{image=suit_uvao_L} 8{image=suit_utan_L} {color=#FF6600}4{image=suit_ussr_L} 4{image=suit_2ch_L}{/color}{/b}."
    "{space=15}Если на руках {b}три{/b} пары, пара карт самого младшего достоинства не учитывается,{nw}"
    "{space=15}{i}комбинации «Три пары» в игре нет{/i}."
    "{space=15}Когда у двух игроков на руках окажутся по две пары, старшей является та,{nw}"
    "{space=15}в которую входят две наиболее высокие по достоинству карты."
    "{space=15}В случае, когда старшие пары карт оказываются идентичными, старшинство{nw}"
    "{space=15}комбинации в целом определяется по младшей паре карт."
    "{space=15}Победителем будет считаться игрок, у которого младшая пара состоит из старших карт.{nw}"
    "{space=15}Если у обоих игроков комбинации по достоинству карт полностью идентичны, объявляется ничья.{nw}"
    ""
    
    $ renpy.pause (1)
    nvl clear
    
    if persistent.font_size == 'small':
        "- {b}Пара{/b}/Двойка (англ. {i}one pair{/i}): две карты одного достоинства, например: {b}{color=#FF6600}9{image=suit_ussr_S}{color=#009833} 9{image=suit_utan_S}{/color}{/b}."
    elif persistent.font_size == 'large':
        "- {b}Пара{/b}/Двойка (англ. {i}one pair{/i}): две карты одного достоинства, например: {b}{color=#FF6600}9{image=suit_ussr_L}{color=#009833} 9{image=suit_utan_L}{/color}{/b}."
    "{space=15}При наличии этой комбинации у двух игроков, преимущество у того, у кого выше{nw}"
    "{space=15}достоинство карт, составляющих пару. Если пары идентичны, объявляется ничья.{nw}"
    ""
            
    "- {b}Старшая карта{/b} (англ. {i}high card{i}): ни одна из вышеописанных комбинаций,{nw}"
    if persistent.font_size == 'small':
        "{space=15}например: {b}{color=#FF6600}Т{image=suit_2ch_S} 10{image=suit_2ch_S}{color=#009833} 9{image=suit_utan_S} 5{image=suit_uvao_S} 4{image=suit_uvao_S}{/color}{color=#FF6600} 2{image=suit_ussr_S}{/color}{/color}{/b}."
    elif persistent.font_size == 'large':
        "{space=15}например: {b}{color=#FF6600}Т{image=suit_2ch_L} 10{image=suit_2ch_L}{color=#009833} 9{image=suit_utan_L} 5{image=suit_uvao_L} 4{image=suit_uvao_L}{/color}{color=#FF6600} 2{image=suit_ussr_L}{/color}{/color}{/b}."
    "{space=15}Вышеприведённая комбинация называется «старший туз»."
    "{space=15}Если у соперников на руках оказывается по старшей карте,{nw}"
    "{space=15}победитель определяется по старшей из имеющихся на руках карт."
    "{space=15}Если старшие карты у игроков равны, объявляется ничья.{nw}"
    ""
    $ renpy.pause (1)
    window hide
    $ set_mode_adv()
    $ persistent.altRulesRead_new = True

label alt_day2_poker_rules_known:
# ----------------------------------------------------------------------------------- /ADD
    window show
    el "Ну а сейчас для лучшего усвоения материала, давайте сыграем пробную партию."
    el "На сторону сдаётся по шесть карт…"
    show us dontlike pioneer at left
    show el normal pioneer at right
    extend " По шесть, а не по двенадцать!"
    with dissolve
    "Закричал он, кинув косой взгляд на столик Шурика и Ульяны."
    "Немудрено — рыжая бестия забрала себе все 12 карт и разглядывала их, выбирая покрасивее."
    hide us with dissolve
    "После нескольких минут споров и ругани Ульянка фыркнула и вернула карты на родину, после чего, перемешав колоду, сдала себе и Шурику по шесть карт."
    window hide
# --------------------------------------------------------------------- ADD Блокировка роллбака включена
    $ d2_cardgame_block_rollback = True
# --------------------------------------------------------------------- /ADD
    stop music fadeout 6
    
    
    if persistent.altCardsDemo_new:
        menu:
            "Пройти обучение":
                jump alt_day2_demo_play_new
            "Пропустить обучение":
                jump alt_day2_cards_continue_new

label alt_day2_demo_play_new:
    python:
        dialogs = {
                        (3, 'rival_select','call'): 'alt_day2_demo_play_intro_new',
                        (3, 'me_defend_1','call'):  'alt_day2_demo_play_me_defend_1_new',
                        (3, 'me_defend_2','call'):  'alt_day2_demo_play_me_defend_2_new',
                        (3, 'me_select_1','call'):  'alt_day2_demo_play_me_select_1_new',
                        (3, 'rival_defend','call'): 'alt_day2_demo_play_rival_defend_new',
                        (2, 'rival_select','jump'): 'alt_day2_demo_play_after_loop_new'
                    }
        generate_cards_alt('bg hall', dialogs)
        rival = CardGameRivalWiseUsual(un_avatar_set, u"Пробная игра", 'foolplay', 5)
        alt_name_my_rival_r = "Лены"
        VISIBLE = False
        alt_whose_first_move = 'rival'
    jump cards_gameloop_wise_alt

label alt_day2_demo_play_intro_new:
    show el normal pioneer at cleft with dissolve
    $ show_cards_alt()
    window show
    el "Это не просто карты."
    $ show_cards_alt()
    if alt_day2_walk == 0:
        $ VISIBLE = True
        $ INVISIBLE = True
        $ alt_hint_poker = True
        $ show_cards_alt()
        th "Это ещё и ваш способ оставить противника без штанов."
        $ show_cards_alt()
        th "Если бы мы играли на деньги… Впрочем, не будем о грустном."
    $ show_cards_alt()
    el "Это ваши войска специального назначения. {w}Элита!"
    $ show_cards_alt()
    el "Вы дорожите каждым из них, ведь его жизнь неповторима."
    $ show_cards_alt()
    el "Потеря каждого из них критична."
    $ show_cards_alt()
    el "А теперь переверните карты и посмотрите."
    $ show_cards_alt()
    "Чего и следовало ожидать, Ульянка перевернула карты Шурика, и задумчиво изучала их."
    $ show_cards_alt()
    el "Свои карты!"
    $ show_cards_alt()
    "Закричал Электроник."
    $ show_cards_alt()
    el "Свои! А не чужие."
    $ show_cards_alt()
    us "А это была разведка! Вот."
    $ show_cards_alt()
    "По сравнению с непрошибаемым Шуриком, Ульяна являла собой образец неуправляемой стихии. Вздохнув, Шурик собрал свои карты и, тщательно перемешав, сдал себе ещё шестёрку карт."
    
    $ VISIBLE = True
    $ alt_hint_poker = True
    $ show_cards_alt()
    "Между тем, Электроник продолжил объяснение:"
    $ show_cards_alt()
    el "Итак, вы во главе элитных войск."
    $ show_cards_alt()
    el "Но само сражение ещё впереди. А пока вам надо укрепить порядки."
    $ show_cards_alt()
    "Окопаться, не иначе."
    $ show_cards_alt()
    el "А для этого… Необходимо сманивать элиту противника на свою сторону!"
    $ show_cards_alt()
    us "Сманивать в смысле «красть»?"
    $ show_cards_alt()
    "В голосе Ульяны слышался неприкрытый восторг."
    $ show_cards_alt()
    el "В целом, д-да…"
    $ show_cards_alt()
    "Ведущего немного смутил эпитет, но крыть было нечем, и он согласился."
    $ show_cards_alt()
    el "В целом. Но не всё так просто."
    $ show_cards_alt()
    el "Первым ходом вы намечаете себе цель, и пытаетесь её сманить."
    $ show_cards_alt()
    el "Вы не видите, кто это, поэтому здесь работает удача."
    $ show_cards_alt()
    us "Мой дедушка офицер!"
    "Заявила Ульяна."
    $ show_cards_alt()
    el "Итак, противник тянется к карте, но и вы не должны дремать!"
    $ show_cards_alt()
    el "У вас есть две попытки запутать врага, поменяв карты местами!"
    $ show_cards_alt()
    el "Или можно не менять, если под ударом ненужная вам карта. Просто пропускаете ход и карта отходит к атакующему."
    $ show_cards_alt()
    el "Естественно, обороняющийся рано или поздно становится атакующим — и вот тогда может вернуть карту или забрать что-то нужное игрока."
    $ show_cards_alt()
    el "Ну а теперь… Сыграем."
    
    hide el with dissolve
    $ show_cards_alt()
    me "Первый ход твой…"
    $ show_cards_alt()
    "Я, как мог, разложил карты поудобнее."
    $ show_cards_alt()
    "И Лена, смутившись ещё больше обычного, потянулась к моим картам…"
    window hide
    return

label alt_day2_demo_play_me_defend_1_new:
    $ show_cards_alt()
    window show
    "Но тут её рука застыла на полпути."
    $ show_cards_alt()
    un "Т-ты будешь…"
    $ show_cards_alt()
    th "Точно! Я же должен защищать свою карту!"
    $ show_cards_alt()
    "Я вспомнил, что там говорил Электроник…"
    $ show_cards_alt()
    th "Чтобы попытаться запутать соперника, можно поменять карты местами — и так два раза. А можно и не менять…"
    $ show_cards_alt()
    th "Защищать мне эту карту или нет?"
    window hide
    return
    
# ============================================ добавлена одна метка
label alt_day2_demo_play_me_defend_2_new:
    $ show_cards_alt()
    window show
    th "И Лена может изменить свой выбор, взяв другую карту, а может и не менять."
    $ show_cards_alt()
    th "Понемногу всё становилось понятно!"
    window hide
    return
# ============================================ добавлена одна метка
    
label alt_day2_demo_play_me_select_1_new:
    window show
    me "Теперь моя очередь."
    $ show_cards_alt()
    th "Я могу вернуть украденную карту или выбрать любую другую…"
    if alt_day2_walk == 0:
        $ show_cards_alt()
        th "А зная карты противника, легко выбрать нужную…"
        $ show_cards_alt()
        th "Никогда бы не подумал, что буду жульничать на турнире, но, возможно, как раз это меня и спасёт…"
    window hide
    return
    
label alt_day2_demo_play_rival_defend_new:
    $ show_cards_alt()
    window show
    th "Лена может попробовать защитить свою карту."
    $ show_cards_alt()
    th "Но если я буду внимательным, то всё равно возьму ту, что выбрал с самого начала…"
    window hide
    return

label alt_day2_demo_play_after_loop_new:
    $ show_cards_alt()
    window show
    th "Получилось!"
    window hide
    $ ui.jumpsoutofcontext('alt_day2_cards_continue_new')
    
label alt_day2_cards_continue_new:
    scene bg int_dining_hall_sunset with dissolve
    python:
        renpy.scene('underlay')
    $ persistent.altCardsDemo_new = True
    window show
    "Электроник, до этого наблюдавший за нами, удовлетворённо кивнул."
    "Похоже, теперь мы действительно разобрались в его игре."
    show el normal pioneer at center with dissolve
    el "Итак, во время игры противники три раза обмениваются своими бойцами, а потом открывают карты."
    el "И мы смотрим, чья армия сильнее."
    hide el with dissolve
    "Электроник отошёл к своему ватману, а Ульяна не выдержала и закричала."
    show us normal pioneer with dissolve
    us "Моя армия будет самой сильной!"
    us "Давайте уже играть!"
    hide us with dissolve
    window hide
    
label alt_day2_tournament_prep_new:
    scene bg int_dining_hall_sunset
    play music music_7dl["explore"] fadein 5
    show mt normal pioneer
    with dissolve
    mt "Давайте-ка мы немного разнообразим игру!"
    show el surprise pioneer at left with dissolve
    el "Что вы имеете в виду?"
    show mt laugh pioneer with dspr
    mt "Я вижу, тут кое-кто очень настроен на победу, так что внесём элемент случайности."
    "Она достала из кармана несколько бумажек и, быстро нарвав их, написала на них номера, ссыпала в панамку и обнесла присутствующих."
    show el sad pioneer with dspr
    el "Воооот, лишние хлопоты."
    "Вздохнул парень."
    show mt normal pioneer with dspr
    mt "Всё хорошо! {w}Тянем жребий и по нему распределяемся на пары."
    mt "А то знаю я эти договорные матчи!"
    "Не прошло и пяти минут, а мы уже разбились по парам."

 # ---------------------------------------------------------------------------------
label alt_day2_tournament_tour_1_new:
    $ alt_tournament_state = "1_round_start"                                                # устанавливаем начало 1-го раунда
    $ alt_day2_gamblers_begin = alt_gamblers_shuffler()                                     # вызываем рандомизатор — получаем список игроков, отсортированный по уcловным номерам.
    $ alt_my_rival_1_tour = alt_get_me_rival(alt_day2_gamblers_begin)                       # узнаём своего соперника
    $ alt_name_my_rival_i = alt_my_rival_1_tour.name['i']                                   # узнаём ИМЯ своего соперника (в именительном падеже)
    $ alt_name_my_rival_r = alt_my_rival_1_tour.name['r']                                   # узнаём ИМЯ своего соперника (в родительном падеже)
    $ alt_name_my_rival_d = alt_my_rival_1_tour.name['d']                                   # узнаём ИМЯ своего соперника (в дательном падеже)
    $ alt_name_my_rival_v = alt_my_rival_1_tour.name['v']                                   # узнаём ИМЯ своего соперника (в винительном падеже)
    $ alt_name_my_rival_t = alt_my_rival_1_tour.name['t']                                   # узнаём ИМЯ своего соперника (в творительном падеже)
    $ alt_spr_my_rival = alt_my_rival_1_tour.take                                           # получаем спрайт соперника — заголовок
    $ alt_emo_my_rival = alt_sprites_rival_recognition[alt_spr_my_rival][0]                 # эмоция (строка)
    $ alt_clot_my_rival = alt_sprites_rival_recognition[alt_spr_my_rival][1]                # одежда (строка)
    $ alt_pos_my_rival = alt_sprites_rival_recognition[alt_spr_my_rival][2]                 # положение
    $ alt_nick_my_rival = alt_my_rival_1_tour.nick                                          # получаем характер соперника (для диалога)
 # ---------------------------------------------------------------------------------
    scene bg int_dining_hall_sunset
    $ renpy.fix_rollback()                                                                  # фиксируем выбор — "откатом" поменять будет нельзя
    window show
    "Мне в оппоненты рандом послал {w}%(alt_name_my_rival_v)s."                             # называем своего соперника
    
# .......................................... ДИАЛОГИ 
    if alt_my_rival_1_tour.take == 'un':
        show un shy pioneer at cright with dspr
        me "И снова добрый вечер."
        "Она смущённо улыбнулась, но ничего не сказала."

    elif alt_my_rival_1_tour.take == 'sl':
        show sl smile2 pioneer at cright with dspr
        sl "Знаешь, я не очень хороша в картах."
        me "Да я вообще ничего про эту игру не знаю."
        "Славя улыбнулась мне и села напротив."

    elif alt_my_rival_1_tour.take == 'dv':
        show dv grin pioneer2 at cright with dspr
        dv "Ну что, готов к сокрушительному поражению?"
        "Усмехнулась она, садясь на противоположное место."
        me "А как же. {w}Я принесу на твою могилку два гладиолуса."

    elif alt_my_rival_1_tour.take == 'mi':
        show mi smile pioneer at cright with dspr
        mi "Ой, привет, Сенечка, а что за игра такая, ты не знаешь? А то меня позвали играть, а правила не объяснили."
        "Не переставая болтать, она села за стол и сложила руки."

    elif alt_my_rival_1_tour.take == 'us':
        show us laugh pioneer at cright with dspr
        us "Готов поддаваться?"
        me "И не мечтай."
        show us calml pioneer with dspr
        us "И не надо! Но играть будем по моим правилам!"
        me "Это по каким это?"
        us "Увидишь!"
        
    elif alt_my_rival_1_tour.take == 'sh':
        show sh normal pioneer at cright with dspr
        sh "Ну что, пусть победит сильнейший?"
        "Я молча пожал ему руку."

    elif alt_my_rival_1_tour.take == 'mz':
        show mz normal pioneer at cright with dspr
        mz "Я твой противник."
        "Скрипнула она, присаживаясь напротив."
        "Я молча кивнул в ответ."
# .......................................... /ДИАЛОГИ 
    window hide

    if persistent.altCardsWon1_new or persistent.altCardsFail_new:
        menu:
            "Играть самостоятельно":
                pass
            "Победа в финале" if persistent.altCardsWon3_new:
                $ alt_day2_detour_1_tour = True                         # Пропускаем 1 тур
                $ alt_day2_detour_semifinal = True                      # Пропускаем полуфинал
                $ alt_day2_detour_final = True                          # Пропускаем финал
                $ alt_day2_tournament_fast_win = True                   # Победа в финале на холяву
                $ karma += 10
            "Поражение в финале" if persistent.altCardsWon2_new:
                $ alt_day2_detour_1_tour = True                         # Пропускаем 1 тур
                $ alt_day2_detour_semifinal = True                      # Пропускаем полуфинал
                $ alt_day2_detour_final = True                          # Пропускаем финал
                $ karma -= 10
            "Поражение в полуфинале" if persistent.altCardsWon1_new:
                $ alt_day2_detour_1_tour = True                         # Пропускаем 1 тур
                $ alt_day2_detour_semifinal = True                      # Пропускаем полуфинал
                $ karma -= 10
            "Поражение в первом же коне":
                $ alt_day2_detour_1_tour = True                         # Пропускаем 1 тур
                
        
    
label alt_day2_participate_new:
    $ alt_day2_gamblers_1_tour = alt_gamblers_arrange(alt_day2_gamblers_begin)      # получаем список игроков, рассаженных по столам попарно (1 тур)
    $ renpy.fix_rollback()                                                          # фиксируем выбор — "откатом" поменять будет нельзя
    $ places_my_table = alt_get_my_table(alt_day2_gamblers_1_tour)                  # Стол Семёна = [место Семёна, место соперника, № их стола]
    
    if not alt_day2_detour_1_tour:                                                  # если НЕ пропуск 1 тура
        scene bg int_dining_hall_sunset
        window show
        "Пока суд да дело, я решил разузнать, какая диспозиция сложилась на игровом поле."
        $ alt_mstt = 9
        call show_tournament_table                                                  # показываем турнирную таблицу — ПУСТУЮ
        window show
        
    $ alt_table_no = 1                                                              # № стола = 1 (начинаем с первого)
    $ alt_mstt = 0                                                                  # обнуляем глобальный счетчик таблицы
    $ alt_random_box_1 = range(1,len(alt_table_affiliation)+1)                      # черный ящик — список от 1 до длины представлений столов +1
    while alt_table_no <= 4:                                                        # перебираем столы от 1 до 4
        if not alt_day2_detour_1_tour:                                              # если НЕ пропуск 1 тура
            $ sitting_at_table,gambler_upper,gambler_lower,must_taunt = alt_declare_tournament_tables(alt_table_no)  #расссадка, игроки, таунты — по номеру стола
            "%(sitting_at_table)s"
            call show_tournament_table                                                  # переход по метке — вызов очередной фишки
            extend " %(gambler_upper)s"                                                 # выводим в окно имя верхнего игрока
            call show_tournament_table                                                  # переход по метке — вызов очередной фишки
            extend " и %(gambler_lower)s."                                              # выводим в окно имя нижего игрока
            if must_taunt != None:                                                      # если таунт есть
                "%(must_taunt)s"                                                        # выводим его
                
#внимание: если Семён сидит не за первым столом, то показывается первая фраза, а если за первым - то вторая. Вроде всё как надо, можно не менять.
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ ВОПРОС
            if alt_table_no == 1 and alt_table_no != places_my_table[2]:
                "С первым столом разобрались, кто-то из них сегодня не дойдёт до финала."
            elif alt_table_no == 2 and places_my_table[2] == 1:                                             
                "Со вторым столом разобрались, кто-то из них сегодня не дойдёт до финала."
                
# для всех столов такое или только для первого — ? если для всех — можно перенести в функцию
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ /ВОПРОС

        if alt_table_no != places_my_table[2]:                                          # если номер стола — НЕ свой
            $ alt_day2_gamblers_1_tour[2*alt_table_no - renpy.random.choice([1,2])].winner = True  # тогда один из игроков (рандомно) — победитель в этапе
            $ renpy.block_rollback()                                                                # блокируем роллбак
        $ alt_table_no += 1                                                             # следующий стол
    if not alt_day2_detour_1_tour:                                                  # если НЕ пропуск 1 тура
        "Таким нехитрым образом удалось немного разобраться с тем, кто и против кого играет."
        "Что ж."
        "Пусть мне повезёт, а одна рыжая зазнайка утрётся!"
        "Я кивнул, сигналиризуя о готовности."

    if alt_day2_detour_1_tour and not alt_day2_detour_semifinal:                # если пропуск 1 тура и не пропуск полуфинала
        jump alt_day2_participate_fail_end_new                                  # переход на  поражение в 1 туре
    elif alt_day2_detour_semifinal:                                             # если пропуск полуфинала
        jump alt_day2_participate_win_end_new                                   # переход на победу в 1 туре
    
label alt_day2_tournament_start_new:                                            # начало 1 тура — сюда переходим при реванше
    call alt_day2_stipulation_new                                               # определяемся, кто первый ходит
    
#-------------------------------------------------------------------------------------------------
    # первоначальные "настройки" игроков — могут меняться по результатам игры
    # 'defense' — защита, 'gamble' — риск, 'succumb' — слив, 'foolplay' — рандом
    # вероятность ошибки: 1 = 80%, .... 4 = 20%, 5 — ошибок нет.
    
    if alt_my_rival_1_tour.take == 'un':                                                    # Лена старается проиграть
        $ alt_day2_gambler_behavior = 'succumb'
        if not alt_day2_revanche:                                                           # еcли НЕ реванш
            $ alt_day2_gambler_skill = 3                                                    # ошибок — 40%(3)
        else:                                                                               # еcли РЕВАНШ
            $ alt_day2_gambler_skill = 4                                                    # ошибок — 20%(4) 
    elif alt_my_rival_1_tour.take == 'sl':                                                  # Славя будет защищаться, ошибок — 40%(3)
        $ alt_day2_gambler_behavior = 'defense'
        $ alt_day2_gambler_skill = 3
    elif alt_my_rival_1_tour.take == 'dv':                                                  # Алиса рискует, ошибок — 80%(4)
        $ alt_day2_gambler_behavior = 'gamble'
        $ alt_day2_gambler_skill = 4
    elif alt_my_rival_1_tour.take == 'mi':                                                  # Мику будет защищаться, ошибок — 60%(3)
        $ alt_day2_gambler_behavior = 'defense'
        $ alt_day2_gambler_skill = 3
    elif alt_my_rival_1_tour.take == 'us':                                                  # Ульяна будет защищаться
        $ alt_day2_gambler_behavior = 'defense'
        if not alt_day2_revanche:                                                           # еcли НЕ реванш
            $ alt_day2_gambler_skill = 1                                                    # ошибок — 80%(1)
        else:                                                                               # еcли РЕВАНШ
            $ alt_day2_gambler_skill = 2                                                    # ошибок — 60%(2)
    elif alt_my_rival_1_tour.take == 'sh':                                                  # Шурик экспериментирует, так что может и рискнуть, и защищаться, и слить; ошибки 40%(3)
        $ alt_day2_experiment = ['defense','gamble','succumb']                              # у него своя кухня — набор из возможных вариантов
        $ alt_day2_gambler_skill = 3
    elif alt_my_rival_1_tour.take == 'mz':                                                  # Женя играет рандомно, как в классике, ошибки = 5
        $ alt_day2_gambler_behavior = 'foolplay'
        $ alt_day2_gambler_skill = 5
#-------------------------------------------------------------------------------------------------

label alt_day2_1_tour_re_game:                                                              # игра 1 тура — сюда возвращаемся на повторную игру 
    $ alt_my_poker_hand = None
    $ alt_rival_poker_hand = None
    
    if alt_day2_walk == 0:
        $ VISIBLE = True
        $ INVISIBLE = True
    else:
        $ VISIBLE = True
        $ INVISIBLE = False

    python:
        dialogs = {
                        (0, 'win','jump'):'alt_day2_one_play_win_new',
                        (0, 'fail','jump'):'alt_day2_one_play_fail_new',
                        (0, 'draw','jump'):'alt_day2_one_play_draw_new'
                    }
        generate_cards_alt('bg hall', dialogs)
        
# ****************   НОВЫЕ  СОПЕРНИКИ   ******************************************
        if alt_my_rival_1_tour.take == 'un':
            rival = CardGameRivalWiseUsual(un_avatar_set, u"Лена", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_1_tour.take == 'sl':
            rival = CardGameRivalWiseUsual(sl_avatar_set, u"Славя", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_1_tour.take == 'dv':
            rival = CardGameRivalWiseUsual(dv_avatar_set, u"Алиса", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_1_tour.take == 'mi':
            rival = CardGameRivalWiseUsual(mi_avatar_set, u"Мику", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_1_tour.take == 'us':
            rival = CardGameRivalWiseLikeUS(us_avatar_set, u"Ульяна", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_1_tour.take == 'sh':
            alt_day2_gambler_behavior = alt_day2_experiment.pop(random.randrange(0,len(alt_day2_experiment)))                   # у Шурика случайный выбор из оставшегося в списке 
            rival = CardGameRivalWiseUsual(sh_avatar_set, u"Шурик", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_1_tour.take == 'mz':
            rival = CardGameRivalWiseUsual(mz_avatar_set, u"Женя", alt_day2_gambler_behavior, alt_day2_gambler_skill)
# ************************************************************************************

    $ alt_hint_poker = alt_hint_poker_contractual                                           # подсказки комбинаций — по просмору правил
    jump cards_gameloop_wise_alt                                                            # переход карточный стол

#-------------------------------------------------------------------------------------------------
label alt_day2_participate_fail_end_new:
    $ alt_day2_result_tour = 1                                              # Семён проиграл в 1 туре
    if alt_day2_revanche:                                               # если был реванш
        if alt_my_rival_1_tour.take == 'un':                            # если соперник — Лена
            "Ну вот, чего я и добивался."
            "Подмигнув Лене, я поднялся и раскланялся."
            me "Я проиграл. Простите."
            "И удалился — до ужина было ещё полчаса, а голова у меня уже серьёзно гудела от шума толпы."

        elif alt_my_rival_1_tour.take == 'us':                          # если соперник — Ульяна
            "Пожав плечами, я встал из-за стола, оставляя в одиночестве что-то восторженно вопящую Ульянку."
            "Переигровки, реванши… Я утратил интерес к игре."
            "Даже не стал досматривать события в полуфинале и финале."
        else:                                                           # ... а может быть кто-то ещё
            pass
            
            # ТОDO — Обсчёт переменных — кто и как сыграл — для проверки по другим дням
            
            
        jump alt_day2_prepare_transition_to_supper                                            # после неудачного реванша -> переход на ужин
    else:
        pass
        
    $ persistent.altCardsFail_new = True
    
    $ alt_day2_gamblers_1_tour[places_my_table[1]].winner = True            # соперник выиграл
    $ alt_tournament_state = "1_round_end"                                  # устанавливаем конец 1-го раунда
    
    scene bg int_dining_hall_sunset with dissolve
    window show
    call alt_day2_summary_poker_round                                       # подводим итоги раунда


# ............................................ ДИАЛОГИ
    if alt_my_rival_1_tour.take == 'un':
        $ lp_un = lp_un + 1
        play music music_7dl["sneakupon"]
        if alt_day2_dv_bet_approve:
            show un cry_smile pioneer at center
            un "Ты поддался… Ты чёртов жулик, ты поддался…"
            "О чем это она? Ещё и жуликом обозвала."
            if alt_day2_walk == 0:
                th "Впрочем, она не так уж и далека от истины."
            else:
                pass
            me "Лена, извини, но…"
            un "Не говори ничего. Я знаю, о чём ты спорил с этой рыжей."
            un "И я знаю — что на кону!"
            show un sad pioneer at center with dissolve
            un "Ты не понимаешь, что никому такая победа не нужна? А тебя завтра… на весь лагерь…"
            me "А ты правда думаешь, что мне не плевать? Пусть говорит что хочет. Я сделал так, как считал правильным."
        else:
            show un angry pioneer with dissolve
            un "Что ты наделал?"
            "Она приподнялась было над столом и тут же упала обратно."
            un "Зачем? Кому нужна такая победа…"
            me "Мне?"
            th "Она такая симпатичная, когда сердится."
        "А она хлопнула ладонью по столу, да так, что на секунду все смолкли и обернулись на неё."
        un "Кому нужна такая победа…"
        "Повторила она."
        me "Эта победа была нужна мне."
        "В гробовой тишине произнёс я."
        show un serious pioneer with dissolve
        me "Просто для того, чтобы указать кое-кому, что не всё решают угрозы или шантаж."
        me "Наслаждайся вечером."
        "Я кивнул и вышел из-за стола, оставляя Лену беззвучно хватать ртом воздух."

    elif alt_my_rival_1_tour.take == 'sl':
        show sl smile pioneer with dspr
        sl "Семён, если ты захочешь сыграть ещё раз, я не против."
        "Забавная девочка, готова даже поступиться собственной победой."
        th "Нет уж, сегодня моя очередь быть благородным."
        "Я наклонился над столом и произнёс:"
        me "Желаю тебе удачи в полуфинале!"
        sl "Но я же просто за компанию играть села!"
        sl "Я вообще карты не люблю."
        show sl sad pioneer with dissolve
        me "А что поделаешь. {w}Записалась — так действуй до конца!"
        me "К тому же, мне очень хочется, чтобы сегодня ты победила. Сумеешь?"
        "Славя неуверенно кивнула, а я поднялся и показал ей большой палец."
        "Чуточку уверенности в себе вне привычной сферы обитания — вот что ей нужно."

    elif alt_my_rival_1_tour.take == 'dv':
        if alt_day2_dv_bet_approve:
            show dv grin pioneer2 with dspr
            dv "Ну что, ты уже приготовился?"
            "Она упивалась моментом."
            if alt_day2_walk == 0:
                th "Мда, и стоило карты метить, если они мне не помогли?"
            else:
                pass
            me "К чему?"
            dv "Как к чему? К рассказу о том, куда смотрел, за что трогал."
            dv "Очень интересный рассказ будет, чувствую!"
            show dv laugh pioneer2 with dspr
            dv "Но ладно."
            me "Да?"
            "Я аж приподнялся на месте."
            th "Неужели передумала!"
            show dv smile pioneer2 with dissolve
            dv "Я расскажу всё в финале, когда меня будут приветствовать как победителя!"
            "Да, зря надеялся."
            "Это же Двачевская, в конце-то концов!"
            th "Ничего хорошего от неё ожидать нельзя."
        "Но я постарался сохранить лицо."
        "Я вежливо встал и наклонил голову:"
        me "Поздравляю тебя с победой."
        me "И удачи в полуфинале."
        "Развернулся и ушёл к болельщикам."
        th "Может быть, удастся затеряться в толпе?"

    elif alt_my_rival_1_tour.take == 'mi':
        show mi surprise pioneer with dspr
        #внимание: имеются ввиду диалоги в конце файла (они отвечают за фразы при неокончательных результатах, например, после первой победы в серии).
        # Диалог ниже как раз похож на первую победу Мику в серии (за исключением последних двух строк). Поэтому предлагается этот отрывок перенести,
        # а здесь написать новый (когда Мику победила в серии 2-1 или 2-0)
        mi "Ой!"                                                        # может,  в диалоги игры, когда Мику выиграла в 1-й раз?
        mi "А что означает это сочетание карт?"
        me "Твою победу."
        "Вежливо пояснил я."
        mi "Мою победу? Правда? А над кем?"
        "Иногда я не мог понять, серьёзна она или шутит."
        th "Мы не слишком долго знаем друг друга, надеюсь, со временем будем понимать лучше."
        me "Надо мной, Мику."
        show mi happy pioneer with dspr
        mi "Ой, какое счастье! А то мне никогда-никогда не везло в картах, я и решила, что это не моё, а тут попросили, я и согласилась."
        mi "Я даже не думала, что сумею победить! А ты не обижаешься? А то хочешь, переиграем, мне не жалко! Нет, правда-правда не обижаешься?"
        show mi smile pioneer with dissolve
        mi "Просто я не хочу, чтобы мне было хорошо за счёт других, это плохо, мне всегда Па говорил, что счастья на чужих слезах не построишь."
        me "Всё в порядке. Ты здорово играешь, поэтому и победила."
        me "Удачи тебе в полуфинале."
        "Пожелал я и, отвернувшись, удалился."

    elif alt_my_rival_1_tour.take == 'us':
        if alt_day2_dv_bet_approve:
            show us laugh pioneer
            us "Хы! А ты всё-таки продул!"
            "Спасибо, кэп."
            th "Это обязательно орать тут на всю столову, правда?"
            me "Ты тоже заметила, да?"
            us "Я думала придумать чего бы такого тебе припомнить, но вспомнила, что ничего о тебе не знаю."
            if alt_day2_us_escape:
                us "Ну разве что только то, что с тобой не скучно."
            us "Хочешь, ещё сыграем? {w}На просто так."
            show us grin pioneer with dspr
            us "Пока остальные тормозят, как раз партию успеем. Ну что?"
            me "Спасибо, но, наверное, нет."
            show us dontlike pioneer with dissolve
            us "Зануда! {w}И что, даже отыграться не хочешь?"
            "Отыграться? О чём это она?"
            us "Неужели не обидно проиграть девчонке?"
            me "Да мне фиолетово, на самом-то деле. "
            th "Кто там что думает и решает, остаётся его достоянием."
        "Мудрый совет на все случаи жизни: болтать поменьше."
        us "Зануда! {w}Зануда."
        "Кричала она."
        "А потом резко вскочила и пошла к столику, отведённому под следующую игру. "
        us "Просто ты проигравший и тебе неприятно!"
        show us normal pioneer with dissolve
        me "Да, возьми меня ещё раз на «слабо», детка."
        me "Наслаждайся вечером."
        "Я отправился в сторону толпы зрителей. Пришёл мой черёд сменить амплуа."

    elif alt_my_rival_1_tour.take == 'sh':
        show sh normal pioneer with dissolve
        sh "Это была достойная игра. Спасибо."
        "Он протянул мне руку, которую я с достоинством пожал."
        sh "А я пошёл дальше громить вражеские порядки."

    elif alt_my_rival_1_tour.take == 'mz':
        show mz normal pioneer with dissolve
        "Женя пожала плечами и встала из-за стола."
        mz "Похоже, это будет ещё проще, чем мне казалось."
# ............................................ \\диалоги

    scene bg int_dining_hall_sunset
    window show
    "А ситуация, между тем, складывалась следующая:"
    window hide
    $ renpy.pause(.5)
    call alt_day2_1_tour_analizer                                                   # Вызов анализатора 1 раунда
    $ renpy.block_rollback()                                                          # блокируем роллбак
    stop ambience
    stop music fadeout 3
    window hide
    $ alt_drawing_of_detour()                                                       # вызываем рандомизатор пропуска полуфинала и финала
    $ renpy.fix_rollback()                                                          # фиксируем выбор — "откатом" поменять будет нельзя
    jump alt_day2_semifinal_new                                                     # переход в полуфинал ?
#------------------------------------------------------------------------------------------------
label alt_day2_participate_win_end_new:
    $ alt_day2_result_tour = 2                                              # Семён выиграл в 1 туре
    if not alt_day2_detour_semifinal:                                       # если не "выигрыш" в 1 туре скипом
        $ persistent.altCardsWonRivals_new[alt_spr_my_rival] = True         # Выиграли у этого соперника
    $ persistent.altCardsWon1_new = True
    $ alt_day2_gamblers_1_tour[places_my_table[0]].winner = True            # Семён выиграл
    $ alt_tournament_state = "1_round_end"                                  # устанавливаем конец 1-го раунда
    
# ------------------------------------------------------------------------- 
# ЕСЛИ Славя, Мику или Шурик и НЕ скип тура — итоги ДО диалогов
    if (alt_my_rival_1_tour.take in ['sl','mi','sh']) and not alt_day2_detour_semifinal:
        scene bg int_dining_hall_sunset
        window show
        "Первый тур закончился."
        "Ситуация, между тем, складывалась следующая:"
        call alt_day2_1_tour_analizer                                                   # вызываем анализатор 1 тура
        $ renpy.block_rollback()                                                          # блокируем роллбак
# ------------------------------------------------------------------------- 
    $ renpy.pause(1)
    scene bg int_dining_hall_sunset
    window show
    call alt_day2_summary_poker_round                                           # подводим итоги раунда                                
    
# ............................................ ДИАЛОГИ
    if alt_my_rival_1_tour.take == 'un':
        #внимание: аналогично верхнему
        "У Лены не было ничего."                                                # и этот кусочек может в диалоги игры
        "А с тем, что было, я бы постеснялся открывать карты."
        "Бедная девочка."
        "Она сидела, будто сама не способная поверить в то, что только что произошло."
        if lp_un >= 6 and not alt_day2_detour_semifinal:
            menu:
                "Матч-реванш":
                    $ karma += 5
                    $ alt_day2_revanche = True
                    $ lp_un += 1
                    if loki:
                        "Я дёрнул рукой, и карты посыпались на пол."
                        me "Эй, погодите!"
                        show el normal pioneer far at left
                        el "Что случилось?"
                        me "Да карты упали. Партия не засчитана, давай ещё одну."
                    else:
                        me "Неудачная партия."
                        un "Да…"
                        me "Может, ещё разок?"
                        show el normal pioneer far at left
                    el "Я же сказал — никаких переигровок!"
                    me "А это не переигровка, это… Это… Фальстарт!" # Лучше такая капитализация: «А это не переигровка, это… это… фальстарт!», но не обязательно.
                    "Он неприязненно посмотрел на меня."
                    el "Ладно, давайте ещё раз!"
                    hide el with dissolve
                    window hide
                    $ alt_day2_my_win = alt_day2_rival_win = alt_day2_game_played_out = 0           # обнуляем результат турнира — если реванш
                    jump alt_day2_tournament_start_new
                "Ничего не делать":
                    pass
        else:
            pass
        $ lp_un -= 1
        $ lp_dv += 1
        "Я улыбнулся."
        me "Спасибо за игру!"
        un "Н-не за что."
        "Она встала из-за стола и исчезла за болельщиками."
        hide un with dissolve
        
#внимание:
# TODO — пропуск диалогов — надо, если надо — где ???
# ====================================================== ОТСЕБЯТИНА. Пропускаем часть диалога, если "выиграли" 1 тур скипом
        if not alt_day2_detour_semifinal:
# =======================================
        
            "А я не мог сдержать ликования."
            th "Я подебил! То есть, я победил."
            dreamgirl "Ура! {w=.4}У девочки. {w=.4}В игру, которую ни ты, ни она не знаете. {w}Велико достижение."
            th "Заткнись, внутренний голос."
            th "Я буду радоваться победе так, как буду радоваться только в финале, когда раскатаю эту рыжую нахалку с сухим счётом!"
            dreamgirl "Нет, ну ты и правда герой. Спору нет."
            dreamgirl "Может, следовало дать девочке выиграть? Она и так выглядит не самой счастливой, а ты выбил из-под неё остатки почвы."
            dreamgirl "И как оно по ощущениям? Стоило того?"
            th "Я сказал  — заткнись."
            show blinking with dissolve
            "У меня цель не ободрить каждого сирого, а утереть нос одной рыжей зазнайке!"
            "Хотя, честно сказать, искушение слить партию просто для того, чтобы посмотреть, как она выполнит свои угрозы, достаточно велико. {w}Нет, ну серьезно!"
            scene bg ext_square_sunset
            show prologue_dream
            with fade
            window show
            "Завтра мы встаём, идём на линейку, а там уже на трибуне, между Ольгой Дмитриевной и Славей, стоит она."
            show dv grin pioneer2 with diam
            "И своим вредным голосом говорит — так, мол, и так, некий Семён, приехать в лагерь ещё не успел, как пошёл подглядывать за мной, и даже полапал немного."
            "Да это же реклама такая, что я за неё ещё и приплачивать должен!"
            "В духе «Сёма едет! Прячьте девок!»."
            hide dv with dissolve
        window hide
        scene bg int_dining_hall_sunset with dissolve

    elif alt_my_rival_1_tour.take == 'sl':
        "Славя резко вскочила и оперлась кулаками о стол."
        show sl serious pioneer with dspr
        sl "А ты серьёзный противник."
        "Исподлобья процедила она."
        show sl angry pioneer with dspr
        sl "Напомни мне никогда не недооценивать тебя!"
        me "Многие, кто недооценили Семёна, горько пожалели об этом!"
        "Подыграл я."
        "Тут она не выдержала и разулыбалась, испортив всю сценку."
        show sl smile2 pioneer with dspr
        sl "А партия действительно была интересная!"
        if lp_sl >= 6 and not alt_day2_detour_semifinal:
            menu:
                "Хочешь ещё разок?":
                    $ karma += 5
                    show sl smile pioneer with dspr
                    sl "Спасибо"
                    $ lp_sl += 1
                    show sl laugh pioneer with dspr
                    extend ", но… Нет!"
                    sl "Давай-ка ты сам покажешь класс!"
                    "Девочка потрепала меня по плечу и направилась в стан болельщиков."
                    hide sl with dissolve
                    jump alt_day2_semifinal_new
                "Ничего не делать":
                    pass
        else:
            pass
        "Я улыбнулся."
        me "Спасибо за игру!"
        sl "Тебе спасибо!"
        "Кивнув мне, она поднялась и отошла к Ольге Дмитриевне, и у них там завязалась оживлённая беседа."
        hide sl with dissolve
        
# ====================================================== ОТСЕБЯТИНА. Пропускаем часть диалога, если "выиграли" 1 тур скипом
        if not alt_day2_detour_semifinal:
# =======================================

            "Что ж, это была трудная схватка, но я победил."
            th "Идеальное же противостояние, игра в которой вы оба ничего не понимаете."
            dreamgirl "Ну да, ну да."
            "Пробормотал внутренний голос."
            dreamgirl "Носкиллер рандомный."
            th "Помолчи. Ты ничего не понимаешь."
            th "Это вопрос индивидуального престижа. {w}Я буду двигаться в финал."
            #внимание: далее идёт текст авторства тов. nuttyprof
            if alt_result_dv_1_tour == 4:                                                       # Дваче в другом полуфинале, если в 1/2 с Семёном — как-то не того...
                extend " И раскатаю там рыжее хамло с нулевым счётом."                          # добавлено по логике, править
            elif alt_result_dv_1_tour == 3:                                                              # Дваче в 1/2 к Семёну
                extend" И раскатаю там соперника с нулевым счётом."                               # добавлено по логике, править
            elif alt_result_dv_1_tour == 2:                                                         # Дваче слетела в 1 туре 
                extend" И раскатаю там соперника с нулевым счётом."                               # добавлено по логике, править
            dreamgirl "Надежды… Мечты… Фантазии…"
            th "Ты что, сомневаешься во мне?!"
            dreamgirl "Нет-нет-нет, ты что! {w}Я в тебя верю! Я знаю твой потенциал."
            th "Вот видишь!"
            dreamgirl "Ты слетишь на полпути."
            th "Да ну тебя!"
            if alt_result_dv_1_tour == 4:                                                                # Дваче в другом полуфинале
                "Может быть, это {i}она{/i} слетит на полпути!"
                "Вот возьмёт и проиграет."
                dreamgirl "Надежды… Мечты…"
                th "Ты повторяешься."
                dreamgirl "Просто ты слишком нос задираешь. {w}А настоящий мастер лишён гордыни."
            elif alt_result_dv_1_tour == 3:                                                              # Дваче в 1/2 к Семёну
                th "Между прочим, у нас сейчас как раз будет шанс стреножить Рыжевскую в полуфинале."
                dreamgirl "Ну да, это нам, конечно, повезло."
                dreamgirl "Но лучше приготовься к суровому испытанию — просто так она тебе победу не отдаст!"
            elif alt_result_dv_1_tour == 2:                                                                 # Дваче слетела в 1 туре 
                "Я усмехнулся."
                th "А даже если и слечу."
                th "Обращаю твоё внимание, что пока мы тут препирались, Двачевская изволила вылететь в самом первом раунде."
                "Я снял воображаемую шапку и прижал её к груди."
                me "Помянем!"
                "Двачевская оскалилась, но ничего не сказала."

    elif alt_my_rival_1_tour.take == 'dv':
        show dv sad pioneer2 with dspr
        "Алиска облажалась."
        "Ха. Ха. Ха."
        "Её вид — это то, что не купишь ни за какие мастеркарды с визами."
        "Поистине бесценное зрелище!"
        
# ====================================================== ОТСЕБЯТИНА. Пропускаем часть диалога, если "выиграли" 1 тур скипом
        if not alt_day2_detour_semifinal:
# =======================================
        
            if lp_dv >= 6:
                menu:
                    "Ну что, как я тебя?":
                        $ karma += 5
                        if loki or herc:
                            $ lp_dv += 1
                            show dv rage pioneer2 with dspr
                            "Алиса надулась, набычилась…"
                            me "Разделал как Рандом черепаху!"
                            "Не удивлюсь, если она сейчас придумает ещё какую-нибудь гадость, только чтобы уязвить меня."
                            show dv angry pioneer2 with dspr
                            "Но она меня удивила."
                            show dv laugh pioneer2 with dspr
                            dv "А ты хорош! Хорош!"
                            "Расхохоталась она, ткнув меня кулаком в плечо."
                            dv "Пожалуй, будем считать наше пари закрытым."
                            th "Уффф."
                            "Я подавил желание облегчённо вытереть лоб."
                            show dv grin pioneer2 with dspr
                            dv "А то если хочешь, можем ещё на что-нибудь поспорить?"
                            "Я отшатнулся."
                            "Но постарался ответить солидно:"
                            me "Нет. {w}Свою натюрель ты уже поставила на кон."
                            dreamgirl "Дальше только честь девичья! {w}Ну-ка, скажешь это вслух?"
                            "Ага, сейчас. У меня и «натюрель»-то вышла дрожащим голосом."
                            "Алиса снова рассмеялась, увидев мою реакцию, и поднялась."
                            show dv smile pioneer2 with dspr
                            dv "Удачи тебе."
                        else:
                            "Начал было я, и, чувствуя, как запал иссякает, продолжил уже куда спокойнее:"
                            me "Кажется, я победил."
                            dv "Угу."
                            me "И ты теперь…"
                            show dv sad pioneer2 with dspr
                            $ renpy.pause(.4)
                            show dv guilty pioneer2 with dissolve
                            dv "Да…"
                            dv "Никому я ничего не скажу. {w}Ты победитель."
                            "Алиса выглядела подавленной и какой-то… Обескураженной, что ли."
                            "Кажется, её смутил не столько проигрыш, сколько моя на него реакция."
                            dv "Ладно, бывай."
                        hide dv with dissolve
                        window hide
                        jump alt_day2_1_tour_end
                    "Партия":
                        "Алиса кивнула и молча поднялась из-за стола."
                        pass
            else:
                pass
        "Кажется, свою малюсенькую проблему с пари я только что успешно решил."

    elif alt_my_rival_1_tour.take == 'mi':
        show mi upset pioneer with dspr
        mi "Ой!"
        "Она прижала руки ко рту."
        mi "Я что, я проиграла, да? А то я так и не поняла, что тут делать, только таскала у тебя карты, и не отдавала тебе свои."
        "Она покачала головой."
        mi "Какая-то непонятная игра."
        show mi smile pioneer with dspr
        mi "Но всё равно, спасибо, что играл со мной!"
        if lp_mi >= 6 and not alt_day2_detour_semifinal:
            menu:
                "Может, ещё?":
                    $ karma += 5
                    $ lp_mi += 1 
                    "Мне понравилось просто сидеть с ней за одним столом."
                    "Тем более, что на нас всё равно никто не смотрел."
                    "Внимание зала сфокусировалось на основных действующих лицах сегодняшнего вечера — Алисе и Ульяне."
                    me "Давай?"
                    show mi shy pioneer with dspr
                    mi "А разве так можно?"
                    me "Нет, но… Кому какое дело?"
                    show el serious pioneer at left with dissolve
                    el "Мне есть дело!"
                    "Ответил появившийся из ниоткуда Электроник."
                    el "Ты победил, пожалте за полуфинальный столик!"
                    hide el with dissolve
                    "Блин."
                    "Моя улыбка вышла извиняющейся."
                    me "Тогда увидимся."
                "Всегда рад":
                    "Я улыбнулся."
                    me "Если вдруг захочешь ещё как-нибудь сыграть, обращайся!"
            "Мику кивнула и встала из-за стола."
        else:
            $ lp_mi -= 1
        "Я улыбнулся."
        me "Всегда пожалуйста!"
        mi "Я пойду, ладно? Хочу увидеть, как ты будешь побеждать! Ты же будешь побеждать, правда? Я буду очень-очень за тебя болеть!"
        "Не в силах сдержать улыбку, я кивнул."
        me "Конечно же, буду."
        mi "Тогда удачи тебе дальше!"
        "Она ушла."
        hide mi with dissolve
        
# ====================================================== ОТСЕБЯТИНА. Пропускаем часть диалога, если "выиграли" 1 тур скипом
        if not alt_day2_detour_semifinal:
# =======================================
        
            "Не могу сказать, что пришлось потрудиться."
            "По мне, так это было чистое везение."
            "Хотя, конечно, моя карма и везение — это слова-антонимы."
            "Я — ходячее олицетворение закона Мэрфи."
            dreamgirl "Ну да, ну да. {w}А то, что ты вытянул билет даже не на миллион, а на новую жизнь, это мы в расчёт как бы не берём, да?"
            th "Ты о попадании в лагерь? "
            th "Я не могу назвать это везением в прямом смысле этого слова."
            dreamgirl "А как это ещё назвать?"
            th "Ну… Просто оказался в ненужном месте в ненужное время."
            dreamgirl "И получил полон рот молодости, лета и сексапильных пионерок."
            th "Знаешь, я не верю, когда много хорошо. {w}Обязательно где-то должен быть подвох."
            dreamgirl "И какой в этот раз?"
            th "Ну, например, может оказаться, что перенос в лагерь является побочным эффектом от попадания под луч космической энергии."
            th "Или вообще это спецслужбы тестировали прототип телепортатора, и у них что-то сбилось в настройках."
            dreamgirl "Не знаю, что ты употребляешь, но отсыпь немного. {w}К тому же, у тебя тут эротическое пари, помнишь?"
            if alt_result_dv_1_tour == 4:                                                                   # Дваче в другом полуфинале
                th "Помню, помню."
                "Но у этого пари все шансы разрешиться совершенно самостоятельно."
                dreamgirl "Надежды вьюношей питают…"
                th "Не науки разве?"
                dreamgirl "В твоём случае именно надежды."
                dreamgirl "Будь уверен, она доберётся до тебя и порвёт на мелкие клочки, а потом исполнит свою угрозу."
                th "О, спасибо тебе, мрачный зануда."
            elif alt_result_dv_1_tour == 3:                                                                 # Дваче в 1/2 к Семёну
                th "Забудешь тут."
                "Судя по графику, моим противником в полуфинале выступает как раз Двачевская."
                dreamgirl "Вот свезло так свезло!"
                dreamgirl "Давай сделаем ей больно!"
            elif alt_result_dv_1_tour == 2:                                                                  # Дваче слетела в 1 туре
                "Это было бы даже смешно."
                th "Пари? Какое пари?"
                th "Пока мы тут о везении судачили, Алиску вышибли на первом же кону."
                "Я снял воображаемую шапку и прижал её к груди."
                me "Помянем!"
                "Двачевская оскалилась, но ничего не сказала."

    elif alt_my_rival_1_tour.take == 'us':
        if alt_day2_revanche:
            show us angry pioneer with dissolve
            us "Эй! "
            show us dontlike pioneer with dspr
            extend "Так нечестно! "
            us "Ты должен был поддаться и проиграть, ты обещал!"
            "Она надулась и топнула ногой, явно расстроенная."
            th "Дуется, как мышь на крупу."
            "Я с трудом сдерживал смех."
            me "Всё, тебе дали шанс, ты его проморгала. Брысь."
            "Она надулась и ушла."
            "А я остался наслаждаться своей победой."
            hide us with dissolve
            jump alt_day2_1_tour_end
        else:
            show us sad pioneer with dspr
            us "Так нельзя, я только разыгрываться начала!"
            me "Я тоже. {w}Ты проиграла, я победил. Всё честно."
            us "Переиграем! Только ты теперь поддавайся, слышишь?"
            us "Я должна победить и забрать главный приз!"
            show el serious pioneer at left with dissolve
            "Её крики привлекли внимание Электроника."
            el "Никаких переигровок!"
            el "Один матч, три раунда, проигравший выбывает."
            hide el with dissolve
            "Ульяна и бровью не повела."
            show us angry pioneer with dspr
            us "Ты должен проиграть! Должен! Понял! "
            "Ещё немного, и начну хохотать в голос, настолько потешно это выглядело."
            
# ====================================================== ОТСЕБЯТИНА. Пропускаем часть диалога, если "выиграли" 1 тур скипом
            if not alt_day2_detour_semifinal:
# =======================================
            
                if alt_day2_us_escape:
                    us " Ах так! Да я тогда… Я тогда завтра снова сбегу, понял!"
                    us "И чисти тогда свою картошку сам! На весь лагерь!"
                    "А вот эта угроза была уже посерьёзнее, дежурить по столовой одному мне совершенно не улыбалось."
                else:
                    us "Ах так! Тогда я всем расскажу про тебя и Двачевскую!"
                    if alt_day2_dv_bet_approve and (loki or herc):
                        me "Мелкая нахалка, не смей! Это только наш с ней спор, ты только разрубала!"
                        "Ульяна только улыбнулась."
                    else:
                        me "Ты всем расскажешь то, что она обещала рассказать? В случае моего проигрыша?"
                        "Она кивнула."
                if herc or loki:
                    menu:
                        "А тебе не надо горячего шоколада?":
                            show us surp1 pioneer with dspr
                            us "Что?"
                            me "Я говорю, можешь делать как хочешь, но ты проиграла."
                            me "А карточный долг священен. Всё, брысь отсюда, я к победе иду."
                            "Она надулась, но сделала, как я сказал."
                            hide us
                            with flash_red
                            "Правда, попутно наступила мне на ногу — пускай."
                            "Я был благодушен и простил ей эту маленькую шалость."
                            jump alt_day2_1_tour_end                                                 # В ПОЛУФИНАЛ
                        "Ладно. Как хочешь":
                            $ lp_us += 1
                elif not alt_day2_revanche:
                    "Я вздохнул."
                    me "Уговорила. Дам тебе ещё один шанс."
                else:
                    me "Я крепко об этом пожалею, но…  Рассказывай."
                    "Я поднялся из-за стола."
                    jump alt_day2_1_tour_end                                                 # В ПОЛУФИНАЛ
                window hide
                $ alt_day2_revanche = True
                $ alt_day2_my_win = alt_day2_rival_win = alt_day2_game_played_out = 0                   # обнуляем результат турнира — если реванш
                jump alt_day2_tournament_start_new                                                      # НА ПЕРЕИГРОВКУ
            else:
                me "Можешь делать как хочешь, но ты проиграла."
                me "А карточный долг священен. Всё, брысь отсюда, я к победе иду."
                "Она надулась, но сделала, как я сказал."
                hide us
                with flash_red
                "Правда, попутно наступила мне на ногу — пускай."
                "Я был благодушен и простил ей эту маленькую шалость."

    elif alt_my_rival_1_tour.take == 'sh':
        "Шурику не повезло."
        "Но, похоже, его больше интересовал сам процесс проверки новых правил и алгоритмов, чем победа."
        "Настоящий фанатик своего дела."
        show sh normal pioneer with dspr
        sh "Ты очень хорошо умеешь приспособиться к новым правилам игры."
        "Похвалил он."
        "И, пожав мне руку, удалился."
        hide sh
        
# ====================================================== ОТСЕБЯТИНА. Пропускаем часть диалога, если "выиграли" 1 тур скипом
        if not alt_day2_detour_semifinal:
# =======================================
        
            "Наверное, отправился изобретать очередную дикую штуку или строчить очерк об оной в стенгазету."
            "Я с удивлением поймал себя на мысли, что нахожу Шурика и Славю очень похожими."
            "Оба увлечены своим делом, оба дико ответственные."
            "И оба почти не отдыхают."
            th "Наверное, стоило бы сдать партию, я раздолбай, я и так способ ляжки потянуть найду, а он, похоже, сейчас обратно сидеть в клуб."
            "Так и лето пройдёт, а он всё будет бледным."
            dreamgirl "Эй!"
            th "Что?"
            dreamgirl "Это у тебя там что за гадость? {w}Совесть? {w}Выброси её немедленно."
            dreamgirl "Вечно всякую дрянь с пола поднимаешь."
            th "Что такое?"
            dreamgirl "Напоминаю, что мы не просто так тут штаны просиживаем."
            dreamgirl "У нас есть одна цель! Показать одной рыжей террористке, чего стоит слово!"
            if alt_result_dv_1_tour == 4:                                                           # Дваче в другом полуфинале
                dreamgirl "И особый воспитательный момент несёт то, что мы умоем её в игре по её же правилам!"
                th "Если она проиграет за другим столом, то никого мы не умоем."
                dreamgirl "Есть подозрение, что такие, как она, так просто не сдаются."
                th "Ну, если встимся в финале, я её обыграю."
                dreamgirl "С таким настроем ты никого не обыграешь. {w}Соберись!"
            elif alt_result_dv_1_tour == 3:                                                         # Дваче в 1/2 к Семёну
                th "Ага, прямо сейчас и покажем."
                dreamgirl "Здорово! Расправа оказалась куда ближе, чем мне казалось!"
                dreamgirl "Она просила сделать ей посопротивляться, исполни её просьбу."
            elif alt_result_dv_1_tour == 2:                                                         # Дваче слетела в 1 туре
                "Заниматься оценками слов, честно говоря, было уже поздновато."
                "Я посмотрел на таблицу участников — Алиса вылетела после первой же партии."    
                th "Не{w=.3} по{w=.2}вез{w=.3}ло."
                th "Покойся с миром, дорогая бандитка."
                th "Я отомщу за тебя."

    elif alt_my_rival_1_tour.take == 'mz':
        "Библиотекарше не повезло."
        "Похоже, что там совсем грустно всё было в плане опыта игры в карты."
        "Ну и правильно, с кем руку-то набьёшь, если твой лучший друг — это даже не книга."
        "А подушка."
        "Буркнув нечто невразумительное, она поднялась и исчезла."
# ............................................ \\диалоги

    
# -------------------------------------------------------------------------
label alt_day2_1_tour_end:
# ЕСЛИ НЕ Славя, Мику или Шурик ИЛИ при скипе — итоги после диалогов
    if (alt_my_rival_1_tour.take not in ['sl','mi','sh']) or alt_day2_detour_semifinal:
        scene bg int_dining_hall_sunset
        window show
        "Первый тур закончился."
        "Ситуация, между тем, складывалась следующая:"
        call alt_day2_1_tour_analizer                                                       # вызываем анализатор 1 тура
        $ renpy.block_rollback()                                                          # блокируем роллбак
    scene bg int_dining_hall_sunset with dissolve
    stop ambience
    stop music fadeout 3
# -------------------------------------------------------------------------    

    "Ладно, это всё лирика."
    jump alt_day2_semifinal_new                                             # переход в полуфинал
    
#-------------------------------------------------------------------------------------------------
label alt_day2_semifinal_new:
    scene bg int_dining_hall_sunset
    window show
    show el smile pioneer at left with dissolve
    el "Итак!"
    "Подал голос Электроник, явно гордящийся своей ролью мастер-церемонимейстера."
    el "Первый тур окончен, победители встречаются во втором туре!"
    
    $ alt_tournament_state = "semifinal_start"                                                      # устанавливаем начало полуфинала
#-------------------------------------------------------------------------------------------------
    if alt_day2_result_tour != 1:                                                                       # если не продули в 1 туре
        $ alt_day2_my_win = alt_day2_rival_win = alt_day2_game_played_out = 0                           # обнуляем результат игр
        $ alt_my_rival_semifinal = alt_get_me_rival(alt_day2_gamblers_semifinal)                        # узнаём своего соперника
    
        $ alt_name_my_rival_i = alt_my_rival_semifinal.name['i']                                        # узнаём ИМЯ своего соперника (в именительном падеже)
        $ alt_name_my_rival_r = alt_my_rival_semifinal.name['r']                                        # узнаём ИМЯ своего соперника (в родительном падеже)
        $ alt_name_my_rival_d = alt_my_rival_semifinal.name['d']                                        # узнаём ИМЯ своего соперника (в дательном падеже)
        $ alt_name_my_rival_v = alt_my_rival_semifinal.name['v']                                        # узнаём ИМЯ своего соперника (в винительном падеже)
        $ alt_name_my_rival_t = alt_my_rival_semifinal.name['t']                                        # узнаём ИМЯ своего соперника (в творительном падеже)
    
        $ alt_spr_my_rival = alt_my_rival_semifinal.take                                                # получаем спрайт соперника — заголовок
        $ alt_emo_my_rival = alt_sprites_rival_recognition[alt_spr_my_rival][0]                         # эмоция (строка)
        $ alt_clot_my_rival = alt_sprites_rival_recognition[alt_spr_my_rival][1]                        # одежда (строка)
        $ alt_pos_my_rival = alt_sprites_rival_recognition[alt_spr_my_rival][2]                         # положение
    
        $ alt_nick_my_rival = alt_my_rival_semifinal.nick                                               # получаем характер соперника (для диалога)

        if alt_my_rival_1_tour.take == 'un':
            "Лена, оказывается, никуда не ушла, она просто стояла скромно и явно собиралась следить за событиями до самого финала."
            show un smile2 pioneer far at left
            "При этом на лице её не было ни злости, ни обиды, ни чего-либо в этом духе."
            "Напротив, в её глазах горел… Азарт!"
            "При этом — азарт болельщика."
            hide un with dissolve
            "Что ж, убедившись в том, что не обидел её, я немного расслабился."
    "Между тем, в таблице уже появились имена участников второго тура."
    call show_tournament_table                                                                      # "показали таблицу"
    $ alt_mstt = 0
    if alt_day2_result_tour != 1:                                                                       # если не продули в 1 туре
        $ places_my_table = alt_get_my_table(alt_day2_gamblers_semifinal)                               # Стол Семёна = [место Семёна, место соперника, № их стола]
    else:                                                                                               # продули в 1 туре
        $ alt_table_no = 5
    "И если верить этой таблице, то в полуфинале встречаются четыре игрока."
    $ alt_random_box_1 = range(1,len(alt_table_affiliation)+1)                                      # черный ящик — список от 1 до длины представлений столов +1
    while alt_table_no <= 6:                                                                        # перебираем столы от 5 по 6
        $ sitting_at_table,gambler_upper,gambler_lower,must_taunt = alt_declare_tournament_tables(alt_table_no)  #расссадка, игроки, таунты — по номеру стола
        "%(sitting_at_table)s"
        call show_tournament_table
        extend " %(gambler_upper)s"                                                                 # выводим в окно имя верхнего игрока
        call show_tournament_table
        extend " и %(gambler_lower)s."                                                              # выводим в окно имя нижего игрока
        if must_taunt != None:                                                                      # если таунт есть
            "%(must_taunt)s"                                                                        # выводим его
        if alt_day2_result_tour != 1:                                                                       # если не продули в 1 туре
            if alt_table_no != places_my_table[2]:                                                          # если номер стола — НЕ свой
                $ alt_day2_gamblers_semifinal[2*(alt_table_no-4)-renpy.random.choice([1,2])].winner = True  # тогда один из игроков (рандомно) — победитель в этапе
                $ renpy.block_rollback()
        $ alt_table_no += 1
        
    if alt_day2_result_tour == 1:                                                               # если продули в 1 туре
        $ alt_tournament_state = "semifinal_end"                                                # устанавливаем конец полуфинала
        $ alt_drawing_of_detour_semifinal()
        $ renpy.fix_rollback()                                                                  # фиксируем выбор — "откатом" поменять будет нельзя
        jump alt_day2_semifinal_detour                                                          # и переходим в конец проигрыша в 1/2

    scene bg int_dining_hall_sunset
    window show
    "За стол полуфиналиста посадили моего оппонента."
    
# .......................................... ДИАЛОГИ
    if alt_my_rival_semifinal.take == 'un':
        "Им оказалась Лена."
        show un shy pioneer with dspr
        me "Удачи нам обоим?"
        show un smile pioneer with dspr
        $ renpy.pause(.3)
        show un shy pioneer with dspr
        un "Д-да..."
        "Она попыталась улыбнуться, но тут же снова смешалась и смолкла."
        
    elif alt_my_rival_semifinal.take == 'sl':
        "Славю."
        show sl smile pioneer with dspr
        sl "Ух! Не думала, что так далеко зайду!"
        "Улыбнулась она."
        me "Это не значит, что я теперь буду тебе поддаваться!"
        show sl laugh pioneer with dspr
        sl "И не надо!"
        "Рассмеялась девочка."
        sl "Пускай победит сильнейший!"
        
    elif alt_my_rival_semifinal.take == 'dv':
        "Алиса? Надо же, какая встреча."
        show dv grin pioneer2 with dspr
        dv "Я придумала новое правило."
        "Прошептала она, наклонившись ко мне."
        me "Какое ещё правило?"
        dv "Если ты меня победишь сейчас, но проиграешь в финале — я всё равно всё всем расскажу."
        me "Эй, так нечестно!"
        show dv laugh pioneer2 with dspr
        dv "Хотя ты не победишь."
        "Рассмеялась девочка."
        dv "Тебе конец!"

    elif alt_my_rival_semifinal.take == 'mi':
        "Снова она."
        "Господи, куда от неё деться, куда ни пойду, она везде!"
        show mi smile pioneer with dspr
        mi "Ой, Сенечка, а я так и не разобралась в том, что нам говорили, просто тянула и тянула карты, а потом мне сказали, что я победила. Вот."
        mi "А ты понял, как в эту игру играть? А то если понял и вдруг захочешь, то у меня есть карты, мы могли бы потом попробовать ещё раз, только в этот раз, знаешь, чтобы все знали правила, ведь так интереснее!"
        th "Дуракам везёт, да?"
        show mi normal pioneer with dspr
        mi "Ой, а почему ты делаешь такое лицо, как будто я тебя смертельно утомила? Я же не специально, просто ты такой интересный, и всё время молчишь."
        th "Спокойствие. {w}Терпение — добродетель."
        "Мику говорила так, будто в её языке отсутствовали знаки препинания."
        "Но во время матча она сосредоточенно молчала — я отметил этот момент."
    
    elif alt_my_rival_semifinal.take == 'us':
        "Напротив меня уселась Ульянка."
        show us grin pioneer with dspr
        window show
        play music music_7dl["bureaucracy"] fadein 1
        us "Будешь поддаваться, будешь? "
        "С улыбкой до ушей она уставилась на меня."
        us "Я хочу всех победить!"
        me "Не буду."
        "Я отрицательно покачал головой."
        if alt_day2_dv_bet_approve:
            me "У нас же спор, помнишь?"
            if loki or herc:
                extend "Ты разбивала!"
            show us sad pioneer with dspr
            us "Спор — это да."
            us "Но играть будем по моим правилам!"
            me "Что бы это значило?!"
            show us laugh pioneer with dspr
        us "Просто я ничего не поняла и не запомнила."
        
    elif alt_my_rival_semifinal.take == 'sh':
        "Александр Трофимов. {w}Больше известный как Шурик за схожесть с одним киногероем."
        show sh normal pioneer with dspr
        sh "Это будет достойная схватка."
        "Кивнул он."
        me "Не думай, что я буду тебе поддаваться."
        show sh smile pioneer with dspr
        sh "И ты тоже не надейся!"
        me "Тогда к оружию!"
        
    elif alt_my_rival_semifinal.take == 'mz':
        "Жужу? Серьёзно? Как она победить-то умудрилась, с таким отношением к игре?"
        show mz normal pioneer with dspr
        mz "Слушай. Как там тебя."
        "Начала она."
        me "Семён."
        mz "А, вот. Семён."
        mz "Семён, хочешь, я скажу, что ты победил, и пойду уже?"
        me "А так разве можно?"
        mt "Нет, нельзя! Играйте давайте!"
        "Крикнула со стороны болельщиков вожатая."
        "Чертыхнувшись, Женя отказалась от своих планов.."
# .......................................... /ДИАЛОГИ

    window hide
# ----------------------------------------------------------------------------------------------------
    if alt_day2_detour_semifinal:                                           # если пропуск полуфинала
        scene bg int_dining_hall_sunset with dissolve2
        $ renpy.pause(1.0)
        if not alt_day2_detour_final:                                       # Если НЕ пропуск финала
            jump alt_day2_semifinal_fail_end_new                            # на поражение в 1/2 финала
        elif alt_day2_detour_final:                                         # Если выбрано "проиграть в финале"      
            jump alt_day2_semifinal_win_end_new                             # на победу в 1/2 финала
            
# ----------------------------------------------------------------------------------------------------
label alt_day2_semifinal_start_new:                                                     # начало полуфинала
    call alt_day2_stipulation_new                                                       # определяемся, кто первый ходит
    
    # первоначальные "настройки" игроков — могут меняться по результатам игры
    # 'defense' — защита, 'gamble' — риск, 'succumb' — слив, 'foolplay' — рандом
    # вероятность ошибки: 1 = 80%, .... 4 = 20%, 5 — ошибок нет.
    
    if alt_my_rival_semifinal.take == 'un':                                                    # В отличие от 1 тура....... 
        if not alt_day2_dv_bet_approve:                                                         # если с Алисой не спорить
            $ alt_day2_gambler_behavior = 'gamble'                                              # Лена пытается... рискнуть ? почему нет ?
            $ alt_day2_gambler_skill = 3                                                        # правда, ошибок многовато — 40%(3) 
        else:
            $ alt_day2_gambler_behavior = 'succumb'                                             # Если поспорить — то также игра в поддавки
            $ alt_day2_gambler_skill = 4                                                        # может ошибиться  — 20%(4)
    elif alt_my_rival_semifinal.take == 'sl':                                                  # Славя будет защищаться, ошибок — 40%(3)
        $ alt_day2_gambler_behavior = 'defense'
        $ alt_day2_gambler_skill = 3
    elif alt_my_rival_semifinal.take == 'dv':                                                  # Алиса рискует, ошибок — 80%(4)
        $ alt_day2_gambler_behavior = 'gamble'
        $ alt_day2_gambler_skill = 4
    elif alt_my_rival_semifinal.take == 'mi':                                                  # Мику будет защищаться, ошибок — 20%(4)
        $ alt_day2_gambler_behavior = 'defense'
        $ alt_day2_gambler_skill = 4
    elif alt_my_rival_semifinal.take == 'us':                                                  # Ульяна будет защищаться по-своему
        $ alt_day2_gambler_behavior = 'defense'
        $ alt_day2_gambler_skill = 3                                                            # ошибок — 40%(3)
    elif alt_my_rival_semifinal.take == 'sh':                                                  # Шурик экспериментирует, так что может и рискнуть, и защищаться, и слить; ошибки 20%(4)
        $ alt_day2_experiment = ['defense','gamble','succumb']                                  # у него своя кухня — набор из возможных вариантов
        $ alt_day2_gambler_skill = 4
    elif alt_my_rival_semifinal.take == 'mz':                                                  # Женя играет рандомно, как в классике, ошибки = 5
        $ alt_day2_gambler_behavior = 'foolplay'
        $ alt_day2_gambler_skill = 5

label alt_day2_semifinal_re_game:                                                           # игра в полуфинале — сюда возвращаемся на повторную игру 
    $ alt_my_poker_hand = None
    $ alt_rival_poker_hand = None

    if alt_day2_walk == 0:
        $ VISIBLE = True
        $ INVISIBLE = True
    else:
        $ VISIBLE = True
        $ INVISIBLE = False

    python:
        dialogs = {
                        (0, 'win','jump'):'alt_day2_one_play_win_new',
                        (0, 'fail','jump'):'alt_day2_one_play_fail_new',
                        (0, 'draw','jump'):'alt_day2_one_play_draw_new'
                    }
        generate_cards_alt('bg hall', dialogs)

        
# ****************   НОВЫЕ  СОПЕРНИКИ   ******************************************

        if alt_my_rival_semifinal.take == 'un':
            rival = CardGameRivalWiseUsual(un_avatar_set, u"Лена", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_semifinal.take == 'sl':
            rival = CardGameRivalWiseUsual(sl_avatar_set, u"Славя", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_semifinal.take == 'dv':
            rival = CardGameRivalWiseUsual(dv_avatar_set, u"Алиса", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_semifinal.take == 'mi':
            rival = CardGameRivalWiseUsual(mi_avatar_set, u"Мику", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_semifinal.take == 'us':
            rival = CardGameRivalWiseLikeUS(us_avatar_set, u"Ульяна", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_semifinal.take == 'sh':
            alt_day2_gambler_behavior = alt_day2_experiment.pop(random.randrange(0,len(alt_day2_experiment)))                   # у Шурика случайный выбор из оставшегося в списке 
            rival = CardGameRivalWiseUsual(sh_avatar_set, u"Шурик", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_semifinal.take == 'mz':
            rival = CardGameRivalWiseUsual(mz_avatar_set, u"Женя", alt_day2_gambler_behavior, alt_day2_gambler_skill)
            
# ************************************************************************************

    $ alt_hint_poker = alt_hint_poker_contractual                                           # подсказки комбинаций — по просмору правил
    jump cards_gameloop_wise_alt                                                            # переход карточный стол
                    
#-------------------------------------------------------------------------------------------------
label alt_day2_semifinal_fail_end_new:
    $ alt_day2_result_tour = 11                                                 # Семён проиграл в полуфинале
    $ persistent.altCardsWon1_new = True
    
    $ alt_day2_gamblers_semifinal[places_my_table[1]].winner = True            # соперник выиграл
    $ alt_rival_final = alt_day2_gamblers_semifinal[places_my_table[1]]         # и он выходит в финал
    $ alt_day2_gamblers_semifinal[places_my_table[0]].winner = False            # Семён проиграл
    $ alt_tournament_state = "semifinal_end"                                   # устанавливаем конец полуфинала
    scene bg int_dining_hall_sunset with dissolve
    window show
    call alt_day2_summary_poker_round
    
# ............................................ ДИАЛОГИ;
    if alt_my_rival_semifinal.take == 'un':
        $ lp_un += 1
        if alt_day2_dv_bet_approve:
            show un serious pioneer at center
            un "И зачем ты это сделал?"
            "Спросила она, смотря на меня с явно выраженной неприязнью."
            me "Извини?"
            un "Думаешь, я не слышала о вашем с Алисой маленьком «пари»?"
            un "Так и выигрывал бы!"
            if alt_day2_walk == 0:
                th "Да я и планировал. Даже карты пометил. Но…"
            else:
                pass
            th "Как-то не срослось."
            me "Да что теперь-то говорить? Я проиграл, ты победила. Удачного вечера."
            "Тем более, что мы не ведём переговоров с террористами."
        else:
            show un angry pioneer with dissolve
            un "Ты поддался, да?"
            "Лена наклонила голову набок и сверлила меня неприязненным взглядом."
            un "Вместо того, чтобы нормально играть, ты устроил поддавки."
            me "Тебе показалось."
            "Усмехнулся я."
        un "Прошу разрешить нам сыграть ещё раз!"
        "В наступившей тишине попросила Лена."
        un "Мой соперник поддавался."
        show dv grin pioneer2 at left with dissolve
        dv "Поддавался — значит, сам дурак."
        "Фыркнула Алиса."
        "Ну да, она-то знает, что на кону."
        show un serious pioneer with dissolve
        un "А ты бы вообще молчала! Это всё из-за тебя! Снова!"
        "Она спрятала лицо в ладонях, а я поднялся из-за стола."
        "Чувствуя себя рабочей ступенью, что вывела на орбиту очередной шаттл."

    elif alt_my_rival_semifinal.take == 'sl':
        show sl normal pioneer with dspr
        sl "И снова меня заставляют заниматься непонятными вещами."
        me "Прости?"
        th "Заговаривается, что ли?"
        "Славя отмахнулась."
        show sl serious pioneer with dspr
        sl "Не обращай внимания, просто мысли вслух."
        me "Ясно. {w}Что ж, тогда удачи тебе в финале!"
        sl "Точно."
        sl "Зачем я вообще играть согласилась."
        show sl sad pioneer with dissolve
        me "Не любишь карты?"
        sl "Нет. Я другие игры люблю."
        "Она сморщилась, будто съела нечто кислое."
        "А я поднялся — меня ждала волнительная роль болельщика за финалистов."

    elif alt_my_rival_semifinal.take == 'dv':
        if alt_day2_dv_bet_approve:
            show dv grin pioneer2 with dspr
            dv "Как думаешь, будет лучше, если я сама с трибуны объявлю?"
            "Алиса злорадствовала так, будто я был её кровный враг с традициями пяти колен."
            dv "Или лучше вытащить тебя на трибуну вместе с собой?"
            if alt_day2_walk == 0:
                th "Лучше объясни мне, откуда ты знаешь {i}мой собственный{/i} крап."
            else:
                pass
            me "Не получится."
            show dv surprise pioneer2 with dspr
            dv "Почему?"
            me "Потому что если ты вытащишь меня на трибуны, никто в жизни не поверит, что мне хватило сил справиться с тобой и — что ты там говорила?"
            show dv laugh pioneer2 with dspr
            dv "Да. Ну…"
            "Ей пришла в голову мысль."
            dv "Я скажу, что ты меня связал."
            me "Колготками!"
        "Алиса весело расхохоталась, а я поднялся."
        "Господи, почему все стервы такие рыжие?"
        "Неужели у меня где-то написано «издеваться сюда»?"
        me "Играй. Тебя финал ждёт."
        me "А если проиграешь, то стыд тебе и позор."
        "Развернулся и ушёл к болельщикам."

    elif alt_my_rival_semifinal.take == 'mi':
        show mi happy pioneer with dspr
        mi "Ура! Я снова побеждаю!"
        mi "Да я, да я… Я супер-Мику!"
        me "О господи, где вы откопали это чудо."
        "Пробормотал я."
        show mi smile pioneer with dspr
        mi "Я хочу отметить свою победу каким-нибудь очень хорошим делом или даже поступком, но мне что-то ничего в голову не приходит, может быть, ты, Сенечка, что-нибудь посоветуешь?"
        "Человек-пулемёт."
        th "Временами нами неминуемо на кон были выкинуты карты, да масти не те…"
        th "Солнышко, милая, ну хватит уже трещать, я же ничего плохого не сделал тебе, за что ты меня тут расстреливаешь!"
        me "Не знаю."
        "Угрюмо ответил я."
        "Поражение меня несколько подкосило."
        show mi happy pioneer with dspr
        mi "Ой, а я знаю, кажется! Да! Мне только что идея в голову пришла! Я…"
        show mi happy pioneer far with dissolve
        "Она забралась на стол."
        mi "Я вам спою!"
        "Она набрала в грудь воздуха, и…"
        show dv angry pioneer2 at cleft with easeinleft
        show mt angry pioneer at cright with easeinright
        with vpunch
        "Неизвестно откуда взявшиеся Ольга и Алиса, взревев в унисон, ринулись стаскивать её на пол."
        "Усмехнувшись, я встал из-за стола и отошёл к болельщикам."

    elif alt_my_rival_semifinal.take == 'us':
        if alt_day2_dv_bet_approve:
            show us laugh pioneer
            us "Ура-ура-ура, прекрасная игра! Красив я и умён, и ловок, и силён!"
            "Прокричала она."
            me "Ты ещё фляк сделай от радости."
            th "Почему ей так нравится факт, что теперь меня освистают на весь лагерь?"
            me "Не знал, что твоим кумиром является Винни Пух со своими кричалками."
            us "А как же!"
            if alt_day2_us_escape:
                us "У меня и медведь есть!"
                "Она показала язык."
                us "Но не узнать лучшее в мире приведение… стыд и срам!"
        "Я поморщился и встал."
        us "Неудачникам привет."
        "Крикнула она мне в спину."
        "А я не среагировал. Привык."
        
    elif alt_my_rival_semifinal.take == 'sh':
        show sh normal pioneer with dissolve
        sh "Жаль, что так быстро всё закончилось."
        "С достоинством кивнул Шурик."
        sh "Идеально, если бы нам дали партий десять с одной колоды, чтобы можно было вычислить логику."
        me "И сидеть до утра?"
        me "Я-то не против, да кто ж нам позволит."
        "Я кивнул и поднялся из-за стола."

    elif alt_my_rival_semifinal.take == 'mz':
        show mz normal pioneer with dissolve
        mz "Упс."
        "Пробормотала она себе под нос."
        mz "Специально же карты не открывала. Здесь вообще как-нибудь проиграть возможно?"
        me "Как видишь."
        "Сказал я и встал из-за стола."
# ............................................ \\диалоги

label alt_day2_semifinal_detour:
    $ renpy.pause(.5)
    scene bg int_dining_hall_sunset
    window show
    "В полуфинале был такой расклад:"
#-------------------------------------------------------------------------------------------------
    call alt_day2_semifinal_analizer                                                  # анализ полуфинала 
    $ renpy.block_rollback()                                                          # блокируем роллбак
    stop ambience
    stop music fadeout 3
    window hide
    jump alt_day2_final_new                                 # и смотрим финал 
#-------------------------------------------------------------------------------------------------
label alt_day2_semifinal_win_end_new:
    $ alt_day2_result_tour = 12                                             # Семён выиграл в полуфинале
    if not alt_day2_detour_final:                                           # если не "выигрыш" в полуфинале скипом
        $ persistent.altCardsWonRivals_new[alt_spr_my_rival] = True         # Выиграли у этого соперника

    $ persistent.altCardsWon2_new = True
    $ alt_day2_gamblers_semifinal[places_my_table[0]].winner = True             # Семён выиграл
    $ alt_rival_final = alt_day2_gamblers_semifinal[places_my_table[0]]         # и он выходит в финал
    $ alt_day2_gamblers_semifinal[places_my_table[1]].winner = False            # Соперник проиграл
    $ alt_tournament_state = "semifinal_end"                                    # устанавливаем конец полуфинала
    scene bg int_dining_hall_sunset
    window show
    call alt_day2_summary_poker_round

# ............................................ ДИАЛОГИ
    if alt_my_rival_semifinal.take == 'un':
        show un serious pioneer with dspr
        "Лена старалась изо всех сил."
        "Видно было, что ей понравилось то, как её восприняли всерьёз."
        show un sad pioneer with dspr
        "Жаль только, что иногда даже старания изо всех сил решительно недостаточно."
        "Ведь ты играешь против батьки!"
        un "Блин! Я почти выиграла!"
        "Вот они злобятся, и кричат, и ножками мотылькают, и невдомёк им, почему окружающим так смешно."
        me "Хочешь реванш?"
        un "Нееет, реванш это не то."
        "Вздохнула она."
        if alt_day2_walk == 0:
            th "Эт ничего, знала бы ты, за счёт чего я тебя обыграл…"
        me "То есть, всё нормально?"
        "Она кивнула."
        "Что она ещё могла сделать?"
        th "А она азартная."
        "Отметил я для себя."
        th "То есть, в случае чего, её можно взять на слаб{b}о{/b}?"
        "Кого-то она мне напомнила этой своей импульсивностью."
        "И когда я понял кого именно, то долго тряс головой, отгоняя глупые мысли."
        show un normal pioneer with dspr
        un "Почему ты смотришь так странно?"
        "Да нет, быть не может."
        "Это просто я надышался запахов из столовой, и меня разбирает галлюцинациями."
        me "Двачевскую!"
        "Алиса покосилась на меня — мол, кто поминает имя моё всуе — но промолчала."
        "А я, не объясняя ничего больше, отправился за стол местных небожителей."
        hide un with dissolve
        "Меня ждал финал!"

    elif alt_my_rival_semifinal.take == 'sl':
        show sl smile2 pioneer with dspr
        "Славя тихонько вздохнула, и улыбнулась."
        "Я не очень понимал, чем вызвана её позитивная реакция, но обрадовался, что не обидел своей победой девушку."
        show sl normal pioneer with dspr
        "Она легко поднялась со стула и кивнула мне:"
        sl "Не успел приехать, а уже первое место занял."
        sl "Так вот и становятся легендами!"
        me "Так я же ещё ничего не занимал…"
        show sl laugh pioneer with dspr
        sl "Только не говори мне, что ты не нацелен на победу!"
        hide sl with dissolve
        "Она отошла к болельщикам."
        "А я пошёл к столу финалистов, между делом оценивая получившуюся ситуацию."

    elif alt_my_rival_semifinal.take == 'dv':
        show dv surprise pioneer2 with dissolve
        $ lp_dv += 1
        th "Итак, Гагарин долетался, Пушкин дописался."
        th "Выиграл!!!"
        show dv normal pioneer2 with dspr
        th "А рыжая доугрожалась."
        "Я поднялся из-за стола и бросил пренебрежительный взгляд на несчастную Алису."
        "Кажется, она чувствовала себя совершенно не в своей тарелке."
        "Теперь мой путь лежит к горним высям, где мне оппонентами выступят сами боги!"
        th "А не всякие самодовольные гадины, считающие, что меня можно запугать или запутать."
        if herc or loki:
            "Я подмигнул Двачевской."
            me "Поздравляю!"
            dv "Что?"
            me "С позорным поражением тебя!"
            $ lp_dv += 1
            "По-моему, она меня всё-таки обругала матом."
            "Не могу сказать — её перекосило так, что я расхохотался."
        else:
            "Я молча встал и направился к столу финалистов."
            "У меня нет времени на детсадовскую возню с неудачниками."

    elif alt_my_rival_semifinal.take == 'mi':
        show mi dontlike pioneer with dspr
        "Мику определённо не была в восторге от того, что я победил."
        "Похоже, она начала худо-бедно разбираться в правилах — и тут на тебе."
        "Humiliating Defeat."
        "Наткнулась на меня."
        mi "В следующий раз победа будет моя!"
        "Она вздёрнула нос к потолку и, поднявшись, гордо удалилась."
        "Правда, немного подпортила картинку, у двери обернувшись и показав мне язык."
        "Культурный человек, наследие эпохи…"
        me "Спасибо за игру!"
        "Крикнул я, и отправился за самый важный стол."
        "Меня ждал финальный раунд смертельной схватки."
        "Между делом отметил положение за соседним столом."

    elif alt_my_rival_semifinal.take == 'us':
        show us dontlike pioneer with dspr
        "Выиграть у Ульяны оказалось легче, чем…"
        "Чем пережить последствия этой победы…"
        show us angry pioneer with dspr
        "Потому что она вдруг перегнулась через стол и принялась колотить меня своими маленькими кулачками."
        "И довольно сильно!"
        us "Ты ведь обещал проиграть!"
        "Она была так обижена, будто я её предал!"
        us "Обещал! Я ведь тебя просила!"
        "Интересно, она понимает, что только что призналась в жульничестве?"
        if alt_day2_walk == 0:
            th "Впрочем, я и сам жульничал, но…"
        else:
            pass
        me "Ничего я не обещал!"
        "С трудом, но мне удалось вставить пару слов в перерыве между ударами…"
        "И мне было не ясно только одно…"
        th "Почему меня никто не спасает?!!"
        th "Где Ольга Дмитриевна, когда она так нужна?!"
        "Но, кажется, всем было настолько весело наблюдать, как меня убивают, что никто и не думал прекращать развлечение…"
        "Наконец поставив сотый синяк на моих руках и голове, Ульяна немного запыхалась и перестала меня бить."
        show us dontlike pioneer with dspr
        "Но она всё ещё была недовольна…"
        "И это ещё мягко сказано…"
        us "У-у-у!"
        "Она свирепо топнула ножкой."
        us "Ладно-ладно!"
        us "Я это тебе ещё припомню."
        hide us with dissolve
        "И с этими словами она резко развернулась и пошла в зал."
        "У меня появилась пара минут на то, чтобы привести себя в порядок и уточнить ситуацию в плей-офф."

    elif alt_my_rival_semifinal.take == 'sh':
        show sh normal pioneer with dspr
        "Шурик кивнул мне и поднялся."
        "Не знаю, впечатлил его мой навык игры, в которую я играю второй раз в жизни (первый раз — в четвертьфинале), или нет."
        "Так или иначе, он достаточно равнодушно отнёсся к поражению."
        show sh smile pioneer with dspr
        sh "Насчёт клуба кибернетиков, если вдруг что…"
        "Я кивнул."
        "По слухам, им вечно не хватало новых членов."
        "Но давайте насчёт кибернетики позже, а пока посмотрим, что там у других пионеров творится."

    elif alt_my_rival_semifinal.take == 'mz':
        show mz normal pioneer with dspr
        "Реакция Жужи меня позабавила."
        "Сначала она бросила карты на стол и спрятала лицо в ладонях."
        "А затем вскинула руки вверх и рявкнула:"
        mz "Аллилуйя!"
        "После чего телепортировалась из столовой."
        "А я же решил узнать, как там дела у соседей."
# ............................................ \\диалоги

#-------------------------------------------------------------------------------------------------
    $ renpy.pause(.5)
    call alt_day2_semifinal_analizer                                    # анализ полуфинала 
    $ renpy.block_rollback()                                                          # блокируем роллбак
    stop ambience
    stop music fadeout 3
    window hide
#-------------------------------------------------------------------------------------------------
label alt_day2_final_new:
    $ alt_day2_my_win = alt_day2_rival_win = alt_day2_game_played_out = 0                       # обнуляем результат игр
    $ alt_tournament_state = "final_start"                                                      # устанавливаем начало финала
    if alt_day2_result_tour == 1:                                                               # Если продул в 1 туре
        $ alt_drawing_of_detour_final()                                                         # вызываем рандомизатор
        $ renpy.fix_rollback()                                                                  # фиксируем выбор — "откатом" поменять будет нельзя
# -----------------------------------------------------------------------
    $ alt_my_rival_final, alt_index_rival_final = alt_get_me_rival_final(alt_day2_gamblers_final,alt_rival_final)      # узнаём второго соперника в финале и его индекс  в рассадке
    
    $ alt_name_my_rival_i = alt_my_rival_final.name['i']                                   # узнаём ИМЯ второго финалиста (в именительном падеже)
    $ alt_name_my_rival_r = alt_my_rival_final.name['r']                                   # узнаём ИМЯ второго финалиста (в родительном падеже)
    $ alt_name_my_rival_d = alt_my_rival_final.name['d']                                   # узнаём ИМЯ второго финалиста (в дательном падеже)
    $ alt_name_my_rival_v = alt_my_rival_final.name['v']                                   # узнаём ИМЯ второго финалиста (в винительном падеже)
    $ alt_name_my_rival_t = alt_my_rival_final.name['t']                                   # узнаём ИМЯ второго финалиста (в творительном падеже)

    $ alt_spr_my_rival = alt_my_rival_final.take                                                # получаем спрайт соперника — заголовок
    $ alt_emo_my_rival = alt_sprites_rival_recognition[alt_spr_my_rival][0]                     # эмоция (строка)
    $ alt_clot_my_rival = alt_sprites_rival_recognition[alt_spr_my_rival][1]                    # одежда (строка)
    $ alt_pos_my_rival = alt_sprites_rival_recognition[alt_spr_my_rival][2]                     # положение
    
    $ alt_nick_my_rival = alt_my_rival_final.nick                                               # получаем характер соперника (для диалога)
# -----------------------------------------------------------------------

#внимание: аналогично верхнему
    # ================================================ НЕМНОГО ОТСЕБЯТИНЫ — пересаживаемся за финальный стол.
    window show
    show el smile pioneer at left with dissolve
    el "Полуфиналы завершены, победители встречаются в финале!"
    $ alt_mstt = 2                                                                              
    call show_tournament_table                                                                  # показать таблицу — итоги полуфинала
    
# ----------------------------------------------------------------------------------------------------
label alt_day2_final_choice_new:
    if alt_rival_final.take == 'me':                                                            # Семён прошел в финал
        "Я уверенно двигаюсь к победе, следующая моя жертва уже видна на горизонте."

# .......................................... ДИАЛОГИ
        if alt_my_rival_final.take == 'un':
            "Прости, Лена. Ничего личного."
        elif alt_my_rival_final.take == 'sl':
            "Славя. Ну, она всё равно без души играет, так что я ей только доброе дело сделаю."
        elif alt_my_rival_final.take == 'dv':
            "Алиса, ага."
            me "Алиса, а Алиса."
            dv "Чего?"
            me "Тебе конец."
            "Она расхохоталась."
        elif alt_my_rival_final.take == 'mi':
            "Мику."
            "Как галантный парень я склонен сдать эту партию, чтобы сделать девушке приятное."
            "Но как игрок я чувствую запах победы, поэтому никакой пощады!"
        elif alt_my_rival_final.take == 'us':
            "Мелкая? Блин, кто-нибудь, объясните мне внятно: какого чёрта это мелкое недоразумение забыло в финале?"
        elif alt_my_rival_final.take == 'sh':
            "Шурик? Хм. Это будет интересный бой."
        elif alt_my_rival_final.take == 'mz':
            "Жужелица."
            "Может быть, и скрипит о том, что играть не хочет, но — блин, она же в финале!"
            "Придётся потрудиться."
# .......................................... /ДИАЛОГИ

        if alt_day2_detour_final:                                                                  # если пропуск финала
            scene bg int_dining_hall_sunset with dissolve2
            $ renpy.pause(1.0)
            window show
            if not alt_day2_tournament_fast_win:                                                   # Если НЕ победа в финале
                $ alt_day2_result_tour = 21                                                         # Семён проиграл в финале
                "Похоже, у меня не было ни шанса."
                call alt_day2_summary_poker_round
                window hide
                jump alt_day2_final_fail_end_new                                                    # на поражение в финале
            elif alt_day2_tournament_fast_win:                                                      # если победа в финале
                $ alt_day2_result_tour = 22                                                         # Семён выиграл в финале
                call alt_day2_summary_poker_round
                window hide
                jump alt_day2_final_win_end_new                                                    # на победу в финале

        jump alt_day2_final_start_new                                                              # играем финал
# ----------------------------------------------------------------------------------------------------
    else:                                                                                      # Семён продул в 1/2
        $ alt_name_rival_final = alt_rival_final.name['i']                                     # Получаем имя финалиста — кому Семён проиграл
        if alt_day2_result_tour == 1:                                                           # Если продул в 1 туре
            if alt_rival_final.take == alt_my_rival_1_tour.take:                                # соперник в 1 туре и финале тот же
                "В финал выходит мой соперник в первом коне — %(alt_name_rival_final)s"
            else:
                if alt_my_rival_1_tour.take == 'sh':
                    "Шурик, мой удачливый соперник, в полуфинале проиграл."
                else:
                    $ alt_name_rival_1_tour = alt_my_rival_1_tour.name['i']
                    "%(alt_name_rival_1_tour)s, отправившая меня в компанию болельщиков, сама проиграла в полуфинале."
                "А финал выходит %(alt_name_rival_final)s"
        else:
            "Так как я сдулся и проиграл, в финал отправляется %(alt_name_rival_final)s"
        extend ", где встретит "
# ---------------------------------------------------
        if alt_my_rival_semifinal == None:                                                                        # Если каким-то образом второй финалист не назначен (может быть и такое)
            $ alt_my_rival_semifinal = alt_day2_gamblers_final[1-alt_day2_gamblers_final.index(alt_rival_final)]  # Это НЕ тот, кому Семён проиграл
# ---------------------------------------------------

# .......................................... ДИАЛОГИ
        if alt_my_rival_final.take == 'un':
            extend "Лену и попытается обыграть её."
        elif alt_my_rival_final.take == 'sl':
            extend "Славю и докажет всем, что блондинка — это диагноз."
        elif alt_my_rival_final.take == 'dv':
            if alt_rival_final.take == 'us':
                extend "… Алису? Так они с самого начала это планировали?!"
            else:
                extend "Алису и попробует уцелеть в этой схватке."
        elif alt_my_rival_final.take == 'mi':
            extend " Мику. {w}Не думаю, что там будет много проблем. Хотя японка и добралась до финала."
        elif alt_my_rival_final.take == 'us':
            if alt_rival_final.take == 'dv':
                extend "Ульянку."
                "Смешно, но, похоже, рыжие в самом деле попросту разметали этот турнир по брёвнышку, как и хотели."
            else:
                extend "Ульяну и попробует выжить после встречи с ней."
        elif alt_my_rival_final.take == 'sh':
            extend "Шурика и попробует доказать, что мозги в карточной игре не решают."
        elif alt_my_rival_final.take == 'mz':
            extend "Женю."
            "Что ещё можно про неё сказать?"
            "Во. Жужелица."
# .......................................... /ДИАЛОГИ

        $ alt_day2_gamblers_final[renpy.random.choice([0,1])].winner = True                                    #  один из игроков (рандомно) — победитель в финале
        $ alt_tournament_state = "final_end"
        call alt_day2_final_analizer
        $ renpy.block_rollback()                                                                                # блокируем роллбак
        
#внимание: аналогично диалогам под "Я уверенно двигаюсь к победе, следующая моя жертва уже видна на горизонте.", только для проигравшего Семёна
    # TODO — что-либо сказать бы по этому поводу — поздравления победителю и все такое
        
        jump alt_day2_prepare_transition_to_supper
# ------------------------------------------------------------------------------------------------------------------------------

label alt_day2_final_start_new:
    call alt_day2_checking_scores
    call alt_day2_stipulation_new                                                       # определяемся, кто первый ходит
# ----------------------------------------------------------------------------
    # первоначальные "настройки" игроков — могут меняться по результатам игры
    # 'defense' — защита, 'gamble' — риск, 'succumb' — слив, 'foolplay' — рандом
    # вероятность ошибки: 1 = 80%, .... 4 = 20%, 5 — ошибок нет.
    
    if alt_my_rival_final.take == 'un':                                                    # Добрались сюда — так что нефиг, Лена защищается
        $ alt_day2_gambler_behavior = 'defense'
        $ alt_day2_gambler_skill = 4                                                       # ошибоки, правда, есть — 20%(4) 
    elif alt_my_rival_final.take == 'sl':                                                  # Славя будет защищаться, может ошибиться — 20%(4)
        $ alt_day2_gambler_behavior = 'defense'
        $ alt_day2_gambler_skill = 4
    elif alt_my_rival_final.take == 'dv':                                                  # Алиса рискует, поблажек не будет
        $ alt_day2_gambler_behavior = 'gamble'
        $ alt_day2_gambler_skill = 5
    elif alt_my_rival_final.take == 'mi':                                                  # Мику будет защищаться, ошибок не будет
        $ alt_day2_gambler_behavior = 'defense'
        $ alt_day2_gambler_skill = 5
    elif alt_my_rival_final.take == 'us':                                                  # Ульяна к финалу научилась играть и будет защищаться, но с ошибками 40% (3)
        $ alt_day2_gambler_behavior = 'defense'
        $ alt_day2_gambler_skill = 3                                                       # ошибок — 40%(3)
    elif alt_my_rival_final.take == 'sh':                                                  # Шурик экспериментирует по-прежнему, но без слива, и без ошибок — научился уже поди
        $ alt_day2_experiment = ['defense','gamble']                                       # у него своя кухня — набор из возможных вариантов
        $ alt_day2_gambler_skill = 5
    elif alt_my_rival_final.take == 'mz':                                                  # Женя играет рандомно, как в классике, ошибки = 5
        $ alt_day2_gambler_behavior = 'foolplay'
        $ alt_day2_gambler_skill = 5
# ----------------------------------------------------------------------------

    if alt_day2_walk == 0:
        $ VISIBLE = True
        $ INVISIBLE = True
    else:
        $ VISIBLE = True
        $ INVISIBLE = False

# ------------------------------------------------------------------------------------------------------------------------------
# Палим Семёна с крапом карт
    if alt_day2_walk == 0 and INVISIBLE:                                    # Если Сёма мухлевал И ЕГО ещё не поймали, его таки в финале МОГУТ спалить
        window show
#внимание: если кроме Алисы никто не "палит" крап, можно убрать всё, кроме if alt_my_rival_final.take == 'dv':
# ---------------------------------------------------------------------------------- Вопрос
        if alt_my_rival_final.take == 'un':                                 # Может спалить Лена
            pass                                                            # Пока заглушка, но мало ли.....
        elif alt_my_rival_final.take == 'sl':                               # Может спалить Славя
            pass
# ---------------------------------------------------------------------------------- /Вопрос
        elif alt_my_rival_final.take == 'dv':                               # Точно палит Алиса
            "Но прежде, чем всё началось, Алиса с подозрением оглядела карты, которыми мы играли."
            th "Неужели…"
            "По спине пробежал холодок…"
            "А она слегка перегнулась через стол и, лукаво улыбаясь, спросила шёпотом — так, что слышать её мог только я…"
            show dv smile pioneer2 with dissolve
            dv "Так ты все карты пометил, да?"
            dv "Предусмотрительный…"
            th "Она знала, что я жульничал!!!"
            "Я покраснел."
            th "Если сейчас она встанет и скажет всем…"
            th "Это будет ужасно!!!"
            th "Невыносимо!!!"
            th "Кошмарно!!!"
            "Но Алиса, кажется, и не думала выдавать меня…"
            "Она улыбалась!"
            dv "Надеялся и меня так обыграть?"
            "И я, проклиная свою честность, тоже шёпотом, ответил:"
            me "Да…"
            "Она фыркнула, впрочем, совсем беззлобно."
            dv "Даже не мечтай…"
            "Незаметно для зрителей она достала из кармана совершенно новую колоду карт и поменяла её местами с помеченной мной…"
            dv "Играть будем моими!"
            "Она довольно улыбнулась."
            dv "Я тоже предусмотрительная…"
            "Игра началась."
            $ INVISIBLE = False
# ---------------------------------------------------------------------------------- Вопрос
        elif alt_my_rival_final.take == 'mi':                               # Может спалить Мику
            pass
        elif alt_my_rival_final.take == 'us':                               # Может спалить Ульяна
            pass
        elif alt_my_rival_final.take == 'sh':                               # Может спалить Шурик
            pass
        elif alt_my_rival_final.take == 'mz':                               # Может спалить Женя
            pass
# ---------------------------------------------------------------------------------- /Вопрос
    window hide
# ------------------------------------------------------------------------------------------------------------------------------

label alt_day2_final_re_game:                                                           # игра в финале — сюда возвращаемся на повторную игру 
    $ alt_my_poker_hand = None
    $ alt_rival_poker_hand = None

    python:
        dialogs = {
                        (0, 'win','jump'):'alt_day2_one_play_win_new',
                        (0, 'fail','jump'):'alt_day2_one_play_fail_new',
                        (0, 'draw','jump'):'alt_day2_one_play_draw_new'
                    }
        generate_cards_alt('bg hall', dialogs)
        
# ****************   НОВЫЕ  СОПЕРНИКИ   ******************************************
        if alt_my_rival_final.take == 'un':
            rival = CardGameRivalWiseUsual(un_avatar_set, u"Лена", alt_day2_gambler_behavior, alt_day2_gambler_skill) 
        elif alt_my_rival_final.take == 'sl':
            rival = CardGameRivalWiseUsual(sl_avatar_set, u"Славя", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_final.take == 'dv':
            rival = CardGameRivalWiseUsual(dv_avatar_set, u"Алиса", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_final.take == 'mi':
            rival = CardGameRivalWiseUsual(mi_avatar_set, u"Мику", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_final.take == 'us':
            rival = CardGameRivalWiseUsual(us_avatar_set, u"Ульяна", alt_day2_gambler_behavior, alt_day2_gambler_skill) # К финалу Ульянка уже и играть научиться должна бы
        elif alt_my_rival_final.take == 'sh':
            alt_day2_gambler_behavior = renpy.random.choice(alt_day2_experiment)                                             # а вот в финале — не удаляем вариант, а выбираем
            rival = CardGameRivalWiseUsual(sh_avatar_set, u"Шурик", alt_day2_gambler_behavior, alt_day2_gambler_skill)
        elif alt_my_rival_final.take == 'mz':
            rival = CardGameRivalWiseUsual(mz_avatar_set, alt_day2_gambler_behavior, alt_day2_gambler_skill)           # Женя играет рандомно, как в классике
# ************************************************************************************

    $ alt_hint_poker = alt_hint_poker_contractual                                           # подсказки комбинаций — по просмору правил
    jump cards_gameloop_wise_alt                                                            # переход карточный стол
    
#-------------------------------------------------------------------------------------------------
label alt_day2_final_fail_end_new:
    $ alt_day2_result_tour = 21                                             # Семён проиграл в финале
    window hide
    scene bg int_dining_hall_sunset with dissolve
    $ persistent.altCardsWon2_new = True

    if alt_day2_gamblers_final[0].take != 'me':                             # если 1-й игрок — НЕ Семён
        $ alt_day2_gamblers_final[0].winner = True                          # он и выиграл
    else:                                                                   # если 2-й игрок — НЕ Семён
        $ alt_day2_gamblers_final[1].winner = True                          # он и выиграл
    $ alt_tournament_state = "final_end"                                    # устанавливаем конец финала
    
    if not alt_day2_detour_final:                                           # если НЕ пропуск финала
        window show
        "Похоже, у меня не было ни шанса."
        call alt_day2_summary_poker_round
        
    scene
    call alt_day2_final_analizer
    $ renpy.block_rollback()                                                          # блокируем роллбак
    scene bg int_dining_hall_sunset with dissolve
    window show
    
# ............................................ ДИАЛОГИ
    if alt_my_rival_final.take == 'un':
        play music music_7dl["take_my_hand"] fadein 3
        $ lp_un += 1
        show un surprise pioneer with dspr
        "Кажется, Лена ещё не до конца поняла, что именно сейчас произошло."
        "А произошло рождение легенды, +50 к опыту, новый уровень и разблокировка уверенности в себе!"
        show un cry_smile pioneer with dspr
        "Лена смотрела на меня долго, неотрывно, и у неё тряслись руки."
        "Я молчу, она молчит, а вокруг нас как будто выросла некая отталкивающая стенка, защищающая нас — но лишь пока мы вместе."
        "Как будто два человека, каждый из которых неполон в одиночестве, вместе они намного сильнее, чем если просто сложить их характеристики."
        "Я не могу сказать сейчас, поддавался ли я, или играл в полную силу, но просто прийти сюда уже было хорошей идеей, сторицей окупившейся этими мгновениями."
        dreamgirl "Не влюбись в неё, барин, вы знакомы меньше суток."
        "Я пожал плечами."
        th "Ну и что?"
        "Ведь поют же все вокруг о любви с первого взгляда, почему бы и мне не пасть жертвой этого волшебного явления?"
        "Ну ладно, но просто признаться себе в том, что она мне нравится, я могу?"
        "Просто лицо, фигура и манера поведения."
        th "Возможно, у неё килограммовые тараканы там, и она только с виду няша-скромняша, глазки в пол, ресничками бяк-бяк."
        th "Но я-то об этом не знаю, правда?"
        th "А значит, буду наслаждаться неведением."
        th "Ибо оно и есть истинное блаженство."
        "Не знать плохого о любимых, не понимать смысл текста красивой песни на японском, не думать об удобрениях для клубники и яблонь, не понимать, что красивая шубка означает смерть животного."
        "Здесь и сейчас — на долю малую секунды — просто влюбиться, пасть жертвой ситуации, настроения и атмосферы."
        window hide
        with fade
        window show
        "И отпустить мгновение, потому что пора просыпаться и идти на работу."
        me "Поздравляю с победой."
        "Улыбнулся я."
        show un shy pioneer with dspr
        un "С-спасибо…"
        "Её имя уже внесли в список победителей, и завтра, скорее всего, заставят поднимать флаг, как самую активную участницу."
        "Ведь нельзя же занять первое место, не принимая активного участия."
        "Правда?"
        "Ох, мои соболезнования."
        th "Хотя это, наверное, мне соболезновать надо?"
        dreamgirl "Намекаешь на двачевские инсинуации? Не дрейфь, она умылась, не дойдя и до финала, постесняется."
        "Будто подтверждая мои слова, Алиса, что всю партию следила за нами, казалось, забыв дышать, вздрогнула и отвела глаза."
        "Похоже, да, не хватит ей пороху довести свою гадость до логического завершения."
        stop music fadeout 3

    elif alt_my_rival_final.take == 'sl':
        $ lp_sl -= 1
        $ karma += 10
        "Славя застонала и уронила голову на сложенные руки."
        play music music_list["forest_maiden"] fadein 5
        sl "Вы хотя бы пытались?" # Это она ко всему отряду, похоже, обращается. Надо бы как-то прояснить этот момент, а то я сначала на понял.
        me "Я — старался!"
        show sl normal pioneer with dspr
        sl "Семен, пожалуйста."
        "Она нахмурилась."
        sl "Хуже меня нет игрока в карты, а я заняла… Ах, зачем я вообще согласилась!"
        me "Но мы же…"
        sl "Вам что, и правда было настолько всё равно, что вы даже поленились немного постараться?"
        show sl sad pioneer with dspr
        sl "Я очень, очень расстроена."
        sl "Если вы и на завтрашних танцах будете такими же активными, я пойму намёк, и до конца смены развлекайте себя сами."
        show mt laugh pioneer at left with dspr
        mt "Что это у нас, а?"
        mt "Демарш победителя? Ну, наконец-то! {w}Я уже было подумала, что ты оживший экспонент мадам Тюссо."
        show sl angry pioneer with dspr
        sl "Ольга Дмитриевна, я серьёзно, а вы!"
        show mt normal pioneer with dspr
        mt "Славь, просто наслаждайся победой, хорошо? {w}Я знаю твоё отношение к карточным играм, и если бы у меня была возможность поставить кого-нибудь вместо тебя, я бы так и поступила."
        "Ольга сочувстенно повздыхала, подмигнула ей и скрылась на кухне."
        "Похоже, слова о призе имели под собой кое-какое обоснование!"
        stop music fadeout 3

    elif alt_my_rival_final.take == 'dv':
        play music music_7dl["sneakupon"]
        $ lp_dv = lp_dv/2
        if loki:
            "Проиграть было забавно."
            "С любой из сторон, как ни крути, я оказывался в выигрыше — в случае победы мне удастся немного заткнуть Двачевскую."
            dreamgirl "Ровно до того момента, пока она не созреет для новой шалости."
            th "Этого достаточно."
            "А в случае поражения она устроит мне пиар-акцию в духе «Сёма едет, прячьте тёлок.»"
            "Так что я от всей души пожелал удачи сопернице."
            "И приготовился к шоу."
        else:
            th "Я слил."
            th "Я облажался."
            th "Как всегда…"
            if alt_day2_walk == 0:                                                 # была лишняя проверка
                th "Несмотря даже на то, что я пометил карты."
            "Появилось это противное чувство, что сейчас на меня начнут показывать пальцем и шептаться «Смотрите, это он! Да, он! Он облажался.»"
            "Я двинулся прочь от стола, не поднимая ни на кого глаз."
            "Особенно — на Алису."
            "Её взгляд буквально жёг мне спину."
        if alt_day2_dv_bet_approve:                                                 # Спорил
            th "Я проиграл пари."
            if loki:
                "Теперь ждём завтрашнего дня и наслаждаемся бесплатной рекламой?"
            else:
                "Теперь мне… {w}Крышка? Кранты? Конец?"
                th "Может, сбежать из лагеря, пока не поздно?"
        else:                                                                       # НЕ спорил
            if alt_day2_dv_harass:                                                  # Если лапал
                "И теперь, если она расскажет всем, что я её лапал — это же правдой будет, да?"
                "Как говорил мой батя в трудных ситуациях — не упс, а йопс."
            else:                                                                   # НЕ лапал
                "Хотя я не спорил с Двачевской, она теперь вполне может рассказать всем то, что она напридумывала на крыльце."
                "И ей поверят. Как обычно верят любому победителю."

        "Алиса победила, и все наперебой принялись её поздравлять."
        "Электроник взмахнул руками, ознаменовав окончание турнира, и дописал в таблицу её имя."
        th "Алиса выиграла…"
        th "А я проиграл"
        if alt_day2_dv_bet_approve:
            extend " и турнир, и пари…"
        else:
            extend " как и всегда, впрочем."
        th "Что же будет?!"
        "Я посмотрел на Алису. Казалось, на её лице не было и следа радости…"
        show dv normal pioneer2 at fleft with dissolve
        if alt_day2_dv_harass:
            "Алиса встала из-за стола и, ощутимо заставляя себя…"
            show mt normal pioneer at fright with dissolve
            "Направилась к вожатой! Да! Момент истины!"
            show dv normal pioneer2 at fleft with moveinleft
            th "Хватит ли девочке пороху?"
            "Внутри меня всё трепетало в предвкушении."
            "Я подвинулся поближе, пытаясь расслышать подробности"
            "Но она говорила шёпотом, и я ничего не мог расслышать…"
            show dv guilty pioneer2 at cright
            show mt normal pioneer at fright
            with dissolve
            "Она краснела всё сильнее, и я буквально мог читать по губам."
            "…руками…"
            "…прямо за грудь…"
            "…и под юбку…"
            me "Двачевская, у тебя такая пылкая фантазия!"
            "Подвёл черту их шептанью я."
            show dv sad pioneer2 at left
            show mt normal pioneer at right
            with dissolve
            me "Может, вслух расскажешь? Мне тоже охота послушать, что я там и сколько раз."
            stop music fadeout 3
            "А Ольга Дмитриевна спокойно посмотрела на меня и сказала:"
            mt "А по-моему, всё верно."
            show mt smile pioneer at right with dspr
            mt "У тебя не было ни единого шанса."
            "Я расхохотался и освободил столик."
            "Кто бы сомневался. Не такой реакции от меня ждала Алиска, совсем не такой."
        else:
            "С равнодушием, лениво бросив на меня прищуренный взгляд, Алиса…"
            show mt normal pioneer at fright with dissolve
            "Пошла прямо к Ольге Дмитриевне, стоявшей всё это время среди зрителей!"
            show dv normal pioneer2 at fleft:
                xalign 0.1
                linear 3.0 xalign 0.7
            th "Неужели она сделает это?!"
            "Всё во мне словно перевернулось!"
            "Я бросился вслед за ней…"
            "Но было уже поздно…"
            show dv smile pioneer2 at cright
            show mt normal pioneer at fright
            with dissolve
            "Алиса стояла рядом с Ольгой Дмитриевной и что-то горячо шептала ей на ухо, весьма лукаво поглядывая на меня!"
            "Этого я не мог допустить!"
            "С громким криком…"
            me "Это неправда!"
            me "Всё, что она говорит обо мне — НЕ-ПРАВ-ДА!"
            show dv smile pioneer2 at left
            show mt normal pioneer at right
            with dissolve
            "Я подбежал к ним…"
            stop music fadeout 3
            "А Ольга Дмитриевна спокойно посмотрела на меня и сказала:"
            mt "А по-моему, всё верно."
            show mt smile pioneer at right with dspr
            mt "Ты совсем не умеешь играть в карты…"
            "Такого позора я ещё никогда не испытывал…"

    elif alt_my_rival_final.take == 'mi':
        play music music_7dl["ourfirstmet"] fadein 3
        show mi happy pioneer with dspr
        $ lp_mi += 1
        $ karma += 10
        mi "Да! Да! Вы понимаете это?! Это снова я, и я снова на коне!"
        mi "У меня не было никаких сомнений в том, что я приду и всех победю!"
        mi "И я пришла и победила."
        mi "Да я, да я… Я супер-Мику!"
        me "Очаровательное чудовище."
        "Пробормотал я."
        show mi smile pioneer with dspr
        mi "Я не так часто выхожу из клуба, потому что всем постоянно что-то надо, все куда-то спешат и говорят мне «потом поговорим!»."
        mi "А я не хочу потом, я сейчас хочу! И сейчас, пока я победитель, вы все должны меня слушать и не ругаться, что я много болтаю!"
        th "Дефицит внимания, ласки, тепла и заботы… А я ещё себя хикикомори считал."
        me "А кричать-то зачем?"
        "Оказаться в финале для меня уже было изрядным достижением, поэтому я не особо расстраивался насчёт проигрыша."
        play music music_7dl["tender_song"] fadein 3
        "А Мику вдруг воздела к небу пальчик."
        show mi happy pioneer with dspr
        mi "Ой, а я знаю, кажется! Да! Мне только что идея в голову пришла! Я…"
        show mi happy pioneer far with dissolve
        "Она забралась на стол."
        mi "Я вам спою!"
        "Она набрала в грудь воздуха, и…"
        show dv angry pioneer2 at cleft with easeinleft
        show mt angry pioneer at cright with easeinright
        with vpunch
        "Неизвестно откуда взявшиеся Ольга и Алиса, взревев в унисон, ринулись было стаскивать её на пол."
        "Но где там!"
        show mi laugh pioneer far at fleft with diam
        "Стол для игры финалистов был большой, не чета узеньким, за которым мы квалифицировались. "
        "Поэтому маленькая, юркая японочка успешно прыгала между руками загребущими и голосила во всю силу своих развитых лёгких."
        "Пела она о чём-то своём, на лунном наречии, которое я даже под градусом считал зубодробительным, а потому и не пытался вслушиваться."
        "Куда интереснее было слушать голос."
        "И смеяться над тем, как тут и там в такт пению раздаются хлопки."
        "Чаще ловящих Мику Алисы и Ольги Дмитриевны, но и из благодарной публики тоже шла своя доля оваций."
        mi "Ла-ла, ла-ла-ла-ла, ла-ла-ла, ла-ла-ла-ла!"
        "Вопила она, бегая по столам, стульям и демонстрируя нам не только высокий уровень игры в карты, но и недюжинную подготовку по части паркура."
        "Я бы поставил на японку и не прогадал."
        "У неё вся жизнь такая."
        "Суетная, бегательно-прыгательная на сцене, и выступления не по три форматных минутки, а полноценные концерты на несколько часов."
        hide mt
        hide dv
        with dissolve
        "Так что ещё минут пять — и обе ловчих свалились рядом со столами, а она всё продолжала и продолжала петь, делая в воздухе странные, стригущие движения пальцами."
        "Отчего-то от таких движений, да ещё в исполнении ультрамаринового маникюра неприятно-холодно ёкало в животе."
        show mi normal pioneer far at center with easeinleft
        window hide
        with fade
        window show
        "Но всё когда-нибудь кончается."
        show mi smile pioneer with dissolve
        "Кончилась и долгоиграющая песенка японской старлетки, и она, подойдя по столу с моей стороны, протянула мне руку."
        "И я, как истинный джентльмен, принял её и помог девочке спуститься."
        show mi happy pioneer close with dspr
        mi "Спасибо! Ты мой герой!"
        show mt rage pioneer at fleft with dissolve
        mt "Ну, Хатсуне!"
        "Мику на миг прижалась ко мне всем телом, а затем убежала от криков разъярённой вожатой."
        hide mi with flash

    elif alt_my_rival_final.take == 'us':
        $ lp_us += 1
        play music music_7dl["genki"] fadein 3
        "Как известно, в карты везёт новичкам и дурачкам."
        "Так как мы все здесь новички, мы были в равных условиях."
        "Но кое-кому перепало на один шанс больше!"
        "И все догадываются, о ком речь, и почему ему больше досталось!"
        "Эти пустые, стеклянные голубые глаза очень странно смотрятся в обрамлении алой чёлки."
        "Косица пшеничного цвета, как у Слави, этому ребёнку подошла  куда бы больше."
        "Такая вот несостоявшаяся блондинка."
        show us laugh pioneer with dspr
        us "Ура! Я победила!"
        "Она вскочила на стул!"
        us "Я победила! И теперь суперприз мой! {w}Моооооой!"
        me "Твой, твой. Ты только слезь со стула, а то брякнешься ещё."
        "Да где там."
        "Ульянка начала подпрыгивать на опасно скрипящем стуле и скандировать:"
        us "Приз! Приз! Приз!"
        me "Успокойся, а?"
        show us grin pioneer with dspr
        us "Ты просто завидуешь, что у меня будет приз, а у тебя нет!"
        "Понятия не имею, о каком призе она говорит."
        "Вообще, пойду-ка я, пока чего не случилось."
        hide us
        window hide
        scene
        call show_tournament_table
        window show
        "А в самом центре таблицы огромными красными буквами значилось имя."
        el "Победитель — Ульяна!"
        "Все стали кричать «поздравляем, поздравляем»!"
        scene bg int_dining_hall_sunset with dissolve
        window show
        "Но Ульяна отмахнулась. {w}Её интересовало другое:"
        us "А где призы?"

    elif alt_my_rival_final.take == 'sh':
        "Чествование Шурика выглядело неловко и натянуто."
        "Он встал, поклонился и вышел из столовой, не дожидаясь даже, когда его имя внесут в таблицу лидеров."
        mi "Кошмарный человек."
        "Заметила Мику."
        mi "Совершенно далёк от публичности."
        un "У него другие достоинства."
        us "Да? Ну-ка подробнее, пожалуйста, о достоинствах, а то я не расслышала."
        un "Тебе бы только о похабностях слушать."
        sl "Лена, а ты бы сама немного думала, что говоришь в присутствии ребёнка."
        us "Эй, мне уже четырнадцать."
        un "Э…"
        sl "Да-да, ты тут о достоинствах Шурика разглагольствовала. "
        dv "Девочки, а что это вы тут обсуждаете, и без меня."
        un "Ой, потеряйся, Двачевская, кошмарище лесное, додумалась новичка сиськами запугивать."
        me "Эй, я всё ещё здесь!"
        all "Заткнись!" with vpunch
        "Я и заткнулся."
        "Что мне ещё оставалось."

    elif alt_my_rival_final.take == 'mz':
        show mz normal pioneer with dspr
        "Жужелица встала."
        "Окинула всех диковатым взглядом."
        mz "Всё, что ли? Больше жертв не будет?"
        play sound sfx_7dl["highfive"]
        $ renpy.pause (3)
        play sound sfx_7dl["highfive"]
        $ renpy.pause (3)
        "В полной тишине спросила она."
        play sound sfx_7dl["highfive"]
        $ renpy.pause (3)
        play sound sfx_7dl["highfive"]
        show el smile pioneer at left with dissolve
        "Только Электроник продолжал хлопать."
        mz "Ну ладно. Я пойду тогда."
        el "Ура, да здравствует победитель!"
        hide mz           
        play sound sfx_7dl["highfive"]
        "Закричал Сыроежкин ей вслед."
        "По-моему, это всё-таки любовь."
        sh "Эл, всё, она ушла. Упокойся."
# ............................................ \\диалоги
    window hide
    stop music fadeout 3
    jump alt_day2_prepare_transition_to_supper                        # пошли ужинать

#-------------------------------------------------------------------------------------------------
label alt_day2_final_win_end_new:
    $ alt_day2_result_tour = 22                                             # Семён выиграл в финале
    $ lp_dv += 1
    
    if not alt_day2_detour_final:                                          # если НЕ пропуск финала
        $ persistent.altCardsWonRivals_new[alt_spr_my_rival] = True        # Выиграли у этого соперника
    $ persistent.altCardsWon3_new = True                                           
    
    if alt_day2_gamblers_final[0].take == 'me':                             # если 1-й игрок — Семён
        $ alt_day2_gamblers_final[0].winner = True                            # он и выиграл
    else:                                                                   # если 2-й игрок — Семён
        $ alt_day2_gamblers_final[1].winner = True                            # он и выиграл
    $ alt_tournament_state = "final_end"                                   # устанавливаем конец финала
    
    if not alt_day2_detour_final:                                                # если НЕ пропуск финала
        window show
        call alt_day2_summary_poker_round

    scene
    call alt_day2_final_analizer
    $ renpy.block_rollback()                                                          # блокируем роллбак
    scene bg int_dining_hall_sunset with dissolve
    window show

# ............................................ ДИАЛОГИ
    if alt_my_rival_final.take == 'un':
        play music music_7dl["take_my_hand"] fadein 3
        show un shy pioneer with dissolve
        un "К-кажется, в-всё."
        me "Что?"
        show un scared pioneer with dspr
        un "Н-ну… Ты выиграл. П-поздравляю."
        "Пробормотала она."
        "Её с трудом можно было разобрать за шумом толпы, а она всё продолжала и продолжала говорить.."
        "Будь моя воля, я бы, наверное, попросил её говорить громче."
        th "Но где там."
        th "Это же означает неминуемое сближение."
        window hide
        scene bg int_dining_hall_sunset with dissolve
        window show
        "Не слушая больше то, что она мне говорит, я поднялся."
        "И пошёл к доске, где Электроник уже писал моё имя."
        window hide
        scene
        call show_tournament_table
        window show
        "Моё!"
        if alt_day2_dv_bet_approve or alt_day2_dv_harass:
            th "И пусть только рыжая стерлядь попробует что-нибудь там вякнуть."
        window hide
        scene bg int_dining_hall_sunset with dissolve
        show dv smile pioneer2 with dissolve
        window show
        if alt_day2_dv_harass:
            "Поймав мой взгляд, она покраснела как маков цвет."
            "А я, склонив голову набок, изобразил пантомиму под названием «натягиваю резиновую перчатку»."
            show dv shy pioneer2 with dissolve
            "И красноречиво так пошевелил пальцами."
            "Алисе аж плохо стало."
            th "Или это она подумала, что я не перчатку надеваю, а… Фу, какая она испорченная."
        else:
            "Лена потерялась на заднем плане где-то, но я неотрывно чувствовал её взгляд лопатками."
            dv "Поздравляю!" with vpunch
            play sound sfx_punch_medium
            "Поэтому почти ожидал хлопка между лопаток."
            "Видимо она так приветствует всех, кто ей интересен."
        window hide
        hide dv with dissolve

    elif alt_my_rival_final.take == 'sl':
        $ lp_sl += 1
        play music music_7dl["please_reprise"] fadein 3
        show sl smile pioneer with dspr
        "Я победил?"
        "Победил?!"
        me "Да!"
        "Бросив над головой карты, рявкнул я:"
        me "Я — победитель!!!" with vpunch
        show sl normal pioneer with dspr
        "Почему-то здесь и сейчас хотелось вести себя так, как душа лежит."
        "Не так, как правила того требуют, или «что же люди скажут»."
        "Это её влияние. Её."
        "А ведь мы знакомы меньше суток."
        "Но уже сейчас искренность проявлений чувств становится одной из самых важных добродетелей."
        sl "Да!"
        "Звонко произнесла она."
        "Её глаза сияли."
        sl "Ты победитель турнира."
        sl "Ты — победитель."
        "Как в боксе, она стоит рядом со мной."
        "Хватает меня за запястье."
        "И тянет к небу поднятой рукой."
        sl "Се-{w}мён!  Се-{w}мён!"
        "Скандирует она."
        "Трудно бороться с чувством сюрреалистичности происходящего."
        "Как будто бы я попал в какую-нибудь космическую оперу или ещё какой-то пафосный жанр."
        th "Но эти люди не умеют стесняться честного слова и  честного чувства."
        show sl happy pioneer with dissolve
        "Они кричат вместе с ней."
        "Смотрят на меня."
        "Мои пятнадцать минут славы."
        dreamgirl "Пятнадцать минут Слави?"
        "А я расхохотался."
        th "Да! Да, чёрт возьми. Именно так."
        "К нам протолкалась Ольга Дмитриевна."
        mt "Не уходи никуда после ужина, будет вручение призов."
        dv "Поздравляю!"
        "Из-за спины я услышал голос, который слышать бы очень не хотел."
        "Судя по сузившимся глазам Слави, не я один."
        "Но я обернулся."
        show dv smile pioneer2 at cleft with dissolve
        if alt_day2_dv_bet_approve:
            dv "Ты победил в споре и турнире."
        else:
            dv "Молоток!"
        "Она ткнула меня кулаком в плечо и, развернувшись, растворилась в толпе."
        window hide

    elif alt_my_rival_final.take == 'dv':
        $ lp_dv += 1
        play music music_7dl["sheiscool"] fadein 3
        th "Я выиграл!"
        th "Выиграл?"
        th "Выиграл!!!"
        show dv normal pioneer2 with dspr
        "Ещё несколько часов назад я не мог и представить себя таким счастливым!"
        "Я победно смотрел на Алису, ещё не веря до конца в свою удачу…"
        "А вокруг уже все поздравляли меня с победой, и Электроник писал моё имя в своей таблице!"
        window hide
        scene
        call show_tournament_table
        window show
        th "Моё имя!!!"
        th "Я выиграл турнир!"
        window hide
        scene bg int_dining_hall_sunset with dissolve
        window show
        "Словно и не было этих часов переживаний и напряжения…"
        "Я стал лёгким, как пёрышко…"
        "Я как будто научился летать!"
        if alt_day2_dv_bet_approve:
            th "Я выиграл пари!!!"
        show dv smile pioneer2 with dissolve
        if alt_day2_dv_harass:
            "Алиса была готова на месте провалиться — до такой степени она покраснела."
            "Поймав её взгляд, я подмигнул, сделав препохабнейшую морду лица."
            show dv rage pioneer2 with dissolve
            "Её перекосило."
            "А я расхохотался."
            "Вечер сегодня определённо мой!"
        else:
            "А Алиса наконец поднялась со своего места и, проходя мимо меня, хлопнула по плечу."
            dv "Поздравляю!"
            "И от этих слов мне стало так радостно!"
            th "Я победил Алису!!!"
        window hide
        hide dv with dissolve

    elif alt_my_rival_final.take == 'mi':
        $ lp_mi += 2
        $ alt_day2_mi_snap = True
        play music music_7dl["tellyourworld"] fadein 3
        show mi smile pioneer with dspr
        mi "Ты и правда победил! Ты молодец!"
        "Воскликнула она."
        show mi normal pioneer with dspr
        mi "Только не думай, что тебе это поможет!"
        "Строго сказала девочка."
        mi "В следующий раз я тебя обязательно обыграю!"
        "Конечно. Сколько угодно. Но — в следующий раз."
        "А сейчас…"
        "В таблице красовалось моё имя, выведенное толстым красным маркером."
        "Мику схватила меня за руку и потащила за собой."
        me "Эй!"
        mi "Да быстрее же ты!"
        "Ничего не понимая, я поспешил за ней."
        me "И что?"
        "Мы остановились у доски, и девочка кому-то замахала."
        mi "Дядя Боря-сенсей! Мы здесь!"
        if ('sport_area' in list_voyage_7dl):
            th "Что ей может понадобиться от Саныча?"
            "С любопытством подумал я."
        show ba normal uniform at cleft behind mi
        show mi smile pioneer at right
        with dissolve
        ba "Да, малая, чего звала?"
        mi "У вас ещё есть кадры?"
        show ba smile uniform with dspr
        ba "Для тебя, малая, сколько влезет."
        "Из ниоткуда в его руках появился жёсткий коричневый чехол для фотоаппарата, а оттуда…"
        "Старый добрый «компакт-автомат», плёночный."
        "Я чуть было не сказал «раритет», но видно было, что машинка рабочая."
        ba "Только без вспышки сегодня, так что становитесь как-нибудь, где посветлее."
        "Мику улыбнулась и развернула кипучую деятельность, тормоша всех и переставляя."
        "В результате полотнище таблицы было снято и перенесено поближе к окошку, где Шурик и Электроник держали его на растяг."
        scene bg int_dining_hall_sunset
        with dissolve
        scene
        call show_tournament_table
        "Мику встала рядом."
        show mi normal pioneer at cleft with dissolve
        "Ещё ближе."
        "Ещё чуточку."
        mi "Сень!"
        "Наконец не выдержала она."
        mi "Я же с тобой фотографируюсь!!! А ну, быстро обними девушку."
        me "Но я…"
        "Я вздохнул."
        th "Я не помню, когда я последний раз так фотографировался с кем-то."
        th "Я не умею никого обнимать для фото…"
        mi "Смелее же, ну!"
        "Она нетерпеливо пошевелила плечиком."
        "И я, вздохнув, положил ей на плечо руку."
        "Неловко — как и чувствовал себя — неловко."
        "Свисающая кисть, нечувствительные пальцы."
        "Как фотографировался бы с другом, а не с девушкой."
        "До меня слишком поздно дошло, что девушку надо обнимать за талию, а не вот так."
        window hide
        scene cg d2_mi_me_polaroid_7dl
        with dissolve
        "Но… поздно!"
        window hide
        play sound sfx_7dl["snap"]
        scene expression Sepia("cg d2_mi_me_polaroid_7dl")
        show PolaroidFrame_7dl
        with flash
        $ renpy.pause(3)
        me "Сыыыр."
        "Запоздало опомнился я."
        mi "Хи-хи-хи."
        mi "Сенечка, ты чудо."
        "Она рассмеялась и убежала."
        window hide
        scene bg int_dining_hall_sunset with dissolve

    elif alt_my_rival_final.take == 'us':
        $ lp_us -= 1
        th "Я выиграл!"
        th "Выиграл?"
        th "Выиграл!!!"
        "Бац!" with vpunch
        with flash_red
        play music music_7dl["genki"] fadein 3
        show us calml pioneer with dissolve
        us "И ничего ты не выиграл!"
        "Она хмуро смотрела на меня снизу вверх."
        us "Ты играл неправильно, переигрываем!"
        me "Что это значит, «неправильно»?"
        show us dontlike pioneer with dspr
        me "Я выиграл турнир! {w}Как я могу играть неправильно?"
        us "Молча! Ты жульничал!"
        "Она топнула ногой."
        us "Ты неправильно играл и жульничал!"
        if alt_day2_walk == 0:
            th "Неужели про крап узнала? Но как?"
            th "Если она сейчас всем про него раcскажет, меня линчуют на ближайшей осине."
        us "Ты плохо мне поддавался."
        "А. Ну, это меняло всё дело."
        hide us with dissolve
        "Я расхохотался и отошёл."
        show dv smile pioneer2 with dissolve
        "А Алиса наконец поднялась со своего места и, проходя мимо меня, хлопнула по плечу."
        dv "Поздравляю!"
        "И от этих слов мне стало так радостно!"
        th "Я победил!!!"
        hide dv with dissolve
        window hide

    elif alt_my_rival_final.take == 'sh':
        play music music_7dl["dead_silence"] fadein 3
        show sh rage pioneer with dissolve
        sh "Значит, победил?"
        "Медленно произнёс он."
        "Он так странно стоял, что я никак не мог разглядеть его глаз из-за бликов на очках."
        show sh serious pioneer with dspr
        "Да и сама его поза…"
        "Почему-то вдруг вспомнился персонаж Элайджи Вуда из «Города Грехов»."
        "Вроде бы, ничего такого сверхъестественного не делал, но тревогу внушал примерно так же — одним появлением на экране."
        "И Шурик заставлял меня тревожиться."
        sh "То есть, думаешь, что можно просто так прийти и выиграть мой турнир?"
        stop ambience
        scene black
        show sh rage pioneer close
        with diam
        sh "Да кто ты такой вообще?"
        sh "Вожатая о тебе ничего не говорит, никто ничего не знает."
        show sh rage pioneer close
        sh "А может быть, ты…"
        scene expression Noir("bg int_dining_hall_day")
        show sh rage pioneer close:
            xalign .5 yalign .7 zoom 0.7
            ease 0.3 yalign .4 zoom 1.25
        "Он сделал резкий шаг в мою сторону и протянул руку."
        mt "Шурик!"
        stop music fadeout 3
        play ambience ambience_dining_hall_full fadein 5
        show blinking
        scene bg int_dining_hall_sunset
        with diam
        show sh upset pioneer with dissolve
        "Наваждение момента исчезло, Шурик из зловещей фигуры превратился обратно в обычного, чуть рассеянного, парня."
        "Серые, давящие стены уступили место красноватому свету катящегося на закат светила."
        "И самое главное — "
        "Ведь я же победитель!"
        hide sh with dissolve
        window hide
        scene
        call show_tournament_table
        window show
        "Электроник внёс моё имя в список победителей." 
        el "А после ужина…"
        scene bg int_dining_hall_sunset with dissolve
        window show
        "Ольга Дмитриевна заткнула ему рот рукой."
        th "Правильно, пусть будет сюрпризом. А для спойлерщиков в аду отдельный котёл стоит."
        window hide

    elif alt_my_rival_final.take == 'mz':
        "Реакция Жужелицы была обескураживающей."
        "Её не было."
        "Но меня это не смущало."
        "Самое главное, что я победил!"
        "Остальные пусть думают и делают что хотят."
        "Даже Алиса."
        "Сейчас-то ей никто не поверит."
        "И это, пожалуй, радует больше всего."
        window hide
# ............................................ \\диалоги
    
    scene bg int_dining_hall_sunset with dissolve2
    jump alt_day2_prepare_transition_to_supper                                            # ушли ужинать
    
    

    
# ======================================================================================================================
#                                          ОБЩИЕ МЕТКИ ПО ОБРАБОТКЕ ТУРНИРА
# ======================================================================================================================

# ----------------------------------------------------------------------------------
# ОРПРЕДЕЛЯЕМСЯ С ОЧЕРЁДНОСТЬЮ ПЕРВОХО ХОДА В КОНЕ
label alt_day2_stipulation_new:
    scene bg int_dining_hall_sunset with dissolve2
    python:
        alt_spr_rival =[alt_spr_my_rival,alt_emo_my_rival,alt_clot_my_rival]
        alt_spr_my_riv_1 = " ".join(alt_spr_rival)
        renpy.show(alt_spr_my_riv_1,[alt_pos_my_rival])
        renpy.transition(dspr) 
    window show
    alt_nick_my_rival "Кто первый ходит?"
    window hide
    
#внимание: во избежание подкруток убрать меню и оставить безальтернативно "Монетку кинем"
# TODO — убрать лишние пункты меню
    menu:
        "Камень, ножницы, бумага?":
            label alt_day2_RPS: 
                scene bg int_dining_hall_sunset
                python:
                    renpy.show(alt_spr_my_riv_1,[alt_pos_my_rival])
                    renpy.transition(dspr)
                call RPS_game(alt_opp = alt_nick_my_rival)
                if RPS_winner == 1:
                    me "%(alt_name_my_rival_i)s, первый ход — твой."
                    $ alt_whose_first_move = 'rival'
                elif RPS_winner == 0:
                    jump alt_day2_RPS
                elif RPS_winner == -1:
                    alt_nick_my_rival "Первым ходить будешь ты."
                    $ alt_whose_first_move = 'player'
    
        "Монетку кинем (рандом)":
            $ alt_whose_first_move = renpy.random.choice(['rival', 'player'])
            $ renpy.pause(1)
            window show
            "Сомнительная честь сделать первый ход выпала "
            if alt_whose_first_move == 'rival':
                extend "%(alt_name_my_rival_d)s."
            elif alt_whose_first_move == 'player':
                extend "мне."
            window hide
            
        "Ты (первый ход — %(alt_name_my_rival_r)s)":
            $ alt_whose_first_move = 'rival'
            
        "Я (первый ход — Семёна)":
            $ alt_whose_first_move = 'player'

    return
    
# ----------------------------------------------------------------------------------
# Победа Семёна в очередной игре тура
label alt_day2_one_play_win_new:
    $ alt_day2_my_win += 1                                                  # +1 к победам Семёна
    $ alt_day2_game_played_out += 1                                         # +1 результативная игра
    $ alt_day2_result_current_game = 1                                      # победа Семёна
    jump alt_day2_checking_scores                                           # считаем очки
    
# ----------------------------------------------------------------------------------
# Поражение Семёна в очередной игре тура
label alt_day2_one_play_fail_new:
    $ alt_day2_rival_win += 1                                               # +1 к победам соперника
    $ alt_day2_game_played_out += 1                                         # +1 результативная игра
    $ alt_day2_result_current_game = 2                                      # победа соперника
    jump alt_day2_checking_scores                                           # считаем очки

#-----------------------------------------------------------------------------------
# НИЧЬЯ в очередной игре тура
label alt_day2_one_play_draw_new:
    $ show_cards_alt()
    window show
    el "Ничья! Играйте ещё раз."
    window hide
    if alt_tournament_state == "1_round_start":                             # если первый тур
        jump alt_day2_1_tour_re_game                                        # играем первый тур
    elif alt_tournament_state == "semifinal_start":                         # если полуфинал
        jump alt_day2_semifinal_re_game                                  # играем полуфинал
    elif alt_tournament_state == "final_start":                             # если финал
        jump alt_day2_final_re_game                                      # играем финал
        
#-----------------------------------------------------------------------------------
# Анилизируем счёт по играм в этапе
label alt_day2_checking_scores:
    scene bg int_dining_hall_sunset with dissolve
    if alt_day2_my_win == alt_day2_rival_win:                                                   # если счёт равный
        if alt_day2_game_played_out == 0:                                                       # ещё не играли (0:0)
            if alt_day2_gamblers_final[0].take == 'me':                                         # если 1-й игрок — Семён
                $ alt_day2_upper_gambler_name = "Семёном"
                $ alt_day2_bottom_gambler_name = alt_name_my_rival_t
            else:
                $ alt_day2_upper_gambler_name = alt_name_my_rival_t
                $ alt_day2_bottom_gambler_name = "Семёном"
            window show
            show el normal pioneer far at left
            el "До начала финальной игры между %(alt_day2_upper_gambler_name)s и %(alt_day2_bottom_gambler_name)s осталась минута, счёт по-прежнему ноль-ноль."
            "Электроник комментировал игру, как умел."
            hide el with dissolve
            window hide
            return
        else:                                                                                   # если 1:1
            window show
            call alt_day2_current_game_end_compare_hands                                        # сравнение комбинаций по итогам игры
            show el serious pioneer far at left
            el "Итак, по итогам двух игр у нас пока ничья; победитель определится в решающей игре."
            el "А кто будет ходить первым — сейчас разыграем, и поможет нам в этом портативный генератор случайных чисел."
            "Электроник выудил из кармана монету."
            el "Орёл? Решка?"
            menu:
                "Орёл":
                    $ alt_whose_first_move_choice = 1
                "Решка":
                    $ alt_whose_first_move_choice = 0
            $ alt_whose_first_move_random = renpy.random.choice([0, 1])
            if alt_whose_first_move_random == 0:
                "Эл подбросил монетку, выпала решка."
            else:
                "Подброшенная монета упала орлом."
            if alt_whose_first_move_choice == alt_whose_first_move_random:
                if alt_name_my_rival_i == "Шурик":
                    el "Надо же, угадал. Первым ходить будет Шурик,"
                else: 
                    el "Надо же, угадал. Первой ходить будет %(alt_name_my_rival_i)s,"
                if alt_whose_first_move == 'player':
                    extend " как и в первой игре."
                else:
                    extend " как и во второй игре."
                $ alt_whose_first_move = 'rival'
            else:
                el "Мимо. Так что первый ход — твой,"
                if alt_whose_first_move == 'player':
                    extend " как и во второй игре."
                else:
                    extend " как и в первой игре."
                $ alt_whose_first_move = 'player'
            window hide
            scene bg int_dining_hall_sunset with dissolve 
            jump alt_day2_transition_to_game
    elif alt_day2_my_win > alt_day2_rival_win:                                                  # Семён ведёт в счёте
        window show
        call alt_day2_current_game_end_compare_hands                                            # сравнение комбинаций по итогам игры
        if alt_day2_game_played_out == 1:                                                       # по итогам первой игры
            show el normal pioneer far at left
            if alt_whose_first_move == 'rival':                                                 # если первым ходил соперник
                el "Семён, теперь первым будешь ходить ты."
                $ alt_whose_first_move = 'player'                                               # то первым ходит Семён
            else:                                                                               # если ходил Семён
                el "Право первого хода переходит к %(alt_name_my_rival_d)s."
                $ alt_whose_first_move = 'rival'                                                # то первым ходит соперник
            window hide
            scene bg int_dining_hall_sunset with dissolve 
            jump alt_day2_transition_to_game                                                    # переход к игре
        else:                                                                                   # по итогам тура
            show el normal pioneer far at left
            el "Семён выигрывает у %(alt_name_my_rival_r)s со счётом %(alt_day2_my_win)d-%(alt_day2_rival_win)d."
            window hide
            if alt_tournament_state == "final_start":                                           # если финал
                jump alt_day2_final_win_end_new                                                 # победа в финале
            elif alt_tournament_state == "semifinal_start":                                     # если полуфинал
                jump alt_day2_semifinal_win_end_new                                             # победа в полуфинале
            elif (alt_tournament_state == "1_round_start") or alt_day2_revanche:                # если первый тур ИЛИ реванш 
                jump alt_day2_participate_win_end_new                                           # победа в 1 туре                
    else:                                                                                       # соперник выигрывает
        window show
        call alt_day2_current_game_end_compare_hands                                            # сравнение комбинаций по итогам игры
        if alt_day2_game_played_out == 1:                                                       # по итогам первой игры
            show el normal pioneer far at left
            if alt_whose_first_move == 'rival':                                                 # если первым ходил соперник
                el "В следующей игре первым будет ходить Семён."
                $ alt_whose_first_move = 'player'                                               # то первым ходит Семён
            else:                                                                               # если ходил Семён
                el "%(alt_name_my_rival_i)s, теперь первый ход — твой."
                $ alt_whose_first_move = 'rival'                                                # то первым ходит соперник
            window hide
            scene bg int_dining_hall_sunset with dissolve 
            jump alt_day2_transition_to_game                                                    # переход к игре
        else:                                                                                   # по итогам тура
            show el normal pioneer far at left
            el "%(alt_name_my_rival_i)s одерживает победу со счётом %(alt_day2_rival_win)d-%(alt_day2_my_win)d."
            window hide
            if alt_tournament_state == "final_start":                                           # если финал
                jump alt_day2_final_fail_end_new                                                # поражение в финале
            elif alt_tournament_state == "semifinal_start":                                     # если полуфинал
                jump alt_day2_semifinal_fail_end_new                                            # поражение в полуфинале
            elif (alt_tournament_state == "1_round_start") or alt_day2_revanche:                # если первый тур ИЛИ реванш 
                jump alt_day2_participate_fail_end_new                                          # поражение в 1 туре                


#-----------------------------------------------------------------------------------
# Возвращаемся к обратно к игре на соответствующий этап
label alt_day2_transition_to_game:                                                    # переход к игре
    if alt_tournament_state == "final_start":                                         # если финал
        jump alt_day2_final_re_game                                                   # играем финал
    elif alt_tournament_state == "semifinal_start":                                   # если полуфинал
        jump alt_day2_semifinal_re_game                                               # играем полуфинал
    elif (alt_tournament_state == "1_round_start") or alt_day2_revanche:              # если первый тур ИЛИ реванш
        jump alt_day2_1_tour_re_game                                                  # играем 1 тур


        
#-----------------------------------------------------------------------------------
# Результат ИГРЫ (сравниваем и оцениваем комбинации)
label alt_day2_current_game_end_compare_hands:                                      # Результат текущей игры
    $ alt_day2_current_rout_status = 0                                              # текущая игра закончена
    if alt_day2_result_current_game == 1:                                           # победа Семёна
        $ alt_day2_summary_poker_1, alt_day2_summary_poker_2 = alt_comparison_poker_hands(alt_my_poker_hand, alt_rival_poker_hand, 'me', alt_spr_my_rival)
        if alt_day2_game_played_out == 1:                                           # сыграли раз
            $ alt_day2_current_rout_status = 1                                      # Семён выиграл 1-ю игру
        elif alt_day2_game_played_out == 2:                                         # сыграли два раза
            if alt_day2_rival_win == 1:                                             # соперник выиграл один раз
                $ alt_day2_current_rout_status = 2                                  # Семён отыгрался

    elif alt_day2_result_current_game == 2:                                         # победа соперника
        $ alt_day2_summary_poker_1, alt_day2_summary_poker_2 = alt_comparison_poker_hands(alt_rival_poker_hand, alt_my_poker_hand, alt_spr_my_rival, 'me')
        if alt_day2_game_played_out == 1:                                           # сыграли раз
            $ alt_day2_current_rout_status = 3                                      # соперник выиграл 1-ю игру
        elif alt_day2_game_played_out == 2:                                         # сыграли два раза
            if alt_day2_my_win == 1:                                                # Семён выиграл один раз
                $ alt_day2_current_rout_status = 4                                  # соперник отыгрался

    $ alt_day2_result_current_game = 0                                              # результат текущей игры = 0 (ничья)
    "%(alt_day2_summary_poker_1)s"
    "%(alt_day2_summary_poker_2)s"
    
    if alt_day2_current_rout_status in [1,2,3,4]:                                   # если игра не закончена     #moded
        call alt_day2_current_game_ending_dialogs                                   # вызов диалога по текущей ситуации
    else:
        pass
    return
        
#внимание: сценарная работа
#-----------------------------------------------------------------------------------
# TODO — диалоги по итогам очередной игры (выиграл/проиграл-сравнял счёт)
# сортировка — сначала по персонажам, потом — по ситуациям (0-проверка, 1 — Семён выиграл 1-ю, 2 — Семен сравнял счёт, 3 — соперник выиграл 1-ю, 4 — соперник сравнял счёт)
# ---------------------------------------------------------
# если диалоги по объему будут небольшими и без спрайтов — можно будет перебросить их в словарь
# если нет — лучше тут пусть и остаются

# TODO — тут же "накручиваем" скилл соперникам по итогам очередной игры, (если не надо — убрать)

label alt_day2_current_game_ending_dialogs:
# Лена
    if alt_spr_my_rival == 'un':
        if alt_day2_current_rout_status == 1:                   # если Семён выиграл первый раз
            if alt_day2_gambler_behavior != 'succumb':          # если не "поддавки"
                $ alt_day2_gambler_skill += 1                     # увеличиваем навык
            
            show un smile3 pioneer at cright with dspr
            th "(Семён победил в первой игре)."
            un "{i}(Следует обмен мнениями по этому поводу).{/i}"
            
        elif alt_day2_current_rout_status == 2:                 # если Семён отыгрался
            if alt_day2_gambler_behavior != 'succumb':          # если не "поддавки"
                $ alt_day2_gambler_skill += 1                     # увеличиваем навык
        
            show un shy pioneer at cright with dspr
            th "(Семён сравнял счёт в партии)."
            un "{i}(Следует обмен мнениями по этому поводу).{/i}"
            
        elif alt_day2_current_rout_status == 3:                 # и она выиграла первый раз
            if alt_day2_gambler_behavior == 'succumb':          # если "поддавки"
                $ alt_day2_gambler_skill += 1                     # увеличиваем навык
        
            show un serious pioneer at cright with dspr
            th "(Лена победила в первой игре)."
            un "{i}(Следует обмен мнениями по этому поводу).{/i}"
            
        elif alt_day2_current_rout_status == 4:                 # и она отыгралась
            if alt_day2_gambler_behavior == 'succumb':          # если "поддавки"
                $ alt_day2_gambler_skill += 1                     # увеличиваем навык
        
            show un sad pioneer at cright with dspr
            th "(Лена сравняла счёт в партии)."
            un "{i}(Следует обмен мнениями по этому поводу).{/i}"
            
# Славя
    elif alt_spr_my_rival == 'sl':
        if alt_day2_current_rout_status == 1:                   # если Семён выиграл первый раз
            $ alt_day2_gambler_skill += 1                     # увеличиваем навык
        
            show sl serious pioneer at cright with dspr
            th "(Семён победил в первой игре)."
            sl "{i}(Следует обмен мнениями по этому поводу).{/i}"
            
        elif alt_day2_current_rout_status == 2:                 # если Семён отыгрался
            $ alt_day2_gambler_skill += 1                     # увеличиваем навык
        
            show sl sad pioneer at cright with dspr
            th "(Семён сравнял счёт в партии)."
            sl "{i}(Следует обмен мнениями по этому поводу).{/i}"
            
        elif alt_day2_current_rout_status == 3:                 # и она выиграла первый раз
        
            show sl angry pioneer at cright with dspr
            th "(Славя победила в первой игре)."
            sl "{i}(Следует обмен мнениями по этому поводу).{/i}"
            
        elif alt_day2_current_rout_status == 4:                 # и она отыгралась
        
            show sl smile2 pioneer at cright with dspr 
            th "(Славя сравняла счёт в партии)."
            sl "{i}(Следует обмен мнениями по этому поводу).{/i}"
            
# Алиса
    elif alt_spr_my_rival == 'dv':
        if alt_day2_current_rout_status == 1:                   # если Семён выиграл первый раз
            $ alt_day2_gambler_skill += 1                     # увеличиваем навык
        
            show dv surprise pioneer2 at cright with dspr
            th "(Семён победил в первой игре)."
            dv "{i}(Следует обмен мнениями по этому поводу).{/i}"
            
        elif alt_day2_current_rout_status == 2:                 # если Семён отыгрался
            $ alt_day2_gambler_skill += 1                     # увеличиваем навык
            $ alt_day2_gambler_behavior = 'gamble'          # и начинает рисковать
            
            show dv guilty pioneer2 at cright with dspr
            th "(Семён сравнял счёт в партии)."
            dv "{i}(Следует обмен мнениями по этому поводу).{/i}"
            
        elif alt_day2_current_rout_status == 3:                 # и она выиграла первый раз
            $ alt_day2_gambler_behavior = 'defense'              # садится в оборону
        
            show dv smile pioneer2 at cright with dspr
            th "(Алиса победила в первой игре)."
            dv "{i}(Следует обмен мнениями по этому поводу).{/i}"
            
        elif alt_day2_current_rout_status == 4:                 # и она отыгралась
            $ alt_day2_gambler_behavior = 'gamble'          # и начинает рисковать
            
            show dv laugh pioneer2 at cright with dspr
            th "(Алиса сравняла счёт в партии)."
            dv "{i}(Следует обмен мнениями по этому поводу).{/i}"
            
# Мику
    elif alt_spr_my_rival == 'mi':
        if alt_day2_current_rout_status == 1:                   # если Семён выиграл первый раз
            $ alt_day2_gambler_skill += 1                     # увеличиваем навык
            
            show mi upset pioneer at cright with dspr
            th "(Семён победил в первой игре)."
            mi "{i}(Следует обмен мнениями по этому поводу).{/i}"
            
        elif alt_day2_current_rout_status == 2:                 # если Семён отыгрался
            $ alt_day2_gambler_skill += 1                     # увеличиваем навык
            
            show mi dontlike pioneer at cright with dspr
            th "(Семён сравнял счёт в партии)."
            mi "{i}(Следует обмен мнениями по этому поводу).{/i}"
            
        elif alt_day2_current_rout_status == 3:                 # и она выиграла первый раз
        
            show mi shy pioneer at cright with dspr
            th "(Мику победила в первой игре)."
            mi "{i}(Следует обмен мнениями по этому поводу).{/i}"
            
        elif alt_day2_current_rout_status == 4:                 # и она отыгралась
        
            show mi surprise pioneer at cright with dspr
            th "(Мику сравняла счёт в партии)."
            mi "{i}(Следует обмен мнениями по этому поводу).{/i}"
            
# Ульяна
    elif alt_spr_my_rival == 'us':
        if alt_day2_current_rout_status == 1:                   # если Семён выиграл первый раз
            $ alt_day2_gambler_skill += 1                     # увеличиваем навык
        
            show us angry pioneer at cright with dspr
            th "(Семён победил в первой игре)."
            us "{i}(Следует обмен мнениями по этому поводу).{/i}"
            
        elif alt_day2_current_rout_status == 2:                 # если Семён отыгрался
            $ alt_day2_gambler_skill += 1                     # увеличиваем навык
        
            show us dontlike pioneer at cright with dspr
            th "(Семён сравнял счёт в партии)."
            us "{i}(Следует обмен мнениями по этому поводу).{/i}"
            
        elif alt_day2_current_rout_status == 3:                 # и она выиграла первый раз
        
            show us surp1 pioneer at cright with dspr
            th "(Ульяна победила в первой игре)."
            us "{i}(Следует обмен мнениями по этому поводу).{/i}"
            
        elif alt_day2_current_rout_status == 4:                 # и она отыгралась
        
            show us grin pioneer at cright with dspr
            th "(Ульяна сравняла счёт в партии)."
            us "{i}(Следует обмен мнениями по этому поводу).{/i}"
            
# Шурик
    elif alt_spr_my_rival == 'sh':
        $ alt_day2_gambler_skill += 1                     # увеличиваем навык — Шурику без вариантов
        if alt_day2_current_rout_status == 1:                   # если Семён выиграл первый раз
        
            show sh surprise pioneer at cright with dspr
            th "(Семён победил в первой игре)."
            sh "{i}(Следует обмен мнениями по этому поводу).{/i}"
            
        elif alt_day2_current_rout_status == 2:                 # если Семён отыгрался
        
            show sh serious pioneer at cright with dspr
            th "(Семён сравнял счёт в партии)."
            sh "{i}(Следует обмен мнениями по этому поводу).{/i}"
            
        elif alt_day2_current_rout_status == 3:                 # и он выиграл первый раз
        
            show sh normal pioneer at cright with dspr
            th "(Шурик победил в первой игре)."
            sh "{i}(Следует обмен мнениями по этому поводу).{/i}"
            
        elif alt_day2_current_rout_status == 4:                 # и он отыгрался
        
            show sh smile pioneer at cright with dspr
            th "(Шурик сравнял счёт в партии)."
            sh "{i}(Следует обмен мнениями по этому поводу).{/i}"
            
# ============================================================= ВОПРОС — эксперименты Шурика -?
        if alt_day2_current_rout_status in [3,4]:                               # Если Шурик выиграл игру
            if alt_day2_gambler_behavior == 'defense':                          # если Шурик защищался
                sh "Ага, «защитный» алгоритм работает; это радует."
            elif alt_day2_gambler_behavior == 'gamble':                         # если Шурик рисковал
                sh "В этой игре риск себя иногда оправдывает."
            else:                                                               # Шурик сливался
                sh "Странно, но алгоритм игры «в поддавки» на сей раз не сработал."
        else:                                                                   # если Шурик проиграл игру
            if alt_day2_gambler_behavior == 'defense':                          # если Шурик защищался
                sh "Не сработал «защитный» алгоритм."
            elif alt_day2_gambler_behavior == 'gamble':                         # если Шурик рисковал
                sh "М-да, на сей раз риск не оправдался."
            else:                                                               # Шурик сливался
                sh "Так, игра «в поддавки» получилась, как и было задумано."
        sh "Ладно, буду экспериментировать дальше."
# ============================================================= /ВОПРОС
            
# Женя
    elif alt_spr_my_rival == 'mz':
        show mz normal pioneer at cright with dspr
        if alt_day2_current_rout_status == 1:                   # если Семён выиграл первый раз
        
            th "(Семён победил в первой игре)."
            mz "{i}(Следует обмен мнениями по этому поводу).{/i}"
            
        elif alt_day2_current_rout_status == 2:                 # если Семён отыгрался
        
            th "(Семён сравнял счёт в партии)."
            mz "{i}(Следует обмен мнениями по этому поводу).{/i}"
            
        elif alt_day2_current_rout_status == 3:                 # и она выиграла первый раз
        
            th "(Женя победила в первой игре)."
            mz "{i}(Следует обмен мнениями по этому поводу).{/i}"
            
        elif alt_day2_current_rout_status == 4:                 # и она отыгралась
        
            th "(Женя сравняла счёт в партии)."
            mz "{i}(Следует обмен мнениями по этому поводу).{/i}"

            
            
    show el normal pioneer far at left
    if alt_day2_current_rout_status == 1:
        el "В этой игре победил Семён, счёт 1-0 в его пользу."
    elif alt_day2_current_rout_status == 3:
        if alt_spr_my_rival == 'sh':                            # Шурик
            el "В этой игре победил Шурик, счёт 1-0 в его пользу."
        else:
            el "В этой игре %(alt_name_my_rival_i)s побеждает и ведёт в партии со счётом 1-0."
    elif alt_day2_current_rout_status == 2:
        el "Семён выигрывает и сравнивает счёт в раунде."
    elif alt_day2_current_rout_status == 4:
        if alt_spr_my_rival == 'sh':                            # Шурик
            el "Шурик выигрывает и сравнивает счёт в раунде."
        else:
            el "%(alt_name_my_rival_i)s победила и сравняла счёт в партии."
    return
        
#-----------------------------------------------------------------------------------
# Результат КОНА (называем счёт по играм)
label alt_day2_summary_poker_round:
    if alt_day2_result_tour in [1,11,21]:                                                                     # Если проигрыш в КОНЕ     #moded
        if alt_day2_result_tour == 1:
            $ alt_day2_stage_tournament = 'первый тур'
        elif alt_day2_result_tour == 11:
            $ alt_day2_stage_tournament = 'полуфинал'
        elif alt_day2_result_tour == 21:
            $ alt_day2_stage_tournament = 'финальный раунд'
        if alt_day2_detour_1_tour:                                                                     # если скипаем тур
            $ alt_day2_my_win = renpy.random.choice([1,0])                                              # рандомно выигрыш Семёна 0 или 1
        if alt_day2_my_win == 0:                                                                        # если проигравший не выигрывал
            "Я проиграл %(alt_day2_stage_tournament)s %(alt_name_my_rival_d)s, причём всухую."
        else:
            "Я пытался сопротивляться: победитель определился только в третьей игре."
            "Но, как бы там ни было, %(alt_day2_stage_tournament)s %(alt_name_my_rival_d)s я проиграл."
            
    elif alt_day2_result_tour in [2,12,22]:                                                                   # Если выигрыш в КОНЕ     #moded
        if alt_day2_result_tour == 2:
            if alt_day2_revanche:
                $ alt_day2_stage_tournament = 'в матч-реванше'
            else:
                $ alt_day2_stage_tournament = 'в первом туре'
        elif alt_day2_result_tour == 12:
            $ alt_day2_stage_tournament = 'в полуфинале'
        elif alt_day2_result_tour == 22:
            $ alt_day2_stage_tournament = 'в финале'
        if alt_day2_detour_1_tour:                                                                      # если скипаем тур
            $ alt_day2_rival_win = renpy.random.choice([1,0])                                           # рандомно выигрыш соперника 0 или 1
        if alt_day2_rival_win == 0:                                                                     # если проигравший не выигрывал
            "У %(alt_name_my_rival_r)s %(alt_day2_stage_tournament)s я выиграл «всухую», без особых проблем."
        else:
            if alt_spr_my_rival == 'sh':                        # Шурик
                "В %(alt_day2_stage_tournament)s %(alt_name_my_rival_i)s проявил упорство — потребовалась решающая игра."
                "Тем не менее я выиграл, хотя не скажу, что это было просто."
            else:                                               # девчонки
                "%(alt_name_my_rival_i)s оказала упорное сопротивление и даже смогла выиграть у меня один раз."
                "Но в третьей игре и, соответственно, %(alt_day2_stage_tournament)s я всё-таки победил."

    return

#-----------------------------------------------------------------------------------
# АНАЛИЗАТОР 1-го ТУРА
label alt_day2_1_tour_analizer:
    window hide
    $ alt_table_no = 0                                                                  # № стола = 1 (начинаем с НУЛЯ в этом случае)
    $ alt_mstt = 0                                                                      # обнуляем глобальный счетчик таблицы
    call show_tournament_table                                                          #  показываем исходное положение ??? сортируем игроков ???
    $ alt_result_dv_1_tour = alt_get_result_dv(alt_day2_gamblers_1_tour)                # а где там наша ДваЧе?
    $ renpy.pause(1)
    $ alt_random_box_1 = range(1,len(alt_table_winner)+1)                          # черный ящик 1 — список от 1 до длины победителей +1
    $ alt_random_box_2 = range(1,len(alt_table_loser)+1)                          # черный ящик 2 — список от 1 до длины проигравших +1
    window show
    while alt_table_no <= 4:                                                # перебираем столы от 1 до 4
    #результат, игроки, высказывания — по номеру стола
        $ results_at_table,gambler_win,winner_remark,loser_preface,loser_remark = alt_declare_results_tables(alt_table_no, alt_day2_gamblers_1_tour) 
        "%(results_at_table)s"                                                          # оглашаем результат за столом
        call show_tournament_table                                                      # переход по метке — вызов очередной фишки
        extend " %(gambler_win)s."                                                      # выводим в окно имя победителя
        $ a_c_i = 0                                                                     # счетчик фраз
        while a_c_i < len(winner_remark):                                               # пока счетчик фраз меньше их количества
            $ alt_gambler_saying = winner_remark[a_c_i][0]                              # кто говорит
            $ alt_gambler_remark = winner_remark[a_c_i][1]                              # фраза
            if alt_gambler_saying != None:                                              # если определено, от кого фраза
                alt_gambler_saying "%(alt_gambler_remark)s"                             # выводим её от лица говорящего
            else:                                                                       # если "от автора"
                "%(alt_gambler_remark)s"                                                # выводим фразу "от автора"
            $ a_c_i += 1                                                                # увеличиваем счетчик фраз
        "%(loser_preface)s"                                                             # выводим проигравшего
        call show_tournament_table                                                      # переход по метке — вызов очередной фишки
        $ a_c_i = 0                                                                     # счетчик фраз
        while a_c_i < len(loser_remark):                                                # пока счетчик фраз меньше их количества
            $ alt_gambler_saying = loser_remark[a_c_i][0]                               # кто говорит
            $ alt_gambler_remark = loser_remark[a_c_i][1]                               # фраза
            if alt_gambler_saying != None:                                              # если определено, от кого фраза
                alt_gambler_saying "%(alt_gambler_remark)s"                             # выводим её от лица говорящего
            else:                                                                       # если "от автора"
                "%(alt_gambler_remark)s"                                                # выводим фразу "от автора"
            $ a_c_i += 1                                                                # увеличиваем счетчик фраз
        $ alt_table_no += 1                                                             # следующий стол
    return
    
#-----------------------------------------------------------------------------------
# АНАЛИЗАТОР ПОЛУФИНАЛА
label alt_day2_semifinal_analizer:
    window hide
    $ alt_table_no = 4                                                                  # № стола = 4 (начинаем с четвертого в этом случае)
    $ alt_mstt = 0                                                                      # обнуляем глобальный счетчик таблицы
    call show_tournament_table                                                          #  показываем исходное положение ??? сортируем игроков ???
    $ renpy.pause(1)
    $ alt_random_box_1 = range(1,len(alt_table_winner)+1)                               # черный ящик 1 — список от 1 до длины победителей +1
    $ alt_random_box_2 = range(1,len(alt_table_loser)+1)                                # черный ящик 2 — список от 1 до длины проигравших +1
    window show
    while alt_table_no <= 6:                                                            # перебираем столы 5-6
    #результат, игроки, высказывания — по номеру стола
        $ results_at_table,gambler_win,winner_remark,loser_preface,loser_remark = alt_declare_results_tables(alt_table_no, alt_day2_gamblers_semifinal)
        "%(results_at_table)s"                                                          # оглашаем результат за столом
        call show_tournament_table                                                      # переход по метке — вызов очередной фишки
        extend " %(gambler_win)s."                                                      # выводим в окно имя победителя
        $ a_c_i = 0                                                                     # счетчик фраз
        while a_c_i < len(winner_remark):                                               # пока счетчик фраз меньше их количества
            $ alt_gambler_saying = winner_remark[a_c_i][0]                              # кто говорит
            $ alt_gambler_remark = winner_remark[a_c_i][1]                              # фраза
            if alt_gambler_saying != None:                                              # если определено, от кого фраза
                alt_gambler_saying "%(alt_gambler_remark)s"                             # выводим её от лица говорящего
            else:                                                                       # если "от автора"
                "%(alt_gambler_remark)s"                                                # выводим фразу "от автора"
            $ a_c_i += 1                                                                # увеличиваем счетчик фраз
        "%(loser_preface)s"                                                             # выводим проигравшего
        call show_tournament_table                                                      # переход по метке — вызов очередной фишки
        $ a_c_i = 0                                                                     # счетчик фраз
        while a_c_i < len(loser_remark):                                                # пока счетчик фраз меньше их количества
            $ alt_gambler_saying = loser_remark[a_c_i][0]                               # кто говорит
            $ alt_gambler_remark = loser_remark[a_c_i][1]                               # фраза
            if alt_gambler_saying != None:                                              # если определено, от кого фраза
                alt_gambler_saying "%(alt_gambler_remark)s"                             # выводим её от лица говорящего
            else:                                                                       # если "от автора"
                "%(alt_gambler_remark)s"                                                # выводим фразу "от автора"
            $ a_c_i += 1                                                                # увеличиваем счетчик фраз
        $ alt_table_no += 1                                                             # следующий стол
    return
    
#-----------------------------------------------------------------------------------
# АНАЛИЗАТОР ФИНАЛА
label alt_day2_final_analizer:
    $ alt_mstt = 3
    call show_tournament_table                                                          # показываем исходное положение, сортируем игроков

    $ alt_take_tournament_winner = alt_day2_gamblers_final[0].take                      # Ник победителя
    if alt_take_tournament_winner == "me":
        $ alt_name_tournament_winner = "Семёна"
    else:
        $ alt_name_tournament_winner = alt_day2_gamblers_final[0].name['v']             #  Получаем имя победителя турнира
                 
    $ alt_take_tournament_loser = alt_day2_gamblers_final[1].take                       # Ник проигравшего
    if alt_take_tournament_loser == "me":
        $ alt_name_tournament_loser = "Семёну"
    else:
        $ alt_name_tournament_loser = alt_day2_gamblers_final[1].name['d']              #  Получаем имя проигравшего в финале
    
    if alt_take_tournament_loser in ['me','sh']:
        $ alt_pronomen_final_loser = "он"
    else:
        $ alt_pronomen_final_loser = "она"
        
    $ winner_remark, loser_remark = alt_declare_results_final(alt_take_tournament_winner, alt_take_tournament_loser) # вызываем функцию на финал — фразы победителя, проигравшего — по их никам.
    

#внимание: далее идёт текст авторства тов. nuttyprof. Ещё нужно будет подумать над переходами, если мы не участвовали в турнире (вылетели раньше)
# ========================================================================== отсебятина
# TODO Окончание тура — под переделку фраз ????

    el "Итак, турнир окончен."
    "Вспомнил о своих обязанностях организатор."
    $ alt_mstt = 0
    el "Поздравляем нашего победителя — %(alt_name_tournament_winner)s!"
    play sound sfx_concert_applause
    call show_tournament_table                                                          # двигаем победителя
    $ renpy.pause(0.2, hard=True)
    
    $ a_c_i = 0                                                                     # счетчик фраз
    while a_c_i < len(winner_remark):                                               # пока счетчик фраз меньше их количества
        $ alt_gambler_saying = winner_remark[a_c_i][0]                              # кто говорит
        $ alt_gambler_remark = winner_remark[a_c_i][1]                              # фраза
        if alt_gambler_saying != None:                                              # если определено, от кого фраза
            alt_gambler_saying "%(alt_gambler_remark)s"                             # выводим её от лица говорящего
        else:                                                                       # если "от автора"
            "%(alt_gambler_remark)s"                                                # выводим фразу "от автора"
        $ a_c_i += 1                                                                # увеличиваем счетчик фраз
        
    $ alt_mstt +=1
    el "А вот %(alt_name_tournament_loser)s сегодня немного не повезло; тем не менее, %(alt_pronomen_final_loser)s занимает почётное второе место."
    call show_tournament_table                                                      # прячем проигравшего
    $ renpy.pause(0.2, hard=True)
    
    $ a_c_i = 0                                                                     # счетчик фраз
    while a_c_i < len(loser_remark):                                                # пока счетчик фраз меньше их количества
        $ alt_gambler_saying = loser_remark[a_c_i][0]                               # кто говорит
        $ alt_gambler_remark = loser_remark[a_c_i][1]                               # фраза
        if alt_gambler_saying != None:                                              # если определено, от кого фраза
            alt_gambler_saying "%(alt_gambler_remark)s"                             # выводим её от лица говорящего
        else:                                                                       # если "от автора"
            "%(alt_gambler_remark)s"                                                # выводим фразу "от автора"
        $ a_c_i += 1                                                                # увеличиваем счетчик фраз
# ========================================================================== /отсебятина
    return




# --------------------------------------------------------------------------
# Подготовка перехода на ужин: — очистка слоя, разблокировка роллбака
label alt_day2_prepare_transition_to_supper:
    window hide
    python:
        renpy.scene('underlay')
    if not (alt_day2_revanche and (alt_day2_result_tour == 1)):
        $ alt_who_how_plays_poker()                                                         # посмотрели, кто и как сыграл
    else:
        $ alt_day2_gamblers_result['me'] = 1
        if alt_my_rival_1_tour.take == 'us':
            $ alt_day2_gamblers_result['us'] = 2
        elif alt_my_rival_1_tour.take == 'un':
            $ alt_day2_gamblers_result['un'] = 2
        $ alt_my_rival_semifinal = alt_my_rival_1_tour
        $ alt_my_rival_final = alt_my_rival_1_tour
        $ alt_my_rival_semifinal.take = None
        $ alt_my_rival_final.take = None
    if alt_day2_gamblers_result['me'] <= 11:
        $ alt_my_rival_final.take = None
        if alt_day2_gamblers_result['me'] == 1:
            $ alt_my_rival_semifinal.take = None
        
# -------------------------------------------------------------------------
# УБРАТЬ после согласования переменных
    if alt_my_rival_1_tour.take == 'un':                # Если соперник в 1 туре — Лена
        $ alt_pe = 1
        if alt_day2_gamblers_result['un'] > 2:          # .. и если её результат больше 2
            $ alt_day2_fail = 1
    if alt_day2_gamblers_result['un'] in [2,11]:        # Лена, как минимум, добралась до полуфинала
        $ alt_day2_hf2 = 1
    if alt_my_rival_semifinal.take == 'us':             # Ульяна — соперник в полуфинале
        $ alt_day2_hf2 = 5
        if alt_day2_gamblers_result['me'] >= 21:        # и если Семён её победил
            $ alt_day2_round3 = 1
    if alt_day2_gamblers_result['us'] == 22:            # Ульяна — победитель турнира
        $ alt_day2_f1 = 5
        $ alt_day2_round3 = 1
    if alt_day2_gamblers_result['mi'] >= 21:            # Мику, как минимум, вышла в финал
        $ alt_day2_f1 = 4
    if alt_day2_gamblers_result['un'] >= 21:            # Лена, как минимум, вышла в финал
        $ alt_day2_f1 = 1
        if alt_day2_gamblers_result['me'] == 21:        # А дальше немного плясок с бубном — для правильного выхода на строку
            $ alt_day2_round3 = 1
        elif alt_day2_gamblers_result['me'] < 20:
            $ alt_day2_round3 = 3
    if alt_day2_gamblers_result['me'] == 22:            # Семён выиграл турнир
        $ alt_day2_round3 = 2
        $ alt_day2_dv_bet_won = 1                       # Вопрос ?????
    if alt_day2_gamblers_result['me'] == 1:             # Семён проиграл в 1 туре
        $ alt_day2_round1 = 1
    if alt_day2_gamblers_result['me'] == 11:            # Семён проиграл в полуфинале
        $ alt_day2_round2 = 1
    if (alt_day2_gamblers_result['me'] < alt_day2_gamblers_result['dv']) or (alt_day2_gamblers_result['me'] == 1):
        $ alt_day2_dv_bet_won = 2                       # Алиса прошла дальше Семёна или наравне (напр, оба продули в 1 туре или 1\2)
    if alt_my_rival_final.take == 'mi':                 # Мику — соперник Семёна в финале
        $ alt_day2_f1 = 4
    if alt_day2_gamblers_result['me'] > 1:              # Семён, по крайней мере, не проиграл в 1 туре
        $ alt_day2_fail = 0
    if (alt_my_rival_1_tour.take == 'un') and (alt_day2_gamblers_result['me'] == 1): # Семён проиграл Лене в 1 туре.
        $ alt_day2_fail = 1
    if (alt_day2_gamblers_result['me'] <= 21) and (alt_day2_dv_bet_won != 2):            # Семён НЕ выиграл турнир
        $ alt_day2_dv_bet_won = 0
# -------------------------------------------------------------------------

    $ d2_cardgame_block_rollback = False
    jump alt_day2_supper 
    
