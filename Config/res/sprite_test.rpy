label alt_test:
    python:
        for dist in alt_dist:
            if dist == "normal/":
                for who in alt_body_list.keys():
                    for num in alt_body_list[who]:
                        for body in alt_body_list[who][num]:
                            for clothes in alt_clothes_list[who][num]:
                                for emo in alt_emo_list[who][num]:
                                    if alt_acc_list[who][num]:
                                        for acc in alt_acc_list[who][num]:
                                            if 'body2' in body:
                                                who_num = who + '2'
                                            elif 'body' in body:
                                                who_num = who
                                            renpy.show(who_num + ' ' + emo + ' ' + clothes + ' ' + acc)
                                    else:
                                        if 'body2' in body:
                                            who_num = who + '2'
                                        elif 'body' in body:
                                            who_num = who
                                        renpy.show(who_num + ' ' + emo + ' ' + clothes)
                                    renpy.pause(1.0)
                                    renpy.hide(who_num + ' ' + emo + ' ' + clothes)
