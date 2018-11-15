init 999999:
    if not renpy.version(tuple=False) == "Ren'Py 7.0.0.196":
        # neko
        image sl neko veryfar = ComposeSpriteSet('veryfar', 'sl/sl_neko.png')['veryfar']
        image dv neko veryfar = ComposeSpriteSet('veryfar', 'dv/dv_neko.png')['veryfar']
        image un neko veryfar = ComposeSpriteSet('veryfar', 'un/un_neko.png')['veryfar']
        image mi neko veryfar = ComposeSpriteSet('veryfar', 'mi/mi_neko.png')['veryfar']
        
        # sl
        image sl pioneer normal veryfar = ComposeSpriteSet('veryfar', 'sl/sl_1_body.png', 'sl/sl_1_pioneer.png', 'sl/sl_1_normal.png')['veryfar']
        image sl pioneer serious veryfar = ComposeSpriteSet('veryfar', 'sl/sl_1_body.png', 'sl/sl_1_pioneer.png', 'sl/sl_1_serious.png')['veryfar']
        image sl pioneer scared veryfar = ComposeSpriteSet('veryfar', 'sl/sl_4_body.png', 'sl/sl_4_pioneer.png', 'sl/sl_4_scared.png')['veryfar']   
        image sl pioneer surprise veryfar = ComposeSpriteSet('veryfar', 'sl/sl_3_body.png', 'sl/sl_3_pioneer.png', 'sl/sl_3_surprise.png')['veryfar']   
        
        # un
        image un pioneer normal veryfar = ComposeSpriteSet('veryfar', 'un/un_1_body.png', 'un/un_1_pioneer.png', 'un/un_1_normal.png')['veryfar']
        image un pioneer scared veryfar = ComposeSpriteSet('veryfar', 'un/un_2_body.png', 'un/un_2_pioneer.png', 'un/un_2_scared.png')['veryfar']
        image un pioneer shocked veryfar = ComposeSpriteSet('veryfar', 'un/un_2_body.png', 'un/un_2_pioneer.png', 'un/un_2_shocked.png')['veryfar']    
        image un pioneer serious veryfar = ComposeSpriteSet('veryfar', 'un/un_3_body.png', 'un/un_3_pioneer.png', 'un/un_3_serious.png')['veryfar']
        image un pioneer evilsmile veryfar = ComposeSpriteSet('veryfar', 'un/un_1_body.png', 'un/un_1_pioneer.png', 'un/un_1_evil_smile.png')['veryfar']
        image un pioneer shy veryfar = ComposeSpriteSet('veryfar', 'un/un_1_body.png', 'un/un_1_pioneer.png', 'un/un_1_shy.png')['veryfar']
        image un pioneer surprise veryfar = ComposeSpriteSet('veryfar', 'un/un_2_body.png', 'un/un_2_pioneer.png', 'un/un_2_surprise.png')['veryfar']

        # el
        image el pioneer slap = ComposeSpriteSet('normal', 'el/el_2_body.png', 'el/el_2_pioneer.png',  'el/el_slap.png')['normal']
        image el pioneer normal veryfar = ComposeSpriteSet('veryfar', 'el/el_1_body.png', 'el/el_1_pioneer.png',  'el/el_1_normal.png')['veryfar']
        image el pioneer scared veryfar = ComposeSpriteSet('veryfar', 'el/el_2_body.png', 'el/el_2_pioneer.png',  'el/el_2_scared.png')['veryfar']
        image el pioneer sad veryfar = ComposeSpriteSet('veryfar', 'el/el_2_body.png', 'el/el_2_pioneer.png',  'el/el_2_sad.png')['veryfar']
        image el pioneer surprise veryfar = ComposeSpriteSet('veryfar', 'el/el_2_body.png', 'el/el_2_pioneer.png',  'el/el_2_surprise.png')['veryfar']
        
        # sh
        image sh pioneer rage veryfar = ComposeSpriteSet('veryfar', 'sh/sh_2_body.png', 'sh/sh_2_rage.png')['veryfar']
        image sh pioneer scared veryfar = ComposeSpriteSet('veryfar', 'sh/sh_1_body.png', 'sh/sh_1_scared.png')['veryfar']
        
        $ _sh_angry_bar = ComposeSpriteSet(('veryfar', 'far','normal','close'), 'sh/sh_angry_bar.png')
        $ _sh_angry_bar3 = ComposeSpriteSet(('normal', 'far', 'veryfar'),  'sh/sh_angry_bar3.png')
        image sh angry bar close        = _sh_angry_bar['close']
        image sh angry bar              = _sh_angry_bar['normal']
        image sh angry bar far          = _sh_angry_bar['far']
        image sh angry bar veryfar      = _sh_angry_bar['veryfar']
        image sh angry bar2 close       = ComposeSpriteSet( 'close',  'sh/sh_angry_bar2.png')['close']
        image sh mad bar2 close         = ComposeSpriteSet( 'close',  'sh/sh_angry_bar2.png', 'sh/sh_mad_smile.png')['close']
        image sh angry bar3             = _sh_angry_bar3['normal']
        image sh angry bar3 far         = _sh_angry_bar3['far']
        image sh angry bar3 veryfar     = _sh_angry_bar3['veryfar']

        # mt
        image mt pioneer angry veryfar = ComposeSpriteSet('veryfar',  'mt/mt_2_body.png', 'mt/mt_2_pioneer.png',  'mt/mt_2_angry.png')['veryfar']
        image mt pioneer normal veryfar = ComposeSpriteSet('veryfar', 'mt/mt_1_body.png',  'mt/mt_1_pioneer.png', 'mt/mt_1_normal.png')['veryfar']
        image mt pioneer scared3 veryfar = ComposeSpriteSet('veryfar', 'mt/mt_3_body.png',  'mt/mt_3_pioneer.png', 'mt/mt_3_scared3.png')['veryfar']
        image mt pioneer surprise veryfar = ComposeSpriteSet('veryfar', 'mt/mt_1_body.png',  'mt/mt_1_pioneer.png', 'mt/mt_1_surprise.png')['veryfar']
        image mt scared3 panama pioneer = ComposeSpriteSet('normal', 'mt/mt_3_body.png',  'mt/mt_3_pioneer.png', 'mt/mt_3_scared3.png', 'mt/mt_3_panama.png')['normal']
        #image mt surprise panama pioneer = ComposeSpriteSet('normal', 'mt/mt_3_body.png',  'mt/mt_3_pioneer.png', 'mt/mt_1_surprise.png', 'mt/mt_3_panama.png')['normal']

        # cs 
        $ _cs_normal2 = ComposeSpriteSet(('normal', 'close', 'far'), 'cs/cs_2_body.png', 'cs/cs_1_normal.png')
        $ _cs_smile2 = ComposeSpriteSet( ('normal', 'close', 'far'), 'cs/cs_2_body.png',  'cs/cs_1_smile.png')
        $ _cs_badgirl2 = ComposeSpriteSet(('close', 'normal'), 'cs/cs_2_body.png', 'cs/cs_2_badgirl.png')
        image cs normal2 close    = _cs_normal2['close']
        image cs normal2          = _cs_normal2['normal']
        image cs normal2 far      = _cs_normal2['far']
        image cs smile2 close    = _cs_smile2['close']
        image cs smile2          = _cs_smile2['normal']
        image cs smile2 far      = _cs_smile2['far']
        image cs shy2 close    = ComposeSpriteSet( 'close', 'cs/cs_2_body.png', 'cs/cs_1_shy.png')['close']
        image cs badgirl2 close    = _cs_badgirl2['close']
        image cs badgirl2          = _cs_badgirl2['normal']
        image cs badgirl2 glasses    = ComposeSpriteSet('normal', 'cs/cs_1_body.png', 'cs/cs_1_glasses.png', 'cs/cs_2_badgirl.png')['normal']