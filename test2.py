import os
import time
from threading import Thread
from db import DBHelper

# import csv


db = DBHelper('localhost', 'webasudd', 'asudduser', 'asuddp@ss')


class MyThread(Thread):
    """
    A threading example
    """

    def __init__(self, node):
        """Инициализация потока"""
        Thread.__init__(self)
        self.node = node

    def run(self):
        """Запуск потока"""
        ping_list = []
        if len(self.node[5]) > 0:
            ping_list.append(os.system(f"ping -c 3 {self.node[5]} > /dev/null"))
        if len(self.node[6]) > 0:
            ping_list.append(os.system(f"ping -c 3 {self.node[6]} > /dev/null"))
        if len(self.node[7]) > 0:
            ping_list.append(os.system(f"ping -c 3 {self.node[7]} > /dev/null"))
        if sum(ping_list) > 0:
            db.update_node(self.node[1], 'offline')
        else:
            db.update_node(self.node[1], 'online')
            # print(f'{self.ip} -- up')
            # db.test_update_status(self.ip, status)
        # else:
        #     status = 'offline'
        # print(f'{self.ip} -- down')
        # db.test_update_status(self.ip, status)
        # return status


class Node:
    """Needed to create object Node"""

    def __init__(self, name, typenode, latitude, longitude,
                 ext_ip, vpn_ip, main_ip, status):
        self.stat = ["down", "down", "down"]
        self.name = name
        self.typenode = typenode
        self.latitude = latitude
        self.longitude = longitude
        self.ext_ip = ext_ip
        self.vpn_ip = vpn_ip
        self.main_ip = main_ip
        self.status = status


# def create_threads():
#     """
#     Создаем группу потоков
#     """
#     list_ip = ['172.16.160.' + str(x) for x in range(1, 255)]
#     for ip in list_ip:
#         my_thread = MyThread(ip)
#         my_thread.start()


# def run(ip):
#     """Запуск потока"""
#     ping = os.system(f"ping -c 3 {ip} > /dev/null")
#     if ping == 0:
#         print(f'{ip} -- up')
# else:
#     print(f'{ip} -- down')


# def csv_to_db():
#     """need start at once, to add all nodes(csv-format) in database"""
#     with open('nodes.csv', newline='') as csv_file:
#         reader = csv.reader(csv_file, delimiter=',')
#         for row in reader:
#             print(row)
#             node = Node(name=row[0], typenode=row[1], latitude=row[2], longitude=row[3], ext_ip=row[4], vpn_ip=row[5],
#                          main_ip=row[6], status=row[7])
#             print(node)
#             db.add_node(node)


if __name__ == "__main__":
    nodes = list(db.get_all_nodes())
    while True:
        for node in nodes:
            ping_thread = MyThread(node)
            ping_thread.start()
        time.sleep(60)
