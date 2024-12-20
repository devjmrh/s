import os
import asyncio
import logging
from config import Config
from pyrogram import Client
from rich.console import Console
from rich.table import Table
from HackSessionBot.Helpers.data import LOG_TEXT,ART
from pyromod import listen 
import sqlite3
conn = sqlite3.connect(":memory:")  # قاعدة بيانات في الذاكرة
#getting variables
API_ID = Config.API_ID
API_HASH = Config.API_HASH
TOKEN = Config.TOKEN
START_PIC = Config.START_PIC
CHAT = Config.CHAT


if not START_PIC:
    START_PIC = "7158379495:AAG4MmpxffHB5Rht9Twa6OL1NJEh1LobIas"

#rich
LOG = Console()

#logger
logging.basicConfig(level=logging.INFO)

#client
app = Client(
    "SupremeStark",
    api_id = API_ID,
    api_hash = API_HASH,
    bot_token = TOKEN )
    


async def HackSessionBot():
    os.system("clear")
    header = Table(show_header=True, header_style="bold green")
    header.add_column(LOG_TEXT)
    LOG.print(header)
    LOG.print(f"[bold cyan]{ART}")
    LOG.print("[bold yellow]تم عزيزي المواطن")
    await app.start()    
    


loop = asyncio.get_event_loop()
loop.run_until_complete(HackSessionBot())    



    
    

    
    



