from etl.connections import get_ai_connection


def load_products(products):
    connection = get_ai_connection()

    try:
        cursor = connection.cursor()

        query = """
            INSERT INTO products (
                odoo_id,
                name,
                product_code,
                price,
                pack_size
            )
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (odoo_id)
            DO UPDATE SET
                name = EXCLUDED.name,
                product_code = EXCLUDED.product_code,
                price = EXCLUDED.price,
                pack_size = EXCLUDED.pack_size,
                updated_at = CURRENT_TIMESTAMP
        """

        for product in products:
            cursor.execute(
                query,
                (
                    product["odoo_id"],
                    product["name"],
                    product["product_code"],
                    product["price"],
                    product["pack_size"]
                ),
            )

        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()