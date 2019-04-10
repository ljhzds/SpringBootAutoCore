# coding: utf-8
import os
from utils import get_jinja_env


def gen_configs_and_mainclass(config):
    locals().update(config)
    CODE_SAVE_ROOT = config.get('CODE_SAVE_ROOT')
    APP_NAME = config.get('APP_NAME')
    APP_PACKAGE_NAME = config.get('APP_PACKAGE_NAME')
    env = get_jinja_env()

    properties_filename = os.path.join(CODE_SAVE_ROOT, APP_NAME, 'src', 'spring_gen', 'resources', 'application.properties')
    mybatis_config_filename = os.path.join(CODE_SAVE_ROOT, APP_NAME, 'src', 'spring_gen', 'resources', 'mybatis-config.xml')

    application_java_filename = os.path.join(CODE_SAVE_ROOT, APP_NAME, 'src', 'spring_gen', 'java',
                                             *APP_PACKAGE_NAME.split('.'), APP_NAME + 'Application.java')
    pom_xml_filename = os.path.join(CODE_SAVE_ROOT, APP_NAME, 'pom.xml')

    with open(properties_filename, 'w', encoding='utf-8') as f:
        template = env.get_template('application.properties')
        f.write(template.render(**locals()))

    with open(mybatis_config_filename, 'w', encoding='utf-8') as f:
        template = env.get_template('mybatis-config.xml')
        f.write(template.render(**locals()))

    with open(application_java_filename, 'w', encoding='utf-8') as f:
        template = env.get_template('application.javatl')
        f.write(template.render(**locals()))

    with open(pom_xml_filename, 'w', encoding='utf-8') as f:
        template = env.get_template('pom.xml')
        f.write(template.render(**locals()))
