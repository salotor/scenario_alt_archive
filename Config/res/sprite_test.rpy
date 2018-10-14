label alt_test:
    python:
        for dist in alt_dist:
            if dist == "normal/":
                for who in alt_body_list.keys():
                    for pose in alt_body_list[who]:
                        for body in alt_body_list[who][pose]:
                            for clothes in alt_clothes_list[who][pose]:
                                for emo in alt_emo_list[who][pose]:
                                    for acc in alt_acc_list[who][pose]:
                                        if body != None:
                                            if 'body2' in body:
                                                who_num = who + '2'
                                            elif 'body' in body:
                                                who_num = who
                                            if clothes != 'body':
                                                if emo != None:
                                                    if acc != None:
                                                        renpy.show(who_num + ' ' + emo + ' ' + clothes + ' ' + acc)
                                                        renpy.pause(0.5)
                                                        renpy.hide(who_num + ' ' + emo + ' ' + clothes + ' ' + acc)
                                                        renpy.show(who_num + ' ' + emo + ' ' + clothes + ' ' + acc + ' close')
                                                        renpy.pause(0.5)
                                                        renpy.hide(who_num + ' ' + emo + ' ' + clothes + ' ' + acc + ' close')
                                                    else:
                                                        renpy.show(who_num + ' ' + emo + ' ' + clothes)
                                                        renpy.pause(0.5)
                                                        renpy.hide(who_num + ' ' + emo + ' ' + clothes)
                                                        renpy.show(who_num + ' ' + emo + ' ' + clothes + ' close')
                                                        renpy.pause(0.5)
                                                        renpy.hide(who_num + ' ' + emo + ' ' + clothes + ' close')
                                            else:
                                                if emo != None:
                                                    if acc != None:
                                                        renpy.show(who_num + ' ' + emo + ' ' + 'body' + ' ' + acc)
                                                        renpy.pause(0.5)
                                                        renpy.hide(who_num + ' ' + emo + ' ' + 'body' + ' ' + acc)
                                                        renpy.show(who_num + ' ' + emo + ' ' + 'body' + ' ' + acc + ' close')
                                                        renpy.pause(0.5)
                                                        renpy.hide(who_num + ' ' + emo + ' ' + 'body' + ' ' + acc + ' close')
                                                    else:
                                                        renpy.show(who_num + ' ' + emo + ' ' + 'body')
                                                        renpy.pause(0.5)
                                                        renpy.hide(who_num + ' ' + emo + ' ' + 'body')
                                                        renpy.show(who_num + ' ' + emo + ' ' + 'body' + ' close')
                                                        renpy.pause(0.5)
                                                        renpy.hide(who_num + ' ' + emo + ' ' + 'body' + ' close')
                                        else:
                                            who_num = who
                                            if emo != None:
                                                if acc != None:
                                                    renpy.show(who_num + ' ' + emo + ' ' + clothes + ' ' + acc)
                                                    renpy.pause(0.5)
                                                    renpy.hide(who_num + ' ' + emo + ' ' + clothes + ' ' + acc)
                                                    renpy.show(who_num + ' ' + emo + ' ' + clothes + ' ' + acc + ' close')
                                                    renpy.pause(0.5)
                                                    renpy.hide(who_num + ' ' + emo + ' ' + clothes + ' ' + acc + ' close')
                                                else:
                                                    renpy.show(who_num + ' ' + emo + ' ' + clothes)
                                                    renpy.pause(0.5)
                                                    renpy.hide(who_num + ' ' + emo + ' ' + clothes)
                                                    renpy.show(who_num + ' ' + emo + ' ' + clothes + ' close')
                                                    renpy.pause(0.5)
                                                    renpy.hide(who_num + ' ' + emo + ' ' + clothes + ' close')
