import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(user='postgres', password='postgres', host='localhost')
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = conn.cursor()
cursor.execute('SELECT \'CREATE DATABASE mydb\' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = \'mydb\');') #may already exist if dbdrop.py used
cursor.execute('create table users ( usr varchar(20) not null primary key, password varchar(20) not null );')
cursor.execute('insert into users (usr, password) values (\'Andruxa\', \'yopta\');')

cursor.execute('create table user_chat ( usr varchar(20) references users(usr), id bigint not null );')
cursor.execute('insert into user_chat (usr, id) values (\'Andruxa\', \'-1001539495622\'), (\'Andruxa\', \'-1001589621629\')') #ids of two test chats
