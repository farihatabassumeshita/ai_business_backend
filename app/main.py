from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import engine, Base, get_db
from . import models
from .schemas import ProductCreate, ProductResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/products", response_model=ProductResponse)
def create_product(product: ProductCreate,db: Session = Depends(get_db)):
    new_product = models.Product(name=product.name,sku=product.sku,price=product.price)

    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@app.get("/products")
def get_all_product(db: Session = Depends(get_db)):
    products = (db.query(models.Product)).all()
    return products


@app.get("/products/{product_id}")
def get_product(product_id: int,db: Session = Depends(get_db)):
    product = (db.query(models.Product).filter(models.Product.id == product_id).first())
    if product is None:
        return {"message": "Product not found"}
    return product

@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = (db.query(models.Product)).filter(models.Product.id == product_id).first()
    if product is None:
        return {"message" : "Product Not found"}
    db.delete(product)
    db.commit()
    return {"message" : "Product deleted Successfully"}