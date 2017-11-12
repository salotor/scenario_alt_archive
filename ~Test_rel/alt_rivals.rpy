init -50 python:
    """
    Стили игры:
    'defense' - защищаемся (если есть хоть что-то на руках - защищаем эту комбинацию)
    'gamble' - рискуем (если "недофлеш", "недострит" - 4 из 5 - и есть пара или 2+2 - допускаем разбитие комбинации)
    'succumb' - играем в поддавки (специальный слив партии) - "защита" наоборот
    'foolplay' - валяем дурака(анализ проводится, но ходы - 100% рандом)
    для вышеперечисленного возможен рандом на "ошибку" ('foolplay') ; вероятность меняется:
    5 - рандом исключен,
    4, 3, 2, 1 - соответственно 20, 40, 60, 80 % вероятность ошибки.
    """
    import random
    
    class CardGameRivalWise_alt:                                                # УМНЫЙ (ну, почти) СОПЕРНИК

        def __init__(self, avatar, name, behavior = 'defense', skill = 5):      # свойства нашего соперника (аватар и имя передаются при вызове, поведение и "навык" МОЖНО передать при вызове)
            self.name = name                                                    # имя - передаём
            self.mood = 0                                                       # режим аватара - присваиваем по ходу дела
            self.avatar = avatar                                                # аватарку передаём
    # ---------------------------------------------------------------------
            self.combo_in_hand = None                                           # комбинация в руке
            self.combo_was_before = None                                        # комбинация, что была раньше
            self.as_changed_combo = 'unclear'                                   # как комбинация изменилась (никак, хуже, лучше) ('does', 'worse', 'better')
            if behavior in ['defense','gamble','succumb','foolplay']:           # если стиль игры из предопределённых
                self.playstyle = behavior                                       # поведение в игре - по переданному
            else:                                                               # Если же стиль не опознали
                self.playstyle = 'defense'                                      # поведение в игре - принимаем защитное
            if skill > 5:                                                       # если переданный "навык игры" больше 5
                self.mistake_chance = 5                                         # принимаем шанс ошибиться 0
            elif skill < 1:                                                     # если переданный "навык игры" меньше 1
                self.mistake_chance = 1                                         # принимаем шанс ошибиться 80%
            else:                                                               # если от 1 до 5
                self.mistake_chance = skill                                     # шанс ошибиться - по переданному
            self.make_mistakes = False                                          # при очередном ходе ошибаемся ?
            self.yourself_need_cards = []                                       # нужные нам карты - карты входят в актуальную комбинацию
            self.would_not_want_give = []                                       # карты, которые не хотелось бы отдавать
            self.can_give_in_a_pinch = []                                       # карты, которые можно отдать в крайнем случае
            self.waste_cards = []                                               # мусор (не входят в актуальную комбинацию)
            self.this_give_definitely_succumb = []                              # список карт, которые нужно отдать, если 'succumb'
            self.its_urgent_shove = []                                          # это срочно спихнуть (первый приоритет на обмен/отдачу)
            self.these_proposed_to_take = []                                    # эти карты предлагать на обмен/отдачу
            self.pick_this_cards_urgently = []                                  # забрать эти карты у Семёна СРОЧНО
            self.pick_this_cards_afterwards = []                                # забрать эти карты у Семёна ПОТОМ
            self.never_touch_cards = []                                         # а эти карты у Семёна не трогать
            self.pulled_player_card = 7                                         # за какой картой потянулся Семён (7 - такой в игре нет, для проверки)
            self.what_we_trying_foist_7 = 7                                     # что нам хочет отдать Сеня на 7 картах
            self.dragged_player_card = 7                                        # какую карту вытащил Семён
            self.degree_usefulness_card = 0                                     # степень "полезности" вытащенной карты
            self.inserted_player_card = 7                                       # в каком месте у Семёна наша карта
            self.table_card_points = []                                         # таблица очков карт на руках
            self.table_card_suit = []                                           # потенциальный флеш
            self.table_card_sequence_min = []                                   # потенциальный стрит младший/минимальный (от пятёрки)
            self.table_card_sequence_max = []                                   # потенциальный стрит старший/максимальный
            self.table_card_possible_combo = []                                 # возможная комбинация (флеш, стрит)
            self.player_conceal_card = False                                    # "прячет" ли Семён эту карту
            self.player_unnecessary_card = 7                                    # эта карта у нас Семёну, вероятно, не нужна (отдал сразу или подсунул на 7-ми картах)
            self.player_accept_card = 7                                         # эта карта у нас Семёну, вероятно, нужна (защищал её)
            self.last_selected_card = 7                                         # последняя выбранная карта (используется в режиме слива)
            
    # МЕТОДЫ НОВЫЕ ========================================================================================
        def what_we_have(self):                                                 # что же мы таки имеем на руках
            self.combo_in_hand = what_category_alt(cards_rival)                 # вызываем определение своей комбинации
            self.choice_need_cards()                                            # получаем индексы нужных нам карт
            self.choice_waste_cards()                                           # а также - индексы ненужных
            self.what_cards_have()                                              # и получаем значения очков
# .................................
        def check_for_four_suit(self):                                          # проверим на ЧЕТЫРЕ в мастях
            global types                                                        # понадобится список мастей
            self.table_card_suit = []                                           # очищаем таблицу
        #-------------------------------------------
            total_2ch = 0                                                       # количество карт масти 2ch
            total_ussr = 0                                                      # количество карт масти ussr
            total_utan = 0                                                      # количество карт масти utan
            total_uvao = 0                                                      # количество карт масти uvao
            suit_max = 0                                                        # количество карт максимальной масти
            suit = None                                                         # максимальная масть
        #-------------------------------------------
            for i in range(0,n_cards):                                          # перебираем свои карты
                if cards_rival[i].name[1] == "2ch":                             # если карта ЭТОЙ масти
                    total_2ch += 1                                              # увеличиваем счетчик ЭТОЙ масти на 1
                elif cards_rival[i].name[1] == "ussr":
                    total_ussr += 1
                elif cards_rival[i].name[1] == "utan":
                    total_utan += 1
                elif cards_rival[i].name[1] == "uvao":
                    total_uvao += 1
        #-------------------------------------------
            suit_max = max(total_2ch,total_ussr,total_utan,total_uvao)          # выясняем максимум карт одной масти
        #-------------------------------------------
            if suit_max >= 4:                                                   # если максимальное количество карт в масти 4 или больше
                if suit_max == total_2ch:                                       # если max = ЭТОЙ масти
                    suit = types[0]                                             # масть = из списка мастей [номер в нём] - ["2ch","ussr","utan","uvao"]
                elif suit_max == total_ussr:
                    suit = types[1]
                elif suit_max == total_utan:
                    suit = types[2]
                elif suit_max == total_uvao:
                    suit = types[3]
                for j in range(0,n_cards):                                      # ещё раз перебираем карты
                    if cards_rival[j].name[1] == suit:                          # если очередная карта нужной масти
                        self.table_card_suit.append(j)                          # добавляем её номер в список мастей
# .................................
        def check_for_four_sequence(self):                                      # проверим на ЧЕТЫРЕ подряд
            cardset_tmp = cards_rival[:]                                        # копируем кардсет, упражняемся с ним, не трогаем основной
            self.table_card_sequence_min = []                                   # очищаем таблицы
            self.table_card_sequence_max = []                                   # очищаем таблицы
            values_max = []                                                     # возможная максимальная последовательнось (туз старший)
            values_min = []                                                     # возможная минимальная последовательнось (туз младший)
            values_max_1 = []                                                   # очищаем таблицу первой возможной последовательности
            values_max_2 = []                                                   # очищаем таблицу второй возможной последовательности
            values_max_3 = []                                                   # очищаем таблицу третьей возможной последовательности
            values_max_com_12 = []                                              # очищаем таблицу первой последовательности на 2-х
            values_max_com_23 = []                                              # очищаем таблицу второй последовательности на 2-х
            triplex_seq = 0                                                     # сколько последовательностей по три
        #------------------------------------------- 
            len_seq_max = 0                                                     # количество карт в максимальной последовательности
            seq_value_max = 0                                                   # старшая карта в последовательности
            len_seq_1 = 0                                                       # количество карт в первой последовательности
            seq_value_1 = 0                                                     # старшая карта в первой последовательности
            len_seq_2 = 0                                                       # количество карт во второй последовательности
            seq_value_2 = 0                                                     # старшая карта во второй последовательности
            len_seq_3 = 0                                                       # количество карт в третьей последовательности
            seq_value_3 = 0                                                     # старшая карта в третьей последовательности
        #-------------------------------------------
            cardset_tmp.sort(cmp,card_value_alt_as_max)                         # сортируем список от 2
            val_i = 0                                                           # количество очков текущей карты в переборе
            val_prev = 0                                                        # количество очков предыдущей карты в переборе
            run_number = 0                                                      # номер результативного прохода
            len_seq_run = 0                                                     # количество карт в возможных последовательностях на проходах
            for i in range(0,n_cards):                                          # перебираем карты
                val_i = card_value_alt_as_max(cardset_tmp[i])                   # читаем значение очередной карты; туз = 14
                if val_i != 0:                                                  # если карта нормальная
                    run_number +=1                                              # увеличиваем счетчих проходов (отсеиваем пустую карту)
                    if run_number == 1:                                         # на первом проходе
                        len_seq_run = 1                                         # длину текущей последовательности принимаем = 1
                        len_seq_max = 1                                         # длину максимальной последовательности принимаем = 1
                    else:                                                       # на следующих проходах
                        if val_i == (val_prev + 1):                             # если очередная карта в последовательности
                            len_seq_run += 1                                    # длину текущей последовательности увеличиваем на 1
                            if len_seq_run > len_seq_max:                       # если текущая последовательность больше максимальной
                                len_seq_max = len_seq_run                       # максимальную последовательность принимаем по текущей
                                seq_value_max = val_i                           # старшую карту принимаем по текущей
                        elif val_i == val_prev:                                 # если карты равны
                            pass                                                # карту пропускаем, последовательность не сбрасываем
                        elif val_i > (val_prev + 1):                            # если очередная карта не в последовательности
                            if len_seq_run >= 2:                                # если была набрана последовательность в 2 карты или более - смотрим, что это за последовательность
                                if len_seq_1 == 0:                              #   ... и эта последовательность первая
                                    len_seq_1 = len_seq_run                     # длина первой последовательности = длине текущей последовательности
                                    seq_value_1 = val_prev                      # старшая карта первой последовательности = предыдущей карте
                                elif (len_seq_1 != 0) and (len_seq_2 == 0):     #   ... и эта последовательность вторая
                                    len_seq_2 = len_seq_run                     # длина второй последовательности = длине текущей последовательности
                                    seq_value_2 = val_prev                      # старшая карта второй последовательности = предыдущей карте
                                elif (len_seq_1 != 0) and (len_seq_2 != 0) and (len_seq_3 == 0): #   ... и эта последовательность третья
                                    len_seq_3 = len_seq_run                     # длина третьей последовательности = длине текущей последовательности
                                    seq_value_3 = val_prev                      # старшая карта третьей последовательности = предыдущей карте
                            len_seq_run = 1                                     # длину текущей последовательности принимаем = 1
                    val_prev = val_i                                            # значение карты для сравнения принимаем: значение текущей карты
        #-------------------------------------------
            if len_seq_max >= 4:                                                # если на максимуме набрали последовательность в 4 и более
                values_max = []                                                 # готовим таблицу очков карт
                cardset_tmp.sort(cmp,card_value_alt_as_max)                     # сортируем таблицу (туз = 14)
                cardset_tmp.reverse()                                           # и "переворачиваем" её (старшая - первая)
                val = seq_value_max                                             # ожидаемое значение = значению старшей карты
                for i in range(0,n_cards):                                      # перебираем сортированный сет
                    if card_value_alt_as_max(cardset_tmp[i]) == val:            # значение очередной карты = ожидаемому
                        values_max.append(val)                                  # добавляем такое значение в набор
                        val -=1                                                 # уменьшаем ожидаемое значение
        #------------------------------------------
            if len_seq_max == 3:                                                # если максимальная последовательность = 3 - какая из трёх
                values_max = []                                                 # готовим таблицу очков карт
                if len_seq_1 == 3:                                              # если первая
                    triplex_seq +=1                                             # считаем последовательности по три
                    above_1 = seq_value_1 + 2                                   # возможная доп. карта старше трёх
                    below_1 = seq_value_1 - 4                                   # возможная доп. карта младше трёх
                    if (above_1 in self.table_card_points) or (below_1 in self.table_card_points): # если есть одна из карт по схеме 3+1
                        values_max_1 = [seq_value_1,seq_value_1-1,seq_value_1-2] # вставляем в таблицу три карты последовательности - старшая первая
                        if above_1 in self.table_card_points:                   # если есть старшая карта
                            values_max_1.insert(0,above_1)                      # вставляем её в начало списка
                        if below_1 in self.table_card_points:                   # если есть и младшая карта
                            values_max_1.append(below_1)                        # добавляем её к набору
                if len_seq_2 == 3:                                              # если вторая
                    triplex_seq +=1                                             # считаем последовательности по три
                    above_2 = seq_value_2 + 2                                   # возможная доп. карта старше трёх
                    below_2 = seq_value_2 - 4                                   # возможная доп. карта младше трёх
                    if (above_2 in self.table_card_points) or (below_2 in self.table_card_points): # если есть одна из карт по схеме 3+1
                        values_max_2 = [seq_value_2,seq_value_2-1,seq_value_2-2] # вставляем в таблицу три карты последовательности - старшая первая
                        if above_2 in self.table_card_points:                   # если есть старшая карта
                            values_max_2.insert(0,above_2)                      # вставляем её в начало списка 
                        if below_2 in self.table_card_points:                   # если есть и младшая карта
                            values_max_2.append(below_2)                        # добавляем её к набору
                if len_seq_3 == 3:                                              # если третья
                    triplex_seq +=1                                             # считаем последовательности по три
                    above_3 = seq_value_3 + 2                                   # возможная доп. карта старше трёх
                    below_3 = seq_value_3 - 4                                   # возможная доп. карта младше трёх
                    if (above_3 in self.table_card_points) or (below_3 in self.table_card_points): # если есть одна из карт по схеме 3+1
                        values_max_3 = [seq_value_3,seq_value_3-1,seq_value_3-2] # вставляем в таблицу три карты последовательности - старшая первая
                        if above_3 in self.table_card_points:                   # если есть старшая карта
                            values_max_3.insert(0,above_3)                      # вставляем её в начало списка 
                        if below_3 in self.table_card_points:                   # если есть и младшая карта
                            values_max_3.append(below_3)                        # добавляем её к набору
                if len(values_max_3) !=0:                                       # начинаем с третьей - потенциально старшей
                    values_max = values_max_3[:]                                # добавляем всё оттуда в максимальную последовательность
                    # дальнейшая проверка смысла не имеет - если треться последовательность тройная - первые две могут быть только по две
                else:                                                           # если третья последовательность не тройная
                    if len(values_max_2) !=0:                                   # проверяем вторую последовательность - если не пустая (вторая - тройная, первая тоже может быть тройной)
                        values_max = values_max_2[:]                            # добавляем всё оттуда в максимальную последовательность
                        if len(values_max_1) !=0:                               # проверяем первую последовательность - если не пустая
                            for i in range (0,len(values_max_1)):               # перебираем ёё
                                if values_max_1[i] not in values_max:           # и если в ней найдётся цифра, которой ёще нет в максимальной последовательности
                                    values_max.append(values_max_1[i])          # добавляем её туда.
                    else:                                                       # если и вторая последовательность не тройная
                        if len(values_max_1) !=0:                               # проверяем первую последовательность - если не пустая (может и лишнее, но чтоб не вылетело)
                            values_max = values_max_1[:]                        # добавляем всё оттуда в максимальную последовательность
        #------------------------------------------
            if (len_seq_max == 2) or (triplex_seq == 1):                        # если максимальная последовательность = 2 или одна тройная последовательность, проверяем двойные 
                if len_seq_1 in [2,3]:                                          # если первая последовательность = 2 или 3
                    if len_seq_2 == 2:                                          # если вторая последовательность = 2
                        if seq_value_2 == (seq_value_1+3):                      # если старшая второй последовательности = старшая первой +3
                            values_max_com_12 = [seq_value_2,seq_value_2-1,seq_value_1,seq_value_1-1]     # добавляем числа второй последовательности и два старшие первой
                        if len_seq_3 == 2:                                      # если третья последовательность = 2
                            if seq_value_3 == (seq_value_2+3):                  # если старшая третьей последовательности = старшая второй +3
                                values_max_com_23 = [seq_value_3,seq_value_3-1,seq_value_2,seq_value_2-1]     # добавляем числа третьей последовательности и два старшие второй
                        elif len_seq_3 == 3:                                    # если третья последовательность = 3
                            if seq_value_3 == (seq_value_2+4):                  # если старшая третьей последовательности = старшая второй +4
                                values_max_com_23 = [seq_value_3-1,seq_value_3-2,seq_value_2,seq_value_2-1]     # добавляем два младшие числа третьей последовательности и два старшие второй
                    elif len_seq_2 == 3:                                        # если вторая последовательность = 3
                        if seq_value_2 == (seq_value_1+4):                      # если старшая второй последовательности = старшая первой +4
                            values_max_com_12 = [seq_value_2-1,seq_value_2-2,seq_value_1,seq_value_1-1]     # добавляем 2 младшие числа второй последовательности и два старшие первой
                if len(values_max) == 0:                                        # если максимальной последовательности в тройках не было
                    if len(values_max_com_23) != 0:                             # что-то нашли во 2-3 паре
                        values_max = values_max_com_23[:]                       # добавляем все из этого списка в максимальный
                        if len(values_max_com_12) != 0:                         # и что-то нашли в 1-2 паре
                            for i in range (0,len(values_max_com_12)):          # перебираем эту последовательность
                                if values_max_com_12[i] not in values_max:      # и если такого числа в максимальной нет
                                    values_max.append(values_max_com_12[i])     # добавляем его туда
                    else:                                                       # список по 2-3 паре пустой
                        if len(values_max_com_12) != 0:                         # что-то нашли в 1-2 паре
                            values_max = values_max_com_12[:]                   # добавляем все из этого списка в максимальный
                else:                                                           # если на тройке есть максимальная последовательность уже
                    if len(values_max_com_23) != 0:                             # что-то нашли во 2-3 паре
                        for i in range (0,len(values_max_com_23)):              # перебираем эту последовательность
                            if values_max_com_23[i] not in values_max:          # и если такого числа в максимальной нет
                                values_max.append(values_max_com_23[i])         # добавляем его туда
                    if len(values_max_com_12) != 0:                             # что-то нашли в 1-2 паре
                        for i in range (0,len(values_max_com_12)):              # перебираем эту последовательность
                            if values_max_com_12[i] not in values_max:          # и если такого числа в максимальной нет
                                values_max.append(values_max_com_12[i])         # добавляем его туда
                    values_max.sort()                                           # сортируем максимальную от минимума
                    values_max.reverse()                                        # и "переворачиваем" - от максимума.
        #-------------------------------------------
        # проверка на потенциальный стрит от пятёрки (младший)
            values_min = []                                                     # готовим таблицу очков карт
            for mix in [[2,3,4,14],[2,3,5,14],[2,4,5,14],[3,4,5,14]]:           # проверяем 4-ре возможных сочетания с тузом 
                                                                                # если все очки карт из сочетания входят в списое очков наших карт
                if (mix[0] in self.table_card_points) and (mix[1] in self.table_card_points) and (mix[2] in self.table_card_points) and (mix[3] in self.table_card_points):
                    values_min = mix[:]                                         # принимаем это сочетание, как таблицу очков минимума
                    break                                                       # на том цикл заканчиваем
        #-------------------------------------------
            for i in range(0,n_cards):                                          # перебираем СВОИ КАРТЫ
                if card_value_alt_as_max(cards_rival[i]) in values_max:         # если значение очередной карты в списке максимальных значений
                    self.table_card_sequence_max.append(i)                      # индекс карты добавляем в таблицу

                if card_value_alt_as_min(cards_rival[i]) in values_min:         # если значение очередной карты в списке минимальных значений
                    self.table_card_sequence_min.append(i)                      # индекс карты добавляем в таблицу
# .................................
        def what_cards_have(self):                                              # какие карты у нас на руках (значения очков)
            self.table_card_points = []                                         # обнуляем таблицу на вызове функции
            for i in range(0,n_cards):                                          # перебираем свои карты
                if cards_rival[i].name == name_of_none:                         # если карта пустая
                    val = 99                                                    # очков - 99 (чтобы её не выбрать)
                else:                                                           # если карта нормальная
                    val = card_value_alt_as_max(cards_rival[i])                 # читаем ёе значение (туз старший)
                self.table_card_points.append(int(val))                         # добавляем значение в список
            if self.combo_in_hand[0] < 5:                                       # если меньше флеша
                self.check_for_four_suit()                                      # проверяем на 4 в масти
            else:
                self.table_card_suit = []                                       # убираем недофлеш
                self.table_card_sequence_max = []                               # и недостриты 
                self.table_card_sequence_min = []
            if self.combo_in_hand[0] < 4:                                       # если меньше стрита
                self.check_for_four_sequence()                                  # проверяем на 4 последовательные
            else:
                self.table_card_sequence_max = []                               # убираем недостриты 
                self.table_card_sequence_min = []
# .................................
        def remember_combo(self):                                               # запоминаем комбинацию
            self.combo_was_before = []                                          # создаём пустой список
            if self.combo_in_hand != None:                                      # если получили комбо "на руках"
                self.combo_was_before = self.combo_in_hand[:]                   # запоминаем его
# ................................. 
        def compare_combo(self):                                                # сравниваем комбинации до и после
            if self.combo_in_hand != None and self.combo_was_before != None:    # если определили новую и запомнили старую комбо
                if self.combo_in_hand[0] > self.combo_was_before[0]:            # если новая комбинация старше
                    self.as_changed_combo = 'better'                            # результат - стало лучше
                elif self.combo_in_hand[0] < self.combo_was_before[0]:          # если новая комбинация младше
                    self.as_changed_combo = 'worse'                             # результат - стало хуже
                else:                                                           # если комбинации равного достоинства
                    if self.combo_in_hand[1] > self.combo_was_before[1]:        # если новая старшая карта больше
                        self.as_changed_combo = 'better'                        # результат - стало лучше
                    elif self.combo_in_hand[1] < self.combo_was_before[1]:      # если новая старшая карта меньше
                        self.as_changed_combo = 'worse'                         # результат - стало хуже
                    else:                                                       # если старшие карты одинаковы
                        if self.combo_in_hand[3] > self.combo_was_before[3]:    # если новая младшая пара больше
                            self.as_changed_combo = 'better'                    # результат - стало лучше
                        elif self.combo_in_hand[3] < self.combo_was_before[3]:  # если новая младшая пара меньше
                            self.as_changed_combo = 'worse'                     # результат - стало хуже
                        else:                                                   # если младшие пары одинаковы
                            self.as_changed_combo = 'does'                      # результат - ситуация не поменялась
            else:
                self.as_changed_combo = 'unclear'                               # непонятно: наборов карт не обнаружено
# .................................
        def remember_cards(self):                                                   # запоминаем возможные недокомбинации
            self.table_card_possible_combo = []                                     # возможная комбинация - очищаем
            if self.combo_in_hand[0] < 4:                                           # если меньше стрита на руках
                if len(self.table_card_suit) != 0:                                      # если недофлеш
                    self.table_card_possible_combo = self.table_card_suit[:]            # принимаем его, как возможную комбинацию
                if len(self.table_card_sequence_max) != 0:                              # если что-то есть в большом стрите
                    for i in range(0,len(self.table_card_sequence_max)):                # перебираем его 
                        if self.table_card_sequence_max[i] not in self.table_card_possible_combo: # если такой карты там ещё нет
                            self.table_card_possible_combo.append(self.table_card_sequence_max[i]) # добавляем её туда
                if len(self.table_card_sequence_min) != 0:                              # если что-то есть в малом стрите
                    for i in range(0,len(self.table_card_sequence_min)):                # перебираем его 
                        if self.table_card_sequence_min[i] not in self.table_card_possible_combo: # если такой карты там ещё нет
                            self.table_card_possible_combo.append(self.table_card_sequence_min[i]) # добавляем её туда
                if len(self.table_card_possible_combo) !=0:                             # если список возможных комбинаций не пустой
                    self.table_card_possible_combo.sort()                               # сортируем список
# .................................
        def choice_need_cards(self):                                                        # отбираем карты в комбинации
            self.yourself_need_cards = []                                                   # очищаем список
            for i in range(0,n_cards):                                                      # перебираем свои карты
                if cards_rival[i].in_combo:                                                 # если карта в комбинации карт
                    self.yourself_need_cards.append(i)                                      # добавляем индекс этой карты в сет
# ................................. 
        def choice_waste_cards(self):                                                       # отбираем мусор (не в комбинации)
            self.waste_cards = []                                                           # очищаем список
            for i in range(0,n_cards):                                                      # перебираем свои карты
                if not cards_rival[i].in_combo and cards_rival[i].name != name_of_none:     # если карта НЕ в комбинации карт и она НЕ пустая
                    self.waste_cards.append(i)                                              # добавляем индекс этой карты в сет
# .................................
        def selection_cards_for_defense(self):                                              # отбор карт на защиту
            self.would_not_want_give = self.yourself_need_cards[:]                          # не отдавать - то, что в комбинации
            if len(self.table_card_suit) != 0:                                              # если есть что-то в недофлешах
                for i in range(0,len(self.table_card_suit)):                                # перебираем сет
                    if (self.table_card_suit[i] not in self.can_give_in_a_pinch) and (self.table_card_suit[i] not in self.yourself_need_cards):# такой карты ещё не добавлено и её нет в нужных
                        self.can_give_in_a_pinch.append(self.table_card_suit[i])            # добавляем эту карту
            if len(self.table_card_sequence_max) != 0:                                      # что-то есть в старшем недострите
                for i in range(0,len(self.table_card_sequence_max)):                        # переберём его и
                    if (self.table_card_sequence_max[i] not in self.can_give_in_a_pinch) and (self.table_card_sequence_max[i] not in self.yourself_need_cards):#  карта не добавлена и не нужна
                        self.can_give_in_a_pinch.append(self.table_card_sequence_max[i])    # добавляем эту карту
            if len(self.table_card_sequence_min) != 0:                                      # что-то есть в младшем недострите
                for i in range(0,len(self.table_card_sequence_min)):                        # переберём его и
                    if (self.table_card_sequence_min[i] not in self.can_give_in_a_pinch) and (self.table_card_sequence_min[i] not in self.yourself_need_cards):# карта не добавлена и не нужна
                        self.can_give_in_a_pinch.append(self.table_card_sequence_min[i])    # добавляем эту карту
        # что предлагаем
            for j in range (0, n_cards):                                                    # смотрим, что мы можем предложить из своего
                if cards_rival[j].name != name_of_none:                                     # если карта не пустая
                    if (j not in self.yourself_need_cards) and (j not in self.can_give_in_a_pinch):     # очередная карта нам не особенно и нужна-то
                        self.these_proposed_to_take.append(j)                               # добавим её в список предлагаемых
        # в первую очередь предлагаем
            if len(self.these_proposed_to_take) != 0:                                       # если есть, что предлагать к обмену
                self.its_urgent_shove = self.find_low_cards(self.these_proposed_to_take)    # на отдачу в первую очередь - младшие из предлагаемых к обмену
            else:                                                                           # если предлагать нечего:
                self.its_urgent_shove = self.find_low_cards(self.can_give_in_a_pinch)       # на отдачу в первую очередь - младшие из тех, что на крайний случай
# .................................
        def selection_cards_for_gamble_not_give(self):                                      # отбор карт на риск - НЕ ОТДАВАТЬ
            if len(self.table_card_suit) != 0:                                              # если есть что-то в недофлешах
                self.would_not_want_give = self.table_card_suit[:]                          # не отдавать - недофлеш
            if len(self.table_card_sequence_max) != 0:                                      # что-то есть в старшем недострите
                for i in range(0,len(self.table_card_sequence_max)):                        # переберём его и
                    if self.table_card_sequence_max[i] not in self.would_not_want_give:     # если карта ещё не добавлена
                        self.would_not_want_give.append(self.table_card_sequence_max[i])    # добавляем эту карту в нужные
            if len(self.table_card_sequence_min) != 0:                                      # что-то есть в младшем недострите
                for i in range(0,len(self.table_card_sequence_min)):                        # переберём его и
                    if self.table_card_sequence_min[i] not in self.would_not_want_give:     # если карта ещё не добавлена
                        self.would_not_want_give.append(self.table_card_sequence_min[i])    # добавляем эту карту в нужные
# .................................
        def selection_cards_for_gamble_proposed(self):                                      # отбор карт на риск - ПРЕДЛАГАТЬ
            if len(self.table_card_possible_combo) == 0:                                    # если нам предкомбинацию не разрушали
                for j in range (0, n_cards):                                                    # смотрим, что мы можем предложить из своего
                    if cards_rival[j].name != name_of_none:                                     # если карта не пустая
                        if (j not in self.would_not_want_give) and (j not in self.can_give_in_a_pinch):     # очередная карта не в крайнем случае
                            self.these_proposed_to_take.append(j)                               # добавим её в список предлагаемых
                self.selection_cards_for_gamble_urgent_shove()                                  # отбираем самые ненужные карты
            else:                                                                           # если предкомбинация разрушена
                for j in range (0, n_cards):                                                    # смотрим, что мы можем предложить из своего
                    if cards_rival[j].name != name_of_none:                                     # если карта не пустая
                        if j not in self.table_card_possible_combo:                             # если карта не входила в предкомбинацию
                            if (j not in self.would_not_want_give) and (j not in self.can_give_in_a_pinch):     # очередная карта не в нужных и не в крайнем случае
                                self.these_proposed_to_take.append(j)                               # добавим её в список предлагаемых
                self.selection_cards_for_gamble_urgent_shove()                                  # отбираем самые ненужные карты
# .................................
        def selection_cards_for_gamble_urgent_shove(self):                                  # отбор карт на риск в первую очередь - ПРЕДЛАГАТЬ
            if len(self.these_proposed_to_take) != 0:                                       # если есть, что предлагать к обмену
                self.its_urgent_shove = self.find_low_cards(self.these_proposed_to_take)    # на отдачу в первую очередь - младшие из предлагаемых к обмену
            else:                                                                           # если предлагать нечего:
                if len(self.can_give_in_a_pinch) !=0:                                       # если есть что отдать в крайнем случае
                    self.its_urgent_shove = self.find_low_cards(self.can_give_in_a_pinch)   # на отдачу в первую очередь - младшие из тех, что на крайний случай
                else:                                                                       # если ВСЕ карты нужны
                    self.its_urgent_shove = self.find_low_cards(self.would_not_want_give)   # самые младшие из нужных
# .................................
        def sort_cards_on_usefulness(self):                                                 # сортировка карт по категориям "полезности"
            self.would_not_want_give = []                                                   # очищаем список - что и самому надо (не отдавать)
            self.can_give_in_a_pinch = []                                                   # очищаем список - что можно отдать (в крайнем случае)
            self.these_proposed_to_take = []                                                # очищаем список - что предлагать Семёну
            self.its_urgent_shove = []                                                      # очищаем список - что отдать в первую очередь
        # -----------------------------------------------------------
            self.what_we_have()                                                             # смотрим, что на руках есть
            self.how_skill()                                                                # проверяем навык
        # ----------------------------------------------------------
            if self.playstyle == 'defense':                                                 # если защищаемся
                self.selection_cards_for_defense()                                          # сортируем карты под защиту
        # -----------------------------------------------------------
            elif self.playstyle == 'gamble':                                                        # если рискуем
                if self.combo_in_hand[0] < 4:                                                       # если на руках ДО стрита (карта, пара, две пары, тройка)
                    self.selection_cards_for_gamble_not_give()                                      # сортируем карты под риск - не отдавать
                    if len(self.would_not_want_give) == 0:                                          # если нет недокомбинаций
                        self.selection_cards_for_defense()                                          # сортируем карты под защиту
                    else:                                                                           # есть чем рискнуть
                        if self.combo_in_hand[0] in [0,1,3]:                                        # если на руках старшая карта, пара или тройка
                            for i in range(0,len(self.yourself_need_cards)):                        # перебираем карты в комбинации
                                if self.yourself_need_cards[i] not in self.would_not_want_give:     # если карты из комбинации нет в нужных
                                    self.can_give_in_a_pinch.append(self.yourself_need_cards[i])    # добавляем эту карту в список первоочередных
                            self.selection_cards_for_gamble_proposed()                              # сортируем карты под риск - предлагать
                        elif self.combo_in_hand[0] == 2:                                                    # если на руках две пары
                            for i in range(0,len(self.yourself_need_cards)):                                # перебираем карты в комбинации
                                if self.table_card_points[self.yourself_need_cards[i]] == self.combo_in_hand[1]: # если текущая карта - в старшей паре
                                    if self.yourself_need_cards[i] not in self.would_not_want_give:         # если карты из комбинации нет в нужных
                                        self.would_not_want_give.append(self.yourself_need_cards[i])        # добавляем эту карту в НУЖНЫЕ
                                else:                                                                       # если текущая карта в младшей паре
                                    if self.yourself_need_cards[i] not in self.would_not_want_give:         # если карты из комбинации нет в нужных
                                        self.can_give_in_a_pinch.append(self.yourself_need_cards[i])        # добавляем эту карту в список первоочередных
                            self.selection_cards_for_gamble_proposed()                                      # сортируем карты под риск - предлагать
                else:                                                                               # если на руках от стрита и выше
                    self.selection_cards_for_defense()                                              # сортируем карты под защиту
        # ----------------------------------------------------------- 
            elif self.playstyle == 'succumb':                                                       # если сливаемся
                if self.combo_in_hand[0] in [7,6,3,2]:                                              # если две пары, тройка, фулл-хаус, покер
                    for i in range(0,n_cards):                                                      # перебираем свои карты
                        if card_value_alt_as_max(cards_rival[i]) == self.combo_in_hand[1]:          # если значение очередной карты - равно старшей карте комбинации
                            if i not in self.this_give_definitely_succumb:                          # если ещё такой карты в списке нет
                                self.this_give_definitely_succumb.insert(0,i)                       # вставляем на 0-ю позицию
                    if (self.combo_in_hand[0] == 2) and (len(self.this_give_definitely_succumb)>2): # если 2 пары и список больше 2-х
                        del self.this_give_definitely_succumb[2:len(self.this_give_definitely_succumb)]# удаляем лишнее
                    if (self.combo_in_hand[0] in [3,6]) and (len(self.this_give_definitely_succumb)>3):# если тройка или фулл и список больше 3-х
                        del self.this_give_definitely_succumb[3:len(self.this_give_definitely_succumb)]# удаляем лишнее
                    if (self.combo_in_hand[0] == 7) and (len(self.this_give_definitely_succumb)>4): # если покер и список больше 4-х
                        del self.this_give_definitely_succumb[4:len(self.this_give_definitely_succumb)]# удаляем лишнее
                self.its_urgent_shove = self.find_older_cards(self.yourself_need_cards)             # В список на срочную отдачу - старшие карты из комбинации
                self.these_proposed_to_take = self.yourself_need_cards[:]                           # предлагать к обмену - остальные карты комбинации
                if len(self.table_card_suit) != 0:                                                  # если есть что-то в недофлешах
                    for i in range(0,len(self.table_card_suit)):                                    # переберём его и
                        if self.table_card_suit[i] not in self.these_proposed_to_take:              # такой карты ещё не добавлено
                            self.these_proposed_to_take.append(self.table_card_suit[i])             # добавляем её
                if len(self.table_card_sequence_max) != 0:                                          # что-то есть в старшем недострите
                    for i in range(0,len(self.table_card_sequence_max)):                            # переберём его и
                        if self.table_card_sequence_max[i] not in self.these_proposed_to_take:      # такой карты ещё не добавлено
                            self.these_proposed_to_take.append(self.table_card_sequence_max[i])     # добавляем её
                if len(self.table_card_sequence_min) != 0:                                          # что-то есть в младшем недострите
                    for i in range(0,len(self.table_card_sequence_min)):                            # переберём его и
                        if self.table_card_sequence_min[i] not in self.these_proposed_to_take:      # такой карты ещё не добавлено
                            self.these_proposed_to_take.append(self.table_card_sequence_min[i])     # добавляем её
                for j in range (0,len(self.waste_cards)):                                           # перебираем мусор
                    if self.waste_cards[j] not in self.these_proposed_to_take:                      # если очередной карты нет в списке предлагаемых
                        if self.waste_cards[j] not in self.this_give_definitely_succumb:            # и её же нет в списке на срочный слив
                            self.would_not_want_give.append(self.waste_cards[j])                    # добавляем её в список нужных нам
        # -----------------------------------------------------------
            elif self.playstyle == 'foolplay':                                                      # если включили дурака
                pass
        # -----------------------------------------------------------
            if self.player_unnecessary_card < 7:                                                    # если определена карта, отданная Семёном у нас - НЕНУЖНАЯ ему
                if self.playstyle in ['defense', 'gamble']:                                         # если защищаемся или рискуем
                    if (self.player_unnecessary_card in self.would_not_want_give) or (self.player_unnecessary_card in self.can_give_in_a_pinch):    # если эта карта попала в нужные 
                        pass
                    elif self.player_unnecessary_card in self.these_proposed_to_take:                   # если она попала в предлагаемые к отдаче
                        if self.player_unnecessary_card not in self.its_urgent_shove:                   # эта карта ещё не попала в первую очередь на отдачу
                            self.its_urgent_shove.insert(0,self.player_unnecessary_card)                # вставляем её туда
                elif self.playstyle == 'succumb':                                                       # если сливаемся
                    if self.player_unnecessary_card in self.its_urgent_shove:                           # если эта карта в списке на срочную отдачу
                        self.its_urgent_shove.remove(self.player_unnecessary_card)                      # удаляем её оттуда
                    if self.player_unnecessary_card in self.these_proposed_to_take:                     # если эта карта в списке предлагаемых
                        self.these_proposed_to_take.remove(self.player_unnecessary_card)                # удаляем её оттуда
                    if self.player_unnecessary_card in self.can_give_in_a_pinch:                        # если эта карта в списке на крайний случай 
                        self.can_give_in_a_pinch.remove(self.player_unnecessary_card)                   # удаляем её оттуда
                    if self.player_unnecessary_card not in self.would_not_want_give:                    # если не попала в список " не отдавать"
                        self.would_not_want_give.append(self.player_unnecessary_card)                   # добавляем её в список "не отдавать"
                elif self.playstyle == 'foolplay':                                                      # если включили дурака
                    pass                                                                                # пропускаем
            # -----------------------------------------------------------
            if self.player_accept_card < 7:                                                         # если определена карта, отданная Семёном, как НУЖНАЯ ему
                if self.playstyle in ['defense', 'gamble']:                                         # если защищаемся или рискуем
                    if (self.player_accept_card in self.its_urgent_shove) and (len(self.its_urgent_shove)>1):   # если эта карта в списке на срочную отдачу и она там не одна
                        self.its_urgent_shove.remove(self.player_accept_card)                                   # удаляем её оттуда
                    if (self.player_accept_card in self.these_proposed_to_take) and (len(self.these_proposed_to_take)>1):# если эта карта в списке предлагаемых и она там не одна
                        self.these_proposed_to_take.remove(self.player_accept_card)                                   # удаляем её оттуда
                    if self.player_accept_card in self.can_give_in_a_pinch:                             # если эта карта в списке на крайний случай 
                        self.can_give_in_a_pinch.remove(self.player_accept_card)                        # удаляем её оттуда
                    if self.player_accept_card not in self.would_not_want_give:                         # если не попала в список " не отдавать"
                        if (self.player_accept_card not in self.its_urgent_shove) and (self.player_accept_card not in self.these_proposed_to_take): # и её нет в списках на отдачу
                            self.would_not_want_give.append(self.player_accept_card)                    # добавляем её в список "не отдавать"
                elif self.playstyle == 'succumb':                                                       # если сливаемся
                    pass
                elif self.playstyle == 'foolplay':                                                      # если включили дурака
                    pass 
# .................................
        def find_low_cards(self,table):                                             # функция поиска младших карт в наборе
            min_in_combo = 15                                                       # минимальная карта в предлагаемых - принимаем 15
            i_min = []                                                              # индексы минимальных карт
            res = []                                                                # результат
            for j in range (0,len(table)):                                          # перебираем предлагаемые
                ind = table[j]                                                      # указатель на список своих карт
                if self.table_card_points[ind] < min_in_combo:                      # если очередная карта в списке по индексу меньше минимальной
                    min_in_combo = self.table_card_points[ind]                      # принимаем её за минимальную
            for j in range (0,len(table)):                                          # перебираем предлагаемые
                ind = table[j]                                                      # указатель на список своих карт
                if self.table_card_points[ind] in [min_in_combo, min_in_combo+1] :  # если очередная карта в списке минимальная или на 1 больше
                    i_min.append(j)                                                 # в список индексов минимальных карт из предлагаемых добавляем значение
            for i in i_min:                                                         # переберём индексы минимальных карт
                res.append(table[i])                                                # и добавим младшие карты из передлагаемых в список ненужных
            return res                                                              # возвращаем таблицу
# .................................
        def find_older_cards(self,table):                                           # функция поиска старших карт в наборе
            max_in_combo = 0                                                        # максимальная карта в комбинации - принимаем 0
            i_max = []                                                              # индексы максимальных карт
            res = []                                                                # результат
            for j in range (0,len(table)):                                          # перебираем комбинацию
                ind = table[j]                                                      # указатель на список своих карт
                if self.table_card_points[ind] > max_in_combo:                      # если очередная карта в списке по индексу больше максимальной
                    max_in_combo = self.table_card_points[ind]                      # принимаем её за максимальную
            for j in range (0,len(table)):                                          # перебираем комбинацию
                ind = table[j]                                                      # указатель на список своих карт
                if self.table_card_points[ind] >= max_in_combo:                     # если очередная карта в списке по индексу больше или равна максимальной
                    i_max.append(j)                                                 # в список индексов максимальных карт комбинации добавляем значение
            for i in i_max:                                                         # переберём индексы максимальных карт
                res.append(table[i])                                                # и добавим старшие карты комбинации в список ненужных
            return res                                                              # возвращаем таблицу
# .................................
        def what_pulled_player(self):                                           # что собрался вытащить игрок
            for i in range(0,n_cards):                                          # перебираем свои карты
                if cards_rival[i].interesting:                                  # если Семён потянулся за этой картой
                    self.pulled_player_card = i                                 # то это она и есть
# .................................
        def do_we_need_this_card(self):                                         # что игрок вытащил и насколько эта карта важна
            self.degree_usefulness_card = 0                                     # степень "полезности" вытащенной карты
            self.what_pulled_player()                                           # смотрим, куда Сёма нацелился
            self.dragged_player_card = self.pulled_player_card                  # и эту карту он сейчас заберёт
            if self.dragged_player_card in self.would_not_want_give:            # если карта из тех, что не отдавать
                self.degree_usefulness_card = 3                                 # забрать её срочно
            elif self.dragged_player_card in self.can_give_in_a_pinch:          # если карта из тех, что в крайнем случае
                self.degree_usefulness_card = 2                                 # запомнить её, заберём в другой раз, это не срочно
            elif (self.dragged_player_card in self.its_urgent_shove) or (self.dragged_player_card in self.these_proposed_to_take): # если карта из числа ненужных
                self.degree_usefulness_card = 1                                 # то и хрен с нею
# .................................
        def to_give_just_card(self):                                            # а может, сразу отдать карту Семёну?
            min_cards = 15                                                      # значение очков карты = 15 (такого нет точно)
            i_min = 7                                                           # индекс карты = 7 (такого нет точно)
            global changes_left                                                 # понадобится количество оставшихся обменов
            self.how_skill()                                                    # проверяем навык
            if (self.playstyle in ['defense','gamble','succumb']) and (not self.make_mistakes): # если стиль игры из определённых и не ошибаемся
                self.sort_cards_on_usefulness()                                 # рассортировали своё по степени нужности
                self.what_pulled_player()                                       # смотрим, куда потянулся Семён
        #-------------------------------------------
                if self.pulled_player_card in self.this_give_definitely_succumb:    # если потянулся к той карте, которая у нас в срочном сливе
                    if self.combo_in_hand[0] not in [4,5,8,9]:                  # если на руках НЕ флэш или стрит
                        renpy.pause(1.0)                                        # немного подумали и.....
                        changes_left = 0                                        # сбрасываем обмены (Сеня заберёт карту)
                    else:                                                       # если флеш или стрит
                        pass                                                    # таки будем менять карты
                elif self.pulled_player_card in self.its_urgent_shove:          # если эта карта - в списке сплавляемых в первую очередь
                    if (len(self.its_urgent_shove) == 1) or (self.playstyle == 'succumb'): # и такая карта всего одна ИЛИ игра в поддавки
                        renpy.pause(1.0)                                        # немного подумали и.....
                        changes_left = 0                                        # сбрасываем обмены (Сеня заберёт карту)
                    elif len(self.its_urgent_shove) > 1:                        # и совсем ненужных несколько 
                        k = random.choice([1,2,3])                              # решаем - отдавать карту сразу (1,2) или нет (3) - вероятность 0,66
                        if k in [1,2]:                                          # и если да
                            renpy.pause(1.0)                                    # немного подумали и.....
                            changes_left = 0                                    # сбрасываем обмены (Сеня заберёт карту)
                elif (self.pulled_player_card in self.these_proposed_to_take) and (self.playstyle != 'succumb'):    # если эта карта - в списке предлагаемых на обмен и НЕ слив
                    k = random.choice([1,2,3,4])                                # решаем - отдавать карту сразу (1) или нет (2,3,4) - вероятность 0,25
                    if k == 1:                                                  # и если да
                        renpy.pause(1.0)                                        # немного подумали и.....
                        changes_left = 0                                        # сбрасываем обмены (Сеня заберёт карту)
        #-------------------------------------------
            elif (self.playstyle == 'foolplay') or (self.make_mistakes):        # если включили дурака или ошибаемся
                k = random.choice([1,2,3,4,5,6,7])                              # решаем - отдавать карту сразу (1) или нет (2..7) - вероятность 0,15
                if k == 1:                                                      # и если да
                    renpy.pause(1.0)                                            # немного подумали и.....
                    changes_left = 0                                            # сбрасываем обмены (Сеня заберёт карту)
# .................................
        def what_to_xchange_think(self):                                        # думаем, какие карты будем менять
            self.how_skill()                                                    # проверяем навык
        #-------------------------------------------
            if (self.playstyle in ['defense','gamble','succumb']) and (not self.make_mistakes): # если стиль игры из определённых и не ошибаемся
                self.what_pulled_player()                                       # смотрим, куда потянулся Семён
                i = self.pulled_player_card                                     # первая карта на обмен - она же
                j = 7                                                           # вторую - принимаем = 7
                if (i in self.would_not_want_give) or (i in self.can_give_in_a_pinch): # если карта в списках нужных
                    if len(self.its_urgent_shove) != 0:                         # если есть, что срочно отдать
                        j = random.choice(self.its_urgent_shove)                # случайная карта из ненужных
                    elif len(self.these_proposed_to_take) != 0:                 # если срочного нет, но есть, что можно предложить на обмен
                        j = random.choice(self.these_proposed_to_take)          # случайная карта из обменных
                    elif len(self.can_give_in_a_pinch) != 0:                    # если ненужных нет, но есть что отдать в крайнем случае
                        j = random.choice(self.can_give_in_a_pinch)             # случайная из крайнего случая
                        while i == j:                                           # если (а затем - пока) индексы одинаковы
                            j = random.choice(self.can_give_in_a_pinch)         # ещё рандомим вторую карту
                elif i in self.these_proposed_to_take:                          # если карта в списке предлагаемых
                    if len(self.its_urgent_shove) != 0:                         # если есть, что срочно отдать
                        j = random.choice(self.its_urgent_shove)                # случайная карта из ненужных
                    else:                                                       # если срочно отдавать нечего
                        j = random.choice(self.these_proposed_to_take)          # случайная карта из обменных
                        while i == j:                                           # если (а затем - пока) индексы одинаковы
                            j = random.choice(self.these_proposed_to_take)      # ещё рандомим вторую карту
                elif i in self.its_urgent_shove:                                # если карта в списке срочного сброса, но попали сюда
                    j = random.choice(self.its_urgent_shove)                    # случайная карта из ненужных
                    while i == j:                                               # если (а затем - пока) индексы одинаковы
                        j = random.choice(self.its_urgent_shove)                # ещё рандомим вторую карту
                if j == 7:                                                      # каким-то образом карты для обмена не нашлось
                    j = random.choice(self.yourself_need_cards+self.waste_cards)    # вторая карта для обмена из числа нужных + ненужных
                    while i == j:                                                   # если (а затем - пока) индексы одинаковы
                        j = random.choice(self.yourself_need_cards+self.waste_cards)# ещё рандомим вторую карту
        #-------------------------------------------
            elif (self.playstyle == 'foolplay') or (self.make_mistakes):        # если включили дурака или ошибаемся
                i = random.choice(self.yourself_need_cards+self.waste_cards)    # первая карта для обмена из числа нужных + ненужных
                j = random.choice(self.yourself_need_cards+self.waste_cards)    # вторая карта для обмена из числа нужных + ненужных
                while i == j:                                                   # если (а затем - пока) индексы одинаковы
                    j = random.choice(self.yourself_need_cards+self.waste_cards)# ещё рандомим вторую карту
        #-------------------------------------------
            if self.player_unnecessary_card == i:                               # если выбранная карта - не нужная Семёну
                self.player_unnecessary_card = j                                # меняем её позицию
            elif self.player_unnecessary_card == j:                             # если одна из карт - не нужная Семёну
                self.player_unnecessary_card = i                                # меняем её позицию
            if self.player_accept_card == i:                                    # если выбранная карта - НУЖНАЯ Семёну
                self.player_accept_card = j                                     # меняем её позицию
            elif self.player_accept_card == j:                                  # если одна из карт - НУЖНАЯ Семёну
                self.player_accept_card = i                                     # меняем её позицию
        #-------------------------------------------
            if len (self.this_give_definitely_succumb) !=0:                     # если список старших карт на отдачу не пуст
                if j in self.this_give_definitely_succumb:                      # если выбранная для обмена карта в списке
                    self.this_give_definitely_succumb.remove(j)                 # удаляем её
                    self.this_give_definitely_succumb.append(i)                 # добавляем ту, за которой потянулся Семён
        #-------------------------------------------
            return (i,j)                                                        # выдаём позиции для обмена
# .................................
        def what_at_us_took(self,z):                                                # а что у нас Семён забрал - нужную или ненужную    
            if self.degree_usefulness_card == 3:                                    # если забрал нужную
                self.pick_this_cards_urgently.insert(0,self.inserted_player_card)   # добавляем вынутую у нас карту в список "забрать срочно"
            elif self.degree_usefulness_card == 2:                                  # если забрал из тех, что на крайний случай
                self.pick_this_cards_afterwards.insert(0,self.inserted_player_card) # добавляем вынутую у нас карту в список "забрать потом"
            elif self.degree_usefulness_card == 1:                                  # если забрал ненужную
                self.never_touch_cards.insert(0,self.inserted_player_card)          # добавляем вынутую у нас карту в список ненужных у Семёна
            if z == self.player_unnecessary_card:                                   # сбагрили Семёну его же ненужную ему карту
                self.player_unnecessary_card = 7                                    # присваиваем индекс 7
            if z == self.player_accept_card:                                        # Семён забрал у нас нужную ему карту
                self.player_accept_card = 7                                         # присваиваем индекс 7
                
            if z in self.this_give_definitely_succumb:                              # если забрал ту, которая в списке слива
                if self.inserted_player_card not in self.never_touch_cards:         # если такой карты ещё нет в списке
                    self.never_touch_cards.insert(0,self.inserted_player_card)          # добавляем её в список "не трогать"
                self.this_give_definitely_succumb.remove(z)                         # удаляем эту карту у себя
# .................................
        def what_card_we_gave_7(self,x,y):                                          # какая карта отдана при игре на 7 картах (карта игрока, карта Семёна)
            if x in self.would_not_want_give:                                       # если карта У СЕБЯ и нам нужна
                self.pick_this_cards_urgently.insert(0,y)                           # вставляем её индекс У СЕМЁНА в список на срочное изъятие
            if x in self.can_give_in_a_pinch:                                       # если карта У СЕБЯ из тех, что на крайний случай
                self.pick_this_cards_afterwards.insert(0,y)                         # вставляем её индекс У СЕМЁНА в список на "забрать потом"
            if (x in self.its_urgent_shove) or (x in self.these_proposed_to_take):  # и если карта У СЕБЯ из тех, что надо срочно спихнуть
                self.never_touch_cards.insert(0,y)                                  # вставляем её индекс У СЕМЁНА в список "не трогать"
            if x in self.this_give_definitely_succumb:                              # если карта их сливного списка
                self.never_touch_cards.insert(0,y)                                  # вставляем её индекс У СЕМЁНА в список "не трогать"
                self.this_give_definitely_succumb.remove(x)                         # и удаляем у себя
# .................................
        def tracked_movement(self,i,j):                                         # отслеживаем перемещение интересующих нас карт (какие вообще переместились)
            temp_x1 = temp_x2 = temp_x3 = temp_y1 = temp_y2 = temp_y3 = 7       # такой карты точно нет, потому временные именно такие
            x1 = x2 = x3 = y1 = y2 = y3 = 7                                     # индексы также принимаем по 7
        #-------------------------------------------
            if i in self.never_touch_cards:                                     # если первая карта пары в блоке ненужных
                x1 = self.never_touch_cards.index(i)                            # индекс нахождения этой карты в списке
                temp_x1 = j                                                     # запоминаем вторую карту пары
            elif i in self.pick_this_cards_afterwards:                          # если первая карта пары в списке "забрать потом"
                x2 = self.pick_this_cards_afterwards.index(i)                   # индекс нахождения этой карты в списке
                temp_x2 = j                                                     # запоминаем вторую карту пары
            elif i in self.pick_this_cards_urgently:                            # если первая карта пары в списке "забрать срочно"
                x3 = self.pick_this_cards_urgently.index(i)                     # индекс нахождения этой карты в списке
                temp_x3 = j                                                     # запоминаем вторую карту пары
        #-------------------------------------------
            if j in self.never_touch_cards:                                     # если вторая карта пары в блоке ненужных
                y1 = self.never_touch_cards.index(j)                            # индекс нахождения этой карты в списке
                temp_y1 = i                                                     # запоминаем первую карту пары
            elif j in self.pick_this_cards_afterwards:                          # если вторая карта пары в списке "забрать потом"
                y2 = self.pick_this_cards_afterwards.index(j)                   # индекс нахождения этой карты в списке
                temp_y2 = i                                                     # запоминаем первую карту пары
            elif j in self.pick_this_cards_urgently:                            # если вторая карта пары в списке "забрать срочно"
                y3 = self.pick_this_cards_urgently.index(j)                     # индекс нахождения этой карты в списке
                temp_y3 = i                                                     # запоминаем первую карту пары
        #-------------------------------------------
            if temp_x1 != 7:                                                    # первая карта попала в список ненужных
                self.never_touch_cards[x1] = temp_x1                            # меняем на место второй карты в паре
            if temp_y1 != 7:                                                    # вторая карта попала в список ненужных
                self.never_touch_cards[y1] = temp_y1                            # меняем на место первой карты в паре
            if temp_x2 != 7:                                                    # первая карта попала в список "на потом"
                self.pick_this_cards_afterwards[x2] = temp_x2                   # меняем на место второй карты в паре
            if temp_y2 != 7:                                                    # вторая карта попала в список "на потом"
                self.pick_this_cards_afterwards[y2] = temp_y2                   # меняем на место первой карты в паре
            if temp_x3 != 7:                                                    # первая карта попала в список "забрать срочно"
                self.pick_this_cards_urgently[x3] = temp_x3                     # меняем на место второй карты в паре
            if temp_y3 != 7:                                                    # вторая карта попала в список забрать срочно
                self.pick_this_cards_urgently[y3] = temp_y3                     # меняем на место первой карты в паре
# .................................
        def usual_card_choose(self):                                            # "обычный" выбор карты у Семёна
            temp = []                                                           # пустой слот для отдачи
            if len(self.pick_this_cards_urgently) != 0:                         # если список "забрать срочно" не пустой
                res = self.pick_this_cards_urgently[0]                          # а вот самую первую оттедова и тянем
            elif len(self.pick_this_cards_afterwards) != 0:                     # если список "забрать потом" не пустой
                res = self.pick_this_cards_afterwards[0]                        # а вот самую первую оттедова и тянем
            else:                                                               # если срочно ничего забирать не надо
                if len(self.never_touch_cards) != 0:                            # если список ненужных карт не пустой
                    for item in set(range(0,n_cards)).difference(self.never_touch_cards): #перебрали список от 0 до числа карт; выводим те, которых нет в ненужных
                        if cards_my[item].name != name_of_none:             # если очередная карта не пустая
                            temp.append(item)                               # добавим её в список на вытягивание
                    res = random.choice(temp)                               # выбираем рандомно из списка на забор
                else:                                                       # если ненужных карт нет
                    res = random.randrange(0,n_cards)                       # рандом изо всех
                    if cards_my[res].interesting:                           # если карта уже отмечена
                        y = random.choice([True,False])                     # подумаем, а не выбрать ли другую
                        if y:                                               # если выбрать другую
                            res = random.randrange(0,n_cards)               # выбираем ёщё раз рандомно из всех
                            while cards_my[res].name == name_of_none:       # пока попадается карта пустая
                                res = random.randrange(0,n_cards)           # выбираем другую
                    else:                                                   # если карта не отмечена
                        while cards_my[res].name == name_of_none:           # пока попадается карта пустая
                            res = random.randrange(0,n_cards)               # выбираем другую
            return res
# .................................
        def random_card_choose(self):                                       # "случайный" выбор карты у Семёна
            x = random.randrange(0,n_cards)                                 # рандом изо всех
            while cards_my[x].name == name_of_none:                         # если карта пустая
                x = random.randrange(0,n_cards)                             # выбираем другую
            return x
# .................................
        def what_card_choose(self):                                             # какую карту будем выбирать у Семэна?
            global cycles_left                                                  # потребуется количество оставшихся циклов
            self.how_skill()                                                            # проверяем навык
            if (self.playstyle in ['defense','succumb']) and (not self.make_mistakes):  # если защита или слив и не ошибаемся
                res = self.usual_card_choose()                                          # "обычный выбор" у Семёна
        #-------------------------------------------
            elif (self.playstyle =='gamble') and (not self.make_mistakes):          # если рискуем и не ошибаемся
                self.what_cards_have()                                              # проверяем, что там у нас на руках
                
                if self.combo_was_before == None:                                   # если комбинации еще не сравнивали
                    self.combo_was_before = []                                      # создаём пустой список
                if len(self.combo_was_before) == 0:                                 # если список пустой
                    self.combo_was_before = [0,0,0,0]                               # создаём заполнитель для проверки
                
                if (self.combo_was_before[0] >= 4) and (self.as_changed_combo == 'worse'):  # если был стрит и выше и положение ухудшилось
                    res = self.usual_card_choose()                                          # "обычный выбор" у Семёна, нефиг рисковать
                else:                                                                       # во всех других случаях
                    if (len(self.table_card_suit) !=0) or (len(self.table_card_sequence_min) !=0) or (len(self.table_card_sequence_max) !=0): # если осталось, из-за чего рисковали
                        if cycles_left == 3:                                            # если осталось три круга
                            res = self.random_card_choose()                             # "случайный выбор" у Семёна - рискуем, однако
                        elif cycles_left == 2:                                          # если осталось два круга
                            if len(self.pick_this_cards_urgently) <= 1:                 # если количество карт, что надо забрать строчно - нет или одна
                                res = self.random_card_choose()                         # "случайный выбор" у Семёна - рискуем, однако
                                while res in self.never_touch_cards:                    # если "случайная" карта и нам не нужна
                                    res = self.random_card_choose()                     # ещё "случайный выбор" у Семёна
                            else:                                                       # если срочно забрать надо две карты
                                res = self.usual_card_choose()                          # "обычный выбор" у Семёна
                        elif cycles_left == 1:                                          # если остался один круг
                            if len(self.pick_this_cards_urgently) == 0:                 # вдруг ничего срочно забрать не надо
                                res = self.random_card_choose()                         # "случайный выбор" у Семёна - рискуем до упора
                                while res in self.never_touch_cards:                    # если "случайная" карта и нам не нужна
                                    res = self.random_card_choose()                     # ещё "случайный выбор" у Семёна
                            else:                                                       # свою карту надо забирать и срочно
                                res = self.usual_card_choose()                          # "обычный выбор" у Семёна
                    else:                                                               # если рисковать уже смысла нет
                        if self.combo_in_hand[0] >=4:                                   # если риск оправдался
                            self.pick_this_cards_urgently = []                          # удаляем карты "забрать срочно"
                            self.pick_this_cards_afterwards = []                        # удаляем карты "забрать потом"
                        res = self.usual_card_choose()                                  # "обычный выбор" у Семёна
        #-------------------------------------------
            elif (self.playstyle == 'foolplay') or (self.make_mistakes):        # если включили дурака или ошибаемся
                res = self.random_card_choose()                                 # "случайный выбор" у Семёна
        #-------------------------------------------
            return res 
# .................................
        def pick_my_card_last_think(self):                                      # последняя выделенная карта игрока - используется в режиме (соперник забирает)
            self.how_skill()                                                    # проверяем навык
            if (self.playstyle in ['defense','gamble']) and (not self.make_mistakes): # если защита или риск и не ошибаемся
                x = self.pick_my_card_last_usual()                              # обычный выбор последней карты
                
            elif (self.playstyle == 'succumb') and (not self.make_mistakes):    # если слив и не ошибаемся
                if self.last_selected_card !=7 :                                # если определена последняя выбранная карта
                    if self.last_selected_card not in self.never_touch_cards:   # если последняя выбранная НЕ в списке тех, которые "не трогать"
                        x = self.last_selected_card                             # выбираем ту карту, которую нам подсунули
                    else:                                                       # Семён подсунул ту карту, что "не трогать"
                        if len(self.pick_this_cards_urgently) !=0:              # список "забрать срочно" НЕ пустой
                            x = self.pick_this_cards_urgently[0]                # а вот самую первую и выбираем
                        elif len(self.pick_this_cards_afterwards) !=0:          # список "забрать потом" НЕ пустой
                            x = self.pick_this_cards_afterwards[0]              # а вот самую первую и выбираем
                        else:                                                   # списки "забрать эти карты" пустые
                            x = self.pick_my_card_last_usual()                  # обычный выбор последней карты
                else:                                                           # последний выбор не определен
                    x = self.pick_my_card_last_random()                         # рандомный выбор
                
            elif (self.playstyle == 'foolplay') or (self.make_mistakes):        # если включили дурака или ошибаемся
                x = self.pick_my_card_last_random()                             # рандомный выбор
                
            self.last_selected_card = 7                                         # сбрасываем последнюю выбранную карту
            self.what_is_pulled_out(x)                                          # проверяем, что вынули у Семёна
            return x
# .................................
        def pick_my_card_last_usual(self):                                      # последняя выделенная карта игрока - обычный режим
            for i in range(0,n_cards):                                          # перебрать карты
                if  cards_my[i].interesting:                                    # если карта игрока выделена соперником
                    x = i                                                       # вернуть место карты в стеке
            return x
# .................................
        def pick_my_card_last_random(self):                                     # последняя выделенная карта игрока - ослучайный выбор
            x = random.randrange(0,n_cards)                                     # рандом изо всех
            while cards_my[x].name == name_of_none:                             # если карта пустая
                x = random.randrange(0,n_cards)                                 # выбираем другую
            return x
# .................................
        def what_is_pulled_out(self,i):                                         # проверяем, что вынули у Семёна (номер его карты)
            if i in self.pick_this_cards_urgently:                              # если карта входит в список карт "забрать срочно"
                self.pick_this_cards_urgently.remove(i)                         # удаляем эту карту
            if i in self.pick_this_cards_afterwards:                            # если карта входит в список карт "забрать потом"
                self.pick_this_cards_afterwards.remove(i)                       # удаляем эту карту
            if i in self.never_touch_cards:                                     # если карта входит в список карт "не забирать"
                self.never_touch_cards.remove(i)                                # удаляем эту карту
# .................................
        def give_away_card_think(self):                                         # что отдаём при игре на 7 картах ?
            self.how_skill()                                                    # проверяем навык
            if (self.playstyle in ['defense','succumb']) and (not self.make_mistakes): # если защищаемся или сливаем и не ошибаемся
                if len (self.this_give_definitely_succumb) != 0:                    # если список срочного слива не пустой
                    if self.combo_in_hand[0] not in [4,5,8,9]:                      # если НЕ флэш или стрит
                        i = random.choice(self.this_give_definitely_succumb)        # случайную карту из срочного слива предлагаем
                    else:                                                           # если есть что сливать, но комбинация старше
                        i = self.give_away_card_think_usual()                       # предлагаем на обмен то, что обычно
                else:                                                               # список срочного слива пустой
                    i = self.give_away_card_think_usual()                           # предлагаем на обмен то, что обычно
            elif (self.playstyle =='gamble') and (not self.make_mistakes):      # если рискуем и не ошибаемся
                if self.combo_in_hand[0] < 4:                                       # если меньше стрита
                    if len(self.table_card_possible_combo) !=0:                     # если что-то есть в возможной комбинации
                        i = 7                                                       # индекс отдаваемой карты принимаем 7
                        if len(self.its_urgent_shove) !=0:                          # если список того, что надо сдать, не пустой
                            for j in range (0,len(self.its_urgent_shove)):          # перебираем его и..
                                if self.its_urgent_shove[j] not in self.table_card_possible_combo:  # если очередная карта не в потенциальной комбинации
                                    i = self.its_urgent_shove[j]                    # первую же такую карту и отдаём
                                    break                                           # и цикл завершаем
                        if i == 7:                                                  # не нашли подходящую карту в срочном сбросе
                            if len(self.these_proposed_to_take) !=0:                # есть что предлагать вообще
                                for j in range (0,len(self.these_proposed_to_take)):# перебираем его и..
                                    if self.these_proposed_to_take[j] not in self.table_card_possible_combo:  # если очередная карта не в потенциальной комбинации
                                        i = self.these_proposed_to_take[j]          # первую же такую карту и отдаём
                                        break                                       # и цикл завершаем
                        if i == 7:                                                  # не нашли подходящую карту в предлагаемых на сброс
                            if len(self.can_give_in_a_pinch) !=0:                   # что-то есть в крайнем случае
                                for j in range (0,len(self.can_give_in_a_pinch)):   # перебираем его и..
                                    if self.can_give_in_a_pinch[j] not in self.table_card_possible_combo:  # если очередная карта не в потенциальной комбинации
                                        i = self.can_give_in_a_pinch[j]             # первую же такую карту и отдаём
                                        break                                       # и цикл завершаем
                        if i == 7:                                                  # что-то найти была не судьба
                            i = self.give_away_card_think_usual()                   # предлагаем на обмен то, что обычно
                    else:                                                           # если в возможной комбинации ничего нет
                        i = self.give_away_card_think_usual()                       # предлагаем на обмен то, что обычно
                else:                                                               # если стрит и выше
                    i = self.give_away_card_think_usual()                           # предлагаем на обмен то, что обычно
            elif (self.playstyle == 'foolplay') or (self.make_mistakes):        # если включили дурака или ошибаемся
                i = random.randrange(0,n_cards)                                 # отдаём случайную карту (из нужных и ненужных)
            return i
# .................................
        def give_away_card_think_usual(self):                                   # что отдаём при игре на 7 картах - обычно
            if len(self.its_urgent_shove) != 0:                                 # если список того, что надо сдать, не пустой
                i = random.choice(self.its_urgent_shove)                        # случайная карта из списка на срочное впаривание
            elif len(self.these_proposed_to_take) !=0:                          # если вдруг случится так, что срочно впарить нечего  и есть, что предложить на обмен
                i = random.choice(self.these_proposed_to_take)                  # случайная карта из предлагаемых к отдаче
            elif len(self.can_give_in_a_pinch) !=0:                             # если ничего нет в первых вариантах, но не пустой список крайнего случая
                i = random.choice(self.can_give_in_a_pinch)                     # случайная карта из отдаваемых в крайнем случае
            return i
# .................................
        def how_skill(self):                                                    # проверка навыка (вероятность ошибки)
            self.make_mistakes = True                                           # включаем режим ошибки
            i = random.choice([1,2,3,4,5])                                      # рандомно выбираем значение вероятности ошибки, шанс ошибки: 5-0%, 4-20%, 3-40% 2-60% 1-80%
            if i <= self.mistake_chance:                                        # если вероятность ошибки меньше или равна навыку
                self.make_mistakes = False                                      # не ошибаемся
# .................................



##########################  ИГРОКИ  ##################################### 



# =======================================================================
    class CardGameRivalWiseUsual(CardGameRivalWise_alt):                    # обычный игрок
        def allow_to_take(self):                                            # разрешение на выбор карт у соперника при ходе игрока (обычный соперник)
            for i in range(0,n_cards):                                      # перебираем карты
                cards_rival[i].allow = True                                 # для каждой карты = доступна для выбора
# .................................
        def allow_to_defend(self):                                          # режим защиты обычного игрока
            return True                                 
# .................................
        def want_to_defend(self):                                           # разрешение ИГРОКУ на защиту (отличается у Ульяны в классике)
            return True
 
# =======================================================================
    class CardGameRivalWiseLikeUS(CardGameRivalWise_alt):                   # стиль игры - как у Ульяны
        def what_card_choose(self):                                         # переопределённый метод - за Ульяну выбирает Семён
            type,index = cards_interact_alt()                               # из-за этой строки
            return index
# .................................
        def allow_to_take(self):                                            # разрешение на выбор карт у соперника при ходе игрока (Ульяна)
            for i in range(0,n_cards):                                      # перебираем карты
                cards_rival[i].allow = False                                # делаем ВСЕ карты соперника недоступными для выбора
            self.how_skill()                                                # проверяем навык
        #-------------------------------------------
            if (self.playstyle in ['defense','gamble','succumb']) and (not self.make_mistakes): # если стиль игры из определённых и не ошибаемся
                if len(self.its_urgent_shove) != 0:                             # если есть, что срочно отдать
                    i = random.choice(self.its_urgent_shove)                    # случайная карта из ненужных
                elif len(self.these_proposed_to_take) != 0:                     # если срочного нет, но есть, что можно предложить на обмен
                    i = random.choice(self.these_proposed_to_take)              # случайная карта из обменных
                elif len(self.can_give_in_a_pinch) != 0:                        # если ненужных нет, но есть что отдать в крайнем случае
                    i = random.choice(self.can_give_in_a_pinch)                 # случайная из крайнего случая
        #-------------------------------------------
            elif (self.playstyle == 'foolplay') or (self.make_mistakes):        # если включили дурака или ошибаемся
                i = random.choice(self.yourself_need_cards+self.waste_cards)    # отдаём случайную карту из числа нужных + ненужных
        #-------------------------------------------
            cards_rival[i].allow = True                                         # выбранную карту делаем доступной для выбора
            cards_rival[i].interesting = True                                   # и её же выделяем стрелкой
# .................................
        def want_to_defend(self):                                               # режим защиты Ульяны
            return False
# .................................
        def allow_to_defend(self):                                              # разрешение Ульяне на защиту (нет)
            return False
        
    
    

