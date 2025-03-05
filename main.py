from telethon import TelegramClient, events
from telethon.tl.functions.account import UpdateProfileRequest
from datetime import datetime, timedelta, timezone
import asyncio

API_ID = "28045735"
API_HASH = "f1eb1969ff9a1f9c8b8bbbbb752cb7ae"
Phone = "+998938100804"

client = TelegramClient("Akmaljon", API_ID, API_HASH)

async def update_nickname():
    while True:
        now = datetime.now(timezone.utc) + timedelta(hours=5, minutes=0.55)
        new_name = f" 𝗥𝗼𝘁𝗮𝘁𝘂𝘆  | {now.strftime('%H:%M')} | "
        try:
            await client(UpdateProfileRequest(first_name=new_name))
            print(f"Nik yangilandi: {new_name}")
        except Exception as e:
            print(f"Xatolik: {e}")
        await asyncio.sleep(60)

responses = {
    "Nima gap ukam": "raxmat tinchu oʻzizdachi",
    "nima gap": "raxmat tinchu oʻzizdachi",
    "pubgga kiryapsimi": "yo vaht bolmayapti aka(uka)",
    "qales": "zoʼr xudoga shukur",
    "qalisiz": "zoʼr xudoga shukur",
    "Cal off dutyga qachon oʻynemiz": "vaqt bolmayaptida oʻqshla bn",
    "Akmaljon uka yaxshimisz": "xa raxmat aka xudoga shukur",
    "rasmga olib tashlavoring": "xop xaliroq",
    "rasm": "xop xaliroq tashlavoraman",
    "Clashga kiryapsimi": "xa bazida",
    "qaydasan": "tinchlikmi axr",
    "ha tinchlik": "xaa",
    "qachon kelasan": "aniqmas"
}

@client.on(events.NewMessage)
async def message_handler(event):
    if event.is_private:
        me = await client.get_me()
        if event.sender_id != me.id:
            text = event.raw_text.lower()
            

            if text.startswith('/del'):

                await client.delete_messages(event.chat_id, [event.id])
                return
            
            for question, answer in responses.items():
                if text.strip() == question.lower():
                    await event.reply(answer)
                    break


        
        
        @client.on(events.NewMessage(pattern="/bot"))
        async def start_handler(event):
            if event.is_private:
                await event.reply("Bot Ishga tushdi va ishlamoqda ")
        
        
@client.on(events.NewMessage(pattern="/del"))
async def delete_messages(event):
    if event.is_private:
        responses = []
        async for message in client.iter_messages(event.chat_id, from_user=None):
            responses.append(message)
            try:
                await client.delete_messages(event.chat_id, message.id, revoke=True)
            except Exception as e:
                print(f"Xabar o‘chirishda xatolik: {e}")
        for response in responses:
            try:
                await client.delete_messages(event.chat_id, response.id, revoke=True)
            except Exception as e:
                print(f"Error ! < / > ")
        await event.reply("")

print("Userbot ishga tushdi...")

with client:
    client.loop.create_task(update_nickname())
    client.run_until_disconnected()
