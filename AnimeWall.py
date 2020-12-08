import random
import os
import time
import sys
import ctypes
from win10toast import ToastNotifier

def main():
    try:
        imagens = os.listdir(os.chdir('images'))
        while True:
            background = random.choice(imagens)
            background = os.path.realpath(background)
            ctypes.windll.user32.SystemParametersInfoW(20, 0, r'%s' % (background) , 3)
            time.sleep(8200)
    except FileNotFoundError:
        path_local = os.getcwd()
        msg = "A pasta 'images' contento papeis de parede não foi encontrada ao lado do aplicativo em execução: %s" % (path_local)
        popup = ctypes.windll.user32.MessageBoxW(0, msg, "ANIME WALLPAPER", 2)
        if popup == 4:
            main()
        else:
            sys.exit()
    except IndexError:
        popup = ctypes.windll.user32.MessageBoxW(0, "A pasta 'images' não contém imagens para ser usadas.", "ANIME WALLPAPER", 1)
    except:
        popup = ctypes.windll.user32.MessageBoxW(0, "Não foi possivel iniciar devido a um erro desconhecido.", "ANIME WALLPAPER", 1)

if __name__ == '__main__':
    main()
