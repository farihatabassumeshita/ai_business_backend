from etl.extract.products import extract_products
from etl.extract.suppliers import extract_suppliers
from etl.extract.customers import extract_customers
from etl.extract.purchase_orders import extract_purchase_orders
from etl.extract.purchase_order_lines import extract_purchase_order_lines
from etl.transform.products import transform_products
from etl.transform.suppliers import transform_suppliers
from etl.transform.customers import transform_customers
from etl.transform.purchase_orders import transform_purchase_orders
from etl.transform.purchase_order_lines import transform_purchase_order_lines
from etl.load.products import load_products
from etl.load.suppliers import load_suppliers
from etl.load.customers import load_customers
from etl.load.purchase_orders import load_purchase_orders
from etl.load.purchase_order_lines import load_purchase_order_lines


def run_products_etl():
    print("Starting products ETL...")
    products = extract_products()
    print(f"Extracted: {len(products)} products")
    products = transform_products(products)
    print(f"Transformed: {len(products)} products")
    load_products(products)
    print(f"Loaded: {len(products)} products")

def run_suppliers_etl():
    print("Starting suppliers ETL...")
    suppliers = extract_suppliers()
    print(f"Extracted: {len(suppliers)} suppliers")
    suppliers = transform_suppliers(suppliers)
    print(f"Transformed: {len(suppliers)} suppliers")
    load_suppliers(suppliers)
    print(f"Loaded: {len(suppliers)} suppliers")

def run_customers_etl():
    print("Starting customers ETL...")
    customers = extract_customers()
    print(f"Extracted: {len(customers)} customers")
    customers = transform_customers(customers)
    print(f"Transformed: {len(customers)} customers")
    load_customers(customers)
    print(f"Loaded: {len(customers)} customers")

def run_purchase_orders_etl():
    print("Starting purchase_orders ETL...")
    purchase_orders = extract_purchase_orders()
    print(f"Extracted: {len(purchase_orders)} purchase_orders")
    purchase_orders = transform_purchase_orders(purchase_orders)
    print(f"Transformed: {len(purchase_orders)} purchase_orders")
    load_purchase_orders(purchase_orders)
    print(f"Loaded: {len(purchase_orders)} purchase_orders")

def run_purchase_order_lines_etl():
    print("Starting purchase_order_lines ETL...")
    purchase_order_lines = extract_purchase_order_lines()
    print(f"Extracted: {len(purchase_order_lines)} purchase_order_lines")
    purchase_order_lines = transform_purchase_order_lines(purchase_order_lines)
    print(f"Transformed: {len(purchase_order_lines)} purchase_order_lines")
    load_purchase_order_lines(purchase_order_lines)
    print(f"Loaded: {len(purchase_order_lines)} purchase_order_lines")


def main():
    # run_products_etl()
    # run_suppliers_etl()
    # run_customers_etl()
    # run_purchase_orders_etl()
    run_purchase_order_lines_etl()


if __name__ == "__main__":
    main()