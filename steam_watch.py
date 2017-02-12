import platform
import os
import subprocess
import time
import math
from os.path import join, getsize

interval_sec = 60

default_dirs = [
    'C:\\Program Files (x86)\\Steam\\steamapps\\downloading',
    'E:\\Games\\SteamLibrary\\steamapps\\downloading'
]


def get_dir_size(path):
    total = 0
    for root, dirs, files in os.walk(path):
        for name in files:
            total += getsize(join(root, name))
    return total


def shutdown():
    plat = platform.system()
    print('Shutting down...')

    if plat is 'Windows':
        subprocess.call(['shutdown', '/s'])
    elif plat is 'Linux':
        subprocess.call(['shutdown', '-h', 'now'])


def loop(path, is_downloading=True):
    if(is_downloading):
        time.sleep(interval_sec)
        size = get_dir_size(path)
        if size != 0:
            print('Still downloading... current size: {} GB'
                  .format(round(size / math.pow(1024, 3), 2)))
            loop(path)
        else:
            print('Download finished!')
            shutdown()


def prompt():
    choice = int(input('\n\t[1] C:\SteamApps\n\t[2] E:\SteamApps\n\t[3] Other\n\nPick a number: '))

    if choice is 3:
        path = input('\nDirectory to watch: ')
    else:
        path = default_dirs[choice - 1]

    print('Watching directory: {}'.format(path))
    loop(path)


prompt()
