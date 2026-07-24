from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
from typing import List, Dict
import asyncio
import uuid
from datetime import datetime, timedelta
import uvicorn
 
app = FastAPI()

# in-memory db
orders_db: Dict[str, dict] = {}

class OrderItem(BaseModel):
    name: str
    quantity: int
    price: float

class Order(BaseModel):
    id: str
    items: List[OrderItem]
    total: float
    status: str  # "pending", "paid", "canceled"
    created_at: datetime

class CreateOrderRequest(BaseModel):
    items: List[OrderItem]

@app.post("/orders", response_model=Order)
def create_order(order_request: CreateOrderRequest):
    order_id = str(uuid.uuid4())
    total = sum(item.quantity * item.price for item in order_request.items)
    new_order = {
        "id": order_id,
        "items": order_request.items,
        "total": total,
        "status": "pending",
        "created_at": datetime.utcnow(),
    }
    
    orders_db[order_id] = new_order
    return new_order

@app.get("/orders", response_model=List[Order])
def list_orders():
    return list(orders_db.values())

@app.get("/orders/{order_id}", response_model=Order)
def get_order(order_id: str):
    order = orders_db.get(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return order

async def process_payment(order_id: str):
    await asyncio.sleep(5)  # Simulates processing time
    
    order = orders_db.get(order_id)
    if order and order["status"] == "pending":
        order["status"] = "paid"

@app.put("/orders/{order_id}/cancel")
def cancel_order(order_id: str):
  order = orders_db.get(order_id)
  if not order:
      raise HTTPException(status_code=404, detail="Order not found")
  if order and order["status"] != "pending": 
       raise HTTPException(status_code=400, detail="Order couldnt be cancel")
  order["status"] = "cancel"
  return {"message": "Payment cancel successly"}
  
@app.post("/orders/{order_id}/pay")
def pay_order(order_id: str, background_tasks: BackgroundTasks):
    order = orders_db.get(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    if order["status"] != "pending":
        raise HTTPException(status_code=400, detail="Order couldnt be paid")

    background_tasks.add_task(process_payment, order_id)
    return {"message": "Payment process has started"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)