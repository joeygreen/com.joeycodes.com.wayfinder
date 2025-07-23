from pydantic import BaseModel, computed_field

class ProductRequest(BaseModel):
    product_id: str
    product_description_string: str

    @computed_field
    @property
    def url(self) -> str:
        """Example Usage of properties: Constructs the product URL based on the product ID and description. This is totally unnecessary as you could just send the url in directly."""
        return f"https://www.disneystore.com/{self.product_description_string}-{self.product_id}.html"

    @computed_field
    @property
    def css_selector(self) -> str:
        return ".product-oos-info"