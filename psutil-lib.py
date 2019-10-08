#!/usr/bin/python3
# -*- coding: utf-8 -*-

import psutil
import sys
import time

if __name__ == '__main__':
    var = sys.argv[1]
    if var == "cpu_percent":
        psutil.cpu_percent()
        time.sleep(0.1)
        print(psutil.cpu_percent())
    elif var == "virtual_memory":
        print(psutil.virtual_memory().percent)
