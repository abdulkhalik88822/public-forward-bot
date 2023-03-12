import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "23785747"))
    API_HASH = os.environ.get("API_HASH", "c77dded6cdf46494e51816511b9b1ece")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6265513460:AAEVABfwA8nb-OamLRm_aTEzP9kUlsnvzos")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "5941212132")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Abdul12:Abdul12@cluster0.o6jx2be.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQBf4zKtsfs99UCht1XMEcIFZEkGGDfhiHuMmAa8oOa59RnAEzRfrrj9zV3s0qCssTzgozmbJFnhVLpymamy6-JLCIV0SrQT9qdA8ZjIAYjWIn_lN6M7yAysItJKcQfMUraAHWG03o4pRNSBD4zeMyrPO16ktDMzlB0mLIUGQ7S3v5WLzVVlW8z9Rm3DWlNJ8y9fKJBpuZ6WxDdcaPvc33cWlZk0MoQ5quJH0lNQemk2K2VohBzSQSk9hNVdSX0HaZoLbJe30vZyKanDFqT6oCWMbItgbenvB-e1oTpTi6OzKHMK10JRa_Ib9lwTvOP_xUzL3SmRfZ2yiEF_gocl39ksAAAAAWyu0rsA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001626107740"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "Auto_forword_dd_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
