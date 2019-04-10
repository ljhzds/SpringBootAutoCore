# coding: utf-8
import os


# from load_config import APP_NAME, CODE_SAVE_ROOT


def init(tables, config):
    APP_NAME = config.get('APP_NAME')
    CODE_SAVE_ROOT = config.get('CODE_SAVE_ROOT')
    sql_save_root = os.path.join(CODE_SAVE_ROOT, APP_NAME)
    with open(os.path.join(sql_save_root, 'init.sql'), 'w', encoding='utf-8') as fw:
        for table_info in tables:
            table, column_list = table_info
            fw.write('-- {}-{} 建表\n'.format(table.name, table.cn_name))
            fw.write('CREATE TABLE `{}` (\n'.format(table.name))
            for col in column_list:
                col_str = '  `{}` {}({}) '.format(col.name, col.data_type, col.length)
                col_str += 'DEFAULT NULL,\n' if col.is_allow_null == 'Y' else 'NOT NULL,\n'
                fw.write(col_str)
            for col in column_list:
                if col.is_key == 'Y':
                    fw.write('  PRIMARY KEY (`{}`)\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ;\n\n'.format(col.name))


def mock_data(tables):
    import random, string
    ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))
    for table_info in tables:
        table, column_list = table_info
