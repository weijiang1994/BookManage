"""
coding:utf-8
file: dbutil.py
@author: jiangwei
@contact: jiangwei_1994124@163.com
@time: 2020/5/9 20:03
@desc:
"""
import pymysql


class DBHelp:
    instance = None

    def __init__(self, host='127.0.0.1', port=3306, user='root', pwd='1994124', db='book', charset='utf8'):
        self._conn = pymysql.connect(host=host, port=port, user=user, passwd=pwd, db=db, charset=charset)
        self._cur = self._conn.cursor()

    @classmethod
    def get_instance(cls):
        if cls.instance:
            return cls.instance
        else:
            cls.instance = DBHelp()
            return cls.instance

    def query_all(self, table_name):
        sql = 'select * from {}'.format(table_name)
        count = self._cur.execute(sql)
        res = self._cur.fetchall()
        return count, res

    def query_super(self, table_name, column_name, condition):
        sql = "select * from {} where {}='{}'".format(table_name, column_name, condition)
        count = self._cur.execute(sql)
        res = self._cur.fetchall()
        return count, res

    def add_user(self, data):
        sql = "insert into user (id, username, password, role, create_time, delete_flag, current_login_time) " \
              "values (%s, %s, %s, %s, %s, %s, %s)"
        self._cur.execute(sql, data)

    def add_book(self, data):
        sql = "insert into book (id, book_name,author,publish_company,store_number,borrow_number,create_time," \
              "publish_date) values (%s, %s, %s, %s, %s, %s, %s, %s)"
        self._cur.execute(sql, data)

    def update_super(self, table_name, column_name, condition, data):
        sql = "update {} set book_name='{}', author='{}', publish_company='{}',  publish_date='{}', store_number={}" \
              " where {}='{}'".format(table_name, data[0], data[1], data[2], data[3], data[4], column_name, condition)
        self._cur.execute(sql)

    def delete(self, table_name, column_name, condition):
        sql = "delete from {} where {}='{}'".format(table_name, column_name, condition)
        self._cur.execute(sql)

    def update_borrow(self, book_id):
        sql = "update book set store_number=store_number-1 where id='{}'".format(book_id)
        self._cur.execute(sql)
        sql = "update book set borrow_number=borrow_number+1 where id='{}'".format(book_id)
        self._cur.execute(sql)

    def update_borrow_statue(self, book_id):
        sql = "update borrow_info set return_flag=1 where id='{}'".format(book_id)
        self._cur.execute(sql)

    def insert_borrow_info(self, data):
        sql = "insert into borrow_info (id, book_id, book_name, borrow_user, borrow_num, borrow_days, borrow_time," \
              "return_time, return_flag) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self._cur.execute(sql, data)

    def db_commit(self):
        self._conn.commit()

    def db_rollback(self):
        self._conn.rollback()
