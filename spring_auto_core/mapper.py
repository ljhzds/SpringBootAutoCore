# coding: utf-8
import os

from .utils import tablename_to_classname, get_jinja_env


def colname_to_sqlcondition(col_java_name):
    # written on: {{ article.pub_date|datetimeformat }}
    return '#{{{}}}'.format(col_java_name)


def gen_mapper_xml(tables, config):
    locals().update(config)
    CODE_SAVE_ROOT = config.get('CODE_SAVE_ROOT')
    APP_NAME = config.get('APP_NAME')
    APP_PACKAGE_NAME = config.get('APP_PACKAGE_NAME')
    xml_save_root = os.path.join(CODE_SAVE_ROOT, APP_NAME, 'src', 'spring_gen', 'resources', 'mapper')

    env = get_jinja_env()
    env.filters['colcondition'] = colname_to_sqlcondition

    template = env.get_template('mapper.xml')

    for table_info in tables:
        table, column_list = table_info
        classname = tablename_to_classname(table.name)
        model_class_name = APP_PACKAGE_NAME + '.model.' + classname
        namespace = APP_PACKAGE_NAME + '.dao.' + classname + 'Dao'

        columns_str = ', '.join([col.name for col in column_list])
        columns_java_str = ', '.join([colname_to_sqlcondition(col.java_name) for col in column_list])

        key_data_type = 'java.lang.Long'
        key_col_name = 'id'
        key_col_valname = '#{id}'

        for col in column_list:
            if col.is_key == 'Y':
                key_col_name = col.name
                key_col_valname = colname_to_sqlcondition(col.java_name)
                if col.java_data_type == 'String':
                    key_data_type = 'java.lang.String'
                elif col.java_data_type == 'long':
                    key_data_type = 'java.lang.Long'
                elif col.java_data_type == 'int':
                    key_data_type = 'java.lang.Integer'
                else:
                    key_data_type = 'java.lang.String'

        with open(os.path.join(xml_save_root, classname + 'Mapper.xml'), 'w', encoding='utf-8') as f:
            f.write(template.render(**locals()))


if __name__ == '__main__':
    gen_mapper_xml()
