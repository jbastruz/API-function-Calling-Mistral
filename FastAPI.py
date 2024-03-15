import csv
from typing import Annotated
from datetime import date
from fastapi import FastAPI, HTTPException, Depends, APIRouter
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from typing import List

app = FastAPI(title="FastAPI")

tags_metadata = [
    {
        "name": "Public",
        "description": "API pour les transactions"
    },
    {
        "name": "Admin Access",
        "description": "API pour les utilisateurs"
    }
]

class Transaction(BaseModel):
    transaction_id: str
    customer_id: str
    payment_amount: float
    payment_date: date
    payment_status: str

# Define a basic authentication scheme
security = HTTPBasic()

correct_username = "your_username"
correct_password = "your_password"

# Define a function to check the credentials
async def authenticate(credentials: HTTPBasicCredentials):
    global username, password
    if credentials.username == correct_username and credentials.password == correct_password:
        return True
    else:
        return False
    
def read_csv(file_name: str) -> List[Transaction]:
    with open(file_name, mode='r') as file:
        reader = csv.DictReader(file)
        items = [Transaction(**row) for row in reader]
    return items

def write_csv(file_name: str, items: List[Transaction]):
    with open(file_name, mode='w', newline='') as file:
        fieldnames = ['transaction_id','customer_id','payment_amount','payment_date','payment_status']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in items:
            writer.writerow(item.model_dump())

@app.get('/Transaction', response_model=List[Transaction], tags=["Public"])
def get_items():
    items = read_csv('items.csv')
    return items

@app.get('/Transaction/count', response_model=int, tags=["Admin Access"])
async def get_items_count(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    if not await authenticate(credentials):
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    items = read_csv('items.csv')
    return len(items)

@app.get('/Transaction/max', response_model=Transaction, tags=["Public"])
def get_items_max():
    items = read_csv('items.csv')
    return max(items, key=lambda item: item.payment_amount)

@app.get('/Transaction/min', response_model=Transaction, tags=["Public"])
def get_items_min():
    items = read_csv('items.csv')
    return min(items, key=lambda item: item.payment_amount)

@app.get('/Transaction/{item_id}', response_model=Transaction, tags=["Public"])
def get_item(item_id: str):
    items = read_csv('items.csv')
    item = next((item for item in items if item.transaction_id == item_id), None)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.post('/Transaction/create', tags=["Admin Access"])
async def create_item(item: Transaction, credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    if not await authenticate(credentials):
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    items = read_csv('items.csv')
    items.append(item)
    write_csv('items.csv', items)
    return {'message': 'Item created successfully'}

@app.put('/Transaction/{item_id}', tags=["Admin Access"])
async def update_item(item_id: str, item: Transaction, credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    if not await authenticate(credentials):
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    items = read_csv('items.csv')
    done = False
    for i, item in enumerate(items):
        if item.transaction_id == item_id:
            items[i] = item
            done = True
            break
    write_csv('items.csv', items)

    if not done:
        raise HTTPException(status_code=404, detail="Item not found")

    return {'message': 'Item updated successfully'}

@app.delete('/Transaction/{item_id}', tags=["Admin Access"])
async def delete_item(item_id: str, credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    if not await authenticate(credentials):
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    items = read_csv('items.csv')
    items = [item for item in items if item.transaction_id != item_id]
    write_csv('items.csv', items)
    return {'message': 'Item deleted successfully'}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)