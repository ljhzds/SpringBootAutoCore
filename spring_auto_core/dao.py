# coding: utf-8
import os
from utils import tablename_to_classname


def gen_dao(tables, config):
    locals().update(config)
    CODE_SAVE_ROOT = config.get('CODE_SAVE_ROOT')
    APP_NAME = config.get('APP_NAME')
    APP_PACKAGE_NAME = config.get('APP_PACKAGE_NAME')
    dao_file_save_root = os.path.join(os.path.join(CODE_SAVE_ROOT, APP_NAME), 'src', 'spring_gen', 'java',
                                      *APP_PACKAGE_NAME.split('.'), 'dao')

    for table_info in tables:
        table, column_list = table_info

        classname = tablename_to_classname(table.name) + 'Dao'
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
        with open(os.path.join(dao_file_save_root, classname + '.java'), 'w', encoding='utf-8') as f:
            f.write('package {}.dao;\n\n'.format(APP_PACKAGE_NAME))
            f.write(
                'import java.util.List;\nimport org.apache.ibatis.annotations.Param;\nimport {}.model.{};\n\n'.format(
                    APP_PACKAGE_NAME, model_class_name))
            f.write('public interface {} {{\n\n'.format(classname))
            f.write(' ' * 4 + 'List<{model_class_name}> find{model_class_name}s();\n\n'.format(
                model_class_name=model_class_name))
            f.write(
                ' ' * 4 + '{model_class_name} findByKey(@Param("{pkey}") {key_type} {key});\n\n'.format(**locals()));

            f.write(' ' * 4 + '{key_type} save{model_class_name}({model_class_name} {instance_name});\n\n'.format(
                **locals()))

            f.write(' ' * 4 + '{key_type} update{model_class_name}({model_class_name} {instance_name});\n\n'.format(
                **locals()))
            f.write(' ' * 4 + '{key_type} delete{model_class_name}({key_type} {pkey});\n\n'.format(
                **locals()))
            f.write('}\n')


if __name__ == '__main__':
    pass
