def transform_supplier(supplier):
    return {
        "odoo_id": supplier["id"],
        "name": supplier["name"],
        "supplier_code": supplier["vendor_code"],
        "phone": supplier["phone"],
        "country": supplier["country"],
        "is_customer": supplier["is_customer"],
        "payment_type": supplier["payment_type"],
        "channel_sales": supplier["channel_sales"],
        "partner_code": supplier["partner_code"],
        "distributor_type": supplier["distributor_type"],
        "short_code": supplier["short_code"],
    }


def transform_suppliers(suppliers):
    return [
        transform_supplier(supplier)
        for supplier in suppliers
    ]