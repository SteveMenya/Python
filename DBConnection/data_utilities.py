import errno
import os
from _datetime import datetime
from time import strftime

import pymysql

from DBConnection.constant import YEAR_MONTH_DAY


def execute_statement(statement_to_execute, my_list_data=None, select=True, insert=True):
    """
    Returns a result
    :param my_list_data:
    :param insert:
    :param select:
    :param statement_to_execute: the statement to be executed
    :return: results from execution
    """
    try:
        with database_connection() as my_db_connection:
            with my_db_connection.cursor() as cursor:
                if select:
                    cursor.execute(statement_to_execute)
                    my_db_connection.commit()
                    return cursor.fetchall()
                if insert and my_list_data is not None:
                    cursor.executemany(statement_to_execute, my_list_data)
                    my_db_connection.commit()
                return cursor.lastrowid
    except pymysql.err.OperationalError:
        return 'Issue occured'

    finally:
        (print('done'))


def database_connection():
    try:
        return pymysql.connect(user=os.environ.get('DATABASE_USERNAME'),
                               database=os.environ.get('DATABASE'),
                               password=os.environ.get('DATABASE_PASSWORD'),
                               port=3306)

        # return cnx
    except pymysql.err.OperationalError as err:
        print(err)
        if err.errno == errno.EAGAIN:
            print("Something is wrong with your user name or password")
        elif err.errno == errno.EWOULDBLOCK:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()


def get_all_employees():
    """
    gets all employees from the practice database
    :return a result from query: A
    """

    statement = 'SELECT * FROM employees;'
    return execute_statement(statement)


def print_schema_old_table(connection):
    for (tableName,) in connection.execute(
            """
            select NAME from SQLITE_MASTER where TYPE='table' order by NAME;
            """
    ):
        print("{}:".format(tableName))
        for (
                columnID, columnName, columnType,
                columnNotNull, columnDefault, columnPK,
        ) in connection.execute("pragma table_info('{}');".format(tableName)):
            print("  {id}: {name}({type}){null}{default}{pk}".format(
                id=columnID,
                name=columnName,
                type=columnType,
                null=" not null" if columnNotNull else "",
                default=" [{}]".format(columnDefault) if columnDefault else "",
                pk=" *{}".format(columnPK) if columnPK else "",
            ))


def create_employee_backup():
    """

    :return: table name
    """
    statement = """
    CREATE TABLE IF NOT EXISTS `employees_backup` (
  `id` int NOT NULL AUTO_INCREMENT,
  `em_name` varchar(255) NOT NULL,
  `gender` char(1) NOT NULL,
  `contact_number` varchar(255) DEFAULT NULL,
  `salary` float NOT NULL,
  `years_in_company` int NOT NULL,
  `date_created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
    """
    execute_statement(statement)
    return 'employees_backup'


def drop_table():
    """
    Drops a db table
    :return: t or false
    """

    statement = """
    DROP table IF exists EMPLOYEES_BACKUP;
    """
    return execute_statement(statement)


def insert_data_to_back_up_table(table_name, tuple_data):
    """
    Inserts the data into table name provided
    :param tuple_data:
    :param table_name:
    :return:
    """
    my_list_data = []
    for row in tuple_data:
        my_list_data.append(row)
    statement = f"Insert into {table_name} values (%s,%s,%s,%s,%s,%s,%s);"
    return execute_statement(statement, my_list_data, select=False)
    # db_connection.commit()


def convert_date_time_for_mysql(the_date):
    """

    :param the_date:
    :return:
    """
    the_new_date = datetime.strptime(str(the_date), YEAR_MONTH_DAY)
    print(the_new_date)
    return the_new_date
