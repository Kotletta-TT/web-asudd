import pymysql
import datetime

class DBHelper:

    def __init__(self, dbhost, dbname, dbuser, dbpassword):
        self.dbpassword = dbpassword
        self.dbuser = dbuser
        self.dbname = dbname
        self.dbhost = dbhost


    def connect(self):
        return pymysql.connect(host=self.dbhost,
                               user=self.dbuser,
                               password=self.dbpassword,
                               db=self.dbname)


    def add_node(self, node):
        connection = self.connect()
        try:
            query = "INSERT INTO nodes (name, type, lat, lng, addr, status, description) VALUES (%s, %s, %s, %s, %s, %s, %s);"
            with connection.cursor() as cur:
                cur.execute(query, (node.name, node.type, node.coord[0], node.coord[1], ','.join(node.addr), node.status, node.desc))
                connection.commit()
        finally:
            connection.close()

    def get_node(self, name):
       # node = []
        connection = self.connect()
        try:
            query = "SELECT * FROM nodes WHERE name=\'" + name + "\';"
            with connection.cursor() as cur:
                cur.execute(query)
                data = cur.fetchall()
                data = data[0]
                node = {
                    "name": data[1],
                    "type": data[2],
                    'coord': [data[3], data[4]],
                    'addr': data[5].split(","),
                    'status': data[6],
                    'desc': data[7]
                }
                return node
        finally:
            connection.close()

    def get_all(self):
        connection = self.connect()
        try:
            query = "SELECT * FROM nodes;"
            with connection.cursor() as cur:
                cur.execute(query)
                data = cur.fetchall()
                return data

        finally:
            connection.close()

