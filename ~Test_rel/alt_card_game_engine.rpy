init 1 python:                                              # начинаем на шаг позже оригинала
    alt_hint_poker = False                                  # окна с подсказками отключены
    alt_my_poker_hand = None                                # моя комбинация (цифры)
    alt_rival_poker_hand = None                             # комбинация соперника (цифры)
    alt_name_my_poker_hand = None                           # моя комбинация для подсказки
    alt_name_rival_poker_hand  = None                       # комбинация соперника для подсказки
    alt_whose_first_move = 'rival'                          # кто первый ходит (соперник - 'rival'; игрок - 'player')
    alt_name_my_rival_r = "соперника"                       # подписываем "подсказку" соперника
    
# ---------------------------------------------------------------------------------------------
    def show_cards_alt(): 
        renpy.scene('underlay')
        renpy.show(cards_bg,layer='underlay')
        ui.layer('underlay')
        for i in range(0,n_cards):
            if  cards_rival[i].interesting :
                x = int(card_dx*i+card_left_dx+card_width/2.0-arrow_width/2.0)
                y = card_top_dy+card_height+20
                ui.at( Move( (x,y), (x,y), 1 ) )
                ui.image(card_up,xpos=x,ypos=y)
            if  cards_state == "me_select_2" and cards_rival[i].allow:
                card_button(cards_rival[i], card_dx*i+card_left_dx, card_top_dy+cards_rival[i].dy, ("rival",i))
            else:
                card_button(cards_rival[i], card_dx*i+card_left_dx, card_top_dy+cards_rival[i].dy, "ignore")
            if  cards_my[i].interesting:
                x = int(card_dx*i+card_left_dx+card_width/2.0-arrow_width/2.0)
                y = card_bottom_dy-100
                ui.at( Move( (x,y), (x,y), 1 ) )
                ui.image(card_down,xpos=x,ypos=y)
            if  cards_state in ["me_select_1","me_defend_1","me_defend_2","rival_select"] or (cards_state == "me_select_2" and i==my_card) :
                card_button(cards_my[i], card_dx*i+card_left_dx, card_bottom_dy+cards_my[i].dy, ("my",i))
            else:
                card_button(cards_my[i], card_dx*i+card_left_dx, card_bottom_dy+cards_my[i].dy, "ignore")
                
        if  cards_state in ["interuption","init"]:
            ui.close()
            return
            
        avatar = LiveComposite(
                         (210,210),
                         (0,0), avatar_frame,
                         (5,5), rival.avatar['body'],
                         (5,5), rival.avatar[rival.mood],
                     )

        ui.imagebutton(avatar,avatar,clicked=None,
                  xpos=card_dx*(n_cards)+card_left_dx+20,
                  ypos=card_top_dy,
              )

        ui.button(clicked=None, xanchor=1.0, xpadding=6, xminimum=200,
                  xpos=card_dx*(n_cards+1)+card_left_dx+button_dx,
                  ypos=card_top_dy+220,
                  style=style.cards_button,
              )
        ui.text(u"Соперник:",style="button_text",size=15)

        ui.button(clicked=None, xanchor=1.0, xpadding=6, xminimum=200,
                  xpos=card_dx*(n_cards+1)+card_left_dx+button_dx,
                  ypos=card_top_dy+240,
                  style=style.cards_button,
              )
        ui.text(rival.name,style="button_text",size=25)

        ui.button(clicked=None, xanchor=1.0, xpadding=6, xminimum=200,
                  xpos=card_dx*(n_cards+1)+card_left_dx+button_dx,
                  ypos=card_bottom_dy+0,
                  style=style.cards_button,
              )
        ui.text(u"Чей ход:",style="button_text",size=15)

        ui.button(clicked=None, xanchor=1.0, xpadding=6, xminimum=200,
                  xpos=card_dx*(n_cards+1)+card_left_dx+button_dx,
                  ypos=card_bottom_dy+20,
                  style=style.cards_button,
              )
        if  cards_state in ["me_defend_1","me_defend_2","me_get","me_select_1","me_select_2"]:
            ui.text(u"Твой",style="button_text",size=25)
        if  cards_state in ["rival_defend","rival_get","rival_select"]:
            ui.text(u"Чужой",style="button_text",size=25)
        if  cards_state in ["results"]:
            ui.text(u"---",style="button_text",size=25)

        ui.button(clicked=None, xanchor=1.0, xpadding=6, xminimum=200,
                  xpos=card_dx*(n_cards+1)+card_left_dx+button_dx,
                  ypos=card_bottom_dy+90 - button_dy,
                  style=style.cards_button,
              )
        ui.text(u"Фаза игры:",style="button_text",size=15)

        ui.button(clicked=None, xanchor=1.0, xpadding=6, xminimum=200,
                  xpos=card_dx*(n_cards+1)+card_left_dx+button_dx,
                  ypos=card_bottom_dy+110 - button_dy,
                  style=style.cards_button,
              )
        if  cards_state in ["me_defend_1","me_defend_2","rival_defend"]:
            ui.text(u"Защита",style="button_text",size=25)
        if  cards_state == "me_select_1":
            ui.text(u"Сброс",style="button_text",size=25)
        if  cards_state in ["me_select_2","rival_select"]:
            ui.text(u"Захват",style="button_text",size=25)
        if  cards_state in ["me_get","rival_get"]:
            if  CARD_GAME_WITH_EXCHANGE:
                ui.text(u"Обмен",style="button_text",size=25)
            else:
                ui.text(u"Вытягивание",style="button_text",size=25)
        if  cards_state in ["results"]:
            ui.text(u"Итоги",style="button_text",size=25)

        if  cards_state in ["me_defend_1","me_defend_2"]:
            ui.button(clicked=ui.returns("end_of_turn"), xanchor=1.0, xpadding=6, xminimum=25,
                      xpos=card_dx*(n_cards+1)+card_left_dx+button_dx,
                      ypos=card_bottom_dy+110 - button_dy,
                      style=style.cards_button,
                  )
            ui.text(u"X",style="button_text",size=25)

        ui.button(clicked=None, xanchor=1.0, xpadding=6, xminimum=200,
                  xpos=card_dx*(n_cards+1)+card_left_dx+button_dx,
                  ypos=card_bottom_dy+180 - button_dy,
                  style=style.cards_button,
              )
        ui.text(u"Кругов осталось:",style="button_text",size=15)

        ui.button(clicked=None, xanchor=1.0, xpadding=6, xminimum=200,
                  xpos=card_dx*(n_cards+1)+card_left_dx+button_dx,
                  ypos=card_bottom_dy+200 - button_dy,
                  style=style.cards_button,
              )
        ui.text("%d"%cycles_left,style="button_text",size=25)

        ui.button(clicked=None, xanchor=1.0, xpadding=6, xminimum=200,
                  xpos=card_dx*(n_cards+1)+card_left_dx+button_dx,
                  ypos=card_bottom_dy+270 - button_dy,
                  style=style.cards_button,
              )
        ui.text(u"Обменов осталось:",style="button_text",size=15)

        ui.button(clicked=None, xanchor=1.0, xpadding=6, xminimum=200,
                  xpos=card_dx*(n_cards+1)+card_left_dx+button_dx,
                  ypos=card_bottom_dy+290 - button_dy,
                  style=style.cards_button,
              )
        if  changes_left == 0:
            changes_left_text = "---"
        else:
            changes_left_text = "%d"%changes_left
        ui.text(changes_left_text,style="button_text",size=25)

        if VISIBLE and alt_hint_poker:
            ui.button(clicked=None, xanchor=0.5, xpadding=10, xminimum=400,
                xpos = screen_width/2,
                ypos = screen_height - card_top_dy - bottom_dy,
                style=style.cards_button,
            )
            ui.text("%s - %s" % ("У меня", alt_name_my_poker_hand),style="button_text",size=23)

        if (INVISIBLE or cards_rival[0].visible == 'VISIBLE') and alt_hint_poker: 
            ui.button(clicked=None, xanchor=0.5, xpadding=10, xminimum=400,
                xpos = screen_width/2,
                ypos = card_top_dy - 28,
                style=style.cards_button,
            )
            ui.text("%s %s - %s" % ("У", alt_name_my_rival_r, alt_name_rival_poker_hand),style="button_text",size=23)

        if  result_status != 'in_progress':
            renpy.block_rollback()
            ui.button(clicked=ui.returns("ok"), xanchor=1.0, xpadding=6, xminimum=200,
                  xpos=screen_width/2+100,
                  ypos=screen_height/2-35 - bottom_dy - bottom_dy_result,
                  style=style.cards_button,
              )
            if  result_status == 'win':
                ui.text(u"Победа",style="button_text",size=72)
            if  result_status == 'draw':
                ui.text(u"Ничья",style="button_text",size=72)
            if  result_status == 'fail':
                ui.text(u"FAIL",style="button_text",size=72)
        ui.close() 

# -----------------------------------------------------------------------------------------------------------------------------------------------------
    def cards_interact_alt(): 
        show_cards_alt()
        answer = ui.interact()
        if  answer=="ignore":
            ui.jumps("cards_gameloop_wise_alt")()
        if cards_state == "me_defend_1":
            renpy.music.play("sound/sfx/cardgame/new/choose_card_2.ogg", channel="sound")
        elif cards_state == "me_defend_2":
            renpy.music.play("sound/sfx/cardgame/new/choose_card_1.ogg", channel="sound")
        return answer
# -----------------------------------------------------------------------------------------------------------------------------------------------------
    def card_value_alt_as_max(x): # Получаем значения карт. Туз = 14 (старший)
        if  x.name[0] == 1:
            return 14
        else:
            return x.name[0]
            
    def card_value_alt_as_min(x): # Получаем значения карт. Туз = 1 (младший)
        return x.name[0]
# -----------------------------------------------------------------------------------------------------------------------------------------------------
    def sort_cards_alt_as_max(): # сортировка - туз старший
        cards_rival.sort(cmp,card_value_alt_as_max)
        cards_my.sort(cmp,card_value_alt_as_max)

    def sort_cards_alt_as_min(): # сортировка - туз младший
        cards_rival.sort(cmp,card_value_alt_as_min)
        cards_my.sort(cmp,card_value_alt_as_min)

    def sort_cards_alt_upshot(): # итоговая сортировка карт
        global cards_rival
        global cards_my
        
        rival_hand = what_category_alt(cards_rival)                     # посмотрели, что на руках у соперника
        my_hand = what_category_alt(cards_my)                           # посмотрели, что у нас на руках
        
        if rival_hand[0] in [4,8] and rival_hand[1] == 5:               # если стриты и старшая карта 5 (младший стрит) у соперника
            cards_rival.sort(cmp,card_value_alt_as_min)                 # сортируем карты соперника - туз младший
        else:                                                           # во всех прочих случаях
            cards_rival.sort(cmp,card_value_alt_as_max)                 # сортируем карты соперника - туз старший
        cards_rival.reverse()                                           # "переворачиваем" карты - старшая карта слева
        if not CARD_GAME_WITH_EXCHANGE:                                 # если сдавалось по шести карт
            temp = cards_rival.pop(n_cards-1)                           # "вынимаем" последнюю (правую) - пустую карту
            cards_rival.insert(0,temp)                                  # .. и "вставляем" её в начало (слева)
            
        if my_hand[0] in [4,8] and my_hand[1] == 5:                     # если стриты и старшая карта 5 (младший стрит) у нас
            cards_my.sort(cmp,card_value_alt_as_min)                    # сортируем свои карты - туз младший 
        else:                                                           # во всех прочих случаях
            cards_my.sort(cmp,card_value_alt_as_max)                    # сортируем свои карты - туз старший
        cards_my.reverse()                                              # "переворачиваем" карты - старшая карта слева
        if not CARD_GAME_WITH_EXCHANGE:                                 # если сдавалось по шести карт
            temp = cards_my.pop(n_cards-1)                              # "вынимаем" последнюю (правую) - пустую карту
            cards_my.insert(0,temp)                                     # .. и "вставляем" её в начало (слева)

# -----------------------------------------------------------------------------------------------------------------------------------------------------
    def interuption_region_alt():
        global cycles_left
        global cards_state
        if cards_state == "me_select_1" or cards_state == "me_defend_1": #Ошибка?
            renpy.music.play("sound/sfx/cardgame/new/choose_card_2.ogg", channel="sound")
        elif cards_state == "rival_defend":
            renpy.music.play("sound/sfx/cardgame/new/choose_card_1.ogg", channel="sound")
        position = (cycles_left,cards_state,"call")
        if  position in game_interuptions:
            tmp_state = cards_state
            cards_state = "interuption"
            show_cards_alt()
            renpy.call_in_new_context(game_interuptions[position])
            renpy.block_rollback()
            cards_state = tmp_state
            del game_interuptions[position]
        position = (cycles_left,cards_state,"jump")
        if  position in game_interuptions:
            tmp_state = cards_state
            cards_state = "interuption"
            renpy.scene('underlay')
            ui.jumps(game_interuptions[position])()
# -----------------------------------------------------------------------------------------------------------------------------------------------------
# Покерные комбинации (по старшинству):
#  9 - Роял-флеш      (royal flush)       = Т,К,Д,В,10 одной масти
#  8 - Стрит-флеш     (straight flush)    = 5 карт по порядку ОДНОЙ масти, туз может быть первым (роял-флеш) и последним (..3,2,Т)
#  7 - Каре           (quads)             = 4 карты одного достоинства
#  6 - Фул-хауз       (full house)        = тройка + пара
#  5 - Флеш           (flush)             = 5 карт ОДНОЙ масти
#  4 - Стрит          (straight)          = 5 карт по порядку ЛЮБОЙ масти, туз может быть первым (Т,К,Д..) и последним (..3,2,Т)
#  3 - Тройка         (three of a kind)   = 3 карты одного достоинства
#  2 - Две пары       (two pairs)         = две двойки
#  1 - Одна пара      (one pair)          = 2 карты одного достоинства
#  0 - Старшая карта  (high card)         = ни одной вышеперечисленной комбинации, берется старшая карта
#
# Если комбинации одинаковы = выигрыш по большей карте в комбинации
#
# Масти: "2ch","ussr","utan","uvao"
# Картинки: В = 11, Д = 12, К = 13, Т = 1 / 14            
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def what_suit_cards_alt(cardset):                               # определяем количество карт в мастях - передаем кардсет
        cardset_tmp = cardset[:]                                    # копируем кардсет, упражняемся с ним, не трогаем основной
    # ............................................. 
        total_2ch = 0                                               # количество карт масти 2ch
        total_ussr = 0                                              # количество карт масти ussr
        total_utan = 0                                              # количество карт масти utan
        total_uvao = 0                                              # количество карт масти uvao
        value_2ch = 0                                               # старшая карта масти 2ch
        value_ussr = 0                                              # старшая карта масти ussr
        value_utan = 0                                              # старшая карта масти utan
        value_uvao = 0                                              # старшая карта масти uvao
        suit_max = 0                                                # количество карт максимальной масти
        suit_value = 0                                              # старшая карта максимальной масти
        suit_numb = None                                            # номер максимальной масти
    # .............................................
        cardset_tmp.sort(cmp,card_value_alt_as_max)                 # сортируем список от 2
    # .............................................
        for i in range(0,n_cards):
            if cardset_tmp[i].name[1] == "2ch":                     # если карта ЭТОЙ масти
                total_2ch += 1                                      # увеличиваем счетчик ЭТОЙ масти на 1
                value_2ch = cardset_tmp[i].name[0]                  # значение максимума принимаем по значению карты
            elif cardset_tmp[i].name[1] == "ussr":
                total_ussr += 1
                value_ussr = cardset_tmp[i].name[0]
            elif cardset_tmp[i].name[1] == "utan":
                total_utan += 1
                value_utan = cardset_tmp[i].name[0]
            elif cardset_tmp[i].name[1] == "uvao":
                total_uvao += 1
                value_uvao = cardset_tmp[i].name[0]
    # .............................................
        suit_max = max(total_2ch, total_ussr, total_utan, total_uvao) # выясняем максимум карт одной масти
        if suit_max >= 5:                                           # если максимальное количество карт в масти >= 5
            if suit_max == total_2ch:                               # если max = ЭТОЙ масти
                suit_numb = 0                                       # номер масти = ЭТОЙ масти
                suit_value = value_2ch                              # старшая карта - по ЭТОЙ масти
            elif suit_max == total_ussr:
                suit_numb = 1
                suit_value = value_ussr
            elif suit_max == total_utan:
                suit_numb = 2
                suit_value = value_utan
            elif suit_max == total_uvao:
                suit_numb = 3
                suit_value = value_uvao
    # .............................................
            if suit_value == 1:                                     # если туз определился, как младший
                suit_value = 14                                     # возвращаем 14 очков
    # .............................................
        return suit_numb, suit_value                                # возвращаем имя масти, максмальную карту масти
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def what_sequence_cards_alt(cardset):                           # определяем последовательность карт у нас на руках - передаем кардсет
        cardset_tmp = cardset[:]                                    # копируем кардсет, упражняемся с ним, не трогаем основной
    # ............................................. 
        combo_sequence = False                                      # последовательности нет
        orders = ['min','max']                                      # туз - младший, старший
        order = None
        len_seq_max_k = [0,0]                                       # количество карт в максимальной последовательности [мин, макс] 
        seq_value_k = [0,0]                                         # старшая карта в последовательности  [мин, макс]
        len_seq_max = 0                                             # количество карт в максимальной последовательности ИТОГО
        seq_value = 0                                               # старшая карта в последовательности ИТОГО
    # .............................................    
        for k in range(0,2):                                        # для минимума (0) и максимума (1)
            order = orders[k]                                       # сортировка по порядку
            if order == 'min':                                      # если порядок сортировки - туз = меньшая карта
                cardset_tmp.sort(cmp,card_value_alt_as_min)         # сортируем список от 1
            elif order == 'max':                                    # если порядок сортировки - туз = старшая карта
                cardset_tmp.sort(cmp,card_value_alt_as_max)         # сортируем список от 2
            val_i = 0                                                   # количество очков текущей карты в переборе
            val_prev = 0                                                # количество очков предыдущей карты в переборе 
            run_number = 0                                              # номер результативного прохода
            len_seq_run = 0                                             # количество карт в возможных последовательностях на проходах
            for i in range(0,n_cards):                              # цикл в цикле - перебираем карты
                if order == 'min':                                  # если порядок сортировки - туз = меньшая карта
                    val_i = card_value_alt_as_min(cardset_tmp[i])   # читаем значение очередной карты; туз = 1
                elif order == 'max':                                # если порядок сортировки - туз = старшая карта
                    val_i = card_value_alt_as_max(cardset_tmp[i])   # читаем значение очередной карты; туз = 14
    # ............................................. 
                if val_i != 0:                                          # если карта нормальная
                    run_number +=1                                      # увеличиваем счетчих проходов
                    if run_number == 1:                                 # на первом проходе
                        len_seq_run = 1                                 # длину текущей последовательности принимаем = 1, карты не сравниваем - не с чем
                        len_seq_max_k[k] = 1                            # длину максимальной последовательности принимаем = 1, карты не сравниваем - не с чем
                    else:                                               # на следующих проходах
                        if val_i == (val_prev + 1):                     # если очередная карта в последовательности
                            len_seq_run += 1                            # длину текущей последовательности увеличиваем на 1
                            if len_seq_run > len_seq_max_k[k]:          # если текущая последовательность больше максимальной
                                len_seq_max_k[k] = len_seq_run          # максимальную последовательность принимаем по текущей
                                seq_value_k[k] = val_i                  # старшую карту принимаем по текущей
                        elif val_i == val_prev:                         # если карты равны 
                            pass                                        # карту пропускаем, последовательность не сбрасываем
                        elif val_i > (val_prev + 1):                    # если очередная карта не в последовательности
                            len_seq_run = 1                             # длину текущей последовательности принимаем = 1
                    val_prev = val_i                                    # значение карты для сравнения принимаем: значение текущей карты
    # ............................................. 
        len_seq_max = max(len_seq_max_k)                                # максимальную длину последовательности принимаем по максимальной из мин-макс
        if len_seq_max == len_seq_max_k[1]:                             # если максимальная последовательность, когда туз старший
            seq_value = seq_value_k[1]                                  # очки старшей карты - по старшей карте, когда туз старший
        else:                                                           # если последовательности равны или минимальная больше
            seq_value = seq_value_k[0]                                  # очки старшей карты - по старшей карте, когда туз младший
            cardset_tmp.sort(cmp,card_value_alt_as_min)                 # и пересортировываем список от 1
    # .............................................
        if len_seq_max >= 5:                                            # если набрали последовательность в 5 карт или больше
            combo_sequence = True                                       #  - есть последовательность
    # .............................................
        return combo_sequence, seq_value                                # возвращаем наличие последовательности, значение старшей карты, набор карт
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def what_amount_cards_alt(cardset):                             # определяем количество карт по достоинству - передаем кардсет
        cardset_tmp = cardset[:]                                    # копируем кардсет, упражняемся с ним, не трогаем основной
    # .............................................
        amount_cards = []                                           # пустой список значений карт на руках
        val_i = 0                                                   # количество очков текущей карты в переборе, туз = 14
        is_four = False                                             # есть четверка
        is_triple = False                                           # есть тройка
        is_pair_one = False                                         # есть пара
        is_pair_two = False                                         # есть вторая пара
        amount_value_four = 0                                       # старшинство в комбинации 4
        amount_value_triple = 0                                     # старшинство в комбинации 3
        amount_value_pair = 0                                       # старшинство в комбинации 2
        amount_value_one = 0                                        # старшинство в комбинации 1 
        combo_number = 0                                            # номер комбинации
        amount_value = 0                                            # старшая карта = 0
        amount_minor = 0                                            # старшинство младшей пары = 0
    # ............................................. 
        cardset_tmp.sort(cmp,card_value_alt_as_max)                 # сортируем список от 2
    # ............................................. 
        for i in range(0,n_cards):
            val_i = card_value_alt_as_max(cardset_tmp[i])           # читаем значение очередной карты; туз = 14
            if val_i != 0:                                          # если карта нормальная
                amount_cards.append (val_i)                         # добавляем значение текущей карты в список
    # ............................................. 
        for j in range(2,15):                                       # пробежимся по значениям карт, (старшая - туз+1)
            if amount_cards.count(j) == 4:                          # проверяем четверку
                amount_value_four = j                               # старшинство в комбинации 4
                is_four = True                                      # есть черверка
                break                                               # есть четверка - дальнейшая проверка смысла не имеет
            elif amount_cards.count(j) == 3:                        # проверяем тройку
                if is_triple:                                       # если УЖЕ есть тройка
                    is_pair_two = True                              # младшую тройку назначаем парой
                    amount_minor = amount_value_triple              # старшинство младшей пары - по старой тройке
                    amount_value_triple = j                         # старшинство в комбинации 3
                    break                                           # есть вторая тройка - дальнейшая проверка смысла не имеет
                else:                                               # тройки еще нет
                    is_triple = True                                # есть тройка
                    amount_value_triple = j                         # старшинство в комбинации 3
                    continue                                        # эту цифру на пару не проверяем
            elif amount_cards.count(j) == 2:                        # проверяем пару
                if is_pair_one:                                     # пара УЖЕ есть
                    is_pair_two = True                              # принимаем вторую пару
                    amount_minor = amount_value_pair                # старшинство младшей пары - по старой паре
                    amount_value_pair = j                           # старшинство в комбинации 2
                    continue                                        # и проверяем следующую цифру
                else:                                               # пары еще нет
                    is_pair_one = True                              # есть пара
                    amount_value_pair = j                           # старшинство в комбинации 2
                    continue                                        # и проверяем следующую цифру
            elif amount_cards.count(j) == 1:                        # если комбинаций нет, но есть карта
                amount_value_one = j                                # назначается старшей
    # ............................................. 
        if is_four:                                                 # если нашли четверку
            amount_value = amount_value_four                        # старшинство - по четверке
            combo_number = 7                                        # комбинация = 'quads' = 7
        elif is_triple:                                             # если тройка
            amount_value = amount_value_triple                      # старшинство - по тройке
            if is_pair_one or is_pair_two:                          # + одна из пар
                combo_number = 6                                    # комбинация = 'full_house' = 6
                amount_minor = amount_value_pair                    # старшинство пары - по старшей паре
            else:                                                   # пар нет
                combo_number = 3                                    # комбинация = 'three_of_a_kind' = 3
        elif is_pair_one:                                           # если пара
            amount_value = amount_value_pair                        # старшинство - по паре
            if is_pair_two:                                         # + вторая пара
                combo_number = 2                                    # комбинация = 'two_pairs' = 2
            else:                                                   # второй пары нет
                combo_number = 1                                    # комбинация = 'one_pair' = 1
        else:
            amount_value = amount_value_one                         # старшинство - по карте
            combo_number = 0                                        # комбинация = 'нет' = 0
        return combo_number, amount_value, amount_minor             # возвращаем: номер комбинации, старшинство в комбинации, старшинство младшей пары
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def mark_suit_cards_alt(cardset,suit_numb):                     # маркируем карты в мастях - передаем кардсет
        cardset_tmp = cardset[:]                                    # копируем кардсет, упражняемся с ним, не трогаем основной
        cardset_tmp.sort(cmp,card_value_alt_as_max)                 # сортируем список от 2
        j = n_cards-1                                               # счетчик = количество карт -1
        k = 0                                                       # признак достаточности
        while j >= 0:                                                # перебираем карты со старшей
            if cardset_tmp[j].suit == suit_numb:                    # если номер масти карты = номер масти
                cardset_tmp[j].in_combo = True                      # карта в комбинации
                k += 1                                              # к признаку достаточности +1
                if k == 5:                                          # насчитали 5 карт
                    break                                           # перебор можно закончить
            j -= 1                                                  # уменьшаем счетчик
        return cardset_tmp                                          # возвращаем набор карт
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def mark_sequence_cards_alt(cardset, seq_value):                # маркируем карты в последовательности - передаем кардсет, старшую карту
        cardset_tmp = cardset[:]                                    # копируем кардсет, упражняемся с ним, не трогаем основной
        if seq_value == 14:                                         # если туз в последовательности - старший
            cardset_tmp.sort(cmp,card_value_alt_as_max)             # сортируем список от 2
        else:                                                       # если старший - НЕ туз
            cardset_tmp.sort(cmp,card_value_alt_as_min)             # сортируем список от 1
        j = n_cards-1                                               # счетчик = количество карт -1
        k = 0                                                       # признак достаточности
        val = seq_value                                             # ожидаемое значение очков = максимальному
        while j >= 0:                                                # перебираем карты со старшей
            if card_value_alt_as_max(cardset_tmp[j]) == val or card_value_alt_as_min(cardset_tmp[j]) == val:  # значение очередной карты = ожидаемому
                cardset_tmp[j].in_combo = True                      # карта в комбинации
                k += 1                                              # к признаку достаточности +1
                val -=1                                             # уменьшаем ожидаемое значение
            if k == 5:                                              # если насчитали 5 карт
                break                                               # перебор можно закончить
            j -= 1                                                  # уменьшаем счетчик
        return cardset_tmp                                          # возвращаем набор карт
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def mark_amount_cards_alt(cardset, combo, value, minor):        # маркируем карты по количеству - передаем кардсет, комбинацию, старшую карту, младшую пару
        cardset_tmp = cardset[:]                                    # копируем кардсет, упражняемся с ним, не трогаем основной
        cardset_tmp.sort(cmp,card_value_alt_as_max)                 # сортируем список от 2
        j = n_cards-1                                               # счетчик = количество карт -1
        k = 0                                                       # признак достаточности
        if combo == 1:                                              # если пара
            m = 2                                                   # количество для сравнения
        elif combo == 3:                                            # если тройка
            m = 3                                                   # количество для сравнения
        elif combo in [2,7]:                                        # если две пары или покер
            m = 4                                                   # количество для сравнения
        elif combo == 6:                                            # если фулл-хаус
            m = 5                                                   # количество для сравнения
        while j >= 0:                                                # перебираем карты со старшей
            if combo == 0:                                          # если одна карта
                cardset_tmp[j].in_combo = True                      # её и маркируем
                break                                               # и прерываем цикл
            elif combo in [7,3,1]:                                  # если простая последовательность
                if card_value_alt_as_max(cardset_tmp[j]) == value:  # если количество очков карты совпадает с максимальным
                    cardset_tmp[j].in_combo = True                  # карта в комбинации
                    k += 1                                          # к признаку достаточности +1
                if k == m:                                          # если насчитали нужное количество карт
                    break                                           # перебор можно закончить
            elif combo == 2:                                        # если две пары
                if card_value_alt_as_max(cardset_tmp[j]) == value:  # если количество очков карты совпадает с максимальным
                    cardset_tmp[j].in_combo = True                  # карта в комбинации
                    k += 1                                          # к признаку достаточности +1
                if k == 2:                                          # если насчитали две карты
                    i = j                                           # устанавливаем счетчик - по последней карте старшей пары
                    while i >= 0:                                    # перебираем карты со старшей
                        if card_value_alt_as_max(cardset_tmp[i]) == minor:  # если количество очков карты совпадает с минорной парой
                            cardset_tmp[i].in_combo = True          # карта в комбинации
                            k += 1                                  # к признаку достаточности +1
                        if k == m:                                  # если насчитали нужное количество карт
                            break                                   # перебор можно закончить
                        i -= 1                                      # уменьшаем счетчик
            elif combo == 6:                                        # если 3+2
                if card_value_alt_as_max(cardset_tmp[j]) == value:  # если количество очков карты совпадает с максимальным
                    cardset_tmp[j].in_combo = True                  # карта в комбинации
                    k += 1                                          # к признаку достаточности +1
                if k == 3:                                          # если насчитали три карты
                    i = n_cards-1                                   # устанавливаем счетчик по максимуму (перебор по новой)
                    while i >= 0:                                    # перебираем карты со старшей
                        if card_value_alt_as_max(cardset_tmp[i]) == minor:  # если количество очков карты совпадает с минорной парой
                            cardset_tmp[i].in_combo = True          # карта в комбинации
                            k += 1                                  # к признаку достаточности +1
                        if k == m:                                  # если насчитали нужное количество карт
                            break                                   # перебор можно закончить
                        i -= 1                                      # уменьшаем счетчик
            j -= 1                                                  # уменьшаем счетчик
        return cardset_tmp                                          # возвращаем набор карт
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def what_category_alt(cardset): # пытаемся определить, что же у нас на руках, цифры
        global cards_state
        cardset_tmp = cardset[:] # копируем кардсет, упражняемся с ним, не трогаем основной 
    # .............................................
        combo_suit = False                                                              # нет 5 карт в масти
        value_suit = 0                                                                  # нет старшей карты в последовательности
        name_suit = None                                                                # нет масти в последовательности
        combo_sequence = False                                                          # нет 5 карт в последовательности
        value_sequence = 0                                                              # нет старшей карты в последовательности
        combo_amount = 0                                                                # нет комбинаций по достоинству ( = одна карта)
        value_amount = 0                                                                # нет старшей карты по достоинству
        combo_result = 0                                                                # нет номера комбинации в итоге ( = одна карта)
        value_result = 0                                                                # нет старшей карты комбинации в итоге
        poker_hand = None                                                               # нет комбинации [№ комбинации, значение старшей карты] 
        straight_flush = False                                                          # нет стрит-флеша
    # .............................................
        number_suit, value_suit = what_suit_cards_alt(cardset_tmp)                      # вызов функции подсчета карт по мастям
        if number_suit != None:                                                         # если определено имя масти
            combo_suit = True                                                           # 5 карт в масти есть
    # .............................................
        combo_sequence, value_sequence = what_sequence_cards_alt(cardset_tmp)           # вызов функций проверки последовательностей, туз = 1 / 14 (перебор внутри)

    # .............................................
        combo_amount, value_amount, minor_amount = what_amount_cards_alt(cardset_tmp)   # вызов функций подсчета карт по достоинству
        
    # .............................................
    # что же мы таки имеем
        if combo_suit and combo_sequence:                                               # собрали масть и 5 по порядку = стрит-флеш - а вот вам дуля - на 6/7 картах могут пересечься комбинации 
            straight_flush = really_straight_flush_alt(cardset_tmp, number_suit)        # назначаем дополнительную проверку (Кардсет, № масти)
            if not straight_flush:                                                      # если нам показалось, а на самом деле нет стрит-флеша
                combo_result = 5                                                        # это простой флеш 
                value_result = value_suit                                               # старшая карта - по старшей в масти
            else:                                                                       # если таки да
                value_result = value_sequence                                           # старшая карта - по старшей в последовательности
                if value_sequence == 14:                                                # если еще и туз - старший
                    combo_result = 9                                                    # Роял-флеш
                else:                                                                   # если не туз
                    combo_result = 8                                                    # стрит-флеш
        elif combo_amount > 5 and combo_result < 8:                                     # если покер (4) или фулл-хауз (3+2)  и не стрит-флеш
            value_result = value_amount                                                 # старшая карта - по старшей в комбинации
            combo_result = combo_amount                                                 # комбинация - по количеству карт    
        elif combo_suit and not combo_sequence and combo_result < 6:                    # собрали масть без последовательности и нет комбинации старше 
            value_result = value_suit                                                   # старшая карта - по старшей в масти
            combo_result = 5                                                            # флеш 
        elif not combo_suit and combo_sequence and combo_result < 6:                    # собрали последовательность без масти и нет комбинации старше 
            value_result = value_sequence                                               # старшая карта - по старшей в последовательности
            combo_result = 4                                                            # стрит
        elif combo_result < 4:                                                          # ничего старше не собрали
            value_result = value_amount                                                 # старшая карта - по старшей в комбинации
            combo_result = combo_amount                                                 # комбинация - по количеству карт
            
        poker_hand = [combo_result, value_result, number_suit, minor_amount]            # в руке: [комбинация, старшая карта, масть, младшая пара]
    # .............................................
        for i in range(0,n_cards):
            cardset[i].in_combo = False                                                 # для начала сбасываем принадлежность к комбинации
    # определяем, какие карты входят в комбинацию
        if combo_result in [9,8,5]:                                                     # если флеши
            cardset_suit = mark_suit_cards_alt(cardset,number_suit)                     # вызываем маркировку флешей, передаём карты и масть флешей
        elif combo_result == 4:                                                         # если стрит
            cardset_sequence = mark_sequence_cards_alt(cardset, value_sequence)         # вызываем маркировку стритов, передаём карты и старшую карту
        else:                                                                           # если количество карт
            cardset_amount = mark_amount_cards_alt(cardset, combo_result, value_result, minor_amount) # вызываем маркировку по количеству карт, передаём карты, комбинацию, старшинство, младшую пару
    # .............................................
    # обработка результата
        if cards_state == "results":
            for i in range(0,n_cards):                          # для индекса от 0 до 7 (кол-во карт в сете)
                cardset[i].interesting = False                  # карты не интересны
            for i in range(0,n_cards):                          # для индекса от 0 до 7 (кол-во карт в сете)
                if cardset[i].in_combo == True:                 # если карта в комбинации
                    cardset[i].interesting = True               # карта нам интересна
    # .............................................
        return poker_hand
        
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def really_straight_flush_alt(cardset, number_suit):                                # А не врёшь, что стрит-флеш (карсет, N масти)
        result = False                                                                  # стрит-флеша нет
        int_cardset = []                                                                # сюда отбираем карты
    # .............................................
        for i in range (0,len(cardset)):                                                # перебираем переданные карты
            if cardset[i].suit == number_suit:                                          # если масть очередной карты = масти комбинации
                int_cardset.append(cardset[i])                                          # добавляем эту карту в набор
    # .............................................  
        if len(int_cardset) >= 5:                                                       # если набрали 5 карт и больше
            for k in [0,1]:                                                             # проверяем на минимум и максимум
                val_j = 0                                                               # количество очков текущей карты в переборе
                val_prev = 0                                                            # количество очков предыдущей карты в переборе 
                len_seq_run = 0                                                         # количество карт в возможных последовательностях на проходах
                len_seq_max = 0                                                         # длина максимальной последовательности
                if k == 0:                                                              # в зависимости от значения счетчика
                    int_cardset.sort(cmp,card_value_alt_as_max)                         # сортируем список от 2 (туз старший)
                else:
                    int_cardset.sort(cmp,card_value_alt_as_min)                         # или сортируем список от 1 (туз младший)
                int_cardset.reverse()                                                   # и "переворачиваем" его: [0] - старшая карта
                for j in range (0,len(int_cardset)):                                    # перебираем отобранные карты
                    if k == 0:                                                          # в зависимости от значения счетчика
                        val_j = card_value_alt_as_max(int_cardset[j])                   # читаем значение очередной карты - туз старший
                    else:
                        val_j = card_value_alt_as_min(int_cardset[j])                   # читаем значение очередной карты - туз младший
                    if j == 0:                                                          # на первом проходе
                        len_seq_run = 1                                                 # длину текущей последовательности принимаем = 1, карты не сравниваем - не с чем
                    else:                                                               # на следующих проходах
                        if val_j == (val_prev-1):                                       # если очередная карта в последовательности
                            len_seq_run += 1                                            # длину текущей последовательности увеличиваем на 1
                            if len_seq_run > len_seq_max:                               # если текущая последовательность больше максимальной
                                len_seq_max = len_seq_run                               # максимальную последовательность принимаем по текущей
                        elif val_j == val_prev:                                         # если карты равны
                            pass                                                        # карту пропускаем, последовательность не сбрасываем
                        elif val_j < (val_prev-1):                                      # если очередная карта не в последовательности
                            len_seq_run = 1                                             # длину текущей последовательности принимаем = 1
                    val_prev = val_j                                                    # значение карты для сравнения принимаем: значение текущей карты
                if len_seq_max >= 5:                                                    # если набрали последовательность в 5 карт или больше на каком-то проходе
                    result = True                                                       # таки это стрит-флеш
    # .............................................
        return result

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def name_of_poker_hands_alt(cardset): # называем покерную комбинацию словами
        cardset_tmp = cardset[:] # копируем кардсет, упражняемся с ним, не трогаем основной 
    # .............................................
        name_of_combo = ["старшая карта","пара","две пары","тройка","стрит","флеш","фулл-хаус","покер","стрит-флеш","роял-флеш"]    # комбинации
        name_of_card = ["","туз","двойка","тройка","четвёрка","пятёрка","шестёрка","семёрка","восьмёрка","девятка","десятка","валет","дама","король","туз"]
        name_of_cards = ["","","двойки","тройки","четвёрки","пятёрки","шестёрки","семёрки","восьмёрки","девятки","десятки","вальты","дамы","короли","тузы"]
        name_of_suit = ["Дваче","СССР","Унылок","ЮВАО"]     # масти                                                                           
    # .............................................
        poker_hand = None                                   # пустая комбинация
        combo_name = None                                   # имени комбинации нет
        value_name = None                                   # имени старшей карты нет
        suit_name = None                                    # имени масти нет
        combo_in_hand = None                                # В руке (строка): пусто
    # .............................................
        poker_hand = what_category_alt(cardset_tmp)
        combo_name = name_of_combo[poker_hand[0]]           # получаем имя комбинации
        if poker_hand[0] in [0,4,5,8]:                      # если старшая карта или масти, кроме рояля, или стрит
            value_name = name_of_card[poker_hand[1]]        # получаем имя карты - единственное число
        else:                                               # если любая комбинация, кроме старшей карты
            value_name = name_of_cards[poker_hand[1]]       # получаем имя карт - множественное число
        if poker_hand[0] in [5,8,9]:                        # если собраны масти
            suit_name = name_of_suit[poker_hand[2]]         # получаем имя масти
    # .............................................
        if poker_hand[0] == 0:                                                                  # если старшая карта
            combo_in_hand = "%s :%s" % (combo_name, value_name)                                 # строка для старшей карты
        elif poker_hand[0] in [5,8]:                                                            # если масти, кроме рояля
            combo_in_hand = "%s %s, старшая карта: %s" % (combo_name, suit_name, value_name)    # строка для мастей
        elif poker_hand[0] == 9:                                                                # собрали роял-флеш
            combo_in_hand = "%s %s" % (combo_name, suit_name)                                   # собрали роял-флеш
        elif poker_hand[0] == 4:                                                                # собрали стрит
            combo_in_hand = "%s , старшая карта: %s" % (combo_name, value_name)                 # строка для стрита
        else:                                                                                   # если ничего особенного
            combo_in_hand = "%s , старшие карты: %s" % (combo_name, value_name)                 # строка для прочих случаев
    # .............................................
        return combo_in_hand, poker_hand

# =========================================================================================================================
# Сравнение сетов карт, победа/поражение
# а) сравниваем комбинации - победа/поражение/разница в номерах
# б) если комбинации одинаковые - сравниваем старшие карты - победа\поражение
# в) если комбинации и старшие карты одинаковы - сравниваем младшую пару - победа/поражение
# г) если все одинаково - ничья

    def count_score_alt():
        poker_hand_my = what_category_alt(cards_my)                         # посмотрели, что у нас на руках
        poker_hand_rival = what_category_alt(cards_rival)                   # посмотрели, что на руках у соперника
        
        if poker_hand_my[0] > poker_hand_rival[0]:                          # если моя комбинация старше
            return 'win'                                                    # я выиграл
        elif poker_hand_my[0] < poker_hand_rival[0]:                        # если моя комбинация младше
            return 'fail'                                                   # соперник выиграл
        else:                                                               # комбинации равны
            if poker_hand_my[1] > poker_hand_rival[1]:                      # если моя старшая карта больше
                return 'win'                                                # я выиграл
            elif poker_hand_my[1] < poker_hand_rival[1]:                    # если моя старшая карта меньше
                return 'fail'                                               # соперник выиграл
            else:                                                           # и старшие карты равны
                if poker_hand_my[3] > poker_hand_rival[3]:                  # если моя младшая пара больше
                    return 'win'                                            # я выиграл
                elif poker_hand_my[3] < poker_hand_rival[3]:                # если моя младшая пара меньше
                    return 'fail'                                           # соперник выиграл
                else:                                                       # если и это одинаково
                    return 'draw'                                           # похоже, ничья

# =========================================================================================================================

init 3 python:                              # начинаем на шаг позже оригинала
    if  not config_session:
# ============================================================================================================================================== 
        def generate_cards_alt(bg,dialogs): # генерация карт, вызываем из кода, передавая основу и диалоги
            global cards_bg                 # подложка, далее присваиваем bg, переданное из кода
            global game_interuptions        # прерываение игры - далее присваиваем диалоги
            global cards_my                 # сет моих карт
            global cards_rival              # сет карт соперника
            global cycles_left              # осталось циклов
            global changes_left             # осталось обменов
            global cards_state              # стадия игры
            global result_status            #
            
            cards_bg = bg                   # берем подоснову, переданную из кода
            game_interuptions = dialogs     # присваиваем переданные диалоги
            cycles_left  = n_cycles         # оставщиеся циклы принимаем = 3 (в ините)
            changes_left = n_xchanges       # оставщиеся обмены принимаем = 2 (в ините)
            cards_state = "init"            # Стадия игры = "начало"
            result_status = "in_progress"   #
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
            k = 0 # обнуляем счетчик раздачи?
            cset = [] # пустой сет карт в игре
            while k<2*n_cards: # пока: счетчик < 2 х колво_карт (7 в init'е) = k < 14 - делаем 14 карт (12 в игре)
                name = (renpy.random.randint(1,13),types[renpy.random.randint(0,3)]) # имя = рандом (1..13), рандом из типов, например, имя = '5uvao'
                if  not name in cset: # если такого имени в наборе еще нет
                    cset.append(name) # добавляем в набор игровых карт такое имя
                    k += 1 # увеличиваем счетчик на 1
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
            cards_rival = [] #карты соперника, по началу пусто
            for i in range(0,n_cards): # от 0 до 7 = 7 позиций, старшая не считается, формируем сет карт соперника
                rival = [] # очередная карта соперника
                rival.visible = 'INVISIBLE' # видимость карты соперника - "НЕВИДИМА" должна быть
                rival.name = cset[i] # имя карты соперника - принимаем по индексу из сета карт в игре 0...7 карта
                rival.suit = types.index(rival.name[1])     # номер масти карты - по вхождению масти в список
                
                rival.interesting = False # карта неинтересна
                rival.in_combo = False # карта не в комбинации
                
                rival.hot = False #
                rival.allow = False #
                rival.x = int((screen_width - card_width )/2.0) #
                rival.y = int((screen_height - card_height)/2.0) #
                rival.dy = 0 #
                cards_rival.append(rival) # добавляем очередную карту в сет карт соперника
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
            cards_my    = [] #мои карты, по началу пусто
            for i in range(0,n_cards): # от 0 до 7 = 7 позиций, старшая не ситается, формируем сет своих карт
                my = [] # очередная моя карта
                my.visible = 'VISIBLE' # видимость моей карты - "ВИДИМА" должна быть
                my.name = cset[n_cards+i] # имя моей карты - принимаем по индексу из сета карт в игре 7...14 карта 
                my.suit = types.index(my.name[1])       # номер масти карты - по вхождению масти в список
 
                my.interesting = False #
                my.in_combo = False # карта не в комбинации
                
                my.hot = False #
                my.allow = False #
                my.x = int((screen_width - card_width )/2.0) #
                my.y = int((screen_height - card_height)/2.0) #
                my.dy = 0 #
                cards_my.append(my) # добавляем очередную карту в сет своих карт
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
            if not  CARD_GAME_WITH_EXCHANGE: # если (False) играем 6 карт, левые карты - "пустые"; если (True) - играем 7 карт 
                cards_rival[0].name = name_of_none # "нулевая" карта в сете соперника - пустое изображение
                cards_my[0].name = name_of_none # "нулевая" карта в своем сете - пустое изображение
            
            if cards_state == "init":
                deal_cards = {"1":"sound/sfx/cardgame/new/deal_card_1.ogg","2":"sound/sfx/cardgame/new/deal_card_2.ogg","3":"sound/sfx/cardgame/new/deal_card_3.ogg","4":"sound/sfx/cardgame/new/deal_card_4.ogg" }
                from random import randint
                deal_card = deal_cards[str(randint(1,4))]
                renpy.music.play(deal_card, channel="sound")
                
# ==============================================================================================================================================       
#                                                        ИГРА В КАРТЫ. Покер. Новые соперники
# =====================================================================================================================================================
label cards_gameloop_wise_alt:                                           
    python:
        renpy.block_rollback()
        renpy.scene('underlay')
        renpy.scene('master') 
#------------------------------------------------------------------------------------
        if cards_state == "init":                                               # если стадия "начало"
            show_cards_alt()                                                    # показываем карты
            rival.sort_cards_on_usefulness()                                    # соперник оценивает свою комбинацию
            renpy.pause(1)
            if alt_whose_first_move == 'rival':                                 # если первым ходит соперник
                new_state = "rival_select"                                      # следующая стадия = "соперник выбирает"
            elif alt_whose_first_move == 'player':                              # если первым ходит игрок
                rival.allow_to_take()                                           # установка разрешений на выбор карт у соперника
                new_state = "me_select_1"                                       # следующая стадия = "игрок выбирает"
#------------------------------------------------------------------------------------
        if cards_state == "rival_select":                                       # если стадия "соперник выбирает"
            rival.sort_cards_on_usefulness()                                    # соперник оценивает свои карты
            interuption_region_alt()                                            # прерывание - если есть диалог => идем по метке
            my_card = rival.what_card_choose()                                  # что же мы будем тянуть у Семёна?
            
            rival.last_selected_card = my_card                                  # запоминаем последнюю выбранную карту (под слив)
            
            for i in range(0,n_cards):                                          # перебираем карты
                cards_my[i].interesting = False                                 # сброс маркировки с карт игрока
                cards_rival[i].interesting = False                              # сброс маркировки с карт соперника
            cards_my[my_card].interesting = True                                # маркируем карту игрока, выбранную соперником
            show_cards_alt()                                                    # показываем карты
            renpy.pause(1)
            if  not rival.allow_to_defend():                                    # если нет разрешения на защиту (актуально для Ульяны в классике)
                rival.player_conceal_card = True                                # Семён карту сбросил без борьбы
                new_state = "rival_get"                                         # следующая стадия = "соперник забирает карту"
            else:                                                               # если разрешение на защиту есть
                new_state = "me_defend_1"                                       # следующая стадия = "защита игрока _ 1"
#------------------------------------------------------------------------------------
        if cards_state == "me_defend_1":                                        # Семён защищается - 1
            interuption_region_alt()                                            # Обработка прерывания
            answer = cards_interact_alt()                                       # действие - интерактив.
            if  answer == "end_of_turn":                                        # если нажата кнопка "конец тура"
                rival.player_conceal_card = True                                # Семён карту сбросил без борьбы
                new_state = "rival_get"                                         # соперник получает карту
            else:
                if rival.want_to_defend():                                      # если НЕ Ульяна
                    rival.player_conceal_card = False                           # Семён карту защищал
                else:                                                           # для Ульяны
                    rival.player_conceal_card = True                            # Семён карту сбросил без борьбы
                type,index = answer
                cards_my[index].dy = -40
                prev_answer = index
                new_state = "me_defend_2"
#------------------------------------------------------------------------------------
        if cards_state == "me_defend_2":                                        # Семён защищается - 2
            #interuption_region_alt()                                            # Обработка прерывания - перенесено ниже
            answer = cards_interact_alt()                                       # действие - интерактив.
            cards_my[prev_answer].dy = 0                                        # выдвинутую карту смещаем назад
            if  answer == "end_of_turn":                                        # если нажата кнопка "конец тура"
                interuption_region_alt()                                        # Обработка прерывания
                rival.player_conceal_card = True                                # Семён карту сбросил без борьбы
                new_state = "rival_get"                                         # соперник получает карту
            else:
                if rival.want_to_defend():                                      # если НЕ Ульяна
                    rival.player_conceal_card = False                           # Семён карту защищал
                else:                                                           # для Ульяны
                    rival.player_conceal_card = True                            # Семён карту сбросил без борьбы
                type,index = answer
                if  prev_answer == index:
                    cards_my[prev_answer].dy = 0
                    new_state = "me_defend_1"
                else:
                    move_buttons(cards_my,prev_answer,cards_my,index)               # игрок тасует карты
                    rival.tracked_movement(prev_answer,index)                       # отслеживаем перемещение интересующих нас карт Сэмэна
                    changes_left -= 1
                    interuption_region_alt()                                        # Обработка прерывания
                    if  changes_left == 0:
                        new_state = "rival_get"
                    else:
                        new_state = "rival_select"
#------------------------------------------------------------------------------------
        if cards_state == "rival_get": 
            if  changes_left == 0:
                my_card = rival.pick_my_card_last_think()                           # какую карту забираем у игрока
            for i in range(0,n_cards):
                cards_my[i].interesting = False
                cards_rival[i].interesting = False
            cards_my[my_card].interesting = True
            show_cards_alt()
            renpy.pause(1)
            interuption_region_alt()
            if CARD_GAME_WITH_EXCHANGE:                                             # если игра на 7 картах
                rival_card = rival.give_away_card_think()                           # какую карту отдаём игроку ?
                rival.what_card_we_gave_7(rival_card,my_card)                       # смотрим, ЧТО отдали и КУДА вставили - заносим в соответствующий список
                cards_rival[rival_card].interesting = True
                show_cards_alt()
                renpy.pause(1)
            else:
                for i in range(0,n_cards):
                    if  cards_rival[i].name == name_of_none:
                        rival_card = i
            xchange_cards()                                                         # обменялись картами
            if rival.player_conceal_card:                                           # если Семён карту сбросил
                rival.player_unnecessary_card = rival_card                          # запоминаем её - вернуть ему обратно её
            else:                                                                   # Семён защищал эту карту
                rival.player_accept_card = rival_card                               # запоминаем её - потянется ли за ней?
            if not CARD_GAME_WITH_EXCHANGE:                                         # если НЕ игра на 7 картах
                rival.what_is_pulled_out(my_card)                                   # смотрим, что же мы забрали, вносим корректировку
            show_cards_alt()                                                        # показываем стол
            rival.remember_combo()                                                  # если соперник забирает, сначала запоминает
            rival.sort_cards_on_usefulness()                                        # потом оценивает новую комбинацию
            rival.compare_combo()                                                   # ... и сравнивает комбинации
            if alt_whose_first_move == 'player':                                    # минус цикл на ходе соперника, если игрок начинает
                cycles_left -= 1
            if cycles_left != 0:
                changes_left = n_xchanges
                rival.allow_to_take()
                renpy.pause(1)
                new_state = "me_select_1"
            else:
                new_state = "results"
#------------------------------------------------------------------------------------
        if cards_state == "me_select_1":
            interuption_region_alt()
            if  CARD_GAME_WITH_EXCHANGE:
                answer = cards_interact_alt()
                type,index = answer
                cards_my[index].dy = -40
                my_card = index
                rival.what_we_trying_foist_7 = index                        # номер карты, которую нам хочет всучить Семён на 7 картах
            else:
                rival.what_we_trying_foist_7 = 7                            # "обнуляем" отдаваемую карту при игре на 7-ми картах
                for i in range(0,n_cards):
                    if  cards_my[i].name == name_of_none:
                        my_card = i
            new_state = "me_select_2"
#------------------------------------------------------------------------------------
        if cards_state == "me_select_2":
            interuption_region_alt()
            answer = cards_interact_alt()
            type,index = answer
            if type == "my":
                cards_my[index].dy = 0
                new_state = "me_select_1"
            else:
                rival_card = index
                for i in range(0,n_cards):
                    cards_rival[i].interesting = False
                    cards_my[i].interesting = False
                cards_rival[index].interesting = True
                new_state = "rival_defend"
#------------------------------------------------------------------------------------
        if cards_state == "rival_defend":
            show_cards_alt()                                                    # показали карты
            renpy.pause(1)
            interuption_region_alt()                                            # обработали прерывания
            rival.to_give_just_card()                                           # подумали - а может, сразу отдать
            if  changes_left == 0:                                              # если обменов не осталось
                rival.do_we_need_this_card()                                    # смотрим, что заберут и проверяем, не пригодилась бы эта карта
                new_state = "me_get"
            else:
                if  not rival.want_to_defend():                                 # если игрок не готов к отдаче (Ульяна)
                    changes_left == 0
                    rival.player_conceal_card = True                            # Семён карту сбросил без борьбы
                    new_state = "me_get"
                else:
                    i,j = rival.what_to_xchange_think()                         # решаем, какие карты будем менять
                    changes_left -= 1                                           # уменьшаем число доступных обменов
                    move_buttons(cards_rival,i,cards_rival,j)                   # меняем свою карту
                    rival.sort_cards_on_usefulness()                            # после обмена карт - ещё раз смотрим, где нужные
                    tmp_interest = cards_rival[i].interesting
                    cards_rival[i].interesting = cards_rival[j].interesting
                    cards_rival[j].interesting = tmp_interest
                    new_state = "me_select_2"
#------------------------------------------------------------------------------------
        if cards_state == "me_get":
            interuption_region_alt()
            cards_my[my_card].dy = 0
            rival.remember_combo()                                      # когда игрок должен забрать карту, перед самым обменом карт, соперник запоминает, что было
            if CARD_GAME_WITH_EXCHANGE:                                 # ЕСЛИ играли на 7-ми картах
                rival.player_unnecessary_card = rival_card              # Эту карту нам отдал Семён - она ему, походу, не нужна
                rival.what_is_pulled_out(rival.what_we_trying_foist_7)  # контролируем стеки карт, убираем неактуальные
            rival.inserted_player_card = my_card                        # Семён нашу карту забрал в это место
            
            if rival.playstyle == 'gamble':                             # если рискуем
                rival.remember_cards()                                  # запоминаем недокомбинации, если были
            xchange_cards()                                             # обменялись картами
            rival.sort_cards_on_usefulness()                            # потом оцениваем новую комбинацию
            rival.compare_combo()                                       # ... и сравниваем комбинации
            rival.what_at_us_took(rival_card)                           # а что он у нас забрал, собственно ?
            if alt_whose_first_move == 'rival':                         # минус цикл на своём ходе - если соперник начинает
                cycles_left -= 1
            if  cycles_left != 0:
                changes_left = n_xchanges
                new_state = "rival_select"
            else:
                new_state = "results"
#------------------------------------------------------------------------------------
        if cards_state == "results":
            interuption_region_alt()
            show_cards_alt()
            renpy.pause(2)
            sort_cards_alt_upshot()                                         # сортируем карты на итог
            if not VISIBLE:
                VISIBLE = True
            for i in range(0,n_cards):
                cards_rival[i].visible = 'VISIBLE'
                cards_my[i].visible = 'VISIBLE'
            alt_hint_poker = True
            result_status = count_score_alt()                               # вызываем подсчет очков
            answer = "ignore"
            while answer=="ignore":
                show_cards_alt()
                answer = ui.interact()
            new_state = result_status
#------------------------------------------------------------------------------------
        if cards_state in ["win","draw","fail"]:
            alt_hint_poker = False                                          # "закрываем" подсказку
            interuption_region_alt()
            renpy.error("out of end-of-card-game interruption")
        cards_state = new_state                                             # меняем стадию игры на новую
        alt_name_my_poker_hand, alt_my_poker_hand = name_of_poker_hands_alt(cards_my)
        alt_name_rival_poker_hand, alt_rival_poker_hand = name_of_poker_hands_alt(cards_rival)
#------------------------------------------------------------------------------------
    jump cards_gameloop_wise_alt