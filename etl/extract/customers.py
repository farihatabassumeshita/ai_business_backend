from psycopg2.extras import RealDictCursor

from etl.connections import get_odoo_connection


def extract_customers(limit=None):
    connection = get_odoo_connection()

    try:
        cursor = connection.cursor(
            cursor_factory=RealDictCursor
        )

        query = """
            SELECT
                rp.id,
                rp.name,
                rp.vendor_code,
                rp.phone,
                rc.name AS country,
                rp.is_customer,
                rp.payment_type,
                rp.channel_sales,
                rp.partner_code,
                dp.distributor_type,
                dp.short_code
            FROM res_partner rp
            LEFT JOIN res_country rc
                ON rp.country_id = rc.id
            LEFT JOIN distributor_type dp
                ON rp.distributor_type = dp.id
            WHERE rp.active = TRUE
                AND rp.is_customer = TRUE
        """

        params = []

        if limit:
            query += " LIMIT %s"
            params.append(limit)

        cursor.execute(query, params)

        return cursor.fetchall()

    finally:
        connection.close()