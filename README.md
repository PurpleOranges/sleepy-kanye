Telegram "bot" that will auto-reply to messages with pictures of sleeping kanye when you are AFK. Based on [Telethon]


When you recieve a message, the bot will randomly select a file from the `pics` directory to reply with.

# Setup
Edit the `.env` file with your information. You can get your "API_ID" and "API_HASH" from https://my.telegram.org/

# Running
run the bot on a computer that will stay online.

```bash
python3 ./sleepy-kanye.py
```
to activate "sleep mode" type `!sleep` into a telegram chat.

to deactivate sleep mode, type `!wake`


![alt text](pics/chair.jpg)




[Telethon]: https://github.com/LonamiWebs/Telethon




credit
------

i stole some code from here: 
https://gist.github.com/yi-jiayu/acc31fbad5a25f746430428ce4d62c28
