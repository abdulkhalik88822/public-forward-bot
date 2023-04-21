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
    SESSION = os.environ.get("SESSION", "BQCcVKrUXOUoFwF-0ZiBRPNlslEFFDPkZ8COLTJ9fe2ffvahC46DXRNdqS9ghgh1uFJxtN1j3fLgkYeXvwZ-htr233DfgDrA7y94eoyeQu321PgQ87xoGSH-Jd3TWYjox11hDgYQ5vneVZYEW4s3VJeJulWNFtfhU-whP5u1hRtE_o-f8jhLwkVef8hYdC3P0tleyZuIfmQroAuz2hdgjdsB6AlzG5zP6va3f6dDo2D3LZkljgvlIcqnzyXwm89JuB-wcBwTusX_OzPI5bkU8bNYQ52taidaptfYFFM4b1kMhTP1iru0q6arbwY1znGT8phxdc15bq0axxlsPLJi0koKAAAAATK48jYA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001887724395"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "Link_auto_filter_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
