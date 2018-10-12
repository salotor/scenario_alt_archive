python early:
    def alt_recalculation_function_x(old_pos):
        return int(old_pos*1920/1920)
    
    def alt_recalculation_function_y(old_pos):
        return int(old_pos*1080/1080)
        
init 300 python:
    alt_images = default_7dl_path + "Pics/sprites/"
    bl_images = "game/images/sprites/"
    
    alt_body_list = {
                    'dv':{'1':['ori_body','7dl_body2'],
                          '2':['ori_body','7dl_body2'],
                          '3':['ori_body','7dl_body2'],
                          '4':['ori_body','7dl_body2'],
                          '5':['ori_body','7dl_body2']}
        }
    alt_clothes_list = {
                    'dv':{'1':['ori_pioneer','ori_pioneer2','ori_swim','7dl_dress','7dl_sport'],
                          '2':['ori_pioneer','ori_pioneer2','ori_swim','7dl_sport'],
                          '3':['ori_pioneer','ori_pioneer2','7dl_dress','7dl_sport'],
                          '4':['ori_pioneer','ori_pioneer2','ori_swim','7dl_dress','7dl_sport','7dl_dress_pregnant','7dl_winter'],
                          '5':['ori_pioneer','ori_pioneer2','7dl_sport']}
        }
    alt_emo_list = {
                    'dv':{'1':['ori_cry','ori_scared','ori_shocked','ori_surprise'],
                          '2':['ori_grin'],
                          '3':['ori_guilty','ori_sad','ori_shy'],
                          '4':['ori_laugh','ori_normal','ori_smile','7dl_soft_smile'],
                          '5':['ori_angry','ori_rage']}
        }
    alt_acc_list = {
        }
    
    alt_dist = ['normal/']
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
                                        if body[0:2] == 'ori':
                                            body_path = bl_images + dist + who + '/' + who + '_' + num + '_' + body[4:len(body)] + '.png'
                                        elif body[0:2] == '7dl':
                                            body_path = alt_images + dist + who + '/' + who + '_' + num + '_' + body[4:len(body)] + '.png'
                                        if clothes[0:2] == 'ori':
                                            clothes_path = bl_images + dist + who + '/' + who + '_' + num + '_' + clothes[4:len(clothes)] + '.png'
                                        elif clothes[0:2] == '7dl':
                                            clothes_path = alt_images + dist + who + '/' + who + '_' + num + '_' + clothes[4:len(clothes)] + '.png'
                                        if emo[0:2] == 'ori':
                                            emo_path = bl_images + dist + who + '/' + who + '_' + num + '_' + emo[4:len(emo)] + '.png'
                                        elif emo[0:2] == '7dl':
                                            emo_path = alt_images + dist + who + '/' + who + '_' + num + '_' + emo[4:len(emo)] + '.png'
                                        if acc[0:2] == 'ori':
                                            acc_path = bl_images + dist + who + '/' + who + '_' + num + '_' + acc[4:len(acc)] + '.png'
                                        elif acc[0:2] == '7dl':
                                            acc_path = alt_images + dist + who + '/' + who + '_' + num + '_' + acc[4:len(acc)] + '.png'
                                        renpy.image(who_num + ' ' + emo[4:len(emo)] + ' ' + clothes[4:len(clothes)] + ' ' + acc[4:len(acc)],
                                                            ConditionSwitch("persistent.sprite_time=='sunset'",
                                                            im.MatrixColor(im.Composite((alt_recalculation_function_x(900),alt_recalculation_function_y(1080)),
                                                            (0, 0), body_path,
                                                            (0, 0), clothes_path,
                                                            (0, 0), emo_path,
                                                            (0, 0), acc_path),
                                                            im.matrix.tint(0.94, 0.82, 1.0) ),
    
                                                            "persistent.sprite_time=='night'",
                                                            im.MatrixColor(im.Composite((alt_recalculation_function_x(900),alt_recalculation_function_y(1080)),
                                                            (0, 0), body_path,
                                                            (0, 0), clothes_path,
                                                            (0, 0), emo_path,
                                                            (0, 0), acc_path),
                                                            im.matrix.tint(0.63, 0.78, 0.82) ),
    
                                                            True,
                                                            im.Composite((alt_recalculation_function_x(900),alt_recalculation_function_y(1080)),
                                                            (0, 0), body_path,
                                                            (0, 0), clothes_path,
                                                            (0, 0), emo_path,
                                                            (0, 0), acc_path), )
                                                            )
                                else:
                                    if 'body2' in body:
                                        who_num = who + '2'
                                    if body[0:2] == 'ori':
                                        body_path = bl_images + dist + who + '/' + who + '_' + num + '_' + body[4:len(body)] + '.png'
                                    elif body[0:2] == '7dl':
                                        body_path = alt_images + dist + who + '/' + who + '_' + num + '_' + body[4:len(body)] + '.png'
                                    if clothes[0:2] == 'ori':
                                        clothes_path = bl_images + dist + who + '/' + who + '_' + num + '_' + clothes[4:len(clothes)] + '.png'
                                    elif clothes[0:2] == '7dl':
                                        clothes_path = alt_images + dist + who + '/' + who + '_' + num + '_' + clothes[4:len(clothes)] + '.png'
                                    if emo[0:2] == 'ori':
                                        emo_path = bl_images + dist + who + '/' + who + '_' + num + '_' + emo[4:len(emo)] + '.png'
                                    elif emo[0:2] == '7dl':
                                        emo_path = alt_images + dist + who + '/' + who + '_' + num + '_' + emo[4:len(emo)] + '.png'
                                    renpy.image(who_num + ' ' + emo[4:len(emo)] + ' ' + clothes[4:len(clothes)],
                                                        ConditionSwitch("persistent.sprite_time=='sunset'",
                                                        im.MatrixColor(im.Composite((alt_recalculation_function_x(900),alt_recalculation_function_y(1080)),
                                                        (0, 0), body_path,
                                                        (0, 0), clothes_path,
                                                        (0, 0), emo_path),
                                                        im.matrix.tint(0.94, 0.82, 1.0) ),

                                                        "persistent.sprite_time=='night'",
                                                        im.MatrixColor(im.Composite((alt_recalculation_function_x(900),alt_recalculation_function_y(1080)),
                                                        (0, 0), body_path,
                                                        (0, 0), clothes_path,
                                                        (0, 0), emo_path),
                                                        im.matrix.tint(0.63, 0.78, 0.82) ),

                                                        True,
                                                        im.Composite((alt_recalculation_function_x(900),alt_recalculation_function_y(1080)),
                                                        (0, 0), body_path,
                                                        (0, 0), clothes_path,
                                                        (0, 0), emo_path), )
                                                        )     
