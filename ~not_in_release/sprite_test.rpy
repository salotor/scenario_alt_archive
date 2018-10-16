label alt_test:
    python:
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
                                                        renpy.show(who_num + ' ' + emo + ' ' + clothes + ' ' + acc)
                                                        renpy.show(who_num + ' ' + emo + ' ' + clothes + ' ' + acc + ' close')
                                                    else:
                                                        renpy.show(who_num + ' ' + emo + ' ' + clothes)
                                                        renpy.show(who_num + ' ' + emo + ' ' + clothes + ' close')
                                            elif clothes == 'body':
                                                if emo != '':
                                                    if acc != '':
                                                        renpy.show(who_num + ' ' + emo + ' ' + 'body' + ' ' + acc)
                                                        renpy.show(who_num + ' ' + emo + ' ' + 'body' + ' ' + acc + ' close')
                                                    else:
                                                        renpy.show(who_num + ' ' + emo + ' ' + 'body')
                                                        renpy.show(who_num + ' ' + emo + ' ' + 'body' + ' close')
                                            else:
                                                if emo != '':
                                                    if acc != '':
                                                        if who == 'cs':
                                                            renpy.show(who_num + ' ' + emo + ' ' + acc)
                                                            renpy.show(who_num + ' ' + emo + ' ' + acc + ' close')
                                                        else:
                                                            renpy.show(who_num + ' ' + emo + ' ' + 'pioneer' + ' ' + acc)
                                                            renpy.show(who_num + ' ' + emo + ' ' + 'pioneer' + ' ' + acc + ' close')
                                                    else:
                                                        renpy.show(who_num + ' ' + emo + ' ' + 'body')
                                                        renpy.show(who_num + ' ' + emo + ' ' + 'body' + ' close')
                                        else:
                                            who_num = who
                                            if emo != '':
                                                if acc != '':
                                                    renpy.show(who_num + ' ' + emo + ' ' + clothes + ' ' + acc)
                                                    renpy.show(who_num + ' ' + emo + ' ' + clothes + ' ' + acc + ' close')
                                                else:
                                                    renpy.show(who_num + ' ' + emo + ' ' + clothes)
                                                    renpy.show(who_num + ' ' + emo + ' ' + clothes + ' close')
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
                                                        renpy.show(who_num + ' ' + emo + ' ' + clothes + ' ' + acc + ' far')
                                                    else:
                                                        renpy.show(who_num + ' ' + emo + ' ' + clothes + ' far')
                                            elif clothes == 'body':
                                                if emo != '':
                                                    if acc != '':
                                                        renpy.show(who_num + ' ' + emo + ' ' + 'body' + ' ' + acc + ' far')
                                                    else:
                                                        renpy.show(who_num + ' ' + emo + ' ' + 'body' + ' far')
                                            else:
                                                if emo != '':
                                                    if acc != '':
                                                        if who == 'cs':
                                                            renpy.show(who_num + ' ' + emo + ' ' + acc + ' far')
                                                        else:
                                                            renpy.show(who_num + ' ' + emo + ' ' + 'pioneer' + ' ' + acc + ' far')
                                                    else:
                                                        if who == 'cs':
                                                            renpy.show(who_num + ' ' + emo + ' far')
                                                        else:
                                                            renpy.show(who_num + ' ' + emo + ' ' + 'pioneer' + ' far')
                                        else:
                                            who_num = who
                                            if emo != '':
                                                if acc != '':
                                                    renpy.show(who_num + ' ' + emo + ' ' + clothes + ' ' + acc + ' far')
                                                else:
                                                    renpy.show(who_num + ' ' + emo + ' ' + clothes + ' far')
        for custom in alt_custom_list:
            if 'far' in custom:
                renpy.show(custom)
            else:
                renpy.show(custom)