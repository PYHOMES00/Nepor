import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7498735093:AAEaO6EvPML6g0M-MIrrPvorv6CvRWWFfas")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "28243586"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "4022d5686b9b7a7cf8891205921a0ab3")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://madarazbotz:riVNFzoBGQlnkmEA@cluster0.4nx2vpf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

#PICS
PICS = (os.environ.get('PICS', 'https://telegra.ph/file/f69ffb788e27be2d60e84.jpg https://telegra.ph/file/531109a51df28b01d5822.jpg https://telegra.ph/file/4ff2445eb814758548b52.jpg')).split() # Bot Start Picture
