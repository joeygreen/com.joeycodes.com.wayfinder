from pydantic import BaseModel

class ProductCheckResponse(BaseModel):
    product_id: str | None = None
    description: str | None = None
    url: str
    status: str | None = None
    error: str | None = None