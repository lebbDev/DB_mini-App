import psycopg2


tables = {
    "restaurants": ["restaurant_id", "restaurant_name", "addres", "phone", "rating", "opening_time", "closing_time"],
    "chefs": ["chef_id", "restaurant_id", "chef_name", "chef_surname", "post", "salary", "experience_years"],
    "dishes": ["dish_id", "dish_name", "price", "presence", "restaurant_id"],
    "dishes_chefs": ["dish_id", "chef_id"],
    "ingredients": ["ingredient_id", "name", "quantity"],
    "ingredients_dishes": ["ingredient_id", "dish_id"]
}

def list_to_seq(ls):
    res = ''
    lenght = len(ls)
    for i in range(lenght - 1):
        res += ls[i] + ", "
    
    return res + ls[lenght - 1]

def insert_record(cursor, table, colums, values):
    cursor.execute("INSERT INTO %s (%s) VALUES (%s);"
                       % (table, colums, values)
        )

def delete_record(cursor, table, id_name, id):
    if isinstance(id_name, list):
        id_list = id.split(',')
        cursor.execute("DELETE FROM %s WHERE %s = %s AND %s = %s;" % (table, id_name[0], id_list[0], id_name[1], id_list[1]))
    else:   
        cursor.execute("DELETE FROM %s WHERE %s = %s;" % (table, id_name, id))

def update_record(cursor, table, column, new_value, id_name, id):
    if isinstance(id_name, list):
        id_list = id.split(',')
        cursor.execute("UPDATE %s SET %s = %s WHERE %s = %s AND %s = %s;" % (table, column, new_value, id_name[0], id_list[0], id_name[1], id_list[1]))
    else:
        cursor.execute("UPDATE %s SET %s = %s WHERE %s = %s;" % (table, column, new_value, id_name, id))

def get_one_record(cursor, table, id_name, id):
    if isinstance(id_name, list):
        id_list = id.split(',')
        cursor.execute("SELECT * FROM %s WHERE %s = %s AND %s = %s;" % (table, id_name[0], id_list[0], id_name[1], id_list[1]))
    else:
        cursor.execute("SELECT * FROM %s WHERE %s = %s;" % (table, id_name, id))
    return cursor.fetchone()

def get_all_records(cursor, table):
    cursor.execute("SELECT * FROM %s;" % (table))
    return cursor.fetchall()

def connect_db():
    try:
        connection = psycopg2.connect(
            host="localhost",
            port="5432",
            user="postgres",
            password="***********" ,
            database="restaurants",
        )
        print("Соединение с базой данных открыто")

        connection.autocommit = True
        cursor = connection.cursor()
        
        return [connection, cursor]
    except Exception as ex:
        print("ОШИБКА во время подключения к PostgreSQL:", ex)
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с базой данных закрыто")

def disconnect_db(connect):
    try:
        if connect[0]:
            connect[1].close()
            connect[0].close()
            print("Соединение с базой данных закрыто")
    except Exception as ex:
        print("ОШИБКА во время отключения от PostgreSQL:", ex)