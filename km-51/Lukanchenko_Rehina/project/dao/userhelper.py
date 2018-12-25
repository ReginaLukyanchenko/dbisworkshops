import cx_Oracle
from dao.dbCredentials import *


class User:
    def __init__(self):
        self.__db = cx_Oracle.connect(username, password, databaseName)
        self.__cursor = self.__db.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__cursor.close()
        self.__db.close()

    def authorization(self, p_login, p_password):
        status = self.__cursor.var(cx_Oracle.STRING)
        self.__cursor.callproc("user_package.authorization", [status, p_login, p_password])
        return status.values[0]

    def register(self, p_id_code, p_last_name, p_first_name,  p_email, p_login, p_password):
        status = self.__cursor.var(cx_Oracle.STRING)
        self.__cursor.callproc("user_package.registration", [status, p_id_code, p_last_name, p_first_name,
                                                      p_login, p_password, p_email])
        return status.values[0]

    def get_user(self, p_login):
        query = 'select * from table(user_package.get_user(:login))'
        self.__cursor.execute(query, login=p_login)
        user = self.__cursor.fetchall()
        return user[0]

    def update(self, p_id_code, p_last_name, p_first_name, p_email, p_login):
        status = self.__cursor.var(cx_Oracle.STRING)
        self.__cursor.callproc("user_package.edit_user_info", [status, p_id_code, p_last_name, p_first_name, p_email,
                                                               p_login, None, None])
        return status.values[0]

    def update_password(self, p_id_code, p_old_password, p_new_password):
        status = self.__cursor.var(cx_Oracle.STRING)
        self.__cursor.callproc("user_package.edit_user_info", [status, p_id_code, None, None, None,
                                                               None, p_old_password, p_new_password])
        return status.values[0]


class Group:
    def __init__(self):
        self.__db = cx_Oracle.connect(username, password, databaseName)
        self.__cursor = self.__db.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__cursor.close()
        self.__db.close()

    def get_groups(self):
        query = 'select * from table(group_package.get_groups)'
        self.__cursor.execute(query)
        groups = self.__cursor.fetchall()
        return groups

    def get_student_group(self, p_group_id):
        query = 'select * from table(student_package.get_student_group(:group_id))'
        self.__cursor.execute(query, group_id=p_group_id)
        group = self.__cursor.fetchall()
        return group

    def get_group(self, p_group_id):
        query = 'select * from table(group_package.get_group(:group_id))'
        self.__cursor.execute(query, group_id=p_group_id)
        group = self.__cursor.fetchall()
        return group


class Discipline:
    def __init__(self):
        self.__db = cx_Oracle.connect(username, password, databaseName)
        self.__cursor = self.__db.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__cursor.close()
        self.__db.close()

    def get_disciplines(self):
        query = 'select * from table(discipline_package.get_disciplines)'
        self.__cursor.execute(query)
        disciplines = self.__cursor.fetchall()
        return disciplines

    def get_discipline(self, p_discipline_id):
        query = 'select * from table(discipline_package.get_discipline(:discipline_id))'
        self.__cursor.execute(query, discipline_id=p_discipline_id)
        discipline = self.__cursor.fetchall()
        return discipline

