import psycopg2
conn = psycopg2.connect(dbname='tg_to_web_db', user='postgres', password='postgres', host='localhost')
cursor = conn.cursor()
