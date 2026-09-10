from etl.connections import get_ai_connection


def load_purchase_orders(purchase_orders):
    connection = get_ai_connection()

    try:
        cursor = connection.cursor()
        # -----------------------------------
        # Build supplier mapping
        # Odoo supplier ID -> AI supplier ID
        # -----------------------------------
        cursor.execute("""
            SELECT id, odoo_id
            FROM suppliers
        """)

        supplier_map = {
            row[1]: row[0]
            for row in cursor.fetchall()
        }

        query = """
            INSERT INTO purchase_orders (
                odoo_id,
                name,
                supplier_id,
                order_date,
                state,
                amount_total,
                custom_po_ref,
                ship_mode,
                approx_shipment_date,
                approx_arrival_month,
                vendor_code,
                payment_type,
                invoice_no,
                pi_reference,
                user_id,
                company_id,
                currency_rate,
                shipments_count
            )
            VALUES (
                %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s
            )
            ON CONFLICT (odoo_id)
            DO UPDATE SET
                name = EXCLUDED.name,
                supplier_id = EXCLUDED.supplier_id,
                order_date = EXCLUDED.order_date,
                state = EXCLUDED.state,
                amount_total = EXCLUDED.amount_total,
                custom_po_ref = EXCLUDED.custom_po_ref,
                ship_mode = EXCLUDED.ship_mode,
                approx_shipment_date = EXCLUDED.approx_shipment_date,
                approx_arrival_month = EXCLUDED.approx_arrival_month,
                vendor_code = EXCLUDED.vendor_code,
                payment_type = EXCLUDED.payment_type,
                invoice_no = EXCLUDED.invoice_no,
                pi_reference = EXCLUDED.pi_reference,
                user_id = EXCLUDED.user_id,
                company_id = EXCLUDED.company_id,
                currency_rate = EXCLUDED.currency_rate,
                shipments_count = EXCLUDED.shipments_count
        """

        for purchase_order in purchase_orders:
            odoo_supplier_id = purchase_order["supplier_id"]
            # -----------------------------------
            # Convert Odoo supplier ID
            # to AI database supplier ID
            # -----------------------------------

            supplier_id = supplier_map.get(odoo_supplier_id)

            if supplier_id is None:
                print(
                    f"WARNING: Supplier with Odoo ID "
                    f"{odoo_supplier_id} not found. "
                    f"Skipping PO {purchase_order['odoo_id']}"
                )
                continue
            cursor.execute(
                query,
                (
                    purchase_order["odoo_id"],
                    purchase_order["name"],
                    supplier_id,
                    purchase_order["order_date"],
                    purchase_order["state"],
                    purchase_order["amount_total"],
                    purchase_order["custom_po_ref"],
                    purchase_order["ship_mode"],
                    purchase_order["approx_shipment_date"],
                    purchase_order["approx_arrival_month"],
                    purchase_order["vendor_code"],
                    purchase_order["payment_type"],
                    purchase_order["invoice_no"],
                    purchase_order["pi_reference"],
                    purchase_order["user_id"],
                    purchase_order["company_id"],
                    purchase_order["currency_rate"],
                    purchase_order["shipments_count"],
                ),
            )

        connection.commit()

        print(f"{len(purchase_orders)} purchase orders loaded successfully.")

    except Exception as e:
        connection.rollback()
        raise e

    finally:
        cursor.close()
        connection.close()