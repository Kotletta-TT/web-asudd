import pymysql


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
        """add full nodes to real table"""
        connection = self.connect()
        try:
            query = "INSERT INTO nodes (name, type, latitude, longitude, ext_ip, vpn_ip, main_ip, status) VALUES (%s, " \
                    "%s, %s, %s, %s, %s, %s, %s);"
            with connection.cursor() as cur:
                cur.execute(query, (
                node.name, node.typenode, node.latitude, node.longitude, node.ext_ip, node.vpn_ip, node.main_ip,
                node.status))
                connection.commit()

        finally:
            connection.close()

    def get_node(self, name):
        """get node from database"""
        connection = self.connect()
        try:
            query = "SELECT * FROM nodes WHERE name=%s;"
            with connection.cursor() as cur:
                cur.execute(query, name)
                data = cur.fetchall()
                return data
        finally:
            connection.close()

    def get_all_nodes(self):
        """get all nodes from database"""
        connection = self.connect()
        try:
            query = "SELECT * FROM nodes;"
            with connection.cursor() as cur:
                cur.execute(query)
                data = cur.fetchall()
                return data
        finally:
            connection.close()

    def update_node(self, name, status):
        connection = self.connect()
        try:
            query = "UPDATE nodes SET status=%s WHERE name=%s;"
            with connection.cursor() as cur:
                cur.execute(query, (status, name))
                connection.commit()
        finally:
            connection.close()

            # def test_take_ip(self, name):
    #     """This test empty ip row and handling"""
    #     connection = self.connect()
    #     try:
    #         query = "SELECT ext_ip FROM nodes WHERE name=%s;"
    #         with connection.cursor() as cur:
    #             cur.execute(query, name)
    #             data = cur.fetchall()
    #             return data
    #     finally:
    #         connection.close()
    #
    # def test_add_ip(self, ip):
    #     """func from test_table, autofill table"""
    #     connection = self.connect()
    #     try:
    #         query = "INSERT INTO test_table (ip, status) VALUES (%s, %s);"
    #         with connection.cursor() as cur:
    #             cur.execute(query, (ip, "offline"))
    #             connection.commit()
    #     finally:
    #         connection.close()
    #
    # def test_update_status(self, ip, status):
    #     """Test update status to test_table (ip, status)"""
    #     connection = self.connect()
    #     try:
    #         query = "UPDATE test_table SET status=%s WHERE ip=%s;"
    #         with connection.cursor() as cur:
    #             cur.execute(query, (status, ip))
    #             connection.commit()
    #     finally:
    #         connection.close()

# list_ip = ['172.16.160.' + str(x) for x in range(1, 256)]
# db = DBHelper('localhost', 'webasudd', 'asudduser', 'asuddp@ss')
# db.test_update_status('172.16.160.1', 'online')
# def auto_fill():
#    for ip in list_ip:
#        print(ip)
#        a = db.test_add_ip(ip)
# auto_fill()
