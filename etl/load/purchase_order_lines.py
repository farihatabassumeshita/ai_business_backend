from etl.connections import get_ai_connection


def load_purchase_order_lines(purchase_order_lines):
    connection = get_ai_connection()

    try:
        cursor = connection.cursor()

        query = """
            INSERT INTO purchase_order_lines (
                odoo_id,
                purchase_order_id,
                product_id,
                name,
                quantity,
                unit_price,
                subtotal
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s)

            ON CONFLICT (odoo_id)
            DO UPDATE SET
                purchase_order_id = EXCLUDED.purchase_order_id,
                product_id = EXCLUDED.product_id,
                quantity = EXCLUDED.quantity,
                name = EXCLUDED.name,
                unit_price = EXCLUDED.unit_price,
                subtotal = EXCLUDED.subtotal
        """

        for line in purchase_order_lines:
             # -----------------------------------
            # 1. Get AI database Purchase Order ID
            # -----------------------------------
            cursor.execute(
                """
                SELECT id
                FROM purchase_orders
                WHERE odoo_id = %s
                """,
                (line["purchase_order_id"],)
            )

            purchase_order_result = cursor.fetchone()
            if not purchase_order_result:
                print(
                    f"Skipping line {line['odoo_id']}: "
                    f"Purchase Order Odoo ID "
                    f"{line['purchase_order_id']} not found"
                )
                continue

            purchase_order_id = purchase_order_result[0]
             # -----------------------------------
            # 2. Get AI database Product ID
            # -----------------------------------
            cursor.execute(
                """
                SELECT id
                FROM products
                WHERE odoo_id = %s
                """,
                (line["product_id"],)
            )

            product_result = cursor.fetchone()

            if not product_result:
                print(
                    f"Skipping line {line['odoo_id']}: "
                    f"Product Odoo ID "
                    f"{line['product_id']} not found"
                )
                continue

            product_id = product_result[0]

            cursor.execute(
                query,
                (
                    line["odoo_id"],
                    purchase_order_id,
                    product_id,
                    line["name"],
                    line["quantity"],
                    line["unit_price"],
                    line["subtotal"],
                )
            )

        connection.commit()

    finally:
        connection.close()