import MySQLdb

class my_sql():
      def __init__(self,
                  ip,
                  user_name,
                  password,
                  database_name
                  ):
            self.db = MySQLdb.connect(
                  ip,
                  user_name,
                  password,
                  database_name
                  )
            # 创建游标
            self.cursor = self.db.cursor()
            pass
      # 采用execute执行语句
      def cmd(self,cmd):
            self.cursor.execute(cmd)
            pass

def main():
      first_sql = my_sql(
            ip="localhost",
            user_name="LHR",
            password="",
            database_name="runoob"
            )
      first_sql.cmd("SELECT VERSION();")
      data = first_sql.cursor.fetchone()
      print("database version {}".format(data))
      first_sql.cmd("SHOW TABLES;")
      data = first_sql.cursor.fetchone()
      print("database version {}".format(data))
      first_sql.db.close()
      return 

if __name__ == "__main__":
      main()
