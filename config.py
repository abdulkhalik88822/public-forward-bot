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
    SESSION = os.environ.get("SESSION", "BQCb5jnX1x69kTAqq2uOD1vUGHxrmDc7M2TvlX5W47iWpbafIgPMLoP-LdPwPuVZDo74x-Lf3nFnr03xj4NlHIeSvbjqXZXDdVhnebAp5Y8AD7Msn2z1j3f9Fkjs8hn14_EBFyPYACly8O9_NfbBDtkZtIur7uwkeR76_JuL2KqopoPHt3R59JbtacC8uMT2LqvtyvKtBvQm7bB3Z7RgMmsvKaYmF2QmUMTr0zZmNlAogFMDMD5o7V8KawSrS4eImbu9jF6CiQ8RAPyYKUxPyx6zBMc_0w1ygOB-Mf45JqxQZSlwPcyLYi6M1xmhUilHIHa0SNOMckGzcVeHv7RNLU-rAAAAAWyu0rsA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1001887724395"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "Auto_forword_dd_bot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
