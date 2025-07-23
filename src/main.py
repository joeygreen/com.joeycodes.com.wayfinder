from typing import List
from application.scraper import fetch_html, check_availability
from models.product_request import ProductRequest

def main():
    figment_loungefly = ProductRequest(
            product_id="442098208713",
            product_description_string="figment-loungefly-mini-backpack",
        )
    daisy_loungefly = ProductRequest(
        product_id="671803539686",
        product_description_string="daisy-duck-85th-anniversary-loungefly-mini-backpack",
    )

    product_requests: List[ProductRequest] = [figment_loungefly, daisy_loungefly]

    for product in product_requests:
        print("---------------------------")
        print(f"Checking availability for: {product.product_description_string}\n")
        html = fetch_html(product.url)
        status = check_availability(html, product.css_selector)
        print(f"{status}")
        print("---------------------------\n")

if __name__ == "__main__":
    main()

