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
                                            body_path = bl_images + dist + who + '/' + who + '_' + num + '_' + body[4:len(emo)]
                                        elif body[0:2] == 'ori':
                                        renpy.image(who_num + ' ' + emo[4:len(emo)] + ' ' + clothes[4:len(clothes)] + ' ' + acc[4:len(acc)],
                                                            ConditionSwitch("persistent.sprite_time=='sunset'",
                                                            im.MatrixColor(im.Composite((alt_recalculation_function_x(900),alt_recalculation_function_y(1080)),
                                                            (0, 0), body,
                                                            (0, 0), clothes,
                                                            (0, 0), emo,
                                                            (0, 0), acc),
                                                            im.matrix.tint(0.94, 0.82, 1.0) ),
    
                                                            "persistent.sprite_time=='night'",
                                                            im.MatrixColor(im.Composite((alt_recalculation_function_x(900),alt_recalculation_function_y(1080)),
                                                            (0, 0), body,
                                                            (0, 0), clothes,
                                                            (0, 0), emo,
                                                            (0, 0), acc),
                                                            im.matrix.tint(0.63, 0.78, 0.82) ),
    
                                                            True,
                                                            im.Composite((alt_recalculation_function_x(900),alt_recalculation_function_y(1080)),
                                                            (0, 0), body,
                                                            (0, 0), clothes,
                                                            (0, 0), emo,
                                                            (0, 0), acc), )
                                                            )
                                
                                renpy.image('alt_'+who + ' ' + emo[len(alt_images)+21:-4] + ' ' + clothes[len(alt_images)+25:-4],
                                                ConditionSwitch("persistent.sprite_time=='sunset'",
                                                im.MatrixColor(im.Composite((alt_recalculation_function_x(900),alt_recalculation_function_y(1080)),
                                                (0, 0), body,
                                                (0, 0), clothes,
                                                (0, 0), emo),
                                                im.matrix.tint(0.94, 0.82, 1.0) ),
    
                                                "persistent.sprite_time=='night'",
                                                im.MatrixColor(im.Composite((alt_recalculation_function_x(900),alt_recalculation_function_y(1080)),
                                                (0, 0), body,
                                                (0, 0), clothes,
                                                (0, 0), emo),
                                                im.matrix.tint(0.63, 0.78, 0.82) ),
    
                                                True,
                                                im.Composite((alt_recalculation_function_x(900),alt_recalculation_function_y(1080)),
                                                (0, 0), body,
                                                (0, 0), clothes,
                                                (0, 0), emo),
                                                )
                                                )
                
                alt_emo_list = {}
                alt_body_list = {}
                alt_clothes_list = {}
                alt_acc_list = {}
        
        elif dist == "far/":
            for who in alt_spr_list_far.keys():
                for num in alt_spr_list_far[who]:
                    for file in renpy.list_files():
                        if file.startswith(alt_images + dist + who + '/' + num + '/'):
                            if "body" in file and file not in body:
                                body.append(file)
                            
                            if "clothes" in file and file not in clothes:
                                clothes.append(file)
                            
                            if "emo" in file and file not in emo:
                                emo.append(file)
                            
                            if 'acc/' in file:
                                acc.append(file)
                    
                    alt_body_list[num] = body
                    alt_clothes_list[num] = clothes
                    alt_emo_list[num] = emo
                    
                    if acc:
                        alt_acc_list[num] = acc
                    else:
                        alt_acc_list[num] = []
                    
                    body = []
                    clothes = []
                    emo = []
                    acc = []
                
                for num in alt_spr_list[who]:
                    for body in alt_body_list[num]:
                        for clothes in alt_clothes_list[num]:
                            for emo in alt_emo_list[num]:
                                if alt_acc_list[num]:
                                    for acc in alt_acc_list[num]:
                                        renpy.image('alt_'+who + ' ' + emo[len(alt_images)+18:-4] + ' ' + clothes[len(alt_images)+22:-4] + ' ' + acc[len(alt_images)+18:-4] + " far",
                                                            ConditionSwitch("persistent.sprite_time=='sunset'",
                                                            im.MatrixColor(im.Composite((alt_recalculation_function_x(900),alt_recalculation_function_y(1080)),
                                                            (0, 0), body,
                                                            (0, 0), clothes,
                                                            (0, 0), emo,
                                                            (0, 0), acc),
                                                            im.matrix.tint(0.94, 0.82, 1.0) ),
    
                                                            "persistent.sprite_time=='night'",
                                                            im.MatrixColor(im.Composite((alt_recalculation_function_x(900),alt_recalculation_function_y(1080)),
                                                            (0, 0), body,
                                                            (0, 0), clothes,
                                                            (0, 0), emo,
                                                            (0, 0), acc),
                                                            im.matrix.tint(0.63, 0.78, 0.82) ),
    
                                                            True,
                                                            im.Composite((alt_recalculation_function_x(900),alt_recalculation_function_y(1080)),
                                                            (0, 0), body,
                                                            (0, 0), clothes,
                                                            (0, 0), emo,
                                                            (0, 0), acc), )
                                                            )
                                
                                renpy.image('alt_'+who + ' ' + emo[len(alt_images)+18:-4] + ' ' + clothes[len(alt_images)+22:-4] + " far",
                                                ConditionSwitch("persistent.sprite_time=='sunset'",
                                                im.MatrixColor(im.Composite((alt_recalculation_function_x(900),alt_recalculation_function_y(1080)),
                                                (0, 0), body,
                                                (0, 0), clothes,
                                                (0, 0), emo),
                                                im.matrix.tint(0.94, 0.82, 1.0) ),
    
                                                "persistent.sprite_time=='night'",
                                                im.MatrixColor(im.Composite((alt_recalculation_function_x(900),alt_recalculation_function_y(1080)),
                                                (0, 0), body,
                                                (0, 0), clothes,
                                                (0, 0), emo),
                                                im.matrix.tint(0.63, 0.78, 0.82) ),
    
                                                True,
                                                im.Composite((alt_recalculation_function_x(900),alt_recalculation_function_y(1080)),
                                                (0, 0), body,
                                                (0, 0), clothes,
                                                (0, 0), emo),
                                                )
                                                )
                
                alt_emo_list = {}
                alt_body_list = {}
                alt_clothes_list = {}
                alt_acc_list = {}
    
    for f in renpy.list_files():
        if f.startswith('alt/images/'):
            for fold in ('bg','cg'):
                renpy.image('alt_'+fold+' '+f[len('alt/images/')+3:-(len(f.split('.')[-1])+1)],f)
