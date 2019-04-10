# coding: utf-8
import os
import pathlib

from load_config import APP_NAME, CODE_SAVE_ROOT, APP_PACKAGE_NAME


def create_app_directory(app_package_name, save_root):
    p = os.path.join(save_root, 'src', 'spring_gen', 'java', *app_package_name.split('.'))
    pathlib.Path(p).mkdir(parents=True, exist_ok=True)

    for s in ('controller', 'dao', 'model', 'service'):
        pathlib.Path(os.path.join(p, s)).mkdir(parents=True, exist_ok=True)
        if s == 'service':
            pathlib.Path(os.path.join(p, s, 'impl')).mkdir(parents=True, exist_ok=True)

    p = os.path.join(save_root, 'src', 'spring_gen', 'resources', 'mapper')
    pathlib.Path(p).mkdir(parents=True, exist_ok=True)

    p = os.path.join(save_root, 'src', 'test', 'java', *app_package_name.split('.'))
    pathlib.Path(p).mkdir(parents=True, exist_ok=True)

    p = os.path.join(save_root, 'target')
    pathlib.Path(p).mkdir(parents=True, exist_ok=True)


if __name__ == '__main__':
    create_app_directory(APP_PACKAGE_NAME, os.path.join(CODE_SAVE_ROOT, APP_NAME))
