import qq
from config import appid, token
import logging

logging.basicConfig(level=logging.DEBUG)

client = qq.Client


@client.event
async def on_message(message: qq.Message):
    print(message.content)

@client.event
async def on_ready():
    print("机器人登录成功！")

if __name__ == '__main__':
   client.run(token=f"{appid}.{token}")