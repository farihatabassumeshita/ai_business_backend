from etl.extract.products import extract_products
from etl.transform.products import transform_products
from etl.load.products import load_products


def run_products_etl():
    print("Starting products ETL...")

    products = extract_products()

    print(f"Extracted: {len(products)} products")

    products = transform_products(products)

    print(f"Transformed: {len(products)} products")

    load_products(products)

    print(f"Loaded: {len(products)} products")


def main():
    run_products_etl()


if __name__ == "__main__":
    main()