"""
@Time    : 2020/5/11 14:24
@Author  : weijiang
@Site    : 
@File    : 数据库操作.py
@Software: PyCharm
"""
import pymysql
host = ''
port = 0
user = ''
password = ''
print('Starting the create database operation, please enter the information required for the database.')
print('------------------------------------')
host = input('please input database host:')
port = input('please input database port:')
user = input('please input database user:')
password = input('please input database password:')
print('------------------------------------')
try:
    conn = pymysql.connect(host=host, port=int(port), user=user, password=password)

    print('create database...')
    cur = conn.cursor()
    cur.execute('create database if not exists book')
    print('database created done.')
    print('------------------------------------')
    conn.select_db('book')

    print('create user table...')
    cur.execute("CREATE TABLE IF NOT EXISTS user ("
                "id varchar(50) PRIMARY KEY,"
                "username varchar(255),"
                "password varchar(255),"
                "role int(11),"
                "create_time datetime,"
                "delete_flag int(11),"
                "current_login_time datetime)")
    print('user table created done.')
    print('------------------------------------')

    print('create book table...')
    cur.execute("CREATE TABLE IF NOT EXISTS book("
                "id varchar(50) PRIMARY KEY,"
                "book_name varchar(255),"
                "author varchar(255),"
                "publish_company varchar(255),"
                "store_number int(11),"
                "borrow_number int(11),"
                "create_time datetime,"
                "publish_date datetime)")
    print('book table created done.')
    print('------------------------------------')

    print('create borrow_info table...')
    cur.execute("CREATE TABLE IF NOT EXISTS borrow_info ("
                "id varchar(50) PRIMARY KEY,"
                "book_id varchar(50),"
                "book_name varchar(255),"
                "borrow_user varchar(255),"
                "borrow_num int(11),"
                "borrow_days int(11),"
                "borrow_time datetime,"
                "return_time datetime,"
                "return_flag int(11))")
    print('borrow_info table created done.')
    print('------------------------------------')

    print('create ask_return table...')
    cur.execute("create table if not exists ask_return ("
                "id int(11) PRIMARY KEY AUTO_INCREMENT NOT NULL,"
                "user_name varchar(50) NOT NULL,"
                "borrow_id varchar(50) NOT NULL,"
                "is_read int(11) NOT NULL,"
                "time datetime)")
    print('ask_return table created done.')
    print('-'*30)
    print('operate done.')
    print('create database successful.')
except Exception as e:
    print('the require information of database is correct, please check it and retry.')
    print(e.args)
    import traceback
    traceback.print_exc()
    print('create database failed.')

print('Is insert some sample data into the database?')
print('1. insert')
print('2. exit')
insert_tag = input('please select the option:')
if insert_tag == '1':
    print('------------------------------------')
    print('starting the insert data operation...')
    admin_data = ['12644064935811ea9063d8c497639e37', 'admin', '21232f297a57a5a743894a0e4a801fc3', 0,
                  '2020-05-11 15:23:12', 0, '2020-05-11 15:24:23']
    user_data = ['99477a9e935811ea8171d8c497639e37', 'zhangsan', 'e10adc3949ba59abbe56e057f20f883e', 1,
                 '2020-05-11 15:23:12', 0, '2020-05-11 15:24:23']
    sql = 'insert into user (id, username, password, role, create_time, delete_flag, current_login_time) values(%s,%s,'\
          '%s,%s,%s,%s,%s)'
    cur.execute(sql, admin_data)
    cur.execute(sql, user_data)
    conn.commit()
    cur.close()
    conn.close()
    print('insert operation done.')
    print('------------------------------------')
    print('Now you can use admin account login with username="admin" password="admin" or use the normal account login'
          'with username="zhangsan" password="123456".')
else:
    print('system exit.')
