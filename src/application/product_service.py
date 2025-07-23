from models.product_check_response import ProductCheckResponse
from models.product_request import ProductRequest
from application.scraper import check_availability, fetch_html

def check_product(product: ProductRequest) -> ProductCheckResponse:
    try:
        html = fetch_html(product.url)
        status = check_availability(html, product.css_selector)
        return ProductCheckResponse(
            product_id=product.product_id,
            description=product.product_description_string,
            url=product.url,
            status=status
        )
    except Exception as e:
        return ProductCheckResponse(
            product_id=product.product_id,
            description=product.product_description_string,
            url=product.url,
            error=str(e)
        )