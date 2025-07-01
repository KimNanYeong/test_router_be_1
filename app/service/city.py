import pymysql
from app.db.connect import (
    get_db_connection,
    close_connection,
    close_cursor,
    commit,
    rollback,
)

def get_city(city_id: int) -> str:
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        select_query = "SELECT city_name FROM city WHERE city_id = %s;"
        cursor.execute(select_query, (city_id,))
        result = cursor.fetchone()

        if result:
            return result[0]
        else:
            return 0
    except Exception as e:
        rollback(connection)
        print(f"get_city_id:{e}")
    finally:
        close_cursor(cursor)
        close_connection(connection)

