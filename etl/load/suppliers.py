from etl.connections import get_ai_connection


def load_suppliers(suppliers):
    connection = get_ai_connection()

    try:
        cursor = connection.cursor()

        query = """
            INSERT INTO suppliers (
                odoo_id,
                name,
                supplier_code,
                phone,
                country,
                is_customer,
                payment_type,
                channel_sales,
                partner_code,
                distributor_type,
                short_code
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)

            ON CONFLICT (odoo_id)
            DO UPDATE SET
                name = EXCLUDED.name,
                supplier_code = EXCLUDED.supplier_code,
                phone = EXCLUDED.phone,
                country = EXCLUDED.country,
                is_customer = EXCLUDED.is_customer,
                payment_type = EXCLUDED.payment_type,
                channel_sales = EXCLUDED.channel_sales,
                partner_code = EXCLUDED.partner_code,
                distributor_type = EXCLUDED.distributor_type,
                short_code = EXCLUDED.short_code,
                updated_at = CURRENT_TIMESTAMP
        """

        for supplier in suppliers:
            cursor.execute(
                query,
                (
                    supplier["odoo_id"],
                    supplier["name"],
                    supplier["supplier_code"],
                    supplier["phone"],
                    supplier["country"],
                    supplier["is_customer"],
                    supplier["payment_type"],
                    supplier["channel_sales"],
                    supplier["partner_code"],
                    supplier["distributor_type"],
                    supplier["short_code"]
                ),
            )

        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()