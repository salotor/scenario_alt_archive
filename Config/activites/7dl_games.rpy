label alt_day3_miku_rhymes_in:
    label alt_day3_miku_rhymes_start:
        #Мини-игра с подбором рифмы.
        me "Ну давай попробуем."
        mi "Хорошо."
        "Она взяла гитару и наиграла первую строфу."
        "Ещё раз."
        "И ещё."
        "Пока я не запомнил."
        mi "Справишься?"
        "Я кивнул и взял в руки гитару."
        mi "И?"
        "После нескольких попыток, я сумел выдавить из инструмента нечто, похожее на мелодию."
        mi "Отлично!"
        "Мику схватила карандаш и застрочила по бумаге."
        show mi sad pioneer with dspr
        "Потом остановилась и перечеркала всё."
        mi "Не то. Нет, не то."
        "Бормотала она себе под нос."
        mi "И это тоже."
        mi "Сенечка, поможешь?"
        me "Да, конечно. Что такое?"
        mi "Мне нужно стишок сочинить… Слова к песне…"
        mi "Но что-то не получается. Может, ты попробуешь?"
        me "Давай."
        mi "Система достаточно простая - выбираешь настроение первой строки, потом второй, и так далее."
        me "Похоже, ничего сложного."
    init:
        $ rhyme_tone = 0
        $ rhyme_tone1 = 0
        $ rhyme_tone2 = 0
        $ rhyme_tone3 = 0
        $ rhyme_tone4 = 0
        $ rhyme_tone5 = 0
        $ rhyme_tone6 = 0
        $ rhyme_tone7 = 0
        $ rhyme_tone8 = 0
        $ rhyme_tone9 = 0

        
    label rhyme_start:
        show mi smile pioneer with dspr
        mi "Итак, какое настроение у первой строки? От одного до десяти."
        menu:
            "1":
                $ rhyme_tone = 1
            "2":
                $ rhyme_tone = 2
            "3":
                $ rhyme_tone = 3
            "4":
                $ rhyme_tone = 4
            "5":
                $ rhyme_tone = 5
            "6":
                $ rhyme_tone = 6
            "7":
                $ rhyme_tone = 7
            "8":
                $ rhyme_tone = 8
            "9":
                $ rhyme_tone = 9
            "10":
                $ rhyme_tone = 10

        mi "Отлично! Теперь я могу дописывать стишок на основе выбранного тобой настроения, или ты можешь выбрать дальше."
        menu:
            "Жги!":
                mi "Итак!"
                $ rhyme_tone1 = rhyme_tone
                $ rhyme_tone2 = rhyme_tone
                $ rhyme_tone3 = rhyme_tone
                $ rhyme_tone4 = rhyme_tone
                $ rhyme_tone5 = rhyme_tone
                $ rhyme_tone6 = rhyme_tone
                $ rhyme_tone7 = rhyme_tone
                $ rhyme_tone8 = rhyme_tone
                $ rhyme_tone9 = rhyme_tone
                jump alt_rhyme_reading
            "Выберу ещё!":
                $ rhyme_tone1 = renpy.random.randint(1, 10)
                $ rhyme_tone2 = renpy.random.randint(1, 10)
                mi "Хорошо! Какое настроение у следующего отрывка от 1 до 10?"
                menu:
                    "1":
                        $ rhyme_tone3 = 1
                    "2":
                        $ rhyme_tone3 = 2
                    "3":
                        $ rhyme_tone3 = 3
                    "4":
                        $ rhyme_tone3 = 4
                    "5":
                        $ rhyme_tone3 = 5
                    "6":
                        $ rhyme_tone3 = 6
                    "7":
                        $ rhyme_tone3 = 7
                    "8":
                        $ rhyme_tone3 = 8
                    "9":
                        $ rhyme_tone3 = 9
                    "10":
                        $ rhyme_tone3 = 10
        $ rhyme_tone4 = renpy.random.randint(1, 10)
        mi "Очень хорошо! Теперь, раз уж выбрал вторую строчку, выбирай и остальные две!"
        $ rhyme_tone6 = renpy.random.randint(1, 10)
        menu:
            "1":
                $ rhyme_tone5 = 1
            "2":
                $ rhyme_tone5 = 2
            "3":
                $ rhyme_tone5 = 3
            "4":
                $ rhyme_tone5 = 4
            "5":
                $ rhyme_tone5 = 5
            "6":
                $ rhyme_tone5 = 6
            "7":
                $ rhyme_tone5 = 7
            "8":
                $ rhyme_tone5 = 8
            "9":
                $ rhyme_tone5 = 9
            "10":
                $ rhyme_tone5 = 10
        mi "И последняя строчка!"
        $ rhyme_tone8 = renpy.random.randint(1, 10)
        $ rhyme_tone9 = renpy.random.randint(1, 10)
        menu:
            "1":
                $ rhyme_tone7 = 1
            "2":
                $ rhyme_tone7 = 2
            "3":
                $ rhyme_tone7 = 3
            "4":
                $ rhyme_tone7 = 4
            "5":
                $ rhyme_tone7 = 5
            "6":
                $ rhyme_tone7 = 6
            "7":
                $ rhyme_tone7 = 7
            "8":
                $ rhyme_tone7 = 8
            "9":
                $ rhyme_tone7 = 9
            "10":
                $ rhyme_tone7 = 10
    label alt_rhyme_reading:
        if rhyme_tone == 1:
            $ alt_rhyme_tone = "Я помню"
        if rhyme_tone == 2:
            $ alt_rhyme_tone = "Не помню"
        if rhyme_tone == 3:
            $ alt_rhyme_tone = "Забыть бы"
        if rhyme_tone == 4:
            $ alt_rhyme_tone = "Купите"
        if rhyme_tone == 5:
            $ alt_rhyme_tone = "И на фиг"
        if rhyme_tone == 6:
            $ alt_rhyme_tone = "Какое"
        if rhyme_tone == 7:
            $ alt_rhyme_tone = "Угробил"
        if rhyme_tone == 8:
            $ alt_rhyme_tone = "Не очень"
        if rhyme_tone == 9:
            $ alt_rhyme_tone = "Открою"
        if rhyme_tone == 10:
            $ alt_rhyme_tone = "Ты чуешь?"
        
        if rhyme_tone1 == 1:
            $ alt_rhyme_tone1 = "чудное"
        if rhyme_tone1 == 2:
            $ alt_rhyme_tone1 = "странное"
        if rhyme_tone1 == 3:
            $ alt_rhyme_tone1 = "некое"
        if rhyme_tone1 == 4:
            $ alt_rhyme_tone1 = "вкусное"
        if rhyme_tone1 == 5:
            $ alt_rhyme_tone1 = "пьяное"
        if rhyme_tone1 == 6:
            $ alt_rhyme_tone1 = "свинское"
        if rhyme_tone1 == 7:
            $ alt_rhyme_tone1 = "чёткое"
        if rhyme_tone1 == 8:
            $ alt_rhyme_tone1 = "сраное"
        if rhyme_tone1 == 9:
            $ alt_rhyme_tone1 = "нужное"
        if rhyme_tone1 == 10:
            $ alt_rhyme_tone1 = "конское"
        
        if rhyme_tone2 == 1:
            $ alt_rhyme_tone2 = "мгновенье"
        if rhyme_tone2 == 2:
            $ alt_rhyme_tone2 = "затменье"
        if rhyme_tone2 == 3:
            $ alt_rhyme_tone2 = "хотенье"
        if rhyme_tone2 == 4:
            $ alt_rhyme_tone2 = "варенье"
        if rhyme_tone2 == 5:
            $ alt_rhyme_tone2 = "творенье"
        if rhyme_tone2 == 6:
            $ alt_rhyme_tone2 = "везенье"
        if rhyme_tone2 == 7:
            $ alt_rhyme_tone2 = "рожденье"
        if rhyme_tone2 == 8:
            $ alt_rhyme_tone2 = "смущенье"
        if rhyme_tone2 == 9:
            $ alt_rhyme_tone2 = "печенье"
        if rhyme_tone2 == 10:
            $ alt_rhyme_tone2 = "ученье"

        if rhyme_tone3 == 1:
            $ alt_rhyme_tone3 = "Передо мной"
        if rhyme_tone3 == 2:
            $ alt_rhyme_tone3 = "Под косячком"
        if rhyme_tone3 == 3:
            $ alt_rhyme_tone3 = "На кладбище"
        if rhyme_tone3 == 4:
            $ alt_rhyme_tone3 = "В моих мечтах"
        if rhyme_tone3 == 5:
            $ alt_rhyme_tone3 = "Под скальпелем"
        if rhyme_tone3 == 6:
            $ alt_rhyme_tone3 = "В моих штанах"
        if rhyme_tone3 == 7:
            $ alt_rhyme_tone3 = "Из-за угла"
        if rhyme_tone3 == 8:
            $ alt_rhyme_tone3 = "Промеж ушей"
        if rhyme_tone3 == 9:
            $ alt_rhyme_tone3 = "В ночном горшке"
        if rhyme_tone3 == 10:
            $ alt_rhyme_tone3 = "Из головы"
        
        if rhyme_tone4 == 1:
            $ alt_rhyme_tone4 = "явилась ты"
        if rhyme_tone4 == 2:
            $ alt_rhyme_tone4 = "добилась ты"
        if rhyme_tone4 == 3:
            $ alt_rhyme_tone4 = "торчат кресты"
        if rhyme_tone4 == 4:
            $ alt_rhyme_tone4 = "стихов листы"
        if rhyme_tone4 == 5:
            $ alt_rhyme_tone4 = "забилась ты"
        if rhyme_tone4 == 6:
            $ alt_rhyme_tone4 = "мои трусы"
        if rhyme_tone4 == 7:
            $ alt_rhyme_tone4 = "поют дрозды"
        if rhyme_tone4 == 8:
            $ alt_rhyme_tone4 = "из темноты"
        if rhyme_tone4 == 9:
            $ alt_rhyme_tone4 = "помылась ты"
        if rhyme_tone4 == 10:
            $ alt_rhyme_tone4 = "удар поддых"
        
        if rhyme_tone5 == 1:
            $ alt_rhyme_tone5 = "мимолётное"
        if rhyme_tone5 == 2:
            $ alt_rhyme_tone5 = "детородное"
        if rhyme_tone5 == 3:
            $ alt_rhyme_tone5 = "психотропное"
        if rhyme_tone5 == 4:
            $ alt_rhyme_tone5 = "нейролептиков"
        if rhyme_tone5 == 5:
            $ alt_rhyme_tone5 = "очевидное"
        if rhyme_tone5 == 6:
            $ alt_rhyme_tone5 = "невменяемо"
        if rhyme_tone5 == 7:
            $ alt_rhyme_tone5 = "нам не чуждое"
        if rhyme_tone5 == 8:
            $ alt_rhyme_tone5 = "благородное"
        if rhyme_tone5 == 9:
            $ alt_rhyme_tone5 = "межушанское"
        if rhyme_tone5 == 10:
            $ alt_rhyme_tone5 = "зело злобное"
        
        if rhyme_tone6 == 1:
            $ alt_rhyme_tone6 = "виденье"
        if rhyme_tone6 == 2:
            $ alt_rhyme_tone6 = "сиденье"
        if rhyme_tone6 == 3:
            $ alt_rhyme_tone6 = "паренье"
        if rhyme_tone6 == 4:
            $ alt_rhyme_tone6 = "сужденье"
        if rhyme_tone6 == 5:
            $ alt_rhyme_tone6 = "вращенье"
        if rhyme_tone6 == 6:
            $ alt_rhyme_tone6 = "сношенье"
        if rhyme_tone6 == 7:
            $ alt_rhyme_tone6 = "смятенье"
        if rhyme_tone6 == 8:
            $ alt_rhyme_tone6 = "паденье"
        if rhyme_tone6 == 9:
            $ alt_rhyme_tone6 = "сплетенье"
        if rhyme_tone6 == 10:
            $ alt_rhyme_tone6 = "бухтенье"
        
        if rhyme_tone7 == 1:
            $ alt_rhyme_tone7 = "гений"
        if rhyme_tone7 == 2:
            $ alt_rhyme_tone7 = "сторож"
        if rhyme_tone7 == 3:
            $ alt_rhyme_tone7 = "символ"
        if rhyme_tone7 == 4:
            $ alt_rhyme_tone7 = "булки"
        if rhyme_tone7 == 5:
            $ alt_rhyme_tone7 = "правда"
        if rhyme_tone7 == 6:
            $ alt_rhyme_tone7 = "ангел"
        if rhyme_tone7 == 7:
            $ alt_rhyme_tone7 = "водка"
        if rhyme_tone7 == 8:
            $ alt_rhyme_tone7 = "пиво"
        if rhyme_tone7 == 9:
            $ alt_rhyme_tone7 = "злоба"
        if rhyme_tone7 == 10:
            $ alt_rhyme_tone7 = "зависть"
        
        if rhyme_tone8 == 1:
            $ alt_rhyme_tone8 = "чистой"
        if rhyme_tone8 == 2:
            $ alt_rhyme_tone8 = "вечной"
        if rhyme_tone8 == 3:
            $ alt_rhyme_tone8 = "тухлой"
        if rhyme_tone8 == 4:
            $ alt_rhyme_tone8 = "просит"
        if rhyme_tone8 == 5:
            $ alt_rhyme_tone8 = "грязной"
        if rhyme_tone8 == 6:
            $ alt_rhyme_tone8 = "типа"
        if rhyme_tone8 == 7:
            $ alt_rhyme_tone8 = "стрёмной"
        if rhyme_tone8 == 8:
            $ alt_rhyme_tone8 = "в пене"
        if rhyme_tone8 == 9:
            $ alt_rhyme_tone8 = "жаждет"
        if rhyme_tone8 == 10:
            $ alt_rhyme_tone8 = "женской"
        
        if rhyme_tone9 == 1:
            $ alt_rhyme_tone9 = "красоты"
        if rhyme_tone9 == 2:
            $ alt_rhyme_tone9 = "мерзлоты"
        if rhyme_tone9 == 3:
            $ alt_rhyme_tone9 = "суеты"
        if rhyme_tone9 == 4:
            $ alt_rhyme_tone9 = "наркоты"
        if rhyme_tone9 == 5:
            $ alt_rhyme_tone9 = "срамоты"
        if rhyme_tone9 == 6:
            $ alt_rhyme_tone9 = "школоты"
        if rhyme_tone9 == 7:
            $ alt_rhyme_tone9 = "пустоты"
        if rhyme_tone9 == 8:
            $ alt_rhyme_tone9 = "простоты"
        if rhyme_tone9 == 9:
            $ alt_rhyme_tone9 = "гопоты"
        if rhyme_tone9 == 10:
            $ alt_rhyme_tone9 = "наготы"
        "Мику откашлялась, расправила плечи и с выражением прочитала:"
        mi "%(alt_rhyme_tone)s %(alt_rhyme_tone1)s %(alt_rhyme_tone2)s — \n%(alt_rhyme_tone3)s %(alt_rhyme_tone4)s !"
        mi "Как %(alt_rhyme_tone5)s %(alt_rhyme_tone6)s,\nКак %(alt_rhyme_tone7)s %(alt_rhyme_tone8)s %(alt_rhyme_tone9)s !"
        mi "Понравилось?"
        if rhyme_tone1 == 1:
            me "Что-то пушкиновщиной отдаёт."
            mi "Спасибо! Я старалась!"
        else:
            me "Супер!"
            "Ответил я."
    mi "Ещё разок?"
    menu:
        "Давай!":
            jump alt_day3_miku_rhymes_start
        "Хватит пока!":
            return
    me "Ну, я, пожалуй, пойду."
    mi "Да, конечно. Увидимся завтра."
    mi "Или можешь перед ужином зайти, подберём тебе наряд для танцев. Хочешь?"
    me "Какой смысл? Мне всё равно танцевать не с кем."
    mi "А как же я?"
    me "Что?"
    mi "Я могу потанцевать с тобой."
    th "Вот уж спасибочки."
    me "Как будто непонятно что я в виду имел."
    "Вздохнул я и поплёлся полдничать."
    "Что же касается Лены…"
    if lp_un < 0:
        th "Я смолчу. Я смирюсь."
        th "Я прощу."
        $ lp_un = 0
    else:
        th "Буду пытаться дальше."
        $ lp_un += 1
    return
    
label RPS_game(alt_opp): # параметры вызова. Обязательный параметр - alt_opp
    
    #  кто что выбросил:
    $ sam_move = renpy.random.choice(["Камень", "Ножницы", "Бумага"])
    $ alt_opp_move = renpy.random.choice(["Камень", "Ножницы", "Бумага"])
    $ RPS_winner = 0 # 1 - player, -1 - alt_opp, 0 - draw
    
    $ alt_taunt = renpy.random.randint(1, 9) # Определяем порядок насмешек плюс очередность хода
    if alt_taunt == 1: 
        $ alt_rps_taunt_won = "Ура!"
        $ alt_rps_taunt_lose = "Ура…."
        $ alt_rps_taunt_draw = "Ещё раз."
    elif alt_taunt == 2: 
        $ alt_rps_taunt_won = "Победа!"
        $ alt_rps_taunt_lose = "Тебе повезло."
        $ alt_rps_taunt_draw = "Боевая ничья."
    elif alt_taunt == 3: 
        $ alt_rps_taunt_won = "И победителем становится… Я!"
        $ alt_rps_taunt_lose = "Жульничаешь, поди?"
        $ alt_rps_taunt_draw = "Повторим!"
    elif alt_taunt == 4: 
        $ alt_rps_taunt_won = "Вот так!"
        $ alt_rps_taunt_lose = "Вот блин!"
        $ alt_rps_taunt_draw = "Следующий кон!"
    elif alt_taunt == 5: 
        $ alt_rps_taunt_won = "Знай наших!"
        $ alt_rps_taunt_lose = "Не везёт, и всё тут!"
        $ alt_rps_taunt_draw = "Сначала."
    elif alt_taunt == 6: 
        $ alt_rps_taunt_won = "У тебя не было ни шанса!"
        $ alt_rps_taunt_lose = "Опять жульничаешь…"
        $ alt_rps_taunt_draw = "И ещё разок…"
    elif alt_taunt == 7: 
        $ alt_rps_taunt_won = "Повезло, конечно."
        $ alt_rps_taunt_lose = "Да что ты будешь делать!"
        $ alt_rps_taunt_draw = "Ничья."
    elif alt_taunt == 8: 
        $ alt_rps_taunt_won = "Ожидаемая победа."
        $ alt_rps_taunt_lose = "Ну да, твоя победа!"
        $ alt_rps_taunt_draw = "Никому не повезло."
    elif alt_taunt == 9: 
         $ alt_rps_taunt_won = "Да!"
         $ alt_rps_taunt_lose = "Нееееет!"
         $ alt_rps_taunt_draw = "Ну-ка, заново!"
    
    if alt_taunt > 5:
        if sam_move == "Камень":
            show sam_rock at left with zoomin
            with vpunch
            if alt_opp_move == "Ножницы":
                show miku_scissor at right with zoomin
                with vpunch
                alt_opp "%(alt_rps_taunt_lose)s"
                $ RPS_winner = 1
            if alt_opp_move == "Бумага":
                show miku_paper at right with zoomin
                with vpunch
                alt_opp "%(alt_rps_taunt_won)s"
                $ RPS_winner = -1
            if alt_opp_move == "Камень":
                show miku_rock at right with zoomin
                with vpunch
                alt_opp "%(alt_rps_taunt_draw)s"
                $ RPS_winner = 0
        elif sam_move == "Ножницы":
            show sam_scissor at left with zoomin
            with vpunch
            if alt_opp_move == "Ножницы":
                show miku_scissor at right with zoomin
                with vpunch
                alt_opp "%(alt_rps_taunt_draw)s"
                $ RPS_winner = 0
            if alt_opp_move == "Бумага":
                show miku_paper at right with zoomin
                with vpunch
                alt_opp "%(alt_rps_taunt_lose)s"
                $ RPS_winner = 1
            if alt_opp_move == "Камень":
                show miku_rock at right with zoomin
                with vpunch
                alt_opp "%(alt_rps_taunt_won)s"
                $ RPS_winner = -1
        elif sam_move == "Бумага":
            show sam_paper at left with zoomin
            with vpunch
            if alt_opp_move == "Ножницы":
                show miku_scissor at right with zoomin
                with vpunch
                alt_opp "%(alt_rps_taunt_won)s"
                $ RPS_winner = -1
            if alt_opp_move == "Бумага":
                show miku_paper at right with zoomin
                with vpunch
                alt_opp "%(alt_rps_taunt_draw)s"
                $ RPS_winner = 0
            if alt_opp_move == "Камень":
                show miku_rock at right with zoomin
                with vpunch
                alt_opp "%(alt_rps_taunt_lose)s"
                $ RPS_winner = 1
    else:
        if alt_opp_move == "Камень":
            show miku_rock at right with zoomin
            with vpunch
            if sam_move == "Ножницы":
                show sam_scissor at left with zoomin
                with vpunch
                me "%(alt_rps_taunt_lose)s"
                $ RPS_winner = -1
            if sam_move == "Бумага":
                show sam_paper at left with zoomin
                with vpunch
                me "%(alt_rps_taunt_won)s"
                $ RPS_winner = 1
            if sam_move == "Камень":
                show sam_rock at left with zoomin
                with vpunch
                me "%(alt_rps_taunt_draw)s"
                $ RPS_winner = 0
        elif alt_opp_move == "Ножницы":
            show miku_scissor at right with zoomin
            with vpunch
            if sam_move == "Ножницы":
                show sam_scissor at left with zoomin
                with vpunch
                me "%(alt_rps_taunt_draw)s"
                $ RPS_winner = 0
            if sam_move == "Бумага":
                show sam_paper at left with zoomin
                with vpunch
                me "%(alt_rps_taunt_lose)s"
                $ RPS_winner = -1
            if sam_move == "Камень":
                show sam_rock at left with zoomin
                with vpunch
                me "%(alt_rps_taunt_won)s"
                $ RPS_winner = 1
        elif alt_opp_move == "Бумага":
            show miku_paper at right with zoomin
            with vpunch
            if sam_move == "Ножницы":
                show sam_scissor at left with zoomin
                with vpunch
                me "%(alt_rps_taunt_won)s"
                $ RPS_winner = 1
            if sam_move == "Бумага":
                show sam_paper at left with zoomin
                with vpunch
                me "%(alt_rps_taunt_draw)s"
                $ RPS_winner = 0
            if sam_move == "Камень":
                show sam_rock at left with zoomin
                with vpunch
                me "%(alt_rps_taunt_lose)s"
                $ RPS_winner = -1
    return
    
#Антигаремник-кастратор!
label alt_day3_lp_checker(alt_dater):
    if alt_dater == un:
        $ lp_un += 1
        $ lp_sl -= 1
        $ lp_dv -= 1
        $ lp_mi -= 1
        if ('sl' in list_d2_date_7dl):
            $ lp_sl -= 1
        elif ('dv' in list_d2_date_7dl):
            $ lp_dv -= 1
        elif ('mi' in list_d2_date_7dl):
            $ lp_mi -= 1
        #Уникальная возможность огрести ещё минусов по флагам д3
        if alt_day3_event1 == 22: #Судим волейбол для Слави
            $ lp_sl -= 1
        elif alt_day3_event1 == 33: #Играем на гитарьке с ДваЧе
            $ lp_dv -= 1
        elif alt_day3_event2 == 43: #Потанцульки-обнимашки с Годзиллой
            $ lp_mi -= 1
        return
        
    elif alt_dater == sl:
        $ lp_un -= 1
        $ lp_sl += 1
        $ lp_dv -= 1
        $ lp_mi -= 1
        if ('un' in list_d2_date_7dl) or ('un_loki' in list_d2_date_7dl) or ('un_herc' in list_d2_date_7dl) or ('un_fz' in list_d2_date_7dl) or ('un' in list_d2_date_7dl)31:
            $ lp_un -= 1
        elif ('dv' in list_d2_date_7dl):
            $ lp_dv -= 1
        elif ('mi' in list_d2_date_7dl):
            $ lp_mi -= 1
            
        if alt_day3_event2 == 11 == 2:
            $ lp_un = lp_un
        elif alt_day3_event1 == 33:
            $ lp_dv -= 1
        elif alt_day3_event2 == 43:
            $ lp_mi -= 1
        return
        
    elif alt_dater == dv:
        $ lp_un -= 1
        $ lp_sl -= 1
        $ lp_dv += 1
        $ lp_mi -= 1
        if ('un' in list_d2_date_7dl) or ('un_loki' in list_d2_date_7dl) or ('un_herc' in list_d2_date_7dl) or ('un_fz' in list_d2_date_7dl) or ('un' in list_d2_date_7dl)31:
            $ lp_un -= 1
        elif ('sl' in list_d2_date_7dl):
            $ lp_sl -= 1
        elif ('mi' in list_d2_date_7dl):
            $ lp_mi -= 1
        
        if alt_day3_event2 == 11 == 2:
            $ lp_un -= 1
        elif alt_day3_event1 == 22:
            $ lp_sl -= 1
        elif alt_day3_event2 == 43:
            $ lp_mi -= 1
        return
        
    elif alt_dater == mi:
        $ lp_un -= 1
        $ lp_sl -= 1
        $ lp_dv -= 1
        $ lp_mi += 1
        if ('un' in list_d2_date_7dl) or ('un_loki' in list_d2_date_7dl) or ('un_herc' in list_d2_date_7dl) or ('un_fz' in list_d2_date_7dl) or ('un' in list_d2_date_7dl)31:
            $ lp_un -= 1
        elif ('sl' in list_d2_date_7dl):
            $ lp_sl -= 1
        elif ('dv' in list_d2_date_7dl):
            $ lp_dv -= 1

        if alt_day3_event2 == 11 == 2:
            $ lp_un -= 1
        elif alt_day3_event1 == 22:
            $ lp_sl -= 1
        elif alt_day3_event1 == 33:
            $ lp_dv -= 1
        return
        
label alt_shuffler:
    $ alt_pe = renpy.random.randint(1, 7) #Приоритет: оппонент Сэму
    return alt_pe

label alt_shuffler_pl1:
    $ alt_player1 = renpy.random.randint(1, 7) #Формируем первый стол:
    while alt_player1==alt_pe:
        $ alt_player1 = renpy.random.randint(1, 7)
    return alt_player1
label alt_shuffler_pl2:
    $ alt_player2 = renpy.random.randint(1, 7)
    while (alt_player1==alt_player2) or (alt_pe==alt_player2):
        $ alt_player2 = renpy.random.randint(1, 7)
    return alt_player2
label alt_shuffler_pl3:
    $ alt_player3 = renpy.random.randint(1, 7) #Формируем второй стол
    while (alt_player1==alt_player3) or (alt_player2==alt_player3) or (alt_pe==alt_player3):
        $ alt_player3 = renpy.random.randint(1, 7)
    return alt_player3
label alt_shuffler_pl4:
    $ alt_player4 = renpy.random.randint(1, 7)
    while (alt_player1==alt_player4) or (alt_player2==alt_player4) or (alt_player3==alt_player4) or (alt_pe==alt_player4):
        $ alt_player4 = renpy.random.randint(1, 7)
    return alt_player4
label alt_shuffler_pl5:
    $ alt_player5 = renpy.random.randint(1, 7) #Третий стол
    while (alt_player1==alt_player5) or (alt_player2==alt_player5) or (alt_player3==alt_player5) or (alt_player4==alt_player5) or (alt_pe==alt_player5):
        $ alt_player5 = renpy.random.randint(1, 7)
    return alt_player4
label alt_shuffler_pl6:
    $ alt_player6 = renpy.random.randint(1, 7)
    while (alt_player1==alt_player6) or (alt_player2==alt_player6) or (alt_player3==alt_player6) or (alt_player4==alt_player6) or (alt_player5==alt_player6) or (alt_pe==alt_player6):
        $ alt_player6 = renpy.random.randint(1, 7)
    return alt_player6
    
label alt_7dl_titles:
    scene bg black
    with dissolve2
    pause(1)
    show alt_credits alt_credits_text:
        xalign 0.5 
        ypos 1.3 
        linear 67.0 ypos -1.3 
    $ renpy.pause(67, hard=True)
    scene black
    with dissolve2
    stop music fadeout 3
    $ renpy.pause(4, hard=True)
    return
    
label alt_cotocombs:
    menu:
        "Открыть карту?":
            jump alt_cotocombs_map
        "Воспользоваться автопилотом.":
            "Я решил прислушаться к интуиции и, прикинув направление, зашагал в нужную сторону."
            return 
label alt_cotocombs_map:
    #Пилим DND-карту. Отдельным файлом, интеграция в шароёбства по котокомбам
    #Активный тайл-сет: 8х8, номерация тайлов с левого нижнего угла, старт с тайла 8, если идём со стороны старого лагеря, либо с тайла 64, если идём от Генды.
    #Ключи участия: alt_catac_wet(попал в воду), alt_ow_77 (односторонний спуск, закрывающий выход), alt_ow_73(односторонний проход через воду(засыпает породой))
    #Ключи прохождения alt_catac2 = True (открывает тайл на карте), alt_catac_came = 0 (расчёт, куда какой поворот смотрит.)
    #Погнали ништяки - собственно тайлы и пути.
    #Доступные тайлы:
    #2 -  вверх в 22 (мокрый)
    #6 - вверх в 26, вправо в 7  - доступна только с 7 (мокрый)
    #7 - влево к 6, вверх в 27, вправо в 8, 
    #8 - влево к 7, вправо к выходу (если  есть верёвка)
    #22 - вверх в 32(можно пробежаться до 72), вниз в 2
    #25 - вверх в 35 (шахта)
    #26 - вверх в 36, вправо в 27
    #27 - вниз в 7, и влево к 26
    #32 - вверх в 42, вниз в 22, вправо в 33(можно пробежаться до 36)
    #33 - влево в 32, вправо в 34  
    #34 - влево в 33, вправо в 35,  вверх в 41
    #35 - влево в 34, вправо в 36, вниз в 25
    #36 - влево в 35, вверх в 46
    #42 - вверх в 52, вниз в 32
    #44 - вверх в 54, вниз в 34
    #45 - вверх в 55
    #46 - вверх в 56, вниз в в 36
    #52 - вверх в 62, вниз в 42
    #54 - вниз в 44, вправо в 55
    #55 - вверх в 65, влево в 54, вправо в 56, вниз в 45(для д3 ключей)
    #56 - влево в 55, вниз в 46
    #62 - вверх в 72, вниз в 52
    #65 - вверх в 75, вниз в 55
    #68 - вверх в 78(шахта)
    #72 - вверх в 82, вниз в 72, вправо в 73
    #73 - вправо в 74(затяжное падение одностороннее)
    #74 - вверх в 84, попытаться влево в 73(хуюшки) (мокрый)
    #75 - вниз в 65, вверх в 85, вправо в 76
    #76 - влево в 75, вправо в 77
    #77 - влево в 76, вправо в 78(дверь)
    #78 - влево в 76(если есть верёвка), вверх в 88
    #82 - вниз в 72 (шахта)
    #83 - вправо в 82 (дикий ИИ Шурика), если мокрый, ёбнет током
    #84 - влево в 83(если ходил соло), вправо в 85, вниз в 74(мокрый)
    #85 - влево в 84, вниз в 75
    #88 - вверх в лагерь (комната с лестницей)
label alt_catac_tile2:
    $ alt_catac_tile2 = True
