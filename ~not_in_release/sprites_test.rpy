init:
    $ mods["alt_sprites_test"] = u"Тест спрайтов 7дл"
    $ mod_tags["alt_sprites_test"] = ["length:days","gameplay:vn","protagonist:male"]
label alt_sprites_test:
    python:
        normal_sprites_list = []
        close_sprites_list = []
        far_sprites_list = []
        custom_sprites_list = []
        for dist in alt_dist:
            if dist == "normal/":
                for who in alt_body_dict.keys():
                    for pose in alt_body_dict[who]:
                        for body in alt_body_dict[who][pose]:
                            for clothes in alt_clothes_dict[who][pose]:
                                for emo in alt_emo_dict[who][pose]:
                                    for acc in alt_acc_dict[who][pose]:
                                        if body != '':
                                            if 'body2' in body:
                                                who_num = who + '2'
                                            elif 'body' in body:
                                                who_num = who
                                            if clothes != '' and clothes != 'body':
                                                if emo != '':
                                                    if acc != '':
                                                        normal_sprites_list.append(who_num + ' ' + emo + ' ' + clothes + ' ' + acc)
                                                        close_sprites_list.append(who_num + ' ' + emo + ' ' + clothes + ' ' + acc + ' close')
                                                    else:
                                                        normal_sprites_list.append(who_num + ' ' + emo + ' ' + clothes)
                                                        close_sprites_list.append(who_num + ' ' + emo + ' ' + clothes + ' close')
                                            elif clothes == 'body':
                                                if emo != '':
                                                    if acc != '':
                                                        normal_sprites_list.append(who_num + ' ' + emo + ' ' + 'body' + ' ' + acc)
                                                        close_sprites_list.append(who_num + ' ' + emo + ' ' + 'body' + ' ' + acc + ' close')
                                                    else:
                                                        normal_sprites_list.append(who_num + ' ' + emo + ' ' + 'body')
                                                        close_sprites_list.append(who_num + ' ' + emo + ' ' + 'body' + ' close')
                                            else:
                                                if emo != '':
                                                    if acc != '':
                                                        if who == 'cs':
                                                            normal_sprites_list.append(who_num + ' ' + emo + ' ' + acc)
                                                            close_sprites_list.append(who_num + ' ' + emo + ' ' + acc + ' close')
                                                        else:
                                                            normal_sprites_list.append(who_num + ' ' + emo + ' ' + 'pioneer' + ' ' + acc)
                                                            close_sprites_list.append(who_num + ' ' + emo + ' ' + 'pioneer' + ' ' + acc + ' close')
                                                    else:
                                                        if who == 'cs':
                                                            normal_sprites_list.append(who_num + ' ' + emo)
                                                            close_sprites_list.append(who_num + ' ' + emo + ' close')
                                                        else:
                                                            normal_sprites_list.append(who_num + ' ' + emo + ' ' + 'pioneer')
                                                            close_sprites_list.append(who_num + ' ' + emo + ' ' + 'pioneer' + ' close')
                                        else:
                                            who_num = who
                                            if emo != '':
                                                if acc != '':
                                                    normal_sprites_list.append(who_num + ' ' + emo + ' ' + clothes + ' ' + acc)
                                                    close_sprites_list.append(who_num + ' ' + emo + ' ' + clothes + ' ' + acc + ' close')
                                                else:
                                                    normal_sprites_list.append(who_num + ' ' + emo + ' ' + clothes)
                                                    close_sprites_list.append(who_num + ' ' + emo + ' ' + clothes + ' close')
            elif dist == "far/":
                for who in alt_body_far_dict.keys():
                    for pose in alt_body_far_dict[who]:
                        for body in alt_body_far_dict[who][pose]:
                            for clothes in alt_clothes_far_dict[who][pose]:
                                for emo in alt_emo_far_dict[who][pose]:
                                    for acc in alt_acc_far_dict[who][pose]:
                                        if body != '':
                                            if 'body2' in body:
                                                who_num = who + '2'
                                            elif 'body' in body:
                                                who_num = who
                                            if clothes != '' and clothes != 'body':
                                                if emo != '':
                                                    if acc != '':
                                                        far_sprites_list.append(who_num + ' ' + emo + ' ' + clothes + ' ' + acc + ' far')
                                                    else:
                                                        far_sprites_list.append(who_num + ' ' + emo + ' ' + clothes + ' far')
                                            elif clothes == 'body':
                                                if emo != '':
                                                    if acc != '':
                                                        far_sprites_list.append(who_num + ' ' + emo + ' ' + 'body' + ' ' + acc + ' far')
                                                    else:
                                                        far_sprites_list.append(who_num + ' ' + emo + ' ' + 'body' + ' far')
                                            else:
                                                if emo != '':
                                                    if acc != '':
                                                        if who == 'cs':
                                                            far_sprites_list.append(who_num + ' ' + emo + ' ' + acc + ' far')
                                                        else:
                                                            far_sprites_list.append(who_num + ' ' + emo + ' ' + 'pioneer' + ' ' + acc + ' far')
                                                    else:
                                                        if who == 'cs':
                                                            far_sprites_list.append(who_num + ' ' + emo + ' far')
                                                        else:
                                                            far_sprites_list.append(who_num + ' ' + emo + ' ' + 'pioneer' + ' far')
                                        else:
                                            who_num = who
                                            if emo != '':
                                                if acc != '':
                                                    far_sprites_list.append(who_num + ' ' + emo + ' ' + clothes + ' ' + acc + ' far')
                                                else:
                                                    far_sprites_list.append(who_num + ' ' + emo + ' ' + clothes + ' far')
        for custom in alt_custom_list:
            if 'far' in custom:
                custom_sprites_list.append(custom)
            else:
                custom_sprites_list.append(custom)
    $ filter1 = renpy.input("Фильтр 1")
    $ filter2 = renpy.input("Фильтр 2")
    menu:
        "normal":
            python:
                for x in normal_sprites_list:
                    if (filter1 in x) and (filter2 in x):
                        renpy.show(x)
                        ui.button(clicked=None, xcenter=0.5, ycenter=0.8)
                        ui.text(x, style="button_text", size=30)
                        renpy.pause(.5)
                        renpy.hide(x)
        "close":
            python:
                for x in close_sprites_list:
                    if (filter1 in x) and (filter2 in x):
                        renpy.show(x)
                        ui.button(clicked=None, xcenter=0.5, ycenter=0.8)
                        ui.text(x, style="button_text", size=30)
                        renpy.pause(.5)
                        renpy.hide(x)
        "far":
            python:
                for x in far_sprites_list:
                    if (filter1 in x) and (filter2 in x):
                        renpy.show(x)
                        ui.button(clicked=None, xcenter=0.5, ycenter=0.8)
                        ui.text(x, style="button_text", size=30)
                        renpy.pause(.5)
                        renpy.hide(x)
        "custom":
            python:
                for x in custom_sprites_list:
                    if (filter1 in x) and (filter2 in x):
                        renpy.show(x)
                        ui.button(clicked=None, xcenter=0.5, ycenter=0.8)
                        ui.text(x, style="button_text", size=30)
                        renpy.pause(.5)
                        renpy.hide(x)
jump alt_sprites_test