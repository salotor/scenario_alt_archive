transform close_sprites:
    zoom 1.25
    yoffset 238
    xoffset 38
    
init 9999 python:
    alt_sprites = default_7dl_path + "Pics/sprites/"
    if renpy.version(tuple=False) == "Ren'Py 6.16.3.502":
        bl_sprites = "images/1080/sprites/"
    else:
        bl_sprites = "images/sprites/"
        
    alt_body_dict = {
                    'al':{'1':['']},
                    'ba':{'1':['body']},
                    'dn':{'1':[''],
                          '2':[''],
                          '3':['']},
                    'cs':{'1':['body']},
                    'dv':{'1':['body','body2'],
                          '2':['body','body2'],
                          '3':['body','body2'],
                          '4':['body','body2'],
                          '5':['body','body2']},
                    'el':{'1':['body'],
                          '2':['body'],
                          '3':['body']},
                    'ln':{'1':['body'],
                          '2':['body'],
                          '3':['body']},
                    'mi':{'1':['body'],
                          '2':['body'],
                          '3':['body']},
                    'mt':{'1':['body','body2'],
                          '2':['body'],
                          '3':['body']},
                    'mz':{'1':['body'],
                          '2':['body'],
                          '3':['body']},
                    'sak':{'1':[''],
                           '2':[''],
                           '3':['']},
                    'sh':{'1':['body'],
                          '2':['body'],
                          '3':['body']},
                    'sl':{'1':['body','body2'],
                          '2':['body','body2'],
                          '3':['body','body2'],
                          '4':['body','body2'],
                          '5':['']},
                    'tn':{'1':['']},
                    'un':{'1':['body'],
                          '2':['body'],
                          '3':['body']},
                    'us':{'1':['body','body2'],
                          '2':['body','body2'],
                          '3':['body','body2'],
                          '4':['body']},
                    'uv':{'1':['body'],
                          '2':['body'],
                          '3':['body'],
                          '4':['body']}
        }
    alt_clothes_dict = {
                    'al':{'1':['pioneer','shirt']},
                    'ba':{'1':['uniform']},
                    'dn':{'1':['pioneer'],
                          '2':['pioneer'],
                          '3':['pioneer']},
                    'cs':{'1':['']},
                    'dv':{'1':['dress','pioneer','pioneer2','sport','swim','body'],
                          '2':['pioneer','pioneer2','sport','swim','body'],
                          '3':['dress','pioneer','pioneer2','sport','body'],
                          '4':['dress','dress_pregnant','pioneer','pioneer2','sport','swim','winter','body'],
                          '5':['pioneer','pioneer2','sport','body']},
                    'el':{'1':['pioneer'],
                          '2':['pioneer'],
                          '3':['pioneer']},
                    'ln':{'1':['dress','pioneer','body'],
                          '2':['dress','pioneer','body'],
                          '3':['dress','pioneer','body']},
                    'mi':{'1':['casual','dress','pioneer','swim','voca','body'],
                          '2':['casual','dress','pioneer','swim','voca','body'],
                          '3':['casual','dress','pioneer','swim','voca','body']},
                    'mt':{'1':['dress','pioneer','sport','swim','swim2','body'],
                          '2':['dress','pioneer','sport','swim','swim2','body'],
                          '3':['dress','pioneer','sport','swim2','body']},
                    'mz':{'1':['pioneer'],
                          '2':['pioneer'],
                          '3':['pioneer']},
                    'sak':{'1':['suit'],
                           '2':['suit'],
                           '3':['suit']},
                    'sh':{'1':[''],
                          '2':[''],
                          '3':['']},
                    'sl':{'1':['casual','dress','pioneer','pioneer2','sport','swim','uniform','body'],
                          '2':['dress','pioneer','pioneer2','sport','swim','body'],
                          '3':['casual','dress','pioneer','pioneer2','sport','swim','voca','body'],
                          '4':['dress','pioneer','pioneer2','sport','swim','body'],
                          '5':['25']},
                    'tn':{'1':['pioneer']},
                    'un':{'1':['dress','modern','pioneer','sleep','sport','swim','winter','body'],
                          '2':['dress','pioneer','sleep','sport','swim','winter','body'],
                          '3':['dress','pioneer','sleep','sport','winter','body']},
                    'us':{'1':['dress','pioneer','sport','swim'],
                          '2':['dress','pioneer','sport','swim'],
                          '3':['dress','pioneer','sport','swim'],
                          '4':['old']},
                    'uv':{'1':['pioneer'],
                          '2':['pioneer'],
                          '3':['pioneer'],
                          '4':['pioneer']}
        }
    alt_emo_dict = {
                    'al':{'1':['angry','dontlike','laugh','normal','sad','shy','smile']},
                    'ba':{'1':['em1','evil','normal','smile']},
                    'cs':{'1':['doubt','fear','glasses_over','glasses_through','grin','laugh','normal','shy','smile']},
                    'dn':{'1':['dontcare','grin','normal','smile','unsured'],
                          '2':['dontlike','upset'],
                          '3':['sad','scared','shocked','sick','surprise']},
                    'dv':{'1':['cry','scared','shocked','surprise'],
                          '2':['grin'],
                          '3':['guilty','sad','shy'],
                          '4':['laugh','normal','smile','soft_smile'],
                          '5':['angry','rage']},
                    'el':{'1':['grin','normal','smile'],
                          '2':['fingal','sad','scared','shocked','surprise','upset'],
                          '3':['angry','laugh','serious']},
                    'ln':{'1':['angry','normal','sad'],
                          '2':['dontlike','grin','guilty'],
                          '3':['serious','smile','surprise']},
                    'mi':{'1':['cry','dontlike','laugh','scared','shocked','shy','surprise'],
                          '2':['cry_smile','grin','happy','sad','smile'],
                          '3':['angry','normal','rage','serious','smile2','upset']},
                    'mt':{'1':['normal','sad','smile','smile_g','surprise'],
                          '2':['angry','rage','shocked'],
                          '3':['feared','grin','laugh','scared']},
                    'mz':{'1':['bukal','laugh','normal'],
                          '2':['angry','rage'],
                          '3':['shy','smile']},
                    'sak':{'1':['calm','normal','sorrow','unsured'],
                          '2':['dontlike','sigh','smile','treat'],
                          '3':['angry','pain','sad','scared']},
                    'sh':{'1':['laugh','scared','smile','upset'],
                          '2':['cry','mad_smile','normal_smile','rage'],
                          '3':['normal','serious','surprise']},
                    'sl':{'1':['dontlike','normal','serious','smile'],
                          '2':['grin','happy','laugh','shy','smile2'],
                          '3':['angry','happy2','sad','shy2','surprise','upset'],
                          '4':['cry','scared','tender'],
                          '5':['displeased','fear_1','fear_2','neutral']},
                    'tn':{'1':['dontlike','grin','laugh','normal','sad','shy','smile']},
                    'un':{'1':['angry','evil_smile','normal','shy','smile','smile2','sorrow'],
                          '2':['cry','cry_smile','sad','scared','shocked','surprise'],
                          '3':['angry2','grin','laugh','rage','serious','smile3']},
                    'us':{'1':['grin','laugh','laugh2','normal','sad','smile'],
                          '2':['angry','calml','dontlike','fear','upset'],
                          '3':['cry','cry2','shy','shy2','surp1','surp2','surp3'],
                          '4':['grin','laugh','normal','shy','smile']},
                    'uv':{'1':['dontlike','rage','sad','shocked'],
                          '2':['normal','smile'],
                          '3':['grin','laugh','surprise2'],
                          '4':['guilty','surprise','upset']}
        }
    alt_acc_dict = {
                    'al':{'1':['']},
                    'ba':{'1':['']},
                    'dn':{'1':[''],
                          '2':[''],
                          '3':['']},
                    'cs':{'1':['glasses','stethoscope','']},
                    'dv':{'1':[''],
                          '2':[''],
                          '3':[''],
                          '4':[''],
                          '5':['']},
                    'el':{'1':[''],
                          '2':[''],
                          '3':['']},
                    'ln':{'1':[''],
                          '2':[''],
                          '3':['']},
                    'mi':{'1':[''],
                          '2':['blond','platinum','red',''],
                          '3':['platinum','']},
                    'mt':{'1':['panama',''],
                          '2':['panama',''],
                          '3':['panama','']},
                    'mz':{'1':['glasses',''],
                          '2':['glasses',''],
                          '3':['glasses','']},
                    'sak':{'1':[''],
                           '2':[''],
                           '3':['']},
                    'sh':{'1':[''],
                          '2':[''],
                          '3':['']},
                    'sl':{'1':[''],
                          '2':[''],
                          '3':[''],
                          '4':[''],
                          '5':['']},
                    'tn':{'1':['']},
                    'un':{'1':[''],
                          '2':[''],
                          '3':['']},
                    'us':{'1':['bear',''],
                          '2':[''],
                          '3':[''],
                          '4':['']},
                    'uv':{'1':[''],
                          '2':[''],
                          '3':[''],
                          '4':['']}
        }

    alt_body_far_dict = {
                    'cs':{'1':['body']},
                    'dv':{'1':['body'],
                          '2':['body'],
                          '3':['body'],
                          '4':['body'],
                          '5':['body']},
                    'el':{'1':['body'],
                          '2':['body'],
                          '3':['body']},
                    'ln':{'1':['body'],
                          '2':['body'],
                          '3':['body']},
                    'mi':{'1':['body'],
                          '2':['body'],
                          '3':['body']},
                    'mt':{'1':['body'],
                          '2':['body'],
                          '3':['body']},
                    'mz':{'1':['body'],
                          '2':['body'],
                          '3':['body']},
                    'sak':{'1':[''],
                           '2':[''],
                           '3':['']},
                    'sh':{'1':['body'],
                          '2':['body'],
                          '3':['body']},
                    'sl':{'1':['body'],
                          '2':['body'],
                          '3':['body'],
                          '4':['body'],
                          '5':['']},
                    'un':{'1':['body'],
                          '2':['body'],
                          '3':['body']},
                    'us':{'1':['body'],
                          '2':['body'],
                          '3':['body']},
                    'uv':{'1':['body'],
                          '2':['body'],
                          '3':['body'],
                          '4':['body']}
        }
    alt_clothes_far_dict = {
                    'cs':{'1':['']},
                    'dv':{'1':['pioneer','pioneer2','swim'],
                          '2':['pioneer','pioneer2','swim'],
                          '3':['pioneer','pioneer2'],
                          '4':['dress','pioneer','pioneer2','sport','swim'],
                          '5':['pioneer','pioneer2']},
                    'el':{'1':['pioneer'],
                          '2':['pioneer'],
                          '3':['pioneer']},
                    'ln':{'1':['dress','pioneer'],
                          '2':['dress','pioneer'],
                          '3':['dress','pioneer']},
                    'mi':{'1':['pioneer','swim','voca'],
                          '2':['casual','pioneer','swim','voca'],
                          '3':['pioneer','swim','voca']},
                    'mt':{'1':['dress','pioneer','swim'],
                          '2':['dress','pioneer','swim'],
                          '3':['pioneer']},
                    'mz':{'1':['pioneer'],
                          '2':['pioneer'],
                          '3':['pioneer']},
                    'sak':{'1':['suit'],
                           '2':['suit'],
                           '3':['suit']},
                    'sh':{'1':[''],
                          '2':[''],
                          '3':['']},
                    'sl':{'1':['dress','pioneer','sport','swim'],
                          '2':['dress','pioneer','sport','swim'],
                          '3':['dress','pioneer','sport','swim'],
                          '4':['dress','pioneer','sport','swim'],
                          '5':['25']},
                    'un':{'1':['dress','pioneer','sport','swim'],
                          '2':['dress','pioneer','sport','swim'],
                          '3':['dress','pioneer','sport']},
                    'us':{'1':['dress','pioneer','sport','swim'],
                          '2':['dress','pioneer','sport','swim'],
                          '3':['dress','pioneer','sport','swim']},
                    'uv':{'1':['pioneer'],
                          '2':['pioneer'],
                          '3':['pioneer'],
                          '4':['pioneer']}
        }
    alt_emo_far_dict = {
                    'cs':{'1':['badgirl','doubt','fear','glasses_over','glasses_through','laugh','normal','shy','smile']},
                    'dv':{'1':['cry','scared','shocked','surprise'],
                          '2':['grin'],
                          '3':['guilty','sad','shy'],
                          '4':['laugh','normal','smile'],
                          '5':['angry','rage']},
                    'el':{'1':['grin','normal','smile'],
                          '2':['fingal','sad','scared','shocked','surprise','upset'],
                          '3':['angry','laugh','serious']},
                    'ln':{'1':['angry','normal','sad'],
                          '2':['dontlike','grin','guilty'],
                          '3':['serious','smile','surprise']},
                    'mi':{'1':['cry','dontlike','laugh','scared','shocked','shy','surprise'],
                          '2':['cry_smile','grin','happy','sad','smile'],
                          '3':['angry','normal','rage','serious','upset']},
                    'mt':{'1':['normal','sad','smile','surprise'],
                          '2':['angry','rage','shocked'],
                          '3':['grin','laugh','scared']},
                    'mz':{'1':['bukal','laugh','normal'],
                          '2':['angry','rage'],
                          '3':['shy','smile']},
                    'sak':{'1':['calm','normal','sorrow','unsured'],
                          '2':['donlike','sigh','smile','treat'],
                          '3':['angry','pain','sad','scared']},
                    'sh':{'1':['laugh','scared','smile','upset'],
                          '2':['cry','normal_smile','rage'],
                          '3':['normal','serious','surprise']},
                    'sl':{'1':['normal','serious','smile'],
                          '2':['happy','laugh','shy','smile2'],
                          '3':['angry','sad','surprise'],
                          '4':['scared','tender'],
                          '5':['displeased','fear_1','fear_2','neutral']},
                    'un':{'1':['angry','evil_smile','normal','shy','smile','smile2'],
                          '2':['cry','cry_smile','sad','scared','shocked','surprise'],
                          '3':['angry2','grin','laugh','rage','serious','smile3']},
                    'us':{'1':['grin','laugh','laugh2','normal','sad','smile'],
                          '2':['angry','calml','dontlike','fear','upset'],
                          '3':['cry','cry2','shy','shy2','surp1','surp2','surp3']},
                    'uv':{'1':['dontlike','rage','sad','shocked'],
                          '2':['normal','smile'],
                          '3':['grin','laugh','surprise2'],
                          '4':['guilty','surprise','upset']}
        }
    alt_acc_far_dict = {
                    'cs':{'1':['glasses','stethoscope','']},
                    'dv':{'1':[''],
                          '2':[''],
                          '3':[''],
                          '4':[''],
                          '5':['']},
                    'el':{'1':[''],
                          '2':[''],
                          '3':['']},
                    'ln':{'1':[''],
                          '2':[''],
                          '3':['']},
                    'mi':{'1':[''],
                          '2':[''],
                          '3':['']},
                    'mt':{'1':['panama',''],
                          '2':['panama',''],
                          '3':['panama','']},
                    'mz':{'1':['glasses',''],
                          '2':['glasses',''],
                          '3':['glasses','']},
                    'sak':{'1':[''],
                           '2':[''],
                           '3':['']},
                    'sh':{'1':[''],
                          '2':[''],
                          '3':['']},
                    'sl':{'1':[''],
                          '2':[''],
                          '3':[''],
                          '4':[''],
                          '5':['']},
                    'un':{'1':[''],
                          '2':[''],
                          '3':['']},
                    'us':{'1':[''],
                          '2':[''],
                          '3':['']},
                    'uv':{'1':[''],
                          '2':[''],
                          '3':[''],
                          '4':['']}
        }

    alt_custom_list = [
                    'al normal pioneer far',
                    'ase_clear',
                    'tn normal pioneer far'
        ]
        
    alt_dist = ['normal/','far/']
    
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
                                        if renpy.loadable(bl_sprites + dist + who + '/' + who + '_' + pose + '_' + body + '.png'):
                                            body_path = bl_sprites + dist + who + '/' + who + '_' + pose + '_' + body + '.png'
                                        elif renpy.loadable(alt_sprites + dist + who + '/' + who + '_' + pose + '_' + body + '.png'):
                                            body_path = alt_sprites + dist + who + '/' + who + '_' + pose + '_' + body + '.png'
                                        if clothes != 'body':
                                            if renpy.loadable(bl_sprites + dist + who + '/' + who + '_' + pose + '_' + clothes + '.png'):
                                                clothes_path = bl_sprites + dist + who + '/' + who + '_' + pose + '_' + clothes + '.png'
                                            elif renpy.loadable(alt_sprites + dist + who + '/' + who + '_' + pose + '_' + clothes + '.png'):
                                                clothes_path = alt_sprites + dist + who + '/' + who + '_' + pose + '_' + clothes + '.png'
                                            if emo != '':
                                                if renpy.loadable(bl_sprites + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'):
                                                    emo_path = bl_sprites + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'
                                                elif renpy.loadable(alt_sprites + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'):
                                                    emo_path = alt_sprites + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'
                                                if acc != '':
                                                    if renpy.loadable(bl_sprites + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'):
                                                        acc_path = bl_sprites + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'
                                                    elif renpy.loadable(alt_sprites + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'):
                                                        acc_path = alt_sprites + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'
                                                    renpy.image(who_num + ' ' + emo + ' ' + clothes + ' ' + acc,
                                                                        ConditionSwitch("persistent.sprite_time=='sunset'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), clothes_path,
                                                                        (0, 0), emo_path,
                                                                        (0, 0), acc_path),
                                                                        im.matrix.tint(0.94, 0.82, 1.0) ),

                                                                        "persistent.sprite_time=='night'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), clothes_path,
                                                                        (0, 0), emo_path,
                                                                        (0, 0), acc_path),
                                                                        im.matrix.tint(0.63, 0.78, 0.82) ),

                                                                        True,
                                                                        im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), clothes_path,
                                                                        (0, 0), emo_path,
                                                                        (0, 0), acc_path), )
                                                                        )
                                                    renpy.image(who_num + ' ' + emo + ' ' + clothes + ' ' + acc + ' close',
                                                                        At(ConditionSwitch("persistent.sprite_time=='sunset'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), clothes_path,
                                                                        (0, 0), emo_path,
                                                                        (0, 0), acc_path),
                                                                        im.matrix.tint(0.94, 0.82, 1.0) ),

                                                                        "persistent.sprite_time=='night'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), clothes_path,
                                                                        (0, 0), emo_path,
                                                                        (0, 0), acc_path),
                                                                        im.matrix.tint(0.63, 0.78, 0.82) ),

                                                                        True,
                                                                        im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), clothes_path,
                                                                        (0, 0), emo_path,
                                                                        (0, 0), acc_path), ), 
                                                                        close_sprites)
                                                                        )
                                                else:
                                                    renpy.image(who_num + ' ' + emo + ' ' + clothes,
                                                                        ConditionSwitch("persistent.sprite_time=='sunset'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), clothes_path,
                                                                        (0, 0), emo_path),
                                                                        im.matrix.tint(0.94, 0.82, 1.0) ),

                                                                        "persistent.sprite_time=='night'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), clothes_path,
                                                                        (0, 0), emo_path),
                                                                        im.matrix.tint(0.63, 0.78, 0.82) ),

                                                                        True,
                                                                        im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), clothes_path,
                                                                        (0, 0), emo_path), )
                                                                        )
                                                    renpy.image(who_num + ' ' + emo + ' ' + clothes + ' close',
                                                                        At(ConditionSwitch("persistent.sprite_time=='sunset'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), clothes_path,
                                                                        (0, 0), emo_path),
                                                                        im.matrix.tint(0.94, 0.82, 1.0) ),

                                                                        "persistent.sprite_time=='night'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), clothes_path,
                                                                        (0, 0), emo_path),
                                                                        im.matrix.tint(0.63, 0.78, 0.82) ),

                                                                        True,
                                                                        im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), clothes_path,
                                                                        (0, 0), emo_path), ), 
                                                                        close_sprites)
                                                                        )
                                        else:
                                            if emo != '':
                                                if renpy.loadable(bl_sprites + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'):
                                                    emo_path = bl_sprites + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'
                                                elif renpy.loadable(alt_sprites + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'):
                                                    emo_path = alt_sprites + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'
                                                if acc != '':
                                                    if renpy.loadable(bl_sprites + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'):
                                                        acc_path = bl_sprites + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'
                                                    elif renpy.loadable(alt_sprites + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'):
                                                        acc_path = alt_sprites + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'
                                                    renpy.image(who_num + ' ' + emo + ' ' + 'body' + ' ' + acc,
                                                                        ConditionSwitch("persistent.sprite_time=='sunset'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), emo_path,
                                                                        (0, 0), acc_path),
                                                                        im.matrix.tint(0.94, 0.82, 1.0) ),

                                                                        "persistent.sprite_time=='night'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), emo_path,
                                                                        (0, 0), acc_path),
                                                                        im.matrix.tint(0.63, 0.78, 0.82) ),

                                                                        True,
                                                                        im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), emo_path,
                                                                        (0, 0), acc_path), )
                                                                        )
                                                    renpy.image(who_num + ' ' + emo + ' ' + 'body' + ' ' + acc + ' close',
                                                                        At(ConditionSwitch("persistent.sprite_time=='sunset'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), emo_path,
                                                                        (0, 0), acc_path),
                                                                        im.matrix.tint(0.94, 0.82, 1.0) ),

                                                                        "persistent.sprite_time=='night'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), emo_path,
                                                                        (0, 0), acc_path),
                                                                        im.matrix.tint(0.63, 0.78, 0.82) ),

                                                                        True,
                                                                        im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), emo_path,
                                                                        (0, 0), acc_path), ), 
                                                                        close_sprites)
                                                                        )
                                                else:
                                                    renpy.image(who_num + ' ' + emo + ' ' + 'body',
                                                                        ConditionSwitch("persistent.sprite_time=='sunset'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), emo_path),
                                                                        im.matrix.tint(0.94, 0.82, 1.0) ),

                                                                        "persistent.sprite_time=='night'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), emo_path),
                                                                        im.matrix.tint(0.63, 0.78, 0.82) ),

                                                                        True,
                                                                        im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), emo_path), )
                                                                        )
                                                    renpy.image(who_num + ' ' + emo + ' ' + 'body' + ' close',
                                                                        At(ConditionSwitch("persistent.sprite_time=='sunset'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), emo_path),
                                                                        im.matrix.tint(0.94, 0.82, 1.0) ),

                                                                        "persistent.sprite_time=='night'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), emo_path),
                                                                        im.matrix.tint(0.63, 0.78, 0.82) ),

                                                                        True,
                                                                        im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), emo_path), ), 
                                                                        close_sprites)
                                                                        )
                                    else:
                                        who_num = who
                                        if renpy.loadable(bl_sprites + dist + who + '/' + who + '_' + pose + '_' + clothes + '.png'):
                                            clothes_path = bl_sprites + dist + who + '/' + who + '_' + pose + '_' + clothes + '.png'
                                        elif renpy.loadable(alt_sprites + dist + who + '/' + who + '_' + pose + '_' + clothes + '.png'):
                                            clothes_path = alt_sprites + dist + who + '/' + who + '_' + pose + '_' + clothes + '.png'
                                        if emo != '':
                                            if renpy.loadable(bl_sprites + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'):
                                                emo_path = bl_sprites + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'
                                            elif renpy.loadable(alt_sprites + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'):
                                                emo_path = alt_sprites + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'
                                            if acc != '':
                                                if renpy.loadable(bl_sprites + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'):
                                                    acc_path = bl_sprites + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'
                                                elif renpy.loadable(alt_sprites + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'):
                                                    acc_path = alt_sprites + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'
                                                renpy.image(who_num + ' ' + emo + ' ' + clothes + ' ' + acc,
                                                                    ConditionSwitch("persistent.sprite_time=='sunset'",
                                                                    im.MatrixColor(im.Composite((900, 1080),
                                                                    (0, 0), clothes_path,
                                                                    (0, 0), emo_path,
                                                                    (0, 0), acc_path),
                                                                    im.matrix.tint(0.94, 0.82, 1.0) ),

                                                                    "persistent.sprite_time=='night'",
                                                                    im.MatrixColor(im.Composite((900, 1080),
                                                                    (0, 0), clothes_path,
                                                                    (0, 0), emo_path,
                                                                    (0, 0), acc_path),
                                                                    im.matrix.tint(0.63, 0.78, 0.82) ),

                                                                    True,
                                                                    im.Composite((900, 1080),
                                                                    (0, 0), clothes_path,
                                                                    (0, 0), emo_path,
                                                                    (0, 0), acc_path), )
                                                                    )
                                                renpy.image(who_num + ' ' + emo + ' ' + clothes + ' ' + acc + ' close',
                                                                    At(ConditionSwitch("persistent.sprite_time=='sunset'",
                                                                    im.MatrixColor(im.Composite((900, 1080),
                                                                    (0, 0), clothes_path,
                                                                    (0, 0), emo_path,
                                                                    (0, 0), acc_path),
                                                                    im.matrix.tint(0.94, 0.82, 1.0) ),

                                                                    "persistent.sprite_time=='night'",
                                                                    im.MatrixColor(im.Composite((900, 1080),
                                                                    (0, 0), clothes_path,
                                                                    (0, 0), emo_path,
                                                                    (0, 0), acc_path),
                                                                    im.matrix.tint(0.63, 0.78, 0.82) ),

                                                                    True,
                                                                    im.Composite((900, 1080),
                                                                    (0, 0), clothes_path,
                                                                    (0, 0), emo_path,
                                                                    (0, 0), acc_path), ), 
                                                                    close_sprites)
                                                                    )
                                            else:
                                                renpy.image(who_num + ' ' + emo + ' ' + clothes,
                                                                    ConditionSwitch("persistent.sprite_time=='sunset'",
                                                                    im.MatrixColor(im.Composite((900, 1080),
                                                                    (0, 0), clothes_path,
                                                                    (0, 0), emo_path),
                                                                    im.matrix.tint(0.94, 0.82, 1.0) ),

                                                                    "persistent.sprite_time=='night'",
                                                                    im.MatrixColor(im.Composite((900, 1080),
                                                                    (0, 0), clothes_path,
                                                                    (0, 0), emo_path),
                                                                    im.matrix.tint(0.63, 0.78, 0.82) ),

                                                                    True,
                                                                    im.Composite((900, 1080),
                                                                    (0, 0), clothes_path,
                                                                    (0, 0), emo_path), )
                                                                    )
                                                renpy.image(who_num + ' ' + emo + ' ' + clothes + ' close',
                                                                    At(ConditionSwitch("persistent.sprite_time=='sunset'",
                                                                    im.MatrixColor(im.Composite((900, 1080),
                                                                    (0, 0), clothes_path,
                                                                    (0, 0), emo_path),
                                                                    im.matrix.tint(0.94, 0.82, 1.0) ),

                                                                    "persistent.sprite_time=='night'",
                                                                    im.MatrixColor(im.Composite((900, 1080),
                                                                    (0, 0), clothes_path,
                                                                    (0, 0), emo_path),
                                                                    im.matrix.tint(0.63, 0.78, 0.82) ),

                                                                    True,
                                                                    im.Composite((900, 1080),
                                                                    (0, 0), clothes_path,
                                                                    (0, 0), emo_path), ), 
                                                                    close_sprites)
                                                                    )
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
                                        if renpy.loadable(bl_sprites + dist + who + '/' + who + '_' + pose + '_' + body + '.png'):
                                            body_path = bl_sprites + dist + who + '/' + who + '_' + pose + '_' + body + '.png'
                                        elif renpy.loadable(alt_sprites + dist + who + '/' + who + '_' + pose + '_' + body + '.png'):
                                            body_path = alt_sprites + dist + who + '/' + who + '_' + pose + '_' + body + '.png'
                                        if clothes != 'body':
                                            if renpy.loadable(bl_sprites + dist + who + '/' + who + '_' + pose + '_' + clothes + '.png'):
                                                clothes_path = bl_sprites + dist + who + '/' + who + '_' + pose + '_' + clothes + '.png'
                                            elif renpy.loadable(alt_sprites + dist + who + '/' + who + '_' + pose + '_' + clothes + '.png'):
                                                clothes_path = alt_sprites + dist + who + '/' + who + '_' + pose + '_' + clothes + '.png'
                                            if emo != '':
                                                if renpy.loadable(bl_sprites + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'):
                                                    emo_path = bl_sprites + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'
                                                elif renpy.loadable(alt_sprites + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'):
                                                    emo_path = alt_sprites + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'
                                                if acc != '':
                                                    if renpy.loadable(bl_sprites + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'):
                                                        acc_path = bl_sprites + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'
                                                    elif renpy.loadable(alt_sprites + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'):
                                                        acc_path = alt_sprites + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'
                                                    renpy.image(who_num + ' ' + emo + ' ' + clothes + ' ' + acc + ' far',
                                                                        ConditionSwitch("persistent.sprite_time=='sunset'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), clothes_path,
                                                                        (0, 0), emo_path,
                                                                        (0, 0), acc_path),
                                                                        im.matrix.tint(0.94, 0.82, 1.0) ),

                                                                        "persistent.sprite_time=='night'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), clothes_path,
                                                                        (0, 0), emo_path,
                                                                        (0, 0), acc_path),
                                                                        im.matrix.tint(0.63, 0.78, 0.82) ),

                                                                        True,
                                                                        im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), clothes_path,
                                                                        (0, 0), emo_path,
                                                                        (0, 0), acc_path), )
                                                                        )
                                                else:
                                                    renpy.image(who_num + ' ' + emo + ' ' + clothes + ' far',
                                                                        ConditionSwitch("persistent.sprite_time=='sunset'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), clothes_path,
                                                                        (0, 0), emo_path),
                                                                        im.matrix.tint(0.94, 0.82, 1.0) ),

                                                                        "persistent.sprite_time=='night'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), clothes_path,
                                                                        (0, 0), emo_path),
                                                                        im.matrix.tint(0.63, 0.78, 0.82) ),

                                                                        True,
                                                                        im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), clothes_path,
                                                                        (0, 0), emo_path), )
                                                                        )
                                        else:
                                            if emo != '':
                                                if renpy.loadable(bl_sprites + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'):
                                                    emo_path = bl_sprites + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'
                                                elif renpy.loadable(alt_sprites + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'):
                                                    emo_path = alt_sprites + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'
                                                if acc != '':
                                                    if renpy.loadable(bl_sprites + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'):
                                                        acc_path = bl_sprites + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'
                                                    elif renpy.loadable(alt_sprites + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'):
                                                        acc_path = alt_sprites + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'
                                                    renpy.image(who_num + ' ' + emo + ' ' + 'body' + ' ' + acc + ' far',
                                                                        ConditionSwitch("persistent.sprite_time=='sunset'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), emo_path,
                                                                        (0, 0), acc_path),
                                                                        im.matrix.tint(0.94, 0.82, 1.0) ),

                                                                        "persistent.sprite_time=='night'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), emo_path,
                                                                        (0, 0), acc_path),
                                                                        im.matrix.tint(0.63, 0.78, 0.82) ),

                                                                        True,
                                                                        im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), emo_path,
                                                                        (0, 0), acc_path), )
                                                                        )
                                                else:
                                                    renpy.image(who_num + ' ' + emo + ' ' + 'body' + ' far',
                                                                        ConditionSwitch("persistent.sprite_time=='sunset'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), emo_path),
                                                                        im.matrix.tint(0.94, 0.82, 1.0) ),

                                                                        "persistent.sprite_time=='night'",
                                                                        im.MatrixColor(im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), emo_path),
                                                                        im.matrix.tint(0.63, 0.78, 0.82) ),

                                                                        True,
                                                                        im.Composite((900, 1080),
                                                                        (0, 0), body_path,
                                                                        (0, 0), emo_path), )
                                                                        )
                                    else:
                                        who_num = who
                                        if renpy.loadable(bl_sprites + dist + who + '/' + who + '_' + pose + '_' + clothes + '.png'):
                                            clothes_path = bl_sprites + dist + who + '/' + who + '_' + pose + '_' + clothes + '.png'
                                        elif renpy.loadable(alt_sprites + dist + who + '/' + who + '_' + pose + '_' + clothes + '.png'):
                                            clothes_path = alt_sprites + dist + who + '/' + who + '_' + pose + '_' + clothes + '.png'
                                        if emo != '':
                                            if renpy.loadable(bl_sprites + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'):
                                                emo_path = bl_sprites + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'
                                            elif renpy.loadable(alt_sprites + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'):
                                                emo_path = alt_sprites + dist + who + '/' + who + '_' + pose + '_' + emo + '.png'
                                            if acc != '':
                                                if renpy.loadable(bl_sprites + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'):
                                                    acc_path = bl_sprites + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'
                                                elif renpy.loadable(alt_sprites + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'):
                                                    acc_path = alt_sprites + dist + who + '/' + who + '_' + pose + '_' + acc + '.png'
                                                renpy.image(who_num + ' ' + emo + ' ' + clothes + ' ' + acc + ' far',
                                                                    ConditionSwitch("persistent.sprite_time=='sunset'",
                                                                    im.MatrixColor(im.Composite((900, 1080),
                                                                    (0, 0), clothes_path,
                                                                    (0, 0), emo_path,
                                                                    (0, 0), acc_path),
                                                                    im.matrix.tint(0.94, 0.82, 1.0) ),

                                                                    "persistent.sprite_time=='night'",
                                                                    im.MatrixColor(im.Composite((900, 1080),
                                                                    (0, 0), clothes_path,
                                                                    (0, 0), emo_path,
                                                                    (0, 0), acc_path),
                                                                    im.matrix.tint(0.63, 0.78, 0.82) ),

                                                                    True,
                                                                    im.Composite((900, 1080),
                                                                    (0, 0), clothes_path,
                                                                    (0, 0), emo_path,
                                                                    (0, 0), acc_path), )
                                                                    )
                                            else:
                                                renpy.image(who_num + ' ' + emo + ' ' + clothes + ' far',
                                                                    ConditionSwitch("persistent.sprite_time=='sunset'",
                                                                    im.MatrixColor(im.Composite((900, 1080),
                                                                    (0, 0), clothes_path,
                                                                    (0, 0), emo_path),
                                                                    im.matrix.tint(0.94, 0.82, 1.0) ),

                                                                    "persistent.sprite_time=='night'",
                                                                    im.MatrixColor(im.Composite((900, 1080),
                                                                    (0, 0), clothes_path,
                                                                    (0, 0), emo_path),
                                                                    im.matrix.tint(0.63, 0.78, 0.82) ),

                                                                    True,
                                                                    im.Composite((900, 1080),
                                                                    (0, 0), clothes_path,
                                                                    (0, 0), emo_path), )
                                                                    )                                                  
                                    
    for custom in alt_custom_list:
        custom_path = alt_sprites + 'custom/' + custom + '.png'
        renpy.image(custom,
                            ConditionSwitch("persistent.sprite_time=='sunset'",
                            im.MatrixColor(im.Composite((900, 1080),
                            (0, 0), custom_path),
                            im.matrix.tint(0.94, 0.82, 1.0) ),

                            "persistent.sprite_time=='night'",
                            im.MatrixColor(im.Composite((900, 1080),
                            (0, 0), custom_path),
                            im.matrix.tint(0.63, 0.78, 0.82) ),

                            True,
                            im.Composite((900, 1080),
                            (0, 0), custom_path), )
                            )                                    
                            
    image pi = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), bl_sprites+"normal/pi/pi_1_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), bl_sprites+"normal/pi/pi_1_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), bl_sprites+"normal/pi/pi_1_pioneer.png") )
    image pi smile = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((900,1080), (0,0), bl_sprites+"normal/pi/pi_1_pioneer_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((900,1080), (0,0), bl_sprites+"normal/pi/pi_1_pioneer_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((900,1080), (0,0), bl_sprites+"normal/pi/pi_1_pioneer_smile.png") )
    image pi close = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((1050,1080), (0,0), bl_sprites+"close/pi/pi_1_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((1050,1080), (0,0), bl_sprites+"close/pi/pi_1_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((1050,1080), (0,0), bl_sprites+"close/pi/pi_1_pioneer.png") )
    image pi far = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((630,1080), (0,0), bl_sprites+"far/pi/pi_1_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((630,1080), (0,0), bl_sprites+"far/pi/pi_1_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
    True,im.Composite((630,1080), (0,0), bl_sprites+"far/pi/pi_1_pioneer.png") )
                            
                            
                            