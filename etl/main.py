from etl.extract.products import extract_products
from etl.extract.suppliers import extract_suppliers
from etl.extract.customers import extract_customers
from etl.transform.products import transform_products
from etl.transform.suppliers import transform_suppliers
from etl.transform.customers import transform_customers
from etl.load.products import load_products
from etl.load.suppliers import load_suppliers
from etl.load.customers import load_customers


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


def main():
    # run_products_etl()
    run_suppliers_etl()
    run_customers_etl()


if __name__ == "__main__":
    main()