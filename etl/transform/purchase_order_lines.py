def transform_purchase_order_line(purchase_order_line):
    return{
            "odoo_id": purchase_order_line["odoo_id"],
            "purchase_order_id": purchase_order_line["purchase_order_id"],
            "product_id": purchase_order_line["product_id"],
            "name": purchase_order_line["name"],
            "quantity": purchase_order_line["quantity"],
            "unit_price": purchase_order_line["price_unit"],
            "subtotal": purchase_order_line["price_subtotal"],
        }

def transform_purchase_order_lines(purchase_order_lines):
    return [
        transform_purchase_order_line(purchase_order_line)
        for purchase_order_line in purchase_order_lines
    ]