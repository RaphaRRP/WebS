data_base = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='colombo'
)

pip install mysql-connector-python
pip install requests
pip install beautifulsoup4
pip install inquirer
pip install pandas





create database colombo;

use colombo;

create table colombo.samsung (
    id_celular int auto_increment primary key,
    modelo varchar(250),
    valor varchar(250)
);

create table colombo.motorola (
    id_celular int auto_increment primary key,
    modelo varchar(250),
    valor varchar(250)
);

create table colombo.nokia (
    id_celular int auto_increment primary key,
    modelo varchar(250),
    valor varchar(250)
);
create table colombo.iphone (
    id_celular int auto_increment primary key,
    modelo varchar(250),
    valor varchar(250)
);

create table colombo.xiaomi (
    id_celular int auto_increment primary key,
    modelo varchar(250),
    valor varchar(250)
);