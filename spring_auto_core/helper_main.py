# coding: utf-8
import os, sys

import click

from load_config import get_all_config
from read_config_excel import get_tables
from directory import create_app_directory
from init_create_sql import init
from model import gen_model
from mapper import gen_mapper_xml
from dao import gen_dao
from service_and_controller import gen_service_and_controller
from properties_pom import gen_configs_and_mainclass


@click.command()
@click.argument('config_xlsx_path', type=click.Path(exists=True))
def spring_gen(config_xlsx_path):
    # click.echo(1111, sys.argv)
    click.echo(f"开始根据配置文件：【{config_xlsx_path}】生成基于springboot的web工程代码!")
    # config_excel_filename = 'C:\\Users\\13676\\PycharmProjects\\pyDailyScripts\\spring_helper\\templates\\tables.xlsx'
    config_excel_filename = config_xlsx_path
    # 获取配置
    config = get_all_config(config_excel_filename)
    code_save_path = os.path.join(config.get('CODE_SAVE_ROOT'), config.get('APP_NAME'))
    click.echo("基于springboot的web工程代码将保存在：【{}】目录下!".format(code_save_path))

    # 生成目录结构
    click.echo("开始生成目录结构...")
    create_app_directory(config.get('APP_PACKAGE_NAME'),
                         os.path.join(config.get('CODE_SAVE_ROOT'), config.get('APP_NAME')))
    # 生成建表语句
    click.echo("开始生成建表语句...")
    tables = get_tables(config_excel_filename)
    init(tables, config)
    # 生成mapper.xml
    click.echo("开始生成mapper.xml...")
    gen_mapper_xml(tables, config)
    # 生成 models
    click.echo("开始生成models...")
    gen_model(tables, config)
    # 生成 dao
    click.echo("开始生成dao...")
    gen_dao(tables, config)
    # 生成 service serviceImpl controller
    click.echo("开始生成 service serviceImpl controller...")
    gen_service_and_controller(tables, config)
    # 生成 pom.xml application.properties spring_gen class
    click.echo("生成 pom.xml application.properties 和 spring_gen class...")
    gen_configs_and_mainclass(config)
    click.echo("基于springboot的web工程代码生成完毕，代码保存在：【{}】目录下!".format(code_save_path))

    return code_save_path


if __name__ == '__main__':
    import sys

    # print(sys.argv)
    sys.argv.append('C:\\Users\\13676\\PycharmProjects\\pyDailyScripts\\spring_helper\\templates\\tables.xlsx')
    spring_gen()
