import asyncio
import datetime
import os
from telegram import Bot

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = int(os.getenv("CHAT_ID"))

bot = Bot(token=BOT_TOKEN)

async def invia_sondaggio():
    domanda = "Estoy buscando marineros para zarpar ¿quién está conmigo?"
    opzioni = [
        "Le daré por la tarde",
        "Le daré por la tarde y por la noche",
        "Le daré por la noche",
        "Nada, hoy no puedo"
    ]
    await bot.send_poll(chat_id=CHAT_ID, question=domanda, options=opzioni, is_anonymous=False)

async def programma_sondaggi():
    while True:
        now = datetime.datetime.now()
        prossimo_invio = now.replace(hour=12, minute=0, second=0, microsecond=0)
        if prossimo_invio < now:
            prossimo_invio += datetime.timedelta(days=1)
        attesa = (prossimo_invio - now).total_seconds()
        await asyncio.sleep(attesa)
        await invia_sondaggio()

async def main():
    await programma_sondaggi()

if __name__ == '__main__':
    asyncio.run(main())
