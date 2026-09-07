from etl.connections import get_ai_connection


def load_customers(customers):
    connection = get_ai_connection()

    try:
        cursor = connection.cursor()

        query = """
            INSERT INTO customers (
                odoo_id,
                name,
                customer_code,
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
                customer_code = EXCLUDED.customer_code,
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

        for customer in customers:
            cursor.execute(
                query,
                (
                    customer["odoo_id"],
                    customer["name"],
                    customer["customer_code"],
                    customer["phone"],
                    customer["country"],
                    customer["is_customer"],
                    customer["payment_type"],
                    customer["channel_sales"],
                    customer["partner_code"],
                    customer["distributor_type"],
                    customer["short_code"]
                ),
            )

        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()