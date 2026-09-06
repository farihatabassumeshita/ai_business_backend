import os

from dotenv import load_dotenv


load_dotenv()


ODOO_DB_CONFIG = {
    "host": os.getenv("ODOO_DB_HOST"),
    "port": os.getenv("ODOO_DB_PORT", "5432"),
    "dbname": os.getenv("ODOO_DB_NAME"),
    "user": os.getenv("ODOO_DB_USER"),
    "password": os.getenv("ODOO_DB_PASSWORD"),
}


AI_DB_CONFIG = {
    "host": os.getenv("AI_DB_HOST"),
    "port": os.getenv("AI_DB_PORT", "5432"),
    "dbname": os.getenv("AI_DB_NAME"),
    "user": os.getenv("AI_DB_USER"),
    "password": os.getenv("AI_DB_PASSWORD"),
}