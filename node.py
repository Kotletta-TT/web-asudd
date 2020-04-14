import os

class Node:

    def __init__(self, name: str, typenode: str, coord: list, addr: list, status: str, desc=None):
        self.stat = ["down", "down", "down"]
        self.name = name
        self.type = typenode
        self.coord = coord
        self.addr = addr
        self.status = status
        self.desc = desc

    def ping(self, ip):
        ping = f"ping -c 3 {ip} > /dev/null"
        return os.system(ping)

    def stats(self):
        self.stat = []
        for ip in self.addr:
            if self.ping(ip) == 0:
                self.stat.append("up")
            else:
                self.stat.append("down")

    def check_status(self):
        if "down" in self.stat:
            self.status = "offline"
        else:
            self.status = "online"



    def take_screenshot(self):
        if self.type == "cam":
            pass





vk01 = Node("vk01", "cam", ['43.581482', '39.722635'], ['31.173.192.49', '10.10.20.101', '172.30.100.254'], "online")


