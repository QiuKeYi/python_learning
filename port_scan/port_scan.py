# -*- coding:utf-8 -*-
# author: qky
# time : 2018年4月23日 00:12:25
# function: 端口扫描工具()

import sys
import threading,queue
import time
import socket
import ipaddress

Ports = (21,22,23,25,80,81,88,90,91,8000,8001,8080,8081,8888,9090,9000,9001,9090)   #此处放置端口列表


class PortScan(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self._queue = queue

    def run(self):
        while True:
            if self._queue.empty():
                break
            try:
                ip = str(self._queue.get(timeout=0.5))
                for port in Ports:
                    addr = (ip,port)
                    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                    try:
                        s.settimeout(0.3)
                        s.connect(addr)
                        print("%s:%d"%(ip,port))
                    except:
                        s.close()
                        continue
            except:
                continue


def main():
    threads = []
    thread_count = 5
    task_queue = queue.Queue()

    ip_seg = input("请输入扫描网段：")
    IPS = ipaddress.IPv4Network(ip_seg)
    for ip in IPS:
        task_queue.put(ip)

    for i in range(thread_count):
        threads.append(PortScan(task_queue))

    for t in threads:
        t.start()

    for t in threads:
        t.join()


if __name__ == "__main__":
    time_start = time.time()
    main()
    print("时间消耗："+str(time.time()-time_start))
