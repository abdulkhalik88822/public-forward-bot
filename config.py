import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "26618097"))
    API_HASH = os.environ.get("API_HASH", "1154f54e18b67c1239f9674c643b7bcb")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6265513460:AAEVABfwA8nb-OamLRm_aTEzP9kUlsnvzos")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "5941212132")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://kailash:pass@cluster0.sqtztxm.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQG168YAggfSG726-n4jEMUx_GJsNkW8GZlSay2_YR5mYVn8mctQ0V75cjfPwj10xejYLXnCaGinrkk2L9_ILyGPHQryyy1pBmSClhKz5Kr4o9_DkAecrA9KR3DhEtoSZZ3qm4mbXLsgVJMqBKGCFkeEkajJJDQzN2VC-qkRSSOYFnXWnoLz1-u4WpdEQNyzHEGKuKJpXTVaXwIcjAdLAaAKc3Js5GYuqeu37-HYAKAK5PTiJl-lOuGHWuX9ba1XimoE2VyByizmgqf2TlKOTFnalCBk3Hq6M5m47_uzxqj1bkoHxmN-kZc-D7b15cOu-phnnLA6r-eJ1kb-_jH1zjrAVgbF8wAAAAFVZCN4AA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001569815531"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "Link_auto_filter_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
