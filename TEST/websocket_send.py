import json
import asyncio
import websockets

URL_TEST = '192.168.0.173/ws/web/server_info/'
URL_VORA = '192.168.0.149/ws/server_infor/'




async def INPUT_Info():
    uri = "ws://"+ URL_TEST
    async with websockets.connect(uri) as websocket:
        text = input("Please input data : ")
        temp = {'message' : text }


        data_ = json.dumps(temp)
        await websocket.send(data_)        
        print(f"> {data_}")

        # greeting = await websocket.recv()
        # print(f"< {greeting}")


def Send_Info() :
    asyncio.get_event_loop().run_until_complete(INPUT_Info())



if __name__ == '__main__':
    while 1 :
        Send_Info()