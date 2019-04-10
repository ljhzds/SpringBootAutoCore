# coding: utf-8
from read_config_excel import read_app_config
from secret_remote import JDBC_URL, DB_DRIVER, DB_PASSWD, DB_USER

# 工程名
APP_NAME = 'pySpringAutoDemo'
API_VERSION = 'v1'
# 工程包名
APP_GROUP_ID = 'com.zhangdesheng'
APP_ART_ID = 'autodemo'
APP_PACKAGE_NAME = 'com.zhangdesheng.autodemo'
APP_DESC = 'python generator demo'
# 工程保存目录
CODE_SAVE_ROOT = 'C:\\spring_learning\\'
CODE_SAVE_ROOT_TMP = '/tmp/springauto/'
# CODE_SAVE_ROOT_TMP = CODE_SAVE_ROOT

SPRINGBOOT_VERSION = '1.5.19.RELEASE'
JAVA_VERSION = '1.8'


def get_all_config(desc_excel_file_path=None, is_web_app=False):
    default_config = {k: v for k, v in globals().items() if k == k.upper()}
    print(read_app_config(desc_excel_file_path))
    default_config.update(read_app_config(desc_excel_file_path))

    if is_web_app:
        default_config.update({'CODE_SAVE_ROOT': CODE_SAVE_ROOT_TMP})

    return default_config


if __name__ == '__main__':
    print(get_all_config())
