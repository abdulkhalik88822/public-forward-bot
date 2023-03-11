import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "23785747"))
    API_HASH = os.environ.get("API_HASH", "c77dded6cdf46494e51816511b9b1ece")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6265513460:AAEVABfwA8nb-OamLRm_aTEzP9kUlsnvzos")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "5941212132")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://abdul744:abdul744@cluster0.o6jx2be.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQAo-XsnEsVttqWORM6HcAZgi8gMyXQJFxST6qFmy0zzUjo6UPkY0HQQcz2KPtca1KAw8Ip-tvHTbTUQR2GmgTbG9Ezfr6k9MXjqnJTNWFCXvPp8045NIH5XEAI9XvTPVkx4P8EBtVTuVhgFGVFw7fINFN3x2Q6-KAVaFEK9wN52F035uSVf6b5dTdAqJ6BrtHkAamGkIXcGogSVM3jra_EjgOltAfXpLDyByNdzBAyf2TucIxZUhjfxPVWO0a_LrMI0irW8z86SkUlPChheOVf4VFue-DxgN6x2sPJ66MaVtUXt3-gllkLveVGn_YPCsYVBk5xREE1ebXZ6LZ8RaO83AAAAAWyu0rsA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "1626107740"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "5941212132")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
