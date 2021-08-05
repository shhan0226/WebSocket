import os
import psutil
import time
import socket

import requests, json

import asyncio
import websockets

'''NETWORK'''

physical_nics = []
nic_info_str = []
net_path = "/sys/class/net"
nics = os.listdir(net_path)

# print("==============================[NICS]")
# print(nics)


for i in nics:
    interface = os.path.join(net_path, i, "device")
    if os.path.exists(interface):
        physical_nics.append(i)

# print("==============================[physical_nics]")
# print(physical_nics)


nics = psutil.net_if_addrs()

# print("==============================[NICS]")
# print(nics)


print("=================================================")
for nic in physical_nics:    
    for i in nics[nic]:
        if i.family == socket.AF_INET:                         
            nic_info_str.append( {
                'ip_str' : i.address,
            })
        elif i.family == psutil.AF_LINK :            
            nic_info_str.append( {
                'mac_str': i.address.replace(':','').upper(),
            })

print(nic_info_str)
             
            




    #     if i.family == psutil.AF_LINK :
    #         print(i)



# data0 = psutil.net_io_counters(pernic=True)
# start = time.time()
# time.sleep(2)
# data1 = psutil.net_io_counters(pernic=True)
# end = time.time()
# diff = end - start

# for nic in physical_nics:
#     for i in nics[nic]:
#         if i.family == psutil.AF_LINK:
#             nic_info_str.append({
#                                     'name_str': nic,
#                                     'mac_str': i.address.replace(':','').upper(),
#                                     'rx_kbps_str': str(int((data1[nic][1] - data0[nic][1]) / diff / 1024)),
#                                     'tx_kbps_str': str(int((data1[nic][0] - data0[nic][0]) / diff / 1024)),
#                                 })

# nic_count_str = str(len(physical_nics))

# print(nic_info_str)
# print(nic_count_str)




# '''CPU'''
# # CPU Usage
# cpu_usage_str = "%.1f" % (psutil.cpu_percent())

# print(cpu_usage_str)

# # CPU Model
# # cpu_model_str = os.popen('cat /proc/cpuinfo | grep "model name" | uniq').read().split(':')[1].strip()
# # print(cpu_model_str)



# '''MEM'''
# mem_total_kilo = psutil.virtual_memory().total / 1024
# mem_free_kilo = psutil.virtual_memory().free / 1024
# mem_used_kilo = mem_total_kilo - mem_free_kilo

# # MEM Total
# mem_total_str = str(int(mem_total_kilo))

# print(mem_total_str)


# # MEM Used
# mem_used_str = str(int(mem_used_kilo))

# print(mem_used_str)



# URL = 'ws://192.168.0.138/ws/server_infor'
# #data = { 'message' : {'test' : 'test'} }
# #res = requests.post(URL, data=json.dumps(data))
# #print(res)



# async def hello():
#     # uri = "ws://localhost:8765"
#     async with websockets.connect(URL) as websocket:
#         await websocket.send("Hello world!")
#         # await websocket.recv()

# asyncio.get_event_loop().run_until_complete(hello())





print("END ...")