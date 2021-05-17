from telethon import functions, types
from telethon.sync import TelegramClient
from telethon import TelegramClient, events, sync
import configparser
from ast import literal_eval as make_list


config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')
api_id = int(config['cfg']['api_id'])
api_hash = config['cfg']['api_hash']
channels = make_list(config['cfg']['channels'])

client = TelegramClient('telegram', api_id, api_hash)
client.start()
@client.on(events.NewMessage())
async def normal_handler(event):
    for channel in channels:
        print(event)
        if(event.chat_id == channel[0]):
            await client.send_message(channel[1], event.message)


client.run_until_disconnected()

