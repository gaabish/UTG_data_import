import psycopg2
from Classes.code import *
from Classes.code_tree import *
from Classes.code_tree_root import *
from Classes.сode_transaction import *

with open(input('Путь к файлу (включая наименование файла и его расширение) с параметрами подключения: '),
          'r', encoding='utf8') as file_connection:
    reader = file_connection.readlines()
    props = dict()
    for r in reader:
        reader.index(r)
        prop = (r.split('=')[0], r.split('=')[1].strip())
        props[prop[0]] = prop[1]
    conn = psycopg2.connect(dbname=props['dbname'], user=props['user'],
                            password=props['password'], host=props['host'],
                            port=props['port'])
with open(input('Путь к файлу (включая наименование файла и его расширение) с данными для импорта: '),
          'r', encoding='utf8') as file_data:
    reader = file_data.readlines()
    for r in range(1, len(reader)):
        line_data = reader[r].strip().split(';')
        code = create_code_from_line(line_data)
        code_transaction = create_code_transaction_from_line(line_data, code)
        code_tree_root = create_code_tree_root_from_line(line_data, code, code_transaction)
        code_tree = create_code_tree_from_line(code)
        cursor = conn.cursor()
        cursor.execute(code.prepare_to_insert())
        cursor.execute(code_tree.prepare_to_insert())
        cursor.execute(code_transaction.prepare_to_insert())
        cursor.execute(code_tree_root.prepare_to_insert())
        conn.commit()
        cursor.execute('SELECT COUNT(*) FROM core.code')
        print('Записей в таблице код {r}'.format(r=cursor.fetchone()))
        cursor.close()
    conn.close()
