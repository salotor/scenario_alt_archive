init:
    $ mods["alt_sprites_test"] = u"Тест спрайтов 7дл"
    $ mod_tags["alt_sprites_test"] = ["length:days","gameplay:vn","protagonist:male"]
label alt_sprites_test:
    python:
        normal_sprites_list = []
        close_sprites_list = []
        far_sprites_list = []
        custom_sprites_list = []
        normal_sprites_full_list = []
        close_sprites_full_list = []
        far_sprites_full_list = []
        custom_sprites_full_list = []
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
                                                        if not (who_num + ' ' + emo + ' ' + clothes + ' ' + acc in bl_sprites_list):
                                                            normal_sprites_list.append(who_num + ' ' + emo + ' ' + clothes + ' ' + acc)
                                                        else:
                                                            normal_sprites_full_list.append(who_num + ' ' + emo + ' ' + clothes + ' ' + acc)
                                                        if not (who_num + ' ' + emo + ' ' + clothes + ' ' + acc + ' close' in bl_sprites_list):
                                                            close_sprites_list.append(who_num + ' ' + emo + ' ' + clothes + ' ' + acc + ' close')
                                                        else:
                                                            close_sprites_full_list.append(who_num + ' ' + emo + ' ' + clothes + ' ' + acc + ' close')
                                                    else:
                                                        if not (who_num + ' ' + emo + ' ' + clothes in bl_sprites_list):
                                                            normal_sprites_list.append(who_num + ' ' + emo + ' ' + clothes)
                                                        else:
                                                            normal_sprites_full_list.append(who_num + ' ' + emo + ' ' + clothes)
                                                        if not (who_num + ' ' + emo + ' ' + clothes + ' close' in bl_sprites_list):
                                                            close_sprites_list.append(who_num + ' ' + emo + ' ' + clothes + ' close')
                                                        else:
                                                            close_sprites_full_list.append(who_num + ' ' + emo + ' ' + clothes + ' close')
                                            elif clothes == 'body':
                                                if emo != '':
                                                    if acc != '':
                                                        if not (who_num + ' ' + emo + ' ' + 'body' + ' ' + acc in bl_sprites_list):
                                                            normal_sprites_list.append(who_num + ' ' + emo + ' ' + 'body' + ' ' + acc)
                                                        else:
                                                            normal_sprites_full_list.append(who_num + ' ' + emo + ' ' + 'body' + ' ' + acc)
                                                        if not (who_num + ' ' + emo + ' ' + 'body' + ' ' + acc + ' close' in bl_sprites_list):
                                                            close_sprites_list.append(who_num + ' ' + emo + ' ' + 'body' + ' ' + acc + ' close')
                                                        else:
                                                            close_sprites_full_list.append(who_num + ' ' + emo + ' ' + 'body' + ' ' + acc + ' close')
                                                    else:
                                                        if not (who_num + ' ' + emo + ' ' + 'body' in bl_sprites_list):
                                                            normal_sprites_list.append(who_num + ' ' + emo + ' ' + 'body')
                                                        else:
                                                            normal_sprites_full_list.append(who_num + ' ' + emo + ' ' + 'body')
                                                        if not (who_num + ' ' + emo + ' ' + 'body' + ' close' in bl_sprites_list):
                                                            close_sprites_list.append(who_num + ' ' + emo + ' ' + 'body' + ' close')
                                                        else:
                                                            close_sprites_full_list.append(who_num + ' ' + emo + ' ' + 'body' + ' close')
                                            else:
                                                if emo != '':
                                                    if acc != '':
                                                        if who == 'cs':
                                                            if not (who_num + ' ' + emo + ' ' + acc in bl_sprites_list):
                                                                normal_sprites_list.append(who_num + ' ' + emo + ' ' + acc)
                                                            else:
                                                                normal_sprites_full_list.append(who_num + ' ' + emo + ' ' + acc)
                                                            if not (who_num + ' ' + emo + ' ' + acc + ' close' in bl_sprites_list):
                                                                close_sprites_list.append(who_num + ' ' + emo + ' ' + acc + ' close')
                                                            else:
                                                                close_sprites_full_list.append(who_num + ' ' + emo + ' ' + acc + ' close')
                                                        else:
                                                            if not (who_num + ' ' + emo + ' ' + 'pioneer' + ' ' + acc in bl_sprites_list):
                                                                normal_sprites_list.append(who_num + ' ' + emo + ' ' + 'pioneer' + ' ' + acc)
                                                            else:
                                                                normal_sprites_full_list.append(who_num + ' ' + emo + ' ' + 'pioneer' + ' ' + acc)
                                                            if not (who_num + ' ' + emo + ' ' + 'pioneer' + ' ' + acc + ' close' in bl_sprites_list):
                                                                close_sprites_list.append(who_num + ' ' + emo + ' ' + 'pioneer' + ' ' + acc + ' close')
                                                            else:
                                                                close_sprites_full_list.append(who_num + ' ' + emo + ' ' + 'pioneer' + ' ' + acc + ' close')
                                                    else:
                                                        if who == 'cs':
                                                            if not (who_num + ' ' + emo in bl_sprites_list):
                                                                normal_sprites_list.append(who_num + ' ' + emo)
                                                            else:
                                                                normal_sprites_full_list.append(who_num + ' ' + emo)
                                                            if not (who_num + ' ' + emo + ' close' in bl_sprites_list):
                                                                close_sprites_list.append(who_num + ' ' + emo + ' close')
                                                            else:
                                                                close_sprites_full_list.append(who_num + ' ' + emo + ' close')
                                                        else:
                                                            if not (who_num + ' ' + emo + ' ' + 'pioneer' in bl_sprites_list):
                                                                normal_sprites_list.append(who_num + ' ' + emo + ' ' + 'pioneer')
                                                            else:
                                                                normal_sprites_full_list.append(who_num + ' ' + emo + ' ' + 'pioneer')
                                                            if not (who_num + ' ' + emo + ' ' + 'pioneer' + ' close' in bl_sprites_list):
                                                                close_sprites_list.append(who_num + ' ' + emo + ' ' + 'pioneer' + ' close')
                                                            else:
                                                                close_sprites_full_list.append(who_num + ' ' + emo + ' ' + 'pioneer' + ' close')
                                        else:
                                            who_num = who
                                            if emo != '':
                                                if acc != '':
                                                    if not (who_num + ' ' + emo + ' ' + clothes + ' ' + acc in bl_sprites_list):
                                                        normal_sprites_list.append(who_num + ' ' + emo + ' ' + clothes + ' ' + acc)
                                                    else:
                                                        normal_sprites_full_list.append(who_num + ' ' + emo + ' ' + clothes + ' ' + acc)
                                                    if not (who_num + ' ' + emo + ' ' + clothes + ' ' + acc + ' close' in bl_sprites_list):
                                                        close_sprites_list.append(who_num + ' ' + emo + ' ' + clothes + ' ' + acc + ' close')
                                                    else:
                                                        close_sprites_full_list.append(who_num + ' ' + emo + ' ' + clothes + ' ' + acc + ' close')
                                                else:
                                                    if not (who_num + ' ' + emo + ' ' + clothes in bl_sprites_list):
                                                        normal_sprites_list.append(who_num + ' ' + emo + ' ' + clothes)
                                                    else:
                                                        normal_sprites_full_list.append(who_num + ' ' + emo + ' ' + clothes)
                                                    if not (who_num + ' ' + emo + ' ' + clothes + ' close' in bl_sprites_list):
                                                        close_sprites_list.append(who_num + ' ' + emo + ' ' + clothes + ' close')
                                                    else:
                                                        close_sprites_full_list.append(who_num + ' ' + emo + ' ' + clothes + ' close')
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
                                                        if not (who_num + ' ' + emo + ' ' + clothes + ' ' + acc + ' far' in bl_sprites_list):
                                                            far_sprites_list.append(who_num + ' ' + emo + ' ' + clothes + ' ' + acc + ' far')
                                                        else:
                                                            far_sprites_full_list.append(who_num + ' ' + emo + ' ' + clothes + ' ' + acc + ' far')
                                                    else:
                                                        if not (who_num + ' ' + emo + ' ' + clothes + ' far' in bl_sprites_list):
                                                            far_sprites_list.append(who_num + ' ' + emo + ' ' + clothes + ' far')
                                                        else:
                                                            far_sprites_full_list.append(who_num + ' ' + emo + ' ' + clothes + ' far')
                                            elif clothes == 'body':
                                                if emo != '':
                                                    if acc != '':
                                                        if not (who_num + ' ' + emo + ' ' + 'body' + ' ' + acc + ' far' in bl_sprites_list):
                                                            far_sprites_list.append(who_num + ' ' + emo + ' ' + 'body' + ' ' + acc + ' far')
                                                        else:
                                                            far_sprites_full_list.append(who_num + ' ' + emo + ' ' + 'body' + ' ' + acc + ' far')
                                                    else:
                                                        if not (who_num + ' ' + emo + ' ' + 'body' + ' far' in bl_sprites_list):
                                                            far_sprites_list.append(who_num + ' ' + emo + ' ' + 'body' + ' far')
                                                        else:
                                                            far_sprites_full_list.append(who_num + ' ' + emo + ' ' + 'body' + ' far')
                                            else:
                                                if emo != '':
                                                    if acc != '':
                                                        if who == 'cs':
                                                            if not (who_num + ' ' + emo + ' ' + acc + ' far' in bl_sprites_list):
                                                                far_sprites_list.append(who_num + ' ' + emo + ' ' + acc + ' far')
                                                            else:
                                                                far_sprites_full_list.append(who_num + ' ' + emo + ' ' + acc + ' far')
                                                        else:
                                                            if not (who_num + ' ' + emo + ' ' + 'pioneer' + ' ' + acc + ' far' in bl_sprites_list):
                                                                far_sprites_list.append(who_num + ' ' + emo + ' ' + 'pioneer' + ' ' + acc + ' far')
                                                            else:
                                                                far_sprites_full_list.append(who_num + ' ' + emo + ' ' + 'pioneer' + ' ' + acc + ' far')
                                                    else:
                                                        if who == 'cs':
                                                            if not (who_num + ' ' + emo + ' far' in bl_sprites_list):
                                                                far_sprites_list.append(who_num + ' ' + emo + ' far')
                                                            else:
                                                                far_sprites_full_list.append(who_num + ' ' + emo + ' far')
                                                        else:
                                                            if not (who_num + ' ' + emo + ' ' + 'pioneer' + ' far' in bl_sprites_list):
                                                                far_sprites_list.append(who_num + ' ' + emo + ' ' + 'pioneer' + ' far')
                                                            else:
                                                                far_sprites_full_list.append(who_num + ' ' + emo + ' ' + 'pioneer' + ' far')
                                        else:
                                            who_num = who
                                            if emo != '':
                                                if acc != '':
                                                    if not (who_num + ' ' + emo + ' ' + clothes + ' ' + acc + ' far' in bl_sprites_list):
                                                        far_sprites_list.append(who_num + ' ' + emo + ' ' + clothes + ' ' + acc + ' far')
                                                    else:
                                                        far_sprites_full_list.append(who_num + ' ' + emo + ' ' + clothes + ' ' + acc + ' far')
                                                else:
                                                    if not (who_num + ' ' + emo + ' ' + clothes + ' far' in bl_sprites_list):
                                                        far_sprites_list.append(who_num + ' ' + emo + ' ' + clothes + ' far')
                                                    else:
                                                        far_sprites_full_list.append(who_num + ' ' + emo + ' ' + clothes + ' far')
        for custom in alt_custom_list:
            if 'far' in custom:
                if not (custom in bl_sprites_list):
                    custom_sprites_list.append(custom)
                else:
                    custom_sprites_full_list.append(custom)
            else:
                if not (custom in bl_sprites_list):
                    custom_sprites_list.append(custom)
                else:
                    custom_sprites_full_list.append(custom)
    menu:
        "normal":
            python:
                filter1 = renpy.input("Фильтр 1")
                filter2 = renpy.input("Фильтр 2")
                for x in normal_sprites_list:
                    if (filter1 in x) and (filter2 in x):
                        renpy.show(x)
                        ui.button(clicked=None, xcenter=0.5, ycenter=0.8)
                        ui.text(x, style="button_text", size=30)
                        renpy.pause(600)
                        renpy.hide(x)
        "close":
            python:
                filter1 = renpy.input("Фильтр 1")
                filter2 = renpy.input("Фильтр 2")
                for x in close_sprites_list:
                    if (filter1 in x) and (filter2 in x):
                        renpy.show(x)
                        ui.button(clicked=None, xcenter=0.5, ycenter=0.8)
                        ui.text(x, style="button_text", size=30)
                        renpy.pause(600)
                        renpy.hide(x)
        "far":
            python:
                filter1 = renpy.input("Фильтр 1")
                filter2 = renpy.input("Фильтр 2")
                for x in far_sprites_list:
                    if (filter1 in x) and (filter2 in x):
                        renpy.show(x)
                        ui.button(clicked=None, xcenter=0.5, ycenter=0.8)
                        ui.text(x, style="button_text", size=30)
                        renpy.pause(600)
                        renpy.hide(x)
        "custom":
            python:
                filter1 = renpy.input("Фильтр 1")
                filter2 = renpy.input("Фильтр 2")
                for x in custom_sprites_list:
                    if (filter1 in x) and (filter2 in x):
                        renpy.show(x)
                        ui.button(clicked=None, xcenter=0.5, ycenter=0.8)
                        ui.text(x, style="button_text", size=30)
                        renpy.pause(600)
                        renpy.hide(x)
        "test all":
            python:
                for x in normal_sprites_list:
                    renpy.show(x)
                    renpy.pause(.01)
                    renpy.hide(x)
                for x in close_sprites_list:
                    renpy.show(x)
                    renpy.pause(.01)
                    renpy.hide(x)
                for x in far_sprites_list:
                    renpy.show(x)
                    renpy.pause(.01)
                    renpy.hide(x)
                for x in custom_sprites_list:
                    renpy.show(x)
                    renpy.pause(.01)
                    renpy.hide(x)
    jump alt_sprites_test