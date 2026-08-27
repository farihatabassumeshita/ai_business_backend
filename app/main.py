from fastapi import FastAPI

from .database import Base, engine
from .routes.product_routes import router as product_router
from .routes.document_routes import router as document_router

from .models.product import Product
from .models.document import Document

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(product_router)
app.include_router(document_router)


@app.get("/")
def root():

    return {
        "message": "API is running"
    }