import mariadb as db
import dbcreds


def connect_db():
    conn = None
    cursor = None
    try:
        conn = db.connect(user=dbcreds.user, password=dbcreds.password,
                          host=dbcreds.host, port=dbcreds.port, database=dbcreds.database)
        cursor = conn.cursor()
    except db.OperationalError:
        print("Something is wrong with the DB, please try again in 5 minutes")
    except:
        print("Something went wrong!")
    return conn, cursor


def disconnect_db(conn, cursor):
    try:
        cursor.close()
    except:
        print("The issue with cursor")
    try:
        conn.close()
    except:
        print("The issue with connection")


def list_all_candies():
    candies = []
    conn, cursor = connect_db()
    try:
        cursor.execute(
            "select id, name, description, image_url, quantity from candy")
        candies = cursor.fetchall()
    except db.OperationalError:
        print("Something is wrong with the DB, please try again in 5 minutes")
    except db.ProgrammingError:
        print("Error running DB query, please file bug report")
    except:
        print("Something went wrong!")
    disconnect_db(conn, cursor)
    return candies


def add_new_candy(name, description, image_url):
    new_candy = None
    conn, cursor = connect_db()
    try:
        cursor.execute(
            "insert into candy(name, description, image_url) values(?, ?, ?)", [name, description, image_url, ])
        conn.commit()
        if(cursor.rowcount == 1):
            new_candy = True
    except db.OperationalError:
        print("Something is wrong with the DB, please try again in 5 minutes")
    except db.ProgrammingError:
        print("Error running DB query, please file bug report")
    except:
        print("Something went wrong!")
    disconnect_db(conn, cursor)
    return new_candy


def update_candy(candy_id):
    success = None
    conn, cursor = connect_db()
    try:
        cursor.execute(
            "update candy set quantity = quantity + 1 where id = ?", [candy_id])
        conn.commit()
        if(cursor.rowcount == 1):
            success = True
    except db.OperationalError:
        print("Something is wrong with the DB, please try again in 5 minutes")
    except db.ProgrammingError:
        print("Error running DB query, please file bug report")
    except:
        print("Something went wrong!")
    disconnect_db(conn, cursor)
    return success


def delete_candy(candy_id):
    success = None
    conn, cursor = connect_db()
    try:
        cursor.execute(
            "delete from candy where id = ?", [candy_id])
        conn.commit()
        if(cursor.rowcount == 1):
            success = True
    except db.OperationalError:
        print("Something is wrong with the DB, please try again in 5 minutes")
    except db.ProgrammingError:
        print("Error running DB query, please file bug report")
    except:
        print("Something went wrong!")
    disconnect_db(conn, cursor)
    return success
