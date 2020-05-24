#!/usr/bin/env python3

import time
from telethon import TelegramClient, events
import os, random
from dotenv import load_dotenv

load_dotenv() # get .env variable

session  = os.environ.get('TG_SESSION', 'printer')
api_id   = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
phone    = os.getenv("PHONE_NUM")
password = os.getenv("PASSWORD") #if you have 2FA enabled

session_file = 'ikanye'  # use your username if unsure

# content of the automatic reply
message = "SleepyKanye.jpg"

# choose random kanye picture from "pics" directory
def get_random_kanye_pic():
    randomPic = "./pics/"+random.choice(os.listdir("./pics"))
    #print("sending "+randomPic) #for debugging
    return randomPic
    


if __name__ == '__main__':
    # Create the client and connect
    # use sequential_updates=True to respond to messages one at a time
    client = TelegramClient(session_file, api_id, api_hash, sequential_updates=True)


    @client.on(events.NewMessage(incoming=True))
    async def handle_new_message(event):
        if event.is_private:  # only auto-reply to private chats
            from_ = await event.client.get_entity(event.from_id)  # this lookup will be cached by telethon
            if not from_.bot:  # don't auto-reply to bots
                print(time.asctime(), '-', event.message)  # optionally log time and message
                time.sleep(1)  # pause for 1 second to rate-limit automatic replies
                #await event.respond(file='pics/kanye.jpg')
                await event.respond(file=get_random_kanye_pic())


    print(time.asctime(), '-', 'Auto-replying...')
    client.start(phone, password)
    client.run_until_disconnected()
    print(time.asctime(), '-', 'Stopped!')


