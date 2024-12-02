# main.py
from fastapi import FastAPI, BackgroundTasks, HTTPException
import database, schemas

app = FastAPI()

# Simulated email-sending function
def send_email_notification(item_name: str):
    from time import sleep
    for i in range(5, -1, -1):
        print(f'Sending email in {i} seconds...')
        sleep(i)
    print(f"Sending email: 'A new item \"{item_name}\" has been added to the inventory.'")

# Add an item to the dummy database and trigger a background task
@app.post("/items/", response_model=schemas.ItemResponse)
def add_item(item: schemas.ItemCreate, background_tasks: BackgroundTasks):
    # Simulate adding an item to the in-memory DB
    new_id = len(database.db) + 1
    new_item = database.Item(id=new_id, name=item.name, description=item.description)
    database.db.append(new_item)

    # Trigger background task for email notification
    background_tasks.add_task(send_email_notification, item.name)

    return new_item

# Retrieve all items from the dummy database
@app.get("/items/", response_model=list[schemas.ItemResponse])
def get_items():
    return database.db
