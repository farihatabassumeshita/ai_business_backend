from psycopg2.extras import RealDictCursor

from etl.connections import get_odoo_connection


def extract_purchase_orders(limit=None):
    connection = get_odoo_connection()

    try:
        cursor = connection.cursor(
            cursor_factory=RealDictCursor
        )

        query = """
            SELECT
                po.id,
                po.name,
                po.partner_id,
                po.date_order,
                po.state,
                po.amount_total,
                po.custom_po_ref,
                po.ship_mode,
                po.approx_shipment_date,
                po.approx_arrival_month,
                po.vendor_code,
                rp.payment_type,
                po.invoice_no,
                po.pi_reference,
                po.user_id,
                po.company_id,
                po.currency_rate,
                po.shipments_count,
                po.order_type
            FROM purchase_po po
            LEFT JOIN res_company rc
                ON po.company_id = rc.id
            LEFT JOIN res_partner rp
                ON po.partner_id = rp.id
            WHERE po.state != 'cancel'
        """

        params = []
        
        if limit:
            query += " LIMIT %s"
            params.append(limit)

        cursor.execute(query, params)

        return cursor.fetchall()

    finally:
        connection.close()