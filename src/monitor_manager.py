from typing import Dict, List
from uuid import uuid4
from models.product_check_response import ProductCheckResponse

monitor_data: Dict[str, List[ProductCheckResponse]] = {}

def create_monitor_job_id() -> str:
    return str(uuid4())

def save_result(job_id: str, result: ProductCheckResponse):
    monitor_data.setdefault(job_id, []).append(result)

def get_results(job_id: str) -> List[ProductCheckResponse]:
    return monitor_data.get(job_id, [])