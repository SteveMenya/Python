import errno
import os

import pymysql


def execute_statement(statement_to_execute):
    """
    Returns a result
    :param statement_to_execute: the statement to be executed
    :return: results from execution
    """
    try:
        with database_connection() as my_db_connection:
            with my_db_connection.cursor() as cursor:
                cursor.execute(statement_to_execute)
                my_db_connection.commit()
                return cursor.fetchall()
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
