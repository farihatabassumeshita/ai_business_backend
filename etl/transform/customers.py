def transform_customer(customer):
    return {
        "odoo_id": customer["id"],
        "name": customer["name"],
        "customer_code": customer["vendor_code"],
        "phone": customer["phone"],
        "country": customer["country"],
        "is_customer": customer["is_customer"],
        "payment_type": customer["payment_type"],
        "channel_sales": customer["channel_sales"],
        "partner_code": customer["partner_code"],
        "distributor_type": customer["distributor_type"],
        "short_code": customer["short_code"],
    }


def transform_customers(customers):
    return [
        transform_customer(customer)
        for customer in customers
    ]