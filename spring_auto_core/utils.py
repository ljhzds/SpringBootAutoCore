# coding: utf-8
import os
import tarfile
import jinja2
from jinja2 import Environment, select_autoescape


def tablename_to_classname(table_name):
    words = table_name.split('_')
    classname = ''.join([w[0].upper() + w[1:].lower() for w in words])
    return classname


def columnname_to_valname(table_name):
    words = table_name.split('_')
    valname = ''.join([w[0].upper() + w[1:].lower() for w in words])
    return valname[0].lower() + valname[1:]


def get_jinja_env():
    env = Environment(
        loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
        autoescape=select_autoescape(['xml'])
    )
    return env


def compress_file(tarfilename, dirname):  # tarfilename是压缩包名字，dirname是要打包的目录
    if os.path.isfile(dirname):
        with tarfile.open(tarfilename, 'w') as tar:
            tar.add(dirname)
    else:
        with tarfile.open(tarfilename, 'w') as tar:
            for root, dirs, files in os.walk(dirname):
                for single_file in files:
                    # if single_file != tarfilename:
                    filepath = os.path.join(root, single_file)
                    tar.add(filepath)


if __name__ == '__main__':
    print(tablename_to_classname('pm_tax_branch'))
