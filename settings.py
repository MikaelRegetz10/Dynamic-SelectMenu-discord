from dotenv import load_dotenv
import os

load_dotenv()

ID_SERVER = os.getenv('ID_SERVER')
TOKEN_DISCORD = os.getenv('TOKEN_DISCORD')
DB_HOST = os.getenv('DB_HOST')
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
