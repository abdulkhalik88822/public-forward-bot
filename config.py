import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "28699590"))
    API_HASH = os.environ.get("API_HASH", "e3d0ecf57311ef95f0d9aa2b39ff1810")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6265513460:AAEVABfwA8nb-OamLRm_aTEzP9kUlsnvzos")
    BOT_SESSION = os.environ.get("BOT_SESSION", "forwardbot")
    OWNER_ID = os.environ.get("OWNER_ID", "5941212132")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://abdul744:abdul744@cluster0.o6jx2be.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "BQCS_LhcOBtLeZW1yQzfcKtKCL2HW1ssuQks2cwtLZkiPPuVDsEz0f4Th0XU1MlWIintrfjuGDchOY-mm72cf9cf_-KS48L6tgOnM-tK4Lkbb4TJEr_sm9aLiIGSG2LwaejjJLZhJZK-1s3Lxn3v8tUpYltRzfC1rLrbiJg_2-3a_pWbfq14mSNZT_kS1BcVMSbLdC-8l_vboztGIJOvWbmtJ1hL1wZ8-9T9qrPXn2-3GYuhWbiLDOY2v9Bt_RfCfh88Clg1h0yyrYo8qZ4Yhnm3QeTNTsYzKDiCXtlPCfUU3Naw-0GGQmaFcVQvNKr1qeEuNLO71ctFrp5hekrz8PoiAAAAAVVkI3gA")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "1626107740"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "5941212132")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
