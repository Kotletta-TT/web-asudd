import csv
#from dbnode import DBHelper
#from node import Node
from app import db, Nodes


# db = DBHelper('localhost', 'webasudd', 'asudduser', 'asuddp@ss')

with open('nodes.csv' , newline='') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    for row in reader:
        node = Nodes(name=row[0], type=row[1], latitude=row[2], longitude=row[3], ext_ip=row[4], vpn_ip=row[5], main_ip=row[6], status=row[7])
        db.session.add(node)
        db.session.commit()
        db.session.close()