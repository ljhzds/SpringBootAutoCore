# coding: utf-8
import os

from utils import tablename_to_classname, get_jinja_env


def cover_mess(s):
    return '{' + s + '}'


def gen_service_and_controller(tables, config):
    CODE_SAVE_ROOT = config.get('CODE_SAVE_ROOT')
    APP_NAME = config.get('APP_NAME')
    APP_PACKAGE_NAME = config.get('APP_PACKAGE_NAME')
    locals().update(config)

    service_save_root = os.path.join(CODE_SAVE_ROOT, APP_NAME, 'src', 'spring_gen', 'java',
                                     *APP_PACKAGE_NAME.split('.'), 'service')
    controller_save_root = os.path.join(CODE_SAVE_ROOT, APP_NAME, 'src', 'spring_gen', 'java',
                                        *APP_PACKAGE_NAME.split('.'), 'controller')
    service_imp_save_root = os.path.join(service_save_root, 'impl')
    env = env = get_jinja_env()
    env.filters['cover_mess'] = cover_mess
    template = env.get_template('service.javatl')
    template_impl = env.get_template('serviceImpl.javatl')
    template_controller = env.get_template('controller.javatl')
    for table_info in tables:
        table, column_list = table_info
        classname = tablename_to_classname(table.name) + 'Service'
        controller_classname = tablename_to_classname(table.name) + 'RestController'
        model_class_name = tablename_to_classname(table.name)
        instance_name = model_class_name[0].lower() + model_class_name[1:]
        key = 'id'
        pkey = 'id'
        key_type = 'Long'
        for col in column_list:
            if col.is_key == 'Y':
                pkey = col.java_name
                key = col.name
                key_type = col.java_data_type
                break
        with open(os.path.join(service_save_root, classname + '.java'), 'w', encoding='utf-8') as f:
            f.write(template.render(**locals()))

        with open(os.path.join(service_imp_save_root, classname + 'Impl.java'), 'w', encoding='utf-8') as f:
            f.write(template_impl.render(**locals()))

        with open(os.path.join(controller_save_root, controller_classname + '.java'), 'w', encoding='utf-8') as f:
            f.write(template_controller.render(**locals()))
