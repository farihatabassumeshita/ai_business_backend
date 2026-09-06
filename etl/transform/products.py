def transform_product(product):
    return {
        "odoo_id": product["id"],
        "name": product["name"],
        "product_code": product["default_code"],
        "price": product["list_price"],
        "pack_size": product["pack_size_ferrero"],
    }


def transform_products(products):
    return [
        transform_product(product)
        for product in products
    ]