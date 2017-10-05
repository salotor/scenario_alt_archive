label alt_day2_tournament_prep:
    scene bg int_dining_hall_sunset
    play music music_list["my_daily_life"] fadein 5
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
    "Мне в оппоненты рандом послал"
    call alt_shuffler
    
    scene bg int_dining_hall_sunset
    call alt_shuffler_pl1
    call alt_shuffler_pl2
    call alt_shuffler_pl3
    call alt_shuffler_pl4
    call alt_shuffler_pl5
    call alt_shuffler_pl6
    if alt_pe == 1:
        show un shy pioneer at cright with dspr
        extend " Лену."
        me "И снова добрый вечер."
        "Она смущённо улыбнулась, но ничего не сказала."

    elif alt_pe == 2:#
        show sl smile2 pioneer at cright with dspr
        extend " Славю."
        sl "Знаешь, я не очень хорошо в картах."
        me "Да я вообще ничего про эту игру не знаю."
        "Славя улыбнулась мне и села напротив."

    elif alt_pe == 3:
        show dv grin pioneer2 at cright with dspr
        extend " Алису."
        dv "Ну что, готов к сокрушительному поражению?"
        "Усмехнулась она, садясь на противоположное место."
        me "А как же. {w}Я принесу на твою могилку два гладиолуса."

    elif alt_pe == 4:#
        show mi smile pioneer at cright with dspr
        extend " Мику."
        mi "Ой, привет, Сенечка, а что за игра такая, ты не знаешь? А то меня позвали играть, а правила не объяснили."
        "Не переставая болтать, она села за стол и сложила руки."

    elif alt_pe == 5:#
        show us laugh pioneer at cright with dspr
        extend " Ульяну."
        us "Готов поддаваться?"
        me "И не мечтай."
        show us calml pioneer with dspr
        us "И не надо! Но играть будем по моим правилам!"
        me "Это по каким это?"
        us "Увидишь!"
        
    elif alt_pe == 6:#
        show sh normal pioneer at cright with dspr
        extend " Шурика."
        sh "Ну что, пусть победит сильнейший?"
        "Я молча пожал ему руку."

    elif alt_pe == 7:#
        show mz normal pioneer at cright with dspr
        extend " Женю."
        mz "Я твой противник."
        "Скрипнула она, присаживаясь напротив."
        "Я молча кивнул в ответ."
        
    
    if persistent.altCardsWon1 or persistent.altCardsFail:
        menu:
            "Играть самостоятельно.":
                jump alt_day2_participate
            "Победа в финале." if persistent.altCardsWon3:
                $ alt_day2_f1 = renpy.random.randint(1, 7)
                $ alt_day2_round3 = 2
                $ karma += 10
                jump alt_day2_final_win
            "Поражение в финале." if persistent.altCardsWon2:
                $ alt_day2_f1 = renpy.random.randint(1, 7)
                $ alt_day2_round3 = 1
                $ karma -= 10
                jump alt_day2_final_fail
            "Поражение в полуфинале.":
                call alt_day2_qf_analizer
                $ alt_day2_round2 = 1
                $ karma -= 10
                jump alt_day2_semifinal_fail
            "Поражение в первом же коне.":
                $ alt_day2_round1 = 1
                jump alt_day2_participate_fail


label alt_day2_participate:
    "Пока суд да дело, я решил разузнать, какая диспозиция сложилась на игровом поле."
    scene bg int_dining_hall_sunset
    show alt_tournament_bg
    with dissolve
    if alt_pe == 1:
        show un_playon:
            pos (1315,620)
        show me_playon:
            pos (1315,775)
        with diam
        "Мне противостояла Лена"
    elif alt_pe == 2:
        show sl_playon:
            pos (1315,620)
        show me_playon:
            pos (1315,775)
        with diam
        "Мне противостояла Славя"
    elif alt_pe == 3:
        show dv_playon:
            pos (1315,620)
        show me_playon:
            pos (1315,775)
        with diam
        "Алиса, улыбаясь, сидела напротив меня"
    elif alt_pe == 4:
        show mi_playon:
            pos (1315,620)
        show me_playon:
            pos (1315,775)
        with diam
        "По ту сторону стола мне лучезарно улыбалась японка"
    elif alt_pe == 5:
        show us_playon:
            pos (1315,620)
        show me_playon:
            pos (1315,775)
        with diam
        "Ульянка корчила мне рожи с той стороны стола"
    elif alt_pe == 6:
        show sh_playon:
            pos (1315,620)
        show me_playon:
            pos (1315,775)
        with diam
        "У нас здесь образовалась мужская компания"
    elif alt_pe == 7:
        show mz_playon:
            pos (1315,620)
        show me_playon:
            pos (1315,775)
        with diam
        "Из-за стёкол очков на меня зыркала нелюдимая библиотекарша"

    extend ", а вот за другими столами дела сложились куда интереснее."
    
    "Первый стол заняли"
    if alt_player1 == 1:
        show un_playon:
            pos (459,157)
        with dissolve
        extend " Лена"
    elif alt_player1 == 2:
        show sl_playon:
            pos (459,157)
        with dissolve
        extend " Славя"
    elif alt_player1 == 3:
        show dv_playon:
            pos (459,157)
        with dissolve
        extend " Алиса"
    elif alt_player1 == 4:
        show mi_playon:
            pos (459,157)
        with dissolve
        extend " Мику"
    elif alt_player1 == 5:
        show us_playon:
            pos (459,157)
        with dissolve
        extend " Ульяна"
    elif alt_player1 == 6:
        show sh_playon:
            pos (459,157)
        with dissolve
        extend " Шурик"
    elif alt_player1 == 7:
        show mz_playon:
            pos (459,157)
        with dissolve
        extend " Женя"
    
    if alt_player2 == 1:
        show un_playon:
            pos (459,312)
        with dissolve
        extend " и Лена."
        "Девочка перехватила мой взгляд и вся покраснела."
    elif alt_player2 == 2:
        show sl_playon:
            pos (459,312)
        with dissolve
        extend " и Славя."
        "Славя почувствовала, что я на неё смотрю, и улыбнулась."
    elif alt_player2 == 3:
        show dv_playon:
            pos (459,312)
        with dissolve
        extend " и рыжая."
        "Она расхохоталась, увидев, как я притворяюсь, что не смотрю на неё."
    elif alt_player2 == 4:
        show mi_playon:
            pos (459,312)
        with dissolve
        extend " и Мику."
        "Вид у японки был забавный — она изо всех сил притворялась, что знает, зачем здесь находится."
    elif alt_player2 == 5:
        show us_playon:
            pos (459,312)
        with dissolve
        extend " и Ульяна."
        "Мелкая показала мне язык и отвернулась."
    elif alt_player2 == 6:
        show sh_playon:
            pos (459,312)
        with dissolve
        extend " и Шурик."
        "Он подмигнул мне и выставил большой палец."
    elif alt_player2 == 7:
        show mz_playon:
            pos (459,312)
        with dissolve
        extend " и Жужелица."
        "Она, как обычно, проигнорировала меня."
    "С первым столом разобрались, кто-то из них сегодня не дойдёт до финала."
    
    "Следующий стол принадлежал "
    if alt_player3 == 1:
        show un_playon:
            pos (459,620)
        with dissolve
        extend " Лене"
    elif alt_player3 == 2:
        show sl_playon:
            pos (459,620)
        with dissolve
        extend " Славе"
    elif alt_player3 == 3:
        show dv_playon:
            pos (459,620)
        with dissolve
        extend " Алисе"
    elif alt_player3 == 4:
        show mi_playon:
            pos (459,620)
        with dissolve
        extend " Мику"
    elif alt_player3 == 5:
        show us_playon:
            pos (459,620)
        with dissolve
        extend " Ульянке"
    elif alt_player3 == 6:
        show sh_playon:
            pos (459,620)
        with dissolve
        extend " Шурику"
    elif alt_player3 == 7:
        show mz_playon:
            pos (459,620)
        with dissolve
        extend " Жене"

    if alt_player4 == 1:
        show un_playon:
            pos (459,775)
        with dissolve
        extend " и Лене."
        "Девочка притворилась, что не заметила, как я смотрю на неё."
    elif alt_player4 == 2:
        show sl_playon:
            pos (459,775)
        with dissolve
        extend " и Славе."
        "Славя ободряюще кивнула мне."
    elif alt_player4 == 3:
        show dv_playon:
            pos (459,775)
        with dissolve
        extend " и Алиске."
        "Надеюсь, она слетит в первом же раунде!"
    elif alt_player4 == 4:
        show mi_playon:
            pos (459,775)
        with dissolve
        extend " и Мику."
        "За эту переживать не приходится — она, похоже, вообще к картам равнодушна."
    elif alt_player4 == 5:
        show us_playon:
            pos (459,775)
        with dissolve
        extend " и Ульяне."
        "Мелкая была занята запугиванием оппонента."
    elif alt_player4 == 6:
        show sh_playon:
            pos (459,775)
        with dissolve
        extend " и Шурику."
        "Прикрыв глаза, кибернетик что-то высчитывал в уме. Шансы на победу?"
    elif alt_player4 == 7:
        show mz_playon:
            pos (459,775)
        with dissolve
        extend " и Жене."
        "Видно было, что она рада бы всё бросить и пойти в библиотеку."
    "И, наконец, последний стол."
    
    "За ним сидели"
    if alt_player5 == 1:
        show un_playon:
            pos (1315,157)
        with dissolve
        extend " Лена"
    elif alt_player5 == 2:
        show sl_playon:
            pos (1315,157)
        with dissolve
        extend " Славя"
    elif alt_player5 == 3:
        show dv_playon:
            pos (1315,157)
        with dissolve
        extend " Алиса"
    elif alt_player5 == 4:
        show mi_playon:
            pos (1315,157)
        with dissolve
        extend " Мику"
    elif alt_player5 == 5:
        show us_playon:
            pos (1315,157)
        with dissolve
        extend " Ульяна"
    elif alt_player5 == 6:
        show sh_playon:
            pos (1315,157)
        with dissolve
        extend " Шурик"
    elif alt_player5 == 7:
        show mz_playon:
            pos (1315,157)
        with dissolve
        extend " Женя"
    if alt_player6 == 1:
        show un_playon:
            pos (1315,312)
        with dissolve
        extend " и Лена."
        "Удивлён, что она согласилась участвовать в публичном мероприятии."
    elif alt_player6 == 2:
        show sl_playon:
            pos (1315,312)
        with dissolve
        extend " и Славя."
        "Странно было видеть «правильную» девочку с картами в зубах."
    elif alt_player6 == 3:
        show dv_playon:
            pos (1315,312)
        with dissolve
        extend " и Алиса."
        "Ну уж это-та своего не упустит."
    elif alt_player6 == 4:
        show mi_playon:
            pos (1315,312)
        with dissolve
        extend " и Мику."
        "Японка явно была чем-то взволнована. {w}И дело было совсем не в картах."
    elif alt_player6 == 5:
        show us_playon:
            pos (1315,312)
        with dissolve
        extend " и Ульяна."
        "Она улыбалась и качала головой, готовясь к решительной победе!"
    elif alt_player6 == 6:
        show sh_playon:
            pos (1315,312)
        with dissolve
        extend " и Шурик."
        "Парень, похоже, и в самом деле ни разу не слышал про такую игру — выглядел он растерянным."
    elif alt_player6 == 7:
        show mz_playon:
            pos (1315,312)
        with dissolve
        extend " и Женя."
        "Вот уж кто тут явно выглядит чужеродно."
    "Таким нехитрым образом удалось немного разобраться с тем, кто и против кого играет."
    "Что ж."
    "Пусть мне повезёт, а одна рыжая зазнайка утрётся!"
    "Я кивнул, сигналиризуя о готовности."
label alt_day2_tournament_start:
    if alt_day2_walk == 0:
        $ VISIBLE = True
        $ INVISIBLE = True
    else:
        $ VISIBLE = True
        $ INVISIBLE = False
    python:
        dialogs = {
                        (0, 'win','jump'):'alt_day2_participate_win',
                        (0, 'fail','jump'):'alt_day2_participate_fail',
                        (0, 'draw','jump'):'alt_day2_participate_draw'
                    }
        generate_cards('bg hall', dialogs)
        if alt_pe == 1:
            rival = CardGameRivalUn(un_avatar_set, u"Лена")
        elif alt_pe == 2:
            rival = CardGameRivalSl(sl_avatar_set, u"Славя")
        elif alt_pe == 3:
            rival = CardGameRivalDv(dv_avatar_set, u"Алиса")
        elif alt_pe == 4:
            rival = CardGameRivalMi(mi_avatar_set, u"Мику")
        elif alt_pe == 5:
            rival = CardGameRivalUs(us_avatar_set, u"Ульяна")
        elif alt_pe == 6:
            rival = CardGameRivalSh(sh_avatar_set, u"Шурик")
        elif alt_pe == 7:
            rival = CardGameRivalMz(mz_avatar_set, u"Женя")
    jump cards_gameloop

label alt_day2_participate_draw:
    $ show_cards()
    window show
    el "Ничья! Играйте ещё раз."
    window hide
    jump alt_day2_participate


label alt_day2_participate_fail:
    $ alt_day2_round1 = 1

    if alt_day2_revanche and (alt_pe == 1):
        "Ну вот, чего я и добивался."
        "Подмигнув Лене, я поднялся и раскланялся."
        me "Я проиграл. Простите."
        "И удалился — до ужина было ещё полчаса, а голова у меня уже серьёзно гудела от шума толпы."
        jump alt_day2_supper
    elif alt_day2_revanche and (alt_pe == 5):
        "Пожав плечами, я встал из-за стола, оставляя в одиночестве что-то восторженно вопящую Ульянку."
        "Переигровки, реванши… Я утратил интерес к игре."
        "Даже не стал досматривать события в полуфинале и финале."
        jump alt_day2_supper
    else:
        pass
    $ persistent.altCardsFail = True
    $ alt_day2_fail = 1
    scene bg int_dining_hall_day with dissolve
    window show
    if alt_pe == 1:
        $ lp_un += 1
        play music music_list["you_lost_me"]
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
    elif alt_pe == 2:
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
    elif alt_pe == 3:
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
    elif alt_pe == 4:
        show mi surprise pioneer with dspr
        mi "Ой!"
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
    elif alt_pe == 5:
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
    elif alt_pe == 6:
        show sh normal pioneer with dissolve
        sh "Это была достойная игра. Спасибо."
        "Он протянул мне руку, которую я с достоинством пожал."
        sh "А я пошёл дальше громить вражеские порядки."

    elif alt_pe == 7:
        show mz normal pioneer with dissolve
        "Женя пожала плечами и встала из-за стола."
        mz "Похоже, это будет ещё проще, чем мне казалось."

    #Анализ ситуации c поражением в первом раунде
    scene bg int_dining_hall_sunset
    "Ситуация, между тем, складывалась следующая:"
    show alt_tournament_bg with dissolve
    "Я остаюсь в первом коне."
    show me_playon:
        pos (1315,775)
    with diam
    "Мой оппонент направляется в полуфинал."
    if alt_pe == 1:
        show un_playon:
            pos (1315,620)
        $ renpy.pause(.3)
        hide un_playon
        show un_playon:
            pos (1135,698)
        with diam
        $ alt_day2_hf4 = 1
    elif alt_pe == 2:
        show sl_playon:
            pos (1315,620)
        $ renpy.pause(.3)
        hide sl_playon
        show sl_playon:
            pos (1135,698)
        with diam
        $ alt_day2_hf4 = 2
    elif alt_pe == 3:
        show dv_playon:
            pos (1315,620)
        $ renpy.pause(.3)
        hide dv_playon
        show dv_playon:
            pos (1135,698)
        with diam
        $ alt_day2_hf4 = 3
    elif alt_pe == 4:
        show mi_playon:
            pos (1315,620)
        $ renpy.pause(.3)
        hide mi_playon
        show mi_playon:
            pos (1135,698)
        with diam
        $ alt_day2_hf4 = 4
    elif alt_pe == 5:
        show us_playon:
            pos (1315,620)
        $ renpy.pause(.3)
        hide us_playon
        show us_playon:
            pos (1135,698)
        with diam
        $ alt_day2_hf4 = 5
    elif alt_pe == 6:
        show sh_playon:
            pos (1315,620)
        $ renpy.pause(.3)
        hide sh_playon
        show sh_playon:
            pos (1135,698)
        with diam
        $ alt_day2_hf4 = 6
    elif alt_pe == 7:
        show mz_playon:
            pos (1315,620)
        $ renpy.pause(.3)
        hide mz_playon
        show mz_playon:
            pos (1135,698)
        with diam
        $ alt_day2_hf4 = 7

    $ renpy.pause(.5)
    call alt_day2_qf_analizer
    stop ambience
    stop music fadeout 3
    window hide
    jump alt_day2_supper

label alt_day2_participate_win:
    $ persistent.altCardsWon1 = True
    scene bg int_dining_hall_sunset
    $ alt_day2_round1 = 2
    window show    
    call alt_day2_qf_analizer
    $ renpy.pause(1)
    scene bg int_dining_hall_sunset
    if alt_pe == 1:
        "У Лены не было ничего."
        "А с тем, что было, я бы постеснялся открывать карты."
        "Бедная девочка."
        "Она сидела, будто сама не способная поверить в то, что только что произошло."
        if lp_un >= 6 and not alt_day2_revanche:
            menu:
                "Матч-реванш":
                    $ karma += 5
                    $ alt_day2_revanche = True
                    if loki:
                        $ lp_un += 1
                        "Я дёрнул рукой, и карты посыпались на пол."
                        me "Эй, погодите!"
                        show el normal pioneer far at left
                        el "Что случилось?"
                        me "Да карты упали. Партия не засчитана, давай ещё одну."
                        el "Я же сказал — никаких переигровок!"
                        me "А это не переигровка, это… Это… Фальстарт!"
                        "Он неприязненно посмотрел на меня."
                        el "Ладно, давайте ещё раз!"
                        hide el with dissolve
                        window hide
                        jump alt_day2_tournament_start
                    else:
                        $ lp_un += 1
                        me "Неудачная партия."
                        un "Да…"
                        me "Может, ещё разок?"
                        show el normal pioneer far at left
                        el "Я же сказал — никаких переигровок!"
                        me "А это не переигровка, это… Это… Фальстарт!"
                        "Он неприязненно посмотрел на меня."
                        el "Ладно, давайте ещё раз!"
                        hide el
                        window hide
                        jump alt_day2_tournament_start
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
        "А я не мог сдержать ликования."
        th "Я подебил! То есть, я победил."
        dreamgirl "Ура! {w=.4} У девочки. {w=.4}В игру, которую ни ты, ни она не знаете. {w}Велико достижение."
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
        window show
        hide dv with dissolve
        scene bg int_dining_hall_day with dissolve
        "Ладно, это всё лирика."
    elif alt_pe == 2:
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
        if lp_sl >= 6:
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
                    jump alt_day2_semifinal
                "Ничего не делать":
                    pass
        else:
            pass
        "Я улыбнулся."
        me "Спасибо за игру!"
        sl "Тебе спасибо!"
        "Кивнув мне, она поднялась и отошла к Ольге Дмитриевне, и у них там завязалась оживлённая беседа."
        hide sl with dissolve
        "Что ж, это была трудная схватка, но я победил."
        th "Идеальное же противостояние, игра в которой вы оба ничего не понимаете."
        dreamgirl "Ну да, ну да."
        "Пробормотал внутренний голос."
        dreamgirl "Носкиллер рандомный."
        th "Помолчи. Ты ничего не понимаешь."
        th "Это вопрос индивидуального престижа. {w}Я буду двигаться в финале и раскатаю там рыжее хамло с нулевым счётом."
        dreamgirl "Надежды… Мечты… Фантазии…"
        th "Ты что, сомневаешься во мне?!"
        dreamgirl "Нет-нет-нет, ты что! {w}Я в тебя верю! Я знаю твой потенциал."
        th "Вот видишь!"
        dreamgirl "Ты слетишь на полпути."
        th "Да ну тебя!"
        if (alt_day2_hf1 == 3) or (alt_day2_hf2 == 3):
            "Может быть, это {i}она{/i} слетит на полпути!"
            "Вот возьмёт и проиграет."
            dreamgirl "Надежды… Мечты…"
            th "Ты повторяешься."
            dreamgirl "Просто ты слишком нос задираешь. {w}А настоящий мастер лишён гордыни."
        elif alt_day2_hf3 == 3:
            th "Между прочим, у нас сейчас как раз будет шанс стреножить её в полуфинале."
            dreamgirl "Ну да, это нам, конечно, повезло."
            dreamgirl "Но лучше приготовься к суровому испытанию — просто так она тебе победу не отдаст!"
        else:
            "Я усмехнулся."
            th "А даже если и слечу."
            th "Обращаю твоё внимание, что пока мы тут препирались, Двачевская изволила вылететь в самом первом раунде."
            "Я снял воображаемую шапку и прижал её к груди."
            me "Помянем!"
            "Двачевская оскалилась, но ничего не сказала."
        "Ладно, это всё лирика."
    elif alt_pe == 3:
        show dv sad pioneer2 with dspr
        "Алиска облажалась."
        "Ха. Ха. Ха."
        "Её вид — это то, что не купишь ни за какие мастеркарды с визами."
        "Поистине бесценное зрелище!"
        if lp_dv >= 6:
            menu:
                "Ну что, как я тебя?":
                    $ karma += 5
                    if loki or herc:
                        $ lp_dv += 1
                        show dv rage pioneer2 with dspr
                        "Алиса надулась, набычилась…"
                        me "Разделал как бог черепаху!"
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
                        "Я отшатнулся"
                        "Но постарался ответить солидно:"
                        me "Нет. {w}Свою натюрель ты уже поставила на кон."
                        dreamgirl "Дальше только честь девичья! {w}Ну-ка, скажешь это вслух?"
                        "Ага, сейчас. У меня и «натюрель»-то вышла дрожащим голосом."
                        "Алиса снова рассмеялась, увидев мою реакцию, и поднялась."
                        show dv smile pioneer2 with dspr
                        dv "Удачи тебе."
                        hide dv with dissolve
                        window hide
                        
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
                        
                "Партия.":
                    "Алиса кивнула и молча поднялась из-за стола."
                    pass
        else:
            pass
        "Кажется, свою малюсенькую проблему с пари я только что успешно решил."
        "Ладно, это всё лирика."
    elif alt_pe == 4:
        show mi upset pioneer with dspr
        mi "Ой!"
        "Она прижала руки ко рту."
        mi "Я что, я проиграла, да? А то я так и не поняла, что тут делать, только таскала у тебя карты, и не отдавала тебе свои."
        "Она покачала головой."
        mi "Какая-то непонятная игра."
        show mi smile pioneer with dspr
        mi "Но всё равно, спасибо, что играл со мной!"
        if lp_mi >= 6:
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
                    el "Мне есть дело!"
                    "Ответил появившийся из ниоткуда Электроник."
                    el "Ты победил, пожалте за полуфинальный столик!"
                    "Блин."
                    "Моя улыбка вышла извиняющейся."
                    me "Тогда увидимся."
                    "Мику кивнула и встала из-за стола."
                "Всегда рад.":
                    "Я улыбнулся."
                    me "Если вдруг захочешь ещё как-нибудь сыграть, обращайся!"
                    "Мику кивнула и встала из-за стола."
        else:
            pass
            $ lp_mi -= 1
        "Я улыбнулся."
        me "Всегда пожалуйста!"
        mi "Я пойду, ладно? Хочу увидеть, как ты будешь побеждать! Ты же будешь побеждать, правда? Я буду очень-очень за тебя болеть!"
        "Не в силах сдержать улыбку, я кивнул."
        me "Конечно же, буду."
        mi "Тогда удачи тебе дальше!"
        "Она ушла."
        hide mi with dissolve
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
        if (alt_day2_hf1 == 3) or (alt_day2_hf2 == 3):
            th "Помню, помню."
            "Но у этого пари все шансы разрешиться совершенно самостоятельно."
            dreamgirl "Надежды вьюношей питают…"
            th "Не науки разве?"
            dreamgirl "В твоём случае именно надежды."
            dreamgirl "Будь уверен, она доберётся до тебя и порвёт на мелкие клочки, а потом исполнит свою угрозу."
            th "О, спасибо тебе, мрачный зануда."
        elif alt_day2_hf3 == 3:
            th "Забудешь тут."
            "Судя по графику, моим противником в полуфинале выступает как раз Двачевская."
            dreamgirl "Вот свезло так свезло!"
            dreamgirl "Давай сделаем ей больно!"
        else:
            "Это было бы даже смешно."
            th "Пари? Какое пари?"
            th "Пока мы тут о везении судачили, Алиску вышибли на первом же кону."
            "Я снял воображаемую шапку и прижал её к груди."
            me "Помянем!"
            "Двачевская оскалилась, но ничего не сказала."
        "Ладно, это всё лирика."
    elif alt_pe == 5:
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
            jump alt_day2_semifinal
        else:
            show us sad pioneer with dspr
            us "Так нельзя, я только разыгрываться начала!"
            me "Я тоже. {w}Ты проиграла, я победил. Всё честно."
            us "Переиграем! Только ты теперь поддавайся, слышишь?"
            us "Я должна победить и забрать главный приз!"
            "Её крики привлекли внимание Электроника."
            el "Никаких переигровок!"
            el "Один матч, три раунда, проигравший выбывает."
            "Ульяна и бровью не повела."
            show us angry pioneer with dspr
            us "Ты должен проиграть! Должен! Понял! "
            "Ещё немного, и начну хохотать в голос, настолько потешно это выглядело."
            if alt_day2_us_escape:
                us " Ах так! Да я тогда… Я тогда завтра снова сбегу, понял!"
                us "И чисти тогда свою картошку сам! На весь лагерь!"
                "А вот эта угроза была уже посерьёзнее, дежурить по столовой одному мне совершенно не улыбалось."
            else:
                us "Ах так! Тогда я всем расскажу про тебя и Двачевскую!"
                if alt_day2_dv_bet_approve:
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
                        jump alt_day2_semifinal
                    "Ладно. Как хочешь.":
                        $ lp_us += 1
                        $ alt_day2_revanche = true
                        jump alt_day2_tournament_start
            elif not alt_day2_revanche:
                "Я вздохнул."
                me "Уговорила. Дам тебе ещё один шанс."
                $ alt_day2_revanche = true
                jump alt_day2_tournament_start
            else:
                me "Я крепко об этом пожалею, но…  Рассказывай."
                "Я поднялся из-за стола."
    elif alt_pe == 6:
        "Шурику не повезло."
        "Но, похоже, его больше интересовал сам процесс проверки новых правил и алгоритмов, чем победа."
        "Настоящий фанатик своего дела."
        show sh normal pioneer with dspr
        sh "Ты очень хорошо умеешь приспособиться к новым правилам игры."
        "Похвалил он."
        hide sh
        "И, пожав мне руку, удалился."
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
        if (alt_day2_hf1 == 3) or (alt_day2_hf2 == 3):
            dreamgirl "И особый воспитательный момент несёт то, что мы умоем её в игре по её же правилам!"
            th "Если она проиграет за вторым столом, то никого мы не умоем."
            dreamgirl "Есть подозрение, что такие, как она, так просто не сдаются."
            th "Ну, если встречу, я её обыграю."
            dreamgirl "С таким настроем ты никого не обыграешь. {w}Соберись!"
        elif alt_day2_hf3 == 3:
            th "Ага, прямо сейчас и покажем."
            dreamgirl "Здорово! Расправа оказалась куда ближе, чем мне казалось!"
            dreamgirl "Она просила сделать ей посопротивляться, исполни её просьбу."
        else:
            "Заниматься оценками слов, честно говоря, было уже поздновато."
            "Я посмотрел на таблицу участников — Алиса вылетела после первой же партии."
            th "Не{w=.3} по{w=.2}вез{w=.3}ло."
            th "Покойся с миром, дорогая бандитка."
            th "Я отомщу за тебя."
        "Ладно, это всё лирика."
    elif alt_pe == 7:
        "Библиотекарше не повезло."
        "Похоже, что там совсем грустно всё было в плане опыта игры в карты."
        "Ну и правильно, с кем руку-то набьёшь, если твой лучший друг — это даже не книга."
        "А подушка."
        "Буркнув нечто невразумительное, она поднялась и исчезла."
        "Ладно, это всё лирика."

    "Первый тур закончился."
    #Анализ ситуации c победой в первом коне (см корды спотов)
    "Ситуация, между тем, складывалась следующая:"
    show alt_tournament_bg with dissolve
    show me_playon:
        pos (1315,775)
    "Я направляюсь к победе."
    $ renpy.pause(1)
    show me_playon:
        pos (1135,698)
    with diam
    if alt_pe == 1:
        show un_playon:
            pos (1315,620)
        $ renpy.pause(1)
        hide un_playon with diam
    elif alt_pe == 2:
        show sl_playon:
            pos (1315,620)
        $ renpy.pause(1)
        hide sl_playon with diam
    elif alt_pe == 3:
        show dv_playon:
            pos (1315,620)
        $ renpy.pause(1)
        hide dv_playon with diam
    elif alt_pe == 4:
        show mi_playon:
            pos (1315,620)
        $ renpy.pause(1)
        hide mi_playon with diam
    elif alt_pe == 5:
        show us_playon:
            pos (1315,620)
        $ renpy.pause(1)
        hide us_playon with diam
    elif alt_pe == 6:
        show sh_playon:
            pos (1315,620)
        $ renpy.pause(1)
        hide sh_playon with diam
    elif alt_pe == 7:
        show mz_playon:
            pos (1315,620)
        $ renpy.pause(1)
        hide mz_playon with diam
        
    "А мой соперник отправляется в ад!"
    "То есть, остаётся в первом коне."

    
label alt_day2_semifinal:
    "За стол полуфиналиста посадили моего оппонента."
    scene bg int_dining_hall_sunset
    if alt_day2_hf2 == 1:
        "Им оказалась Лена."
        show un shy pioneer with dspr
        me "Ну что, удачи нам обоим?"
        show un smile pioneer with dspr
        $ renpy.pause(.3)
        show un shy pioneer with dspr
        un "Д-да…"
        "Она попыталась улыбнуться, но тут же снова смешалась и смолкла."
    if alt_day2_hf2 == 2:
        "Славю."
        show sl smile pioneer with dspr
        sl "Ух! Не думала, что так далеко зайду!"
        "Улыбнулась она."
        me "Это не значит, что я теперь буду тебе поддаваться!"
        show sl laugh pioneer with dspr
        sl "И не надо!"
        "Рассмеялась девочка."
        sl "Пускай победит сильнейший!"
    if alt_day2_hf2 == 3:
        "Алиса? Надо же, какая встреча."
        show dv grin pioneer2 with dspr
        dv "Я придумала новое правило."
        "Прошептала она, наклонившись ко мне."
        me "Какое ещё правило?"
        dv "Если ты меня победишь сейчас, но не победишь в финале — я всё равно всё всем расскажу."
        me "Эй, так нечестно!"
        show dv laugh pioneer2 with dspr
        dv "Хотя ты не победишь."
        "Рассмеялась девочка."
        dv "Тебе конец!"
    if alt_day2_hf2 == 4:
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
    if alt_day2_hf2 == 5:
        "Напротив меня уселась Ульянка."
        show us grin pioneer with dspr
        window show
        play music music_list["i_want_to_play"] fadein 1
        us "Будешь поддаваться, будешь? "
        "С улыбкой до ушей она уставилась на меня."
        us "Я хочу всех победить!"
        me "Не буду."
        "Я отрицательно покачал головой."
        if alt_day2_dv_bet_approve:
            me "У нас же спор, помнишь? Ты разбивала!"
            show us sad pioneer with dspr
            us "Спор — это да."
            us "Но играть будем по моим правилам!"
            me "Что бы это значило?!"
            show us laugh pioneer with dspr
        us "Просто я ничего не поняла и не запомнила."
        
    if alt_day2_hf2 == 6:
        "Александр Трофимов. {w}Больше известный как Шурик за схожесть с одним киногероем."
        show sh normal pioneer with dspr
        sh "Это будет достойная схватка."
        "Кивнул он."
        me "Не думай, что я буду тебе поддаваться."
        show sh smile pioneer with dspr
        sh "И ты тоже не надейся!"
        me "Тогда к оружию!"
    if alt_day2_hf2 == 7:
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


    el "Итак!"
    "Подал голос Электроник, явно гордящийся своей ролью мастер-церемонимейстера."
    el "Первый тур окончен, победители встречаются во втором туре!"
    if alt_pe == 1:
        "Лена, оказывается, никуда не ушла, она просто стояла скромно и явно собиралась следить за событиями до самого финала."
        show un smile2 pioneer far at left
        "При этом на лице её не было ни злости, ни обиды, ни чего-либо в этом духе."
        "Напротив, в её глазах горел… Азарт!"
        "При этом — азарт болельщика."
        hide un with dissolve
        "Что ж, убедившись в том, что не обидел её, я немного расслабился."
    "Между тем, в таблице уже появились имена участников второго тура."
    "И если верить этой таблице, то в полуфинале встречаются четыре игрока."
    "За первым столом полуфиналистов встречаются:"
    if alt_day2_hf1 == 1:
        extend " Лена"
    if alt_day2_hf1 == 2:
        extend " Славя"
    if alt_day2_hf1 == 3:
        extend " Алиса"
    if alt_day2_hf1 == 4:
        extend " Мику"
    if alt_day2_hf1 == 5:
        extend " Ульяна"
    if alt_day2_hf1 == 6:
        extend " Шурик"
    if alt_day2_hf1 == 7:
        extend " Женя"
    if alt_day2_hf3 == 1:
        extend " и Лена."
    if alt_day2_hf3 == 2:
        extend " и Славя."
    if alt_day2_hf3 == 3:
        extend " и Алиса."
    if alt_day2_hf3 == 4:
        extend " и Мику."
    if alt_day2_hf3 == 5:
        extend " и Ульяна."
    if alt_day2_hf3 == 6:
        extend " и Шурик."
    if alt_day2_hf3 == 7:
        extend " и Женя."
    "Когда второй столик прочно оккупировали ваш покорный слуга"
    if alt_day2_hf2 == 1:
        extend " и Лена."
    if alt_day2_hf2 == 2:
        extend " и Славя."
    if alt_day2_hf2 == 3:
        extend " и Алиса."
    if alt_day2_hf2 == 4:
        extend " и Мику."
    if alt_day2_hf2 == 5:
        extend " и Ульяна."
    if alt_day2_hf2 == 6:
        extend " и Шурик."
    if alt_day2_hf2 == 7:
        extend " и Женя."
    window hide
label alt_day2_semifinal_start:
    if alt_day2_walk == 0:
        $ VISIBLE = True
        $ INVISIBLE = True
    else:
        $ VISIBLE = True
        $ INVISIBLE = False
    python:
        dialogs = {
                        (0, 'win','jump'):'alt_day2_semifinal_win',
                        (0, 'fail','jump'):'alt_day2_semifinal_fail',
                        (0, 'draw','jump'):'alt_day2_semifinal_draw'
                    }
        generate_cards('bg hall', dialogs)
        if alt_day2_hf2 == 1:
            rival = CardGameRivalUn(un_avatar_set, u"Лена")
        elif alt_day2_hf2 == 2:
            rival = CardGameRivalSl(sl_avatar_set, u"Славя")
        elif alt_day2_hf2 == 3:
            rival = CardGameRivalDv(dv_avatar_set, u"Алиса")
        elif alt_day2_hf2 == 4:
            rival = CardGameRivalMi(mi_avatar_set, u"Мику")
        elif alt_day2_hf2 == 5:
            rival = CardGameRivalUs(us_avatar_set, u"Ульяна")
        elif alt_day2_hf2 == 6:
            rival = CardGameRivalSh(sh_avatar_set, u"Шурик")
        elif alt_day2_hf2 == 7:
            rival = CardGameRivalMz(mz_avatar_set, u"Женя")
    jump cards_gameloop

label alt_day2_semifinal_fail:
    scene bg int_dining_hall_sunset
    $ persistent.altCardsWon1 = True
    $ alt_day2_round2 = 1
    if alt_day2_hf2 == 1:
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
    elif alt_day2_hf2 == 2:
        scene bg int_dining_hall_sunset
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
    elif alt_day2_hf2 == 3:
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
    elif alt_day2_hf2 == 4:
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

    elif alt_day2_hf2 == 5:
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

    elif alt_day2_hf2 == 6:
        show sh normal pioneer with dissolve
        sh "Жаль, что так быстро всё закончилось."
        "С достоинством кивнул Шурик."
        sh "Идеально, если бы нам дали партий десять с одной колоды, чтобы можно было вычислить логику."
        me "И сидеть до утра?"
        me "Я-то не против, да кто ж нам позволит."
        "Я кивнул и поднялся из-за стола."
    elif alt_day2_hf2 == 7:
        show mz normal pioneer with dissolve
        mz "Упс."
        "Пробормотала она себе под нос."
        mz "Специально же карты не открывала. Здесь вообще как-нибудь проиграть возможно?"
        me "Как видишь."
        "Сказал я и встал из-за стола."

    #Анализ ситуации c поражением в полуфинале
    scene bg int_dining_hall_sunset
    "В полуфинале был такой расклад:"
    show alt_tournament_bg with dissolve
    "Я выбыл в полуфинале."
    show me_playon:
        pos (890,360)
    with diam
    "А мой оппонент отправился дальше."
    if alt_day2_hf2 == 1:
        show un_playon:
            pos (1135,235)
        $ renpy.pause(.3)
        hide un_playon
        show un_playon:
            pos (890,360)
        with diam
        $ alt_day2_f2 = 1
    elif alt_day2_hf2 == 2:
        show sl_playon:
            pos (1135,235)
        $ renpy.pause(.3)
        hide sl_playon
        show sl_playon:
            pos (890,360)
        with diam
        $ alt_day2_f2 = 2
    elif alt_day2_hf2 == 3:
        show dv_playon:
            pos (1135,235)
        $ renpy.pause(.3)
        hide dv_playon
        show dv_playon:
            pos (890,360)
        with diam
        $ alt_day2_f2 = 3
    elif alt_day2_hf2 == 4:
        show mi_playon:
            pos (1135,235)
        $ renpy.pause(.3)
        hide mi_playon
        show mi_playon:
            pos (890,360)
        with diam
        $ alt_day2_f2 = 4
    elif alt_day2_hf2 == 5:
        show us_playon:
            pos (1135,235)
        $ renpy.pause(.3)
        hide us_playon
        show us_playon:
            pos (890,360)
        with diam
        $ alt_day2_f2 = 5
    elif alt_day2_hf2 == 6:
        show sh_playon:
            pos (1135,235)
        $ renpy.pause(.3)
        hide sh_playon
        show sh_playon:
            pos (890,360)
        with diam
        $ alt_day2_f2 = 6
    elif alt_day2_hf2 == 7:
        show mz_playon:
            pos (1135,235)
        $ renpy.pause(.3)
        hide mz_playon
        show mz_playon:
            pos (890,360)
        with diam
        $ alt_day2_f2 = 7

    $ renpy.pause(.5)
    call alt_day2_hf_analizer
    stop ambience
    stop music fadeout 3
    window hide
    jump alt_day2_supper

label alt_day2_semifinal_draw:
    $ show_cards()
    window show
    el "Ничья! Играйте ещё раз."
    window hide
    jump alt_day2_semifinal_start

label alt_day2_semifinal_win:
    $ alt_day2_round2 = 2
    $ persistent.altCardsWon2 = True
    scene bg int_dining_hall_sunset
    if alt_day2_hf2 == 1:
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
        "А пока мне готовили жертву, я окинул взглядом изменившийся баланс сил."
    elif alt_day2_hf2 == 2:
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
    elif alt_day2_hf2 == 3:
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
    elif alt_day2_hf2 == 4:
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
    elif alt_day2_hf2 == 5:
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
    elif alt_day2_hf2 == 6:
        show sh normal pioneer with dspr
        "Шурик кивнул мне и поднялся."
        "Не знаю, впечатлил его мой навык игры, в которую я играю второй раз в жизни (первый раз — в четвертьфинале) или нет."
        "Так или иначе, он достаточно равнодушно отнёсся к поражению."
        show sh smile pioneer with dspr
        sh "Насчёт клуба кибернетиков, если вдруг что…"
        "Я кивнул."
        "По слухам, им вечно не хватало новых членов."
        "Но давайте насчёт кибернетики позже, а пока посмотрим, что там у других пионеров творится."
    elif alt_day2_hf2 == 7:
        show mz normal pioneer with dspr
        "Реакция Жужи меня позабавила."
        "Сначала она бросила карты на стол и спрятала лицо в ладонях."
        "А затем вскинула руки вверх и рявкнула:"
        mz "Аллилуйя!"
        "После чего телепортировалась из столовой."
        "А я же решил узнать, как там дела у соседей."
    $ renpy.pause(.5)
    call alt_day2_hf_analizer
    stop ambience
    stop music fadeout 3
    window hide

label alt_day2_final_start:
    #Финал 1 против 3 — 960,430
    #Финал 2 против 4 — 960,643
    #Победитель 1121,530
    if alt_day2_f1 == 3:
        if alt_day2_walk == 0:
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
            window hide
            $ INVISIBLE = False
    else:
        if alt_day2_walk == 0:
            $ VISIBLE = True
            $ INVISIBLE = True
        else:
            $ VISIBLE = True
            $ INVISIBLE = False
    python:
        dialogs = {
                        (0, 'win','jump'):'alt_day2_final_win',
                        (0, 'fail','jump'):'alt_day2_final_fail',
                        (0, 'draw','jump'):'alt_day2_final_draw'
                    }
        generate_cards('bg hall', dialogs)
        if alt_day2_f1 == 1:
            rival = CardGameRivalUn(un_avatar_set, u"Лена")
        elif alt_day2_f1 == 2:
            rival = CardGameRivalSl(sl_avatar_set, u"Славя")
        elif alt_day2_f1 == 3:
            rival = CardGameRivalDv(dv_avatar_set, u"Алиса")
        elif alt_day2_f1 == 4:
            rival = CardGameRivalMi(mi_avatar_set, u"Мику")
        elif alt_day2_f1 == 5:
            rival = CardGameRivalUs(us_avatar_set, u"Ульяна")
        elif alt_day2_f1 == 6:
            rival = CardGameRivalSh(sh_avatar_set, u"Шурик")
        elif alt_day2_f1 == 7:
            rival = CardGameRivalMz(mz_avatar_set, u"Женя")
    jump cards_gameloop

label alt_day2_final_fail:
    window hide
    $ persistent.altCardsWon2 = True
    $ alt_day2_round3 = 1
    scene bg int_dining_hall_sunset
    show alt_tournament_bg
    show me_playon:
        pos (890,575)
    if alt_day2_f1 == 1:
        show un_playon:
            pos (890,360)
        $ renpy.pause (.3)
        show un_playon:
            pos (1051,460)
        hide me_playon
        with diam
    if alt_day2_f1 == 2:
        show sl_playon:
            pos (890,360)
        $ renpy.pause (.3)
        show sl_playon:
            pos (1051,460)
        hide me_playon
        with diam
    if alt_day2_f1 == 3:
        show dv_playon:
            pos (890,360)
        $ renpy.pause (.3)
        show dv_playon:
            pos (1051,460)
        hide me_playon
        with diam
    if alt_day2_f1 == 4:
        show mi_playon:
            pos (890,360)
        $ renpy.pause (.3)
        show mi_playon:
            pos (1051,460)
        hide me_playon
        with diam
    if alt_day2_f1 == 5:
        show us_playon:
            pos (890,360)
        $ renpy.pause (.3)
        show us_playon:
            pos (1051,460)
        hide me_playon
        with diam
    if alt_day2_f1 == 6:
        show sh_playon:
            pos (890,360)
        $ renpy.pause (.3)
        show sh_playon:
            pos (1051,460)
        hide me_playon
        with diam
    if alt_day2_f1 == 7:
        show mz_playon:
            pos (890,360)
        $ renpy.pause (.3)
        show mz_playon:
            pos (1051,460)
        hide me_playon
        with diam
    window show
    scene bg int_dining_hall_sunset
    "Похоже, у меня не было ни шанса."
    if alt_day2_f1 == 1:
        play music take_my_hand fadein 3
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
        window hide
    elif alt_day2_f1 == 2:
        $ lp_sl -= 1
        $ karma += 10
        "Славя застонала и уронила голову на сложенные руки."
        play music music_list["forest_maiden"] fadein 5
        sl "Вы хотя бы пытались?"
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
        window hide
    elif alt_day2_f1 == 3:
        scene bg int_dining_hall_day with dissolve
        play music music_list["you_lost_me"]
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
            if (alt_day2_walk == 0) and (alt_day2_fail != 1):
                th "Несмотря даже на то, что я пометил карты."
            "Появилось это противное чувство, что сейчас на меня начнут показывать пальцем и шептаться «Смотрите, это он! Да, он! Он облажался.»"
            "Я двинулся прочь от стола, не поднимая ни на кого глаз."
            "Особенно — на Алису."
            "Её взгляд буквально жёг мне спину."
        if alt_day2_dv_bet_approve:
            th "Я проиграл пари."
            if loki:
                "Теперь ждём завтрашнего дня и наслаждаемся бесплатной рекламой?"
            else:
                "Теперь мне… {w}Крышка? Кранты? Конец?"
                th "Может, сбежать из лагеря, пока не поздно?"
        elif alt_day2_dv_harass:
            "И теперь, если она расскажет всем, что я её лапал — это же правдой будет, да?"
            "Как говорил мой батя в трудных ситуациях — не упс, а йопс."
        else:
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
        window hide
        jump alt_day2_supper
    elif alt_day2_f1 == 4:
        play music ourfirstmet fadein 3
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
        play music tender_song fadein 3
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
        "Так что ещё минут пять — и обе ловчих свалились рядом со столами, а она всё продолжала и продолжала петь, делая в воздухе странные, стригущие движение пальцами."
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
        
    elif alt_day2_f1 == 5:
        $ lp_us += 1
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
        "А в самом центре таблицы огромными красными буквами значилось имя."
        el "Победитель — Ульяна!"
        "Все стали кричать «поздравляем, поздравляем»!"
        "Но Ульяна отмахнулась. {w}Её интересовало другое:"
        us "А где призы?"
    elif alt_day2_f1 == 6:
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
    elif alt_day2_f1 == 7:
        show mz normal pioneer with dspr
        "Жужелица встала."
        "Окинула всех диковатым взглядом."
        mz "Всё, что ли? Больше жертв не будет?"
        play sound highfive
        $ renpy.pause (3)
        play sound highfive
        $ renpy.pause (3)
        "В полной тишине спросила она."
        play sound highfive
        $ renpy.pause (3)
        play sound highfive
        show el smile pioneer at left with dissolve
        "Только Электроник продолжал хлопать."
        mz "Ну ладно. Я пойду тогда."
        el "Ура, да здравствует победитель!"
        play sound highfive
        "Закричал Сыроежкин ей вслед."
        "По-моему, это всё-таки любовь."
        sh "Эл, всё, она ушла. Упокойся."
    jump alt_day2_supper    
    
label alt_day2_final_draw:
    $ show_cards()
    window show
    el "Ничья! Играйте ещё раз."
    window hide
    jump alt_day2_final_start

label alt_day2_final_win:
    $ lp_dv += 1
    window hide
    $ persistent.altCardsWon3 = True
    $ alt_day2_round3 = 2
    $ alt_day2_dv_bet_won = 1
    scene bg int_dining_hall_sunset
    show alt_tournament_bg
    show me_playon:
        pos (890,575)
    if alt_day2_f1 == 1:
        show un_playon:
            pos (890,360)
    if alt_day2_f1 == 2:
        show sl_playon:
            pos (890,360)
    if alt_day2_f1 == 3:
        show dv_playon:
            pos (890,360)
    if alt_day2_f1 == 4:
        show mi_playon:
            pos (890,360)
    if alt_day2_f1 == 5:
        show us_playon:
            pos (890,360)
    if alt_day2_f1 == 6:
        show sh_playon:
            pos (890,360)
    if alt_day2_f1 == 7:
        show mz_playon:
            pos (890,360)
    $ renpy.pause(1)
    show me_playon:
        pos (1051,460)
    with diam
    window show
    scene bg int_dining_hall_sunset
    if alt_day2_f1 == 1:
        play music take_my_hand fadein 3
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
        "Моё!"
        if alt_day2_dv_bet_approve:
            th "И пусть только рыжая стерлядь попробует что-нибудь там вякнуть."
        show dv smile pioneer2 with dissolve
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
    elif alt_day2_f1 == 2:
        $ lp_sl += 1
        play music Please_Reprise fadein 3
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
        "И тянет к небу поднятой рукой"
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
        dv "Ты победил в споре и турнире."
        "Она ткнула меня кулаком в плечо и, развернувшись, растворилась в толпе."
        window hide
    elif alt_day2_f1 == 3:
        $ lp_dv += 1
        play music sheiscool fadein 3
        th "Я выиграл!"
        th "Выиграл?"
        th "Выиграл!!!"
        show dv normal pioneer2 with dspr
        "Ещё несколько часов назад я не мог и представить себя таким счастливым!"
        "Я победно смотрел на Алису, ещё не веря до конца в свою удачу…"
        "А вокруг уже все поздравляли меня с победой, и Электроник писал моё имя в своей таблице!"
        th "Моё имя!!!"
        th "Я выиграл турнир!"
        window hide
        scene bg int_dining_hall_day with dissolve
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
    elif alt_day2_f1 == 4:
        $ lp_mi += 2
        $ alt_day2_mi_snap = True
        play music tellyourworld fadein 3
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
        if alt_day2_phys_done:
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
        "Старый добрый «компакт-автомат», пленочный."
        "Я чуть было не сказал «раритет», но видно было, что машинка рабочая."
        ba "Только без вспышки сегодня, так что становитесь как-нибудь, где посветлее."
        "Мику улыбнулась и развернула кипучую деятельность, тормоша всех и переставляя."
        "В результате, полотнище таблицы было снято и перенесено поближе к окошку, где Шурик и Электроник держали его на растяг."
        scene bg int_dining_hall_sunset
        show alt_tournament_bg
        with dissolve
        "Мику встала рядом."
        show mi normal pioneer at cleft with dissolve
        "Ещё ближе."
        "Ещё чуточку."
        mi "Сень!"
        "Наконец, не выдержала она."
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
        play sound snap
        scene expression Sepia("cg d2_mi_me_polaroid_7dl")
        show PolariodFrame
        with flash
        $ renpy.pause(3)
        me "Сыыыр."
        "Запоздало опомнился я."
        mi "Хи-хи-хи."
        mi "Сенечка, ты чудо."
        "Она рассмеялась и убежала."
        window hide
        scene bg int_dining_hall_sunset with dissolve
    elif alt_day2_f1 == 5:
        $ lp_us -= 1
        th "Я выиграл!"
        th "Выиграл?"
        th "Выиграл!!!"
        "Бац!" with vpunch
        with flash_red
        play music genki fadein 3
        show us calml pioneer with dspr
        us "И ничего ты не выиграл!"
        "Она хмуро смотрела на меня снизу вверх."
        us "Ты играл неправильно, переигрываем!"
        me "Что это значит, «неправильно»?"
        show us dontlike pioneer with dissolve
        me "Я выиграл турнир! {w}Как я могу играть неправильно?"
        us "Молча! Ты жульничал!"
        "Она топнула ногой."
        us "Ты неправильно играл и жульничал!"
        if alt_day2_walk == 0:
            th "Неужели про крап узнала? Но как?"
            th "Если она сейчас всем про него раcскажет, меня линчуют на ближайшей осине."
        us "Ты плохо мне поддавался."
        "А. Ну, это меняло всё дело."
        "Я расхохотался и отошёл."
        "А Алиса наконец поднялась со своего места и, проходя мимо меня, хлопнула по плечу."
        dv "Поздравляю!"
        "И от этих слов мне стало так радостно!"
        th "Я победил!!!"
        window hide
        hide dv with dissolve
    elif alt_day2_f1 == 6:
        play music dead_silence fadein 3
        show sh rage pioneer with dspr
        sh "Значит, победил?"
        "Медленно произнёс он."
        "Он так странно стоял, что никак не мог разглядеть его глаз из-за бликов на очках."
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
        play ambience ambience_dining_hall_full fadein 5
        show blinking
        scene bg int_dining_hall_sunset
        with diam
        "Наваждение момента исчезло, Шурик из зловещей фигуры превратился обратно в обычного, чуть рассеянного, парня."
        "Серые, давящие стены уступили место красноватому свету катящегося на закат светила."
        "И самое главное — "
        "Ведь я же победитель!"
        "Электроник внёс моё имя в список победителей."
        el "А после ужина…"
        "Ольга Дмитриевна заткнула ему рот рукой."
        th "Правильно, пусть будет сюрпризом. А для спойлерщиков в аду отдельный котёл стоит."
        window hide
        hide dv with dissolve
    elif alt_day2_f1 == 7:
        "Реакция Жужелицы была обескураживающей."
        "Её не было."
        "Но меня это не смущало."
        "Самое главное, что я победил!"
        "Остальные пусть думают и делают что хотят."
        "Даже Алиса."
        "Сейчас-то ей никто не поверит."
        "И это, пожалуй, радует больше всего."
        window hide
    jump alt_day2_supper

label alt_day2_qf_analizer:
    scene bg int_dining_hall_sunset
    show alt_tournament_bg
    with dissolve
    "Что же касается других столов…"
    "Там всё тоже достаточно любопытно."
    
    "За первым столом победа ушла"
    $ alt_dd1 = renpy.random.choice([10, 1])
    if alt_dd1 == 10:
        $ alt_day2_hf1 = alt_player1
    else:
        $ alt_day2_hf1 = alt_player2
        
    if alt_day2_hf1 == 1:
        extend " Лене."
        if alt_day2_hf1 == alt_player1:
            show un_playon:
                pos (459,157)
        else:
            show un_playon:
                pos (459,312)
    elif alt_day2_hf1 == 2:
        extend " Славе."
        if alt_day2_hf1 == alt_player1:
            show sl_playon:
                pos (459,157)
        else:
            show sl_playon:
                pos (459,312)
    elif alt_day2_hf1 == 3:
        extend " Алисе."
        if alt_day2_hf1 == alt_player1:
            show dv_playon:
                pos (459,157)
        else:
            show dv_playon:
                pos (459,312)
    elif alt_day2_hf1 == 4:
        extend " Мику."
        if alt_day2_hf1 == alt_player1:
            show mi_playon:
                pos (459,157)
        else:
            show mi_playon:
                pos (459,312)
    elif alt_day2_hf1 == 5:
        extend " Ульяне."
        if alt_day2_hf1 == alt_player1:
            show us_playon:
                pos (459,157)
        else:
            show us_playon:
                pos (459,312)
    elif alt_day2_hf1 == 6:
        extend " Шурику."
        if alt_day2_hf1 == alt_player1:
            show sh_playon:
                pos (459,157)
        else:
            show sh_playon:
                pos (459,312)
    elif alt_day2_hf1 == 7:
        extend " Жене."
        if alt_day2_hf1 == alt_player1:
            show mz_playon:
                pos (459,157)
        else:
            show mz_playon:
                pos (459,312)
    $ renpy.pause(.3)
    if alt_day2_hf1 == 1:
        show un_playon:
            pos (648,235)
        with diam
        "Ей пришлось потрудиться, но победа оказалась за ней."
    elif alt_day2_hf1 == 2:
        show sl_playon:
            pos (648,235)
        with diam
        "Активистка, похоже, не поняла, что произошло, но покорно пересела за стол полуфиналистов."
    elif alt_day2_hf1 == 3:
        show dv_playon:
            pos (648,235)
        with diam
        "Она раскатала противника с разгромным счётом — кажется, наслаждалась игрой."
    elif alt_day2_hf1 == 4:
        show mi_playon:
            pos (648,235)
        with diam
        "Да уж, талантливый человек талантлив во всём."
    elif alt_day2_hf1 == 5:
        show us_playon:
            pos (648,235)
        with diam
        "Мелкая и не думала учить правила игры."
        "Вместо этого она явно прибегла к какому-то жульничеству."
    elif alt_day2_hf1 == 6:
        show sh_playon:
            pos (648,235)
        with diam
        "Честно сказать, не удивлён. У него были все шансы."
    elif alt_day2_hf1 == 7:
        show mz_playon:
            pos (648,235)
        with diam
        "Она с неудовольствием скривилась, кажется, поняла, что победа значит ещё и дальнейшее участие в этой дурацкой игре."
    
    "Проигравшая сторона постаралась отреагировать с достоинством."
    if ((alt_player1 == 1) or (alt_player2 == 1)) and (alt_day2_hf1 != 1):
        if alt_player1 == 1:
            show un_playon:
                pos (459,157)
        else:
            show un_playon:
                pos (459,312)
        with dissolve
        "Лена тихо поднялась и присоединилась к болельщикам."
        hide un_playon with diam
    elif ((alt_player1 == 2) or (alt_player2 == 2)) and (alt_day2_hf1 != 2):
        if alt_player1 == 3:
            show sl_playon:
                pos (459,157)
        else:
            show sl_playon:
                pos (459,312)
        with dissolve
        "Славя пожала плечами и поднялась — кажется, она куда-то торопилась."
        hide sl_playon with diam
    elif ((alt_player1 == 3) or (alt_player2 == 3)) and (alt_day2_hf1 != 3):
        if alt_player1 == 3:
            show dv_playon:
                pos (459,157)
        else:
            show dv_playon:
                pos (459,312)
        with dissolve
        "Увидеть лицо Двачевской, терпящей поражение — бесценно!"
        "Я расхохотался, прикрываясь рукой, но она, похоже, услышала — обожгла взглядом."
        hide dv_playon with diam
    elif ((alt_player1 == 4) or (alt_player2 == 4)) and (alt_day2_hf1 != 4):
        if alt_player1 == 4:
            show mi_playon:
                pos (459,157)
        else:
            show mi_playon:
                pos (459,312)
        with dissolve
        "Мику поднялась, помахала всем и встала к болельщикам."
        "Она была чем-то очень довольная."
        hide mi_playon with diam
    elif ((alt_player1 == 5) or (alt_player2 == 5)) and (alt_day2_hf1 != 5):
        if alt_player1 == 5:
            show us_playon:
                pos (459,157)
        else:
            show us_playon:
                pos (459,312)
        with dissolve
        "Ульяна надулась, закричала что-то и пробовала было топать ногами, но Ольга Дмитриевна быстро успокоила её."
        "Понурившись, мелкая побрела прочь из столовой."
        hide us_playon with diam
    elif ((alt_player1 == 6) or (alt_player2 == 6)) and (alt_day2_hf1 != 6):
        if alt_player1 == 6:
            show sh_playon:
                pos (459,157)
        else:
            show sh_playon:
                pos (459,312)
        with dissolve
        "Шурик среагировал так, как я и ожидал — поправил очки, резким движением отбросил чёлку со лба и встал."
        "Коротко наклонил голову и занял своё место в толпе."
        hide sh_playon with diam
    elif ((alt_player1 == 7) or (alt_player2 == 7)) and (alt_day2_hf1 != 7):
        if alt_player1 == 7:
            show mz_playon:
                pos (459,157)
        else:
            show mz_playon:
                pos (459,312)
        with dissolve
        "С видом величайшего облегчения Женя бросила карты на стол и, встав, направилась на улицу."
        hide mz_playon with diam
        
    
    "Второй стол принёс удачу"
    $ alt_dd2 = renpy.random.choice([10, 1])
    if alt_dd2 == 10:
        $ alt_day2_hf2 = alt_player3
    else:
        $ alt_day2_hf2 = alt_player4
        
    if alt_day2_hf2 == 1:
        extend " Лене."
        if alt_day2_hf2 == alt_player3:
            show un_playon:
                pos (459,620)
        else:
            show un_playon:
                pos (459,775)
    elif alt_day2_hf2 == 2:
        extend " Славе."
        if alt_day2_hf2 == alt_player3:
            show sl_playon:
                pos (459,620)
        else:
            show sl_playon:
                pos (459,775)
    elif alt_day2_hf2 == 3:
        extend " Алисе."
        if alt_day2_hf2 == alt_player3:
            show dv_playon:
                pos (459,620)
        else:
            show dv_playon:
                pos (459,775)
    elif alt_day2_hf2 == 4:
        extend " Мику."
        if alt_day2_hf2 == alt_player3:
            show mi_playon:
                pos (459,620)
        else:
            show mi_playon:
                pos (459,775)
    elif alt_day2_hf2 == 5:
        extend " Ульяне."
        if alt_day2_hf2 == alt_player3:
            show us_playon:
                pos (459,620)
        else:
            show us_playon:
                pos (459,775)
    elif alt_day2_hf2 == 6:
        extend " Шурику."
        if alt_day2_hf2 == alt_player3:
            show sh_playon:
                pos (459,620)
        else:
            show sh_playon:
                pos (459,775)
    elif alt_day2_hf2 == 7:
        extend " Жене."
        if alt_day2_hf2 == alt_player3:
            show mz_playon:
                pos (459,620)
        else:
            show mz_playon:
                pos (459,775)
    $ renpy.pause(.3)
    if alt_day2_hf2 == 1:
        show un_playon:
            pos (648,698)
        with diam
        "Ей пришлось потрудиться, но победа оказалась за ней."
    elif alt_day2_hf2 == 2:
        show sl_playon:
            pos (648,698)
        with diam
        "Активистка, похоже, не поняла, что произошло, но покорно пересела за стол полуфиналистов."
    elif alt_day2_hf2 == 3:
        show dv_playon:
            pos (648,698)
        with diam
        "Она раскатала противника с разгромным счётом — кажется, наслаждалась игрой."
    elif alt_day2_hf2 == 4:
        show mi_playon:
            pos (648,698)
        with diam
        "Да уж, талантливый человек талантлив во всём."
    elif alt_day2_hf2 == 5:
        show us_playon:
            pos (648,698)
        with diam
        "Мелкая и не думала учить правила игры."
        "Вместо этого она явно прибегла к какому-то жульничеству."
    elif alt_day2_hf2 == 6:
        show sh_playon:
            pos (648,698)
        with diam
        "Честно сказать, не удивлён. У него были все шансы."
    elif alt_day2_hf2 == 7:
        show mz_playon:
            pos (648,698)
        with diam
        "Она с неудовольствием скривилась, кажется, поняла, что победа значит ещё и дальнейшее участие в этой дурацкой игре."
    
    "Случайность, наверное."
    if ((alt_player3 == 1) or (alt_player4 == 1)) and (alt_day2_hf2 != 1):
        if alt_player3 == 1:
            show un_playon:
                pos (459,620)
        else:
            show un_playon:
                pos (459,775)
        with dissolve
        "Лена тихо поднялась и присоединилась к болельщикам."
        hide un_playon with diam
    elif ((alt_player3 == 2) or (alt_player4 == 2)) and (alt_day2_hf2 != 2):
        if alt_player3 == 1:
            show sl_playon:
                pos (459,620)
        else:
            show sl_playon:
                pos (459,775)
        with dissolve
        "Славя пожала плечами и поднялась — кажется, она куда-то торопилась."
        hide sl_playon with diam
    elif ((alt_player3 == 3) or (alt_player4 == 3)) and (alt_day2_hf2 != 3):
        if alt_player3 == 1:
            show dv_playon:
                pos (459,620)
        else:
            show dv_playon:
                pos (459,775)
        with dissolve
        "Увидеть лицо Двачевской, терпящей поражение — бесценно!"
        "Я расхохотался, прикрываясь рукой, но она, похоже, услышала — обожгла взглядом."
        hide dv_playon with diam
    elif ((alt_player3 == 4) or (alt_player4 == 4)) and (alt_day2_hf2 != 4):
        if alt_player3 == 1:
            show mi_playon:
                pos (459,620)
        else:
            show mi_playon:
                pos (459,775)
        with dissolve
        "Мику поднялась, помахала всем и встала к болельщикам."
        "Она была чем-то очень довольная."
        hide mi_playon with diam
    elif ((alt_player3 == 5) or (alt_player4 == 5)) and (alt_day2_hf2 != 5):
        if alt_player3 == 1:
            show us_playon:
                pos (459,620)
        else:
            show us_playon:
                pos (459,775)
        with dissolve
        "Ульяна надулась, закричала что-то и пробовала было топать ногами, но Ольга Дмитриевна быстро успокоила её."
        "Понурившись, мелкая побрела прочь из столовой."
        hide us_playon with diam
    elif ((alt_player3 == 6) or (alt_player4 == 6)) and (alt_day2_hf2 != 6):
        if alt_player3 == 1:
            show sh_playon:
                pos (459,620)
        else:
            show sh_playon:
                pos (459,775)
        with dissolve
        "Шурик среагировал так, как я и ожидал — поправил очки, резким движением отбросил чёлку со лба и встал."
        "Коротко наклонил голову и занял своё место в толпе."
        hide sh_playon with diam
    elif ((alt_player3 == 7) or (alt_player4 == 7)) and (alt_day2_hf2 != 7):
        if alt_player3 == 1:
            show mz_playon:
                pos (459,620)
        else:
            show mz_playon:
                pos (459,775)
        with dissolve
        "С видом величайшего облегчения Женя бросила карты на стол и, встав, направилась на улицу."
        hide mz_playon with diam
        
    "За третьим же столом, кажется, всё подыгрывало"
    $ alt_dd3 = renpy.random.choice([10, 1])
    if alt_dd3 == 10:
        $ alt_day2_hf3 = alt_player5
    else:
        $ alt_day2_hf3 = alt_player6
        
    if alt_day2_hf3 == 1:
        extend " Лене."
        if alt_day2_hf3 == alt_player5:
            show un_playon:
                pos (1315,157)
        else:
            show un_playon:
                pos (1315,312)
    elif alt_day2_hf3 == 2:
        extend " Славе."
        if alt_day2_hf3 == alt_player5:
            show sl_playon:
                pos (1315,157)
        else:
            show sl_playon:
                pos (1315,312)
    elif alt_day2_hf3 == 3:
        extend " Алисе."
        if alt_day2_hf3 == alt_player5:
            show dv_playon:
                pos (1315,157)
        else:
            show dv_playon:
                pos (1315,312)
    elif alt_day2_hf3 == 4:
        extend " Мику."
        if alt_day2_hf3 == alt_player5:
            show mi_playon:
                pos (1315,157)
        else:
            show mi_playon:
                pos (1315,312)
    elif alt_day2_hf3 == 5:
        extend " Ульяне."
        if alt_day2_hf3 == alt_player5:
            show us_playon:
                pos (1315,157)
        else:
            show us_playon:
                pos (1315,312)
    elif alt_day2_hf3 == 6:
        extend " Шурику."
        if alt_day2_hf3 == alt_player5:
            show sh_playon:
                pos (1315,157)
        else:
            show sh_playon:
                pos (1315,312)
    elif alt_day2_hf3 == 7:
        extend " Жене."
        if alt_day2_hf3 == alt_player5:
            show mz_playon:
                pos (1315,157)
        else:
            show mz_playon:
                pos (1315,312)
    $ renpy.pause(.3)
    if alt_day2_hf3 == 1:
        show un_playon:
            pos (1135,235)
        with diam
        "Ей пришлось потрудиться, но победа оказалась за ней."
    elif alt_day2_hf3 == 2:
        show sl_playon:
            pos (1135,235)
        with diam
        "Активистка, похоже, не поняла, что произошло, но покорно пересела за стол полуфиналистов."
    elif alt_day2_hf3 == 3:
        show dv_playon:
            pos (1135,235)
        with diam
        "Она раскатала противника с разгромным счётом — кажется, наслаждалась игрой."
    elif alt_day2_hf3 == 4:
        show mi_playon:
            pos (1135,235)
        with diam
        "Да уж, талантливый человек талантлив во всём."
    elif alt_day2_hf3 == 5:
        show us_playon:
            pos (1135,235)
        with diam
        "Мелкая и не думала учить правила игры."
        "Вместо этого она явно прибегла к какому-то жульничеству."
    elif alt_day2_hf3 == 6:
        show sh_playon:
            pos (1135,235)
        with diam
        "Честно сказать, не удивлён. У него были все шансы."
    elif alt_day2_hf3 == 7:
        show mz_playon:
            pos (1135,235)
        with diam
        "Она с неудовольствием скривилась, кажется, поняла, что победа значит ещё и дальнейшее участие в этой дурацкой игре."
    
    "Побеждённому оставалось лишь признать своё поражение."
    if ((alt_player5 == 1) or (alt_player6 == 1)) and (alt_day2_hf3 != 1):
        if alt_player5 == 1:
            show un_playon:
                pos (1315,157)
        else:
            show un_playon:
                pos (1315,312)
        with dissolve
        "Лена тихо поднялась и присоединилась к болельщикам."
        hide un_playon with diam
    elif ((alt_player5 == 2) or (alt_player6 == 2)) and (alt_day2_hf3 != 2):
        if alt_player5 == 1:
            show sl_playon:
                pos (1315,157)
        else:
            show sl_playon:
                pos (1315,312)
        with dissolve
        "Славя пожала плечами и поднялась — кажется, она куда-то торопилась."
        hide sl_playon with diam
    elif ((alt_player5 == 3) or (alt_player6 == 3)) and (alt_day2_hf3 != 3):
        if alt_player5 == 1:
            show dv_playon:
                pos (1315,157)
        else:
            show dv_playon:
                pos (1315,312)
        with dissolve
        "Увидеть лицо Двачевской, терпящей поражение — бесценно!"
        "Я расхохотался, прикрываясь рукой, но она, похоже, услышала — обожгла взглядом."
        hide dv_playon with diam
    elif ((alt_player5 == 4) or (alt_player6 == 4)) and (alt_day2_hf3 != 4):
        if alt_player5 == 1:
            show mi_playon:
                pos (1315,157)
        else:
            show mi_playon:
                pos (1315,312)
        with dissolve
        "Мику поднялась, помахала всем и встала к болельщикам."
        "Она была чем-то очень довольная."
        hide mi_playon with diam
    elif ((alt_player5 == 5) or (alt_player6 == 5)) and (alt_day2_hf3 != 5):
        if alt_player5 == 1:
            show us_playon:
                pos (1315,157)
        else:
            show us_playon:
                pos (1315,312)
        with dissolve
        "Ульяна надулась, закричала что-то и пробовала было топать ногами, но Ольга Дмитриевна быстро успокоила её."
        "Понурившись, мелкая побрела прочь из столовой."
        hide us_playon with diam
    elif ((alt_player5 == 6) or (alt_player6 == 6)) and (alt_day2_hf3 != 6):
        if alt_player5 == 1:
            show sh_playon:
                pos (1315,157)
        else:
            show sh_playon:
                pos (1315,312)
        with dissolve
        "Шурик среагировал так, как я и ожидал — поправил очки, резким движением отбросил чёлку со лба и встал."
        "Коротко наклонил голову и занял своё место в толпе."
        hide sh_playon with diam
    elif ((alt_player5 == 7) or (alt_player6 == 7)) and (alt_day2_hf3 != 7):
        if alt_player5 == 1:
            show mz_playon:
                pos (1315,157)
        else:
            show mz_playon:
                pos (1315,312)
        with dissolve
        "С видом величайшего облегчения Женя бросила карты на стол и, встав, направилась на улицу."
        hide mz_playon with diam
    return
    
label alt_day2_hf_analizer:
    $ alt_dd11 = renpy.random.choice([10, 1])
    "На соседнем же столе борьба разыгралась нешуточная."
    scene bg int_dining_hall_sunset
    show alt_tournament_bg
    with dissolve
    "Но удача сегодня совершенно определённо улыбалась"
    if alt_dd11 == 10:
        $ alt_day2_f1 = alt_day2_hf1
    else:
        $ alt_day2_f1 = alt_day2_hf3
    if alt_day2_f1 == 1:
        extend " Лене."
        if alt_day2_hf1 == 1:
            show un_playon:
                pos (648,235)
        else:        
            show un_playon:
                pos (1135,235)
    elif alt_day2_f1 == 2:
        extend " Славе."
        if alt_day2_hf1 == 2:
            show sl_playon:
                pos (648,235)
        else:        
            show sl_playon:
                pos (1135,235)
    elif alt_day2_f1 == 3:
        extend " Алисе."
        if alt_day2_hf1 == 3:
            show dv_playon:
                pos (648,235)
        else:        
            show dv_playon:
                pos (1135,235)
    elif alt_day2_f1 == 4:
        extend " Мику."
        if alt_day2_hf1 == 1:
            show mi_playon:
                pos (648,235)
        else:        
            show mi_playon:
                pos (1135,235)
    elif alt_day2_f1 == 5:
        extend " Ульянке."
        if alt_day2_hf1 == 5:
            show us_playon:
                pos (648,235)
        else:        
            show us_playon:
                pos (1135,235)
    elif alt_day2_f1 == 6:
        extend " Шурику."
        if alt_day2_hf1 == 6:
            show sh_playon:
                pos (648,235)
        else:        
            show sh_playon:
                pos (1135,235)
    elif alt_day2_f1 == 7:
        extend " Жужелице."
        if alt_day2_hf1 == 7:
            show mz_playon:
                pos (648,235)
        else:        
            show mz_playon:
                pos (1135,235)
                
    $ renpy.pause(.3)
    if alt_day2_hf1 == 1:
        show un_playon:
            pos (890,360)
        with diam
        "Вот уже вторую игру подряд она сидит с потерянным видом, но ей достаются всё более сильные комбинации. Не подыгрывает ли ей крупье?"
    elif alt_day2_hf1 == 2:
        show sl_playon:
            pos (890,360)
        with diam
        "Девушка ворчала и пожимала плечами, не особо желая продолжать игру, кажется, она и присоединиться-то решила из одного лишь чувства товарищества."
    elif alt_day2_hf1 == 3:
        show dv_playon:
            pos (890,360)
        with diam
        "Рыжая пёрла бульдозером, не задерживаясь ни на одном из оппонентов — её целью был финал, и никак иначе!"
    elif alt_day2_hf1 == 4:
        show mi_playon:
            pos (890,360)
        with diam
        "Она радовалась каждой удачной карте как маленький ребёнок, а когда вскрылись и сверили комбинации — то от радости завизжала и полезла было на стол петь, но была вовремя удалена оттуда бдительной вожатой."
    elif alt_day2_hf1 == 5:
        show us_playon:
            pos (890,360)
        with diam
        "Мелкая сегодня в ударе."
        "Вторая игра подряд без знания правил — практически как вождение автомобиля без рук."
    elif alt_day2_hf1 == 6:
        show sh_playon:
            pos (890,360)
        with diam
        "Он не показывал особого интереса. Быть может, в этом и был его секрет?"
    elif alt_day2_hf1 == 7:
        show mz_playon:
            pos (890,360)
        with diam
        "Меня откровенно забавляло то, что она-то как раз меньше всего хотела играть."
        "А ушла так далеко."
        
    "Второму полуфиналисту повезло куда меньше."
    if ((alt_day2_hf1 == 1) or (alt_day2_hf3 == 1)) and (alt_day2_f1 != 1):
        if alt_day2_hf1 == 1:
            show un_playon:
                pos (648,235)
        else:
            show un_playon:
                pos (1135,235)
        $ renpy.pause(1)
        hide un_playon with diam
        "Лена тихо поднялась и присоединилась к болельщикам."
    elif ((alt_day2_hf1 == 2) or (alt_day2_hf3 == 2)) and (alt_day2_f1 != 2):
        if alt_day2_hf1 == 2:
            show sl_playon:
                pos (648,235)
        else:
            show sl_playon:
                pos (1135,235)
        $ renpy.pause(1)
        hide sl_playon with diam
        "Славя замученно улыбнулась и с огромным облегчением отодвинула карты."
        sl "Всё, наигралась на год вперёд."
        "Она поднялась и пошла к ждущей её Ольге Дмитриевне."
    elif ((alt_day2_hf1 == 3) or (alt_day2_hf3 == 3)) and (alt_day2_f1 != 3):
        if alt_day2_hf1 == 3:
            show dv_playon:
                pos (648,235)
        else:
            show dv_playon:
                pos (1135,235)
        $ renpy.pause(1)
        hide dv_playon with diam
        "Алиса долго не хотела верить в то, что проиграла."
        "Она даже пыталась заставить судью назначить переигровку — безрезультатно."
        "Она встала из-за стола, цедя непечатное."
    elif ((alt_day2_hf1 == 4) or (alt_day2_hf3 == 4)) and (alt_day2_f1 != 4):
        if alt_day2_hf1 == 4:
            show mi_playon:
                pos (648,235)
        else:
            show mi_playon:
                pos (1135,235)
        $ renpy.pause(1)
        hide mi_playon with diam
        "Посмотрела на свои карты ещё раз, видимо, пытаясь запомнить получше."
        "А может, она так и не усвоила правил игры."
        "Я бы не удивился."
    elif ((alt_day2_hf1 == 5) or (alt_day2_hf3 == 5)) and (alt_day2_f1 != 5):
        if alt_day2_hf1 == 5:
            show us_playon:
                pos (648,235)
        else:
            show us_playon:
                pos (1135,235)
        $ renpy.pause(1)
        hide us_playon with diam
        us "Эй, вы все неправильно играли! Вы все жулики, жулики!"
        "Кричала она, отбиваясь."
        "Минут десять только ушло на то, чтобы немного успокоить её и привести в чувство."
        "Она топнула ногой и выбежала из зала."
    elif ((alt_day2_hf1 == 6) or (alt_day2_hf3 == 6)) and (alt_day2_f1 != 6):
        if alt_day2_hf1 == 6:
            show sh_playon:
                pos (648,235)
        else:
            show sh_playon:
                pos (1135,235)
        $ renpy.pause(1)
        hide sh_playon with diam
        "Шурик кивнул и поднялся из-за стола."
        "Кажется, у него проблемы с проявлением эмоций."
    elif ((alt_day2_hf1 == 7) or (alt_day2_hf3 == 7)) and (alt_day2_f1 != 7):
        if alt_day2_hf1 == 7:
            show mz_playon:
                pos (648,235)
        else:
            show mz_playon:
                pos (1135,235)
        $ renpy.pause(1)
        hide mz_playon with diam
        "Давненько я не видел, чтобы так бурно радовались поражению."
        "Женя разулыбалась, вздохнула, расправила плечи."
        mz "Ну наконец-то!"
        "Рявкнула она и вышла вон из столовой."
    
    
    "Что же касается нашего стола…"
    if alt_day2_round2 == 1:
        $ alt_day2_f2 = alt_day2_hf2
        "Так как я сдулся и проиграл, в финал отправляется"
        if alt_day2_hf2 == 1:
            extend " Лена"
            show un_playon:
                pos (720,698)
            $ renpy.pause(.3)
            hide un_playon
            show un_playon:
                pos (890,575)
            with diam
        elif alt_day2_hf2 == 2:
            extend " Славя"
            show sl_playon:
                pos (720,698)
            $ renpy.pause(.3)
            hide sl_playon
            show sl_playon:
                pos (890,575)
            with diam
        elif alt_day2_hf2 == 3:
            extend " Алиса"
            show dv_playon:
                pos (720,698)
            $ renpy.pause(.3)
            hide dv_playon
            show dv_playon:
                pos (890,575)
            with diam
        elif alt_day2_hf2 == 4:
            extend " Мику"
            show mi_playon:
                pos (720,698)
            $ renpy.pause(.3)
            hide mi_playon
            show mi_playon:
                pos (890,575)
            with diam
        elif alt_day2_hf2 == 5:
            extend " Ульяна"
            show us_playon:
                pos (720,698)
            $ renpy.pause(.3)
            hide us_playon
            show us_playon:
                pos (890,575)
            with diam
        elif alt_day2_hf2 == 6:
            extend " Шурик"
            show sh_playon:
                pos (720,698)
            $ renpy.pause(.3)
            hide sh_playon
            show sh_playon:
                pos (890,575)
            with diam
        elif alt_day2_hf2 == 7:
            extend " Женя"
            show mz_playon:
                pos (720,698)
            $ renpy.pause(.3)
            hide mz_playon
            show mz_playon:
                pos (890,575)
        with diam
        extend ", где встретит"
        if alt_day2_f1 == 1:
            extend " Лену и попытается обыграть её."
        elif alt_day2_f1 == 2:
            extend " Славю и докажет всем, что блондинка — это диагноз."
        elif (alt_day2_f1 == 3) and (alt_day2_f2 == 5):
            extend "… Алису? Так они с самого начала это планировали?!"
        elif alt_day2_f1 == 3:
            extend " Алису и попробует уцелеть в этой схватке."
        elif alt_day2_f1 == 4:
            extend "Мику. {w}Не думаю, что там будет много проблем. Хотя японка и добралась до финала."
        elif (alt_day2_f1 == 5) and (alt_day2_f2 == 3):
            extend " Ульянку."
            "Смешно, но, похоже, рыжие в самом деле попросту разметали этот турнир по брёвнышку, как и хотели."
        elif alt_day2_f1 == 5:
            extend " Ульяну и попробует выжить после встречи с ней."
        elif alt_day2_f1 == 6:
            extend " Шурика и попробует доказать, что мозги в карточной игре не решают."
        elif alt_day2_f1 == 7:
            extend " Женю."
            "Что ещё можно про неё сказать?"
            "Во. Жужелица."
    else:
        show me_playon:
            pos (890,575)
        with diam
        "Я двигаюсь уверенно, следующая моя жертва уже видна на горизонте."
        if alt_day2_f1 == 1:
            "Прости, Лена. Ничего личного."
        elif alt_day2_f1 == 2:
            "Славя. Ну, она всё равно без души играет, так что я ей только доброе дело сделаю."
        elif alt_day2_f1 == 3:
            "Алиса, ага."
            me "Алиса, а Алиса."
            dv "Чего?"
            me "Тебе конец."
            "Она расхохоталась."
        elif alt_day2_f1 == 4:
            "Мику."
            "Как галантный парень я склонен сдать эту партию, чтобы сделать девушке приятное."
            "Но как игрок я чувствую запах победы, поэтому никакой пощады!"
        elif alt_day2_f1 == 5:
            "Мелкая? Блин, кто-нибудь объясните мне внятно, какого чёрта это мелкое недоразумение забыло в финале?"
        elif alt_day2_f1 == 6:
            "Шурик? Хм. Это будет интересный бой."
        elif alt_day2_f1 == 7:
            "Жужелица."
            "Может быть, и скрипит о том, что играть не хочет, но — блин, она же в финале!"
            "Придётся потрудиться."
    return
