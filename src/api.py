from fastapi import FastAPI
from typing import List
from models.product_request import ProductRequest
from application.product_service import check_product

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Wayfinder Scraper API is running"}

@app.post("/check")
def check_multiple_products(products: List[ProductRequest]):
    return {"results": [check_product(p) for p in products]}