#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
import psutil

if __name__ == '__main__':
    status = True
    while status:
        var = input().encode("utf-8")
        if var == "cpu_percent":
            print(psutil.cpu_percent())
        elif var == "virtual_memory":
            print(psutil.virtual_memory().percent)

        time.sleep(0.1)
