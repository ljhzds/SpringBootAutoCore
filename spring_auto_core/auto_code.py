# coding: utf-8
import os

from spring_auto_core.load_config import get_all_config
from spring_auto_core.read_config_excel import get_tables
from spring_auto_core.directory import create_app_directory
from spring_auto_core.init_create_sql import init
from spring_auto_core.model import gen_model
from spring_auto_core.mapper import gen_mapper_xml
from spring_auto_core.dao import gen_dao
from spring_auto_core.service_and_controller import gen_service_and_controller
from spring_auto_core.properties_pom import gen_configs_and_mainclass


def spring_gen(config_xlsx_path):
    # print(1111, sys.argv)
    print(f"开始根据配置文件：【{config_xlsx_path}】生成基于springboot的web工程代码!")
    # config_excel_filename = 'C:\\Users\\13676\\PycharmProjects\\pyDailyScripts\\spring_helper\\templates\\tables.xlsx'
    config_excel_filename = config_xlsx_path
    # 获取配置
    config = get_all_config(config_excel_filename)
    code_save_path = os.path.join(config.get('CODE_SAVE_ROOT'), config.get('APP_NAME'))
    print("基于springboot的web工程代码将保存在：【{}】目录下!".format(code_save_path))

    # 生成目录结构
    print("开始生成目录结构...")
    create_app_directory(config.get('APP_PACKAGE_NAME'),
                         os.path.join(config.get('CODE_SAVE_ROOT'), config.get('APP_NAME')))
    # 生成建表语句
    print("开始生成建表语句...")
    tables = get_tables(config_excel_filename)
    init(tables, config)
    # 生成mapper.xml
    print("开始生成mapper.xml...")
    gen_mapper_xml(tables, config)
    # 生成 models
    print("开始生成models...")
    gen_model(tables, config)
    # 生成 dao
    print("开始生成dao...")
    gen_dao(tables, config)
    # 生成 service serviceImpl controller
    print("开始生成 service serviceImpl controller...")
    gen_service_and_controller(tables, config)
    # 生成 pom.xml application.properties spring_gen class
    print("生成 pom.xml application.properties 和 spring_gen class...")
    gen_configs_and_mainclass(config)
    print("基于springboot的web工程代码生成完毕，代码保存在：【{}】目录下!".format(code_save_path))

    return code_save_path


if __name__ == '__main__':
    spring_gen('')
