class ProductRequest:
    def __init__(self, product_id, product_description_string):
        self.url = f"https://www.disneystore.com/{product_description_string}-{product_id}.html"
        self.css_selector = ".product-oos-info"
        self.product_id = product_id
        self.product_description_string = product_description_string

    def __repr__(self):
        return f"ProductRequest(product_id={self.product_id}, quantity={self.quantity}, request_date={self.request_date})"