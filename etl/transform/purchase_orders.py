def transform_purchase_order(purchase_order):
    return {
        "odoo_id": purchase_order["id"],
        "name": purchase_order["name"],
        "supplier_id": purchase_order["partner_id"],
        "order_date": purchase_order["date_order"],
        "state": purchase_order["state"],
        "amount_total": purchase_order["amount_total"],
        "custom_po_ref": purchase_order["custom_po_ref"],
        "ship_mode": purchase_order["ship_mode"],
        "approx_shipment_date": purchase_order["approx_shipment_date"],
        "approx_arrival_month": purchase_order["approx_arrival_month"],
        "vendor_code": purchase_order["vendor_code"],
        "payment_type": purchase_order["payment_type"],
        "invoice_no": purchase_order["invoice_no"],
        "pi_reference": purchase_order["pi_reference"],
        "user_id": purchase_order["user_id"],
        "company_id": purchase_order["company_id"],
        "currency_rate": purchase_order["currency_rate"],
        "shipments_count": purchase_order["shipments_count"],
    }


def transform_purchase_orders(purchase_orders):
    return [
        transform_purchase_order(purchase_order)
        for purchase_order in purchase_orders
    ]