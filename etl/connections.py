import psycopg2

from etl.config import ODOO_DB_CONFIG, AI_DB_CONFIG


def get_odoo_connection():
    return psycopg2.connect(**ODOO_DB_CONFIG)


def get_ai_connection():
    return psycopg2.connect(**AI_DB_CONFIG)