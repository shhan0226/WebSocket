import json
import asyncio
import websockets
import psutil
import time
import os
import socket

URL_VORA = '192.168.0.146/ws/server_info/'


async def INPUT_Info():
    uri = "ws://"+ URL_VORA
    async with websockets.connect(uri) as websocket:        
        temp = {
            'type' : 'server_info',
            'message' : {
                'NIC' : nic_info_str,
                'CPU_USAGE' : cpu_usage_str,
                'MEM_USAGE' : mem_usage_str,
            }
        }


        data_ = json.dumps(temp)
        await websocket.send(data_)        
        print(f"> {data_}")


def Send_Info() :
    time.sleep(3)
    asyncio.get_event_loop().run_until_complete(INPUT_Info())
    



if __name__ == '__main__':
    while 1 :
        '''NETWORK'''
        physical_nics = []
        nic_info_str = []
        nics_info_str = []
        count = 0

        net_path = "/sys/class/net"


        nics = os.listdir(net_path)
        # print(nics)



        for i in nics:
            interface = os.path.join(net_path, i, "device")
            if os.path.exists(interface):
                physical_nics.append(i)
        
        nics = psutil.net_if_addrs()
        # print(nics)
    
        ip_ = ''
        mac_ = ''
        for nic in physical_nics:                
            for physical_nic in nics[nic]:

                if physical_nic.family == socket.AF_INET:                         
                    ip_ =  physical_nic.address

                if physical_nic.family == psutil.AF_LINK :            
                    mac_= physical_nic.address

            nic_info_str.append({
                "ip_str" : ip_,
                "mac_str" : mac_,

            })


        print('nics_info_str : ', nic_info_str)


        '''CPU'''
        # CPU Usage
        cpu_usage_str = "%.1f" % (psutil.cpu_percent())
        print('cpu_usage_str : ', cpu_usage_str)

        '''MEM'''
        mem_total_kilo = psutil.virtual_memory().total / 1024
        mem_free_kilo = psutil.virtual_memory().free / 1024
        mem_used_kilo = mem_total_kilo - mem_free_kilo
        # MEM Total
        mem_total_str = str(float(mem_total_kilo))
        # MEM Used
        mem_used_str = str(float(mem_used_kilo))
        # MEM Usage
        meme_usage = round( mem_used_kilo / mem_total_kilo * 100.0, 1)
        mem_usage_str = str(float(meme_usage)) 
        print('mem_usage_str : ', mem_usage_str)

        try:
            Send_Info()
        except Exception as e: 
            print(e)
        continue