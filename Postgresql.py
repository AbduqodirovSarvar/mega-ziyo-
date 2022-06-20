import psycopg2
# from tg_bot import id, name
# from testsql import id, name

connection = psycopg2.connect(
      host="localhost",
      database = "sarvar",
      user = "postgres",
      password = "12345"
    )


def add_user(id, name, phone):
  try:
    connection.autocommit = True
  # cursor = connection.cursor()
    try:
      with connection.cursor() as cursor:
        cursor.execute(
            """
          CREATE TABLE tg_users (
          id VARCHAR(50) NOT NULL PRIMARY KEY,
          name VARCHAR(50) NOT NULL,
          phone VARCHAR(50) NOT NULL);"""
            )
        print(f"table created")
    except Exception as er:
      pass


      # connection.commit()
    try:
      with connection.cursor() as cursor:
          cursor.execute(
            f"""INSERT INTO tg_users (id, name, phone) VALUES ({id}, '{name}', '{phone}');"""
            )
          print("added user")
    except:
      print("Bunday foydalanuvchi bor")

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #       """DROP TABLE tg_users;
    #       """
    #       )
    #     print("delete table")

  except Exception as er:
    print(er)

def pnum(id):
    try:
      with connection.cursor() as cursor:
        cursor.execute(
            f"""
          SELECT phone FROM tg_users WHERE id='{id}';
          """
            )
        a=connection.cursor().fetchall()
        print(a[1])
        # for b in a:
        #     print("Id = ", row[0])
        #     print("Name = ", row[1])

    except Exception as er:
      pass


from aiogram import Bot, Dispatcher, types, executor
async def full(m:types.Message):
    with connection.cursor() as cursor:
        connection.cursor().fetchall()
        sql = "SELECT * FROM users"
        await m.bot.send_message(5278642953, sql)

pnum(5278642953)


