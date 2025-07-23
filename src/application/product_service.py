from application.scraper import fetch_html, check_availability
from models.product_request import ProductRequest

def check_product(product: ProductRequest) -> dict:
    try:
        html = fetch_html(product.url)
        status = check_availability(html, product.css_selector)
        return {
            "product_id": product.product_id,
            "description": product.product_description_string,
            "url": product.url,
            "status": status
        }
    except Exception as e:
        return {
            "product_id": product.product_id,
            "description": product.product_description_string,
            "url": product.url,
            "error": str(e)
        }