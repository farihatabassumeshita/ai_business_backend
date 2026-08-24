from sqlalchemy.orm import Session

from ..models.product import Product

#Getting all product
def get_products(db: Session):
    return db.query(Product).all()

#Getting filter product
def get_product(db: Session, product_id: int):
    return (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )

#Create product
def create_product(db: Session, name: str, sku: str, price: float):
    product = Product(name=name, sku=sku, price=price)

    db.add(product)
    db.commit()
    db.refresh(product)

    return product

#Delete Product
def delete_product(db: Session, product_id: int):

    product = get_product(db, product_id)

    if product is None:
        return None

    db.delete(product)
    db.commit()

    return product