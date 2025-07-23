from pydantic import BaseModel

class ProductCheckResponse(BaseModel):
    product_id: str
    description: str
    url: str
    status: str | None = None
    error: str | None = None