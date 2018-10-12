python early:
    def alt_recalculation_function_x(old_pos):
        return int(old_pos*1920/1920)
    
    def alt_recalculation_function_y(old_pos):
        return int(old_pos*1080/1080)
        
init 300 python:
    alt_images = default_7dl_path + "Pics/sprites/"
    bl_images = "images/sprites/"
    
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
                    'dv':{'1':[],
                          '2':[],
                          '3':[],
                          '4':[],
                          '5':[]}
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
                                        elif 'body' in body:
                                            who_num = who
                                        if body[:3] == 'ori':
                                            body_path = bl_images + dist + who + '/' + who + '_' + num + '_' + body[4:] + '.png'
                                        elif body[:3] == '7dl':
                                            body_path = alt_images + dist + who + '/' + who + '_' + num + '_' + body[4:] + '.png'
                                        if clothes[:3] == 'ori':
                                            clothes_path = bl_images + dist + who + '/' + who + '_' + num + '_' + clothes[4:] + '.png'
                                        elif clothes[:3] == '7dl':
                                            clothes_path = alt_images + dist + who + '/' + who + '_' + num + '_' + clothes[4:] + '.png'
                                        if emo[:3] == 'ori':
                                            emo_path = bl_images + dist + who + '/' + who + '_' + num + '_' + emo[4:] + '.png'
                                        elif emo[:3] == '7dl':
                                            emo_path = alt_images + dist + who + '/' + who + '_' + num + '_' + emo[4:] + '.png'
                                        if acc[:3] == 'ori':
                                            acc_path = bl_images + dist + who + '/' + who + '_' + num + '_' + acc[4:] + '.png'
                                        elif acc[:3] == '7dl':
                                            acc_path = alt_images + dist + who + '/' + who + '_' + num + '_' + acc[4:] + '.png'
                                        renpy.image(who_num + ' ' + emo[4:] + ' ' + clothes[4:] + ' ' + acc[4:],
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
                                    elif 'body' in body:
                                        who_num = who
                                    if body[:3] == 'ori':
                                        body_path = bl_images + dist + who + '/' + who + '_' + num + '_' + body[4:] + '.png'
                                    elif body[:3] == '7dl':
                                        body_path = alt_images + dist + who + '/' + who + '_' + num + '_' + body[4:] + '.png'
                                    if clothes[:3] == 'ori':
                                        clothes_path = bl_images + dist + who + '/' + who + '_' + num + '_' + clothes[4:] + '.png'
                                    elif clothes[:3] == '7dl':
                                        clothes_path = alt_images + dist + who + '/' + who + '_' + num + '_' + clothes[4:] + '.png'
                                    if emo[:3] == 'ori':
                                        emo_path = bl_images + dist + who + '/' + who + '_' + num + '_' + emo[4:] + '.png'
                                    elif emo[:3] == '7dl':
                                        emo_path = alt_images + dist + who + '/' + who + '_' + num + '_' + emo[4:] + '.png'
                                    renpy.image(who_num + ' ' + emo[4:] + ' ' + clothes[4:],
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
