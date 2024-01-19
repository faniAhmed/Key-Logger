from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    text: str

@app.post("/process_data")
def process_data(item: Item):
    print(f"Received data: {item.text}")
    with open('keys.txt', 'a') as f:
        f.write(item.text)    
    return {"message": "Data processed successfully"}
