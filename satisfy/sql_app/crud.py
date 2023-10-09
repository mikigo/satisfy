from sqlalchemy.orm import Session

from . import models
from . import schemas


def get_items(db: Session, item:schemas.ItemGet):
    return db.query(models.Item(**item.model_dump())).all()


def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
