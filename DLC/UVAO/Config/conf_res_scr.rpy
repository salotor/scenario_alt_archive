init -999 python:
    def get_image_uvao_7dl(file):
        return default_7dl_path+"DLC/UVAO/Pics/%s" % (file)

init -998 python:
    def get_sfx_uvao_7dl(file):
        return default_7dl_path+"DLC/UVAO/Sound/sfx/%s" % (file)
    def get_music_uvao_7dl(file):
        return default_7dl_path+"DLC/UVAO/Sound/music/%s" % (file)
