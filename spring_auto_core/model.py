# coding: utf-8
import os
from .utils import tablename_to_classname, columnname_to_valname


def gen_model(tables, config):
    locals().update(config)
    CODE_SAVE_ROOT = config.get('CODE_SAVE_ROOT')
    APP_NAME = config.get('APP_NAME')
    APP_PACKAGE_NAME = config.get('APP_PACKAGE_NAME')
    model_file_save_root = os.path.join(os.path.join(CODE_SAVE_ROOT, APP_NAME), 'src', 'spring_gen', 'java',
                                        *APP_PACKAGE_NAME.split('.'), 'model')
    for table_info in tables:
        table, column_list = table_info
        classname = tablename_to_classname(table.name)
        with open(os.path.join(model_file_save_root, classname + '.java'), 'w', encoding='utf-8') as f:
            f.write('package {}.model;\n'.format(APP_PACKAGE_NAME))
            f.write('public class {} {{\n\n'.format(classname))

            for col in column_list:
                f.write('    private {} {};\n'.format(col.java_data_type, columnname_to_valname(col.name)))
            f.write('\n')
            for col in column_list:
                valname = columnname_to_valname(col.name)
                f.write(
                    ' ' * 4 + 'public {} get{}() {{\n'.format(col.java_data_type, valname[0].upper() + valname[1:]) +
                    ' ' * 8 + 'return {};\n'.format(valname) + ' ' * 4 + '}\n\n')
                f.write(
                    ' ' * 4 + 'public void set{}({} {}) {{\n'.format(valname[0].upper() + valname[1:],
                                                                     col.java_data_type,
                                                                     valname) +
                    ' ' * 8 + 'this.{} = {};\n'.format(valname, valname) + ' ' * 4 + '}\n\n')
            f.write('}\n')


if __name__ == '__main__':
    pass
