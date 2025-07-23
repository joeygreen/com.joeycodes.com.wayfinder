from pydantic import BaseModel, computed_field
from typing import Optional

class ProductRequest(BaseModel):
    product_id: Optional[str] = None
    product_description_string: Optional[str] = None
    url: Optional[str] = None

    @computed_field
    @property
    def computed_url(self) -> str:
        if self.url:
            return self.url
        if self.product_id and self.product_description_string:
            return f"https://www.disneystore.com/{self.product_description_string}-{self.product_id}.html"
        raise ValueError("Insufficient data to compute URL.")

    @computed_field
    @property
    def css_selector(self) -> str:
        return ".product-oos-info"