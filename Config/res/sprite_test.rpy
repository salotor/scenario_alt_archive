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
                                        if 'body2' in body:
                                            who_num = who + '2'
                                        elif 'body' in body:
                                            who_num = who
                                        if clothes == '':
                                            clothes = 'body'
                                    renpy.show(who_num + ' ' + emo + ' ' + clothes + ' ' + acc, at_list=[left]) 
                                    renpy.pause(1.0)
                                    renpy.hide(who_num + ' ' + emo + ' ' + clothes + ' ' + acc) 
                                    renpy.show(who_num + ' ' + emo + ' ' + clothes + ' ' + acc + ' ' + 'close', at_list=[right])
                                    renpy.pause(1.0)
                                    renpy.hide(who_num + ' ' + emo + ' ' + clothes + ' ' + acc + ' ' + 'close')
