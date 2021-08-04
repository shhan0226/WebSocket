import os
import platform
import psutil
import time
import json
import asyncio
import websockets



'''CPU'''
# CPU Usage
cpu_usage_str = "%.1f" % (psutil.cpu_percent())
print(psutil.cpu_percent())

# CPU Model
# cpu_model_str = os.popen('cat /proc/cpuinfo | grep "model name" | uniq').read().split(':')[1].strip()

print('cpu_usage_str : ', cpu_usage_str)

'''MEM'''
mem_total_kilo = psutil.virtual_memory().total / 1024
mem_free_kilo = psutil.virtual_memory().free / 1024
mem_used_kilo = mem_total_kilo - mem_free_kilo

# MEM Total
mem_total_str = str(int(mem_total_kilo))
print(mem_total_str)

# MEM Used
mem_used_str = str(int(mem_used_kilo))

# MEM Usage
mem_usage_str = str(mem_used_kilo / mem_total_kilo)

print('mem_usage_str : ', mem_usage_str)

