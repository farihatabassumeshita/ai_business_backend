from psycopg2.extras import RealDictCursor

from etl.connections import get_odoo_connection


def extract_products(limit=None):
    connection = get_odoo_connection()

    try:
        cursor = connection.cursor(
            cursor_factory=RealDictCursor
        )

        query = """
            SELECT
                pp.id,
                pt.name,
                pp.default_code,
                pt.list_price,
                pt.pack_size_ferrero
            FROM product_product pp
            JOIN product_template pt
                ON pp.product_tmpl_id = pt.id
            WHERE pp.active = TRUE
        """

        params = []

        if limit:
            query += " LIMIT %s"
            params.append(limit)

        cursor.execute(query, params)

        products = cursor.fetchall()

        print("EXTRACTED PRODUCTS:", len(products))

        return products

    finally:
        connection.close()