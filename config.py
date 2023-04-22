import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "26618097"))
    API_HASH = os.environ.get("API_HASH", "1154f54e18b67c1239f9674c643b7bcb")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5967250731:AAHdc_fnsJlewcP9UdKOfGPG939oVOhMY60")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "5941212132")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://Abdul12:Abdul12@cluster0.o6jx2be.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQCDODin3B0FHaNp2oMGSjrUMYSOZmkXUwddly5P0nnKX5B5iD-kz-daZxdMu6wTxc6iIF0VSJVAkBS94EcAkk8L2TCKp5vhY2FDSW1mxwKwKNkfY56h7q4SSeySt3cxnp_DdoQyR53YoWeadbRS3lVdM2C38VvphFb1J57PbmCWalQaBG-78CUdhPInjzFSxL3TVPdqgD-VwueXaV2gAS83vIhX8VU7VOQp4OLh9B0skbCPQZcaL5qCprcN_2q7NDpWYpa5mPcRsG9inqfTRU9MPdxih9G0GMlpkHS2Zt0e3HpAzUBeEXOQ3SfErpyPMizFrRpHvxjSr39bv8FvETpEAAAAAV9RMh0A")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001887724395"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "Link_auto_filter_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
