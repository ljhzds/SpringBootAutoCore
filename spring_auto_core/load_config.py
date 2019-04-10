# coding: utf-8
from read_config_excel import read_app_config

# 工程名
APP_NAME = 'pySpringAutoDemo'
API_VERSION = 'v1'
# 工程包名
APP_GROUP_ID = 'com.guangfa'
APP_ART_ID = 'autodemo'
APP_PACKAGE_NAME = 'com.guangfa.autodemo'
APP_DESC = 'python generator demo'
# 工程保存目录
CODE_SAVE_ROOT = 'C:\\spring_learning\\'
# CODE_SAVE_ROOT_TMP = '/tmp/springauto/'
CODE_SAVE_ROOT_TMP = CODE_SAVE_ROOT

SPRINGBOOT_VERSION = '1.5.19.RELEASE'
JAVA_VERSION = '1.8'

JDBC_URL = 'jdbc:mysql://119.29.103.193:3306/easyweb?useUnicode=true&characterEncoding=utf8'
DB_USER = 'zdstest'
DB_PASSWD = 'SFD_SF3437lk'
DB_DRIVER = 'com.mysql.jdbc.Driver'


def get_all_config(desc_excel_file_path=None, is_web_app=False):
    default_config = {k: v for k, v in globals().items() if k == k.upper()}
    print(read_app_config(desc_excel_file_path))
    default_config.update(read_app_config(desc_excel_file_path))

    if is_web_app:
        default_config.update({'CODE_SAVE_ROOT': CODE_SAVE_ROOT_TMP})

    return default_config


if __name__ == '__main__':
    print(get_all_config())
