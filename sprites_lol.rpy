# Версия от 19.07.2018 Чиним косяки за советами
python early:
    lolcheck = True
    
# Привет иос
# Ведёрки тоже не отстают
# Кривой фикс виджетов
init 100 python:
    style.button_text.color = "#ffffff"
    style.button_text.hover_color = "#ffffff"
    style.button_text.insensitive_color = "#ffffff"
    style.button_text.size = 24
    style.button_text.drop_shadow = (2, 2)
    style.button_text.drop_shadow_color = "#ffffff"
    style.button_text.selected_color = "#ffffff"
    style.button_text.selected_hover_color = "#ffffff"
    style.button_text.background = "#ffffff"
#####################################################################

# Переопределение
init -999 python:
    # Вымученный ужас который ищет недостающие картинки
    import renpy.loader as loader
    def load(name):
        if renpy.config.reject_backslash and "\\" in name:
            raise Exception("Backslash in filename, use '/' instead: %r" % name)

        for p in loader.get_prefixes():
            rv = loader.load_core(p + name)
            if rv is not None:
                return rv
                
        nm = name.lower()
        while (nm.find("/") != -1):
            nm = nm[nm.find("/")+1:]
            for dr, fl in loader.listdirfiles():
                if nm in fl.lower():
                    rv = loader.load_core(fl)
                    if rv is not None:
                        return rv
        raise IOError("Couldn't find file '%s'." % name)
        
    loader.load = load


# Привет, Андрей
init 101 python:
    #Переопределение функции которая шлет нас на*** при наличии более одного изображения
    
    from renpy.display.core import ImagePredictInfo #Лезем в **еня
    images = renpy.display.image.images
    image_attributes = renpy.display.image.image_attributes
    def choose_image_new(self, tag, required, optional, exception_name): # берем функцию
        """
        """

        # The longest length of an image that matches.
        max_len = 0

        # The list of matching images.
        matches = None

        for attrs in image_attributes[tag]:

            num_required = 0

            for i in attrs:
                if i in required:
                    num_required += 1
                    continue

                elif i not in optional:
                    break

            else:

                # We don't have any not-found attributes. But we might not
                # have all of the attributes.

                if num_required != len(required):
                    continue

                len_attrs = len(set(attrs))

                if len_attrs < max_len:
                    continue

                if len_attrs > max_len:
                    max_len = len_attrs
                    matches = [ ]

                matches.append((tag, ) + attrs)

        if matches is None:
            return None

        if len(matches) == 1:
            return matches[0]

        if exception_name:
            # блочим самый ебаный момент
            # raise Exception("Showing '" + " ".join(exception_name) + "' is ambiguous, possible images include: " + ", ".join(" ".join(i) for i in matches))
            return matches[-1] # Возвращаем то, что нужно
        else:
            return None
            
    ImagePredictInfo.choose_image = choose_image_new
# Конец переопределения

# Подчистка некрасивостей
    def clearimages():
        hents = ['cg d2_mt_undressed','cg d2_mt_undressed_2','cg d2_sl_swim','cg d3_sl_bathhouse','cg d5_dv_us_wash','cg d5_dv_us_wash_2','cg d5_dv_us_wash_3','cg d5_dv_us_wash_4','cg d6_dv_hentai','cg d6_dv_hentai_2','cg d6_sl_hentai_1','cg d6_sl_hentai_2','cg d6_sl_swim','cg d7_sl_morning','cg d7_sl_morning_2','cg d7_un_hentai','cg d7_un_hentai_3','cg miku_h_1_cenz','cg miku_h_2_cenz','cg uvao_h_cenz']
        if renpy.android and config.version < "1.3": # Не чистим если 1.3
            sprts = ["image cs normal stethoscope far", "image dv grin swim far", "image dv laugh swim far", "image dv scared pioneer far", "image sl smile2 sport far", "image dv rage pioneer2 far", "image mi scared pioneer far", "image us grin pioneer far", "image un angry swim far", "image mi happy pioneer far", "image un serious pioneer far", "image us surp2 sport far", "image un smile2 dress far", "image us surp2 pioneer far", "image sl shy sport far", "image cs smile far", "image mz rage pioneer far", "image un cry sport far", "image un evil_smile swim far", "image sh smile pioneer far", "image us sad swim far", "image sh cry far", "image sh surprise pioneer far", "image mt grin panama pioneer far", "image dv sad pioneer far", "image mt smile panama swim far", "image dv cry pioneer2 far", "image mt rage panama pioneer far", "image un smile dress far", "image mi dontlike swim far", "image un angry2 dress far", "image sl serious dress far", "image dv guilty pioneer far", "image mz normal pioneer far", "image un cry_smile swim far", "image uv normal far", "image us angry swim far", "image mt normal swim far", "image us dontlike pioneer far", "image un normal sport far", "image un grin sport far", "image mi laugh pioneer far", "image un shocked sport far", "image us laugh2 dress far", "image el laugh pioneer far", "image sl tender pioneer far", "image sl smile pioneer far", "image us angry pioneer far", "image sh normal_smile pioneer far", "image dv laugh pioneer far", "image us sad dress far", "image mt rage panama swim far", "image un angry dress far", "image un angry pioneer far", "image cs normal far", "image us upset pioneer far", "image us smile dress far", "image dv shy pioneer far", "image un smile3 sport far", "image un shy sport far", "image cs smile glasses far", "image sl scared sport far", "image dv shy pioneer2 far", "image us fear swim far", "image sh smile far", "image us fear dress far", "image mt sad pioneer far", "image mt smile dress far", "image un smile2 swim far", "image sh normal_smile far", "image sl tender swim far", "image mt rage pioneer far", "image mt angry panama pioneer far", "image un smile2 pioneer far", "image el normal pioneer far", "image mt smile panama dress far", "image sl laugh sport far", "image us upset sport far", "image mt normal pioneer far", "image us cry2 swim far", "image mt surprise swim far", "image sl smile dress far", "image us upset swim far", "image un smile sport far", "image un smile pioneer far", "image us upset dress far", "image us laugh pioneer far", "image un rage sport far", "image sl scared pioneer far", "image us shy2 sport far", "image sl surprise sport far", "image us surp1 swim far", "image mt angry dress far", "image uv upset far", "image sh serious far", "image uv guilty far", "image us calml swim far", "image us shy2 swim far", "image us dontlike dress far", "image mi smile pioneer far", "image us dontlike sport far", "image un normal pioneer far", "image us cry pioneer far", "image un shy swim far", "image sl smile2 pioneer far", "image mi cry_smile pioneer far", "image un normal swim far", "image dv normal swim far", "image un scared pioneer far", "image dv smile pioneer far", "image us shy swim far", "image cs shy glasses far", "image cs smile stethoscope far", "image us grin swim far", "image sl normal dress far", "image mi cry pioneer far", "image mt grin pioneer far", "image mt surprise pioneer far", "image dv smile swim far", "image un laugh dress far", "image sl serious pioneer far", "image us smile sport far", "image sh serious pioneer far", "image un serious sport far", "image mt normal panama pioneer far", "image mt sad panama dress far", "image sl angry dress far", "image sl surprise dress far", "image dv shocked pioneer far", "image us surp2 swim far", "image sl tender sport far", "image sl surprise pioneer far", "image us grin sport far", "image us laugh2 swim far", "image dv guilty pioneer2 far", "image sl smile2 swim far", "image mi normal swim far", "image sl normal sport far", "image mi sad pioneer far", "image un smile3 pioneer far", "image sl smile2 dress far", "image us smile swim far", "image mt rage panama dress far", "image dv surprise pioneer2 far", "image us cry2 sport far", "image un normal dress far", "image mi smile swim far", "image cs normal glasses far", "image uv rage far", "image sl sad dress far", "image mt rage swim far", "image dv rage pioneer far", "image el surprise pioneer far", "image un cry pioneer far", "image mi dontlike pioneer far", "image sl shy swim far", "image el serious pioneer far", "image un scared swim far", "image el scared pioneer far", "image mi cry swim far", "image mz smile pioneer far", "image us laugh sport far", "image mt surprise dress far", "image mt sad panama swim far", "image sh upset far", "image un evil_smile sport far", "image uv surprise far", "image el grin pioneer far", "image mt smile swim far", "image us shy sport far", "image us fear sport far", "image un evil_smile pioneer far", "image us laugh2 pioneer far", "image sl shy pioneer far", "image us surp3 pioneer far", "image mi laugh swim far", "image un smile3 dress far", "image us surp3 swim far", "image un grin pioneer far", "image mt laugh panama pioneer far", "image sl shy dress far", "image el sad pioneer far", "image un surprise sport far", "image mt surprise panama pioneer far", "image us angry dress far", "image sl serious sport far", "image un scared sport far", "image un cry dress far", "image dv scared pioneer2 far", "image dv shocked pioneer2 far", "image sl laugh swim far", "image us surp1 dress far", "image dv shocked swim far", "image sh laugh far", "image us surp2 dress far", "image uv sad far", "image el angry pioneer far", "image us cry2 dress far", "image sl sad sport far", "image mi scared swim far", "image us laugh swim far", "image mi surprise swim far", "image sl smile swim far", "image us shy2 dress far", "image sl surprise swim far", "image dv smile pioneer2 far", "image mt sad dress far", "image mt smile panama pioneer far", "image dv angry pioneer2 far", "image uv shocked far", "image mz shy glasses pioneer far", "image dv sad pioneer2 far", "image us shy dress far", "image dv normal pioneer far", "image us calml pioneer far", "image mt sad swim far", "image sl tender dress far", "image uv dontlike far", "image sh surprise far", "image us dontlike swim far", "image sl angry pioneer far", "image us shy pioneer far", "image un cry_smile pioneer far", "image un shy pioneer far", "image mt normal panama swim far", "image sl normal swim far", "image mz laugh pioneer far", "image dv surprise swim far", "image sl laugh pioneer far", "image sh laugh pioneer far", "image sl smile sport far", "image sl scared swim far", "image un scared dress far", "image sl serious swim far", "image mt normal dress far", "image us grin dress far", "image sl laugh dress far", "image us laugh dress far", "image dv cry swim far", "image cs shy stethoscope far", "image sh upset pioneer far", "image mz shy pioneer far", "image mz laugh glasses pioneer far", "image mz normal glasses pioneer far", "image cs shy far", "image pi far", "image mz bukal glasses pioneer far", "image mi rage pioneer far", "image sl normal pioneer far", "image mi rage swim far", "image el upset pioneer far", "image us normal pioneer far", "image un shy dress far", "image mt surprise panama swim far", "image us sad sport far", "image mi angry swim far", "image sl happy pioneer far", "image mt sad panama pioneer far", "image us calml sport far", "image us shy2 pioneer far", "image un surprise pioneer far", "image us cry sport far", "image mi angry pioneer far", "image us sad pioneer far", "image uv smile far", "image un cry swim far", "image sh normal pioneer far", "image sh rage far", "image us normal sport far", "image un angry2 sport far", "image sl happy swim far", "image mz rage glasses pioneer far", "image us smile pioneer far", "image mt angry panama swim far", "image sh cry pioneer far", "image mz smile glasses pioneer far", "image sh scared pioneer far", "image mi upset pioneer far", "image mi upset swim far", "image us normal swim far", "image sh normal far", "image un shocked dress far", "image un angry sport far", "image el smile pioneer far", "image mi cry_smile swim far", "image mi grin pioneer far", "image sl scared dress far", "image un cry_smile dress far", "image un cry_smile sport far", "image un sad sport far", "image mt surprise panama dress far", "image dv normal pioneer2 far", "image mz angry glasses pioneer far", "image us cry2 pioneer far", "image mi sad swim far", "image un sad swim far", "image us laugh2 sport far", "image dv angry pioneer far", "image mt smile pioneer far", "image mi shy swim far", "image un grin dress far", "image mt laugh pioneer far", "image un laugh pioneer far", "image dv laugh pioneer2 far", "image us surp1 pioneer far", "image sh rage pioneer far", "image mt angry panama dress far", "image un shocked swim far", "image un evil_smile dress far", "image uv laugh far", "image dv scared swim far", "image mi shocked swim far", "image mt angry pioneer far", "image el fingal pioneer far", "image us surp3 sport far", "image sl happy dress far", "image sh scared far", "image un angry2 pioneer far", "image uv grin far", "image mi shy pioneer far", "image sl sad pioneer far", "image un smile2 sport far", "image us cry dress far", "image un rage pioneer far", "image sl sad swim far", "image mi normal pioneer far", "image us surp1 sport far", "image us cry swim far", "image un serious dress far", "image un laugh sport far", "image un surprise dress far", "image mi happy swim far", "image mi serious swim far", "image uv surprise2 far", "image mz angry pioneer far", "image un sad pioneer far", "image dv surprise pioneer far", "image mz bukal pioneer far", "image mi shocked pioneer far", "image sl happy sport far", "image un sad dress far", "image dv cry pioneer far", "image sl angry swim far", "image un rage dress far", "image us normal dress far", "image sl angry sport far", "image us fear pioneer far", "image mt normal panama dress far", "image mi serious pioneer far", "image un shocked pioneer far", "image dv grin pioneer2 far", "image dv grin pioneer far", "image mt rage dress far", "image us angry sport far", "image mi grin swim far", "image mt angry swim far", "image un surprise swim far", "image el shocked pioneer far", "image us calml dress far", "image us surp3 dress far", "image un smile swim far", "image mi surprise pioneer far", "image cs normal stethoscope", "image dv grin swim", "image dv laugh swim", "image dv scared pioneer", "image sl smile2 sport", "image dv rage pioneer2", "image mi scared pioneer", "image us grin pioneer", "image un angry swim", "image mi happy pioneer", "image un serious pioneer", "image us surp2 sport", "image un smile2 dress", "image us surp2 pioneer", "image sl shy sport", "image cs smile", "image mz rage pioneer", "image un cry sport", "image un evil_smile swim", "image sh smile pioneer", "image us sad swim", "image sh cry", "image sh surprise pioneer", "image mt grin panama pioneer", "image dv sad pioneer", "image mt smile panama swim", "image dv cry pioneer2", "image mt rage panama pioneer", "image un smile dress", "image mi dontlike swim", "image un angry2 dress", "image sl serious dress", "image dv guilty pioneer", "image mz normal pioneer", "image un cry_smile swim", "image uv normal", "image us angry swim", "image mt normal swim", "image us dontlike pioneer", "image un normal sport", "image un grin sport", "image mi laugh pioneer", "image un shocked sport", "image us laugh2 dress", "image el laugh pioneer", "image sl tender pioneer", "image sl smile pioneer", "image us angry pioneer", "image sh normal_smile pioneer", "image dv laugh pioneer", "image us sad dress", "image mt rage panama swim", "image un angry dress", "image un angry pioneer", "image cs normal", "image us upset pioneer", "image us smile dress", "image dv shy pioneer", "image un smile3 sport", "image un shy sport", "image cs smile glasses", "image sl scared sport", "image dv shy pioneer2", "image us fear swim", "image sh smile", "image us fear dress", "image mt sad pioneer", "image mt smile dress", "image un smile2 swim", "image sh normal_smile", "image sl tender swim", "image mt rage pioneer", "image mt angry panama pioneer", "image un smile2 pioneer", "image el normal pioneer", "image mt smile panama dress", "image sl laugh sport", "image us upset sport", "image mt normal pioneer", "image us cry2 swim", "image mt surprise swim", "image sl smile dress", "image us upset swim", "image un smile sport", "image un smile pioneer", "image us upset dress", "image us laugh pioneer", "image un rage sport", "image sl scared pioneer", "image us shy2 sport", "image sl surprise sport", "image us surp1 swim", "image mt angry dress", "image uv upset", "image sh serious", "image uv guilty", "image us calml swim", "image us shy2 swim", "image us dontlike dress", "image mi smile pioneer", "image us dontlike sport", "image un normal pioneer", "image un normal pioneer red", "image us cry pioneer", "image un shy swim", "image sl smile2 pioneer", "image mi cry_smile pioneer", "image un normal swim", "image dv normal swim", "image un scared pioneer", "image dv smile pioneer", "image us shy swim", "image cs shy glasses", "image cs smile stethoscope", "image us grin swim", "image sl normal dress", "image mi cry pioneer", "image mt grin pioneer", "image mt surprise pioneer", "image dv smile swim", "image un laugh dress", "image sl serious pioneer", "image us smile sport", "image sh serious pioneer", "image un serious sport", "image mt normal panama pioneer", "image mt sad panama dress", "image sl angry dress", "image sl surprise dress", "image dv shocked pioneer", "image us surp2 swim", "image sl tender sport", "image sl surprise pioneer", "image us grin sport", "image us laugh2 swim", "image dv guilty pioneer2", "image sl smile2 swim", "image mi normal swim", "image sl normal sport", "image mi sad pioneer", "image un smile3 pioneer", "image sl smile2 dress", "image us smile swim", "image mt rage panama dress", "image dv surprise pioneer2", "image us cry2 sport", "image un normal dress", "image mi smile swim", "image cs normal glasses", "image uv rage", "image sl sad dress", "image mt rage swim", "image dv rage pioneer", "image el surprise pioneer", "image un cry pioneer", "image mi dontlike pioneer", "image sl shy swim", "image el serious pioneer", "image un scared swim", "image el scared pioneer", "image mi cry swim", "image mz smile pioneer", "image us laugh sport", "image mt surprise dress", "image mt sad panama swim", "image sh upset", "image un evil_smile sport", "image uv surprise", "image el grin pioneer", "image mt smile swim", "image us shy sport", "image us fear sport", "image un evil_smile pioneer", "image us laugh2 pioneer", "image sl shy pioneer", "image us surp3 pioneer", "image mi laugh swim", "image un smile3 dress", "image us surp3 swim", "image un grin pioneer", "image mt laugh panama pioneer", "image sl shy dress", "image el sad pioneer", "image un surprise sport", "image mt surprise panama pioneer", "image us angry dress", "image sl serious sport", "image un scared sport", "image un cry dress", "image dv scared pioneer2", "image dv shocked pioneer2", "image sl laugh swim", "image us surp1 dress", "image dv shocked swim", "image sh laugh", "image us surp2 dress", "image uv sad", "image el angry pioneer", "image us cry2 dress", "image sl sad sport", "image mi scared swim", "image us laugh swim", "image mi surprise swim", "image sl smile swim", "image us shy2 dress", "image sl surprise swim", "image dv smile pioneer2", "image mt sad dress", "image mt smile panama pioneer", "image dv angry pioneer2", "image uv shocked", "image mz shy glasses pioneer", "image dv sad pioneer2", "image us shy dress", "image dv normal pioneer", "image us calml pioneer", "image mt sad swim", "image sl tender dress", "image uv dontlike", "image sh surprise", "image us dontlike swim", "image sl angry pioneer", "image us shy pioneer", "image un cry_smile pioneer", "image un shy pioneer", "image mt normal panama swim", "image sl normal swim", "image mz laugh pioneer", "image dv surprise swim", "image sl laugh pioneer", "image sh laugh pioneer", "image sl smile sport", "image sl scared swim", "image un scared dress", "image sl serious swim", "image mt normal dress", "image us grin dress", "image sl laugh dress", "image us laugh dress", "image dv cry swim", "image cs shy stethoscope", "image sh upset pioneer", "image mz shy pioneer", "image mz laugh glasses pioneer", "image mz normal glasses pioneer", "image cs shy", "image pi normal", "image mz bukal glasses pioneer", "image mi rage pioneer", "image sl normal pioneer", "image mi rage swim", "image el upset pioneer", "image us normal pioneer", "image un shy dress", "image mt surprise panama swim", "image us sad sport", "image mi angry swim", "image sl happy pioneer", "image mt sad panama pioneer", "image us calml sport", "image us shy2 pioneer", "image un surprise pioneer", "image un surprise pioneer red", "image us cry sport", "image mi angry pioneer", "image us sad pioneer", "image uv smile", "image un cry swim", "image sh normal pioneer", "image sh rage", "image us normal sport", "image un angry2 sport", "image sl happy swim", "image mz rage glasses pioneer", "image us smile pioneer", "image mt angry panama swim", "image sh cry pioneer", "image mz smile glasses pioneer", "image sh scared pioneer", "image mi upset pioneer", "image mi upset swim", "image us normal swim", "image sh normal", "image un shocked dress", "image un angry sport", "image el smile pioneer", "image mi cry_smile swim", "image mi grin pioneer", "image sl scared dress", "image un cry_smile dress", "image un cry_smile sport", "image un sad sport", "image mt surprise panama dress", "image dv normal pioneer2", "image mz angry glasses pioneer", "image us cry2 pioneer", "image mi sad swim", "image un sad swim", "image us laugh2 sport", "image dv angry pioneer", "image mt smile pioneer", "image mt scared pioneer", "image mi shy swim", "image un grin dress", "image mt laugh pioneer", "image un laugh pioneer", "image dv laugh pioneer2", "image us surp1 pioneer", "image sh rage pioneer", "image mt angry panama dress", "image un shocked swim", "image un evil_smile dress", "image uv laugh", "image dv scared swim", "image mi shocked swim", "image mt angry pioneer", "image el fingal pioneer", "image us surp3 sport", "image sl happy dress", "image sh scared", "image un angry2 pioneer", "image uv grin", "image mi shy pioneer", "image sl sad pioneer", "image un smile2 sport", "image us cry dress", "image un rage pioneer", "image sl sad swim", "image mi normal pioneer", "image us surp1 sport", "image us cry swim", "image un serious dress", "image un laugh sport", "image un surprise dress", "image mi happy swim", "image mi serious swim", "image uv surprise2", "image mz angry pioneer", "image un sad pioneer", "image dv surprise pioneer", "image mz bukal pioneer", "image mi shocked pioneer", "image sl happy sport", "image un sad dress", "image dv cry pioneer", "image sl angry swim", "image un rage dress", "image us normal dress", "image sl angry sport", "image us fear pioneer", "image mt normal panama dress", "image mi serious pioneer", "image un shocked pioneer", "image dv grin pioneer2", "image dv grin pioneer", "image mt rage dress", "image us angry sport", "image mi grin swim", "image mt angry swim", "image un surprise swim", "image el shocked pioneer", "image us calml dress", "image us surp3 dress", "image un smile swim", "image mi surprise pioneer", "image cs normal stethoscope close", "image dv grin swim close", "image dv laugh swim close", "image dv scared pioneer close", "image sl smile2 sport close", "image dv rage pioneer2 close", "image mi scared pioneer close", "image us grin pioneer close", "image un angry swim close", "image mi happy pioneer close", "image un serious pioneer close", "image us surp2 sport close", "image un smile2 dress close", "image us surp2 pioneer close", "image sl shy sport close", "image cs smile close", "image mz rage pioneer close", "image un cry sport close", "image un evil_smile swim close", "image sh smile pioneer close", "image us sad swim close", "image sh cry close", "image sh surprise pioneer close", "image mt grin panama pioneer close", "image dv sad pioneer close", "image mt smile panama swim close", "image dv cry pioneer2 close", "image mt rage panama pioneer close", "image un smile dress close", "image mi dontlike swim close", "image un angry2 dress close", "image sl serious dress close", "image dv guilty pioneer close", "image mz normal pioneer close", "image un cry_smile swim close", "image uv normal close", "image us angry swim close", "image mt normal swim close", "image us dontlike pioneer close", "image un normal sport close", "image un grin sport close", "image mi laugh pioneer close", "image un shocked sport close", "image us laugh2 dress close", "image el laugh pioneer close", "image sl tender pioneer close", "image sl smile pioneer close", "image us angry pioneer close", "image sh normal_smile pioneer close", "image dv laugh pioneer close", "image us sad dress close", "image mt rage panama swim close", "image un angry dress close", "image un angry pioneer close", "image cs normal close", "image us upset pioneer close", "image us smile dress close", "image dv shy pioneer close", "image un smile3 sport close", "image un shy sport close", "image cs smile glasses close", "image sl scared sport close", "image dv shy pioneer2 close", "image us fear swim close", "image sh smile close", "image us fear dress close", "image mt sad pioneer close", "image mt smile dress close", "image un smile2 swim close", "image sh normal_smile close", "image sl tender swim close", "image mt rage pioneer close", "image mt angry panama pioneer close", "image un smile2 pioneer close", "image el normal pioneer close", "image mt smile panama dress close", "image sl laugh sport close", "image us upset sport close", "image mt normal pioneer close", "image us cry2 swim close", "image mt surprise swim close", "image sl smile dress close", "image us upset swim close", "image un smile sport close", "image un smile pioneer close", "image us upset dress close", "image us laugh pioneer close", "image un rage sport close", "image sl scared pioneer close", "image us shy2 sport close", "image sl surprise sport close", "image us surp1 swim close", "image mt angry dress close", "image uv upset close", "image sh serious close", "image uv guilty close", "image us calml swim close", "image us shy2 swim close", "image us dontlike dress close", "image mi smile pioneer close", "image us dontlike sport close", "image un normal pioneer close", "image us cry pioneer close", "image un shy swim close", "image sl smile2 pioneer close", "image mi cry_smile pioneer close", "image un normal swim close", "image dv normal swim close", "image un scared pioneer close", "image dv smile pioneer close", "image us shy swim close", "image cs shy glasses close", "image cs smile stethoscope close", "image us grin swim close", "image sl normal dress close", "image mi cry pioneer close", "image mt grin pioneer close", "image mt surprise pioneer close", "image dv smile swim close", "image un laugh dress close", "image sl serious pioneer close", "image us smile sport close", "image sh serious pioneer close", "image un serious sport close", "image mt normal panama pioneer close", "image mt sad panama dress close", "image sl angry dress close", "image sl surprise dress close", "image dv shocked pioneer close", "image us surp2 swim close", "image sl tender sport close", "image sl surprise pioneer close", "image us grin sport close", "image us laugh2 swim close", "image dv guilty pioneer2 close", "image sl smile2 swim close", "image mi normal swim close", "image sl normal sport close", "image mi sad pioneer close", "image un smile3 pioneer close", "image sl smile2 dress close", "image us smile swim close", "image mt rage panama dress close", "image dv surprise pioneer2 close", "image us cry2 sport close", "image un normal dress close", "image mi smile swim close", "image cs normal glasses close", "image uv rage close", "image sl sad dress close", "image mt rage swim close", "image dv rage pioneer close", "image el surprise pioneer close", "image un cry pioneer close", "image mi dontlike pioneer close", "image sl shy swim close", "image el serious pioneer close", "image un scared swim close", "image el scared pioneer close", "image mi cry swim close", "image mz smile pioneer close", "image us laugh sport close", "image mt surprise dress close", "image mt sad panama swim close", "image sh upset close", "image un evil_smile sport close", "image uv surprise close", "image el grin pioneer close", "image mt smile swim close", "image us shy sport close", "image us fear sport close", "image un evil_smile pioneer close", "image us laugh2 pioneer close", "image sl shy pioneer close", "image us surp3 pioneer close", "image mi laugh swim close", "image un smile3 dress close", "image us surp3 swim close", "image un grin pioneer close", "image mt laugh panama pioneer close", "image sl shy dress close", "image el sad pioneer close", "image un surprise sport close", "image mt surprise panama pioneer close", "image us angry dress close", "image sl serious sport close", "image un scared sport close", "image un cry dress close", "image dv scared pioneer2 close", "image dv shocked pioneer2 close", "image sl laugh swim close", "image us surp1 dress close", "image dv shocked swim close", "image sh laugh close", "image us surp2 dress close", "image uv sad close", "image el angry pioneer close", "image us cry2 dress close", "image sl sad sport close", "image mi scared swim close", "image us laugh swim close", "image mi surprise swim close", "image sl smile swim close", "image us shy2 dress close", "image sl surprise swim close", "image dv smile pioneer2 close", "image mt sad dress close", "image mt smile panama pioneer close", "image dv angry pioneer2 close", "image uv shocked close", "image mz shy glasses pioneer close", "image dv sad pioneer2 close", "image us shy dress close", "image dv normal pioneer close", "image us calml pioneer close", "image mt sad swim close", "image sl tender dress close", "image uv dontlike close", "image sh surprise close", "image us dontlike swim close", "image sl angry pioneer close", "image us shy pioneer close", "image un cry_smile pioneer close", "image un shy pioneer close", "image mt normal panama swim close", "image sl normal swim close", "image mz laugh pioneer close", "image dv surprise swim close", "image sl laugh pioneer close", "image sh laugh pioneer close", "image sl smile sport close", "image sl scared swim close", "image un scared dress close", "image sl serious swim close", "image mt normal dress close", "image us grin dress close", "image sl laugh dress close", "image us laugh dress close", "image dv cry swim close", "image cs shy stethoscope close", "image sh upset pioneer close", "image mz shy pioneer close", "image mz laugh glasses pioneer close", "image mz normal glasses pioneer close", "image cs shy close", "image pi close", "image mz bukal glasses pioneer close", "image mi rage pioneer close", "image sl normal pioneer close", "image mi rage swim close", "image el upset pioneer close", "image us normal pioneer close", "image un shy dress close", "image mt surprise panama swim close", "image us sad sport close", "image mi angry swim close", "image sl happy pioneer close", "image mt sad panama pioneer close", "image us calml sport close", "image us shy2 pioneer close", "image un surprise pioneer close", "image us cry sport close", "image mi angry pioneer close", "image us sad pioneer close", "image uv smile close", "image un cry swim close", "image sh normal pioneer close", "image sh rage close", "image us normal sport close", "image un angry2 sport close", "image sl happy swim close", "image mz rage glasses pioneer close", "image us smile pioneer close", "image mt angry panama swim close", "image sh cry pioneer close", "image mz smile glasses pioneer close", "image sh scared pioneer close", "image mi upset pioneer close", "image mi upset swim close", "image us normal swim close", "image sh normal close", "image un shocked dress close", "image un angry sport close", "image el smile pioneer close", "image mi cry_smile swim close", "image mi grin pioneer close", "image sl scared dress close", "image un cry_smile dress close", "image un cry_smile sport close", "image un sad sport close", "image mt surprise panama dress close", "image dv normal pioneer2 close", "image mz angry glasses pioneer close", "image us cry2 pioneer close", "image mi sad swim close", "image un sad swim close", "image us laugh2 sport close", "image dv angry pioneer close", "image mt smile pioneer close", "image mi shy swim close", "image un grin dress close", "image mt laugh pioneer close", "image un laugh pioneer close", "image dv laugh pioneer2 close", "image us surp1 pioneer close", "image sh rage pioneer close", "image mt angry panama dress close", "image un shocked swim close", "image un evil_smile dress close", "image uv laugh close", "image dv scared swim close", "image mi shocked swim close", "image mt angry pioneer close", "image el fingal pioneer close", "image us surp3 sport close", "image sl happy dress close", "image sh scared close", "image un angry2 pioneer close", "image uv grin close", "image mi shy pioneer close", "image sl sad pioneer close", "image un smile2 sport close", "image us cry dress close", "image un rage pioneer close", "image sl sad swim close", "image mi normal pioneer close", "image us surp1 sport close", "image us cry swim close", "image un serious dress close", "image un laugh sport close", "image un surprise dress close", "image mi happy swim close", "image mi serious swim close", "image uv surprise2 close", "image mz angry pioneer close", "image un sad pioneer close", "image dv surprise pioneer close", "image mz bukal pioneer close", "image mi shocked pioneer close", "image sl happy sport close", "image un sad dress close", "image dv cry pioneer close", "image sl angry swim close", "image un rage dress close", "image us normal dress close", "image sl angry sport close", "image us fear pioneer close", "image mt normal panama dress close", "image mi serious pioneer close", "image un shocked pioneer close", "image dv grin pioneer2 close", "image dv grin pioneer close", "image mt rage dress close", "image us angry sport close", "image mi grin swim close", "image mt angry swim close", "image un surprise swim close", "image el shocked pioneer close", "image us calml dress close", "image us surp3 dress close", "image un smile swim close", "image mi surprise pioneer close", "image mt shocked pioneer", "image un normal body", "image un smile body", "image un shy body", "image un surprise body", "image un angry body", "image un angry2 body", "image un cry body", "image un grin body", "image un laugh body", "image un rage body", "image un scared body", "image un shocked body", "image un smile2 body", "image un smile3 body", "image un sad body", "image un evil_smile body", "image un cry_smile body", "image un serious body", "image un normal body close", "image un smile body close", "image un shy body close", "image un surprise body close", "image un angry body close", "image un angry2 body close", "image un cry body close", "image un grin body close", "image un laugh body close", "image un rage body close", "image un scared body close", "image un shocked body close", "image un smile2 body close", "image un smile3 body close", "image un sad body close", "image un evil_smile body close", "image un cry_smile body close", "image un serious body close", "image dv scared body", "image dv sad body", "image dv guilty body", "image dv laugh body", "image dv shy body", "image dv smile body", "image dv shocked body", "image dv rage body", "image dv normal body", "image dv angry body", "image dv surprise body", "image dv cry body", "image dv grin body", "image dv scared body close", "image dv sad body close", "image dv guilty body close", "image dv laugh body close", "image dv shy body close", "image dv smile body close", "image dv shocked body close", "image dv rage body close", "image dv normal body close", "image dv angry body close", "image dv surprise body close", "image dv cry body close", "image dv grin body close", "image pi smile"]
            for i in sprts:
                a = tuple(i.split())
                while renpy.display.image.image_attributes[a[0]].count(a[1:]) != 0:
                    renpy.display.image.image_attributes[a[0]].remove(a[1:])
                    if a in renpy.display.image.images.keys():
                        renpy.display.image.images.pop(a)
        if not persistent.hentai: # А хентай всегду, буахахах
            for i in hents:
                renpy.image(i,'images/misc/none.png')
        
init 124:
    if lolcheck:
        $ clearimages()
        $ lolcheck = False
        if renpy.android and config.version < "1.3": # Типа не надо если 1.3
            image cs normal stethoscope far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/cs/cs_1_body.png",(0,0), "images/sprites/far/cs/cs_1_stethoscope.png",(0,0), "images/sprites/far/cs/cs_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/cs/cs_1_body.png",(0,0), "images/sprites/far/cs/cs_1_stethoscope.png",(0,0), "images/sprites/far/cs/cs_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/cs/cs_1_body.png",(0,0), "images/sprites/far/cs/cs_1_stethoscope.png",(0,0), "images/sprites/far/cs/cs_1_normal.png") )
            image dv grin swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_2_body.png",(0,0), "images/sprites/far/dv/dv_2_swim.png",(0,0), "images/sprites/far/dv/dv_2_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_2_body.png",(0,0), "images/sprites/far/dv/dv_2_swim.png",(0,0), "images/sprites/far/dv/dv_2_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_2_body.png",(0,0), "images/sprites/far/dv/dv_2_swim.png",(0,0), "images/sprites/far/dv/dv_2_grin.png") )
            image dv laugh swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_4_body.png",(0,0), "images/sprites/far/dv/dv_4_swim.png",(0,0), "images/sprites/far/dv/dv_4_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_4_body.png",(0,0), "images/sprites/far/dv/dv_4_swim.png",(0,0), "images/sprites/far/dv/dv_4_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_4_body.png",(0,0), "images/sprites/far/dv/dv_4_swim.png",(0,0), "images/sprites/far/dv/dv_4_laugh.png") )
            image dv scared pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_1_body.png",(0,0), "images/sprites/far/dv/dv_1_pioneer.png",(0,0), "images/sprites/far/dv/dv_1_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_1_body.png",(0,0), "images/sprites/far/dv/dv_1_pioneer.png",(0,0), "images/sprites/far/dv/dv_1_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_1_body.png",(0,0), "images/sprites/far/dv/dv_1_pioneer.png",(0,0), "images/sprites/far/dv/dv_1_scared.png") )
            image sl smile2 sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_sport.png",(0,0), "images/sprites/far/sl/sl_2_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_sport.png",(0,0), "images/sprites/far/sl/sl_2_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_sport.png",(0,0), "images/sprites/far/sl/sl_2_smile2.png") )
            image dv rage pioneer2 far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_5_body.png",(0,0), "images/sprites/far/dv/dv_5_pioneer2.png",(0,0), "images/sprites/far/dv/dv_5_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_5_body.png",(0,0), "images/sprites/far/dv/dv_5_pioneer2.png",(0,0), "images/sprites/far/dv/dv_5_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_5_body.png",(0,0), "images/sprites/far/dv/dv_5_pioneer2.png",(0,0), "images/sprites/far/dv/dv_5_rage.png") )
            image mi scared pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_pioneer.png",(0,0), "images/sprites/far/mi/mi_1_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_pioneer.png",(0,0), "images/sprites/far/mi/mi_1_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_pioneer.png",(0,0), "images/sprites/far/mi/mi_1_scared.png") )
            image us grin pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_pioneer.png",(0,0), "images/sprites/far/us/us_1_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_pioneer.png",(0,0), "images/sprites/far/us/us_1_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_pioneer.png",(0,0), "images/sprites/far/us/us_1_grin.png") )
            image un angry swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_swim.png",(0,0), "images/sprites/far/un/un_1_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_swim.png",(0,0), "images/sprites/far/un/un_1_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_swim.png",(0,0), "images/sprites/far/un/un_1_angry.png") )
            image mi happy pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_2_body.png",(0,0), "images/sprites/far/mi/mi_2_pioneer.png",(0,0), "images/sprites/far/mi/mi_2_happy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_2_body.png",(0,0), "images/sprites/far/mi/mi_2_pioneer.png",(0,0), "images/sprites/far/mi/mi_2_happy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_2_body.png",(0,0), "images/sprites/far/mi/mi_2_pioneer.png",(0,0), "images/sprites/far/mi/mi_2_happy.png") )
            image un serious pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_pioneer.png",(0,0), "images/sprites/far/un/un_3_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_pioneer.png",(0,0), "images/sprites/far/un/un_3_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_pioneer.png",(0,0), "images/sprites/far/un/un_3_serious.png") )
            image us surp2 sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_sport.png",(0,0), "images/sprites/far/us/us_3_surp2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_sport.png",(0,0), "images/sprites/far/us/us_3_surp2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_sport.png",(0,0), "images/sprites/far/us/us_3_surp2.png") )
            image un smile2 dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_dress.png",(0,0), "images/sprites/far/un/un_1_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_dress.png",(0,0), "images/sprites/far/un/un_1_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_dress.png",(0,0), "images/sprites/far/un/un_1_smile2.png") )
            image us surp2 pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_pioneer.png",(0,0), "images/sprites/far/us/us_3_surp2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_pioneer.png",(0,0), "images/sprites/far/us/us_3_surp2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_pioneer.png",(0,0), "images/sprites/far/us/us_3_surp2.png") )
            image sl shy sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_sport.png",(0,0), "images/sprites/far/sl/sl_2_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_sport.png",(0,0), "images/sprites/far/sl/sl_2_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_sport.png",(0,0), "images/sprites/far/sl/sl_2_shy.png") )
            image cs smile far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/cs/cs_1_body.png",(0,0), "images/sprites/far/cs/cs_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/cs/cs_1_body.png",(0,0), "images/sprites/far/cs/cs_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/cs/cs_1_body.png",(0,0), "images/sprites/far/cs/cs_1_smile.png") )
            image mz rage pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_2_body.png",(0,0), "images/sprites/far/mz/mz_2_pioneer.png",(0,0), "images/sprites/far/mz/mz_2_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_2_body.png",(0,0), "images/sprites/far/mz/mz_2_pioneer.png",(0,0), "images/sprites/far/mz/mz_2_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_2_body.png",(0,0), "images/sprites/far/mz/mz_2_pioneer.png",(0,0), "images/sprites/far/mz/mz_2_rage.png") )
            image un cry sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_sport.png",(0,0), "images/sprites/far/un/un_2_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_sport.png",(0,0), "images/sprites/far/un/un_2_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_sport.png",(0,0), "images/sprites/far/un/un_2_cry.png") )
            image un evil_smile swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_swim.png",(0,0), "images/sprites/far/un/un_1_evil_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_swim.png",(0,0), "images/sprites/far/un/un_1_evil_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_swim.png",(0,0), "images/sprites/far/un/un_1_evil_smile.png") )
            image sh smile pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_1_body.png",(0,0), "images/sprites/far/sh/sh_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_1_body.png",(0,0), "images/sprites/far/sh/sh_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_1_body.png",(0,0), "images/sprites/far/sh/sh_1_smile.png") )
            image us sad swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_swim.png",(0,0), "images/sprites/far/us/us_1_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_swim.png",(0,0), "images/sprites/far/us/us_1_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_swim.png",(0,0), "images/sprites/far/us/us_1_sad.png") )
            image sh cry far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_2_body.png",(0,0), "images/sprites/far/sh/sh_2_rage.png",(0,0), "images/sprites/far/sh/sh_2_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_2_body.png",(0,0), "images/sprites/far/sh/sh_2_rage.png",(0,0), "images/sprites/far/sh/sh_2_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_2_body.png",(0,0), "images/sprites/far/sh/sh_2_rage.png",(0,0), "images/sprites/far/sh/sh_2_cry.png") )
            image sh surprise pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_3_body.png",(0,0), "images/sprites/far/sh/sh_3_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_3_body.png",(0,0), "images/sprites/far/sh/sh_3_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_3_body.png",(0,0), "images/sprites/far/sh/sh_3_surprise.png") )
            image mt grin panama pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_3_body.png",(0,0), "images/sprites/far/mt/mt_3_panama.png",(0,0), "images/sprites/far/mt/mt_3_grin.png",(0,0), "images/sprites/far/mt/mt_3_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_3_body.png",(0,0), "images/sprites/far/mt/mt_3_panama.png",(0,0), "images/sprites/far/mt/mt_3_grin.png",(0,0), "images/sprites/far/mt/mt_3_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_3_body.png",(0,0), "images/sprites/far/mt/mt_3_panama.png",(0,0), "images/sprites/far/mt/mt_3_grin.png",(0,0), "images/sprites/far/mt/mt_3_pioneer.png") )
            image dv sad pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_3_body.png",(0,0), "images/sprites/far/dv/dv_3_pioneer.png",(0,0), "images/sprites/far/dv/dv_3_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_3_body.png",(0,0), "images/sprites/far/dv/dv_3_pioneer.png",(0,0), "images/sprites/far/dv/dv_3_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_3_body.png",(0,0), "images/sprites/far/dv/dv_3_pioneer.png",(0,0), "images/sprites/far/dv/dv_3_sad.png") )
            image mt smile panama swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_panama.png",(0,0), "images/sprites/far/mt/mt_1_smile.png",(0,0), "images/sprites/far/mt/mt_1_swim.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_panama.png",(0,0), "images/sprites/far/mt/mt_1_smile.png",(0,0), "images/sprites/far/mt/mt_1_swim.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_panama.png",(0,0), "images/sprites/far/mt/mt_1_smile.png",(0,0), "images/sprites/far/mt/mt_1_swim.png") )
            image dv cry pioneer2 far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_1_body.png",(0,0), "images/sprites/far/dv/dv_1_pioneer2.png",(0,0), "images/sprites/far/dv/dv_1_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_1_body.png",(0,0), "images/sprites/far/dv/dv_1_pioneer2.png",(0,0), "images/sprites/far/dv/dv_1_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_1_body.png",(0,0), "images/sprites/far/dv/dv_1_pioneer2.png",(0,0), "images/sprites/far/dv/dv_1_cry.png") )
            image mt rage panama pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_2_body.png",(0,0), "images/sprites/far/mt/mt_2_panama.png",(0,0), "images/sprites/far/mt/mt_2_rage.png",(0,0), "images/sprites/far/mt/mt_2_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_2_body.png",(0,0), "images/sprites/far/mt/mt_2_panama.png",(0,0), "images/sprites/far/mt/mt_2_rage.png",(0,0), "images/sprites/far/mt/mt_2_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_2_body.png",(0,0), "images/sprites/far/mt/mt_2_panama.png",(0,0), "images/sprites/far/mt/mt_2_rage.png",(0,0), "images/sprites/far/mt/mt_2_pioneer.png") )
            image un smile dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_dress.png",(0,0), "images/sprites/far/un/un_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_dress.png",(0,0), "images/sprites/far/un/un_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_dress.png",(0,0), "images/sprites/far/un/un_1_smile.png") )
            image mi dontlike swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_swim.png",(0,0), "images/sprites/far/mi/mi_1_dontlike.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_swim.png",(0,0), "images/sprites/far/mi/mi_1_dontlike.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_swim.png",(0,0), "images/sprites/far/mi/mi_1_dontlike.png") )
            image un angry2 dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_dress.png",(0,0), "images/sprites/far/un/un_3_angry2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_dress.png",(0,0), "images/sprites/far/un/un_3_angry2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_dress.png",(0,0), "images/sprites/far/un/un_3_angry2.png") )
            image sl serious dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_1_body.png",(0,0), "images/sprites/far/sl/sl_1_dress.png",(0,0), "images/sprites/far/sl/sl_1_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_1_body.png",(0,0), "images/sprites/far/sl/sl_1_dress.png",(0,0), "images/sprites/far/sl/sl_1_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_1_body.png",(0,0), "images/sprites/far/sl/sl_1_dress.png",(0,0), "images/sprites/far/sl/sl_1_serious.png") )
            image dv guilty pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_3_body.png",(0,0), "images/sprites/far/dv/dv_3_pioneer.png",(0,0), "images/sprites/far/dv/dv_3_guilty.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_3_body.png",(0,0), "images/sprites/far/dv/dv_3_pioneer.png",(0,0), "images/sprites/far/dv/dv_3_guilty.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_3_body.png",(0,0), "images/sprites/far/dv/dv_3_pioneer.png",(0,0), "images/sprites/far/dv/dv_3_guilty.png") )
            image mz normal pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_1_body.png",(0,0), "images/sprites/far/mz/mz_1_pioneer.png",(0,0), "images/sprites/far/mz/mz_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_1_body.png",(0,0), "images/sprites/far/mz/mz_1_pioneer.png",(0,0), "images/sprites/far/mz/mz_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_1_body.png",(0,0), "images/sprites/far/mz/mz_1_pioneer.png",(0,0), "images/sprites/far/mz/mz_1_normal.png") )
            image un cry_smile swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_swim.png",(0,0), "images/sprites/far/un/un_2_cry_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_swim.png",(0,0), "images/sprites/far/un/un_2_cry_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_swim.png",(0,0), "images/sprites/far/un/un_2_cry_smile.png") )
            image uv normal far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/uv/uv_2_body.png",(0,0), "images/sprites/far/uv/uv_2_pioneer.png",(0,0), "images/sprites/far/uv/uv_2_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/uv/uv_2_body.png",(0,0), "images/sprites/far/uv/uv_2_pioneer.png",(0,0), "images/sprites/far/uv/uv_2_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/uv/uv_2_body.png",(0,0), "images/sprites/far/uv/uv_2_pioneer.png",(0,0), "images/sprites/far/uv/uv_2_normal.png") )
            image us angry swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_swim.png",(0,0), "images/sprites/far/us/us_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_swim.png",(0,0), "images/sprites/far/us/us_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_swim.png",(0,0), "images/sprites/far/us/us_2_angry.png") )
            image mt normal swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_swim.png",(0,0), "images/sprites/far/mt/mt_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_swim.png",(0,0), "images/sprites/far/mt/mt_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_swim.png",(0,0), "images/sprites/far/mt/mt_1_normal.png") )
            image us dontlike pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_pioneer.png",(0,0), "images/sprites/far/us/us_2_dontlike.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_pioneer.png",(0,0), "images/sprites/far/us/us_2_dontlike.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_pioneer.png",(0,0), "images/sprites/far/us/us_2_dontlike.png") )
            image un normal sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_sport.png",(0,0), "images/sprites/far/un/un_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_sport.png",(0,0), "images/sprites/far/un/un_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_sport.png",(0,0), "images/sprites/far/un/un_1_normal.png") )
            image un grin sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_sport.png",(0,0), "images/sprites/far/un/un_3_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_sport.png",(0,0), "images/sprites/far/un/un_3_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_sport.png",(0,0), "images/sprites/far/un/un_3_grin.png") )
            image mi laugh pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_pioneer.png",(0,0), "images/sprites/far/mi/mi_1_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_pioneer.png",(0,0), "images/sprites/far/mi/mi_1_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_pioneer.png",(0,0), "images/sprites/far/mi/mi_1_laugh.png") )
            image un shocked sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_sport.png",(0,0), "images/sprites/far/un/un_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_sport.png",(0,0), "images/sprites/far/un/un_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_sport.png",(0,0), "images/sprites/far/un/un_2_shocked.png") )
            image us laugh2 dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_dress.png",(0,0), "images/sprites/far/us/us_1_laugh2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_dress.png",(0,0), "images/sprites/far/us/us_1_laugh2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_dress.png",(0,0), "images/sprites/far/us/us_1_laugh2.png") )
            image el laugh pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/el/el_3_body.png",(0,0), "images/sprites/far/el/el_3_pioneer.png",(0,0), "images/sprites/far/el/el_3_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/el/el_3_body.png",(0,0), "images/sprites/far/el/el_3_pioneer.png",(0,0), "images/sprites/far/el/el_3_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/el/el_3_body.png",(0,0), "images/sprites/far/el/el_3_pioneer.png",(0,0), "images/sprites/far/el/el_3_laugh.png") )
            image sl tender pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_4_body.png",(0,0), "images/sprites/far/sl/sl_4_pioneer.png",(0,0), "images/sprites/far/sl/sl_4_tender.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_4_body.png",(0,0), "images/sprites/far/sl/sl_4_pioneer.png",(0,0), "images/sprites/far/sl/sl_4_tender.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_4_body.png",(0,0), "images/sprites/far/sl/sl_4_pioneer.png",(0,0), "images/sprites/far/sl/sl_4_tender.png") )
            image sl smile pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_1_body.png",(0,0), "images/sprites/far/sl/sl_1_pioneer.png",(0,0), "images/sprites/far/sl/sl_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_1_body.png",(0,0), "images/sprites/far/sl/sl_1_pioneer.png",(0,0), "images/sprites/far/sl/sl_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_1_body.png",(0,0), "images/sprites/far/sl/sl_1_pioneer.png",(0,0), "images/sprites/far/sl/sl_1_smile.png") )
            image us angry pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_pioneer.png",(0,0), "images/sprites/far/us/us_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_pioneer.png",(0,0), "images/sprites/far/us/us_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_pioneer.png",(0,0), "images/sprites/far/us/us_2_angry.png") )
            image sh normal_smile pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_2_body.png",(0,0), "images/sprites/far/sh/sh_2_normal_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_2_body.png",(0,0), "images/sprites/far/sh/sh_2_normal_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_2_body.png",(0,0), "images/sprites/far/sh/sh_2_normal_smile.png") )
            image dv laugh pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_4_body.png",(0,0), "images/sprites/far/dv/dv_4_pioneer.png",(0,0), "images/sprites/far/dv/dv_4_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_4_body.png",(0,0), "images/sprites/far/dv/dv_4_pioneer.png",(0,0), "images/sprites/far/dv/dv_4_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_4_body.png",(0,0), "images/sprites/far/dv/dv_4_pioneer.png",(0,0), "images/sprites/far/dv/dv_4_laugh.png") )
            image us sad dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_dress.png",(0,0), "images/sprites/far/us/us_1_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_dress.png",(0,0), "images/sprites/far/us/us_1_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_dress.png",(0,0), "images/sprites/far/us/us_1_sad.png") )
            image mt rage panama swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_2_body.png",(0,0), "images/sprites/far/mt/mt_2_panama.png",(0,0), "images/sprites/far/mt/mt_2_rage.png",(0,0), "images/sprites/far/mt/mt_2_swim.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_2_body.png",(0,0), "images/sprites/far/mt/mt_2_panama.png",(0,0), "images/sprites/far/mt/mt_2_rage.png",(0,0), "images/sprites/far/mt/mt_2_swim.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_2_body.png",(0,0), "images/sprites/far/mt/mt_2_panama.png",(0,0), "images/sprites/far/mt/mt_2_rage.png",(0,0), "images/sprites/far/mt/mt_2_swim.png") )
            image un angry dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_dress.png",(0,0), "images/sprites/far/un/un_1_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_dress.png",(0,0), "images/sprites/far/un/un_1_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_dress.png",(0,0), "images/sprites/far/un/un_1_angry.png") )
            image un angry pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_pioneer.png",(0,0), "images/sprites/far/un/un_1_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_pioneer.png",(0,0), "images/sprites/far/un/un_1_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_pioneer.png",(0,0), "images/sprites/far/un/un_1_angry.png") )
            image cs normal far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/cs/cs_1_body.png",(0,0), "images/sprites/far/cs/cs_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/cs/cs_1_body.png",(0,0), "images/sprites/far/cs/cs_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/cs/cs_1_body.png",(0,0), "images/sprites/far/cs/cs_1_normal.png") )
            image us upset pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_pioneer.png",(0,0), "images/sprites/far/us/us_2_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_pioneer.png",(0,0), "images/sprites/far/us/us_2_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_pioneer.png",(0,0), "images/sprites/far/us/us_2_upset.png") )
            image us smile dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_dress.png",(0,0), "images/sprites/far/us/us_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_dress.png",(0,0), "images/sprites/far/us/us_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_dress.png",(0,0), "images/sprites/far/us/us_1_smile.png") )
            image dv shy pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_3_body.png",(0,0), "images/sprites/far/dv/dv_3_pioneer.png",(0,0), "images/sprites/far/dv/dv_3_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_3_body.png",(0,0), "images/sprites/far/dv/dv_3_pioneer.png",(0,0), "images/sprites/far/dv/dv_3_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_3_body.png",(0,0), "images/sprites/far/dv/dv_3_pioneer.png",(0,0), "images/sprites/far/dv/dv_3_shy.png") )
            image un smile3 sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_sport.png",(0,0), "images/sprites/far/un/un_3_smile3.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_sport.png",(0,0), "images/sprites/far/un/un_3_smile3.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_sport.png",(0,0), "images/sprites/far/un/un_3_smile3.png") )
            image un shy sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_sport.png",(0,0), "images/sprites/far/un/un_1_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_sport.png",(0,0), "images/sprites/far/un/un_1_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_sport.png",(0,0), "images/sprites/far/un/un_1_shy.png") )
            image cs smile glasses far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/cs/cs_1_body.png",(0,0), "images/sprites/far/cs/cs_1_glasses.png",(0,0), "images/sprites/far/cs/cs_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/cs/cs_1_body.png",(0,0), "images/sprites/far/cs/cs_1_glasses.png",(0,0), "images/sprites/far/cs/cs_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/cs/cs_1_body.png",(0,0), "images/sprites/far/cs/cs_1_glasses.png",(0,0), "images/sprites/far/cs/cs_1_smile.png") )
            image sl scared sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_4_body.png",(0,0), "images/sprites/far/sl/sl_4_sport.png",(0,0), "images/sprites/far/sl/sl_4_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_4_body.png",(0,0), "images/sprites/far/sl/sl_4_sport.png",(0,0), "images/sprites/far/sl/sl_4_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_4_body.png",(0,0), "images/sprites/far/sl/sl_4_sport.png",(0,0), "images/sprites/far/sl/sl_4_scared.png") )
            image dv shy pioneer2 far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_3_body.png",(0,0), "images/sprites/far/dv/dv_3_pioneer2.png",(0,0), "images/sprites/far/dv/dv_3_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_3_body.png",(0,0), "images/sprites/far/dv/dv_3_pioneer2.png",(0,0), "images/sprites/far/dv/dv_3_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_3_body.png",(0,0), "images/sprites/far/dv/dv_3_pioneer2.png",(0,0), "images/sprites/far/dv/dv_3_shy.png") )
            image us fear swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_swim.png",(0,0), "images/sprites/far/us/us_2_fear.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_swim.png",(0,0), "images/sprites/far/us/us_2_fear.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_swim.png",(0,0), "images/sprites/far/us/us_2_fear.png") )
            image sh smile far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_1_body.png",(0,0), "images/sprites/far/sh/sh_1_laugh.png",(0,0), "images/sprites/far/sh/sh_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_1_body.png",(0,0), "images/sprites/far/sh/sh_1_laugh.png",(0,0), "images/sprites/far/sh/sh_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_1_body.png",(0,0), "images/sprites/far/sh/sh_1_laugh.png",(0,0), "images/sprites/far/sh/sh_1_smile.png") )
            image us fear dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_dress.png",(0,0), "images/sprites/far/us/us_2_fear.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_dress.png",(0,0), "images/sprites/far/us/us_2_fear.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_dress.png",(0,0), "images/sprites/far/us/us_2_fear.png") )
            image mt sad pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_pioneer.png",(0,0), "images/sprites/far/mt/mt_1_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_pioneer.png",(0,0), "images/sprites/far/mt/mt_1_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_pioneer.png",(0,0), "images/sprites/far/mt/mt_1_sad.png") )
            image mt smile dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_dress.png",(0,0), "images/sprites/far/mt/mt_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_dress.png",(0,0), "images/sprites/far/mt/mt_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_dress.png",(0,0), "images/sprites/far/mt/mt_1_smile.png") )
            image un smile2 swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_swim.png",(0,0), "images/sprites/far/un/un_1_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_swim.png",(0,0), "images/sprites/far/un/un_1_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_swim.png",(0,0), "images/sprites/far/un/un_1_smile2.png") )
            image sh normal_smile far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_2_body.png",(0,0), "images/sprites/far/sh/sh_2_rage.png",(0,0), "images/sprites/far/sh/sh_2_normal_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_2_body.png",(0,0), "images/sprites/far/sh/sh_2_rage.png",(0,0), "images/sprites/far/sh/sh_2_normal_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_2_body.png",(0,0), "images/sprites/far/sh/sh_2_rage.png",(0,0), "images/sprites/far/sh/sh_2_normal_smile.png") )
            image sl tender swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_4_body.png",(0,0), "images/sprites/far/sl/sl_4_swim.png",(0,0), "images/sprites/far/sl/sl_4_tender.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_4_body.png",(0,0), "images/sprites/far/sl/sl_4_swim.png",(0,0), "images/sprites/far/sl/sl_4_tender.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_4_body.png",(0,0), "images/sprites/far/sl/sl_4_swim.png",(0,0), "images/sprites/far/sl/sl_4_tender.png") )
            image mt rage pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_2_body.png",(0,0), "images/sprites/far/mt/mt_2_pioneer.png",(0,0), "images/sprites/far/mt/mt_2_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_2_body.png",(0,0), "images/sprites/far/mt/mt_2_pioneer.png",(0,0), "images/sprites/far/mt/mt_2_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_2_body.png",(0,0), "images/sprites/far/mt/mt_2_pioneer.png",(0,0), "images/sprites/far/mt/mt_2_rage.png") )
            image mt angry panama pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_2_body.png",(0,0), "images/sprites/far/mt/mt_2_panama.png",(0,0), "images/sprites/far/mt/mt_2_angry.png",(0,0), "images/sprites/far/mt/mt_2_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_2_body.png",(0,0), "images/sprites/far/mt/mt_2_panama.png",(0,0), "images/sprites/far/mt/mt_2_angry.png",(0,0), "images/sprites/far/mt/mt_2_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_2_body.png",(0,0), "images/sprites/far/mt/mt_2_panama.png",(0,0), "images/sprites/far/mt/mt_2_angry.png",(0,0), "images/sprites/far/mt/mt_2_pioneer.png") )
            image un smile2 pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_pioneer.png",(0,0), "images/sprites/far/un/un_1_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_pioneer.png",(0,0), "images/sprites/far/un/un_1_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_pioneer.png",(0,0), "images/sprites/far/un/un_1_smile2.png") )
            image el normal pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/el/el_1_body.png",(0,0), "images/sprites/far/el/el_1_pioneer.png",(0,0), "images/sprites/far/el/el_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/el/el_1_body.png",(0,0), "images/sprites/far/el/el_1_pioneer.png",(0,0), "images/sprites/far/el/el_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/el/el_1_body.png",(0,0), "images/sprites/far/el/el_1_pioneer.png",(0,0), "images/sprites/far/el/el_1_normal.png") )
            image mt smile panama dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_panama.png",(0,0), "images/sprites/far/mt/mt_1_smile.png",(0,0), "images/sprites/far/mt/mt_1_dress.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_panama.png",(0,0), "images/sprites/far/mt/mt_1_smile.png",(0,0), "images/sprites/far/mt/mt_1_dress.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_panama.png",(0,0), "images/sprites/far/mt/mt_1_smile.png",(0,0), "images/sprites/far/mt/mt_1_dress.png") )
            image sl laugh sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_sport.png",(0,0), "images/sprites/far/sl/sl_2_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_sport.png",(0,0), "images/sprites/far/sl/sl_2_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_sport.png",(0,0), "images/sprites/far/sl/sl_2_laugh.png") )
            image us upset sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_sport.png",(0,0), "images/sprites/far/us/us_2_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_sport.png",(0,0), "images/sprites/far/us/us_2_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_sport.png",(0,0), "images/sprites/far/us/us_2_upset.png") )
            image mt normal pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_pioneer.png",(0,0), "images/sprites/far/mt/mt_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_pioneer.png",(0,0), "images/sprites/far/mt/mt_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_pioneer.png",(0,0), "images/sprites/far/mt/mt_1_normal.png") )
            image us cry2 swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_swim.png",(0,0), "images/sprites/far/us/us_3_cry2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_swim.png",(0,0), "images/sprites/far/us/us_3_cry2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_swim.png",(0,0), "images/sprites/far/us/us_3_cry2.png") )
            image mt surprise swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_swim.png",(0,0), "images/sprites/far/mt/mt_1_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_swim.png",(0,0), "images/sprites/far/mt/mt_1_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_swim.png",(0,0), "images/sprites/far/mt/mt_1_surprise.png") )
            image sl smile dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_1_body.png",(0,0), "images/sprites/far/sl/sl_1_dress.png",(0,0), "images/sprites/far/sl/sl_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_1_body.png",(0,0), "images/sprites/far/sl/sl_1_dress.png",(0,0), "images/sprites/far/sl/sl_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_1_body.png",(0,0), "images/sprites/far/sl/sl_1_dress.png",(0,0), "images/sprites/far/sl/sl_1_smile.png") )
            image us upset swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_swim.png",(0,0), "images/sprites/far/us/us_2_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_swim.png",(0,0), "images/sprites/far/us/us_2_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_swim.png",(0,0), "images/sprites/far/us/us_2_upset.png") )
            image un smile sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_sport.png",(0,0), "images/sprites/far/un/un_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_sport.png",(0,0), "images/sprites/far/un/un_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_sport.png",(0,0), "images/sprites/far/un/un_1_smile.png") )
            image un smile pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_pioneer.png",(0,0), "images/sprites/far/un/un_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_pioneer.png",(0,0), "images/sprites/far/un/un_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_pioneer.png",(0,0), "images/sprites/far/un/un_1_smile.png") )
            image us upset dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_dress.png",(0,0), "images/sprites/far/us/us_2_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_dress.png",(0,0), "images/sprites/far/us/us_2_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_dress.png",(0,0), "images/sprites/far/us/us_2_upset.png") )
            image us laugh pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_pioneer.png",(0,0), "images/sprites/far/us/us_1_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_pioneer.png",(0,0), "images/sprites/far/us/us_1_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_pioneer.png",(0,0), "images/sprites/far/us/us_1_laugh.png") )
            image un rage sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_sport.png",(0,0), "images/sprites/far/un/un_3_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_sport.png",(0,0), "images/sprites/far/un/un_3_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_sport.png",(0,0), "images/sprites/far/un/un_3_rage.png") )
            image sl scared pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_4_body.png",(0,0), "images/sprites/far/sl/sl_4_pioneer.png",(0,0), "images/sprites/far/sl/sl_4_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_4_body.png",(0,0), "images/sprites/far/sl/sl_4_pioneer.png",(0,0), "images/sprites/far/sl/sl_4_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_4_body.png",(0,0), "images/sprites/far/sl/sl_4_pioneer.png",(0,0), "images/sprites/far/sl/sl_4_scared.png") )
            image us shy2 sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_sport.png",(0,0), "images/sprites/far/us/us_3_shy2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_sport.png",(0,0), "images/sprites/far/us/us_3_shy2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_sport.png",(0,0), "images/sprites/far/us/us_3_shy2.png") )
            image sl surprise sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_3_body.png",(0,0), "images/sprites/far/sl/sl_3_sport.png",(0,0), "images/sprites/far/sl/sl_3_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_3_body.png",(0,0), "images/sprites/far/sl/sl_3_sport.png",(0,0), "images/sprites/far/sl/sl_3_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_3_body.png",(0,0), "images/sprites/far/sl/sl_3_sport.png",(0,0), "images/sprites/far/sl/sl_3_surprise.png") )
            image us surp1 swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_swim.png",(0,0), "images/sprites/far/us/us_3_surp1.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_swim.png",(0,0), "images/sprites/far/us/us_3_surp1.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_swim.png",(0,0), "images/sprites/far/us/us_3_surp1.png") )
            image mt angry dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_2_body.png",(0,0), "images/sprites/far/mt/mt_2_dress.png",(0,0), "images/sprites/far/mt/mt_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_2_body.png",(0,0), "images/sprites/far/mt/mt_2_dress.png",(0,0), "images/sprites/far/mt/mt_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_2_body.png",(0,0), "images/sprites/far/mt/mt_2_dress.png",(0,0), "images/sprites/far/mt/mt_2_angry.png") )
            image uv upset far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/uv/uv_4_body.png",(0,0), "images/sprites/far/uv/uv_4_pioneer.png",(0,0), "images/sprites/far/uv/uv_4_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/uv/uv_4_body.png",(0,0), "images/sprites/far/uv/uv_4_pioneer.png",(0,0), "images/sprites/far/uv/uv_4_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/uv/uv_4_body.png",(0,0), "images/sprites/far/uv/uv_4_pioneer.png",(0,0), "images/sprites/far/uv/uv_4_upset.png") )
            image sh serious far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_3_body.png",(0,0), "images/sprites/far/sh/sh_3_normal.png",(0,0), "images/sprites/far/sh/sh_3_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_3_body.png",(0,0), "images/sprites/far/sh/sh_3_normal.png",(0,0), "images/sprites/far/sh/sh_3_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_3_body.png",(0,0), "images/sprites/far/sh/sh_3_normal.png",(0,0), "images/sprites/far/sh/sh_3_serious.png") )
            image uv guilty far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/uv/uv_4_body.png",(0,0), "images/sprites/far/uv/uv_4_pioneer.png",(0,0), "images/sprites/far/uv/uv_4_guilty.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/uv/uv_4_body.png",(0,0), "images/sprites/far/uv/uv_4_pioneer.png",(0,0), "images/sprites/far/uv/uv_4_guilty.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/uv/uv_4_body.png",(0,0), "images/sprites/far/uv/uv_4_pioneer.png",(0,0), "images/sprites/far/uv/uv_4_guilty.png") )
            image us calml swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_swim.png",(0,0), "images/sprites/far/us/us_2_calml.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_swim.png",(0,0), "images/sprites/far/us/us_2_calml.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_swim.png",(0,0), "images/sprites/far/us/us_2_calml.png") )
            image us shy2 swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_swim.png",(0,0), "images/sprites/far/us/us_3_shy2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_swim.png",(0,0), "images/sprites/far/us/us_3_shy2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_swim.png",(0,0), "images/sprites/far/us/us_3_shy2.png") )
            image us dontlike dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_dress.png",(0,0), "images/sprites/far/us/us_2_dontlike.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_dress.png",(0,0), "images/sprites/far/us/us_2_dontlike.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_dress.png",(0,0), "images/sprites/far/us/us_2_dontlike.png") )
            image mi smile pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_2_body.png",(0,0), "images/sprites/far/mi/mi_2_pioneer.png",(0,0), "images/sprites/far/mi/mi_2_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_2_body.png",(0,0), "images/sprites/far/mi/mi_2_pioneer.png",(0,0), "images/sprites/far/mi/mi_2_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_2_body.png",(0,0), "images/sprites/far/mi/mi_2_pioneer.png",(0,0), "images/sprites/far/mi/mi_2_smile.png") )
            image us dontlike sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_sport.png",(0,0), "images/sprites/far/us/us_2_dontlike.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_sport.png",(0,0), "images/sprites/far/us/us_2_dontlike.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_sport.png",(0,0), "images/sprites/far/us/us_2_dontlike.png") )
            image un normal pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_pioneer.png",(0,0), "images/sprites/far/un/un_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_pioneer.png",(0,0), "images/sprites/far/un/un_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_pioneer.png",(0,0), "images/sprites/far/un/un_1_normal.png") )
            image us cry pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_pioneer.png",(0,0), "images/sprites/far/us/us_3_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_pioneer.png",(0,0), "images/sprites/far/us/us_3_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_pioneer.png",(0,0), "images/sprites/far/us/us_3_cry.png") )
            image un shy swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_swim.png",(0,0), "images/sprites/far/un/un_1_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_swim.png",(0,0), "images/sprites/far/un/un_1_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_swim.png",(0,0), "images/sprites/far/un/un_1_shy.png") )
            image sl smile2 pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_pioneer.png",(0,0), "images/sprites/far/sl/sl_2_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_pioneer.png",(0,0), "images/sprites/far/sl/sl_2_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_pioneer.png",(0,0), "images/sprites/far/sl/sl_2_smile2.png") )
            image mi cry_smile pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_2_body.png",(0,0), "images/sprites/far/mi/mi_2_pioneer.png",(0,0), "images/sprites/far/mi/mi_2_cry_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_2_body.png",(0,0), "images/sprites/far/mi/mi_2_pioneer.png",(0,0), "images/sprites/far/mi/mi_2_cry_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_2_body.png",(0,0), "images/sprites/far/mi/mi_2_pioneer.png",(0,0), "images/sprites/far/mi/mi_2_cry_smile.png") )
            image un normal swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_swim.png",(0,0), "images/sprites/far/un/un_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_swim.png",(0,0), "images/sprites/far/un/un_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_swim.png",(0,0), "images/sprites/far/un/un_1_normal.png") )
            image dv normal swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_4_body.png",(0,0), "images/sprites/far/dv/dv_4_swim.png",(0,0), "images/sprites/far/dv/dv_4_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_4_body.png",(0,0), "images/sprites/far/dv/dv_4_swim.png",(0,0), "images/sprites/far/dv/dv_4_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_4_body.png",(0,0), "images/sprites/far/dv/dv_4_swim.png",(0,0), "images/sprites/far/dv/dv_4_normal.png") )
            image un scared pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_pioneer.png",(0,0), "images/sprites/far/un/un_2_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_pioneer.png",(0,0), "images/sprites/far/un/un_2_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_pioneer.png",(0,0), "images/sprites/far/un/un_2_scared.png") )
            image dv smile pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_4_body.png",(0,0), "images/sprites/far/dv/dv_4_pioneer.png",(0,0), "images/sprites/far/dv/dv_4_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_4_body.png",(0,0), "images/sprites/far/dv/dv_4_pioneer.png",(0,0), "images/sprites/far/dv/dv_4_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_4_body.png",(0,0), "images/sprites/far/dv/dv_4_pioneer.png",(0,0), "images/sprites/far/dv/dv_4_smile.png") )
            image us shy swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_swim.png",(0,0), "images/sprites/far/us/us_3_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_swim.png",(0,0), "images/sprites/far/us/us_3_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_swim.png",(0,0), "images/sprites/far/us/us_3_shy.png") )
            image cs shy glasses far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/cs/cs_1_body.png",(0,0), "images/sprites/far/cs/cs_1_glasses.png",(0,0), "images/sprites/far/cs/cs_1_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/cs/cs_1_body.png",(0,0), "images/sprites/far/cs/cs_1_glasses.png",(0,0), "images/sprites/far/cs/cs_1_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/cs/cs_1_body.png",(0,0), "images/sprites/far/cs/cs_1_glasses.png",(0,0), "images/sprites/far/cs/cs_1_shy.png") )
            image cs smile stethoscope far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/cs/cs_1_body.png",(0,0), "images/sprites/far/cs/cs_1_stethoscope.png",(0,0), "images/sprites/far/cs/cs_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/cs/cs_1_body.png",(0,0), "images/sprites/far/cs/cs_1_stethoscope.png",(0,0), "images/sprites/far/cs/cs_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/cs/cs_1_body.png",(0,0), "images/sprites/far/cs/cs_1_stethoscope.png",(0,0), "images/sprites/far/cs/cs_1_smile.png") )
            image us grin swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_swim.png",(0,0), "images/sprites/far/us/us_1_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_swim.png",(0,0), "images/sprites/far/us/us_1_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_swim.png",(0,0), "images/sprites/far/us/us_1_grin.png") )
            image sl normal dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_1_body.png",(0,0), "images/sprites/far/sl/sl_1_dress.png",(0,0), "images/sprites/far/sl/sl_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_1_body.png",(0,0), "images/sprites/far/sl/sl_1_dress.png",(0,0), "images/sprites/far/sl/sl_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_1_body.png",(0,0), "images/sprites/far/sl/sl_1_dress.png",(0,0), "images/sprites/far/sl/sl_1_normal.png") )
            image mi cry pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_pioneer.png",(0,0), "images/sprites/far/mi/mi_1_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_pioneer.png",(0,0), "images/sprites/far/mi/mi_1_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_pioneer.png",(0,0), "images/sprites/far/mi/mi_1_cry.png") )
            image mt grin pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_3_body.png",(0,0), "images/sprites/far/mt/mt_3_pioneer.png",(0,0), "images/sprites/far/mt/mt_3_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_3_body.png",(0,0), "images/sprites/far/mt/mt_3_pioneer.png",(0,0), "images/sprites/far/mt/mt_3_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_3_body.png",(0,0), "images/sprites/far/mt/mt_3_pioneer.png",(0,0), "images/sprites/far/mt/mt_3_grin.png") )
            image mt surprise pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_pioneer.png",(0,0), "images/sprites/far/mt/mt_1_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_pioneer.png",(0,0), "images/sprites/far/mt/mt_1_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_pioneer.png",(0,0), "images/sprites/far/mt/mt_1_surprise.png") )
            image dv smile swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_4_body.png",(0,0), "images/sprites/far/dv/dv_4_swim.png",(0,0), "images/sprites/far/dv/dv_4_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_4_body.png",(0,0), "images/sprites/far/dv/dv_4_swim.png",(0,0), "images/sprites/far/dv/dv_4_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_4_body.png",(0,0), "images/sprites/far/dv/dv_4_swim.png",(0,0), "images/sprites/far/dv/dv_4_smile.png") )
            image un laugh dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_dress.png",(0,0), "images/sprites/far/un/un_3_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_dress.png",(0,0), "images/sprites/far/un/un_3_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_dress.png",(0,0), "images/sprites/far/un/un_3_laugh.png") )
            image sl serious pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_1_body.png",(0,0), "images/sprites/far/sl/sl_1_pioneer.png",(0,0), "images/sprites/far/sl/sl_1_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_1_body.png",(0,0), "images/sprites/far/sl/sl_1_pioneer.png",(0,0), "images/sprites/far/sl/sl_1_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_1_body.png",(0,0), "images/sprites/far/sl/sl_1_pioneer.png",(0,0), "images/sprites/far/sl/sl_1_serious.png") )
            image us smile sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_sport.png",(0,0), "images/sprites/far/us/us_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_sport.png",(0,0), "images/sprites/far/us/us_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_sport.png",(0,0), "images/sprites/far/us/us_1_smile.png") )
            image sh serious pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_3_body.png",(0,0), "images/sprites/far/sh/sh_3_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_3_body.png",(0,0), "images/sprites/far/sh/sh_3_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_3_body.png",(0,0), "images/sprites/far/sh/sh_3_serious.png") )
            image un serious sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_sport.png",(0,0), "images/sprites/far/un/un_3_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_sport.png",(0,0), "images/sprites/far/un/un_3_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_sport.png",(0,0), "images/sprites/far/un/un_3_serious.png") )
            image mt normal panama pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_panama.png",(0,0), "images/sprites/far/mt/mt_1_normal.png",(0,0), "images/sprites/far/mt/mt_1_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_panama.png",(0,0), "images/sprites/far/mt/mt_1_normal.png",(0,0), "images/sprites/far/mt/mt_1_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_panama.png",(0,0), "images/sprites/far/mt/mt_1_normal.png",(0,0), "images/sprites/far/mt/mt_1_pioneer.png") )
            image mt sad panama dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_panama.png",(0,0), "images/sprites/far/mt/mt_1_sad.png",(0,0), "images/sprites/far/mt/mt_1_dress.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_panama.png",(0,0), "images/sprites/far/mt/mt_1_sad.png",(0,0), "images/sprites/far/mt/mt_1_dress.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_panama.png",(0,0), "images/sprites/far/mt/mt_1_sad.png",(0,0), "images/sprites/far/mt/mt_1_dress.png") )
            image sl angry dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_3_body.png",(0,0), "images/sprites/far/sl/sl_3_dress.png",(0,0), "images/sprites/far/sl/sl_3_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_3_body.png",(0,0), "images/sprites/far/sl/sl_3_dress.png",(0,0), "images/sprites/far/sl/sl_3_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_3_body.png",(0,0), "images/sprites/far/sl/sl_3_dress.png",(0,0), "images/sprites/far/sl/sl_3_angry.png") )
            image sl surprise dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_3_body.png",(0,0), "images/sprites/far/sl/sl_3_dress.png",(0,0), "images/sprites/far/sl/sl_3_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_3_body.png",(0,0), "images/sprites/far/sl/sl_3_dress.png",(0,0), "images/sprites/far/sl/sl_3_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_3_body.png",(0,0), "images/sprites/far/sl/sl_3_dress.png",(0,0), "images/sprites/far/sl/sl_3_surprise.png") )
            image dv shocked pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_1_body.png",(0,0), "images/sprites/far/dv/dv_1_pioneer.png",(0,0), "images/sprites/far/dv/dv_1_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_1_body.png",(0,0), "images/sprites/far/dv/dv_1_pioneer.png",(0,0), "images/sprites/far/dv/dv_1_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_1_body.png",(0,0), "images/sprites/far/dv/dv_1_pioneer.png",(0,0), "images/sprites/far/dv/dv_1_shocked.png") )
            image us surp2 swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_swim.png",(0,0), "images/sprites/far/us/us_3_surp2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_swim.png",(0,0), "images/sprites/far/us/us_3_surp2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_swim.png",(0,0), "images/sprites/far/us/us_3_surp2.png") )
            image sl tender sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_4_body.png",(0,0), "images/sprites/far/sl/sl_4_sport.png",(0,0), "images/sprites/far/sl/sl_4_tender.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_4_body.png",(0,0), "images/sprites/far/sl/sl_4_sport.png",(0,0), "images/sprites/far/sl/sl_4_tender.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_4_body.png",(0,0), "images/sprites/far/sl/sl_4_sport.png",(0,0), "images/sprites/far/sl/sl_4_tender.png") )
            image sl surprise pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_3_body.png",(0,0), "images/sprites/far/sl/sl_3_pioneer.png",(0,0), "images/sprites/far/sl/sl_3_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_3_body.png",(0,0), "images/sprites/far/sl/sl_3_pioneer.png",(0,0), "images/sprites/far/sl/sl_3_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_3_body.png",(0,0), "images/sprites/far/sl/sl_3_pioneer.png",(0,0), "images/sprites/far/sl/sl_3_surprise.png") )
            image us grin sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_sport.png",(0,0), "images/sprites/far/us/us_1_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_sport.png",(0,0), "images/sprites/far/us/us_1_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_sport.png",(0,0), "images/sprites/far/us/us_1_grin.png") )
            image us laugh2 swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_swim.png",(0,0), "images/sprites/far/us/us_1_laugh2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_swim.png",(0,0), "images/sprites/far/us/us_1_laugh2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_swim.png",(0,0), "images/sprites/far/us/us_1_laugh2.png") )
            image dv guilty pioneer2 far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_3_body.png",(0,0), "images/sprites/far/dv/dv_3_pioneer2.png",(0,0), "images/sprites/far/dv/dv_3_guilty.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_3_body.png",(0,0), "images/sprites/far/dv/dv_3_pioneer2.png",(0,0), "images/sprites/far/dv/dv_3_guilty.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_3_body.png",(0,0), "images/sprites/far/dv/dv_3_pioneer2.png",(0,0), "images/sprites/far/dv/dv_3_guilty.png") )
            image sl smile2 swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_swim.png",(0,0), "images/sprites/far/sl/sl_2_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_swim.png",(0,0), "images/sprites/far/sl/sl_2_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_swim.png",(0,0), "images/sprites/far/sl/sl_2_smile2.png") )
            image mi normal swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_3_body.png",(0,0), "images/sprites/far/mi/mi_3_swim.png",(0,0), "images/sprites/far/mi/mi_3_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_3_body.png",(0,0), "images/sprites/far/mi/mi_3_swim.png",(0,0), "images/sprites/far/mi/mi_3_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_3_body.png",(0,0), "images/sprites/far/mi/mi_3_swim.png",(0,0), "images/sprites/far/mi/mi_3_normal.png") )
            image sl normal sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_1_body.png",(0,0), "images/sprites/far/sl/sl_1_sport.png",(0,0), "images/sprites/far/sl/sl_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_1_body.png",(0,0), "images/sprites/far/sl/sl_1_sport.png",(0,0), "images/sprites/far/sl/sl_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_1_body.png",(0,0), "images/sprites/far/sl/sl_1_sport.png",(0,0), "images/sprites/far/sl/sl_1_normal.png") )
            image mi sad pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_2_body.png",(0,0), "images/sprites/far/mi/mi_2_pioneer.png",(0,0), "images/sprites/far/mi/mi_2_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_2_body.png",(0,0), "images/sprites/far/mi/mi_2_pioneer.png",(0,0), "images/sprites/far/mi/mi_2_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_2_body.png",(0,0), "images/sprites/far/mi/mi_2_pioneer.png",(0,0), "images/sprites/far/mi/mi_2_sad.png") )
            image un smile3 pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_pioneer.png",(0,0), "images/sprites/far/un/un_3_smile3.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_pioneer.png",(0,0), "images/sprites/far/un/un_3_smile3.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_pioneer.png",(0,0), "images/sprites/far/un/un_3_smile3.png") )
            image sl smile2 dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_dress.png",(0,0), "images/sprites/far/sl/sl_2_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_dress.png",(0,0), "images/sprites/far/sl/sl_2_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_dress.png",(0,0), "images/sprites/far/sl/sl_2_smile2.png") )
            image us smile swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_swim.png",(0,0), "images/sprites/far/us/us_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_swim.png",(0,0), "images/sprites/far/us/us_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_swim.png",(0,0), "images/sprites/far/us/us_1_smile.png") )
            image mt rage panama dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_2_body.png",(0,0), "images/sprites/far/mt/mt_2_panama.png",(0,0), "images/sprites/far/mt/mt_2_rage.png",(0,0), "images/sprites/far/mt/mt_2_dress.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_2_body.png",(0,0), "images/sprites/far/mt/mt_2_panama.png",(0,0), "images/sprites/far/mt/mt_2_rage.png",(0,0), "images/sprites/far/mt/mt_2_dress.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_2_body.png",(0,0), "images/sprites/far/mt/mt_2_panama.png",(0,0), "images/sprites/far/mt/mt_2_rage.png",(0,0), "images/sprites/far/mt/mt_2_dress.png") )
            image dv surprise pioneer2 far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_1_body.png",(0,0), "images/sprites/far/dv/dv_1_pioneer2.png",(0,0), "images/sprites/far/dv/dv_1_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_1_body.png",(0,0), "images/sprites/far/dv/dv_1_pioneer2.png",(0,0), "images/sprites/far/dv/dv_1_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_1_body.png",(0,0), "images/sprites/far/dv/dv_1_pioneer2.png",(0,0), "images/sprites/far/dv/dv_1_surprise.png") )
            image us cry2 sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_sport.png",(0,0), "images/sprites/far/us/us_3_cry2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_sport.png",(0,0), "images/sprites/far/us/us_3_cry2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_sport.png",(0,0), "images/sprites/far/us/us_3_cry2.png") )
            image un normal dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_dress.png",(0,0), "images/sprites/far/un/un_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_dress.png",(0,0), "images/sprites/far/un/un_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_dress.png",(0,0), "images/sprites/far/un/un_1_normal.png") )
            image mi smile swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_2_body.png",(0,0), "images/sprites/far/mi/mi_2_swim.png",(0,0), "images/sprites/far/mi/mi_2_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_2_body.png",(0,0), "images/sprites/far/mi/mi_2_swim.png",(0,0), "images/sprites/far/mi/mi_2_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_2_body.png",(0,0), "images/sprites/far/mi/mi_2_swim.png",(0,0), "images/sprites/far/mi/mi_2_smile.png") )
            image cs normal glasses far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/cs/cs_1_body.png",(0,0), "images/sprites/far/cs/cs_1_glasses.png",(0,0), "images/sprites/far/cs/cs_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/cs/cs_1_body.png",(0,0), "images/sprites/far/cs/cs_1_glasses.png",(0,0), "images/sprites/far/cs/cs_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/cs/cs_1_body.png",(0,0), "images/sprites/far/cs/cs_1_glasses.png",(0,0), "images/sprites/far/cs/cs_1_normal.png") )
            image uv rage far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/uv/uv_1_body.png",(0,0), "images/sprites/far/uv/uv_1_pioneer.png",(0,0), "images/sprites/far/uv/uv_1_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/uv/uv_1_body.png",(0,0), "images/sprites/far/uv/uv_1_pioneer.png",(0,0), "images/sprites/far/uv/uv_1_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/uv/uv_1_body.png",(0,0), "images/sprites/far/uv/uv_1_pioneer.png",(0,0), "images/sprites/far/uv/uv_1_rage.png") )
            image sl sad dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_3_body.png",(0,0), "images/sprites/far/sl/sl_3_dress.png",(0,0), "images/sprites/far/sl/sl_3_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_3_body.png",(0,0), "images/sprites/far/sl/sl_3_dress.png",(0,0), "images/sprites/far/sl/sl_3_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_3_body.png",(0,0), "images/sprites/far/sl/sl_3_dress.png",(0,0), "images/sprites/far/sl/sl_3_sad.png") )
            image mt rage swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_2_body.png",(0,0), "images/sprites/far/mt/mt_2_swim.png",(0,0), "images/sprites/far/mt/mt_2_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_2_body.png",(0,0), "images/sprites/far/mt/mt_2_swim.png",(0,0), "images/sprites/far/mt/mt_2_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_2_body.png",(0,0), "images/sprites/far/mt/mt_2_swim.png",(0,0), "images/sprites/far/mt/mt_2_rage.png") )
            image dv rage pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_5_body.png",(0,0), "images/sprites/far/dv/dv_5_pioneer.png",(0,0), "images/sprites/far/dv/dv_5_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_5_body.png",(0,0), "images/sprites/far/dv/dv_5_pioneer.png",(0,0), "images/sprites/far/dv/dv_5_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_5_body.png",(0,0), "images/sprites/far/dv/dv_5_pioneer.png",(0,0), "images/sprites/far/dv/dv_5_rage.png") )
            image el surprise pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/el/el_2_body.png",(0,0), "images/sprites/far/el/el_2_pioneer.png",(0,0), "images/sprites/far/el/el_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/el/el_2_body.png",(0,0), "images/sprites/far/el/el_2_pioneer.png",(0,0), "images/sprites/far/el/el_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/el/el_2_body.png",(0,0), "images/sprites/far/el/el_2_pioneer.png",(0,0), "images/sprites/far/el/el_2_surprise.png") )
            image un cry pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_pioneer.png",(0,0), "images/sprites/far/un/un_2_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_pioneer.png",(0,0), "images/sprites/far/un/un_2_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_pioneer.png",(0,0), "images/sprites/far/un/un_2_cry.png") )
            image mi dontlike pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_pioneer.png",(0,0), "images/sprites/far/mi/mi_1_dontlike.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_pioneer.png",(0,0), "images/sprites/far/mi/mi_1_dontlike.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_pioneer.png",(0,0), "images/sprites/far/mi/mi_1_dontlike.png") )
            image sl shy swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_swim.png",(0,0), "images/sprites/far/sl/sl_2_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_swim.png",(0,0), "images/sprites/far/sl/sl_2_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_swim.png",(0,0), "images/sprites/far/sl/sl_2_shy.png") )
            image el serious pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/el/el_3_body.png",(0,0), "images/sprites/far/el/el_3_pioneer.png",(0,0), "images/sprites/far/el/el_3_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/el/el_3_body.png",(0,0), "images/sprites/far/el/el_3_pioneer.png",(0,0), "images/sprites/far/el/el_3_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/el/el_3_body.png",(0,0), "images/sprites/far/el/el_3_pioneer.png",(0,0), "images/sprites/far/el/el_3_serious.png") )
            image un scared swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_swim.png",(0,0), "images/sprites/far/un/un_2_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_swim.png",(0,0), "images/sprites/far/un/un_2_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_swim.png",(0,0), "images/sprites/far/un/un_2_scared.png") )
            image el scared pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/el/el_2_body.png",(0,0), "images/sprites/far/el/el_2_pioneer.png",(0,0), "images/sprites/far/el/el_2_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/el/el_2_body.png",(0,0), "images/sprites/far/el/el_2_pioneer.png",(0,0), "images/sprites/far/el/el_2_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/el/el_2_body.png",(0,0), "images/sprites/far/el/el_2_pioneer.png",(0,0), "images/sprites/far/el/el_2_scared.png") )
            image mi cry swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_swim.png",(0,0), "images/sprites/far/mi/mi_1_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_swim.png",(0,0), "images/sprites/far/mi/mi_1_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_swim.png",(0,0), "images/sprites/far/mi/mi_1_cry.png") )
            image mz smile pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_3_body.png",(0,0), "images/sprites/far/mz/mz_3_pioneer.png",(0,0), "images/sprites/far/mz/mz_3_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_3_body.png",(0,0), "images/sprites/far/mz/mz_3_pioneer.png",(0,0), "images/sprites/far/mz/mz_3_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_3_body.png",(0,0), "images/sprites/far/mz/mz_3_pioneer.png",(0,0), "images/sprites/far/mz/mz_3_smile.png") )
            image us laugh sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_sport.png",(0,0), "images/sprites/far/us/us_1_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_sport.png",(0,0), "images/sprites/far/us/us_1_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_sport.png",(0,0), "images/sprites/far/us/us_1_laugh.png") )
            image mt surprise dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_dress.png",(0,0), "images/sprites/far/mt/mt_1_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_dress.png",(0,0), "images/sprites/far/mt/mt_1_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_dress.png",(0,0), "images/sprites/far/mt/mt_1_surprise.png") )
            image mt sad panama swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_panama.png",(0,0), "images/sprites/far/mt/mt_1_sad.png",(0,0), "images/sprites/far/mt/mt_1_swim.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_panama.png",(0,0), "images/sprites/far/mt/mt_1_sad.png",(0,0), "images/sprites/far/mt/mt_1_swim.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_panama.png",(0,0), "images/sprites/far/mt/mt_1_sad.png",(0,0), "images/sprites/far/mt/mt_1_swim.png") )
            image sh upset far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_1_body.png",(0,0), "images/sprites/far/sh/sh_1_laugh.png",(0,0), "images/sprites/far/sh/sh_1_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_1_body.png",(0,0), "images/sprites/far/sh/sh_1_laugh.png",(0,0), "images/sprites/far/sh/sh_1_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_1_body.png",(0,0), "images/sprites/far/sh/sh_1_laugh.png",(0,0), "images/sprites/far/sh/sh_1_upset.png") )
            image un evil_smile sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_sport.png",(0,0), "images/sprites/far/un/un_1_evil_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_sport.png",(0,0), "images/sprites/far/un/un_1_evil_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_sport.png",(0,0), "images/sprites/far/un/un_1_evil_smile.png") )
            image uv surprise far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/uv/uv_4_body.png",(0,0), "images/sprites/far/uv/uv_4_pioneer.png",(0,0), "images/sprites/far/uv/uv_4_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/uv/uv_4_body.png",(0,0), "images/sprites/far/uv/uv_4_pioneer.png",(0,0), "images/sprites/far/uv/uv_4_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/uv/uv_4_body.png",(0,0), "images/sprites/far/uv/uv_4_pioneer.png",(0,0), "images/sprites/far/uv/uv_4_surprise.png") )
            image el grin pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/el/el_1_body.png",(0,0), "images/sprites/far/el/el_1_pioneer.png",(0,0), "images/sprites/far/el/el_1_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/el/el_1_body.png",(0,0), "images/sprites/far/el/el_1_pioneer.png",(0,0), "images/sprites/far/el/el_1_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/el/el_1_body.png",(0,0), "images/sprites/far/el/el_1_pioneer.png",(0,0), "images/sprites/far/el/el_1_grin.png") )
            image mt smile swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_swim.png",(0,0), "images/sprites/far/mt/mt_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_swim.png",(0,0), "images/sprites/far/mt/mt_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_swim.png",(0,0), "images/sprites/far/mt/mt_1_smile.png") )
            image us shy sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_sport.png",(0,0), "images/sprites/far/us/us_3_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_sport.png",(0,0), "images/sprites/far/us/us_3_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_sport.png",(0,0), "images/sprites/far/us/us_3_shy.png") )
            image us fear sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_sport.png",(0,0), "images/sprites/far/us/us_2_fear.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_sport.png",(0,0), "images/sprites/far/us/us_2_fear.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_sport.png",(0,0), "images/sprites/far/us/us_2_fear.png") )
            image un evil_smile pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_pioneer.png",(0,0), "images/sprites/far/un/un_1_evil_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_pioneer.png",(0,0), "images/sprites/far/un/un_1_evil_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_pioneer.png",(0,0), "images/sprites/far/un/un_1_evil_smile.png") )
            image us laugh2 pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_pioneer.png",(0,0), "images/sprites/far/us/us_1_laugh2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_pioneer.png",(0,0), "images/sprites/far/us/us_1_laugh2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_pioneer.png",(0,0), "images/sprites/far/us/us_1_laugh2.png") )
            image sl shy pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_pioneer.png",(0,0), "images/sprites/far/sl/sl_2_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_pioneer.png",(0,0), "images/sprites/far/sl/sl_2_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_pioneer.png",(0,0), "images/sprites/far/sl/sl_2_shy.png") )
            image us surp3 pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_pioneer.png",(0,0), "images/sprites/far/us/us_3_surp3.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_pioneer.png",(0,0), "images/sprites/far/us/us_3_surp3.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_pioneer.png",(0,0), "images/sprites/far/us/us_3_surp3.png") )
            image mi laugh swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_swim.png",(0,0), "images/sprites/far/mi/mi_1_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_swim.png",(0,0), "images/sprites/far/mi/mi_1_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_swim.png",(0,0), "images/sprites/far/mi/mi_1_laugh.png") )
            image un smile3 dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_dress.png",(0,0), "images/sprites/far/un/un_3_smile3.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_dress.png",(0,0), "images/sprites/far/un/un_3_smile3.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_dress.png",(0,0), "images/sprites/far/un/un_3_smile3.png") )
            image us surp3 swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_swim.png",(0,0), "images/sprites/far/us/us_3_surp3.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_swim.png",(0,0), "images/sprites/far/us/us_3_surp3.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_swim.png",(0,0), "images/sprites/far/us/us_3_surp3.png") )
            image un grin pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_pioneer.png",(0,0), "images/sprites/far/un/un_3_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_pioneer.png",(0,0), "images/sprites/far/un/un_3_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_pioneer.png",(0,0), "images/sprites/far/un/un_3_grin.png") )
            image mt laugh panama pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_3_body.png",(0,0), "images/sprites/far/mt/mt_3_panama.png",(0,0), "images/sprites/far/mt/mt_3_laugh.png",(0,0), "images/sprites/far/mt/mt_3_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_3_body.png",(0,0), "images/sprites/far/mt/mt_3_panama.png",(0,0), "images/sprites/far/mt/mt_3_laugh.png",(0,0), "images/sprites/far/mt/mt_3_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_3_body.png",(0,0), "images/sprites/far/mt/mt_3_panama.png",(0,0), "images/sprites/far/mt/mt_3_laugh.png",(0,0), "images/sprites/far/mt/mt_3_pioneer.png") )
            image sl shy dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_dress.png",(0,0), "images/sprites/far/sl/sl_2_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_dress.png",(0,0), "images/sprites/far/sl/sl_2_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_dress.png",(0,0), "images/sprites/far/sl/sl_2_shy.png") )
            image el sad pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/el/el_2_body.png",(0,0), "images/sprites/far/el/el_2_pioneer.png",(0,0), "images/sprites/far/el/el_2_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/el/el_2_body.png",(0,0), "images/sprites/far/el/el_2_pioneer.png",(0,0), "images/sprites/far/el/el_2_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/el/el_2_body.png",(0,0), "images/sprites/far/el/el_2_pioneer.png",(0,0), "images/sprites/far/el/el_2_sad.png") )
            image un surprise sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_sport.png",(0,0), "images/sprites/far/un/un_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_sport.png",(0,0), "images/sprites/far/un/un_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_sport.png",(0,0), "images/sprites/far/un/un_2_surprise.png") )
            image mt surprise panama pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_panama.png",(0,0), "images/sprites/far/mt/mt_1_surprise.png",(0,0), "images/sprites/far/mt/mt_1_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_panama.png",(0,0), "images/sprites/far/mt/mt_1_surprise.png",(0,0), "images/sprites/far/mt/mt_1_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_panama.png",(0,0), "images/sprites/far/mt/mt_1_surprise.png",(0,0), "images/sprites/far/mt/mt_1_pioneer.png") )
            image us angry dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_dress.png",(0,0), "images/sprites/far/us/us_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_dress.png",(0,0), "images/sprites/far/us/us_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_dress.png",(0,0), "images/sprites/far/us/us_2_angry.png") )
            image sl serious sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_1_body.png",(0,0), "images/sprites/far/sl/sl_1_sport.png",(0,0), "images/sprites/far/sl/sl_1_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_1_body.png",(0,0), "images/sprites/far/sl/sl_1_sport.png",(0,0), "images/sprites/far/sl/sl_1_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_1_body.png",(0,0), "images/sprites/far/sl/sl_1_sport.png",(0,0), "images/sprites/far/sl/sl_1_serious.png") )
            image un scared sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_sport.png",(0,0), "images/sprites/far/un/un_2_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_sport.png",(0,0), "images/sprites/far/un/un_2_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_sport.png",(0,0), "images/sprites/far/un/un_2_scared.png") )
            image un cry dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_dress.png",(0,0), "images/sprites/far/un/un_2_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_dress.png",(0,0), "images/sprites/far/un/un_2_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_dress.png",(0,0), "images/sprites/far/un/un_2_cry.png") )
            image dv scared pioneer2 far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_1_body.png",(0,0), "images/sprites/far/dv/dv_1_pioneer2.png",(0,0), "images/sprites/far/dv/dv_1_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_1_body.png",(0,0), "images/sprites/far/dv/dv_1_pioneer2.png",(0,0), "images/sprites/far/dv/dv_1_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_1_body.png",(0,0), "images/sprites/far/dv/dv_1_pioneer2.png",(0,0), "images/sprites/far/dv/dv_1_scared.png") )
            image dv shocked pioneer2 far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_1_body.png",(0,0), "images/sprites/far/dv/dv_1_pioneer2.png",(0,0), "images/sprites/far/dv/dv_1_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_1_body.png",(0,0), "images/sprites/far/dv/dv_1_pioneer2.png",(0,0), "images/sprites/far/dv/dv_1_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_1_body.png",(0,0), "images/sprites/far/dv/dv_1_pioneer2.png",(0,0), "images/sprites/far/dv/dv_1_shocked.png") )
            image sl laugh swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_swim.png",(0,0), "images/sprites/far/sl/sl_2_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_swim.png",(0,0), "images/sprites/far/sl/sl_2_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_swim.png",(0,0), "images/sprites/far/sl/sl_2_laugh.png") )
            image us surp1 dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_dress.png",(0,0), "images/sprites/far/us/us_3_surp1.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_dress.png",(0,0), "images/sprites/far/us/us_3_surp1.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_dress.png",(0,0), "images/sprites/far/us/us_3_surp1.png") )
            image dv shocked swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_1_body.png",(0,0), "images/sprites/far/dv/dv_1_swim.png",(0,0), "images/sprites/far/dv/dv_1_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_1_body.png",(0,0), "images/sprites/far/dv/dv_1_swim.png",(0,0), "images/sprites/far/dv/dv_1_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_1_body.png",(0,0), "images/sprites/far/dv/dv_1_swim.png",(0,0), "images/sprites/far/dv/dv_1_shocked.png") )
            image sh laugh far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_1_body.png",(0,0), "images/sprites/far/sh/sh_1_laugh.png",(0,0), "images/sprites/far/sh/sh_1_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_1_body.png",(0,0), "images/sprites/far/sh/sh_1_laugh.png",(0,0), "images/sprites/far/sh/sh_1_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_1_body.png",(0,0), "images/sprites/far/sh/sh_1_laugh.png",(0,0), "images/sprites/far/sh/sh_1_laugh.png") )
            image us surp2 dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_dress.png",(0,0), "images/sprites/far/us/us_3_surp2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_dress.png",(0,0), "images/sprites/far/us/us_3_surp2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_dress.png",(0,0), "images/sprites/far/us/us_3_surp2.png") )
            image uv sad far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/uv/uv_1_body.png",(0,0), "images/sprites/far/uv/uv_1_pioneer.png",(0,0), "images/sprites/far/uv/uv_1_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/uv/uv_1_body.png",(0,0), "images/sprites/far/uv/uv_1_pioneer.png",(0,0), "images/sprites/far/uv/uv_1_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/uv/uv_1_body.png",(0,0), "images/sprites/far/uv/uv_1_pioneer.png",(0,0), "images/sprites/far/uv/uv_1_sad.png") )
            image el angry pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/el/el_3_body.png",(0,0), "images/sprites/far/el/el_3_pioneer.png",(0,0), "images/sprites/far/el/el_3_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/el/el_3_body.png",(0,0), "images/sprites/far/el/el_3_pioneer.png",(0,0), "images/sprites/far/el/el_3_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/el/el_3_body.png",(0,0), "images/sprites/far/el/el_3_pioneer.png",(0,0), "images/sprites/far/el/el_3_angry.png") )
            image us cry2 dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_dress.png",(0,0), "images/sprites/far/us/us_3_cry2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_dress.png",(0,0), "images/sprites/far/us/us_3_cry2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_dress.png",(0,0), "images/sprites/far/us/us_3_cry2.png") )
            image sl sad sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_3_body.png",(0,0), "images/sprites/far/sl/sl_3_sport.png",(0,0), "images/sprites/far/sl/sl_3_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_3_body.png",(0,0), "images/sprites/far/sl/sl_3_sport.png",(0,0), "images/sprites/far/sl/sl_3_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_3_body.png",(0,0), "images/sprites/far/sl/sl_3_sport.png",(0,0), "images/sprites/far/sl/sl_3_sad.png") )
            image mi scared swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_swim.png",(0,0), "images/sprites/far/mi/mi_1_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_swim.png",(0,0), "images/sprites/far/mi/mi_1_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_swim.png",(0,0), "images/sprites/far/mi/mi_1_scared.png") )
            image us laugh swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_swim.png",(0,0), "images/sprites/far/us/us_1_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_swim.png",(0,0), "images/sprites/far/us/us_1_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_swim.png",(0,0), "images/sprites/far/us/us_1_laugh.png") )
            image mi surprise swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_swim.png",(0,0), "images/sprites/far/mi/mi_1_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_swim.png",(0,0), "images/sprites/far/mi/mi_1_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_swim.png",(0,0), "images/sprites/far/mi/mi_1_surprise.png") )
            image sl smile swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_1_body.png",(0,0), "images/sprites/far/sl/sl_1_swim.png",(0,0), "images/sprites/far/sl/sl_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_1_body.png",(0,0), "images/sprites/far/sl/sl_1_swim.png",(0,0), "images/sprites/far/sl/sl_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_1_body.png",(0,0), "images/sprites/far/sl/sl_1_swim.png",(0,0), "images/sprites/far/sl/sl_1_smile.png") )
            image us shy2 dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_dress.png",(0,0), "images/sprites/far/us/us_3_shy2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_dress.png",(0,0), "images/sprites/far/us/us_3_shy2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_dress.png",(0,0), "images/sprites/far/us/us_3_shy2.png") )
            image sl surprise swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_3_body.png",(0,0), "images/sprites/far/sl/sl_3_swim.png",(0,0), "images/sprites/far/sl/sl_3_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_3_body.png",(0,0), "images/sprites/far/sl/sl_3_swim.png",(0,0), "images/sprites/far/sl/sl_3_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_3_body.png",(0,0), "images/sprites/far/sl/sl_3_swim.png",(0,0), "images/sprites/far/sl/sl_3_surprise.png") )
            image dv smile pioneer2 far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_4_body.png",(0,0), "images/sprites/far/dv/dv_4_pioneer2.png",(0,0), "images/sprites/far/dv/dv_4_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_4_body.png",(0,0), "images/sprites/far/dv/dv_4_pioneer2.png",(0,0), "images/sprites/far/dv/dv_4_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_4_body.png",(0,0), "images/sprites/far/dv/dv_4_pioneer2.png",(0,0), "images/sprites/far/dv/dv_4_smile.png") )
            image mt sad dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_dress.png",(0,0), "images/sprites/far/mt/mt_1_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_dress.png",(0,0), "images/sprites/far/mt/mt_1_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_dress.png",(0,0), "images/sprites/far/mt/mt_1_sad.png") )
            image mt smile panama pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_panama.png",(0,0), "images/sprites/far/mt/mt_1_smile.png",(0,0), "images/sprites/far/mt/mt_1_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_panama.png",(0,0), "images/sprites/far/mt/mt_1_smile.png",(0,0), "images/sprites/far/mt/mt_1_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_panama.png",(0,0), "images/sprites/far/mt/mt_1_smile.png",(0,0), "images/sprites/far/mt/mt_1_pioneer.png") )
            image dv angry pioneer2 far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_5_body.png",(0,0), "images/sprites/far/dv/dv_5_pioneer2.png",(0,0), "images/sprites/far/dv/dv_5_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_5_body.png",(0,0), "images/sprites/far/dv/dv_5_pioneer2.png",(0,0), "images/sprites/far/dv/dv_5_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_5_body.png",(0,0), "images/sprites/far/dv/dv_5_pioneer2.png",(0,0), "images/sprites/far/dv/dv_5_angry.png") )
            image uv shocked far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/uv/uv_1_body.png",(0,0), "images/sprites/far/uv/uv_1_pioneer.png",(0,0), "images/sprites/far/uv/uv_1_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/uv/uv_1_body.png",(0,0), "images/sprites/far/uv/uv_1_pioneer.png",(0,0), "images/sprites/far/uv/uv_1_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/uv/uv_1_body.png",(0,0), "images/sprites/far/uv/uv_1_pioneer.png",(0,0), "images/sprites/far/uv/uv_1_shocked.png") )
            image mz shy glasses pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_3_body.png",(0,0), "images/sprites/far/mz/mz_3_glasses.png",(0,0), "images/sprites/far/mz/mz_3_shy.png",(0,0), "images/sprites/far/mz/mz_3_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_3_body.png",(0,0), "images/sprites/far/mz/mz_3_glasses.png",(0,0), "images/sprites/far/mz/mz_3_shy.png",(0,0), "images/sprites/far/mz/mz_3_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_3_body.png",(0,0), "images/sprites/far/mz/mz_3_glasses.png",(0,0), "images/sprites/far/mz/mz_3_shy.png",(0,0), "images/sprites/far/mz/mz_3_pioneer.png") )
            image dv sad pioneer2 far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_3_body.png",(0,0), "images/sprites/far/dv/dv_3_pioneer2.png",(0,0), "images/sprites/far/dv/dv_3_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_3_body.png",(0,0), "images/sprites/far/dv/dv_3_pioneer2.png",(0,0), "images/sprites/far/dv/dv_3_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_3_body.png",(0,0), "images/sprites/far/dv/dv_3_pioneer2.png",(0,0), "images/sprites/far/dv/dv_3_sad.png") )
            image us shy dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_dress.png",(0,0), "images/sprites/far/us/us_3_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_dress.png",(0,0), "images/sprites/far/us/us_3_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_dress.png",(0,0), "images/sprites/far/us/us_3_shy.png") )
            image dv normal pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_4_body.png",(0,0), "images/sprites/far/dv/dv_4_pioneer.png",(0,0), "images/sprites/far/dv/dv_4_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_4_body.png",(0,0), "images/sprites/far/dv/dv_4_pioneer.png",(0,0), "images/sprites/far/dv/dv_4_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_4_body.png",(0,0), "images/sprites/far/dv/dv_4_pioneer.png",(0,0), "images/sprites/far/dv/dv_4_normal.png") )
            image us calml pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_pioneer.png",(0,0), "images/sprites/far/us/us_2_calml.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_pioneer.png",(0,0), "images/sprites/far/us/us_2_calml.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_pioneer.png",(0,0), "images/sprites/far/us/us_2_calml.png") )
            image mt sad swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_swim.png",(0,0), "images/sprites/far/mt/mt_1_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_swim.png",(0,0), "images/sprites/far/mt/mt_1_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_swim.png",(0,0), "images/sprites/far/mt/mt_1_sad.png") )
            image sl tender dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_4_body.png",(0,0), "images/sprites/far/sl/sl_4_dress.png",(0,0), "images/sprites/far/sl/sl_4_tender.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_4_body.png",(0,0), "images/sprites/far/sl/sl_4_dress.png",(0,0), "images/sprites/far/sl/sl_4_tender.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_4_body.png",(0,0), "images/sprites/far/sl/sl_4_dress.png",(0,0), "images/sprites/far/sl/sl_4_tender.png") )
            image uv dontlike far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/uv/uv_1_body.png",(0,0), "images/sprites/far/uv/uv_1_pioneer.png",(0,0), "images/sprites/far/uv/uv_1_dontlike.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/uv/uv_1_body.png",(0,0), "images/sprites/far/uv/uv_1_pioneer.png",(0,0), "images/sprites/far/uv/uv_1_dontlike.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/uv/uv_1_body.png",(0,0), "images/sprites/far/uv/uv_1_pioneer.png",(0,0), "images/sprites/far/uv/uv_1_dontlike.png") )
            image sh surprise far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_3_body.png",(0,0), "images/sprites/far/sh/sh_3_normal.png",(0,0), "images/sprites/far/sh/sh_3_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_3_body.png",(0,0), "images/sprites/far/sh/sh_3_normal.png",(0,0), "images/sprites/far/sh/sh_3_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_3_body.png",(0,0), "images/sprites/far/sh/sh_3_normal.png",(0,0), "images/sprites/far/sh/sh_3_surprise.png") )
            image us dontlike swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_swim.png",(0,0), "images/sprites/far/us/us_2_dontlike.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_swim.png",(0,0), "images/sprites/far/us/us_2_dontlike.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_swim.png",(0,0), "images/sprites/far/us/us_2_dontlike.png") )
            image sl angry pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_3_body.png",(0,0), "images/sprites/far/sl/sl_3_pioneer.png",(0,0), "images/sprites/far/sl/sl_3_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_3_body.png",(0,0), "images/sprites/far/sl/sl_3_pioneer.png",(0,0), "images/sprites/far/sl/sl_3_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_3_body.png",(0,0), "images/sprites/far/sl/sl_3_pioneer.png",(0,0), "images/sprites/far/sl/sl_3_angry.png") )
            image us shy pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_pioneer.png",(0,0), "images/sprites/far/us/us_3_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_pioneer.png",(0,0), "images/sprites/far/us/us_3_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_pioneer.png",(0,0), "images/sprites/far/us/us_3_shy.png") )
            image un cry_smile pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_pioneer.png",(0,0), "images/sprites/far/un/un_2_cry_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_pioneer.png",(0,0), "images/sprites/far/un/un_2_cry_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_pioneer.png",(0,0), "images/sprites/far/un/un_2_cry_smile.png") )
            image un shy pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_pioneer.png",(0,0), "images/sprites/far/un/un_1_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_pioneer.png",(0,0), "images/sprites/far/un/un_1_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_pioneer.png",(0,0), "images/sprites/far/un/un_1_shy.png") )
            image mt normal panama swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_panama.png",(0,0), "images/sprites/far/mt/mt_1_normal.png",(0,0), "images/sprites/far/mt/mt_1_swim.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_panama.png",(0,0), "images/sprites/far/mt/mt_1_normal.png",(0,0), "images/sprites/far/mt/mt_1_swim.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_panama.png",(0,0), "images/sprites/far/mt/mt_1_normal.png",(0,0), "images/sprites/far/mt/mt_1_swim.png") )
            image sl normal swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_1_body.png",(0,0), "images/sprites/far/sl/sl_1_swim.png",(0,0), "images/sprites/far/sl/sl_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_1_body.png",(0,0), "images/sprites/far/sl/sl_1_swim.png",(0,0), "images/sprites/far/sl/sl_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_1_body.png",(0,0), "images/sprites/far/sl/sl_1_swim.png",(0,0), "images/sprites/far/sl/sl_1_normal.png") )
            image mz laugh pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_1_body.png",(0,0), "images/sprites/far/mz/mz_1_pioneer.png",(0,0), "images/sprites/far/mz/mz_1_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_1_body.png",(0,0), "images/sprites/far/mz/mz_1_pioneer.png",(0,0), "images/sprites/far/mz/mz_1_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_1_body.png",(0,0), "images/sprites/far/mz/mz_1_pioneer.png",(0,0), "images/sprites/far/mz/mz_1_laugh.png") )
            image dv surprise swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_1_body.png",(0,0), "images/sprites/far/dv/dv_1_swim.png",(0,0), "images/sprites/far/dv/dv_1_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_1_body.png",(0,0), "images/sprites/far/dv/dv_1_swim.png",(0,0), "images/sprites/far/dv/dv_1_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_1_body.png",(0,0), "images/sprites/far/dv/dv_1_swim.png",(0,0), "images/sprites/far/dv/dv_1_surprise.png") )
            image sl laugh pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_pioneer.png",(0,0), "images/sprites/far/sl/sl_2_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_pioneer.png",(0,0), "images/sprites/far/sl/sl_2_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_pioneer.png",(0,0), "images/sprites/far/sl/sl_2_laugh.png") )
            image sh laugh pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_1_body.png",(0,0), "images/sprites/far/sh/sh_1_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_1_body.png",(0,0), "images/sprites/far/sh/sh_1_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_1_body.png",(0,0), "images/sprites/far/sh/sh_1_laugh.png") )
            image sl smile sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_1_body.png",(0,0), "images/sprites/far/sl/sl_1_sport.png",(0,0), "images/sprites/far/sl/sl_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_1_body.png",(0,0), "images/sprites/far/sl/sl_1_sport.png",(0,0), "images/sprites/far/sl/sl_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_1_body.png",(0,0), "images/sprites/far/sl/sl_1_sport.png",(0,0), "images/sprites/far/sl/sl_1_smile.png") )
            image sl scared swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_4_body.png",(0,0), "images/sprites/far/sl/sl_4_swim.png",(0,0), "images/sprites/far/sl/sl_4_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_4_body.png",(0,0), "images/sprites/far/sl/sl_4_swim.png",(0,0), "images/sprites/far/sl/sl_4_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_4_body.png",(0,0), "images/sprites/far/sl/sl_4_swim.png",(0,0), "images/sprites/far/sl/sl_4_scared.png") )
            image un scared dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_dress.png",(0,0), "images/sprites/far/un/un_2_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_dress.png",(0,0), "images/sprites/far/un/un_2_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_dress.png",(0,0), "images/sprites/far/un/un_2_scared.png") )
            image sl serious swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_1_body.png",(0,0), "images/sprites/far/sl/sl_1_swim.png",(0,0), "images/sprites/far/sl/sl_1_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_1_body.png",(0,0), "images/sprites/far/sl/sl_1_swim.png",(0,0), "images/sprites/far/sl/sl_1_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_1_body.png",(0,0), "images/sprites/far/sl/sl_1_swim.png",(0,0), "images/sprites/far/sl/sl_1_serious.png") )
            image mt normal dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_dress.png",(0,0), "images/sprites/far/mt/mt_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_dress.png",(0,0), "images/sprites/far/mt/mt_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_dress.png",(0,0), "images/sprites/far/mt/mt_1_normal.png") )
            image us grin dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_dress.png",(0,0), "images/sprites/far/us/us_1_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_dress.png",(0,0), "images/sprites/far/us/us_1_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_dress.png",(0,0), "images/sprites/far/us/us_1_grin.png") )
            image sl laugh dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_dress.png",(0,0), "images/sprites/far/sl/sl_2_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_dress.png",(0,0), "images/sprites/far/sl/sl_2_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_dress.png",(0,0), "images/sprites/far/sl/sl_2_laugh.png") )
            image us laugh dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_dress.png",(0,0), "images/sprites/far/us/us_1_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_dress.png",(0,0), "images/sprites/far/us/us_1_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_dress.png",(0,0), "images/sprites/far/us/us_1_laugh.png") )
            image dv cry swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_1_body.png",(0,0), "images/sprites/far/dv/dv_1_swim.png",(0,0), "images/sprites/far/dv/dv_1_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_1_body.png",(0,0), "images/sprites/far/dv/dv_1_swim.png",(0,0), "images/sprites/far/dv/dv_1_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_1_body.png",(0,0), "images/sprites/far/dv/dv_1_swim.png",(0,0), "images/sprites/far/dv/dv_1_cry.png") )
            image cs shy stethoscope far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/cs/cs_1_body.png",(0,0), "images/sprites/far/cs/cs_1_stethoscope.png",(0,0), "images/sprites/far/cs/cs_1_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/cs/cs_1_body.png",(0,0), "images/sprites/far/cs/cs_1_stethoscope.png",(0,0), "images/sprites/far/cs/cs_1_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/cs/cs_1_body.png",(0,0), "images/sprites/far/cs/cs_1_stethoscope.png",(0,0), "images/sprites/far/cs/cs_1_shy.png") )
            image sh upset pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_1_body.png",(0,0), "images/sprites/far/sh/sh_1_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_1_body.png",(0,0), "images/sprites/far/sh/sh_1_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_1_body.png",(0,0), "images/sprites/far/sh/sh_1_upset.png") )
            image mz shy pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_3_body.png",(0,0), "images/sprites/far/mz/mz_3_pioneer.png",(0,0), "images/sprites/far/mz/mz_3_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_3_body.png",(0,0), "images/sprites/far/mz/mz_3_pioneer.png",(0,0), "images/sprites/far/mz/mz_3_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_3_body.png",(0,0), "images/sprites/far/mz/mz_3_pioneer.png",(0,0), "images/sprites/far/mz/mz_3_shy.png") )
            image mz laugh glasses pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_1_body.png",(0,0), "images/sprites/far/mz/mz_1_glasses.png",(0,0), "images/sprites/far/mz/mz_1_laugh.png",(0,0), "images/sprites/far/mz/mz_1_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_1_body.png",(0,0), "images/sprites/far/mz/mz_1_glasses.png",(0,0), "images/sprites/far/mz/mz_1_laugh.png",(0,0), "images/sprites/far/mz/mz_1_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_1_body.png",(0,0), "images/sprites/far/mz/mz_1_glasses.png",(0,0), "images/sprites/far/mz/mz_1_laugh.png",(0,0), "images/sprites/far/mz/mz_1_pioneer.png") )
            image mz normal glasses pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_1_body.png",(0,0), "images/sprites/far/mz/mz_1_glasses.png",(0,0), "images/sprites/far/mz/mz_1_normal.png",(0,0), "images/sprites/far/mz/mz_1_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_1_body.png",(0,0), "images/sprites/far/mz/mz_1_glasses.png",(0,0), "images/sprites/far/mz/mz_1_normal.png",(0,0), "images/sprites/far/mz/mz_1_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_1_body.png",(0,0), "images/sprites/far/mz/mz_1_glasses.png",(0,0), "images/sprites/far/mz/mz_1_normal.png",(0,0), "images/sprites/far/mz/mz_1_pioneer.png") )
            image cs shy far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/cs/cs_1_body.png",(0,0), "images/sprites/far/cs/cs_1_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/cs/cs_1_body.png",(0,0), "images/sprites/far/cs/cs_1_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/cs/cs_1_body.png",(0,0), "images/sprites/far/cs/cs_1_shy.png") )
            image pi far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/pi/pi_1_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/pi/pi_1_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/pi/pi_1_pioneer.png") )
            image mz bukal glasses pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_1_body.png",(0,0), "images/sprites/far/mz/mz_1_glasses.png",(0,0), "images/sprites/far/mz/mz_1_bukal.png",(0,0), "images/sprites/far/mz/mz_1_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_1_body.png",(0,0), "images/sprites/far/mz/mz_1_glasses.png",(0,0), "images/sprites/far/mz/mz_1_bukal.png",(0,0), "images/sprites/far/mz/mz_1_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_1_body.png",(0,0), "images/sprites/far/mz/mz_1_glasses.png",(0,0), "images/sprites/far/mz/mz_1_bukal.png",(0,0), "images/sprites/far/mz/mz_1_pioneer.png") )
            image mi rage pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_3_body.png",(0,0), "images/sprites/far/mi/mi_3_pioneer.png",(0,0), "images/sprites/far/mi/mi_3_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_3_body.png",(0,0), "images/sprites/far/mi/mi_3_pioneer.png",(0,0), "images/sprites/far/mi/mi_3_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_3_body.png",(0,0), "images/sprites/far/mi/mi_3_pioneer.png",(0,0), "images/sprites/far/mi/mi_3_rage.png") )
            image sl normal pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_1_body.png",(0,0), "images/sprites/far/sl/sl_1_pioneer.png",(0,0), "images/sprites/far/sl/sl_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_1_body.png",(0,0), "images/sprites/far/sl/sl_1_pioneer.png",(0,0), "images/sprites/far/sl/sl_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_1_body.png",(0,0), "images/sprites/far/sl/sl_1_pioneer.png",(0,0), "images/sprites/far/sl/sl_1_normal.png") )
            image mi rage swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_3_body.png",(0,0), "images/sprites/far/mi/mi_3_swim.png",(0,0), "images/sprites/far/mi/mi_3_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_3_body.png",(0,0), "images/sprites/far/mi/mi_3_swim.png",(0,0), "images/sprites/far/mi/mi_3_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_3_body.png",(0,0), "images/sprites/far/mi/mi_3_swim.png",(0,0), "images/sprites/far/mi/mi_3_rage.png") )
            image el upset pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/el/el_2_body.png",(0,0), "images/sprites/far/el/el_2_pioneer.png",(0,0), "images/sprites/far/el/el_2_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/el/el_2_body.png",(0,0), "images/sprites/far/el/el_2_pioneer.png",(0,0), "images/sprites/far/el/el_2_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/el/el_2_body.png",(0,0), "images/sprites/far/el/el_2_pioneer.png",(0,0), "images/sprites/far/el/el_2_upset.png") )
            image us normal pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_pioneer.png",(0,0), "images/sprites/far/us/us_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_pioneer.png",(0,0), "images/sprites/far/us/us_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_pioneer.png",(0,0), "images/sprites/far/us/us_1_normal.png") )
            image un shy dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_dress.png",(0,0), "images/sprites/far/un/un_1_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_dress.png",(0,0), "images/sprites/far/un/un_1_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_dress.png",(0,0), "images/sprites/far/un/un_1_shy.png") )
            image mt surprise panama swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_panama.png",(0,0), "images/sprites/far/mt/mt_1_surprise.png",(0,0), "images/sprites/far/mt/mt_1_swim.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_panama.png",(0,0), "images/sprites/far/mt/mt_1_surprise.png",(0,0), "images/sprites/far/mt/mt_1_swim.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_panama.png",(0,0), "images/sprites/far/mt/mt_1_surprise.png",(0,0), "images/sprites/far/mt/mt_1_swim.png") )
            image us sad sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_sport.png",(0,0), "images/sprites/far/us/us_1_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_sport.png",(0,0), "images/sprites/far/us/us_1_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_sport.png",(0,0), "images/sprites/far/us/us_1_sad.png") )
            image mi angry swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_3_body.png",(0,0), "images/sprites/far/mi/mi_3_swim.png",(0,0), "images/sprites/far/mi/mi_3_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_3_body.png",(0,0), "images/sprites/far/mi/mi_3_swim.png",(0,0), "images/sprites/far/mi/mi_3_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_3_body.png",(0,0), "images/sprites/far/mi/mi_3_swim.png",(0,0), "images/sprites/far/mi/mi_3_angry.png") )
            image sl happy pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_pioneer.png",(0,0), "images/sprites/far/sl/sl_2_happy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_pioneer.png",(0,0), "images/sprites/far/sl/sl_2_happy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_pioneer.png",(0,0), "images/sprites/far/sl/sl_2_happy.png") )
            image mt sad panama pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_panama.png",(0,0), "images/sprites/far/mt/mt_1_sad.png",(0,0), "images/sprites/far/mt/mt_1_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_panama.png",(0,0), "images/sprites/far/mt/mt_1_sad.png",(0,0), "images/sprites/far/mt/mt_1_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_panama.png",(0,0), "images/sprites/far/mt/mt_1_sad.png",(0,0), "images/sprites/far/mt/mt_1_pioneer.png") )
            image us calml sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_sport.png",(0,0), "images/sprites/far/us/us_2_calml.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_sport.png",(0,0), "images/sprites/far/us/us_2_calml.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_sport.png",(0,0), "images/sprites/far/us/us_2_calml.png") )
            image us shy2 pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_pioneer.png",(0,0), "images/sprites/far/us/us_3_shy2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_pioneer.png",(0,0), "images/sprites/far/us/us_3_shy2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_pioneer.png",(0,0), "images/sprites/far/us/us_3_shy2.png") )
            image un surprise pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_pioneer.png",(0,0), "images/sprites/far/un/un_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_pioneer.png",(0,0), "images/sprites/far/un/un_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_pioneer.png",(0,0), "images/sprites/far/un/un_2_surprise.png") )
            image us cry sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_sport.png",(0,0), "images/sprites/far/us/us_3_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_sport.png",(0,0), "images/sprites/far/us/us_3_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_sport.png",(0,0), "images/sprites/far/us/us_3_cry.png") )
            image mi angry pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_3_body.png",(0,0), "images/sprites/far/mi/mi_3_pioneer.png",(0,0), "images/sprites/far/mi/mi_3_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_3_body.png",(0,0), "images/sprites/far/mi/mi_3_pioneer.png",(0,0), "images/sprites/far/mi/mi_3_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_3_body.png",(0,0), "images/sprites/far/mi/mi_3_pioneer.png",(0,0), "images/sprites/far/mi/mi_3_angry.png") )
            image us sad pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_pioneer.png",(0,0), "images/sprites/far/us/us_1_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_pioneer.png",(0,0), "images/sprites/far/us/us_1_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_pioneer.png",(0,0), "images/sprites/far/us/us_1_sad.png") )
            image uv smile far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/uv/uv_2_body.png",(0,0), "images/sprites/far/uv/uv_2_pioneer.png",(0,0), "images/sprites/far/uv/uv_2_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/uv/uv_2_body.png",(0,0), "images/sprites/far/uv/uv_2_pioneer.png",(0,0), "images/sprites/far/uv/uv_2_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/uv/uv_2_body.png",(0,0), "images/sprites/far/uv/uv_2_pioneer.png",(0,0), "images/sprites/far/uv/uv_2_smile.png") )
            image un cry swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_swim.png",(0,0), "images/sprites/far/un/un_2_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_swim.png",(0,0), "images/sprites/far/un/un_2_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_swim.png",(0,0), "images/sprites/far/un/un_2_cry.png") )
            image sh normal pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_3_body.png",(0,0), "images/sprites/far/sh/sh_3_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_3_body.png",(0,0), "images/sprites/far/sh/sh_3_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_3_body.png",(0,0), "images/sprites/far/sh/sh_3_normal.png") )
            image sh rage far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_2_body.png",(0,0), "images/sprites/far/sh/sh_2_rage.png",(0,0), "images/sprites/far/sh/sh_2_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_2_body.png",(0,0), "images/sprites/far/sh/sh_2_rage.png",(0,0), "images/sprites/far/sh/sh_2_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_2_body.png",(0,0), "images/sprites/far/sh/sh_2_rage.png",(0,0), "images/sprites/far/sh/sh_2_rage.png") )
            image us normal sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_sport.png",(0,0), "images/sprites/far/us/us_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_sport.png",(0,0), "images/sprites/far/us/us_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_sport.png",(0,0), "images/sprites/far/us/us_1_normal.png") )
            image un angry2 sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_sport.png",(0,0), "images/sprites/far/un/un_3_angry2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_sport.png",(0,0), "images/sprites/far/un/un_3_angry2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_sport.png",(0,0), "images/sprites/far/un/un_3_angry2.png") )
            image sl happy swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_swim.png",(0,0), "images/sprites/far/sl/sl_2_happy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_swim.png",(0,0), "images/sprites/far/sl/sl_2_happy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_swim.png",(0,0), "images/sprites/far/sl/sl_2_happy.png") )
            image mz rage glasses pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_2_body.png",(0,0), "images/sprites/far/mz/mz_2_glasses.png",(0,0), "images/sprites/far/mz/mz_2_rage.png",(0,0), "images/sprites/far/mz/mz_2_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_2_body.png",(0,0), "images/sprites/far/mz/mz_2_glasses.png",(0,0), "images/sprites/far/mz/mz_2_rage.png",(0,0), "images/sprites/far/mz/mz_2_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_2_body.png",(0,0), "images/sprites/far/mz/mz_2_glasses.png",(0,0), "images/sprites/far/mz/mz_2_rage.png",(0,0), "images/sprites/far/mz/mz_2_pioneer.png") )
            image us smile pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_pioneer.png",(0,0), "images/sprites/far/us/us_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_pioneer.png",(0,0), "images/sprites/far/us/us_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_pioneer.png",(0,0), "images/sprites/far/us/us_1_smile.png") )
            image mt angry panama swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_2_body.png",(0,0), "images/sprites/far/mt/mt_2_panama.png",(0,0), "images/sprites/far/mt/mt_2_angry.png",(0,0), "images/sprites/far/mt/mt_2_swim.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_2_body.png",(0,0), "images/sprites/far/mt/mt_2_panama.png",(0,0), "images/sprites/far/mt/mt_2_angry.png",(0,0), "images/sprites/far/mt/mt_2_swim.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_2_body.png",(0,0), "images/sprites/far/mt/mt_2_panama.png",(0,0), "images/sprites/far/mt/mt_2_angry.png",(0,0), "images/sprites/far/mt/mt_2_swim.png") )
            image sh cry pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_2_body.png",(0,0), "images/sprites/far/sh/sh_2_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_2_body.png",(0,0), "images/sprites/far/sh/sh_2_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_2_body.png",(0,0), "images/sprites/far/sh/sh_2_cry.png") )
            image mz smile glasses pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_3_body.png",(0,0), "images/sprites/far/mz/mz_3_glasses.png",(0,0), "images/sprites/far/mz/mz_3_smile.png",(0,0), "images/sprites/far/mz/mz_3_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_3_body.png",(0,0), "images/sprites/far/mz/mz_3_glasses.png",(0,0), "images/sprites/far/mz/mz_3_smile.png",(0,0), "images/sprites/far/mz/mz_3_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_3_body.png",(0,0), "images/sprites/far/mz/mz_3_glasses.png",(0,0), "images/sprites/far/mz/mz_3_smile.png",(0,0), "images/sprites/far/mz/mz_3_pioneer.png") )
            image sh scared pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_1_body.png",(0,0), "images/sprites/far/sh/sh_1_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_1_body.png",(0,0), "images/sprites/far/sh/sh_1_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_1_body.png",(0,0), "images/sprites/far/sh/sh_1_scared.png") )
            image mi upset pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_3_body.png",(0,0), "images/sprites/far/mi/mi_3_pioneer.png",(0,0), "images/sprites/far/mi/mi_3_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_3_body.png",(0,0), "images/sprites/far/mi/mi_3_pioneer.png",(0,0), "images/sprites/far/mi/mi_3_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_3_body.png",(0,0), "images/sprites/far/mi/mi_3_pioneer.png",(0,0), "images/sprites/far/mi/mi_3_upset.png") )
            image mi upset swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_3_body.png",(0,0), "images/sprites/far/mi/mi_3_swim.png",(0,0), "images/sprites/far/mi/mi_3_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_3_body.png",(0,0), "images/sprites/far/mi/mi_3_swim.png",(0,0), "images/sprites/far/mi/mi_3_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_3_body.png",(0,0), "images/sprites/far/mi/mi_3_swim.png",(0,0), "images/sprites/far/mi/mi_3_upset.png") )
            image us normal swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_swim.png",(0,0), "images/sprites/far/us/us_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_swim.png",(0,0), "images/sprites/far/us/us_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_swim.png",(0,0), "images/sprites/far/us/us_1_normal.png") )
            image sh normal far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_3_body.png",(0,0), "images/sprites/far/sh/sh_3_normal.png",(0,0), "images/sprites/far/sh/sh_3_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_3_body.png",(0,0), "images/sprites/far/sh/sh_3_normal.png",(0,0), "images/sprites/far/sh/sh_3_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_3_body.png",(0,0), "images/sprites/far/sh/sh_3_normal.png",(0,0), "images/sprites/far/sh/sh_3_normal.png") )
            image un shocked dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_dress.png",(0,0), "images/sprites/far/un/un_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_dress.png",(0,0), "images/sprites/far/un/un_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_dress.png",(0,0), "images/sprites/far/un/un_2_shocked.png") )
            image un angry sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_sport.png",(0,0), "images/sprites/far/un/un_1_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_sport.png",(0,0), "images/sprites/far/un/un_1_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_sport.png",(0,0), "images/sprites/far/un/un_1_angry.png") )
            image el smile pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/el/el_1_body.png",(0,0), "images/sprites/far/el/el_1_pioneer.png",(0,0), "images/sprites/far/el/el_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/el/el_1_body.png",(0,0), "images/sprites/far/el/el_1_pioneer.png",(0,0), "images/sprites/far/el/el_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/el/el_1_body.png",(0,0), "images/sprites/far/el/el_1_pioneer.png",(0,0), "images/sprites/far/el/el_1_smile.png") )
            image mi cry_smile swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_2_body.png",(0,0), "images/sprites/far/mi/mi_2_swim.png",(0,0), "images/sprites/far/mi/mi_2_cry_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_2_body.png",(0,0), "images/sprites/far/mi/mi_2_swim.png",(0,0), "images/sprites/far/mi/mi_2_cry_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_2_body.png",(0,0), "images/sprites/far/mi/mi_2_swim.png",(0,0), "images/sprites/far/mi/mi_2_cry_smile.png") )
            image mi grin pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_2_body.png",(0,0), "images/sprites/far/mi/mi_2_pioneer.png",(0,0), "images/sprites/far/mi/mi_2_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_2_body.png",(0,0), "images/sprites/far/mi/mi_2_pioneer.png",(0,0), "images/sprites/far/mi/mi_2_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_2_body.png",(0,0), "images/sprites/far/mi/mi_2_pioneer.png",(0,0), "images/sprites/far/mi/mi_2_grin.png") )
            image sl scared dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_4_body.png",(0,0), "images/sprites/far/sl/sl_4_dress.png",(0,0), "images/sprites/far/sl/sl_4_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_4_body.png",(0,0), "images/sprites/far/sl/sl_4_dress.png",(0,0), "images/sprites/far/sl/sl_4_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_4_body.png",(0,0), "images/sprites/far/sl/sl_4_dress.png",(0,0), "images/sprites/far/sl/sl_4_scared.png") )
            image un cry_smile dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_dress.png",(0,0), "images/sprites/far/un/un_2_cry_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_dress.png",(0,0), "images/sprites/far/un/un_2_cry_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_dress.png",(0,0), "images/sprites/far/un/un_2_cry_smile.png") )
            image un cry_smile sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_sport.png",(0,0), "images/sprites/far/un/un_2_cry_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_sport.png",(0,0), "images/sprites/far/un/un_2_cry_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_sport.png",(0,0), "images/sprites/far/un/un_2_cry_smile.png") )
            image un sad sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_sport.png",(0,0), "images/sprites/far/un/un_2_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_sport.png",(0,0), "images/sprites/far/un/un_2_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_sport.png",(0,0), "images/sprites/far/un/un_2_sad.png") )
            image mt surprise panama dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_panama.png",(0,0), "images/sprites/far/mt/mt_1_surprise.png",(0,0), "images/sprites/far/mt/mt_1_dress.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_panama.png",(0,0), "images/sprites/far/mt/mt_1_surprise.png",(0,0), "images/sprites/far/mt/mt_1_dress.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_panama.png",(0,0), "images/sprites/far/mt/mt_1_surprise.png",(0,0), "images/sprites/far/mt/mt_1_dress.png") )
            image dv normal pioneer2 far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_4_body.png",(0,0), "images/sprites/far/dv/dv_4_pioneer2.png",(0,0), "images/sprites/far/dv/dv_4_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_4_body.png",(0,0), "images/sprites/far/dv/dv_4_pioneer2.png",(0,0), "images/sprites/far/dv/dv_4_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_4_body.png",(0,0), "images/sprites/far/dv/dv_4_pioneer2.png",(0,0), "images/sprites/far/dv/dv_4_normal.png") )
            image mz angry glasses pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_2_body.png",(0,0), "images/sprites/far/mz/mz_2_glasses.png",(0,0), "images/sprites/far/mz/mz_2_angry.png",(0,0), "images/sprites/far/mz/mz_2_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_2_body.png",(0,0), "images/sprites/far/mz/mz_2_glasses.png",(0,0), "images/sprites/far/mz/mz_2_angry.png",(0,0), "images/sprites/far/mz/mz_2_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_2_body.png",(0,0), "images/sprites/far/mz/mz_2_glasses.png",(0,0), "images/sprites/far/mz/mz_2_angry.png",(0,0), "images/sprites/far/mz/mz_2_pioneer.png") )
            image us cry2 pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_pioneer.png",(0,0), "images/sprites/far/us/us_3_cry2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_pioneer.png",(0,0), "images/sprites/far/us/us_3_cry2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_pioneer.png",(0,0), "images/sprites/far/us/us_3_cry2.png") )
            image mi sad swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_2_body.png",(0,0), "images/sprites/far/mi/mi_2_swim.png",(0,0), "images/sprites/far/mi/mi_2_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_2_body.png",(0,0), "images/sprites/far/mi/mi_2_swim.png",(0,0), "images/sprites/far/mi/mi_2_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_2_body.png",(0,0), "images/sprites/far/mi/mi_2_swim.png",(0,0), "images/sprites/far/mi/mi_2_sad.png") )
            image un sad swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_swim.png",(0,0), "images/sprites/far/un/un_2_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_swim.png",(0,0), "images/sprites/far/un/un_2_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_swim.png",(0,0), "images/sprites/far/un/un_2_sad.png") )
            image us laugh2 sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_sport.png",(0,0), "images/sprites/far/us/us_1_laugh2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_sport.png",(0,0), "images/sprites/far/us/us_1_laugh2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_sport.png",(0,0), "images/sprites/far/us/us_1_laugh2.png") )
            image dv angry pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_5_body.png",(0,0), "images/sprites/far/dv/dv_5_pioneer.png",(0,0), "images/sprites/far/dv/dv_5_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_5_body.png",(0,0), "images/sprites/far/dv/dv_5_pioneer.png",(0,0), "images/sprites/far/dv/dv_5_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_5_body.png",(0,0), "images/sprites/far/dv/dv_5_pioneer.png",(0,0), "images/sprites/far/dv/dv_5_angry.png") )
            image mt smile pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_pioneer.png",(0,0), "images/sprites/far/mt/mt_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_pioneer.png",(0,0), "images/sprites/far/mt/mt_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_pioneer.png",(0,0), "images/sprites/far/mt/mt_1_smile.png") )
            image mi shy swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_swim.png",(0,0), "images/sprites/far/mi/mi_1_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_swim.png",(0,0), "images/sprites/far/mi/mi_1_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_swim.png",(0,0), "images/sprites/far/mi/mi_1_shy.png") )
            image un grin dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_dress.png",(0,0), "images/sprites/far/un/un_3_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_dress.png",(0,0), "images/sprites/far/un/un_3_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_dress.png",(0,0), "images/sprites/far/un/un_3_grin.png") )
            image mt laugh pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_3_body.png",(0,0), "images/sprites/far/mt/mt_3_pioneer.png",(0,0), "images/sprites/far/mt/mt_3_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_3_body.png",(0,0), "images/sprites/far/mt/mt_3_pioneer.png",(0,0), "images/sprites/far/mt/mt_3_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_3_body.png",(0,0), "images/sprites/far/mt/mt_3_pioneer.png",(0,0), "images/sprites/far/mt/mt_3_laugh.png") )
            image un laugh pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_pioneer.png",(0,0), "images/sprites/far/un/un_3_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_pioneer.png",(0,0), "images/sprites/far/un/un_3_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_pioneer.png",(0,0), "images/sprites/far/un/un_3_laugh.png") )
            image dv laugh pioneer2 far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_4_body.png",(0,0), "images/sprites/far/dv/dv_4_pioneer2.png",(0,0), "images/sprites/far/dv/dv_4_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_4_body.png",(0,0), "images/sprites/far/dv/dv_4_pioneer2.png",(0,0), "images/sprites/far/dv/dv_4_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_4_body.png",(0,0), "images/sprites/far/dv/dv_4_pioneer2.png",(0,0), "images/sprites/far/dv/dv_4_laugh.png") )
            image us surp1 pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_pioneer.png",(0,0), "images/sprites/far/us/us_3_surp1.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_pioneer.png",(0,0), "images/sprites/far/us/us_3_surp1.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_pioneer.png",(0,0), "images/sprites/far/us/us_3_surp1.png") )
            image sh rage pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_2_body.png",(0,0), "images/sprites/far/sh/sh_2_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_2_body.png",(0,0), "images/sprites/far/sh/sh_2_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_2_body.png",(0,0), "images/sprites/far/sh/sh_2_rage.png") )
            image mt angry panama dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_2_body.png",(0,0), "images/sprites/far/mt/mt_2_panama.png",(0,0), "images/sprites/far/mt/mt_2_angry.png",(0,0), "images/sprites/far/mt/mt_2_dress.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_2_body.png",(0,0), "images/sprites/far/mt/mt_2_panama.png",(0,0), "images/sprites/far/mt/mt_2_angry.png",(0,0), "images/sprites/far/mt/mt_2_dress.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_2_body.png",(0,0), "images/sprites/far/mt/mt_2_panama.png",(0,0), "images/sprites/far/mt/mt_2_angry.png",(0,0), "images/sprites/far/mt/mt_2_dress.png") )
            image un shocked swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_swim.png",(0,0), "images/sprites/far/un/un_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_swim.png",(0,0), "images/sprites/far/un/un_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_swim.png",(0,0), "images/sprites/far/un/un_2_shocked.png") )
            image un evil_smile dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_dress.png",(0,0), "images/sprites/far/un/un_1_evil_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_dress.png",(0,0), "images/sprites/far/un/un_1_evil_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_dress.png",(0,0), "images/sprites/far/un/un_1_evil_smile.png") )
            image uv laugh far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/uv/uv_3_body.png",(0,0), "images/sprites/far/uv/uv_3_pioneer.png",(0,0), "images/sprites/far/uv/uv_3_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/uv/uv_3_body.png",(0,0), "images/sprites/far/uv/uv_3_pioneer.png",(0,0), "images/sprites/far/uv/uv_3_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/uv/uv_3_body.png",(0,0), "images/sprites/far/uv/uv_3_pioneer.png",(0,0), "images/sprites/far/uv/uv_3_laugh.png") )
            image dv scared swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_1_body.png",(0,0), "images/sprites/far/dv/dv_1_swim.png",(0,0), "images/sprites/far/dv/dv_1_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_1_body.png",(0,0), "images/sprites/far/dv/dv_1_swim.png",(0,0), "images/sprites/far/dv/dv_1_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_1_body.png",(0,0), "images/sprites/far/dv/dv_1_swim.png",(0,0), "images/sprites/far/dv/dv_1_scared.png") )
            image mi shocked swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_swim.png",(0,0), "images/sprites/far/mi/mi_1_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_swim.png",(0,0), "images/sprites/far/mi/mi_1_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_swim.png",(0,0), "images/sprites/far/mi/mi_1_shocked.png") )
            image mt angry pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_2_body.png",(0,0), "images/sprites/far/mt/mt_2_pioneer.png",(0,0), "images/sprites/far/mt/mt_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_2_body.png",(0,0), "images/sprites/far/mt/mt_2_pioneer.png",(0,0), "images/sprites/far/mt/mt_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_2_body.png",(0,0), "images/sprites/far/mt/mt_2_pioneer.png",(0,0), "images/sprites/far/mt/mt_2_angry.png") )
            image el fingal pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/el/el_2_body.png",(0,0), "images/sprites/far/el/el_2_pioneer.png",(0,0), "images/sprites/far/el/el_2_fingal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/el/el_2_body.png",(0,0), "images/sprites/far/el/el_2_pioneer.png",(0,0), "images/sprites/far/el/el_2_fingal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/el/el_2_body.png",(0,0), "images/sprites/far/el/el_2_pioneer.png",(0,0), "images/sprites/far/el/el_2_fingal.png") )
            image us surp3 sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_sport.png",(0,0), "images/sprites/far/us/us_3_surp3.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_sport.png",(0,0), "images/sprites/far/us/us_3_surp3.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_sport.png",(0,0), "images/sprites/far/us/us_3_surp3.png") )
            image sl happy dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_dress.png",(0,0), "images/sprites/far/sl/sl_2_happy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_dress.png",(0,0), "images/sprites/far/sl/sl_2_happy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_dress.png",(0,0), "images/sprites/far/sl/sl_2_happy.png") )
            image sh scared far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_1_body.png",(0,0), "images/sprites/far/sh/sh_1_laugh.png",(0,0), "images/sprites/far/sh/sh_1_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_1_body.png",(0,0), "images/sprites/far/sh/sh_1_laugh.png",(0,0), "images/sprites/far/sh/sh_1_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sh/sh_1_body.png",(0,0), "images/sprites/far/sh/sh_1_laugh.png",(0,0), "images/sprites/far/sh/sh_1_scared.png") )
            image un angry2 pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_pioneer.png",(0,0), "images/sprites/far/un/un_3_angry2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_pioneer.png",(0,0), "images/sprites/far/un/un_3_angry2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_pioneer.png",(0,0), "images/sprites/far/un/un_3_angry2.png") )
            image uv grin far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/uv/uv_3_body.png",(0,0), "images/sprites/far/uv/uv_3_pioneer.png",(0,0), "images/sprites/far/uv/uv_3_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/uv/uv_3_body.png",(0,0), "images/sprites/far/uv/uv_3_pioneer.png",(0,0), "images/sprites/far/uv/uv_3_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/uv/uv_3_body.png",(0,0), "images/sprites/far/uv/uv_3_pioneer.png",(0,0), "images/sprites/far/uv/uv_3_grin.png") )
            image mi shy pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_pioneer.png",(0,0), "images/sprites/far/mi/mi_1_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_pioneer.png",(0,0), "images/sprites/far/mi/mi_1_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_pioneer.png",(0,0), "images/sprites/far/mi/mi_1_shy.png") )
            image sl sad pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_3_body.png",(0,0), "images/sprites/far/sl/sl_3_pioneer.png",(0,0), "images/sprites/far/sl/sl_3_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_3_body.png",(0,0), "images/sprites/far/sl/sl_3_pioneer.png",(0,0), "images/sprites/far/sl/sl_3_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_3_body.png",(0,0), "images/sprites/far/sl/sl_3_pioneer.png",(0,0), "images/sprites/far/sl/sl_3_sad.png") )
            image un smile2 sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_sport.png",(0,0), "images/sprites/far/un/un_1_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_sport.png",(0,0), "images/sprites/far/un/un_1_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_sport.png",(0,0), "images/sprites/far/un/un_1_smile2.png") )
            image us cry dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_dress.png",(0,0), "images/sprites/far/us/us_3_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_dress.png",(0,0), "images/sprites/far/us/us_3_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_dress.png",(0,0), "images/sprites/far/us/us_3_cry.png") )
            image un rage pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_pioneer.png",(0,0), "images/sprites/far/un/un_3_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_pioneer.png",(0,0), "images/sprites/far/un/un_3_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_pioneer.png",(0,0), "images/sprites/far/un/un_3_rage.png") )
            image sl sad swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_3_body.png",(0,0), "images/sprites/far/sl/sl_3_swim.png",(0,0), "images/sprites/far/sl/sl_3_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_3_body.png",(0,0), "images/sprites/far/sl/sl_3_swim.png",(0,0), "images/sprites/far/sl/sl_3_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_3_body.png",(0,0), "images/sprites/far/sl/sl_3_swim.png",(0,0), "images/sprites/far/sl/sl_3_sad.png") )
            image mi normal pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_3_body.png",(0,0), "images/sprites/far/mi/mi_3_pioneer.png",(0,0), "images/sprites/far/mi/mi_3_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_3_body.png",(0,0), "images/sprites/far/mi/mi_3_pioneer.png",(0,0), "images/sprites/far/mi/mi_3_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_3_body.png",(0,0), "images/sprites/far/mi/mi_3_pioneer.png",(0,0), "images/sprites/far/mi/mi_3_normal.png") )
            image us surp1 sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_sport.png",(0,0), "images/sprites/far/us/us_3_surp1.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_sport.png",(0,0), "images/sprites/far/us/us_3_surp1.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_sport.png",(0,0), "images/sprites/far/us/us_3_surp1.png") )
            image us cry swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_swim.png",(0,0), "images/sprites/far/us/us_3_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_swim.png",(0,0), "images/sprites/far/us/us_3_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_swim.png",(0,0), "images/sprites/far/us/us_3_cry.png") )
            image un serious dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_dress.png",(0,0), "images/sprites/far/un/un_3_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_dress.png",(0,0), "images/sprites/far/un/un_3_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_dress.png",(0,0), "images/sprites/far/un/un_3_serious.png") )
            image un laugh sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_sport.png",(0,0), "images/sprites/far/un/un_3_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_sport.png",(0,0), "images/sprites/far/un/un_3_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_sport.png",(0,0), "images/sprites/far/un/un_3_laugh.png") )
            image un surprise dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_dress.png",(0,0), "images/sprites/far/un/un_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_dress.png",(0,0), "images/sprites/far/un/un_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_dress.png",(0,0), "images/sprites/far/un/un_2_surprise.png") )
            image mi happy swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_2_body.png",(0,0), "images/sprites/far/mi/mi_2_swim.png",(0,0), "images/sprites/far/mi/mi_2_happy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_2_body.png",(0,0), "images/sprites/far/mi/mi_2_swim.png",(0,0), "images/sprites/far/mi/mi_2_happy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_2_body.png",(0,0), "images/sprites/far/mi/mi_2_swim.png",(0,0), "images/sprites/far/mi/mi_2_happy.png") )
            image mi serious swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_3_body.png",(0,0), "images/sprites/far/mi/mi_3_swim.png",(0,0), "images/sprites/far/mi/mi_3_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_3_body.png",(0,0), "images/sprites/far/mi/mi_3_swim.png",(0,0), "images/sprites/far/mi/mi_3_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_3_body.png",(0,0), "images/sprites/far/mi/mi_3_swim.png",(0,0), "images/sprites/far/mi/mi_3_serious.png") )
            image uv surprise2 far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/uv/uv_3_body.png",(0,0), "images/sprites/far/uv/uv_3_pioneer.png",(0,0), "images/sprites/far/uv/uv_3_surprise2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/uv/uv_3_body.png",(0,0), "images/sprites/far/uv/uv_3_pioneer.png",(0,0), "images/sprites/far/uv/uv_3_surprise2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/uv/uv_3_body.png",(0,0), "images/sprites/far/uv/uv_3_pioneer.png",(0,0), "images/sprites/far/uv/uv_3_surprise2.png") )
            image mz angry pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_2_body.png",(0,0), "images/sprites/far/mz/mz_2_pioneer.png",(0,0), "images/sprites/far/mz/mz_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_2_body.png",(0,0), "images/sprites/far/mz/mz_2_pioneer.png",(0,0), "images/sprites/far/mz/mz_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_2_body.png",(0,0), "images/sprites/far/mz/mz_2_pioneer.png",(0,0), "images/sprites/far/mz/mz_2_angry.png") )
            image un sad pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_pioneer.png",(0,0), "images/sprites/far/un/un_2_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_pioneer.png",(0,0), "images/sprites/far/un/un_2_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_pioneer.png",(0,0), "images/sprites/far/un/un_2_sad.png") )
            image dv surprise pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_1_body.png",(0,0), "images/sprites/far/dv/dv_1_pioneer.png",(0,0), "images/sprites/far/dv/dv_1_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_1_body.png",(0,0), "images/sprites/far/dv/dv_1_pioneer.png",(0,0), "images/sprites/far/dv/dv_1_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_1_body.png",(0,0), "images/sprites/far/dv/dv_1_pioneer.png",(0,0), "images/sprites/far/dv/dv_1_surprise.png") )
            image mz bukal pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_1_body.png",(0,0), "images/sprites/far/mz/mz_1_pioneer.png",(0,0), "images/sprites/far/mz/mz_1_bukal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_1_body.png",(0,0), "images/sprites/far/mz/mz_1_pioneer.png",(0,0), "images/sprites/far/mz/mz_1_bukal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mz/mz_1_body.png",(0,0), "images/sprites/far/mz/mz_1_pioneer.png",(0,0), "images/sprites/far/mz/mz_1_bukal.png") )
            image mi shocked pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_pioneer.png",(0,0), "images/sprites/far/mi/mi_1_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_pioneer.png",(0,0), "images/sprites/far/mi/mi_1_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_pioneer.png",(0,0), "images/sprites/far/mi/mi_1_shocked.png") )
            image sl happy sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_sport.png",(0,0), "images/sprites/far/sl/sl_2_happy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_sport.png",(0,0), "images/sprites/far/sl/sl_2_happy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_2_body.png",(0,0), "images/sprites/far/sl/sl_2_sport.png",(0,0), "images/sprites/far/sl/sl_2_happy.png") )
            image un sad dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_dress.png",(0,0), "images/sprites/far/un/un_2_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_dress.png",(0,0), "images/sprites/far/un/un_2_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_dress.png",(0,0), "images/sprites/far/un/un_2_sad.png") )
            image dv cry pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_1_body.png",(0,0), "images/sprites/far/dv/dv_1_pioneer.png",(0,0), "images/sprites/far/dv/dv_1_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_1_body.png",(0,0), "images/sprites/far/dv/dv_1_pioneer.png",(0,0), "images/sprites/far/dv/dv_1_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_1_body.png",(0,0), "images/sprites/far/dv/dv_1_pioneer.png",(0,0), "images/sprites/far/dv/dv_1_cry.png") )
            image sl angry swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_3_body.png",(0,0), "images/sprites/far/sl/sl_3_swim.png",(0,0), "images/sprites/far/sl/sl_3_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_3_body.png",(0,0), "images/sprites/far/sl/sl_3_swim.png",(0,0), "images/sprites/far/sl/sl_3_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_3_body.png",(0,0), "images/sprites/far/sl/sl_3_swim.png",(0,0), "images/sprites/far/sl/sl_3_angry.png") )
            image un rage dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_dress.png",(0,0), "images/sprites/far/un/un_3_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_dress.png",(0,0), "images/sprites/far/un/un_3_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_3_body.png",(0,0), "images/sprites/far/un/un_3_dress.png",(0,0), "images/sprites/far/un/un_3_rage.png") )
            image us normal dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_dress.png",(0,0), "images/sprites/far/us/us_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_dress.png",(0,0), "images/sprites/far/us/us_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_1_body.png",(0,0), "images/sprites/far/us/us_1_dress.png",(0,0), "images/sprites/far/us/us_1_normal.png") )
            image sl angry sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_3_body.png",(0,0), "images/sprites/far/sl/sl_3_sport.png",(0,0), "images/sprites/far/sl/sl_3_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_3_body.png",(0,0), "images/sprites/far/sl/sl_3_sport.png",(0,0), "images/sprites/far/sl/sl_3_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/sl/sl_3_body.png",(0,0), "images/sprites/far/sl/sl_3_sport.png",(0,0), "images/sprites/far/sl/sl_3_angry.png") )
            image us fear pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_pioneer.png",(0,0), "images/sprites/far/us/us_2_fear.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_pioneer.png",(0,0), "images/sprites/far/us/us_2_fear.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_pioneer.png",(0,0), "images/sprites/far/us/us_2_fear.png") )
            image mt normal panama dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_panama.png",(0,0), "images/sprites/far/mt/mt_1_normal.png",(0,0), "images/sprites/far/mt/mt_1_dress.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_panama.png",(0,0), "images/sprites/far/mt/mt_1_normal.png",(0,0), "images/sprites/far/mt/mt_1_dress.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_1_body.png",(0,0), "images/sprites/far/mt/mt_1_panama.png",(0,0), "images/sprites/far/mt/mt_1_normal.png",(0,0), "images/sprites/far/mt/mt_1_dress.png") )
            image mi serious pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_3_body.png",(0,0), "images/sprites/far/mi/mi_3_pioneer.png",(0,0), "images/sprites/far/mi/mi_3_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_3_body.png",(0,0), "images/sprites/far/mi/mi_3_pioneer.png",(0,0), "images/sprites/far/mi/mi_3_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_3_body.png",(0,0), "images/sprites/far/mi/mi_3_pioneer.png",(0,0), "images/sprites/far/mi/mi_3_serious.png") )
            image un shocked pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_pioneer.png",(0,0), "images/sprites/far/un/un_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_pioneer.png",(0,0), "images/sprites/far/un/un_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_pioneer.png",(0,0), "images/sprites/far/un/un_2_shocked.png") )
            image dv grin pioneer2 far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_2_body.png",(0,0), "images/sprites/far/dv/dv_2_pioneer2.png",(0,0), "images/sprites/far/dv/dv_2_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_2_body.png",(0,0), "images/sprites/far/dv/dv_2_pioneer2.png",(0,0), "images/sprites/far/dv/dv_2_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_2_body.png",(0,0), "images/sprites/far/dv/dv_2_pioneer2.png",(0,0), "images/sprites/far/dv/dv_2_grin.png") )
            image dv grin pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_2_body.png",(0,0), "images/sprites/far/dv/dv_2_pioneer.png",(0,0), "images/sprites/far/dv/dv_2_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_2_body.png",(0,0), "images/sprites/far/dv/dv_2_pioneer.png",(0,0), "images/sprites/far/dv/dv_2_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/dv/dv_2_body.png",(0,0), "images/sprites/far/dv/dv_2_pioneer.png",(0,0), "images/sprites/far/dv/dv_2_grin.png") )
            image mt rage dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_2_body.png",(0,0), "images/sprites/far/mt/mt_2_dress.png",(0,0), "images/sprites/far/mt/mt_2_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_2_body.png",(0,0), "images/sprites/far/mt/mt_2_dress.png",(0,0), "images/sprites/far/mt/mt_2_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_2_body.png",(0,0), "images/sprites/far/mt/mt_2_dress.png",(0,0), "images/sprites/far/mt/mt_2_rage.png") )
            image us angry sport far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_sport.png",(0,0), "images/sprites/far/us/us_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_sport.png",(0,0), "images/sprites/far/us/us_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_sport.png",(0,0), "images/sprites/far/us/us_2_angry.png") )
            image mi grin swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_2_body.png",(0,0), "images/sprites/far/mi/mi_2_swim.png",(0,0), "images/sprites/far/mi/mi_2_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_2_body.png",(0,0), "images/sprites/far/mi/mi_2_swim.png",(0,0), "images/sprites/far/mi/mi_2_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_2_body.png",(0,0), "images/sprites/far/mi/mi_2_swim.png",(0,0), "images/sprites/far/mi/mi_2_grin.png") )
            image mt angry swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_2_body.png",(0,0), "images/sprites/far/mt/mt_2_swim.png",(0,0), "images/sprites/far/mt/mt_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_2_body.png",(0,0), "images/sprites/far/mt/mt_2_swim.png",(0,0), "images/sprites/far/mt/mt_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mt/mt_2_body.png",(0,0), "images/sprites/far/mt/mt_2_swim.png",(0,0), "images/sprites/far/mt/mt_2_angry.png") )
            image un surprise swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_swim.png",(0,0), "images/sprites/far/un/un_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_swim.png",(0,0), "images/sprites/far/un/un_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_2_body.png",(0,0), "images/sprites/far/un/un_2_swim.png",(0,0), "images/sprites/far/un/un_2_surprise.png") )
            image el shocked pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/el/el_2_body.png",(0,0), "images/sprites/far/el/el_2_pioneer.png",(0,0), "images/sprites/far/el/el_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/el/el_2_body.png",(0,0), "images/sprites/far/el/el_2_pioneer.png",(0,0), "images/sprites/far/el/el_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/el/el_2_body.png",(0,0), "images/sprites/far/el/el_2_pioneer.png",(0,0), "images/sprites/far/el/el_2_shocked.png") )
            image us calml dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_dress.png",(0,0), "images/sprites/far/us/us_2_calml.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_dress.png",(0,0), "images/sprites/far/us/us_2_calml.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_2_body.png",(0,0), "images/sprites/far/us/us_2_dress.png",(0,0), "images/sprites/far/us/us_2_calml.png") )
            image us surp3 dress far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_dress.png",(0,0), "images/sprites/far/us/us_3_surp3.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_dress.png",(0,0), "images/sprites/far/us/us_3_surp3.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/us/us_3_body.png",(0,0), "images/sprites/far/us/us_3_dress.png",(0,0), "images/sprites/far/us/us_3_surp3.png") )
            image un smile swim far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_swim.png",(0,0), "images/sprites/far/un/un_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_swim.png",(0,0), "images/sprites/far/un/un_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/un/un_1_body.png",(0,0), "images/sprites/far/un/un_1_swim.png",(0,0), "images/sprites/far/un/un_1_smile.png") )
            image mi surprise pioneer far = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_pioneer.png",(0,0), "images/sprites/far/mi/mi_1_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_pioneer.png",(0,0), "images/sprites/far/mi/mi_1_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((420,720), (0,0), "images/sprites/far/mi/mi_1_body.png",(0,0), "images/sprites/far/mi/mi_1_pioneer.png",(0,0), "images/sprites/far/mi/mi_1_surprise.png") )
            image cs normal stethoscope = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/cs/cs_1_body.png",(0,0), "images/sprites/normal/cs/cs_1_stethoscope.png",(0,0), "images/sprites/normal/cs/cs_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/cs/cs_1_body.png",(0,0), "images/sprites/normal/cs/cs_1_stethoscope.png",(0,0), "images/sprites/normal/cs/cs_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/cs/cs_1_body.png",(0,0), "images/sprites/normal/cs/cs_1_stethoscope.png",(0,0), "images/sprites/normal/cs/cs_1_normal.png") )
            image dv grin swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_2_body.png",(0,0), "images/sprites/normal/dv/dv_2_swim.png",(0,0), "images/sprites/normal/dv/dv_2_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_2_body.png",(0,0), "images/sprites/normal/dv/dv_2_swim.png",(0,0), "images/sprites/normal/dv/dv_2_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_2_body.png",(0,0), "images/sprites/normal/dv/dv_2_swim.png",(0,0), "images/sprites/normal/dv/dv_2_grin.png") )
            image dv laugh swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_4_body.png",(0,0), "images/sprites/normal/dv/dv_4_swim.png",(0,0), "images/sprites/normal/dv/dv_4_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_4_body.png",(0,0), "images/sprites/normal/dv/dv_4_swim.png",(0,0), "images/sprites/normal/dv/dv_4_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_4_body.png",(0,0), "images/sprites/normal/dv/dv_4_swim.png",(0,0), "images/sprites/normal/dv/dv_4_laugh.png") )
            image dv scared pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_pioneer.png",(0,0), "images/sprites/normal/dv/dv_1_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_pioneer.png",(0,0), "images/sprites/normal/dv/dv_1_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_pioneer.png",(0,0), "images/sprites/normal/dv/dv_1_scared.png") )
            image sl smile2 sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_sport.png",(0,0), "images/sprites/normal/sl/sl_2_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_sport.png",(0,0), "images/sprites/normal/sl/sl_2_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_sport.png",(0,0), "images/sprites/normal/sl/sl_2_smile2.png") )
            image dv rage pioneer2 = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_5_body.png",(0,0), "images/sprites/normal/dv/dv_5_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_5_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_5_body.png",(0,0), "images/sprites/normal/dv/dv_5_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_5_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_5_body.png",(0,0), "images/sprites/normal/dv/dv_5_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_5_rage.png") )
            image mi scared pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_pioneer.png",(0,0), "images/sprites/normal/mi/mi_1_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_pioneer.png",(0,0), "images/sprites/normal/mi/mi_1_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_pioneer.png",(0,0), "images/sprites/normal/mi/mi_1_scared.png") )
            image us grin pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_pioneer.png",(0,0), "images/sprites/normal/us/us_1_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_pioneer.png",(0,0), "images/sprites/normal/us/us_1_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_pioneer.png",(0,0), "images/sprites/normal/us/us_1_grin.png") )
            image un angry swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_swim.png",(0,0), "images/sprites/normal/un/un_1_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_swim.png",(0,0), "images/sprites/normal/un/un_1_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_swim.png",(0,0), "images/sprites/normal/un/un_1_angry.png") )
            image mi happy pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_2_body.png",(0,0), "images/sprites/normal/mi/mi_2_pioneer.png",(0,0), "images/sprites/normal/mi/mi_2_happy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_2_body.png",(0,0), "images/sprites/normal/mi/mi_2_pioneer.png",(0,0), "images/sprites/normal/mi/mi_2_happy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_2_body.png",(0,0), "images/sprites/normal/mi/mi_2_pioneer.png",(0,0), "images/sprites/normal/mi/mi_2_happy.png") )
            image un serious pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_pioneer.png",(0,0), "images/sprites/normal/un/un_3_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_pioneer.png",(0,0), "images/sprites/normal/un/un_3_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_pioneer.png",(0,0), "images/sprites/normal/un/un_3_serious.png") )
            image us surp2 sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_sport.png",(0,0), "images/sprites/normal/us/us_3_surp2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_sport.png",(0,0), "images/sprites/normal/us/us_3_surp2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_sport.png",(0,0), "images/sprites/normal/us/us_3_surp2.png") )
            image un smile2 dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_dress.png",(0,0), "images/sprites/normal/un/un_1_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_dress.png",(0,0), "images/sprites/normal/un/un_1_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_dress.png",(0,0), "images/sprites/normal/un/un_1_smile2.png") )
            image us surp2 pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_pioneer.png",(0,0), "images/sprites/normal/us/us_3_surp2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_pioneer.png",(0,0), "images/sprites/normal/us/us_3_surp2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_pioneer.png",(0,0), "images/sprites/normal/us/us_3_surp2.png") )
            image sl shy sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_sport.png",(0,0), "images/sprites/normal/sl/sl_2_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_sport.png",(0,0), "images/sprites/normal/sl/sl_2_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_sport.png",(0,0), "images/sprites/normal/sl/sl_2_shy.png") )
            image cs smile = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/cs/cs_1_body.png",(0,0), "images/sprites/normal/cs/cs_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/cs/cs_1_body.png",(0,0), "images/sprites/normal/cs/cs_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/cs/cs_1_body.png",(0,0), "images/sprites/normal/cs/cs_1_smile.png") )
            image mz rage pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_2_body.png",(0,0), "images/sprites/normal/mz/mz_2_pioneer.png",(0,0), "images/sprites/normal/mz/mz_2_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_2_body.png",(0,0), "images/sprites/normal/mz/mz_2_pioneer.png",(0,0), "images/sprites/normal/mz/mz_2_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_2_body.png",(0,0), "images/sprites/normal/mz/mz_2_pioneer.png",(0,0), "images/sprites/normal/mz/mz_2_rage.png") )
            image un cry sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_sport.png",(0,0), "images/sprites/normal/un/un_2_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_sport.png",(0,0), "images/sprites/normal/un/un_2_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_sport.png",(0,0), "images/sprites/normal/un/un_2_cry.png") )
            image un evil_smile swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_swim.png",(0,0), "images/sprites/normal/un/un_1_evil_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_swim.png",(0,0), "images/sprites/normal/un/un_1_evil_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_swim.png",(0,0), "images/sprites/normal/un/un_1_evil_smile.png") )
            image sh smile pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_1_body.png",(0,0), "images/sprites/normal/sh/sh_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_1_body.png",(0,0), "images/sprites/normal/sh/sh_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_1_body.png",(0,0), "images/sprites/normal/sh/sh_1_smile.png") )
            image us sad swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_swim.png",(0,0), "images/sprites/normal/us/us_1_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_swim.png",(0,0), "images/sprites/normal/us/us_1_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_swim.png",(0,0), "images/sprites/normal/us/us_1_sad.png") )
            image sh cry = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_2_body.png",(0,0), "images/sprites/normal/sh/sh_2_rage.png",(0,0), "images/sprites/normal/sh/sh_2_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_2_body.png",(0,0), "images/sprites/normal/sh/sh_2_rage.png",(0,0), "images/sprites/normal/sh/sh_2_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_2_body.png",(0,0), "images/sprites/normal/sh/sh_2_rage.png",(0,0), "images/sprites/normal/sh/sh_2_cry.png") )
            image sh surprise pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_3_body.png",(0,0), "images/sprites/normal/sh/sh_3_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_3_body.png",(0,0), "images/sprites/normal/sh/sh_3_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_3_body.png",(0,0), "images/sprites/normal/sh/sh_3_surprise.png") )
            image mt grin panama pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_3_body.png",(0,0), "images/sprites/normal/mt/mt_3_panama.png",(0,0), "images/sprites/normal/mt/mt_3_grin.png",(0,0), "images/sprites/normal/mt/mt_3_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_3_body.png",(0,0), "images/sprites/normal/mt/mt_3_panama.png",(0,0), "images/sprites/normal/mt/mt_3_grin.png",(0,0), "images/sprites/normal/mt/mt_3_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_3_body.png",(0,0), "images/sprites/normal/mt/mt_3_panama.png",(0,0), "images/sprites/normal/mt/mt_3_grin.png",(0,0), "images/sprites/normal/mt/mt_3_pioneer.png") )
            image dv sad pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_3_body.png",(0,0), "images/sprites/normal/dv/dv_3_pioneer.png",(0,0), "images/sprites/normal/dv/dv_3_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_3_body.png",(0,0), "images/sprites/normal/dv/dv_3_pioneer.png",(0,0), "images/sprites/normal/dv/dv_3_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_3_body.png",(0,0), "images/sprites/normal/dv/dv_3_pioneer.png",(0,0), "images/sprites/normal/dv/dv_3_sad.png") )
            image mt smile panama swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_panama.png",(0,0), "images/sprites/normal/mt/mt_1_smile.png",(0,0), "images/sprites/normal/mt/mt_1_swim.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_panama.png",(0,0), "images/sprites/normal/mt/mt_1_smile.png",(0,0), "images/sprites/normal/mt/mt_1_swim.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_panama.png",(0,0), "images/sprites/normal/mt/mt_1_smile.png",(0,0), "images/sprites/normal/mt/mt_1_swim.png") )
            image dv cry pioneer2 = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_1_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_1_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_1_cry.png") )
            image mt rage panama pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_panama.png",(0,0), "images/sprites/normal/mt/mt_2_rage.png",(0,0), "images/sprites/normal/mt/mt_2_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_panama.png",(0,0), "images/sprites/normal/mt/mt_2_rage.png",(0,0), "images/sprites/normal/mt/mt_2_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_panama.png",(0,0), "images/sprites/normal/mt/mt_2_rage.png",(0,0), "images/sprites/normal/mt/mt_2_pioneer.png") )
            image un smile dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_dress.png",(0,0), "images/sprites/normal/un/un_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_dress.png",(0,0), "images/sprites/normal/un/un_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_dress.png",(0,0), "images/sprites/normal/un/un_1_smile.png") )
            image mi dontlike swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_swim.png",(0,0), "images/sprites/normal/mi/mi_1_dontlike.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_swim.png",(0,0), "images/sprites/normal/mi/mi_1_dontlike.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_swim.png",(0,0), "images/sprites/normal/mi/mi_1_dontlike.png") )
            image un angry2 dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_dress.png",(0,0), "images/sprites/normal/un/un_3_angry2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_dress.png",(0,0), "images/sprites/normal/un/un_3_angry2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_dress.png",(0,0), "images/sprites/normal/un/un_3_angry2.png") )
            image sl serious dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_1_body.png",(0,0), "images/sprites/normal/sl/sl_1_dress.png",(0,0), "images/sprites/normal/sl/sl_1_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_1_body.png",(0,0), "images/sprites/normal/sl/sl_1_dress.png",(0,0), "images/sprites/normal/sl/sl_1_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_1_body.png",(0,0), "images/sprites/normal/sl/sl_1_dress.png",(0,0), "images/sprites/normal/sl/sl_1_serious.png") )
            image dv guilty pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_3_body.png",(0,0), "images/sprites/normal/dv/dv_3_pioneer.png",(0,0), "images/sprites/normal/dv/dv_3_guilty.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_3_body.png",(0,0), "images/sprites/normal/dv/dv_3_pioneer.png",(0,0), "images/sprites/normal/dv/dv_3_guilty.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_3_body.png",(0,0), "images/sprites/normal/dv/dv_3_pioneer.png",(0,0), "images/sprites/normal/dv/dv_3_guilty.png") )
            image mz normal pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_1_body.png",(0,0), "images/sprites/normal/mz/mz_1_pioneer.png",(0,0), "images/sprites/normal/mz/mz_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_1_body.png",(0,0), "images/sprites/normal/mz/mz_1_pioneer.png",(0,0), "images/sprites/normal/mz/mz_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_1_body.png",(0,0), "images/sprites/normal/mz/mz_1_pioneer.png",(0,0), "images/sprites/normal/mz/mz_1_normal.png") )
            image un cry_smile swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_swim.png",(0,0), "images/sprites/normal/un/un_2_cry_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_swim.png",(0,0), "images/sprites/normal/un/un_2_cry_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_swim.png",(0,0), "images/sprites/normal/un/un_2_cry_smile.png") )
            image uv normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/uv/uv_2_body.png",(0,0), "images/sprites/normal/uv/uv_2_pioneer.png",(0,0), "images/sprites/normal/uv/uv_2_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/uv/uv_2_body.png",(0,0), "images/sprites/normal/uv/uv_2_pioneer.png",(0,0), "images/sprites/normal/uv/uv_2_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/uv/uv_2_body.png",(0,0), "images/sprites/normal/uv/uv_2_pioneer.png",(0,0), "images/sprites/normal/uv/uv_2_normal.png") )
            image us angry swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_swim.png",(0,0), "images/sprites/normal/us/us_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_swim.png",(0,0), "images/sprites/normal/us/us_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_swim.png",(0,0), "images/sprites/normal/us/us_2_angry.png") )
            image mt normal swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_swim.png",(0,0), "images/sprites/normal/mt/mt_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_swim.png",(0,0), "images/sprites/normal/mt/mt_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_swim.png",(0,0), "images/sprites/normal/mt/mt_1_normal.png") )
            image us dontlike pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_pioneer.png",(0,0), "images/sprites/normal/us/us_2_dontlike.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_pioneer.png",(0,0), "images/sprites/normal/us/us_2_dontlike.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_pioneer.png",(0,0), "images/sprites/normal/us/us_2_dontlike.png") )
            image un normal sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_sport.png",(0,0), "images/sprites/normal/un/un_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_sport.png",(0,0), "images/sprites/normal/un/un_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_sport.png",(0,0), "images/sprites/normal/un/un_1_normal.png") )
            image un grin sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_sport.png",(0,0), "images/sprites/normal/un/un_3_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_sport.png",(0,0), "images/sprites/normal/un/un_3_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_sport.png",(0,0), "images/sprites/normal/un/un_3_grin.png") )
            image mi laugh pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_pioneer.png",(0,0), "images/sprites/normal/mi/mi_1_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_pioneer.png",(0,0), "images/sprites/normal/mi/mi_1_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_pioneer.png",(0,0), "images/sprites/normal/mi/mi_1_laugh.png") )
            image un shocked sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_sport.png",(0,0), "images/sprites/normal/un/un_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_sport.png",(0,0), "images/sprites/normal/un/un_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_sport.png",(0,0), "images/sprites/normal/un/un_2_shocked.png") )
            image us laugh2 dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_dress.png",(0,0), "images/sprites/normal/us/us_1_laugh2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_dress.png",(0,0), "images/sprites/normal/us/us_1_laugh2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_dress.png",(0,0), "images/sprites/normal/us/us_1_laugh2.png") )
            image el laugh pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/el/el_3_body.png",(0,0), "images/sprites/normal/el/el_3_pioneer.png",(0,0), "images/sprites/normal/el/el_3_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/el/el_3_body.png",(0,0), "images/sprites/normal/el/el_3_pioneer.png",(0,0), "images/sprites/normal/el/el_3_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/el/el_3_body.png",(0,0), "images/sprites/normal/el/el_3_pioneer.png",(0,0), "images/sprites/normal/el/el_3_laugh.png") )
            image sl tender pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_4_body.png",(0,0), "images/sprites/normal/sl/sl_4_pioneer.png",(0,0), "images/sprites/normal/sl/sl_4_tender.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_4_body.png",(0,0), "images/sprites/normal/sl/sl_4_pioneer.png",(0,0), "images/sprites/normal/sl/sl_4_tender.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_4_body.png",(0,0), "images/sprites/normal/sl/sl_4_pioneer.png",(0,0), "images/sprites/normal/sl/sl_4_tender.png") )
            image sl smile pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_1_body.png",(0,0), "images/sprites/normal/sl/sl_1_pioneer.png",(0,0), "images/sprites/normal/sl/sl_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_1_body.png",(0,0), "images/sprites/normal/sl/sl_1_pioneer.png",(0,0), "images/sprites/normal/sl/sl_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_1_body.png",(0,0), "images/sprites/normal/sl/sl_1_pioneer.png",(0,0), "images/sprites/normal/sl/sl_1_smile.png") )
            image us angry pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_pioneer.png",(0,0), "images/sprites/normal/us/us_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_pioneer.png",(0,0), "images/sprites/normal/us/us_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_pioneer.png",(0,0), "images/sprites/normal/us/us_2_angry.png") )
            image sh normal_smile pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_2_body.png",(0,0), "images/sprites/normal/sh/sh_2_normal_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_2_body.png",(0,0), "images/sprites/normal/sh/sh_2_normal_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_2_body.png",(0,0), "images/sprites/normal/sh/sh_2_normal_smile.png") )
            image dv laugh pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_4_body.png",(0,0), "images/sprites/normal/dv/dv_4_pioneer.png",(0,0), "images/sprites/normal/dv/dv_4_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_4_body.png",(0,0), "images/sprites/normal/dv/dv_4_pioneer.png",(0,0), "images/sprites/normal/dv/dv_4_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_4_body.png",(0,0), "images/sprites/normal/dv/dv_4_pioneer.png",(0,0), "images/sprites/normal/dv/dv_4_laugh.png") )
            image us sad dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_dress.png",(0,0), "images/sprites/normal/us/us_1_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_dress.png",(0,0), "images/sprites/normal/us/us_1_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_dress.png",(0,0), "images/sprites/normal/us/us_1_sad.png") )
            image mt rage panama swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_panama.png",(0,0), "images/sprites/normal/mt/mt_2_rage.png",(0,0), "images/sprites/normal/mt/mt_2_swim.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_panama.png",(0,0), "images/sprites/normal/mt/mt_2_rage.png",(0,0), "images/sprites/normal/mt/mt_2_swim.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_panama.png",(0,0), "images/sprites/normal/mt/mt_2_rage.png",(0,0), "images/sprites/normal/mt/mt_2_swim.png") )
            image un angry dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_dress.png",(0,0), "images/sprites/normal/un/un_1_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_dress.png",(0,0), "images/sprites/normal/un/un_1_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_dress.png",(0,0), "images/sprites/normal/un/un_1_angry.png") )
            image un angry pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_pioneer.png",(0,0), "images/sprites/normal/un/un_1_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_pioneer.png",(0,0), "images/sprites/normal/un/un_1_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_pioneer.png",(0,0), "images/sprites/normal/un/un_1_angry.png") )
            image cs normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/cs/cs_1_body.png",(0,0), "images/sprites/normal/cs/cs_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/cs/cs_1_body.png",(0,0), "images/sprites/normal/cs/cs_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/cs/cs_1_body.png",(0,0), "images/sprites/normal/cs/cs_1_normal.png") )
            image us upset pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_pioneer.png",(0,0), "images/sprites/normal/us/us_2_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_pioneer.png",(0,0), "images/sprites/normal/us/us_2_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_pioneer.png",(0,0), "images/sprites/normal/us/us_2_upset.png") )
            image us smile dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_dress.png",(0,0), "images/sprites/normal/us/us_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_dress.png",(0,0), "images/sprites/normal/us/us_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_dress.png",(0,0), "images/sprites/normal/us/us_1_smile.png") )
            image dv shy pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_3_body.png",(0,0), "images/sprites/normal/dv/dv_3_pioneer.png",(0,0), "images/sprites/normal/dv/dv_3_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_3_body.png",(0,0), "images/sprites/normal/dv/dv_3_pioneer.png",(0,0), "images/sprites/normal/dv/dv_3_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_3_body.png",(0,0), "images/sprites/normal/dv/dv_3_pioneer.png",(0,0), "images/sprites/normal/dv/dv_3_shy.png") )
            image un smile3 sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_sport.png",(0,0), "images/sprites/normal/un/un_3_smile3.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_sport.png",(0,0), "images/sprites/normal/un/un_3_smile3.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_sport.png",(0,0), "images/sprites/normal/un/un_3_smile3.png") )
            image un shy sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_sport.png",(0,0), "images/sprites/normal/un/un_1_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_sport.png",(0,0), "images/sprites/normal/un/un_1_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_sport.png",(0,0), "images/sprites/normal/un/un_1_shy.png") )
            image cs smile glasses = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/cs/cs_1_body.png",(0,0), "images/sprites/normal/cs/cs_1_glasses.png",(0,0), "images/sprites/normal/cs/cs_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/cs/cs_1_body.png",(0,0), "images/sprites/normal/cs/cs_1_glasses.png",(0,0), "images/sprites/normal/cs/cs_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/cs/cs_1_body.png",(0,0), "images/sprites/normal/cs/cs_1_glasses.png",(0,0), "images/sprites/normal/cs/cs_1_smile.png") )
            image sl scared sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_4_body.png",(0,0), "images/sprites/normal/sl/sl_4_sport.png",(0,0), "images/sprites/normal/sl/sl_4_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_4_body.png",(0,0), "images/sprites/normal/sl/sl_4_sport.png",(0,0), "images/sprites/normal/sl/sl_4_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_4_body.png",(0,0), "images/sprites/normal/sl/sl_4_sport.png",(0,0), "images/sprites/normal/sl/sl_4_scared.png") )
            image dv shy pioneer2 = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_3_body.png",(0,0), "images/sprites/normal/dv/dv_3_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_3_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_3_body.png",(0,0), "images/sprites/normal/dv/dv_3_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_3_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_3_body.png",(0,0), "images/sprites/normal/dv/dv_3_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_3_shy.png") )
            image us fear swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_swim.png",(0,0), "images/sprites/normal/us/us_2_fear.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_swim.png",(0,0), "images/sprites/normal/us/us_2_fear.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_swim.png",(0,0), "images/sprites/normal/us/us_2_fear.png") )
            image sh smile = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_1_body.png",(0,0), "images/sprites/normal/sh/sh_1_laugh.png",(0,0), "images/sprites/normal/sh/sh_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_1_body.png",(0,0), "images/sprites/normal/sh/sh_1_laugh.png",(0,0), "images/sprites/normal/sh/sh_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_1_body.png",(0,0), "images/sprites/normal/sh/sh_1_laugh.png",(0,0), "images/sprites/normal/sh/sh_1_smile.png") )
            image us fear dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_dress.png",(0,0), "images/sprites/normal/us/us_2_fear.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_dress.png",(0,0), "images/sprites/normal/us/us_2_fear.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_dress.png",(0,0), "images/sprites/normal/us/us_2_fear.png") )
            image mt sad pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_pioneer.png",(0,0), "images/sprites/normal/mt/mt_1_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_pioneer.png",(0,0), "images/sprites/normal/mt/mt_1_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_pioneer.png",(0,0), "images/sprites/normal/mt/mt_1_sad.png") )
            image mt smile dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_dress.png",(0,0), "images/sprites/normal/mt/mt_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_dress.png",(0,0), "images/sprites/normal/mt/mt_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_dress.png",(0,0), "images/sprites/normal/mt/mt_1_smile.png") )
            image un smile2 swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_swim.png",(0,0), "images/sprites/normal/un/un_1_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_swim.png",(0,0), "images/sprites/normal/un/un_1_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_swim.png",(0,0), "images/sprites/normal/un/un_1_smile2.png") )
            image sh normal_smile = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_2_body.png",(0,0), "images/sprites/normal/sh/sh_2_rage.png",(0,0), "images/sprites/normal/sh/sh_2_normal_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_2_body.png",(0,0), "images/sprites/normal/sh/sh_2_rage.png",(0,0), "images/sprites/normal/sh/sh_2_normal_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_2_body.png",(0,0), "images/sprites/normal/sh/sh_2_rage.png",(0,0), "images/sprites/normal/sh/sh_2_normal_smile.png") )
            image sl tender swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_4_body.png",(0,0), "images/sprites/normal/sl/sl_4_swim.png",(0,0), "images/sprites/normal/sl/sl_4_tender.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_4_body.png",(0,0), "images/sprites/normal/sl/sl_4_swim.png",(0,0), "images/sprites/normal/sl/sl_4_tender.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_4_body.png",(0,0), "images/sprites/normal/sl/sl_4_swim.png",(0,0), "images/sprites/normal/sl/sl_4_tender.png") )
            image mt rage pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_pioneer.png",(0,0), "images/sprites/normal/mt/mt_2_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_pioneer.png",(0,0), "images/sprites/normal/mt/mt_2_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_pioneer.png",(0,0), "images/sprites/normal/mt/mt_2_rage.png") )
            image mt angry panama pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_panama.png",(0,0), "images/sprites/normal/mt/mt_2_angry.png",(0,0), "images/sprites/normal/mt/mt_2_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_panama.png",(0,0), "images/sprites/normal/mt/mt_2_angry.png",(0,0), "images/sprites/normal/mt/mt_2_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_panama.png",(0,0), "images/sprites/normal/mt/mt_2_angry.png",(0,0), "images/sprites/normal/mt/mt_2_pioneer.png") )
            image un smile2 pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_pioneer.png",(0,0), "images/sprites/normal/un/un_1_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_pioneer.png",(0,0), "images/sprites/normal/un/un_1_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_pioneer.png",(0,0), "images/sprites/normal/un/un_1_smile2.png") )
            image el normal pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/el/el_1_body.png",(0,0), "images/sprites/normal/el/el_1_pioneer.png",(0,0), "images/sprites/normal/el/el_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/el/el_1_body.png",(0,0), "images/sprites/normal/el/el_1_pioneer.png",(0,0), "images/sprites/normal/el/el_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/el/el_1_body.png",(0,0), "images/sprites/normal/el/el_1_pioneer.png",(0,0), "images/sprites/normal/el/el_1_normal.png") )
            image mt smile panama dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_panama.png",(0,0), "images/sprites/normal/mt/mt_1_smile.png",(0,0), "images/sprites/normal/mt/mt_1_dress.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_panama.png",(0,0), "images/sprites/normal/mt/mt_1_smile.png",(0,0), "images/sprites/normal/mt/mt_1_dress.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_panama.png",(0,0), "images/sprites/normal/mt/mt_1_smile.png",(0,0), "images/sprites/normal/mt/mt_1_dress.png") )
            image sl laugh sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_sport.png",(0,0), "images/sprites/normal/sl/sl_2_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_sport.png",(0,0), "images/sprites/normal/sl/sl_2_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_sport.png",(0,0), "images/sprites/normal/sl/sl_2_laugh.png") )
            image us upset sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_sport.png",(0,0), "images/sprites/normal/us/us_2_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_sport.png",(0,0), "images/sprites/normal/us/us_2_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_sport.png",(0,0), "images/sprites/normal/us/us_2_upset.png") )
            image mt normal pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_pioneer.png",(0,0), "images/sprites/normal/mt/mt_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_pioneer.png",(0,0), "images/sprites/normal/mt/mt_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_pioneer.png",(0,0), "images/sprites/normal/mt/mt_1_normal.png") )
            image us cry2 swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_swim.png",(0,0), "images/sprites/normal/us/us_3_cry2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_swim.png",(0,0), "images/sprites/normal/us/us_3_cry2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_swim.png",(0,0), "images/sprites/normal/us/us_3_cry2.png") )
            image mt surprise swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_swim.png",(0,0), "images/sprites/normal/mt/mt_1_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_swim.png",(0,0), "images/sprites/normal/mt/mt_1_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_swim.png",(0,0), "images/sprites/normal/mt/mt_1_surprise.png") )
            image sl smile dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_1_body.png",(0,0), "images/sprites/normal/sl/sl_1_dress.png",(0,0), "images/sprites/normal/sl/sl_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_1_body.png",(0,0), "images/sprites/normal/sl/sl_1_dress.png",(0,0), "images/sprites/normal/sl/sl_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_1_body.png",(0,0), "images/sprites/normal/sl/sl_1_dress.png",(0,0), "images/sprites/normal/sl/sl_1_smile.png") )
            image us upset swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_swim.png",(0,0), "images/sprites/normal/us/us_2_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_swim.png",(0,0), "images/sprites/normal/us/us_2_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_swim.png",(0,0), "images/sprites/normal/us/us_2_upset.png") )
            image un smile sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_sport.png",(0,0), "images/sprites/normal/un/un_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_sport.png",(0,0), "images/sprites/normal/un/un_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_sport.png",(0,0), "images/sprites/normal/un/un_1_smile.png") )
            image un smile pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_pioneer.png",(0,0), "images/sprites/normal/un/un_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_pioneer.png",(0,0), "images/sprites/normal/un/un_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_pioneer.png",(0,0), "images/sprites/normal/un/un_1_smile.png") )
            image us upset dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_dress.png",(0,0), "images/sprites/normal/us/us_2_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_dress.png",(0,0), "images/sprites/normal/us/us_2_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_dress.png",(0,0), "images/sprites/normal/us/us_2_upset.png") )
            image us laugh pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_pioneer.png",(0,0), "images/sprites/normal/us/us_1_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_pioneer.png",(0,0), "images/sprites/normal/us/us_1_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_pioneer.png",(0,0), "images/sprites/normal/us/us_1_laugh.png") )
            image un rage sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_sport.png",(0,0), "images/sprites/normal/un/un_3_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_sport.png",(0,0), "images/sprites/normal/un/un_3_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_sport.png",(0,0), "images/sprites/normal/un/un_3_rage.png") )
            image sl scared pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_4_body.png",(0,0), "images/sprites/normal/sl/sl_4_pioneer.png",(0,0), "images/sprites/normal/sl/sl_4_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_4_body.png",(0,0), "images/sprites/normal/sl/sl_4_pioneer.png",(0,0), "images/sprites/normal/sl/sl_4_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_4_body.png",(0,0), "images/sprites/normal/sl/sl_4_pioneer.png",(0,0), "images/sprites/normal/sl/sl_4_scared.png") )
            image us shy2 sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_sport.png",(0,0), "images/sprites/normal/us/us_3_shy2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_sport.png",(0,0), "images/sprites/normal/us/us_3_shy2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_sport.png",(0,0), "images/sprites/normal/us/us_3_shy2.png") )
            image sl surprise sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_3_body.png",(0,0), "images/sprites/normal/sl/sl_3_sport.png",(0,0), "images/sprites/normal/sl/sl_3_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_3_body.png",(0,0), "images/sprites/normal/sl/sl_3_sport.png",(0,0), "images/sprites/normal/sl/sl_3_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_3_body.png",(0,0), "images/sprites/normal/sl/sl_3_sport.png",(0,0), "images/sprites/normal/sl/sl_3_surprise.png") )
            image us surp1 swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_swim.png",(0,0), "images/sprites/normal/us/us_3_surp1.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_swim.png",(0,0), "images/sprites/normal/us/us_3_surp1.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_swim.png",(0,0), "images/sprites/normal/us/us_3_surp1.png") )
            image mt angry dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_dress.png",(0,0), "images/sprites/normal/mt/mt_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_dress.png",(0,0), "images/sprites/normal/mt/mt_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_dress.png",(0,0), "images/sprites/normal/mt/mt_2_angry.png") )
            image uv upset = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/uv/uv_4_body.png",(0,0), "images/sprites/normal/uv/uv_4_pioneer.png",(0,0), "images/sprites/normal/uv/uv_4_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/uv/uv_4_body.png",(0,0), "images/sprites/normal/uv/uv_4_pioneer.png",(0,0), "images/sprites/normal/uv/uv_4_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/uv/uv_4_body.png",(0,0), "images/sprites/normal/uv/uv_4_pioneer.png",(0,0), "images/sprites/normal/uv/uv_4_upset.png") )
            image sh serious = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_3_body.png",(0,0), "images/sprites/normal/sh/sh_3_normal.png",(0,0), "images/sprites/normal/sh/sh_3_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_3_body.png",(0,0), "images/sprites/normal/sh/sh_3_normal.png",(0,0), "images/sprites/normal/sh/sh_3_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_3_body.png",(0,0), "images/sprites/normal/sh/sh_3_normal.png",(0,0), "images/sprites/normal/sh/sh_3_serious.png") )
            image uv guilty = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/uv/uv_4_body.png",(0,0), "images/sprites/normal/uv/uv_4_pioneer.png",(0,0), "images/sprites/normal/uv/uv_4_guilty.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/uv/uv_4_body.png",(0,0), "images/sprites/normal/uv/uv_4_pioneer.png",(0,0), "images/sprites/normal/uv/uv_4_guilty.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/uv/uv_4_body.png",(0,0), "images/sprites/normal/uv/uv_4_pioneer.png",(0,0), "images/sprites/normal/uv/uv_4_guilty.png") )
            image us calml swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_swim.png",(0,0), "images/sprites/normal/us/us_2_calml.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_swim.png",(0,0), "images/sprites/normal/us/us_2_calml.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_swim.png",(0,0), "images/sprites/normal/us/us_2_calml.png") )
            image us shy2 swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_swim.png",(0,0), "images/sprites/normal/us/us_3_shy2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_swim.png",(0,0), "images/sprites/normal/us/us_3_shy2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_swim.png",(0,0), "images/sprites/normal/us/us_3_shy2.png") )
            image us dontlike dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_dress.png",(0,0), "images/sprites/normal/us/us_2_dontlike.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_dress.png",(0,0), "images/sprites/normal/us/us_2_dontlike.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_dress.png",(0,0), "images/sprites/normal/us/us_2_dontlike.png") )
            image mi smile pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_2_body.png",(0,0), "images/sprites/normal/mi/mi_2_pioneer.png",(0,0), "images/sprites/normal/mi/mi_2_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_2_body.png",(0,0), "images/sprites/normal/mi/mi_2_pioneer.png",(0,0), "images/sprites/normal/mi/mi_2_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_2_body.png",(0,0), "images/sprites/normal/mi/mi_2_pioneer.png",(0,0), "images/sprites/normal/mi/mi_2_smile.png") )
            image us dontlike sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_sport.png",(0,0), "images/sprites/normal/us/us_2_dontlike.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_sport.png",(0,0), "images/sprites/normal/us/us_2_dontlike.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_sport.png",(0,0), "images/sprites/normal/us/us_2_dontlike.png") )
            image un normal pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_pioneer.png",(0,0), "images/sprites/normal/un/un_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_pioneer.png",(0,0), "images/sprites/normal/un/un_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_pioneer.png",(0,0), "images/sprites/normal/un/un_1_normal.png") )
            image un normal pioneer red = im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_pioneer.png",(0,0), "images/sprites/normal/un/un_1_normal.png"), im.matrix.tint(1, 0.1, 0.1) )
            image us cry pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_pioneer.png",(0,0), "images/sprites/normal/us/us_3_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_pioneer.png",(0,0), "images/sprites/normal/us/us_3_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_pioneer.png",(0,0), "images/sprites/normal/us/us_3_cry.png") )
            image un shy swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_swim.png",(0,0), "images/sprites/normal/un/un_1_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_swim.png",(0,0), "images/sprites/normal/un/un_1_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_swim.png",(0,0), "images/sprites/normal/un/un_1_shy.png") )
            image sl smile2 pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_pioneer.png",(0,0), "images/sprites/normal/sl/sl_2_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_pioneer.png",(0,0), "images/sprites/normal/sl/sl_2_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_pioneer.png",(0,0), "images/sprites/normal/sl/sl_2_smile2.png") )
            image mi cry_smile pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_2_body.png",(0,0), "images/sprites/normal/mi/mi_2_pioneer.png",(0,0), "images/sprites/normal/mi/mi_2_cry_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_2_body.png",(0,0), "images/sprites/normal/mi/mi_2_pioneer.png",(0,0), "images/sprites/normal/mi/mi_2_cry_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_2_body.png",(0,0), "images/sprites/normal/mi/mi_2_pioneer.png",(0,0), "images/sprites/normal/mi/mi_2_cry_smile.png") )
            image un normal swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_swim.png",(0,0), "images/sprites/normal/un/un_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_swim.png",(0,0), "images/sprites/normal/un/un_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_swim.png",(0,0), "images/sprites/normal/un/un_1_normal.png") )
            image dv normal swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_4_body.png",(0,0), "images/sprites/normal/dv/dv_4_swim.png",(0,0), "images/sprites/normal/dv/dv_4_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_4_body.png",(0,0), "images/sprites/normal/dv/dv_4_swim.png",(0,0), "images/sprites/normal/dv/dv_4_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_4_body.png",(0,0), "images/sprites/normal/dv/dv_4_swim.png",(0,0), "images/sprites/normal/dv/dv_4_normal.png") )
            image un scared pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_pioneer.png",(0,0), "images/sprites/normal/un/un_2_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_pioneer.png",(0,0), "images/sprites/normal/un/un_2_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_pioneer.png",(0,0), "images/sprites/normal/un/un_2_scared.png") )
            image dv smile pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_4_body.png",(0,0), "images/sprites/normal/dv/dv_4_pioneer.png",(0,0), "images/sprites/normal/dv/dv_4_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_4_body.png",(0,0), "images/sprites/normal/dv/dv_4_pioneer.png",(0,0), "images/sprites/normal/dv/dv_4_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_4_body.png",(0,0), "images/sprites/normal/dv/dv_4_pioneer.png",(0,0), "images/sprites/normal/dv/dv_4_smile.png") )
            image us shy swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_swim.png",(0,0), "images/sprites/normal/us/us_3_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_swim.png",(0,0), "images/sprites/normal/us/us_3_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_swim.png",(0,0), "images/sprites/normal/us/us_3_shy.png") )
            image cs shy glasses = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/cs/cs_1_body.png",(0,0), "images/sprites/normal/cs/cs_1_glasses.png",(0,0), "images/sprites/normal/cs/cs_1_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/cs/cs_1_body.png",(0,0), "images/sprites/normal/cs/cs_1_glasses.png",(0,0), "images/sprites/normal/cs/cs_1_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/cs/cs_1_body.png",(0,0), "images/sprites/normal/cs/cs_1_glasses.png",(0,0), "images/sprites/normal/cs/cs_1_shy.png") )
            image cs smile stethoscope = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/cs/cs_1_body.png",(0,0), "images/sprites/normal/cs/cs_1_stethoscope.png",(0,0), "images/sprites/normal/cs/cs_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/cs/cs_1_body.png",(0,0), "images/sprites/normal/cs/cs_1_stethoscope.png",(0,0), "images/sprites/normal/cs/cs_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/cs/cs_1_body.png",(0,0), "images/sprites/normal/cs/cs_1_stethoscope.png",(0,0), "images/sprites/normal/cs/cs_1_smile.png") )
            image us grin swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_swim.png",(0,0), "images/sprites/normal/us/us_1_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_swim.png",(0,0), "images/sprites/normal/us/us_1_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_swim.png",(0,0), "images/sprites/normal/us/us_1_grin.png") )
            image sl normal dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_1_body.png",(0,0), "images/sprites/normal/sl/sl_1_dress.png",(0,0), "images/sprites/normal/sl/sl_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_1_body.png",(0,0), "images/sprites/normal/sl/sl_1_dress.png",(0,0), "images/sprites/normal/sl/sl_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_1_body.png",(0,0), "images/sprites/normal/sl/sl_1_dress.png",(0,0), "images/sprites/normal/sl/sl_1_normal.png") )
            image mi cry pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_pioneer.png",(0,0), "images/sprites/normal/mi/mi_1_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_pioneer.png",(0,0), "images/sprites/normal/mi/mi_1_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_pioneer.png",(0,0), "images/sprites/normal/mi/mi_1_cry.png") )
            image mt grin pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_3_body.png",(0,0), "images/sprites/normal/mt/mt_3_pioneer.png",(0,0), "images/sprites/normal/mt/mt_3_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_3_body.png",(0,0), "images/sprites/normal/mt/mt_3_pioneer.png",(0,0), "images/sprites/normal/mt/mt_3_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_3_body.png",(0,0), "images/sprites/normal/mt/mt_3_pioneer.png",(0,0), "images/sprites/normal/mt/mt_3_grin.png") )
            image mt surprise pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_pioneer.png",(0,0), "images/sprites/normal/mt/mt_1_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_pioneer.png",(0,0), "images/sprites/normal/mt/mt_1_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_pioneer.png",(0,0), "images/sprites/normal/mt/mt_1_surprise.png") )
            image dv smile swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_4_body.png",(0,0), "images/sprites/normal/dv/dv_4_swim.png",(0,0), "images/sprites/normal/dv/dv_4_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_4_body.png",(0,0), "images/sprites/normal/dv/dv_4_swim.png",(0,0), "images/sprites/normal/dv/dv_4_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_4_body.png",(0,0), "images/sprites/normal/dv/dv_4_swim.png",(0,0), "images/sprites/normal/dv/dv_4_smile.png") )
            image un laugh dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_dress.png",(0,0), "images/sprites/normal/un/un_3_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_dress.png",(0,0), "images/sprites/normal/un/un_3_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_dress.png",(0,0), "images/sprites/normal/un/un_3_laugh.png") )
            image sl serious pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_1_body.png",(0,0), "images/sprites/normal/sl/sl_1_pioneer.png",(0,0), "images/sprites/normal/sl/sl_1_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_1_body.png",(0,0), "images/sprites/normal/sl/sl_1_pioneer.png",(0,0), "images/sprites/normal/sl/sl_1_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_1_body.png",(0,0), "images/sprites/normal/sl/sl_1_pioneer.png",(0,0), "images/sprites/normal/sl/sl_1_serious.png") )
            image us smile sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_sport.png",(0,0), "images/sprites/normal/us/us_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_sport.png",(0,0), "images/sprites/normal/us/us_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_sport.png",(0,0), "images/sprites/normal/us/us_1_smile.png") )
            image sh serious pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_3_body.png",(0,0), "images/sprites/normal/sh/sh_3_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_3_body.png",(0,0), "images/sprites/normal/sh/sh_3_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_3_body.png",(0,0), "images/sprites/normal/sh/sh_3_serious.png") )
            image un serious sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_sport.png",(0,0), "images/sprites/normal/un/un_3_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_sport.png",(0,0), "images/sprites/normal/un/un_3_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_sport.png",(0,0), "images/sprites/normal/un/un_3_serious.png") )
            image mt normal panama pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_panama.png",(0,0), "images/sprites/normal/mt/mt_1_normal.png",(0,0), "images/sprites/normal/mt/mt_1_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_panama.png",(0,0), "images/sprites/normal/mt/mt_1_normal.png",(0,0), "images/sprites/normal/mt/mt_1_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_panama.png",(0,0), "images/sprites/normal/mt/mt_1_normal.png",(0,0), "images/sprites/normal/mt/mt_1_pioneer.png") )
            image mt sad panama dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_panama.png",(0,0), "images/sprites/normal/mt/mt_1_sad.png",(0,0), "images/sprites/normal/mt/mt_1_dress.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_panama.png",(0,0), "images/sprites/normal/mt/mt_1_sad.png",(0,0), "images/sprites/normal/mt/mt_1_dress.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_panama.png",(0,0), "images/sprites/normal/mt/mt_1_sad.png",(0,0), "images/sprites/normal/mt/mt_1_dress.png") )
            image sl angry dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_3_body.png",(0,0), "images/sprites/normal/sl/sl_3_dress.png",(0,0), "images/sprites/normal/sl/sl_3_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_3_body.png",(0,0), "images/sprites/normal/sl/sl_3_dress.png",(0,0), "images/sprites/normal/sl/sl_3_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_3_body.png",(0,0), "images/sprites/normal/sl/sl_3_dress.png",(0,0), "images/sprites/normal/sl/sl_3_angry.png") )
            image sl surprise dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_3_body.png",(0,0), "images/sprites/normal/sl/sl_3_dress.png",(0,0), "images/sprites/normal/sl/sl_3_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_3_body.png",(0,0), "images/sprites/normal/sl/sl_3_dress.png",(0,0), "images/sprites/normal/sl/sl_3_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_3_body.png",(0,0), "images/sprites/normal/sl/sl_3_dress.png",(0,0), "images/sprites/normal/sl/sl_3_surprise.png") )
            image dv shocked pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_pioneer.png",(0,0), "images/sprites/normal/dv/dv_1_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_pioneer.png",(0,0), "images/sprites/normal/dv/dv_1_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_pioneer.png",(0,0), "images/sprites/normal/dv/dv_1_shocked.png") )
            image us surp2 swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_swim.png",(0,0), "images/sprites/normal/us/us_3_surp2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_swim.png",(0,0), "images/sprites/normal/us/us_3_surp2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_swim.png",(0,0), "images/sprites/normal/us/us_3_surp2.png") )
            image sl tender sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_4_body.png",(0,0), "images/sprites/normal/sl/sl_4_sport.png",(0,0), "images/sprites/normal/sl/sl_4_tender.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_4_body.png",(0,0), "images/sprites/normal/sl/sl_4_sport.png",(0,0), "images/sprites/normal/sl/sl_4_tender.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_4_body.png",(0,0), "images/sprites/normal/sl/sl_4_sport.png",(0,0), "images/sprites/normal/sl/sl_4_tender.png") )
            image sl surprise pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_3_body.png",(0,0), "images/sprites/normal/sl/sl_3_pioneer.png",(0,0), "images/sprites/normal/sl/sl_3_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_3_body.png",(0,0), "images/sprites/normal/sl/sl_3_pioneer.png",(0,0), "images/sprites/normal/sl/sl_3_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_3_body.png",(0,0), "images/sprites/normal/sl/sl_3_pioneer.png",(0,0), "images/sprites/normal/sl/sl_3_surprise.png") )
            image us grin sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_sport.png",(0,0), "images/sprites/normal/us/us_1_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_sport.png",(0,0), "images/sprites/normal/us/us_1_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_sport.png",(0,0), "images/sprites/normal/us/us_1_grin.png") )
            image us laugh2 swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_swim.png",(0,0), "images/sprites/normal/us/us_1_laugh2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_swim.png",(0,0), "images/sprites/normal/us/us_1_laugh2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_swim.png",(0,0), "images/sprites/normal/us/us_1_laugh2.png") )
            image dv guilty pioneer2 = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_3_body.png",(0,0), "images/sprites/normal/dv/dv_3_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_3_guilty.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_3_body.png",(0,0), "images/sprites/normal/dv/dv_3_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_3_guilty.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_3_body.png",(0,0), "images/sprites/normal/dv/dv_3_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_3_guilty.png") )
            image sl smile2 swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_swim.png",(0,0), "images/sprites/normal/sl/sl_2_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_swim.png",(0,0), "images/sprites/normal/sl/sl_2_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_swim.png",(0,0), "images/sprites/normal/sl/sl_2_smile2.png") )
            image mi normal swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_3_body.png",(0,0), "images/sprites/normal/mi/mi_3_swim.png",(0,0), "images/sprites/normal/mi/mi_3_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_3_body.png",(0,0), "images/sprites/normal/mi/mi_3_swim.png",(0,0), "images/sprites/normal/mi/mi_3_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_3_body.png",(0,0), "images/sprites/normal/mi/mi_3_swim.png",(0,0), "images/sprites/normal/mi/mi_3_normal.png") )
            image sl normal sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_1_body.png",(0,0), "images/sprites/normal/sl/sl_1_sport.png",(0,0), "images/sprites/normal/sl/sl_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_1_body.png",(0,0), "images/sprites/normal/sl/sl_1_sport.png",(0,0), "images/sprites/normal/sl/sl_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_1_body.png",(0,0), "images/sprites/normal/sl/sl_1_sport.png",(0,0), "images/sprites/normal/sl/sl_1_normal.png") )
            image mi sad pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_2_body.png",(0,0), "images/sprites/normal/mi/mi_2_pioneer.png",(0,0), "images/sprites/normal/mi/mi_2_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_2_body.png",(0,0), "images/sprites/normal/mi/mi_2_pioneer.png",(0,0), "images/sprites/normal/mi/mi_2_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_2_body.png",(0,0), "images/sprites/normal/mi/mi_2_pioneer.png",(0,0), "images/sprites/normal/mi/mi_2_sad.png") )
            image un smile3 pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_pioneer.png",(0,0), "images/sprites/normal/un/un_3_smile3.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_pioneer.png",(0,0), "images/sprites/normal/un/un_3_smile3.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_pioneer.png",(0,0), "images/sprites/normal/un/un_3_smile3.png") )
            image sl smile2 dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_dress.png",(0,0), "images/sprites/normal/sl/sl_2_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_dress.png",(0,0), "images/sprites/normal/sl/sl_2_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_dress.png",(0,0), "images/sprites/normal/sl/sl_2_smile2.png") )
            image us smile swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_swim.png",(0,0), "images/sprites/normal/us/us_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_swim.png",(0,0), "images/sprites/normal/us/us_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_swim.png",(0,0), "images/sprites/normal/us/us_1_smile.png") )
            image mt rage panama dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_panama.png",(0,0), "images/sprites/normal/mt/mt_2_rage.png",(0,0), "images/sprites/normal/mt/mt_2_dress.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_panama.png",(0,0), "images/sprites/normal/mt/mt_2_rage.png",(0,0), "images/sprites/normal/mt/mt_2_dress.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_panama.png",(0,0), "images/sprites/normal/mt/mt_2_rage.png",(0,0), "images/sprites/normal/mt/mt_2_dress.png") )
            image dv surprise pioneer2 = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_1_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_1_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_1_surprise.png") )
            image us cry2 sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_sport.png",(0,0), "images/sprites/normal/us/us_3_cry2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_sport.png",(0,0), "images/sprites/normal/us/us_3_cry2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_sport.png",(0,0), "images/sprites/normal/us/us_3_cry2.png") )
            image un normal dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_dress.png",(0,0), "images/sprites/normal/un/un_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_dress.png",(0,0), "images/sprites/normal/un/un_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_dress.png",(0,0), "images/sprites/normal/un/un_1_normal.png") )
            image mi smile swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_2_body.png",(0,0), "images/sprites/normal/mi/mi_2_swim.png",(0,0), "images/sprites/normal/mi/mi_2_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_2_body.png",(0,0), "images/sprites/normal/mi/mi_2_swim.png",(0,0), "images/sprites/normal/mi/mi_2_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_2_body.png",(0,0), "images/sprites/normal/mi/mi_2_swim.png",(0,0), "images/sprites/normal/mi/mi_2_smile.png") )
            image cs normal glasses = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/cs/cs_1_body.png",(0,0), "images/sprites/normal/cs/cs_1_glasses.png",(0,0), "images/sprites/normal/cs/cs_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/cs/cs_1_body.png",(0,0), "images/sprites/normal/cs/cs_1_glasses.png",(0,0), "images/sprites/normal/cs/cs_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/cs/cs_1_body.png",(0,0), "images/sprites/normal/cs/cs_1_glasses.png",(0,0), "images/sprites/normal/cs/cs_1_normal.png") )
            image uv rage = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/uv/uv_1_body.png",(0,0), "images/sprites/normal/uv/uv_1_pioneer.png",(0,0), "images/sprites/normal/uv/uv_1_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/uv/uv_1_body.png",(0,0), "images/sprites/normal/uv/uv_1_pioneer.png",(0,0), "images/sprites/normal/uv/uv_1_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/uv/uv_1_body.png",(0,0), "images/sprites/normal/uv/uv_1_pioneer.png",(0,0), "images/sprites/normal/uv/uv_1_rage.png") )
            image sl sad dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_3_body.png",(0,0), "images/sprites/normal/sl/sl_3_dress.png",(0,0), "images/sprites/normal/sl/sl_3_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_3_body.png",(0,0), "images/sprites/normal/sl/sl_3_dress.png",(0,0), "images/sprites/normal/sl/sl_3_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_3_body.png",(0,0), "images/sprites/normal/sl/sl_3_dress.png",(0,0), "images/sprites/normal/sl/sl_3_sad.png") )
            image mt rage swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_swim.png",(0,0), "images/sprites/normal/mt/mt_2_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_swim.png",(0,0), "images/sprites/normal/mt/mt_2_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_swim.png",(0,0), "images/sprites/normal/mt/mt_2_rage.png") )
            image dv rage pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_5_body.png",(0,0), "images/sprites/normal/dv/dv_5_pioneer.png",(0,0), "images/sprites/normal/dv/dv_5_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_5_body.png",(0,0), "images/sprites/normal/dv/dv_5_pioneer.png",(0,0), "images/sprites/normal/dv/dv_5_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_5_body.png",(0,0), "images/sprites/normal/dv/dv_5_pioneer.png",(0,0), "images/sprites/normal/dv/dv_5_rage.png") )
            image el surprise pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/el/el_2_body.png",(0,0), "images/sprites/normal/el/el_2_pioneer.png",(0,0), "images/sprites/normal/el/el_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/el/el_2_body.png",(0,0), "images/sprites/normal/el/el_2_pioneer.png",(0,0), "images/sprites/normal/el/el_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/el/el_2_body.png",(0,0), "images/sprites/normal/el/el_2_pioneer.png",(0,0), "images/sprites/normal/el/el_2_surprise.png") )
            image un cry pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_pioneer.png",(0,0), "images/sprites/normal/un/un_2_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_pioneer.png",(0,0), "images/sprites/normal/un/un_2_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_pioneer.png",(0,0), "images/sprites/normal/un/un_2_cry.png") )
            image mi dontlike pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_pioneer.png",(0,0), "images/sprites/normal/mi/mi_1_dontlike.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_pioneer.png",(0,0), "images/sprites/normal/mi/mi_1_dontlike.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_pioneer.png",(0,0), "images/sprites/normal/mi/mi_1_dontlike.png") )
            image sl shy swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_swim.png",(0,0), "images/sprites/normal/sl/sl_2_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_swim.png",(0,0), "images/sprites/normal/sl/sl_2_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_swim.png",(0,0), "images/sprites/normal/sl/sl_2_shy.png") )
            image el serious pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/el/el_3_body.png",(0,0), "images/sprites/normal/el/el_3_pioneer.png",(0,0), "images/sprites/normal/el/el_3_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/el/el_3_body.png",(0,0), "images/sprites/normal/el/el_3_pioneer.png",(0,0), "images/sprites/normal/el/el_3_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/el/el_3_body.png",(0,0), "images/sprites/normal/el/el_3_pioneer.png",(0,0), "images/sprites/normal/el/el_3_serious.png") )
            image un scared swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_swim.png",(0,0), "images/sprites/normal/un/un_2_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_swim.png",(0,0), "images/sprites/normal/un/un_2_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_swim.png",(0,0), "images/sprites/normal/un/un_2_scared.png") )
            image el scared pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/el/el_2_body.png",(0,0), "images/sprites/normal/el/el_2_pioneer.png",(0,0), "images/sprites/normal/el/el_2_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/el/el_2_body.png",(0,0), "images/sprites/normal/el/el_2_pioneer.png",(0,0), "images/sprites/normal/el/el_2_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/el/el_2_body.png",(0,0), "images/sprites/normal/el/el_2_pioneer.png",(0,0), "images/sprites/normal/el/el_2_scared.png") )
            image mi cry swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_swim.png",(0,0), "images/sprites/normal/mi/mi_1_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_swim.png",(0,0), "images/sprites/normal/mi/mi_1_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_swim.png",(0,0), "images/sprites/normal/mi/mi_1_cry.png") )
            image mz smile pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_3_body.png",(0,0), "images/sprites/normal/mz/mz_3_pioneer.png",(0,0), "images/sprites/normal/mz/mz_3_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_3_body.png",(0,0), "images/sprites/normal/mz/mz_3_pioneer.png",(0,0), "images/sprites/normal/mz/mz_3_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_3_body.png",(0,0), "images/sprites/normal/mz/mz_3_pioneer.png",(0,0), "images/sprites/normal/mz/mz_3_smile.png") )
            image us laugh sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_sport.png",(0,0), "images/sprites/normal/us/us_1_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_sport.png",(0,0), "images/sprites/normal/us/us_1_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_sport.png",(0,0), "images/sprites/normal/us/us_1_laugh.png") )
            image mt surprise dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_dress.png",(0,0), "images/sprites/normal/mt/mt_1_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_dress.png",(0,0), "images/sprites/normal/mt/mt_1_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_dress.png",(0,0), "images/sprites/normal/mt/mt_1_surprise.png") )
            image mt sad panama swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_panama.png",(0,0), "images/sprites/normal/mt/mt_1_sad.png",(0,0), "images/sprites/normal/mt/mt_1_swim.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_panama.png",(0,0), "images/sprites/normal/mt/mt_1_sad.png",(0,0), "images/sprites/normal/mt/mt_1_swim.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_panama.png",(0,0), "images/sprites/normal/mt/mt_1_sad.png",(0,0), "images/sprites/normal/mt/mt_1_swim.png") )
            image sh upset = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_1_body.png",(0,0), "images/sprites/normal/sh/sh_1_laugh.png",(0,0), "images/sprites/normal/sh/sh_1_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_1_body.png",(0,0), "images/sprites/normal/sh/sh_1_laugh.png",(0,0), "images/sprites/normal/sh/sh_1_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_1_body.png",(0,0), "images/sprites/normal/sh/sh_1_laugh.png",(0,0), "images/sprites/normal/sh/sh_1_upset.png") )
            image un evil_smile sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_sport.png",(0,0), "images/sprites/normal/un/un_1_evil_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_sport.png",(0,0), "images/sprites/normal/un/un_1_evil_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_sport.png",(0,0), "images/sprites/normal/un/un_1_evil_smile.png") )
            image uv surprise = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/uv/uv_4_body.png",(0,0), "images/sprites/normal/uv/uv_4_pioneer.png",(0,0), "images/sprites/normal/uv/uv_4_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/uv/uv_4_body.png",(0,0), "images/sprites/normal/uv/uv_4_pioneer.png",(0,0), "images/sprites/normal/uv/uv_4_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/uv/uv_4_body.png",(0,0), "images/sprites/normal/uv/uv_4_pioneer.png",(0,0), "images/sprites/normal/uv/uv_4_surprise.png") )
            image el grin pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/el/el_1_body.png",(0,0), "images/sprites/normal/el/el_1_pioneer.png",(0,0), "images/sprites/normal/el/el_1_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/el/el_1_body.png",(0,0), "images/sprites/normal/el/el_1_pioneer.png",(0,0), "images/sprites/normal/el/el_1_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/el/el_1_body.png",(0,0), "images/sprites/normal/el/el_1_pioneer.png",(0,0), "images/sprites/normal/el/el_1_grin.png") )
            image mt smile swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_swim.png",(0,0), "images/sprites/normal/mt/mt_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_swim.png",(0,0), "images/sprites/normal/mt/mt_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_swim.png",(0,0), "images/sprites/normal/mt/mt_1_smile.png") )
            image us shy sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_sport.png",(0,0), "images/sprites/normal/us/us_3_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_sport.png",(0,0), "images/sprites/normal/us/us_3_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_sport.png",(0,0), "images/sprites/normal/us/us_3_shy.png") )
            image us fear sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_sport.png",(0,0), "images/sprites/normal/us/us_2_fear.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_sport.png",(0,0), "images/sprites/normal/us/us_2_fear.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_sport.png",(0,0), "images/sprites/normal/us/us_2_fear.png") )
            image un evil_smile pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_pioneer.png",(0,0), "images/sprites/normal/un/un_1_evil_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_pioneer.png",(0,0), "images/sprites/normal/un/un_1_evil_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_pioneer.png",(0,0), "images/sprites/normal/un/un_1_evil_smile.png") )
            image us laugh2 pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_pioneer.png",(0,0), "images/sprites/normal/us/us_1_laugh2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_pioneer.png",(0,0), "images/sprites/normal/us/us_1_laugh2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_pioneer.png",(0,0), "images/sprites/normal/us/us_1_laugh2.png") )
            image sl shy pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_pioneer.png",(0,0), "images/sprites/normal/sl/sl_2_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_pioneer.png",(0,0), "images/sprites/normal/sl/sl_2_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_pioneer.png",(0,0), "images/sprites/normal/sl/sl_2_shy.png") )
            image us surp3 pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_pioneer.png",(0,0), "images/sprites/normal/us/us_3_surp3.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_pioneer.png",(0,0), "images/sprites/normal/us/us_3_surp3.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_pioneer.png",(0,0), "images/sprites/normal/us/us_3_surp3.png") )
            image mi laugh swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_swim.png",(0,0), "images/sprites/normal/mi/mi_1_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_swim.png",(0,0), "images/sprites/normal/mi/mi_1_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_swim.png",(0,0), "images/sprites/normal/mi/mi_1_laugh.png") )
            image un smile3 dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_dress.png",(0,0), "images/sprites/normal/un/un_3_smile3.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_dress.png",(0,0), "images/sprites/normal/un/un_3_smile3.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_dress.png",(0,0), "images/sprites/normal/un/un_3_smile3.png") )
            image us surp3 swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_swim.png",(0,0), "images/sprites/normal/us/us_3_surp3.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_swim.png",(0,0), "images/sprites/normal/us/us_3_surp3.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_swim.png",(0,0), "images/sprites/normal/us/us_3_surp3.png") )
            image un grin pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_pioneer.png",(0,0), "images/sprites/normal/un/un_3_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_pioneer.png",(0,0), "images/sprites/normal/un/un_3_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_pioneer.png",(0,0), "images/sprites/normal/un/un_3_grin.png") )
            image mt laugh panama pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_3_body.png",(0,0), "images/sprites/normal/mt/mt_3_panama.png",(0,0), "images/sprites/normal/mt/mt_3_laugh.png",(0,0), "images/sprites/normal/mt/mt_3_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_3_body.png",(0,0), "images/sprites/normal/mt/mt_3_panama.png",(0,0), "images/sprites/normal/mt/mt_3_laugh.png",(0,0), "images/sprites/normal/mt/mt_3_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_3_body.png",(0,0), "images/sprites/normal/mt/mt_3_panama.png",(0,0), "images/sprites/normal/mt/mt_3_laugh.png",(0,0), "images/sprites/normal/mt/mt_3_pioneer.png") )
            image sl shy dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_dress.png",(0,0), "images/sprites/normal/sl/sl_2_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_dress.png",(0,0), "images/sprites/normal/sl/sl_2_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_dress.png",(0,0), "images/sprites/normal/sl/sl_2_shy.png") )
            image el sad pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/el/el_2_body.png",(0,0), "images/sprites/normal/el/el_2_pioneer.png",(0,0), "images/sprites/normal/el/el_2_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/el/el_2_body.png",(0,0), "images/sprites/normal/el/el_2_pioneer.png",(0,0), "images/sprites/normal/el/el_2_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/el/el_2_body.png",(0,0), "images/sprites/normal/el/el_2_pioneer.png",(0,0), "images/sprites/normal/el/el_2_sad.png") )
            image un surprise sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_sport.png",(0,0), "images/sprites/normal/un/un_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_sport.png",(0,0), "images/sprites/normal/un/un_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_sport.png",(0,0), "images/sprites/normal/un/un_2_surprise.png") )
            image mt surprise panama pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_panama.png",(0,0), "images/sprites/normal/mt/mt_1_surprise.png",(0,0), "images/sprites/normal/mt/mt_1_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_panama.png",(0,0), "images/sprites/normal/mt/mt_1_surprise.png",(0,0), "images/sprites/normal/mt/mt_1_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_panama.png",(0,0), "images/sprites/normal/mt/mt_1_surprise.png",(0,0), "images/sprites/normal/mt/mt_1_pioneer.png") )
            image us angry dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_dress.png",(0,0), "images/sprites/normal/us/us_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_dress.png",(0,0), "images/sprites/normal/us/us_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_dress.png",(0,0), "images/sprites/normal/us/us_2_angry.png") )
            image sl serious sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_1_body.png",(0,0), "images/sprites/normal/sl/sl_1_sport.png",(0,0), "images/sprites/normal/sl/sl_1_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_1_body.png",(0,0), "images/sprites/normal/sl/sl_1_sport.png",(0,0), "images/sprites/normal/sl/sl_1_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_1_body.png",(0,0), "images/sprites/normal/sl/sl_1_sport.png",(0,0), "images/sprites/normal/sl/sl_1_serious.png") )
            image un scared sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_sport.png",(0,0), "images/sprites/normal/un/un_2_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_sport.png",(0,0), "images/sprites/normal/un/un_2_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_sport.png",(0,0), "images/sprites/normal/un/un_2_scared.png") )
            image un cry dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_dress.png",(0,0), "images/sprites/normal/un/un_2_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_dress.png",(0,0), "images/sprites/normal/un/un_2_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_dress.png",(0,0), "images/sprites/normal/un/un_2_cry.png") )
            image dv scared pioneer2 = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_1_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_1_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_1_scared.png") )
            image dv shocked pioneer2 = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_1_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_1_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_1_shocked.png") )
            image sl laugh swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_swim.png",(0,0), "images/sprites/normal/sl/sl_2_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_swim.png",(0,0), "images/sprites/normal/sl/sl_2_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_swim.png",(0,0), "images/sprites/normal/sl/sl_2_laugh.png") )
            image us surp1 dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_dress.png",(0,0), "images/sprites/normal/us/us_3_surp1.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_dress.png",(0,0), "images/sprites/normal/us/us_3_surp1.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_dress.png",(0,0), "images/sprites/normal/us/us_3_surp1.png") )
            image dv shocked swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_swim.png",(0,0), "images/sprites/normal/dv/dv_1_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_swim.png",(0,0), "images/sprites/normal/dv/dv_1_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_swim.png",(0,0), "images/sprites/normal/dv/dv_1_shocked.png") )
            image sh laugh = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_1_body.png",(0,0), "images/sprites/normal/sh/sh_1_laugh.png",(0,0), "images/sprites/normal/sh/sh_1_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_1_body.png",(0,0), "images/sprites/normal/sh/sh_1_laugh.png",(0,0), "images/sprites/normal/sh/sh_1_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_1_body.png",(0,0), "images/sprites/normal/sh/sh_1_laugh.png",(0,0), "images/sprites/normal/sh/sh_1_laugh.png") )
            image us surp2 dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_dress.png",(0,0), "images/sprites/normal/us/us_3_surp2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_dress.png",(0,0), "images/sprites/normal/us/us_3_surp2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_dress.png",(0,0), "images/sprites/normal/us/us_3_surp2.png") )
            image uv sad = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/uv/uv_1_body.png",(0,0), "images/sprites/normal/uv/uv_1_pioneer.png",(0,0), "images/sprites/normal/uv/uv_1_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/uv/uv_1_body.png",(0,0), "images/sprites/normal/uv/uv_1_pioneer.png",(0,0), "images/sprites/normal/uv/uv_1_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/uv/uv_1_body.png",(0,0), "images/sprites/normal/uv/uv_1_pioneer.png",(0,0), "images/sprites/normal/uv/uv_1_sad.png") )
            image el angry pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/el/el_3_body.png",(0,0), "images/sprites/normal/el/el_3_pioneer.png",(0,0), "images/sprites/normal/el/el_3_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/el/el_3_body.png",(0,0), "images/sprites/normal/el/el_3_pioneer.png",(0,0), "images/sprites/normal/el/el_3_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/el/el_3_body.png",(0,0), "images/sprites/normal/el/el_3_pioneer.png",(0,0), "images/sprites/normal/el/el_3_angry.png") )
            image us cry2 dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_dress.png",(0,0), "images/sprites/normal/us/us_3_cry2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_dress.png",(0,0), "images/sprites/normal/us/us_3_cry2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_dress.png",(0,0), "images/sprites/normal/us/us_3_cry2.png") )
            image sl sad sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_3_body.png",(0,0), "images/sprites/normal/sl/sl_3_sport.png",(0,0), "images/sprites/normal/sl/sl_3_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_3_body.png",(0,0), "images/sprites/normal/sl/sl_3_sport.png",(0,0), "images/sprites/normal/sl/sl_3_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_3_body.png",(0,0), "images/sprites/normal/sl/sl_3_sport.png",(0,0), "images/sprites/normal/sl/sl_3_sad.png") )
            image mi scared swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_swim.png",(0,0), "images/sprites/normal/mi/mi_1_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_swim.png",(0,0), "images/sprites/normal/mi/mi_1_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_swim.png",(0,0), "images/sprites/normal/mi/mi_1_scared.png") )
            image us laugh swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_swim.png",(0,0), "images/sprites/normal/us/us_1_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_swim.png",(0,0), "images/sprites/normal/us/us_1_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_swim.png",(0,0), "images/sprites/normal/us/us_1_laugh.png") )
            image mi surprise swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_swim.png",(0,0), "images/sprites/normal/mi/mi_1_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_swim.png",(0,0), "images/sprites/normal/mi/mi_1_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_swim.png",(0,0), "images/sprites/normal/mi/mi_1_surprise.png") )
            image sl smile swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_1_body.png",(0,0), "images/sprites/normal/sl/sl_1_swim.png",(0,0), "images/sprites/normal/sl/sl_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_1_body.png",(0,0), "images/sprites/normal/sl/sl_1_swim.png",(0,0), "images/sprites/normal/sl/sl_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_1_body.png",(0,0), "images/sprites/normal/sl/sl_1_swim.png",(0,0), "images/sprites/normal/sl/sl_1_smile.png") )
            image us shy2 dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_dress.png",(0,0), "images/sprites/normal/us/us_3_shy2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_dress.png",(0,0), "images/sprites/normal/us/us_3_shy2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_dress.png",(0,0), "images/sprites/normal/us/us_3_shy2.png") )
            image sl surprise swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_3_body.png",(0,0), "images/sprites/normal/sl/sl_3_swim.png",(0,0), "images/sprites/normal/sl/sl_3_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_3_body.png",(0,0), "images/sprites/normal/sl/sl_3_swim.png",(0,0), "images/sprites/normal/sl/sl_3_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_3_body.png",(0,0), "images/sprites/normal/sl/sl_3_swim.png",(0,0), "images/sprites/normal/sl/sl_3_surprise.png") )
            image dv smile pioneer2 = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_4_body.png",(0,0), "images/sprites/normal/dv/dv_4_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_4_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_4_body.png",(0,0), "images/sprites/normal/dv/dv_4_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_4_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_4_body.png",(0,0), "images/sprites/normal/dv/dv_4_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_4_smile.png") )
            image mt sad dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_dress.png",(0,0), "images/sprites/normal/mt/mt_1_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_dress.png",(0,0), "images/sprites/normal/mt/mt_1_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_dress.png",(0,0), "images/sprites/normal/mt/mt_1_sad.png") )
            image mt smile panama pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_panama.png",(0,0), "images/sprites/normal/mt/mt_1_smile.png",(0,0), "images/sprites/normal/mt/mt_1_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_panama.png",(0,0), "images/sprites/normal/mt/mt_1_smile.png",(0,0), "images/sprites/normal/mt/mt_1_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_panama.png",(0,0), "images/sprites/normal/mt/mt_1_smile.png",(0,0), "images/sprites/normal/mt/mt_1_pioneer.png") )
            image dv angry pioneer2 = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_5_body.png",(0,0), "images/sprites/normal/dv/dv_5_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_5_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_5_body.png",(0,0), "images/sprites/normal/dv/dv_5_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_5_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_5_body.png",(0,0), "images/sprites/normal/dv/dv_5_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_5_angry.png") )
            image uv shocked = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/uv/uv_1_body.png",(0,0), "images/sprites/normal/uv/uv_1_pioneer.png",(0,0), "images/sprites/normal/uv/uv_1_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/uv/uv_1_body.png",(0,0), "images/sprites/normal/uv/uv_1_pioneer.png",(0,0), "images/sprites/normal/uv/uv_1_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/uv/uv_1_body.png",(0,0), "images/sprites/normal/uv/uv_1_pioneer.png",(0,0), "images/sprites/normal/uv/uv_1_shocked.png") )
            image mz shy glasses pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_3_body.png",(0,0), "images/sprites/normal/mz/mz_3_glasses.png",(0,0), "images/sprites/normal/mz/mz_3_shy.png",(0,0), "images/sprites/normal/mz/mz_3_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_3_body.png",(0,0), "images/sprites/normal/mz/mz_3_glasses.png",(0,0), "images/sprites/normal/mz/mz_3_shy.png",(0,0), "images/sprites/normal/mz/mz_3_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_3_body.png",(0,0), "images/sprites/normal/mz/mz_3_glasses.png",(0,0), "images/sprites/normal/mz/mz_3_shy.png",(0,0), "images/sprites/normal/mz/mz_3_pioneer.png") )
            image dv sad pioneer2 = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_3_body.png",(0,0), "images/sprites/normal/dv/dv_3_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_3_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_3_body.png",(0,0), "images/sprites/normal/dv/dv_3_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_3_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_3_body.png",(0,0), "images/sprites/normal/dv/dv_3_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_3_sad.png") )
            image us shy dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_dress.png",(0,0), "images/sprites/normal/us/us_3_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_dress.png",(0,0), "images/sprites/normal/us/us_3_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_dress.png",(0,0), "images/sprites/normal/us/us_3_shy.png") )
            image dv normal pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_4_body.png",(0,0), "images/sprites/normal/dv/dv_4_pioneer.png",(0,0), "images/sprites/normal/dv/dv_4_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_4_body.png",(0,0), "images/sprites/normal/dv/dv_4_pioneer.png",(0,0), "images/sprites/normal/dv/dv_4_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_4_body.png",(0,0), "images/sprites/normal/dv/dv_4_pioneer.png",(0,0), "images/sprites/normal/dv/dv_4_normal.png") )
            image us calml pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_pioneer.png",(0,0), "images/sprites/normal/us/us_2_calml.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_pioneer.png",(0,0), "images/sprites/normal/us/us_2_calml.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_pioneer.png",(0,0), "images/sprites/normal/us/us_2_calml.png") )
            image mt sad swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_swim.png",(0,0), "images/sprites/normal/mt/mt_1_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_swim.png",(0,0), "images/sprites/normal/mt/mt_1_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_swim.png",(0,0), "images/sprites/normal/mt/mt_1_sad.png") )
            image sl tender dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_4_body.png",(0,0), "images/sprites/normal/sl/sl_4_dress.png",(0,0), "images/sprites/normal/sl/sl_4_tender.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_4_body.png",(0,0), "images/sprites/normal/sl/sl_4_dress.png",(0,0), "images/sprites/normal/sl/sl_4_tender.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_4_body.png",(0,0), "images/sprites/normal/sl/sl_4_dress.png",(0,0), "images/sprites/normal/sl/sl_4_tender.png") )
            image uv dontlike = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/uv/uv_1_body.png",(0,0), "images/sprites/normal/uv/uv_1_pioneer.png",(0,0), "images/sprites/normal/uv/uv_1_dontlike.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/uv/uv_1_body.png",(0,0), "images/sprites/normal/uv/uv_1_pioneer.png",(0,0), "images/sprites/normal/uv/uv_1_dontlike.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/uv/uv_1_body.png",(0,0), "images/sprites/normal/uv/uv_1_pioneer.png",(0,0), "images/sprites/normal/uv/uv_1_dontlike.png") )
            image sh surprise = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_3_body.png",(0,0), "images/sprites/normal/sh/sh_3_normal.png",(0,0), "images/sprites/normal/sh/sh_3_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_3_body.png",(0,0), "images/sprites/normal/sh/sh_3_normal.png",(0,0), "images/sprites/normal/sh/sh_3_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_3_body.png",(0,0), "images/sprites/normal/sh/sh_3_normal.png",(0,0), "images/sprites/normal/sh/sh_3_surprise.png") )
            image us dontlike swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_swim.png",(0,0), "images/sprites/normal/us/us_2_dontlike.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_swim.png",(0,0), "images/sprites/normal/us/us_2_dontlike.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_swim.png",(0,0), "images/sprites/normal/us/us_2_dontlike.png") )
            image sl angry pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_3_body.png",(0,0), "images/sprites/normal/sl/sl_3_pioneer.png",(0,0), "images/sprites/normal/sl/sl_3_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_3_body.png",(0,0), "images/sprites/normal/sl/sl_3_pioneer.png",(0,0), "images/sprites/normal/sl/sl_3_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_3_body.png",(0,0), "images/sprites/normal/sl/sl_3_pioneer.png",(0,0), "images/sprites/normal/sl/sl_3_angry.png") )
            image us shy pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_pioneer.png",(0,0), "images/sprites/normal/us/us_3_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_pioneer.png",(0,0), "images/sprites/normal/us/us_3_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_pioneer.png",(0,0), "images/sprites/normal/us/us_3_shy.png") )
            image un cry_smile pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_pioneer.png",(0,0), "images/sprites/normal/un/un_2_cry_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_pioneer.png",(0,0), "images/sprites/normal/un/un_2_cry_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_pioneer.png",(0,0), "images/sprites/normal/un/un_2_cry_smile.png") )
            image un shy pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_pioneer.png",(0,0), "images/sprites/normal/un/un_1_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_pioneer.png",(0,0), "images/sprites/normal/un/un_1_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_pioneer.png",(0,0), "images/sprites/normal/un/un_1_shy.png") )
            image mt normal panama swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_panama.png",(0,0), "images/sprites/normal/mt/mt_1_normal.png",(0,0), "images/sprites/normal/mt/mt_1_swim.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_panama.png",(0,0), "images/sprites/normal/mt/mt_1_normal.png",(0,0), "images/sprites/normal/mt/mt_1_swim.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_panama.png",(0,0), "images/sprites/normal/mt/mt_1_normal.png",(0,0), "images/sprites/normal/mt/mt_1_swim.png") )
            image sl normal swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_1_body.png",(0,0), "images/sprites/normal/sl/sl_1_swim.png",(0,0), "images/sprites/normal/sl/sl_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_1_body.png",(0,0), "images/sprites/normal/sl/sl_1_swim.png",(0,0), "images/sprites/normal/sl/sl_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_1_body.png",(0,0), "images/sprites/normal/sl/sl_1_swim.png",(0,0), "images/sprites/normal/sl/sl_1_normal.png") )
            image mz laugh pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_1_body.png",(0,0), "images/sprites/normal/mz/mz_1_pioneer.png",(0,0), "images/sprites/normal/mz/mz_1_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_1_body.png",(0,0), "images/sprites/normal/mz/mz_1_pioneer.png",(0,0), "images/sprites/normal/mz/mz_1_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_1_body.png",(0,0), "images/sprites/normal/mz/mz_1_pioneer.png",(0,0), "images/sprites/normal/mz/mz_1_laugh.png") )
            image dv surprise swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_swim.png",(0,0), "images/sprites/normal/dv/dv_1_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_swim.png",(0,0), "images/sprites/normal/dv/dv_1_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_swim.png",(0,0), "images/sprites/normal/dv/dv_1_surprise.png") )
            image sl laugh pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_pioneer.png",(0,0), "images/sprites/normal/sl/sl_2_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_pioneer.png",(0,0), "images/sprites/normal/sl/sl_2_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_pioneer.png",(0,0), "images/sprites/normal/sl/sl_2_laugh.png") )
            image sh laugh pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_1_body.png",(0,0), "images/sprites/normal/sh/sh_1_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_1_body.png",(0,0), "images/sprites/normal/sh/sh_1_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_1_body.png",(0,0), "images/sprites/normal/sh/sh_1_laugh.png") )
            image sl smile sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_1_body.png",(0,0), "images/sprites/normal/sl/sl_1_sport.png",(0,0), "images/sprites/normal/sl/sl_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_1_body.png",(0,0), "images/sprites/normal/sl/sl_1_sport.png",(0,0), "images/sprites/normal/sl/sl_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_1_body.png",(0,0), "images/sprites/normal/sl/sl_1_sport.png",(0,0), "images/sprites/normal/sl/sl_1_smile.png") )
            image sl scared swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_4_body.png",(0,0), "images/sprites/normal/sl/sl_4_swim.png",(0,0), "images/sprites/normal/sl/sl_4_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_4_body.png",(0,0), "images/sprites/normal/sl/sl_4_swim.png",(0,0), "images/sprites/normal/sl/sl_4_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_4_body.png",(0,0), "images/sprites/normal/sl/sl_4_swim.png",(0,0), "images/sprites/normal/sl/sl_4_scared.png") )
            image un scared dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_dress.png",(0,0), "images/sprites/normal/un/un_2_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_dress.png",(0,0), "images/sprites/normal/un/un_2_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_dress.png",(0,0), "images/sprites/normal/un/un_2_scared.png") )
            image sl serious swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_1_body.png",(0,0), "images/sprites/normal/sl/sl_1_swim.png",(0,0), "images/sprites/normal/sl/sl_1_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_1_body.png",(0,0), "images/sprites/normal/sl/sl_1_swim.png",(0,0), "images/sprites/normal/sl/sl_1_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_1_body.png",(0,0), "images/sprites/normal/sl/sl_1_swim.png",(0,0), "images/sprites/normal/sl/sl_1_serious.png") )
            image mt normal dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_dress.png",(0,0), "images/sprites/normal/mt/mt_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_dress.png",(0,0), "images/sprites/normal/mt/mt_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_dress.png",(0,0), "images/sprites/normal/mt/mt_1_normal.png") )
            image us grin dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_dress.png",(0,0), "images/sprites/normal/us/us_1_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_dress.png",(0,0), "images/sprites/normal/us/us_1_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_dress.png",(0,0), "images/sprites/normal/us/us_1_grin.png") )
            image sl laugh dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_dress.png",(0,0), "images/sprites/normal/sl/sl_2_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_dress.png",(0,0), "images/sprites/normal/sl/sl_2_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_dress.png",(0,0), "images/sprites/normal/sl/sl_2_laugh.png") )
            image us laugh dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_dress.png",(0,0), "images/sprites/normal/us/us_1_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_dress.png",(0,0), "images/sprites/normal/us/us_1_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_dress.png",(0,0), "images/sprites/normal/us/us_1_laugh.png") )
            image dv cry swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_swim.png",(0,0), "images/sprites/normal/dv/dv_1_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_swim.png",(0,0), "images/sprites/normal/dv/dv_1_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_swim.png",(0,0), "images/sprites/normal/dv/dv_1_cry.png") )
            image cs shy stethoscope = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/cs/cs_1_body.png",(0,0), "images/sprites/normal/cs/cs_1_stethoscope.png",(0,0), "images/sprites/normal/cs/cs_1_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/cs/cs_1_body.png",(0,0), "images/sprites/normal/cs/cs_1_stethoscope.png",(0,0), "images/sprites/normal/cs/cs_1_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/cs/cs_1_body.png",(0,0), "images/sprites/normal/cs/cs_1_stethoscope.png",(0,0), "images/sprites/normal/cs/cs_1_shy.png") )
            image sh upset pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_1_body.png",(0,0), "images/sprites/normal/sh/sh_1_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_1_body.png",(0,0), "images/sprites/normal/sh/sh_1_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_1_body.png",(0,0), "images/sprites/normal/sh/sh_1_upset.png") )
            image mz shy pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_3_body.png",(0,0), "images/sprites/normal/mz/mz_3_pioneer.png",(0,0), "images/sprites/normal/mz/mz_3_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_3_body.png",(0,0), "images/sprites/normal/mz/mz_3_pioneer.png",(0,0), "images/sprites/normal/mz/mz_3_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_3_body.png",(0,0), "images/sprites/normal/mz/mz_3_pioneer.png",(0,0), "images/sprites/normal/mz/mz_3_shy.png") )
            image mz laugh glasses pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_1_body.png",(0,0), "images/sprites/normal/mz/mz_1_glasses.png",(0,0), "images/sprites/normal/mz/mz_1_laugh.png",(0,0), "images/sprites/normal/mz/mz_1_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_1_body.png",(0,0), "images/sprites/normal/mz/mz_1_glasses.png",(0,0), "images/sprites/normal/mz/mz_1_laugh.png",(0,0), "images/sprites/normal/mz/mz_1_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_1_body.png",(0,0), "images/sprites/normal/mz/mz_1_glasses.png",(0,0), "images/sprites/normal/mz/mz_1_laugh.png",(0,0), "images/sprites/normal/mz/mz_1_pioneer.png") )
            image mz normal glasses pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_1_body.png",(0,0), "images/sprites/normal/mz/mz_1_glasses.png",(0,0), "images/sprites/normal/mz/mz_1_normal.png",(0,0), "images/sprites/normal/mz/mz_1_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_1_body.png",(0,0), "images/sprites/normal/mz/mz_1_glasses.png",(0,0), "images/sprites/normal/mz/mz_1_normal.png",(0,0), "images/sprites/normal/mz/mz_1_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_1_body.png",(0,0), "images/sprites/normal/mz/mz_1_glasses.png",(0,0), "images/sprites/normal/mz/mz_1_normal.png",(0,0), "images/sprites/normal/mz/mz_1_pioneer.png") )
            image cs shy = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/cs/cs_1_body.png",(0,0), "images/sprites/normal/cs/cs_1_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/cs/cs_1_body.png",(0,0), "images/sprites/normal/cs/cs_1_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/cs/cs_1_body.png",(0,0), "images/sprites/normal/cs/cs_1_shy.png") )
            image pi normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/pi/pi_1_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/pi/pi_1_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/pi/pi_1_pioneer.png") )
            image mz bukal glasses pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_1_body.png",(0,0), "images/sprites/normal/mz/mz_1_glasses.png",(0,0), "images/sprites/normal/mz/mz_1_bukal.png",(0,0), "images/sprites/normal/mz/mz_1_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_1_body.png",(0,0), "images/sprites/normal/mz/mz_1_glasses.png",(0,0), "images/sprites/normal/mz/mz_1_bukal.png",(0,0), "images/sprites/normal/mz/mz_1_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_1_body.png",(0,0), "images/sprites/normal/mz/mz_1_glasses.png",(0,0), "images/sprites/normal/mz/mz_1_bukal.png",(0,0), "images/sprites/normal/mz/mz_1_pioneer.png") )
            image mi rage pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_3_body.png",(0,0), "images/sprites/normal/mi/mi_3_pioneer.png",(0,0), "images/sprites/normal/mi/mi_3_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_3_body.png",(0,0), "images/sprites/normal/mi/mi_3_pioneer.png",(0,0), "images/sprites/normal/mi/mi_3_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_3_body.png",(0,0), "images/sprites/normal/mi/mi_3_pioneer.png",(0,0), "images/sprites/normal/mi/mi_3_rage.png") )
            image sl normal pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_1_body.png",(0,0), "images/sprites/normal/sl/sl_1_pioneer.png",(0,0), "images/sprites/normal/sl/sl_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_1_body.png",(0,0), "images/sprites/normal/sl/sl_1_pioneer.png",(0,0), "images/sprites/normal/sl/sl_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_1_body.png",(0,0), "images/sprites/normal/sl/sl_1_pioneer.png",(0,0), "images/sprites/normal/sl/sl_1_normal.png") )
            image mi rage swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_3_body.png",(0,0), "images/sprites/normal/mi/mi_3_swim.png",(0,0), "images/sprites/normal/mi/mi_3_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_3_body.png",(0,0), "images/sprites/normal/mi/mi_3_swim.png",(0,0), "images/sprites/normal/mi/mi_3_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_3_body.png",(0,0), "images/sprites/normal/mi/mi_3_swim.png",(0,0), "images/sprites/normal/mi/mi_3_rage.png") )
            image el upset pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/el/el_2_body.png",(0,0), "images/sprites/normal/el/el_2_pioneer.png",(0,0), "images/sprites/normal/el/el_2_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/el/el_2_body.png",(0,0), "images/sprites/normal/el/el_2_pioneer.png",(0,0), "images/sprites/normal/el/el_2_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/el/el_2_body.png",(0,0), "images/sprites/normal/el/el_2_pioneer.png",(0,0), "images/sprites/normal/el/el_2_upset.png") )
            image us normal pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_pioneer.png",(0,0), "images/sprites/normal/us/us_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_pioneer.png",(0,0), "images/sprites/normal/us/us_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_pioneer.png",(0,0), "images/sprites/normal/us/us_1_normal.png") )
            image un shy dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_dress.png",(0,0), "images/sprites/normal/un/un_1_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_dress.png",(0,0), "images/sprites/normal/un/un_1_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_dress.png",(0,0), "images/sprites/normal/un/un_1_shy.png") )
            image mt surprise panama swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_panama.png",(0,0), "images/sprites/normal/mt/mt_1_surprise.png",(0,0), "images/sprites/normal/mt/mt_1_swim.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_panama.png",(0,0), "images/sprites/normal/mt/mt_1_surprise.png",(0,0), "images/sprites/normal/mt/mt_1_swim.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_panama.png",(0,0), "images/sprites/normal/mt/mt_1_surprise.png",(0,0), "images/sprites/normal/mt/mt_1_swim.png") )
            image us sad sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_sport.png",(0,0), "images/sprites/normal/us/us_1_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_sport.png",(0,0), "images/sprites/normal/us/us_1_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_sport.png",(0,0), "images/sprites/normal/us/us_1_sad.png") )
            image mi angry swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_3_body.png",(0,0), "images/sprites/normal/mi/mi_3_swim.png",(0,0), "images/sprites/normal/mi/mi_3_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_3_body.png",(0,0), "images/sprites/normal/mi/mi_3_swim.png",(0,0), "images/sprites/normal/mi/mi_3_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_3_body.png",(0,0), "images/sprites/normal/mi/mi_3_swim.png",(0,0), "images/sprites/normal/mi/mi_3_angry.png") )
            image sl happy pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_pioneer.png",(0,0), "images/sprites/normal/sl/sl_2_happy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_pioneer.png",(0,0), "images/sprites/normal/sl/sl_2_happy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_pioneer.png",(0,0), "images/sprites/normal/sl/sl_2_happy.png") )
            image mt sad panama pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_panama.png",(0,0), "images/sprites/normal/mt/mt_1_sad.png",(0,0), "images/sprites/normal/mt/mt_1_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_panama.png",(0,0), "images/sprites/normal/mt/mt_1_sad.png",(0,0), "images/sprites/normal/mt/mt_1_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_panama.png",(0,0), "images/sprites/normal/mt/mt_1_sad.png",(0,0), "images/sprites/normal/mt/mt_1_pioneer.png") )
            image us calml sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_sport.png",(0,0), "images/sprites/normal/us/us_2_calml.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_sport.png",(0,0), "images/sprites/normal/us/us_2_calml.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_sport.png",(0,0), "images/sprites/normal/us/us_2_calml.png") )
            image us shy2 pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_pioneer.png",(0,0), "images/sprites/normal/us/us_3_shy2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_pioneer.png",(0,0), "images/sprites/normal/us/us_3_shy2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_pioneer.png",(0,0), "images/sprites/normal/us/us_3_shy2.png") )
            image un surprise pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_pioneer.png",(0,0), "images/sprites/normal/un/un_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_pioneer.png",(0,0), "images/sprites/normal/un/un_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_pioneer.png",(0,0), "images/sprites/normal/un/un_2_surprise.png") )
            image un surprise pioneer red = im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_pioneer.png",(0,0), "images/sprites/normal/un/un_2_surprise.png"), im.matrix.tint(1, 0.1, 0.1) )
            image us cry sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_sport.png",(0,0), "images/sprites/normal/us/us_3_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_sport.png",(0,0), "images/sprites/normal/us/us_3_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_sport.png",(0,0), "images/sprites/normal/us/us_3_cry.png") )
            image mi angry pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_3_body.png",(0,0), "images/sprites/normal/mi/mi_3_pioneer.png",(0,0), "images/sprites/normal/mi/mi_3_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_3_body.png",(0,0), "images/sprites/normal/mi/mi_3_pioneer.png",(0,0), "images/sprites/normal/mi/mi_3_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_3_body.png",(0,0), "images/sprites/normal/mi/mi_3_pioneer.png",(0,0), "images/sprites/normal/mi/mi_3_angry.png") )
            image us sad pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_pioneer.png",(0,0), "images/sprites/normal/us/us_1_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_pioneer.png",(0,0), "images/sprites/normal/us/us_1_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_pioneer.png",(0,0), "images/sprites/normal/us/us_1_sad.png") )
            image uv smile = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/uv/uv_2_body.png",(0,0), "images/sprites/normal/uv/uv_2_pioneer.png",(0,0), "images/sprites/normal/uv/uv_2_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/uv/uv_2_body.png",(0,0), "images/sprites/normal/uv/uv_2_pioneer.png",(0,0), "images/sprites/normal/uv/uv_2_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/uv/uv_2_body.png",(0,0), "images/sprites/normal/uv/uv_2_pioneer.png",(0,0), "images/sprites/normal/uv/uv_2_smile.png") )
            image un cry swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_swim.png",(0,0), "images/sprites/normal/un/un_2_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_swim.png",(0,0), "images/sprites/normal/un/un_2_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_swim.png",(0,0), "images/sprites/normal/un/un_2_cry.png") )
            image sh normal pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_3_body.png",(0,0), "images/sprites/normal/sh/sh_3_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_3_body.png",(0,0), "images/sprites/normal/sh/sh_3_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_3_body.png",(0,0), "images/sprites/normal/sh/sh_3_normal.png") )
            image sh rage = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_2_body.png",(0,0), "images/sprites/normal/sh/sh_2_rage.png",(0,0), "images/sprites/normal/sh/sh_2_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_2_body.png",(0,0), "images/sprites/normal/sh/sh_2_rage.png",(0,0), "images/sprites/normal/sh/sh_2_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_2_body.png",(0,0), "images/sprites/normal/sh/sh_2_rage.png",(0,0), "images/sprites/normal/sh/sh_2_rage.png") )
            image us normal sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_sport.png",(0,0), "images/sprites/normal/us/us_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_sport.png",(0,0), "images/sprites/normal/us/us_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_sport.png",(0,0), "images/sprites/normal/us/us_1_normal.png") )
            image un angry2 sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_sport.png",(0,0), "images/sprites/normal/un/un_3_angry2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_sport.png",(0,0), "images/sprites/normal/un/un_3_angry2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_sport.png",(0,0), "images/sprites/normal/un/un_3_angry2.png") )
            image sl happy swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_swim.png",(0,0), "images/sprites/normal/sl/sl_2_happy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_swim.png",(0,0), "images/sprites/normal/sl/sl_2_happy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_swim.png",(0,0), "images/sprites/normal/sl/sl_2_happy.png") )
            image mz rage glasses pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_2_body.png",(0,0), "images/sprites/normal/mz/mz_2_glasses.png",(0,0), "images/sprites/normal/mz/mz_2_rage.png",(0,0), "images/sprites/normal/mz/mz_2_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_2_body.png",(0,0), "images/sprites/normal/mz/mz_2_glasses.png",(0,0), "images/sprites/normal/mz/mz_2_rage.png",(0,0), "images/sprites/normal/mz/mz_2_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_2_body.png",(0,0), "images/sprites/normal/mz/mz_2_glasses.png",(0,0), "images/sprites/normal/mz/mz_2_rage.png",(0,0), "images/sprites/normal/mz/mz_2_pioneer.png") )
            image us smile pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_pioneer.png",(0,0), "images/sprites/normal/us/us_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_pioneer.png",(0,0), "images/sprites/normal/us/us_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_pioneer.png",(0,0), "images/sprites/normal/us/us_1_smile.png") )
            image mt angry panama swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_panama.png",(0,0), "images/sprites/normal/mt/mt_2_angry.png",(0,0), "images/sprites/normal/mt/mt_2_swim.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_panama.png",(0,0), "images/sprites/normal/mt/mt_2_angry.png",(0,0), "images/sprites/normal/mt/mt_2_swim.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_panama.png",(0,0), "images/sprites/normal/mt/mt_2_angry.png",(0,0), "images/sprites/normal/mt/mt_2_swim.png") )
            image sh cry pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_2_body.png",(0,0), "images/sprites/normal/sh/sh_2_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_2_body.png",(0,0), "images/sprites/normal/sh/sh_2_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_2_body.png",(0,0), "images/sprites/normal/sh/sh_2_cry.png") )
            image mz smile glasses pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_3_body.png",(0,0), "images/sprites/normal/mz/mz_3_glasses.png",(0,0), "images/sprites/normal/mz/mz_3_smile.png",(0,0), "images/sprites/normal/mz/mz_3_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_3_body.png",(0,0), "images/sprites/normal/mz/mz_3_glasses.png",(0,0), "images/sprites/normal/mz/mz_3_smile.png",(0,0), "images/sprites/normal/mz/mz_3_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_3_body.png",(0,0), "images/sprites/normal/mz/mz_3_glasses.png",(0,0), "images/sprites/normal/mz/mz_3_smile.png",(0,0), "images/sprites/normal/mz/mz_3_pioneer.png") )
            image sh scared pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_1_body.png",(0,0), "images/sprites/normal/sh/sh_1_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_1_body.png",(0,0), "images/sprites/normal/sh/sh_1_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_1_body.png",(0,0), "images/sprites/normal/sh/sh_1_scared.png") )
            image mi upset pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_3_body.png",(0,0), "images/sprites/normal/mi/mi_3_pioneer.png",(0,0), "images/sprites/normal/mi/mi_3_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_3_body.png",(0,0), "images/sprites/normal/mi/mi_3_pioneer.png",(0,0), "images/sprites/normal/mi/mi_3_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_3_body.png",(0,0), "images/sprites/normal/mi/mi_3_pioneer.png",(0,0), "images/sprites/normal/mi/mi_3_upset.png") )
            image mi upset swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_3_body.png",(0,0), "images/sprites/normal/mi/mi_3_swim.png",(0,0), "images/sprites/normal/mi/mi_3_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_3_body.png",(0,0), "images/sprites/normal/mi/mi_3_swim.png",(0,0), "images/sprites/normal/mi/mi_3_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_3_body.png",(0,0), "images/sprites/normal/mi/mi_3_swim.png",(0,0), "images/sprites/normal/mi/mi_3_upset.png") )
            image us normal swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_swim.png",(0,0), "images/sprites/normal/us/us_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_swim.png",(0,0), "images/sprites/normal/us/us_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_swim.png",(0,0), "images/sprites/normal/us/us_1_normal.png") )
            image sh normal = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_3_body.png",(0,0), "images/sprites/normal/sh/sh_3_normal.png",(0,0), "images/sprites/normal/sh/sh_3_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_3_body.png",(0,0), "images/sprites/normal/sh/sh_3_normal.png",(0,0), "images/sprites/normal/sh/sh_3_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_3_body.png",(0,0), "images/sprites/normal/sh/sh_3_normal.png",(0,0), "images/sprites/normal/sh/sh_3_normal.png") )
            image un shocked dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_dress.png",(0,0), "images/sprites/normal/un/un_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_dress.png",(0,0), "images/sprites/normal/un/un_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_dress.png",(0,0), "images/sprites/normal/un/un_2_shocked.png") )
            image un angry sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_sport.png",(0,0), "images/sprites/normal/un/un_1_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_sport.png",(0,0), "images/sprites/normal/un/un_1_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_sport.png",(0,0), "images/sprites/normal/un/un_1_angry.png") )
            image el smile pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/el/el_1_body.png",(0,0), "images/sprites/normal/el/el_1_pioneer.png",(0,0), "images/sprites/normal/el/el_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/el/el_1_body.png",(0,0), "images/sprites/normal/el/el_1_pioneer.png",(0,0), "images/sprites/normal/el/el_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/el/el_1_body.png",(0,0), "images/sprites/normal/el/el_1_pioneer.png",(0,0), "images/sprites/normal/el/el_1_smile.png") )
            image mi cry_smile swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_2_body.png",(0,0), "images/sprites/normal/mi/mi_2_swim.png",(0,0), "images/sprites/normal/mi/mi_2_cry_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_2_body.png",(0,0), "images/sprites/normal/mi/mi_2_swim.png",(0,0), "images/sprites/normal/mi/mi_2_cry_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_2_body.png",(0,0), "images/sprites/normal/mi/mi_2_swim.png",(0,0), "images/sprites/normal/mi/mi_2_cry_smile.png") )
            image mi grin pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_2_body.png",(0,0), "images/sprites/normal/mi/mi_2_pioneer.png",(0,0), "images/sprites/normal/mi/mi_2_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_2_body.png",(0,0), "images/sprites/normal/mi/mi_2_pioneer.png",(0,0), "images/sprites/normal/mi/mi_2_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_2_body.png",(0,0), "images/sprites/normal/mi/mi_2_pioneer.png",(0,0), "images/sprites/normal/mi/mi_2_grin.png") )
            image sl scared dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_4_body.png",(0,0), "images/sprites/normal/sl/sl_4_dress.png",(0,0), "images/sprites/normal/sl/sl_4_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_4_body.png",(0,0), "images/sprites/normal/sl/sl_4_dress.png",(0,0), "images/sprites/normal/sl/sl_4_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_4_body.png",(0,0), "images/sprites/normal/sl/sl_4_dress.png",(0,0), "images/sprites/normal/sl/sl_4_scared.png") )
            image un cry_smile dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_dress.png",(0,0), "images/sprites/normal/un/un_2_cry_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_dress.png",(0,0), "images/sprites/normal/un/un_2_cry_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_dress.png",(0,0), "images/sprites/normal/un/un_2_cry_smile.png") )
            image un cry_smile sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_sport.png",(0,0), "images/sprites/normal/un/un_2_cry_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_sport.png",(0,0), "images/sprites/normal/un/un_2_cry_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_sport.png",(0,0), "images/sprites/normal/un/un_2_cry_smile.png") )
            image un sad sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_sport.png",(0,0), "images/sprites/normal/un/un_2_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_sport.png",(0,0), "images/sprites/normal/un/un_2_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_sport.png",(0,0), "images/sprites/normal/un/un_2_sad.png") )
            image mt surprise panama dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_panama.png",(0,0), "images/sprites/normal/mt/mt_1_surprise.png",(0,0), "images/sprites/normal/mt/mt_1_dress.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_panama.png",(0,0), "images/sprites/normal/mt/mt_1_surprise.png",(0,0), "images/sprites/normal/mt/mt_1_dress.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_panama.png",(0,0), "images/sprites/normal/mt/mt_1_surprise.png",(0,0), "images/sprites/normal/mt/mt_1_dress.png") )
            image dv normal pioneer2 = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_4_body.png",(0,0), "images/sprites/normal/dv/dv_4_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_4_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_4_body.png",(0,0), "images/sprites/normal/dv/dv_4_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_4_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_4_body.png",(0,0), "images/sprites/normal/dv/dv_4_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_4_normal.png") )
            image mz angry glasses pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_2_body.png",(0,0), "images/sprites/normal/mz/mz_2_glasses.png",(0,0), "images/sprites/normal/mz/mz_2_angry.png",(0,0), "images/sprites/normal/mz/mz_2_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_2_body.png",(0,0), "images/sprites/normal/mz/mz_2_glasses.png",(0,0), "images/sprites/normal/mz/mz_2_angry.png",(0,0), "images/sprites/normal/mz/mz_2_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_2_body.png",(0,0), "images/sprites/normal/mz/mz_2_glasses.png",(0,0), "images/sprites/normal/mz/mz_2_angry.png",(0,0), "images/sprites/normal/mz/mz_2_pioneer.png") )
            image us cry2 pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_pioneer.png",(0,0), "images/sprites/normal/us/us_3_cry2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_pioneer.png",(0,0), "images/sprites/normal/us/us_3_cry2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_pioneer.png",(0,0), "images/sprites/normal/us/us_3_cry2.png") )
            image mi sad swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_2_body.png",(0,0), "images/sprites/normal/mi/mi_2_swim.png",(0,0), "images/sprites/normal/mi/mi_2_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_2_body.png",(0,0), "images/sprites/normal/mi/mi_2_swim.png",(0,0), "images/sprites/normal/mi/mi_2_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_2_body.png",(0,0), "images/sprites/normal/mi/mi_2_swim.png",(0,0), "images/sprites/normal/mi/mi_2_sad.png") )
            image un sad swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_swim.png",(0,0), "images/sprites/normal/un/un_2_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_swim.png",(0,0), "images/sprites/normal/un/un_2_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_swim.png",(0,0), "images/sprites/normal/un/un_2_sad.png") )
            image us laugh2 sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_sport.png",(0,0), "images/sprites/normal/us/us_1_laugh2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_sport.png",(0,0), "images/sprites/normal/us/us_1_laugh2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_sport.png",(0,0), "images/sprites/normal/us/us_1_laugh2.png") )
            image dv angry pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_5_body.png",(0,0), "images/sprites/normal/dv/dv_5_pioneer.png",(0,0), "images/sprites/normal/dv/dv_5_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_5_body.png",(0,0), "images/sprites/normal/dv/dv_5_pioneer.png",(0,0), "images/sprites/normal/dv/dv_5_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_5_body.png",(0,0), "images/sprites/normal/dv/dv_5_pioneer.png",(0,0), "images/sprites/normal/dv/dv_5_angry.png") )
            image mt smile pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_pioneer.png",(0,0), "images/sprites/normal/mt/mt_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_pioneer.png",(0,0), "images/sprites/normal/mt/mt_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_pioneer.png",(0,0), "images/sprites/normal/mt/mt_1_smile.png") )
            image mt scared pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_3_body.png",(0,0), "images/sprites/normal/mt/mt_3_pioneer.png",(0,0), "images/sprites/normal/mt/mt_3_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_3_body.png",(0,0), "images/sprites/normal/mt/mt_3_pioneer.png",(0,0), "images/sprites/normal/mt/mt_3_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_3_body.png",(0,0), "images/sprites/normal/mt/mt_3_pioneer.png",(0,0), "images/sprites/normal/mt/mt_3_scared.png") )
            image mi shy swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_swim.png",(0,0), "images/sprites/normal/mi/mi_1_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_swim.png",(0,0), "images/sprites/normal/mi/mi_1_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_swim.png",(0,0), "images/sprites/normal/mi/mi_1_shy.png") )
            image un grin dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_dress.png",(0,0), "images/sprites/normal/un/un_3_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_dress.png",(0,0), "images/sprites/normal/un/un_3_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_dress.png",(0,0), "images/sprites/normal/un/un_3_grin.png") )
            image mt laugh pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_3_body.png",(0,0), "images/sprites/normal/mt/mt_3_pioneer.png",(0,0), "images/sprites/normal/mt/mt_3_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_3_body.png",(0,0), "images/sprites/normal/mt/mt_3_pioneer.png",(0,0), "images/sprites/normal/mt/mt_3_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_3_body.png",(0,0), "images/sprites/normal/mt/mt_3_pioneer.png",(0,0), "images/sprites/normal/mt/mt_3_laugh.png") )
            image un laugh pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_pioneer.png",(0,0), "images/sprites/normal/un/un_3_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_pioneer.png",(0,0), "images/sprites/normal/un/un_3_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_pioneer.png",(0,0), "images/sprites/normal/un/un_3_laugh.png") )
            image dv laugh pioneer2 = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_4_body.png",(0,0), "images/sprites/normal/dv/dv_4_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_4_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_4_body.png",(0,0), "images/sprites/normal/dv/dv_4_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_4_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_4_body.png",(0,0), "images/sprites/normal/dv/dv_4_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_4_laugh.png") )
            image us surp1 pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_pioneer.png",(0,0), "images/sprites/normal/us/us_3_surp1.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_pioneer.png",(0,0), "images/sprites/normal/us/us_3_surp1.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_pioneer.png",(0,0), "images/sprites/normal/us/us_3_surp1.png") )
            image sh rage pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_2_body.png",(0,0), "images/sprites/normal/sh/sh_2_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_2_body.png",(0,0), "images/sprites/normal/sh/sh_2_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_2_body.png",(0,0), "images/sprites/normal/sh/sh_2_rage.png") )
            image mt angry panama dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_panama.png",(0,0), "images/sprites/normal/mt/mt_2_angry.png",(0,0), "images/sprites/normal/mt/mt_2_dress.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_panama.png",(0,0), "images/sprites/normal/mt/mt_2_angry.png",(0,0), "images/sprites/normal/mt/mt_2_dress.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_panama.png",(0,0), "images/sprites/normal/mt/mt_2_angry.png",(0,0), "images/sprites/normal/mt/mt_2_dress.png") )
            image un shocked swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_swim.png",(0,0), "images/sprites/normal/un/un_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_swim.png",(0,0), "images/sprites/normal/un/un_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_swim.png",(0,0), "images/sprites/normal/un/un_2_shocked.png") )
            image un evil_smile dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_dress.png",(0,0), "images/sprites/normal/un/un_1_evil_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_dress.png",(0,0), "images/sprites/normal/un/un_1_evil_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_dress.png",(0,0), "images/sprites/normal/un/un_1_evil_smile.png") )
            image uv laugh = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/uv/uv_3_body.png",(0,0), "images/sprites/normal/uv/uv_3_pioneer.png",(0,0), "images/sprites/normal/uv/uv_3_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/uv/uv_3_body.png",(0,0), "images/sprites/normal/uv/uv_3_pioneer.png",(0,0), "images/sprites/normal/uv/uv_3_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/uv/uv_3_body.png",(0,0), "images/sprites/normal/uv/uv_3_pioneer.png",(0,0), "images/sprites/normal/uv/uv_3_laugh.png") )
            image dv scared swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_swim.png",(0,0), "images/sprites/normal/dv/dv_1_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_swim.png",(0,0), "images/sprites/normal/dv/dv_1_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_swim.png",(0,0), "images/sprites/normal/dv/dv_1_scared.png") )
            image mi shocked swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_swim.png",(0,0), "images/sprites/normal/mi/mi_1_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_swim.png",(0,0), "images/sprites/normal/mi/mi_1_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_swim.png",(0,0), "images/sprites/normal/mi/mi_1_shocked.png") )
            image mt angry pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_pioneer.png",(0,0), "images/sprites/normal/mt/mt_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_pioneer.png",(0,0), "images/sprites/normal/mt/mt_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_pioneer.png",(0,0), "images/sprites/normal/mt/mt_2_angry.png") )
            image el fingal pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/el/el_2_body.png",(0,0), "images/sprites/normal/el/el_2_pioneer.png",(0,0), "images/sprites/normal/el/el_2_fingal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/el/el_2_body.png",(0,0), "images/sprites/normal/el/el_2_pioneer.png",(0,0), "images/sprites/normal/el/el_2_fingal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/el/el_2_body.png",(0,0), "images/sprites/normal/el/el_2_pioneer.png",(0,0), "images/sprites/normal/el/el_2_fingal.png") )
            image us surp3 sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_sport.png",(0,0), "images/sprites/normal/us/us_3_surp3.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_sport.png",(0,0), "images/sprites/normal/us/us_3_surp3.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_sport.png",(0,0), "images/sprites/normal/us/us_3_surp3.png") )
            image sl happy dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_dress.png",(0,0), "images/sprites/normal/sl/sl_2_happy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_dress.png",(0,0), "images/sprites/normal/sl/sl_2_happy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_dress.png",(0,0), "images/sprites/normal/sl/sl_2_happy.png") )
            image sh scared = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_1_body.png",(0,0), "images/sprites/normal/sh/sh_1_laugh.png",(0,0), "images/sprites/normal/sh/sh_1_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_1_body.png",(0,0), "images/sprites/normal/sh/sh_1_laugh.png",(0,0), "images/sprites/normal/sh/sh_1_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sh/sh_1_body.png",(0,0), "images/sprites/normal/sh/sh_1_laugh.png",(0,0), "images/sprites/normal/sh/sh_1_scared.png") )
            image un angry2 pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_pioneer.png",(0,0), "images/sprites/normal/un/un_3_angry2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_pioneer.png",(0,0), "images/sprites/normal/un/un_3_angry2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_pioneer.png",(0,0), "images/sprites/normal/un/un_3_angry2.png") )
            image uv grin = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/uv/uv_3_body.png",(0,0), "images/sprites/normal/uv/uv_3_pioneer.png",(0,0), "images/sprites/normal/uv/uv_3_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/uv/uv_3_body.png",(0,0), "images/sprites/normal/uv/uv_3_pioneer.png",(0,0), "images/sprites/normal/uv/uv_3_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/uv/uv_3_body.png",(0,0), "images/sprites/normal/uv/uv_3_pioneer.png",(0,0), "images/sprites/normal/uv/uv_3_grin.png") )
            image mi shy pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_pioneer.png",(0,0), "images/sprites/normal/mi/mi_1_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_pioneer.png",(0,0), "images/sprites/normal/mi/mi_1_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_pioneer.png",(0,0), "images/sprites/normal/mi/mi_1_shy.png") )
            image sl sad pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_3_body.png",(0,0), "images/sprites/normal/sl/sl_3_pioneer.png",(0,0), "images/sprites/normal/sl/sl_3_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_3_body.png",(0,0), "images/sprites/normal/sl/sl_3_pioneer.png",(0,0), "images/sprites/normal/sl/sl_3_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_3_body.png",(0,0), "images/sprites/normal/sl/sl_3_pioneer.png",(0,0), "images/sprites/normal/sl/sl_3_sad.png") )
            image un smile2 sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_sport.png",(0,0), "images/sprites/normal/un/un_1_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_sport.png",(0,0), "images/sprites/normal/un/un_1_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_sport.png",(0,0), "images/sprites/normal/un/un_1_smile2.png") )
            image us cry dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_dress.png",(0,0), "images/sprites/normal/us/us_3_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_dress.png",(0,0), "images/sprites/normal/us/us_3_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_dress.png",(0,0), "images/sprites/normal/us/us_3_cry.png") )
            image un rage pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_pioneer.png",(0,0), "images/sprites/normal/un/un_3_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_pioneer.png",(0,0), "images/sprites/normal/un/un_3_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_pioneer.png",(0,0), "images/sprites/normal/un/un_3_rage.png") )
            image sl sad swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_3_body.png",(0,0), "images/sprites/normal/sl/sl_3_swim.png",(0,0), "images/sprites/normal/sl/sl_3_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_3_body.png",(0,0), "images/sprites/normal/sl/sl_3_swim.png",(0,0), "images/sprites/normal/sl/sl_3_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_3_body.png",(0,0), "images/sprites/normal/sl/sl_3_swim.png",(0,0), "images/sprites/normal/sl/sl_3_sad.png") )
            image mi normal pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_3_body.png",(0,0), "images/sprites/normal/mi/mi_3_pioneer.png",(0,0), "images/sprites/normal/mi/mi_3_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_3_body.png",(0,0), "images/sprites/normal/mi/mi_3_pioneer.png",(0,0), "images/sprites/normal/mi/mi_3_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_3_body.png",(0,0), "images/sprites/normal/mi/mi_3_pioneer.png",(0,0), "images/sprites/normal/mi/mi_3_normal.png") )
            image us surp1 sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_sport.png",(0,0), "images/sprites/normal/us/us_3_surp1.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_sport.png",(0,0), "images/sprites/normal/us/us_3_surp1.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_sport.png",(0,0), "images/sprites/normal/us/us_3_surp1.png") )
            image us cry swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_swim.png",(0,0), "images/sprites/normal/us/us_3_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_swim.png",(0,0), "images/sprites/normal/us/us_3_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_swim.png",(0,0), "images/sprites/normal/us/us_3_cry.png") )
            image un serious dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_dress.png",(0,0), "images/sprites/normal/un/un_3_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_dress.png",(0,0), "images/sprites/normal/un/un_3_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_dress.png",(0,0), "images/sprites/normal/un/un_3_serious.png") )
            image un laugh sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_sport.png",(0,0), "images/sprites/normal/un/un_3_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_sport.png",(0,0), "images/sprites/normal/un/un_3_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_sport.png",(0,0), "images/sprites/normal/un/un_3_laugh.png") )
            image un surprise dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_dress.png",(0,0), "images/sprites/normal/un/un_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_dress.png",(0,0), "images/sprites/normal/un/un_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_dress.png",(0,0), "images/sprites/normal/un/un_2_surprise.png") )
            image mi happy swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_2_body.png",(0,0), "images/sprites/normal/mi/mi_2_swim.png",(0,0), "images/sprites/normal/mi/mi_2_happy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_2_body.png",(0,0), "images/sprites/normal/mi/mi_2_swim.png",(0,0), "images/sprites/normal/mi/mi_2_happy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_2_body.png",(0,0), "images/sprites/normal/mi/mi_2_swim.png",(0,0), "images/sprites/normal/mi/mi_2_happy.png") )
            image mi serious swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_3_body.png",(0,0), "images/sprites/normal/mi/mi_3_swim.png",(0,0), "images/sprites/normal/mi/mi_3_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_3_body.png",(0,0), "images/sprites/normal/mi/mi_3_swim.png",(0,0), "images/sprites/normal/mi/mi_3_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_3_body.png",(0,0), "images/sprites/normal/mi/mi_3_swim.png",(0,0), "images/sprites/normal/mi/mi_3_serious.png") )
            image uv surprise2 = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/uv/uv_3_body.png",(0,0), "images/sprites/normal/uv/uv_3_pioneer.png",(0,0), "images/sprites/normal/uv/uv_3_surprise2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/uv/uv_3_body.png",(0,0), "images/sprites/normal/uv/uv_3_pioneer.png",(0,0), "images/sprites/normal/uv/uv_3_surprise2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/uv/uv_3_body.png",(0,0), "images/sprites/normal/uv/uv_3_pioneer.png",(0,0), "images/sprites/normal/uv/uv_3_surprise2.png") )
            image mz angry pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_2_body.png",(0,0), "images/sprites/normal/mz/mz_2_pioneer.png",(0,0), "images/sprites/normal/mz/mz_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_2_body.png",(0,0), "images/sprites/normal/mz/mz_2_pioneer.png",(0,0), "images/sprites/normal/mz/mz_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_2_body.png",(0,0), "images/sprites/normal/mz/mz_2_pioneer.png",(0,0), "images/sprites/normal/mz/mz_2_angry.png") )
            image un sad pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_pioneer.png",(0,0), "images/sprites/normal/un/un_2_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_pioneer.png",(0,0), "images/sprites/normal/un/un_2_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_pioneer.png",(0,0), "images/sprites/normal/un/un_2_sad.png") )
            image dv surprise pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_pioneer.png",(0,0), "images/sprites/normal/dv/dv_1_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_pioneer.png",(0,0), "images/sprites/normal/dv/dv_1_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_pioneer.png",(0,0), "images/sprites/normal/dv/dv_1_surprise.png") )
            image mz bukal pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_1_body.png",(0,0), "images/sprites/normal/mz/mz_1_pioneer.png",(0,0), "images/sprites/normal/mz/mz_1_bukal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_1_body.png",(0,0), "images/sprites/normal/mz/mz_1_pioneer.png",(0,0), "images/sprites/normal/mz/mz_1_bukal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mz/mz_1_body.png",(0,0), "images/sprites/normal/mz/mz_1_pioneer.png",(0,0), "images/sprites/normal/mz/mz_1_bukal.png") )
            image mi shocked pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_pioneer.png",(0,0), "images/sprites/normal/mi/mi_1_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_pioneer.png",(0,0), "images/sprites/normal/mi/mi_1_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_pioneer.png",(0,0), "images/sprites/normal/mi/mi_1_shocked.png") )
            image sl happy sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_sport.png",(0,0), "images/sprites/normal/sl/sl_2_happy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_sport.png",(0,0), "images/sprites/normal/sl/sl_2_happy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_2_body.png",(0,0), "images/sprites/normal/sl/sl_2_sport.png",(0,0), "images/sprites/normal/sl/sl_2_happy.png") )
            image un sad dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_dress.png",(0,0), "images/sprites/normal/un/un_2_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_dress.png",(0,0), "images/sprites/normal/un/un_2_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_dress.png",(0,0), "images/sprites/normal/un/un_2_sad.png") )
            image dv cry pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_pioneer.png",(0,0), "images/sprites/normal/dv/dv_1_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_pioneer.png",(0,0), "images/sprites/normal/dv/dv_1_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_pioneer.png",(0,0), "images/sprites/normal/dv/dv_1_cry.png") )
            image sl angry swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_3_body.png",(0,0), "images/sprites/normal/sl/sl_3_swim.png",(0,0), "images/sprites/normal/sl/sl_3_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_3_body.png",(0,0), "images/sprites/normal/sl/sl_3_swim.png",(0,0), "images/sprites/normal/sl/sl_3_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_3_body.png",(0,0), "images/sprites/normal/sl/sl_3_swim.png",(0,0), "images/sprites/normal/sl/sl_3_angry.png") )
            image un rage dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_dress.png",(0,0), "images/sprites/normal/un/un_3_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_dress.png",(0,0), "images/sprites/normal/un/un_3_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_dress.png",(0,0), "images/sprites/normal/un/un_3_rage.png") )
            image us normal dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_dress.png",(0,0), "images/sprites/normal/us/us_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_dress.png",(0,0), "images/sprites/normal/us/us_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_1_body.png",(0,0), "images/sprites/normal/us/us_1_dress.png",(0,0), "images/sprites/normal/us/us_1_normal.png") )
            image sl angry sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_3_body.png",(0,0), "images/sprites/normal/sl/sl_3_sport.png",(0,0), "images/sprites/normal/sl/sl_3_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_3_body.png",(0,0), "images/sprites/normal/sl/sl_3_sport.png",(0,0), "images/sprites/normal/sl/sl_3_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/sl/sl_3_body.png",(0,0), "images/sprites/normal/sl/sl_3_sport.png",(0,0), "images/sprites/normal/sl/sl_3_angry.png") )
            image us fear pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_pioneer.png",(0,0), "images/sprites/normal/us/us_2_fear.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_pioneer.png",(0,0), "images/sprites/normal/us/us_2_fear.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_pioneer.png",(0,0), "images/sprites/normal/us/us_2_fear.png") )
            image mt normal panama dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_panama.png",(0,0), "images/sprites/normal/mt/mt_1_normal.png",(0,0), "images/sprites/normal/mt/mt_1_dress.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_panama.png",(0,0), "images/sprites/normal/mt/mt_1_normal.png",(0,0), "images/sprites/normal/mt/mt_1_dress.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_1_body.png",(0,0), "images/sprites/normal/mt/mt_1_panama.png",(0,0), "images/sprites/normal/mt/mt_1_normal.png",(0,0), "images/sprites/normal/mt/mt_1_dress.png") )
            image mi serious pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_3_body.png",(0,0), "images/sprites/normal/mi/mi_3_pioneer.png",(0,0), "images/sprites/normal/mi/mi_3_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_3_body.png",(0,0), "images/sprites/normal/mi/mi_3_pioneer.png",(0,0), "images/sprites/normal/mi/mi_3_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_3_body.png",(0,0), "images/sprites/normal/mi/mi_3_pioneer.png",(0,0), "images/sprites/normal/mi/mi_3_serious.png") )
            image un shocked pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_pioneer.png",(0,0), "images/sprites/normal/un/un_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_pioneer.png",(0,0), "images/sprites/normal/un/un_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_pioneer.png",(0,0), "images/sprites/normal/un/un_2_shocked.png") )
            image dv grin pioneer2 = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_2_body.png",(0,0), "images/sprites/normal/dv/dv_2_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_2_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_2_body.png",(0,0), "images/sprites/normal/dv/dv_2_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_2_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_2_body.png",(0,0), "images/sprites/normal/dv/dv_2_pioneer2.png",(0,0), "images/sprites/normal/dv/dv_2_grin.png") )
            image dv grin pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_2_body.png",(0,0), "images/sprites/normal/dv/dv_2_pioneer.png",(0,0), "images/sprites/normal/dv/dv_2_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_2_body.png",(0,0), "images/sprites/normal/dv/dv_2_pioneer.png",(0,0), "images/sprites/normal/dv/dv_2_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_2_body.png",(0,0), "images/sprites/normal/dv/dv_2_pioneer.png",(0,0), "images/sprites/normal/dv/dv_2_grin.png") )
            image mt rage dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_dress.png",(0,0), "images/sprites/normal/mt/mt_2_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_dress.png",(0,0), "images/sprites/normal/mt/mt_2_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_dress.png",(0,0), "images/sprites/normal/mt/mt_2_rage.png") )
            image us angry sport = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_sport.png",(0,0), "images/sprites/normal/us/us_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_sport.png",(0,0), "images/sprites/normal/us/us_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_sport.png",(0,0), "images/sprites/normal/us/us_2_angry.png") )
            image mi grin swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_2_body.png",(0,0), "images/sprites/normal/mi/mi_2_swim.png",(0,0), "images/sprites/normal/mi/mi_2_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_2_body.png",(0,0), "images/sprites/normal/mi/mi_2_swim.png",(0,0), "images/sprites/normal/mi/mi_2_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_2_body.png",(0,0), "images/sprites/normal/mi/mi_2_swim.png",(0,0), "images/sprites/normal/mi/mi_2_grin.png") )
            image mt angry swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_swim.png",(0,0), "images/sprites/normal/mt/mt_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_swim.png",(0,0), "images/sprites/normal/mt/mt_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_swim.png",(0,0), "images/sprites/normal/mt/mt_2_angry.png") )
            image un surprise swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_swim.png",(0,0), "images/sprites/normal/un/un_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_swim.png",(0,0), "images/sprites/normal/un/un_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_swim.png",(0,0), "images/sprites/normal/un/un_2_surprise.png") )
            image el shocked pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/el/el_2_body.png",(0,0), "images/sprites/normal/el/el_2_pioneer.png",(0,0), "images/sprites/normal/el/el_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/el/el_2_body.png",(0,0), "images/sprites/normal/el/el_2_pioneer.png",(0,0), "images/sprites/normal/el/el_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/el/el_2_body.png",(0,0), "images/sprites/normal/el/el_2_pioneer.png",(0,0), "images/sprites/normal/el/el_2_shocked.png") )
            image us calml dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_dress.png",(0,0), "images/sprites/normal/us/us_2_calml.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_dress.png",(0,0), "images/sprites/normal/us/us_2_calml.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_2_body.png",(0,0), "images/sprites/normal/us/us_2_dress.png",(0,0), "images/sprites/normal/us/us_2_calml.png") )
            image us surp3 dress = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_dress.png",(0,0), "images/sprites/normal/us/us_3_surp3.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_dress.png",(0,0), "images/sprites/normal/us/us_3_surp3.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/us/us_3_body.png",(0,0), "images/sprites/normal/us/us_3_dress.png",(0,0), "images/sprites/normal/us/us_3_surp3.png") )
            image un smile swim = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_swim.png",(0,0), "images/sprites/normal/un/un_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_swim.png",(0,0), "images/sprites/normal/un/un_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_swim.png",(0,0), "images/sprites/normal/un/un_1_smile.png") )
            image mi surprise pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_pioneer.png",(0,0), "images/sprites/normal/mi/mi_1_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_pioneer.png",(0,0), "images/sprites/normal/mi/mi_1_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mi/mi_1_body.png",(0,0), "images/sprites/normal/mi/mi_1_pioneer.png",(0,0), "images/sprites/normal/mi/mi_1_surprise.png") )
            image cs normal stethoscope close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/cs/cs_1_body.png",(0,0), "images/sprites/close/cs/cs_1_stethoscope.png",(0,0), "images/sprites/close/cs/cs_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/cs/cs_1_body.png",(0,0), "images/sprites/close/cs/cs_1_stethoscope.png",(0,0), "images/sprites/close/cs/cs_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/cs/cs_1_body.png",(0,0), "images/sprites/close/cs/cs_1_stethoscope.png",(0,0), "images/sprites/close/cs/cs_1_normal.png") )
            image dv grin swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_2_body.png",(0,0), "images/sprites/close/dv/dv_2_swim.png",(0,0), "images/sprites/close/dv/dv_2_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_2_body.png",(0,0), "images/sprites/close/dv/dv_2_swim.png",(0,0), "images/sprites/close/dv/dv_2_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_2_body.png",(0,0), "images/sprites/close/dv/dv_2_swim.png",(0,0), "images/sprites/close/dv/dv_2_grin.png") )
            image dv laugh swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_4_body.png",(0,0), "images/sprites/close/dv/dv_4_swim.png",(0,0), "images/sprites/close/dv/dv_4_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_4_body.png",(0,0), "images/sprites/close/dv/dv_4_swim.png",(0,0), "images/sprites/close/dv/dv_4_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_4_body.png",(0,0), "images/sprites/close/dv/dv_4_swim.png",(0,0), "images/sprites/close/dv/dv_4_laugh.png") )
            image dv scared pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_pioneer.png",(0,0), "images/sprites/close/dv/dv_1_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_pioneer.png",(0,0), "images/sprites/close/dv/dv_1_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_pioneer.png",(0,0), "images/sprites/close/dv/dv_1_scared.png") )
            image sl smile2 sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_sport.png",(0,0), "images/sprites/close/sl/sl_2_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_sport.png",(0,0), "images/sprites/close/sl/sl_2_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_sport.png",(0,0), "images/sprites/close/sl/sl_2_smile2.png") )
            image dv rage pioneer2 close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_5_body.png",(0,0), "images/sprites/close/dv/dv_5_pioneer2.png",(0,0), "images/sprites/close/dv/dv_5_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_5_body.png",(0,0), "images/sprites/close/dv/dv_5_pioneer2.png",(0,0), "images/sprites/close/dv/dv_5_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_5_body.png",(0,0), "images/sprites/close/dv/dv_5_pioneer2.png",(0,0), "images/sprites/close/dv/dv_5_rage.png") )
            image mi scared pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_pioneer.png",(0,0), "images/sprites/close/mi/mi_1_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_pioneer.png",(0,0), "images/sprites/close/mi/mi_1_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_pioneer.png",(0,0), "images/sprites/close/mi/mi_1_scared.png") )
            image us grin pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_pioneer.png",(0,0), "images/sprites/close/us/us_1_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_pioneer.png",(0,0), "images/sprites/close/us/us_1_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_pioneer.png",(0,0), "images/sprites/close/us/us_1_grin.png") )
            image un angry swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_swim.png",(0,0), "images/sprites/close/un/un_1_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_swim.png",(0,0), "images/sprites/close/un/un_1_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_swim.png",(0,0), "images/sprites/close/un/un_1_angry.png") )
            image mi happy pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_2_body.png",(0,0), "images/sprites/close/mi/mi_2_pioneer.png",(0,0), "images/sprites/close/mi/mi_2_happy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_2_body.png",(0,0), "images/sprites/close/mi/mi_2_pioneer.png",(0,0), "images/sprites/close/mi/mi_2_happy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_2_body.png",(0,0), "images/sprites/close/mi/mi_2_pioneer.png",(0,0), "images/sprites/close/mi/mi_2_happy.png") )
            image un serious pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_pioneer.png",(0,0), "images/sprites/close/un/un_3_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_pioneer.png",(0,0), "images/sprites/close/un/un_3_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_pioneer.png",(0,0), "images/sprites/close/un/un_3_serious.png") )
            image us surp2 sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_sport.png",(0,0), "images/sprites/close/us/us_3_surp2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_sport.png",(0,0), "images/sprites/close/us/us_3_surp2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_sport.png",(0,0), "images/sprites/close/us/us_3_surp2.png") )
            image un smile2 dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_dress.png",(0,0), "images/sprites/close/un/un_1_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_dress.png",(0,0), "images/sprites/close/un/un_1_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_dress.png",(0,0), "images/sprites/close/un/un_1_smile2.png") )
            image us surp2 pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_pioneer.png",(0,0), "images/sprites/close/us/us_3_surp2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_pioneer.png",(0,0), "images/sprites/close/us/us_3_surp2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_pioneer.png",(0,0), "images/sprites/close/us/us_3_surp2.png") )
            image sl shy sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_sport.png",(0,0), "images/sprites/close/sl/sl_2_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_sport.png",(0,0), "images/sprites/close/sl/sl_2_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_sport.png",(0,0), "images/sprites/close/sl/sl_2_shy.png") )
            image cs smile close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/cs/cs_1_body.png",(0,0), "images/sprites/close/cs/cs_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/cs/cs_1_body.png",(0,0), "images/sprites/close/cs/cs_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/cs/cs_1_body.png",(0,0), "images/sprites/close/cs/cs_1_smile.png") )
            image mz rage pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_2_body.png",(0,0), "images/sprites/close/mz/mz_2_pioneer.png",(0,0), "images/sprites/close/mz/mz_2_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_2_body.png",(0,0), "images/sprites/close/mz/mz_2_pioneer.png",(0,0), "images/sprites/close/mz/mz_2_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_2_body.png",(0,0), "images/sprites/close/mz/mz_2_pioneer.png",(0,0), "images/sprites/close/mz/mz_2_rage.png") )
            image un cry sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_sport.png",(0,0), "images/sprites/close/un/un_2_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_sport.png",(0,0), "images/sprites/close/un/un_2_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_sport.png",(0,0), "images/sprites/close/un/un_2_cry.png") )
            image un evil_smile swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_swim.png",(0,0), "images/sprites/close/un/un_1_evil_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_swim.png",(0,0), "images/sprites/close/un/un_1_evil_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_swim.png",(0,0), "images/sprites/close/un/un_1_evil_smile.png") )
            image sh smile pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_1_body.png",(0,0), "images/sprites/close/sh/sh_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_1_body.png",(0,0), "images/sprites/close/sh/sh_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_1_body.png",(0,0), "images/sprites/close/sh/sh_1_smile.png") )
            image us sad swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_swim.png",(0,0), "images/sprites/close/us/us_1_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_swim.png",(0,0), "images/sprites/close/us/us_1_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_swim.png",(0,0), "images/sprites/close/us/us_1_sad.png") )
            image sh cry close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_2_body.png",(0,0), "images/sprites/close/sh/sh_2_rage.png",(0,0), "images/sprites/close/sh/sh_2_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_2_body.png",(0,0), "images/sprites/close/sh/sh_2_rage.png",(0,0), "images/sprites/close/sh/sh_2_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_2_body.png",(0,0), "images/sprites/close/sh/sh_2_rage.png",(0,0), "images/sprites/close/sh/sh_2_cry.png") )
            image sh surprise pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_3_body.png",(0,0), "images/sprites/close/sh/sh_3_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_3_body.png",(0,0), "images/sprites/close/sh/sh_3_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_3_body.png",(0,0), "images/sprites/close/sh/sh_3_surprise.png") )
            image mt grin panama pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_3_body.png",(0,0), "images/sprites/close/mt/mt_3_panama.png",(0,0), "images/sprites/close/mt/mt_3_grin.png",(0,0), "images/sprites/close/mt/mt_3_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_3_body.png",(0,0), "images/sprites/close/mt/mt_3_panama.png",(0,0), "images/sprites/close/mt/mt_3_grin.png",(0,0), "images/sprites/close/mt/mt_3_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_3_body.png",(0,0), "images/sprites/close/mt/mt_3_panama.png",(0,0), "images/sprites/close/mt/mt_3_grin.png",(0,0), "images/sprites/close/mt/mt_3_pioneer.png") )
            image dv sad pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_3_body.png",(0,0), "images/sprites/close/dv/dv_3_pioneer.png",(0,0), "images/sprites/close/dv/dv_3_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_3_body.png",(0,0), "images/sprites/close/dv/dv_3_pioneer.png",(0,0), "images/sprites/close/dv/dv_3_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_3_body.png",(0,0), "images/sprites/close/dv/dv_3_pioneer.png",(0,0), "images/sprites/close/dv/dv_3_sad.png") )
            image mt smile panama swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_panama.png",(0,0), "images/sprites/close/mt/mt_1_smile.png",(0,0), "images/sprites/close/mt/mt_1_swim.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_panama.png",(0,0), "images/sprites/close/mt/mt_1_smile.png",(0,0), "images/sprites/close/mt/mt_1_swim.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_panama.png",(0,0), "images/sprites/close/mt/mt_1_smile.png",(0,0), "images/sprites/close/mt/mt_1_swim.png") )
            image dv cry pioneer2 close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_pioneer2.png",(0,0), "images/sprites/close/dv/dv_1_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_pioneer2.png",(0,0), "images/sprites/close/dv/dv_1_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_pioneer2.png",(0,0), "images/sprites/close/dv/dv_1_cry.png") )
            image mt rage panama pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_2_body.png",(0,0), "images/sprites/close/mt/mt_2_panama.png",(0,0), "images/sprites/close/mt/mt_2_rage.png",(0,0), "images/sprites/close/mt/mt_2_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_2_body.png",(0,0), "images/sprites/close/mt/mt_2_panama.png",(0,0), "images/sprites/close/mt/mt_2_rage.png",(0,0), "images/sprites/close/mt/mt_2_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_2_body.png",(0,0), "images/sprites/close/mt/mt_2_panama.png",(0,0), "images/sprites/close/mt/mt_2_rage.png",(0,0), "images/sprites/close/mt/mt_2_pioneer.png") )
            image un smile dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_dress.png",(0,0), "images/sprites/close/un/un_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_dress.png",(0,0), "images/sprites/close/un/un_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_dress.png",(0,0), "images/sprites/close/un/un_1_smile.png") )
            image mi dontlike swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_swim.png",(0,0), "images/sprites/close/mi/mi_1_dontlike.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_swim.png",(0,0), "images/sprites/close/mi/mi_1_dontlike.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_swim.png",(0,0), "images/sprites/close/mi/mi_1_dontlike.png") )
            image un angry2 dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_dress.png",(0,0), "images/sprites/close/un/un_3_angry2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_dress.png",(0,0), "images/sprites/close/un/un_3_angry2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_dress.png",(0,0), "images/sprites/close/un/un_3_angry2.png") )
            image sl serious dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_1_body.png",(0,0), "images/sprites/close/sl/sl_1_dress.png",(0,0), "images/sprites/close/sl/sl_1_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_1_body.png",(0,0), "images/sprites/close/sl/sl_1_dress.png",(0,0), "images/sprites/close/sl/sl_1_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_1_body.png",(0,0), "images/sprites/close/sl/sl_1_dress.png",(0,0), "images/sprites/close/sl/sl_1_serious.png") )
            image dv guilty pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_3_body.png",(0,0), "images/sprites/close/dv/dv_3_pioneer.png",(0,0), "images/sprites/close/dv/dv_3_guilty.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_3_body.png",(0,0), "images/sprites/close/dv/dv_3_pioneer.png",(0,0), "images/sprites/close/dv/dv_3_guilty.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_3_body.png",(0,0), "images/sprites/close/dv/dv_3_pioneer.png",(0,0), "images/sprites/close/dv/dv_3_guilty.png") )
            image mz normal pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_1_body.png",(0,0), "images/sprites/close/mz/mz_1_pioneer.png",(0,0), "images/sprites/close/mz/mz_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_1_body.png",(0,0), "images/sprites/close/mz/mz_1_pioneer.png",(0,0), "images/sprites/close/mz/mz_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_1_body.png",(0,0), "images/sprites/close/mz/mz_1_pioneer.png",(0,0), "images/sprites/close/mz/mz_1_normal.png") )
            image un cry_smile swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_swim.png",(0,0), "images/sprites/close/un/un_2_cry_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_swim.png",(0,0), "images/sprites/close/un/un_2_cry_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_swim.png",(0,0), "images/sprites/close/un/un_2_cry_smile.png") )
            image uv normal close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/uv/uv_2_body.png",(0,0), "images/sprites/close/uv/uv_2_pioneer.png",(0,0), "images/sprites/close/uv/uv_2_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/uv/uv_2_body.png",(0,0), "images/sprites/close/uv/uv_2_pioneer.png",(0,0), "images/sprites/close/uv/uv_2_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/uv/uv_2_body.png",(0,0), "images/sprites/close/uv/uv_2_pioneer.png",(0,0), "images/sprites/close/uv/uv_2_normal.png") )
            image us angry swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_swim.png",(0,0), "images/sprites/close/us/us_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_swim.png",(0,0), "images/sprites/close/us/us_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_swim.png",(0,0), "images/sprites/close/us/us_2_angry.png") )
            image mt normal swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_swim.png",(0,0), "images/sprites/close/mt/mt_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_swim.png",(0,0), "images/sprites/close/mt/mt_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_swim.png",(0,0), "images/sprites/close/mt/mt_1_normal.png") )
            image us dontlike pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_pioneer.png",(0,0), "images/sprites/close/us/us_2_dontlike.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_pioneer.png",(0,0), "images/sprites/close/us/us_2_dontlike.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_pioneer.png",(0,0), "images/sprites/close/us/us_2_dontlike.png") )
            image un normal sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_sport.png",(0,0), "images/sprites/close/un/un_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_sport.png",(0,0), "images/sprites/close/un/un_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_sport.png",(0,0), "images/sprites/close/un/un_1_normal.png") )
            image un grin sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_sport.png",(0,0), "images/sprites/close/un/un_3_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_sport.png",(0,0), "images/sprites/close/un/un_3_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_sport.png",(0,0), "images/sprites/close/un/un_3_grin.png") )
            image mi laugh pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_pioneer.png",(0,0), "images/sprites/close/mi/mi_1_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_pioneer.png",(0,0), "images/sprites/close/mi/mi_1_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_pioneer.png",(0,0), "images/sprites/close/mi/mi_1_laugh.png") )
            image un shocked sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_sport.png",(0,0), "images/sprites/close/un/un_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_sport.png",(0,0), "images/sprites/close/un/un_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_sport.png",(0,0), "images/sprites/close/un/un_2_shocked.png") )
            image us laugh2 dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_dress.png",(0,0), "images/sprites/close/us/us_1_laugh2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_dress.png",(0,0), "images/sprites/close/us/us_1_laugh2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_dress.png",(0,0), "images/sprites/close/us/us_1_laugh2.png") )
            image el laugh pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/el/el_3_body.png",(0,0), "images/sprites/close/el/el_3_pioneer.png",(0,0), "images/sprites/close/el/el_3_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/el/el_3_body.png",(0,0), "images/sprites/close/el/el_3_pioneer.png",(0,0), "images/sprites/close/el/el_3_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/el/el_3_body.png",(0,0), "images/sprites/close/el/el_3_pioneer.png",(0,0), "images/sprites/close/el/el_3_laugh.png") )
            image sl tender pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_4_body.png",(0,0), "images/sprites/close/sl/sl_4_pioneer.png",(0,0), "images/sprites/close/sl/sl_4_tender.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_4_body.png",(0,0), "images/sprites/close/sl/sl_4_pioneer.png",(0,0), "images/sprites/close/sl/sl_4_tender.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_4_body.png",(0,0), "images/sprites/close/sl/sl_4_pioneer.png",(0,0), "images/sprites/close/sl/sl_4_tender.png") )
            image sl smile pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_1_body.png",(0,0), "images/sprites/close/sl/sl_1_pioneer.png",(0,0), "images/sprites/close/sl/sl_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_1_body.png",(0,0), "images/sprites/close/sl/sl_1_pioneer.png",(0,0), "images/sprites/close/sl/sl_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_1_body.png",(0,0), "images/sprites/close/sl/sl_1_pioneer.png",(0,0), "images/sprites/close/sl/sl_1_smile.png") )
            image us angry pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_pioneer.png",(0,0), "images/sprites/close/us/us_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_pioneer.png",(0,0), "images/sprites/close/us/us_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_pioneer.png",(0,0), "images/sprites/close/us/us_2_angry.png") )
            image sh normal_smile pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_2_body.png",(0,0), "images/sprites/close/sh/sh_2_normal_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_2_body.png",(0,0), "images/sprites/close/sh/sh_2_normal_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_2_body.png",(0,0), "images/sprites/close/sh/sh_2_normal_smile.png") )
            image dv laugh pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_4_body.png",(0,0), "images/sprites/close/dv/dv_4_pioneer.png",(0,0), "images/sprites/close/dv/dv_4_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_4_body.png",(0,0), "images/sprites/close/dv/dv_4_pioneer.png",(0,0), "images/sprites/close/dv/dv_4_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_4_body.png",(0,0), "images/sprites/close/dv/dv_4_pioneer.png",(0,0), "images/sprites/close/dv/dv_4_laugh.png") )
            image us sad dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_dress.png",(0,0), "images/sprites/close/us/us_1_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_dress.png",(0,0), "images/sprites/close/us/us_1_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_dress.png",(0,0), "images/sprites/close/us/us_1_sad.png") )
            image mt rage panama swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_2_body.png",(0,0), "images/sprites/close/mt/mt_2_panama.png",(0,0), "images/sprites/close/mt/mt_2_rage.png",(0,0), "images/sprites/close/mt/mt_2_swim.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_2_body.png",(0,0), "images/sprites/close/mt/mt_2_panama.png",(0,0), "images/sprites/close/mt/mt_2_rage.png",(0,0), "images/sprites/close/mt/mt_2_swim.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_2_body.png",(0,0), "images/sprites/close/mt/mt_2_panama.png",(0,0), "images/sprites/close/mt/mt_2_rage.png",(0,0), "images/sprites/close/mt/mt_2_swim.png") )
            image un angry dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_dress.png",(0,0), "images/sprites/close/un/un_1_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_dress.png",(0,0), "images/sprites/close/un/un_1_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_dress.png",(0,0), "images/sprites/close/un/un_1_angry.png") )
            image un angry pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_pioneer.png",(0,0), "images/sprites/close/un/un_1_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_pioneer.png",(0,0), "images/sprites/close/un/un_1_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_pioneer.png",(0,0), "images/sprites/close/un/un_1_angry.png") )
            image cs normal close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/cs/cs_1_body.png",(0,0), "images/sprites/close/cs/cs_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/cs/cs_1_body.png",(0,0), "images/sprites/close/cs/cs_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/cs/cs_1_body.png",(0,0), "images/sprites/close/cs/cs_1_normal.png") )
            image us upset pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_pioneer.png",(0,0), "images/sprites/close/us/us_2_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_pioneer.png",(0,0), "images/sprites/close/us/us_2_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_pioneer.png",(0,0), "images/sprites/close/us/us_2_upset.png") )
            image us smile dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_dress.png",(0,0), "images/sprites/close/us/us_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_dress.png",(0,0), "images/sprites/close/us/us_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_dress.png",(0,0), "images/sprites/close/us/us_1_smile.png") )
            image dv shy pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_3_body.png",(0,0), "images/sprites/close/dv/dv_3_pioneer.png",(0,0), "images/sprites/close/dv/dv_3_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_3_body.png",(0,0), "images/sprites/close/dv/dv_3_pioneer.png",(0,0), "images/sprites/close/dv/dv_3_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_3_body.png",(0,0), "images/sprites/close/dv/dv_3_pioneer.png",(0,0), "images/sprites/close/dv/dv_3_shy.png") )
            image un smile3 sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_sport.png",(0,0), "images/sprites/close/un/un_3_smile3.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_sport.png",(0,0), "images/sprites/close/un/un_3_smile3.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_sport.png",(0,0), "images/sprites/close/un/un_3_smile3.png") )
            image un shy sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_sport.png",(0,0), "images/sprites/close/un/un_1_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_sport.png",(0,0), "images/sprites/close/un/un_1_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_sport.png",(0,0), "images/sprites/close/un/un_1_shy.png") )
            image cs smile glasses close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/cs/cs_1_body.png",(0,0), "images/sprites/close/cs/cs_1_glasses.png",(0,0), "images/sprites/close/cs/cs_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/cs/cs_1_body.png",(0,0), "images/sprites/close/cs/cs_1_glasses.png",(0,0), "images/sprites/close/cs/cs_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/cs/cs_1_body.png",(0,0), "images/sprites/close/cs/cs_1_glasses.png",(0,0), "images/sprites/close/cs/cs_1_smile.png") )
            image sl scared sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_4_body.png",(0,0), "images/sprites/close/sl/sl_4_sport.png",(0,0), "images/sprites/close/sl/sl_4_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_4_body.png",(0,0), "images/sprites/close/sl/sl_4_sport.png",(0,0), "images/sprites/close/sl/sl_4_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_4_body.png",(0,0), "images/sprites/close/sl/sl_4_sport.png",(0,0), "images/sprites/close/sl/sl_4_scared.png") )
            image dv shy pioneer2 close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_3_body.png",(0,0), "images/sprites/close/dv/dv_3_pioneer2.png",(0,0), "images/sprites/close/dv/dv_3_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_3_body.png",(0,0), "images/sprites/close/dv/dv_3_pioneer2.png",(0,0), "images/sprites/close/dv/dv_3_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_3_body.png",(0,0), "images/sprites/close/dv/dv_3_pioneer2.png",(0,0), "images/sprites/close/dv/dv_3_shy.png") )
            image us fear swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_swim.png",(0,0), "images/sprites/close/us/us_2_fear.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_swim.png",(0,0), "images/sprites/close/us/us_2_fear.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_swim.png",(0,0), "images/sprites/close/us/us_2_fear.png") )
            image sh smile close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_1_body.png",(0,0), "images/sprites/close/sh/sh_1_laugh.png",(0,0), "images/sprites/close/sh/sh_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_1_body.png",(0,0), "images/sprites/close/sh/sh_1_laugh.png",(0,0), "images/sprites/close/sh/sh_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_1_body.png",(0,0), "images/sprites/close/sh/sh_1_laugh.png",(0,0), "images/sprites/close/sh/sh_1_smile.png") )
            image us fear dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_dress.png",(0,0), "images/sprites/close/us/us_2_fear.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_dress.png",(0,0), "images/sprites/close/us/us_2_fear.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_dress.png",(0,0), "images/sprites/close/us/us_2_fear.png") )
            image mt sad pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_pioneer.png",(0,0), "images/sprites/close/mt/mt_1_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_pioneer.png",(0,0), "images/sprites/close/mt/mt_1_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_pioneer.png",(0,0), "images/sprites/close/mt/mt_1_sad.png") )
            image mt smile dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_dress.png",(0,0), "images/sprites/close/mt/mt_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_dress.png",(0,0), "images/sprites/close/mt/mt_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_dress.png",(0,0), "images/sprites/close/mt/mt_1_smile.png") )
            image un smile2 swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_swim.png",(0,0), "images/sprites/close/un/un_1_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_swim.png",(0,0), "images/sprites/close/un/un_1_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_swim.png",(0,0), "images/sprites/close/un/un_1_smile2.png") )
            image sh normal_smile close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_2_body.png",(0,0), "images/sprites/close/sh/sh_2_rage.png",(0,0), "images/sprites/close/sh/sh_2_normal_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_2_body.png",(0,0), "images/sprites/close/sh/sh_2_rage.png",(0,0), "images/sprites/close/sh/sh_2_normal_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_2_body.png",(0,0), "images/sprites/close/sh/sh_2_rage.png",(0,0), "images/sprites/close/sh/sh_2_normal_smile.png") )
            image sl tender swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_4_body.png",(0,0), "images/sprites/close/sl/sl_4_swim.png",(0,0), "images/sprites/close/sl/sl_4_tender.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_4_body.png",(0,0), "images/sprites/close/sl/sl_4_swim.png",(0,0), "images/sprites/close/sl/sl_4_tender.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_4_body.png",(0,0), "images/sprites/close/sl/sl_4_swim.png",(0,0), "images/sprites/close/sl/sl_4_tender.png") )
            image mt rage pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_2_body.png",(0,0), "images/sprites/close/mt/mt_2_pioneer.png",(0,0), "images/sprites/close/mt/mt_2_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_2_body.png",(0,0), "images/sprites/close/mt/mt_2_pioneer.png",(0,0), "images/sprites/close/mt/mt_2_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_2_body.png",(0,0), "images/sprites/close/mt/mt_2_pioneer.png",(0,0), "images/sprites/close/mt/mt_2_rage.png") )
            image mt angry panama pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_2_body.png",(0,0), "images/sprites/close/mt/mt_2_panama.png",(0,0), "images/sprites/close/mt/mt_2_angry.png",(0,0), "images/sprites/close/mt/mt_2_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_2_body.png",(0,0), "images/sprites/close/mt/mt_2_panama.png",(0,0), "images/sprites/close/mt/mt_2_angry.png",(0,0), "images/sprites/close/mt/mt_2_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_2_body.png",(0,0), "images/sprites/close/mt/mt_2_panama.png",(0,0), "images/sprites/close/mt/mt_2_angry.png",(0,0), "images/sprites/close/mt/mt_2_pioneer.png") )
            image un smile2 pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_pioneer.png",(0,0), "images/sprites/close/un/un_1_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_pioneer.png",(0,0), "images/sprites/close/un/un_1_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_pioneer.png",(0,0), "images/sprites/close/un/un_1_smile2.png") )
            image el normal pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/el/el_1_body.png",(0,0), "images/sprites/close/el/el_1_pioneer.png",(0,0), "images/sprites/close/el/el_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/el/el_1_body.png",(0,0), "images/sprites/close/el/el_1_pioneer.png",(0,0), "images/sprites/close/el/el_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/el/el_1_body.png",(0,0), "images/sprites/close/el/el_1_pioneer.png",(0,0), "images/sprites/close/el/el_1_normal.png") )
            image mt smile panama dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_panama.png",(0,0), "images/sprites/close/mt/mt_1_smile.png",(0,0), "images/sprites/close/mt/mt_1_dress.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_panama.png",(0,0), "images/sprites/close/mt/mt_1_smile.png",(0,0), "images/sprites/close/mt/mt_1_dress.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_panama.png",(0,0), "images/sprites/close/mt/mt_1_smile.png",(0,0), "images/sprites/close/mt/mt_1_dress.png") )
            image sl laugh sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_sport.png",(0,0), "images/sprites/close/sl/sl_2_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_sport.png",(0,0), "images/sprites/close/sl/sl_2_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_sport.png",(0,0), "images/sprites/close/sl/sl_2_laugh.png") )
            image us upset sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_sport.png",(0,0), "images/sprites/close/us/us_2_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_sport.png",(0,0), "images/sprites/close/us/us_2_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_sport.png",(0,0), "images/sprites/close/us/us_2_upset.png") )
            image mt normal pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_pioneer.png",(0,0), "images/sprites/close/mt/mt_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_pioneer.png",(0,0), "images/sprites/close/mt/mt_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_pioneer.png",(0,0), "images/sprites/close/mt/mt_1_normal.png") )
            image us cry2 swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_swim.png",(0,0), "images/sprites/close/us/us_3_cry2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_swim.png",(0,0), "images/sprites/close/us/us_3_cry2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_swim.png",(0,0), "images/sprites/close/us/us_3_cry2.png") )
            image mt surprise swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_swim.png",(0,0), "images/sprites/close/mt/mt_1_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_swim.png",(0,0), "images/sprites/close/mt/mt_1_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_swim.png",(0,0), "images/sprites/close/mt/mt_1_surprise.png") )
            image sl smile dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_1_body.png",(0,0), "images/sprites/close/sl/sl_1_dress.png",(0,0), "images/sprites/close/sl/sl_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_1_body.png",(0,0), "images/sprites/close/sl/sl_1_dress.png",(0,0), "images/sprites/close/sl/sl_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_1_body.png",(0,0), "images/sprites/close/sl/sl_1_dress.png",(0,0), "images/sprites/close/sl/sl_1_smile.png") )
            image us upset swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_swim.png",(0,0), "images/sprites/close/us/us_2_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_swim.png",(0,0), "images/sprites/close/us/us_2_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_swim.png",(0,0), "images/sprites/close/us/us_2_upset.png") )
            image un smile sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_sport.png",(0,0), "images/sprites/close/un/un_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_sport.png",(0,0), "images/sprites/close/un/un_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_sport.png",(0,0), "images/sprites/close/un/un_1_smile.png") )
            image un smile pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_pioneer.png",(0,0), "images/sprites/close/un/un_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_pioneer.png",(0,0), "images/sprites/close/un/un_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_pioneer.png",(0,0), "images/sprites/close/un/un_1_smile.png") )
            image us upset dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_dress.png",(0,0), "images/sprites/close/us/us_2_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_dress.png",(0,0), "images/sprites/close/us/us_2_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_dress.png",(0,0), "images/sprites/close/us/us_2_upset.png") )
            image us laugh pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_pioneer.png",(0,0), "images/sprites/close/us/us_1_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_pioneer.png",(0,0), "images/sprites/close/us/us_1_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_pioneer.png",(0,0), "images/sprites/close/us/us_1_laugh.png") )
            image un rage sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_sport.png",(0,0), "images/sprites/close/un/un_3_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_sport.png",(0,0), "images/sprites/close/un/un_3_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_sport.png",(0,0), "images/sprites/close/un/un_3_rage.png") )
            image sl scared pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_4_body.png",(0,0), "images/sprites/close/sl/sl_4_pioneer.png",(0,0), "images/sprites/close/sl/sl_4_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_4_body.png",(0,0), "images/sprites/close/sl/sl_4_pioneer.png",(0,0), "images/sprites/close/sl/sl_4_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_4_body.png",(0,0), "images/sprites/close/sl/sl_4_pioneer.png",(0,0), "images/sprites/close/sl/sl_4_scared.png") )
            image us shy2 sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_sport.png",(0,0), "images/sprites/close/us/us_3_shy2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_sport.png",(0,0), "images/sprites/close/us/us_3_shy2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_sport.png",(0,0), "images/sprites/close/us/us_3_shy2.png") )
            image sl surprise sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_sport.png",(0,0), "images/sprites/close/sl/sl_3_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_sport.png",(0,0), "images/sprites/close/sl/sl_3_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_sport.png",(0,0), "images/sprites/close/sl/sl_3_surprise.png") )
            image us surp1 swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_swim.png",(0,0), "images/sprites/close/us/us_3_surp1.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_swim.png",(0,0), "images/sprites/close/us/us_3_surp1.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_swim.png",(0,0), "images/sprites/close/us/us_3_surp1.png") )
            image mt angry dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_2_body.png",(0,0), "images/sprites/close/mt/mt_2_dress.png",(0,0), "images/sprites/close/mt/mt_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_2_body.png",(0,0), "images/sprites/close/mt/mt_2_dress.png",(0,0), "images/sprites/close/mt/mt_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_2_body.png",(0,0), "images/sprites/close/mt/mt_2_dress.png",(0,0), "images/sprites/close/mt/mt_2_angry.png") )
            image uv upset close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/uv/uv_4_body.png",(0,0), "images/sprites/close/uv/uv_4_pioneer.png",(0,0), "images/sprites/close/uv/uv_4_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/uv/uv_4_body.png",(0,0), "images/sprites/close/uv/uv_4_pioneer.png",(0,0), "images/sprites/close/uv/uv_4_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/uv/uv_4_body.png",(0,0), "images/sprites/close/uv/uv_4_pioneer.png",(0,0), "images/sprites/close/uv/uv_4_upset.png") )
            image sh serious close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_3_body.png",(0,0), "images/sprites/close/sh/sh_3_normal.png",(0,0), "images/sprites/close/sh/sh_3_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_3_body.png",(0,0), "images/sprites/close/sh/sh_3_normal.png",(0,0), "images/sprites/close/sh/sh_3_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_3_body.png",(0,0), "images/sprites/close/sh/sh_3_normal.png",(0,0), "images/sprites/close/sh/sh_3_serious.png") )
            image uv guilty close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/uv/uv_4_body.png",(0,0), "images/sprites/close/uv/uv_4_pioneer.png",(0,0), "images/sprites/close/uv/uv_4_guilty.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/uv/uv_4_body.png",(0,0), "images/sprites/close/uv/uv_4_pioneer.png",(0,0), "images/sprites/close/uv/uv_4_guilty.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/uv/uv_4_body.png",(0,0), "images/sprites/close/uv/uv_4_pioneer.png",(0,0), "images/sprites/close/uv/uv_4_guilty.png") )
            image us calml swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_swim.png",(0,0), "images/sprites/close/us/us_2_calml.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_swim.png",(0,0), "images/sprites/close/us/us_2_calml.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_swim.png",(0,0), "images/sprites/close/us/us_2_calml.png") )
            image us shy2 swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_swim.png",(0,0), "images/sprites/close/us/us_3_shy2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_swim.png",(0,0), "images/sprites/close/us/us_3_shy2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_swim.png",(0,0), "images/sprites/close/us/us_3_shy2.png") )
            image us dontlike dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_dress.png",(0,0), "images/sprites/close/us/us_2_dontlike.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_dress.png",(0,0), "images/sprites/close/us/us_2_dontlike.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_dress.png",(0,0), "images/sprites/close/us/us_2_dontlike.png") )
            image mi smile pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_2_body.png",(0,0), "images/sprites/close/mi/mi_2_pioneer.png",(0,0), "images/sprites/close/mi/mi_2_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_2_body.png",(0,0), "images/sprites/close/mi/mi_2_pioneer.png",(0,0), "images/sprites/close/mi/mi_2_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_2_body.png",(0,0), "images/sprites/close/mi/mi_2_pioneer.png",(0,0), "images/sprites/close/mi/mi_2_smile.png") )
            image us dontlike sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_sport.png",(0,0), "images/sprites/close/us/us_2_dontlike.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_sport.png",(0,0), "images/sprites/close/us/us_2_dontlike.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_sport.png",(0,0), "images/sprites/close/us/us_2_dontlike.png") )
            image un normal pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_pioneer.png",(0,0), "images/sprites/close/un/un_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_pioneer.png",(0,0), "images/sprites/close/un/un_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_pioneer.png",(0,0), "images/sprites/close/un/un_1_normal.png") )
            image us cry pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_pioneer.png",(0,0), "images/sprites/close/us/us_3_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_pioneer.png",(0,0), "images/sprites/close/us/us_3_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_pioneer.png",(0,0), "images/sprites/close/us/us_3_cry.png") )
            image un shy swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_swim.png",(0,0), "images/sprites/close/un/un_1_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_swim.png",(0,0), "images/sprites/close/un/un_1_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_swim.png",(0,0), "images/sprites/close/un/un_1_shy.png") )
            image sl smile2 pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_pioneer.png",(0,0), "images/sprites/close/sl/sl_2_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_pioneer.png",(0,0), "images/sprites/close/sl/sl_2_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_pioneer.png",(0,0), "images/sprites/close/sl/sl_2_smile2.png") )
            image mi cry_smile pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_2_body.png",(0,0), "images/sprites/close/mi/mi_2_pioneer.png",(0,0), "images/sprites/close/mi/mi_2_cry_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_2_body.png",(0,0), "images/sprites/close/mi/mi_2_pioneer.png",(0,0), "images/sprites/close/mi/mi_2_cry_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_2_body.png",(0,0), "images/sprites/close/mi/mi_2_pioneer.png",(0,0), "images/sprites/close/mi/mi_2_cry_smile.png") )
            image un normal swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_swim.png",(0,0), "images/sprites/close/un/un_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_swim.png",(0,0), "images/sprites/close/un/un_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_swim.png",(0,0), "images/sprites/close/un/un_1_normal.png") )
            image dv normal swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_4_body.png",(0,0), "images/sprites/close/dv/dv_4_swim.png",(0,0), "images/sprites/close/dv/dv_4_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_4_body.png",(0,0), "images/sprites/close/dv/dv_4_swim.png",(0,0), "images/sprites/close/dv/dv_4_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_4_body.png",(0,0), "images/sprites/close/dv/dv_4_swim.png",(0,0), "images/sprites/close/dv/dv_4_normal.png") )
            image un scared pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_pioneer.png",(0,0), "images/sprites/close/un/un_2_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_pioneer.png",(0,0), "images/sprites/close/un/un_2_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_pioneer.png",(0,0), "images/sprites/close/un/un_2_scared.png") )
            image dv smile pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_4_body.png",(0,0), "images/sprites/close/dv/dv_4_pioneer.png",(0,0), "images/sprites/close/dv/dv_4_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_4_body.png",(0,0), "images/sprites/close/dv/dv_4_pioneer.png",(0,0), "images/sprites/close/dv/dv_4_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_4_body.png",(0,0), "images/sprites/close/dv/dv_4_pioneer.png",(0,0), "images/sprites/close/dv/dv_4_smile.png") )
            image us shy swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_swim.png",(0,0), "images/sprites/close/us/us_3_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_swim.png",(0,0), "images/sprites/close/us/us_3_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_swim.png",(0,0), "images/sprites/close/us/us_3_shy.png") )
            image cs shy glasses close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/cs/cs_1_body.png",(0,0), "images/sprites/close/cs/cs_1_glasses.png",(0,0), "images/sprites/close/cs/cs_1_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/cs/cs_1_body.png",(0,0), "images/sprites/close/cs/cs_1_glasses.png",(0,0), "images/sprites/close/cs/cs_1_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/cs/cs_1_body.png",(0,0), "images/sprites/close/cs/cs_1_glasses.png",(0,0), "images/sprites/close/cs/cs_1_shy.png") )
            image cs smile stethoscope close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/cs/cs_1_body.png",(0,0), "images/sprites/close/cs/cs_1_stethoscope.png",(0,0), "images/sprites/close/cs/cs_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/cs/cs_1_body.png",(0,0), "images/sprites/close/cs/cs_1_stethoscope.png",(0,0), "images/sprites/close/cs/cs_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/cs/cs_1_body.png",(0,0), "images/sprites/close/cs/cs_1_stethoscope.png",(0,0), "images/sprites/close/cs/cs_1_smile.png") )
            image us grin swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_swim.png",(0,0), "images/sprites/close/us/us_1_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_swim.png",(0,0), "images/sprites/close/us/us_1_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_swim.png",(0,0), "images/sprites/close/us/us_1_grin.png") )
            image sl normal dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_1_body.png",(0,0), "images/sprites/close/sl/sl_1_dress.png",(0,0), "images/sprites/close/sl/sl_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_1_body.png",(0,0), "images/sprites/close/sl/sl_1_dress.png",(0,0), "images/sprites/close/sl/sl_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_1_body.png",(0,0), "images/sprites/close/sl/sl_1_dress.png",(0,0), "images/sprites/close/sl/sl_1_normal.png") )
            image mi cry pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_pioneer.png",(0,0), "images/sprites/close/mi/mi_1_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_pioneer.png",(0,0), "images/sprites/close/mi/mi_1_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_pioneer.png",(0,0), "images/sprites/close/mi/mi_1_cry.png") )
            image mt grin pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_3_body.png",(0,0), "images/sprites/close/mt/mt_3_pioneer.png",(0,0), "images/sprites/close/mt/mt_3_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_3_body.png",(0,0), "images/sprites/close/mt/mt_3_pioneer.png",(0,0), "images/sprites/close/mt/mt_3_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_3_body.png",(0,0), "images/sprites/close/mt/mt_3_pioneer.png",(0,0), "images/sprites/close/mt/mt_3_grin.png") )
            image mt surprise pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_pioneer.png",(0,0), "images/sprites/close/mt/mt_1_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_pioneer.png",(0,0), "images/sprites/close/mt/mt_1_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_pioneer.png",(0,0), "images/sprites/close/mt/mt_1_surprise.png") )
            image dv smile swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_4_body.png",(0,0), "images/sprites/close/dv/dv_4_swim.png",(0,0), "images/sprites/close/dv/dv_4_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_4_body.png",(0,0), "images/sprites/close/dv/dv_4_swim.png",(0,0), "images/sprites/close/dv/dv_4_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_4_body.png",(0,0), "images/sprites/close/dv/dv_4_swim.png",(0,0), "images/sprites/close/dv/dv_4_smile.png") )
            image un laugh dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_dress.png",(0,0), "images/sprites/close/un/un_3_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_dress.png",(0,0), "images/sprites/close/un/un_3_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_dress.png",(0,0), "images/sprites/close/un/un_3_laugh.png") )
            image sl serious pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_1_body.png",(0,0), "images/sprites/close/sl/sl_1_pioneer.png",(0,0), "images/sprites/close/sl/sl_1_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_1_body.png",(0,0), "images/sprites/close/sl/sl_1_pioneer.png",(0,0), "images/sprites/close/sl/sl_1_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_1_body.png",(0,0), "images/sprites/close/sl/sl_1_pioneer.png",(0,0), "images/sprites/close/sl/sl_1_serious.png") )
            image us smile sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_sport.png",(0,0), "images/sprites/close/us/us_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_sport.png",(0,0), "images/sprites/close/us/us_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_sport.png",(0,0), "images/sprites/close/us/us_1_smile.png") )
            image sh serious pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_3_body.png",(0,0), "images/sprites/close/sh/sh_3_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_3_body.png",(0,0), "images/sprites/close/sh/sh_3_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_3_body.png",(0,0), "images/sprites/close/sh/sh_3_serious.png") )
            image un serious sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_sport.png",(0,0), "images/sprites/close/un/un_3_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_sport.png",(0,0), "images/sprites/close/un/un_3_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_sport.png",(0,0), "images/sprites/close/un/un_3_serious.png") )
            image mt normal panama pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_panama.png",(0,0), "images/sprites/close/mt/mt_1_normal.png",(0,0), "images/sprites/close/mt/mt_1_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_panama.png",(0,0), "images/sprites/close/mt/mt_1_normal.png",(0,0), "images/sprites/close/mt/mt_1_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_panama.png",(0,0), "images/sprites/close/mt/mt_1_normal.png",(0,0), "images/sprites/close/mt/mt_1_pioneer.png") )
            image mt sad panama dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_panama.png",(0,0), "images/sprites/close/mt/mt_1_sad.png",(0,0), "images/sprites/close/mt/mt_1_dress.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_panama.png",(0,0), "images/sprites/close/mt/mt_1_sad.png",(0,0), "images/sprites/close/mt/mt_1_dress.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_panama.png",(0,0), "images/sprites/close/mt/mt_1_sad.png",(0,0), "images/sprites/close/mt/mt_1_dress.png") )
            image sl angry dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_dress.png",(0,0), "images/sprites/close/sl/sl_3_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_dress.png",(0,0), "images/sprites/close/sl/sl_3_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_dress.png",(0,0), "images/sprites/close/sl/sl_3_angry.png") )
            image sl surprise dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_dress.png",(0,0), "images/sprites/close/sl/sl_3_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_dress.png",(0,0), "images/sprites/close/sl/sl_3_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_dress.png",(0,0), "images/sprites/close/sl/sl_3_surprise.png") )
            image dv shocked pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_pioneer.png",(0,0), "images/sprites/close/dv/dv_1_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_pioneer.png",(0,0), "images/sprites/close/dv/dv_1_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_pioneer.png",(0,0), "images/sprites/close/dv/dv_1_shocked.png") )
            image us surp2 swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_swim.png",(0,0), "images/sprites/close/us/us_3_surp2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_swim.png",(0,0), "images/sprites/close/us/us_3_surp2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_swim.png",(0,0), "images/sprites/close/us/us_3_surp2.png") )
            image sl tender sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_4_body.png",(0,0), "images/sprites/close/sl/sl_4_sport.png",(0,0), "images/sprites/close/sl/sl_4_tender.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_4_body.png",(0,0), "images/sprites/close/sl/sl_4_sport.png",(0,0), "images/sprites/close/sl/sl_4_tender.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_4_body.png",(0,0), "images/sprites/close/sl/sl_4_sport.png",(0,0), "images/sprites/close/sl/sl_4_tender.png") )
            image sl surprise pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_pioneer.png",(0,0), "images/sprites/close/sl/sl_3_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_pioneer.png",(0,0), "images/sprites/close/sl/sl_3_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_pioneer.png",(0,0), "images/sprites/close/sl/sl_3_surprise.png") )
            image us grin sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_sport.png",(0,0), "images/sprites/close/us/us_1_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_sport.png",(0,0), "images/sprites/close/us/us_1_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_sport.png",(0,0), "images/sprites/close/us/us_1_grin.png") )
            image us laugh2 swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_swim.png",(0,0), "images/sprites/close/us/us_1_laugh2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_swim.png",(0,0), "images/sprites/close/us/us_1_laugh2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_swim.png",(0,0), "images/sprites/close/us/us_1_laugh2.png") )
            image dv guilty pioneer2 close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_3_body.png",(0,0), "images/sprites/close/dv/dv_3_pioneer2.png",(0,0), "images/sprites/close/dv/dv_3_guilty.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_3_body.png",(0,0), "images/sprites/close/dv/dv_3_pioneer2.png",(0,0), "images/sprites/close/dv/dv_3_guilty.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_3_body.png",(0,0), "images/sprites/close/dv/dv_3_pioneer2.png",(0,0), "images/sprites/close/dv/dv_3_guilty.png") )
            image sl smile2 swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_swim.png",(0,0), "images/sprites/close/sl/sl_2_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_swim.png",(0,0), "images/sprites/close/sl/sl_2_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_swim.png",(0,0), "images/sprites/close/sl/sl_2_smile2.png") )
            image mi normal swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_3_body.png",(0,0), "images/sprites/close/mi/mi_3_swim.png",(0,0), "images/sprites/close/mi/mi_3_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_3_body.png",(0,0), "images/sprites/close/mi/mi_3_swim.png",(0,0), "images/sprites/close/mi/mi_3_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_3_body.png",(0,0), "images/sprites/close/mi/mi_3_swim.png",(0,0), "images/sprites/close/mi/mi_3_normal.png") )
            image sl normal sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_1_body.png",(0,0), "images/sprites/close/sl/sl_1_sport.png",(0,0), "images/sprites/close/sl/sl_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_1_body.png",(0,0), "images/sprites/close/sl/sl_1_sport.png",(0,0), "images/sprites/close/sl/sl_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_1_body.png",(0,0), "images/sprites/close/sl/sl_1_sport.png",(0,0), "images/sprites/close/sl/sl_1_normal.png") )
            image mi sad pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_2_body.png",(0,0), "images/sprites/close/mi/mi_2_pioneer.png",(0,0), "images/sprites/close/mi/mi_2_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_2_body.png",(0,0), "images/sprites/close/mi/mi_2_pioneer.png",(0,0), "images/sprites/close/mi/mi_2_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_2_body.png",(0,0), "images/sprites/close/mi/mi_2_pioneer.png",(0,0), "images/sprites/close/mi/mi_2_sad.png") )
            image un smile3 pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_pioneer.png",(0,0), "images/sprites/close/un/un_3_smile3.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_pioneer.png",(0,0), "images/sprites/close/un/un_3_smile3.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_pioneer.png",(0,0), "images/sprites/close/un/un_3_smile3.png") )
            image sl smile2 dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_dress.png",(0,0), "images/sprites/close/sl/sl_2_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_dress.png",(0,0), "images/sprites/close/sl/sl_2_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_dress.png",(0,0), "images/sprites/close/sl/sl_2_smile2.png") )
            image us smile swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_swim.png",(0,0), "images/sprites/close/us/us_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_swim.png",(0,0), "images/sprites/close/us/us_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_swim.png",(0,0), "images/sprites/close/us/us_1_smile.png") )
            image mt rage panama dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_2_body.png",(0,0), "images/sprites/close/mt/mt_2_panama.png",(0,0), "images/sprites/close/mt/mt_2_rage.png",(0,0), "images/sprites/close/mt/mt_2_dress.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_2_body.png",(0,0), "images/sprites/close/mt/mt_2_panama.png",(0,0), "images/sprites/close/mt/mt_2_rage.png",(0,0), "images/sprites/close/mt/mt_2_dress.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_2_body.png",(0,0), "images/sprites/close/mt/mt_2_panama.png",(0,0), "images/sprites/close/mt/mt_2_rage.png",(0,0), "images/sprites/close/mt/mt_2_dress.png") )
            image dv surprise pioneer2 close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_pioneer2.png",(0,0), "images/sprites/close/dv/dv_1_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_pioneer2.png",(0,0), "images/sprites/close/dv/dv_1_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_pioneer2.png",(0,0), "images/sprites/close/dv/dv_1_surprise.png") )
            image us cry2 sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_sport.png",(0,0), "images/sprites/close/us/us_3_cry2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_sport.png",(0,0), "images/sprites/close/us/us_3_cry2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_sport.png",(0,0), "images/sprites/close/us/us_3_cry2.png") )
            image un normal dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_dress.png",(0,0), "images/sprites/close/un/un_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_dress.png",(0,0), "images/sprites/close/un/un_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_dress.png",(0,0), "images/sprites/close/un/un_1_normal.png") )
            image mi smile swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_2_body.png",(0,0), "images/sprites/close/mi/mi_2_swim.png",(0,0), "images/sprites/close/mi/mi_2_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_2_body.png",(0,0), "images/sprites/close/mi/mi_2_swim.png",(0,0), "images/sprites/close/mi/mi_2_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_2_body.png",(0,0), "images/sprites/close/mi/mi_2_swim.png",(0,0), "images/sprites/close/mi/mi_2_smile.png") )
            image cs normal glasses close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/cs/cs_1_body.png",(0,0), "images/sprites/close/cs/cs_1_glasses.png",(0,0), "images/sprites/close/cs/cs_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/cs/cs_1_body.png",(0,0), "images/sprites/close/cs/cs_1_glasses.png",(0,0), "images/sprites/close/cs/cs_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/cs/cs_1_body.png",(0,0), "images/sprites/close/cs/cs_1_glasses.png",(0,0), "images/sprites/close/cs/cs_1_normal.png") )
            image uv rage close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/uv/uv_1_body.png",(0,0), "images/sprites/close/uv/uv_1_pioneer.png",(0,0), "images/sprites/close/uv/uv_1_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/uv/uv_1_body.png",(0,0), "images/sprites/close/uv/uv_1_pioneer.png",(0,0), "images/sprites/close/uv/uv_1_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/uv/uv_1_body.png",(0,0), "images/sprites/close/uv/uv_1_pioneer.png",(0,0), "images/sprites/close/uv/uv_1_rage.png") )
            image sl sad dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_dress.png",(0,0), "images/sprites/close/sl/sl_3_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_dress.png",(0,0), "images/sprites/close/sl/sl_3_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_dress.png",(0,0), "images/sprites/close/sl/sl_3_sad.png") )
            image mt rage swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_2_body.png",(0,0), "images/sprites/close/mt/mt_2_swim.png",(0,0), "images/sprites/close/mt/mt_2_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_2_body.png",(0,0), "images/sprites/close/mt/mt_2_swim.png",(0,0), "images/sprites/close/mt/mt_2_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_2_body.png",(0,0), "images/sprites/close/mt/mt_2_swim.png",(0,0), "images/sprites/close/mt/mt_2_rage.png") )
            image dv rage pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_5_body.png",(0,0), "images/sprites/close/dv/dv_5_pioneer.png",(0,0), "images/sprites/close/dv/dv_5_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_5_body.png",(0,0), "images/sprites/close/dv/dv_5_pioneer.png",(0,0), "images/sprites/close/dv/dv_5_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_5_body.png",(0,0), "images/sprites/close/dv/dv_5_pioneer.png",(0,0), "images/sprites/close/dv/dv_5_rage.png") )
            image el surprise pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/el/el_2_body.png",(0,0), "images/sprites/close/el/el_2_pioneer.png",(0,0), "images/sprites/close/el/el_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/el/el_2_body.png",(0,0), "images/sprites/close/el/el_2_pioneer.png",(0,0), "images/sprites/close/el/el_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/el/el_2_body.png",(0,0), "images/sprites/close/el/el_2_pioneer.png",(0,0), "images/sprites/close/el/el_2_surprise.png") )
            image un cry pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_pioneer.png",(0,0), "images/sprites/close/un/un_2_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_pioneer.png",(0,0), "images/sprites/close/un/un_2_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_pioneer.png",(0,0), "images/sprites/close/un/un_2_cry.png") )
            image mi dontlike pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_pioneer.png",(0,0), "images/sprites/close/mi/mi_1_dontlike.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_pioneer.png",(0,0), "images/sprites/close/mi/mi_1_dontlike.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_pioneer.png",(0,0), "images/sprites/close/mi/mi_1_dontlike.png") )
            image sl shy swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_swim.png",(0,0), "images/sprites/close/sl/sl_2_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_swim.png",(0,0), "images/sprites/close/sl/sl_2_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_swim.png",(0,0), "images/sprites/close/sl/sl_2_shy.png") )
            image el serious pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/el/el_3_body.png",(0,0), "images/sprites/close/el/el_3_pioneer.png",(0,0), "images/sprites/close/el/el_3_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/el/el_3_body.png",(0,0), "images/sprites/close/el/el_3_pioneer.png",(0,0), "images/sprites/close/el/el_3_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/el/el_3_body.png",(0,0), "images/sprites/close/el/el_3_pioneer.png",(0,0), "images/sprites/close/el/el_3_serious.png") )
            image un scared swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_swim.png",(0,0), "images/sprites/close/un/un_2_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_swim.png",(0,0), "images/sprites/close/un/un_2_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_swim.png",(0,0), "images/sprites/close/un/un_2_scared.png") )
            image el scared pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/el/el_2_body.png",(0,0), "images/sprites/close/el/el_2_pioneer.png",(0,0), "images/sprites/close/el/el_2_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/el/el_2_body.png",(0,0), "images/sprites/close/el/el_2_pioneer.png",(0,0), "images/sprites/close/el/el_2_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/el/el_2_body.png",(0,0), "images/sprites/close/el/el_2_pioneer.png",(0,0), "images/sprites/close/el/el_2_scared.png") )
            image mi cry swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_swim.png",(0,0), "images/sprites/close/mi/mi_1_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_swim.png",(0,0), "images/sprites/close/mi/mi_1_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_swim.png",(0,0), "images/sprites/close/mi/mi_1_cry.png") )
            image mz smile pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_3_body.png",(0,0), "images/sprites/close/mz/mz_3_pioneer.png",(0,0), "images/sprites/close/mz/mz_3_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_3_body.png",(0,0), "images/sprites/close/mz/mz_3_pioneer.png",(0,0), "images/sprites/close/mz/mz_3_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_3_body.png",(0,0), "images/sprites/close/mz/mz_3_pioneer.png",(0,0), "images/sprites/close/mz/mz_3_smile.png") )
            image us laugh sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_sport.png",(0,0), "images/sprites/close/us/us_1_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_sport.png",(0,0), "images/sprites/close/us/us_1_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_sport.png",(0,0), "images/sprites/close/us/us_1_laugh.png") )
            image mt surprise dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_dress.png",(0,0), "images/sprites/close/mt/mt_1_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_dress.png",(0,0), "images/sprites/close/mt/mt_1_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_dress.png",(0,0), "images/sprites/close/mt/mt_1_surprise.png") )
            image mt sad panama swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_panama.png",(0,0), "images/sprites/close/mt/mt_1_sad.png",(0,0), "images/sprites/close/mt/mt_1_swim.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_panama.png",(0,0), "images/sprites/close/mt/mt_1_sad.png",(0,0), "images/sprites/close/mt/mt_1_swim.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_panama.png",(0,0), "images/sprites/close/mt/mt_1_sad.png",(0,0), "images/sprites/close/mt/mt_1_swim.png") )
            image sh upset close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_1_body.png",(0,0), "images/sprites/close/sh/sh_1_laugh.png",(0,0), "images/sprites/close/sh/sh_1_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_1_body.png",(0,0), "images/sprites/close/sh/sh_1_laugh.png",(0,0), "images/sprites/close/sh/sh_1_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_1_body.png",(0,0), "images/sprites/close/sh/sh_1_laugh.png",(0,0), "images/sprites/close/sh/sh_1_upset.png") )
            image un evil_smile sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_sport.png",(0,0), "images/sprites/close/un/un_1_evil_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_sport.png",(0,0), "images/sprites/close/un/un_1_evil_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_sport.png",(0,0), "images/sprites/close/un/un_1_evil_smile.png") )
            image uv surprise close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/uv/uv_4_body.png",(0,0), "images/sprites/close/uv/uv_4_pioneer.png",(0,0), "images/sprites/close/uv/uv_4_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/uv/uv_4_body.png",(0,0), "images/sprites/close/uv/uv_4_pioneer.png",(0,0), "images/sprites/close/uv/uv_4_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/uv/uv_4_body.png",(0,0), "images/sprites/close/uv/uv_4_pioneer.png",(0,0), "images/sprites/close/uv/uv_4_surprise.png") )
            image el grin pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/el/el_1_body.png",(0,0), "images/sprites/close/el/el_1_pioneer.png",(0,0), "images/sprites/close/el/el_1_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/el/el_1_body.png",(0,0), "images/sprites/close/el/el_1_pioneer.png",(0,0), "images/sprites/close/el/el_1_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/el/el_1_body.png",(0,0), "images/sprites/close/el/el_1_pioneer.png",(0,0), "images/sprites/close/el/el_1_grin.png") )
            image mt smile swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_swim.png",(0,0), "images/sprites/close/mt/mt_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_swim.png",(0,0), "images/sprites/close/mt/mt_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_swim.png",(0,0), "images/sprites/close/mt/mt_1_smile.png") )
            image us shy sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_sport.png",(0,0), "images/sprites/close/us/us_3_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_sport.png",(0,0), "images/sprites/close/us/us_3_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_sport.png",(0,0), "images/sprites/close/us/us_3_shy.png") )
            image us fear sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_sport.png",(0,0), "images/sprites/close/us/us_2_fear.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_sport.png",(0,0), "images/sprites/close/us/us_2_fear.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_sport.png",(0,0), "images/sprites/close/us/us_2_fear.png") )
            image un evil_smile pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_pioneer.png",(0,0), "images/sprites/close/un/un_1_evil_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_pioneer.png",(0,0), "images/sprites/close/un/un_1_evil_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_pioneer.png",(0,0), "images/sprites/close/un/un_1_evil_smile.png") )
            image us laugh2 pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_pioneer.png",(0,0), "images/sprites/close/us/us_1_laugh2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_pioneer.png",(0,0), "images/sprites/close/us/us_1_laugh2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_pioneer.png",(0,0), "images/sprites/close/us/us_1_laugh2.png") )
            image sl shy pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_pioneer.png",(0,0), "images/sprites/close/sl/sl_2_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_pioneer.png",(0,0), "images/sprites/close/sl/sl_2_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_pioneer.png",(0,0), "images/sprites/close/sl/sl_2_shy.png") )
            image us surp3 pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_pioneer.png",(0,0), "images/sprites/close/us/us_3_surp3.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_pioneer.png",(0,0), "images/sprites/close/us/us_3_surp3.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_pioneer.png",(0,0), "images/sprites/close/us/us_3_surp3.png") )
            image mi laugh swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_swim.png",(0,0), "images/sprites/close/mi/mi_1_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_swim.png",(0,0), "images/sprites/close/mi/mi_1_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_swim.png",(0,0), "images/sprites/close/mi/mi_1_laugh.png") )
            image un smile3 dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_dress.png",(0,0), "images/sprites/close/un/un_3_smile3.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_dress.png",(0,0), "images/sprites/close/un/un_3_smile3.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_dress.png",(0,0), "images/sprites/close/un/un_3_smile3.png") )
            image us surp3 swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_swim.png",(0,0), "images/sprites/close/us/us_3_surp3.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_swim.png",(0,0), "images/sprites/close/us/us_3_surp3.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_swim.png",(0,0), "images/sprites/close/us/us_3_surp3.png") )
            image un grin pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_pioneer.png",(0,0), "images/sprites/close/un/un_3_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_pioneer.png",(0,0), "images/sprites/close/un/un_3_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_pioneer.png",(0,0), "images/sprites/close/un/un_3_grin.png") )
            image mt laugh panama pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_3_body.png",(0,0), "images/sprites/close/mt/mt_3_panama.png",(0,0), "images/sprites/close/mt/mt_3_laugh.png",(0,0), "images/sprites/close/mt/mt_3_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_3_body.png",(0,0), "images/sprites/close/mt/mt_3_panama.png",(0,0), "images/sprites/close/mt/mt_3_laugh.png",(0,0), "images/sprites/close/mt/mt_3_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_3_body.png",(0,0), "images/sprites/close/mt/mt_3_panama.png",(0,0), "images/sprites/close/mt/mt_3_laugh.png",(0,0), "images/sprites/close/mt/mt_3_pioneer.png") )
            image sl shy dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_dress.png",(0,0), "images/sprites/close/sl/sl_2_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_dress.png",(0,0), "images/sprites/close/sl/sl_2_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_dress.png",(0,0), "images/sprites/close/sl/sl_2_shy.png") )
            image el sad pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/el/el_2_body.png",(0,0), "images/sprites/close/el/el_2_pioneer.png",(0,0), "images/sprites/close/el/el_2_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/el/el_2_body.png",(0,0), "images/sprites/close/el/el_2_pioneer.png",(0,0), "images/sprites/close/el/el_2_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/el/el_2_body.png",(0,0), "images/sprites/close/el/el_2_pioneer.png",(0,0), "images/sprites/close/el/el_2_sad.png") )
            image un surprise sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_sport.png",(0,0), "images/sprites/close/un/un_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_sport.png",(0,0), "images/sprites/close/un/un_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_sport.png",(0,0), "images/sprites/close/un/un_2_surprise.png") )
            image mt surprise panama pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_panama.png",(0,0), "images/sprites/close/mt/mt_1_surprise.png",(0,0), "images/sprites/close/mt/mt_1_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_panama.png",(0,0), "images/sprites/close/mt/mt_1_surprise.png",(0,0), "images/sprites/close/mt/mt_1_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_panama.png",(0,0), "images/sprites/close/mt/mt_1_surprise.png",(0,0), "images/sprites/close/mt/mt_1_pioneer.png") )
            image us angry dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_dress.png",(0,0), "images/sprites/close/us/us_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_dress.png",(0,0), "images/sprites/close/us/us_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_dress.png",(0,0), "images/sprites/close/us/us_2_angry.png") )
            image sl serious sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_1_body.png",(0,0), "images/sprites/close/sl/sl_1_sport.png",(0,0), "images/sprites/close/sl/sl_1_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_1_body.png",(0,0), "images/sprites/close/sl/sl_1_sport.png",(0,0), "images/sprites/close/sl/sl_1_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_1_body.png",(0,0), "images/sprites/close/sl/sl_1_sport.png",(0,0), "images/sprites/close/sl/sl_1_serious.png") )
            image un scared sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_sport.png",(0,0), "images/sprites/close/un/un_2_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_sport.png",(0,0), "images/sprites/close/un/un_2_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_sport.png",(0,0), "images/sprites/close/un/un_2_scared.png") )
            image un cry dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_dress.png",(0,0), "images/sprites/close/un/un_2_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_dress.png",(0,0), "images/sprites/close/un/un_2_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_dress.png",(0,0), "images/sprites/close/un/un_2_cry.png") )
            image dv scared pioneer2 close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_pioneer2.png",(0,0), "images/sprites/close/dv/dv_1_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_pioneer2.png",(0,0), "images/sprites/close/dv/dv_1_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_pioneer2.png",(0,0), "images/sprites/close/dv/dv_1_scared.png") )
            image dv shocked pioneer2 close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_pioneer2.png",(0,0), "images/sprites/close/dv/dv_1_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_pioneer2.png",(0,0), "images/sprites/close/dv/dv_1_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_pioneer2.png",(0,0), "images/sprites/close/dv/dv_1_shocked.png") )
            image sl laugh swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_swim.png",(0,0), "images/sprites/close/sl/sl_2_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_swim.png",(0,0), "images/sprites/close/sl/sl_2_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_swim.png",(0,0), "images/sprites/close/sl/sl_2_laugh.png") )
            image us surp1 dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_dress.png",(0,0), "images/sprites/close/us/us_3_surp1.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_dress.png",(0,0), "images/sprites/close/us/us_3_surp1.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_dress.png",(0,0), "images/sprites/close/us/us_3_surp1.png") )
            image dv shocked swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_swim.png",(0,0), "images/sprites/close/dv/dv_1_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_swim.png",(0,0), "images/sprites/close/dv/dv_1_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_swim.png",(0,0), "images/sprites/close/dv/dv_1_shocked.png") )
            image sh laugh close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_1_body.png",(0,0), "images/sprites/close/sh/sh_1_laugh.png",(0,0), "images/sprites/close/sh/sh_1_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_1_body.png",(0,0), "images/sprites/close/sh/sh_1_laugh.png",(0,0), "images/sprites/close/sh/sh_1_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_1_body.png",(0,0), "images/sprites/close/sh/sh_1_laugh.png",(0,0), "images/sprites/close/sh/sh_1_laugh.png") )
            image us surp2 dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_dress.png",(0,0), "images/sprites/close/us/us_3_surp2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_dress.png",(0,0), "images/sprites/close/us/us_3_surp2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_dress.png",(0,0), "images/sprites/close/us/us_3_surp2.png") )
            image uv sad close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/uv/uv_1_body.png",(0,0), "images/sprites/close/uv/uv_1_pioneer.png",(0,0), "images/sprites/close/uv/uv_1_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/uv/uv_1_body.png",(0,0), "images/sprites/close/uv/uv_1_pioneer.png",(0,0), "images/sprites/close/uv/uv_1_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/uv/uv_1_body.png",(0,0), "images/sprites/close/uv/uv_1_pioneer.png",(0,0), "images/sprites/close/uv/uv_1_sad.png") )
            image el angry pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/el/el_3_body.png",(0,0), "images/sprites/close/el/el_3_pioneer.png",(0,0), "images/sprites/close/el/el_3_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/el/el_3_body.png",(0,0), "images/sprites/close/el/el_3_pioneer.png",(0,0), "images/sprites/close/el/el_3_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/el/el_3_body.png",(0,0), "images/sprites/close/el/el_3_pioneer.png",(0,0), "images/sprites/close/el/el_3_angry.png") )
            image us cry2 dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_dress.png",(0,0), "images/sprites/close/us/us_3_cry2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_dress.png",(0,0), "images/sprites/close/us/us_3_cry2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_dress.png",(0,0), "images/sprites/close/us/us_3_cry2.png") )
            image sl sad sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_sport.png",(0,0), "images/sprites/close/sl/sl_3_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_sport.png",(0,0), "images/sprites/close/sl/sl_3_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_sport.png",(0,0), "images/sprites/close/sl/sl_3_sad.png") )
            image mi scared swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_swim.png",(0,0), "images/sprites/close/mi/mi_1_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_swim.png",(0,0), "images/sprites/close/mi/mi_1_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_swim.png",(0,0), "images/sprites/close/mi/mi_1_scared.png") )
            image us laugh swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_swim.png",(0,0), "images/sprites/close/us/us_1_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_swim.png",(0,0), "images/sprites/close/us/us_1_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_swim.png",(0,0), "images/sprites/close/us/us_1_laugh.png") )
            image mi surprise swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_swim.png",(0,0), "images/sprites/close/mi/mi_1_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_swim.png",(0,0), "images/sprites/close/mi/mi_1_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_swim.png",(0,0), "images/sprites/close/mi/mi_1_surprise.png") )
            image sl smile swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_1_body.png",(0,0), "images/sprites/close/sl/sl_1_swim.png",(0,0), "images/sprites/close/sl/sl_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_1_body.png",(0,0), "images/sprites/close/sl/sl_1_swim.png",(0,0), "images/sprites/close/sl/sl_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_1_body.png",(0,0), "images/sprites/close/sl/sl_1_swim.png",(0,0), "images/sprites/close/sl/sl_1_smile.png") )
            image us shy2 dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_dress.png",(0,0), "images/sprites/close/us/us_3_shy2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_dress.png",(0,0), "images/sprites/close/us/us_3_shy2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_dress.png",(0,0), "images/sprites/close/us/us_3_shy2.png") )
            image sl surprise swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_swim.png",(0,0), "images/sprites/close/sl/sl_3_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_swim.png",(0,0), "images/sprites/close/sl/sl_3_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_swim.png",(0,0), "images/sprites/close/sl/sl_3_surprise.png") )
            image dv smile pioneer2 close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_4_body.png",(0,0), "images/sprites/close/dv/dv_4_pioneer2.png",(0,0), "images/sprites/close/dv/dv_4_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_4_body.png",(0,0), "images/sprites/close/dv/dv_4_pioneer2.png",(0,0), "images/sprites/close/dv/dv_4_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_4_body.png",(0,0), "images/sprites/close/dv/dv_4_pioneer2.png",(0,0), "images/sprites/close/dv/dv_4_smile.png") )
            image mt sad dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_dress.png",(0,0), "images/sprites/close/mt/mt_1_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_dress.png",(0,0), "images/sprites/close/mt/mt_1_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_dress.png",(0,0), "images/sprites/close/mt/mt_1_sad.png") )
            image mt smile panama pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_panama.png",(0,0), "images/sprites/close/mt/mt_1_smile.png",(0,0), "images/sprites/close/mt/mt_1_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_panama.png",(0,0), "images/sprites/close/mt/mt_1_smile.png",(0,0), "images/sprites/close/mt/mt_1_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_panama.png",(0,0), "images/sprites/close/mt/mt_1_smile.png",(0,0), "images/sprites/close/mt/mt_1_pioneer.png") )
            image dv angry pioneer2 close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_5_body.png",(0,0), "images/sprites/close/dv/dv_5_pioneer2.png",(0,0), "images/sprites/close/dv/dv_5_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_5_body.png",(0,0), "images/sprites/close/dv/dv_5_pioneer2.png",(0,0), "images/sprites/close/dv/dv_5_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_5_body.png",(0,0), "images/sprites/close/dv/dv_5_pioneer2.png",(0,0), "images/sprites/close/dv/dv_5_angry.png") )
            image uv shocked close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/uv/uv_1_body.png",(0,0), "images/sprites/close/uv/uv_1_pioneer.png",(0,0), "images/sprites/close/uv/uv_1_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/uv/uv_1_body.png",(0,0), "images/sprites/close/uv/uv_1_pioneer.png",(0,0), "images/sprites/close/uv/uv_1_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/uv/uv_1_body.png",(0,0), "images/sprites/close/uv/uv_1_pioneer.png",(0,0), "images/sprites/close/uv/uv_1_shocked.png") )
            image mz shy glasses pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_3_body.png",(0,0), "images/sprites/close/mz/mz_3_glasses.png",(0,0), "images/sprites/close/mz/mz_3_shy.png",(0,0), "images/sprites/close/mz/mz_3_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_3_body.png",(0,0), "images/sprites/close/mz/mz_3_glasses.png",(0,0), "images/sprites/close/mz/mz_3_shy.png",(0,0), "images/sprites/close/mz/mz_3_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_3_body.png",(0,0), "images/sprites/close/mz/mz_3_glasses.png",(0,0), "images/sprites/close/mz/mz_3_shy.png",(0,0), "images/sprites/close/mz/mz_3_pioneer.png") )
            image dv sad pioneer2 close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_3_body.png",(0,0), "images/sprites/close/dv/dv_3_pioneer2.png",(0,0), "images/sprites/close/dv/dv_3_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_3_body.png",(0,0), "images/sprites/close/dv/dv_3_pioneer2.png",(0,0), "images/sprites/close/dv/dv_3_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_3_body.png",(0,0), "images/sprites/close/dv/dv_3_pioneer2.png",(0,0), "images/sprites/close/dv/dv_3_sad.png") )
            image us shy dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_dress.png",(0,0), "images/sprites/close/us/us_3_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_dress.png",(0,0), "images/sprites/close/us/us_3_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_dress.png",(0,0), "images/sprites/close/us/us_3_shy.png") )
            image dv normal pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_4_body.png",(0,0), "images/sprites/close/dv/dv_4_pioneer.png",(0,0), "images/sprites/close/dv/dv_4_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_4_body.png",(0,0), "images/sprites/close/dv/dv_4_pioneer.png",(0,0), "images/sprites/close/dv/dv_4_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_4_body.png",(0,0), "images/sprites/close/dv/dv_4_pioneer.png",(0,0), "images/sprites/close/dv/dv_4_normal.png") )
            image us calml pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_pioneer.png",(0,0), "images/sprites/close/us/us_2_calml.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_pioneer.png",(0,0), "images/sprites/close/us/us_2_calml.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_pioneer.png",(0,0), "images/sprites/close/us/us_2_calml.png") )
            image mt sad swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_swim.png",(0,0), "images/sprites/close/mt/mt_1_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_swim.png",(0,0), "images/sprites/close/mt/mt_1_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_swim.png",(0,0), "images/sprites/close/mt/mt_1_sad.png") )
            image sl tender dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_4_body.png",(0,0), "images/sprites/close/sl/sl_4_dress.png",(0,0), "images/sprites/close/sl/sl_4_tender.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_4_body.png",(0,0), "images/sprites/close/sl/sl_4_dress.png",(0,0), "images/sprites/close/sl/sl_4_tender.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_4_body.png",(0,0), "images/sprites/close/sl/sl_4_dress.png",(0,0), "images/sprites/close/sl/sl_4_tender.png") )
            image uv dontlike close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/uv/uv_1_body.png",(0,0), "images/sprites/close/uv/uv_1_pioneer.png",(0,0), "images/sprites/close/uv/uv_1_dontlike.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/uv/uv_1_body.png",(0,0), "images/sprites/close/uv/uv_1_pioneer.png",(0,0), "images/sprites/close/uv/uv_1_dontlike.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/uv/uv_1_body.png",(0,0), "images/sprites/close/uv/uv_1_pioneer.png",(0,0), "images/sprites/close/uv/uv_1_dontlike.png") )
            image sh surprise close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_3_body.png",(0,0), "images/sprites/close/sh/sh_3_normal.png",(0,0), "images/sprites/close/sh/sh_3_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_3_body.png",(0,0), "images/sprites/close/sh/sh_3_normal.png",(0,0), "images/sprites/close/sh/sh_3_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_3_body.png",(0,0), "images/sprites/close/sh/sh_3_normal.png",(0,0), "images/sprites/close/sh/sh_3_surprise.png") )
            image us dontlike swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_swim.png",(0,0), "images/sprites/close/us/us_2_dontlike.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_swim.png",(0,0), "images/sprites/close/us/us_2_dontlike.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_swim.png",(0,0), "images/sprites/close/us/us_2_dontlike.png") )
            image sl angry pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_pioneer.png",(0,0), "images/sprites/close/sl/sl_3_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_pioneer.png",(0,0), "images/sprites/close/sl/sl_3_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_pioneer.png",(0,0), "images/sprites/close/sl/sl_3_angry.png") )
            image us shy pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_pioneer.png",(0,0), "images/sprites/close/us/us_3_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_pioneer.png",(0,0), "images/sprites/close/us/us_3_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_pioneer.png",(0,0), "images/sprites/close/us/us_3_shy.png") )
            image un cry_smile pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_pioneer.png",(0,0), "images/sprites/close/un/un_2_cry_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_pioneer.png",(0,0), "images/sprites/close/un/un_2_cry_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_pioneer.png",(0,0), "images/sprites/close/un/un_2_cry_smile.png") )
            image un shy pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_pioneer.png",(0,0), "images/sprites/close/un/un_1_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_pioneer.png",(0,0), "images/sprites/close/un/un_1_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_pioneer.png",(0,0), "images/sprites/close/un/un_1_shy.png") )
            image mt normal panama swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_panama.png",(0,0), "images/sprites/close/mt/mt_1_normal.png",(0,0), "images/sprites/close/mt/mt_1_swim.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_panama.png",(0,0), "images/sprites/close/mt/mt_1_normal.png",(0,0), "images/sprites/close/mt/mt_1_swim.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_panama.png",(0,0), "images/sprites/close/mt/mt_1_normal.png",(0,0), "images/sprites/close/mt/mt_1_swim.png") )
            image sl normal swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_1_body.png",(0,0), "images/sprites/close/sl/sl_1_swim.png",(0,0), "images/sprites/close/sl/sl_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_1_body.png",(0,0), "images/sprites/close/sl/sl_1_swim.png",(0,0), "images/sprites/close/sl/sl_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_1_body.png",(0,0), "images/sprites/close/sl/sl_1_swim.png",(0,0), "images/sprites/close/sl/sl_1_normal.png") )
            image mz laugh pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_1_body.png",(0,0), "images/sprites/close/mz/mz_1_pioneer.png",(0,0), "images/sprites/close/mz/mz_1_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_1_body.png",(0,0), "images/sprites/close/mz/mz_1_pioneer.png",(0,0), "images/sprites/close/mz/mz_1_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_1_body.png",(0,0), "images/sprites/close/mz/mz_1_pioneer.png",(0,0), "images/sprites/close/mz/mz_1_laugh.png") )
            image dv surprise swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_swim.png",(0,0), "images/sprites/close/dv/dv_1_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_swim.png",(0,0), "images/sprites/close/dv/dv_1_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_swim.png",(0,0), "images/sprites/close/dv/dv_1_surprise.png") )
            image sl laugh pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_pioneer.png",(0,0), "images/sprites/close/sl/sl_2_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_pioneer.png",(0,0), "images/sprites/close/sl/sl_2_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_pioneer.png",(0,0), "images/sprites/close/sl/sl_2_laugh.png") )
            image sh laugh pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_1_body.png",(0,0), "images/sprites/close/sh/sh_1_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_1_body.png",(0,0), "images/sprites/close/sh/sh_1_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_1_body.png",(0,0), "images/sprites/close/sh/sh_1_laugh.png") )
            image sl smile sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_1_body.png",(0,0), "images/sprites/close/sl/sl_1_sport.png",(0,0), "images/sprites/close/sl/sl_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_1_body.png",(0,0), "images/sprites/close/sl/sl_1_sport.png",(0,0), "images/sprites/close/sl/sl_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_1_body.png",(0,0), "images/sprites/close/sl/sl_1_sport.png",(0,0), "images/sprites/close/sl/sl_1_smile.png") )
            image sl scared swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_4_body.png",(0,0), "images/sprites/close/sl/sl_4_swim.png",(0,0), "images/sprites/close/sl/sl_4_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_4_body.png",(0,0), "images/sprites/close/sl/sl_4_swim.png",(0,0), "images/sprites/close/sl/sl_4_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_4_body.png",(0,0), "images/sprites/close/sl/sl_4_swim.png",(0,0), "images/sprites/close/sl/sl_4_scared.png") )
            image un scared dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_dress.png",(0,0), "images/sprites/close/un/un_2_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_dress.png",(0,0), "images/sprites/close/un/un_2_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_dress.png",(0,0), "images/sprites/close/un/un_2_scared.png") )
            image sl serious swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_1_body.png",(0,0), "images/sprites/close/sl/sl_1_swim.png",(0,0), "images/sprites/close/sl/sl_1_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_1_body.png",(0,0), "images/sprites/close/sl/sl_1_swim.png",(0,0), "images/sprites/close/sl/sl_1_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_1_body.png",(0,0), "images/sprites/close/sl/sl_1_swim.png",(0,0), "images/sprites/close/sl/sl_1_serious.png") )
            image mt normal dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_dress.png",(0,0), "images/sprites/close/mt/mt_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_dress.png",(0,0), "images/sprites/close/mt/mt_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_dress.png",(0,0), "images/sprites/close/mt/mt_1_normal.png") )
            image us grin dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_dress.png",(0,0), "images/sprites/close/us/us_1_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_dress.png",(0,0), "images/sprites/close/us/us_1_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_dress.png",(0,0), "images/sprites/close/us/us_1_grin.png") )
            image sl laugh dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_dress.png",(0,0), "images/sprites/close/sl/sl_2_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_dress.png",(0,0), "images/sprites/close/sl/sl_2_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_dress.png",(0,0), "images/sprites/close/sl/sl_2_laugh.png") )
            image us laugh dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_dress.png",(0,0), "images/sprites/close/us/us_1_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_dress.png",(0,0), "images/sprites/close/us/us_1_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_dress.png",(0,0), "images/sprites/close/us/us_1_laugh.png") )
            image dv cry swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_swim.png",(0,0), "images/sprites/close/dv/dv_1_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_swim.png",(0,0), "images/sprites/close/dv/dv_1_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_swim.png",(0,0), "images/sprites/close/dv/dv_1_cry.png") )
            image cs shy stethoscope close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/cs/cs_1_body.png",(0,0), "images/sprites/close/cs/cs_1_stethoscope.png",(0,0), "images/sprites/close/cs/cs_1_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/cs/cs_1_body.png",(0,0), "images/sprites/close/cs/cs_1_stethoscope.png",(0,0), "images/sprites/close/cs/cs_1_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/cs/cs_1_body.png",(0,0), "images/sprites/close/cs/cs_1_stethoscope.png",(0,0), "images/sprites/close/cs/cs_1_shy.png") )
            image sh upset pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_1_body.png",(0,0), "images/sprites/close/sh/sh_1_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_1_body.png",(0,0), "images/sprites/close/sh/sh_1_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_1_body.png",(0,0), "images/sprites/close/sh/sh_1_upset.png") )
            image mz shy pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_3_body.png",(0,0), "images/sprites/close/mz/mz_3_pioneer.png",(0,0), "images/sprites/close/mz/mz_3_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_3_body.png",(0,0), "images/sprites/close/mz/mz_3_pioneer.png",(0,0), "images/sprites/close/mz/mz_3_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_3_body.png",(0,0), "images/sprites/close/mz/mz_3_pioneer.png",(0,0), "images/sprites/close/mz/mz_3_shy.png") )
            image mz laugh glasses pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_1_body.png",(0,0), "images/sprites/close/mz/mz_1_glasses.png",(0,0), "images/sprites/close/mz/mz_1_laugh.png",(0,0), "images/sprites/close/mz/mz_1_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_1_body.png",(0,0), "images/sprites/close/mz/mz_1_glasses.png",(0,0), "images/sprites/close/mz/mz_1_laugh.png",(0,0), "images/sprites/close/mz/mz_1_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_1_body.png",(0,0), "images/sprites/close/mz/mz_1_glasses.png",(0,0), "images/sprites/close/mz/mz_1_laugh.png",(0,0), "images/sprites/close/mz/mz_1_pioneer.png") )
            image mz normal glasses pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_1_body.png",(0,0), "images/sprites/close/mz/mz_1_glasses.png",(0,0), "images/sprites/close/mz/mz_1_normal.png",(0,0), "images/sprites/close/mz/mz_1_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_1_body.png",(0,0), "images/sprites/close/mz/mz_1_glasses.png",(0,0), "images/sprites/close/mz/mz_1_normal.png",(0,0), "images/sprites/close/mz/mz_1_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_1_body.png",(0,0), "images/sprites/close/mz/mz_1_glasses.png",(0,0), "images/sprites/close/mz/mz_1_normal.png",(0,0), "images/sprites/close/mz/mz_1_pioneer.png") )
            image cs shy close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/cs/cs_1_body.png",(0,0), "images/sprites/close/cs/cs_1_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/cs/cs_1_body.png",(0,0), "images/sprites/close/cs/cs_1_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/cs/cs_1_body.png",(0,0), "images/sprites/close/cs/cs_1_shy.png") )
            image pi close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/pi/pi_1_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/pi/pi_1_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/pi/pi_1_pioneer.png") )
            image mz bukal glasses pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_1_body.png",(0,0), "images/sprites/close/mz/mz_1_glasses.png",(0,0), "images/sprites/close/mz/mz_1_bukal.png",(0,0), "images/sprites/close/mz/mz_1_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_1_body.png",(0,0), "images/sprites/close/mz/mz_1_glasses.png",(0,0), "images/sprites/close/mz/mz_1_bukal.png",(0,0), "images/sprites/close/mz/mz_1_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_1_body.png",(0,0), "images/sprites/close/mz/mz_1_glasses.png",(0,0), "images/sprites/close/mz/mz_1_bukal.png",(0,0), "images/sprites/close/mz/mz_1_pioneer.png") )
            image mi rage pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_3_body.png",(0,0), "images/sprites/close/mi/mi_3_pioneer.png",(0,0), "images/sprites/close/mi/mi_3_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_3_body.png",(0,0), "images/sprites/close/mi/mi_3_pioneer.png",(0,0), "images/sprites/close/mi/mi_3_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_3_body.png",(0,0), "images/sprites/close/mi/mi_3_pioneer.png",(0,0), "images/sprites/close/mi/mi_3_rage.png") )
            image sl normal pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_1_body.png",(0,0), "images/sprites/close/sl/sl_1_pioneer.png",(0,0), "images/sprites/close/sl/sl_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_1_body.png",(0,0), "images/sprites/close/sl/sl_1_pioneer.png",(0,0), "images/sprites/close/sl/sl_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_1_body.png",(0,0), "images/sprites/close/sl/sl_1_pioneer.png",(0,0), "images/sprites/close/sl/sl_1_normal.png") )
            image mi rage swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_3_body.png",(0,0), "images/sprites/close/mi/mi_3_swim.png",(0,0), "images/sprites/close/mi/mi_3_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_3_body.png",(0,0), "images/sprites/close/mi/mi_3_swim.png",(0,0), "images/sprites/close/mi/mi_3_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_3_body.png",(0,0), "images/sprites/close/mi/mi_3_swim.png",(0,0), "images/sprites/close/mi/mi_3_rage.png") )
            image el upset pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/el/el_2_body.png",(0,0), "images/sprites/close/el/el_2_pioneer.png",(0,0), "images/sprites/close/el/el_2_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/el/el_2_body.png",(0,0), "images/sprites/close/el/el_2_pioneer.png",(0,0), "images/sprites/close/el/el_2_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/el/el_2_body.png",(0,0), "images/sprites/close/el/el_2_pioneer.png",(0,0), "images/sprites/close/el/el_2_upset.png") )
            image us normal pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_pioneer.png",(0,0), "images/sprites/close/us/us_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_pioneer.png",(0,0), "images/sprites/close/us/us_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_pioneer.png",(0,0), "images/sprites/close/us/us_1_normal.png") )
            image un shy dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_dress.png",(0,0), "images/sprites/close/un/un_1_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_dress.png",(0,0), "images/sprites/close/un/un_1_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_dress.png",(0,0), "images/sprites/close/un/un_1_shy.png") )
            image mt surprise panama swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_panama.png",(0,0), "images/sprites/close/mt/mt_1_surprise.png",(0,0), "images/sprites/close/mt/mt_1_swim.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_panama.png",(0,0), "images/sprites/close/mt/mt_1_surprise.png",(0,0), "images/sprites/close/mt/mt_1_swim.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_panama.png",(0,0), "images/sprites/close/mt/mt_1_surprise.png",(0,0), "images/sprites/close/mt/mt_1_swim.png") )
            image us sad sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_sport.png",(0,0), "images/sprites/close/us/us_1_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_sport.png",(0,0), "images/sprites/close/us/us_1_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_sport.png",(0,0), "images/sprites/close/us/us_1_sad.png") )
            image mi angry swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_3_body.png",(0,0), "images/sprites/close/mi/mi_3_swim.png",(0,0), "images/sprites/close/mi/mi_3_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_3_body.png",(0,0), "images/sprites/close/mi/mi_3_swim.png",(0,0), "images/sprites/close/mi/mi_3_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_3_body.png",(0,0), "images/sprites/close/mi/mi_3_swim.png",(0,0), "images/sprites/close/mi/mi_3_angry.png") )
            image sl happy pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_pioneer.png",(0,0), "images/sprites/close/sl/sl_2_happy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_pioneer.png",(0,0), "images/sprites/close/sl/sl_2_happy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_pioneer.png",(0,0), "images/sprites/close/sl/sl_2_happy.png") )
            image mt sad panama pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_panama.png",(0,0), "images/sprites/close/mt/mt_1_sad.png",(0,0), "images/sprites/close/mt/mt_1_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_panama.png",(0,0), "images/sprites/close/mt/mt_1_sad.png",(0,0), "images/sprites/close/mt/mt_1_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_panama.png",(0,0), "images/sprites/close/mt/mt_1_sad.png",(0,0), "images/sprites/close/mt/mt_1_pioneer.png") )
            image us calml sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_sport.png",(0,0), "images/sprites/close/us/us_2_calml.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_sport.png",(0,0), "images/sprites/close/us/us_2_calml.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_sport.png",(0,0), "images/sprites/close/us/us_2_calml.png") )
            image us shy2 pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_pioneer.png",(0,0), "images/sprites/close/us/us_3_shy2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_pioneer.png",(0,0), "images/sprites/close/us/us_3_shy2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_pioneer.png",(0,0), "images/sprites/close/us/us_3_shy2.png") )
            image un surprise pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_pioneer.png",(0,0), "images/sprites/close/un/un_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_pioneer.png",(0,0), "images/sprites/close/un/un_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_pioneer.png",(0,0), "images/sprites/close/un/un_2_surprise.png") )
            image us cry sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_sport.png",(0,0), "images/sprites/close/us/us_3_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_sport.png",(0,0), "images/sprites/close/us/us_3_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_sport.png",(0,0), "images/sprites/close/us/us_3_cry.png") )
            image mi angry pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_3_body.png",(0,0), "images/sprites/close/mi/mi_3_pioneer.png",(0,0), "images/sprites/close/mi/mi_3_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_3_body.png",(0,0), "images/sprites/close/mi/mi_3_pioneer.png",(0,0), "images/sprites/close/mi/mi_3_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_3_body.png",(0,0), "images/sprites/close/mi/mi_3_pioneer.png",(0,0), "images/sprites/close/mi/mi_3_angry.png") )
            image us sad pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_pioneer.png",(0,0), "images/sprites/close/us/us_1_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_pioneer.png",(0,0), "images/sprites/close/us/us_1_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_pioneer.png",(0,0), "images/sprites/close/us/us_1_sad.png") )
            image uv smile close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/uv/uv_2_body.png",(0,0), "images/sprites/close/uv/uv_2_pioneer.png",(0,0), "images/sprites/close/uv/uv_2_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/uv/uv_2_body.png",(0,0), "images/sprites/close/uv/uv_2_pioneer.png",(0,0), "images/sprites/close/uv/uv_2_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/uv/uv_2_body.png",(0,0), "images/sprites/close/uv/uv_2_pioneer.png",(0,0), "images/sprites/close/uv/uv_2_smile.png") )
            image un cry swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_swim.png",(0,0), "images/sprites/close/un/un_2_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_swim.png",(0,0), "images/sprites/close/un/un_2_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_swim.png",(0,0), "images/sprites/close/un/un_2_cry.png") )
            image sh normal pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_3_body.png",(0,0), "images/sprites/close/sh/sh_3_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_3_body.png",(0,0), "images/sprites/close/sh/sh_3_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_3_body.png",(0,0), "images/sprites/close/sh/sh_3_normal.png") )
            image sh rage close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_2_body.png",(0,0), "images/sprites/close/sh/sh_2_rage.png",(0,0), "images/sprites/close/sh/sh_2_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_2_body.png",(0,0), "images/sprites/close/sh/sh_2_rage.png",(0,0), "images/sprites/close/sh/sh_2_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_2_body.png",(0,0), "images/sprites/close/sh/sh_2_rage.png",(0,0), "images/sprites/close/sh/sh_2_rage.png") )
            image us normal sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_sport.png",(0,0), "images/sprites/close/us/us_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_sport.png",(0,0), "images/sprites/close/us/us_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_sport.png",(0,0), "images/sprites/close/us/us_1_normal.png") )
            image un angry2 sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_sport.png",(0,0), "images/sprites/close/un/un_3_angry2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_sport.png",(0,0), "images/sprites/close/un/un_3_angry2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_sport.png",(0,0), "images/sprites/close/un/un_3_angry2.png") )
            image sl happy swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_swim.png",(0,0), "images/sprites/close/sl/sl_2_happy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_swim.png",(0,0), "images/sprites/close/sl/sl_2_happy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_swim.png",(0,0), "images/sprites/close/sl/sl_2_happy.png") )
            image mz rage glasses pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_2_body.png",(0,0), "images/sprites/close/mz/mz_2_glasses.png",(0,0), "images/sprites/close/mz/mz_2_rage.png",(0,0), "images/sprites/close/mz/mz_2_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_2_body.png",(0,0), "images/sprites/close/mz/mz_2_glasses.png",(0,0), "images/sprites/close/mz/mz_2_rage.png",(0,0), "images/sprites/close/mz/mz_2_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_2_body.png",(0,0), "images/sprites/close/mz/mz_2_glasses.png",(0,0), "images/sprites/close/mz/mz_2_rage.png",(0,0), "images/sprites/close/mz/mz_2_pioneer.png") )
            image us smile pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_pioneer.png",(0,0), "images/sprites/close/us/us_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_pioneer.png",(0,0), "images/sprites/close/us/us_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_pioneer.png",(0,0), "images/sprites/close/us/us_1_smile.png") )
            image mt angry panama swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_2_body.png",(0,0), "images/sprites/close/mt/mt_2_panama.png",(0,0), "images/sprites/close/mt/mt_2_angry.png",(0,0), "images/sprites/close/mt/mt_2_swim.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_2_body.png",(0,0), "images/sprites/close/mt/mt_2_panama.png",(0,0), "images/sprites/close/mt/mt_2_angry.png",(0,0), "images/sprites/close/mt/mt_2_swim.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_2_body.png",(0,0), "images/sprites/close/mt/mt_2_panama.png",(0,0), "images/sprites/close/mt/mt_2_angry.png",(0,0), "images/sprites/close/mt/mt_2_swim.png") )
            image sh cry pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_2_body.png",(0,0), "images/sprites/close/sh/sh_2_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_2_body.png",(0,0), "images/sprites/close/sh/sh_2_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_2_body.png",(0,0), "images/sprites/close/sh/sh_2_cry.png") )
            image mz smile glasses pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_3_body.png",(0,0), "images/sprites/close/mz/mz_3_glasses.png",(0,0), "images/sprites/close/mz/mz_3_smile.png",(0,0), "images/sprites/close/mz/mz_3_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_3_body.png",(0,0), "images/sprites/close/mz/mz_3_glasses.png",(0,0), "images/sprites/close/mz/mz_3_smile.png",(0,0), "images/sprites/close/mz/mz_3_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_3_body.png",(0,0), "images/sprites/close/mz/mz_3_glasses.png",(0,0), "images/sprites/close/mz/mz_3_smile.png",(0,0), "images/sprites/close/mz/mz_3_pioneer.png") )
            image sh scared pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_1_body.png",(0,0), "images/sprites/close/sh/sh_1_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_1_body.png",(0,0), "images/sprites/close/sh/sh_1_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_1_body.png",(0,0), "images/sprites/close/sh/sh_1_scared.png") )
            image mi upset pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_3_body.png",(0,0), "images/sprites/close/mi/mi_3_pioneer.png",(0,0), "images/sprites/close/mi/mi_3_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_3_body.png",(0,0), "images/sprites/close/mi/mi_3_pioneer.png",(0,0), "images/sprites/close/mi/mi_3_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_3_body.png",(0,0), "images/sprites/close/mi/mi_3_pioneer.png",(0,0), "images/sprites/close/mi/mi_3_upset.png") )
            image mi upset swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_3_body.png",(0,0), "images/sprites/close/mi/mi_3_swim.png",(0,0), "images/sprites/close/mi/mi_3_upset.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_3_body.png",(0,0), "images/sprites/close/mi/mi_3_swim.png",(0,0), "images/sprites/close/mi/mi_3_upset.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_3_body.png",(0,0), "images/sprites/close/mi/mi_3_swim.png",(0,0), "images/sprites/close/mi/mi_3_upset.png") )
            image us normal swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_swim.png",(0,0), "images/sprites/close/us/us_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_swim.png",(0,0), "images/sprites/close/us/us_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_swim.png",(0,0), "images/sprites/close/us/us_1_normal.png") )
            image sh normal close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_3_body.png",(0,0), "images/sprites/close/sh/sh_3_normal.png",(0,0), "images/sprites/close/sh/sh_3_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_3_body.png",(0,0), "images/sprites/close/sh/sh_3_normal.png",(0,0), "images/sprites/close/sh/sh_3_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_3_body.png",(0,0), "images/sprites/close/sh/sh_3_normal.png",(0,0), "images/sprites/close/sh/sh_3_normal.png") )
            image un shocked dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_dress.png",(0,0), "images/sprites/close/un/un_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_dress.png",(0,0), "images/sprites/close/un/un_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_dress.png",(0,0), "images/sprites/close/un/un_2_shocked.png") )
            image un angry sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_sport.png",(0,0), "images/sprites/close/un/un_1_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_sport.png",(0,0), "images/sprites/close/un/un_1_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_sport.png",(0,0), "images/sprites/close/un/un_1_angry.png") )
            image el smile pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/el/el_1_body.png",(0,0), "images/sprites/close/el/el_1_pioneer.png",(0,0), "images/sprites/close/el/el_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/el/el_1_body.png",(0,0), "images/sprites/close/el/el_1_pioneer.png",(0,0), "images/sprites/close/el/el_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/el/el_1_body.png",(0,0), "images/sprites/close/el/el_1_pioneer.png",(0,0), "images/sprites/close/el/el_1_smile.png") )
            image mi cry_smile swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_2_body.png",(0,0), "images/sprites/close/mi/mi_2_swim.png",(0,0), "images/sprites/close/mi/mi_2_cry_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_2_body.png",(0,0), "images/sprites/close/mi/mi_2_swim.png",(0,0), "images/sprites/close/mi/mi_2_cry_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_2_body.png",(0,0), "images/sprites/close/mi/mi_2_swim.png",(0,0), "images/sprites/close/mi/mi_2_cry_smile.png") )
            image mi grin pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_2_body.png",(0,0), "images/sprites/close/mi/mi_2_pioneer.png",(0,0), "images/sprites/close/mi/mi_2_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_2_body.png",(0,0), "images/sprites/close/mi/mi_2_pioneer.png",(0,0), "images/sprites/close/mi/mi_2_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_2_body.png",(0,0), "images/sprites/close/mi/mi_2_pioneer.png",(0,0), "images/sprites/close/mi/mi_2_grin.png") )
            image sl scared dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_4_body.png",(0,0), "images/sprites/close/sl/sl_4_dress.png",(0,0), "images/sprites/close/sl/sl_4_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_4_body.png",(0,0), "images/sprites/close/sl/sl_4_dress.png",(0,0), "images/sprites/close/sl/sl_4_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_4_body.png",(0,0), "images/sprites/close/sl/sl_4_dress.png",(0,0), "images/sprites/close/sl/sl_4_scared.png") )
            image un cry_smile dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_dress.png",(0,0), "images/sprites/close/un/un_2_cry_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_dress.png",(0,0), "images/sprites/close/un/un_2_cry_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_dress.png",(0,0), "images/sprites/close/un/un_2_cry_smile.png") )
            image un cry_smile sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_sport.png",(0,0), "images/sprites/close/un/un_2_cry_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_sport.png",(0,0), "images/sprites/close/un/un_2_cry_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_sport.png",(0,0), "images/sprites/close/un/un_2_cry_smile.png") )
            image un sad sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_sport.png",(0,0), "images/sprites/close/un/un_2_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_sport.png",(0,0), "images/sprites/close/un/un_2_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_sport.png",(0,0), "images/sprites/close/un/un_2_sad.png") )
            image mt surprise panama dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_panama.png",(0,0), "images/sprites/close/mt/mt_1_surprise.png",(0,0), "images/sprites/close/mt/mt_1_dress.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_panama.png",(0,0), "images/sprites/close/mt/mt_1_surprise.png",(0,0), "images/sprites/close/mt/mt_1_dress.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_panama.png",(0,0), "images/sprites/close/mt/mt_1_surprise.png",(0,0), "images/sprites/close/mt/mt_1_dress.png") )
            image dv normal pioneer2 close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_4_body.png",(0,0), "images/sprites/close/dv/dv_4_pioneer2.png",(0,0), "images/sprites/close/dv/dv_4_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_4_body.png",(0,0), "images/sprites/close/dv/dv_4_pioneer2.png",(0,0), "images/sprites/close/dv/dv_4_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_4_body.png",(0,0), "images/sprites/close/dv/dv_4_pioneer2.png",(0,0), "images/sprites/close/dv/dv_4_normal.png") )
            image mz angry glasses pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_2_body.png",(0,0), "images/sprites/close/mz/mz_2_glasses.png",(0,0), "images/sprites/close/mz/mz_2_angry.png",(0,0), "images/sprites/close/mz/mz_2_pioneer.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_2_body.png",(0,0), "images/sprites/close/mz/mz_2_glasses.png",(0,0), "images/sprites/close/mz/mz_2_angry.png",(0,0), "images/sprites/close/mz/mz_2_pioneer.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_2_body.png",(0,0), "images/sprites/close/mz/mz_2_glasses.png",(0,0), "images/sprites/close/mz/mz_2_angry.png",(0,0), "images/sprites/close/mz/mz_2_pioneer.png") )
            image us cry2 pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_pioneer.png",(0,0), "images/sprites/close/us/us_3_cry2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_pioneer.png",(0,0), "images/sprites/close/us/us_3_cry2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_pioneer.png",(0,0), "images/sprites/close/us/us_3_cry2.png") )
            image mi sad swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_2_body.png",(0,0), "images/sprites/close/mi/mi_2_swim.png",(0,0), "images/sprites/close/mi/mi_2_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_2_body.png",(0,0), "images/sprites/close/mi/mi_2_swim.png",(0,0), "images/sprites/close/mi/mi_2_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_2_body.png",(0,0), "images/sprites/close/mi/mi_2_swim.png",(0,0), "images/sprites/close/mi/mi_2_sad.png") )
            image un sad swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_swim.png",(0,0), "images/sprites/close/un/un_2_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_swim.png",(0,0), "images/sprites/close/un/un_2_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_swim.png",(0,0), "images/sprites/close/un/un_2_sad.png") )
            image us laugh2 sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_sport.png",(0,0), "images/sprites/close/us/us_1_laugh2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_sport.png",(0,0), "images/sprites/close/us/us_1_laugh2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_sport.png",(0,0), "images/sprites/close/us/us_1_laugh2.png") )
            image dv angry pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_5_body.png",(0,0), "images/sprites/close/dv/dv_5_pioneer.png",(0,0), "images/sprites/close/dv/dv_5_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_5_body.png",(0,0), "images/sprites/close/dv/dv_5_pioneer.png",(0,0), "images/sprites/close/dv/dv_5_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_5_body.png",(0,0), "images/sprites/close/dv/dv_5_pioneer.png",(0,0), "images/sprites/close/dv/dv_5_angry.png") )
            image mt smile pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_pioneer.png",(0,0), "images/sprites/close/mt/mt_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_pioneer.png",(0,0), "images/sprites/close/mt/mt_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_pioneer.png",(0,0), "images/sprites/close/mt/mt_1_smile.png") )
            image mi shy swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_swim.png",(0,0), "images/sprites/close/mi/mi_1_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_swim.png",(0,0), "images/sprites/close/mi/mi_1_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_swim.png",(0,0), "images/sprites/close/mi/mi_1_shy.png") )
            image un grin dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_dress.png",(0,0), "images/sprites/close/un/un_3_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_dress.png",(0,0), "images/sprites/close/un/un_3_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_dress.png",(0,0), "images/sprites/close/un/un_3_grin.png") )
            image mt laugh pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_3_body.png",(0,0), "images/sprites/close/mt/mt_3_pioneer.png",(0,0), "images/sprites/close/mt/mt_3_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_3_body.png",(0,0), "images/sprites/close/mt/mt_3_pioneer.png",(0,0), "images/sprites/close/mt/mt_3_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_3_body.png",(0,0), "images/sprites/close/mt/mt_3_pioneer.png",(0,0), "images/sprites/close/mt/mt_3_laugh.png") )
            image un laugh pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_pioneer.png",(0,0), "images/sprites/close/un/un_3_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_pioneer.png",(0,0), "images/sprites/close/un/un_3_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_pioneer.png",(0,0), "images/sprites/close/un/un_3_laugh.png") )
            image dv laugh pioneer2 close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_4_body.png",(0,0), "images/sprites/close/dv/dv_4_pioneer2.png",(0,0), "images/sprites/close/dv/dv_4_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_4_body.png",(0,0), "images/sprites/close/dv/dv_4_pioneer2.png",(0,0), "images/sprites/close/dv/dv_4_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_4_body.png",(0,0), "images/sprites/close/dv/dv_4_pioneer2.png",(0,0), "images/sprites/close/dv/dv_4_laugh.png") )
            image us surp1 pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_pioneer.png",(0,0), "images/sprites/close/us/us_3_surp1.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_pioneer.png",(0,0), "images/sprites/close/us/us_3_surp1.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_pioneer.png",(0,0), "images/sprites/close/us/us_3_surp1.png") )
            image sh rage pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_2_body.png",(0,0), "images/sprites/close/sh/sh_2_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_2_body.png",(0,0), "images/sprites/close/sh/sh_2_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_2_body.png",(0,0), "images/sprites/close/sh/sh_2_rage.png") )
            image mt angry panama dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_2_body.png",(0,0), "images/sprites/close/mt/mt_2_panama.png",(0,0), "images/sprites/close/mt/mt_2_angry.png",(0,0), "images/sprites/close/mt/mt_2_dress.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_2_body.png",(0,0), "images/sprites/close/mt/mt_2_panama.png",(0,0), "images/sprites/close/mt/mt_2_angry.png",(0,0), "images/sprites/close/mt/mt_2_dress.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_2_body.png",(0,0), "images/sprites/close/mt/mt_2_panama.png",(0,0), "images/sprites/close/mt/mt_2_angry.png",(0,0), "images/sprites/close/mt/mt_2_dress.png") )
            image un shocked swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_swim.png",(0,0), "images/sprites/close/un/un_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_swim.png",(0,0), "images/sprites/close/un/un_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_swim.png",(0,0), "images/sprites/close/un/un_2_shocked.png") )
            image un evil_smile dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_dress.png",(0,0), "images/sprites/close/un/un_1_evil_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_dress.png",(0,0), "images/sprites/close/un/un_1_evil_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_dress.png",(0,0), "images/sprites/close/un/un_1_evil_smile.png") )
            image uv laugh close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/uv/uv_3_body.png",(0,0), "images/sprites/close/uv/uv_3_pioneer.png",(0,0), "images/sprites/close/uv/uv_3_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/uv/uv_3_body.png",(0,0), "images/sprites/close/uv/uv_3_pioneer.png",(0,0), "images/sprites/close/uv/uv_3_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/uv/uv_3_body.png",(0,0), "images/sprites/close/uv/uv_3_pioneer.png",(0,0), "images/sprites/close/uv/uv_3_laugh.png") )
            image dv scared swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_swim.png",(0,0), "images/sprites/close/dv/dv_1_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_swim.png",(0,0), "images/sprites/close/dv/dv_1_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_swim.png",(0,0), "images/sprites/close/dv/dv_1_scared.png") )
            image mi shocked swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_swim.png",(0,0), "images/sprites/close/mi/mi_1_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_swim.png",(0,0), "images/sprites/close/mi/mi_1_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_swim.png",(0,0), "images/sprites/close/mi/mi_1_shocked.png") )
            image mt angry pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_2_body.png",(0,0), "images/sprites/close/mt/mt_2_pioneer.png",(0,0), "images/sprites/close/mt/mt_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_2_body.png",(0,0), "images/sprites/close/mt/mt_2_pioneer.png",(0,0), "images/sprites/close/mt/mt_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_2_body.png",(0,0), "images/sprites/close/mt/mt_2_pioneer.png",(0,0), "images/sprites/close/mt/mt_2_angry.png") )
            image el fingal pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/el/el_2_body.png",(0,0), "images/sprites/close/el/el_2_pioneer.png",(0,0), "images/sprites/close/el/el_2_fingal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/el/el_2_body.png",(0,0), "images/sprites/close/el/el_2_pioneer.png",(0,0), "images/sprites/close/el/el_2_fingal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/el/el_2_body.png",(0,0), "images/sprites/close/el/el_2_pioneer.png",(0,0), "images/sprites/close/el/el_2_fingal.png") )
            image us surp3 sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_sport.png",(0,0), "images/sprites/close/us/us_3_surp3.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_sport.png",(0,0), "images/sprites/close/us/us_3_surp3.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_sport.png",(0,0), "images/sprites/close/us/us_3_surp3.png") )
            image sl happy dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_dress.png",(0,0), "images/sprites/close/sl/sl_2_happy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_dress.png",(0,0), "images/sprites/close/sl/sl_2_happy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_dress.png",(0,0), "images/sprites/close/sl/sl_2_happy.png") )
            image sh scared close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_1_body.png",(0,0), "images/sprites/close/sh/sh_1_laugh.png",(0,0), "images/sprites/close/sh/sh_1_scared.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_1_body.png",(0,0), "images/sprites/close/sh/sh_1_laugh.png",(0,0), "images/sprites/close/sh/sh_1_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sh/sh_1_body.png",(0,0), "images/sprites/close/sh/sh_1_laugh.png",(0,0), "images/sprites/close/sh/sh_1_scared.png") )
            image un angry2 pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_pioneer.png",(0,0), "images/sprites/close/un/un_3_angry2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_pioneer.png",(0,0), "images/sprites/close/un/un_3_angry2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_pioneer.png",(0,0), "images/sprites/close/un/un_3_angry2.png") )
            image uv grin close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/uv/uv_3_body.png",(0,0), "images/sprites/close/uv/uv_3_pioneer.png",(0,0), "images/sprites/close/uv/uv_3_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/uv/uv_3_body.png",(0,0), "images/sprites/close/uv/uv_3_pioneer.png",(0,0), "images/sprites/close/uv/uv_3_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/uv/uv_3_body.png",(0,0), "images/sprites/close/uv/uv_3_pioneer.png",(0,0), "images/sprites/close/uv/uv_3_grin.png") )
            image mi shy pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_pioneer.png",(0,0), "images/sprites/close/mi/mi_1_shy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_pioneer.png",(0,0), "images/sprites/close/mi/mi_1_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_pioneer.png",(0,0), "images/sprites/close/mi/mi_1_shy.png") )
            image sl sad pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_pioneer.png",(0,0), "images/sprites/close/sl/sl_3_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_pioneer.png",(0,0), "images/sprites/close/sl/sl_3_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_pioneer.png",(0,0), "images/sprites/close/sl/sl_3_sad.png") )
            image un smile2 sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_sport.png",(0,0), "images/sprites/close/un/un_1_smile2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_sport.png",(0,0), "images/sprites/close/un/un_1_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_sport.png",(0,0), "images/sprites/close/un/un_1_smile2.png") )
            image us cry dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_dress.png",(0,0), "images/sprites/close/us/us_3_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_dress.png",(0,0), "images/sprites/close/us/us_3_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_dress.png",(0,0), "images/sprites/close/us/us_3_cry.png") )
            image un rage pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_pioneer.png",(0,0), "images/sprites/close/un/un_3_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_pioneer.png",(0,0), "images/sprites/close/un/un_3_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_pioneer.png",(0,0), "images/sprites/close/un/un_3_rage.png") )
            image sl sad swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_swim.png",(0,0), "images/sprites/close/sl/sl_3_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_swim.png",(0,0), "images/sprites/close/sl/sl_3_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_swim.png",(0,0), "images/sprites/close/sl/sl_3_sad.png") )
            image mi normal pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_3_body.png",(0,0), "images/sprites/close/mi/mi_3_pioneer.png",(0,0), "images/sprites/close/mi/mi_3_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_3_body.png",(0,0), "images/sprites/close/mi/mi_3_pioneer.png",(0,0), "images/sprites/close/mi/mi_3_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_3_body.png",(0,0), "images/sprites/close/mi/mi_3_pioneer.png",(0,0), "images/sprites/close/mi/mi_3_normal.png") )
            image us surp1 sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_sport.png",(0,0), "images/sprites/close/us/us_3_surp1.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_sport.png",(0,0), "images/sprites/close/us/us_3_surp1.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_sport.png",(0,0), "images/sprites/close/us/us_3_surp1.png") )
            image us cry swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_swim.png",(0,0), "images/sprites/close/us/us_3_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_swim.png",(0,0), "images/sprites/close/us/us_3_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_swim.png",(0,0), "images/sprites/close/us/us_3_cry.png") )
            image un serious dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_dress.png",(0,0), "images/sprites/close/un/un_3_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_dress.png",(0,0), "images/sprites/close/un/un_3_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_dress.png",(0,0), "images/sprites/close/un/un_3_serious.png") )
            image un laugh sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_sport.png",(0,0), "images/sprites/close/un/un_3_laugh.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_sport.png",(0,0), "images/sprites/close/un/un_3_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_sport.png",(0,0), "images/sprites/close/un/un_3_laugh.png") )
            image un surprise dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_dress.png",(0,0), "images/sprites/close/un/un_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_dress.png",(0,0), "images/sprites/close/un/un_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_dress.png",(0,0), "images/sprites/close/un/un_2_surprise.png") )
            image mi happy swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_2_body.png",(0,0), "images/sprites/close/mi/mi_2_swim.png",(0,0), "images/sprites/close/mi/mi_2_happy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_2_body.png",(0,0), "images/sprites/close/mi/mi_2_swim.png",(0,0), "images/sprites/close/mi/mi_2_happy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_2_body.png",(0,0), "images/sprites/close/mi/mi_2_swim.png",(0,0), "images/sprites/close/mi/mi_2_happy.png") )
            image mi serious swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_3_body.png",(0,0), "images/sprites/close/mi/mi_3_swim.png",(0,0), "images/sprites/close/mi/mi_3_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_3_body.png",(0,0), "images/sprites/close/mi/mi_3_swim.png",(0,0), "images/sprites/close/mi/mi_3_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_3_body.png",(0,0), "images/sprites/close/mi/mi_3_swim.png",(0,0), "images/sprites/close/mi/mi_3_serious.png") )
            image uv surprise2 close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/uv/uv_3_body.png",(0,0), "images/sprites/close/uv/uv_3_pioneer.png",(0,0), "images/sprites/close/uv/uv_3_surprise2.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/uv/uv_3_body.png",(0,0), "images/sprites/close/uv/uv_3_pioneer.png",(0,0), "images/sprites/close/uv/uv_3_surprise2.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/uv/uv_3_body.png",(0,0), "images/sprites/close/uv/uv_3_pioneer.png",(0,0), "images/sprites/close/uv/uv_3_surprise2.png") )
            image mz angry pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_2_body.png",(0,0), "images/sprites/close/mz/mz_2_pioneer.png",(0,0), "images/sprites/close/mz/mz_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_2_body.png",(0,0), "images/sprites/close/mz/mz_2_pioneer.png",(0,0), "images/sprites/close/mz/mz_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_2_body.png",(0,0), "images/sprites/close/mz/mz_2_pioneer.png",(0,0), "images/sprites/close/mz/mz_2_angry.png") )
            image un sad pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_pioneer.png",(0,0), "images/sprites/close/un/un_2_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_pioneer.png",(0,0), "images/sprites/close/un/un_2_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_pioneer.png",(0,0), "images/sprites/close/un/un_2_sad.png") )
            image dv surprise pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_pioneer.png",(0,0), "images/sprites/close/dv/dv_1_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_pioneer.png",(0,0), "images/sprites/close/dv/dv_1_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_pioneer.png",(0,0), "images/sprites/close/dv/dv_1_surprise.png") )
            image mz bukal pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_1_body.png",(0,0), "images/sprites/close/mz/mz_1_pioneer.png",(0,0), "images/sprites/close/mz/mz_1_bukal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_1_body.png",(0,0), "images/sprites/close/mz/mz_1_pioneer.png",(0,0), "images/sprites/close/mz/mz_1_bukal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mz/mz_1_body.png",(0,0), "images/sprites/close/mz/mz_1_pioneer.png",(0,0), "images/sprites/close/mz/mz_1_bukal.png") )
            image mi shocked pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_pioneer.png",(0,0), "images/sprites/close/mi/mi_1_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_pioneer.png",(0,0), "images/sprites/close/mi/mi_1_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_pioneer.png",(0,0), "images/sprites/close/mi/mi_1_shocked.png") )
            image sl happy sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_sport.png",(0,0), "images/sprites/close/sl/sl_2_happy.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_sport.png",(0,0), "images/sprites/close/sl/sl_2_happy.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_2_body.png",(0,0), "images/sprites/close/sl/sl_2_sport.png",(0,0), "images/sprites/close/sl/sl_2_happy.png") )
            image un sad dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_dress.png",(0,0), "images/sprites/close/un/un_2_sad.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_dress.png",(0,0), "images/sprites/close/un/un_2_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_dress.png",(0,0), "images/sprites/close/un/un_2_sad.png") )
            image dv cry pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_pioneer.png",(0,0), "images/sprites/close/dv/dv_1_cry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_pioneer.png",(0,0), "images/sprites/close/dv/dv_1_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_pioneer.png",(0,0), "images/sprites/close/dv/dv_1_cry.png") )
            image sl angry swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_swim.png",(0,0), "images/sprites/close/sl/sl_3_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_swim.png",(0,0), "images/sprites/close/sl/sl_3_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_swim.png",(0,0), "images/sprites/close/sl/sl_3_angry.png") )
            image un rage dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_dress.png",(0,0), "images/sprites/close/un/un_3_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_dress.png",(0,0), "images/sprites/close/un/un_3_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_dress.png",(0,0), "images/sprites/close/un/un_3_rage.png") )
            image us normal dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_dress.png",(0,0), "images/sprites/close/us/us_1_normal.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_dress.png",(0,0), "images/sprites/close/us/us_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_1_body.png",(0,0), "images/sprites/close/us/us_1_dress.png",(0,0), "images/sprites/close/us/us_1_normal.png") )
            image sl angry sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_sport.png",(0,0), "images/sprites/close/sl/sl_3_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_sport.png",(0,0), "images/sprites/close/sl/sl_3_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/sl/sl_3_body.png",(0,0), "images/sprites/close/sl/sl_3_sport.png",(0,0), "images/sprites/close/sl/sl_3_angry.png") )
            image us fear pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_pioneer.png",(0,0), "images/sprites/close/us/us_2_fear.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_pioneer.png",(0,0), "images/sprites/close/us/us_2_fear.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_pioneer.png",(0,0), "images/sprites/close/us/us_2_fear.png") )
            image mt normal panama dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_panama.png",(0,0), "images/sprites/close/mt/mt_1_normal.png",(0,0), "images/sprites/close/mt/mt_1_dress.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_panama.png",(0,0), "images/sprites/close/mt/mt_1_normal.png",(0,0), "images/sprites/close/mt/mt_1_dress.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_1_body.png",(0,0), "images/sprites/close/mt/mt_1_panama.png",(0,0), "images/sprites/close/mt/mt_1_normal.png",(0,0), "images/sprites/close/mt/mt_1_dress.png") )
            image mi serious pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_3_body.png",(0,0), "images/sprites/close/mi/mi_3_pioneer.png",(0,0), "images/sprites/close/mi/mi_3_serious.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_3_body.png",(0,0), "images/sprites/close/mi/mi_3_pioneer.png",(0,0), "images/sprites/close/mi/mi_3_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_3_body.png",(0,0), "images/sprites/close/mi/mi_3_pioneer.png",(0,0), "images/sprites/close/mi/mi_3_serious.png") )
            image un shocked pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_pioneer.png",(0,0), "images/sprites/close/un/un_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_pioneer.png",(0,0), "images/sprites/close/un/un_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_pioneer.png",(0,0), "images/sprites/close/un/un_2_shocked.png") )
            image dv grin pioneer2 close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_2_body.png",(0,0), "images/sprites/close/dv/dv_2_pioneer2.png",(0,0), "images/sprites/close/dv/dv_2_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_2_body.png",(0,0), "images/sprites/close/dv/dv_2_pioneer2.png",(0,0), "images/sprites/close/dv/dv_2_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_2_body.png",(0,0), "images/sprites/close/dv/dv_2_pioneer2.png",(0,0), "images/sprites/close/dv/dv_2_grin.png") )
            image dv grin pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_2_body.png",(0,0), "images/sprites/close/dv/dv_2_pioneer.png",(0,0), "images/sprites/close/dv/dv_2_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_2_body.png",(0,0), "images/sprites/close/dv/dv_2_pioneer.png",(0,0), "images/sprites/close/dv/dv_2_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_2_body.png",(0,0), "images/sprites/close/dv/dv_2_pioneer.png",(0,0), "images/sprites/close/dv/dv_2_grin.png") )
            image mt rage dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_2_body.png",(0,0), "images/sprites/close/mt/mt_2_dress.png",(0,0), "images/sprites/close/mt/mt_2_rage.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_2_body.png",(0,0), "images/sprites/close/mt/mt_2_dress.png",(0,0), "images/sprites/close/mt/mt_2_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_2_body.png",(0,0), "images/sprites/close/mt/mt_2_dress.png",(0,0), "images/sprites/close/mt/mt_2_rage.png") )
            image us angry sport close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_sport.png",(0,0), "images/sprites/close/us/us_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_sport.png",(0,0), "images/sprites/close/us/us_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_sport.png",(0,0), "images/sprites/close/us/us_2_angry.png") )
            image mi grin swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_2_body.png",(0,0), "images/sprites/close/mi/mi_2_swim.png",(0,0), "images/sprites/close/mi/mi_2_grin.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_2_body.png",(0,0), "images/sprites/close/mi/mi_2_swim.png",(0,0), "images/sprites/close/mi/mi_2_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_2_body.png",(0,0), "images/sprites/close/mi/mi_2_swim.png",(0,0), "images/sprites/close/mi/mi_2_grin.png") )
            image mt angry swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_2_body.png",(0,0), "images/sprites/close/mt/mt_2_swim.png",(0,0), "images/sprites/close/mt/mt_2_angry.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_2_body.png",(0,0), "images/sprites/close/mt/mt_2_swim.png",(0,0), "images/sprites/close/mt/mt_2_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mt/mt_2_body.png",(0,0), "images/sprites/close/mt/mt_2_swim.png",(0,0), "images/sprites/close/mt/mt_2_angry.png") )
            image un surprise swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_swim.png",(0,0), "images/sprites/close/un/un_2_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_swim.png",(0,0), "images/sprites/close/un/un_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_swim.png",(0,0), "images/sprites/close/un/un_2_surprise.png") )
            image el shocked pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/el/el_2_body.png",(0,0), "images/sprites/close/el/el_2_pioneer.png",(0,0), "images/sprites/close/el/el_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/el/el_2_body.png",(0,0), "images/sprites/close/el/el_2_pioneer.png",(0,0), "images/sprites/close/el/el_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/el/el_2_body.png",(0,0), "images/sprites/close/el/el_2_pioneer.png",(0,0), "images/sprites/close/el/el_2_shocked.png") )
            image us calml dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_dress.png",(0,0), "images/sprites/close/us/us_2_calml.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_dress.png",(0,0), "images/sprites/close/us/us_2_calml.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_2_body.png",(0,0), "images/sprites/close/us/us_2_dress.png",(0,0), "images/sprites/close/us/us_2_calml.png") )
            image us surp3 dress close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_dress.png",(0,0), "images/sprites/close/us/us_3_surp3.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_dress.png",(0,0), "images/sprites/close/us/us_3_surp3.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/us/us_3_body.png",(0,0), "images/sprites/close/us/us_3_dress.png",(0,0), "images/sprites/close/us/us_3_surp3.png") )
            image un smile swim close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_swim.png",(0,0), "images/sprites/close/un/un_1_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_swim.png",(0,0), "images/sprites/close/un/un_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_swim.png",(0,0), "images/sprites/close/un/un_1_smile.png") )
            image mi surprise pioneer close = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_pioneer.png",(0,0), "images/sprites/close/mi/mi_1_surprise.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_pioneer.png",(0,0), "images/sprites/close/mi/mi_1_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((700,720), (0,0), "images/sprites/close/mi/mi_1_body.png",(0,0), "images/sprites/close/mi/mi_1_pioneer.png",(0,0), "images/sprites/close/mi/mi_1_surprise.png") )
            image mt shocked pioneer = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_pioneer.png",(0,0), "images/sprites/normal/mt/mt_2_shocked.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_pioneer.png",(0,0), "images/sprites/normal/mt/mt_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/mt/mt_2_body.png",(0,0), "images/sprites/normal/mt/mt_2_pioneer.png",(0,0), "images/sprites/normal/mt/mt_2_shocked.png") )
    
            image un normal body = im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) )
            image un smile body = im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) )
            image un shy body = im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) )
            image un surprise body = im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) )
            image un angry body = im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) )
            image un angry2 body = im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_angry2.png"), im.matrix.tint(0.63, 0.78, 0.82) )
            image un cry body = im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) )
            image un grin body = im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) )
            image un laugh body = im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) )
            image un rage body = im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) )
            image un scared body = im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) )
            image un shocked body = im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) )
            image un smile2 body = im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) )
            image un smile3 body = im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_smile3.png"), im.matrix.tint(0.63, 0.78, 0.82) )
            image un sad body = im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) )
            image un evil_smile body = im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_1_body.png",(0,0), "images/sprites/normal/un/un_1_evil_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) )
            image un cry_smile body = im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_2_body.png",(0,0), "images/sprites/normal/un/un_2_cry_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) )
            image un serious body = im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/un/un_3_body.png",(0,0), "images/sprites/normal/un/un_3_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) )
            image un normal body close = im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_normal.png"), im.matrix.tint(0.63, 0.78, 0.82) )
            image un smile body close = im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) )
            image un shy body close = im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_shy.png"), im.matrix.tint(0.63, 0.78, 0.82) )
            image un surprise body close = im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_surprise.png"), im.matrix.tint(0.63, 0.78, 0.82) )
            image un angry body close = im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_angry.png"), im.matrix.tint(0.63, 0.78, 0.82) )
            image un angry2 body close = im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_angry2.png"), im.matrix.tint(0.63, 0.78, 0.82) )
            image un cry body close = im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_cry.png"), im.matrix.tint(0.63, 0.78, 0.82) )
            image un grin body close = im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_grin.png"), im.matrix.tint(0.63, 0.78, 0.82) )
            image un laugh body close = im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_laugh.png"), im.matrix.tint(0.63, 0.78, 0.82) )
            image un rage body close = im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_rage.png"), im.matrix.tint(0.63, 0.78, 0.82) )
            image un scared body close = im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_scared.png"), im.matrix.tint(0.63, 0.78, 0.82) )
            image un shocked body close = im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_shocked.png"), im.matrix.tint(0.63, 0.78, 0.82) )
            image un smile2 body close = im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_smile2.png"), im.matrix.tint(0.63, 0.78, 0.82) )
            image un smile3 body close = im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_smile3.png"), im.matrix.tint(0.63, 0.78, 0.82) )
            image un sad body close = im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_sad.png"), im.matrix.tint(0.63, 0.78, 0.82) )
            image un evil_smile body close = im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_1_body.png",(0,0), "images/sprites/close/un/un_1_evil_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) )
            image un cry_smile body close = im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_2_body.png",(0,0), "images/sprites/close/un/un_2_cry_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) )
            image un serious body close = im.MatrixColor( im.Composite((700,720), (0,0), "images/sprites/close/un/un_3_body.png",(0,0), "images/sprites/close/un/un_3_serious.png"), im.matrix.tint(0.63, 0.78, 0.82) )
            image dv scared body = im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0),  "images/sprites/normal/dv/dv_1_scared.png")
            image dv sad body = im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_3_body.png",(0,0), "images/sprites/normal/dv/dv_3_sad.png")
            image dv guilty body = im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_3_body.png",(0,0), "images/sprites/normal/dv/dv_3_guilty.png")
            image dv laugh body = im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_4_body.png",(0,0),  "images/sprites/normal/dv/dv_4_laugh.png")
            image dv shy body = im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_3_body.png",(0,0), "images/sprites/normal/dv/dv_3_shy.png")
            image dv smile body = im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_4_body.png",(0,0), "images/sprites/normal/dv/dv_4_smile.png")
            image dv shocked body = im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_shocked.png")
            image dv rage body = im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_5_body.png",(0,0), "images/sprites/normal/dv/dv_5_rage.png")
            image dv normal body = im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_4_body.png",(0,0), "images/sprites/normal/dv/dv_4_normal.png")
            image dv angry body = im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_5_body.png",(0,0), "images/sprites/normal/dv/dv_5_angry.png")
            image dv surprise body = im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_surprise.png")
            image dv cry body = im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_1_body.png",(0,0), "images/sprites/normal/dv/dv_1_cry.png")
            image dv grin body = im.Composite((600,720), (0,0), "images/sprites/normal/dv/dv_2_body.png",(0,0), "images/sprites/normal/dv/dv_2_grin.png")
            image dv scared body close = im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_scared.png")
            image dv sad body close = im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_3_body.png",(0,0), "images/sprites/close/dv/dv_3_sad.png")
            image dv guilty body close = im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_3_body.png",(0,0), "images/sprites/close/dv/dv_3_guilty.png")
            image dv laugh body close = im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_4_body.png",(0,0), "images/sprites/close/dv/dv_4_laugh.png")
            image dv shy body close = im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_3_body.png",(0,0), "images/sprites/close/dv/dv_3_shy.png")
            image dv smile body close = im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_4_body.png",(0,0), "images/sprites/close/dv/dv_4_smile.png")
            image dv shocked body close = im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_shocked.png")
            image dv rage body close = im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_5_body.png",(0,0), "images/sprites/close/dv/dv_5_rage.png")
            image dv normal body close = im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_4_body.png",(0,0),  "images/sprites/close/dv/dv_4_normal.png")
            image dv angry body close = im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_5_body.png",(0,0), "images/sprites/close/dv/dv_5_angry.png")
            image dv surprise body close = im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0),"images/sprites/close/dv/dv_1_surprise.png")
            image dv cry body close = im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_1_body.png",(0,0), "images/sprites/close/dv/dv_1_cry.png")
            image dv grin body close = im.Composite((700,720), (0,0), "images/sprites/close/dv/dv_2_body.png",(0,0), "images/sprites/close/dv/dv_2_grin.png")
            image pi smile = ConditionSwitch(
            "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/pi/pi_1_pioneer_smile.png"), im.matrix.tint(0.94, 0.82, 1.0) ),
            "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((600,720), (0,0), "images/sprites/normal/pi/pi_1_pioneer_smile.png"), im.matrix.tint(0.63, 0.78, 0.82) ),
            True,im.Composite((600,720), (0,0), "images/sprites/normal/pi/pi_1_pioneer_smile.png") )
