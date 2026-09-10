from psycopg2.extras import RealDictCursor
from etl.connections import get_odoo_connection


def extract_purchase_order_lines(limit=None):
    connection = get_odoo_connection()

    try:
        cursor = connection.cursor(
            cursor_factory=RealDictCursor
        )

        query = """
            SELECT
                pol.id AS odoo_id,
                pol.order_id AS purchase_order_id,
                pol.product_id,
                pol.name,
                pol.product_qty AS quantity,
                pol.product_uom,
                pol.price_unit,
                pol.price_subtotal
            FROM purchase_po_line pol

            JOIN purchase_po po
                ON po.id = pol.order_id

            WHERE po.state != 'cancel'
        """

        if limit:
            query += " LIMIT %s"
            cursor.execute(query, (limit,))
        else:
            cursor.execute(query)

        return cursor.fetchall()

    finally:
        connection.close()