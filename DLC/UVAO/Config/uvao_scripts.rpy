init -999 python:
    def get_image_uvao_7dl(file):
        return default_7dl_path+"DLC/UVAO/Pics/%s" % (file)
        
init -998 python:
    def get_sfx_uvao_7dl(file):
        return default_7dl_path+"DLC/UVAO/Sound/sfx/%s" % (file)
    def get_music_uvao_7dl(file):
        return default_7dl_path+"DLC/UVAO/Sound/music/%s" % (file)

init -5 python:
    # Фабрика спрайтов (Provided by UVAO)
    # Константы:
    # тонировка:
    tint_night = im.matrix.tint(0.63, 0.78, 0.82)
    tint_sunset = im.matrix.tint(0.94, 0.82, 1.0)    

    # Простая функция, строит спрайт из переданных путей
    def ComposeSprite(*argv):
        #строим аргументы для im.Composite
        subargs = list()
        for arg in argv:
           subargs.append( (0,0) )
           subargs.append( arg )
        sprite = im.Composite(None, *subargs)
        return ConditionSwitch("persistent.sprite_time=='sunset'", im.MatrixColor(sprite, tint_sunset), "persistent.sprite_time=='night'", im.MatrixColor(sprite, tint_night), True, sprite)
    # /ComposeSprite(*argv)
        
    # Функция, собирающая спрайты из запчастей
    # types - набор калибров спрайтов. Любой набор из ('far', 'close', 'normal', 'veryfar'). По пути, где лежат спрайты, должны быть соотвествующие директории, иначе не найдет
    # argv - файлы-запчасти. передаются в формате ('path', 'file') - например ('images/1080/sprites/','dv/dv_1_coat.png'), или просто 'file'
    # на выходе - dict спрайтов, по одному для каждого из types
    def ComposeSpriteSet(distance, *argv):
        if isinstance(distance, str): #если types содержит только один параметр.
            distances = (distance,) # 1-tuple. Иначе for будет перебирать символы в строке.
        else:
            distances = distance
        ret = dict()    
        for dst in distances:
            #строим аргументы для ComposeSprite
            subargs = list()
            for arg in argv:
                if isinstance(arg, str): #просто file
                    subarg = (default_7dl_path + 'DLC/UVAO/Pics/sprites/', arg)
                else: # (path, file)
                    subarg = arg;
                subargs.append( subarg[0] + '/' + dst +'/' + subarg[1] ) # 'images/1080/sprites/normal/dv/dv_1_coat.png'
            ret[dst] = ComposeSprite(*subargs)
        return ret
    # /ComposeSpriteSet(type, *argv)    
