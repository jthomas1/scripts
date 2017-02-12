import platform
import os
import subprocess
import time
import math
from os.path import join, getsize

interval_sec = 60

# items in dirs appear in the menu as quick options
# leave the list empty to skip options and input manually

dirs = [
    {
        'name': 'C:\\SteamLibrary',
        'path': 'C:\\Program Files (x86)\\Steam\\steamapps\\downloading'
    },
    {
        'name': 'E:\\SteamLibrary',
        'path': 'E:\\Games\\SteamLibrary\\steamapps\\downloading'
    }
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


def wait(path, is_downloading=True):
    if(is_downloading):
        time.sleep(interval_sec)
        size = get_dir_size(path)
        if size != 0:
            print('Still downloading... current size: {} GB'
                  .format(round(size / math.pow(1024, 3), 2)))
            wait(path)
        else:
            print('Download finished!')
            shutdown()


def custom():
    path = input('\nDirectory to watch: ')

    if os.path.exists(path) and os.path.isdir(path):
        print('Watching directory: {}'.format(path))
        wait(path)
    else:
        print('\n\n\tNot a directory: {}\n\n\tPlease check it exists!'.format(path))
        prompt()


def prompt():
    if len(dirs) == 0:
        custom()
    else:
        msg = '\n\t[0] Custom'

        for key, val in enumerate(dirs):
            msg += '\n\t[{}] {}'.format(key + 1, val['name'])

        msg += '\n\nPick a number: '

        choice = input(msg)

        try:
            choice = int(choice)

            if choice < 0 or choice > len(dirs):
                print('Invalid choice: {}'.format(choice))
                prompt()
            else:
                path = ''
                if choice is 0:
                    custom()
                else:
                    path = dirs[choice - 1]['path']
                    print('Watching directory: {}'.format(path))
                    wait(path)
        except:
            print('\n\n\tInvalid choice: {}\n\nChoose again...'.format(choice))
            prompt()


if __name__ == "__main__":
    prompt()
