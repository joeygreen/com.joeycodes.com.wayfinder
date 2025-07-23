import asyncio
from fastapi import BackgroundTasks, FastAPI
from monitor_manager import create_monitor_job_id, save_result, get_results
from models.product_request import ProductRequest
from application.product_service import check_product

app = FastAPI()

@app.post("/monitor")
async def monitor_url(
    url: str,
    interval: int,
    duration: int,
    background_tasks: BackgroundTasks
):
    job_id = create_monitor_job_id()
    product = ProductRequest(url=url)
    background_tasks.add_task(run_monitoring_task, job_id, product, interval, duration)
    return {"job_id": job_id}

@app.get("/monitor/{job_id}")
def fetch_monitor_results(job_id: str):
    return {"results": [r.model_dump() for r in get_results(job_id)]}

async def run_monitoring_task(job_id: str, product: ProductRequest, interval: int, duration: int):
    start_time = asyncio.get_event_loop().time()

    while (asyncio.get_event_loop().time() - start_time) < duration:
        result = check_product(product)
        save_result(job_id, result)
        await asyncio.sleep(interval)