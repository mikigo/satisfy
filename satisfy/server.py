import os

import uvicorn
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def hello():
    return {"msg": "hello mikigo"}


@app.get("/get_center/", response_model=schemas.Item)
def read_items(item: schemas.ItemGet, db: Session = Depends(get_db)):
    items = crud.get_items(db=db, item=item)
    # TODO
    return items


@app.post("/create_items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    res = crud.create_item(db=db, item=item)
    return res


if __name__ == '__main__':
    uvicorn.run(
        app="server:app",
        host=os.popen("hostname -I").read().split(" ")[0],
        port=5000,
        reload=True
    )
