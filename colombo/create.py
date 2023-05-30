from connect import cursor, data_base


def create(tabela, modelo, valor):
    sql = f'''INSERT INTO {tabela} (modelo, valor)
    values ("{modelo}", "{valor}")'''
    cursor.execute(sql)
    data_base.commit()

def delete():
    sql = f'''DROP TABLE IF EXISTS Samsung, Motorola, Nokia, Apple, Xiaomi'''
    cursor.execute(sql)
    data_base.commit()


def criar_tabela(tabela):
    sql = f'''create table {tabela} (
    id_celular int auto_increment primary key,
    modelo varchar(250),
    valor varchar(250)
    );'''
    cursor.execute(sql)
    data_base.commit()